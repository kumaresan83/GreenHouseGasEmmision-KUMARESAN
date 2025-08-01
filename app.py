import streamlit as st
import pandas as pd


def welcome_page():
    
    st.markdown("""
        <style>
        .welcome-container {
            background-color: #00004d; /* Dark blue from the image */
            color: white;
            padding: 4rem;
            min-height: 80vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }
        .welcome-container h1 {
            color: white;
            font-size: 3rem;
            font-weight: bold;
            line-height: 1.2;
        }
        .welcome-container p {
            color: #d1fae5;
            font-size: 0.875rem;
            text-transform: uppercase;
            letter-spacing: 0.1em;
        }
        .stButton button {
            background-color: #669933; 
            color: white;
            font-weight: bold;
            padding: 0.75rem 2rem;
            border-radius: 9999px; 
            border: none;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        .stButton button:hover {
            background-color: #55802b;
        }
        </style>
        """, unsafe_allow_html=True)

    
    st.markdown(
        """
        <div class="welcome-container">
            <p>Cloud Computing & GHG Emissions By <bold>KUMARESAN</bold></p>
            <h1>Greenhouse Gas<br>Emissions in<br>Data Centres</h1>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    if st.button("Start", key="start_button"):
        st.session_state.page = 'predictor'


def predictor_page():
    st.markdown("""
        <style>
        body {
            background-color: #e6f7e6; /* Light green background */
        }
        .form-container {
            background-color: #ffffff;
            border-color: #669933; /* Green border */
        }
        .text-green-800 { color: #294c77; }
        .text-green-700 { color: #294c77; }
        .bg-green-600 { background-color: #669933; }
        .hover\:bg-green-700:hover { background-color: #55802b; }
        .focus\:ring-green-500:focus { border-color: #669933; }
        .focus\:border-green-500:focus { border-color: #669933; }
        .text-green-900 { color: #294c77; }
        .bg-green-50 { background-color: #f0fdf4; }
        .border-green-300 { border-color: #d1fae5; }
        .stButton button {
            background-color: #669933;
            color: white;
            font-weight: bold;
            padding: 0.75rem 2rem;
            border-radius: 9999px;
            position : center;
        }
        .stButton button:hover {
            background-color: #55802b;
        }
        </style>
        """, unsafe_allow_html=True)

    
    st.markdown('<h1 class="text-3xl font-bold text-green-800">Greenhouse Gas Emission Predictor</h1>', unsafe_allow_html=True)
    st.markdown('<p class="text-gray-600 mt-2">Estimate total emissions based on supply chain factors and data quality metrics.</p>', unsafe_allow_html=True)

    st.markdown('<hr class="my-6 border-green-200">', unsafe_allow_html=True)

    
    with st.form("predictor-form-content"):
        st.subheader("Product Details")

        col1, col2 = st.columns(2)
        with col1:
            substance = st.selectbox("Type of Gas:", ['carbon dioxide', 'methane', 'nitrous oxide', 'other GHGs'])
        with col2:
            unit = st.selectbox("Measurement Unit:", ['kg/2018 USD, purchaser price', 'kg CO2e/2018 USD, purchaser price'])

        col3, col4 = st.columns(2)
        with col3:
            supply_wo_margin = st.number_input("Estimated Emissions (without margin):", min_value=0.0)
        with col4:
            margin = st.number_input("Margin of Error (if known):", min_value=0.0)

        st.subheader("Data Quality")
        st.markdown('<p class="text-gray-600 italic">Please rate the quality of your data on a scale from 0.0 (low quality) to 1.0 (high quality).</p>', unsafe_allow_html=True)

        dq_reliability = st.slider("Reliability of Data", 0.0, 1.0, 0.0, step=0.01)
        dq_temporal = st.slider("Timeliness of Data", 0.0, 1.0, 0.0, step=0.01)
        dq_geo = st.slider("Geographic Relevance", 0.0, 1.0, 0.0, step=0.01)
        dq_tech = st.slider("Technological Relevance", 0.0, 1.0, 0.0, step=0.01)
        dq_data = st.slider("Data Collection Quality", 0.0, 1.0, 0.0, step=0.01)

        predict_button = st.form_submit_button("Predict Emission Factor")

    if predict_button:

        average_dq = (dq_reliability + dq_temporal + dq_geo + dq_tech + dq_data) / 5
        prediction = supply_wo_margin + margin * average_dq

        st.markdown(f"""
            <div class="mt-4 p-4 bg-green-50 text-green-900 border-2 border-green-300 rounded-lg text-xl font-bold flex items-center justify-center space-x-4 w-full">
                <span>Predicted Factor = {prediction:.4f}</span>
            </div>
        """, unsafe_allow_html=True)

        
        results_text = f"""
Greenhouse Gas Emission Predictor Results

Type of Gas: {substance}
Measurement Unit: {unit}
Estimated Emissions: {supply_wo_margin}
Margin of Error: {margin}
Reliability of Data: {dq_reliability}
Timeliness of Data: {dq_temporal}
Geographic Relevance: {dq_geo}
Technological Relevance: {dq_tech}
Data Collection Quality: {dq_data}

Predicted Factor = {prediction:.4f}
"""
        st.download_button(
            label="Download Results",
            data=results_text,
            file_name="ghg_prediction_results.txt",
            mime="text/plain",
            key="download_button"
        )


if 'page' not in st.session_state:
    st.session_state.page = 'welcome'

if st.session_state.page == 'welcome':
    welcome_page()
elif st.session_state.page == 'predictor':
    predictor_page()
    
    if st.button("< Welcome"):
        st.session_state.page = 'welcome'