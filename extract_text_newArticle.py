import requests
from bs4 import BeautifulSoup
import json
import re

# ニュースページのURL
news_page_url = 'https://aismiley.co.jp/ai_news/'
#news_page_url = 'https://kuretom.com'

# ニュースページからHTMLを取得
response = requests.get(news_page_url)
html = response.content

# BeautifulSoupオブジェクトの作成
soup = BeautifulSoup(html, 'html.parser')

# JSONデータを含むscriptタグを探す
script_tag = soup.find('script', type='application/ld+json')

# 最新の記事のURLとタイトルを取得
if script_tag:
    # 改行やタブなどの制御文字を削除
    cleaned_json = re.sub(r'\s+', ' ', script_tag.string)

    # JSONデータの解析
    json_data = json.loads(cleaned_json)
    url = json_data.get("mainEntityOfPage", {}).get("@id", "")
    title = json_data.get("headline", "タイトルが見つかりません。")

    if url:
        print(f"最新の記事のURL: {url}")
        print(f"最新の記事のタイトル: {title}")

        # ここで最新の記事のURLから本文を取得
        response = requests.get(url)
        html = response.content
        soup = BeautifulSoup(html, 'html.parser')

        # JSONデータを含むscriptタグを探す
        script_tag = soup.find('script', type='application/ld+json')
        if script_tag:
            cleaned_json = re.sub(r'\s+', ' ', script_tag.string)
            json_data = json.loads(cleaned_json)
            article_body = json_data.get("articleBody", "本文が見つかりません。")
            print(article_body)
        else:
            print("記事ページのJSONデータが見つかりません。")

    else:
        print("最新の記事のURLが見つかりません。")

else:
    print("ニュースページのJSONデータが見つかりません。")
