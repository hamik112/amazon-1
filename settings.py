# -*- coding: utf-8 -*-
"""
MYSQL_HOST = '47.91.140.136'  # 服务器上改为localhost
MYSQL_PORT = 3306
MYSQL_USER = 'bgpc'
MYSQL_PASSWD = 'bgpc1qaz@WSX'
MYSQL_DB = 'scb_crawler_system'
MYSQL_CHARSET = 'utf8'
MYSQL_SOCKET = '/data/crawler_system/mysql_data/mysql/mysql.sock'
"""
MYSQL_HOST = '127.0.0.1'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PASSWD = '123456'
MYSQL_DB = 'scb_crawler_system'
MYSQL_CHARSET = 'utf8'

RS_HOST = '127.0.0.1'
RS_PORT = 6379
RS_DB = 0

# 高匿
url = 'http://dev.kuaidaili.com/api/getproxy/?orderid=937340558535151&num=1000&b_pcchrome=1&b_pcie=1&b_pcff=1&protocol=1&method=2&an_ha=1&quality=1&format=json&sep=1'
PROXY_URL ='http://dev.kuaidaili.com/api/getproxy/?orderid=937340558535151&num=100&b_pcchrome=1&b_pcie=1&b_pcff=1&protocol=1&method=2&an_ha=1&sp1=1&quality=1&sort=1&format=json&sep=1'

