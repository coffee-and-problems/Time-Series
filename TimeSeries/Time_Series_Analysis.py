import numpy as np
from os.path import join
import matplotlib.pyplot as plt
import TSAnalyzer

time_series = np.loadtxt(join('..', 'Data', 'time_series_data.dat'))
N = len(time_series)

plt.subplot(4, 1, 1)
plt.plot(time_series)
plt.title('Исходный временной ряд')
plt.xlabel('time (s)')

(trend, a, b) = TSAnalyzer.get_trend(time_series)
trend_label = "α = %.2f, β = %.2f" % (a-0.01, b)

plt.subplot(4, 1, 2)
plt.plot(time_series)
plt.plot(trend, label = trend_label)
plt.title('Исходный временной ряд, тренд')
plt.legend()
plt.xlabel('time (s)')

centered_series = TSAnalyzer.center(time_series, trend)
(D, g) = TSAnalyzer.dispersion(centered_series)

plt.subplot(4, 1, 3)
plt.plot(centered_series)
plt.title('Центрированный временной ряд')
plt.xlabel('time (s)')

(x, perio) = TSAnalyzer.periodogramma(centered_series)

plt.subplot(4, 1, 4)
plt.plot(x, perio)
plt.axhline(y = 0.09, color='orange', linestyle='--')
plt.title('Периодограмма')
plt.xlabel('frequency (1/s)')

plt.tight_layout()
plt.show()

corellogramma = TSAnalyzer.autocorrelation(centered_series)

from parameters_resource import A1
from math import sqrt
gamma = (A1*A1)/(2*corellogramma[0] - A1*A1)

max_periodogramma = np.amax(perio)
A_a = sqrt(4*max_periodogramma)
gamma_a = (A_a*A_a)/(2*corellogramma[0] - A_a*A_a)
print("Дисперсия = %.1f, сигнал/шум с известным A = %.3f" % (D, gamma))
print("сигнал/шум с найденным А = %.3f" % gamma_a)



plt.subplot(3, 1, 1)
plt.plot(corellogramma)
plt.title('Смещенная коррелограмма')
plt.xlabel('time (s)')

a = 0.25
N_asterix = int(0.5*N)
weighted_corell = corellogramma[:N_asterix-1] * TSAnalyzer.Tukey(a, N_asterix)
(x, smoothed_period) = TSAnalyzer.smooth(weighted_corell, N_asterix)

plt.subplot(3, 1, 2)
plt.plot(x, smoothed_period)
plt.title('Сглаженная периодограмма, параметры a = %.2f, N* = %.1f N' % (a, 0.5))
plt.xlabel('frequency (1/s)')

a = 0.25
N_asterix = int(0.1*N)
weighted_corell = corellogramma[:N_asterix-1] * TSAnalyzer.Tukey(a, N_asterix)
(x, smoothed_period) = TSAnalyzer.smooth(weighted_corell, N_asterix)

plt.subplot(3, 1, 3)
plt.plot(x, smoothed_period)
plt.title('Сглаженная периодограмма, параметры a = %.2f, N* = %.1f N' % (a, 0.1))
plt.xlabel('frequency (1/s)')

plt.tight_layout()
plt.show()
