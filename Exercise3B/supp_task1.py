import numpy
from ex3b_funcs import single_coil, reverse_coil, magnetic_field, \
        plot_magnetic_field_2D

N = 1000
left_wire = single_coil(-0.5, int(N))
right_wire = reverse_coil(0.5, int(N))

nx = 101
ny = 101
lims = numpy.array([[-1.5, 1.5], [-1.5, 1.5]])
x = numpy.linspace(lims[0,0], lims[0,1], nx)
y = numpy.linspace(lims[1,0], lims[1,1], ny)
X, Y = numpy.meshgrid(x, y)

points = numpy.zeros((nx, ny, 3))
points[:,:,0] = X
points[:,:,1] = Y
B = numpy.zeros_like(points)

for i in range(nx):
    for j in range(ny):
        B[i,j,:] = magnetic_field(left_wire, points[i,j,:]) + \
                magnetic_field(right_wire, points[i,j,:])

plot_magnetic_field_2D(X, Y, B, lims, 'supp_task1_magfield_xyplane.pdf')

lims = numpy.array([[-0.05, 0.05], [-0.05, 0.05]])
x = numpy.linspace(lims[0,0], lims[0,1], nx)
y = numpy.linspace(lims[1,0], lims[1,1], ny)
X, Y = numpy.meshgrid(x, y)

points[:,:,0] = X
points[:,:,1] = Y

for i in range(nx):
    for j in range(ny):
        B[i,j,:] = magnetic_field(left_wire, points[i,j,:]) + \
                magnetic_field(right_wire, points[i,j,:])

plot_magnetic_field_2D(X, Y, B, lims, 'supp_task1_magfield_xyplane_zoom.pdf')
