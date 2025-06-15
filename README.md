# Flood Fill

## Descrição

Este é um trabalho desenvolvido para a disciplina de Fundamentos de Projeto e Análise de Algoritmos, ministrada pelo professor João Paulo Aramuni em 2025/1 no bacharelado em Engenharia de Software da PUC Minas.

Consiste na implementação em Python do algoritmo **Flood Fill** para mapear automaticamente um terreno 2D composto por células navegáveis (0) e obstáculos (1). A cada região conectada encontrada, é atribuído um número correspondente a uma "cor".

O arquivo main.py contém o código com a implementação.

## Objetivo

Facilitar a visualização e o planejamento de robôs autônomos em terrenos com múltiplas regiões desconectadas por obstáculos.

## Como rodar o projeto

1. Clone o repositório com o comando no terminal `git clone git@github.com:milenalara/floodfill.git`

2. Abra o diretório no terminal e execute com Python 3: `python main.py`


## Explicação das funções

- O grid é percorrido automaticamente a partir de qualquer célula com valor `0`.
- O algoritmo Flood Fill identifica todas as células navegáveis conectadas ortogonalmente.
- Cada região é colorida com um número diferente (2, 3, 4...).
- Obstáculos (`1`) e áreas já coloridas (>=2) são respeitados.


```py
def flood_fill(grid, x, y, new_color):
    # Se a célula inicial não for navegável, não faz nada
    if grid[x][y] != 0:
        return
    # Inicializa uma pilha com a célula inicial
    stack = [(x, y)]
    # Obtém o número de linhas e colunas do grid
    rows, cols = len(grid), len(grid[0])
    
    # Enquanto houver células na pilha
    while stack:
        # Remove a última célula inserida (busca em profundidade)
        cx, cy = stack.pop()
        # Se for navegável, pinta com a nova cor
        if grid[cx][cy] == 0:
            grid[cx][cy] = new_color
            # Verifica os vizinhos ortogonais: cima, baixo, esquerda, direita
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                nx, ny = cx + dx, cy + dy
                # Se o vizinho está dentro dos limites e for navegável, adiciona à pilha
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                    stack.append((nx, ny))

# Encontra a próxima célula navegável (valor 0) para iniciar o próximo preenchimento
def find_next_start(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                return i, j
    return None  # Retorna None se não houver mais células navegáveis

# Imprime o grid de forma legível no terminal
def print_grid(grid):
    for row in grid:
        print(" ".join(str(cell) for cell in row))
        
def main():
    # Grid de exemplo com obstáculos (1) e regiões livres (0)
    grid = [
        [0, 0, 1, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 1, 1, 1],
        [1, 1, 0, 0, 0]
    ]

    # Exibe o grid original
    print("Grid inicial:")
    print_grid(grid)

    # Cor inicial para preenchimento (2 = primeira região, 3 = próxima, etc.)
    color = 2

    # Enquanto houver regiões navegáveis, aplica o Flood Fill
    while True:
        start = find_next_start(grid)
        if not start:
            break  # Encerra quando não há mais regiões navegáveis

        x, y = start
        flood_fill(grid, x, y, color)
        color += 1  # Incrementa a cor para a próxima região

    # Exibe o grid após preenchimento completo
    print("\nGrid preenchido:")
    print_grid(grid)
```

## Como rodas o projeto

Execute com Python 3:

```bash
python main.py
```

## Exemplo

### Entrada:

```
0 0 1 0 0
0 1 1 0 0
0 0 1 1 1
1 1 0 0 0
```

### Saída:

```
2 2 1 3 3
2 1 1 3 3
2 2 1 1 1
1 1 4 4 4
```
