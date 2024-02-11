# Linear Algebra, Homework 18

## Problem 1 

Linear mapping $\varphi\colon\mathbb{R}^4\mapsto\mathbb{R}^3$ in a pair of standard bases has a matrix $\begin{pmatrix}
    1 & 1 & 0 & 2\\
    3 & -3 & 2 & 0\\
    2 & -1 & 1 & 1
\end{pmatrix}$. Find the basis of an image of this linear mapping.

---

Firstly, solve $Ax=0$ and find what variables are main:

$$\begin{pmatrix}
    1 & 1 & 0 & 2\\
    3 & -3 & 2 & 0\\
    2 & -1 & 1 & 1
\end{pmatrix}\sim\begin{pmatrix}
    1 & 0 & \frac{1}{3} & 1\\
    0 & 1 & -\frac{1}{3} & 1\\
    0 & 0 & 0 & 0
\end{pmatrix}$$

This means that since we are just searching for the basis to be able to get all possible vectors that the matrix can send vectors to, we just take the first two columns of the matrix above to get the basis of an image (since all other bases are standard).

$$\text{Im}\,\varphi=\langle(1, 3, 2), (1, -3, -1)\rangle$$

## Problem 2

Find the basis of an image of a linear mapping $\varphi\colon M_2(\mathbb{R})\mapsto M_2(\mathbb{R}),\varphi(X)=AX$, where $A=\begin{pmatrix}
    1 & 2\\
    2 & 4
\end{pmatrix}$

---

Let's find $A(\varphi,\mathbf{e},\mathbf{f})$ by checking what vectors of the standard basis get sent to there, and then establish an isomorphism between matrices and vectors:

$$\varphi(e_1)=\begin{pmatrix}
    1 & 0\\
    2 & 0
\end{pmatrix}\simeq\begin{pmatrix}
    1\\
    0\\
    2\\
    0
\end{pmatrix}, \quad \varphi(e_2)=\begin{pmatrix}
    0 & 1\\
    0 & 2
\end{pmatrix}\simeq\begin{pmatrix}
    0\\
    1\\
    0\\
    2\\
\end{pmatrix}$$

$$\varphi(e_3)=\begin{pmatrix}
    2 & 0\\
    4 & 0
\end{pmatrix}\simeq\begin{pmatrix}
    2\\
    0\\
    4\\
    0
\end{pmatrix}, \quad \varphi(e_4)=\begin{pmatrix}
    0 & 2\\
    0 & 4
\end{pmatrix}\simeq\begin{pmatrix}
    0\\
    2\\
    0\\
    4\\
\end{pmatrix}$$


$$A(\varphi,\mathbf{e},\mathbf{f})=\begin{pmatrix}
    1 & 0 & 2 & 0\\
    0 & 1 & 0 & 2\\
    2 & 0 & 4 & 0\\
    0 & 2 & 0 & 4
\end{pmatrix}\sim\begin{pmatrix}
    1 & 0 & 2 & 0\\
    0 & 1 & 0 & 2\\
    0 & 0 & 0 & 0\\
    0 & 0 & 0 & 0
\end{pmatrix}$$

First two coordinates are fixed, so take those as vectors of the basis, and we'll be set:

$$\text{Im}\,\varphi=\left\langle\begin{pmatrix}
    1 & 0\\
    2 & 0\\
\end{pmatrix},\begin{pmatrix}
    0 & 1\\
    0 & 2
\end{pmatrix}\right\rangle$$

## Problem 3

Linear mapping $\varphi\colon\mathbb{R}^4\mapsto\mathbb{R}^3$ in a pair of standard bases has a matrix $\begin{pmatrix}
    1 & 1 & 2 & 2\\
    2 & 2 & 4 & 4\\
    3 & 3 & 6 & 6
\end{pmatrix}$. Find a pair of bases in which mapping $\varphi$ has a diagonal matrix with ones and zero akin to the seminar and write this matrix down.

---

Firstly, we need to find what vectors get sent to $0$, for this, find the basis of $\ker \varphi$:

$$\begin{pmatrix}
    1 & 1 & 2 & 2\\
    2 & 2 & 4 & 4\\
    3 & 3 & 6 & 6
\end{pmatrix}\sim\begin{pmatrix}
    1 & 1 & 2 & 2\\
    0 & 0 & 0 & 0\\
    0 & 0 & 0 & 0
\end{pmatrix}$$

Implies the fundamental system of solutions is 

$$\Phi=\begin{pmatrix}
    -1 & -2 & -2\\
    1 & 0 & 0\\
    0 & 1 & 0\\
    0 & 0 & 1
\end{pmatrix}$$

Now create a whole new basis by appending unit vectors to the beginning:

$$\mathbf{e}'=\langle(1,0,0,0),(-1,1,0,0),(-2,0,1,0),(-2,0,0,1)\rangle$$

Applying the matrix to the first unit vector, we get $f_1'=(1,2,3)$ (just take the first column) and we may present the second basis, preemptively filling it with unit vectors via appension (I know it's an archaic form, it's just funny):

$$\mathbf{f}'=\langle(1,2,3),(0,1,0),(0,0,1)\rangle$$

$$A'(\varphi,\mathbf{e}',\mathbf{f}')=\begin{pmatrix}
    1 & 0 & 0 & 0\\
    0 & 0 & 0 & 0\\
    0 & 0 & 0 & 0
\end{pmatrix}$$

