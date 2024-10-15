
# German Traffic Sign Recognition

## Overview

This project aims to develop a model for classifying traffic signs using the German Traffic Sign Recognition Benchmark (GTSRB) dataset. The model is built using Convolutional Neural Networks (CNN) and is deployed via a Streamlit application for easy interaction.

## Project Structure

- `main.py`: This file contains the code to train the CNN model on the GTSRB dataset.
- `mlops.py`: This file contains the Streamlit application for image upload and prediction.
- `GTSRB.h5`: The trained model saved in HDF5 format.

## Dataset

The dataset used in this project is the German Traffic Sign Recognition Benchmark (GTSRB). It contains images of various traffic signs collected from different locations. The dataset is divided into 43 classes, each representing a different traffic sign.

### Classes

The classes in the dataset are as follows:

0. Speed limit (20km/h)
1. Speed limit (30km/h)
2. Speed limit (50km/h)
3. Speed limit (60km/h)
4. Speed limit (70km/h)
5. Speed limit (80km/h)
6. End of speed limit (80km/h)
7. Speed limit (100km/h)
8. Speed limit (120km/h)
9. No passing
10. No passing for vehicles over 3.5 metric tons
11. Right-of-way at the next intersection
12. Priority road
13. Yield
14. Stop
15. No Vehicles
16. Vehicles over 3.5 metric tons prohibited
17. No entry
18. General caution
19. Dangerous curve to the left
20. Dangerous curve to the right
21. Double curve
22. Bumpy road
23. Slippery road
24. Road narrows on the right
25. Road work
26. Traffic signals
27. Pedestrians
28. Children crossing
29. Bicycles crossing
30. Beware of ice/snow
31. Wild animals crossing
32. End of all speed and passing limits
33. Turn right ahead
34. Turn left ahead
35. Ahead only
36. Go straight or right
37. Go straight or left
38. Keep right
39. Keep left
40. Roundabout mandatory
41. End of no passing
42. End of no passing by vehicles over 3.5 metric tons

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Training the Model

To train the model, run the following command:
```bash
python main.py
```

This will preprocess the dataset, build the model, and save the trained model as `GTSRB.h5`.

### Running the Streamlit App

To run the Streamlit application, use the following command:
```bash
streamlit run mlops2.py
```

This will start a local server, and you can access the app in your web browser at `http://localhost:8501`.

### Making Predictions

1. Upload an image of a traffic sign (PNG, JPG, JPEG).
2. The model will process the image and display the predicted traffic sign along with its description.

## Model Architecture

The model is a Convolutional Neural Network (CNN) consisting of the following layers:

- Convolutional layers with ReLU activation
- MaxPooling layers
- Dropout layers to prevent overfitting
- Fully connected layers with softmax activation for classification

## Results

After training, the model achieved the following results:
- Test Loss: [Insert Test Loss]
- Test Accuracy: [Insert Test Accuracy]

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
