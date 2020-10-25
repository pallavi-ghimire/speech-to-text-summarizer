# Speech-to-Text Summarizer

Speech-to-Text is an online tool that helps you transcribe your audio file and generate a summary of the text.
To run, simply type 'python hello.py'. Once running, go to http://127.0.0.1:5000/ and do the following: 
  1. Provide a file of the extension .flac as an input. Ensure that the audio clip was recorded in 44100 Hz. Either drag and drop, or click 'Browse'.
  2. Enter the percentage of the text you would want as an output summary.
  3. Click 'Start Summarization!'.
The output will be displayed in the same page after reload, just below the button you just clicked. It will consist of the entire text, and your summary.

Note:
  1. The project utilizes Google Speech-to-Text API. I had used a key that was in the file named 'Final_Year_Project-82c37bffc5b0.json'. 
  You need to download your own key in .json format and do one of the following: 
    Either copy contents from there and paste in the same file, or
    Replace the name of file in line number 14, filename: 'google_speech.py'.
  2. The 'resources' folder is only created for ease of use; for you to not misplace your audio files. It does not affect execution.
