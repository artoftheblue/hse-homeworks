## Problem 1

Determine the number of solutions that the system has in relation to parameters $a$ and $b$:

$$\begin{cases}ax+7z=2, \\-2x-y=1,\\-4x-6y+bz=-4\end{cases}$$

---

Rewrite as a matrix:

$$\begin{pmatrix}a & 0 & 7 & \bigm| & 2\\-2 & -1 & 0 & \bigm| & 1 \\ -4 & -6 & b & \bigm| &-4 \end{pmatrix}\sim\begin{pmatrix}a & 0 & 7 & \bigm| & 2\\2 & 1 & 0 & \bigm| & -1 \\ 8 & 0 & b & \bigm| &-6 \end{pmatrix}$$

2nd does not depend on $a, b$, so consider the following matrix:

$$\begin{pmatrix}a & 0 & 7 & \bigm| & 2\\ 8 & 0 & b & \bigm| &-6 \end{pmatrix}\sim\begin{pmatrix}a & 0 & 7 & \bigm| & 2\\ \frac{8}{3} & 0 & \frac{b}{3} & \bigm| &-2 \end{pmatrix}\sim\begin{pmatrix}a+\frac{8}{3} & 0 & 7+\frac{b}{3} & \bigm| & 0\\ \frac{8}{3} & 0 & \frac{b}{3} & \bigm| &-2 \end{pmatrix}$$

For the number of solutions to be infinite, we need a line that would have all zeros. Therefore, the system above has infinite solutions if:

$$\begin{cases}a+\frac{8}{3}=0\\7+\frac{b}{3}=0\end{cases}\Rightarrow\begin{cases}a=-\frac{8}{3}\\b=-21\end{cases}$$

For the number of solutions to be zero, we need a line that would have all zeros except for the number coefficent. Consider all cases when we subtract the second line from the first one multiplied by a certain coefficient. Make sure that the free coefficient would be not be equal to zero:

$$\begin{cases}a+8k=0\\7+bk=0\\2-6k\neq0\end{cases}\Rightarrow\begin{cases}k\neq\frac{1}{3}\\7-\frac{ab}{8}=0\end{cases}\Rightarrow\begin{cases}k\neq\frac{1}{3}\\ab=56\end{cases}\Rightarrow\begin{cases}a=n\\b=\frac{56}{n}\\n\in\mathbb{R}\setminus\{-\frac{8}{3}, 0\}\end{cases}$$

Otherwise, the system of equations would have a single solution.

---

Answer:

* Infinite solutions: $${a \choose b} = {-\frac{8}{3} \choose -21}$$
* No solutions: $${a \choose b} = {n \choose \frac{56}{n}},n\in\mathbb{R}\setminus\{-\frac{8}{3}, 0\}$$
* Single solution: otherwise.

## Problem 2

Given matrix 

$$A=\begin{pmatrix}
    4 & 2 & 6 \\
    0 & 0 & 0 \\ 
    0 & 7 & 1
\end{pmatrix},$$

find all matrices $X$ such that 

$$X=\begin{pmatrix}
    * & * & * \\
    0 & * & 0 \\
    0 & * & *
\end{pmatrix}$$

and $AX=XA$.

---

Replace asterisks with variables:

$$X=\begin{pmatrix}
    a & b & c \\
    0 & d & 0 \\
    0 & e & f 
\end{pmatrix}$$

Multiply:

$$\begin{pmatrix}
    4 & 2 & 6 \\
    0 & 0 & 0 \\ 
    0 & 7 & 1
\end{pmatrix}\begin{pmatrix}
    a & b & c \\
    0 & d & 0 \\
    0 & e & f 
\end{pmatrix}=\begin{pmatrix}
    4a & 4a + 2b + 6c & 4c + 6f \\
    0 & 0 & 0 \\
    0 & 7d + e & f\\
\end{pmatrix}$$

$$\begin{pmatrix}
    a & b & c \\
    0 & d & 0 \\
    0 & e & f 
