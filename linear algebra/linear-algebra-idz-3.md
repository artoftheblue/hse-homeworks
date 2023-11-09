# Individual Homework #3

## Problem 1

Find inverse matrix of 

$$\begin{pmatrix}
    -6 & 4 & 3 & 3\\
    2 & -2 & 0 & -1\\
    -2 & -5 & -2 & 3\\
    -1 & -1 & 0 & 1
\end{pmatrix}$$

---

Per Gauss:

$$\begin{pmatrix}
    -6 & 4 & 3 & 3 & \bigm| & 1 & 0 & 0 & 0\\
    2 & -2 & 0 & -1 & \bigm| & 0 & 1 & 0 & 0\\
    -2 & -5 & -2 & 3 & \bigm| & 0 & 0 & 1 & 0\\
    -1 & -1 & 0 & 1 & \bigm| & 0 & 0 & 0 & 1
\end{pmatrix}$$

$$\begin{pmatrix}
    1 & 1 & 0 & -1 & \bigm| & 0 & 0 & 0 & -1\\
    -6 & 4 & 3 & 3 & \bigm| & 1 & 0 & 0 & 0\\
    2 & -2 & 0 & -1 & \bigm| & 0 & 1 & 0 & 0\\
    -2 & -5 & -2 & 3 & \bigm| & 0 & 0 & 1 & 0\\
\end{pmatrix}$$

$$\begin{pmatrix}
    1 & 1 & 0 & -1 & \bigm| & 0 & 0 & 0 & -1\\
    0 & 10 & 3 & -3 & \bigm| & 1 & 0 & 0 & -6\\
    0 & -4 & 0 & 1 & \bigm| & 0 & 1 & 0 & 2\\
    0 & -3 & -2 & 1 & \bigm| & 0 & 0 & 1 & -2\\
\end{pmatrix}$$

$$\begin{pmatrix}
    1 & 1 & 0 & -1 & \bigm| & 0 & 0 & 0 & -1\\
    0 & 10 & 3 & -3 & \bigm| & 1 & 0 & 0 & -6\\
    0 & 0 & 1.2 & -0.2 & \bigm| & 0.4 & 1 & 0 & -0.4\\
    0 & 0 & -1.1 & 0.1 & \bigm| & 0.3 & 0 & 1 & -3.8\\
\end{pmatrix}$$

$$\begin{pmatrix}
    1 & 1 & 0 & -1 & \bigm| & 0 & 0 & 0 & -1\\
    0 & 1 & 0.3 & -0.3 & \bigm| & 0.1 & 0 & 0 & -0.6\\
    0 & 0 & 1.2 & -0.2 & \bigm| & 0.4 & 1 & 0 & -0.4\\
    0 & 0 & -1.1 & 0.1 & \bigm| & 0.3 & 0 & 1 & -3.8\\
\end{pmatrix}$$

$$\begin{pmatrix}
    1 & 1 & 0 & -1 & \bigm| & 0 & 0 & 0 & -1\\
    0 & 1 & 0.3 & -0.3 & \bigm| & 0.1 & 0 & 0 & -0.6\\
    0 & 0 & 0.1 & -0.1 & \bigm| & 0.7 & 1 & 1 & -4.2\\
    0 & 0 & -1.1 & 0.1 & \bigm| & 0.3 & 0 & 1 & -3.8\\
\end{pmatrix}$$

$$\begin{pmatrix}
    1 & 1 & 0 & -1 & \bigm| & 0 & 0 & 0 & -1\\
    0 & 1 & 0.3 & -0.3 & \bigm| & 0.1 & 0 & 0 & -0.6\\
    0 & 0 & 0.1 & -0.1 & \bigm| & 0.7 & 1 & 1 & -4.2\\
    0 & 0 & -1 & 0 & \bigm| & 1 & 1 & 2 & -8\\
\end{pmatrix}$$

