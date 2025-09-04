
# import torch
# import cv2
# import os

# # Load trained YOLOv5 model
# # Update the path to your trained weights if different
# model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5/runs/train/exp9/weights/best.pt')

# # Function to detect defects
# def detect_defects(image_path):
#     # Run inference
#     results = model(image_path)

#     # Extract detections
#     detections = results.pandas().xyxy[0]  # bounding box dataframe

#     if detections.empty:
#         print("✅ No defect detected.")
#     else:
#         print("🔍 Defects detected:")
#         for i, row in detections.iterrows():
#             cls = row['name']  # defect class name
#             conf = row['confidence']
#             x1, y1, x2, y2 = int(row['xmin']), int(row['ymin']), int(row['xmax']), int(row['ymax'])
            
#             print(f" - {cls} (confidence: {conf:.2f}) at location: ({x1}, {y1}, {x2}, {y2})")

#     # Save result with bounding boxes (inside runs/detect/)
#     results.save()

#     return detections

# if __name__ == "__main__":
#     # Ask user for image path
#     img_path = input("Enter path to image: ").strip()

#     if not os.path.exists(img_path):
#         print("❌ Image not found. Please check the path.")
#     else:
#         detect_defects(img_path)


import torch
import os
import glob
import cv2

# Load trained YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5/runs/train/exp9/weights/best.pt')

# Define fixed colors for each defect type
CLASS_COLORS = {
    'keyhole': (0, 0, 255),         # Red
    'groove': (255, 165, 0),          # Light Blue/Orange
    'flash': (255, 0, 255),        # Magenta
    'voids': (255, 0, 0),          # Blue
    'microcracks': (128, 0, 128),  # Purple
    'defectless': (0, 128, 128),# Teal
}

def detect_defects(image_path, save_folder):
    # Run inference
    results = model(image_path)

    # Extract detections
    detections = results.pandas().xyxy[0]

    # Load the image
    img = cv2.imread(image_path)

    # Print detected defects and annotate
    if detections.empty:
        print(f"✅ {os.path.basename(image_path)} : No defect detected.")
    else:
        print(f"🔍 {os.path.basename(image_path)} : Defects detected:")
        for _, row in detections.iterrows():
            cls = row['name']
            conf = row['confidence']
            x1, y1, x2, y2 = int(row['xmin']), int(row['ymin']), int(row['xmax']), int(row['ymax'])
            print(f" - {cls} (confidence: {conf:.2f}) at coordinates: ({x1}, {y1}, {x2}, {y2})")

            # Draw rectangle and label
            color = CLASS_COLORS.get(cls, (0, 255, 0))  # default green if not defined
            thickness = 2
            font_scale = 1.0
            font = cv2.FONT_HERSHEY_SIMPLEX

            # Draw bounding box
            cv2.rectangle(img, (x1, y1), (x2, y2), color, thickness)

            # Label text with confidence
            label = f"{cls} {conf:.2f}"
            (text_width, text_height), baseline = cv2.getTextSize(label, font, font_scale, thickness)
            cv2.rectangle(img, (x1, y1 - text_height - 10), (x1 + text_width, y1), color, -1)
            cv2.putText(img, label, (x1, y1 - 5), font, font_scale, (255, 255, 255), thickness)

    # Save annotated image
    os.makedirs(save_folder, exist_ok=True)
    save_path = os.path.join(save_folder, os.path.basename(image_path))
    cv2.imwrite(save_path, img)

    return detections

def get_next_exp_folder(base="exp"):
    """Find the next available exp folder name (exp1, exp2, exp3...)"""
    i = 1
    while os.path.exists(f"{base}{i}"):
        i += 1
    return f"{base}{i}"

if __name__ == "__main__":
    path = input("Enter path to image or folder: ").strip()

    if not os.path.exists(path):
        print("❌ Path not found. Please check again.")
    else:
        output_folder = get_next_exp_folder()

        if os.path.isfile(path):  # Single image
            detect_defects(path, output_folder)
        elif os.path.isdir(path):  # Folder of images
            image_files = glob.glob(os.path.join(path, "*.jpg")) + \
                          glob.glob(os.path.join(path, "*.png")) + \
                          glob.glob(os.path.join(path, "*.jpeg"))
            print(f"📂 Found {len(image_files)} images in folder '{path}'")
            for img in image_files:
                detect_defects(img, output_folder)
        else:
            print("⚠️ Path is neither a file nor a folder.")

        print(f"\n✅ All processed images saved in folder: {output_folder}")
