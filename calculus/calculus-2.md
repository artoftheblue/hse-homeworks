## Problem 1

### Subproblem A

Show that $\lim_{n\rightarrow\infty}\frac{n}{n+1}\neq 2$.

Let's suppose that $\lim_{n\rightarrow\infty}\frac{n}{n+1}=2$ and try to find a contradiction:

$$\lim_{n\rightarrow\infty}\frac{n}{n+1}=2\Rightarrow\lim_{n\rightarrow\infty}(\frac{n}{n+1}-2)=0\Rightarrow\lim_{n\rightarrow\infty}(\frac{(n + 1) - 1}{n+1}-2)=0\Rightarrow$$

$$\lim_{n\rightarrow\infty}(1 - \frac{1}{n+1}-2)=0\Rightarrow\lim_{n\rightarrow\infty}(-\frac{1}{n+1}-1)=0$$

Since $-\frac{1}{n+1} < 0$ and $-1 < 0$, then the sum of these components cannot physically be equal to $0$. Therefore, $\lim_{n\rightarrow\infty}\frac{n}{n+1}\neq 2$, q. e. d.

---

Afterwards, show that $\lim_{n\rightarrow\infty}\frac{n}{n+1}=1$. Similarly as above:

$$\lim_{n\rightarrow\infty}\left(1-\frac{1}{n+1} - 1\right)=\lim_{n\rightarrow\infty}\left(-\frac{1}{n+1}\right)$$

Therefore, as per the limit definition, $\forall\varepsilon >0, \exists N \in \mathbb{N} \colon \forall n > N, |x_n - x|<\varepsilon$. For any $\varepsilon$:

$$\left|-\frac{1}{n+1}\right|<\varepsilon\Rightarrow\frac{1}{n+1}<\varepsilon$$

Since $n + 1>n$, $\frac{1}{n+1}<\frac{1}{n}$:

$$\frac{1}{n+1}<\frac{1}{n}<\varepsilon$$

Now $\forall n > N$, we can find some $N=\left[\frac{1}{\varepsilon}\right]$, which means that $\forall n > N$, $\left| -\frac{1}{n+1}\right|<\varepsilon$, q. e. d.

--- 

Show after which number all elements of the sequence would fall into the $(0.99, 1.01)$ interval. In this interval, $\varepsilon = 0.01$. As per the equation above,

$$N=\left[\frac{1}{\varepsilon}\right]=\left[\frac{1}{0.01}\right]=100$$

Using Python for calculations, we may check that, truly, starting from the 100th element, all elements of the sequence fall within $\varepsilon$ of the limit:


```
98 0.98989898989899
99 0.99
100 0.9900990099009901
101 0.9901960784313726
102 0.9902912621359223
103 0.9903846153846154
104 0.9904761904761905
```

Answer: $100$

### Subproblem B

Assume sequence $\{x_n\}$, where $x_n=\frac{5n^2+10n-3}{8n^2+n+2}$. Show that $\lim_{n\rightarrow\infty}x_n\neq 0$.

Similarly as above, assume that $\lim_{n\rightarrow\infty}x_n=0$ and try to find such $\varepsilon$ for which there would not be a number after which an infinite number of elements would be less than $\varepsilon$.

Say that $\varepsilon = 0.5$, then $\left|\frac{5n^2+10n-3}{8n^2+n+2}\right|<0.5\Rightarrow-0.5<\frac{5n^2+10n-3}{8n^2+n+2}<0.5$.

Consider the rightmost part of the equation:

$$\frac{5n^2+10n-3}{8n^2+n+2}<\frac{1}{2}$$

$$10n^2+20n-6<8n^2+n+2$$

$$2n^2+19n-8<0$$

$$n \in \left(\left[-\frac{19}{4}-\frac{5\sqrt{17}}{4}\right],\left[-\frac{19}{4}+\frac{5\sqrt{17}}{4}\right]\right) \Rightarrow n \in \left[-9, 0\right],$$

which means that there are no $n \geq 1$, for which there would be a single element within $0.5$ range from $0 \Rightarrow$ $\lim_{n\rightarrow\infty}x_n\neq 0$, q. e. d.

---

Assume that $\lim_{n\rightarrow\infty}x_n=\frac{5}{8}$. Then,

$$\lim_{n\rightarrow\infty}\left(\frac{5n^2+10n-3}{8n^2+n+2}-\frac{5}{8}\right)=\lim_{n\rightarrow\infty}\left(\frac{40n^2+80n-24-40n^2-5n-10}{8(8n^2+n+2)}\right)=$$

$$=\lim_{n\rightarrow\infty}\left(\frac{75n-34}{8(8n^2+n+2)}\right)$$

