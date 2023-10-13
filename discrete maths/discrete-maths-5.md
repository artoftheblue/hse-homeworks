## Problem 5.1

Given set $U$ that contains $n$ elements. How many possiblities to choose two subsets $A, B$ in $U$ such that 

### Subproblem A

Sets $A \cap B = \varnothing$.

For every element in $U$, we need to distribute this element either to $A$, to $B$, or to neither sets. Thus, there are $3$ options to distribute each element somewhere and we need to find all words of length $n$ in an alphabet of $3$ elements.

Therefore, there are $3 \times 3 \times \dots \times 3=3^n$ possible variants to choose two such subsets.

Answer: $3^n$

### Subproblem B

Set $A \subseteq B$.

First, choose some set $B$. For each element in $U$, either choose this element to be in $B$ or not. In total, similarly as above, find the number of words of length $n$ in the alphabet of $2$ elements. There would be $2^n$ such subsets.

Now, for each $B$, choose some subset $A\subseteq B$.

Consider subset $B$ of size $k$. There are $n\choose k$ ways to choose a subset of size $k$ out of $U$. Afterwards, there are $2^k$ ways to choose $k$ elements out of such subset $B$ so that $A \subseteq B$ would hold. In total, it also evaluates to

$${n \choose 0} 2^0+{n\choose 1}2^1+\dots+{n\choose n - 1}2^{n-1}+{n\choose n}2^n=(1 + 2)^n=3^n$$

> I assume that an easier approach might have been applying the approach in the first task but instead distibuting each of the elements in $U$ to one of three options (either no set, only set $B$, or both sets). Then, the solution is identical to subproblem $A$

Answer: $3^n$

## Problem 5.2

Find the number of such routes from $(0, 0)$ to $(n, n)$ that each step is either $\mathcal{S}_1=(1, 0)$ or $\mathcal{S}_2=(0, 1)$ and in each point $(x, y)$ of the route the inequation $|x-y|\leq 1$ is true.

Consider a subsequence of steps that sends us from $(k, k) \mapsto (k + 1, k + 1)$, maintaining the $|x-y|\leq 1$ restriction.

Look closer at two options:

* $\mathcal{S}_1$ is first: $(k, k) \xrightarrow{\mathcal{S}_1} (k + 1, k)$. The only possible next step is $\mathcal{S}_2$ since otherwise $|x-y|\leq 1$ restriction does not hold.
* $\mathcal{S}_2$ is first: $(k, k) \xrightarrow{\mathcal{S}_2} (k, k + 1)$. The only possible next step is $\mathcal{S}_2$ since otherwise $|x-y|\leq 1$ restriction does not hold.

Therefore, we have only $2$ possible options for $(k, k) \mapsto (k+1,k+1)$:

* $(k, k) \xrightarrow{\mathcal{S}_1} (k + 1, k) \xrightarrow{\mathcal{S}_2} (k + 1, k + 1)$
* $(k, k) \xrightarrow{\mathcal{S}_2} (k, k + 1) \xrightarrow{\mathcal{S}_1} (k + 1, k + 1)$

Overall, the number of possible routes would be equal to words of length $n-1$ from the alphabet $\{\mathcal{S_1},\mathcal{S_2}\}$. In total, the answer would be $2^{n-1}$.

Answer: $2^{n-1}$

## Problem 5.3

Define $Z_n$ as the number of binary words of length $n$ that do not contain two zeros in a row. Prove that $Z_n = F_{n+2}$ for all $n\geq1$.

Write out how $Z_n$ is calculated to figure out the pattern:

| $n$ | values | end with $0$ | end with $1$ | total |
|-:|:-|:-:|:-:|:-:|
| $1$ | $0, 1$ | $1$ | $1$ | $2$ | 
| $2$ | $01, 10, 11$ | $1$ | $2$ | $3$ |
| $3$ | $010, 011, 101, 110, 111$ | $2$ | $3$ | $5$ |
| $4$ | $0101, 0110, 0111, 1010, 1011, 1101, 1110, 1111$ | $3$ | $5$ | $8$ |
| $5$ | $01010, 01011, 0111, 01110, 01111, 10101, 10110, \\ 10111, 11010, 11011, 11101, 11110, 11111$ | $5$ | $8$ | $13$ |
| $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ |  $\vdots$ |

Awesome, so the way how the next value $Z_n$ is defined is the following, considering that $k_{(n)0}, k_{(n)1}$ are the counts of words that end with $0, 1$ in $Z_n$:

* Take all $k_{(n-1)0}$ values, then increase the length of the word by $1$ by adding one $1$ as the last letter.
* Take all $k_{(n-1)1}$ values, then increase the length of the word by $1$ by adding either one $1$ or one $0$ as the last letter.

Now, $Z_n= k_{(n-1)1}+(k_{(n-1)0}+k_{(n-1)1})=k_{(n-1)1}+Z_{n-1}$. Since per definition $k_{(n-1)1}=k_{(n-2)1}+k_{(n-2)0}=Z_{n-2}$, then $Z_n = Z_{n-2} + Z_{n-1}$. We have calculated the base to be $Z_1 =F_3= 2$ and $Z_2 = F_4 = 3$. Therefore, since induction base and induction step have been calculated and checked and the definition of the algorithm is deterministic, $Z_n = F_{n}+F_{n+1}=F_{n+2}, n \geq 1$, q. e. d.

## Problem 5.4

Give the combinatorial proof of the equation

$$\sum_{j=0}^k{r \choose j}{s \choose k - j}={r + s \choose k}$$

Suppose there are two sets that contain $r$ and $s$ values each. In how many ways can we create a subset that contains $k$ elements? This is precisely the definition of a combination, therefore the answer to this question would be ${r+s\choose k}$.

Alternatively, we could sum the number of subsets of length $k$. The number of valid options would a subset of $j$ elements from the first set and $k − j$ elements from the second set. Take combinations of $r\choose j$ and $s \choose k -j$ respectively and multiply them together as they are dependent. The total would indeed be $\sum_{j=0}^k{r \choose j}{s \choose k - j}$.

Therefore, by double counting proof, we get $\sum_{j=0}^k{r \choose j}{s \choose k - j}={r + s \choose k}$, q. e. d.
