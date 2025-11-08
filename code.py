import sympy as sp # SymPy is a Python library for symbolic computation -> it can manipulate mathematical expressions algebraically
import numpy as np # NumPy is a Python library for numerical operations, especially with arrays and matrices

# Start of code
# Introductory message
print("This algorithm implements Newton's method for two variables.")
print()

# Variable definition
x, y = sp.symbols('x y')

func_str = input("Enter the function f(x, y): ") # Function input from the user
f = sp.sympify(func_str) # Using SymPy to convert a string representation of a mathematical expression into a symbolic expression

# Compute gradient (first derivatives) and Hessian (second derivatives matrix)
grad_f = [sp.diff(f, var) for var in (x, y)]
hessian_f = sp.hessian(f, (x, y))

# Get initial point (x0,y0) from the user
x0 = float(input("x0 = "))
y0 = float(input("y0 = "))
xn = np.array([x0, y0], dtype='float64') # Store initial point as a numpy array of type float64

# Initialize control parameters
max_iter = 100   # Maximum number of iterations
epsilon = 1e-6   # Convergence tolerance
iteration_count = 0  # Iteration counter
converged = False    # Boolean flag for convergence

# Display initial information
f_xy0 = f.subs({x: x0, y: y0}) # f: is a symbolic expression (e.g., x**2 + y**2), 
                               # subs(): replaces the symbolic variables x and y with the numeric values x0 and y0
                               # f_xy0 now holds the evaluated expression at that point

print(f"\nValue of f(x, y) = {f} at point ({x0}, {y0}) is: f(x0, y0) = {f_xy0}") # Prints the original function and its evaluated value at the point (x0, y0)

print(f"Gradient: {[str(g) for g in grad_f]}") # Prints the gradient vector of the function f, 
                                               # grad_f: is expected to be a list of partial derivatives like [∂f/∂x, ∂f/∂y]
                                               # str(g): converts each symbolic derivative to a readable string
print("Hessian:")
sp.pprint(hessian_f) # hessian_f: is assumed to be a SymPy Matrix object containing second derivatives
                     # sp.pprint(...): formats and prints it nicely in the console, showing it like a true matrix rather than a flat list

for i in range(max_iter): # Starts a loop that runs up to max_iter times
    iteration_count += 1 # Tracks how many iterations have occurred using iteration_count

    # Compute gradient and Hessian values at the current point
    grad_val = np.array([g.subs({x: xn[0], y: xn[1]}) for g in grad_f], dtype='float64') # Evaluates the gradient vector at the current point xn = [x0, y0]
                                                                                         # grad_f: is a list of symbolic partial derivatives
                                                                                         # subs(...): replaces symbolic variables with numeric values
    hessian_val = np.array(hessian_f.subs({x: xn[0], y: xn[1]})).astype(np.float64) # Evaluates the Hessian matrix numerically at the current point
    det_hessian = np.linalg.det(hessian_val) # Computes the determinant of the Hessian to check if it's invertible.

    # If the determinant is zero, the Hessian is not invertible, so the algorithm stops
    if det_hessian == 0:
        print(f"\n❌ The Hessian matrix at point {xn} is NOT invertible.")
        print("🔍 Hessian determinant:", det_hessian)
        print("🧠 Cannot proceed without the inverse.")
        break

    # Solve the system $$H$$ * $$\delta$$ = \grad f$$ to find the correction vector!!!!!!!!!!!!!!!!!!!
    delta = np.linalg.solve(hessian_val, grad_val)
    xn_new = xn - delta

    # Display intermediate results
    print(f"\nStep {iteration_count}:")
    print(f"  Point: {xn}")
    print(f"  Gradient: {grad_val}")
    print(f"  Hessian:\n{hessian_val}")
    print(f"  Hessian determinant: {det_hessian}")
    print(f"  Correction: {delta}")
    print(f"  New point: {xn_new}")

    # Convergence check
    if np.linalg.norm(xn_new - xn) < epsilon:
        xn = xn_new
        converged = True
        print("\n✅ Convergence achieved.")
        break

    xn = xn_new

# Display final point and total iterations
print(f"\n📍 Final point: x = {xn[0]}, y = {xn[1]}")
print(f"🔢 Total iterations: {iteration_count}")

# Additional evaluation
hess_final = sp.Matrix(hessian_f.subs({x: xn[0], y: xn[1]}))
det_final = hess_final.det()
f_xx_final = sp.diff(f, x, x).subs({x: xn[0], y: xn[1]})

print(f"\nDeterminant at final point: det(H) = {det_final}")
print(f"f_xx at final point: {f_xx_final}")

# Determine type of critical point
# If the Hessian matrix is positive definite (all principal minors positive), the function has a local minimum.
if det_final > 0 and f_xx_final > 0: 
    print("➡️ The point is a **local minimum**.")

# If the Hessian matrix is negative definite (all principal minors negative), the function has a local maximum.    
elif det_final > 0 and f_xx_final < 0:
    print("⬅️ The point is a **local maximum**.")
    
# If the Hessian has both positive and negative elements, the point is a saddle point.
elif det_final < 0:
    print("↔️ The point is a **saddle point**.")

# The determinant of the Hessian is crucial because it shows whether the matrix is invertible.
# If the determinant is zero, the Hessian is not invertible, and we cannot continue Newton’s method since the inverse of the Hessian is required for the update step.
else:
    print("⚠️ Determinant is 0 — inconclusive result.")

# If method did not converge
if not converged:
    print("❗ The method did not converge within the iteration limit.")

# End of code








