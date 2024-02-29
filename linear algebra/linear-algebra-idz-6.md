# Individual Homework 6, Linear Algebra

## Problem 1

Let $V = \mathbb{R}[x]_{\leqslant2}$ be a space of polynomials with real coefficients from varaible $x$ of degree not higher than $2$. Linear mapping $\varphi\colon V\mapsto\mathbb{R}^2$ in basis $(1+x+x^2,-2+2x+3x^2,-1+x+2x^2)$ of space $V$ in basis $((-1,1), (3,1))$ of space $\mathbb{R}^2$ has a matrix 

$$\begin{pmatrix}
    -2 & -1 & 5\\
    -1 & 4 & 3\\
\end{pmatrix}$$

Find $\varphi(-3+5x+6x^2)$.

---

Let's find coordinates of this polynomial in given basis

$$-3+5x+6x^2\mapsto(-3,5,6)$$

$$(1+x+x^2,-2+2x+3x^2,-1+x+2x^2)\mapsto((1,1,1),(-2,2,3),(-1,1,2))$$

Basis vectors go into columns and solve the HSLE $Ax=(-3,5,6)^T$:

$$\begin{pmatrix}
    1 & -2 & -1 & \bigm| & -3\\
    1 & 2 & 1 & \bigm| & 5\\
    1 & 3 & 2 & \bigm| & 6
\end{pmatrix}\sim\begin{pmatrix}
    1 & 0 & 0 & \bigm| & 1\\
    0 & 1 & 0 & \bigm| & 3\\
    0 & 0 & 1 & \bigm| & -2
\end{pmatrix}$$

Coordinates of given polynomial in the first basis are equal to $(1,3,-2)$.

Apply the transformation matrix to this vector to get:

$$\begin{pmatrix}
    -2 & -1 & 5\\
    -1 & 4 & 3\\
\end{pmatrix}\begin{pmatrix}
    1\\
    3\\
    -2
\end{pmatrix}=\begin{pmatrix}
    -2\times1 + -1\times3 + 5\times-2\\
    -1\times1 + 4\times3 + 3\times-2
\end{pmatrix}=$$

$$=\begin{pmatrix}
    -2-3-10\\
    -1+12-6
\end{pmatrix}=\begin{pmatrix}
    -15\\
    5
\end{pmatrix}$$

which means that $\varphi(-3+5x+6x^2)=(-15,5)^T$

## Problem 2

### Subproblem A

Prove that only a single linear mapping $\varphi\colon\mathbb{R}^5\mapsto\mathbb{R}^3$ exists such that it maps vectors 

$$a_1=(-2,-3,4,2,-1), a_2=(0,3,0,3,-2), a_3=(-2,2,-5,0,0),\\a_4=(-5,-2,3,-3,2),a_5=(-5,-5,-3,-1,1)$$

to corresponding vectors

$$b_1=(50,68,14), b_2=(42,41,13), b_3=(-30,-72,-6),\\b_4=(-5,-12,-1),b_5=(-39,-78,-9)$$

---

> Note that I have redefined the fields of the matrix with the same letters as the original vectors so please don't get confused.

The linear mapping transformation matrix would take the form of and be applied like

$$\begin{pmatrix}
    a_1 & a_2 & a_3 & a_4 & a_5\\
    b_1 & b_2 & b_3 & b_4 & b_5\\
    c_1 & c_2 & c_3 & c_4 & c_5\\
\end{pmatrix}a_1^T=b_1^T$$

which would leave us with the following SLEs. We need to prove that each of them has only a single solution.

For $a_i$:

$$\begin{pmatrix}
    -2 & -3 & 4 & 2 & -1 & 50\\
    0 & 3 & 0 & 3 & -2 & 42\\
    -2 & 2 & -5 & 0 & 0 & -30\\
    -5 & -2 & 3 & -3 & 2 & -5\\
    -5 & -5 & -3 & -1 & 1 & -39
