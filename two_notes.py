
import audiogen
from note_freqs import getFreq

print getFreq('F#4')
print getFreq('E4')

import time

audiogen.sampler.play(audiogen.tone(getFreq('F#4')))

time.sleep(3)
audiogen.sampler.play(audiogen.tone(getFreq('E4')))
