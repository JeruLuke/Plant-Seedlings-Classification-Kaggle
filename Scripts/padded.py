import cv2
import os
import numpy as np

 

src = 'C:/Users/selwyn77/Desktop/New Folder/'
dest = 'C:/Users/selwyn77/Desktop/padded/'

pad_size = 512 

for folder in os.listdir(src): 
    print (folder)
    
    if os.path.isdir(src + folder):
        print ('True')
        
        if not os.path.exists(dest + folder):
            os.makedirs(dest + folder)
            
            contents = os.listdir(os.path.join(src, folder)) 
            ll = os.path.join(src, folder)
            print(contents)
            #file_count = 0
            if os.path.isdir(src + folder):        
                for f in contents:
                    if f.endswith ('.png'):
                
                        print (f)
                
                        img = cv2.imread(os.path.join(ll, f))
                        print(img.shape)
                        h, w, _ = img.shape
                        if (h > w):
                            img = cv2.resize(img, (w, w))
                        elif (w < h):
                            img = cv2.resize(img, (h, h))
                        else:
                            img = img
                        
                        if (img.shape[0] > pad_size):
                            img = cv2.resize(img, (pad_size, pad_size))
                            cv2.imwrite(dest + folder + '/' + f, img)
                        else:
                            width_diff = pad_size - w
                            height_diff = pad_size - h
                            
                            left = width_diff/2
                            right = width_diff - left
                            top = height_diff/2
                            bottom = height_diff - top
                            
                            black_pixels = [0, 0, 0]
                
                            padded_img = cv2.copyMakeBorder(img, top, left, right, bottom, cv2.BORDER_CONSTANT, value = black_pixels)
#                            padded_img = cv2.copyMakeBorder(img, top, left, right, bottom, cv2.BORDER_REPLICATE)
                            
                            cv2.imwrite(dest + folder + '/' + f, padded_img)


            
            
        
