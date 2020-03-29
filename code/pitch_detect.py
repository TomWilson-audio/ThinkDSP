import thinkdsp as dsp
#import matplotlib
from matplotlib import pyplot

cos_sig = dsp.CosSignal(freq=440, amp=1.0, offset=0)
sin_sig = dsp.SinSignal(freq=880, amp=0.5, offset=0)
mix = cos_sig + sin_sig

cos_wave = cos_sig.make_wave(duration=0.01, start=0, framerate=44100)
sin_wave = sin_sig.make_wave(duration=0.01, start=0, framerate=44100)
wave = mix.make_wave(duration=0.01, start=0, framerate=44100)

cos_wave.plot()
sin_wave.plot()
wave.plot()
pyplot.show()



