import random
import matplotlib.pyplot as plt

class Helper:
    @staticmethod
    def generate_tasks(num_tasks):
        tasks = []
        
        for _ in range(num_tasks):
            tasks.append(random.randint(1, 99))
            
        return tasks
    
    @staticmethod
    #O limite inferior serve só pra ter uma ideia de qual é o valor mínimo possível para o makespan.
    #Não necessariamente vai ser possível atingir esse valor. Esse é o melhor cenário possível, e o mínimo teórico.
    def get_lower_bound(tasks, machines):
        return sum(tasks) / machines
    
    @staticmethod
    def plot_results(makespan_history, temperature_history):
        plt.figure(figsize=(12, 5))
        
        plt.subplot(1, 2, 1)
        plt.plot(makespan_history)
        plt.xlabel('Iteração')
        plt.ylabel('Makespan')
        plt.title('Mudança do Makespan ao longo das iterações')
        
        plt.subplot(1, 2, 2)
        plt.plot(temperature_history)
        plt.xlabel('Iteração')
        plt.ylabel('Temperatura')
        plt.title('Mudança de Temperatura ao longo das iterações')
        
        plt.tight_layout()
        plt.show()

    @staticmethod
    def write_solution(solution, num_tasks, machines, makespan, temperature, iterations, filename='output.txt'):
        with open(filename, 'w') as file:
            file.write("Simulated Annealing Job Scheduling Results\n")
            file.write("---------------------------------------------------------\n\n")

            file.write(f"Número de Tarefas: {num_tasks}\n")
            file.write(f"Número de Máquinas: {machines}\n")
            file.write(f"Melhor Makespan encontrado: {makespan[-1]}\n")
            file.write(f"Temperatura Inicial: {temperature[0]:.2f}\n")
            file.write(f"Temperatura Final: {temperature[-1]:.2f}\n")
            file.write(f"Iterações realizadas: {iterations}\n")

            file.write("\nDistribuição das Tarefas:\n\n")

            for i in range(len(solution)):
                file.write(f"Máquina {i + 1}: \n")
                file.write("Tarefas: ")
                tasks = [j + 1 for j in range(len(solution[i])) if solution[i][j] == 1]
                file.write(", ".join(map(str, tasks)) + "\n\n")