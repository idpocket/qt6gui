'''


v2.0.0
'''
import re
import time
from threading import Thread

from selenium import webdriver

from selenium.webdriver.common.by import By


# addnum = int(input('输入点赞数:'))
option = webdriver.ChromeOptions()
option.add_argument('headless')
# for _ in range(addnum):
#     browser = webdriver.Chrome(chrome_options=option)
#     url = 'http://java.newswz.cn/newinvest/integrity/votered2?id=5113'
#     browser.get(url)
#     time.sleep(2)
#     html = browser.page_source
#     xp = '//*[@id="button"]'
#     bt = browser.find_element(By.ID, 'button')
#     # 正则表达
#     pa = re.compile(f'<span>(.*?)赞</span>')
#     i = pa.findall(html)[0]
#     i = int(i)
#     bt.click()
#     print(f'现在点赞数为：{i}')

#退出


def run():

    browser = webdriver.Chrome(chrome_options=option)
    url = 'http://java.newswz.cn/newinvest/integrity/votered2?id=5113'
    # num = int(input('增加点赞数：'))
    browser.get(url)
    html = browser.page_source
    pa = re.compile(f'<span>(.*?)赞</span>')
    i = pa.findall(html)[0]
    print(f'初始点赞数{i}')
    for _ in range(1):

        browser.get(url)
        time.sleep(1)
        html = browser.page_source
        xp = '//*[@id="button"]'
        bt = browser.find_element(By.ID, 'button')

        bt.click()
        time.sleep(1)
        alert = browser.switch_to.alert
        alert.accept()
        # time.sleep(1)
        # browser.quit()


        print(f'点赞成功{_}次')
    browser.get(url)
    html = browser.page_source
    pa = re.compile(f'<span>(.*?)赞</span>')
    i = pa.findall(html)[0]
    print(f"最终点赞数：{i}")
# pa = re.compile(f'<span>(.*?)赞</span>')
# i = pa.findall(html)[0]
# print(i)


# browser.quit()

# print(browser.page_source)
# browser.close()

# num = int(input('增加点赞数：'))
# num =int(input(f'输入点赞数：'))
def run2(num):
    num=num
    n = 1
    s = 0
    browser = webdriver.Chrome(chrome_options=option)
    url = 'http://java.newswz.cn/newinvest/integrity/votered2?id=5113'
    # num = int(input('增加点赞数：'))
    browser.get(url)
    html = browser.page_source
    pa = re.compile(f'<span>(.*?)赞</span>')
    i = pa.findall(html)[0]
    print(f'初始点赞数{i}')

    while num:
        try:
            s= s+1
            browser.get(url)
            time.sleep(0.5)
            html = browser.page_source
            xp = '//*[@id="button"]'
            bt = browser.find_element(By.ID, 'button')
            bt.click()
            time.sleep(0.5)
            alert = browser.switch_to.alert
            alert.accept()
            print(f'点赞了{s}次')
            num = num-1
        except:
            pass


    browser.get(url)
    html = browser.page_source
    pa = re.compile(f'<span>(.*?)赞</span>')
    i = pa.findall(html)[0]
    print(f"最终点赞数：{i}")


# t1 = Thread(target=run2,args=(10,))
# time.sleep(1)
# t2 = Thread(target=run2,args=(10,))
# time.sleep(1)
# t3 = Thread(target=run2,args=(10,))
# t1.start()
# t2.start()
# t3.start()
# t1.join()
# t2.join()
# t3.join()
t = []
for _ in range(40):
    dz = Thread(target=run2,args=(500,))
    t.append(dz)
for _ in t:
    _.start()
    time.sleep(1)
for _ in range(t):
    _.join()

