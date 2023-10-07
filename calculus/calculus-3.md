# Just Great Tasks

## Problem 1

Show that $\sup(A)=1$, where $A=\left\{\frac{n}{n+1}, n \in \mathbb{N} \right\}$.

### Solution

First, show that the upper bound exists. $\frac{n}{n+1}<1$ since $n < n + 1$ for all natural numbers. Therefore, there is some upper bound $=1$, and we need to prove whether it is the supremum (if it is actually the minimum upper bound).

Assume $\sup(A)=1$. For some arbitrary $\varepsilon>0$, try to find some value such that for $a \in A$: $1-\varepsilon<a<1$. For instance, for $\varepsilon = 0.01, n=100$, $\exists a = \frac{n}{n+1}=\frac{100}{101}$. Similarly, for any $\varepsilon$, we could find some $n$ that would lie between $1-\varepsilon$ and $1$. Therefore, the assumption is true, q. e. d.

## Problem 2

Show that $\inf(A)=0$, where $A=\left\{\frac{1}{n}, n \in \mathbb{N} \right\}$.

### Solution

Similarly to task above, first, show that the lower bound exists. $\frac{1}{n}>0$ since $n \in \mathbb{N}$. Therefore, there is some lower bound $=0$, and we need to prove whether it is the infinum (if it is actually the maximum lower bound).

Assume $\inf(A)=0$. For some arbitrary $\varepsilon>0$, try to find some value such that for $a \in A$: $0<a<0+\varepsilon$. For instance, for $\varepsilon = 0.01, n=101$, $\exists a = \frac{1}{n}=\frac{1}{101}$. Similarly, for any $\varepsilon$, we could find some $n$ that would lie between $0$ and $0+\varepsilon$. Therefore, the assumption is true, q. e. d.

## Problem 3

Let $A, B \subseteq \mathbb{R}$ be two non-empty subsets in set $\mathbb{R}$. Define *distance* from $A$ to $B$ as a positive number like the following:

$$d(A, B) := \inf_{x\in A, y\in B}|x-y|$$

Is it possible that $A \cap B = \varnothing$, but $d(A,B)=0$?

### Solution

Proof by example. Take some one-element set $A = \{a\}$, where $a\in\mathbb{R}$. Derive the second set as follows: $B = \mathbb{R} \setminus A$. In other words, there are two sets, the first of which is just a single point and the second of which is all points except for that single point. The intersection of these sets would be $A \cap B = \varnothing$.

Separate set $B$ into two intervals: $B_1 = (-\infty, a), B_2 = (a, +\infty)$. These sets are symmetric over the point $a$ and appear to infinitely converge to some value next to $a$ from both sides (and since we define $d(A,B)$ as an absolute value, we could only consider one set, as the other would be identical to it by symmetry).

There is always some $\varepsilon > 0$ such that $a - \varepsilon\in B_2$; therefore, similarly to tasks above, since for $a\in A, a-\varepsilon\in B, |a - (a - \varepsilon)| = \varepsilon$. Since the distance (without the infinum just yet) is equal to $\varepsilon$, then out of all upper bounds, the smallest would be $0\Rightarrow d(A, B) := \inf_{x\in A, y\in B}|x-y| = 0$. We have found such an example, q. e. d.

