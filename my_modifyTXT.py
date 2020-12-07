import os
import numpy as np

"""
针对yolov5测试得到的txt文本，将其转换为计算mAP所需的文本
"""


def my_def_data(input_path, output_path, if_confi):
    # path = r"C:\Users\Wayne\Desktop\test"
    files = os.listdir(input_path)
    # path2 = r"C:\Users\Wayne\Desktop\new1"
    # files2 = os.listdir(output_path)
    name = ['person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck', 'boat', 'traffic_light',
            'fire_hydrant', 'stop_sign', 'parking_meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow',
            'elephant', 'bear', 'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee',
            'skis', 'snowboard', 'sports_ball', 'kite', 'baseball_bat', 'baseball_glove', 'skateboard', 'surfboard',
            'tennis_racket', 'bottle', 'wine_glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple',
            'sandwich', 'orange', 'broccoli', 'carrot', 'hot_dog', 'pizza', 'donut', 'cake', 'chair', 'couch',
            'potted_plant', 'bed', 'dining_table', 'toilet', 'tv', 'laptop', 'mouse', 'remote', 'keyboard',
            'cell_phone', 'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors',
            'teddy_bear', 'hair_drier', 'toothbrush']
    for file in files:
        filename = input_path + '\\' + file  # txt文件和当前脚本在同一目录下，所以不用写具体路径
        a, b, c, d, e, a2 = [], [], [], [], [], []
        with open(filename, 'r') as file_to_read:
            while True:
                lines = file_to_read.readline()  # 整行读取数据
                if not lines:
                    break
                    pass
                a1, b1, c1, d1, e1 = [float(i) for i in lines.split()]  # 将整行数据分割处理，如果分割符是空格，括号里就不用传入参数，如果是逗号， 则传入‘，'字符。
                a.append(a1)  # 添加新读取的数据
                b.append(b1)
                c.append(c1)
                d.append(d1)
                e.append(e1)
                pass
        for i in range(len(a)):
            a2.append(name[int(a[i])])
        confi = 0.88 * np.ones((1, len(a)))
        filename2 = output_path + '\\' + file
        open(filename2, 'w').close()
        if if_confi:
            for i in range(len(a)):
                new_list = []
                b2 = b[i] - 0.5 * d[i]
                c2 = c[i] - 0.5 * e[i]
                d2 = b[i] + 0.5 * d[i]
                e2 = c[i] + 0.5 * e[i]
                new_list.append(a2[i])
                new_list.append(confi[0][i])
                new_list.append(b2)
                new_list.append(c2)
                new_list.append(d2)
                new_list.append(e2)
                with open(filename2, 'a') as file_1:
                    s = str(new_list).replace('[', '').replace(']', '')  # 去除[],这两行按数据不同，可以选择
                    s = s.replace("'", '').replace(',', '') + '\n'  # 去除单引号，逗号，每行末尾追加换行符
                    file_1.write(s)
                file_1.close()
        else:
            for i in range(len(a)):
                new_list = []
                b2 = b[i] - 0.5 * d[i]
                c2 = c[i] - 0.5 * e[i]
                d2 = b[i] + 0.5 * d[i]
                e2 = c[i] + 0.5 * e[i]
                new_list.append(a2[i])
                # new_list.append(confi[0][i])
                new_list.append(b2)
                new_list.append(c2)
                new_list.append(d2)
                new_list.append(e2)
                with open(filename2, 'a') as file_1:
                    s = str(new_list).replace('[', '').replace(']', '')  # 去除[],这两行按数据不同，可以选择
                    s = s.replace("'", '').replace(',', '') + '\n'  # 去除单引号，逗号，每行末尾追加换行符
                    file_1.write(s)
                file_1.close()


my_def_data(r'C:\Users\Wayne\Desktop\test', r'C:\Users\Wayne\Desktop\new1', 1)
