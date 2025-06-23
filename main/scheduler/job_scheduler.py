
class JobScheduler:
    def __init__(self, tasks, machines):
        self.tasks = tasks
        self.machines = machines
        self.assignments = self.create_initial_solution()

    def initialize_assignments(self):
        assignments = []
        for _ in range(self.machines):
            assignments.append([0] * len(self.tasks))

        return assignments

    def create_initial_solution(self):
        assignments = self.initialize_assignments()
        for i in range(len(self.tasks)):
            assignments[i % self.machines][i] = 1
        return assignments

    def calculate_makespan(self, assignments):
        cost = [0] * len(assignments)

        for i in range(len(assignments)):
            for j in range(len(self.tasks)):
                if(assignments[i][j] == 1):
                    cost[i] += self.tasks[j]

        return max(cost)

    def find_task(self, selected_task, state):
        for i in range(len(state)):
            if state[i][selected_task] == 1:
                return i
            
        return -1