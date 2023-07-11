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

'''
經濟部 水利署 焦點
'''


def scrabing():

    # 建立Chromedriver執行檔位置
    s = Service("chromedriver.exe")

    # 設定瀏覽器為googleChrome
    driver = webdriver.Chrome(service=s)

    # 設定網址
    url = "https://www.wra.gov.tw/News.aspx?n=6430&sms=9122"

    # 設定"主頁面"網址
    url_original = "https://www.dorts.gov.taipei/"

    # 指定前往的網頁
    driver.get(url)

    # 要打開 不然沒辦法點時間框框
    driver.maximize_window()

    # 跳轉到新網頁，時停5秒讓網頁load資料
    time.sleep(3)

    # 上述整合成二維資料
    merge_2D = []

    # 上述整合成二維資料，後續再轉成字典型態資料
    merge_dict = []
    dict_final = []

    soup = BeautifulSoup(driver.page_source, "html.parser")

    # 最大範圍
    table = soup.find('table', {'id': "table_0"}).tbody

    # 每一列
    rows = table.find_all('tr')

    for row in rows:
        # 標題
        title = row.find_all('td')[0].text

        # 日期
        date = row.find_all('td')[1].string

        # 後半段網址
        url_back = row.find_all('td')[0].span.a.get('href')

        url = url_original + url_back

        # 年分 日期的前3個字元
        year = int(date[:3])

        # 改成西元年分 (+1911)
        year_vids = year + 1911

        # 組合成西元 日期
        dt_vids = str(year_vids) + date[3:]

        # 轉換成時間格式資料
        dt = datetime.strptime(dt_vids, "%Y-%m-%d")

        # 只要 7天內的 資料
        if dt >= seven_day_ago:
            dt = dt.strftime("%Y-%m-%d")
            merge_2D.append([title, dt, url])
            merge_dict.append([title, dt, url])
        else:
            break

    key = ["標題", "發布時間"]

    for merge_part in merge_dict:
        # 鍵值合併
        dict_merge_data = dict(zip(key, merge_part))
        dict_final.append(dict_merge_data)

    # 回傳 二維陣列資料
    return merge_2D

    # 回傳 字典型態資料
    # return dict_final


if __name__ == '__main__':
    # 當天日期
    today = datetime.today()
    # 當天日期的7天前
    seven_day_ago = today - timedelta(days=7)

    list_1 = scrabing()

