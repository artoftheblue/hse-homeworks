# Первое домашнее задание

### 1. Генератор случайных полезностей (15 баллов)

Василий нашёл некоторую таинственную машину, которая для любых двух заданных Василием благ генерировала функцию полезности, описывающую его предпочтения таким образом, будто других благ не существует в мире. Для некоторых товаров он получил следующие функции полезности:

* $U(x,y) = 42 + x^2 + y$;
* $U(x,y) = \min\{x+2y; x^2\}$;
* $U(x,y) = (3x-7)/4$.
  
Для всех пар товаров скажите, являются ли предпочтения выпуклыми. Проиллюстрируйте графически. 

---

Let's interpret how the first function looks. It looks like an $x^2$ parabola mounted on an $z=y$ graph in the three-dimensional plane shifted by $42$ utility units up. 

Since as $y$ increases, the same level of utility is reached by utilizing less and less $x$, it is pretty obvious that contour lines would slowly arc inwards toward the $y$-axis, compared to the perpendicular to $x$-axis lines (since the function does not depend on $y$) when the utility function is $U(x,y)=x^2+\text{const}$.

> Onwards, upper contour sets are shown as graph paper, and lower contour sets are shown as grey. Contour lines are red.  

Contour lines for $U(x,y)=x^2+42$:

![alt text](image-1.png)

Contour lines for $U(x,y)=x^2+y+42$:

![alt text](image-2.png)

As we may see from the figure above, $L^+$ is not convex, which implies **preferences are not convex.**

Three-dimensional plot for the sake of visualization:

![alt text](image-3.png)

---

We have already seen in the previous task how $U(x,y)=x^2+\text{const}$ looks, so let's graph $U(x,y)x+2y$:

> In the figure it's not black; it's just a very shadow-y grey.

![alt text](image-5.png)

and take the minimum of them to get $U(x,y) = \min\{x+2y; x^2\}$.

![alt text](image-4.png)

Joining two straight contour linessi (which have convex upper contour sets) using a $\min$ function maintains convexities of upper contour sets. This is further backed by the figure above, where the set is clearly convex since all chords between any two points from the contour line would lie within the upper contour set. Therefore, **these preferences are convex.**

Three-dimensional plot for the sake of visualization:

![alt text](image-7.png)

---

This function is perhaps the simplest of all: $U(x,y) = (3x-7)/4$. We just have a linear function that only depends on $x$, which obviously means that **the preferences are convex** since it's linear and it depends on a single variable and as it could be seen below, $L^+(x,y)$ is convex.

![alt text](image-6.png)

Three-dimensional plot once again:

![alt text](image-8.png)

###  2. Что если? (15 баллов)

Что если полезность агента имеет вид $U(x,y) = 10-5x^2 + 42x + y$, цена товара $x$ равна 17, цена товара $y$ равна 1, как тогда зависит потребляемое количества $x$ от дохода $W > 0$? А потребляемое количество $y$?

---

The budget limitation for prices $p=17,q=1$ would be $B(x,y)=17x+y-W\leq0$.

> On the graph, the budget limitation is denoted by blue.

Firstly, find the optimum of the function to figure out the point we have to consider. For this, find the Largangian of the function:

$$\mathcal{L}(x,y|\lambda)=U(x,y)-\lambda B(x,y)$$

$$\mathcal{L}(x,y|\lambda)=10-5x^2 + 42x + y-\lambda(17x+y-W)$$

Write out the first order conditions:

$$\begin{cases}
    \mathcal{L}_x'=0\\
    \mathcal{L}_y'=0\\
    \mathcal{L}_\lambda'=0
\end{cases}\implies\begin{cases}
    -10x+42-17\lambda=0\\
    1-\lambda=0\\
    17x+y-W=0
\end{cases}\implies$$

$$\begin{cases}
    x=\frac{5}{2}\\
    \lambda=1\\
    y=W-17x
\end{cases}\implies\begin{cases}
    x=\frac{5}{2}\\
    \lambda=1\\
    y=W-\frac{85}{2}
\end{cases}$$

Visualizations:

![alt text](image-9.png)

All the optimum points (orange color) for some $W$ happen to lie on a straight line since $x=\text{const}=\frac{5}{2}$

![alt text](image-11.png)

We have already arrived at the solution by writing out $\mathcal{L}$, so the intake of $x$ is constant at $x=\displaystyle\frac{5}{2}$ and the intake of $y$ depends on the budget and is equal to $y=W-\displaystyle\frac{85}{2}$.

![alt text](image-12.png)

