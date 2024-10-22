# Microeconomics, Homework 3

## Problem 1

Two countries are separated by the ocean and shipping costs are $t$ dollars per unit of quantity. Transporation costs are paid by the exporting firm. Each of the two firms sells both at home and abroad competing in outputs. Total output sold in country $1$ is $Q_1=q_1^h+q_1^f$ and in country $2$, $Q_2=q_2^h+q_2^f$, respectively, where by $h$ we denote production for the home market and with $f$, production for the foreign market. Market demand for both markets are is defined as $p_i(q_i)=a-bQ_i,i=\{1,2\}$. Marginal costs of production can be neglected. Find equilibrium outputs $(q_1^h,q_1^f,q_2^h,q_2^f)$ and equilibrium prices. You may refer to the thorem on symmetric equilibrium if you wish.

---

Cournot model goes brrr:

Firstly, write down the profit of the first firm on the first market:

$$\pi_1^1=p_1q_1=(a-bq_1-bq_2)q_1=(a-bq_2)q_1-bq_1^2\to\max_{q_1}$$

Maximizing this, we get

$$q_1^1=\max\left\{0,\frac{a-bq_2}{2b}\right\}$$

which is non-zero for $q_2\leq\frac{a}{b}$ and zero otherwise.

Profit of the second firm on the first market -- here we have to also account for the tax.

$$\pi_2=p_1q_2-tq_2=(a-bq_1-bq_2)q_2-tq_2=(a-bq_1-t)q_2-bq_2\to$$

Thus we get optimum 

$$q_2^1=\max\left\{0,\frac{a-bq_1-t}{2b}\right\}$$

which is non-zero for $q_1<\frac{a-t}{b}$ and zero otherwise.

> The thing above would be completely identical due to the symmetric equilibrium theorem because we have completely equivalent demand and costs functions.

Now we shall consider all four cases where quantities are either zero or non-zero:

### Case 1

Merging two non-zero cases $q_1=\frac{a+t}{3b}$ and $q_2=\frac{a-2t}{3b}$, we get final restriction of $a>2t$.

### Case 2

Merging cases $q_1=0$ and $q_2=\frac{a-t}{2b}$, we realize that this case is impossible because the restrictions intersect with each other.

### Case 3 

Merging cases $q_1=\frac{a}{2b}$ and $q_2=0$, we get final restriction of $a\leq 2t$, which is directly inverse to case one.

### Case 4

Case for $q_1=0,q_2=0$ is trivial and occurs when $a=0$.

---

Plugging the quantities in the equations, we get equilibirum prices, thus they are

$$p'=\frac{a}{2},\quad p''=\frac{a+t}{3}$$

first case being for $a\in(0, 2t]$ and second case being for $a\in(2t,+\infty)$

Thus we get two sets of answers:

1. $a\in(0, 2t]\colon$

$$(q_1^h,q_1^f,q_2^h,q_2^f, p_1, p_2)=\left(\frac{a}{2b},0,\frac{a}{2b},0,\frac{a}{2},\frac{a}{2}\right)$$

2. $a\in(2t,+\infty)\colon$

$$(q_1^h,q_1^f,q_2^h,q_2^f, p_1,p_2)=\left(\frac{a+t}{3b},\frac{a-2t}{3b},\frac{a+t}{3b},\frac{a-2t}{3b},\frac{a+t}{3},\frac{a+t}{3}\right)$$

## Problem 2

$N\geq 2$ identical firms with zero marginal costs enter the consumer market in the form of a circular city which length is $1$. Consumers are uniformly distributed along this circle and each of the consumers is willing to buy $1$ unit of good produced by these firms. Upon entry, each firm pays $f$ dollars for the license. Transportation costs of a consumer is defined as $\alpha x^2$, where $\alpha > 0$ and $x$ is the distance from a consumer to the closest seller-producer. 

### Subproblem A

Assuming that all distances between adjacent firms are the same and firms act as monopolists towards respective market segments, find how $p_1$ and $p_{i-1}$ are related if $p_i$ and $p_{i-1}$ are prices set by the corresponding firms.

---

Firsly, it's fair to due to the uniform distribution that the firms would be attracting $\frac{1}{N}=d$ of the market to themselves. People between adjacent firms would only choose between those two firms. There would be people equiproxime up to the transportation cost to each of the firms who would randomly choose between two firms with equal probabilities so thus we get that all firms get identical shares of the market equal to distance $x$.

Thus we need to maximize profit for each of the firms. The profits would be the same up to index $i\equiv i-1$:

$$\pi_{i-1}=p_{i-1}x-f\to\max$$

Now we need to find the value of $x$. Let's consider the equiproxime buyer:

$$p_i+\alpha(d-x)^2=p_{i-1}+\alpha x^2$$

$$x=\frac{\frac{p_i}{d^2}+\alpha-\frac{p_{i-1}}{d^2}}{2\alpha\frac{1}{d}}$$

$$x=\frac{p_i+\alpha d^2-p_{i-1}}{2d\alpha}$$

Plug it into the profit function:

$$\pi_{i-1}=\frac{p_{i-1}(p_i+\alpha d^2-p_{i-1})}{2d\alpha}-f\to\max$$

Maximizing this monstrosity, we get

$$p_{i-1}=\max\left\{\frac{p_1+\alpha d^2}{2},0\right\}$$

> I'm intentionally using $\max$ functions in order to eliminate cases when profit is negative. In these cases the firm would simply not enter the market.

> Considering the the distribution is uniform, we would always have some consumers willing to buy from each firm.

---

Now, we need to check for what prices profit would be negative. Plug the optimum price into the profit function and assume it should be greater than zero. 

