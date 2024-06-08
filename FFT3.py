#!/usr/bin/env python
# coding: utf-8

# In[18]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

##importing CSV data file
##no of rows to skip at top
n= 5

##replace path of data file 
t1=pd.read_csv('GorkhaEQ_EW.csv',skiprows=n,usecols=[0])
t2=pd.read_csv('DhadingEQ_EW.csv',skiprows=n,usecols=[0])
t3=pd.read_csv('JajarkotEQ_EW.csv',skiprows=n,usecols=[0])
acc1=pd.read_csv('GorkhaEQ_EW.csv',skiprows=n,usecols=[1])
acc2=pd.read_csv('DhadingEQ_EW.csv',skiprows=n,usecols=[1])
acc3=pd.read_csv('JajarkotEQ_EW.csv',skiprows=n,usecols=[1])

##dt is time increment in every data
##dt=0.01 means it takes 100 data in a second
dt1=0.01
dt2=0.01
dt3=0.01

##calculating length of data
n1 = len(acc1)
n2 = len(acc2)
n3 = len(acc3)

##computing frequency using scipy fftpack
freq1 = np.fft.fftfreq(n1, d=dt1)
freq2 = np.fft.fftfreq(n2, d=dt2)
freq3 = np.fft.fftfreq(n3, d=dt3)


## Fast Fourier Transform of Acceleration
accfft1 = np.array(np.fft.fft(acc1, axis=0))
accfft2 = np.array(np.fft.fft(acc2, axis=0))
accfft3 = np.array(np.fft.fft(acc3, axis=0))

##computing absolute value of fft
Accfft1=np.abs(accfft1)*dt1
Accfft2=np.abs(accfft2)*dt2
Accfft3=np.abs(accfft3)*dt3

##plotting the spectral
plt.loglog(freq1,Accfft1,label="Gorkha",lw=0.3, color='r')
plt.loglog(freq2,Accfft2,label="Dhading",lw=0.3, color='b')
plt.loglog(freq3,Accfft3,label="Jajarkot",lw=0.3, color='g')

plt.xlabel('Frequency, Hz')
plt.ylabel(' Amplitude cm/s^2')
plt.grid()
plt.title("Amplitude vs Frequency-EW")
plt.legend()




# In[19]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

##importing CSV data file
##no of rows to skip at top
n= 5

##replace path of data file 
t1=pd.read_csv('GorkhaEQ_NS.csv',skiprows=n,usecols=[0])
t2=pd.read_csv('DhadingEQ_NS.csv',skiprows=n,usecols=[0])
t3=pd.read_csv('JajarkotEQ_NS.csv',skiprows=n,usecols=[0])
acc1=pd.read_csv('GorkhaEQ_NS.csv',skiprows=n,usecols=[1])
acc2=pd.read_csv('DhadingEQ_NS.csv',skiprows=n,usecols=[1])
acc3=pd.read_csv('JajarkotEQ_NS.csv',skiprows=n,usecols=[1])

##dt is time increment in every data
##dt=0.01 means it takes 100 data in a second
dt1=0.01
dt2=0.01
dt3=0.01

##calculating length of data
n1 = len(acc1)
n2 = len(acc2)
n3 = len(acc3)

##computing frequency using scipy fftpack
freq1 = np.fft.fftfreq(n1, d=dt1)
freq2 = np.fft.fftfreq(n2, d=dt2)
freq3 = np.fft.fftfreq(n3, d=dt3)


## Fast Fourier Transform of Acceleration
accfft1 = np.array(np.fft.fft(acc1, axis=0))
accfft2 = np.array(np.fft.fft(acc2, axis=0))
accfft3 = np.array(np.fft.fft(acc3, axis=0))

##computing absolute value of fft
Accfft1=np.abs(accfft1)*dt1
Accfft2=np.abs(accfft2)*dt2
Accfft3=np.abs(accfft3)*dt3

##plotting the spectral
plt.loglog(freq1,Accfft1,label="Gorkha",lw=0.3, color='r')
plt.loglog(freq2,Accfft2,label="Dhading",lw=0.3, color='b')
plt.loglog(freq3,Accfft3,label="Jajarkot",lw=0.3, color='g')

plt.xlabel('Frequency, Hz')
plt.ylabel(' Amplitude cm/s^2')
plt.grid()
plt.title("Amplitude vs Frequency-NS")
plt.legend()




