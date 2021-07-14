'''
Created on 13 Jul 2021

@author: pandorasainz
citations: 
1- https://stackoverflow.com/questions/8863917/importerror-no-module-named-pil #to import pillow
2- https://stackoverflow.com/questions/67209502/import-requests-modulenotfounderror-no-module-named-requests # to import requests
'''
from PIL import Image, ImageFilter, ImageDraw, ImageFont
import os, sys
import requests
from io import BytesIO
from image_functions import *



if __name__ == '__main__':
    # open an image file. The default path is where this python module is
    '''
    im = Image.open("SiriusAndViolet.jpg")
    print(im.width, im.height, im.mode, im.format)  # Display some info about the image
    '''
    
    # Load and Show Image
    '''
    my_image = load_image("SiriusAndViolet.jpg")
    if my_image != None:
        my_image.show(my_image)
    else: 
        print('unable to open the file.')
    '''
        
    #crop Image
    '''
    im = Image.open("SiriusAndViolet.jpg")  
    im_c = im.crop((200,300,400,500)) # (left, top, right, bottom) it's a tuple!
    im_c.show()
    '''
    
    #blur image
    '''
    my_image = blur_image(load_image("SiriusAndViolet.jpg"))
    my_image.show()
    '''
    
    
    
    
    
    
    
    
    