# Dicrete Maths, Homework 7

## Hyper Important Test

![Alt text](image.png)

## Problem 1 

There are 40 tourists in the group. Out of them, 20 know English, 15 know French, and 11 know Spanish. 7 people know both English and French, 5 people know both English and Spanish, and 3 people know both French and Spanish. 2 tourists know all three languages. How many people in the group know neither of these languages?

---

Draw a visual aid picture:

![Alt text](image-1.png)

Define each sector from the problem statement accordingly:

* $|T| = 40$
* $|E| = 20$
* $|F| = 15$
* $|S| = 11$
* $|E \cap F| = 7$
* $|E \cap S| = 5$
* $|F \cap S| = 3$
* $|E \cap F \cap S| = 2$

We need to find $|T| - |E \cup F \cup S|$. Therefore, using the exclusion-inclusion formula:

$$|T| - |E \cup F \cup S| = |T| - |E| - |F| - |S| + |E \cap F| + |E \cap S| + |F \cap S| - |E \cap F \cap S| =$$

$$= 40 - 20 - 15 - 11 + 7 + 5 + 3 - 2 = -6 + 15 - 2 = 7$$

**Answer:** 7

## Problem 2

Given 3 carnations, 4 roses, and 5 tulips. How many ways are there to create a bouquet out of 7 flowers, using the existing flowers? (flowers of the same kind are considered the same)

---

Consider 4 possible groups: (0, 1, 2, or 3 carnations in the bouquet). How many possibilities are there to create a bouquet of 7 flowers?

Arrange the flowers in the first group:

$$\overset{1}{R}\overset{2}{R}\overset{3}{R}\overset{4}{R}\overset{5}{T}\overset{6}{T}\overset{7}{T}\overset{8}{T}\overset{9}{T}$$

How many possible ways to choose a slice of this arrangement of length 7 are there? In other words, how many possibilies are there to place two separators so that there would be 7 items between them? In total, the answer would the number of roses and tulips minus the length of the slice plus 1: $(4+5)-7+1=3$

The slices, for the sake of visualization:

$$\underbrace{\overset{1}{R}\overset{2}{R}\overset{3}{R}\overset{4}{R}\overset{5}{T}\overset{6}{T}\overset{7}{T}}TT \ \ R\underbrace{\overset{1}{R}\overset{2}{R}\overset{3}{R}\overset{4}{T}\overset{5}{T}\overset{6}{T}\overset{7}{T}}T \ \ RR\underbrace{\overset{1}{R}\overset{2}{R}\overset{3}{T}\overset{4}{T}\overset{5}{T}\overset{6}{T}\overset{7}{T}}$$

Similarly, now consider the number of such slices in the following sets:

$$\underbrace{\overset{1}{R}\overset{2}{R}\overset{3}{R}\overset{4}{R}\overset{5}{C}\overset{6}{T}\overset{7}{T}}TTT \Rightarrow 4$$

$$\underbrace{\overset{1}{R}\overset{2}{R}\overset{3}{R}\overset{4}{R}\overset{5}{C}\overset{6}{C}\overset{7}{T}}TTTT \Rightarrow 5$$

$$\underbrace{\overset{1}{R}\overset{2}{R}\overset{3}{R}\overset{4}{R}\overset{5}{C}\overset{6}{C}\overset{7}{C}}TTTTT \Rightarrow 6$$

Sum all the possible slice beginnings: $3+4+5+6=18$. Is this the final answer? No, because the following slice:

$$\underbrace{\overset{1}{C}\overset{2}{C}\overset{3}{T}\overset{4}{T}\overset{5}{T}\overset{6}{T}\overset{7}{T}}$$

is accounted twice.

Therefore, the final answer is $18-1=17$.

**Answer:** 17

## Problem 3

How many binary words of length 12 have the subword $1100$?

---

Let's calculate the number of words that do not have the subword $1100$.

Using a recursive approach, calculate the number of words of length $n$, starting from $n=1$. It is obvious that no words of length $\leq 3$ have the required subword, so $f(0),f(1),f(2),f(3)=2^n$:

|input value|result|
|:-:|:-:|
|$f(0)$|$1$|
|$f(1)$|$2$|
|$f(2)$|$4$|
|$f(3)$|$8$|

Further, for values greater than $3$, let's consider how the words are derived from the previous iteration. From the possible words of length $3$, there would be a single option to get $1100$ through machinations, adding $0$ to the word $110$. For words of length $4$, there would be two options to get a word that corresponds to the pattern $*1100$, either from $0110$ or from $1110$, and so on. Effectively, we take the number of words with one letter less ($n-1$), multiply this number by two and subtract all the words of length ($n-4$):

For all further iterations, to get the number of valid words of a certain length, all words that end with $110$ have to be counted and subtracted from the total once since the action below is invalid. This corresponds to the number of words that are $3$ letters shorter (because if all words denoted by asterisks are valid, then it's only possible to get an invalid word if we were to add $0$ to the end of a word that ends with $110$). Example:

$$\underbrace{*}_{f(1)}110 \xrightarrow{+0} \underbrace{*}_{f(1)}1100$$

$$\underbrace{*******}_{f(7)}\ 110 \xrightarrow{+0} \underbrace{*******}_{f(7)}\ 1100$$

This is a single case, only when we add $0$ to the end of words that end with $110$ and start with words of length $(n-4)$, thus the number of such words that have to be subtracted is $f(n-4)$. 

The recursive formula to get the number of words that do not have the subword $1100$ inside of them is:

    def f(n: int):
      if n < 0:
          return 0
      if n == 0:
          return 1
      return 2 * f(n - 1) - f(n - 4)

Calculating the recursive formula for $n=12$, we get $f(12)=2031$.

Now, subtract this number from the number of total words, which is $2^{12}=4096$. In total, $4096-2031=2065$.

**Answer:** 2065

## Problem 4

Prove that if $k=\lfloor\frac{n}{\ln n}\rfloor$, then the proportion of all surjections from $[n]$ to $[k]$ among all total functions from $[n]$ to $[k]$ is such that $S_{n,k}>0.999$ for all big enough $n$.

---

First of all, the number of surjections from one set to the other is 

$$\text{Surj}(n,k)=\sum^{k}_{p=0}(-1)^p{k \choose p}(k-p)^n=k^n+\sum^{k}_{p=1}(-1)^{p}{k \choose p}(k-p)^n$$

We need to estimate the proporation of all these surjections to the number of total functions, which is $k^n$. If we prove that 

$$\lim_{n\to\infty}S_{n,k}=\lim_{n\to \infty}\frac{\text{Surj}(n,k)}{k^n}=1$$

then it would be always possible to find such $n$ that $S_{n,k}>0.999$ since it would approach $1$.

Check whether this is true by substituing the formula for surjections into the equation:

$$\lim_{n\to\infty}S_{n,k}=\lim_{n\to \infty}\frac{\text{Surj}(n,k)}{k^n}=\lim_{n\to\infty}\left(\frac{k^n}{k^n}+\sum^{k}_{p=1}\frac{(-1)^{p}{k \choose p}(k-p)^n}{k^n}\right)=$$

$$=1+\lim_{n\to\infty}\sum^{k}_{p=1}\frac{(-1)^{p}{k \choose p}(k-p)^n}{k^n}$$

(really, really) try to evaluate the limit of a single itself, taking into account that $p$ in every single term in the sum depends on $n$ to an extent that $p<n$ and can, thus, be considered a constant:

$$\lim_{n\to\infty}\frac{(-1)^{p}{k \choose p}(k-p)^n}{k^n}=(-1)^p\lim_{n\to\infty}\frac{{k \choose p}(k-p)^n}{k^n}=$$

$$=(-1)^p\lim_{n\to\infty}\left({k \choose p}\underbrace{\frac{(k-p)}{k}\times\dots\times\frac{(k-p)}{k}}_{n}\right)=$$

$$=(-1)^p\lim_{n\to\infty}\left(\frac{k!}{p!(k-p)!}\underbrace{\frac{(k-p)}{k}\times\dots\times\frac{(k-p)}{k}}_{n}\right)=$$

$$=\frac{(-1)^p}{p!}\lim_{n\to\infty}\left(\frac{k!}{(k-p)!}\underbrace{\frac{(k-p)}{k}\times\dots\times\frac{(k-p)}{k}}_{n}\right)=$$

$$=\frac{(-1)^p}{p!}\lim_{n\to\infty}\left(\underbrace{(k - p + 1)(k - p + 2)\times\dots\times(k - 1)k}_p\times\underbrace{\frac{(k-p)}{k}\times\dots\times\frac{(k-p)}{k}}_{n}\right)$$

Estimate this scary product within the limit:

$$(k-p)^p\left(\frac{k-p}{k}\right)^n\leq\underbrace{(k - p + 1)(k - p + 2)\times\dots\times(k - 1)k}_p\times\underbrace{\frac{(k-p)}{k}\times\dots\times\frac{(k-p)}{k}}_{n}\leq k^p\left(\frac{k-p}{k}\right)^n$$

Now, it would have been nice to use limit arithmetic, but ah well, $\lim_{n\to\infty}(k-p)^p=\infty$ since $\lim_{n\to\infty}k=\lim_{n\to\infty}\frac{n}{\ln n}=\infty$ since $\ln n$ asymptotically falls slower than $n$. Therefore, try to get some kinda undefined value by taking the limits, use the sequeeze theorem, and then compare asymptotes of the resulting functions.

$$\lim_{n\to\infty}\left((k-p)^p\left(\frac{k-p}{k}\right)^n\right)\leq$$

$$\leq\lim_{n\to\infty}\left(\underbrace{(k - p + 1)(k - p + 2)\times\dots\times(k - 1)k}_p\times\underbrace{\frac{(k-p)}{k}\times\dots\times\frac{(k-p)}{k}}_{n}\right)\leq$$

$$\leq\lim_{n\to\infty}\left(k^p\left(\frac{k-p}{k}\right)^n\right)$$

Asymptotes of $(k-p)^p$ and $k^p$ are the same and equal to the asymptote of $n^p$, aka some kinda monomial raised to the power of a constant $p$. The asymptote of $\left(\frac{(k-p)}{k}\right)^n$ is $a^n$, where since $p > 0$, $0 < a < 1$. Since $(k-p)^p$ and $k^p$ grow slower asymptotically than $a^n$, then the undetermined value after we calculate limits would collapse to the following:

$$\lim_{n\to\infty}\infty\cdot0\leq\lim_{n\to\infty}\left(\underbrace{(k - p + 1)(k - p + 2)\times\dots\times(k - 1)k}_p\times\underbrace{\frac{(k-p)}{k}\times\dots\times\frac{(k-p)}{k}}_{n}\right)\leq\lim_{n\to\infty}\infty\cdot0$$

$$0\leq\lim_{n\to\infty}\left(\underbrace{(k - p + 1)(k - p + 2)\times\dots\times(k - 1)k}_p\times\underbrace{\frac{(k-p)}{k}\times\dots\times\frac{(k-p)}{k}}_{n}\right)\leq0$$

Therefore, per squeeze theorem and the magic of asymptotes:

$$\lim_{n\to\infty}\left(\underbrace{(k - p + 1)(k - p + 2)\times\dots\times(k - 1)k}_p\times\underbrace{\frac{(k-p)}{k}\times\dots\times\frac{(k-p)}{k}}_{n}\right)=0$$

$$\lim_{n\to\infty}S_{n,k}=1+\sum^{k}_{p=1}\frac{(-1)^p}{p!}\lim_{n\to\infty}0=1+0=1$$

Since $\lim_{n\to\infty}S_{n,k}=1$, then there certainly is some $n$ for which $S_{n,k}>0.999$, q. e. d.