$$\begin{pmatrix}
    1 & 1 & 0 & -1 & \bigm| & 0 & 0 & 0 & -1\\
    0 & 1 & 0.3 & -0.3 & \bigm| & 0.1 & 0 & 0 & -0.6\\
    0 & 0 & 1 & -1 & \bigm| & 7 & 10 & 10 & -42\\
    0 & 0 & -1 & 0 & \bigm| & 1 & 1 & 2 & -8\\
\end{pmatrix}$$

$$\begin{pmatrix}
    1 & 1 & 0 & -1 & \bigm| & 0 & 0 & 0 & -1\\
    0 & 1 & 0.3 & -0.3 & \bigm| & 0.1 & 0 & 0 & -0.6\\
    0 & 0 & 1 & -1 & \bigm| & 7 & 10 & 10 & -42\\
    0 & 0 & 0 & 1 & \bigm| & -8 & -11 & -12 & 50\\
\end{pmatrix}$$

$$\begin{pmatrix}
    1 & 1 & 0 & -1 & \bigm| & 0 & 0 & 0 & -1\\
    0 & 10 & 3 & -3 & \bigm| & 1 & 0 & 0 & -6\\
    0 & 0 & 1 & 0 & \bigm| & -1 & -1 & -2 & 8\\
    0 & 0 & 0 & 1 & \bigm| & -8 & -11 & -12 & 50\\
\end{pmatrix}$$

$$\begin{pmatrix}
    1 & 1 & 0 & -1 & \bigm| & 0 & 0 & 0 & -1\\
    0 & 10 & 0 & -3 & \bigm| & 4 & 3 & 6 & -30\\
    0 & 0 & 1 & 0 & \bigm| & -1 & -1 & -2 & 8\\
    0 & 0 & 0 & 1 & \bigm| & -8 & -11 & -12 & 50\\
\end{pmatrix}$$

$$\begin{pmatrix}
    1 & 1 & 0 & -1 & \bigm| & 0 & 0 & 0 & -1\\
    0 & 10 & 0 & 0 & \bigm| & -20 & -30 & -30 & 120\\
    0 & 0 & 1 & 0 & \bigm| & -1 & -1 & -2 & 8\\
    0 & 0 & 0 & 1 & \bigm| & -8 & -11 & -12 & 50\\
\end{pmatrix}$$

$$\begin{pmatrix}
    1 & 1 & 0 & -1 & \bigm| & 0 & 0 & 0 & -1\\
    0 & 1 & 0 & 0 & \bigm| & -2 & -3 & -3 & 12\\
    0 & 0 & 1 & 0 & \bigm| & -1 & -1 & -2 & 8\\
    0 & 0 & 0 & 1 & \bigm| & -8 & -11 & -12 & 50\\
\end{pmatrix}$$

$$\begin{pmatrix}
    1 & 0 & 0 & -1 & \bigm| & 2 & 3 & 3 & -13\\
    0 & 1 & 0 & 0 & \bigm| & -2 & -3 & -3 & 12\\
    0 & 0 & 1 & 0 & \bigm| & -1 & -1 & -2 & 8\\
    0 & 0 & 0 & 1 & \bigm| & -8 & -11 & -12 & 50\\
\end{pmatrix}$$

$$\begin{pmatrix}
    1 & 0 & 0 & 0 & \bigm| & -6 & -8 & -9 & 37\\
    0 & 1 & 0 & 0 & \bigm| & -2 & -3 & -3 & 12\\
    0 & 0 & 1 & 0 & \bigm| & -1 & -1 & -2 & 8\\
    0 & 0 & 0 & 1 & \bigm| & -8 & -11 & -12 & 50\\
\end{pmatrix}$$

**Answer:**

$$\begin{pmatrix}
    -6 & -8 & -9 & 37\\
    -2 & -3 & -3 & 12\\
    -1 & -1 & -2 & 8\\
    -8 & -11 & -12 & 50\\
\end{pmatrix}$$

## Problem 2

Solve equation for $X$:

