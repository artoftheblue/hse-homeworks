# Linear Algebra, Homework 16

## Problem 1

Let in space $\mathbb{R}^4$ 

$$U=\langle(1,1,1,1), (-1,-2,0,1)\rangle \quad V=\langle(-1,-1,1,-1),(2,2,0,1)\rangle$$

Prove that $\mathbb{R}^4=U\oplus V$, and find the projection of vector $(4,2,4,4)$ to subspace $U$ parallel to $V$.

---

For $\mathbb{R}^4=U\oplus V$ to be true, we need all vectors to be linearly independent to each other (and the rank of such matrix should be 4):

$$\begin{pmatrix}
    1 & 1 & 1 & 1\\
    -1 & 2 & 0 & 1\\
    -1 & -1 & 1 & -1\\
    2 & 2 & 0 & 1\\
\end{pmatrix}\sim\begin{pmatrix}
    1 & 1 & 1 & 1\\
    0 & 3 & 1 & 2\\
    0 & 0 & 2 & 0\\
    0 & 0 & 0 & -1
\end{pmatrix}
$$

which implies that the rank is equal to $4$ and all vectors are linearly independent $\implies$ they generate a $\mathbb{R}^4$ space.

Write vectors into columns of matrix $S=(A|B)$ and solve the linear system of equations $Sx=v$:

$$\begin{pmatrix}
    1 & -1 & -1 & 2\\
    1 & -2 & -1 & 2\\
    1 & 0 & 1 & 0\\
    1 & 1 & -1 & 1
\end{pmatrix}\begin{pmatrix}
    u_1\\
    u_2\\
    w_1\\
    w_2\\
\end{pmatrix}=\begin{pmatrix}
    4\\
    2\\
    4\\
    4\\
\end{pmatrix}\implies\begin{pmatrix}
    u_1\\
    u_2\\
    w_1\\
    w_2\\
\end{pmatrix}=\begin{pmatrix}
    1\\
    2\\
    3\\
    4\\
\end{pmatrix}$$

$$v=u_1+2u_2+3w_1+4w_2\implies$$

the projection of $v$ to $U$ parallel to $W$ is

$$(1,1,1,1)+2(-1,-2,0,1)=(-1,-3,1,3)$$

## Problem 2

Prove that the space of matrices $\mathbf{M}_n(\mathbb{R})$ is a direct sum of the subspace of symmetric and the subspace of skew-symmetric matrices and find projections of matrix 

$$\begin{pmatrix}
    1 & 1 & \dots & 1\\
    0 & 1 & \dots & 1\\
    \vdots & \vdots & \ddots & \vdots\\
    0 & 0 & \dots & 1
\end{pmatrix}$$

to each of these subspaces parallel to the other subspaces.

---

Start with this little bit of logic $\forall A\in\mathbf{M}_n(\mathbb{R})$:

$$A = A$$

$$A = \frac{1}{2}A+\frac{1}{2}A$$

$$A = \frac{1}{2}A+\frac{1}{2}A^T+\frac{1}{2}A-\frac{1}{2}A^T$$

$$A=\underbrace{\frac{1}{2}(A+A^T)}_{A_1}+\underbrace{\frac{1}{2}(A-A^T)}_{A_2}$$

$A_1$ is symmetric since every $a_{1ij}=\frac{1}{2}(a_{ij}+a_{ji})=a_{1ji}$

$A_2$ is skew-symmetric since every $a_{2ij}=\frac{1}{2}(a_{ij}-a_{ji})=-\frac{1}{2}(a_{ji}-a_{ij})=-a_{2ji}$

and $A$ is per definition precisely 

$$A=A_1\oplus A_2$$

---

$$\begin{pmatrix}
    1 & 1 & \dots & 1\\
    0 & 1 & \dots & 1\\
    \vdots & \vdots & \ddots & \vdots\\
    0 & 0 & \dots & 1
\end{pmatrix}=\underbrace{\begin{pmatrix}
    1 & \frac{1}{2} & \dots & \frac{1}{2}\\
    \frac{1}{2} & 1 & \dots & \frac{1}{2}\\
    \vdots & \vdots & \ddots & \vdots\\
    \frac{1}{2} & \frac{1}{2} & \dots & 1
\end{pmatrix}}_{P_1}+\underbrace{\begin{pmatrix}
    0 & \frac{1}{2} & \dots & \frac{1}{2}\\
    -\frac{1}{2} & 0 & \dots & \frac{1}{2}\\
    \vdots & \vdots & \ddots & \vdots\\
    -\frac{1}{2} & -\frac{1}{2} & \dots & 0
\end{pmatrix}}_{P_2}$$

Thus, the projection matrix in $A_1$ parallel to $A_2$ is $P_1$ and the projection matrix in $A_2$ parallel to $A_1$ is $P_2$.


## Problem 3

Consider in space $M_n(\mathbb{R})$ subspaces $U$ and $W$, where $U$ consists of all symmetric matrices, and $W$, of all strictly upper triangular matrices. Prove that $M_n(\mathbb{R})=U\oplus W$, and find the projection of a matrix from the previous task to each of these subspaces along the other.

