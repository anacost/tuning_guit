import sounddevice as sd
from scipy.io.wavfile import write
import librosa
import librosa.display
import matplotlib.pyplot as plt
fs = 44100 #Sample rate
seconds = 4 #duration of recording
print('start recording')
myrecording = sd.rec(int(seconds*fs), samplerate=fs, channels=1)
sd.wait() #wait until recording is finished
print('finished recording')
write('output.wav', fs, myrecording) #save as wav file
y, sr =librosa.load('output.wav')
chroma = librosa.feature.chroma_cqt(y=y, sr=sr)
fig, ax = plt.subplots()
img = librosa.display.specshow(chroma, y_axis='chroma', x_axis='time',ax=ax)
ax.set(title='Chromagram demostration')
fig.colorbar(img, ax=ax);
