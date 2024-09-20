# Calculus, Homework 1 

> Artemis Sinelnikov, EDA-231

## Problem 1

Bring the double integral $\iint\limits_Df(x,y)dxdy$ to an iterated one in all possible orders, where

$$D=\{(x,y)|x\in[0,\tfrac{1}{2}], y\in[0,1],(x-1)^2+(y-1)^2\geq 1\}$$

---

First and foremost, let's plot the area that we'd be calculating via integration.

![alt text](image-2.png)

---

Consider that the first way to iterate the double integral would be to slice it vertically.

X-range would be $[0, \tfrac{1}{2}]$.

Calculating Y-range, we get:

$$(x-1)^2+(y-1)^2\geq1$$

$$(y-1)^2\geq1-(x-1)^2$$

Since this is the lower half of the circle, 

$$y-1\leq-\sqrt{1-(x-1)^2}$$

$$y\leq1-\sqrt{1-(x-1)^2}$$

the expression above is the upper bound and $0$ would be the lower bound.

$$\int_0^{\frac{1}{2}}dx\int^{1-\sqrt{1-(x-1)^2}}_0f(x,y)dy$$

---

Now slice the integral horizontally.

The Y-range would be $[0, 1]$.

The expression for the circlular arc upper bound would be equivalent since the circle expression is symmetric over $x=y$. 

$$x\leq1-\sqrt{1-(y-1)^2}$$

However, as we may see above, there are two sectors divided by the blue dashed line. The separating point would be 

$$y=1-\sqrt{1-\left(\frac{1}{2}-1\right)^2}=1-\sqrt{\frac{3}{4}}$$

This would split our horizontal slice into two parts with two Y-ranges, those being $\left[0,1-\sqrt\frac{3}{4}\right]$ and $\left[1-\sqrt\frac{3}{4}, 1\right]$.

The first part is bounded by $x=[0, \tfrac{1}{2}]$ and the second part is bounded between zero and the arc. Thus, we get

$$\int_0^{1-\sqrt\frac{3}{4}}dy\int_0^{\frac{1}{2}}f(x,y)dx+\int_{1-\sqrt\frac{3}{4}}^1dy\int_0^{1-\sqrt{1-(y-1)^2}}f(x,y)dx$$

## Problem 2

Change the order of integration in the iterated integal:

$$\int\limits^1_0dy\int\limits^{\sqrt{4-y^2}}_{\sqrt{4-4y}}f(x,y)dx+\int\limits^2_1dy\int\limits^{\sqrt{4-y^2}}_0f(x,y)dx$$

---

Area that we're considering looks like this:

![alt text](image-1.png)

* The red line denotes graph $\sqrt{4-y^2}$
* The blue line denotes graph $\sqrt{4-4y}$

It is obvious that when changing the order of integration to the vertical case, we simply take the red line as the upper bound and the blue line as the lower bound. This allows us to use a single double integral over the Y-range of $[0, 2]$:

$$\int\limits^2_0dx\int\limits^{\sqrt{4-y^2}}_{\sqrt{4-4y}}f(x,y)dy$$

## Problem 3

Calculate the integral:

$$\int\limits^2_0x^2dx\int\limits^2_x\ln(1+y^2)dy$$

---

Visualizing the boundaries, we get:

![alt text](image-6.png)

To calculate the integral, transfer $x^2$ into the second integral because it is constant in relation to $y$.

$$\mathcal{I}=\int\limits^2_0dx\int\limits^2_xx^2\ln(1+y^2)dy=\int\limits^2_0\int\limits^2_xx^2\ln(1+y^2)dydx$$

> Now change the order of integration, which would be bounded between $x=0$ and $x=y$. We do this because it's easier to calculate limits in which one of the bounds is $0$ and because in this case we wouldn't have to integrate the logarithm, treating it as a constant.

$$\begin{align*}\mathcal{I}&=\int\limits^2_0\int\limits^y_0x^2\ln(1+y^2)dxdy=\int\limits^2_0\frac{x^3\ln(1+y^2)}{3}\biggr|^y_0dy\\&=\int\limits^2_0\frac{y^3\ln(1+y^2)}{3}dy=\frac{1}{3}\int\limits^2_0y^3\ln(1+y^2)dy\end{align*}
$$

> Now we could integrate by parts.

$$\int fdg=fg-\int gdf$$

$$f=\ln(1+y^2),\quad dg=y^3dy$$

$$df=\frac{2y}{1+y^2},\quad g=\frac{y^4}{4}$$

$$\frac{1}{3}\int y^3\ln(1+y^2)dy=\frac{y^4\ln(1+y^2)}{12}+\frac{1}{6}\int \frac{y^5}{1+y^2}dy$$

