import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image
import numpy as np

# Load the trained model
model = load_model('GTSRB.h5')

# Set up the Streamlit interface
st.title("German Traffic Sign Recognition Benchmark Dataset")
st.write("Upload an image to classify it.")

uploaded_file1 = st.file_uploader("Put the image here", type=["png"], key="uploader1")
uploaded_file2 = st.file_uploader("Put the image here", type=["png"], key="uploader2")
uploaded_file3 = st.file_uploader("Put the image here", type=["png"], key="uploader3")

selected_file = st.radio(
    "Choose the image to classify",
    ("First Image", "Second Image", "Third Image")
)

# Determine which file was selected
if selected_file == "First Image" and uploaded_file1 is not None:
    selected_image = uploaded_file1
elif selected_file == "Second Image" and uploaded_file2 is not None:
    selected_image = uploaded_file2
elif selected_file == "Third Image" and uploaded_file3 is not None:
    selected_image = uploaded_file3
else:
    selected_image = None

if selected_image is not None:
    # Load the image
    image = Image.open(selected_image).convert('L').resize((50, 50))
    st.image(selected_image, caption='Uploaded Image', use_column_width=True)

    # Prepare the image for the model
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)

    # Make a prediction
    prediction = model.predict(image)
    predicted_class = np.argmax(prediction, axis=1)[0]

    # Dictionary of class labels
    class_labels = {
        0: "Speed limit (20km/h)",
        1: "Speed limit (30km/h)",
        2: "Speed limit (50km/h)",
        3: "Speed limit (60km/h)",
        4: "Speed limit (70km/h)",
        5: "Speed limit (80km/h)",
        6: "End of speed limit (80km/h)",
        7: "Speed limit (100km/h)",
        8: "Speed limit (120km/h)",
        9: "No passing",
        10: "No passing for vehicles over 3.5 metric tons",
        11: "Right-of-way at the next intersection",
        12: "Priority road",
        13: "Yield",
        14: "Stop",
        15: "No Vehicles",
        16: "Vehicles over 3.5 metric tons prohibited",
        17: "No entry",
        18: "General caution",
        19: "Dangerous curve to the left",
        20: "Dangerous curve to the right",
        21: "Double curve",
        22: "Bumpy road",
        23: "Slippery road",
        24: "Road narrows on the right",
        25: "Road work",
        26: "Traffic signals",
        27: "Pedestrians",
        28: "Children crossing",
        29: "Bicycles crossing",
        30: "Beware of ice/snow",
        31: "Wild animals crossing",
        32: "End of all speed and passing limits",
        33: "Turn right ahead",
        34: "Turn left ahead",
        35: "Ahead only",
        36: "Go straight or right",
        37: "Go straight or left",
        38: "Keep right",
        39: "Keep left",
        40: "Roundabout mandatory",
        41: "End of no passing",
        42: "End of no passing by vehicles over 3.5 metric tons"
    }

    # Display the prediction
    st.write(f"Prediction: {class_labels.get(predicted_class, 'Unknown')}")
