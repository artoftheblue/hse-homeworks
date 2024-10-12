# Microeconomics, Homework 1

## Problem 1

The cost function of a non-discriminating monopolist is $c(y)=cy$, and the inverse demand function is $p(y)=a-by^d$, where $a, b, c, d > 0$ are some parameters such that an equilibrium exists.

### Subproblem A

Find the elasticity of demand as a function of output $y$. Calculate the Lerner index.

---

Firstly, transform the inverse demand function into an explicit demand function:

$$p=a-by^d$$

$$by^d=a-p$$

$$y^d=\frac{a-p}{b}$$

$$y=\sqrt[d]{\frac{a-p}{b}}$$

We know that elasticity is 

$$\varepsilon^y_p=\frac{\partial y}{\partial p}\frac{p}{y}$$

Find the derivative first:

$$\frac{\partial}{\partial p}\left(\sqrt[d]{\frac{a-p}{b}}\right)=\left(\frac{a-p}{b}\right)^{(\frac{1}{d}-1)}\times-\frac{1}{b}\times\frac{1}{d}=-\frac{\left(\frac{a-p}{b}\right)^{(\frac{1}{d}-1)}}{bd}$$

Now plug everything into the formula:

$$\varepsilon^y_p=-\frac{\left(\frac{a-p}{b}\right)^{(\frac{1}{d}-1)}}{bd}\frac{p}{\sqrt[d]{\frac{a-p}{b}}}=-\frac{p}{bd\left(\frac{a-p}{b}\right)}=-\frac{p}{d(a-p)}$$

Since we wanted this to be a function of y, we get 

$$\boxed{\varepsilon^y_p(y)=-\frac{a-by^d}{d(a-a+by^d)}=-\frac{a-by^d}{dby^d}}$$

---

Find the Lerner index, which is defined by

$$L=\frac{p-MC}{p}$$

$$MC=p(y)'_y=c$$

Plug $p$ into the formula:

$$\boxed{L=\frac{a-by^d-c}{a-by^d}=1-\frac{c}{a-by^d}}$$

### Subproblem B

Find an equilibirum.

---

The profit function of the monopolist is

$$\pi(y)=TR(y)-TC(y)$$

where

$$TR(y)=p(y)y=(a-by^d)y$$

$$TC(y)=c(y)=cy$$

$$\pi(y)=(a-by^d)y-cy\to\max$$

To maximize this function of one variable, find its derivative and equate it to zero:

$$\frac{\partial\pi}{\partial y}=a-(d+1)by^d-c=0$$

We get the optimal output as follows, which is our sought-for equilibrium.

$$\boxed{y^*=\sqrt[d]{\frac{a-c}{b(d+1)}}}$$

Optimal price at the equilibrium would be

$$p^*=a-by^d=a-\frac{a-c}{d+1}=\frac{ad+c}{d+1}$$$

### Subproblem C

Prove that the monopoly output is lower than if the price is equal to the marginal cost (the case of perfect compeition).

---

The output for $p=MC=c$ would be:

$$y=\sqrt[d]{\frac{a-c}{b}}$$

Compare it to the equilibrium output we have found above:

$$\sqrt[d]{\frac{a-c}{b(d+1)}}\sim\sqrt[d]{\frac{a-c}{b}}$$

$$\frac{1}{(d+1)}\sim 1$$

Given that $d\neq0$ since that would be the case when $p=c$, $\frac{1}{d+1}$ is always lesser than $1$ for all given $d>0$.

This implies that the monopoly output would be lower than the perfect competition case since $d>0$ and the monopoly output is $d+1$ times smaller than the PC case one.

### Subproblem D

Calculate consumer surplus and producer surplus at the equilibrium point.

---

To calculate consumer surplus, we simply take the integral of the difference between implicit demand function and the optimal demand (the result is kinda scary by itself though).

