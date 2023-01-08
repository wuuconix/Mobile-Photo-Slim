import os

tar_path = ".\Camera_Slim"

def push(filename:str): #push之后需要发送广播刷新mediastroe使相册刷新
    os.system(f"adb push {tar_path}/{filename} /storage/emulated/0/DCIM/Camera_Slim/{filename} > log.txt")
    os.system(f"adb shell am broadcast -a android.intent.action.MEDIA_SCANNER_SCAN_FILE -d file:///storage/emulated/0/DCIM/Camera_Slim/{filename} > log.txt")

def start(images: list):
    for filename in images:
        push(filename)
        print(f"🎉{filename} 上传并广播成功")

def is_image(filename: str):
    return filename.endswith(".jpg")

images = [image for image in filter(is_image, os.listdir("./Camera"))]
start(images)