# Chapter 19: 12.3.3 Continuity of a Function at a Point

## (a) Continuous Function

A function $f$ is said to be continuous at a number " $c$ " if and only if the following three conditions are satisfied.
(i) $f(c)$ is defined
(ii) $\operatorname{Lim}_{x \rightarrow c} f(x)$ exists
(iii) $\operatorname{Lim}_{x \rightarrow c} f(x)=f(c)$
(b) Discontinuous Function

If one or more of these three conditions fail to hold at " $c$ ", then the function $f$ is said to be discontinuous at " $c$ ".

Example 10 Consider the function $f(x)=\frac{x^{2}-1}{x-1}$, discuss the continuity of $f$ at $x=1$.
Solution Here $f(1)$ is not defined.
$\Rightarrow f(x)$ is discontinuous at 1 .
Example 11 For $f(x)=3 x^{2}-5 x+4$, discuss continuity of $f$ at $x=1$.
Solution $\operatorname{Lim}_{x \rightarrow 1} f(x)=\operatorname{Lim}_{x \rightarrow 1}\left(3 x^{2}-5 x+4\right)=3-5+4=2$ and $f(1)=3-5+4=2$

$$
\Rightarrow \quad \operatorname{Lim}_{x \rightarrow 1} f(x)=f(1)
$$

