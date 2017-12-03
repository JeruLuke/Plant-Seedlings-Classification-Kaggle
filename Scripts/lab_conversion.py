import os
import cv2

src = '/home/ubuntu/Kaggle/Plant/Data/resized_350_train/'
dest = '/home/ubuntu/Kaggle/Plant/Data/train_350_a_channel/'

for name in os.listdir(src):
    print (name    )


    if os.path.isdir(src + name):
        #print 'True'
        if not os.path.exists(dest + name):
            os.makedirs(dest + name)
            #print (name)
            contents = os.listdir(os.path.join(src, name)) 
            #print contents
            count = 0
            for f in contents:
                if f.endswith('.png'):
                    img = cv2.imread(src + name + '/' + f, 1)
                    lab= cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
                    l, a, b = cv2.split(lab)
                    cv2.imwrite(dest + name + '/' + f, a)
                    count+=1
            #print count)
