---
layout: default
title: ブロックチェーンキャッチアップ
---

# ブロックチェーンキャッチアップ

ブロックチェーン関連ニュースを毎日収集し、ビジネス視点で深読みしたレポートをまとめています。

---

## レポート

{% assign summaries = site.pages | where_exp: "page", "page.path contains 'Summary/'" | where_exp: "page", "page.name != 'index.md'" | sort: "path" | reverse %}
{% for page in summaries limit:3 %}
{% assign parts = page.path | split: '/' %}
- [{{ parts[1] }}.{{ parts[2] }}.{{ page.name | replace: '.md', '' | split: '-' | last }}]({{ page.url | relative_url }})
{% endfor %}

[過去のレポートを見る →](./Summary/)