---

Both subspaces are obviously linearly independent because upper triangle matrices are not symmetric by any chance.

The basis for the subspace of symmetric matrices would consist of $n$ such matrices with $1$ on the diagonal

$$\begin{pmatrix}
    1 & 0 & \dots & 0\\
    0 & 0 & \dots & 0\\
    \vdots & \vdots & \ddots & \vdots\\
    0 & 0 & \dots & 0
\end{pmatrix}$$

and $\frac{1}{2}(n^2-n)$ matrices with a pair of ones mirrored along the main diagonal, $\frac{1}{2}(n^2+n)$ in total:

$$\begin{pmatrix}
    0 & 1 & \dots & 0\\
    1 & 0 & \dots & 0\\
    \vdots & \vdots & \ddots & \vdots\\
    0 & 0 & \dots & 0
\end{pmatrix}$$

The basis for the subspace of strictly upper triangular matrices would consist of $\frac{1}{2}(n^2-n)$ vectors in total:

$$\begin{pmatrix}
    0 & 1 & \dots & 0\\
    0 & 0 & \dots & 0\\
    \vdots & \vdots & \ddots & \vdots\\
    0 & 0 & \dots & 0
\end{pmatrix}$$

We can get a combination of two basis vectors by combining two last showcased respective vectors like this: 

$$\begin{pmatrix}
    0 & 0 & \dots & 0\\
    1 & 0 & \dots & 0\\
    \vdots & \vdots & \ddots & \vdots\\
    0 & 0 & \dots & 0
\end{pmatrix}=\begin{pmatrix}
    0 & 1 & \dots & 0\\
    1 & 0 & \dots & 0\\
    \vdots & \vdots & \ddots & \vdots\\
    0 & 0 & \dots & 0
\end{pmatrix}-\begin{pmatrix}
    0 & 1 & \dots & 0\\
    0 & 0 & \dots & 0\\
    \vdots & \vdots & \ddots & \vdots\\
    0 & 0 & \dots & 0
\end{pmatrix}$$

Therefore, we have an ability to customize any item of the matrix independently, which implies $U \oplus W$ generates $M_n(\mathbb{R})$.

---

Projections here are really simple since the diagonal is only reachable from the symmetric subspace and the rest of the matrix can be filled by using a unit strict upper triangle matrix:

$$\begin{pmatrix}
    1 & 1 & \dots & 1\\
    0 & 1 & \dots & 1\\
    \vdots & \vdots & \ddots & \vdots\\
    0 & 0 & \dots & 1
\end{pmatrix}=\underbrace{\begin{pmatrix}
    1 & 0 & \dots & 0 \\
    0 & 1 & \dots & 0\\
    \vdots & \vdots & \ddots & \vdots\\
    0 & 0 & \dots & 1
\end{pmatrix}}_{P_1}+\underbrace{\begin{pmatrix}
    0 & 1 & \dots & 1\\
    0 & 0 & \dots & 1\\
    \vdots & \vdots & \ddots & \vdots\\
    0 & 0 & \dots & 0
\end{pmatrix}}_{P_2}$$

Thus, the projection matrix in $U$ parallel to $W$ is $P_1$ and the projection matrix in $W$ parallel to $U$ is $P_2$.



## Problem 4

Consider in space $\mathbb{R}^5$ subspaces $U_1=\langle(1, 1, 1, 1, 0)\rangle, U_2=\langle(0, 1, 0, 0, -1)\rangle$ and $U_3$, which is a set of solutions of the following set of equations:

$$\begin{cases}
    x_1+x_2=0\\
    x_3-x_5=0
\end{cases}$$

Prove that $\mathbb{R}^5=U_1\oplus U_2\oplus U_3$.

---

Firstly, transition from a linear system of equations to a linear span for simplicity's sake:

$$\begin{pmatrix}
    1 & 1 & 0 & 0 & 0\\
    0 & 0 & 1 & 0 & -1\\
\end{pmatrix}$$

$$X=\begin{pmatrix}
    -x_2\\
    x_2\\
    x_5\\
    x_4\\
    x_5\\
\end{pmatrix}\implies\Phi_{U_3}=\begin{pmatrix}
    -1 & 0 & 0\\
    1 & 0 & 0\\
    0 & 0 & 1\\
    0 & 1 & 0\\
    0 & 0 & 1\\
\end{pmatrix}$$

which implies that $U_3=\langle(-1,1,0,0,0),(0,0,0,1,0),(0,0,1,0,1)\rangle$

Now, check whether the vectors are all linearly independent:

$$\begin{pmatrix}
    1 & 1 & 1 & 1 & 0\\
    0 & 1 & 0 & 0 & -1\\
    -1 & 1 & 0 & 0 & 0\\
    0 & 0 & 0 & 1 & 0\\
    0 & 0 & 1 & 0 & 1\\
\end{pmatrix}\sim\begin{pmatrix}
    1 & 1 & 1 & 1 & 0\\
    0 & 1 & 0 & 0 & -1\\
    0 & 0 & 1 & 1 & 0\\
    0 & 0 & 0 & 1 & 0\\
    0 & 0 & 0 & 0 & 1\\
