import numpy as np
from os.path import join
import matplotlib.pyplot as plt
import TSAnalyzer

time_series = np.loadtxt(join('..', 'Data', 'time_series_data.dat'))

plt.subplot(3, 1, 1)
plt.plot(time_series)
plt.title('Исходный временной ряд')
plt.xlabel('time (s)')
plt.ylabel('X')

(trend, a, b) = TSAnalyzer.get_trend(time_series)
trend_label = "α = %.2f, β = %.2f" % (a, b)

plt.subplot(3, 1, 2)
plt.plot(time_series)
plt.plot(trend, label = trend_label)
plt.title('Исходный временной ряд, тренд')
plt.legend()
plt.xlabel('time (s)')
plt.ylabel('X')
plt.tight_layout()

centered_series = TSAnalyzer.center(time_series, trend)

plt.subplot(3, 1, 3)
plt.plot(centered_series)
plt.title('Центрированный временной ряд')
plt.xlabel('time (s)')
plt.ylabel('X')

plt.show()
