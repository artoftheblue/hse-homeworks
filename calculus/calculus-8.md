## Problem A

$$\lim_{x\to0}\frac{\cos x-\cos 3x}{x^2}=\lim_{x\to0}\frac{1-\frac{x^2}{2}-1+\frac{9x^2}{2} +o(x^2)}{x^2}=\lim_{x\to0}\frac{4x^2+o(x^2)}{x^2}=4$$

## Problem B

$$\lim_{x\to0}\frac{\cos(a+2x)-2\cos(a+x)+\cos a}{x^2}=\lim_{x\to0}\frac{2\cos(\frac{a+2x}{2}-\frac{a}{2})\cos(\frac{a+2x}{2}+\frac{a}{2})-2\cos(a+x)}{x^2}=$$

$$\lim_{x\to0}\frac{2\cos(x)\cos(a+x)-2\cos(a+x)}{x^2}=\lim_{x\to0}\frac{2\cos(a+x)(\cos(x)-1)}{x^2}=$$

$$\lim_{x\to0}\frac{2\cos(a+x)(1-\frac{x^2}{2}-1+o(x^2))}{x^2}=\lim_{x\to0}\frac{2\cos(a+x)(-\frac{x^2}{2}+o(x^2))}{x^2}=$$

$$\lim_{x\to0}\left(2\cos(a+x)\left(-\frac{1}{2}+o(1)\right)\right)=\lim_{x\to0}\left(-\cos(a+x)+o(1)\right)=-\cos(a+0)+0=-\cos a$$

## Problem C

$$\lim_{x\to+\infty}(\sqrt[3]{x^3+3x^2}-\sqrt{x^2-2x})=\lim_{x\to+\infty}\left(x\sqrt[3]{1+\frac{3}{x}}-x\sqrt{1-\frac{2}{x}}\right)=$$

$$\lim_{t\to0}\left(\frac{1}{t}\sqrt[3]{1+3t}-\frac{1}{t}\sqrt{1-2t}\right)=\lim_{t\to0}\left(\frac{1}{t}(1+t+o(t))-\frac{1}{t}(1-t+o(t))\right)=$$

$$\lim_{t\to0}\left(\frac{1}{t}\left((1+t+o(t)-1+t+o(t))\right)\right)=\lim_{t\to0}\left(\frac{2t+o(t)}{t}\right)=\lim_{t\to0}\left(2+o(1)\right)=2$$

## Problem D

$$\lim_{x\to a}\frac{a^x-x^a}{x-a}, \ \ a >0$$

$$\lim_{y\to 0}\frac{a^{(y+a)}-(y+a)^a}{(y+a)-a}=\lim_{y\to 0}\frac{a^{(y+a)}-(y+a)^a}{y}=\lim_{y\to 0}\frac{a^ya^a-a^a(\frac{y}{a}+1)^a}{y}=$$

$$\lim_{y\to 0}\frac{a^a(1+y\ln(a)-(\frac{y}{a}+1)^a)}{y}=\lim_{y\to 0}\frac{a^a(1+y\ln a+o(y)-y-1+o(y))}{y}=$$

$$\lim_{y\to0}\frac{a^ay(\ln a - 1 +o(1))}{y}=\lim_{y\to0}\left(a^a(\ln a-1+o(1))\right)=a^a(\ln a -1)$$

## Problem E

$$\lim_{y\to a}\frac{\ln y-\ln a}{y - a}=\lim_{x\to 0}\frac{\ln(x+a)-\ln a}{(x+a) - a}=\lim_{x\to 0}\frac{\ln(a(\frac{x}{a}+1))-\ln a}{x}=\lim_{x\to 0}\frac{\ln(\frac{x}{a}+1)+\ln a-\ln a}{x}=$$

$$\lim_{x\to 0}\frac{\ln(\frac{x}{a}+1)}{x}=\lim_{x\to 0}\frac{\frac{x}{a}+o(x)}{x}=\lim_{x\to 0}\left(\frac{1}{a}+o(1)\right)=\frac{1}{a}$$

## Problem F

$$\lim_{x\to0}\frac{\ln(x^2+e^x)}{\ln(x^4+e^{2x})}=\lim_{x\to0}\frac{\ln(x^2+1+x+o(x))}{\ln(x^4+1+2x+o(x))}=\lim_{x\to0}\frac{x^2+x+o(x^2)}{x^4+2x+o(x^4)}=$$

$$\lim_{x\to0}\frac{x+1+o(x)}{x^3+2+o(x^3)}=\frac{0+1+0}{0+2+0}=\frac{1}{2}$$

## Problem G

