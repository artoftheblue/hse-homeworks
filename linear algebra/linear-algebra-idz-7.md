# Linear Algebra, Individual Homework 7

## Problem 1

Find the normalized form and some non-singular coordinate replacement for the following quadratic form over $\mathbb{R}$:

$$Q(x_1,x_2,x_3)=-81x_1^2-29x_2^2-101x_3^2-36x_1x_2+162x_1x_3+76x_2x_3$$

---

Corresponding matrix of the quadratic form is 

$$\begin{pmatrix}
    -81 & -\frac{36}{2} & \frac{162}{2}\\
    -\frac{36}{2} & -29 & \frac{76}{2}\\
    \frac{162}{2} & \frac{76}{2} & -101
\end{pmatrix}=\begin{pmatrix}
    -81 & -18 & 81\\
    -18 & -29 & 38\\
    81 & 38 & -101
\end{pmatrix}$$

Now use symmetric Gauss' method to find the normalized form:

$$\begin{pmatrix}
    -81 & -18 & 81\\
    -18 & -29 & 38\\
    81 & 38 & -101
\end{pmatrix}\xRightarrow{(3):=(3)+1\times(1)}\begin{pmatrix}
    -81 & -18 & 0\\
    -18 & -29 & 20\\
    0 & 20 & 20
\end{pmatrix}\xRightarrow{(2):=(2)-\frac{2}{9}\times(1)}$$

$$\begin{pmatrix}
    -81 & 0 & 0\\
    0 & -25 & 20\\
    0 & 20 & -20
\end{pmatrix}\xRightarrow{(3):=(3)+\frac{4}{5}\times(2)}\begin{pmatrix}
    -81 & 0 & 0\\
    0 & -25 & 0\\
    0 & 0 & -4
\end{pmatrix}$$

Since we have tracked all the transformations, we may get the following transformation matrix:

$$\begin{pmatrix}
    1 & \frac{2}{9} & -1\\
    0 & 1 & -\frac{4}{5}\\
    0 & 0 & 1
\end{pmatrix}$$

which corresponds to the following replacement:

$$\begin{cases}
    y_1'=(x_1+\frac{2}{9}x_2-x_3)\\
    y_2'=(x_2-\frac{4}{5}x_3)\\
    y_3'=x_3
\end{cases}$$

and we get the form:

$$Q(y_1,y_2,y_3)=-81y_1'^2-25y_2'^2-4y_3'^2$$

Introduce a replacement

$$\begin{cases}
    y_1=9y'_1\\
    y_2=5y'_2\\
    y_3=6y'_3
\end{cases}\implies\begin{cases}
    y_1=9(x_1+\frac{2}{9}x_2-x_3)\\
    y_2=5(x_2-\frac{4}{5}x_3)\\
    y_3=6x_3
\end{cases}$$

This means that the normalized form would be 

$$-y_1^2-y_2^2-y_3^2$$

and the replacement is

$$\begin{cases}
    y_1=9(x_1+\frac{2}{9}x_2-x_3)\\
    y_2=5(x_2-\frac{4}{5}x_3)\\
    y_3=2x_3
\end{cases}\implies\begin{cases}
    x_1=\frac{y_1}{9}- \frac{2 y_{2}}{45} +\frac{37 y_{3}}{90}\\
    x_2=\frac{y_2}{5}+\frac{2y_3}{5}\\
    x_3=\frac{y_3}{2}
\end{cases}$$


## Problem 2

Determine the normalized form of the quadratic form depending on value $b$:

$$Q(x_1,x_2,x_3)=-9x_1^2+(-7b+4)x_2^2+(-7b-7)x_3^2-18x_1x_2+14x_1x_3+2(7b-1)x_2x_3$$

---

Firstly, use symmetric Gauss to arrive at some canonized form:

$$\begin{pmatrix}
    -9 & -9 & 7\\
    -9 & -7b + 4 & 7b-1\\
    7 & 7b-1 & -7b-7
\end{pmatrix}\xRightarrow{(2):=(2)-1\times(1)}\begin{pmatrix}
    -9 & 0 & 7\\
    0 & -7b + 13 & 7b-8\\
    7 & 7b-8 & -7b-7
\end{pmatrix}$$

$$\xRightarrow{(3):=(3)+\frac{7}{9}\times(1)}\begin{pmatrix}
    -9 & 0 & 0\\
    0 & -7b + 13 & 7b-8\\
    0 & 7b-8 & -7b-\frac{14}{9}
