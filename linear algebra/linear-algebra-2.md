## Problem 1 

Find a polynomial $P(x)$ of a degree not higher than $3$, for which $P(-1)=-4$, $P(0)=1$, $P(1)=2$, $P(2)=2$.

---

Consider $ax^3+bx^2+cx+d$

$$\begin{cases}
    -a+b-c+d=-4\\
    d=1\\
    a+b+c+d=2\\
    8a+4b+2c+d=2
\end{cases}$$

$$\begin{cases}
    -a+b-c=-5\\
    a+b+c=1\\
    8a+4b+2c=1\\
    d=1\\
\end{cases}$$

$$\begin{cases}
    a+c=3\\
    b=-2\\
    8a+2c=9\\
    d=1\\
\end{cases}$$

$$\begin{cases}
    a=\frac{1}{2}\\
    b=-2\\
    c=\frac{5}{2}\\
    d=1\\
\end{cases}$$

Therefore, $P(x)=\frac{1}{2}x^3-2x^2+\frac{5}{2}x+1$

## Problem 2 

Find a polynomial $P(x)$ of a degree not higher than $3$, for which $P(1)=3$, $P'(1)=5$, $P'(-1)=-3$, $P''(-1)=1$. 

---

Consider $P(x)=ax^3+bx^2+cx+d, P'(x)=3ax^2+2bx+c, P''(x)=6ax+2b$

$$\begin{cases}
    a+b+c+d=3\\
    3a+2b+c=5\\
    3a-2b+c=-3\\
    -6a+2b=1\\
\end{cases}$$

$$\begin{cases}
    a+b+c+d=3\\
    6a+2c=2\\
    6a-4b+2c=-6\\
    -6a+2b=1\\
\end{cases}$$

$$\begin{cases}
    a=\frac{1}{2}\\
    b=2\\
    c=-\frac{1}{2}\\
    d=1\\
\end{cases}$$

Therefore, $\frac{1}{2}x^3+2x^2-\frac{1}{2}x+1=0$

---

> Solve matrix equations:

## Problem 3

$$\begin{pmatrix}
    3 & -1\\
    5 & -2\\
\end{pmatrix}X=\begin{pmatrix}
    14 & 16\\
    9 & 10\\
\end{pmatrix}$$

---

$$\begin{cases}
    3a-c=14\\
    3b-d=16\\
    5a-2c=9\\
    5b-2d=10
\end{cases}$$

$$\begin{cases}
    a=19\\
    b=22\\
    c=43\\
    d=50\\
\end{cases}$$

Answer: $$X=\begin{pmatrix}
    19 & 22\\
    43 & 50\\
\end{pmatrix}$$

## Problem 4

$$X\begin{pmatrix}
   5 & 3 & 1\\
   1 & -3 & -2\\
   -5 & -1 & 1 
\end{pmatrix}=\begin{pmatrix}
    -8 & 3 & 0\\
    -5 & 9 & 0\\
    -2 & 15 & 0
\end{pmatrix}$$

---

## Problem 5

$$X\begin{pmatrix}
    3 & 6\\
    4 & 8
\end{pmatrix}=\begin{pmatrix}
    2 & 4\\
    9 & 18
\end{pmatrix}$$

## Problem 6

$$\begin{pmatrix}
    1 & 1 & 1 & \dots & 1\\
    0 & 1 & 1 & \dots & 1\\
    0 & 0 & 1 & \dots & 1\\
    \vdots & \vdots & \vdots & \ddots & \vdots\\
    0 & 0 & 0 & \dots & 1\\
\end{pmatrix}X=\begin{pmatrix}
    1 & 2 & 3 & \dots & n\\
    0 & 1 & 2 & \dots & n-1\\
    0 & 0 & 1 & \dots & n-2\\
    \vdots & \vdots & \vdots & \ddots & \vdots\\
    0 & 0 & 0 & \dots & 1\\
\end{pmatrix}$$

## Problem 7 

For given matrix $\displaystyle A=\begin{pmatrix}
    1 & 1 & 0 & 2\\
    2 & -1 & -1 & 1\\
    -3 & 3 & 2 & 0\\
\end{pmatrix}$ find a square matrix $U$ such that matrix $UA$ has an improved row echelon form and also write this form down.

> Find inverse matrices:

## Problem 8

### Subproblem A

$$\begin{pmatrix}
    1 & 2\\
    3 & 4\\
\end{pmatrix}$$

### Suproblem B

$$\begin{pmatrix}
    3 & 4\\
    5 & 7\\
\end{pmatrix}$$

## Problem 9

$$\begin{pmatrix}
    2 & 7 & 3\\
    3 & 9 & 4\\
    1 & 5 & 3\\
\end{pmatrix}$$

## Problem 10

$$\begin{pmatrix}
    1 & 4 & 7\\
    2 & 5 & 8\\
    3 & 6 & 9\\
