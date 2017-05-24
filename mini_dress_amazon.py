# -*- coding: utf-8 -*-
import requests
import re
from settings import HEADERS
import random
from lxml import etree
from amazon_store import AmazonStore, AmazonIpStore
import traceback
import codecs
import time
import json

first_url = 'https://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=mini+dress'


def get_products_lst(html):
    global count
    sel = etree.HTML(html)
    p_lst = []
    products_lst = sel.xpath('//div[@id="resultsCol"]//ul')
    for i in range(len(products_lst)):
        for j in range(len(products_lst[i].xpath('li'))):
            p_result = dict()
            p_title = products_lst[i].xpath('li')[j].xpath(
                'div/div[starts-with(@class, "a-row a-spacing-none")][1]/div[1]/a/@title')
            if len(p_title) > 0:
                p_result['title'] = p_title[0]

            product_url = products_lst[i].xpath('li')[j].xpath(
                'div/div[starts-with(@class, "a-row a-spacing-none")][1]/div[1]/a/@href')
            if len(product_url) > 0:
                p_url = re.findall('(.+)/ref', product_url[0])[0]
                p_result['url'] = p_url

            p_img = products_lst[i].xpath('li')[j].xpath(
                'div/div[1]//img/@src')
            if len(p_img) > 0:
                p_img = re.findall(r'(.+)\._.+\.jpg', p_img[0])[0] + '.jpg'
                p_result['img'] = p_img

            p_asin = products_lst[i].xpath('li')[j].xpath('@data-asin')
            if len(p_asin) > 0:
                p_result['asin'] = p_asin[0]
            if len(p_result) == 4:
                p_lst.append(p_result)
    for p in p_lst:
        url = p['url']
        if url.startswith('http'):
            count += 1
            print count
            title = p['title'].encode('utf-8')
            img = p['img']
            asin = p['asin']
            print asin
            print url
            print title
            print img
            amazon_store.insert_url_title(asin, url, title, img, "Women's Clothing", 'mini dress', 'amazon', 'US')
    next_page_url = 'https://www.amazon.com' + sel.xpath('//a[@id="pagnNextLink"]/@href')[0]
    crawl_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    create_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    amazon_store.insert_page_url(next_page_url, 'mini dress', crawl_time, create_time)


def get_product_info(html, p_id):
    price = '0'
    sale_price = '0'
    grade_count = 0
    review_count = 0
    attribute = dict()
    feature = ''
    extra_image_urls = ''
    description = ''
    generation_time = '0000-00-00'
    sel = etree.HTML(html)

    # price
    if len(sel.xpath('//span[@id="priceblock_ourprice"]/text()')) > 0:
        _price = sel.xpath('//span[@id="priceblock_ourprice"]/text()')
        if len(_price) > 1:
            price = ''.join(_price)
        elif len(_price) > 0:
            price = _price[0].strip()
    elif len(sel.xpath('//div[@id="price"]//span[@class="a-text-strike"]/text()')) > 0:
        price = sel.xpath('//div[@id="price"]//span[@class="a-text-strike"]/text()')[0].strip()

    # sale_price
    _sale_price = sel.xpath('//span[@id="priceblock_saleprice"]/text()')
    if len(_sale_price) > 0:
        if _sale_price[0].strip().startswith('$'):
            sale_price = _sale_price[0].strip()

    if price == '0':
        price = sale_price
        sale_price = '0'

    # grade_count
    _grade_count = sel.xpath('//span[@id="acrPopover"]/@title')
    if len(_grade_count) > 0:
        grade_count = _grade_count[0].split(' ')[0]

    # review_count
    _review_count = sel.xpath('//span[@id="acrCustomerReviewText"]/text()')
    if len(_review_count) > 0:
        review_count = _review_count[0].split(' ')[0].replace(',', '')

    # attribute
    size = sel.xpath('//div[@id="variation_size_name"]')
    if len(size) > 0:
        if len(size[0].xpath('//select[@id="native_dropdown_selected_size_name"]')) > 0:
            attribute['size'] = [item.strip() for item in
                                 size[0].xpath('//select[@id="native_dropdown_selected_size_name"]/option/text()')[1:]]
        elif len(size[0].xpath('//span[@class="selection"]/text()')) > 0:
            attribute['size'] = size[0].xpath('//span[@class="selection"]/text()')[0]
        elif len(size[0].xpath('div/text()')) > 0:
            attribute['size'] = ''.join([item.strip() for item in size[0].xpath('div/text()')])

    color = sel.xpath('//div[@id="variation_color_name"]')
    if len(color) > 0:
        if len(color[0].xpath('//select[@id="native_dropdown_selected_color_name"]//option/@data-a-html-content')) > 0:
            attribute['color'] = color[0].xpath(
                '//select[@id="native_dropdown_selected_color_name"]//option/@data-a-html-content')
        elif len(color[0].xpath('ul//li/@title')) > 0:
            attribute['color'] = [' '.join(color.split(' ')[3:]) for color in color[0].xpath('ul//li/@title')]
        elif len(color[0].xpath('//span[@class="selection"]/text()')) > 0:
            attribute['color'] = ''.join([item.strip() for item in color[0].xpath('//span[@class="selection"]/text()')])
        elif len(color[0].xpath('div/text()')) > 0:
            attribute['color'] = ''.join([item.strip() for item in color[0].xpath('div/text()')])

    style = sel.xpath('//div[@id="variation_style_name"]')
    if len(style) > 0:
        style_option = sel.xpath('//select[@id="native_dropdown_selected_style_name"]//option/@data-a-html-content')
        if len(style_option) > 0:
            attribute['style'] = style_option
        else:
            styles = style[0].xpath('ul//li/@title')
            attribute['style'] = [' '.join(style.split(' ')[3:]) for style in styles]
    if len(attribute) == 0:
        attribute = ''
    else:
        attribute = json.dumps(attribute)

    # extra_image_urls
    eiu = []
    _extra_image_urls = sel.xpath('//div[@id="altImages"]')
    if len(_extra_image_urls) > 0:
        _extra_image_urls = _extra_image_urls[0].xpath('ul/li//img/@src')
        for url in _extra_image_urls:
            if 'jpg' in url:
                image_url = re.findall(r'(.+)\._.+\.jpg', url)[0] + '.jpg'
                eiu.append(image_url)
            elif 'png' in url:
                image_url = re.findall(r'(.+)\._.+\.png', url)[0] + '.png'
                eiu.append(image_url)
            else:
                pass
    if len(eiu) > 0:
        extra_image_urls = ','.join(eiu)

    # description
    _description = sel.xpath('//div[@id="productDescription"]/p/text()')
    if len(_description) > 0:
        description = ''.join(_description).strip().encode('utf-8')

    # feature
    _feature = sel.xpath('//div[@id="feature-bullets"]/ul/li/span/text()')
    if len(_feature) > 0:
        feature = ''.join([ft.strip() for ft in _feature]).encode('utf-8')

    # generation_time
    detail_1 = sel.xpath('//div[@id="detailBullets_feature_div"]//li/span/span[@class="a-text-bold"]')
    detail_2 = sel.xpath('//table[@id="productDetails_detailBullets_sections1"]//tr//th')
    if len(detail_1) > 0:
        for d in detail_1:
            if len(d.xpath('text()')) > 0 and d.xpath('text()')[0].strip().startswith('Date first available'):
                format_time = d.xpath('../span[2]/text()')[0].replace(',', '').split()
    elif len(detail_2) > 0:
        for d in detail_2:
            if len(d.xpath('text()')) > 0 and d.xpath('text()')[0].strip().startswith('Date first available'):
                format_time = d.xpath('../td/text()')[0].replace(',', '').split()
    if len(detail_1) > 0 or len(detail_2) > 0:
        month, dt, year = format_time
        m = format_month(month)
        generation_time = '%s-%s-%s' % (year, m, dt)

    crawl_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    create_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

    print 'price: ', price
    print 'sale_price: ', sale_price
    print 'grade_count: ', grade_count
    print 'review_count: ', review_count
    print 'attribute: ', attribute
    print 'feature: ', feature
    print 'extra_image_urls: ', extra_image_urls
    print 'description: ', description
    print 'generation_time: ', generation_time

    assert extra_image_urls != ''  # 触发异常换ip
    amazon_store.update_mini_dress(1,price,sale_price,grade_count,review_count,attribute,feature,extra_image_urls,
                                   description,generation_time,crawl_time,create_time,p_id)


