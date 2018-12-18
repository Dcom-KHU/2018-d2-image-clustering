import os
import re
import glob
import numpy as np
import PIL.Image as img

def img_array(path):
    image = img.open(path)
    tmp = np.array(image)
    image.close()
    return tmp

re_model = re.compile("^(\d+)_")
  
train = glob.glob('data/train/*.jpg')
train_X = np.array([np.array(img.open(fname).resize((300, 300), img.ANTIALIAS)) for fname in train])
train_Y = np.array([os.path.split(fname)[1].split('_')[0] for fname in train])
print('train finished')

test = glob.glob('data/test/*.jpg')
test_X = np.array([np.array(img.open(fname).resize((300, 300), img.ANTIALIAS)) for fname in test])
test_Y = np.array([os.path.split(fname)[1].split('_')[0] for fname in test])
print('test finished')
