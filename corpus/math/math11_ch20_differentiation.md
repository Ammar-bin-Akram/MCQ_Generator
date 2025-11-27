# Chapter 20: Differentiation

## INTRODUCTION

The ancient Greeks knew the concepts of area, volume, centroids etc. which are related to integral calculus. Later on, in the seventeenth century, Sir Isaac Newton, an English mathematician ( 1642 - 1727) and Gottfried Whilhe G. W. Leibniz, a German mathematician, ( 1646 - 1716) considered the problem of instantaneous rates of change. They reached independently to the invention of differential calculus. After the development of calculus, mathematics became a powerful tool for dealing with rates of change and describing the physical universe.

### 13.1 Tangent to a Curve at a Point

Let $P(x, f(x))$ and $Q(x+\delta x, f(x+\delta x))$ be two points on arc $A B$ of graph of $f$ defined by the equation $y=f(x)$ as shown in Figure 13.1.
Where $\delta x$ is the increment in the value of $x$ (read as delta $x$ )
The line $P Q$ is secant of the curve and slope of
Figure 13.1
secant line passing through $P(x, f(x))$ and $Q(x+\delta x, f(x+\delta x))$ is:

$$
m_{\mathrm{am}}=\frac{R Q}{P R}=\frac{f(x+\delta x)-f(x)}{\delta x}
$$

Where $m_{\text {anc }}$ is slope of the secant line. Revolving the secant line $P Q$ towards $P$, some of its successive positions $P Q_{1}, P Q_{2}, P Q_{3}, \ldots$ are shown in the Figure 13.2. Points $Q_{i}(i=1,2,3, \ldots)$ are getting closer and closer to the point $P$ and $P R$ are approaching zero.
Figure 13.2

In other words, as $\delta x \rightarrow 0$, the point $Q$ approaches $P$, and the secant line becomes the tangent line. The revolving secant line becomes the tangent line $P T$ at $P$ while $\delta x$

approaches zero, that is,

$$
m_{\mathrm{ten}}=\operatorname{Lim}_{\delta x \rightarrow 0} \frac{f(x+\delta x)-f(x)}{\delta x}
$$

where $m_{\text {ten }}$ denotes the slope of tangent line. We see that $m_{\text {ten }}$ is the limit of $m_{\text {ten }}$ as $Q$ approaches $P$ along the curve $y=f(x)$.
Example 1 Find the gradient and an equation of tangent line to the graph of $f(x)=x^{2}-2$ at the point $P(-1,-1)$.
Solution To find the gradient or slope of the tangent line at point $(-1,-1)$, put $x=-1$ in equation (2)

$$
\begin{aligned}
m_{\text {ten }} & =\lim _{\delta x \rightarrow 0} \frac{f(-1+\delta x)-f(-1)}{\delta x} \\
& =\operatorname{Lim}_{\delta x \rightarrow 0} \frac{(-1+\delta x)^{2}-2-\left((-1)^{2}-2\right)}{\delta x} \\
& =\operatorname{Lim}_{\delta x \rightarrow 0} \frac{1-2 \delta x+\delta x^{2}-2-(1-2)}{\delta x} \\
& =\operatorname{Lim}_{\delta x \rightarrow 0} \frac{1-2 \delta x+\delta x^{2}-2+1}{\delta x}=\operatorname{Lim}_{\delta x \rightarrow 0} \frac{-2 \delta x+\delta x^{2}}{\delta x} \\
& =\operatorname{Lim}_{\delta x \rightarrow 0} \frac{\delta x(-2+\delta x)}{\delta x}=\operatorname{Lim}_{\delta x \rightarrow 0}(-2+\delta x)=-2
\end{aligned}
$$

Now to find the equation of tangent line we use the point slope form of equation of line with slope $=-2$ and point $(-1,-1)$
$y-(-1)=-2(x-(-1)) \Rightarrow y+1=-2 x-2$
or $y=-2 x-3$, which is the required equation of tangent line.
The graph of $f$ and tangent line are shown in the above figure.

