import cv2
import random
import numpy as np

# 輸入原圖
img = cv2.imread("C:/Users/226083/Desktop/opencv_test/mmax.jpg")
# np.set_printoptions(threshold=np.inf)
# print(img)
# kernel = np.ones((3,3),np.uint8)
# oo = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel, iterations = 2)

# 腐蝕
# kernal = np.ones((13, 13), np.uint8)
# erosion = cv2.erode(img, kernal, iterations=1)

# numpy.ndarray
# print(type(img))

# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# 高斯模糊
# blur_img = cv2.GaussianBlur(img, (0, 0), 3)

# usm = 原圖*係數1 - 高斯模糊圖*係數2
# cv2.addWeighted(原圖, 係數1, 高斯模糊圖, 係數2, 亮度調整)
# usm = cv2.addWeighted(img, 2, blur_img, -1, 0)

# 分離色彩空間
# img_lab = cv2.cvtColor(img, cv2.COLOR_BGR2Lab)
# L, a, b = cv2.split(img_lab)
B, G, R = cv2.split(img)



scharrx = cv2.Scharr(B, cv2.CV_64F, 1, 0)
scharrx = cv2.convertScaleAbs(scharrx)

scharry = cv2.Scharr(B, cv2.CV_64F, 0, 1)
scharry = cv2.convertScaleAbs(scharry)

scharrxy = cv2.addWeighted(scharrx, 0.8, scharry, 0.8, 3)


# 腐蝕
# kernel = np.ones((3,3),np.uint8)
# erosion = cv2.erode(L, kernel, iterations=1)
# opening = cv2.morphologyEx(L,cv2.MORPH_BLACKHAT,kernel, iterations = 2)
# gra = cv2.morphologyEx(opening,cv2.MORPH_GRADIENT,kernel, iterations = 2)




# 二值化
# rets, thresh = cv2.threshold(L, 80, 255, cv2.THRESH_BINARY)
rets, thresh = cv2.threshold(scharrxy, 88, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)


th2 = cv2.adaptiveThreshold(thresh, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 3)


# 取得輪廓
contourss, hierarchy = cv2.findContours(th2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 用於裝 "輪廓點" 集合資料
bounding_boxes = []

count = 0

blue = []
# 最小矩形
for cnt in contourss:

    box = cv2.minAreaRect(cnt)

    box = np.intp(cv2.boxPoints(box))  # –> int0會省略小數點後方的數字 # 改版 改成intp


    # 寬度
    weight = ((box[1][0] - box[0][0]) ** 2 + (box[1][1] - box[0][1]) ** 2) ** 0.5

    # 高度
    high = ((box[3][0] - box[0][0]) ** 2 + (box[3][1] - box[0][1]) ** 2) ** 0.5

    # 劃出全部結果 測試用
    # cv2.drawContours(img, [box], -1, (244, 0, 0), 2)


    # 綠線
    # if 70 < high < 100 and 200000 > weight * high > 20000:
    #     # print("weight =%s"%weight , "      ", "high =%s"%high , "        ", "area =%s "%(weight * high))
    #     cv2.drawContours(img, [box], -1, (0, 255, 0), 2)

    # 藍線
    # if weight > 30 and high > 50 and 50000 > weight * high > 20000 and (weight*2 + high*2) > 600:
    #
    #     # print("藍線區")
    #     print("weight =%s"%weight , "      ", "high =%s"%high , "        ", "area =%s "%(weight * high), "       ", "length =%s"%(weight*2 + high*2))
    #
    #     a = weight.astype(np.int64)
    #
    #
    #     blue.append(box.tolist())
    #     print("[box = ]", box)
    #     print("--------------------------------\n")
        # cv2.drawContours(img, [box], -1, (244, 0, 0), 2)

    # if 50000 > weight * high > 20000 and weight > 200:
    #     blue.append(box.tolist())

    # if 80000 > weight * high > 50000 and 150 > weight > 100:
    #     blue.append(box.tolist())

    if 150 > high > 80:
        blue.append(box.tolist())


data_blue = []

for an in blue:
    # print(an)
    blue_w = ((an[1][0] - an[0][0]) ** 2 + (an[1][1] - an[0][1]) ** 2) ** 0.5
    blue_h = ((an[3][0] - an[0][0]) ** 2 + (an[3][1] - an[0][1]) ** 2) ** 0.5
    blue_area = blue_w * blue_h
    print("aaa= ",blue_area)
    data_blue.append(blue_area)

    q = np.array(an)

    cv2.drawContours(img, [q], -1, (244, 0, 0), 2)


print("-------------")

for en in blue:
    blue_w = ((en[1][0] - en[0][0]) ** 2 + (en[1][1] - en[0][1]) ** 2) ** 0.5
    blue_h = ((en[3][0] - en[0][0]) ** 2 + (en[3][1] - en[0][1]) ** 2) ** 0.5
    blue_area = blue_w * blue_h
    # print("aaa= ",blue_area)

    if min(data_blue) == blue_area:
        print("bbbb", blue_area)
        print(np.array(en))
        g = np.array(en)

        cv2.drawContours(img, [g], -1, (244, 0, 0), 2)
        # print("bbbb", en[0][0])
        # print("bbbb", en[0][1])
        # print("bbbb", en[1][0])
        # print("bbbb", en[1][1])


# print(min(data_blue))


    # 黃線
    # if 70 < high < 180 and weight * high > 30000:
    #     print("黃線區")
    #     print("weight =%s"%weight , "      ", "high =%s"%high , "        ", "area =%s "%(weight * high), "       ", "length =%s"%(weight*2 + high*2))
    #     print("--------------------------------")
    #     cv2.drawContours(img, [box], -1, (0, 255, 255), 2)



# 垂直矩形
# for cnt in contourss:
#     # cv2.boundingRect() 透過輪廓，找到外接矩形的座標參數
#     # 返回4個值：x,y,w,h
#     bounding_boxes.append(cv2.boundingRect(cnt))
#
# for bbox in bounding_boxes:
#     # 矩陣中 最左上角座標的x軸數值
#     x = bbox[0]
#
#     # 矩陣中 最左上角座標的y軸數值
#     y = bbox[1]
#
#     # 矩陣的寬度w
#     w = bbox[2]
#
#     # 矩陣的高度h
#     h = bbox[3]
#
#     # 畫出所有結果
#     # cv2.rectangle(img, (bbox[0], bbox[1]), (bbox[0] + bbox[2], bbox[1] + bbox[3]), (0, 255, 0), 2)
#
#     # 畫出 "指定框框大小條件" 下的結果，視情況調整
#     # (0, 255, 0)：綠線
#     # 2：線條粗度(設定1會太細，看不太出結果)；如果2改成-1，會變成畫出實心矩形
#     if w > 300 and 300 > h > 69 and w*h < 200000:
#         print("框框的參數(左上角座標的x值,左上角座標的y值,矩陣的寬度,矩陣的高度) = ", bbox)
#         # 畫出矩形框框，畫在 "原圖" 上
#         cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
#         count += 1
#         print("")
# #
# print("{}個框".format(count))

cv2.namedWindow("sharpen_image", 0)
# 調整輸出視窗大小，看原圖是橫的還是直的
# cv2.resizeWindow("sharpen_image", 1200, 800)
cv2.imshow("sharpen_image", img)

# cv2.imwrite('C:/Users/226083/Desktop/opencv_test/r1_1_test.jpg', img)


cv2.waitKey(0)
cv2.destroyAllWindows()