$$\begin{align*}CS&=\int^{y^*}_0p(y)-p^*dy=\int^{y^*}_0\left(a-by^d-\frac{ad+c}{d+1}\right)dy\\
&=\int^{y^*}_0\left(-by^d+\frac{a-c}{d+1}\right)dy=\left(-\frac{by^{d+1}}{d+1}+\frac{a-c}{d+1}y\right)\biggm|_0^{y^*}\\
&=-\left(\frac{a-c}{b}\right)\sqrt[d]{\frac{a-c}{b(d+1)}}+\frac{a-c}{d+1}\sqrt[d]{\frac{a-c}{b(d+1)}}\\
&=\boxed{\sqrt[d]{\frac{a-c}{b(d+1)}}\left(\frac{a-c}{d+1}-\frac{a-c}{b}\right)}
\end{align*}
$$

To calculate producer surplus for this case with no fixed costs (costs which are independent of volume of product), we simply take the profit:

$$\begin{align*}PS&=\pi(y^*)=(a-by^{*d})y^*-cy^*\\&=\left(a-b\frac{a-c}{b(d+1)}\right)\sqrt[d]{\frac{a-c}{b(d+1)}}-c\sqrt[d]{\frac{a-c}{b(d+1)}}
=\boxed{\left(\frac{ad-cd}{d+1}\right)\sqrt[d]{\frac{a-c}{b(d+1)}}}
\end{align*}$$

### Subproblem E

Let the monopolist be taxed in the amount of $t$ per each unit of output. Find a new equilibrium.

---

If we are taxed amount $t$ for each output unit, we have to take that into account in our costs function:

$$TC(y)=c(y)=(c+t)y$$

$$\pi(y)=(a-by^d)y-(c+t)y\to\max$$

We get the equilibrium in a similar way as we did above:

$$\frac{\partial\pi}{\partial y}=a-(d+1)by^d-c-t=0$$

$$\boxed{y^*_t=\sqrt[d]{\frac{a-c-t}{b(d+1)}}}$$

Optimal price at the equilibrium would be

$$p_t=a-by^d=a-\frac{a-c-t}{d+1}=\frac{ad+c+t}{d+1}$$$

### Subproblem F

How much will the price change after the tax is introduced? How does this value depend on $d$ (is this relation positive or negative)? Give an intuitive explanation of this dependence based on elasticity.

---

As we have calculated above, the price changes by

$$p_t-p=\frac{ad+c+t}{d+1}-\frac{ad+c}{d+1}=\frac{t}{d+1}$$

The relation is **inverse**, the higher $d$ is, the less the consumer would have to pay for it. Effectively, we transfer the tax burden onto consumers.

Given our elasticity of

$$\varepsilon^y_p=-\frac{a-by^d}{dby^d}$$

which implies that if our price grows $\frac{1}{d}$-fold, then the demand for it would decrease proportionally. Intuitively, the impact $d$ on the demand and on the price scales inversely with increasing values of $d$. (The higher $d$ is, the less demand there is among consumers.) This also implies that $d$ would lead to the monopolist scaling her prices along with it (increasing the $d$-exponent would lead to lower prices).

Regarding elasticity, the higher $d$ is, the less elastic the demand would be 
as small changes in price would not affect consumers nor the monopolist as much. 

Overall, $d$ variable has a fun effect of stablizing the prices through scaling them by lowering elasticity.

## Problem 2

Let here be two submarkets with aggregated demand functions $y_1(p_1)=a-p_1$ and $y_2(p_2)=b-p_2$, where $a, b$ are some positive parameters and $a>b$. A monopolist firm is characterized by a cost function $c(y)=cy$, where $y$ is aggregate output $y=y_1+y_2$ and $c$ is a positive parameter.

### Subproblem A

Find its profit provided that the firm is a monopolist and conducts third-type discrimination in submarkets.

---

Third-type discrimination means that we segregate markets. Therefore, we may set the aggregate prices $p_1,p_2$ different to different markets and the maximize our profit.

We want to maximize our profit for each market separately. In order to do it, multiply revenue by demand and subtract costs:

$$\pi_1=p_1y_1(p_1)-c(y)=p_1(a-p_1)-cy\to\max$$

$$\pi_2=p_2y_2(p_2)-c(y)=p_2(b-p_2)-cy\to\max$$

The optimums would be

$$a-2p_1-c=0\implies p_1=\frac{a-c}{2}$$

$$b-2p_2-c=0\implies p_2=\frac{b-c}{2}$$

And the optimal production would be 

$$y_1=a-\frac{a-c}{2}=\frac{a+c}{2}$$

