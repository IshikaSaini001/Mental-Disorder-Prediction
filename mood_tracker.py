import streamlit as st
from datetime import datetime

def log_mood():
    st.title("Mood Tracker")
    st.write("How are you feeling today?")
    
    # Mood options
    mood = st.radio("Select your mood:", ["Happy", "Sad", "Stressed", "Relaxed", "Anxious"])
    
    # Store mood entry in session state
    if 'mood_entries' not in st.session_state:
        st.session_state.mood_entries = []

    if st.button("Log Mood"):
        mood_entry = {
            "mood": mood,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        st.session_state.mood_entries.append(mood_entry)
        st.success(f"Mood logged: {mood}")
