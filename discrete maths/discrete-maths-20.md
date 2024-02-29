# Homework 20, Discrete Maths

## Problem 1

Choose an arbitary function $f\colon\{1,2,\dots,n\}\mapsto\{1,2,\dots,n\}$. All outcomes are equally probable. Are events "$f(1)=f(2)$" and "$f(2)=f(3)$" independent?

---

> Technically this might be sufficient since it's kinda obvious, but obviousness here frequently doesn't work, so I'll also present a stricter approach. 
> Values $f(n)$ are independent from one another, and every value of $f(n)$ for any $n$ is equally probable with a probability of $\displaystyle\frac{1}{n}$.
> Let's fix the value of $f(2)=\text{const}$. Then, the first event is dependent only on the value of $f(1)$, and the second event is dependent only on the value of $f(3)$, which means they're independent.

For the events to be independent, the following has to be true:

$$P[A\cap B]=P[B]\cdot P[A]$$

What is the probability of $P[B]$ and $P[A]$ independently? Kinda follow the approach above. Say, that we have already chosen $f(2)$, and need to choose $f(1)$ for event $A$ and $f(3)$ for event $B$. For the events to happen, our chosen values for $f(1), f(3)$ have to be the same as $f(2)$. $f(2)$ has already been chosen out of $n$ equally probable options, so the chance of choosing the same option as $f(2)$ for each of these cases (independently, for now) is $\displaystyle\frac{1}{n}$.

> Note that the above explanations apply symmetrically if we were to first choose $f(1)$ or $f(3)$, respectively, and only then choose $f(2)$ for each of the cases.

Thus, 

$$P[A]=\frac{1}{n},\quad P[B]=\frac{1}{n}$$

Now, what are the chances of the event $A\cap B$ occurring? This event would be called "$f(1)=f(2)=f(3)$". Let's calculate its chance of occurring: fix $f(1)$ to some value. We need to calculate the chance that $f(2),f(3)$ would be the same as $f(1)$, so we need to choose a specific number out of $n$ options, twice, thus giving us a probability of $\displaystyle\frac{1}{n}\cdot\frac{1}{n}=\frac{1}{n^2}$.

Thus, 

$$P[A\cap B]=\frac{1}{n^2}=\frac{1}{n}\cdot\frac{1}{n}=P[A]\cdot P[B]$$

which means that the events are independent from each other.

## Problem 2

In a lotto, four numbers out of $\{1,2,\dots,16\}$ are chosen randomly and with equally probable chances. Find the probability of an event $A$ "there is no $13$ among the chosen numbers" under a condition $B$ that "there is no $1$ among the chosen numbers".

---

The probability space is all sequences with non-repeating numbers of length $4$ from the set above. This gives us 

$$A^{4}_{16}=\frac{16!}{(16-4)!}=16\times15\times14\times13$$

total possible sequences.

The number of sequences when event $A$ or event $B$ occur are (we just remove a single number from the pool of possible options):

$$A^4_{15}=\frac{15!}{(15-4)!}=15\times14\times13\times12$$

Now, we know that 

$$P[A|B]=\frac{P[A\cap B]}{P[B]}$$

Event $A\cap B$ could be defined as "there is neither $13$ or $1$ among the chosen numbers", which gives us 

$$A^4_{14}=\frac{14!}{(14-4)!}=14\times13\times12\times11$$

possible options.

Now, 

$$P[B]=\frac{15\times14\times13\times12}{16\times15\times14\times13}=\frac{3}{4}$$

$$P[A\cap B]=\frac{14\times13\times12\times11}{16\times15\times14\times13}=\frac{3}{4}\cdot\frac{11}{15}=\frac{33}{60}$$

Finally,

$$P[A|B]=\frac{\frac{33}{60}}{\frac{3}{4}}=\frac{11}{15}$$

which is the final answer.

## Problem 3

Four people $A,B,C,$ and $D$ form a queue in a random order (all options are equally probable). Find the conditional probability that $A$ precedes $B$ (event $X$) if it is known that $A$ precedes $C$ (event $Y$).

---

We once again need to use the formula from above:

$$P[X|Y]=\frac{P[X\cap Y]}{P[Y]}$$

To find the number of possible options, I will just list them all. There are obviously $4!$ permutations, resulting in $24$ options:

         Y | X & Y
    ABCD V     V
    ABDC V     V
    ACBD V     V
    ACDB V     V
    ADBC V     V
    ADCB V     V
    BACD V     X
    BADC V     X
    BCAD X     X
    BCDA X     X
    BDAC V     X
    BDCA X     X
    CABD X     X
    CADB X     X
    CBAD X     X
    CBDA X     X
    CDAB X     X
    CDBA X     X
    DABC V     V
    DACB V     V
    DBAC V     X
    DBCA X     X
    DCAB X     X
    DCBA X     X

We have $8$ options for $A\cap B$ and $12$ options for $B$.

Thus, 

$$P[Y]=\frac{12}{24}=\frac{1}{2},\quad P[X\cap Y]=\frac{8}{24}=\frac{1}{3}$$

and

$$P[X|Y]=\frac{P[X\cap Y]}{P[Y]}=\frac{\frac{8}{24}}{\frac{1}{2}}=\frac{16}{24}=\frac{2}{3}$$

## Problem 4

In the first box there are $9$ chips enumerated from $1$ to $9$. In the second box there are $10$ chips, enumerated from $2$ to $11$. Chips in each box differ from each other only by numbers. A random box is chosen with equal probabilities, and then a random chip is chosen with equal probabilities from the chosen box. What is the probability that a box with $10$ chips is chosen (event $A$) if a chip with number $7$ was pulled out (event $B$)?

---

Let's denote chosen chips with two coordinates: its box number and its own number. Formula from above strikes again:

$$P[A|B]=\frac{P[A\cap B]}{P[B]}$$

The chance that we choose either boxes is $\displaystyle\frac{1}{2}$. Thus, we may split the field of probabilities into two parts. The first part would have each of the events "chips with certain coordinates is pulled"

$$(1, 1), (1, 2), \dots (1, 9)$$

occur with a probability of $\displaystyle\frac{1}{2}\times\frac{1}{9}=\frac{1}{18}$ since we divide this half into $9$ equally probable events.

Whereas similar events for the second box

$$(2, 2), (2, 3), \dots (2, 11)$$

each occur with a probability of $\displaystyle\frac{1}{2}\times\frac{1}{10}=\frac{1}{20}$ since here we have $10$ equally probable options.

Thus, the chance of pulling a chip with number $7$ is equal to the sum of respective probabilities from each of the boxes:

$$P[B]=\frac{1}{18}+\frac{1}{20}=\frac{19}{180}$$

The chance of a certain chip with number $7$ from the second box is simply

$$P[A\cap B]=\frac{1}{20}$$

Finally,

$$P[A|B]=\frac{\frac{1}{20}}{\frac{19}{180}}=\frac{9}{19}$$

which is the final answer.