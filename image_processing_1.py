# IMPORT LIBRARIES
import scipy
import scipy.ndimage
import matplotlib.pyplot as plt 
import numpy as np 
from PIL import Image, ImageFilter
import os

# IMPORT IMAGE
a = scipy.ndimage.imread("dhoni.jpg")

#FUCTION FOR IMAGE TRANSFORMATION
def image_transformations(image, action):

	if (action == 'crop'):
		cropped_img = image[image.shape[0]/2:(image.shape[0]/2 + 300), image.shape[1]/2 : (image.shape[1]/2) + 300, :]
		return cropped_img

	elif (action == 'up_down'):
		up_down_img = np.flipud(image) 
		return up_down_img

	elif (action == 'rotate_with_reshape'):
		rotated_reshaped = scipy.ndimage.rotate(image, 45, reshape = True)
		return rotated_reshaped

	elif (action == 'rotate_without_reshape'):
		rotated_wo_reshaped = scipy.ndimage.rotate(image, 45, reshape = False) 
		return rotated_wo_reshaped       


# FUNCTION FOR IMAGE FILTERING
def image_filtering(image, filter_method, param):

	if (filter_method == 'gaussian'):
		if (param > 10):
			print("very blurred")
		blurred_gaussian = scipy.ndimage.gaussian_filter(image, sigma = param)
		return blurred_gaussian
			
	if (filter_method == 'uniform'):
		blurred_uniform = scipy.ndimage.uniform_filter(image, size = param)
		return blurred_uniform
		

# FUNCTION FOR IMAGE SHARPENING
def image_sharpening(image, alpha):
 	image_blurred = image_filtering(a, filter_method = 'gaussian', param = 4)
	image_blurred_f = image_filtering(image_blurred, filter_method = 'gaussian', param = 2)
	sharpened_image = (image_blurred + alpha* (image_blurred - image_blurred_f))
	return sharpened_image 


# OUTPUT OF ALL FUNCTIONS
t_c = image_transformations(a, action = 'crop')
t_c = Image.fromarray(t_c)
print t_c.show()

t_ud = image_transformations(a, action = 'up_down')
t_ud = Image.fromarray(t_ud)
print t_ud.show()

t_r = image_transformations(a, action = 'rotate_with_reshape')
t_r = Image.fromarray(t_r)
print t_r.show()

t_wo_r = image_transformations(a, action = 'rotate_with_reshape')
t_wo_r = Image.fromarray(t_wo_r)
print t_wo_r.show()

f = image_filtering(a, filter_method ='uniform',  param = 10)   
f = Image.fromarray(f)
print f.show()

s = image_sharpening(a, 4)
s = Image.fromarray(s)
print s.show()







