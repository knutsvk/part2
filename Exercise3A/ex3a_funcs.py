import numpy
from numpy.fft import fft, fftshift
from matplotlib import pyplot

def fraunhofer(A, L, N):
    # y = y / (lam D)
    y = numpy.linspace(-(N-1)**2 / (2*L*N), (N-1)**2 / (2*L*N), N)
    psi = fft(A)
    psi = fftshift(psi)
    I = numpy.abs(psi)**2
    return y, I / I[N//2]

def fresnel(A, L, d, lam, D, N): 
    x = numpy.linspace(-L / 2, L / 2, N)
    y = numpy.linspace(-(N-1)**2 / (2*L*N), (N-1)**2 / (2*L*N), N)
    mod_factor = numpy.exp(1j * numpy.pi * x**2 / (lam * D))
    A_mod = mod_factor * A
    psi = fft(A_mod)
    psi = fftshift(psi)
    I = numpy.abs(psi)**2
    return y, I / I[N//2]

def single_slit(L, d, N):
    x = numpy.linspace(-L / 2, L / 2, N)
    A = numpy.zeros(N, dtype=complex)
    slit = (x <= d / 2) & (x >= -d / 2)
    A[slit] = 1
    return A

def sin_grating(L, d, m, s, N): 
    x = numpy.linspace(-L / 2, L / 2, N)
    phi = m / 2 * numpy.sin(2 * numpy.pi * x / s)
    grating = (x <= d / 2) & (x >= -d / 2)
    A = numpy.zeros(N, dtype=complex)
    A[grating] = numpy.exp(1j*phi[grating])
    return A