\end{pmatrix}\sim\begin{pmatrix}
    1 & 0 & 0 & 0 & 0 & -2\\
    0 & 1 & 0 & 0 & 0 & 3\\
    0 & 0 & 1 & 0 & 0 & 8\\
    0 & 0 & 0 & 1 & 0 & 13\\
    0 & 0 & 0 & 0 & 1 & 3
\end{pmatrix}$$

therefore, there is a single solution of $(a_1,a_2,a_3,a_4,a_5)=(-2,3,8,13,3)$

For $b_i$:

$$\begin{pmatrix}
    -2 & -3 & 4 & 2 & -1 & 68\\
    0 & 3 & 0 & 3 & -2 & 41\\
    -2 & 2 & -5 & 0 & 0 & -72\\
    -5 & -2 & 3 & -3 & 2 & -12\\
    -5 & -5 & -3 & -1 & 1 & -78
\end{pmatrix}\sim\begin{pmatrix}
    1 & 0 & 0 & 0 & 0 & 3\\
    0 & 1 & 0 & 0 & 0 & 2\\
    0 & 0 & 1 & 0 & 0 & 14\\
    0 & 0 & 0 & 1 & 0 & 13\\
    0 & 0 & 0 & 0 & 1 & 2
\end{pmatrix}$$

therefore, there is a single solution of $(b_1,b_2,b_3,b_4,b_5)=(3,2,14,13,2)$

For $c_i$

$$\begin{pmatrix}
    -2 & -3 & 4 & 2 & -1 & 14\\
    0 & 3 & 0 & 3 & -2 & 13\\
    -2 & 2 & -5 & 0 & 0 & -6\\
    -5 & -2 & 3 & -3 & 2 & -1\\
    -5 & -5 & -3 & -1 & 1 & -9
\end{pmatrix}\sim\begin{pmatrix}
    1 & 0 & 0 & 0 & 0 & -1\\
    0 & 1 & 0 & 0 & 0 & 1\\
    0 & 0 & 1 & 0 & 0 & 2\\
    0 & 0 & 0 & 1 & 0 & 4\\
    0 & 0 & 0 & 0 & 1 & 1
\end{pmatrix}$$

therefore, there is a single solution of $(c_1,c_2,c_3,c_4,c_5)=(-1,1,2,4,1)$

which implies there is a unique linear mapping that maps these vectors to their corresponding:

$$\begin{pmatrix}
    -2 & 3 & 8 & 13 & 3\\
    3 & 2 & 14 & 13 & 2\\
    -1 & 1 & 2 & 4 & 1
\end{pmatrix}$$

### Subproblem B

Find the basis of the kernel and the image of this linear mapping. Present the answer in a standard basis.

---

To find the kernel of the linear mapping, solve the matrix from above as a HSLU:

$$\begin{pmatrix}
    -2 & 3 & 8 & 13 & 3\\
    3 & 2 & 14 & 13 & 2\\
    -1 & 1 & 2 & 4 & 1
\end{pmatrix}\sim\begin{pmatrix}
    1 & 0 & 2 & 1 & 0\\
    0 & 1 & 4 & 5 & 1\\
    0 & 0 & 0 & 0 & 0
\end{pmatrix}$$

Now find the fundamental system of solutions:

$$\Phi=\begin{pmatrix}
    -2 & -1 & 0\\
    -4 & -5 & -1\\
    1 & 0 & 0\\
    0 & 1 & 0\\
    0 & 0 & 1
\end{pmatrix}$$

Since the bases we're working in are standard, then the basis of $\ker\varphi$ is

$$\begin{pmatrix}
    -2\\
    -4\\
    1\\
    0\\
    0\\
\end{pmatrix},\quad\begin{pmatrix}
    -1\\
    -5\\
    0\\
    1\\
    0
\end{pmatrix},\quad\begin{pmatrix}
    0\\
    -1\\
    0\\
    0\\
    1
\end{pmatrix}$$

To get the image from here, we know that the main variables in the reduced row echelon form give us the basis of $\text{im}\ \varphi$ in the pair of standard bases, so we simply take

