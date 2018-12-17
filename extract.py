# encoding:utf-8
import re
from lxml import etree


def extract_data(company_url, html):
    x_html = etree.HTML(html)
    data = dict()
    companylogo=x_html.xpath('//div[@class="top_info_wrap"]/img/@src')
    if companylogo:
        data['companyLogo'] = companylogo[0][2:]
    data['companyFullName'] = re.findall('<div.*?company_main.*?title="(.*?)">', html, re.S)[0]
    data['homepage'] = re.findall('<div.*?company_main.*?href="(.*?)"', html, re.S)[0]
    data['industryField'] = re.findall('公司基本信息.*?type.*?<span>(.*?)</span>', html, re.S)[0]
    data['financeStage'] = re.findall('公司基本信息.*?process.*?<span>(.*?)</span>', html, re.S)[0]
    data['population'] = re.findall('公司基本信息.*?number.*?<span>(.*?)</span>', html, re.S)[0]
    data['city'] = re.findall('公司基本信息.*?address.*?<span>(.*?)</span>', html, re.S)[0]
    data['companyShortName'] = re.findall('<div.*?company_main.*?公司">(.*?)</a>', html, re.S)[0].strip()
    data['companyFeatures'] = re.findall('<div.*?company_word">(.*?)</div>', html, re.S)[0].strip()
    data['tags'] = re.findall('<li.*?con_ul_li">\s+(.*?)\s+</li>', html, re.S)
    data['addresses'] = re.findall('公司位置.*?mlist_li_desc">(.*?)</p>', html, re.S)[0].strip()
    intro = x_html.xpath('//*[@class="company_content"]/p/text()')
    if intro:
        data['intro'] = intro
    else:
        data['intro'] = ''
    data['companyId'] = re.findall('<script id="companyInfoData".*?companyId":(.*?),', html, re.S)[0]
    history_list = []
    histories = x_html.xpath('//ul[@class="history_ul"]/li')
    if not histories:
        data['histories'] = history_list
    for item in history_list:
        items = dict()
        history = etree.fromstring(etree.tostring(item))
        date_day = history.xpath('//*[@class="date_day"]/text()')
        date_year = history.xpath('//*[@class="date_year"]/text()')
        try:
            items['history_date'] = date_year[0] + date_day[0]
        except IndexError:
            items['history_date'] = ''
        history_url = history.xpath('//p/@data-href')
        if history_url:
            items['history_url'] = history_url
        else:
            items['history_url'] = ''
        history_title = history.xpath('//*[@class="desc_title desc_hover clearfix"]//a[1]/text()')
        if history_title:
            items['history_date'] = history_title[0].strip()
        desc_intro1 = history.xpath('//div[@class="desc_intro"]/p/text()')
        desc_intro1 = ''.join(desc_intro1).strip()
        desc_intro2 = history.xpath('//div[@class="desc_intro"]/text()')
        desc_intro2 = ''.join(desc_intro2).strip()
        if desc_intro1:
            items['desc_intro'] = desc_intro1
        elif desc_intro2:
            items['desc_intro'] = desc_intro2
        else:
            items['desc_intro'] = ''
        history_list.append(items)
    data['histories'] = history_list
    products = []
    company_products = x_html.xpath('//*[@id="company_products"]/div[2]/div')
    if not company_products:
        data['products'] = products
    for item in company_products:
        items = dict()
        product = etree.fromstring((etree.tostring(item)))
        product_img = product.xpath('//img/@src')
        if product_img:
            items['product_img'] = product_img[0][2:]
        else:
            items['product_img'] = ''
        product_url = product.xpath('//div[@class="product_url"]/a/@href')
        if product_url:
            items['product_url'] = product_url[0]
        else:
            items['product_url'] = ''
        product_profile1 = product.xpath('//div[@class="product_profile"]/p/text()')
        product_profile1 = ''.join(product_profile1).strip()
        product_profile2 = product.xpath('//div[@class="product_profile"]/text()')
        product_profile2 = ''.join(product_profile2).strip()
        if product_profile1:
            items['product_profile'] = product_profile1
        elif product_profile2:
            items['product_profile'] = product_profile2
        else:
            items['product_profile'] = ''
        products.append(items)
    data['products'] = products
    data['approve'] = re.findall('<script id="companyInfoData".*?approve":(\d),', html, re.S)[0]
    data['dataInfo'] = re.findall('<script id="companyInfoData".*?dataInfo":({.*?}),', html, re.S)[0]
    manager_list = []
    managers = x_html.xpath('//ul[@class="manager_list"]/li')
    for item in managers:
        items = dict()
        manager = etree.fromstring(etree.tostring(item))
        manager_name = manager.xpath('//*[@class="item_manager_name"]/span/text()')
        if manager_name:
            items['manager_name'] = manager_name[0]
        manager_img = manager.xpath('//*[@class="item_manger_photo_show"]/@src')
        if manager_img:
            items['manager_img'] = manager_img[0][2:]
        manager_title = manager.xpath('//*[@class="item_manager_title"]/text()')
        if manager_title:
            items['manager_title'] = manager_title[0]
        manager_intro_1 = manager.xpath('//*[@class="item_manager_content"]/p/text()')
        manager_intro_2 = manager.xpath('//*[@class="item_manager_content"]/text()')
        if manager_intro_1:
            items['manager_intro'] = ''.join(manager_intro_1)
        elif manager_intro_2:
            items['manager_intro'] = ''.join(manager_intro_2)
        else:
            items['manager_intro'] = ''
        manager_list.append(items)
    data['managers'] = manager_list
    data.setdefault('companyUrl', company_url)
    return data
