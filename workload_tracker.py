import streamlit as st
from datetime import datetime

def track_workload():
    st.title("Workload Management")
    
    # Store tasks in session state
    if 'tasks' not in st.session_state:
        st.session_state.tasks = []

    task_name = st.text_input("What task are you currently working on?")
    deadline = st.date_input("Deadline for this task:")
    priority = st.selectbox("Priority", ["Low", "Medium", "High"])

    if st.button("Save Task"):
        if task_name:
            task = {
                "task": task_name,
                "deadline": deadline.strftime("%Y-%m-%d"),
                "priority": priority
            }
            st.session_state.tasks.append(task)
            st.success("Task saved!")
        else:
            st.warning("Please enter a task before saving.")

    # Display task list
    if st.session_state.tasks:
        st.subheader("Your Tasks")
        for task in st.session_state.tasks:
            st.write(f"{task['task']} - Deadline: {task['deadline']} - Priority: {task['priority']}")
    else:
        st.write("No tasks added yet.")
