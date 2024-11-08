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





# import streamlit as st
# import random
# import pandas as pd
# from datetime import datetime, timedelta
# import matplotlib.pyplot as plt
# from fpdf import FPDF

# # Function to display custom CSS for a more aesthetic sidebar
# def add_sidebar_styles():
#     st.markdown("""
#     <style>
#         /* Custom Sidebar Styles */
#         .css-1d391kg {
#             background-color: #f1f3f5;
#         }
#         .css-ffhzg2 {
#             color: #4CAF50;
#             font-size: 18px;
#         }
#         .css-1gb49b7 {
#             color: #ffffff;
#             background-color: #0073e6;
#         }
#         .css-ffhzg2:hover {
#             background-color: #0073e6;
#             color: white;
#         }
#         .css-ffhzg2:active {
#             background-color: #005bb5;
#         }
#         .stButton>button {
#             border-radius: 5px;
#             background-color: #0073e6;
#             color: white;
#             font-size: 16px;
#             height: 40px;
#         }
#         .stButton>button:hover {
#             background-color: white;
#         }
#         .stButton>button:active {
#             background-color: #003d80;
#         }
#     </style>
#     """, unsafe_allow_html=True)

# # Function to generate PDF from journal entries
# def generate_pdf(journal_entries):
#     pdf = FPDF()
#     pdf.set_auto_page_break(auto=True, margin=15)
#     pdf.add_page()

#     # Set title
#     pdf.set_font("Arial", "B", 16)
#     pdf.cell(200, 10, txt="Your Journal Entries", ln=True, align="C")

#     # Add entries
#     pdf.set_font("Arial", size=12)
#     for entry in journal_entries:
#         pdf.ln(10)
#         pdf.multi_cell(0, 10, f"Date: {entry['timestamp']}\n{entry['entry']}\n")

#     # Save PDF to a file
#     pdf_output = "/tmp/journal_entries.pdf"
#     pdf.output(pdf_output)
    
#     return pdf_output

# # Function for Home Page
# def home_page():
#     st.title("Welcome to Your Mental Health Support App")
#     st.write("This app helps you track your mood, manage your workload, and provides mental health tips.")
#     st.write("Please use the sidebar to navigate through the app and access different tools.")
    
# # Function to track and log mood
# def log_mood():
#     st.write("How are you feeling today?")
    
#     # Mood options
#     mood = st.radio("Select your mood:", ["Happy", "Sad", "Stressed", "Relaxed", "Anxious"])
    
#     # Store mood entry in session state
#     if 'mood_entries' not in st.session_state:
#         st.session_state.mood_entries = []

#     if st.button("Log Mood"):
#         mood_entry = {
#             "mood": mood,
#             "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         }
#         st.session_state.mood_entries.append(mood_entry)
#         st.success(f"Mood logged: {mood}")

# # Function to track and log journal entries
# def log_journal():
#     st.title("Daily Journal")
    
#     # Store journal entries in session state
#     if 'journal_entries' not in st.session_state:
#         st.session_state.journal_entries = []

#     journal_entry = st.text_area("Write down your thoughts or feelings for today:")

#     if st.button("Save Journal Entry"):
#         if journal_entry:
#             entry = {
#                 "entry": journal_entry,
#                 "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#             }
#             st.session_state.journal_entries.append(entry)
#             st.success("Journal entry saved!")
#         else:
#             st.warning("Please write something before saving.")

#     # Provide option to download the journal entries as a PDF
#     if st.session_state.journal_entries:
#         if st.button("Download Journal Entries as PDF"):
#             pdf_output = generate_pdf(st.session_state.journal_entries)
#             st.download_button(
#                 label="Download PDF",
#                 data=open(pdf_output, "rb").read(),
#                 file_name="journal_entries.pdf",
#                 mime="application/pdf"
#             )

# # Function to track workload
# def track_workload():
#     st.title("Workload Management")
    
#     # Store tasks in session state
#     if 'tasks' not in st.session_state:
#         st.session_state.tasks = []

