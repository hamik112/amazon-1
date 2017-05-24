# -*- coding: utf-8 -*-

from pyvirtualdisplay import Display
from selenium import webdriver
import random
from settings import HEADERS


class WebDriver:

    def __init__(self):
        self.driver = None

    def start(self):
        self.display = Display(visible=0, size=(1024, 768))
        self.display.start()
        pass

    def close(self):
        if self.driver:
            self.driver.quit()
        #self.display.stop()

    def firefox_with_proxy(self, proxy_temp=None):
        random_header = random.choice(HEADERS)
        proxy = ''
        if not proxy_temp:
            print(u'没有代理ip')
        elif isinstance(proxy_temp, str):
            proxy = dict()
            proxy['http'] = proxy_temp.split(':')[0]
            proxy['port'] = proxy_temp.split(':')[1]
        elif isinstance(proxy_temp, dict):
            proxy = proxy_temp
        #print proxy
        profile = webdriver.FirefoxProfile()
        profile.set_preference('network.proxy.type', 1)
        profile.set_preference('network.proxy.http', proxy['http'])
        profile.set_preference('network.proxy.http_port', int(proxy['port']))
        profile.set_preference('network.proxy.ssl', proxy['http'])
        profile.set_preference('network.proxy.ssl_port', proxy['port'])
        profile.set_preference('general.useragent.override', random_header)
        if self.driver:
            self.driver.quit()
        try:
            self.driver = webdriver.Firefox(profile)
            self.driver.set_page_load_timeout(20)
        except:
            self.close()
            self.start()
            self.driver = webdriver.Firefox(profile)
            self.driver.set_page_load_timeout(20)

        return self.driver