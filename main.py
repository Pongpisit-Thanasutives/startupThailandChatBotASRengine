import os
import Microphone
import speechInput
import dialogflowClient
from pysine import sine

sine(frequency=640.0, duration=0.1)
Microphone.record("microphone-results.wav", 4)
speechInput.bandpass_filter()
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'startupthailandchatbot.json'
dialogflowClient.detect_intent_audio(project_id="startupthailandchatbot", session_id="0", audio_file_path="microphone-results-clean.wav", language_code="th-TH")