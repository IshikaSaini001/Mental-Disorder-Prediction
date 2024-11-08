import streamlit as st
from datetime import datetime
from fpdf import FPDF

def generate_pdf(journal_entries):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Set title
    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, txt="Your Journal Entries", ln=True, align="C")

    # Add entries
    pdf.set_font("Arial", size=12)
    for entry in journal_entries:
        pdf.ln(10)
        pdf.multi_cell(0, 10, f"Date: {entry['timestamp']}\n{entry['entry']}\n")

    # Save PDF to a file
    pdf_output = "/tmp/journal_entries.pdf"
    pdf.output(pdf_output)
    
    return pdf_output

def log_journal():
    st.title("Daily Journal")
    
    # Store journal entries in session state
    if 'journal_entries' not in st.session_state:
        st.session_state.journal_entries = []

    journal_entry = st.text_area("Write down your thoughts or feelings for today:")

    if st.button("Save Journal Entry"):
        if journal_entry:
            entry = {
                "entry": journal_entry,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            st.session_state.journal_entries.append(entry)
            st.success("Journal entry saved!")
        else:
            st.warning("Please write something before saving.")

    # Provide option to download the journal entries as a PDF
    if st.session_state.journal_entries:
        if st.button("Download Journal Entries as PDF"):
            pdf_output = generate_pdf(st.session_state.journal_entries)
            st.download_button(
                label="Download PDF",
                data=open(pdf_output, "rb").read(),
                file_name="journal_entries.pdf",
                mime="application/pdf"
            )
