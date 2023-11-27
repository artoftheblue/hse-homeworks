# Discrete Mathematics, Homework 10

## Problem 1

### Subproblem A

Is it true that the composition of reflexive relations over set $A$ is reflexive?

---

Per the definition of composition, $(a,a)\in R \circ R$ only if there is $x \in A$ so that $(a,x)\in R$ and $(x,a) \in R$. Since $R$ is reflexive, then take $x=a$ and then since $(a, a) \in R$ and (duh) $(a, a) \in R$ then $(a, a) \in R\circ R$, q. e. d.

**Answer:** yes, it is true.

### Subproblem B

Is it true that the composition of antireflexive relations over set $A$ is antireflexive?

--- 

Per the definition of antireflexiveness, $(a, a) \not\in R$. Prove by counter-example:

$$R_1=\{(a, x)\} \ \ R_2=\{(x,a)\} \ \ R_1 \circ R_2 =\{(a,a)\}$$

$R_1 \circ R_2$ is reflexive, therefore no, it is not true.

**Answer:** no, it is not true.

## Problem 2

Give an example of a relation that is not reflexive, nor antireflextive, nor symmetric, nor antisymmetric, nor transitive, but is total.

--- 

Consider the following relation over $\{0,1,2\}$, we will define it everywhere, **so it would be total**:

| | $0$ | $1$ | $2$ |
|:-:|:-:|:-:|:-:|
| $0$ | $1$ | $1$ | $0$ |
| $1$ | $1$ | $0$ | $1$ |
| $2$ | $1$ | $0$ | $0$ |

$$R=\{(0,0), (0, 1), (1, 0), (2, 0), (1, 2)\}$$

Check for each property:

* not reflexive since $\exists (1,1)\notin R$, whereas all $(a,a) \in R$ is required;
* not anti-reflexive since $\exists (0,0) \in R$, whereas all $(a, a) \notin R$ is required;
* not symmetric since $\exists (2,0) \in R$ and $\exists (0,2) \notin R$, whereas $\forall a \neq b, (a, b) \in R\colon (b, a) \in R$ is required;
* not anti-symmetric since $\exists (1,0), (0, 1) \in R$, whereas $\forall a \neq b, (a, b) \in R\colon (b, a) \notin R$ is required;
* not transitive since $\exists (0, 1), (1, 2) \in R$ and $(0, 2) \notin R$, whereas $\forall (a, b), (b, c) \in R\colon (a, c) \in R$ is required.

## Problem 3

How many antisymmetric non-transitive binary relations are there on the set of $\{1, 2, 3\}$?

---

Можно сделать перебор ручками, но я сделаю перебор питоном (комментарии прилагаются):

```
def is_antisymmetric(relation: list) -> bool:
    relation1 = relation.copy()

    # убираем пары (а, а), потому что они нерелевантны
    for t in range(1, 4):
        if (t, t) in relation1:
            relation1.remove((t, t))

    # проверяем, что условие антисимметричности выполнено для всех
    # для каждой пары (a, b) нет (b, a)
    if all(t[::-1] not in relation1 for t in relation1):
        return True
    
    return False

def is_transitive(relation: list) -> bool:
    # условие транзитивности: если (a, b) есть и при b = c (c, d) (b, d)
    # тоже есть, тогда (a, d) должно быть в отношении, иначе бан
    for a, b in relation:
        for c, d in relation:
            if b == c and ((a, d) not in relation):
                return False
            
    return True

def mask_array(array: list, mask: list) -> list:
    # просто функция бинарной маски
    result = []
    for i in range(len(array)):
        if mask[i]:
            result.append(array[i])
    
    return result

# генерируем все пары бинарного отношения {1, 2, 3}^2
relation_select = [(i, j) for i in range(1, 4) for j in range(1, 4)]
mask_length = len(relation_select)

counter = 0
for i in range(0, 2 ** mask_length):
    # перебор всех вариантов через бинарную маску
    mask = [char == "1" for char in bin(i)[2:].zfill(mask_length)]
    masked = mask_array(relation_select, mask)
    if not is_transitive(masked) and is_antisymmetric(masked):
        counter += 1
        print(masked)

print(counter)
```

---

```
[(2, 3), (3, 1)]
[(2, 3), (3, 1), (3, 3)]
[(2, 2), (2, 3), (3, 1)]
[(2, 2), (2, 3), (3, 1), (3, 3)]
[(2, 1), (3, 2)]
... [54 lines omitted]
[(1, 1), (1, 2), (2, 2), (3, 1), (3, 3)]
[(1, 1), (1, 2), (2, 2), (2, 3)]
[(1, 1), (1, 2), (2, 2), (2, 3), (3, 3)]
[(1, 1), (1, 2), (2, 2), (2, 3), (3, 1)]
[(1, 1), (1, 2), (2, 2), (2, 3), (3, 1), (3, 3)]
64
```

