## Problem 1

Let $A$ be some matrix and $\lambda, \mu \in \R$. Prove that $(\lambda + \mu)A = \lambda A + \mu A$ and $\lambda(\mu A) = (\lambda\mu)A$.

### Solution

Suppose:

$$A = \begin{pmatrix}
a_{11} & a_{12} & ... & a_{1n}\\
a_{21} & a_{22} & ... & a_{2n}\\
... & ... & ... & ...\\
a_{m1} & a_{m2} & ... & a_{mn}
\end{pmatrix}$$

Evaluate $(\lambda + \mu)A$:

$$(\lambda + \mu)\begin{pmatrix}
a_{11} & a_{12} & ... & a_{1n}\\
a_{21} & a_{22} & ... & a_{2n}\\
... & ... & ... & ...\\
a_{m1} & a_{m2} & ... & a_{mn}
\end{pmatrix}=\begin{pmatrix}
(\lambda + \mu)a_{11} & (\lambda + \mu)a_{12} & ... & (\lambda + \mu)a_{1n}\\
(\lambda + \mu)a_{21} & (\lambda + \mu)a_{22} & ... & (\lambda + \mu)a_{2n}\\
... & ... & ... & ...\\
(\lambda + \mu)a_{m1} & (\lambda + \mu)a_{m2} & ... & (\lambda + \mu)a_{mn}
\end{pmatrix}=X$$

Evaluate $\lambda A + \mu A$:

$$\lambda\begin{pmatrix}
a_{11} & a_{12} & ... & a_{1n}\\
a_{21} & a_{22} & ... & a_{2n}\\
... & ... & ... & ...\\
a_{m1} & a_{m2} & ... & a_{mn}
\end{pmatrix}+\mu\begin{pmatrix}
a_{11} & a_{12} & ... & a_{1n}\\
a_{21} & a_{22} & ... & a_{2n}\\
... & ... & ... & ...\\
a_{m1} & a_{m2} & ... & a_{mn}
\end{pmatrix}=$$

$$=\begin{pmatrix}
\lambda a_{11} & \lambda a_{12} & ... & \lambda a_{1n}\\
\lambda a_{21} & \lambda a_{22} & ... & \lambda a_{2n}\\
... & ... & ... & ...\\
\lambda a_{m1} & \lambda a_{m2} & ... & \lambda a_{mn}
\end{pmatrix}+\begin{pmatrix}
\mu a_{11} & \mu a_{12} & ... & \mu a_{1n}\\
\mu a_{21} & \mu a_{22} & ... & \mu a_{2n}\\
... & ... & ... & ...\\
\mu a_{m1} & \mu a_{m2} & ... & \mu a_{mn}
\end{pmatrix}=$$

$$=\begin{pmatrix}
\lambda a_{11} + \mu a_{11} & \lambda a_{12} + \mu a_{12} & ... & \lambda a_{1n} + \mu a_{1n}\\
\lambda a_{21} + \mu a_{21} & \lambda a_{22} + \mu a_{22} & ... & \lambda a_{2n} + \mu a_{2n}\\
... & ... & ... & ...\\
\lambda a_{m1} + \mu a_{m1} & \lambda a_{m2} + \mu a_{m2} & ... & \lambda a_{mn} + \mu a_{mn}
\end{pmatrix}=$$

$$=\begin{pmatrix}
(\lambda + \mu) a_{11} & (\lambda + \mu) a_{12} & ... & (\lambda + \mu) a_{1n}\\
(\lambda + \mu) a_{21} & (\lambda + \mu) a_{22} & ... & (\lambda + \mu) a_{2n}\\
... & ... & ... & ...\\
(\lambda + \mu) a_{m1} & (\lambda + \mu) a_{m2} & ... & (\lambda + \mu) a_{mn}
\end{pmatrix}=X$$

Both parts of the first equation evaluate to the same matrix; therefore, the first equation is true, q. e. d.

---

Evaluate $\lambda(\mu A)$:  

