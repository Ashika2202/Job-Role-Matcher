import os
import streamlit as st
import google.generativeai as genai

# ✅ Directly set your API key here (RECOMMENDED for local testing)
GOOGLE_API_KEY = "AIzaSyBuLPYzZnpgBAaS8E5e4pIK1D3citOoZHQ"

# Configure Gemini with API key
genai.configure(api_key=GOOGLE_API_KEY)

# Load Gemini model
model = genai.GenerativeModel("gemini-2.0-flash")

# Streamlit page setup
st.set_page_config(page_title="🔍 Job Role Matcher", layout="centered")

st.markdown(
    """
    <h2 style="text-align: center;">🔍 Job Role Matcher</h2>
    <p style="text-align: center; font-size: 16px;">
        Discover career paths based on your <b>skills</b>, <b>experience</b>, and <b>interests</b>. 
        Powered by Google Gemini AI.
    </p>
    <hr>
    """,
    unsafe_allow_html=True,
)

# Form for user input
with st.form("job_matcher_form"):
    st.subheader("📝 Your Profile")
    skills = st.text_area("💼 Skills", placeholder="e.g. Python, JavaScript, Data Analysis")
    experience = st.text_input("📊 Experience", placeholder="e.g. 2 years in web development")
    interests = st.text_area("🎯 Interests", placeholder="e.g. AI, startups, fintech")

    submitted = st.form_submit_button("🚀 Generate Job Matches")

# When form is submitted
if submitted:
    if not skills or not experience or not interests:
        st.warning("🚫 Please fill in all the fields.")
    else:
        with st.spinner("🔎 Generating your personalized job recommendations..."):
            prompt = f"""
You are an AI career assistant. Based on the user's profile below:

Skills: {skills}
Experience: {experience}
Interests: {interests}

Suggest the top 5 most relevant job roles and industries. For each role, provide:
1. **Job Title** – Industry
2. **Why this fits the user** (2-3 lines)
3. **Upskilling Tip** (1-2 lines)

Output should be clear, professional, and easy to read.
"""
            try:
                response = model.generate_content(prompt)
                st.success("✅ Here are your top 5 job matches:")
                st.markdown(
                    f"<div style='background-color: #f9f9f9; padding: 15px; border-radius: 10px;'>{response.text}</div>",
                    unsafe_allow_html=True
                )
            except Exception as e:
                st.error(f"❌ Error generating recommendations: {e}")
