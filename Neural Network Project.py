#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Importing the necessary packages.

import numpy as np
import pandas as pd
import PIL
from PIL import Image
import glob
import keras
import tensorflow as tf
import os


# In[3]:


# identifying the root and subfolders in the image data.

directory= r"C:\Users\mesut\Desktop\UZH M.Sc. Data Science\02. Applied Business Analytics Programming Bootcamp-2\project"

train_data_root=directory+ "\images\seg_train"
test_data_root=directory+ "\images\seg_test"

#categories_train = os.listdir(directory+"\images\seg_train")
#categories_test = os.listdir(directory+"\images\seg_train")

categories_train = os.listdir(train_data_root)
categories_test=os.listdir(test_data_root)

print(categories_train)
print(categories_test)


# In[17]:


# train datadan baslayacagız, önce path train datanın

train_data=[]
train_labels=[]

# train data categorileri üzerinde iterate 
for category in categories_train:
    
    #we change the path to obtain the images.
    path= train_data_root + "\\"+ (category)
    print("CATEGORY", category)
    
    # according to image category, we append labels to label array of training  data.
    if category == "buildings":
        label = 1
    elif category == "forest":
        label= 2
    elif category == "glacier":
        label=3
    elif category == "mountain":
        label=4
    elif category=="sea":
        label=5
    elif category=="street"
        label=6
        
        for file in os.listdir(path):    
            
            # IMAGE OPERATIONS
            image=Image.open(file)
            image=image.resize((64,64), Image.ANTIALIAS)
            image.save(file)
            
            print(file)


# ### path= r'C:\Users\mesut\Desktop\UZH M.Sc. Data Science\02. Applied Business Analytics Programming Bootcamp-2\project'
# 
# dir_list = next(os.walk('.'))
# #print(dir_list)
# 
# directories=[]
# for folder, sub_folders, files in os.walk(path):
#     for s_folders in sub_folders:
#     #for subfolder in dirs:
#         print(s_folders)
#         directories.append(dirs)
#     #for name in files:
#         #if name.endswith((".html", ".htm")):
#          #   # whatever
#             

# In[ ]:


directory=r'C:\Users\mesut\Desktop\UZH M.Sc. Data Science\02. Applied Business Analytics Programming Bootcamp-2\project\images'

mylist=[]

images=[]
labels=[]



##accessing the subfolders from mail directory.
#or root, subfolders, files in os.walk(directory):
    
 #  if len(subfolders) >3:
 #      labels.append(subfolders)
 #      print(subfolders)

#rint(labels[1])
# accessing the subfolders from mail directory.
for files in os.listdir(directory):
    print(files)
    
    #f len(subfolders) >3:
    #   labels.append(subfolders)
   #    print(subfolders)
#
#rint(labels[1])  

# accessing image files via folder directory.
for image_file in os.listdir(directory+labels[0]):
    print(image_file)
    
    #for file in 
    #li=subfolders.split('\\')
    #if len(li) >3 :
     #   mylist.append(li)

    #for file in subfolders:
      #  print(file)
    


# In[ ]:


# for each image, we are reducing the size from 150x150 to 100x100.
def resizing(size):
    """This function accepts desired size """
    
# resizing training images.

for file in glob.glob('seg_train/buildings/*jpg'):
    #print(file)
    image=Image.open(file)
    image=image.resize((64,64), Image.ANTIALIAS)
    image.save(file)
    #print(image.size)
    


# In[ ]:


for file in glob.glob('seg_train/forest/*jpg'):
    #print(file)
    image=Image.open(file)
    image=image.resize((64,64), Image.ANTIALIAS)
    image.save(file)
    #print(image.size)


# In[ ]:


for file in glob.glob('seg_train/glacier/*jpg'):
    #print(file)
    image=Image.open(file)
    image=image.resize((64,64), Image.ANTIALIAS)
    image.save(file)
    #print(image.size)


# In[ ]:


for file in glob.glob('seg_train/mountain/*jpg'):
    #print(file)
    image=Image.open(file)
    image=image.resize((64,64), Image.ANTIALIAS)
    image.save(file)
    #print(image.size)


# In[ ]:


for file in glob.glob('seg_train/sea/*jpg'):
    #print(file)
    image=Image.open(file)
    image=image.resize((64,64), Image.ANTIALIAS)
    image.save(file)
    #print(image.size)


# In[ ]:


for file in glob.glob('seg_train/street/*jpg'):
    #print(file)
    image=Image.open(file)
    image=image.resize((64,64), Image.ANTIALIAS)
    image.save(file)
    #print(image.size)


# In[ ]:


# resizing the test images.
for file in glob.glob('seg_test/buildings/*jpg'):
    #print(file)
    image=Image.open(file)
    image=image.resize((64,64), Image.ANTIALIAS)
    image.save(file)
    #print(image.size)
    
for file in glob.glob('seg_test/forest/*jpg'):
    #print(file)
    image=Image.open(file)
    image=image.resize((64,64), Image.ANTIALIAS)
    image.save(file)
    #print(image.size)
    
for file in glob.glob('seg_test/glacier/*jpg'):
    #print(file)
    image=Image.open(file)
    image=image.resize((64,64), Image.ANTIALIAS)
    image.save(file)
    #print(image.size)
    
for file in glob.glob('seg_test/mountain/*jpg'):
    #print(file)
    image=Image.open(file)
    image=image.resize((64,64), Image.ANTIALIAS)
    image.save(file)
    #print(image.size)
    
for file in glob.glob('seg_test/sea/*jpg'):
    #print(file)
    image=Image.open(file)
    image=image.resize((64,64), Image.ANTIALIAS)
    image.save(file)
    #print(image.size)
    
for file in glob.glob('seg_test/street/*jpg'):
    #print(file)
    image=Image.open(file)
    image=image.resize((64,64), Image.ANTIALIAS)
    image.save(file)
    #print(image.size)


# In[ ]:




