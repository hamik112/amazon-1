# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import re
import time
import traceback
from amazon_store import AmazonStore, AmazonIpStore
import configparser
import codecs
import random
import os
import json
from web_driver import WebDriver
from pyvirtualdisplay import Display


def isDisplayed(is_driver, elementType, element):
    try:
        if elementType == 'id':
            try:
                is_driver.find_element_by_id(element)
                return True
            except:
                return False
        elif elementType == 'name':
            try:
                is_driver.find_element_by_name(element)
                return True
            except:
                return False

        elif elementType == 'xpath':
            try:
                is_driver.find_element_by_xpath(element)
                return True
            except:
                return False
    except:
        traceback.print_exc()
        return False


def get_inventory(driver, url):
    inventory = 0
    global flag, price, review_count, grade_count, select_attribute, captcha_num, fg
    try:
        driver.get(url)
        if isDisplayed(driver, 'id', 'captchacharacters'):
            captcha_num += 1
            if captcha_num == 3:  # 遇三次验证码退出程序
                fg = False
            print u'遇到验证码 %s 次' % captcha_num
            return
    except TimeoutException:
        driver.find_element_by_id('twotabsearchtextbox').send_keys(Keys.ESCAPE)
        print u'首页加载超时'

    try:
        # if isDisplayed(driver, 'id', 'variation_number_of_items'):
        #     wd.find_element_by_xpath('//div[@id="variation_number_of_items"]//li[@title="Click to select 1"]//button').click()
        #     time.sleep(2)
        if isDisplayed(driver, 'id', 'native_dropdown_selected_size_name'):
            WebDriverWait(wd, 10).until(EC.presence_of_element_located((By.ID, 'native_dropdown_selected_size_name')))
            if int(_id) == 94:
                wd.find_elements_by_xpath('//select[@id="native_dropdown_selected_size_name"]//option[@class="dropdownAvailable"]')[0].click()  # 选择size第一项
            else:
                wd.find_element_by_id("native_size_name_0").click()
            time.sleep(2)
        WebDriverWait(driver, 10).until_not(EC.presence_of_element_located((By.XPATH, '//input[@id="add-to-cart-button" and @style="cursor: not-allowed;"]')))
        time.sleep(1)
        WebDriverWait(wd, 10).until(EC.presence_of_element_located((By.ID, 'acrCustomerReviewText')))
        WebDriverWait(wd, 10).until(EC.presence_of_element_located((By.ID, 'acrPopover')))
        if isDisplayed(driver, 'id', 'priceblock_ourprice'):
            price = driver.find_element_by_xpath('//span[@id="priceblock_ourprice"]').text
        elif isDisplayed(driver, 'id', 'priceblock_dealprice'):
            price = driver.find_element_by_xpath('//span[@id="priceblock_dealprice"]').text
        elif isDisplayed(driver, 'id', 'priceblock_saleprice'):
            price = driver.find_element_by_xpath('//span[@id="priceblock_saleprice"]').text
        review_count = driver.find_element_by_xpath('//span[@id="acrCustomerReviewText"]').text.split(' ')[0].replace(',', '')
        grade_count = driver.find_element_by_xpath('//span[@id="acrPopover"]').get_attribute('title').split(' ')[0]
        print 'price: ', price
        print 'review_count: ', review_count
        print 'grade_count: ', grade_count
        if isDisplayed(driver, 'id', 'variation_size_name'):
            if isDisplayed(driver, 'xpath', '//div[@id="variation_size_name"]//select//option'):
                select_size = wd.find_element_by_xpath('//div[@id="variation_size_name"]//select//option[@class="dropdownSelect"]').get_attribute('data-a-html-content')
            else:
                select_size = wd.find_element_by_xpath('//div[@id="variation_size_name"]//span[@class="selection"]').text
            select_attribute['select_size'] = select_size
        if isDisplayed(driver, 'id', 'variation_color_name'):
            if isDisplayed(driver, 'id', 'native_dropdown_selected_color_name'):
                select_color = wd.find_element_by_xpath('//div[@id="variation_color_name"]//select//option[@class="dropdownSelect"]').get_attribute('data-a-html-content')
            elif isDisplayed(driver, 'xpath', '//div[@id="variation_color_name"]//ul//li'):
                select_color = wd.find_element_by_xpath('//div[@id="variation_color_name"]//ul//li[starts-with(@class,"swatchSelect")]').get_attribute('title').split(' ')[3:][0]
            else:
                select_color = wd.find_element_by_xpath('//div[@id="variation_color_name"]//span[@class="selection"]').text
            select_attribute['select_color'] = select_color
        if isDisplayed(driver, 'id', 'variation_style_name'):
            if isDisplayed(driver, 'xpath', '//div[@id="variation_style_name"]//select'):
                select_style = wd.find_element_by_xpath('//div[@id="variation_style_name"]//select//option[@class="dropdownSelect"]').get_attribute('data-a-html-content')
            elif isDisplayed(driver, 'xpath', '//div[@id="variation_style_name"]//ul'):
                select_style = wd.find_element_by_xpath('//div[@id="variation_style_name"]//ul//li[starts-with(@class,"swatchSelect")]').get_attribute('title').split(' ')[3:][0]
            elif isDisplayed(driver, 'xpath', '//div[@id="variation_style_name"]/div'):
                select_style = wd.find_element_by_xpath('//div[@id="variation_style_name"]/div').text.strip()
            select_attribute['select_style'] = select_style
        print 'select_attribute: ', select_attribute
    except TimeoutException:
        driver.execute_script("window.stop()")
        print u'选择size超时'

    if review_count == 0:
        return
    WebDriverWait(driver, 10).until_not(EC.presence_of_element_located((By.XPATH, '//input[@id="add-to-cart-button" and @style="cursor: not-allowed;"]')))
    quantity = driver.find_elements_by_xpath('//select[@id="quantity"]//option')
    if len(quantity) == 0 and price == '0':
        inventory = 0
        flag = False
    elif len(quantity) == 0:
        inventory = 1
        flag = False
    elif 0 < len(quantity) < 30:
        inventory = len(quantity)
        flag = False
    else:
        try:
            driver.find_element_by_id("quantity").find_elements_by_tag_name("option")[len(quantity) - 1].click()
            driver.execute_script('document.getElementById("addToCart").submit();')
            time.sleep(2)
            driver.execute_script('window.stop()')
        except TimeoutException:
            driver.execute_script('window.stop()')
            print u'加入购入车超时'
        try:
            driver.get("https://www.amazon.com/gp/cart/view.html/ref=lh_cart")
            time.sleep(2)
        except TimeoutException:
            driver.execute_script('window.stop()')
            print u'进入购物车超时'
        try:
            driver.find_element_by_xpath('//input[@name="quantityBox"]').clear()
            driver.find_element_by_xpath('//input[@name="quantityBox"]').send_keys('999' + Keys.ENTER)
            time.sleep(2)
            WebDriverWait(driver, 10).until_not(EC.presence_of_element_located((By.ID, 'a-autoid-3-announce')))
            time.sleep(1)
            inventory = driver.find_element_by_xpath('//input[@name="quantityBox"]').get_attribute('value')
        except TimeoutException:
            print u'更新库存超时'

    print 'inventory: ', inventory
    return inventory


