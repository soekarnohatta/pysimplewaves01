import numpy as np
import matplotlib.pyplot as plot

def wave_maker(t, x, wave_func):
    amplitude = np.sin(1)
    if wave_func[6] == "+ " and wave_func[7] == "+":
        if wave_func[1] == "cos":
            amplitude = wave_func[0] * np.cos((wave_func[4] * t) + (wave_func[3] * x) + wave_func[5])
        else:
            amplitude = wave_func[0] * np.sin((wave_func[4] * t) + (wave_func[3] * x) + wave_func[5])
    if wave_func[6] == "+ " and wave_func[7] == "-":
        if wave_func[1] == "cos":
            amplitude = wave_func[0] * np.cos((wave_func[4] * t) + (wave_func[3] * x) - wave_func[5])
        else:
            amplitude = wave_func[0] * np.sin((wave_func[4] * t) + (wave_func[3] * x) - wave_func[5])
    if wave_func[6] == "-" and wave_func[7] == "+":
        if wave_func[1] == "cos":
            amplitude = wave_func[0] * np.cos((wave_func[4] * t) - (wave_func[3] * x) + wave_func[5])
        else:
            amplitude = wave_func[0] * np.sin((wave_func[4] * t) - (wave_func[3] * x) + wave_func[5])
    if wave_func[6] == "-" and wave_func[7] == "-":
        if wave_func[1] == "cos":
            amplitude = wave_func[0] * np.cos((wave_func[4] * t) - (wave_func[3] * x) - wave_func[5])
        else:
            amplitude = wave_func[0] * np.sin((wave_func[4] * t) - (wave_func[3] * x) - wave_func[5])

    return amplitude, t, x


def visualize_wave(comp_eq, to_save):
    t = np.linspace(0, 10, 1000)

    plot.plot(t, comp_eq)
    plot.title('Visualisasi Gelombang')
    plot.xlabel('Time')
    plot.ylabel('Amplitude = sin or cos(args)')
    plot.grid(True, which='both')
    plot.axhline(y=0, color='k')
    plot.savefig("PyWaveBot/data/%s.png" % to_save)
    plot.clf()