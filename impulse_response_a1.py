import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

num = np.poly1d([1,0])
den = np.poly1d([1,3,2,1])
sys = signal.TransferFunction(num,den)
t,y = signal.impulse(sys)
plt.plot(t,y)
plt.xlabel('$t$')
plt.ylabel('$y$')
plt.grid() # minor
plt.axis()
plt.show()
