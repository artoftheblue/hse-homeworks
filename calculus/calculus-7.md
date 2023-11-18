# Calculus, Homework 7

> Calculate the following limits:

## Problem 1

### Subproblem A

$$\lim_{x\to2}\frac{x^2+x-6}{x^2-3x+2}=\lim_{x\to2}\frac{(x+3)(x-2)}{(x-1)(x-2)}=\lim_{x\to2}\frac{x+3}{x-1}=\frac{2+3}{2-1}=5$$

Answer:

$$\lim_{x\to2}\frac{x^2+x-6}{x^2-3x+2}=5$$

### Subproblem C

$$\lim_{x\to1}\frac{x^5-3x^4+3x^3-x^2}{x^4-6x^2+8x-3}=\lim_{x\to1}\frac{x^2(x^3-3x^2+3x-1)}{x^4-6x^2+8x-3}=\lim_{x\to1}\frac{x^2(x-1)^3}{x^4-6x^2+8x-3}=$$

$$\lim_{x\to1}\frac{x^2(x-1)^3}{(x+3)(x-1)^3}=\lim_{x\to1}\frac{x^2}{(x+3)}=\frac{1^2}{1+4}=\frac{1}{4}$$

Answer:

$$\lim_{x\to1}\frac{x^5-3x^4+3x^3-x^2}{x^4-6x^2+8x-3}=\frac{1}{4}$$

### Subproblem F

$$\lim_{x\to3}\frac{\sqrt{x+13}-2\sqrt{x+1}}{x^2-9}=\lim_{x\to3}\frac{x+13-4x-4}{(x^2-9)(\sqrt{x+13}+2\sqrt{x+1})}=$$

$$\lim_{x\to3}\frac{-3(x-3)}{(x-3)(x+3)(\sqrt{x+13}+2\sqrt{x+1})}=\lim_{x\to3}\frac{-3}{(x+3)(\sqrt{x+13}+2\sqrt{x+1})}=$$

$$\lim_{x\to3}\frac{-3}{(x+3)(\sqrt{x+13}+2\sqrt{x+1})}=\frac{-3}{6\times(\sqrt{3+13}+2\sqrt{3+1})}=-\frac{1}{2\times8}=-\frac{1}{16}$$

Answer:

$$\lim_{x\to3}\frac{\sqrt{x+13}-2\sqrt{x+1}}{x^2-9}=-\frac{1}{16}$$


## Problem 2

### Subproblem A

$$\lim_{x\to1}\frac{\sin\frac{\pi x}{2}}{x}=\frac{\sin \frac{\pi}{2}}{1}=1$$

Answer:

$$\lim_{x\to1}\frac{\sin\frac{\pi x}{2}}{x}=1$$

### Subproblem C

$$\lim_{x\to0}\frac{\tg x+\tg 2x+\dots + \tg nx}{\arctg x}=\lim_{x\to0}\sum^n_{k=1}\frac{\tg kx}{\arctg x}$$

> Since $\tg x = x + o(x)$ and $\arctg x = x + o(x)$, then

$$\lim_{x\to0}\frac{\tg kx}{\arctg x}=\lim_{x\to0}\frac{kx + o(x)}{x+o(x)}=\lim_{x\to0}(k+o(1))=k$$

> Alternatively, since $\displaystyle\lim_{x\to0}\frac{\tg x}{x}=\lim_{x\to0}\frac{\arctg x}{x}=1$
> $$\lim_{x\to0}\frac{\tg kx}{\arctg x}=\lim_{x\to0}\frac{kx\tg kx}{kx\arctg x}=k\lim_{x\to0}\frac{\tg kx}{kx}\lim_{x\to0}\frac{x}{\arctg x}=k\times1\times1^{-1}=k$$

Therefore,

$$\lim_{x\to0}\sum^n_{k=1}\frac{\tg kx}{\arctg x}=\sum^n_{k=1}k=\frac{n(n+1)}{2}$$

