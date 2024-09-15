# -*- coding: utf-8 -*-
"""MyFirstColabNotebook

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11rhFjT0Y1PLsZ54w652efTDCmCciuQYq

## **Owen Randolph, Week 1 Coding Practice Submission, DSCI-D590 Applied Data Science 9998**
"""

time.sleep(5)
print (time.ctime())

import time
print(time.ctime())

"""This is **bold**.
This is *italic*.
This is ~strikethrough~.

$\sqrt{3x-1}+(1+x)^2$

$e^x = \sum_{i = 0}^\infty \frac{1}{i!}x^i$
"""

message = 'A Great Tutorial on Colab by Tutorialspoint!'
greeting = !echo -e "$message\n$message"
greeting

!pwd

# /content is the default location in your Colab session

!wget https://archive.ics.uci.edu/static/public/2/adult.zip -P "/content"

!ls

!unzip "/content/adult.zip"

import pandas as pd
data = pd.read_csv("/content/adult.data")
data.head(5)

from google.colab import files
uploaded = files.upload()

data = pd.read_csv("/content/stocks.csv")
data.head(5)

from google.colab import drive
drive.mount('/content/drive')

!git clone https://github.com/wxs/keras-mnist-tutorial.git

!ls /bin

from google.colab import drive
drive.mount("/content/drive")

!ls "/content/drive/My Drive/Colab Notebooks"

import numpy as np
from matplotlib import pyplot as plt

y = np.random.randn(100)
x = [x for x in range(len(y))]

plt.plot(x, y, '-')
plt.fill_between(x, y, 200, where = (y > 195), facecolor='g', alpha=0.6)

plt.title("Sample Plot")
plt.show()

# Commented out IPython magic to ensure Python compatibility.
# %ldir

# Commented out IPython magic to ensure Python compatibility.
# %history

# Commented out IPython magic to ensure Python compatibility.
# %%html
# <marquee style='width: 50%; color: Green;'>Welcome to Tutorialspoint!</marquee>

# Commented out IPython magic to ensure Python compatibility.
# %%html
# <svg xmlns="https://www.w3.org/2000/svg" viewBox="0 0 600 400" width="400" height="400">
#    <rect x="10" y="00" width="300" height="100" rx="0" style="fill:orange; stroke:black; fill-opacity:1.0" />
#    <rect x="10" y="100" width="300" height="100" rx="0" style="fill:white; stroke:black; fill-opacity:1.0;" />
#    <rect x="10" y="200" width="300" height="100" rx="0" style="fill:green; stroke:black; fill-opacity:1.0;" />
# </svg>

# Commented out IPython magic to ensure Python compatibility.
# %lsmagic

import tensorflow as tf
mnist = tf.keras.datasets.mnist
print("Data is being loaded")

tf.test.gpu_device_name()

from tensorflow.python.client import device_lib
device_lib.list_local_devices()

!cat /proc/meminfo