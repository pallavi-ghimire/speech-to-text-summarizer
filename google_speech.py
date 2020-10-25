import io
import os
# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
from google.oauth2 import service_account
from final import final


def google_speech(filename, perc):
    transcript = ""
    # Instantiates a client
    my_credentials = service_account.Credentials.from_service_account_file('Final_Year_Project-82c37bffc5b0.json')
    client = speech.SpeechClient(credentials=my_credentials)

    # Uploads the file to the bucket
    os.system("gsutil cp resources/"+filename+" gs://fyp_project_bucket")

    # For GCS
    file_name = 'gs://fyp_project_bucket/'+filename

    # Loads the audio into memory

    # For Local File
    # with io.open(file_name, 'rb') as audio_file:
    #     content = audio_file.read()
    #     audio = types.RecognitionAudio(content=content)

    # For GCS file
    audio = {'uri': file_name}
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
        sample_rate_hertz=44100,
        language_code='en-US',
        enable_automatic_punctuation=True)
    # Detects speech in the audio file
    # response = client.recognize(config, audio)

    # for result in response.results:
    #     print('Transcript: {}'.format(result.alternatives[0].transcript))

    operation = client.long_running_recognize(config, audio)
    print(u"Waiting for operation to complete...")
    response = operation.result()

    for result in response.results:
        # First alternative is the most probable result
        alternative = result.alternatives[0]
        # print(alternative.transcript)
        # print(u"{}".format(alternative.transcript))
        transcript = transcript + alternative.transcript
        # print("\nI am here" ,transcript)
        # final(transcript)
    # print(transcript)
    summary = final(transcript, perc)

    class all:
        def __init__(self):
            self.unsummarized = transcript
            self.summarized = summary
    # return summary
    return all()

# google_speech()