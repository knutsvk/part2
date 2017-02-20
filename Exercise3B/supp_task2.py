import numpy
from ex3b_funcs import single_coil, magnetic_field, plot_magnetic_field_2D

# line segments per coil
n_segments = 100

# Discretise xy-plane
nx = 100
ny = 100
lims = numpy.array([[-5, 5], [-5, 5]])
x = numpy.linspace(lims[0,0], lims[0,1], nx)
y = numpy.linspace(lims[1,0], lims[1,1], ny)
X, Y = numpy.meshgrid(x, y)

# Compute fields for various coil amounts 
n_coils = numpy.array([2, 3, 5, 10, 40])
for N in n_coils: 
    coil_locations = numpy.linspace(-5, 5, N)
    coils = numpy.empty((N, n_segments, 3))
    coils = numpy.asarray([single_coil(x, n_segments) for x in coil_locations])


    points = numpy.zeros((nx, ny, 3))
    points[:,:,0] = X
    points[:,:,1] = Y
    B = numpy.zeros_like(points)

    for i in range(nx):
        for j in range(ny):
            for wire in coils:
                B[i,j,:] += magnetic_field(wire, points[i,j,:])

    plot_magnetic_field_2D(X, Y, B, lims, 'supp_task2_N' + str(N) + '.pdf')