---

Okay, I actually came up with a better solution ($\overline{X}$ denotes an inverted bit in the table):

| | $1$ | $2$ | $3$ |
|:-:|:-:|:-:|:-:|
| $1$ | $X$ | $A$ | $B$ |
| $2$ | $\overline{A}$ | $X$ | $C$ |
| $3$ | $\overline{B}$ | $\overline{C}$ | $X$ |

$X$ are currently irrelevant, let's consider all relations that are transitive by assigning required values to $A, B, C$ and then we could add all combinations out of the set $\{(1,1),(2,2),(3,3)\}$ to the relation without affecting its transitivity or anti-symmetry. Using a binary mask, there would be $2^3$ such combinations, which we would need to later multiply by all valid relations dependent on $A, B, C$.

Find all anti-symmetric relations by filling the table above: for each pair $(A, \overline{A})$ there are three options that maintain antisymmetry: $(0, 0), (1, 0), (0, 1)$. Therefore, by applying a ternary mask, there would be $3^3=27$ such relations.

We know that an empty relation is transitive and relations consisting of a single element are transitive, thus removing $1+6$ possible relations. Now we need to check $20$ remaining ones, which is totally doable by hand:

```
[(3, 1), (3, 2)] - trans (no connections)
[(2, 3), (3, 1)] - non-trans (connection and only 2 elements)
[(2, 1), (3, 2)] - non-trans (connection and only 2 elements)
[(2, 1), (3, 1)] - trans (no connections)
[(2, 1), (3, 1), (3, 2)] - trans
[(2, 1), (2, 3)] - trans (no connections)
[(2, 1), (2, 3), (3, 1)] - trans
[(1, 3), (3, 2)] - non-trans (connection and only 2 elements)
[(1, 3), (2, 3)] - trans (no connections)
[(1, 3), (2, 1)] - non-trans (connection and only 2 elements)
[(1, 3), (2, 1), (3, 2)] - non-trans (lacking (1, 2), for instance)
[(1, 3), (2, 1), (2, 3)] - trans
[(1, 2), (3, 2)] - trans (no connections)
[(1, 2), (3, 1)] - non-trans (connection and only 2 elements)
[(1, 2), (3, 1), (3, 2)] - trans
[(1, 2), (2, 3)] - non-trans (connection and only 2 elements)
[(1, 2), (2, 3), (3, 1)] - non-trans (lacking (2, 1), for instance)
[(1, 2), (1, 3)] - trans (no connections)
[(1, 2), (1, 3), (3, 2)] - trans
[(1, 2), (1, 3), (2, 3)] - trans
```

There are $8$ non-transitive antisymmetric relations, and now we may add any of the $8$ subsets of $\{(1, 1), (2, 2), (3,3)\}$ to it, maintaining its non-transitivity and anti-symmetry, thus we get the final answer of $8 \times 8 = 64$.

**Answer:** $64$


## Problem 4

There are $2$ elements in a relation. How many elements could exist in its transitive closure?

---

Transitive closure $R^*$ always contains $R$, so at the least it may contain $2$ elements. 

For each ordered pair of different tuples in relation $R$, we need to add at max a single tuple (in case this tuple doesn't already exist). Therefore, the maximum number elements added to the transitive closure on the top of the already-existing $|R|$ elements will be equal to $|R|(|R|-1)$ (that's the number of pairs of tuples).

Therefore, $|R^*|\leq |R| + |R|(|R| - 1) = |R| + |R|^2 - |R|=|R|^2\Rightarrow|R^*|\leq |R|^2$

Thus, the cardinality of the transitive closure set may not be more than $|R|^2=2^2=4$.

Now, prove by example that each of the possibilities for $|R*|=2,3,4$ is possible:

* For $A = \{0,1\},R=\{(0, 0), (0, 1)\}$, $R^*=R=\{(0, 0), (0, 1)\}, |R^*|=2$
* For $A = \{0, 1, 2\},R=\{(0,1),(1,2)\}$, $R^*=\{(0,1),(1,2),(0,2)\}, |R^*|=3$
* For $A = \{0, 1\},R=\{(0,1),(1,0)\}$, $R^*=\{(0,0),(0,1),(1,0),(1,1)\}, |R^*|=4$

Thus, we get $|R^*|= 2, 3, 4$.

Answer: $2$, $3$, or $4$.