import numpy as np
import tensorflow_hub as hub
import tensorflow as tf
import cv2 as cv
import pandas as pd


detector = hub.load("https://tfhub.dev/tensorflow/efficientdet/lite2/detection/1")
labels = pd.read_csv('labels.csv',sep=';',index_col='ID')
labels = labels['OBJECT (2017 REL.)']

cap = cv.VideoCapture('media/videoplayback.mp4')
while cap.isOpened():
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    #Resize to respect the input_shape
    #inp = cv.resize(frame, (width , height ))

    #Convert img to RGB
    rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

    #Is optional but i recommend (float convertion and convert img to tensor image)
    rgb_tensor = tf.convert_to_tensor(rgb, dtype=tf.uint8)

    #Add dims to rgb_tensor
    rgb_tensor = tf.expand_dims(rgb_tensor , 0)
    
    boxes, scores, classes, num_detections = detector(rgb_tensor)
    
    pred_labels = classes.numpy().astype('int')[0]
    
    pred_labels = [labels[i] for i in pred_labels]
    pred_boxes = boxes.numpy()[0].astype('int')
    pred_scores = scores.numpy()[0]

    img_boxes = frame;

    for score, (ymin,xmin,ymax,xmax), label in zip(pred_scores, pred_boxes, pred_labels):
        if score < 0.5:
            continue
            
        score_txt = f'{100 * round(score,0)}'
        img_boxes = cv.rectangle(img_boxes,(xmin, ymax),(xmax, ymin),(0,255,0),1)      
        font = cv.FONT_HERSHEY_SIMPLEX
        cv.putText(img_boxes,label,(xmin, ymax-10), font, 0.5, (255,0,0), 1, cv.LINE_AA)
        cv.putText(img_boxes,score_txt,(xmax, ymax-10), font, 0.5, (255,0,0), 1, cv.LINE_AA)

    cv.imshow('frame', img_boxes)
    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()