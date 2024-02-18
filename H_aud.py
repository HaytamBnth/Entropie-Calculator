#!/bin/python3

import librosa
import numpy as np
import math

def somme_audio(audio):
	#***-initialisation***#
	tot = 0	      	      #
	somme_amp = {}	      #
	H = 0		      #
	#*********************#
	
	# calcul les valeurs d'amplitude
	compt_amp = np.histogram(audio, bins=256)[0]
    

	

	# transferer les amplitudes en dict
	for amplitude, compt in enumerate(compt_amp):
		somme_amp[amplitude] = compt
	
	
	#calcul des somme d'amplitude
	
	
	for k,v in somme_amp.items():
		somme_amp[k] = somme_amp.get(k, 0) + v
		tot += v
	print(somme_amp)
	P ={}
	for k, v in somme_amp.items():
		P[k] = v/tot
	
	for k,v in P.items():
		if v > 0:
			H += -(v*math.log2(v))
	
	return  H

chemin = input('entrez votre audio: ')
y, sr = librosa.load(chemin, sr=None)
H = somme_audio(y)
print(f"l'entropie de votre audio est: {H}")
