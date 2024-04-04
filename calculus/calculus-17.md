# Calculus, Homework 17

## Problem 1

Using Largange's Theorem and the first comparison criteria, prove that the following series $(x_n)$ diverge:

> Honestly, I don't quite get the point of the task

### Subproblem A

$$x_n=\frac{1}{n^{1+\sigma}},\quad \sigma>0$$

---

We need to find some convergent series, the derivative for which is equal to the series below:

$$f(n+1)-f(n)=f'(n+\theta),\quad 0<\theta <1$$

Let:

$$f'(n+\theta)=\frac{1}{(n+\theta)^{\sigma+1}}>\frac{1}{n^{\sigma+1}}$$

This is eerily similar to integration, so:

$$\int\frac{dn}{n^{\sigma+1}}=-\frac{1}{\sigma n^\sigma}+C$$

Thus we have 

$$f(n)=-\frac{1}{\sigma n^\sigma}$$ 

and since for this series exists some number $N$, for which we can define 

$$y_n:=f(n+1)-f(n)$$

such that $\forall n>N$:

$$x_n<y_n$$

take

$$y_n=f(n+1)-f(n)$$

$$y_n=-\frac{1}{\sigma n^\sigma}+\frac{1}{\sigma n^\sigma\times n}=-\frac{1}{\sigma n^\sigma}\left(1-\frac{1}{n}\right)$$

This is a telescopic sum, so sum of $(y_n)$ would be

$$\frac{1}{\sigma}-\frac{1}{\sigma(n+1)^\sigma}$$

the limit of this is 

$$\lim_{n\to\infty}\left(\frac{1}{\sigma}-\frac{1}{\sigma(n+1)^\sigma}\right)=\frac{1}{\sigma}$$

thus this series converges since it has a non-infinite sum.

Now given that 

$$\left(\frac{1}{(n+\theta)^{\sigma+1}}\right)$$

can be treated similarly since we'd get another telescopic sum, then we know that the following series within our given conditions are almost similar:

$$\left(\frac{1}{(n+1)^{\sigma +1}}\right),\quad \left(\frac{1}{n^{\sigma +1}}\right)$$

Thus we may conclude that

$$\left(\frac{1}{n^{\sigma +1}}\right)$$

also converges per the first comparison criteria.

### Subproblem B

$$x_n=\frac{1}{n\ln n}$$

---

Consider 

$$f(x):=\ln(\ln(x))$$

on $[n, n+1]$ and since $f(x)$ is differentiable, we get that per Lagrange theorem 

$$\exists n+\theta\in(n, n+1),\quad 0<\theta<1$$

$$f(n+1)-f(n)=f'(n+\theta)\implies$$

$$\ln(\ln(n+1))-\ln(\ln(n))=\frac{1}{(n+\theta)\ln(n+\theta)}$$

Since we know that $n+\theta <n+1$, then 

$$y_n=\ln(\ln(n+1))-\ln(\ln(n))>\frac{1}{(n+1)\ln(n+1)}$$

which means that per the first comparison criteria we get that since $(y_n)$ diverges since telescopically we get a single expression that approaches infinity as $n$ approaches infinity, therefore the series

$$\left(\frac{1}{n\ln n}\right)$$

also diverges

## Problem 2

Determine absolute convergence of the following series $(x_n)$:

### Subproblem A

$$x_n=\frac{x^n}{n!}$$

--- 

Find d'Alembert's variant:

$$\mathfrak{D}_n=\frac{|x_{n+1}|}{|x_n|}=\frac{|x^{n+1}n!|}{|(n+1)!x^n|}=\left|\frac{x}{n+1}\right|$$

$$\lim_{n\to\infty}\mathfrak{D}_n=0\implies$$

the series converges absolutely $\forall x$.

### Subproblem B

$$x_n=xn^{n-1}$$

---

d'Alembert's variant:

$$\mathfrak{D}_n=\frac{|x_{n+1}|}{|x_n|}=\frac{|x(n+1)^{n}|}{|xn^{n-1}|}=\left(\frac{n+1}{n}\right)^n\times n$$

