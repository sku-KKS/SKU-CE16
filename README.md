# SKU-CE16



### 환경

* Windows 10 Pro
* i7-8700
* GTX 1080
* RAM 16G
* Visual studio 2019
* CUDA 10.1
* cuDNN 7.6.5
* OpenCV 4.2.1
* darknet
* yolo v3
* yolo mark
* anaconda



### 제공받은 데이터 처리

이미지파일, json 파일을 제공받았다.

json 파일에 각 객체에 대한 **좌표값**과 **라벨링**이 되어있음을 확인했다.

yolo_mark는 이미지에 bounding box 즉, 좌표값과 라벨링을 하여 학습데이터를 과정 입니다.

하지만 이미지 하나하나 라벨링 하기에는 비효율적이라 생각하여, 제공받은 json파일에 있는 

좌표값과 라벨링이 있기 떄문에 이것을 이용하였습니다.



