# Newton's Method for Two Variables (Python) 📈👩🏻‍💻

This project implements **Newton's Method** for optimizing functions with two variables using Python.


## What It Calculates 🧮

- The **gradient** $$\nabla f$$ (vector of first derivatives) is a vector indicating the direction of the steepest increase of the function. In Newton’s method, the gradient indicates where the function increases or decreases faster. 
  
$$
\nabla f(x, y) = \begin{bmatrix}
  \frac{\partial f}{\partial x} \\
  \frac{\partial f}{\partial y}
  \end{bmatrix}
$$

  
  
  ❓ But, the gradient alone only provides the direction of change, not how “steep” the change is. 
  
  ✨This is where the Hessian comes in...  

- The **Hessian matrix** $$H$$ (matrix of second derivatives) contains the second derivatives of the function. Second derivatives reveal the curvature of the function and help us understand its behavior near a point.

  
$$
H(x, y) = \begin{bmatrix}
  \frac{\partial^2 f}{\partial x^2} & \frac{\partial^2 f}{\partial x \partial y} \\
  \frac{\partial^2 f}{\partial y \partial x} & \frac{\partial^2 f}{\partial y^2}
  \end{bmatrix}
$$


- The **determinant** of the Hessian matrix to check invertibility

  
$$
\det(H) = \left( \frac{\partial^2 f}{\partial x^2} \cdot \frac{\partial^2 f}{\partial y^2} \right) - \left( \frac{\partial^2 f}{\partial x \partial y} \cdot \frac{\partial^2 f}{\partial y \partial x} \right)
$$


- Automatic classification of the critical point as a **local minimum**, **local maximum**, or **saddle point**

#### Therefore, Newton’s method uses: 😉
 1) The Gradient to determine the optimization direction
 2) The Hessian to understand curvature
 3) The Hessian determinant to ensure invertibility and fast convergence

---

## How Newton's Method Works 💡

Newton's method is an efficient optimization algorithm that uses both the gradient and the Hessian matrix of a function to find critical points where the gradient equals zero. The steps for solving Newton's method:

1. Takes a function $$f(x,y)$$ as input
2. Computes the gradient amd Hessian symbolically using sympy
3. Starting from the initial point $$\mathbf{x}_n$$, the numerical update is performed as:

  $$
  \mathbf{x}_{n+1} = \mathbf{x}_n - H^{-1} \cdot \nabla f
  $$

  where,

- $H^-1$ = the inverse of the Hessian matrix (matrix of second derivatives)  
- $\nabla f$ = gradient (vector of first derivatives) 

4. Stops when convergence is reached or when the Hessian is not invertible


---



## Interpretation of $\delta$ 🤔

The appropriate definition of the above type is as:

$$
\mathbf{x}_{n+1} = \mathbf{x}_n - \delta
$$

where, the correction vector $\delta$ is defined as:

$$
\delta = H^{-1} \cdot \nabla f
$$


It determines how far and in which direction to move at each iteration.


---

## Visual Comparison between Newton's Method and Gradient Descent 📐🔍

![Newton vs Gradient Descent](https://github.com/user-attachments/assets/74673bc1-f649-4962-accd-e3c094611bcd)

---

## How to Run It (on PyCharm) 🚀

- Install the `sympy` and `numpy` libraries  
- Run the Python script implementing the algorithm

---

## Tools Used 🧠

- ChatGPT AI Tool for assistance and code optimization

---

## What I Learned 🎯

- Symbolic differentiation and Hessian computation using SymPy  
- Matrix inversion and determinant checking with NumPy  
- Convergence criteria in numerical optimization methods
