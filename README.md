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
python3 detect.py --weights runs/train/exp/weights/best.pt --img 640 --conf 0.25 --source ../test_images


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



<img width="2048" height="2048" alt="Gemini_Generated_Image_70zp7s70zp7s70zp" src="https://github.com/user-attachments/assets/260b9829-e592-4ab4-bd60-36e26153548f" />


<img width="2048" height="2048" alt="Gemini_Generated_Image_dqs3bodqs3bodqs3" src="https://github.com/user-attachments/assets/82346975-1174-44d5-b197-682c8d889fa6" />


![mc,voids,g](https://github.com/user-attachments/assets/360d2ed8-4624-41fc-a0f3-950e0fecc655)


<img width="1470" height="956" alt="Screenshot 2025-08-31 at 11 44 47 PM" src="https://github.com/user-attachments/assets/cf0a7778-d862-435c-b157-34596638a09c" />


![kh,f_9](https://github.com/user-attachments/assets/820ce084-a2ab-4a08-bcb9-f6999e6caff3)







