# scrabing
scrabing 爬蟲程式，每支程式中皆有註解說明爬的網站是哪個網站

# 

程式內的這段
s = Service("chromedriver.exe")

"chromedriver.exe"需定期更新，否則程式會跳出瀏覽器版本不相應的錯誤，通常需要下載最新版，不過依照執行程式後，"run中顯示的版本序號為準"

下載後的"chromedriver.exe"，檔案的放置位置和爬蟲程式相同的資料夾下

# 

# google瀏覽器執行檔下載位置：
https://chromedriver.chromium.org/downloads


#


# write_in_mysql_example.py
執行完爬蟲程式後，將資料寫入MYSQL資料庫
"內容僅為範例，依各使用者調整資料庫參數設定、資料庫table名稱、資料庫欄位"