$$\lambda(\mu A) = \lambda\begin{pmatrix}
\mu a_{11} & \mu a_{12} & ... & \mu a_{1n}\\
\mu a_{21} & \mu a_{22} & ... & \mu a_{2n}\\
... & ... & ... & ...\\
\mu a_{m1} & \mu a_{m2} & ... & \mu a_{mn}
\end{pmatrix}=\begin{pmatrix}
\lambda\mu a_{11} & \lambda\mu a_{12} & ... & \lambda\mu a_{1n}\\
\lambda\mu a_{21} & \lambda\mu a_{22} & ... & \lambda\mu a_{2n}\\
... & ... & ... & ...\\
\lambda\mu a_{m1} & \lambda\mu a_{m2} & ... & \lambda\mu a_{mn}
\end{pmatrix} = Y$$

Evaluate $(\lambda\mu)A$:

$$(\lambda\mu)A=\begin{pmatrix}
\lambda\mu a_{11} & \lambda\mu a_{12} & ... & \lambda\mu a_{1n}\\
\lambda\mu a_{21} & \lambda\mu a_{22} & ... & \lambda\mu a_{2n}\\
... & ... & ... & ...\\
\lambda\mu a_{m1} & \lambda\mu a_{m2} & ... & \lambda\mu a_{mn}
\end{pmatrix} = Y$$

Both parts of the second equation evaluate to the same matrix as well; therefore, the second equation is also true, q. e. d.

## Problem 2

### Subproblem A

$$\begin{pmatrix}
1 & 5 & 3 \\
2 & -3 & 1
\end{pmatrix}\cdot\begin{pmatrix}
2 & -3 & 5 \\
-1 & 4 & -2 \\
3 & -1 & 1
\end{pmatrix}=$$

$$=\begin{pmatrix}
1\cdot 2+5\cdot-1+3\cdot 3 & 1\cdot-3+5\cdot4+3\cdot-1 & 1\cdot 5+5\cdot-2+3\cdot 1. \\
2\cdot 2 + -3\cdot-1+1\cdot 3 & 2\cdot-3+-3\cdot 4+1\cdot-1 & 2\cdot 5+-3\cdot-2+1\cdot 1
\end{pmatrix}=$$

$$=\begin{pmatrix}
6 & 14 & -2 \\
10 & -19 & 17
\end{pmatrix}$$

### Subproblem B

$$\begin{pmatrix}
3 & 0 & 2 \\
0 & 1 & 3 \\
2 & 2 & 0 \\
0 & 1 & 0
\end{pmatrix}\cdot\begin{pmatrix}
1 & 2 & -1 & 2 \\
-2 & -1 & 1 & 2 \\
2 & 1 & 1 & 2
\end{pmatrix}+\begin{pmatrix}
0 & -4 & 6 & 1 \\
2 & 2 & -5 & -2 \\
2 & -2 & 6 & 4 \\
1 & 3 & 0 & 1
\end{pmatrix}=$$
$$=\begin{pmatrix}
3\cdot1 + 0\cdot-2 + 2\cdot2 & 3\cdot2 + 0\cdot-1 + 2\cdot1 & 3\cdot-1 + 0\cdot1 + 2\cdot1 & 3\cdot2 + 0\cdot2 + 2\cdot2 \\
0\cdot1 + 1\cdot-2 + 3\cdot2 & 0\cdot2 + 1\cdot-1 + 3\cdot1 & 0\cdot-1 + 1\cdot1 + 3\cdot1 & 0\cdot2 + 1\cdot2 + 3\cdot2 \\
2\cdot1 + 2\cdot-2 + 0\cdot2 & 2\cdot2 + 2\cdot-1 + 0\cdot1 & 2\cdot-1 + 2\cdot1 + 0\cdot1 & 2\cdot2 + 2\cdot2 + 0\cdot2 \\
0\cdot1 + 1\cdot-2 + 0\cdot2 & 0\cdot2 + 1\cdot-1 + 0\cdot1 & 0\cdot-1 + 1\cdot1 + 0\cdot1 & 0\cdot2 + 1\cdot2 + 0\cdot2 
\end{pmatrix}=$$

