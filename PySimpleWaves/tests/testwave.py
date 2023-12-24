import unittest

import numpy as np

from PySimpleWaves.wave.wave import Wave


class TestWave(unittest.TestCase):

    def test_wave(self):
        newWave = Wave("y=4sin(5t-8x")
        newWave.compute_equation()

        x = np.linspace(0, 10, 1000)
        t = np.linspace(0, 10, 1000)
        to_check = 4 * np.sin((5 * t) - (8 * x))
        self.assertEqual(newWave.compute_equation(), to_check)


unittest.main()
