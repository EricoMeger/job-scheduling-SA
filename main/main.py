import matplotlib.pyplot as plt
from sa.simulated_annealing import SimulatedAnnealing
from utils.helper import Helper

tasks = Helper.generate_tasks(1000) #Auto generate x tasks with random durations between 1 and 99
machines = 2
initial_temp = 1000
v = 50
max_iterations = 10000

simulated_annealing = SimulatedAnnealing(tasks, machines, initial_temp, v, max_iterations)
solution, cost, makespan_history, temperature_history, iterations = simulated_annealing.optimize_makespan()

print(f"Limite inferior: {Helper.get_lower_bound(tasks, machines)}. Esse limite é a solução ótima teórica, mas espera-se que o SA encontre algo igual ou muito perto disso.")

print("Melhor makespan alcançado:", cost)
Helper.write_solution(solution, len(tasks), machines, makespan_history, temperature_history, iterations)
Helper.plot_results(makespan_history, temperature_history)