> Now substitute $u=y^2,\ du=2ydy\implies dy=\frac{du}{2y}$.

$$\frac{y^4\ln(1+y^2)}{12}-\frac{1}{12}\int \frac{u^2}{1+u}du$$

$$\frac{y^4\ln(1+y^2)}{12}-\frac{1}{12}\int \frac{u^2+2u+1-2u-1}{1+u}du$$

$$\frac{y^4\ln(1+y^2)}{12}-\frac{1}{12}\int \frac{(u+1)^2-2u-2+1}{u+1}du$$

$$\frac{y^4\ln(1+y^2)}{12}-\frac{1}{12}\int \frac{(u+1)^2-2(u+1)+1}{u+1}du$$

$$\frac{y^4\ln(1+y^2)}{12}-\frac{1}{12}\int \left(u+1-2+\frac{1}{u+1}\right)du$$

$$\frac{y^4\ln(1+y^2)}{12}-\frac{1}{12}\int \left(u-1+\frac{1}{u+1}\right)du$$

$$\frac{y^4\ln(1+y^2)}{12}+\frac{1}{12}\left(\frac{u^2}{2}-u+\ln(u+1)\right)$$

$$\frac{y^4\ln(1+y^2)}{12}+\frac{1}{12}\left(\frac{y^4}{2}-y^2+\ln(y^2+1)\right)$$

$$\frac{1}{12}(y^4-1)\ln(y^2+1)-\frac{1}{24}y^2(y^2-2)$$

> Finally, calculate the definite integral by plugging in $y=2$:

$$\frac{15}{12}\ln(5)-\frac{8}{24}=\frac{5}{3}\ln(5)-\frac{1}{3}$$

## Problem 4

Calculate integral 

$$\iint\limits_Dx^2ydxdy$$

where $D$ is a closed triangle with vertices $(0,0),(2,1),(1,-2)$.

---

The bounding box of the triangle would be denoted by the following three lines:

![alt text](image-3.png)

which are

$$\begin{cases}
    2y=x & \text{green}\\
    \frac{y}{3}+\frac{5}{3}=x & \text{purple}\\
    -\frac{y}{2}=x & \text{black}
\end{cases}$$

The figure we need to calculate is 

![alt text](image-4.png)

which I will split into two parts horizontally over $y=0$.

![alt text](image-5.png)

Thus we'd have

$$\underbrace{\int^{0}_{-2}dy\int^{\frac{y}{3}+\frac{5}{3}}_{2y}x^2ydx}_{\mathcal{I_A}} + \underbrace{\int^1_0dy\int^{\frac{y}{3}+\frac{5}{3}}_{-\frac{y}{2}}x^2ydx}_{\mathcal{I_B}}$$


$$\begin{align*}\mathcal{I_A}&=\int^1_0dy\int^{\frac{y}{3}+\frac{5}{3}}_{2y}x^2ydx\\
&=\int^1_0\left(\frac{x^3y}{3}\right)\biggm|^{\frac{y}{3}+\frac{5}{3}}_{2y}dy\\
&=\int^1_0\left(\frac{(\frac{y}{3}+\frac{5}{3})^3y}{3}-\frac{(2y)^3y}{3}\right)dy\\
&=\int^1_0\left(-\frac{215y^4}{81}+\frac{5y^3}{27}+\frac{25y^2}{27}+\frac{125y}{81}\right)dy\\
&=-\frac{215y^5}{405}+\frac{5y^4}{108}+\frac{25y^3}{81}+\frac{125y^2}{162}\biggm|^1_0\\
&=\frac{193}{324}
\end{align*}$$

$$\begin{align*}
\mathcal{I_B}&=\int^{0}_{-2}dy\int^{\frac{y}{3}+\frac{5}{3}}_{-\frac{y}{2}}x^2ydx\\
&=\int^{0}_{-2}\left(\frac{x^3y}{3}\right)\biggm|^{\frac{y}{3}+\frac{5}{3}}_{-\frac{y}{2}}dy\\
&=\int^{0}_{-2}\left(\frac{(\frac{y}{3}+\frac{5}{3})^3y}{3}-\frac{(-\frac{y}{2})^3y}{3}\right)dy\\
&=\int^{0}_{-2}\left(\frac{35y^4}{648}+\frac{5y^3}{27}+\frac{25y^2}{27}+\frac{125y}{81}\right)dy\\
&=\frac{35y^5}{3240}+\frac{5y^4}{108}+\frac{25y^3}{81}+\frac{125y^2}{162}\biggm|^{0}_{-2}\\
&=-\frac{82}{81}
\end{align*}$$

$$\mathcal{I_A}+\mathcal{I_B}=\frac{193}{324}-\frac{82}{81}=-\frac{5}{12}$$