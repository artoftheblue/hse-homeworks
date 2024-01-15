# Individual Homework №4, Linear Algebra

## Problem 1

Given matrix

$$A=\begin{pmatrix}
    14 + 7i & -12 - 8i\\
    18 + 12i & -16 - 13i
\end{pmatrix}\in M_{2\times2}(\mathbb{C})$$

find all values $x\in\mathbb{C}$, for which matrix $A - xE$ is irreversible.

---

For a matrix to be irreversible, its determinant has to be equal to $0$:

$$|A-xE|=\det\begin{pmatrix}
    14 + 7i - x & -12 - 8i\\
    18 + 12i & -16 - 13i - x
\end{pmatrix}=0$$

$$\det\begin{pmatrix}
    14 + 7i - x & -12 - 8i\\
    18 + 12i & -16 - 13i - x
\end{pmatrix}=0$$

Thus,

$$(14+7i-x)(-16-13i-x)-(18-12i)(-12-8i)=0$$

$$-91i^2+6ix-294i+x^2+2x-224+216-96i^2=0$$

$$91+6ix-294i+x^2+2x-224+216+96=0$$

$$x^2+2x+6ix+179-294i=0$$

$$x^2+x(2+6i)+179-294i$$

$$x^2+(2+6i)x-(8-6i)=-187+300i$$

$$(x+(1+3i))^2=-187+300i$$

$$x=\plusmn\sqrt{-187+300i}-(1+3i)$$

**Answer:** $$x=\plusmn\sqrt{-187+300i}-(1+3i)$$



## Problem 2

Calculate

$$\sqrt[4]{-18-18\sqrt{3}i}$$

---

$$z_0=18\sqrt[4]{-1-\sqrt{3}i}$$

$$z_1 = -1-\sqrt{3}i$$

Get the trigonometric form:

$$z_1=|z_1|(\cos\phi+i\sin\phi)$$

$$|z_1|=\sqrt{(-1)^2+(-\sqrt{3})^2}=2$$

$$\cos\phi=-\frac{1}{2}$$

$$\sin\phi=-\frac{\sqrt{3}}{2}$$

$$\phi=-\frac{2\pi}{3}$$

$$z_1=2\left(\cos\left(-\frac{2\pi}{3}\right)+i\left(-\frac{2\pi}{3}\right)\right)$$


Find such $w_i$ that $w_i^4=z_1$.

$$w_i=\sqrt[4]{|z_1|}\left(\cos \frac{\phi+2\pi k}{4}+i\sin\frac{\phi+2\pi k}{4}\right)$$

$$w_i=\sqrt[4]{2}\left(\cos \frac{-\frac{2\pi}{3}+2\pi k}{4}+i\sin \frac{-\frac{2\pi}{3}+2\pi k}{4}\right)$$

$$w_i=\sqrt[4]{2}\left(\cos \left(-\frac{\pi}{6}+\frac{\pi k}{2}\right)+i\sin \left(-\frac{\pi}{6}+\frac{\pi k}{2}\right)\right)$$

Now find all $4$ roots and thus get **the answer**:

$$w_1=\sqrt[4]{2}\left(\cos \left(-\frac{\pi}{6}\right)+i\sin \left(-\frac{\pi}{6}\right)\right)$$

$$w_2=\sqrt[4]{2}\left(\cos \frac{\pi}{3}+i\sin \frac{\pi}{3}\right)$$

$$w_3=\sqrt[4]{2}\left(\cos \frac{5\pi}{6}+i\sin \frac{5\pi}{6}\right)$$

$$w_4=\sqrt[4]{2}\left(\cos \left(-\frac{2\pi}{3}\right)+i\sin \left(-\frac{2\pi}{3}\right)\right)$$

## Problem 3

Given vectors

$$v_1=\begin{pmatrix}
    8\\
    -7\\
    1\\
    -1\\
    -4
\end{pmatrix} \ \ v_2=\begin{pmatrix}
    -88\\
    82\\
    -12\\
    5\\
    45
\end{pmatrix} \ \ v_3=\begin{pmatrix}
    200\\
    -200\\
    30\\
    a\\
    -104
\end{pmatrix}$$

