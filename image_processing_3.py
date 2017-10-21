import scipy
import scipy.ndimage 
import numpy as np 
import matplotlib.pyplot as plt 

def edge_detect_sobel(image, rotation, sigma):
	image = scipy.ndimage.rotate(image, rotation, mode = 'constant')
	image = scipy.ndimage.gaussian_filter(image, sigma)
	feature_x = scipy.ndimage.sobel(image, axis = 0, mode = 'constant')
	feature_y = scipy.ndimage.sobel(image, axis = 1, mode = 'constant')
	feature_total = np.hypot(feature_x, feature_y)
	return image, feature_x, feature_y, feature_total


def run():
	im  = scipy.misc.imread("dog_jumping.jpg", flatten = True)
	im, f_x, f_y, f_total = edge_detect_sobel(im, 15, 0.25)
	plt.imshow(im)
	plt.show()
	plt.imshow(f_x)
	plt.show()
	plt.imshow(f_y)
	plt.show()
	plt.imshow(f_total)
	plt.show()


if __name__ == '__main__':
	 run()    



