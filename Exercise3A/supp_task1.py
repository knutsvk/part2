import numpy
from matplotlib import pyplot
from ex3a_funcs import fresnel, single_slit, sin_grating

lam = 500e-9
d = 100e-6
D = 5e-3
L = 5e-3

N = 2**9

A = single_slit(L, d, N)
y, I = fresnel(A, L, d, lam, D, N)

pyplot.clf()
pyplot.plot(y * d, I)
pyplot.xlabel('$y d / (\lambda D)$')
pyplot.ylabel('$I/I_0$')
pyplot.savefig('supp_task1_slit.pdf')

d = 2e-3
D = 0.5
s = 100e-6
m = 8

N = 2**12

A = sin_grating(L, d, m, s, N)
y, I = fresnel(A, L, d, lam, D, N)

pyplot.clf()
pyplot.plot(y * d, I)
pyplot.xlabel('$y d / (\lambda D)$')
pyplot.ylabel('$I/I_0$')
pyplot.xlim([-200,200])
pyplot.savefig('supp_task1_grating.pdf')
