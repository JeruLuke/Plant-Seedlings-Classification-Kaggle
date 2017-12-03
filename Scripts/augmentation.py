#-- snippet to augment images rotation, flipping and flip+rotation

import cv2
import os

src = '/home/ubuntu/Kaggle/Plant/Data/resized_350_train/'
dest = '/home/ubuntu/Kaggle/Plant/Data/augmented_350/' 

for name in os.listdir(src):
    print ( name)
    if os.path.isdir(src + name):
        #print 'True'
        if not os.path.exists(dest + name):
            os.makedirs(dest + name)
        #print name
            contents = os.listdir(os.path.join(src, name)) 
            #print contents
            count = 0
            for f in contents:
                if f.endswith('.png'):
                    img = cv2.imread(src + name + '/' + f, 1)
                    
                    #--- flipping ---
                    cv2.imwrite(dest + name + '/v_flip_' + f, cv2.flip(img, 1))
                    cv2.imwrite(dest + name + '/h_flip_' + f, cv2.flip(img, 0))
                    
                    #--- rotation ---
                    rows, cols, _ = img.shape
                    for ang in [0, 90, 180, 270]:
           #             print ang
                        M = cv2.getRotationMatrix2D((cols/2,rows/2), ang, 1)
                        dst = cv2.warpAffine(img, M, (cols, rows))
                        cv2.imwrite(dest + name + '/' + str(ang) + '_' + f, dst)
                    
                    for ang in [90, 270]:
          #              print ang
                        M = cv2.getRotationMatrix2D((cols/2,rows/2), ang, 1)
                        dst1 = cv2.warpAffine(cv2.flip(img, 1), M, (cols, rows))
                        dst2 = cv2.warpAffine(cv2.flip(img, 0), M, (cols, rows))
                        cv2.imwrite(dest + name + '/' + 'v_flip_' + str(ang) + '_' + f, dst1)
                        cv2.imwrite(dest + name + '/' + 'h_flip_' + str(ang) + '_' + f, dst2)

