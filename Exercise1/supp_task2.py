import numpy
from matplotlib import pyplot
from ex1_funcs import fresnel_s, fresnel_c

# Slit width
d = 10e-2

# Wavelength
lam = 1e-2

# Distance to screen
dist = numpy.array([30e-2, 50e-2, 100e-2])

# Length of screen
L = 5 * d

# Values of y (distance on screen, midpoint = L/2)
y = numpy.linspace(0, L, 400)

# Allocate variables 
real = numpy.empty_like(y)
imag = numpy.empty_like(y)
fig = pyplot.figure()

# Compute values for different screen distances
for D in dist:
    u0 = numpy.sqrt(2 / (lam * D)) * ((L - d) / 2 - y)
    u1 = numpy.sqrt(2 / (lam * D)) * ((L + d) / 2 - y)
    # TODO: vectorize fresnel funcs
    for i in range(len(y)):
        real[i] = fresnel_c(u1[i]) - fresnel_c(u0[i])
        imag[i] = fresnel_s(u1[i]) - fresnel_s(u0[i])

    # Plot result
    filename = 'supp_task2_D' + str(int(D * 100)) + '.pdf'
    pyplot.clf()
    pyplot.xlabel('$y / d$')
    pyplot.ylabel('$\Psi / \Psi_0$')
    pyplot.plot(y / d, real, 'r', label='$\mathrm{Re}$')
    pyplot.plot(y / d, imag, 'b', label='$\mathrm{Im}$')
    pyplot.legend()
    pyplot.savefig(filename)
