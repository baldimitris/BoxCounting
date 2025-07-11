import sys
import numpy as np
from PIL import Image


'''
' Calculates the Fractal Dimension of a PNG image.
' The image must have dimensions 1024x1024x pixels.
' @arg img_filename the name of the PNG file to process.
' @return a float representing the image's Fractal Dimension.
'''
def Calculate_FractalDimension( img_filename ):
    img = Image.open( img_filename )
    pixels = img.load()
    img_width  = img.size[0]
    img_height = img.size[1]

    is_it_rgb = True # for supporting both RGB and monochrome images 
    if isinstance( pixels[0,0], int): is_it_rgb = False
   
    BOX_SIZES = [1,2,4,8,16,32,64,128]
    INVERSE_BOX_SIZES = []
    for i in range(0, len(BOX_SIZES)):
        INVERSE_BOX_SIZES.append( 1 / BOX_SIZES[i] )
    BOXES = {}
    for box_size in BOX_SIZES: # box_size is the box's side in pixels
        num_of_Boxes_with_content = 0
        # FOR EACH BOX
        for x in range(0, img_width, box_size):
            for y in range(0, img_height, box_size):
                # FOR EACH PIXEL IN THE BOX
                found_content_pixel = False
                for i in range(x, x+box_size):
                    if found_content_pixel: break
                    for j in range(y, y+box_size):
                        if found_content_pixel: break
                        if is_it_rgb:
                            if pixels[i,j][0] != 255:
                                found_content_pixel = True
                                num_of_Boxes_with_content += 1
                        else:
                            if pixels[i,j] != 255:
                                found_content_pixel = True
                                num_of_Boxes_with_content += 1
                           
        BOXES[ box_size ] = num_of_Boxes_with_content
   
    counts = []
    for i in range(0, len(BOXES)):
        counts.append( BOXES[ BOX_SIZES[i] ] )
    coeffs = np.polyfit(np.log10(INVERSE_BOX_SIZES), np.log10(counts), 1)
    
    return coeffs[0]



    
####################################################################################
####################################################################################    
####################################################################################    
    
if len(sys.argv) != 2:
    print("Processes a 1024x1024 PNG image with the Box Counting method and prints its Fractal Dimension.")
    print("USAGE:\tpython",  sys.argv[0], "<image filename>")
else:
    print( "The Fractal Dimension of", sys.argv[1], "is", Calculate_FractalDimension(sys.argv[1]) )
    