## Problem 1

Let $E = E' = \mathbb{Z}$ with a metric of $d(x, y) :=|x-y|$. Would mapping $f: E \mapsto E', f(n)=n$ be continuous?

---

For a mapping to be continuous, for each $x_0\in E$, for all neighbourhoods (balls) $B'(x_0, r)$ of a point $f(x_0)\in E'$, there should exist such $B(x_0, r)\in E$ that $f(B(x_0, r))\subseteq B'(f(x_0), r)$.

Since $\forall n \in \mathbb{Z}, n \mapsto n$ and $\forall x, y \in \mathbb{Z}, d(x, y) \in \mathbb{Z}$, which is the metric space we are working in, then any ball in the original space would be mapped to the same place on the same point as it was beforehand. Effectively, nothing changes.

> *Technically, I could prove this more carefully, but I mean, literally nothing changes, all points get mapped to the same points and even the original space is a continuum, so I don't think it's necessary.*

---

Answer: yes, it would be continuous

## Problem 2

Using only the definition of a continuous mapping, show that $f: \mathbb{R} \mapsto \mathbb{R}$,

$$f(x):=\begin{cases}x, \ \ \ \ \ x \geq 0, \\ -1, \ \ x < 0\end{cases}$$

is not continuous in point $x_0 = 0$. What distance function should be introduced (and where?) for it to be continuous? (Or is it even possible?)

---

According to the definition, $f: E \mapsto E'$ is continuous if for each $x_0\in E$, for all neighbourhoods (balls) $B'(x_0, r)$ of a point $f(x_0)\in E'$ exists such $B(x_0, r)\in E$ that $f(B(x_0, r))\subseteq B'(f(x_0), r)$. Since we need to prove the opposite, find a counterexample.

For some $r > 0$, the ball $B(x_0, r)$ around $x_0 = 0$ would be an interval of $B(0,r)=(-r,r)$. Assume that $r=0.5$. Then, $B(0, 0.5)$ before the mapping would include values that lie in the interval of $(-0.5, 0)$. All these values $\forall r > 0$ (not a single one can be found!) would get sent to $-1$ after the mapping takes place, thus excluding them from the ball $B(0, 0.5)$. Congratulations, we have found a counterexample, thus the mapping is not continuous in $x_0 = 0$, q. e. d.

---

If we want to try and make this mapping continuous, we could, for example, introduce a distance function in the metric space after the mapping takes place as follows: $d(x, y) = a$, where $a\in\mathbb{R}$. Thus, making the metric between any two values in the second space the same (for instance, this could be a non-weighted graph). 

This way, since the original metric space is continuous, then regardless of $r$ in the second space, all balls $B'(f(x_0),r)$ would include ALL $f(x)$ for any $x$. Therefore, any ball from the first metric space that contains any elements could be mapped to a ball that would contain ALL elements.

---

Answer: yes, it is possible if we introduce a constant distance function in the second metric space.


## Problem 3 

Using only the definition of a continuous mapping, show that $f: \mathbb{R}\mapsto\mathbb{R}, f(x) = x^2$ is continuous.

---

According to the definition, $f: E \mapsto E'$ is continuous if for each $x_0\in E$, for all neighbourhoods (balls) $B'(x_0, r)$ of a point $f(x_0)\in E'$ exists such $B(x_0, r)\in E$ that $f(B(x_0, r))\subseteq B'(f(x_0), r)$.

First of all, notice that cases when $x>0$ and $x<0$ are symmetric. So, it's enough to consider one of them. Afterwards, we will consider the point when $x=0$.

For $x>0$, take some arbitrary $x_0$. For any $B'(x_0, r)$, would it be possible to find some $B(x_0, r)$ that it would be included inside $B'(x_0, r)$ after the mapping takes place? Yes, some interval $(-r + x_0, x_0 + r)$ would always exist for any positive and for any negative original $x_0$, and we could always find a respective ball since all values, which are either always in $\mathbb{R}^+$ or $\mathbb{R}^-$ would be mapped to $\mathbb{R}^+$, by simply nudging $r$ until all values are included in the resulting ball.

