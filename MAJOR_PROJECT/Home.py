import streamlit as st

# Page configuration with no sidebar
st.set_page_config(
    page_title="Chemical Engineering Analysis Tools",
    page_icon="⚗️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide sidebar and add styling
st.markdown("""
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
    .main {
        background-color: #f5f7f9;
        position: relative;
    }
    .tool-card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        height: 100%;
        transition: transform 0.3s ease;
    }
    .tool-card:hover {
        transform: translateY(-5px);
    }
    .tool-button {
        display: block;
        background-color: #4CAF50;
        color: white;
        padding: 15px 30px;
        border-radius: 5px;
        text-align: center;
        margin-top: 20px;
        text-decoration: none;
        font-weight: bold;
    }
    .tool-button:hover {
        background-color: #45a049;
    }
</style>
""", unsafe_allow_html=True)

# Title section
st.markdown("""
<div style='text-align: center; padding: 30px 0;'>
    <h1 style='color: #2c3e50; font-size: 2.5em; margin-bottom: 20px;'>
        Chemical Engineering Analysis Suite
    </h1>
</div>
""", unsafe_allow_html=True)

# Create two columns for the tools
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="tool-card">
        <h2 style='color: #2c3e50; margin-bottom: 20px;'>Mass Transfer Analysis Tool 🧪</h2>
        <p style='color: #34495e; margin: 20px 0;'>
        Comprehensive mass transfer analysis features:
        <ul>
            <li>Sherwood number correlations</li>
            <li>Real-time data processing</li>
            <li>Multiple regression analysis</li>
            <li>Uncertainty quantification</li>
            <li>Advanced visualization</li>
            <li>Predictive modeling</li>
        </ul>
        </p>
        <a href="Mass_Transfer_Analysis" class="tool-button">
            Launch Mass Transfer Analysis
        </a>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="tool-card">
        <h2 style='color: #2c3e50; margin-bottom: 20px;'>Bubble Analysis Tool 🔍</h2>
        <p style='color: #34495e; margin: 20px 0;'>
        Advanced bubble detection features:
        <ul>
            <li>Automated bubble detection</li>
            <li>Size distribution analysis</li>
            <li>Spatial distribution mapping</li>
            <li>Cluster analysis</li>
            <li>3D visualization</li>
            <li>Statistical analysis</li>
        </ul>
        </p>
        <a href="Bubble_Analysis" class="tool-button">
            Launch Bubble Analysis
        </a>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
<div style='text-align: center; padding: 30px 0; margin-top: 30px;'>
    <p style='color: #34495e;'>
        Powered by Advanced Analytics & Machine Learning
    </p>
</div>
""", unsafe_allow_html=True)

# cd /workspaces/Algorithmic_Trading_K25/MAJOR_PROJECT
# streamlit run Home.py --server.enableCORS false --server.enableXsrfProtection false