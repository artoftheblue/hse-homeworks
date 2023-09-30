# Homework 3

## Problem 3.1

Per definition, functions from $A$ to $B$ are subsets of $A\times B$, and therefore, theoretical set operations are applicable to them. Let $f, g$ be two functions from $A$ to $B$.

Is it true that: 

### Subproblem A

Their union is also a function?

---

In other words, we need to prove that their union ($f \cup g$) is a subset of $A\times B$.

Let $\forall n,m \in \mathbb{N} \colon a_n \in A, b_m \in B$; therefore,

$$A\times B=
\begin{Bmatrix}
    (a_1, b_1) & \dots & (a_1, b_m) \\
    \vdots & \ddots & \vdots \\  
    (a_n, b_1) & \dots & (a_n, b_m) 
\end{Bmatrix}
$$

Take some $A', A'' \subseteq A$ and some $B', B'' \subseteq B$ such that $\forall x, f\colon A' \mapsto B', g\colon A'' \mapsto B''$.

Now, for some $K_p = \{k \ | \ k \in \mathbb{N}\}$ (different $p$-s are selected for each set), the following is true:

* for $K_{p_1}\colon\{a_k \ | \ k \in \mathbb{N}, 1\leq k\leq n  \} = A'$
* for $K_{p_2}\colon\{a_k \ | \ k \in \mathbb{N}, 1\leq k\leq n  \} = A''$
* for $K_{p_3}\colon\{b_k \ | \ k \in \mathbb{N}, 1\leq k\leq n  \} = B''$
* for $K_{p_4}\colon\{b_k \ | \ k \in \mathbb{N}, 1\leq k\leq n  \} = B''$

If we take the union of these sets, then the domans and ranges "merge" (merging together pairs from either $f$, $g$, or both):

* $\text{Dom} \ (f \cup g) = \text{Dom} \ f \cup \text{Dom} \ g=A' \cup A''$;
* $\text{Range} \ (f \cup g) = \text{Range} \ f \cup \text{Range} \ g=B' \cup B''$.

Therefore, $(f \cup g)(x) \colon A' \cup A'' \mapsto B' \cup B''$, which means that any $(x,y) \in A' \cup A'' \times B' \cup B''$ since $(x, y) \in f \lor (x, y) \in g$ So, the union of two functions is a function since the range and domain of the resulting function are subsets of $A\times B$, q. e. d.

### Subproblem B

Their intersection is also a function?

---

In other words, we need to prove that their union ($f \cap g$) is a subset of $A\times B$.

`-- || -- This part is identical to above, so it was omitted -- || -- `

If we take the intersection of these sets, then the domans and ranges intersectand only pairs that previously were in both sets remain:

* $\text{Dom} \ (f \cap g) = \text{Dom} \ f \cap \text{Dom} \ g=A' \cap A''$;
* $\text{Range} \ (f \cap g) = \text{Range} \ f \cap \text{Range} \ g=B' \cap B''$.

Therefore, $(f \cap g)(x) \colon A' \cap A'' \mapsto B' \cap B''$, which means that any $(x,y) \in A' \cap A'' \times B' \cap B''$ since $(x, y) \in f \lor (x, y) \in g$. So, the intersection of two functions is a function since the range and domain of the resulting function are subsets of $A\times B$, q. e. d.

## Problem 2

Prove that function $f\colon (x_0,x_1,\dots,x_{n-1})\mapsto(x_0+0,x_1+1,\dots,x_{n-1}+n-1)$ is a bijection from the set of non-descending integer sequences to the set of strictly ascending integer sequences. 

Since the function has a clearly range and domain, it's total and not partial. 

According to bijection definition, the function should be both a surjection and an injection:

* injection definition: $f(x)\colon A \mapsto B, \forall x, y \colon x \neq y \Rightarrow f(x) \neq f(y)$
* surjection definition: $f(x)\colon A \mapsto B, \text{Range}\ f = B, \forall y \in B, \exists x \in A, (x, y) \in f$

