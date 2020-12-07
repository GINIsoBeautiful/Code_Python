import os
import cv2
import numpy as np

"""
对Extracting_xywh.py进行优化，可以提取原始图片的高和宽
"""

path = r"C:\Users\Wayne\Desktop\label_2"  # 标签文件
files = os.listdir(path)
output_path = r"C:\Users\Wayne\Desktop\output_label"
name = ['Car', 'Van', 'Truck', 'Pedestrian', 'Person_sitting', 'Cyclist', 'Tram', 'Misc', 'DontCare']
img_path = r"D:\Code_Python\datasets\images\train"
for file in files:
    filename = path + '\\' + file  # txt文件和当前脚本在同一目录下，所以不用写具体路径
    a, b, c, d, e = [], [], [], [], []
    ff = list(file)
    ff[7] = 'p'
    ff[8] = 'n'
    ff[9] = 'g'
    ff1 = ''.join(ff)
    img_name = img_path + '\\' + ff1
    img = cv2.imread(img_name)
    img_h = img.shape[0]
    img_w = img.shape[1]
    with open(filename, 'r') as file_to_read:
        while True:
            lines = file_to_read.readline()  # 整行读取数据
            if not lines:
                break
                pass
            data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11, data12, data13, data14, data15 = [
                str(i) for i in lines.split()]  # 将整行数据分割处理，如果分割符是空格，括号里就不用传入参数，如果是逗号， 则传入‘，'字符。
            a.append(data1)  # 添加新读取的数据
            b.append(float(data5))
            c.append(float(data6))
            d.append(float(data7))
            e.append(float(data8))
            pass
    # img_w = 1242
    # img_h = 375
    filename2 = output_path + '\\' + file
    open(filename2, 'w').close()
    for i in range(len(a)):
        new_list = []
        a1 = name.index(a[i])
        x_cen = ((b[i] + d[i]) / 2) / img_w
        y_cen = ((c[i] + e[i]) / 2) / img_h
        width = (d[i] - b[i]) / img_w
        heigth = (e[i] - c[i]) / img_h
        new_list.append(a1)
        new_list.append(x_cen)
        new_list.append(y_cen)
        new_list.append(width)
        new_list.append(heigth)
        with open(filename2, 'a') as file_1:
            s = str(new_list).replace('[', '').replace(']', '')  # 去除[],这两行按数据不同，可以选择
            s = s.replace("'", '').replace(',', '') + '\n'  # 去除单引号，逗号，每行末尾追加换行符
            file_1.write(s)
        file_1.close()
print("成功")
