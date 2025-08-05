import streamlit as st
from utils.parse_transcript import read_transcript
from agent.meeting_agent import extract_summary_and_actions

st.title("📋 AI Meeting Summary & Action Item Extractor")

uploaded_file = st.file_uploader("Upload Meeting Transcript (.txt)", type=["txt"])
openai_key = st.text_input("Enter OpenAI API Key", type="password")

if uploaded_file and openai_key:
    transcript = uploaded_file.read().decode("utf-8")
    st.text_area("Meeting Transcript", transcript, height=300)

    if st.button("Extract Summary & Actions"):
        with st.spinner("Extracting..."):
            result = extract_summary_and_actions(transcript, openai_key)
            st.markdown("### 📝 Extracted Info")
            st.markdown(result)
