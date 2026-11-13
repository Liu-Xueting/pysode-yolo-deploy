import os

# --- 配置区域 ---
# 你的原标签路径
source_labels_dir = "C:\\Users\\lxt\\Downloads\\tissue_phone\\valid\\labels"
# 修改后存放的新路径（建议放个新文件夹，防止改错）
target_labels_dir = "C:\\Users\\lxt\\Downloads\\tissue_phone\\valid\\labels_fixed"

# 定义 ID 映射：把原文件的 0(纸巾) 变成 1，1(手机) 变成 2
id_mapping = {0: 1, 1: 2}

# 创建目标文件夹
os.makedirs(target_labels_dir, exist_ok=True)
# -------------

print("开始转换标签...")
count = 0

for filename in os.listdir(source_labels_dir):
    if filename.endswith(".txt"):
        filepath = os.path.join(source_labels_dir, filename)
        target_filepath = os.path.join(target_labels_dir, filename)

        with open(filepath, "r") as f:
            lines = f.readlines()

        new_lines = []
        for i, line in enumerate(lines):
            # 保留行尾的换行符，防止最后一行没换行导致格式错误
            line = line.strip()
            if not line:
                continue

            parts = line.split()

            # 提取原来的 ID 和坐标
            old_id = int(parts[0])
            coords = parts[1:]  # 这里就是所有坐标，原封不动

            # 替换 ID
            new_id = id_mapping.get(old_id, old_id)

            # 重新组合
            new_line = str(new_id) + " " + " ".join(coords) + "\n"
            new_lines.append(new_line)

            # 打印第一个文件的第一行作为抽样检查
            if count == 0 and i == 0:
                print(f"【抽样检查】 文件: {filename}")
                print(f"修改前: {line}")
                print(f"修改后: {new_line.strip()}")

        # 写入新文件
        with open(target_filepath, "w") as f:
            f.writelines(new_lines)
        count += 1

print(f"处理完成！共转换了 {count} 个文件。")
print(f"请检查 {target_labels_dir} 里的文件是否符合预期。")
