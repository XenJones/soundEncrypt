from scipy.io.wavfile import write, read
import numpy as np
from scipy.fft import *
import librosa

def encrypt(message, file):
    samArr = np.array([])
    samplerate = 44100
    frList = list(message)
    for i in frList:
        t = np.linspace(0., 1., samplerate)
        amplitude = np.iinfo(np.int16).max
        data = amplitude * np.sin(2. * np.pi * ord(i) * 100 * t)
        samArr = np.append(samArr, data.astype(np.int16))
    samArr = samArr.astype(np.int16)
    write(file, samplerate, samArr)

def decrypt(infile, outfile):
    def freq(file, start_time, end_time):


        # Open the file and convert to mono
        sr, data = read(file)
        if data.ndim > 1:
            data = data[:, 0]
        else:
            pass

        # Return a slice of the data from start_time to end_time
        dataToRead = data[int(start_time * sr / 1000): int(end_time * sr / 1000) + 1]

        # Fourier Transform
        N = len(dataToRead)
        yf = rfft(dataToRead)
        xf = rfftfreq(N, 1 / sr)


        idx = np.argmax(np.abs(yf))
        freq = xf[idx]
        return freq

    message = ''

    for i in range(round(librosa.get_duration(path=infile))):
        frequency = freq(infile, i * 1000, i * 1000 + 1000)
        message += (chr(round((int(frequency)) / 100)))
    with open(outfile, 'w') as outfile:
        outfile.write(message)