# In[20]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

##importing CSV data file
##no of rows to skip at top
n= 5

##replace path of data file 
t1=pd.read_csv('GorkhaEQ_UD.csv',skiprows=n,usecols=[0])
t2=pd.read_csv('DhadingEQ_UD.csv',skiprows=n,usecols=[0])
t3=pd.read_csv('JajarkotEQ_UD.csv',skiprows=n,usecols=[0])
acc1=pd.read_csv('GorkhaEQ_UD.csv',skiprows=n,usecols=[1])
acc2=pd.read_csv('DhadingEQ_UD.csv',skiprows=n,usecols=[1])
acc3=pd.read_csv('JajarkotEQ_UD.csv',skiprows=n,usecols=[1])

##dt is time increment in every data
##dt=0.01 means it takes 100 data in a second
dt1=0.01
dt2=0.01
dt3=0.01

##calculating length of data
n1 = len(acc1)
n2 = len(acc2)
n3 = len(acc3)

##computing frequency using scipy fftpack
freq1 = np.fft.fftfreq(n1, d=dt1)
freq2 = np.fft.fftfreq(n2, d=dt2)
freq3 = np.fft.fftfreq(n3, d=dt3)


## Fast Fourier Transform of Acceleration
accfft1 = np.array(np.fft.fft(acc1, axis=0))
accfft2 = np.array(np.fft.fft(acc2, axis=0))
accfft3 = np.array(np.fft.fft(acc3, axis=0))

##computing absolute value of fft
Accfft1=np.abs(accfft1)*dt1
Accfft2=np.abs(accfft2)*dt2
Accfft3=np.abs(accfft3)*dt3

##plotting the spectral
plt.loglog(freq1,Accfft1,label="Gorkha",lw=0.3, color='r')
plt.loglog(freq2,Accfft2,label="Dhading",lw=0.3, color='b')
plt.loglog(freq3,Accfft3,label="Jajarkot",lw=0.3, color='g')

plt.xlabel('Frequency, Hz')
plt.ylabel(' Amplitude cm/s^2')
plt.grid()
plt.title("Amplitude vs Frequency-UD")
plt.legend()




# In[21]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

##importing CSV data file
##no of rows to skip at top
n= 6

##replace path of data file 
#TIME PERIOD DATA FROM EXCEL SHEET
t1=pd.read_csv('EQ_DATA.csv',skiprows=n,usecols=[4])
t2=pd.read_csv('EQ_DATA.csv',skiprows=n,usecols=[6])
t3=pd.read_csv('EQ_DATA.csv',skiprows=n,usecols=[13])
#ACCELERATION DATA FROM EXCEL SHEET
acc1=pd.read_csv('EQ_DATA.csv',skiprows=n,usecols=[5])
acc2=pd.read_csv('EQ_DATA.csv',skiprows=n,usecols=[12])
acc3=pd.read_csv('EQ_DATA.csv',skiprows=n,usecols=[19])

##dt is time increment in every data
##dt=0.01 means it takes 100 data in a second
dt1=0.01
dt2=0.01
dt3=0.01

##calculating length of data
n1 = len(acc1)
n2 = len(acc2)
n3 = len(acc3)

##computing frequency using scipy fftpack
freq1 = np.fft.fftfreq(n1, d=dt1)
freq2 = np.fft.fftfreq(n2, d=dt2)
freq3 = np.fft.fftfreq(n3, d=dt3)


## Fast Fourier Transform of Acceleration
accfft1 = np.array(np.fft.fft(acc1, axis=0))
accfft2 = np.array(np.fft.fft(acc2, axis=0))
accfft3 = np.array(np.fft.fft(acc3, axis=0))

##computing absolute value of fft
Accfft1=np.abs(accfft1)*dt1
Accfft2=np.abs(accfft2)*dt2
Accfft3=np.abs(accfft3)*dt3

##plotting the spectral
plt.loglog(freq1,Accfft1,label="Gorkha",lw=0.3, color='r')
plt.loglog(freq2,Accfft2,label="Dhading",lw=0.3, color='b')
plt.loglog(freq3,Accfft3,label="Jajarkot",lw=0.3, color='g')

plt.xlabel('frequency, Hz')
plt.ylabel(' Amplitude cm/s^2')
plt.grid()
plt.title("Amplitude vs Frequency-EW")
plt.legend()




# In[ ]:




