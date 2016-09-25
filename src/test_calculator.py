from unittest import TestCase
from .calculator import Calculator

__author__ = 'Luis_Sebastian_Talero'


class TestCalculator(TestCase):
    def test_sumar(self):
        self.assertEqual(Calculator.sumar(""), 0, "Empty String")

    def test_sumar_una_cadena(self):
        self.assertEqual(Calculator.sumar("1"), 1, "One number")
        self.assertEqual(Calculator.sumar("2"), 2, "One number")

    def test_sumar_dos_cadenas(self):
        self.assertEqual(Calculator.sumar("1,1"), 2, "Two numbers")
        self.assertEqual(Calculator.sumar("2,1"), 3, "Two numbers")

    def test_sumar_dos_cadenas(self):
        self.assertEqual(Calculator.sumar("1,1,1"), 3, "More than two")
        self.assertEqual(Calculator.sumar("1,1,2"), 4, "More than two")