Answer:

$$\lim_{x\to0}\frac{\tg x+\tg 2x+\dots + \tg nx}{\arctg x}=\frac{n(n+1)}{2}$$

### Subproblem D

$$\lim_{x\to0}\frac{\tg x - \sin x}{\sin^3x}=\lim_{x\to0}\frac{\sin x - \sin x\cos x}{\sin^3x\cos x}=\lim_{x\to0}\frac{1 - \cos x}{\sin^2x\cos x}=$$

> Since $1 - \cos x=2\sin^2\frac{x}{2}, \sin x\cos x=\frac{1}{2}\sin 2x, \sin x = x + o(x)$, then:

$$\lim_{x\to0}\frac{2\sin^2\frac{x}{2}}{\frac{1}{2}\sin 2x\sin x}=\lim_{x\to0}\frac{2(\frac{x}{2}+o(x))^2}{\frac{1}{2}(2x+o(x))(x + o(x))}=4\lim_{x\to0}\frac{\frac{x^2}{4}+xo(x)+o(x^2)}{2x^2+2xo(x)+xo(x)+ o(x^2)}=$$

$$4\lim_{x\to0}\frac{\frac{x^2}{4}+o(x^2)}{2x^2+o(x^2)}=\frac{4}{8}\lim_{x\to0}\frac{x^2+o(x^2)}{x^2+o(x^2)}=\frac{1}{2}$$

> Alternatively, since $\displaystyle\lim_{x\to0}\frac{\sin x}{x}=1$
> $$\lim_{x\to0}\frac{2\sin^2\frac{x}{2}}{\frac{1}{2}\sin 2x\sin x}=\frac{1}{2}\lim_{x\to0}\frac{\sin^2\frac{x}{2}}{\frac{x^2}{2^2}}\frac{x}{\sin x}\frac{2x}{\sin 2x}=\frac{1}{2}\times1^2\times1^{-1}\times1^{-1}=\frac{1}{2}$$

Answer:

$$\lim_{x\to0}\frac{\tg x - \sin x}{\sin^3x}=\frac{1}{2}$$

### Subproblem E

$$\lim_{x\to a}\frac{\sin x - \sin a}{x-a}=\lim_{x\to a}\frac{2\sin\frac{x-a}{2}\cos\frac{x+a}{2}}{x-a}\xRightarrow{z=x-a}\lim_{z\to 0}\frac{2\sin\frac{z}{2}\cos(\frac{z}{2}+a)}{z}=$$

$$\lim_{z\to 0}\frac{2(\frac{z}{2}+o(z))\cos(\frac{z}{2}+a)}{z}=\lim_{z\to 0}\frac{(z+o(z))\cos(\frac{z}{2}+a)}{z}=$$

$$\lim_{z\to 0}\frac{z\cos(\frac{z}{2}+a)+o(z)\cos(\frac{z}{2}+a)}{z}=\lim_{z\to 0}\left(\cos\left(\frac{z}{2}+a\right)+o(1)\cos\left(\frac{z}{2}+a\right)\right)=$$

$$\cos\left(\frac{0}{2}+a\right)+0=\cos(a)$$

> Alternatively,
> $$\lim_{z\to 0}\frac{\sin\frac{z}{2}}{\frac{z}{2}}\cos\left(\frac{z}{2}+a\right)=1\times\cos\left(\frac{0}{2}+a\right)=\cos a$$

Answer:

$$\lim_{x\to a}\frac{\sin x - \sin a}{x-a}=\cos(a)$$

### Subproblem F

$$\lim_{x\to 1}\frac{\ln(x^2+\cos\frac{\pi x}{2})}{\sqrt{x} - 1}=\lim_{y\to 0}\frac{\ln((y+1)^2+\cos(\frac{\pi y}{2}+\frac{\pi}{2}))}{\sqrt{y+1} - 1}=$$

> Since $\displaystyle\cos x = -\sin\left(x+\frac{\pi}{2}\right), \sin x = x - \frac{x^3}{6}+ o(x^3)$

