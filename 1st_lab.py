import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq, ifft
import cmath, math

Input_1kHz_15kHz =[

+0.0000000000, +0.5924659585, -0.0947343455, +0.1913417162, +1.0000000000, +0.4174197128, +0.3535533906, +1.2552931065,
+0.8660254038, +0.4619397663, +1.3194792169, +1.1827865776, +0.5000000000, +1.1827865776, +1.3194792169, +0.4619397663,
+0.8660254038, +1.2552931065, +0.3535533906, +0.4174197128, +1.0000000000, +0.1913417162, -0.0947343455, +0.5924659585,
-0.0000000000, -0.5924659585, +0.0947343455, -0.1913417162, -1.0000000000, -0.4174197128, -0.3535533906, -1.2552931065,
-0.8660254038, -0.4619397663, -1.3194792169, -1.1827865776, -0.5000000000, -1.1827865776, -1.3194792169, -0.4619397663,
-0.8660254038, -1.2552931065, -0.3535533906, -0.4174197128, -1.0000000000, -0.1913417162, +0.0947343455, -0.5924659585,
+0.0000000000, +0.5924659585, -0.0947343455, +0.1913417162, +1.0000000000, +0.4174197128, +0.3535533906, +1.2552931065,
+0.8660254038, +0.4619397663, +1.3194792169, +1.1827865776, +0.5000000000, +1.1827865776, +1.3194792169, +0.4619397663,
+0.8660254038, +1.2552931065, +0.3535533906, +0.4174197128, +1.0000000000, +0.1913417162, -0.0947343455, +0.5924659585,
+0.0000000000, -0.5924659585, +0.0947343455, -0.1913417162, -1.0000000000, -0.4174197128, -0.3535533906, -1.2552931065,
-0.8660254038, -0.4619397663, -1.3194792169, -1.1827865776, -0.5000000000, -1.1827865776, -1.3194792169, -0.4619397663,
-0.8660254038, -1.2552931065, -0.3535533906, -0.4174197128, -1.0000000000, -0.1913417162, +0.0947343455, -0.5924659585,
+0.0000000000, +0.5924659585, -0.0947343455, +0.1913417162, +1.0000000000, +0.4174197128, +0.3535533906, +1.2552931065,
+0.8660254038, +0.4619397663, +1.3194792169, +1.1827865776, +0.5000000000, +1.1827865776, +1.3194792169, +0.4619397663,
+0.8660254038, +1.2552931065, +0.3535533906, +0.4174197128, +1.0000000000, +0.1913417162, -0.0947343455, +0.5924659585,
+0.0000000000, -0.5924659585, +0.0947343455, -0.1913417162, -1.0000000000, -0.4174197128, -0.3535533906, -1.2552931065,
-0.8660254038, -0.4619397663, -1.3194792169, -1.1827865776, -0.5000000000, -1.1827865776, -1.3194792169, -0.4619397663,
-0.8660254038, -1.2552931065, -0.3535533906, -0.4174197128, -1.0000000000, -0.1913417162, +0.0947343455, -0.5924659585,
-0.0000000000, +0.5924659585, -0.0947343455, +0.1913417162, +1.0000000000, +0.4174197128, +0.3535533906, +1.2552931065,
+0.8660254038, +0.4619397663, +1.3194792169, +1.1827865776, +0.5000000000, +1.1827865776, +1.3194792169, +0.4619397663,
+0.8660254038, +1.2552931065, +0.3535533906, +0.4174197128, +1.0000000000, +0.1913417162, -0.0947343455, +0.5924659585,
-0.0000000000, -0.5924659585, +0.0947343455, -0.1913417162, -1.0000000000, -0.4174197128, -0.3535533906, -1.2552931065,
-0.8660254038, -0.4619397663, -1.3194792169, -1.1827865776, -0.5000000000, -1.1827865776, -1.3194792169, -0.4619397663,
-0.8660254038, -1.2552931065, -0.3535533906, -0.4174197128, -1.0000000000, -0.1913417162, +0.0947343455, -0.5924659585,
+0.0000000000, +0.5924659585, -0.0947343455, +0.1913417162, +1.0000000000, +0.4174197128, +0.3535533906, +1.2552931065,
+0.8660254038, +0.4619397663, +1.3194792169, +1.1827865776, +0.5000000000, +1.1827865776, +1.3194792169, +0.4619397663,
+0.8660254038, +1.2552931065, +0.3535533906, +0.4174197128, +1.0000000000, +0.1913417162, -0.0947343455, +0.5924659585,
+0.0000000000, -0.5924659585, +0.0947343455, -0.1913417162, -1.0000000000, -0.4174197128, -0.3535533906, -1.2552931065,
-0.8660254038, -0.4619397663, -1.3194792169, -1.1827865776, -0.5000000000, -1.1827865776, -1.3194792169, -0.4619397663,
-0.8660254038, -1.2552931065, -0.3535533906, -0.4174197128, -1.0000000000, -0.1913417162, +0.0947343455, -0.5924659585,
-0.0000000000, +0.5924659585, -0.0947343455, +0.1913417162, +1.0000000000, +0.4174197128, +0.3535533906, +1.2552931065,
+0.8660254038, +0.4619397663, +1.3194792169, +1.1827865776, +0.5000000000, +1.1827865776, +1.3194792169, +0.4619397663,
+0.8660254038, +1.2552931065, +0.3535533906, +0.4174197128, +1.0000000000, +0.1913417162, -0.0947343455, +0.5924659585,
+0.0000000000, -0.5924659585, +0.0947343455, -0.1913417162, -1.0000000000, -0.4174197128, -0.3535533906, -1.2552931065,
-0.8660254038, -0.4619397663, -1.3194792169, -1.1827865776, -0.5000000000, -1.1827865776, -1.3194792169, -0.4619397663,
-0.8660254038, -1.2552931065, -0.3535533906, -0.4174197128, -1.0000000000, -0.1913417162, +0.0947343455, -0.5924659585,
-0.0000000000, +0.5924659585, -0.0947343455, +0.1913417162, +1.0000000000, +0.4174197128, +0.3535533906, +1.2552931065,
+0.8660254038, +0.4619397663, +1.3194792169, +1.1827865776, +0.5000000000, +1.1827865776, +1.3194792169, +0.4619397663,
+0.8660254038, +1.2552931065, +0.3535533906, +0.4174197128, +1.0000000000, +0.1913417162, -0.0947343455, +0.5924659585,
+0.0000000000, -0.5924659585, +0.0947343455, -0.1913417162, -1.0000000000, -0.4174197128, -0.3535533906, -1.2552931065,
]

