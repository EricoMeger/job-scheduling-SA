import copy
import random
import math

from scheduler.job_scheduler import JobScheduler

class SimulatedAnnealing:
    def __init__(self, tasks, machines, initial_temp=1000, v=20, max_iterations=10000, patience=500):

        self.scheduler = JobScheduler(tasks, machines)

        self.tasks = tasks
        self.machines = machines
        self.initial_temp = initial_temp
        self.v = v
        self.max_iterations = max_iterations
        self.patience = patience

    def generate_neighbor(self, current_state):
        neighbor = copy.deepcopy(current_state) #Deveria ter feito em C++
        
        selected_task = random.randint(0, len(neighbor[0]) - 1)
        
        machine_from = self.scheduler.find_task(selected_task, neighbor)
        
        if machine_from == -1:
            return neighbor
        
        machine_to = machine_from
        
        while machine_to == machine_from:
            machine_to = random.randint(0, len(neighbor) - 1)
        
        neighbor[machine_from][selected_task] = 0
        neighbor[machine_to][selected_task] = 1
        
        return neighbor

    # Função de resfriamento adaptativo baseada no método VCF (Variable Cooling Factor)
    # implementada com base no paper "An Optimal Cooling Schedule Using a Simulated Annealing Based Approach"
    
    #fórmula:
    #     phi_k = (1 + 1 / sqrt(k*(v + 1) + v))^-1
    # onde:
    #     k = número do ciclo de resfriamento (começa em 1, cresce a cada 'v' iterações)
    #     v = número fixo de iterações por ciclo de temperatura (vc q define)

    # Isso cria um fator de resfriamento dinâmico (phi_k) que começa pequeno (resfriamento rápido)
    # e vai aumentando com o tempo (resfriamento mais lento), permitindo uma transição gradual
    # da exploração (busca global) para a intensificação (busca local).

    def phi(self, k, v):
        return (1 + 1 / math.sqrt(k * (v + 1) + v)) ** -1

    def optimize_makespan(self):
        current_solution = self.scheduler.create_initial_solution()
        current_cost = self.scheduler.calculate_makespan(current_solution)
        
        best_solution = current_solution
        best_cost = current_cost
        
        temperature = self.initial_temp
        
        makespan_history = []
        temperature_history = []
        
        stagnation_counter = 0
        
        for i in range(self.max_iterations):
            #Atualiza a temperatura somente a cada v iterações
            if i % self.v == 0:
                k = i // self.v + 1
                temperature *= self.phi(k, self.v)
            
            candidate_solution = self.generate_neighbor(current_solution)
            candidate_cost = self.scheduler.calculate_makespan(candidate_solution)
            
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
                    stagnation_counter = 0
                else:
                    stagnation_counter += 1
            
            makespan_history.append(best_cost)
            temperature_history.append(temperature)
            
            if stagnation_counter >= self.patience:
                print(f"Parando mais cedo na iteração {i} devido à estagnação.")
                break
                            
        return best_solution, best_cost, makespan_history, temperature_history