## Individual Homework 1 (variant 20)

### Problem 1

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

### Problem 2

### Problem 5

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

**Answer: the matrix is inconsistent.**

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