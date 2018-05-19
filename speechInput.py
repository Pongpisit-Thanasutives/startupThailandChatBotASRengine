import speech_recognition as sr
import googleRecognizer
import subprocess
from subprocess import Popen, PIPE

def bandpass_filter():
    subprocess.call("./clean.sh")
    # replace pwd with your computer password
    pwd = ""
    proc = Popen(["sudo", "-S", "ffmpeg", "-i", "microphone-results-clean.wav", "-af", "highpass=300, lowpass=3400", "microphone-results-clean.wav"], stdout=PIPE, stdin=PIPE, stderr=PIPE, universal_newlines=True)
    proc.stdin.write("{}\n".format(pwd))
    out,err = proc.communicate(input="{}\n".format("y"))

def recognize(filename):
	# Speech recognition using Google Speech Recognition
	r = sr.Recognizer()
	with sr.AudioFile(filename) as source:
		audio = r.record(source)
	try:
		return r.recognize_google(audio, language='th-TH')
	except sr.UnknownValueError:
		return ''
	except sr.RequestError as e:
		return ''
	return googleRecognizer.recognize("microphone-results-clean.wav")