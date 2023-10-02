
# Face Tracker

The Face Tracker project leverages the power of deep learning, utilizing the VGG16 architecture which was fine-tuned for my custom dataset, 


## Preview
![Preveiew](https://github.com/Krithik-sri/Face_Tracker/assets/123297016/4f1376cc-90b1-46da-ab81-c58fa778b8a1)


## Run

To take the images for the dataset run `image_collection.py`

To annotate the images use the [labelme](https://github.com/wkentaro/labelme) package

To split the images into train test and validation split run `split_data.py`

To train the model run each cell in order in `face_detection.ipynb`

## Features
### Deep Learning Model
- The project employs the VGG16 deep convolutional neural network (CNN) architecture. Fine-tuned layers of VGG16 are used for face detection in tensorflow.
- OpenCV is used to make real-time face detection

### Custom Dataset
- This project so that anyone can make their own custom dataset using their webcam and their own face as data.
- Took 90 photos of myself in various scenarios and some without my face to add some noise to the dataset.
-  The [labelme](https://readme.so/editor) library was used to annotate the labels for the images.
- The [albumentations](https://albumentations.ai) library was used to augment the images to around 4000 images.

### Real Time tracking
The deep learning model aimed for real-time face tracking using OpenCV
## Dependencies

```bash
tensorflow==2.8.0
albumentation==1.1.0
labelme==5.3.1
opencv-python==4.5.4.60
python==3.9
```

