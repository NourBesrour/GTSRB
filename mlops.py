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

# File uploader for the image
uploaded_file = st.file_uploader("Put the image here", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Load the image
    image = Image.open(uploaded_file).convert('L').resize((50, 50))
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Prepare the image for the model
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)

    # Make a prediction
    prediction = model.predict(image)
    predicted_class = np.argmax(prediction, axis=1)[0]

    # Mapping the predicted class to traffic sign names
    traffic_signs = [
        "Speed limit (20km/h)", "Speed limit (30km/h)", "Speed limit (50km/h)", 
        "Speed limit (60km/h)", "Speed limit (70km/h)", "Speed limit (80km/h)", 
        "End of speed limit (80km/h)", "Speed limit (100km/h)", "Speed limit (120km/h)", 
        "No passing", "No passing for vehicles over 3.5 metric tons", 
        "Right-of-way at the next intersection", "Priority road", "Yield", "Stop", 
        "No Vehicles", "Vehicles over 3.5 metric tons prohibited", "No entry", 
        "General caution", "Dangerous curve to the left", "Dangerous curve to the right", 
        "Double curve", "Bumpy road", "Slippery road", "Road narrows on the right", 
        "Road work", "Traffic signals", "Pedestrians", "Children crossing", 
        "Bicycles crossing", "Beware of ice/snow", "Wild animals crossing", 
        "End of all speed and passing limits", "Turn right ahead", "Turn left ahead", 
        "Ahead only", "Go straight or right", "Go straight or left", 
        "Keep right", "Keep left", "Roundabout mandatory", "End of no passing", 
        "End of no passing by vehicles over 3.5 metric tons"
    ]

    # Display the prediction
    if predicted_class < len(traffic_signs):
        st.markdown(f"<h1 style='font-size: 2em;'>Prediction: {traffic_signs[predicted_class]}</h1>", unsafe_allow_html=True)
    else:
        st.markdown("<h1 style='font-size: 2em;'>Unknown class.</h1>", unsafe_allow_html=True)


