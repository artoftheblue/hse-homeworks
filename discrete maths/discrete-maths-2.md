## Problem 2.1

Given sequence $A=(1,2,3,4,5,6,7,8,9,1,0,1,1,1,2, \dots, 2, 0, 2, 3)$, find the number of zeros in the sequence.

#### Solution

In the patterns below, $?$ denotes any non-zero digit.

|number patterns|number count|zero count|total|
|-:|:-:|:-:|:-|
|$?0$|$9$|$1$|$9$|
|$?00$|$9$|$2$|$18$|
|$?0?, ??0$|$2\times9\times9$|$1$|$162$|
|$?000$|$2$|$3$|$6$|
|$10??, 1?0?, 1??0$|$3\times9\times9$|$1$|$243$|
|$1?00, 10?0, 100?$|$3\times9$|$2$|$54$|
|$200?$|$9$|$2$|$18$|
|$2010, 2020$|$2$|$2$|$4$|
|$201?$|$9$|$1$|$9$|
|$2021, 2022, 2023$|$3$|$1$|$3$|
|$\Sigma$|||$526$|

#### Answer

$526$

## Problem 2.2

How many ways are there to choose two squares on a $10\times10$ board so that they would not have any adjacent corners or edges?

#### Solution

I will map all the cases on a $10\times10$ markdown board.

* O - example chosen square;
* X - adjacent square that cannot be chosen;
* V - other possible chosen squares;
* Z - X or V.

Case $1$, the first chosen square is a corner:

||1|2|3|4|5|6|7|8|9|10|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|O|X|.|.|.|.|.|.|.|V|
|2|X|X|.|.|.|.|.|.|.|.|
|3|.|.|.|.|.|.|.|.|.|.|
|4|.|.|.|.|.|.|.|.|.|.|
|5|.|.|.|.|.|.|.|.|.|.|
|6|.|.|.|.|.|.|.|.|.|.|
|7|.|.|.|.|.|.|.|.|.|.|
|8|.|.|.|.|.|.|.|.|.|.|
|9|.|.|.|.|.|.|.|.|.|.|
|10|V|.|.|.|.|.|.|.|.|V|

There are $4$ corners in total and $100-4=96$ ways to choose the second square $n_{corners}=4\times96 = 384$.

Case 2, the first chosen square is an edge:

||1|2|3|4|5|6|7|8|9|10|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|X|O|Z|V|V|V|V|V|V|.|
|2|Z|X|X|.|.|.|.|.|.|V|
|3|V|.|.|.|.|.|.|.|.|V|
|4|V|.|.|.|.|.|.|.|.|V|
|5|V|.|.|.|.|.|.|.|.|V|
|6|V|.|.|.|.|.|.|.|.|V|
|7|V|.|.|.|.|.|.|.|.|V|
|8|V|.|.|.|.|.|.|.|.|V|
|9|V|.|.|.|.|.|.|.|.|V|
|10|.|V|V|V|V|V|V|V|V|.|

There are $32$ edges in total and $100-6=94$ ways to choose the second square $n_{edges}=32\times94=3008$.

Case 3, the first chosen square is one of the centers:

||1|2|3|4|5|6|7|8|9|10|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|X|X|X|.|.|.|.|.|.|.|
|2|X|O|Z|V|V|V|V|V|V|.|
|3|X|Z|Z|V|V|V|V|V|V|.|
|4|.|V|V|V|V|V|V|V|V|.|
|5|.|V|V|V|V|V|V|V|V|.|
|6|.|V|V|V|V|V|V|V|V|.|
|7|.|V|V|V|V|V|V|V|V|.|
|8|.|V|V|V|V|V|V|V|V|.|
|9|.|V|V|V|V|V|V|V|V|.|
|10|.|.|.|.|.|.|.|.|.|.|

There are $64$ centers in total and $100-9=91$ ways to choose the second square $n_{centers}=64\times91=5824$.

Here it has to be noted that the order of the chosen squares does not matter, therefore the final result will be the sum of all $n$-s **divided by 2.**

Total $n=\frac{1}{2}(n_{corners}+n_{edges}+n_{centers})=\frac{1}{2}(5824+3008+384)=4608$

#### Answer 

$4608$

## Problem 2.3

### Subproblem A

Prove that $(A_1 \setminus A_2)\times(B_1 \setminus B_2) \subseteq (A_1 \times B_1) \setminus (A_2 \times B_2)$ is true for any sets $A_1, A_2, B_1, B_2$.

