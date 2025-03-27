import streamlit as st
from PIL import Image
import numpy as np
import cv2
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

# Function to analyze bubble intensity and identify the most suitable bubble
def analyze_bubbles(image_array):
    # Convert the image to binary using thresholding
    _, binary_image = cv2.threshold(image_array, 128, 255, cv2.THRESH_BINARY)

    # Find contours of bubbles in the binary image
    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Calculate bubble areas and identify the largest bubble
    bubble_areas = [cv2.contourArea(c) for c in contours]
    largest_bubble_index = np.argmax(bubble_areas) if bubble_areas else None

    return len(contours), contours, largest_bubble_index, bubble_areas

# Function to analyze surface properties of the most suitable bubble
def analyze_surface_properties(contours, largest_bubble_index):
    if largest_bubble_index is None:
        return 0, 0

    # Extract the contour of the largest bubble
    largest_contour = contours[largest_bubble_index]

    # Calculate perimeter and circularity
    perimeter = cv2.arcLength(largest_contour, True)
    area = cv2.contourArea(largest_contour)
    circularity = (4 * np.pi * area) / (perimeter ** 2) if perimeter > 0 else 0

    return perimeter, circularity

# Function to calculate bubble size, diameter, average diameter, and relate them to mass transfer
def calculate_mass_transfer(bubble_areas):
    # Calculate diameters from areas (assuming circular bubbles)
    bubble_diameters = [2 * (area / np.pi) ** 0.5 for area in bubble_areas]
    average_diameter = np.mean(bubble_diameters) if bubble_diameters else 0

    # Relate bubble size and diameter to mass transfer coefficient (k_La)
    k_L = 0.02  # Liquid-side mass transfer coefficient (m/s)
    interfacial_area = sum(bubble_areas)  # Total interfacial area
    k_La = k_L * interfacial_area  # Volumetric mass transfer coefficient

    return bubble_diameters, average_diameter, k_La

# Streamlit app configuration
st.set_page_config(
    page_title="Bubble Hydrodynamics and Mass Transfer Analysis",
    page_icon="🌊",
    layout="wide",
)

# Load Lottie animations for header and footer
header_animation_url = "https://assets7.lottiefiles.com/packages/lf20_i9mxcD.json"
footer_animation_url = "https://assets7.lottiefiles.com/packages/lf20_tljjah.json"
header_animation = load_lottie_url(header_animation_url)
footer_animation = load_lottie_url(footer_animation_url)

# Display header with animation (fallback if not loaded)
st.title("🌊 Bubble Hydrodynamics and Mass Transfer Analysis")
if header_animation:
    st_lottie(header_animation, height=200)
else:
    st.warning("Unable to load header animation.")

# File uploader for image files
uploaded_file = st.file_uploader("Upload an Image of Bubbles (JPG or PNG)", type=["jpg", "jpeg", "png"])

if uploaded_file:
    st.info("Processing uploaded image...")
    
    # Load the image using PIL and convert it to grayscale
    image = Image.open(uploaded_file).convert("L")
    
    # Convert the grayscale image to a numpy array for processing
    image_array = np.array(image)

    # Display the uploaded grayscale image
    st.image(image_array, caption="Uploaded Grayscale Image", use_column_width=True)

    # Perform analysis on bubbles in the image
    num_bubbles, contours, largest_bubble_index, bubble_areas = analyze_bubbles(image_array)

    # Analyze surface properties of the most suitable bubble (largest)
    perimeter, circularity = analyze_surface_properties(contours, largest_bubble_index)

    # Calculate mass transfer parameters based on all bubbles in the image
    bubble_diameters, average_diameter, k_La = calculate_mass_transfer(bubble_areas)

    # Display results in a visually appealing way
    st.success("Analysis Complete!")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric(label="Number of Bubbles", value=num_bubbles)
        st.metric(label="Largest Bubble Area (pixels)", value=f"{bubble_areas[largest_bubble_index]:.2f}" if largest_bubble_index is not None else "N/A")
        st.metric(label="Perimeter of Largest Bubble", value=f"{perimeter:.2f}")
    
    with col2:
        st.metric(label="Circularity of Largest Bubble", value=f"{circularity:.4f}")
        st.metric(label="Average Bubble Diameter (pixels)", value=f"{average_diameter:.2f}")
        st.metric(label="Volumetric Mass Transfer Coefficient (k_La)", value=f"{k_La:.4f} m/s")

# Footer Animation and Style Tips
st.markdown("---")
if footer_animation:
    st_lottie(footer_animation, height=150)
else:
    st.warning("Unable to load footer animation.")
st.write("Designed with ❤️ using Streamlit.")


#streamlit run /workspaces/Algorithmic_Trading_K25/MAJOR_PROJECT/t_1.py --server.enableCORS false --server.enableXsrfProtection false
