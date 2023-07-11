# import套件
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time
import csv
import openpyxl
import pymysql
from datetime import datetime

# 建立Chromedriver執行檔位置
s = Service("chromedriver.exe")


over_18_header = {"cookie": "over18=1"}

# 設定瀏覽器為googleChrome
driver = webdriver.Chrome(service=s)

ppt_url = "https://www.ptt.cc/bbs/Beauty/M.1670539605.A.390.html"

driver.get(ppt_url)

driver.add_cookie({'name': 'over18', 'value': '1'})

# web = requests.get(你想爬的網站)
# 因為是爬取PTT網站，所以會有詢問年齡('over18')的限制
# 2種寫法

# 第1種寫法：header
# cookie設定

# web = requests.get(ppt_url, headers=over_18_header)



# cookies={'over18':'1'}表示選取"超過18歲"的選項




# web = requests.get('https://www.ptt.cc/bbs/Beauty/M.1670539605.A.390.html', cookies={'over18':'1'})

# soup = BeautifulSoup(web.text, "html.parser")

time.sleep(5)


# # 選取階層，PTT表特版的階層不難，如下圖
# imgs = soup.find_all('img')
#
# # name計數器，用於下載圖片後，每一張圖片的命名編號起始點
# name = 0
#
# for i in imgs:
#     # print(i['src'])
#     print(i)
#     jpg = requests.get(i['src'])
#     f = open(f'C:/Users/226083/PycharmProjects/pythonProject1/bt_1/bt_{name}.jpg', 'wb')
#     f.write(jpg.content)
#     f.close()
#     name = name + 1