def format_month(m):
    month = ['January', 'February', 'March', 'April', 'May', 'June',
             'July', 'August', 'September', 'October', 'November', 'December']
    for index, item in enumerate(month):
        if m == item:
            return index+1


if __name__ == '__main__':
    amazon_store = AmazonStore()
    amazon_ip = AmazonIpStore()

    # 获取所有商品链接
    """
    pages_url_lst = amazon_store.select_page_url()
    num = len(pages_url_lst)
    count = 0
    try:
        for n in range(num, 101):
            pages_url_lst = amazon_store.select_page_url()
            page_url = pages_url_lst[-1]['scapu_url']
            print u'第%s页: ' % n, page_url
            res = s.get(page_url, timeout=10)
            with codecs.open('amazon.html', 'w') as html_file:
                html_file.write(res.content)
            print res.status_code
            if res.status_code == 200:
                get_products_lst(res.content)

    except:
        traceback.print_exc()
    """

    # 获取单个商品详情信息

    while 1:
        try:
            ip_total = amazon_ip.count_total()[0][0]
            print u'可以代理ip: %s' % ip_total
            if int(ip_total) > 0:
                ip = amazon_ip.select_ip(1, 'amazon.com')[0][0]  # 取出status为1的代理ip
                print(u'当前使用代理ip: %s' % ip)
            else:
                break

            headers = {
                'User-Agent': random.choice(HEADERS)
            }
            proxies = {
                'http': 'http://' + ip
            }
            s = requests.session()
            s.headers.update(headers)
            s.proxies.update(proxies)
            amazon_store = AmazonStore()
            status_0 = amazon_store.count_status_0()
            while len(status_0):
                _id = status_0[0]['scps_id']
                _url = status_0[0]['scps_product_url']
                print _id, _url
                r = s.get(_url, timeout=5)
                # with codecs.open('amazon.html', 'w') as html_file:
                #     html_file.write(r.content)
                if r.status_code == 404:
                    amazon_store.delete_id(_id)
                elif r.status_code == 200:
                    get_product_info(r.content, _id)
                time.sleep(1)
                status_0 = amazon_store.count_status_0()
                t = random.randint(1, 3)
                time.sleep(t)
            print u'采集完毕'
            amazon_store.close()
            amazon_ip.close()
            break
        except:
            traceback.print_exc()
            amazon_ip.delete_ip(ip, 'amazon.com')
            time.sleep(1)





