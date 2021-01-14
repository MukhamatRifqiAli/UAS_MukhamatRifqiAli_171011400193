#!/usr/bin/env python
# coding: utf-8

# # <font color = "green">Python : Tugas UAS Kecerdasan Buatan Image Processing </font>

# ## <font color = "red"> Metode Pertama</font>
# ## <font color = "blue"> Menggunakan Pillow (PIL)  Modul</font>

# In[6]:


# importing PIL Module
from PIL import Image

# Read image
img = Image.open('./MukhamatRifqiAli.jpg')

# Display image
img.show()


# ## <font color = "red"> Metode Ke dua</font>
# ## <font color = "blue"> Menggunakan Pillow (PIL) Dengan matplotlib Modul</font>

# In[5]:


from PIL import Image
import matplotlib.pyplot as plt

img = Image.open('./MukhamatRifqiAli.jpg')

plt.imshow(img)
plt.show()


# ## <font color = "red"> Metode Ke Tiga</font>
# ## <font color = "blue"> Menggunakan Modul matplotlib Modul</font>
# 

# In[7]:


# importing matplotlib modules
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Read image
img = mpimg.imread('./MukhamatRifqiAli.jpg')

# Display image
plt.imshow(img)
plt.show()


# ## <font color = "red"> Metode Ke Empat</font>
# ## <font color = "blue"> Menggunakan Modul gambar dengan matplotlib</font>
# 

# In[8]:


# importing imageio module
import imageio
# importing matplotlib module
import matplotlib.pyplot as plt

# Read image
img = imageio.imread('./MukhamatRifqiAli.jpg')

plt.imshow(img)
plt.show()


# ## <font color = "red"> Metode Ke Lima</font>
# ## <font color = "blue"> Menggunakan gambar Modul OpenCV</font>
# 

# In[5]:


# importing cv2 module
import cv2 as cv
# Read image
img = cv.imread('./MukhamatRifqiAli.jpg',0)
# NB: 1 :cv.IMREAD_COLOR = to loads color image, transparancy neglected 
#0: CV.IMREAD_GRAYSCALE = to loads image in grayscale mode  
# -1: cv.IMREAD_UNCHANGED = to loads image including as such alpha channel

#Display image
cv.imshow('windowTitle',img)

# to display image until you press any key in keyboard
cv.waitKey(0)

# to destroy all windows
cv.destroyAllWindows()


# ## <font color = "red"> Metode Ke Enam</font>
# ## <font color = "blue"> Menggunakan gambar Modul OpenCV Dengan Matplotlib </font>
# 

# In[14]:


# importing cv-python (cv2) module
import cv2 as cv
import matplotlib.pyplot as plt
# Read the image in Color mode
img = cv.imread('./MukhamatRifqiAli.jpg',0) 

# Convert from BGR Color mode to RGB Color Mode
RGBimg = cv.cvtColor(img, cv.COLOR_BGR2RGB)

plt.imshow(RGBimg)


# In[ ]:




