Exercise 3A: Diffraction by the FFT
Function definitions can be found in the file 'ex3a_funcs.py'. 

Core Task 1
The solution method works well, as can be seen from the magnetic field on the
x-axis. Even with N=10 the relative error is below 10% for -5 <= x <= 5.
According to the log-log plot of error norm vs N, the convergence rate looks to
be quadratic, which is excellent. The filled contour plots and streamlines in
the xy-plane show that the code also handles several dimensions well. 
To generate relevant plots, run:
python core_task1.py

Core Task 2
With 1000 line segments per coil, and the slice of the cylinder discretised by
100x100 points, the maximum percentage deviation from the field strength at
(x,y) = (0,0) is 1.17e-05. 
To generate plots of the field for the Helmholtz coils, run: 
python core_task2.py

Supplementary Task 1 
Results as expected. To generate plots with one coil reversed, run: 
python supp_task1.py

Supplementary Task 2
To generate lots of pretty plots of magnetic field for different coil amounts:
python supp_task2.py
