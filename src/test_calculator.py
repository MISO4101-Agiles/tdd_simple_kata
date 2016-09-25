from unittest import TestCase
from .calculator import Calculator

__author__ = 'Luis_Sebastian_Talero'


class TestCalculator(TestCase):
    def test_sumar(self):
        self.assertEqual(Calculator.sumar(""), 0, "Empty String")
