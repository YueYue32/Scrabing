# sl
scrabing

# 程式內的這段，"chromedriver.exe"需定期更新，否則程式會跳出瀏覽器版本不相應的錯誤
# google瀏覽器執行檔下載位置：https://chromedriver.chromium.org/downloads
# 通常需要下載最新版，不過依照執行程式後，run中顯示的版本後碼為準

# 建立Chromedriver執行檔位置
s = Service("chromedriver.exe")

# 設定瀏覽器為googleChrome
driver = webdriver.Chrome(service=s)
