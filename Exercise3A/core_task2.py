import numpy
from matplotlib import pyplot
from ex3a_funcs import fraunhofer, sin_grating

lam = 500e-9
d = 2e-3
D = 10
L = 5e-3

s = 100e-6
m = 8

N = 2**9

A = sin_grating(L, d, m, s, N)
y, I = fraunhofer(A, L, N)

pyplot.clf()
pyplot.plot(y * d, I)
pyplot.xlabel('$y d / (\lambda D)$')
pyplot.ylabel('$I/I_0$')
pyplot.savefig('core_task2.pdf')

