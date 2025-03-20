import pytest
import math
from src.geometric.geometric import Geometria

class TestGeometria:
    def setup_method(self):
        self.geometria = Geometria()
    
    def test_area_rectangulo(self):
        assert self.geometria.area_rectangulo(5, 4) == 20
        assert self.geometria.area_rectangulo(2.5, 3) == 7.5
        assert self.geometria.area_rectangulo(0, 5) == 0
        assert self.geometria.area_rectangulo(-3, 4) == 0 
    
    def test_perimetro_rectangulo(self):
        assert self.geometria.perimetro_rectangulo(5, 4) == 18
        assert self.geometria.perimetro_rectangulo(2.5, 3) == 11
        assert self.geometria.perimetro_rectangulo(2, 2) == 8
        assert self.geometria.perimetro_rectangulo(-3, 4) == 0  
    
    def test_perimetro_triangulo(self):
        assert self.geometria.perimetro_triangulo(5, 5, 5) == 15
        assert self.geometria.perimetro_triangulo(3, 4, 5) == 12
        assert self.geometria.perimetro_triangulo(2.5, 3.5, 4.5) == 10.5 
    
    def test_area_circulo(self):
        assert round(self.geometria.area_circulo(2), 2) == 12.57
        assert round(self.geometria.area_circulo(1.5), 2) == 7.07
        assert self.geometria.area_circulo(0) == 0
        assert self.geometria.area_circulo(-2) == 0 
        
    def test_perimetro_circulo(self):
        assert round(self.geometria.perimetro_circulo(2), 2) == 12.57
        assert round(self.geometria.perimetro_circulo(1.5), 2) == 9.42
        assert self.geometria.perimetro_circulo(0) == 0
        assert self.geometria.perimetro_circulo(-2) == 0 
    
    def test_es_triangulo_valido(self):
        assert self.geometria.es_triangulo_valido(3, 4, 5) == True
        assert self.geometria.es_triangulo_valido(1, 2, 10) == False
        assert self.geometria.es_triangulo_valido(-1, 4, 5) == False
        assert self.geometria.es_triangulo_valido(0, 5, 5) == False  
   
