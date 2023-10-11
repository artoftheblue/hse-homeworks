## Problem 1 

Determine whether the sequences are fundamental (Cauchy seequences).

### Preamble

A sequence is fundamental (Cauchy) if $\forall \varepsilon > 0, \exists N$ such that $\forall n,m \geq N, |a_n-a_m| < \varepsilon$.

### Subproblem A

$$x_n=\frac{1+4n^2}{2+2n^2}$$

Permute stuff around:

$$\frac{1+4n^2}{2+2n^2}=\frac{4+4n^2-3}{2+2n^2}=2-\frac{3}{2+2n^2}$$

Compare some elements $x_n$ and $x_m$ (per the triangle inequation), assuming $m>n$:

$$|x_n-x_m|=\left|2-\frac{3}{2+2n^2}-2+\frac{3}{2+2m^2}\right|=\frac{3}{2+2n^2}+\frac{3}{2+2m^2}<\frac{6}{2+2n^2}=\frac{3}{1+n^2}<\frac{3}{n^2}$$

Now, $\forall n,m\geq N$ and $\forall \varepsilon>0$: 

$$\frac{3}{N^2}<\varepsilon\Rightarrow\frac{3}{\varepsilon}<N^2\Rightarrow N^2>\frac{3}{\varepsilon}\Rightarrow N > \sqrt{\frac{3}{\varepsilon}}$$

Therefore, starting $N=\left[\sqrt{\frac{3}{\varepsilon}}\right]$, the distance between any two values will be less than some arbitrary value $\varepsilon$, which means that the sequence is fundamental (Cauchy).

Answer: a Cauchy sequence.

### Subproblem B

$$a_n=1+\frac{1}{2^2}+\dots+\frac{1}{n^2}$$

Compare some elements $a_n$ and $a_m$ (considering $m < n$) and use some funny tricks like a telescopic sum to properly compare everything: 

$$|a_n-a_m|=1+\frac{1}{2^2}+\dots+\frac{1}{n^2}-\left(1+\frac{1}{2^2}+\dots+\frac{1}{m^2}\right)=\frac{1}{(m + 1)^2}+\frac{1}{(m+2)^2}+\dots+\frac{1}{n^2}<$$

$$<\frac{1}{m}\cdot\frac{1}{m+1}+\frac{1}{m+1}\cdot\frac{1}{m+2}+\dots+\frac{1}{n-1}\cdot\frac{1}{n}=$$

$$=\left(\frac{1}{m}-\frac{1}{m+1}\right)+\left(\frac{1}{m+1}-\frac{1}{m+2}\right)+\dots+\left(\frac{1}{n-1}-\frac{1}{n}\right)=\frac{1}{m}-\frac{1}{n}<\frac{1}{m}$$

Now, $\forall n,m\geq N$ and $\forall \varepsilon>0$: 

$$\frac{1}{N}<\varepsilon$$

Therefore, starting $N=\left[\frac{1}{\varepsilon}\right]$, the distance between any two values will be less than some arbitrary value $\varepsilon$, which means that the sequence is fundamental (Cauchy).

Answer: a Cauchy sequence.

### Subproblem C

$$a_n=1+\frac{1}{4}+\frac{1}{7}+\dots+\frac{1}{3n-2}$$

Compare some elements $a_n$ and $a_m$ ($n=m+k, k \in\mathbb{N}$):

$$|a_n - a_m| = 1 +\frac{1}{4}+\frac{1}{7}+\dots+\frac{1}{3n-2}-\left(1+\frac{1}{4}+\frac{1}{7}+\dots+\frac{1}{3m-2}\right)=$$

$$=\underbrace{\frac{1}{3(m + 1) - 2}+\frac{1}{3(m+2)-2}+\dots + \frac{1}{3(m+k)-2}}_{k}>$$

$$>\underbrace{\frac{1}{3n-2}+\frac{1}{3n-2}+\dots +\frac{1}{3n-2}}_k=\frac{k}{3n-2}>\frac{k}{3n}$$

Try to find a counterexample, when $\nexists N \ \forall \varepsilon$. Say that $k=m$, then $|a_n-a_m|>\frac{k}{3n}=\frac{m}{3\cdot2m}=\frac{1}{6}$ and then $\exists \varepsilon=0.1$, for which $|a_n-a_m|<0.1$ contradicts $|a_n-a_m|>\frac{1}{6}$. Therefore, the sequence is not fundamental (not Cauchy).  

Answer: **not** a Cauchy sequence.

## Problem 2

Find the limit $$\lim_{n\to\infty}\left(1+\frac{3}{2n}\right)^{13n+11}$$

On the lecture it was proven that 

$$\lim_{n\to\infty}\left(1+\frac{1}{n}\right)^n=e$$

Let's try using this special limit and permute stuff around:

$$\lim_{n\to\infty}\left(1+\frac{3}{2n}\right)^{13n+11}=\lim_{n\to\infty}\left(1+\frac{1}{\frac{2}{3}n}\right)^{\frac{39}{2}(\frac{2}{3}n)+11}=\lim_{n\to\infty}\left(\left(1+\frac{1}{\frac{2}{3}n}\right)^{\frac{39}{2}(\frac{2}{3}n)}\left(1+\frac{1}{\frac{2}{3}n}\right)^{11}\right)=$$

