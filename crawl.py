# encoding:utf-8、
import requests
import re
import time
from lagou_company import config
import json
import random
import socket
from lagou_company import extract
from retrying import retry


class lagou():
    """
    step1:初始化
    step2:访问'https://a.lagou.com/collect'得到cookie，session 保存
    step3:访问具体公司接口，得到html，提取数据
    step4:由于不同数据接口，cookie在变化，所以再循环2-3
    step5:根据筛选条件，翻页访问得到所有公司的url,遍历---step3
    """

    def __init__(self):
        headers = config.gongsi_headers
        self.session = requests.session()
        self.response = self.session.get('https://www.lagou.com/gongsi/', headers=headers)
        self.title = re.findall('<title>(.*?)</title>', self.response.text)[0]
        # print(self.title)
        # print(self.session.cookies)
        self.get_cookie('https://www.lagou.com/gongsi/', self.title)
        # print(self.session.cookies)

    # 每次访问公司数据接口前，都要拿到cookie
    def get_cookie(self, company_url, title):
        url = 'https://a.lagou.com/collect'
        headers = {'User-Agent':
                       'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
                   'Referer': company_url,
                   'Accept': 'image / webp, image / apng, image / *, * / *;q = 0.8',
                   'Accept - Encoding': 'gzip, deflate, br',
                   'Connection': 'keep - alive',
                   'Host': 'a.lagou.com',
                   }
        params = {'v': '1',
                  '_v': 'j31',
                  'a': '1328310556',
                  't': 'pageview',
                  '_s': '1',
                  'dl': company_url,
                  'dr': 'https://www.lagou.com/gongsi/',
                  'ul': 'zh-cn',
                  'de': 'UTF-8',
                  'dt': title,
                  'sd': '24-bit',
                  'sr': '1920x1080',
                  'vp': '693x921',
                  'je': '0',
                  '_u': 'MACAAAQBK~',
                  'jid': '',
                  'cid': '1300984840.1537927701',
                  'tid': 'UA-41268416-1',
                  'z': '86864211'
                  }
        self.session.get(url, headers=headers, params=params)

    @retry(retry_on_exception=IndexError, wait_fixed=2)
    def get_company_html(self, company_url):
        headers = config.page_headers
        response1 = self.session.get(company_url, headers=headers)
        title = re.findall('<title>(.*?)</title>', response1.text)[0]
        print(title)
        self.get_cookie(company_url, title)
        return response1.text

    # 根据筛选条件（可在config中修改）翻页得到所有公司url
    def get_company_url_list(self):
        headers = config.json_headers
        company_url_list = []
        company_position = config.COMPANY_POSITION
        company_finance_stage = config.COMPANY_FINANCE_STAGE
        company_filed = config.COMPANY_FIELD
        company_size = config.COMPANY_SIZE
        for position in company_position:
            for finance_stage in company_finance_stage:
                for filed in company_filed:
                    for size in company_size:
                        filter_condition = '{}-{}-{}-{}'.format(position, finance_stage, filed, size)
                        url = 'https://www.lagou.com/gongsi/' + filter_condition + '.json'
                        for pageNum in range(1, 2):
                            data = {'first': 'false', 'pn': pageNum, 'sortField': 0, 'havemark': 0}
                            socket.setdefaulttimeout(20)
                            # print(self.session.cookies)
                            response = self.session.post(url, headers=headers, data=data)
                            try:
                                response_result = json.loads(response.text)['result']
                                if not response_result:
                                    break
                                company_id = re.findall('"companyId":(.*?),', response.text)
                                response.close()
                                print(filter_condition, pageNum)
                                for id in company_id:
                                    company_page_url = 'https://www.lagou.com/gongsi/{company_id}.html'.format(
                                        company_id=id)
                                    company_url_list.append(company_page_url)
                            except json.decoder.JSONDecodeError:
                                print(1)
                                continue
                            time.sleep(20)
                    self.get_cookie(url, self.title)
        return company_url_list

    def main(self, company_url):
        html = self.get_company_html(company_url)
        company_data = extract.extract_data(company_url,html)
        return company_data


if __name__ == '__main__':
    start = time.process_time()
    a = lagou()
    result = []
    company_url_list = list(set(a.get_company_url_list()))
    print(len(company_url_list))
    for companyUrl in company_url_list[:3]:
        company_data = a.main(companyUrl)
        print(company_data)
        result.append(company_data)
        print("爬取第{}个公司".format(len(result)))
        time.sleep(random.uniform(1, 2))
    end = time.process_time()
    print("所需时间：{}s".format(end - start))
