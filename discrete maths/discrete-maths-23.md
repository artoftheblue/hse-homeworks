# Discrete Maths, Last Homework

## Problem 1

Find the last two digits of $99^{1000}$.

---

$$99^{1000}\equiv (-1)^{1000}\equiv 1 \mod 100$$

This implies that the last two digits are $01$.

## Problem 2

Prove that numbers $a^2$ and $b^2$ give the same remainders when dividing by $a-b$ if $a, b$ are positive integers and $a > b$.

---

$$a^2-b^2=(a+b)(a-b)\equiv 0 \mod (a-b)$$

Since the number is divisible by $(a-b)$, its remainder $\mod (a-b)$ is $0$, which implies that the same remainder is given.

## Problem 3

Let $x, y$ be integers. Prove that $x + 10y$ is divisible by $13 \iff u+4x$ is divisible by $13$.

---

$$\begin{align*}
x+10y\equiv 0 &\mod 13\iff\\
4x+40y\equiv 0 &\mod 13\iff\\
4x+39y+y\equiv 0&\mod 13\iff\\
4x+y\equiv 0&\mod 13
\end{align*}$$

## Problem 4

Solve a comparsion $53x\equiv 1 \mod 42$ using extended Euclidean algorithm.

---

$$53x\equiv1\mod42$$

We need to find the inverse of $53 \mod 42$. For this, solve

$$53x+42y\equiv 1\mod42$$

Write some code to execute extended euclidean algorithm:

    def extended_euclidean_algorithm(a, b):
        s, t = 1, 0
        s_prev, t_prev = 0, 1

        r, r_prev = a, b

        steps = []

        while r != 0:
            quotient = r_prev // r
            r_prev, r = r, r_prev - quotient * r
            s_prev, s = s, s_prev - quotient * s
            t_prev, t = t, t_prev - quotient * t

            steps.append((r_prev, s_prev, t_prev))

        return steps

    a = 53
    b = 42
    steps = extended_euclidean_algorithm(a, b)

    for step in steps:
        print(f"r={step[0]}, x={step[1]}, y={step[2]}")


As an answer, we get

    r=53, x=1, y=0
    r=42, x=0, y=1
    r=11, x=1, y=-1
    r=9, x=-3, y=4
    r=2, x=4, y=-5
    r=1, x=-19, y=24

$-19\equiv23\mod42\implies23$ is the solution. Check it:

$$53\times23\equiv1219\equiv1\mod42$$

**Answer:** $23$.