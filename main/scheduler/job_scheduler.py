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