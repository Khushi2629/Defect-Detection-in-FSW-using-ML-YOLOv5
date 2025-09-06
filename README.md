# The trained YOLOv5 model outputs:

1. Defect Type (class name)

2. Confidence Score (probability of detection)

3. Bounding Box Coordinates (precise defect location on the weld surface)


# 📂 Dataset

* Total images used: ~210 weld surface images

* Annotated using LabelImg in YOLO format (.txt files)

* Defect classes:

1. Keyhole

2. Flash

3. Grooves

4. Microcracks

5. Voids

6. Defectless

   <img width="699" height="231" alt="Screenshot 2025-09-06 at 7 26 48 PM" src="https://github.com/user-attachments/assets/aa60aa7b-cfb4-4f78-87f7-8fcd04cfdbea" />


# 🚀 Training

To train the model:
python3 train.py --img 640 --batch 16 --epochs 50 --data ../BTP_YOLO/data.yaml --weights yolov5s.pt


--img: image size (default 640x640)

--batch: batch size

--epochs: number of training epochs

--data: dataset configuration file

--weights: pretrained YOLOv5 weights



# 🔍 Inference

Run inference on test images:
cd /home/your-username/Desktop/BTP_YOLO/yolov5
python3 detect.py --weights ../BTP_YOLO/runs/train/exp/weights/best.pt --source ../BTP_YOLO/test_images/sample.jpg --save-txt --save-conf

Use the latest exp run

Results will be saved in:
runs/detect/exp/
Each output image contains bounding boxes with defect labels and confidence scores.


# 🛠️ Tech Stack

Python

PyTorch

YOLOv5

OpenCV

LabelImg (for annotation)


# Example output is below:

<img width="1470" height="956" alt="Screenshot 2025-09-06 at 7 26 03 PM" src="https://github.com/user-attachments/assets/af7ccd23-6af8-4dc7-ae74-46704a8d66f5" />

<img width="751" height="663" alt="Screenshot 2025-09-06 at 8 15 30 PM" src="https://github.com/user-attachments/assets/95832cee-ba73-4dd8-833d-36ea17c2ee67" />

<img width="916" height="774" alt="Screenshot 2025-09-06 at 8 15 15 PM" src="https://github.com/user-attachments/assets/ca147388-18a7-48c4-a28d-4f1464aaaa62" />

<img width="745" height="628" alt="Screenshot 2025-09-06 at 8 14 25 PM" src="https://github.com/user-attachments/assets/3b42f494-073a-46ad-8adf-45a7d7d344f1" />

<img width="744" height="652" alt="Screenshot 2025-09-06 at 8 14 42 PM" src="https://github.com/user-attachments/assets/175c7bf6-185b-4732-94db-5e1c7d7754e7" />










<img width="1470" height="956" alt="Screenshot 2025-08-31 at 11 44 47 PM" src="https://github.com/user-attachments/assets/cf0a7778-d862-435c-b157-34596638a09c" />


![kh,f_9](https://github.com/user-attachments/assets/820ce084-a2ab-4a08-bcb9-f6999e6caff3)







