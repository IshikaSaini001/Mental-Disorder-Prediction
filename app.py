import streamlit as st
import pickle
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.preprocessing import LabelEncoder
import base64


# Function to load and encode the image file
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Set the path to your image file
image_path = "pexels-scottwebb-305821.jpg"  

# Convert image to base64
base64_image = get_base64_image(image_path)

# Add CSS to insert background image
page_bg_img = f'''
<style>
.stApp {{
    background-image: url("data:image/jpeg;base64,{base64_image}");
    background-size: cover;
}}
</style>
'''

# Apply the CSS
st.markdown(page_bg_img, unsafe_allow_html=True)

# Content to display
# Title and Description
# st.title("Mental Health Disorder Prediction App")
st.markdown("<h1 style='color:green;'>Mental Disorder Prediction App</h1>", unsafe_allow_html=True)

# st.write("""
# ## Overview
# This application is designed to help individuals understand their mental health better by analyzing responses to a series of questions. 
# Using a trained machine learning model, this app provides insights into potential mental health conditions based on user inputs. 
# ### How It Works
# Simply answer the questions below, and the model will predict the mental health disorder that most aligns with your responses. The results are shown with a confidence score for each possible disorder, represented in an interactive pie chart.
# ### Disclaimer
# This tool is intended for educational purposes only and should not be considered as a diagnostic tool. For an accurate diagnosis and personalized treatment, please consult a licensed mental health professional.
# """)



# Load the trained model and encoders
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# Define the label encoders used during training
encodings_objs = {}  # Load or recreate label encoders based on training code
column_options = {
    'Sadness': ['Always', 'Usually', 'Sometimes', 'Seldom', 'Never'],
    'Euphoric': ['Always', 'Usually', 'Sometimes', 'Seldom', 'Never'],
    'Exhausted': ['Always', 'Usually', 'Sometimes', 'Seldom', 'Never'],
    'Sleep dissorder': ['Always', 'Usually', 'Sometimes', 'Seldom', 'Never'],
    'Mood Swing': ['YES', 'NO'],
    'Suicidal thoughts': ['YES', 'NO'],
    'Anorxia': ['YES', 'NO'],
    'Authority Respect': ['YES', 'NO'],
    'Try-Explanation': ['YES', 'NO'],
    'Aggressive Response': ['YES', 'NO'],
    'Ignore & Move-On': ['YES', 'NO'],
    'Nervous Break-down': ['YES', 'NO'],
    'Admit Mistakes': ['YES', 'NO'],
    'Overthinking': ['YES', 'NO'],
}

# Initialize encoding objects for categorical columns
for column, categories in column_options.items():
    encoder = LabelEncoder()
    encoder.fit(categories)
    encodings_objs[column] = encoder

# Title
# st.title("Mental Disorder Prediction App")

# User Input Fields
st.markdown("### Please answer the following questions:")
patient_input = {}
for col in column_options.keys():
    patient_input[col] = st.selectbox(f"{col}:", column_options[col])

# For numerical fields (ratings)
patient_input['Sexual Activity'] = st.slider("Sexual Activity (1-10):", 1, 10, 5)
patient_input['Concentration'] = st.slider("Concentration (1-10):", 1, 10, 5)
patient_input['Optimisim'] = st.slider("Optimism (1-10):", 1, 10, 5)

# DataFrame with input
input_df = pd.DataFrame([patient_input])

# Encode categorical inputs
for col in column_options.keys():
    input_df[col] = encodings_objs[col].transform(input_df[col])

# Display Prediction Button
if st.button("Predict Mental Disorder"):
    # Get prediction probabilities
    prediction_prob = model.predict_proba(input_df)[0]
    predicted_class = model.classes_[np.argmax(prediction_prob)]
    
    # Display prediction
    st.markdown(f"### Predicted Disorder: **{predicted_class}**")

    # Pie chart of prediction confidence
    fig = px.pie(
        values=prediction_prob * 100,
        names=model.classes_,
        title="Prediction Confidence for Each Disorder"
    )
    st.plotly_chart(fig)

    import streamlit as st

# Function to display custom CSS for an aesthetic sidebar
def add_sidebar_styles():
    st.markdown("""
    <style>
        .css-1d391kg {
            background-color: #f1f3f5;
        }
        .css-ffhzg2 {
            color: #4CAF50;
            font-size: 18px;
        }
        .css-1gb49b7 {
            color: #ffffff;
            background-color: #0073e6;
        }
        .css-ffhzg2:hover {
            background-color: #0073e6;
            color: white;
        }
        .css-ffhzg2:active {
            background-color: #005bb5;
        }
        .stButton>button {
            border-radius: 5px;
            background-color: #0073e6;
            color: white;
            font-size: 16px;
            height: 40px;
        }
        .stButton>button:hover {
            background-color: white;
        }
        .stButton>button:active {
            background-color: #003d80;
        }
    </style>
    """, unsafe_allow_html=True)

# Sidebar Navigation for Multi-Page App
def app():
    add_sidebar_styles()

    # Sidebar for navigation between pages
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Select a page", 
                            options=["Home", "Mood Tracker", "My Journal", "Workload Tracker", "My Data"])

    # Show content based on selected page
    if page == "Home":
        home_page()
    elif page == "Mood Tracker":
        import mood_tracker
        mood_tracker.log_mood()
    elif page == "Daily Journal":
        import daily_journal
        daily_journal.log_journal()
    elif page == "Workload Tracker":
        import workload_tracker
        workload_tracker.track_workload()
    elif page == "My Data":
        import view_all_data
        view_all_data.view_all_data()

# Home page content
def home_page():
    st.markdown(f"<h2 style='color: black ;'>Welcome to Your Personal Tracker App</h2>", unsafe_allow_html=True)
    st.markdown(f"<p style='color: black ;'>This app helps you track your mood, manage your workload, and provides mental health tips.</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    app()





