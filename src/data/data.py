import pytest

# Intentamos importar la clase Data de manera robusta
try:
    from src.data.data import Data
except ModuleNotFoundError:
    raise ImportError("No se pudo encontrar el módulo 'Data'. Verifica la ruta y que 'src' esté en el PYTHONPATH.")

class TestData:
    def setup_method(self):
        self.data = Data()

    def test_invertir_lista(self):
        assert self.data.invertir_lista([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
        assert self.data.invertir_lista([]) == []
        assert self.data.invertir_lista([42]) == [42]
        assert self.data.invertir_lista(["a", "b", "c"]) == ["c", "b", "a"]

    def test_buscar_elemento(self):
        assert self.data.buscar_elemento([10, 20, 30, 40, 50], 30) == 2
        assert self.data.buscar_elemento([10, 20, 30, 40, 50], 60) == -1
        assert self.data.buscar_elemento([10, 20, 30, 20, 50], 20) == 1
        assert self.data.buscar_elemento([], 42) == -1

    def test_eliminar_duplicados(self):
        assert self.data.eliminar_duplicados([1, 2, 2, 3, 4, 4, 5]) == [1, 2, 3, 4, 5]
        assert self.data.eliminar_duplicados([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
        assert self.data.eliminar_duplicados([]) == []
        assert self.data.eliminar_duplicados([1, "a", 1, "a", True]) == [1, "a", True]

    def test_merge_ordenado(self):
        assert self.data.merge_ordenado([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
        assert self.data.merge_ordenado([], [1, 2, 3]) == [1, 2, 3]
        assert self.data.merge_ordenado([], []) == []
        assert self.data.merge_ordenado([1, 2, 3], [1, 3, 5]) == [1, 1, 2, 3, 3, 5]

    def test_rotar_lista(self):
        assert self.data.rotar_lista([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]
        assert self.data.rotar_lista([1, 2, 3], 5) == [2, 3, 1]
        assert self.data.rotar_lista([1, 2, 3], 0) == [1, 2, 3]
        assert self.data.rotar_lista([], 3) == []

    def test_encuentra_numero_faltante(self):
        assert self.data.encuentra_numero_faltante([1, 2, 4, 5]) == 3
        assert self.data.encuentra_numero_faltante([2, 3, 4, 5]) == 1
        assert self.data.encuentra_numero_faltante([1, 2, 3, 4]) == 5

    def test_es_subconjunto(self):
        assert self.data.es_subconjunto([1, 2], [1, 2, 3, 4]) is True
        assert self.data.es_subconjunto([1, 5], [1, 2, 3, 4]) is False
        assert self.data.es_subconjunto([1, 2, 3], [1, 2, 3]) is True
        assert self.data.es_subconjunto([], [1, 2, 3]) is True

    def test_implementar_pila(self):
        pila = self.data.implementar_pila()
        assert "push" in pila and "pop" in pila and "peek" in pila and "is_empty" in pila
        assert pila["is_empty"]() is True
        assert pila["peek"]() == 1
        pila 
        ["peek"]() == 2
        assert pila["pop"]() == 2
        assert pila["pop"]() == 1
        assert pila["is_empty"]() is True

    def test_implementar_cola(self):
        cola = self.data.implementar_cola()
        assert "enqueue" in cola and "dequeue" in cola and "peek" in cola and "is_empty" in cola
        assert cola["is_empty"]() is True
        cola 
        assert cola 
        cola 
        assert cola["peek"]() == 1
        assert cola["dequeue"]() == 1
        assert cola["dequeue"]() == 2
        assert cola["is_empty"]() is True

    def test_matriz_transpuesta(self):
        assert self.data.matriz_transpuesta([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]
        assert self.data.matriz_transpuesta([[1, 2], [3, 4]]) == [[1, 3], [2, 4]]
        assert self.data.matriz_transpuesta([[5]]) == [[5]]
        assert self.data.matriz_transpuesta([]) == []

