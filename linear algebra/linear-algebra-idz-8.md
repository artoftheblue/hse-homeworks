# Linear Algebra, Individual Homework 8, Variant 18

## Problem 1

Complement vector $v=\frac{1}{10}(-5,1,7,5)$ to an orthonormal basis in $\mathbb{R}^4$.

---

Add three vectors to the existing one:

$$\langle v,e_2,e_3,e_4\rangle$$

Since we have added the standard vectors, it's obvious that the span above would be linearly independent. Thus, apply the Gram-Schmidt orthogonalization approach:

$$f_{k + 1} = e_{k + 1} - \sum_{i = 1}^{k}{\frac{(f_i, e_i)}{(f_i,f_i)}f_i}$$

$$\begin{align*}
    f_1,=\frac{1}{10}(-5,1,7,5)\\
    f_2&=(0,1,0,0)-\frac{0.1}{1}\frac{1}{10}(-5,1,7,5)\\&=\frac{1}{100}(5,99,-7,-5)\\
    f_3&=(0,0,1,0)-\frac{0.7}{1}\frac{1}{10}(-5,1,7,5)+\frac{0.07}{0.99}\frac{1}{100}(5,99,-7,-5)\\&=(0,0,1,0)-\frac{7}{100}(-5,1,7,5)-\frac{7}{9900}(-5,-99,7,5)\\
    &=\frac{1}{99}(35,0,50,-35)\\
    f_4&=(0,0,0,1)-\frac{0.5}{1}\frac{1}{10}(-5,1,7,5)+\frac{0.05}{0.99}\frac{1}{100}(5,99,-7,-5)+\frac{35}{99}\frac{33^2}{25\cdot22}\frac{1}{99}(35,0,50,-35)\\
    &=(0,0,0,1)-\frac{1}{20}(-5,1,7,5)+\frac{5}{9900}(5,99,-7,-5)+\frac{7}{990}(35,0,50,-35)\\
    &=\frac{1}{2}(1,0,0,1)
\end{align*}$$

Now normalize all the vectors: 

$$\begin{align*}
\frac{1}{10}(-5,1,7,5)&\leadsto\frac{1}{10}(-5,1,7,5)\\
\frac{1}{100}(5,99,-7,-5)&\leadsto\frac{1}{\frac{1}{100}\sqrt{5^2+99^2+7^2+5^2}}\frac{1}{100}(5,99,-7,-5)\\
&\leadsto\frac{1}{30\sqrt{11}}(5,99,-7,-5)\\
\frac{1}{99}(35,0,50,-35)&\leadsto\frac{1}{\frac{5}{99}\sqrt{7^2+10^2+7^2}}\frac{5}{99}(7,0,10,-7)\\
&\leadsto\frac{1}{3\sqrt{22}}(7,0,10,-7)\\
\frac{1}{2}(1,0,0,1)&\leadsto\frac{1}{\sqrt{2}}(1,0,0,1)
\end{align*}
$$

## Problem 2

Subspace $U$ of a euclidean space $\mathbb{R}^4$ is defined by a system of equations 

$$\begin{cases}
    -7x_1-2x_2+x_3-30x_4=0\\
    6x_2-24x_3+6x_4=0
\end{cases}$$

For vector $v=(-1,1,-5,-3)$ find its projection to $U$, its orthogonal part in relation to $U$ and the distance from it to $U$.

---

First, find the basis that is generated by the matrix

$$\begin{pmatrix}
    -7 & -2 & 1 & -30\\
    0 & 6 & -24 & 6
\end{pmatrix}\leadsto\begin{pmatrix}
    1 & 0 & 1 & -4\\
    0 & 1 & -4 & 1
\end{pmatrix}$$

Fundamental system of solutions would be:

$$\begin{cases}
    x_1=-x_3+4x_4\\
    x_2=4x_3-x_4\\
    x_3=x_3\\
    x_4=x_4
\end{cases}$$

$$A=\begin{pmatrix}
    -1 & 4\\
    4 & -1\\
    1 & 0\\
    0 & 1
\end{pmatrix}\implies\mathbf{e}=\langle(-1, 4, 1, 0),(4, -1, 0, 1)\rangle$$

