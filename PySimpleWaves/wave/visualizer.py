from PySimpleWaves.wave.utils.gen import visualize_wave
from PySimpleWaves.wave.wave import Wave


class Visualizer(Wave):
    def __init__(self, equation: str):
        super().__init__(equation)

    def visualize_image(self, path):
        if self.superposed != 0:
            visualize_wave(self.superposed, path)
            return

        visualize_wave(self.computed_equation, path)