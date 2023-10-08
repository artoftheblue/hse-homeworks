## Individual Homework 1 (variant 20)

### Problem 1

> *Today, my son asked "Can I have a book mark?" and I burst into tears. 11 years old and he still doesn't know my name is Brian.*

Given:

$$A= \begin{pmatrix}
    -5 & 4 & 3 \\ 
    0 & 0 & 6
\end{pmatrix}, \ \ B=\begin{pmatrix}
    -5 & 3 & -4 \\
    -5 & 1 & 7
\end{pmatrix}, \ \ C=\begin{pmatrix}
    4 & 4 \\
    4 & 5
\end{pmatrix}, \ \ D=\begin{pmatrix}
    4 & 0\\
    0 & 9
\end{pmatrix}$$

Calculate:

$$\text{tr}(A^TA)DBB^T+\text{tr}((7BA^T+7AB^T)D+D(-7AB^T+4BA^T))(A+B)(A^T-B^T)-9C^2-18CD-9D^2$$

I shall split this monstrosity into three parts and calculate each one separately (I will omit some partial calculations as otherwise it would take an eternity to tex everything):

#### Part 1

$$\text{tr}(A^TA)DBB^T$$

$$A^T = \begin{pmatrix}
    -5 & 0 \\
    4 & 0 \\ 
    3 & 6 \\
\end{pmatrix}$$

$$A^TA=\begin{pmatrix}
    -5 & 0 \\
    4 & 0 \\ 
    3 & 6 \\
\end{pmatrix}\begin{pmatrix}
    -5 & 4 & 3 \\ 
    0 & 0 & 6
\end{pmatrix}=\begin{pmatrix}
    25 & -20 & -15 \\
    -20 & 16 & 12 \\
    -15 & 12 & 45
\end{pmatrix}$$

$$\text{tr}A^TA= 25+16+45=86$$

$$DB=\begin{pmatrix}
    4 & 0\\
    0 & 9
\end{pmatrix}\begin{pmatrix}
    -5 & 3 & -4 \\
    -5 & 1 & 7
\end{pmatrix}=\begin{pmatrix}
    -20 & 12 & -16 \\
    -45 & 9 & 63
\end{pmatrix}$$

$$B^T=\begin{pmatrix}
    -5 & -5 \\
    3 & 1 \\
    -4 & 7 
\end{pmatrix}$$

$$DBB^T =\begin{pmatrix}
    -20 & 12 & -16 \\
    -45 & 9 & 63
\end{pmatrix}\begin{pmatrix}
    -5 & -5 \\
    3 & 1 \\
    -4 & 7 
\end{pmatrix}=\begin{pmatrix}
    100 + 36 + 64 & 100 + 12 - 112\\
    225 + 27 - 252 & 225 + 9 + 441
\end{pmatrix}=\begin{pmatrix}
    200 & 0 \\
    0 & 675
\end{pmatrix}$$ 

$$\text{tr}(A^TA)DBB^T=86\begin{pmatrix}
    200 & 0 \\
    0 & 675
\end{pmatrix}=\begin{pmatrix}
    17200 & 0 \\
    0 & 58050
\end{pmatrix}$$

<div style="page-break-after: always;"></div>

#### Part 2

$$\text{tr}((7BA^T+7AB^T)D+D(-7AB^T+4BA^T))(A+B)(A^T-B^T)$$

$$BA^T=\begin{pmatrix}
    -5 & 3 & -4 \\
    -5 & 1 & 7
\end{pmatrix}\begin{pmatrix}
    -5 & 0 \\
    4 & 0 \\ 
    3 & 6 \\
\end{pmatrix}=\begin{pmatrix}
    25 & -24 \\
    50 & 42
\end{pmatrix}$$

$$AB^T=(BA^T)^T=\begin{pmatrix}
    25 & 50 \\
    -24 & 42
\end{pmatrix}$$

$$7BA^T+7AB^T=7\left(\begin{pmatrix}
    25 & -24 \\
    50 & 42
\end{pmatrix}+\begin{pmatrix}
    25 & 50 \\
    -24 & 42
\end{pmatrix}\right)=\begin{pmatrix}
    350 & 182 \\
    182 & 588