This is our basis, so we may apply the formula for an orthogonal projection:

$$\text{pr}_Uv=A(A^TA)^{-1}A^Tv$$

$$\begin{align*}\text{pr}_Uv&=\begin{pmatrix}
    -1 & 4\\
    4 & -1\\
    1 & 0\\
    0 & 1
\end{pmatrix}\left(\begin{pmatrix}
    -1 & 4 & 1 & 0\\
    4 & -1 & 0 & 1\\
\end{pmatrix}\begin{pmatrix}
    -1 & 4\\
    4 & -1\\
    1 & 0\\
    0 & 1
\end{pmatrix}\right)^{-1}\begin{pmatrix}
    -1 & 4 & 1 & 0\\
    4 & -1 & 0 & 1\\
\end{pmatrix}\begin{pmatrix}
-1\\
1\\
-4\\
-3
\end{pmatrix}\\
&=\begin{pmatrix}
    -1 & 4\\
    4 & -1\\
    1 & 0\\
    0 & 1
\end{pmatrix}\begin{pmatrix}
    18 & -8\\
    -8 & 18
\end{pmatrix}^{-1}\begin{pmatrix}
    -1 & 4 & 1 & 0\\
    4 & -1 & 0 & 1\\
\end{pmatrix}\begin{pmatrix}
-1\\
1\\
-4\\
-3
\end{pmatrix}=\\
&=\frac{1}{130}\begin{pmatrix}
    -1 & 4\\
    4 & -1\\
    1 & 0\\
    0 & 1
\end{pmatrix}\begin{pmatrix}
    9 & 4\\
    4 & 9
\end{pmatrix}\begin{pmatrix}
    -1 & 4 & 1 & 0\\
    4 & -1 & 0 & 1\\
\end{pmatrix}\begin{pmatrix}
-1\\
1\\
-4\\
-3
\end{pmatrix}=\\
&=\frac{1}{130}\begin{pmatrix}
    7 & 32\\
    32 & 7\\
    9 & 4\\
    4 & 9
\end{pmatrix}\begin{pmatrix}
    -1 & 4 & 1 & 0\\
    4 & -1 & 0 & 1\\
\end{pmatrix}\begin{pmatrix}
-1\\
1\\
-4\\
-3
\end{pmatrix}=\\
&=\frac{1}{130}\begin{pmatrix}
    121 & -4 & 7 & 32\\
    -4 & 121 & 32 & 7\\
    7 & 32 & 9 & 4\\
    32 & 7 & 4 & 9
\end{pmatrix}\begin{pmatrix}
-1\\
1\\
-4\\
-3
\end{pmatrix}=\\
&=\frac{8}{130}\begin{pmatrix}
-32\\
-7\\
-4\\
-9
\end{pmatrix}
\end{align*}$$

The orthogonal projection would be just the original vector minus its projection:

$$\text{ort}_Uv=v-\text{pr}_Uv=\begin{pmatrix}
    -1\\
    1\\
    -5\\
    -3
\end{pmatrix}-\frac{8}{130}\begin{pmatrix}
-32\\
-7\\
-4\\
-9
\end{pmatrix}=\frac{3}{65}\begin{pmatrix}
    21\\
    31\\
    -103\\
    -53
\end{pmatrix}$$

Distance would be just the length of the orthogonal projection vector:

$$\text{dist}_Uv=\frac{3}{65}\sqrt{21^2+31^2+103^2+53^2}=\frac{6}{65}\sqrt{3705}$$


## Problem 3

In euclidean space $\mathbb{R}^4$, two subspaces $U=\langle u_1,u_2\rangle$ and $W=\langle w_1,w_2\rangle$ are given, where $u_1=(-1,-2,-2,1),u_2=(-1,3,1,-3),w_1=(-2,-2,1,-1),w_2=(3,3,1,-1)$. Find the vector $v\in\mathbb{R}^4$, for which $\text{pr}_Uv=(14,3,13,6)$ and $\text{ort}_Wv=(-5,5,20,20)$.

---

Rewrite the subspaces as matrices:

