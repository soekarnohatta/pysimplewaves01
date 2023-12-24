import numpy
import numpy as np

from PySimpleWaves.wave.utils.gen import wave_maker
from PySimpleWaves.wave.utils.parser import wave_parser


class Wave():
    def __init__(self, equation: str):
        self.equation = equation
        self.computed_equation = 0
        self.superposed = 0

    def compute_equation(self):
        t = np.linspace(0, 10, 1000)
        x = np.linspace(0, 10, 1000)
        to_parse = wave_parser(self.equation)

        self.computed_equation = wave_maker(t, x, to_parse)
        return self.computed_equation

    def analyze(self):
        to_analyze = wave_parser(self.equation)
        return [to_analyze[0], to_analyze[1], to_analyze[2], to_analyze[3], to_analyze[4], to_analyze[5],
                  numpy.absolute(2*numpy.pi/to_analyze[3]), 2*numpy.pi/to_analyze[4], to_analyze[4]/to_analyze[3]]

    def superpose(self, eqs: [str]):
        i = 0
        wave_eqs = []
        for val in eqs:
            i += 1
            if val != eqs[0]:
                wave_eqs.append(wave_parser(eqs[i - 1]))

        wave_calc = []
        t = np.linspace(0, 10, 1000)
        x = np.linspace(0, 10, 1000)
        for val in wave_eqs:
            amplitude, _, _ = wave_maker(t, x, val)
            wave_calc.append(amplitude)

        self.superposed = 0
        for val in wave_calc:
            self.superposed += val

        return self.superposed
