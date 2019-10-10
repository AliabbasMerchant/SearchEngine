from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='.\\lib\\chromedriver.exe')  # It could also be PhantomJS instead of Chrome
driver.get("https://summerofcode.withgoogle.com/organizations")

SCROLL_PAUSE_TIME = 3

last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

print(driver.page_source)