$$A_U=\begin{pmatrix}
    -1 & -1 \\
    -2 & 3 \\
    -2 & 1 \\
    1 & -3
\end{pmatrix},\quad A_W=\begin{pmatrix}
    -2 & 3 \\
    -2 & 3\\
    1 & 1\\
    -1 & -1\\
\end{pmatrix}$$

We know that 

$$\text{pr}_Uv=A_U(A_U^TA_U)^{-1}A_U^Tv$$

and

$$\text{ort}_Wv=v-A_W(A_W^TA_W)^{-1}A_W^Tv$$

Calculate the coefficient matrices:

$$\begin{align*}A_U(A_U^TA_U)^{-1}A_U^T&=\begin{pmatrix}
    -1 & -1 \\
    -2 & 3 \\
    -2 & 1 \\
    1 & -3
\end{pmatrix}\left(\begin{pmatrix}
    -1 & -2 & -2 & 1 \\
    -1 & 3 & 1 & -3\\
\end{pmatrix}\begin{pmatrix}
    -1 & -1 \\
    -2 & 3 \\
    -2 & 1 \\
    1 & -3
\end{pmatrix}\right)^{-1}\begin{pmatrix}
    -1 & -2 & -2 & 1 \\
    -1 & 3 & 1 & -3\\
\end{pmatrix}\\
&=\begin{pmatrix}
    -1 & -1 \\
    -2 & 3 \\
    -2 & 1 \\
    1 & -3
\end{pmatrix}\begin{pmatrix}10 & -10\\
-10 & 20\end{pmatrix}^{-1}\begin{pmatrix}
    -1 & -2 & -2 & 1 \\
    -1 & 3 & 1 & -3\\
\end{pmatrix}\\
&=\frac{1}{10}\begin{pmatrix}
    -1 & -1 \\
    -2 & 3 \\
    -2 & 1 \\
    1 & -3
\end{pmatrix}\begin{pmatrix}2 & 1\\
1 & 1\end{pmatrix}\begin{pmatrix}
    -1 & -2 & -2 & 1 \\
    -1 & 3 & 1 & -3\\
\end{pmatrix}\\
&=\frac{1}{10}\begin{pmatrix}
    -3 & -2 \\
    -1 & 1 \\
    -3 & -1 \\
    -1 & -2
\end{pmatrix}\begin{pmatrix}
    -1 & -2 & -2 & 1 \\
    -1 & 3 & 1 & -3\\
\end{pmatrix}\\
&=\frac{1}{10}\begin{pmatrix}
    5 & 0 & 4 & 3 \\
    0 & 5 & 3 & -4 \\
    4 & 3 & 5 & 0 \\
    3 & -4 & 0 & 5
\end{pmatrix}
\end{align*}$$

$$\begin{align*}
A_W(A_W^TA_W)^{-1}A_W^T&=\begin{pmatrix}
    -2 & 3 \\
    -2 & 3\\
    1 & 1\\
    -1 & -1\\
\end{pmatrix}\left(\begin{pmatrix}
    -2 & -2 & 1 & -1 \\
    3 & 3 & 1 & -1\\
\end{pmatrix}\begin{pmatrix}
    -2 & 3 \\
    -2 & 3\\
    1 & 1\\
    -1 & -1\\
\end{pmatrix}\right
)^{-1}\begin{pmatrix}
    -2 & -2 & 1 & -1 \\
    3 & 3 & 1 & -1\\
\end{pmatrix}\\
&=\begin{pmatrix}
    -2 & 3 \\
    -2 & 3\\
    1 & 1\\
    -1 & -1\\
\end{pmatrix}\begin{pmatrix}
10 & -10\\
-10 & 20
\end{pmatrix}^{-1}\begin{pmatrix}
    -2 & -2 & 1 & -1 \\
    3 & 3 & 1 & -1\\
\end{pmatrix}\\
&=\frac{1}{10}\begin{pmatrix}
    -2 & 3 \\
    -2 & 3\\
    1 & 1\\
    -1 & -1\\
\end{pmatrix}\begin{pmatrix}
2 & 1\\
1 & 1
\end{pmatrix}\begin{pmatrix}
    -2 & -2 & 1 & -1 \\
    3 & 3 & 1 & -1\\
