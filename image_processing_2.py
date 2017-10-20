import scipy
import scipy.ndimage
import numpy as np 
from PIL import Image
from scipy import misc

# IMPORT IMAGE
a = scipy.misc.imread("royal_tiger.jpeg", flatten = True)

# FUNCTION TO CONVERT NDARRY TO IMAGE
def image_show(image):

	image = Image.fromarray(np.uint8(image))
	return image.show()

# FUNCTION TO ADD RANDOM NOISE
def add_noise(image):

	noise =  image.std() * np.random.random(image.shape)
	noisy_image = image + noise 
	return noisy_image

# FUNCTION FOR DENOISING NOISY IMAGE USING GAUSSIAN FILTER
def denoise_image(image, sigma):

	denoised_image = scipy.ndimage.gaussian_filter(image, sigma)
	return denoised_image

# FUNCTION FOR DENOISING NOISY IMAGE USING MEDIAN FILTER
def denoise_with_median_filter(image, param):

	denoise_median = scipy.ndimage.median_filter(image, param)
	return denoise_median


def run():
	noisy_image = add_noise(a)
	denoised_image = denoise_image(noisy_image, 2) 
	denoise_median = denoise_with_median_filter(noisy_image, param = 3)
	image_show(a)
	image_show(noisy_image)
	image_show(denoised_image)
	image_show(denoise_median)


	
if __name__ == '__main__':
	 run()