Now, for all $\varepsilon$:

$$\frac{75n-34}{8(8n^2+n+2)}<\frac{75n}{8(8n^2+n+2)}<\frac{75n}{64n^2}=\frac{75}{64n}<\varepsilon$$

Therefore, $\forall n > N$:

$$N = \left[\frac{75}{64\varepsilon}\right]$$

It can be concluded that $\lim_{n\rightarrow\infty}x_n=\frac{5}{8}$, q. e. d.

### Subproblem C

Prove that $\lim_{n\rightarrow\infty}2^{\frac{n-1}{n^2}}=1$.

Similarly as above, assume:

$$\lim_{n\rightarrow\infty}\left(2^{\frac{n-1}{n^2}}-1\right)=0$$

Then, for all $\varepsilon$:

$$2^{\frac{n-1}{n^2}}-1<\varepsilon$$

Logarithmize:

$$2^{\frac{n-1}{n^2}}<2^{\log_2(\varepsilon+1)}\Rightarrow\frac{n-1}{n^2}<\log_2(\varepsilon+1)\Rightarrow$$

$$\frac{n-1}{n^2}<\frac{n}{n^2}=\frac{1}{n}<\log_2(\varepsilon+1)=\frac{\ln(\varepsilon+1)}{\ln2}\Rightarrow$$

$$\frac{1}{n}<\frac{\ln(\varepsilon+1)}{\ln2}\Rightarrow n>\frac{\ln 2}{\ln(\varepsilon+1)}\Rightarrow$$

$$n>\log_{\varepsilon+1}2$$

Logarithm base is always larger than $1$ and it would never be undefined since $\varepsilon>0$. Therefore, $\forall n > N$:

$$N=\left[\log_{\varepsilon+1}2\right]$$

As a result, $\lim_{n\rightarrow\infty}2^{\frac{n-1}{n^2}}=1$, q. e. d.

### Subproblem D

Prove that

$$\lim_{n\rightarrow\infty}\frac{6n^4+n^3+3}{2n^4-n+1}=3$$

Similarly as above,

$$\lim_{n\rightarrow\infty}\left(\frac{6n^4+n^3+3}{2n^4-n+1}-3\right)=\lim_{n\rightarrow\infty}\left(\frac{6n^4+n^3+3-6n^4+3n-3}{2n^4-n+1}\right)=$$

$$=\lim_{n\rightarrow\infty}\left(\frac{n^3+3n}{2n^4-n+1}\right)$$

Then, $\forall \varepsilon$:

$$\frac{n^3+3n}{2n^4-n+1}<\varepsilon$$

We need to estimate this equation somehow, for all $n \in \mathbb{N}$, assume some $k_1=5$:

$$n^3+3n < k_1n^3=5n^3\Rightarrow 4n^3-3n>0 \Rightarrow 4n(n^2-\frac{3}{4})>0,$$

which is always true. The following equation with $k_2=1$ would be true for $n = 1$ and onwards:

$$2n^4-n+1\geq n^4=k_2n^4$$

Therefore, the following estimation would be true:

$$\frac{n^3+3n}{2n^4-n+1}<\frac{5n^3}{n^4}=\frac{5}{n}<\varepsilon$$

And $\forall n > N$:

$$N=\left[\frac{5}{\varepsilon}\right]$$

In the end, $$\lim_{n\rightarrow\infty}\frac{6n^4+n^3+3}{2n^4-n+1}=3,$$

q. e. d.

## Problem 2

Calculate limits:

### Subproblem A

$$\lim_{n\rightarrow\infty}\frac{n!}{n^n}=\lim_{n\rightarrow\infty}\frac{1\times2\times3\times\dots\times (n - 2) \times (n - 1) \times n}{n\times n \times n \times \dots \times n \times n \times n}=$$

$$=\lim_{n\rightarrow\infty}\left(\frac{1}{n}\times\frac{2}{n}\times\frac{3}{n}\times\dots\times\frac{n-2}{n}\times\frac{n-1}{n}\times1\right)$$

Each (except for the last one) of the terms above is $< 1$. Therefore, the multiplication of all these elements will be less (for $n > 1$) than any (!) of the product components, so: 

$$0\leq\frac{n!}{n^n}\leq\frac{1}{n}$$

Since we know that $\lim_{n\rightarrow\infty}\frac{1}{n}=0$, then according to the squeeze principle:

$$\lim_{n\rightarrow\infty}0=\lim_{n\rightarrow\infty}\frac{n!}{n^n}=\lim_{n\rightarrow\infty}\frac{1}{n}=0$$

*Alternatively, just use limit arithmetic: since $\lim_{n\rightarrow\infty}\frac{1}{n}=0$, the entire limit is equal to $0$.*

