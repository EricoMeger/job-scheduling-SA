import random

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
    selected_task = random.randint(0, len(current_state) - 1)
    
    machine_from = find_task(selected_task, current_state)
    
    if machine_from == -1:
        return current_state
    
    machine_to = machine_from
    
    while machine_to == machine_from:
        machine_to = random.randint(0, len(current_state) - 1)
    
    current_state[machine_from][selected_task] = 0
    current_state[machine_to][selected_task] = 1
    
    return current_state

tasks = [1, 2, 3, 4, 5]
machines = 2
machine_assignments = create_initial_solution(tasks, machines)

print(machine_assignments)

generate_neighbor(machine_assignments)

print(machine_assignments)