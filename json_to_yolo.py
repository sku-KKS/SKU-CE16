#!/usr/bin/env python
# coding: utf-8

# In[2]:


import json


# In[3]:


json_data=[]
for i in range(10329):
    with open('C:\\Users\\pl_workstation\\Desktop\\contest\\object detect\\json\\train ('+str(i+1)+').json', 'r') as f:
        json_data.append(json.load(f))


# In[3]:


def cal_xywh(sx,sy,ex,ey):
    global x,y,w,h
    x=(sx+ex)/2/1920
    y=(sy+ey)/2/1080
    w=(ex-sx)/1920
    h=(ey-sy)/1080


# In[4]:


def class_form(name):
    if name=='일반차량':
        return 0
    elif name=='보행자':
        return 2
    elif name=='이륜차':
        return 1
    else:
        return 0
        


# In[5]:


for i in range(10329):
    xlist=[]
    ylist=[]
    wlist=[]
    hlist=[]
    for j in range(len(json_data[i]['annotations'])):
        cal_xywh(
            json_data[i]['annotations'][j]['points'][0][0],
            json_data[i]['annotations'][j]['points'][0][1],
            json_data[i]['annotations'][j]['points'][2][0],
            json_data[i]['annotations'][j]['points'][2][1])

        xlist.append(round(x,6))
        ylist.append(round(y,6))
        wlist.append(round(w,6))
        hlist.append(round(h,6))
        
    llist=[]
    
    for k in range(len(json_data[i]['annotations'])):
        llist.append(class_form(json_data[i]['annotations'][k]['label']))
        
    with open('train ('+str(i+1)+').txt', 'w') as f:
        for l in range(len(json_data[i]['annotations'])):
            f.write(str(llist[l])+' '+str(xlist[l])+' '+str(ylist[l])+' '+
                    str(wlist[l])+' '+str(hlist[l])+'\n')

