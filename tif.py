import os
import shutil
from PIL import Image


input_folder = r"E:\2025Spring\map\map\Graphs"   
output_folder = r"E:\2025Spring\map\map\Graphs_TIF"  


os.makedirs(output_folder, exist_ok=True)


for file in os.listdir(input_folder):
    input_path = os.path.join(input_folder, file)

    
    if file.lower().endswith(".png"):
        
        img = Image.open(input_path)
        output_path = os.path.join(output_folder, file.replace(".png", ".tif"))
        img.save(output_path, format="TIFF")
        print(f"Converted {file} → {output_path}")

    elif file.lower().endswith(".tif"):
        
        output_path = os.path.join(output_folder, file)
        shutil.copy2(input_path, output_path)
        print(f"Copied {file} → {output_path}")

print("✅ All images are now in TIF format and stored in:", output_folder)
