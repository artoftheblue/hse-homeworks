# Calculus, Homework 9

> Find derivatives

## Problem A

$$f(x)=\frac{2+x^2}{\sqrt{1+x^4}}$$

$$f(x)'=\frac{(2+x^2)'\sqrt{1+x^4}-(2+x^2)\sqrt{1+x^4}'}{\sqrt{1+x^4}^2}=\frac{2x\sqrt{1+x^4}-(2+x^2)(x^4)'\frac{1}{2\sqrt{1+x^4}}}{\sqrt{1+x^4}^2}=$$

$$\frac{2x(1+x^4)-\frac{1}{2}4x^3(2+x^2)}{\sqrt{1+x^4}^3}=\frac{2x(1+x^4-2x^2-x^4)}{\sqrt{1+x^4}^3}=\frac{2x(1-2x^2 )}{\sqrt{1+x^4}^3}$$

## Problem B

$$f(x)=e^{3x}(x+3)$$

$$f'(x)=e^{3x}(x+3)'+(e^{3x})'(x+3)=e^{3x}+e^{3x}(3x)'(x+3)=e^{3x}(1+3(x+3))=e^{3x}(3x+10)$$

## Problem C

$$f(x)=x^22^x+x^33^x$$

> $a^x=e^{\ln(a^x)}=e^{x\ln a} \Rightarrow (a^x)'=(x\ln a)'e^{x\ln a}=a^x\ln a$

$$f'(x)=(x^2)(2^x)'+(x^2)'(2^x)+(x^3)(3^x)'+(x^3)'(3^x)=x^22^x\ln 2+2x(2^x)+x^33^x\ln 3+3x^23^x=$$

$$2^x(x^2\ln 2+2x)+3^x(x^3\ln 3 + 3x^2)$$

## Problem D

$$f(x)=\sin x\cdot\cos^23x$$

$$f'(x)=(\sin x)'\cos^23x+\sin x(\cos^23x)'=(\cos x)\cos^23x+\sin x(2\cos3x)(\cos3x)'=$$

$$(\cos x)\cos^23x+\sin x(2\cos3x)(-\sin3x)(3x)'=\cos x\cdot\cos^23x-6\sin x\cdot \cos3x\cdot\sin3x=$$

$$\cos x\cdot\cos^23x-3\sin x\cdot \sin6x$$

## Problem E

$$f(x)=e^{2x}(3\cos3x-2\sin3x)$$

$$f'(x)=e^{2x}(3\cos3x-2\sin3x)'+(e^{2x})'(3\cos3x-2\sin3x)=$$

$$e^{2x}(3(\cos3x)'-2(\sin3x)')+2e^{2x}(3\cos3x-2\sin3x)=$$

$$e^{2x}(-9\sin3x-6\cos3x)+2e^{2x}(3\cos3x-2\sin3x)=$$

$$e^{2x}(-9\sin3x-6\cos3x+6\cos3x-4\sin3x)=-13e^{2x}\sin3x$$

## Problem F

$$f(x)=x^{a^a}+a^{x^a}+a^{a^x} \ \ (a > 0)$$

$$f'(x)=(x^{a^a})'+(a^{x^a})'+(a^{a^x})'=a^ax^{a^a - 1}+(x^a)'a^{x^a}\ln a+(a^x)'a^{a^x}\ln a=$$

$$a^ax^{a^a - 1}+ax^{a-1}a^{x^a}\ln a+a^x\ln a\cdot a^{a^x}\ln a=a^ax^{a^a - 1}+x^{a-1}a^{x^a+1}\ln a+a^{a^x+x}\ln^2 a$$

## Problem G

$$f(x)=\arccos\frac{1+x^3}{1-x^3}$$

> $\displaystyle(\arccos x)' = -\frac{1}{\sqrt{1-x^2}}$

$$f'(x)=\left(\frac{1+x^3}{1-x^3}\right)'\left(-\frac{1}{\sqrt{1-\left(\frac{1+x^3}{1-x^3}\right)^2}}\right)=$$

$$\frac{(1+x^3)'(1-x^3)-(1+x^3)(1-x^3)'}{(1-x^3)^2}\left(-\frac{1}{\sqrt{1-\left(\frac{1+x^3}{1-x^3}\right)^2}}\right)=$$

$$\frac{3x^2(1-x^3)+3x^2(1+x^3)}{(1-x^3)^2}\left(-\frac{1}{\sqrt{1-\left(\frac{1+x^3}{1-x^3}\right)^2}}\right)=$$

$$-\frac{1}{\sqrt{1-\left(\frac{1+x^3}{1-x^3}\right)^2}}\frac{6x^2}{(1-x^3)^2}=-\frac{6x^2}{\sqrt{1-\frac{(1+x^3)^2}{(1-x^3)^2}}(1-x^3)^2}=$$