\end{pmatrix}\xRightarrow{(3):=(3)+1\times(2)}$$

$$\begin{pmatrix}
    -9 & 0 & 0\\
    0 & -7b + 13 & 5\\
    0 & 5 & -\frac{41}{9}
\end{pmatrix}\xRightarrow{(2):=(2)+\frac{45}{41}\times(3)}\begin{pmatrix}
    -9 & 0 & 0\\
    0 & -7b + \frac{758}{41} & 0\\
    0 & 0 & -\frac{41}{9}
\end{pmatrix}$$

Thus, the canonized quadratic form currently looks like

$$-9y_1'^2+\left(-7b+\frac{758}{41}\right)y_2'^2-\frac{41}{9}y_3'^2$$

We can easily normalize the first two coefficients to be $-1$, so the normalized form depends only on the second coefficient. Thus, the form would have normalized forms of 

$$-y_1^2+y_2^2-y_3^2,\quad  b < \frac{758}{287}$$

$$-y_1^2-y_3^2,\quad  b = \frac{758}{287}$$

$$-y_1^2-y_2^2-y_3^2,\quad  b > \frac{758}{287}$$

## Problem 3

In vector space $V=\mathbb{R}[x]_{\leq3}$ consider a function 

$$Q(f)=\int\limits^1_{-1}f^2dx-\int\limits^2_0f^2dx$$

### Subproblem A

Prove that $Q$ is a quadratic form in $V$.

---

First, write out the intergral using the Newton-Leibnitz formula for some $f=ax^3+bx^2+cx+d$:

$$Q(f)=\int^1_{-1}(ax^3+bx^2+cx+d)^2dx-\int^2_0(ax^3+bx^2+cx+d)^2dx=$$

$$\int(ax^3+bx^2+cx+d)^2dx=\\=\frac{a^2 x^7}{7} +  \frac{x^5 (2 a c + b^2)}{5} + \frac{x^4 (a d + b c)}{2} + \frac{a b x^6}{3} + \frac{x^3 (2 b d + c^2)}{3} + c d x^2 + d^2 x$$
Now calculate all this garbage:

$$f(1)= \frac{a^{2}}{7} + \frac{a b}{3} + \frac{2 a c}{5} + \frac{a d}{2} + \frac{b^{2}}{5} + \frac{b c}{2} + \frac{2 b d}{3} + \frac{c^{2}}{3} + c d + d^{2}$$

$$f(-1)=-\frac{a^{2}}{7} + \frac{a b}{3} - \frac{2 a c}{5} + \frac{a d}{2} - \frac{b^{2}}{5} + \frac{b c}{2} - \frac{2 b d}{3} - \frac{c^{2}}{3} + c d - d^{2}$$

$$f(2)=\frac{128 a^{2}}{7} + \frac{64 ab}{3} + \frac{64 ac}{5} + 8 ad + \frac{32 b^{2}}{5} + 8 bc + \frac{16 bd}{3} + \frac{8 c^{2}}{3} + 4 cd + 2 d^{2}$$

$$
f(0)=0
$$

Now, 

$$\begin{align*}
    Q(f)=\ &f(1)-f(-1)-f(2)+f(0)=\\
    &\frac{a^{2}}{7} + \frac{a b}{3} + \frac{2 a c}{5} + \frac{a d}{2} + \frac{b^{2}}{5} + \frac{b c}{2} + \frac{2 b d}{3} + \frac{c^{2}}{3} + c d + d^{2}-\\
    &(-\frac{a^{2}}{7} + \frac{a b}{3} - \frac{2 a c}{5} + \frac{a d}{2} - \frac{b^{2}}{5} + \frac{b c}{2} - \frac{2 b d}{3} - \frac{c^{2}}{3} + c d - d^{2})-\\
    &(\frac{128 a^{2}}{7} + \frac{64 ab}{3} + \frac{64 ac}{5} + 8 ad + \frac{32 b^{2}}{5} + 8 bc + \frac{16 bd}{3} + \frac{8 c^{2}}{3} + 4 cd + 2 d^{2}) \\
    &=-18 a^{2} - \frac{64 a b}{3} - 12 a c - 8 a d - 6 b^{2} - 8 b c - 4 b d - 2 c^{2} - 4 c d
\end{align*}$$