\end{pmatrix}$$

## Problem 11

> Find straight and inverse products of the following permutations:

## Subproblem A

$$\begin{pmatrix}
    1 & 2 & 3 & 4 & 5 & 6\\
    3 & 6 & 4 & 5 & 2 & 1\\
\end{pmatrix}\times\begin{pmatrix}
    1 & 2 & 3 & 4 & 5 & 6\\
    2 & 4 & 1 & 5 & 6 & 3\\
\end{pmatrix}$$

## Subproblem B

$$\begin{pmatrix}
    1 & 2 & 3 & 4 & 5\\
    2 & 1 & 3 & 5 & 4\\
\end{pmatrix}\times\begin{pmatrix}
    1 & 2 & 3 & 4 & 5\\
    4 & 5 & 3 & 2 & 1\\
\end{pmatrix}$$

## Problem 12

> Use cycle notation:

### Subproblem A

$$\begin{pmatrix}
    1 & 2 & 3 & 4 & 5 & 6 & 7\\
    5 & 4 & 1 & 7 & 3 & 6 & 2\\
\end{pmatrix}$$

### Subproblem B

$$\begin{pmatrix}
    1 & 2 & 3 & 4 & 5 & 6 & 7\\
    3 & 1 & 6 & 7 & 5 & 2 & 4\\
\end{pmatrix}$$

### Subproblem C

$$\begin{pmatrix}
    1 & 2 & 3 & 4 & 5 & 6 & 7\\
    3 & 7 & 6 & 5 & 1 & 2 & 4\\
\end{pmatrix}$$

### Subproblem D

$$\begin{pmatrix}
    1 & 2 & 3 & 4 & 5 & 6 & 7\\
    4 & 3 & 6 & 7 & 1 & 5 & 2\\
\end{pmatrix}$$

> Use table notation:

### Subproblem E

$$(1 \ 3 \ 6)(2 \ 4 \ 7)(5)$$

### Subproblem F

$$(1 \ 6 \ 5\ 4 \ 2 \ 3 \ 7)$$

## Problem 13

Count the number of inversion in a sequence:

### Subproblem A

$$1, 3, 5, 7, \dots, 2n-1, 2, 4, 6, 7, \dots,2n$$

### Subproblem B

$$k, k+1,\dots,n,1,2,\dots,k-1$$

## Problem 14

Determine parity of permutations:

### Subproblem A

$$\begin{pmatrix}
    1 & 2 & 3 & 4 & 5 & 6 & 7\\
    5 & 6 & 4 & 7 & 2 & 1 & 3\\
\end{pmatrix}$$

### Subproblem B

$$\begin{pmatrix}
    1 & 2 & 3 & 4 & 5 & 6 & 7 & 8\\
    3 & 5 & 2 & 1 & 6 & 4 & 8 & 7\\
\end{pmatrix}$$

### Subproblem C

$$\begin{pmatrix}
    3 & 5 & 6 & 4 & 2 & 1 & 7\\
    2 & 4 & 1 & 7 & 6 & 5 & 3\\
\end{pmatrix}$$

### Subproblem D

$$\begin{pmatrix}
    2 & 7 & 5 & 4 & 8 & 3 & 6 & 1\\
    3 & 5 & 8 & 7 & 2 & 6 & 1 & 4\\
\end{pmatrix}$$

## Problem 15

Solve permutation equation:

$$\begin{pmatrix}
    1 & 2 & 3 & 4 & 5 & 6 & 7\\
    6 & 7 & 4 & 2 & 1 & 3 & 5\\
\end{pmatrix}X\begin{pmatrix}
    1 & 2 & 3 & 4 & 5 & 6 & 7\\
    3 & 4 & 7 & 6 & 2 & 1 & 5\\
\end{pmatrix}=\begin{pmatrix}
    1 & 2 & 3 & 4 & 5 & 6 & 7\\
    7 & 1 & 4 & 6 & 3 & 5 & 2\\
\end{pmatrix}$$

## Problem 16

Calculate $\sigma^{77}, \sigma^{90},\sigma^{119},\sigma^{148}$ if $\displaystyle\sigma=\begin{pmatrix}
    1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & 10 & 11 & 12\\
    5 & 9 & 11 & 3 & 8 & 10 & 2 & 12 & 7 & 4 & 6 & 1\\
\end{pmatrix}$.

## Problem 17

By how many may the number of inversions in permutation $\displaystyle\sigma=\begin{pmatrix}
    1 & 2 & 3 & \dots & n\\
    \sigma(1) & \sigma(2) & \sigma(3) & \dots & \sigma(n)
\end{pmatrix}$ change if one were to swap two adjacent elements? How would the sign of the permutation change?

## Problem 18

Let $\rho$ be a result of a permutation $\sigma$ with two elements swapped ($\sigma(i)$ and $\sigma(j)$) in the lower row. Describe permutation $\sigma^{-1}\rho$  