$$\left(\begin{pmatrix}
    1 & 2 & 3 & 4 & 5 & 6 & 7 & 8\\
    4 & 6 & 8 & 5 & 1 & 3 & 7 & 2
\end{pmatrix}^{11}\cdot\begin{pmatrix}
    1 & 2 & 3 & 4 & 5 & 6 & 7 & 8\\
    4 & 8 & 5 & 6 & 2 & 7 & 3 & 1\\
\end{pmatrix}^{-1}\right)^{149}\cdot X=\begin{pmatrix}
    1 & 2 & 3 & 4 & 5 & 6 & 7 & 8\\
    6 & 3 & 1 & 5 & 4 & 7 & 8 & 2\\
\end{pmatrix}$$

---

$$\begin{pmatrix}
    1 & 2 & 3 & 4 & 5 & 6 & 7 & 8\\
    4 & 8 & 5 & 6 & 2 & 7 & 3 & 1\\
\end{pmatrix}^{-1}=\begin{pmatrix}
    1 & 2 & 3 & 4 & 5 & 6 & 7 & 8\\
    8 & 5 & 7 & 1 & 3 & 4 & 6 & 2\\
\end{pmatrix}$$

---

In the following permutation, there are $3$ cycles: 

$$\begin{pmatrix}
    1 & 2 & 3 & 4 & 5 & 6 & 7 & 8\\
    4 & 6 & 8 & 5 & 1 & 3 & 7 & 2\\
\end{pmatrix}$$

* $\text{mod} \ 3$: $\ \xrightarrow{0}1\xrightarrow{1} 4 \xrightarrow{2} 5$
* $\text{mod} \ 4$: $\ \xrightarrow{0} 2 \xrightarrow{1} 6 \xrightarrow{2} 3 \xrightarrow{3} 8$
* $\text{mod} \ 1$: $\ \xrightarrow{0} 7$

This permutation is composed with the permutation $11$ times, a composition of $12$ permutations in total. Since $12 \ \text{mod} \ 3 = 0, 12 \ \text{mod} \ 4 = 0, 12 \ \text{mod} \ 1 = 0$, then since 

$$\begin{pmatrix}
    1 & 2 & 3 & 4 & 5 & 6 & 7 & 8\\
    4 & 6 & 8 & 5 & 1 & 3 & 7 & 2
\end{pmatrix}^{11}\begin{pmatrix}
    1 & 2 & 3 & 4 & 5 & 6 & 7 & 8\\
    8 & 5 & 7 & 1 & 3 & 4 & 6 & 2\\
\end{pmatrix}=\begin{pmatrix}
    1 & 2 & 3 & 4 & 5 & 6 & 7 & 8\\
    8 & 5 & 7 & 1 & 3 & 4 & 6 & 2\\
\end{pmatrix}$$

is fhe first mapping, then after $11$ compositions it would bring us back to square one.

The resulting permutation consists of a single cycle of length $8$:

* $1 \rightarrow  8 \rightarrow 2 \rightarrow 5 \rightarrow 3  \rightarrow 7 \rightarrow 6 \rightarrow 4\rightarrow 1$

Composing this permutation with itself $149 - 1=148$ times would be identical to composing it $148 \ \text{mod} \ 8 = 4$ times, thus we need to shift each position in the permutation above $4$ spaces along the cycle:

$$\begin{pmatrix}
    1 & 2 & 3 & 4 & 5 & 6 & 7 & 8\\
    8 & 5 & 7 & 1 & 3 & 4 & 6 & 2\\
\end{pmatrix}^{149}=\begin{pmatrix}
    1 & 2 & 3 & 4 & 5 & 6 & 7 & 8\\
    8 & 5 & 7 & 1 & 3 & 4 & 6 & 2\\
\end{pmatrix}^5=\begin{pmatrix}
    1 & 2 & 3 & 4 & 5 & 6 & 7 & 8\\
    7 & 4 & 8 & 3 & 1 & 5 & 2 & 6\\
\end{pmatrix}$$

Sweet, now we only need to solve the following equation:

