# Calculus, Homework 19

## Problem 1

Let $\omega_{k,m}=x^k\ln^m(x)$. Find the integral of this form for all $k, m$. (Present a recurrent formula).

$$\int x^k\ln^m(x)dx=\int_m$$

$$u=\ln^m(x), dv = x^kdx, du=m\ln^{m-1}(x)\frac{1}{x}dx, v=\frac{x^{k+1}}{k+1}$$

$$\frac{\ln^m(x)x^{k+1}}{k+1}-\int\frac{m\ln^{m-1}(x)x^{k+1}}{(k+1)x}dx=$$

$$\frac{\ln^m(x)x^{k+1}}{k+1}-\frac{m}{k+1}\int\ln^{m-1}(x)x^{k}dx$$

$$\int_m=\frac{\ln^m(x)x^{k+1}}{k+1}-\frac{m}{k+1}\int_{m-1}$$

$$\int_1=\int x^k\ln(x)dx$$

$$u=\ln(x), dv = x^kdx, du=\frac{1}{x}dx, v=\frac{x^{k+1}}{k+1}$$

$$\int_1=\frac{\ln(x)x^{k+1}}{k+1}+\frac{1}{k+1}\int x^kdx=\frac{\ln(x)x^{k+1}}{k+1}+\frac{x^{k+1}}{(k+1)^2}$$

## Problem 2

> Find the following integrals:

> Integration by parts formula for reference: $\displaystyle\int fdg=fg-\int gdf$

### Subproblem A

$$\int e^{ax}\sin(bx)dx$$

$$f=\sin (bx), df=b\cos(bx)dx, dg=e^{ax}dx, g = \frac{e^{ax}}{a}\implies$$

$$\frac{e^{ax}}{a}\sin(bx)-\int\frac{e^{ax}}{a}b\cos(bx)dx$$

$$f =\cos(bx), df=-b\sin(bx)dx, dg=e^{ax}dx, g=\frac{e^{ax}}{a}\implies$$

$$\frac{e^{ax}}{a}\sin(bx)-\frac{b}{a}\left(\frac{e^ax}{a}\cos(bx)+\frac{b}{a}\int e^{ax}\sin(bx)dx\right)$$

> We have arrived at the integral that we've started with, so we may express it out and arrive at the solution:

$$\frac{e^{ax}}{a}\sin(bx)-\frac{b}{a}\left(\frac{e^{ax}}{a}\cos(bx)+\frac{b}{a}\int e^{ax}\sin(bx)dx\right)=\int e^{ax}\sin(bx)dx$$

$$\left(\frac{b^2}{a^2}+1\right)\int e^{ax}\sin(bx)dx=\frac{e^{ax}}{a}\sin(bx)-\frac{be^{ax}}{a^2}\cos(bx)+C$$

$$\int e^{ax}\sin(bx)dx=\frac{\frac{e^{ax}}{a}\sin(bx)-\frac{be^{ax}}{a^2}\cos(bx)}{\left(\frac{b^2}{a^2}+1\right)}+C$$

$$=\frac{(a \sin{(b x)} - b \cos{(b x)}) e^{a x}}{a^{2} + b^{2}}+C$$

> Now we need to consider two cases. First, for $a=0$, and second, for $a=b=0$:

First, $a=0$:

$$\int \sin(bx)dx = - \frac{\cos{(b x)}}{b}$$

Second, $a=b=0$:

$$\int 0dx = 0$$

### Subproblem B

$$\int x\cos(3x)dx$$

$$f=x, dg=\cos(3x)dx, df=1dx, g=\frac{\sin 3x}{3}dx$$

$$\frac{1}{3}x\sin 3x-\frac{1}{3}\int\sin3x dx=\frac{1}{3}x\sin 3x-\frac{1}{9}\int\sin3xd(3x)=$$

$$\frac{1}{3}x\sin 3x-\frac{1}{9}\cos(3x)+C$$

### Subproblem C

$$\int \frac{x\cos(x)}{\sin^2(x)}dx$$

$$f=x, dg=\frac{\cos(x)}{\sin^2(x)}, g=-\frac{1}{\sin (x)},df=dx$$

$$-\frac{x}{\sin(x)}-\int\frac{dx}{\sin(x)}=-\frac{x}{\sin(x)}-\ln\tg\frac{x}{2}$$

### Subproblem D

$$\int x^3e^{-x^2}dx$$

$$u=x^2, du=2xdx$$

