from PIL import Image
import numpy as np
import cv2
import os

def make_square(im, min_size=256, fill_color=(0, 0, 0)):
    x, y = im.size
    size = max(min_size, x, y)
    new_im = Image.new('RGB', (size, size), fill_color)
    new_im.paste(im, (int((size - x) / 2), int((size - y) / 2)))
    return new_im

def resize_image(image,im_name,im_size):
	im = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
	im = cv2.resize(im,(im_size,im_size))
	cv2.imwrite(os.path.join(destination+im_name),im)

destination = "resized_reshaped_images"
im_name = "test2.jpg"

reshaped_im = make_square(Image.open(im_name))
reshaped_im = np.array(reshaped_im)
resize_image(reshaped_im,im_name,224)