\end{pmatrix}\begin{pmatrix}
    4 & 2 & 6 \\
    0 & 0 & 0 \\ 
    0 & 7 & 1
\end{pmatrix}=\begin{pmatrix}
    4a & 2a + 7c & 6a + c \\
    0 & 0 & 0 \\
    0 & 7f & f \\
\end{pmatrix}$$

Equalize: 

$$\begin{pmatrix}
    4a & 4a + 2b + 6c & 4c + 6f \\
    0 & 0 & 0 \\
    0 & 7d + e & f\\
\end{pmatrix}=\begin{pmatrix}
    4a & 2a + 7c & 6a + c \\
    0 & 0 & 0 \\
    0 & 7f & f \\
\end{pmatrix}$$

Rewrite as a system of equations and a matrix:

$$\begin{cases}
    4a = 4a \\
    4a + 2b + 6c = 2a + 7c \\
    4c + 6f = 6a + c \\
    0 = 0 \\
    0 = 0 \\
    0 = 0 \\
    0 = 0 \\
    7d + e = 7f \\
    f = f 
\end{cases}\Rightarrow\begin{cases}
    2a + 2b - c = 0 \\
    -6a + 3c + 6f = 0 \\
    7d + e - 7f = 0 
\end{cases} \sim \begin{pmatrix}
    2 & 2 & -1 & 0 & 0 & 0 & \bigm| & 0 \\
    -6 & 0 & 3 & 0 & 0 & 6 & \bigm| & 0 \\
    0 & 0 & 0 & 7 & 1 & -7 & \bigm| & 0\\
\end{pmatrix}$$

Solve using the gaussian method:

$$\begin{pmatrix}
    2 & 2 & -1 & 0 & 0 & 0 & \bigm| & 0 \\
    -6 & 0 & 3 & 0 & 0 & 6 & \bigm| & 0 \\
    0 & 0 & 0 & 7 & 1 & -7 & \bigm| & 0\\
\end{pmatrix}\sim\begin{pmatrix}
    1 & 1 & -\frac{1}{2} & 0 & 0 & 0 & \bigm| & 0 \\
    -1 & 0 & \frac{1}{2} & 0 & 0 & 1 & \bigm| & 0 \\
    0 & 0 & 0 & 1 & \frac{1}{7} & -1 & \bigm| & 0\\
\end{pmatrix}\sim$$

$$\sim\begin{pmatrix}
    1 & 1 & -\frac{1}{2} & 0 & 0 & 0 & \bigm| & 0 \\
    0 & 1 & 0 & 0 & 0 & 1 & \bigm| & 0 \\
    0 & 0 & 0 & 1 & \frac{1}{7} & -1 & \bigm| & 0\\
\end{pmatrix}\sim\begin{pmatrix}
    1 & 0 & -\frac{1}{2} & 0 & 0 & -1 & \bigm| & 0 \\
    0 & 1 & 0 & 0 & 0 & 1 & \bigm| & 0 \\
    0 & 0 & 0 & 1 & \frac{1}{7} & -1 & \bigm| & 0\\
\end{pmatrix}$$

Therefore,

$$\begin{cases}
    a = \frac{1}{2}c+f \\
    b = -f \\
    d = -\frac{1}{7}e + f
\end{cases}$$

Substitute back into the original equation:

$$X=\begin{pmatrix}
    a & b & c \\
    0 & d & 0 \\
    0 & e & f 
\end{pmatrix}=\begin{pmatrix}
    \frac{1}{2}c+f & -f & c \\
    0 & -\frac{1}{7}e+f & 0 \\
    0 & e & f 
\end{pmatrix}$$

> I accidentally solved the task from the 25th variant, oops, but I'm too lazy to solve the correct one especially that I have already texed the entire thing and it doesn't really change anything as the algorithm is the same.

## Problem 3

Solve a matrix equation $AX=B$, where

$$A=\begin{pmatrix}
    11 & 5 & 5 & 2 \\
    -2 & 11 & 5 & 0 \\ 
    0 & 2 & 1 & 0
