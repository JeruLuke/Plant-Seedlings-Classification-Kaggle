src = '/home/ubuntu/Kaggle/Plant/Data/augmented_350/'
dest = '/home/ubuntu/Kaggle/Plant/Data/aug_500/'

import random
import os
import shutil
import numpy as np
import cv2
#print len(os.walk('dir_name').next()[1])

files = folders = j = 0

for j, dirnames, filenames in os.walk(src):
  
    #files += len(filenames)
    #folders += len(dirnames)
#    j += len(j)
    print (j)
    f = j.rsplit('/', 1)[1]


    if not os.path.exists(dest + f):
        os.makedirs(dest + f)
        
        files = os.listdir(src + f)
        for i in range(0, 500):
            if files[i].endswith('.png'):
                shutil.copy(src + f + '/' + files[i], dest + f + '/' + files[i])
