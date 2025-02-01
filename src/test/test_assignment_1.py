import math
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main.assignment_1 import root_two, bisection_method, fixed_point_iteration, newton_method



def f(x):
    return math.cos(x) - x

def df(x):
    return -math.sin(x) - 1

def bisection_function(x):
    return x**3 + 4*x**2 - 10

# Parameters to use in the functions
x0_root_two = 1.5
x0_fixed_point = 1.5
tolerance = 1e-6
max_iterations = 50

# Running the functions (prints to console)
root_two(x0_root_two, tolerance)
fixed_point_iteration(x0_fixed_point, tolerance, max_iterations)
c, steps = bisection_method(1, 2, 0.001, bisection_function)
print(f"\nBisection Approximate Root = {c:.6f} after {steps} steps\n")

x0_newton = 0.5  
root, steps = newton_method(f, df, x0_newton, 1e-10, 100)
print(f"\nNewton-Raphson Approximate Root: {root:.10f}\n")