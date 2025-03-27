import os
import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import numpy as np
from scipy.ndimage import label
import cv2
import pandas as pd
from streamlit_lottie import st_lottie
import requests

# Function to load Lottie animations from a URL
def load_lottie_url(url: str):
    try:
        response = requests.get(url)
        if response.status_code != 200:
            return None
        return response.json()
    except Exception as e:
        print(f"Error loading Lottie animation: {e}")
        return None

# Function to analyze bubbles in the image
def analyze_bubbles(image_array):
    # Convert the image to binary using thresholding
    _, binary_image = cv2.threshold(image_array, 128, 255, cv2.THRESH_BINARY)

    # Label connected components (bubbles)
    labeled_image, num_bubbles = label(binary_image)

    # Calculate bubble areas and diameters
    bubble_areas = [np.sum(labeled_image == bubble_id) for bubble_id in range(1, num_bubbles + 1)]
    bubble_diameters_pixels = [2 * (area / np.pi) ** 0.5 for area in bubble_areas]  # Diameter from area

    # Convert to cm and mm (assuming pixel-to-cm ratio is 0.0264 cm/pixel)
    pixel_to_cm_ratio = 0.0264
    bubble_diameters_cm = [d * pixel_to_cm_ratio for d in bubble_diameters_pixels]
    bubble_diameters_mm = [d * pixel_to_cm_ratio * 10 for d in bubble_diameters_pixels]

    # Create a DataFrame with results
    data = {
        "Bubble ID": list(range(1, num_bubbles + 1)),
        "Bubble Area (pixels²)": bubble_areas,
        "Bubble Diameter (pixels)": bubble_diameters_pixels,
        "Bubble Diameter (cm)": bubble_diameters_cm,
        "Bubble Diameter (mm)": bubble_diameters_mm,
    }
    df_results = pd.DataFrame(data).sort_values(by="Bubble Diameter (pixels)", ascending=True).reset_index(drop=True)

    return num_bubbles, df_results, labeled_image

# Function to mark bubbles with numbers on the image
def mark_bubbles_with_numbers(image_array, labeled_image):
    marked_image = Image.fromarray(image_array).convert("RGB")
    draw = ImageDraw.Draw(marked_image)

    font_size = max(10, int(image_array.shape[0] / 50))  # Dynamic font size based on image dimensions
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except IOError:
        font = ImageFont.load_default()

    for bubble_id in range(1, np.max(labeled_image) + 1):
        coords = np.argwhere(labeled_image == bubble_id)
        if len(coords) > 0:
            y_min, x_min = coords.min(axis=0)
            y_max, x_max = coords.max(axis=0)
            center_x, center_y = int((x_min + x_max) / 2), int((y_min + y_max) / 2)
            draw.rectangle([x_min, y_min, x_max, y_max], outline="red", width=2)
            draw.text((center_x - font_size // 2, center_y - font_size // 2), str(bubble_id), fill="yellow", font=font)

    return marked_image

# Streamlit app configuration
st.set_page_config(
    page_title="Bubble Analysis App",
    page_icon="🌊",
    layout="wide",
)

# Load Lottie animations for header and footer
header_animation_url = "https://assets7.lottiefiles.com/packages/lf20_i9mxcD.json"
footer_animation_url = "https://assets7.lottiefiles.com/packages/lf20_kxsdj5o6.json"  # New footer animation URL
header_animation = load_lottie_url(header_animation_url)
footer_animation = load_lottie_url(footer_animation_url)

# Display header with animation (fallback if not loaded)
st.title("🌊 Bubble Analysis App")
if header_animation:
    st_lottie(header_animation, height=200)
else:
    st.warning("Unable to load header animation.")

# Ask user whether to use the previous image or upload a new one
use_previous_image = st.radio(
    "Do you want to use the previous image or upload a new one?",
    options=["Use Previous Image", "Upload New Image"]
)

image_path = "image_analysis_1.jpg"  # Default image path

if use_previous_image == "Use Previous Image":
    if not os.path.isfile(image_path):  # Check if the file exists
        st.warning("There is no previous data to be loaded.")
        st.stop()
    else:
        image = Image.open(image_path).convert("L")
else:
    uploaded_file = st.file_uploader("Upload an Image of Bubbles (JPG or PNG)", type=["jpg", "jpeg", "png"])
    
    if uploaded_file:
        image = Image.open(uploaded_file).convert("L")
        image.save(image_path)  # Save the uploaded image for future use
    else:
        st.warning("Please upload an image to proceed.")
        st.stop()

# Convert the grayscale image to a numpy array for processing
image_array = np.array(image)

# Perform analysis on bubbles in the image
num_bubbles, df_results, labeled_image = analyze_bubbles(image_array)

# Display results table first
st.write("### Results Table")
st.dataframe(df_results.style.format("{:.4f}"))

# Bubble marking option with numbering
mark_bubbles_option = st.checkbox("Mark Bubbles with Numbers on Uploaded Image")

if mark_bubbles_option:
    marked_image_with_numbers = mark_bubbles_with_numbers(image_array, labeled_image)
    st.image(marked_image_with_numbers, caption="Image with Marked Bubbles and Numbers", use_container_width=True)

# Bubble analysis tabbed interface
tab1, tab2 = st.tabs(["Bubble Analysis", "Detailed Bubble Study"])

with tab1:
    st.success("Bubble Analysis Complete!")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric(label="Number of Bubbles", value=num_bubbles)

with tab2:
    selected_bubble_id = st.number_input(
        "Enter the Bubble ID You Want to Study:",
        min_value=1,
        max_value=num_bubbles,
        step=1,
    )

    if selected_bubble_id:
        selected_bubble_data = df_results[df_results["Bubble ID"] == selected_bubble_id]
        
        if not selected_bubble_data.empty:
            st.write(f"### Details of Bubble ID #{selected_bubble_id}")
            st.write(f"- **Area:** {selected_bubble_data['Bubble Area (pixels²)'].values[0]:.2f} pixels²")
            st.write(f"- **Diameter (pixels):** {selected_bubble_data['Bubble Diameter (pixels)'].values[0]:.4f} pixels")
            st.write(f"- **Diameter (cm):** {selected_bubble_data['Bubble Diameter (cm)'].values[0]:.4f} cm")
            st.write(f"- **Diameter (mm):** {selected_bubble_data['Bubble Diameter (mm)'].values[0]:.4f} mm")

# Footer Animation and Style Tips
st.markdown("---")
if footer_animation:
    st_lottie(footer_animation, height=150)
else:
    st.warning("Unable to load footer animation.")
st.write("Designed with ❤️ using Streamlit.")

#streamlit run /workspaces/Algorithmic_Trading_K25/MAJOR_PROJECT/T1.py --server.enableCORS false --server.enableXsrfProtection false
