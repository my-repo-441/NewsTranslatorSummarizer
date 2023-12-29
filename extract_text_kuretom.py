import requests
from bs4 import BeautifulSoup

# スクレイピングしたいウェブサイトのURL
#url = 'https://www.kuretom.com/aws-all-cert/'
url = 'https://www.artificialintelligence-news.com/2023/12/19/ai-big-data-expo-maximising-value-real-time-data-streams/'

# ウェブサイトからHTMLを取得
response = requests.get(url)
html = response.content

# BeautifulSoupオブジェクトの作成
soup = BeautifulSoup(html, 'html.parser')

# 本文を含む要素を探す
# 例: <p> タグと特定のクラスを持つ <div> タグ
article_contents = soup.find_all(['p', 'div'], class_=['cboxcomment', 'voicecomment', 'wp-block-image size-large is-style-stk_border', 'wp-block-heading'])

# 本文のテキストを取得
for content in article_contents:
    print(content.get_text(strip=True))