$$=\begin{pmatrix}
7 & 8 & -1 & 10 \\
4 & 2 & 4 & 8 \\
-2 & 2 & 0 & 8 \\
-2 & -1 & 1 & 2
\end{pmatrix}+\begin{pmatrix}
0 & -4 & 6 & 1 \\
2 & 2 & -5 & -2 \\
2 & -2 & 6 & 4 \\
1 & 3 & 0 & 1
\end{pmatrix}=\begin{pmatrix}
7 & 4 & 5 & 11 \\
6 & 4 & -1 & 6 \\
0 & 0 & 6 & 12 \\
-1 & 2 & 1 & 3
\end{pmatrix}$$

## Problem 3

Find all $(2 \times 2)$ matrices $B$ that commute with matrix $A = \begin{pmatrix}
2 & -1 \\
1 & 0
\end{pmatrix}$, i. e. for which $AB=BA$.

### Solution

Let $B=\begin{pmatrix}
b_{11} & b_{12} \\
b_{21} & b_{22}
\end{pmatrix}$. 

Evaluate $AB$ and $BA$:

$$AB=\begin{pmatrix}
2b_{11} - b_{21} & 2b_{12} -b_{22} \\
b_{11} & b_{12}
\end{pmatrix}
$$

$$BA=\begin{pmatrix}
2b_{11} + b_{12} & -b_{11} \\
2b_{21} + b_{22} & -b_{21}
\end{pmatrix}
$$

Therefore, for $AB=BA$, the following system of equations has to be true:
$$
\begin{cases}
2b_{11} - b_{21} = 2b_{11} + b_{12} \\
2b_{12} -b_{22} = -b_{11} \\
b_{11} = 2b_{21} + b_{22} \\
b_{12} = -b_{21}
\end{cases}\Rightarrow
\begin{cases}
-b_{21} = b_{12} \\
b_{11} = b_{22} - 2b_{12} \\
b_{11} = 2b_{21} + b_{22} \\
b_{12} = -b_{21}
\end{cases}\Rightarrow
\begin{cases}
b_{12} = -b_{21} \\
b_{11} = b_{22} + 2b_{21}
\end{cases}$$

Thus, considering $b_{21} = x$, $b_{22} = y$, matrix $B=\begin{pmatrix}
y+2x & -x \\
x & y
\end{pmatrix}$

## Problem 4

Evaluate the following expression:

$$\begin{pmatrix}
\cos\alpha & -\sin\alpha \\
\sin\alpha & \cos\alpha
\end{pmatrix}^n$$

### Solution

Evaluate matrices for $n=1, 2$ to try and figure out the pattern:

$$\begin{pmatrix}
\cos\alpha & -\sin\alpha \\
\sin\alpha & \cos\alpha
\end{pmatrix}^1 = \begin{pmatrix}
\cos\alpha & -\sin\alpha \\
\sin\alpha & \cos\alpha
\end{pmatrix}$$

$$\begin{pmatrix}
\cos\alpha & -\sin\alpha \\
\sin\alpha & \cos\alpha
\end{pmatrix}^2 = \begin{pmatrix}
\cos^2\alpha - \sin^2a & -2\sin\alpha\cos\alpha \\
2\sin\alpha\cos\alpha & \cos^2\alpha-\sin^2\alpha
\end{pmatrix} = \begin{pmatrix}
\cos2\alpha & -\sin2\alpha \\
\sin2\alpha & \cos2\alpha
\end{pmatrix}$$

It appears that $\begin{pmatrix}
\cos\alpha & -\sin\alpha \\
\sin\alpha & \cos\alpha
\end{pmatrix}^n = \begin{pmatrix}
\cos n\alpha & -\sin n\alpha \\
\sin n\alpha & \cos n\alpha
\end{pmatrix}$. This shall be the induction hypothesis. Its base for $n=1$ has been already proven in the beginning of the solution, so only the induction step has to be checked.