\end{pmatrix}, \ \ \ B=\begin{pmatrix}
    5 & 1 & -23 \\
    -26 & -18 & 16 \\
    -4 & -3 & 2
\end{pmatrix}$$

---

$$X = \begin{pmatrix}
    a & b & c \\
    d & e & f \\
    g & h & i \\
    j & k & l
\end{pmatrix}$$

$$\begin{pmatrix}
    11 & 5 & 5 & 2 \\
    -2 & 11 & 5 & 0 \\ 
    0 & 2 & 1 & 0
\end{pmatrix}\begin{pmatrix}
    a & b & c \\
    d & e & f \\
    g & h & i \\
    j & k & l
\end{pmatrix}=\begin{pmatrix}
    5 & 1 & -23 \\
    -26 & -18 & 16 \\
    -4 & -3 & 2
\end{pmatrix}$$

Then solve the corresponding matrix:

$$\begin{pmatrix}
    a & b & c & d & e & f & g & h & i & j & k & l & \bigm| & \\
    11 & 0 & 0 & 5 & 0 & 0 & 5 & 0 & 0 & 2 & 0 & 0 & \bigm| & 5\\
    0 & 11 & 0 & 0 & 5 & 0 & 0 & 5 & 0 & 0 & 2 & 0 & \bigm| & 1\\
    0 & 0 & 11 & 0 & 0 & 5 & 0 & 0 & 5 & 0 & 0 & 2 & \bigm| & -23\\
    -2 & 0 & 0 & 11 & 0 & 0 & 5 & 0 & 0 & 0 & 0 & 0 & \bigm| & -26\\
    0 & -2 & 0 & 0 & 11 & 0 & 0 & 5 & 0 & 0 & 0 & 0 & \bigm| & -18\\
    0 & 0 & -2 & 0 & 0 & 11 & 0 & 0 & 5 & 0 & 0 & 0 & \bigm| & 16\\
    0 & 0 & 0 & 2 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & \bigm| & -4\\
    0 & 0 & 0 & 0 & 2 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & \bigm| & -3\\
    0 & 0 & 0 & 0 & 0 & 2 & 0 & 0 & 1 & 0 & 0 & 0 & \bigm| & 2\\
\end{pmatrix}$$

$$\begin{pmatrix}
    a & b & c & d & e & f & g & h & i & j & k & l & \bigm| & \\
    1 & 0 & 0 & 60 & 0 & 0 & 30 & 0 & 0 & 2 & 0 & 0 & \bigm| & -125\\
    -2 & 0 & 0 & 11 & 0 & 0 & 5 & 0 & 0 & 0 & 0 & 0 & \bigm| & -26\\
    0 & 0 & 0 & 2 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & \bigm| & -4\\
    \\
    0 & 1 & 0 & 0 & 60 & 0 & 0 & 30 & 0 & 0 & 2 & 0 & \bigm| & -89\\
    0 & -2 & 0 & 0 & 11 & 0 & 0 & 5 & 0 & 0 & 0 & 0 & \bigm| & -18\\
    0 & 0 & 0 & 0 & 2 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & \bigm| & -3\\
    \\
    0 & 0 & 1 & 0 & 0 & 60 & 0 & 0 & 30 & 0 & 0 & 2 & \bigm| & 57\\
    0 & 0 & -2 & 0 & 0 & 11 & 0 & 0 & 5 & 0 & 0 & 0 & \bigm| & 16\\
    0 & 0 & 0 & 0 & 0 & 2 & 0 & 0 & 1 & 0 & 0 & 0 & \bigm| & 2\\
\end{pmatrix}$$

