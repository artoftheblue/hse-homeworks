# Discrete Maths, Homework 21

## Problem 1

Consider the following game. A fair 6-sided die is thrown thrice. If $6$ never got rolled, then the player loses $1$ ruble. If $6$ got rolled once, the player wins $1$ ruble, if twice, wins $2$ rubles, and if thrice, wins $3$ rubles. Is this game winning to the player on average?

---

The chance that the player never rolls a $6$ is

$$\frac{5}{6}^3=\frac{125}{216}$$

The chance that the player rolls a $6$ once is 

$${3\choose 1}\frac{1}{6}\times\frac{5}{6}^2=\frac{75}{216}$$

The chance that the player rolls a $6$ twice is

$${3\choose 2}\frac{1}{6}^2\times\frac{5}{6} = \frac{15}{216}$$

The chance that the player rolls a $6$ twice is

$$\frac{1}{6}^3= \frac{1}{216}$$

Thus, the mathematical expectation of this game is 

$$E[\text{game}]=-1\times\frac{125}{216}+1\times\frac{75}{216}+2\times\frac{15}{216}+3\times\frac{1}{216} = - \frac{17}{216}$$

which means that this game is losing on average.

## Problem 2

The probability space is the set of all permutations of $(x_1,\dots,x_n)$ of elements from $1$ to $n$. All outcomes are equally probable. Find the mathematical expectation of the number of numbers that did not change their position.

---

Let's find the chance that a number remained on place. This also would give us the proportion of all sequences that have the number with a certain index that remained on place.

This chance is obviously $\frac{1}{n}$ since that's the chance that we have placed the number in its spot.

Thus, the mathematical expectation that a number remained on its spot independent of other values is

$$E[i|x_i=i]=\frac{1}{n}$$

Summarize this all for numbers (there are $n$ of such) to get the required mathematical expectation 

$$E[\forall i|x_i=i]=\frac{1}{n}\times n = 1$$

## Problem 3

Let $X$ be a random value. It is known that $E[2^X]=5$. Prove that 

$$P[X\geq6]<\frac{1}{10}$$

---

Markov's inequality:

$$P[f\geq\alpha]\leq\frac{E[f]}{\alpha}$$

Thus we know that 

$$P[X\geq6]\leq\frac{E[X]}{6}$$

since we are given the value $E[2^X]=5$, we may transition to this:

$$P[2^X\geq2^6]\leq\frac{E[2^X]}{2^6}$$

$$P[2^X\geq64]\leq\frac{5}{2^6}=\frac{5}{64}$$

and since $\frac{5}{64}<\frac{5}{50}<\frac{1}{10}$, we have 

$$P[2^X\geq64]<\frac{1}{10}\implies P[X\geq6]<\frac{1}{10}$$

## Problem 4

Each of the numbers $a_1,\dots,a_n$ is selected randomly, equally probably, and independently out of numbers $1,2,\dots,n$

### Subproblem A

Find the mathematical expectation of the number of different numbers among multiset $A=\{a_1,\dots,a_n\}$.

---

Let's calculate the number of unique elements. Define a characteristic function as

$$\chi_i=\begin{cases}
    1, a_i \notin A[1..i] \setminus a_i,\\
    0, a_i \in A[1..i] \setminus a_i,
\end{cases}$$

Thus, the mathematical expectation would be

$$E[\text{unique elements}]=\sum^n_{i=1}E[\chi_i]$$

Calculate the number of permutations of numbers $1..n$ of length $i - 1$ that would not contain a certain value $k\in[1..i]$. This would yield us $(n-1)^{i-1}$ possible permutations and allow us to get the number of all possible sequences for a possibility to make that some taken $k$ a unique number.

Thus, comparing this to the number of all sequences up to $i$, we have $n^i$ total possible sequences. Thus, the chance that a certain single number out of a continual sequence is unique would be 

$$\frac{(n-1)^{i-1}}{n^i}$$

And if we desire for any number to be unique, we simply multiply this by the count of all numbers:

$$\frac{n(n-1)^{i-1}}{n^i}=\frac{(n-1)^{i-1}}{n^{i-1}}$$

Therefore,

$$E[\chi_i]=\frac{(n-1)^{i-1}}{n^{i-1}}$$

Calculate the geometric progression for starter element $b_1=1$ (since there is one unique element in the sequence of length $1$) and step $q=\frac{n-1}{n}$:

$$E[\text{unique elements}]=\sum^n_{i=1}\frac{(n-1)^{i-1}}{n^{i-1}} = \frac{b_1(1-q^n)}{1-q}=\frac{1(1-{\frac{(n-1)}{n}}^{n})}{1-\frac{(n-1)}{n}} =$$

$$= \frac{1-{\frac{(n-1)}{n}}^{n}}{1-\frac{(n-1)}{n}}=\frac{1-{\frac{(n-1)}{n}}^{n}}{\frac{n-(n-1)}{n}}=\frac{1-{\frac{(n-1)}{n}}^{n}}{\frac{1}{n}}=n \left(1 - \left(\frac{n - 1}{n}\right)^{n}\right)$$

### Subproblem B

Find the function that takes the form of $Cn^\alpha$, which would be equivalent to the derived mathematical expectation as $n\to\infty$.

---

Take the limit of the function above

$$\lim_{n\to\infty}\left(n\left(1 - \left(\frac{n - 1}{n}\right)^{n}\right)\right)=\lim_{n\to\infty}\left(1 - \left(\frac{n - 1}{n}\right)^{n}\right)\lim_{n\to\infty}n=$$

$$=\lim_{n\to\infty}\left(1 - \left(1-\frac{1}{n}\right)^{n}\right)\lim_{n\to\infty}n=\left(1-\frac{1}{e}\right)\lim_{n\to\infty}n\implies$$

$$C=1-\frac{1}{e},\quad f(n)=Cn$$

