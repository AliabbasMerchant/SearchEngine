import requests
from selenium import webdriver
import time


class ContentFetcher:
    def __init__(self):
        opts = webdriver.ChromeOptions()
        opts.headless = True

        self.driver = webdriver.Chrome(executable_path='.\\lib\\chromedriver.exe', options=opts)
        self.SCROLL_PAUSE_TIME = 3

    def fetch_dynamically(self, url: str, scroll: bool = True, scroll_limit: int = None) -> str:
        driver = self.driver
        driver.get(url)
        if scroll:
            last_height = driver.execute_script("return document.body.scrollHeight")
            limit = 0
            while True:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(self.SCROLL_PAUSE_TIME)  # So that the new data is loaded
                new_height = driver.execute_script("return document.body.scrollHeight")
                if new_height == last_height:
                    break
                last_height = new_height
                limit += 1
                if scroll_limit is not None:
                    if limit >= scroll_limit:
                        break
        return driver.page_source

    def fetch_statically(self, url: str) -> str:
        r = requests.get(url)
        return r.content.decode('utf-8')

    def fetch(self, url: str, dynamic: bool = True) -> str:
        if dynamic:
            return self.fetch_dynamically(url)
        else:
            return self.fetch_statically(url)
