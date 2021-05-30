import abc
import threading
from queue import Queue
from typing import Union


class Spider(object):
    def __init__(self, thread_num: int):
        self.thread_num = thread_num
        self.queue = Queue()

    def do_work(self):
        while not self.queue.empty():
            item = self.queue.get()
            self.crawl(item)

    def crawl(self, item):
        pass

    def save2db(self, data: Union[dict, list]):
        if isinstance(data, dict):
            pass
        elif isinstance(data, list):
            pass

    def insert_data(self):
        pass

    def init_queue(self):
        raise NotImplementedError('必须实现init_queue方法')

    def start(self):
        self.init_queue()
        threads = []
        for _ in range(self.thread_num):
            t = threading.Thread(target=self.crawl)
            threads.append(t)
        for t in threads:
            t.join()
