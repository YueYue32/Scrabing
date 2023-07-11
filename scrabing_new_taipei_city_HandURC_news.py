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
from datetime import datetime, timedelta
import calendar

'''
新北市住宅及都市更新中心 新聞稿
'''

def scrabing():

    list_merge = []
    soup = BeautifulSoup(driver.page_source, "html.parser")

    # 整片資訊區域
    table = soup.find('div', class_="max-w-7xl mx-auto sm:px-6 lg:px-8 px-4")

    # 區塊 集
    rows = table.find_all('div', class_="space-y-2 sm:space-y-3 text-dark-500")

    # 每一區塊
    for row in rows:

        # 上半部 包含標題、發布時間
        upper = row.find('div', class_="leading-6")

        # 標題
        title = upper.h3.string

        # 網址
        url = upper.h3.a.get('href')

        # 時間
        dt = upper.p.string.replace(" ", "-")
        dt = datetime.strptime(dt, '%d-%b-%Y')
        dt = datetime.strftime(dt, '%Y-%m-%d')

        # 下半部，只有文章內容，所以不用lower命名
        article = row.find("div", class_="text-base").p.string

        # 只抓30天內資料
        if dt >= thirty_day_ago:
            list_merge.append([title, dt, article, url])
        else:
            break

    key = ["標題", "時間", "文章", "網址"]

    dict_final = []

    for merge_part in list_merge:
        # 鍵值合併
        dict_merge_data = dict(zip(key, merge_part))
        # 字典型態資料格式
        dict_final.append(dict_merge_data)

    # 回傳 二維陣列資料
    return list_merge

    # 回傳 字典型態資料
    # return dict_final

def sliderwindow():
    # 隨機滑動
    scroll_height = driver.execute_script("return document.body.scrollHeight")
    # print(scroll_height) #2722
    driver.execute_script('window.scrollBy(0,{})'.format(scroll_height))


if __name__ == '__main__':
    # 建立Chromedriver執行檔位置
    s = Service("chromedriver.exe")

    # 設定瀏覽器為googleChrome
    driver = webdriver.Chrome(service=s)

    # 設定等待時間上限10秒
    # driver.implicitly_wait(10)
    main_url = "https://www.nthurc.org.tw/news/press-release"

    month_dict = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06", "Jul": "07",
                  "Aug": "08",
                  "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}

    # 當天日期
    today = datetime.today()
    # 當天日期的30天前
    thirty_day_ago = today - timedelta(days=30)
    thirty_day_ago = thirty_day_ago.strftime("%Y-%m-%d")

    driver.delete_all_cookies()
    driver.get(main_url)
    time.sleep(3)
    sliderwindow()
    time.sleep(3)

    list_1 = scrabing()