$$\lim_{n\to\infty}n\left(\frac{n+1}{n}\right)^n =\lim_{n\to\infty}n e=\infty\implies$$

the series diverges absolutely $\forall x$.

### Subproblem C

$$x_n=\frac{x^n}{n^s}, \quad s>0, x\neq -1$$

---

d'Alembert's variant:

$$\mathfrak{D}_n=\frac{|x^{n+1}|n^s}{(n+1)^s|x^n|}=|x|\left(\frac{n}{n+1}\right)^s=|x|\left(1+\frac{1}{n}\right)^s$$

$$\lim_{n\to\infty}|x|\left(1+\frac{1}{n}\right)^s = |x|$$

which implies that the series converges absolutely for $-1<x<1$ and diverges for $x>1\lor x<-1$. Additionally, when $x=\plusmn1$, the series converges absolutely if $s>1$ and diverges absolutely if $s\leq1$ since then it would be a Dirichet's series.

### Subproblem D

$$x_n=n!\frac{x^n}{n^n}$$

---

d'Alembert's variant:

$$\mathfrak{D}_n=\frac{|x_{n+1}|}{|x_n|}=\frac{|(n+1)!x^{n+1}n^n|}{|(n+1)^{n+1}n!x^n|}=\frac{|n!(n+1)x^{n+1}n^n|}{|(n+1)^n(n+1)n!x^n|}=|x|\left(\frac{n}{n+1}\right)^n$$

$$\lim_{n\to\infty}|x|\left(\frac{n}{n+1}\right)^n = \frac{|{x}|}{e}$$

which implies that the series converges absolutely for $-e<x<e$ and diverges absolutely for $x>e \lor x<-e$. In case when $x=\plusmn e$, we may use the limit test to determine whether the series diverges:

$$\lim_{n\to\infty}n!\frac{|e|^n}{n^n}=\lim_{n\to\infty}\left(\frac{|e|}{n}\times\frac{2|e|}{n}\times\dots\times\frac{(n-1)|e|}{n}\times\frac{n|e|}{n}\right)$$

We understand that from some $k$, $\displaystyle\frac{k|e|}{n}$ is greater than $1$. Therefore, this limit is equal to $\infty$ and the series diverges absolutely for $x=\plusmn e$.

### Subproblem E

$$x_n=\frac{(nx)^n}{n!}, \quad x\neq-\frac{1}{e}$$

---

d'Alembert's variant:

$$\mathfrak{D}_n=\frac{|x_{n+1}|}{|x_n|}=\frac{(n+1)^n(n+1)|x|^{n+1}n!}{n!(n+1)n^n|x|^n} = |{x}|\left(1+\frac{1}{n}\right)^n$$

$$\lim_{n\to\infty}|{x}|\left(1+\frac{1}{n}\right)^n=|x|e$$

which implies that the series converges for $\displaystyle-\frac{1}{e}<x<\frac{1}{e}$ and diverges absolutely for $\displaystyle x>\frac{1}{e}\lor x<-\frac{1}{e}$. We don't need to determine absolutely convergence for $\displaystyle x=-\frac{1}{e}$, so consider the case for $\displaystyle x=\frac{1}{e}$. Similarly to above, use the limit test:

$$\lim_{n\to\infty}\frac{n^n}{e^nn!}=\lim_{n\to\infty}\left(\frac{n}{e}\times\frac{n}{2e}\times\dots\times\frac{n}{(n-1)e}\times\frac{n}{ne}\right)$$

We understand that from some $k$, $\displaystyle\frac{n}{ke}$ is greater than $1$. Therefore, this limit is equal to $\infty$ and the series diverges absolutely for $x=\displaystyle \frac{1}{e}$.

### Subproblem F

$$x_n=\frac{x^n}{1-x}, \quad x\neq\plusmn1$$

---

d'Alembert's variant:

$$\mathfrak{D}_n=\frac{|x_{n+1}|}{|x_n|}=\frac{|x^{n+1}||1-x|}{|x||x^n|}=|1-x|$$

From here, it's obvious that the series converges for $|x|<1$ and diverges for $|x|>1$.