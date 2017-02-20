import numpy
from numpy.linalg import norm
from matplotlib import pyplot
from ex3b_funcs import single_coil, magnetic_field, single_coil_field, \
        plot_magnetic_field_2D

# Error analysis using N^1 to N^max_exp line segments to discretise coil
max_exp = 5
n_lines = numpy.logspace(1, max_exp, max_exp)

# Compute B-field at 100 different points on x-axis
nx = 100
x = numpy.linspace(-5, 5, nx)

# Points in Cartesian 3D space
points = numpy.zeros((nx, 3))
points[:,0] = x
B = numpy.zeros_like(points)

# Compute exact solution
B_ex = single_coil_field(x)

# Compute errors in domain for each accuracy
errors = numpy.zeros((nx, max_exp))
for i, N in enumerate(n_lines): 
    wire = single_coil(0, int(N))
    B = numpy.asarray([magnetic_field(wire, r) for r in points])
    errors[:,i] = abs((B[:,0] - B_ex) / B_ex)

# Plot the magnetic field for the highest resolution
pyplot.clf()
pyplot.plot(x, B[:,0], 'x', label='Computational')
pyplot.plot(x, B_ex, '-', label='Analytic')
pyplot.xlabel('$x / R$')
pyplot.ylabel('$B / (\mu_0 I)$')
pyplot.legend()
pyplot.savefig('core_task1_magfield_N1e5.pdf')

# Plot the errors throughout the domain for the lowest resolution
pyplot.clf()
pyplot.plot(x, errors[:,0])
pyplot.xlabel('$x / R$')
pyplot.ylabel('$||(B - B_{\mathrm{exact}}) / B_{\mathrm{exact}}||_2$')
pyplot.title('$N=10$')
pyplot.savefig('core_task1_error_N10.pdf')

# Plot norm of errors vs. number of line segments with logarithmic axes
pyplot.clf()
pyplot.loglog(n_lines, norm(errors, axis=0), 'x')
pyplot.xlabel('$N$')
pyplot.ylabel('$||(B - B_{\mathrm{exact}}) / B_{\mathrm{exact}}||_2$')
pyplot.savefig('core_task1_convergence.pdf')

# Now compute solution in the xy-plane
n_lines = 1000
wire = single_coil(0, int(n_lines))
nx = 100
ny = 100
lims = numpy.array([[-1.5, 1.5], [-1.5, 1.5]])
x = numpy.linspace(lims[0,0], lims[0,1], nx)
y = numpy.linspace(lims[1,0], lims[1,1], ny)
X, Y = numpy.meshgrid(x, y)
points = numpy.zeros((nx, ny, 3))
points[:,:,0] = X
points[:,:,1] = Y
B = numpy.zeros_like(points)
# TODO: Check if there is pythonic way of doing double for-loops
for i in range(nx):
    for j in range(ny):
        B[i,j,:] = magnetic_field(wire, points[i,j,:])

# Plot filled contour plot and streamlines of magnetic field in xy-plane
# Filled contours and colorbar correspond to magnetic field strength
# Streamlines illustrate the direction of flow in the field
plot_magnetic_field_2D(X, Y, B, lims, 'core_task1_magfield_xyplane.pdf')