$$y_2=b-\frac{b-c}{2}=\frac{b+c}{2}$$

Total profit then would be 

$$\begin{align*}\pi&=\pi_1+\pi_2=\max\left\{\frac{a-c}{2}\frac{a+c}{2}-c\frac{a+c}{2},0\right\}+\max\left\{\frac{b-c}{2}\frac{b+c}{2}-c\frac{b+c}{2},0\right\}\\
&=\boxed{\max\left\{\frac{a^2-ac}{2}-c^2,0\right\}+\max\left\{\frac{b^2-bc}{2}-c^2,0\right\}}\end{align*}$$

> It has to be said that if costs are higher than $a$ or $b$, then nothing would be bought on the corresponding markets because the monopolist would only sell something if the consumers would pay them instead. This is represented by the $\max$ functions.

### Subproblem B

Let a firm have the opportunity to confuct discrimination of the first type for a fee $F$. Find the maximum cost of $(F)$ for the firm.

---

We are seeking to extract all consumer surplus from the market. Effectively, we're treating every point in an aggregated market as each new person who would be acquiring each next item for a linearly smaller price ranging from $0$ to $a$ (or $b$, respectively).

Since we are given linear functions, we may simply treat CS as areas of triangles under our demand functions.

They would be equilateral and square with a side length of $a$ and $b$ respectively.

> At this point it has to be said that the integrals are not actually calculated from $a, b$ but rather from $c$ because we would not want to sell anything for lower than our costs. Thus, we start selling our products from the maximum possible cost and go lower until we hit the mark when it is not profitable to produce anything anymore.

> Therefore, we need to cut off a piece of the triangle, which I will do using integrals.

> I also consider the case when $a, b > c$ since otherwise the monopolist would not produce anything.

$$CS_a=\int\limits_c^a(a-p)dp=ap-\frac{p^2}{2}\biggm|_c^a=a^2-\frac{a^2}{2}-ac+\frac{c^2}{2}=\frac{a^2+c^2}{2}-ac$$

$$CS_b=\int\limits_c^b(b-p)dp=bp-\frac{p^2}{2}\biggm|_c^b=b^2-\frac{b^2}{2}-bc+\frac{c^2}{2}=\frac{b^2+c^2}{2}-bc$$

Our output in this case would be $(a - c) + (b - c)=a+b-2c$, thus our costs for production would be $(a+b-2c)c$.

Our total profit alongside with consumer surplus (which is basically how much the consumers would have paid us) would also include the costs and would be

$$\begin{align*}\pi&=CS_a+CS_b-c(y)=\frac{a^2+c^2}{2}-ac+\frac{b^2+c^2}{2}-bc-(a+b-2c)c\\
&=\frac{a^2+b^2}{2}-c^2-ac-bc-ac-bc+2c^2=\frac{a^2+b^2}{2}+c^2-2ac-2bc\end{align*}$$

Thus, the maximum fee $F$ would be equal to the profit since the monopolist would obviously not pay more than that:

$$\boxed{F_1=\frac{a^2+b^2}{2}+c^2-2ac-2bc}$$

> Alternatively, it might be implied in the task that the person would only switch to this type of discrimination if they would benefit from it. In this case, the maximum $F$ would be the difference between profits in third type of discrimination and the first type of discrimination. 

$$F_2=F_1-\max\left\{\frac{a^2-ac}{2}-c^2,0\right\}+\max\left\{\frac{b^2-bc}{2}-c^2,0\right\}$$

### Subproblem C

Let each submarket characterize the behaviour of the representative consumer. It is known that the utility functions of each representtative consumer can be written in a quasilinear form: $U_i(x_i)=v(x_i)-px_i$ and $v(0)=0$. Let the monopolist conduct discrimination of the second type. Find the optimal packages that maximize the monopolist's profit from the policy pursued: $(t_x,x), (t_y,y)$. Where $t_i$ is the package price and $x, y$ are quantities in the respective packages.

---

From the given conditions I assume that

