import thinkdsp as dsp
import thinkplot as plot
#import matplotlib
from matplotlib import pyplot

cos_sig = dsp.CosSignal(freq=440, amp=1.0, offset=0)
sin_sig = dsp.SinSignal(freq=880, amp=0.5, offset=0)
mix = cos_sig + sin_sig

cos_wave = cos_sig.make_wave(duration=0.5, start=0, framerate=44100)
sin_wave = sin_sig.make_wave(duration=0.5, start=0, framerate=44100)
wave = mix.make_wave(duration=0.5, start=0, framerate=44100)

period = mix.period
segment = wave.segment(start=0, duration=period*3)      #Take 3 period segment of wave

print('Plotting Waveform (time domain)...')
#cos_wave.plot()        #uncomment to plot cos
#sin_wave.plot()        #uncomment to plot sin
#wave.plot()            #uncomment to plot wave
segment.plot()
pyplot.show()

#
#   Draw Spectrum from Wave (time domain to frequency domain)
#
print('Plotting Spectrum (frequency domain)...')
spectrum = wave.make_spectrum()
spectrum.plot()
plot.show()

t = 0
index_at_t = wave.find_index(t)             #Get index for a given time
sample_at_t = wave.ys[index_at_t]           #Access individual samples with .ys[i] 
print("Sample at Index[" + str(index_at_t) + "] = "+ str(sample_at_t))










