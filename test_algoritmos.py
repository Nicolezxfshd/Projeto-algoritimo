"""
Testes para algoritmos de busca e ordenação usando pytest.
Testa casos: lista vazia, números repetidos, valores inexistentes, listas já ordenadas.
"""
import pytest
from algoritmos_busca import busca_linear, busca_binaria
from algoritmos_ordenacao import bubble_sort, sort_python


# ==================== TESTES DE BUSCA LINEAR ====================

def test_busca_linear_encontrado():
    """Testa busca linear com valor existente."""
    lista = [5, 3, 8, 1, 9, 2]
    assert busca_linear(lista, 8) == 2
    assert busca_linear(lista, 5) == 0
    assert busca_linear(lista, 2) == 5


def test_busca_linear_nao_encontrado():
    """Testa busca linear com valor inexistente."""
    lista = [5, 3, 8, 1, 9, 2]
    assert busca_linear(lista, 7) == -1
    assert busca_linear(lista, 100) == -1


def test_busca_linear_lista_vazia():
    """Testa busca linear em lista vazia."""
    assert busca_linear([], 5) == -1


def test_busca_linear_repetidos():
    """Testa busca linear com números repetidos."""
    lista = [5, 3, 8, 3, 9, 2]
    assert busca_linear(lista, 3) == 1  # Retorna primeira ocorrência


def test_busca_linear_unico_elemento():
    """Testa busca linear com único elemento."""
    assert busca_linear([42], 42) == 0
    assert busca_linear([42], 10) == -1


# ==================== TESTES DE BUSCA BINÁRIA ====================

def test_busca_binaria_encontrado():
    """Testa busca binária com valor existente."""
    lista = [1, 2, 3, 5, 8, 9]
    assert busca_binaria(lista, 8) == 4
    assert busca_binaria(lista, 1) == 0
    assert busca_binaria(lista, 9) == 5


def test_busca_binaria_nao_encontrado():
    """Testa busca binária com valor inexistente."""
    lista = [1, 2, 3, 5, 8, 9]
    assert busca_binaria(lista, 7) == -1
    assert busca_binaria(lista, 100) == -1


def test_busca_binaria_lista_vazia():
    """Testa busca binária em lista vazia."""
    assert busca_binaria([], 5) == -1


def test_busca_binaria_repetidos():
    """Testa busca binária com números repetidos."""
    lista = [1, 2, 3, 3, 5, 8]
    resultado = busca_binaria(lista, 3)
    assert resultado in [2, 3]  # Pode retornar qualquer uma das ocorrências


def test_busca_binaria_unico_elemento():
    """Testa busca binária com único elemento."""
    assert busca_binaria([42], 42) == 0
    assert busca_binaria([42], 10) == -1


# ==================== TESTES DE BUBBLE SORT ====================

def test_bubble_sort_basico():
    """Testa bubble sort com lista básica."""
    lista = [5, 3, 8, 1, 9, 2]
    resultado = bubble_sort(lista)
    assert resultado == [1, 2, 3, 5, 8, 9]
    # Verifica que a lista original não foi modificada
    assert lista == [5, 3, 8, 1, 9, 2]


def test_bubble_sort_vazia():
    """Testa bubble sort com lista vazia."""
    assert bubble_sort([]) == []


def test_bubble_sort_unico():
    """Testa bubble sort com único elemento."""
    assert bubble_sort([42]) == [42]


def test_bubble_sort_ordenada():
    """Testa bubble sort com lista já ordenada."""
    lista = [1, 2, 3, 4, 5]
    assert bubble_sort(lista) == [1, 2, 3, 4, 5]


def test_bubble_sort_reversa():
    """Testa bubble sort com lista em ordem reversa."""
    lista = [5, 4, 3, 2, 1]
    assert bubble_sort(lista) == [1, 2, 3, 4, 5]


def test_bubble_sort_repetidos():
    """Testa bubble sort com números repetidos."""
    lista = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    assert bubble_sort(lista) == [1, 1, 2, 3, 4, 5, 5, 6, 9]


def test_bubble_sort_negativos():
    """Testa bubble sort com números negativos."""
    lista = [3, -1, 4, -5, 0]
    assert bubble_sort(lista) == [-5, -1, 0, 3, 4]


# ==================== TESTES DE SORT PYTHON ====================

def test_sort_python_basico():
    """Testa sort() do Python com lista básica."""
    lista = [5, 3, 8, 1, 9, 2]
    resultado = sort_python(lista)
    assert resultado == [1, 2, 3, 5, 8, 9]
    # Verifica que a lista original não foi modificada
    assert lista == [5, 3, 8, 1, 9, 2]


def test_sort_python_vazia():
    """Testa sort() do Python com lista vazia."""
    assert sort_python([]) == []


def test_sort_python_repetidos():
    """Testa sort() do Python com números repetidos."""
    lista = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    assert sort_python(lista) == [1, 1, 2, 3, 4, 5, 5, 6, 9]


# ==================== TESTES COMPARATIVOS ====================

def test_comparacao_ordenacao():
    """Compara resultados do bubble sort e sort() do Python."""
    lista = [5, 3, 8, 1, 9, 2, 7, 4, 6]
    assert bubble_sort(lista) == sort_python(lista)


def test_comparacao_busca():
    """Compara resultados da busca linear e binária em lista ordenada."""
    lista = [1, 2, 3, 5, 8, 9]
    assert busca_linear(lista, 8) == 4
    assert busca_binaria(lista, 8) == 4
