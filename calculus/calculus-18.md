# Calculus, Homework 18

## Problem 1

> Integrate (if possible)

### Subproblem 1

$$\int(2x^2+1)^3dx=\int(8x^6+12x^4+6x^2+1)dx=$$

$$8\int x^6dx+12\int x^4dx + 6\int x^2dx+\int dx=$$

$$\frac{8}{7}x^7+\frac{12}{5}x^5+2x^3+x+С$$

### Subproblem 2

$$\int(1+\sqrt{x})^4dx\xRightarrow{u=\sqrt{x},\ du=\frac{dx}{2\sqrt{x}},\ x=u^2,\ dx=2\sqrt{x}du}2\int u(1+u)^4dx$$

$$\xRightarrow{u=s-1,\ ds=du}2\int(s-1)s^4ds=2\int s^5ds+2\int s^4ds=$$

$$\frac{s^6}{3}-\frac{2}{5}s^5+C=\frac{(u+1)^6}{3}-\frac{2}{5}(u+1)^5+С=$$

$$\frac{(\sqrt{x}+1)^6}{3}-\frac{2}{5}(\sqrt{x}+1)^5+С=\frac{1}{15}(\sqrt{x}+1)^5(5\sqrt{x}-1)+С$$

### Subproblem 3

$$\int\frac{(x+1)(x^2-3)}{3x^2}dx=\frac{1}{3}\int\frac{x^3-3x+x^2-3}{x^2}dx=$$

$$\frac{1}{3}\int\left(x-\frac{3}{x}+1-\frac{3}{x^2}\right)dx=\frac{1}{3}\left(\int xdx-\int\frac{3dx}{x}+\int dx-\int\frac{3dx}{x^2}\right)=$$

$$\frac{1}{3}\left(\frac{x^2}{2}-3\ln x+x+\frac{3}{x}\right) = \frac{x^{2}}{6} + \frac{x}{3} - \ln{(x)} + \frac{1}{x}+С$$

### Subproblem 4

$$\int\frac{dx}{\sqrt{a^2-x^2}}=\frac{1}{a}\int\frac{dx}{\sqrt{1-\frac{x^2}{a^2}}}\xRightarrow{u=\frac{x}{a},\ x=au,\ du=\frac{dx}{a},\ dx=adu}$$

$$\int\frac{du}{\sqrt{1-u^2}}=\arcsin u=\arcsin\left(\frac{x}{a}\right)+С$$

### Subproblem 5

> Honestly the only idea that came to mind is to somehow factor out the minus using imaginary numbers as well to get the $\arctan$, which appears to have actually worked

$$\int\frac{1}{x^2-a}dx=-\frac{1}{a}\int\frac{1}{1+i^2\frac{x^2}{\sqrt{a}^2}}dx\xRightarrow{u=\frac{ix}{\sqrt{a}},\ x=\frac{\sqrt{a}u}{i},\ du=\frac{i}{\sqrt{a}}dx,\ dx=\frac{\sqrt{a}}{i}du}$$

$$-\frac{i}{\sqrt{a}}\int\frac{1}{1+u^2}du = - \frac{i {\arctan{u}}}{\sqrt{a}}+С$$

### Subproblem 6

> Sorry, no tex-ed long division

$$\int\frac{x^3+2x^2-3x+10}{x+4}dx=\int\left(x^2-2x+5+\frac{10}{x+4}\right)dx=$$

$$\int x^2dx-\int 2xdx+\int 5dx+\int\frac{10}{x+4}dx=$$

$$\frac{x^{3}}{3}- x^{2}+5 x+10 \ln{(x + 4)}+С$$

### Subproblem 7

$$\int\frac{e^xdx}{\sqrt{1-e^{2x}}}\xRightarrow{u=e^x,\ du=e^xdx,\ dx=\frac{du}{e^x}}$$

$$\int\frac{du}{\sqrt{1-u^2}}=\arcsin u=\arcsin e^x+С$$

