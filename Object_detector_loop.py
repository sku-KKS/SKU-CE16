#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np


# In[2]:


classes = []
colors=[]

w_adr="C:\\Users\\pl_workstation\\Desktop\\test\\yolo-obj_last.weights"
c_adr="C:\\Users\\pl_workstation\\Desktop\\test\\yolo-obj.cfg"
net = cv2.dnn.readNet(w_adr, c_adr)


# In[3]:


n_adr="C:\\Users\\pl_workstation\\Desktop\\test\\obj.names"
with open(n_adr, "r") as f:
    classes = [line.strip() for line in f.readlines()]


# In[4]:


layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]


# In[5]:


colors = np.random.uniform(0, 255, size=(len(classes), 3))
font = cv2.FONT_HERSHEY_PLAIN


# In[6]:


img_save=[]


# In[9]:


for z in range(10048):
    
    class_ids = []
    confidences = []
    bound=[]
    boxes = []   
    
    img = cv2.imread("C:\\Users\\pl_workstation\\Desktop\\test\\result_source\\test ("+str(z+1)+").png")
    height, width, channels = img.shape

    blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)

    for out in outs:
        for detection in out:
            
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            
            if confidence > 0.5:
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                
                sx = int(center_x - w / 2)
                sy = int(center_y - h / 2)
                ex = int(center_x + w / 2)
                ey = int(center_y + h / 2)
                
                bound.append([sx, sy, ex, ey])
                boxes.append([sx, sy, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)
            

    with open('result_'+str(z+1).zfill(5)+'.txt', 'w') as f:
        for l in range(len(bound)):
            f.write(str(classes[class_ids[l]])+' '+str(round(confidences[l],5))+' '+str(bound[l][0])+' '+str(bound[l][1])+' '+
                    str(bound[l][2])+' '+str(bound[l][3])+'\n')
            
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)        

    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            color = colors[(i%3)]
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
            cv2.putText(img, label, (x, y + 30), font, 2, color, 2)
    
    img_save.append(img)

