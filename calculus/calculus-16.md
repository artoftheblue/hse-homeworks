# Calculus, Homework 16

## Problem 1

Determine whether series $(x_n), (y_n), (z_n)$ converge:

$$x_n=\frac{n^2}{2^{n-1}},\quad y_n=\left(\frac{n+1}{8n-1}\right)^n,\quad z_n=nz^{n-1},\ z>0$$

---

d'Alembert criteria:

$$x_n=\frac{n^2}{2^{n-1}},\quad x_{n+1}=\frac{(n+1)^2}{2^{n}}$$

$$\lim_{n\to\infty}\frac{x_{n+1}}{x_n}=\lim_{n\to\infty}\frac{(n+1)^2}{2^{n}}\frac{2^{n-1}}{n^2}=\lim_{n\to\infty}\frac{(1+\frac{1}{n})^2}{2}=\frac{1}{2}$$

which implies that the series converges.

---

$$y_n=\left(\frac{n+1}{8n-1}\right)^n,\quad y_{n+1}=\left(\frac{n+2}{8n+7}\right)^{n+1}$$

$$\lim_{n\to\infty}\frac{y_{n+1}}{y_n}=\lim_{n\to\infty}\left(\frac{n+2}{8n+7}\right)^{n+1}\left(\frac{8n-1}{n+1}\right)^n=$$

$$\lim_{n\to\infty}\left(\frac{1+\frac{2}{n}}{8+\frac{7}{n}}\right)^{n+1}\left(\frac{8-\frac{1}{n}}{1+\frac{1}{n}}\right)^n=\lim_{n\to\infty}\left(\frac{1+\frac{2}{n}}{8+\frac{7}{n}}\right)\times1=\frac{1}{8}$$

which also implies the series converges.

---

$$z_n=nz^{n-1},\quad z_{n+1}=(n+1)z^n$$

$$\lim_{n\to\infty}\frac{z_{n+1}}{z_n}=\lim_{n\to\infty}\frac{(n+1)z^n}{nz^{n-1}}=\lim_{n\to\infty}\frac{(1+\frac{1}{n})z^n}{z^{n-1}}=\lim_{n\to\infty}\frac{z^n}{z^{n-1}}=z$$

which implies that the series converges if $z<1$ and diverges if $z\geq1$. The series diverges if $z=1$ since we get a series of we get a series $(n)$ which is a sequence of all natural numbers, which diverges.

## Problem 2

Using the radical Cauchy criteria, determine whether series $(x_n)$ converges:

$$x_n=\frac{x^n}{a_n},\quad n\geq 1$$

where $x>0$ and $(a_n)$ is a sequence of positive numbers with a limit $\lim_{n\to\infty}a_n=a$.

---

$$\lim_{n\to\infty}\sqrt[n]{x_n}=\lim_{n\to\infty}\sqrt[n]{\frac{x^n}{a_n}}=\lim_{n\to\infty}\frac{x}{\sqrt[n]{a_n}}=\lim_{n\to\infty}\frac{x}{\sqrt[n]{a}}=x$$

which implies the series converges if $x < 1$ and diverges if $x > 1$. As for $x=1$, the series also diverges since we would approach a sum larger than $\frac{1}{a}$, which itself diverges.

## Problem 3

Using the d'Alembert criteria, determine whether series $(x_n)$ converges, where

$$x_n=\frac{(nx)^n}{n!},\quad x>0, n\geq 0$$

---

$$x_n=\frac{(nx)^n}{n!},\quad x_{n+1}=\frac{((n+1)x)^{n+1}}{(n+1)!}$$

$$\lim_{n\to\infty}\frac{x_{n+1}}{x_n}=\lim_{n\to\infty}\frac{((n+1)x)^{n+1}}{(n+1)!}\frac{n!}{(nx)^n}=\lim_{n\to\infty}\frac{(n+1)^nx}{n^n} = \lim_{n\to\infty}\left(1+\frac{1}{n}\right)^nx=e x$$

which implies the series converges if $x<\frac{1}{e}$, diverges if $x>\frac{1}{e}$ and is indeterminable through d'Alembert if $x=\frac{1}{e}$.

## Problem 4

Consider series $(x_n)$ where

$$x_n=(ab)^n,\quad n\geq 0$$

and $a,b$ are two different positive numbers. Using the radical Cauchy criteria and d'Alembert's criteria determine whether the series converges.

---

d'Alembert:

$$x_n=(ab)^n,\quad x_{n+1}=(ab)^{n+1}$$

$$\lim_{n\to\infty}\frac{x_{n+1}}{x_n}=\lim_{n\to\infty}\frac{(ab)^{n+1}}{(ab)^n}=ab$$

which implies that the series converges when $ab<1$ and diverges when $ab\geq1$ (diverges when it is equal to one since then we get a sequence of ones, which diverges).

