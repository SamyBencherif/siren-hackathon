from play_tone_wf import getWaveformOfNote, playWaveform, getWaveformOfSilence
from note_freqs import getFreq

import numpy as np

masm_src = open('MarioThemCode.masm', 'r+t').read()


treble_notes = []
bass_notes = []

qbt = .3

def is_rest(col):
	return True in [sum(x)==0 for x in col]

for line in masm_src.split('\n'):
	if len(line) and line[0] == '*':
		pass
	elif line[:3] == '---':
		clef = line.split()[1]
	elif line == '|':
		pass
	elif line == 'QUARTER_REST':
		pass
		# TODO implement this rest

		if clef.lower() == "treble":
			treble_notes.append([getWaveformOfSilence(qbt)])
		else:  # bass
			bass_notes.append([getWaveformOfSilence(qbt)])

	elif line == 'HALF_REST':
		pass
		# TODO implement this rest

		if clef.lower() == "treble":
			treble_notes.append([getWaveformOfSilence(qbt)])
			treble_notes.append([getWaveformOfSilence(qbt)])
		else:  # bass
			bass_notes.append([getWaveformOfSilence(qbt)])
			bass_notes.append([getWaveformOfSilence(qbt)])
	elif line == 'WHOLE_REST':
		pass
		# TODO implement this rest

		if clef.lower() == "treble":
			treble_notes.append([getWaveformOfSilence(qbt)])
			treble_notes.append([getWaveformOfSilence(qbt)])
			treble_notes.append([getWaveformOfSilence(qbt)])
			treble_notes.append([getWaveformOfSilence(qbt)])
		else:  # bass
			bass_notes.append([getWaveformOfSilence(qbt)])
			bass_notes.append([getWaveformOfSilence(qbt)])
			bass_notes.append([getWaveformOfSilence(qbt)])
			bass_notes.append([getWaveformOfSilence(qbt)])

	elif line.replace(' ', '') == '':
		pass

	elif line[:4].lower() == "line":
		pass
	else:  # This is a set of notes
		notes = line.replace(' ', '').split(',')

		freqs = [getFreq(x) for x in notes]
		if clef.lower() == "treble":
			print ("tr")
		print (freqs)

		waveforms = [getWaveformOfNote(x, qbt) for x in freqs]

		if clef.lower() == "treble":
			treble_notes.append(waveforms)
		else:  # bass
			bass_notes.append(waveforms)

for i in range(len(bass_notes)):
	bass_notes[i] #sum of waveforms in this index
	treble_notes[i] #sum of waveforms in this index
	#add them together
	#put it in combined_clef[i]

	if is_rest(bass_notes[i]):
		col = sum(treble_notes[i])
	elif is_rest(treble_notes[i]):
		col = sum(bass_notes[i])
	else:
		col = sum(bass_notes[i]) + sum(treble_notes[i]) #waveform that plays an entire column of notes

	try:
		playWaveform(col)
	except:
		print("Error note problem ahhhh!")