$$\begin{pmatrix}
    1 & 2 & 3 & 4 & 5 & 6 & 7 & 8\\
    7 & 4 & 8 & 3 & 1 & 5 & 2 & 6\\
\end{pmatrix}\cdot X = \begin{pmatrix}
    1 & 2 & 3 & 4 & 5 & 6 & 7 & 8\\
    6 & 3 & 1 & 5 & 4 & 7 & 8 & 2\\
\end{pmatrix}$$

Write up as a tri-permutation (custom notation, oopsie):

$$\begin{pmatrix}
    1 & 2 & 3 & 4 & 5 & 6 & 7 & 8\\
    ? & ? & ? & ? & ? & ? & ? & ?\\
    6 & 3 & 1 & 5 & 4 & 7 & 8 & 2\\
\end{pmatrix}$$

Use mappings from 

$$\begin{pmatrix}
    1 & 2 & 3 & 4 & 5 & 6 & 7 & 8\\
    7 & 4 & 8 & 3 & 1 & 5 & 2 & 6\\
\end{pmatrix}$$

to fill in the gaps and get 

$$\begin{pmatrix}
    1 & 2 & 3 & 4 & 5 & 6 & 7 & 8\\
    8 & 4 & 5 & 6 & 2 & 1 & 3 & 7\\
    6 & 3 & 1 & 5 & 4 & 7 & 8 & 2\\
\end{pmatrix}\Rightarrow X=\begin{pmatrix}
    1 & 2 & 3 & 4 & 5 & 6 & 7 & 8\\
    8 & 4 & 5 & 6 & 2 & 1 & 3 & 7\\
\end{pmatrix}$$

**Answer:**

$$\begin{pmatrix}
    1 & 2 & 3 & 4 & 5 & 6 & 7 & 8\\
    8 & 4 & 5 & 6 & 2 & 1 & 3 & 7\\
\end{pmatrix}$$

## Problem 3

Find whether a permutation is odd or even:

$$\sigma=\begin{pmatrix}
    1 & 2 & \dots & 97 & 98 & \dots &131 & 132 & \dots & 256\\
    160 & 161 & \dots & 256 & 126 & \dots & 159 & 1 & \dots & 125
\end{pmatrix}$$

---

Calculate the number of inversions:

* There are $256-159=97$ elements in the first group, $159-125=34$ elements in the second group, and $125$ elements in the third group.
* Both groups $2$ and $3$ are wholly inverted in relation to the first group.
* The third group is inverted in relation to the second group. 

Therefore, the total number of inversions:

$$97\times(34+125)+34\times125=15423+4250=19673$$

The number of inversions is odd $\Rightarrow$ the permutation is odd.

> It is also fair to mention that this entire permutation turns out to be a single cycle of even ($256$) length; therefore, since cycles of even lengths are odd, the entire permutation is odd as well.

**Answer:**

$$\text{sgn}\sigma=-1$$

## Problem 4

Calculate: 

$$\det\begin{vmatrix}
    0 & 0 & x & 0 & 0 & 2\\
    x & x & 9 & x & 0 & 1\\
    0 & 7 & 0 & 8 & 4 & 4\\
    0 & 2 & 0 & 0 & 0 & 7\\
    5 & 4 & x & x & 4 & 5\\
    0 & 4 & 2 & 2 & 5 & 5\\
\end{vmatrix}$$

---

$$x\det\begin{vmatrix}
    x & x & x & 0 & 1\\
    0 & 7 & 8 & 4 & 4\\
    0 & 2 & 0 & 0 & 7\\
    5 & 4 & x & 4 & 5\\
    0 & 4 & 2 & 5 & 5\\
\end{vmatrix}+2\det\begin{vmatrix}
    x & x & 9 & x & 0\\
    0 & 7 & 0 & 8 & 4\\
    0 & 2 & 0 & 0 & 0\\
    5 & 4 & x & x & 4\\
    0 & 4 & 2 & 2 & 5\\
\end{vmatrix}$$

$$2x\det\begin{vmatrix}
    x & x & 0 & 1\\
    0 & 8 & 4 & 4\\
    5 & x & 4 & 5\\
    0 & 2 & 5 & 5\\