$$\frac{1}{2}\int e^{-u}udu$$

$$f=u, df=1du, dg=e^{-u}du, g=-e^{-u}$$

$$-\frac{1}{2}e^{-u}u+\frac{1}{2}\int e^{-u}du=-\frac{1}{2}e^{-u}u-\frac{1}{2}\int e^{-u}d(-u)$$

$$=-\frac{1}{2}e^{-u}u-\frac{1}{2}e^{-u}+C=-\frac{1}{2}e^{-x^2}(x^2+1)+C$$

### Subproblem E

$$\int e^{\sqrt{x}}dx$$

$$u=\sqrt{x},du=\frac{1}{2u}dx$$

$$2\int e^uudu$$

$$f=u, dg=e^udu, df=1du, g=e^u$$

$$2e^uu-2\int e^udu=2e^uu-2e^u+C=$$

$$2e^{\sqrt{x}}(\sqrt{x}-1)+C$$

### Subproblem F

$$\int\sin(\ln x) dx$$

$$u=\ln x, du=\frac{1}{e^u}dx, dx=e^udu, x=e^u$$

$$\int\sin(u)e^udu$$

> We have solved this integral above, so we may simply use

$$\frac{1}{2}e^u(\sin(u)-\cos(u))=\frac{1}{2}x(\sin\ln x-\cos\ln x)$$

## Problem 3

### Subproblem A

$$\int\frac{x^3+1}{x^3-5x^2+6x}dx$$

$$\int\frac{x^3+1}{x^3-5x^2+6x}dx=\int\left(1+\frac{5x^2-6x+1}{x^3-5x^2+6x}\right)dx=$$

$$\int\left(1+\frac{5x^2-6x+1}{x(x-3)(x-2)}\right)dx=\int\left(1+\frac{A}{x}+\frac{B}{x-2}+\frac{C}{x-3}\right)dx$$

$$5x^2-6x+1=A(x-2)(x-3)+Bx(x-3)+Cx(x-2)=\\ Ax^2-5Ax+6A+Bx^2-3Bx+Cx^2-2Cx$$

$$\begin{cases}
    A+B+C=5\\
    -5A-3B-2C=-6\\
    6A=1
\end{cases}\implies\begin{cases}
    B+C=\frac{29}{6}\\
    3B+2C=\frac{31}{6}\\
    A=\frac{1}{6}
\end{cases}\implies\begin{cases}
    A=\frac{1}{6}\\
    B=-\frac{9}{2}\\
    C=\frac{28}{3}
\end{cases}$$

$$\int\left(1+\frac{1}{6x}-\frac{9}{2(x-2)}+\frac{28}{3(x-3)}\right)dx=$$

$$\int dx+\frac{1}{6}\int\frac{dx}{x}-\frac{9}{2}\int\frac{dx}{x-2}+\frac{28}{3}\int\frac{dx}{x-3}=$$

$$x+\frac{1}{6}\ln x-\frac{9}{2}\ln (x-2)+\frac{28}{3}\ln(x-3)+C$$

### Subproblem B

$$\int\frac{x}{x^3-3x+2}dx$$

$$\int\frac{x}{(x-1)^2(x+2)}dx=\int\left(\frac{A}{(x-1)^2}+\frac{B}{x-1}+\frac{C}{x+2}\right) dx$$

$$x=A(x+2)+B(x-1)(x+2)+C(x-1)^2=\\
Ax+2A+Bx^2+Bx-2B+Cx^2-2Cx+C$$

$$\begin{pmatrix}
0 & 1 & 1 & \bigm| & 0\\
1 & 1 & -2 & \bigm| & 1\\
2 & -2 & -2 & \bigm| & 0
\end{pmatrix}\sim\begin{pmatrix}
0 & 1 & 0 & \bigm| & \frac{2}{9}\\
1 & 0 & 0 & \bigm| & \frac{1}{3}\\
0 & 0 & 1 & \bigm| & -\frac{2}{9}
\end{pmatrix}$$

$$\frac{1}{3}\int\frac{dx}{(x-1)^2}+\frac{2}{9}\int\frac{dx}{x-1}-\frac{2}{9}\int\frac{dx}{x+2}$$

$$-\frac{1}{3}\frac{1}{x-1}+\frac{2}{9}\ln(x-1)-\frac{2}{9}\ln(x+2)+C$$

### Subproblem C

$$\int\frac{dx}{(x+1)(x+2)^2(x+3)^3}$$

