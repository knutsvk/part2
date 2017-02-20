import numpy
from matplotlib import pyplot
from ex1_funcs import fresnel_s, fresnel_c

t = numpy.linspace(-5, 5, 500)
x = numpy.empty_like(t)
y = numpy.empty_like(t)
for i,v in enumerate(t):
    # TODO: vectorise properly 
    x[i] = fresnel_s(v)
    y[i] = fresnel_c(v)

pyplot.plot(x, y)
pyplot.xlabel('$x$')
pyplot.ylabel('$y$')
pyplot.axis('equal')
pyplot.savefig('core_task2.pdf')
