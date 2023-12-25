# BEE12C-Multiracial_Skin_Tone_Recognition-Danial

# Skin Tone Detection Project

## Abstract
This project focuses on the development of a skin tone detection system using machine learning techniques, particularly Convolutional Neural Networks (CNNs). It aims to accurately categorize diverse skin tones across different racial groups and assign specific hex codes. The system's core purpose extends to potential applications in the beauty industry, including a personalized makeup recommender system based on identified skin tones.

## Methodology
The project utilizes the Monk Skin Tone Dataset (MST Dataset) and employs advanced image preprocessing techniques to clean and prepare the data for model training. Convolutional Neural Networks (CNNs) are developed and fine-tuned using TensorFlow to detect and categorize skin tones. The block diagram within this repository illustrates the logical flow of processes involved, spanning from dataset collection to skin tone detection and user interface/output.

![Data Preperation (2)](https://github.com/Danial-Ahmad10/BEE12C-Multiracial_Skin_Tone_Recognition-Danial/assets/133823702/29a25def-9103-4de5-8e26-05b26969e262)

## Monk Skin Tone Dataset
In this project, we use the MST dataset provided by Google. It contains a total of 1515 images and 31 videos, among a total of 19 different subjects. Each subject has an average of 87 pictures from different angles. The dataset contains images of people, labelled with different skin tones, ranging from 1 to 10. The label represents the skin tone (darker skin tones have higher numbers). We use this dataset as a scale to identify each person's skin tone. This dataset also includes a label of well_lit or poorly_lit which explains to us the lighting conditions of the picture taken. It also includes the poses made by the person. The dataset was released by Google in March of 2023, and there are very few models at the time of this project's implementation. The Skin Tones have 10 levels as shown below:

![image](https://github.com/Danial-Ahmad10/BEE12C-Multiracial_Skin_Tone_Recognition-Danial/assets/133823702/b3491d85-f4ac-4ccc-9c6b-d1372abf0778)
You can download this dataset from this [website](https://skintone.google/the-scale).

## Model
We used MobileNetV2 as a pre-trained model and applied an output layer with a Softmax activation function that will classify between our desired 10 classes. In addition to that, we used MTCNN to detect faces first, which is a pre-trained model that we used and it detected faces quite accurately. However, it had an issue with detecting darker skinned faces.

## Repository Structure
- `/data`: Contains the Monk Skin Tone Dataset (MST Dataset).
- `/code`: Includes scripts and notebooks for data preprocessing, model development, and skin tone detection.
- `/results`: Holds visualizations, model evaluations, and outcomes.
- `/docs`: Additional project documentation and references.

