# Individual Homework, Variant 17

> $\sim$ denotes a row echelon transformation using Gaussian elimination.

## Problem 1

Represent matrix 

$$A=\begin{pmatrix}
    5 & -18 & 17 & 1 & -6\\
    -17 & -9 & 19 & 38 & -18\\
    -39 & 10 & -18 & 49 & 14\\
    -23 & 17 & -40 & 10 & 38\\
    15 & 2 & -20 & -37 & 26\\
\end{pmatrix}$$

as a sum of $r$ matrices of rank $1$, where $r=\text{rk}A$.

---

Reduce the matrix to a row echelon form:

$$A=\begin{pmatrix}
    5 & -18 & 17 & 1 & -6\\
    -17 & -9 & 19 & 38 & -18\\
    -39 & 10 & -18 & 49 & 14\\
    -23 & 17 & -40 & 10 & 38\\
    15 & 2 & -20 & -37 & 26\\
\end{pmatrix}\sim\begin{pmatrix}
    1 & 0 & 0 & -\frac{103}{67} & \frac{2}{67}\\
    0 & 1 & 0 & \frac{13}{67} & -\frac{64}{67}\\
    0 & 0 & 1 & \frac{48}{67} & -\frac{92}{67}\\
    0 & 0 & 0 & 0 & 0\\
    0 & 0 & 0 & 0 & 0\\
\end{pmatrix}$$

This gives us $r=\text{rk}A=3$ and we need to represent the last two columns as the sum of the first two. Gladly, the linear combinations of those columns are given in the matrix above:

$$A^{(4)}=\frac{1}{67}\left(-103A^{(1)}+13A^{(2)}+48A^{(3)}\right)$$

$$A^{(5)}=\frac{1}{67}\left(2A^{(1)}-64A^{(2)}-92A^{(3)}\right)$$

Thus, we may split this matrix into $3$ basis matrices of $\text{rk} 1$, expressing vectors from $A^{(1)}$ to $A^{(3)}$ as a linear combination of vectors $A^{(4)}$ and $A^{(5)}$:

$$A_1=\frac{1}{67}\begin{pmatrix}
    335 & 0 & 0 & -515 & 10\\
    -1139 & 0 & 0 & 1751 & -34\\
    -2613 &  0 & 0 & 4017 & -78\\
    -1541 & 0 & 0 & 2369 & -46\\
    1005 & 0 & 0 & -1545 & 30
\end{pmatrix}$$

$$A_2=\frac{1}{67}\begin{pmatrix}
    0 & -1206 & 0 & -234 & 1152\\
    0 &-603 & 0 & -117 & 576\\
    0 & 670 & 0 & 130 & -640\\
    0 & 1139 & 0 & 221 & -1088\\
    0 & 134 & 0 & 26 & -128\\
\end{pmatrix}$$

$$A_3=\frac{1}{67}\begin{pmatrix}
    0 & 0 & 1139 & 816 & -1564\\
    0 & 0 & 1273 & 912 & -1748\\
    0 & 0 & -1206 & -864 & 1656\\
    0 & 0 & -2680 & -1920 & 3680\\
    0 & 0 & -1340 & -960 & 1840
\end{pmatrix}$$

and 

$$A=A_1+A_2+A_3$$

## Problem 2

In space $\mathbb{R}^3$ there are two bases $\mathbf{e}=(e_1, e_2, e_3)$ and $\mathbf{e}'=(e_1', e_2', e_3')$, where

$$e_1=(-1, -1, 1), \quad e_2=(2,2,3), \quad, e_3=(1, -2, -2)$$

$$e_1'=(-1,7,6), \quad e_2'=(1,8,-9), \quad e'_3=(-3, 11,-4)$$

and vector $v$ in basis $\mathbf{e}$ with coordinates $(-1,2,5)$.

Translate from the basis $\mathbf(e)$

### Subproblem A

Prove that sets of vectors $\mathbf{e}$ and $\mathbf{e}'$ are truly bases in $\mathbb{R}^3$

