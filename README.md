# German Traffic Sign Recognition with CNN and Streamlit

This project focuses on building and deploying a machine learning model to classify German traffic signs using Convolutional Neural Networks (CNNs) and TensorFlow. The model is trained on the [German Traffic Sign Recognition Benchmark (GTSRB)](http://benchmark.ini.rub.de/?section=gtsrb&subsection=dataset) dataset and is deployed using a Streamlit app to allow for easy image classification.

## Table of Contents

- [Project Overview](#project-overview)
- [Installation](#installation)


## Project Overview

The goal of this project is to accurately classify images of traffic signs using a CNN. The project consists of two main components:
1. **Training a CNN Model**: The model is trained on a set of pre-processed images from the GTSRB dataset.
2. **Deployment with Streamlit**: A simple web interface is created using Streamlit to upload and classify images of traffic signs.

## Installation

To run this project, you need to have Python installed along with the required libraries. You can install the dependencies using pip:

```bash
pip install tensorflow scikit-learn numpy matplotlib opencv-python streamlit pillow
