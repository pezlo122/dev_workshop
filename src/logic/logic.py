import pytest
from src.logic.logic import Logica

class TestLogica:
    def setup_method(self):
        self.logica = Logica()
    
    def test_AND(self):
        assert self.logica.AND(True, True) == True
        assert self.logica.AND(True, False) == False
        assert self.logica.AND(False, True) == False
        assert self.logica.AND(False, False) == False
    
    def test_OR(self):
        assert self.logica.OR(True, True) == True
        assert self.logica.OR(True, False) == True
        assert self.logica.OR(False, True) == True
        assert self.logica.OR(False, False) == False
    
    def test_NOT(self):
        assert self.logica.NOT(True) == False
        assert self.logica.NOT(False) == True
    
    def test_XOR(self):
        assert self.logica.XOR(True, True) == False
        assert self.logica.XOR(True, False) == True
        assert self.logica.XOR(False, True) == True
        assert self.logica.XOR(False, False) == False
    
    def test_NAND(self):
        assert self.logica.NAND(True, True) == False
        assert self.logica.NAND(True, False) == True
        assert self.logica.NAND(False, True) == True
        assert self.logica.NAND(False, False) == True
    
    def test_NOR(self):
        assert self.logica.NOR(True, True) == False
        assert self.logica.NOR(True, False) == False
        assert self.logica.NOR(False, True) == False
        assert self.logica.NOR(False, False) == True
    
    def test_XNOR(self):
        assert self.logica.XNOR(True, True) == True
        assert self.logica.XNOR(True, False) == False
        assert self.logica.XNOR(False, True) == False
        assert self.logica.XNOR(False, False) == True
    
    def test_implicacion(self):
        assert self.logica.implicacion(True, True) == True
        assert self.logica.implicacion(True, False) == False
        assert self.logica.implicacion(False, True) == True
        assert self.logica.implicacion(False, False) == True
    
    def test_bi_implicacion(self):
        assert self.logica.bi_implicacion(True, True) == True
        assert self.logica.bi_implicacion(True, False) == False
        assert self.logica.bi_implicacion(False, True) == False
        assert self.logica.bi_implicacion(False, False) == True