\end{pmatrix}$$

since the rank of the matrix is $5$, then the vectors are linearly independent and $\mathbb{R}^4=U_1\oplus U_2\oplus U_3$ is true.

## Problem 5

Let $U$ be a subspace in $\mathbb{R}^4$ generated by vectors $(1,1,1,-1), (2, 1, 1,-2), (0, 1, 1, 0)$

---

Firstly, the basis of $U$ would be $\{(1,1,1,-1), (0, 1, 1, 0)\}$ since $(2, 1, 1,-2)=2\times(1,1,1,-1)- (0, 1, 1, 0)$

$$\begin{pmatrix}
    1 & 1 & 1 & -1\\
    0 & 1 & 1 & 0\\
\end{pmatrix}\sim\begin{pmatrix}
    1 & 0 & 0 & -1\\
    0 & 1 & 1 & 0
\end{pmatrix}$$

### Subproblem A

Construct (by presenting a basis) some complementary to $U$ subspace $W\subseteq\mathbb{R}^4$ (meaning such that $\mathbb{R}^4=U\oplus W$) 

---

$$\begin{pmatrix}
    1 & 0 & 0 & -1\\
    0 & 1 & 1 & 0\\
    0 & 0 & 1 & 0\\
    0 & 0 & 0 & 1
\end{pmatrix}$$

implies $W=\{(0,0,1,0),(0,0,0,1)\}$ is a valid complementary subspace $W$ such that $U\oplus W$ generate $\mathbb{R}^4$.

### Subproblem B

Construct (by presenting a basis) some other complementary to $U$ subspace $W'\subseteq\mathbb{R}^4$.

---

For the subspace to be different, its basis cannot be linearly dependent to the basis in subproblem A. For instance, take $\{(1, 2, 1, 1), (0, 0, 0, 1)\}$

$$\begin{pmatrix}
    1 & 0 & 0 & -1\\
    0 & 1 & 1 & 0\\
    1 & 2 & 1 & 1\\
    0 & 0 & 0 & 1
\end{pmatrix}\sim\begin{pmatrix}
    1 & 0 & 0 & -1\\
    0 & 1 & 1 & 0\\
    0 & 0 & 1 & -2\\
    0 & 0 & 0 & 1
\end{pmatrix}$$

which implies $W=\{(1, 2, 1, 1), (0, 0, 0, 1)\}$ is also a valid complementary subspace!

## Problem 6

In space $\mathbb{R}^4$, given a vector $v=(1,1,1,1)$ and a subspace $U$, which is the set of solutions to the system of equations

$$\begin{cases}
    x_1+x_3=0\\
    x_1+x_2-2x_4=0
\end{cases}$$

find some subspace $W\subseteq\mathbb{R}^4$ such that $\mathbb{R}^4=U\oplus W$ and the projection of a vector $v$ on $U$ along $W$ is equal to $(1,-1,-1,0)$.

---

Transition from a linear system of equations to a linear span:

$$\begin{pmatrix}
    1 & 0 & 1 & 0\\
    1 & 1 & 0 & -2\\
\end{pmatrix}\sim\begin{pmatrix}
    1 & 0 & 1 & 0\\
    0 & 1 & -1 & -2\\
\end{pmatrix}$$

$$X=\begin{pmatrix}
    -x_3\\
    x_3+2x_4\\
    x_3\\
    x_4\\
\end{pmatrix}\implies\Phi_U=\begin{pmatrix}
    -1 & 0\\
    1 & 2\\
    1 & 0\\
    0 & 1\\
\end{pmatrix}$$

$$U=\langle(-1, 1, 1, 0),(0, 2, 0, 1)\rangle$$

We know that 

$$v=(1,1,1,1)=\alpha_1(-1,1,1,0)+\alpha_2(0,2,0,1)+\beta_1 w_1+\beta_2 w_2$$

and 

$$\alpha_1(-1,1,1,0)+\alpha_2(0,2,0,1)=(1,-1,-1,0)$$

$$(1,1,1,1)=(1,-1,-1,0)+\beta_1 w_1+\beta_2 w_2$$

$$(0,2,0,1)=\beta_1 w_1+\beta_2 w_2$$

for instance,

$$w_1=(0,1,1,0), \quad w_2=(0,1,-1,1)$$

Now check whether a direct sum of $W=\langle(0,1,1,0),(0,1,-1,1) \rangle$ and $U$ generates $\mathbb{R}^4$. We would need to determine whether any of the vectors from the first basis can be expressing using vectors from the second basis and vice versa, but this is not possible since the matrix rank of 

$$\begin{pmatrix}
    -1 & 1 & 1 & 0\\
    0 & 2 & 0 & 1\\
    0 & 1 & 1 & 0\\
    0 & 1 & -1 & 1
\end{pmatrix}$$

is equal to $3$. Therefore, $W=\langle(0,1,1,0),(0,1,-1,1) \rangle$ is valid.