which is a polynomial of mononomials of degree exactly $2$, so this is definitely a quadratic form.

### Subproblem B

Does such a basis $\mathbf{e}=(e_1,\dots,e_4)$ exist that quadratic form $Q$ in coordinates $\mathbf{x}=(x_1,\dots,x_4)$ in this basis has a form of 

$$55x_1^2-58x_1x_2+120x_1x_3+46x_1x_4+20x_2^2-74x_2x_3-14x_2x_4+3x_3^2-10x_3x_4+12x_4^2$$

If this basis exists, present it.

---

Previous form matrix:

$$\begin{pmatrix}
    -18 & -\frac{32}{3} & -6 & -4\\
    -\frac{32}{3} & -6 & -4 & -2\\
    -6 & -4 & -2 & -4\\
    -4 & -2 & -4 & 0
\end{pmatrix}$$

Current form matrix:

$$\begin{pmatrix}
    55 & -29 & 60 & 23\\
    -29 & 20 & -37 & -7\\
    60 & -37 & 3 & -5\\
    23 & -7 & -5 & 12
\end{pmatrix}$$

If their inertia coefficients would be different, then it would prove that it's impossible to find such a basis.

Use Jacobi's approach because it's the fastest one since I can easily force the computer to do it for me. First coefficients:

$$\begin{cases}
    \Delta_1=-18\\
    \Delta_2=- \frac{52}{9}\\
    \Delta_3=\frac{32}{9}\\
    \Delta_4=\frac{256}{9}
\end{cases}$$

which implies that this form has a normalized form of 

$$-x_1^2+x_2^2-x_3^2+x_4^2$$

Second coefficients

$$\begin{cases}
    \Delta_1=55\\
    \Delta_2=259\\
    \Delta_3=-17758\\
    \Delta_4=-95481
\end{cases}$$

which implies that this form has a normalized form of

$$x_1^2+x_2^2-x_3^2+x_4^2$$

> Technically this could have been checked by simply looking at the first coefficient, but alas, I have already forced the computer to suffer.

These normalized forms are different (their inertia coefficients are also different), which means that it's impossible to find such a basis that is wanted from us in the given conditions.

## Problem 4

Determine all values of $a, b$ when bilinear form 

$$\beta(x,y)=(-9b+31)x_1y_1+(3b-9)x_1y_2+(-1.5a+5.5)x_1y_3+(3b-9)x_2y_1+2x_2y_2+\\(2b-4)x_2y_3+(-3b+11)x_3y_1+(2b-4)x_3y_2+3x_3y_3$$

defines a dot product in $\mathbb{R}^3$.

---

For a bilinear form to define a dot product, we need it to be symmetric and positively-defined.

Firstly, let's construct a matrix of this form:

$$\begin{pmatrix}
    -9b+31 & 3b-9 & -1.5a + 5.5\\
    3b-9 & 2 & 2b-4\\
    -3b+11 & 2b-4 & 3
\end{pmatrix}$$

To check when it is symmetric, solve the following system of equations:

$$\begin{cases}
    3b-9 = 3b-9\\
    -3b+11=-1.5a+5.5\\
    2b-4=2b-4
\end{cases}\implies\quad\begin{gathered}
    -3b+11=-1.5a+5.5\implies\\-6b+22=-3a+11\implies3a-6b=-11\implies\\ a=2b-\frac{11}{3}
\end{gathered}$$

Plug this back into the original matrix:

$$\begin{pmatrix}
    -9b+31 & 3b-9 & -3b+11\\
    3b-9 & 2 & 2b-4\\
    -3b+11 & 2b-4 & 3
\end{pmatrix}$$

To check whether it's positively defined, we could use Sylvester's criterion:

$$\begin{cases}
    \Delta_1>0\\
    \Delta_2>0\\
    \Delta_3>0
\end{cases}\implies\begin{cases}
    \begin{vmatrix}
    -9b+31
\end{vmatrix}>0\\
\begin{vmatrix}
    -9b+31 & 3b-9 \\
    3b-9 & 2 \\
\end{vmatrix}>0\\
\begin{vmatrix}
    -9b+31 & 3b-9 & -3b+11\\
    3b-9 & 2 & 2b-4\\
    -3b+11 & 2b-4 & 3
\end{vmatrix}>0
\end{cases}\implies$$

