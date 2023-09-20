## Problem 1.8

Is $\sqrt{2} + \sqrt{3}$ rational?

#### Solution

It is known that $\forall x \in \mathbb{Q} \colon x^2 \in \mathbb{Q}$. Therefore, we need to check whether this is true for $\sqrt{2} + \sqrt{3}$. Suppose $\sqrt{2} + \sqrt{3} \in \mathbb{Q}$.

$$(\sqrt{2} + \sqrt{3})^2 = 2 + 2 \cdot \sqrt{2}\sqrt{3} + 3 = 5 + 2\sqrt{6}$$ 

$\sqrt{6} \in \mathbb{R} \Rightarrow 2\sqrt{6} \in \mathbb{R} \Rightarrow 5+2\sqrt{6} \in \mathbb{R}$. The sum of a rational number and a product of an irrational and a rational one is irrational. Since $(\sqrt{2} + \sqrt{3})^2 \in \mathbb{R}$, then $\sqrt{2} + \sqrt{3} \notin \mathbb{Q}$, q. e. d.

#### Answer

$$\sqrt{2} + \sqrt{3} \notin \mathbb{Q}$$

## Problem 1.9 

### Subproblem A

Evaluate $\frac{1}{1\cdot5} + \frac{1}{5\cdot9}+\dots+\frac{1}{(4n-3)(4n+1)}$.
$$
$$
#### Solution
$$a_n=\frac{3n-2}{4n-3}-\frac{3n+1}{4n+1}=\frac{(3n-2)(4n+1) + (3n+1)(4n -3)}{(4n-3)(4n+1)}$$
$$=\frac{12n^2-5n-2-(12n^2-5n-3)}{(4n-3)(4n+1)}=\frac{1}{(4n-3)(4n+1)}$$
$$\frac{1}{1\cdot5} + \frac{1}{5\cdot9}+\dots+\frac{1}{(4n-3)(4n+1)}=\underbrace{\frac{1}{1} - \frac{4}{5}}_{a_1}+ \underbrace{\frac{4}{5} - \frac{7}{9}}_{a_2}+ \underbrace{\frac{7}{9} - \frac{10}{13}}_{a_3}+\dots+\underbrace{\frac{3n-2}{4n-3}-\frac{3n+1}{4n+1}}_{a_n}=$$
$$=1 - \frac{3n+1}{4n+1}=\frac{4n+1-3n+1}{4n+1}=\frac{n+2}{4n+1}$$

#### Answer

$$\frac{n+2}{4n+1}$$

### Subproblem B

Evaluate $\frac{1}{2}+\frac{3}{2^2}+\dots+\frac{2n-1}{2^n}$.

#### Solution

$$S = \frac{1}{2}+\frac{3}{2^2}+\dots+\frac{2n-1}{2^n}$$

Multiply the sequence by $\frac{1}{2}$:

$$\frac{1}{2}S=\frac{1}{2^2}+\frac{3}{2^3}+\dots+\frac{2n-1}{2^{n+1}}$$

Subtract the resulting sequence from the original one:

$$S - \frac{1}{2}S=\frac{1}{2}+\frac{3}{2^2}+\dots+\frac{2n-1}{2^n}-\frac{1}{2^2}-\frac{3}{2^3}-\dots-\frac{2n-1}{2^{n+1}}=$$
$$=\frac{1}{2}+\underbrace{\frac{3}{4}-\frac{1}{4}}_{\frac{1}{2}}+\underbrace{\frac{5}{8}-\frac{3}{8}}_{\frac{1}{4}} + \dots + \underbrace{\frac{2n-1}{2^n} - \frac{2n-3}{2^n}}_{\frac{1}{2^{n-1}}}-\frac{2n-1}{2^{n+1}}$$

Simplify and rearrange the elements:

$$\frac{1}{2}S+\frac{2n-1}{2^{n+1}}-\frac{1}{2}=\frac{1}{2}+\frac{1}{4}+\frac{1}{8}+\dots+\frac{1}{2^{n-1}}$$

