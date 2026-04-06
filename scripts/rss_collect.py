#!/usr/bin/env python3
"""ブロックチェーン専門RSSフィードから記事を収集し、Raw/フォルダにMarkdownとして保存する"""

import os
import re
import xml.etree.ElementTree as ET
from urllib.request import urlopen, Request
from urllib.error import URLError
from datetime import datetime, timedelta, timezone
from html.parser import HTMLParser

JST = timezone(timedelta(hours=9))

# ブロックチェーン専門サイト（全記事取得）
BLOCKCHAIN_FEEDS = [
    "https://nft-times.jp/feed/",
    "https://jba-web.jp/feed/",
    "https://gaiax-blockchain.com/feed/",
    "https://blockchain-biz-consulting.com/media/feed/",
    "https://www.neweconomy.jp/feed/",
    "https://crypto-times.jp/feed/",
]

# イベント系記事を除外するキーワード
EXCLUDE_KEYWORDS = [
    "セミナー", "ウェビナー", "ワークショップ", "受付開始", "申込",
    "参加者募集", "開催決定", "開催のお知らせ", "登壇",
]

NS = {
    "atom": "http://www.w3.org/2005/Atom",
    "dc": "http://purl.org/dc/elements/1.1/",
    "content": "http://purl.org/rss/1.0/modules/content/",
    "rss1": "http://purl.org/rss/1.0/",
}


def strip_html(text: str) -> str:
    return re.sub(r"<[^>]+>", "", text).strip()


def fetch_full_article(url: str) -> str:
    """記事URLから全文を取得する。取得できない場合は空文字を返す。"""
    try:
        req = Request(url, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        })
        with urlopen(req, timeout=15) as resp:
            raw = resp.read()
            content_type = resp.headers.get("Content-Type", "")
            charset = None
            if "charset=" in content_type:
                charset = content_type.split("charset=")[-1].strip().split(";")[0]
            if not charset:
                head = raw[:2000].decode("ascii", errors="replace")
                m = re.search(r'charset=["\']?([^"\'\s;>]+)', head, re.IGNORECASE)
                if m:
                    charset = m.group(1)
            charset = charset or "utf-8"
            try:
                html = raw.decode(charset, errors="replace")
            except (LookupError, UnicodeDecodeError):
                html = raw.decode("utf-8", errors="replace")
    except (URLError, Exception):
        return ""

    article_match = re.search(r"<article[^>]*>(.*?)</article>", html, re.DOTALL)
    if article_match:
        text = strip_html(article_match.group(1))
        if len(text) > 200:
            return text[:10000]

    paragraphs = re.findall(r"<p[^>]*>(.*?)</p>", html, re.DOTALL)
    if paragraphs:
        text = "\n\n".join(strip_html(p) for p in paragraphs if len(strip_html(p)) > 30)
        if len(text) > 200:
            return text[:10000]

    for pattern in [
        r'<div[^>]*class="[^"]*(?:article|entry|post|content|main)[^"]*"[^>]*>(.*?)</div>',
    ]:
        match = re.search(pattern, html, re.DOTALL | re.IGNORECASE)
        if match:
            text = strip_html(match.group(1))
            if len(text) > 200:
                return text[:10000]

    return ""


def is_recent(pub_date: str, hours: int = 48) -> bool:
    """公開日時が指定時間以内かどうか判定。ブロックチェーン系は更新頻度が低いので48時間に設定。"""
    if not pub_date:
        return True
    now = datetime.now(timezone.utc)
    cutoff = now - timedelta(hours=hours)

    for fmt in [
        "%a, %d %b %Y %H:%M:%S %z",
        "%a, %d %b %Y %H:%M:%S %Z",
        "%Y-%m-%dT%H:%M:%S%z",
        "%Y-%m-%dT%H:%M:%SZ",
        "%Y-%m-%d %H:%M:%S%z",
        "%Y-%m-%d",
    ]:
        try:
            dt = datetime.strptime(pub_date.strip(), fmt)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=JST)
            return dt >= cutoff
        except ValueError:
            continue
    return True


def safe_filename(title: str) -> str:
    name = re.sub(r'[\\/:*?"<>|]', "", title)[:80].strip()
    return name if name else "untitled"


