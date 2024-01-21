# Linear Algebra, Homework 15 (in theory)

## Problem 1

Let vectors $e_1,\dots,e_n$ and $x$ be defined by their coordinates in some basis:

$$e_1=(2, 1, -3), e_2=(3, 2, -5), e_3=(1, -1, 1), x=(6,2, -7)$$

Prove that $e_1,\dots,e_n$ is also a basis in this space and find coordinates of vector $x$ in this basis.

---

Check whether the vectors $e_i$ are linearly independent:

$$
A=\begin{pmatrix}
    2 & 3 & 1\\
    1 & 2 & -1\\
    -3 & -5 & 1\\
\end{pmatrix} \sim \begin{pmatrix}
    0 & -1 & 3\\
    1 & 2 & -1\\
    0 & 1 & -2\\
\end{pmatrix} \sim \begin{pmatrix}
    1 & 2 & -1\\
    0 & -1 & 3\\
    0 & 0 & 1\\
\end{pmatrix}
$$

They are linearly independent; therefore, $e_i$ form a basis, q. e. d.

We need to find what vector gets "sent" to vector $x$ after the basis matrix is applied as follows: $A\overline{x}=x$, thus:

$$
\begin{pmatrix}
    2 & 3 & 1 & \bigm| & 6\\
    1 & 2 & -1 & \bigm| & 2\\
    -3 & -5 & 1 & \bigm| & -7\\
\end{pmatrix}\sim \begin{pmatrix}
    1 & 2 & -1 & \bigm| & 2\\
    0 & -1 & 3 & \bigm| & 2\\
    0 & 1 & -2 & \bigm| & -1\\
\end{pmatrix}\sim$$

$$\begin{pmatrix}
    1 & 2 & -1 & \bigm| & 2\\
    0 & -1 & 3 & \bigm| & 2\\
    0 & 0 & 1 & \bigm| & 1\\
\end{pmatrix}\sim\begin{pmatrix}
    1 & 0 & 5 & \bigm| & 6\\
    0 & 1 & -3 & \bigm| & -2\\
    0 & 0 & 1 & \bigm| & 1\\
\end{pmatrix}\sim\begin{pmatrix}
    1 & 0 & 0 & \bigm| & 1\\
    0 & 1 & 0 & \bigm| & 1\\
    0 & 0 & 1 & \bigm| & 1\\
\end{pmatrix}
$$

**Answer:**

$$\overline{x}=\begin{pmatrix}
1 \\
1 \\
1 \\
\end{pmatrix}
$$

## Problem 2

How would a basis conversion matrix change if one would write the vectors of each of bases in a reversed order?

---

> It is pretty obvious that this matrix would be a symmetry of some sort.