The right part of the equation is a geometric progression, therefore we may apply the formula $\frac{q (b_1^k-1)}{q-1}$, where $k=n-1$, $b_1 = \frac{1}{2}$, and $q=\frac{1}{2}$.

$$\frac{1}{2}S+\frac{2n-1}{2^{n+1}}-\frac{1}{2}=\frac{\frac{1}{2}(\frac{1}{2}^{n-1}-1)}{\frac{1}{2}-1}=\frac{\frac{1}{2^n}-\frac{1}{2}}{-\frac{1}{2}}=1-\frac{1}{2^{n-1}}$$

Now evaluate $S$:

$$\frac{1}{2}S+\frac{2n-1}{2^{n+1}}-\frac{1}{2}=1-\frac{1}{2^{n-1}}$$
$$S=-\frac{2n-1}{2^{n}}-\frac{1}{2^{n-2}}+3=\frac{3\cdot2^{n}-2n-3}{2^n}=\frac{3(2^n-1) - 2n}{2^n}$$

#### Answer

$$\frac{3(2^n-1) - 2n}{2^n}$$

## Problem 1.10

Prove that $\sqrt{n} < \frac{1}{\sqrt{1}} + \frac{1}{\sqrt{2}} + \dots + \frac{1}{\sqrt{n}}<2\sqrt{n}$, for $n\geq2$ by induction.

#### Solution

Prove the first part of the double inequation:

$$\sqrt{n}<\frac{1}{\sqrt{1}}+\frac{1}{\sqrt{2}}+\dots+\frac{1}{\sqrt{n}}$$

Check whether the inequation is true for $n=2$ **(induction base)**:

$$\frac{1}{\sqrt{1}}+\frac{1}{\sqrt{2}}=\frac{\sqrt{2} + 1}{\sqrt{2}}=\frac{2+\sqrt{2}}{2}=1+\frac{\sqrt{2}}{2}$$
$$\sqrt{2}<1+\frac{\sqrt{2}}{2}\Rightarrow\frac{\sqrt{2}}{2}<1\Rightarrow\sqrt{2}<2,$$

which is true.

Therefore, now we need to prove the **induction hypothesis** that

$$\sqrt{n}<\frac{1}{\sqrt{1}}+\frac{1}{\sqrt{2}}+\dots+\frac{1}{\sqrt{n}}$$

Check whether the equation would be true if we were to add $\frac{1}{\sqrt{n+1}}$ to it (**induction step**):

$$\sqrt{n}+\frac{1}{\sqrt{n+1}}<\frac{1}{\sqrt{1}}+\frac{1}{\sqrt{2}}+\dots+\frac{1}{\sqrt{n}}+\frac{1}{\sqrt{n+1}}$$

$$\frac{\sqrt{n}\sqrt{n+1}+1}{\sqrt{n+1}}<\frac{1}{\sqrt{1}}+\frac{1}{\sqrt{2}}+\dots+\frac{1}{\sqrt{n}}+\frac{1}{\sqrt{n+1}}$$

Estimate the equation on the lefthand side above against $\sqrt{n+1}$:

$$\frac{\sqrt{n}(n+1)+\sqrt{n+1}}{n+1}>\sqrt{n+1}$$
$$\sqrt{n}(n+1)+\sqrt{n+1}>n\sqrt{n+1}+\sqrt{n+1}$$
$$\sqrt{n}(n+1)>n\sqrt{n+1}$$
$$\sqrt{n+1}>\sqrt{n}\Rightarrow$$
$$\Rightarrow\sqrt{n+1}<\frac{1}{\sqrt{1}}+\frac{1}{\sqrt{2}}+\dots+\frac{1}{\sqrt{n+1}}$$

q. e. d.

Prove the second part of the double inequation:

$$\frac{1}{\sqrt{1}} + \frac{1}{\sqrt{2}} + \dots + \frac{1}{\sqrt{n}}<2\sqrt{n}$$

