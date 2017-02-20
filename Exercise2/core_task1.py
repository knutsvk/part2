import numpy
from matplotlib import pyplot
from scipy.optimize import curve_fit
from ex2_funcs import solve_ode, plot_energy, find_period, linear_function

# Set up parameters
q = 0
F = 0
# Number of natural periods per value of theta0
n_periods = 5
thetas = numpy.linspace(1e-6, numpy.pi, endpoint=False)
periods = numpy.empty_like(thetas)

for i, theta0 in enumerate(thetas) :
    t, y = solve_ode(theta0, q, F, n_periods)
    periods[i] = find_period(t, y)

# Print value of period for theta0 = pi/2
print("theta0 = pi / 2 => T =", periods[len(thetas)//2])

# Generate plot of period vs amplitude
fig = pyplot.figure()
pyplot.xlabel(r'$\theta_0 / \pi$')
pyplot.ylabel(r'$T \mathrm{(s)} / (2 \pi)$')
pyplot.plot(thetas / numpy.pi, periods / (2 * numpy.pi), 'o')
pyplot.savefig('core_task1_period_amplitude.pdf')

# Now investigate energy conservation 
theta0 = 0.01
n_periods = 10000

t, y = solve_ode(theta0, q, F, n_periods)
plot_energy(t, y, 'core_task1_energy_conservation.pdf')
