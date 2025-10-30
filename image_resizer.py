import os
from PIL import Image

input_folder = "images"
output_folder = "resized"
os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.endswith((".jpg", ".png", ".jpeg")):
        try:
            img_path = os.path.join(input_folder, filename)
            img = Image.open(img_path)
            resized_img = img.resize((300, 300))  # Resize to 300x300
            new_filename = os.path.splitext(filename)[0] + ".png"
            resized_img.save(os.path.join(output_folder, new_filename))
        except Exception as e:
            print(f"Error processing {filename}: {e}")