$$\begin{pmatrix}
    -2\\
    3\\
    -1
\end{pmatrix},\quad\begin{pmatrix}
    3\\
    2\\
    1
\end{pmatrix}$$

## Problem 3

Linear mapping $\varphi\colon\mathbb{R^5}\mapsto\mathbb{R^5}$ in a pair of standard bases has a matrix 

$$\begin{pmatrix}
    -3 & -1 & -3 & -2 & 1\\
    7 & -11 & 10 & 4 & 7\\
    2 & 5 & 1 & 3 & -3\\
    5 & -3 & 6 & 6 & 3\\
    1 & 0 & 1 & 5 & 2
\end{pmatrix}$$

Construct some linear mapping $\psi\colon\mathbb{R^5}\mapsto\mathbb{R^5}$ for which $\ker\psi=\text{im}\ \varphi$ and $\text{im}\ \psi=\ker\varphi$ and present its matrix in a pair of standard bases.

---

Firstly, find the bases of the image and the kernel of $\varphi$, similar to above:

$$\begin{pmatrix}
    -3 & -1 & -3 & -2 & 1\\
    7 & -11 & 10 & 4 & 7\\
    2 & 5 & 1 & 3 & -3\\
    5 & -3 & 6 & 6 & 3\\
    1 & 0 & 1 & 5 & 2
\end{pmatrix}\sim\begin{pmatrix}
    1 & 0 & 0 & 63 & 30\\
    0 & 1 & 0 & -13 & -7\\
    0 & 0 & 1 & -58 & -28\\
    0 & 0 & 0 & 0 & 0\\
    0 & 0 & 0 & 0 & 0\\
\end{pmatrix}$$

$$\Phi=\begin{pmatrix}
    -63 & -30\\
    13 & 7 \\
    58 & 28\\
    1 & 0 \\
    0 & 1
\end{pmatrix}$$

which means that the basis of $\ker\varphi$ is 

$$\begin{pmatrix}
    -63\\
    13\\
    58\\
    1\\
    0\\
\end{pmatrix},\begin{pmatrix}
    -30\\
    7 \\
    28\\
    0 \\
    1
\end{pmatrix}$$

simplifying it slightly:

$$\begin{pmatrix}
    -3\\
    -1\\
    2\\
    1\\
    -2\\
\end{pmatrix},\begin{pmatrix}
    -30\\
    7 \\
    28\\
    0 \\
    1
\end{pmatrix}$$

and the basis of $\text{im}\ \varphi$ is 

$$\begin{pmatrix}
    -3\\
    7\\
    2\\
    5\\
    1\\
\end{pmatrix},\begin{pmatrix}
    -1\\
    -11\\
    5\\
    -3\\
    0
\end{pmatrix},\begin{pmatrix}
    -3\\
    10\\
    1\\
    6\\
    1
\end{pmatrix}$$

Let's simplify the basis of the image, write the vectors as rows in reversed order:

$$\begin{pmatrix}
    1 & 6 & 1 & 10 & -3\\
    0 & -3 & 5 & -11 & -1\\
    1 & 5 & 2 & 7 & -3
\end{pmatrix}\sim\begin{pmatrix}
    1 & 0 & 0 & -1 & \frac{1}{2}\\
    0 & 1 & 0 & 2 & -\frac{1}{2}\\
    0 & 0 & 1 & -1 & -\frac{1}{2}
\end{pmatrix}$$

Bring back the basis, which now looks like:

$$\begin{pmatrix}
    -\frac{1}{2}\\
    -1\\
    1\\
    0\\
    0
\end{pmatrix},\begin{pmatrix}
    -\frac{1}{2}\\
    2\\
    0\\
    1\\
    0
\end{pmatrix},\begin{pmatrix}
    \frac{1}{2}\\
    -1\\
    0\\
    0\\
    1
\end{pmatrix}$$

---