$$\begin{cases}
    31 - 9 b>0\\
    - 9 b^{2} + 36 b - 19>0\\
    - b^{2} + 4 b - 3>0
\end{cases}\implies\begin{cases}
    b < \frac{31}{9}\\
    b\in(2-\frac{\sqrt{17}}{3}, 2+\frac{\sqrt{17}}{3})\\
    b\in(1,3)
\end{cases}\implies b\in(1,3)$$

Thus, all pairs for which this would be a dot product are

$$(a,b)=\left(2b-\frac{11}{3}, b\right), \quad b\in(1,3)$$

## Problem 5

Does a system of three vectors in $\mathbb{R}^3$ exist such that its Graham matrix is equal to 

$$\begin{pmatrix}
    25 & 16 & -82\\
    16 & 18 & -68\\
    -82 & -68 & 300
\end{pmatrix}$$

exist? If it exists, then present such system. The dot product is standard.

---

Graham's matrix for a system of vectors $\langle v_1,v_2,v_3\rangle$ looks like 

$$\begin{pmatrix}
    v_1\cdot v_1 & v_1\cdot v_2 & v_1 \cdot v_3\\
    v_2\cdot v_1 & v_2\cdot v_2 & v_2 \cdot v_3\\
    v_3\cdot v_1 & v_3\cdot v_2 & v_3 \cdot v_3\\
\end{pmatrix}=\begin{pmatrix}
    25 & 16 & -82\\
    16 & 18 & -68\\
    -82 & -68 & 300
\end{pmatrix}$$

Then this would effectively correspond to some kinda quadratic form. 

$$25(v_1\cdot v_1)+32(v_1\cdot v_2)-164(v_1\cdot v_3)+18(v_2\cdot v_2)-136(v_2\cdot v_3)+300(v_3\cdot v_3)$$

Use symmetric Gauss once again, tracking the transformations:

$$\begin{pmatrix}
    25 & 16 & -82\\
    16 & 18 & -68\\
    -82 & -68 & 300
\end{pmatrix}\xRightarrow{(2):=(2)-\frac{16}{25}\times(1)}\begin{pmatrix}
    25 & 0 & -82\\
    0 & \frac{194}{25} & - \frac{388}{25}\\
    -82 & - \frac{388}{25} & 300
\end{pmatrix}\xRightarrow{(3):=(3)+\frac{82}{25}\times(1)}$$

$$\begin{pmatrix}
    25 & 0 & 0\\
    0 & \frac{194}{25} & - \frac{388}{25}\\
    0 & - \frac{388}{25} & \frac{776}{25}
\end{pmatrix}\xRightarrow{(3):=(3)+2\times(2)}\begin{pmatrix}
    25 & 0 & 0\\
    0 & \frac{194}{25} & 0\\
    0 & 0 & 0
\end{pmatrix}$$

Canonized quadratic form:

$$25y_1^2+\frac{194}{25}y_2^2$$

Transformation matrix:

$$C=\begin{pmatrix}
    1 & -\frac{16}{25} & 2\\
    0 & 1 & 2\\
    0 & 0 & 1
\end{pmatrix}$$

We get that this form is positively defined, so it definitely exists. Take its inverse:

$$C^{-1}=\begin{pmatrix}
    1 & \frac{16}{25} & -\frac{82}{25}\\
    0 & 1 & -2\\
    0 & 0 & 1
\end{pmatrix}$$

Now say that we have some vectors $\langle e_1,e_2,e_3\rangle=\langle(5,0,0),(0,\frac{\sqrt{194}}{5},0),(0,0,0)\rangle$

then we could get the required set of vectors by 

$$\langle f_1,f_2,f_3\rangle=\langle(5,0,0),(0,\frac{\sqrt{194}}{5},0),(0,0,0)\rangle\begin{pmatrix}
    1 & -\frac{16}{25} & 2\\
    0 & 1 & 2\\
    0 & 0 & 1
\end{pmatrix}=$$

$$=\langle(5,0,0),\frac{16}{25}(5,0,0)+(0,\frac{\sqrt{194}}{5},0),-\frac{82}{25}(5,0,0)-2(0,\frac{\sqrt{194}}{5},0)\rangle=$$

$$=\left\langle(5,0,0),\left(\frac{16}{5},\frac{\sqrt{194}}{5},0\right),\left(-\frac{82}{5},-\frac{2\sqrt{194}}{5},0\right)\right\rangle$$

