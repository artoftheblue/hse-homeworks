# Linear Algebra, Homework 19

## Problem 1

Prove that for any non-zero linear function $f$ in $n$-dimensional space $V$ exists a basis $(e_1,\dots,e_n)$ of space $V$ such that 

$$f(x_1e_1+\dots+x_ne_n)=x_1$$

for any coefficients $x_1,\dots,x_n$.

## Problem 2

Let $(e_1,e_2,e_3)$ be some basis of a three-dimensional vector space $V$, and $(\varepsilon_1,\varepsilon+2,\varepsilon_3)$ be a dual basis to it of space $V^*$.

### Subproblem A

Find the basis of space $V^*$ dual to basis $(3e_1+e_2-2e_3, 2e_1+e_3,e_1)$ of space $V$.

---

Transformation matrix from basis $(e_1,e_2,e_3)$ to $(3e_1+e_2-2e_3, 2e_1+e_3,e_1)$ is 

$$(3e_1+e_2-2e_3, 2e_1+e_3,e_1)=(e_1,e_2,e_3)\begin{pmatrix}
    3 & 2 & 1\\
    1 & 0 & 0\\
    -2 & 1 & 0
\end{pmatrix}$$

The inverse of this matrix is

$$\begin{pmatrix}
    3 & 2 & 1\\
    1 & 0 & 0\\
    -2 & 1 & 0
\end{pmatrix}^{-1}=\begin{pmatrix}
    0 & 1 & 0\\
    0 & 2 & 1\\
    1 & -7 & -2
\end{pmatrix}$$

Thus, find the dual basis:

$$\begin{pmatrix}
    \varepsilon'_1\\
    \varepsilon'_2\\
    \varepsilon'_3
\end{pmatrix}=\begin{pmatrix}
    0 & 1 & 0\\
    0 & 2 & 1\\
    1 & -7 & -2
\end{pmatrix}\begin{pmatrix}
    \varepsilon_1\\
    \varepsilon_2\\
    \varepsilon_3
\end{pmatrix}=\begin{pmatrix}
    \varepsilon_2\\
    2\varepsilon_2+\varepsilon_3\\
    \varepsilon_1-7\varepsilon_2-2\varepsilon_3
\end{pmatrix}$$

which means that the answer is 

$$(\varepsilon_2,2\varepsilon_2+\varepsilon_3,\varepsilon_1-7\varepsilon_2-2\varepsilon_3)$$

### Subproblem B

Find the basis of space $V$, for which the dual is basis $(\varepsilon_3,2\varepsilon_1+\varepsilon_3,3\varepsilon_1+\varepsilon_2-2\varepsilon_3)$ in space $V^*$.

---

Find the transformation matrix

$$\begin{pmatrix}
    \varepsilon'_1\\
    \varepsilon'_2\\
    \varepsilon'_3
\end{pmatrix}=\begin{pmatrix}
    0 & 0 & 1\\
    2 & 0 & 1\\
    3 & 1 & -2
\end{pmatrix}\begin{pmatrix}
    \varepsilon_1\\
    \varepsilon_2\\
    \varepsilon_3
\end{pmatrix}$$

Find the inverse of the matrix:

$$\begin{pmatrix}
    0 & 0 & 1\\
    2 & 0 & 1\\
    3 & 1 & -2
\end{pmatrix}^{-1}=\frac{1}{2}\begin{pmatrix}
    -1 & 1 & 0\\
    7 & -3 & 2\\
    2 & 0 & 0
\end{pmatrix}$$

Now, calculate the basis which would be our answer:

$$(e'_1,e_2',e_3')=\frac{1}{2}(e_1,e_2,e_3)\begin{pmatrix}
    -1 & 1 & 0\\
    7 & -3 & 2\\
    2 & 0 & 0
\end{pmatrix}=$$

$$=\frac{1}{2}(-e_1+7e_2+2e_3,e_1-3e_2,2e_2)=$$

$$=\left(-\frac{e_1}{2}+\frac{7e_2}{2}+e_3,\frac{e_1}{2}-\frac{3e_2}{2},e_2\right)$$

## Problem 3

Let $V=\mathbb{R}[x]_{\leq n}$. Consider linear functions $\varepsilon_0,\varepsilon_1,\dots,\varepsilon_n\in V^*$, where $\varepsilon_i(f)=f^{(i)}(0)$. Prove that these functions form a basis in $V^*$, and find the basis in $V$, for which this basis is dual.