# TranscribING-YouTube-videos-with-Google-Gemini.

# Gemini YouTube Transcript Summarizer

This Streamlit application leverages Google Gemini Pro to generate detailed notes or concise summaries from YouTube video transcripts. It provides a user-friendly interface for extracting key insights and storing them for future reference.

## Features

- **YouTube Video Transcript Summarization:**  Input a YouTube video link, and the app will extract the transcript and generate either detailed notes or a concise summary.
- **Detailed Notes:**  Provides a comprehensive breakdown of key points, including timestamps, context, and explanations.
- **Concise Summary:**  Offers a brief overview of the video's main points, also with timestamps.
- **History Storage:**  Saves generated summaries in a database for easy access and review.
- **User-Friendly Interface:**  Streamlit provides a simple and intuitive web-based interface for interacting with the app.

## Installation

1. **Install Python:** If you don't have Python installed, download and install it from [https://www.python.org/](https://www.python.org/).
2. **Install Required Libraries:**
   ```bash
   pip install streamlit youtube-transcript-api google-generativeai sqlite3
Set up Google Generative AI API Key:
Obtain an API key from https://cloud.google.com/generative-ai.
Create a .env file in the root directory of your project and add the following line:
GOOGLE_API_KEY=YOUR_API_KEY
Install the python-dotenv package:
pip install python-dotenv
Import and load the environment variables in your app.py file:
from dotenv import load_dotenv
load_dotenv()
Running the App
Save the code: Save the provided Python code as app.py.
Run the script: Open a terminal or command prompt and navigate to the directory where you saved the file. Then, run the following command:
streamlit run app.py
Usage
Launch the app: Run the app.py script.
Enter YouTube Link: Paste the URL of the YouTube video you want to summarize.
Choose Output Type: Select either "Detailed Notes" or "Summary" based on your preference.
Generate: Click the "Generate" button to process the transcript and generate the output.
View Output: The generated summary will be displayed below the "Output" heading.
Access History: Use the "Select History" dropdown to view previously generated summaries.
Notes
The app stores history in a SQLite database named history.db.
The app uses Google Gemini Pro for text generation. Make sure to cite the generated content appropriately.
