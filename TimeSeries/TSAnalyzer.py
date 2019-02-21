import sys
from os.path import join
__data_path = join('..', 'Data')
sys.path.append(__data_path)
from parameters_resource import *
import numpy as np

def get_trend(np_data):
    """Возвращает линейную аппроксимацию тренда и его параметры"""
    from sklearn.linear_model import LinearRegression

    model = LinearRegression()
    x = np.linspace(0, N-1, N//Δt)
    x_2d = np.reshape(x, (len(x),1))
    model.fit(x_2d, np_data)
    trend = model.predict(x_2d)

    from scipy import polyfit
    (b, a) = polyfit(x, trend, 1)
    return (trend, a, b)

def center(np_data, trend):
    """Центрирует ряд"""
    no_trend = np_data - trend
    mean = np.mean(no_trend)
    return no_trend - mean

def periodogramma(centered_series):
    """Возвращает частоты и периодограмму"""
    from scipy.fftpack import fft
    X = fft(centered_series, 1024)
    D = 1/(N*N) * (X.real*X.real + X.imag*X.imag)
    p = np.array_split(D, 2)[0]
    x = (np.linspace(0, (N-1), N//Δt))/(2*N)
    return (x, p)

def dispersion(centered_series):
    """Оценка дисперсии центрированного ряда"""
    sum = np.sum(centered_series*centered_series)
    return 1/(N - 1) * sum

def autocorrelation(centered_series):
    """Возвращает коррелограмму"""
    from scipy.fftpack import fft, ifft
    ffted = fft(centered_series, 512)
    cor = ifft(np.abs(ffted)**2).real/N
    return cor[:N-1]


#Осторожно! Лямбды!

def Tukey(a, N_asterix):
    """Возвращает numpy массив весовой функции Тьюки с параметрами a, N_coeff*N"""
    N_asterix = int(N_asterix)
    return np.fromfunction(lambda m: 1-2*a + 2*a*np.cos((np.pi*m)/N_asterix), (N_asterix-1, ), dtype=int)

def smooth(weighted_corell):
    """Возвращает частоты и сглаженную периодограмму"""
    from scipy.fftpack import fft
    N2 = 1024
    N1 = 512
    ffted = fft(weighted_corell, N2).real[:N1-1]
    D = 2*ffted
    return D