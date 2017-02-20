import numpy
from matplotlib import pyplot
from ex3a_funcs import fraunhofer, single_slit
from scipy.special import sinc

lam = 500e-9
d = 100e-6
D = 1
L = 5e-3

N = 2**9

A = single_slit(L, d, N)
y, I = fraunhofer(A, L, N)

pyplot.clf()
pyplot.plot(y * d, I, '--', label='Computed')
pyplot.plot(y * d, sinc(d * y)**2, label='Theoretical')
pyplot.xlabel('$y d / (\lambda D)$')
pyplot.ylabel('$I/I_0$')
pyplot.legend()
pyplot.savefig('core_task1.pdf')
