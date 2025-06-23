def generate_tasks(num_tasks):
    tasks = []
    
    for _ in range(num_tasks):
        tasks.append(random.randint(1, 99))
        
    return tasks

#O limite inferior serve só pra ter uma ideia de qual é o valor mínimo possível para o makespan.
#Não necessariamente vai ser possível atingir esse valor. Esse é o melhor cenário possível, e o mínimo teórico.
def get_lower_bound(tasks, machines):
    return sum(tasks) / machines