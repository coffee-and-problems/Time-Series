import sys
from os.path import join
data_path = join('..', 'Data')
sys.path.append(data_path)
from parameters_resource import *
import numpy as np

class Time_Series(object):
    """Временной ряд с линейным трендом и нормальным шумом"""
    def __init__(self):
        Time_Series.save(Time_Series.make())

    @staticmethod
    def make():
        tk = np.linspace(0, N-1, N//Δt)
        σ = np.sqrt(A1*A1/(2*γ))
        return α + β*tk + A1*np.cos(2*np.pi*ν1*tk - φ1) + σ*np.random.normal(0, 1, N//Δt)

    @staticmethod
    def save(data):
        with open(join(data_path, 'time_series_data.dat'), 'w') as f:
            np.savetxt(f, data)