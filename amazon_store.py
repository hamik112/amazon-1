# -*- coding: utf-8 -*-
from settings import *
import sys
import traceback
import MySQLdb


class AmazonStore:
    def __init__(self):
        try:
            self.conn = MySQLdb.connect(
                host=MYSQL_HOST,
                port=MYSQL_PORT,
                user=MYSQL_USER,
                passwd=MYSQL_PASSWD,
                charset=MYSQL_CHARSET,
                db=MYSQL_DB,
                unix_socket=MYSQL_SOCKET
            )
        except:
            traceback.print_exc()
            sys.exit()

    def insert_info(self, _product_id, _product_url, _name, _price, _review_count, _grade_count, _image_url, _category,
                    _paltform, _crawl_time, _create_time, _attribute, _extra_image_urls, _description, _tags, _shop_url):
        sql = 'insert into scb_crawler_products_sku_chenyang(scps_product_id,scps_product_url,scps_name,scps_price,' \
              'scps_review_count,scps_grade_count,scps_image_url,scps_category,scps_platform,scps_crawl_time,' \
              'scps_create_time,scps_attribute,scps_extra_image_urls,scps_description,scps_tags,scps_shop_url)' \
              'values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        cur = self.conn.cursor()
        cur.execute(sql, (_product_id, _product_url, _name, _price, _review_count, _grade_count, _image_url, _category,
                    _paltform, _crawl_time, _create_time, _attribute, _extra_image_urls, _description, _tags, _shop_url))
        self.conn.commit()

    def select_info(self):
        cur = self.conn.cursor(MySQLdb.cursors.DictCursor)
        sql = 'select * from scb_crawler_products_sku_chenyang'
        result = cur.execute(sql)
        return cur.fetchmany(result)

    def update_info(self, _attribute, _extra_image_urls, _description, _id):
        cur = self.conn.cursor()
        _attribute = MySQLdb.escape_string(_attribute)
        _description = MySQLdb.escape_string(_description)
        cur.execute('update scb_crawler_products_sku_chenyang set scps_attribute="%s", scps_extra_image_urls="%s", scps_description="%s" where scps_id="%s"'% (_attribute, _extra_image_urls, _description, _id))
        self.conn.commit()

    # def select_inventory_info(self):
    #     cur = self.conn.cursor(MySQLdb.cursors.DictCursor)
    #     sql = 'select * from scb_crawler_products_sku_dynamic_chenyang'
    #     result = cur.execute(sql)
    #     return cur.fetchmany(result)

    def update_inventory_info(self, _inventory, _id):
        cur = self.conn.cursor()
        cur.execute('update scb_crawler_products_sku_chenyang set scps_total_inventory="%s" where scps_id="%s"'% (_inventory, _id))
        self.conn.commit()

    # inventory
    def get_product_url(self):  # 取出status为0的row的id和product_url
        cur = self.conn.cursor(MySQLdb.cursors.DictCursor)
        sql = 'select scps_id, scps_product_url from scb_crawler_products_sku_chenyang where scps_status=0 limit 1'
        result = cur.execute(sql)
        return cur.fetchmany(result)

    def add_inventory(self, _id, _price, _review_count, _grade_count, _total_inventory, _crawl_time, _create_time, _remark):  # 插入库存等信息
        sql = 'insert into scb_crawler_products_sku_dynamic_chenyang(scps_id,scpsd_price,scpsd_review_count,scpsd_grade_count,' \
              'scpsd_total_inventory,scpsd_crawl_time,scpsd_create_time,scpsd_remark)values(%s,%s,%s,%s,%s,%s,%s,%s)'
        cur = self.conn.cursor()
        cur.execute(sql, (_id, _price, _review_count, _grade_count, _total_inventory, _crawl_time, _create_time, _remark))
        self.conn.commit()

    def set_status_1(self, _id):
        cur = self.conn.cursor()
        cur.execute('update scb_crawler_products_sku_chenyang set scps_status=1 where scps_id="%s"' % _id)
        self.conn.commit()

    def set_status_0(self):
        cur = self.conn.cursor()
        cur.execute('update scb_crawler_products_sku_chenyang set scps_status=0')
        self.conn.commit()

    # mini dress
    def insert_page_url(self, _url, _type, _crawl_time, _create_time):
        _url = MySQLdb.escape_string(_url)
        sql = "insert into scb_crawler_amazon_page_url(scapu_url, scapu_type, scapu_crawl_time, scapu_create_time) values (%s,%s,%s,%s)"
        cur = self.conn.cursor()
        cur.execute(sql, (_url, _type, _crawl_time, _create_time))
        self.conn.commit()

    def select_page_url(self):
        cur = self.conn.cursor(MySQLdb.cursors.DictCursor)
        sql = 'select * from scb_crawler_amazon_page_url'
        result = cur.execute(sql)
        return cur.fetchmany(result)

    def insert_url_title(self, _id, _url, _title, _img, _category, _search_word, _platform, _currency, _attribute='', _extra_image_urls='', _description='', _tags='', _shop_url='', _feature=''):
        sql = "insert into scb_crawler_products_sku_mini_dress_amazon(scps_product_id,scps_product_url, scps_name, scps_image_url,scps_category,scps_search_word," \
              "scps_platform,scps_currency,scps_attribute,scps_extra_image_urls,scps_description,scps_tags,scps_shop_url, scps_feature )values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cur = self.conn.cursor()
        cur.execute(sql, (_id, _url, _title, _img, _category, _search_word, _platform, _currency, _attribute, _extra_image_urls, _description, _tags, _shop_url, _feature))
        self.conn.commit()

    def update_mini_dress(self, _status, _price, _sale_price, _grade_count, _review_count, _attribute, _feature, _extra_image_urls,
                          _description, _generation_time, _crawl_time, _create_time, _id):
        _attribute = MySQLdb.escape_string(_attribute)
        _feature = MySQLdb.escape_string(_feature)
        _description = MySQLdb.escape_string(_description)
        cur = self.conn.cursor()
        cur.execute('update scb_crawler_products_sku_mini_dress_amazon set scps_status="%s", scps_price="%s", scps_sale_price="%s", scps_grade_count="%s",'
                    'scps_review_count="%s", scps_attribute="%s", scps_feature="%s", scps_extra_image_urls="%s", scps_description="%s",'
                    'scps_generation_time="%s", scps_crawl_time="%s", scps_create_time="%s" where scps_id="%s"'
                    % (_status, _price, _sale_price, _grade_count, _review_count, _attribute, _feature, _extra_image_urls,
                       _description, _generation_time, _crawl_time, _create_time, _id))
        self.conn.commit()

    def count_status_0(self):
        cur = self.conn.cursor(MySQLdb.cursors.DictCursor)
        sql = 'select scps_id, scps_product_url from scb_crawler_products_sku_mini_dress_amazon where scps_status=0 limit 1'
        result = cur.execute(sql)
        return cur.fetchmany(result)

    def change_status(self):
        cur = self.conn.cursor()
        cur.execute('update scb_crawler_products_sku_mini_dress_amazon set scps_status=0 where scps_id > 0')
        self.conn.commit()

    def delete_row(self, _id):
        cur = self.conn.cursor()
        cur.execute('delete from scb_crawler_products_sku_mini_dress_amazon where scps_id="%s"' % _id)
        self.conn.commit()

    # test
    def insert_test(self, _text):  # 插入不重复t_text, 提前设置t_text索引unique
        cur = self.conn.cursor()
        sql = "insert ignore into test(t_text)values(%s)"
        cur.execute(sql, _text)
        self.conn.commit()

    def close(self):
        cursor = self.conn.cursor()
        cursor.close()
        self.conn.close()


