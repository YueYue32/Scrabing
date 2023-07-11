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
import random
from pynput.mouse import Button, Controller
from pynput import mouse


'''
經濟部 水利署
'''


def scrabing():
    # 建立操作單位
    # control = mouse.Controller()

    # 延遲的秒數
    # random.randint(1,4)

    # 建立Chromedriver執行檔位置
    s = Service("chromedriver.exe")

    # 設定瀏覽器為googleChrome
    driver = webdriver.Chrome(service=s)

    # 設定網址
    url = "https://www.wra.gov.tw/"

    # 指定前往的網頁
    driver.get(url)
    # driver.maximize_window()

    # 跳轉到新網頁，時停5秒讓網頁load資料
    time.sleep(3)

    soup = BeautifulSoup(driver.page_source, "html.parser")

    # 次範圍
    rows = soup.find('div', class_="current-info")

    # 上述整合
    merge_2D = []
    merge_dict = []

    parts = rows.find_all('div', class_="in")

    for part in parts:
        # 水庫名稱
        stat_title = part.find('div', class_="title").text.strip()  # len(title) == 12

        # 資料區域，包含水量、水量百分比
        data = part.find('div', class_="dyna-info")

        # 水量
        amount_of_water = data.find('div', class_="dam-cap").text.strip()
        amount_of_water = "蓄水量：" + str(amount_of_water) + "(單位：萬立方公尺)"

        # 水量百分比
        percentage_of_water = data.find('div', class_="dam-prop").text.strip()
        percentage_of_water = str(percentage_of_water) + "%"

        # 二維資料陣列
        merge_2D.append([stat_title, amount_of_water, percentage_of_water])

        # 二維資料陣列，後面用拿去變更成dict型態資料
        merge_dict.append([stat_title, amount_of_water, percentage_of_water])

    key = ["水庫名稱", "蓄水量(單位：萬立方公尺)", "蓄水量百分比(%)"]

    dict_final = []

    for merge_part in merge_dict:
        # 鍵值合併
        dict_merge_data = dict(zip(key, merge_part))
        # 字典型態資料格式
        dict_final.append(dict_merge_data)

    # 回傳 二維陣列資料
    return merge_2D

    # 回傳 字典型態資料
    # return dict_final


if __name__ == '__main__':
    list_1 = scrabing()

