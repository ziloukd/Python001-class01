'''验证码识别'''
# 需要安装依赖libpng, jepg, libjiff, lebtonica　和　tesseract
# python 需要安装的库有：Pillow, pytesseract

from fake_useragent import UserAgent
import requests
import os
from PIL import Image
import pytesseract
from lxml import etree

ua = UserAgent(verify_ssl=False)

def simulated_login():
    '''login_url:https://so.gushiwen.org/user/login.aspx?from=http%3a%2f%2fso.gushiwen.org%2fuser%2fcollect.aspx'''
    # 构造一个user-agent
    headers = {'User-Agent':ua.random}

    # 1.获取验证码图片
    # 1.1发起请求
    index_url = 'https://so.gushiwen.org/user/login.aspx?from=http%3a%2f%2fso.gushiwen.org%2fuser%2fcollect.aspx'
    html = requests.get(index_url, headers=headers).content.decode()

    # 1.2 解析响应，获得url
    tree = etree.HTML(html)
    url = 'https://so.gushiwen.org' + tree.xpath('//img[@alt="看不清，换一张"]/@src')[0]

    # 1.3下载图片
    if not os.path.exists('./imgs'):
        os.mkdir('./imgs')
    pic = requests.get(url, headers=headers)
    # print(pic.status_code)
    with open('./imgs/1.jpg', 'wb') as f1:
        f1.write(pic.content)

    # 2.识别验证码
    # 2.1 打开并显示文件
    im = Image.open('./imgs/1.jpg')

    # 2.2 灰度图片
    gray = im.convert('L')
    gray.save('./imgs/1_gray.jpg')
    im.close()

    # 2.3二值化
    threshold = 100
    table = []

    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    
    out = gray.point(table, '1')
    out.save('./imgs/2_gray.jpg')

    th = Image.open('./imgs/2_gray.jpg')
    code = pytesseract.image_to_string(th, lang='chi_sim+eng')

    # 3模拟登录
    print(code)
    s = requests.Session()
    form_data = {
        '__VIEWSTATE': 'sDqgIc1igzPvhqFj6mpsFdK7m8n6Os72+mL3PoXxlLO9cox1EnrskEbqT1CvR/+KBL7/LpciIJ+KloMIpWoGrjogUOUaD68MupWecdqcfIdj3UjaEJo7K8I7oow=',
        '__VIEWSTATEGENERATOR': 'C93BE1AE',
        'from': 'http://so.gushiwen.org/user/collect.aspx',
        'email': 'leiwuyu1@163.com',
        'pwd': 'test123456',
        'code': code,
        'denglu': '登录',
    }

    login_url = 'https://so.gushiwen.org/user/login.aspx?from=http%3a%2f%2fso.gushiwen.org%2fuser%2fcollect.aspx'
    res = s.post(url, headers=headers, data=form_data)
    res = s.get('https://so.gushiwen.org/user/collect.aspx', headers=headers)
    with open('./html.html', 'w', encoding='utf-8') as f1:
        f1.write(res.text)


simulated_login()

