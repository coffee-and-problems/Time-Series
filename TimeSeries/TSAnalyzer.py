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
    X = fft(centered_series)
    D = 1/(N*N) * (X.real*X.real + X.imag*X.imag)
    p = np.array_split(D, 2)[0]
    x = (np.linspace(0, (N-1), N//(2*Δt)))/(2*N)
    return (x, p)

def dispersion(centered_series):
    """Оценка дисперсии центрированного ряда"""
    sum = np.sum(centered_series*centered_series)
    return 1/(N - 1) * sum

def autocorr2(x):
    r2=np.fft.ifft(np.abs(np.fft.fft(x))**2).real
    c=(r2/N-np.mean(x)**2)/np.std(x)**2
    return c[:len(x)//2]

def autocorrelation(centered_series):
    """Возвращает коррелограмму"""
    cor = np.correlate(centered_series, centered_series, "full")
    cor = cor/85
    return np.array_split(cor, 2)[1]


#Осторожно! Делегаты!

def Tukey(a, N_coeff):
    """Возвращает numpy массив весовой функции Тьюки с параметрами a, N_coeff*N"""
    N_asterix = N_coeff * N
    return np.fromfunction(lambda m: 1-2*a + 2*a*np.cos((np.pi*m)/N_asterix), (N-1, ), dtype=int)

def smooth(weighted_corell):
    """Возвращает частоты и сглаженную периодограмму"""
    from scipy.fftpack import fft
    c0 = np.full((N-1,), weighted_corell[0])
    fftX = fft(weighted_corell)
    D = 1/N * 2 *(fftX.real - c0)
    p = np.array_split(D, 2)[0]
    x = (np.linspace(0, (N-1), N//(2*Δt)))/(2*N)
    return (x, p)