We get

$$\frac{(p_i+\alpha d^2)^2}{2\alpha d}-f>0\implies p_1>2\sqrt{2\alpha fd}-\alpha d^2$$

Looking at the second firm (this exercise is up to the one who would be checking it because it is completely identical up to the index), we get the very same profit maximization problem thus we may get that 

$$\boxed{\left(p_i,p_{i-1}\right)=\left(\frac{p_i+\alpha d^2}{2},\frac{p_{i-1}+\alpha d^2}{2}\right)}$$

given that 

$$\forall j\in\{i, i-1\}\colon p_j>2\sqrt{2\alpha f d}-\alpha d^2$$

would be our answer.

### Subproblem B

By applying first-order condition to the profits of the $i$-th and the and the $i-1$-th firms show that the equilibirium in the whole market is symmetric.

---

We may plug equaltions for prices into each other to show that they would be identical, which would prove the required condition considering identical costs and profit functions. Thus, the market would be symmetric.

$$p_{i-1}=\frac{p_{i-1}+\alpha d^2}{4}+\frac{\alpha d^2}{2}=\alpha d^2=p_i$$

Completely identical for $p_{i}$, thus we have shown that the market is symmetrical.

### Subproblem C

Given the license cost $f$, find the maximum number of firms $N$ that enter the market.

---

Let's plug $d=\frac{1}{N}$ back and try to increase the price until it would be equal to the expression in the previous subproblem.

$$2\sqrt{2}\sqrt{\frac{\alpha f}{N}}-\frac{\alpha}{N^2}\leq\frac{\alpha}{N^2}$$

$$\frac{8\alpha f}{N^2}\leq\frac{4\alpha^2}{N^4}$$

$$2 f\leq\frac{\alpha}{N^2}$$

$$\boxed{N=\sqrt{\frac{\alpha}{2f}}}$$

## Problem 3

Assume that an investor has a million dollars that can be invested in a certain asset. Investing $X\in[0, 1]$, she will recieve $r_HX$ in addition to $X$ with probability $\mathbb{P}$ and will lose $r_LX$ with probability $1-\mathbb{P}$. Assume that $1>r_i>0$ where $i=H, L$. The preferences of the investor can be represented by the VNM utility function with $u(w)=\ln w$.

### Subproblem 1

Assume that the optimal size of investment in the asset is strictly positive and less than one million dollars. Find the optimal amount the investor chooses to invest as a function of $r_H, r_L$, and $\mathbb{P}$.

---

The chance that a desirable outcome happens is $\mathbb{P}$. The chance that an undesirable outcome happens is $1-\mathbb{P}$.

Respectively, the investor's total profit would be $1\,000\,000+r_HX$ and $1\,000\,000-r_LX$.

The goal of the task is to maximize expected profit:

$$\mathbb{E}[\Pi]=\mathbb{P}\ln(1\,000\,000+r_HX)+(1-\mathbb{P})\ln(1\,000\,000-r_LX)\to\max_{X}$$

and there is also a restiction on the amount we can invest:

$$0\leq X\leq1\,000\,000$$

To maximize this, simply take the derivative:

$$\frac{\mathbb{P}r_H}{1\,000\,000+r_HX}-\frac{(1-\mathbb{P})r_L}{1\,000\,000-r_LX}=0$$

and eventually get $X$ out of here:

$$\mathbb{P}r_H(1\,000\,000-r_LX)-(1-\mathbb{P})r_L(1\,000\,000+r_HX)=0$$

$$1\,000\,000(\mathbb{P}r_H-(1-\mathbb{P})r_L)-(r_L\mathbb{P}r_H+r_H(1-\mathbb{P})r_L)X=0$$

$$X(r_H,r_L,\mathbb{P})=\min\left\{\max\left\{0, 1\,000\,000\times\frac{\mathbb{P}r_H-(1-\mathbb{P})r_L}{r_Lr_H}\right\},1\,000\,000\right\}$$

Ideally we also should have the second derivative of $\mathbb{E}[\Pi]<0$ because otherwise the optimum wouldn't be internal.


### Subproblem 2

For which values of $r_H, r_L$ and $\mathbb{P}$ will the optimal investment amount be equal to zero (she will not invest at all)? Explain the economic intuition behind your answer.

---

To be honest, I have already solved the entirety of the task above, and since I'm running out of time I'll just say that this is inferred from the multiexpression above:

$$1\,000\,000\times\frac{\mathbb{P}r_H-(1-\mathbb{P})r_L}{r_Lr_H}\leq0$$

$$\mathbb{P}r_H-(1-\mathbb{P})r_L\leq0$$

$$\mathbb{P}\leq \frac{r_L}{r_H+r_L}$$

This happens because the expected return amount is always lower than the amount invested when we also take risk into account (return rate is less than 1). That's basically what happens in casinos aka why you should never play in them.

### Subproblem 3

For which values of $r_H, r_L$ and $\mathbb{P}$ will the optimal investment amount be equal to one million dollars (she will invest all the money she has)? Explain your answer.

---

Very similar situation here, it happens whenever this expression is 

$$1\,000\,000\times\frac{\mathbb{P}r_H-(1-\mathbb{P})r_L}{r_Lr_H}\geq1\,000\,000$$

aka

$$\frac{\mathbb{P}r_H-(1-\mathbb{P})r_L}{r_Lr_H}\geq 1$$

$$\mathbb{P}\geq \frac{r_L(r_H+1)}{r_H+r_L}$$

here the expected acceptable return rate is higher than $1$ thus in addition to risks thus here it is rational to invest more than we have given the potential profit, however we simply don't have infinite money so we have to just invest all we have.