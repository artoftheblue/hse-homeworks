# Теория меры

## Занятие 1

```{prf:definition}
Прямоугольник $P:=\{(x,y): a <x < b, c < y< d\}$

Его площадь $\mu(P):=(b-a)(d-c)$

Множество всех прямоугольников $\mathfrak{S}$.

$P_1\cap P_2=\varnothing$

$\mu(P_1\cup P_2)=\mu(P_1)+\mu(P_2)$
```

$\mu\colon\mathfrak{S}\to\mathbb{R}$

1. $\mu(P)\leq 0$
2. Если все $P_i$ попарно не пересекаются, то

$$\mu\left(\bigcup_{i=1}^n P_i\right)=\sum^n_{i=1}\mu(P_i)$$

```{seealso}
Докажите самостоятельно:
$$\mu(P_1\cup P_2)=\mu(P_1)+\mu(P_2)-\mu(P_1\cap P_2)$$
```

```{prf:definition}
Элементарное множество это множество на $\mathbb{R}^2$, которое можно представить хотя бы одним способом как объединение конечного числа попарно непересекающихся прямоугольников.
```

$$A\triangle B=(A\setminus B)\cup (B\setminus A)=(A\cup B)\setminus (A\cap B)$$

```{prf:theorem}
$A, B$ — элементарные множества, $\implies A\cup B, A\cap B, A\setminus B, A\triangle B$ — тоже элементарные
```

```{prf:proof}
:nonumber:
$P_1,P_2\in\mathfrak{S}\implies P_1\cap P_2\in\mathfrak{S}$

$$A=\bigcup^n_{i=1} =P_i, \quad B=\bigcup^m_{j=1} Q_j$$

$$A\cap B:=\left(\bigcup^n_{i=1}P_i\right)\cap\left(\bigcup^m_{j=1}Q_j\right)=\bigcup^n_{i=1}\bigcup^m_{j=1}(P_i\cap Q_j)$$

:::{note}
$$\bigcup^n_{i=1}P_i=P_1\cup P_2\cup P_3\cup\ldots\cup P_n$$
:::

$P_1\setminus P_2$ — элементарное множество

---

$Q$ — прямоугольник, $A=\displaystyle=\bigcup^\infty_{i=1}P_i$

$$Q\setminus A=Q\setminus\bigcup^n_{i=1}P_i=\cap^n_{i=1}(Q\setminus P_i)$$

где $Q\setminus P_i$ — элементарное множество $\implies$ мы опять получили элементарное множество.

$$A\cup B=P\setminus((P\setminus A)\cap (P\setminus B))$$

$A, B$ — два элементарных множества. 

$$\exists P\supset A, B$$

$$A\triangle B=(A\cup B)\setminus (A\cap B)$$

$B=\cup Q_j, A$ — элементарны

$B\setminus A=\bigcup(Q_i\setminus A)$
```

$X$ — множество, $X\neq\varnothing$

$2^X$ — множество всех подмножеств множества $X$

$\chi_A\colon X\mapsto \{0, 1\}$

$\chi_A(x)=\begin{cases}
    1, & x\in A\\
    0, & x\not\in A
\end{cases}$

$$\left\{\text{множество всех подмножеств в } X \right\}\leftrightarrow\{\text{все функции } X\mapsto \{0, 1\}\}$$

$A, B\subset X$

$\chi_{A\cap B}=\chi_A\cdot\chi_B$

$\chi_{A\cap B}=\begin{cases}
    1, x\in A\cap B\implies x\in A, x\in B, (\chi_A(x)=1,\chi_B(x)=1)\\
    0, x\not\in A\cap B\implies x\not\in A, x\in B, (\chi_A(x)=0,\chi_B(x)=1)\
\end{cases}$

1. $\boxed{\chi_{A\cap B}=\chi_A\cdot\chi_B}$
2. $\chi_{A\triangle B}=(\chi_A+\chi_B)\mod 2$

---

$\chi_A\cdot(\chi_B+\chi_C)=\chi_A\chi_B+\chi_A\chi_C$

т. е. $\{\chi_A,A\in 2^x\}$ образует кольцо

$$\boxed{\int x_a:=\mu(A)}$$

```{prf:definition}
Кольцо — непустое множество $R$, на котором введены две бинарные операции: $(+, \cdot)\colon R\times R\mapsto R$

1. $a+(b+c)=(a+b)+c$
2. $a+b = b+c$
3. $\exists\textbf{0}\in R:\textbf{0}+\textbf{0}=\textbf{0}$
4. $\forall a\in R, \exists (-a)\in R\colon a+(-a)=0$
5. $a\cdot(b+c)=a\cdot b+b\cdot c$
6. $(a+c)\cdot c=a\cdot c + b\cdot c$

---

7. $\exists 1$
8. $a\cdot b = b\cdot a$
9. $a\cdot(b\cdot c)=(a\cdot b)\cdot c$
```

## Занятие 2