Prove that $\begin{pmatrix}
\cos n\alpha & -\sin n\alpha \\
\sin n\alpha & \cos n\alpha
\end{pmatrix}\begin{pmatrix}
\cos \alpha & -\sin \alpha \\
\sin \alpha & \cos \alpha
\end{pmatrix}=\begin{pmatrix}
\cos ((n + 1)\alpha) & -\sin ((n + 1)\alpha) \\
\sin ((n + 1)\alpha) & \cos ((n + 1)\alpha)
\end{pmatrix}$.

$$\begin{pmatrix}
\cos n\alpha & -\sin n\alpha \\
\sin n\alpha & \cos n\alpha
\end{pmatrix}\begin{pmatrix}
\cos \alpha & -\sin \alpha \\
\sin \alpha & \cos \alpha
\end{pmatrix}=\begin{pmatrix}
\cos n\alpha\cos\alpha - \sin n\alpha\sin\alpha & -\sin n\alpha\cos\alpha - \sin\alpha\cos n\alpha \\
\sin n\alpha\cos\alpha + \sin\alpha\cos n\alpha & \cos n\alpha\cos\alpha - \sin n\alpha\sin\alpha
\end{pmatrix}=$$

$$=\begin{pmatrix}
\cos ((n+1)\alpha) & -\sin ((n+1)\alpha) \\
\sin ((n+1)\alpha) & \cos ((n+1)\alpha)
\end{pmatrix}$$

Therefore, $\begin{pmatrix}
\cos\alpha & -\sin\alpha \\
\sin\alpha & \cos\alpha
\end{pmatrix}^n = \begin{pmatrix}
\cos n\alpha & -\sin n\alpha \\
\sin n\alpha & \cos n\alpha
\end{pmatrix}$, q. e. d.

## Problem 5

Evaluate the following expression:

$$\begin{pmatrix}
\lambda_1 & & & 0 \\
 & \lambda_2 & & \\
 & & \ddots & \\
0 & & & \lambda_n
\end{pmatrix}^k$$

### Solution

Evaluate matrices for $n=1, 2$ to try and figure out the pattern:

$$\begin{pmatrix}
\lambda_1 & & & 0 \\
 & \lambda_2 & & \\
 & & \ddots & \\
0 & & & \lambda_n
\end{pmatrix}^1=\begin{pmatrix}
\lambda_1^1 & & & 0 \\
 & \lambda_2^1 & & \\
 & & \ddots & \\
0 & & & \lambda_n^1
\end{pmatrix}$$

$$\begin{pmatrix}
\lambda_1 & & & 0 \\
 & \lambda_2 & & \\
 & & \ddots & \\
0 & & & \lambda_n
\end{pmatrix}^2=\begin{pmatrix}
\lambda_1 \cdot \lambda_1 + 0 + ... + 0 & \lambda_1 \cdot 0 + 0 \cdot \lambda_2 + 0 + ... + 0 & \dots & \lambda_1 \cdot 0 + ... + 0 + 0 \cdot \lambda_n \\
0 \cdot \lambda_1 + \lambda_2 \cdot 0 + ... + 0 & 0 + \lambda_2 \cdot \lambda_2 + 0 + ... + 0 & \dots & 0 + \lambda_2 \cdot 0 + ... + 0 \cdot \lambda_n \\
\vdots & \vdots & \ddots & \vdots \\
0 \cdot \lambda_1 + 0 + ... + \lambda_n \cdot 0 & 0 + 0 \cdot \lambda_2 + ... + \lambda_n \cdot 0& \dots & 0 + ... + 0 + \lambda_n \cdot \lambda_n
\end{pmatrix}=\begin{pmatrix}
\lambda_1^2 & & & 0 \\
 & \lambda_2^2 & & \\
 & & \ddots & \\
0 & & & \lambda_n^2
\end{pmatrix}$$

Similarly as in Problem 4, prove the hypothesis that $\begin{pmatrix}
\lambda_1 & & & 0 \\
 & \lambda_2 & & \\
 & & \ddots & \\
0 & & & \lambda_n
\end{pmatrix}^k=\begin{pmatrix}
\lambda_1^k & & & 0 \\
 & \lambda_2^k & & \\
 & & \ddots & \\
0 & & & \lambda_n^k
\end{pmatrix}$ via induction. The induction base is true as previously described. We need to check whether the induction step is true:

