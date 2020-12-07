import cv2

'''
测试输出后的标签是否正确
'''
img = cv2.imread(r'C:\Users\Wayne\Desktop\0000f77c-62c2a288.jpg')
img_h = img.shape[0]
img_w = img.shape[1]
aa = [0.218216,0.452550,0.044950,0.086712]  # 获取归一化后的坐标
xmin = int((aa[0] - aa[2] / 2) * img_w)
ymin = int((aa[1] - aa[3] / 2) * img_h)
xmax = int((aa[0] + aa[2] / 2) * img_w)
ymax = int((aa[1] + aa[3] / 2) * img_h)
cv2.rectangle(img, (xmin, ymin), (xmax, ymax), (0, 255, 0), 3)  # 边框的左上角的像素坐标是，右下角的像素坐标是
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
