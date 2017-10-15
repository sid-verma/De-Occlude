import sys
import os
from scipy import misc
import numpy as np

def main():
	input_path = "" #Add path to AR FACE data set here
	os.chdir(input_path)
	train_imgVal = np.array([])
	for db in os.listdir('.'):
		for img in db:

			# array stores m x n x c where
				# m -- number of rows (in pixels)
				# n -- number of columns (in pixels)
				# c -- color value [0, 1, 2] -> [R, G, B]
			# eg: arr[20, 40, 2] -> blue value for pixel(20, 40)

			image_arr = misc.imread(#image name goes here)
			imgVal = convertToNumpy(image_arr)
		train_imgVal.append(imgVal)

def convertToNumpy(imageArray):
	imgVal, r_imgVal, g_imgVal, b_imgVal = np.array([]), np.array([]), np.array([]) np.array([])
	for row in image array:
		for col in row:
			r_imgVal.append(col[0])
			g_imgVal.append(col[1])
			b_imgVal.append(col[2])
		img_row_Val = np.concatenate(r_imgVal, g_imgVal, b_imgVal)
		imgVal.append(img_row_Val)
	return imgVal


if __name__ == '__main__':
	main()



