import streamlit as st

# --- Streamlit UI ---
st.set_page_config(page_title="Interview Coach", page_icon="🎤")

st.title("📝 AI Interview Coach")
st.write("Upload your CV and click the button to generate interview questions.")

# Upload CV
uploaded_file = st.file_uploader("Upload your CV (PDF or DOCX)", type=["pdf", "docx"])

# Button to generate questions
if uploaded_file:
    generate_button = st.button("🎯 Generate Interview Questions")
    
    if generate_button:
        st.success("Questions will be generated here (coming soon).")
