import numpy as np

def calculate_brightness(img):
	# Write your code here
	if not(all(len(row) == len(img[0]) for row in img)):
		return -1
	img = np.array(img)
	if img.size == 0 or np.max(img)<0 or np.min(img)>255 or img.shape[0] != img.shape[1]:
		return -1
	return np.mean(img)