Assume the original basis conversion matrix is something like this (example given for $3$ dimensions for simplicity's sake). 

$$A=\begin{pmatrix}
    a_{11} & a_{12} & a_{13}\\
    a_{21} & a_{22} & a_{23}\\
    a_{31} & a_{32} & a_{33}\\
\end{pmatrix}$$

Reversing the order of dimension of one of the bases would have the same effect as reversing (mirroring) lines over their center. Similarly, reversing the order of dimensions of the second basis would have an effect of reversing (mirroring) columns over their center. 

Both these transformations could be applied in any order, as shown by the matrix multiplication below:

$$\begin{pmatrix}
    0 & 0 & 1\\
    0 & 1 & 0\\
    1 & 0 & 1\\
\end{pmatrix}\begin{pmatrix}
    a_{11} & a_{12} & a_{13}\\
    a_{21} & a_{22} & a_{23}\\
    a_{31} & a_{32} & a_{33}\\
\end{pmatrix}\begin{pmatrix}
    0 & 0 & 1\\
    0 & 1 & 0\\
    1 & 0 & 1\\
\end{pmatrix}=\begin{pmatrix}
    a_{33} & a_{32} & a_{31}\\
    a_{23} & a_{22} & a_{21}\\
    a_{13} & a_{12} & a_{11}\\
\end{pmatrix}$$

Therefore, **the described transformation is identical to a center symmetry of a matrix.**

## Problem 4

Subspaces $U$ and $W$ in $F^4$ are defined as set of solutions to HSLUs

$$\begin{cases}
x_1+2x_2+x_4=0\\
x_1+x_2+x_3=0\\
\end{cases} \ \ \text{and} \ \  \begin{cases}
    x_1+x_3=0\\
    x_1+3x_2+x_4=0
\end{cases}$$

respectively. Find the basis in $U\cap W$ and basis in $U + W$.

---

Take the intersection of two HSLUs to find $U \cap W$:

$$\begin{pmatrix}
    1 & 2 & 0 & 1\\
    1 & 1 & 1 & 0\\
    1 & 0 & 1 & 0\\
    1 & 3 & 0 & 1\\
\end{pmatrix}\sim\begin{pmatrix}
    1 & 2 & 0 & 1\\
    0 & -1 & 1 & -1\\
    0 & -2 & 1 & -1\\
    0 & 1 & 0 & 0\\
\end{pmatrix}\sim\begin{pmatrix}
    1 & 0 & 0 & 1\\
    0 & 0 & 1 & -1\\
    0 & 0 & 1 & -1\\
    0 & 1 & 0 & 0\\
\end{pmatrix}\sim\begin{pmatrix}
    1 & 0 & 0 & 1\\
    0 & 0 & 0 & 0\\
    0 & 0 & 1 & -1\\
    0 & 1 & 0 & 0\\
\end{pmatrix}\implies$$

The solution is 

$$\begin{pmatrix}
    -x_4\\
    0\\
    x_4\\
    x_4\\
\end{pmatrix}$$

**And the basis in $U \cap W$ would be something like**

$$\begin{pmatrix}
    -1\\
    0\\
    1\\
    1\\
\end{pmatrix}$$

---

Now, find bases in both $U$ and $W$:

$$U\colon \begin{pmatrix} 
    1 & 2 & 0 & 1\\
    1 & 1 & 1 & 0\\
\end{pmatrix}\sim\begin{pmatrix} 
    1 & 0 & 2 & -1\\
    0 & 1 & -1 & 1\\
\end{pmatrix}\implies$$

The solution would be 

$$\begin{pmatrix}
    -2x_3+x_4\\
    x_3-x_4\\
    x_3\\
    x_4
\end{pmatrix}$$

Thus, the basis for $U$ would consist of vectors $\{(-2, 1, 1, 0), (1, -1, 0, 1)\}$.

$$W\colon \begin{pmatrix} 
    1 & 0 & 1 & 0\\
    1 & 3 & 0 & 1\\
\end{pmatrix}\sim\begin{pmatrix} 
    1 & 0 & 1 & 0\\
    0 & 1 & -\frac{1}{3} & \frac{1}{3}\\
\end{pmatrix}\implies$$

The solution would be

$$\begin{pmatrix}
    -x_3\\
    \frac{1}{3}(x_3-x_4)\\
    x_3\\
    x_4
\end{pmatrix}$$

Thus, the basis for $U$ would consist of vectors $\{(-3, 1, 3, 0), (0, -1, 0, 3)\}$.

Now, $U+W$ would be the linear span of all the basis vectors of $U$ and $W$. To find the basis, write another matrix:

$$\begin{pmatrix}
    -2 & 1 & -3 & 0\\
    1 & -1 & 1 & -1\\
    1 & 0 & 3 & 0\\
    0 & 1 & 0 & 3\\
\end{pmatrix}\sim\begin{pmatrix}
    1 & 0 & 0 & -2\\
    0 & 1 & 0 & -3\\
    0 & 0 & 1 & -1\\
    0 & 0 & 0 & 0\\
\end{pmatrix}\implies$$

Thus, the basis for $U+W$ would consist of vectors $\{(-2, 1, 1, 0), (1, -1, 0, 1), (-3, 1, 3, 0)\}$

## Problem 5

Subspaces $U$ and $W$ in $F^4$ are defined as set of solutions to HSLUs

$$\begin{cases}
x_1+x_2-x_5=0\\
x_2+x_3+x_5=0\\
x_3+x_4+x_5=0\\
\end{cases} \ \ \text{and} \ \  \begin{cases}
    x_1+x_3+x_5=0\\
    2x_2+3x_2+x_4=0\\
    x_1+2x_2+x_3+2x_4-x_5=0
\end{cases}$$

respectively. Find $\text{dim}(U\cap W)$ and $\text{dim}(U + W)$.

---

For $W \cap W$, do the same thing as above:

$$\begin{pmatrix}
    1 & 1 & 0 & 0 & -1\\
    0 & 1 & 1 & 0 & 1\\
    0 & 0 & 1 & 1 & 1\\
    1 & 0 & 1 & 0 & 1\\
    0 & 2 & 1 & 1 & 0\\
    1 & 2 & 1 & 2 & -1\\
\end{pmatrix}\sim\begin{pmatrix}
    1 & 1 & 0 & 0 & -1\\
    0 & 1 & 1 & 0 & 1\\
    0 & 0 & 1 & 1 & 1\\
    0 & -1 & 1 & 0 & 2\\
    0 & 2 & 1 & 1 & 0\\
    0 & 1 & 1 & 2 & 0\\
\end{pmatrix}\sim\begin{pmatrix}
    1 & 0 & -1 & 0 & -2\\
    0 & 1 & 1 & 0 & 1\\
    0 & 0 & 1 & 1 & 1\\
    0 & 0 & 2 & 0 & 3\\
    0 & 0 & -1 & 1 & -2\\
    0 & 0 & 0 & 2 & -1\\
\end{pmatrix}\sim$$

$$\begin{pmatrix}
    1 & 0 & 0 & 1 & -1\\
    0 & 1 & 0 & -1 & 0\\
    0 & 0 & 1 & 1 & 1\\
    0 & 0 & 0 & -2 & 1\\
    0 & 0 & 0 & 2 & -1\\
    0 & 0 & 0 & 2 & -1\\
\end{pmatrix}\sim\begin{pmatrix}
    1 & 0 & 0 & 1 & -1\\
    0 & 1 & 0 & -1 & 0\\
    0 & 0 & 1 & 1 & 1\\
    0 & 0 & 0 & 1 & 0.5\\
    0 & 0 & 0 & 0 & 0\\
    0 & 0 & 0 & 0 & 0\\
\end{pmatrix}\sim\begin{pmatrix}
    1 & 0 & 0 & 0 & \diamond\\
    0 & 1 & 0 & 0 & \diamond\\
    0 & 0 & 1 & 0 & \diamond\\
    0 & 0 & 0 & 1 & 0.5\\
    0 & 0 & 0 & 0 & 0\\
    0 & 0 & 0 & 0 & 0\\
\end{pmatrix}\implies$$

$$\text{dim}(U\cap W)=5-4=1$$

We could use the following formula to get the required answer:

$$\text{dim}(U + W)=\text{dim}U+\text{dim}W-\text{dim}(U \cap W)$$

Find dimensions of each of the subspaces:

$$U\colon\begin{pmatrix}
    1 & 1 & 0 & 0 & -1\\
    0 & 1 & 1 & 0 & 1\\
    0 & 0 & 1 & 1 & 1
\end{pmatrix}\sim\begin{pmatrix}
    1 & 0 & 0 & \diamond & \diamond\\
    0 & 1 & 0 & \diamond & \diamond\\
    0 & 0 & 1 & 1 & 1
\end{pmatrix}\implies\dim U=5-3=2$$

$$W\colon\begin{pmatrix}
    1 & 0 & 1 & 0 & 1\\
    0 & 2 & 1 & 1 & 0\\
    1 & 2 & 1 & 2 & -1
\end{pmatrix}\sim\begin{pmatrix}
    1 & 0 & 0 & \diamond & \diamond\\
    0 & 1 & 0 & \diamond & \diamond\\
    0 & 0 & 1 & \diamond & \diamond
\end{pmatrix}\implies\dim U=5-3=2$$

Therefore, **the answer:**

$$\text{dim}(U + W)=2+2-1=3$$

## Problem 6

Find dimensions of the sum and the intersection of linear spans of vectors in $\mathbb{R}^4$:

### Subproblem A

$$S=\langle(1, 1, 1, 1), (1, -1, 1, -1), (1, 3, 1, 3)\rangle$$

$$T=\langle(1, 2, 0, 2), (1, 2, 1, 2), (3, 1, 3, 1)\rangle$$

---

It is obvious that $2\times(1, 1, 1, 1)- (1, -1, 1, -1)=(1, 3, 1, 3)$, which implies that $\dim S=2$.

As for $T$:

$$\begin{pmatrix}
    1 & 1 & 3\\
    2 & 2 & 1\\
    0 & 1 & 3\\
    2 & 2 & 1\\
\end{pmatrix}\sim\begin{pmatrix}
    1 & 1 & 3\\
    0 & 0 & -5\\
    0 & 1 & 3\\
    0 & 0 & 0\\
\end{pmatrix}$$

from which $\dim T=3$ is obvious.

Now, find the size of $S+T$:

$$\begin{pmatrix}
    1 & 1 & 1 & 1 & 1 & 3\\
    1 & -1 & 3 & 2 & 2 & 1\\
    1 & 1 & 1 & 0 & 1 & 3\\
    1 & -1 & 3 & 2 & 2 & 1\\
\end{pmatrix}\sim\begin{pmatrix}
    1 & 0 & 2 & 0 & \diamond & \diamond\\
    0 & 1 & -1 & 0 & \diamond & \diamond\\
    0 & 0 & 0 & 1 & \diamond & \diamond\\
    0 & 0 & 0 & 0 & 0 & 0\\
\end{pmatrix}$$

which implies $\dim(S+T)=3$

Now per our awesome formula **get the answer**: 

$$\dim(S\cap T)=-\dim(S+T)+\dim S+\dim T=-3+2+3=2$$

### Subproblem B

$$S=\langle(2, -1, 0, -2), (3, -2, 1, 0), (1, -1, 1, -1)\rangle$$

$$T=\langle(3, -1, -1, 0), (0, -1, 2, 3), (5, -2, -1, 0)\rangle$$

---

Do the same things all over again:

$$\begin{pmatrix}
    2 & 3 & 1\\
    -1 & -2 & -1\\
    0 & 1 & 1\\
    -2 & 0 & -1\\
\end{pmatrix}\sim\begin{pmatrix}
    1 & 0 & 0\\
    0 & 1 & 0\\
    0 & 0 & 1\\
    0 & 0 & 0\\
\end{pmatrix}\implies\dim S=3$$

$$\begin{pmatrix}
    -3 & 0 & -5\\
    1 & 1 & 2\\
    1 & -2 & 1\\
    0 & -3 & 0\\
\end{pmatrix}\sim\begin{pmatrix}
    1 & 0 & 0\\
    0 & 1 & 0\\
    0 & 0 & 1\\
    0 & 0 & 0\\
\end{pmatrix}\implies\dim T=3$$

$$\begin{pmatrix}
    2 & 3 & 1 & -3 & 0 & -5\\
    -1 & -2 & -1 & 1 & 1 & 2\\
    0 & 1 & 1 & 1 & -2 & 1\\
    -2 & 0 & -1 & 0 & -3 & 0\\
\end{pmatrix}\sim\begin{pmatrix}
    1 & 0 & 0 & \diamond & \diamond & \diamond\\
    0 & 1 & 0 & \diamond & \diamond & \diamond\\
    0 & 0 & 1 & \diamond & \diamond & \diamond\\
    0 & 0 & 0 & 0 & 0 & 0\\
\end{pmatrix}\implies\dim(S+T)=3$$

Therefore, the **answer** is $\dim(S\cap T)=-\dim(S+T)+\dim S+\dim T=-3+3+3=3$

## Problem 9

Let $L_1$ and $L_2$ be subspaces of a finite vector space $V$. Prove that if $\dim(L_1+L_2)=1+\dim(L_1\cap L_2)$, then sum $L_1+L_2$ is equal to one of these subspaces and $L_1 \cap L_2$ to the other.

---

Let's try to see what $\dim(L_1+L_2)=1+\dim(L_1\cap L_2)$ implies. Dimension of the intersection is precisely $1$ higher than the dimension of the sum, therefore there is a single vector which is a part  