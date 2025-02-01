import math

def root_two(x0, tolerance):
    print("\n==================================================")
    print("Approximation Algorithm (Slide 11, Chapter 2.1)")
    print("=================================================\n")
    
    iterations = 0
    diff = x0
    x = x0

    print(f"Iteration {iterations}: x = {x:.6f}")

    while diff >= tolerance:
        iterations += 1
        prev_x = x
        x = (x / 2) + (1 / x)
        diff = abs(x - prev_x)
        print(f"Iteration {iterations}: x = {x:.6f}")

    print(f"\nConvergence after {iterations} iterations\n")

def bisection_method(a, b, tolerance, f):
    print("\n=============================================")
    print("The Bisection Method (Slide 14, Chapter 2.1)")
    print("==============================================\n")
    
    steps = 0
    while b - a > tolerance:
        steps += 1
        c = (a + b) / 2
        if f(c) == 0:
            return c, steps
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c
    return c, steps

def fixed_point_iteration(x0, tolerance, max_iterations):
    print("\n=================================================")
    print("The Fixed-Point Iteration (Slide 13, Chapter 2.2)")
    print("===================================================\n")
    
    i = 1
    x = 0
    
    while i <= max_iterations:
        x = x0 - x0*x0*x0 - 4 * x0*x0 + 10 
        
        if math.isnan(x):
            print("\nResult diverges")
            break
        
        print(f"Iteration {i}: x = {x:.6f}")
        
        if abs(x - x0) < tolerance:
            break
        
        i += 1
        x0 = x
    
    print(f"\nFailure after {i} iterations\n")

def newton_method(f, df, x0, tolerance, max_iterations):
    print("\n=================================================")
    print("The Newton-Raphson Method (Slide 7, Chapter 2.3)")
    print("===================================================\n")
    
    x = x0
    steps = 0
    print(f"Initial guess: x0 = {x0:.6f}")
    
    for _ in range(max_iterations):
        x_next = x - f(x) / df(x)
        steps += 1
        print(f"Iteration {steps}: x = {x_next:.6f}")
        
        if abs(x_next - x) < tolerance:
            print(f"\nConverged after {steps} iterations.")
            return x_next, steps
        
        x = x_next
    
    print("Max Iterations Reached!")
    return x, steps    

def f(x):
    return math.cos(x) - x

def df(x):
    return -math.sin(x) - 1

def bisection_function(x):
    return x**3 + 4*x**2 - 10