\end{pmatrix}\\
&=\frac{1}{10}\begin{pmatrix}
    -1 & 1 \\
    -1 & 1\\
    3 & 2\\
    -3 & -2\\
\end{pmatrix}\begin{pmatrix}
    -2 & -2 & 1 & -1 \\
    3 & 3 & 1 & -1\\
\end{pmatrix}\\
&=\frac{1}{2}\begin{pmatrix}
    1 & 1 & 0 & 0\\
    1 & 1 & 0 & 0\\
    0 & 0 & 1 & -1\\
    0 & 0 & -1 & 1
\end{pmatrix}\\
\end{align*}$$

Now we have the following:

$$\frac{1}{10}\begin{pmatrix}
    5 & 0 & 4 & 3 \\
    0 & 5 & 3 & -4 \\
    4 & 3 & 5 & 0 \\
    3 & -4 & 0 & 5
\end{pmatrix}v=(14,3,13,6)^T$$

$$\begin{pmatrix}
    5 & 0 & 4 & 3 \\
    0 & 5 & 3 & -4 \\
    4 & 3 & 5 & 0 \\
    3 & -4 & 0 & 5
\end{pmatrix}v=\begin{pmatrix}
    140\\
    30\\
    130\\
    60
\end{pmatrix}\leadsto\begin{pmatrix}
    1 & 0 & \frac{4}{5} & \frac{3}{5} &\bigm| & 28\\
    0 & 1 & \frac{3}{5} & -\frac{4}{5} &\bigm|& 6\\
    0 & 0 & 0 & 0 &\bigm| & 0\\
    0 & 0 & 0 & 0 &\bigm| & 0\\
\end{pmatrix}$$

---

$$v-\frac{1}{2}\begin{pmatrix}
    1 & 1 & 0 & 0\\
    1 & 1 & 0 & 0\\
    0 & 0 & 1 & -1\\
    0 & 0 & -1 & 1
\end{pmatrix}v=(-5,5,20,20)^T\leadsto\frac{1}{2}\begin{pmatrix}
    1 & -1 & 0 & 0\\
    -1 & 1 & 0 & 0\\
    0 & 0 & 1 & 1\\
    0 & 0 & 1 & 1
\end{pmatrix}v=(-5,5,20,20)^T$$

$$\begin{pmatrix}
    1 & -1 & 0 & 0\\
    -1 & 1 & 0 & 0\\
    0 & 0 & 1 & 1\\
    0 & 0 & 1 & 1
\end{pmatrix}v=\begin{pmatrix}
    -10\\
    10\\
    40\\
    40
\end{pmatrix}\leadsto\begin{pmatrix}
    1 & -1 & 0 & 0 &\bigm| & -10\\
    0 & 0 & 1 & 1 &\bigm|& 40\\
    0 & 0 & 0 & 0 &\bigm| & 0\\
    0 & 0 & 0 & 0 &\bigm| & 0\\
\end{pmatrix}$$

Combining these two systems together, we get:

$$\begin{pmatrix}
    1 & 0 & \frac{4}{5} & \frac{3}{5} &\bigm| & 28\\
    0 & 1 & \frac{3}{5} & -\frac{4}{5} &\bigm|& 6\\
    1 & -1 & 0 & 0 &\bigm| & -10\\
    0 & 0 & 1 & 1 &\bigm|& 40\\
\end{pmatrix}\leadsto\begin{pmatrix}
    1 & 0 & 0 & 0 & \bigm| & 0\\
    0 & 1 & 0 & 0 & \bigm| & 10\\
    0 & 0 & 1 & 0 & \bigm| & 20\\
    0 & 0 & 0 & 1 & \bigm| & 20
\end{pmatrix}$$

which implies that the required vector is 

$$v=\begin{pmatrix}
    0\\
    10\\
    20\\
    20
\end{pmatrix}$$


## Problem 4