Answer: $\lim_{n\rightarrow\infty}\frac{n!}{n^n}=0$

### Subproblem B

$$\lim_{n\rightarrow\infty}\sqrt[n^2]{n!}=\lim_{n\rightarrow\infty}\sqrt[n^2]{1}\sqrt[n^2]{2}\sqrt[n^2]{3}\dots\sqrt[n^2]{n}$$

From the binomial formula, we know that $\lim_{n\rightarrow\infty}\sqrt[n]{n}=1$. According the squeeze theorem once again,

$$1 \leq \sqrt[n^2]{n}\leq \sqrt[n]{n}$$

$$\lim_{n\rightarrow\infty}1=\lim_{n\rightarrow\infty}\sqrt[n^2]{n}=\lim_{n\rightarrow\infty}\sqrt[n]{n}=1$$

and $\forall k \in \mathbb{N}$:

$$1 \leq \sqrt[n^2]{k} \leq \sqrt[n]{k}$$

$$\lim_{n\rightarrow\infty}1=\lim_{n\rightarrow\infty}\sqrt[n^2]{k}=\lim_{n\rightarrow\infty}\sqrt[n]{k}=1$$

Limit of a multiplication is equal to the multiplication of limits, which are all defined and are equal to $1$. Therefore, $$\lim_{n\rightarrow\infty}\sqrt[n^2]{n!}=\lim_{n\rightarrow\infty}\sqrt[n^2]{1}\times\lim_{n\rightarrow\infty}\sqrt[n^2]{2}\times\lim_{n\rightarrow\infty}\sqrt[n^2]{3}\times\dots\times\lim_{n\rightarrow\infty}\sqrt[n^2]{n}=1\times1\times1\times\dots\times1=1$$

Answer: $\lim_{n\rightarrow\infty}\sqrt[n^2]{n!}=1$

### Subproblem C

$$\lim_{n\rightarrow\infty}\sqrt[n]{3^n+1}=\lim_{n\rightarrow\infty}3\sqrt[n]{1+\frac{1}{3^n}}$$

Looking a little bit closer, we can use the squeeze theorem (for $n \geq 5$, as it approaches $\infty$) to evaluate $\lim_{n\rightarrow\infty}\frac{1}{3^n}$:

$$0\leq\frac{1}{3^n}\leq\frac{1}{n!}$$

$$\lim_{n\rightarrow\infty}0=\lim_{n\rightarrow\infty}\frac{1}{3^n}=\lim_{n\rightarrow\infty}\frac{1}{n!}=0$$

Substitute the limit back into the original equation:

$$\lim_{n\rightarrow\infty}\sqrt[n]{3^n+1}=\lim_{n\rightarrow\infty}3\sqrt[n]{1+0}=3$$

Answer: $\lim_{n\rightarrow\infty}\sqrt[n]{3^n+1}=3$

### Subproblem D

$$\lim_{n\rightarrow\infty}\sqrt2\sqrt[4]{2}\sqrt[8]{2}\dots\sqrt[2^n]{2}=\lim_{n\rightarrow\infty}2^{\frac{1}{2}+\frac{1}{4}+\frac{1}{8}+\dots+\frac{1}{2^n}}$$

Notice that the exponent is almost equal to $1$ and for any finite $n$ it would evaluate to:

$$\frac{1}{2}+\frac{1}{4}+\frac{1}{8}+\dots+\frac{1}{2^n}=1-\frac{1}{2^n}$$

Therefore,

$$\lim_{n\rightarrow\infty}\sqrt2\sqrt[4]{2}\sqrt[8]{2}\dots\sqrt[2^n]{2}=\lim_{n\rightarrow\infty}2^{1-\frac{1}{2^n}}$$

Same as above, looking a little bit closer, we can use the squeeze theorem (for $n \geq 3$, as it approaches $\infty$) to evaluate $\lim_{n\rightarrow\infty}\frac{1}{2^n}$:

$$0\leq\frac{1}{2^n}\leq\frac{1}{n!}$$

$$\lim_{n\rightarrow\infty}0=\lim_{n\rightarrow\infty}\frac{1}{2^n}=\lim_{n\rightarrow\infty}\frac{1}{n!}=0$$

Because of this,

$$\lim_{n\rightarrow\infty}\sqrt2\sqrt[4]{2}\sqrt[8]{2}\dots\sqrt[2^n]{2}=\lim_{n\rightarrow\infty}2^{1-\frac{1}{2^n}}=\lim_{n\rightarrow\infty}2^{1-0}=2$$

Answer: $\lim_{n\rightarrow\infty}\sqrt2\sqrt[4]{2}\sqrt[8]{2}\dots\sqrt[2^n]{2}=2$