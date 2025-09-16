# Microeconomics 2, Homework 2-1

## Problem 1

There is a seller on the used cars market who is selling one car. The buyer knows that the car can be a "Peach", a "Banana", or a "Lemon" with probabilities specified in the table below. The table also summarizes the buyer's and the seller's valuation for owning a car of any type. We are looking for equilibria where the seller and the buyer act as price-takers.

| Type | Probability | Buyer Value | Seller Value |
| :--: | :---------: | :---------: | :----------: |
| Lemon | $\frac{1}{2}$ | $8$ | $6$ |
| Banana | $\frac{1}{6}$ | $24$ | $14$ |
| Peach | $\frac{1}{3}$ | $30$ | $24$ |

### Subproblem A

Assume that the buyer and the seller are symmetrically uninformed about the true quality of the car (both know only the ex-ante distribution of types). Describe all equilibria.

---

Find the expected value for the buyer:

$$\mathbb{E}[w_b]=\frac{1}{2}\times8+\frac{1}{6}\times24+\frac{1}{3}\times30=4+4+10=18$$

and for the seller, respectively:

$$\mathbb{E}[w_s]=\frac{1}{2}\times6+\frac{1}{6}\times14+\frac{1}{3}\times24=3+\frac{7}{3}+8=\frac{40}{3}$$

To find prices $p$ at which all car types would be traded, we take the intersection of intervals at which both seller and buyer do not end up with a loss.

$$p\in[18,+\infty)\cap\left(-\infty,\frac{40}{3}\right]=\left[\frac{40}{3},18\right]$$

### Subproblem B

Assume that the seller knows the true quality of the car while the buyer does not. Describe all equilibria (i. e. what types of cars are traded and at what price).

---

Let's consider descending prices:

1. $p\in[15,+\infty)$ 

## Problem 2

Consider Spence's job marker signalling model with discrete education. There are two types of workers and two firms on the market. A worker can either have high productivity $H=8$, or low productivity $L=4$. The probability that a worker in population is of high productivity $\lambda=\frac{1}{4}$. The worker knows her productivity and chooses education $e\in\{0,1\}$, i.e., only two levels of education are possible. The firms observe $e$ — but not the productivity — and pay the worker her expected productivity from their viewpoint $w$. The payoff of the worker with productivity $\theta\in\{H, L\}$ is

$$w-\frac{64}{\theta^2}\cdot e$$

where $\frac{64}{\theta^2}$ is the cost of education $e=1$ for a worker with productivity $\theta$.

### Subproblem A

Describe all pooling equilibria of the model (there can be at most two, but do both exist?)

### Subproblem B

Describe all separating equilibria of the model (there are at most two as well, you need to verify that either type does not want to imitate the other type behaviour).

## Problem 3

Consider the model of countersignaling from the lecture. Assume that $\lambda_L=\lambda_M=\lambda_H=\frac{1}{3}$, $L=1,M=3,H=5$, $c(e,\theta)=(6-\theta)\cdot e$ and $\pi_H=0.8,\pi_L=0.2$. We are looking for a countersignaling equilibrium with $e^L=e^H=0$ and $e^M>0$.

### Subproblem A

What is the wage paid to a worker with observed education $e^M$?

### Subproblem B

Calculate wages $w_g$ and $w_b$ that are paid to a worker with education $e=0$ and observed signal "good"/"bad".

### Subproblem C

What are the expected utilities each type of worker gets in this countersignaling equilibrium?

### Subproblem D

What is the possible range for $\pi_M$ such that this countersignaling equilibrium exists?
