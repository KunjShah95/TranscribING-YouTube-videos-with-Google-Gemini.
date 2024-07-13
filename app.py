import os
import streamlit as st
from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi
import google.generativeai as genai
import time
import sqlite3
import datetime

# Load environment variables
load_dotenv()

# Configure Google GenerativeAI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Database setup
conn = sqlite3.connect('history.db')  # Connect to the database outside the button block
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    youtube_link TEXT,
    output_type TEXT,
    summary TEXT
)''')
conn.commit()

# Prompts for summarization
prompt_detailed = """Welcome, Video Summarizer! Your task is to provide a very detailed breakdown of the key points and essential information from the given YouTube video transcript.  Please present your notes in a comprehensive and informative manner, including timestamps for each key point. Aim for a very detailed explanation of each point, going beyond a simple bullet point summary.  Provide as much context and information as possible for each key point. Let's dive into the provided transcript and extract the vital details for our audience.  Please format your response in a way that is easy to read and understand, with clear headings and subheadings for each key point.  Use a conversational tone and provide as much detail as possible for each key point.  Make sure to include the timestamp for each key point in your response."""

prompt_summary = """Welcome, Video Summarizer! Your task is to provide a concise summary of the key points and essential information from the given YouTube video transcript. Please present your summary in a clear and concise manner, including timestamps for each key point.  Let's dive into the provided transcript and extract the vital details for our audience.  Please format your response in a way that is easy to read and understand, with clear headings and subheadings for each key point.  Use a conversational tone and provide a brief overview of each key point.  Make sure to include the timestamp for each key point in your response."""

# Function to extract transcript details from a YouTube video URL
def extract_transcript_details(youtube_video_url):
    try:
        video_id = youtube_video_url.split("=")[1]
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)

        transcript = ""
        for i in transcript_text:
            transcript += " " + i["text"]

        return transcript
    except Exception as e:
        st.error(f"Error extracting transcript: {e}")
        return None


# Function to generate summary using Google Gemini Pro (with rate limiting)
def generate_gemini_content(transcript_text, prompt):
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt + transcript_text)
        return response.text
    except Exception as e:
        if "429" in str(e):  # Check for rate limit error
            st.error("Rate limit exceeded. Please try again later.")
            time.sleep(5)  # Wait for 5 seconds
            return None
        else:
            st.error(f"Error generating summary: {e}")
            return None


# Streamlit UI
st.title(
    "Gemini YouTube Transcript Summarizer: Extract Key Insights from YouTube Videos"
)

# Disclaimer and Citation Instructions
st.markdown("**Disclaimer:** This application uses Google Gemini Pro to generate summaries. The generated content is not original and should be cited appropriately.")
st.markdown("**Citation:** To cite the generated content, please include the following information: Google Gemini Pro, [Date of Generation], [Relevant Parameters (if any)]")

youtube_link = st.text_input("Enter YouTube Video Link:")

if youtube_link:
    video_id = youtube_link.split("=")[1]
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)

# Buttons for summary options
summary_option = st.radio("Choose Output Type:", ("Detailed Notes", "Summary"))

# History
history_option = st.selectbox("Select History:", ["None", "Detailed Notes", "Summary"])

# Generate Button
if st.button("Generate"):
    transcript_text = extract_transcript_details(youtube_link)

    if transcript_text:
        if summary_option == "Detailed Notes":
            summary = generate_gemini_content(transcript_text, prompt_detailed)
        else:
            summary = generate_gemini_content(transcript_text, prompt_summary)

        # Display summary
        if summary:
            st.markdown("## Output:")
            st.write(summary)

        # Store in database
        cursor.execute(
            "INSERT INTO history (youtube_link, output_type, summary) VALUES (?, ?, ?)",
            (youtube_link, summary_option, summary),
        )
        conn.commit()

# History Display
if history_option != "None":
    st.markdown("## History:")
    if history_option == "Detailed Notes":
        cursor.execute(
            "SELECT summary FROM history WHERE output_type = 'Detailed Notes' ORDER BY id DESC LIMIT 1"
        )
        history_summary = cursor.fetchone()
        if history_summary:
            st.write(history_summary[0])
    else:
        cursor.execute(
            "SELECT summary FROM history WHERE output_type = 'Summary' ORDER BY id DESC LIMIT 1"
        )
        history_summary = cursor.fetchone()
        if history_summary:
            st.write(history_summary[0])

conn.close()  # Close the database connection outside the button block