* $x, y$ are redefinitions of $a, b$ which are supposed to be independent from the variables from the beginning of the problem 
* utility functions of each representative consumer are the same
* the more accurate form of the utility function is $U_i(x_i)=v(x_i)-t_i$ interpreting this as if a consumer loses a chunk of utility from spending money equal to the cost of the package bought  
* also, I will consider a single case when $x<y$ because the second case is identical up to symmetriy and the case $x=y$ is trivial since the packages are the same. 

Now to the actual solution. Any consumer would choose the package that maximizes their utility. This means that the i-th package would be chosen over j-th for k-th consumer if

$$U_k(x_i)>U_k(x_j)\implies v(x_i)-t_i>v(x_j)-t_j$$

The monopolist profit function would be the revenue from the packages sold minus the costs required to produce the packages

$$\pi=t_x\delta_x+t_y\delta_y-c(x\delta_x+y\delta_y)$$

where

$$\delta_i=\begin{cases}
0, & \text{if no i-th packages are sold},\\
1, & \text{if a single i-th package was sold},\\
2, & \text{if both i-th packages were sold}
\end{cases}$$

Since $v(x)$ is quasilinear, we may determine that it is increasing, thus the optimal price difference would be the difference in utility that the consumers have for each package:

$$t_y-t_x=v(y)-v(x)$$

$$t_y=t_x+(v(y)-v(x))$$

If we wouldn't set the prices to such, then we would be losing consumer surplus that would be gained from switching to an alternative package.

This effectively transforms both functions to the same one.

$$U_i(x)=v(x)-t_x$$

$$U_i(y)=v(y)-t_y=v(y)-t_x-v(y)+v(x)=v(x)-t_x$$

Effectively, we would just use one of the packages as a decoy, not giving people an alternative that would be better than they could switch to. 

Afterwards, we need to decide what $x$ and $y$ to actually take. For this, I haven't actually been able to figure out what to do.

It should be possible to solve this task by using 

$$\begin{cases}v(x)-t_x\geq v(y)-t_v\\
v(y)-t_y\geq v(x)-t_y\\
v(x)-t_x\geq 0\\
v(y)-t_y\geq 0
\end{cases}$$

> The latter two equations follow from the fact that $v(0)=0$ because the function is increasing and quasilinear

## Problem 3

Let there be two submarkets with aggregated demand functions $y_1(p_1)=90-p_1$, and $y_2(p_2)=180-p_2$. A monopolist firm is characterized by a cost function: $c(y)=y$, where $y$ is aggregate output $y=y_1+y_2$. A monopoly firm exists for an infinite number of periods, $n=\infty$, choosing in each period the equilibrium outputs in each of the submarkets $(y_t^1,y_t^2)$. In this case, the firm has preferences regarding intertemporal earnings. Thus, profit in the period $t$ must be discounted at the rate $\rho$, where $\rho\in(0, 1)$. Thus, the firm maximizes the value of 

$$\Pi^*=\sum^\infty_{t=0}\frac{\Pi_t(y^1_t,y_t^2)}{(1+\rho)^t}\to\max_{y_t^1,y_t^2}$$

Each period, market demand is restored to its original state, that is, the monopolist solves the problem of maximizing current profits anew each period. At the same time, he cannot get into debt or make savings for future periods.

* If a monopolist agrees to pay product taxes $t_1=1$ and $t_2=3$ in each of the submarkets, then the state will allow it to act as a monopolist and conduct discrimination of the third type. Thus, the total tax payments will be $T=t_1y_1+t_2y_2$.
* If the firm decides to cheat and not pay the tax on the $i$-th submarket in period $t$, then the government gets angry and deprives it of the right to conduct discrimination in all subsequent periods. In this case, the firm is obliged to set a single monopoly price on both submarkets, but still had to pay a per-product tax on both of the submarkets at a rate of $t=1$.
* If the monopolist completely refuses to pay taxes on both submarkets in period $t$, then the state deprives it of its monopoly rights, forcing to work as a perfect competitive firm in all subsequent periods.

How are the incentives to deviate from $\rho$ related? Write out the optimal behavior of the firm in each period $t$ depending on the discount factor $\rho$. What is the maximum profit of a monopolist firm $\Pi^*(\rho)$? Is it profitable for the firm to deviate in any period? If so, in which one and how exactly: stop paying taxes in one of the submarkets or in both?

---

Taking the infinite geometric series into account and the $\rho$ value, the sum collapses into