Now, we may try and construct the matrix of the linear mapping $\psi$ by first treating this basis of the image of the linear mapping $\varphi$ as a fundamental system of solutions of the transformation matrix of mapping $\psi$ 

$$\begin{pmatrix}
    1 & 0 & \frac{1}{2} & \frac{1}{2} & -\frac{1}{2}\\
    0 & 1 & 1 & -2 & 1\\
    0 & 0 & 0 & 0 & 0\\
    0 & 0 & 0 & 0 & 0\\
    0 & 0 & 0 & 0 & 0\\
\end{pmatrix}$$

and we need to bring this back to such a form that the first two columns would be as follows:

$$\begin{pmatrix}
    -3 & -30 & \diamond & \diamond & \diamond\\
    -1 & 7 & \diamond & \diamond & \diamond\\
    2 & 28 & \diamond & \diamond & \diamond\\
    1 & 0 & \diamond & \diamond & \diamond\\
    -2 & 1 & \diamond & \diamond & \diamond\\
\end{pmatrix}$$

thus, the first column would be a linear combination of $-3\begin{pmatrix}
    1 & 0 & \frac{1}{2} & \frac{1}{2} & -\frac{1}{2}
\end{pmatrix}-30\begin{pmatrix}0 & 1 & 1 & -2 & 1\end{pmatrix}$ and so on for the other columns, thus giving us the matrix:

$$\begin{pmatrix}
    -3 & -30 & -\frac{63}{2} & \frac{117}{2} &-\frac{57}{2}\\
    -1 & 7 & \frac{13}{2} & -\frac{29}{2} & \frac{15}{2}\\
    2 & 28 & 29 & -55 & 27\\
    1 & 0 & \frac{1}{2} & \frac{1}{2} & -\frac{1}{2}\\
    -2 & 1 & 0 & -3 & 2
\end{pmatrix}$$

Let's multiply this matrix by $2$ for neatness (we can do that since any scalar multipled by a zero vector yields a zero vector), and this would be our final answer:

$$\begin{pmatrix}
    -6 & -60 & -63 & 117 & -57\\
    -2 & 14 & 13 & -29 & 15\\
    4 & 56 & 58 & -110 & 54\\
    2 & 0 & 1 & 1 & -1\\
    -4 & 2 & 0 & -6 & 4
\end{pmatrix}$$

## Problem 4

Linear mapping $\varphi\colon\mathbb{R^5}\mapsto\mathbb{R^4}$ in bases $\textbf{e}=(e_1,e_2,e_3,e_4,e_5)$ and $\textbf{f}=(f_1,f_2,f_3,f_4)$ has a matrix 

$$A=\begin{pmatrix}
    1 & -24 & 45 & 36 & 12\\
    20 & 0 & 20 & 44 & -14\\
    36 & 4 & -9 & 2 & 16\\
    -3 & -20 & 36 & 26 & 10\\
\end{pmatrix}$$

Find bases of spaces $\mathbb{R}^5$ and $\mathbb{R}^4$, in which the matrix of the mapping $\varphi$ has a diagonal form $F$ with ones and zeros on the diagonal. Present this matrix and the corresponding matrix decomposition $A=C_1DC_2^{-1}$, where $C_1,C_2$ are non-singular matrices.

---

Find the basis of $\ker\varphi$, similarly to above:

$$A=\begin{pmatrix}
    1 & -24 & 45 & 36 & 12\\
    20 & 0 & 20 & 44 & -14\\
    36 & 4 & -9 & 2 & 16\\
    -3 & -20 & 36 & 26 & 10\\
\end{pmatrix}\sim\begin{pmatrix}
    1 & 0 & 0 & \frac{3}{10} & \frac{9}{20}\\
    0 & 1 & 0 & \frac{83}{40} & -\frac{211}{80}\\
    0 & 0 & 1 & \frac{19}{10} & -\frac{23}{20}\\
    0 & 0 & 0 & 0 & 0
\end{pmatrix}$$

By writing out FSS we can instantaneously also get the vectors of the basis of $\ker\varphi$:

$$\Phi=\begin{pmatrix}
    -6 & -9\\
    -\frac{83}{2} &\frac{211}{4}\\
    -38 & 23\\
    20 & 0\\
    0 & 20
\end{pmatrix}$$

Thus, assume that 

$$e'_4=\begin{pmatrix}
    -6\\
    -\frac{83}{2}\\
    -38\\
    20\\
    0
\end{pmatrix},\quad e'_5=\begin{pmatrix}
    -9\\
    \frac{211}{4}\\
    23\\
    0\\
    20
\end{pmatrix}$$

Take first three vectors from the original basis as a complement to the sought-after basis $\textbf{e}'$, which would be $(e_1,e_2,e_3,e'_4, e'_5)=(e'_1,e'_2,e'_3,e'_4,e'_5), e_1=e_1', e_2=e_2', e_3=e_3', e_4'=-6e_1-\frac{83}{2}e_2-38e_3+20e_4, e_5'=-9e_1+\frac{211}{4}e_2+23e_3+20e_5$

Now, take images of each of the basis vectors to get the second basis:

$$f'_1=\varphi(e_1')=\varphi(e_1)=(f_1,f_2,f_3,f_4)\begin{pmatrix}
    1\\
    20\\
    36\\
    -3
\end{pmatrix}=f_1+20f_2+36f_3-3f_4$$

$$f'_2=\varphi(e_2')=\varphi(e_2)=(f_1,f_2,f_3,f_4)\begin{pmatrix}
    -24\\
    0\\
    4\\
    -20
\end{pmatrix}=-24f_1+4f_3-20f_4$$

$$f'_3=\varphi(e_3')=\varphi(e_3)=(f_1,f_2,f_3,f_4)\begin{pmatrix}
    45\\
    20\\
    -9\\
    36
\end{pmatrix}=45f_1+20f_2-9f_3+36f_4$$

complement this basis using a vector $f'_4=f_4$

Thus, we get matrix $D$:

$$D=\begin{pmatrix}
    1 & 0 & 0 & 0 & 0\\
    0 & 1 & 0 & 0 & 0\\
    0 & 0 & 1 & 0 & 0\\
    0 & 0 & 0 & 0 & 0
\end{pmatrix}$$

and the matrix decomposition is:

$$A=\begin{pmatrix}
    1 & -24 & 45 & 0\\
    20 & 0 & 20 & 0\\
    36 & 4 & -9 & 0\\
    -3 & -20 & 36 & 1\\
\end{pmatrix}\begin{pmatrix}
    1 & 0 & 0 & 0 & 0\\
    0 & 1 & 0 & 0 & 0\\
    0 & 0 & 1 & 0 & 0\\
    0 & 0 & 0 & 0 & 0
\end{pmatrix}\begin{pmatrix}
    1 & 0 & 0 & -6 & -9\\
    0 & 1 & 0 & -\frac{83}{2} & \frac{211}{4}\\
    0 & 0 & 1 & -38 & 23\\
    0 & 0 & 0 & 20 & 0\\
    0 & 0 & 0 & 0 & 20
\end{pmatrix}^{-1}$$

## Problem 5

Let $V=\mathbb{R}[x]_{\leqslant2}$ be a space of polynomials of degree not higher than $2$ from variable $x$ with real coefficients. Let $(\varepsilon_1,\varepsilon_2,\varepsilon_3)$ be a base of space $V^*$ dual to basis $\mathbf{e}$

$$-1+x+3x^2,\quad2-3x-4x^2,\quad4-21x^2$$

of space $V$, and $(f_1,f_2,f_3)$ be basis of space $V$, to which basis $(\rho_1,\rho_2,\rho_3)$ in space $V^*$ is dual, where

$$\rho_1(f)=f(1),\quad\rho_2(f)=f'(-1),\quad\rho_3(f)=\frac{3}{2}\int\limits^2_0f(x)dx$$