\end{vmatrix}+7x\det\begin{vmatrix}
    x & x & x & 0\\
    0 & 7 & 8 & 4\\
    5 & 4 & x & 4\\
    0 & 4 & 2 & 5\\
\end{vmatrix}+4\det\begin{vmatrix}
    x & 9 & x & 0\\
    0 & 0 & 8 & 4\\
    5 & x & x & 4\\
    0 & 2 & 2 & 5\\
\end{vmatrix}$$

$$2x\det\begin{vmatrix}
    x & x & 0 & 1\\
    0 & 8 & 4 & 4\\
    5 & x & 4 & 5\\
    0 & 2 & 5 & 5\\
\end{vmatrix}+7x\det\begin{vmatrix}
    x & x & x & 0\\
    0 & 7 & 8 & 4\\
    5 & 4 & x & 4\\
    0 & 4 & 2 & 5\\
\end{vmatrix}+32\det\begin{vmatrix}
    x & 9 & 0\\
    5 & x & 4\\
    0 & 2 & 5\\
\end{vmatrix}+16\det\begin{vmatrix}
    x & 9 & x\\
    5 & x & x\\
    0 & 2 & 2\\
\end{vmatrix}$$

$$2x\det\begin{vmatrix}
    x & x & 0 & 1\\
    0 & 8 & 4 & 4\\
    5 & x & 4 & 5\\
    0 & 2 & 5 & 5\\
\end{vmatrix}+7x\det\begin{vmatrix}
    x & x & x & 0\\
    0 & 7 & 8 & 4\\
    5 & 4 & x & 4\\
    0 & 4 & 2 & 5\\
\end{vmatrix}+64\det\begin{vmatrix}
    x & 0\\
    5 & 4\\
\end{vmatrix}+160\det\begin{vmatrix}
    x & 9\\
    5 & x\\
\end{vmatrix}+32\det\begin{vmatrix}
    x & x\\
    5 & x\\
\end{vmatrix}+32\det\begin{vmatrix}
    x & 9\\
    5 & x\\
\end{vmatrix}$$

$$2x\det\begin{vmatrix}
    x & x & 0 & 1\\
    0 & 8 & 4 & 4\\
    5 & x & 4 & 5\\
    0 & 2 & 5 & 5\\
\end{vmatrix}+7x\det\begin{vmatrix}
    x & x & x & 0\\
    0 & 7 & 8 & 4\\
    5 & 4 & x & 4\\
    0 & 4 & 2 & 5\\
\end{vmatrix}+256x+160(x^2-45)+32(x^2-5x)+32(x^2-45)$$

$$2x\det\begin{vmatrix}
    x & x & 0 & 1\\
    0 & 8 & 4 & 4\\
    5 & x & 4 & 5\\
    0 & 2 & 5 & 5\\
\end{vmatrix}+7x\det\begin{vmatrix}
    x & x & x & 0\\
    0 & 7 & 8 & 4\\
    5 & 4 & x & 4\\
    0 & 4 & 2 & 5\\
\end{vmatrix}+224x^2+96x-8640$$

Find 

$$\det\begin{vmatrix}
    x & x & 0 & 1\\
    0 & 8 & 4 & 4\\
    5 & x & 4 & 5\\
    0 & 2 & 5 & 5\\
\end{vmatrix}=-\det\begin{vmatrix}
    5 & x & 4 & 5\\
    0 & 8 & 4 & 4\\
    x & x & 0 & 1\\
    0 & 2 & 5 & 5\\
\end{vmatrix}=-\det\begin{vmatrix}
    5 & x & 4 & 5\\
    0 & 8 & 4 & 4\\
    0 & 0.2(-5+x)x & -0.8x & 1-x\\
    0 & 2 & 5 & 5\\
\end{vmatrix}=$$