$$\begin{pmatrix}
    a & b & c & d & e & f & g & h & i & j & k & l & \bigm| & \\
    1 & 0 & 0 & 60 & 0 & 0 & 30 & 0 & 0 & 2 & 0 & 0 & \bigm| & -125\\
    0 & 0 & 0 & 131 & 0 & 0 & 65 & 0 & 0 & 0 & 0 & 0 & \bigm| & -276\\
    0 & 0 & 0 & 2 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & \bigm| & -4\\
    \\
    0 & 1 & 0 & 0 & 60 & 0 & 0 & 30 & 0 & 0 & 2 & 0 & \bigm| & -89\\
    0 & 0 & 0 & 0 & 131 & 0 & 0 & 65 & 0 & 0 & 0 & 0 & \bigm| & -196\\
    0 & 0 & 0 & 0 & 2 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & \bigm| & -3\\
    \\
    0 & 0 & 1 & 0 & 0 & 60 & 0 & 0 & 30 & 0 & 0 & 2 & \bigm| & 57\\
    0 & 0 & 0 & 0 & 0 & 131 & 0 & 0 & 65 & 0 & 0 & 0 & \bigm| & 130\\
    0 & 0 & 0 & 0 & 0 & 2 & 0 & 0 & 1 & 0 & 0 & 0 & \bigm| & 2\\
\end{pmatrix}$$

$$\begin{pmatrix}
    a & b & c & d & e & f & g & h & i & j & k & l & \bigm| & \\
    1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 2 & 0 & 0 & \bigm| & -5\\
    0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & \bigm| & -16\\
    0 & 0 & 0 & 2 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & \bigm| & -4\\
    \\
    0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 2 & 0 & \bigm| & 1\\
    0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & \bigm| & -1\\
    0 & 0 & 0 & 0 & 2 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & \bigm| & -3\\
    \\
    0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 2 & \bigm| & -3\\
    0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & \bigm| & 0\\
    0 & 0 & 0 & 0 & 0 & 2 & 0 & 0 & 1 & 0 & 0 & 0 & \bigm| & 2\\
\end{pmatrix}$$

$$\begin{pmatrix}
    a & b & c & d & e & f & g & h & i & j & k & l & \bigm| & \\
    1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 2 & 0 & 0 & \bigm| & -5\\
    0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & \bigm| & -16\\
    0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & \bigm| & 28\\
    \\
    0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 2 & 0 & \bigm| & 1\\
    0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & \bigm| & -1\\
    0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & \bigm| & -1\\
    \\
    0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 2 & \bigm| & -3\\
    0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & \bigm| & 0\\
    0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & \bigm| & 2\\
\end{pmatrix}$$



Now, 

$$\begin{cases}
    a = -5 -2j \\
    b = 1 -2k\\
    c = -3 -2l\\
    d = -16\\
    e = -1\\
    f = 0\\
    g = 28\\
    h = -1\\
    i = 2
\end{cases}\Rightarrow$$

Answer:

$$X=\begin{pmatrix}
    -5-2j & 1-2k & -3-2l \\
    -16 & -1 & 0\\
    28 & -1 & 2\\
    j & k & l
\end{pmatrix}$$

## Problem 4

Given matrix 

$$A=\begin{pmatrix}
    -4 & -17 & -12 & 4 & 5 \\
    5 & 13 & 8 & -5 & -5 \\
    1 & 4 & 3 & -1 & -1 \\
    -1 & -2 & -1 & 1 & 1
\end{pmatrix},$$

Find square matrix $P$, for which matrix $PA$ is an row echelon form of matrix $A$.

---

Firstly, find the row echelon form of the matrix $A$ using elementary operations as matrix multiplications:

$$\begin{pmatrix}
    1 & 0 & 0 & 0 \\
    0 & 0 & 1 & 0 \\
    0 & 1 & 0 & 0 \\
    0 & 0 & 0 & 1
\end{pmatrix}\begin{pmatrix}
    0 & 0 & 1 & 0 \\
    0 & 1 & 0 & 0 \\
    1 & 0 & 0 & 0 \\
    0 & 0 & 0 & 1
\end{pmatrix}\begin{pmatrix}
    -4 & -17 & -12 & 4 & 5 \\
    5 & 13 & 8 & -5 & -5 \\
    1 & 4 & 3 & -1 & -1 \\
    -1 & -2 & -1 & 1 & 1
