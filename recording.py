import sounddevice as sd
from scipy.io.wavfile import write
from pydub import AudioSegment

fs = 44100 #Sample rate
seconds = 3 # Duration of recording

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
sd.wait() #wait until recording is finished
write('output.wav', fs, myrecording) #save as wav file
AudioSegment.from_file('output.wav')