$$-\det\begin{vmatrix}
    5 & x & 4 & 5\\
    0 & 8 & 4 & 4\\
    0 & 0 & -0.1(-13+x)x & 0.1(10-15x+x^2)\\
    0 & 0 & 4 & 4\\
\end{vmatrix}=\det\begin{vmatrix}
    5 & x & 4 & 5\\
    0 & 8 & 4 & 4\\
    0 & 0 & 4 & 4\\
    0 & 0 & -0.1(-13+x)x & 0.1(10-15x+x^2)\\
\end{vmatrix}=$$

$$\det\begin{vmatrix}
    5 & x & 4 & 5\\
    0 & 8 & 4 & 4\\
    0 & 0 & 4 & 4\\
    0 & 0 & 0 & 1-0.2x\\
\end{vmatrix}=5\times8\times4\times\left(1-\frac{x}{5}\right)=-32x+160$$

Find 

$$\det\begin{vmatrix}
    x & x & x & 0\\
    0 & 7 & 8 & 4\\
    5 & 4 & x & 4\\
    0 & 4 & 2 & 5\\
\end{vmatrix}=-\det\begin{vmatrix}
    5 & 4 & x & 4\\
    0 & 7 & 8 & 4\\
    x & x & x & 0\\
    0 & 4 & 2 & 5\\
\end{vmatrix}=-\det\begin{vmatrix}
    5 & 4 & x & 4\\
    0 & 7 & 8 & 4\\
    0 & 0.2x & -0.2(-5+x)x & -0.8x\\
    0 & 4 & 2 & 5\\
\end{vmatrix}=$$

$$-\det\begin{vmatrix}
    5 & 4 & x & 4\\
    0 & 7 & 8 & 4\\
    0 & 0 & \frac{1}{35}(27-7x)x & -\frac{32}{25}x\\
    0 & 0 & -\frac{18}{7} & \frac{19}{7}\\
\end{vmatrix}=\det\begin{vmatrix}
    5 & 4 & x & 4\\
    0 & 7 & 8 & 4\\
    0 & 0 & -\frac{18}{7} & \frac{19}{7}\\
    0 & 0 & \frac{1}{35}(27-7x)x & -\frac{32}{25}x\\
\end{vmatrix}=\det\begin{vmatrix}
    5 & 4 & x & 4\\
    0 & 7 & 8 & 4\\
    0 & 0 & -\frac{18}{7} & \frac{19}{7}\\
    0 & 0 & 0 & -\frac{1}{90}x(9+19x)\\
\end{vmatrix}=$$

$$\frac{5\times7\times-18\times-x(9+19x)}{7\times90}=19x^2+9x$$

Finally,

$$2x(-32x+160)+7x(19x^2+9x)+256x+160(x^2-45)+32(x^2-5x)+32(x^2-45)=$$

$$133x^3+(63+32+192-64)x^2+(-160+320+256)x-8640=133x^3+223x^2+416x-8640$$

**Answer:** 

