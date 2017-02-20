import numpy
from scipy.integrate import quadrature

def estimate_sintegral(n_points):
    s = numpy.pi / 8
    V = s**8
    points = s * numpy.random.rand(n_points, 8)
    func_values = 1e6 * numpy.sin(numpy.sum(points, axis=1))
    func_avg = numpy.mean(func_values)
    func_squared_avg = numpy.mean(func_values**2)
    est = V * func_avg
    std = V * numpy.sqrt((func_squared_avg - func_avg**2) / n_points)
    return est, std

def inverse_sqrt(N, b):
    return b / numpy.sqrt(N)

def f_cos(x):
    return numpy.cos(numpy.pi * x**2 / 2)

def f_sin(x):
    return numpy.sin(numpy.pi * x**2 / 2)

def fresnel_c(u, tolerance=1.49e-08, max_iters=1000):
    return quadrature(f_cos, numpy.zeros_like(u), u, tol=tolerance, rtol=tolerance,
            maxiter=max_iters, vec_func=True)[0]

def fresnel_s(u, tolerance=1.49e-08, max_iters=1000):
    return quadrature(f_sin, numpy.zeros_like(u), u, tol=tolerance, rtol=tolerance,
            maxiter=max_iters, vec_func=True)[0]
