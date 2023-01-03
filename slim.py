from PIL import Image
import os

# 把需要压缩的图片复制到origin文件夹中
# 在cmd中执行 dir /b origin > files.txt 得到需要压缩的图片名们
# 运行该程序，压缩后的图片将在slim文件夹中。

ori_path = ".\origin"
tar_path = ".\slim"

def fileList(): #从files.txt里得到文件列表
    with open("files.txt", "r", encoding="utf-8") as f:
        files = f.read().split("\n")
        return files

def slim(filename:str):
    img = Image.open(f"{ori_path}\\{filename}")
    if 'exif' in img.info:  #图片有exif信息
        img.save(f"{tar_path}\\{filename}", exif = img.info['exif'], quality = 25)
    else:                   #图片没有exif信息的情况
        img.save(f"{tar_path}\\{filename}", quality = 25)

def size(path:str): #得到图片的空间大小 单位MB
    size = os.path.getsize(f"{path}")
    return (size / 1000 ** 2)

def start(files:list):
    for filename in files:
        fat_size = size(f"{ori_path}\\{filename}")
        slim(filename)
        slim_size = size(f"{tar_path}\\{filename}")
        print(f"🎉{filename} 瘦身完毕 瘦身前{fat_size}MB 瘦身后{slim_size}MB")
    print(f"图片瘦身顺利结束💕")

files = fileList()
start(files)