### Subproblem 8

$$\int xe^{x^2}dx\xRightarrow{u=x^2,\ du=2xdx}\frac{1}{2}\int e^udu=\frac{e^u}{2}+С=\frac{e^{x^2}}{2}+С$$

### Subproblem 9

> Let's try to rewrite this in a tangent form using the formulas $\sin x=\frac{2\tg\frac{x}{2}}{\tg^2 \frac{x}{2}+1}, \cos x =\frac{1-\tg^2\frac{x}{2}}{\tg^2\frac{x}{2}+1}$

$$\int\frac{dx}{1+\sin(x)}=\int\frac{dx}{1+\frac{2\tg \frac{x}{2}}{\tg^2 \frac{x}{2}+1}}=\int\frac{dx}{\frac{\tg^2 \frac{x}{2}+2\tg \frac{x}{2}+1}{\tg^2 \frac{x}{2}+1}}$$

$$\xRightarrow{u=\tg\frac{x}{2},\ du=\frac{1}{2\cos^2\frac{x}{2}}dx,\ dx=\frac{2du}{u^2+1}}2\int\frac{\frac{du}{u^2+1}}{\frac{u^2+2u+1}{u^2+1}}=$$

$$2\int\frac{du}{(u+1)^2}\xRightarrow{s=u+1,ds=du}2\int\frac{du}{s^2}=-\frac{2}{s}+С=$$

$$-\frac{2}{u+1}+С=-\frac{2}{\tg\frac{x}{2}+1}$$


### Subproblem 10

$$\int\frac{x^3dx}{x^8+2}\xRightarrow{u=x^4,\ du=4x^3dx}\frac{1}{4}\int\frac{du}{u^2+2}=\frac{1}{8}\int\frac{du}{\frac{u^2}{2}+1}=$$

$$\xRightarrow{s=\frac{u}{\sqrt{2}},\ ds=\frac{1}{\sqrt{2}}du}\frac{1}{4\sqrt{2}}\int\frac{ds}{s^2+1}=$$

$$\frac{\arctan s}{4\sqrt{2}}+С=\frac{\arctan \frac{u}{\sqrt{2}}}{4\sqrt{2}}+С=\frac{\arctan \frac{x^4}{\sqrt{2}}}{4\sqrt{2}}+С$$

### Subproblem 11

> Kinda cheaty way, but it's literally a table integral of a cosecant >:)

$$\int\frac{dx}{\sin(x)}=\int\csc x dx=\ln\tg\frac{x}{2}$$

### Subproblem 12

Consider $1$-form $\omega$ depending on parameters $a,b,c,d\in\mathbb{R}$ and integrate it.

> Strategy: first integrate the form, and then see whether the resulting expression is undefined

#### Subsubproblem A

$$\omega=\frac{ax+b}{cx+d}dx,\quad c\neq d\neq0$$

---

$$\int\frac{ax+b}{cx+d}dx=\int\frac{bc-ad}{c(cx+d)}dx+\int\frac{a}{c}dx=$$

$$\left(b-\frac{ad}{c}\right)\int\frac{dx}{cx+d}+\frac{ax}{c}+С\xRightarrow{u=cx+d,\ du=cdx}$$

$$\left(b-\frac{ad}{c}\right)\frac{1}{c}\int\frac{du}{u}+\frac{ax}{c}+С=$$

$$\left(\frac{b}{c}-\frac{ad}{c^2}\right)\ln(cx+d)+\frac{ax}{c}+С$$

The expression above is true for $c\neq0$, now when $c=0$:

$$\int\frac{ax+b}{d}dx=\frac{ax^2+2bx}{2d}+С$$

Answer:

$$\int\omega=\begin{cases}
    \left(\frac{bc-ad}{c^2}\right)\ln(cx+d)+\frac{ax}{c}+С\quad c\neq0\\
    \frac{ax^2+2bx}{2d}+С,\qquad\qquad\qquad\quad\ \, c=0
