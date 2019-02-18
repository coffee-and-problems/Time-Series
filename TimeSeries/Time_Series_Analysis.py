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
D = TSAnalyzer.dispersion(centered_series)
print("Дисперсия = ", D)

plt.subplot(4, 1, 3)
plt.plot(centered_series)
plt.title('Центрированный временной ряд')
plt.xlabel('time (s)')

(x, fourier) = TSAnalyzer.periodogramma(centered_series)

plt.subplot(4, 1, 4)
plt.plot(x, fourier)
plt.axhline(y = 0.05, color='orange', linestyle='--')
plt.title('Периодограмма')
plt.xlabel('frequency (1/s)')

plt.tight_layout()
plt.show()

#corellogramma = TSAnalyzer.autocorr2(centered_series)

#plt.subplot(3, 1, 1)
#plt.plot(corellogramma)
#plt.title('Смещенная коррелограмма')
#plt.xlabel('time (s)')

corellogramma = TSAnalyzer.autocorrelation(centered_series)

plt.subplot(3, 1, 1)
plt.plot(corellogramma)
plt.title('Смещенная коррелограмма')
plt.xlabel('time (s)')

a = 0.25
N_coeff = 0.5
weighted_corell = corellogramma * TSAnalyzer.Tukey(a, N_coeff)
(x, smoothed_period) = TSAnalyzer.smooth(weighted_corell)

plt.subplot(3, 1, 2)
plt.plot(x, smoothed_period)
plt.title('Сглаженная периодограмма, параметры a = %.2f, N* = %.1f N' % (a, N_coeff))
plt.xlabel('frequency (1/s)')

a = 0.25
N_coeff = 0.1
weighted_corell = corellogramma * TSAnalyzer.Tukey(a, N_coeff)
(x, smoothed_period) = TSAnalyzer.smooth(weighted_corell)

plt.subplot(3, 1, 3)
plt.plot(weighted_corell)
plt.title('Сглаженная периодограмма, параметры a = %.2f, N* = %.1f N' % (a, N_coeff))
plt.xlabel('frequency (1/s)')

plt.tight_layout()
plt.show()