prove that they are linearly independent for all values of parameter $a$, and for each $a$, complement these vectors to a basis of the entire $\mathbb{R}^5$ space.

---

$$\alpha_1v_1+\alpha_2v_2+\alpha_3v_3=\vec{0}$$

Calculate the matrix's rank, first reducing the matrix to a row echelon form:

$$\begin{pmatrix}
    8 & -88 & 200\\
    -7 & 82 & -200\\
    1 & -12 & 30\\
    -1 & 5 & a\\
    -4 & 45 & 104
\end{pmatrix}$$

$$\begin{pmatrix}
    1 & -12 & 30\\
    0 & -2 & 10\\
    0 & 8 & -40\\
    0 & -7 & a + 30\\
    0 & -3 & 224
\end{pmatrix}$$

$$\begin{pmatrix}
    1 & -12 & 30\\
    0 & -2 & 10\\
    0 & 0 & 0\\
    0 & 0 & a - 5\\
    0 & 0 & 209
\end{pmatrix}$$

$$\begin{pmatrix}
    1 & -12 & 30\\
    0 & -2 & 10\\
    0 & 0 & 209\\
    0 & 0 & a - 5\\
    0 & 0 & 0\\
\end{pmatrix}$$

At this point, we may add $\displaystyle\frac{-a+5}{209}$ times row $3$ to row $4$ regardless of value $a$ and get a matrix of rank $3$ (there are $3$ non-zero rows in this form of the matrix), which proves that these $3$ vectors are linearly independent.

Now build a basis from this. Try to add the following vectors to the basis and check whether the determinant of the resulting matrix would be $0$ or not:

$$v_4=\begin{pmatrix}
    1\\
    0\\
    0\\
    0\\
    0
\end{pmatrix} \ \ v_5=\begin{pmatrix}
    0\\
    0\\
    0\\
    0\\
    1\\
\end{pmatrix}$$

Resulting matrix:

$$\begin{pmatrix}
    1 & 8 & -88 & 200 & 0\\
    0 & -7 & 82 & -200 & 0\\
    0 & 1 & -12 & 30 & 0\\
    0 & -1 & 5 & a & 0\\
    0 & -4 & 45 & 104 & 1
\end{pmatrix}$$

Row echelon form:

$$\begin{pmatrix}
    1 & 8 & -88 & 200 & 0\\
    0 & 1 & -12 & 30 & 0\\
    0 & 0 & -2 & 10 & 0\\
    0 & 0 & -7 & a + 30 & 0\\
    0 & 0 & -3 & 224 & 1
\end{pmatrix}$$

$$\begin{pmatrix}
    1 & 8 & -88 & 200 & 0\\
    0 & 1 & -12 & 30 & 0\\
    0 & 0 & -7 & a + 30 & 0\\
    0 & 0 & 0 & -\frac{2}{7}(a-5) & 0\\
    0 & 0 & 0 & \diamond(a) & 1
\end{pmatrix}$$

> Here we have some kinda value $\diamond(a)$ that depends on $a$ that I was too lazy to calculate since the next form is

$$\begin{pmatrix}
    1 & 8 & -88 & 200 & 0\\
    0 & 1 & -12 & 30 & 0\\
    0 & 0 & -7 & a + 30 & 0\\
    0 & 0 & 0 & -\frac{2}{7}(a-5) & 0\\
    0 & 0 & 0 & 0 & 1
\end{pmatrix}$$

Determinant of a row echelon form is equal to the product of the values on the diagonal, and since there are no zeros, $\det(v^{(i)})\neq0$ and the **set of vectors $v_i \ \forall i=1\dots5$ is the basis.** 

## Problem 4

Subspace $U\subseteq\mathbb{R}^5$ is defined as a linear combination of vectors

$$v_1=\begin{pmatrix}
    19\\
    14\\
    27\\
    10\\
    28
\end{pmatrix} \ \ v_2=\begin{pmatrix}
    -14\\
    -7\\
    -15\\
    3\\
    -13
\end{pmatrix} \ \ v_3=\begin{pmatrix}
    -1\\
    -6\\
    -2\\
    -5\\
    -4
\end{pmatrix} \ \ v_4=\begin{pmatrix}
    -13\\
    -9\\
    -20\\
    -9\\
    -21\\
