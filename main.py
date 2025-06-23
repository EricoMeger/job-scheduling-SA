def initialize_assignments(tasks, machines):
    assignments = []
    for _ in range(machines):
        assignments.append([0] * len(tasks))

    return assignments

tasks = [1, 2, 3, 4, 5]
machines = 2
machine_assignments = initialize_assignments(tasks, machines)

print(machine_assignments)