$$\int\left(\frac{A}{x+1}+\frac{B}{x+2}+\frac{C}{(x+2)^2}+\frac{D}{x+3}+\frac{E}{(x+3)^2}+\frac{F}{(x+3)^3}\right)dx$$

$$1=A(x+2)^2(x+3)^3+B(x+1)(x+2)(x+3)^3+C(x+1)(x+3)^3+\\+D(x+1)(x+2)^2(x+3)^2+E(x+1)(x+2)^2(x+3)+F(x+1)(x+2)^2=$$

> No torturing myself here unfortunately, the matrix instantly

$$\begin{pmatrix}
    108 & 54 & 27 & 36 & 12 & 4\\
    216 & 135 & 54 & 96 & 28 & 8\\
    171 & 126 & 36 & 97 & 23 & 5\\
    67 & 56 & 10 & 47 & 8 & 1\\
    13 & 12 & 1 & 11 & 1 & 0\\
    1 & 1 & 0 & 1 & 0 & 0
\end{pmatrix}\begin{pmatrix}
    A\\
    B\\
    C\\
    D\\
    E\\
    F
\end{pmatrix}=\begin{pmatrix}
    1\\
    0\\
    0\\
    0\\
    0\\
    0\\
\end{pmatrix}\implies$$

$$\begin{pmatrix}
    A\\
    B\\
    C\\
    D\\
    E\\
    F
\end{pmatrix}=\begin{pmatrix}
    \frac{1}{8}\\
    2\\
    -1\\
    -\frac{17}{8}\\
    -\frac{5}{4}\\
    -\frac{1}{2}
\end{pmatrix}$$

$$\frac{1}{8}\int\frac{dx}{x+1}+2\int\frac{dx}{x+2}-\int\frac{dx}{(x+2)^2}-$$

$$-\frac{17}{8}\int\frac{dx}{x+3}-\frac{5}{4}\int\frac{dx}{(x+3)^2}-\frac{1}{2}\int\frac{dx}{(x+3)^3}dx=$$

$$\frac{1}{8}\ln(x+1)+2\ln(x+2)-\frac{17}{8}\ln(x+3)+\\\frac{1}{x+2}+\frac{5}{4}\frac{1}{x+3}+\frac{1}{4}\frac{1}{(x+3)^2}+C$$

### Subproblem D

$$\int\frac{dx}{x(x+1)(x^2+1)}$$

$$\int\left(\frac{A}{x}+\frac{B}{x+1}+\frac{Cx+D}{x^2+1}\right)dx$$

$$1=A(x^3+x^2+x+1)+Bx(x^2+1)+(x^2+x)(Cx+D)=\\ (A+B+C)x^3+(A+C+D)x^2+(A+B+D)x+A$$

$$\begin{pmatrix}
    1 & 0 & 0 & 0\\
    1 & 1 & 0 & 1\\
    1 & 0 & 1 & 1\\
    1 & 1 & 1 & 0    
\end{pmatrix}\begin{pmatrix}
    A\\
    B\\
    C\\
    D
\end{pmatrix}=\begin{pmatrix}
    1\\
    0\\
    0\\
    0\\
\end{pmatrix}\implies\begin{pmatrix}
    A\\
    B\\
    C\\
    D
\end{pmatrix}=\begin{pmatrix}
    1\\
    -\frac{1}{2}\\
    -\frac{1}{2}\\
    -\frac{1}{2}\\
\end{pmatrix}$$

$$\int\frac{dx}{x}-\frac{1}{2}\int\frac{dx}{x+1}-\frac{1}{2}\int\frac{x}{x^2+1}dx-\frac{1}{2}\int\frac{1}{x^2+1}dx$$

$$\ln x -\frac{1}{2} \ln(x+1)-\frac{1}{4}\int\frac{d(x^2+1)}{x^2+1}-\frac{1}{2}\arctg x$$

$$\ln x -\frac{1}{2} \ln(x+1)-\frac{1}{4}\ln (x^2+1)-\frac{1}{2}\arctg x+C$$

### Subproblem E

$$\int\frac{dx}{x^4+x^2+1}$$

$$\int\left(\frac{dx}{(x^2-x+1)(x^2+x+1)}\right)=\int\left(\frac{Ax+B}{x^2-x+1}+\frac{Cx+D}{x^2+x+1}\right)dx$$

$$1=Ax(x^2+x+1)+B(x^2+x+1)+Cx(x^2-x+1)+D(x^2-x+1)=\\ B+D+(A+C)x^3+(A+B-C+D)x^2+(A+B+C-D)x$$

