import random
import math
import copy

def initialize_assignments(tasks, machines):
    assignments = []
    for _ in range(machines):
        assignments.append([0] * len(tasks))

    return assignments

def create_initial_solution(tasks, machines):
    assignments = initialize_assignments(tasks, machines)
    for i in range(len(tasks)):
        assignments[i % machines][i] = 1
    return assignments

def calculate_makespan(tasks, assignments):
    cost = [0] * len(assignments)

    for i in range(len(assignments)):
        for j in range(len(tasks)):
            if(assignments[i][j] == 1):
                cost[i] += tasks[j]

    return max(cost)

def find_task(selected_task, state):
    for i in range(len(state)):
        if state[i][selected_task] == 1:
            return i
        
    return -1
    
def generate_neighbor(current_state):
    neighbor = copy.deepcopy(current_state) #Deveria ter feito em C++
    
    selected_task = random.randint(0, len(neighbor[0]) - 1)
    
    machine_from = find_task(selected_task, neighbor)
    
    if machine_from == -1:
        return neighbor
    
    machine_to = machine_from
    
    while machine_to == machine_from:
        machine_to = random.randint(0, len(neighbor) - 1)
    
    neighbor[machine_from][selected_task] = 0
    neighbor[machine_to][selected_task] = 1
    
    return neighbor

def simulated_annealing(tasks, machines, initial_temp, cooling_rate, max_iterations):
    current_solution = create_initial_solution(tasks, machines)
    current_cost = calculate_makespan(tasks, current_solution)
    
    best_solution = current_solution
    best_cost = current_cost
    
    temperature = initial_temp
    
    for i in range(max_iterations):
        
        temperature *= cooling_rate
        
        candidate_solution = generate_neighbor(current_solution)
        candidate_cost = calculate_makespan(tasks, candidate_solution)
        
        #Para fugir de mínimos locais, o SA usa uma probabilidade para aceitar soluções piores.
        #O random.random() gera um número aleatório entre 0 e 1, que é comparado com a probabilidade de aceitação.
        #A probabilidade de aceitação reduz conforme a temperatura diminui.
        #A ideia é que no começo nós exploramos o espaço de possibilidades, por isso aceitamos soluções piores mais facilmente,
        #Mas conforme a temperatura diminui, vamos nos aproximando de uma solução ótima, e a probabilidade de aceitar soluções piores diminui.
        if candidate_cost < best_cost or random.random() < math.exp((current_cost - candidate_cost) / temperature):
            current_solution = candidate_solution
            current_cost = candidate_cost
            
            if current_cost < best_cost:
                best_solution = current_solution
                best_cost = current_cost
                
        if i % 100 == 0:
            print(f"Iteration {i}, Current Cost: {current_cost}, Best Cost: {best_cost}, Temperature: {temperature:.4f}")
                
    
    return best_solution, best_cost

tasks = [20, 10, 7, 5]
machines = 2

print(simulated_annealing(tasks, machines, initial_temp=1000, cooling_rate=0.95, max_iterations=10000))