## Problem 1 

Find the number of surjective non-descending functions from $[10]$ to $[7]$. Function $f$ is non-descending if $x\leq y \Rightarrow f(x) \leq f(y)$.

---

This function is a surjection if $\forall y \in [7], \exists f(x) = y$. Since the function has to be non-descending, then to maintain the surjective property, we absolutely have to assign each value $y\in\{0, 1, 2, 3, 4, 5, 6\}$ some $x\in\{0,1,2,3,4,5,6,7,8,9\}$ and then have relatively free will to choose what $y$ to assign the remaining $10-7=3$ values, maintaining the non-descending property.

Example: Separating $10$ values collapses to separating $3$ values since it's necessary to have at least one value in each group.

$$*\ | ***| **\ | * | * | * | \ *$$

$$\downarrow$$

$$\ | **\ | *| \ | \ | \ |$$

$3$ values need to be separated into $7$ groups. 

$$\left(n\choose k\right)={n+k-1\choose k}=\left(7\choose 3\right)={7 + 3 - 1\choose 3}={9\choose 3}=\frac{9!}{3!\cdot6!}=\frac{7\cdot8\cdot9}{2\cdot3}=3\cdot4\cdot7=84$$

---

**Answer:** $84$


## Problem 2

Prove that 

$$\sum^k_{j=0}{n + j - 1 \choose j}={n + k \choose k}$$

---

$${n - 1 \choose 0}+{n \choose 1}+{n + 1 \choose 2}+\dots+{n + k - 1\choose k}={n + k \choose k}$$

$${n - 1 \choose 0}=1={n\choose0}\Rightarrow$$

$${n \choose 0}+{n \choose 1}+{n + 1 \choose 2}+\dots+{n + k - 1\choose k}={n + k \choose k}$$

$${n \choose k} + {n \choose k + 1}={n + 1 \choose k + 1}\Rightarrow$$

$$\overbrace{{n \choose 0}+{n \choose 1}}^{{n + 1\choose 1}}+{n + 1 \choose 2}+\dots+{n + k - 1\choose k}={n + k \choose k}\Rightarrow$$

$$\overbrace{{n + 1\choose 1}+{n + 1 \choose 2}}^{{n + 2 \choose 2}}+\dots+{n + k - 1\choose k}={n + k \choose k}\Rightarrow$$

$$\vdots$$

$$\overbrace{{n + k - 1 \choose k - 1}{n + k - 1\choose k}}^{{n+k\choose k}}={n + k \choose k}\Rightarrow$$

$${n+k\choose k}={n + k \choose k}$$

q. e. d.

## Problem 3 

How many permutations of ABRACADABRA such that no two A-s are next to each other are there?

---

First, count the number of permutations of BBCDRR:

$${6\choose2,1,1,2}=\frac{6!}{2!\cdot2!}=2\cdot3\cdot5\cdot6=180$$

Afterwards, for X $\in$ {B, C, D, R}, there would be $7$ places for $A$: AXAXAXAXAXAX. Choose 5 of them:

$${7\choose5}=\frac{7!}{2!\cdot5!}=\frac{7\cdot6}{2}=21$$

Now, the final answer would be:

$${6\choose2,1,1,2}{7\choose5}=180\cdot21=3780$$

---

**Answer:** $3780$

## Problem 4

Compare numbers:

$$\sum^{512}_{i=0}2^{2i}{1024\choose 2i} \ \text{and} \ \sum^{511}_{i=0}2^{2i+1}{1024\choose 2i + 1}$$

---

Notice that this is literally a binomial expansion:

$$\sum^{512}_{i=0}2^{2i}{1024\choose 2i} - \sum^{511}_{i=0}2^{2i+1}{1024\choose 2i + 1}=$$

$$={1024 \choose 1024}2^{1024}(-1)^0+{1024 \choose 1023}2^{1023}(-1)^1+\dots+{1024\choose0}2^{0}(-1)^{1024}=(2-1)^{1024}=1^{1024}=1$$

Therefore, the first number is larger.

---

**Answer:**

$$\sum^{512}_{i=0}2^{2i}{1024\choose 2i}$$
