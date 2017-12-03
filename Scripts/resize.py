# snippet to resize images to 350 in all the subfolders of train folder ---
import os 
import cv2 
import numpy as np
 
src = '/home/ubuntu/Kaggle/Plant/Data/train/' 
dest = '/home/ubuntu/Kaggle/Plant/Data/resized_350_train/' 

resize_var = 350

for name in os.listdir(src):
    print (name)


    if os.path.isdir(src + name):
        #print 'True'
        if not os.path.exists(dest + name):
            os.makedirs(dest + name)
        #print name
            contents = os.listdir(os.path.join(src, name)) 
            print (contents)
            count = 0
            for f in contents:
                if f.endswith('.png'):
                    img = cv2.imread(src + name + '/' + f, 1)
                    resized = cv2.resize(img, (resize_var, resize_var))
                    cv2.imwrite(dest + name + '/' + f, resized)
                    count+=1
            print (count)

'''
resize_var = 350
 
import shutil 
#print len(os.walk('dir_name').next()[1]) 

 
files = folders = j = 0 
for j, dirnames, filenames in os.walk(src): 
   
    files += len(filenames) 
    folders += len(dirnames) 
#    j += len(j) 
#    print j 
    f = j.rsplit('/', 1)[1] 

 

 
    if not os.path.exists(dest + f): 
        os.makedirs(dest + f) 
        print (f)
        files = os.listdir(src + f) 
        for fi in files: 
            if fi.endswith('.png'): 
               print (src + f + '/' + fi)               
               img = cv2.imread(src + f + '/' + fi, 1)
               resized = cv2.resize(img, (resize_var, resize_var))  
               cv2.imwrite(dest + f + fi, resized)                
# shutil.copy(src + f + '/' + files[i], dest + f + '/' + files[i]) 
'''

'''
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