class AmazonIpStore:
    def __init__(self):
        try:
            self.conn = MySQLdb.connect(
                host=MYSQL_HOST,
                port=MYSQL_PORT,
                user=MYSQL_USER,
                passwd=MYSQL_PASSWD,
                charset=MYSQL_CHARSET,
                db=MYSQL_DB,
                unix_socket=MYSQL_SOCKET
            )
        except:
            traceback.print_exc()
            sys.exit()

    def insert_info(self, ip, _interval, _check_time, _status=1, _domain="amazon.com"):  # 存贮已验证ip
        cursor = self.conn.cursor()
        sql = 'insert into scb_crawler_cy_ip(scci_ip,scci_interval,scci_check_time,scci_status,scci_domain)VALUES (%s,%s,%s,%s,%s)'
        cursor.execute(sql, (ip, _interval, _check_time, _status, _domain))
        self.conn.commit()

    def count_total(self):  # 统计ip总数
        cursor = self.conn.cursor()
        sql = "select count(*) from scb_crawler_cy_ip"
        result = cursor.execute(sql)
        return cursor.fetchmany(result)

    def select_ip(self, status, domain):  # 选择响应时间最短的ip
        cursor = self.conn.cursor()
        sql = "select scci_ip from scb_crawler_cy_ip where scci_status=%s and scci_domain='%s' order by scci_interval limit 1" % (status, domain)
        result = cursor.execute(sql)
        return cursor.fetchmany(result)

    def delete_ip(self, ip, domain):  # 删除无效ip
        cursor = self.conn.cursor()
        cursor.execute("delete from scb_crawler_cy_ip where scci_ip='%s' and scci_domain='%s'" % (ip, domain))
        self.conn.commit()

    def close(self):
        cursor = self.conn.cursor()
        cursor.close()
        self.conn.close()


if __name__ == '__main__':
    amazon_store = AmazonStore()
    amazon_store.change_status_1()