Consider a linear function $\alpha\in V^*$ that has coordinates $(-4,4,4)$ in basis $(\varepsilon_1,\varepsilon_2,\varepsilon_3)$, and a polynomial $h\in V$ that has coordinates $(-4,4,4)$ in basis $(f_1,f_2,f_3)$. Find the value of $\alpha(h)$

---

Let's look at what $\rho$-s do to our polynomial $a+bx+cx^2$:

$$\rho_1(a+bx+cx^2)=a+b+c$$

$$\rho_2(a+bx+cx^2)=b-2c$$

$$\rho_3(a+bx+cx^2)=\frac{3}{2}\left(\left(ax+\frac{bx^2}{2}+\frac{cx^3}{3}\right)\Biggm|_2-\left(ax+\frac{bx^2}{2}+\frac{cx^3}{3}\right)\Biggm|_0\right)=$$

$$=\frac{3}{2}\left(2a+2b+\frac{8}{3}c\right)=3a+3b+4c$$

Thus, the transformation matrix of basis $\Rho=(\rho_1,\rho_2,\rho_3)$ is

$$\begin{pmatrix}
    1 & 1 & 1\\
    0 & 1 & -2\\
    3 & 3 & 4
\end{pmatrix}$$

Take its inverse to find the specific values of the dual basis $\mathbf{f}$: 

$$\begin{pmatrix}
    10 & -1 & -3\\
    -6 & 1 & 2\\
    -3 & 0 & 1
\end{pmatrix}$$

and we get the basis

$$\mathbf{f}=(10-6x-3x^2,-1+x,-3+2x+x^2)$$

Since $h$ has coordinates $(-4,4,4)$, then

$$h=-4(10-6x-3x^2)+4(-1+x)+4(-3+2x+x^2)=$$

$$=4(-10+6x+3x^2-1+x-3+2x+x^2)=-56+36x+16x^2$$

Now, find the transformation matrix from $\mathbf{f}\mapsto\mathbf{e}$, write the vectors from $\mathbf{e}=(-1+x+3x^2,2-3x-4x^2,4-21x^2)$ into columns along the transformation matrix from above and find the solution of this SLU:

$$\begin{pmatrix}
    -1 & 2 & 4 & \bigm| & 10 & -1 & -3\\
    1 & -3 & 0 & \bigm| & -6 & 1 & 2\\
    3 & -4 & -21 & \bigm| & -3 & 0 & 1
\end{pmatrix}\sim\begin{pmatrix}
    1 & 0 & 0 & \bigm| & -438 & 37 & 125\\
    0 & 1 & 0 & \bigm| & -144 & 12 & 41\\
    0 & 0 & 1 & \bigm| & -35 & 3 & 10\\ 
\end{pmatrix}$$

this implies that the transformation matrix is

$$\begin{pmatrix}
    -438 & 37 & 125\\
    -144 & 12 & 41\\
    -35 & 3 & 10
\end{pmatrix}$$

and that 

$$\varepsilon_1=-438\rho_1+37\rho_2+125\rho_3$$

$$\varepsilon_2=-144\rho_1+12\rho_2+41\rho_3$$

$$\varepsilon_3=-35\rho_1+3\rho_2+10\rho_3$$

Since coordinates of $\alpha$ are $(-4,4,4)$, then we get:

$$\alpha=-4\varepsilon_1+4\varepsilon_2+4\varepsilon_3$$

$$\alpha=4(-\varepsilon_1+\varepsilon_2+\varepsilon_3)$$

$$\alpha(h)=4(259\rho_1(h)-22\rho_2(h)-74\rho_3(h))$$

Calculate values of $\rho_i$ for $h=-56+36x+16x^2$:

$$\rho_1(h)=-56+36+16=4$$

$$\rho_2(h)=36-32=4$$

$$\rho_3(h)=-168+108+64=4$$

and we get 

$$\alpha(h)=16(259-22-74)=16\times163=2\,608$$

which is our answer (actually the numbers were weirdly cooperative this time somehow).