$$\begin{pmatrix}
    0 & 1 & 0 & 1\\
    1 & 1 & 1 & -1\\
    1 & 1 & -1 & 1\\
    1 & 0 & 1 & 0
\end{pmatrix}\begin{pmatrix}
    A\\
    B\\
    C\\
    D
\end{pmatrix}=\begin{pmatrix}
    1\\
    0\\
    0\\
    0
\end{pmatrix}\implies\begin{pmatrix}
    A\\
    B\\
    C\\
    D
\end{pmatrix}=\begin{pmatrix}
    -\frac{1}{2}\\
    \frac{1}{2}\\
    \frac{1}{2}\\
    \frac{1}{2}
\end{pmatrix}$$

$$\frac{1}{2}\int\frac{-x+1}{x^2-x+1}dx+\frac{1}{2}\int\frac{x+1}{x^2+x+1}dx$$

$$\frac{1}{2}\bigg(\int\frac{dx}{2(x^2-x+1)}-\int\frac{2x-1}{2(x^2-x-1)}dx+$$

$$+\int\frac{2x+1}{2(x^2+x+1)}dx+\int\frac{dx}{2(x^2+x+1)}\bigg)$$

$$\frac{1}{2}\bigg(\int\frac{dx}{2(x^2-x+1)}-\int\frac{d(x^2-x-1)}{2(x^2-x-1)}+$$

$$+\int\frac{d(x^2+x+1)}{2(x^2+x+1)}+\int\frac{dx}{2(x^2+x+1)}\bigg)$$

$$\frac{1}{4}(\ln(x^2+x+1)-\ln(x^2-x-1))+$$

$$+\frac{1}{4}\left(\int\frac{dx}{(x^2-x+1)}+\int\frac{dx}{(x^2+x+1)}\right)$$

> Evaluate the following integral:

$$\int\frac{dx}{(x^2\plusmn x+1)}=\int\frac{dx}{(x\plusmn\frac{1}{2})^2+\frac{3}{4}}=\frac{4}{3}\int\frac{dx}{\frac{4}{3}(x\plusmn\frac{1}{2})^2+1}$$

$$=\frac{4}{3}\int\frac{dx}{(\frac{2}{\sqrt{3}}(x\plusmn\frac{1}{2}))^2+1}=\frac{4}{3}\frac{\sqrt{3}}{2}\int\frac{d(\frac{2}{\sqrt{3}}(x\plusmn\frac{1}{2}))}{(\frac{2}{\sqrt{3}}(x\plusmn\frac{1}{2}))^2+1}+C=$$

$$\frac{2}{\sqrt{3}}\int\frac{d(\frac{2}{\sqrt{3}}(x\plusmn\frac{1}{2}))}{(\frac{2}{\sqrt{3}}(x\plusmn\frac{1}{2}))^2+1}=\frac{2}{\sqrt{3}}\arctg \left(\frac{2}{\sqrt{3}}(x\plusmn\frac{1}{2})\right)$$

> And now the final integral:

$$\frac{1}{4}(\ln(x^2+x+1)-\ln(x^2-x-1))+\\+\frac{1}{4}\left(\frac{2}{\sqrt{3}}\arctg \left(\frac{2}{\sqrt{3}}(x-\frac{1}{2})\right)+\frac{2}{\sqrt{3}}\arctg \left(\frac{2}{\sqrt{3}}(x+\frac{1}{2})\right)\right)+C=$$

$$\frac{1}{4}(\ln(x^2+x+1)-\ln(x^2-x-1))+\\+\frac{1}{2\sqrt{3}}\left(\arctg \left(\frac{2}{\sqrt{3}}(x-\frac{1}{2})\right)+\arctg \left(\frac{2}{\sqrt{3}}(x+\frac{1}{2})\right)\right)+C$$


### Subproblem F

$$\int\frac{dx}{x^6+1}$$

$$\int\frac{dx}{(x^2-\sqrt{3}x+1)(x^2+\sqrt{3}x+1)(x^2+1)}=$$

$$\int\left(\frac{Cx+D}{x^2-\sqrt{3}x+1}+\frac{Ex+F}{x^2+\sqrt{3}x+1}+\frac{Ax+B}{x^2+1}\right)dx$$