However, what would happen if our budget $W$ would not allow us to buy $\displaystyle\frac{5}{2}$ units of good $x$? Then, we would just buy a bit less than that, as shown by the graph below:

![alt text](image-13.png)

Therefore, the final correlation between $W, x, y$ would be:

$$\begin{cases}
    x=\min\left\{\displaystyle\frac{W}{17},\frac{5}{2}\right\}\\
    y=W-x
\end{cases}$$

###  3. Какие-то мармышки (20 баллов)

Известно, что Паша потребляет только два товара мармеладных мишек ($x$) и рыбу ($y$), на которые ежемесячно Паша тратит 10 000 рублей. Он может покупать их возле дома по ценам 100 и 400 за единицу или на оптовой базе по ценам 100 и 150 рублей. Но ему нужно потратить 4000 рублей для того, чтобы добраться до оптовой базы и вернуться домой. Зато на оптовой базе он может получить 5 единиц мармеладных мишек бесплатно для дегустации. 

1. Изобразите бюджетное ограничение Паши. Запишите уравнение бюджетной линии. 
2. Пусть предпочтения Паши описываются функцией полезности $U(x,y) = x^{\alpha} y^{\beta}$, $\alpha, \beta \in (0;1)$. Найдите оптимальный набор для Паши. 
3. Пусть предпочтения Паши описываются функцией полезности $U(x,y) = x^2 +  y^2$. Найдите оптимальный набор для Паши в этом случае. 

---

#### First limitation for $U(x,y) = x^{\alpha} y^{\beta}$

Budget limitation **at home** based on budget $W=10\,000$, prices $p=100$ and $q=400$ is $B(x,y)=100x+400y-10\,000\leq0$.

Corresponding graph:

![alt text](image-14.png)

Let's logarithmically transform the Cobb-Douglas utility function to get $U(x,y)=x^{\alpha} y^{\beta}\sim \overset{\sim}{U}(x,y) = \alpha\log x + \beta\log y$.

Write out the Lagrangian and the first order conditions to find the optimal point:

$$\mathcal{L}(x,y|\lambda)=\alpha\log x + \beta\log y-\lambda(100x+400y-10\,000)$$

$$\begin{cases}
    \mathcal{L}_x'=0\\
    \mathcal{L}_y'=0\\
    \mathcal{L}_\lambda'=0
\end{cases}\implies\begin{cases}
    \frac{\alpha}{x}-100\lambda=0\\
    \frac{\beta}{y}-400\lambda=0\\
    100x+400y-10\,000=0
\end{cases}\implies$$

$$\begin{cases}
    \alpha = 100\lambda x\\
    \beta = 400\lambda y\\
    x + 4y=100
\end{cases}\implies\begin{cases}
    \alpha + \beta=10000\lambda\\
    \beta = 400\lambda y\\
    x=100-4y
\end{cases}\implies\begin{cases}
    \lambda=\frac{\alpha + \beta}{10000}\\
    y=\frac{25\beta}{\alpha + \beta}\\
    x=\frac{100\alpha}{\alpha + \beta}
\end{cases}$$

The visualization is very typical and Cobb-Douglasesque.

![alt text](image-18.png)

Optimal set of goods is $\displaystyle x=\frac{100\alpha}{\alpha + \beta}, y=\frac{25\beta}{\alpha + \beta}$.

#### Second limitation for $U(x,y) = x^{\alpha} y^{\beta}$

Budget limitation **at the wholesale base** based on budget $W_1=10\,000-4\,000=6\,000$, prices $p_1=100$ and $q_1=150$, as well as $5$ extra gummy bears, is $B_1(x,y)=100\max\{0,x-5\}+150y-6000\leq0$. 

$U(x,y) = x^{\alpha} y^{\beta}\sim U(x,y) = \alpha\log x+\beta\log y$

Same-scale comparison as above:

![alt text](image-26.png)

Write out the Lagrangian and the first order conditions to find the optimal point when we decide to take $x\geq5$:

$$\mathcal{L}(x,y|\lambda)=\alpha\log x + \beta\log y-\lambda(100x+150y-6\,500)$$

$$\begin{cases}
    \mathcal{L}_x'=0\\
    \mathcal{L}_y'=0\\
    \mathcal{L}_\lambda'=0
\end{cases}\implies\begin{cases}
    \frac{\alpha}{x}-100\lambda=0\\
    \frac{\beta}{y}-150\lambda=0\\
    100x+150y-6\,500=0
\end{cases}\implies$$

$$\begin{cases}
    \alpha = 100\lambda x\\
    \beta = 150\lambda y\\
    2x + 3y=130
