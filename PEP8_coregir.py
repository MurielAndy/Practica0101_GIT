# script.py
import os 
import sys


def mi_funcionSuma(A, B, C, imprime = True):
    resultado = A+B+C
    if imprime != False:
        print(resultado)
    return resultado


a = 4
variable_b = 5
var_c = 10

mi_funcionSuma(a, variable_b, var_c)