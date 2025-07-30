import cv2
import numpy as np
import streamlit as st
from PIL import Image
import io

st.title("Image Blender App By RUSHO")

# Upload two images
file1 = st.file_uploader("Upload First Image", type=["jpg", "png"])
file2 = st.file_uploader("Upload Second Image", type=["jpg", "png"])

if file1 and file2:
    img1 = Image.open(file1)
    img2 = Image.open(file2)

    img1 = img1.resize((500, 700))
    img2 = img2.resize((500, 700))

    img1_np = np.array(img1)
    img2_np = np.array(img2)

    alpha = st.slider("Blend Ratio", 0, 100, 50) / 100
    switch = st.radio("Switch", ["OFF", "ON"])

    if switch == "ON":
        blended = cv2.addWeighted(img1_np, 1 - alpha, img2_np, alpha, 0)
    else:
        blended = np.zeros_like(img1_np)

    st.image(blended, caption=f"Blend Alpha: {alpha:.2f}", use_column_width=True)

    # Save blended image as a file and create a download button
    # Convert to PIL image for saving
    blended_image = Image.fromarray(blended)

    # Save image to a BytesIO object
    img_byte_arr = io.BytesIO()
    blended_image.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()

    # Create a download button
    st.download_button(
        label="Download Blended Image",
        data=img_byte_arr,
        file_name="blended_image.png",
        mime="image/png"
    )
