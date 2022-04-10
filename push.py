import os

tar_path = ".\slim"

def fileList(): #从files.txt里得到文件列表
    with open("files.txt", "r") as f:
        files = f.read().split("\n")
        return files

def push(filename:str): #push之后需要发送广播刷新mediastroe使相册刷新
    os.system(f"adb push {tar_path}/{filename} /storage/emulated/0/DCIM/Camera_Slim/{filename} > log.txt")
    os.system(f"adb shell am broadcast -a android.intent.action.MEDIA_SCANNER_SCAN_FILE -d file:///storage/emulated/0/DCIM/Camera_Slim/{filename} > log.txt")

def start(files:list):
    for filename in files:
        if filename == "":
            break
        push(filename)
        print(f"🎉{filename} 上传并广播成功")

files = fileList()
start(files)