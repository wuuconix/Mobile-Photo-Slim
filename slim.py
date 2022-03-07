from PIL import Image
import os

""" Warning: 运行此程序前请先执行 adb shell ls /storage/emulated/0/DCIM/Camera > files.txt
    并手动选择你需要进行瘦身的图片们
    得到files.txt后注意，由于它是由cmd命令行重定向的，文件编码格式比较神秘，你需要在vscode中通过编码保存为utf-8格式
"""

def fileList(): #从files.txt里得到文件列表
    with open("files.txt", "r") as f:
        files = f.read().split("\n")
        return files

def rm(filename:str):
    os.system(f"adb shell rm /storage/emulated/0/DCIM/Camera/{filename} > log.txt")

def pull(filename:str):
    os.system(f"adb pull /storage/emulated/0/DCIM/Camera/{filename} ./{filename} > log.txt")

def push(filename:str): #push之后需要发送广播刷新mediastroe使相册刷新
    os.system(f"adb push ./{filename} /storage/emulated/0/DCIM/Camera/{filename} > log.txt")
    os.system(f"adb shell am broadcast -a android.intent.action.MEDIA_SCANNER_SCAN_FILE -d file:///storage/emulated/0/DCIM/Camera/{filename} > log.txt")

def rm_local(filename:str): #删除该项目下图片
    os.system(f"del {filename} >> log.txt")

def slim(filename:str): #将IMG_20220307_170459.jpg 瘦身为 IMG_20220307_170459_slim.jpg 默认quality 75% 大概压缩为原体积的1/5
    img = Image.open(filename)
    img.save(filename, exif = img.info['exif'])

def size(filename:str): #得到图片的空间大小 单位MB
    size = os.path.getsize(filename)
    return (size / 1000 ** 2)

def start(files:list):
    for filename in files:
        if filename == "":
            break
        pull(filename)
        fat_size = size(filename)
        if fat_size > 2: #大于2MB 需要压缩
            slim(filename)
            slim_size = size(filename)
            rm(filename)
            push(filename)
            print(f"🎉{filename} 瘦身完毕 瘦身前{fat_size}MB 瘦身后{slim_size}MB")
        else:
            print(f"🎉{filename} 不需要瘦身 大小{fat_size}MB")
        rm_local(filename)
    print(f"图片瘦身顺利结束💕")

files = fileList()
start(files)