\end{pmatrix}$$

$$(7BA^T+7AB^T)D=\begin{pmatrix}
    350 & 182 \\
    182 & 588
\end{pmatrix}\begin{pmatrix}
    4 & 0\\
    0 & 9
\end{pmatrix}=\begin{pmatrix}
    1400 & 1638 \\
    728 & 5292
\end{pmatrix}$$

$$-7AB^T=-7\begin{pmatrix}
    25 & 50 \\
    -24 & 42
\end{pmatrix}=\begin{pmatrix}
    -175 & -350 \\
    168 & -294
\end{pmatrix}$$

$$4BA^T=4\begin{pmatrix}
    25 & -24 \\
    50 & 42
\end{pmatrix}=\begin{pmatrix}
    100 & -96 \\
    200 & 168
\end{pmatrix}$$

$$-7AB^T+4BA^T=\begin{pmatrix}
    -75 & -446 \\
    368 & -126
\end{pmatrix}$$

$$D(-7AB^T+4BA^T)=\begin{pmatrix}
    4 & 0\\
    0 & 9
\end{pmatrix}\begin{pmatrix}
    -75 & -446 \\
    368 & -126
\end{pmatrix}=\begin{pmatrix}
    -300 & -1784\\
    3312 & -1134
\end{pmatrix}$$

$$\text{tr}((7BA^T+7AB^T)D+D(-7AB^T+4BA^T))=(1400+5292)+(-300-1134)=5258$$

$$A+B= \begin{pmatrix}
    -5 & 4 & 3 \\ 
    0 & 0 & 6
\end{pmatrix}+\begin{pmatrix}
    -5 & 3 & -4 \\
    -5 & 1 & 7
\end{pmatrix}=\begin{pmatrix}
    -10 & 7 & -1 \\
    -5 & 1 & 13
\end{pmatrix}$$

$$A^T-B^T=\begin{pmatrix}
    -5 & 0 \\
    4 & 0 \\ 
    3 & 6 \\
\end{pmatrix}-\begin{pmatrix}
    -5 & -5 \\
    3 & 1 \\
    -4 & 7 
\end{pmatrix}=\begin{pmatrix}
    0 & -5 \\
    1 & -1 \\ 
    7 & -1
\end{pmatrix}$$

$$(A+B)(A^T-B^T)=\begin{pmatrix}
    -10 & 7 & -1 \\
    -5 & 1 & 13
\end{pmatrix}\begin{pmatrix}
    0 & -5 \\
    1 & -1 \\ 
    7 & -1
\end{pmatrix}=\begin{pmatrix}
    0 & -56\\
    92 & -39
\end{pmatrix}$$

$$\text{tr}((7BA^T+7AB^T)D+D(-7AB^T+4BA^T))(A+B)(A^T-B^T)=5258\begin{pmatrix}
    0 & -56\\
    92 & -39
\end{pmatrix}=\\\begin{pmatrix}
    0 & -294448\\
    483726 & -205062
\end{pmatrix}$$


<div style="page-break-after: always;"></div>

#### Part 3

$$-9C^2-18CD-9D^2$$

$$C^2=\begin{pmatrix}
    4 & 4 \\
    4 & 5
\end{pmatrix}\begin{pmatrix}
    4 & 4 \\
    4 & 5
\end{pmatrix}=\begin{pmatrix}
    32 & 36 \\
    36 & 41
\end{pmatrix}$$

$$CD=\begin{pmatrix}
    4 & 4 \\
    4 & 5
\end{pmatrix}\begin{pmatrix}
    4 & 0\\
    0 & 9
\end{pmatrix}=\begin{pmatrix}
    16 & 36\\
    16 & 45
\end{pmatrix}$$

$$D^2=\begin{pmatrix}
    4 & 0\\
    0 & 9
\end{pmatrix}\begin{pmatrix}
    4 & 0\\
    0 & 9
\end{pmatrix}=\begin{pmatrix}
    16 & 0\\
    0 & 81