\end{cases}\implies\begin{cases}
    \alpha + \beta=6500\lambda\\
    \beta = 150\lambda y\\
    2x + 3y=130
\end{cases}\implies\begin{cases}
    \lambda=\frac{\alpha + \beta}{6500}\\
    x=\frac{65\alpha}{\alpha + \beta}\\
    y=\frac{130\beta}{3(\alpha + \beta)}\\
\end{cases}$$

Cobb-Douglasesque visualization similar to above:

![alt text](image-27.png)

Optimal set of goods for this scenario is $\displaystyle x=\frac{65\alpha}{\alpha + \beta},y=\frac{50\beta}{\alpha + \beta}$.

Plus, we need to additionally check the edge case for when the optimum scenario lies within the $x<5$ sector, which our solution doesn't yet account for.

$$\frac{65\alpha}{\alpha + \beta}<5\implies65\alpha<5\alpha+5\beta\implies12\alpha<\beta$$

This means that if $12\alpha<\beta$, then we take the option of $(x,y)=(5,40)$

#### Optimum for $U(x,y) = x^{\alpha} y^{\beta}$

Now compare utilities for the first case and for the second case:

$$(x,y)_1=\left(\frac{100\alpha}{\alpha + \beta},\frac{25\beta}{\alpha + \beta}\right)$$

$$(x,y)_2=\left(\frac{65\alpha}{\alpha + \beta},\frac{130\beta}{3(\alpha + \beta)}\right)$$

$$U_1(x,y)>U_2(x,y)$$

$$\frac{100^\alpha\alpha^\alpha}{(\alpha + \beta)^\alpha}\frac{25^\beta\beta^\beta}{(\alpha + \beta)^\beta}>\frac{65^\alpha\alpha^\alpha}{(\alpha + \beta)^\alpha}\frac{\frac{130}{3}^\beta\beta^\beta}{(\alpha + \beta)^\beta}$$

$$100^\alpha\alpha^\alpha25^\beta\beta^\beta>65^\alpha\alpha^\alpha\frac{130}{3}^\beta\beta^\beta$$

$$\frac{100^\alpha\alpha^\alpha25^\beta\beta^\beta}{65^\alpha\alpha^\alpha\frac{130}{3}^\beta\beta^\beta}>1$$

Considering that $\alpha=\gamma\beta$:

$$\frac{100^{\beta\gamma}25^\beta}{65^{\beta\gamma}\frac{130}{3}^\beta}>1$$

$$\frac{100^{\gamma}\cdot 5}{65^{\gamma}\cdot\frac{26}{3}}>1$$

We get

$$\gamma=\frac{\log(2)-\log(3)-\log(5)+\log(13)}{2\log(2)+\log(5)-\log(13)}$$

> I extensively checked this in desmos, so if this is not right, I am going to literally explode.

Visualization for these conditions whenever utility graphs are the same and yield the very same utility value.

![alt text](image-28.png)

Visualization when the first option (red) is preferable:

![alt text](image-29.png)

When the second option (purple) is preferable:

![alt text](image-30.png)

Therefore, the final answer to this monstrosity:

$$\begin{cases}
    (x,y)_0=(5,40),\quad \alpha<\displaystyle\frac{\beta}{12}\\\\
    (x,y)_1=\displaystyle\left(\frac{100\alpha}{\alpha + \beta},\frac{25\beta}{\alpha + \beta}\right),\quad \alpha<\gamma\beta\\\\
    (x,y)_2=\displaystyle\left(\frac{65\alpha}{\alpha + \beta},\frac{130\beta}{3(\alpha + \beta)}\right),\quad\alpha\geq\gamma\beta\\\\
    \gamma=\displaystyle\frac{\log(2)-\log(3)-\log(5)+\log(13)}{2\log(2)+\log(5)-\log(13)}\approx1.27685271716\dots\\
\end{cases}$$

---

#### First limitation for $U(x,y) = x^2 + y^2$

Utility function and budget limitation for this case, similarly as above:

$$U(x,y) = x^2 + y^2$$

$$B(x,y)=100x+400y-10\,000\leq0$$

Since $U(x,y)=x^2+y^2$ is a convex utility function, the sought out optimal option would be to simply buy as much of the cheapest good as possible:

![alt text](image-25.png)

We are able to afford $x=\frac{10000}{100}=100$ gummy bear units, which is our optimal choice, and which gives us $x^2=100^2=10000$ utility units:

$$(x,y)=(100,0)$$

#### Second limitation for $U(x,y) = x^2 + y^2$

Utility function and budget limitation for this case, similarly as above:

$$U(x,y) = x^2 + y^2$$

$$B_1(x,y)=100x+150y-6000\leq0$$

