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
- **patience**: Número máximo de iterações consecutivas permitidas sem melhoria no makespan antes de encerrar a execução antecipadamente.

Esses parâmetros podem ser ajustados diretamente no arquivo `main.py`.

## Resfriamento Adaptativo com VCF

Este projeto utiliza o método de resfriamento adaptativo VCF (Variable Cooling Factor) para controlar a temperatura no algoritmo de Simulated Annealing. Ao contrário de um fator de resfriamento fixo, o VCF ajusta dinamicamente o ritmo de resfriamento a cada ciclo, simulando a forma como partículas perdem energia na natureza, rapidamente no início e mais lentamente ao longo do tempo.

### Fórmula

A temperatura é atualizada a cada ciclo k, de acordo com:
    
$$
\Phi_k = \left(1 + \frac{1}{\sqrt{k(v + 1) + v}}\right)^{-1}, T_{k+1} = \Phi_k \cdot T_k
$$

Onde:
- $\Phi_k$: fator de resfriamento variável no ciclo k
- $v$: número de iterações por ciclo de temperatura
- $T_k$: temperatura atual
- $T_{k+1}$: nova temperatura após o ciclo

### Intuição

- No início (ciclos pequenos), $\Phi_k$ é menor → a temperatura cai mais rapidamente.
- Conforme $k$ cresce, $\Phi_k$ se aproxima de 1 → o resfriamento desacelera.
- Isso garante uma transição suave da exploração global (aceitação de soluções piores) para refinamento local (busca precisa).

## Resultados
- O makespan ao longo das iterações e a evolução da temperatura são exibidos em gráficos.
- O resultado final é salvo em `output.txt`.

## Referências

### Job Scheduling
- [Identical Machines Scheduling (Wikipedia)](https://en.wikipedia.org/wiki/Identical-machines_scheduling)
- [Job-shop Scheduling (Wikipedia)](https://en.wikipedia.org/wiki/Job-shop_scheduling)
- [Optimal Job Scheduling (Wikipedia)](https://en.wikipedia.org/wiki/Optimal_job_scheduling)

### Simulated Annealing
- [An Optimal Cooling Schedule Using a Simulated Annealing Based Approach (SCIRP)](https://www.scirp.org/journal/paperinformation?paperid=78834)
- [Simulated Annealing with Python (Nathan's Blog)](https://nathan.fun/posts/2020-05-14/simulated-annealing-with-python/)
- [Optimization by Simulated Annealing (Science)](https://www.science.org/doi/10.1126/science.220.4598.671)

---

Autor: [Érico Meger](https://github.com/EricoMeger)
