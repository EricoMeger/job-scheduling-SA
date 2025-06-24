# Job Scheduling com Simulated Annealing

Este projeto implementa uma solução para o problema de escalonamento de tarefas (Job Scheduling) utilizando o algoritmo de Simulated Annealing (SA).

## Descrição
O objetivo é distribuir um conjunto de tarefas entre máquinas de forma que o tempo total de execução (makespan) seja minimizado. O algoritmo de Simulated Annealing é utilizado para buscar uma solução próxima do ótimo global, evitando mínimos locais.

## Estrutura do Projeto
```
job-scheduling-SA/
├─ main/
│  ├─ sa/
│  │  └─ simulated_annealing.py
│  ├─ scheduler/
│  │  └─ job_scheduler.py
│  ├─ utils/
│  │  └─ helper.py
│  └─ main.py
├─ .gitignore
├─ LICENSE
├─ output.txt
├─ README.md
└─ requirements.txt
```

## Como Executar
1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
2. Execute o script principal:
   ```bash
   python3 main/main.py
   ```

## Parâmetros Principais
- **tasks**: Número de tarefas geradas aleatoriamente.
- **machines**: Número de máquinas disponíveis.
- **initial_temp**: Temperatura inicial do SA.
- **v**: Fator de resfriamento (número de ciclos até que haja a resfriação).
- **max_iterations**: Número máximo de iterações.

Esses parâmetros podem ser ajustados diretamente no arquivo `main.py`.

## Resultados
- O makespan ao longo das iterações e a evolução da temperatura são exibidos em gráficos.
- O resultado final é salvo em `output.txt`.

## Referências

### Job Scheduling
- [Identical Machines Scheduling (Wikipedia)](https://en.wikipedia.org/wiki/Identical-machines_scheduling)
- [Job-shop Scheduling (Wikipedia)](https://en.wikipedia.org/wiki/Job-shop_scheduling)
- [Optimal Job Scheduling (Wikipedia)](https://en.wikipedia.org/wiki/Optimal_job_scheduling)

### Simulated Annealing
- [A Simulated Annealing Algorithm for Job Shop Scheduling Problem (SCIRP)](https://www.scirp.org/journal/paperinformation?paperid=78834)
- [Simulated Annealing with Python (Nathan's Blog)](https://nathan.fun/posts/2020-05-14/simulated-annealing-with-python/)
- [Optimization by Simulated Annealing (Science)](https://www.science.org/doi/10.1126/science.220.4598.671)

---

Autor: [Érico Meger](https://github.com/EricoMeger)
