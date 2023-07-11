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


def scrabing():
    list_merge = []
    soup = BeautifulSoup(driver.page_source, "html.parser")
    table = soup.find('div', class_="news-home")

    rows = table.find_all('div', class_="col-md-12 home-news-loop")

    for row in rows:

        # 發布日期
        dt = row.a.h3.span.string
        dt_format = datetime.strptime(dt, "%Y-%m-%d")
        date_time = datetime.strftime(dt_format, "%Y/%m/%d")

        # 標題
        title = row.a.h3.text.replace(dt, "").strip()

        # 網址
        url = row.a.get('href')

        list_merge.append([date_time, title, url])

    print(list_merge)
    return list_merge


if __name__ == '__main__':
    # 建立Chromedriver執行檔位置
    s = Service("chromedriver.exe")

    # 設定瀏覽器為googleChrome
    driver = webdriver.Chrome(service=s)

    # 設定等待時間上限10秒
    # driver.implicitly_wait(10)
    main_url = "https://www.turc.org.tw/tw/modules/news/?storytopic=1"

    # 當天日期
    today = datetime.today()
    # 當天日期的7天前
    seven_day_ago = today - timedelta(days=7)
    seven_day_ago = seven_day_ago.strftime("%Y/%m/%d")

    driver.delete_all_cookies()
    driver.get(main_url)
    time.sleep(2)

    list_1 = scrabing()
