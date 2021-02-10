import sounddevice as sd
from scipy.io.wavfile import write
import librosa

fs = 44100 #Sample rate
seconds = 4 #duration of recording

print('start recording')
myrecording = sd.rec(int(seconds*fs), samplerate=fs, channels=1)
sd.wait() #wait until recording is finished
print('finished recording')
write('output.wav', fs, myrecording) #save as wav file
y, sr =librosa.load('output.wav')
librosa.yin(y, fmin=310, fmax=400)

# Guitar strings are E2=82.41Hz, A2=110Hz, D3=146.8Hz, G3=196Hz, B3=246.9Hz, E4=329.6Hz