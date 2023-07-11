# 寫入資料庫前準備，連線、設定執行語法(cursor)

# 連線參數設定  依照各使用者資訊 輸入資料
dbhost = ""

dbuser = ""

dbpassword = ""

dbname = ""

# 資料庫連線設定
db = pymysql.connect(host=dbhost, user=dbuser, password=dbpassword, database=dbname, charset="utf8")

# 建立操作游標
cursor = db.cursor()

# ======================================================================================




# ======================================================================================
# 寫入資料庫

# 寫入指令 依照各使用者的資料庫table資訊 輸入資料
sql = "INSERT INTO kousiong_mrt(title , unit,dt ,click_num, url ) VALUES (%s,%s,%s,%s,%s)"

# 建立"防止多次寫入"機制(避免寫入重複資料)
# 邏輯：SELECT * FROM kousiong_mrt WHERE title = "寫入資料的標題"，看看底下"Resulr Grid"是否有顯示出資料


for i in list1:
    i0 = i[0]
    com = 'SELECT * FROM kousiong_mrt WHERE title = %s '
    strt = (i0)

    cursor.execute(com, strt)

    # 重點注意：cursor.fetchall()指令，顯示出"資料庫底下"Result Grid"全部資料
    # 如果沒有資料，則該指令長度為"0"，若是有資料，該指令長度則為"1"
    search_all = cursor.fetchall()



    if len(search_all) == 0:
        print("add")
        print("i0 = ", i0)

        try:

            cursor.execute(sql, i)

            # 提交修改
            db.commit()
            print('success')


        except pymysql.Error as e:
            # 發生錯誤時停止執行SQL
            db.rollback()
            print('error = ', str(e))

cursor.close()
db.close()
