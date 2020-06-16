from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests
import time
import crawler.utils as utils
x = 10
def bar():

    print(x)
    x += 1
#
# content_fetcher = ContentFetcher()
# weburl = 'https://summerofcode.withgoogle.com/organizations'
# html = content_fetcher.fetch(weburl)





'''
def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)
    return u" ".join(t.strip() for t in visible_texts)

print(text_from_html(driver.page_source))

#print(driver.page_source)
 def crawl(self) -> None:
         '''
#
# soup = BeautifulSoup(html, 'html.parser')
#
# # print(soup.find_all('a',href=True))
#
# s = set()
# for link in soup.find_all('a', href=True):
#     li = urljoin(weburl, link.get('href'))
#     s.add(li)
# for li in s:
#     print(li)
