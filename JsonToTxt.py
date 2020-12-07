import json
import os

'''
将BK100数据集中的标签json文件转化为yolov5需要的txt标签
'''


def bdd2yolo5(categorys, jsonFile, writepath):
    strs = ""
    f = open(jsonFile)
    info = json.load(f)
    # print(len(info))
    # print(info["name"])
    # write = open(writepath + "%s.txt" % info["name"], 'w')
    write = open(writepath + os.sep + "%s.txt" % info["name"], 'w')
    for obj in info["frames"]:
        # print(obj["objects"])
        for objects in obj["objects"]:
            # print(objects)
            if objects["category"] in categorys:
                dw = 1.0 / 1280
                dh = 1.0 / 720
                strs += str(categorys.index(objects["category"]))
                strs += " "
                strs += str(((objects["box2d"]["x1"] + objects["box2d"]["x2"]) / 2.0) * dw)
                strs += " "
                strs += str(((objects["box2d"]["y1"] + objects["box2d"]["y2"]) / 2.0) * dh)
                strs += " "
                strs += str(((objects["box2d"]["x2"] - objects["box2d"]["x1"])) * dw)
                strs += " "
                strs += str(((objects["box2d"]["y2"] - objects["box2d"]["y1"])) * dh)
                strs += "\n"
        write.writelines(strs)
        write.close()
        print("%s has been dealt!" % info["name"])


if __name__ == "__main__":
    ####################args#####################
    # 自己需要从BDD数据集里提取的目标类别
    categorys = ['car', 'bus', 'person', 'bike', 'truck', 'motor', 'train', 'rider', 'traffic sign', 'traffic light']
    readpath = r"D:\百度云\BDD100K\bdd100k\labels\100k\train"  # BDD数据集标签读取路径，这里需要分两次手动去修改train、val的地址
    writepath = r"C:\Users\Wayne\Desktop\test1"  # BDD数据集转换后的标签保存路径

    fileList = os.listdir(readpath)
    # print(fileList)
    for file in fileList:
        print(file)
        # filepath = readpath + file
        filepath = os.path.join(readpath, file)
        bdd2yolo5(categorys, filepath, writepath)
