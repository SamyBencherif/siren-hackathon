#https://stackoverflow.com/questions/8299303/generating-sine-wave-sound-in-python
#
import pyaudio
import numpy as np
from note_freqs import getFreq

def getWaveformOfNote(note, length):
    volume = 0.5     # range [0.0, 1.0]
    fs = 44100       # sampling rate, Hz, must be integer
    p = pyaudio.PyAudio()
    # generate samples, note conversion to float32 array
    samples = (np.sin(2*np.pi*np.arange(fs*length)*note/fs)).astype(np.float32)
    # for paFloat32 sample values must be in range [-1.0, 1.0]
    stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=fs,
                output=True)
    # play. 
    stream.write(volume*samples)
    stream.stop_stream()
    stream.close()
    p.terminate()


getWaveformOfNote(getFreq('A4'), 1.0)
