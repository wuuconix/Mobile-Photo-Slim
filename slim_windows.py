from PIL import Image
import os

ori_path = "C:\\Users\\15219\OneDrive - uconix\\图片\\手机相册"
tar_path = "C:\\Users\\15219\\Downloads\\手机相册瘦身版"

def fileList(): #从files.txt里得到文件列表
    with open("files.txt", "r", encoding="utf-8") as f:
        files = f.read().split("\n")
        return files

def slim(filename:str): #将IMG_20220307_170459.jpg 瘦身为 IMG_20220307_170459_slim.jpg 默认quality 75% 大概压缩为原体积的1/5
    img = Image.open(f"{ori_path}\\{filename}")
    img.save(f"{tar_path}\\{filename}" , exif = img.info['exif'], quality = 25)

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