Consider the sequence $(x_0,x_1,\dots,x_{n-1})$, which is non-descending, $\Rightarrow x_0 \leq x_1 \leq \dots \leq x_{n-1}$.

Add $1$ to every element of the equation and compare to $x_0$:

$$x_0<x_0 + 1 \leq x_1 + 1 \leq \dots \leq x_{n-1} + 1$$

Omit $x_0 + 1$ from the equation to get the first part of the result inequation:

$$x_0 + 0<x_1 + 1 \leq \dots \leq x_{n-1} + 1$$

By induction, repeat the same steps over and over again to arrive at the following inequation:

$$x_0+0<x_1+1<\dots<x_{n-1}+n-1$$

Next, since the same constant is added to each element $x_n$ depending on its position, then the action that happens is a kind of "a parallel shift" that "shifts" all the values to a set of different ones linearly, so it's impossible for multiple values to map to the same value $\Rightarrow f\colon (x_0,x_1,\dots,x_{n-1})\mapsto(x_0+0,x_1+1,\dots,x_{n-1}+n-1), \forall x_k, x_p \colon x_k \neq x_p \Rightarrow f(x_k) \neq f(x_p) \Rightarrow$ the function is an injection.

Lastly, say that $(b_1, b_2, \dots b_{n+1})$ is some sequence. Then we can restore the original sequence using an inverse function $f^{-1}$ that subtracts $n$ from every $n$-th number. Since the inverse of a linear function is also linear, then the entire $\text{Range}\ f$ can be mapped to $\text{Range}\ f^{-1}$ and vice versa via linear transformations. The field of any sequence of numbers of any length is reachable through linear transformations, so $\text{Range}\ f = (x_0+0,x_1+1,\dots,x_{n-1}+n-1)$ includes all possible sequences and $\forall y \in B, \exists x \in A, (x, y) \in f$, which was just described above.

The function $f$ is both an injection and a surjection $\Rightarrow$ the function is a bijection, q. e. d.

## Problem 3 (it has been annihilated so there is nothing)

<center>
    <img src="C:\Users\Artyom\Documents\GitHub\hse-homeworks\assets\img\kitty.png" style="height: 300px; width:300px;"/>
</center>

## Problem 4

Set $A$ consists of triangles, the sides of which are all natural numbers (and not equal to $0$), and their perimeter is equal to $2020$.

Set $B$ consists of triangles, the sides of which are all natural numbers (and not equal to $0$), and their perimeter is equal to $2023$. What is larger, $|A|$ or $|B|$?

$$A=\{(a_A, b_A, c_A) \ | \ a_A + b_A + c_A = 2020, a_A + b_A > c_A, a_A + c_A > b_A, b_A + c_A > a_A \}$$

$$B=\{(a_B, b_B, c_B) \ | \ a_B + b_B + c_B = 2023, a_B + b_B > c_B, a_B + c_B > b_B, b_B + c_B > a_B\}$$

Add $1$ to each of the sides in set $A$, then $a_A + 1 + b_A + 1 + c_A + 1 = 2023$ (all the equations could be conserved because we would add $2$ to its lefthand side, which more than we add to the righthand side). Then, we could map every single element from $A \mapsto$ some element from $B$: 

$$(a_A, b_A, c_A) \mapsto (a_A + 1, b_A + 1, c_A + 1)$$

Attempt to find some value in $B$ that is not in $A$. It is obvious that for some $a_B = a_A + 1 \geq 2$ since $a_A \geq 1$. Therefore, find such a triple $\in B$ that for $a_A = 1$ and a triangle with a perimeter of $2023$ exists:

$$(a_B, b_B, c_B)=(1, 1011, 1011)$$

Since $1 + 1011 > 1011$, $1011 + 1011 > 1$, $1 + 1011 > 1011$, then this is an unmapped value in set $B \Rightarrow$ there are more elements in $B$ than in $A \Rightarrow |B| > |A|$

Answer: $|B| > |A|$