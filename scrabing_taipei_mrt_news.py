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
import random
from pynput.mouse import Button, Controller
from pynput import mouse
from selenium.webdriver.support.select import Select

'''
臺北大眾捷運股份有限公司 新聞稿
'''


def scrabing():

    # 建立操作單位
    # control = mouse.Controller()

    # 建立Chromedriver執行檔位置
    s = Service("chromedriver.exe")

    # 設定瀏覽器為googleChrome
    driver = webdriver.Chrome(service=s)

    # 設定網址
    url = "https://www.metro.taipei/News.aspx?n=30CCEFD2A45592BF&sms=72544237BBE4C5F6#Accesskey_C"

    # 設定主網址
    url_front = "https://www.metro.taipei/"

    # 指定前往的網頁
    driver.get(url)
    driver.maximize_window()

    # 跳轉到新網頁，時停5秒讓網頁load資料
    time.sleep(2)


    # # 點擊 "每頁筆數"
    # select_category = Select(
    #     driver.find_element(By.ID,
    #                         'SelectNumOnPage'))
    #
    # time.sleep(1)
    #
    # select_category.select_by_value("200")
    #
    # time.sleep(2)
    #
    # # 按下 "每頁筆數" 右邊的小按鈕(執行)
    # bottun_next = driver.find_element(By.CLASS_NAME, "btn").click()

    time.sleep(1)

    soup = BeautifulSoup(driver.page_source, "html.parser")

    # 最大範圍
    table = soup.find('div', class_="area-table rwd-straight")

    # 次範圍 左邊 標題
    rows_title = table.find_all('td', class_="CCMS_jGridView_td_Class_1")

    # 次範圍 中間 日期
    rows_date = table.find_all('td', class_="CCMS_jGridView_td_Class_2")

    # 次範圍 右邊 發布單位
    rows_unit = table.find_all('td', class_="CCMS_jGridView_td_Class_3")

    # 裝 "標題"
    title_list = []

    # 裝 "日期"
    date_list = []

    # 裝 "發布單位"
    unit_list = []

    # 裝"網址"
    url_list = []

    # 上述整合成二維資料
    merge_2D = []

    # 上述整合成二維資料，後續再轉成字典型態資料
    merge_dict = []
    dict_final = []

    # 標題、網址區域
    for row_t in rows_title:
        # 標題
        title = row_t.span.a.string
        title_list.append(title)

        # 後半部網址
        url_back = row_t.span.a.get('href')
        # 合併網址
        url = url_front + url_back
        url_list.append(url)

    # 時間區域
    for row_d in rows_date:

        date = row_d.span.string

        # 年分 前3個字元
        year = int(date[:3])

        # 改成西元年分 (+1911)
        year_vids = year + 1911

        # 組合成西元 日期
        dt_vids = str(year_vids) + date[3:]

        # 改成時間格式的資料
        dt = datetime.strptime(dt_vids, "%Y-%m-%d")

        date_list.append(dt)

    # 單位區域
    for rows_u in rows_unit:
        unit = rows_u.span.string
        unit_list.append(unit)

    key = ["標題", "發布日期", "發布機關", '網址']

    for num in range(len(rows_title)):
        # 判斷只要 7天內 的資料
        if date_list[num] >= seven_day_ago:
            dt = date_list[num].strftime("%Y-%m-%d")

            # 二維陣列資料
            merge_2D.append([title_list[num], dt, unit_list[num], url_list[num]])

            # 二維陣列資料，後面會拿去合成成dict型態資料
            merge_dict.append([title_list[num], dt, unit_list[num], url_list[num]])

        else:
            break

    for merge_part in merge_dict:
        dict_merge_data = dict(zip(key, merge_part))
        # 字典型態資料格式
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

