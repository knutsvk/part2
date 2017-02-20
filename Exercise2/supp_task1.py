from ex2_funcs import solve_ode, plot_solution

q = 0.5
F = 1.2
n_periods = 30

theta0 = 0.2
t, y = solve_ode(theta0, q, F, n_periods)
filename = 'supp_task1_init1.pdf'
plot_solution(t, y, filename)

theta0 = 0.20001
t, y = solve_ode(theta0, q, F, n_periods)
filename = 'supp_task1_init2.pdf'
plot_solution(t, y, filename)
