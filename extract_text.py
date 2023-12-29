import requests
from bs4 import BeautifulSoup
import json
import re

# スクレイピングしたいウェブサイトのURL
url = 'https://www.artificialintelligence-news.com/2023/12/19/ai-big-data-expo-maximising-value-real-time-data-streams/'

# ウェブサイトからHTMLを取得
response = requests.get(url)
html = response.content

# BeautifulSoupオブジェクトの作成
soup = BeautifulSoup(html, 'html.parser')

# JSONデータを含むscriptタグを探す
script_tag = soup.find('script', type='application/ld+json')

# JSONデータの抽出と前処理
if script_tag:
    # 改行やタブなどの制御文字を削除
    cleaned_json = re.sub(r'\s+', ' ', script_tag.string)

    # JSONデータの解析
    json_data = json.loads(cleaned_json)
    article_body = json_data.get("articleBody", "本文が見つかりません。")
    print(article_body)
else:
    print("JSONデータが見つかりません。")