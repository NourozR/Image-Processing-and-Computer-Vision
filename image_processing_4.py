# IMPORT LIBRARIES
import scipy
import scipy.ndimage 
import numpy as np 
import matplotlib.pyplot as plt 

im = scipy.ndimage.imread("few_people.jpg")


def image_segmentation(image, sigma, noise_factor):
	image = scipy.ndimage.gaussian_filter(image, sigma = sigma)
	mask = (image > image.mean()).astype(np.float)
	mask = mask + 0.01 * image 
	image = mask + noise_factor * np.random.random(mask.shape)
	hist, bin_edge = np.histogram(image, bins = 50)
	bin_center = bin_edge[: -1] + bin_edge[1:]
	seg_image = image > 0.7 
	image_clean = scipy.ndimage.binary_opening(seg_image)
	return seg_image, image_clean


def run():
	img = image_segmentation(im, 0.2, 0.1)
	plt.imshow(im)
	plt.show()
	plt.imshow(img)
	plt.show()


if __name__ == '__main__':
	 run()    






