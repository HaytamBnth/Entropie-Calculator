#!/bin/python3

from PIL import Image
import math

def cal_prob_img(image):
	
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
	
	tot_coul = 0
	for v in mon_dict.values():
		tot_coul += v
	print(mon_dict)
	for k,v in mon_dict.items():
		P_couleur.append(v/tot_coul)
	
	
	
	for p in P_couleur :
		H += -(p*math.log2(p))
	
	return H

image = input(f'entrer votre image: ')
H = cal_prob_img(image)
print(f'\n\n -----> l entropie de votre image est: {H}')