**Answer: no :(**

## Problem 4

Examine the following recurrent sequences for convergence and find the limit if they do converge:

### Preamble

Per Weierstrass, we need to find either the supremum or the infinum of each sequence.

If the sequence is non-descending and has an upper bound, then $\exists\lim_{n\to\infty}a_n=\sup\{a_n\}$.

If the sequence is non-ascending and has a lower bound, then $\exists\lim_{n\to\infty}a_n=\inf\{a_n\}$

### Subproblem A

$$a_{n+1}=1-\frac{1}{4a_n}, a_1=1$$

Check whether the sequence is non-ascending by comparing two elements of the equation:

$$a_{n+1}-a_{n}=1-\frac{1}{4a_n}-a_n=\frac{4a_n-4a_n^2-1}{4a_n}=\frac{-(2a_n-1)^2}{4a_n}$$

The numerator of the fraction is always positive as it's a square; therefore, the sign of the equation depends only on $a_n$. If $a_n>0$, then the entire sequence will be descending, which is true since $a_1=1$.

Great, the sequence has a lower bound (infinum), $\exists a=\lim_{n\to\infty}a_n=\inf\{a_n\}$. Try to evaluate it by assuming $a_n=a_{n+1}=a$, since we want the difference between two successive elements to be minimal ($0$):

$$a=\lim_{x\to\infty}\left(1-\frac{1}{4a_n}\right)=1-\frac{1}{4a}\Rightarrow4a^2-4a+1=0\Rightarrow(2a-1)^2=0\Rightarrow a=\frac{1}{2}$$

Awesome, $a_n$ never evaluates to negative numbers, which means that our value is the limit.

Answer: $\frac{1}{2}$

### Subproblem B

$$a_{n+1} = \frac{4}{3}a_n-a_n^2, a_1=\frac{1}{2}$$

Check whether the sequence is non-ascending by comparing two elements of the equation:

$$a_{n-1}-a_n=\frac{4}{3}a_n-a_n^2-a_n=\frac{1}{3}a_n-a_n^2=a_n\left(\frac{1}{3}-a_n\right)$$

Since the sign of the equation depends on $a_n$, then the equation above would evaluate to a negative value if $a_n>\frac{1}{3} \lor a_n<0$, which means that the sequence is probably non-ascending (check later).

Awesome, the sequence has a lower bound, $\exists a=\lim_{n\to\infty}a_n=\inf\{a_n\}$. Attempt to evaluate it by assuming $a_n=a_{n+1}=a$, since we want the difference between two successive elements to be minimal ($0$):

$$a=\lim_{n\to\infty}\left(\frac{4}{3}a_n-a_n^2\right)=\frac{4}{3}a-a^2\Rightarrow a^2-\frac{1}{3}a=0\Rightarrow a\left(a-\frac{1}{3}\right)=0$$

There appears to be at least two possible infinums ($a=0 \lor a=\frac{1}{3}$); however, only one of them can exist, so we take the highest, which we approach from the top, i. e. $\inf\{a_n\}=\frac{1}{3}\Rightarrow\lim_{n\to\infty}a_n=\frac{1}{3}$.

Amazing, $a_n$ is never $\in [0, \frac{1}{3}]$ so it is never ascending and is bounded.

Answer: $\frac{1}{3}$

### Subproblem C

$$x_{n+1}=\frac{1}{m}\left((m-1)x_n+\frac{a}{x_n^{m-1}}\right), n\geq1,m\in\mathbb{N},x_1>0$$

Since this task is eerily similar to the last one, we could instantly try to find such values that the difference between them is minimal. Therefore, assume $x_{n+1}=x_n=x$:

$$x=\frac{1}{m}\left((m-1)x+\frac{a}{x^{m-1}}\right)\Rightarrow x=\frac{m-1}{m}x+\frac{a}{mx^{m-1}}\Rightarrow mx^m\left(\frac{m-1}{m}-1\right)=a\Rightarrow$$

$$x=\sqrt[m]{a}$$

Since this value exists, the sequence has some kind of bound. 

As for ascension/descention, if $x_n < \sqrt[m]{a}$, then the two elements would be in ascending order and if $x_n > \sqrt[m]{a}$, then they would be in descending order. This way, if the starting value $x_1 < \sqrt[m]{a}$, it would be ascend once, and starting $n=2$, it would descend infinitely, approaching $\sqrt[m]{a}$. Otherwise, if $x_n > \sqrt[m]{a}$, the sequence would descend infinitely starting from $n=1$.

Therefore, we may simply cut off the first element of the sequence and always take some $A_0\subseteq\{x_{n}\}$ such that all its elements are descending from the first one. There is an infinite number of these descending subsets and they would be bound by $\inf\{a_n\}=\sqrt[m]{a}$, which is the limit: $\lim_{n\to\infty}x_{n}=\sqrt[m]{a}$.

Answer: $\sqrt[m]{a}$

### Subproblem D

$$x_1=a, x_2=b, x_{n+1}=\frac{1}{2}(x_n+x_{n-1}), n\geq1$$

Tough one, it's pretty obvious from messing around with Python that the limit is $\frac{2b+a}{3}$, but proving it is an entirely different case. Attempt to subtract one sequence element from the next to compare the elements:

$$x_{n+1}-x_{n}=\frac{1}{2}(x_n+x_{n-1})-x_{n}=-\frac{1}{2}x_n + \frac{1}{2}x_{n-1}=\frac{1}{2}(x_{n-1}-x_n)=-\frac{1}{2}(x_n-x_{n-1})$$

Insane, we got the very same expression! Therefore,

$$x_{n+1}-x_{n}=\underbrace{(-1)\times\dots\times (-1)}_{n-1}\overbrace{\frac{1}{2}\times\dots\times\frac{1}{2}}^{n-1}(x_2-x_1)=(-1)^{n-1}\frac{1}{2^{n-1}}(x_2-x_1)=(-1)^{n-1}\frac{1}{2^{n-1}}(b-a)=(*)$$

Using some other funny tricks (add $\frac{1}{2}x_n$ to both sides), we notice that once again, it's the very same expression on both sides:

$$x_{n+1}=\frac{1}{2}x_n+\frac{1}{2}x_{n-1}\Rightarrow \underbrace{x_{n+1}+\frac{1}{2}x_n=x_n+\frac{1}{2}x_{n-1}=\dots=x_2+\frac{1}{2}x_1}_{n}=b + \frac{1}{2}a=(**)$$

Subtract $(**)-(*)$:

$$(**)=x_{n+1}+\frac{1}{2}x_n=b + \frac{1}{2}a$$

$$(*)=x_{n+1}-x_{n}=(-1)^{n-1}\frac{1}{2^{n-1}}(b-a)$$

$$\frac{3}{2}x_n=b + \frac{1}{2}a-(-1)^{n-1}\frac{1}{2^{n-1}}(b-a)=b + \frac{1}{2}a-\frac{(-1)^{n-1}}{2^{n-1}}(b-a)$$

$$x_n=\frac{2b+a}{3}-\frac{(-1)^{n-1}}{2^{n-1}}(b-a)$$

Great, we have a non-recursive limit, which we can calculate:

$$\lim_{n\to\infty}{x_n}=\lim_{x\to\infty}\left(\frac{2b+a}{3}-\frac{(-1)^{n-1}}{2^{n-1}}(b-a)\right)=\frac{2b+a}{3}-\lim_{x\to\infty}\left(\frac{(-1)^{n-1}}{2^{n-1}}(b-a)\right)$$

Per squeeze theorem, 

$$0<\frac{(-1)^{n-1}}{2^{n-1}}(b-a)<\frac{1}{n!}$$

$$\lim_{n\to\infty}0=\lim_{n\to\infty}\left(\frac{(-1)^{n-1}}{2^{n-1}}(b-a)\right)=\lim_{n\to\infty}\frac{1}{n!}=0$$

Therefore,

$$\lim_{n\to\infty}{x_n}=\frac{2b+a}{3}-\lim_{x\to\infty}\left(\frac{(-1)^{n-1}}{2^{n-1}}(b-a)\right)=\frac{2b+a}{3}$$

Answer:

$$\frac{2b+a}{3}$$

## Problem 5

Define sequence $\{a_n\}$ as $a_{n+1}=a_n^2+a_n$. What should $a_1$ be in order for this sequence to have a limit?

### Solution

Compare two successive elements:

$$a_{n+1}-a_{n}=a_n^2+a_n-a_n=a_n^2$$

Since $a_n^2\geq0$, this sequence is non-descending. For it to have a limit per Weierstrass, it needs to have an upper bound. Assume that the difference between two elements of the sequence is so small that $a_n=a_{n+1}=a$:

$$a=a^2+a\Rightarrow a^2=0\Rightarrow a=0$$

Okay, so if there is a limit, then it is equal to $0$. $\lim_{n\to\infty}a_n=0$. Now consider some options:

* if $a_n > 0$, then the sequence diverges as it infinitely increases and does not have an upper bound;
* if $a_n = 0$, then the sequence consists of a stable sequence of $0$-s, and then $\lim_{x\to\infty}\{a_n\}=0$;
* if $a_n < -1$, then the sequence diverges as it would infinitely increase from $n=2$ since $a_n^2-a_n>0$;
* if $a_n=-1$, then the first element of the sequence is $-1$ and afterwards all elements are equal to $1-1=0$, so it suffers the same fate as $a_n=0$;
* finally, if $-1<a_n<0$, then the sequence converges because it has a lower bound of $\inf\{a_n\}=-1$ (the sequence is ascending) and has an upper bound of $\sup\{a_n\}=0$ per Weierstrass since we have proven that a limit of this sequence exists.

Answer: $\lim_{n\to\infty}a_n=0, a_n\in[-1,0]$