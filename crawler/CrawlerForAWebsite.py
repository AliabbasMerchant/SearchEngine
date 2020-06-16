from bs4 import BeautifulSoup
from urllib.parse import urljoin
from crawler.ContentFetcher import ContentFetcher
import crawler.utils as utils
import time
import concurrent.futures


class CrawlerForAWebsite:
    def __init__(self, main_url: str, limit: int = 100):
        self.main_url = main_url
        self.domain = utils.get_domain_name(main_url)
        self.queue = set()
        self.content = dict()
        self.limit = limit

    def crawl(self) -> None:
        count = 0
        start_time = time.time()
        self.queue.add(self.main_url)
        while count < self.limit and len(self.queue) > 0:
            count += 1
            url = self.queue.pop()

            content, links = self.get_content_and_same_domain_links(url)

            self.content[url] = content
            end_time=time.time()
            print(f"URL {url} has {len(links)} links in {end_time  - start_time} sec")
            with open('crawled_file', 'a') as f:

                f.write(url)
                f.write('\n')
            self.queue.update(links)



    def get_content_and_same_domain_links(self, url: str) -> (str, list):
        content_fetcher = ContentFetcher()
        html = content_fetcher.fetch_dynamically(url, scroll=False)
        soup = BeautifulSoup(html, 'html.parser')
        links = set()
        for link in soup.find_all('a', href=True):
            li = urljoin(self.main_url, link.get('href'))
            if utils.get_domain_name(li) == self.domain:
                links.add(li)
        return html, links


if __name__ == '__main__':
    crawler = CrawlerForAWebsite("https://github.com/")
    crawler.crawl()