$$\begin{pmatrix}
\lambda_1^k & & & 0 \\
 & \lambda_2^k & & \\
 & & \ddots & \\
0 & & & \lambda_n^k
\end{pmatrix}\begin{pmatrix}
\lambda_1 & & & 0 \\
 & \lambda_2 & & \\
 & & \ddots & \\
0 & & & \lambda_n
\end{pmatrix} =$$

$$=\begin{pmatrix}
\lambda_1^k \cdot \lambda_1 + 0 + ... + 0 & \lambda_1^k \cdot 0 + 0 \cdot \lambda_2 + 0 + ... + 0 & \dots & \lambda_1^k \cdot 0 + ... + 0 + 0 \cdot \lambda_n \\
0 \cdot \lambda_1 + \lambda_2 \cdot 0 + ... + 0 & 0 + \lambda_2^k \cdot \lambda_2 + 0 + ... + 0 & \dots & 0 + \lambda_2^k \cdot 0 + ... + 0 \cdot \lambda_n \\
\vdots & \vdots & \ddots & \vdots \\
0 \cdot \lambda_1 + 0 + ... + \lambda_n^k \cdot 0 & 0 + 0 \cdot \lambda_2 + ... + \lambda_n^k \cdot 0& \dots & 0 + ... + 0 + \lambda_n^k \cdot \lambda_n
\end{pmatrix}=\begin{pmatrix}
\lambda_1^{k+1} & & & 0 \\
 & \lambda_2^{k+1} & & \\
 & & \ddots & \\
0 & & & \lambda_n^{k+1}
\end{pmatrix}$$

Therefore, $\begin{pmatrix}
\lambda_1 & & & 0 \\
 & \lambda_2 & & \\
 & & \ddots & \\
0 & & & \lambda_n
\end{pmatrix}^k=\begin{pmatrix}
\lambda_1^k & & & 0 \\
 & \lambda_2^k & & \\
 & & \ddots & \\
0 & & & \lambda_n^k
\end{pmatrix}$, q. e. d.

## Problem 6

Evaluate the following expression: 

$$\begin{pmatrix}
\lambda & 1 \\
0 & \lambda
\end{pmatrix}^n$$

### Solution 

Similarly as in Problems 5, 6, evaluate the expression for $n=1,2$:

$$\begin{pmatrix}
\lambda & 1 \\
0 & \lambda
\end{pmatrix}^1=\begin{pmatrix}
\lambda^1 & 1\cdot\lambda^{1-1} \\
0 & \lambda^1
\end{pmatrix}^1$$

$$\begin{pmatrix}
\lambda & 1 \\
0 & \lambda
\end{pmatrix}^2=\begin{pmatrix}
\lambda \cdot \lambda + 1 \cdot 0 & \lambda \cdot 1 + 1 \cdot \lambda \\
0 \cdot \lambda + \lambda \cdot 0 & 0 \cdot 1 + \lambda \cdot \lambda
\end{pmatrix}=\begin{pmatrix}
\lambda^2 & 2\lambda^{n-1} \\
0 & \lambda^2
\end{pmatrix}$$

Induction base is already proven, now we need to prove that $\begin{pmatrix}
\lambda^n & n\lambda^{n-1} \\
0 & \lambda^n
\end{pmatrix}^n\begin{pmatrix}
\lambda & 1 \\
0 & \lambda
\end{pmatrix}=\begin{pmatrix}
\lambda^{n+1} & (n+1)\lambda^n \\
0 & \lambda^{n+1}
\end{pmatrix}$:

$$\begin{pmatrix}
\lambda^n & n\lambda^{n-1} \\
0 & \lambda^n
\end{pmatrix}^n\begin{pmatrix}
\lambda & 1 \\
0 & \lambda
\end{pmatrix}=\begin{pmatrix}
\lambda^n \cdot \lambda + n\lambda^{n-1} \cdot 0& n\lambda^{n-1} \cdot \lambda + 1\cdot\lambda \\
0 \cdot \lambda^n + \lambda^n \cdot 0 & 0 \cdot n\lambda^{n-1} + \lambda^n \cdot \lambda
\end{pmatrix}=$$