$$\lim_{x\to0}(1+\tg^2x)^{\frac{1}{\ln\cos x}}=\lim_{x\to0}(1+(x+o(x))^2)^{\frac{1}{\ln\left(1-\frac{x^2}{2}+o(x^2)\right)}}=\lim_{x\to0}(1+x^2+o(x^2))^{\frac{1}{-\frac{x^2}{2}+o(x^2)}}=$$

$$\lim_{x\to0}(1+x^2+o(x^2))^{\frac{1}{x^2+o(x^2)}\times-2}=e^{-2}$$

## Problem H

$$\lim_{x\to1}(x^2+\sin^2(\pi x))^\frac{1}{\ln x}=\lim_{y\to0}((y+1)^2+\sin^2(\pi (y + 1)))^\frac{1}{\ln (y+1)}=\lim_{y\to0}((y+1)^2-\sin^2(\pi y))^\frac{1}{\ln (y+1)}=$$

$$\lim_{y\to0}((y+1)^2-(\pi y + o(y))^2)^\frac{1}{y+o(y)}=\lim_{y\to0}(y^2+2y+1-\pi^2 y^2 + o(y)^2)^\frac{1}{y+o(y)}=$$

$$\lim_{y\to0}\left(1+\frac{y^2(1-\pi^2)+2y+o(y^2)}{1}\right)^\frac{1}{y+o(y)}=\lim_{y\to0}\left(1+\frac{1}{\frac{1}{y^2(1-\pi^2)+2y+o(y^2)}}\right)^\frac{1}{y+o(y)}=$$

$$\lim_{y\to0}\left(1+\frac{1}{\frac{1}{y^2(1-\pi^2)+2y+o(y^2)}}\right)^{\frac{1}{y^2(1-\pi^2)+2y+o(y^2)}\frac{y^2(1-\pi^2)+2y+o(y^2)}{y+o(y)}}=e^{\lim_{y\to0}\frac{y(1-\pi^2)+2+o(y)}{1+o(1)}}=$$

$$e^{0\times(1-\pi^2)+2+0}=e^2$$

## Problem I

$$\lim_{x\to\pi}\left(\frac{\cos x}{\cos 3x}\right)^\frac{1}{(\sqrt{\pi x}-\pi)^2}=\lim_{y\to0}\left(\frac{\cos(y+\pi)}{\cos(3y+3\pi)}\right)^\frac{1}{(\sqrt{\pi (y + \pi)}-\pi)^2}=\lim_{y\to0}\left(\frac{-\cos y}{-\cos 3y}\right)^\frac{1}{(\sqrt{\pi (y + \pi)}-\pi)^2}=$$

$$\lim_{y\to0}\left(\frac{\cos y}{\cos 3y}\right)^\frac{1}{(\pi\sqrt{\frac{y}{\pi} + 1}-\pi)^2}=\lim_{y\to0}\left(\frac{1-\frac{y^2}{2}+o(y^2)}{1-\frac{9y^2}{2}+o(y^2)}\right)^\frac{1}{\left(\pi\left(\frac{1}{2}\frac{y}{\pi} + 1\right)-\pi+o(y)\right)^2}=\lim_{y\to0}\left(\frac{1-\frac{y^2}{2}+o(y^2)}{1-\frac{9y^2}{2}+o(y^2)}\right)^\frac{1}{\left(\frac{y}{2}+o(y)\right)^2}=$$

$$\lim_{y\to0}\left(1+\frac{1}{\frac{2-9y^2}{8y^2}}+o(1)\right)^{\frac{2-9y^2}{8y^2}\frac{8y^2}{2-9y^2}\frac{1}{\frac{y^2}{4}+o(y^2)}}=e^{\lim_{y\to0}\frac{8y^2}{2-9y^2}\frac{1}{\frac{y^2}{4}+o(y^2)}}=e^{\lim_{y\to0}\frac{32y^2}{2y^2-9y^4+o(y^2)}}=$$

$$e^{\lim_{y\to0}\frac{32}{2-9y^2+o(1)}}=e^{\frac{32}{2-0+0}}=e^{16}$$

## Problem J

$$\lim_{x\to1}x^{\tg\left(\frac{\pi x}{2}\right)}=\lim_{y\to0}(y+1)^{\tg\left(\frac{\pi (y+1)}{2}\right)}=\lim_{y\to0}(y+1)^{-\ctg\left(\frac{\pi y}{2}\right)}=\lim_{y\to0}(y+1)^{-\frac{2}{\pi y+o(y)}}=$$

$$\lim_{y\to0}(y+1)^{\frac{1}{y+o(y)}\times-\frac{2}{\pi}}=e^{-\frac{2}{\pi}}$$