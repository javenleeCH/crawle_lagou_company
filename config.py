# encoding:utf-8
json_headers = {'User-Agent':
                    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
                'Host': 'www.lagou.com',
                'Referer': 'https://www.lagou.com/gongsi/',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Connection': 'keep-alive',
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Accept - Encoding': 'gzip, deflate, br',
                'Accept - Language': 'zh-CN,zh;q=0.9,en-GB;q=0.8,en;q=0.7',
                'X-Anit-Forge-Code': '0',
                'X-Anit-Forge-Token': None,
                'X-Requested-With': 'XMLHttpRequest',
                # 'Cookie': 'WEBTJ-ID=20181214142255-167ab61d7cd341-0af0a74307ed6e-b78173e-2073600-167ab61d7cebb5; _ga=GA1.2.1734497476.1544768576; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1544768576; user_trace_token=20181214142256-b2613732-ff68-11e8-8cef-5254005c3644; LGSID=20181214142256-b2613893-ff68-11e8-8cef-5254005c3644; PRE_UTM=m_cf_cpt_baidu_pc; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Fs%3Fie%3DUTF-8%26wd%3D%25E6%258B%2589%25E5%258B%25BE; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flp%2Fhtml%2Fcommon.html%3Futm_source%3Dm_cf_cpt_baidu_pc; LGUID=20181214142256-b2613a4d-ff68-11e8-8cef-5254005c3644; _gid=GA1.2.1021171526.1544768576; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22167ab61e215228-0cdbce5004e699-b78173e-2073600-167ab61e21611cf%22%2C%22%24device_id%22%3A%22167ab61e215228-0cdbce5004e699-b78173e-2073600-167ab61e21611cf%22%2C%22props%22%3A%7B%22%24latest_utm_source%22%3A%22m_cf_cpt_baidu_pc%22%7D%7D; _putrc=A40A6D74B50EBAB2; login=true; unick=%E6%98%8E%E6%98%8E; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; gate_login_token=964c8c7541c0bd84d4e68b598281614fdd02f26ceca2b5d1; index_location_city=%E6%AD%A6%E6%B1%89; TG-TRACK-CODE=index_company; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1544769757; LGRID=20181214144238-725e856b-ff6b-11e8-918f-525400f775ce'
                }
gongsi_headers = {'User-Agent':
                      'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
                  'Referer': 'https://www.lagou.com/gongsi/',
                  'Host': 'www.lagou.com',
                  'Connection': 'keep-alive',
                  'Cookie': 'WEBTJ-ID=20181214142255-167ab61d7cd341-0af0a74307ed6e-b78173e-2073600-167ab61d7cebb5; _ga=GA1.2.1734497476.1544768576; _gat=1; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1544768576; user_trace_token=20181214142256-b2613732-ff68-11e8-8cef-5254005c3644; LGSID=20181214142256-b2613893-ff68-11e8-8cef-5254005c3644; PRE_UTM=m_cf_cpt_baidu_pc; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Fs%3Fie%3DUTF-8%26wd%3D%25E6%258B%2589%25E5%258B%25BE; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flp%2Fhtml%2Fcommon.html%3Futm_source%3Dm_cf_cpt_baidu_pc; LGUID=20181214142256-b2613a4d-ff68-11e8-8cef-5254005c3644; _gid=GA1.2.1021171526.1544768576; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22167ab61e215228-0cdbce5004e699-b78173e-2073600-167ab61e21611cf%22%2C%22%24device_id%22%3A%22167ab61e215228-0cdbce5004e699-b78173e-2073600-167ab61e21611cf%22%2C%22props%22%3A%7B%22%24latest_utm_source%22%3A%22m_cf_cpt_baidu_pc%22%7D%7D; sm_auth_id=falh57r635647tai; _putrc=A40A6D74B50EBAB2; login=true; unick=%E6%98%8E%E6%98%8E; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; gate_login_token=964c8c7541c0bd84d4e68b598281614fdd02f26ceca2b5d1; index_location_city=%E6%AD%A6%E6%B1%89; TG-TRACK-CODE=index_company; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1544768655; LGRID=20181214142415-e170db36-ff68-11e8-8cef-5254005c3644"; _putrc=""; _gat=1; LGRID=20181206102058-9164354f-f8fd-11e8-8cc6-525400f775ce; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1544062857'}
page_headers = {'User-Agent':
                    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
                'Referer': 'https://www.lagou.com/gongsi/',
                'Host': 'www.lagou.com',
                'Connection': 'keep-alive',
                'Accept': 'image / webp, image / apng, image / *, * / *;q = 0.8',
                'Accept - Encoding': 'gzip, deflate, br',
                'Accept - Language': 'zh-CN,zh;q=0.9,en-GB;q=0.8,en;q=0.7',
                # 'X_Anti_Forge_Token': self.Token,
                # 'X_Anti_Forge_Code':self.Code
                }
# 不限0 北京2 上海3 深圳215 广州213 杭州6 成都252 南京79 武汉184 西安298 厦门129 长沙198 苏州80 天津4
COMPANY_POSITION = [0]
# COMPANY_POSITION = [str(position) for position in COMPANY_POSITION]

# 不限0 未融资1 天使轮2 A轮3 B轮4 C轮5 D轮及以上6 上市公司7 不需要融资8
COMPANY_FINANCE_STAGE = [0]

# 不限0 移动互联网24 电子商务25 金融33 企业服务27 教育29 文化娱乐45 游戏31 O2O(28) 硬件47 医疗健康34
# 生活服务35 广告营销43 旅游32 数据服务41 社交网络26 分类信息48 信息安全38 招聘49 区块链15793 人工智能15794 其他10594
COMPANY_FIELD = [0]

# 不限0 少于15人1 15-50人2 50-150人3 150-500人4 500-2000人5 2000以上6
COMPANY_SIZE = [0]