> I beg for this to be correct otherwise my sanity will literally implode and cause me to die (also I didn't continue with the algebraic expansion because I kept messing up for some reason and the answer went to hell)

$$133x^3+223x^2+416x-8640$$

## Problem 5

Find the coefficient before $x^5$ in the determinant expression:

$$\begin{vmatrix}
    2 & 5 & 10 & 9 & x & 8 & 10\\
    5 & 8 & 8 & x & 5 & 6 & 8\\
    10 & 8 & x & 8 & 7 & 8 & 9\\
    9 & x & 8 & 8 & 1 & 6 & 8\\
    x & 5 & 7 & 1 & 7 & 9 & x\\
    8 & 6 & 8 & 6 & 9 & x & 4\\
    10 & 8 & 9 & 8 & x & 4 & 6\\
\end{vmatrix}$$

---

Simplify:

$$\begin{vmatrix}
    x & 5 & 7 & 1 & 7 & 9 & x\\
    9 & x & 8 & 8 & 1 & 6 & 8\\
    10 & 8 & x & 8 & 7 & 8 & 9\\
    5 & 8 & 8 & x & 5 & 6 & 8\\
    2 & 5 & 10 & 9 & x & 8 & 10\\
    8 & 6 & 8 & 6 & 9 & x & 4\\
    10 & 8 & 9 & 8 & x & 4 & 6\\
\end{vmatrix}$$

$$\begin{vmatrix}
    x & 5 & 7 & 1 & 7 & 9 & x\\
    9 & x & 8 & 8 & 1 & 6 & 8\\
    10 & 8 & x & 8 & 7 & 8 & 9\\
    5 & 8 & 8 & x & 5 & 6 & 8\\
    2 & 5 & 10 & 9 & x & 8 & 10\\
    8 & 6 & 8 & 6 & 9 & x & 4\\
    8 & 3 & -1 & -1 & 0 & -4 & -4\\
\end{vmatrix}$$

$$\begin{vmatrix}
    x & 5 & 7 & 1 & 7 & 9 & 0\\
    9 & x & 8 & 8 & 1 & 6 & -1\\
    10 & 8 & x & 8 & 7 & 8 & -1\\
    5 & 8 & 8 & x & 5 & 6 & 3\\
    2 & 5 & 10 & 9 & x & 8 & 8\\
    8 & 6 & 8 & 6 & 9 & x & -4\\
    8 & 3 & -1 & -1 & 0 & -4 & -12\\
\end{vmatrix}$$


We need to consider ${6 \choose 5}=6$ options of choosing $5$ lines out of $6$ lines that have $x$ after simplifications and calculate determinants of those minors:

$$\begin{vmatrix}
    x & 5 & 7 & 1 & 7 & 9 & \overset{M_{17}}{\boxed{0}}\\
    9 & x & 8 & 8 & 1 & 6 & \overset{M_{27}}{\boxed{-1}}\\
    10 & 8 & x & 8 & 7 & 8 & \overset{M_{37}}{\boxed{-1}}\\
    5 & 8 & 8 & x & 5 & 6 & \overset{M_{47}}{\boxed{3}}\\
    2 & 5 & 10 & 9 & x & 8 & \overset{M_{57}}{\boxed{8}}\\
    8 & 6 & 8 & 6 & 9 & x & \overset{M_{67}}{\boxed{-4}}\\
    \overset{M_{17}}{\boxed{8}} & \overset{M_{27}}{\boxed{3}} & \overset{M_{37}}{\boxed{-1}} & \overset{M_{47}}{\boxed{-1}} & \overset{M_{57}}{\boxed{0}} & \overset{M_{67}}{\boxed{-4}} & -12\\
\end{vmatrix}$$

We only take the auxiliary diagonal of each of the minors, since we don't need the $x$-s (multiply respective values highlighted above), thus for $kx^5 \in \det A$ (funny notation, I know). $M_{ij}$ denotes which columns/lines have not been taken as a part of the algebraic expansion, and now to evaluate all the minors/algebraic complements after the expansion over $x$ has taken place:

$$x^5M_{17} = x^5\begin{vmatrix}
    x & 0 \\
    8 & -12\\
\end{vmatrix}$$

$$x^5M_{27} = x^5\begin{vmatrix}
    x & -1 \\
    3 & -12\\
\end{vmatrix}$$

$$x^5M_{37} = x^5\begin{vmatrix}
    x & -1 \\
    -1 & -12\\
\end{vmatrix}$$

$$x^5M_{47} = x^5\begin{vmatrix}
    x & 3 \\
    -1 & -12\\
\end{vmatrix}$$

$$x^5M_{57} = x^5\begin{vmatrix}
    x & 8 \\
    0 & -12\\
\end{vmatrix}$$

$$x^5M_{57} = x^5\begin{vmatrix}
    x & -4 \\
    -4 & -12\\
\end{vmatrix}$$

Now, only take the auxiliary diagoal since we don't care about $x^6$:

$$k=-(8\times0 + 3\times-1+-1\times-1+-1\times3+0\times8+-4\times-4)=-(0-3+1-3+0+16)=-11$$

**Answer:** $$-11$$