Impulse_response = [
  -0.0018225230, -0.0015879294, +0.0000000000, +0.0036977508, +0.0080754303, +0.0085302217, -0.0000000000, -0.0173976984,
  -0.0341458607, -0.0333591565, +0.0000000000, +0.0676308395, +0.1522061835, +0.2229246956, +0.2504960933, +0.2229246956,
  +0.1522061835, +0.0676308395, +0.0000000000, -0.0333591565, -0.0341458607, -0.0173976984, -0.0000000000, +0.0085302217,
  +0.0080754303, +0.0036977508, +0.0000000000, -0.0015879294, -0.0018225230
]

ECG = [
    0, 0.0010593, 0.0021186, 0.003178, 0.0042373, 0.0052966, 0.0063559,
    0.0074153, 0.0084746, 0.045198, 0.081921, 0.11864, 0.15537, 0.19209,
    0.22881, 0.26554, 0.30226, 0.33898, 0.30226, 0.26554, 0.22881, 0.19209,
    0.15537, 0.11864, 0.081921, 0.045198, 0.0084746, 0.0077684, 0.0070621,
    0.0063559, 0.0056497, 0.0049435, 0.0042373, 0.0035311, 0.0028249,
    0.0021186, 0.0014124, 0.00070621, 0, -0.096045, -0.19209, -0.28814,
    -0.073446, 0.14124, 0.35593, 0.57062, 0.78531, 1, 0.73729, 0.47458,
    0.21186, -0.050847, -0.31356, -0.57627, -0.83898, -0.55932, -0.27966, 0,
    0.00073692, 0.0014738, 0.0022108, 0.0029477, 0.0036846, 0.0044215,
    0.0051584, 0.0058954, 0.0066323, 0.0073692, 0.0081061, 0.008843, 0.00958,
    0.010317, 0.011054, 0.011791, 0.012528, 0.013265, 0.014001, 0.014738,
    0.015475, 0.016212, 0.016949, 0.03484, 0.052731, 0.070621, 0.088512,
    0.1064, 0.12429, 0.14218, 0.16008, 0.17797, 0.16186, 0.14576, 0.12966,
    0.11356, 0.097458, 0.081356, 0.065254, 0.049153, 0.033051, 0.016949,
    0.013559, 0.010169, 0.0067797, 0.0033898, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0010593, 0.0021186, 0.003178,
    0.0042373, 0.0052966, 0.0063559, 0.0074153, 0.0084746, 0.045198, 0.081921,
    0.11864, 0.15537, 0.19209, 0.22881, 0.26554, 0.30226, 0.33898, 0.30226,
    0.26554, 0.22881, 0.19209, 0.15537, 0.11864, 0.081921, 0.045198, 0.0084746,
    0.0077684, 0.0070621, 0.0063559, 0.0056497, 0.0049435, 0.0042373,
    0.0035311, 0.0028249, 0.0021186, 0.0014124, 0.00070621, 0, -0.096045,
    -0.19209, -0.28814, -0.073446, 0.14124, 0.35593, 0.57062, 0.78531, 1,
    0.73729, 0.47458, 0.21186, -0.050847, -0.31356, -0.57627, -0.83898,
    -0.55932, -0.27966, 0, 0.00073692, 0.0014738, 0.0022108, 0.0029477,
    0.0036846, 0.0044215, 0.0051584, 0.0058954, 0.0066323, 0.0073692,
    0.0081061, 0.008843, 0.00958, 0.010317, 0.011054, 0.011791, 0.012528,
    0.013265, 0.014001, 0.014738, 0.015475, 0.016212, 0.016949, 0.03484,
    0.052731, 0.070621, 0.088512, 0.1064, 0.12429, 0.14218, 0.16008, 0.17797,
    0.16186, 0.14576, 0.12966, 0.11356, 0.097458, 0.081356, 0.065254, 0.049153,
    0.033051, 0.016949, 0.013559, 0.010169, 0.0067797, 0.0033898, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0010593,
    0.0021186, 0.003178, 0.0042373, 0.0052966, 0.0063559, 0.0074153, 0.0084746,
    0.045198, 0.081921, 0.11864, 0.15537, 0.19209, 0.22881, 0.26554, 0.30226,
    0.33898, 0.30226, 0.26554, 0.22881, 0.19209, 0.15537, 0.11864, 0.081921,
    0.045198, 0.0084746, 0.0077684, 0.0070621, 0.0063559, 0.0056497, 0.0049435,
    0.0042373, 0.0035311, 0.0028249, 0.0021186, 0.0014124, 0.00070621, 0,
    -0.096045, -0.19209, -0.28814, -0.073446, 0.14124, 0.35593, 0.57062,
    0.78531, 1, 0.73729, 0.47458, 0.21186, -0.050847, -0.31356, -0.57627,
    -0.83898, -0.55932, -0.27966, 0, 0.00073692, 0.0014738, 0.0022108,
    0.0029477, 0.0036846, 0.0044215, 0.0051584, 0.0058954, 0.0066323,
    0.0073692, 0.0081061, 0.008843, 0.00958, 0.010317, 0.011054, 0.011791,
    0.012528, 0.013265, 0.014001, 0.014738, 0.015475, 0.016212, 0.016949,
    0.03484, 0.052731, 0.070621, 0.088512, 0.1064, 0.12429, 0.14218, 0.16008,
    0.17797, 0.16186, 0.14576, 0.12966, 0.11356, 0.097458, 0.081356, 0.065254,
    0.049153, 0.033051, 0.016949, 0.013559, 0.010169, 0.0067797, 0.0033898, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0.0010593, 0.0021186, 0.003178, 0.0042373, 0.0052966, 0.0063559, 0.0074153,
    0.0084746, 0.045198, 0.081921, 0.11864, 0.15537, 0.19209, 0.22881, 0.26554,
    0.30226, 0.33898, 0.30226, 0.26554, 0.22881, 0.19209, 0.15537, 0.11864,
    0.081921, 0.045198, 0.0084746, 0.0077684, 0.0070621, 0.0063559, 0.0056497,
    0.0049435, 0.0042373, 0.0035311, 0.0028249, 0.0021186, 0.0014124,
    0.00070621, 0, -0.096045, -0.19209, -0.28814, -0.073446, 0.14124, 0.35593,
    0.57062, 0.78531, 1, 0.73729, 0.47458, 0.21186, -0.050847, -0.31356,
    -0.57627, -0.83898, -0.55932, -0.27966, 0, 0.00073692, 0.0014738,
    0.0022108, 0.0029477, 0.0036846, 0.0044215, 0.0051584, 0.0058954,
    0.0066323, 0.0073692, 0.0081061, 0.008843, 0.00958, 0.010317, 0.011054,
    0.011791, 0.012528, 0.013265, 0.014001, 0.014738, 0.015475, 0.016212,
    0.016949, 0.03484, 0.052731, 0.070621, 0.088512, 0.1064, 0.12429, 0.14218,
    0.16008, 0.17797, 0.16186, 0.14576, 0.12966, 0.11356, 0.097458, 0.081356,
    0.065254, 0.049153, 0.033051, 0.016949, 0.013559, 0.010169, 0.0067797,
    0.0033898, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0.0010593, 0.0021186, 0.003178, 0.0042373, 0.0052966,
    0.0063559, 0.0074153, 0.0084746, 0.045198, 0.081921, 0.11864, 0.15537,
    0.19209, 0.22881, 0.26554, 0.30226, 0.33898, 0.30226, 0.26554, 0.22881,
    0.19209, 0.15537, 0.11864, 0.081921, 0.045198, 0.0084746, 0.0077684,
    0.0070621, 0.0063559, 0.0056497, 0.0049435, 0.0042373, 0.0035311,
    0.0028249, 0.0021186, 0.0014124, 0.00070621, 0, -0.096045, -0.19209,
    -0.28814, -0.073446, 0.14124, 0.35593, 0.57062, 0.78531, 1, 0.73729,
    0.47458, 0.21186, -0.050847, -0.31356, -0.57627, -0.83898, -0.55932,
    -0.27966, 0, 0.00073692, 0.0014738, 0.0022108, 0.0029477, 0.0036846,
    0.0044215, 0.0051584, 0.0058954, 0.0066323, 0.0073692, 0.0081061, 0.008843,
    0.00958, 0.010317, 0.011054, 0.011791, 0.012528, 0.013265, 0.014001,
    0.014738, 0.015475, 0.016212, 0.016949, 0.03484, 0.052731, 0.070621,
    0.088512, 0.1064, 0.12429, 0.14218, 0.16008, 0.17797, 0.16186, 0.14576,
    0.12966, 0.11356, 0.097458, 0.081356, 0.065254, 0.049153, 0.033051,
    0.016949, 0.013559, 0.010169, 0.0067797, 0.0033898, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

x = np.arange(-np.pi, np.pi, 2*np.pi/320)

# Input_1kHz_15kHz_1 = [Input_1kHz_15kHz[0:160]] + [Input_1kHz_15kHz[161:]]

def swap_two_halves(signal):
    first_half = signal[:int(len(signal) / 2)]
    second_half = signal[int(len(signal) / 2 + 1):]
    new_signal = []
    for element in second_half:
        new_signal.append(element)
    for element in first_half:
        new_signal.append(element)
    final_signal = np.array(new_signal)
    return final_signal

def plot(array, title):
    plt.title(title)
    plt.plot(x, array)
    plt.show()

def plot_dis(array, title):
    plt.title(title)
    plt.plot(array, ".")
    plt.show()

plt.clf()

print(len(x))
Input_1kHz_15kHz_1 = swap_two_halves(Input_1kHz_15kHz)

plot(Input_1kHz_15kHz, "Input Signal")
plot_dis(Input_1kHz_15kHz, "Input Signal D")
#plot(Impulse_response)

# Number of samples in normalized_tone
# without abs we only get the real part
y = fft(Input_1kHz_15kHz)
plot(y.real, "Real")
# y_1 = fft(Input_1kHz_15kHz_1)

#there are 1 low freg but high mag and 1 high freq but low mag
# abs shows the magnitude
plot(abs(y), "Magnitude")

#imag plot
img = []
for c in y:
    img.append(c.imag)
plot(img, "Imaginary")

#Inverse-FFT
inv = ifft(y)
#print(inv)
plot(inv.real, "Inverse fft")

#phase plot
phase = []
for c in y:
    phase.append(cmath.phase(c))
plot(phase, "Phase")

#impulse response
# plot_dis(Impulse_response, "Impulse response") #discrete => continuous, next use fft to get the requirement
# fft_impulse = fft(Impulse_response)
# plot(fft_impulse, "Fourier Transform of Impulse Response")
# plot(abs(fft_impulse), "Mag of Ft im")
# img_i = []
# for c in fft_impulse:
#     img_i.append(c.imag)
# plot(img_i, "Imaginary Im")
# phase_i = []
# for c in fft_impulse:
#     phase_i.append(cmath.phase(c))
# plot(phase_i, "Phase Im")


convo = np.convolve(Input_1kHz_15kHz, Impulse_response, mode="same")
#print(convo)
#plot_dis(convo, "Convolution")

#multi and then convert = convert and then multi (prove)

fourier = fft(convo)
# plot(abs(fourier), "Fourier Transform of the convolution")

# plt.title("Fourier Transform of the convolution 1")
# plt.plot(fourier)
# plt.show()

Pad_impulse_response = (Impulse_response + 320*[0])[:320]
#print(Pad_impulse_response)
# ft_pad = fft(Pad_impulse_response)
# freq_mul = np.multiply(y, ft_pad)
# plot(abs(freq_mul), "Frequency multiplication")