$$\lim_{y\to 0}\frac{\ln((y+1)^2-\sin\frac{\pi y}{2})}{\sqrt{y+1} - 1}=\lim_{y\to 0}\frac{\ln((y+1)^2-\frac{\pi y}{2}+\frac{\pi^3 y^3}{8}+o(y^3))}{\sqrt{y+1} - 1}=\lim_{y\to 0}\frac{\ln(1+y^2+(2-\frac{\pi}{2})y+\frac{\pi^3 y^3}{8}+o(y^3))}{\sqrt{y+1} - 1}=$$

> Since $\displaystyle\sqrt{1+x}=1+\frac{x}{2}-\frac{x^2}{8}+\frac{x^3}{16}+o(x^3), \ln(1+x) = x + o(x)$

$$\lim_{y\to 0}\frac{y^2+(2-\frac{\pi}{2})y+\frac{\pi^3 y^3}{8}+o(y^3)}{1+\frac{y}{2}-\frac{y^2}{8} +\frac{y^3}{16}-1+o(y^3)}=\lim_{y\to 0}\frac{y+(2-\frac{\pi}{2})+\frac{\pi^3 y^2}{8}+o(y^2)}{\frac{1}{2}-\frac{y}{8}+\frac{y^2}{16}+o(y^2)}=\frac{0+(2-\frac{\pi}{2})+0+0}{\frac{1}{2}-0+0+0}=4-\pi$$

> Alternatively, since $\displaystyle\lim_{x\to0}\frac{(y+1)^\alpha-1}{y}=\alpha,\lim_{x\to0}\frac{\sin x}{x}=1$
> $$\lim_{y\to 0}\frac{\ln((y+1)^2-\sin\frac{\pi y}{2})}{\sqrt{y+1} - 1}=\lim_{y\to0}\frac{y}{(y+1)^\frac{1}{2}-1}\frac{(y+2-\frac{\pi}{2}\frac{\sin\frac{\pi y}{2}}{\frac{\pi y}{2}})\ln(1+y(y+2-\frac{\pi}{2}\frac{\sin\frac{\pi y}{2}}{\frac{\pi y}{2}}))}{(y+2-\frac{\pi}{2}\frac{\sin\frac{\pi y}{2}}{\frac{\pi y}{2}})y}=$$
>
> $$\left(\frac{1}{2}\right)^{-1}\times\lim_{y\to0}\left(y+2-\frac{\pi}{2}\frac{\sin\frac{\pi y}{2}}{\frac{\pi y}{2}}\right)\times 1=2\lim_{y\to0}\left(y+2-\frac{\pi}{2}\times1\right)=2\left(0+2-\frac{\pi}{2}\right)=4-\pi$$

Answer: 

$$\lim_{x\to 1}\frac{\ln(x^2+\cos\frac{\pi x}{2})}{\sqrt{x} - 1}=4-\pi$$

### Subproblem G

$$\lim_{x\to+0}\frac{\sqrt{1-e^{-x}}-\sqrt{1-\cos x}}{\sqrt{\sin x}}=\lim_{x\to+0}\frac{\sqrt{1-e^{-x}}}{\sqrt{\sin x}}-\lim_{x\to+0}\frac{\sqrt{1-\cos x}}{\sqrt{\sin x}}$$

> Since $e^x = 1 + x + o(x), \sin x = x + o(x)$

$$\lim_{x\to+0}\frac{\sqrt{1-e^{-x}}}{\sqrt{\sin x}}=\lim_{x\to+0}\sqrt{\frac{1-1 + x + o(x)}{x+o(x)}}=\lim_{x\to+0}\sqrt{\frac{x + o(x)}{x+o(x)}}=1$$

