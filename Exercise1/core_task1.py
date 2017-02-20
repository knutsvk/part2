import numpy
from matplotlib import pyplot 
from scipy.optimize import curve_fit
from ex1_funcs import estimate_sintegral, inverse_sqrt

# Problem parameters
max_exp = 6         # Will use N up to 10**max_exp
n_estimates = 100   # Number of estimates per choice of N

# Set up the different values of N to try
N = numpy.logspace(2, max_exp, num=max_exp-1)
errors = numpy.empty_like(N)

# For each value of N, perform n_estimates experiments
estimates = numpy.empty(n_estimates)
stderr = numpy.empty(n_estimates)

for i, n in enumerate(N):
    for est in range(n_estimates):
        estimates[est], stderr[est] = estimate_sintegral(int(n))
    errors[i] = numpy.std(estimates)
    print("N =", int(n), "\tresult =", numpy.mean(estimates), 
            "+-", numpy.mean(stderr))

# Curve fitting 
popt, pcov = curve_fit(inverse_sqrt, N, errors)

# Plot errors vs N
fig = pyplot.figure()
pyplot.xlabel('$N$')
pyplot.ylabel('$\sigma$')
pyplot.loglog(N, errors, 'x', label='Computational')
N_dense = numpy.logspace(2, max_exp, num=500)
pyplot.loglog(N_dense, inverse_sqrt(N_dense, popt[0]), 
    label='Curve fit $\propto N^{-1/2}$')
pyplot.legend()
pyplot.savefig('core_task1.pdf')
