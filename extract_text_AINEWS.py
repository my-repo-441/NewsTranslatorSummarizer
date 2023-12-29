import requests
from bs4 import BeautifulSoup
import json
import re

# ニュースページのURL
#url = 'https://news.mit.edu/2023/leveraging-language-understand-machines-1222'
#url = 'https://www.kuretom.com/aws-all-cert/'
url = 'https://www.zdnet.com/article/supernatural-on-meta-quest-hands-on/'

# ウェブサイトからHTMLを取得
response = requests.get(url)

# ステータスコードのチェック
if response.status_code == 200:
    html = response.content
    soup = BeautifulSoup(html, 'html.parser')
    article_contents = soup.find_all('p')
    for content in article_contents:
        print(content.get_text(strip=True))
else:
    print(f"Error: Status code {response.status_code}")