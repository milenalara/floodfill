# Flood Fill - Colorindo Regiões de um Terreno com Obstáculos

## Descrição

Este projeto implementa o algoritmo **Flood Fill** para mapear automaticamente um terreno 2D composto por células navegáveis (0) e obstáculos (1). A cada região conectada encontrada, é atribuído um número correspondente a uma "cor".

## Objetivo

Facilitar a visualização e o planejamento de robôs autônomos em terrenos com múltiplas regiões desconectadas por obstáculos.

## Como funciona

- O grid é percorrido automaticamente a partir de qualquer célula com valor `0`.
- O algoritmo Flood Fill identifica todas as células navegáveis conectadas ortogonalmente.
- Cada região é colorida com um número diferente (2, 3, 4...).
- Obstáculos (`1`) e áreas já coloridas (>=2) são respeitados.

## Execução

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
