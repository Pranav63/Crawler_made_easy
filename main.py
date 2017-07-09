import requests
from bs4 import BeautifulSoup

def crawler(max_pages):
    page=1
    while page<=max_pages:
        url="https://www.raghavdua.com"
        source_code=requests.get(url)
        text=source_code.text
        soup = BeautifulSoup(text)
        for link in soup.findAll('h1',{'class':'name'}):
            #ul = link.get('href')
            print(link.string)
            single_page(href)
        page += 1

def single_page(page_url):
    source_code = requests.get(url)
    text = source_code.text
    soup = BeautifulSoup(text)
    for page_item in soup.findAll('a',{'class':'header-logo-invertocat'}):
        href="https://www.ragahavdua.com"+page_item.get('href')
        print(href)
crawler(3)


