import streamlit as st
import pandas as pd

def view_all_data():
    st.title("View All Your Data")
    
    # Display Journal Entries
    if 'journal_entries' in st.session_state and st.session_state.journal_entries:
        st.subheader("Your Journal Entries")
        journal_df = pd.DataFrame(st.session_state.journal_entries)
        st.write(journal_df)
    else:
        st.write("No journal entries saved yet.")

    # Display Mood History
    if 'mood_entries' in st.session_state and st.session_state.mood_entries:
        st.subheader("Mood History")
        mood_df = pd.DataFrame(st.session_state.mood_entries)
        st.write(mood_df)
