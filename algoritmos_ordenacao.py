"""
Algoritmos de Ordenação: Bubble Sort
Complexidade:
- Bubble Sort: O(n²) no pior caso
- sort() do Python: O(n log n) (Timsort)
"""


def bubble_sort(lista):
    """
    Implementação do Bubble Sort.
    Ordena a lista em ordem crescente.
    
    Args:
        lista: Lista de números para ordenar
        
    Returns:
        list: Nova lista ordenada (não modifica a original)
    """
    # Cria uma cópia para não modificar a lista original
    lista_copia = lista.copy()
    n = len(lista_copia)
    
    for i in range(n):
        # Flag para otimização: se não houver trocas, a lista já está ordenada
        houve_troca = False
        
        for j in range(0, n - i - 1):
            if lista_copia[j] > lista_copia[j + 1]:
                # Troca os elementos adjacentes
                lista_copia[j], lista_copia[j + 1] = lista_copia[j + 1], lista_copia[j]
                houve_troca = True
        
        # Se não houve trocas, a lista já está ordenada
        if not houve_troca:
            break
    
    return lista_copia


def sort_python(lista):
    """
    Usa o sort() nativo do Python para ordenação.
    
    Args:
        lista: Lista de números para ordenar
        
    Returns:
        list: Nova lista ordenada (não modifica a original)
    """
    lista_copia = lista.copy()
    lista_copia.sort()
    return lista_copia
