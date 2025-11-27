# Chapter 1: DIFFERENTIATION

### 2.1 INTRODUCTION

The ancient Greeks knew the concepts of area, volume and centroids etc. which are related to integral calculus. Later on, in the seventeenth century, Sir Isaac Newton, an English mathematician (1642-1727) and Gottfried Whilhelm Leibniz, a German mathematician, (1646-1716) considered the problem of instantaneous rates of change. They reached independently to the invention of differential calculus. After the development of calculus, mathematics became a powerful tool for dealing with rates of change and describing the physical universe.

## Dependent and Independent Variables

In differential calculus, we mainly deal with the rate of change of a dependent variable with respect to one or more independent variables. Now, we first explain the terms dependent and independent variables.

We usually write $y=\sigma^{f}(x)$ where $f(x)$ is the value of $f$ at $x \quad D_{y}$ (the domain of the function $f$ ). Let us consider the functional relation $v=f(x)=x^{2}+1$ (A)

For different values of $x \in D_{y}, f(x)$ or the expression $x^{2}+1$ assumes different values. For example; if $x=1,1.5,2$ etc., then

$$ \begin{aligned} & f(1)=(1)^{2}+1=2, f(1.5)=(1.5)^{2}+1=2.25+1=3.25 \ & f(2)=(2)^{2}+1=4+1=5 \end{aligned} $$

We see that for the change $1.5-1=0.5$ in the value of $x$, the corresponding change in the value of $y$ or $f(x)$ is given by $f(1.5)-f(1)=3.25-2=1.25$ It is obvious that the change in the value of the expression $x^{2}+1$ (or $f(x)$ ) depends upon the change in the value of the variable $x$. As $x$ behaves independently, so we call it the independent variable. But the behaviour of $y$ or $f(x)$ depends on the variable $x$, so we call it the dependent variable.

The change in the value of $x$ (positive or negative) is called the increment of $x$ and is denoted by the symbol $\delta x$ (read as delta $x$ ). The corresponding change in the dependent variable $y$ or $f(x)$ for the change $\delta x$ in the value of $x$ is denoted by $\delta y$ or $\delta f=f(x+\delta x)-f(x)$. version: 1.1

Usually the small changes in the values of the variables are taken as increments of variables. Note: In this Chapter we shall discuss functions of the form $y=f(x)$ where $x=D_{y}$ and is called an independent variable while $x$ is called the dependent variable.

### 2.1.1 AVERAGE RATE OF CHANGE

Suppose a particle (or an object) is moving in a straight line and its positions (from some fixed point) after times $t$ and $t_{1}$ are given by $s(t)$ and $s\left(t_{1}\right)$, then the distance traveled in the time interval $t_{1}-t$ where $t_{1}>t$ is $s\left(t_{1}\right)-s(t)$ and the difference quotient $\frac{s\left(t_{1}\right)-s(t)}{t_{1}-t}$ (i) represents the average rate of change of distance over the time interval $t_{1}-t$. If $t_{1}-t$ is not small, then the average rate of change does not represent an accurate rate of change near $t$. We can elaborate this idea by a moving particle in a straight line whose position in metres after $t$ seconds is given by

$$ s(t)=t^{2}+t $$

We construct a table for different values of $t$ as under:

|  Interval | Average rate of change (i.e. average speed)  |
| --- | --- |
|  $t=3$ secs to $t=5$ secs | $\frac{s(5)-s(3)}{5-3}=\frac{(25+5)-(9+3)}{2}=\frac{30-12}{2}=9$  |
|  $t=3$ secs to $t=4$ secs | $\frac{s(4)-s(3)}{4-3}=\frac{(16+4)-12}{1}=\frac{20-12}{1}=8$  |
|  $t=3$ secs to $t=3.5$ secs | $\frac{s(3.5)-s(3)}{3.5-3}=\frac{\left(\frac{49}{4}+\frac{7}{2}\right)-12}{0.5}=\frac{\frac{15}{4}}{0.5}=7.5$  |

We see that none of average rates of change approximates to the actual speed of the particle after 3 seconds.

Now we construct a table by taking small intervals.

|  Interval | Average rate of change  |
| --- | --- |
|  $t=3$ secs to $t=3.1 \mathrm{secs}$ | $\frac{((3.1)^{2}+3.1)-12}{3.1-3}=\frac{12.71-12}{0.1}=\frac{0.71}{0.1}=7.1$  |
|  $t=3$ secs to $t=3.01 \mathrm{secs}$ | $\frac{((3.01)^{2}+3.01)-12}{3.01-3}=\frac{12.0701-12}{0.01}=\frac{0.0701}{0.01}=7.01$  |
|  $t=3$ secs to $t=3.001 \mathrm{secs}$ | $\frac{((3.001)^{2}+3.001)-12}{3.001-3}=\frac{12.007001-12}{0.001}=\frac{0.007001}{0.001}=7.001$  |

The above table shows that the average rate of change after 3 seconds approximates to 7 metre/sec. as the length of the interval becomes very very small. In other words, we can say that the speed of the particle is 7 metre/sec. after 3 seconds.

If $t_{i}=t+\delta t$ then the difference quoteint (i) becomes

$$
\frac{s(t+\delta t)-s(t)}{\delta t}
$$

which represents the average rate of change of distance over the interval $\delta t$ and

$$
\lim _{t \rightarrow \infty} \frac{s(t+\delta t)-s(t)}{\delta t}, \text { provided this limit exists, is called the instantaneous rate of change }
$$

of distance 's' at time $t$.

### 2.1.2 Derivative of a Function

Let $f$ be a real valued function continuous in the interval $\left(x, x_{i}\right) \subseteq D_{f}$ (the domain of $f$ ), then

$$ \text { difference quotient } \frac{f\left(x_{i}\right)-f(x)}{x_{i}-x} $$

represents the average rate of change in the value of $f$ with respect to the change $x_{i}-x$ in the value of independent variable $x$. If $x_{i}$, approaches to $x$, then

$$
\lim _{x_{i} \rightarrow x} \frac{f\left(x_{i}\right)-f(x)}{x_{i}-x}
$$

provided this limit exists, is called the instantaneous rate of change of $f$ with respect to $x$ at $x$ and is written as $f^{\prime}(x)$. If $x_{i}=x+\delta x$ i.e., $x_{i}-x=\delta x$, then the expression (i) can be expressed as

$$
\frac{f(x+\delta x)-f(x)}{\delta x}
$$

and

$$
\lim _{\delta x \rightarrow 0} \frac{f(x+\delta x)-f(x)}{\delta x}
$$

provided the limit exists, is defined to be the derivative of $f$ (or differential coefficient of $f$ ) with respect to $x$ at $x$ and is denoted by $f^{\prime}(x)$ (read as "f-prime of $x$ "). The domain of $f^{\prime}$ consists of all $x$ for which the limit exists. If $x \in D_{f}$ and $f^{\prime}(x)$ exists, then $f$ is said to be differentiable at $x$. The process of finding $f^{\prime}$ is called differentiation.

## Notation for Derivative

Several notations are used for derivatives. We have used the functional symbol $f^{\prime}(x)$, for the derivative of $f$ at $x$. For the function $y=f(x)$.

$$ y+\delta y=f(x+\delta x) $$

where $\delta y$ is the increment of $y$ (change in the value of $y$ ) corresponding to $\delta x$, the change in the value of $x$, then

$$ \delta y=f(x+\delta x)-f(x) $$

Dividing both the sides of (iv) by $\delta x$, we get

$$ \frac{\delta y}{\delta x}=\frac{f(x+\delta x)-f(x)}{\delta x} $$

Taking limit of both the sides of (v) as $\delta x \rightarrow 0$, we have

$$ \begin{aligned} & \lim *{x \rightarrow \infty} \frac{\delta y}{\delta x}=\lim _{x \rightarrow \infty} \frac{f(x+\delta x)-f(x)}{\delta x} \ & \text { (vi) } \ & \frac{\lim }{x \rightarrow \infty} \frac{\delta y}{\delta x} \text { is denoted by } \frac{d y}{d x}, \text { so (vi) is written as } \frac{d y}{d x}=f^{\prime}(x) \end{aligned} $$

Note: The symbol $\frac{d y}{d x}$ is used for the derivative of $y$ with respect to $x$ and here it is not a quotient of $d y$ and $d x . \frac{d y}{d x}$ is also denoted by $y^{\prime}$.

Now we write, in a table the notations for the derivative of $y=f(x)$ used by different mathematicians:

|  Name of
Mathematician | Leibniz | Newton | Lagrange | Cauchy  |
| --- | --- | --- | --- | --- |
|  Notation used for derivative | $\frac{d y}{d x}=\frac{d f}{d x}$ | $f(x)$ | $f^{\prime}(x)$ | $D f(x)$  |

If we replace $x+\delta x$ by $x$ and $x$ by a, then the expression $f(x+\delta x)-f(x)$ becomes $f(x)-f(a)$, and the change $\delta x$ in the independent variable, in this case, is $x-a$.

So the expression $\frac{f(x+\delta x)-f(x)}{\delta x}$ is written as $\frac{f(x)-f(a)}{x-a} \quad$ (vii) Taking the limit of the expressiom(vii) when $x \rightarrow a$, gives

$$ \lim _{x \rightarrow a} \frac{f(x)-f(a)}{x-a}=f^{\prime}(a) \text {. Here } f^{\prime}(a) $$

is called the derivative of $f$ at $x=a$.

### 2.2 FINDING $\mathbf{f}^{\prime}(\mathbf{x})$ FROM DEFINITION OF DERIVATIVE

Given a function $f, f^{\prime}(x)$ if it exists, can be found by the following four steps Step I Find $f(x+\delta x)$ Step II Simplify $f(x+\delta x)-f(x)$ Step III Divide $f(x+\delta x)-f(x)$ by $\delta x$ to get $\frac{f(x+\delta x)-f(x)}{\delta x}$ and simplify it Step IV Find $\lim _{x \rightarrow \infty} \frac{f(x+\delta x)-f(x)}{\delta x}$ The method of finding derivatives by this process is called differentiation by definition or by ab-initio or from first principle.

Example 1: Find the derivative of the following functions by definition (a) $f(x)=\infty$ (b) $f(x) \quad x^{2}$

Solution: (a) For $f(x)=c$ (i) $f(x+\delta x)=c$ (ii) $f(x+\delta x)-f(x)=c-c=0$ (iii) $\frac{f(x+\delta x)-f(x)}{\delta x}=\frac{0}{\delta x}=0$ (iv) $\lim _{x \rightarrow 0} \frac{f(x+\delta x)-f(x)}{\delta x}=\lim _{x \rightarrow 0}(0)=0$

Thus $\quad f^{\prime}(x)=0$, that is, $\frac{d}{d x}(c)=0$ (b) For $f(x)=x^{2}$ (i) $f(x+\delta x)=(x+\delta x)^{2}$ (ii) $f(x+\delta x)-f(x)=(x+\delta x)^{2}-x^{2}=x^{2}+2 x \delta x+(\delta x)^{2}-x^{2}$ ${ }^{\infty} 2 x \delta x+(\delta x)^{2}=(2 x+\delta x) \delta x$ version: 1.1

(ii) $\frac{f(x+\delta x)-f(x)}{\delta x}=\frac{(2 x+\delta x) \delta x}{\delta x}=\mathbf{2} x \quad \delta x, \quad\left(\begin{array}{ll}\delta \mathrm{x} & 0\end{array}\right)$
(iv) $\lim _{x \rightarrow a} \frac{f(x+\delta x)-f(x)}{\delta x}=\lim _{x \rightarrow a}(2 x+\delta x)=2 x$
i.e.,

$$
f^{\prime}(x)=2 x
$$

Example 2: Find the derivative of $\sqrt{x}$ at $x=a$ from first principle.

Solution: If $\quad f(x)=\sqrt{x}$, then
(i) $\quad f(x+\delta x)=\sqrt{x+\delta x}$ and
(ii) $f(x+\delta x)-f(x)=\sqrt{x+\delta x}-\sqrt{x}$

$$
\begin{aligned}
& =\frac{(\sqrt{x+\delta x}-\sqrt{x})(\sqrt{x+\delta x}+\sqrt{x})}{\sqrt{x+\delta x}+\sqrt{x}}(\begin{array}{c}
\text { rationalizing the } \\
\text { numerator }
\end{array}) \\
& =\frac{(x+\delta x)-x}{\sqrt{x+\delta x}+\sqrt{x}}
\end{aligned}
$$

i.e., $\quad f(x+\delta x)-f(x)=\frac{\delta x}{\sqrt{x+\delta x}+\sqrt{x}}$
(iii) Dividing both sides of(1)by $\delta x$, we have

$$
\frac{f(x+\delta x)-f(x)}{\delta x}=\frac{\delta x}{\delta x(\sqrt{x+\delta x}+\sqrt{x})} \cdot \frac{1}{\sqrt{x+\delta x}+\sqrt{x}}(\because \delta x \quad 0)
$$

(iv) Taking limit of both the sides as $\delta x \rightarrow 0$, we have

$$
\lim _{x \rightarrow a} \frac{f(x+\delta x)-f(x)}{\delta x}=\lim _{x \rightarrow a}\left(\frac{1}{\sqrt{x+\delta x}+\sqrt{x}}\right)
$$

i.e., $\quad f^{\prime}(x)=\frac{1}{\sqrt{x}+\sqrt{x}}=\frac{1}{2 \sqrt{x}} \quad(x>0)$
and $\quad f^{\prime}(a)=\frac{1}{2 \sqrt{a}}$
or
Putting $\quad x=a$ in $f(x)=\sqrt{x}$, gives $\quad f(a) \quad \sqrt{a}$
So $\quad f(x)-f(a)=\sqrt{x}-\sqrt{a}$
Using alternative form for the definition of a derivative, we have

$$
\begin{aligned}
& \frac{f(x)-f(a)}{x-a}=\frac{\sqrt{x}-\sqrt{a}}{x-a} \\
& =\frac{(\sqrt{x}-\sqrt{a})(\sqrt{x}+\sqrt{a})}{(x-a)(\sqrt{x}+\sqrt{a})} \text { (rationalizing the numerator) } \\
& =\frac{x-a}{(x-a)(\sqrt{x}+\sqrt{a})} \cdot \frac{1}{\sqrt{x}+\sqrt{a}} \quad(x \quad a)
\end{aligned}
$$

Taking limit of both the sides of (II)as $x \rightarrow a$, gives

$$
\lim _{x \rightarrow a} \frac{f(x)-f(a)}{x-a}=\lim _{x \rightarrow a} \frac{1}{\sqrt{x}+\sqrt{a}} \cdot \frac{1}{\sqrt{a}+\sqrt{a}}
$$

i.e.,

$$
f^{\prime}(a)=\frac{1}{2 \sqrt{a}}
$$

Example 3: If $y=\frac{1}{x^{2}}$, then find $\frac{d y}{d x}$ at $x=-1$ by ab-initio method.

Solution: Here $y=\frac{1}{x^{2}}$, so

$$
y+\delta y=\frac{1}{(x+\delta x)^{2}}
$$

Subtracting (i) from (ii), we get

$$
\begin{aligned}
\delta y & =\frac{1}{(x+\delta x)^{2}} \cdot \frac{1}{x^{2}}=\frac{x^{2}-(x+\delta x)^{2}}{x^{2}(x+\delta x)^{2}} \\
& =\frac{(x+(x+\delta x))(x-(x+\delta x))}{x^{2}(x+\delta x)^{2}}
\end{aligned}
$$

$$
=\frac{(2 x+\delta x)(-\delta x)}{x^{2}(x+\delta x)^{2}} \cdot \frac{-\delta x(2 x+\delta x)}{x^{2}(x+\delta x)^{2}}
$$

Dividing both sides of (iii) by $\delta x$, we have

$$
\frac{\delta y}{\delta x}=\frac{-\delta x(2 x+\delta x)}{x^{2}(x+\delta x)^{2} \delta x} \cdot \frac{-(2 x+\delta x)}{x^{2}(x+\delta x)^{2}} \quad(\delta x \quad 0)
$$

Taking limit as $\delta x \rightarrow 0$, gives

$$
\begin{aligned}
& \lim _{\delta x \rightarrow 0} \frac{\delta y}{\delta x}=\lim _{\delta x \rightarrow 0} \frac{-(2 x+\delta x)}{x^{2}(x+\delta x)^{2}} \\
& =\frac{-(2 x)}{x^{2}\left(x^{2}\right)} \quad \quad \text { (Using quotient theorem of limits) } \\
& \text { i.e., } \quad \frac{d y}{d x}=\frac{-2}{x^{2}} \text { and } \quad \frac{d y}{d x} \mathrm{~b}_{x-1} \quad \frac{-2}{(-1)^{2}} \quad \frac{-2}{-1} \quad 2
\end{aligned}
$$

Note: The value of $\frac{d y}{d x}$ at $(x-1)$ is written as $\frac{d y}{d x} \frac{1}{x-1}$.

Example 4: Find the derivative of $x^{\frac{3}{2}}$ and also calculate the value of derivative at $x=8$.

Solution: Let $f(x)=x^{\frac{3}{2}}$. Then

$$
f(x+\delta x)=(x+\delta x)^{\frac{3}{2}}
$$

and

$$
f(x+\delta x)-f(x)=(x+\delta x)^{\frac{3}{2}}-x^{\frac{3}{2}}=\frac{\left((x+\delta x)^{\frac{3}{2}}-x^{\frac{3}{2}}\right)\left[(x+\delta x)^{\frac{3}{2}}+(x+\delta x)^{\frac{3}{2}} \cdot x^{\frac{3}{2}}+x^{\frac{3}{2}}\right]}{(x+\delta x)^{\frac{3}{2}}+(x+\delta x)^{\frac{3}{2}} \cdot x^{\frac{3}{2}}+x^{\frac{3}{2}}}
$$

version: 1.1

$$
=\frac{\left[(x+\delta x)^{\frac{3}{2}}\right]^{3}-\left(x^{\frac{3}{2}}\right)^{3}}{(x+\delta x)^{\frac{3}{2}}+(x+\delta x)^{\frac{3}{2}} \cdot x^{\frac{3}{2}}+x^{\frac{3}{2}}} \frac{(x+\delta x)^{2}-x^{2}}{(x+\delta x)^{\frac{3}{2}}+(x+\delta x)^{\frac{3}{2}} \cdot x^{\frac{3}{2}}+x^{\frac{3}{2}}}
$$

i.e., $\quad f(x+\delta x)-f(x)=\frac{\delta x(2 x+\delta x)}{(x+\delta x)^{\frac{3}{2}}+(x+\delta x)^{\frac{3}{2}} \cdot x^{\frac{3}{2}}+x^{\frac{3}{2}}}$
Dividing both the sides of (i) by $\delta x$, we get

$$
\frac{f(x+\delta x)-f(x)}{\delta x}=\frac{2 x+\delta x}{(x+\delta x)^{\frac{3}{2}}+(x+\delta x)^{\frac{3}{2}} \cdot x^{\frac{3}{2}}+x^{\frac{3}{2}}}
$$

Taking limit of both the sides as $\delta x \rightarrow 0$, we have

$$
f^{\prime}(x)=\frac{2 x}{x^{\frac{3}{2}}+x^{\frac{3}{2}} \cdot x^{\frac{3}{2}}+x^{\frac{3}{2}}} \frac{2 x}{3 x^{\frac{3}{2}}} \frac{2}{3 x^{\frac{1}{2}}}
$$

and

$$
f^{\prime}(8)=\frac{2}{3.8 \frac{1}{3}}=\frac{1}{3}
$$

Example 5: Find the derivative of $x^{3}+2 x+3$.
Solution: Let $y=x^{3}+2 x+3$. Then
(i) $y+\delta y=(x+\delta x)^{3}+2(x+\delta x)+3$
(ii) $\delta y=\left[(x+\delta x)^{3}+2(x+\delta x)+3\right]-\left[x^{3}+2 x+3\right]$

$$
\begin{aligned}
& =\left[(x+\delta x)^{3}-x^{3}\right]+2[(x+\delta x)-x]+(3-3) \\
& =[(x+\delta x)-x]\left[(x+\delta x)^{3}+(x+\delta x) x+x^{2}\right]+2 \delta x
\end{aligned}
$$

(iii) $\frac{\delta y}{\delta x}=\frac{\delta x\left[(x+\delta x)^{3}+(x+\delta x) x+x^{2}\right]+2 \delta x}{\delta x}$

$$
=(x+\delta x)^{2}+(x+\delta x) x+x^{2}+2
$$

(iv) $\lim _{x \rightarrow \infty} \frac{\delta y}{\delta x}=\lim _{x \rightarrow \infty}\left[(x+\delta x)^{2}+(x+\delta x) x+x^{2}+2\right]$

$$
\frac{d y}{d x}=(x)^{2}+(x) x+x^{2}+2
$$

i.e., $\frac{d}{d x}\left(x^{2}+2 x+3\right)=3 x^{2}+2$

### 2.2.1 Derivation of $\mathbf{x}^{n}$ where $\mathbf{n} \in \mathbf{Z}$.

(a) We find the derivative of $x^{n}$ when $n$ is positive integer.
(a) Let $y=x^{n}$. Then

$$
y+\delta y=(x+\delta x)^{n}
$$

and $\quad \delta y=(x+\delta x)^{n}-x^{n}$
Using the binomial theorem, we have

$$
\delta y=\left[x^{n}+n x^{n-1} \cdot \delta x+\frac{n(n-1)}{\frac{1}{n} x^{n-2}}\left(\left(\delta x^{2} \cdot\right) \quad \cdot n \quad(\delta x)^{n}\right)\right] \quad x^{n}
$$

i.e., $\quad \delta y=\delta x\left[n x^{n-1}+\frac{n(n-1)}{\frac{1}{n} x^{n-2}} \cdot \delta x \quad \ldots \quad(\delta x)^{n-1}\right]$
Dividing both sides of (i) by $\delta x$, gives

$$
\frac{\delta y}{\delta x}=n x^{n-1}+\frac{n(n-1)}{\frac{1}{n} x^{n-2}} \cdot \delta x+\ldots \quad(\delta x)^{n-1}
$$

Note that each term on the right hand side of (ii) involves $\delta x$ except the first term, so taking the limit as $\delta x \rightarrow 0$, we get $\frac{d y}{d x}=n x^{n-1}$

As $y=\alpha^{n}$, so $\frac{d}{d x}\left(x^{n}\right) \quad n \cdot x^{n-1}$

$$
y=x^{n}
$$

Note: If $n=0$, then the formula $\frac{d}{d x}\left(x^{n}\right)=n x^{n-1}$ reduces to $\frac{d}{d x}\left(x^{0}\right)=0 x^{0-1}=0$ i.e., $\frac{d}{d x}(1)=0$ which is correct by example 1 part (a).
(b) Let $y=x^{n}$ where $n$ is a negative integer.

Let $n=-m$ ( $m$ is a positive integer). Then

$$
y=x^{-m}=\frac{1}{x^{m}}
$$

and $\quad y+\delta y=\frac{1}{(x+\delta x)^{m}}$
Subtracting (i) from (ii). gives

$$
\begin{aligned}
& \delta y=\frac{1}{(x+\delta x)^{m}}-\frac{1}{x^{m}}=\frac{x^{m}-(x+\delta x)^{m}}{x^{m}(x+\delta x)^{m}} \\
= & \frac{x^{m}-\left(x^{m}+m x^{m-1} \delta x+\frac{m(m-1)}{\frac{1}{n} x^{m-2}}(\delta x)^{2}+\ldots+(\delta x)^{m}\right]}{x^{m}(x+\delta x)^{m}} \\
& \quad \text { (expanding }(x+\delta x)^{m} \text { by binomial theorem) } \\
= & \frac{-\delta x\left(m x^{m-1}+\frac{m(m-1)}{\frac{1}{n} x^{m-2}} \delta x+\ldots+(\delta x)^{m-1}\right)}{x^{m}(x+\delta x)^{m}} \\
& \text { and } \frac{\delta y}{\delta x}=\frac{-1}{x^{m}(x+\delta x)^{m}}\left(m x^{m-1}+\frac{m(m-1)}{\frac{1}{n} x^{m-2}} \cdot \delta x \quad \ldots \quad(\delta x)^{m-1}\right)
\end{aligned}
$$

Taking limit when $\delta x \rightarrow 0$, we get

$$
\frac{d y}{d x}=\frac{-1}{x^{m} \cdot x^{n}}\left(m x^{m-1}\right) \quad \text { (all terms containing } \delta x \text {,vanish) }
$$

$$
\begin{aligned}
& =(-m) x^{m-1} \cdot x^{-2 m}=(-m) x^{(-m)+1}=n x^{n-1} \quad[\because m-n] \\
& \text { or } \quad \frac{d}{d x}(x)^{n}=n x^{n-1}
\end{aligned}
$$

So far we have proved that $\frac{d}{d x}[x]^{n}=n x^{n-1}$, if $n \in Z$
The above rule holds if $n \in Q-Z$
For example $\frac{d}{d x}\left(x^{\frac{2}{3}}\right)=\frac{2}{3} x^{\frac{2}{3}-1}=\frac{2}{3 x^{\frac{1}{3}}}$
The proof of $\frac{d}{d x}\left[x^{n}\right]=n x^{n-1}$ when $n \in Q-Z$ is left as an exercise.

Note that $\frac{d}{d x}\left[x^{n}\right]=n x^{n-1}$ is called power rule.

## Exercise 2.1

1. Find by definition, the derivatives w.r.t ' $x$ ' of the following functions defined as:
(i) $2 x^{2}+1$
(ii) $2-\sqrt{x}$
(iii) $\frac{1}{\sqrt{x}}$
(iv) $\frac{1}{x^{2}}$
(v) $\frac{1}{x-a}$
(vi) $x(x-3)$
(vii) $\frac{2}{x^{4}}$
(viii) $(x+4)^{\frac{1}{2}}$
(ix) $x^{\frac{2}{3}}$
(xi) $x^{m}, m \in N$
(xii) $\frac{1}{x^{n}, m \in N}$
(xiii) $x^{4 n}$
(xiv) $x^{-100}$
2. Find $\frac{d y}{d x}$ from first principle if
(i) $\sqrt{x+2}$
(ii) $\frac{1}{\sqrt{x+a}}$
version: 1.1

### 2.2.2 DIFFERENTIATION OF EXPRESSIONS OF THE TYPES:

$$
(a x+b)^{n} \text { and } \frac{1}{(a x+b)^{n}}, \quad n=1,2,3 \ldots
$$

We find the derivatives of $(a x+b)^{n}$ and $\frac{1}{(a x+b)^{n}}$ from the first principle when $n \in N$
Example 1: Find from definition the differential coefficient of $(a x+b)^{n}$ w.r.t. ' $x$ ' when n is a positive integer.

Solution: Let $y=(a x+b)^{n},(n$ is a positive integer)
Then $y+\delta y=[a(x+\delta x)+b]^{n}=[(a x+b)+a \delta x]^{n}$
Using the binomial theorem we have

$$
\begin{aligned}
& y+\delta y=(a x \quad b)^{n} \quad\binom{n}{1}(a x \quad b)^{n-1}(a \delta x) \quad\binom{n}{2}(a x \quad b)^{n-1}(a \delta x)^{2}+\ldots \quad(a \delta x)^{n} \\
& \delta y=(y+\delta y)-y=\binom{n}{1}(a x+b)^{n-1}(a \delta x)+\binom{n}{2}(a x+b)^{n-2} \cdot a^{2}(\delta x)^{2}+\ldots+a^{n}(\delta x)^{n} \\
& \quad=\delta x\left[\binom{n}{1}(a x+b)^{n-1} \cdot a+\binom{n}{2}(a x+b)^{n-2} \cdot a^{2} \delta x+\ldots+a^{n}(\delta x)^{n-1}\right]
\end{aligned}
$$

So $\frac{\delta y}{\delta x}=\binom{n}{1}(a x+b)^{n-1} a+\binom{n}{2}(a x+b)^{n-2} \cdot a^{2} \delta x+\ldots+a^{n}(\delta x)^{n-1}$
Taking limit when $\delta x \rightarrow 0$, we have

$$
\lim _{\delta x \rightarrow 0} \frac{\delta y}{\delta x}=\lim _{\delta x \rightarrow 0}\left[\binom{n}{1}(a x+b)^{n-1} \cdot a+\binom{n}{2}(a x+b)^{n-2} \cdot a^{2} \delta x+\ldots+a^{n}(\delta x)^{n-1}\right]
$$

Or $\frac{d y}{d x}=\binom{n}{1}(a x+b)^{n-1} \cdot a$ [All other terms tends to zero when $\delta x \rightarrow 0$ ]
Thus $\frac{d}{d x}(a x+b)^{n}=n(a x+b)^{n-1} \cdot a$

Example 2: Find from first principle, the derivative of $\frac{1}{(a x+b)^{2}}$ w.r.t. ' $x$ ',

Solution: Let $y=\frac{1}{(a x+b)^{2}}$ (when $n$ is a positive integer). Then

$$
\begin{aligned}
& y+\delta y=\frac{1}{\left[a(x+\delta x)+b\right]^{n}} \quad \text { and } \\
& \delta y=y+\delta y-y=\frac{1}{\left[(a x+b)+a \delta x\right]^{n}}-\frac{1}{(a x+b)^{n}} \\
& \text { or } \quad \delta y=\frac{(a x+b)^{n}-(a x+b+a \delta x)^{n}}{\left[(a x+b)+a \delta x\right]^{n}(a x+b)^{n}} \\
& \text { or } \quad \delta y=\frac{-1}{\left[(a x+b)+a \delta x\right]^{n}(a x+b)^{n}} \mathrm{x}\left[\left(\begin{array}{ll}
(a x & b)
\end{array}\right) a \delta x\right]^{n}\left(\begin{array}{ll}
(a x & b)
\end{array}\right)^{n} \text { (I) }
\end{aligned}
$$

Using the binomial theorem, we simplify the expression
$\left[(a x+b)+a \delta x\right]^{n}-(a x+b)^{n}$, That is,
$\left[(a x+b)+a \delta x\right]^{n}-(a x+b)^{n}=[(a x+b)^{n}+\binom{n}{1}(a x+b)^{n-1}(a \delta x)$

$$
\begin{gathered}
+\binom{n}{2}(a x+b)^{n-2} \cdot a^{2}(\delta x)^{2}+\ldots+(a \delta x)^{n} \\
=\binom{n}{1}(a x+b)^{n-1} \cdot a \delta x+\binom{n}{2}(a x+b)^{n-2} \cdot a^{2}(\delta x)^{2}+\ldots+a^{n}(\delta x)^{n} \\
=\delta x\left[\binom{n}{1}(a x+b)^{n-1} \cdot a+\binom{n}{2}(a x+b)^{n-2} a^{2} \delta x+\ldots+a^{n}(\delta x)^{n-1}\right]
\end{gathered}
$$

## Now (I) becomes

$$
\delta y=\frac{\delta x}{[(a x+b)+a \delta x]^{n}(a x+b)^{n-1}}\binom{n}{1}(a \pi b)^{n-1} . a
$$

$$
+\binom{n}{2}(a x+b)^{n-2} \cdot a^{2} \delta x+\ldots+\mathrm{a}^{n}(\delta x)^{n-1}
$$

and $\frac{\delta y}{\delta x}=\frac{1}{[(a x+b)+a \delta x]^{n}(a x+b)^{n-1}}\binom{n}{1}(a \pi b)^{n-1} . a$

$$
+\binom{n}{2}(a x+b)^{n-2} \cdot a^{2} \delta x+\ldots+\mathrm{a}^{n}(\delta x)^{n-1}
$$

Using the product and sum rules of limits when $\delta x \rightarrow 0$, we have

$$
\frac{d y}{d x}=\frac{1}{(a x+b)^{n}(a x+b)^{n}}\binom{n}{1}(a \pi b)^{n-1} . a \quad\left(\frac{\square \lim _{\delta x \rightarrow 0} \frac{\delta y}{\delta x}=\frac{d y}{d x} \text { and }}{\text { all other terms containing }}\right)
$$

or $\frac{d}{d x}=\left[\frac{1}{(a x+b)^{n}}\right]=\frac{-n a}{(a x+b)^{n-1}}=n(a x b)^{-(n+1)} . a$

## Exercise 2.2

1. Find from first principles, the derivatives of the following expressions w.r.t. their respective independent variables:
(i) $(a x+b)^{2}$
(ii) $(2 x+3)^{3}$
(iii) $(3 t+2)^{-2}$
(iv) $\frac{1}{(a x+b)^{2}}$
(v) $\frac{1}{(a z-b)^{2}}$

### 2.3 THEOREMS ON DIFFERENTIATION

We have, so far proved the following two formulas:

1. $\frac{d y}{d x}(c)=0$ i.e.. the derivative of a constant function is zero.
2. $\frac{d}{d x}\left(x^{n}\right)=n x^{n-1}$ power formula (or rule) when $n$ is any rational number.
Now we will prove other important formulas (or rules) which are used to determine derivatives of different functions efficiently. Henceforth, in all subsequent discussion, $f, g, h$ etc. all denote functions differentiable at $x$, unless stated otherwise.
3. Derivative of $y=c f(x)$

Proof: Let $y=c f(x)$. Then
(i) $y+\delta y=c f(x+\delta x)$ and
(ii) $y+\delta y-y=c f(x+\delta x)-c f(x)$
or $\delta y=c \mid f(x+\delta x)-f(x) \quad$ (factoring out $c$ )
(iii) $\frac{\delta y}{\delta x}=c\left(\frac{f(x+\delta x)-f(x)}{\delta x}\right)$

Taking limit when $\delta x \rightarrow 0$
(iv) $\lim _{\delta x \rightarrow 0} \frac{\delta y}{\delta x}=\lim _{\delta x \rightarrow 0}\left[c \frac{f(x+\delta x)-f(x)}{\delta x}\right] \quad c \lim _{\delta x \rightarrow 0} \frac{f(x+\delta x)-f(x)}{\delta x}$

A constant factor can be taken out from a limit sign.
Thus $\frac{d y}{d x}=c f^{\prime}(x)$, that is, $[c f(x)]=c f^{\prime}(x)$
or $\frac{d y}{d x}=c f^{\prime}(x) \quad=\quad[c f(x)]=c f^{\prime}(x)$

Example 1: Calculate $\frac{d}{d x}\left(3 x^{\frac{1}{3}}\right)$
Solution: $\quad \frac{d}{d x}\left(3 x^{\frac{1}{3}}\right)=3 \frac{d}{d x}\left(x^{\frac{1}{3}}\right) \quad$ (Using Formula 3)

$$
=3 \mathrm{x} \frac{4}{3} x^{\frac{1}{3}}=4 x^{\frac{1}{3}} \quad \text { (Using power rule) }
$$

4. Derivative of a sum or a Difference of Functions:

If $f$ and $g$ are differentiable at $x$, then $f+g, f-g$ are also differentiable at $x$ and $[f(x)+g(x)]=f^{\prime}(x)+g^{\prime}(x)$, that is, $\frac{d}{d x}[f(x)+g(x)]=\frac{d}{d x}[f(x)]+\frac{d}{d x}[g(x)]$ Also $[f(x)-g(x)]=f^{\prime}(x)-g^{\prime}(x)$, that is, $\frac{d}{d x}[f(x)-g(x)]=\frac{d}{d x}[f(x)]-\frac{d}{d x}[g(x)]$
Proof: Let $\phi(x)=f(x)+g(x)$. Then
(i) $\phi(x+\delta x)=f(x+\delta x)+g(x+\delta x)$ and
(ii) $\phi(x+\delta x)-\phi(x)=f(x+\delta x)+g(x+\delta x)-[f(x)+g(x)]$
$=[f(x+\delta x)-f(x)]+[g(x+\delta x)-g(x)]$ (rearranging the terms)
(iii) $\frac{\phi(x+\delta x)-\phi(x)}{\delta x}=\frac{f(x+\delta x)-f(x)}{\delta x} \quad \frac{g(x+\delta x)-g(x)}{\delta x}$

Taking the limit when $\delta x \rightarrow 0$
(iv) $\lim _{\delta x \rightarrow 0} \frac{\phi(x+\delta x)-\phi(x)}{\delta x}=\lim _{\delta x \rightarrow 0}\left[\frac{f(x+\delta x)-f(x)}{\delta x} \frac{g(x+\delta x)-g(x)}{\delta x}\right]$
$=\lim _{\delta x \rightarrow 0} \frac{f(x+\delta x)-f(x)}{\delta x} \lim _{\delta x \rightarrow 0} \frac{g(x+\delta x)-g(x)}{\delta x}$
(The limit of a sum is the sum of the limits)

$$
\phi^{\prime} x=f^{\prime}(x)+g^{\prime}(x), \text { that is }[f(x)+g(x)] \equiv f^{\prime}(x)+g^{\prime}(x)
$$

or $\frac{d}{d x}[f(x)+g(x)]=\frac{d}{d x}[f(x)]+\frac{d}{d x}[g(x)]$
The proof for the second part is similar.

Note: Sum or difference formula can be extended to find derivative of more than two functions.

Example 1: Find the derivative of $y=\frac{3}{4} x^{4}+\frac{2}{3} x^{3}+\frac{1}{2} x^{2}+2 x+5$ w.r.t. $x$.

Solution: $y=\frac{3}{4} x^{4}+\frac{2}{3} x^{3}+\frac{1}{2} x^{2}+2 x+5$
Differentiating with respect to $x$, we have
$\frac{d y}{d x}\left[\frac{3}{4} x^{4}+\frac{2}{3} x^{3}+\frac{1}{2} x^{2}+2 x+5\right]=\frac{d}{d x}\left[\frac{3}{4} x^{4}\right]+\frac{d}{d x}\left[\frac{2}{3} x^{3}\right]+\frac{d}{d x}\left[\frac{1}{2} x^{2}\right]+\frac{d}{d x}(2 x)+\frac{d}{d x}(5)$
(Using formula 4)
$=\frac{3}{4} \frac{d}{d x}\left(x^{4}\right)+\frac{2}{3} \frac{d}{d x}\left(x^{3}\right)+\frac{1}{2} \frac{d}{d x}\left(x^{2}\right)+2 \frac{d}{d x}(x)+0 \quad$ (Using formula 3 and 1)
$=\frac{3}{4}\left(4 x^{4-1}\right)+\frac{2}{3}\left(3 x^{3-1}\right)+\frac{1}{2}\left(2 x^{3-1}\right)+2\left(1 . x^{2-1}\right) \quad$ (By power formula)
$=3 x^{3}+2 x^{2}+x+2$

Example 2: Find the derivative of $y=\left(x^{2}+5\right)\left(x^{3}+7\right)$ with respect to $x$.
Solution: $y=\left(x^{2}+5\right)\left(x^{3}+7\right) \quad=x^{2}+5 x^{3}+7 x^{2}+35$
Differentiating with respect to $x$, we get

$$
\begin{aligned}
& \frac{d y}{d x}=\frac{d}{d x}\left[x^{2}+5 x^{3}+7 x^{2}+35\right] \\
= & \frac{d}{d x}\left[x^{2}\right]+5 \frac{d}{d x}\left(x^{2}\right)+7 \frac{d}{d x}\left(x^{2}\right)+\frac{d}{d x}(35) \text { (Using formulas } 3 \text { and } 4 \text { ) } \\
= & 5 x^{3-1}+5 \times 3 x^{3-1}+7 \times 2 x^{2-1}+0 \\
= & 5 x^{4}+15 x^{2}+14 x
\end{aligned}
$$

Example 3: $\quad$ Find the derivative of $y=(2 \sqrt{x}+2)(x-\sqrt{x})$ with respect to $x$.

Solution: $y=(2 \sqrt{x}+2)(x-\sqrt{x})$

$$
\begin{aligned}
& =2(\sqrt{x}+1) \sqrt{x}(\sqrt{x}-1)=2 \sqrt{x}(\sqrt{x}+1)(\sqrt{x}-1) \\
& =2 \sqrt{x}(x+1)=2\left(x^{\frac{1}{2}}-x^{\frac{1}{2}}\right)
\end{aligned}
$$

Differentiating with respect to $x$, we have

$$
\begin{aligned}
& \frac{d y}{d x}=\frac{d}{d x}\left[2\left(x^{\frac{1}{2}}-x^{\frac{1}{2}}\right)\right] \\
& =2\left[\frac{d}{d x}\left(x^{\frac{1}{2}}\right)-\frac{d}{d x}\left(x^{\frac{1}{2}}\right)\right]=2\left[\frac{3}{2} x^{\frac{1}{2}-1}-\frac{1}{2} x^{\frac{1}{2}-1}\right] \\
& =3 x^{\frac{1}{2}}-x^{\frac{1}{2}}=3 \sqrt{x}-\frac{1}{\sqrt{x}}=\frac{3 x-1}{\sqrt{x}}
\end{aligned}
$$

## 5. Derivative of a product. (The product Rule)

If $f$ and $g$ are differentiable at $x$, then $f g$ is also differentiable at $x$ and

$$
\begin{aligned}
& {[f(x) g(x)]=f^{\prime}(x) g(x)+f(x) g^{\prime}(x) \text {, that is, } \\
& \frac{d}{d x}[f(x) g(x)]=-\left[\frac{d}{d x}[f(x)]\right] g(x) \quad f(x) \left[\frac{d}{d x}[g(x)]\right]}
\end{aligned}
$$

Proof: Let

$$
\phi(x)=f(x) g(x) \text {. Then }
$$

(i) $\quad \phi(x+\delta x)=f(x+\delta x) g(x+\delta x)$
(ii) $\quad \phi(x+\delta x)-\phi(x)=f(x+\delta x) g(x+\delta x)-f(x) g(x)$

Subtracting and adding $f(x) g(x+\delta x)$ in step (ii), gives
$\phi(x+\delta x)-\phi(x)=f(x+\delta x) g(x+\delta x)-f(x) g(x+\delta x)+f(x) g(x+\delta x)-f(x) g(x)$

$$
=[f(x+\delta x)-f(x)] g(x+\delta x)+f(x)[g(x+\delta x)-g(x)]
$$

(iii) $\frac{\phi(x+\delta x)-\phi(x)}{\delta x}=\left[\frac{f(x+\delta x)-f(x)}{\delta x}\right] g(x \delta x) \quad f(x)\left[\frac{g(x+\delta x)-g(x)}{\delta x}\right]$

Taking limit when $\delta x \rightarrow 0$
(iv) $\lim _{\delta x \rightarrow 0} \frac{\phi(x+\delta x)-\phi(x)}{\delta x}$

$$
\begin{aligned}
& =\lim _{\delta x \rightarrow 0}\left[\frac{f(x+\delta x)-f(x)}{\delta x} g(x+\delta x)+f(x) \cdot \frac{g(x+\delta x)-g(x)}{\delta x}\right] \\
& =\lim _{\delta x \rightarrow 0} \frac{f(x+\delta x)-f(x)}{\delta x} \cdot \lim _{\delta x \rightarrow 0} g(x+\delta x)+\lim _{\delta x \rightarrow 0} f(x) \cdot \lim _{\delta x \rightarrow 0} \frac{g(x+\delta x)-g(x)}{\delta x}
\end{aligned}
$$

(Using limit theorems)
Thus $\phi^{\prime}(x)=f^{\prime}(x) g(x)+f(x) g^{\prime}(x) \quad\left[\because \lim _{\delta x \rightarrow 0} g(x+\delta x)=g(x)\right]$
or $\quad \frac{d}{d x}[f(x) \cdot g(x)]=\frac{d}{d x}[f(x)] \cdot g(x) \quad f(x)\left[\frac{d}{d x} g(x)\right]$
Example: Find derivative of $y=(2 \sqrt{x}+2)(x-\sqrt{x})$ with respect to $x$

Solution: $y=(2 \sqrt{x}+2)(x-\sqrt{x})$

$$
=2(\sqrt{x}+1)(x-\sqrt{x})
$$

Differentiating with respect to $x$, we get

$$
\begin{aligned}
\frac{d y}{d x} & =2 \frac{d}{d x}[(\sqrt{x}+1)(x-\sqrt{x})] \\
& =2\left[\left(\frac{d}{d x}(\sqrt{x}+1)\right)(x-\sqrt{x})+(\sqrt{x}+1) \frac{d}{d x}(x-\sqrt{x})\right] \\
& =2\left[\left(\frac{1}{2} x^{\frac{1}{2}-1}+0\right)(x-\sqrt{x})+(\sqrt{x}+1) \times\left(1-\frac{1}{2} x^{\frac{1}{2}-1}\right)\right]
\end{aligned}
$$

$$
\begin{aligned}
& =2\left[\frac{1}{2 \sqrt{x}}(x-\sqrt{x})+(\sqrt{x}+1) \times\left(1-\frac{1}{2 \sqrt{x}}\right)\right] \\
& =2\left[\frac{x-\sqrt{x}}{2 \sqrt{x}}+(\sqrt{x}+1)\left(\frac{2 \sqrt{x}-1}{2 \sqrt{x}}\right)\right] \\
& =\frac{1}{\sqrt{x}}[x-\sqrt{x}+2 x-\sqrt{x}+2 \sqrt{x}-1] \\
& =\frac{3 x-1}{\sqrt{x}}
\end{aligned}
$$

## 6. Derivative of a Quotient (The Quotient Rule)

If $f$ and $g$ are differentiable at $x$ and $g(x) \neq 0$, for any $x \in D(g)$ then $\frac{f}{g}$ is differentiable at $x$ and $\left(\frac{f(x)}{g(x)}\right)=\frac{f^{\prime}(x) g(x)-f(x) g^{\prime}(x)}{[g(x)]^{2}}$
that is, $\frac{d}{d x}[\frac{f(x)}{g(x)}]=\frac{\left[\frac{d}{d x}[f(x)]\right] g(x)-f(x)\left[\frac{d}{d x}[g(x)]\right]}{[g(x)]^{2}}$
Proof: Let $\phi(x)=\frac{f(x)}{g(x)}$ Then
(i) $\phi(x+\delta x)=\frac{f(x+\delta x)}{g(x+\delta x)}$
(ii) $\phi(x+\delta x)-\phi(x)=\frac{f(x+\delta x)}{g(x+\delta x)} \cdot \frac{f(x)}{g(x)}=\frac{f(x+\delta x) g(x)-f(x) g(x+\delta x)}{g(x) g(x+\delta x)}$

Subtracting and adding $f(x) g(x)$ in the numerator of step (ii), gives

$$
\begin{aligned}
\phi(x+\delta x)-\phi(x) & =\frac{f(x+\delta x) g(x)-f(x) g(x)-f(x) g(x+\delta x)+f(x) g(x)}{g(x) g(x+\delta x)} \\
& =\frac{1}{g(x) g(x+\delta x)}[(f(x+\delta x)-f(x)) g(x)-f(x)(g(x+\delta x)-g(x))]
\end{aligned}
$$

(iii) $\frac{\phi(x+\delta x)-\phi(x)}{\delta x}=\frac{1}{g(x) g(x+\delta x)}\left[\frac{f(x+\delta x)-f(x)}{\delta x} g(x) \quad f(x) \cdot \frac{g(x+\delta x)-g(x)}{\delta x}\right]$

Taking limit when $\delta x \rightarrow 0$
(iv) $\lim _{\delta x \rightarrow 0} \frac{\phi(x+\delta x)-\phi(x)}{\delta x}$
$\lim _{\delta \rightarrow 0}\left[\frac{1}{g(x) g(x+\delta x)}\left(\frac{f(x+\delta x)-f(x)}{\delta x} \cdot g(x)-f(x) \cdot \frac{g(x+\delta x)-g(x)}{\delta x}\right)\right]$
Using limit theorems, we have
$\phi^{\prime}(x)=\frac{1}{g(x) \cdot g(x)}\left[f^{\prime}(x) g(x) \quad f(x) g^{\prime}(x)\right]=\left(\because \lim _{\delta x \rightarrow 0} g(x \quad \delta x) \quad g(x)\right)$
Thus $\left(\frac{f(x)}{g(x)}\right)=\frac{f^{\prime}(x) g(x)-f(x) g^{\prime}(x)}{[g(x)]^{2}}$ or $\frac{d}{d x}\left[\frac{f(x)}{g(x)}\right] \cdot\left[\frac{d}{d x}[f(x)]\right] g(x)-f(x)\left[\frac{d}{d x}[g(x)]\right]$
$[g(x)]^{2}$

## First Alternative Proof:

$$
\phi(x)=\frac{f(x)}{g(x)} \text { can be written as } f(x)=\phi(x) g(x)
$$

Using the procedure used to prove product rule, quotient rule can be proved.
Second Alternative Proof: We first prove the reciprocal rule and then use product rule to prove the quotient rule.

The reciprocal rule. If $g$ is differentiable at $x$ and $g(x) \neq 0$, then $\frac{1}{g}$ is differentiable at $x$ and $\frac{d}{d x}\left[\frac{1}{g(x)}\right]=\frac{\frac{d}{d x}[g(x)]}{[g(x)]^{2}}$ (Proof of reciprocal rule is left as an exercise)

Using the product rule to $f(x) \cdot \frac{1}{g(x)}$, we have

$$
\begin{aligned}
& \frac{d}{d x}\left[f(x) \cdot \frac{1}{g(x)}\right]=\left(\frac{d}{d x}[f(x)]\right) \cdot \frac{1}{g(x)} \quad f(x) \cdot \frac{d}{d x}\left[\frac{1}{g(x)}\right] \\
& =\frac{\frac{d}{d x}[f(x)]}{g(x)}+f(x) \cdot \frac{\frac{d}{d x}[g(x)]}{[g(x)]^{2}} \\
& \text { i.e., } \quad \frac{d}{d x}\left[\frac{f(x)}{g(x)}\right]=\frac{\left[\frac{d}{d x}[f(x)]\right] g(x)-f(x)\left[\frac{d}{d x}[g(x)]\right]}{[g(x)]^{2}}
\end{aligned}
$$

Example 2: $\quad$ Find $\frac{d y}{d x}$ if $y=\frac{\left(\sqrt{x}+1\right)\left(x^{\frac{3}{2}}-1\right)}{x^{\frac{1}{2}}-1}, \quad(x \neq 1)$
Solution: Given that

$$
\begin{aligned}
& y=\frac{\left(\sqrt{x}+1\right)\left(x^{\frac{3}{2}}-1\right)}{x^{\frac{1}{2}}-1} \quad \frac{\left(\sqrt{x}+1\right)\left[(\sqrt{x})^{2}-(1)^{2}\right]}{\sqrt{x}-1} \\
& =\frac{(\sqrt{x}+1)(\sqrt{x}-1)(x+1+\sqrt{x})}{\sqrt{x}-1}=(\sqrt{x}+1)(x+1+\sqrt{x}) \\
& =(\sqrt{x}+1)(\sqrt{x}-1)(x+1+\sqrt{x})=(\sqrt{x}+1)^{2}+(\sqrt{x}+1) x \\
& =x+1+2 \sqrt{x}+x \sqrt{x}+x=x^{\frac{3}{2}}+2 x+2 x^{\frac{1}{2}}+1 \\
& \frac{d y}{d x}=\frac{d}{d x}\left(x^{\frac{3}{2}}+2 x+2 x^{\frac{1}{2}}+1\right)=\frac{d}{d x}\left(x^{\frac{3}{2}}\right)+\frac{d}{d x}(2 x)+\frac{d}{d x}\left(2 x^{\frac{1}{2}}\right)+\frac{d}{d x}(1) \\
& =\frac{3}{2} x^{\frac{3}{2}}+2(1)+2 \frac{1}{2 \sqrt{x}}+0=\frac{3}{2} \sqrt{x}+2+\frac{1}{\sqrt{x}}
\end{aligned}
$$

Example 3: Differentiate $\frac{(\sqrt{x}+1)\left(x^{\frac{1}{x}}-1\right)}{x^{\frac{1}{x}}-x^{\frac{1}{x}}}$ with respect to $x$.

Solution: Let $y=\frac{(\sqrt{x}+1)\left(x^{\frac{1}{x}}-1\right)}{\sqrt{x}-x^{\frac{1}{x}}}$

$$
\begin{aligned}
& =\frac{(\sqrt{x}+1)\left(x^{\frac{1}{x}}-1\right)}{\sqrt{x}(x-1)} \\
& =\frac{(\sqrt{x}+1)(\sqrt{x}-1)(x+\sqrt{x}+1)}{\sqrt{x}(\sqrt{x}-1)} \quad \frac{(x-1)(x+\sqrt{x}+1)}{\sqrt{x}(\sqrt{x}-1)} \\
& =\frac{x+\sqrt{x}+1}{\sqrt{x}}
\end{aligned}
$$

Differentiating with respect to $x$, we have

$$
\begin{aligned}
& \frac{d y}{d x}=\frac{d}{d x}\left[\frac{x+\sqrt{x}+1}{\sqrt{x}}\right] \\
& =\frac{\sqrt{x}}{d x} \frac{d}{(x+\sqrt{x}+1)-(x+\sqrt{x}+1)}=\frac{d}{d x}(\sqrt{x}) \\
& =\frac{\sqrt{x}\left(1+\frac{1}{2} x^{-\frac{1}{2}}+0\right)-(x+\sqrt{x}+1)\left(\frac{1}{2} x^{-\frac{1}{2}}\right)}{x} \\
& =\frac{\sqrt{x}\left(1+\frac{1}{2 \sqrt{x}}\right)-(x+\sqrt{x}+1)}{x}
\end{aligned}
$$

$$
=\frac{\sqrt{x}\left(\frac{2 \sqrt{x}+1}{2 \sqrt{x}}\right)-\frac{x+\sqrt{x}+1}{2 \sqrt{x}}}{x} \quad \frac{2 x+\sqrt{x}-x-\sqrt{x}-1}{x \cdot 2 \sqrt{x}} \quad \frac{x-1}{2 x^{\frac{1}{x}}}
$$

Example 4: Differentiate $\frac{2 x^{3}-3 x^{2}+5}{x^{2}+1}$ with respect to $x$.
Solution: Let $\phi(x)=\frac{2 x^{3}-3 x^{2}+5}{x^{2}+1}$. Then we take

$$
f(x)=2 x^{3}-3 x^{2}+5 \text { and } g(x)=x^{2}+1
$$

Now $\quad f^{\prime}(x)=\frac{d}{d x}\left[2 x^{3}-3 x^{2}+5\right]=2\left(3 x^{2}\right)-3(2 x)+0=6 x^{2}-6 x$
and

$$
g^{\prime}(x)=\frac{d}{d x}\left[x^{2}+1\right]=2 x+0=2 x
$$

Using the quotient formula: $\phi^{\prime}(x)=\frac{f^{\prime}(x) g(x)-f(x) g^{\prime}(x)}{[g(x)]^{3}}$, we obtain

$$
\begin{aligned}
\frac{d}{d x}\left[\frac{2 x^{3}-3 x^{2}+5}{x^{2}+1}\right] & =\frac{\left(6 x^{2}-6 x\right)\left(x^{2}+1\right)-\left(2 x^{3}+3 x^{2}+5\right)(2 x)}{\left(x^{2}+1\right)^{3}} \\
& =\frac{6 x^{4}-6 x^{3}+6 x^{2}-6 x-\left(4 x^{4}-6 x^{3}+10 x\right)}{\left(x^{2}+1\right)^{3}} \\
& =\frac{6 x^{4}-6 x^{3}+6 x^{2}-6 x-4 x^{4}+6 x^{3}-10 x}{\left(x^{2}+1\right)^{3}} \\
& =\frac{2 x^{4}+6 x^{2}-16 x}{\left(x^{2}+1\right)^{3}}
\end{aligned}
$$

## EXERCISE 2.3

Differentiate w.r.t. $x$

1. $x^{4}+2 x^{3}+x^{2}$
2. $x^{-3}+2 x^{-2 / 3}+3$
3. $\frac{a+x}{a-x}$

4. $\frac{2 x-3}{2 x+1}$
5. $(x-5)(3-x)$
6. $\left(\sqrt{x}-\frac{1}{\sqrt{x}}\right)^{2}$
7. $\frac{(1+\sqrt{x})\left(x-x^{2}\right)}{\sqrt{x}}$
8. $\frac{\left(x^{2}+1\right)^{2}}{x^{2}-1}$
9. $\frac{x^{2}+1}{x^{2}-3}$
9. $\frac{\sqrt{1+x}}{\sqrt{1-x}}$
10. $\frac{2 x-1}{\sqrt{x^{2}+1}}$
11. $\sqrt{\frac{a-x}{a+x}}$
12. $\frac{\sqrt{x^{2}+1}}{\sqrt{x^{2}-1}}$
13. $\frac{\sqrt{1+x}-\sqrt{1-x}}{\sqrt{1+x}+\sqrt{1-x}}$
14. $\frac{x \sqrt{a+x}}{\sqrt{a-x}}$
15. If $y=\sqrt{x}-\frac{1}{\sqrt{x}}$, show that $2 \frac{d y}{d x}+y=2 \sqrt{x}$
16. If $y=x^{4}+2 x^{2}+2$, prove that $\frac{d y}{d x}=4 x \sqrt{y-1}$

### 2.4 THE CHAIN RULE

The composition fog of functions $f$ and $g$ is the function whose values $f(g(x))$, are found for each $x$ in the domain of $g$ for which $g(x)$ is in the domain of $f(f(g(x)))$ is read as $f$ of $g$ of $x$ ).

Theorem. If $g$ is differentiable at the point $x$ and $f$ is differentiable at the point $g(x)$ then the composition function fog is differentiable at the point $x$ and $(\text { fog })^{*}(x)=f^{*}[g(x)] \cdot g^{*}(x)$. The proof of the chain rule is beyond the scope of this book.

$$
\begin{aligned}
& \text { If } y=(\text { fog })(x)=f[g(x)], \text { then } \\
& \qquad(\text { fog })^{*}(x)=\frac{f}{x} f[g(x)]^{\frac{1}{2}} \cdot \frac{d y}{d x} \\
& \Rightarrow \frac{d y}{d x}=f^{*}[g(x)] \cdot g^{*}(x) \\
& \text { Let } u=g(x) \\
& \text { Then } y=f(u)
\end{aligned}
$$

Differentiating (ii) and (iii) w.r.t $x$ and $u$ respectively, we have.

$$
\frac{d u}{d x}=\frac{d}{d x}[g(x)]=g^{*}(x)
$$

and $\frac{d y}{d u}=\frac{d}{d u}[f(u)]=f^{*} u$
Thus (i) can be written in the following forms
(a) $\frac{d}{d x}(f(u))=f^{*}(u) \frac{d u}{d x}$
(b) $\frac{d y}{d u}=\frac{d y}{d u} \frac{d u}{d x}$

The proof of the Chain rule is beyond the scope of this book.

$$
\begin{aligned}
& \text { Note: 1. Let } y=\frac{1}{2} g(x)^{\frac{1}{2}} \text { and } u \quad g(x) \\
& \text { Then } y=u^{4} \text { and } \frac{d y}{d u}=n u^{n-1} \quad \text { (power rule) } \\
& \text { But } \frac{d y}{d x}=\frac{d y}{d u} \frac{d u}{d x}=n u^{n-1} \frac{d u}{d x} \\
& \text { or } \frac{d}{d x}[g(x)]^{n}=n[g(x)]^{\frac{n-1}{2}} \cdot g^{*}(x) \quad\left(1 \cdot \frac{d u}{d x}=g^{*}(x)\right)
\end{aligned}
$$

2. Reciprocal rule can be written as

$$
\begin{aligned}
\frac{d}{d x}\left(\frac{1}{g(x)}\right)=\frac{d}{d x}[g(x)]^{-1} & =-1 \cdot[g(x)]^{-1.5} \cdot g^{*}(x) \\
& =(-1)[g(x)]^{-1} \cdot g^{*}(x)
\end{aligned}
$$

Example 1: Find the derivative of $\left(x^{2}+1\right)^{n}$ with respect to

Solution: $\quad$ Let $y=\left(x^{2}-1\right)^{2}+$ and $u \neq 1$ Then $y \quad u^{n}$

$$
\text { Now } \frac{d u}{d x}=a x^{2} \text { and } \frac{d y}{d u} \quad 9 u^{4}
$$

Using the formula $\frac{d y}{d x}=9 u^{2} \frac{d u}{d x}$, we have
or $\quad \frac{d}{d x}\left(x^{2}+1\right)^{4}=9\left(x^{2}+1\right)^{4}\left(3 x^{2}\right) \quad\left(\because u=x^{2}+1\right.$ and $\left.\frac{d u}{d x}=3 x^{2}\right)$

$$
=27 x^{2}\left(x^{2}+1\right)^{4}
$$

Example 2: $\quad$ Differentiate $\sqrt{\frac{a-x}{a+x}},(x \neq-a)$ with respect to $x$
Solution: $\quad$ Let $\quad y=\sqrt{\frac{a-x}{a+x}}$ and $u=\frac{a-x}{a+x}$. Then $y \quad u^{\frac{1}{2}}$

$$
\text { Now } \frac{d y}{d u}=\frac{1}{2} u^{\frac{1}{2}-1}=\frac{1}{2} u^{-\frac{1}{2}}
$$

and $\frac{d u}{d x}=\frac{d}{d x}\left[\frac{a-x}{a+x}\right]=\frac{\left[\frac{d}{d x}(a-x)\right](a+x)-(a-x)\left[\frac{d}{d x}(a+x)\right]}{(a+x)^{2}}$

$$
=\frac{(0-1)(a+x)-(a-x)(0+1)}{(a+x)^{2}} \quad \frac{-a-x-a+x}{(a+x)^{2}} \quad \frac{-2 a}{(a+x)^{2}}
$$

Using the formula $\quad \frac{d y}{d x}=\frac{d y}{d u} \frac{d u}{d x}$, we have

$$
\begin{aligned}
\frac{d}{d x}\left(\sqrt{\frac{a-x}{a+x}}\right) & =\frac{1}{2} u^{-\frac{1}{2}}\left[\frac{-2 a}{(a+x)^{2}}\right]=\frac{1}{2}\left(\frac{a-x}{a+x}\right)^{-\frac{1}{2}} \times \frac{-2 a}{(a+x)^{2}}\left(\because u=\frac{a-x}{a+x}\right) \\
& =\frac{(a-x)^{-\frac{1}{2}}}{(a+x)^{-\frac{1}{2}}} \times \frac{-a}{(a+x)^{2}}=\frac{-a}{(a-x)^{\frac{1}{2}}(a+x)^{\frac{1}{2}}}
\end{aligned}
$$

Example 3: $\quad$ Find $\frac{d y}{d x}$ if $y=\frac{\sqrt{a+x}+\sqrt{a-x}}{\sqrt{a+x}-\sqrt{a-x}} \quad(x \neq 0)$
Solution: $\quad y=\frac{\sqrt{a+x}}{\sqrt{a+x}-\sqrt{a-x}}$
Multiplying the numerator and the denominator by $\sqrt{a+x}-\sqrt{a-x}$, gives

$$
\begin{aligned}
y & =\frac{(\sqrt{a+x}+\sqrt{a-x})(\sqrt{a+x}-\sqrt{a-x})}{(\sqrt{a+x}-\sqrt{a-x})(\sqrt{a+x}-\sqrt{a-x})} \\
& =\frac{(\sqrt{a+x})^{\frac{1}{2}}-(\sqrt{a-x})^{\frac{1}{2}}}{(a+x)+(a-x)-2 \sqrt{a^{2}-x^{2}}}-\frac{(a+x)-(a-x)}{2 a-2 \sqrt{a^{2}-x^{2}}} \quad \frac{2 x}{2\left(a-\sqrt{a^{2}-x^{2}}\right)}
\end{aligned}
$$

that is, $y=\frac{x}{a-\sqrt{a^{2}-x^{2}}}$
Let $f(x)=x$ and $g(x)=a-\sqrt{a^{2}-x^{2}}$, then
$f(x)^{x}=1$ and $\cdot g^{\prime}(x)=\theta \cdot \frac{d}{d x}\left(\boldsymbol{\alpha}^{2} \quad \boldsymbol{\alpha}^{2}\right)^{\frac{1}{2}} \quad \frac{1}{2}\left(a^{2} \quad-\boldsymbol{\alpha}^{2}\right)^{\frac{1}{2}-1} \frac{d}{d x}\left(a^{2} \quad x^{2}\right)$

$$
--=\frac{1}{2 \sqrt{a^{2}-x^{2}}} \times(2 \alpha) \frac{x}{\sqrt{a^{2}-x^{2}}}
$$

Using the formula $\frac{d y}{d x}=\frac{f^{\prime}(x) g(x)-f(x) g^{\prime}(x)}{[g(x)]^{4}}$, we have

$$
\begin{aligned}
\frac{d y}{d x} & =\frac{1 \cdot\left(a-\sqrt{a^{2}-x^{2}}\right)-x \cdot \sqrt{a^{2}-x^{2}}}{\left(a-\sqrt{a^{2}-x^{2}}\right)} \\
& =\frac{a \sqrt{a^{2}-x^{2}}-\left(a^{2}-x^{2}\right)-x^{2}}{\sqrt{a^{2}-x^{2}}\left(a-\sqrt{a^{2}-x^{2}}\right)^{2}}-\frac{a \sqrt{a^{2}-x^{2}}-a^{4}}{\sqrt{a^{2}-x^{2}}\left(a-\sqrt{a^{2}-x^{2}}\right)^{4}}
\end{aligned}
$$

$$
=\frac{-a\left(a-\sqrt{a^{2}-x^{2}}\right)}{\sqrt{a^{2}-x^{2}}\left(a-\sqrt{a^{2}-x^{2}}\right)^{2}}=\frac{-a}{\sqrt{a^{2}-x^{2}}\left(a-\sqrt{a^{2}-x^{2}}\right)^{2}}
$$

Example 4: $\quad$ Find $\frac{d y}{d x}$ if $y=(1+2 \sqrt{x})^{\frac{1}{2}} \cdot x^{\frac{3}{2}}$
Solution: $y=\left(\begin{array}{lll}1 & \text { a } \sqrt{\pi}\end{array}\right)^{\frac{1}{2}} \cdot x^{\frac{3}{2}}\left[\left(\begin{array}{lll}1 & 2 \sqrt{x}\end{array}\right)\left(x^{\frac{1}{2}}\right)\right]^{\frac{1}{2}}$
Let $\quad u=(1+2 \sqrt{x}) \cdot x^{\frac{1}{2}}$
Then $\quad y=u^{3}$
Differentiating (ii) with respect to $u$, we have

$$
\frac{d y}{d x}=3 u^{2} \quad 3\left[\left(\begin{array}{ll}
1 & 2 \sqrt{x}
\end{array}\right) x^{\frac{1}{2}}\right]^{2} \quad 3\left(\begin{array}{ll}
1 & 2 \sqrt{x}
\end{array}\right)^{2} \cdot x
$$

Differentiating (i) with respect to $x$, gives

$$
\begin{aligned}
& \frac{d u}{d x}=\left(0+2 \cdot \frac{1}{2 \sqrt{x}}\right) x^{\frac{1}{2}}+(1+2 \sqrt{x}) \frac{1}{2 \sqrt{x}} \\
& \quad=1 \quad \frac{1+2 \sqrt{x}}{2 \sqrt{x}} \quad \frac{2 \sqrt{x}+1+2 \sqrt{x}}{2 \sqrt{x}} \quad \frac{1+4 \sqrt{x}}{2 \sqrt{x}}
\end{aligned}
$$

Using the formula $\frac{d y}{d x}=\frac{d y}{d u} \frac{d u}{d x}$, we have

$$
\begin{aligned}
\frac{d}{d x}\left[(1+2 \sqrt{x})^{2} \cdot x^{\frac{1}{2}}\right] & =3\left(\begin{array}{ll}
1 & 2 \sqrt{x}
\end{array}\right)^{2} \cdot x \cdot x\left(\frac{1+4 \sqrt{x}}{2 \sqrt{x}}\right) \\
& =\frac{3}{2}\left(\begin{array}{ll}
1 & 2 \sqrt{x}
\end{array}\right)^{2} \sqrt{x}\left(\begin{array}{ll}
1 & 4 \sqrt{x}
\end{array}\right) \\
& =-\left(\begin{array}{ll}
1 & 2 \sqrt{x}
\end{array}\right) \cdot\left(\begin{array}{ll}
\sqrt{x} & 4 x
\end{array}\right)
\end{aligned}
$$

Example 5: If $y=(a x+b)^{n}$ where $n$ is a negative integer, find $\frac{d y}{d x}$ using quotient theorem
Solution: Let $n=-m$ where $m$ is a positive integer. Then
version: 1.1

$$
y=(a x+b)^{n}=(a x+b)^{-m}=\frac{1}{(a x+b)^{m}}
$$

We first find $\frac{d}{d x}(a x+b)^{m}$. Let $u=a x \quad b$. Then

$$
\begin{aligned}
& \frac{d}{d x}(a x+b)^{m}=\frac{d}{d x}\left(u^{m}\right)=\frac{d}{d x}\left(u^{m}\right) \frac{d u}{d x} \quad \text { (using chain rule) } \\
& \quad=m u^{m-1} \times \mathrm{a}=\mathrm{m}\left(\begin{array}{ll}
a x & b
\end{array}\right)^{m-1} \cdot a \quad\left(\because \frac{d}{d x}(a x+b)=a\right)
\end{aligned}
$$

Now differentiating (i) w.r.t. ${ }^{x}$, we have

$$
\begin{aligned}
& \frac{d y}{d x}=\frac{d}{d x}\left[\frac{1}{(a x+b)^{m}}\right] \frac{\frac{d}{d x}(1) \cdot(a x+b)^{m}-1 \cdot \frac{d}{d x}(a x+b)^{m}}{\left[(a x+b)^{m}\right]^{m}} \\
& =\frac{0 \cdot(a x+b)^{m}-1 \cdot m(a x+b)^{m-1} \cdot a}{(a x+b)^{1 / m}} \\
& \quad-=\left(\begin{array}{ll}
m(a x & b)^{m-1} \cdot a
\end{array}\right) \times(a \neq b)^{-2 / m}+m(a x \quad b)^{m-1-2 / m} \cdot a \\
& \quad=(-m)(a x+b)^{-m-1} \cdot a+=n(a x \quad b)^{n-1} \cdot a=(\because \cdot m \quad n)
\end{aligned}
$$

Example 6: $\quad$ Find $\frac{d y}{d x}$ if $y=x^{n}$ where $n=\frac{p}{q}, q \neq 0$
Solution: Given that $y=x^{n}$ where $n=\frac{p}{q}, q \quad 0$, putting $n \quad \frac{p}{q}$, we have

$$
y=x^{\frac{p}{q}}
$$

Taking qth power of both sides of (i), we get

$$
y^{q}=x^{p}
$$

Differentiating both sides of (ii) w.r.t. ${ }^{x} x^{x}$, gives

$$
\begin{aligned}
& \frac{d}{d x}\left(y^{p}\right)=\frac{d}{d x}\left(x^{p}\right) \text { or } \frac{d}{d y}\left(y^{q}\right) \cdot \frac{d y}{d x}=\frac{d}{d x}\left(x^{p}\right) \text { (Using chain rule) } \\
& \Rightarrow \mathrm{q} \mathrm{y}^{p-1} \frac{d y}{d x}=\mathrm{px}^{p-1}
\end{aligned}
$$

Multiplying both sides of (iii) by $y$, we have

$$
\begin{aligned}
& q \cdot y^{p} \frac{d y}{d x}=p y x^{p-1} \text { or } \quad \text { q. } x^{p} \frac{d y}{d x}=p \cdot x^{p} \quad x^{p-1} \quad \text { (using (i) and (ii)) } \\
& \Rightarrow \frac{d y}{d x}=\frac{p}{q} \cdot \frac{1}{x^{p}} \cdot \frac{p}{x^{p}} x^{p-1}=\frac{p}{q} \times x^{\frac{p}{q} \times q \cdot x \cdot p} \\
& \quad \times \frac{p}{q} \times \frac{p}{q-1}=\mathrm{nx}^{n-1}\left[\cdot \frac{p}{q}=\mathrm{n}\right] \\
& \text { Thus } \frac{d}{d x}\left(x^{n}\right) \mathrm{n} x^{n-1} \text {. }
\end{aligned}
$$

### 2.5 DERIVATIVES OF INVERSE FUNCTIONS

If for each $x \in \mathrm{D}_{t}, f(x)=y$ and for each $y \in \mathrm{D}_{g}, g(x)=x$, then $f$ and $g$ are inverse of each other, that is,

$$
(g \text { of })(x)=g(f(x))=g(y)=x
$$

and $(f \text { o g })(y)=f(g(y))=f(x)=y$
Using chain rule, we can prove that

$$
f^{\prime}(x) \cdot g^{\prime}(y)=1
$$

$\Rightarrow f^{\prime}(x)=\frac{1}{g^{\prime}(y)}$
$\Rightarrow \frac{d y}{d x}=\frac{1}{\frac{d x}{d y}} \quad\left(\begin{array}{l}\cdot \cdot \quad f(x)=y \Rightarrow f^{\prime}(x)=\frac{d y}{d x} \\ \text { and } g(y)=x \Rightarrow g^{\prime}(y)=\frac{d x}{d y}\end{array}\right)$

### 2.6 DERIVATIVE OF A FUNCTION GIVEN IN THE FORM OF PARAMETRIC EQUATIONS

The equations $x=a t^{2}$ and $y=2 a t$ express $x$ and $y$ as function of $t$. Here the variable $t$ is called a parameter and the equations of $x$ and $y$ in terms of $t$ are called the parametric equations.

Now we explain the method of finding derivatives of functions given in the form of parametric equations by the following examples.

Example 1: $\quad$ Find $\frac{d y}{d x}$ if $x=a t^{2}$ and $y=2 a t$.

Solution: We use the chain rule to find $\frac{d y}{d x}$
Here $\frac{d y}{d t}=\frac{d}{d t}(2 a t)=2 a \cdot 1=2 a$
and $\frac{d x}{d t}=\frac{d}{d t}\left(a t^{2}\right)=a(2 t)=2 a t$
so $\quad \frac{d y}{d x}=\frac{d y}{d t} \cdot \frac{d t}{d x}=\frac{\frac{d y}{d t}}{\frac{d x}{d t}}=\frac{2 a}{2 a t}=\frac{2 a}{y} \quad(\because 2 \mathrm{a}=y)$
Eliminating $t$, we get $x=a\left(\frac{y}{2 a}\right)^{2}=a \cdot \frac{y^{2}}{4 a^{2}}=\frac{y^{2}}{4 a} \Rightarrow y^{2}=4 a x$
Differentiating both sides of (i) w.r.t. ' $x$ ' we have

$$
\begin{aligned}
& \frac{d}{d x}\left(y^{2}\right)=\frac{d}{d x}(4 a x) \\
& \frac{d}{d x}\left(y^{2}\right) \cdot \frac{d y}{d x}=4 a \cdot \frac{d}{d x}(x) \quad \Rightarrow 2 x \frac{d y}{d x}=4 a \text { (1) } \\
& \Rightarrow \frac{d y}{d x}=\frac{2 a}{y}
\end{aligned}
$$

Example 2: $\quad$ Find $\frac{d y}{d x}$ if $x 1-t^{2}$ and $y=3 t^{2}-2 t^{2}$.
Solution: Given that $x=1-t^{2} \ldots .$. (i) and $y=3 t^{2}-2 t^{2}$
Differentiating (i) w.r.t. ' $t$ ', we get

$$
\frac{d y}{d t}=\frac{d}{d t}\left(1-t^{2}\right)=\frac{d}{d t}(1)-\frac{d}{d t}\left(t^{2}\right)=0-2 t=-2 t
$$

Differentiating (ii) w.r.t. ' $t$ ', we have

$$
\begin{aligned}
& \frac{d y}{d t}=\frac{d}{d t}\left(3 t^{2}-2 t^{2}\right)=\frac{d}{d t}\left(3 t^{2}\right)=\frac{d}{d t}\left(2 t^{2}\right) \\
& =3(2 t)-2\left(3 t^{2}\right)=6 t-6 t^{2}=6 t(1-t)
\end{aligned}
$$

Applying the formula

$$
\begin{aligned}
& \frac{d y}{d x}=\frac{d y}{d t} \frac{d t}{d x}=\frac{\frac{d y}{d t}}{\frac{d t}{d t}} \\
& =\frac{6 t(1-t)}{-2 t}=-3(1-t)=3(t-1)
\end{aligned}
$$

Example 3: $\quad$ Find $\frac{d y}{d x}$ if $x=\frac{1-t^{2}}{1+t^{2}}, y=\frac{2 t}{1+t}$

Solution: Given that $x=\frac{\left(1+t^{2}\right)}{1+t^{2}}$
(i) and $y \quad \frac{2 t}{1+t^{2}}$
(ii)

Differentiating (i) w.r.t. ' $t$ ', we get

$$
\begin{aligned}
& \frac{d x}{d t}=\frac{d}{d t}\left(\frac{1-t^{2}}{1+t^{2}}\right)=\frac{\left(\frac{d}{d t}\left(1-t^{2}\right)\right)\left(1+t^{2}\right)-\left(1-t^{2}\right) \cdot \frac{d}{d t}\left(1+t^{2}\right)}{\left(1+t^{2}\right)^{2}} \\
& =\frac{(-2 t)\left(1+t^{2}\right)-\left(1-t^{2}\right)(2 t)}{\left(1+t^{2}\right)^{2}} \quad \frac{2 t\left(-1-t^{2}-1+t^{2}\right)}{\left(1+t^{2}\right)^{2}} \quad \frac{-4 t}{\left(1+t^{2}\right)^{2}}
\end{aligned}
$$

Differentiating (i) w.r.t. ' $t$ ', we have

$$
\begin{aligned}
\frac{d y}{d t} & =\frac{d}{d t}\left(\frac{2 t}{1+t^{2}}\right) \quad \frac{\left(\frac{d}{d t}(2 t)\right)\left(1+t^{2}\right)-2 t \times \frac{d}{d t}\left(1+t^{2}\right)}{\left(1+t^{2}\right)^{2}} \\
& =\frac{2\left(1+t^{2}\right)-2 t(2 t)}{\left(1+t^{2}\right)^{2}}=\frac{2+2 t^{2}-4 t^{2}}{\left(1+t^{2}\right)^{2}} \quad \frac{2-2 t^{2}}{\left(1+t^{2}\right)^{2}} \quad \frac{2\left(1-t^{2}\right)}{\left(1+t^{2}\right)^{2}} \\
\frac{d y}{d x} & =\frac{d y}{d t} \frac{d t}{d x}=\frac{\frac{d y}{d t}}{\frac{d t}{d x}}=\frac{\frac{2\left(1-t^{2}\right)}{\left(1+t^{2}\right)^{2}}}{\frac{4 t}{\left(1+t^{2}\right)^{2}}}=\frac{2\left(1-t^{2}\right)}{-4 t}=\frac{t^{2}-1}{2 t}
\end{aligned}
$$

### 2.7 Differentiation of Implicit Relations

Sometimes the functional relation is not explicitly expressed in the form $y=f(x)$ but an equation involving $x$ and $y$ is given. To find $\frac{d y}{d x}$ from such an equation, we differentiate each term of the equation and use the chain rule where it is required. The process of finding $\frac{d y}{d x}$ in this way, is called implicit differentiation. We explain the implicit differentiation in the following examples.

Example 1: $\quad$ Find $\frac{d y}{d x}$ if $x^{2}+y^{2}=4$
Solution: Here $x^{2}+y^{2}=4$
Differentiating both sides of (i) w.r.t. ' $x$ ', we get

$$
\begin{aligned}
& 2 x+2 y \frac{d y}{d x}=0 \\
& \text { or } x+y \frac{d y}{d x}=0 \Rightarrow \frac{d y}{d x}=\frac{x}{y}
\end{aligned}
$$

Solving (i) for $y$ in terms of $x$, we have
$y \equiv \sqrt{4 x^{2}}$
$\Rightarrow y=\sqrt{4-x^{2}}$
(ii)
or $y \equiv \sqrt{4 x^{2}}$
(iii)
$\frac{d y}{d x}$ found above represents the derivative of each of functions defined as in $d x$ (ii) and (iii)

From (ii) $\frac{d y}{d x}=\frac{1}{2 \sqrt{4-x^{2}}} \times(-2 x)=\frac{x}{\sqrt{4-x^{2}}}$

$$
=-\frac{x}{y}\left(\because \sqrt{4-x^{2}=y}\right)
$$

From (iii) $\frac{d y}{d x}=-\frac{1}{2 \sqrt{4-x^{2}}} \times(-2 x)=-\frac{-x}{-\sqrt{4-x^{2}}}=-\frac{x}{y}(\because-\sqrt{4-x}=y)$

Example 2: Find $\frac{d y}{d x}$.if $y^{2}+x^{2}-4 x=5$.
Solution: Given that $y^{2}+x^{2}-4 x=5$
Differentiating both sides of (i) w.r.t. ' $x$ ', we get

$$
\begin{aligned}
& \frac{d}{d x}\left[y^{2}+x^{2}-4 x\right]=\frac{d}{d x}(5) \\
& \text { or } \quad 2 y \frac{d y}{d x}+2 x-4=0 \quad\left[\because \frac{d}{d x}\left(y^{2}\right)=\frac{d}{d x}\left(y^{2}\right) \frac{d y}{d x}=2 y \frac{d y}{d x}\right]
\end{aligned}
$$

$$
\Rightarrow \quad 2 y \frac{d y}{d x}=4-2 x \quad \Rightarrow \frac{d y}{d x}=\frac{2(2-x)}{2 y}=\frac{2-x}{y}
$$

Note: Solving (i) for $y$, we have

$$
y^{2}=5+4 x-x \quad \Rightarrow \quad y= \pm \sqrt{5+4 x-x^{2}}
$$

Thus $y=\sqrt{5+4 x-x^{2}}$
(ii)
or $\quad y=-\sqrt{5+4 x-x^{2}}$
(iv)

Each of these equations (iii) and (iv) defines a function.
Let $y=f_{1}(x)=\sqrt{5+4 x-x^{2}}$
and $y=f_{1}(x)=-\sqrt{5+4 x-x^{2}}$.
Differentiation (v) w.r.t. ' $x$ ', we get

$$
f_{1}^{\prime}(x)=\frac{1}{2}\left(5+4 x-x^{2}\right)^{-\frac{1}{2}} \times(4-2 x)=\frac{2-x}{\sqrt{5+4 x-x^{2}}}
$$

From (v), $\sqrt{5+4 x-x^{2}}=y, \quad$ so $\quad f_{1}^{\prime}(x) \quad \frac{2-x}{y}$
Also $f_{2}^{\prime}(x)=-\frac{1}{2}\left(5+4 x-x^{2}\right)^{-\frac{1}{2}} \times(4-2 x)=\frac{2-x}{-\sqrt{5+4 x-x^{2}}}$
From (vi) $-\sqrt{5+4 x-x^{2}}=y, \quad$ so $\quad f_{2}^{\prime}(x) \quad \frac{2-x}{y}$
Thus (ii) represents the derivative of $f_{1}(x)$ as well as that of $f_{2}(x)$.

Example 3: $\quad$ Find $\frac{d y}{d x}$ if $y^{2}-x y-x^{2}+4=0$.
Solution: Given that $y^{2}-x y-x^{2}+4=0$
Differentiating both sides of (i) w.r.t. ' $x$ ', gives

$$
\begin{aligned}
& \frac{d}{d x}\left(y^{2}-x y-x^{2}+4\right)=\frac{d}{d x}(0)=0 \\
& \text { or } \quad 2 y \frac{d y}{d x}-\left(1 . y+x \frac{d y}{d x}\right)-2 x+0=0 \\
& \Rightarrow \quad(2 y-x) \frac{d y}{d x}=2 x \quad y \quad \Rightarrow \frac{d y}{d x}=\frac{2 x+y}{2 y-x}
\end{aligned}
$$

Example 4: $\quad$ Find $\frac{d y}{d x}$ if $y^{2}-2 x y^{2}-x^{2} y+3 x=0$.
Solution: Differentiating both sides of the given equation w.r.t. ' $x$ ' we have

$$
\begin{aligned}
& \frac{d}{d x}\left(y^{2}-2 x y^{2}+x^{2} y+3 x\right)=\frac{d}{d x}(0)=0 \\
& \text { or } \quad \frac{d}{d x}\left(y^{2}\right)-\frac{d}{d x}\left(2 x y^{2}\right)+\frac{d}{d x}\left(x^{2} y\right)+\frac{d}{d x}(3 x)=0 \\
& \frac{d}{d x}\left(y^{2}\right)-2\left[1 . y^{2}+x \frac{d}{d x}\left(y^{2}\right)\right]+\left(2 x y+x^{2} \frac{d y}{d x}\right)+3=0
\end{aligned}
$$

Using the chain rule on $\frac{d}{d x}\left(y^{2}\right)$ and $\frac{d}{d x}\left(y^{2}\right)$, we have

$$
3 y^{2} \frac{d y}{d x}-2\left[y^{2}+x\left(2 x \frac{d y}{d x}\right)\right]+2 x y+x^{2} \frac{d y}{d x}+3=0
$$

or $\quad\left(3 y^{2}-4 x y+x^{2}\right) \frac{d y}{d x}=2 y^{2}-2 x y-3$
$\Rightarrow \quad \frac{d y}{d x}=\frac{2 y^{2}-2 x y-3}{3 y^{2}-4 x y+x^{2}}$
Example 5: Differentiate $x^{2}+\frac{1}{x^{2}}$ w.r.t. $x-\frac{1}{x}$
Solution: Let $y=x^{2} \frac{1}{x^{2}}$ and $u \quad x \frac{1}{x}$. Then

$$
\begin{aligned}
& \frac{d y}{d x}=2 x+(-2) \frac{1}{x^{2}}=2\left(x-\frac{1}{x^{2}}\right)=\frac{2\left(x^{2}-1\right)}{x^{2}}=\frac{2\left(x^{2}-1\right)\left(x^{2}+1\right)}{x^{2}} \\
& \text { and } \quad \frac{d u}{d x}=1-(-1) \frac{1}{x^{2}}=1+\frac{1}{x^{2}}=\frac{x^{2}+1}{x^{2}} \\
& \text { Thus } \frac{d y}{d u}=\frac{d y}{d x} \frac{d x}{d u}=\frac{2\left(x^{2}-1\right)\left(x^{2}+1\right)}{x^{2}} \times \frac{x^{2}}{x^{2}+1} \quad \frac{2\left(x^{2}-1\right)}{x} \quad 2\left(x \quad \frac{1}{x}\right)
\end{aligned}
$$

## EXERCISE 2.4

1. Find $\frac{d y}{d x}$ by making suitable substitutions in the following functions defined as:
(i) $y=\sqrt{\frac{1-x}{1+x}}$
(ii) $y=\sqrt{x+\sqrt{x}}$
(iii) $y=x \sqrt{\frac{a+x}{a-x}}$
(iv) $y=\left(3 x^{2}-2 x+7\right)^{6}$
(v) $\sqrt{\frac{a^{2}+x^{2}}{a^{2}-x}}$
2. Find $\frac{d y}{d x}$ if:
(i) $3 x+4 y+7=0$
(ii) $x y+y^{2}=2$
(iii) $x^{2}-4 x y-5 y=0$
(iv) $4 x^{2}+2 k x y+b y^{2}+2 g x+2 f y+c=0$
(v) $x \sqrt{1+y}+y \sqrt{1+x}=0$
(vi) $y\left(x^{2}-1\right)=x \sqrt{x^{2}+4}$
3. Find $\frac{d y}{d x}$ of the following parametric functions
(i) $x=\theta+\frac{1}{\theta}$ and $y=\theta+1$
(ii) $x=\frac{a\left(1-t^{2}\right)}{1+t^{2}}, y=\frac{2 b t}{1+t^{2}}$
4. Prove that $y \frac{d y}{d x}+x=0$ if $x=\frac{1-t^{2}}{1+t^{2}}, y=\frac{2 t}{1+t}$

5. Differentiate
(i) $x^{2}-\frac{1}{x^{2}}$ w.r.t $x^{4}$
(ii) $\left(1+x^{2}\right)^{n}$ w.r.t $x^{2}$
(iii) $\frac{x^{2}+1}{x^{2}-1}$ w.r.t $\frac{x-1}{x+1}$
(iv) $\frac{a x+b}{c x+d}$ w.r.t $\frac{a x^{2}+b}{a x^{2}+d}$
(v) $\frac{x^{2}+1}{x^{2}-1}$ w.r.t $x^{3}$

### 2.8 DERIVATIVES OF TRIGONOMETRIC FUNCTIONS

While finding derivatives of trigonometric functions, we assume that $x$ is measured in radians. The limit theorems $\lim _{x \rightarrow 0} \frac{\sin x}{x}=4$ and $\lim _{x \rightarrow 0} \frac{1-\cos x}{x} \quad 0$ are used to find the derivative formulas for $\sin x$ and $\cos x$.

We prove from first principle that

$$
\frac{d}{d x}(\sin x)=\cos x \text { and } \frac{d}{d x}(\cos x)=-\sin x
$$

Let $y=\sin x$ Then $y+\delta y=\sin (x+\delta x)$
and $\delta y=\sin (x+\delta x)-\sin x$

$$
\begin{aligned}
& =2 \cos \left(\frac{x+\delta x+x}{2}\right) \sin \left(\frac{x+\delta x-x}{2}\right)+2 \cos \left(x \frac{\delta x}{2}\right) \sin \left(\frac{\delta x}{2}\right) \\
& \frac{\delta y}{\delta x}=\frac{2 \cos \left(x+\frac{\delta x}{2}\right) \sin \left(\frac{\delta x}{2}\right)}{\frac{\delta x}{2}} \cdot \cos \left(x \frac{\delta x}{2}\right) \frac{\sin \left(\frac{\delta x}{2}\right)}{\frac{\delta x}{2}} \\
& \lim _{\delta x \rightarrow 0} \frac{\delta y}{\delta x}=\lim _{\delta x \rightarrow 0}\left[\cos \left(x+\frac{\delta x}{2}\right) \frac{\sin \left(\frac{\delta x}{2}\right)}{\frac{\delta x}{2}}\right]
\end{aligned}
$$

$$
\begin{aligned}
& =\lim _{\frac{\delta x}{2} \rightarrow 0} \cos \left(x \frac{\delta x}{2}\right) \lim _{\frac{\delta x}{2} \rightarrow 0} \frac{\sin \left(\frac{\delta x}{2}\right)}{\frac{\delta x}{2}} \cdot\left(\frac{-\frac{\delta x}{2}}{\text { when } \delta x \rightarrow 0}\right) \\
& \text { Thus } \frac{d y}{d x}=\cos x \text { d. }\left(\frac{1-\lim _{\delta x \rightarrow 0} \cos \left(x \frac{\delta x}{2}\right)}{\frac{\delta x}{2}} \cos x \text { and } \lim _{\delta x \rightarrow 0} \frac{\sin \frac{\delta x}{2}}{\frac{\delta x}{2}} 1\right)
\end{aligned}
$$

Let $y=\cos x$, then $y+\delta y=\cos (x+\delta x)$
and $\delta y=\cos (x+\delta x)-\cos x$

$$
\begin{aligned}
& =\cos x \cos \delta x-\sin x \sin \delta x-\cos x \\
& =\sin x \sin \delta x \cos x\left(\frac{1-\cos \delta x}{\delta x}\right) \\
& \frac{\delta y}{\delta x}=(\sin x) \cdot \frac{\sin \delta x}{\delta x} \cos x\left(\frac{1-\cos \delta x}{\delta x}\right) \\
& \lim _{\delta x \rightarrow 0} \frac{\delta y}{\delta x}=\lim _{\delta x \rightarrow 0}\left[(\sin x) \frac{\sin \delta x}{\delta x} \cos x\left(\frac{1-\cos \delta x}{\delta x}\right)\right] \\
& =\lim _{\delta x \rightarrow 0}\left[(-\sin x) \frac{\sin \delta x}{\delta x}\right]-\lim _{\delta x \rightarrow 0}\left[-\cos x\left(\frac{1-\cos \delta x}{\delta x}\right)\right]
\end{aligned}
$$

Thus $\frac{d y}{d x}=(\sin x) \cdot 1(\cos x)(0)$

$$
\left(\frac{1-\lim _{\delta x \rightarrow 0} \frac{\sin \delta y}{\delta x}=1 \text { and }}{\lim _{\delta x \rightarrow 0}\left(\frac{1-\cos \delta x}{\delta x}\right)=0\right)
$$

or $\frac{d}{d x}(\cos x)=-\sin x$
Now using $\frac{d}{d x}(\sin x)=\cos x$ and $\frac{d}{d x}(\cos x)=-\sin x$, we prove that

$$
\frac{d}{d x}(\sec x)=\sec x \tan x \quad \text { and } \quad \frac{d}{d x}(\cot x) \quad \operatorname{cosec}^{2} x
$$

$$
\begin{aligned}
& \text { Proof of } \frac{d}{d x}(s e c x)=s e c x \tan x \\
& \text { Let } \quad y=s e c x=\frac{1}{\cos x}
\end{aligned}
$$

Differentiating (i) w.r.t. ' $x$ ', we have

$$
\begin{aligned}
\frac{d}{d x}(y)= & \frac{d}{d x}\left[\frac{1}{\cos x}\right]=\frac{\left[\frac{d}{d x}(1)\right] \cos x-1 \cdot \frac{d}{d x}(\cos x)}{(\cos x)^{\prime}}\binom{\text { Using }}{\text { quotient }}(\text { formula }) \\
& =\frac{0 \cdot \cos x-1 \cdot(-\sin x)}{\cos ^{2} x} \\
& =\frac{1}{\cos x} \cdot \frac{\sin x}{\cos x} \quad \sec x \tan x
\end{aligned}
$$

Thus $\frac{d}{d x}(s e c x)=s e c x \tan x$
Proof of $\frac{d}{d x}(\cot x)=\cos e c^{2} x$
Let $\quad y=\cot x=\frac{\cos x}{\sin x}$
Differentiating (i) w.r.t. ' $x$ ', we get

$$
\begin{aligned}
\frac{d}{d x}(y)= & \frac{d}{d x}\left[\frac{\cos x}{\sin x}\right]=\frac{\left[\frac{d}{d x}(\cos x)\right] \sin x-\cos x \frac{d}{d x}(\sin x)}{(\sin x)^{\prime}}\binom{\text { Using }}{\text { quotient }}(\text { formula }) \\
& =\frac{(-\sin x) \sin x-\cos x(\cos x)}{\sin ^{2} x} \\
& =\frac{-\left(\sin ^{2} x+\cos ^{2} x\right)}{\sin ^{2} x}=\frac{1}{\sin ^{2} x} \quad \cos e c^{2} x
\end{aligned}
$$

Thus $\frac{d}{d x}(\cot x)=\cos e c^{2} x$

Now we write the derivatives of six trigonometric functions
(1) $\frac{d}{d x}(\sin x)=\cos x$
(2) $\frac{d}{d x}(\cos x)=\sin x$
(3) $\frac{d}{d x}(\tan x)=s e c^{2} x$
(4) $\frac{d}{d x}(\cot x)=-\cos e c^{2} x$
(5) $\frac{d}{d x}(\operatorname{cosec} x)=-\operatorname{cosec} x \cot x$
(6) $\frac{d}{d x}(\sec x)=\sec x \tan x$

Example 1: Find the derivative of $\tan x$ from first principle.
Solution: Let $y=\tan x$, then $+y \quad \delta x \quad \tan (x \quad \delta x)$ and

$$
\begin{aligned}
& \delta y=y+\delta x-y=\tan (x+\delta x)-\tan x \\
& =\frac{\sin (x+\delta x)}{\cos (x+\delta x)} \cdot \frac{\sin x}{\cos x}=\frac{\sin (x+\delta x) \cos x-\cos (x+\delta x) \sin x}{\cos (x+\delta x) \cos x} \\
& =\frac{\sin (x+\delta x-x)}{\cos (x+\delta x) \cdot \cos x} \cdot \frac{\sin \delta x}{\cos (x+\delta x) \cos x} \\
& \frac{\delta y}{\delta x}=\frac{1}{\cos (x+\delta x) \cdot \cos x} \cdot \frac{\sin \delta x}{\delta x} \\
& \text { or } \quad \lim _{\delta x \rightarrow 0} \frac{\delta y}{\delta x}=\lim _{\delta x \rightarrow 0}\left(\frac{1}{\cos (x+\delta x) \cdot \cos x}\right) \lim _{\delta x \rightarrow 0}\left(\frac{\sin \delta x}{\delta x}\right) \\
& \text { Thus } \frac{d y}{d x}=\frac{1}{(\cos x)(\cos x)} \cdot 1 \quad \sec ^{2} x \quad\binom{\because \lim _{\delta x \rightarrow 0} \cos (x+\delta x)=\cos x}{ \text { and } \lim _{\delta x \rightarrow 0} \frac{\sin \delta x}{\delta x}=1}
\end{aligned}
$$

Thus $\frac{d y}{d x}=\sec ^{2} x$
or
$\frac{d}{d x}(\tan x)=\sec ^{2} x$

Example 2: Differentiate ab-initio w.r.t. ' $x$ '
(i) $\cos 2 x$
(ii) $\sin \sqrt{x}$
(iii) $\cot ^{2} x$

Solution: (i) Let $y=\cos 2 x$, then $y+\delta y=\cos 2(x+\delta x)$
and $\delta y=\cos (2 x+2 \delta x)-\cos 2 x$

$$
=2 \sin \frac{2 x+2 \delta x+2 x}{2} \sin \frac{2 x+2 \delta x-2 x}{2}=\geqslant \sin (2 x \quad \delta x) \sin \delta x
$$

Now $\frac{\delta y}{\delta x}=\geqslant \sin (2 x \quad \delta x) \cdot \frac{\sin \delta x}{\delta x}$
Thus $\frac{d y}{d x}=\lim _{\delta x \rightarrow 0}\left[\begin{array}{ll}2 \sin (2 x & \delta x) \cdot \frac{\sin \delta x}{\delta x}\end{array}\right]$

$$
=\geqslant \lim _{\delta x \rightarrow 0}(\sin 2 x \quad \delta x) \cdot \lim _{\delta x \rightarrow 0} \frac{\sin \delta x}{\delta x}
$$

$=(2 \sin 2 x) \cdot 1 \quad 2 \sin 2 x\left(\because \lim _{\delta x \rightarrow 0} \sin (2 x+\delta x)=\sin 2 x\right.$ and $\left.\lim _{\delta x \rightarrow 0} \frac{\sin \delta x}{\delta x} 1\right)$
(ii) Let $y=\sin \sqrt{x}$, then $y+\delta y=\sin \sqrt{x \quad \delta x}$
and $\delta y=\sin \sqrt{x+\delta x}-\sin \sqrt{x}$

$$
=2 \cos \left(\frac{\sqrt{x+\delta x}+\sqrt{x}}{2}\right) \sin \left(\frac{\sqrt{x+\delta x}-\sqrt{x}}{2}\right)
$$

As $(\sqrt{x+\delta x}+\sqrt{x})(\sqrt{x+\delta x}-\sqrt{x})=(x+\delta x)-x=\delta x$,
So $\frac{\delta y}{\delta x}=2 \cos \left(\frac{\sqrt{x+\delta x}+\sqrt{x}}{2}\right) \frac{\sin \left(\frac{\sqrt{x+\delta x}-\sqrt{x}}{2}\right)}{\delta x}$

$$
=\frac{2 \cos \left(\frac{\sqrt{x+\delta x}+\sqrt{x}}{2}\right) \sin \left(\frac{\sqrt{x+\delta x}-\sqrt{x}}{2}\right)}{(\sqrt{x+\delta x}+\sqrt{x})(\sqrt{x+\delta x}-\sqrt{x})}
$$

version: 1.1

$$
\frac{\cos \left(\frac{\sqrt{x+\delta x}+\sqrt{x}}{2}\right)}{\sqrt{x+\delta x}+\sqrt{x}} \frac{\sin \left(\frac{\sqrt{x+\delta x}-\sqrt{x}}{2}\right)}{\frac{\sqrt{x+\delta x}-\sqrt{x}}{2}}
$$

Thus $\frac{d y}{d x}=\lim _{\delta x \rightarrow 0}\left(\frac{\cos \frac{\sqrt{x+\delta x}+\sqrt{x}}{2}}{\sqrt{x+\delta x}+\sqrt{x}}\right) \frac{\lim _{\sqrt{x+\delta x}-\sqrt{x}}}{2} \quad 0\left(\frac{\sin \left(\frac{\sqrt{x+\delta x}-\sqrt{x}}{2}\right)}{\frac{\sqrt{x+\delta x}-\sqrt{x}}{2}}\right)$
$\frac{d y}{d x}=\left(\frac{\cos \frac{\sqrt{x}+\sqrt{x}}{2}}{\sqrt{x+\sqrt{x}}}\right) \cdot 1 \quad \frac{\cos \sqrt{x}}{2 \sqrt{x}} \quad\left(\because \frac{\sqrt{x+\delta x}-\sqrt{x}}{2} \rightarrow 0\right.$ when $)$
(iii) Let $y=\cot ^{2} x$, then

$$
\begin{aligned}
& y+\delta y=\cot ^{2}(x+\delta x) \\
& \delta y=\cot ^{2}(x+\delta x)-\cot ^{2} x=[\cot (x+\delta x)+\cot x] \times[\cot (x-\delta x) \cot x] \\
&=[\cot (x+\delta x)+\cot x]\left(\frac{\cos (x+\delta x)}{\sin (x+\delta x)} \frac{\cos x}{\sin x}\right) \\
&=[\cot (x+\delta x)+\cot x] \times \frac{\sin x \cos (x+\delta x)-\cos x \sin (x+\delta x)}{\sin (x+\delta x) \sin x} \\
& \frac{\delta y}{\delta x}=\left(\frac{\cot (x+\delta x)+\cot x}{\sin (x+\delta x) \sin x}\right) \frac{-\sin \delta x}{\delta x}\binom{\sin x \cos (x+\delta x)-\cos x \sin (x+\delta x)}{=\sin (x-(x+\delta x))=\sin (-\delta x)=-\sin \delta x} \\
& \lim _{\delta x \rightarrow 0} \frac{\delta y}{\delta x}=\lim _{\delta x \rightarrow 0}\left(\frac{\cot (x+\delta x)+\cot x}{\sin (x+\delta x) \sin x} \cdot(1) \frac{\sin \delta x}{\delta x}\right) \\
& \text { Thus } \frac{d y}{d x}=\frac{\cot x+\cot x}{\sin x \sin x} \cdot(1) \cdot 1 \quad\left(\frac{\because \lim _{\delta x \rightarrow 0} \cot (x+\delta x)=\cot x}{\text { and } \lim _{\delta x \rightarrow 0} \sin (x+\delta x)=\sin x}\right) \\
& =\frac{-2 \cot x}{\sin ^{2} x} \cdot 1=-2 \cot x \cos \sec ^{2} x
\end{aligned}
$$

Example 3: Differentiate $\sin ^{3} x$ w.r.t. $\cos ^{2} x$
Solution: Let $y=\sin ^{3} x$ and $u \cos ^{2} x$

$$
\begin{aligned}
& \text { Now } \quad \frac{d y}{d x}=3 \sin ^{4} x \cos x \quad \text { and } \quad \frac{d u}{d x}-2 \cos x(\sin x) \\
& \text { Thus } \frac{d y}{d u}=\frac{d y}{d x} \frac{d x}{d u}=\left(3 \sin ^{4} x \cos x\right) \cdot \frac{1}{-2 \cos x \sin x}\left(\because \frac{d x}{d u} \cdot \frac{1}{\frac{d x}{d u}}\right) \\
& =-\frac{3}{2} \sin x .
\end{aligned}
$$

### 2.9 DERIVATIVES OF INVERSE TRIGONOMETRIC FUNCTIONS

Here we want to prove that

1. $\frac{d}{d x}\left[\sin ^{-1} x\right]=\frac{1}{\sqrt{1-x^{2}}}$,
$x \in(-1,1)$ or $-1<x<1$
2. $\frac{d}{d x}\left[\operatorname{Cos}^{-1} x\right]=\frac{1}{\sqrt{1-x^{2}}}$,
$x \in(-1,1)$ or $-1<x<1$
3. $\frac{d}{d x}\left[\operatorname{Tan}^{-1} x\right]=-\frac{1}{1+x^{2}}$,
$x \in R$
4. $\frac{d}{d x}\left[\operatorname{Cosec}^{-1} x\right]=-\frac{1}{|x| \sqrt{x^{2}-1}}$,
$x \in[-1,1]^{4},[-1,1]^{4}=(-\infty,-1) \cup(1, \infty)$
5. $\frac{d}{d x}\left[\operatorname{Sec}^{-1} x\right]=-\frac{1}{|x| \sqrt{x^{2}-1}}$,
$x \in[-1,1]^{4},[-1,1]^{4}=(-\infty,-1) \cup(1, \infty)$
6. $\frac{d}{d x}\left[\operatorname{Cos}^{-1} x\right]=-\frac{1}{1+x^{2}}$,
$x \in R$

Proof of (1). Let $y=\operatorname{Sin}^{-1} x$
(1).

Then $\quad x=\operatorname{Sin} y$ or $x \sin y$ for $y\left[\frac{\pi}{2}, \frac{\pi}{2}\right]$
Differentiating both sides of (ii) w.r.t. ' $x$ ', we get

$$
\begin{aligned}
& 1=\frac{d}{d x}(\sin y)=\frac{d}{d x}(\sin y) \frac{d y}{d x}=\cos y \frac{d y}{d x} \\
& \Rightarrow \quad \frac{d y}{d x}=\frac{1}{\cos y} \text { for } \quad y\left(\frac{\pi}{2}, \frac{\pi}{2}\right) \\
& =\frac{1}{\sqrt{1-\sin ^{2} y}} \quad[\because \cos y \text { is positive for } y \in\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)]
\end{aligned}
$$

Thus $\frac{d}{d x}\left(\sin ^{-1} x\right)=\frac{1}{\sqrt{1-x^{2}}}<$ for $\quad 1 \quad x \quad 1$
Proof of (2). Let $y=\operatorname{Cos}^{-1} x$
Then $\quad x=\operatorname{Cos} y$ or $x \cos y$ for $y[0, \pi]$
Differentiating both sides of (ii) w.r.t. ' $x$ ', gives

$$
\begin{aligned}
& 1=\frac{d}{d x}(\cos y)=\frac{d}{d x}(\cos y) \frac{d y}{d x}-\sin y \frac{d y}{d x} \\
& \Rightarrow \quad \frac{d y}{d x}=\frac{1}{\sin y} \quad \text { for } \quad y \in(0, \pi) \\
& \quad=\frac{1}{\sqrt{1-\cos ^{2} y}} \quad[\because \sin y \text { is positive for } y \in(0, \pi)]
\end{aligned}
$$

Thus $\frac{d}{d x}\left(\operatorname{Cos}^{-1} x\right)=-\frac{1}{\sqrt{1-x^{2}}}$ for $\quad 4 \quad \alpha \quad 4$
Proof of (3). Let $y=\operatorname{Tan}^{-1} x$
Then $\quad x=$ Tan $y$ or $x=\tan y$ for $y\left(\frac{\pi}{2}, \frac{\pi}{2}\right)$
Differentiating both sides of (ii) w.r.t. ' $x$ ', we have

$$
\begin{aligned}
& 1=\frac{d}{d x}(\tan y)=\frac{d}{d x}(\tan y) \frac{d y}{d x}=s e c^{2} y \frac{d y}{d x} \\
\Rightarrow & \frac{d y}{d x}=\frac{1}{\sec ^{2} y} \quad \text { for } \quad y \quad\left(\frac{\pi}{2}, \frac{\pi}{2}\right) \\
& =\frac{1}{1+\tan ^{2} y}=\frac{1}{1+x^{2}} \quad \text { for } \quad x \in R
\end{aligned}
$$

Thus $\frac{d}{d x}\left(\operatorname{Tan}^{-1} x\right)=\frac{1}{1+x^{2}}$ for $x \quad R$
Proof of (4). Let $y=\operatorname{Cosec}^{-1} x$
Then $\quad x=\operatorname{Gosec} y$ or $x \quad \cos \operatorname{ec} y$ for $y\left[\frac{\pi}{2}, \frac{\pi}{2}\right] \quad\{0\}$
$\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]-\{0\}$ is also written as $\left[-\frac{\pi}{2} 0\right] \cup\left[0, \frac{\pi}{2}\right]$
Differentiating both sides of (ii) w.r.t. ' $x$ ', we get

$$
\begin{aligned}
& 1=\frac{d}{d x}(\operatorname{cosec} y) \quad \frac{d}{d x}\left(\operatorname{cosec} y\right) \frac{d y}{d x} \\
& =\left(-\operatorname{cosec} y \cot y\right) \frac{d y}{d x} \\
\Rightarrow \quad & \frac{d y}{d x}=-\frac{1}{\operatorname{cosec} y \cot y} \quad \text { for } \quad y \in\left[\frac{\pi}{2}, \frac{\pi}{2}\right]-\{0\}
\end{aligned}
$$

When $y \in\left(0, \frac{\pi}{2}\right)$, cosecy and $\cot y$ are positive.
As $\operatorname{cosec} y=x$, so $x$ is positive in this case
and $\cot y=\sqrt{\operatorname{cosec}^{2} y-1}=\sqrt{x^{2}-1} \quad$ for all $x>1$
Thus $\frac{d}{d x}\left(\operatorname{Cosec}^{-1} x\right)=\frac{-1}{x \sqrt{x^{2}-1}} \quad$ for $\quad x \quad 1$

When $y \in\left(-\frac{\pi}{2}, 0\right)$, cosec $y$ and $\cot y$ are negative
As $\operatorname{cosec} y=x$, so $x$ is negative in this case
and $\cot y=-\sqrt{\operatorname{cosec}^{2} y-1}=-\sqrt{x^{2}-1} \quad$ when $x<-1$

$$
\begin{aligned}
& \text { Thus } \frac{d}{d x}\left[\operatorname{Cosec}^{-1} x\right]=\frac{-1}{x\left(-\sqrt{x^{2}-1}\right)} \quad(x \quad 1) \\
& =\frac{-1}{(-x) \sqrt{x^{2}-1}} \quad(x \quad 1) \\
& \frac{d}{d x}\left[\operatorname{cosec}^{-1} x\right]=-\frac{1}{|x| \sqrt{x^{2}-1}} \quad \text { for } \quad x \in[-1,1]^{r}
\end{aligned}
$$

Proof of (5). is left as an exercise
Proof of (6). is similar to that of (4)

Example 1: $\quad$ Find $\frac{d y}{d x}$ if $\quad y=x \operatorname{Sin}^{-1}\left(\frac{x}{a}\right)+\sqrt{a^{2}+x^{2}}$

Solution: Given that $y=x \operatorname{Sin}^{-1}\left(\frac{x}{a}\right)+\sqrt{a^{2}+x^{2}}$
Differentiating w.r.t. $x$, we have

$$
\begin{aligned}
& \frac{d y}{d x}=\frac{d}{d x}\left[x \operatorname{Sin}^{-1} \frac{x}{a}+\sqrt{a^{2}+x^{2}}\right]=\frac{d}{d x}\left[x \operatorname{Sin}^{-1} \frac{x}{a}\right]+\frac{d}{d x}\left(a^{2}+x^{2}\right)^{1 / 2} \\
& =1 \cdot \operatorname{Sin}^{-1} \frac{x}{a}+x \cdot \frac{1}{\sqrt{1-\left(\frac{x}{a}\right)^{2}}} \cdot \frac{d}{d x}\left(\frac{x}{a}\right) \cdot \frac{1}{2}\left(\omega^{2} \quad x^{2}\right)^{\frac{1}{2}-1} \cdot \frac{d}{d x}\left(\omega^{2} \quad x^{2}\right)
\end{aligned}
$$

$$
\begin{aligned}
& \operatorname{Sin}^{-1} \frac{x}{a}+x \frac{1}{\sqrt{1-\frac{x^{2}}{a^{2}}}} \frac{1}{a}+\frac{1}{2 \sqrt{a^{2}-x^{2}}}(-2 x) \\
& \operatorname{Sin}^{-1} \frac{x}{a}+x \frac{a}{\sqrt{a^{2}-x^{2}}} \frac{1}{a}-\frac{1}{\sqrt{a^{2}-x^{2}}}=\operatorname{Sin}^{-1} \frac{x}{a}
\end{aligned}
$$

Example 2: If $y=\tan \left(2 \operatorname{Tan}^{-1} \frac{x}{2}\right)$, show that $\frac{d y}{d x}-\frac{4\left(1+y^{2}\right)}{4+x^{2}}$

Solution: Let $u=2 \operatorname{Tan}^{-1} \frac{x}{2}$, then

$$
y=\tan u \Rightarrow \frac{d y}{d u}=\sec ^{2} u=1+\tan ^{2} u=1+y^{2}
$$

and $\frac{d u}{d x}=\frac{d}{d x}\left(2 \sqrt{\tan ^{-1} \frac{x}{2}}\right) \cdot \mathbb{2} \frac{1}{1+\left(\frac{x}{2}\right)^{2}} \frac{d}{d x}\left(\frac{x}{2}\right)-\frac{2}{1+\frac{x^{2}}{4}} \frac{1}{2}-\frac{4}{4+x^{2}}$
Thus $\frac{d y}{d x}=\frac{d y}{d u} \frac{d u}{d x}=\left(1 \quad y^{2}\right) \cdot \frac{4}{4+x^{2}}-\frac{4\left(1+y^{2}\right)}{4+x^{2}}$

## EXERCISE 2.5

1. Differentiate the following trigonometric functions from the first principle,
(i) $\sin x$
(ii) $\tan 3 x$
(iii) $\sin 2 x+\cos 2 x$
(iv) $\cos x^{2}$
(v) $\tan ^{2} x$
(vi) $\sqrt{\tan x}$
(vii) $\cos \sqrt{x}$
2. Differentiate the following w.r.t. the variable involved
(i) $x^{2} \sec 4 x$
(ii) $\tan ^{2} \theta \sec ^{2} \theta$
(iii) $(\sin 2 \theta-\cos 3 \theta)^{2}$
(iv) $\cos \sqrt{x}+\sqrt{\sin x}$
version: 1.1
3. Find $\frac{d y}{d x}$ if
(i) $y=x \cos y$
(ii) $x=y \sin y$
4. Find the derivative w.r.t. $x$
(i) $\cos \sqrt{\frac{1+x}{1+2 x}}$
(ii) $\sin \sqrt{\frac{1+2 x}{1+x}}$
5. Differentiate
(i) $\sin x$ w.r.t. $\cot x$
(ii) $\sin ^{2} x$ w.r.t. $\cos ^{4} x$
6. If $\tan y(1+\tan x)=1 \tan x$, show that $\frac{d y}{d x}=1$
7. If $y=\sqrt{\tan x+\sqrt{\tan x+\sqrt{\tan x}}}+\ldots \infty$, prove that $\cdot(2 y \quad \frac{1}{2} \frac{d y}{d x} \quad \sec ^{2} x$.
8. If $x=a \cos ^{3} \theta, y=b \sin ^{3} \theta$, show that $a \frac{d y}{d x} \approx b \tan \theta \quad 0$
9. Find $\frac{d y}{d x}$ if $x=a(\cos t+\sin t), y=a(\sin t-t \cos t)$
10. Differentiate w.r.t. $x$
(i) $\operatorname{Cos}^{-1} \frac{x}{a}$
(ii) $\operatorname{Cot}^{-1} \frac{x}{a}$
(iii) $\frac{1}{a} \operatorname{Sin}^{-1} \frac{a}{x}$
(iv) $\operatorname{Sin}^{-1} \sqrt{1-x^{2}}$
(v) $\operatorname{Sec}^{-1}\left(\frac{x^{2}+1}{x^{2}-1}\right)$
(vi) $\operatorname{Cot}^{-1}\left(\frac{2 x}{1-x^{2}}\right)$
(vii) $\operatorname{Cos}^{-1}\left(\frac{1-x^{2}}{1+x^{2}}\right)$
11. $\frac{d y}{d x}=\frac{y}{x}$ if $\frac{y}{x}=\operatorname{Tan}^{-1} \frac{x}{y}$
12. If $y=\tan \left(\varphi \operatorname{Tan}^{-1} \varphi\right)$, show that $\left(1 \quad x^{2}\right) y, \quad p\left(1 \quad y^{2}\right) \quad 0$

### 2.10 DERIVATIVE OF EXPONENTIAL FUNCTIONS:

A function $f$ defined by
$f(x)=a^{x}$
$a>0, a \neq 1$ and $x$ is any real number.
is called an exponential function
If $a=e$, then $y=a^{x}$ becomes $y=e^{x} \cdot e^{x}$ is called the natural exponential function.
Now we find derivatives of $e^{x}$ and $a^{x}$ from the first principle:

1. Let $y=e^{x}$ then
$y+\delta y=e^{x+\delta x}$ and $\delta y=y+\delta y-y=e^{x+\delta x}-e^{x}=e^{x} \cdot e^{\delta x}-e^{x}$
That is, $\delta y=e^{x}\left(e^{\delta x}-1\right)$ and $\frac{\delta y}{\delta x} \quad e^{x} \cdot\left(\frac{e^{\delta x}-1}{\delta x}\right)$
Thus $\lim _{\delta x \rightarrow 0} \frac{\delta y}{\delta x}=\lim _{\delta x \rightarrow 0} e^{x}\left(\frac{e^{\delta x}-1}{\delta x}\right) e^{x} \cdot \lim _{\delta x \rightarrow 0}\left(\frac{e^{\delta x}-1}{\delta x}\right)$
$\left(\because \lim _{\delta x \rightarrow 0} e^{x}=e^{x} \cdot\right)$
$\frac{d y}{d x}=e^{x} \cdot 1\left(\right.$ Using $\left.\lim _{h \rightarrow 0} \frac{e^{h}-1}{h} 1\right)$
or $\frac{d}{d x}\left(e^{x}\right)=e^{x}$
2. Let $\quad y=a^{x}$, then

$$
y+\delta y=a^{x+\delta x} \text { and } \delta y=a^{x+\delta x}-a^{x}=a^{x} \cdot a^{\delta x}-a^{x}=a^{x}\left(a^{\delta x}-1\right)
$$

Dividing both sides by $\delta x$, we have

$$
\frac{\delta y}{\delta x}=a^{x}\left(\frac{a^{\delta x}-1}{\delta x}\right)
$$

Thus $\frac{d y}{d x}=\lim _{\delta x \rightarrow 0} a^{x}\left(\frac{a^{\delta x}-1}{\delta x}\right) a^{x} \cdot \lim _{\delta x \rightarrow 0}\left(\frac{a^{\delta x}-1}{\delta x}\right)\left(\because \lim _{\delta x \rightarrow 0} a^{x} a^{x}\right)$

$$
=a^{x} \cdot(\ln a)\left(\text { Using } \lim _{h \rightarrow 0} \frac{a^{h}-1}{h} \quad \log _{a} \ln a\right)
$$

or $\frac{d}{d x}\left(a^{x}\right)=a^{x} \cdot(\ln a)$

Example 1: $\quad$ Find $\frac{d y}{d x}$ if : (i) $y=e^{x^{2}+1}$
(ii) $y=a^{x / 2}$

Solution: (i) Let $\quad u=x^{2}+1$, then

$$
y=\mathrm{e}^{u} \quad \ldots .(\mathrm{A}) \text { and } \frac{d u}{d x}=\frac{d}{d x}\left(x^{2}+1\right)=2 x
$$

Differentiating both sides of (A) w.r.t. ' $x$ ', we have

$$
\begin{aligned}
& \frac{d}{d x}(y)=\frac{d}{d x}\left(e^{u}\right)=\frac{d}{d u}\left(e^{u}\right) \cdot \frac{d u}{d x} \quad \text { (Using the chain rule) } \\
& =e^{u} \frac{d u}{d x} \quad\left(\text { Using } \frac{d}{d x}\left(e^{u}\right) \quad e^{x}\right) \\
& \text { Thus } \frac{d y}{d x}=e^{x^{2}+1} \cdot(2 x) \quad\left(\forall u \quad x^{2} \quad 1 \Rightarrow \text { and } \frac{d u}{d x} \quad 2 x\right)
\end{aligned}
$$

(ii) Let $u=\sqrt{x} \quad$ Then $\quad y \quad a^{u}$
and $\frac{d u}{d x}=\frac{d}{d x}\left(x^{1 / 2}\right)=\frac{1}{2} x^{-1 / 2}=\frac{1}{2 \sqrt{x}}$
Differentiating both sides of (A) w.r.t. ' $x$ ', gives

$$
\begin{aligned}
& \frac{d y}{d x}=\frac{d}{d x}\left(a^{u}\right)=\frac{d}{d u}\left(a^{u}\right) \cdot \frac{d u}{d x} \quad\left(\because \frac{d y}{d x} \quad \frac{d y}{d u} \frac{d u}{d x}\right) \\
& =\left(a^{u} \ln a\right) \cdot \frac{d u}{d x} \quad\left(\text { Using } \frac{d}{d x}\left(a^{x}\right) \quad a^{x} \ln a\right) \\
& \text { Thus } \frac{d}{d x}\left(a^{x / 2}\right)=\left(a^{x / 2} \ln a\right) \cdot \frac{1}{2 \sqrt{x}}=\left(\because u \quad \sqrt{x} \text { and } \frac{d u}{d x} \quad \frac{1}{2 \sqrt{x}}\right)
\end{aligned}
$$

$$
=\frac{\ln a}{2} \cdot a^{\sqrt{x}} \frac{1}{\sqrt{x}}
$$

Example 2: Differentiate $y=a^{x}$ w.r.t. $x$.
Solution: Here $\mathrm{y}=a^{x}$

$$
=e^{x \ln a}
$$

Differentiating w.r.t. ' $x$ ', we have

$$
\begin{aligned}
\frac{d y}{d x} & =e^{x \ln a} \cdot \frac{d}{d x}(x \ln \mathrm{a}) \\
& =w^{\prime} \cdot(\ln a) \quad\left(\because e^{x \ln a} \quad a^{x}\right) \\
& =w^{\prime} \cdot(\ln a) \quad\left(\because e^{x \ln a} \quad a^{x}\right)
\end{aligned}
$$

### 2.11 DERIVATIVE OF THE LOGARITHMIC FUNCTION

## Logarithmic Function:

If $a>0 \quad a \neq 1$ and $x=a$, then the function defind by

$$
y=\log _{a}{ }^{x} \quad(x \quad 0)
$$

is called the logarithm of $x$ to the base a.
The logarithmic functions $\log _{a}{ }^{x}$ and $\log _{10}{ }^{x}$ are called natural and common logarithms respectively, $y=\log _{a}{ }^{x}$ is written as $y=\ln x$.

We first find $\frac{d}{d x}(\ln x)$.
Let $y=\ln x$ Then

$$
\begin{aligned}
& y+\delta y=\ln (x+\delta x) \quad \text { and } \\
& \delta y=\ln (x+\delta x)-\ln x=\left(\frac{x+\delta x}{x}\right)=\ln \left(1+\frac{\delta x}{x}\right)
\end{aligned}
$$

Now $\quad \frac{\delta y}{\delta x}=\frac{1}{\delta x} \ln \left(1+\frac{\delta x}{x}\right)$

$$
=\frac{1}{x} \frac{x}{\delta x} \ln \left(1+\frac{\delta x}{x}\right)=\frac{1}{x} \ln \left(1+\frac{\delta x}{x}\right)^{\frac{x}{d x}}
$$

Thus $\lim _{\delta x \rightarrow 0} \frac{\delta y}{\delta x}=\lim _{\delta x \rightarrow 0}\left[\frac{1}{x} \ln \left(1+\frac{\delta x}{x}\right)^{\frac{x}{d x}}\right]=\frac{1}{x} \lim _{\delta x \rightarrow 0}\left[\ln \left(1+\frac{\delta x}{x}\right)^{\frac{x}{d x}}\right]$

$$
\frac{d y}{d x}=\frac{1}{x} \cdot \ln \left[\lim _{\frac{x}{x} \rightarrow 0}\left(1 \cdot \frac{\delta x}{x}\right)^{\frac{x}{d x}}\right]
$$

$\left(\because \frac{\delta x}{x} \rightarrow 0\right.$ when $\left.\delta x \rightarrow 0\right)$

$$
\begin{aligned}
& =\frac{1}{x} \ln e \quad\left[\because \lim _{z \rightarrow 0}(1+z)^{\frac{x}{z}}=e\right] \\
& =\frac{1}{x} \cdot 1=\frac{1}{e} \quad=\left(\because \log _{e}^{e} 1\right)
\end{aligned}
$$

Now we find derivative of the general logarithmic function.
Let $\quad y=\log _{a}{ }^{x}$ then

$$
\begin{aligned}
& y+\delta y=\log _{a}(x+\delta x) \text { and } \\
& \delta y=\log _{a}(x+\delta x)-\log _{a}{ }^{x}=\log \left(\frac{x+\delta x}{x}\right)=\log _{a}\left(1+\frac{\delta x}{x}\right) \\
& \frac{\delta y}{\delta x}=\frac{1}{\delta x} \log _{a}\left(1+\frac{\delta x}{x}\right)=\frac{1}{x} \cdot \frac{x}{\delta x} \log _{a}\left(1+\frac{\delta x}{x}\right) \\
&=\frac{1}{x} \log _{a}\left(1+\frac{\delta x}{x}\right)^{\frac{x}{d x}}
\end{aligned}
$$

Thus $\frac{d y}{d x}=\lim _{\delta x \rightarrow 0}\left[\frac{1}{x} \log _{a}\left(1+\frac{\delta x}{x}\right)^{\frac{x}{d x}}\right]=\frac{1}{x} \lim _{\delta x \rightarrow 0}\left[\log _{a}\left(1+\frac{\delta x}{x}\right)^{\frac{x}{d x}}\right]$

$$
=\frac{1}{x} \log _{a}\left[\frac{\lim _{\frac{\delta x}{x} \rightarrow 0}}{\frac{\delta x}{x} \rightarrow 0}\left(1 \cdot \frac{\delta x}{x}\right)^{\frac{x}{d x}}\right]
$$

$$
\begin{aligned}
& =\frac{1}{x} \log _{a}^{x} \quad\left(\because \lim _{z \rightarrow 0}(1+z)^{\frac{1}{x}}=e\right) \\
& \text { or } \frac{d}{d x}\left[\log _{a}^{x}\right]=\frac{1}{x} \cdot \frac{1}{\ln \mathrm{a}} \quad\left(\because \log _{a}^{x}=\frac{1}{\log _{a}^{x}} \cdot \frac{1}{\ln \mathrm{a}}\right)
\end{aligned}
$$

Example 1: $\quad$ Find $\frac{d y}{d x}$ if $y=\log _{a x}\left(a x^{2}+b x+c\right)$
Solution: Let $u=a x^{2}+b x+c$ Then

$$
\begin{aligned}
& y=\log _{a x}^{u} \Rightarrow \frac{d y}{d u}=\frac{1}{u} \cdot \frac{1}{\ln 10} \\
& \text { and } \frac{d u}{d x}=\frac{d}{d x}(a x+b x+c)=a(2 x)+b(1)=2 a x+b \\
& \text { Thus } \frac{d y}{d x}=\frac{d y}{d u} \cdot \frac{d u}{d x}=\left(\frac{1}{u} \cdot \frac{1}{\ln 10}\right) \frac{d u}{d x} \\
& =\frac{1}{\left(a x^{2}+b x+c\right) \ln 10}(2 a x \quad b) \\
& \text { or } \frac{d}{d x}\left[\log _{a x}\left(a x^{2}+b x+c\right)\right]=\frac{2 a x+b}{\left(a x^{2}+b x+c\right) \ln 10}
\end{aligned}
$$

Example 2: $\quad$ Differentiate $\ln \left(x^{2}+2 x\right)$ w.r.t.' $x^{\prime}$.
Solution: Let $\quad y=\ln \left(x^{2}+2 x\right)$, then

$$
\begin{aligned}
\frac{d y}{d x} & =\frac{d}{d x}\left[\ln \left(x^{2}+2 x\right)\right]=\frac{1}{\left(x^{2}+2 x\right)} \cdot \frac{d}{d x}\left(x^{2}+2 x\right) \quad \text { (Using chain rule) } \\
& =\frac{1}{x^{2}+2 x}(2 x+2)=\frac{2(x+1)}{x^{2}+2 x} \\
\text { Thus } \frac{d}{d x}\left[\ln \left(x^{2}+2 x\right)\right] & =\frac{2(x+1)}{x^{2}+2 x}
\end{aligned}
$$

version: 1.1

### 2.12 LOGARITHMIC DIFFERENTIATION

Algebraic expressions consisting of product, quotient and powers can be often simplified before differentiation by taking logarithm.

Example 1: $\quad$ Differentiate $y=e^{f(y)}$ w.r.t.' $x^{\prime}$.
Solution: Here $y=e^{f(x)}$
Taking logarithm of both sides of (i), we have

$$
\begin{aligned}
\ln y & =f(x) \cdot \ln e \\
& =f(x) \\
& \text { ( } \because \text { In } \mathrm{e}=1)
\end{aligned}
$$

Differentiating w.r.t $x$, we get

$$
\begin{aligned}
& \frac{1}{y} \cdot \frac{d y}{d x}=f^{\prime}(x) \\
& \text { So } \frac{d y}{d x} y \quad f^{\prime}(x) \quad e^{f(x)} \quad f^{\prime}(x) \\
& \text { or } \frac{d}{d x}\left(e^{f(x)}\right)=e^{f(x)} \times f^{\prime}(x)
\end{aligned}
$$

Example 2: $\quad$ Find derivative of $\frac{x \sqrt{x^{2}+3}}{x^{2}+1}$
Solution: Let $y=\frac{x \sqrt{x^{2}+3}}{\left(x^{2}+1\right)}$
Taking logarithm of both sides, we have

$$
\ln y=\ln \left(\frac{x \sqrt{x^{2}+3}}{x^{2}+1}\right)=\ln \left(x \sqrt{x^{2}+3}\right)-\ln \left(x^{2}+1\right)
$$

or $\ln y=\ln x+\frac{1}{2} \ln \left(x^{2}+3\right)-\ln \left(x^{2}+1\right)$
Differentiating both sides of (ii) w.r.t ' $x$ ',

$$
\begin{aligned}
& \frac{d}{d x}[\ln y]=\frac{d}{d x}\left[\ln x+\frac{1}{2} \ln \left(x^{2}+3\right)-\ln \left(x^{2}+1\right)\right] \\
& \frac{1}{y} \frac{d y}{d x}=\frac{1}{x}+\frac{1}{2} \cdot \frac{1}{x^{2}+3}+2 x-\frac{1}{x^{2}+1}+2 x \\
& \quad \frac{1}{x} \cdot \frac{x}{x^{2}+3}-\frac{2 x}{x^{2}+1} \\
& =\frac{\left(x^{2}+3\right)\left(x^{2}+1\right)+x \cdot x\left(x^{2}+1\right)-2 x \cdot x\left(x^{2}+3\right)}{x\left(x^{2}+3\right)\left(x^{2}+1\right)} \\
& =\frac{x^{4}+4 x^{2}+3+x^{4}+x^{2}-2 x^{4}-6 x^{2}}{x\left(x^{2}+3\right)\left(x^{2}+1\right)} \cdot \frac{3-x^{2}}{x\left(x^{2}+3\right)\left(x^{2}+1\right)} \\
& \text { Thus } \frac{d y}{d x}=\frac{y\left(3-x^{2}\right)}{x\left(x^{2}+1\right)\left(x^{2}+1\right)} \cdot \frac{y \sqrt{x^{2}+3}}{x^{2}+1} \cdot \frac{3-x^{2}}{x\left(x^{2}+3\right)\left(x^{2}+1\right)} \\
& =\frac{3-x^{2}}{\sqrt{x^{2}+3} \cdot\left(x^{2}+1\right)^{3}}
\end{aligned}
$$

Example 3: Differentiate $(\ln x)^{t}$ w.r.t. ' $x$ '.

Solution: Let $y=(\ln x)^{*}$
Taking logarithm of both sides of (i), we have

$$
\ln y=\ln \left[(\ln x)^{*}\right] \quad x \ln (\ln x)
$$

Differentiating w.r.t $x$,

$$
\begin{aligned}
\frac{1}{y} \frac{d y}{d x} & =1 \cdot \ln (\ln x)+x \cdot \frac{1}{\ln x} \cdot \frac{d}{d x}(\ln x) \\
& =\ln (\ln x)+x \cdot \frac{1}{\ln x} \cdot \frac{1}{x}=\ln (\ln x)+\frac{1}{\ln x} \\
\frac{d y}{d x} & =y\left[\ln (\ln x)+\frac{1}{\ln x}\right]=(\ln x)^{t}\left[\ln (\ln x)+\frac{1}{\ln x}\right]
\end{aligned}
$$

### 2.13 DERIVATIVE OF HYPERBOLIC FUNCTIONS

The functions defined by:

$$
\begin{aligned}
& \sinh x=\frac{e^{x}-e^{-x}}{2}, x \in R ; \cosh x=\frac{e^{x}+e^{-x}}{2} ; x \in R \\
& \tanh x=\frac{\sinh x}{\cosh x}=\frac{e^{x}-e^{-x}}{e^{x}+e^{-x}} ; x \in R
\end{aligned}
$$

are called hyperbolic functions.
The reciprocals of these three functions are defined as:

$$
\begin{aligned}
& \operatorname{cosech} x=\frac{1}{\sinh x}=\frac{2}{e^{x}-e^{-x}}, x \in R-\{0\} \\
& \operatorname{sech} x=\frac{1}{\cosh x}=\frac{2}{e^{x}+e^{-x}}, x \in R \\
& \operatorname{coth}=\frac{1}{\tanh x}=\frac{e^{x}+e^{-x}}{e^{x}-e^{-x}}, x \in R-\{0\}
\end{aligned}
$$

Derivatives of $\sin h x, \cos h x$ and $\tan h x$ are found as explained below:

$$
\begin{aligned}
& \frac{d}{d x}(\sinh x)=\frac{d}{d x}\left[\frac{1}{2}\left(e^{x}-e^{-x}\right)\right]=\frac{1}{2}\left[e^{x}-e^{-x} t-1 j\right]=\frac{1}{2}\left(e^{x}+e^{-x}\right)=\cosh x \\
& \frac{d}{d x}(\cosh x)=\frac{d}{d x}\left[\frac{1}{2}\left(e^{x}+e^{-x}\right)\right]=\frac{1}{2}\left[e^{x}+e^{-x} \cdot t-1 j\right]=\frac{1}{2}\left(e^{x}-e^{-x}\right)=\sinh x \\
& \frac{d}{d x}[\tanh x]=\frac{d}{d x} \frac{e^{x}-e^{-x}}{e^{x}+e^{-x}} \cdot \frac{\left(e^{x}+e^{-x}\right)\left(e^{x}+e^{-x}\right)-\left(e^{x}-e^{-x}\right)\left(e^{x}-e^{-x}\right)}{\left(e^{x}+e^{-x}\right)^{2}} \\
& =\frac{e^{2 x}+e^{-2 x}+2-\left(e^{2 x}+e^{-2 x}-2\right)}{\left(e^{x}+e^{-x}\right)^{2}} \quad \frac{4}{\left(e^{x}+e^{-x}\right)^{2}} \\
& =\left(\frac{2}{e^{x}+e^{-x}}\right)^{2}=\operatorname{sech}^{2} x
\end{aligned}
$$

The following results can easily be proved.

$$
\begin{aligned}
& \frac{d}{d x}(\cos e h x)=\operatorname{coth} x \cos \operatorname{ech} x ; \frac{d}{d x}(\operatorname{sech} x) \quad \tanh x \operatorname{sech} x \\
& \frac{d}{d x}(\operatorname{coth} x)=-\cos e c h^{2} x
\end{aligned}
$$

Example 1: $\quad$ Find $\frac{d y}{d x}$ if $y=\sinh 2 x$
Solution: Let $u=2 x$, then

$$
y=\sinh u \quad \Rightarrow \frac{d y}{d u}=\cosh u
$$

and $\frac{d u}{d x}=\frac{d}{d x}(2 x)=2$.
Thus $\frac{d y}{d x}=\frac{d y}{d u} \cdot \frac{d u}{d x}=\cosh u \cdot \frac{d u}{d x}=[\cosh (2 x)]. 2=2 \cosh 2 x$
or $\frac{d}{d x}[\sinh 2 x]=2 \cosh 2 x$.
Example 2: $\quad$ Find $\frac{d y}{d x}$ if $y=\tanh \left(x^{2}\right)$
Solution: Let $u=x^{2}$, then $y=\tanh u \Rightarrow \frac{d y}{d u}=\operatorname{sech}^{2} u$
and $\frac{d u}{d x}=\frac{d}{d x}(x)=2 x$
Thus $\frac{d y}{d x}=\frac{d y}{d u} \cdot \frac{d u}{d x}=\operatorname{sech}^{2} u \cdot \frac{d u}{d x}=\left[\operatorname{sech}^{2}\left(x^{2}\right)\right] \quad 2 x$
or $\frac{d}{d x}\left[\tanh x^{2}\right]=2 x \operatorname{sech}^{2} x^{2}$

### 2.14 DERIVATIVES OF THE INVERSE HYPERBOLIC FUNCTIONS:

The inverse hyperbolic functions are defined by:

1. $y=\sinh ^{-1} \infty$ if and if $x \quad \sinh y ; x, y \quad R$
2. $y=\cosh ^{-1} x$ if and only if $x \cosh y \infty ; x[\mathrm{~V}), y[0,]]$
3. $y=\tanh ^{-1} x$ if andonly if $x \in \tanh y ; x(1,1), y \quad R$
4. $y=\operatorname{coth}^{-1} x$ if andonly if $x \in \operatorname{coth} y ; x[1,1], y \quad R\{0\}$
5. $y=\operatorname{sech}^{-1} x$ if and only if $x=\operatorname{sech} y ; x(0,1], y[0$, )
6. $y=\cos e c h^{-1} x$ if andonly if $x \operatorname{osec} h y ; x \not R \quad\{0\}, y \quad R\{0\}$

The following two equations can easily be derived:
(i) $\sinh ^{-1} x=\ln \left(x+\sqrt{x^{2}+1}\right)$
(ii) $\cosh ^{-1} x=\ln \left(x \cdot \sqrt{x^{2}-1}\right)$

## Proof of (i).

Let $y=\min ^{-1} x$ for $x, y \quad R$, then

$$
\begin{aligned}
& x=\sinh y \Rightarrow x=\frac{e^{y}-e^{-y}}{2} \\
& \Rightarrow 2 x e^{y}=e^{2 y}-1
\end{aligned}
$$

or $e^{2 y}-2 x e^{y}-1=0$
Solving the above equation for $e^{y}$, we have

$$
\begin{aligned}
e^{y} & =\frac{2 x \pm \sqrt{4 x^{2}+4}}{2} \\
& =\frac{2 x \pm 2 \sqrt{x^{2}+1}}{2}=x \pm \sqrt{x^{2}+1}
\end{aligned}
$$

As $e^{y}$ is positive for $y \in R$, so we discard

$$
x-\sqrt{x^{2}+1}
$$

Thus $e^{y}=x+\sqrt{x^{2}+1} \Rightarrow y=\ln \left(x+\sqrt{x^{2}+1}\right)$

$$
\Rightarrow \sinh ^{-1} x=\operatorname{In}\left(x+\sqrt{x^{2}+1}\right)
$$

Proof of (ii)
Let $y=\cosh ^{-1} x$ for $x \in[1, \infty), y \in[0, \in)$, then

$$
x=\cosh y \Rightarrow x=\frac{e^{y}+e^{-y}}{2} \Rightarrow e^{2 y}-2 e^{y}+1=0
$$

Solivng (1) gives, $e^{y}=\frac{2 x \pm \sqrt{4 x^{2}-4}}{2}=\frac{2 x \pm 2 \sqrt{x^{2}-1}}{2}=x \pm \sqrt{x^{2}-1}$.
$e^{y}=x-\sqrt{x^{2}-1}$ can be written as $y=\ln \left(x \quad \sqrt{x^{2}-1}\right)$
If $x=1$, then $y=\ln (1-\sqrt{1-1})=\ln (1)=0$ but
$\ln \left(x-\sqrt{x^{2}-1}\right)$ is negative for all $x>1$, that is
for each $x \in(1, \infty), y \notin(0, \infty)$, so we discard this value of $e^{y}$
Thus $e^{y}=x+\sqrt{x^{2}+1}$ which give $y=\ln \left(x+\sqrt{x^{2}-1}\right)$, that is

$$
\cosh ^{-1} x=\operatorname{In}\left(x+\sqrt{x^{2}-1}\right)
$$

Derivative of $\sinh ^{-1} x$ :
Let $y=\mathfrak{a} \operatorname{inh}^{-1} x ; x, y \quad R$
Then $x=\sinh y$

$$
\begin{aligned}
& \frac{d x}{d y}=\cosh y \quad \Rightarrow \frac{d y}{d x}=\frac{1}{\cosh y} \quad\left(\because \frac{d y}{d x} \frac{1}{d x}\right) \\
& \text { or } \quad \frac{d y}{d x}=\frac{1}{\cosh y}=\frac{1}{\sqrt{1+\sinh ^{2} y}}>\quad(\because \cosh y \quad 0) \\
& \frac{d y}{d x}=\frac{d}{d x}\left(\operatorname{asinh}^{-1} x\right) \quad \frac{1}{\sqrt{1+x^{2}}} \quad(x \quad R)
\end{aligned}
$$

## Derivative of $\cosh ^{-1} x$ :

Let $y=\cosh ^{-1} \alpha ; \quad \in x \ni[1), y[0,)$
Then $x=\cosh y$

$$
\begin{aligned}
& \text { and } \frac{d x}{d y}=\sinh y \quad \Rightarrow \frac{d y}{d x}=\frac{1}{\sinh y}=\quad\left(\because \frac{d y}{d x} \frac{1}{d x}\right) \\
& \text { or } \frac{d y}{d x}=\frac{1}{\sinh y}=\frac{1}{\sqrt{\cosh ^{2} y-1}} \quad(\because \sinh y>0, \text { as } y>0) \\
& \text { Thus } \frac{d y}{d x}=\frac{d}{d x}\left(\operatorname{asinh}^{-1} x\right) \quad \frac{1}{\sqrt{x^{2}-1}} \quad(x \quad 1) \\
& \text { As } \cosh ^{-1} x=\ln \left(x+\sqrt{x^{2}-1}\right), \text { so } \\
& \frac{d}{d x}\left[\cosh ^{-1} x\right]=\frac{1}{x+\sqrt{x^{2}-1}}\left(1+\frac{2 x}{2 \sqrt{x^{2}-1}}\right)=\frac{1}{x+\sqrt{x^{2}-1}} \cdot \frac{\sqrt{x^{2}-1}+x}{\sqrt{x^{2}-1}} \cdot \frac{1}{\sqrt{x^{2}-1}}
\end{aligned}
$$

## Derivative of $\tanh ^{-1} x$ :

Let $y=\tanh ^{-1} x ; \quad x \in(-1,1), y \in R$

$$
\begin{aligned}
& \text { Then } x=\tanh y \text { and } \frac{d x}{d y}=\operatorname{sech}^{2} \Rightarrow \frac{d y}{d x}=\frac{1}{\operatorname{sech}^{2} y} \quad \frac{d y}{d x} \frac{1}{d x} \\
& \frac{d y}{d x}=\frac{1}{1-\tanh ^{2} y}-\frac{1}{1-x^{2}} \quad\left(\because \operatorname{sech}^{2} y-1 \quad \tanh ^{2} y\right) \\
& \text { Thus } \frac{d}{d x}\left(\tanh ^{-1} x\right)=\frac{1}{1-x^{2}} \quad ; \quad-1<x<1 \text { or }|x| \quad 1
\end{aligned}
$$

The following differentiation formulae can be easily proved.

$$
\frac{d}{d x}\left(\cosh ^{-1} x\right)=\frac{1}{1-x^{2}} \quad \text { or }-\frac{1}{x^{2}-1} \quad|x|>1
$$

$$
\begin{aligned}
& \frac{d}{d x}\left(\operatorname{sech}^{-1} x\right)=-\frac{1}{x \sqrt{1-x^{2}}} ; \quad 0 \Rightarrow 4 \\
& \frac{d}{d x}\left(\operatorname{conech}^{-1} x\right)=\frac{1}{x \sqrt{1+x^{2}}} ; x \quad 0 \\
& \text { or } \frac{d}{d x}\left(\operatorname{conech}^{-1} x\right)=-\frac{1}{|x| \sqrt{1+x^{2}}} ; \quad x \quad \text { of }-|0|
\end{aligned}
$$

Example 1: $\quad$ Find $\frac{d y}{d x}$ if $y=\sinh ^{-1}(a x+b)$
Solution: Let $u=a x+b$, then

$$
\begin{aligned}
& y=\sinh ^{-1} u \Rightarrow \frac{d y}{d x}=\frac{1}{\sqrt{1+u^{2}}} \\
& \frac{d y}{d x}=\frac{d y}{d u} \frac{d u}{d x}=\frac{1}{\sqrt{1+u^{2}}} \frac{d u}{d x}
\end{aligned}
$$

Thus $\frac{d}{d x}\left[\sinh ^{-1}(a x+b)=\frac{1}{\sqrt{1+(a x+b)^{2}}} . a\right.$ $\left(>\frac{d u}{d x} \quad \frac{d}{d x}(a x-b) \quad a\right)$
Example 2: $\quad$ Find $\frac{d y}{d x}$ if $y=\cosh \frac{u}{2}(\sec x) \quad 0 \quad x \quad \pi / 2$
Solution: Let $u=\sec x$, then

$$
\begin{aligned}
& y=\cosh ^{-1} u \Rightarrow \frac{d y}{d x}=\frac{1}{\sqrt{u^{2}-1}} \\
& \text { and } \frac{d u}{d x}=\frac{d}{d x}(\sec x)=\sec x \tan x \\
& \text { Thus } \frac{d y}{d x}=\frac{d y}{d u} \frac{d u}{d x}=\frac{1}{\sqrt{u^{2}-1}} \frac{d u}{d x} \\
& =\frac{1}{\sqrt{\sec x}}(\sec x \tan x) \frac{1}{\tan x}(\sec x \tan x) \sec x \\
& \text { or } \frac{d}{d x}\left[\cosh ^{-1}(\sec x)\right]=\sec x
\end{aligned}
$$

## EXERCISE 2.6

1. Find $f^{x}(x)$ if
(i) $f(x)=e^{i \frac{x}{x-1}}$
(ii) $f(x)=x^{3} e^{\frac{x}{x-1}}(x \neq 0)$
(iii) $f(x)=e^{x}(1+\ln x)$
(iv) $f(x)=\frac{e^{x}}{e^{-x}+1}$
(v) $\ln \left(e^{x}+e^{-x}\right)$
(vi) $f x=\frac{e^{x u}-e^{-x u}}{e^{x u}+e^{-x u}}$
(vii) $f(x)=\sqrt{\ln \left(e^{2 x}+e^{-2 x}\right)}$
(viii) $f(x)=\ln \left(\sqrt{e^{2 x}+e^{-2 x}}\right)$
2. Find $\frac{d y}{d x}$ if
(i) $y=x^{3} \ln \sqrt{x}$
(ii) $y=x \sqrt{\ln x}$
(iii) $y=\frac{x}{\ln x}$
(iv) $y=x^{2} \ln \frac{1}{x}$
(v) $y=\ln \sqrt{\frac{x^{2}-1}{x^{2}+1}}$
(vi) $y=\ln \left(x+\sqrt{x^{2}+1}\right)$
(vii) $y=\ln \left(9-x^{2}\right)$
(viii) $y=e^{-2 x} \sin 2 x$
(ix) $y=e^{-x}\left(x^{2}+2 x^{2}+1\right)$
(x) $y=x e^{x u x}$
(xi) $y=\frac{5 e^{3 x-6}}{x}$
(xii) $y=(l n x)^{n x}$
(xiv) $y=\frac{\sqrt{x^{2}-1}(x+1)}{\left(x^{2}+1\right)^{3 / 2}}$
3. Find $\frac{d y}{d x}$ if
(i) $y=\cosh 2 x$
(ii) $y=\sinh 3 x$
(iii) $y=\tanh ^{-1}(x i n x) \quad \frac{\pi}{2} \quad x \quad \frac{\pi}{2}$
(iv) $y=\sinh ^{-1}\left(x^{2}\right)$
(v) $y=\ln (\tanh x)$
(vi) $y=\sinh ^{-1}\left(\frac{x}{2}\right)$

### 2.15 SUCCESSIVE DIFFERENTIATION (OR HIGHER DERIVATIVES):

Sometimes it is useful to find the differential coefficient of a derived function. If we denote $f^{\prime}$ as the first derivative of $f$, then $\left(f^{\prime}\right)^{\prime}$ is the derivative of $f^{\prime}$ and is called the second derivative of $f$. For convenience we write it as $f^{\prime \prime}$.

Similarly $\left(f^{\prime}\right)^{\prime}$, the derivative of $f^{\prime \prime}$, is called the third derivative of $f$ and is written as $f^{\prime \prime \prime}$. In general, for $n \geq 4$, the $n$th derivative of $f$ is written as $f^{(n)}$. Here we state different notations used for derivatives of higher orders.

|  1st derivative | 2nd derivative | 3rd derivative | $n$th derivative  |
| --- | --- | --- | --- |
|  $y^{\prime}$ | $y^{\prime \prime}$ | $y^{\prime \prime \prime}$ | $y^{(n)}$  |
|  $\frac{d y}{d x}$ | $\frac{d^{2} y}{d x^{2}}$ | $\frac{d^{3} y}{d x^{3}}$ | $\frac{d^{n} y}{d x^{n}}$  |
|  $y_{1}$ | $y_{2}$ | $y_{3}$ | $y_{n}$  |
|  $D_{1}$ | $D^{2}$ | $D^{3}$ | $D^{n}$  |
|  $\frac{d f}{d x}$ | $\frac{d^{2} f}{d x^{2}}$ | $\frac{d^{3} f}{d x^{3}}$ | $\frac{d^{n} f}{d x^{n}}$  |

Example 1: Find higher derivatives of the polynomial

$$ f(x)=\frac{1}{12} x^{4}-\frac{1}{6} x^{2}+\frac{1}{4} x^{3}+2 x+7 $$

Solution: $f^{\prime}(x)=\frac{1}{12}\left(4 x^{4}\right)-\frac{1}{6}\left(3 x^{2}\right)+\frac{1}{4}(2 x)+2+0=\frac{1}{3} x^{2}-\frac{1}{2} x^{2}+\frac{1}{2} x+2$ $f^{\prime \prime \prime}(x)=\frac{1}{3}\left(3 x^{2}\right)-\frac{1}{2}(2 x)+\frac{1}{2}(1)+0=x^{2}-x+\frac{1}{2}$ $f^{\prime \prime \prime}(x)=2 x-1$ $f^{\prime \prime}(x)=2$ All other higher derivatives are zero.

Example 2: $\quad$ Find $\frac{d^{3} y}{d x^{3}}$ if $y=\ln \left(x+\sqrt{x^{2}+a^{2}}\right)$

Solution: Give that $y=\ln \left(x+\sqrt{x^{2}+a^{2}}\right)$ Differentiating both sides of (i) w.r.t. ' $x$ ', we have

$$ \begin{aligned} \frac{d y}{d x} & =\frac{1}{x+\sqrt{x^{2}+a^{2}}} \frac{d}{d x}\left(x \quad \sqrt{x^{2} \quad a^{2}}\right) \ & =+\frac{1}{x+\sqrt{x^{2}+a^{2}}}\left[1 \quad \frac{1+2 x}{2 \sqrt{x^{2}+a^{2}}}\right] \ & =+\frac{1}{x+\sqrt{x^{2}+a^{2}}}\left(\frac{\sqrt{x^{2}+a^{2}}+x}{2 \sqrt{x^{2}+a^{2}}}\right) \end{aligned} $$

That is, $\frac{d y}{d x}=\frac{1}{\sqrt{x^{2}+a^{2}}}$ Differentiating (ii) w.r.t. ' $x$ ', we have

$$ \begin{aligned} \frac{d^{2} y}{d x^{2}} & =\frac{d}{d x}\left[\left(x^{2}+a^{2}\right)^{-1 / 2}\right] \neq \frac{1}{2}\left(x^{2} \times a^{2}\right)^{-1 / 2} \quad 2 x \ \text { or } \quad \frac{d^{2} x}{d x^{2}} & =-\frac{x}{\left(x^{2}+a^{2}\right)^{1 / 2}} \end{aligned} $$

Differentiating (iii) w.r.t. ' $x$ ', we get

$$ \begin{aligned} \frac{d^{3} y}{d x^{3}} & =\frac{1 \cdot\left(x^{2}+a^{2}\right)^{1 / 2}-x \cdot \frac{3}{2}\left(x^{2}+a^{2}\right)^{1 / 2} \cdot 2 x}{\left(x^{2}+a^{2}\right)^{3 / 2} \mid} \ & =\frac{\left(x^{2}+a^{2}\right)^{1 / 2}\left[\left(x^{2}+a^{2}\right)-3 x^{2}\right]}{\left(x^{2}+a^{2}\right)^{3}} \quad \frac{a^{2}-2 x^{2}}{\left(x^{2}+a^{2}\right)^{3 / 2}} \ \frac{d^{3} y}{d x^{3}} & =\frac{2 x^{2}-a^{2}}{\left(x^{2}+a^{2}\right)^{3 / 2}} \end{aligned} $$

Example 3: $\quad$ Find $\frac{d^{2} y}{d x^{2}}$ if $y^{2}+3 a x^{2}+x^{3}=0$
Solution: Given that $y^{2}+3 a x^{2}+x^{3}=0$
Differentiating both sides of (i) w.r.t. ' $x$ ', gives

$$
\begin{aligned}
\frac{d}{d x}\left[y^{2}+3 a x^{2}+x^{3}\right]=\frac{d}{d x}(0) & =0 \\
3 y^{2} \frac{d y}{d x}+3 a(2 x)+3 x^{2}=0 & \Rightarrow y^{2} \frac{d y}{d x} \propto\left(2 a x \quad x^{2}\right) \\
& \Rightarrow \frac{d y}{d x}=-\frac{2 a x+x^{2}}{y^{2}}
\end{aligned}
$$

Differentiating both sides of (ii) w.r.t. ' $x$ ', gives

$$
\begin{aligned}
\frac{d^{2} y}{d x^{2}}= & (1) \frac{d}{d x}\left[\frac{2 a x+x^{2}}{y^{2}}\right]-\frac{(2 a+2 x) y^{2}-\left(2 a x+x^{2}\right)\left(2 y \frac{d y}{d x}\right)}{\left(y^{2}\right)^{2}} \\
= & -\frac{2(a+x) y^{2}-\left(2 a x+x^{2}\right) \cdot 2 y \cdot\left(-\frac{2 a x+x^{2}}{y^{2}}\right)}{y^{2}} \\
= & \frac{2\left[(a+x) y^{2}+\left(2 a x+x^{2}\right)\left(2 a x+x^{2}\right)\right]}{y^{2}} \\
= & \frac{2\left[(a+x) y^{2}+\left(2 a x+x^{2}\right)^{2}\right]}{y^{2} \cdot y} \\
= & \frac{2\left[(a+x)\left(-3 a x^{2}-x^{2}\right)+x^{2}(2 a+x)^{2}\right]}{y^{2}}\left(\because y^{2}=3 a x^{2} \quad x^{2}\right) \\
= & \frac{2 x^{2}\left[-(a+x)(3 a+x)+\left(4 a^{2}+x^{2}+4 a x\right)\right]}{y^{2}} \\
= & \frac{2 x^{2}\left[-\left(3 a^{2}+4 a x+x^{2}\right)+4 a^{2}+x^{2}+4 a x\right]}{y^{2}} \\
= & \frac{2 x^{2}\left[a^{2}\right]}{y^{2}} \quad \frac{-2 a^{2} x^{2}}{y^{2}}
\end{aligned}
$$

$$
\text { version: } 1.1
$$

Example 1: If $x=a(\theta \sin \theta), y \quad a(1 \cos \theta)$. Then
show that $y^{2} \frac{d^{2} y}{d x^{2}}+a=0$
Solution: Given that $x=a(\theta+\sin \theta)$
and $\quad y=a(1+\cos \theta)$
Differentiating (i) and (ii) w.r.t' $\theta^{2}$, we get

$$
\begin{aligned}
\frac{d x}{d \theta} & =a(1+\cos \theta) \\
\text { and } \frac{d y}{d \theta} & =a(-\sin \theta)
\end{aligned}
$$

Using $\frac{d y}{d x}=\frac{d y}{d \theta} \cdot \frac{d \theta}{d x}=\frac{d y}{d \theta}$ we have
$=\frac{-a \sin \theta}{a(1+\cos \theta)} \quad \frac{-\sin \theta}{1+\cos \theta}$
That is, $\frac{d y}{d x}=-\frac{\sin \theta}{1+\cos \theta}$
Differentiating (v) w.r.t. ' $x$ '

$$
\begin{aligned}
\frac{d^{2} y}{d x^{2}} & =\frac{d}{d x}\left(-\frac{\sin \theta}{1+\cos \theta}\right) \quad \frac{d}{d \theta}\left(\frac{\sin \theta}{1+\cos \theta}\right) \quad \frac{d \theta}{d x} \\
& =-\frac{\cos \theta(1+\cos \theta)-\sin \theta(-\sin \theta)}{(1+\cos \theta)^{2}} \quad \frac{d \theta}{d x} \\
\frac{d^{2} y}{d x^{2}} & =-\frac{\cos \theta+\cos ^{2} \theta+\sin ^{2} \theta}{(1+\cos \theta)^{2}} \quad \frac{d \theta}{d x} \\
& =\frac{1+\cos \theta}{(1+\cos \theta)^{2}} \quad \frac{1}{a(1+\cos \theta)} \quad\left(\because \frac{d x}{d \theta}=a(1+\cos \theta)\right)
\end{aligned}
$$

$$
\begin{aligned}
& =\frac{1}{a} \frac{1}{(1+\cos \theta)^{2}} \quad \frac{1}{a} \frac{1}{\left(\frac{y}{a}\right)^{2}} \quad \quad \left(\because 1+\cos \theta=\frac{y}{a}\right) \\
& =-\frac{1}{a} \times \frac{a^{2}}{y^{2}}=-\frac{a}{y^{2}} \\
& \text { or } \quad y^{2} \frac{d^{2} y}{d x^{2}}=-a \quad \Rightarrow y^{2} \frac{d^{2} y}{d x^{2}}+a=0
\end{aligned}
$$

Example 5: Find the first four derivatives of $\cos (a x+b)$.
Solution: Let $y=\cos (a x+b)$, then

$$
\begin{aligned}
y_{1} & =\frac{d}{d x}[\cos (a x+b)]=\sin (a x \quad b) \cdot \frac{d}{d x}\left(a x \quad b\right) \\
& =-\sin (a x+b) \times(a+0)=-\mathrm{a} \sin (a x+b) \\
y_{2} & =-\mathrm{a} \frac{a}{d x}[\sin (a x+b)]=(-\mathrm{a})[\cos (a x+b) \times(a+0)] \\
& =\mathrm{a}^{2} \cos (a x \quad b) \\
y_{3} & =-a^{2} \frac{d}{d x}[\cos (a x+b)]=\left(-a^{2}\right)[-\sin (a x+b) \times(a+0)] \\
& =a^{2} \sin (a x+b) \\
y_{4} & =a^{2} \frac{d}{d x}[\sin (a x+b)]=\left.a^{2} \times[\cos (a x+b)] \times a\right\}=a^{4} \cos (a x+b)
\end{aligned}
$$

Example 6: If $y=e^{-a x} \neq$ thenshow that $\frac{d^{2} y}{d x^{2}} \quad a^{2} y \quad 0$

Solution: As $y=e^{-a x}$, so $\frac{d y}{d x}=\frac{d}{d x}\left(e^{-a x}\right)=e^{-a x} \frac{d}{d x}(-a x)=e^{-a x} \cdot(-a)$
That is $\frac{d y}{d x}=-a y$

$$
\left(\because e^{-a x}=y\right)
$$

Now $\frac{d y}{d x}\left[\frac{d y}{d x}\right]=\frac{d}{d x}[-a y] \Rightarrow \frac{d^{2} y}{d x^{2}}=-\frac{d y}{d x}(-a)(-a y)\left(\begin{array}{lll}a & \frac{d y}{d x} & a y\end{array}\right)$
or $\frac{d^{2} y}{d x^{2}}=a^{2} y$
Differentiating (i) w.r.t. ' $x$ ' we get

$$
\begin{aligned}
& \frac{d}{d x}\left[\frac{d^{2} y}{d x^{2}}\right]=\frac{d}{d x}\left[a^{2} y\right] \Rightarrow \frac{d^{2} y}{d x^{2}}=a^{2} \frac{d y}{d x}=a^{2}(-a y)=a^{3} y \\
& \text { Thus } \frac{d^{2} y}{d x^{2}}+a^{2} y=0
\end{aligned}
$$

Example 7: If $y=S i n^{-1} \frac{x}{a}$, then show that $y_{3} \rightarrow\left(a^{2} \quad x^{2}\right)$

Solution: $y=\sin ^{-1} \frac{x}{a}$, so

$$
\begin{aligned}
y_{1}=\frac{d y}{d x} & =\frac{d}{d x}\left[\operatorname{Sin}^{-1} \frac{x}{a}\right] \frac{1}{\sqrt{1-\left(\frac{x}{a}\right)^{2}}} \frac{d}{d x}\left(\frac{x}{a}\right) \\
& =\frac{1}{\sqrt{\frac{a^{2}-x^{2}}{a^{2}}}} \frac{1}{a} \frac{a}{\sqrt{a^{2}-x^{2}}} \frac{1}{a}\left(a^{2} \quad x^{2}\right)^{-1 / 2} \\
y_{2}=\frac{d}{d x}\left[\left(a^{2}-x^{2}\right)^{-1 / 2}\right] & =-\frac{1}{2}\left(a^{2}-x^{2}\right)^{-1 / 2} \times(-2 x)=x\left(a^{2}-x^{2}\right)^{-1 / 2}
\end{aligned}
$$

## EXERCISE 2.7

1. Find $y_{1}$ if
(i) $y=2 x^{3}-3 x^{4}+4 x^{3}+x-2$
(ii) $y=(2 x+5)^{3 / 2}$
(iii) $y=\sqrt{x}+\frac{1}{\sqrt{x}}$
2. Find $y_{2}$ if
(i) $y=x^{2} \cdot e^{-x}$
(ii) $y=\ln \left(\frac{2 x+3}{3 x+2}\right)$
3. Find $y_{3}$ if
(i) $x^{2}+y^{2}=a^{2}$
(ii) $x^{3}-y^{3}=a$
(iii) $x=a \cos \theta, y=a \sin \theta$
(iv) $x=a t^{2}, y=b t^{4}$
(v) $x^{3}+y^{3}+2 g x+2 f y+c=0$
4. Find $y_{4}$ if
(i) $y=\sin 3 x$
(ii) $y=\cos ^{3} x$
(iii) $y=\ln \left(x^{2}-9\right)$
5. If $x=\operatorname{Sin} \theta, y=\operatorname{Sin} m \theta$. Show that $\left(1 \quad x \frac{1}{2}\right) y_{2} \quad \propto y_{1} \quad m^{2} y \quad 0$
6. If $y=e^{x} \sin x$, show that $\frac{d^{2} y}{d x^{2}}=2 \frac{d y}{d x} \quad 2 y \quad 0$
7. If $y=e^{x y} \sin b x$, show that $\frac{d^{2} y}{d x^{2}}=2 a \frac{d y}{d x} \quad\left(a^{2} \quad b^{2}\right) y \quad 0$
8. If $y=\left(\cos ^{-1} x\right)^{2}$, prove that $\left(1 \quad x^{2}\right) y_{2} \quad x y_{1} \quad 2 \quad 0$
9. If $y=a \cos (l n x)+b \sin (l n x)$, prove that $x^{2} \frac{d^{2} y}{d x^{2}}+b \frac{d y}{d x}+y=0$.

### 2.16 SERIES EXPANSIONS OF FUNCTIONS

A series of the form $a_{n}+a_{1} x+a_{2} x^{2}+a_{3} x^{3}+a_{4} x^{4}+\ldots \ldots+a_{n} x^{n}+\ldots$ is called a power series expansion of a function $f(x)$ where $a_{n}, a_{1}, a_{2}, \ldots, a_{n}, \ldots$ are constants and $x$ is a variable.

We determine the coefficient $a_{n}, a_{1}, a_{2}, \ldots, a_{n}, \ldots$ to specify power series by finding successive derivatives of the power series and evaluating them at $x=0$. That is,
version: 1.1

$$
\begin{aligned}
& f(x)=a_{0}+a_{1} x+a_{2} x^{2}+a_{3} x^{3}+a_{4} x^{4}+a_{5} x^{5}+\ldots \ldots+a_{n} x^{n}+\ldots . f(0)=a_{0} \\
& f^{\prime}(x)=a_{1}+2 a_{2} x+3 a_{3} x^{2}+4 a_{4} x^{3}+5 a_{5} x^{4}+\ldots \ldots+n a x^{n-1}+\ldots . f^{\prime}(0)=a_{1} \\
& f^{\prime \prime}(x)=2 a_{2}+6 a_{3} x+12 a_{4} x^{2}+20 a_{5} x^{3}+\ldots+n(n-1) a_{n} x^{n-2}+\ldots f^{\prime \prime}(0)=2 a_{2} \\
& f^{\prime \prime \prime}(x)=6 a_{3}+24 a_{4} x+60 a_{5} x^{2}+\ldots . \quad f^{\prime \prime}(0)=6 a_{3} \\
& f^{(0)}(x)=24 a_{4}+120 a_{5} x \ldots \ldots . \quad f^{(0)}(0)=24 a_{4}
\end{aligned}
$$

So we have $a_{0}=f(0), a_{1}=f^{\prime}(0), a_{2}=\frac{f^{\prime}(0)}{2!}, a_{3}=\frac{f^{\prime \prime}(0)}{3!}, a_{4}=\frac{f^{(0)}(0)}{4!}$
Following the above pattern, we can write $a_{n}=\frac{f^{\prime \prime}(0)}{n!}$
Thus substituting these values in the power series, we have

$$
f(x)=f(0)+f^{\prime}(0) x+\frac{f^{\prime \prime}(0)}{2!} x^{2}+\frac{f^{\prime \prime}(0)}{3!} x^{3}+\frac{f^{(0)}(0)}{4!} x^{4}+\ldots+\frac{f^{\prime \prime}(0)}{n!} x^{n}+\ldots
$$

This expansion of $f(x)$ is called the Maclaurin series expansion.
The above expansion is also named as Maclaurin's Theorem and can be stated as:
If $f(x)$ is expanded in ascending powers of $x$ as an infinite series, then

$$
f(x)=f(0)+f^{\prime}(0) x+\frac{f^{\prime \prime}(0)}{2!} x^{2}+\frac{f^{\prime \prime}(0)}{3!} x^{3}+\frac{f^{(0)}(0)}{4!} x^{4}+\ldots+\frac{f^{\prime \prime}(0)}{n!} x^{n}+\ldots
$$

Note that a function $f$ can be expanded in the Maclaurin series if the function is defined in the interval containing 0 and its derivatives exist at $x=0$.

The expansion is only valid if it is convergent.

Example 1: $\quad$ Expand $f(x)=\frac{1}{1+x}$ in the Maclaurin series.
Solution: $f$ is defined at $x=0$ that is, $f(0) 1$. Now we find successive derivatives of $f$ and their values at $x=0$.

$$
\begin{aligned}
& f^{\prime}(x)=(-1)(1+x)^{-2} \text { and } f^{\prime}(0)=1 \\
& f^{\prime \prime}(x)=(-1)(-2)(1+x)^{-3} \text { and } f^{\prime \prime}(0) \leftarrow 1 \longdiv { 1 } \\
& f^{\prime \prime}(x)=(-1)(-2)(-3)(1+x)^{-4} \text { and } f^{\prime \prime}(0) \leftarrow 1 \longdiv { 1 } \\
& \text { version: } 1.1
\end{aligned}
$$

$$
f^{(0)}(x)=(-1)(-2)(-3)(-4)(1+x)^{-3} \text { and } f^{(0)}(0) \quad(-1)^{3} \mid 4
$$

Following the pattern, we can write $f^{(x)}(0)=(-1)^{3} \mid \underline{n}$
Now substituting $f(0)=1, f^{\prime}(0)=1, f^{\prime \prime}(0)(1)^{3} \mid \underline{2}$,
$f^{\prime \prime}(0)=(-1)^{3} \mid 3, f^{(0)}(0)(1)^{3} \mid 4, \ldots, f^{(x)}(0)(1)^{3} \mid \underline{n}$ in the formula.
$f(x)=f(0)+f^{\prime}(0) x+\frac{f^{\prime}(0)}{12} x^{2}+\frac{f^{\prime \prime}(0)}{13} x^{3}+\frac{f^{(0)}(0)}{14} x^{4}=\ldots+\frac{f^{(x)}(0)}{1 \underline{n}} x^{2} \ldots$

$$
+\frac{f^{(x)}(0)}{1 \underline{n}} x^{2}+\ldots \text {, we have }
$$

$$
\frac{1}{1+x}=1+(-1) x+(-1)^{3} \frac{13}{12} x^{2}+(-1)^{3} \frac{13}{13} x^{3}+(-1)^{4} \frac{14}{14} x^{4}+\ldots+\frac{(-1)^{3} \mid \underline{n}}{1 \underline{n}} x^{4}+\ldots
$$

Thus, the Maclaurin series for $\frac{1}{1+x}$ is the geometric series with the first term 1 and common ratio -x .

Note: Applying the formula $x=\frac{n_{1}}{1-x}$, we have

$$
1-x+x_{1}-x_{1}+\ldots=\frac{1}{1-(-x)}=\frac{1}{1+x}
$$

Example 2: Find the Maclaurin series for $\sin x$
Solution: Let $f(x)=\sin x$. Then $f(0)=\sin 00$.

$$
\begin{aligned}
& f^{\prime}(x)=\cos x \text { and } f^{\prime}(0)=\cos 0=1 ; f^{\prime}(x)=\sin x \text { and } f^{\prime}(0) \quad \sin 0 \quad 0 \\
& f^{\prime \prime}(x)=-\cos x \text { and } f^{\prime \prime}(0)=-\cos 0=-1 ; f^{(0)}(x)=-\{-\sin x\}=-\sin x \\
& \text { and } f^{(0)}(0)=\sin (0)=0 \\
& f^{(3)}=(x)=\cos x \text { and } f^{(3)}(0)=\cos 0-1, f^{(0)}(x)=-\sin x \\
& \text { and } f^{(0)}(0)=0 ; f^{(3)} \quad \cos x \text { and } f^{(3)}(0) \quad 1
\end{aligned}
$$

Putting these values in the formula

$$
\begin{aligned}
& f(x)=f(0)+f^{\prime}(0) x+\frac{f^{\prime}(0)}{12} x^{2}+\frac{f^{\prime \prime}(0)}{13} x^{3}+\frac{f^{(0)}(0)}{14} x^{4}+\frac{f^{(3)}(0)}{15}+\ldots \text {, we have } \\
& \sin x=0 \quad 1 . x \quad \frac{0}{12} x^{2} \quad \frac{-1}{13} x^{3} \quad \frac{0}{14} x^{4} \quad \frac{1}{15} x^{5} \quad \frac{0}{16} x^{6} \quad \frac{-1}{15} x^{7} \quad \ldots \\
& \quad=x-\frac{x^{3}}{13}+\frac{x^{5}}{15}-\frac{x^{7}}{17}+\ldots \ldots
\end{aligned}
$$

Example 3: Expand $a^{x}$ in the Maclaurin series.

Solution: Let $f(x)=a^{x}$, then

$$
\begin{aligned}
& f^{\prime}(x)=a^{x} \ln a, f^{\prime \prime}(x) \quad a^{x}(\ln a)^{3}, f^{\prime \prime}(x) \quad a^{x}(\ln a)^{3} \\
& f^{(0)}(x)=a^{x}(\ln a)^{3}, \ldots, f^{(x)}(x) \quad a^{x}(\ln a)^{(x)}
\end{aligned}
$$

Putting $x=0$ in $f(x), f^{\prime}(x), f^{\prime \prime}(x), f^{(0)}(x), \ldots f^{(x)}(x)$, we get

$$
\begin{aligned}
& f(0)=a^{0}=1, f^{\prime}(0)=a^{0} \ln a=\ln a, f^{\prime}(0)=(\ln a)^{3}, f^{\prime \prime}(0) \quad(\ln a)^{3} \\
& f^{(0)}(0)=(\ln a)^{3}, \ldots, f^{(x)}(0) \quad(\ln a)^{x}
\end{aligned}
$$

Substituting these values in the formula

$$
\begin{aligned}
& f(x)=f(0)+f^{\prime}(0) x+\frac{f^{\prime}(0)}{12} x^{2}+\frac{f^{\prime \prime}(0)}{13} x^{3}+\ldots+\frac{f^{(x)}(0)}{1 \underline{n}} x^{4}+\ldots \text {, we have } \\
& a^{x}=1+(\ln a) . x+\frac{(\ln a)^{3}}{12} x^{2}+\frac{(\ln a)^{3}}{13} x^{3}+\ldots+\frac{(\ln a)^{7}}{1 \underline{n}} x^{4}+\ldots
\end{aligned}
$$

Note: If we put $0=\infty$ in the above expansion, we get

$$
\begin{aligned}
& e^{x}=1+x+\frac{x^{3}}{12}+\frac{x^{5}}{13}+\ldots+\frac{x^{7}}{1 \underline{n}}+\ldots \\
& \text { Replacing } x \text { by } 1 \text {, we have } \\
& e=1+1+\frac{1}{12}+\frac{1}{13}+\ldots+\frac{1}{1 \underline{n}}
\end{aligned}
$$

Example 4: $\quad$ Expand $(1+x)^{n}$ in the Maclaurin series.

Solution: Let $f(x)=(1+x)^{n}$, then

$$
\begin{aligned}
& f^{\prime}(x)=n(1+x)^{n-1}, \quad f^{\prime \prime}(x)=n(n-1)(1+x)^{n-2} \\
& f^{\prime \prime}(x)=n(n-1)(n-2)(1+x)^{n-3}, f^{(1)}(x)=n(n-1)(n-2)(n-3)(1+x)^{n-4}
\end{aligned}
$$

Putting $x=0$, we get

$$
\begin{aligned}
& f(0)=(1+0)^{2}=1, f^{\prime}(0)=n(1+0)^{n-1}=n \\
& f^{\prime}(0)=n(n-1)(1+0)^{n-2}=n(n-1) \\
& f^{\prime \prime}(0)=n(n-1)(n-2)(1+0)^{n-3}=n(n-1)(n-2) \\
& f^{(1)}(0)=n(n-1)(n-2)(n-3)(1+0)^{n-4}=n(n-1)(n-3)
\end{aligned}
$$

Substituting these values in the formula

$$
\begin{aligned}
& f(x)=f(0) \quad f^{\prime}(0) \mathrm{s} x \quad \frac{f^{\prime \prime}(0)}{\lfloor 2 \alpha^{2}} \quad \frac{f^{\prime \prime}(0)}{\lfloor 3 \alpha^{2}} \quad \ldots, \text { we have } \\
& (1+x)^{n} \neq 1 \quad n+x \quad \frac{n(n-1)}{\lfloor 2 \alpha^{2}} \quad \frac{n(n-1)(n-2)}{\lfloor 3 \alpha^{2}+\ldots}
\end{aligned}
$$

### 2.17 TAILOR SERIES EXPANSIONS OF FUNCTIONS:

If $f$ is defined in the interval containing ' $\alpha$ ' and its derivatives of all orders exist at $x=\alpha$, then we can expand $f(x)$ as

$$
\begin{aligned}
f(x)= & f(a)+f^{\prime}(a)(x-a)+\frac{f^{\prime}(a)}{\lfloor 2}(x-a)^{2}+\frac{f^{\prime \prime}(a)}{\lfloor 3}(x-a)^{3} \\
& +\frac{f^{(1)}(a)}{\lfloor 4}(x-a)^{4}+\ldots+\frac{f^{(n)}(a)}{\lfloor n}(x-a)^{n}+\ldots
\end{aligned}
$$

Let $\quad f(x)=a_{0}+a_{1}(x-a)+a_{2}(x-a)^{2}+a_{3}(x-a)^{3}+a_{4}(x-a)^{4}+\ldots$ $+a_{n}(x-a)^{n}+\ldots$
Obviously $f(a)=a_{0}(\cdot ;$ putting $x=a$, all other terms vanish $)$

$$
\begin{aligned}
& f^{\prime}(x) \neq a_{1} \quad 2 a_{2}(x+a) \quad 3 a_{3}(x-a)^{2} \quad 4 a_{4}(x-a)^{3}+\ldots \quad n a_{5}(x-a)^{n-1} \quad \ldots \\
& f^{\prime \prime}(x)=2 a_{1}+6 a_{1}(x-a)+12 a_{4}(x-a)^{3}+\ldots+n(n-1) a_{n}(x-a)^{n-2}+\ldots \\
& f^{\prime \prime \prime}(x)=6 a_{1}+24 a_{4}(x-a)+\ldots \ldots
\end{aligned}
$$

Putting $x=a$, we get $f^{\prime \prime}(a)=a_{1} ; f^{\prime \prime \prime}(a)=2 a_{2} \Rightarrow a_{2}=\frac{f^{\prime \prime \prime}(a)}{\lfloor 2} ;=f^{\prime \prime \prime \prime}(a) \quad 6 a_{3}$
$\Rightarrow \quad a_{3}=\frac{f^{\prime \prime \prime \prime}(a)}{\lfloor 3}$

Following the above pattern, we have $\quad \frac{f^{(1)}(a)}{\lfloor}$
Substituting the values of $a_{0}, a_{1}, a_{2}, a_{3}, \ldots$, we get

$$
\begin{aligned}
f(x)=f(a)+f^{\prime}(a)(x-a)+\frac{f^{\prime \prime \prime}(a)}{\lfloor 2}(x-a)^{2}+\frac{f^{\prime \prime \prime \prime}(a)}{\lfloor 3}(x-a)^{3}+\ldots \\
+\frac{f^{(n)}(a)}{\lfloor n}(x-a)^{n}+\ldots
\end{aligned}
$$

This expansion is the Taylor series for $f$ at $x=a$. The expansionisonly valid if it is convergent.

If $\sigma=0$, then the above expansion becomes

$$
f(x)=f(0)+f^{\prime}(0) x+\frac{f^{\prime \prime \prime}(0)}{\lfloor 2} x^{2}+\frac{f^{\prime \prime \prime}(0)}{\lfloor 3} x^{3}+\ldots+\frac{f^{(n)}(0)}{\lfloor n} x^{n}+\ldots
$$

which is the Maclaurin series for $f$ at $x=a$.
Replacing $x$ by $x+h$ and $\alpha$ by $x$, the expansion in (A) can be written as
$f(x+h)=f(x)+f^{\prime}(x) h+\frac{f^{\prime \prime \prime}(x)}{\lfloor 2} h^{2}+\frac{f^{\prime \prime \prime \prime}(x)}{\lfloor 3} h^{3}+\ldots+\frac{f^{(n)}(x)}{\lfloor n} h^{n}+\ldots$ (B)
The expansions in (B) is termed as Taylor's Theorem and can be stated as: If $x$ and $h$ are two independent quantities and $f(x+h)$ can be expanded in ascending power of $h$ as an infinite series, then

$$
f(x+h)=f(x)+f^{\prime}(x) h+\frac{f^{\prime \prime}(x)}{\frac{1}{2}} h^{2}+\frac{f^{\prime \prime \prime}(x)}{\frac{1}{2}} h^{2}+\ldots+\frac{f^{(n)}(x)}{\frac{1}{2}} h^{n}+\ldots
$$

Example 1: Find the Taylor series expansion of $\ln (1+x)$ at $x=2$.
Solution: Let $f(x)=\ln (1+x)$, then $f(2)=\ln (1+2)=\ln 3$
Finding he successive derivatives of $\ln (1+x)$ and evaluating them at $x=2$

$$
\begin{aligned}
& f^{\prime}(x)=\frac{1}{1+x} \quad \text { and } f^{\prime}(2)=\frac{1}{1+2}=\frac{1}{3} \\
& f^{\prime \prime}(x)=(-1)(-2)(1+x)^{-\frac{1}{3}} \quad \text { and } f^{\prime \prime}(2)=(-1+2)^{-2}=-\frac{1}{9} \\
& f^{\prime \prime \prime}(x)=(-1)(-2)(1+x)^{-3} \quad \text { and } f^{\prime \prime}(2)=\frac{1}{2} \cdot(1+2)^{-2}=\frac{\frac{1}{2}}{27} \\
& f^{(n)}(x)=(-1)(-2)(-3)(1+x)^{-4}=(-1)^{2} \frac{1}{2}(1+x)^{-4} \text { and } f^{(n)}(2)=\frac{\frac{1}{3}}{81}
\end{aligned}
$$

The Taylor series expansions of $f$ at $x=a$ is

$$
f(x)=f(a)+f^{\prime}(a) \cdot(x-a)+\frac{f^{\prime}(a)}{\frac{1}{2}}(x-a)^{2}+\frac{f^{\prime \prime}(a)}{\frac{1}{2}}(x-a)^{3}+\ldots
$$

Now substituting the relative values, we have

$$
\begin{aligned}
& \ln (1+x)=\ln 3+\frac{1}{3}(x-2)+\frac{-1}{\frac{1}{2}}(x-2)^{2}+\frac{\frac{12}{27}}{\frac{1}{2}}(x-2)^{3}+\frac{-\frac{13}{81}}{\frac{1}{2}}(x-2)^{4}+\ldots \\
& =\ln 3+\frac{x-2}{1.3}-\frac{(x-2)^{2}}{2.3^{2}}+\frac{(x-2)^{2}}{3.3^{2}}-\frac{(x-2)^{3}}{4.3^{3}}+\ldots
\end{aligned}
$$

Example 2: Use the Taylor series expansion to find the value of $\sin 31^{\circ}$.
Solution: We take $a=30^{\circ}=\frac{\pi}{6}$

$$
\text { Let } f(x)=\sin x \text {, then } F\left(\frac{\pi}{6}\right) \quad \min \frac{\pi}{6} \quad \frac{1}{2}
$$

Now taking the successive derivative of $\sin x$ and evaluating them at $\frac{\pi}{6}$, we have

$$
\begin{array}{ll}
f^{\prime}(x)=\cos x & \text { and } f^{\prime}\left(\frac{\pi}{6}\right)=\cos \frac{\pi}{6}=\frac{\sqrt{3}}{2} \\
f^{\prime \prime \prime}(x)=-\sin x & \text { and } f^{\prime}\left(\frac{\pi}{6}\right)=\sin \frac{\pi}{6}-\frac{-1}{2} \\
f^{\prime \prime}(x)=-\cos x & \text { and } f^{\prime}\left(\frac{\pi}{6}\right)=\cos \frac{\pi}{6}-\frac{\sqrt{3}}{2} \\
f^{(n)}(x)=-(- \sin x)=\sin x & \text { and } f^{(n)}\left(\frac{\pi}{6}\right)=\sin \frac{\pi}{6}=\frac{1}{2}
\end{array}
$$

Thus the Taylor series expansion at $a=\frac{\pi}{6}$ is

$$
\begin{aligned}
\sin x= & \frac{1}{2}+\frac{\sqrt{3}}{2}\left(x-\frac{\pi}{6}\right)+\frac{-\frac{1}{2}}{\frac{1}{2}}\left(x-\frac{\pi}{6}\right)^{2}+\frac{-\frac{\sqrt{3}}{2}}{\frac{1}{2}}\left(x-\frac{\pi}{6}\right)^{3}+\ldots \\
& =\frac{1}{2}+\frac{\sqrt{3}}{2}\left(x-\frac{\pi}{6}\right)-\frac{1}{2 \frac{1}{2}}\left(x-\frac{\pi}{6}\right)^{2}-\frac{\sqrt{3}}{2 \frac{1}{2}}\left(x-\frac{\pi}{6}\right)^{3}+\ldots \\
\text { For } x= & 31^{\circ} \cdot x \quad \frac{\pi}{6}=\left(34^{\circ} \quad 30^{\circ}\right) \sim 4^{\circ} \quad .017455 \\
\sin 31^{\circ} & =\frac{1}{2}+\frac{\sqrt{3}}{2}(.017455)-\frac{1}{4}(.017455)^{2}-\frac{\sqrt{3}}{12}(.017455)^{3} \\
& \approx .5+.015116-0.000076 \approx .5150
\end{aligned}
$$

Example 3: $\quad$ Prove that $e^{a+b}=e^{a}\left(1+h+\frac{h^{2}}{2}+\frac{h^{3}}{2}+\ldots\right)$

Solution: Let $f(x+h)=e^{a+b_{0}}$ then $f(x) \quad e^{x} \quad \ldots$ (i)
By successive derivatives of (i) w.r.t ' $x$ ' we have

$$
f^{\prime}(x)=e^{x}, f^{\prime \prime}(x)=e^{x}, f^{\prime \prime}(x)=e^{x} \quad \text { etc. }
$$

By Taylor's Theorem we have

$$
f(x+h)=f(x)+h f^{\prime}(x)+\frac{h^{2}}{12} f^{\prime \prime \prime}(x)+\frac{h^{3}}{12}+f^{\prime \prime \prime \prime}(x)+\ldots
$$

Putting the relative values, we get

$$
\begin{aligned}
e^{x+h} & =e^{x}+h e^{x}+\frac{h^{2}}{12} e^{x}+\frac{h^{3}}{12} e^{x}+\ldots \\
& =e^{x}\left[1+h+\frac{h^{2}}{12}+\frac{h^{3}}{12}+\ldots\right]
\end{aligned}
$$

## EXERCISE 2.8

1. Apply the Maclaurin series expansion to prove that:
(i) $\ln (1+x)=x-\frac{x^{2}}{2}+\frac{x^{3}}{2}-\frac{x^{4}}{2}+\ldots \ldots$
(ii) $\cos x=1-\frac{x^{2}}{12}+\frac{x^{4}}{14}-\frac{x^{6}}{16}+\ldots \ldots$
(iii) $\sqrt{1+x}=1+\frac{x}{2}-\frac{x^{2}}{8}+\frac{x^{3}}{16}+\ldots \ldots$
(iv) $e^{x} \quad=1+x+\frac{x^{2}}{12}+\frac{x^{3}}{13}+\ldots \ldots$
(v) $e^{2 x}=1+2 x+\frac{4 x^{2}}{12}-\frac{8 x^{3}}{13}+\ldots \ldots$
2. Show that:
$\cos (x+h)=\cos x-h \sin x-\frac{h^{2}}{12} \cos x+\frac{h^{3}}{12} \sin x+\ldots \ldots$
and evaluate $\cos 61^{\circ}$.
3. Show that $2^{x+h}=2^{x}\{1+(\ln 2) h+\frac{(\ln 2)^{2} h^{2}}{12}+\frac{(\ln 2)^{3} h^{3}}{12}+\ldots\}$

## 2.18 GEOMETRICAL INTERPRETATION OF A DERIVATIVE

Let $A B$ be the arc of the graph of $f$ defined by the equation $y=f(x)$.
Let $P(x, f(x))$ and $Q(x+\delta x, f(x+\delta x))$ be two neighbouring points on the arc $A B$ where $x$, $x+\delta x \in D_{f}$.

The line $P Q$ is secant of the curve and it makes $\angle X S Q$ with the positive direction of the $x$-axis. (See the figure 2.21.1)

Drawing the ordinates $P M, Q N$ and perpendicular $P R$ to $N Q$, we have
$R Q=N Q-N R=N Q-M P=f(x+\delta x)-f(x)$
FIGURE 2.21.1
and $P R=M N=O N-O M=x+\delta x-x=\delta x$
Thus $\tan m \angle X S Q=\tan m \angle R P Q$
$=\frac{R Q}{P R}=\frac{f(x+\delta x)-f(x)}{\delta x}$
Revolving the secant line $P Q$ about $P$ towards $P$, some of its successive positions $P Q_{i}, P Q_{j}, P Q_{k}, \ldots$ are shown in the figure 2.21.2. Points $Q_{i}(i=1,2,3, \ldots)$ are getting closer and closer to the point $P$ and $P R$, i.e; $\delta x_{i}(i=1,2,3, \ldots)$ are approaching to zero.

In other words we can say that the revolving secant line approaches the tangent line $P T$ as its limiting position at $P$ while $\delta x$ approaches zero, that is,
$\tan m \angle X S Q \rightarrow \tan m \angle X T P$ when $\delta \mathrm{x} \rightarrow 0$
or $\frac{f(x+\delta x)-f(x)}{\delta x} \rightarrow \tan m \angle X T P$ as $\delta x \rightarrow 0$
so $\lim _{\delta x \rightarrow 0} \frac{f(x+\delta x)-f(x)}{\delta x}=\tan m \angle X T P$
$$
\text { or } \quad f^{\prime}(x)=\tan m \angle X T P
$$

Thus the slope of the tangent line to the graph of $f$ at $(x, f(x))$ is $f^{\prime}(x)$.
Example 1: $\quad$ Discuss the tangent line to the graph of the function $|x|$ at $x=0$.

Solution: Let $\quad f(x)=|x|$

$$
\begin{aligned}
& f(0)=|0|=0 \quad \text { and } \\
& f(0+\delta x)=|0+\delta x|=|\delta x| \\
& \text { so } \quad f(0+\delta x)-f(0)=|\delta x|-0 \\
& \text { and } \quad \frac{f(0+\delta x)-f(0)}{\delta x}=\frac{|\delta x|}{\delta x} \\
& \text { Thus } f^{\prime}(0)=\lim _{\delta x \rightarrow 0} \frac{|\delta x|}{\delta x} \\
& \text { Because }|\delta x|=\delta x \quad \text { when } \delta x>0 \\
& \text { and } \quad|\delta x|=-\delta x \quad \text { when } \delta x<0
\end{aligned}
$$

so we consider one-sided limits

$$
\begin{aligned}
& \lim _{\delta x \rightarrow 0^{+}} \frac{|\delta x|}{\delta x}=\lim _{\delta x \rightarrow 0^{-}} \frac{\delta x}{\delta x}=1 \\
& \text { and } \lim _{\delta x \rightarrow 0^{-}} \frac{|\delta x|}{\delta x}=\lim _{\delta x \rightarrow 0^{-}} \frac{-\delta x}{\delta x}-1
\end{aligned}
$$

The right hand and left hand limits are not equal, therefore, the $\lim _{\delta x \rightarrow 0^{-}} \frac{|\delta x|}{\delta x}$ does not exist.

This means that $f^{\prime}(0)$, the derivative of $f$ at $x=0$ does not exist and there is no tangent line to the graph of $f$ and $x=0$
(see the figure 2.21.3).

Example 2: Find the equations of the tangents to the curve $x^{2}-y^{2}-6 y=0$ at the point whose abscissa is 4 .

Solution. Given that $x^{2}-y^{2}-6 y=0$
We first find the $y$-coordinates of the points at which the equations of the tangents are to be found. Putting $x=4$ is (i) gives

$$
\begin{aligned}
& 16-y^{2}-6 y=0 \quad \Rightarrow y^{2}+6 y-16=0 \\
& \text { or } y=\frac{-6 \pm \sqrt{36+64}}{2}=\frac{-6 \pm \sqrt{100}}{2}=\frac{-6 \pm 10}{2}, \text { that is, } \\
& y=\frac{-6+10}{2}=\frac{4}{2}=2 \quad \text { or } \quad y=\frac{-6-10}{2}=\frac{-16}{2}=-8
\end{aligned}
$$

Thus the points are $(4,2)$ and $(4,-8)$.
Differentiating (i) w.r.t. ' $x$ ' we have

$$
2 x-2 y \frac{d y}{d x}-6 \frac{d y}{d x}=0 \quad \Rightarrow 2 \frac{d y}{d x}(y+3)=2 x \quad \Rightarrow \frac{d y}{d x}=\frac{x}{y+3}
$$

The slope of the tangent to (i) at $(4,2)==\frac{4}{2+3}=\frac{4}{5}$.
Therefore, the equation of the tangent to (i) at $(4,2)$ is

$$
\begin{aligned}
& y-2=\frac{4}{5}(x-4) \quad \Rightarrow 5 y-10=4 x-16 \\
& \text { or } \quad 5 y=4 x-6
\end{aligned}
$$

The slope of the tangent to (i) at $(4,-8)=\frac{4}{-8+3}=\frac{4}{5}$.
Therefore the equation of the tangent to (i) at $(4,-8)$ is

$$
\begin{aligned}
& y-(-8)=-\frac{4}{5}(x-4) \\
& 5 y+40=-4 x+16 \quad \Rightarrow 4 x+5 y+24=0
\end{aligned}
$$

## 2.19 INCREASING AND DECREASING FUNCTIONS

Let $f$ be defined on an interval $(a, b)$ and let $x_{1}, x_{2} \in(a, b)$. Then
(i) $f$ is increasing on the interval $(a, b)$ if $f\left(x_{2}\right)>f\left(x_{1}\right)$ whenever $x_{2}>x_{1}$
(ii) $f$ is decreasing on the interval $(a, b)$ if $f\left(x_{2}\right)<f\left(x_{1}\right)$ whenever $x_{2}>x_{1}$
We see that a differentiable function $f$ is increasing on $(a, b)$ if tangent lines to its graph at all points $(x, f(x))$ where $x \in(a, b)$ have positive slopes, that is,
$f^{\prime}(x)>0$ for all $x$ such that $a<x<b$
and $f$ is decreasing on $(a, b)$ if tangent lines to its graph at all points $(x, f(x))$ where $x \in(a, b)$, have negative slopes, that is, $f^{\prime}(x)<0$ for all $x$ such that $a<x<b$

Now we state the above observation in the following theorem.

## Theorem:

Let $f$ be a differentiable function on the open interval (a,b). Then
(i) $f$ is increasing on $(a, b)$ if $f^{\prime}(x)>0$ for each $x \in(a, b)$
(ii) $f$ is decreasing on $(a, b)$ if $f^{\prime}(x)<0$ for each $x \in(a, b)$

Let $f(x)=x^{2}$, then

$$
f\left(x_{2}\right)-f\left(x_{1}\right)=x_{2}^{2}-x_{1}^{2}=\left(x_{2}-x_{1}\right)\left(x_{2}+x_{1}\right)
$$

If $\quad x_{1}, x_{2} \in(-\infty, 0)$ and $x_{2}>x_{1}$, then
version: 1.1

$$
\begin{aligned}
& f\left(x_{2}\right)-f\left(x_{1}\right)<0 \quad\left(\because x_{2}-x_{1}>0 \text { and } x_{2}+x_{1}<0\right) \\
& \Rightarrow f\left(x_{2}\right)<f\left(x_{1}\right) \\
& \Rightarrow f \text { is decreasing on the interval }(-\infty, 0) \\
& \text { If } x_{1}, x_{2} \in(0, \infty) \text { and } x_{2}>x_{1} \text {, then } \\
& f\left(x_{2}\right)-f\left(x_{1}\right)>0 \quad\left(\because x_{2}-x_{1}>0 \text { and } x_{2}+x_{1}>0\right) \\
& \Rightarrow f\left(x_{2}\right)>f\left(x_{1}\right) \\
& \Rightarrow f \text { is increasing on the interval }(0, \infty)
\end{aligned}
$$

Here $f^{\prime}(x)=2 x$ and $f^{\prime}(\mathbf{x})-\mathbf{0}$ for all $x \quad(\quad, 0)$, therefore,
$f$ is decreasing on the interval $(-\infty, 0)$
Also $f^{\prime}(x)>0$ for all $x \in(0, \infty)$, so $f$ is increasing on the interval $(0, \infty)$.
From the above theorem we can conclude that

1. $f^{\prime}\left(x_{1}\right)<0 \Rightarrow f$ is decreasing at $x_{1}$
2. $f^{\prime}\left(x_{1}\right)=0 \Rightarrow f$ is neither increasing nor decreasing at $x_{1}$
3. $f^{\prime}\left(x_{1}\right)>0 \Rightarrow f$ is increasing at $x_{1}$

Now we illustrate the ideas discussed so far considering the function $f$ defined as
$f(x)=4 x-x^{2}$
To draw the graph of $f$, we form a table of some ordered pairs which belongs to $f$

| $x$ | -1 | 0 | 1 | 2 | 3 | 4 | 5 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| $y=f(x)$ | -5 | 0 | 3 | 4 | 3 | 0 | -5 |

From the graph of *f*, it is obvious that *y* rises from 0 to 4 as *x* increases from 0 to 2 and *y* falls from 4 to 0 as *x* increases from 2 to 4.

In other words, we can say that the function *f* defined as in (I) is increasing in the interval 0 < *x* < 2 and is decreasing in the interval 2 < *x* < 4.

The slope of the tangent to the graph of *f* at any point in the interval 0 < *x* < 2, in which the function *f* is increasing is positive because it makes an acute angle with the positive direction of *x*-axis. (See the tangent line to the graph of *f* at (1, 3)).

But the slope of the tangent line to the graph of *f* at any point in the interval 2 < *x* < 4 in which the function *f* is decreasing is negative as it makes an obtuse angle with the positive direction of *x*-axis. (See the tangent line to the graph of *f* at (3, 3)).

As we know that the slope of the tangent line to the graph of *f* at (*x*, *f*(*x*)) is *f* (*x*), so the derivative of the function *f* i.e., *f* (*x*), is positive in the interval in which *f* is increasing and *f* (*x*), is negative in the interval in which *f* is decreasing.

The function *f* under consideration is actually increasing at each *x* for which *f* (*x*) > 0.

$$
\text{i.e. } 4 - 2x > 0 \qquad \Rightarrow -2x > -4 \qquad \Rightarrow x < 2
$$

Thus it is increasing in the interval (-∞, 2). Similarly we can show that it is decreasing, in the interval (2, ∞).

Now we give an analytical approach to the above discussion.

Let *f* be an increasing function in some interval in which it is differentiable. Let *x* and *x* + *δx* be two, points in that interval such that *x* + *δx* > *x*.

As the function *f* is increasing in the interval, it conveys the fact that *f*(*x* + *δx*) > *f*(*x*).

Consequently we have, *f*(*x* + *δx*) - *f*(*x*) > 0 and (*x* + *δx*) - *x* > 0, that is,

$$
f(x + \deltax) - f(x) > 0 \text{ and } \deltax > 0
$$

or

$$
\frac{f(x + \deltax) - f(x)}{\delta x} > 0
$$

The above difference quotient becomes one-sided limit

$$
\lim_{\deltax \to 0} \frac{f(x + \deltax) - f(x)}{\delta x}
$$

As *f* is differentiable, so *f* (*x*) exists and one sided limit must equal to *f* (*x*). Thus *f* (*x*) > 0.

### Example 1: Determine the values of *x* for which *f* defined as *f*(*x*) = *x*² + 2*x* − 3 is

(i) increasing (ii) decreasing.

(iii) find the point where the function is neither increasing nor decreasing.

**Solution:** The table of some ordered pairs satisfying *f*(*x*) = *x*² + 2*x* − 3 is given below:

|  *x* | -4 | -3 | -2 | -1 | 0 | 1 | 2  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  *y* = *f*(*x*) | 5 | 0 | -3 | -4 | -3 | 0 | 5  |

The graph of $f$ is shown in the figure2.22.2.

$$
f^{\prime}(x)=2 x+2
$$

(i) The condition $f^{\prime}(x)>0 \quad \Rightarrow 2 x+2>0$

$$
\Rightarrow 2 x \quad>-2
$$

which gives $x>-1$, so the function $f$ defined as $f(x)=x^{2}+2 x-3$ is increasing in the interval $(-1, \infty)$.
(ii) And the condition $f^{\prime}(x)<0 \Rightarrow 2 x+2<0$

$$
\Rightarrow 2 x<-2
$$

which gives $x<-1$, so the function $f$ under consideration in the example I is decreasing in the interval $(-\infty,-1)$.
(iii) The function is neither increasing nor decreasing where $f^{\prime}(x)=0$, that is,

$$
2 x+2=0 \quad \Rightarrow x=-1
$$

If $x=-1$ then $f(-1)=(-1)^{2}+2(-1)-3=-4$. Thus $f$ is neither increasing nor deceasing at the point $(-1,-4)$.
Note: Any point where $f$ is neither increasing nor decreasing is called a stationary point, provided that $f^{\prime}(x)=0$ at that point.

Example 2: Determine the intervals in which $f$ is increasing or it is decreasing if

$$
f(x)=x^{2}-6 x^{2}+9 x
$$

Solution. $f^{\prime}(x)=3 x^{2}-12 x+9$

$$
\begin{aligned}
& =3\left(x^{2}-4 x+3\right) \\
& =3(x-1)(x-3) \\
& f^{\prime}(x)>0 \\
\Rightarrow & x^{2}-4 x+3>0 \\
\Rightarrow & (x-1)(x-3)>0
\end{aligned}
$$

$(x-1)(x-3)>0^{\prime}$ in the intervals $(-\infty, 1)$ and $(3, \infty)$
$f^{\prime}(x)<0 \quad \Rightarrow(x-1)(x-3)<0$
$(x-1)(x-3)<0$ if $x>1$ and $x<3$ that is $1<x<3$

### 2.20 RELATIVE EXTREMA

Let $(c-\delta x, c+\delta x) \subseteq D_{c^{-}},($domain of a function $f)$, where $\delta x$ is small positive number.

If $f(c) \geq f(x)$ for all $x \in(c-\delta x, c+\delta x)$ then the function $f$ is said to have a relative maxima at $x=c$.

Similarly if $f(c) \leq f(x)$ for all $x \in(c-\delta x, c+\delta x)$, then the function $f$ has relative minima at $x=c$.

Both relative maximum and relative minimum are called in general relative extrema.

The graph of a function is shown in the adjoining figure. It has relative maxima at $x=b$ and $x=d$. But at $x=a$ and $x=c$, it has relative minima.

Note that the relative maxima at $x=d$ is not the highest point of the graph.

### 2.21 CRITICAL VALUES AND CRITICAL POINTS

If $c \in D f$ and $f^{\prime}(c)=0$ or $f^{\prime}(c)$ does not exist, then the number $c$ is called a critical value for $f$ while the point $(c, f(c))$ on the graph of $f$ is named as a critical point.

Note: There are functions which have extrema (maxima or minima) at the points where their derivatives do not exist. For example, the derivatives of the function $f$ and $\phi$ defined as.

$$
\begin{gathered}
f(x)=|x| \\
\text { and } \phi(x)=\left[\begin{array}{l}
2-x \quad x>0 \\
2+x \quad x \leq 0
\end{array}\right.
\end{gathered}
$$

do not exist at $(0,0)$ and $(0,2)$ respectively.
But $f$ has minima at $(0,0)$ and $\phi$ has maxima at $(0,2)$. See the adjoining figures.

Those critical points on the graph of $f$ at which $f^{\prime}(x)=0$ are called stationary points of $f$.

Now we discuss relative maxima and relative minima of the differentiable function $f$ defined as:

$$
y=f(x)=x^{3}-3 x^{2}+4 \ldots(1)
$$

Graph of $f$ is drawn with the help of some ordered pairs tabulated as below:

| $X$ | $-3 / 2$ | -1 | $-1 / 2$ | 0 | $1 / 2$ | 1 | $3 / 2$ | 2 | $5 / 2$ | 3 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| $Y$ | $-49 / 8$ | 0 | $25 / 8$ | 4 | $27 / 8$ | 2 | $5 / 8$ | 0 | $7 / 8$ | 4 |

Now differentiating (i) w.r.t. ' $x$ ' we get

$$
\begin{aligned}
& f^{\prime}(x)=3 x^{2}-6 x=3 x(x-2) \\
& f^{\prime}(x)=0 \quad \Rightarrow 3 x(x-2)=0 \quad \Rightarrow x=0 \text { or } x=2
\end{aligned}
$$

Now we consider an interval $(-\delta x, \delta x)$ in the neighbourhood of $x=0$. Let $0-\varepsilon$ is a point in the interval $(-\delta x, 0)$ We see that

$$
\begin{aligned}
& f^{\prime}(0-\varepsilon)=3(-\varepsilon)(-\varepsilon-2) \\
& =3 \varepsilon(\varepsilon+2)>0 \quad(\because \varepsilon>0, \varepsilon+2>0)
\end{aligned}
$$

That is $f^{\prime}(x)$ is positive for all $x \in(-\delta x, 0)$.
Let $0+\varepsilon_{1}$ is a point in the interval $(0, \delta x)$, then we have

$$
\begin{aligned}
f^{\prime}\left(0+\varepsilon_{1}\right) & =3\left(\varepsilon_{1}\right)\left(\varepsilon_{1}-2\right) \\
& =3 \varepsilon_{1}\left(2 \varepsilon_{1}\right) \quad 0\left(\because 2-\varepsilon_{1}>0, \varepsilon_{1}>0\right), \text { that is, }
\end{aligned}
$$

$f^{\prime}(x)$ is negative for all $x \in(0, \delta x)$
We note that $f^{\prime}(x)>0$ before $x=0, f^{\prime}(x)=0$ at $x \ll 0$ and $f^{\prime}(x) \quad 0$ after $x=0$.
The graph of $f$ shows that it has relative maxima at $x=0$.
Thus we conclude that a function has relative maxima at $x=c$ if $f^{\prime}(x)>0$, before $x=c f^{\prime}(c)=0$ and $f^{\prime}(x)<0$ after $x=c$.

Considering an interval $(2-\delta x, 2+\delta x)$ in the neighbourhood of $x=2$ we find the values of $f^{\prime}(2-\varepsilon)$ and $f^{\prime}(2+\varepsilon)$ when $2-\varepsilon \in(2-\delta x, 2)$ and $2+\varepsilon \in(2,2+\delta x)$

$$
\begin{aligned}
f^{\prime}(2-\varepsilon) & =3(2-\varepsilon)(2-\varepsilon-2) & {\left[\because f^{\prime}(x)=3 x(x-2)\right]} \\
& =3(2-\varepsilon)(-\varepsilon) & \\
& =-3 \varepsilon(2-\varepsilon)<0 & (\because \varepsilon>0,2-\varepsilon>0) \\
\text { and } f^{\prime}(2+\varepsilon) & =3(2+\varepsilon)(2+\varepsilon-2) & \\
& =3 \varepsilon(2+\varepsilon)>0 & (\because \varepsilon>0,2+\varepsilon>0)
\end{aligned}
$$

We see that $f^{\prime}(x)<0$ before $x=2, f^{\prime}(x)=0$ at $x=2$ and $f^{\prime}(x)>0$ after $x=2$.
It is obvious from the graph that it has relative minima at $x=2$.
Thus we conclude that a function has relative minima at $x=c$ if $f^{\prime}(x)<0$ before $x=c, f^{\prime}(x)=0$ at $x=c$ and $f^{\prime}(x)>0$ after $x=c$.

## First Derivative Rule:

Let $f$ be differentiable in neighbourhood of $c$ where $f^{\prime}(c)=0$.

1. If $f^{\prime}(x)$ changes sign from positive to negative as $x$ increases through $c$, then $f(c)$ the relative maxima of $f$.
2. If $f^{\prime}(x)$ changes sign from negative to positive as $x$ increases through $c$, then $f(c)$ is the relative minima of $f$.

Note: 1. A stationary point is called a turning point if it is either a maximum point or a minimum point.
2. If $f^{\prime}(x)>0$ before the point $x=a, f^{\prime}(x)=0$ at $x=0$ and $f^{\prime}(x)>0$ after $x=0$, then $f$ does not has a relative maxima.
See the graph of $f(x)=x^{3}$. In this case, we have

$$
\begin{aligned}
& f^{\prime}(x)=3 x^{2}, \text { that is, } \\
& f^{\prime}(0-\varepsilon)=3(-\varepsilon)^{2}=3 \varepsilon^{2}>0 \\
& \text { and } f^{\prime}(0+\varepsilon)=3(\varepsilon)^{2}=3 \varepsilon^{2}>0
\end{aligned}
$$

The function $f$ is increasing before $x=0$ and also it is increasing after $x=0$.
Such a point of the function is called the point of inflexion.
## Second Derivative Test:

We have noticed that the first derivative $f^{\prime}(x)$ of a function changes its sign from positive to negative at the point where $f$ has relative maxima, that is, $f^{\prime}$ is a decreasing function in the neighbouring interval containing the point where $f$ has relative maxima.

Thus $f^{\prime \prime}(x)$ is negative at the point where $f$ has a relative maxima.
But $f^{\prime}(x)$ of a function $f$ changes its sign from negative to positive at the point where $f$ has relative minima, that is, $f^{\prime}$ is an increasing function in the neighbouring interval containing the point where $f$ has relative minima.

Thus $f^{\prime \prime}(x)$ is positive at the point where $f$ has relative minima.

## Second Derivative Rule

Let $f$ be differential function in a neighbourhood of $c$ where $f^{\prime}(c)=0$. Then

1. $f$ has relative maxima at $c$ if $f^{\prime \prime}(c)<0$.
2. $f$ has relative minima at $c$ if $f^{\prime \prime}(c)>0$.

Example 1: $\quad$ Examine the function defined as

$$
f(x)=x^{3}-6 x^{2}+9 x \text { for extreme values. }
$$

Solution: $f^{\prime}(x)=3 x^{2}-12 x+9$

$$
=3\left(x^{2}-4 x+3\right)=3(x-1)(x-3)
$$

## First Method

If $x=1-\varepsilon$ where $\varepsilon$ is very very small positive number, then

$$
\begin{aligned}
& (x-1)(x-3)=(1-\varepsilon-1)(1-\varepsilon-3)=(-\varepsilon)(-\varepsilon-2)=\varepsilon(2+\varepsilon)>0 \text { that is } \\
& f^{\prime}(x)>0 \text { before } x=1 . \text { For } x=1 \quad \varepsilon \text {, we have } \\
& (x-1)(x-3)=(1+\varepsilon-1)(1+\varepsilon-3)=( \varepsilon)(-2+\varepsilon)=-\varepsilon(2-\varepsilon)<0
\end{aligned}
$$

That is, $f^{\prime}(x)<0$ after $x=1$
As $f^{\prime}(x)>0$ before $x=1, f^{\prime}(x)=0$ at $x \quad 1$ and $f^{\prime}(x)<0$ after $x \quad 1$
Thus $f$ has relative maxima at $x=1$ and $f(1)=-1-6+9=4$.
Let $x=3-\varepsilon$, then

$$
(x-1)(x-3)=(3-\varepsilon-1)(3-\varepsilon-3)=(2-\varepsilon)(-\varepsilon)=-\varepsilon(2-\varepsilon)<0
$$

That is $f^{\prime}(x)<0$ before $x=3$.
For $x=3+\varepsilon$

$$
(x-1)(x-3)=(3+\varepsilon-1)(3+\varepsilon-3)=(2+\varepsilon)(\varepsilon)>0
$$

That is, $f^{\prime}(x)>0$ after $x=3$.
As $f^{\prime}(x)<0$ before $x=3, f^{\prime}(x)$ at $x=3$ and $f^{\prime}(x)>0$ after $x=3$,
Thus $f$ has relative minima at $x=3$. and $f(3)=3(3)^{2}-12(3)+9=0$
Second Method: $f^{\prime \prime}(x)=3(2 x-4)=6(x-2)$

$$
f^{\prime \prime}(1)=6(1-2)=-6<0 \text {, therefore, }
$$

$f$ has relative maxima at $x=1$ and $f(1)=(1)^{2}-6(1)^{2}+9(1)$

$$
=1-6+9=4
$$

$f^{\prime \prime}(3)=6(3-2)=6>0$, therefore $f$ has relative minima at $x=3$ and $f(3)=27-54+27=0$

Example 2: Examine the function defined as $f(x)=1+x^{3}$ for extreme values
Solution: Given that $f(x)=1+x^{3}$
Differentiating w.r.t. ' $x$ ' we get $f^{\prime}(x)=3 x^{2}$

$$
\begin{array}{ll}
f^{\prime}(x)=0 & \Rightarrow 3 x^{2}=0 \\
f^{\prime \prime}(x)=6 x & \text { and } f^{\prime \prime}(0)=6(0)=0
\end{array}
$$

The second derivative does not help in determining the extreme values.

$$
\begin{aligned}
& f^{\prime}(0-\varepsilon)=3(0-\varepsilon)^{2}=3 \varepsilon^{2}>0 \\
& f^{\prime}(0+\varepsilon)=3(0+\varepsilon)^{2}=3 \varepsilon^{2}>0
\end{aligned}
$$

As the first derivative does not change sign at $x=0$, therefore $(0,0)$ is a point of inflexion.

Example 3: Discuss the function defined as $f(x)=\sin x+\frac{1}{2 \sqrt{2}} \cos 2 x$ for extreme values in the interval $(0,2 \pi)$.

Solution: Given that $f(x)=\sin x+\frac{1}{2 \sqrt{2}} \cos 2 x$

$$
\begin{aligned}
& f^{\prime}(x)=\cos x+\frac{1}{2 \sqrt{2}}(-2 \sin 2 x)=\cos x-\frac{1}{\sqrt{2}} \sin 2 x \\
& =\cos x \quad \frac{1}{\sqrt{2}}(2 \sin x-\cos x) \quad \cos x \quad \sqrt{2} \sin x \cos x \\
& =\cos x(1-\sqrt{2} \sin x)
\end{aligned}
$$

Now $f^{\prime}(x)=0 \quad \Rightarrow \cos x(1-\sqrt{2} \sin x)=0$

$$
\Rightarrow \cos x=0 \quad \Rightarrow x=\frac{\pi}{2} \cdot \frac{3 \pi}{2}
$$

or $\quad 1-\sqrt{2} \sin x=0 \quad \Rightarrow \sin x=\frac{1}{\sqrt{2}} \quad \Rightarrow x=\frac{\pi}{4} \cdot \frac{3 \pi}{4}$
Differentiating (i) w.r.t. ' $x$ ', we have

$$
f^{\prime \prime \prime}(*)=\sin x \quad \frac{1}{\sqrt{2}}(\cos 2 x) \cdot 2-\sin x \quad \sqrt{2} \cos 2 x
$$

As $f^{\prime \prime \prime}\left(\frac{\pi}{2}\right)=-\sin \frac{\pi}{2}-\sqrt{2} \cos \pi=-1-\sqrt{2} \times(-1)=\sqrt{2}-1>0$
and $f^{\prime \prime \prime}\left(\frac{3 \pi}{2}\right)=-\sin \frac{3 \pi}{2}-\sqrt{2} \cos 3 \pi=-(-1)-\sqrt{2}(-1)=1+\sqrt{2}>0$
Thus $f(x)$ has minimum values for $x=\frac{\pi}{2}$ and $x=\frac{3 \pi}{2}$
As $f^{\prime \prime \prime}\left(\frac{\pi}{4}\right)=\sin \frac{\pi}{4} \quad \sqrt{2} \cos \frac{\pi}{2}-\frac{1}{\sqrt{2}} \cdot \sqrt{2}<0 \quad \frac{1}{\sqrt{2}} \quad 0$
and $f^{\prime \prime \prime}\left(\frac{3 \pi}{4}\right)=\sin \frac{3 \pi}{4} \quad \sqrt{2} \cos \frac{3 \pi}{2}-\frac{1}{\sqrt{2}} \cdot \sqrt{2}<0 \quad \frac{1}{\sqrt{2}} \quad 0$
Thus $f(x)$ has minimum values for $x=\frac{\pi}{4}$ and $x=\frac{3 \pi}{4}$

## EXERCISE 2.9

1. Determine the intervals in which $f$ is increasing or decreasing for the domain mentioned in each case.
(i) $f(x)=\sin x$
; $\quad x \in(-\pi, \pi)$
(ii) $f(x)=\cos x$
; $\quad x \in\left(\frac{-\pi}{2}, \frac{\pi}{2}\right)$
(iii) $f(x)=4-x^{2}$
; $\quad x \in(-2,2)$
(iv) $f(x)=x^{2}+3 x+2$
; $\quad x \in(-4,1)$
2. Find the extreme values for the following functions defined as:
(i) $f(x)=1-x^{3}$
(ii) $f(x)=x^{2}-x-2$
(iii) $f(x)=5 x^{2}-6 x+2$
(iv) $f(x)=3 x^{2}$
(v) $f(x)=3 x^{2}-4 x+5$
(vi) $f(x)=2 x^{2}-2 x^{2}-36 x+3$

(vii) $f(x)=x^{x}-4 x^{2}$
(viii) $f(x)=(x-2)^{2}(x-1)$
(ix) $f(x)=5+3 x-x^{2}$
3. Find the maximum and minimum values of the function defined by the following equation occurring in the interval $[0.2 \pi]$
$f(x)=\sin x+\cos x$.
4. Show that $y=\frac{\ln x}{x}$ has maximum value at $x=e$.
5. Show that $y=x^{e}$ has a minimum value at $x=\frac{1}{e}$.

## Application of Maxima and Minima

Now we apply the concept of maxima and minima to the practical problems. We first form the functional relation of the form $y=f(x)$ from the given information and find the maximum or minimum value of $f$ as required. Here we solve some examples relating to maxima and minima problems.

Example 1: Find two positive integers whose sum is 9 and the product of one with the square of the other will be maximum.

Solution: Let $x$ and $9-x$ be the two required positive integers such that

$$
x(9-x)^{2} \text { will be maximum. }
$$

Let $f(x)=x(9-x)^{2}$. Then

$$
\begin{aligned}
f^{\prime}(x) & =1 \cdot(9-x)^{2}+x \cdot 2(9-x) \times(-1) \\
& =(9-x)[9-x-2 x]=(9-x)(9-3 x)=3(9-x)(3-x) \\
f^{\prime}(x) & =0 \Rightarrow 3(9-x)(3-x)=0 \Rightarrow x=9 \text { or } x=3
\end{aligned}
$$

In this case $x=9$ is not possible because

$$
\begin{aligned}
& 9-x=9-9=0 \text { which is not positive integer. } \\
& f^{\prime \prime}(x)=3 \frac{1}{(}-1)(3-x)+(9-x) \times(-1)=3 \frac{1}{}-3+x-9+x \frac{1}{}
\end{aligned}
$$

$$
=3 \frac{1}{2 x}-12 \frac{1}{}=6(x-6)
$$

As $f^{\prime \prime}(3)=6(3-6)=6(-3)=-18$ which is negative.
Thus $f(x)$ gives the maximum value if $x=3$, so the other positive integer is 6 because $9-3=6$.

Example 2: What are the dimensions of a box of a square base having largest volume if the sum of one side of the base and its height is 12 cm .

Solution: Let the length of one side of the base (in cm ) be $x$ and the height of the box (in cm ) be h , then $\mathrm{V}=x^{2} h$

It is given that $x+h=12 \quad \Rightarrow h=12-x$
Thus $\mathrm{V}=\mathrm{x}^{2}(12-\mathrm{x})$ and

$$
\begin{aligned}
\frac{d V}{d x}= & 2 x(12-x)+x^{2}(-1)=24 x-3 x^{2}=3 x(8-x) \\
& \frac{d V}{d x}=0 \Rightarrow 3 x(8-x)=0 . \text { In this case } \mathrm{x} \text { cannot be zero, } \\
\text { so } \quad & 8-x=0 \Rightarrow x=8 . \\
& \frac{d^{2} V}{d x^{2}}=24-6 x \text { which is negative for } x=8
\end{aligned}
$$

Thus $V$ is maximum if $x=8(c m)$ and $h=12-8=4(c m)$
Example 3: The perimeter of a triangle is 20 centimetres. If one side is of length 8 centimetres, what are lengths of the other two sides for maximum area of the triangle?

Solution: Let the length of one unknown side (in cm ) be $x$, then the length of the other unknown side (in cm ) will be $20-x-8=12-x$.

Let $y$ denote the square of the area of the triangle, then we have

$$
\begin{aligned}
& y=10(10-8)(10-x)(10-12+x) \quad\left(1 / x-\frac{20}{2}-10 \text { and area of the triangle } \sqrt{x(x-a)(x-b)(x-c)}\right) \\
& =10.2(10-x)(x-2)=20\left(-x^{2}+12 x-20\right)
\end{aligned}
$$

$$
\begin{aligned}
& \frac{d y}{d x}=20(-2 x+12)=-40(x-6) \\
& \frac{d y}{d x}=0 \quad \Rightarrow x=6
\end{aligned}
$$

As $\frac{d^{2} y}{d x^{2}}$ is $-\mathrm{ve}, \mathrm{so} x=6$ gives the maximum area of the triangle.
The length of other unknown side $=12-6=6(\mathrm{~cm})$
Thus the lengths of the other two sides are 6 cm and 6 cm .
Example 4: An open box of rectangular base is to be made from 24 cm by 45 cm cardboard by cutting out square sheets of equal size from each corner and bending the sides. Find the dimensions of corner squares to obtain a box having largest possible volume.

Solution: Let $x$ (in cm ) be the length of a side of each square sheet to be cut off from each comer of the cardboard. Then the length and breadth of the resulting box (in cm ) will be $45-2 x$ and $24-2 x$ respectively. Obviously the height of the box (in cm ) will be $x$. Thus the volume $V$ of the box (in cubic cm ) will be given by

$$
\begin{aligned}
V & =x(24-2 x)(45-2 x)=2 x(12-x)(45-2 x) \\
& =2 x\left(540-69 x+2 x^{2}\right)
\end{aligned}
$$

and $\quad \frac{d V}{d x}=2\left[1 .\left(2 x^{2}-69 x+540\right)+x(4 x-69)\right]$

$$
\begin{aligned}
& =2\left(6 x^{2}-138 x+540\right) \\
= & 12\left(x^{2}-23 x+90\right)=12(x-5)(x-18) \\
& \frac{d V}{d x}=0 \quad \Rightarrow 12(x-5)(x-18)=0 \quad \Rightarrow x=5 \text { or } x=18 \\
& \Rightarrow x=5[\because \text { if } x=18, \text { then } 12-x=12-18=-6, \text { that is, }
\end{aligned}
$$

$V$ is negative which is not possible]
$\frac{d^{2} y}{d x^{2}}=12(2 x-23)$
$\frac{d^{2} V}{d x^{2}}$ is negative for $x=5$ because $12(2 \times 5-23)=12(-13)$
Thus V will be maximum if the length of a side of the corner square to be cut off is 5 cm .
Example 5: Find the point on the graph of the curve $y=4-x^{2}$ which is closest to the point $(3,4)$.

Solution: Let $l$ be distance between a point $(x, y)$ on the curve $y=4-x^{2}$ and the point $(3$, 4). Then $l=\sqrt{(x-3)^{2}+(y-4)^{2}}$

$$
\begin{aligned}
& =\sqrt{(x-3)^{2}+\left(4-x^{2}-4\right)^{2}} \quad\left(\because(x, y) \text { is on the curve } y=4-x^{2}\right) \\
& =\sqrt{(x-3)^{2}+x^{4}}
\end{aligned}
$$

Now we find $x$ for which $l$ is minimum.

$$
\begin{aligned}
\frac{d l}{d x} & =\frac{1}{2 \sqrt{(x-3)^{2}+x^{4}}}\left[\left(\begin{array}{lll}
2(x & 3 & 4 x^{2}
\end{array}\right)\right] \\
& =\frac{1}{2 l} 2\left(2 x^{2}+x-3\right)
\end{aligned}
$$

$$
\begin{aligned}
& =\frac{1}{l}\left(2 x^{2}+x-3\right) \\
& =\frac{1}{l}(x-1)\left(2 x^{2}+x-3\right) \\
& \frac{d l}{d x}=0 \Rightarrow \frac{1}{l}(x-1)\left(2 x^{2}+2 x+3\right)=0 \Rightarrow x-1=0 \text { or } 2 x^{2}+2 x+3=0 \\
& \Rightarrow x=1 \quad\left(\because 2 x^{2}+2 x+3=0\right) \\
& l \text { is positive for } 1-\varepsilon \text { and } 1+\varepsilon \text { where } \varepsilon \text { is very very small positive real number. } \\
& \text { Also } 2 x^{2}+2 x+3=2\left(x^{2}+x+\frac{1}{4}\right)+\frac{5}{2}=2\left(x+\frac{1}{2}\right)^{2}+\frac{5}{2} \text { is positive, for } x=1-\varepsilon \\
& \text { and } x=1+\varepsilon
\end{aligned}
$$

The sign of $\frac{d l}{d x}$ depends on the factor $x-1$.
$x-1$ is negative for $x=1-\varepsilon$ because $x-1=1-\varepsilon-1=-\varepsilon \quad \ldots . .(\mathrm{i})$
$x-1$ is positive for $x=1+\varepsilon$ because $x-1=1+\varepsilon-1=\varepsilon \quad \ldots .$. (ii)
From (i) and (ii), we conclude that $\frac{d l}{d x}$ changes sign from -ve to +ve at $x=1$.
Thus $l$ has a minimum value at $x=1$.
Putting $x=1$ in $y=4-x^{2}$, we get the $y$-coordinate of the required point which is $4-(1)^{2}=3$
Hence the required point on the curve is $(1,3)$.

## EXERCISE 2.10

1. Find two positive integers whose sum is 30 and their product will be maximum.
2. Divide 20 into two parts so that the sum of their squares will be minimum.
3. Find two positive integers whose sum is 12 and the product of one with the square of the other will be maximum.
4. The perimeter of a triangle is 16 centimetres. If one side is of length 6 cm , what are length of the other sides for maximum area of the triangle?
5. Find the dimensions of a rectangle of largest area having perimeter 120 centimetres.
6. Find the lengths of the sides of a variable rectangle having area $36 \mathrm{~cm}^{2}$ when its perimeter is minimum.
7. A box with a square base and open top is to have a volume of 4 cubic dm . Find the dimensions of the box which will require the least material.
8. Find the dimensions of a rectangular garden having perimeter 80 metres if its area is to be maximum.
9. An open tank of square base of side $x$ and vertical sides is to be constructed to contain a given quantity of water. Find the depth in terms of $x$ if the expense of lining the inside of the tank with lead will be least.
10. Find the dimensions of the rectangle of maximum area which fits inside the semi-circle of radius 8 cm as shown in the figure.
11. Find the point on the curve $y=x^{2}-1$ that is closest to the point $(3,-1)$.
12. Find the point on the curve $y=x^{2}+1$ that is closest to the point $(18,1)$.

# CHAPTER

## 3

## Integration

Animation 3.1: Integration
Source and credit: eLearn.Punjab

# 3.1 INTRODUCTION

When the derived function (or differential coefficient) of a function is known, then the aim to find the function itself can be achieved. The technique or method to find such a function whose derivative is given involves the inverse process of differentiation, called **anti-derivation** or **integration**. We use differentials of variables while applying method of substitution in integrating process. Before the further study of anti-derivation, we first discuss the differentials of variables.

### 3.1.1 Differentials of Variables

Let *f* be a differentiable function in the interval *a* < *x* < *b*, defined as *y* = *f*(*x*), then

$$
\delta y = f(x + \delta x) - f(x)
$$

and

$$
\lim_{d \to \infty} \frac{\delta y}{dx} = \lim_{d \to \infty} \frac{f(x + \delta x) - f(x)}{\delta x} \quad f'(x), \text{ that is}
$$

$$
\frac{dy}{dx} = f'(x)
$$

We know that before the limit is reached, $\frac{\delta y}{\delta x}$ differs from *f*'(x) by a very small real number $\varepsilon$.

Let

$$
\frac{\delta y}{\delta x} = f'(x) + \varepsilon \qquad \text{where } \varepsilon is very small
$$

or

$$
\delta y = f'(x)\delta x + \varepsilon \quad \delta x \qquad \text{(i)}
$$

The term $f'(x)\delta x$ being more important than the term $\varepsilon \delta x$, is called the differential of the dependent variable *y* and is denoted by *dy* (or *df*)

Thus *dy* = $f'(x)\delta x$ (ii)

As

$$
dx = (x)'\delta x = (1)\delta x, \text{ so}
$$

the differential of *x* is denoted by *dx* and is defined by the relation *dx* = $\delta x$.

The equation (ii) becomes

$$
dy = f'(x) \, dx \qquad \text{(iii)}
$$

**Note:** Instead of *dy*, we can write *df*, that is, *df* = *f*'(x) *dx* where *f*'(x) being coefficient of differential is called differential coefficient.

### 3.1.2 Distinguishing Between *dy* and $\delta y$

The tangent line is drawn to the graph of *y* = *f*(*x*) at *P*(*x*, *f*(*x*) and *MP* is the ordinate of *P*, that is, *MP* = *f*(*x*). (see Fig. 3.1)

Let $\delta x$ be small number, then the point *N* is located at *x* + $\delta x$ on the *x*-axis. Let the vertical line through *N* cut the tangent line at *T* and the graph of *f* at *Q*. Then the point *Q* is (*x* + $\delta x$, *f*(*x* + $\delta x*)), so

$$
d x = \delta x = PR
$$

and

$$
\delta y = RQ = RT + TQ
$$

$$
= \tan \varphi \delta x + TQ \qquad \left( \because \tan \varphi = \frac{RT}{PR} \right)
$$

where $\varphi$ is the angle which the tangent *PT* makes with the positive direction of the *x*-axis.

or

$$
\delta y = f'(x) dx + TQ \qquad \left( \therefore \tan \varphi \delta x = f'(x) \right)
$$

$$
\Rightarrow \quad \delta y = dy + TQ
$$

We see that $\delta y$ is the rise of *f* for a change $\delta x$ in *x* at *x* where as *dy* is the rise of the tangent line at *P* corresponding to the same change $\delta x$ in *x*.

The importance of the differential is obvious from the figure 3.1. As $\delta x$ approaches 0, the value of *dy* gets closer and closer to that of $\delta y$, so for small values of $\delta x$,

$$
dy = \delta y
$$

or

$$
dy = f'(x) dx \quad [\because dy = f'(x) dx] \qquad \text{(iv)}
$$

We know that

$$
\delta y = f(x + \delta x) - f(x) \qquad \text{ for } f(x + \delta x) = f(x) + \delta y
$$

But

$$
\delta y \approx dy, \text{ so}
$$

$$
f(x + \delta x) \approx f(x) + dy \qquad \text{(v)}
$$

$$
f(x + \delta x) \approx f(x) + f'(x) dx \qquad \text{(vi)}
$$

Example: Find $\delta y$ and $d y$ of the function defined as $f(x)=x^{2}, \quad$ when $x=2$ and $d x=0.01$

Solution: As $f(x)=x^{2}$, so $f^{\prime}(x)=2 x$

$$
\begin{aligned}
& \delta y=f(x+\delta x)-f(x)=(x+\delta x)^{2}-x^{2} \\
& =2 x \delta x+(\delta x)^{2}=2 x d x+(d x)^{2} \quad(\because \delta x=d x) \\
& \text { Thus } f(2+0.01)-f(2)=2(2)(0.01)+(0.01)^{2} \\
& =0.04+0.0001=0.0401 \text {, that is } \\
& \delta y=0.0401 \text { when } x=2 \text { and } \delta x=d x=0.01 \\
& \text { Also } d y=f^{\prime}(x) d x \\
& =2(2) \times(0.01)=0.04 \quad\left(\because f^{\prime}(x)=2 x, x=2 \text { and } d x=0.01\right) \\
& \text { Thus } \delta y-d y=0.0401-0.04=0.0001 \text {. }
\end{aligned}
$$

### 3.1.3 Finding $\frac{d y}{d x}$ by using differentials

We explain the process in the following example.
Example: Using differentials find $\frac{d y}{d x}$ when $\frac{y}{x}-\ln x=\ln c$
Solution: Finding differentials of both sides of the given equation, we get

$$
d\left[\frac{y}{x}-\ln x\right]=d[\ln c]=0
$$

using $d(f \pm g)=d f \pm d g$, we have

$$
d\left[\frac{y}{x}\right]-d(\ln x) \gg 0 \quad \frac{d}{d x}\left[y \frac{1}{x}\right] \quad \frac{1}{x} d x \quad 0
$$

Using $d(f g)=f d g+g d f$, we get

$$
\begin{aligned}
& y d\left(\frac{1}{x}\right)+\frac{1}{x} d y-\frac{1}{x} d x=0 \\
& y \times\left(\frac{1}{x^{2}} d x\right)+\frac{1}{x} d y-\frac{1}{x} d x=0 \Rightarrow \frac{1}{x} d y=\frac{1}{x} d x+\frac{y}{x^{2}} d x
\end{aligned}
$$

$$
\begin{aligned}
& \text { or } \quad \frac{1}{x} d y=\left(\frac{1}{x} \quad \frac{y}{x^{2}}\right) d x \quad\left(\frac{x+y}{x^{2}}\right) d x \quad \frac{1}{x}\left(\frac{x+y}{x}\right) d x \\
& \Rightarrow d y=\left(\frac{x+y}{x}\right) d x \\
& \text { Thus } \quad \frac{d y}{d x}=\frac{x+y}{x} \quad\left[\because d y=f^{\prime}(x) d x\right]
\end{aligned}
$$

### 3.1.4 Simple application of differentials

Use of differentials for approximation is explained in the following examples.
Example 1: Use differentials to approximate the value of $\sqrt{17}$.
Solution: Let $f(x)=\sqrt{x}$
Then $f(x+\delta x)=\sqrt{x+\delta x}$
As the nearest perfect square root to 17 is 16 , so we take $x=16$
and $\delta x=d x=1$
Then $y=f(16)=\sqrt{16}=4$
Using $f(x+\delta x) \approx f(x)+d y$

$$
\approx f(x)+f^{\prime}(x) d x \text {. we have }
$$

$$
\begin{aligned}
f(16+1) & \approx f(16)+\frac{1}{2 \sqrt{16}} \times(1) \quad\left(\because f^{\prime}(x)=\frac{1}{2 \sqrt{x}}\right) \\
& \approx 4+\frac{1}{2 \times 4}=4+\frac{1}{8}=4.125
\end{aligned}
$$

Hence $\sqrt{17} \approx 4.125$
Example 2: Use differentials to approximate the value of $\sqrt[3]{8.6}$
Solution: Let $f(x)=\sqrt[3]{x} \quad$ then

$$
y+\delta y=f(x+\delta x)=\sqrt[3]{x+\delta x}=\sqrt[3]{x+d x} \quad(\because \delta x=d x) \text { and } f^{\prime}(x) \frac{1}{3 x^{3}}
$$

As the nearest perfect cube root to 8.6 is 8 , so we take $x=8$ and $d x=0.6$, then

$$
\begin{aligned}
& f(8)=\sqrt[3]{8}=2 \quad \text { and } \quad f^{\prime}(8)=\frac{1}{3(8)^{2}} \quad \frac{1}{3 \times 4} \quad \frac{1}{12} \\
& \text { so } \quad d y=f^{\prime}(x) d x=\frac{1}{12} \times(0.6)=0.05 \\
& \text { Using } f(x+\delta x)=f(x)+d y \text {, we have } \\
& f(8+0.6)=f(8)+0.05 \\
& \quad \neq 2 \quad 0.05 \quad 2.05
\end{aligned}
$$

But using calculator, we find that $\sqrt[3]{8.6}$ is approximately equal to 2.0488 .

## Example 3: Using differentials, find the approximate value of $\sin 46^{\circ}$

Solution: Let $y=\sin x$, then

$$
y+\delta y=\sin (x+\delta x)=\sin (x+d x) \quad(\delta x=d x)
$$

We take $x=45^{\circ}=\frac{\pi}{4} \quad$ and $d x=1^{\circ} \quad=0.01745$

$$
\text { Hence } d y=\cos x d x \quad\left(-\frac{d}{d x}(\sin x)=\cos x\right)
$$

$$
\begin{aligned}
& \approx\left(\cos 45^{\circ}\right)(0.01745)=\frac{1}{\sqrt{2}}(0.01745) \\
& \approx 0.7071(0.01745) \\
& \approx 0.01234 \\
& \text { Using } f(x+\delta x) \approx f(x)+d y \text { we have } \\
& \sin \left(46^{\circ}\right) \approx \sin 45^{\circ}+d y \approx 0.7071+0.01234=0.71944 \\
& \approx 0.7194
\end{aligned}
$$

Using calculator, we find $\sin 46^{\circ}$ is approximately equal to 0.71934 .
Example 4: The side of a cube is measured to be 20 cm with a maximum error of 12 cm in its measurement. Find the maximum error in the calculated volume of the cube.

Solution: Let $x$ be the side and $V$ be the volume of the cube, then

$$
V=x^{3} \quad \text { and } \quad d V=\left(3 x^{2}\right) d x
$$

Taking $x=20(\mathrm{~cm})$ and $d x=0.12(\mathrm{~cm})$, we get

$$
d V=[3(20)^{2}](0.12)=1200 x(0.12)=144(\text { cubic } \mathrm{cm})
$$

The error 144 cubic cm in volume calculation of a cube is either positive or negative.

## EXERCISE 3.1

1. Find $\delta y$ and $d y$ in the following cases:
(i) $y=x^{2}-1$
when $x$ changes from 3 to 3.02
(ii) $y=x^{2}+2 x$
when $x$ changes from 2 to 1.8
(iii) $y=\sqrt{x}$
when $x$ changes from 4 to 4.41
2. Using differentials find $\frac{d y}{d x}$ and $\frac{d x}{d y}$ in the following equations
(i) $x y+x=4$
(ii) $x^{2}+2 y^{2}=16$
(iii) $x^{4}+y^{2}=x y^{2}$
(iv) $x y-\ln x=c$
3. Use differentials to approximate the values of
(i) $\sqrt[3]{17}$
(ii) $(31)^{1 / 5}$
(iii) $\cos 29^{\circ}$
(iv) $\sin 61^{\circ}$
4. Find the approximate increase in the volume of a cube if the length of its each edge changes from 5 to 5.02 .
5. Find the approximate increase in the area of a circular disc if its diameter is ?

### 3.2 INTEGRATION AS ANTI - DERIVATIVE (INVERSE OF DERIVATIVE)

In chapter 2, we have been finding the derived function (differential coefficient) of a given function. Now we consider the reverse (or inverse) process i.e. we find a function when its derivative is known. In other words we can say that if $\phi^{\prime}(x)=f(x)$, then $\phi(x)$ is called an anti-derivative or an integral of $f(x)$. For example, an anti-derivative of $f(x)=3 x^{2}$ is $\phi(x)=x^{3}$ because $\phi^{\prime}(x)=\frac{d}{d x}\left(x^{3}\right)=3 x^{2}=f(x)$.

The inverse process of differentiation i.e. the process of finding such a function whose derivative is given is called anti-differentiation or integration.

While finding the derivatives of the expressions such as $x^{2}+x, x^{2}+x+5, x^{2}+x-3$ etc., we see that the derivative of each of them is $2 x+1$, that is,
$\frac{d}{d x}\left(x^{2}+x\right)=\frac{d}{d x}\left(x^{2}+x+5\right)=\frac{d}{d x}\left(x^{2}+x-3\right)=2 x+1$
Now if $f(x)=2 x+1$
Then $\phi(x)=x^{2}+x$
is not only anti-derivative of (i). But all anti-derivatives of $f(x)=2 x+1$ are included in $x^{2}+x+c$ where $c$ is the arbitrary constant which can be found if further information is given. As $c$ is not definite, so $\phi(x)+c$ is called the indefinite integral of $f(x)$, that is,
$\int f(x) d x=\Phi(x)+c$
In (ii), $f(x)$ is called integrand and $c$ is named as the constant of integration.
The symbol $\int \ldots d x$ indicates that integrand is to be integrated w.r.t. $x$.
Note that $\frac{d}{d x}$ and $\int \ldots d x$ are inverse operations of each other.

### 3.2.1 Some Standard Formulae for Anti-Derivatives

We give below a list of standard formulae for anti-derivatives which can be obtained from the corresponding formulae for derivatives:

## General Form

In formulae 1-7 and 10-14, a $\neq 0$

1. $\int(a x+b)^{n} d x=\frac{(a x+b)^{n-1}}{a(n+1)}+c,(n \neq-1) \quad\left\{x^{n} d x=\frac{x^{n-1}}{n+1}+c(n \neq-1)\right.$
2. $\int \sin (a x+b) d x=-\frac{1}{a} \cos (a x+b)+c \quad \int \sin x d x=\cos x$
3. $\int \cos (a x+b) d x=\frac{1}{a} \sin (a x+b)+c \quad \int \cos x d x=\sin x+c$
4. $\int \sec ^{2}(a x+b) d x=\frac{1}{a} \tan (a x+b)+c \quad \int \sec ^{2} x d x=\tan x$
5. $\int \operatorname{cosec}^{2}(a x+b) d x=-\frac{1}{a} \cot (a x+b)+c \quad \int \operatorname{cosec}^{2} x d x=\cot x$
6. $\int \sec (a x+b) \tan (a x+b) d x=\frac{1}{a} \sec (a x+b)+c \quad \int \sec x \tan x d x \neq \sec x$
7. $\int \operatorname{cosec}(a x+b) \cot (a x+b) d x=-\frac{1}{a} \operatorname{cosec}(a x+b)+c \quad \int \operatorname{cosec} \cot x d x=\operatorname{cosec} x$
8. $\int e^{2 x+a} d x=\frac{1}{\lambda} x e^{2 x+a}+c(\lambda \neq 0) \quad \int e^{x} d x=e^{x}+c$
9. $\int a^{2 x+a} d x=\frac{1}{\lambda \ln a} a^{2 x+a}+c .(a) 0, a \neq 1, \lambda \neq 0) \quad \int a^{2} d x=\frac{1}{\ln a} a^{2}+c .(a) 0, a \neq 1)$
10. $\int \frac{1}{a x+b} d x=\int(a x+b)^{-1} d x \quad\left\{\frac{1}{\lambda} d x=\ln |x|+c, x \neq 0\right.$

$$
=\frac{1}{a} \ln |a x+b|+c,(a x+b \neq 0)
$$

11. $\int \tan (a x+b) d x=\frac{1}{a} \ln |\sec (a x+b)|+c \quad \int \tan x d x=\ln |\sec (x)|+c$

$$
\Rightarrow \frac{1}{a} \ln |\cos (\boldsymbol{a} x \quad \boldsymbol{b})| \quad c \quad=\ln |\cos x| \quad c
$$

12. $\int \cot (a x+b) d x=\frac{1}{a} \ln |\sin (a x+b)|+c \quad \int \cot x d x=\ln |\sin x|+c$
13. $\int \sec (a x+b) d x=\frac{1}{a} \ln |\sec (a x+b)+\tan (a x+b)|+c \quad \int \sec x d x=\ln |\sec x+\tan x|+c$
14. $\int \operatorname{cosec}(a x+b) d x=\frac{1}{a} \ln |\operatorname{cosec}(a x+b)-\cot (a x+b)|+c \quad \int \operatorname{cosec} x d x=\ln |\operatorname{cosec} x-\cot x|+c$

These formulae can be verified by showing that the derivative of the right hand side of each with respect to $x$ is equal to the corresponding integrand.

## Examples:

1. $\int x^{5} d x=\frac{x^{5-1}}{5+1}+c=\frac{x^{6}}{6}+c \quad\left(1-\frac{d}{d x}\left(\frac{1}{6} x^{6}\right)\right)=\frac{1}{6} d x\left(x^{6}\right)=\frac{1}{6} \cdot 6 x^{6-1}=x^{5}$
2. $\int \frac{1}{\sqrt{x^{3}}} d x=\int x^{-\frac{1}{2}} d x=\frac{x^{-\frac{1}{2}-1}}{-\frac{3}{2}+1} \quad\left[1-\frac{d}{d x}\left(\frac{-2}{\sqrt{x}}\right)=-2 \frac{d}{d x}(x)^{\frac{1}{2}}\right]$

$$
=\frac{x^{\frac{1}{2}}}{-\frac{1}{2}}+c=-\frac{2}{\sqrt{x}}+c \quad=-2 \cdot\left(-\frac{1}{2}\right) x^{\frac{1}{2}+}=x^{\frac{-1}{2}} \frac{1}{\sqrt{x^{2}}}
$$

3. $\int \frac{1}{(2 x+3)^{4}} d \dot{x}=(\varnothing x \quad 3)^{-4} d x \quad\left(\because \frac{d}{d x}\left(\frac{1}{6(2 x+3)^{2}}\right)\right)$
$=\frac{(2 x+3)^{-4+1}}{2(-4+1)}+c=\frac{(2 x+3)^{-3}}{-6}+c \quad=\frac{1}{6} \frac{d}{d x}\left((2 x \quad 3)^{-3}\right)$
$=\frac{1}{6(2 x+3)^{2}} \quad c \quad=-\frac{1}{6}(-3)(2 x+3)^{-3-1}(2)=\frac{1}{(2 x+3)^{4}}$
4. $\int \cos 2 x d x=\frac{\sin 2 x}{2}+c=\frac{1}{2} \sin 2 x+c \quad\left(\because \frac{d}{d x}\left(\frac{1}{2} \sin 2 x\right)=\frac{1}{2} \frac{d}{d x}(\sin 2 x)\right)$
$=\frac{1}{2}(\cos 2 x) \times 2=\cos 2 x$
5. $\int \sin 3 x d x=\frac{-\cos 3 x}{3}+c=\frac{1}{3} \cos 3 x+c \quad\left(\because \frac{d}{d x}\left(-\frac{1}{3} \cos 3 x\right)=\frac{1}{3} \frac{d}{d x}(\cos 3 x)\right)$
6. $\int \cos \sec ^{2} x d x=\operatorname{sec} x \quad c \quad\left(\because \frac{d}{d x}(-\cot x)=-\left(-\cos \sec ^{2} x\right)=\cos \sec ^{2} x\right)$
7. $\int \sec 5 x \tan 5 x d x=\frac{\sec 5 x}{5} \quad c \quad\left(\because \frac{d}{d x}\left(\frac{\sec 5 x}{5}\right)\right)=\frac{1}{5}(\operatorname{sen} 5 x \tan 5 x) \quad 5 \quad \sec 5 x \tan 5 x$
8. $\int e^{a x+b} d x=\frac{e^{a x+b}}{a}+c \quad\left(\because \frac{d}{d x}\left(\frac{e^{a x+b}}{a}\right)=\frac{1}{a}\left(e^{a x+b} \times a\right)=e^{a x+b}\right)$
9. $\int 3^{3 / 2} d x=\frac{3^{3 / 2}}{\lambda \ln 3}+c \quad\left(\because \frac{d}{d x}\left(\frac{3^{3 / 2}}{\lambda \ln 3}\right)=\frac{1}{\lambda \ln 3}\left(3^{3 / 2}(\ln 3) \lambda\right) \quad 3^{3 / 2}\right)$
10. $\int \frac{1}{a x+b} d \dot{x}=(\omega x \quad b)^{-1} d x \quad\left(\because \frac{d}{d x}\left(\frac{1}{a} \ln (a x+b)=\frac{1}{a} \frac{1}{a x+b} \cdot a=\frac{1}{a x+b}\right)\right)$
$=\frac{1}{a} \ln (a x+b)+c \cdot(a x+b>0)$
11. $\int \frac{1}{\sqrt{x^{2}+a^{2}}} d x=\ln \left(x+\sqrt{x^{2}+a^{2}}\right)+c \quad\left(\because \frac{d}{d x}\left(\ln (x+\sqrt{x^{2}+a^{2}})\right)=\frac{1}{x+\sqrt{x^{2}+a^{2}}}\left(1+\frac{1}{2 \sqrt{x^{2}+a^{2}}}+2 x\right)\right)$

$$
\frac{1}{x+\sqrt{x^{2}+a^{2}}}=\frac{\sqrt{x^{2}+a^{2}}+x}{\sqrt{x^{2}+a^{2}}}=\frac{1}{\sqrt{x^{2}+a^{2}}}
$$

### 3.2.2 Theorems on Anti-Derivatives

I. The integral of the product of a constant and a function is equal to the product of the constant and the integral of the function.
In symbols,

$$
\int \operatorname{of}(x) d x=a \mid f(x) d x \quad \text { where } a \text { is a constant. }
$$

II. The integral of the sum (or difference) of two functions is equal to the sum (or difference) of their integrals.
In symbols,

$$
\int\left[f_{1}(x) \pm f_{2}(x)\right] d x=\int f_{1}(x) d x \pm \int f_{2}(x) d x
$$

### 3.2.3 Anti-Derivatives of $[f(x)]^{\circ} f^{\prime}(x)$ and $[f(x)]^{-1} f^{\prime}(x)$

$$
\begin{aligned}
& \text { Prove that: (i) } \int[f(x)]^{\circ} f^{\prime}(x) d x=+\frac{[f(x)]^{n+1}}{n+1} \quad \text { c. } \quad(n \neq-1) \\
& \text { (ii) } \int[f(x)]^{-1} f^{\prime}(x) d x=\ln f(x)+c . \quad(f(x)>0)
\end{aligned}
$$

Proof:
(i) Since $\frac{d}{d x}\left([f(x)^{n+1}\right)=(n+1)[f(x)]^{\circ} f^{\prime}(x)$
$\therefore \quad$ by definition, $\int(n+1)[f(x)]^{\circ} f^{\prime}(x) d x=[f(x)]^{n+1}+c$,
$(n+1) \int[f(x)]^{\circ} f^{\prime}(x) d x=\frac{1}{2} f(x)]^{n+1} \quad c$, (by theorem I)
or $\int[f(x)]^{\circ} f^{\prime}(x) d x=\frac{[f(x)]^{n+1}}{n+1}+c \quad$ where $\quad c \quad \frac{c}{n+1}(n \quad 1)$

(ii) Since $\frac{d}{d x}\{\ln f(x)\}=\frac{1}{f(x)} \cdot f^{\prime}(x)$

By definition, we have
$\int \frac{1}{f(x)} \cdot f^{\prime}(x) d x=\ln f(x) \quad$ ( $\left.\neq(x) 0\right)$
or $\int[f(x)]^{-1} f^{\prime}(x) d x=\ln f(x)+c$.
Thus we can prove that
(i) $\int x^{n} d x=\frac{x^{n+1}}{n+1}+c, \quad(n \neq-1)$
(ii) $\int(a x+b)^{n} d x=\frac{(a x+b)^{n+1}}{a(n+1)}+c, \quad(a \neq 0, n \neq-1)$
(iii) $\int \frac{1}{x} d x=\ln |x|+c$
(iv) $\int \frac{1}{a x+b} d x=\frac{1}{c_{1}} \ln |a x+b|+c, \quad(a \neq 0)$

Examples: Evaluate
(i) $\int(x+1)(x-3) d x$
(ii) $\int x \sqrt{x^{2}-1} d x$
(iii) $\int \frac{x}{x+2} d x, \quad(x>-2)$
(iv) $\int \frac{1}{\sqrt{x}(\sqrt{x+1})} d x, \quad(x>0)$
(v) $\int \frac{d x}{\sqrt{x+1}-\sqrt{x}}, \quad(x>0)$
(vi) $\int \frac{\sin x+\cos ^{2} x}{\cos ^{2} x \sin x} d x$
(vii) $\int \frac{3-\cos 2 x}{1+\cos 2 x} d x, \quad(\cos 2 x \neq-1)$

# (i) $\int(x+1)(x-3) d x=\int\left(x^{2}-2 x-3\right) d x$

$$
\begin{aligned}
& =\int x^{2} d x-2 \int x d x-3 \int 1 d x \quad \text { (By theorems I and II) } \\
& =\frac{x^{3}}{3}-2 \cdot \frac{x^{2}}{2}-3 \cdot x+c \quad \cup \int x^{n} d x=\frac{x^{n+1}}{n+1}+c_{1} \text { and }
\end{aligned}
$$

$$
=\frac{1}{3} x^{2}-x^{2}-3 x+c \quad \int 1 d x=x^{0}=d x \quad \frac{x^{n+1}}{1} \quad c_{2}
$$

(ii) $\int x \sqrt{x^{2}-1} d x=\int\left(x^{2}-1\right)^{\frac{1}{2}} x d x$

$$
\begin{aligned}
& =\int[f(x)]^{-\frac{1}{2}} f^{\prime}(x) d x \quad \text { (If } f(x)=x^{2}-1 \\
& =\frac{1}{2} \int[f(x)]^{\frac{1}{2}} f^{\prime}(x) \quad \text { then } f^{\prime}(x)+2 x \Rightarrow x \neq \frac{1}{2} f^{\prime}(x)) \\
& =\frac{1}{2} \frac{[f(x)]^{\frac{1}{2}}}{2}+c=\frac{1}{3}\left(x^{2}+1\right)^{\frac{1}{2}}+c
\end{aligned}
$$

(iii) $\int \frac{x}{x+2} d x=\int \frac{x+2-2}{x+2} d x, \quad(x>-2)$

$$
=\int\left(1-\frac{2}{x+2}\right) d x=\int d x-2 \int(x+2)^{-1} \cdot 1 d x=x-2 \ln (x+2)+c
$$

(iv) $\int \frac{1}{\sqrt{x}(\sqrt{x}+1)} d x=\frac{1}{\sqrt{x}+1}-\frac{1}{\sqrt{x}} d x \quad(x \quad 0)$

$$
\begin{aligned}
& =\int[f(x)]^{-1} \cdot 2 f^{\prime}(x) d x \quad \cup f^{\prime}(x) \quad \frac{1}{2 \sqrt{x}} \quad \text { if } f(x) \quad \sqrt{x} \quad 1 \\
& =-2 \int[f(x)]^{-1} f^{\prime}(x) d x \quad \text { or } \frac{1}{\sqrt{x}} \quad 2 f^{\prime}(x) \\
& =2 \ln f(x)+c=2 \ln (\sqrt{x}+1)+c
\end{aligned}
$$

(v) $\int \frac{d x}{\sqrt{x+1}-\sqrt{x}}, \quad(x>0)$

Rationalizing the denominator, we have

$$
\int \frac{d x}{\sqrt{x+1}-\sqrt{x}}=\int \frac{\sqrt{x+1}+\sqrt{x}}{(\sqrt{x+1}-\sqrt{x})(\sqrt{x+1}+\sqrt{x})} d x
$$

$$
\begin{aligned}
& =\int \frac{\sqrt{x+1}+\sqrt{x}}{x+1-x} d x=\int\left[(\# \quad 1)^{\frac{1}{2}} \quad x^{\frac{1}{2}}\right] d x \\
& =\int(x \quad 1)^{\frac{1}{2}} d x \quad \int x^{\frac{1}{2}} d x \\
& =\frac{(x+1)^{\frac{1}{2}}}{2}+\frac{x^{\frac{1}{2}}}{2}+c=\frac{2}{3}(x+1)^{\frac{1}{2}}+\frac{2}{3} x^{\frac{1}{2}}+c
\end{aligned}
$$

(vi) $\int \frac{\sin x+\cos ^{2} x}{\cos ^{2} x \sin x} d x$

Solution: $\int \frac{\sin x+\cos ^{2} x}{\cos ^{2} x \sin x} d x=+\int\left(\frac{\sin x}{\cos ^{2} x \sin x} \quad \frac{\cos ^{2} x}{\cos ^{2} x \sin x}\right) d x$

$$
\begin{aligned}
& =\int\left(\frac{1}{\cos ^{2} x}+\frac{\cos x}{\sin x}\right) d x \\
& =\int \sec ^{2} x d x+\int \cot x d x \\
& =\tan x \quad \ln |\sin | \quad c
\end{aligned}
$$

(vii) $\int \frac{3-\cos 2 x}{1+\cos 2 x} d x, \quad(\cos 2 x \neq-1)$

Solution: $\int \frac{3-\cos 2 x}{1+\cos 2 x}=\int \frac{4-\left(1+\cos 2 x\right)}{1+\cos 2 x} d x \quad \int\left(\frac{4}{1+\cos 2 x} \quad 1\right) d x$

$$
\begin{aligned}
& =\int \frac{4}{2 \cos ^{2} x} d x-\int 1 d x=\int 2 \sec ^{2} x d x-\int 1 d x \\
& =2 \tan x-x+c
\end{aligned}
$$

## EXERCISE 3.2

## 1. Evaluate the following indefinite integrals

(i) $\int\left(3 x^{2}-2 x+1\right) d x$
(ii) $\int\left(\sqrt{x}+\frac{1}{\sqrt{x}}\right) d x, \quad(x>0)$
(iii) $\int x(\sqrt{x}+1) d x, \quad(x>0)$
(iv) $\int(2 x+3)^{\frac{1}{2}} d x$
(v) $\int(\sqrt{x}+1)^{3} d x, \quad(x>0)$
(vi) $\int\left(\sqrt{x}-\frac{1}{\sqrt{x}}\right)^{3} \mathrm{dx}, \quad(x>0)$
(vii) $\int \frac{3 x+2}{\sqrt{x}} d x, \quad(x>0)$
(viii) $\int \frac{\sqrt{y}(y+1)}{y} d y,(y>0)$
(ix) $\int \frac{(\sqrt{\theta}-1)^{3}}{\sqrt{\theta}} d \theta,(\theta>0)$
(x) $\int \frac{(1-\sqrt{x})^{3}}{\sqrt{x}} d x, \quad(x>0)$
(xi) $\int \frac{e^{2 x}+e^{x}}{e^{x}} d x$

## 2. Evaluate

(i) $\int \frac{d x}{\sqrt{x+a}+\sqrt{x+b}}\left(\frac{x+a>0}{x+b>0}\right)$
(ii) $\int \frac{1-x^{2}}{1+x^{2}} d x$
(iii) $\int \frac{d x}{\sqrt{x+a}+\sqrt{x}},(x>0, a>0)$
(iv) $\int(a-2 x)^{\frac{1}{2}} d x$
(v) $\int \frac{\left(1+e^{x}\right)^{3}}{e^{x}} d x$
(vi) $\int \sin (a+b) x d x$
(vii) $\int \sqrt{1-\cos 2 x} d x,(1-\cos 2 x>0)$
(viii) $\int(\ln x) \times \frac{1}{x} d x,(x>0)$
(ix) $\int \sin ^{2} x d x$
(x) $\int \frac{1}{1+\cos x} d x,\left(-\frac{\pi}{2}<x<\frac{\pi}{2}\right)$
(xi) $\int \frac{a x+b}{a x^{2}+2 b x+c} d x$
(xii) $\int \frac{\cos 2 x-1}{1+\cos 2 x} d x,(1+\cos 2 x \neq 0)$
(xiv) $\int \tan ^{2} x d x$

### 3.3 INTEGRATION BY METHOD OF SUBSTITUTION

Sometimes it is possible to convert an integral into a standard form or to an easy integral by a suitable change of a variable. Now we evaluate $\int f(x) d x$ by the method of substitution. Let $x$ be a function of a variable $t$, that is,
if

$$
\begin{array}{lll}
x=\phi(t), & \text { then } & d x=\phi^{\prime}(t) d t \\
x=\phi(t) & \text { and } & d x=\phi^{\prime}(t) d t \text {, we have } \\
& \int f(x) d x=\int f(\phi(t) \phi^{\prime}(t)) d t
\end{array}
$$

Now we explain the procedure with the help of some examples.
Example 1: $\quad$ Evaluate $\int \frac{a d t}{2 \sqrt{a t+b}} \quad(a t+b>0)$
Solution: $\quad$ Let $a t+b=u$. Then

$$
a d t=d u
$$

Thus $\int \frac{a d t}{2 \sqrt{a t+b}}=\int \frac{d u}{2 \sqrt{u}}=\frac{1}{2} \int u^{\frac{1}{2}} d u$

$$
=\frac{1}{2}\left(\frac{u^{-\frac{1}{2}+1}}{-\frac{1}{2}+1}\right)+c=\frac{1}{2}\left(\frac{u^{\frac{1}{2}}}{1}\right)+c=u^{\frac{1}{2}}+c=\sqrt{a t+b}+c
$$

Example 2: $\quad$ Evaluate $\int \frac{x}{\sqrt{4+x^{2}}} d x$.
Solution: Put $4+x^{2}=t$

$$
\begin{aligned}
& \Rightarrow 2 x d x=d t \text { or } x d x=\frac{1}{2} d t \text {, therefore } \\
& \int \frac{x}{\sqrt{4+x^{2}}} d x=\int \frac{1}{\sqrt{t}}\left(\frac{1}{2}\right) d t \quad \frac{1}{2} \int t^{\frac{-1}{2}} d t \quad+\frac{1}{2} \frac{t^{1 / 2}}{1 / 2} \quad c \\
& =\sqrt{t}+c=\sqrt{4+x^{2}}+c
\end{aligned}
$$

Example 3: $\quad$ Evaluate $\int x \sqrt{x-a} d x, \quad(x>a)$
Solution: $\quad$ Let $x-a=t \Rightarrow x=a+t$

$$
\Rightarrow d x=d t
$$

Thus $\int x \sqrt{x-a} d x=\int(a+t) \sqrt{t} d t$

$$
\begin{aligned}
& =\int\left(a t^{\frac{1}{2}}+t^{\frac{1}{2}}\right) d t=a \int t^{\frac{1}{2}} d t+\int t^{\frac{1}{2}} d t \\
& =a \frac{t^{\frac{1}{2}}}{3}+\frac{t^{\frac{1}{2}}}{2}+c=\frac{2 a}{3} t^{\frac{1}{3}}+\frac{2}{5} t^{\frac{1}{3}}+c \\
& =2 t^{\frac{1}{3}}\left(\frac{a}{3}+\frac{1}{3} t\right)+c=2(x-a)^{\frac{1}{3}}\left(\frac{a}{3}+\frac{1}{5}(x-a)\right)+c \\
& =2(x-a)^{\frac{1}{3}}\left(\frac{5 a+3(x-a)}{15}\right) \quad \propto \quad \frac{2}{15}(x-a)^{\frac{1}{3}}(5 a \quad 3 x \quad 3 a) \quad c \\
& =\frac{2}{15}(x-a)^{\frac{1}{3}}(2 a+3 x)+c
\end{aligned}
$$

Example 4: $\quad$ Evaluate $\int \frac{\cot \sqrt{x}}{x} d x . \quad(x>0)$.
Solution: $\quad$ Put $\sqrt{x}=z$,
then $d(\sqrt{x})=\infty d z \quad \frac{1}{2 \sqrt{x}} d x \quad d z$
or $\quad \frac{1}{\sqrt{x}} d x=2 d z$
thus $\int \frac{\cot \sqrt{x}}{\sqrt{x}} d x=\int \cot \sqrt{x} \frac{1}{\sqrt{x}} d x \quad \int \cot z .(2 d z)$

$$
\begin{aligned}
& =2 \int \cot z d z \quad 2 \int \frac{\cos z}{\sin z} d z \quad 2 \int(\sin z)^{-1} \cos z d z \\
& =2 \ln |\sin z|+c, \quad \overline{(z>0} \text { as } x>0) \\
& =2 \ln |\sin \sqrt{x}| \quad c
\end{aligned}
$$

Example 5: Evaluate (i) $\int \cos \varepsilon x d x \quad$ (ii) $\int \sec x d x$
Solution: $\int \cos \varepsilon x d x=\int \frac{\cos \varepsilon x(\cos \varepsilon x-\cot x)}{\cos \varepsilon x-\cot x} d x$
Put $\cos \varepsilon x \cot x=t$, then $\left(\cos \varepsilon x \cot x \quad \cos \varepsilon^{2} x\right) \cdot d x \quad d t$
or $\cos \varepsilon x(\cos \varepsilon x-\cot x) d x=d t$
so $\int \frac{\cos \varepsilon x(\cos \varepsilon x-\cot x)}{(\cos \varepsilon x-\cot x)} d x=\int \frac{1}{t} d t=\ln |t|+c$
Thus $\cos \varepsilon x d x=\ln \left|\cos \varepsilon x-\cot x\right|+c \quad[\because t=\cos \varepsilon x-\cot x]$
(ii) $\int \sec x d x=\int \frac{\sec x(\sec x+\tan x)}{(\sec x+\tan x)} d x$

Put $\sec x+\tan x=t$, then $\left(\sec x \tan x+\sec ^{2} x\right) d x=d t$
or $\sec x(\sec x+\tan x) d x=d t$
so $\int \frac{\sec x(\sec x-\tan x)}{(\sec x-\tan x)} d x=\int \frac{1}{t} d t=\ln |t|+c$
Thus $\int \sec x d x=\ln |\sec x+\tan x|+c \quad(\because t=\sec x+\tan x)$
Example 6: Evaluate $\int \cos ^{3} x \sqrt{\sin x} d x .(\sin x>0)$.
Solution: $\quad$ Put $\sqrt{\sin x}=t$, then $d t=\left[\frac{1}{2 \sqrt{\sin x}} \cdot \cos x\right] d x$
or $2 t d t==\cos x d x \quad[\because \sqrt{\sin x} \quad t]$
Putting $\sqrt{\sin x}==t$ and $\cos x d x \quad 2 t d t$ in the integral, we have,
$\int \cos ^{2} x \sqrt{\sin x} \cos x d x=\int\left(1-t^{4}\right) \cdot t=2 t d t, \quad\left(\because \cos ^{2} x=1 \approx \sin ^{2} x \quad 1 \quad t^{4}\right)$

$$
=2 \int\left(t^{2}-t^{4}\right) d t=2 \int t^{2} d t-2 \int t^{6} d t
$$

$$
=2 \cdot \frac{t^{3}}{3}-2 \frac{t^{3}}{7}+c
$$

$$
=\frac{2}{3}(\sin x)^{\frac{3}{2}}-\frac{2}{3}(\sin x)^{\frac{3}{2}}+c=\frac{2}{3} \sin ^{\frac{3}{2}} x-\frac{2}{7} \sin ^{\frac{3}{2}} x+c
$$

Version: 1.1

Example 7: Evaluate $\int \sqrt{1+\sin x} d x .\left(-\frac{\pi}{2}<x<\frac{\pi}{2}\right)$
Solution: $\int \sqrt{1+\sin x} d x=\int \sqrt{1} \sin x \frac{\sqrt{1-\sin x}}{\sqrt{1-\sin x}} d x=\int \frac{\sqrt{1-\sin ^{2} x}}{\sqrt{1-\sin x}} d x$

$$
=\int \frac{\cos x}{\sqrt{1-\sin x}} d x
$$

Put $\sin x=t$, then $\cos x d x=d t$, therefore

$$
\begin{aligned}
\int \sqrt{1+\sin x} d x & =\int \frac{1}{\sqrt{1-\sin x}} \cdot \cos x d x=\int \frac{d t}{\sqrt{1-t}}=\int(1-t)^{\frac{1}{2}} d t \\
& =\frac{(1-t)^{\frac{1}{2}} \cdot \cdot}{\left(-\frac{1}{2}+1\right)(-1)+c}=-2 \sqrt{1-t}+c \\
& =\frac{2 \sqrt{1} \quad \sin x}{2 \sqrt{1}}
\end{aligned}
$$

Example 8: Find $\int \frac{d x}{x(\ln 2 x)}, \quad(x>0)$
Solution: Put $\ln 2 x=t$, then

$$
\begin{aligned}
& \frac{1}{2 x} \cdot 2 d x=d t \quad \text { or } \quad \frac{1}{x} d x=d t \\
& \text { Thus } \int \frac{1}{(\ln 2 x)^{4}} \cdot \frac{1}{x} d x=\int \frac{1}{t^{2}} \cdot d t=\int t^{-1} d t=\frac{t^{-2}}{-2}+c \\
& \quad=-\frac{1}{2 t^{2}}+c=-\frac{1}{2(\ln 2 x)^{2}}+c
\end{aligned}
$$

Example 9: Find $\int a^{a^{2}} x d x . \quad(a>0, a \neq 1)$
Solution: Put $x^{2}=t$, then $x d x=\frac{1}{2} d t$
Thus $\int a^{a^{2}} x d x=\int a^{2} \times \frac{1}{2} d t$

$$
=\frac{1}{2} \int a^{c} d t=\frac{1}{2} \frac{a^{t}}{l n a}+c=\frac{a^{x^{2}}}{2 l n a}+c
$$

Example 10: Evaluate
(i) $\int \frac{1}{\sqrt{a^{2}-x^{2}}} d x, \quad(-a<x<a)$
(ii) $\int \frac{1}{x \sqrt{x^{2}-a^{2}}} d x,(x>a$ or $x<-a)$

## where $a$ is positive.

Solution: (i) Let $\quad x=a \operatorname{Sin} \theta, \quad$ that is,

$$
x=a \operatorname{Sin} \theta \quad \text { for }-\frac{\pi}{2}<\theta<\frac{\pi}{2}, \quad \text { then } d x=a \cos \theta d \theta
$$

Thus $\int \frac{d x}{\sqrt{a^{2}-x^{2}}}=\int \frac{a \cos \theta d \theta}{\sqrt{a^{2}-a^{2}} \sin ^{2} \theta}$

$$
\begin{aligned}
& =\int \frac{a \cos \theta d \theta}{a \sqrt{1-\sin ^{2} \theta}} \int \frac{a \cos \theta d \theta}{a \cos \theta} \\
& =\int 1 d \theta=\theta+c \\
& =\operatorname{Sin}^{-1}\left(\frac{x}{a}\right) \quad c \quad\left(\sqrt{-\frac{x}{a}} \quad \operatorname{Sin} \theta\right)
\end{aligned}
$$

(ii) Put $x=a \operatorname{Sec} \theta$ i.e., $x=a \sec \theta \quad$ for $\theta<\theta<\frac{\pi}{2}$ or $\frac{\pi}{2}<\theta<\pi$. Then $d x=a \sec \theta \tan \theta d \theta$

$$
\begin{aligned}
& \text { Thus } \int \frac{d x}{x \sqrt{x^{2}-a^{2}}}=\int \frac{a \sec \theta \tan \theta d \theta}{a \sec \theta \sqrt{a^{2} \sec ^{2} \theta-a^{2}}} \\
& =\int \frac{a \sec \theta \tan \theta d \theta}{a \sec \theta a \tan \theta} \quad\left(\sqrt{\sqrt{a^{2}\left(\sec ^{2} \theta\right.}{ }^{1}}\right) \\
& =\frac{1}{a} \int 1 d \theta=\frac{1}{a} \quad \theta+c \quad=\sqrt{a^{2} \tan ^{2}}=a \tan \theta) \\
& =\frac{1}{a} \operatorname{Sec}^{-1} \frac{x}{a} \quad c . \quad\left(\sqrt{\operatorname{Sec} \theta} \quad \frac{x}{a}\right)
\end{aligned}
$$

version: 1.1

### 3.4 SOME USEFUL SUBSTITUTIONS

We list below suitable substitutions for certain expressions to be integrated.

## Expression Involving

## Suitable Substitution

(i) $\sqrt{a^{2}-x^{2}}$
$x=a \sin \theta$
(ii) $\sqrt{x^{2}-a^{2}}$
$x=a \sec \theta$
(iii) $\sqrt{a^{2}+x^{2}}$
$x=a \tan \theta$
(iv) $\sqrt{x+a}($ or $\sqrt{x-a})$
$\sqrt{x+a}=t($ or $\sqrt{x-a}=t)$
(v) $\sqrt{2 a x-x^{2}}$
$x-a=a \sin \theta$
(vi) $\sqrt{2 a x+x^{2}}$
$x+a=a \sec \theta$

Example 1. Evaluate $\int \frac{1}{\sqrt{a^{2}+x^{2}}} d x \quad(a>\theta)$

Solution: $\quad$ Let $x=a \tan \theta$ for $-\frac{\pi}{2}<\theta<\frac{\pi}{2}$. Then

$$
d x=a \sec ^{2} \theta d \theta
$$

Thus

$$
\begin{aligned}
\int \frac{1}{\sqrt{a^{2}+x^{2}}} d x & =\int \frac{1}{\sqrt{a^{2}+a^{2}} \tan ^{2} \theta} \times a \sec ^{2} \theta d \theta=\int \frac{a \sec ^{2} \theta d \theta}{a \sqrt{1+\tan ^{2} \theta}} \\
& =\int \frac{a \sec ^{2} \theta d \theta}{a \sec \theta} \int \sec \theta d \theta \\
& =\int \frac{\sec \theta(\sec \theta+\tan \theta)}{\sec \theta+\tan \theta} d \theta \quad \ln (\sec -\theta \quad \tan \theta) \quad c_{1} \\
& =\ln \left(\frac{\sqrt{a^{2}+x^{2}}}{a} \frac{x}{a}\right) \quad v_{1}\left(\sqrt{\sec ^{2} \theta} \quad \llbracket \operatorname{man}^{2} \theta \llbracket \frac{x^{2}}{a^{2}} \quad \frac{a^{2}+x^{2}}{a^{2}}\right. \text { i.e., } \\
& =\ln \left(\frac{\sqrt{a^{2}+x^{2}}+x}{a}\right) \quad c_{1} \quad \sec \theta \quad \frac{\sqrt{a^{2}+x^{2}}}{a} \text { as } \sec \theta \text { is } \\
& =\ln \left(x+\sqrt{a^{2}+x^{2}}\right)-\ln a+c_{1} \quad \text { positive-for }<\frac{\pi}{2}<\theta \quad \frac{\pi}{2}
\end{aligned}
$$

$$
=\ln \left(x+\sqrt{a^{2}+x^{2}}\right)+c \quad \text { where } c=c_{1}-\ln a
$$

Note: $x+\sqrt{a^{2}+x^{2}}$ is always positive for real values of $a$.
Example 2. Evaluate $\int \frac{d x}{\sqrt{2 x+x^{2}}}, \quad(x>0)$
Solution: $\quad \int \frac{d x}{\sqrt{2 x+x^{2}}}=\int \frac{d x}{\sqrt{(x+1)^{2}-1}}$
Let $\quad x+1=\sec \theta$. Then $\quad\left[0<\theta<\frac{\pi}{2}\right]$

$$
d x=\sec \theta \tan \theta d \theta
$$

Thus $\int \frac{d x}{\sqrt{(x+1)^{2}-1}}=\int \frac{\sec \theta \tan d \theta}{\sqrt{\sec ^{2} \theta-1}}=\int \frac{\sec \theta \tan d \theta}{\tan \theta}=\int \sec \theta d \theta$

$$
=\operatorname{ln}(\sec \theta+\tan \theta)+c=\ln \left(x+1+\sqrt{2 x \quad x^{2}}\right)+c_{1}
$$

## EXERCISE 3.3

## Evaluate the following integrals:

1. $\int \frac{-2 x}{\sqrt{4-x^{2}}} d x$
2. $\int \frac{d x}{x^{2}+4 x+13}$
3. $\int \frac{x^{2}}{4+x^{2}} d x$
4. $\int \frac{1}{x \ln x} d x$
5. $\int \frac{e^{x}}{e^{x}+3} d x$
6. $\int \frac{x+b}{(x+2 b x+c)^{\frac{1}{2}}} d x$
7. $\int \frac{\sec ^{2} x}{\sqrt{\tan x}} d x$
8. (a) Show that $\int \frac{d x}{x^{2}-a^{2}}=\ln \left(x+\sqrt{x^{2}-a^{2}}\right)+c$
(b) show that $\int \sqrt{a^{2}-x^{2}} d x=\frac{a}{-} \operatorname{Sin}^{-\frac{x}{a}}+\frac{x}{a} \sqrt{a^{2}-x^{2}}+c$

## Evaluate the following integrals:

9. $\int \frac{d x}{\left(1+x^{2}\right)^{\frac{1}{2}}}$
10. $\int \frac{1}{\left(1+x^{2}\right) \operatorname{Tan}^{-1} x} d x$
11. $\int \sqrt{\frac{1+x}{1-x}} d x$
12. $\int \frac{\sin \theta}{1+\cos ^{2} \theta} d \theta$
13. $\int \frac{a x}{\sqrt{a^{2}-x^{2}}}$
14. $\int \frac{d x}{\sqrt{7-6 x-x^{2}}}$
15. $\int \frac{\cos x}{\sin x \ln \sin x} d x$
16. $\int \cos x\left(\frac{\ln \sin x}{\sin x}\right) d x$
17. $\int \frac{x d x}{4+2 x+x^{2}}$
18. $\int \frac{x}{x^{2}+2 x^{2}+5} d x$
19. $\int\left[\cos \left(\sqrt{x}-\frac{x}{2}\right)\right] \times\left(\frac{1}{\sqrt{x}}-1\right) d x$
20. $\int \frac{x+2}{\sqrt{x}+3} d x$
21. $\int \frac{\sqrt{2}}{\sin x+\cos x} d x$
22. $\int \frac{d x}{\frac{1}{2} \sin x+\frac{\sqrt{3}}{2} \cos x}$

### 3.5 INTEGRATION BY PARTS

We know that for any two functions $f$ and $g$,

$$
\begin{aligned}
& \frac{d}{d x}[f(x) g(x)]=\not f(x) g(x) \quad f(x) g^{\prime}(x) \\
& \text { or } \quad f(x) g^{\prime}(x) \quad=\frac{d}{d x}[f(x) g(x)] \quad f^{\prime}(x) g(x)
\end{aligned}
$$

Integrating both the sides with respect to $x$, we get,

$$
\begin{aligned}
\int f(x) g^{\prime}(x) d x & =\int\left[\frac{d}{d x}(f(x) g(x)) \quad f^{\prime}(x) g(x)\right] d x \\
& =\int\left(\frac{d}{d x}[f(x) g(x)]\right) d x \quad \int f^{\prime}(x) g(x) d x
\end{aligned}
$$

$$
=f(x) g(x)+c-\int f^{\prime}(x) g(x) d x \quad \text { (By Definition) }
$$

i.e., $\int f(x) g^{\prime}(x)=f(x) g(x) \quad \int g(x) f^{\prime}(x) d x \quad c \quad$ (i)
or $\int f^{\prime}(x) g^{\prime}(x) d x=-f(x) g(x) \quad \int g(x) f^{\prime}(x) d x \quad$ (i)

A constant of integration is written, when $\int g(x) f^{\prime}(x) d x$ is evaluated. The equation (i) or (i)' is known as the formula for integration by parts.

$$
\begin{aligned}
& \text { If we put } u=f(x) \quad \text { and } \quad d v=g^{+}(x) d x \\
& \text { then } \quad d u=f^{\prime}(x) d x \quad \text { and } \quad v=g(x) .
\end{aligned}
$$

The equation (i) and (i)' can be written as

$$
\begin{aligned}
& \int u d v=w v \int v d u \quad c \quad \text { (ii) } \\
& \int u d v=u v-\int v d u \quad \text { (iii) }
\end{aligned}
$$

Example 1. Find $\int x \cos x d x$.
Solution: If $f(x)=x$ and $g^{+}(x)=\cos x$,
then $f^{\prime}(x)=1 \quad$ and $\quad g(x)=\sin x$
Thus $\int x \cos x d x=x \sin x-\int(\sin x)(1) d x$

$$
\begin{aligned}
& =x \sin x-(-\cos x)+c \\
& =-x \sin x+\cos x \quad c
\end{aligned}
$$

Example 2. Find $\int x e^{x} d x$
Solution: Let $u=x$ and $d v=e^{x} d x$,
then $d u=1 . d x$ and $v=e^{x}$
Applying the formula for integration by parts, we have

$$
\int x e^{x} d x=x e^{x} \int e^{x} \times 1 d x=x e^{x} \quad e^{x}+c
$$

## Example 3. Evaluate $\int x \tan ^{2} x d x$

Solution: $\int x \tan ^{2} x d x=\int x\left(\sec ^{2} x-1\right) d x \quad\left(\because 1+\tan ^{2} x=\sec ^{2} x\right)$

$$
=-\int x \sec ^{2} x d x \quad \int x d x
$$

Integrating the fist integral by parts on the right side of (I), we get

$$
\begin{aligned}
\int x \tan ^{2} x d x= & {\left[x \tan x-\int \tan x \cdot 1 d x\right]-\left(\frac{x^{2}}{2}+c_{1}\right) } \\
= & x \tan x-d x+\int \frac{1}{\cos x} \quad(\quad \sin x) d x=\left(\frac{x^{2}}{2}-c\right)-x \tan x+\ln |\cos x| \quad c_{2} \quad \frac{x^{2}}{2} \quad c_{1} \\
= & x \tan x+\ln |\cos x|-\frac{x^{2}}{2}+c, \quad \text { where } c=c_{2}-c_{1}
\end{aligned}
$$

Example 4. Evaluate $\int x^{6} \ln x d x$
Solution: $\int x^{6} \ln x d x=\int(\ln x) x^{6} d x$

$$
\begin{aligned}
& =(\ln x) \frac{x^{6}}{6}-\int \frac{x^{6}}{6} \frac{1}{x} d x=\frac{x^{6}}{6} \ln x-\frac{1}{6} \int x^{6} d x \\
& =\frac{x^{6}}{6} \ln x-\frac{1}{6}\left[\frac{x^{6}}{6}+c_{1}\right] \\
& =\frac{x^{6}}{6} \ln x \quad \frac{x^{6}}{36}+c \quad \text { where } c=\frac{c_{1}}{6}
\end{aligned}
$$

Example 5. Evaluate $\int \ln \left(x+\sqrt{x^{2}+1}\right) d x$

Solution: $\quad$ Let $f(x)=\ln \left(x+\sqrt{x^{2}+1}\right)$ and $g^{\prime}(x)=1$. Then

$$
\begin{aligned}
f^{\prime}(x) & =\frac{1}{x+\sqrt{x^{2}+1}}\left\{1 \quad \frac{1}{2}\left(x^{2} \quad 1\right)^{\frac{1}{2}-1}, 2 x\right) \\
& =-\frac{1}{x+\sqrt{x^{2}+1}} \cdot\left(1 \quad \frac{x}{\sqrt{x^{2}+1}}\right)
\end{aligned}
$$

$$
=\frac{1}{x+\sqrt{x^{2}+1}}-\left(\frac{\sqrt{x^{2}+1}+x}{\sqrt{x^{2}+1}}\right)=\frac{1}{\sqrt{x^{2}+1}} \text { and } g(x)=x
$$

Using the formula $\int f(x) g^{\prime}(x) d x=f(x) g(x)-\int g(x) f^{\prime}(x) d x$, we get

$$
\begin{aligned}
\int \ln \left(x+\sqrt{x^{2}+1}\right) \cdot 1 d x & =\left\{\ln \left(x+\sqrt{x^{2}+1}\right)\right\} \cdot x-\int x \cdot \frac{1}{\sqrt{x^{2}+1}} d x \\
& \int \ln \left(x+\sqrt{x^{2}+1}\right) x-\frac{1}{2} \int\left(x^{2}+1\right)^{\frac{1}{2}}(2 x) d x \\
& =x \ln \left(x+\sqrt{x^{2}+1}\right)-\frac{1}{2}\left[\frac{\left(x^{2}+1\right)^{\frac{1}{2}}}{\frac{1}{2}} \quad c_{1}\right] \\
& =x \ln \left(x+\sqrt{x^{2}+1}\right)-\sqrt{x^{2}+1}+c_{1}, \text { where } c=\frac{1}{2} c_{1}
\end{aligned}
$$

Example 6. Evaluate $\int x^{2} \cdot a e^{a x} d x$
Solution: If we put $f(x)=x^{2} \quad$ and $\quad g^{\prime}(x)=a e^{a x}$, then

$$
f^{\prime}(x)=2 x \quad \text { and } \quad g(x)=e^{a x}
$$

Using the formula $\int f(x) g^{\prime}(x) d x=f(x) g(x)-\int g(x) f^{\prime}(x) d x$, we get

$$
\begin{aligned}
\int x^{2} \cdot a x^{2} d x & =x^{2} e^{a x}-\int e^{a x} \cdot(2 x) d x \\
& =x^{2} e^{a x}-2 \int x e^{a x} d x
\end{aligned}
$$

But $\int x e^{a x} d x=x\left(\frac{e^{a x}}{a}\right)-\int\left(\frac{e^{a x}}{a}\right) \times 1 \cdot d x$

$$
=\frac{1}{a} x e^{a x}-\frac{1}{a} \int e^{a x} d x=\frac{1}{a} x e^{a x}-\frac{1}{a}\left(\frac{e^{a x}}{a}\right)+c_{1}
$$

Thus $\int x^{2} a e^{a x} d x=x^{2} e^{a x}-2\left[\frac{1}{a} \cdot x e^{a x}-\frac{1}{a^{2}} e^{a x}+c_{1}\right]$

$$
=x^{2} e^{a x}-\frac{2}{a} \cdot x e^{a x}+\frac{2}{a^{2}} e^{a x}+c_{1} \quad \text { where } c=2 c_{1}
$$

$$
\text { version: } 1.1
$$

Example 7. Find $\int e^{a x} \cos b x d x$.
Solution: $\quad$ Let $f(x)=e^{a x} \quad$ and $\quad g^{\prime}(x)=\cos b x$
then

$$
f^{\prime}(x)=a \cdot e^{a x} \quad \text { and } \quad g(x) \quad \frac{\sin b x}{b}
$$

Thus $\int e^{a x} \cos b x d x=e^{a x} \quad\left(\frac{\sin b x}{b}\right) \quad \int\left(\frac{\sin b x}{b}\right) \quad\left(a e^{a x}\right) d x$

$$
=\frac{1}{b} e^{a x} \sin b x \quad \frac{a}{b} \int e^{a x} \sin b x d x
$$

Integrating $\int e^{a x} \sin b x d x$, by parts, we get

$$
\begin{aligned}
\int e^{a x} \sin b x d x & =e^{a x} \times\left(-\frac{\cos b x}{b}\right)-\int\left(-\frac{\cos b x}{b}\right) \times\left(a e^{a x}\right) d x+c_{1} \\
& =\frac{1}{b} e^{a x} \cos b x \quad \frac{a}{b} \int e^{a x} \cos b x d x \quad c_{1}
\end{aligned}
$$

Putting the value of $\int e^{a x} \sin b x d x$ in (I), we get

$$
\begin{aligned}
& \int e^{a x} \cos b x d x=\frac{1}{b} e^{a x} \sin b x-\frac{a}{b}\left[-\frac{1}{b} e^{a x} \cos b x+\frac{a}{b} \int e^{a x} \cos b x d x \quad c_{1}\right] \\
& =\frac{1}{b} e^{a x} \sin b x+\frac{a}{b^{2}} e^{a x} \cos b x-\frac{a^{2}}{b^{2}} \int e^{a x} \cos b x d x-\frac{a}{b} \cdot c_{1} \\
& \text { or }\left(\frac{a^{2}}{b^{2}}\right) \int e^{a x} \cos b x d x=\frac{1}{b} e^{a x} \sin b x+\frac{a}{b^{2}} e^{a x} \cos b x-\frac{a}{b} \cdot c_{1} \\
& \text { i.e. } \int e^{a x} \cos b x d x=\frac{b^{2}}{a^{2}+b^{2}}\left[\frac{1}{b^{2}} e^{a x} \sin b x-\frac{a}{b^{2}} e^{a x} \cos b x\right] \quad \frac{b^{2}}{a^{2}+b^{2}} \quad \frac{a}{b} \cdot c_{1} \\
& =\frac{e^{a x}}{a^{2}+b^{2}}[b \sin b x+a \cos b x]+c, \quad \text { where } c=\frac{a b}{b\left(a^{2}+b^{2}\right)} c_{1}
\end{aligned}
$$

If we put $a=r \cos \theta \quad$ and $\quad b=r \sin \theta$;
then $a^{2}+b^{2}=r^{2} \Rightarrow r=\sqrt{a^{2}+b^{2}}$

$$
\frac{b}{a}=\frac{r \sin \theta}{r \cos \theta}=\tan \theta \Rightarrow \theta=\tan ^{-1} \frac{b}{a}
$$

and $a \cos b x+b \sin b x=r \cos \theta \cos b x+r \sin \theta \sin b x$

$$
\begin{aligned}
& =r[\cos b x \cos \theta+\sin b x \sin \theta]=r \cos (b x-\theta) \\
& \quad \Rightarrow \sqrt{a^{2} b^{2}} \cos \left(b x \quad \tan ^{-1} \frac{b}{a}\right),=\left(\theta \quad \tan ^{-1} \frac{b}{a}\right)
\end{aligned}
$$

The answer can be written as:

$$
\int e^{a x} \cos b x d x=\frac{1}{\sqrt{a^{2}-b^{2}}} e^{a x} \cos \left(b x-\tan ^{-1} \frac{b}{a}\right)+c
$$

Example 8. Evaluate $\int \sqrt{a^{2}+x^{2}} d x$
Solution: $\int \sqrt{a^{2}+x^{2}} \cdot 1 d x=\left(\sqrt{a^{2}+x^{2}}\right) x-\int x \cdot \frac{1}{2}\left(a^{2}+x^{2}\right)^{\frac{1}{2}} \cdot 2 x d x$

$$
\begin{aligned}
& =x \sqrt{a^{2}+x^{2}}-\int \frac{x^{2}}{\sqrt{a^{2}+x^{2}}} d x \\
& =x \sqrt{a^{2}+x^{2}}-\int \frac{a^{2}+x^{2}-a^{2}}{\sqrt{a^{2}+x^{2}}} d x \\
& =x \sqrt{a^{2}+x^{2}}-\int \sqrt{a^{2}+x^{2}} d x+\int \frac{a^{2}}{\sqrt{a^{2}+x^{2}}} d x \\
& 2 \int \sqrt{a^{2}+x^{2}} d x=x \sqrt{a^{2}+x^{2}}+a^{2} \cdot \int \frac{1}{\sqrt{a^{2}+x^{2}}} d x \\
& =x \sqrt{a^{2}+x^{2}}+\mathrm{a}^{2}\left[\ln \left(x+\sqrt{a^{2}+x^{2}}\right)+c_{1}\right]
\end{aligned}
$$

(See Example 1 Article 3.4)
$\int \sqrt{a^{2}+x^{2}} d x=\frac{x}{2} \sqrt{a^{2}+x^{2}}+\frac{a^{2}}{2} \ln \left(x+\sqrt{a^{2}+x^{2}}\right)+\mathrm{c}$, where $\mathrm{c}=\frac{a^{2} c_{1}}{2}$
Similarly integrals $\int \sqrt{a^{2}-x^{2}} d x$ and $\int \sqrt{x^{2}-a^{2}}$ can be evaluated.
Example 9. Evaluate $\int \sin ^{4} x d x$.
Solution: $\quad \int \sin ^{4} x d x=\int \sin ^{3} x \nu \sin ^{3} x d x \quad-\int \sin ^{3} x\left(1 \quad \cos ^{3} x\right) d x$

$$
\begin{aligned}
& =-\int \sin ^{3} x d x \quad \int \sin ^{3} x \cos ^{3} x d x \\
& =-\int \frac{1-\cos 2 x}{2} d x \quad \int \sin ^{3} x \cos ^{3} x d x \\
& \text { Integrating } \int \sin ^{3} x \cos ^{3} x d x \text { by parts, we have }
\end{aligned}
$$

$$
\begin{aligned}
& =-\cos x\left(\frac{\sin ^{3} x}{3}\right) \quad \int \frac{\sin ^{3} x}{3} \times(-\sin x) d x \quad[\because \text { If } f(x)=\cos x \text { and } \\
& g^{\prime}(x)=\sin ^{3} x \cos x . \\
& =\frac{1}{3} \cos x \sin ^{3} x \quad \frac{1}{3} \int \sin ^{4} x d x \quad \ldots . .(\mathrm{II})+\text { then } f^{\prime}(x)=\sin x \\
& \text { and } g(x)=\sin ^{3} \frac{\sin ^{3} x}{3}]
\end{aligned}
$$

Putting the value of $\int \sin ^{3} x \cos ^{3} x d x$ in (I), we obtain,

$$
\begin{aligned}
\int \sin ^{4} x d x & =-\int\left(\frac{1}{2} \quad \frac{\cos 2 x}{2}\right) d x \quad\left[\frac{1}{3} \cos x \sin ^{3} x \quad \frac{1}{3} \int \sin ^{4} x d x\right] \\
& =\frac{1}{2} \int 1 d x \quad \frac{1}{2} \int \cos 2 x d x \quad \frac{1}{3} \cos x \sin ^{3} x \quad \frac{1}{3} \int \sin ^{4} x d x \\
\text { or }\left(1+\frac{1}{3}\right) \int \sin ^{4} x d x & =\frac{1}{2} \times-\frac{1}{2}\left(\frac{\sin 2 x}{2}\right) \quad e_{1} \quad \frac{1}{3} \cos x \sin ^{3} x \\
\int \sin ^{4} x d x & =\frac{3}{4}\left[\frac{1}{2} \times-\frac{1}{4} \sin 2 x-\frac{1}{3} \cos x \sin ^{3} x \quad c\right] \\
& =\frac{5}{8} x \quad \frac{3}{16} \sin 2 x \quad \frac{1}{4} \cos x \sin ^{3} x \quad c \quad \text { where } c \quad \frac{3}{4} c_{1}
\end{aligned}
$$

Example 10. Evaluate $\int \frac{e^{x^{2}}(1+\sin x)}{1+\cos x} d x$.
Solution: $\quad \int \frac{e^{x^{2}}(1+\sin x)}{1+\cos x} d x=\int \frac{e^{x}\left(1+2 \sin \frac{x}{2} \cos \frac{x}{2}\right.}{2 \cos ^{2} \frac{x}{2}} d x\left[\because 1+\cos x=1+2 \cos ^{2} \frac{x}{2} \quad 1\right]$

i.e. $\int \frac{e^{x}(1+\sin x)}{1+\cos x} d x=+\int e^{x}\left(\frac{1}{2} \sec ^{2} \frac{x}{2} \quad \tan \frac{x}{2}\right) d x$

$$
=+\frac{1}{2} \int e^{x} \sec ^{2} \frac{x}{2} d x \quad \int e^{x} \tan \frac{x}{2} d x
$$

But $\int\left(\tan \frac{x}{2}\right) \cdot e^{x} d x=\left(\tan \frac{x}{2}\right) \cdot e^{x} \int e^{x}\left(\sec ^{2} \frac{x}{2}\right) \cdot \frac{1}{2} d x \quad c$, (Integrating by parts)
i.e. $\int e^{x} \tan \frac{x}{2} d x=e^{2} \tan \frac{x}{2} \quad \frac{1}{2} \int e^{x} \sec ^{2} \frac{x}{2} d x \quad c$
Putting the value of $\int e^{x} \tan \frac{x}{2} d x$ in (I), we get
$\int \frac{e^{x}(1+\sin x)}{1+\cos x} d x=\frac{1}{2} \int e^{x} \sec ^{2} \frac{x}{2} d x \quad\left[e^{x} \tan \frac{x}{2} \quad \frac{1}{2} \int e^{x} \sec ^{2} \frac{x}{2} d x=c\right] \quad e^{x} \tan \frac{x}{2} \quad c$
Example 11. Show that $\int e^{a x}\left[a f(x)+f^{\prime}(x)\right] d x=e^{a x} f(c)+c$.
Solution: $\int e^{a x}\left[a f(x)+f^{\prime}(x)\right] d x=\int e^{a x} \cdot a f(x) d x+\int e^{a x} \cdot f^{\prime}(x) d x \quad \ldots$ (i)
In the second integral, let $\varphi(x)=e^{a x}$ and $g^{\prime}(x)=f^{\prime}(x)$,
then

$$
\varphi^{\prime}(x)=\left(e^{a x}\right) \times a \text { and } g(x)=f(x)
$$

so

$$
\int e^{a x} \cdot f^{\prime}(x) d x=e^{a x} \times f(x)-\int f(x) \times\left(a e^{a x}\right) d x+c
$$

$$
=e^{a x} f(x) \quad \int a e^{a x} f(s i) d x \quad c
$$

thus $\int e^{a x}\left[a f(x)+f^{\prime}(x)\right] d x=\int a e^{a x} f(x) d x+\int e^{a x} f^{\prime}(x) d x+c$

$$
\begin{aligned}
& =\int a e^{a x} f(x) d x+\left[e^{a x} f(x)-\int a e^{a x} f(x) d x+c\right] \\
& =e^{a x} f(x)+c
\end{aligned}
$$

## EXERCISE 3.4

1. Evaluate the following integrals by parts add a word representing all the functions are defined.
(i) $\int x \sin x d x$
(ii) $\int \ln x d x$
(iii) $\int x \ln x d x$
(iv) $\int x^{2} \ln x d x$
(v) $\int x^{2} \ln x d x$
(vii) $\int \operatorname{Tan}^{-1} x d x$
(viii) $\int x^{2} \sin x d x$
(ix) $\int x^{2} \operatorname{Tan}^{-1} x d x$
(xi) $\int x^{3} \operatorname{Tan}^{-1} x d x$
(xiii) $\int \operatorname{Sin}^{-1} x d x$
(xiv) $\int x \operatorname{Sin}^{-1} x d x$
(xv) $\int e^{x} \sin x \cos x d x$
(xvi) $\int x \sin x \cos x d x$
(xvii) $\int x \cos ^{2} x d x$
(xviii) $\int x \sin ^{2} x d x$
(xix) $\int(\ln x)^{3} d x$
(xx) $\int(\ln (\tan x) \sec ^{3} x d x$
(xxi) $\int \frac{x \operatorname{Sin}^{-1} x}{\sqrt{1-x^{2}}} d x$
2. Evaluate the following integral.
(i) $\int \tan ^{4} x d x$
(ii) $\int \sec ^{4} x d x$
(iii) $\int e^{x} \sin 2 x \cos x d x$
(iv) $\int \tan ^{3} x \sec x d x$
(v) $\int x^{3} e^{3 x} d x$
(vi) $\int e^{-x} \sin 2 x d x$
(vii) $\int e^{2 x} \cos 3 x d x$
(viii) $\int \operatorname{cosec}^{3} x d x$
3. Show that $\int e^{a x} \sin b x d x=\frac{1}{\sqrt{a^{2}+b^{2}}} e^{a x} \sin \left(b x+\operatorname{Tan}^{2} \frac{b}{a}\right) \quad c$.
4. Evaluate the following indefinite integrals.
(i) $\int \sqrt{a^{2}-x^{2}} d x$
(ii) $\int \sqrt{x^{2}-\mathrm{a}^{2}} d x$
(iii) $\int \sqrt{4-5 x^{2}} d x$
(iv) $\int \sqrt{3-4 x^{2}} d x$
(v) $\int \sqrt{x^{2}+4} d x$
(vi) $\int x^{2} e^{a x} d x$

5. Evaluate the following integrals.
(i) $\int e^{x}\left(\frac{1}{x}+\ln x\right) d x$
(ii) $\int e^{x}(\cos x+\sin x) d x$
(iii) $\int e^{x x}\left[a \operatorname{Sec}^{-1} x+\frac{1}{x \sqrt{x^{2}-1}}\right] d x$
(iv) $\int e^{x x}\left[\frac{3 \sin x-\cos x}{\sin ^{2} x}\right] d x$
(v) $\int e^{x x}[-\sin x+2 \cos x] d x$
(vi) $\int \frac{x e^{x}}{(1+x)^{2}} d x$
(vii) $\int e^{-x}(\cos x-\sin x) d x$
(viii) $\int \frac{e^{a \cdot 2 \cdot a x^{2} x}}{\left(1+x^{2}\right)} d x$
(ix) $\int \frac{2 x}{1-\sin x} d x$
(x) $\int \frac{e^{x}(1+x)}{(2+x)^{2}} d x$
(xi) $\int\left(\frac{1-\sin x}{1-\cos x}\right) e^{x} d x$

### 3.5 INTEGRATION INVOLVING PARTIAL FRACTIONS

If $P(x), Q(x)$ are polynomial functions and the denominator $Q(x)(\neq 0)$, in the rational function $\frac{P(x)}{Q(x)}$, can be factorized into linear and quadratic (irreducible) factors, then the rational function is written as a sum of simpler rational functions, each of which can be integrated by methods already known to us.

Here we will give examples of the following three cases when the denominator $Q(x)$ contains

Case I. Non-repeated linear factors.
Case II. Repeated and non-repeated linear factors.
Case III. Linear and non-repeated irreducible quadratic factors or non repeated irreducible quadratic factors.

## EXAMPLES OF CASE I

Example 1: $\quad$ Evaluate $\int \frac{-x+6}{2 x^{2}-7 x+6} d x, \quad(x>2)$
Solution: $\quad$ The denominator $2 x^{2}-7 x+6=(x-2)(2 x-3)$,
Let

$$
\frac{-x+6}{(x-2)(2 x-3)}=\frac{\mathrm{A}}{x-2}+\frac{\mathrm{B}}{2 x-3}
$$

or $\quad-x+6=A(2 x-3)+B(x-2)$ which is true for all $x$
Putting $x=2$, we get

$$
-2+6=A(4-3)+B \times 0 \Rightarrow A=4
$$

and Putting $\quad x=\frac{3}{2}$, we get $-\frac{3}{2}+6=A(0)+B\left(\frac{3}{2}-2\right)$
or

$$
\frac{9}{2}=B\left(-\frac{1}{2}\right) \Rightarrow B=-9
$$

Thus $\int \frac{-x+6}{(x-2)(2 x-3)} d x=\int\left(\frac{4}{x-2}+\frac{-9}{2 x-3}\right) d x$

$$
\begin{aligned}
& =4 \int(x-2)^{-1} 1 \cdot d x-\frac{9}{2} \int(2 x-3)^{-1} \cdot 2 d x \\
& =4 \ln (x-2)-\frac{9}{2} \ln (2 x-3)+c, \quad(x>2)
\end{aligned}
$$

Example 2: $\quad$ Evaluate $\int \frac{2 x^{3}-9 x^{2}+12 x}{2 x^{2}-7 x+6} d x, \quad(x>2)$
Solution: After performing the division by the denominator, we get

$$
\begin{aligned}
\int \frac{2 x^{3}-9 x^{2}+12 x}{2 x^{2}-7 x+6} d x & =\int\left(x-1+\frac{-x+6}{2 x^{2}-7 x+6}\right) d x \\
& =\int x d x-\int 1 d x+\int \frac{4}{(x-2)} d x+\int \frac{-9}{2 x-3} d x, \quad \text { (See the Example 1) } \\
& =\frac{x^{2}}{2}-x+4 \ln (x-2)-\frac{9}{2}(2 x-3)+c, \quad(x>2)
\end{aligned}
$$

Example 3: Evaluate (i) $\int \frac{2 a}{x^{2}-a^{2}} d x,(x>a)$
(ii) $\int \frac{2 a}{a^{2}-x^{2}} d x,(x<a)$

Solution: (i) The denominator $x^{2}-a^{2}=(x-a)(x+a)$,
Let $\frac{2 a}{(x-a)(x+a)}=\frac{A}{x-a}+\frac{B}{x+a}$

$$
=\frac{1}{x-a}-\frac{1}{x+a}, \text { (Applying the method of partial fractions) }
$$

Thus $\int \frac{2 a}{(x-a)(x+a)} d x=\int\left(\frac{1}{x-a}-\frac{1}{x+a}\right) d x=\int(x-a)^{-1} \cdot 1 d x+(x-a)^{-1} \cdot 1 d x$

$$
=\ln |x-a|-\ln |x+a|+c=\ln \frac{|x-a|}{|x+a|}+c, \quad(x>a)
$$

(ii) It is left as an exercise.

## EXAMPLES OF CASE II

Example 4: Evaluate $\int \frac{7}{(x-1)} \frac{1}{(x+1)} d x \quad(x \quad 1)$
Solution: We write

$$
\begin{aligned}
& \int \frac{7 x-1}{(x-1)^{2}(x+1)} d x=\frac{A}{x-1}+\frac{B}{(x-1)^{2}}+\frac{C}{x+1} \\
& =\frac{2}{x-1}+\frac{3}{(x-1)^{2}}-\frac{2}{x+1} \quad \text { Applying the method } \\
& \text { of Partial Fractions } \\
& \text { Thus } \int \frac{7 x-1}{(x-1)^{2}(x+1)} d x=\int\left[\frac{2}{x-1}+\frac{3}{(x-1)^{2}}-\frac{2}{x+1}\right] d x \\
& =2 \int(x-1)^{-1} \cdot 1 d x+3 \int(x-1)^{-2} \cdot 1 d x-2 \int(x+1)^{-1} \cdot 1 d x \\
& =2 \ln (x-1)+3 \frac{(x-1)^{-2+1}}{-2+1}-2 \ln (x+1)+c \quad(x>1)
\end{aligned}
$$

$$
\begin{aligned}
& =2[\ln (x-1)-\ln (x+1)]+3\left[\frac{(x-1)^{-2}}{-1}\right] \quad c \\
& =2 \ln \left(\frac{x-1}{x+1}\right)-\frac{3}{x-1}+c
\end{aligned}
$$

Example 5: Evaluate $\int \frac{e^{x}\left(x^{2}+1\right)}{(x+1)^{2}} d x$
Solution: $\int \frac{e^{x}\left(x^{2}+1\right)}{(x+1)^{2}} d x=\int e^{x}\left(1-\frac{2}{(x+1)}+\frac{2}{(x+1)^{2}}\right) d x$, (By Partial Fractions)

$$
\Rightarrow \int \frac{e^{x}\left(x^{2}+1\right)}{(x+1)^{2}} d x=\int e^{x} d x-2 \int \frac{e^{x}}{x+1} d x+2 \int \frac{e^{x}}{(x+1)^{2}} d x
$$

We integrate by parts the last integral on the right side of (I).

$$
\begin{aligned}
& \int e^{x}(x+1)^{-2} d x=\mathrm{e}^{x} \cdot \frac{(x+1)^{-1}}{-1}-\int\left(\frac{(x+1)^{-1}}{-1}\right) \cdot e^{x} d x \\
& \text { or } \int \frac{e^{x}}{(x+1)^{2}} d x=\frac{e^{x}}{x+1} \quad \int \frac{e^{x}}{x+1} d x
\end{aligned}
$$

Using (II), (I) becomes

$$
\begin{aligned}
& \int \frac{e^{x}\left(x^{2}+1\right)}{(x+1)^{2}} d x=\int e^{x} d x-2 \int \frac{e^{x}}{x+1} d x+2\left(-\frac{e^{x}}{x+1}+\int \frac{e^{x}}{x+1} d x\right) \\
& =\left(e^{x}+c\right)-2 \int \frac{e^{x}}{x+1} d x-\frac{2 e^{x}}{x+1}+2 \int \frac{e^{x}}{x+1} d x \\
& =e^{x}-\frac{2 e^{x}}{x+1}+c=\frac{x e^{x}+e^{x}-2 e^{x}}{x+1}+c=\frac{e^{x}(x-1)}{x+1}+c
\end{aligned}
$$

Example 6: Evaluate $\int \frac{1}{x^{3}-1} d x$
Solution: The denominator $x^{3}-1=(x-1)\left(x^{2}+x+1\right)$,
version: 1.1

Let $\frac{1}{(x-1)\left(x^{2}+x+1\right)}=\frac{A}{x-1}+\frac{B x+C}{x^{2}+x+1}$

$$
\begin{aligned}
& =\frac{\frac{1}{3}}{x-1}+\frac{\left(-\frac{1}{3}\right) x-\frac{2}{3}}{x^{2}+x+1} \quad \text { (Applying the method of partial fractions) } \\
& =\frac{1}{3} \cdot \frac{1}{x-1} \cdot \frac{1}{3} \cdot \frac{x+2}{x^{2}+x+1}
\end{aligned}
$$

Thus $\frac{1}{(x-1)\left(x^{2}+x+1\right)} d x=\int\left(\frac{1}{3} \cdot \frac{1}{x-1}-\frac{1}{6} \cdot \frac{2 x+4}{x^{2}+x+1}\right) d x$

$$
\begin{aligned}
& =\int\left[\frac{1}{3} \cdot \frac{1}{x-1} 1 . d x-\frac{1}{6} \cdot \frac{2 x+1}{x^{2}+x+1}-\frac{1}{6} \cdot \frac{3}{x^{2}+x+1}\right) d x \\
& =\frac{1}{2} \int(x-1)^{3} d x-\frac{1}{6} \int\left(x^{2}+x+1\right)^{2}(2 x+1) d x-\frac{1}{2} \int \frac{1}{\left(x+\frac{1}{2}\right)^{2}+\left(\frac{\sqrt{3}}{2}\right)^{2}} d x \\
& =\frac{1}{3} \ln |x-1|-\frac{1}{6} \ln \left(x^{2}+x+1\right)-\frac{1}{2} \cdot \frac{1}{\frac{\sqrt{3}}{2}} \operatorname{Tan}^{-1}\left(\frac{x+\frac{1}{2}}{\frac{\sqrt{3}}{2}}\right) \quad c \\
& =\frac{1}{3} \ln |x-1|-\frac{1}{6} \ln \left(x^{2}+x+1\right)-\frac{1}{\sqrt{3}} \operatorname{Tan}^{-1}\left(\frac{2 x+1}{\sqrt{3}}\right) \quad c
\end{aligned}
$$

## Note: $\quad \mathbf{x}^{2} \times \mathbf{x}+\mathbf{1}$ is positive for real values of $\mathbf{x}$.

Example 7: $\quad$ Evaluate $\int \frac{2 x}{x^{2}-1} d x$
Solution: $\quad$ Put $x^{2}=t$, then $2 x d x=d t$ and

$$
\begin{aligned}
\int \frac{2 x}{x^{2}-1} d x & =\int \frac{1}{t^{2}-1} d t=\int \frac{1}{(t-1)\left(t^{2}+t+1\right)} \\
& =\frac{1}{3} \ln |t-1|-\frac{1}{6} \ln \left(t^{2}+t+1\right)-\frac{1}{\sqrt{3}} \operatorname{Tan}^{-1}\left(\frac{2 t+1}{\sqrt{3}}\right) \quad c
\end{aligned}
$$

(See the example 6)

$$
=\frac{1}{3} \ln \left|x^{2}-1\right|-\frac{1}{6} \ln \left(x^{2}+x^{2}+1\right)-\frac{1}{\sqrt{3}} \operatorname{Tan}^{-1}\left(\frac{2 x^{2}+1}{\sqrt{3}}\right) \quad c
$$

Example 8: $\quad$ Evaluate $\int \frac{3}{x\left(x^{2}-1\right)} d x, x \neq 0, x \neq-1$

Solution: Let $\frac{3}{x\left(x^{2}-1\right)}=\frac{A}{x} \quad \frac{B}{x-1} \quad \frac{C x+D}{x+x+1}$

$$
=\frac{-3}{x} \quad \frac{1}{x-1} \quad \frac{2 x+1}{x^{2}+x+1} \quad \text { (By the method of partial fractions) }
$$

Let $\int \frac{3}{x(x-1)\left(x^{2}+x+1\right)} d x=\int\left(\frac{-3}{x}+\frac{1}{x-1}+\frac{2 x+1}{x^{2}+x+1}\right) d x$

$$
\begin{aligned}
& =-3 \int(x)^{-1} 1 . d x+\int(x-1)^{-1} 1 . d x+\int\left(x^{2}+x+1\right)^{-1}(2 x+1) d x \\
& =-3 \ln |x|+\ln |x-1|+\ln \left(x^{2}+x+1\right)+c \\
& =-3 \ln |x|+\ln |x-1|\left(x^{2}+x+1\right)+c \\
& =-3 \ln |x|+\ln \left|x^{2}-1\right|+c
\end{aligned}
$$

Example 9: $\quad$ Evaluate $\int \frac{2 x^{2}+6 x}{\left(x^{2}+1\right)(x+2 x+3)} d x$
Solution: We write
Let $\frac{2 x^{2}+6 x}{\left(x^{2}+1\right)\left(x^{2}+2 x+3\right)}=\frac{A x+B}{x^{2}+1}+\frac{C x+D}{x^{2}+2 x+3}$

$$
=\frac{2 x+1}{x^{2}+1}-\frac{2 x+3}{x^{2}+2 x+3} \text { (Applying the method of partial fractions) }
$$

Thus $\int \frac{2 x^{2}+6 x}{\left(x^{2}+1\right)\left(x^{2}+2 x+3\right)} d x=\int\left(\frac{2 x+1}{x^{2}+1}-\frac{2 x+3}{x^{2}+2 x+3}\right) d x$

$$
=\int \frac{2 x}{x^{2}+1} d x+\int \frac{1}{x^{2}+1}-\int \frac{2 x+2}{x^{2}+2 x+3} d x-\int \frac{1}{x^{2}+2 x+3} d x
$$

$$
\begin{aligned}
& =\int\left(x^{2}+1\right)^{-1}(2 x) d x+\int \frac{1}{x^{2}+1} d x-\int(x+2 x+3)^{-1}(2 x+2) d x-\int \frac{1}{(x+1)^{2}+\sqrt{2} \sqrt{2}} d x \\
& =\ln \left(x^{2}+1\right)+\operatorname{Tan}^{-1} x-\ln \left(x^{2}+2 x+3\right)-\frac{1}{\sqrt{2}} \operatorname{Tan}^{-1} \frac{x+1}{\sqrt{2}} \quad c
\end{aligned}
$$

## EXERCISE 3.5

## Evaluate the following integrals.

1. $\int \frac{3 x+1}{x^{2}-x-6} d x$
2. $\int \frac{5 x+8}{(x+3)(2 x-1)} d x$
3. $\int \frac{x^{2}+3 x-34}{x^{2}+2 x-15} d x$
4. $\int \frac{(a-b) x}{(x-a)(x-b)} d x,(a>b)$
5. $\int \frac{3-x}{1-x-6 x^{2}} d x$
6. $\int \frac{2 x}{x^{2}-a^{2}} d x$
7. $\int \frac{1}{6 x^{2}+5 x-4} d x$
8. $\int \frac{2 x^{2}-3 x^{2}-x-7}{2 x^{2}-3 x-2} d x$
9. $\int \frac{3 x^{2}-12 x+11}{(x-1)(x-2)(x-3)} d x$
10. $\int \frac{2 x-1}{x(x-1)(x-3)} d x$
11. $\int \frac{5 x^{2}+9 x+6}{\left(x^{2}-1\right)(2 x+3)} d x$
12. $\int \frac{4+7 x}{(1+x)^{2}(2+3 x)} d x$
13. $\int \frac{2 x^{2}}{(x-1)^{2}(x+1)} d x$
14. $\int \frac{1}{(x-1)(x+1)^{2}} d x$
15. $\int \frac{x+4}{x^{2}-3 x^{2}+4} d x$
16. $\int \frac{x^{3}-6 x^{2}+25}{(x+1)^{2}(x-2)^{2}} d x$
17. $\int \frac{x^{2}+22 x^{2}+14 x-17}{(x-3)(x+2)^{2}} d x$
18. $\int \frac{x-2}{(x+1)\left(x^{2}+1\right)} d x$
19. $\int \frac{x}{(x-1)\left(x^{2}+1\right)} d x$
20. $\int \frac{9 x-7}{(x+3)\left(x^{2}+1\right)} d x$
21. $\int \frac{1+4 x}{(x-3)\left(x^{2}+4\right)} d x$
22. $\int \frac{12}{+8} d x$
23. $\int \frac{9 x+6}{x^{2}-8} d x$
24. $\int \frac{2 x^{2}+5 x+3}{(x-1)^{2}\left(x^{2}+4\right)} d x$
25. $\int \frac{2 x^{2}-x-7}{(x+2)^{2}\left(x^{2}+x+1\right)} d x$
26. $\int \frac{3 x+1}{\left(4 x^{2}+1\right)\left(x^{2}-x+1\right)} d x$
27. $\int \frac{4 x+1}{\left(x^{2}+4\right)\left(x^{2}+4 x+5\right)} d x$
28. $\int \frac{6 a^{2}}{\left(x^{2}+a^{2}\right)\left(x^{2}+4 a^{2}\right)} d x$
29. $\int \frac{2 x^{2}-2}{\left(x^{4}+x^{2}+1\right)} d x$
30. $\int \frac{3 x-8}{\left(x^{2}-x+2\right)\left(x^{2}+x+2\right)} d x$
31. $\int \frac{3 x^{3}+4 x^{2}+9 x+5}{\left(x^{2}+x+1\right)\left(x^{2}+2 x+3\right)} d x$

### 3.6 THE DEFINITE INTEGRALS

We have already discussed in section 3.2 about the indefinite integral that is, if $\phi^{\prime}(x)=$ $f(x)$, then

$$
\int f(x) d x=\phi(x)+c \text {, where } c \text { is an arbitrary constant }
$$

If $\int f(x) d x=\phi(x)+c$, then the integral of $f$ from $a$ to $b$ is denoted by $\int_{a}^{b} f(x) d x$ (read as
intergral from $a$ to $b$ of $f$ of $x, d x$ ) and is evaluated as:

$$
\begin{aligned}
\int_{a}^{b} f(x) d x & =\int_{a}^{b} \phi^{\prime}(x) d x \quad \text { (if } f(x)=\phi^{\prime}(x)) \\
& =\left|\phi(x)+c\right|_{a}^{b}=[\phi(b)+c]-[\phi(a)+c]=\phi(b)-\phi(a)
\end{aligned}
$$

$\int_{a}^{b} f(x) d x$ has a definite value $\phi(b)-\phi(a)$, so it is called the definite integral of $f$ from $a$ to $b$. $\phi(b)-\phi(a)$ is denoted as $[\phi(x)]_{a}^{b}$ or $\phi(x)]_{a}^{b}$ (read $\phi(x)$ from $a$ to $b$ )

The interval $[a, b]$ is called the range of integration while $a$ and $b$ are known as the lower and upper limits respectively.

As $\phi(b)-\phi(a)$ is a definite value, so the variable of integration $x$ in $\int f(x) d x$ can be replaced by any other letter.
i.e. $\int f(x) d x=\int f(t) d t=\phi(b)-\phi(a)$

Note: If the lower limit is a constant and the upper limit is a variable, then the integral is a function of the upper limit, that is, $\int f(t) d t=|\phi(t)|_{a}^{b}=\phi(x)-\phi(a)$

For Example, $\int \frac{1}{2} 3 t^{2} d t=\left[t^{2}\right]_{a}^{b}=x^{3}-a^{3}$
The relation $\phi^{\prime}(x)=f(x)$ shows that $f(x)$ gives the rate of change of $\phi(x)$, so the total change in $\phi(x)$ from $a$ to $b$ as $\phi(b)-\phi(a)$ shows the connection between anti-derivatives and definite integral $\int f(x) d x$.

### 3.6.1 The Area Under The Curve

About 300 B.C. and around this, mathematicians succeeded to find area of plane region like triangle, rectangle, trapezium and regular polygons etc. but the area of the complicated region bounded by the curves and the $x$-axis from $x=a$ to $x=b$ was a challenge for mathematicians before the invention of integral calculus.

Now we give attention to the use of integration for evaluating areas. Suppose that a function $f$ is continuous on interval $a \leq x \leq b$ and $f(x)>0$. To determine the area under the graph of $f$ and above the $x$-axis from $x=a$ to $x=b$, we follow the idea of Archimedes (287-212 B.C.) for approximating the function by horizontal functions and the area under $f$ by the sum of small rectangles.

To explain the idea mentioned above, we first draw the graph of $f$ defined as: $f(x)=\frac{1}{2} x^{2}$

The graph of $f$ is shown in the figure. We divide the interval $[1,3]$ into four sub-intervals of equal length $=\frac{3-1}{4}=\frac{1}{2}$.

As the subintervals are
$\left[x_{0}, x_{1}\right],\left[x_{1}, x_{2}\right],\left[x_{2}, x_{3}\right],\left[x_{3}, x_{4}\right]$, so
$x_{0}=1, x_{1}=1.5, x_{2}=2, x_{3}=2.5, x_{4}=3$
In the figure $M A=f\left(x_{0}\right), N B=f\left(x_{1}\right)$ and $M N=\delta x$, so it
is obvious that the area of the rectangle $A M N C<$ the area of the shaded region $A M N B<$ area of the rectangle $D M N B$, that is,
$f\left(x_{0}\right) \delta x<$ area of the shaded region $A M N B<f\left(x_{1}\right) \delta x$
Let $\stackrel{\circ}{x}_{1}, \stackrel{\circ}{x}_{2}, \stackrel{\circ}{x}_{3}, \stackrel{\circ}{x}_{4}$ be the mid point of four subintervals mentioned above.

Then the value of $f$ at $\stackrel{\circ}{x}_{1}$, is $f\left(\stackrel{\circ}{x}_{1}\right)$, so the area of the rectangle $F M N E=f\left(\stackrel{\circ}{x}_{1}\right) \delta x$
(See the rectangle $F M N E$ shown in the figure)
We observe that the area of the rectangle $F M N E$ is approximately equal to the area of the region $A M N B$ under the graph of $f$ from $x_{0}$ to $x_{1}$.
Now we calculate the sum of areas of the rectangles shown in the figure, that is, $f\left(\stackrel{\circ}{x}_{1}\right) \delta x+f\left(\stackrel{\circ}{x}_{2}\right) \delta x+f\left(\stackrel{\circ}{x}_{3}\right) \delta x+f\left(\stackrel{\circ}{x}_{4}\right) \delta x$

$$
=\left[f\left(\stackrel{\circ}{x}_{1}\right)+f\left(\stackrel{\circ}{x}_{2}\right)+f\left(\stackrel{\circ}{x}_{3}\right)+f\left(\stackrel{\circ}{x}_{4}\right)\right] \delta x
$$

$$
\begin{aligned}
& =\left[\frac{1}{2}\left(\frac{x_{0}+x_{1}}{2}\right)^{2}+\frac{1}{2}\left(\frac{x_{1}+x_{2}}{2}\right)^{2}+\frac{1}{2}\left(\frac{x_{2}+x_{3}}{2}\right)^{2}+\frac{1}{2}\left(\frac{x_{3}+x_{4}}{2}\right)^{2}\right] \frac{1}{2} \\
& =\frac{1}{4}\left[\left(\frac{1+1.5}{2}\right)^{2}+\left(\frac{1.5+2}{2}\right)^{2}+\left(\frac{2+2.5}{2}\right)^{2}+\left(\frac{2.5+3}{2}\right)^{2}\right] \\
& =\frac{1}{4}\left[\left(1.25\right)^{2}+\left(1.75\right)^{2}+\left(2.25\right)^{2}+\left(2.75\right)^{2}\right] \\
& =\frac{1}{4}\left(1.5625+3.0625+5.0625+7.5625\right) \\
& =\frac{1}{4}(17.25)=4.3125
\end{aligned}
$$

But $\int \frac{1}{2} x^{2} d x=\left[\frac{1}{2} \cdot \frac{x^{2}}{3}\right]_{1}^{3}=\frac{1}{6}(27-1)=\frac{26}{6}=4.3$
If we go on increasing the number of intervals, then the sum of areas of small rectangles approaches closer to the number 4.3.

If we divide the interval $[1,3]$ into $n$ intervals and take $x_{i}$ the coordinate of any point of the $i$ th interval and $\delta x_{i}=x_{i}-x_{i-1}, i=1,2,3, \ldots, n$, then the sum of areas of $n$ rectangles is $\sum_{i=1}^{n} f\left(x_{i}\right) \delta x$ which tends to the number 4.3 when $n \rightarrow \infty$ and each $\delta x_{i} \rightarrow 0$.

Thus $\lim _{\substack{x \rightarrow \infty \\ x_{i} \rightarrow 0}} \sum_{i=1}^{n} f\left(x_{i}\right) \delta x_{i}=4.3$ and we conclude that

$$
\lim _{\substack{x \rightarrow \infty \\ x_{i} \rightarrow 0}} \sum_{i=1}^{n} f\left(x_{i}\right) \delta_{i} x=\int_{1}^{1} \frac{1}{2} x^{2} d x
$$

Thus the area above the $x$-axis and under the curve $y=f(x)$ from $a$ to $b$ is the definite integral $\int f(x) d x$.

Consider a function $f$ which is continuous on the interval $a \leq x \leq b$ and $f(x)>0$. The graph of $f$ is shown in the figure.
We define the function $A(x)$ as the area above the $x$-axis and under the curve $y=f(x)$ from $a$ to $x$. Let $\delta x$ be a small positive number and $x+\delta x$ be any number in the interval $[a, b]$ such that $a<x<x+\delta x$.

Let $P\left(x, f(x)\right)$ and $Q(x+\delta x, f(x+b x))$ be two points on the graph of $f$. The ordinates $P M$ and $Q N$ are drawn and two rectangles $P M N R, S M N Q$ are completed.

According to above definition, the area above the $x$-axis and under the curve $y=f(x)$ from $a$ to $x+\delta x$
is $A(x+\delta x)$, so the change in area is
$A(x+\delta x)-A(x)$ which is shaded in the figure
Note that the function $f$ is increasing in the interval $\left[x, x+\delta x\right]$.
From the figure, it is obvious that area of the rectangle $P M N R<A(x+\delta x)-A(x)<$ area of the rectangle $S M N Q$, i.e.,

$$
f(x) \delta x<A(x+\delta x)-A(x)<f(x+\delta x) \delta x
$$

Dividing the inequality by $\delta x$, we have

$$
\begin{aligned}
& f(x)<\frac{A(x+\delta x)-A(x)}{d x}<f(x+\delta x) \\
& \lim _{x \rightarrow \infty} f(x)=f(x) \quad \text { and } \quad \lim _{x \rightarrow \infty} f(x+\delta x)=f(x)
\end{aligned}
$$

Since the limits of the extremes in (I) are equal, so

$$
\frac{A(x+\delta x)-A(x)}{\delta x} \longrightarrow f(x) \quad \text { when } \delta x \rightarrow 0
$$

Thus $\quad \lim _{x \rightarrow \infty} \frac{A(x+\delta x)-A(x)}{\delta x}=f(x)$.
or

$$
A^{+}(x)=f(x)
$$

that is, $A(x)$ is an antiderivative of $f$, so $\int f(x) d x=A(x)+c$
and $\int f(x) d x=[A(x)]_{a}^{c}=A(x)-A(a)$

Since $A(x)$ is defined as the area under the curve $y=f(x)$ from $a$ to $x$, so $A(a)=0$
Thus

$$
A(x)=\int f(x) d x
$$

Putting $x=b$ in the equation (I), gives

$$
A(b)=\int f(x) d x
$$

which shows that the area $A$ of the region, above the $x$-axis and under the curve $y=f(x)$ from $a$ to $b$ is given by
$\int_{a}^{b} f(x) d x$, that is, $A=\int_{a}^{b} f(x) d x$
If the graph of $f$ is entirely below the $x$-axis, then the value of each $f\left(x_{i}\right)$ is negative and each product $f\left(x_{i}\right) d x_{i}$, is also negative, so in such a case, the definite integral is negative.

Thus the area, bounded in this case by the curve $y=f(x)$, the $x$-axis and the lines $x=a, x=b$ is $-\int f(x) d x$.

For example, $\sin x$ is negative for $-\pi<x<0$ and is positive for $0<x<\pi$.

Therefore the area bounded by the $x$-axis and graph of $\sin$ function from $-\pi$ to $\pi$ is given by

$$
\begin{aligned}
-\int_{-\pi}^{\pi} \sin x & d x+\int_{0}^{\pi} \sin x d x=\int_{0}^{\pi} \sin x d x+\int_{0}^{\pi} \sin x d x\left[\cup \int_{\pi}^{\pi} f(x) d x=\int_{0}^{\pi} f(x) d x\right] \\
& =[-\cos x]_{0}^{-\pi}+[-\cos x]_{0}^{\pi}=-\left[\cos (-\pi)-\cos 0\right]+[-(\cos \pi-\cos 0)] \\
& =-[(-1)-1]-[(-1)-1]=2+2=4
\end{aligned}
$$

## $\int \sin x d x=\int \cos x]_{0}^{-\pi}-\int \cos \pi-\cos (\pi)-\int(-1) \geq 0$

### 3.6.2 Fundamental Theorem and Properties of Definite Integrals

The Definite integral $\int_{a}^{b} f(x) d x$
gives the area under the curve $y=f(x)$ from $x=a$ to $x=b$ and the $x$-axis (proof is given in the article 3.6.1)

## (b) Fundamental Theorem of Calculus

If $f$ is continuous on $[a, b]$ and $\phi^{\prime}(x)=f(x)$, that is,
$\phi(x)$ is any anti-derivative of $f$ on $[a, b]$, then

$$
\int f(x) d x=\phi(b)-\phi(a)
$$

Note that the difference $\phi(b)-\phi(a)$ is independent of the choice of anti-derivative of the function $f$.
(c) $\int_{a}^{b} f(x) d x=-\int_{a}^{b} f(x) d x$
(d) $\int_{a}^{b} f(x) d x=\int_{a}^{b} f(x) d x+\int_{a}^{b} f(x) d x, \quad a \quad c \quad b$

## Proof of (c) and (d):

(c) If $\phi^{\prime}(x)=f(x)$, that is, if $\phi$ is an anti-derivative of $f$, then using the Fundamental Theorem of Calculus, we get

$$
\int_{a}^{b} f(x) d x=\phi(b)-\phi(a)=-[\phi(a)-\phi(b)]=-\int_{a}^{b} f(x) d x
$$

(d) If $\phi^{\prime}(x)=f(x)$, that is, if $\phi(x)$ is an anti-derivative of $f(x)$, then applying the Fundamental Theorem of Calculus, we have

$$
\int_{a}^{b} f(x) d x=\phi(c) \quad \phi(a) \text { and } \int_{a}^{b} f(x) d x \quad \phi(b) \quad \phi(c)
$$

Thus $\int_{a}^{b} f(x) d x+\int_{a}^{b} f(x) d x=\phi(c)-\phi(a)+\phi(b)-\phi(c)$

$$
=\phi(b)-\phi(c)=\int_{a}^{b} f(x) d x
$$

Other properties of definite integrals can easily be proved by applying the Fundamental Theorem of Calculus.
Now we evaluate some definite integrals in the following examples.
Example 1: $\quad$ Evaluate (i) $\quad \int_{a}^{b}\left(x^{3}+3 x^{4}\right) d x \quad$ (ii) $\quad \frac{1}{2} \frac{x^{2}+1}{x+1} d x$

## (i) $\int_{a}^{b}\left(x^{3}+3 x^{2}\right) d x=\int_{a}^{b} x^{3} d x+\int_{a}^{b} 3 x^{2} d x$

$$
\begin{aligned}
& =\left[\frac{x^{4}}{4}\right]_{1}^{4}+\left[x^{3}\right]_{11}^{4}=\left[\frac{(3)^{4}}{4} \quad \frac{(-1)^{4}}{4}\right] \quad\left[(3)^{2} \quad(1)^{2}\right] \\
& =\left[\frac{81}{4}-\frac{1}{4}\right]+[27-(-1)]=\frac{81-1}{4}+(27+1) \\
& =20+28=48
\end{aligned}
$$

(ii) $\int_{a}^{b} \frac{x^{2}+1}{x+1} d x=\int_{a}^{b} \frac{x^{2}-1+2}{x+1} d x$

$$
\begin{aligned}
& =\int_{a}^{b}\left(\frac{x^{2}-1}{x+1}+\frac{2}{x+1}\right) d x=\int_{a}^{b}\left(x-1+\frac{2}{x+1}\right) d x \\
& =\int_{a}^{b} x d x-\int_{a}^{b} 1 d x+2 \int_{a}^{b} \frac{1}{x+1} d x
\end{aligned}
$$

$$
\begin{aligned}
& =\left[\frac{x^{4}}{2}\right]_{a}^{4}-[x]_{a}^{4}+2[\ln (x+1)]_{a}^{4} \\
& =\left[\frac{(2)^{4}}{2}-\frac{(1)^{4}}{2}\right]-[2-1]+2[\ln (2+1)-\ln (1+1)] \\
& =\left(2-\frac{1}{2}\right)-1+2[\ln 3-\ln 2] \\
& =\frac{1}{2}+2 \ln \frac{3}{2}
\end{aligned}
$$

Example 2: $\quad$ Evaluate (i) $\quad \int_{a}^{\infty} \frac{x^{3}+9 x+1}{x^{2}+9} d x \quad$ (ii) $\int_{a}^{\infty} \sec x(\sec x+\tan x) d x$

## (i) $\int_{a}^{\infty} \frac{x^{3}+9 x+1}{x^{2}+9} d x=\int_{a}^{\infty}\left(\frac{x^{3}+9 x}{x^{2}+9}+\frac{1}{x^{2}+9}\right) d x$

$$
\begin{aligned}
& =\int_{a}^{\infty}\left(\frac{x\left(x^{2}+9\right)}{x^{2}+9}+\frac{1}{x^{2}+9}\right) d x=\int_{a}^{\infty}\left(x+\frac{1}{x^{2}+9}\right) d x \\
& =\int_{a}^{\infty} x d x+\int_{a}^{\infty} \frac{1}{x^{2}+9} d x \\
& =\left(\frac{x^{2}}{2}\right)_{a}^{\infty}-\left[\frac{1}{3} \operatorname{Tan}^{-1} \frac{x}{3}\right]_{a}^{\infty}\left(\sqrt{ } \int \frac{1}{x^{2}+(3)^{2}} d x=\frac{1}{3} \operatorname{Tan}^{-1} \frac{x}{3} \quad c\right) \\
& =\left(\frac{(\sqrt{3})^{2}}{2}-\frac{(0)^{2}}{2}\right)+\frac{1}{3}\left(\operatorname{Tan}^{-1} \frac{\sqrt{3}}{3}-\operatorname{Tan}^{-1} \frac{0}{3}\right) \\
& =\left(\frac{3}{2}-0\right)+\frac{1}{3}\left(\operatorname{Tan}^{-1} \frac{1}{\sqrt{3}}-\operatorname{Tan}^{-1} 0\right) \\
& =\frac{3}{2}+\frac{1}{3}\left(\frac{\pi}{6}-0\right)=\frac{3}{2}+\frac{\pi}{18}\left(\sqrt{ } \operatorname{Tan}^{-1} \frac{1}{\sqrt{3}}=\frac{\pi}{6} \text { and } \operatorname{Tan}^{-1} 0=0\right)
\end{aligned}
$$

(ii) $\int_{0}^{\pi} \sec x(\sec x+\tan x) d x=\int_{0}^{\pi}\left(\sec ^{2} x+\sec x \tan x\right) d x$

$$
\begin{aligned}
& =+\int_{0}^{\pi} \sec ^{2} x d x \quad \int_{0}^{\pi} \sec x \tan x d x \\
& =\left[\tan x\right]_{x}^{\frac{\pi}{2}}+\left[\sec x\right]_{x}^{\frac{\pi}{2}}=\left(\tan \frac{\pi}{4} \quad \tan 0\right) \quad\left(\sec \frac{\pi}{4} \quad \sec 0\right) \\
& =(1-0)+(\sqrt{2}-1)=\sqrt{2}
\end{aligned}
$$

Example 3: $\quad$ Evaluate $\int_{0}^{\pi} \frac{1}{1-\sin x} d x$
Solution: $\int_{0}^{\pi} \frac{1}{1-\sin x} d x=\int_{\frac{\pi}{2}}^{\pi} \frac{1+\sin x}{(1-\sin x)(1+\sin x)} d x$

$$
\begin{aligned}
& =\int_{0}^{\pi} \frac{1+\sin x}{1-\sin ^{2} x} d x=\int_{\frac{\pi}{2}}^{\pi} \frac{1+\sin x}{\cos ^{2} x} d x \\
& =\int_{0}^{\pi}\left(\frac{1}{\cos ^{2} x}+\frac{\sin x}{\cos ^{2} x}\right) d x=\int_{\frac{\pi}{2}}^{\frac{\pi}{2}}\left(\sec ^{2} x \quad \sec x \tan x\right) d x \\
& =\sqrt{2} \quad \text { \{See the solution of example 2(ii) }\}
\end{aligned}
$$

Example 4: $\quad$ Evaluate $\int_{0}^{\pi}(x+|x|) d x$
Solution: $\int_{0}^{\pi}(x+|x|) d x=\int_{0}^{\pi}(x+|x|) d x+\int_{\frac{\pi}{2}}(x+|x|) d x \quad$ (by property (d))

$$
=\int_{0}^{\pi}[x+(-x)] d x+\int_{0}^{\pi}(x+(x)] d x \quad\binom{\because|x|=x}{=x} \text { if } x \geq 0
$$

version: 1.1

$$
\begin{aligned}
& =\int_{-1}^{0} 0 d x+\int_{0}^{1} 2 x d x-0+2 \int_{0}^{2} x d x \\
& =2\left[\frac{x^{2}}{2}\right]_{0}^{2}=2\left(\frac{4}{2}-\frac{0}{2}\right)=4
\end{aligned}
$$

Example 5: Evaluate $\quad \int_{0}^{\pi} \frac{3 x}{\sqrt{x^{2}+9}} d x$
Solution: Let $f(x)=x^{2}+9$. Then $f^{\prime}(x)=2 x$, so

$$
\begin{aligned}
\int \frac{3 x}{\sqrt{x^{2}+9}} d x & =\int \frac{\frac{3}{2}(2 x)}{\sqrt{x^{2}+9}} d x+\frac{3}{2} \int\left(x^{2} 9\right)^{\frac{1}{2}}(2 x) d x \\
& =\frac{3}{2} \int[f(x)]^{\frac{1}{2}} f(x) d x \\
& =\frac{3}{2} \frac{[f(x)]^{\frac{1}{2} \cdot}}{-\frac{1}{2}+1}=3[f(x)]^{\frac{1}{2}}+c=3\left(x^{2}+9\right)^{\frac{1}{2}}+c
\end{aligned}
$$

Thus $\int_{0}^{\pi} \frac{3 x}{\sqrt{x^{2}+9}} d x=\left[3\left(x^{2}+9\right)^{\frac{1}{2}}\right]_{0}^{\frac{1}{2}}=3\left[(7+9)^{\frac{1}{2}}-(0+9)^{\frac{1}{2}}\right]$

$$
=3\left[(16)^{\frac{1}{2}}-(9)^{\frac{1}{2}}\right]=3(4-3)=3
$$

Example 6: Evaluate $\quad \int_{0}^{\pi} \frac{\operatorname{Sin}^{-1} x}{\sqrt{1-x^{2}}} d x, \quad x \neq-1,1$
Solution: Let $t=\operatorname{Sin}^{-1} x$. Then $x=\sin t$ for $-\frac{\pi}{2} \leq t \leq \frac{\pi}{2}$
and $d x=\cos t d t=\sqrt{1-\sin ^{2} t} d t \quad\left[\because \cos t \text { is +ve for }-\frac{\pi}{2} \leq t \leq \frac{\pi}{2}\right]$

$$
=\sqrt{1-x^{2}} d t
$$

$$
\begin{aligned}
& \text { or } \frac{1}{\sqrt{1-x^{2}}} d x=d t \quad(x \neq-1,1) \\
& \text { if } \quad x=\frac{1}{2}, \text { then } \frac{1}{2}=S \text { in } t \quad \Rightarrow t=\operatorname{Sin}^{-1} \frac{1}{2}=\frac{\pi}{6} \\
& \text { and if } x=\frac{\sqrt{3}}{2} \text {, then } \frac{\sqrt{3}}{2}=\operatorname{Sin} t \quad \Rightarrow t=\operatorname{Sin}^{-1} \frac{\sqrt{3}}{2}=\frac{1}{3} \\
& \text { Thus } \int_{1}^{\sqrt{3}} \frac{\operatorname{Sin}^{-1} x}{\sqrt{1-x^{2}}} d x=\int_{\frac{1}{2}}^{\sqrt{3}}\left(\operatorname{Sin}^{-1} x\right) \cdot \frac{1}{\sqrt{1-x^{2}}} d x \\
& =\int_{\frac{1}{2}}^{\pi} t d t \Rightarrow\left(\because x=\operatorname{Sin} t \quad \operatorname{Sin}^{-1} x \quad t\right) \\
& =\left[\frac{t^{2}}{2}\right]_{\frac{1}{2}}^{\frac{1}{2}}=\frac{1}{2}\left[\left(\frac{\pi}{3}\right)^{2}-\left(\frac{\pi}{6}\right)^{2}\right]=\frac{1}{2}\left(\frac{\pi^{2}}{9}-\frac{\pi^{2}}{36}\right) \\
& =\frac{1}{2}\left(\frac{4 \pi^{2}-\pi^{2}}{36}\right)=\frac{3 \pi^{2}}{72}=\frac{\pi^{2}}{24}
\end{aligned}
$$

Example 7: $\quad$ Evaluate $\int_{0}^{\pi} x \cos x d x$
Solution: $\quad$ Applying the formula

$$
\begin{aligned}
\int f(x) \phi^{\prime}(x) d x & =f(x) \phi(x)-\int \phi(x) f^{\prime}(x) d x, \text { we have } \\
\int x \cos x d x & =x \sin x-\int(\sin x)(1) d x \\
& =x \sin x-\left[\left[-\cos x\right)+c_{x}\right] \\
& =x \sin x+\cos x+c \quad \text { where } c=-c_{x}
\end{aligned}
$$

Thus $\int_{0}^{\pi} x \cos x d x=[x \sin x+\cos x]_{x}^{2}$

$$
\begin{aligned}
& =\left(\frac{\pi}{6} \sin \frac{\pi}{6}+\cos \frac{\pi}{6}\right)-(0 \sin 0+\cos 0) \\
& =\frac{\pi}{6} \cdot \frac{1}{2}+\frac{\sqrt{3}}{2}-(0+1)=\frac{\pi}{12}+\frac{\sqrt{3}}{2}-1
\end{aligned}
$$

Example 8: $\quad$ Evaluate $\int x \operatorname{In} x d x$
Solution: $\quad$ Applying the formula

$$
\begin{aligned}
\int f(x) \phi^{\prime}(x) d x & =f(x) \phi(x)-\int \phi(x) f^{\prime}(x) d x, \text { we have } \\
\int(\ln x) x d x= & (\ln x) \cdot \frac{x^{2}}{2}-\int\left(\frac{x^{2}}{2}\right) \cdot \frac{1}{x} d x \\
= & \frac{1}{2} x^{2} \ln x-\frac{1}{2} \int x d x=\frac{1}{2} x^{2} \ln x \cdot \frac{1}{2}\left(\frac{x^{2}}{2}\right) \quad c
\end{aligned}
$$

Thus $\int_{1} x \operatorname{In} x d x=\left[\frac{1}{2} x^{2} \ln x-\frac{x^{2}}{4}\right]_{x}^{c}$

$$
\begin{aligned}
& =\left(\frac{1}{2} e^{2} \ln e-\frac{e}{4}\right)-\left(\frac{1}{2}(1)^{2} \ln 1-\frac{(1)^{2}}{4}\right) \\
& =\left(\frac{e^{2}}{2} \cdot 1-\frac{e^{2}}{4}\right)-\left(\frac{1}{2} \cdot 0-\frac{1}{4}\right) \quad(\because \operatorname{In} e=1 \text { and } \operatorname{In} 1=0) \\
& =\frac{e^{2}}{4}+\frac{1}{4}
\end{aligned}
$$

Example 9: If $\int_{0}^{\frac{1}{2}} f(x) d x=5, \int_{1}^{2} f(x)=3$ and $\int_{0}^{\frac{1}{2}} g(x) d x=4$, then
evaluate the following definite integrals:
(i) $\int_{1}^{2} f(x) d x$
(ii) $\int_{1}^{2}[2 f(x)+3 g(x)] d x$
(iii) $\int_{0}^{1} 3 f(x) d x-\int_{0}^{1} 2 g(x) d x$

Solution: (i) $\int_{a}^{1} f(x) d x=\int_{a}^{1} f(x) d x+\int_{1}^{1} f(x) d x=5+3=8$
(ii) $\int_{a}^{1}[2 f(x)+3 g(x)] d x=\int_{a}^{1} 2 f(x) d x+\int_{a}^{1} 3 g(x) d x$

$$
\begin{aligned}
= & 2 \int_{a}^{1} f(x) d x+3 \int_{a}^{1} g(x) d x \\
= & 2(5)+3(4)=10+12=22
\end{aligned}
$$

(iii) $\int_{a}^{1} 3 f(x) d x-\int_{a}^{1} 2 g(x) d x=3 \int_{a}^{1} f(x) d x-2 \int_{a}^{1} g(x) d x$

$$
=3 \times 5-2 \times 4=15-8=7
$$

## EXERCISE 3.6

## Evaluate the following definite integrals.

1. $\int_{a}^{1}\left(x^{2}+1\right) d x$
2. $\int_{a}^{1}\left(x^{2 / 3}+1\right) d x$
3. $\int_{a}^{1} \frac{1}{(2 x-1)^{2}} d x$
4. $\int_{a}^{2} \sqrt{3-x} d x$
5. $\int_{a}^{2} \sqrt{(2 t-1)} d t$
6. $\int_{a}^{2} x \sqrt{x^{2}-1} d x$
7. $\int_{a}^{3} \frac{x}{x^{2}+2} d x$
8. $\int_{a}^{3}\left(x-\frac{1}{x}\right)^{3} d x$
9. $\int_{a}^{3}\left(x+\frac{1}{x}\right) \sqrt{x^{2}+x+1} d x$
10. $\int_{a}^{3} \frac{d x}{x^{2}+9}$
11. $\int_{a}^{6} \cos t d t$
12. $\int_{a}^{3}\left(x+\frac{1}{x}\right)^{3}\left(1-\frac{1}{x^{2}}\right) d x$
13. $\int_{a}^{2} \ln x d x$
14. $\int_{a}^{3}\left(e^{\frac{x}{2}}-e^{\frac{1}{2}}\right) d x$
15. $\int_{a}^{6} \frac{\cos \theta+\sin \theta}{2 \cos ^{2} \theta} d \theta$
16. $\int_{a}^{6} \cos ^{3} \theta d \theta$
17. $\int_{a}^{6} \cos ^{2} \theta \cot ^{2} \theta d \theta$
18. $\int_{a}^{6} \cos ^{4} t d t$
version: 1.1
19. $\int_{a}^{6} \cos ^{2} \theta \sin \theta d \theta$
20. $\int_{a}^{6}\left(1+\cos ^{2} \theta\right) \tan ^{2} \theta d \theta$
21. $\int_{a}^{6} \frac{\sec \theta}{\sin \theta+\cos \theta} d \theta$
22. $\int_{a}^{1}|x-3| d x$
23. $\int_{1}^{1} \frac{\left(\frac{1}{x^{2}}+2\right)^{3}}{x^{3}} d x$
24. $\int_{a}^{1} \frac{x^{2}-2}{x+1} d x$
25. $\int_{a}^{1} \frac{3 x^{2}-2 x+1}{(x-1)\left(x^{2}+1\right)} d x$
26. $\int_{a}^{6} \frac{\sin x-1}{\cos ^{2} x}$
27. $\int_{a}^{6} \frac{1}{1+\sin x} d x$
28. $\int_{a}^{6} \frac{3 x}{\sqrt{4-3 x}} d x$
29. $\int_{a}^{6} \frac{\cos x}{\sin x(2+\sin x)} d x$
30. $\int_{a}^{6} \frac{\sin x}{(1+\cos x)(2+\cos x)} d x$

### 3.7 APPLICATION OF DEFINITE INTEGRALS.

Here we shall give some examples involving area bounded by the curve and the $x$-axis.
Example 1. Find the area bounded by the curve $y=4-x^{2}$ and the $x$-axis.

Solution: We first find the points where the curve cuts the $x$-axis. Putting $y=0$, we have
$4-x^{2}=0 \Rightarrow x= \pm 2$.
So the curve cuts the $x$-axis at $(-2,0)$ and $(2,0)$
The area above the $x$-axis and under the curve $y=4-x^{2}$ is
shown in the figure as shaded region..

Thus the required area $=\int(4-x) d x=[4 x--]$

$$
\begin{aligned}
& =\left(4(2)-\frac{(2)^{2}}{3}\right)-\left(4(-2)-\frac{(-2)^{2}}{3}\right) \\
& =\left(8-\frac{8}{3}\right)-\left(-8+\frac{8}{3}\right) \\
& =\frac{16}{3}\left(\frac{-16}{3}\right) \quad \frac{32}{3}
\end{aligned}
$$

Example 2. Find the area bounded by the curve $y=x^{3}+3 x^{2}$ and the $x$-axis.
Solution: Putting $y=0$, we have

$$
\begin{aligned}
x^{3}+3 x^{2} & =0 \\
\Rightarrow x^{2}(x+3) & =0 \Rightarrow x=0, x=-3
\end{aligned}
$$

The curve cuts the $x$-axis at $(-3,0)$ and $(0,0)$ (see the figure).

Thus the required area $=\int_{-3}^{0}\left(x^{3}+3 x^{2}\right) d x$

$$
\begin{aligned}
& =\left[\frac{x^{4}}{4}+x^{2}\right]_{-3}^{0} \\
& =\left(\frac{0}{4}+0\right)-\left(\frac{(-3)^{4}}{4}+(-3)^{2}\right) \\
& =0-\left(\frac{81}{4}-27\right)=-\left(\frac{81-108}{4}\right)=-\left(-\frac{27}{4}\right)=\frac{27}{4}
\end{aligned}
$$

Example 3. Find the area bounded by $y=x\left(x^{3}-4\right)$ and the $x$-axis.
Solution: Putting $y=0$, we have

$$
x\left(x^{3}-4\right) \Rightarrow x=0, x= \pm 2
$$

The curve cuts the $x$-axis at $(-2,0),(0,0)$ and $(2,0)$. The graph of $f$ is shown in the figure and we have to calculate the area of the shaded region.

$$
f(x)=x\left(x^{2}-4\right)
$$

$f(x) \geq 0$ for $-2 \leq x \leq 0$, that is, the area in the interval $[-2,0]$ is above the $x$-axis and is equal to

$$
\begin{aligned}
& \int_{0}^{x} x\left(x^{2}-4\right) d x \\
& =\int_{-2}^{0}\left(x^{3} \quad 4 x\right) d x=\left|\frac{x^{4}}{4} \quad 4\left(\frac{x^{2}}{2}\right)\right|_{-2}^{0}=-\left[\frac{x^{4}}{4} \quad 2 x^{2}\right]_{-2}^{0} \\
& =0-\left(\frac{(-2)^{4}}{4}-2(-2)^{2}\right)=0-\left(\frac{16}{4}-8\right)=-(4-8)=4
\end{aligned}
$$

$f(x) \leq 0$ for $0 \leq x \leq 2$, that is, the area in the interval $[0,2]$ is below the $x$-axis and is equal to $-\int_{0}^{x}\left(x^{2}-4\right) d x \ll\left[\frac{x^{4}}{4} \quad 2 x^{2}\right]_{0}^{2}$

$$
\begin{aligned}
& =\left[\left(\frac{16}{4} \quad 2(4)\right) \quad 0\right] \\
& =-[-4-8]=-(-4)=4
\end{aligned}
$$

Thus the area of the shaded region $=4+4=8$
Example 4: Find the area bounded by the curve $f(x)=x^{3}-2 x^{2}+1$ and the $x$-axis in the 1st quadrant.

Solution: As $f(1)=1-2+1=0$, so $x-1$ is factor of $x^{3}-2 x^{2}+1$. By long division, we find that $x^{2}-x-1$ is also a factor of $x^{3}-2 x^{2}+1$.

Solving $x^{2}-x-1=0$, we get

$$
x=\frac{1 \pm \sqrt{1+4}}{2}=\frac{1 \pm \sqrt{5}}{2}
$$

Thus the curve cuts the $x$-axis at $x=1, \frac{1+\sqrt{5}}{2}$ and $\frac{1-\sqrt{5}}{2}$

The graph of the curve is shown in the adjoining figure and the required area is shaded.
The required area $A$ will be

$$
\begin{aligned}
A & =\int_{0}^{A}\left(x^{2}-2 x^{2}+1\right) d x \\
& =\left|\frac{x^{4}}{4}-2 \frac{x^{2}}{3}+x\right|_{0} \\
& =\left(\frac{1}{4}-\frac{2}{3}+1\right)-0=\frac{3-8+12}{12}=\frac{7}{12}
\end{aligned}
$$

Example 5: Find the area between the $x$-axis and the curve $y^{2}=4-x$ in the first quadrant from $x=0$ to $x=3$.

Solution: The branch of the curve above the $x$-axis is

$$
y=\sqrt{4-x}
$$

The area to be determined is shaded in the adjoining figure.
Thus the required area $=\int_{0}^{1} \sqrt{4-x} d x$
Let $4-x=t$ (i), then $-d x=d t \Rightarrow d x=-d t$
Putting $x=0$ and $x=3$ (i), we get $t=4$ and $t=1$
Now the required area $=\int_{t}^{1} t^{\frac{1}{2}} \times(-d t)=-\int_{t}^{1} t^{\frac{1}{2}} d t$

$$
\begin{aligned}
& =\int_{t}^{4} t^{\frac{1}{2}} d t=\left|\frac{t^{0.5}}{3 / 2}\right|_{0}^{4} \\
& =\frac{2}{3}\left|t^{0.5}\right|_{0}^{4}=\frac{2}{3}\left[(4)^{\frac{3}{2}} \quad(1)^{\frac{1}{2}}\right] \quad \frac{2}{3}[8 \quad 4] \quad \frac{14}{3} \text { (square units) }
\end{aligned}
$$

## EXERCISE 3.7

1. Find the area between the $x$-axis and the curve $y=x^{2}+1$ from $x=1$ to $x=2$.
2. Find the area, above the $x$-axis and under the curve $y=5-x^{2}$ from $x=-1$ to $x=2$.
3. Find the area below the curve $y=3 \sqrt{x}$ and above the $x$-axis between $x=1$ and $x=4$.
4. Find the area bounded by $\cos$ function from $x=-\frac{\pi}{4}$ to $x=\frac{\pi}{2}$
5. Find the area between the $x$-axis and the curve $y=4 x-x^{2}$.
6. Determine the area bounded by the parabola $y=x^{2}+2 x-3$ and the $x$-axis.
7. Find the area bounded by the curve $y=x^{3}+1$, the $x$-axis and line $x=2$.
8. Find the area bounded by the curve $y=x^{2}-4 x$ and the $x$-axis.
9. Find the area between the curve $y=x(x-1)(x+1)$ and the $x$-axis.
10. Find the area above the $x$-axis, bounded by the curve $y^{2}=3-x$ from $x=-1$ to $x=2$
11. Find the area between the $x$-axis and the curve $y=-\cos \frac{1}{2} x$ from $x=\pi$ to $\pi$
12. Find the area between the $x$-axis and the curve $y=\sin 2 x$ from $x=0$ to $x=\frac{\pi}{3}$
13. Find the area between the $x$-axis and the curve $y=\sqrt{2 a x-x^{2}}$ when $a>0$.

### 3.8 DIFFERENTIAL EQUATIONS

An equation containing at least one derivative of a dependent, variable with respect to an independent variable such as

$$
y \frac{d y}{d x}+2 x=0
$$

$$
\text { or } \quad \frac{x d^{2} y}{d x^{2}}+\frac{d y}{d x}-2 x=0
$$

is called a differential equation.
Derivatives may be of first or higher orders. A differential equation containing only derivative of first order can be written in terms of differentials. So we can write the equation (i) as $y d y+2 x d x=0$ but the equation (ii) cannot be written in terms of differentials.

Order: The order of a differential equation is the order of the highest derivative in the equation. As the order of the equation (i) is one so it is called a first order differential equation. But equation (ii) contains the second order derivative and is called a second order differential equation.

### 3.8.1 Solution of a Differential Equation of first order:

$$
\begin{aligned}
& \text { Consider the equation } \\
& y=A x^{2}+4 \\
& \text { where } A \text { is a real constant } \\
& \text { Differentiating (iii) with respect to } x \text { gives } \\
& \qquad \frac{d y}{d x}=2 A x \\
& \text { (iv) }
\end{aligned}
$$

From (iii) $A=\frac{y-4}{x^{2}}$, so putting the value of $A$ in (iv), we get

$$
\begin{aligned}
& \frac{d y}{d x}=2\left(\frac{y-4}{x^{2}}\right) x \\
\Rightarrow \quad & x \frac{d y}{d x}=2 y-8 \text { which is free of constant } A \\
\Rightarrow \quad & 2 y-x \frac{d y}{d x}=8
\end{aligned}
$$

Substituting the value of $y$ and its derivative in (v), we see that it is satisfied, that is.
$2\left(A x^{2}+4\right)-x(2 A x)=2 A x^{2}+8-2 A x^{2}=8$
which shows that (iii) is asolution of (v)
Giving a particular value to $A$. say $A=-1$. we get

$$
y=-x^{2}+4
$$

We see that (v) is satisfied if we put $y=-x^{2}+4$ and $\frac{d y}{d x}=-2 x$, so $y=-x^{2}+4$ is also a solution of (v).

For different values of $A$, (iii) represents different parabolas with vertex at $(0,4)$ and the axis along the $y$-axis. We have drawn two members of the family of parabolas.

$$
y=A x^{2}+4 \quad \text { for } \quad A=-1,1
$$

All solutions obtained from (iii) by putting different values of $A$, are called particular solutions of (v) while the solution (iii) itself is called the general solution of (v).

A solution of differential equation is a relation between the variables (not involving derivatives) which satisfies the differential equation.

Here we shall solve differential equations of first order with variables separable in the forms

$$
\frac{d y}{d x}=\frac{f(x)}{g(y)} \quad \text { or } \quad \frac{d y}{d x}=\frac{g(y)}{f(x)}
$$

Example 1: Solve the differential equation $(x-1) d x+y d y=0$
Solution: Variables in the given equation are in separable form, so integrating either terms, we have

$$
\begin{gathered}
\int(x-1) d x+\int y d y=c_{1}, \quad \text { where } c_{1} \text { is a constant } \\
\text { or }\left(\frac{x^{2}}{2}-x\right)+\frac{y^{2}}{2}=c_{1}, \quad \text { which gives }
\end{gathered}
$$

Thus the required general solution is $x^{2}+y^{2}-2 x=c, \quad$ where $c=2 c_{1}$
Example 2: Solve differential equation

$$
x^{2}(2 y+1) \frac{d y}{d x}-1=0
$$

Solution: The given differential equation can be written as

$$
x^{2}(2 y+1) \frac{d y}{d x}=1
$$

Dividing by $x^{2}$, we have $(2 y+1) \frac{d y}{d x}=\frac{1}{x^{2}}, \quad(x \neq 0)$
Multiplying both sides of (i) by $d x$, we get

$$
(2 y+1)\left(\frac{d y}{d x} d x\right)=\frac{1}{x^{2}} d x
$$

or $\quad(2 y+1) d y=\frac{1}{x^{2}} d x \quad\left(\because \frac{d y}{d x} d x=d y\right)$
Integrating either side gives

$$
\int(2 y+1) d y=\int \frac{1}{x^{2}} d x
$$

or $\quad y^{2}+y=-\frac{1}{x}+c \quad\left(\because \int x^{-2} d x=\frac{x^{-1}}{-1}+c\right)$
Thus $y^{2}+y=c-\frac{1}{x}$ is the general solution of the given differential equation.

## Example 3: Solve the differential equation

$$
\frac{1}{x} \frac{d y}{d x}-2 y=0 \quad x \neq 0, y>0
$$

Solution: Multiplying the both sides of the given equation by $\frac{x}{y} d x$, gives

$$
\frac{1}{y}\left(\frac{d y}{d x} d x\right)-2 x d x=0 \quad \text { or } \quad \frac{1}{y} d y \quad 2 x d x \quad\left(\because \frac{d y}{d x} d x \quad d y\right)
$$

Now integrating either side gives $\ln y=x^{2}+c_{1} \quad$ where $c_{1}$ is a constant
or $y=\mathrm{e}^{x^{2}+c_{1}}=\mathrm{e}^{x^{2}} \cdot e^{x_{1}}$
Thus $y=c e^{x^{2}}$ where $\quad e^{c_{1}}=c$
is the required general solution of the given differential equation.
Example 4: $\quad$ Solve $\frac{d y}{d x}=\frac{y^{2}+1}{e^{-x}}$
Solution: Separating the variables, we have

$$
\frac{1}{y^{2}+1} d y=\frac{1}{e^{-x}} d x=e^{x} d x
$$

Now integrating either side gives

$$
\operatorname{Tan}^{-1} y=\mathrm{e}^{x}+\mathrm{c}, \quad \text { where } \mathrm{c} \text { is a constant, }
$$

or $\quad y=\operatorname{Tan}\left(\mathrm{e}^{x}+\mathrm{c}\right)$
which is the general solution of the given differential equation.

$$
\text { version: } 1.1
$$

Example 5: $\quad$ Solve $2 e^{x} \tan y d x+\left(1-e^{x}\right) \sec ^{2} y d y=0\left(\begin{array}{c}0<y<\frac{\pi}{2} \\ \text { or } \pi<y<\frac{3 \pi}{2}\end{array}\right)$
Solution: Given that: $2 e^{x} \tan y d x+\left(1-e^{x}\right) \sec ^{2} y d y=0$
Dividing either term of (i) by $\tan y\left(1-e^{x}\right)$, we get

$$
\begin{aligned}
& \frac{2 e^{x}}{1-e^{x}} d x+\frac{\sec ^{2} y}{\tan y} d y=0 \\
& \text { or } \quad \frac{-2 e^{x}}{e^{x}-1} d x+\frac{\sec ^{2} y}{\tan y} d y=0
\end{aligned}
$$

Integrating, we have

$$
\int-2\left(\frac{e^{x}}{e^{x}-1}\right) d x+\int\left(\frac{\sec ^{2} y}{\tan y}\right) d y=c_{1} \quad\left(e^{x}-1>0\right)
$$

or $\quad-2 \ln \left(e^{x}-1\right)+\ln (\tan y)=c_{1}$
$\Rightarrow \quad \ln \left(e^{x}-1\right)^{-2}+\ln (\tan y)=\ln c, \quad$ where $c_{1}=\ln c$
or $\quad \ln \left[\left(e^{x}-1\right)^{-2} \tan y\right]=\ln c$
$\Rightarrow \quad\left(e^{x}-1\right)^{-2} \tan y=c \quad \Rightarrow \quad \tan y=c\left(e^{x}-1\right)^{2}$.
Example 6: Solve $(\sin y+y \cos y) d y=[x(2 \ln x+1)] d x$
Solution: $(\sin y+y \cos y) d y=(2 x \ln x+x) d x$
(i)

$$
\begin{aligned}
& \text { or } \quad(1 \cdot \sin y+y \cos y) d y=\left(2 x \ln x+x^{2} \cdot \frac{1}{x}\right) d x \\
& \Rightarrow\left(\frac{d}{d y}(y \sin y)\right) d y=\left(\frac{d}{d x}\left(x^{2} \ln x\right)\right) d x\left(\because \frac{d}{d y}(y \sin y)=1 \cdot \sin y \quad y \cos y \text { and }\right. \\
& \left.\frac{d}{d x}\left(x^{2} \ln x\right) 2 x \ln x+x^{2} \cdot \frac{1}{x}\right)
\end{aligned}
$$

Integrating, we have

$$
\int\left(\frac{d}{d y}(y \sin y)\right) d y=+\int\left(\frac{d}{d x}\left(x^{2} \ln x\right)\right) d x
$$

$$
\Rightarrow \quad y \sin y = x^2 \ln x + c
$$

### 3.8.2 Initial Conditions

Differential equations occur in numerous practical problems concerning physical, biological, and social sciences.

The arbitrary constants involving the solution of different equations can be determined by the given conditions. Such conditions are called **initial value conditions**.

The general solution of differential equations in variable separable form contains only one variable. Here we shall consider those differential equations which have only one initial value condition.

Note that the general solution of differential equations of order *n* contains *n* arbitrary constants which can be determined by *n* initial value conditions.

**Example 1:** The slope of the tangent at any point of the curve is given by

$$
\frac{dy}{dx} = 2x - 2, \text{ find the equation of the curve if } y = 0 \text{ when } x = -1.
$$

**Solution:** Given that

$$
\frac{dy}{dx} = 2x - 2
$$

(i)

Equation (i) can be written as

$$
\frac{dy}{dx} = \frac{(2x - 2)dx}{(2x - 2)dx}
$$

(ii)

Integrating either side of (ii) gives

$$
\frac{dy}{dx} = \frac{(2x - 2)dx}{(2x - 2)dx}
$$

or

$$
\frac{y}{x^2} = \frac{x^2 - 2x + c}{(2x - 1) + c}
$$

(iii)

Applying the given condition, we have

$$
0 = (-1)^2 - 2(-1) + c \Rightarrow c = -3
$$

Thus (iii) becomes

$$
\frac{y}{x^2} = 2x - 3
$$

which represents a parabola as shown in the adjoining figure.

For *c* = 0, (iii) becomes

$$
y = x^2 - 2x
$$

The graph of

$$
y = x^2 - 2x
$$

is also shown in the figure.

**Note:** The general solution represents a system of parabolas which are vertically above or below each other.

**Example 2:** Solve

$$
\frac{dy}{dx} = \frac{3}{4}x^4 + x - 3, \text{ if } y = 0 \text{ when } x = 2
$$

**Solution:** Given that

$$
\frac{dy}{dx} = \frac{3}{4}x^2 + x - 3
$$

(i)

Separating variables, we have

$$
dy = \frac{3}{4}x^2 + x - 3
$$

(ii)

Integrating either side of (ii) gives

$$
\frac{dy}{dx} = \frac{3}{4}x^2 + x - 3
$$

or

$$
\frac{y}{x^2} = \frac{3}{4}x^2 + \frac{x^2}{2} - 3x + c
$$

(iii)

Now applying the initial value condition, we have

$$
0 = \frac{1}{4}(8) + \frac{1}{2}(4) - 3(2) + c
$$

$$
\Rightarrow \quad c = 6 - 2 - 2 = 2
$$

Thus (iii) becomes

$$
\frac{y}{x^2} = \frac{1}{4}x^2 + \frac{1}{2}x^2 - 3x + 2
$$

$$
\Rightarrow \quad 4y = x^2 + 2x^2 - 12x + 8
$$

**Example 3:** A particle is moving in a straight line and its acceleration is given by

$$
a = 2t - 7
$$

(i) Find *v* (velocity) in terms of *t* if *v* = 10 m/sec, when *t* = 0

(ii) Find *s* (distance) in terms of *t* if *s* = 0, when *t* = 0.

Solution: Given that $a=2 t-7$, that is

$$
\begin{aligned}
& \frac{d v}{d t}=2 t \quad 7=\left(\because a \quad \frac{d v}{d t}\right) \\
\Rightarrow & d v=(2 t-7) d t
\end{aligned}
$$

Integrating, we have

$$
\begin{aligned}
& \int d v=\int(2 t-7) d t \\
\Rightarrow & v=t^{2}-7 t+c_{1}
\end{aligned}
$$

Applying the first initial value condition, we get

$$
10=0-0+c_{1} \quad \Rightarrow \quad c_{1}=10
$$

The equation (1) becomes

$$
v=t^{2}-7 t+10 \quad \text { which is the solution of (i) }
$$

Now $\frac{d s}{d t}=t^{3}-7 t+10 \quad\left(\because v=\frac{d s}{d t}\right)$
$\Rightarrow \quad d s=\left(t^{2}-7 t+10\right) d t$
Integrating both sides of (2), we get

$$
\begin{aligned}
& \int d s=\int\left(t^{3}-7 t+10\right) d t \\
\Rightarrow & s=\frac{t^{3}}{3}-7 \frac{t^{2}}{2}+10 t+c_{2}
\end{aligned}
$$

Applying the second initial value condition, gives

$$
0=0-0+0+c_{2} \quad \Rightarrow c_{2}=0
$$

Thus is $\quad s=\frac{1}{3} t^{3}-\frac{7}{2} t^{2}+10 t \quad$ the solution of (ii)
Example 4: In a culture, bacteria increases at the rate proportional to the number of bacteria present. If bacteria are 100 initially and are doubled in 2 hours, find the number of bacteria present four hours later.

Solution: Let $p$ be the number of bacteria present at time $t$, then

$$
\frac{d p}{d t} \Rightarrow k p, \quad(k \quad 0)
$$

$$
\begin{aligned}
& \text { or } \quad \frac{1}{p} d p=k d t \quad \Rightarrow \ln p=k t+c_{1} \\
& \Rightarrow \quad p=e^{k t+c_{1}}=e^{k t} \cdot e^{c_{1}} \\
& \text { or } p \Rightarrow c e^{k t} \quad \text { (i) (where } e^{c_{1}} \quad c \text { ) }
\end{aligned}
$$

Applying the given condition, that is $p=100$ when $t=0$, we have

$$
100=c e^{100}=c \quad\left(\because e^{0}=1\right)
$$

Putting $c=100$, (i) becomes $p=100 e^{k t}$
$p$ will be 200 when $t=2$ (hours), so (ii) gives

$$
200=100 e^{2 k} \quad \Rightarrow \quad e^{2 k}=2
$$

or $2 k=\ln 2 \quad \Rightarrow k=\frac{1}{2} \ln 2$
Subsituting $\quad=-\ln 2$ in (ii), we get

$$
\begin{aligned}
& p=100 e^{\left(\frac{1}{2} \ln 2\right)} \quad \Rightarrow 100 e^{\frac{1}{2} \ln 2} \quad 100 e^{\ln \left(2^{\frac{1}{2}}\right)} \\
& p=100\left(2^{\frac{1}{2}}\right)
\end{aligned}
$$

If $t=4$ (hours), then $p=100\left(2^{\frac{4}{2}}\right)=100 \quad 4 \quad 400$.
Example 5: A ball is thrown vertically upward with a velocity of $1470 \mathrm{~cm} / \mathrm{sec}$ Neglecting air resistance, find
(i) velocity of ball at any time $t$
(ii) distance traveled in any time $t$
(iii) maximum height attained by the ball.

## Solution.

(i) Let $v$ be the velocity of the ball at any time $t$, then by Newton's law of motion, we have

$$
\begin{aligned}
& \frac{d v}{d t} \Rightarrow g \Rightarrow \quad \Rightarrow g d t \\
& \text { or } \quad \int d v=\int-g d t \quad \text { (integrating either side of (i)) } \\
& v=-g t+c_{1}
\end{aligned}
$$

Given that $v=1470(\mathrm{~cm} / \mathrm{sec})$ when $t=0$, so

$$
1470=-g(0)+c_{1} \Rightarrow c_{1}=1470
$$

Thus (ii) becomes $v=-g t+1470=1470-980 t$ (taking $g=980$ )
(ii) Let $h$ be the height of the ball at any time $t$, then

$$
\frac{d h}{d t}=1470-980 t \quad\left(\because v=\frac{d h}{d t}\right)
$$

or $\quad d h=(1470-980 t) d t$

$$
h=1470 t-980 \frac{t^{2}}{2}+c_{2}=1470 t-490 t^{2}+c_{2}
$$

$h=0$ when $t=0$, so we have

$$
0=1470 \times 0-490(0)^{2}+c_{2} \Rightarrow c_{2}=0
$$

Putting $c_{2}=0$ in (iii), we have

$$
h=1470 t-490 t^{2}
$$

(iii) The maximum height will be attained when $v=0$, that is

$$
1470-980 t=0 \quad \Rightarrow t=\frac{1470}{980}=\frac{3}{2}(\sec )
$$

Thus the maximum height attained in (cms) $=1470 \times\left(\frac{3}{2}\right)-490 \times\left(\frac{3}{2}\right)^{2}$

$$
=2205-1102.5=1102.5
$$

## EXERCISE 3.8

1. Check that each of the following equations written against the differential equation is its solution.
(i) $x \frac{d y}{d x}=1+y$
(ii) $x^{2}(2 y+1) \frac{d y}{d x}-1=0$
(iii) $y \frac{d y}{d x}-e^{2 x}=1$
(iv) $\frac{1}{x} \frac{d y}{d x}-2 y=0$
(v) $\frac{d y}{d x}=\frac{x^{2}+1}{e^{-x}}$
$\begin{array}{ll}\text { , } & y=c x-1 \\ \text {, } & y^{2}+y=c-\frac{1}{x} \\ & y^{2}=e^{2 x}+2 x+c \\ & y=c e^{x^{2}}\end{array}$
$\begin{array}{ll}\text {, } & y=\tan \left(e^{x}+c\right) \\ \text {, } & y=\tan \left(e^{x}+c\right)\end{array}$

Solve the following differential equations:
2. $\frac{d y}{d x}=-y$
3. $y d x+x d y=0$
4. $\frac{d y}{d x}=\frac{1-x}{y}$
5. $\frac{d y}{d x}=\frac{y}{x^{2}}:(y>0)$
6. $\sin y \cos \sec x \frac{d y}{d x}=1$
7. $x d y+y(x-1) d x=0$
8. $\frac{x^{2}+1}{y+1} \Rightarrow \frac{x}{y} \frac{d y}{d x} \cdot(x, y \quad 0)$
9. $\frac{1}{x} \frac{d y}{d x}=\frac{1}{2}\left(1+y^{2}\right)$
10. $2 x^{2} y \frac{d y}{d x}=x^{2}-1$
11. $\frac{d y}{d x}+\frac{2 x y}{2 y+1}=x$
12. $\left(x^{2}-y x^{2}\right) \frac{d y}{d x}+y^{2}+x y^{2}=0$
13. $\sec ^{2} x \tan y d x+\sec ^{2} y \tan x d y=0$
14. $\left(y-x \frac{d y}{d x}\right)=2\left(y^{2}+\frac{d y}{d x}\right)$
15. $1+\cos x \tan y \frac{d y}{d x}=0$
16. $y-x \frac{d y}{d x}=3\left(1+x \frac{d y}{d x}\right)$
17. $\sec x+\tan y \frac{d y}{d x}=0$
18. $\left(e^{x}+e^{-x}\right) \frac{d y}{d x}=e^{x} \quad e^{-x}$
19. Find the general solution of the equation $\frac{d y}{d x}-x=x y^{2}$ Also find the particular solution if $y=1$ when $x=0$.
20. Solve the differential equation $\frac{d y}{d t}=2 x$ given that $x=4$ when $t=0$.
21. Solve the differential equation $\frac{d x}{d t}+2 x t=0$. Also find the particular solution if $s=4 e$, when $t=0$.
22. In, a culture, bacteria increases at the rate proportional to the number of bacteria present. If bacteria are 200 initially and are doubled in 2 hours, find the number of bacteria present four hours later.
23. A ball is thrown vertically upward with a velocity of $2450 \mathrm{~cm} / \mathrm{sec}$. Neglecting air resistance, find
(i) velocity of ball at any time $t$
(ii) distance traveled in any time $t$
(iii) maximum height attained by the ball.

# CHAPTER

## 4

## Introduction to Analytic Geometry

## 4.1 INTRODUCTION

Geometry is one of the most ancient branches of mathematics. The Greeks systematically studied it about four centuries B.C. Most of the geometry taught in schools is due to Euclid who expounded thirteen books on the subject ( 300 B.C.). A French philosopher and $m$ athematician Rene Descartes (1596-1650 A.D.) introduced algebraic methods in geometry which gave birth to analytical geometry (or coordinate geometry). Our aim is to present fundamentals of the subject in this book.

## Coordinate System

Draw in a plane two mutually perpendicular number lines $x^{\prime} x$ and $y^{\prime} y$, one horizontal and the other vertical. Let their point of intersection be $O$, to which we call the origin and the real number 0 of both the lines is represented by $O$. The two lines are called the coordinate axes. The horizontal line $x^{\prime} O x$ is called the $\boldsymbol{x}$-axis and the vertical line $y^{\prime} O y$ is called the $\boldsymbol{y}$-axis.

As in the case of number line, we follow the convention that all points on the $y$-axis above $x^{\prime} O x$ are associated with positive real numbers, those below $x^{\prime} O x$ with negative real numbers. Similarly, all points on the $x$-axis and lying on the right of $O$ will be positive and those on the left of $O$ and lying on the $x$-axis will be negative.

Suppose $P$ is any point in the plane. Then $\boldsymbol{P}$ can be located by using an ordered pair of real numbers. Through $P$ draw lines parallel to the coordinates axes meeting $x$-axis at $R$ and $y$-axis at $S$.
Let the directed distance $\overline{O R}=x$ and the directed distance $\overline{O S}=y$.
The ordered pair $(x, y)$ gives us enough information to locate the point $P$. Thus, with every point $P$ in the plane, we can associate an ordered pair of real numbers $(x, y)$ and we say
version: 1.1
that $P$ has coordinates $(x, y)$. It may be noted that $x$ and $y$ are the directed distances of $P$ from the $y$-axis and the $x$-axis respectively. The reverse of this technique also provides method for associating exactly one point in the plane with any ordered pair $(x, y)$ of real numbers. This method of pairing off in a one-to-one fashion the points in a plane with ordered pairs of real numbers is called the two dimensional rectangular (or Cartesian) coordinate system.

If $(x, y)$ are the coordinates of a point $P$, then the first member (component) of the ordered pair is called the $\boldsymbol{x}$-coordinate or abscissa of $P$ and the second member of the ordered pair is called the $\boldsymbol{y}$-coordinate or ordinate of $P$. Note that abscissa is always first element and the ordinate is second element in an ordered pair.
The coordinate axes divide the plane into four equal parts called quadrants. They are defined as follows:

Quadrant I: All points $(x, y)$ with $x>0, y>0$
Quadrant II: All points $(x, y)$ with $x<0, y>0$
Quadrant III: All points $(x, y)$ with $x<0, y<0$
Quadrant IV: All points $(x, y)$ with $x>0, y<0$
The point $P$ in the plane that corresponds to an ordered pair $(x, y)$ is called the graph of $(x, y)$.
Thus given a set of ordered pairs of real numbers, the graph of the set is the aggregate of all points in the plane that correspond to ordered pairs of the set.

## i- Write down the coordinates of the points if not mentioned.
ii- Locate $(0,-1),(2,2),(-4,7)$ and $(-3,-3)$.

#### 4.1.1 The Distance Formula

Let *A* (*x*<sub>1</sub>, *y*<sub>1</sub>) and *B* (*x*<sub>2</sub>, *y*<sub>2</sub>) be two points in the plane. We can find the distance *d* = |*AB*| from the right triangle *AQB* by using the Pythagorean theorem. We have

$$
d = AB = AQ + QB^2 \tag{1}
$$

|*AQ*| = |*BS*| = |*BO* + *OS*|

|*OR* | *OS*|

|*SB*| = |*SB* - *SQ*|

|*y*<sub>1</sub> | *y*<sub>1</sub> | | || || | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |

or

$$
x = \frac{k_1 v_1 + k_2 v_2}{k_1 + k_2}
$$

Similarly, by drawing perpendiculars from *A*, *B* and *P* to the *y*-axis and proceeding as before, we can show that

$$
y = \frac{k_1 v_1 + k_2 v_2}{k_1 + k_2}
$$

#### **Note:**

(i) If the directed distances *AP* and *PB* have the same sign, then their ratio is positive and *P* is said to divide *AB* internally.

(ii) If the directed distances *AP* and *PB* have opposite signs i.e., *P* is beyond *AB*, then their ratio is negative and *P* is said to divide *AB* **externally**.

$$
\frac{AP}{BP} = \frac{k_1}{k_2} \quad \text{or} \quad \frac{AP}{PB} = \frac{k_2}{k_2}
$$

Proceeding as before, we can show in this case that

$$
x = \frac{k_1 v_1 - k_2 v_2}{k_1 - k_2} \quad \text{y} \quad \frac{k_1 v_2 - k_2 v_2}{k_1 - k_2}
$$

Thus *P* is said to divide the line segment *AB* in ratio *k₁*, *k₂*, **internally** or **externally** according as *P* lies between *AB* or beyond *AB*.

(iii) If *k₁* = *k₂* = 1:1, then *P* becomes **midpoint** of *AB* and coordinates of *P* are

$$
x = \frac{x_1 + x_2}{2}, \quad \text{y} \quad \frac{y_1 - y_2}{2}
$$

(iv) The above theorem is valid in whichever quadrant *A* and *B* lie.

**Example 1:** Find the coordinates of the point that divides the join of *A* (−6, 3) and *B* (5, −2) in the ratio 2 : 3.

(i) internally

(ii) externally

**Solution:** (i) Here *k₁* = 2, *k₂* = 3, *x₁* = 6, *x₂* = 5.

By the formula, we have

$$
x = \frac{2 \times 5 + 3 \times (-6)}{2 + 3} \quad \text{or} \quad \frac{-6}{5} \quad \text{and} \quad y = \frac{2(-2) + 3(3)}{2 + 3} \quad 1
$$

Coordinates of the required point are (−8, 5, 1)

(ii) In this case

$$
x = \frac{2 \times 5 - 3 \times (-6)}{2 - 3} \quad \text{or} \quad y = \frac{2(-2) - 3(3)}{2 + 3} \quad 13
$$

Thus the required point has coordinates (−28, 13)

#### **Theorem:**

The centroid of a *ΔABC* is a point that divides each median in the ratio 2 : 1. Using this show that medians of a triangle are concurrent.

**Proof:** Let the vertices of a *ΔABC* have coordinates as shown in the figure.

Midpoint of *BC* is *D* (x, y, z, x + y, z).

Let *G* (x, y) be the centroid of the *Δ*. Then *G* divides *AD* in the ratio 2 : 1. Therefore

$$
\frac{2 \cdot \frac{x_1 + x_2}{2}}{2 + 1} \quad \text{or} \quad \frac{x_1 + x_2 + x_3}{2 + 1}
$$

Similarly,

$$
y = \frac{y_1 + y_2 + y_3}{2 + 1} \quad \text{or} \quad \frac{y_1 + y_2 + y_3}{2 + 1}
$$

In the same way, we can show that coordinate of the point that divides *BE* and *CF* each in the ratio 2 : 1 are (x, y, z, x + y, z).

Thus (x, y) lies on each median and so the medians of the *ΔABC* are concurrent.

**Theorem:** Bisectors of angles of a triangle are concurrent.

**Proof:** Let the coordinates of the vertices of a triangle be as shown in the figure.

Suppose |*BC*| = *a*, |*CA*| = *b* and |*AB*| = *c*.

Let the bisector of *LA* meet *BC* at *D*. Then *D* divides *BC* in the ratio *c* : *b*. Therefore

coordinates of $D$ are $\left(\frac{c x_{1}+b x_{2}}{b+c} \cdot \frac{c y_{1}+b y_{2}}{b+c}\right)$
The bisector of $\angle B$ meets $A C$ at $I$ and $I$ divides $A D$ in the ratio $c:|B D|$
Now $\frac{|B D|}{|D C|}=\frac{c}{b}$ or $\frac{|D C|}{|B D|} \cdot \frac{b}{c}$
or $\frac{|D C|+|B D|}{|B D|}=\frac{b+c}{c}$
or $\frac{a}{|B D|}=\frac{b+c}{c}$ or $|B D| \cdot \frac{a c}{b+c}$
Thus $I$ divides $A D$ in the ratio $c: \frac{a c}{b+c}$ or in the ratio $b+c: a$ Coordinates of $I$ are

$$
\left(\frac{(b+c) \frac{b x_{2}+c x_{1}}{b+c}+a x_{1}}{a+b+c} \cdot \frac{(b+c) \frac{b y_{2}+c y_{1}}{b+c}+a y_{1}}{a+b+c}\right)
$$

i.e., $\quad\left(\frac{a x_{1}+b x_{2}+c x_{1}}{a+b+c} \cdot \frac{a y_{1}+b y_{2}+c y_{2}}{a+b+c}\right)$

The symmetry of these coordinates shows that the bisector of $\angle C$ will also pass through this point.

Thus the angle bisectors of a triangle are concurrent.

## EXERCISE 4.1

1. Describe the location in the plane of the point $P(x, y)$ for which
(i) $x>0$
(ii) $x>0$ and $y>0$
(iii) $x=0$
(iv) $y=0$
(v) $x<0$ and $y \geq 0$
(vi) $x=y$
(vii) $|x|=|y|$
(viii) $|x| \geq 3$
(ix) $x>2$ and $y=2$
(x) $x$ and $y$ have opposite signs.
version: 1.1
2. Find in each of the following:
(i) the distance between the two given points
(ii) midpoint of the line segment joining the two points
(a) $A(3,1) ; B(-2,-4)$
(b) $A(-8,3) ; B(2,-1)$
(c) $A\left(-\sqrt{5},-\frac{1}{3}\right) ; B(-3 \sqrt{5}, 5)$
3. Which of the following points are at a distance of 15 units from the origin?
(a) $(\sqrt{176}, 7)$
(b) $(10,-10)$
(c) $(1,15)$
(d) $\left(\frac{15}{2}, \frac{15}{2}\right)$
4. Show that
(i) the points $A(0,2), B(\sqrt{3}, 1)$ and $C(0,-2)$ are vertices of a right triangle.
(ii) the points $A(3,1), B(-2,-3)$ and $C(2,2)$ are vertices of an isosceles triangle.
(iii) the points $A(5,2), B(-2,3), C(-3,-4)$ and $D(4,-5)$ are vertices of a parallelogram. Is the parallelogram a square?
5. The midpoints of the sides of a triangle are $(1,-1),(-4,-3)$ and $(-1,1)$. Find coordinates of the vertices of the triangle.
6. Find $h$ such that the points $A(\sqrt{3},-1), B(0,2)$ and $C(h,-2)$ are vertices of a right triangle with right angle at the vertex $A$.
7. Find $h$ such that $A(-1, k), B(3,2)$ and $C(7,3)$ are collinear.
8. The points $A(-5,-2)$ and $B(5,-4)$ are ends of a diameter of a circle. Find the centre and radius of the circle.
9. Find $k$ such that the points $A(k, 1), B(2,7)$ and $C(-6,-7)$ are vertices of a right triangle with right angle at the vertex $A$.
10. A quadrilateral has the points $A(9,3), B(-7,7), C(-3,-7)$ and $D(5,-5)$ as its vertices. Find the midpoints of its sides. Show that the figure formed by joining the midpoints consecutively is a parallelogram.

11. Find *h* such that the quadrilateral with vertices *A* (–3, 0), *B* (1, –2), *C* (5, 0) and *D* (1, *h*) is parallelogram. Is it a square?
12. If two vertices of an equilateral triangle are *A* (–3, 0) and *B* (3, 0), find the third vertex. How many of these triangles are possible?
13. Find the points trisecting the join of *A* (–1, 4) and *B* (6, 2).
14. Find the point three-fifth of the way along the line segment from *A* (–5, 8) to *B* (5, 3).
15. Find the point *P* on the join of *A* (1, 4) and *B* (5, 6) that is twice as far from *A* as *B* is from *A* and lies
    - (i) on the same side of *A* as *B* does.
    - (ii) on the opposite side of *A* as *B* does.
16. Find the point which is equidistant from the points *A* (5, 3), *B* (–2, 2) and *C* (4, 2). What is the radius of the circumcircle of the ∆ABC?
17. The points (4, –2), (–2, 4) and (5, 5) are the vertices of a triangle. Find in-centre of the triangle.
18. Find the points that divide the line segment joining *A*(*x*<sub>*1*</sub>, *y*<sub>*1*</sub>) and *B*(*x*<sub>*2*</sub>, *y*<sub>*2*</sub>) into four equal parts.

## 4.2 TRANSLATION AND ROTATION OF AXES

### *Translation of Axes*

Let *xy*-coordinate system be given and *O'* (*h, k*) be any point in the plane. Through *O'* draw two mutually perpendicular lines *OX*, *OY* such that *OX* is parallel to *Ox*. The new axes *OX* and *OY* are called **translations** of the *Ox* – and *Oy* – axes through the point *O'*. In translation of axes, origin is shifted to another point in the plane but the axes remain parallel to the old axes.

Let *P* be a point with coordinates (*x, y*) referred to *xy*-coordinate system and the axes be translated through the point *O'*(*h, k*) and *OX*, *OY* be the new axes. If *P* has coordinates (*X, Y*) referred to the new axes, then we need to find *X, Y* in terms of *x, y*.

Draw *PM* and *O' N* perpendiculars to *Ox*. From the figure, we have

*OM* = *x*, *MP* = *y*, *ON* = *h*, *NO'* = *k* = *MM*<sup>+</sup>

Now *X* = *O'M'* = *NM* = *OM* – *OM* – *ON* = *x* – *h*

Similarly, *Y* = *M'P* = *MP* – *MM'* = *y* *k*

Thus the coordinates of *P* referred to *XY*-system are (*x* – *h*, *y* – *k*)

i.e. *X* = *x* – *h*

*Y* = *y* – *k*

Moreover, *x* = *X* + *h*, + *y* = *Y* *k*.

**Example 1:** The coordinates of a point *P* are (–6, 9). The axes are translated through the point *O'* (–3, 2). Find the coordinates of *P* referred to the new axes.

**Solution.** Here *h* = 3*x* *k* 2

Coordinates of *P* referred to the new axes are (*X, Y*) given by

*X* = –6 – (–3) = –3 and *Y* = 9 – 2 = 7

Thus *P* (*X, Y*) = *P* (–3, 7).

**Example 2:** The *xy*-coordinate axes are translated through the point *O'* (4, 6). The coordinates of the point *P* are (2, –3) referred to the new axes. Find the coordinates of *P* referred to the original axes.

**Solution:** Here *X* = –2, *Y* = 3, *h* = 4, *k* = 6.

We have *x* = *X* + *h* = 4 + 2 = 6

*y* = *Y* + *k* = –3 + 6 = 3

Thus required coordinates are *P* (6, 3).

### *Rotation of Axes*

Let *xy*-coordinate system be given. We rotate *Ox* and *Oy* about the origin through an angle *θ*(0 < *θ* < 90˚) so that the new axes are *OX* and *OY* as shown in the figure. Let a point *P* have coordinates (*x, y*) referred to the *xy*-system of

coordinates. Suppose $P$ has coordinates $(X, Y)$ referred to the $X Y$-coordinate system. We have to find $X, Y$ in terms of the given coordinates $x, y$. Let $\alpha$ be measure of the angle that $O P$ makes with $O$.

From $P$, draw $P M$ perpendicular to $O x$ and $P M^{\prime}$ perpendicular to $O X$. Let $|O P|=r$. From the right triangle $O P M^{\prime}$, we have

$$
\left.\begin{array}{l}
O M^{\prime}=X=r \cos (\alpha-\theta) \\
M^{\prime} P=Y=r \sin (\alpha-\theta)
\end{array}\right]
$$

Also from the $\triangle O P M$, we have

$$
x=r \cos \alpha, \quad y=r \sin \alpha
$$

System of equations (1) may be re-written as:

$$
\left.\begin{array}{l}
X=r \cos \alpha \cos \theta \quad r \sin \alpha \sin \theta \\
Y=r \sin \alpha \cos \theta \quad r \cos \alpha \sin \theta
\end{array}\right\}
$$

Substituting from (2) into the above equations, we have

$$
\left.\begin{array}{l}
X=x \cos \theta+y \sin \theta \\
Y=y \cos \theta-x \sin \theta
\end{array}\right\}
$$

i.e., $(X, Y)=(x \cos \theta \quad y \sin \theta, \min \theta \quad y \cos \theta)$
are the coordinates of $P$ referred to the new axes $O X$ and $O Y$.
Example 3: The $x y$-coordinate axes are rotated about the origin through an angle of $30^{\circ}$. If the $x y$-coordinates of a point are $(5,7)$, find its $X Y$-coordinates, where $O X$ and $O Y$ are the axes obtained after rotation.

Solution. Let $(X, Y)$ be the coordinates of $P$ referred to the $X Y$-axes. Here $\theta=30^{\circ}$.
From equations (3) above, we have

$$
\begin{aligned}
& X=5 \cos 30^{\circ}+7 \sin 30^{\circ} \text { and } \quad \forall=5 \sin 30^{\circ} 7 \cos 30^{\circ} \\
\text { or } & X=\frac{5 \sqrt{3}}{2}, \frac{7}{2}=\text { and } \quad Y=\frac{-5}{2}, \frac{7 \sqrt{3}}{2}
\end{aligned}
$$

i.e., $(X, Y) \quad\left(\frac{5 \sqrt{3}+7}{2}, \frac{-5+7 \sqrt{3}}{2}\right)$
are the required coordinates.

Example 4: $\quad$ The $x y$-axes are rotated about the origin through an angle of arctan $\frac{4}{3}$ lying in the first quadrant. The coordinates of a point $P$ referred to the new axes $O X$ and $O Y$ are $P(-1,-7)$. Find the coordinates of $P$ referred to the $x y$-coordinate system.

Solution. Let $P(x, y)$ be the coordinates of $P$ referred to the $x y$-coordinate system. Angle of rotation is given by arctan $\theta=\frac{4}{3}$. Therefore, $\sin \theta=\frac{4}{5}, \cos \theta=\frac{3}{5}$.

From equations (3) above, we have

$$
\begin{aligned}
& X=x \cos \theta+y \sin \theta \text { and } \quad \forall=x \sin \theta \quad y \cos \theta \\
\text { or } & -1=\frac{3}{5} x+\frac{4}{5} y \text { and }-7=-\frac{4}{5} x+\frac{3}{5} y \\
\text { or } & 3 x+4 y+5=0 \text { and }-4 x+3 y+35=0
\end{aligned}
$$

Solving these equations, we have

$$
\frac{x}{125}=-\frac{y}{-125}=\frac{1}{25} \quad \Rightarrow x=5, y=-5
$$

Thus coordinates of $P$ referred to the $x y$-system are $(5,-5)$.

## EXERCISE 4.2

1. The two points $P$ and $O^{\prime}$ are given in $x y$-coordinate system. Find the $X Y$-coordinates of $P$ reffered to the translated axes $O^{\prime} X$ and $O^{\prime} Y$.
(i) $P(3,2) ; O^{\prime}(1,3)$
(ii) $P(-2,6) ; O^{\prime}(-3,2)$
(iii) $P(-6,-8) ; O^{\prime}(-4,-6)$
(iv) $P\left(\frac{3}{2}, \frac{5}{2}\right) ; O^{\prime}\left(-\frac{1}{2}, \frac{7}{2}\right)$

2. The $x y$-coordinate axes are translated through the point whose coordinates are given in $x y$-coordinate system. The coordinates of $P$ are given in the $X Y$-coordinate system. Find the coordinates of $P$ in $x y$-coordinate system.
(i) $P(8,10) ; O^{\prime}(3,4)$
(ii) $P(-5,-3) ; O^{\prime}(-2,-6)$
(iii) $P\left(-\frac{3}{4},-\frac{7}{6}\right) ; O^{\prime}\left(\frac{1}{4},-\frac{1}{6}\right)$
(iv) $P(4,-3) ; O^{\prime}(-2,3)$
3. The $x y$-coordinate axes are rotated about the origin through the indicated angle. The new axes are $O X$ and $O Y$. Find the $X Y$-coordinates of the point $P$ with the given $x y$-coordinates.
(i) $P(5,3) ; \theta=45^{\circ}$
(ii) $P(3,-7) ; \quad \theta=30^{\circ}$
(iii) $P(11,-15) ; \theta=60^{\circ}$
(iv) $P(15,10): \theta=\arctan \frac{1}{3}$
4. The $x y$-coordinate axes are rotated about the origin through the indicated angle and the new axes are $O X$ and $O Y$.
Find the $x y$-coordinates of $P$ with the given $X Y$-coordinates.
(i) $P(-5,3) ; \quad \theta=30^{\circ}$
(ii) $P(-7 \sqrt{2}, 5 \sqrt{2}) ; \theta=45^{\circ}$

### 4.3 EQUATIONS OF STRAIGHT LINES

Inclination of a Line: The angle $\alpha\left(0^{\circ}<\alpha<180^{\circ}\right)$ measured counterclockwise from positive $x$-axis to a non-horizontal straight line $l$ is called the inclination of $l$.
Observe that the angle $\alpha$ in the different positions of the line $l$ is $\alpha_{1} 0^{\circ}$ and $90^{\circ}$ respectively.

## (i) If $l$ is parallel to $x$-axis, then $\alpha=0^{\circ}$
(ii) If $l$ is parallel to $y$-axis, then $\alpha=90^{\circ}$

Slope or gradient of a line: When we walk on an inclined plane, we cover horizontal distance (run) as well as vertical distance (rise) at the same time.
It is harder to climb a steeper inclined plane. The measure of steepness (ratio of rise to the run) is termed as slope or gradient of the inclined path and is denoted by $m$.
$$
m=\frac{r i s e}{r u n}=\frac{y}{x}=\tan \alpha
$$

In analytical geometry, slope or gradient $\boldsymbol{m}$ of a non-vertical straight line with $\alpha$ as its inclination is defined by: $m: \tan \alpha$

If $l$ is horizontal its slope is zero and if $l$ is vertical then its slope is undefined.
If $0<\alpha<90^{\circ}, \mathrm{m}$ is positive and if $90^{\circ}<\alpha<180^{\circ}$, then $m$ is negative

### 4.3.1 Slope or Gradient of a Straight Line Joining Two Points

If a non-vertical line $l$ with inclination $\alpha$ passes through two points $P\left(x_{1}, y_{1}\right)$ and $Q\left(x_{1}, y_{1}\right)$, then the slope or gradient $m$ of $l$ is given by $m=\frac{y_{1}-y_{1}}{x_{1}-x_{1}}=\tan \alpha$
Proof: Let $m$ be the slope of the line $l$.
Draw perpendiculars $P M$ and $Q M^{\prime}$ on $x$-axis and a perpendicular $P R$ on $Q M^{\prime}$
Then $\angle R P Q=\alpha, m \overline{P R}=x_{1}-x_{1}$ and $m \overline{Q R}=y_{1}-y_{1}$
The slope or gradient of $l$ is defined as: $m=\tan \alpha=\frac{y_{1}-y_{1}}{x_{1}-x_{1}}$

**Case (i).** When 0 < α < π/2

In the right triangle *PRQ*, we have

$$
m = \tan \alpha = \frac{y_2 - y_1}{x_2 - x_1}
$$

**Case (ii)** When π/2 < α < π

In the right triangle *PRQ*

$$
\tan (\pi - \alpha) = \frac{y_2 - y_1}{x_2 - x_1}
$$

or

$$
-\tan \alpha = \frac{y_2 - y_1}{x_2 - x_1}
$$

or

$$
\tan \alpha = \frac{y_2 - y_1}{x_2 - x_1}
$$

or

$$
m = \frac{y_2 - y_1}{x_2 - x_1}
$$

Thus if *P(x1, y1)* and *Q(x2, y2)* are two points on a line, then slope of *PQ* is given by:

$$
m = \frac{y_2 - y_1}{x_2 - x_1} \quad \text{or} \quad m \quad \frac{y_2 - y_2}{x_2 - x_2}
$$

**Note:**

- (i) $m \neq \frac{y_2 - y_1}{x_2 - x_1}$ and $m \neq \frac{y_2 - y_2}{x_2 - x_1}$.
- (ii) $f$ is horizontal, iff $m = 0$ (∀ α = 0).
- (iii) $f$ is vertical, iff $m$ is not defined (∀ α = 90).
- (iv) If slope of *AB* = slope of *BC*, then the points *A*, *B* and *C* are collinear.

**Theorem:** The two lines *l1* and *l2* with respective slopes *m1* and *m2* are

- (i) parallel iff *m1 = m2*.
- (ii) perpendicular iff *m1 =* 1/*m2*

or

$$
m_1 m_2 + l = 0
$$

**Example 1:** Show that the points *A*(–3, 6), *B*(3, 2) and *C*(6, 0) are collinear.

**Solution:** We know that the points *A*, *B* and *C* are collinear if the line *AB* and *BC* have the same slopes. Here Slope of

$$
AB = \frac{2 - 6}{3 - (-3)} = \frac{-4}{3 + 3} = \frac{-4}{6} = \frac{-2}{3} \quad \text{and} \quad \text{slope of } BC = \frac{0 - 2}{6 - 3} = \frac{-2}{3}
$$

Slope of *AB* = Slope of *BC*

Thus *A*, *B* and *C* are collinear.

**Example 2:** Show that the triangle with vertices *A*(1, 1), *B*(4, 5) and *C*(12, –1) is a right triangle.

**Solution:** Slope of *AB* = *m1* = 5/1 + 4/3

$$
\text{and Slope of } BC = m_2 = \frac{-1 - 5}{12 - 4} = \frac{-6}{8} = \frac{-3}{4}
$$

Since *m1m2* = (4/3) - 3/4 = 1, therefore, *AB* ⊥ *BC*

So Δ*ABC* is a right triangle.

**4. Introduction to Analytic Geometry** *eLearn.Punjab*

**4.1 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.2 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.3 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.4 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.5 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.6 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.7 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.8 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.9 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.10 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.11 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.12 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.13 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.14 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.15 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.16 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.17 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.18 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.19 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.20 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.21 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.22 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.23 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.24 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.25 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.26 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.27 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.28 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.29 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.30 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.31 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.32 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.33 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.34 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.35 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.36 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.37 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.38 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.39 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.49 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.50 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.51 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.52 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.53 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.54 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.55 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.56 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.57 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.58 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.59 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.60 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.61 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.62 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.63 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.64 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.65 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.66 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.67 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.68 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.69 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.70 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.71 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.72 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.73 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.74 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.75 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.76 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.77 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.78 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.79 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.80 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.81 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.82 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.83 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.84 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.85 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.86 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.87 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.88 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.89 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.90 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.91 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.92 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.93 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.94 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.95 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.96 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.97 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.98 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.99 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.10 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.11 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.12 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.13 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.14 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.15 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.16 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.17 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.18 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.19 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.20 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.21 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.22 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.23 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.24 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.25 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.26 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.27 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.28 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.29 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.30 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.31 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.32 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.33 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.34 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.35 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.36 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.37 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.38 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.39 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.40 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.41 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.42 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.43 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.44 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.45 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.46 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.47 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.48 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.49 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.50 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.51 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.52 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.53 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.54 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.55 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.56 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.57 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.58 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.59 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.60 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.61 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.62 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.63 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.64 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.65 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.66 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.67 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.68 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.69 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.70 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.71 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.72 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.73 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.74 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.75 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.76 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.77 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.78 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.79 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.80 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.81 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.82 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.83 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.84 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.85 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.86 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.87 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.88 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.89 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.90 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.91 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.92 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.93 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.94 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.95 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.96 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.97 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.98 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.99 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.10 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.11 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.12 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.13 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.14 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.15 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.16 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.17 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.18 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.19 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.20 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.21 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.22 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.23 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.24 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.25 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.26 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.27 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.28 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.29 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.30 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.31 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.32 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.33 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.34 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.35 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.36 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.37 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.38 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.39 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.40 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.41 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.42 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.43 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.44 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.45 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.46 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.47 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.48 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.49 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.50 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.51 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.52 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.53 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.54 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.55 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.56 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.57 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.58 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.59 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.60 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.61 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.62 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.63 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.64 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.65 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.66 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.67 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.68 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.69 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.70 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.71 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.72 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.73 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.74 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.75 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.76 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.77 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.78 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.79 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.80 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.81 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.82 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.83 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.84 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.85 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.86 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.87 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.88 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.89 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.90 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.91 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.92 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.93 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.94 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.95 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.96 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.97 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.98 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.99 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.10 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.11 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.12 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.13 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.14 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.15 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.16 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.17 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.18 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.19 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.10 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.11 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.12 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.13 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.14 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.15 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.16 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.17 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.18 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.19 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.10 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.11 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.12 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.13 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.14 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.15 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.16 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.17 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.18 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.19 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.10 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.11 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.12 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.13 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.14 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.15 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.16 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.17 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.18 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.19 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.10 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.11 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.12 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.13 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.14 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.15 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.16 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.17 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.18 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.19 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.10 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.11 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.12 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.13 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.14 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.15 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.16 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.17 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.18 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.19 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.20 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.21 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.22 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.23 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.24 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.25 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.26 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.27 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.28 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.29 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.30 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.31 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.32 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.33 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.34 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.35 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.36 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.37 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.38 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.39 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.40 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.41 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.42 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.43 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.44 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.45 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.46 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.47 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.48 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.49 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.50 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.51 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.52 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.53 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.54 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.55 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.56 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.57 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.58 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.59 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.60 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.61 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.62 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.63 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.64 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.65 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.66 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.67 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.68 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.69 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.70 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.71 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.72 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.73 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.74 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.75 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.76 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.77 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.78 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.79 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.80 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.81 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.82 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.83 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.84 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.85 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.86 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.87 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.88 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.89 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.90 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.91 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.92 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.93 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.94 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.95 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.96 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.97 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.98 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.99 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.99 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.10 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.11 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.12 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.13 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.14 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.15 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.16 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.17 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.18 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.19 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.10 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.11 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.12 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.13 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.14 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.15 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.16 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.17 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.18 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.19 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.10 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.11 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.12 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.13 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.14 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.15 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.16 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.17 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.18 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.19 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.10 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.11 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.12 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.13 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.14 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.15 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.16 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.17 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.18 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.19 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.10 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.11 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.12 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.13 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.14 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.15 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.16 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.17 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.18 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.19 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.10 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.11 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.12 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.13 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.14 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.15 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.16 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.17 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.18 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.19 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.10 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.12 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.13 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.14 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.15 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.16 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.17 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.18 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.19 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.10 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.12 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.13 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.14 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.15 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.16 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.17 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.18 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.19 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.10 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.12 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.13 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.14 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.15 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.16 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.17 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.18 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.19 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.10 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.12 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.13 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.14 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.15 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.16 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.17 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.18 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.19 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.10 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.12 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.13 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.14 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.15 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.16 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.17 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.18 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.19 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.10 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.12 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.13 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.14 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.15 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.16 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.17 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.18 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.19 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.10 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.110 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.120 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.13 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.14 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.15 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.16 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.17 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.18 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.19 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.10 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.110 Introduction to Analyticategory** *eLearn.Punjab*

**4.120 Introduction to Analyticategory** *eLearn.Punjab*

**4.13 Introduction to Analyticategory** *eLearn.Punjab*

**4.14 Introduction to Analyticategory** *eLearn.Punjab*

**4.15 Introduction to Analyticategory** *eLearn.Punjab*

**4.16 Introduction to Analyticategory** *eLearn.Punjab*

**4.17 Introduction to Analyticategory** *eLearn.Punjab*

**4.18 Introduction to Analyticategory** *eLearn.Punjab*

**4.19 Introduction to Analyticategory** *eLearn.Punjab*

**4.10 Introduction to Analyticategory** *eLearn.Punjab*

**4.14 Introduction to Analyticategory** *eLearn.Punjab*

**4.15 Introduction to Analyticategory** *eLearn.Punjab*

**4.16 Introduction to Analyticategory** *eLearn.Punjab*

**4.17 Introduction to Analyticategory** *eLearn.Punjab*

**4.18 Introduction to Analyticategory** *eLearn.Punjab*

**4.19 Introduction to Analyticategory** *eLearn.Punjab*

**4.10 Introduction to Analyticategory** *eLearn.Punjab*

**4.110 Introduction to Analyticategory** *eLearn.Punjab*

**4.120 Introduction to Analyticategory** *eLearn.Punjab*

**4.13 Introduction to Analyticategory** *eLearn.Punjab*

**4.14 Introduction to Analyticategory** *eLearn.Punjab*

**4.15 Introduction to Analyticategory** *eLearn.Punjab*

**4.16 Introduction to Analyticategory** *eLearn.Punjab*

**4.17 Introduction to Analyticategory** *eLearn.Punjab*

**4.18 Introduction to Analyticategory** *eLearn.Punjab*

**4.19 Introduction to Analyticategory** *eLearn.Punjab*

**4.10 Introduction to Analyticategory** *eLearn.Punjab*

**4.110 Introduction to Analyticategory** *eLearn.Punjab*

**4.120 Introduction to Analyticategory** *eLearn.Punjab*

**4.13 Introduction to Analyticategory** *eLearn.Punjab*

**4.14 Introduction to Analyticategory** *eLearn.Punjab*

**4.15 Introduction to Analyticategory** *eLearn.Punjab*

**4.16 Introduction to Analyticategory** *eLearn.Punjab*

**4.17 Introduction to Analyticategory** *eLearn.Punjab*

**4.18 Introduction to Analyticategory** *eLearn.Punjab*

**4.19 Introduction to Analyticategory** *eLearn.Punjab*

**4.10 Introduction to Analyticategory** *eLearn.Punjab*

**4.14 Introduction to Analyticocracy** *eLearn.Punjab*

**4.15 Introduction to Analyticocracy** *eLearn.Punjab*

**4.16 Introduction to Analyticocracy** *eLearn.Punjab*

**4.17 Introduction to Analyticocracy** *eLearn.Punjab*

**4.18 Introduction to Analyticocracy** *eLearn.Punjab*

**4.19 Introduction to Analyticocracy** *eLearn.Punjab*

**4.10 Introduction to Analyticocracy** *eLearn.Punjab*

**4.14 Introduction to Analyticocracy** *eLearn.Punjab*

**4.15 Introduction to Analyticocracy** *eLearn.Punjab*

**4.16 Introduction to Analyticocracy** *eLearn.Punjab*

**4.17 Introduction to Analyticocracy** *eLearn.Punjab*

**4.18 Introduction to Analyticocracy** *eLearn.Punjab*

**4.19 Introduction to Analyticocracy** *eLearn.Punjab*

**4.10 Introduction to Analyticocracy** *eLearn.Punjab*

**4.110 Introduction to Analyticocracy** *eLearn.Punjab*

**4.120 Introduction to Analyticocracy** *eLearn.Punjab*

**4.13 Introduction to Analyticocracy** *eLearn.Punjab*

**4.14 Introduction to Analyticocracy** *eLearn.Punjab*

**4.15 Introduction to Analyticocracy** *eLearn.Punjab*

**4.16 Introduction to Analyticocracy** *eLearn.Punjab*

**4.17 Introduction to Analyticocracy** *eLearn.Punjab*

**4.18 Introduction to Analyticocracy** *eLearn.Punjab*

**4.19 Introduction to Analyticocracy** *eLearn.Punjab*

**4.10 Introduction to Analyticocracy** *eLearn.Punjab*

**4.14 Introduction to Analyticocracy** *eLearn.Punjab*

**4.15 Introduction to Analyticocracy** *eLearn.Punjab*

**4.16 Introduction to Analyticocracy** *eLearn.Punjab*

**4.17 Introduction to Analyticocracy** *eLearn.Punjab*

**4.18 Introduction to Analyticocracy** *eLearn.Punjab*

**4.19 Introduction to Analyticocracy** *eLearn.Punjab*

**4.10 Introduction to Analyticocracy** *eLearn.Punjab*

**4.10 Introduction to Analyticocracy** *eLearn.Punjab*

**4.16 Introduction to Analyticocracy** *eLearn.Punjab*

**4.17 Introduction to Analyticocracy** *eLearn.Punjab*

**4.18 Introduction to Analyticocracy** *eLearn.Punjab*

**4.19 Introduction to Analyticocracy** *eLearn.Punjab*

**4.10 Introduction to Analyticocracy** *eLearn.Punjab*

**4.10 Introduction to Analyticocracy** *eLearn.Punjab*

**4.17 Introduction to Analyticocracy** *eLearn.Punjab*

**4.19 Introduction to Analyticocracy** *eLearn.Punjab*

**4.10 Introduction to Analyticocracy** *eLearn.Punjab*

**4.10 Introduction to Analyticocracy** *eLearn.Punjab*

**4.19 Introduction to Analyticocracy** *eLearn.Punjab*

**4.19 Introduction to Analyticocracy** *eLearn.Punjab*

**4.19 Introduction to Analyticocracy** *eLearn.Punjab*

**4.19 Introduction to Analyticocracy** *eLearn.Punjab*

**4.19 Introduction to Analyticocracy** *eLearn.Punjab*

**4.19 Introduction to Analyticocracy** *eLearn.Punjab*

**4.19 Introduction to Analyticocracy** *eLearn.Punjab*

**4.19 Introduction to Analyticocracy** *eLearn.Punjab*

**4.19 Introduction to Analyticocracy** *eLearn.Punjab*

**4.19 Introduction to Analyticocracy** *eLearn.Punjab*

**4.19 Introduction to Analyticocracy** *eLearn.Punjab*

**4.19 Introduction to Analyticocracy** *eLearn.Punjab*

**4.19 Introduction to Analyticocracy** *eLearn.Punjab*

**4.19 Introduction to Analyticocracy** *eLearn.Punjab*

**4.19 Introduction to Analyticocracy** *eLearn.Punjab*

**4.19 Introduction to Analyticocracy** *eLearn.Punjab*

**4.19 Introduction to Analyticocracy** *eLearn.Punjab*

**4.19 Introduction to Analyticocracy** *eLearn.Punjab*

**4.19 Introduction to Analyticocracy** *eLearn.Punjab*

**4.19 Introduction to Analyticocracy** *eLearn.Punjab*

**4.19 Introduction to Analyticocracy** *eLearn.Punjab*

**4.19 Introduction to Analyticocracy** *eLearn.Punjab*

**4.19 Introduction to Analyticocracy** *eLearn.Punjab*

**4.19 Introduction to Analyticocracy** *eLearn.Punjab*

**4.19 Introduction to Analyticocracy** *eLearn.Punjab*

**4.19 Introduction to Analyticocracy** *eLearn.Punjab*

**4.19 Introduction to Analyticocracy** *eLearn.Punjab*

**4.19 Introduction to Analyticocracy** *eLearn.Punjab*

**4.19 Introduction to Analyticocracy** *eLearn.Punjab*

**4.19 Introduction to Analyticocracy** *eLearn.Punjab*

**4.19 Introduction to Analyticocracy** *eLearn.Punjab*

All the points on the line *I* parallel to *x*-axis remain at a constant distance (say *a*) from *x*-axis. Therefore, each point on the line has its distance from *x*-axis equal to *a*, which is its *y*-coordinate (ordinate). So, all the points on this line satisfy the equation: *y* = *a*

|  Note: | (i) | If *a* > 0, then the line *I* is above the *x*-axis.  |
| --- | --- | --- |
|   | (ii) | If *a* < 0, then the line *I* is below the *x*-axis.  |
|   | (iii) | If *a* = 0, then the line *I* becomes the *x*-axis.  |
|   |  | Thus the equation of *x*-axis is *y* = 0  |

### 4.3.2 Equation of a Straight Line Parallel to the *x*-axis (or perpendicular to the *y*-axis)

### 4.3.4 Derivation of Standard Forms of Equations of Straight Lines

#### Intercepts:

- If a line intersects *x*-axis at (*a*, 0), then *a* is called *x*-intercept of the line.
- If a line intersects *y*-axis at (0, *b*), then *b* is called *y*-intercept of the line.

#### 1. Slope-Intercept form of Equation of a Straight Line:

**Theorem:** Equation of a non-vertical straight line with slope *m* and *y*-intercept *c* is given by:

$$ y = mx + c $$

**Proof:** Let *P*(*x*, *y*) be an arbitrary point of the straight line *I* with slope *m* and *y*-intercept *c*. As *C*(0, *c*) and *P*(*x*, *y*) lie on the line, so the slope of the line is:

$$ m = \frac{y - c}{x - 0} \quad \text{or} \quad y - c = mx \quad \text{and} \quad y = mx + c $$

is an equation of *I*.

The equation of the line for which

$$ c = 0 \text{ is } \qquad y = mc $$

In this case the line passes through the origin.

**Example 1:** Find an equation of the straight line if

- (a) its slope is 2 and *y*-intercept is 5
- (b) it is perpendicular to a line with slope –6 and its *y*-intercept is $$\frac{4}{3}$$

**Solution:** (a) The slope and *y*-intercept of the line are respectively:

$$ m = 2 \qquad \text{and} \qquad c = 5 $$

Thus *y* = 2*x* + 5 (Slope-intercept form: *y* = *mx* + *c*)

is the required equation.

- (b) The slope of the given line is

$$ m_i = -6 $$

The slope of the required line is:

$$ m_i = \frac{1}{m_i} \quad \frac{1}{6} $$

The slope and *y*-intercept of the required line are respectively:

$$ m = \frac{1}{6} \qquad \text{(slope of } \perp \text{ line is } -6) \quad \text{and} \qquad c = \frac{4}{3} $$

Thus *y* = $$\frac{1}{6}(*)$$ or *6y* *x* 8

is the required equation.

#### 2. Point-slope Form of Equation of a Straight Line:

**Theorem:** Equation of a non-vertical straight line *I* with slope *m* and passing through a point *Q*(*x*, *y*) is

$$
y-y_1 = m(x - x_1)
$$

**Proof:** Let \( P(x, y) \) be an arbitrary point of the straight line with slope \( m \) and passing through \( Q(x_1, y_1) \).

As \( Q(x_1, y_1) \) and \( P(x, y) \) both lie on the line, so the slope of the line is

$$
m = \frac{y - y_1}{x - x_1} \text{ or } y - y_1 = m(x - x_1)
$$

which is an equation of the straight line passing through \( x_1, y_1 \) with slope \( m \).

### 3. Symmetric Form of Equation of a Straight Line:

We have \( \frac{y - y_1}{x - x_1} = \tan \alpha \), where \( \alpha \) is the inclination of the line.

$$
\lim_{m \to \infty} \frac{x - x_1}{\cos \alpha} = \frac{y - y_1}{\sin \alpha} = r(\sin \alpha)
$$

This is called **symmetric** form of equation of the line.

**Example 2:** Write down an equation of the straight line passing through \( (5, 1) \) and parallel to a line passing through the points \( (0, -1) \), \( (7, -15) \).

**Solution:** Let \( m \) be the slope of the required straight line, then

$$
m = \frac{-15 - (-1)}{7 - 0} \qquad \text{(☞ Slopes of parallel lines are equal)}
$$

$$
= -2
$$

As the point \( (5, 1) \) lies on the required line having slope -2 so, by point-slope form of equation of the straight line, we have

$$
y - (1) = -2(x - 5)
$$

or

$$
y = -2x + 11
$$

or

$$
2x + y - 11 = 0
$$

is an equation of the required line.

### 4. Two-point Form of Equation of a Straight Line:

**Theorem:** Equation of a non-vertical straight line passing through two points \( Q(x_1, y_1) \) and \( R(x_2, y_2) \) is

$$
y - y_1 = \frac{y_2 - y_1}{x_2 - x_1} (x - x_1) \text{ or } y - y_2 = \frac{y_2 - y_1}{x_2 - x_1} (x - x_2)
$$

**Proof:** Let \( P(x, y) \) be an arbitrary point of the line passing through \( Q(x_1, y_1) \) and \( R(x_2, y_2) \). So

$$
\frac{y - y_1}{x - x_1} = \frac{y - y_2}{x - x_2} = \frac{y_2 - y_1}{x_2 - x_1} \qquad (P, Q \text{ and } R \text{ are collinear points})
$$

We take

$$
\frac{y - y_1}{x - x_1} = \frac{y_2 - y_1}{x_2 - x_1}
$$

or

$$
y - y_1 = \frac{y_2 - y_1}{x_2 - x_1} (x - x_1) \text{ the required equation of the line } PQ.
$$

or

$$
(y_2 - y_1) x - (x_2 - x_1) y + (x_2 y_2 - x_2 y_1) = 0
$$

We may write this equation in determinant form as:

$$
\left| \begin{array}{ccc}
x & y & 1 \\
x_1 & y_1 & 1 \\
x_2 & y_2 & 1
\end{array} \right|
$$

**Note:** (i) If \( x_1 = x_2 \) then the slope becomes undefined. So, the line is vertical.

(ii) \( y - y_2 = \frac{y_2 - y_1}{x_2 - x_1} (x - x_1) \) can be derived similarly.

Example 3: Find an equation of line through the points $(-2,1)$ and $(6,-4)$.

Solution: Using two-points form of the equation of straight line, the required equation is

$$
\begin{aligned}
& y-1=\frac{-4-1}{6-(-2)}[x-(-2)] \\
\text { or } \quad & y-1=\frac{-5}{9}(x+2) \text { or } 5 x+8 y+2=0
\end{aligned}
$$

## 5. Intercept Form of Equation of a Straight Line:

Theorem: Equation of a line whose non-zero $x$ and $y$-intercepts are $a$ and $b$ respectively is

$$
\frac{x}{a} \cdot \frac{y}{b}=1
$$

Proof: Let $P(x, y)$ be an arbitrary point of the line whose non-zero $x$ and $y$-intercepts are $a$ and $b$ respectively. Obviously, the points $A(a, 0)$ and $B(0, b)$ lie on the required line. So, by the two-point form of the equation of line, we have

$$
\begin{aligned}
& y-0=\frac{b-0}{0-a}(x-a) \quad(P, A \text { and } B \text { are collinear }) \\
& \text { or } \quad-a y=b(x-a) \\
& \text { or } \quad b x+a y=a b \\
& \text { or } \quad \frac{x}{a}+\frac{y}{b}=1 \quad \text { (dividing by } a b \text { ) } \\
& \text { Hence the result. }
\end{aligned}
$$

Example 4: Write down an equation of the line which cuts the $x$-axis at $(2,0)$ and $y$-axis at $(0,-4)$.

Solution: As 2 and -4 are respectively $x$ and $y$-intercepts of the required line, so by two-intercepts form of equation of a straight line, we have

$$
\frac{x}{2}+\frac{y}{-4}=1-\quad \text { or }=2 x \quad y \quad 4 \quad 0
$$

which is the required equation.

Example 5: Find an equation of the line through the point $P(2,3)$ which forms an isosceles triangle with the coordinate axes in the first quadrant.

Solution: Let $O A B$ be an isosceles triangle so that the line $A B$ passes through $A=(a, 0)$ and $B(0, a)$, where $a$ is some positive real number.
Slope of $A B=\frac{a-0}{0-a}=-1$. But $A B$ passes through $P(2,3)$.
$\because \quad$ Equation of the line through $P(2,3)$ with slope -1 is

$$
y-3=-1(x-2) \text { or } \quad x+y-5=0
$$

## 6. Normal Form of Equation of a Straight Line:

Theorem: An equation of a non-vertical straight line $I$, such that length of the perpendicular from the origin to $I$ is $p$ and $\alpha$ is the inclination of this perpendicular, is

$$
x \cos \alpha+y \sin \alpha=p
$$

Proof: Let the line $I$ meet the $x$-axis and $y$-axis at the points $A$ and $B$ respectively. Let $P(x, y)$ be an arbitrary point of $A B$ and let $O R$ be perpendicular to the line $I$. Then $|O R|=p$.

From the right triangles $O R A$ and $O R B$, we have,

$$
\cos \alpha=\frac{p}{O A} \quad \text { or } \quad O A=\frac{p}{\cos \alpha}
$$

and

$$
\cos \left(90^{\circ}-\alpha\right)=\frac{p}{O B} \quad \text { or } \quad O B=\frac{p}{\sin \alpha}
$$

$$
\left[:: \cos \left(90^{\circ}-\alpha\right)=\sin \alpha\right)\right]
$$

As $O A$ and $O B$ are the $x$ and $y$-intercepts of the line $A B$, so equation of $A B$ is

$$
\frac{x}{p / \cos \alpha}+\frac{y}{p / \sin \alpha}=1 \quad \text { (Two-intercept form) }
$$

That is $x \cos \alpha+y \sin \alpha=p$ is the required equation.

Example 6: The length of perpendicular from the origin to a line is 5 units and the inclination of this perpendicular is $120^{\circ}$. Find the slope and $y$-intercept of the line.

Solution. Here $p=5, \alpha=120^{\circ}$.
Equation of the line in normal form is

$$
\begin{aligned}
& x \cos 120^{\circ}+y \sin 120^{\circ}=5 \\
& \Rightarrow \quad-\frac{1}{2} x+\frac{\sqrt{3}}{2} y=5 \\
& \Rightarrow \quad x-\sqrt{3} y+10=0
\end{aligned}
$$

To find the slope of the line, we re-write (1) as: $y=\frac{x}{\sqrt{3}}+\frac{10}{\sqrt{3}}$
which is slope-intercept form of the equation.
Here $\quad m=\frac{1}{\sqrt{3}}$ and $c=\frac{10}{\sqrt{3}}$

### 4.3.5 A Linear Equation in two Variables Represents a Straight Line

Theorem: The linear equation $a x+b y+c=0$ in two variables $x$ and $y$ represents a straight line. A linear equation in two variables $x$ and $y$ is

$$
a x+b y+c=0
$$

where $a, b$ and $c$ are constants and $a$ and $b$ are not simultaneously zero.

## 4. Introduction to Analytic Geometry

## 4.3.5 A Linear Equation in two Variables Represents a Straight Line

Theorem: The linear equation $a x+b y+c=0$ in two variables $x$ and $y$ represents a straight line. A linear equation in two variables $x$ and $y$ is

$$
a x+b y+c=0
$$

where $a, b$ and $c$ are constants and $a$ and $b$ are not simultaneously zero.

## 24

## Remember that:

The equation (I) represents a straight line and is called the general equation of a straight line.
the $y$-axis at a directed distance $-\frac{c}{a}$ from the $y$-axis.
Case II: $\quad a=0, \quad b \neq 0$
In this case equation (1) takes the form:

$$
b x+c=0 \text { or } y=-\frac{c}{b}
$$

which is an equation of the straight line parallel to $x$-axis at a directed distance $\frac{-c}{b}$ from the $x$-axis.
Case III: $\quad a \neq 0 \quad, \quad b \neq 0$
In this case equation (1) takes the form:

$$
b y=-a x-c \quad \text { or } \quad y=\frac{-a}{b} x-\frac{c}{b}=m x+c
$$

which is the slope-intercept form of the straight line with slope $\frac{-a}{b}$ and $y$-intercept $\frac{-c}{b}$.
Thus the equation $a x+b y+c=0$, always represents a straight line.

### 4.3.6 To Transform the General Linear Equation to Standard Forms

Theorem: To transform the equation $a x+b y+c=0$ in the standard form

## 1. Slope-Intercept Form.

We have

$$
b y=-a x-c \quad \text { or } \quad y=\frac{-a}{b} \times-\frac{c}{b}=m x+c \text {, where } m=\frac{-a}{b}, c=\frac{-c}{b}
$$

## 2. Point - Slope Form

We note from (1) above that slope of the line $a x+b y+c=0$ is $\frac{-a}{b}$. A point on the line is $\left(\frac{-c}{a}, 0\right)$

Equation of the line becomes $y=\frac{-a}{b}\left(x+\frac{c}{a}\right)$
which is in the point-slope form.

## 3. Symmetric Form

$$
m=\tan \alpha=\frac{-a}{b} \cdot \sin \alpha=\frac{a}{\pm \sqrt{a^{2}+b^{2}}} \cdot \cos \alpha \quad \frac{b}{\pm \sqrt{a^{2}+b^{2}}}
$$

A point on $a x+b y+c=0$ is $\left(\frac{-c}{a}, 0\right)$
Equation in the symmetric form becomes

$$
\frac{x-\left(-\frac{c}{a}\right)}{b / \pm \sqrt{a^{2}+b^{2}}}=\frac{y-0}{a / \pm \sqrt{a^{2}+b^{2}}} \quad r
$$

is the required transformed equation. Sign of the radical to be properly chosen.

## 4. Two -Point Form

We choose two arbitrary points on $a x+b y+c=0$. Two such points are $\left(\frac{-c}{a}, 0\right)$ and $\left(0, \frac{-c}{b}\right)$. Equation of the line through these points is

$$
\frac{y-0}{0+\frac{c}{b}}=\frac{x+\frac{c}{a}}{-\frac{c}{a}-0} \quad \text { i.e., } y \quad 0 \quad \frac{-a}{b}\left(x \quad \frac{c}{a}\right)
$$

## 5. Intercept Form.

$$
a x+b y=-c \quad \text { or } \quad \frac{a x}{-c}+\frac{b y}{-c}=1 \quad \text { i.e } \quad \frac{x}{-c / a} \quad \frac{y}{-c / b} \quad 1=
$$

which is an equation in two intercepts form.

## 6. Normal Form.

The equation: $a x+b y+c=0$
can be written in the normal form as:

$$
\frac{a x+b y}{\pm \sqrt{a^{2}+b^{2}}}=\frac{-c}{\pm \sqrt{a^{2}+b^{2}}}
$$

The sign of the radical to be such that the right hand side of (2) is positive.
Proof. We know that an equation of a line in normal form is

$$
x \cos \alpha+y \sin \alpha=p
$$

If (1) and (3) are identical, we must have

$$
\frac{a}{\cos \alpha}=\frac{b}{\sin \alpha}=\frac{-c}{p}
$$

i.e.,

$$
\frac{p}{-c}=\frac{\cos \alpha}{a}=\frac{\sin \alpha}{b}=\frac{\sqrt{\cos ^{2} \alpha+\sin ^{2} \alpha}}{\pm \sqrt{a^{2}+b^{2}}} \quad \frac{1}{\pm \sqrt{a^{2}+b^{2}}}
$$

Hence, $\quad \cos \alpha=\frac{a}{\pm \sqrt{a^{2}+b^{2}}}$ and $\sin \alpha \quad \frac{b}{\pm \sqrt{a^{2}+b^{2}}}$
Substituting for $\cos \alpha, \sin \alpha$ and $p$ into (3), we have

$$
\frac{a x+b y}{\pm \sqrt{a^{2}+b^{2}}}=\frac{-c}{\pm \sqrt{a^{2}+b^{2}}}
$$

Thus (1) can be reduced to the form (2) by dividing it by $\pm \sqrt{a^{2}+b^{2}}$. The sign of the radical to be chosen so that the right hand side of (2) is positive.

Example 1: Transform the equation $5 x-12 y+39=0$ into
(i) Slope intercept form.
(ii) Two-intercept form.
(iii) Normal form.
(iv) Point-slope form.
(v) Two-point form.
(vi) Symmetric form.

## (i) We have $12 y=8 x \quad 39$ or $=y \quad \frac{5}{12} x \quad \frac{39}{12} y m \quad \frac{5}{12}, y$-intercept $c=\frac{39}{12}$
(ii) $5 x-12 y=39$ or $\frac{5 x}{-39} \quad \frac{12 y}{39} \quad 1$ or $\frac{x}{-39 / 5} \quad \frac{y}{39 / 12} \quad 1$ is the required equation.
(iii) $5 x-12 y=39$. Divide both sides by $\pm \sqrt{5^{2}+125}=13$. Since R.H.S is to be positive, we have to take negative sign.

Hence $=\frac{5 x}{-13}+\frac{12 y}{13}=3$ is the normal form of the equation.
(iv) A point on the line is $\left(\frac{-39}{5}, 0\right)$ and its slope is $\frac{5}{12}$.

Equation can be written as: $y-0=\frac{5}{12}\left(x+\frac{39}{5}\right)$
(v) Another point on the line is $\left(0, \frac{39}{12}\right)$. Line through $\left(\frac{-39}{5}, 0\right)$ and $\left(0, \frac{39}{12}\right)$ is

$$
\frac{y-0}{0-\frac{39}{12}}=\frac{x+\frac{39}{5}}{-\frac{39}{5}-0}
$$

(vi) We have $\tan \alpha=\frac{5}{12}=m, \sin \alpha=\frac{5}{13}, \cos \alpha=\frac{12}{13}$. A point of the line is $\left(\frac{-39}{5}, 0\right)$. Equation of the line in symmetric form is

$$
\frac{x+39 / 5}{12 / 13}=\frac{y-0}{5 / 13}=r(\text { say })
$$

Example 2: $\quad$ Sketch the line
$3 x+2 y+6=0$.

Solution: To sketch the graph of (1), we find two points on it. If $y=0, x=-2$ and if $x=0, y=-3$.

Thus $x$ intercept $=-2$
$y$ intercept $=-3$
The points $A(-2,0), B(0,-3)$ are on (1). Plot these points in the plane and draw the straight line through $A$ and $B$. It is the graph of (1).

Example 3: $\quad$ Find the distance between the parallel lines
$2 x+y+2=0$
and $\quad 6 x+3 y-8=0$
(1)

Sketch the lines. Also find an equation of the line parallel to the given lines and lying midway between them.

Solution: We first convert both the lines into normal form. (1) can be written as $2 x+y=-2$
Dividing both sides by $-\sqrt{4+1}$, we have

$$
\frac{-2}{\sqrt{5}} x+\frac{-y}{\sqrt{5}}=\frac{2}{\sqrt{5}}
$$

which is normal form of (1). Normal form of (2) is

$$
\frac{6 x}{\sqrt{45}}+\frac{3 y}{\sqrt{45}}=\frac{8}{\sqrt{45}}
$$

i.e., $\frac{2 x}{\sqrt{5}}+\frac{y}{\sqrt{5}}=\frac{8}{3 \sqrt{5}}$

Length of the perpendicular from $(0,0)$ to the line (1) is $\frac{-}{\sqrt{5}}[$ From (3)]
Similarly, length of the perpendicular from $(0,0)$ to the line (2) is $\frac{8}{3 \sqrt{5}}[$ From (4)]

From the graphs of the lines it is clear that the lines are on opposite sides of the origin, so the distance between them equals the sum of the two perpendicular lengths.
i.e., Required distance $=\frac{2}{\sqrt{5}}+\frac{8}{3 \sqrt{5}}=\frac{14}{3 \sqrt{5}}$

The line parallel to the given lines lying midway between them is such that length of the perpendicular
from $O$ to the line $=\frac{8}{3 \sqrt{5}}-\frac{7}{3 \sqrt{5}}\left(\right.$ or $\frac{7}{3 \sqrt{5}}-\frac{2}{\sqrt{5}}$ ) $=\frac{1}{3 \sqrt{5}}$
Required line is $=\frac{2 x}{\sqrt{5}}+\frac{y}{\sqrt{5}}=-\frac{1}{3 \sqrt{5}}$ or $6 x+3 y=1$

### 4.3.7 Position of a point with respect to a line

Consider a non-vertical line $I$

$$
I: a x+b y+c=0
$$

in the $x y$-plane. Obviously, each point of the plane is either above the line or below the line or on the line.

Theorem: Let $P\left(x_{i}, y_{i}\right)$ be a point in the plane not lying on $I$

$$
I: a x+b y+c=0
$$

then $P$ lies
a) above the line (1) if $a x_{i}+b y_{i}+c>0$
b) below the line (1) if $a x_{i}+b y_{i}+c<0$

Proof: We can suppose that $b>0$ (first multiply the equation by -1 if needed). Draw a perpendicular from $P$ on $x$-axis meeting the line at $\left\langle x_{i} x_{i}, y^{\prime}\right\rangle$.

Thus $a x_{i}+b y^{\prime}+c=0$ so that

$$
y^{\prime}=\frac{a}{b} x_{i} \frac{c}{b}
$$

The point $P\left(x_{i}, y_{i}\right)$ is above the line if $y_{i}>y^{\prime}$ that is

$$
\begin{aligned}
& y_{i}-y^{\prime}>0 \\
\text { i.e. } & y_{i}-\left(-\frac{a}{b} x_{i}-\frac{c}{b}\right)>0 \\
\Rightarrow \quad & a x_{i}+b y_{i}+c>0
\end{aligned}
$$

Similarly $P\left(x_{i}, y_{i}\right)$ is below the line if

$$
y_{i}-y^{\prime}<0 \quad \text { i.e. } y_{i}-\left(-\frac{a}{b} x_{i}-\frac{c}{b}\right)
$$

or

$$
a x_{i}+b y_{i}+c<0
$$

The point $P\left(x_{i}, y_{i}\right)$ is on the line if

$$
a x_{i}+b y_{i}+c=
$$

Corollary 1. The point $P$ is above or below $I$ respectively if $a x_{i}+b y_{i}+c$ and $b$ have the same sign or have opposite signs.

Proof. If $P$ is above $I$, then $y_{i}-y^{\prime}>0$ i.e., $\frac{a x_{i}+b y_{i}+c}{b}>0$
Thus $a x_{i}+b y_{i}+c$ and $b$ have the same sign.
Similarly, $P$ is below $I$ if

$$
y_{i}-y^{\prime}<0 \quad \text { i.e., } \frac{a x_{i}+b y_{i}+c}{b}<0
$$

Thus $a x_{i}+b y_{i}+c$ and $b$ have opposite signs.
Corollary 2. The point $P\left(x_{i}, y_{i}\right)$ and the origin are
(i) on the same side of $I$ according as $a x_{i}+b y_{i}+c$ and $c$ have the same sign.
(ii) on the opposite sides of $I$ according as $a x_{i}+b y_{i}+c$ and $c$ have opposite signs.

Proof. (i) The point $P\left(x_{i}, y_{i}\right)$ and $O(0,0)$ are on the same side of $I$ if $a x_{i}+b y_{i}+c$ and $a .0+b .0+c$ have the same sign.
(ii) Proof is left as an exercise

Example 1: Check whether the point $(-2,4)$ lies above or below the line $4 x+5 y-3=0$

Solution: Here $b=5$ is positive. Also
$4(-2)+5(4)-3=-8+20-3=9>0$
The coefficient of $y$ in (1) and the expression (2) have the same sign and so the point $(-2,4)$ lies above (1).

Example 2: $\quad$ Check whether the origin and the point $P(5,-8)$ lie on the same side or on the opposite sides of the line:

$$
3 x+7 y+15=0
$$

## Here $\quad c=15$
For $P(5,-8)$,
$3(5)+7(-8)+15=-26<0$
But $\quad c=15>0$
$c$ and the expression (2) have opposite signs. Thus $O(0,0)$ and $P(5,-8)$ are on the opposite sides of (1).

Note: To check whether a point $P\left(x_{1}, y_{1}\right)$ lies above or below the line $a x+b y+c=0$
we make the co-efficient of $y$ positive by multiplying the equation by $(-1)$ if needed.

### 4.4 TWO AND THREE STRAIGHT LINES

For any two distinct lines $l_{1}, l_{2}$.
$l_{1}: a_{1} x+b_{1} y+c=0$ and $l_{2}: a_{2} x+b_{2} y+c=0$, one and only one of the following holds:
(i) $l_{1} \| l_{2}$
(ii) $l_{1} \perp l_{2}$
(iii) $l_{1}$ and $l_{2}$ are not related as (i) or (ii).

The slopes of $l_{1}$ and $l_{2}$ are $m_{1}=\frac{a_{1}}{b_{1}}, m_{2} \quad \frac{a_{2}}{b_{2}}$
(iv) $l_{1} \leq l_{2} \Leftrightarrow$ slope of $l_{1}\left(m_{1}\right)=$ slope of $l_{2}\left(m_{2}\right)$.

$$
\begin{aligned}
& \Leftrightarrow \quad \frac{a_{1}}{b_{1}}=-\frac{a_{2}}{b_{2}} \\
& \Leftrightarrow \quad \frac{a_{1}}{b_{2}}=-\frac{a_{2}}{b_{2}} \quad \Leftrightarrow \quad a_{1} b_{2}-b_{1} a_{2}=0
\end{aligned}
$$

(ii) $l_{1} \perp l_{2} \Leftrightarrow m_{1} m_{2}=-1$

$$
\Leftrightarrow\left(-\frac{a_{1}}{b_{1}}\right)\left(-\frac{a_{2}}{b_{2}}\right)=-1 \quad \Leftrightarrow a_{1} a_{2}+b_{1} b_{2}=0
$$

(iii) If $l_{1}$ and $l_{2}$ are not related as in (i) and (ii), then there is no simple relation of the above forms.

### 4.4.1 The Point of Intersection of two Straight Lines

Let $\quad l_{1}: a_{1} x+b_{1} y+c_{1}=0$
and $\quad l_{2}: a_{2} x+b_{2} y+c_{2}=0$
be two non-parallel lines. Then $a_{1} b_{2}-b_{1} a_{2} \neq 0$
Let $P\left(x_{1}, y_{1}\right)$ be the point of intersection of $l_{1}$ and $l_{2}$. Then
$a_{1} x_{1}+b_{1} y_{1}+c_{1}=0$
$a_{2} x_{1}+b_{2} y_{1}+c_{2}=0$
Solving (3) and (4) simultaneously, we have

$$
\begin{aligned}
& \frac{x_{1}}{b_{1} c_{2}-b_{2} c_{1}}=\frac{y_{1}}{a_{1} c_{1}-a_{1} c_{2}}=\frac{1}{a_{1} b_{2}-a_{2} b_{1}} \\
& x_{1}=\frac{b_{1} c_{2}-b_{2} c_{1}}{a_{1} b_{2}-a_{2} b_{1}} \text { and } y_{1} \quad \frac{a_{1} c_{1}-a_{1} c_{2}}{a_{1} b_{2}-a_{2} b_{1}}
\end{aligned}
$$

is the required point of intersection.

Note: $a_{1} b_{2}-a_{2} b_{1} \neq 0$, otherwise $l_{1} \| l_{2}$

Examples 1: Find the point of intersection of the lines

$$
\begin{aligned}
& 5 x+7 y=35 \\
& 3 x-7 y=21
\end{aligned}
$$

(ii)

Solution: We note that the lines are not parallel and so they

$$
\begin{aligned}
& \text { * If the lines are parallel } \\
& \text { then solution does not } \\
& \text { must intersect at a point. Adding (i) and (ii), we have } \\
& 8 x=56 \quad \text { or } \quad x=7 \\
& \text { Setting this value of } x \text { into (1), we find, } y=0 \text {. } \\
& \text { Thus }(7,0) \text { is the point of intersection of the two lines. }
\end{aligned}
$$

exist ( $z a, b_{1}-a, b_{1}=0$ )

* Before solving equations one should ensure that lines are not parallel.

### 4.4.2 Condition of Concurrency of Three Straight Lines

Three non-parallel lines

$$
\begin{aligned}
& l_{1}: a_{1} x+b_{1} y+c_{1}=0 \\
& l_{2}: a_{1} x+b_{2} y+c_{2}=0 \\
& l_{3}: a_{1} x+b_{2} y+c_{3}=0
\end{aligned}
$$

are concurrent iff $\left|\begin{array}{ll}a_{1} & b_{1} \\ a_{2} & b_{2} \\ a_{3} & b_{3} & c_{3}\end{array}\right|=0$

Proof: If the lines are concurrent then they have a common point of intersection $P\left(x_{1}, y_{1}\right)$ say. As $l_{1} \not l_{2}$, so their point of intersection $(x, y)$ is

$$
x=\frac{b_{1} c_{1}-b_{2} c_{2}}{a_{1} b_{2}-a_{2} b_{1}} \text { and } y \quad \frac{a_{1} c_{1}-a_{2} c_{2}}{a_{1} b_{2}-a_{2} b_{1}}
$$

This point also lies on (3), so

$$
\begin{aligned}
& a_{1}\left(\frac{b_{1} c_{1}-b_{2} c_{2}}{a_{1} b_{2}-a_{2} b_{1}}\right)+b_{2}\left(\frac{a_{1} c_{1}-a_{2} c_{2}}{a_{1} b_{2}-a_{2} b_{1}}\right)+c_{3}=0 \\
& a_{1}\left(b_{1} c_{2}-b_{2} c_{2}\right)+b_{2}\left(a_{1} c_{1}-a_{2} c_{2}\right)+c_{3}\left(a_{1} b_{2}-a_{2} b_{1}\right)=0
\end{aligned}
$$

or

An easier way to write the above equation is in the following determinant form:

$$
\left|\begin{array}{lll}
a_{1} & b_{1} & c_{1} \\
a_{2} & b_{2} & c_{2}
\end{array}\right|=0
$$

This is a necessary and sufficient condition of concurrency of the given three lines.
Example 1: Check whether the following lines are concurrent or not. If concurrent, find the point of concurrency.

$$
\begin{aligned}
& 3 x-4 y-3=0 \\
& 5 x+12 y+1=0 \\
& 32 x+4 y-17=0
\end{aligned}
$$

Solution. The determinant of the coefficients of the given equations is

$$
\begin{aligned}
& \left|\begin{array}{lll}
3 & -4 & -3 \\
5 & 12 & 1 \\
32 & 4 & -17
\end{array}\right|=\left|\begin{array}{lll}
18 & 32 & 0 \\
5 & 12 & 1 \\
117 & 208 & 0
\end{array}\right| \cdot \text { by } \quad R_{1}+3 R_{2} \\
& =-1\left|\begin{array}{ll}
18 & 32 \\
117 & 208
\end{array}\right|=-\left(208 \times 18-117 \times 32\right)=0
\end{aligned}
$$

Thus the lines are concurrent.
The point of intersection of any two lines is the required point of concurrency. From (1) and (2), we have

$$
\begin{aligned}
& \frac{x}{-4+36}=\frac{y}{-15-3}=\frac{1}{36+20} \\
& x=\frac{32}{56}=\frac{4}{7} \text { and } y=\frac{-18}{56}=\frac{-9}{28} \text { i.e. }\left(\frac{4}{7}, \frac{-9}{28}\right)
\end{aligned}
$$

is the point of intersection.

### 4.4.3 Equation of Lines through the point of intersection of two lines

We can find a family of lines through the point of intersection of two non parallel lines $l_{1}$ and $l_{2}$.

Let $l_{1}: a_{1} x+b_{1} y+c_{1}=0$
and $l_{2}: a_{2} x+b_{2} y+c_{2}=0$
For a non-zero real $h$, consider the equation

$$
a_{1} x+b_{1} y+c_{1}+h\left(a_{1} x+b_{1} y+c_{2}\right)=0
$$

This, being a linear equation, represents a straight line. For different values of $h$, (3) represents different lines. Thus (3) is a family of lines.

If $\left(x_{1}, y_{1}\right)$ is any point lying on both (1) and (2), then it is their point of intersection. Since $\left(x_{1}, y_{1}\right)$ lies on both (1) and (2), we have

$$
a_{1} x+b_{1} y+c_{1}=0+\text { and }+a_{2} x \quad b_{2} y \quad c_{2} \quad 0
$$

From the above two equations, we note that $\left(x_{1}, y_{1}\right)$ also lies on (3).
Thus (3) is the required family of lines through the point of intersection of (1) and (2). Since $h$ can assume an infinite number of values, (3) represents an infinite number of lines.

A particular line of the family (3) can be determined if one more condition is given.
Example 2: Find the family of lines through the point of intersection of the lines

$$
\begin{aligned}
& 3 x-4 y-10=0 \\
& x+2 y-10=0
\end{aligned}
$$

Find the member of the family which is
(i) parallel to a line with slope $\frac{-2}{3}$
(ii) perpendicular to the line $l: 3 x-4 y+1=0$.

Solution: (i) A family of lines through the point of intersection of equations (1) and (2) is

$$
\begin{aligned}
& 3 x-4 y-10+k(x+2 y-10)=0 \\
& \text { or } \quad(3+k) x+(-4+2 k) y+(-10-10 k)=0
\end{aligned}
$$

Slope $m$ of (3) is given by: $m=-\frac{3+k}{-4+2 k}$
This is slope of any member of the family (3).
If (3) is parallel to the line with slope $-\frac{2}{3}$ then
$-\frac{3+k}{-4+2 k}=\frac{-2}{3}$ or $9+3 k=-8+4 k$ i.e., $k=17$
Substituting $k=17$ into (3), equation of the member of the family is
$20 x+30 y-180=0$ i.e., $2 x+3 y-18=0$
(ii) Slope of $3 x-4 y+1=0$
is $\frac{3}{4}$. Since (3) is to be perpendicular to (4), we have $-\frac{3+k}{-4+2 k} \times \frac{3}{4}=-1$
or $9+3 k=-16+8 k \quad$ or $\quad k=5$
Inserting this value of $k$ into (3), we get $4 x+3 y-30=0$ which is required equation of the line.

Theorem: Altitudes of a triangle are concurrent.
Proof. Let the coordinates of the vertices of $\triangle A B C$ be as shown in the figure.

Then slope of $B C=\frac{y_{2}-y_{1}}{x_{2}-x_{1}}$
Therefore slope of the altitude $A D=-\frac{x_{2}-x_{1}}{y_{2}-y_{1}}$

## Equation of the altitude $A D$ is

$$
\begin{aligned}
& y-y_{1}=-\frac{x_{2}-x_{1}}{y_{2}-y_{1}}\left(x-x_{1}\right) \quad \text { (Point-slope form) } \\
& \text { or } \quad x\left(x_{1}-x_{2}\right)+y\left(y_{2}-y_{1}\right)-x_{1}\left(x_{2}-x_{1}\right)-y_{1}\left(y_{2}-y_{2}\right)=0
\end{aligned}
$$

Equations of the altitudes $B E$ and $C F$ are respectively (by symmetry)

$$
x\left(x_{1}-x_{1}\right)+y\left(y_{1}-y_{1}\right)-x_{2}\left(x_{1}-x_{1}\right)-y_{2}\left(y_{2}-y_{1}\right)=0
$$

and $x\left(x_{1}-x_{2}\right)+y\left(y_{1}-y_{2}\right)-x_{1}\left(x_{1}-x_{2}\right)-y_{1}\left(y_{2}-y_{1}\right)=0$
The three lines (1), (2) and (3) are concurrent if and only if

$$
\mathrm{D}=\left|\begin{array}{ccc}
x_{2}-x_{1} & y_{2}-y_{1} & -x_{1}\left(x_{2}-x_{1}\right)-y_{1}\left(y_{2}-y_{1}\right) \\
x_{1}-x_{1} & y_{2}-y_{1} & -x_{2}\left(x_{1}-x_{1}\right)-y_{2}\left(y_{2}-y_{1}\right) \\
x_{1}-x_{2} & y_{1}-y_{2} & -x_{1}\left(x_{1}-x_{2}\right)-y_{1}\left(y_{1}-y_{2}\right)
\end{array}\right| \text { is zero }
$$

Adding 2nd and 3rd rows to the 1st row of the determihant, we have

$$
\left|\begin{array}{ccc}
0 & 0 & 0 \\
x_{1}-x_{1} & y_{1}-y_{1} & -x_{2}\left(x_{1}-x_{1}\right)-y_{2}\left(y_{1}-y_{1}\right) \\
x_{1}-x_{2} & y_{1}-y_{2} & -x_{3}\left(x_{1}-x_{2}\right)-y_{3}\left(y_{1}-y_{2}\right)
\end{array}\right| = 0
$$

Thus the altitudes of a triangle are concurrent.

**Theorem:** Right bisectors of a triangle are concurrent.

**Proof.** Let \( A\left(x_{1}, y_{1}\right), B\left(x_{2}, y_{2}\right) \) and \( C\left(x_{3}, y_{3}\right) \) be the vertices of \( \Delta ABC \).

The midpoint \( D \) of \( BC \) has coordinates

$$
\left(\frac{x_2 + x_1}{2}, \frac{y_2 + y_3}{2}\right)
$$

Since the slope of \( BC \) is \( \frac{y_2 - y_3}{x_2 - x_3} \), the slope of the right bisector \( DO \) of \( BC \) is \( -\frac{x_2 - x_3}{y_2 - y_3} \).

### *Equation of the right bisector \( DO \) of \( BC \) is*

$$
y - \frac{y_2 + y_3}{2} = \frac{x_2 - x_3}{y_2 - y_3} \left( x \frac{x_2 + x_3}{2} \right) \quad \text{(Point-slope form)}
$$

or

$$
x \left(x_2 - x_3\right) + y \left(y_2 - y_3\right) - \frac{1}{2} \left( y_2^2 - y_3^2 \right) - \frac{1}{2} \left( x_2^2 - x_3^2 \right) = 0 \quad (1)
$$

*By symmetry, equations of the other two right bisectors \( EO \) and \( FO \) are respectively:*

$$
x \left(x_2 - x_3\right) + y \left(y_2 - y_3\right) - \frac{1}{2} \left( y_2^2 - y_3^2 \right) - \frac{1}{2} \left( x_2^2 - x_3^2 \right) = 0 \quad (2)
$$

and

$$
x \left(x_2 - x_3\right) + y \left(y_2 - y_3\right) - \frac{1}{2} \left( y_2^2 - y_3^2 \right) - \frac{1}{2} \left( x_2^2 - x_3^2 \right) = 0 \quad (3)
$$

The lines (1), (2) and (3) will be concurrent if and only if

$$
\begin{vmatrix}
x_2 - x_3 & y_2 - y_3 & -\frac{1}{2} \left( y_2^2 - y_3^2 \right) - \frac{1}{2} \left( x_2^2 - x_3^2 \right) \\
x_3 - x_1 & y_2 - y_3 & -\frac{1}{2} \left( y_2^2 - y_3^2 \right) - \frac{1}{2} \left( x_2^2 - x_3^2 \right) \\
x_1 - x_2 & y_1 - y_2 & -\frac{1}{2} \left( y_1^2 - y_3^2 \right) - \frac{1}{2} \left( x_1^2 - x_3^2 \right)
\end{vmatrix} = 0
$$

Adding 2nd and 3rd rows to 1st row of the determinant, we have

$$
\left|\begin{array}{ccc}
0 & 0 & 0 \\
x_2 - x_1 & y_2 - y_1 & -\frac{1}{2} \left( y_2^2 - y_3^2 \right) - \frac{1}{2} \left( x_2^2 - x_3^2 \right) \\
x_1 - x_2 & y_1 - y_2 & -\frac{1}{2} \left( y_1^2 - y_3^2 \right) - \frac{1}{2} \left( x_1^2 - x_3^2 \right)
\end{array}\right| = 0
$$

Thus the right bisectors of a triangle are concurrent.

**Note:** If equations of sides of the triangle are given, then intersection of any two lines gives a vertex of the triangle.

### 4.4.4 Distance of a point from a line

**Theorem:** The distance \( d \) from the point \( P\left(x_1, y_1\right) \) to the line \( l \)

$$
l : ax + by + c = 0 \quad (1)
$$

is given by

$$
d = \frac{\left| ax_1 + by_1 + c \right|}{\sqrt{a^2 + b^2}}
$$

**Proof:** Let \( l \) be non-vertical and non-horizontal line.

From \( P \), draw

$$
PQR \perp Os \text{ and } PM \perp l.
$$

Let the ordinate of \( Q \) be \( y_1 \) so that coordinates of \( Q \) are \( (x_1, y_1) \). Since \( Q \) lies on \( l \), we have \( ax_1 + by_1 + c = 0 \).

or $\quad y_{2}=\frac{-a x_{1}-c}{b}$
From the figure it is clear that $\angle M P Q=\alpha=$ the inclination of $I$.

$$
\text { Now } \tan \alpha=\text { slope of } I \frac{-a}{b}
$$

Therefore, $|\cos \alpha|=\frac{|b|}{\sqrt{a^{2}+b^{2}}}$
Thus $\quad|P M|=d=|P Q||\cos \alpha|=\left|y_{1}-y_{2}\right||\cos \alpha|$

$$
\begin{aligned}
& =\left|y_{1}-\frac{-a x_{1}-c}{b}\right| \frac{|b|}{\sqrt{a^{2}+b^{2}}} \\
& =\frac{\left|b y_{1}+a x_{1}+c\right|}{|b| \sqrt{a^{2}+b^{2}}} \quad|b| \quad \frac{\left|a x_{1}+b y_{1}+c\right|}{\sqrt{a^{2}+b^{2}}}
\end{aligned}
$$

If $I$ is horizontal, its equation is of the form $y=-\frac{c}{b}$ and the distance from $P\left(x_{1}, y_{1}\right)$ to $I$ is simply the difference of the $y$-values.

$$
\therefore \quad d=\left|y_{1}-\left(-\frac{c}{b}\right)\right|=\left|\frac{b y_{1}+c}{b}\right|
$$

Similarly, if the line is vertical and has equation: $x=\frac{-c}{a}$ then $d \quad \frac{\left|a x_{1}+c\right|}{a}$.
Note: If the point $P\left(x_{1}, y_{1}\right)$ lies on $I$, then the distance $d$ is zero, since $\left(x_{1}, y_{1}\right)$ satisfies the equation i.e., $a x_{1}+b y_{1}+c=0$

### 4.4.5 Distance Between two Parallel Lines

The distance between two parallel lines is the distance from any point on one of the lines to the other line.

Example: Find the distance between the parallel lines
$I: 2 x-5 y+13=0$ and
$I_{1}: 2 x-5 y+6=0$

Solution: First find any point on one of the lines, say $I_{1}$. If $x=1$ lies on $I_{1}$, then
$y=3$ and the point $(1,3)$ lies on it. The distance $d$ from $(1,3)$ to $I_{2}$ is

$$
d=\frac{|2(1)-5(3)+6|}{\sqrt{(-2)^{2}+5^{2}}} \quad \frac{|2-15+6|}{\sqrt{4+25}} \quad \frac{7}{\sqrt{29}}
$$

The distance between the parallel lines is $\frac{7}{\sqrt{29}}$.

### 4.4.6 Area of a Triangular Region Whose Vertices are Given

To find the area of a triangular region whose vertices are: $P\left(x_{1}, y_{1}\right), Q\left(x_{2}, y_{2}\right)$ and $R\left(x_{3}, y_{3}\right)$.
Draw perpendiculars $\overline{P L}, \overline{Q N}$ and $\overline{R M}$ on $x$-axis.
Area of the triangular region $P Q R$

- Area of the trapezoidal region $P L M R$
+ Area of the trapezoidal region $R M N Q$
- Area of the trapezoidal region $P L N Q$.
$=\frac{1}{2}\left(\left|\overline{P L}\right|+\left|\overline{R M}\right|\right)\left(\left|\overline{L M}\right|\right)+\frac{1}{2}\left(\left|\overline{R M}\right|+\left|\overline{Q N}\right|\right)\left(\left|\overline{M N}\right|\right)-\frac{1}{2}\left(\left|\overline{P L}\right|+\left|\overline{Q N}\right|\right)\left(\left|\overline{L N}\right|\right)$
$=\frac{1}{2}\left[\left(y_{1}+y_{2}\right)\left(x_{3}-x_{1}\right)+\left(y_{2}+y_{3}\right)\left(x_{2}-x_{3}\right)-\left(y_{1}+y_{2}\right)\left(x_{2}-x_{1}\right)\right]$
$=\frac{1}{2}\left(x_{1} y_{1}+x_{2} y_{2}-x_{1} y_{1}+x_{1} y_{3}+x_{2} y_{2}+x_{2} y_{2}-x_{2} y_{3}-x_{2} y_{1}+x_{1} y_{1}+x_{1} y_{2}\right)$
$=\frac{1}{2}\left(x_{1} y_{1}-x_{1} y_{3}+x_{2} y_{2}-x_{2} y_{2}-x_{2} y_{1}+x_{1} y_{2}\right)$
Thus required area $A$ is given by:
$\Delta=\frac{1}{2}\left(x_{1}\left(y_{2}-y_{3}\right)+x_{2}\left(y_{3}-y_{1}\right)+x_{3}\left(y_{1}-y_{2}\right)\right)$

Forollary: If the points $P, Q$ and $R$ are collinear, then
$\Delta=0$

Note: In numerical problems, if sign of the area is negative, then it is to be omitted.
Example 1: Find the area of the region bounded by the triangle with vertices $(a, b+c)$, $(a, b-c)$ and $(-a, c)$.
Solution: Required area $\Delta$ is

$$
\begin{aligned}
& \Delta=\frac{1}{2}\left[\begin{array}{ll}
a & b+c \\
a & b-c
\end{array}\right] \\
& \left.\begin{array}{ll}
a \\
-a & c
\end{array}\right] \\
& =\frac{1}{2}\left[\begin{array}{ll}
a & b+c \\
a & c
\end{array}\right]
\end{aligned}
$$

Trapezium:
A quadrilateral having two parallel and two non-parallel sides.
Area of trapezoidal region:
$\frac{1}{2}$ (sum of $\|$ sides) /distance between $\|$ sides
$=\frac{1}{2}[-2 c(a+a)]$, expanding by the second row
$=-2 c a$
Thus $\Delta=2 c a$
Example 2: By considering the area of the region bounded by the triangle with vertices $A(1,4), B(2,-3)$ and $C(3,-10)$
check whether the three points are collinear or not.
Solution: Area $\Delta$ of the region bounded by the triangle $A B C$ is

$$
\begin{aligned}
& \Delta=\frac{1}{2}\left[\begin{array}{ll}
1 & 4 \\
2 & -3 \\
3 & -10
\end{array}\right] \quad=\frac{1}{2}\left[\begin{array}{cc}
1 & 4 \\
1 & -7 \\
3 & -14
\end{array}\right] \text { by } R_{2}-R_{1} \text { and } R_{3}-R_{1} \\
& =\frac{1}{2}[1(-14+14)] \text {, expanding by third column } \\
& =0
\end{aligned}
$$

Thus the points are collinear.

## EXERCISE 4.3

1. Find the slope and inclination of the line joining the points:
(i) $(-2,4) ;(5,11)$
(ii) $(3,-2) ;(2,7)$
(iii) $(4,6) ;(4,8)$

Sketch each line in the plane.
2. In the triangle $A(8,6) B(-4,2), C(-2,-6)$, find the slope of
(i) each side of the triangle
(ii) each median of the triangle
(iii) each altitude of the triangle.
3. By means of slopes, show that the following points lie on the same line:
(a) $(-1,-3) ;(1,5) ;(2,9)$
(b) $(4,-5) ;(7,5) ;(10,15)$
(c) $(-4,6) ;(3,8) ;(10,10)$
(d) $(a, 2 b):(c, a+b) ;(2 c-a, 2 a)$
4. Find $k$ so that the line joining $A(7,3) ; B(k,-6)$ and the line joining $C(-4,5) ; D(-6,4)$ are (i) parallel (ii) perpendicular.
5. Using slopes, show that the triangle with its vertices $A(6,1), B(2,7)$ and $C(-6,-7)$ is a right triangle.
6. The three points $A(7,-1), B(-2,2)$ and $C(1,4)$ are consecutive vertices of a parallelogram. Find the fourth vertex.
7. The points $A(-1,2), B(3,-1)$ and $C(6,3)$ are consecutive vertices of a rhombus. Find the fourth vertex and show that the diagonals of the rhombus are perpendicular to each other.
8. Two pairs of points are given. Find whether the two lines determined by these points are :
(i) parallel
(ii) perpendicular
(iii) none.
(a) $(1,-2),(2,4)$ and $(4,1),(-8,2)$
(b) $(-3,4),(6,2)$ and $(4,5),(-2,-7)$
9. Find an equation of
(a) the horizontal line through $(7,-9)$
(b) the vertical line through $(-5,3)$

(c) the line bisecting the first and third quadrants.
(d) the line bisecting the second and fourth quadrants.
10. Find an equation of the line
(a) through $A(-6,5)$ having slope 7
(b) through $(8,-3)$ having slope 0
(c) through $(-8,5)$ having slope undefined
(d) through $(-5,-3)$ and $(9,-1)$
(e) $y$-intercept: -7 and slope: -5
(f) $x$-intercept: -3 and $y$-intercept: 4
(g) $x$-intercept: -9 and slope: -4
11. Find an equation of the perpendicular bisector of the segment joining the points $A(3,5)$ and $B(9,8)$.
12. Find equations of the sides, altitudes and medians of the triangle whose vertices are $A(-3,2), B(5,4)$ and $C(3,-8)$.
13. Find an equation of the line through $(-4,-6)$ and perpendicular to a line having slope $\frac{-3}{2}$
14. Find an equation of the line through $(11,-5)$ and parallel to a line with slope -24 .
15. The points $A(-1,2), B(6,3)$ and $C(2,-4)$ are vertices of a triangle. Show that the line joining the midpoint $D$ of $A B$ and the midpoint $E$ of $A C$ is parallel to $B C$ and $D E=\frac{1}{2} B C$.
16. A milkman can sell 560 litres of milk at Rs. 12.50 per litre and 700 litres of milk at Rs. 12.00 per litre. Assuming the graph of the sale price and the milk sold to be a straight line, find the number of litres of milk that the milkman can sell at Rs. 12.25 per litre.
17. The population of Pakistan to the nearest million was 60 million in 1961 and 95 million in 1981. Using $t$ as the number of years after 1961, find an equation of the line that gives the population in terms of $t$. Use this equation to find the population in (a) 1947 (b) 1997.
18. A house was purchased for Rs. 1 million in 1980. It is worth Rs. 4 million in 1996. Assuming that the value increased by the same amount each year, find an equation that gives the value of the house after $t$ years of the date of purchase. What was its value in 1990?
19. Plot the Celsius $(C)$ and Fahrenheit $(F)$ temperature scales on the horizontal axis and the vertical axis respectively. Draw the line joining the freezing point and the boiling point of water. Find an equation giving $F$ temperature in terms of $C$.
20. The average entry test score of engineering candidates was 592 in the year 1998 while the score was 564 in 2002. Assuming that the relationship between time and score is linear, find the average score for 2006.
21. Convert each of the following equation into
(i) Slope intercept form
(ii) two intercept form
(iii) normal form
(a) $2 x-4 y+11=0$
(b) $4 x+7 y-2=0$
(c) $15 y-8 x+13=0$

Also find the length of the perpendicular from $(0,0)$ to each line.
22. In each of the following check whether the two lines are
(i) parallel
(ii) perpendicular
(iii) neither parallel nor perpendicular
(a) $2 x+y-3=0$
$4 x+2 y+5=0$
(b) $3 y+2 x+5$
$3 \# 2 y \# 0$
(c) $4 y+2 x-1=0$
$x-2 y-7=0$
(d) $4 x-y+2=0-$
$\triangleright \triangleleft 2 x \quad 3 y \quad 1 \quad 0$
(e) $12 x+35 y-7=0$
$105 x-36 y+11=0$
23. Find the distance between the given parallel lines. Sketch the lines. Also find an equation of the parallel line lying midway between them.
(a) $3 x-4 y+3=0$
$3 x-4 y+7=0$
(b) $12 x+5 y-6=0$
$12 x+5 y+13=0$
(c) $x+2 y-5=0+$
$\triangleright \quad 2 x \quad 4 y \quad 1$

**24.** Find an equation of the line through (−4, 7) and parallel to the line 2*x* − 7*y* + 4 = 0.

**25.** Find an equation of the line through (5, −8) and perpendicular to the join of *A* (−15, −8), *B* (10, 7).

**26.** Find equations of two parallel lines perpendicular to 2*x* − *y* + 3 = 0 such that the product of the *x*-and *y*-intercepts of each is 3.

**27.** One vertex of a parallelogram is (1, 4); the diagonals intersect at (2, 1) and the sides have slopes 1 and $$\frac{-1}{2}$$. Find the other three vertices.

**28.** Find whether the given point lies above or below the given line
- (a) (5, 8); 2*x* − 3*y* + 6 = 0
- (b) (−7, 6); 4*x* + 3*y* − 9 = 0

**29.** Check whether the given points are on the same or opposite sides of the given line.
- (a) (0, 0) and (−4, 7); 6*x* − 7*y* + 70 = 0
- (b) (2, 3) and (−2, 3); 3*x* − 5*y* + 8 = 0

**30.** Find the distance from the point *P*(6, −1) to the line 6*x* − 4*y* + 9 = 0.

**31.** Find the area of the triangular region whose vertices are *A* (5, 3), *B* (−2, 2), *C* (4, 2).

**32.** The coordinates of three points are *A*(2, 3), *B*(−1, 1) and *C*(4, −5). By computing the area bounded by *ABC* check whether the points are collinear.

### **4.5. ANGLE BETWEEN TWO LINES**

Let *l<sub>1</sub>* and *l<sub>2</sub>* be two intersecting lines, which meet at a point *P*. At the point *P* two supplementary angles are formed by the lines *l<sub>1</sub>* and *l<sub>2</sub>*.

Unless *l<sub>1</sub>* ⊥ *l<sub>2</sub>* one of the two angles is acute. The angle from *l<sub>1</sub>* to *l<sub>2</sub>* is the angle *θ* through which *l<sub>1</sub>* is rotated anti-clockwise about the point *P* so that it coincides with *l<sub>2</sub>*.

In the figure below *θ* is angle of intersection of the two lines and it is measured from *l<sub>1</sub>* to *l<sub>2</sub>* in counterclockwise direction, *ψ* is also angle of intersection but it is measured from *l<sub>1</sub>* to *l<sub>1</sub>*.

With this convention for angle of intersection, it is clear that the inclination of a line is the angle measured in the counterclockwise direction from the positive *x*-axis to the line, and it tallies with the earlier definition of the inclination of a line.

**Theorem:** Let *l<sub>1</sub>* and *l<sub>2</sub>* be two non-vertical lines such that they are not perpendicular to each other. If *m<sub>1</sub>* and *m<sub>2</sub>* are the slopes of *l<sub>1</sub>* and *l<sub>2</sub>* respectively: the angle *θ* from *l<sub>1</sub>* to *l<sub>2</sub>* is given by:

$$
\tan \theta = \frac{m_1 - m_1}{1 + m_1 m_2}
$$

**Proof:** From the figure, we have

$$
\alpha_2 = \alpha_1 + \theta
$$

or

$$
\theta = \alpha_2 - \alpha_1
$$

$$
\tan \theta = \tan(\alpha_2 - \alpha_1) = \frac{\tan \alpha_2 - \tan \alpha_1}{1 + \tan \alpha_1 \tan \alpha_2} = \frac{m_2 - m_1}{1 + m_1 m_2}
$$

$$
\therefore \quad \tan \theta = \tan(\alpha_2 - \alpha_1) = \frac{\tan \alpha_2 - \tan \alpha_1}{1 + \tan \alpha_1 \tan \alpha_2} = \frac{m_2 - m_1}{1 + m_1 m_2}
$$

**Corollary 1.** *l<sub>1</sub>* || *l<sub>2</sub>* if and only if *m<sub>1</sub>* = *m<sub>2</sub>*

$$
\Rightarrow \quad \tan \theta = 0 \quad \frac{m_1 - m_1}{1 + m_1 m_2}
$$

$$
\Rightarrow \quad m_2 = m_1
$$

**Corollary 2.** *l<sub>1</sub>* ⊥ *l<sub>2</sub>* iff 1 + *m<sub>1</sub>m<sub>2</sub>* = 0

$$
\Rightarrow \quad \tan \theta = \frac{m_2 - m_1}{1 + m_1 m_2} = \tan \frac{\theta}{2} = + \quad = 1 \quad m_1 m_2 \quad 0
$$

These two results have already been stated in 4.3.1.

**Example 1:** Find the angle from the line with slope $$\frac{-7}{3}$$ to the line with slope $$\frac{5}{2}$$.

**Solution:** Here *m<sub>2</sub>* = $$\frac{5}{2}$$, *m<sub>1</sub>* = $$\frac{-7}{3}$$. If *θ* is measure of the required angle, then

$$
\tan \theta=\frac{\frac{5}{2}-\left(\frac{-7}{3}\right)}{1+\frac{5}{2}\left(\frac{-7}{3}\right)}=\frac{29}{-29}=-1
$$

Thus $\theta=135^{\circ}$
Example 2: Find the angles of the triangle whose vertices are

$$
A(-5,4), B(-2,-1), C(7,-5)
$$

Solution: Let the slopes of the sides $A B, B C$ and $C A$ be denoted by $m_{x}, m_{y}, m_{z}$ respectively. Then

$$
m_{x}=\frac{4+1}{-5+2}-\frac{-5}{3}, m_{y}=\frac{-5+1}{7+2}=\frac{-4}{9}, m_{z}=\frac{-5-4}{7+5}=\frac{-3}{4}
$$

Now angle $A$ is measured from $A B$ to $A C$.

$$
\tan A=\frac{m_{x}-m_{y}}{1+m_{x} m_{y}}=\frac{\frac{-3}{4}+\frac{5}{3}}{1+\left(\frac{-3}{4}\right)\left(\frac{-5}{3}\right)} \quad \frac{11}{27} \quad \text { or } \quad m \underbrace{\underline{A}}_{22.2^{\circ}}
$$

The angle $B$ is measured from $B C$ to $B A$

$$
\therefore \quad \tan B=\frac{m_{x}-m_{y}}{1+m_{x} m_{y}}=\frac{\frac{-5}{3}+\frac{4}{9}}{1+\left(\frac{-5}{3}\right)\left(\frac{-4}{9}\right)}=\frac{-33}{47} \quad \text { or } \quad m \underbrace{B}_{B}=144.9^{\circ}
$$

The angle $C$ is measured from $C A$ to $C B$.

$$
\therefore \quad \tan A=\frac{m_{x}-m_{y}}{1+m_{x} m_{y}}=\frac{\frac{-4}{9}+\frac{3}{4}}{1+\left(\frac{-4}{9}\right)\left(\frac{-3}{4}\right)}=\frac{11}{48} \quad \text { or } \quad m \underbrace{C}_{C}=12.9^{\circ}
$$

# 4.5.1 Equation of a Straight Line in Matrix form

It is easy to solve two or three simultaneous linear equations by elementary methods. If the number of equations and variables become large, the solution of the equations by ordinary method becomes very difficult. In such a case, given equations are written in matrix form and solved.

## One Linear Equation:

A linear equation

$$
l: a x+b y+c=0
$$

in two variables $x$ and $y$ has its matrix form as:

$$
\begin{aligned}
& {[a x+b y]=[-c]} \\
& \text { or } \quad\left[\begin{array}{ll}
a & b
\end{array}\right]\left[\begin{array}{l}
x \\
y
\end{array}\right]=[-c] \\
& \text { or } \quad A X \times C
\end{aligned}
$$

where $\quad A=[a \quad b], \quad X=\left[\begin{array}{l}x \\ y\end{array}\right]$ and $C=[-c]$

## A System of Two Linear Equations:

A system of two linear equations

$$
\begin{aligned}
& l_{1}: a_{1} x+b_{1} y+c=0 \\
& l: a_{2} x+b_{2} y+c=0
\end{aligned}
$$

in two variables $x$ and $y$ can be written in matrix form as:

$$
\begin{aligned}
& {\left[\begin{array}{l}
a_{1} x+b_{1} y \\
a_{2} x+b_{2} y
\end{array}\right] \times\left[\begin{array}{l}
-c_{1} \\
-c_{2}
\end{array}\right]} \\
& \text { or } \\
& \left[\begin{array}{ll}
a_{1} & b_{1} \\
a_{2} & b_{2}
\end{array}\right]\left[\begin{array}{l}
x \\
y
\end{array}\right]=\left[\begin{array}{l}
-c_{1} \\
-c_{2}
\end{array}\right] \\
& \text { or } \\
& A X \times C
\end{aligned}
$$

$$
A X \times C
$$

where $\quad A=\left[\begin{array}{ll}a_{1} & b_{1} \\ a_{2} & b_{2}\end{array}\right], \quad X\left[\begin{array}{l}x \\ y\end{array}\right]$ and $C=\left[\begin{array}{l}-c_{1} \\ -c_{2}\end{array}\right]$
Equations (2) have a solution iff $\operatorname{det} A \neq 0$.

## A System of Three Linear Equations:

A system of three linear equations

$$
\begin{aligned}
& l_{1}: a_{1} x+b_{1} y+c_{1}=0 \\
& l_{2}: a_{2} x+b_{2} y+c_{2}=0 \\
& l_{3}: a_{3} x+b_{3} y+c_{3}=0
\end{aligned}
$$

in two variables $y$ and $y$ takes the matrix form as

$$
\begin{aligned}
& {\left[\begin{array}{lll}
a_{1} x+b_{1} y+c_{1} \\
a_{2} x+b_{2} y+c_{2}
\end{array}\right]=\left[\begin{array}{l}
0 \\
0 \\

\end{array}\right]} \\
& \text { or } \quad\left[\begin{array}{llll}
a_{1} & b_{1} & c_{1}
\end{array}\right]\left[\begin{array}{l}
x \\
y \\
a_{2}
\end{array}\right]=\left[\begin{array}{l}
0 \\
0 \\

\end{array}\right]
\end{aligned}
$$

or

$$
\left[\begin{array}{lll}
a_{1} & b_{1} & c_{1}
\end{array}\right]
$$

If the matrix

$$
\left[\begin{array}{lll}
a_{1} & b_{1} & c_{1}
\end{array}\right] \text { is singular, then the lines (5) are concurrent }
$$

is singular, then the lines (5) are concurrent
a $_{1} \quad b_{1} \quad c_{1}$ and so the system (5) has a unique solution.
Example 1: Express the system

$$
\begin{aligned}
& 3 x+4 y-7=0 \\
& 2 x-5 y+8=0 \\
& x+y-3=0
\end{aligned}
$$

in matrix form and check whether the three lines are concurrent
Solution. The matrix form of the system is

$$
\left[\begin{array}{rrrr}
3 & 4 & -7 \\
2 & -5 & 8 \\
1 & 1 & -3
\end{array}\right]\left[\begin{array}{l}
x \\
y \\

\end{array}\right]=\left[\begin{array}{l}
0 \\
0 \\

\end{array}\right]
$$

Coefficient matrix of the system is

$$
A=\left[\begin{array}{rrrr}
3 & 4 & -7 \\
2 & 5 & 8 \\
1 & 1 & -3
\end{array}\right] \text { and } \operatorname{det} A\left[\begin{array}{lll}
0 & 1 & 2 \\
0 & & 7 & 14 \\
1 & & 1 & -3
\end{array}\right] \begin{aligned}
& \text { by } R_{1}-3 R_{2} \\
& \text { and } R_{2}-2 R_{3}
\end{aligned}
$$

and $\operatorname{det} A=1(14+14)=28 \neq 0$
As $A$ is non-singular, so the lines are not concurrent.
Example 2: Find a system of linear equations corresponding to the matrix form

$$
\left[\begin{array}{llll}
1 & 2 & 5 \\
3 & 5 & 1 \\
4 & 7 & 6
\end{array}\right]\left[\begin{array}{l}
x \\
y \\

\end{array}\right]=\left[\begin{array}{l}
0 \\
0 \\

\end{array}\right]
$$

Are the lines represented by the system concurrent?
Solution: Multiplying the matrices on the L.H.S. of (1), we have

$$
\left[\begin{array}{l}
x+2 y+5 \\
3 x+5 y+1 \\
4 x+7 y+6
\end{array}\right]=\left[\begin{array}{l}
0 \\
0 \\

\end{array}\right]
$$

By using the definition of equality of two matrices, we have from (2),

$$
\begin{aligned}
& x+2 y+5=0 \\
& 3 x+5 y+1=0 \\
& 4 x+7 y+6=0
\end{aligned}
$$

as the required system of equations. The coefficient matrix $A$ of the system is such that

$$
\operatorname{det} A=\left[\begin{array}{llll}
1 & 2 & 5 \\
3 & 5 & 1 \\
4 & 7 & 6
\end{array}\right]=\left[\begin{array}{lll}
1 & 2 & 5 \\
0 & -1 & -14 \\
0 & -1 & -14
\end{array}\right]=0
$$

Thus the lines of the system are concurrent.

## EXERCISE 4.4

1. Find the point of intersection of the lines
(i) $x-2 y+1=0-\quad$ and $2 x \quad y \quad 2 \quad 0$
(ii) $3 x+y+12=0+\quad$ and $=\quad x \quad 2 y \quad 1 \quad 0$
(iii) $x+4 y-12=0-\quad$ and $=\quad x \quad 3 y \quad 3 \quad 0$
2. Find an equation of the line through
(i) the point $(2,-9)$ and the intersection of the lines $2 x+5 y-8=0-\quad$ and $=3 x \quad 4 y \quad 6 \quad 0$
(ii) the intersection of the lines $x-y-4=0+\quad+$ and $7 x \quad y \quad 20 \quad 0 \quad$ and
(a) parallel
(b) perpendicular to the line $6 x+y-14=0$
(iii) through the intersection of the lines $x+2 y+3=0,3 x+4 y+7=0$ and making equal intercepts on the axes.
3. Find an equation of the line through the intersection of $16 x-10 y-33=0 ; 12 x-14 y-29=0 \quad$ and the intersection of $x-y+4=0 \quad ; \quad x-7 y+2=0$
4. Find the condition that the lines $y=m_{1} x+c_{1} ; y=m_{2} x+c_{2}$ and $y=m_{3} x+c_{3}$ are concurrent.
5. Determine the value of $p$ such that the lines $2 x-3 y-1=0$, $3 x-y-5=0$ and $3 x+4 y+8=0$ meet at a point.
6. Show that the lines $4 x-3 y-8=0,3 x-4 y-6=0$ and $x-y-2=0$ are concurrent and the third-line bisects the angle formed by the first two lines.
7. The vertices of a triangle are $A(-2,3), B(-4,1)$ and $C(3,5)$. Find coordinates of the
(i) centroid
(ii) orthocentre
(iii) circumcentre of the triangle

Are these three points collinear?
8. Check whether the lines
$4 x-3 y-8=0 ; \quad 3 x-4 y-6=0 ; \quad x-y-2=0$
are concurrent. If so, find the point where they meet
9. Find the coordinates of the vertices of the triangle formed by the lines $x-2 y-6=0 ; \quad 3 x-y+3=0 ; \quad 2 x+y-4=0$
Also find measures of the angles of the triangle.
10. Find the angle measured from the line $l_{1}$ to the line $l_{2}$ where
(a) $l_{1}:$ Joining $(2,7)$ and $(7,10)$
$l_{2}:$ Joining $(1,1)$ and $(-5,3)$
(b) $l_{1}:$ Joining $(3,-1)$ and $(5,7)$
$l_{2}:$ Joining $(2,4)$ and $(-8,2)$
Also find the acute angle in each case.
(c) $l_{1}:$ Joining $(1,-7)$ and $(6,-4)$
$l_{2}:$ Joining $(-1,2)$ and $(-6,-1)$
(d) $l_{1}:$ Joining $(-9,-1)$ and $(3,-5)$
$l_{2}:$ Joining $(2,7)$ and $(-6,-7)$
11. Find the interior angles of the triangle whose vertices are
(a) $A(-2,11), B(-6,-3),(4,-9)$
(b) $A(6,1), \quad B(2,7), C(-6,-7)$
(c) $A(2,-5), \quad B(-4,-3),(-1,5)$
(d) $A(2,8), \quad B(-5,4), C(4,-9)$
12. Find the interior angles of the quadrilateral whose vertices are $A(5,2), B(-2,3)$, $C(-3,-4)$ and $D(4,-5)$
13. Show that the points
$A(0,0), B(2,1), C(3,3), D(1,2)$ are the vertices of a rhombus.
Find its interior angles.
14. Find the area of the region bounded by the triangle whose sides are $7 x-y-10=0 ; \quad 10 x+y-14=0 ; \quad 3 x+2 y+3=0$
15. The vertices of a triangle are $A(-2,3), B(-4,1)$ and $C(3,5)$. Find the centre of the circumcircle of the triangle.

16. Express the given system of equations in matrix form. Find in each case whether the lines are concurrent.
(a) $x+3 y-2=0 ; \quad 2 x-y+4=0 ; \quad x-11 y+14=0$
(b) $2 x+3 y+4=0 ; \quad x-2 y-3=0 ; \quad 3 x+y-8=0$
(c) $3 x-4 y-2=0 ; \quad x+2 y-4=0 ; \quad 3 x-2 y+5=0$.
17. Find a system of linear equations corresponding to the given matrix form. Check whether the lines represented by the system are concurrent.
(a) $\left[\begin{array}{cccc|c}1 & 0 & -1 & x \\ 2 & 0 & 1 & y & 0 \\ 0 & -1 & 6 & 1 & 0\end{array}\right]$
(b) $\left[\begin{array}{cccc|c}1 & 1 & 2 & x \\ 2 & 4 & -3 & y & 0 \\ 3 & 6 & -5 & 1\end{array}\right]$
$=\left[\begin{array}{c}0 \\ 0 \\ 0\end{array}\right]$

### 4.6 HOMOGENEOUS EQUATION OF THE SECOND DEGREE IN TWO VARIABLES

We have already seen that if a graph is a straight line, then its equation is a linear equation in the variables $x$ and $y$. Conversely, the graph of any linear equation in $x$ and $y$ is a straight line.

Suppose we have two straight lines represented by

$$
a_{x} x+b_{y} y+c_{z}=0
$$

and

$$
a_{y} x+b_{z} y+c_{x}=0
$$

Multiplying equations (1) and (2), we have

$$
\left(a_{x} x+b_{y} y+c_{z}\right)\left(a_{y} x+b_{z} y+c_{x}\right)=0
$$

It is a second degree equation in $x$ and $y$.
Equation (3) is called joint equation of the pair of lines (1) and (2). On the other hand, given an equation of the second degree in $x$ and $y$, say

$$
a x^{2}+2 h x y+b y^{2}+2 g x+2 f y+c=0
$$

where $a \neq 0$, represents equations of a pair of lines if (4) can be resolved into two linear factors. In this section, we shall study special joint equations of pairs of lines which pass through the origin.

Let $y=m_{1} x$ and $y=m_{2} x$ be two lines passing through the origin. Their joint equation is: $\left(y-m_{1} x\right)\left(y-m_{2} x\right)=0$
or $\quad y^{2}-\left(m_{1}+m_{2}\right) x y+m_{1} m_{2} x^{2}=0$
Equation (5) is a special type of a second degree homogeneous equation.

### 4.6.1 Homogeneous Equation

Let $f(x, y)=0$
be any equation in the variables $x$ and $y$. Equation (1) is called a homogeneous equation of degree $n$ (a positive integer) if

$$
f(k x, k y)=k^{n} f(x, y)
$$

for some real number $k$.
For example, in equation (5) above if we replace $x$ and $y$ by $k x$ and $k y$ respectively, we have

$$
\begin{aligned}
& k^{2} y^{2}-k^{2}\left(m_{1}+m_{2}\right) x y+k^{2} m_{1} m_{2} x^{2}=0 \\
\text { or } & k^{2}\left[y^{2}-\left(m_{1}+m_{2}\right) x y+m_{1} m_{2} x^{2}\right]=0 \quad \text { i.e., } \quad k^{2} f(x, y) \quad 0
\end{aligned}
$$

Thus (5) is a homogeneous equation of degree 2.

$$
a x^{2}+2 h x y+b y^{2}=0
$$

A general second degree homogeneous equation can be written as:

$$
a x^{2}+2 h x y+b y^{2}=0
$$

provided $a, h$ and $b$ are not simultaneously zero.

Theorem: Every homogenous second degree equation

$$
a x^{2}+2 h x y+b y^{2}=0
$$

represents a pair of lines through the origin. The lines are
(i) real and distinct, if $h^{2}>a b$
(ii) real and coincident, if $h \quad a b$
(iii) imaginary, if $h^{2}<a b$

Proof: Multiplying (1) by b and re-arranging the terms, we have

$$
b^{2} y^{2}+2 b k x y+a b x^{2}=0
$$

or $\quad b^{2} y^{2}+2 b k x y+h^{3} x^{2}-h^{3} x^{2}+a b x^{2}=0$
or $\quad(b y+h x)^{3}-x^{2}\left(h^{3}-a b\right)=0$
or $\quad(b y+h x+x \sqrt{h^{3}-a b})(b y+h x-x \sqrt{h^{3}-a b})=0$
Thus (1) represents a pair of lines whose equations are:

$$
b y+x\left(h+\sqrt{h^{3}-a b}\right)=0
$$

and $b y+x\left(h-\sqrt{h^{3}-a b}\right)=0$
Clearly, the lines (2) and (3) are
(i) real and distinct if $h^{3}>a b$. (ii) real and coincident, if $h^{3}=a b$.
(iii) imaginary, if $h^{3}<a b$.

It is interesting to note that even in case the lines are imaginary, they intersect in a real point viz $(0,0)$ since this point lies on their joint equation (1).

Example: Find an equation of each of the lines represented by

$$
20 x^{2}+17 x y-24 y^{2}=0
$$

Solution. The equation may be written as

$$
\begin{aligned}
& 24\left(\frac{y}{x}\right)^{2}-17\left(\frac{y}{x}\right)-20=0 \\
& \Rightarrow \quad \frac{y}{x}=\frac{17 \pm \sqrt{289+1920}}{48}-\frac{17 \pm 47}{48}-\frac{4}{3}-\frac{-5}{8} \\
& \Rightarrow \quad y=\frac{4}{3} x \quad \text { and } \quad y=\frac{-5}{8} x \\
& \Rightarrow \quad 4 x-3 y=0 \quad \text { and } \quad 5 x+8 y=0
\end{aligned}
$$

version: 1.1

### 4.6.2 To find measure of the angle between the lines represented by

$$
a x^{2}+2 h x y+b y^{2}=0
$$

We have already seen that the lines represented by (1) are

$$
b y+x\left(h+\sqrt{h^{3}-a b}\right)=0
$$

and $\quad b y+x\left(h-\sqrt{h^{3}-a b}\right)=0$
Now slopes of (2) and (3) are respectively given by:

$$
m_{1}=\frac{-\left(h+\sqrt{h^{3}-a b}\right)}{b}, \text { and } m_{2}=\frac{-\left(h-\sqrt{h^{3}-a b}\right)}{b}
$$

Therefore, $m_{1}+m_{2}=\frac{-2 h}{b} \quad$ and $m_{1} m_{2} \quad \frac{a}{b}$
If $\theta$ is measure of the angle between the lines (2) and (3), then

$$
\tan \theta=\frac{m_{1}-m_{2}}{1+m_{1} m_{2}}=\sqrt{\frac{\left(m_{1}+m_{2}\right)^{2}-4 m_{1} m_{2}}{1+m_{1} m_{2}}} \cdot \frac{\sqrt{\frac{4 h^{3}-4 a}{b^{3}}-\frac{a}{b}}}{1+\frac{a}{b}} \cdot \frac{2 \sqrt{h^{3}-a b}}{a+b}
$$

The two lines are parallel, if $\theta=0$, so that $\tan \theta=0$ which implies $\boldsymbol{h}^{2}-\boldsymbol{a} \boldsymbol{b}=\mathbf{0}$, which is the condition for the lines to be coincident.
If the lines are orthogonal, then $\theta=90^{\circ}$, so that $\tan \theta$ is not defined. This implies $\boldsymbol{a}+\boldsymbol{b}=\mathbf{0}$. Hence the condition for (1) to represent a pair of orthogonal (perpendicular) lines is that sum of the coefficients of $\boldsymbol{x}^{\mathbf{2}}$ and $\boldsymbol{y}^{\mathbf{2}}$ is $\mathbf{0}$.

Example 1: Find measure of the angle between the lines represented by

$$
x^{2}-x y-6 y^{2}=0
$$

Solution. Here $a=1 ; \quad b=\frac{1}{2}, b \quad 6$

If $\theta$ is measure of the angle between the given lines, then

$$
\tan \theta=\frac{2 \sqrt{b^{2}-a b}}{a+b}=\frac{2 \sqrt{\frac{1+6}{4}}}{-5}=-1 \Rightarrow \theta=135^{\circ}
$$

Acute angle between the lines $=180^{\circ}-\theta=180^{\circ}-135^{\circ}=45^{\circ}$
Example2: Find a joint equation of the straight lines through the origin perpendicular to the lines represented by

$$
x^{2}+x y-6 y^{2}=0
$$

Solution: (1) may be written as

$$
(x-2 y)(x+3 y)=0
$$

Thus the lines represented by (1) are

$$
x-2 y=0
$$

and $\quad x+3 y=0$
The line through $(0,0)$ and perpendicular to (2) is

$$
y \Rightarrow 2 x \text { or } \quad+y \quad \nRightarrow x \quad 0
$$

Similarly, the line through $(0,0)$ and perpendicular to (3) is

$$
y=3 x-\text { or } \quad y \quad 3 x \quad 0
$$

Joint equation of the lines (4) and (5) is

$$
(y+2 x)(y-3 x)=0 \quad \text { or } \quad y^{2}-x y-6 x^{2}=0
$$

## EXERCISE 4.5

Find the lines represented by each of the following and also find measure of the, angle between them (Problems 1-6):

1. $10 x^{2}-23 x y-5 y^{2}=0$
2. $3 x^{2}+7 x y+2 y^{2}=0$
3. $9 x^{2}+24 x y+16 y^{2}=0$
4. $2 x^{2}+3 x y-5 y^{2}=0$
5. $6 x^{2}-19 x y+15 y^{2}=0$
6. $x^{2}+2 x y \sec \alpha+y^{2}=0$
7. Find a joint equation of the lines through the origin and perpendicular to the lines:

$$
x^{2}-2 x y \tan \alpha-y^{2}=0
$$

8. Find a joint equation of the lines through the origin and perpendicular to the lines:

$$
a x^{2}+2 b x y+b y^{2}=0
$$

9. Find the area of the region bounded by:

$$
10 x^{2}-x y-21 y^{2}=0 \text { and } \quad x+y+1=0
$$

# CHAPTER

## Linear Inequalities and Linear Programming

## 5.1 INTRODUCTION

Many real life problems involve linear inequalities. Here we shall consider those problems (relating to trade, industry and agriculture etc.) which involve systems of linear inequalities in two variables. Linear inequalities in such problems are used to prescribe limitations or restrictions on allocation of available resources (material, capital, machine capacities, labour hours, land etc.). In this chapter, our main goal will be to optimize (maximize or minimize) a quantity under consideration subject to certain restrictions.

The method under our discussion is called the linear programming method and it involves solutions of certain linear inequalities.

### 5.2 LINEAR INEQUALITIES

Inequalities are expressed by the following four symbols;
$>$ (greater than); < (less than); $\geq$ (greater than or equal to); $\leq$ (less than or equal to)
For example (i) $a x<b$ (ii) $a x+b \geq c$ (iii) $a x+b y>c$ (iv) $a x+b y \leq c$ are inequalities. Inequalities (i) and (ii) are in one variable while inequalities (iii) and (iv) are in two variables.

The following operations will not affect the order (or sense) of inequality while changing it to simpler equivalent form:
(i) Adding or subtracting a constant to each side of it.
(ii) Multiplying or dividing each side of it by a positive constant.

Note that the order (or sense) of an inequality is changed by multiplying or dividing its each side by a negative constant.

Now for revision we consider inequality, $x<\frac{3}{2}$
All real numbers $<\frac{3}{2}$ are in the solution set of (A).
Thus the interval $\left(-\infty, \frac{3}{2}\right)$ or $-\infty<x<\frac{3}{2}$ is the solution set of the
inequality (A) which is shown in the figure 5.21

$$
-5 \quad-4 \quad-3 \quad-2 \quad-1 \quad 0 \quad 1 \quad 2 \quad 3 \quad 4 \quad 5
$$

We conclude that the solution set of an inequality consists of all solutions of the inequality.

### 5.2.1 Graphing of A Linear Inequality in Two Variables

Generally a linear inequality in two variables $x$ and $y$ can be one of the following forms: $a x+b y<c ; \quad a x+b y>c ; \quad a x+b y \leq c ; \quad a x+b y \geq c$
where $a, b, c$ are constants and $a, b$ are not both zero.
We know that the graph of linear equation of the form
$a x+b y=c$ is a line which divides the plane into two disjoint regions as stated below:
(1) The set of ordered pairs $(x, y)$ such that $a x+b y<c$
(2) The set of ordered pairs $(x, y)$ such that $a x+b y>c$

The regions (1) and (2) are called half planes and the line $a x+b y=c$ is called the boundary of each half plane.

Note that a vertical line divides the plane into left and right half planes while a nonvertical line divides the plane into upper and lower half planes.

A solution of a linear inequality in $x$ and $y$ is an ordered pair of numbers which satisfies the inequality.

For example, the ordered pair $(1,1)$ is a solution of the inequality $x+2 y<6$ because $1+2(1)=3<6$ which is true.

There are infinitely many ordered pairs that satisfy the inequality $x+2 y<6$, so its graph will be a half plane.

Note that the linear equation $a x+b y=c$ is called "associated or corresponding equation" of each of the above mentioned inequalities.

## Procedure for Graphing a linear Inequality in two Variables

(i) The corresponding equation of the inequality is first graphed by using 'dashes' if the inequality involves the symbols $>$ or $<$ and a solid line is drawn if the inequality involves the symbols $\geq$ or $\leq$.
(ii) A test point (not on the graph of the corresponding equation) is chosen which determines that the half plane is on which side of the boundary line.

Example 1. Graph the inequality $x+2 y<6$.
Solution. The associated equation of the inequality

$$
\begin{aligned}
& x+2 y<6 \\
& \text { is } \quad x+2 y=6
\end{aligned}
$$

The line (ii) intersects the $x$-axis and $y$-axis at $(6,0)$ and $(0.3)$ respectively. As no point of the line (ii) is a solution $x^{*}$ of the inequality (i), so the graph of the line (ii) is shown by using dashes. We take $O(0,0)$ as a test point because it is not on the line (ii).

Substituting $x=0, y=0$ in the expression $x+2 y$ gives $0-2(0)=0<6$, so the point $(0,0)$ satisfies the inequality (i).

Any other point below the line (ii) satisfies the inequality (i), that is all points in the half plane containing the point $(0,0)$ satisfy the inequality (i).
Thus the graph of the solution set of inequality (i) is the a region on the origin-side of the line (ii), that is, the region below the line (ii). A portion of the open halfplane below ${ }^{x^{*}}$ the line (ii) is shown as shaded region in figure 5.22(a)

All points above the dashed line satisfy the inequality $x+2 y>6$
(ii)

A portion of the open half plane above the line (ii) is shown by shading in figure $5.22(b)$

Note: 1. The graph of the inequality $x+2 y \leq 6$.(iv) includes the graph of the line (ii),' so the open half-plane below the line (ii) including the graph of the line (ii) is the graph of the inequality (iv). A portion of the graph of the inequality (iv) is shown by shading in figure $5.22(b)$.
Note: 2 All points on the line (ii) and above the line (ii) satisfy the inequality $x+2 y \geq 6 \ldots$. (v). This means that the solution set of the inequality (v) consists of all points above the line (ii) and all points on the lines (ii). The graph of the inequality (v) is partially shown as shaded region in figure $5.22(d)$
Note: 3 that the graphs of
$x+2 y \leq 6$ and $x+2 y \geq 6$ are closed half planes.

Example 2. Graph the following linear inequalities in $x y$-plane;
(i) $2 x \geq-3$
(ii) $y \leq 2$

Solution. The inequality (i) in $x y$-plane is considered as $2 x+0 y \geq-3$ and its solution set consists of all point $(x, y)$
such that $x, y \in R$ and $x \geq-\frac{3}{2}$
The corresponding equation of the inequality (i) is $2 x=-3$
which a vertical line (parallel to the $y$-axis) and its graph is drawn in figure 5.23(a).
The graph of the inequality $2 x>-3$ is the open half plane to the right of the line (1).
Thus the graph of $2 x \geq-3$ is the closed half-plane to the right of the line (1).
(ii) The associated equation of the inequality (ii) is $y=2$
which is a horizontal line (parallel to the $x$-axis) and its $x^{*}$ graph is shown in figure 5.23(b) Here the solution set of the inequality $y<2$ is the open half plane below the boundary line $y=2$. Thus the graph of $y \leq 2$ consists of the boundary line and the open half plane below it.
Fig. 5.23(b)
Note that the intersection of graphs of 2x ≥ –3 and y ≤ 2 is partially shown in the adjoining figure 5.23(c).

### 5.3 REGION BOUNDED BY 2 OR 3 SIMULTANEOUS INEQUALITIES

The graph of a system of inequalities consists of the set of all ordered pairs (x, y) in the xy-plane which simultaneously satisfy all the inequalities in the system. Find the graph of such a system, we draw the graph of each inequality in the system on the same coordinate axes and then take intersection of all the graphs. The common region so obtained is called the solution region for the system of inequalities.

#### Example 1: Graph the system of inequalities

$$
x - 2y \leq 6
$$

$$
2x + y \geq 2
$$

#### Solution.

The graph of the line x – 2y = 6 is drawn by joining the point (6, 0) and (0, –3). The point (0, 0) satisfies the inequality x – 2y < 6 because 0 – 2(0) = 0 < 6. Thus the graph of x – 2y ≤ 6 is the upper half-plane including the graph of the line x – 2y = 6. The closed half-plane is partially shown by shading in figure 5.31(a).

#### Solution.

The graph of the line x – 2y = 6 is drawn by joining the point (6, 0) and (0, –3). The point (0, 0) satisfies the inequality x – 2y < 6 because 0 – 2(0) = 0 < 6. Thus the graph of x – 2y ≤ 6 is the upper half-plane including the graph of the line x – 2y = 6. The closed half-plane is partially shown by shading in figure 5.31(a).

#### *version: 1.1*

We draw the graph of the line 2x + y = 2 joining the points (1, 0) and (0, 2). The point (0, 0) does not satisfy the inequality 2x + y > 2 because 2(0) + 0 = 0 ≠ 2. Thus the graph of the inequality 2x + y ≥ 2 is the closed half-plane not on the origin-side of the line 2x + y = 2.

Thus the closed half-plane is shown partially as a shaded region in figure 5.31(b). The solution region of the given system of inequalities is the intersection of the graphs indicated in figures 5.31(a) and 5.31(b) and is shown as shaded region in figure 5.31(c).

The intersection point (2, – 2) can be found by solving the equations x – 2y = 6 and 2x + y = 2.

Note that the line x – 2y = 6 and 2x + y = 2 divide the xy-plane into four regions bounded by these lines. These four (bounded) regions are displayed in the adjoining figure.

Example 2. Graph the solution region for the following system of inequalities:

$$x - 2y \leq 6, \quad 2x + y > 2, \quad x + 2y \geq 10$$

Solution: The graph of the inequalities $x-2 y \leq 6$ and $2 x+y \geq 2$ have already drawn in figure 5.31(a) and 5.31(b) and their intersection is partially shown as a shaded region in figure 5.31(c) of the example 1 Art (5.3). Following the procedure of the example 1 of Art (5.3) the graph of the inequality $x+2 y \leq 10$ is shown partially in the figure 5.32(a).

The intersection of three graphs is the required solution region which is the shaded triangular region $P Q R$ (including its sides) shown partially in the figure 5.32(b).

Now we define a corner point of a solution region.

## DEFINITION:

A point of a solution region where two of its boundary lines intersect, is called a corner point or vertex of the solution region.

Such points play a useful role while solving linear programming problems. In example 2, the following three corner points are obtained by corresponding equations (of linear inequalities) given in the example 2(a) pairs.

|  Corresponding lines of inequalities: | Corner Points  |
| --- | --- |
|  $x-2 y=6, \quad 2 x+y=2$ | $P(2,-2)$  |
|  $x-2 y=6, \quad x+2 y=10$ | $Q(8,1)$  |
|  $2 x+y=2, \quad x+2 y=10$ | $R(-2,6)$  |

Example 3. Graph the following systems of inequalities.

|  (i) | $2 x+y \geq 2$ | (ii) | $2 x+y \geq 2$ | (iii) | $2 x+y \geq 2$  |
| --- | --- | --- | --- | --- | --- |
|   | $x+2 y \leq 10$ |  | $x+2 y \leq 10$ |  | $x+2 y \leq 10$  |
|   | $y \geq 0$ |  | $x \geq 0$ |  | $x \geq 0, y \geq 0$  |

## (i) The corresponding equations of the inequalities

$$ \begin{array}{llll} 2 x+y \geq 2 & \text { and } & x+2 y \leq 10 & \text { are } \ 2 x+y=2 & \text { (I) and } & x+2 y=10 & \text { (II) } \end{array} $$

For the partial graph of $2 x+y \geq 2$ see figure 5.31(b) of the example 1 and the graph of the inequality $x+2 y \leq 10$ is partially shown in figure 5.32(a) of the example 2.

The solution region of the inequalities $2 x+y \geq 2$ and $x+2 y \leq 10$ is the intersection of their individual graphs. The common region of the graphs of inequalities is partially shown as a shaded region in $x^{2}$ figure 5.33(a).

The graph of $y \geq 0$ is the upper half plane including the graph of the corresponding line $y=0$ (the $x$-axis) of the linear inequality $y \geq 0$. The graph of $y \geq 0$ is partially displayed in figure 5.33(b).

The solution region of the system of inequalities in (i) is the intersection of the graphs shown in figure 5.33(a) and 5.33(b). This solution region is displayed in figure 5.33(c).

(ii) See figure 5.33(a) for the graphs of the inequalities 2*x* + *y* ≥ 2 and *x* + 2*y* ≤ 10.

The graph of *x* ≥ 0 consists of the open half-plane to the right of the corresponding line *x* = 0 (*y*-axis) of the inequality *x* ≥ 0 and its graph. See figure 5.34(a).

Thus the solution region of the inequalities in (ii) is partially shown in figure 5.34(b). This region is the intersection of graphs in figure 5.33(a) and 5.34(a).

## **EXERCISE 5.1**

- **1. Graph the solution set of each of the following linear inequality in xy-plane:**
  - (i) 2*x* + *y* ≤ 6
  - (ii) 3*x* + 7*y* ≥ 21
  - (iii) 3*x* − 2*y* ≥ 6
  - (iv) 5*x* − 4*y* ≤ 20
  - (v) 2*x* + 1 ≥ 0
  - (vi) 3*y* − 4 ≤ 0
- **2. Indicate the solution set of the following systems of linear inequalities by shading:**
  - (i) 2*x* − 3*y* ≤ 6
  - (ii) *x* + *y* ≥ 5
  - (iii) 3*x* + 7*y* ≥ 21
  - 2*x* + 3*y* ≤ 12
  - −*y* + *x* ≤ 1
  - *x* − *y* ≤ 2
  - (iv) 4*x* − 3*y* ≤ 12
  - (v) 3*x* + 7*y* ≥ 21
  - (*x*) 3*x* + 7*y* ≥ 21
  - (*y*) 3*x* + 7*y* ≥ 21
  - (*x*) 3*x* + 7*y* ≥ 21
  - (*y*) 3*x* − 3*y* ≥ 4
- **3. Indicate the solution region of the following systems of linear inequalities by shading:**
  - (i) 2*x* − 3*y* ≤ 6
  - (ii) *x* + *y* ≤ 5
  - (iii) *x* + *y* ≥ 5
  - 2*x* + 3*y* ≤ 12
  - *y* − 2*x* ≤ 2
  - *x* − *y* ≥ 1
  - *y* ≥ 0
  - (iv) 3*x* + 7*y* ≤ 21
  - (v) 3*x* + 7*y* ≤ 21
  - (vi) 3*x* + 7*y* ≤ 21
  - (vii) 3*x* + 7*y* ≤ 21
  - 2*x* − *y* ≥ −3
  - *x* ≥ 0
  - (*y*) ≥ 0
  - (*x*) ≥ 0

*version: 1.1*

4. Graph the solution region of the following system of linear inequalities and find the corner points in each case.
(i) $2 x-3 y \leq 6$
(ii) $x+y \leq 5$
(iii) $3 x+7 y \leq 21$
$2 x+3 y \leq 12$
$-2 x+y \leq 2$
$2 x-y \leq-3$
$x \geq 0$
$y \geq 0$
$y \geq 0$
(iv) $3 x+2 y \geq 6$
(v) $5 x+7 y \leq 35$
(vi) $5 x+7 y \leq 35$
$x+3 y \leq 6$
$-x+3 y \leq 3$
$x-2 y \leq 2$
$y \geq 0$
$x \geq 0$
$x \geq 0$
5. Graph the solution region of the following system of linear inequalities by shading.
(i) $3 x-4 y \leq 12$
(ii) $3 x-4 y \leq 12$
(iii) $2 x+y \leq 4$
$3 x+2 y \geq 3$
$x+2 y \leq 6$
$2 x-3 y \geq 12$
$x+2 y \leq 9$
$x+y \geq 1$
$x+2 y \leq 6$
(iv) $2 x+y \leq 10$
(v) $2 x+3 y \leq 18$
(vi) $3 x-2 y \geq 3$
$x+y \leq 7$
$2 x+y \leq 10$
$x+4 y \leq 12$
$-2 x+y \leq 4$
$-2 x+y \leq 2$
$3 x+y \leq 12$

### 5.4 PROBLEM CONSTRAINTS

In the beginning we described that linear inequalities prescribe limitations and restrictions on allocation of available sources. While tackling a certain problem from every day life each linear inequality concerning the problem is named as problem constraint. The system of linear inequalities involved in the problem concerned are called problem constraints. The variables used in the system of linear inequalities relating to the problems of every day life are non-negative and are called non-negative constraints. These nonnegative constraints play an important role for taking decision. So these variables are called decision variables.

### 5.5 Feasible solution set

We see that solution region of the inequalities in example 2 of Art 5.3 is not within the first quadrant. If the nonnegative constraints $x \geq 0$ and $y \geq 0$ are included with the system of inequalities given in the example 2, then the solution region is restricted to the first quadrant.

It is the polygonal region $A B C D E$ (including its sides) as shown in the figure 5.51.

Such a region (which is restricted to the first quadrant) is referred to as a feasible region for the set of given constraints. Each point of the feasible region is called a feasible solution of the system of linear inequalities (or for the set of a given constraints). A set consisting of all the feasible solutions of the system of linear inequalities is called a feasible solution set.

Example 1. Graph the feasible region and find the corner points for the following system of inequalities (or subject to the following constraints).

$$
\begin{aligned}
& x-y \leq 3 \\
& x+2 y \leq 6 \\
& x \geq 0, \quad y \geq 0
\end{aligned}
$$

Solution: The associated equations for the inequalities

$$
\begin{aligned}
& x-y \leq 3 \quad \text { (i) } \quad \text { and } x+2 y \leq 6 \quad \text { (ii) } \\
& \text { are } x-y=3 \quad \text { (1) and } x+2 y=6 \quad(2)
\end{aligned}
$$

As the point $(3,0)$ and $(0,-3)$ are on the line (1), so the graph of $x-y=3$ is drawn by joining the points $(3,0)$ and $(0,-3)$ by solid line.

Similarly line (2) is graphed by joining the points $(6,0)$ and $(0,3)$ by solid line. For $x=0$ and $y=0$, we have;

$$
0-0=0 \leq 3 \text { and } 0+2(0)=0 \leq 6
$$

so both the closed half-planes are on the origin sides of the lines (1) and (2). The intersection of these closed half-planes is partially displayed as shaded region in figure 5.52(a).

For the graph of *y* ≥ 0, see figure 5.33(b) of the example 3 of art 5.3.

The intersection of graphs shown in figures 5.52(a) and 5.33(b) is partially graphed as shaded region in figure 5.52(b).

The graph of *x* ≥ 0 is drawn in figure 5.34(a). The intersection of the graphs shown in figures 5.52(a) and 5.34(a) is graphed in figure 5.52(c).

Finally the graph of the given system of linear inequalities is displayed in figure 5.52(d) which is the feasible region for the given system of linear inequalities. The points (0, 0), (3, 0), (4, 1) and (0, 3) are corner points of the feasible region.

*version: 1.1*

**Example 2.** A manufacturer wants to make two types of concrete. Each bag of Agrade concrete contains 8 kilograms of gravel (small pebbles with coarse sand) and 4 kilograms of cement while each bag of B-grade concrete contains 12 kilograms of gravel and two kilograms of cement. If there are 1920 kilograms of gravel and 480 kilograms of cement, then graph the feasible region under the given restrictions and find corner points of the feasible region.

**Solution:** Let *x* be the number of bags of A-grade concrete produced and *y* denote the number of bags of B-grade concrete produced, then 8*x* kilograms of gravel will be used for A-grade concrete and 12*y* kilograms of gravel will be required for B-grade concrete so 8*x* + 12*y* should not exceed 1920, that is,

$$8x + 12y \leq 1920$$

Similarly, the linear constraint for cement will be

$$4x + 2y \leq 480$$

Now we have to graph the feasible region for the linear constraints

$$8x + 12y \leq 1920$$
$$4x + 2y \leq 480, \quad x \geq 0, \quad y \geq 0$$

Taking the one unit along *x*-axis and *y*-axis equal to 40 we draw the graph of the feasible region required.

The shaded region of figure 5.53(a) shows the graph of 8*x* + 12*y* ≤ 1920 including the nonnegative constraints *x* ≥ 0 and *y* ≥ 0.

In the figure 5.53(b), the graph of 4*x* + 2*y* ≤ 480 including the nonnegative constraints *x* ≥ 0 and *y* ≥ 0 is displayed as shaded region.

The intersection of these two graphs is shown as shaded region in figure 5.53(c), which is the feasible region for the given linear constraints.

The point (0, 0), (120, 0), (60, 120) and (0, 160) are the corner points of the feasible region.

**Example 3. Graph the feasible regions subject to the following constraints.**

(a) $$2x - 3y \leq 6$$
(b) $$2x - 3y \leq 6$$
$$2x + y \geq 2$$
$$2x + y \geq 2$$
$$x \geq 0, y \geq 0$$

$$2x + y \geq 2$$

$$x + 2y < 8, \quad x \geq 0, \quad y \geq 0$$

**Solution:** The graph of $$2x - 3y \leq 6$$ is the closed half-plane on the origin side of $$2x - 3y = 6$$. The portion of the graph of system $$2x - 3y \leq 6$$,

$$x \geq 0, \quad y \geq 0$$

is shown as shaded region in figure 5.54(a).

*version: 1.1*

The graph of $$2x + y \geq 2$$ is the closed half-plane not on the origin side of $$2x + y = 2$$. The portion of the graph of the system $$2x + y \geq 2$$,

$$x \geq 0, y \geq 0$$

is displayed as shaded region in figure 5.54(b).

The graph of the system

$$2x - 3y \leq 6, \quad 2x + y \leq 2,$$
$$x \geq 0, \quad y \geq 0$$

is the intersection of the graphs shown in figures 5.54(a) and 5.54(b) and it is partially displayed in figure 5.54(c) as shaded region.

(b) The graph of system $$x + 2y \leq 8, \quad x \geq 0, \quad y \geq 0$$ is a triangular region indicated in figure 5.45(d).

Thus the graph of the system

$$2x - 3y \leq 6$$
$$2x + y \geq 2$$
$$x + 2y \leq 8$$
$$x \geq 0, y \geq 0$$

is the intersection of the graphs shown in figures 5.54(c) and 5.54(d). It is the shaded region indicated in the figure 5.54(e).

**Note:** The corner points of feasible region the set of constraints in (a) are (1, 0), (3, 0) and (0, 2) while the corner points of the feasible region for the set of constraints in (b) are (1, 0):

$$(3, 0) \left( \frac{16}{7} \cdot \frac{10}{7} \right), (0, 4) \text{ and } (0, 2)$$

We see that the feasible solution regions in example 3(a) and 3(b) are of different types. The feasible region in example 3(a) is unbounded as it cannot be enclosed in any circle how large it may be while the feasible region in example 3(b) can easily be enclosed within a circle, so it is bounded. If the line segment obtained by joining any two points of a region lies entirely within the region, then the region is called **convex**.

Both the feasible regions of example 3(a) and 3(b) are convex but the regions such as shown in the adjoining figures are not convex.

## **EXERCISE 5.2**

**1. Graph the feasible region of the following system of linear inequalities and find the corner points in each case.**

(i) $$2x - 3y \leq 6$$ (ii) $$x + y \leq 5$$ (iii) $$x + y \leq 5$$ $$2x + 3y \leq 12$$ $$-2y + y \leq 2$$ $$x \geq 0, y \geq 0$$ $$x \geq 0, y \geq 0$$ (iv) $$3x + 7y \leq 21$$ (v) $$3x + 2y > 6$$ $$x - y \leq 3$$ $$x + y \leq 4$$ $$x \geq 0, y \geq 0$$ $$x \geq 0, y \geq 0$$ (vi) $$5x + 7y \leq 35$$ $$x - 2y \leq 4$$ $$x \geq 0, y \geq 0$$

**2. Graph the feasible region of the following system of linear inequalities and find the corner points in each case.**

(i) $$2x + y \leq 10$$ (ii) $$2x + 3y \leq 18$$ (iii) $$2x + 3y \leq 18$$ $$x + 4y \leq 12$$ $$x + 2y \leq 10$$ $$x + 4y \leq 12$$ $$x \geq 0, y \geq 0$$ $$x \geq 0, y \geq 0$$ (iv) $$x + 2y \leq 14$$ (v) $$x + 3y \leq 15$$ (vi) $$2x + y \leq 20$$ $$3x + 15y \leq 120$$ $$x + y \leq 11$$ $$x \geq 0, y \geq 0$$

## **5.6 LINEAR PROGRAMMING**

A function which is to be maximized or minimized is called an **objective function**. Note that there are infinitely many feasible solutions in the feasible region. The feasible solution which maximizes or minimizes the objective function is called the **optimal solution**. The theorem of linear programming states that the maximum and minimum values of the objective function occur at corner points of the feasible region.

#### **Procedure for determining optimal solution:**

(i) Graph the solution set of linear inequality constraints to determine feasible region.

(ii) Find the corner points of the feasible region.

(iii) Evaluate the objective function at each corner point to find the optimal solution.

**Example 1.** Find the maximum and minimum values of the function defined as:

$$f(x, y) = 2x + 3y \qquad \text{subject to the constraints;}$$

$$x - y \leq 2 \qquad x + y \leq 4 \qquad 2x - y \leq 6, \quad x \geq 0$$

**Solution.** The graphs of $$x - y \leq 2$$ is the closed half plane on the origin side of $$x - y = 2$$ and the graph of $$x + y \leq 4$$ is the closed half-plane not on the origin side of $$x + y = 4$$. The graph of the system

$$x - y \leq 2, x + y \geq 4$$

*version: 1.1*

*version: 1.1*

including the non-negative constraints *x* ≥ 0 is partially displayed as shaded region in the figure 5.61. The graph of 2*x* − *y* ≤ 6 consists of the graph of the line 2*x* − *y* = 6 and the half plane on the origin side of the line 2*x* − *y*=6. A portion of the solution region of the given system of inequalities is shaded in the figure 5.62.

We see that feasible region is unbounded upwards and its corner points are *A*(0, 4), *B*(3, 1) and *C*(4, 2). Note that the point at which the lines *x* + *y* = 4 and 2*x* − *y* = 6 intersect is not a corner point of the feasible region.

It is obvious that the expression 2*x* + 3*y* does not possess a maximum value in the feasible region because its value can be made larger than any number by increasing *x* and *y*. We calculate the values of *f* at the corner points to find its minimum value:

$$
\begin{array}{rcl}
f(0, 4) & = & 2(0) + 3 \times 4 & = & 12 \\
f(3, 1) & = & 2 \times 3 + 3 \times 1 & = & 6 + 3 = 9 \\
f(4, 2) & = & 2 \times 4 + 3 \times 2 & = & 8 + 6 = 14
\end{array}
$$

Thus the minimum value of 2*x* + 3*y* is 9 at the corner point (3, 1).

**Notes:** If *f*(*x*, *y*) = 2*x* + 3*y*, then *f*(0, 4) = 2*x* 0 + 2*x* 4 = 8, *f*(3, 1) = 2*x* 3 + 2*x* 4 = 6 + 2 = 9 and (4, 2) = 2*x* 4 + 2*x* 2 = 8 + 4 = 12. The minimum value of 2*x* + 3*y* is the same, at two corner points (0, 4) and (3, 1).

We observe that the minimum value of 2*x* + 2*y* at each point of the line segment *AB* is 8 as:

$$
\begin{array}{rcl}
f(x, y) & = & 2x + 2(4 - x) \quad (\because \quad x + y = 4 \Rightarrow y = 4 - x) \\
& = & 2x + 8 - 2x = 8
\end{array}
$$

**Example 2.** Find the minimum and maximum values of *f* and *φ* defined as:

$$
f(x, y) = 4x + 5y, \qquad \phi(x, y) = 4x + 6y
$$

under the constraints

$$
2x - 3y \leq 6 \qquad 2x + y \geq 2 \qquad 2x + 3y \leq 12 \qquad x \geq 0, \quad y \geq 0
$$

**Solution.** The graphs of 2*x* − 3*y* ≤ 6, 2*x* + *y* ≥ 2, are displayed in the example 3 of Art. 5.5. Joining the points (6, 0) and (0, 4), we obtain the graph of the line 2*x* + 3*y* = 12. As 2(0) + 3(0) = 0 < 12, so the graph of 2*x* + 3*y* < 12 is the half plane below the line 2*x* + 3*y* = 12. Thus the graph of 2*x* + 3*y* ≤ 12 consists of the graph of the line 2*x* + 3*y* = 12 and the half plane below the line 2*x* + 3*y* = 12. The solution region of 2*x* − 3*y* ≤ 6, 2*x* + *y* ≥ 2 and 2*x* + 3*y* ≤ 12 is the triangular region *PQR* shown in figure 5.63. The non-negative constraints *x* ≥ 0, *y* ≥ 0 indicated the first quadrant. Thus the feasible region satisfying all the constraints is shaded in the figure 5.63 and its corner points are (1, 0), (0, 2), (0, 4), (9, 2, 1) and (3, 0).

We find values of *f* at the corner points.

|  Corner point | *f*(*x*, *y*) = 4*x* + 5*y*  |
| --- | --- |
|  (1, 0) | *f*(1, 0) = 4 *x* 1 + 5.0 = 4  |
|  (0, 2) | *f*(0, 2) = 4 *x* 0 + 5.2 = 10  |
|  (0, 4) | *f*(0, 4) = 4 *x* 0 + 5.4 = 20  |
|  (9/2, 1) | *f*(9/2, 1) = 4 *x* 9/2 + 5.1 = 23  |
|  (3, 0) | *f*(3, 0) = 4 *x* 3 + 5.0 *x* 0 = 12  |

From the above table, it follows that the minimum value of *f* is 4 at the corner point (1, 0) and maximum value of *f* is 23 at the corner point (9, 2, 1). The values of *φ* at the corner points are given below in tabular form.

|  Corner point | *φ*(*x*, *y*) = 4*x* + 5*y*  |
| --- | --- |
|  (1, 0) | *φ*(1, 0) = 4.1 + 6.0 = 4  |
|  (0, 2) | *φ*(0, 2) = 4.0 + 6.2 = 12  |
|  (0, 4) | *φ*(0, 4) = 4.0 + 6.4 = 24  |
|  (9/2, 1) | *φ*(9/2, 1) = 4.9/2 + 6.1 = 24  |
|  (3, 0) | *φ*(3, 0) = 4 *x* 3 + 6.0 = 12  |

The minimum value of *φ* is 4 at the point (1, 0) and maximum value of *φ* is 24 at the corner points (0, 4) and (9, 2, 1). As observed in the above example, it follows that the function *φ* has maximum value at all the points of the line segment between the points

(0, 4) and $\left(\frac{9}{3}, 1\right)$.

Note 1. Some times it may happen that each point of constraint line gives the optimal value of the objective function.

Note 2. For different value of $k$, the equation $4 x+5 y=k$ represents lines parallel to the line $4 x+5 y=0$. For a certain admissible value of $k$, the intersection of $4 x+5 y=k$ with the feasible region gives feasible solutions for which the profit is $k$.

### 5.7 LINEAR PROGRAMMING PROBLEMS

Convert a linear programming problem to a mathematical form by using variables, then follow the procedure given in Art 5.6.

Example 1: A farmer possesses 100 canals of land and wants to grow corn and wheat. Cultivation of corn requires 3 hours per canal while cultivation of wheat requires 2 hours per canal. Working hours cannot exceed 240. If he gets a profit of Rs. 20 per canal for corn and Rs. 15/- per canal for wheat, how many canals of each he should cultivate to maximize his profit?

Solution: Suppose that he cultivates $x$ canals of corn and $y$ canals of wheat. Then constraints can be written as:

$$ \begin{aligned} & x+y \leq 100 \ & 3 x+2 y \leq 240 \end{aligned} $$

Non-negative constraints are $x \geq 0, y \geq 0$. Let $P(x, y) x^{*}$ be the profit function, then

$$ P(x, y)=20 x+15 y $$

Now the problem is to maximize the profit function $P$ under the given constraints. Graphing the inequalities, we obtain the feasible region which is shaded in the figure 5.71. Solving the equations $x+y=100$ and $3 x+2 y=240$ gives $x=240-2(x+y)=240-200=40$ and $y=100-40=60$, that is; their point of intersection is $(40,60)$. The corner points of the feasible region are $(0,0),(0,100),(40,60)$ and $(80,0)$. Now we find the values of $P$ at the corner points.

|  Corner point | $P(x, y)=20 x+15 y$  |
| --- | --- |
|  $(0,0)$ | $P(0,0)=20 \times 0+15 \times 0=0$  |
|  $(0,100)$ | $P(0,100)=20 \times 0+15 \times 100=1500$  |
|  $(40,60)$ | $P(40,60)=20 \times 40+15 \times 60=1700$  |
|  $(80,0)$ | $P(80,0)=20 \times 80+15 \times 0=1600$  |

From the above table, it follows that the maximum profit is Rs. 1700 at the corner point $(40,60)$. Thus the farmer will get the maximum profit if he cultivates 40 canals of corn and 60 canals of wheat.

Exam ple 2. A factory produces bicycles and motorcycles by using two machines $A$ and B. Machine $A$ has at most 120 hours available and machine $B$ has a maximum of 144 hours available. Manufacturing a bicycle requires 5 hours in machine $A$ and 4 hours in machine $B$ while manufacturing of a motorcycle requires 4 hours in machine $A$ and 8 hours in machine $B$. If he gets profit of Rs. 40 per bicycle and profit of Rs. 50 per motorcycle, how many bicycles and motorcycles should be manufactured to get maximum profit?

Solution: Let the number of bicycles to be manufactured be $x$ and the number of motor cycles to be manufactured be $y$.

Then the time required to use machine $A$ for $x$ bicycles and $y$ motorcycles is $5 x+4 y$ (hours) and the time required to use machine $B$ for $x$ bicycles and $y$ motorcycles in $4 x+8 y$ (hours). Thus the problem constraints are $5 x+4 y \leq 120$

$$ \begin{array}{ll} \text { And } & 4 x+8 y \leq 144 \ \Rightarrow & 2 x+4 y \leq 72 \end{array} $$

Since the numbers of articles to be produced cannot be negative, so $x \geq 0, y \geq 0$. Let $P(x, y)$ be the profit function, then $P(x, y)=40 x+50 y$. Now the problem is to maximize $P$ subject to the constraints:

$$
\begin{aligned}
& 5 x+4 y \leq 120 \\
& 2 x+4 y \leq 72 \quad ; \quad x \geq 0, y \geq 0
\end{aligned}
$$

Solving $5 x+4 y=120$ and $2 x+4 y=72$, gives $3 x=48 \Rightarrow x=16$ and $4 y=72-2 x=72-32=40 \Rightarrow y=10$.

Thus their point of intersection is $(16,10)$. Graphing the linear inequality constraints, the feasible region obtained is depicted in the figure 5.72 by shading. The corner points of the feasible region are $(0,0),(0,18),(16,10)$ and $(24,0)$. Now we find the values of $P$ at the corner points.

|  Corner point | $P(x, y)=40 x+50 y$  |
| --- | --- |
|  $(0,0)$ | $P(0,0)=40 \times 0+50 \times 0=0$  |
|  $(0,18)$ | $P(0,18)=40 \times 0+50 \times 18=900$  |
|  $(16,10)$ | $P(16,10)=40 \times 16+50 \times 10=1140$  |
|  $(24,0)$ | $P(24,0)=40 \times 24+50 \times 0=960$  |

From the above table, it follows, that the maximum profit is Rs. 1140 at the corner point $(16,10)$. Manufacturer gets the maximum profit if he manufactures 16 bicycles and 10 motorcycles.

## EXERCISE 5.3

1. Maximize $f(x, y)=2 x+5 y$ subject to the constraints $2 y-x \leq 8 ; \quad x-y \leq 4 ; \quad x \quad 0 \geq 0 ; \quad y \geq 0$
2. Maximize $f(x, y)=x+3 y$ subject to the constraints $2 x+5 y \leq 30 ; \quad 5 x+4 y \leq 20 ; \quad x \geq 0 ; \quad y \geq 0$
3. Maximize $z=2 x+3 y$; subject to the constraints: $3 x+4 y \leq 12 ; \quad 2 x+y \leq 4 ; \quad 4 x-y \leq 4 ; x \geq 0 ; y \geq 0$
4. Minimize $z=2 x+y$ : subject to the constraints: $x+y \geq 3 ; \quad 7 x+5 y \leq 35 ; \quad x \geq 0 ; \quad y \geq 0$
5. Maximize the function defined as; $f(x, y)=2 x+3 y$ subject to the constraints: $2 x+y \leq 8 ; \quad x+2 y \leq 14 ; \quad x \geq 0 ; \quad y \geq 0$
6. Minimize $z=3 x+y$; subject to the constraints: $3 x+5 y \geq 15 ; \quad x+6 y \geq 9 ; \quad x \geq 0 ; \quad y \geq 0$
7. Each unit of food $X$ costs Rs. 25 and contains 2 units of protein and 4 units of iron while each unit of food $Y$ costs Rs. 30 and contains 3 units of protein and 2 unit of iron. Each animal must receive at least 12 units of protein and 16 units of iron each day. How many units of each food should be fed to each animal at the smallest possible cost?
8. A dealer wishes to purchase a number of fans and sewing machines. He has only Rs. 5760 to invest and has space atmost for 20 items. A fan costs him Rs. 360 and a sewing machine costs Rs. 240. His expectation is that the can sell a fan at a profit of Rs. 22 and a sewing machine at a profit of Rs. 18. Assuming that he can sell all the items that he can buy, how should he invest his money in order to maximize his profit?
9. A machine can produce product $A$ by using 2 units of chemical and 1 unit of a compound or can produce product $B$ by using 1 unit of chemical and 2 units of the compound. Only 800 units of chemical and 1000 units of the compound are available. The profits per unit of $A$ and $B$ are Rs. 30 and Rs. 20 respectively, maximize the profit function.

# CHAPTER

## 6

## Conic Sections

## 6.1 INTRODUCTION

Conic sections or simply conics, are the curves obtained by cutting a (double) right circular cone by a plane. Let $R S$ be a line through the centre $C$ of a given circle and perpendicular to its plane. Let $A$ be a fixed point on $R S$. All lines through $A$ and points on the circle generate a right circular cone. The lines are called rulings or generators of the cone. The surface generated consists of two parts, called nappes, meeting at the fixed point $A$, called the vertex or apex of the cone. The line $\boldsymbol{R} \boldsymbol{S}$ is called axis of the cone.

If the cone is cut by a plane perpendicular to the axis of the cone, then the section is a circle.
The size of the circle depends on how near the plane is to the vertex of the cone. If the plane passes through the vertex $A$, the intersection is just a single point or a point circle. If the cutting plane is slightly tilted and cuts only one nappe of the cone, the resulting section is an ellipse. If the intersecting plane is parallel to a generator of the cone, but intersects its one nappe only, the curve of intersection is a parabola. If the cutting plane is parallel to the axis of the cone and intersects both of its nappes, then the curve of intersection is a hyperbola.

The Greek mathematicians Apollonius' (260-200 B.C.) and Pappus (early fourth century) discovered many intersecting properties of the conic sections. They used the methods of Euclidean geometry to study conics. We shall not study conics from the point of view stated above, but rather approach them with the more powerful tools of analytic geometry.

The theory of conics plays an important role in modern space mechanics, occeangraphy and many other branches of science and technology.

We first study the properties of a Circle. Other conics will be taken up later.

### 6.1.1 Equation of a Circle

The set of all points in the plane that are equally distant from a fixed point is called a circle. The fixed point is called the centre of the circle and the distance from the center of the circle to any point on the circle is called the radius of the circle.

If $C(h, k)$ is centre of a circle, $r$ its radius and $P(x, y)$ any point on the circle, then the circle, denoted $S(C ; r)$ in set notation is

$$
S(C ; r)=\{P(x, y) \mid \overline{C P} \mid r\}
$$

By the distance formula, we get

$$
|\overline{C P}|=\sqrt{(x-h)^{2}+(y-k)^{2}}=r
$$

or $\quad(x-h)^{2}+(y-k)^{2}=r^{2}$
is an equation of the circle in standard form.
If the centre of the circle is the origin, then (1) reduces to

$$
x^{2}+y^{2}=r^{2}
$$

If $r=0$, the circle is called a point circle which consists of the centre only.

Let $P(x, y)$ be any point on the circle (2) and let the inclination of $O P$ be $\theta$ as shown in the figure. It is clear that

$$
\left.\begin{array}{l}
x=r \cos \theta \\
y=r \sin \theta
\end{array}\right\}
$$

The point $P(r \cos \theta, r \sin \theta)$ lies on (2) for all values of $\theta$. Equations (3) are called parametric equations of the circle (2).

Example 1: Write an equation of the circle with centre $(-3,5)$ and radius 7.
Solution: Required equation is

$$
(x+3)^{2}+(y-5)^{2}=7^{2}
$$

or

$$
x^{2}+y^{2}+6 x-10 y-15=0
$$

### 6.1.1 General Form of an Equation of a Circle

Theorem: The equation

$$
x^{2}+y^{2}+2 g x+2 f y+c=0
$$

represents a circle $g, f$ and $c$ being constants.
Equation (1) can be written as:

$$
\left(x^{2}+2 g x+g^{2}\right)+\left(y^{2}+2 f y+f^{2}\right)=g^{2}+f^{2}-c
$$

or

$$
[x-(-g)]^{2}+\left[y-(-f)\right]^{2}=\left(\sqrt{g^{2}+f^{2}-c}\right)^{2}
$$

which is standard form of an equation of a circle with centre $(-g,-f)$ and radius $\sqrt{g^{2}+f^{2}-c}$.
The equation (1) is called general form of an equation of a circle.

## 1. (1) is a second degree equation in which coefficient of each of $x^{2}$ and $y^{2}$ is 1 .
2. (1) contains no term involving the product $x y$.

Thus a second degree equation in which coefficients of $x^{2}$ and $y^{2}$ are equal and there is no product term $x y$ represents a circle.

If three non-collinear points through which a circle passes are known, then we can find the three constants $f, g$ and $c$ in (1).

Example 2: Show that the equation:

$$
5 x^{2}+5 y^{2}+24 x+36 y+10=0
$$

represents a circle. Also find its centre and radius.
Solution: The given equation can be written as:

$$
x^{2}+y^{2}+\frac{24}{5} x+\frac{36}{5} y+2=0
$$

which is an equation of a circle in the general form. Here

$$
g=\frac{12}{5} \cdot f=\frac{18}{5} \cdot c=2
$$

$$
\begin{aligned}
& \text { Thus centre of the circle }=(-g,-f)=\left(\frac{-12}{5}, \frac{-18}{5}\right) \\
& \text { Radius of the circle }=\sqrt{g^{2}+f^{2}-c}=\sqrt{\frac{144}{25}+\frac{324}{25}-2} \\
& =\sqrt{\frac{418}{25}}=\frac{\sqrt{418}}{5}
\end{aligned}
$$

### 6.1.2 Equations of Circles Determined by Given Conditions

The general equation of a circle $x^{2}+y^{2}+2 g x+2 f y+c=0$ contains three independent constants $g, f$ and $c$, which can be found if the equation satisfies three given conditions. We discuss different cases in the following paragraphs.

## 1. A Circle Passing Through Three Non-collincar Points.

If three non-collinear points, through which a circle passes, are known, then we can find the three independent constants $f, g$ and $c$ occurring in the general equation of a circle.

Example 3: Find an equation of the circle which passes through the points $A(5,10), B(6,9)$ and $C(-2,3)$.

Solution: Suppose equation of the required circle is

$$
x^{2}+y^{2}+2 g x+2 f y+c=0
$$

Since the three given points lie on the circle, they all satisfy (1). Substituting the three points into (1), we get

$$
\begin{aligned}
& 25+100+10 g+20 f+c=0 \\
& \Rightarrow \quad 10 g+20 f+c+125=0 \\
& 36+81+12 g+18 f+c+117=0 \\
& \Rightarrow \quad 12 g+18 f+c+117=0 \\
& 4+9-4 g+6 f+c=0 \\
& \quad-4 g+6 f+c+13=0
\end{aligned}
$$

Now we solve the equations (2), (3) and (4).
Subtracting (3) from (2), we have

$$
-2 g+2 f+8=0
$$

or

$$
g-f-4 = 0 \tag{5}
$$

Subtracting (4) from (2), we have.

$$
14g + 14f + 112 = 0 \tag{6}
$$

or

$$
g + f + 8 = 0 \tag{6}
$$

From (5) and (6), we have,

$$
f = -6 \text{ and } g = -2.
$$

Inserting the values of *f* and *g* into (2), we get *c* = 15

Thus equation of the circle is: *x*² + *y*² − 4*x* − 12*y* + 15 = 0

### 2. A circle passing through two points and having its centre on a given line.

**Example 4:** Find an equation of the circle having the join of *A* (*x*₁, *y*₁) and *B* (*x*₂, *y*₂) as a diameter.

**Solution:** Since *AB* is a diameter of the circle, its midpoint is the centre of the circle. The radius of the circle is known and standard form of an equation of the circle may be easily written. However, a more elegant procedure is to make use of the plane geometry. If (*x*, *y*) is any point on the circle, then *m*⊥*APB* = 90°.

Thus the lines *AP* and *BP* are perpendicular to each other.

$$
\text{Slope of } \quad AP = \frac{y - y_1}{x - x_1} \quad \text{and} \quad \text{Slope of } \quad BP \quad \frac{y - y_2}{x - x_2}
$$

By the condition of perpendicularity of two lines, we get

$$
\frac{y - y_1}{x - x_1} \times \frac{y - y_2}{x - x_2} = 1
$$

or

$$
(x - x_1)(x - x_2) + (y - y_1)(y - y_2) = 0
$$

This is required equation of the circle.

### 3. A circle passing through two points and equation of tangent at one of these points is known.

**Example 5:** Find an equation of the circle passing through the point (−2, −5) and touching the line 3*x* + 4*y* − 24 = 0 at the point (4, 3).

**Solution:** Let the circle be

$$
x^2 + y^2 + 2gx + 2fy + c = 0 \tag{1}
$$

The points (−2, −5) and (4, 3) lie on it. Therefore

$$
-4g - 10f + c + 29 = 0 \tag{2}
$$

$$
8g + 6f + c + 25 = 0 \tag{3}
$$

The line

$$
3x + 4y - 24 = 0 \tag{4}
$$

Touches the circle at (4, 3).

A line through (4, 3) and perpendicular to (4) is

$$
y - 3 = \frac{4}{3} \left( x - 4 \right) \quad \text{or} \quad 4x - 3y - 7 = 0
$$

This line being a normal through (4, 3) passes through the centre (−g, −f) of the circle (1). Therefore

$$
-4g + 3f - 7 = 0 \tag{5}
$$

From (2) − (3), we get

$$
-12g - 16f + 4 = 0
$$

or

$$
3g + 4f - 1 = 0 \tag{6}
$$

Solving (5) and (6), we have *g* = −1, *f* = 1. Inserting these values of *g* and *f* into (3), we find *c* = −23. Equation of the required circle is

$$
x^2 + y^2 - 2x + 2y - 23 = 0
$$

### 4. A circle passing through two points and touching a given line.

**Example 6:** Find an equation of the circle passing through the points *A*(1, 2) and *B*(1, −2) and touching the line *x* + 2*y* + 5 = 0.

**Solution:** Let *O*(*h, k*) be the centre of the required circle. Then

$$
\begin{aligned}
& |O A|=|O B|=\text { radius of the circle. } \\
& \text { i.e., } \quad(h-1)^{2}+(k-2)^{2}=(h-1)^{2}+(k+2)^{2} \\
& \text { or } 8 k=0 \quad \text { i.e., } k=0 \\
& \text { Hence }|O A|=|O B| \\
& =\sqrt{(h-1)^{2}+4}
\end{aligned}
$$

Now length of perpendicular from $(h, k)$ i.e., $(h, 0)$ to the line $x+2 y+5=0$ equals the radius of the circle and is given by

$$
\frac{|h+5|}{\sqrt{5}}
$$

Therefore, $\frac{|h+5|}{\sqrt{5}} \cdot|O A|=\sqrt{(h-1)^{2}+4}$
or $\frac{(h+5)^{2}}{5}=(h-1)^{2}+4$ or $4 h^{2}-20 h=0 \quad$ i.e., $h=0,5$
Thus centres of the two circles are at $(0,0)$ and $(5,0)$.
Radius of the first circle $=\sqrt{5} \quad$; Radius of the second circle $=\sqrt{20}$
Equations of the circles are

$$
\begin{array}{lll}
x^{2}+y^{2}=5 & \text { and } & (x-5)^{2}+y^{2}=20 \\
x^{2}+y^{2}=5 & \text { and } & x^{2}+y^{2}-10 x+5=0
\end{array}
$$

## EXERCISE 6.1

1. In each of the following, find an equation of the circle with
(a) centre at $(5,-2)$ and radius 4
(b) centre at $(\sqrt{2},-3 \sqrt{3})$ and radius $2 \sqrt{2}$
(c) ends of a diameter at $(-3,2)$ and $(5,-6)$.
2. Find the centre and radius of the circle with the given equation
(a) $x^{2}+y^{2}+12 x-10 y=0$
(b) $5 x^{2}+5 y^{2}+14 x+12 y-10=0$
(c) $x^{2}+y^{2}-6 x+4 y+13=0$
(d) $4 x^{2}+4 y^{2}-8 x+12 y-25=0$
3. Write an equation of the circle that passes through the given points
(a) $A(4,5), B(-4,-3), C(8,-3)$
(b) $A(-7,7), B(5,-1), C(10,0)$
(c) $A(a, 0), B(0, b), C(0,0)$
(d) $A(5,6), B(-3,2), C(3,-4)$
4. In each of the following, find an equation of the circle passing through
(a) $A(3,-1), B(0,1)$ and having centre at $4 x-3 y-3=0$
(b) $A(-3,1)$ with radius 2 and centre at $2 x-3 y+3=0$
(c) $A(5,1)$ and tangent to the line $2 x-y-10=0$ at $B(3,-4)$
(d) $A(1,4), B(-1,8)$ and tangent to the line $x+3 y-3=0$
5. Find an equation of a circle of radius $a$ and lying in the second quadrant such that it is tangent to both the axes.
6. Show that the lines $3 x-2 y=0$ and $2 x+3 y-13=0$ are tangents to the circle $x^{2}+y^{2}+6 x-4 y=0$
7. Show that the circles
$x^{2}+y^{2}+2 x-2 y-7=0$ and $x^{2}+y^{2}-6 x+4 y+9=0$ touch externally.
8. Show that the circles
$x^{2}+y^{2}+2 x-8=0$ and $x^{2}+y^{2}-6 x+6 y-46=0$ touch internally.
9. Find equations of the circles of radius 2 and tangent to the line $x-y-4=0$ at $A(1,-3)$.

### 6.2 TANGENTS AND NORMALS

A tangent to a curve is a line that touches the curve without cutting through it. We know that for any curve whose equation is given by $y=f(x)$ or $f(x, y)=0$, the derivative is slope of the tangent at any point $P(x, y)$ to the curve. The equation of the tangent to the curve can easily be written by the pointslope formula. The normal to the curve at $P$ is the line through $P$ perpendicular to the tangent to the curve at $P$. This method can be very

conveniently employed to find equations of tangent and normal to the circle $x^{2}+y^{2}+2 g x+2 f y+c=0$ at the point $P\left(x_{1}, y_{1}\right)$.
Here $\quad f\left(x_{1} y\right)=x^{2}+y^{2}+2 g x+2 f y+c=0$
Differentiating (1) w.r.t. $x$, we get

$$
\begin{aligned}
& 2 x+2 y \frac{d y}{d x}+2 g+2 f \frac{d y}{d x}=0 \text { or } \quad \frac{d y}{d x}=\frac{x+g}{y+f} \\
& \left.\frac{d y}{d x}\right]_{x, y, y_{1}}=-\frac{x_{1}+g}{y_{1}+f}=\text { Slope of the tangent at }\left(x_{1}, y_{1}\right)
\end{aligned}
$$

Equation of the Tangent at $P$ is given by

$$
\begin{aligned}
& y-y_{1}=-\frac{x_{1}+g}{y_{1}+f}\left(x-x_{1}\right) \quad \text { (Point-slope form) } \\
& \text { or } \quad y\left(y_{1}+f\right)-y_{1}^{2}-y_{1} f=-x\left(x_{1}+g\right)+x_{1}^{2}+x_{1} g \\
& \text { or } \quad x x_{1}+y y_{1}+g x+f y=x_{1}^{2}+y_{1}^{2}+g x_{1}+f y_{1} \\
& \text { or } \quad x x_{1}+y y_{1}+g x+f y+g x_{1}+f y_{1}+c=x_{1}^{2}+y_{1}^{2}+g x_{1}+f y_{1}+g x_{1}+f y_{1}+c \\
& \text { (adding } g x_{1}+f y_{1}+c \text { to both sides) } \\
& x x_{1}+y y_{1}+g\left(x+x_{1}\right)+f\left(y+y_{1}\right)+c=0 \\
& \text { since } \quad\left(x_{1}, y_{1}\right) \text { lies on (1) and so } \\
& x_{1}^{2}+y_{1}^{2}+2 g x_{1}+2 f y_{1}+c=0
\end{aligned}
$$

Thus $\frac{\left(x_{1}+y y_{1}+g\left(x+x_{1}\right)+f\left(y+y_{1}\right)+c=0\right)}{x_{1}+g}$ is the required equation of the tangent.
To find an equation of the normal at $P$, we note that slope of the normal is

$$
\frac{y_{1}+f}{x_{1}+g} \quad \text { (negative reciprocal of slope of the tangent) }
$$

Equation of the normal at $P\left(x_{1}, y_{1}\right)$ is

$$
y-y_{1}=\frac{y_{1}+f}{x_{1}+g}\left(x-x_{1}\right)
$$

or $\quad \frac{\left(y-y_{1}\right)\left(x_{1}+g\right)=\left(x-x_{1}\right)\left(y_{1}+f\right)}{x_{1}+g}$ is an equation of the normal at $\left(x_{1}, y_{1}\right)$.

## Theorem:

The point $P\left(x_{1}, y_{1}\right)$ lies outside, on or inside the circle $x^{2}+y^{2}+2 g x+2 f y+c=0$ according as

$$
x_{1}^{2}+y_{1}^{2}+2 g x_{1}+2 f y_{1}+c \stackrel{\infty}{\times} \mid 0
$$

Proof. Radius $r$ of the given circle is

$$
r=\sqrt{g^{2}+f^{2}-c}
$$

The point $P\left(x_{1}, y_{1}\right)$ lies outside, on or inside the circle, according as:

$$
m[C P] \stackrel{\infty}{\times} \mid r
$$

i.e., according as: $\quad \sqrt{\left(x_{1}+g\right)^{2}+\left(y_{1}+f\right)^{2}} \stackrel{\infty}{\times} \sqrt{g^{2}+f^{2}-c}$
or according as : $\quad x_{1}^{2}+2 g x_{1}+g^{2}+y_{1}^{2}+f^{2}+2 f y_{1} \stackrel{\infty}{\times} \sqrt[3]{g^{2}+f^{2}-c}$
or according as : $\quad x_{1}^{2}+y_{1}^{2}+2 g x_{1}+2 f y_{1}+c \stackrel{\infty}{\times} \mid 0$.
Example 1: Determine whether the point $P(-5,6)$ lies outside, on or inside the circle: $x^{2}+y^{2}+4 x-6 y-12=0$

Solution: Putting $x=-5$ and $y=6$ in the left hand member of the equation of the circle, we get

$$
25+36-20-36-12=-7<0
$$

Thus the point $P(-5,6)$ lies inside the circle.
Theorem: The line $y=m x+c$ intersects the circle $x^{2}+y^{2}=a^{2}$ in at the most two points.
Proof: It is known from plane geometry that a line can meet a circle in at the most two points.

To prove it analytically, we note that the coordinates of the points where the line

$$
\begin{aligned}
& y=m x+c \\
& \text { intersects the circle } \\
& x^{2}+y^{2}=a^{2}
\end{aligned}
$$

are the simultaneous solutions of the equations (1) and (2).
Substituting the value of $y$ from equation (1) into equation (2), we get

$$
x^{2}+(m x+c)^{2}=a^{2}
$$

or $\quad x^{2}\left(1+m^{2}\right)+2 m c x+c^{2}-a^{2}=0$
This being quadratic in $x$, gives two values of $x$ say $x_{1}$ and $x_{2}$. Thus the line intersects the circle in at the most two points. For nature of the points we examine the discriminant of (3).

The discriminant of (3) is $\left(2 m c\right)^{2}-4\left(1+m^{2}\right)\left(c^{2}-a^{2}\right)$

$$
\begin{aligned}
& =4 m^{2} c^{2}-4\left(1+m^{2}\right)\left(c^{2}-a^{2}\right) \\
& =4 m^{2} c^{2}-4 m^{2} c^{2}-4\left(c^{2}-a^{2}-a^{2} m^{2}\right) \\
& =4\left[-c^{2}+a^{2}\left(1+m^{2}\right)\right]
\end{aligned}
$$

These points are
(i) Real and distinct, if $a^{2}\left(1+m^{2}\right)-c^{2}>0$
(ii) Real and coincident if $a^{2}\left(1+m^{2}\right)-c^{2}=0$
(iii) Imaginary if $a^{2}\left(1+m^{2}\right)-c^{2}<0$

## Condition that the line may be a tangent to the circle.

The line (1) is tangent to the circle (2) if it meets the circle in one point.
i.e., if $c^{2}=a^{2}\left(1+m^{2}\right)$ or $\varepsilon=\alpha \sqrt{1-m^{2}}$
is the condition for (1) to be a tangent to (2).
Example 2: Find the co-ordinates of the points of intersection of the line $2 x+y=5$ and the circle $x^{2}+y^{2}+2 x-9=0$. Also find the length of the intercepted chord.

Solution: From $2 x+y=5$, we have

$$
y=(5-2 x)
$$

Inserting this value of $y$ into the equation of the circle, we get

$$
\begin{aligned}
& x^{2}+(5-2 x)^{2}+2 x-9=0 \\
& \text { or } \quad 5 x^{2}-18 x+16=0 \\
& \Rightarrow \quad x=\frac{18 \pm \sqrt{324-320}}{10} \quad \frac{18 \pm 2}{10} \quad 2, \frac{8}{5}
\end{aligned}
$$

When $x=2, y=5-4=1$
When $x=\frac{8}{5}, y=5-\frac{16}{5}-\frac{9}{5}$

Thus the points of intersection are $P(2,1)$ and $Q\left(\frac{8}{5}, \frac{9}{5}\right)$
Length of the chord intercepted

$$
=\sqrt[3]{P Q}=\sqrt{\left(\frac{8}{5}-2\right)^{2}+\left(\frac{9}{5}-1\right)^{2}}=\sqrt{\frac{4}{25}-\frac{16}{25}}=\frac{2}{\sqrt{5}}
$$

Theorem: Two tangents can be drawn to a circle from any point $P\left(x_{1}, y_{1}\right)$. The tangents are real and distinct, coincident or imaginary according as the point lies outside, on or inside the circle.

Proof: Let an equation of the circle be $x^{2}+y^{2}=a^{2}$
We have already seen that the line

$$
y=m x+a \sqrt{1+m^{2}}
$$

is a tangent to the given circle for all values of $m$. If it passes through the point $P\left(x_{1}, y_{1}\right)$, then

$$
\begin{aligned}
& y_{1}=m x_{1}+a \sqrt{1+m^{2}} \\
& \text { or } \quad\left(y_{1}-m x_{1}\right)^{2}=a^{2}\left(1+m^{2}\right) \\
& \text { or } \quad m^{2}\left(x_{1}^{2}-a^{2}\right)-2 m x_{1} y_{1}+y_{1}^{2}-a^{2}=0
\end{aligned}
$$

This being quadratic in $m$, gives two values of $m$ and so there are two tangents from $P\left(x_{1}, y_{1}\right)$ to the circle. These tangents are real and distinct, coincident or imaginary according as the roots of (2) are real and distinct, coincident or imaginary
i.e., according as $x_{1}^{2} y_{1}^{2}-\left(x_{1}^{2}-a^{2}\right)\left(y_{1}^{2}-a^{2}\right) \stackrel{\text { o }}{=} 0$
or $\quad x_{1}^{2} a^{2}+y_{1}^{2} a^{2}+a^{2} \stackrel{\text { o }}{=} 0 \quad$ or $\quad x_{1}^{2}+y_{1}^{2}-a^{2} \stackrel{\text { o }}{=} 0$
i.e., according as the point $P\left(x_{1}, y_{1}\right)$ lies outside, on or inside the circle $x^{2}+y^{2}-a^{2}=0$

Example 3: Write equations of two tangents from $(2,3)$ to the circle $x^{2}+y^{2}=9$.
Solution. Any tangent to the circle is

$$
y=m x+3 \sqrt{1+m^{2}}
$$

If it passes through $(2,3)$, then

$$
\begin{aligned}
& 3=2 m+3 \sqrt{1+m^{2}} \\
\text { or } & (3-2 m)^{2} \equiv 9\left(1+m^{2}\right) \\
\text { or } & 9-12 m+4 m^{2} \equiv 9+9 m^{2} \\
& \text { or } \quad 5 m^{2}+12 m=0 \quad \text { i.e., } m=0, \frac{-12}{5}
\end{aligned}
$$

Inserting these values of $m$ into (1), we have equations of the tangents from $(2,3)$ to the circle as :

$$
\begin{aligned}
& \text { For } m=0: y=0 . x+3 \sqrt{1+0} \\
& \text { or } y=3 \\
& \text { For } m=\frac{-12}{5}: y=\frac{-12}{5} x+3 \sqrt{1+\frac{144}{25}}=\frac{-12}{5} x+\frac{39}{5} \\
& \text { or } \quad 5 y+12 x-39=0
\end{aligned}
$$

Example 4: Write equations of the tangents to the circle

$$
x^{2}+y^{2}-4 x+6 y+9 \equiv 0
$$

at the points on the circle whose ordinate is -2 .

Solution: Substituting $y=-2$ into (1), we get

$$
\begin{aligned}
& x^{2}-4 x+1 \equiv 0 \\
& \text { or } \quad x=\frac{4 \pm \sqrt{16-4}}{2} \quad \pm 2 \quad \sqrt{3}
\end{aligned}
$$

The points on the circle with ordinate -2 are

$$
(2+\sqrt{3},-2),(2-\sqrt{3},-2)
$$

Equations of the tangents to (1) at these points are

$$
\begin{aligned}
& (2+\sqrt{3}) x-2 y-2(x+2+\sqrt{3})+3(y-2)+9=0 \\
& \text { and } \quad(2-\sqrt{3}) x-2 y-2(x+2-\sqrt{3})+3(y-2)+9=0 \\
& \text { i.e., } \quad \sqrt{3} x+y-2 \sqrt{3}-1=0 \\
& \text { and } \quad-\sqrt{3} x+y+2 \sqrt{3}-1=0
\end{aligned}
$$

## Example 5: $\quad$ Find a joint equation to the pair of tangents drawn from $(5,0)$ to the circle:

$$
x^{2}+y^{2}=9
$$

Solution: Let $P(h, k)$ be any point on either of the two tangents drawn from $A(5,0)$ to the given circle (1). Equation of $P A$ is

$$
y-0=\frac{k-0}{h-5}(x-5) \quad \text { or } k x-(h-5) y-5 k=0
$$

Since (2) is tangent to the circle (1), the perpendicular distance of (2) from the centre of the circle equals the radius of the circle.
i.e., $\quad \frac{|-5 k|}{\sqrt{k^{2}+(h-5)^{2}}}=3$
or $\quad 25 k^{2}=9\left[k^{2}+(h-5)^{2}\right]$ or $16 k^{2}-9(h-5)^{2}=0$
Thus $(h, k)$ lies on

$$
9(x-5)^{2}-16 y^{2} \equiv 0
$$

But $(h, k)$ is any point of either of the two tangents.
Hence (3) is the joint equations of the two tangents.

### 6.2.1 Length of the tangent to a circle (Tangential Distance)

Let $P\left(x_{i}, y_{i}\right)$ be a point outside the circle

$$
x^{2}+y^{2}+2 g x+2 f y+c \equiv 0
$$

We know that two real and distinct tangents can be drawn to the circle from an external point $P$. If the points of contact of these tangents with the circle are $S$ and $T$, then each of the length $P S$ and $P T$ is called length of the tangent or tangential distance from $P$ to the circle (1).

The centre of the circle has coordinates $(-g,-f)$. Join $P O$ and $O T$. From the right triangle $O P T$ we have,

$$
\begin{aligned}
\text { length of the tangent } & =\frac{|P T|}{\sqrt{O P^{2}-O T^{2}}} \\
& =\sqrt{\left(x_{i}+g\right)^{2}+\left(y_{i}+f\right)^{2}-\left(g^{2}+f^{2}-c\right)}
\end{aligned}
$$

version: 1.1

$$
=\sqrt{x_{1}^{2}+y_{1}^{2}+2 g x_{1}+2 f y_{1}+c}
$$

It is easy to see that length of the second tangent $\overrightarrow{P S}$ also equals (2).
Example 6: Find the length of the tangent from the point $P(-5,10)$ to the circle

$$
5 x^{2}+5 y^{2}+14 x+12 y-10=0
$$

Solution: Equation of the given circle in standard form is

$$
x^{2}+y^{2}+\frac{14}{5} x+\frac{12}{5} y-2=0
$$

Square of the length of the tangent from $P(-5,10)$ to the circle (1) is obtained by substituting -5 for $x$ and 10 for $y$ in the left hand member of (1)

$$
\therefore \quad \text { Required length } \quad=\sqrt{(-5)^{2}+(10)^{2}-14+24-2}=\sqrt{133}
$$

Example 7: Write equations of the tangent lines to the circle $x^{2}+y^{2}+4 x+2 y=0$ drawn from $P(-1,2)$. Also find the tangential distance.

Solution: An equation of the line through $P(-1,2)$ having slope $m$ is

$$
y-2=m(x+1) \text { or } \quad m x-y+m+2=0
$$

Centre of the circle is $C(-2,-1)$.

$$
\text { Radius }=\sqrt{4+1}=\sqrt{5}
$$

If (1) is tangent to the circle, then its distance from the centre of the circle equals the radius of the circle. Therefore

$$
\frac{[-2 m+1+m+2]}{\sqrt{m^{2}+1}}=\sqrt{5}
$$

or $\quad(-m+3)^{2}=5\left(m^{2}+1\right)$
or $\quad 4 m^{2}+6 m-4=0$ or $2 m^{2}+3 m-2=0$

$$
m=\frac{-3 \pm \sqrt{9+16}}{4}=\frac{-3 \pm 5}{4}=-2, \frac{1}{2}
$$

Equations of the tangents are from equation (1)

$$
\text { version: } 1.1
$$

For $m=-2:-2 x-y=0$ or $2 x+y=0$
For $m=\frac{1}{2}: \frac{1}{2} x-y+\frac{5}{2}=0$ or $x-2 y+5=0$
Tangential distance $=\sqrt{1+4-4+4}=\sqrt{5}$
Example 8: Tangents are drawn from $(-3,4)$ to the circle $x^{2}+y^{2}=21$. Find an equation of the line joining the points of contact (The line is called the chord of contact).

Solution: Let the points of contact of the two tangents be $P\left(x_{1}, y_{1}\right)$ and $Q\left(x_{2}, y_{2}\right)$
An equation of the tangent at $P$ is

$$
x x_{1}+y y_{1}=21
$$

An equation of the tangent at $Q$ is

$$
x x_{2}+y y_{2}=21
$$

Since (1) and (2) pass through $(-3,4)$, so

$$
-3 x_{1}+4 y_{1}=21
$$

and $-3 x_{2}+4 y_{2}=21$
(3) and (4) show that both the points $P\left(x_{1}, y_{1}\right), Q\left(x_{2}, y_{2}\right)$ lie on $-3 x+4 y=21$ and so it is the required equation of the chord of contact.

## EXERCISE 6.2

1. Write down equations of the tangent and normal to the circle
(i) $x^{2}+y^{2}=25$ at $(4,3)$ and at $(5 \cos \theta, 5 \sin \theta)$
(ii) $3 x^{2}+3 y^{2}+5 x-13 y+2=0$ at $\left(1, \frac{10}{3}\right)$
2. Write down equations of the tangent and normal to the circle $4 x^{2}+4 y^{2}-16 x+24 y-117=0$
at the points on the circle whose abscissa is -4 .
3. Check the position of the point $(5,6)$ with respect to the circle
(i) $x^{2}+y^{2}=81$
(ii) $2 x^{2}+2 y^{2}+12 x-8 y+1=0$
4. Find the length of the tangent drawn from the point $(-5,4)$ to the circle $5 x^{2}+5 y^{2}-10 x+15 y-131=0$

**5.** Find the length of the chord cut off from the line 2*x* + 3*y* = 13 by the circle *x*<sup>2</sup> + *y*<sup>2</sup> = 26

**6.** Find the coordinates of the points of intersection of the line *x* + 2*y* = 6 with the circle: *x*<sup>2</sup> + *y*<sup>2</sup> – 2*x* – 2*y* – 39 = 0

**7.** Find equations of the tangents to the circle *x*<sup>2</sup> + *y*<sup>2</sup> = 2
- (i) parallel to the line *x* – 2*y* + 1 = 0
- (ii) perpendicular to the line 3*x* + 2*y* = 6

**8.** Find equations of the tangents drawn from
- (i) (0, 5) to *x*<sup>2</sup> + *y*<sup>2</sup> = 16
- (ii) (−1, 2) to *x*<sup>2</sup> + *y*<sup>2</sup> + 4*x* + 2*y* = 0
- (iii) (−7, −2) to (*x* + 1)<sup>2</sup> + (*y* – 2)<sup>2</sup> = 26

Also find the points of contact

**9.** Find an equation of the chord of contact of the tangents drawn from (4, 5) to the circle *2x*<sup>2</sup> + 2*y*<sup>2</sup> – 8*x* + 12*y* + 21 = 0

### **6.3 ANALYTIC PROOFS OF IMPORTANT PROPERTIES OF A CIRCLE**

A line segment whose end points lie on a circle is called a **chord** of the circle. A **diameter** of a circle is a chord containing the centre of the circle.

**Theorem:** Length of a diameter of the circle *x*<sup>2</sup> + *y*<sup>2</sup> = *a*<sup>2</sup> is 2*a*.

**Proof:** Let *AOB* be a diameter of the circle

*a*<sup>2</sup> + *y*<sup>2</sup> = *a*<sup>2</sup>

(1)

*O*(0,0) is center of (1).

Let the coordinates of *A* be (*x*<sub>*1*</sub>, *y*<sub>*1*</sub>).

Equation of *AOB* is

$$
y = \frac{y_1}{x_1} x \qquad \text{(2)}
$$

Substituting the value of *y* from (2) into (1), we have

$$
x^2 + \frac{y_1^2}{x_1^2} x^2 = a^2 \quad \text{or} \quad x^2 (x_1^2 + y_1^2) = a^2 x_1^2
$$

or

$$
a^2 x^2 = a^2 x_1^2 \qquad \qquad \qquad \qquad \text{(3/ } x_1^2 + y_1^2 = x^2)
$$

i.e.,

$$
x = \pm x_1
$$

If

$$
x = x_1, \quad \text{then} \quad y = y_1 \qquad \text{(4/ } y = \frac{y_1}{x_1} x)
$$

Similarly when

$$
x = -x_1, \quad \text{then} \qquad y = -y_1
$$

Thus *B* has coordinates (−*x*<sub>*1*</sub>, −*y*<sub>*1*</sub>).

Length of diameter *AB* = $$\sqrt{(x_1 + x_1)^2 + (y_1 + y_1)^2}$$

$$
= \sqrt{4(x_1^2 + y_1^2)} = \sqrt{4a^2} = 2a
$$

**Theorem 2:** Perpendicular dropped from the centre of a circle on a chord bisects the chord.

**Proof:** Let *x*<sup>2</sup> + *y*<sup>2</sup> = *a*<sup>2</sup> be a circle, in which *AB* is a chord with end points *A*(*x*<sub>*1*</sub>, *y*<sub>*1*</sub>), *B*(*x*<sub>*2*</sub>, *y*<sub>*2*</sub>) on the circle and *OM* is perpendicular from the centre to the chord. We need to show that *OM* bisects the chord *AB*.

$$
\text{Slop of } AB = \frac{y_2 - y_1}{x_2 - x_1}
$$

$$
\text{Slop of perpendicular to } AB = \frac{-(x_2 - x_1)}{y_2 - y_1} = \frac{x_2 - x_1}{y_2 - y_1} = m \text{ (say)}
$$

So equation of *OM* with slope *m* and point *O*(0,0) on it, is given by

$$
y - 0 = \frac{(x_1 - x_1)}{(y_2 - y_1)}(x - 0) \qquad \text{(point - slope form)}
$$

or

$$
y = \left(\frac{x_1 - x_1}{y_2 - y_1}\right)x \qquad \text{(1)}
$$

(1) is the equation of the perpendicular $O M$ from centre to the chord. We will show that it bisects the chord i.e., intersection of $O M$ and $A B$ is the midpoint of $A B$.

Equation of $A B$ is

$$
y-y_{1}=\frac{y_{1}-y_{2}}{x_{1}-x_{2}}\left(x-x_{1}\right)
$$

The foot of the perpendicular $O M$ is the point of intersection of (1) and (2). Inserting the value of $y$ from (1) into (2), we have

$$
\begin{aligned}
& -\frac{x_{1}-x_{2}}{y_{1}-y_{2}} x-y_{1}=\frac{y_{1}-y_{2}}{x_{1}-x_{2}}\left(x-x_{1}\right) \\
\text { or } & x\left(\frac{y_{1}-y_{2}}{x_{1}-x_{2}}+\frac{x_{1}-x_{2}}{y_{1}-y_{2}}\right)=\frac{x_{1}\left(y_{1}-y_{2}\right)}{x_{1}-x_{2}}-y_{1} \\
\text { or } & \frac{x\left[y_{1}^{2}+y_{2}^{2}-2 y_{1} y_{2}+x_{1}^{2}+x_{2}^{2}-2 x_{1} x_{2}\right]}{\left(x_{1}-x_{2}\right)\left(y_{1}-y_{2}\right)}=\frac{x_{2} y_{1}-x_{1} y_{2}}{x_{1}-x_{2}} \\
\text { or } & x\left(2 a^{2}-2 x_{1} x_{2}-2 y_{1} y_{2}\right)=x_{2} y_{1}^{2}-x_{1} y_{1} y_{2}-x_{2} y_{1} y_{2}+x_{1} y_{2}^{2} \\
\text { or } & 2 x\left(a^{2}-x_{1} x_{2}-y_{1} y_{2}\right)=x_{2}\left(a^{2}-x_{1}^{2}\right)-y_{1} y_{2}\left(x_{1}+x_{2}\right)+x_{1}\left(a^{2}-x_{2}^{2}\right) \\
& \quad=a^{2}\left(x_{1}+x_{2}\right)-x_{1} x_{2}\left(x_{1}+x_{2}\right)-y_{1} y_{2}\left(x_{1}+x_{2}\right) \\
& \quad=\left(x_{1}+x_{2}\right)\left(a^{2}-x_{1} x_{2}-y_{1} y_{2}\right)
\end{aligned}
$$

(The points $\left(x_{1}, y_{1}\right)$ and $\left(x_{2}, y_{2}\right)$ lie on the circle)
or $\quad x=\frac{x_{1}+x_{2}}{2}$
Putting $\quad x=\frac{x_{1}+x_{2}}{2} \quad$ into (1), we get

$$
y=\frac{\left(x_{1}-x_{2}\right)}{y_{2}-y_{1}} \frac{\left(x_{1}+x_{2}\right)}{2} \quad \frac{x_{1}^{2}-x_{2}^{2}}{2\left(y_{2}-y_{1}\right)}
$$

or $\quad y=\frac{y_{2}^{2}-y_{1}^{2}}{2\left(y_{2}-y_{1}\right)}=\frac{\left(y_{2}-y_{1}\right)\left(y_{2}+y_{1}\right)}{2\left(y_{2}-y_{1}\right)} \quad\left[\begin{array}{l}x_{1}^{2}+y_{2}^{2}=a^{2} \\ x_{2}^{2}+y_{2}^{2}=a^{2} \\ \Rightarrow x_{1}^{2}-x_{2}^{2}=y_{1}^{2}-y_{2}^{2}\end{array}\right]$
So, $\quad\left(\frac{x_{1}+x_{2}}{2}, \frac{y_{1}+y_{2}}{2}\right)$ is the point of intersection of $O M$ and $A B$ which is the midpoint of $A B$.
version: 1.1

## Theorem 3:

The perpendicular bisector of any chord of a circle passes through the centre of the circle.

Proof: $\quad$ Let $x^{2}+y^{2}=a^{2}$ be a circle and $A\left(x_{1}, y_{1}\right)$,
$B\left(x_{2}, y_{2}\right)$ be the end points of a chord of this circle. Let $M$ be the mid point of $A B$, i.e.
$M\left(\frac{x_{1}+x_{2}}{2}, \frac{y_{1}+y_{2}}{2}\right)$
The slop of $A B=\frac{y_{2}-y_{1}}{x_{2}-x_{1}}$
The slope of perpendicular bisector of $A B$ is
$$
-\left(\frac{x_{2}-x_{1}}{y_{2}-y_{1}}\right)
$$

So, equation of perpendicular bisector in point-slope form, is

$$
y-\frac{y_{1}+y_{2}}{2}=\left(\frac{x_{2}-x_{1}}{y_{2}-y_{1}}\right)\left(x-\frac{x_{1}+x_{2}}{2}\right)
$$

We check whether the centre $(0,0)$ of the circle lies on (1) or not

$$
\begin{aligned}
& 0-\frac{y_{1}+y_{2}}{2}=\frac{-\left(x_{2}-x_{1}\right)}{\left(y_{2}-y_{1}\right)}\left(0-\frac{x_{1}+x_{2}}{2}\right) \\
\text { or } & -\left(\frac{y_{1}+y_{2}}{2}\right)\left(y_{2}-y_{1}\right)=\left(x_{2}-x_{1}\right) \frac{\left(x_{1}+x_{2}\right)}{2} \\
\text { or } & -\left(y_{2}^{2}-y_{1}^{2}\right)=x_{2}^{2}-x_{1}^{2} \text { or } x_{1}^{2}+y_{1}^{2}=x_{2}^{2}+y_{2}^{2} \\
\text { or } & a^{2}=a^{2} \quad \text { which is true }
\end{aligned}
$$

Hence the perpendicular bisector of any chord passes through the centre of the circle.

## Theorem 4:

The line joining the centre of a circle to the midpoint of a chord is perpendicular to the chord.

Proof: $\quad$ Let $A\left(x_{1}, y_{1}\right), B\left(x_{2}, y_{2}\right)$ be the end points of any chord the circle $x^{2}+y^{2}=a^{2} . O(0,0)$

is centre of the circle and *M* [ *x*<sup>1</sup> + *x*<sup>2</sup> + *y*<sup>1</sup> + *y*<sup>2</sup> ] is the midpoint of *AB*. Join the centre *O* with the mid point *M*. We need to show that *OM* is perpendicular to *AB* i.e., product of slopes of *AB* and *OM* is –1.

Slope of *AB* = *m*<sup>1</sup> = *x*<sup>1</sup> − *y*<sup>1</sup> *x*<sup>2</sup> − *x*<sup>1</sup> Slope of *OM* *m*<sup>2</sup> = *x*<sup>2</sup> − *y*<sup>2</sup> *x*<sup>2</sup> − *x*<sup>1</sup> *x*<sup>2</sup> − *x*<sup>1</sup> *2*

$$\therefore m_m = \frac{y_2 - y_1}{x_2 - x_1} \cdot \frac{y_2 + y_1}{x_2 + x_1} = \frac{y_2^2 - y_1^2}{x_2^2 - x_1^2} \tag{1}$$

As *A* and *B* lie on the circle, so

$$x_1^2 + y_1^2 = a^2 \quad \text{and} \quad x_2^2 + y_2^2 = a^2$$

Their subtraction gives *x*<sup>1</sup> − *x*<sup>2</sup> + *y*<sup>1</sup> − *y*<sup>2</sup> = 0

or *y*<sup>2</sup> − *y*<sup>1</sup> = *x*<sup>1</sup> − *x*<sup>2</sup> = −(*x*<sup>2</sup> − *x*<sup>1</sup>)

Putting this value in (1), we get

$$m_m = \frac{(x_1^2 - x_1^1)}{(x_2^2 - x_2^1)} \quad \text{I}$$

So *OM* is perpendicular to *AB*.

**Theorem 5:** Congruent chords of a circle are equidistant from the centre.

**Proof:** Let *x*<sup>2</sup> + *y*<sup>2</sup> = *a*<sup>2</sup> be the circle in which *AB* and *CD* are two congruent chords i.e., |*AB*| = |*CD*| and the coordinates of *A*, *B*, *C* and *D* be as in the figure. Also let *OM* and *ON* be the perpendicular distances of the chords from the centre (0, 0)(*x*<sub>1</sub>, *y*<sub>1</sub>) of the circle.

We know from Theorem 2 that *M* and *N* are the midpoints of *AB* and *CD* respectively.

**Theorem 6:** Show that measure of the central angle of a minor arc is double the measure of the angle subtended in the corresponding major arc.

**Proof:** Let the circle be *x*<sup>2</sup> + *y*<sup>2</sup> = *a*<sup>2</sup>. *A*(*a* cosθ<sub>1</sub>, *a* sinθ<sub>1</sub>) and *B*(*a* cosθ<sub>2</sub>, *a* sinθ<sub>2</sub>) be end points of a minor arc *AB*. Let *P* (*a* cosθ, *a* sinθ) be a point on the major arc. Central angle subtended by the minor arc *AB* is ∠ *AOB* = θ<sub>2</sub> − θ<sub>1</sub>.

We need to show *m*∠*APB* = $$\frac{1}{2}(\theta_1 - \theta_1)$$

**6.** *Conic Sections* **eLearn.Punjab**

### 6. *Conic Sections* **eLearn.Punjab**

**Theorem 1.1**

**Theorem 1.1**

$$
\begin{aligned}
m_{1}= & \text { slope of } A P \quad \frac{a(\sin \theta-\sin \theta_{1})}{a(\cos \theta-\cos \theta_{1})} \quad \frac{2 \cos \theta+\theta_{1}}{2} \sin \frac{\theta-\theta_{1}}{2} \\
& =\cot \left(\frac{\theta+\theta_{1}}{2}\right)-\tan \left(\frac{\pi}{2}-\frac{\theta+\theta_{1}}{2}\right)
\end{aligned}
$$

Similarly, (by symmetry)

$$
\begin{aligned}
& m_{2}=\text { slope-of } B P \quad+\tan \left(\frac{\pi}{2}-\frac{\theta+\theta_{2}}{2}\right) \\
& \tan \angle A P B=\frac{m_{2}-m_{1}}{1+m_{1} m_{2}}=\frac{\tan \left(\frac{\pi}{2}+\frac{\theta+\theta_{2}}{2}\right)-\tan \left(\frac{\pi}{2}+\frac{\theta+\theta_{1}}{2}\right)}{1+\tan \left(\frac{\pi}{2}+\frac{\theta+\theta_{1}}{2}\right) \tan \left(\frac{\pi}{2}+\frac{\theta+\theta_{2}}{2}\right)} \\
& =\tan \left(\frac{\pi}{2}+\frac{\theta+\theta_{2}}{2}-\frac{\pi}{2}-\frac{\theta+\theta_{1}}{2}\right)=\tan \left(\frac{\theta_{2}-\theta_{1}}{2}\right) \\
& \text { Hence } m \angle A P B=\frac{1}{2}\left(\theta_{2}-\theta_{1}\right)
\end{aligned}
$$

Theorem 7: An angle in a semi-circle is a right angle.
Proof: Let $x^{2}+y^{2}=a^{2}$ be a circle, with centre $O$. Let $A O B$ be any diameter of the circle and $P\left(x_{1}, y_{1}\right)$ be any point on the circle.

We have to show that $m \angle A P B=90^{\circ}$.
Suppose the coordinates of $A$ are $\left(x_{1}, y_{1}\right)$.
Then $B$ has coordinates
$\left\{-x_{1},-y_{1}\right\}$.
(Slope of $A P=\frac{y_{1}-y_{2}}{x_{1}-x_{2}}=m_{1}$, say
Slope of $B P=\frac{y_{1}+y_{2}}{x_{1}+x_{2}}=m_{2}$, say
Challenged
State and prove the converse of this Theorem.

$$
m_{1} m_{2}=\frac{y_{1}^{2}-y_{2}^{2}}{x_{1}^{2}-x_{2}^{2}}
$$

Since $A\left(x_{1}, y_{1}\right)$ and $P\left(x_{2}, y_{2}\right)$ lie on the circle, we have

$$
\begin{aligned}
& x_{1}^{2}+y_{1}^{2}=a^{2} \Rightarrow x_{1}^{2}=a^{2}-y_{1}^{2} \\
& x_{2}^{2}+y_{2}^{2}=a^{2} \Rightarrow x_{2}^{2}=a^{2}-y_{2}^{2}
\end{aligned}
$$

Substituting the values of $x_{1}^{2}$ and $x_{2}^{2}$ from (2) into (1), we get

$$
m_{1} m_{2}=\frac{y_{1}^{2}-y_{2}^{2}}{\left(a^{2}-y_{1}^{2}\right)-\left(a^{2}-y_{2}^{2}\right)}=\frac{y_{1}^{2}-y_{2}^{2}}{-\left(y_{1}^{2}-y_{2}^{2}\right)}=-1
$$

Thus $A P \perp B P$ and so $m \angle A P B=90^{\circ}$

Theorem 8: The tangent to a circle at any point of the circle is perpendicular to the radial segment at that point.

Proof: Let $P T$ be the tangent to the circle $x^{2}+y^{2}=a^{2}$ at any point $P\left(x_{1}, y_{1}\right)$ lying on it. We have to show that the radial segment $O P \perp P T$.

Differentiating $x^{2}+y^{2}=a^{2}$, we have

$$
2 x+2 y \frac{d y}{d x}=0 \Rightarrow \frac{d y}{d x}=\frac{x}{y}
$$

Slope of the tangent at $P=\frac{d y}{d x} \frac{1}{2}=\frac{-x_{1}}{y_{1}}$
Slope of $O P=\frac{y_{1}-0}{x_{1}-0}-\frac{y_{1}}{x_{1}}$
Product of slopes of $O P$ and $P T=\frac{-x_{1}}{y_{1}} \frac{y_{1}}{x_{1}}=-1$
Thus $O P \perp P T$.

Theorem 9: The perpendicular at the outer end of a radial segment is tangent to the circle.

Proof: Let $P T$ be the perpendicular to the outer end of the radial segment $O P$ of the circle $x^{2}+y^{2} \equiv a^{2}$. We have to show that $P T$ is tangent to the circle at $P$. Suppose the coordinates of $P$ are $\left(x_{1}, y_{1}\right)$.

Since $P T$ is perpendicular to $O P$ so
Slope of $P T=\frac{-1}{\text { slope of } O P} \cdot \frac{-1}{y_{1}} \cdot \frac{-x_{1}}{y_{1}}$
Equation of $P T$ is $y-y_{1}=\frac{-x_{1}}{y_{1}}\left(x-x_{1}\right)$
or $y y_{1}-y^{2}=-x x_{1}+x_{1}^{2}$
or $y y_{1}+x x_{1}=y_{1}^{2}+x_{1}^{2}=a^{2} \quad(\because P$ lies on the circle $)$
or $y y_{1}+x x_{1}-a^{2}=0$
Distance of $P T$ from $O$ (centre of the circle)

$$
=\frac{\left[y_{1}(0)+x_{1}(0)-a^{2}\right]}{\sqrt{x^{2}+y^{2}}} \cdot \frac{\left|a^{2}\right|}{\sqrt{a^{2}}} \cdot \frac{a^{2}}{a} \quad a \quad \text { (radius of the circle) }
$$

Thus $P T$ is tangent to the circle at $P\left(x_{1}, y_{1}\right)$.

## EXERCISE 6.3

1. Prove that normal lines of a circle pass through the centre of the circle.
2. Prove that the straight line drawn from the centre of a circle perpendicular to a tangent passes through the point of tangency.
3. Prove that the mid point of the hypotenuse of a right triangle is the circumcentre of the triangle.
4. Prove that the perpendicular dropped from a point of a circle on a diameter is a mean proportional between the segments into which it divides the diameter.

In the following pages we shall study the remaining three conics.
Let $L$ be a fixed line in a plane and $F$ be a fixed point not on the line $L$.

Suppose $|P M|$ denotes the distance of a point $P(x, y)$ from the line $L$. The set of all points $P$ in the plane such that

$$
\frac{|P F|}{|P M|}=e . \quad(\text { a positive constant })
$$

is called a conic section.
(i) If $e \equiv 1$, then the conic is a parabola.
(ii) If $0<e<1$, then the conic is an ellipse.
(iii) If $e>1$, then the conic is a hyperbola.

The fixed line $L$ is called a directrix and the fixed point $F$ is called a focus of the conic. The number e is called the eccentricity of the conic.

### 6.4 PARABOLA

We have already stated that a conic section is a parabola if $e \equiv 1$.
We shall first derive an equation of a parabola in the standard form and study its important properties.

If we take the focus of the parabola as $F(a, 0), a>0$ and its directrix as line $L$ whose equation is $x \equiv-a$, then its equation becomes very simple.

Let $P(x, y)$ be a point on the parabola. So, by definition

$$
\frac{|P F|}{|P M|}=4 . \quad \text { or } \quad|P F||P M|
$$

Now $|P M|=x+a$
and $|P F|=\sqrt{(x-a)^{2}+(y-0)^{2}}$
Substituting into (1), we get

$$
\begin{aligned}
& \sqrt{(x-a)^{2}+y^{2}}=x+a \\
& (x-a)^{2}+y^{2}=(x+a)^{2}
\end{aligned}
$$

or

$$
y^{2}=(x+a)^{2}-(x-a)^{2}=4 a x \quad \text { or } \quad y^{2}=4 a z
$$

which is standard equation of the parabola.

## Definitions

(i) The line through the focus and perpendicular to the directrix is called axis of the parabola. In case of (2), the axis is $y=0$.
(ii) The point where the axis meets the parabola is called vertex of the parabola. Clearly the equation (2) has vertex $A(0,0)$. The line through $A$ and perpendicular to the axis of the parabola has equation $x=0$. It meets the parabola at coincident points and so it is a tangent to the curve at $A$.
(iii) A line joining two distinct points on a parabola is called a chord of the parabola. A chord passing through the focus of a parabola is called a focal chord of the parabola. The focal chord perpendicular to the axis of the parabola (1) is called latusrectum of the parabola. It has an equation $x=a$ and it intersects the curve at the points where

$$
y^{2}=4 a^{2} \quad \text { or } \quad y= \pm 2 a
$$

Thus coordinates of the end points $L$ and $L^{\prime}$ of the latusrectum are

$$
L(a, 2 a) \text { and } L^{\prime}(a,-2 a)
$$

The length of the latusrectum is $\left|L L^{\prime}\right|=4 a$.
(iv) The point $\left(a t^{2}, 2 a t\right)$ lies on the parabola $y^{2}=4 a x$ for any real $t$.

$$
x=a t^{2}, y=2 a t
$$

are called parametric equations of the parabola $y^{2}=4 a x$.

### 6.4.1 General Form of an Equation of a Parabola

Let $F(h, k)$ be the focus and the line $l x+m y+n=0$ be the directrix of a parabola. An equation of the parabola can be derived by the definition of the parabola. Let $P(x, y)$ be a point on the parabola. Length of the perpendicular $P M$ from $P(x, y)$ to the directrix is given by;

$$
|P M|=\frac{|l x+m y+n|}{\sqrt{l^{2}+m^{2}}}
$$

By definition, $(x-h)^{2}+(y-k)^{2}=\frac{(l x+m y+n)^{2}}{l^{2}+m^{2}}$
is an equation of the required parabola.
A second degree equation of the form

$$
a x^{2}+b y^{2}+2 g x+2 f y+c=0
$$

with either $a=0$ or $b=0$ but not both zero, represents a parabola. The equation can be analyzed by completing the square.

### 6.4.2 Other Standard parabolas

There are other choices for the focus and directrix which also give standard equations of parabolas.
(i) If the focus lies on the $y$-axis with coordinates $F(0, a)$ and directrix of the parabola is $y=-a$, then equation of the parabola is

$$
x^{2}=4 a y
$$

The equation can be derived by difinition.
(ii) If the focus is $F(0,-a)$ and directrix is the line $y=a$, then equation of the parabola is

$$
x^{2}=-4 a y
$$

Opening of the parabola is upward in case of (3) and downward in case of (4). Both the curves are symmetric with respect to the $y$-axis.
The graphs of (3) and (4) are shown below.
(iii) If the focus of the parabola is $F(-a, 0)$, and its directrix is the line $x=a$, then equation of the parabola is

$$
y^{2}=-4 a x
$$

The curve is symmetric with respect to the $x$-axis and lies in the second and third quadrants only. Opening of the parabola is to the left as shown in the figure
## **6.4.3 Graph of the Parabola**

$$y^2 = 4ax$$

We note that corresponding to each positive value of *x* there are two equal and opposite values of *y*. Thus the curve is symmetric with respect to the *x*–axis. The curve passes through the origin and *x* = 0 is tangent to the curve at (0,0). If *x* is negative, then *y* is negative and so *y* is imaginary. Thus no portion of the curve lies on the left of the *y*–axis. As *x* increases, *y* also increases numerically so that the curve extends to infinity and lies in the first and fourth quadrants. Opening of the parabola is to the right of *y*–axis.

Sketching graphs of other standard parabolas is similar and is left as an exercise.

|  **S. No.** | **1** | **2** | **3** | **4**  |
| --- | --- | --- | --- | --- |
|  **Equation** | $$y^2 = 4ax$$ | $$y^2 = -4ax$$ | $$x^2 = 4ay$$ | $$x^2 = -4ay$$  |
|  **Focus** | (a, 0) | (-a, 0) | (0, a) | (0, -a)  |
|  **Directrix** | *x* = *-a* | *x* = *a* | *y* = *-a* | *y* = *a*  |
|  **Vertex** | (0,0) | (0,0) | (0,0) | (0,0)  |
|  **Axis** | *y* = 0 | *y* = 0 | *x* = 0 | *x* = 0  |
|  **Latusrectum** | *x* = *a* | *x* = *-a* | *y* = *a* | *y* = *-a*  |
|  **Graph** |  |  |  |   |

**Example 1:** Analyze the parabola *x* = -16*y* and draw its graph.

**Solution.** We compare the given equation with *x* = -4*ay*

**Version:** 1.1

Here: - 4*a* = 16 - *a* = 4.

The focus of the parabola lies on the *y*-axis and its opening is downward. Coordinates of the focus = (0, -4).

Equation of its axis is *x* = 0.

Length of the latusrectum is 16 and *y* = 0 is tangent to the parabola at its vertex. The shape of the curve is as shown in the figure.

**Example 2.** Find an equation of the parabola whose focus is *F* (-3, 4) and directrix is 3*x* - 4*y* + 5 = 0.

**Solution:** Let *P*(*x*, *y*) be a point on the parabola. Length of the perpendicular |*P*| from *P*(*x*, *y*) to the directrix 3*x* - 4*y* + 5 = 0 is

$$\left| \frac{3x - 4y + 5}{3^2 + (-4)^2} \right|$$

By definition, |*P*| = |*P*| or |*P*| = |*P*|

or

$$(x + 3)^2 + (y - 4)^2 = \frac{(3x - 4y + 5)^2}{25}$$

or

$$25(x^2 + 6x + 9 + y^2 - 8y + 16) = 9x^2 + 16y^2 + 25 - 24xy + 30x - 40y$$

or

$$16x^2 + 24xy + 9y^2 + 120x - 160y + 600 = 0$$

is an equation of the required parabola.

**Example 3.** Analyze the parabola

$$x^2 - 4x - 3y + 13 = 0$$

and sketch its graph.

**Solution.** The given equation may be written as

$$x^2 - 4x + 4 = 3y - 9$$

or

$$(x - 2)^2 = 3(y - 3)$$

Let: - 2 = *X*, - *y* - 3 = *Y*

The equation (2) becomes *X* = 3*Y*

**Version:** 1.1

which is a parabola whose focus lies on $X=0$ and whose directrix is $Y=\frac{-3}{4}$ Thus coordinates of the focus of (3) are

$$
\begin{aligned}
& X=0, Y=\frac{-3}{4} \\
& \text { i.e., } \quad x-2=0-\quad \text { and } \quad y \quad 3 \quad \frac{3}{4} \\
& \text { or } \quad x=2, y=\frac{15}{4}
\end{aligned}
$$

Thus coordinates of the focus of the parabola
(1) are $\left(2, \frac{15}{4}\right)$

Axis of (3) is $X=0$ or $x-2=0$ is the axis of (1).
Veitex of (3) has coordinates

$$
\begin{aligned}
& X=0, Y=0 \\
& \text { or } \quad x-2=0, y-3=0
\end{aligned}
$$

i.e., $x=2, y=3$ are coordinates of the vertex of (1).

Equation of the directrix of (3) is
$Y=\frac{-3}{4}$ i.e. $y-3=\frac{-3}{4}$ or $y=\frac{9}{4}$ is an equation of the directrix of (1).
Magnitude of the latusrectum of the parabola (3) and also of (1) is 3.
The graph of (1) can easily be sketched and is as shown in the above figure.

Theorem: The point of a parabola which is closest to the focus is the vertex of the parabola.
Proof: Let the parabola be

$$
x^{2}=4 a y, a>0
$$

with focus at $F(0, a)$ and $P(x, y)$ be any point on the parabola.

$$
\begin{aligned}
& |P F|=\sqrt{x^{2}+(y-a)^{2}} \\
& =\sqrt{4 a y+(y-a)^{2}} \\
& =y+a
\end{aligned}
$$

$$
\text { version: } 1.1
$$

Since $y$ can take up only non-negative values, $|P F|$ is minimum when $y=0$. Thus $P$ coincides with $A$ so that of all points on the parabola, its vertex $A$ is closest to the focus.

Example 4. A comet has a parabolic orbit with the sun at the focus. When the comet is 100 million km from the sun, the line joining the sun and the comet makes an angle of $60^{\circ}$ with the axis of the parabola. How close will the comet get to the sun?

Solution. Let the sun $S$ be the origin. If the vertex of the parabola has coordinates $(-a, 0)$ then directrix of the parabola is

$$
x=-2 a, \quad(a>0)
$$

if the comet is at $P(x, y)$, then
by definition $|P S|=|P M|$
i,e., $x^{2}+y^{2}=(x+2 a)^{2}$
or $y^{2}=4 a x+4 a^{2}$ is orbit of the comet
Now $|P S|=\sqrt{x^{2}+y^{2}}$

$$
=x+2 a=100,000,000
$$

The comet is closest to the sun when it is at $A$.
Now $\quad x=P S \cos 60^{\circ}$

$$
|x|=\frac{|P S|}{2}=\frac{x+2 a}{2}
$$

or $\quad \frac{x+2 a}{|x|}=\frac{2}{1} \quad$ or $\quad \frac{x+2 a}{2 a} \quad 2=,(|x| \quad|-2 a| \quad 2 a)$
or $\quad \frac{100,000,000}{2 a}=2$
or $\quad a=25,000,000$
Thus the comet is closest to the sun when it is $25,000,000 \mathrm{~km}$ from the sun.

## Reflecting Property of the parabola.

A frequently used property of a parabola is its reflecting property. If a light source is placed at the focus of a parabolic reflecting surface then a light ray travelling from $F$ to a point $P$ on the parabola will be reflected in the direction $P R$ parallel to the axis of the parabola.

The designs of searchlights, reflecting telescopes and microwave antenas are based on reflecting property of the parabola.

Another application of the parabola is in a Suspension bridge. The main cables are of parabolic shape. The total weight of the bridge is uniformly distributed along its length if the shape of the cables is parabolic. Cables in any other shape will not carry the weight evenly.

Example 6. A suspension bridge with weight uniformly distributed along the length has two towers of 100 m height above the road surface and are 400 m apart. The cables are parabolic in shape and are tangent to road surface at the centre of the bridge. Find the height of the cables at a point 100 m from the centre.

Solution. The parabola formed by the $P$ cables $(1,200,100)$ has $A(0,0)$ as vertex and focus on the $y$-axis. An equation of this parabola is $x^{2}=4 a y$.

The point $Q(200,100)$ lies on the parabola and so
$(200)^{2}=4 a \times 100$
or $\quad a=100$
Thus an equation of the parabola is

$$
x^{2}=400 y
$$

To find the height of the cables when $x=100$, we have from (1)

$$
(100)^{2}=400 y
$$

or $\quad y=25$
Thus required height $=25 \mathrm{~m}$

## EXERCISE 6.4

1. Find the focus, vertex and directrix of the parabola. Sketch its graph.
(i) $y^{2}=8 x$
(ii) $x^{2}=-16 y$
(iii) $x^{2}=5 y$
(iv) $y^{2}=-12 x$
(v) $x^{2}=4(y-1)$
(vi) $y^{2}=-8(x-3)$
(vii) $(x-1)^{2}=8(y+2)$
(viii) $y=6 x^{2}-1$
(ix) $x+8-y^{2}+2 y=0$
(x) $x^{2}-4 x-8 y+4=0$
version: 1.1
2. Write an equation of the parabola with given elements.
(i) Focus $(-3,1)$; directrix $x=3$
(ii) Focus $(2,5)$; directrix $y=1$
(iii) Focus $(-3,1)$; directrix $x-2 y-3=0$
(iv) Focus $(1,2)$; vertex $(3,2)$
(v) Focus $(-1,0)$; vertex $(-1,2)$
(vi) Directrix $x=-2$; Focus $(2,2)$
(vii) Directrix $y=3$; vertex $(2,2)$
(viii) Directrix $y=1$, length of latusrectum is 8 . Opens downward.
(ix) Axis $y=0$, through $(2,1)$ and $(11,-2)$
(x) Axis parallal to $y$-axis, the points $(0,3),(3,4)$ and $(4,11)$ lie on the graph.
3. Find an equation of the parabola having its focus at the origon and directrix, parallel to the (i) $x$-axis (ii) $y$-axis.
4. Show that an equation of the parabola with focus at ( $a \cos \alpha, a \sin \alpha$ ) and directrix $x \cos \alpha+y \sin \alpha+a=0$ is
$(x \sin \alpha-y \cos \alpha)^{2}=4 a(x \cos \alpha+y \sin \alpha)$
5. Show that the ordinate at any point $P$ of the parabola is a mean proportional between the length of the latus rectum and the abscissa of $P$.
6. A comet has a parabolic orbit with the earth at the focus. When the comet is 150,000 km from the earth, the line joining the comet and the earth makes an angle of $30^{\circ}$ with the axis of the parabola. How close will the comet come to the earth?
7. Find an equation of the parabola formed by the cables of a suspension bridge whose span is $a \mathrm{~m}$ and the vertical height of the supporting towers is $b \mathrm{~m}$.
8. A parabolic arch has a 100 m base and height 25 m . Find the height of the arch at the point 30 m from the centre of the base.
9. Show that tangent at any point $P$ of a parabola makes equal angles with the line $P F$ and the line through $P$ parallel to the axis of the parabola, $F$ being focus. (These angles are called respectively angle of incidence and angle of reflection).

### 6.5 ELLIPSE AND ITS ELEMENTS

We have already stated that a conic section is an ellipse if $e<1$.
Let $0<e<1$ and $F$ be a fixed point and $L$ be a fixed line not containing $F$. Let $P(x, y)$ be a point in the plane and $|P M|$ be the perpendicular distance of $P$ from $L$.
The set of all points $P$ such that

$$
\left|\frac{P F}{P M}\right|=e
$$

is called an ellipse.
The number e is eccentricity of the ellipse, $F$ a focus and $L$ a directrix.

### 6.5.1 Standard Form of an Ellipse

Let $F(-c, 0)$ be the focus and line $x=\frac{-c}{e^{2}}$ be the directix of an ellipse with eccentricity $e$, $(0<e<1)$. Let $P(x, y)$ be any point on the ellipse and suppose that $|P M|$ is the perpendicular distance of $P$ from the directrix. Then

$$
|P M|=x+\frac{c}{e^{2}}
$$

The condition $|P F|=e|P M|$ takes the analytic form

$$
(x+c)^{2}+y^{2}=e^{2}\left(x+\frac{c}{e^{2}}\right)^{2}
$$

$$
\text { or } \quad x^{2}+2 c x+c^{2}+y^{2}=e^{2} x^{2}+2 c x+\frac{c^{2}}{e^{2}} \quad \text { or } \quad x^{2}\left(4 e^{2}\right)+y^{2}=\frac{e^{2}}{e^{2}}\left(4 e^{2}\right)
$$

version: 1.1
or $x^{2}\left(1-e^{2}\right)+y^{2}=a^{2}\left(1-e^{2}\right)$. where $\frac{c}{e} a$
or $\quad \frac{x^{2}}{a^{2}}+\frac{y^{2}}{a^{2}\left(1-e^{2}\right)}=1$
If we write $b^{2}=a^{2}\left(1-e^{2}\right)$, then (1) takes the form

$$
\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1
$$

which is an equation of the ellipse in the standard form.
Moreover, eccentricity of the ellipse is $e=\frac{c}{a}$.
We have $b^{2}=a^{2}\left(1-e^{2}\right)$
(i) From the relation $b^{2}=a^{2}\left(1-e^{2}\right)$, we note that $b<a$
(ii) Since we set $\frac{c}{e}=a$, the focus $F$ has coordinates $(-a e, 0)$ and equation of the directrix is $x=\frac{-a}{e}$.
(iii) If we take the point $(a e, 0)$ as focus and the line $x=\frac{a}{e}$ as directrix, it can be seen easily that we again obtain equation (2). Thus the ellipse (2) has two foci $(-a e, 0)$ and $(a e, 0)$ and two directrices $x=\pm \frac{a}{e}$.
(iv) The point (acos $\theta$, bsin $\theta$ ) lies on (2) for all real $\theta . x=\operatorname{acos} \theta, y=b \sin \theta$ are called parametric equations of the ellipse (2).
(v) If in (2), $b=a$ then it becomes

$$
x^{2}+y^{2}=a^{2}
$$

which is a circle. In this case $b^{2}=a^{2}\left(1-e^{2}\right)=a^{2}$ and so $e=0$. Thus circle is a special case of an ellipse with eccenctricty 0 and foci tending to the centre.
Definitions: Let $F^{\prime}$ and $F$ be two foci of the ellipse

$$
\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1
$$

- (i) The midpoint *C* of *FF'* is called the **centre** of the ellipse. In case of (1) coordinates of *C* are (0,0).
- (ii) The intersection of (1) with the line joining the foci are obtained by setting *y* = 0 into (1). These are the points *A*<sup>0</sup>(−*a*, 0) and *A*(*a*, 0). The points *A* and *A'* are called **vertices** of the ellipse.
- (iii) The line segment *AA'* = 2*a* is called the **major axis** of the ellipse. The line through the centre of (1) and perpendicular to the major axis has its equation as *x* = 0. It meets (1) at points *B'* (0, *b*) and *B'* (0,−*b*). The line segment *BB'* = 2*b* is called the **minor axis** of the ellipse and *B'*, *B'* are some-times called the **covertices** of the ellipse. Since *b*<sup>2</sup> = *a*<sup>2</sup>(1 − *e*<sup>2</sup>) and *e* < 1, the length of the major axis is greater than the length of the minor axis. (See figure)
- (iv) Foci of an ellipse always lie on the major axis.
- (v) Each of the focal chords *LFL'* and *NF'N'* perpendicular to the major axis of an ellipse is called a **latusrectum** of the ellipse. Thus there are two **laterarecta** of an ellipse. It is an easy exercise to find that length of each latusrectum is *2b*<sup>2</sup> *a*. (See problem 5).
- (vi) If the foci lie on the *y*–axis with coordinates (0,−*ae*) and (0,*ae*), then equation of the ellipse is

$$
\frac{x^2}{b^2} + \frac{y^2}{a^2} = 1 \quad \text{or} \quad a > b.
$$

The reader is urged to derive this equation.

#### 6.5.2 Graph of an Ellipse

Let an equation of the ellipse be

$$
\frac{x^2}{a^2} + \frac{y^2}{b^2} > 1
$$

Since only even powers of both *x* and *y* occur in (1), the curve is symmetric with respect to both the axes.

From (1), we note that

$$
\frac{x^2}{a^2} \leq 1 \quad \text{and} \quad \frac{y^2}{b^2} \leq 1
$$

i.e.,

$$
\frac{x^2}{a^2} \leq a^2 \quad \text{and} \quad y^2 \leq b^2
$$

or

$$
-a \leq x \leq a \quad \text{and} \quad -b \leq y \leq b
$$

Thus all points of the ellipse lie on or within the rectangle (2). The curve meets the *x*-axis at *A*(−*a*, 0) and *A'*(*a*, 0) and it meets the *y*-axis at *B*(0,−*b*), *B'* (0, *b*). The graph of the ellipse can easily be drawn as shown in the following figure.

The graph of the ellipse

$$
\frac{x^2}{b^2} + \frac{y^2}{a^2} = 1, \quad a > b
$$

can be sketched as in the case of (1). Its shape is shown in above figure (ii).

# **6. Conic Sections**

|  **Summary of standard Ellipses** |  |   |
| --- | --- | --- |
|  **Equation** | $$ \frac{x^2}{a^2} + \frac{y^2}{b^2} = 1, a > b $$
$$ c^2 = a^2 - b^2 $$ | $$ \frac{x^2}{b^2} + \frac{y^2}{a^2} = 1, a > b $$
$$ c^2 = a^2 - b^2 $$  |
|  **Foci** | (∆c, 0) | (0, ∆c)  |
|  **Directrices** | $$ x = \pm \frac{c}{e^2} $$ | $$ y = \pm \frac{c}{e^2} $$  |
|  **Major axis** | $$ y = 0 $$ | $$ x = 0 $$  |
|  **Vertices** | (∆a, 0) | (0, ∆a)  |
|  **Convertices** | (0, ∆b) | (∆b, 0)  |
|  **Centre** | (0, 0) | (0, 0)  |
|  **Eccentricity** | $$ e = \frac{c}{a} < 1 $$ | $$ e = \frac{c}{a} < 1 $$  |
|  **Graph** |  |   |
|  |   |   |
|  |   |   |
|  **Note:** In each ellipse |  |   |
|  Length of major axis = 2a, Length of minor axis = 2b |  |   |
|  Length of Latusrectum = $$\frac{2b^2}{a}$$, Foci lie on the major axis |  |   |

**Example 1.** Find an equation of the ellipse having centre at (0,0), focus at (0,−3) and one vertex at (0,4). Sketch its graph.

**Solution.** The second vertex has coordinates (0, −4). Length of the semi-major axis is

$$ a = 4 $$

Also

$$ c = 3 $$

From $$ b^2 = a^2 - c^2 $$, we have

$$ b^2 = 16 - 9 = 7 $$

$$ b = \sqrt{7} $$ which is length of the semi-minor axis. Since the foci lie on the y-axis; equation of the ellipse is

$$ \frac{y^2}{16} + \frac{x^2}{7} = 1 $$

The graph is as shown above.

**Example 2.** Analyze the equation

$$ 4x^2 + 9y^2 = 36 $$

and sketch its graph.

**Solution:** The given equation may be written as

$$ \frac{x^2}{a} + \frac{y^2}{a} = 1 $$

which is standard form of an ellipse. Semi-major axis $$ a = 3 $$ Semi-minor axis $$ b = 2 $$ From $$ b^2 = a^2 - c^2 $$, we have

$$ c^2 = b^2 - a^2 = 9 - 4 = 5 $$

or

$$ c = \pm \sqrt{5} $$

For

$$ F(-\sqrt{5}, 0), \quad F'(\sqrt{5}, 0); \quad \text{Vertices:} \quad A(-3, 0), A'(3, 0) $$

**40**

**41**

C
Example 4. An arch in the form of half an ellipse is 40 m wide and 15 m high at the centre. Find the height of the arch at a distance of 10 m from its centre.

Solution: Let the $x$-axis be along the base of the arch and the $y$-axis pass through its centre. An equation of the ellipse representing the arch is

$$
\frac{x^{2}}{20^{2}}+\frac{y^{2}}{15^{2}}=1
$$

Let the height of an arch at a distance of 10 m from the centre be $y$. Then the points $(10, y)$ lies on (1)

For $x=10$, we have

$$
\begin{aligned}
& \frac{y^{2}}{15^{2}}=1-\frac{1}{4}=\left(\frac{\sqrt{3}}{2}\right)^{2} \\
& \text { so that } y=\frac{15 \sqrt{3}}{2} \\
& \text { Required height }=\frac{15 \sqrt{3}}{2} m
\end{aligned}
$$

## EXERCISE 6.5

1. Find an equation of the ellipse with given data and sketch its graph:
(i) Foci $( \pm 3,0)$ and minor axis of length 10
(ii) Foci $(0,-1)$ and $(0,-5)$ and major axis of length 6 .
(iii) Foci $(-3 \sqrt{3}, 0)$ and vertices $( \pm 6,0)$
(iv) Vertices $(-1,1),(5,1)$; foci $(4,1)$ and $(0,1)$
(v) Foci $( \pm \sqrt{5}, 0)$ and passing through the point $\left(\frac{3}{2}, \sqrt{3}\right)$
(vi) Vertices $(0, \pm 5)$, eccentricity $\frac{3}{5}$.
(vii) Centre $(0,0)$, focus $(0,-3)$, vertex $(0,4)$
(viii) Centre $(2,2)$, major axis parallel to $y$-axis and of length 8 units, minor axis parallel to $x$-axis and of length 6 units.
(ix) Centre $(0,0)$, symmetric with respect to both the axes and passing through the points $(2,3)$ and $(6,1)$.
(x) Centre $(0,0)$, major axis horizontal, the points $(3,1),(4,0)$ lie on the graph.
2. Find the centre, foci, eccentricity, vertices and directrices of the ellipse, whose equation is given:
(i) $x^{2}+4 y^{2}=16$
(ii) $9 x^{2}+y^{2}=18$
(iii) $25 x^{2}+9 y^{2}=225$
(iv) $\frac{(2 x-1)^{2}}{4}+\frac{(y+2)^{2}}{16}=1$
(v) $x^{2}+16 x+4 y^{2}-16 y+76=0$
(vi) $25 x^{2}+4 y^{2}-250 x-16 y+541=0$
3. Let $a$ be a positive number and $0<c<a$. Let $F(-c, 0)$ and $F^{\prime}(c, 0)$ be two given points. Prove that the locus of points $P(x, y)$ such that

$$
|P F|+\left|P F^{\prime}\right|=2 a, \text { is an ellipse. }
$$

4. Use problem 3 to find equation of the ellipse as locus of points $P(x, y)$ such that the sum of the distances from $P$ to the points $(0,0)$ and $(1,1)$ is 2 .
5. Prove that the lactusrectum of the ellipse.

$$
\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1 \text { is } \frac{2 b^{2}}{a}
$$

6. The major axis of an ellipse in standard form lies along the $x$-axis and has length $4 \sqrt{2}$. The distance between the foci equals the length of the minor axis. Write an equation of the ellipse.
7. An astroid has elliptic orbit with the sun at one focus. Its distance from the sun ranges from 17 million miles to 183 million miles. Write an equation of the orbit of the astroid.
8. An arch in the shape of a semi-ellipse is 90 m wide at the base and 30 m high at the centre. At what distance from the centre is the arch $20 \sqrt{2} \mathrm{~m}$ high?
9. The moon orbits the earth in an elliptic path with earth at one focus. The major and minor axes of the orbit are $768,806 \mathrm{~km}$ and $767,746 \mathrm{~km}$ respectively. Find the greatest and least distances (in Astronomy called the apogee and perigee respectively) of the moon from the earth.

### 6.6 HYPERBOLA AND ITS ELEMENTS

We have already stated that a conic section is a hyperbola if $e>1$. Let $e>1$ and $F$ be a fixed point and $L$ be a line not containing $F$. Also let $P(x, y)$ be a point in the plane and $|P M|$ be the perpendicular distance of $P$ from $L$.

The set of all points $P(x, y)$ such that

$$
\frac{|P F|}{|P M|}=e>1
$$

is called a hyperbola.
$F$ and $L$ are respectively focus and directrix of the hyperbola $e$ is the eccentricity.

### 6.6.1 Standard Equation of Hyperbola

Let $F(c, 0)$ be the focus with $c>0$ and $x=\frac{c}{c^{2}}$ be the directrix of the hyperbola. Also let $P(x, y)$ be a point on the hyperbola, then by definition

$$
\frac{|P F|}{|P M|}=e
$$

i.e. $(x-c)^{3}+y^{2}=e^{2}\left(x-\frac{c}{e^{2}}\right)^{2} \quad$ or $\quad x \frac{c}{e^{2}} \quad 2 c \neq \quad c \neq \quad y \frac{c}{e^{2}} \quad e^{2} x \frac{c}{e^{2}} \quad 2 c \neq \quad \frac{e^{2}}{a^{2}}$
or $\quad x^{2}\left(e^{2}-1\right)-y^{2}=c^{2}\left(1-\frac{1}{e^{2}}\right)=\frac{c^{2}}{e^{2}}\left(e^{2}-1\right)$
Let us set $a=\frac{c}{e}$, so that (2) becomes
$x^{2}\left(e^{2}-1\right)-y^{2}-a^{2}\left(e^{2}-1\right)=0-\quad$ or $\quad \frac{x^{2}}{a^{2}} \quad \frac{y^{2}}{a^{2}\left(e^{2}-1\right)} \quad 1$
or $\quad \frac{x^{2}}{a^{2}}-\frac{y^{2}}{b^{2}}=1$
where $\quad b^{2}=a^{2}\left(e^{2}-1\right) \approx c^{2}-a^{2} \quad \because c=a e$
(3) is standard equation of the hyperbola.

It is clear that the curve is symmetric with respect to both the axes.
If we take the point $(-c, 0)$ as focus
and the line $x=\frac{-c}{e^{2}}$ as directrix, then it is easy to see that the set of all points $P(x, y)$ such that

$$
|P F|=e|P M|
$$

is hyperbola with (3) as its equation.
Thus a hyperbola has two foci and two directrices.

If the foci lie on the $y$-axis, then roles of $x$ and $y$ are interchanged in (3) and the equation of the hyperbola becomes

$$
\frac{y^{2}}{a^{2}}-\frac{x^{2}}{b^{2}}=1
$$

Definition: The hyperbola

$$
\frac{x^{2}}{a^{2}}-\frac{y^{2}}{b^{2}}=1
$$

meets the $x$-axis at points with $y=0$ and $x= \pm a$. The points $A(-a, 0$ and $A \nmid a, 0)$ are called vertices of the hyperbola. The line segament $A A^{\prime}=2 a$ is called the transverse (or focal) axis of the hyperbola (3). The equation (3) does not meet the $y$-axis in real points. However the line segment joining the points $B(0,-b)$ and $B^{\prime}(0, b)$ is called the conjugate axis of the hyperbola. The midpoint $(0,0)$ of $A A^{\prime}$ is called the centre of the hyperbola.

In case of hyperbola (3), we have

$$
b^{2}=a^{2}\left(e^{2}-1\right)=c^{2}-a^{2} \text {. The eccentricity } e=\frac{c}{a}>1
$$

so that, unlike the ellipse, we may have $b>a$ or $b<a$ or $b=a$
(ii) The point ( $a$ sec $\theta, b$ tan $\theta$ ) lies on the hyperbola $\frac{x^{2}}{a^{2}}-\frac{y^{2}}{b^{2}}=1$ for all real values of $\theta$. The equations $x=a \sec \theta, y=b \tan \theta$ are called parametric equations of the hyperbola.
(iii) Since $y= \pm \frac{b}{a} \sqrt{x^{2}-a^{2}}$, when $|x|$, so that $x^{2} \quad a^{2} \quad \Rightarrow$, we have

$$
y:=\frac{b}{a} \cdot x \quad \text { i.e. } \quad \frac{x^{2}}{a^{2}}-\frac{y^{2}}{b^{2}}=0
$$

The lines (2) do not meet the curve but distance of any point on the curve from any of the two lines approaches zero. Such lines are called asymptotes of a curve. Joint equation of the asymptotes of (3) is obtained by writing 0 instead of 1 on the right hand side of the standard form (3). Asymptotes are very helpful in graphing a hyperbola.

The ellipse and hyperbola are called central conics because each has a centre of symmetry.

### 6.6.2 Graph of the hyperbola

$$
\frac{x^{2}}{a^{2}}-\frac{y^{2}}{b^{2}}=1
$$

The curve is symmetric with respect to both the axes. We rewrite (1) as

$$
\begin{aligned}
& \frac{y^{2}}{b^{2}}=\frac{x^{2}}{a^{2}} \quad 1 \quad \text { or } \quad-y^{2} \quad \frac{b^{2}}{a^{2}}\left(x^{2} \quad a^{2}\right) \cdot \\
& \text { or } \pm y=\frac{b}{a} \sqrt{x^{2} \quad a^{2}}
\end{aligned}
$$

If $|x|<a$, then $y$ is imaginary so that no portion of the curve lies between $-\alpha<x<\alpha$. For $x \geq a, y=\frac{b}{a} \sqrt{x^{2}-a^{2}} \leq \frac{b}{a} x$ so that points on the curve lie below the corresponding points on the line $y=\frac{b}{a} x$ in first quadrant.

$$
y=\frac{b}{a} \sqrt{x^{2}-a^{2}} \quad \frac{-b}{a} x \text { if } \geq x \quad a
$$

and in this case the points on the curve lie above the line $y=\frac{-b}{a} x$ in fourth quadrant. If $x \leq \alpha$, then by similar arguments, $y=\frac{b}{a} \sqrt{x^{2}-a^{2}}$ lies below the corresponding point on $y=\frac{-b}{a} x$ in second quadrant. If $y=\frac{-b}{a} \sqrt{x^{2}-a^{2}}$, then points on the curve lie above the correspondent point on $y=\frac{b}{a} x$ in third quadrant. Thus there are two branches of the curve. Moreover, from (2) we see that as $|x| \rightarrow \infty,|y| \rightarrow \infty$ so that the two branches extend to infinity

## Summary of Standard Hyperbolas

|  Equation | $\frac{x^{2}}{a^{2}}-\frac{y^{2}}{b^{2}}=1$ | $\frac{y^{2}}{a^{2}}-\frac{z^{2}}{b^{2}}=1$  |
| --- | --- | --- |
|  Foci | $(\pm c, 0)$ | $(0, \pm c)$  |
|  Directrices | $x= \pm \frac{c}{e^{2}}$ | $y= \pm \frac{c}{e^{2}}$  |
|  Transverse axis | $y=0$ | $x=0$  |
|  Vertices | $( \pm \alpha, 0)$ | $(0, \pm \alpha)$  |
|  Eccentricity | $e=\frac{c}{a}>1$ | $e=\frac{c}{a}>1$  |

version: 1.1

|  Centre | $(0,0)$ | $(0,0)$  |
| --- | --- | --- |
|  Graph |  |   |
|  |   |   |

Example 1. Find an equation of the hyperbola whose foci are ( $\pm 4,0$ ) and vertices ( $\pm 2,0$ ). Sketch its graph.

Solution: The centre of the hyperbola is the origin and the transverse axis is along the $x$-axis. Here $c=4$ and $\alpha=2$ so that $b^{2}=c^{2}-\alpha^{2}=16-4=12$. Therefore, the equation is $\frac{x^{2}}{4}-\frac{y^{2}}{12}=1$. The graph of the curve is as shown. Example 2. Discuss and sketch the graph of the equation $25 x^{2}-16 y^{2}=400$ Solution: The given equation is

$$
\frac{x^{2}}{16}-\frac{y^{2}}{25}=1-\text { or }=\frac{x^{2}}{4^{2}} \cdot \frac{y^{2}}{5^{2}}=1
$$

which is an equation of the hyperbola with transverse axis along the $x$-axis.

$$
\begin{aligned}
& \text { Here } \quad \alpha=4, b=5 \\
& \text { From } \quad b^{2}=c^{2}-a^{2}, \quad \text { we have } \\
& \quad c^{2}=34 \text { or } c= \pm \sqrt{34} \\
& \text { Foci of the hyperbola are: }( \pm \sqrt{34}, 0) \\
& \text { Vertices: }( \pm 4,0) \\
& \text { Ends of the conjugate axes are the points }(0, \pm 5)
\end{aligned}
$$

Eccentricity: $e=\frac{c}{a}=\frac{\sqrt{34}}{4}$
The curve is below the lines $\varepsilon=\frac{b}{a} x \quad x \quad \frac{5}{4} x$
which are its asymptotes. The sketch of the curve is as shown.
Example 3. Find the eccentricity, the coordinates of the vertices and foci of the asymptotes of the hyperbola

$$
\frac{\varepsilon^{2}}{16} \cdot \frac{x^{2}}{49}=1
$$

Also sketch its graph.
Solution. The transverse axis of (1) lies along the $y$-axis. Coordinates of the vertices are $(0, \pm 4)$.

$$
\begin{aligned}
& \text { Here } a=4, b=7 \text { so that from } \varepsilon^{2}=a^{2}+b^{2} \text {, we get } \\
& \varepsilon^{2}=16+49 \text { or } c=\sqrt{65} \\
& \text { Foci are: }(0, \pm \sqrt{65}) \\
& \text { Ends of the conjugate axis are }( \pm 7,0) \\
& \text { Eccentricity }=\frac{c}{a}=\frac{\sqrt{65}}{4} \\
& x= \pm 7, y= \pm 4
\end{aligned}
$$

The graph of the curve is as shown.
Example 4. Discuss and sketch the graph of the equation

$$
4 x^{2}-8 x-y^{2}-2 y-1=0
$$

Solution: Completing the squares in $x$ and $y$ in the given equation, we have

$$
\begin{aligned}
& 4\left(x^{2}-2 x+1\right)-\left(y^{2}+2 y+1\right)=4 \\
\text { or } & 4(x-1)^{2}-(y+1)^{2}=4 \\
\text { or } & \frac{(x-1)^{2}}{1^{2}}-\frac{(y+1)^{2}}{2^{2}}=1
\end{aligned}
$$

$$
\text { version: } 1.1
$$

We write $x-1=X, y+1=Y$ in (2), to have

$$
\frac{X^{2}}{1^{2}}-\frac{Y^{2}}{2^{2}}=1
$$

so that it is a hyperbola with centre at $X=0, Y=0$ i.e., the centre of (1) is $(1,-1)$. The transverse axis of (3) is $Y=0$ i.e., $y+1=0$ is the transverse axis of (1). Vertices of (3) are: $X= \pm 1, y=0$
i.e. $x-1= \pm 1, y+1=0 \quad$ or $\quad(0,-1)$ and $(2,-1)$

Here $a=1$ and $b=2$ so that, we have $c=\sqrt{a^{2}+b^{2}}=\sqrt{5}$
Eccentricity $e=\frac{c}{a}=\sqrt{5}$
Foci of (3) are: $\pm X=\sqrt{5}, Y \quad 0$
i.e., $\quad x=1 \sqrt{5} \quad$ and $\quad \varepsilon \quad 1$
i.e., $\quad(1+\sqrt{5},-1)$ and $(1-\sqrt{5},-1)$ are foci of (1).
Equations of the directrices of (3) are: $X= \pm \frac{c}{e^{2}}= \pm \frac{\sqrt{5}}{5}= \pm \frac{1}{\sqrt{5}}$

$$
\text { or } \quad x-1= \pm \frac{1}{\sqrt{5}} \quad \text { or } \quad x=1+\frac{1}{\sqrt{5}} \quad \text { and } \quad x=1-\frac{1}{\sqrt{5}}
$$

The sketch of the curve is as shown.

## EXERCISE 6.6

1. Find an equation of the hyperbola with the given data. Sketch the graph of each.
(i) Centre $(0,0)$, focus $(6,0)$, vertex $(4,0)$
(ii) Foci $( \pm 5,0)$, vertex $(3,0)$
(iii) Foci $(2 \pm 5 \sqrt{2},-7)$, length of the transverse axis 10 .
(iv) Foci $(0, \pm 6), e=2$.
(v) Foci $(0, \pm 9)$, directrices $y= \pm 4$

(vi) Centre $(2,2)$, horizontal transverse axis of length 6 and eccentricity $e=2$
(vii) Vertices $(2, \pm 3),(0,5)$ lies on the curve.
(viii) Foci $(5,-2),(5,4)$ and one vertex $(5,3)$
2. Find the centre, foci, eccentricity, vertices and equations of directrices of each of the following:
(i) $x^{2}-y^{2}=9$
(ii) $\frac{x^{2}}{4}-\frac{y^{2}}{9}=1$
(iii) $\frac{y^{2}}{16}-\frac{x^{2}}{9}=1$
(iv) $\frac{y^{2}}{4}-x^{2}=1$
(v) $\frac{(x-1)^{2}}{2}-\frac{(y-1)^{2}}{9}=1$
(vi) $\frac{(y+2)^{2}}{9}-\frac{(x-2)^{2}}{16}=1$
(vii) $9 x^{2}-12 x-y^{2}-2 y+2=0$
(viii) $4 y^{2}+12 y-x^{2}+4 x+1=0$
(ix) $x^{2}-y^{2}+8 x-2 y-10=0$
(x) $9 x^{2}-y^{2}-36 x-6 y+18=0$
3. Let $0<a<c$ and $F^{\prime}(-c, 0), F(c, 0)$ be two fixed points. Show that the set of points $P(x, y)$ such that
$|P F|-\left|P K^{\prime}\right|=2 a$, is the hyperbola $\frac{x^{2}}{a^{2}}-\frac{y^{2}}{c^{2}-a^{2}}=1$
( $F, F^{\prime}$ are foci of the hyperbola)
4. Using Problem 3, find an equation of the hyperbola with foci $(-5,-5)$ and $(5,5)$, vertices $(-3 \sqrt{2},-3 \sqrt{2})$ and $(3 \sqrt{2}, 3 \sqrt{2})$.
5. For any point on a hyperbola the difference of its distances from the points $(2,2)$ and $(10,2)$ is 6 . Find an equation of the hyperbola.
6. Two listening posts hear the sound of an enemy gun. The difference in time is one second. If the listening posts are 1400 feet apart, write an equation of the hyperbola passing through the position of the enemy gum. (Sound travels at $1080 \mathrm{ft} / \mathrm{sec}$ ).

### 6.7 TANGENTS AND NORMALS

We have already seen in the geometrical interpretation of the derivative of a curve $y=f(x)$ or $f(x, y)=0$ that $\frac{d y}{d x}$ represents the slope of the tangent line to the curve at the point $(x, y)$. In order to find an equation of the tangent to a given
conic at some point on the conic, we shall first find the slope of the tangent at the given point by calculating $\frac{d y}{d x}$ from the equation of the conic at that point and then using the point - slope form of a line, it will be quite simple to write an equation of the tangent. Since the normal to a curve at a point on the curve is perpendicular to the tangent through the point of tangency, its equation can be easily written.

Example 1. Find equations of the tangent and normal to
(i) $y^{2}=4 a x$
(ii) $\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1$
(iii) $\frac{x^{2}}{a^{2}}-\frac{y^{2}}{b^{2}}=1$
at the point $\left(x_{1}, y_{1}\right)$.
Solution: (i). Differentiating (1) w.r.t. $\quad x$, we get

$$
\begin{aligned}
& 2 y \frac{d y}{d x}=4 a \quad \text { or } \quad \frac{d y}{d x} \quad 2 a \\
& \left.\frac{d y}{d x}\right|_{\left(x_{1}, y_{1}\right)}=\frac{2 a}{y_{1}} \text { Slope of the tangent at }\left(x_{1}, y_{1}\right)
\end{aligned}
$$

Equation of the tangent to (1) at $\left(x_{1}, y_{1}\right)$ is

$$
y-y_{1}=\frac{2 a}{y_{1}}\left(x-x_{1}\right) \text { or } y y_{1}-y_{1}^{2}=2 a x-2 a x_{1} \text { or } y y_{1}-2 a x=y_{1}^{2}-2 a x_{1}
$$

Adding $-2 a x$, to both sides of the above equation, we obtain

$$
y y_{1}=2 a\left(x+x_{1}\right)=y_{1}^{2}-4 a x_{1}
$$

Since $\left(x_{1}, y_{1}\right)$ lies on $y^{2}=4 a x_{1}$ so $y_{1}^{2}-4 a x_{1}=0$
Thus equation of the required tangent is

$$
y y_{1}=2 a\left(x+x_{1}\right)
$$

Slope of the normal $=\frac{-y_{1}}{2 a} \quad$ (negative reciprocal of slope of the tangent)

Equation of the normal is

$$
y-y_{1}=\frac{-y_{1}}{2 a}\left(x-x_{1}\right)
$$

(ii) $\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1$

Differentiating the above equation, w.r.t. $x$, we have

$$
\frac{2 x}{a^{2}}+\frac{2 y}{b^{2}} \frac{d y}{d x}=0-\text { or } \frac{d y}{d x}=\frac{b^{2} x}{a^{2} y}
$$

or $\left.\frac{d y}{d x}\right|_{\left(x_{1}, y_{1}\right)}=\frac{-b^{2} x_{1}}{a^{2} y_{1}}$
Equation of the tangent to (2), at $\left(x_{1}, y_{1}\right)$ is

$$
y-y_{1}=\frac{-b^{2} x_{1}}{a^{2} y_{1}}\left(x-x_{1}\right)
$$

or $\quad \frac{y y_{1}}{b^{2}}, \frac{y_{1}^{2}}{b^{2}}=\frac{-x x_{1}}{a^{2}}+\frac{x_{1}^{2}}{a^{2}} \quad$ or $\quad \frac{x x_{1}}{a^{2}}+\frac{y y_{1}}{b^{2}}=\frac{x^{2}}{a^{2}}+\frac{y_{1}^{2}}{a^{2}}$
Since $\left(x_{1}, y_{1}\right)$ lie on (2) so, $\frac{x_{1}^{2}}{a^{2}}+\frac{y_{1}^{2}}{b^{2}}=1$
Hence an equation of the tangent to (2) at $\left(x_{1}, y_{1}\right)$ is $\frac{x x_{1}}{a^{2}}+\frac{y y_{1}}{b^{2}}=1$
Slope of the normal at $\left(x_{1}, y_{1}\right)$ is $\frac{a^{2} y_{1}}{b^{2} x_{1}}$.
Equation of the normal at $\left(x_{1}, y_{1}\right)$ is

$$
y-y_{1}=\frac{a^{2} y_{1}}{b^{2} x_{1}}\left(x-x_{1}\right)
$$

or $\quad b^{2} x_{1} y-b^{2} x_{1} y_{1}=a^{2} y_{1} x-a^{2} x_{1} y_{1} \quad$ or $\quad a^{2} y_{1} x-b^{2} x_{1} y=x_{1} y_{1}\left(a^{2}-b^{2}\right)$
Dividing both sides of the above equation by $x_{1} y_{1}$, we get
$\frac{a^{2} x}{x_{1}} \quad \frac{b^{2} y}{y_{1}}=a^{2}-b^{2}$, as an equation of the normal.
(iii) Proceeding as in (ii), it is easy to see that equations of the tangent and normal to (3) at $\left(x_{1}, y_{1}\right)$ are

$$
\frac{x x_{1}}{a^{2}}+\frac{y y_{1}}{b^{2}}=1 \quad \text { and } \quad \frac{a^{2} x}{x_{1}}+\frac{b^{2} y}{y_{1}}=a^{2}+b^{2}, \text { respectively. }
$$

## Remarks

An equation of the tangent at the point $\left(x_{1}, y_{1}\right)$ of any conic can be written by making replacements in the equation of the conic as under:

$$
\begin{array}{lll}
\text { Replace } & x^{2} & \text { by } & x x_{1} \\
& y^{2} & \text { by } & y y_{1} \\
& x & \text { by } & \frac{1}{2}\left(x+x_{1}\right) \\
& y & \text { by } & \frac{1}{2}\left(y+y_{1}\right)
\end{array}
$$

Example 1. Write equations of the tangent and normal to the parabola $x^{2}=16 y$ at the point whose abscissa is 8 .

Solution: Since $x=8$ lies on the parabola, substituting this value of $x$ into the given equation, we find

$$
64=16 y \quad \text { or } \quad y=4
$$

Thus we have to find equations of tangent and normal at $(8,4)$.
Slope of the tangent to the parabola at $(8,4)$ is 1 . An equation of the tangent the parabola at $(8,4)$ is

$$
y-4=x-8
$$

or $\quad x-y-4=0$
Slope of the normal at $(8,4)$ is -1 . Therefore, equation of the normal at the given point is

$$
y-4=-(x-8)
$$

or $\quad x+y-12=0$
Example 2. Write equations of the tangent and normal to the conic $\frac{x^{2}}{8}+\frac{y^{2}}{9}=1$ at the point $\left(\frac{8}{3}, 1\right)$.

Solution: The given equation is

$$
9 x^{2}+8 y^{2}-72=0
$$

Differentiating (1) w.r.t. $x$, we have
This is slope of the tangent to (1) at $\left(\frac{8}{3}, 1\right)$.
Equation of the tangent at this point is
$y-1=-3 \cdot\left(x-\frac{8}{3}\right)=-3 x+8$ or $3 x+y-9=0$.
The normal at $\left(\frac{8}{3}, 1\right)$ has the slope $\frac{1}{3}$.
Equation of the normal is
$y-1=\frac{1}{3}\left(x-\frac{8}{3}\right)$ or $3 y-3=x-\frac{8}{3}$ or $3 x-9 y+1=0$

Theorem: To show that a straight line cuts a conic, in general, in two points and to find the condition that the line be a tangent to the conic.

Let a line $y=m x+c$ cut the conics
(i) $y=4 a x$
(ii) $\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1$
(iii) $\frac{x^{2}}{a^{2}}-\frac{y^{2}}{b^{2}}=1$

We shall discuss each case separately.
(i) The points of intersection of

$$
y=m x+c
$$

and $\quad y^{2}=4 a x$
are obtained by solving (1) and (2) simultaneously for $x$ and $y$. Inserting the value of $y$ from (1) into (2), we get

$$
(m x+c)^{2}=4 a x
$$

or $\quad m^{2} x^{2}+(2 m c-4 a) x+c^{2}=0$
which being a quadratic in $x$ gives two values of $x$. These values are the $x$ coordinates of the common points of (1) and (2). Setting these values in (1), we obtain the corresponding
ordinates of the points of intersection. Thus the line (1) cuts the parabola (2) in two points. In order that (1) is a tangent to (2), the points of intersection of a line and the parabola must be conicident. In this case, the roots of (3) should be real and equal.
This means that the discriminant of (3) is zero. Thus

$$
4(m c-2 a)^{2}-4 m^{2} c^{2}=0 \quad \text { i.e., } \quad-4 m c a+4 a^{2}=0
$$

or $\quad c=\frac{a}{m}$, is. the required condition for (1) to be a tangent to (2). Hence

$$
y=m x+\frac{a}{m} \text {, is a tangent to } y^{2}=4 a x \text { for all nonzero values of } m \text {. }
$$

(ii) To determine the points of intersection of

$$
y=m x+c
$$

and

$$
\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1
$$

we solve (1) and (2) simultaneously. Putting the value of $y$ from (1) into (2), we have

$$
\frac{x^{2}}{a^{2}}+\frac{(m x+c)^{2}}{b^{2}}=1
$$

or

$$
\left(a^{2} m^{2}+b^{2}\right) x^{2}+2 m c a^{2} x+a^{2} c^{2}-a^{2} b^{2}=0
$$

which is a quardratic in $x$ and it gives the abscissas of the two points where (1) and (2) intersect. The corresponding values of $y$ are obtained by setting the values of $x$ obtained from (3) into (1). Thus (1) and (2) intersect in two points. Now (1) is a tangent to (2) if the point of intersection is a single point.
This requires (3) to have equal roots. Hence (1) is a tangent to (2) if

$$
\left(2 m c a^{2}\right)^{2}-4\left(a^{2} m^{2}+b^{2}\right)\left(a^{2} c^{2}-a^{2} b^{2}\right)=0
$$

i.e., $\quad m^{2} c^{2} a^{2}-\left(a^{2} m^{2}+b^{2}\right)\left(c^{2}-b^{2}\right)=0$
or $\quad m^{2} c^{2} a^{2}-a^{2} m^{2} c^{2}+a^{2} m^{2} b^{2}-b^{2} c^{2}+b^{4}=0$
or $\quad c^{2}=a^{2} m^{2}+b^{2}$
or $\quad c=\sqrt{a^{2} m^{2} b^{2}}$.
Putting the value of $c$ into (1), we have

$$
\frac{x=m x \sqrt{a^{2} m^{2} b^{2}}}{x}
$$

which are tangents to (2) for all non-zero values of $m$.

(iii) We replace $b^{2}$ by $-b^{2}$ in (ii) and the line $y=m x+c$ is a tangent to

$$
\frac{x^{2}}{a^{2}}-\frac{y^{2}}{b^{2}}=1 \quad \text { if } \quad c=\sqrt{a^{2} m^{2}-b^{2}}
$$

Thus $y=m x \sqrt{a^{2} m^{2}-b^{2}}$ are tangents to the hyperbola: $\frac{x^{2}}{a^{2}}-\frac{y^{2}}{b^{2}}=1$ for all non-zero values of $m$.

Example 4. Find an equation of the tangent to the parabola $y^{2}=-6 x$ which is parallel to the line $2 x+y+1=0$. Also find the point of tangency.

Solution: Slope of the required tangent is $\mathrm{m}=-2$
In the parabola $y^{2}=-6 x$

$$
a=\frac{-6}{4}=\frac{-3}{2}
$$

Equation of the tangent is

$$
y=m x+\frac{a}{m}=-2 x+\frac{3}{4}
$$

i.e., $8 x+4 y-3=0$

Inserting the value of $y$ from (2) viz $y=\frac{-8 x+3}{4}$ into (1), we have

$$
\left(\frac{-8 x+3}{4}\right)^{2}=-6 x
$$

or $\quad 64 x^{2}-48 x+9=-96 x \quad$ or $\quad 64 x^{2}+48 x+9=0$
or $\quad(8 x+3)^{2}=0 \quad$ i.e., $\quad x=\frac{-3}{8}$
Putting this value of $x$ into (2), we get

$$
y=\frac{-8\left(\frac{-3}{8}\right)+3}{4}-\frac{3}{2}
$$

The point of tangency is $\left(\frac{-3}{8}, \frac{3}{2}\right)$.

## Example 5. Find equations of the tangents to the ellipse

$$
\frac{x^{2}}{128}+\frac{y^{2}}{18}=1
$$

which are parallel to the line $3 x+8 y+1=0$. Also find the points of contact.
Solution: The slope of the required tangents is $\frac{-3}{8}$. Equations of the tangents are

$$
y=\frac{-3}{8} x \pm \sqrt{\left(128\left(\frac{-3}{8}\right)^{2}+18=\frac{-3}{8} x \pm 6\right.}
$$

Thus the two tangents are

$$
3 x+8 y+48=0
$$

and $3 x+8 y-48=0$
We solve (1) and (3) simultaneously to find the point of contact. Inserting the value of $y$ from (3) into (1), we get

$$
\begin{aligned}
& \frac{x^{2}}{128}+\frac{\left(\frac{-3}{8} x+6\right)^{2}}{18}=1 \quad \text { or } \quad \frac{x^{2}}{128}+\frac{9}{64} \frac{x^{2}+36}{18}-\frac{9}{2} x \\
& \text { or } \quad \frac{x^{2}}{128}+\frac{x^{2}}{128}+2-\frac{x}{4}=1-\text { or }=\frac{x^{2}}{64}-\frac{x}{4} \quad 1 \quad 0 \\
& \text { or } \quad\left(\frac{x}{8}-1\right)^{2}=0 \quad \text { i.e., } x=8 \quad \text { and so } \quad \frac{-3}{8} x \quad 6 \quad 3
\end{aligned}
$$

Thus $(8,3)$ is the point of tangency of $(3)$.
It can be seen in a similar manner that point of contact of (2) is $(-8,-3)$.
Example 6. Show that the product of the distances from the foci to any tangent to the hyperbola

$$
\frac{x^{2}}{a^{2}}-\frac{y^{2}}{b^{2}}=1
$$

is constant.

Solution: The line

$$
y=m x \sqrt{a^{2} m^{2}-b^{2}}
$$

is a tangent to (1).
Foci of (1) are $F(-c, 0)$ and $F^{\prime}(c, 0)$.
Distance of $F(-c, 0)$ from (2) is

$$
d_{1}=\frac{\left|-c m+\sqrt{a^{2} m^{2}-b^{2}}\right|}{\sqrt{1+m^{2}}}
$$

Distance of $F^{\prime}(c, 0)$ from (2) is

$$
\begin{aligned}
& d_{2}=\frac{\left|c m+\sqrt{a^{2} m^{2}-b^{2}}\right|}{\sqrt{1+m^{2}}} \\
& d_{1} \times d_{2}=\frac{\left|a^{2} m^{2}-b^{2}-c^{2} m^{2}\right|}{1+m^{2}}=\frac{\left|a^{2} m^{2}-c^{2}+a^{2}-c^{2} m^{2}\right|}{1+m^{2}} \text { as } b^{2}=c^{2}-a^{2} \\
& \left|a^{2}-c^{2}\right| \\
& =c^{2}-a^{2} \quad \text { since } \quad c>a
\end{aligned}
$$

which is constant.

## Intersection of Two Coincs

Suppose we are given two conics

$$
\frac{x^{2}}{a^{2}} \cdot \frac{y^{2}}{b^{2}}=1
$$

and $y^{2}=4 a x$
To find the points common to both (1) and (2), we need to solve (1) and (2) simultaneously. It is known from algebra, that the simultaneous solution set of two equations of the second degree consists of four points. Thus two conics will always intersect in four points. These points may be all real and distinct, two real and two imaginary or all imaginary. Two or more points may also coincide. Two conics are said to touch each other if they intersect in two or more coincident points.

Example 7. Find the points of intersection of the ellipse

$$
\frac{x^{2}}{43 / 3} \cdot \frac{y^{2}}{43 / 4}=1-(1)=\text { and the hyperbola } \quad \frac{x^{2}}{7} \cdot \frac{y^{2}}{14} 1
$$

Also sketch the graph of the two conics.
Solution: The two equations may be written as

$$
3 x^{2}+4 y^{2}=43 \quad \text { (1) and } 2 x^{2}-y^{2}=14
$$

Multiplying (2) by 4 and adding the result to (1), we get

$$
11 x^{2}=99 \quad \text { or } \quad x= \pm 3
$$

Setting $x=3$ in to (2), we have $18-y^{2}=14$ or $y= \pm 2$
Thus $(3,2)$ and $(3,-2)$ are two points of intersection of the two conics
Putting $x=-3$ into (2), we get

$$
y= \pm 2
$$

Therefore $(-3,2)$ and $(-3,-2)$ are also points of intersection of (1) and (2). The four points of intersection are as shown in the figure.
Example 8. Find the points of intersection of the conics

$$
y=1+x^{2}
$$

and $\quad y=1+4 x-x^{2}$
Also draw the graph of the conics.
Solution. From (1), we have

$$
x=\sqrt{y-1}
$$

Inserting these values of $x$ into (2), we get

$$
y=1 \pm 4 \sqrt{y-1}-(y-1)
$$

or

$$
2 y-2= \pm 4 \sqrt{y-1} \quad \text { or } \quad(y-1)^{2}=4(y-1)
$$

or

$$
(y-1)(y-1-4)=0
$$

Therefore, $\quad y=1,5$
When $\quad y=1, x=0$
When $\quad y=5, x= \pm 2$

But $(-2,5)$ does not satisfy (2).
Thus $(0,1)$ and $(2,5)$ are the points of intersections of (1) and (2). $y=1+x^{2}$ is a parabola with vertex at $(0,1)$ and opening upward, $y=1+4 x-x^{2}$ may be written as $y-5=-(x-2)^{2}$ which is a parabola with vertex. $(2,5)$ and opening downward
Example 9. Find equations of the common tangents to the two conics

$$
\frac{x^{2}}{16}+\frac{y^{2}}{25}=1 \quad+\quad \text { and } \quad \frac{x^{2}}{25}-\frac{y^{2}}{9}=1
$$

Solution. The tangents with slope $m$, to the two conics are respectively given by

$$
y=\pi n x \sqrt{16 m^{2} 25} \quad \text { and } \quad y=\pi n x \sqrt{25 m^{2} 9}
$$

For a tangent to be common, we must have

$$
16 m^{2}+25=25 m^{2}+9
$$

or $\quad 9 m=16 \quad$ or $\quad m= \pm \frac{4}{3}$.
Using these values of $m$, equations of the four common tangents are:

$$
\pi=\frac{4}{3} x \sqrt{481}
$$

## EXERCISE 6.7

1. Find equations of the tangent and normal to each of the following at the indicated point:
(i) $y^{2}=4 a x$
(ii) $\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1$
(iii) $\frac{x^{2}}{a^{2}}-\frac{y^{2}}{b^{2}}=1$
at $\quad(a \cos \theta, b \sin \theta)$
at $\quad(a \sec \theta, b \tan \theta)$
2. Write equation of the tangent to the given conic at the indicated point
(i) $3 x^{2}=-16 y$ at the points whose ordinate is -3 .
(ii) $3 x^{2}-7 y^{2}=20$ at the points where $y=-1$.
(iii) $3 x^{2}-7 y^{2}+2 x-y-48=0$ at the point where $x=4$.
3. Find equations of the tangents to each of the following through the given point:
(i) $x^{2}+y^{2}=25$
(ii) $y^{2}=12 x$
(iii) $x^{2}-2 y^{2}=2$
through $(7,-1)$
through $(1,4)$
through $(1,-2)$
4. Find equations of the normals to the parabola $y^{2}=8 x$ which are parallel to the line $2 x+3 y=10$.
5. Find equations of the tangents to the ellipse $\frac{x^{2}}{4}+y^{2}=1$ which are parallel to the line $2 x-4 y+5=0$.
6. Find equations of the tangents to the conic $9 x^{2}-4 y^{2}=36$ parallel to $5 x-2 y+7=0$.
7. Find equations of the common tangents to the given conics
(i) $x^{2}=80 y$
(ii) $y^{2}=16 x$
and $x^{2}=2 y$
and $\quad \frac{x^{2}}{3}-\frac{y^{2}}{3}=1$
and $\quad x^{2}-y^{2}=1$
and $\quad 3 y^{2}-2 x^{2}=7$
and $\quad 9 x^{2}+y^{2}=124$
and $\quad x^{2}+y^{2}+y+8=0$

### 6.8 TRANSLATION AND ROTATION OF AXES

## Translation of Axes

In order to facilitate the investigation of properties of a curve with a given equation, it is sometimes necessary to shift the origin $O(0,0)$ to some other point $O^{\prime}(h, k)$. The axes $O^{\prime} X, O^{\prime} Y$ drawn through $O^{\prime}$ remain parallel to the original axes $O x$ and $O y$. The process is called translation of axes.

We have already obtained in Chapter 4 formulas showing relationships between the two sets of coordinates of a point referred to the two sets of coordinate axes.

Recall that if a point $P$ has coordinates $(x$, $y)$ referred to the $x y$-system and has coordinates $(X, Y)$ referred to the translated axes $O^{\prime} X, O^{\prime} Y$ through $O^{\prime}(h, k)$, then
$$
\left.\begin{array}{l}
x=X+h \\
y=T+k
\end{array}\right\}
$$

These are called equations of transformation.
From (1), we have

$$
\left.\begin{array}{l}
X=x-h \\
Y=y-k
\end{array}\right\}
$$

(1) and (2) will be used to transform an equation in one system into the other system. The axes $O x$ and $O y$ are referred to as the original (or old) axes and $O^{\prime} X, O^{\prime} Y$ are called the translated axes (or new axes).

Example 1: Transform the equation $x^{2}+6 x-8 y+17=0$
referred to $O^{\prime}(-3,1)$ as origin, axes remaining parallel to the old axes.

Solution. Equations of transformation are

$$
\begin{aligned}
& x=X-3 \\
& y=Y+1
\end{aligned}
$$

Substituting these values of $x, y$ into (1), we have

$$
(X-3)^{2}+6(X-3)-8(Y+1)+17=0
$$

or $\quad X^{2}-6 X+9+6 X-18-8 Y-8+17=0$
or $\quad X^{2}-8 Y=0$ is the required transformed equation.

Example 2: By transforming the equation

$$
x^{2}+4 y^{2}-4 x+8 y+4=0
$$

referred to a new origin and axes remaining parallel to the original axes, the first degree terms are removed. Find the coordinates of the new origin and the transformed equation.

Solution. Let the coordinates of the new origin be $(h, k)$. Equations of transformation are

$$
\begin{aligned}
& x=X+h \quad, \quad y=Y+k \\
& \text { Substituting these values of } x, y \text { into (1), we get } \\
& (X+h)^{2}+4(Y+k)^{2}-4(X+h)+8(Y+k)+4=0 \\
& \text { or } \quad X^{2}+4 Y^{2}+X(2 h-4)+Y(8 k+8)+h^{2}+4 k^{2}-4 h+8 k+4=0
\end{aligned}
$$

$(h, k)$ is to be so chosen that first degree terms are removed from the transformed equation.

Therefore, $2 h-4=0$ and $8 k+8=0$ giving $h=2$ and $k=-1$. New origin is $O^{\prime}(2,-1)$. Putting $h=2, k=-1$ into (2), the transformed equation is $X^{2}+4 Y^{2}-4=0$.

## Rotation of Axes

To find equations for a rotation of axes about the origin through an angle $\theta(0<\theta<90^{\circ})$. (origin remaining unaltered).

Let the axes be rotated about the origin through an angle $\theta$. The new axes $O X, O Y$ are as shown in the figure.

Let $P$ be any point in the plane with coordinates $P(x, y)$ referred to the $x y$-system and $P(X, Y)$ referred to the $X Y$-system. In either system the distance $r$ between $P$ and $O$ is the same. Draw $P M \perp O x$ and $P Q \perp O X$. Let $\alpha$ be the inclination of $O P$ with $O X$. From the figure, we have
$$
\begin{aligned}
& X=O Q=r \cos \alpha, Y=Q P=r \sin \alpha \\
& \text { and } \quad x=r \cos (\theta+\alpha), y=r \sin (\theta+\alpha) \\
& \text { or } \quad\left.\begin{array}{l}
x=r \cos \theta \cos \alpha \quad r \sin \theta \sin \alpha \\
y=r \sin \theta \cos \alpha+r \cos \theta \sin \alpha
\end{array}\right\}
\end{aligned}
$$

Substituting the values of $r \cos \alpha, r \sin \alpha$ from (1) into (2), we get

$$
\left.\begin{array}{l}
x=X \cos \theta-Y \sin \theta \\
y=X \sin \theta+y \cos \theta
\end{array}\right]
$$

as the required equations of transformation for a rotation of axes through an angle $\theta$.
Example 3: Find an equation of $5 x^{2}-6 x y+5 y^{2}-8=0$ with respect to new axes obtained by rotation of axes about the origin through an angle of $135^{\circ}$.

Solution. Here $\theta=135$. Equations of transformation are

$$
\begin{aligned}
& x=X \cos 135^{\circ}-Y \sin 135^{\circ}=\frac{-X}{\sqrt{2}}-\frac{Y}{\sqrt{2}}=\frac{-1}{\sqrt{2}}(X+Y) \\
& x=X \sin 135^{\circ}+Y \cos 135^{\circ}=\frac{X}{\sqrt{2}}-\frac{Y}{\sqrt{2}}=\frac{1}{\sqrt{2}}(X-Y)
\end{aligned}
$$

Substituting these expressions for $x, y$ into the given equation, we have

$$
\begin{aligned}
& 5\left(-\frac{X+Y}{\sqrt{2}}\right)^{2}-6\left(-\frac{X+Y}{\sqrt{2}}-\frac{X-Y}{\sqrt{2}}\right)+5\left(\frac{X-Y}{\sqrt{2}}\right)^{2}-8=0 \\
\text { or } \quad & \frac{5}{2}\left(X^{2}+2 X Y+Y^{2}\right)+3\left(X^{2}-Y^{2}\right)+\frac{5}{2}\left(X^{2}-2 X Y+Y^{2}\right)-8=0 \\
\text { or } & 8 x^{2}+2 y^{2}-8=0 \quad \text { or } \quad 4 x^{2}+y^{2}=4
\end{aligned}
$$

is the required transformed equation.

Example 4: Find the angle through which the axes be rotated about the origin so that the product term $X Y$ is removed from the transformed equation of $5 x^{2}+2 \sqrt{3} x y+7 x^{2}-16=0$. Also find the transformed equation.

Solution. Let the axes be rotated through an angle $\theta$. Equations of transformation are

$$
x=X \cos \theta-Y \sin \theta \quad ; \quad y=X \sin \theta+Y \cos \theta
$$

Substituting into the given equation, we get

$$
\begin{aligned}
& 5(X \cos \theta-Y \sin \theta)^{2}+2 \sqrt{3}(X \cos \theta-Y \sin \theta)(X \sin \theta+Y \cos \theta) \\
& +7(X \sin \theta+y \cos \theta)^{2}-16=0
\end{aligned}
$$

Since this equation is to be free from the product term $X Y$, the coefficient of $X Y$ is zero, i.e. $-10 \sin \theta \cos \theta+2 \sqrt{3}\left(\cos ^{2} \theta-\sin ^{2} \theta\right)+14 \sin \theta \cos \theta=0$

$$
\text { or } \quad 2 \sin 2 \theta+2 \sqrt{3} \cos 2 \theta=0
$$

$$
\text { or } \quad \tan 2 \theta=\frac{-2 \sqrt{3}}{2}=\tan 120^{\circ} \quad \text { or } \quad \theta=60^{\circ}
$$

Thus axes be rotated through an angle of $60^{\circ}$ so that $X Y$ term is removed from the transformed equation.

Setting $\theta=60^{\circ}$ into (1), the transformed equation is (after simplification)

$$
8 x^{2}+4 y^{2}-16=0 \quad \text { or } \quad 2 x^{2}+y^{2}-4=0
$$

## EXERCISE 6.8

1. Find an equation of each of the following with respect to new parallel axes obtained by shifting the origin to the indicated point:
(i) $x^{2}+16 y-16 \quad=0, \quad O^{\prime}(0,1)$
(ii) $4 x^{2}+y^{2}+16 x-10 y+37 \quad=0, \quad O^{\prime}(2,5)$
(iii) $9 x^{2}+4 x^{2}+18 x-16 y-11 \quad=0, \quad O^{\prime}(-1,2)$
(iv) $x^{2}-y^{2}+4 x+8 y-11 \quad=0, \quad O^{\prime}(-2,4)$
(v) $9 x^{2}-4 y^{2}+36 x+8 y-4 \quad=0, \quad O^{\prime}(2,1)$
2. Find coordinates of the new origin (axes remaining parallel) so that first degree terms are removed from the transformed equation of each of the following. Also find the transformed equation:
(i) $3 x^{2}-2 y^{2}+24 x+12 y+24=0$
(ii) $25 x^{2}+9 y^{2}+50 x-36 y-164=0$
(iii) $x^{2}-y^{2}-6 x+2 y+7=0$
3. In each of the following, find an equation referred to the new axes obtained by rotation of axes about the origin through the given angle:
(i) $x y=1, \quad \theta=45^{\circ}$
(ii) $7 x^{2}-8 x y+y^{2}-9=0, \quad \theta=\arctan 2$
(iii) $9 x^{2}+12 x y+4 y^{2}-x-y=0, \quad \theta=\arctan \frac{2}{3}$
(iv) $x^{2}-2 x y+y^{2}-2 \sqrt{2} x-2 \sqrt{2} y+2=0, \quad \theta=45^{\circ}$

4. Find measure of the angle through which the axes be rotated so that the product term $X Y$ is removed from the transformed equation. Also find the transformed equation:
(i) $2 x^{2}+6 x y+10 y^{2}-11=0$
(ii) $x y+4 x-3 y-10=0$
(iii) $5 x^{2}-6 x y+5 y^{2}-8=0$

### 6.9 THE GENERAL EQUATION OF SECOND DEGREE

Standard equations of conic sections, namely circle, parabola, ellipse and hyperbola have already been studied in the previous sections. Now we shall take up the general equation of second degree viz.

$$
A x^{2}+B y^{2}+G x+F y+C=0
$$

The nature of the curve represented by (1) can be determined by examining the coefficients $A, B$ in the above equation. The following cases arise:
(i) If $A=B \neq 0$, equation (1) may be written as

$$
\begin{aligned}
& A\left(x^{2}+y^{2}\right)+G x+F y+C=0 \text { or } \quad x^{2}+y^{2}+\frac{G}{A} x+\frac{F}{A} y+\frac{C}{A}=0 \\
& \text { which represents a circle with centre at }\left(-\frac{G}{2 A},-\frac{F}{2 A}\right) \text { and radius } \sqrt{\frac{G^{2}}{4 A^{2}}+\frac{F^{2}}{4 A}-\frac{C}{A}}
\end{aligned}
$$

(ii) If $\quad A \neq B$ and both are of the same sign, then we have $\left(A x^{2}+G x\right)+\left(B y^{2}+F y\right)+C=0$
or $\quad A\left(x^{2}+\frac{G}{A} x+\frac{G^{2}}{4 A^{2}}\right)+B\left(y^{2}+\frac{F}{B} y+\frac{F^{2}}{4 B^{2}}\right)=\frac{G^{2}}{4 A}+\frac{F^{2}}{4 B}-C$
or $\quad A\left(x+\frac{G}{2 A}\right)^{2}+B\left(y+\frac{F}{2 B}\right)^{2}=\frac{G^{2}}{4 A}+\frac{F^{2}}{4 B}-C$
If we write $X \Leftrightarrow x \quad \frac{G}{4 A}, Y \quad y \quad \frac{F}{2 B}$, then (2) can be written as
$A X^{2}+B Y^{2}=\frac{G^{2}}{4 A}+\frac{F^{2}}{4 B}-C=K$ (say) or $\frac{X^{2}}{(\sqrt{K / A})^{2}}-\frac{Y^{2}}{(\sqrt{K / B})^{2}}, \quad 1$
which is standard equation of an ellipse in $X Y$-coordinate system.
(iii) If $A \neq B$ and both have opposite signs (say $A$ is positive and $B$ is negative),
we can write (1) as
or $\quad A\left(x^{2}+\frac{G}{A} x+\frac{G^{2}}{4 A^{2}}\right)-B^{\prime}\left(y^{2}-\frac{F}{B^{\prime}} y+\frac{F^{2}}{4 B^{\prime 2}}\right)=\frac{G^{2}}{4 A}-\frac{F^{2}}{4 B^{\prime}}-C=M$ (say)
or $\quad A\left(x+\frac{G}{2 A}\right)^{2}-B^{\prime}\left(y-\frac{F}{2 B^{\prime}}\right)^{2}=M$
or $\quad A X^{2}-B^{\prime} Y^{2}=M$, where $X=x-\frac{G}{2 A}, \quad Y \quad y-\frac{F}{2 B^{\prime}}$
or $\quad \frac{X^{2}}{(\sqrt{M / A})^{2}}-\frac{Y^{2}}{\left(\sqrt{M / B^{2}}\right)^{2}}=1$
and this is standard equation of a hyperbola in $X Y$-coordinates system.
(iv) If $A=0$ or $B=0$ (both cannot be zero since in that case the equation (1) reduces to a linear equation). Assume $A \neq 0$ and $B=0$.
The equation (1) becomes $A x^{2}+G x+F y+C=0$
or $\quad A\left(x^{2}+\frac{G}{A} x+\frac{G^{2}}{4 A^{2}}\right)=-F y-C+\frac{G^{2}}{4 A}$
or $\quad A\left(x+\frac{G}{2 A}\right)^{2}=-F\left(y+\frac{C}{F}-\frac{G^{2}}{4 A F}\right)$
or $\quad A X^{2}=-F Y$, where $X=x+\frac{G}{2 A}, \quad Y=y+\frac{C}{F}-\frac{G^{2}}{4 A F}$
which is standard equation of a parabola in $X Y$-coordinates system.
We summarize these results as under:
Let an equation of second degree be of the form $A x^{2}+B y^{2}+G x+F y+C=0$. It represents:
(i) a circle if $A=B \neq 0$
(ii) an ellipse if $A \neq B$ and both are of the same sign
(iii) a hyperbola if $A \neq B$ and both are of opposite signs
(iv) a parabola if either $A=0$ or $B=0$.

### 6.9.1 Classification of Conics by the Discriminant

The most general equation of the second degree

$$
\alpha x^{2}+2 h x y+b y^{2}+2 g x+2 f y+c=0
$$

represents a conic. The quantity $h^{2}-a b$ is called the discriminant of (1). Nature of the conic can be determined by the discriminant as follows. (1) represents:
(i) an ellipse or a circle if $h^{2}-a b<0$
(ii) a parabola if $h^{2}-a b=0$
(iii) a hyperbola if $h^{2}-a b>0$

The equation (1) can be transformed to the form

$$
A X^{2}+B Y^{2}+2 G X+2 F y+C=0
$$

if the axes are rotated about the origin through an angle $\theta,\left(0<\theta<90^{\circ}\right)$ where $\theta$ is given by

$$
\tan 2 \theta=\frac{2 h}{a-b}
$$

If $a=b$ or $a=0=b$, then the axes are to be rotated through an angle of $45^{\circ}$.
Equations of transformation (as already found) are

$$
\left.\begin{array}{l}
x=X \cos \theta-Y \sin \theta \\
y=X \sin \theta+Y \cos \theta
\end{array}\right\}
$$

Substitution of these values of $x, y$ into (1) will result in an equation of the form (2) in which product term $X Y$ will be missing. Nature of the conic (2) has already been discussed in the last article.

Solving equations (3) for $X, Y$ we find

$$
\left.\begin{array}{l}
X=x \cos \theta+y \sin \theta \\
Y=\pi \sin \theta \quad y \cos \theta
\end{array}\right\}
$$

These equations will be useful in numerical problems.
Note: Under certain conditions equation (1) may not represent any conic, in such a case we say (1) represents a degenerate conic.

One such degenerate conic is a pair of straight lines represented by (1) if

$$
\left.\begin{array}{lll}
a & h & g \\
h & b & f \\
g & f & c
\end{array}\right\}=0
$$

The proofs of the above observations are beyond our scope and are omitted.

## Example 1: $\quad$ Discuss the conic $7 x^{2}-6 \sqrt{3} x y+13 y^{2}-16=0$ and find its elements.

Solution. In order to remove the term involving $x y$, the angle through which axes be rotated is given by

$$
\tan 2 \theta=\frac{-6 \sqrt{3}}{7-13}=\sqrt{3} \quad{ }^{\circ} \text { or } \quad \theta \approx 30
$$

Equations of transformation are

$$
\begin{aligned}
& x=X \cos 30^{\circ}-Y \sin 30^{\circ}=\frac{\sqrt{3} X-Y}{2} \\
& y=X \sin 30^{\circ}+Y \cos 30^{\circ}=\frac{X+\sqrt{3} Y}{2}
\end{aligned}
$$

Substituting these expressions in to the equation (1), we get

$$
\sqrt[3]{\left(\frac{\sqrt{3} X-Y}{2}\right)^{2}-6 \sqrt{3}\left(\frac{\sqrt{3} X-Y}{2}\right)\left(\frac{X+\sqrt{3} Y}{2}\right)}+13\left(\frac{X+\sqrt{3} Y}{2}\right)^{2}=16
$$

which simplifies to

$$
4 X^{2}+16 Y^{2}=16+\quad \text { or } \quad \frac{X^{2}}{4} \quad \frac{Y^{2}}{1} \quad 1
$$

This is an ellipse.
Solving equations (2) for $X$ and $Y$, (or as already found in (4) of 7.7.1, we have

$$
X=\frac{\sqrt{3} x+y}{2}, \quad Y \quad \frac{-x+\sqrt{3} y}{2}
$$

Centre of the ellipse (3) is $X=0, Y=0$
i.e., $\quad \sqrt{3} x+y=0-\quad+$ and $=\quad x \quad \sqrt{3} y \quad 0$
giving $\quad x=0, y=0$. Thus centre of (1) is $(0,0)$
Length of the major axis $=4$, length of minor axis $=2$
Vertices of (3) are: $\quad X=\pm 2, Y=0$

$$
\text { i.e., } \quad \frac{\sqrt{3} x+y}{2}=2 \quad \text { and } \quad \frac{-x+\sqrt{3} y}{2} \quad 0
$$

Solving these equations for $x, y$, we have

$$
(\sqrt{3}, 1),(-\sqrt{3},-1), \text { as vertices of }(1)
$$

Ends of the minor axis are $X=0$ and $Y=1$ i.e., $\frac{\sqrt{3} x+y}{2} \quad 0$ and $\frac{-x+\sqrt{3} y}{2}= \pm 1$. Solving these equations, we get $\left(\frac{1}{2}, \frac{-\sqrt{3}}{2}\right)$ and $\left(-\frac{1}{2}, \frac{\sqrt{3}}{2}\right)$
as ends of the minor axis of (1).
Equation of the major axis: $Y=0$,
i.e.,

$$
-x+\sqrt{3} y=0
$$

Equation of the minor axis: $X=0$,
i.e., $\sqrt{3} x+y=0$

Example 2: Analyze the conic $x y=4$ and write its elements.
Solution: Equation of the conic is

$$
x y-4=0
$$

Here $a=0=b$, so we rotate the axes through an angle of $45^{\circ}$. Equations of transformation are

$$
\begin{aligned}
& x=X \cos 45^{\circ}-Y \sin 45^{\circ}=\frac{X-Y}{\sqrt{2}} \\
& y=X \sin 45^{\circ}-Y \cos 45^{\circ}=\frac{X+Y}{\sqrt{2}}
\end{aligned}
$$

Substituting into (1), we have

$$
\left(\frac{X-Y}{\sqrt{2}}\right)\left(\frac{X+Y}{\sqrt{2}}\right)-4=0
$$

or $X^{2}-Y^{2}=8$

$$
\frac{X^{2}}{8} \cdot \frac{Y^{2}}{8}=1
$$

which is a hyperbola.
Solving equations (2) for $X, Y$, we have

$$
X=\frac{x+y}{\sqrt{2}}, \quad Y \quad \frac{-x+y}{\sqrt{2}}
$$

Centre of the hyperbola (3) is

$$
X=0, Y=0
$$

i.e., $\frac{x+y}{\sqrt{2}}=0, \quad$ and $\frac{-x+y}{\sqrt{2}} \quad 0$
or $\quad x=0, \quad y=0$ is the centre of (1)
Equation of the focal axis: $\quad Y=0$ i.e. $\quad y=x$.
Equation of the conjugate axis: $\quad X=0$ i.e. $\quad y=-x$.
Eccentricity $=\sqrt{2}$
Foci of (3): $X=2 \sqrt{2} \cdot \sqrt{2} \quad \pm Y \quad 0$
or $\quad x+y= \pm 4 \sqrt{2}$
and $-x+y=0$
Solving the above equations for $x, y$, we have the foci of (1) as $(2 \sqrt{2}, 2 \sqrt{2})$ and $(-2 \sqrt{2},-2 \sqrt{2})$ Vertices of (3): $X=2 \sqrt{2}, \quad Y \quad 0$
i.e., $\frac{x+y}{\sqrt{2}}= \pm 2 \sqrt{2}$ and $-x+y \neq 0$

Solving these equations, we have the foci of (1) as

$$
(2 \sqrt{2}, 2 \sqrt{2}) \text { and }(-2 \sqrt{2},-2 \sqrt{2})
$$

Vertices of (3): $X=2 \sqrt{2}, \quad Y \quad 0$

$$
\frac{x+y}{\sqrt{2}}= \pm 2 \sqrt{2} \quad \text { and } \quad-x+y=0
$$

Solving these equations, we have
$(2,2),(-2,-2)$ as vertices of (1).

Asymptotes of the hyperbola (3) are given by $X^{2}-Y^{2}=0$
or $\quad X-Y=0 \quad$ and $\quad X+Y=0$
i.e., $\frac{x+y}{\sqrt{2}}-\frac{-x+y}{\sqrt{2}}=0$ and $\frac{x+y}{\sqrt{2}}-\frac{-x+y}{\sqrt{2}}=0$
i.e., $x=0$ and $y=0$ are equations of the asymptotes of (1).

Example 3: By a rotation of axes, eliminate the $x y$-term in the equation

$$
9 x^{2}+12 x y+4 y^{2}+2 x-3 y=0
$$

Identify the conic and find its elements.

Solution: Here $a=9, b=4,2 h=12$. The angle $\theta$ through which axes be rotated to given by

$$
\begin{aligned}
& \tan 2 \theta=\frac{12}{9-4}=\frac{12}{5} \\
& \text { or } \quad \frac{2 \tan \theta}{1-\tan ^{2} \theta}=\frac{12}{5} \\
& \text { or } 5 \tan \theta=6-6 \tan ^{2} \theta \\
& \text { or } 6 \tan ^{2} \theta+5 \tan \theta-6=0 \\
& \tan \theta=\frac{-5 \pm \sqrt{25+144}}{12}=\frac{-5 \pm 13}{12} \quad \frac{2}{3}, \frac{-3}{2}
\end{aligned}
$$

Since $\theta$ lies in the first quadrant, $\tan \theta=-\frac{2}{3}$ is not admissible.

$$
\tan \theta=\frac{2}{3} \Rightarrow \quad \sin \theta \quad \frac{2}{\sqrt{13}}, \quad \cos \theta \quad \frac{3}{\sqrt{13}}
$$

Equations of transformation become

$$
\begin{aligned}
& x=X \cos \theta-Y \sin \theta=\frac{2}{\sqrt{13}} X-\frac{2}{\sqrt{13}} Y \\
& y=X \sin \theta+Y \cos \theta=\frac{2}{\sqrt{13}} X+\frac{3}{\sqrt{13}} Y
\end{aligned}
$$

Substituting these expressions for $x$ and $y$ into (1), we get

$$
\begin{aligned}
& \frac{9}{(\sqrt{13})^{2}}(3 X-2 Y)^{2}+\frac{12}{13}(3 X-2 Y)(3 X+3 Y)+\frac{4}{13}(2 X+3 Y)^{2} \\
& +\frac{2}{\sqrt{13}}(3 X-2 Y)-\frac{3}{\sqrt{13}}(2 X+3 Y)=0 \\
& \text { or } \quad \frac{9}{13}\left(9 X^{2}-12 X Y+9 Y^{2}\right)+\frac{12}{13}\left(6 X^{2}+5 X Y-6 Y^{2}\right) \\
& +\frac{4}{13}\left(4 X^{2}+12 X Y-9 Y^{2}\right)-\sqrt{13} Y=0 \\
& \text { or } \quad\left(\frac{81}{13}+\frac{72}{13}+\frac{16}{13}\right) X^{2}+\left(-\frac{108}{13}+\frac{60}{13}+\frac{48}{13}\right) X Y \\
& +\left(\frac{36}{13}, \frac{72}{13}+\frac{36}{13}\right) Y^{2}-\sqrt{13} Y=0
\end{aligned}
$$

or $13 X^{2}-\sqrt{13} Y=0 \quad$ or $\quad X^{2} \quad \frac{1}{\sqrt{13}} Y$
which is a parabola.
Solving equation (2) for $X, Y$, we have $X=\frac{3 x+2 y}{\sqrt{13}}, Y=\frac{-2 x+3 y}{\sqrt{13}}$
Elements of the parabola are:
Focus: $X=0, \quad Y=\frac{1}{4 \sqrt{13}}$
i.e., $\frac{3 x+2 y}{\sqrt{13}}=\theta \quad$ and $\quad \frac{-2 x+3 y}{\sqrt{13}} \quad \frac{1}{4 \sqrt{13}}$

Solving these equations, we have $x=\frac{1}{26}, y \quad \frac{3}{52}$ i.e., Focus $\left(\frac{1}{26}, \frac{3}{52}\right)$
Vertex: $\quad X=0, \quad Y=0 \quad$ i.e., $\quad 3 x+2 y=0$ and $-2 x+3 y=0$
i.e., $\quad x=0, \quad y=0 \quad$ i.e., $\quad(0,0)$

Axis: $\quad X=0 \quad$ i.e., $\quad 3 x+2 y=0$

$$
x \text {-intercept }=-\frac{2}{9}, \quad y \text {-intercept }=\frac{3}{4}
$$

Example 4: $\quad$ Show that $2 x^{2}-x y+5 x-2 y+2=0$ represents a pair of lines. Also find an equation of each line.

Solution: Here $a=2, b=0, h=\frac{1}{2}, g \quad \frac{5}{2}, f \quad 1, c=2$.

$$
\begin{gathered}
\left|\begin{array}{ccc}
a & h & g \\
h & b & f \\
g & f & c
\end{array}\right|=\left|\begin{array}{ccc}
2 & -\frac{1}{2} & \frac{5}{2} \\
\frac{1}{2} & 0 & 1 \\
\frac{5}{2} & -1 & 2 \\
\end{array}\right| \\
=\frac{1}{2}\left(-1+\frac{5}{2}\right)+1\left(-2+\frac{5}{4}\right)
\end{gathered}
$$

$$
-\frac{3}{4}-\frac{3}{4}=0
$$

The given equation represents a degenerate conic which is a pair of lines. The given equation is

$$
\begin{aligned}
& 2 x^{2}+x(5-y)+(-2 y+2)=0 \\
\text { or } \quad & x=\frac{y-5 \pm \sqrt{(y-5)^{2}-h(-2 y+2)}}{4} \\
& =\frac{y-5 \pm \sqrt{y^{2}-10 y+25+16 y-16}}{4} \\
& =\frac{y-5 \pm(y+3)}{4} \\
& =\frac{2 y-2}{4}, \quad-2
\end{aligned}
$$

Equations of the lines are $2 x-y+1=0$ and $x+2=0$.

## Tangent

Find an equation of the tangent to the conic

$$
a x^{2}+2 h x y+b y^{2}+2 g x+2 f y+c=0
$$

at the point $\left(x_{1}, y_{1}\right)$
Differentiating (1) w.r.t. $\quad x$, we have

$$
2 a x+2 h y+2 h x \frac{d y}{d x}+2 b y \frac{d y}{d x}+2 g+2 f \frac{d y}{d x}=0
$$

or $\quad \frac{d y}{d x}=-\frac{a x+h y+g}{h x+b y+f}$
or $\left.\frac{d y}{d x}\right|_{x_{1}, y_{1}}=-\frac{a x_{1}+h y_{1}+g}{h x_{1}+b y_{1}+f}$
Equation of the tangent at $\left(x_{1}, y_{1}\right)$ is

$$
y-y_{1}=-\frac{a x_{1}+h y_{1}+g}{h x_{1}+b y_{1}+f}\left(x_{1}, y_{1}\right)
$$

or $\quad(x-x_{1})\left(a x_{1}+h y_{1}+g\right)+(y-y_{1})\left(h x_{1}+b y_{1}+f\right)=0$
or $\quad a x x_{1}+h x y_{1}+g x++h x_{1} y+b y_{1} y+f y$

$$
=a x_{1}^{2}+2 h x_{1} y_{1}+g x_{1}+b y_{1}^{2}+f y_{1}
$$

Adding $g x_{1}+f y_{1}+c$ to both sides of the above equation and regrouping the terms, we have

$$
\begin{aligned}
& a x x_{1}+h\left(x y_{1}+y x_{1}\right)+b y y_{1}+g\left(x+x_{1}\right)+f\left(y+y_{1}\right)+c \\
& =a x_{1}^{2}+2 h x_{1} y_{1}+b y_{1}^{2}+2 g x_{1}+2 f y_{1}+c \\
& =0
\end{aligned}
$$

since the point $\left(x_{1}, y_{1}\right)$ lies on (1).
Hence an equation of the tangent to (1) at $\left(x_{1}, y_{1}\right)$ is

$$
a x x_{1}+h\left(x y_{1}+y x_{1}\right)+b y y_{1}+g\left(x+x_{1}\right)+f\left(y+y_{1}\right)+c=0
$$

Note: An equation of the tangent to the general equation of the second degree at the point $\left(x_{1}, y_{1}\right)$ may be obtained by replacing

$$
\begin{aligned}
& x^{2} \text { by } x x_{1} \\
& y^{2} \text { by } y y_{1} \\
& 2 x y \text { by } x y_{1}+y x_{1} \\
& 2 x \text { by } x+x_{1} \\
& 2 y \text { by } y+y_{1}
\end{aligned}
$$

in the equation of the conic
Example 5: Find an equation of the tangent to the conic $x^{2}-x y+y^{2}-2=0$ at the point whose ordinate is $\sqrt{2}$.

Solution: Putting $y=\sqrt{2}$ into the given equation, we have

$$
\begin{aligned}
& x^{2}-\sqrt{2} x=0 \\
& x(x-\sqrt{2})=0 \quad x=0, \sqrt{2}
\end{aligned}
$$

The two points on the conic are $(0, \sqrt{2})$ and $(\sqrt{2}, \sqrt{2})$.
Tangent at $(0, \sqrt{2})$ is

$$
0 . x-\frac{1}{2}(x . \sqrt{2}+0 . y)+\sqrt{2} y-2=0
$$

or $\quad x-2 y+2 \sqrt{2}=0$
Tangent at $(\sqrt{2}, \sqrt{2})$ is

$$
\sqrt{2} x-\frac{1}{2}(\sqrt{2} x+\sqrt{2} y)+\sqrt{2} y-2=0
$$

or $\quad \sqrt{2} x+\sqrt{2} y-4=0$

# EXERCISE 6.9

1. By a rotation of axes, eliminate the $x y$-term in each of the following equations. Identify the conic and find its elements:
(i) $4 x^{2}-4 x y+y^{2}-6=0$
(ii) $x^{2}-2 x y+y^{2}-8 x-8 y=0$
(iii) $x^{2}+2 x y+y^{2}+2 \sqrt{2}-2 \sqrt{2} y+2=0$
(iv) $x^{2}+x y+y^{2}-4=0$
(v) $7 x^{2}-6 \sqrt{3} x y+13 y^{2}-16=0$
(vi) $4 x^{2}-4 x y+7 y^{2}+12 x+6 y-9=0$
(vii) $x y-4 x-2 y=0$
(viii) $x^{2}+4 x y-2 y^{2}-6=0$
(ix) $x^{2}-4 x y-2 y^{2}+10 x+4 y=0$
2. Show that
(i) $10 x y+8 x-15 y-12=0 \quad$ and
(ii) $6 x^{2}+x y-y^{2}-21 x-8 y+9=0$
each represents a pair of straight lines and find an equation of each line.
3. Find an equation of the tangent to each of the given conics at the indicated point.
(i) $3 x^{2}-7 y^{2}+2 x-y-48=0$
at $(4,1)$
(ii) $x^{2}+5 x y-4 y^{2}+4=0$
at $\quad y=-1$
(iii) $x^{2}+4 x y-3 y^{2}-5 x-9 y+6=0$
at $\quad x=3$.

# CHAPTER

## Vectors

## 7.1 INTRODUCTION

In physics, mathematics and engineering, we encounter with two important quantities, known as **"Scalars and Vectors"**.

A **scalar quantity**, or simply a **scalar**, is one that possesses only magnitude. It can be specified by a number along with unit. In Physics, the quantities like mass, time, density, temperature, length, volume, speed and work are examples of scalars.

A **vector quantity**, or simply a **vector**, is one that possesses both magnitude and direction. In Physics, the quantities like displacement, velocity, acceleration, weight, force, momentum, electric and magnetic fields are examples of vectors.

In this section, we introduce vectors and their fundamental operations we begin with a geometric interpretation of vector in the plane and in space.

### 7.1.1 Geometric Interpretation of Vector

Geometrically, a vector is represented by a directed line segment $$A B$$ with $$A$$ its initial point and $$B$$ its terminal point. It is often found convenient to denote a vector by an arrow and is written either as $$A B$$ or as a boldface symbol like $$v$$ or in underlined form $$\underline{v}$$.

- (i) The magnitude or length or norm of a vector $$A B$$ or $$\underline{v}$$ is its absolute value and is written as $$A B$$ or simply $$A B$$ or $$\mid \underline{v}$$.
- (ii) A unit vector is defined as a vector whose magnitude is unity. Unit vector of vector $$\underline{v}$$ is written as $$\underline{v}$$ (read as $$\underline{v}$$ hat) and is defined by $$\underline{v} = \frac{\underline{v}}{\mid \underline{v}}$$.

- (iii) If terminal point $$B$$ of a vector $$A B$$ coincides with its initial point $$A$$, then magnitude $$A B = 0$$ and $$A B = 0$$, which is called zero or null vector.
- (iv) Two vectors are said to be negative of each other if they have same magnitude but opposite direction.

If $$A B = \underline{v}, \quad \text{then} \quad B A = -AB = -\underline{v}$$

and $$B A = -AB$$

### 7.1.2 Multiplication of Vector by a Scalar

We use the word scalar to mean a real number. Multiplication of a vector $$\underline{v}$$ by a scalar $$k$$ is a vector whose magnitude is $$k$$ times that of $$\underline{v}$$. It is denoted by $$k \underline{v}$$.

- (i) If $$k$$ is $$\rightarrow$$ve, then $$\underline{v}$$ and $$k \underline{v}$$ are in the same direction.
- (ii) If $$k$$ is $$\rightarrow$$ve, then $$\underline{v}$$ and $$k \underline{v}$$ are in the opposite direction.

#### (a) Equal Vectors

Two vectors $$A B$$ and $$\underline{v}$$ are said to be equal, if they have the same magnitude and same direction i.e., $$A B = \overline{C D}$$

#### (b) Parallel Vectors

Two vectors are parallel if and only if they are non-zero scalar multiple of each other, (see figure).

### 7.1.3 Addition and Subtraction of Two Vectors

Addition of two vectors is explained by the following two laws:

#### (i) Triangle Law of Addition

If two vectors *u* and *v* are represented by the two sides *AB* and *BC* of a triangle such that the terminal point of *u* coincide with the initial point of *v*, then the third side *AC* of the triangle gives vector sum *u* + *v*, that is

$$
\overrightarrow{AB} + \overrightarrow{BC} = \overrightarrow{AC} \quad \Rightarrow \quad \underline{u} + \underline{v} = \overrightarrow{AC}
$$

### **(ii) Parallelogram Law of Addition**

If two vectors *u* and *v* are represented by two adjacent sides *AB* and *AC* of a parallelogram as shown in the figure, then diagonal *AD* gives the sum or resultant of $\overrightarrow{AB}$ and $\overrightarrow{AC}$, that is

$$
\overrightarrow{AD} = \overrightarrow{AB} + \overrightarrow{AC} = \underline{u} + \underline{v}
$$

### **Note:** This law was used by Aristotle to describe the combined action of two forces.

### **(b) Subtraction of two vectors**

The difference of two vectors $\overrightarrow{AB}$ and $\overrightarrow{AC}$ is defined by

$$
\overrightarrow{AB} - \overrightarrow{AC} = \overrightarrow{AB} + (- \overrightarrow{AC})
$$

$$
\underline{u} - \underline{v} = \underline{u} + (- \underline{v})
$$

In figure, this difference is interpreted as the main diagonal of the parallelogram with sides $\overrightarrow{AB}$ and $-\overrightarrow{AC}$. We can also interpret the same vector difference as the third side of a triangle with sides $\overrightarrow{AB}$ and $\overrightarrow{AC}$. In this second interpretation, the vector difference $\overrightarrow{AB} - \overrightarrow{AC} = \overrightarrow{CB}$ points the terminal point of the vector from which we are subtracting the second vector.

### **7.1.4 Position Vector**

The vector, whose initial point is the origin *O* and whose terminal point is *P*, is called the position vector of the point *P* and is written as $\overrightarrow{OP}$.

The position vectors of the points *A* and *B* relative to the origin *O* are defined by $\overrightarrow{OA} = \underline{o}$ and $\overrightarrow{OB} = \underline{b}$ respectively. In the figure, by triangle law of addition,

$$
\overrightarrow{OA} + \overrightarrow{AB} = \overrightarrow{OB}
$$

$$
\underline{o} + \overrightarrow{AB} = \underline{b}
$$

$$
\Rightarrow \overrightarrow{AB} = \underline{b} \quad \underline{o}
$$

### **7.1.5 Vectors in a Plane**

Let *R* be the set of real numbers. The Cartesian plane is defined to be the *R*<sup>2</sup> = {(*x*, *y*) : *x*, *y* ∈ *R*}.

An element (*x*, *y*) ∈ *R*<sup>2</sup> represents a point *P*(*x*, *y*) which is uniquely determined by its coordinate *x* and *y*. Given a vector *u* in the plane, there exists a unique point *P*(*x*, *y*) in the plane such that the vector $\overrightarrow{OP}$ is equal to *u* (see figure). So we can use rectangular coordinates (*x*, *y*) for *P* to associate a unique ordered pair [*x*, *y*] to vector *u*.

We define addition and scalar multiplication in *R*<sup>2</sup> by:

- **(i) Addition:** For any two vectors $\underline{u} = [x, y]$ and $\underline{v} = [x', y']$, we have
  $$
  \underline{u} + \underline{v} = [x, y] + [x', y'] = [x + x', y + y']
  $$

- **(ii) Scalar Multiplication:** For $\underline{u} = [x, y]$ and $\alpha \in R$, we have
  $$
  \alpha \underline{u} = \alpha [x, y] = [\alpha x, \alpha y]
  $$

**Definition:** The set of all ordered pairs [*x*, *y*] of real numbers, together with the rules of addition and scalar multiplication, is called the set of **vectors** in *R*<sup>2</sup>.

*version: 1.1*

For the vector **u** = [**x, y**], **x** and **y** are called the components of **u**.

**Note:** The vector [**x, y**] is an ordered pair of numbers, not a point (**x, y**) in the plane.

### (a) Negative of a Vector

In scalar multiplication (ii), if α = −1 and **u** = [**x, y**] then

$$
\alpha_{\mathbf{H}} = (-1) \{\mathbf{x}, \mathbf{y}\} = \{-x, -y\}
$$

which is denoted by **−u** and is called the **additive inverse** of **u** or **negative vector** of **u**.

### (b) Difference of two Vectors

We define **u** − **v** as **u** + (**−v**)
If **u** = [**x, y**] and **v** [**x', y']**, then
**u** − **v** = **u** + (**−v**)
  = [**x, y**] + [**−x' − y']** = [**x − x', y − y']**

### (c) Zero Vector

Clearly **u** + (**−u**) = [**x, y**] + [**−x, −y**] = [**x − x, y − y**] = [0, 0] = 0.
**0** = [0, 0] is called the **Zero (Null) vector**.

### (d) Equal Vectors

Two vectors **u** = [**x, y**] and **v** = [**x', y']** of **R²** are said to be equal if and only if they have the same components. That is,

$$
[x, y] = [x', y'] \text{ if and only if } x = x' \text{ and } y = y'
$$

and we write **u** = **v**.

### (e) Position Vector

For any point **P(x, y)** in **R²**, a vector **u** = [**x, y**] is represented by a directed line segment **OP**, whose initial point is at origin. Such vectors are called position vectors because they provide a unique correspondence between the points (positions) and vectors.

### (f) Magnitude of a Vector

For any vector **u** = [**x, y**] in **R²**, we define the **magnitude** or **norm** or **length** of the vector as of the point **P(x, y)** from the origin **O**.

$$
\begin{array}{ccccc}
\therefore & \text{Magnitude of } \overrightarrow{OP} = |\overrightarrow{OP}| & \text{in} & \sqrt{x^2 - y^2} \\
\end{array}
$$

### 7.1.6 Properties of Magnitude of a Vector

Let **v** be a vector in the plane or in space and let **c** be a real number, then

(i) **v** ≥ 0, and **v** = 0 if and only if **v** = 0

(ii) **cv** = |**c**| **v**|

**Proof:** (i) We write vector **v** in component form as **v** = [**x, y**], then

$$
|\mathbf{v}| = \sqrt{x^2 + y^2} \geq 0 \text{ for all } x \text{ and } y.
$$

Further **v** = √(x^2 + y^2) = 0 if and only if **x** = 0, **y** = 0

In this case **v** = [0, 0] = 0

(ii) **cv** = |**cx, cy**| = √(cx)^2 + (cy)^2 = √c^2 √(x^2 + y^2) = |c|**v**|

### 7.1.7 Another notation for representing vectors in plane

We introduce two special vectors,

$$
i = [1, 0], \quad j = [0, 1] \text{ in } R^2
$$

As magnitude of **i** = √(1^2 + 0^2) = 1

$$
\text{magnitude of } j = \sqrt{0^2 + 1^2} = 1
$$

So **i** and **j** are called unit vectors along **x**-axis, and along **y**-axis respectively. Using the definition of addition and scalar multiplication, the vector [**x, y**] can be written as

$$
\begin{aligned}
\mathbf{u} &= \begin{bmatrix} x, y \end{bmatrix} &= [x, 0] + [0, y] \\
&= x[1, 0] + y[0, 1] \\
&= xi + y
\end{aligned}
$$

Thus each vector [**x, y**] in **R²** can be uniquely represented by **xi + y**.

In terms of unit vector **i** and **j**, the sum **u + v** of two vectors

$$
\begin{aligned}
\mathbf{u} &= \begin{bmatrix} x, y \end{bmatrix} \text{ and } \mathbf{v} \begin{bmatrix} x', y' \end{bmatrix} \text{ is written as} \\
\mathbf{u} + \mathbf{v} &= \begin{bmatrix} x + x', y + y' \end{bmatrix} \\
&= (x + x')i + (y + y')j
\end{aligned}
$$

**version: 1.1**

7.1.8 A unit vector in the direction of another given vector.

A vector $\underline{u}$ is called a unit vector, if $|\underline{u}|=1$
Now we find a unit vector $u$ in the direction of any other given vector $\underline{v}$.
We can do by the use of property (ii) of magnitude of vector, as follows:
$\therefore \quad\left|\frac{1}{|\underline{v}|}\right|=\frac{1}{|\underline{v}||\underline{v}|}=1$
$\therefore \quad$ the vector $\underline{v}=\frac{1}{|\underline{v}|} \underline{v}$ is the required unit vector
It points in the same direction as $v$, because it is a positive scalar multiple of $\underline{v}$.

## Example 1:

For $\underline{v}=[1,-3]$ and $\underline{w}=[2,5]$
(i) $\underline{v}+\underline{w}=[1,-3]+[2,5]=[1+2,-3+5]=[3,2]$
(ii) $4 \underline{v}+2 \underline{w}=[4,-12]+[4,10]=[8,-2]$
(iii) $\underline{v}-\underline{w}=[1,-3]-[2,5]=[1-2,-3-5]=[-1,-8]$
(iv) $\underline{v}-\underline{v}=[1-1,-3+3]=[0,0]=0$
(v) $|\underline{v}|=\sqrt{(1)^{2}+(-3)^{2}}=\sqrt{1+9}=\sqrt{10}$

Example 2: Find the unit vector in the same direction as the vector $\underline{v}=[3,-4]$.
Solution: $\quad \underline{v}=[3,-4]=3(-4 \underline{j})$

$$
|\underline{v}|=\sqrt{3^{2}+(-4)^{2}}=\sqrt{25}=5
$$

Now $\quad \underline{u}=\frac{1}{|\underline{v}|} \underline{v}=\frac{1}{3}[3,-4] \quad$ ( $\underline{u}$ is unit vector in the direction of $v$ )

$$
=\left[\frac{3}{5}, \frac{-4}{5}\right]
$$

Verification: $|\underline{u}|=\sqrt{\left(\frac{3}{5}\right)^{2}+\left(\frac{-4}{5}\right)^{2}}=\sqrt{\frac{9}{25}+\frac{16}{25}}=1$

$$
\underline{v}=[3,-4]=3(-4 \underline{j})
$$

Example 3: Find a unit vector in the direction of the vector
(i) $\underline{v}=2 i+6 \underline{j}$
(ii) $\underline{v}=[-2,4]$

Solution: (i) $\underline{v}=2 i+6 \underline{j}$

$$
|\underline{v}|=\sqrt{(2)^{2}+(6)^{2}}=\sqrt{4+36}=\sqrt{40}
$$

$\therefore \quad$ A unit vector in the direction of $\underline{v}=\frac{\underline{v}}{|\underline{v}|} \quad \frac{2}{\sqrt{40}} i \quad \frac{6}{\sqrt{40}} \underline{j} \quad \frac{1}{\sqrt{10}} i \quad \frac{3}{\sqrt{10}} \underline{j}$
(ii) $\underline{v}=[-2,4]=-2 i+4 \underline{j}$

$$
|\underline{v}|=\sqrt{(-2)^{2}+(4)^{2}}=\sqrt{4+16}=\sqrt{20}
$$

$\therefore \quad$ A unit vector in the direction of $\underline{v}=\frac{\underline{v}}{|\underline{v}|} \quad \frac{-2}{\sqrt{20}} i \quad \frac{4}{\sqrt{20}} \underline{j} \quad \frac{-1}{\sqrt{5}} i \quad \frac{2}{\sqrt{5}} \underline{j}$

Example 4: If $A B C D$ is a parallelogram such that the points $A, B$ and $C$ are respectively $(-2,-3),(1,4)$ and $(0,-5)$. Find the coordinates of $D$.

Solution: Suppose the coordinates of $D$ are $(x, y)$
As $A B C D$ is a parallelogram

$$
\begin{aligned}
& \therefore \quad \overline{A B}=\overline{D C} \text { and } \overline{A B} \| \overline{D C} \\
& \Rightarrow \quad \overline{A B}=\overline{D C} \\
& \therefore \quad(1+2) i+(4+3) \underline{j}=(0-x) i+(-5-y) \underline{j} \\
& \Rightarrow \quad 3 i+7 \underline{j}=-x i+(-5-y) \underline{j}
\end{aligned}
$$

Equating horizontal and vertical components, we have

$$
-x=3 \Rightarrow x=-3
$$

and $\quad-5-y=7 \Rightarrow y=-12$
Hence coordinates of $D$ are $(-3,12)$.

### 7.1.9 The Ratio Formula

Let $A$ and $B$ be two points whose position vectors (p.v.) are $\underline{a}$ and $\underline{b}$ respectively. If a point $P$ divides $A B$ in the ratio $p: q$, then the position vector of $P$ is given by

$$
\underline{r}=\frac{q \underline{a}+p \underline{b}}{p+\underline{q}}
$$

Proof: Given $\underline{a}$ and $\underline{b}$ are position vectors of the points $A$ and $B$ respectively. Let $r$ be the position vector of the point $P$ which divides the line segment $A B$ in the ratio $p: q$. That is

$$
\begin{aligned}
& m \overline{A P}: m \overline{P B}=p: q \\
& \text { So } \quad \frac{m \overline{A P}}{m \overline{P B}}=\frac{p}{q} \\
& \Rightarrow \quad q(m \overline{A P})=p(m \overline{P B}) \\
& \text { Thus } \quad q(\overline{A P})=p(\overline{P B}) \\
& \Rightarrow \quad q(\underline{r}-\underline{a})=p(\underline{b}-\underline{r}) \\
& \Rightarrow \quad q \underline{r}-q \underline{a}=p \underline{b}-p \underline{r} \\
& \Rightarrow \quad p \underline{r}+q \underline{r}=q \underline{a}+p \underline{b} \\
& \Rightarrow \quad \underline{r}(p+q)=q \underline{a}+p \underline{b} \\
& \Rightarrow \quad \underline{r}=\frac{q \underline{a}+p \underline{b}}{q+p}
\end{aligned}
$$

Corollary: If $P$ is the mid point of $A B$, then $p: q \equiv 1: 1$

$$
\therefore \text { positive vector of } P=\underline{r} \quad \frac{\underline{a}+\underline{b}}{2}
$$

### 7.1.10 Vector Geometry

Let us now use the concepts of vectors discussed so far in proving Geometrical Theorems. A few examples are being solved here to illustrate the method.

Example 5: If $\underline{a}$ and $\underline{b}$ be the p.vs of $A$ and $B$ respectively w.r.t. origin $O$, and $C$ be a point on $\overline{A B}$ such that $\overline{O C}=\frac{a+b}{2}$, then show that $C$ is the mid-point of $A B$.

Solution: $\quad \overline{O A}=\underline{a}, \overline{O B}=\underline{b}$ and $\overline{O C}=\frac{1}{2}(\underline{a}+\underline{b})$
$$
\begin{aligned}
& \text { Now } \quad 2 \overline{O C}=\underline{a}+\underline{b} \\
& \Rightarrow \overline{O C}+\overline{O C}=\overline{O A}+\overline{O B} \\
& \Rightarrow \overline{O C}-\overline{O A}=\overline{O B}-\overline{O C} \\
& \Rightarrow \overline{O C}+\overline{A O}=\overline{O B}+\overline{C O} \\
& \Rightarrow \overline{A O}+\overline{O C}=\overline{C O}+\overline{O B} \\
& \therefore \quad \overline{A C}=\overline{C B} \\
& \text { Thus } m \overline{A C}=m \overline{C B}
\end{aligned}
$$

- $C$ is equidistant from $A$ and $B$, but $A, B, C$ are collinear. Hence $C$ is the mid point of $A B$.

Example 6: Use vectors, to prove that the diagonals of a parallelogram bisect each other.

Solution: Let the vertices of the parallelogram be $A, B, C$ and $D$ (see figure)
Since $\overline{A C}=\overline{A B}+\overline{A D}$, the vector from $A$ to the mid point of diagonal $\overline{A C}$ is

$$
\underline{v}=\frac{1}{2}(\overline{A B}+\overline{A D})
$$

Since $\overline{D B}=\overline{A B}-\overline{A D}$, the vector from $A$ to the mid point of diagonal $\overline{D B}$ is

$$
\begin{aligned}
& \underline{w}=\overline{A D}+\frac{1}{2}(\overline{A B}-\overline{A D}) \\
& =\overline{A D}+\frac{1}{2} \overline{A B}-\frac{1}{2} \overline{A D} \\
& =\frac{1}{2}(\overline{A B}+\overline{A D}) \\
& =\underline{\underline{v}}
\end{aligned}
$$

Since $\underline{v}=\underline{w}$, these mid points of the diagonals $\overline{A C}$ and $\overline{D B}$ are the same. Thus the diagonals of a parallelogram bisect each other.

## EXERCISE 7.1

1. Write the vector $\overrightarrow{P Q}$ in the form $x \xi+y \xi$.
(i) $P(2,3), \quad Q(6,-2)$
(ii) $P(0,5), \quad Q(-1,-6)$
2. Find the magnitude of the vector $u$ :
(i) $\mu=2 \xi-7 \xi$
(ii) $\mu=\xi+\xi$
(iii) $\mu=[3,-4]$
3. If $\mu=2 \xi-7 \xi, \quad \mu=\xi-6 \xi$ and $\mu=-6 \xi$. Find the following vectors:
(i) $\mu+\mu-\mu$
(ii) $2 \mu-3 \mu+4 \mu$
(iii) $\frac{1}{2} \mu+\frac{1}{2} \mu+\frac{1}{2} \mu$
4. Find the sum of the vectors $\overrightarrow{A B}$ and $\overrightarrow{C D}$, given the four points $A(1,-1), B(2,0)$, $C(-1,3)$ and $D(-2,2)$.
5. Find the vector from the point $A$ to the origin where $\overrightarrow{A B}=4 \xi-2 \xi$ and $B$ is the point $(-2,5)$.
6. Find a unit vector in the direction of the vector given below:
(i) $\mu=2 \xi-\xi$
(ii) $\mu=\frac{1}{2} \xi+\frac{\sqrt{3}}{2} \xi$
(iii) $\mu=\frac{\sqrt{3}}{2} \xi \frac{1}{2} \xi$
7. If $A, B$ and $C$ are respectively the points $(2,-4),(4,0)$ and $(1,6)$. Use vector method to find the coordinates of the point D if:
(i) $A B C D$ is a parallelogram
(ii) $A D B C$ is a parallelogram
8. If $B, C$ and $D$ are respectively $(4,1),(-2,3)$ and $(-8,0)$. Use vector method to find the coordinates of the point:
(i) $A$ if $A B C D$ is a parallelogram.
(ii) $E$ if $A E B D$ is a parallelogram.
9. If $O$ is the origin and $\overrightarrow{O P}=\overrightarrow{A B}$, find the point $P$ when $A$ and $B$ are $(-3,7)$ and $(1,0)$ respectively.
10. Use vectors, to show that $A B C D$ is a parallelogram, when the points $A, B, C$ and $D$ are respectively $(0,0),(a, 0),(b, c)$ and $(b-a, c)$.
11. If $\overrightarrow{A B}=\overrightarrow{C D}$, find the coordinates of the point $A$ when points $B, C, D$ are $(1,2),(-2,5)$, $(4,11)$ respectively.
12. Find the position vectors of the point of division of the line segments joining the following pair of points, in the given ratio:
(i) Point $C$ with position vector $2 \xi-3 \xi$ and point $D$ with position vector $3 \xi+2 \xi$ in the ratio $4: 3$
(ii) Point $E$ with position vector $5 \xi$ and point $F$ with position vector $4 \xi+\xi$ in ratio $2: 5$
13. Prove that the line segment joining the mid points of two sides of a triangle is parallel to the third side and half as long.
14. Prove that the line segments joining the mid points of the sides of a quadrilateral taken in order form a parallelogram.

### 7.2 INTRODUCTION OF VECTOR IN SPACE

In space, a rectangular coordinate system is constructed using three mutually orthogonal (perpendicular) axes, which have orgin as their common point of intersection. When sketching figures, we follow the convention that the positive $y$ $x$-axis points towards the reader, the positive $y$-axis to the right and the positive $z$-axis points upwards.

These axis are also labeled in accordance with the right hand rule. If fingers of the right hand, pointing in the direction of positive $x$-axis, are curled toward the positive $y$-axis, then the thumb will point in the direction of positive $z$-axis, perpendicular to the $x y$-plane. The broken lines in the figure represent the negative axes.

A point $P$ in space has three coordinates, one along $x$-axis, the second along $y$-axis and the third along $z$-axis. If the distances along $x$-axis, $y$-axis and $z$-axis respectively are $a, b$, and $c$, then the point $P$ is written with a unique triple of real numbers as $P=(a, b, c)$ (see figure).
right hand rule
version: 1.1

# 7.2.1 Concept of a vector in space

The set *R*^3 = ((*x*, *y*, *z*) : *x*, *y*, *z* ∈ *R*) is called the 3-dimensional space. An element (*x*, *y*, *z*) of *R*^3 represents a point *P*(*x*, *y*, *z*), which is uniquely determined by its coordinates *x*, *y* and *z*. Given a vector *u* in space, there exists a unique point *P*(*x*, *y*, *z*) in space such that the vector *∂P* is equal to *u* (see figure).

Now each element (*x*, *y*, *z*) ∈ *P*^3 is associated to a unique ordered triple [*x*, *y*, *z*], which represents the vector *u* = *∂P* = [*x*, *y*, *z*].

We define addition and scalar multiplication in *R*^3.

by:

- (i) **Addition:** For any two vectors *u* = [*x*, *y*, *z*] and *v* = [*x'*, *y'*, *z'*], we have

  *u* + *v* = [*x*, *y*, *z*] + [*x'*, *y'*, *z'*] = [*x* + *x'*, *y* + *y'*, *z* + *z'*]

- (ii) **Scalar Multiplication:** For *u* = [*x*, *y*, *z*] and *α* ∈ *R*, we have

  *αu* = *α*[*x*, *y*, *z*] = [*αx*, *αy*, *αz*]

**Definition:** The set of all ordered triples [*x*, *y*, *z*] of real numbers, together with the rules of addition and scalar multiplication, is called the set of **vectors** in *R*^3.

For the vector *u* = [*x*, *y*, *z*], *x*, *y* and *z* are called the components of *u*.

The definition of vectors in *R*^3 states that vector addition and scalar multiplication are to be carried out for vectors in space just as for vectors in the plane. So we define in *R*^3:

- a) The **negative** of the vector *u* = [*x*, *y*, *z*] as - *u* = (-1)*u* = [-*x*, -*y*, -*z*]
- b) The **difference** of two vectors *v* = [*x'*, *y'*, *z'*] and *v* = [*x'*, *y'*, *z'*] as *v* = *v* = *v* + (-*v*) = [*x'* - *x'*, *y'* - *y'*, *z'* - *z'*]
- c) The **zero vector** as 0 = [0,0,0]
- d) **Equality** of two vectors *v* = [*x'*, *y'*, *z'*] and *v* = [*x'*, *y'*, *z'*] by *v* if and only *x'* = *x'*, *y'* = *y'* and *z'* = *z'*.
- e) **Position Vector**

For any point *P*(*x*, *y*, *z*) in *R*^3, a vector *u* = [*x*, *y*, *z*] is represented by a directed line segment *∂P*, whose initial point is at origin. Such vectors are called position vectors in *R*^3.

- f) **Magnitude** of a vector: We define the **magnitude** or **norm** or **length** of a vector *u* in space by the distance of the point *P*(*x*, *y*, *z*) from the origin *O*.

  *∴* |*∂P*|=|*u*| = √*x*+*y*+*z*+

  **Example 1:** For the vectors *v* = [2,1,3] and *w* = [−1,4,0], we have the following

  - (i) *v* + *w* = [2 − 1, 1 + 4, 3 + 0] = [1,5,3]
  - (ii) *v* − *w* = [2 + 1,1 − 4, 3 − 0] = [3, −3, 3]
  - (iii) 2*w* = 2[−1, 4, 0] = [−2, 8, 0]
  - (iv) |*v* − 2*u*| = [2 + 2,1 − 8,3 − 0]| = [4, −7, 3]| = √(4)+(-7)+(3)+

# 7.2.2 Properties of Vectors

Vectors, both in the plane and in space, have the following properties:

Let *u*, *v* and *w* be vectors in the plane or in space and let *a*, *b* ∈ *R*, then they have the following properties

- (i) *u* + *v* = *v* + *u* (Commutative Property)
- (ii) (*u* + *v*) + *w* = *u* + (*v* + *w*) (Associative Property)
- (iii) *u* + (−1)*u* = *u* − *u* = 0 (Inverse for vector addition)
- (iv) *a*(*v* + *w*) = *a**v* + *a**w* (Distributive Property)
- (v) *a*(*bu*) = (*ab*)*u* (Scalar Multiplication)

**Proof:** Each statement is proved by writing the vector/vectors in component form in *R*^3 / *R*^3 and using the properties of real numbers. We give the proofs of properties (i) and (ii) as follows.

- (i) Since for any two real numbers *a* and *b*

  *a* + *b* = *b* + *a*, it follows, that

  for any two vectors *u* = [*x*, *y*] and *v* = [*x'*, *y'*] in *R*^3, we have

  *u* + *v* = [*x*, *y*] + [*x'* + *y'*]

  = [*x* + *x'*, *y* + *y'*]

  = [*x'* + *x*, *y'* + *y*]

  = [*x'*, *y'*] + [*x*, *y*]

  = *v* + *u*

  So addition of vectors in *R*^3 is commutative

(ii) Since for any three real numbers $a, b, c$,

$$
(a+b)+c=a+(b+c) \quad \text { it follows that }
$$

for any three vectors, $\underline{u}=[x, y], \underline{v}=\left(x^{\prime}, y^{\prime}\right]$ and $w\left[x^{\prime \prime}, y^{\prime \prime}\right]$ in $R^{2}$, we have

$$
\begin{aligned}
(\underline{u}+\underline{v})+\underline{w} & =\left[x+x^{\prime}, y+y^{\prime}\right]+\left[x^{\prime \prime}, y^{\prime \prime}\right] \\
& =\left[\left(x+x^{\prime}\right)+x^{\prime \prime},\left(y+y^{\prime}\right)+y^{\prime \prime}\right] \\
& =\left[x+\left(x^{\prime}+x^{\prime \prime}\right), y+\left(y^{\prime}+y^{\prime \prime}\right)\right] \\
& =\left[x, y\right]+\left[x^{\prime}+x^{\prime \prime}, y^{\prime}+y^{\prime \prime}\right] \\
& =\underline{u}+(\underline{v}+\underline{w})
\end{aligned}
$$

So addition of vectors in $R^{2}$ is associative
The proofs of the other parts are left as an exercise for the students.

### 7.2.3 Another notation for representing vectors in space

As in plane, similarly we introduce three special vectors

$$
\begin{aligned}
& \underline{i}=[1,0,0], \quad \underline{j}=[0,1,0] \text { and } \underline{k}=[0,0,1] \text { in } R^{1} \\
& \text { As magnitude of } \underline{i}=\sqrt{1^{2}+0^{2}+0^{2}}=1 \\
& \text { magnitude of } \underline{j}=\sqrt{0^{2}+1^{2}+0^{2}}=1
\end{aligned}
$$

and magnitude of $\underline{k}=\sqrt{0^{2}+0^{2}+1^{2}}=1$ So $\underline{i}, \underline{j}$ and $\underline{k}$ are called unit vectors along $x$-axis, along $y$-axis and along $z$-axis respectively. Using the definition of addition and scalar multiplication, the vector $[x, y, z]$ can be written as

$$
\begin{aligned}
\underline{u}=[x, y, z] & =[x, 0,0]+[0, y, 0]+[0,0, z] \\
& =x[1,0,0]+y[0,1,0]+z[0,0,, 1] \\
& =x \underline{i}+y \underline{j}+z \underline{k}
\end{aligned}
$$

Thus each vector $[x, y, z]$ in $R^{2}$ can be uniquely represented by $x \underline{i}+y \underline{j}+z \underline{k}$.
In terms of unit vector $\underline{i}, \underline{j}$ and $\underline{k}$, the sum $\underline{u}+\underline{v}$ of two vectors

$$
\begin{aligned}
& \underline{u}=[x, y, z] \text { and } \underline{v}\left[x^{\prime}, y^{\prime}, z^{\prime}\right] \text { is written as } \\
& \underline{u}+\underline{v}=\left[x+x^{\prime}, y+y^{\prime}, z+z^{\prime}\right] \\
& =\left(x+x^{\prime}\right)\left(\left.+\left(y+y^{\prime}\right)\right) \underline{i}+\left(z+z^{\prime}\right) \underline{k}\right.
\end{aligned}
$$

version: 1.1

### 7.2.4 Distance Between two Points in Space

If $\overrightarrow{O P_{1}}$ and $\overrightarrow{O P_{2}}$ are the position vectors of the points $P_{1}\left(x_{1}, y_{1}, z_{1}\right)$ and $P_{2}\left(x_{2}, y_{2}, z_{2}\right)$
The vector $\overrightarrow{P_{1} P_{2}}$, is given by

$$
\begin{aligned}
\overrightarrow{P_{1} P_{2}} & =\overrightarrow{O P_{1}}-\overrightarrow{O P_{1}}=\left[x_{2}-x_{1}, y_{2}-y_{1}, z_{2}-z_{1}\right] \\
\therefore \text { Distance between } P_{1} \text { and } P_{2} & =\left|\overrightarrow{P_{1} P_{2}}\right| \\
& =\sqrt{\left(x_{2}-x_{1}\right)^{2}+\left(y_{2}-y_{1}\right)^{2}+\left(z_{2}-z_{1}\right)^{2}}
\end{aligned}
$$

This is called distance formula between two points $P_{1}$ and $P_{2}$ in $R^{2}$,
Example 2: If $\underline{u}=2 \underline{i}+3 \underline{j}+\underline{k}, \underline{v}=4 \underline{i}+6 \underline{j}+2 \underline{k}$ and $\underline{w}=-6 \underline{i}-9 \underline{j}-3 \underline{k}$, then
(a) Find
(i) $\underline{u}+2 \underline{v}$
(ii) $|\underline{u}-\underline{v}-\underline{u}|$
(b) Show that $\underline{u}, \underline{v}$, and $\underline{w}$ are parallel to each other.

## Solution: (a)

(i) $\underline{u}+2 \underline{v}=2 \underline{i}+3 \underline{j}+\underline{k}+2(4 \underline{i}+6 \underline{j}+2 \underline{k})$

$$
\begin{aligned}
& =2 \underline{i}+3 \underline{j}+\underline{k}+8 \underline{i}+12 \underline{j}+4 \underline{k} \\
& =10 \underline{i}+15 \underline{j}+5 \underline{k}
\end{aligned}
$$

(ii) $\underline{u}-\underline{v}-w=(2 \underline{i}+3 \underline{j}+\underline{k})-(4 \underline{i}+6 \underline{j}+2 \underline{k})-\left(-6 \underline{i}-9 \underline{j}-3 \underline{k}\right)$

$$
=(2-4+6) \underline{i}+(3-6+9) \underline{j}+(1-2+3) \underline{k}
$$

$$
=4 \underline{i}+6 \underline{j}+2 \underline{k}
$$

(b) $\underline{v}=4 \underline{i}+6 \underline{j}+2 \underline{k}=2(2 \underline{i}+3 \underline{j}+\underline{k})$
$\therefore \underline{v}=2 \underline{u}$
$\Rightarrow \quad \underline{u}$ and $\underline{v}$ are parallel vectors, and have same direction
Again

$$
\begin{aligned}
\underline{w} & =-6 \underline{i}-9 \underline{j}-3 \underline{k} \\
& =-3(2 \underline{i}+3 \underline{j}+\underline{k}) \\
\therefore \underline{w} & =-3 \underline{u}
\end{aligned}
$$

$\Rightarrow \quad \underline{u}$ and $\underline{w}$ are parallel vectors and have opposite direction. Hence $\underline{u}, \underline{v}$ and $\underline{w}$ are parallel to each other.

# 7.2.5 Direction Angles and Direction Cosines of a Vector

Let $\underline{r}=\overrightarrow{O P}=x \underline{i}+y \underline{j}+z \underline{k}$ be a non-zero vector, let $\alpha, \beta$ and $\gamma$ denote the angles formed between $\underline{r}$ and the unit coordinate vectors $\underline{i}, \underline{j}$ and $\underline{k}$ respectively.
such that
$0 \leq \alpha \leq \pi, \quad 0 \leq \beta \leq \pi$, and $0 \leq \gamma \leq \pi$,
(i) the angles $\alpha, \beta, \gamma$ are called the direction angles and
(ii) the numbers $\cos \alpha, \cos \beta$ and $\cos \gamma$ are called direction cosines of the vector $\underline{r}$.

## Important Result:

Prove that $\cos ^{2} \alpha+\cos ^{2} \beta+\cos ^{2} \gamma=1$

## Let $\quad \underline{r}=[x, y, z]=x \underline{i}+y \underline{j}+z \underline{k}$
$\therefore \quad|\underline{r}|=\sqrt{x^{2}+y^{2}+z^{2}}=r$
then $\frac{\underline{r}}{|\underline{r}|}=\left[\frac{x}{r}, \frac{y}{r}, \frac{z}{r}\right]$ is the unit vector in the direction of the vector $\underline{r}=\overrightarrow{O P}$.
It can be visualized that the triangle $O A P$ is a right triangle with $\angle A=90^{\circ}$.
Therefore in right triangle $O A P$,

$$
\begin{aligned}
& \cos \alpha=\frac{\overrightarrow{O A}}{\overrightarrow{O P}}=\frac{x}{r}, \text { similarly } \\
& \cos \beta=\frac{y}{r}, \cos \gamma=\frac{z}{r}
\end{aligned}
$$

The numbers $\cos \alpha=\frac{x}{r}, \cos \beta=\frac{y}{r}$ and $\cos \gamma=\frac{z}{r}$ are called the direction cosines of $\overrightarrow{O P}$.
$\therefore \quad \cos ^{2} \alpha+\cos ^{2} \beta+\cos ^{2} \gamma=\frac{x^{2}}{r^{2}}+\frac{y^{2}}{r^{2}}+\frac{z^{2}}{r^{2}}=\frac{z^{2}+y^{2}+z^{2}}{r^{2}}=\frac{r^{2}}{r^{2}}=1$

## EXERCISE 7.2

1. Let $A=(2,5), B=(-1,1)$ and $C=(2,-6)$. Find
(i) $\overrightarrow{A B}$
(ii) $2 \overrightarrow{A B}-\overrightarrow{C B}$
(iii) $2 \overrightarrow{C B}-2 \overrightarrow{C A}$
2. Let $\underline{u}=\underline{i}+2 \underline{j}-\underline{k}, \underline{v}=3 \underline{i}-2 \underline{j}+2 \underline{k}, \underline{w}=5 \underline{i}-\underline{j}+3 \underline{k}$. Find the indicated vector or number.
(i) $\underline{u}+2 \underline{v}+\underline{w}$
(ii) $\underline{u}-3 \underline{w}$
(iii) $|3 \underline{v}+\underline{w}|$
3. Find the magnitude of the vector $\underline{v}$ and write the direction cosines of $\underline{v}$.
(i) $\underline{v}=2 \underline{i}+3 \underline{j}+4 \underline{k}$
(ii) $\underline{v}=\underline{i}-\underline{j}-\underline{k}$
(iii) $\underline{v}=4 \underline{i}-5 \underline{j}$
4. Find $\alpha$, so that $|\alpha \underline{i}+(\alpha+1) \underline{j}+2 \underline{k}|=3$.
5. Find a unit vector in the direction of $\underline{v}=\underline{i}+2 \underline{j}-\underline{k}$.
6. If $\underline{a}=3 \underline{i}-\underline{j}-4 \underline{k}, \underline{b}=-2 \underline{i}-4 \underline{j}-3 \underline{k}$ and $\underline{c}=\underline{i}+2 \underline{j}-\underline{k}$.

Find a unit vector parallel to $3 \underline{a}-2 \underline{b}+4 \underline{c}$.
7. Find a vector whose
(i) magnitude is 4 and is parallel to $2 \underline{i}-3 \underline{j}+6 \underline{k}$
(ii) magnitude is 2 and is parallel to $-\underline{i}+\underline{j}+\underline{k}$
8. If $\underline{u}=2 \underline{i}+3 \underline{j}+4 \underline{k}, \underline{v}=-i+3 \underline{j}-\underline{k}$ and $\underline{w}=\underline{i}+6 \underline{j}+z \underline{k}$ represent the sides of a triangle. Find the value of $z$.
9. The position vectors of the points $A, B, C$ and $D$ are $2 \underline{i}-\underline{j}+\underline{k}, 3 \underline{i}+\underline{j}$, $2 \underline{i}+4 \underline{j}-2 \underline{k}$ and $-\underline{i}-2 \underline{j}+\underline{k}$ respectively. Show that $\overrightarrow{A B}$ is parallel to $\overrightarrow{C D}$.
10. We say that two vectors $\underline{v}$ and $\underline{w}$ in space are parallel if there is a scalar $c$ such that $\underline{v}=c \underline{w}$. The vectors point in the same direction if $c>0$, and the vectors point in the opposite direction if $c<0$
(a) Find two vectors of length 2 parallel to the vector $\underline{v}=2 \underline{i}-4 \underline{j}+4 \underline{k}$.
(b) Find the constant $a$ so that the vectors $\underline{v}=\underline{i}-3 \underline{j}+4 \underline{k}$ and $\underline{w}=\underline{a i}+9 \underline{j}-12 \underline{k}$ are parallel.
(c) Find a vector of length 5 in the direction opposite that of $\underline{v}=\underline{i}-2 \underline{j}+3 \underline{k}$.
(d) Find $a$ and $b$ so that the vectors $3 \underline{i}-\underline{j}+4 \underline{k}$ and $\underline{a i}+b \underline{j}-2 \underline{k}$ are parallel.

7. Vectors
eLearn.Punjab
11. Find the direction cosines for the given vector:
(i) $$y = 3i - \frac{1}{2} + 2k$$
(ii) $$6i - 2\frac{1}{2} + k$$
(iii) $$\overrightarrow{PQ}$$, where $$P = (2, 1, 5)$$ and $$Q$$ (1, 3, 1).
12. Which of the following triples can be the direction angles of a single vector:
(i) $$45^\circ, 45^\circ, 60^\circ$$
(ii) $$30^\circ, 45^\circ, 60^\circ$$
(iii) $$45^\circ, 60^\circ, 60^\circ$$

7.3 THE SCALAR PRODUCT OF TWO VECTORS

We shall now consider products of two vectors that originated in the study of Physics
and Engineering. The concept of angle between two vectors is expressed in terms of a **scalar product of two vectors**.

Definition 1:
Let two non-zero vectors $$u$$ and $$y$$, in the plane or in space, have same initial point. The
dot product of $$u$$ and $$y$$, written as $$u.y$$, is defined by

$$u.y = |u| |y| \cos \theta$$

where $$\theta$$ is the angle between $$u$$ and $$y$$ and $$0 \leq 6 \leq \pi$$

Definition 2:
(a) If $$u = a_1 + b_1 \frac{1}{2} = a_2 + b_2 \frac{1}{2} + b_2 \frac{1}{2}$$
are two non-zero vectors in the plane. The dot product $$u.y$$ is defined by
$$u.y = a_1, a_2 + b_1, b_2$$
(b) If $$u = a_1 + b_1 \frac{1}{2} + c_1 k$$
and $$y = a_1 + b_1 \frac{1}{2} + c_2 k$$
are two non-zero vectors in space. The dot product $$u.y$$ is defined by
$$u.y = a_1, a_2 + b_1, b_2 + c_1 c_2$$

Note: The dot product is also referred to the scalar product or the inner product.

version: 1.1

7.3.1 Deductions of the Important Results

By Applying the definition of dot product to unit vectors $$\frac{1}{2}, \frac{k}{2}$$, we have,

(a) $$(.\frac{1}{2} = |(\frac{1}{2})| \cos 0^\circ 1$$
(b) $$(\frac{1}{2} = |(\frac{1}{2})| \cos 90^\circ 0$$
$$\frac{1}{2} = |(\frac{1}{2})| \cos 90^\circ 0$$
$$\frac{k}{2} = |(\frac{1}{2})| \cos 90^\circ 0$$
(c) $$u.y = |u| |y| \cos \theta$$
$$= |(\frac{1}{2})|u| \cos(-\theta)$$
$$= |(\frac{1}{2})|u| \cos \theta$$

$$\Rightarrow \quad u.y = y.u$$

Dot product of two vectors is commutative.

7.3.2 Perpendicular (Orthogonal) Vectors

Definition: Two non-zero vectors $$u$$ and $$y$$ are perpendicular if and only if $$u.y = 0$$.
Since angle between $$u$$ and $$y$$ is $$\frac{\pi}{2}$$ and $$\cos \frac{\pi}{2} = 0$$
so $$u.y = |u| |y| \cos \frac{\pi}{2}$$
$$\therefore \quad u.y = 0$$

Note: As $$u = 0$$, for every vector $$b$$. So the zero vector is regarded to be perpendicular
to every vector.

7.3.3 Properties of Dot Product

Let $$u$$, $$y$$ and $$w$$ be vectors and let $$c$$ be a real number, then
(i) $$u.y = 0 \Rightarrow u = 0$$ or $$y = 0$$

(ii) $\mu, \underline{v}=\underline{v}, \underline{u}$
(commutative property)
(iii) $\mu \cdot(\underline{v}+\underline{w})=\underline{u}, v+\underline{u}, \underline{w}$
(distributive property)
(iv) $\left(c \underline{u}\right), \underline{v}=\underline{c}(\underline{u}, \underline{v})$.
(c is scalar)

The proofs of the properties are left as an exercise for the students.

### 7.3.4 Analytical Expression of Dot Product $\underline{u}, \underline{v}$ (Dot product of vectors in their components form)

Let $\underline{u}=a_{1} \underline{i}+b_{1} \underline{j}+c_{1} \underline{k}$ and $\underline{v}=a_{2} \underline{i}+b_{2} \underline{j}+c_{2} \underline{k}$
be two non-zero vectors.
From distributive Law we can write:

$$
\begin{aligned}
\therefore \underline{u}, \underline{v}= & \left(a_{1} \underline{i}+b_{1} \underline{j}+c_{1} \underline{k}\right)\left(a_{2} \underline{i}+b_{2} \underline{j}+c_{2} \underline{k}\right) \\
= & a_{1} a_{2}(\underline{i}, \underline{i})+a_{2} b_{1}(\underline{i}, \underline{j})+a_{1} c_{1}(\underline{i}, \underline{k}) \\
& +b_{1} a_{2}(\underline{j}, \underline{i})+b_{1} b_{2}(\underline{j}, \underline{j})+b_{1} c_{2}(\underline{j}, \underline{k}) \\
& +c_{1} a_{2}(\underline{k}, \underline{i})+c_{2} b_{2}(\underline{k}, \underline{j})+c_{1} c_{2}(\underline{k}, \underline{k})
\end{aligned}
$$

$$
\Rightarrow \underline{u}, \underline{v}=a_{1} a_{2}+b_{1} b_{2}+c_{1} c_{2}
$$

Hence the dot product of two vectors is the sum of the product of their corresponding components.
Equivalence of two definitions of dot product of two vectors has been proved in the following example.

Example 1: (i) If $\underline{v}=\left[\underline{x}_{1}, \underline{y}_{1}\right]$ and $\underline{w}=\left[\underline{x}_{2}, \underline{y}_{2}\right]$ are two vectors in the plane, then
$\underline{v}, \underline{w}=\underline{x}_{1} \underline{x}_{2}+\underline{y}_{1} \underline{y}_{2}$
(ii) If $\underline{v}$ and $\underline{w}$ are two non-zero vectors in the plane, then
$\underline{v}, \underline{w}=\underline{\underline{x}} \underline{\underline{x}} \underline{\underline{x}} \cos \theta$
where $\theta$ is the angle between $\underline{v}$ and $\underline{w}$ and $0 \leq \theta \leq \pi$.
Proof: Let $\underline{v}$ and $\underline{w}$ determine the sides of a triangle then the third side, opposite to the angle $\theta$, has length $\mid \underline{v}-\underline{w} \mid$ (by triangle law of addition of vectors)

By law of cosines,

$$
\begin{aligned}
& \mid \underline{v}-\underline{w} \mid^{2}=\left|\underline{v}\right|^{2}+\left|\underline{w}\right|^{2}-2\left|\underline{v}\right| \mid \underline{w} \cos \theta \\
& \text { if } \quad \underline{v}=\left[\underline{x}_{1}, \underline{y}_{1}\right] \text { and } \underline{w}\left[\underline{x}_{2}, \underline{y}_{2}\right], \text { then } \\
& \underline{v}-\underline{w}=\left[\underline{x}_{1}-\underline{x}_{2}, \underline{y}_{1}-\underline{y}_{2}\right]
\end{aligned}
$$

So equation (1) becomes:

$$
\begin{aligned}
& \left|\underline{x}_{1}-\underline{x}_{2}\right|^{2}+\left|\underline{y}_{1}-\underline{y}_{2}\right|^{2}=\left|\underline{x}_{1}^{2}+\underline{y}_{1}^{2}\right|+\left|\underline{x}_{2}^{2}+\underline{y}_{2}^{2}\right|-2\left|\underline{v}\right| \mid \underline{w} \cos \theta \\
& -2 \underline{x}_{1} \underline{x}_{2}-2 \underline{y}_{1} \underline{y}_{2}=2\left|\underline{v}\right| \mid \underline{w} \cos \theta \\
& \Rightarrow \quad \underline{x}_{1} \underline{x}_{2}+\underline{y}_{1} \underline{y}_{2}=\left|\underline{v}\right| \mid \underline{w} \cos \theta=\underline{v}, \underline{w}
\end{aligned}
$$

Example 2: If $\underline{u}=3 \underline{i}-\underline{j}-2 \underline{k}$ and $\underline{v}=\underline{i}+2 \underline{j}-\underline{k}$, then
$\underline{u}, \underline{v}=(-3)(1)+(-1)(2)+(-2)(-1)=3$
Example 3: If $\underline{u}=2 \underline{i}-4 \underline{j}+5 \underline{k}$ and $\underline{v}=-4 \underline{i}-3 \underline{j}-4 \underline{k}$, then
$\underline{u}, \underline{v}=(2)(4)+(-4)(-3)+(5)(-4)=0$
$\Rightarrow \underline{u}$ and $\underline{v}$ are perpendicular

### 7.3.5 Angle between two vectors

The angle between two vectors $\underline{u}$ and $\underline{v}$ is determined from the definition of dot product, that is
(a) $\underline{u}, \underline{v}=\underline{\underline{u}} \underline{\underline{u}} \underline{\underline{v}} \cos \theta, \quad$ where $0 \quad \theta \quad \pi$

$$
\therefore \cos \theta=\frac{\underline{u}, \underline{v}}{\underline{\underline{u}} \underline{\underline{v}}}
$$

(b) $\underline{u}=a_{1} \underline{i}+b_{1} \underline{j}+c_{1} \underline{k}$ and $\underline{v}=a_{2} \underline{i}+b_{2} \underline{j}+c_{2} \underline{k}$, then
$\underline{u}, \underline{v}=a_{1} a_{2}+b_{1} b_{2}+c_{1} c_{2}$
$\left|\underline{u}\right|=\sqrt{a_{1}^{2}+b_{1}^{2}+c_{1}^{2}}$ and $\left|\underline{v}\right|=\sqrt{a_{2}^{2}+b_{2}^{2}+c_{2}^{2}}$
$\therefore \quad \cos \theta=\frac{\underline{u}, \underline{v}}{\underline{\underline{u}} \underline{\underline{v}} \underline{\underline{v}}}$

$\therefore \quad \cos \theta=\frac{a_{1} a_{2}+b_{1} b_{2}+c_{1} c_{2}}{\sqrt{a_{1}^{2}+b_{1}^{2}+c_{1}^{2}} \sqrt{a_{2}^{2}+b_{2}^{2}+c_{2}^{2}}}$

# Corollaries:

(i) If $\theta=0$ or $\pi$, the vectors $\mu$ and $\gamma$ are collinear.
(ii) If $\theta=\frac{\pi}{2}, \cos \theta=0 \Rightarrow \underline{\underline{u}} \underline{\underline{v}}=0$.

The vectors $\underline{u}$ and $\gamma$ are perpendicular or orthogonal.
Example 4: Find the angle between the vectors
$\underline{u}=2 i-\underline{j}+\underline{k} \quad$ and $\quad \gamma=-i+\underline{j}$
Solution: $\underline{u} \cdot \underline{v}=(2 i-\underline{j}+\underline{k}) \cdot(-i+\underline{j}+0 \underline{k})$

$$
=(2 i(-1)+(-1)(1)+(1)(0)=-3
$$

$$
\begin{aligned}
\therefore \quad|\underline{u}| & =|2 i-\underline{j}+\underline{k}|=\sqrt{(2)^{2}+(-1)^{2}+(1)^{2}}=\sqrt{6} \\
\text { and } \quad|\underline{v}| & =|-i+\underline{j}+0 \underline{k}|=\sqrt{(-1)^{2}+(1)^{2}+(0)^{2}}=\sqrt{2}
\end{aligned}
$$

Now $\quad \cos \theta=\frac{\underline{u} \cdot \underline{v}}{|\underline{u}| \cdot|\underline{v}|}$

$$
\begin{aligned}
\Rightarrow \quad \cos \theta & =\frac{-3}{\sqrt{6} \sqrt{2}}=\frac{\sqrt{3}}{2} \\
\therefore \theta & =\frac{5 \pi}{6}
\end{aligned}
$$

Example 5: Find a scalar $\alpha$ so that the vectors $2 i+\alpha \underline{j}+5 \underline{k}$ and $3 i+\underline{j}+\alpha \underline{k}$ are perpendicular.

## Let $\quad \underline{u}=2 i+\alpha \underline{j}+5 \underline{k}$ and $\quad \gamma=3 i+\underline{j}+\alpha \underline{k}$
It is given that $\underline{u}$ and $\gamma$ are perpendicular
$\therefore \underline{u} \cdot \underline{v}=0$
version: 1.1
$\Rightarrow \quad(2 i+\alpha \underline{j}+5 \underline{k}) \cdot(3 i+\underline{j}+\alpha \underline{k})=0$
$\Rightarrow \quad 6+\alpha+5 \alpha=0$
$\therefore \quad \alpha=1$

## Example 6:

Show that the vectors $2 i-\underline{j}+\underline{k}, i-3 \underline{j}-5 \underline{k}$ and $3 i-4 \underline{j}-4 \underline{k}$ form the sides of a right triangle.
Solution:
Let $\overline{A B}=2 i-\underline{j}+\underline{k}$ and $\overline{B C}=\underline{i}-3 \underline{j}-5 \underline{k}$
Now $\overline{A B}+\overline{B C}=(2 i-\underline{j}+\underline{k})+(\underline{i}-3 \underline{j}-5 \underline{k})$

$$
=3 i-4 \underline{j}-4 \underline{k}=\overline{A C} \quad \text { (third side) }
$$

$\therefore \overline{A B}, \overline{B C}$ and $\overline{A C}$ form a triangle $A B C$.
Further we prove that $\triangle A B C$ is a right triangle

$$
\begin{aligned}
\overline{A B} \cdot \overline{B C} & =(2 i-\underline{j}+\underline{k}) \cdot(\underline{i}-3 \underline{j}-5 \underline{k}) \\
& =(2)(1)+(-1)(-3)+(1)(-5) \\
& =2+3-5 \\
& =0
\end{aligned}
$$

$\therefore \overline{A B} \perp \overline{B C}$
Hence $\triangle A B C$ is a right triangle.

### 7.3.6 Projection of one Vector upon another Vector:

In many physical applications, it is required to know "how much" of a vector is applied along a given direction. For this purpose we find the projection of one vector along the other vector.

Let $\overline{O A}=\underline{u}$ and $\overline{O B}=\gamma$
Let $\theta$ be the angle between them, such that $0 \leq \theta \leq \pi$.
Draw $\overline{B M} \perp O A$. Then $\overline{O M}$ is called the projection of $\chi$ along $\mu$.

$$
\begin{aligned}
& \text { Now } \quad \frac{\overline{O M}}{\overline{O B}}=\cos \theta \text {, that is, } \\
& \overline{O M}=\|\overline{O B}\| \cos \theta=\|\underline{\underline{x}}\| \cos \theta
\end{aligned}
$$

By definition, $\cos \theta=\frac{\underline{\underline{u}} \cdot \underline{\underline{v}}}{\|\underline{\underline{u}}\| \underline{\underline{v}}}$
From (1) and (2), $\overline{O M}=\|\underline{\underline{x}}\| \frac{\underline{\underline{u}} \cdot \underline{\underline{v}}}{\|\underline{\underline{u}}\| \underline{\underline{v}}}\|}$

Projection of $\underline{\underline{v}}$ along $\underline{\underline{u}}=\frac{\underline{\underline{u}} \cdot \underline{\underline{v}}}{\|\underline{\underline{u}}\|}$
Similarly, projection of $\underline{\underline{u}}$ along $\underline{\underline{v}}=\frac{\underline{\underline{u}} \cdot \underline{\underline{v}}}{\|\underline{\underline{v}}\|}$

Example 7: Show that the components of a vector are the projections of that vector along $\underline{i}, \underline{j}$ and $\underline{k}$ respectively.

Solution: Let $\underline{\underline{v}}=a \underline{i}+b \underline{j}+c \underline{k}$, then
Projection of $\underline{\underline{v}}$ along $\underline{i}=\frac{\underline{v} \cdot \underline{j}}{\|\underline{\underline{i}}\|}=(a \underline{i}+b \underline{j}+c \underline{k}) \cdot \underline{i}=a$
Projection of $\underline{\underline{v}}$ along $\underline{j}=\frac{\underline{v} \cdot \underline{j}}{\|\underline{\underline{j}}\|}=(a \underline{i}+b \underline{j}+c \underline{k}) \cdot \underline{j}=b$
Projection of $\underline{\underline{v}}$ along $\underline{k}=\frac{\underline{v} \cdot \underline{k}}{\|\underline{\underline{k}}\|}=(a \underline{i}+b \underline{j}+c \underline{k}) \cdot \underline{k}=c$
Hence components $a, b$ and $c$ of vector $\underline{\underline{v}}=a \underline{i}+b \underline{j}+c \underline{k}$ are projections of vector $\underline{\underline{v}}$ along $\underline{i}, \underline{j}$ and $\underline{k}$ respectively.

Example 8: Prove that in any triangle $A B C$
(i) $a^{2}=b^{2}+c^{2}-2 b c \cos A$
(ii) $a=b \cos C+c \cos B$

$$
\text { (Cosine Law) }
$$

(Projection Law)

Solution: Let the vectors $\underline{a}, \underline{b}$ and $\underline{c}$ be along the sides $B C, C A$ and $A B$ of the triangle $A B C$ as shown in the figure.
$\therefore \quad \underline{a}+\underline{b}+\underline{c}=\underline{0}$
$\Rightarrow \quad \underline{a}=-(\underline{b}+\underline{c})$
Now $\underline{a} \cdot \underline{a}=(\underline{b}+\underline{c}) \cdot(\underline{b}+\underline{c})$
$\Rightarrow \quad=b \cdot b+b \cdot c+c \cdot b+c \cdot c$
$\Rightarrow \quad a^{2}=b^{2}+2 \underline{b} \cdot \underline{c}+c^{2}$
$\Rightarrow \quad a^{2}=b^{2}+c^{2}+2 b c \cdot \cos (\pi-A)$
$\therefore \quad a^{2}=b^{2}+c^{2}-2 b c \cos A$
(ii) $\quad \underline{a}+\underline{b}+\underline{c}=\underline{0}$
$\Rightarrow \quad \underline{a}=-\underline{b}-\underline{c}$
Take dot product with $\underline{a}$
$\underline{a} \cdot \underline{a}=-\underline{a} \cdot \underline{b}-\underline{a} \cdot \underline{c}$
$=-a b \cos (\pi-C)-a c \cos (\pi-B)$
$a^{2}=a b \cos C+a c \cos B$
$\Rightarrow a=b \cos C+c \cos B$
Example 9: Prove that: $\cos (\alpha-\beta)=\cos \alpha \cos \beta+\sin \alpha \sin \beta$
Solution: Let $\overline{O A}$ and $\overline{O B}$ be the unit vectors in the $x y$-plane making angles $\alpha$ and $\beta$ with the positive $x$-axis.

$$
\begin{aligned}
& \text { So that } \angle A O B=\alpha-\beta \\
& \text { Now } \overline{O A}=\cos \alpha \underline{i}+\sin \alpha \underline{j} \\
& \text { and } \overline{O B}=\cos \beta \underline{i}+\sin \beta \underline{j} \\
& \therefore \overline{O A} \cdot \overline{O B}=(\cos \alpha \underline{i}+\sin \alpha \underline{j}) \cdot(\cos \beta \underline{i}+\sin \beta \underline{j}) \\
& \Rightarrow\|\overline{O A}\| \overline{O B} \cdot \cos (\alpha-\beta)=\cos \alpha \cos \beta+\sin \alpha \sin \beta \\
& \therefore \cos (\alpha-\beta)=\cos \alpha \cos \beta+\sin \alpha \sin \beta
\end{aligned}
$$

$(\because \mid \overline{O A} \mid=\mid \overline{O B} \mid=1)$

## EXERCISE 7.3

1. Find the cosine of the angle $\theta$ between $\mu$ and $\gamma$ :
(i) $\mu=3 i+j-k, \gamma=2 i-j+k$
(ii) $\mu=i-3 j+4 k, \gamma=4 i-j+3 k$
(iii) $\mu=\left[3 z-5\right], \gamma[6,-2]$
(iv) $\mu=\left[2,3,1\right], \gamma[2,4,1]$
2. Calculate the projection of $\underline{a}$ along $\underline{b}$ and projection of $\underline{b}$ along $\underline{a}$ when:
(i) $\quad a=i \quad k \neq b \quad j \quad k$
(ii) $\underline{a}=3 i+j-k, \underline{b}=-2 i-j+k$
3. Find a real number $\alpha$ so that the vectors $\mu$ and $\gamma$ are perpendicular.
(i) $\mu=2 \alpha i+j-k, \quad \gamma=i+\alpha j+4 k$
(ii) $\mu=\alpha i+2 \alpha j+3 k, \quad \gamma=i+\alpha j+3 k$
4. Find the number $z$ so that the triangle with vertices $A(1,-1,0), B(-2,2,1)$ and $C(0,2, z)$ is a right triangle with right angle at $C$.
5. If $\gamma$ is a vector for which
$\gamma_{i}=0, \gamma_{i j}=0, \gamma_{i} k=0$, find $\gamma_{i}$.
6. (i) Show that the vectors $3 i-2 j+k, i-3 j+5 k$ and $2 i+j-4 k$ form a right angle.
(ii) Show that the set of points $P=(1,3,2), Q=(4,1,4)$ and $P=(6,5,5)$ form a right triangle.
7. Show that mid point of hypotenuse a right triangle is equidistant from its vertices.
8. Prove that perpendicular bisectors of the sides of a triangle are concurrent.
9. Prove that the altitudes of a triangle are concurrent.
10. Prove that the angle in a semi circle is a right angle.
11. Prove that $\cos (\alpha+\beta)=\cos \alpha \cos \beta-\sin \alpha \sin \beta$
12. Prove that in any triangle $A B C$.
(i) $b=c \cos A+a \cos C$
(ii) $c=a \cos B+b \cos A$
(iii) $b^{2}=c^{2}+a^{2}-2 c a \cos B$
(iv) $c^{2}=a^{2}+b^{2}-2 a b \cos C$.

### 7.4 THE CROSS PRODUCT OR VECTOR PRODUCT OF TWO VECTORS

The vector product of two vectors is widely used in Physics, particularly, Mechanics and Electricity. It is only defined for vectors in space.

Let $\mu$ and $\gamma$ be two non-zero vectors. The cross or vector product of $\mu$ and $\gamma$, written as $\mu \times \gamma$, is defined by
Figure (a)
Figure (b)

## Right hand rule

(i) If the fingers of the right hand point along the vector $\underline{\mu}$ and then curl towards the vector $\gamma$, then the thumb will give the direction of $\underline{\hat{\eta}}$ which is $\underline{\mu} \times \gamma$. It is shown in the figure (a).
(ii) In figure (b), the right hand rule shows the direction of $\gamma \times \mu$.

### 7.4.1 Derivation of useful results of cross products

(a) By applying the definition of cross product to unit vectors $\underline{i}, \underline{j}$ and $\underline{k}$, we have:
(a) $\quad i \times i=|i||i| \sin 0^{\circ} \underline{\hat{n}}=0$

$$
\begin{aligned}
& \underline{j} \times \underline{j}=|j||j| \sin 0^{\circ} \underline{\hat{n}}=0 \\
& \underline{k} \times \underline{k}=|\underline{k}||\underline{k}| \sin 0^{\circ} \underline{\hat{n}}=0
\end{aligned}
$$

(b) $\quad i \times \underline{j}=|i||j| \sin 90^{\circ} \underline{k}=\underline{k}$

$$
\begin{aligned}
& \underline{j} \times \underline{k}=|j|||\underline{k}| \sin 90^{\circ} i=i \\
& \underline{k} \times i=|\underline{k}||\underline{i}| \sin 90^{\circ} \underline{j}=\underline{j}
\end{aligned}
$$

(c) $\underline{\mu} \times \gamma=|\underline{\mu}||\underline{i}| \sin \theta \underline{\hat{n}}=|\underline{\gamma}||\underline{\mu}| \sin (-\theta) \underline{\hat{n}}=-|\underline{\gamma}||\underline{\mu}| \sin \theta \underline{\hat{n}}$
$\Rightarrow \quad \underline{\mu} \times \gamma=-\gamma \times \underline{\mu}$
(d) $\underline{\mu} \times \underline{\mu}=|\underline{\mu}||\underline{\mu}| \sin 0^{\circ} \underline{\hat{n}}=0$
Note: The cross product of $i, j$ and $k$ are written in the cyclic pattern. The given figure is helpful in remembering this pattern.
# 7.4.2 Properties of Cross product

The cross product possesses the following properties:
(i) $\underline{u} \times \underline{v}=\underline{0}$ if $\underline{u}=\underline{0}$ or $\underline{v}=\underline{0}$
(ii) $\underline{u} \times \underline{v}=-\underline{v} \times \underline{u}$
(iii) $\underline{u} \times(\underline{v}+\underline{w})=\underline{u} \times \underline{v}+\underline{u} \times \underline{w} \quad$ (Distributive property)
(iv) $\underline{u} \times(k \underline{v})=(k \underline{u}) \times \underline{v}=k(\underline{u} \times \underline{v}), \quad k$ is scalar
(v) $\underline{u} \times \underline{u}=\underline{0}$

The proofs of these properties are left as an exercise for the students.

### 7.4.3 Analytical Expression of $\underline{u} \times \underline{v}$

(Determinant formula for $\underline{u} \times \underline{v}$ )

Let $\underline{u}=a_{1}\left(+b_{1} \underline{j}+c_{1} \underline{k}\right.$ and $\left.\underline{v}=a_{2}\left(+b_{2} \underline{j}+c_{2} \underline{k}\right), \quad\right.$ then

$$
\begin{aligned}
\underline{u} \times \underline{v} & =\left(a_{1}\left(+b_{1} \underline{j}+c_{1} \underline{k}\right) \times\left(a_{2}\left(+b_{2} \underline{j}+c_{2} \underline{k}\right)\right.\right. \\
& =a_{1} a_{2}\left(\left(\times \underline{i}\right)+a_{1} b_{2}\left(\left(\times \underline{j}\right)+a_{1} c_{2}\left(\left(\times \underline{k}\right)\right.\right.\right. \quad \text { (by distributive property) } \\
& \left.+b_{1} a_{2}\left(\underline{j} \times \underline{i}\right)+b_{1} b_{2}\left(\underline{j} \times \underline{j}\right)+b_{1} c_{2}\left(\underline{j} \times \underline{k}\right)\right) \quad \therefore\left(\times \underline{j}=\underline{k}=-\underline{j} \times \underline{i}\right. \\
& +c_{1} a_{2}\left(\underline{k} \times \underline{i}\right)+c_{1} b_{2}\left(\underline{k} \times \underline{j}\right)+c_{1} c_{2}\left(\underline{k} \times \underline{k}\right) \quad\left(\times\left(=\underline{j} \times \underline{j}=\underline{k} \times \underline{k}=0\right.\right. \\
& \left.=a_{1} b_{2} \underline{k}-a_{1} c_{2} \underline{j}-b_{1} a_{2} \underline{k}+b_{1} c_{2}\left(+c_{1} a_{2} \underline{j}-c_{1} b_{2}\right)\right) \\
\Rightarrow \underline{u} \times \underline{v} & =\left(b_{1} c_{2}-c_{1} b_{2}\right)\left(\left(-\left(a_{1} c_{2}-c_{1} a_{2}\right) \underline{j}+\left(a_{1} b_{2}-b_{1} a_{2}\right) \underline{k}\right.\right.
\end{aligned}
$$

The expansion of $3 \times 3$ determinant

$$
\left|\begin{array}{ccc}
\underline{i} & \underline{j} & \underline{k} \\
a_{1} & b_{1} & c_{1} \\
a_{2} & b_{2} & c_{2}
\end{array}\right|=\left(b_{1} c_{2}-c_{1} b_{2}\right)\left(-\left(a_{1} c_{2}-c_{1} a_{2}\right) \underline{j}+\left(a_{1} b_{2}-b_{1} a_{2}\right) \underline{k}\right.
$$

The terms on R.H.S of equation (i) are the same as the terms in the expansion of the above determinant

$$
\text { Hence } \underline{u} \times \underline{v}=\left|\begin{array}{ccc}
\underline{i} & \underline{j} & \underline{k} \\
a_{1} & b_{1} & c_{1} \\
a_{2} & b_{2} & c_{2}
\end{array}\right|
$$

which is known as determinant formula for $\underline{u} \times \underline{v}$.

Note: The expression on R.H.S. of equation (ii) is not an actual determinant, since its entries are not all scalars. It is simply a way of remembering the complicated expression on R.H.S. of equation (i).

### 7.4.4 Parallel Vectors

If $\underline{u}$ and $\underline{v}$ are parallel vectors, $(\theta=\mathbf{0} \quad \sin \theta$ ) then
$\underline{u} \times \underline{v}=\|\underline{u}\| \frac{1}{2} \sin \theta \hat{n}$
$\underline{u} \times \underline{v}=\underline{0}$ or $\underline{v} \times \underline{u}=0$
And if $\underline{u} \times \underline{v}=\underline{0}$, then
either $\sin \theta=0$ or $\left|\underline{u}\right|=0$ or $\left|\underline{v}\right|=0$
(i) If $\sin \theta=0 \Rightarrow \theta=0^{\prime}$ or $180^{\prime}$, which shows that the vectors $\underline{u}$ and $\underline{v}$ are parallel.
(ii) If $\underline{u}=0$ or $\underline{v}=0$, then since the zero vector has no specific direction, we adopt the convention that the zero vector is parallel to every vector.

Note: Zero vector is both parallel and perpendicular to every vector. This apparent contradiction will cause no trouble, since the angle between two vectors is never applied when one of them is zero vector.

Example 1: Find a vector perpendicular to each of the vectors

$$
\underline{a}=2 \underline{i}+\underline{j}+\underline{k} \quad \text { and } \quad \underline{b}=4 \underline{i}+2 \underline{j}-\underline{k}
$$

Solution: A vector perpendicular to both the vectors $\underline{a}$ and $\underline{b}$ is $\underline{a} \times \underline{b}$

$$
\therefore \quad \underline{a} \times \underline{b}=\left|\begin{array}{ccc}
\underline{i} & \underline{j} & \underline{k} \\
2 & -1 & 1 \\
4 & 2 & -1
\end{array}\right|=-i+6 \underline{j}+8 \underline{k}
$$

Verification:

$$
\underline{a}, \underline{a} \times \underline{b}=(2 i+\underline{j}+\underline{k}) \cdot(-i+6 \underline{j}+8 \underline{k})=(2)(-1)+(-1)(6)+(1)(8)=0
$$

and $\quad \underline{b}, \underline{a} \times \underline{b}=(4 i+2 \underline{j}-\underline{k}) \cdot(-i+6 \underline{j}+8 \underline{k})=(4)(-1)+(2)(6)+(-1)(8)=0$
Hence $\underline{a} \times \underline{b}$ is perpendicular to both the vectors $\underline{a}$ and $\underline{b}$.

Example 2: If $\underline{a}=4 i+3 \underline{j}+\underline{k}$ and $\underline{b}=2 i-\underline{j}+2 \underline{k}$. Find a unit vector perpendicular to both $\underline{a}$ and $\underline{b}$. Also find the sine of the angle between the vectors $\underline{a}$ and $\underline{b}$.

$$
\underline{a} \times \underline{b}=\left|\begin{array}{ccc}
\underline{i} & \underline{k} & \\
4 & 3 & 1 \\
2 & -1 & 2
\end{array}\right|=7 i-6 \underline{j}-10 \underline{k}
$$

and $\quad \underline{a} \times \underline{b}=\sqrt{(7)^{2}+(-6)^{2}+(10)^{2}}=\sqrt{185}$
$\therefore \quad$ A unit vector $\underline{\theta}$ perpendicular to $\underline{a}$ and $\underline{b}=\left|\begin{array}{l}\underline{a} \times \underline{b} \\ \underline{a} \times \underline{b}\end{array}\right|$

$$
=\frac{1}{\sqrt{185}}(7 i-6 \underline{j}-10 \underline{k})
$$

Now $\quad|\underline{a}|=\sqrt{(4)^{2}+(3)^{2}+(1)^{2}}=\sqrt{26}$

$$
|\underline{b}|=\sqrt{(2)^{2}+(-1)^{2}+(2)^{2}}=3
$$

If $\theta$ is the angle between $\underline{a}$ and $\underline{b}$, then $|\underline{a} \times \underline{b}|=|\underline{a}||\underline{b}| \sin \theta$

$$
\Rightarrow \quad \sin \theta=\frac{\underline{a} \times \underline{b}}{|\underline{a} \times \underline{b}|}=\frac{\sqrt{185}}{3 \sqrt{26}}
$$

Example 3: Prove that $\sin (\alpha+\beta)=\sin \alpha \cos \beta+\cos \alpha \sin \beta$
Proof: Let $\overrightarrow{O A}$ and $\overrightarrow{O B}$ be unit vectors in the $x y$-plane making angles $\alpha$ and $-\beta$ with the positive $x$-axis respectively

$$
\begin{aligned}
& \text { So that } \angle A O B=\alpha+\beta \\
& \text { Now } \overrightarrow{O A}=\cos \alpha i+\sin \alpha j \\
& \text { and } \overrightarrow{O B}=\cos (-\beta) i+\sin (-\beta) \underline{j} \\
& =\cos \beta i-\sin \beta j \\
& \therefore \overrightarrow{O B} \times \overrightarrow{O A}=(\cos \beta i-\sin \beta j) \times(\cos \alpha i+\sin \alpha j) \\
& \Rightarrow \quad|\overrightarrow{O B}| \overrightarrow{O A}|\sin (\alpha+\beta) \underline{k}=\left|\begin{array}{ccc}
\underline{i} & \underline{j} & \underline{k} \\
\cos \beta & -\sin \beta & 0 \\
\cos \alpha & \sin \alpha & 0
\end{array}\right| \\
& \Rightarrow \quad \sin (\alpha+\beta) \underline{k}=(\sin \alpha \cos \beta+\cos \alpha \sin \beta) \underline{k} \\
& \therefore \quad \sin (\alpha+\beta)=\sin \alpha \cos \beta+\cos \alpha \sin \beta
\end{aligned}
$$

Example 4: In any triangle $A B C$, prove that

$$
\frac{a}{\sin A}=\frac{b}{\sin B}=\frac{c}{\sin C} \quad \text { (Law of Sines) }
$$

Proof: Suppose vectors $\underline{a}, \underline{b}$ and $\underline{c}$ are along the sides $B C, C A$ and $A B$ respectively of the triangle $A B C$.

$$
\begin{aligned}
& \therefore \quad \underline{a}+\underline{b}+\underline{c}=0 \\
& \Rightarrow \quad \underline{b}+\underline{c}=-\underline{a} \\
& \text { Take cross product with } \underline{c} \\
& \underline{b} \times \underline{c}+\underline{c} \times \underline{c}=-\underline{a} \times \underline{c} \\
& \underline{b} \times \underline{c}=\underline{c} \times \underline{a} \quad(\therefore \underline{c} \times \underline{c}=0) \\
& \Rightarrow \quad|\underline{b} \times \underline{c}|=|\underline{c} \times \underline{a}| \\
& |\underline{b}||\underline{c}| \sin (\pi-A)=-|\underline{c}||\underline{a}| \sin (\pi \quad B) \\
& \Rightarrow \quad b c \sin A=a \sin B \Rightarrow b \sin A=a \sin B \\
& \therefore \quad \frac{a}{\sin A}=\frac{b}{\sin B}
\end{aligned}
$$

similarly by taking cross product of (i) with $\underline{b}$, we have

$$
\frac{a}{\sin A}=\frac{c}{\sin C}
$$

From (ii) and (iii), we get

$$
\frac{a}{\sin A}=\frac{b}{\sin B}=\frac{c}{\sin C}
$$

### 7.4.5 Area of Parallelogram

If $\underline{u}$ and $\underline{v}$ are two non-zero vectors and $\theta$ is the angle between $\underline{u}$ and $\underline{v}$, then $|\underline{u}|$ and $|\underline{v}|$ represent the lengths of the adjacent sides of a parallelogram, (see figure)
We know that:
Area of parallelogram $=$ base $x$ height

$$
\begin{aligned}
& =(\text { base })(h)=|\underline{u}||\underline{v}| \sin \theta \\
& \therefore \text { Area of parallelogram }=|\underline{u} \times \underline{v}|
\end{aligned}
$$

### 7.4.6 Area of Triangle

From figure it is clear that
Area of triangle $=\frac{1}{2}$ (Area of parallelogram)
$\therefore \quad$ Area of triangle $=\frac{1}{2}|\underline{u} \quad \underline{v}|$
where $\underline{u}$ and $\underline{v}$ are vectors along two adjacent sides of the triangle.
Example 5: Find the area of the triangle with vertices $A(1,-1,1), B(2,1,-1)$ and $C(-1,1,2)$
Also find a unit vector perpendicular to the plane $A B C$.
Solution: $\overline{A B}=(2-1)(+(1+1) \underline{j}+(-1-1) \underline{k}=\underline{1}+2 \underline{j}-2 \underline{k}$

$$
\overline{A C}=(-1-1) \underline{(}+(1+1) \underline{j}+(2-1) \underline{k}=-2 \underline{1}+2 \underline{j}+\underline{k}
$$

$$
\text { Now } \quad \overline{A B} \times \overline{A C}=\left|\begin{array}{ccc}
\underline{j} & \underline{k} & \underline{k} \\
1 & 2 & -2 \\
-2 & 2 & 1
\end{array}\right|=(2+4) \underline{j}-(1-4) \underline{j}+(2+4) \underline{k}=6 \underline{1}+3 \underline{j}+6 \underline{k}
$$

The area of the parallelogram with adjacent sides $\overline{A B}$ and $\overline{A C}$ is given by

$$
|\overline{A B} \times \overline{A C}|=|6 \underline{1}+3 \underline{j}+6 \underline{k}|=\sqrt{36+9+36}=\sqrt{81}=9
$$

$\therefore \quad$ Area of triangle $=\frac{1}{2}|\overline{A B} \times \overline{A C}|=\frac{1}{2}|6 \underline{1}+3 \underline{j}+6 \underline{k}|=\frac{9}{2}$
A unit vector $\perp$ to the plane $A B C=\frac{\overline{A B} \times \overline{A C}}{|\overline{A B} \times \overline{A C}|}=\frac{1}{9}(6 \underline{1}+3 \underline{j}+6 \underline{k})=\frac{1}{3}(2 \underline{1}+\underline{j}+2 \underline{k})$

Example 6: Find area of the parallelogram whose vertices are $P(0,0,0), Q(-1,2,4)$, $R(2,-1,4)$ and $S(1,1,8)$.

Solution: Area of parallelogram $=|\underline{u} \times \underline{v}|$
where $\underline{u}$ and $\underline{v}$ are two adjacent sides of the parallelogram

$$
\begin{aligned}
& \overline{P Q}=(-1-0) \underline{(}+(-2-0) \underline{j}+(4-0) \underline{k}=-1+2 \underline{j}+4 \underline{k} \\
& \text { and } \quad \overline{P R}=(2-0) \underline{(}+(-1-0) \underline{j}+(4-0) \underline{k}=2 \underline{j}-\underline{j}+4 \underline{k}
\end{aligned}
$$

Now $\quad \overline{P Q} \times \overline{P R}=\left|\begin{array}{ccc}\underline{i} & \underline{j} & \underline{k} \\ -1 & 2 & 4 \\ 2 & -1 & 4\end{array}\right|=(8+4) \underline{j}-(-4-8) \underline{j}+(1-4) \underline{k}$
$\therefore$ Area of parallelogram $=|\overline{P Q} \times \overline{P R}|=|12 \underline{j}+12 \underline{j}-3 \underline{k}|$

$$
\begin{aligned}
& =\sqrt{144+144+9} \\
& =\sqrt{297}
\end{aligned}
$$

## Be careful:

Not all pairs of vertices give a side e.g. $\overline{P S}$ is not a side, it is diagonal since $\overline{P Q}+\overline{P R}=\overline{P S}$

Example7: If $\underline{u}=2 \underline{i}-\underline{j}+\underline{k}$ and $\underline{v}=4 \underline{i}+2 \underline{j}-\underline{k}$, find by determinant formula
(i) $\quad \underline{u} \times \underline{u}$
(ii) $\quad \underline{u} \times \underline{v}$
(iii) $\underline{v} \times \underline{u}$

Solution: $\underline{u}=2 \underline{i}-\underline{j}+\underline{k}$ and $\underline{v}=4 \underline{i}+2 \underline{j}-\underline{k}$ By determinant formula
(i) $\underline{u} \times \underline{u}=\left|\begin{array}{ccc}\underline{i} & \underline{j} & \underline{k} \\ 2= & -\underline{1} & 1 \\ 2 & -1 & 1\end{array}\right| \quad 0 \quad$ ( Two rows are same)
(ii) $\underline{u} \times \underline{v}=\left|\begin{array}{ccc}\underline{i} & \underline{j} & \underline{k} \\ 2 & -1 & 1 \\ 4 & 2 & -1\end{array}\right| \quad \begin{aligned} & -(1-2) \underline{i}-(-2-4) \underline{j}+(4+4) \underline{k}=\underline{i}+6 \underline{j}+8 \underline{k} \\ & \text { (iii) } \quad \underline{v} \times \underline{u}=\left|\begin{array}{ccc}\underline{i} & \underline{j} & \underline{k} \\ 4 & 2 & -1\end{array}\right|=(2-1)(-(4+2) \underline{j}+(-4-4) \underline{k}=\underline{i}-6 \underline{j}-8 \underline{k}$

## EXERCISE 7.4

1. Compute the cross product $a \times b$ and $b \times a$. Check your answer by showing that each $a$ and $b$ is perpendicular to $a \times b$ and $b \times a$.
(i) $\underline{a}=2 \underline{i}+\underline{j}-\underline{k}, \quad \underline{b}=\underline{i}-\underline{j}+\underline{k}$
(ii) $\underline{a}=\underline{i}-\underline{j}=\underline{b} \quad \underline{i} \quad \underline{j}$
(iii) $\underline{a}=3 \underline{i}-2 \underline{j}+\underline{k}, \quad \underline{b}=\underline{i}+\underline{j}$
(iv) $\underline{a}=-4 \underline{i}+\underline{j}-2 \underline{k}, \quad \underline{b}=2 \underline{i}+\underline{j}+\underline{k}$
2. Find a unit vector perpendicular to the plane containing $a$ and $b$. Also find sine of the angle between them.
(i) $\underline{a}=2 \underline{i}-6 \underline{j}-3 \underline{k}, \quad \underline{b}=-4 \underline{i}+3 \underline{j}-\underline{k}$
(ii) $\underline{a}=-i-\underline{j}-\underline{k}, \quad \underline{b}=2 \underline{i}-3 \underline{j}+4 \underline{k}$
(iii) $\underline{a}=2 \underline{i}-2 \underline{j}+4 \underline{k}, \quad \underline{b}=-i+\underline{j}-2 \underline{k}$
(iv) $\underline{a}=\underline{i}-\underline{j}=\underline{b} \quad \underline{i} \quad \underline{j}$
3. Find the area of the triangle, determined by the point $P, Q$ and $R$.
(i) $P(0,0,0) ; Q(2,3,2) ; R(-1,1,4)$
(ii) $P(1,-1,-1) ; Q(2,0,-1) ; R(0,2,1)$
4. find the area of parallelogram, whose vertices are:
(i) $A(0,0,0) ; B(1,2,3) ; C(2,-1,1) ; D(3,1,4)$
(ii) $A(1,2,-1) ; B(4,2,-3) ; C(6,-5,2) ; D(9,-5,0)$
(iii) $A(-1,1,1) ; B(-1,2,2) ; C(-3,4,-5) ; D(-3,5,-4)$
5. Which vectors, if any, are perpendicular or parallel
(i) $\underline{u}=5 \underline{i}-\underline{j}+\underline{k} ; \underline{v}=\underline{j}-5 \underline{k} ; \underline{w}=-15 \underline{i}+3 \underline{j}-3 \underline{k}$
(ii) $\underline{u}=\underline{i}+2 \underline{j}-\underline{k} ; \underline{v}=-i+\underline{j}+\underline{k} ; \underline{w}=-\frac{\pi}{2} \underline{i}-\pi \underline{j}+\frac{\pi}{2} \underline{k}$
6. Prove that: $\quad a \times(b+c)+b \times(c+a)+c \times(a+b)=0$
7. If $a+b+c=0$, then prove that $a \times b=b \times c=c \times a$
8. Prove that: $\sin (\alpha-\beta)=\sin \alpha \cos \beta+\cos \alpha \sin \beta$.
9. If $a \times b=0$ and $a \cdot b=0$, what conclusion can be drawn about $a$ or $b$ ?

### 7.5 SCALAR TRIPLE PRODUCT OF VECTORS

There are two types of triple product of vectors:
(a) Scalar Triple Product: $(\underline{u} \times \underline{v}) \cdot \underline{w}$ or $\underline{u} \cdot(\underline{v} \times \underline{w})$
(b) Vector Triple product: $\underline{u} \times(\underline{v} \times \underline{w})$

In this section we shall study the scalar triple product only

## Definition

Let $\underline{u}=a_{1} \underline{i}+b_{1} \underline{j}+c_{1} \underline{k}, \underline{v}=a_{2} \underline{i}+b_{2} \underline{j}+c_{2} \underline{k}$ and $\underline{w}=a_{3} \underline{i}+b_{3} \underline{j}+c_{3} \underline{k}$ be three vectors
The scalar triple product of vectors $\underline{u}, \underline{v}$ and $\underline{w}$ is defined by $\underline{u} \cdot(\underline{v} \times \underline{w})$ or $\underline{v} \cdot(\underline{w} \times \underline{u})$ or $\underline{w} \cdot(\underline{u} \times \underline{v})$
The scalar triple product $\underline{u} \cdot(\underline{v} \times \underline{w})$ is written as $\underline{u} \cdot(\underline{v} \times \underline{w})=[\underline{u} \times \underline{w}]$

### 7.5.1 Analytical Expression of $\underline{u} \cdot(\underline{v} \times \underline{w})$

Let $\quad \underline{u}=a_{1} \underline{i}+b_{1} \underline{j}+c_{1} \underline{k}, \underline{v}=a_{2} \underline{i}+b_{2} \underline{j}+c_{2} \underline{k}$ and $\underline{w}=a_{3} \underline{i}+b_{3} \underline{j}+c_{3} \underline{k}$
Now $\quad \underline{v} \times \underline{w}=\left|\begin{array}{ccc}\underline{i} & \underline{j} & \underline{k} \\ a_{2} & b_{2} & c_{2} \\ a_{3} & b_{3} & c_{3}\end{array}\right|$

$$
\begin{aligned}
& \Rightarrow \quad \gamma \times \psi=\left(b_{1} c_{1}-b_{1} c_{2}\right) \xi-\left(a_{1} c_{1}-a_{1} c_{2}\right) \int+\left(a_{1} b_{1}-a_{1} b_{2}\right) \xi \\
& \therefore \quad \underline{u}_{1}(\gamma \times \psi)=a_{1}\left(b_{1} c_{1}-b_{1} c_{2}\right)-b_{1}\left(a_{1} c_{1}-a_{1} c_{2}\right)+c_{1}\left(a_{1} b_{1}-a_{1} b_{2}\right) \\
& \Rightarrow \quad \underline{u}_{1}(\gamma \times \psi)=\left|\begin{array}{ccc}
a_{1} & b_{1} & c_{1} \\
a_{2} & b_{2} & c_{2} \\
a_{1} & b_{1} & c_{1}
\end{array}\right| \\
& \text { which is called the determinant formula for scalar triple product of } u, \gamma \text { and } \psi \text { in } \\
& \text { component form. }
\end{aligned}
$$

$$
\begin{aligned}
& \text { Now } \quad \underline{u}_{1}(\gamma \times \psi)=\left|\begin{array}{ccc}
a_{1} & b_{1} & c_{1} \\
a_{2} & b_{2} & c_{2} \\
a_{3} & b_{3} & c_{3}
\end{array}\right| \\
& =-\left|\begin{array}{ccc}
a_{1} & b_{1} & c_{1} \\
a_{2} & b_{2} & c_{2} \\
a_{1} & b_{1} & c_{1}
\end{array}\right| \text { Interchanging } R_{1} \text { and } R_{2} \\
& =\left|\begin{array}{lll}
a_{2} & b_{2} & c_{2} \\
a_{3} & b_{3} & c_{3}
\end{array}\right| \text { Interchanging } R_{1} \text { and } R_{3} \\
& =\left|\begin{array}{lll}
a_{1} & b_{1} & c_{1}
\end{array}\right| \text { Interchanging } R_{2} \text { and } R_{3} \\
& \text { a } \\
& \text { a } \\
& \text { ㄴ } \quad \underline{v}_{1}(\gamma \times \psi)=\underline{v}_{1}(\gamma \times \psi) \\
& \text { Now } \quad \underline{v}_{1}(\gamma \times \psi)=\left|\begin{array}{ccc}
a_{2} & b_{2} & c_{2} \\
a_{3} & b_{3} & c_{3} \\
a_{1} & b_{1} & c_{1}
\end{array}\right| \\
& =-\left|\begin{array}{lll}
a_{3} & b_{3} & c_{3} \\
a_{2} & b_{2} & c_{2}
\end{array}\right| \text { Interchanging } R_{1} \text { and } R_{2} \\
& \text { a } \\
& \text { a } \\
& \text { ㄴ } \\
& \text { ㄴ }
\end{aligned}
$$

$$
\therefore \quad \underline{v}_{1}(\gamma \times \psi)=\underline{v}_{1}(\gamma \times \psi)
$$

Hence

$$
\underline{u}_{1}(\gamma \times \psi)=\underline{v}_{1}(\gamma \times \psi)=\underline{v}_{1}(\gamma \times \gamma)
$$

Note: (i) The value of the triple scalar product depends upon the cycle order of the vectors, but is independent of the position of the dot and cross. So the dot and cross, may be interchanged without altering the value i.e;

$$
\begin{aligned}
& (\underline{u} \times \gamma) \cdot \underline{w}=\underline{w} \cdot(\gamma \times \psi)=[\underline{u} \gamma \cdot \psi] \\
& (\gamma \times \psi) \cdot \underline{w}=\underline{v} \cdot(\psi \times \psi)=[\gamma \cdot \psi \cdot \psi] \\
& (\psi \times \psi) \cdot \gamma=\psi \cdot(\psi \times \gamma)=[\psi \cdot \psi \cdot \gamma] \\
& \text { (iii) The value of the product changes if the order is non-cyclic. } \\
& \text { (iv) } \quad \underline{u}, \gamma, \psi \text { and } \underline{u} \times(\gamma, \psi) \text { are meaningless. }
\end{aligned}
$$

### 7.5.2 The Volume of the Parallelepiped

The triple scalar product $(u \times \gamma) \cdot \psi$ represents the volume of the parallelepiped having $u, \gamma$ and $\psi$ as its conterminous edges.

As it is seen from the formula that:

$$
(\underline{u} \times \gamma) \cdot \underline{w}=[\underline{u} \times \gamma][\underline{w}] \cos \theta
$$

Hence (i) $|\underline{u} \times \gamma|=$ area of the parallelogram with two adjacent sides, $u$ and $\gamma$.
(ii) $|\underline{w}| \cos \theta=$ height of the parallelepiped

$$
(\underline{u} \times \gamma) \cdot \underline{w}=[\underline{u} \times \gamma][\underline{w}] \cos \theta=(\text { Area of parallelogram })(\text { height })
$$

$$
=\text { Volume of the parallelepiped }
$$

Similarly, by taking the base plane formed by $\gamma$ and $\psi$, we have
The volume of the parallelepiped $=(\gamma \times \psi) \cdot u$
And by taking the base plane formed by $\psi$ and $u$, we have
The volume of the parallelepiped $=(\psi \times u) \cdot \gamma$
So, we have: $(u \times \gamma) \cdot \psi=(\gamma \times \psi) \cdot u=(\psi \times u) \cdot \gamma$

### 7.5.3 The Volume of the Tetrahedron:

Volume of the tetrahedron $A B C D$

$$
=\frac{1}{3}(\Delta A B C)(\text { height of } D \text { above the place } A B C)
$$

$=|\underline{w} \times \underline{v}|$
(iii) The value of the product changes if the order is non-cyclic.
(iv) $\quad \underline{u}, \gamma, \psi$ and $\underline{u} \times(\gamma, \psi)$ are meaningless.

$$
\begin{aligned}
& =\frac{1}{3} \frac{1}{2}|\underline{u} \times \underline{v}|(h) \\
& =\frac{1}{6}(\text { Area of parallelogram with } A B \text { and } A C \text { as adjacent sides })(\mathrm{h}) \\
& =\frac{1}{6}(\text { Volume of the parallelepiped with } \underline{u}, \underline{v}, \underline{w} \text { as edges })
\end{aligned}
$$

Thus Volume $=\frac{1}{6}(\underline{u} \times \underline{v}) \cdot \underline{w}=\frac{1}{6}[\underline{u} \underline{v} \underline{w}]$

## Properties of triple scalar Product:

1. If $\underline{u}, \underline{v}$ and $\underline{w}$ are coplanar, then the volume of the parallelepiped so formed is zero i.e; the vectors $\underline{u}, \underline{v}, \underline{w}$ are coplanar $\Leftrightarrow(\underline{u} \times \underline{v}) \cdot \underline{w}=0$
2. If any two vectors of triple scalar product are equal, then its value is zero i.e;

$$
[\underline{u} \underline{u} \underline{w}]=[\underline{u} \underline{v} \underline{v}]=0
$$

Example 1: Find the volume of the parallelepiped determined by

$$
\underline{u}=(+2 \underline{j}-\underline{k}, \underline{v}=\underline{j}-\underline{j}+3 \underline{k}, \underline{w}=\underline{j}-7 \underline{j}-4 \underline{k}
$$

Solution: Volume of the parallelepiped $=\underline{u} \cdot \underline{v} \times \underline{w}=\left|\begin{array}{ccc}1 & 2 & -1 \\ 1 & -2 & 3 \\ 1 & -7 & -4\end{array}\right|$

$$
\begin{aligned}
\Rightarrow \quad \text { Volume } & =1(8+21)-2(-4-3)-1(-7+2) \\
& =29+14+5=48
\end{aligned}
$$

Example 2: Prove that four points $A(-3,5,-4), B(-1,1,1), C(-1,2,2)$ and $D(-3,4,-5)$ are coplaner.

Solution: $\overline{A B}=(-1+3)(\underline{+}(1-5) \underline{j}+(\underline{1}+4) \underline{k}=2 \underline{j}-4 \underline{j}+5 \underline{k}$

$$
\begin{aligned}
& \overline{A C}=(-1+3)(\underline{+}(2-5) \underline{j}+(\underline{2}+4) \underline{k}=2 \underline{j}-3 \underline{j}+6 \underline{k} \\
& \overline{A D}=(3-3)(\underline{+}(4-5) \underline{j}+(-5+4) \underline{k}=0 \underline{j}-\underline{k}=-\underline{j}-\underline{k}
\end{aligned}
$$

Volume of the parallelepiped formed by $\overline{A B}, \overline{A C}$ and $\overline{A D}$ is

$$
\begin{aligned}
& {[\overline{A B} \overline{A C} \overline{A D}]=\left|\begin{array}{ccc}
2 & -4 & 5 \\
2 & -3 & 6 \\
0 & -1 & -1
\end{array}\right|=2(3+6)+4(-2-0)+5(-2-0)} \\
& =18-8-10=0
\end{aligned}
$$

As the volume is zero, so the points $A, B, C$ and $D$ are coplaner.
Example 3: Find the volume of the tetrahedron whose vertices are $A(2,1,8), B(3,2,9), C(2,1,4)$ and $D(3,3,0)$
Solution: $\overline{A B}=(3-2)(\underline{+}(2-1) \underline{j}+(\underline{9}-8) \underline{k}=\underline{j}+\underline{k}$

$$
\begin{aligned}
& \overline{A C}=(2-2)(\underline{+}(1-1) \underline{j}+(\underline{4}-8) \underline{k}=0 \underline{j}-0 \underline{j}-4 \underline{k} \\
& \overline{A D}=(3-2)(\underline{+}(3-1) \underline{j}+(\underline{0}-8) \underline{k}=\underline{j}+2 \underline{j}-8 \underline{k} \\
& \therefore \quad \text { Volume of the tetrahedron }=\frac{1}{6}\left[\overline{A B} \overline{A C} \overline{A D}\right] \\
& =\frac{1}{6}\left|\begin{array}{ccc}
1 & 1 & 1 \\
0 & 0 & -4 \\
1 & 2 & -8
\end{array}\right|=\frac{1}{6}[4(2-1)]-\frac{4}{6}-\frac{2}{3}
\end{aligned}
$$

Example 4: Find the value of $\alpha$, so that $\alpha(\underline{+} \underline{j}, \underline{j}+\underline{j}+3 \underline{k}$ and $2 \underline{j}+\underline{j}-2 \underline{k}$ are coplaner.
Solution: Let $\underline{u}=\alpha(\underline{+} \underline{j}, \underline{v}=\underline{j}+\underline{j}+3 \underline{k}$ and $\underline{w}=2 \underline{j}+\underline{j}-2 \underline{k}$
Triple scalar product

$$
\begin{aligned}
& {[\underline{u} \underline{v} \underline{w}]=\left|\begin{array}{ll}
\alpha & 1 \\
1 & 1
\end{array}\right|=\alpha(-2-3)-1(-2-6)+0(1-2)} \\
& \left|\begin{array}{ll}
2 & 1 \\
2 & 1
\end{array}\right|=\frac{1}{2}
\end{aligned}
$$

$$
=-5 \alpha+8
$$

The vectors will be coplaner if $-5 \alpha+8=0 \Rightarrow \alpha=\frac{8}{5}$

Example 5: Prove that the points whose position vectors are $A(-6 i+3 j+2 k)$, $B(3 i-2 j+4 k), C(5 i+7 j+3 k), D(-13 i+17 j-k)$ are coplaner.
Solution: Let $O$ be the origin.

$$
\begin{aligned}
& \therefore \quad \overrightarrow{O A}=-6 i+3 j+2 k ; \overrightarrow{O B}=3 i-2 j+4 k \\
& \therefore \quad \overrightarrow{O C}=5 i+7 j+3 k ; \quad \overrightarrow{O D} \Rightarrow 13 i-17 j \quad k \\
& \therefore \quad \overrightarrow{A B}=\overrightarrow{O B}-\overrightarrow{O A}=(3 i-2 j+4 k)-(-6 i+3 j+2 k) \\
& \therefore \quad=9 i-5 j+2 k \\
& \begin{aligned}
\overrightarrow{A C} & =\overrightarrow{O C}-\overrightarrow{O A}=(5 i+7 j+3 k)-(-6 i+3 j+2 k) \\
& =11 i+4 j+k
\end{aligned} \\
& \begin{aligned}
\overrightarrow{A D} & =\overrightarrow{O D}-\overrightarrow{O A}=(-13 i+17 j-k)-(-6 i+3 j+2 k) \\
& \therefore \quad=-7 i+14 j-3 k
\end{aligned}
\end{aligned}
$$

Now $\quad \overrightarrow{A B} .(\overrightarrow{A C} \times \overrightarrow{A D})=\left|\begin{array}{ccc}9 & -5 & 2 \\ 11 & 4 & 1 \\ -7 & 14 & -3\end{array}\right|$

$$
\begin{aligned}
& =9(-12-14)+5(-33+7)+2(154+28) \\
& =2341303640
\end{aligned}
$$

$\therefore \overrightarrow{A B}, \overrightarrow{A C}, \overrightarrow{A D}$ are coplaner
$\Rightarrow$ The points $A, B, C$ and $D$ are coplaner.

### 7.5.4 Application of Vectors in Physics and Engineering

## (a) Work done.

If a constant force $E$, applied to a body, acts at an angle $\theta$ to the direction of motion, then the work done by $E$ is defined to be the product of the component of $E$ in the direction of the displacement and the distance that the body moves.
In figure, a constant force $E$ acting on a body, displaces it from $A$ to $B$.
$\therefore \quad$ Work done $=$ (component of $E$ along $A B$ ) (displacement)

$$
=4 F \cos \theta)(A B) \quad E \cdot \overrightarrow{A B}
$$

Example 6: Find the work done by a constant force $E=2 i+4 j$, if its points of application to a body moves it from $A(1,1)$ to $B(4,6)$.
(Assume that $|E|$ is measured in Newton and $|d|$ in meters.)

Solution: The constant force $E=2 i+4 j$,
The displacement of the body $=d=\overrightarrow{A B}$

$$
=(4-1) i+(6-1) j=3 i+5 j
$$

$\therefore \quad$ work done $=E \cdot d$

$$
\begin{aligned}
& \left.\left.\left.\left.\left.+2 i \begin{array}{ll}
4 j
\end{array}\right) \in(3 i \quad 5 j\right) \\
& =(2)(3)+(4)(5)=26 \text { nt. } m
\end{array}\right\rvert\,\right.
\end{aligned}
$$

Example 7: The constant forces $2 i+5 j+6 k$ and $-i+2 j+k$ act on a body, which is displaced from position $P(4,-3,-2)$ to $Q(6,1,-3)$. Find the total work done.

Solution: Total force $=(2 i+5 j+6 k)+(-i+2 j+k)$

$$
\Rightarrow \quad \underline{E}=i+3 j+5 k
$$

The displacement of the body $=\overrightarrow{P Q}=(6-4) i+(1+3) j+(-3+2) k$
$\Rightarrow \quad \underline{d}=2 i+4 j-k$
$\therefore \quad$ work done $=E \cdot d$

$$
\begin{aligned}
& =(i+3 j+5 k) \cdot(2 i+4 j-k) \\
& =2+12-5=9 \text { nt. } m
\end{aligned}
$$

(b) Moment of Force

Let a force $\underline{F}(\overline{P Q})$ act at a point $P$ as shown in the figure, then moment of $\underline{F}$ about 0 .

$$
\begin{aligned}
& =\text { product of force } \underline{F} \text { and perpendicular ON. } \underline{\hat{\sigma}} \\
& =\underline{\hat{O} P} \underline{\hat{P}} \underline{\hat{Q}}=\underline{\tau} \times \underline{F}
\end{aligned}
$$

Example 8: Find the moment about the point $M(-2,4,-6)$ of the force represented by $\overrightarrow{A B}$, where coordinates of points $A$ and $B$ are $(1,2,-3)$ and $(3,-4,2)$ respectively.

Solution: $\quad \overrightarrow{A B}=(3-1)(\div(-4-2) \underline{j}+(2+3) \underline{k}=2(-6 \underline{j}+5 \underline{k}$

$$
\overrightarrow{M A}=(1+2)(\div(2-4) \underline{j}+(-3+6) \underline{k}=3(-2 \underline{j}+3 \underline{k}
$$

Moment of $\overrightarrow{A B}$ about $(-2,4,-6)=\underline{\tau} \times \underline{F}=\overrightarrow{M A} \times \overrightarrow{A B}$

$$
\begin{aligned}
& =\left|\begin{array}{ccc}
\underline{j} & \underline{k} \\
3 & -2 & 3 \\
2 & -6 & 5
\end{array}\right| \\
& =(-10+18) \underline{(}-(15-6) \underline{j}+(-18+4) \underline{k} \\
& =8(-9 \underline{j}-14 \underline{k}
\end{aligned}
$$

Magnitude of the moment $=\sqrt{(8)^{2}+(-9)^{2}+(-14)^{2}}=\sqrt{341}$

## EXERCISE 7.5

1. Find the volume of the parallelepiped for which the given vectors are three edges.
(i) $\underline{u}=3 \underline{i}+2 \underline{k} ; \quad \underline{v} \neq \varnothing \underline{j} \neq \underline{k} ; \quad \underline{w}=\underline{j} \neq \underline{k}$
(ii) $\underline{u}=(-4 \underline{j}-\underline{k} ; \quad \underline{v}=\underline{i}-\underline{j}-2 \underline{k} ; \quad \underline{w}=2 \underline{i}-3 \underline{j}+\underline{k}$
(iii) $\underline{u}=(-2 \underline{j}-3 \underline{k} ; \quad \underline{v}=2 \underline{i}-\underline{j}-\underline{k} ; \quad \underline{w}=\underline{j}+\underline{k}$
2. Verify that
$\underline{a} \cdot \underline{b} \times \underline{c}=\underline{b} \cdot \underline{c} \times \underline{a}=\underline{c} \cdot \underline{a} \times \underline{b}$
if $\underline{a}=3 \underline{i}-\underline{j}+5 \underline{k}, \quad \underline{b}=4 \underline{i}+3 \underline{j}-2 \underline{k}$, and $\underline{c}=2 \underline{i}+5 \underline{j}+\underline{k}$
3. Prove that the vectors $\underline{i}-2 \underline{j}+3 \underline{k},-2 \underline{i}+3 \underline{j}-4 \underline{k}$ and $\underline{i}-3 \underline{j}+5 \underline{k}$ are coplanar
4. Find the constant $\alpha$ such that the vectors are coplanar.
(i) $\underline{i}-\underline{j}+\underline{k}, \quad \underline{i}-2 \underline{j}-3 \underline{k}$ and $3 \underline{i}-\alpha \underline{j}+5 \underline{k}$.
(ii) $\underline{i}-2 \alpha \underline{j}-\underline{k}, \quad \underline{i}-\underline{j}+2 \underline{k}$ and $\alpha \underline{i}-\underline{j}+\underline{k}$
5. (a) Find the value of:
(i) $2 \underline{i} \times 2 \underline{j} \underline{k}$
(ii) $3 \underline{j} \underline{k} \times \underline{i}$
(iii) $[\underline{k}(\underline{j}]$
(iv) $[(i k]$
(b) Prove that $\underline{u}(\underline{v} \times \underline{w})+\underline{v}(\underline{w} \times \underline{u})+\underline{w}(\underline{u} \times \underline{v})=3 \underline{u}(\underline{v} \times \underline{w})$
6. Find volume of the Tetrahedron with the vertices
(i) $(0,1,2), \quad(3,2,1), \quad(1,2,1)$ and $(5,5,6)$
(ii) $(2,1,8), \quad(3,2,9), \quad(2,1,4)$ and $(3,3,10)$.
7. Find the work done, if the point at which the constant force $\underline{F}=4 \underline{i}+3 \underline{j}+5 \underline{k}$ is applied to an object, moves from $P,(3,1,-2)$ to $P,(2,4,6)$.
8. A particle, acted by constant forces $4 \underline{i}+\underline{j}-3 \underline{k}$ and $3 \underline{i}-\underline{j}-\underline{k}$, is displaced from $A(1,2,3)$ to $B(5,4,1)$. Find the work done.
9. A particle is displaced from the point $A(5,-5,-7)$ to the point $B(6,2,-2)$ under the action of constant forces defined by $10 \underline{i}-\underline{j}+11 \underline{k}, 4 \underline{i}+5 \underline{j}+9 \underline{k}$ and $-2 \underline{i}+\underline{j}-9 \underline{k}$. Show that the total work done by the forces is 102 units.
10. A force of magnitude 6 units acting parallel to $2 \underline{i}-2 \underline{j}+\underline{k}$ displaces, the point of application from $(1,2,3)$ to $(5,3,7)$. Find the work done.
11. A force $\underline{F}=3 \underline{i}+2 \underline{j}-4 \underline{k}$ is applied at the point $(1,-1,2)$. Find the moment of the force about the point $(2,-1,3)$.
12. A force $\underline{F}=4 \underline{i}-3 \underline{k}$, passes through the point $A(2,-2,5)$. Find the moment of $\underline{F}$ about the point $B(1,-3,1)$.
13. Give a force $\underline{F}=2 \underline{i}+\underline{j}-3 \underline{k}$ acting at a point $A(1,-2,1)$. Find the moment of $\underline{F}$ about the point $B(2,0,-2)$.
14. Find the moment about $A(1,1,1)$ of each of the concurrent forces $\underline{i}-2 \underline{j}, 3 \underline{i}+2 \underline{j}-\underline{k}$, $5 \underline{j}+2 \underline{k}$, where $P(2,0,1)$ is their point of concurrency.
15. A force $\underline{F}=7 \underline{i}+4 \underline{j}-3 \underline{k}$ is applied at $P(1,-2,3)$. Find its moment about the point $Q(2,1,1)$.