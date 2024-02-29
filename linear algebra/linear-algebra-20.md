# Linear Algebra, Homework 20

> Find the symmetric bilinear functions associated with quadratic functions:

## Problem 1

We know that there is a bijection between all symmetric bilinear forms and matrices of quadratic forms, thus it's really easy to correlate them.

### Algorithm

Write out the matrix of a quadratic form, we get:

$$\begin{pmatrix}
    a_{11} & a_{12} & a_{13}\\
    a_{21} & a_{22} & a_{23}\\
    a_{31} & a_{32} & a_{33}
\end{pmatrix}$$

These coefficients correspond to coefficients of products $x_iy_j$, where $i$ is the row index and $j$ is the column index, we get:

$$\begin{align*}
    \beta(x,y)=\ &a_{11}x_1y_1+a_{12}x_1y_2+a_{13}x_1y_3+\\
    &a_{21}x_2y_1+a_{22}x_2y_2+a_{23}x_2y_3+\\
    &a_{31}x_3y_1+a_{32}x_3y_2+a_{33}x_3y_3
\end{align*}$$

Thus, I'll just use this below without much explanation:

### Subproblem A

$$Q(x)=x_1^2+2x_1x_2+2x_2^2-6x_1x_3+4x_2x_3-x_3^2$$

---

$$\begin{pmatrix}
    1 & 1 & -3\\
    1 & 2 & 2\\
    -3 & 2 & -1
\end{pmatrix}$$

$$\begin{align*}
    \beta(x,y)=\ &x_1y_1+x_1y_2-3x_1y_3+\\
    &x_2y_1+2x_2y_2+2x_2y_3+\\
    &-3x_3y_1+2x_3y_2-x_3y_3
\end{align*}$$

### Subproblem B

$$x_1x_2+x_1x_3+x_2x_3$$

---

$$\frac{1}{2}\begin{pmatrix}
    0 & 1 & 1\\
    1 & 0 & 1\\
    1 & 1 & 0
\end{pmatrix}$$

$$\beta(x,y)=\frac{1}{2}(x_1y_2+x_1y_3+x_2y_1+x_2y_3+x_3y_1+x_3y_2/)$$

## Problem 2

Find the symmetric bilinear functions associated with quadratic functions, where $Q(x)=f(x,x)$:

### Subproblem A

$$f(x,y)=2x_1y_1-3x_1y_2-4x_1y_3+x_2y_1-5x_2y_3+x_3y_3$$

---

$$Q(x)=2x_1^2-3x_1x_2+x_1x_2-4x_1x_3-5x_2x_3+x_3^2=\\=2x_1^2-2x_1x_2-4x_1x_3-5x_2x_3+x_3^2$$

$$\begin{pmatrix}
    2 & -1 & -2\\
    -1 & 0 & -\frac{5}{2}\\
    -2 & -\frac{5}{2} & 1
\end{pmatrix}$$

$$\begin{align*}
    \beta(x,y)=\ &2x_1y_1-x_1y_2-2x_1y_3+\\
    &-x_2y_1-\frac{5}{2}x_2y_3+\\
    &-2x_3y_1-\frac{5}{2}x_3y_2+x_3y_3
\end{align*}$$

### Subproblem B

$$f(x,y)=-x_1y_2+x_2y_1-2x_2y_2+3x_2y_3-x_3y_1+2x_3y_3$$

---

$$Q(x)=-x_1x_2+x_1x_2-2x_2^2+3x_2x_3-x_1x_3+2x_3^2=\\=-2x_2^2+3x_2x_3-x_1x_3+2x_3^2$$

$$\begin{pmatrix}
    0 & 0 & -\frac{1}{2}\\
    0 & -2 & \frac{3}{2}\\
    -\frac{1}{2} & \frac{3}{2} & 2
\end{pmatrix}$$

$$\beta(x,y)=-\frac{1}{2}x_1y_3-2x_2y_2+\frac{3}{2}x_2y_3-\frac{1}{2}x_3y_1+\frac{3}{2}x_3y_2+2x_3y_3$$

---

> Normalize the quadratic forms.

## Problem 3

$$x_1^2-2x_2^2+x_3^2+2x_1x_2+4x_1x_3+2x_2x_3$$

---

Corresponding matrix of the quadratic form:

$$\begin{pmatrix}
    1 & 1 & 2\\
    1 & -2 & 1\\
    2 & 1 & 1
\end{pmatrix}$$

Utilizing the Jacobi method, calculate the minors:

$$\delta_1=1,\\\delta_2=-2-1=-3,\\\delta_3=-2+2+2+8-1-1=8$$

Then, the canonical form follows 

$$\delta_1 x_1^2+\frac{\delta_2}{\delta_1}x_2^2+\frac{\delta_3}{\delta_2}x_3^2=$$

$$x_1^2-3x_2^2-\frac{8}{3}x_3^3$$

Alternatively, symmetric Gauss works here

$$\begin{pmatrix}
    1 & 1 & 2\\
    1 & -2 & 1\\
    2 & 1 & 1
\end{pmatrix}\sim\begin{pmatrix}
    1 & 0 & 2\\
    0 & -3 & -1\\
    2 & -1 & 1
\end{pmatrix}\sim\begin{pmatrix}
    1 & 0 & 0\\
    0 & -3 & 0\\
    0 & 0 &- \frac{8}{3}
\end{pmatrix}$$

## Problem 4

$$x_1^2-3x_3^2-2x_1x_2+2x_1x_3-6x_2x_3$$

---

Corresponding matrix of the quadratic form:

$$\begin{pmatrix}
    1 & -1 & 1\\
    -1 & 0 & -3\\
    1 & -3 & -3
\end{pmatrix}$$

Utilizing the Jacobi method, calculate the minors:

$$\delta_1=1,\\\delta_2=0-1=-1,\\\delta_3=0+3+3+0+3-9=0$$

Then, the canonical form follows 

$$\delta_1 x_1^2+\frac{\delta_2}{\delta_1}x_2^2+\frac{\delta_3}{\delta_2}x_3^2=x_1^2-x_2^2$$

Alternatively, symmetric Gauss works here

$$\begin{pmatrix}
    1 & -1 & 1\\
    -1 & 0 & -3\\
    1 & -3 & -3
\end{pmatrix}\sim\begin{pmatrix}
    1 & 0 & 0\\
    0 & -1 & -2\\
    0 & -2 & -4
\end{pmatrix}\sim\begin{pmatrix}
    1 & 0 & 0\\
    0 & -1 & 0\\
    0 & 0 & 0
\end{pmatrix}$$