
import matplotlib.pyplot as plt
import numpy as np
import sympy as sy

# Sympy para resolver el sistema de ecuaciones lineales
a1, a2, a3 = sy.symbols('a1, a2, a3')
#A = sy.Matrix(( (3, 3, 3, 0), (2, 2, 2, 0), (2, 1, 0, 0), (3, 2, 1, 0) ))
A = sy.Matrix(( (1, 1, 2,0), (0, 1, 1,0) ))
print(sy.solve_linear_system(A, a1, a2, a3))
