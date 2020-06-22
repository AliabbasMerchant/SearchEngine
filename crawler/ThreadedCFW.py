from bs4 import BeautifulSoup
from urllib.parse import urljoin
from crawler.ContentFetcher import ContentFetcher
import crawler.utils as utils
import time
import concurrent.futures
import threading


class CrawlerForAWebsite:
    def __init__(self, main_url: str, limit: int = 100):
        self.main_url = main_url
        self.domain = utils.get_domain_name(main_url)
        self.queue = set()
        self.queue.add(self.main_url)
        self.content = dict()
        self.limit = limit

    def crawl(self,url) :

        start_time = time.time()
        #self.queue.copy().remove(url)
        with open('crawled_file', 'a+') as f:
            if url not in f.read():

                content, links = self.get_content_and_same_domain_links(url)


                self.content[url] = content

                end_time = time.time()
                #print(f"URL {url} has {len(links)} links in {end_time - start_time} sec on thread={threading.current_thread().name}")
                print(f"URL {url} has {len(links)} links")


                f.write(url)
                f.write('\n')
                self.queue.update(links)

    def get_content_and_same_domain_links(self, url: str) -> (str, list):

        html = content_fetcher.fetch_dynamically(url, scroll=False)
        soup = BeautifulSoup(html, 'html.parser')
        links = set()
        for link in soup.find_all('a', href=True):
            li = urljoin(self.main_url, link.get('href'))
            if utils.get_domain_name(li) == self.domain:
                links.add(li)
        return html, links


if __name__ == '__main__':
    crawler = CrawlerForAWebsite('https://www.geeksforgeeks.org')
    content_fetcher = ContentFetcher()

    count = 0
    def worker(url):
        crawler.crawl(url)


    while count < crawler.limit and len(crawler.queue) > 0:
        count += 1

        threads = min(16, len(crawler.queue))
        with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
            fu=[executor.submit(worker, ul) for ul in crawler.queue]





