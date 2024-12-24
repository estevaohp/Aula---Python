import re

import requests # type: ignore
from bs4 import BeautifulSoup # type: ignore

url = 'https://youngfoundations.org/pt/pagenotavailable'
response = requests.get(url)
bytes_html = response.content
parsed_html = BeautifulSoup(bytes_html, 'html.parser', from_encoding='utf-8')
 
top_jobs_heading = parsed_html.select_one('#intro > div > div > article > h2')
 
if top_jobs_heading is not None:
    article = top_jobs_heading.parent
 
    if article is not None:
        for p in article.select('p'):
            print(re.sub(r'\s{1,}', ' ', p.text).strip())   