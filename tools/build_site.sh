#!/bin/sh
# Cloudflare Pages 用：公開するファイルだけを dist/ に集める（content/ data/ tools/ などは出さない）
set -e
cd "$(dirname "$0")/.."
rm -rf dist && mkdir -p dist
cp *.html *.js *.css *.png manifest.webmanifest sitemap.xml dist/
cp -r blog dist/
[ -f robots.txt ] && cp robots.txt dist/ || true
echo "dist/ に $(find dist -type f | wc -l) ファイル"
