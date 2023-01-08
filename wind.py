import shutil
import os

# 收尾工作 最后执行
# 根据你的实际需要增删代码

files = os.listdir("./Camera")
 
for filename in files:
    if filename.endswith(".jpg"):
        shutil.copy2(f"./Camera/{filename}", "D:\\Camera")  # 原图 机械硬盘
        shutil.copy2(f"./Camera_Slim/{filename}", "D:\\Camera_Slim")  # 瘦图 机械硬盘
        shutil.copy2(f"./Camera/{filename}", "C:\\Users\\15219\\OneDrive - uconix\\图片\\手机相册") # 原图 OneDrive
        os.remove(f"./Camera/{filename}")
        os.remove(f"./Camera_Slim/{filename}")
        print(f"图片 {filename} 备份成功")
    elif filename.endswith(".mp4"):
        shutil.copy2(f"./Camera/{filename}", "D:\\手机视频") # 视频 机械硬盘
        shutil.copy2(f"./Camera/{filename}", "C:\\Users\\15219\\OneDrive - uconix\\视频\\手机视频") # 视频 OneDrive
        os.remove(f"./Camera/{filename}")
        print(f"视频 {filename} 备份成功")
    else:
        print("这啥后缀 没见过")
