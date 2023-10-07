## Problem 4.1

Function $f$ from set $X$ to set $Y$ is such that for $A \subseteq X, B \subseteq X$, the following is true:

$$f^{-1}[f[A]]=f^{-1}[f[B]]$$

Does the equation $A=B$ follow out of this?

### Solution

Since $f^{-1}[f[A]]=f^{-1}[f[B]]$, then images of $A, B$ should be equal: $f[A]=f[B]$. Find a counterexample: $f$ is a function that returns modulo 2. Let $A=\{2\}$, $B=\{4\}$. $f[A]=f[B]=\{0\}\Rightarrow f^{-1}[f[A]]=f^{-1}[f[B]]$, but $A\neq B$. Therefore, no, the equation does not follow.

**Answer: no :(**

## Problem 4.2

Function $f$ is defined on the set $A\cup B$ and takes arguments from set $Y$. If one were to replace the symbol $?$ in the following equation:

$$f[A \ \triangle \ B]\ ? \ f[A]\ \triangle\ f[B]$$

with one of the symbols $\subseteq$, $\supseteq$, they would get a statement. What of these two statements are true for any $f$?

### Solution

Let $A_0, B_0$ be sets of all values which are included in $A$ but not in $B$ and vice versa. Let $X = A \cap B$. 

Rewrite the equation:

$$f[A \ \triangle \ B]\ ? \ f[A]\ \triangle\ f[B] = f[A_0 \cup X \ \triangle \ B_0 \cup X]\ ? \ f[A_0 \cup X]\ \triangle\ f[B_0 \cup X] =$$

$$=f[A_0 \cup B_0]\ ? \ f[A_0 \cup X]\ \triangle\ f[B_0 \cup X]=f[A_0] \cup f[B_0]\ ? \ f[A_0] \cup f[X]\ \triangle\ f[B_0] \cup f[X]$$

Now formalize. The first set is a union of images of $A_0, B_0$. The second set is a symmetric difference of two unions: one of images of $A_0, X$ and other of images of $B_0, X$.

Counterexample: It is possible for values from the image of $X$ to be present in the image of $A_0$ or $B_0$. In this case, $f[A]\ \triangle\ f[B]$ may exclude some values from $f[A_0]$ or $f[B_0]$, which fall in both $f[A_0]$ and $f[X]$ as well as in both $f[B_0]$ and $f[X]$. Since all other remaining values would be a part of either $f[A_0]$ or $f[B_0]$, the righthand side of the equation would be a subset of the lefthand side of the equation, and not vice versa. 

Answer: no ($\subseteq$) :( / yes ($\supseteq$) :)

## Problem 4.3

Does a surjection $f$ from the set of words of length $9$ in the alphabet $\{0, 1\}$ to the set of words of length $3$ in the alphabet $\{0,1,2,3,4\}$, for which the preimage of the set 

$$\{(0,0,0), (1,1,1), (2,2,2), (3,3,3), (4,4,4)\}$$

has a cardinarity of $400$, exist?

### Solution

Cardinality of the first set is $2^9=512$. Cardinality of the second set is $5^3=125$. Per the original condition, $400$ values from the first set are mapped to $5$ values in the second set. It is required to map the remaining $512-400=112$ values from the first set to $125-5=120$ values from the second set. 

Is it possible to map the values in such a way the function would remain a surjection? Per the surjection definition, for each value in the second set there should be at least one value in the first one, which is not true $\Rightarrow$ no.

Answer: no :(

## Problem 4.4

How many $6$-digit numbers in which there is an equal number of odd and even digits are there?

There should be $3$ odd and even numbers each.

There are $6 \choose 3$ position combinations of the even digits. 

Then, there are $5$ ways to fill each of the $3$ even slots and $5$ ways to fill each of the $3$ odd slots. Taking into account that a ninth of the numbers would have a leading zero, the final answer would be:

$$\frac{9}{10}{6 \choose 3}\times5^3\times5^3=\frac{9\times6!\times5^6}{10\times3!\times3!}=\frac{2^4\times3^4\times5^7}{2^3\times3^2\times5}=2\times3^2\times5^6=281250$$

Answer: $281250$