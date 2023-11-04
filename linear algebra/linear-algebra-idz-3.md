# Individual Homework #3

## Problem 1

Find inverse matrix of 

$$\begin{pmatrix}
    -6 & 4 & 3 & 3\\
    2 & -2 & 0 & -1\\
    -2 & -5 & -2 & 3\\
    -1 & -1 & 0 & 1
\end{pmatrix}$$

---

Per Gauss:

$$\begin{pmatrix}
    -6 & 4 & 3 & 3 & \bigm| & 1 & 0 & 0 & 0\\
    2 & -2 & 0 & -1 & \bigm| & 0 & 1 & 0 & 0\\
    -2 & -5 & -2 & 3 & \bigm| & 0 & 0 & 1 & 0\\
    -1 & -1 & 0 & 1 & \bigm| & 0 & 0 & 0 & 1
\end{pmatrix}$$

$$\begin{pmatrix}
    1 & 1 & 0 & -1 & \bigm| & 0 & 0 & 0 & -1\\
    -6 & 4 & 3 & 3 & \bigm| & 1 & 0 & 0 & 0\\
    2 & -2 & 0 & -1 & \bigm| & 0 & 1 & 0 & 0\\
    -2 & -5 & -2 & 3 & \bigm| & 0 & 0 & 1 & 0\\
\end{pmatrix}$$

$$\begin{pmatrix}
    1 & 1 & 0 & -1 & \bigm| & 0 & 0 & 0 & -1\\
    0 & 10 & 3 & -3 & \bigm| & 1 & 0 & 0 & -6\\
    0 & -4 & 0 & 1 & \bigm| & 0 & 1 & 0 & 2\\
    0 & -3 & -2 & 1 & \bigm| & 0 & 0 & 1 & -2\\
\end{pmatrix}$$

$$\begin{pmatrix}
    1 & 1 & 0 & -1 & \bigm| & 0 & 0 & 0 & -1\\
    0 & 10 & 3 & -3 & \bigm| & 1 & 0 & 0 & -6\\
    0 & 0 & 1.2 & -0.2 & \bigm| & 0.4 & 1 & 0 & -0.4\\
    0 & 0 & -1.1 & 0.1 & \bigm| & 0.3 & 0 & 1 & -3.8\\
\end{pmatrix}$$

$$\begin{pmatrix}
    1 & 1 & 0 & -1 & \bigm| & 0 & 0 & 0 & -1\\
    0 & 1 & 0.3 & -0.3 & \bigm| & 0.1 & 0 & 0 & -0.6\\
    0 & 0 & 1.2 & -0.2 & \bigm| & 0.4 & 1 & 0 & -0.4\\
    0 & 0 & -1.1 & 0.1 & \bigm| & 0.3 & 0 & 1 & -3.8\\
\end{pmatrix}$$

$$\begin{pmatrix}
    1 & 1 & 0 & -1 & \bigm| & 0 & 0 & 0 & -1\\
    0 & 1 & 0.3 & -0.3 & \bigm| & 0.1 & 0 & 0 & -0.6\\
    0 & 0 & 0.1 & -0.1 & \bigm| & 0.7 & 1 & 1 & -4.2\\
    0 & 0 & -1.1 & 0.1 & \bigm| & 0.3 & 0 & 1 & -3.8\\
\end{pmatrix}$$

$$\begin{pmatrix}
    1 & 1 & 0 & -1 & \bigm| & 0 & 0 & 0 & -1\\
    0 & 1 & 0.3 & -0.3 & \bigm| & 0.1 & 0 & 0 & -0.6\\
    0 & 0 & 0.1 & -0.1 & \bigm| & 0.7 & 1 & 1 & -4.2\\
    0 & 0 & -1 & 0 & \bigm| & 1 & 1 & 2 & -8\\
\end{pmatrix}$$

$$\begin{pmatrix}
    1 & 1 & 0 & -1 & \bigm| & 0 & 0 & 0 & -1\\
    0 & 1 & 0.3 & -0.3 & \bigm| & 0.1 & 0 & 0 & -0.6\\
    0 & 0 & 1 & -1 & \bigm| & 7 & 10 & 10 & -42\\
    0 & 0 & -1 & 0 & \bigm| & 1 & 1 & 2 & -8\\
\end{pmatrix}$$

$$\begin{pmatrix}
    1 & 1 & 0 & -1 & \bigm| & 0 & 0 & 0 & -1\\
    0 & 1 & 0.3 & -0.3 & \bigm| & 0.1 & 0 & 0 & -0.6\\
    0 & 0 & 1 & -1 & \bigm| & 7 & 10 & 10 & -42\\
    0 & 0 & 0 & 1 & \bigm| & -8 & -11 & -12 & 50\\
\end{pmatrix}$$

$$\begin{pmatrix}
    1 & 1 & 0 & -1 & \bigm| & 0 & 0 & 0 & -1\\
    0 & 10 & 3 & -3 & \bigm| & 1 & 0 & 0 & -6\\
    0 & 0 & 1 & 0 & \bigm| & -1 & -1 & -2 & 8\\
    0 & 0 & 0 & 1 & \bigm| & -8 & -11 & -12 & 50\\
\end{pmatrix}$$

$$\begin{pmatrix}
    1 & 1 & 0 & -1 & \bigm| & 0 & 0 & 0 & -1\\
    0 & 10 & 0 & -3 & \bigm| & 4 & 3 & 6 & -30\\
    0 & 0 & 1 & 0 & \bigm| & -1 & -1 & -2 & 8\\
    0 & 0 & 0 & 1 & \bigm| & -8 & -11 & -12 & 50\\
\end{pmatrix}$$

