学习笔记

# Day01

## 异常处理

为了处理异常，我们使用try...except把可能发生错误的语句放在try模块里，用except来处理异常。except可以处理一个专门的异常，也可以处理一组圆括号中的异常，如果except后没有指定异常，则默认处理所有的异常。每一个try，都必须至少有一个except

在python的异常中，有一个万能异常：Exception，他可以捕获任意异常

```python
s1 = 'hello'
try:
  int(s1)
except Exception,e:
  print e
```

程序时需要考虑到try代码块中可能出现的多个异常，可以这样写：

```python
s1 = 'hello'
try:
  int(s1)
except IndexError,e:
  print e
except KeyError,e:
  print e
except ValueError,e:
  print e
```

主动触发异常

```python
try:
  raise Exception('错误了。。。')
except Exception,e:
  print e
```

自定义异常

```python
class WupeiqiException(Exception):
  
  def __init__(self, msg):
    self.message = msg
  
  def __str__(self):
    return self.message
  
try:
  raise WupeiqiException('我的异常')
except WupeiqiException,e:
  print e
```

# Day02

## pymysql 初识

简单使用

```python
import pymysql
import datetime

host = 'localhost'
username = 'root'
password = '12345678'
db_name = 'test'

create_table_sql = """\
CREATE TABLE fuck(
id INT AUTO_INCREMENT PRIMARY KEY,
username VARCHAR(255) UNIQUE ,
nickname VARCHAR(255) NOT NULL ,
birthday DATE
)
"""

insert_table_sql = """\
INSERT INTO fuck(username,nickname,birthday)
 VALUES('{username}','{nickname}','{birthday}')
"""
query_table_sql = """\
SELECT id,username,nickname,birthday
FROM fuck 
"""

delete_table_sql = """\
DELETE FROM fuck 
"""

drop_table_sql = """\
DROP TABLE fuck
"""

connection = pymysql.connect(host=host,
                             user=username,
                             password=password,
                             charset='utf8mb4',
                             db=db_name)

try:
    with connection.cursor() as cursor:
        print('--------------新建表--------------')
        cursor.execute(create_table_sql)
        connection.commit()
        print('--------------插入数据--------------')
        cursor.execute(
            insert_table_sql.format(username='yitian', nickname='易天', birthday=datetime.date.today()))
        cursor.execute(
            insert_table_sql.format(username='zhang3', nickname='张三', birthday=datetime.date.today()))
        cursor.execute(
            insert_table_sql.format(username='li4', nickname='李四', birthday=datetime.date.today()))
        cursor.execute(
            insert_table_sql.format(username='wang5', nickname='王五', birthday=datetime.date.today()))
        connection.commit()

        print('--------------查询数据--------------')
        cursor.execute(query_table_sql)
        results = cursor.fetchall()
        print(f'id\tname\tnickname\tbirthday')
        for row in results:
            print(row[0], row[1], row[2], row[3], sep='\t')

        print('--------------清除数据--------------')
        cursor.execute(delete_table_sql)
        connection.commit()

        print('--------------删除表--------------')
        cursor.execute(drop_table_sql)
        connection.commit()
finally:
    connection.close()
```

## fake-useragent

- **用法**
  引入，生成实例：

```text
from fake_useragent import UserAgent
ua = UserAgent()
```

如果报错 `fake_useragent.errors.FakeUserAgentError: Maximum amount of retries reached` 首先检查网络，然后：如果不希望缓存数据库或不需要可写文件系统：

```text
ua = UserAgent(cache=False)
```

如果不想使用宿主缓存服务器，可以禁用服务器缓存：

```python
ua = UserAgent(use_cache_server=False)
```

如果以上方法均报错，执行：

```text
ua = UserAgent(verify_ssl=False)
```

由于 fake-useragent 库维护的 user-agent 列表存放在在线网页上过低版本依赖的列表网页可能就会报 404 随手更新：

```python
ua.update()
```

查看全部 user-agent ：

```python
ua.data_browsers

In [20]: len(reduce(lambda a, b: a+b, ua.data_browsers.values()))
Out[20]: 250
```

获取随机值：

```python
In [26]: ua.random
Out[26]: 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) 
Chrome/31.0.1650.16 Safari/537.36'
```

## cookies 验证

如果你向同一主机发送多个请求，每个请求对象让你能够跨请求保持session和cookie信息，这时我们要使用到requests的Session()来保持回话请求的cookie和session与服务器的相一致。

示例5.1：创建一个session会话：

```python3
s = requests.Session()

session会话的get与post请求
# 不带可选参数的get请求
>>> r = s.get(url='https://github.com/timeline.json')
# 不带可选参数的post请求
>>> r = s.post(url="http://httpbin.org/post")
```