$$\Pi=\frac{\Pi_t(y^1_t,y_t^2)}{1-\frac{1}{1+\rho}}=\frac{\Pi_t(y^1_t,y_t^2)}{\frac{\rho}{1+\rho}}=\frac{(1+\rho)}{\rho}\Pi_t(y^1_t,y_t^2)$$

Firstly, let's calculate profit in each independent period. It would be simply a sum of two revenues and total costs:

$$\pi_t=p_1y_1+p_2y_2-(y_1+y_2)$$

Now let's consider each option from above.

### Both taxes are paid

Then the profit would be 

$$\pi_t=p_1y_1+p_2y_2-(y_1+y_2)-(t_1y_1+t_2y_2)$$

$$\pi_t=p_1y_1+p_2y_2-(y_1+y_2)-(y_1+3y_2)$$

$$\pi_t=p_1y_1+p_2y_2-2y_1-4y_2$$

$$\pi_t=p_1(90-p_1)+p_2(180-p_2)-2(90-p_1)-4(180-p_2)$$

Now maximize profit for both prices: 

$$92-2p_1=0\implies p_1=46$$

$$184-2p_2=0\implies p_2=92$$

$$y_1(p_1)=90-46=44$$ 

$$y_2(p_2)=180-92=88$$

$$\pi_t=46\times 44+92\times 88-2\times44-4\times88=9680$$

### One single tax is paid

In this case we set the same price to $p$ and effectively pay double the costs for each good

$$\pi_t=p(y_1+y_2)-(y_1+y_2)-(y_1+y_2)$$

$$\pi_t=p(y_1+y_2)-2y_1-2y_2$$

$$\pi_t=p((90-p)+(180-p))-2(90-p)-2(180-p)$$

$$\pi_t=270p-2p^2-180+2p-360+2p$$

$$\pi_t=274p-2p^2-540$$

Maximizing the profit,

$$274-4p=0\implies p=68.5$$

Now calculate the profit:

$$y_1(p_1)=90-68.5=21.5$$ 

$$y_2(p_2)=180-68.5=111.5$$

$$\pi_t=68.5(21.5+111.5)-2\times21.5-2\times111.5=8844.5$$

### No taxes are paid

$$\pi_t=p(y_1+y_2)-(y_1+y_2)$$

In this case we set the price equal to MC, so the profit function would be 

$$MC=1$$

$$\pi_t=(y_1+y_2)-(y_1+y_2)=0$$

which effectively means that this option is never preferable because competing with all the firms will eventually make the price approach the marginal cost.

---

### Not paying the first tax

If we don't pay the first tax, then we may increase our profit by $45\times45-(46\times44-2\times44)=89$ points in the $t$-th step.

Therefore, we need 

$$\frac{(1+\rho)}{\rho}\Pi_t(y^1_t,y_t^2)>9680+89$$

$$\frac{(1+\rho)}{\rho}9680>9749\implies\rho=\frac{9680}{69}$$

in order to avoid this behaviour and prevent the consumer from ignoring the first tax

### Not paying the second tax

In this case we may increase our profit by $90\times90-(92\times88-4\times88)=356$

$$\frac{(1+\rho)}{\rho}\Pi_t(y^1_t,y_t^2)>9680+356$$

$$\frac{(1+\rho)}{\rho}9680>10036\implies\rho=\frac{2420}{89}$$

### Ignoring both taxes

In this case we may increase our profit by $90\times90+45\times45-9680=445$

$$\frac{(1+\rho)}{\rho}\Pi_t(y^1_t,y_t^2)>9680+445$$

$$\frac{(1+\rho)}{\rho}9680>10125\implies\rho=\frac{1936}{89}$$

---

### Conclusion

Not paying any of the taxes even for a brief period is not beneficial in the long-term whatsoever since we would never be able to go back to higher level of profit and only benefit ephemerally. 

In the cases above the firm switches to not paying a certain tax or taxes if $\rho$ is less than the values calculated.

> What is the maximum profit of the monopolist firm?

It heavily depends on the value of $p$ and can be close to infinity for certain really small values of $\rho$. Therefore I don't think finding "maximum profit of the monopolist firm" is a valid question because it's unbounded.