$$\begin{pmatrix}
    1 & 1 & 0 & -1 & \bigm| & 0 & 0 & 0 & -1\\
    0 & 10 & 0 & 0 & \bigm| & -20 & -30 & -30 & 120\\
    0 & 0 & 1 & 0 & \bigm| & -1 & -1 & -2 & 8\\
    0 & 0 & 0 & 1 & \bigm| & -8 & -11 & -12 & 50\\
\end{pmatrix}$$

$$\begin{pmatrix}
    1 & 1 & 0 & -1 & \bigm| & 0 & 0 & 0 & -1\\
    0 & 1 & 0 & 0 & \bigm| & -2 & -3 & -3 & 12\\
    0 & 0 & 1 & 0 & \bigm| & -1 & -1 & -2 & 8\\
    0 & 0 & 0 & 1 & \bigm| & -8 & -11 & -12 & 50\\
\end{pmatrix}$$

$$\begin{pmatrix}
    1 & 0 & 0 & -1 & \bigm| & 2 & 3 & 3 & -13\\
    0 & 1 & 0 & 0 & \bigm| & -2 & -3 & -3 & 12\\
    0 & 0 & 1 & 0 & \bigm| & -1 & -1 & -2 & 8\\
    0 & 0 & 0 & 1 & \bigm| & -8 & -11 & -12 & 50\\
\end{pmatrix}$$

$$\begin{pmatrix}
    1 & 0 & 0 & 0 & \bigm| & -6 & -8 & -9 & 37\\
    0 & 1 & 0 & 0 & \bigm| & -2 & -3 & -3 & 12\\
    0 & 0 & 1 & 0 & \bigm| & -1 & -1 & -2 & 8\\
    0 & 0 & 0 & 1 & \bigm| & -8 & -11 & -12 & 50\\
\end{pmatrix}$$

**Answer:**

$$\begin{pmatrix}
    -6 & -8 & -9 & 37\\
    -2 & -3 & -3 & 12\\
    -1 & -1 & -2 & 8\\
    -8 & -11 & -12 & 50\\
\end{pmatrix}$$

## Problem 2

Solve equation for $X$:

$$\left(\begin{pmatrix}
    1 & 2 & 3 & 4 & 5 & 6 & 7 & 8\\
    4 & 6 & 8 & 5 & 1 & 3 & 7 & 2
\end{pmatrix}^{11}\cdot\begin{pmatrix}
    1 & 2 & 3 & 4 & 5 & 6 & 7 & 8\\
    4 & 8 & 5 & 6 & 2 & 7 & 3 & 1\\
\end{pmatrix}^{-1}\right)^{149}\cdot X=\begin{pmatrix}
    1 & 2 & 3 & 4 & 5 & 6 & 7 & 8\\
    6 & 3 & 1 & 5 & 4 & 7 & 8 & 2\\
\end{pmatrix}$$

---

$$\begin{pmatrix}
    1 & 2 & 3 & 4 & 5 & 6 & 7 & 8\\
    4 & 8 & 5 & 6 & 2 & 7 & 3 & 1\\
\end{pmatrix}^{-1}=\begin{pmatrix}
    1 & 2 & 3 & 4 & 5 & 6 & 7 & 8\\
    8 & 5 & 7 & 1 & 3 & 4 & 6 & 2\\
\end{pmatrix}$$

---

In the following permutation, there are $3$ cycles: 

$$\begin{pmatrix}
    1 & 2 & 3 & 4 & 5 & 6 & 7 & 8\\
    4 & 6 & 8 & 5 & 1 & 3 & 7 & 2\\
\end{pmatrix}$$

* $\text{mod} \ 3$: $\ \xrightarrow{0}{1 \choose 4}\xrightarrow{1} {4 \choose 5} \xrightarrow{2} {5 \choose 1}$
* $\text{mod} \ 4$: $\ \xrightarrow{0} {2 \choose 6} \xrightarrow{1} {6 \choose 3} \xrightarrow{2} {3 \choose 8} \xrightarrow{3} {8 \choose 2}$
* $\text{mod} \ 1$: $\ \xrightarrow{0} {7 \choose 7}$

This permutation is composed with the permutation $11$ times, a multiplication of $12$ permutations in total. Since $12 \ \text{mod} \ 3 = 0$

$$\begin{pmatrix}
    1 & 2 & 3 & 4 & 5 & 6 & 7 & 8\\
    4 & 8 & 5 & 6 & 2 & 7 & 3 & 1\\
\end{pmatrix}$$

## Problem 3

Find whether a permutation is odd or even:

$$\begin{pmatrix}
    1 & 2 & \dots & 97 & 98 & \dots &131 & 132 & \dots & 256\\
    160 & 161 & \dots & 256 & 126 & \dots & 159 & 1 & \dots & 125
\end{pmatrix}$$

## Problem 4

Calculate: 

$$\det\begin{vmatrix}
    0 & 0 & x & 0 & 0 & 2\\
    x & x & 9 & x & 0 & 1\\
    0 & 7 & 0 & 8 & 4 & 4\\
    0 & 2 & 0 & 0 & 0 & 7\\
    5 & 4 & x & x & 4 & 5\\
    0 & 4 & 2 & 2 & 5 & 5\\
\end{vmatrix}$$

---

## Problem 5

Find the coefficient before $x^5$ in the determinant expression:

$$\begin{vmatrix}
    2 & 5 & 10 & 9 & x & 8 & 10\\
    5 & 8 & 8 & x & 5 & 6 & 8\\
    10 & 8 & x & 8 & 7 & 8 & 9\\
    9 & x & 8 & 8 & 1 & 6 & 8\\
    x & 5 & 7 & 1 & 7 & 9 & x\\
    8 & 6 & 8 & 6 & 9 & x & 4\\
    10 & 8 & 9 & 8 & x & 4 & 6\\
\end{vmatrix}$$