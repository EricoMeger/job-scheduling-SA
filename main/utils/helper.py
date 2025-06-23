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
        plt.title('Evolução do Makespan')
        
        plt.subplot(1, 2, 2)
        plt.plot(temperature_history)
        plt.xlabel('Iteração')
        plt.ylabel('Temperatura')
        plt.title('Evolução da Temperatura')
        
        plt.tight_layout()
        plt.show()