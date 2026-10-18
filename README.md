# Projeto de Algoritmos de Busca e Ordenação

Este projeto implementa e compara diferentes algoritmos de busca e ordenação em Python, com foco em entender a complexidade de tempo.

## 📋 Conteúdo

### 1. Algoritmos de Busca
- **Busca Linear**: O(n) - Percorre a lista elemento por elemento
- **Busca Binária**: O(log n) - Divide a lista ao meio repetidamente (requer lista ordenada)

### 2. Algoritmos de Ordenação
- **Bubble Sort**: O(n²) no pior caso - Compara e troca elementos adjacentes
- **sort() do Python**: O(n log n) - Algoritmo Timsort altamente otimizado

### 3. Testes com Pytest
Testes abrangentes que cobrem:
- Listas vazias
- Números repetidos
- Valores inexistentes
- Listas já ordenadas
- Listas em ordem reversa
- Números negativos

## 🚀 Como Usar

### Instalar dependências
```bash
pip install -r requirements.txt
```

### Executar os testes
```bash
pytest test_algoritmos.py -v
```

### Exemplo de uso
```python
from algoritmos_busca import busca_linear, busca_binaria
from algoritmos_ordenacao import bubble_sort, sort_python

# Busca
lista = [5, 3, 8, 1, 9, 2]
print(busca_linear(lista, 8))  # Saída: 2

lista_ordenada = [1, 2, 3, 5, 8, 9]
print(busca_binaria(lista_ordenada, 8))  # Saída: 4

# Ordenação
lista = [5, 3, 8, 1, 9, 2]
print(bubble_sort(lista))  # Saída: [1, 2, 3, 5, 8, 9]
print(sort_python(lista))   # Saída: [1, 2, 3, 5, 8, 9]
```

## 📁 Estrutura do Projeto

```
projeto algoritimo/
├── algoritmos_busca.py      # Implementações de busca linear e binária
├── algoritmos_ordenacao.py  # Implementações de ordenação
├── test_algoritmos.py       # Testes com pytest
├── requirements.txt         # Dependências do projeto
└── README.md               # Este arquivo
```

## 🎯 Conceitos Aprendidos

- **Complexidade de Tempo**: Entender como o tamanho da entrada afeta o desempenho
- **O(n)**: Tempo linear - proporcional ao tamanho da entrada
- **O(log n)**: Tempo logarítmico - muito mais eficiente para grandes conjuntos
- **O(n²)**: Tempo quadrático - torna-se lento com grandes conjuntos
- **O(n log n)**: Tempo eficiente para ordenação