> Alternatively, since $\displaystyle\lim_{x\to0}\frac{e^x-1}{x}=1$
> $$\lim_{x\to+0}\sqrt{\frac{1-e^{-x}}{\sin x}}=\lim_{x\to+0}\sqrt{\frac{x(e^{-x}-1)}{x\sin x}}=\lim_{x\to+0}\sqrt{\frac{(e^{-x}-1)}{x}\frac{x}{\sin x}}=\sqrt{1\times1^{-1}}=1$$

$$\lim_{x\to+0}\frac{\sqrt{1-\cos x}}{\sqrt{\sin x}}=\lim_{x\to+0}\sqrt{\frac{1-\cos x}{\sin x}}=\lim_{x\to+0}\sqrt{\frac{1-\cos x}{\sin^2 x}\sin x}=$$

> Since $\displaystyle\lim_{x\to+0}\frac{1-\cos x}{\sin^2 x}=1-\frac{x^2}{2}$

$$\sqrt{\lim_{x\to+0}\frac{1-\cos x}{\sin^2 x}\lim_{x\to+0}\sin x}=\sqrt{\left(1-\frac{x^2}{2}\right)\lim_{x\to+0}\sin x}=\sqrt{\left(1-\frac{x^2}{2}\right)\times0}=0$$

Therefore, 

$$\lim_{x\to+0}\frac{\sqrt{1-e^{-x}}}{\sqrt{\sin x}}-\lim_{x\to+0}\frac{\sqrt{1-\cos x}}{\sqrt{\sin x}}=1-0=1$$

Answer:

$$\lim_{x\to+0}\frac{\sqrt{1-e^{-x}}-\sqrt{1-\cos x}}{\sqrt{\sin x}}=1$$

### Subproblem H

$$\lim_{x\to1}\frac{\ln(2x^2-x)}{\ln(x^4+x^2-x)}=\lim_{x\to1}\frac{\ln x+\ln(2x-1)}{\ln x+\ln(x^3+x-1)}\xRightarrow{x=y+1}\lim_{y\to0}\frac{\ln(y+1)+\ln(2y+1)}{\ln(y+1)+\ln((y+1)^3+y+1-1)}=$$

> Since $\displaystyle\ln(x+1)=x-\frac{x^2}{2}+\frac{x^3}{3}+o(x^3)$ and $\ln(x+1)=x+o(x)$

$$\lim_{y\to0}\frac{\ln(y+1)+\ln(2y+1)}{\ln(y+1)+\ln(y^3+3y^2+4y+1)}=\lim_{y\to0}\frac{y-\frac{y^2}{2}+\frac{y^3}{3}+o(y^3) + 2y-2y^2+\frac{8y^3}{3}+o(y^3)}{y-\frac{y^2}{2}+\frac{y^3}{3}+o(y^3)+y^3+3y^2+4y+o(y^3)}=$$

$$\lim_{y\to0}\frac{3y-\frac{5y^2}{2}+3y^3+o(y^3)}{5y+\frac{5y^2}{2}+\frac{4y^3}{3}+o(y^3)}=\lim_{y\to0}\frac{3-\frac{5y}{2}+3y^2+o(y^2)}{5+\frac{5y}{2}+\frac{4y^2}{3}+o(y^2)}=\frac{3-0+0+0}{5+0+0+0}=\frac{3}{5}$$

> Alternatively, since $\displaystyle \lim_{x\to0}\frac{\ln(1+x)}{x}=1$
> $$\lim_{y\to0}\frac{\frac{y\ln(y+1)}{y}+\frac{2y\ln(2y+1)}{2y}}{\frac{y\ln(y+1)}{y}+\frac{(y^3+3y^2+4y)\ln(y^3+3y^2+4y+1)}{y^3+3y^2+4y}}=\lim_{y\to0}\frac{y+2y}{y+y^3+3y^2+4y}=\lim_{y\to0}\frac{3}{5+y^2+3y}=\frac{3}{5}$$

Answer:

$$\lim_{x\to1}\frac{\ln(2x^2-x)}{\ln(x^4+x^2-x)}=\frac{3}{5}$$