if __name__ == '__main__':
    amazon_store = AmazonStore()
    amazon_ip = AmazonIpStore()
    captcha_num = 0  # 遇到验证码次数
    fg = True
    while fg:
        row = amazon_store.get_product_url()
        if len(row) == 0:
            break
        ip_total = amazon_ip.count_total()[0][0]
        print u'代理ip数目: %s' % ip_total
        if int(ip_total) > 0:
            ip = amazon_ip.select_ip(1, 'amazon.com')[0][0]  # 取出status为1的代理ip
            print(u'当前使用ip: %s' % ip)
        else:
            break
        # wd = webdriver.Chrome("C:/Users/Administrator/AppData/Local/Google/Chrome/Application/chromedriver.exe")
        # wd = webdriver.Firefox()
        display = Display(visible=0, size=(1920, 1080))
        display.start()
        dri = WebDriver()
        wd = dri.firefox_with_proxy(str(ip))
        # wd.maximize_window()
        # wd.set_page_load_timeout(20)
        try:
            while len(row):
                _id = row[0]['scps_id']
                _product_url = row[0]['scps_product_url']
                print _id, _product_url
                flag = True
                price = '0'
                review_count = 0
                grade_count = 0.0
                select_attribute = dict()
                total_inventory = get_inventory(wd, _product_url)
                crawl_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
                create_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                if review_count == 0:
                    break
                if price != '0' and len(select_attribute) > 0:
                    remark = json.dumps(select_attribute)
                elif price == '0' and len(select_attribute) > 0:
                    remark = json.dumps(select_attribute) + ' :Currently unavailable'
                elif price != 0 and len(select_attribute) == 0:
                    remark = 'no attribute'
                else:
                    remark = 'no attribute' + ' :Currently unavailable'
                if flag:
                    WebDriverWait(wd, 10).until(
                        EC.presence_of_element_located((By.XPATH, '//div[starts-with(@class,"a-alert-content")]')))
                    wd.find_element_by_xpath('//input[@value="Delete"]').click()
                time.sleep(2)
                wd.execute_script('window.stop()')
                amazon_store.add_inventory(_id, price, review_count, grade_count, total_inventory, crawl_time,
                                           create_time, remark)
                amazon_store.set_status_1(_id)
                t = random.randint(2, 5)
                time.sleep(t)
                row = amazon_store.get_product_url()
                if len(row) == 0:
                    fg = False
                    amazon_store.set_status_0()
                    print u'采集完毕'
        except:
            traceback.print_exc()
            amazon_ip.delete_ip(ip, 'amazon.com')
        finally:
            wd.quit()
            display.stop()
