#!/usr/bin/env python
# coding: utf-8

# In[18]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from time_series import write_file

output_result_file = write_file()

# #importing CSV data file
# #no of rows to skip at top
n= 5

# #replace path of data file 
t1=pd.read_csv(output_result_file,skiprows=n,usecols=[0])

acc1=pd.read_csv(output_result_file,skiprows=n,usecols=[1])



# #dt is time increment in every data
# #dt=0.01 means it takes 100 data in a second
dt1=0.01


# #calculating length of data
n1 = len(acc1)


# #computing frequency using scipy fftpack
freq1 = np.fft.fftfreq(n1, d=dt1)



# # Fast Fourier Transform of Acceleration
accfft1 = np.array(np.fft.fft(acc1, axis=0))


# #computing absolute value of fft
Accfft1=np.abs(accfft1)*dt1


# #plotting the spectral
plt.loglog(freq1,Accfft1,label="EW",lw=0.3, color='r')


plt.xlabel('Frequency, Hz')
plt.ylabel(' Amplitude cm/s^2')
plt.grid()
plt.title("Amplitude vs Frequency-EW")
plt.legend()


print(plt,'plt is ---->')










