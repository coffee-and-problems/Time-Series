import numpy as np
from os.path import join
import matplotlib.pyplot as plt
import TSAnalyzer

time_series = np.loadtxt(join('..', 'Data', 'time_series_data.dat'))

plt.subplot(4, 1, 1)
plt.plot(time_series)
plt.title('Исходный временной ряд')
plt.xlabel('time (s)')

(trend, a, b) = TSAnalyzer.get_trend(time_series)
trend_label = "α = %.2f, β = %.2f" % (a, b)

plt.subplot(4, 1, 2)
plt.plot(time_series)
plt.plot(trend, label = trend_label)
plt.title('Исходный временной ряд, тренд')
plt.legend()
plt.xlabel('time (s)')

centered_series = TSAnalyzer.center(time_series, trend)

plt.subplot(4, 1, 3)
plt.plot(centered_series)
plt.title('Центрированный временной ряд')
plt.xlabel('time (s)')

(x, fourier) = TSAnalyzer.periodogramma(centered_series)

plt.subplot(4, 1, 4)
plt.plot(x, fourier)
plt.axhline(y = 0.05, color='orange', linestyle='-')
plt.title('Периодограмма')
plt.xlabel('time (s)')

plt.tight_layout()
plt.show()
