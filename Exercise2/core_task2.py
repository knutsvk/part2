from ex2_funcs import solve_ode, plot_solution

# Try several values for damping
theta0 = 0.01
qs = [1, 5, 10]
F = 0
n_periods = 4

for q in qs: 
    t, y = solve_ode(theta0, q, F, n_periods)
    filename = 'core_task2_damping_q' + str(int(q)) + '.pdf'
    plot_solution(t, y, filename)

# Now keep damping constant and vary driving force
q = 0.5
Fs = [0.5, 1.2, 1.44, 1.465]
n_periods = 10

for F in Fs: 
    t, y = solve_ode(theta0, q, F, n_periods)
    filename = 'core_task2_driving_F' + str(int(F * 1000)) + '.pdf'
    plot_solution(t, y, filename)
