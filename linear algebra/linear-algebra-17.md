# Linear Algebra, Homework 17

## Problem 1

Let $L=K[x]_1$, $K$ is a field. Find the matrix of the linear mapping $\mathcal{A}\colon f(x)\mapsto f(S)$ of a space $L$ to a space $M=\mathbf{M}_2(K)$, where $S=\begin{pmatrix}
    a & b\\
    c & d
\end{pmatrix}$ is a fixed matrix if the basis in $L$ is $(1,x)$ and the basis in $M$ consist of matrix ones.

---

Let's apply $\mathcal{A}$ to the basis vectors ($1$ maps to the unit matrix since $1$ is constant, $f(x)$ maps to matrix $S$):

$$1\mapsto\begin{pmatrix}
    1 & 0\\
    0 & 1
\end{pmatrix},\quad f(x)\mapsto S=\begin{pmatrix}
    a & b\\
    c & d
\end{pmatrix}$$

Since the basis of the resulting space is the standard one, we may simply write the transformation matrix:

$$\begin{pmatrix}
    1 & a\\
    0 & b\\
    0 & c\\
    1 & d
\end{pmatrix}$$

## Problem 2

Consider a mapping $\varphi\colon M_2(F)\mapsto M_2(F), X\mapsto X^T$. Prove that this mapping is linear, and find its matrix in bases $\mathbf{e}$ and $\mathbf{f}$, where $\mathbf{e}=\mathbf{f}$ is a basis of matrix ones.

---

To prove that a mapping is linear, check the following for some $A,B\in M_2(F)$:

$$\varphi(A+B)=\varphi(A)+\varphi(B)$$

$$\varphi\left(\begin{pmatrix}
    a_1 & a_2\\
    a_3 & a_4
\end{pmatrix}+\begin{pmatrix}
    b_1 & b_2\\
    b_3 & b_4
\end{pmatrix}\right)=\varphi\left(\begin{pmatrix}
    a_1 & a_2\\
    a_3 & a_4
\end{pmatrix}\right)+\varphi\left(\begin{pmatrix}
    b_1 & b_2\\
    b_3 & b_4
\end{pmatrix}\right)$$

$$\begin{pmatrix}
    a_1+b_1 & a_2+b_2\\
    a_3+b_3 & a_4+b_4
\end{pmatrix}^T=\begin{pmatrix}
    a_1 & a_2\\
    a_3 & a_4
\end{pmatrix}^T+\begin{pmatrix}
    b_1 & b_2\\
    b_3 & b_4
\end{pmatrix}^T$$

$$\begin{pmatrix}
    a_1+b_1 & a_3+b_3\\
    a_2+b_2 & a_4+b_4
\end{pmatrix}=\begin{pmatrix}
    a_1 & a_3\\
    a_2 & a_4
\end{pmatrix}+\begin{pmatrix}
    b_1 & b_3\\
    b_2 & b_4
\end{pmatrix}$$

$$\begin{pmatrix}
    a_1+b_1 & a_3+b_3\\
    a_2+b_2 & a_4+b_4
\end{pmatrix}=\begin{pmatrix}
    a_1+b_1 & a_3+b_3\\
    a_2+b_2 & a_4+b_4
\end{pmatrix}$$

This property holds, check the other one for same $A$ and $\lambda\in\mathbb{F}$:

$$\varphi(\lambda A)=\lambda\varphi(A)$$

$$\varphi\left(\lambda \begin{pmatrix}
    a_1 & a_2\\
    a_3 & a_4
\end{pmatrix}\right)=\lambda\varphi\left(\begin{pmatrix}
    a_1 & a_2\\
    a_3 & a_4
\end{pmatrix}\right)$$

$$\begin{pmatrix}
    \lambda a_1 & \lambda a_2\\
    \lambda a_3 & \lambda a_4
\end{pmatrix}^T=\lambda\begin{pmatrix}
    a_1 & a_2\\
    a_3 & a_4
\end{pmatrix}^T$$

$$\begin{pmatrix}
    \lambda a_1 & \lambda a_3\\
    \lambda a_2 & \lambda a_4
\end{pmatrix}=\lambda\begin{pmatrix}
    a_1 & a_3\\
    a_2 & a_4
\end{pmatrix}$$

$$\begin{pmatrix}
    \lambda a_1 & \lambda a_3\\
    \lambda a_2 & \lambda a_4
