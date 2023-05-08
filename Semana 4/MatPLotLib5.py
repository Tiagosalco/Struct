import matplotlib.pyplot as plt
import numpy as np

time=np.arange(0,100,0.5) #de 0 a 100 de a 0,5 = [0.5,1,1.5,2,2.5,...
print(time)
amp=np.sin(time)

plt.plot(time,amp,color='violet')
plt.title(label='senial',loc='right',rotation=45)

plt.show()