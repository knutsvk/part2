from ex2_funcs import solve_ode, plot_chaos

n_periods = 3

# Small angle, periodic
theta0 = 0.01
q = 0
F = 0
t, y = solve_ode(theta0, q, F, n_periods)
plot_chaos(t, y, 'supp_task2_1.pdf')

# Large angle
theta0 = 3
t, y = solve_ode(theta0, q, F, n_periods)
plot_chaos(t, y, 'supp_task2_2.pdf')

# Damping
theta0 = 0.01
q = 0.5
t, y = solve_ode(theta0, q, F, n_periods)
plot_chaos(t, y, 'supp_task2_3.pdf')

# Driven
F = 0.1
t, y = solve_ode(theta0, q, F, n_periods)
plot_chaos(t, y, 'supp_task2_4.pdf')

# Strongly driven
F = 1.5
t, y = solve_ode(theta0, q, F, n_periods)
plot_chaos(t, y, 'supp_task2_5.pdf')
