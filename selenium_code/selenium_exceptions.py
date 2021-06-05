from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium import webdriver
from retry import retry


class Spider(object):
    def __init__(self):
        self.driver = webdriver.Chrome('./chromedriver.exe')
        self.driver.implicitly_wait(0.1)
        self.driver.maximize_window()

    @retry((NoSuchElementException, TimeoutException), tries=3, delay=1, backoff=2)
    def crawl(self):
        # 装饰器捕捉指定异常 重试三次,三次仍然异常抛出异常
        self.driver.get('https://blog.csdn.net/qq_34663267/article/details/107914401')
        res = self.driver.find_element_by_id('fake_id')
        return res

    def start(self):
        try:
            self.crawl()
        finally:
            print('after all we need close the browser')
            self.driver.quit()


if __name__ == '__main__':
    s = Spider()
    s.start()