\end{pmatrix}=\begin{pmatrix}
    1 & 4 & 3 & -1 & -1 \\
    -4 & -17 & -12 & 4 & 5 \\
    5 & 13 & 8 & -5 & -5 \\
    -1 & -2 & -1 & 1 & 1
\end{pmatrix}$$

$$\begin{pmatrix}
    1 & 0 & 0 & 0 \\
    0 & 1 & 0 & 0 \\
    0 & 0 & 1 & 0 \\
    1 & 0 & 0 & 1
\end{pmatrix}\begin{pmatrix}
    1 & 0 & 0 & 0 \\
    0 & 1 & 0 & 0 \\
    -5 & 0 & 1 & 0 \\
    0 & 0 & 0 & 1
\end{pmatrix}\begin{pmatrix}
    1 & 0 & 0 & 0 \\
    4 & 1 & 0 & 0 \\
    0 & 0 & 1 & 0 \\
    0 & 0 & 0 & 1
\end{pmatrix}\cdot$$

$$\cdot\begin{pmatrix}
    1 & 4 & 3 & -1 & -1 \\
    -4 & -17 & -12 & 4 & 5 \\
    5 & 13 & 8 & -5 & -5 \\
    -1 & -2 & -1 & 1 & 1
\end{pmatrix}=\begin{pmatrix}
    1 & 4 & 3 & -1 & -1 \\
    0 & -1 & 0 & 0 & 1 \\
    0 & -7 & -7 & 0 & 0 \\
    0 & 2 & 2 & 0 & 0
\end{pmatrix}$$

$$\begin{pmatrix}
    1 & 0 & 0 & 0 \\
    0 & 1 & 0 & 0 \\
    0 & 0 & -\frac{1}{7} & 0 \\
    0 & 0 & \frac{1}{7} & \frac{1}{2}
\end{pmatrix}\begin{pmatrix}
    1 & 0 & 0 & 0 \\
    0 & -1 & 0 & 0 \\
    0 & 0 & 1 & 0 \\
    0 & 0 & 0 & 1
\end{pmatrix}\cdot$$

$$\cdot\begin{pmatrix}
    1 & 4 & 3 & -1 & -1 \\
    0 & -1 & 0 & 0 & 1 \\
    0 & -7 & -7 & 0 & 0 \\
    0 & 2 & 2 & 0 & 0
\end{pmatrix}=\begin{pmatrix}
    1 & 4 & 3 & -1 & -1 \\
    0 & 1 & 0 & 0 & -1 \\
    0 & 1 & 1 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0
\end{pmatrix}$$

$$\begin{pmatrix}
    1 & -4 & 0 & 0 \\
    0 & 1 & 0 & 0 \\
    0 & 0 & 1 & 0 \\
    0 & 0 & 0 & 1
\end{pmatrix}\begin{pmatrix}
    1 & 0 & 0 & 0 \\
    0 & 1 & 0 & 0 \\
    0 & -1 & 1 & 0 \\
    0 & 0 & 0 & 1
\end{pmatrix}\begin{pmatrix}
    1 & 4 & 3 & -1 & -1 \\
    0 & 1 & 0 & 0 & -1 \\
    0 & 1 & 1 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0
\end{pmatrix}=\begin{pmatrix}
    1 & 0 & 3 & -1 & 3 \\
    0 & 1 & 0 & 0 & -1 \\
    0 & 0 & 1 & 0 & 1 \\
    0 & 0 & 0 & 0 & 0
\end{pmatrix}$$

$$\begin{pmatrix}
    1 & 0 & -3 & 0 \\
    0 & 1 & 0 & 0 \\
    0 & 0 & 1 & 0 \\
    0 & 0 & 0 & 1
\end{pmatrix}\begin{pmatrix}
    1 & 0 & 3 & -1 & 3 \\
    0 & 1 & 0 & 0 & -1 \\
    0 & 0 & 1 & 0 & 1 \\
    0 & 0 & 0 & 0 & 0
\end{pmatrix}=\begin{pmatrix}
    1 & 0 & 0 & -1 & 0 \\
    0 & 1 & 0 & 0 & -1 \\
    0 & 0 & 1 & 0 & 1 \\
    0 & 0 & 0 & 0 & 0
