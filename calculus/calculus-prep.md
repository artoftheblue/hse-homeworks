## Problem 1

Estimate:

$$\frac{3n^3+n\sin(n^2)+\ln n}{n^3+n^2+\cos(n)}<\frac{3n^3+2n}{n^3-1}=3+\frac{2n+3}{n^3-1}<\varepsilon$$

Obviously, this is not true, but it would be true if the limit is equal to $3$, therefore

$$\frac{2n+3}{n^3-1}<\varepsilon$$

Very roughly estimating:

$$\frac{3}{n^2}<\varepsilon\Rightarrow N=\left\lfloor\sqrt{\frac{3}{\varepsilon}}\right\rfloor$$

## Problem 2

Find limits

### Subproblem A

$$\lim_{n\to\infty}\left(1+\frac{1}{n^2}\right)^n=\lim_{n\to\infty}\left(\left(1+\frac{1}{n^2}\right)^{n^2}\right)^\frac{1}{n}=\lim_{n\to\infty}e^{\frac{1}{n}}=e^0=1$$

### Subproblem B

$$\lim_{n\to\infty}\left(\sqrt{\frac{1}{n^2+1}}+\dots+\sqrt{\frac{1}{n^2+n}}\right)=\lim_{n\to\infty}\left(\sqrt{\frac{\frac{1}{n^2}}{1+\frac{1}{n^2}}}+\dots+\sqrt\frac{\frac{1}{n^2}}{1+k\frac{1}{n^2}}+\dots+\sqrt{\frac{\frac{1}{n^2}}{1+\frac{1}{n}}}\right)=$$

$$\sqrt{\frac{0}{1+0}}+\dots+\sqrt\frac{0}{1+k\times0}+\dots+\sqrt{\frac{0}{1+0}}=0+\dots+0+\dots+0=0$$

## Problem 3

$$x_{n+1}=x_n^2-x_n+1, \ \ \ \ \ x_1=\frac{1}{2}$$

First, prove that the sequence is bounded:

$$x^2_n-x_n+1=x_n(x_n-1)+1$$

Since $0<x_1<1$, then $-1<(x_n-1)<0$, $-1<x_n(x_n-1)<0$ and $0<x_n(x_n-1)+1<1 \Rightarrow \exists \sup\{x_n\},\inf\{x_n\}$.

Now assume that two consecutive elements are infinitely close to each other:

$$x=x^2-x+1$$

$$x^2-2x+1=0$$

$$(x-1)^2=0$$

$$x=1$$

Therefore, $\lim_{n\to\infty}\{x_n\}=1$

## Problem 4

Determine whether the sequence has a limit. Consider one element from the sum. Since we know that 

$$\lim_{n\to\infty}\sum^{n}_{k=1}\frac{1}{k}$$ 

doesn't exist and sums where $a > k$

$$\lim_{n\to\infty}\sum^{n}_{k=1}\frac{1}{a}$$ 

do exist, we may compare the two sums for $a=k^6$. We want

$$-\frac{1}{k^6}<\frac{\cos^3(k)}{1+k^6\cos^6(k)}<\frac{1}{k^6}$$

Is it always true?

$$-k^6>\frac{1}{\cos^3(k)}+k^6\cos^3(k)>k^6$$

$$-k^6>-1-k^6>\frac{1}{\cos^3(k)}+k^6>1+k^6>k^6$$

Therefore, it is always true and the limit does exist.

## Problem 5

Given path $x=y$

$$\lim_{\substack{x\to0\\y\to0}}\frac{y^2+y^3}{2y^2}=\frac{1+0}{2}=\frac{1}{2}$$

Given path $x=y^2$

$$\lim_{\substack{x\to0\\y\to0}}\frac{y^3+y^3}{y^4+y^2}=\lim_{\substack{x\to0\\y\to0}}\frac{2y^3}{y^2(y^2+1)}=\frac{2\times0}{0+1}=0$$

The limit does not exist.

## Problem 6

To determine this, calculate the following limit:

$$\lim_{\substack{x\to0\\y\to0}}\frac{\sin(xy)}{xy}=1$$

It is the same regardless of the path because it is literally one of the "wonderful" limits.

Since this limit exists and it is the same for all paths, and value in the point of closure $(0,0)$ is equal to the limit above, then the mapping $f(x,y)$ is **continuous** per the continuity criterion.

## Problem 7

### Subproblem A

$$\lim_{x\to3}\left(\frac{19-4x}{5x-8}\right)^{\frac{16-3x}{2x-6}}\xRightarrow{y=x+3}\lim_{y\to0}\left(\frac{19-4y-12}{5y+15-8}\right)^\frac{16-3y-9}{2y+6-6}=\lim_{y\to0}\left(\frac{7-4y}{7+5y}\right)^\frac{7-3y}{2y}=$$

$$\lim_{y\to0}\left(\frac{7-4y}{7+5y}\right)^\frac{7}{2y}=\lim_{y\to0}\left(1-\frac{9y}{7+5y}\right)^{\frac{7}{2y}}=\lim_{y\to0}\left(1-\frac{1}{\frac{7}{9y}+\frac{5}{9}}\right)^{\frac{7}{2y}}=$$

$$\lim_{y\to0}\left(1-\frac{1}{\frac{7}{9y}}\right)^{\frac{7}{2y}}\xRightarrow{\frac{1}{y}=z}\lim_{z\to\infty}\left(1-\frac{1}{\frac{7}{9}z}\right)^{\frac{7}{9}z\times\frac{9}{7}\times\frac{7}{2}}=\left(\frac{1}{e}\right)^\frac{9}{2}=e^{-\frac{9}{2}}$$

### Suproblem B

$$\lim_{x\to0}(1+\tan(x))^{\frac{1}{2x}}=\lim_{x\to0}\left(1+\frac{x\tan(x)}{x}\right)^{\frac{1}{2x}}=\lim_{x\to0}(1+x)^\frac{1}{2x}\xRightarrow{\textstyle x=\frac{1}{z}}$$

$$\lim_{z\to\infty}\left(1+\frac{1}{z}\right)^{z\times\frac{1}{2}}=\sqrt{e}$$