import numpy
from matplotlib import pyplot 
from ex1_funcs import estimate_sintegral

# Runtime parameters
max_exp = 6         # Will use N up to 10**max_exp
n_estimates = 100   # Number of estimates per choice of N

# Set up the different values of N to try
N = numpy.logspace(2, max_exp, num=max_exp-1)
errors = numpy.empty_like(N)
theoretical_errors = numpy.empty_like(N)

# For each value of N, perform n_estimates experiments
estimates = numpy.empty(n_estimates)
stderr = numpy.empty(n_estimates)

for i, n in enumerate(N):
    for est in range(n_estimates):
        estimates[est], stderr[est] = estimate_sintegral(int(n))
    errors[i] = numpy.std(estimates)
    print("N =", int(n), "\tresult =", numpy.mean(estimates), 
            "+-", numpy.mean(stderr))
    theoretical_errors[i] = numpy.mean(stderr)

# Plot difference between computational and theoretical standard devs
fig = pyplot.figure()
pyplot.xlabel('$N$')
pyplot.ylabel('Difference between computational and theoretical errors')
pyplot.loglog(N, numpy.abs(errors-theoretical_errors), 'ro')
pyplot.savefig('supp_task1.pdf')