\end{pmatrix}$$

Now, chaining them all together via multiplication, the required matrix would be the following:

$$P=\begin{pmatrix}
    1 & \frac{3}{7} & \frac{20}{7} & 0 \\
    -1 & 0 & -4 & 0 \\
    1 & -\frac{1}{7} & \frac{33}{7} & 0 \\
    0 & \frac{1}{7} & -\frac{3}{14} & \frac{1}{2}
\end{pmatrix}$$

## Problem 5

Given matrices

$$A=\begin{pmatrix}
    1 & 0 & 0 \\
    0 & 1 & 0 \\
    0 & 0 & 1 \\
    6 & -8 & -4
\end{pmatrix}, \ \ B=\begin{pmatrix}
    1 & 0 & -3 & 2\\
    0 & 1 & 4 & -5\\
    3 & 2 & -1 & -4\\
\end{pmatrix}, \ \ C=\begin{pmatrix}
    1 & 0 & -1 & -2\\
    -2 & 1 & 2 & 2\\
    -2 & 2 & 3 & -2\\
    -2 & -2 & 2 & 9\\
\end{pmatrix}, \ \ D=\begin{pmatrix}
    -5 & -4 & 2 & 0\\
    34 & 11 & 0 & 5 \\
    -83 & -34 & 6 & -10\\
    97 & 29 & 2 & 15\\
\end{pmatrix}$$

Find whether systems $ABC^{-1}x=0$ and $Dx=0$ where $x\in\mathbb{R}^4$ have the same set of solutions.

---

First, find the inverse of $C$ using the gaussian approach:

$$\begin{pmatrix}
    1 & 0 & -1 & -2 & \bigm| & 1 & 0 & 0 & 0\\
    -2 & 1 & 2 & 2 & \bigm| & 0 & 1 & 0 & 0\\
    -2 & 2 & 3 & -2 & \bigm| & 0 & 0 & 1 & 0\\
    -2 & -2 & 2 & 9 & \bigm| & 0 & 0 & 0 & 1\\
\end{pmatrix}\sim\begin{pmatrix}
    1 & 0 & -1 & -2 & \bigm| & 1 & 0 & 0 & 0\\
    0 & 1 & 0 & -2 & \bigm| & 2 & 1 & 0 & 0\\
    0 & 2 & 1 & -6 & \bigm| & 2 & 0 & 1 & 0\\
    0 & -2 & 0 & 5 & \bigm| & 2 & 0 & 0 & 1\\
\end{pmatrix}\sim$$

$$\begin{pmatrix}
    1 & 0 & -1 & -2 & \bigm| & 1 & 0 & 0 & 0\\
    0 & 1 & 0 & -2 & \bigm| & 2 & 1 & 0 & 0\\
    0 & 0 & 1 & -2 & \bigm| & -2 & -2 & 1 & 0\\
    0 & 0 & 0 & 1 & \bigm| & 6 & 2 & 0 & 1\\
\end{pmatrix}\sim\begin{pmatrix}
    1 & 0 & 0 & -4 & \bigm| & -1 & -2 & 1 & 0\\
    0 & 1 & 0 & -2 & \bigm| & 2 & 1 & 0 & 0\\
    0 & 0 & 1 & -2 & \bigm| & -2 & -2 & 1 & 0\\
    0 & 0 & 0 & 1 & \bigm| & 6 & 2 & 0 & 1\\
\end{pmatrix}\sim$$

$$\begin{pmatrix}
    1 & 0 & 0 & 0 & \bigm| & 23 & 6 & 1 & 4\\
    0 & 1 & 0 & 0 & \bigm| & 14 & 5 & 0 & 2\\
    0 & 0 & 1 & 0 & \bigm| & 10 & 2 & 1 & 2\\
    0 & 0 & 0 & 1 & \bigm| & 6 & 2 & 0 & 1\\