In space $W=\mathbb{R}[x]_{\leq2}$ equipped with a structure of a euclidean space in relation to some (unknown) dot product, the volume of a parallelipiped generated by vectors $-2+4x+5x^2,6-10x-18x^2,4-6x-12x^2$ is equal to $4$. Find the volume of a parallelipiped generated by vectors $2-2x+4x^2,-4+5x-11x^2,-4+6x-10x^2$.

---

Map the vectors to two matrices, $V,U$:

$$V=\begin{pmatrix}
    -2 & 6 & 4\\
    4 & -10 & -6\\
    5 & -18 & -12\\
\end{pmatrix},\quad U=\begin{pmatrix}
    2 & -4 & -4\\
    -2 & 5 & 6\\
    4 & -11 & -10
\end{pmatrix}$$

Now find such matrix $C$ such that

$$VC=U$$

We know that $\operatorname{Vol}P(\langle v_1,v_2,v_3\rangle)=\sqrt{\det G(\langle v_1,v_2,v_3\rangle)}$, where $G(\dots)$ is a Gram matrix.

We also know that $G(\langle u_1,u_2,u_3\rangle)=C^TG(\langle v_1,v_2,v_3\rangle)C$. Therefore, $\operatorname{Vol} P(u_1,u_2,u_3)=\sqrt{\det C^TG(v_1,v_2,v_3)C}=|\det C|\sqrt{\det G(v_1,v_2,v_3)}=|\det C|\operatorname{Vol}P(\langle v_1,v_2,v_3\rangle)$

Thus, we may simply find $C$ and calculate the answer:

$$C=V^{-1}U$$

$$V^{-1}=\begin{pmatrix}
    -3 & 0 & -1\\
    -\frac{9}{2} & -1 & -1\\
    \frac{11}{2} & \frac{3}{2} & 1
\end{pmatrix}$$

$$C=\begin{pmatrix}
    -3 & 0 & -1\\
    -\frac{9}{2} & -1 & -1\\
    \frac{11}{2} & \frac{3}{2} & 1
\end{pmatrix}\begin{pmatrix}
    2 & -4 & -4\\
    -2 & 5 & 6\\
    4 & -11 & -10
\end{pmatrix}=\begin{pmatrix}
    -10 & 23 & 22\\
    -11 & 24 & 22\\
    12 & -\frac{51}{2} & -23
\end{pmatrix}\leadsto$$

$$\begin{pmatrix}
    1 & -1 & 0\\
    -11 & 24 & 22\\
    1 & -\frac{3}{2} & -1
\end{pmatrix}\leadsto\begin{pmatrix}
    1 & -1 & 0\\
    -11 & 24 & 22\\
    0 & -\frac{1}{2} & -1
\end{pmatrix}\leadsto\begin{pmatrix}
    1 & 0 & 0\\
    -11 & 13 & 22\\
    0 & -\frac{1}{2} & -1
\end{pmatrix}$$

$$\operatorname{Vol} P(u_1,u_2,u_3)=|\det C|\operatorname{Vol}P( v_1,v_2,v_3)=|-2|\operatorname{Vol}P( v_1,v_2,v_3)=2\times4=8$$

## Problem 5

Let $L$ be a three-dimensional surface in $\mathbb{R}^5$ passing through points $v_0=(-6,-6,1,-9,-7), v_1=(-2, 1,10,-14,-4), v_2=(-1,-6,-2,-5,2),v_3=(-15,-6,5,-6,-2).$ Find a point in $L$ closest to point $v=(5,0,0,10,1)$ and the distance from it to $v$.

---

Firstly, let's shift the surface to be a subspace of the entire space. To do this, we simply shift $v_0\mapsto(0,0,0,0,0)$ and for all other vectors, $v_i\mapsto v_i-v_0$:

$$y_1=v_1-v_0=\begin{pmatrix}
    -2\\ 1\\ 10\\ -14\\ -4
\end{pmatrix}-\begin{pmatrix}
    -6\\ -6\\ 1\\ -9\\ -7\\
\end{pmatrix}=\begin{pmatrix}
    4 \\ 7 \\ 9 \\ -5 \\ 3
\end{pmatrix}$$

$$y_2=v_2-v_0=\begin{pmatrix}
    -1\\
    -6\\
    -2\\
    -5\\
    -2