$$-\frac{6x^2}{\frac{1}{1-x^3}\sqrt{(1-x^3)^2-(1+x^3)^2}(1-x^3)^2}=-\frac{6x^2}{\sqrt{(1-x^3-1-x^3)(1-x^3+1+x^3)}(1-x^3)}=$$

$$-\frac{6x^2}{\sqrt{-4x^3}(1-x^3)}=-\frac{6x^2}{2x\sqrt{-x}(1-x^3)}=-\frac{3x}{\sqrt{-x}(1-x^3)}$$

## Problem H

$$f(x)=2^{\arctg\sqrt{1+x^2}}$$

> $\displaystyle(\arctg x)'=\frac{1}{x^2+1}$

$$f'(x)=(\arctg\sqrt{1+x^2})'2^{\arctg\sqrt{1+x^2}}\ln2=\frac{\sqrt{1+x^2}'}{\sqrt{1+x^2}^2+1}2^{\arctg\sqrt{1+x^2}}\ln2=$$

$$\frac{(x^2)'}{2\sqrt{1+x^2}(2+x^2)}2^{\arctg\sqrt{1+x^2}}\ln2=\frac{x\ln 2\cdot2^{\arctg\sqrt{1+x^2}}}{\sqrt{1+x^2}(2+x^2)}$$

## Problem I

$$f(x)=(1+x)^{\frac{1}{x}}$$

$$f'(x)=(e^{\ln((1+x)^{\frac{1}{x}})})'=e^{\ln((1+x)^{\frac{1}{x}})}(\ln((1+x)^{\frac{1}{x}}))'=(1+x)^{\frac{1}{x}}\left(\frac{1}{x}\ln(1+x)\right)'=$$

$$(1+x)^{\frac{1}{x}}\left(\left(\frac{1}{x}\right)'\ln(1+x)+\frac{1}{x}(\ln(1+x))'\right)=(1+x)^{\frac{1}{x}}\left(-\frac{\ln(1+x)}{x^2}+\frac{1}{x}\cdot\frac{1}{x}\right)=$$

$$(1+x)^{\frac{1}{x}}\left(\frac{1-\ln(1+x)}{x^2}\right)=\frac{(1-\ln(1+x))(1+x)^{\frac{1}{x}}}{x^2}$$

## Problem J

$$f(x)=(\arccos x)^2\left[\ln^2(\arccos x)-\ln\arccos x + \frac{1}{2}\right]$$

> $\displaystyle(\arccos x)' = -\frac{1}{\sqrt{1-x^2}}$

$$f'(x)=\overbrace{((\arccos x)^2)'\left[\ln^2(\arccos x)-\ln\arccos x + \frac{1}{2}\right]}^{\displaystyle A}+\overbrace{(\arccos x)^2\left[\ln^2(\arccos x)-\ln\arccos x + \frac{1}{2}\right]'}^{\displaystyle B}=$$

$$A =\frac{-2\arccos x}{\sqrt{1-x^2}}\left[\ln^2(\arccos x)-\ln\arccos x + \frac{1}{2}\right]=\frac{\arccos x}{\sqrt{1-x^2}}\left[2\ln\arccos x-2\ln^2(\arccos x) - 1\right]$$

$$B=\arccos^2x\left[(\ln^2(\arccos x))'-(\ln\arccos x)' + \left(\frac{1}{2}\right)'\right]=$$

$$\arccos^2x(\ln(\arccos x)(\ln\arccos x - 1))'=$$

$$\arccos^2x((\ln(\arccos x))'(\ln\arccos x - 1)+(\ln(\arccos x))(\ln\arccos x - 1)')=$$

$$\arccos^2x\left(\frac{(\arccos x)'(\ln\arccos x - 1)}{\arccos x}+\frac{(\arccos x)'\ln\arccos x}{\arccos x}\right)=$$

$$\arccos^2x\left(-\frac{1}{\sqrt{1-x^2}}\frac{2\ln\arccos x - 1}{\arccos x}\right)=\frac{\arccos x(1-2\ln\arccos x)}{\sqrt{1-x^2}}$$

$$f'(x)=A+B=\frac{\arccos x}{\sqrt{1-x^2}}\left[2\ln\arccos x-2\ln^2(\arccos x) - 1\right]+\frac{\arccos x(1-2\ln\arccos x)}{\sqrt{1-x^2}}=$$

$$\frac{\arccos x}{\sqrt{1-x^2}}\left[2\ln\arccos x-2\ln^2(\arccos x) - 1+1-2\ln\arccos x\right]=-\frac{2\ln^2\arccos x\cdot\arccos x}{\sqrt{1-x^2}}$$