\end{pmatrix}=\begin{pmatrix}
    \lambda a_1 & \lambda a_3\\
    \lambda a_2 & \lambda a_4
\end{pmatrix}$$

This property also holds $\implies$ the mapping is truly linear.

Consider bases $\mathbf{e}=\mathbf{f}=\left\{\begin{pmatrix}
    1 & 0\\
    0 & 0
\end{pmatrix},\begin{pmatrix}
    0 & 1\\
    0 & 0
\end{pmatrix},\begin{pmatrix}
    0 & 0\\
    1 & 0
\end{pmatrix},\begin{pmatrix}
    0 & 0\\
    0 & 1
\end{pmatrix}\right\}$, write them as vectors:

$$\mathbf{e}=\mathbf{f}=\left\{\begin{pmatrix}
    1\\
    0\\
    0\\
    0\\
\end{pmatrix},\begin{pmatrix}
    0\\
    1\\
    0\\
    0\\
\end{pmatrix},\begin{pmatrix}
    0\\
    0\\
    1\\
    0\\
\end{pmatrix},\begin{pmatrix}
    0\\
    0\\
    0\\
    1\\
\end{pmatrix}\right\}$$

Applying $\varphi$ to each of the basis vectors (writing them as vectors), we get the following in basis $\mathbf{f}=E_4$, where $E_4$ is a unit matrix:

$$\varphi(e_1)=E_4\begin{pmatrix}
    1\\
    0\\
    0\\
    0\\
\end{pmatrix},\quad\varphi(e_2)=E\begin{pmatrix}
    0\\
    0\\
    1\\
    0\\
\end{pmatrix},\quad\varphi(e_3)=E\begin{pmatrix}
    0\\
    1\\
    0\\
    0\\
\end{pmatrix},\quad\varphi(e_4)=E\begin{pmatrix}
    0\\
    0\\
    0\\
    1\\
\end{pmatrix}$$

Therfore, write them into a matrix as vectors (vertically) to get the transformation matrix:

$$A(\varphi, \mathbf{e}, \mathbf{f})=\begin{pmatrix}
    1 & 0 & 0 & 0\\
    0 & 0 & 1 & 0\\
    0 & 1 & 0 & 0\\
    0 & 0 & 0 & 1
\end{pmatrix}$$

## Problem 3