## Problem 4

Linear mapping $\varphi\colon\mathbb{R}^4\mapsto\mathbb{R}^3$ in a pair of standard bases has a matrix $\begin{pmatrix}
    1 & 1 & 0 & 2\\
    3 & -3 & 2 & 0\\
    2 & -1 & 1 & 1
\end{pmatrix}$. Find a pair of bases in which mapping $\varphi$ has a diagonal matrix with ones and zero akin to the seminar and write this matrix down.

---

Doing the same thing all over again:

Firstly, we need to find what vectors get sent to $0$, for this, find the basis of $\ker \varphi$:

$$\begin{pmatrix}
    1 & 1 & 0 & 2\\
    3 & -3 & 2 & 0\\
    2 & -1 & 1 & 1
\end{pmatrix}\sim\begin{pmatrix}
    1 & 0 & \frac{1}{3} & 1\\
    0 & 1 & -\frac{1}{3} & 1\\
    0 & 0 & 0 & 0
\end{pmatrix}$$

Implies the fundamental system of solutions is 

$$\Phi=\begin{pmatrix}
    -1 & -1\\
    1 & -1\\
    3 & 0\\
    0 & 1
\end{pmatrix}$$

Now create a whole new basis by appending unit vectors to the beginning:

$$\mathbf{e}'=\langle(1,0,0,0),(0,1,0,0),(-1,1,3,0),(-1,-1,0,1)\rangle$$

Applying the matrix to the first two unit vectors, we get $f_1'=(1,3,2),f_2'=(1,-3,-1)$ (just take the first two columns) and we may present the second basis, preemptively filling it with unit vectors as above:

$$\mathbf{f}'=\langle(1,3,2),(1,-3,-1),(0,0,1)\rangle$$

$$A'(\varphi,\mathbf{e}',\mathbf{f}')=\begin{pmatrix}
    1 & 0 & 0 & 0\\
    0 & 1 & 0 & 0\\
    0 & 0 & 0 & 0
\end{pmatrix}$$

## Problem 5

Let non-zero linear functions $\alpha,\beta\in V^*$ be such that $\ker\alpha=\ker\beta$. Prove that then $\alpha$ and $\beta$ are proportional, i. e. $\beta=\lambda\alpha$ for some non-zero scalar $\lambda\in F$.

---

The linear form $\begin{pmatrix}
    a_1 & a_2 & \dots & a_n
\end{pmatrix}$ effectively sends some vectors $x$ to a value as follows:

$$\begin{pmatrix}
    a_1 & a_2 & \dots & a_n
\end{pmatrix}\begin{pmatrix}
    x_1\\
    x_2\\
    \vdots\\
    x_n
\end{pmatrix}=a_1x_1+a_2x_2+\dots+a_nx_n$$

Kernels tell us what vectors get sent to zero, thus the sets for each of the functions $\alpha,\beta$ should be same per the given condition that $\ker\alpha=\ker\beta$:

$$a_1x_1+a_2x_2+\dots+a_nx_n=0$$

$$b_1x_1+b_2x_2+\dots+b_nx_n=0$$

Since we know that the solutions are the same, then there exists a certain transformation that maintains the same set of solutions, which is multiplication by a scalar value. Therefore, $b_i$ can be expressed as $\lambda a_i$, and

$$a_1x_1+a_2x_2+\dots+a_nx_n=0$$

$$\lambda a_1x_1+\lambda a_2x_2+\dots+\lambda a_nx_n=0$$

obviously have the same set of solutions, which means that these functions have the same kernel and coefficients proportional to each other, q. e. d.

## Problem 6

Let $V=\mathbb{R}[x]_n$ and mapping $\alpha^a, (a\in\mathbb{R})$ of a space $V$ in $\mathbb{R}$ is defined by $\alpha^a(f)=f(a)$.

Prove that the system $\alpha^0,\alpha^1,\dots,\alpha^n$ is a basis of a dual space $V^*$.

---

this the very same case scenario as in the last homework, where this is some kinda bullshit that I cannot physically comprehend because the the task is too unclear and SERIOUSLY why are we being given a task that asks us to use lagrangian polynomials WHICH IS SOMETHING WE HAVE NEVER COVERED in the FIRST EVER TASK IN THE HOMEWORK WHICH IS SUPPOSED TO BE ABOUT DUAL BASES, FOR F[---]'S SAKE 

## Problem 7

Prove that any $k$-dimensional subspace of an $n$-dimensional space is an intersection of kernels of some $n-k$ linear functions.

---

We know that the linear function $F$ maps values from $\mathbb{R}^k$, then instead of treating it as a function applied to a vector, we can treat it as a set of functions that send each coordinate of a vector to zero.

Take function applied to a vector and split it into multiple:

$$F(\textbf{x})=\begin{pmatrix}
    f_1(x_1)\\
    f_2(x_2)\\
    \vdots\\
    f_n(x_n)
\end{pmatrix}$$

Now, we need to take all values that $f_1$ sends to $0$, all values that $f_2$ sends to $0$, all values that ... $f_n$ sends to $0$ and take their intersection to get the entire function $F$ that sends the whole vector to $0$.

Assume that there is some subspace of dimension $k$. It means that $k$ functions $f_i$ from $F$ out of the total number of $n$ would be non-zero, which, in turn, means that $n-k$ functions have be zero. For this, we have to intersect $n-k$ kernels of a single variable as we have defined before  