#### Solution

Assuming that $\forall n_k, m_k \in \mathbb{N}$, define the following:

* $a_{0,n_k} \in A_1, A_2$;
* $a_{1,n_k} \in A_1$ and $a_{1, n} \notin A_2$;
* $a_{2,n_k} \in A_2$ and $a_{2, n} \notin A_1$;
* $b_{0,n_k} \in B_1, B_2$;
* $b_{1,n_k} \in B_1$ and $b_{1, n} \notin B_2$;
* $b_{2,n_k} \in B_2$ and $b_{2, n} \notin B_1$;
* $A_1 = (a_{1,1}, a_{1,2}, \dots, a_{1,n_1}, a_{0,1}, a_{0, 2}, \dots, a_{0,n_0})$;
* $A_2 = (a_{2,1}, a_{2,2}, \dots, a_{2,n_2}, a_{0,1}, a_{0, 2}, \dots, a_{0,n_0})$;
* $B_1 = (b_{1,1}, b_{1,2}, \dots, b_{1,m_1}, b_{0,1}, b_{0, 2}, \dots, b_{0,m_0})$;
* $B_2 = (b_{2,1}, b_{2,2}, \dots, b_{2,m_2}, b_{0,1}, b_{0, 2}, \dots, b_{0,m_0})$.

Then, considering

* $A_1 \setminus A_2 = \{a_{1,1}, a_{1,2}, \dots, a_{1,n_1}\}$;
* $B_1 \setminus B_2 = \{b_{1,1}, b_{1,2}, \dots, b_{1,m_1}\}$;

Evaluate the **lefthand side** of the statement above:
$$(A_1 \setminus A_2)\times(B_1 \setminus B_2) = \{(a_{1,1}, b_{1, 1}), (a_{1,1}, b_{1,2}),\dots,(a_{1,1}, b_{1,m_1}), \\(a_{1,2}, b_{1, 1}), (a_{1,2}, b_{1,2}),\dots,(a_{1,2}, b_{1,m_1}),\\
\dots, \ \ \dots, \ \ \dots, \ \ \dots, \ \ \dots, \ \ \dots, \ \ \dots, \\
(a_{1,n_1}, b_{1, 1}), (a_{1,n_1}, b_{1,2}),\dots,(a_{1,n_1}, b_{1,m_1})\}$$

---

<img src="C:\Users\Artyom\Documents\GitHub\hse-homeworks\discrete maths\dm2-1.png" style="height: 400px; width:400px;"/>

---

Now, to evaluate the **righthand side** of the statement above, first calculate the following:

$$A_1 \times B_1 = \{(a_{1,1}, b_{1,1}), (a_{1,1}, b_{1,2}), \dots, (a_{1,1}, b_{1,m_1}), (a_{1,1}, b_{0,1}), (a_{1,1}, b_{0, 2}), \dots, (a_{1,1}, b_{0,m_0}),\\ (a_{1,2}, b_{1,1}), (a_{1,2}, b_{1,2}), \dots, (a_{1,2}, b_{1,m_1}), (a_{1,2}, b_{0,1}), (a_{1,2}, b_{0, 2}), \dots, (a_{1,2}, b_{0,m_0}),\\\dots, \ \ \dots, \ \ \dots, \ \ \dots, \ \ \dots, \ \ \dots, \ \ \dots, \ \ \dots, \ \ \dots, \ \ \dots, \ \ \dots, \ \ \dots, \ \ \dots, \ \ \dots,\\(a_{1,n_1}, b_{1,1}), (a_{1,n_1}, b_{1,n_1}), \dots, (a_{1,n_1}, b_{1,m_1}), (a_{1,n_1}, b_{0,1}), (a_{1,n_1}, b_{0, 2}), \dots, (a_{1,n_1}, b_{0,m_0}),\\(a_{0,1}, b_{1,1}), (a_{0,1}, b_{1,2}), \dots, (a_{0,1}, b_{1,m_1}), (a_{0,1}, b_{0,1}), (a_{0,1}, b_{0, 2}), \dots, (a_{0,1}, b_{0,m_0}),\\ (a_{0,2}, b_{1,1}), (a_{0,2}, b_{1,2}), \dots, (a_{0,2}, b_{1,m_1}), (a_{0,2}, b_{0,1}), (a_{0,2}, b_{0, 2}), \dots, (a_{0,2}, b_{0,m_0}),\\\dots, \ \ \dots, \ \ \dots, \ \ \dots, \ \ \dots, \ \ \dots, \ \ \dots, \ \ \dots, \ \ \dots, \ \ \dots, \ \ \dots, \ \ \dots, \ \ \dots, \ \ \dots,\\(a_{0,n_0}, b_{1,1}), (a_{0,n_0}, b_{1,n_1}), \dots, (a_{0,n_0}, b_{1,m_1}), (a_{0,n_0}, b_{0,1}), (a_{0,n_0}, b_{0, 2}), \dots, (a_{0,n_0}, b_{0,m_0}),\}$$