$$=\begin{pmatrix}
\lambda^n \cdot \lambda + n\lambda^{n-1} \cdot 0& n\lambda^{n-1} \cdot \lambda + 1\cdot\lambda \\
0 \cdot \lambda^n + \lambda^n \cdot 0 & 0 \cdot n\lambda^{n-1} + \lambda^n \cdot \lambda
\end{pmatrix}=\begin{pmatrix}
\lambda^{n+1} & (n+1)\lambda^n \\
0 & \lambda^{n+1}
\end{pmatrix}$$

Therefore, $\begin{pmatrix}
\lambda & 1 \\
0 & \lambda
\end{pmatrix}^n = \begin{pmatrix}
\lambda^{n+1} & (n+1)\lambda^n \\
0 & \lambda^{n+1}
\end{pmatrix}$, q. e. d.

## Problem 7

Calculate $H^n$ of the following matrix: 

$$H=\begin{pmatrix}
0 & 1 & 0 & \dots & 0 \\
0 & 0 & 1 & \dots & 0 \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
0 & 0 & 0 & \dots & 1 \\
0 & 0 & 0 & \dots & 0
\end{pmatrix}$$

### Solution

Attempt to square the matrix to see what happens:

$$H^2=\begin{pmatrix}
0 & 1 & 0 & \dots & 0 \\
0 & 0 & 1 & \dots & 0 \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
0 & 0 & 0 & \dots & 1 \\
0 & 0 & 0 & \dots & 0
\end{pmatrix}^2=\begin{pmatrix}
0 & 0 & 1 & 0 & \dots & 0 \\
0 & 0 & 0 & 1 & \dots & 0 \\
\vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\
0 & 0 & 0 & 0 & \dots & 1 \\
0 & 0 & 0 & 0 & \dots & 0 \\
0 & 0 & 0 & 0 & \dots & 0
\end{pmatrix}$$

As seen from the result matrix, the non-zero elements "shift" diagonally by one index on multiplication. We may write an equation that we think would determine the second matrix (consider $h_{ij}$ an element of the result matrix) and then prove it via induction:

$$h_{ij}=\begin{cases}
1, \text{if} \ j-i=n \\
0, \text{otherwise}
\end{cases}$$

The induction base is already proven ($H^1=H$). Therefore, we need to check whether the induction step is true.

For some $n < k$, where $k$ is the matrix's dimension, we multiply $H^n$ by $H$ (positions are represented accurately in each of the multiplication steps):

$$H^n=\begin{pmatrix}
0 & \dots & 1 & 0 & 0 & \dots & 0 \\
0 & \dots & 0 & 1 & 0 & \dots & 0 \\
0 & \dots & 0 & 0 & 1 & \dots & 0 \\
\vdots & \vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\
0 & \dots & 0 & 0 & 0 & \dots & 1 \\
\vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\
0 & \dots & 0 & 0 & 0 & \dots & 0
\end{pmatrix}\begin{pmatrix}
0 & 1 & 0 & \dots & 0 \\
0 & 0 & 1 & \dots & 0 \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
0 & 0 & 0 & \dots & 1 \\
0 & 0 & 0 & \dots & 0
\end{pmatrix}=\begin{pmatrix}
0 & \dots & 0 & 1 & 0 & \dots & 0 \\
0 & \dots & 0 & 0 & 1 & \dots & 0 \\

\vdots & \vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\
0 & \dots & 0 & 0 & 0 & \dots & 1 \\
0 & \dots & 0 & 0 & 0 & \dots & 0 \\
\vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\
0 & \dots & 0 & 0 & 0 & \dots & 0
\end{pmatrix}=H^{n-1}$$

Therefore, the induction step is true, q. e. d.

**NB:** The equation that determines the result matrix is identical to a zero matrix if $n \geq k$.

**Answer:** $H^n = \begin{pmatrix}h_{ij}\end{pmatrix}$, where: $h_{ij}=\begin{cases}
1, \text{if} \ j-i=n \\
0, \text{otherwise}
\end{cases}$