# 13.2 Derivative as the Limit of a Difference Quotient

Let $f$ be a real valued function continuous in the interval $\left(x, x_{1}\right) \subseteq D_{f}$ (domain of $f$ ), then difference quotient $\frac{f\left(x_{1}\right)-f(x)}{x_{1}-x}$
represents the average rate of change in the value of $f$ with respect to the change $x_{1}-x$ in the value of independent variable $x$.

If $x_{1}$ approaches to $x$, then $\operatorname{Lim}_{x_{1} \rightarrow x} \frac{f\left(x_{1}\right)-f(x)}{x_{1}-x}$
provided this limit exists, is called the instantaneous rate of change of $f$ with respect to $x$ and is written as $f^{\prime}(x)$.
If $x_{1}=x+\delta x$ i.e., $x_{1}-x=\delta x$, then the expression (i) can be expressed as

$$
\frac{f(x+\delta x)-f(x)}{\delta x}
$$

and

$$
\operatorname{Lim}_{x_{x} \rightarrow 0} \frac{f(x+\delta x)-f(x)}{\delta x}
$$

(iii)
provided the limit exist, is defined to be the derivative of $f$ (or differential coefficient of $f$ ) with respect to $x$ and is denoted by $f^{\prime}(x)$ (read as " $f$-prime of $x^{\prime \prime}$ ). The domain of $f^{\prime}$ consists of all $x$ for which the limit exists. If $x \in D_{f}$ and $f^{\prime}(x)$ exists, then $f$ is said to be differentiable at $x$. The process of finding $f^{\prime}$ is called differentiation.

# 13.2.1 Derivative as the Rate of Change of Velocity

The rate of change is a fundamental concept in describing the motion of an object moving in a straight line. In physics, this is typically analyzed using position, velocity, and acceleration, which are all related through derivatives (rates of change).
The position versus time graph provides a simple interpretation of the average velocity over a given time interval.
Suppose a particle moves in a straight line and its position at time $t$ is given by the function $s(t)$. The average velocity over the interval from $t$ to $t_{1}$ denoted by $v_{\text {avg }}$ is defined as:

$$
v_{\text {ang }}=\frac{s\left(t_{1}\right)-s(t)}{t_{1}-t}
$$

Equation (i) also represents the slope of secant line passing through the points $(t, s(t))$ and $\left(t_{1}, s\left(t_{1}\right)\right)$. If the interval $t_{1}-t$ is not small, this average velocity does not accurately represent the rate of change at time $t$.
To illustrate this, consider a particle whose position at time $t$ (in seconds) is given by a function $s(t)=t^{2}+t$ in metres. The average rate of change over various time intervals

Starting at $t=3$ seconds is shown in the table below:

| Interval | $t=3$ secs to $t=5$ secs | $t=3$ secs to $t=4$ secs | $t=3$ secs to $t=3.5$ secs |
| :--: | :--: | :--: | :--: |
| Average velocity | $\begin{gathered} s(5)-s(3) \\ 5-3 \end{gathered}=\frac{30-12}{2}=9$ | $\begin{gathered} s(4)-s(3) \\ 4-3 \end{gathered}=\frac{20-12}{1}=8$ | $\begin{gathered} s(3.5)-s(3) \\ 3.5-3 \end{gathered}=\frac{63}{4}-12$ $0.5=7.5$ |
| | $\begin{gathered} 50 \\ 40 \\ 30 \\ 20 \\ 10 \end{gathered}$ | $\begin{gathered} 50 \\ 40 \\ 30 \\ 20 \\ 10 \end{gathered}$ | $\begin{gathered} 50 \\ 40 \\ 30 \\ 20 \\ 10 \end{gathered}$ |

We observe that these values are not closely approximate the particle's velocity at exactly 3 seconds. To obtain a better approximation of velocity at $x=3$, we use smaller intervals:

| Interval | Average velocity |
| :-- | :-- |
| $t=3$ secs to $t=3.1$ secs | $\begin{gathered} \frac{((3.1)^{2}+3.1)-12}{3.1-3}=\frac{0.71}{0.1}=7.1 \\ \hline \end{gathered}$ |
| $t=3$ secs to $t=3.01$ secs | $\begin{gathered} \frac{((3.01)^{2}+3.01)-12}{3.01-3}=\frac{0.0701}{0.01}=7.01 \\ \hline \end{gathered}$ |
| $t=3$ secs to $t=3.001$ secs | $\begin{gathered} \frac{((3.001)^{2}+3.001)-12}{3.001-3}=\frac{0.007001}{0.001}=7.001 \end{gathered}$ |

We see as the length of the time interval decreases, the average velocity becomes instantaneous velocity at $t=3$. Based on the trend, we estimate the instantaneous velocity to be approximately $7 \mathrm{~m} / \mathrm{sec}$.
Thus, over a sufficiently small interval, the velocity changes negligibly. If $t_{1}$ is very close to $t$, the average velocity over $t_{1}-t$ approximates the instantaneous velocity at $t$. As $t_{1}$ approaches $t$, the average velocity is called the instantaneous velocity.
This is similar to approximating the slope of a tangent line by calculating the slope of a secant line. Mathematically, the instantaneous velocity denoted by $v_{\text {inst }}$ is given by the following limit:

$$
v_{\text {inst }}=\operatorname{Lim}_{t_{1} \rightarrow t} \frac{s\left(t_{1}\right)-s(t)}{t_{1}-t} \quad \text { (Provide the limit exist) }
$$

For convenient, if $t_{1}=t+\delta t$, then as $t_{1} \rightarrow t \Rightarrow \delta t \rightarrow 0$, thus above equation becomes:

$$
v_{\text {inst }}=\operatorname{Lim}_{8 t \rightarrow 0} \frac{s(t+\delta t)-s(t)}{\delta t}
$$

In other words, the instantaneous velocity is the derivative of the position function $s(t)$ with respect to time.
Example 2 A particle moves along a line such that its position after $t$ hours is given by: $s(t)=4 t^{2}+2 t+1$ (in miles)
(a) Find the average velocity over the interval $[2,5]$
(b) Find the instantaneous velocity at $t=3$

Solution (a) given position function $s(t)=4 t^{2}+2 t+1$, where $2 \leq t \leq 5$
The average velocity over the interval $2 \leq t \leq 5$ is:

$$
\begin{aligned}
\text { Average velocity }=v_{\text {avg }} & =\frac{s(5)-s(2)}{5-2}=\frac{4(5)^{2}+2(5)+1-[4(2)^{2}+2(2)+1]}{3} \\
& =\frac{111-21}{3}=\frac{90}{3}=30 \mathrm{miles} / \mathrm{hours}
\end{aligned}
$$

(b) Instantaneous velocity can be found using the formula

$$
\begin{aligned}
& \text { Instantaneous velocity }=\lim _{\delta t \rightarrow 0} \frac{s(t+\delta t)-s(t)}{\delta t} \\
& =\lim _{\delta t \rightarrow 0} \frac{4(3+\delta t)^{2}+2(3+\delta t)+1-[4(3)^{2}+2(3)+1]}{\delta t} \\
& =\lim _{\delta t \rightarrow 0} \frac{4\left(9+6 \delta t+\delta t^{2}\right)+6+2 \delta t+1-43}{\delta t} \\
& =\lim _{\delta t \rightarrow 0} \frac{36+24 \delta t+4 \delta t^{2}+6+2 \delta t+1-43}{\delta t} \\
& =\lim _{\delta t \rightarrow 0} \frac{43+26 \delta t+4 \delta t^{2}-43}{\delta t}=\lim _{\delta t \rightarrow 0} \frac{26 \delta t+4 \delta t^{2}}{\delta t}
\end{aligned}
$$

$$
=\lim _{\delta t \rightarrow 0} \frac{\delta t(26+4 \delta t)}{\delta t}=\operatorname{Lim}_{t t \rightarrow 0}(26+4 \delta t)=26
$$

Thus, instantaneous velocity at $t=3$ is 26 miles/hour