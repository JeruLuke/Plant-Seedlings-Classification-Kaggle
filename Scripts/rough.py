# snippet to get number of images and avaerage size of images in each folder 
import os 
import cv2 
import numpy as np
 
#src = '/home/ubuntu/Kaggle/Plant/Data/train/' 
src = '/home/ubuntu/Kaggle/Plant/Data/aug_500/' 

folder_count = 0 
file_count = 0 

count = 0
for folder in os.listdir(src): 
    print (folder )
    count = 0
    list_dir = src + folder + '/'
    height = []
    width = []
#    print(list_dir)
    for f in os.listdir(list_dir):
#      print (f)
     
      if f.endswith('.png'): # eg: '.txt'
         count += 1
         img = cv2.imread(list_dir + f, 0)
         height.append(img.shape[0])
         width.append(img.shape[1])

    print ('Number of images : ', count)
    print ('Average height : ', np.mean(height), ' &  Average width : ', np.mean(width))
'''   
    if os.path.isdir(src + folder): 
#        print 'True' 
        folder_count+=1 
        print folder_count 
        contents = os.listdir(os.path.join(src, name))  
        file_count = 0 
        for f in contents: 
            if f.endswith('.png'): 
                file_count+=1 
        print file_count 
'''