\end{pmatrix}$$

$$-9C^2-18CD-9D^2=-9C^2=-9\left(\begin{pmatrix}
    32 & 36 \\
    36 & 41
\end{pmatrix}+\begin{pmatrix}
    32 & 72\\
    32 & 90
\end{pmatrix}+\begin{pmatrix}
    16 & 0\\
    0 & 81
\end{pmatrix}\right)=\\=\begin{pmatrix}
    -720 & -972\\
    -612 & -1908
\end{pmatrix}$$

#### Finale

$$\begin{pmatrix}
    17200 & 0 \\
    0 & 58050
\end{pmatrix}+\begin{pmatrix}
    0 & -294448\\
    483726 & -205062
\end{pmatrix}+\begin{pmatrix}
    -720 & -972\\
    -612 & -1908
\end{pmatrix}=\begin{pmatrix}
    16480 & -295420 \\
    483124 & -148920
\end{pmatrix}$$

<div style="page-break-after: always;"></div>

### Problem 2

> *Two fish in a tank. One says: ‘How do you drive this thing?'*

Find all possible values of $AB$ if 

$$A + B=\begin{pmatrix}
    a_{11} & a_{12} & a_{13} & a_{14}\\
    a_{12} & a_{22} & a_{23} & a_{24}\\
    a_{13} & a_{23} & a_{33} & a_{34}\\
    a_{14} & a_{24} & a_{34} & a_{44}
\end{pmatrix}+\begin{pmatrix}
    0 & b_{12} & b_{13} & b_{14}\\
    -b_{12} & 0 & b_{23} & b_{24}\\
    -b_{13} & -b_{23} & 0 & b_{34}\\
    -b_{14} & -b_{24} & -b_{34} & 0
\end{pmatrix}=$$

$$=\begin{pmatrix}
    a_{11} & a_{12}+b_{12} & a_{13}+b_{13} & a_{14}+b_{14}\\
    a_{12}-b_{12} & a_{22} & a_{23}+b_{23} & a_{24}+b_{24}\\
    a_{13}-b_{13} & a_{23}-b_{23} & a_{33} & a_{34}+b_{34}\\
    a_{14}-b_{14} & a_{24}-b_{24} & a_{34}-b_{34} & a_{44}
\end{pmatrix}=\begin{pmatrix}
    -60 & 10 & -36 & 8 \\
    -28 & -58 & 42 & -10 \\
    -14 & -18 & -8 & 30 \\
    28 & 52 & -54 & 10
\end{pmatrix}$$

Notice that:

$$\begin{cases}
    a_{12} + b_{12} = 10\\
    a_{12} - b_{12} = -28
\end{cases}\Rightarrow\begin{cases}
    a_{12}=-9\\
    b_{12}=19
\end{cases}$$

$$\begin{cases}
    a_{13} + b_{13} = -36\\
    a_{13} - b_{13} = -14
\end{cases}\Rightarrow\begin{cases}
    a_{13}=-25\\
    b_{13}=-11
\end{cases}$$

$$\begin{cases}
    a_{14} + b_{14} = 8\\
    a_{14} - b_{14} = 28
\end{cases}\Rightarrow\begin{cases}
    a_{14}=18\\
    b_{14}=-10
\end{cases}$$

$$\begin{cases}
    a_{23} + b_{23} = 42\\
    a_{23} - b_{23} = -18
\end{cases}\Rightarrow\begin{cases}
    a_{23}=12\\
    b_{23}=30
\end{cases}$$

$$\begin{cases}
    a_{24} + b_{24} = -10\\
    a_{24} - b_{24} = 52
\end{cases}\Rightarrow\begin{cases}
    a_{24}=21\\
    b_{24}=-31
\end{cases}$$

$$\begin{cases}
    a_{34} + b_{34} = 30\\
    a_{34} - b_{34} = -54
\end{cases}\Rightarrow\begin{cases}
    a_{34}=-12\\
    b_{34}=42
\end{cases}$$

$$\begin{cases}
    a_{11} = -60\\
    a_{22} = -58\\
    a_{33} = -8\\
    a_{44} = 10