$$A_2 \times B_2 = \{(a_{2,1}, b_{2,1}), (a_{2,1}, b_{2,2}), \dots, (a_{2,1}, b_{2,m_2}), (a_{2,1}, b_{0,1}), (a_{2,1}, b_{0, 2}), \dots, (a_{2,1}, b_{0,m_0}),\\ (a_{2,2}, b_{2,1}), (a_{2,2}, b_{2,2}), \dots, (a_{2,2}, b_{2,m_2}), (a_{2,2}, b_{0,1}), (a_{2,2}, b_{0, 2}), \dots, (a_{2,2}, b_{0,m_0}),\\\dots, \ \ \dots, \ \ \dots, \ \ \dots, \ \ \dots, \ \ \dots, \ \ \dots, \ \ \dots, \ \ \dots, \ \ \dots, \ \ \dots, \ \ \dots, \ \ \dots, \ \ \dots,\\(a_{2,n_2}, b_{2,1}), (a_{2,n_2}, b_{2,n_2}), \dots, (a_{2,n_2}, b_{2,m_2}), (a_{2,n_2}, b_{0,1}), (a_{2,n_2}, b_{0, 2}), \dots, (a_{2,n_2}, b_{0,m_0}),\\(a_{0,1}, b_{2,1}), (a_{0,1}, b_{2,2}), \dots, (a_{0,1}, b_{2,m_2}), (a_{0,1}, b_{0,1}), (a_{0,1}, b_{0, 2}), \dots, (a_{0,1}, b_{0,m_0}),\\ (a_{0,2}, b_{2,1}), (a_{0,2}, b_{2,2}), \dots, (a_{0,2}, b_{2,m_2}), (a_{0,2}, b_{0,1}), (a_{0,2}, b_{0, 2}), \dots, (a_{0,2}, b_{0,m_0}),\\\dots, \ \ \dots, \ \ \dots, \ \ \dots, \ \ \dots, \ \ \dots, \ \ \dots, \ \ \dots, \ \ \dots, \ \ \dots, \ \ \dots, \ \ \dots, \ \ \dots, \ \ \dots,\\(a_{0,n_0}, b_{2,1}), (a_{0,n_0}, b_{2,n_2}), \dots, (a_{0,n_0}, b_{2,m_2}), (a_{0,n_0}, b_{0,1}), (a_{0,n_0}, b_{0, 2}), \dots, (a_{0,n_0}, b_{0,m_0}),\}$$

And then, considering the above, the following:

$$(A_1 \times B_1) \setminus (A_2 \times B_2)= \\\{(a_{1,1}, b_{1,1}), (a_{1,1}, b_{1,2}), \dots, (a_{1,1}, b_{1,m_1}), (a_{1,1}, b_{0,1}), (a_{1,1}, b_{0, 2}), \dots, (a_{1,1}, b_{0,m_0}),\\ (a_{1,2}, b_{1,1}), (a_{1,2}, b_{1,2}), \dots, (a_{1,2}, b_{1,m_1}), (a_{1,2}, b_{0,1}), (a_{1,2}, b_{0, 2}), \dots, (a_{1,2}, b_{0,m_0}),\\\dots, \ \ \dots, \ \ \dots, \ \ \dots, \ \ \dots, \ \ \dots, \ \ \dots, \ \ \dots, \ \ \dots, \ \ \dots, \ \ \dots, \ \ \dots, \ \ \dots, \ \ \dots,\\(a_{1,n_1}, b_{1,1}), (a_{1,n_1}, b_{1,n_1}), \dots, (a_{1,n_1}, b_{1,m_1}), (a_{1,n_1}, b_{0,1}), (a_{1,n_1}, b_{0, 2}), \dots, (a_{1,n_1}, b_{0,m_0}),\\(a_{0,1}, b_{1,1}), (a_{0,1}, b_{1,2}), \dots, (a_{0,1}, b_{1,m_1}), \\ (a_{0,2}, b_{1,1}), (a_{0,2}, b_{1,2}), \dots, (a_{0,2}, b_{1,m_1}),\\\dots, \ \ \dots, \ \ \dots, \ \ \dots, \ \ \dots, \ \ \dots, \ \ \dots,\\(a_{0,n_0}, b_{1,1}), (a_{0,n_0}, b_{1,n_1}), \dots, (a_{0,n_0}, b_{1,m_1})\}$$

