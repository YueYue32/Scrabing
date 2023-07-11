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
新北市政府捷運工程局 市政新聞
'''

def scrabing():
    list_merge = []
    soup = BeautifulSoup(driver.page_source, "html.parser")
    table = soup.find('div', class_="listContainer mt-5 animatedParent animateOnce")

    rows = table.find_all('div', class_="row fs-5 item d-flex align-items-center animated fadeInUpShort go")

    for row in rows:

        # 發布日期
        dt = row.find("div", class_="col-4 col-md-3 col-lg-2").span.string
        dt_format = datetime.strptime(dt, "%Y-%m-%d")
        date_time = datetime.strftime(dt_format, "%Y/%m/%d")

        # 標題
        title = row.find("div", class_="col-8 col-md-9 col-lg-10").span.string

        # 後半段 網址
        url_part = row.find("div", class_="col-8 col-md-9 col-lg-10").a.get('href')

        # 合併網址
        url = main_url + url_part

        if date_time >= seven_day_ago:
            list_merge.append([title, date_time, url])
        else:
            break

    print(list_merge)
    return list_merge


if __name__ == '__main__':
    # 建立Chromedriver執行檔位置
    s = Service("chromedriver.exe")

    # 設定瀏覽器為googleChrome
    driver = webdriver.Chrome(service=s)

    # 設定等待時間上限10秒
    # driver.implicitly_wait(10)
    main_url = "https://www.dorts.ntpc.gov.tw/news"

    # 當天日期
    today = datetime.today()
    # 當天日期的7天前
    seven_day_ago = today - timedelta(days=7)
    seven_day_ago = seven_day_ago.strftime("%Y/%m/%d")

    driver.delete_all_cookies()
    driver.get(main_url)
    time.sleep(10)

    list_1 = scrabing()

