import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image


# Page Configuration

st.set_page_config(
    page_title="NeuroVision AI",
    page_icon="🧠",
    layout="centered"
)


# Title

st.title("🧠 NeuroVision AI")
st.subheader("Brain Tumor MRI Classification")

st.write(
    "Upload a brain MRI image and NeuroVision AI will classify it "
    "into one of four categories."
)


# Load Model

@st.cache_resource
def load_model():
    return tf.keras.models.load_model("brain_tumor_model.keras")

model = load_model()


# Classes

CLASS_NAMES = [
    "Glioma",
    "Meningioma",
    "No Tumor",
    "Pituitary"
]


# Image Upload

uploaded_file = st.file_uploader(
    "Upload a Brain MRI Image",
    type=["jpg", "jpeg", "png"]
)


# Prediction
if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    st.image(
        image,
        caption="Uploaded MRI Image",
        use_container_width=True
    )

    # Resize image
    image = image.resize((224, 224))

    # Convert to NumPy
    img_array = np.array(image)

    # Normalize
    img_array = img_array / 255.0

    # Add batch dimension
    img_array = np.expand_dims(img_array, axis=0)

    if st.button("🔍 Predict Tumor"):

        with st.spinner("Analyzing MRI..."):

            prediction = model.predict(img_array)

            predicted_class = np.argmax(prediction[0])
            confidence = float(np.max(prediction[0])) * 100

        st.success(
            f"Prediction: **{CLASS_NAMES[predicted_class]}**"
        )

        st.info(
            f"Confidence: **{confidence:.2f}%**"
        )

        # Show probabilities
        st.subheader("Prediction Probabilities")

        for i, class_name in enumerate(CLASS_NAMES):
            probability = float(prediction[0][i]) * 100

            st.write(
                f"{class_name}: {probability:.2f}%"
            )

            st.progress(
                min(probability / 100, 1.0)
            )


# Disclaimer

st.divider()

st.caption(
    "⚠️ Educational/research prototype only. "
    "This application is not intended for medical diagnosis."
)