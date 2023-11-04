# Calculus Homework #6

## Problem 8.8

> In general, to prove that the two-variable limit does not exist, it is enough to find two different limits for two different paths.

### Subproblem A

$$\displaystyle \lim_{\substack{x\to0\\ y\to0}}\frac{x^3-y}{x^3+y}$$

---

For $y=mx^3$:

$$\lim_{x\to0}\frac{x^3-m^3x^3}{x^3+m^3x^3}=\lim_{x\to0}\frac{1-m^3}{1+m^3}=\frac{1-m^3}{1+m^3}$$

The limit is dependent on $m \Rightarrow$ the limit does not exist.

### Subproblem B

$$\displaystyle \lim_{\substack{x\to0\\ y\to0}}\frac{xy}{x^2+y^2}$$

---

For $y=mx$:

$$\lim_{x\to0}\frac{x\cdot mx}{x^2+m^2x^2}=\lim_{x\to0}\frac{mx^2}{(1+m^2)x^2}=\lim_{x\to0}\frac{m}{1+m^2}=\frac{m}{1+m^2}$$

The limit is dependent on $m \Rightarrow$ the limit does not exist.

### Subproblem C

$$\displaystyle \lim_{\substack{x\to0\\ y\to0}}\frac{y^2-x^2}{y^2+x^2}$$

---

For $y=mx$:

$$\lim_{x\to0}\frac{m^2x^2-x^2}{m^2x^2+x^2}=\lim_{x\to0}\frac{m^2-1}{m^2+1}=\frac{m^2-1}{m^2+1}$$

The limit is dependent on $m \Rightarrow$ the limit does not exist.

### Subproblem D

$$\displaystyle \lim_{\substack{x\to0\\ y\to0}}\frac{x^2y^2}{x^2y^2+(x-y)^2}$$

---

For $y=x$:

$$\lim_{x\to0}\frac{x^2x^2}{x^2x^2+(x-x)^2}=\lim_{x\to0}\frac{x^4}{x^4}=\lim_{x\to0}1=1$$

For $y=0$:

$$\lim_{x\to0}\frac{x^20^2}{x^20^2+(x-0)^2}=\lim_{x\to0}\frac{0}{x^2}=\lim_{x\to0}0=0$$

There are at least two different limits for two paths $y=x, y=0 \Rightarrow$ the limit does not exist.

### Subproblem E

$$\lim_{\substack{x\to0\\ y\to0}}\left(x+y\sin\frac{1}{x}\right)$$

---

$f_1(x)=\sin\frac{1}{x} \in [-1, 1]$ is a bounded function. $f_2(y)=y$ as $y\to0$ is an infinitesimal function. Product of a bounded function and an infinitesimal function is infinitesimal. Therefore, $\lim_{\substack{x\to0\\ y\to0}}g(x,y)=\lim_{\substack{x\to0\\ y\to0}}f_1(x)f_2(y)=0$

$$\lim_{\substack{x\to0\\ y\to0}}\left(x+y\sin\frac{1}{x}\right)=\lim_{\substack{x\to0\\ y\to0}}x+\lim_{\substack{x\to0\\ y\to0}}y\sin\frac{1}{x}=\lim_{x\to0}x+\lim_{\substack{x\to0\\ y\to0}}g(x,y)=0 + 0 = 0$$

Answer: 

$$\lim_{\substack{x\to0\\ y\to0}}\left(x+y\sin\frac{1}{x}\right)=0$$

## Problem 8.9

Find limit of $f(x,y) = \frac{y-2x^2}{y-x^2}$ in point $(0,0)$ along the path $x=\alpha t, y=\beta t, \alpha^2+\beta^2\neq 0$. Prove that $\lim_{\substack{x\to0\\ y\to0}}f(x,y)$ does not exist.

---

$$\lim_{\substack{x\to0\\ y\to0}}\frac{y-2x^2}{y-x^2}\Rightarrow\lim_{t\to0}\frac{\beta t-2\alpha^2t^2}{\beta t-\alpha^2t^2}=\lim_{t\to0}\frac{\beta - 2\alpha^2t}{\beta-\alpha^2t}=\lim_{t\to0}\frac{\beta-0}{\beta-0}=\lim_{t\to0}1=1$$

For $y = mx^2$:

$$\lim_{x\to0}\frac{mx^2-2x^2}{mx^2-x^2}=\lim_{x\to0}\frac{m-2}{m}=\frac{m-2}{m}$$

Thus, the multivariable limit does not exist.

Answer: $\lim_{\substack{x\to0\\ y\to0}}\frac{y-2x^2}{y-x^2}=1$ along the path of $x=\alpha t, y=\beta t, \alpha^2+\beta^2\neq 0$

## Problem 8.10

Is the function 

$$u(x,y)=\begin{cases}
\begin{split}
    \displaystyle\frac{xy}{x^2+y^2}, &\forall x,y\colon x^2+y^2\neq0\\
    0, \ \ \ \ \ \ &\forall x,y\colon x^2+y^2=0
\end{split}
\end{cases}$$

continuous in point $(0,0)$?

---

$$u'(x, y)=\frac{xy}{x^2+y^2}$$

Per the continuity criterion: for $u(x,y)$ to be continuous in point of closure $(0,0)$ it is required and sufficient that $u(0,0)=\lim_{\substack{x \to 0\\y\to0}}u'(x, y).$ This limit of $u'(x,y)$, as proven in **Problem 8.8, Subproblem B** does not exist. Therefore, the function $u(x,y)$ is not continuous.

Answer: $u(x,y)$ is not continuous