For the same reasons as above, we strive to buy as much of the cheapest good as possible:

![alt text](image-23.png)

We are able to afford $x=\frac{6000}{100}=60$ gummy bear units, which is our optimal choice, and which gives us $60^2=3600$ utility units:

$$(x,y)=(60, 0)$$

#### Optimum for $U(x,y) = x^2 + y^2$

The first option gives us more utility, so **the preffered variant is to stay at home and stuff thyself up with gummy bears until you get diabetes: $(x,y)=(100,0)$**

###  4. Вот такие пироги (20 баллов)

Оксана закупает пироги для одного научного мероприятия. Её функция полезности $U(x,y) = 100 - (x-5)^2 - (y-3)^2$, где $x$ — пироги с яйцом,  $y$ — пироги с луком. Запишите функции спроса Оксаны на пироги. Как эти функции зависят от дохода и цен? Являются ли товары субститутами или комплементами? Посчитайте ценовую эластичность спроса на пироги с яйцом. 

---

Let's solve the maximization problem for this utility function an a budget limitation of $B(x,y)=px+qy-W\leq0$:

$$\mathcal{L}(x,y|\lambda)=100-(x-5)^2-(y-3)^2-\lambda(px+qy-W)$$

$$\begin{cases}
    \mathcal{L}_x'=0\\
    \mathcal{L}_y'=0\\
    \mathcal{L}_\lambda'=0
\end{cases}\implies\begin{cases}
    -2(x-5)-\lambda p=0\\
    -2(y-3)-\lambda q=0\\
    px+qy-W=0
\end{cases}\implies$$

$$\begin{cases}
    -2x+10-\lambda p=0\\
    -2y+6-\lambda q=0\\
    px+qy-W=0
\end{cases}\implies\begin{cases}
    \lambda=\frac{10-2x}{p}\\
    \lambda=\frac{6-2y}{q}\\
    px+qy-W=0
\end{cases}\implies$$

Take a singular equation out of here:

$$\frac{10-2x}{p}=\frac{6-2y}{q}$$

$$\frac{5-x}{p}=\frac{3-y}{q}$$

$$x=5-(3-y)\frac{p}{q}$$

Now, since $\displaystyle y=\frac{W-px}{q}$

$$x=5-\left(3-\frac{W-px}{q}\right)\frac{p}{q}$$

$$q^2x=5q^2-3pq-Wp+p^2x$$

$$x^*=\frac{5q^2-3pq+Wp}{p^2+q^2}$$

And since $\displaystyle x=\frac{W-qx}{p}$

$$y=3-(5-x)\frac{q}{p}$$

$$y=3-\left(5-\frac{W-qx}{p}\right)\frac{q}{p}$$

$$p^2y=3p^2-5pq-Wq+q^2x$$

$$y^*=\frac{3p^2-5pq+Wq}{p^2+q^2}$$

Visualization for different cases:

![alt text](image-31.png)

![alt text](image-32.png)

And for the optimum specifically:

![alt text](image-33.png)

---

Are these goods complements or substitutes?

Find derivatives of each good to the price of the other good:

$$\frac{\partial x^*}{\partial q}=\frac{p(-3 p^2 + 10 p q + q (3 q - 2 W))}{(p^2 + q^2)^2}<0$$

Graph for $W=1$:

![alt text](image-34.png)

which means that the good $x$ is not a substitute nor a complement to good $y$, since the derivatives take such wildly different values for different $W$ 

For the second one:

$$\frac{\partial y^*}{\partial p}=\frac{q (5 p^2 + 6 p q - 5 q^2 - 2 p W)}{(p^2 + q^2)^2}<0$$

Graph for $W=1$:

![alt text](image-35.png)

which also means that the good $y$ is not a substitute nor a complement to good $x$, since the derivatives take such wildly different values for different $W$.

---

Price elasticity of pies with eggs: 

$$\varepsilon_{x^*p}=\frac{\partial x^*}{\partial p}\frac{p}{x^*}$$

$$x^*=\frac{5q^2-3pq+Wp}{p^2+q^2}$$

$$\frac{\partial x^*}{\partial p}=\frac{(-3q+W)(p^2+q^2)-2p(5q^2-3pq+Wp)}{(p^2+q^2)^2}$$

$$\varepsilon_{x^*p}=\frac{(-3q+W)(p^2+q^2)-2p(5q^2-3pq+Wp)}{(p^2+q^2)^2}\frac{p(p^2+q^2)}{5q^2-3pq+Wp}$$

$$\varepsilon_{x^*p}=-\frac{2p^2}{p^2+q^2}-\frac{5q^2}{-3pq+pW+5q^2}+1$$

