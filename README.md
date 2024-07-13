**YouTube Transcript Summarization with Gemini**

This Streamlit app utilizes Google Gemini Pro to create detailed notes or concise summaries from YouTube video transcripts, offering a user-friendly interface for extracting key insights.

**Key Features:**
- Input a YouTube video link to extract the transcript and receive either detailed notes or a concise summary.
- Detailed Notes: Get a comprehensive breakdown of key points with timestamps, context, and explanations.
- Concise Summary: Receive a brief overview of the video's main points along with timestamps.
- History Storage: Summaries are saved in a database for easy access and review.
- User-Friendly Interface: Interact with the app through a simple and intuitive web-based interface with Streamlit.

**Installation Guide:**
1. Install Python from [https://www.python.org/] if not already installed.
2. Install required libraries:
   - streamlit
   - youtube-transcript-api
   - google-generativeai
   - sqlite3
3. Obtain a Google Generative AI API key from [https://cloud.google.com/generative-ai].
4. Create a .env file in the project's root directory and add: GOOGLE_API_KEY=YOUR_API_KEY
5. Install python-dotenv: pip install python-dotenv
6. Load environment variables in app.py:
   ```python
   from dotenv import load_dotenv
   load_dotenv()
   ```
**Running the App:**
- Save the code as app.py.
- Run the script in the terminal: streamlit run app.py

**Usage:**
- Launch the app by running app.py.
- Paste the YouTube video URL.
- Choose "Detailed Notes" or "Summary".
- Click "Generate" to process the transcript and view the output.
- Previously generated summaries can be accessed via the "Select History" dropdown.

**Notes:**
- History is stored in a SQLite database named history.db.
- Google Gemini Pro is used for text generation; remember to cite the generated content appropriately.
