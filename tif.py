import os
import shutil
from PIL import Image

# 设置输入和输出文件夹
input_folder = r"E:\2025Spring\map\map\Graphs"  # 你的图片所在路径
output_folder = r"E:\2025Spring\map\map\Graphs_TIF"  # 目标存放路径

# 确保输出文件夹存在
os.makedirs(output_folder, exist_ok=True)

# 遍历所有文件
for file in os.listdir(input_folder):
    input_path = os.path.join(input_folder, file)

    # 确保是图片文件
    if file.lower().endswith(".png"):
        # 转换 PNG 到 TIF
        img = Image.open(input_path)
        output_path = os.path.join(output_folder, file.replace(".png", ".tif"))
        img.save(output_path, format="TIFF")
        print(f"Converted {file} → {output_path}")

    elif file.lower().endswith(".tif"):
        # 直接复制已有的 TIF 文件
        output_path = os.path.join(output_folder, file)
        shutil.copy2(input_path, output_path)
        print(f"Copied {file} → {output_path}")

print("✅ All images are now in TIF format and stored in:", output_folder)
