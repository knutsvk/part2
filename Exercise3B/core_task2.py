import numpy
from ex3b_funcs import single_coil, magnetic_field, plot_magnetic_field_2D

N = 1000
left_wire = single_coil(-0.5, int(N))
right_wire = single_coil(0.5, int(N))

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

plot_magnetic_field_2D(X, Y, B, lims, 'core_task2_magfield_xyplane.pdf')

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

plot_magnetic_field_2D(X, Y, B, lims, 'core_task2_magfield_xyplane_zoom.pdf')

B_abs = numpy.sqrt(numpy.sum(B**2, axis=2))
dev = numpy.abs(B_abs - B_abs[nx//2,ny//2]) / B_abs[nx//2,ny//2]
print('Max percentage deviation from centre field strength:', numpy.max(dev))