$$=\left(\lim_{n\to\infty}\left(1+\frac{1}{\frac{2}{3}n}\right)^{\frac{2}{3}n}\right)^\frac{39}{2}\lim_{n\to\infty}\left(1+\frac{1}{\frac{2}{3}n}\right)^{11}=e^\frac{39}{2}(1+\frac{3}{2}\lim_{n\to\infty}\frac{1}{n})=e^\frac{39}{2}(1+\frac{3}{2}\cdot0)=e^\frac{39}{2}$$

Answer:

$$e^\frac{39}{2}$$

## Problem 3

Find all partial limits of a sequence

$$\{x_n\}=\frac{1}{2}, \frac{1}{2}, \frac{1}{4}, \frac{3}{4}, \frac{1}{8}, \frac{7}{8},\dots,\frac{1}{2^n},\frac{2^n-1}{2^n},\dots$$

Split the original sequence into two: 

$$\{a_n\}=\frac{1}{2^n}, \ \ \{b_n\}=\frac{2^n-1}{2^n}$$

It was proven in previous homeworks that $\lim_{n\to\infty}\frac{1}{2^n}=0$. Therefore, $\lim\inf_{n\to\infty}\{x_n\}=0$.

$$\{b_n\}=\frac{2^n-1}{2^n}=1-\frac{1}{2^n}$$

$$\lim_{n\to\infty}\left(1-\frac{1}{2^n}\right)=1-\lim_{n\to\infty}\frac{1}{2^n}=1$$

Therefore, $\lim_{n\to\infty}\sup\{x_n\}=1$.

There are no other partial limits since there are no other unaccounted elements in the sequence.

Answer:

$$\lim_{n\to\infty}\inf\{x_n\}=0, \lim_{n\to\infty}\sup\{x_n\}=1$$

## Problem 4

Formulate a number sequence that has $a_1, a_2, \dots, a_p$ as its partial limits.

Consider the following sequence:

$$\{x_1\}=a_1, \\ \{x_2\}=a_2, \\ \{x_3\}=a_3, \\ \vdots \\ \{x_p\}=a_p, \\ \{x_{p+1}\}=a_1, \\ \{x_{p+2}\}=a_2, \\ \{x_{p+3}\}=a_3, \\ \vdots \\ \{x_{2p}\}=a_p, \\ \{x_{2p+1}\}=a_1, \\ \{x_{2p+2}\}=a_2, \\ \{x_{2p+3}\}=a_3, \\ \vdots \\ \{x_{3p}\}=a_p \\ \vdots \ \ \vdots \ \ \vdots \\ \{x_{(n-1)p}\}=a_p, \\ \{x_{(n-1)p+1}\}=a_1, \\ \{x_{(n-1)p+2}\}=a_2, \\ \{x_{(n-1)p+3}\}=a_3, \\ \vdots \\ \{x_{np}\}=a_p$$

To calculate partial limits of this sequence, we may split the sequence into $p$ subsequences, grouping together elements that are equal to each other. Limits of each of these monotonous, stagnant subsequences would be some value from $\{a_1, a_2, a_3, \dots a_p\}$, which is precisely what we wanted.

## Problem 5

Formulate such a number sequence $\{a_n\}$ so that each element is also its partial limit. What other partial limits does this sequence certainly have?

Consider the following sequence: 

$$\{1, 1, 2, 1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 4, 5, \dots\}$$

The sequence is defined as follows: we count all numbers from $1$ to $n$ and add them to the sequence, then increase $n$ by $1$ and repeat the process indefinitely.

In this case, there would be an infinite number of each of the natural numbers, so it is always possible to find such a subsequence $\{a_{(k)n}\}$ that would be stagnant and only consist of the same $k\in\mathbb{N}$, defining every single partial limit. Therefore, for $\forall k\in\mathbb{N}, \lim_{n\to\infty}a_{(k)n}=k$.