$$1 = -B+D-F+(-A+C-E)x^5+(-B+\sqrt{3}C+D+\sqrt{3}E-F)x^4+\\+(A+2C+\sqrt{3}D-2E+\sqrt{3}F)x^3+(B+\sqrt{3}C+2D+\sqrt{3}E-2F)x^2+\\+(-A+C+\sqrt{3}D-E+\sqrt{3}F)x$$

$$\begin{pmatrix}
    0 & -1 & 0 & 1 & 0 & -1\\
    -1 & 0 & 1 & \sqrt{3} & -1 & \sqrt{3}\\
    0 & 1 & \sqrt{3} & 2 & \sqrt{3} & -2\\
    1 & 0 & 2 & \sqrt{3} & -2 & \sqrt{3}\\
    0 & -1 & \sqrt{3} & 1 & \sqrt{3} & -1\\
    -1 & 0 & 1 & 0 & - 1 & 0\\
\end{pmatrix}\begin{pmatrix}
    A\\
    B\\
    C\\
    D\\
    E\\
    F\\
\end{pmatrix}=\begin{pmatrix}
    1\\
    0\\
    0\\
    0\\
    0\\
    0\\
\end{pmatrix}\implies$$

$$\begin{pmatrix}
    A\\
    B\\
    C\\
    D\\
    E\\
    F\\
\end{pmatrix}=\begin{pmatrix}
    0\\
    -\frac{1}{3}\\
    -\frac{1}{2\sqrt{3}}\\
    \frac{1}{3}\\
    -\frac{1}{2\sqrt{3}}\\
    -\frac{1}{3}\\
\end{pmatrix}$$

$$\int\left(\frac{-\frac{x}{2\sqrt{3}}+\frac{1}{3}}{x^2-\sqrt{3}x+1}+\frac{\frac{x}{2\sqrt{3}}+\frac{1}{3}}{x^2+\sqrt{3}x+1}\right)dx+\frac{1}{3}\int\frac{dx}{x^2+1}$$

Solve for 

$$\int\frac{\plusmn\frac{x}{2\sqrt{3}}+\frac{1}{3}}{x^2\plusmn\sqrt{3}x+1}dx=\frac{1}{12}\int\frac{1}{x^2\plusmn\sqrt{3}x+1}dx\plusmn\frac{1}{4\sqrt{3}}\int\frac{2x-\sqrt{3}}{x^2-\sqrt{3}x+1}dx$$

First part:

$$\int\frac{dx}{x^2\plusmn\sqrt{3}x+1}=4\int\frac{dx}{(2x\plusmn\sqrt{3})^2+1}=2\int\frac{d(2x\plusmn\sqrt{3})}{(2x\plusmn\sqrt{3})^2+1}=\\2\arctg(2x\plusmn\sqrt{3})+C$$

Second part:

$$\int\frac{2x\plusmn\sqrt{3}}{x^2\plusmn\sqrt{3}x+1}dx=\int\frac{d(2x\plusmn\sqrt{3})}{x^2\plusmn\sqrt{3}x+1}=\ln(x^2\plusmn\sqrt{3}x+1)+C$$

Third part:

$$\int\frac{dx}{x^2+1}=\arctg(x)+C$$

Finally:

$$\int\left(\frac{-\frac{x}{2\sqrt{3}}+\frac{1}{3}}{x^2-\sqrt{3}x+1}+\frac{\frac{x}{2\sqrt{3}}+\frac{1}{3}}{x^2+\sqrt{3}x+1}\right)dx+\frac{1}{3}\int\frac{dx}{x^2+1}=$$

$$\frac{1}{6}(\arctg(2x+\sqrt{3})+\arctg(2x-\sqrt{3}))+\\\frac{1}{4\sqrt{3}}\left(\ln(x^2+\sqrt{3}x+1)-\ln(x^2-\sqrt{3}x+1)\right)+\frac{1}{3}\arctg x+C$$

### Subproblem G

$$\int\frac{dx}{x^5-x^4+x^3-x^2+x-1}$$

I'm insanely lazy, so notice that

$$-\frac{1}{6}\int\frac{2x+1}{x^2+x+1}dx-\frac{1}{2}\int\frac{dx}{x^2-x+1}+\frac{1}{3}\int\frac{dx}{x-1}$$

First two integrals we have already calculated and the last one is terribly easy, so the answer is:

$$-\frac{1}{6}\ln(x^2+x+1)+\frac{1}{3}\ln(1-x)-\frac{\sqrt{3}}{3}\arctg\left(\frac{2\sqrt{3}}{3}x-\frac{\sqrt{3}}{3}\right)$$