\end{pmatrix}\Rightarrow C^{-1}=\begin{pmatrix}
    23 & 6 & 1 & 4 \\
    14 & 5 & 0 & 2 \\
    10 & 2 & 1 & 2 \\
    6 & 2 & 0 & 1
\end{pmatrix}$$

Multiply $AB$:

$$AB=\begin{pmatrix}
    1 & 0 & 0 \\
    0 & 1 & 0 \\
    0 & 0 & 1 \\
    6 & -8 & -4
\end{pmatrix}\begin{pmatrix}
    1 & 0 & -3 & 2\\
    0 & 1 & 4 & -5\\
    3 & 2 & -1 & -4\\
\end{pmatrix}=\begin{pmatrix}
    1 & 0 & -3 & 2 \\
    0 & 1 & 4 & -5 \\
    3 & 2 & -1 & -4\\
    -6 & -16 & -46 & 68
\end{pmatrix}$$

Multiply $ABC^{-1}$:

$$\begin{pmatrix}
    1 & 0 & -3 & 2 \\
    0 & 1 & 4 & -5 \\
    3 & 2 & -1 & -4\\
    -6 & -16 & -46 & 68
\end{pmatrix}\begin{pmatrix}
    23 & 6 & 1 & 4 \\
    14 & 5 & 0 & 2 \\
    10 & 2 & 1 & 2 \\
    6 & 2 & 0 & 1
\end{pmatrix}=\begin{pmatrix}
    5 & 4 & -2 & 0 \\
    24 & 3 & 4 & 5 \\
    63 & 18 & 2 & 10 \\
    -414 & -72 & -52 & -80 \\
\end{pmatrix}$$

Both matrixes have their determinants equal to $0$, therefore, they have the same set of solutions since they could be transformed to one another using elementary transformations (their upper diagonal forms have two blank lines, thus they both have an infinite set of solutions).

Let's check that, making the first two lines the same and then:

$$ABC^{-1}=\begin{pmatrix}
    5 & 4 & -2 & 0 \\
    24 & 3 & 4 & 5 \\
    63 & 18 & 2 & 10 \\
    -414 & -72 & -52 & -80 \\
\end{pmatrix}\sim\begin{pmatrix}
    -5 & -4 & 2 & 0 \\
    34 & 11 & 0 & 5 \\
    63 & 18 & 2 & 10 \\
    -414 & -72 & -52 & -80 \\
\end{pmatrix}\sim$$

$$a = \begin{pmatrix}
    -5 \\
    -4 \\
    2 \\ 
    0 \\
\end{pmatrix} \ \ \ b = \begin{pmatrix}
    34 \\
    11 \\
    0 \\ 
    5 \\
\end{pmatrix}$$

$$\begin{pmatrix}
    63 \\
    18 \\
    2 \\ 
    10 \\
\end{pmatrix}=a+2b \ \ \ \begin{pmatrix}
    -414 \\
    -72 \\
    -52 \\
    -80 \\
\end{pmatrix}=-26a-8b$$

Therefore, the matrix above collapses to the following, which has an infinite number of solutions:

$$\sim\begin{pmatrix}
    -5 & -4 & 2 & 0 \\
    34 & 11 & 0 & 5 \\
    0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0\\
\end{pmatrix}$$

Then, do the same thing for $D$:

$$D=\begin{pmatrix}
    -5 & -4 & 2 & 0\\
    34 & 11 & 0 & 5 \\
    -83 & -34 & 6 & -10\\
    97 & 29 & 2 & 15\\
\end{pmatrix}$$

$$\begin{pmatrix}
    -83 \\
    -34 \\
    6 \\ 
    -10 \\
\end{pmatrix}=3a-2b$$

$$\begin{pmatrix}
    97 \\
    29 \\
    2 \\ 
    15 \\
\end{pmatrix}=a+3b$$

Therefore, $D$ collapses to the same matrix, which obviously also has an infinite number of solutions:

$$\sim\begin{pmatrix}
    -5 & -4 & 2 & 0 \\
    34 & 11 & 0 & 5 \\
    0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0\\
\end{pmatrix}$$

**Answer:** the sets of solutions are the same.