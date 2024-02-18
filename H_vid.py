#!/bin/python3

import cv2
import librosa
import numpy as np
from PIL import Image
import math
from moviepy.editor import VideoFileClip

def somme_rvb(img):
	
	#initialisation
	H=0
	mon_dict = {}
	ls = list()
	P_couleur = list()
	
	#ouvrir l'image
	img = Image.open(image)
	
	largeur, hauteur = img.size
	
	#mettre les valeurs RVB dans une liste 
	tot_coul = hauteur*largeur
	
	for i in range(hauteur):
		for j in range(largeur):
			pixel = img.getpixel((j, i)) 
			ls.append(pixel)
	
	for i in ls:
		mon_dict[i] = mon_dict.get(i, 0)+1
	
	return mon_dict

def somme_audio(audio):
	#***-initialisation***#
	card = 0	      #
	somme_amp = {}	      #
	#*********************#
	
	# calcul les valeurs d'amplitude
	compt_amp = np.histogram(audio, bins=256)[0]
    

	

	# transferer les amplitudes en dict
	for amplitude, compt in enumerate(compt_amp):
		somme_amp[amplitude] = compt
	
	
	#calcul des somme d'amplitude
	for k,v in somme_amp.items():
		card += v
	
	
	return  card, somme_amp


# fonction calcul entropie
def calcul_H_vid(chemin):
	
	
	#ouvrir la video
	cap = cv2.VideoCapture(chemin)
	
	#******initialisation******#
	tot_rvb = [0,0,0]	   #
	pix_tot = 0		   #
	tot_card = 0		   #
	tot_amp_somme = {}	   #
	H_audio = 0		   #
	P_audio = {}		   #
	mon_dict = {}
	#**************************#
	
	#ouvrir la video pour le traitement audio
	video_clip = VideoFileClip(chemin)
	audio = video_clip.audio
	
	while True:
		ret, frame = cap.read()
		if not ret:
			break
			
	# convertir le frame en image
		pil_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

	# Calcul des bits RVB dans la video
		mon_dict = somme_rvb(pil_image)
		for k,v in mon_dict.items():
			tot_dict[k] = tot_dict.get(k, 0)+v
		

	# calcul audio
	if audio is not None:
		fps = video_clip.fps
		y = np.array(audio.to_soundarray(fps=fps)[:, 0]) # on l'utilise en une chaine
		card, amp_somme = somme_audio(y)
		tot_card += card

	for k, v in amp_somme.items():
		tot_amp_somme[k] = tot_amp_somme.get(k, 0) + v

	# équivalent de close()
	cap.release()

	#calcul des probabilités RVB
	Pr = tot_rvb[0] / pix_tot
	Pv = tot_rvb[1] / pix_tot
	Pb = tot_rvb[2] / pix_tot
	
	#entropie RVB
	H_rvb = -(Pr * math.log2(Pr)) - (Pv * math.log2(Pv)) - (Pb * math.log2(Pb))

	
	#calcul d'entropie audio
	for k, v in tot_amp_somme.items():
		P_audio[k] = v / tot_card
		if P_audio[k] != 0:
			H_audio += -(P_audio[k] * math.log2(P_audio[k]))
	
	#entropie total
	H_total = H_rvb + H_audio

	return H_total, H_rvb, H_audio


