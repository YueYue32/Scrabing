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
import os


# 爬蟲功能(爬圖片)
def scrabing():

    url_list = []

    soup = BeautifulSoup(driver.page_source, "html.parser")

    part = soup.find_all("div", class_="media-item")

    for item in part:

        imgs = item.find("div", class_="media-download")

        size = imgs.find_all("a")[1]
        url_back = size["href"]

        url = url_front + url_back
        url_list.append(url)


    return url_list


# 儲存圖片功能
def write_in_images(url_list):
    # name計數器，用於下載圖片後，每一張圖片的命名編號起始點
    name = 1
    for i in url_list:
        print("圖片網址：", i, "儲存成檔案 img_%d" % name)
        # print(i['src'])

        # 取得該圖片，i['src']是圖片的網址
        jpg = requests.get(i)

        # open() 函數用於打開一個文件
        # "wb"，以二進制執行的w(因為圖片檔案是二進位制)
        # "w"，打開指定文件
        f = open(f'C:/Users/226083/PycharmProjects/pythonProject1/new_taipei_imgs/img_{name}.jpg', 'wb')

        # .content，返回的是bytes型數據(二進位制)，一般適用於圖片、文件(把圖片轉成二進制的)
        f.write(jpg.content)

        # 關閉檔案，這可有可無
        f.close()

        # 每爬一張圖，編號+1，用於儲存檔案的名稱
        name = name + 1

    print("總共%d" % name, "張圖")


if __name__ == '__main__':

    # 建立Chromedriver執行檔位置
    s = Service("chromedriver.exe")

    # 設定瀏覽器為googleChrome
    driver = webdriver.Chrome(service=s)

    # 要爬的網址
    imgs_url = "https://www.taiwan.net.tw/m1.aspx?sNo=0012076"

    url_front = "https://www.taiwan.net.tw"

    # 前往該網址
    driver.get(imgs_url)

    # 時停3秒
    time.sleep(3)

    # 進入網站後，呼叫爬蟲功能
    img = scrabing()

    # 資料夾路徑
    path = "C:/Users/226083/PycharmProjects/pythonProject1/new_taipei_imgs"

    # 如果沒有該資料夾，就先建立一個，再執行儲存圖片
    if not os.path.isdir(path):
        os.mkdir(path)
        write_in_images(url_list=img)

    # 如果已經有該資料夾，就直接執行儲存圖片(會覆蓋原資料夾內"同名"的檔案)
    else:
        write_in_images(url_list=img)
