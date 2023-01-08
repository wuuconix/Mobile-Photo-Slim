from PIL import Image
import os

# 首先需要运行一下命令将手机相册中的图片拉取出来
# adb pull /storage/emulated/0/DCIM/Camera/
ori_path = ".\Camera"
tar_path = ".\Camera_Slim"

def slim(filename: str):
    img = Image.open(f"{ori_path}\\{filename}")
    if 'exif' in img.info:  #图片有exif信息
        img.save(f"{tar_path}\\{filename}", exif = img.info['exif'], quality = 25)
    else:                   #图片没有exif信息的情况
        img.save(f"{tar_path}\\{filename}", quality = 25)

def size(path: str): #得到图片的空间大小 单位MB
    size = os.path.getsize(f"{path}")
    return (size / 1000 ** 2)

def start(images: list):
    for filename in images:
        fat_size = size(f"{ori_path}\\{filename}")
        slim(filename)
        slim_size = size(f"{tar_path}\\{filename}")
        print(f"🎉{filename} 瘦身完毕 瘦身前{fat_size}MB 瘦身后{slim_size}MB")
    print(f"图片瘦身顺利结束💕")

def is_image(filename: str):
    return filename.endswith(".jpg")

images = [image for image in filter(is_image, os.listdir("./Camera"))]
start(images)