As for $x_0=0, \forall r>0$, all values from the interval $(0, r)$ would get mapped to $(0, r^2)$, and all values from the interval $(-r, 0)$ would get mapped to the same interval, $(0, (-r)^2)=(0, r^2)$. Therefore, values on either side of zero in the original number line would get mapped to values that lie in $\mathbb{R}^+$, and it would always be possible to nudge $r$ to include all values from the original ball, q. e. d.


## Problem 4 

Show that the following mappings $f: \mathbb{R}^2 \mapsto \mathbb{R}$ are continuous:

### Subproblem A

$$f(x,y)=x-2y$$

---

Technically, we could notice that the transformation is linear since all we did is scale $y$ by $-2$, then find the sum of $x$ and $-2y$, and then collapse all $y\neq 0$ from the original space to $\mathbb{R}$. The image of the mapping would be $\mathbb{R}$, and we can always find some open ball $B'(x_0, r)$, which would be some interval $(-r + x_0, x_0 + r)$, the preimage of which would be some $(-r_1 + x_0, x_0 + r_1)$. 

Since we are working in $\mathbb{R}^2$ and $\mathbb{R}$ respectively, we could linearly shift all open balls before the mapping using two linear transformations to $(x, y) = (0, 0)$ and similarly using a single linear transformation for all balls after the mapping. Then, we could infinitely increase/decrease the radius of the open ball, and it would maintain its openness since we are working with the entirety of $\mathbb{R}$.

Two intervals from the original set: $(-\delta_1 + x_0, x_0 + \delta_1)$ and $(-\delta_2 + y_0, y_0 + \delta_2)$ that form a two-dimensional ball would get collapsed to a one-dimensional ball that would be described by an interval of $(-\delta_1 + 2\delta_2 + x_0 - 2y_0, x_0 - 2y_0 + \delta_1 - 2\delta_2)$, which is obviously an open ball $B(x_0-2y_0, \delta_1 - 2\delta_2)$. For every open ball after the mapping, its preimage is an open ball, q. e. d. 

### Subproblem B

$$f:\mathbb{R}^2\setminus\{y=0\}\mapsto \mathbb{R}, f(x,y)=\frac{x}{y}$$

---

Similarly to subproblem A, use similar logic to arrive at the interval $\left(\frac{-\delta_1+x_0}{-\delta_2+y_0}, \frac{x_0+\delta_1}{y_0+\delta_2}\right)$ (or $\left(\frac{x_0+\delta_1}{y_0+\delta_2}, \frac{-\delta_1+x_0}{-\delta_2+y_0}\right)$, depending on $\delta_1, \delta_2$). Can we always nudge this interval by changing the deltas so that the preimage of the open ball defined by this interval be open? Seemingly, yes, since the numerator is positive and changing the delta scales the ball by some factor and nudging the delta in the denominator inversely scales the ball. 

In other words, is it possible that the preimage somehow would require a value to be $y=0$? Since by nudging $\delta_2$ in such a way that $y_0 = \plusmn\delta_2$, we may end up with an undefined bound for the interval, we need to come up with a different approach.

Define a new mapping from the one, the only, the legendary affine line with double origin to the extended number line as follows:

$$g: \mathbb{R}^2 \setminus \{y = 0\} \cup \{y=0^+,0^-\} \mapsto \overline{\mathbb{R}},g(x,y)=\begin{cases}\frac{x}{y}, y \neq 0,\\-\infty, y = 0^-,\\+\infty, y=0^+\end{cases}$$

And what do we see, this way, considering that the $y=0=0^+=0^-$, the ill-fated $y=0$ cannot physically be part of the preimage since it would require to somehow include unreachable points of $-\infty$ or $+\infty$, which is impossible to reach simply by extending deltas in an open ball. Therefore, all preimages of balls after the mapping would remain open since the only ball that breaks continuity in $R^2 \setminus \{y=0\}$ would be centered on $y=0$ and it is unreachable, q. e. d.