def get_text(el, default=""):
    if el is not None and el.text:
        return el.text.strip()
    return default


def fetch_feed(url: str) -> str:
    try:
        req = Request(url, headers={"User-Agent": "Mozilla/5.0 RSS Collector"})
        with urlopen(req, timeout=15) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except (URLError, Exception) as e:
        print(f"  取得失敗: {e}")
        return ""


def parse_feed(content: str) -> list:
    items = []
    try:
        root = ET.fromstring(content)
    except ET.ParseError:
        return items

    for item in root.findall(".//item"):
        title = get_text(item.find("title"))
        link = get_text(item.find("link"))
        desc = get_text(item.find("description"))
        content_el = item.find("content:encoded", NS)
        body = get_text(content_el) if content_el is not None else desc
        pub = get_text(item.find("pubDate")) or get_text(item.find("dc:date", NS))
        if title and link:
            items.append((title, link, desc, body, pub))

    for item in root.findall("rss1:item", NS):
        title = get_text(item.find("rss1:title", NS))
        link = get_text(item.find("rss1:link", NS))
        desc = get_text(item.find("rss1:description", NS))
        pub = get_text(item.find("dc:date", NS))
        if title and link:
            items.append((title, link, desc, desc, pub))

    for entry in root.findall("atom:entry", NS):
        title = get_text(entry.find("atom:title", NS))
        link_el = entry.find("atom:link", NS)
        link = link_el.get("href", "") if link_el is not None else ""
        desc = get_text(entry.find("atom:summary", NS))
        content_el = entry.find("atom:content", NS)
        body = get_text(content_el) if content_el is not None else desc
        pub = get_text(entry.find("atom:published", NS)) or get_text(
            entry.find("atom:updated", NS)
        )
        if title and link:
            items.append((title, link, desc, body, pub))

    return items


def main():
    os.makedirs("Raw", exist_ok=True)

    now = datetime.now(JST)
    today_str = now.strftime("%Y-%m-%d")

    index_lines = [
        f"# ブロックチェーンRSS収集 {today_str}",
        "",
        f"収集日時: {now.strftime('%Y-%m-%d %H:%M JST')}",
        "",
        "---",
        "",
    ]

    total = 0
    seen_titles = set()

    for feed_url in BLOCKCHAIN_FEEDS:
        print(f"取得中: {feed_url}")
        content = fetch_feed(feed_url)
        if not content:
            continue

        items = parse_feed(content)
        print(f"  → {len(items)}件取得")

        for title, link, desc, body, pub in items:
            if not is_recent(pub):
                continue
            if any(kw in title for kw in EXCLUDE_KEYWORDS):
                continue
            if title in seen_titles:
                continue
            seen_titles.add(title)

            fname = safe_filename(title)
            filepath = f"Raw/{fname}.md"

            if os.path.exists(filepath):
                continue

            clean_desc = strip_html(desc)[:500]
            clean_body = strip_html(body)[:3000]

            if len(clean_body) < 500 and link:
                print(f"    全文取得中: {link[:60]}...")
                full_text = fetch_full_article(link)
                if full_text:
                    article_text = full_text
                else:
                    article_text = clean_body if clean_body else clean_desc
            else:
                article_text = clean_body if clean_body else clean_desc

            with open(filepath, "w", encoding="utf-8") as f:
                f.write("---\n")
                f.write(f'title: "{title}"\n')
                f.write(f'source: "{link}"\n')
                f.write(f"published: {pub}\n")
                f.write("tags:\n  - blockchain\n")
                f.write("---\n\n")
                f.write(article_text)
                f.write("\n")

            index_lines.append(f"### {title}")
            index_lines.append(f"- URL: {link}")
            index_lines.append(f"- 概要: {clean_desc[:200]}")
            index_lines.append("")

            total += 1

    index_lines.append("---")
    index_lines.append(f"合計: {total} 件")

    with open("Raw/index.md", "w", encoding="utf-8") as f:
        f.write("\n".join(index_lines))

    print(f"\n合計記事数: {total}")


if __name__ == "__main__":
    main()