---

Check for linear dependency:

$$\begin{pmatrix}
    -1 & 2 & 1\\
    -1 & 2 & 2\\
    1 & 3 & -2
\end{pmatrix}\sim\begin{pmatrix}
    -1 & 2 & 1\\
    0 & 5 & -1\\
    0 & 0 & 1
\end{pmatrix}$$

$$\begin{pmatrix}
    -1 & 1 & -3\\
    7 & 8 & 11\\
    6 & -9 & -4\\
\end{pmatrix}\sim\begin{pmatrix}
    -1 & 1 & -3\\
    0 & 15 & -10\\
    0 & 0 & -24
\end{pmatrix}$$

Therefore, the bases $\mathbf{e, e}'$ are truly bases.

### Subproblem B

Find the transformation matrix from basis $\mathbf{e}$ to basis $\mathbf{e}'$

---

Write all the vectors into columns and reduce rows:

$$\begin{pmatrix}
    -1 & 2 & 1 & -1 & 1 & -3\\
    -1 & 2 & 2 & 7 & 8 & 11\\
    1 & 3 & -2 & 6 & -9 & 4\\
\end{pmatrix}\sim\begin{pmatrix}
    1 & 0 & 0 & \frac{71}{5} & \frac{28}{5} & 23\\
    0 & 1 & 0 & \frac{13}{5} & -\frac{1}{5} & 3\\
    0 & 0 & 1 & 8 & 7 & 14\\
\end{pmatrix}$$

which implies that the last $3$ columns is the transformation matrix from $\textbf{e}$ to $\textbf{e}'$:

