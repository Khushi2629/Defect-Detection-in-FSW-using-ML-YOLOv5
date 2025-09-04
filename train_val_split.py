import os
import random
import shutil

# Paths
base_dir = os.getcwd()   # current BTP_YOLO directory
images_dir = os.path.join(base_dir, "all_fsw_jpg_images")
labels_dir = os.path.join(base_dir, "labels")

train_img_dir = os.path.join(base_dir, "train/images")
train_lbl_dir = os.path.join(base_dir, "train/labels")
val_img_dir = os.path.join(base_dir, "val/images")
val_lbl_dir = os.path.join(base_dir, "val/labels")

# Train/val ratio
train_ratio = 0.8

# Ensure output dirs exist
for d in [train_img_dir, train_lbl_dir, val_img_dir, val_lbl_dir]:
    os.makedirs(d, exist_ok=True)

# Collect all image files
images = [f for f in os.listdir(images_dir) if f.lower().endswith(('.jpg', '.png'))]
random.shuffle(images)

split_idx = int(len(images) * train_ratio)
train_files = images[:split_idx]
val_files = images[split_idx:]

def copy_files(file_list, img_dest, lbl_dest):
    for file in file_list:
        img_src = os.path.join(images_dir, file)
        lbl_src = os.path.join(labels_dir, os.path.splitext(file)[0] + ".txt")

        # Copy image
        shutil.copy(img_src, img_dest)

        # Copy label if exists
        if os.path.exists(lbl_src):
            shutil.copy(lbl_src, lbl_dest)
        else:
            print(f"⚠️ Label missing for {file}")

# Copy training files
copy_files(train_files, train_img_dir, train_lbl_dir)

# Copy validation files
copy_files(val_files, val_img_dir, val_lbl_dir)

print("✅ Dataset split complete.")
print(f"Training images: {len(train_files)}")
print(f"Validation images: {len(val_files)}")
