## Problem 1

Re-determine parity of permutations using their decrement:

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

## Problem 2

Using the decrement approach, determine signs of permutations:

### Subproblem A

$$\begin{pmatrix}
    1 & 2 & 3 & 4 & \dots & 2n-1 & 2n\\
    2 & 1 & 4 & 3 & \dots & 2n & 2n-1\\
\end{pmatrix}$$

### Subproblem B

$$\begin{pmatrix}
    1 & 2 & 3 & 4 & 5 & 6 & \dots & 3n-2 & 3n-1 & 3n\\
    3 & 2 & 1 & 6 & 5 & 4 & \dots & 3n & 3n-1 & 3n-2\\
\end{pmatrix}$$

### Subproblem C

$$\begin{pmatrix}
    1 & 2 & 3 & 4 & \dots & 2n-3 & 2n-2 & 2n-1 & 2n\\
    3 & 4 & 5 & 6 & \dots & 2n-1 & 2n & 1 & 2
\end{pmatrix}$$

> Calculate determinants

## Problem 3

### Subproblem A

$$\begin{vmatrix}
    5 & 2\\
    7 & 3\\
\end{vmatrix}$$

### Subproblem B

$$\begin{vmatrix}
    1 & 2\\
    3 & 4
\end{vmatrix}$$

### Subproblem C

$$\begin{vmatrix}
    6 & 9 \\
    8 & 12\\
\end{vmatrix}$$

### Subproblem D

$$\begin{vmatrix}
    n + 1 & n\\
    n & n -1\\
\end{vmatrix}$$

### Subproblem E

$$\begin{vmatrix}
    \cos\alpha & \sin\alpha\\
    \sin\alpha & \cos\alpha
\end{vmatrix}$$

## Problem 4

### Subproblem A

$$\begin{vmatrix}
    3 & 2 & 1\\
    2 & 5 & 3\\
    3 & 4 & 2\\
\end{vmatrix}$$

### Subproblem B

$$\begin{vmatrix}
    3 & 4 & -5\\
    8 & 7 & -2\\
    2 & -1 & 8\\
\end{vmatrix}$$

### Subproblem C

$$\begin{vmatrix}
    a & b & c\\
    b & c & a\\
    c & a & b\\
\end{vmatrix}$$

## Problem 5

Determine what products are a part of respective determinants and what signs do they have:

### Subproblem A

$$a_{33}a_{16}a_{72}a_{27}a_{55}a_{61}a_{44}$$

### Subproblem B

$$a_{12}a_{23}a_{34}\dots a_{n-1, n}a_{kk}$$

## Problem 6

### Subproblem A

Choose such values $i, k$ so that the product 

$$a_{62}a_{i5}a_{33}a_{k4}a_{46}a_{21}$$

would be a part of the determiner of the sixth degree with the minus sign.

### Subproblem B

Choose such values $i, k$ so that the product 

$$a_{47}a_{63}a_{1i}a_{55}a_{7k}a_{24}a_{31}$$

would be a part of the determiner of the sixth degree with the plus sign.

## Problem 7 

Find coefficient in $kx^5$ in the determiner expression:

$$\begin{vmatrix}
    2 & -3 & x & 4 & -5\\
    3 & x & -1 & -2 & 4\\
    1 & 3 & 1 & x & 1\\
    -3 & x^2 & -1 & 1 & x\\
    x & -2 & 4 & 5 & -2\\
\end{vmatrix}$$

## Problem 8

Find coefficient in $kx^4$ in the determinant expression:

$$\begin{vmatrix}
    1 & 3 & x & 2 & 2\\
    x & 2 & 1 & 4 & 5\\
    x & 1 & x & 5 & x\\
    3 & x & 1 & 2 & 3\\
    1 & 2 & 4 & x & 2\\
\end{vmatrix}$$

---

$$\begin{vmatrix}
    1 & 3 & x & 2 & 2\\
    x & 2 & 1 & 4 & 5\\
    x & 1 & x & 5 & x\\
    3 & x & 1 & 2 & 3\\
    1 & 2 & 4 & x & 2\\
\end{vmatrix}$$

## Problem 9

How would the determinant of degree $n$ change if one were to write rows in the reversed order?

## Problem 10

How would the determinant of a matrix change if it is transposed?

## Problem 11

How would the determinant of a matrix $A$ change if $\forall i,j$ element $a_{ij}$ were to be multiplied by $c^{i-j}$, where $c\neq0$ is some constant?

## Problem 12

### Subproblem A

Prove that the determinant would not change if one were to subtract all succeeding rows from each row (except for the last one).

### Subproblem B

Prove that the determinant would not change if one were to add all preceding columns to each column (starting from the second column).

## Problem 13 

How would the determinant change if one were to subtract the succeeding row from each row (except or the last one) and subtract the previous first row from the last row?

## Problem 14

Splitting the matrix along the 3rd line, calculate the determinant 

### Subproblem A

$$\begin{vmatrix}
    2 & -3 & 4 & 1\\
    4 & -2 & 3 & 2\\
    a & b & c & d\\
    3 & -1 & 4 & 3
\end{vmatrix}$$

### Subproblem B

$$\begin{vmatrix}
    x & a & b & 0 & c\\
    0 & y & 0 & 0 & d\\
    0 & e & z & 0 & f\\
    g & h & k & u & l\\
    0 & 0 & 0 & 0 & v\\
\end{vmatrix}$$

## Problem 15

### Subproblem A

$$\begin{vmatrix}
    -3 & 9 & 3 & 6\\
    -5 & 8 & 2 & 7\\
    4 & -5 & -3 & -2\\
    7 & -8 & -4 & -5\\
\end{vmatrix}$$

### Subproblem B

$$\begin{vmatrix}
    3 & -3 & -2 & -5\\
    2 & 5 & 4 & 6\\
    5 & 5 & 8 & 8\\
    4 & 4 & 5 & 6
\end{vmatrix}$$

## Problem 16

Given matrices $A, B \in M_4(\mathbb{R})$. It is known that $\det A=1$ and 

$$B^{(1)}=3A^{(3)}-2A^{(4)}, \ \ B^{(2)}=2A^{(1)}+3A^{(2)}, \ \ B^{(3)}=-2A^{(1)}+2A^{(3)}+A^{(4)}, \ \ B^{(4)}=2A^{(2)}+3A^{(4)},$$

where $A^{(i)}$ and $B^{(j)}$ denote $i$-th column of matrix $A$ and $j$-th column of matrix $B$ respectively. Find $\det B$.

## Problem 17

Let $A, B$ be square matrices of the same order $\geqslant 3$ given that all rows in matrix $A$ are the same and all columns in matrix $B$ are the same. What can $\det(A+B)$ be equal to?