Cauchy:

$$\lim_{n\to\infty}\sqrt[n]{x_n}=\lim_{n\to\infty}\sqrt[n]{(ab)^n}=ab$$

implies the same.

## Problem 5

Let $0<r<1,\alpha\in\mathbb{R}$. Prove using the radical Cauchy criteria that series $(x_n)$ where 

$$x_n=r^n|\sin(n\alpha)|,n\geq 1$$

converges.

Is it possible to prove the convergence of this series using the d'Alembert's criteria?

---

$$\lim_{n\to\infty}\sqrt[n]{x_n}=\lim_{n\to\infty}\sqrt[n]{r^n|\sin(n\alpha)|}=r\lim_{n\to\infty}\sqrt[n]{|\sin(n\alpha)|}<0$$

which implies that the series converges since $r<1,|\sin(n\alpha)|\leq1$.

---

$$x_n=r^n|\sin(n\alpha)|,\quad x_{n+1}=r^{n+1}|\sin((n+1)\alpha)|$$

$$\lim_{n\to\infty}\frac{x_{n+1}}{x_n}=\lim_{n\to\infty}\frac{r^{n+1}|\sin((n+1)\alpha)|}{r^{n}|\sin(n\alpha)|} =r\lim_{n \to \infty}\left|{\frac{\sin{(\alpha (n + 1))}}{\sin{(\alpha n)}}}\right|$$

the sine division is indeterminable so no, I don't think it's possible to prove this using d'Alembert's unless we use some ridiculous substitution.

## Problem 6

Consider series $(x_n)$ where

$$x_n=\frac{1}{n!}\left(\frac{n}{e}\right)^n,\quad n\geq 1$$

using Raabe's criterion, determine the convergence of this series.

---

Raabe's criterion tells us that the series $(x_n)$ converges if for large enough $n$ the following is true:

$$n\left(\frac{x_n}{x_{n+1}}-1\right)>1$$

$$x_n=\frac{1}{n!}\left(\frac{n}{e}\right)^n,\quad x_{n+1}=\frac{1}{(n+1)!}\left(\frac{n+1}{e}\right)^{n+1}$$

$$\lim_{n\to\infty}\left(\frac{n}{n!}\left(\frac{n}{e}\right)^n\frac{(n+1)!}{1}\left(\frac{e}{n+1}\right)^{n+1}-n\right)=\lim_{n\to\infty}\left(\frac{nn^n(n+1)!e^{n+1}}{n!e^n(n+1)^{n+1}}-n\right)=$$

$$\lim_{n\to\infty}\left(\frac{n^{n+1}(n+1)e}{(n+1)^{n+1}}-n\right)=\lim_{n\to\infty}\left(\frac{n^{n+1}e}{(n+1)^n}-n\right)=\lim_{n\to\infty}\left(\frac{ne}{(1+\frac{1}{n})^n}-n\right)=$$

$$\lim_{n\to\infty}\left(\frac{ne-n(1+\frac{1}{n})^n}{(1+\frac{1}{n})^n}\right)=\frac{1}{2}$$

> originally I made an assumption that this limit is zero although it isn't somehow

which implies that the series diverges.


## Problem 7

Consider series $(x_n)$, where 

$$x_n=\frac{n!x^n}{(x+a_1)(2x+a_2)\cdots(nx+a_n)},\quad n\geq 1, x>0$$

and $(a_n)$ is a sequence of positive numbers with a limit of $\lim_{n\to\infty}a_n=a$. Using Raabe's criteria, determine the convergence of this series.

---

$$n\left(\frac{x_n}{x_{n+1}}-1\right)>1$$

$$x_n=\frac{n!x^n}{(x+a_1)(2x+a_2)\cdots(nx+a_n)}$$

$$x_{n+1}=\frac{(n+1)!x^{n+1}}{(x+a_1)(2x+a_2)\cdots(nx+a_n)((n+1)x+a_{n+1})}$$

$$\lim_{n\to\infty}n\left(\frac{n!x^n}{(x+a_1)(2x+a_2)\cdots(nx+a_n)}\frac{(x+a_1)(2x+a_2)\cdots(nx+a_n)((n+1)x+a_{n+1})}{(n+1)!x^{n+1}}-1\right)=$$

$$=\lim_{n\to\infty}n\left(\frac{n!x^n((n+1)x+a_{n+1})}{(n+1)!x^{n+1}}-1\right)=\lim_{n\to\infty}\left(n\frac{((n+1)x+a)}{x(n+1)}-1\right)=$$

$$=\lim_{n\to\infty}n\left(\left(1+\frac{a}{x(n-1)}\right)-1\right) = \frac{a}{x}$$

which implies that the series diverges when $\frac{a}{x}<1$ and converges when $\frac{a}{x}>1$.