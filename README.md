# Newton's Method for Two Variables (Python) 🧮
This project implements **Newton's Method** for optimization of functions with two variables using Python.

It calculates:
- The **gradient** (first derivatives)
<img width="177" height="81" alt="image" src="https://github.com/user-attachments/assets/eba88be9-1062-48fa-b058-4395ddf02305" />

- The **Hessian matrix** (second derivatives)
<img width="202" height="91" alt="image" src="https://github.com/user-attachments/assets/fbedd6da-bee4-480c-8685-516b6319eca9" />

- The **determinant** of the Hessian (for checking invertibility)
- And automatically determines whether the result is a **local minimum**, **local maximum**, or **saddle point**

## How it works 💡
Newton's method is an efficient optimization algorithm that uses both the gradient and Hessian of a function to find critical points.

The algorithm:
1. Takes a function f(x, y) as input
2. Computes the gradient and Hessian symbolically using **SymPy**
3. Iteratively updates the variables using <img width="231" height="30" alt="image" src="https://github.com/user-attachments/assets/667f43fe-9aeb-4a23-9f8b-1f89f1a3874e" />

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