\end{pmatrix}$$

### Subproblem A

Choose a basis in $U$ out of these vectors.

---

As per usual, the row echelon form $(v_3, v_1, v_2, v_4)$:

$$\begin{pmatrix}
    -1 & 19 & -14 & -13\\
    -6 & 14 & -7 & -9\\
    -2 & 27 & -15 & -20\\
    -5 & 10 & 3 & -9\\
    -4 & 28 & -13 & -21\\
\end{pmatrix}$$

$$\begin{pmatrix}
    -1 & 19 & -14 & -13\\
    0 & -100 & 77 & 69\\
    0 & -11 & 13 & 6\\
    0 & -85 & 73 & 56\\
    0 & -48 & 43 & 31\\
\end{pmatrix}$$

$$\begin{pmatrix}
    -1 & 19 & -14 & -13\\
    0 & -100 & 77 & 69\\
    0 & 0 & 7.55 & -2.65\\
    0 & 0 & 4.53 & -1.59\\
    0 & 0 & 6.04 & -2.12\\
\end{pmatrix}$$

$$\begin{pmatrix}
    -1 & 19 & -14 & -13\\
    0 & -100 & 77 & 69\\
    0 & 0 & 7.55 & -2.65\\
    0 & 0 & 4.53 & -1.59\\
    0 & 0 & 6.04 & -2.12\\
\end{pmatrix}$$

> All three last rows are proportional to each other!

$$\begin{pmatrix}
    -1 & 19 & -14 & -13\\
    0 & -100 & 77 & 69\\
    0 & 0 & 7.55 & -2.65\\
    0 & 0 & 0 & 0\\
    0 & 0 & 0 & 0\\
\end{pmatrix}$$

Thus, we get that the first three $(v_3, v_1, v_2)$ vectors form a basis.

### Subproblem B

Out of vectors 

$$u_1=\begin{pmatrix}
    3\\
    -13\\
    1\\
    -14\\
    -5
\end{pmatrix} \ \ u_2=\begin{pmatrix}
    -13\\
    2\\
    -16\\
    6\\
    -12
\end{pmatrix}$$

choose those which lie within the span $U$ and find their composition in the found basis.

---

We need to just solve $Ax=u_i$ for each of the vectors and a matrix $(A|u_i)=(v^{(3)}, v^{(1)}, v^{(2)}|u_i)$:

#### First vector

$$\begin{pmatrix}
    -1 & 19 & -14 & \bigm| & 3\\
    -6 & 14 & -7 & \bigm| & -13\\
    -2 & 27 & -15 & \bigm| & 1\\
    -5 & 10 & 3 & \bigm| & -14\\
    -4 & 28 & -13 & \bigm| & -5\\
\end{pmatrix}$$

$$\begin{pmatrix}
    -1 & 19 & -14 & \bigm| & 3\\
    0 & -100 & 77 & \bigm| & -31\\
    0 & -11 & 13 & \bigm| & 5\\
    0 & -85 & 73 & \bigm| & -29\\
    0 & -48 & 43 & \bigm| & -17\\
\end{pmatrix}$$

$$\begin{pmatrix}
    -1 & 19 & -14 & \bigm| & 3\\
    0 & -100 & 77 & \bigm| & -31\\
    0 & 0 & 151 & \bigm| & -53\\
    0 & 0 & 0 & \bigm| & 0\\
    0 & 0 & 0 & \bigm| & 0\\
\end{pmatrix}$$

Now actually get the solution out of the system:

$$\begin{cases}
    -x_3+19x_1-14x_2=3\\
    -100x_1+77x_2=-31\\
    151x_2=-53
\end{cases}$$

$$\begin{cases}
    x_3=\frac{403}{151}\\
    x_1=\frac{6}{151}\\
    x_2=-\frac{53}{151}
\end{cases}$$

Finally,

$$u_1=\frac{1}{151}(6v_1-53v_2+403v_3)$$

#### Second vector

$$\begin{pmatrix}
    -1 & 19 & -14 & \bigm| & -13\\
    -6 & 14 & -7 & \bigm| & 2\\
    -2 & 27 & -15 & \bigm| & -16\\
    -5 & 10 & 3 & \bigm| & 6\\
    -4 & 28 & -13 & \bigm| & -12\\