Therefore, $f(x)$ is continuous at $x=1$
Example 12 Discuss the continuity of the functions $f(x)$ and $g(x)$ at $x=3$
(a) $f(x)=\left\{\begin{array}{ll}\frac{x^{2}-9}{x-3} & \text { if } \quad x \neq 3 \\ 6 & \text { if } \quad x=3\end{array}\right.$
(b) $g(x)=\left\{\frac{x^{2}-9}{x-3} \quad \text { if } \quad x \neq 3\right.$

Solution (a) $f(3)=6$
Now, $\operatorname{Lim}_{x \rightarrow 3} f(x)=\operatorname{Lim}_{x \rightarrow 3} \frac{x^{2}-9}{x-3}$

$$
\begin{aligned}
& =\operatorname{Lim}_{x \rightarrow 3} \frac{(x+3)(x-3)}{(x-3)} \\
& =\operatorname{Lim}_{x \rightarrow 3}(x+3)=3+3=6
\end{aligned}
$$

As $\quad \operatorname{Lim}_{x \rightarrow 3} f(x)=6=f(3)$
$f(x)$ is continuous at $x=3$. It is noted that there is no break in the graph.
Figure 12.5

(b) $g(x)=\frac{x^{2}-9}{x-3}$ if $x \neq 3$

As $g(x)$ is not defined at $x=3$
$\Rightarrow g(x)$ is discontinuous at $x=3$
It is noted that there is a break in the graph at $x=3$ near $x=3$ as shown in the Figure 12.6.
Example 13 Discuss continuity of $f(x)$ at $x=3$, when

$$
f(x)= \begin{cases}x-1, & \text { if } \quad x<3 \\ 2 x+1, & \text { if } \quad x \geq 3\end{cases}
$$

Solution A sketch of the graph of $f$ is shown in the Figure 12.7. We can see that there is a break in the graph at a point when $x=3$.

Now $f(3)=2(3)+1=7$
$\Rightarrow$ Condition (i) is satisfied.
$\operatorname{Lim}_{x \rightarrow 3} f(x)=\operatorname{Lim}_{x \rightarrow 3}(x-1)=3-1=2$
$\operatorname{Lim}_{x \rightarrow 3} f(x)=\operatorname{Lim}_{x \rightarrow 3}(2 x+1)=6+1=7$
$\operatorname{Lim}_{x \rightarrow 3} f(x) \neq \operatorname{Lim}_{x \rightarrow 3} f(x)$
i.e., condition (ii) is not satisfied.
$\therefore \quad \operatorname{Lim}_{x \rightarrow 3} f(x)$ does not exist.
Hence, $f(x)$ is not continuous at $x=3$
Figure 12.7

# EXERCISE 12.2

1. Determine the left hand limit and the right hand limit and then, find limit of the following functions when $x \rightarrow c$.
(i) $f(x)=2 x^{2}+x-5, c=1$
(ii) $f(x)=\frac{x^{2}-9}{x-3}, c=-3$
(iii) $f(x)=|x-5|, c=5$
2. Discuss the continuity of $f(x)$ at $x=c$
(i) $f(x)= \begin{cases}2 x+5 & \text { if } x \leq 2 \\ 4 x+1 & \text { if } x>2\end{cases}, c=2$
(ii) $f(x)= \begin{cases}3 x-1 & \text { if } x<1 \\ 4 & \text { if } x=1, c=1 \\ 2 x & \text { if } x>1\end{cases}$
3. If $f(x)= \begin{cases}3 x & \text { if } \quad x \leq-2 \\ x^{2}-1 & \text { if } \quad-2<x<2 \text { Discuss continuity at } x=2 \text { and } x=-2 \\ 3 & \text { if } x \geq 2\end{cases}$

4. If $f(x)=\left\{\begin{array}{cc}x+2 & x \leq-1 \\ c+2 & x>-1\end{array}\right.$
find " $c$ " so that $\operatorname{Lim}_{x \rightarrow-1} f(x)$ exists.
5. Find the values of $m$ and $n$, so that given function $f$ is continuous at $x=3$
(i) $f(x)=\left\{\begin{array}{cll}mx & \text { if } x<3 \\ n & \text { if } x=3 & \text { (ii) } f(x)=\{ \\ -2 x+9 & \text { if } & x>3\end{array}\right.$
(ii) $f(x)=\left\{\begin{array}{lll}mx & \text { if } x<3 \\ x^{2} & \text { if } x \geq 3\end{array}\right.$
6. $f(x)=\left\{\begin{array}{cll}\sqrt{2 x+5}-\sqrt{x+7} & , & x \neq 2 \\ k & , & x=2\end{array}\right.$

Find value of $k$ so that $f$ is continuous $x=2$.
7. Given the function $f(x)=\left\{\begin{array}{cc}2 x+3, & x \leq 1 \\ -x+4, & x>1\end{array}\right.$

Discuss the limit and continuity at $x=1$.

# 12.4 Application of Transcendental Functions to Limits and Continuity on Real World Problems

Limit and continuity of transcendental functions are fundamental concepts in calculus with numerous real-world applications.
These concepts help us model, analyze and solve problems in various fields such as growth and decay, finance, economics, surveying and predicting long-term stock prices.

## Example 14 Growth and Decay (Radioactive Decay)

The radioactive decay of a substance is given by the function $A(t)=A_{0} e^{-k t}$, where $A_{0}$ is the initial amount of the substance, $k$ is the decay constant, and $t$ is the time in years. Find the limit of the amount of substance as $t \rightarrow \infty$.

## We need to compute the limit: $\operatorname{Lim}_{t \rightarrow \infty} A(t)=\operatorname{Lim}_{t \rightarrow \infty} A_{0} e^{-k t}$
As $t \rightarrow \infty, e^{-k t} \rightarrow 0$, so $\operatorname{Lim}_{t \rightarrow \infty} A_{0} e^{-k t}=A_{0} \times 0=0$
Thus, the amount of radioactive substance approaches 0 as time increases indefinitely. Example 15 Finance (Compound Interest)
The value of an investment grows according to the formula for continuous compounding $A(t)=P_{0} e^{r t}$, where $P_{0}$ is the initial principal, $r$ is the annual interest rate, and $t$ is the time in years. What happens to the value of the investment as $t \rightarrow \infty$ ?

# Unit 42 Limit of Sequences and Conthority

Solution We need to compute the limit: $\operatorname{Lim}_{t \rightarrow \infty} A(t)=\operatorname{Lim}_{t \rightarrow \infty} P_{0} e^{r t}$
Since $e^{r t} \rightarrow \infty$ as $t \rightarrow \infty$ for any positive $r$, the value of the investment grows without bound:

$$
\operatorname{Lim}_{t \rightarrow \infty} P_{0} e^{r t}=\infty
$$

Thus, the value of the investment increases indefinitely as time approaches infinity.

## Example16 Economics (Supply and Demand)

In economics, the demand function $D(p)$ decreases as the price $p$ increases. Suppose the demand function is given by $D(p)=\frac{100}{p+1}$, where $p$ is the price in dollars. Find the limit of the demand as the price becomes very large, i.e., $\operatorname{Lim}_{p \rightarrow \infty} D(p)$ :

Solution $\operatorname{Lim}_{p \rightarrow \infty} D(p)=\operatorname{Lim}_{p \rightarrow \infty} \frac{100}{p+1}$
As $p \rightarrow \infty$, the denominator becomes very large, so $\operatorname{Lim}_{p \rightarrow \infty} \frac{100}{p+1}=0$
Thus, as the price becomes very large, the demand approaches 0 .

## Example17 Astronomy

The apparent brightness $B(d)$ of a star decreases as the distance from Earth increases following the inverse square law $B(d)=\frac{L}{d^{2}}$, where $L$ is the star's luminosity. Find the limit of the brightness as $d \rightarrow \infty$.

Solution $\quad \operatorname{Lim}_{d \rightarrow \infty} B(d)=\operatorname{Lim}_{d \rightarrow \infty} \frac{L}{d^{2}}$
As $d \rightarrow \infty$ the denominator becomes very large, so:

$$
\operatorname{Lim}_{d \rightarrow \infty} \frac{L}{d^{2}}=0
$$

Thus, as the distance increases indefinitely, the apparent brightness of the star approaches 0 .

## EXERCISE 12.3

1. A substance decays exponentially following the formula $A(t)=A_{0} e^{-0.1 t}$, where $A_{0}$ is the initial amount. Find the limit of $A(t)$ as $t \rightarrow \infty$.
2. A town's population is modeled by $P(t)=\frac{100,000}{1+9 e^{-0.5 t}}$. What is the long-term population as $t \rightarrow \infty$.

3. A company's weekly sales (in thousands) follow the function $S(t)=\frac{500 t}{t+10}$. What is the limit of $S(t)$ as $t \rightarrow \infty$ and what does it represent?
4. Signal strength $S(d)$ at a distance $d$ from a tower is modeled as $S(d)=\frac{1000}{d^{2}}$.
(i) What is the signal strength at $d=10$ ?
(ii) What happens to signal strength as $d \rightarrow \infty$ ?
5. A stock price grows according to the function $P(t)=50 \mathrm{e}^{0.05 t}$.
(i) Find the limit of $P(t)$ as $t \rightarrow \infty$.
(ii) Calculate the price after 10 years.
6. The factory's cost function is given as:

$$
C(x)= \begin{cases}10 x+500 & \text { if } \quad x \leq 100 \\ 12 x+300 & \text { if } \quad x>100\end{cases}
$$

Is the cost function continuous at $x=100$ ?
7. Inflation is modeled by $I(t)=I_{0} e^{0.05 t}$, where $I_{0}$ is the initial price index and $t$ is the number of years
(i) Find the inflation rate after 5 years if $I_{0}=100$.
(ii) What is the expected price index after 10 years?
8. The cost to produce $x$ units is:

$$
C(x)= \begin{cases}5 x+20 & \text { if } \quad x \leq 10 \\ 6 x+10 & \text { if } \quad x>10\end{cases}
$$

Is the cost function continuous at $x=10$ ?