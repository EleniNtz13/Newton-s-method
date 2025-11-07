# Newton's Method for Two Variables (Python) 🧮
This project implements **Newton's Method** for optimization of functions with two variables using Python.

It calculates:
- The **gradient** (first derivatives)
- The **Hessian matrix** (second derivatives)
- The **determinant** of the Hessian (for checking invertibility)
- And automatically determines whether the result is a **local minimum**, **local maximum**, or **saddle point**

## How it works 💡
Newton's method is an efficient optimization algorithm that uses both the gradient and Hessian of a function to find critical points.

The algorithm:
1. Takes a function f(x, y) as input
2. Computes the gradient and Hessian symbolically using **SymPy**
3. Iteratively updates the variables using \( x_{n+1} = x_n - H^{-1} \nabla f(x_n) \)
4. Stops when convergence is achieved or when the Hessian is not invertible

## How to run it 🚀
- Install sympy
- Install numpy

## Tool used 🧠
- ChatGPT AI Tool

## What I learned 🎯
- Symbolic differentiation and Hessian computation with SymPy
- Matrix inversion and determinant checks with NumPy
- Convergence criteria for numerical optimization