\end{pmatrix}$$

$$\begin{pmatrix}
    -1 & 19 & -14 & \bigm| & -13\\
    0 & -100 & 77 & \bigm| & 80\\
    0 & -11 & 13 & \bigm| & 10\\
    0 & -85 & 73 & \bigm| & 71\\
    0 & -48 & 43 & \bigm| & 40\\
\end{pmatrix}$$

$$\begin{pmatrix}
    -1 & 19 & -14 & \bigm| & -13\\
    0 & -100 & 77 & \bigm| & 80\\
    0 & 0 & 453 & \bigm| & 120\\
    0 & 0 & 0 & \bigm| & 1\\
    0 & 0 & 151 & \bigm| & 40\\
\end{pmatrix}$$

**This system of equations has no solutions.**

## Problem 5

Find the basis and dimension of the subspace $U\subseteq \mathbb{R}^5$, which is the set of all solutions to the following system:

$$\begin{cases}
    6x_1-3x_2+2x_3-5x_4-x_5=0\\
    9x_1+2x_2+9x_3-19x_4-4x_5=0\\
    10x_1-4x_2+6x_3-18x_4-4x_5=0\\
    14x_1+x_2+9x_3-12x_4-2x_5=0
\end{cases}$$

As per usual, row echelon form and gaussian elimination $(x^{(5)},x^{(3)},x^{(2)},x^{(4)},x^{(1)})$:

$$\begin{pmatrix}
    -1 & 2 & 3 & -5 & 6\\
    -4 & 9 & 2 & -19 & 9\\
    -4 & 6 & -4 & -18 & 10\\
    -2 & 9 & 1 & -12 & 14\\
\end{pmatrix}$$

$$\begin{pmatrix}
    -1 & 2 & 3 & -5 & 6\\
    0 & 1 & 14 & 1 & -15\\
    0 & -2 & 8 & 2 & -14\\
    0 & 5 & 7 & -2 & 2\\
\end{pmatrix}$$

$$\begin{pmatrix}
    -1 & 2 & 3 & -5 & 6\\
    0 & 1 & 14 & 1 & -15\\
    0 & 0 & 36 & 4 & -4\\
    0 & 0 & -63 & -7 & 77\\
\end{pmatrix}$$

$$\begin{pmatrix}
    -1 & 2 & 3 & -5 & 6\\
    0 & 1 & 14 & 1 & -15\\
    0 & 0 & 9 & 1 & -11\\
    0 & 0 & 0 & 0 & 0\\
\end{pmatrix}$$

$$\begin{cases}
    -x_5+2x_3-3x_2-5x_4+6x_1=0\\
    x_3+14x_2+x_4-15x_1=0\\
    9x_2+x_4-11x_1=0\\
\end{cases}$$

$$\begin{cases}
    x_5=-\frac{32}{9}x_4-\frac{17}{9}x_1\\
    x_3=\frac{5}{9}x_4-\frac{19}{9}x_1\\
    x_2=-\frac{1}{9}x_4+\frac{11}{9}x_1\\
\end{cases}$$

Establish a fundamental system of solutions:

|$x_1$|$x_2$|$x_3$|$x_4$|$x_5$|
|:-:|:-:|:-:|:-:|:-:|
| $1$ | $\frac{11}{9}$ | $-\frac{19}{9}$ | $0$ | $-\frac{17}{9}$ |
| $0$ | $-\frac{1}{9}$ | $\frac{5}{9}$ | $1$ | $-\frac{32}{9}$ |

Thus, **the basis** would consist of two vectors:

$$e_1=\begin{pmatrix}
    1\\
    \frac{11}{9}\\
    -\frac{19}{9}\\
    0\\
    -\frac{17}{9}\\
\end{pmatrix} \text{and} \ e_2=\begin{pmatrix}
    0\\
    -\frac{1}{9}\\
    \frac{5}{9}\\
    1\\
    -\frac{32}{9}\\
\end{pmatrix}$$

The **dimension** of the resulting set would be equal to the number of basis vectors. Thus, $U\in\mathbb{R}^2$ and $\text{dim}\ U=2$.