\end{cases}$$

$$A=\begin{pmatrix}
    -60 & -9 & -25 & 18\\
    -9 & -58 & 12 & 21\\
    -25 & 12 & -8 & -12\\
    18 & 21 & -12 & 10
\end{pmatrix}$$

$$B=\begin{pmatrix}
    0 & 19 & -11 & -10\\
    -19 & 0 & 30 & -31\\
    11 & -30 & 0 & 42\\
    -10 & 31 & -42 & 0
\end{pmatrix}$$

Now multiply (sorry it physically doesn't fit in the pdf properly haha...):

$$AB=\begin{pmatrix}
    -60\times0+-9\times-19+-25\times11+18\times-10&-60\times19+-9\times0+-25\times-30+18\times31&-60\times-11+-9\times30+-25\times0+18\times-42&-60\times-10+-9\times-31+-25\times42+18\times0\\
    -9\times0+-58\times-19+12\times11+21\times-10&-9\times19+-58\times0+12\times-30+21\times31&-9\times-11+-58\times30+12\times0+21\times-42&-9\times-10+-58\times-31+12\times42+21\times0\\
    -25\times0+12\times-19+-8\times11+-12\times-10&-25\times19+12\times0+-8\times-30+-12\times31&-25\times-11+12\times30+-8\times0+-12\times-42&-25\times-10+12\times-31+-8\times42+-12\times0\\
    18\times0+21\times-19+-12\times11+10\times-10&18\times19+21\times0+-12\times-30+10\times31&18\times-11+21\times30+-12\times0+10\times-42&18\times-10+21\times-31+-12\times42+10\times0\\
\end{pmatrix}=$$

$$=\begin{pmatrix}
    -284 & 168 & -366 & -171 \\
    1024 & 120 & -2523 & 2392 \\
    196 & -607 & 1139 & -458 \\
    -631 & 1012 & 12 & -1335 \\
\end{pmatrix},$$

which is the answer.

<div style="page-break-after: always;"></div>

### Problem 3

> *Crime in multi-storey car parks. That is wrong on so many different levels.*

Matrix $A$ is shown in a form of $A=CJD$, where:

$$C=\begin{pmatrix}
    1 & 8 & -8 \\
    0 & 1 & -8 \\
    0 & 0 & 1
\end{pmatrix}$$

$$J=\begin{pmatrix}
    -1 & 1 & 0 \\
    0 & -1 & 1 \\
    0 & 0 & -1
\end{pmatrix}$$

$$D=\begin{pmatrix}
    1 & -8 & -56 \\
    0 & 1 & 8 \\
    0 & 0 & 1
\end{pmatrix}$$

Calculate $DC$ and find matrix $S = E + A + \dots + A^{2021}$.

$$DC=\begin{pmatrix}
    1\times1+-8\times0+-56\times0&1\times8+-8\times1+-56\times0&1\times-8+-8\times-8+-56\times1\\
    0\times1+1\times0+8\times0&0\times8+1\times1+8\times0&0\times-8+1\times-8+8\times1\\
    0\times1+0\times0+1\times0&0\times8+0\times1+1\times0&0\times-8+0\times-8+1\times1\\
\end{pmatrix}=$$

$$=\begin{pmatrix}
    1 & 0 & 0 \\
    0 & 1 & 0 \\
    0 & 0 & 1
\end{pmatrix}=E$$

Now, mess around with matrices like $A^n$:

$$A^n=(CDJ)^n=\underbrace{(CJD)(CJD)\dots (CJD)}_{n}=CJ\underbrace{(EJ)(EJ)\dots (EJ)}_{n-1}D=C\underbrace{JJ\dots J}_{n}D=CJ^nD$$

By induction, we can prove that

$$J^n = \begin{pmatrix}
    (-1)^n & (-1)^{n+1}n & (-1)^n\sum^{n-2}_{i=1}n\\
    0 & (-1)^n & (-1)^{n+1}n\\
    0 & 0 & (-1)^n
\end{pmatrix}=\begin{pmatrix}
    (-1)^n & (-1)^{n+1}n & (-1)^n\frac{n(n-1)}{2}\\
    0 & (-1)^n & (-1)^{n+1}n\\
    0 & 0 & (-1)^n
\end{pmatrix}$$

Then, 

$$\sum^{n}_{i=0}J^i=\begin{pmatrix}
    \sum^{n}_{i=0}(-1)^n & \sum^{n}_{i=0}(-1)^{n+1}n &\sum^{n}_{i=0}(-1)^n\frac{n(n-1)}{2}\\
    0 & \sum^{n}_{i=0}(-1)^n & \sum^{n}_{i=0}(-1)^{n+1}n\\
    0 & 0 & \sum^{n}_{i=0}(-1)^n\\
\end{pmatrix}=$$

$$=\begin{pmatrix}
    n\mod 2 & (-1)^n \lfloor\frac{n}{2}\rfloor & (-1)^{n+1}\left(\sum^{\lfloor\frac{n-1}{2}\rfloor}_{i=1}i+\sum^{\lfloor\frac{n-2}{2}\rfloor}_{i=1}i\right)\\
    0 & n\mod 2 & (-1)^n \lfloor\frac{n}{2}\rfloor\\
    0 & 0 & n\mod 2
\end{pmatrix}$$

And,

$$\sum^{2023}_{i=0}J^{i}=\begin{pmatrix}
    1 & -1011 & 1022121\\
    0 & 1 & -1011 \\
    0 & 0 & 1
\end{pmatrix}$$

Finally, per the distribution property:

$$\sum^{2023}_{n=0}A^{n}=C\left(\sum^{2023}_{i=0}J^{i}\right)D=\begin{pmatrix}
    1 & -1011 & 1005945 \\
    0 & 1 & -1011 \\
    0 & 0 & 1
\end{pmatrix},$$

which is the answer.

<div style="page-break-after: always;"></div>

### Problem 4

> *Police arrested two kids yesterday. One was drinking battery acid, the other was eating fireworks. They charged one – and let the other one off.*

Check that matrix

$$S=\begin{pmatrix}
    36 & 42 & -12 \\
    -30 & -35 & 10 \\
    -6 & -7 & 2
\end{pmatrix}$$

takes the form of $S=uv^T$ for some $u, v \in \mathbb{R}^3$ and find $\text{tr}S^{13}$.

$$u=\begin{pmatrix}
    u_1 \\
    u_2 \\
    u_3 \\
\end{pmatrix},\ \ v=\begin{pmatrix}
    v_1 \\
    v_2 \\
    v_3 \\
\end{pmatrix}$$

$$S=uv^T=\begin{pmatrix}
    u_1v_1 & u_1v_2 & u_1v_3 \\
    u_2v_1 & u_2v_2 & u_2v_3 \\
    u_3v_1 & u_3v_2 & u_3v_3 \\
\end{pmatrix}$$

By finding greatest common divisors, notice that 

$$u=\begin{pmatrix}
    6 \\
    -5 \\
    -1 \\
\end{pmatrix},\ \ v=\begin{pmatrix}
    6 \\
    7 \\
    -2 \\
\end{pmatrix},$$

which means that this property holds.

Therefore, considering that $v^Tu=\text{tr}S=36-35+2=3$,

$$S^{13}=u\underbrace{v^Tuv^T\dots u}_{12}v^T=(\text{tr}S)^{12}S$$

At last,

$$\text{tr}S^{13}=\text{tr}((\text{tr}S)^{12}S)=(\text{tr}S)^{13}=3^{13}=1594323,$$

which is the answer.

<div style="page-break-after: always;"></div>

### Problem 5

> *What do you call a fish with no eyes?*
> *A fsh.*

#### Subproblem A

$$\begin{cases}
-3x_1 + 2x_2+3x_3-5x_4=0\\ 
-6x_1+4x_2+6x_3-10x_4=4\\
-8x_1+5x_2+7x_3-12x_4=-5\\
7x_1-4x_2-5x_3+9x_4=-5
\end{cases}$$

Divide the second line by $2$ and see that the first and the second lines are the same, which means that the matrix is inconsistent.

$$\begin{pmatrix}
-3 & 2 & 3 & -5 &\bigm| & 0\\
-6 & 4 & 6 & -10 &\bigm| & 4\\
-8 & 5 & 7 & -12 &\bigm| & -5\\
7 & -4 & -5 & 9 &\bigm| & -5
\end{pmatrix}\sim\begin{pmatrix}
-3 & 2 & 3 & -5 &\bigm| & 0\\
-3 & 2 & 3 & -5 &\bigm| & 4\\
-8 & 5 & 7 & -12 &\bigm| & -5\\
7 & -4 & -5 & 9 &\bigm| & -5
\end{pmatrix}$$

Answer: the matrix is inconsistent.

#### Subproblem B

$$\begin{cases}
-3x_1 + 2x_2+3x_3-5x_4=14\\ 
-6x_1+4x_2+6x_3-10x_4=28\\
-8x_1+5x_2+7x_3-12x_4=36\\
7x_1-4x_2-5x_3+9x_4=-30
\end{cases}$$

$$\begin{pmatrix}
-3 & 2 & 3 & -5 &\bigm| & 14\\
-6 & 4 & 6 & -10 &\bigm| & 28\\
-8 & 5 & 7 & -12 &\bigm| & 36\\
7 & -4 & -5 & 9 &\bigm| & -30
\end{pmatrix}\sim\begin{pmatrix}
-3 & 2 & 3 & -5 &\bigm| & 14\\
-8 & 5 & 7 & -12 &\bigm| & 36\\
7 & -4 & -5 & 9 &\bigm| & -30\\
0 & 0 & 0 & 0 &\bigm| & 0
\end{pmatrix}\sim$$

$$\sim\begin{pmatrix}
1 & -\frac{2}{3} & -1 & \frac{5}{3} &\bigm| & -\frac{14}{3}\\
-8 & 5 & 7 & -12 &\bigm| & 36\\
7 & -4 & -5 & 9 &\bigm| & -30\\
0 & 0 & 0 & 0 &\bigm| & 0
\end{pmatrix}\sim\begin{pmatrix}
1 & -\frac{2}{3} & -1 & \frac{5}{3} &\bigm| & -\frac{14}{3}\\
0 & -\frac{1}{3} & -1 & \frac{4}{3} &\bigm| & -\frac{4}{3}\\
0 & \frac{2}{3} & 2 & -\frac{8}{3} &\bigm| & \frac{8}{3}\\
0 & 0 & 0 & 0 &\bigm| & 0
\end{pmatrix}\sim$$

$$\sim\begin{pmatrix}
1 & -\frac{2}{3} & -1 & \frac{5}{3} &\bigm| & -\frac{14}{3}\\
0 & 1 & 3 & -4 &\bigm| & 4\\
0 & 2 & 6 & -8 &\bigm| & 8\\
0 & 0 & 0 & 0 &\bigm| & 0
\end{pmatrix}\sim\begin{pmatrix}
1 & -\frac{2}{3} & -1 & \frac{5}{3} &\bigm| & -\frac{14}{3}\\
0 & 1 & 3 & -4 &\bigm| & 4\\
0 & 0 & 0 & 0 &\bigm| & 0\\
0 & 0 & 0 & 0 &\bigm| & 0
\end{pmatrix}\sim$$

$$\sim\begin{pmatrix}
1 & 0 & 1 & -1 &\bigm| & -2\\
0 & 1 & 3 & -4 &\bigm| & 4\\
0 & 0 & 0 & 0 &\bigm| & 0\\
0 & 0 & 0 & 0 &\bigm| & 0
\end{pmatrix}$$

Awesome, now write the general solution:

$$\begin{cases}
x_1 = x_4 - x_3 - 2\\
x_2 = 4 - 3x_3 + 4x_4
\end{cases}$$

Example of a partial solution:

$$\begin{cases}
x_1 = x_4 - x_3 - 2\\
x_2 = 4 - 3x_3 + 4x_4\\
x_3 = 0\\
x_4 = 0
\end{cases}$$