$$T^{\textbf{e}\to\textbf{e}'}=\frac{1}{5}\begin{pmatrix}
    71 & 28 & 115\\
    13 & -1 & 15\\
    40 & 35 & 70\\
\end{pmatrix}$$

### Subproblem C

Find coordinates of a vector $v$ in basis $\mathbf{e}'$

---

To do this, we need to find $v'$ in $v=Tv'\implies v'=T^{-1}v$:

First, find $T^{-1}$ using Gaussian elimination:

$$\begin{pmatrix}
    \frac{71}{5} & \frac{28}{5} & 23 & 1 & 0 & 0\\
    \frac{13}{5} & -\frac{1}{5} & 3 & 0 & 1 & 0\\
    8 & 7 & 14 & 0 & 0 & 1\\
\end{pmatrix}\sim\frac{1}{240}\begin{pmatrix}
    \frac{1}{240} & 0 & 0 & -119 & 413 & 107\\
    0 & \frac{1}{240} & 0 & -62 & 74 & 86\\
    0 & 0 & \frac{1}{240} & 99 & -273 & -87
\end{pmatrix}$$

which implies

$$T^{-1}=\frac{1}{240}\begin{pmatrix}
    -119 & 413 & 107\\
    -62 & 74 & 86\\
    99 & -273 & 87
\end{pmatrix}$$

and finally **find the coordinates of the vector**
 
$$v'=\frac{1}{240}\begin{pmatrix}
    -119 & 413 & 107\\
    -62 & 74 & 86\\
    99 & -273 & 87
\end{pmatrix}\begin{pmatrix}
    -1\\
    2\\
    5
\end{pmatrix}=\frac{1}{24}\begin{pmatrix}
    148\\
    64\\
    -21
\end{pmatrix}$$

## Problem 3

Find the basis and the dimension of each of the subspaces $L_1, L_2, U=L_1+L_2, W=L_1\cap L_2$ of space $\mathbb{R}^5$ if $L_1$ is a linear span of vectors

$$a_1=(3,3,0,-4,1),\quad a_2=(-2,0,4,-1,1), \quad a_3=(-1,2,1,4,4), \quad a_4=(-13, -9, 8, 10, -1)$$

and $L_2$ is a linear span of vectors 

$$b_1=(0, 4, -2, 9, 7), \quad b_2=(16, 1, -19, -1, -3), \quad b_3=(-7, -3, 8, 2, 1), \quad b_4=(2, -5, -3, 3, -1)$$

---

Basis and dimension for $L_1$:

$$\begin{pmatrix}
    3 & -2 & -1 & -13\\
    3 & 0 & 2 & -9\\
    0 & 4 & 1 & 8\\
    -4 & -1 & 4 & 10\\
    1 & 1 & 4 & -1\\
\end{pmatrix}\sim\begin{pmatrix}
    1 & 0 & 0 & -3\\
    0 & 1 & 0 & 2\\
    0 & 0 & 1 & 0\\
    0 & 0 & 0 & 0\\
    0 & 0 & 0 & 0\\
\end{pmatrix}$$

which implies basis of $L_1$ is $\langle a_1,a_2,a_3\rangle$ and $\dim L_1=3$.

Basis and dimension for $L_2$:

$$\begin{pmatrix}
    0 & 16 & -7 & 2\\
    4 & 1 & -3 & -5\\
    -2 & -19 & 8 & -3\\
    9 & -1 & 2 & 3\\
    7 & -3 & 1 & -1
\end{pmatrix}\sim\begin{pmatrix}
    1 & 0 & 0 & 0\\
    0 & 1 & 0 & 1\\
    0 & 0 & 1 & 2\\
    0 & 0 & 0 & 0\\
    0 & 0 & 0 & 0\\
\end{pmatrix}$$

which implies basis of $L_2$ is $\langle b_1,b_2,b_3\rangle$ and $\dim L_2=3$.

To find the basis and dimension of $L_1+L_2$, write all vectors into columns and commense row echelonization:

$$\begin{pmatrix}
    3 & -2 & -1 & -13 & 0 & 16 & -7 & 2\\
    3 & 0 & 2 & -9 & 4 & 1 & -3 & -5\\
    0 & 4 & 1 & 8 & -2 & -19 & 8 & -3\\
    -4 & -1 & 4 & 10 & 9 & -1 & 2 & 3\\
    1 & 1 & 4 & -1 & 7 & -3 & 1 & -1
\end{pmatrix}\sim$$

$$\begin{pmatrix}
    1 & 0 & 0 & -3 & 0 & 0 & -1 & -2\\
    0 & 1 & 0 & 2 & -1 & 0 & 2 & 4\\
    0 & 0 & 1 & 0 & 2 & 0 & 0 & 0\\
    0 & 0 & 0 & 0 & 0 & 1 & 0 & 1\\
    0 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\
\end{pmatrix}$$

which implies basis of $L_1+L_2$ is $\langle a_1,a_2,a_3,b_2\rangle$ and $\dim L_1+L_2=4$.

> Notice that technically I could have use the basis vectors, but I was too lazy to change the matrices around for the kjgkhbillionth time

Finally, to find the basis and dimension of $L_1\cap L_2$, write all vectors as columns and find the fundamental system of solutions. We have already almost done that in the previous point, so let's continue:

$$X=\begin{pmatrix}
    3\alpha_4+\beta_3+2\beta_4\\
    -2\alpha_4+\beta_1-2\beta_3-4\beta_4\\
    -2\beta_1\\
    \alpha_4\\
    \beta_1\\
    -\beta_4\\
    \beta_3\\
    \beta_4
\end{pmatrix}$$

$$\begin{pmatrix}
    \Phi_{L_1}\\
    \hline
    \Phi_{L_2}
\end{pmatrix}=\begin{pmatrix}
    3 & 0 & 1 & 2\\
    -2 & 1 & -2 & -4\\
    0 & -2 & 0 & 0\\
    1 & 0 & 0 & 0\\
    \hline
    0 & 1 & 0 & 0\\
    0 & 0 & 0 & -1\\
    0 & 0 & 1 & 0\\
    0 & 0 & 0 & 1
\end{pmatrix}$$

Finally, find $L_1\Phi_{L_1}=-L_2\Phi_{L_2}$:

$$\begin{pmatrix}
    0 & 16 & -7 & 2\\
    4 & 1 & -3 & -5\\
    -2 & -19 & 8 & -3\\
    9 & -1 & 2 & 3\\
    7 & -3 & 1 & -1
\end{pmatrix}\begin{pmatrix}
    0 & 1 & 0 & 0\\
    0 & 0 & 0 & -1\\
    0 & 0 & 1 & 0\\
    0 & 0 & 0 & 1
\end{pmatrix}=\begin{pmatrix}
    0 & 0 & 7 & 14\\
    0 & -4 & 3 & 6\\
    0 & 2 & -8 & -16\\
    0 & -9 & -2 & -4\\
    0 & -7 & -1 & -2
\end{pmatrix}$$

The third and the fourth vectors are proportional to each other, so we may simply drop the fourth one + obviously drop the first one.

Therefore, the basis of $L_1\cap L_2$ is $\langle(0,-4,2,-9,-7),(7,3,-8,-2,-1)\rangle$ and $\dim L_1\cap L_2=2$.

---

## Problem 4

Let $U$ be a subspace in $\mathbb{R}^5$ generated by vectors

$$v_1=(-12, -1, -5, 13, -10), \quad v_2=(14,10,13,12,-11), \quad v_3=(-4, -3, 7, 1, 8), \quad v_4=(34,9,30,-13,17)$$

Present a basis of some subspace $W\subseteq\mathbb{R}^5$ such that $\mathbb{R}^5=U\oplus W$ and $W$ is not represented by a linear span of just vectors of a standard basis of space $\mathbb{R}^5$.

---

Check whether the given vectors are linearly dependent and find the basis in $U$:

$$\begin{pmatrix}
    -12 & 14 & -4 & 34\\
    -1 & 10 & -3 & 9\\
    -5 & 13 & 7 & 30\\
    13 & 12 & 1 & -13\\
    -10 & -11 & 8 & 17\\
\end{pmatrix}\sim\begin{pmatrix}
    1 & 0 & 0 & -2\\
    0 & 1 & 0 & 1\\
    0 & 0 & 1 & 1\\
    0 & 0 & 0 & 0\\
    0 & 0 & 0 & 0
\end{pmatrix}$$

Therefore, basis of $U$ is $\langle v_1,v_2,v_3\rangle$. Let $W=\langle(1,1,1,1,1),(1,0,1,0,1)\rangle$. Check whether this is a complementary subspace to $U$ by checking if $U\oplus W$ form a basis:

$$
\begin{pmatrix}
    -12 & 14 & -4 & 1 & 1\\
    -1 & 10 & -3 & 1 & 0\\
    -5 & 13 & 7 & 1 & 1\\
    13 & 12 & 1 & 1 & 0\\
    -10 & -11 & 8 & 1 & 1\\
\end{pmatrix}\sim\begin{pmatrix}
    1 & 0 & 0 & 0 & 0\\
    0 & 1 & 0 & 0 & 0\\
    0 & 0 & 1 & 0 & 0\\
    0 & 0 & 0 & 1 & 0\\
    0 & 0 & 0 & 0 & 1\\
\end{pmatrix}
$$

Therefore, $U\oplus W$ generate $\mathbb{R}^5$. What remains is to check whether linear spans of $W$ and $\langle e_1, e_2, e_3, e_4, e_5\rangle$ are the same. They are not because, for instance, it's impossible to find such $n, k, 0\leqslant i \leqslant 5$ that $e_i=n(1,1,1,1,1)+k(1,0,1,0,1)$, thus $W=\langle(1,1,1,1,1),(1,0,1,0,1)\rangle$ is valid and is the answer to this problem.

## Problem 5

In space $\text{Mat}_{2\times2}(\mathbb{R})$ consider subspaces $U=\langle v_1, v_2\rangle$ and  $W=\langle v_3, v_4\rangle$, where

$$v_1=\begin{pmatrix}
    -13 & -2\\
    -6 & 12\\
\end{pmatrix}, \quad v_2= \begin{pmatrix}
    -11 & 13\\
    9 & 12\\
\end{pmatrix}, \quad v_3=\begin{pmatrix}
    11 & -12\\
    -5 & -4\\
\end{pmatrix}, \quad v_4=\begin{pmatrix}
    6 & 0\\
    7 & -15
\end{pmatrix}$$

> Note that I will convert all matrices to a vector like follows for convenience's sake: 
> 
> $$\begin{pmatrix}
    a_{11} & a_{12}\\
    a_{21} & a_{22}
    \end{pmatrix}\mapsto\begin{pmatrix}
        a_{11}\\
        a_{12}\\
        a_{21}\\
        a_{22}
    \end{pmatrix}
    $$

### Subproblem A

Prove that $\text{Mat}_{2\times2}(\mathbb{R}) = U \oplus W$.

Transform all matrices to a vector like above and check whether the direct sum forms a basis in $\mathbb{R}^4$ since it was proven on the seminars/lectures that matrices $n\times n$ are isomorphic to vectors in $\mathbb{R}^{n^2}$. It's obvious that the linear spans of $U$ and $W$ have dimensions equal to $2$, therefore checking whether $U\oplus W$ forms a basis would be sufficient to prove that $\text{Mat}_{2\times2}(\mathbb{R}) = U \oplus W$. For this, check linear dependency as many times above (vectors in columns):

$$\begin{pmatrix}
    -13 & -11 & 11 & 6\\
    -2 & 13 & -12 & 0\\
    -6 & 9 & -5 & 7\\
    12 & 12 & -4 & -15
\end{pmatrix}\sim\begin{pmatrix}
    1 & 0 & 0 & 0\\
    0 & 1 & 0 & 0\\
    0 & 0 & 1 & 0\\
    0 & 0 & 0 & 1
\end{pmatrix}$$

Therefore, $\text{Mat}_{2\times2}(\mathbb{R}) = U \oplus W$ is indeed true.

### Subproblem B

Find the projection of a vector 

$$\xi=\begin{pmatrix}
    -7 & -1\\
    5 & 5
\end{pmatrix}$$

to subspace $W$ parallel to subspace $U$.

---

Write vectors $u_1, u_2, w_1, w_2$ into columns and solve $Sx=\xi$

$$\begin{pmatrix}
    -13 & -11 & 11 & 6\\
    -2 & 13 & -12 & 0\\
    -6 & 9 & -5 & 7\\
    12 & 12 & -4 & -15
\end{pmatrix}\begin{pmatrix}
    x_1\\
    x_2\\
    y_1\\
    y_2\\
\end{pmatrix}=\begin{pmatrix}
    -7\\
    -1\\
    5\\
    5
\end{pmatrix}$$

$$\begin{pmatrix}
    -13 & -11 & 11 & 6 & \bigm| & -7\\
    -2 & 13 & -12 & 0 & \bigm| & -1\\
    -6 & 9 & -5 & 7 & \bigm| & 5\\
    12 & 12 & -4 & -15 & \bigm| & 5
\end{pmatrix}\sim\begin{pmatrix}
    1 & 0 & 0 & 0 & \bigm| & 1\\
    0 & 1 & 0 & 0 & \bigm| & 1\\
    0 & 0 & 1 & 0 & \bigm| & 1\\
    0 & 0 & 0 & 1 & \bigm| & 1
\end{pmatrix}$$

Funnily enough, 

$$x=v_1+v_2+v_3+v_4$$

Therefore, projection of $\xi$ on $W$ along $u$ is $v_3+v_4$.

Finally, **the answer**

$$\overline{\xi}=\begin{pmatrix}
    11 & -12\\
    -5 & -4\\
\end{pmatrix}+\begin{pmatrix}
    6 & 0\\
    7 & -15
\end{pmatrix}=\begin{pmatrix}
    17 & -12\\
    2 & -19\\
\end{pmatrix}$$