session会话对象的get与post请求参数与requests()的get与post请求参数一致。



session会话还可以用作with前后文管理器：

示例5.2:

```python3
with requests.Session() as s:
   s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
```

这样能确保 with 区块退出后会话能被关闭，即使发生了异常也一样。



requests的session会话需要注意的是会话方法级别的参数也不会被跨请求保持。

如下示例5.3：

```python3
s = requests.Session()

r = s.get('http://httpbin.org/cookies', cookies={'from-my': 'browser'})
print(r.text)
# '{"cookies": {"from-my": "browser"}}'

r = s.get('http://httpbin.org/cookies')
print(r.text)
# '{"cookies": {}}'
```

第一个get请求中加入方法级别cookies参数，在第二个get请求中不会保持第一个get请求的cookies参数。

# Day03

## selenium 

引用及常量

```python3
url = 'https://www.xxx.xxx/'
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
```

驱动浏览器访问网页并获取当前窗口的hadle name

```python3
driver = webdriver.Chrome()#有界面的驱动chrome浏览器。
driver.maximize_window()#窗口最大化
wait = WebDriverWait(driver, 10)
driver.get(url)#访问制定网页
current_window = driver.current_window_handle  # 获取当前窗口handle name
```

等推荐弹窗加载完成后，模拟触发点击关闭按钮,因为可能会存在超时的问题，需要加上try catch

```text
    print('取消弹框')#操作日志
    cancel = wait.until(
    
    EC.presence_of_element_located((By.CSS_SELECTOR, "#j-homepage > div.g-wrap > div.m-guide-block.animated.bounceInDown > span"))
    )
    cancel.click()
    print('进入登陆页面')
```

输入账号、密码进行网页登陆

```text
    login = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "body > div.g-hd.f-cb > div.m-toolbar > div > ul > li:nth-child(6) > div > a.u-sign-btn.u-sign-in"))
    )
    login.click()
    print('输入账号、密码')
    name = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#j-cpn2"))
    )
    psw = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#j-password"))
    )
    name.send_keys('*******')
    psw.send_keys('*******')
    submit = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#j-login-submit"))
    )
    print('确定登陆')
    submit.click()
    time.sleep(3)#休息一会，怕被对方屏蔽
```

进入个人中心

```python3
    print('进入个人中心')
    geren = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "body > div.g-hd.f-cb > div.m-navbar.f-pos-r > div > ul > li.m-user-nav > a > img"))
    )
    geren.click()
    print('点击我的')
    chujie = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "body > div.g-bd.f-mh500.f-cf > div > div > div.m-page-sidebar > ul > li:nth-child(2) > a > span.title"))
    )
    chujie.click()
```

获取信息列表

因为已经获知每页10条，且共计190条，此处就省去自动获取分页列表长度的步骤。

```text
    for j in range(1,20):
        for i in range(1,11):
            print('遍历：第%d页'%j+'第%d条记录'%i)
            xiangqing =  wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#j-invest-table > tbody > tr:nth-child(%d) > td:nth-child(6) > a.u-eSignatue.u-op-link.z-current.j-eSignatue-finish"%i))
            )
            xiangqing.click()
            all_window=driver.window_handles
            #print(all_window)
            for window in all_window:
                if window != current_window:
                    driver.switch_to.window(window)
            current_window = driver.current_window_handle  # 获取当前窗口handle name
            #print(current_window)
            time.sleep(3)
```

**！关键性操作！**

**这一步是实现窗口切换，句柄切换的关键步骤。**

```text
            all_window=driver.window_handles#先获取打开的所有窗口的句柄
            #print(all_window)
            #遍历句柄，如果存在有句柄不是当前句柄（也就是有新打开的窗口），就把句柄切换到新的窗口。
            for window in all_window:
                if window != current_window:
                    driver.switch_to.window(window)
            current_window = driver.current_window_handle  # 获取当前窗口handle name
            #print(current_window)
            time.sleep(3)
```

进行新开窗口的操作，点击下载按钮

```text
            down =  wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#j-contract-download"))
            )
            down.click()
            reldown =  wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#j-download-box > span"))
            )
            reldown.click()
            time.sleep(3)
            driver.close()
            #切换回窗口A
            driver.switch_to_window(all_window[0]) 
            time.sleep(3)
```

翻页操作，翻页操作用的是selenium驱动js。

```text
        print('翻页')
        if j ==1:
            js = "document.getElementsByClassName('u-pnav-prev')[1].click()"
        else:
            js = "document.getElementsByClassName('u-pnav-prev')[2].click()"
        driver.execute_script(js)
        time.sleep(3)
```