\end{pmatrix}-\begin{pmatrix}
    -6\\ -6\\ 1\\ -9\\ -7\\
\end{pmatrix}=\begin{pmatrix}
    5 \\ 0 \\ -3 \\ 4 \\ 5
\end{pmatrix}$$

$$y_3=v_3-v_0=\begin{pmatrix}
    -15\\ -6 \\ 5 \\ -6 \\ -2
\end{pmatrix}-\begin{pmatrix}
    -6\\ -6\\ 1\\ -9\\ -7\\
\end{pmatrix}=\begin{pmatrix}
    -9\\ 0 \\ 4 \\ 3 \\ 5
\end{pmatrix}$$

Thus, we may write a parametric vector equation of the plane $\Xi$:

$$\Xi=v_0+\begin{pmatrix}y_1\\ y_2\\ y_3\end{pmatrix}\begin{pmatrix}t_1 & t_2 & t_3\end{pmatrix}$$

If we also shift the given point $v$ by $v_0$, then our task collapses to finding the distance between this point $y$ and the following subspace $\Omega$:

$$\Omega=\begin{pmatrix}y_1\\ y_2\\ y_3\end{pmatrix}\begin{pmatrix}t_1 & t_2 & t_3\end{pmatrix},\quad y=v-v_0=\begin{pmatrix}
    5\\ 0\\ 0\\ 10\\ 1
\end{pmatrix}-\begin{pmatrix}
    -6\\ -6\\ 1\\ -9\\ -7\\
\end{pmatrix}=\begin{pmatrix}
    11\\ 6\\-1\\19\\8
\end{pmatrix}$$

Now we may simply calculate the distance by finding the absolute value of the orthogonal projection vector and the closest point by finding the projection of the vector $y$ to our subspace. Then, to find the original point, we would shift it back by $v_0$.

> Ah shit, here we go again:

We know that 

$$\text{pr}_Yy=A_Y(A_Y^TA_Y)^{-1}A_Y^Ty$$

and

$$\text{ort}_Yy=y-A_Y(A_Y^TA_Y)^{-1}A_Y^Ty$$

Calculate the coefficient matrix:

$$A_Y=\begin{pmatrix}
    4 & 5 & -9 \\
    7 & 0 & 0\\
    9 & -3 & 4\\
    -5 & 4 & 3\\
    3 & 5 & 5
\end{pmatrix}$$

$$\begin{align*}A_Y(A_Y^TA_Y)^{-1}A_Y^T&=\begin{pmatrix}
    4 & 5 & -9 \\
    7 & 0 & 0\\
    9 & -3 & 4\\
    -5 & 4 & 3\\
    3 & 5 & 5
\end{pmatrix}\left(\begin{pmatrix}
    4 & 7 & 9 & -5 & 3\\
    5 & 0 & -3 & 4 & 5 \\
    -9 & 0 & 4 & 3 & 5\\
\end{pmatrix}\begin{pmatrix}
    4 & 5 & -9 \\
    7 & 0 & 0\\
    9 & -3 & 4\\
    -5 & 4 & 3\\
    3 & 5 & 5
\end{pmatrix}\right)^{-1}\begin{pmatrix}
    4 & 7 & 9 & -5 & 3\\
    5 & 0 & -3 & 4 & 5 \\
    -9 & 0 & 4 & 3 & 5\\
\end{pmatrix}\\
&=\begin{pmatrix}
    4 & 5 & -9 \\
    7 & 0 & 0\\
    9 & -3 & 4\\
    -5 & 4 & 3\\
    3 & 5 & 5
\end{pmatrix}\begin{pmatrix}
    180 & -12 & 72\\
    -12 & 75 & 70\\
    0 & -20 & -31
\end{pmatrix}^{-1}\begin{pmatrix}
    4 & 7 & 9 & -5 & 3\\
    5 & 0 & -3 & 4 & 5 \\
    -9 & 0 & 4 & 3 & 5\\
\end{pmatrix}\\
&=\frac{1}{144756}\begin{pmatrix}
    4 & 5 & -9 \\
    7 & 0 & 0\\
    9 & -3 & 4\\
    -5 & 4 & 3\\
    3 & 5 & 5
