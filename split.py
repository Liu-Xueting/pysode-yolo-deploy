import os
import shutil

# 你的混合文件夹路径
buffer_dir = "C:\\Users\\lxt\\Downloads\\phone\\replay_buffer"

# 目标图片和标签文件夹路径
target_images_dir = os.path.join(buffer_dir, "images")
target_labels_dir = os.path.join(buffer_dir, "labels")

# 创建目标文件夹
os.makedirs(target_images_dir, exist_ok=True)
os.makedirs(target_labels_dir, exist_ok=True)

# 遍历并移动文件
for file in os.listdir(buffer_dir):
    file_path = os.path.join(buffer_dir, file)

    # 跳过文件夹
    if os.path.isdir(file_path):
        continue

    if file.endswith((".jpg", ".jpeg", ".png")):
        shutil.move(file_path, os.path.join(target_images_dir, file))
    elif file.endswith(".txt"):
        shutil.move(file_path, os.path.join(target_labels_dir, file))

print("整理完成！")