\end{cases}$$

#### Subsubproblem B

$$\omega=\frac{ax^3+bx^2+cx+d}{x^2+1}dx, \quad x\neq i$$

---

$$\int\frac{ax^3+bx^2+cx+d}{x^2+1}dx=\int\frac{-ax-b+cx+d}{x^2+1}dx+\int axdx+\int bdx=$$

$$=(c-a)\int\frac{x}{x^2+1}dx+(d-b)\int\frac{1}{x^2+1}dx+a\int xdx+b\int dx=$$

$$=\frac{c-a}{2}\ln(x^2+1)+(d-b)\arctg x+\frac{ax^2}{2}+bx+С$$

> No interesting variations here

#### Subsubproblem C

$$\omega=\frac{dx}{ax^2+bx+c},\quad a\neq b\neq c\neq 0$$

---

$$\int\frac{dx}{ax^2+bx+c}={\Large\int}\frac{dx}{\frac{4ac-b^2}{4a}+\left(\frac{b}{2\sqrt{a}}+\sqrt{a}x\right)^2}$$

$$\xRightarrow{u=\frac{b}{2\sqrt{a}}+\sqrt{ax},\ du=\sqrt{a}dx}\frac{1}{\sqrt{a}}{\Large\int}\frac{du}{\frac{4c-b^2}{4a}+u^2}=$$

$$\frac{4\sqrt{a}}{4ac-b^2}{\Large\int}\frac{1}{\frac{4a}{4ac-b^2}u^2+1}\xRightarrow{s=\frac{2\sqrt{a}u}{\sqrt{4ac-b^2}},\ ds=\frac{2\sqrt{a}}{\sqrt{4ac-b^2}}du}$$

$$\frac{2}{\sqrt{4ac-b^2}}\int\frac{1}{s^2+1}ds=\frac{2\arctg s}{\sqrt{4ac-b^2}}+С=$$

$$\frac{2\arctg \frac{2\sqrt{a}u}{\sqrt{4ac-b^2}}}{\sqrt{4ac-b^2}}+С=\frac{2\arctg \frac{2\sqrt{a}(\frac{b}{2\sqrt{a}}+\sqrt{ax})}{\sqrt{4ac-b^2}}}{\sqrt{4ac-b^2}}+С=$$

$$\frac{2\arctg \frac{2ax+b}{\sqrt{4ac-b^2}}}{\sqrt{4ac-b^2}}+С$$

This is valid for $4ac\neq b^2$. Now, for $b=\plusmn2\sqrt{ac}:$

$$\int\frac{dx}{(\sqrt{a}x\plusmn\sqrt{c})^2}=$$

$$\frac{1}{\sqrt{a}}\int\frac{1}{(\sqrt{a}x\plusmn\sqrt{c})^2}d(\sqrt{a}x\plusmn\sqrt{c})=-\frac{1}{ax\plusmn\sqrt{ac}}+С$$

Now, what if $a=0$?

$$\int\frac{dx}{bx+c}dx=\frac{1}{b}\int\frac{1}{bx+c}d(bx+c)=\frac{\ln(bx+c)}{b}+С$$

Finally, what if $a=b=0$?

$$\int\frac{dx}{c}=\frac{x}{c}+С$$

Answer:

$$\int\omega=\begin{cases}
    -\frac{1}{ax\plusmn\sqrt{ac}}+С,\qquad\,\ b=\plusmn 2\sqrt{ac}\\
    \frac{\ln(bx+c)}{b}+С,\qquad\quad a=0\\
    \frac{x}{c}+С,\qquad\qquad\quad\ a=b=0\\
    \frac{2\arctg \frac{2ax+b}{\sqrt{4ac-b^2}}}{\sqrt{4ac-b^2}}+С,\quad \text{otherwise}
\end{cases}$$