\end{pmatrix}\begin{pmatrix}
    925 & 1812 & 6240\\
    372 & 5580 & 13464\\
    -240 & -3600 & -13356
\end{pmatrix}\begin{pmatrix}
    4 & 7 & 9 & -5 & 3\\
    5 & 0 & -3 & 4 & 5 \\
    -9 & 0 & 4 & 3 & 5\\
\end{pmatrix}\\
&=\frac{1}{144756}\begin{pmatrix}
    3400 & 2748 & -27924 \\
    6475 & 12684 & 43680\\
    6249 & -14832 & -37656\\
    -3857 & 2460 & -17412\\
    3435 & 15336 & 19260
\end{pmatrix}\begin{pmatrix}
    4 & 7 & 9 & -5 & 3\\
    5 & 0 & -3 & 4 & 5 \\
    -9 & 0 & 4 & 3 & 5\\
\end{pmatrix}\\
&=\frac{1}{144756}\begin{pmatrix}
    278656 & 23800 & -89340 & -89780 & -115680\\
    -303800 & 45325 & 194943 & 149401 & 301245\\
    289740 & 43743 & -49887 & -203541 & -243693\\
    153520 & -26999 & -111741 & -23111 & 86331\\
    -82920 & 24045 & 61947 & 101949 & 183285
\end{pmatrix}\\
\end{align*}$$

Finally get the resulting vector:

$$\frac{1}{144756}\begin{pmatrix}
    278656 & 23800 & -89340 & -89780 & -115680\\
    -303800 & 45325 & 194943 & 149401 & 301245\\
    289740 & 43743 & -49887 & -203541 & -243693\\
    153520 & -26999 & -111741 & -23111 & 86331\\
    -82920 & 24045 & 61947 & 101949 & 183285
\end{pmatrix}\begin{pmatrix}
    11\\ 6\\-1\\19\\8
\end{pmatrix}=\frac{1}{144756}\begin{pmatrix}
    666096\\ 1983786\\ -2317338\\1890006\\2573514
    \end{pmatrix}$$

And to get the coordinates of the closest point, shift it back by $v_0$:

$$\frac{1}{144756}\begin{pmatrix}
    666096\\ 1983786\\ -2317338\\1890006\\2573514
    \end{pmatrix}+\begin{pmatrix}
    -6\\ -6\\ 1\\ -9\\ -7\\
\end{pmatrix}=\frac{1}{144756}\begin{pmatrix}
    -202440\\
    1115250\\
    -2172582\\
    587202\\
    1560222
\end{pmatrix}=\frac{1}{24126}\begin{pmatrix}
    -33740\\
    185875\\
    -362097\\
    97867\\
    260037
\end{pmatrix}$$

Now get the orthogonal projection: 

$$\begin{pmatrix}
    5\\ 0\\ 0\\ 10\\ 1
\end{pmatrix}-\frac{1}{24126}\begin{pmatrix}
    -33740\\
    185875\\
    -362097\\
    97867\\
    260037
\end{pmatrix}=\frac{1}{24126}\begin{pmatrix}
    154370\\
    -185875\\
    362097\\
    143393\\
    -235911
\end{pmatrix}$$

and the length of this vector would be 

$$\frac{\sqrt{154370^2+185875^2+362097^2+143393^2+235911^2}}{24126}=\frac{4}{12063}\sqrt{4151709411}$$

    excuse the fuck
    \frac{1}{144756}
        {{278656 , 23800 , -89340 , -89780 , -115680},
        {-303800 , 45325 , 194943 , 149401 , 301245},
        {289740 , 43743 , -49887 , -203541 , -243693},
        {153520 , -26999 , -111741 , -23111 , 86331},
        {-82920 , 24045 , 61947 , 101949 , 183285}}
        {{925 , 1812 , 6240},
        {372 , 5580 , 13464},
        {-240 , -3600 , -13356}}
    {{4,7,9,-5,3},{5,0,-3,4,5},{-9,0,4,3,5}}
    {{4,5,9},{7,0,0},{9,-3,4},{-5,4,3},{3,5,5}}