### Subproblem C

$$f(x,y):=\max\{x,y\}$$

---

Let's redefine the function as follows:

$$f(x,y)=\begin{cases}x, x > y,\\\alpha,\alpha=x=y,\\y, x < y\end{cases}$$

If we ignore restrictions for a moment, then, obviously, mappings ${x \choose y}\mapsto x$ and ${x\choose y}\mapsto y$ would be rotationally symmetric as we effectively collapse the other coordinate to zero to end up in $\mathbb{R}^1$ from $\mathbb{R}^2$, and those mapping are continuous since $\mathbb{R}$ is a continuum.

Now, consider the restrictions and look how the border between them behaves. Since $\alpha=x=y$, then nudging $\alpha$ by some $\delta$ would symmetrically apply to either coordinate. 

If we take some ball $B'(\alpha, \delta)$ after the mapping has taken place, then the balls in the preimage would be balls $B\left({x\choose y}, \delta\right)$, composed of two one-dimensional balls $B(x, \delta), B(y, \delta)$ and they both would map to the same ball. Similarly, we could find the preimage for any ball $B'$ for any $\alpha, \delta$. Therefore, the mapping is continuous, q. e. d.

## Problem 5

Find image of a mapping $f: \mathbb{R}^2 \mapsto \mathbb{R}^2$, where

### Subproblem A

$$f: {x \choose y} \mapsto {x + y \choose x^2 + y}$$

---

Visualizing how the mapping would unfold, we get a sector bounded by typical parabolas $y=x^2$, origins of which lie on the $y=x$ line. This makes perfect sense since the mapping transforms our values as follows: 

For $x \mapsto x + y$, the value remains the same but gets shifted by a certain linear constant. For $y \mapsto x^2 + y$, the value remains the same but gets shifted by a certain quadratic constant.

Using a geometric approach, we may find a tangent line to $y=x^2$, which would divide $\mathbb{R}^2$ into two sectors, and the values on the line or above would be the image of the aforementioned mapping. To find the tangent, find some $y = x + b$ that would have a single intersection point with $y = x^2$:

$$x + b = x^2 \Rightarrow x^2 - x - b = 0$$

$x^2 - x - b = 0$ would have one root if $b=-\frac{1}{4}$.

Therefore, the required sector is defined by the $y\geq x -\frac{1}{4}$ inequation. Thus, for any $x$, $\inf y=x-\frac{1}{4}$. Since we physically cannot reach points below, we may add a certain non-negative constant to each coordinate to get the final image of the mapping, redefining $x=a$ as the free variable in the meantime:

---

$$\text{Im}f=\left\{{a + r_1\choose a - \frac{1}{4} + r_2} \ \Big| \ \forall r_1, r_2 \in \mathbb{R_{\geq0}}, \forall a \in \mathbb{R}\right\}$$

---

### Subproblem B

$$f: {x \choose y}\mapsto {x\sin y\choose x\cos y}$$

---

It would be fair to notice that the notation $(x, y) = (r\sin\theta, r\cos\theta)$ is a radius-vector and a different way to define points in $\mathbb{R}^2$ in a radial coordinate system. Pretty cool, actually.

Effectively, the mapping just scales $x$ by a certain factor $\sin y \in (-1, 1)$ and replaces $y$ with a similar scaling of $x$ by another certain factor of $\cos y \in (-1, 1)$. Since $x,y\in\mathbb{R}$ and thus can be chosen out of infinitely many options, any point $\in \mathbb{R}$ is reachable this way.



Therefore,

$$\text{Im}f = \left\{{a \choose b} \ | \  \forall a, b \in \mathbb{R}\right\}$$

In other words,

---

$$\text{Im}f = \mathbb{R}^2$$