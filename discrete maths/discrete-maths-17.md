# Discrete Maths, Homework 17

## Problem 1

Consider partial orders, in which there are precisely $5$ minimal and $5$ maximal elements. Find the smallest number of elements in such partial orders.

---

Per given conditions, there should be $5$ different minimal and $5$ different maximal elements (if two minimal/maximal elements overlap, their number would decrease). 

Per definitions:

* an element is maximal if $\nexists x\in P$ such that $x < a$
* an element is minimal if $\nexists x\in P$ such that $x > a$

Take $5$ independent maximal elements and make them also minimal elements. This means that all of these elements are incomparable and thus are all both maximal and minimal. If we were to remove any of these elements, we would go below the required condition of having $5$ elements $\implies$ it's impossible to have a smaller number of elements in such partial orders.

**Answer:** $5$.

## Problem 2

A binary relation on a set of $7$ elements contains precisely $20$ pairs. Is it possible that it is

### Subproblem A

a strict partial order relation?

---

Yes, here is an example:

![alt text](image-28.png)

It was constructed by first taking a linear order of length $5$, which would have $\displaystyle \sum^{5-1=4}_{i}i=4+3+2+1=10$ pairs. Then, we add two more nodes to the start (or to the end, technically doesn't matter) of the linear order and to maintain transitivity, link the prepended nodes by creating an edge between each prependee and each member of the linear order, thus adding $5\times2$ total pairs. The total would be $10+10=20$, so it is possible, q. e. d. 

A slightly more masochistic example is the following:

![alt text](image-30.png)

**Answer:** yes

### Subproblem B

a strict linear order relation?

---

In order to prove this, we should check how many pairs there are in a strict linear order relation on $7$ elements (we make an edge between each pair of elements):

$$\displaystyle \sum^{7-1=6}_{i}i=6+5+4+3+2+1=21$$

Thus, the only and the minimum required number of pairs in a linear order of length $7$ is $21$. Therefore, it is not possible to construct a strict linear order relation on $7$ elements with only $20$ connected pairs, q. e. d.

**Answer:** no

## Problem 3

Prove that a strict order on $14$ elements with $50$ adjacent pairs does not exist.

---

In order to disprove this, we should somehow find the maximum number of pairs in such a relation. For this, we shall take an element and make it comparable to some number of other elements. 

We could split all elements into a bipartite graph in some proportion and try to maximize the number of total edges between the parts. The action of splitting all elements into two parts is justified over splitting the elements into n-partite graphs with $n>2$ since we want to maximize the number of edges (why would we create more parts if that would strip us of the possibility to make edges within the part?). 

This is perhaps the most common optimization problem of maximizing the area of a rectangle with a certain perimeter (the maximum area is when the sides are the closest to each other in terms of length, thus the maximum number of edges is $7\times7=49$, and not $50$), but I'll present a proper solution:

The number of elements in the left part of the graph is $N$, the number of elements in the right part of the graph is $N-14$. The number of total pairs is $f(N)=N(14-N)$.

By plotting the graph, we find the maximum solution at $N=7$ when $f(7)=49$. Since this is the maximum of the function, it's impossible for the requested value to be equal to $50$, q. e. d.

![alt text](image-29.png)



## Problem 4

Prove that linear orders $\mathbb{N}\times_{lex}\mathbb{Z}$ and $\mathbb{Z}\times_{lex}\mathbb{Z}$ are not isomorphic.

---

Let's redefine each pair $(\mathbb{N},\mathbb{Z})$ and $(\mathbb{Z},\mathbb{Z})$ as words. For instance, $(1, -3)\mapsto \text{1-3}$. Plot them on blank paper:

As it could be easily seen from the plots, each subset $(\mathbb{N},z)\in\mathbb{N}\times_{lex}\mathbb{Z}, z\in\mathbb{Z}$ has a minimum of $(0, z)$, whereas there are no minimums in corresponding subsets of $(z_1,\mathbb{Z}),(\mathbb{Z}, z_2)\in\mathbb{Z}\times_{lex}\mathbb{Z}, z_1,z_2\in\mathbb{Z}$. Since isomorphic mappings preserve invariants and there is an invariantic condition (minimum) in the first product but not the second one, the linear orders are not isomorphic, q. e. d.

![alt text](image-31.png)

![alt text](image-32.png)