---

<img src="C:\Users\Artyom\Documents\GitHub\hse-homeworks\discrete maths\dm2-2.png" style="height: 400px; width:400px;"/>

---

This makes it obvious that $(A_1 \setminus A_2)\times(B_1 \setminus B_2) \subseteq (A_1 \times B_1) \setminus (A_2 \times B_2)$ is true as every single item from the set on the lefthand side of the statement is included in the righthand side set regardless of the fact whether sets $A_1, A_2, B_1, B_2$ intersect or not, q. e. d.

### Subproblem B

Is $(A_1 \times B_1) \setminus (A_2 \times B_2) \subseteq (A_1 \setminus A_2)\times(B_1 \setminus B_2)$ true for any sets $A_1, A_2, B_1, B_2$?

#### Solution

As shown above, $(A_1 \times B_1) \setminus (A_2 \times B_2)$ always contains all elements from $(A_1 \setminus A_2)\times(B_1 \setminus B_2)$.

$(A_1 \times B_1) \setminus (A_2 \times B_2)$ also contains elements from $A_1 \cap B_2$ and $A_2 \cap B_1$, which proves the reversed statement $(A_1 \times B_1) \setminus (A_2 \times B_2) \subseteq (A_1 \setminus A_2)\times(B_1 \setminus B_2)$ false unless $A_1 \cap B_2 = \{\varnothing\}$ or $A_2 \cap B_1=\{\varnothing\} \Rightarrow$ the statement is irreversible. 

#### Answer 

False

## Problem 2.4

For any whole positive $n$, prove the equation:

$$n \cdot 2^0 + (n-1)\cdot 2^1 + (n-2)\cdot 2^2 + \dots + 1 \cdot 2^{n-1}=2^{n+1}-2-n$$

#### Solution

Check whether the equation is true for $n=1$ (**induction base**):

$$1\cdot2^0=2^{1+1}-2-1$$

$$1=1$$

State the **induction hypothesis**:

$$n \cdot 2^0 + (n-1)\cdot 2^1 + (n-2)\cdot 2^2 + \dots + 1 \cdot 2^{n-1}=2^{n+1}-2-n$$

To check whether the induction hypothesis holds for $n+1$ (**induction step**), add the following expression to both parts of the equation:

$$2^0 + 2^1 + 2^2 + \dots + 2^{n-1} + 2^n$$

Therefore, we get: 

$$(n + 1) \cdot 2^0 + n\cdot 2^1 + (n-1)\cdot 2^2 + \dots + 2 \cdot 2^{n-1} + 1 \cdot 2^n= \\=2^0 + 2^1 + 2^2 + \dots + 2^{n-1} + 2^n + 2^{n+1} -2-n$$

Rewriting $2^0 + 2^1 + 2^2 + \dots + 2^{n-1} + 2^n$ in binary, we get $1_2 + 10_2 + 100_2 + \dots + 1\underbrace{000\dots0}_{n}\\_2$, which is equal to $\underbrace{111\dots1}_{n+1}\\_2$. Therefore, $2^0 + 2^1 + 2^2 + \dots + 2^{n-1} + 2^n = 2^{n+1} - 1$.

Rewrite the equation further:

$$(n + 1) \cdot 2^0 + n\cdot 2^1 + (n-1)\cdot 2^2 + \dots + 2 \cdot 2^{n-1} + 1 \cdot 2^n= \\=2^0 + 2^1 + 2^2 + \dots + 2^{n-1} + 2^n + 2^{n+1} -2-n=2^{n+2}-1-2-n=\\=2^{n+2}-2-(n+1) \Rightarrow\\n \cdot 2^0 + (n-1)\cdot 2^1 + (n-2)\cdot 2^2 + \dots + 1 \cdot 2^{n-1}=2^{n+1}-2-n$$

q. e. d.