Consider a mapping $\varphi\colon\mathbb{R}[x]_{\leqslant3}\mapsto\mathbb{R}^2$ that maps $f\mapsto (f(-1), f'(1))$. Prove that this mapping is linear and find its matrix in bases $\mathbf{e}$ and $\mathbf{f}$, where $\mathbf{e} = (1,x,x^2,x^3)$ and $\mathbf{f}$ is the standard basis in $\mathbb{R}^2$.

---

Prove that the matrix is linear, similarly to above for some 

$$\varphi(P_1+P_2)=\varphi(P_1)+\varphi(P_2)$$

$$\varphi(a_0+a_1x+a_2x^2+a_3x^3+b_0+b_1x+b_2x^2+b_3x^3)=\\=\varphi(a_0+a_1x+a_2x^2+a_3x^3)+\varphi(b_0+b_1x+b_2x^2+b_3x^3)$$

$$(a_0-a_1+a_2-a_3+b_0-b_1+b_2-b_3, a_1+2a_2+3a_3+b_1-2b_2+3b_3)=\\=(a_0-a_1+a_2-a_3,a_1+2a_2+3a_3)+(b_0-b_1+b_2-b_3,b_1+2b_2+3b_3)$$

$$(a_0-a_1+a_2-a_3+b_0-b_1+b_2-b_3, a_1+2a_2+3a_3+b_1+2b_2+3b_3)=\\=(a_0-a_1+a_2-a_3+b_0-b_1+b_2-b_3, a_1+2a_2+3a_3+b_1+2b_2+3b_3)$$

This identity holds.

$$\varphi(\lambda P)=\lambda\varphi(P)$$

$$\varphi(\lambda a_0+\lambda a_1x+\lambda a_2x^2+\lambda a_3x^3)=\lambda\varphi(a_0+a_1x+a_2x^2+a_3x^3)$$

$$(\lambda a_0-\lambda a_1+\lambda a_2-\lambda a_3,\lambda a_1-2\lambda a_2+3\lambda a_3)=\lambda(a_0-a_1+a_2-a_3,a_1-2a_2+3a_3)$$

$$(\lambda a_0-\lambda a_1+\lambda a_2-\lambda a_3,\lambda a_1-2\lambda a_2+3\lambda a_3)=\\=(\lambda a_0-\lambda a_1+\lambda a_2-\lambda a_3,\lambda a_1-2\lambda a_2+3\lambda a_3)$$

This identity also holds.

---

Let's apply $\varphi$ to each of the basis vectors from $\mathbf{e}$:

$$e_1=1\mapsto(1,0),\quad e_2=x\mapsto(-1, 1),\quad e_3=x^2\mapsto(1,2),\quad e_4=x^3\mapsto(-1,3)$$

Coordinates of the vectors in basis $\mathbf{f}$ would be the same since it's the standard basis; therefore, write out the transformation matrix:

$$A(\varphi,\mathbf{e},\mathbf{f})=\begin{pmatrix}
    1 & -1 & 1 & -1\\
    0 & 1 & 2 & 3
\end{pmatrix}$$

## Problem 4

Let vector space $V$ be defined as $V=U\oplus W$ for two subspaces $U, W\subseteq V$. Prove that the mapping $\varphi\colon V\mapsto U$, mapping each vector to its projection on $U$ along $W$ is linear. Find the matrix of this linear mapping in a pair of bases $(\mathbf{e}\cup \mathbf{f},\mathbf{e})$, where $\mathbf{e}$ is some basis of a subspace $U$ and $\mathbf{f}$ is some basis of a subspace $W$.

---

Originally, any such vector in basis $(u_1,u_2,\dots,u_n,w_1,w_2,\dots,w_m)$, where $n=\dim U, m=\dim W$ would have a form of 

$$v=\begin{pmatrix}
    a_1\\
    a_2\\
    \vdots\\
    a_n\\
    b_1\\
    b_2\\
    \vdots\\
    b_m\\
\end{pmatrix}$$

When we take a projection of a vector to $U$ along $W$, we map that vector to a vector in a basis $(u_1,u_2,\dots,u_n)$:

$$\begin{pmatrix}
    a_1\\
    a_2\\
    \vdots\\
    a_n\\
    b_1\\
    b_2\\
    \vdots\\
    b_m\\
\end{pmatrix}\mapsto\begin{pmatrix}
    a_1\\
    a_2\\
    \vdots\\
    a_n\\
\end{pmatrix}$$

Instead of blindly checking whether this transformation is linear, I will say that this transformation just strips last $m$ dimensions of a vector, thus it is certainly linear.

---

Now, find images of each of the basis vectors:
* $u_i\mapsto u_i$
* $w_i\mapsto\vec{0}$

Since we just strip dimensions in this transformation, the transformation matrix would look like this:

$$A(\varphi,\mathbf{e\cup f},\mathbf{e})=\left(\begin{array}{cccc|cccc}
    1 & 0 & \dots & 0 & 0 & \dots & 0 & 0\\
    0 & 1 & \dots & 0 & 0 & \dots & 0 & 0\\
    \vdots & \vdots & \ddots & \vdots & \vdots & \ddots & \vdots& \vdots\\
    0 & 0 & \dots & 1 & 0 & \dots & 0 & 0
\end{array}\right)$$

## Problem 5

Let linear mapping $\mathcal{A}\colon V\mapsto W$ in bases $(e_1, e_2, e_3)$ of space $V$ and $(f_1, f_2)$ of subspace $W$ have a matrix $\begin{pmatrix}
    0 & 1 & 2\\
    3 & 4 & 5
\end{pmatrix}$. Find the matrix of a mapping $\mathcal{A}$ in bases $(e_1, e_1+e_2, e_1+e_3)$ and $(f_1,f_1+f_2)$.

---

Transformation matrices from the standard basis in $\mathbb{R}^3$ to $(e_1, e_1+e_2, e_1+e_2+e_3)$ is

$$\begin{pmatrix}
    1 & 1 & 1\\
    0 & 1 & 0\\
    0 & 0 & 1
\end{pmatrix}$$

Transformation matrices from the standard basis in $\mathbb{R}^2$ to $(f_1,f_1+f_2)$ is

$$\begin{pmatrix}
    1 & 1\\
    0 & 1\\
\end{pmatrix}$$

and its inverse is 

$$\begin{pmatrix}
    1 & -1\\
    0 & 1\\
\end{pmatrix}$$

To find the matrix in the new basis, multiply the original matrix from the right by the first transformation matrix and then multiple it from the left by the inverse of the second transformation matrix

$$\begin{pmatrix}
    1 & -1\\
    0 & 1\\
\end{pmatrix}\begin{pmatrix}
    0 & 1 & 2\\
    3 & 4 & 5
\end{pmatrix}\begin{pmatrix}
    1 & 1 & 1\\
    0 & 1 & 1\\
    0 & 0 & 1
\end{pmatrix}=\begin{pmatrix}
    -3 & -6 & -12\\
    3 & 7 & 12
\end{pmatrix}$$

## Problem 6

Let $V=\mathbb{R}[x]_{\leqslant2}$ be a space of polynomials with real coefficients with an argument $x$ of degree not higher than $2$. A linear mapping $\varphi\colon V\mapsto \mathbb{R}^2$ in basis $(2x+x^2,x,1-x)$ in space $V$ and basis $((3,2), (1,1))$ in space $\mathbb{R}^2$ has a matrix 

$$\begin{pmatrix}
    1 & 1 & -3\\
    -3 & -1 & 6
\end{pmatrix}$$

Find $\varphi(3+2x+x^2)$.

---

Find coordinates of $3+2x+x^2$ in the first basis:

$$3+2x+x^2=1\times(2x+x^2)+3\times x+3(1-x)\implies\begin{pmatrix}1\\3\\3\end{pmatrix}$$

Coordinates of the image of $\varphi(3+2x+x^2)$ in basis $((3,2), (1,1))$ are equal to:

$$\begin{pmatrix}
    1 & 1 & -3\\
    -3 & -1 & 6
\end{pmatrix}\begin{pmatrix}1\\3\\3\end{pmatrix}=\begin{pmatrix}
    1 + 3 -9\\
    -3 -3 +18
\end{pmatrix}=\begin{pmatrix}
    -5\\
    12
\end{pmatrix}$$



## Problem 7

Linear mapping $\varphi\colon\mathbb{R}^4\mapsto\mathbb{R}^3$ in a pair of standard bases has a matrix $\begin{pmatrix}
    1 & 1 & 0 & 2\\
    3 & -3 & 2 & 0\\
    2 & -1 & 1 & 1
\end{pmatrix}$. Find the basis of the kernel of this linear mapping.

---

To find the kernel, we need to find all vectors that get mapped to $0$. For this, find the fundamental system of solutions for the system of linear equations $Ax=0$ defined by the matrix above:

$$\begin{pmatrix}
    1 & 1 & 0 & 2\\
    3 & -3 & 2 & 0\\
    2 & -1 & 1 & 1
\end{pmatrix}\sim\begin{pmatrix}
    1 & 0 & \frac{1}{3} & 1\\
    0 & 1 & -\frac{1}{3} & 1\\
    0 & 0 & 0 & 0
\end{pmatrix}\implies\Phi=\begin{pmatrix}
    -\frac{1}{3} & -1\\
    \frac{1}{3} & -1\\
    1 & 0\\
    0 & 1\\
\end{pmatrix}$$

Since the bases are standard, we already have it calculated:

The required basis of $\ker\varphi$ is 

$$\begin{pmatrix}
    -1 \\
    1\\
    3\\
    0
\end{pmatrix}, \begin{pmatrix}
    -1\\
    -1\\
    0\\
    1
\end{pmatrix}$$


## Problem 8

Find the basis of the kernel of linear mapping $\varphi\colon M_2(\mathbb{R})\mapsto M_2(\mathbb{R}),\varphi(X)=AX$, where $A=\begin{pmatrix}
    1 & 2\\
    2 & 4
\end{pmatrix}$.

---

Calculate the matrix 

$$AX=\begin{pmatrix}
    1 & 2\\
    2 & 4
\end{pmatrix}\begin{pmatrix}
    a & b\\
    c & d
\end{pmatrix}=\begin{pmatrix}
    a + 2c & b + 2d\\
    2a + 4c & 2b + 4d
\end{pmatrix}$$

Rearrange the matrices in the linear mapping as vectors as follows:

$$\begin{pmatrix}
    a\\
    b\\
    c\\
    d
\end{pmatrix}\mapsto\begin{pmatrix}
    a + 2c \\
    b + 2d \\
    2a + 4c \\
    2b + 4d
\end{pmatrix}$$

Assuming standard bases as nothing else is said about them, find the matrix of the linear mapping:

$$\begin{pmatrix}
    1\\
    0\\
    0\\
    0
\end{pmatrix}\mapsto\begin{pmatrix}
    1\\
    0\\
    2\\
    0
\end{pmatrix},\quad\begin{pmatrix}
    0\\
    1\\
    0\\
    0
\end{pmatrix}\mapsto\begin{pmatrix}
    0\\
    1\\
    0\\
    2
\end{pmatrix},\quad\begin{pmatrix}
    0\\
    0\\
    1\\
    0
\end{pmatrix}\mapsto\begin{pmatrix}
    2\\
    0\\
    4\\
    0
\end{pmatrix},\quad\begin{pmatrix}
    0\\
    0\\
    0\\
    1
\end{pmatrix}\mapsto\begin{pmatrix}
    0\\
    2\\
    0\\
    4
\end{pmatrix}$$

Therefore,

$$A(\varphi, \mathbf{e_1},\mathbf{e_2})=\begin{pmatrix}
    1 & 0 & 2 & 0\\
    0 & 1 & 0 & 2\\
    2 & 0 & 4 & 0\\
    0 & 2 & 0 & 4
\end{pmatrix}$$

Now, solve a system of linear equations $Ax=0$ for this matrix and find its fundamental system of solutions:

$$\begin{pmatrix}
    1 & 0 & 2 & 0\\
    0 & 1 & 0 & 2\\
    2 & 0 & 4 & 0\\
    0 & 2 & 0 & 4
\end{pmatrix}\sim\begin{pmatrix}
    1 & 0 & 2 & 0\\
    0 & 1 & 0 & 2\\
    0 & 0 & 0 & 0\\
    0 & 0 & 0 & 0
\end{pmatrix}\implies\Phi=\begin{pmatrix}
    -2 & 0\\
    0 & -2\\
    1 & 0\\
    0 & 1\\
\end{pmatrix}$$

Since the bases are standard, we may write the final basis based on the solution above:

$$\left(\begin{pmatrix}
    -2 & 0\\
    1 & 0\\
\end{pmatrix}, \begin{pmatrix}
    0 & -2\\
    0 & 1\\
\end{pmatrix}\right)$$

## Problem 9

Prove that any subspace $L$ of a vector space $V$ of finite dimension is a kernel of some linear mapping $\varphi\colon V\mapsto W$ ($W$ can be chosen arbitrarily) and an image of some linear mapping $\psi\colon U\mapsto V$ ($U$ can be chosen arbitrarily). 

---

Firstly, we could just take a linear mapping that collapses all vectors in a certain subspace to a zero (sum of zeros and multiplication of a zero by a scalar results in a zero, so such mapping would be linear).

Therefore, we could take any subspace $L\subseteq V$ with a basis of $(l_1, l_2,\dots,l_n)$. Extending this basis to the basis of the entire space, we would get $(l_1, l_2,\dots,l_n,v_1,v_2,\dots,v_m)$. Now, we could define a mapping $\varphi\colon(l_1, l_2,\dots,l_n,v_1,v_2,\dots,v_m)\mapsto(0,0,\dots,0,v_1,v_2,\dots,v_m)$, which would obviously map any vectors of our subspace $L$ that have a form of $(l_1, l_2,\dots,l_n, 0,0,\dots,0)$ to $(0,0,\dots,0,0,0,\dots,0)\implies$ we have constructed a mapping that always sends vectors from $L$ to $\vec{0}$, implying $L=\ker\varphi$.

As for the image, once again, the extended basis of $L$ in $V$ is $(l_1, l_2,\dots,l_n, 0,0,\dots,0)$. We could simply such choose a vector space $U$ that $U=L$ and an $\text{id}$ linear mapping $\psi$ such that for $u=(u_1, u_2,\dots,u_n)$, $\psi(u)\mapsto l\in L,l=(u_1, u_2,\dots,u_n, 0,0,\dots,0)$. This mapping is also linear (we simply add more zero dimensions, linearity doesn't change) and it's always possible to find such a vector space to map from $\implies L=\text{Im}\,\psi$.
