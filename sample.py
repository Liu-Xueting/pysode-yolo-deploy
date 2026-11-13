import os
import random
import shutil

old_images_dir = "C:\\Users\\lxt\\Downloads\\phone\\train\\images"
old_labels_dir = "C:\\Users\\lxt\\Downloads\\phone\\train\\labels"
buffer_dir = "C:\\Users\\lxt\\Downloads\\phone\\replay_buffer"

os.makedirs(buffer_dir, exist_ok=True)

# 简化：按文件名前缀或实际类别分组抽样，这里演示随机抽取
all_imgs = [f for f in os.listdir(old_images_dir) if f.endswith((".jpg", ".png"))]
sampled = random.sample(all_imgs, min(50, len(all_imgs)))  # 抽取 50 张

for img in sampled:
    shutil.copy(os.path.join(old_images_dir, img), os.path.join(buffer_dir, img))
    lbl = img.rsplit(".", 1)[0] + ".txt"
    lbl_path = os.path.join(old_labels_dir, lbl)
    if os.path.exists(lbl_path):
        shutil.copy(lbl_path, os.path.join(buffer_dir, lbl))
