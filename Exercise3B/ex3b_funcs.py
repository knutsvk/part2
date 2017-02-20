import numpy
from matplotlib import pyplot, cm

def dB(r1, r2, point):
    rmid = (r1 + r2) / 2
    dl = r2 - r1
    r = (point - rmid)
    return numpy.cross(dl, r) / (4 * numpy.pi * numpy.tile(numpy.sum(r**2,
        1)**(3 / 2), (3, 1)).transpose())

def magnetic_field(wire, point):
    return numpy.sum(dB(wire[:-1], wire[1:], point), 0)

def single_coil(x, N):
    # y^2 + z^2 = 1
    wire = numpy.zeros((N + 1, 3))
    theta = numpy.linspace(0, 2 * numpy.pi, N + 1)
    wire[:,0] = x
    wire[:,1] = numpy.cos(theta)
    wire[:,2] = numpy.sin(theta)
    return wire

def reverse_coil(x, N):
    # y^2 + z^2 = 1
    wire = numpy.zeros((N + 1, 3))
    theta = numpy.linspace(2 * numpy.pi, 0, N + 1)
    wire[:,0] = x
    wire[:,1] = numpy.cos(theta)
    wire[:,2] = numpy.sin(theta)
    return wire

def single_coil_field(x):
    return (2 * (1 + x**2)**(3 / 2))**(-1)

def plot_magnetic_field_2D(X, Y, B, lims, filename):
    pyplot.clf()
    pyplot.contourf(X, Y, numpy.sqrt(numpy.sum(B**2, axis=2)), 50, cmap=cm.viridis)
    pyplot.colorbar()
    pyplot.streamplot(X, Y, B[:,:,0], B[:,:,1], color='white', linewidth=0.5,
            density=1.0)
    pyplot.xlabel('$x/R$')
    pyplot.ylabel('$y/R$')
    pyplot.title('$\mathbf{B} / (\mu_0 I)$')
    pyplot.xlim(lims[0,0], lims[0,1])
    pyplot.ylim(lims[1,0], lims[1,1])
    pyplot.savefig(filename)