#     task_name = st.text_input("What task are you currently working on?")
#     deadline = st.date_input("Deadline for this task:")
#     priority = st.selectbox("Priority", ["Low", "Medium", "High"])

#     if st.button("Save Task"):
#         if task_name:
#             task = {
#                 "task": task_name,
#                 "deadline": deadline.strftime("%Y-%m-%d"),
#                 "priority": priority
#             }
#             st.session_state.tasks.append(task)
#             st.success("Task saved!")
#         else:
#             st.warning("Please enter a task before saving.")

#     # Display task list
#     if st.session_state.tasks:
#         st.subheader("Your Tasks")
#         for task in st.session_state.tasks:
#             st.write(f"{task['task']} - Deadline: {task['deadline']} - Priority: {task['priority']}")
#     else:
#         st.write("No tasks added yet.")

# # Function for Mental Health Tips Page
# def mental_health_tips_page():
#     st.title("Mental Health Tips")
#     st.write("Here are some helpful mental health tips for you:")
#     tips = [
#         "Remember to take breaks regularly to clear your mind.",
#         "Stay hydrated! Dehydration can affect your mood and focus.",
#         "Don't hesitate to talk to someone when you're feeling down.",
#         "Practice mindfulness and meditation to stay calm and centered.",
#         "Set achievable goals and don't be too hard on yourself."
#     ]
    
#     # Display tips randomly
#     st.write(random.choice(tips))

# # Function to view all entries and summaries
# def view_all_data():
#     st.title("View All Your Data")
    
#     # Display Journal Entries
#     if 'journal_entries' in st.session_state and st.session_state.journal_entries:
#         st.subheader("Your Journal Entries")
#         journal_df = pd.DataFrame(st.session_state.journal_entries)
#         st.write(journal_df)
#     else:
#         st.write("No journal entries saved yet.")

#     # Display Mood History with Weekly and Monthly Summaries
#     if 'mood_entries' in st.session_state and st.session_state.mood_entries:
#         st.subheader("Mood History")
#         mood_df = pd.DataFrame(st.session_state.mood_entries)
#         st.write(mood_df)
        
#         # Weekly and Monthly Mood Summaries
#         mood_df['timestamp'] = pd.to_datetime(mood_df['timestamp'])
#         mood_df['week'] = mood_df['timestamp'].dt.isocalendar().week
#         mood_df['month'] = mood_df['timestamp'].dt.month
        
#         # Weekly Mood Summary
#         weekly_summary = mood_df.groupby('week')['mood'].value_counts().unstack().fillna(0)
#         st.subheader("Weekly Mood Summary")
#         st.write(weekly_summary)
        
#         # Monthly Mood Summary
#         monthly_summary = mood_df.groupby('month')['mood'].value_counts().unstack().fillna(0)
#         st.subheader("Monthly Mood Summary")
#         st.write(monthly_summary)
        
#         # Plotting Weekly Mood Data
#         st.subheader("Mood Data - Weekly")
#         weekly_summary.plot(kind='bar', stacked=True, figsize=(10, 6))
#         plt.title('Weekly Mood Distribution')
#         plt.xlabel('Week')
#         plt.ylabel('Count of Moods')
#         st.pyplot()

# # Main App to handle Page Navigation
# def app():
#     # Add custom sidebar styles
#     add_sidebar_styles()

#     # Sidebar for navigation
#     st.sidebar.title("Navigation")
#     page = st.sidebar.radio("Select a page", 
#                             options=["Home", "Mood Tracker", "Daily Journal", "Workload Tracker", "Mental Health Tips", "View All Data"])

#     # Show page based on selection
#     if page == "Home":
#         home_page()
#     elif page == "Mood Tracker":
#         log_mood()
#     elif page == "Daily Journal":
#         log_journal()
#     elif page == "Workload Tracker":
#         track_workload()
#     elif page == "Mental Health Tips":
#         mental_health_tips_page()
#     elif page == "View All Data":
#         view_all_data()

# if __name__ == "__main__":
#     app()
