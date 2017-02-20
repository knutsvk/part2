import numpy
from matplotlib import pyplot 
from scipy.integrate import odeint

def dydt(y, t, q, F):
    rhs = y.copy()
    rhs[0] = y[1]
    rhs[1] = - numpy.sin(y[0]) - q * y[1] + F * numpy.sin(2 / 3 * t)
    return rhs

def solve_ode(theta0, q, F, n_periods):
    y0 = numpy.array([theta0, 0])
    t = numpy.linspace(0, n_periods * 2 * numpy.pi, 40 * n_periods)
    y = odeint(dydt, y0, t, args=(q, F))
    return t, y

def find_period(t, y):
    theta = y[:,0]
    periods = []
    t_prev = 0
    found_zero = False
    # Go through all time values
    for i in range(len(t)-1):
        # Angle is exactly zero
        if theta[i] == 0:
            t_next = t[i]
            found_zero = True
        # Angle changes sign
        elif theta[i+1] / theta[i] < 0: 
            t_next = (t[i] + t[i+1]) / 2
            found_zero = True
        if found_zero: 
            # Ignore if this is the first zero found
            if t_prev != 0:
                periods.append(2 * (t_next - t_prev))
            t_prev = t_next
            found_zero = False
    return numpy.mean(periods)

def linear_function(x, a):
    return a * x

def plot_solution(t, y, filename):
    pyplot.clf()
    pyplot.plot(t, y[:,0], label=r'$\theta$')
    pyplot.plot(t, y[:,1], label=r'$\omega \mathrm{(Hz)}$')
    pyplot.xlabel("$t \mathrm{(s)}$")
    pyplot.legend()
    pyplot.savefig(filename)

def plot_energy(t, y, filename):
    theta = y[:,0]
    omega = y[:,1]
    energy = 0.5 * omega**2 + 1 - numpy.cos(theta)
    pyplot.clf()
    pyplot.xlabel('$t \mathrm{(s)}$')
    pyplot.ylabel('$E / E(t=0)$')
    pyplot.ylim([0, 1])
    pyplot.plot(t, energy / energy[0])
    pyplot.savefig(filename)

def plot_chaos(t, y, filename):
    pyplot.clf()
    pyplot.plot(y[:,0], y[:,1])
    pyplot.xlabel(r"$\theta$")
    pyplot.ylabel(r"$\omega \mathrm{(Hz)}$")
    pyplot.savefig(filename)

