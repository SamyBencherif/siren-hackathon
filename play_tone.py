
import audiogen
from note_freqs import getFreq

print getFreq('F#4')
print getFreq('E4')

import time

# This is using the old method:
audiogen.sampler.play(audiogen.tone(getFreq('F#4')))

# from davy wybiral's script we can do the same thing using waveforms:
# but how exactly??