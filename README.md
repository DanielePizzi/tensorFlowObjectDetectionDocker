
## Installation


```
git clone https://github.com/anushkadhiman/YOLOv3-TensorFlow-2.x.git
cd YOLOv3-TensorFlow-2.x
````

```
pip install -r ./requirements.txt
`````

```
# yolov3
wget -P model_data https://pjreddie.com/media/files/yolov3.weights

# yolov3-tiny
wget -P model_data https://pjreddie.com/media/files/yolov3-tiny.weights
``````


## Detection
Start with using pretrained weights to test predictions on both image and video:
```
python detection_demo.py
````

## Result

### Detection by Pre-trained model
![Alt text](detect.jpg?raw=true "image1")
![Alt text](detect2.jpg?raw=true "image2")
![Alt text](video.gif?raw=true "video")

### Detection by Custom Trained model
![Alt text](video2.gif?raw=true "video")