Similarly as above, check the **induction base** for $n$:

$$\frac{1}{\sqrt{1}} + \frac{1}{\sqrt{2}}<2\sqrt{2}$$
$$\frac{\sqrt{2} + 1}{\sqrt{2}}<2\sqrt{2}$$
$$\frac{2 + \sqrt{2}}{2}<2\sqrt{2}$$
$$2 + \sqrt{2}<4\sqrt{2}$$
$$\frac{2}{3}<\sqrt{2},$$

which is true.

**Induction hypothesis:**

$$\frac{1}{\sqrt{1}} + \frac{1}{\sqrt{2}} + \dots + \frac{1}{\sqrt{n-1}}<2\sqrt{n-1}$$

**Induction step:** add one last element ($\frac{1}{\sqrt{n}}$) to each half of the hypothesis. This way we would be able to eventually arrive from the **induction base** to any $n$. 

$$\frac{1}{\sqrt{1}} + \frac{1}{\sqrt{2}} + \dots + \frac{1}{\sqrt{n-1}} + \frac{1}{\sqrt{n}}<2\sqrt{n-1}+\frac{1}{\sqrt{n}}$$

It would be sufficient to prove the following because due to the **transition property** if $2\sqrt{n-1} + \frac{1}{\sqrt{n}}<2\sqrt{n}$ would be true, then $\frac{1}{\sqrt{1}} + \frac{1}{\sqrt{2}} + \dots + \frac{1}{\sqrt{n-1}}+\frac{1}{\sqrt{n}}<2\sqrt{n}$ would also be true.

$$2\sqrt{n-1} + \frac{1}{\sqrt{n}}<2\sqrt{n}$$
$$2\sqrt{n-1}\sqrt{n}<2n-1$$
$$4n^2-4n<4n^2-4n+1$$
$$0<1,$$

q. e. d.

Therefore, 

$$\frac{1}{\sqrt{1}} + \frac{1}{\sqrt{2}} + \dots + \frac{1}{\sqrt{n}}<2\sqrt{n}$$

Lastly,

$$\sqrt{n}<\frac{1}{\sqrt{1}}+\frac{1}{\sqrt{2}}+\dots+\frac{1}{\sqrt{n}}<2\sqrt{n},$$

q. e. d.

## Problem 1.11

Given $n$ **skew lines** and an Euclidean plane, find how many regions the lines divide the plane into.

*I will assume that **skew lines** are such lines that no three lines intersect in a single point and which are not parallel to each other because otherwise the task does not make sense. Generally, the term **skew lines** is used for three-dimensional spaces.*

#### Solution

Evaluate first couple of $n$ to find a pattern.

|lines|number of region|comment|
|-:|:-|:-:|
|$0$|$a_0=1$|$1$ original plane|
|$1$|$a_1=2$|we had $1$ region, got $2$
|$2$|$a_2=4$|new line intersects $1$ existing line, creating $2$ new regions 
|$3$|$a_3=7$|new line intersects $2$ existing lines, creating $3$ new regions
|$4$|$a_4=11$|new line intersects $3$ existing lines, creating $4$ new regions
|$\vdots$|$\vdots$|$\vdots$
|$n$|$a_n=a_{n-1}+n$|new line intersects $n-1$ existing lines, creating $n$ new regions|

Therefore, if there are already $n$ lines and a new ($n+1$)-st line is added, the new line would intersect each of the already existing lines. Those intersections would divide the new line into a certain number ($k+1$) segments. Each of those segments divides one previous region into two new ones (since the regions are convex polygons). Thus, our hypothesis is correct. 

We can look at the formula a little bit closer and see that there is an arithmetic progression inside:

$$a_n=a_{n-1}+n=1 + 1 + 2 + 3 + 4 + \dots + n-1 + n=1+\frac{n(n+1)}{2}$$

#### Answer

$$1+\frac{n(n+1)}{2}$$