# Discrete Maths, Homework 19

## Problem 1

The probability space: sequences $(x_1,x_2)$ of length $2$ that consist of whole number in the $[0,9]$ range. All outcomes are equally probable. Find the probability of the event "$x_1\neq x_2$".

---

Given some $x_1$, the chance for the event $x_1=x_2$ (the next digit being the very same digit out of $10$) occurring is $\displaystyle\frac{1}{10}$.

Thus, the chance of $x_1\neq x_2$ is $\displaystyle1-\frac{1}{10}=\frac{9}{10}$.

> Alternatively, there are only $10$ sequences that have same numbers out of $100$ possible sequences, so the chance could be deduced from this information as well.

## Problem 2

Probability space: sequences $(x_1,x_2,x_3,x_4)$ of length $4$ that consist of whole numbers from $0$ to $2$. All outcomes are equally probable. Find the probability of the event "there are $0$, $1$, and $2$ in the sequence".

---

Total number of possible sequences: $3^4=81$.

Take all $3$-digit words of length $3$, there are $27$ in total. $3$ of them cannot be extended to a valid word of length $3$: $000,111,222$, leaving us with $24$ possible valid beginnings. 

Words that contain all three valid digits result in three possible valid sequences. There are $3!=6$ such words, resulting in $6\times3=18$ possible $4$-letter words.

$3$-letter words that are with $2$ digits which are the same and some other single digit can be extended to a valid word a single possible way, thus there are, $24-6=18$ such words, giving us the final number of valid sequences, $18+18=36$ valid words.

Thus, the chance of the required event is $\displaystyle\frac{36}{81}=\frac{4}{9}$.

---

## Problem 3

Probability space is all whole numbers from $1000$ to $9999$. All outcomes are equally probable. Find the probability of the event "the sum of digits is equal to $9$".

---

Using the stars and bars formula, we need to place $3$ bars between $8$ ones:

$$(1)111|1|11|11\mapsto 4122$$

Thus, the number of such numbers for $n=4, k=8$ would be

$$\left({n\choose k}\right)={n+k-1\choose k}={4+8-1\choose 8}={11 \choose 8}=$$

$$=\frac{11!}{8!3!}=\frac{11\times10\times9}{3\times2\times1}=11\times5\times3=165$$

Thus, the probability is $\displaystyle\frac{165}{9000}=\frac{11}{600}$.

## Problem 4

Probability space: binary words of length $23$. All outcomes are equally probable. Find the probability of an event "on first $11$ positions there are less ones than on the last $12$".

---

Take any word like the following and reverse its bits:

$$\underbrace{00010101101}_5|\underbrace{001010100111}_6\mapsto\underbrace{11101010010}_{11-5=6}|\underbrace{110101011000}_{12-6=6}$$

This way, we may establish a bijection between all the words that have less ones on the first $11$ positions and those that a more or equal number of ones on the first $11$ positions, compared to the last $12$. Since we obviously can do that for every single number, splitting the entire probability space into $2$ equal parts, and the probability in the answer would be $\displaystyle\frac{1}{2}$.