Since by our sequence definition, it only contains natural numbers, any its subsequences would have a limit that is a natural number (albeit it's pretty boring, yeah). Since every single $k \in \mathbb{N}$ and $k \in {a_n}$, then there cannot be any other partial limits since every single possibility is already accounted for.

Answer: no other partial limits.

## Problem 6

Find $\lim\sup x_n$ and $\lim\inf x_n$, where

### Subproblem A

$$x_n=\frac{n^2}{n^2+1}\cos\frac{2\pi n}{3}$$

First of all, state the following for $n\in\mathbb{N}$:

* $\cos\left(\frac{2\pi}{3}+2\pi n\right)=\cos\left(\frac{4\pi}{3}+2\pi n\right)$
  * Therefore, if $n \hspace{-4px} \mod 3 \neq 0$, then we get the first subsequence $x_{(1)n}=\frac{n^2}{n^2+1}\cos\frac{2\pi}{3}=\frac{1}{2}\frac{n^2}{n^2+1}$
* $\cos(2\pi n) = 1$
  * In this case, if $n \hspace{-4px} \mod 3 = 0$, then we get the second subsequence $x_{(2)n}=\frac{n^2}{n^2+1}\cos(0)=\frac{n^2}{n^2+1}$

Calculate the limit of the second subsequence:

$$\{x_{(2)n}\}\lim_{x\to\infty}\frac{n^2}{n^2+1}=\lim_{x\to\infty}\frac{1}{1+\frac{1}{n^2}}=\frac{1}{1+\lim_{x\to\infty}\frac{1}{n^2}}=\frac{1}{1+0}=1$$

Using limit arithmetic, calculate the limit of the first subsequence:

$$\lim_{x\to\infty}\{x_{(1)n}\}=\lim_{x\to\infty}\frac{1}{2}\frac{n^2}{n^2+1}=\frac{1}{2}\lim_{x\to\infty}\{x_{(2)n}\}=\frac{1}{2}$$

Therefore, choose corresponding values from the partial limits and get the answer:

Answer:

$$\lim\sup x_n=1, \ \ \lim\inf x_n = \frac{1}{2}$$

### Subproblem B

$$x_n=(-1)^{n+1}\left(1+\frac{2}{n}\right)^{3n}+\sin\frac{\pi n}{6}$$

Calculate the following for later:

$$\lim_{n\to\infty}\left(1+\frac{2}{n}\right)^{3n}=\lim_{n\to\infty}\left(1+\frac{1}{\frac{1}{2}n}\right)^{\left(\frac{1}{2}n\right)6}=e^6$$

In this sequence, key values depend on whether $n$ is odd and whether it is divisible by $12$.

* $n \hspace{-4px} \mod 2 = 0 \Rightarrow (-1)^{n+1} = -1$ 
* $n \hspace{-4px} \mod 2 \neq 0 \Rightarrow (-1)^{n+1} = 1$ 

Next:

* $n \hspace{-4px} \mod 12 = 0, 6\Rightarrow \sin{\frac{\pi n}{6}} = 0$
* $n \hspace{-4px} \mod 12 = 1, 5\Rightarrow \sin{\frac{\pi n}{6}} = \frac{1}{2}$
* $n \hspace{-4px} \mod 12 = 2, 4\Rightarrow \sin{\frac{\pi n}{6}} = \frac{\sqrt{3}}{2}$
* $n \hspace{-4px} \mod 12 = 3\Rightarrow \sin{\frac{\pi n}{6}} = 1$
* $n \hspace{-4px} \mod 12 = 7,11\Rightarrow \sin{\frac{\pi n}{6}} = -\frac{1}{2}$
* $n \hspace{-4px} \mod 12 = 8, 10\Rightarrow \sin{\frac{\pi n}{6}} = -\frac{\sqrt{3}}{2}$
* $n \hspace{-4px} \mod 12 = 9\Rightarrow \sin{\frac{\pi n}{6}} = -1$

Therefore, let's evaluate $\lim_{x\to\infty}\{x_{(\alpha)n}\}=x$ for each of the $\alpha = n \hspace{-4px} \mod 12$, where $\{x_{(\alpha)n}\}$ is a subsequence of the original sequence with corresponding $\alpha$-s:

* $\alpha = 0, 6 \Rightarrow x = -e^6$
* $\alpha = 1, 5 \Rightarrow x = e^6 + \frac{1}{2}$
* $\alpha = 2, 4 \Rightarrow x = -e^6 + \frac{\sqrt{3}}{2}$
* $\alpha = 3 \Rightarrow x = e^6 + 1$
* $\alpha = 7, 11 \Rightarrow x = e^6 -\frac{1}{2}$
* $\alpha = 8, 10 \Rightarrow x = -e^6 -\frac{\sqrt{3}}{2}$
* $\alpha = 9 \Rightarrow x = e^6 -1$

Awesome, now choose corresponding values from the partial limits and get the answer:

Answer:

$$\lim\sup x_n=e^6 + 1, \ \ \lim\inf x_n = -e^6 -\frac{\sqrt{3}}{2}$$

### Subproblem C

$$x_n=\frac{n}{n+1}\sin^2\frac{\pi n}{4}$$

Similarly as above, check how $\sin^2\frac{\pi n}{4}$ behaves for $n \hspace{-4px} \mod 8$:

* $n \hspace{-4px} \mod 8 = 0, 4\Rightarrow \sin^2\frac{\pi n}{4} = 0$
* $n \hspace{-4px} \mod 8 = 1, 3, 5, 7\Rightarrow \sin^2\frac{\pi n}{4} = \frac{1}{2}$
* $n \hspace{-4px} \mod 8 = 2, 6\Rightarrow \sin^2\frac{\pi n}{4} = 1$

Therefore, we may split our sequence into some number of subsequences (take $3$, for example), and then the partial limits would be one of the coefficients above multiplied by $\lim_{x\to\infty}\frac{n}{n+1}=\lim_{x\to\infty}\frac{1}{1+\frac{1}{n}}=1$.

Therefore, the partial limits would be $0, \frac{1}{2}, 1$. Write the answer:

Answer:

$$\lim\sup x_n=1, \ \ \lim\inf x_n = 0$$