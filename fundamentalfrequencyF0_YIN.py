import sounddevice as sd
from scipy.io.wavfile import write
import librosa
import librosa.display
import numpy as np

fs = 44100 #Sample rate
seconds = 4 #duration of recording

print('start recording')
myrecording = sd.rec(int(seconds*fs), samplerate=fs, channels=1)
sd.wait() #wait until recording is finished
print('finished recording')
write('output.wav', fs, myrecording) #save as wav file
y, sr =librosa.load('output.wav')
f0, voiced_flag, voiced_probs = librosa.pyin(y, fmin=librosa.note_to_hz('E2'), fmax=librosa.note_to_hz('E4'))
times = librosa.times_like(f0)
import matplotlib.pyplot as plt
D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)
fig, ax = plt.subplots()
img = librosa.display.specshow(D, x_axis='time', y_axis='log', ax=ax)
ax.set(title='pYIN fundamental frequency estimation')
fig.colorbar(img, ax=ax, format="%+2.f dB")
ax.plot(times, f0, label='f0', color='cyan', linewidth=3)
ax.legend(loc='upper right')