###  5. Снеки для Ани (20 баллов)

Ниже приведены покупки снеков Аней в прошлом году с разбивкой по месяцам и с указанием цен в онлайн магазине Киоск. Считайте, что в других магазинах Аня не покупает снеки. Другие снеки она не потребляет. Считайте, что Аня рациональна и её предпочтения не меняются в течение года. 

| клиент | месяц | количество пачек сыра | количество пачек чипсов | цена пачки сыра | цена пачки чипсов | расходы |
|----------|----------|----------|----------|----------|----------|----------|
| Аня | Январь | 30 | 0 | 40 | 60 | 1200 |
| Аня | Февраль | 24 | 0 | 50 | 60 | 1200 | 
| Аня | Март | 12 | 8 | 60 | 60 | 1200 |
| Аня | Апрель | 3| 17 | 60 | 60 | 1200 |
| Аня | Май | 5 | 15 | 60 | 60 | 1200 | 
| Аня | Июнь | 13 | 7 | 60 | 60 | 1200 |
| Аня | Июль | 4 | 16 | 60 | 60 | 1200 | 
| Аня | Август | 0 | 20 | 70 | 60 | 1200 |
| Аня | Сентябрь | 0 | 20 | 75 | 60 | 1200 |
| Аня | Октябрь | 16 | 0 | 75 | 80 | 1200 |
| Аня | Ноябрь | 10 | 5 | 80 | 80 | 1200 | 
| Аня | Декабрь | 3 | 12 | 80 | 80 | 1200 | 

1. Запишите расходы Ани в каждом месяце. 
2. Используя здравый смысл, аргументируйте, являются ли данные снеки субститутами или комплементами? Можете ли вы найти этому подтверждение в данных для Ани? Объясните.
3. Какую из четырех полезностей (полезность Кобба-Дугласа, линейная, квазилинейная, леонтьевская) вы бы выбрали для описания предпочтений Ани? Объясните свой выбор и придумайте способ откалибровать её.
4. Для откалиброванной полезности найдите спрос Ани на сыр и чипсы. 

---

> Spendings were added to the table above

It's obvious that the items are substitutes since out of the budget of $1200$, Anya either got some arbitrary amount of each item whenever the prices for them were the same (here each item was equally useful to Anya), or fully **substituted** one item with the other if the price for any of the two items increased, which is clearly inferred from the data above.

I would take the plain simple linear utility since both items contribute to the utility function in equal amounts and Anya's preferences were always biased toward the cheaper item: 

$$U(x,y)=x+y$$

It also is proven by the fact than we do not have a preference towards any particular item whenever they both cost the same (I honestly don't know what's there to calibrate because everything is really obvious).

Let's take the budget limitation of $px+qy-1200\leq0$ and find the demand functions (it's effectively formalizing that has been said above):

$$\begin{cases}
    \begin{cases}
        x^*=\displaystyle\frac{1200}{p}\\
        y^*=0
    \end{cases}\qquad p < q\\
    \begin{cases}
        x^*=0\\
        y^*=\displaystyle\frac{1200}{q}
    \end{cases}\qquad p > q\\
    x^*=y^*=\displaystyle\frac{1200}{\alpha}\qquad p = q=\alpha
\end{cases}$$

###  6.  Кривые Энгеля (10 баллов)

Известно, что оптимальный выбор потребителя описывается соотношением $\frac{\sqrt{y}}{\sqrt{x}}$ = $\frac{p}{q}$. Угловых решений нет. 
1. Пусть цены $(p,q)$ = $(1,1)$, изобразите кривую Энгеля в координатах $(x,y)$. 
2. Можете ли вы сказать, являются ли товары нормальными? Аргуметируйте свой ответ.
3. Пусть цена на товар $x$ выросла на 100%, изобразите новую кривую Энгеля на графике со старой. 

---

Here we go:

![alt text](image-36.png)

Both goods are perfectly interchangeable since their ratio is identical to their prices at $p=q=1$: 

$$\frac{\sqrt{y}}{\sqrt{x}}=\frac{p}{q}\implies\frac{y}{x}=1\implies y=x$$

The goods **are normal** since the more budget we have, the higher the demand for each of good would be, and it's even in equal proportions.

If we were to increase the price of the first good by $100\%$, then

$$\frac{\sqrt{y}}{\sqrt{x}}=\frac{2p}{q}\implies\frac{y}{x}=4\implies y=4x$$

![alt text](image-37.png)

which means that now we want the good $y$ four times at much as we want $x$, but the goods still very much remain normal.