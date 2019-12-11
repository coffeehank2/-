import matplotlib.pyplot as plt
import numpy as np

t=np.linspace(-0.01, 0.02, 200)
x=np.cos(2*np.pi*100*t)
plt.subplot(3,1,1); plt.plot(t,x)

t=np.linspace(-0.01, 0.02, 61)
x=np.cos(2*np.pi*100*t)
plt.subplot(3,1,2); plt.stem(t,x,'filled')

t=np.linspace(-0.01, 0.02, 200)
x=np.cos(2*np.pi*100*t)
plt.subplot(3,1,3)
plt.plot(t,x,':')
t=np.linspace(-0.01, 0.02, 16)
x=np.cos(2*np.pi*100*t)
plt.stem(t,x,'filled')
