from scipy import misc
import numpy as np
import os
from scipy.misc import imsave
import cv2
import time
#************************************INPUT_FOLDER*************************************************
folder='testing'
#*************************************NOISE_INTENSITY**********************************************
intensity=2

list = os.listdir(folder) # dir is your directory path
number_files = len(list)
#print(number_files)
d = 0

print('Starting Conversion')
time.sleep(3)
for file in os.listdir(folder):
    outfile = 'noise/file_%d.jpg' % d
    image = misc.imread(os.path.join(folder, file), mode="L")
    noisy1 = image + 3 * image.std() * np.random.random(image.shape)
    alot = intensity * image.max() * np.random.random(image.shape)
    noisy2 = image + alot
    imsave(outfile, noisy2)
    d += 1
    percentage=(d/number_files)*100
    print(percentage)
    if percentage >= 100 :
        print('Conversion Done!')
        print('Thresholding....')
#************************************INPUT_NOISE_FOLDER**********************************************
time.sleep(3)
there='noise'

list = os.listdir(there)
d=0
for file in os.listdir(there):

    threshold = 'noise1/file_%d.jpg' % d    # output directory

    d += 1
    img = cv2.imread(os.path.join(there, file),0)
    img = cv2.medianBlur(img, 5)
    ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

    cv2.imwrite(threshold, th1)

    percentage = (d / number_files) * 100
    print(percentage)
    if percentage >= 100:
        print('Thresholding Done!')
        
 #****************************************************End**********************************************




















