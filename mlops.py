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

uploaded_file1 = st.file_uploader("Put the image here", type=["png"])
uploaded_file2 = st.file_uploader("Put the image here", type=["png"])
uploaded_file3 = st.file_uploader("Put the image here", type=["png"])

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
    if predicted_class == 0:
        st.write(f"Prediction: Speed limit (20km/h)")
    elif predicted_class == 1:
        st.write(f"Prediction: Speed limit (30km/h)")
    elif predicted_class == 2:
        st.write(f"Prediction: Speed limit (50km/h)")   
    elif predicted_class == 3:
        st.write(f"Prediction: Speed limit (60km/h)")
    elif predicted_class == 4:
        st.write(f"Prediction: Speed limit (70km/h)")
    elif predicted_class == 5:
        st.write(f"Prediction: Speed limit (80km/h)")   
    elif predicted_class == 6:
        st.write(f"Prediction: End of speed limit (80km/h)")       
    elif predicted_class == 7:
        st.write(f"Prediction: Speed limit (100km/h)")
    elif predicted_class == 8:
        st.write(f"Prediction: Speed limit (120km/h)")   
    elif predicted_class == 9:
        st.write(f"Prediction: No passing")
    elif predicted_class == 10:
        st.write(f"Prediction: No passing for vehicles over 3.5 metric tons")
    elif predicted_class == 11:
        st.write(f"Prediction: Right-of-way at the next intersection")   
    elif predicted_class == 12:
        st.write(f"Prediction: Priority road") 
    elif predicted_class == 13:
        st.write(f"Prediction: Yield")
    elif predicted_class == 14:
        st.write(f"Prediction: Stop")   
    elif predicted_class == 15:
        st.write(f"Prediction: No Vehicles")
    elif predicted_class == 16:
        st.write(f"Prediction: Vehicles over 3.5 metric tons prohibited")
    elif predicted_class == 17:
        st.write(f"Prediction: No entry")   
    elif predicted_class == 18:
        st.write(f"Prediction: General caution")       
    elif predicted_class == 19:
        st.write(f"Prediction: Dangerous curve to the left")
    elif predicted_class == 20:
        st.write(f"Prediction: Dangerous curve to the right")   
    elif predicted_class == 21:
        st.write(f"Prediction: Double curve")
    elif predicted_class == 22:
        st.write(f"Prediction: Bumpy road")
    elif predicted_class == 23:
        st.write(f"Prediction: Slippery road")   
    elif predicted_class == 24:
        st.write(f"Prediction: Road narrows on the right")
    elif predicted_class == 25:
        st.write(f"Prediction: Road work")
    elif predicted_class == 26:
        st.write(f"Prediction: Traffic signals")   
    elif predicted_class == 27:
        st.write(f"Prediction: Pedestrians")
    elif predicted_class == 28:
        st.write(f"Prediction: Children crossing")
    elif predicted_class == 29:
        st.write(f"Prediction: Bicycles crossing")   
    elif predicted_class == 30:
        st.write(f"Prediction: Beware of ice/snow")       
    elif predicted_class == 31:
        st.write(f"Prediction: Wild animals crossing")
    elif predicted_class == 32:
        st.write(f"Prediction: End of all speed and passing limits")   
    elif predicted_class == 33:
        st.write(f"Prediction: Turn right ahead")
    elif predicted_class == 34:
        st.write(f"Prediction: Turn left ahead")
    elif predicted_class == 35:
        st.write(f"Prediction: Ahead only")   
    elif predicted_class == 36:
        st.write(f"Prediction: Go straight or right")    
    elif predicted_class == 37:
        st.write(f"Prediction: Go straight or left")
    elif predicted_class ==38:
        st.write(f"Prediction: Keep right")   
    elif predicted_class == 39:
        st.write(f"Prediction: Keep left")
    elif predicted_class == 40:
        st.write(f"Prediction: Roundabout mandatory")
    elif predicted_class == 41:
        st.write(f"Prediction: End of no passing")   
    elif predicted_class == 42:
        st.write(f"Prediction: End of no passing by vehicles over 3.5 metric tons")       
   
    


    
