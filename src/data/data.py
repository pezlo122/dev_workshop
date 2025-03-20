import pytest
from src.data_nslm import Data


class TestData:
    def setup_method(self):
        self.data = Data()
    
    def test_invertir_lista(self):
        test_cases = [
            ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
            ([], []),
            ([42], [42]),
            (["a", "b", "c"], ["c", "b", "a"])
        ]
        
        for entrada, esperado in test_cases:
            resultado = self.data.invertir_lista(entrada)
            print(f"Entrada: {entrada} -> Resultado: {resultado} (Esperado: {esperado})")
            assert resultado == esperado
    
    def test_buscar_elemento(self):
        test_cases = [
            ([10, 20, 30, 40, 50], 30, 2),
            ([10, 20, 30, 40, 50], 60, -1),
            ([10, 20, 30, 20, 50], 20, 1),
            ([], 42, -1)
        ]
        
        for lista, elemento, esperado in test_cases:
            resultado = self.data.buscar_elemento(lista, elemento)
            print(f"Lista: {lista}, Elemento: {elemento} -> Resultado: {resultado} (Esperado: {esperado})")
            assert resultado == esperado
    
    def test_eliminar_duplicados(self):
        test_cases = [
            ([1, 2, 2, 3, 4, 4, 5], [1, 2, 3, 4, 5]),
            ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
            ([], []),
            ([1, "a", 1, "a", True], [1, "a", True])
        ]
        
        for entrada, esperado in test_cases:
            resultado = self.data.eliminar_duplicados(entrada)
            print(f"Entrada: {entrada} -> Resultado: {resultado} (Esperado: {esperado})")
            assert resultado == esperado
    
    def test_merge_ordenado(self):
        test_cases = [
            ([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]),
            ([], [1, 2, 3], [1, 2, 3]),
            ([], [], []),
            ([1, 2, 3], [1, 3, 5], [1, 1, 2, 3, 3, 5])
        ]
        
        for lista1, lista2, esperado in test_cases:
            resultado = self.data.merge_ordenado(lista1, lista2)
            print(f"Lista 1: {lista1}, Lista 2: {lista2} -> Resultado: {resultado} (Esperado: {esperado})")
            assert resultado == esperado
    
    def test_matriz_transpuesta(self):
        test_cases = [
            ([[1, 2, 3], [4, 5, 6]], [[1, 4], [2, 5], [3, 6]]),
            ([[1, 2], [3, 4]], [[1, 3], [2, 4]]),
            ([[5]], [[5]]),
            ([], [])
        ]
        
        for entrada, esperado in test_cases:
            resultado = self.data.matriz_transpuesta(entrada)
            print(f"Matriz: {entrada} -> Resultado: {resultado} (Esperado: {esperado})")
            assert resultado == esperado

