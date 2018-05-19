import io
import os

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

def recognize(filename):
	# Instantiates a client
	client = speech.SpeechClient()

	# Loads the audio into memory
	with io.open(filename, 'rb') as audio_file:
	    content = audio_file.read()
	    audio = types.RecognitionAudio(content=content)

	config = types.RecognitionConfig(
	    encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
	    sample_rate_hertz=16000,
	    language_code='th-TH')

	# Detects speech in the audio file
	response = client.recognize(config, audio)

	for result in response.results:
	    return('{}'.format(result.alternatives[0].transcript))