HEADERS=['Mozilla/4.0 (compatible; MSIE 5.0; Windows 3.1; Trident/7.0; rv:11.0) like Gecko',
'Mozilla/4.0 (compatible; MSIE 6.0; Macintosh; U; Intel Mac OS X 10_6_8; en-us; SV1; LBBROWSER)',
'Mozilla/4.0 (compatible; MSIE 6.0; Mac_PowerPC Mac OS X; ja) Opera 8.01',
'Mozilla/4.0 (compatible; MSIE 6.0; Windows Me; Trident/7.0; rv:11.0; JuziBrowser) like Gecko',
'Mozilla/4.0 (compatible; MSIE 7.0; Macintosh; Intel Mac OS X 10.6; rv:2.0.1; Trident/4.0; Gecko/20100101 Firefox/4.0.1)',
'Mozilla/4.0 (compatible; MSIE 8.0; Macintosh; Intel Mac OS X 10.6; rv:2.0.1; Trident/4.0; Gecko/20100101 Firefox/4.0.1; JuziBrowser)',
'Mozilla/4.0 (compatible; MSIE 8.0; Macintosh; Intel Mac OS X 10.6; rv:2.0.1; Trident/4.0; Gecko/20100101 Firefox/4.0.1)',
'Mozilla/4.0 (compatible; MSIE 8.0; Macintosh; Intel Mac OS X 10_7_0; Trident/4.0)',
'Mozilla/4.0 (compatible; MSIE 8.0; Windows 98; Trident/5.0)',
'Mozilla/5.0 (compatible; MSIE 10.0; compatible; MSIE 7.0; Trident/6.0; JuziBrowser)',
'Mozilla/5.0 (compatible; MSIE 10.0; compatible; MSIE 7.0; Trident/6.0)',
'Mozilla/5.0 (compatible; MSIE 10.0; compatible; MSIE 8.0; Trident/6.0)',
'Mozilla/5.0 (compatible; MSIE 10.0; Macintosh; Intel Mac OS X 10.6; rv:2.0.1; Trident/6.0)',
'Mozilla/5.0 (compatible; MSIE 10.0; Macintosh; Intel Mac OS X 10_7_0; Trident/6.0)',
'Mozilla/5.0 (compatible; MSIE 10.0; Macintosh; Intel Mac OS X 10_7_0; Trident/7.0)',
'Mozilla/5.0 (compatible; MSIE 10.0; Macintosh; Intel Mac OS X 10_7_3; Trident/6.0)',
'Mozilla/5.0 (compatible; MSIE 10.0; Macintosh; U; Intel Mac OS X 10_6_8; en-us; Trident/6.0; JuziBrowser)',
'Mozilla/5.0 (compatible; MSIE 10.0; Macintosh; U; Intel Mac OS X 10_6_8; en-us; Trident/6.0)',
'Mozilla/5.0 (compatible; MSIE 7.0; Trident/7.0; rv:11.0) like Gecko',
'Mozilla/5.0 (compatible; MSIE 8.0; Trident/7.0; LCJB; rv:11.0; JuziBrowser) like Gecko',
'Mozilla/5.0 (compatible; MSIE 8.0; Trident/7.0; rv:11.0; JuziBrowser) like Gecko',
'Mozilla/5.0 (compatible; MSIE 9.0; compatible; MSIE 7.0; Trident/5.0; 360SE)',
'Mozilla/5.0 (compatible; MSIE 9.0; compatible; MSIE 7.0; Trident/5.0)',
'Mozilla/5.0 (compatible; MSIE 9.0; compatible; MSIE 7.0; Trident/7.0; LCJB)',
'Mozilla/5.0 (compatible; MSIE 9.0; compatible; MSIE 7.0; Trident/7.0; MALNJS)',
'Mozilla/5.0 (compatible; MSIE 9.0; compatible; MSIE 7.0; Trident/7.0)',
'Mozilla/5.0 (compatible; MSIE 9.0; compatible; MSIE 8.0; Trident/5.0; JuziBrowser)',
'Mozilla/5.0 (compatible; MSIE 9.0; compatible; MSIE 8.0; Trident/5.0; KB974487)',
'Mozilla/5.0 (compatible; MSIE 9.0; compatible; MSIE 8.0; Trident/5.0; LSIE 1.2.2.42)',
'Mozilla/5.0 (compatible; MSIE 9.0; compatible; MSIE 8.0; Trident/5.0)',
'Mozilla/5.0 (compatible; MSIE 9.0; compatible; MSIE 8.0; Trident/7.0; LCTE)',
'Mozilla/5.0 (compatible; MSIE 9.0; compatible; MSIE 8.0; Trident/7.0)',
'Mozilla/5.0 (compatible; MSIE 9.0; Macintosh; Intel Mac OS X 10.6; rv:2.0.1; Trident/5.0)',
'Mozilla/5.0 (compatible; MSIE 9.0; Macintosh; Intel Mac OS X 10.6; rv:2.0.1; Trident/7.0; LCJB)',
'Mozilla/5.0 (compatible; MSIE 9.0; Macintosh; Intel Mac OS X 10.6; rv:2.0.1; Trident/7.0)',
'Mozilla/5.0 (compatible; MSIE 9.0; Macintosh; Intel Mac OS X 10_7_0; Trident/5.0)',
'Mozilla/5.0 (compatible; MSIE 9.0; Macintosh; Intel Mac OS X 10_7_0; Trident/7.0; LCJB)',
'Mozilla/5.0 (compatible; MSIE 9.0; Macintosh; Intel Mac OS X 10_7_0; Trident/7.0)',
'Mozilla/5.0 (compatible; MSIE 9.0; Macintosh; U; Intel Mac OS X 10_6_8; en-us; Trident/5.0)',
'Mozilla/5.0 (compatible; MSIE 9.0; Macintosh; U; Intel Mac OS X 10_6_8; en-us; Trident/7.0)',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1; rv:37.0) Gecko/20100101 Firefox/37.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:38.0) Gecko/20100101 Firefox/38.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:39.0) Gecko/20100101 Firefox/39.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:41.0) Gecko/20100101 Firefox/41.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:42.0) Gecko/20100101 Firefox/42.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:47.0) Gecko/20100101 Firefox/47.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:48.0) Gecko/20100101 Firefox/48.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:47.0) Gecko/20100101 Firefox/47.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:48.0) Gecko/20100101 Firefox/48.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.5; rv:10.0.2) Gecko/20100101 Firefox/10.0.2',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:16.0) Gecko/20100101 Firefox/16.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1; Trident/7.0; rv:11.0; 2345Explorer 5.0.0.14136) like Gecko',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1; Trident/7.0; rv:11.0) like Gecko',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:25.0) Gecko/20100101 Firefox/25.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:47.0) Gecko/20100101 Firefox/47.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:48.0) Gecko/20100101 Firefox/48.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0; Trident/7.0; rv:11.0; JuziBrowser) like Gecko',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4; rv:20.0) Gecko/20130326150557 Firefox/20.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:41.0) Gecko/20100101 Firefox/41.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:47.0) Gecko/20100101 Firefox/47.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:48.0) Gecko/20100101 Firefox/48.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:21.0) Gecko/20100101 Firefox/21.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:24.0) Gecko/20100101 Firefox/24.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:41.0) Gecko/20100101 Firefox/41.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:47.0) Gecko/20100101 Firefox/47.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:48.0) Gecko/20100101 Firefox/48.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:29.0) Gecko/20100101 Firefox/29.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:34.0) Gecko/20100101 Firefox/34.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:47.0) Gecko/20100101 Firefox/47.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:48.0) Gecko/20100101 Firefox/48.0',
'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.4; en-US; rv:1.9.2.2) Gecko/20100316 Firefox/3.6.2',
'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; zh-CN; rv:1.9.1.2) Gecko/20090729 Firefox/3.5.2',
'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us; Trident/7.0; rv:11.0; JuziBrowser) like Gecko',
'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us; Trident/7.0; rv:11.0) like Gecko',
'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.2.13; ) Gecko/20101203',
'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.2.16) Gecko/20110319 Firefox/3.6.16',
'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; ko; rv:1.9.2.14) Gecko/20110218 Firefox/12.6.14',
'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.9.2; rv:13.0) Gecko/20100101 Firefox/13.0.8',
'Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.8.1.7pre) Gecko/20070815 Firefox/2.0.0.6 Navigator/9.0b3',
'Mozilla/5.0 (Windows 10; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0',
'Mozilla/5.0 (Windows; U; Win 9x 4.90; SG; rv:1.9.2.4) Gecko/20101104 Netscape/9.1.0285',
'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0',
'Mozilla/5.0 (X11; Linux i586; rv:31.0) Gecko/20100101 Firefox/31.0',
'Mozilla/5.0 (X11; Linux i686; rv:10.0.4) Gecko/20100101 Firefox/10.0.4',
'Mozilla/5.0 (X11; Linux i686; rv:17.0) Gecko/20100101 Firefox/17.0',
'Mozilla/5.0 (X11; Linux i686; rv:20.0) Gecko/20100101 Firefox/20.0',
'Mozilla/5.0 (X11; Linux i686; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
'Mozilla/5.0 (X11; Linux i686; rv:2.0b12pre) Gecko/20100101 Firefox/4.0b12pre',
'Mozilla/5.0 (X11; Linux i686; rv:21.0) Gecko/20100101 Firefox/21.0',
'Mozilla/5.0 (X11; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0',
'Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5',
'Mozilla/5.0 (X11; Linux x86_64; rv:10.0.12) Gecko/20130104 Firefox/10.0.12',
'Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/10.0 (Chrome)',
'Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20150101 Firefox/20.0 (Chrome)',
'Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20150101 Firefox/47.0 (Chrome)',
'Mozilla/5.0 (X11; Linux x86_64; rv:18.0) Gecko/20100101 Firefox/18.0',
'Mozilla/5.0 (X11; Linux x86_64; rv:24.0) Gecko/20100101 Firefox/24.0',
'Mozilla/5.0 (X11; Linux x86_64; rv:28.0) Gecko/20100101 Firefox/28.0',
'Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0',
'Mozilla/5.0 (X11; Linux x86_64; rv:43.0) Gecko/20100101 Firefox/43.0',
'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0',
'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0',
'Mozilla/5.0 (X11; Mageia; Linux x86_64; rv:10.0.9) Gecko/20100101 Firefox/10.0.9',
'Mozilla/5.0 (X11; OpenBSD amd64; rv:28.0) Gecko/20100101 Firefox/28.0',
'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:12.0) Gecko/20100101 Firefox/12.0',
'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:15.0) Gecko/20100101 Firefox/15.0.1',
'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:17.0) Gecko/20100101 Firefox/17.0',
'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:17.0) Gecko/20100101 Firefox/17.0/Nutch-1.4',
'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:41.0) Gecko/20100101 Firefox/41.0',
'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:44.0) Gecko/20100101 Firefox/44.0',
'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:13.0) Gecko/20100101 Firefox/13.0.1',
'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0',
'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:21.0) Gecko/20100101 Firefox/21.0',
'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:21.0) Gecko/20130331 Firefox/21.0',
'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:24.0) Gecko/20100101 Firefox/24.0',
'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:26.0) Gecko/20100101 Firefox/26.0',
'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:36.0) Gecko/20100101 Firefox/36.0',
'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:42.0) Gecko/20100101 Firefox/42.0',
'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:44.0) Gecko/20100101 Firefox/44.0',
'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0',
'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0',
'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0',
'Mozilla/5.0 (X11; U; Linux i686; de; rv:1.9.0.14) Gecko/2009082505 Red Hat/3.0.14-1.el5_4 Firefox/3.0.14',
'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.2.1) Gecko/20021204',
'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.12) Gecko/20080219 Firefox/2.0.0.12 Navigator/9.0.0.6',
'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.3) Gecko/2008092416 Firefox/3.0.3',
'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6',
'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.9) Gecko/2009040820 Firefox/3.0.9',
'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.11) Gecko/20101013 Ubuntu/10.04 (lucid) Firefox/3.6.11',
'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a3pre) Gecko/20070330',
'Mozilla/5.0 (X11; U; Linux i686; fi-FI; rv:1.9.2.8) Gecko/20100723 Ubuntu/10.04 (lucid) Firefox/3.6.8',
'Mozilla/5.0 (X11; U; Linux i686)Gecko/20071127 Firefox/2.0.0.11',
'Mozilla/5.0 (X11; U; Linux i686; ja; rv:1.8.0.2) Gecko/20060308 Firefox/1.5.0.2',
'Mozilla/5.0 (X11; U; Linux i686; ru; rv:1.9b5) Gecko/2008032600 SUSE/2.9.95-25.1 Firefox/3.0b5',
'Mozilla/5.0 (X11; U; Linux x86_64; en-GB; rv:1.9.0.10) Gecko/2009042523 Ubuntu/9.04 (jaunty) Firefox/3.0.10',
'Mozilla/5.0 (X11; U; Linux x86_64; en-GB; rv:1.9.2.13) Gecko/20101206 Red Hat/3.6-2.el5 Firefox/3.6.13',
'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.7) Gecko/2009031915 Gentoo Firefox/3.0.7',
'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.13) Gecko/20101206 Ubuntu/10.04 (lucid) Firefox/3.6.13',
'Mozilla/5.0 (X11; U; Linux x86_64; es-ES; rv:1.9.2.12) Gecko/20101027 Fedora/3.6.12-1.fc13 Firefox/3.6.12',
'Mozilla/5.0 (X11; U; Linux x86_64; fr; rv:1.9.2.3) Gecko/20100403 Fedora/3.6.3-4.fc13 Firefox/3.6.3',
'Mozilla/5.0 (X11; U; Linux x86_64; it; rv:1.9.0.8) Gecko/2009032712 Ubuntu/8.10 (intrepid) Firefox/3.0.8',
'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
'Mozilla/8.0 (compatible; MSIE 8.0; Windows 7)'
]
