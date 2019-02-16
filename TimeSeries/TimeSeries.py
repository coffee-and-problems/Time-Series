import numpy as np
from os.path import join
import matplotlib.pyplot as plt

data = np.loadtxt(join('..', 'Data', 'time_series_data.dat'))

plt.plot(data)
plt.show()