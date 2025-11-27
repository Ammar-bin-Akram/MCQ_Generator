# Chapter 2: Functions and Graphs

## INTRODUCTION

Functions are of fundamental importance in mathematics, describing relationships between inputs and outputs through a rule of correspondence. Understanding key concepts such as domain, co-domain and range is essential for analyzing different types of functions, including one-to-one, onto and bijective functions. Graphical representation helps in identifying intersecting points, such as where a linear function meets the coordinate axes, where two linear functions intersect or where a linear and a quadratic function cross. These intersections provide valuable insights into solving equations visually. Additionally, exploring square root and cube root function graphs allows for a deeper understanding of their unique properties and behaviour. This unit will enhance problem-solving skills by combining algebraic and graphical approaches to functions.

### 2.1 Concept of Function

The term function was recognized by a German Mathematician Leibniz (1646-1716) to describe the dependence of one quantity on another. The following examples illustrate how this term is used:
(i) The area $A$ of a square depends on one of its sides $x$ by the formula $A=x^{2}$, so we say that $A$ is a function of $x$.
(ii) The volume " $V$ " of a sphere depends on its radius $r$ by the formula $V=\frac{4}{3} \pi r^{3}$, so we say that $V$ is a function of $r$.
A function is a rule of correspondence, relating two sets in such a way that each element in the first set corresponds to one and only one element in the second set.
Thus in, (i) above, a square of a given side has only one area and in, (ii) above, a sphere of a given radius has only one volume.
Now we have a formal definition:

### 2.1.1 Definition (Function, Domain, Codomain, Range)

A function $f$ from a set $X$ to a set $Y$ is a rule of a correspondence that assigns to each element $x$ in $X$ a unique element $y$ in $Y$. The set $X$ is called the domain of $f$.
The set of corresponding elements $y$ in $Y$ is called the range of $f$. While the codomain of a function is the set $Y$ in which function's output values (range) lie.
Unless stated to the contrary, we shall assume hereafter that the set $X$ and $Y$ consist of real numbers.

Note Co-domain is the set of all possible outputs but the range is the actual set of outputs produced by the function under the given domain that is range set is always a subset of co-domain.

# 2.1.2 Notation and Value of a Function

If a variable $y$ depends on a variable $x$ in such a way that each value of $x$ determines exactly one value of $y$, then we say that " $y$ is a function of $x$ ".
Swiss mathematician Euler (1707 - 1783) invented a symbolic way to write the statement " $y$ is a function of $x$ " as $y=f(x)$, which is read as " $y$ is equal to $f$ of $x$ ".
A function can be thought as a computing machine $f$ that takes an input $x$, operates on it in some way and produces exactly one output $f(x)$. This output $f(x)$ is called the value of $f$ at $x$ or image of $x$ under $f$.
The output $f(x)$ is denoted by a single letter, say $y$ and we write $y=f(x)$.
The variable $x$ is called the independent variable of $f$ and the variable $y$ is called the dependent variable of $f$. For now onward we shall only consider the function in which the variables are real numbers and we say that $f$ is a real valued function of real numbers.
Example 1 Given $f(x)=x^{3}-2 x^{2}+4 x-1$, find:
(i) $f(0)$
(ii) $f(1)$
(iii) $f(-2)$
(iv) $f(1+x)$
(v) $f\left(\frac{1}{x}\right), x \neq 0$

Solution $f(x)=x^{3}-2 x^{2}+4 x-1$
(i) $f(0)=0-0+0-1=-1$
(ii) $f(1)=(1)^{3}-2(1)^{2}+4(1)-1=1-2+4-1=2$
(iii) $f(-2)=(-2)^{3}-2(-2)^{2}+4(-2)-1=-8-8-8-1=-25$
(iv) $f(1+x)=(1+x)^{3}-2(1+x)^{2}+4(1+x)-1$

$$
\begin{aligned}
& =1+3 x+3 x^{2}+x^{3}-2-4 x-2 x^{2}+4+4 x-1 \\
& =x^{3}+x^{2}+3 x+2
\end{aligned}
$$

(v) $f\left(\frac{1}{x}\right)=\left(\frac{1}{x}\right)^{3}-2\left(\frac{1}{x}\right)^{2}+4\left(\frac{1}{x}\right)-1=\frac{1}{x^{2}}-\frac{2}{x^{2}}+\frac{4}{x}-1, x \neq 0$

Example 2 Find the domain and range of $f(x)=x^{2}$.
Solution For every real number $x, f(x)=x^{2}$ is a non-negative real number. So, Domain $f=$ set of all real numbers ; Range $f=$ set of all non-negative real numbers.

Example 3 Find the domain and range of $f(x)=\frac{x}{x^{2}-4}$.
Solution At $x=2$ and $x=-2, f(x)=\frac{x}{x^{2}-4}$ is not defined. So,
Domain $f=$ set of all real numbers except -2 and 2 or $R-\{-2,2\}$
Let $y=\frac{x}{x^{2}-4} \Rightarrow y\left(x^{2}-4\right)=x \Rightarrow x^{2} y-4 y=x$

$$
\begin{aligned}
x^{2} y-x-4 y & =0 \\
x & =\frac{-(-1) \pm \sqrt{(-1)^{2}-4(y)(-4 y)}}{2 y} \\
x & =\frac{1 \pm \sqrt{1+16 y^{2}}}{2 y}, y \neq 0
\end{aligned}
$$

## Remember

There are two types of intervals known as open interval and closed interval. In an open interval $(a, b)$, the endpoints are not included. In a closed interval $[a, b]$, the endpoints are included.

Clearly $x$ is defined for all $y \neq 0$

$$
\text { For } y=0 \text {, we have } 0=\frac{x}{x^{2}-4} \Rightarrow x=0
$$

This is $f(0)=0$
So, range $f=$ set of all real numbers or $(-\infty, \infty)$
Example 4 Find the domain and range of $f(x)=\sqrt{x^{2}-9}$.
Solution As square root of a negative number is not a real number, therefore $x^{2}-9 \geq 0$
(i)

Let $x^{2}-9=0 \Rightarrow x= \pm 3$
Critical points divide the number line into three regions:
Put $x=-4$ in (i), $16-9 \geq 0$ (True)
Put $x=0$ in (i), $0-9 \geq 0$ (False)
Put $x=4$ in (i), $16-9 \geq 0$ (True)
So, domain $f \doteq(-\infty,-3] \cup[3, \infty)$
The smallest value of $x^{2}-9$ is 0 (when $x= \pm 3$ ).
$\Rightarrow y=\sqrt{x^{2}-9}=\sqrt{0}=0$
As $|x|$ increases beyond $3, x^{2}-9$ grows to $+\infty$, so $y$ grows to $+\infty$.
So, range $f=[0, \infty)$

# 2.1.3 Vertical Line Test

The vertical line test is a method used to determine whether a graph represents a function. A graph represents a function if and only if no vertical line intersects the graph more than once. If any vertical line passes through the graph more than once, it is not a function.

Explanation is given in the following figure.
# 2.1.4 Types of Function

## (i) One-to-One (Injective) Function

A function $f: x \rightarrow y$ is one-to-one if different inputs produce different outputs, that is if $f\left(x_{1}\right)=f\left(x_{2}\right)$ implies $x_{1}=x_{2}$. This means that no two different elements of the domain map to the same element of the co-domain.
For example, $f(x)=5 x+7$ is one-to-one because if $5 x_{1}+7=5 x_{2}+7$ implies $x_{1}=x_{2}$.

## (ii) Onto (Surjective) Function

A function $f: X \rightarrow Y$ is called onto (or surjective) function if every element in the co-domain $Y$ has at least one pre-image in the domain $X$. In other words, for every $y$ in $Y$, there exists an $x$ in $X$ such that $f(x)=y$.
For example, $f(x)=2 x+3$, where the domain and co-domain are both real numbers.
Here $y=2 x+3 \Rightarrow x=\frac{y-3}{2}$. Here for each $y$ in $R$, there exists $\frac{y-3}{2}$ in $R$ such that $f\left(\frac{y-3}{2}\right)=y$. Hence $f$ is an onto function.

## (iii) Bijective Function

A function $f: X \rightarrow Y$ is called bijective if it is both one-to-one and onto.
Piecewise Function
A piecewise function is a function that is defined by different expressions (or "pieces") over different intervals of its domain. Each piece applies to a specific part of the domain.
For example, $\quad f(x)=\left\{\begin{array}{l}2 x+1 \text { if } x<0 \\ x^{2}-1 \text { if } x \geq 0\end{array}\right.$
For $x<0$, the function behaves as $2 x+1$ and for $x \geq 0$, it behaves as $x^{2}-1$
Example 5 Show that the function $f(x)=x+1$, where the domain and co-domain are all real numbers, is bijective.
Solution A function is bijective if it is both one-to-one and onto.
A function is one-to-one if $f\left(x_{1}\right)=f\left(x_{2}\right) \Rightarrow x_{1}=x_{2}$ for $f(x)=x+1$
Suppose $f\left(x_{1}\right)=f\left(x_{2}\right)$

$$
\begin{aligned}
& \Rightarrow \quad x_{1}+1=x_{2}+1 \\
& \Rightarrow \quad x_{1}=x_{2}
\end{aligned}
$$

So, the given function is one-to-one.
It is also onto because for every real number $y$, there is a real number $x$ (specifically $x=y-1$ ) such that $f(y-1)=y-1+1=y$. Hence, $f(x)$ is bijective.
Exemple 6 Show that the function $f(x)=x^{2}-2$, where the domain and co-domain are all real numbers, is neither one-to-one nor onto.
Solution As $f\left(x_{1}\right)=f\left(x_{2}\right) \Rightarrow x_{1}^{2}-2=x_{2}^{2}-2 \Rightarrow x_{1}^{2}=x_{2}^{2}$
Taking square root, we get $x_{1}=x_{2}$ or $x_{1}=-x_{2}$
This does not imply that $x_{1}=x_{2}$, for example $x_{1}=2, x_{2}=-2 \Rightarrow x_{1} \neq x_{2}$ and $f(2)=2=f(-2)$.
Thus, $f$ is not one-to-one.
Also, the element -2 in the co-domain $R$ is the smallest value that $f(x)=x^{2}-2$ can attain, and it is only achieved when $x=0$. However, any number less than -2 (in co-domain $R$ ) is not the image of any real number $x$ in domain $R$. For example, $f(x)=-3 \Rightarrow x^{2}-2=-3$ has no
real root. Hence, $f(x)$ is nether one-to-one nor onto.

# EXERCISE 2.1

1. Given that:
(a) $f(x)=x^{2}-1$
(b) $f(x)=\sqrt{2 x+3}$
Find:
(i) $f(-3)$
(ii) $f(0)$
(iii) $f(x-2)$
(iv) $f\left(x^{2}+3\right)$
2. Find $\frac{f(a+h)-f(a)}{h}$ and simplify where,
(i) $f(x)=4 x+7$
(ii) $f(x)=\sin x$
(iii) $f(x)=x^{3}+x^{2}-1$
(iv) $f(x)=\tan x$

3. Express the following:
(a) The area $A$ of a square as a function of its perimeter $P$.
(b) The circumference $C$ of a circle as a function of its area $A$.
(c) The surface area $S$ of a cube as a function of its volume $V$.
4. Find the domain and the range of the function $g$ defined below:
(i) $g(x)=5-x$
(ii) $g(x)=\sqrt{x+2}$
(iii) $g(x)= \begin{cases}6 x+7, & x \leq-2 \\ 4-3 x, & x>-2\end{cases}$
(iv) $g(x)=|x-5|$
(v) $g(x)=\frac{x+2}{3-x}$
5. Given $f(x)=x^{3}-a x^{2}+b x+1$. If $f(2)=-3$ and $f(-1)=0$. Find the values of $a$ and $b$.
6. A stone falls from a height of 60 m on the ground, the height $h$ after $x$ seconds is approximately given by $h(x)=40-10 x^{2}$.
(i) What is the height of stone when:
(a) $x=1 \mathrm{sec}$ ?
(b) $x=1.5 \mathrm{sec}$ ?
(c) $x=1.7 \mathrm{sec}$ ?
(ii) When does the stone strike the ground?
7. Consider the function $f(x)=3 x-5$.
(i) Determine the domain and range of $f(x)$.
(ii) Is the function $f$ one-to-one? Justify your answer.
(iii) Is the function $f$ onto if the co-domain is all real numbers? Explain.
8. Let $f: R \rightarrow R$ be defined by $f(x)=\frac{2 x-3}{x+1}$.
(i) Find the domain and range of $f(x)$. (ii) Determine whether $f(x)$ is onto.
(iii) Prove that $f(x)$ is one-to-one.
9. Consider the function $f: \mathrm{R}^{+} \rightarrow \mathrm{R}^{+}$defined by $f(x)=e^{-x}$. Show that $f(x)$ is a bijective.
10. Let $g: R \rightarrow R$ be given by $g(x)=x^{3}-3 x$. Determine if $g(x)$ is injective and/or surjective.

# 2.2 Finding the Intersecting Point(s) Graphically

The point of intersection is a point where two or more graphs meet on the coordinate plane. This point represents the solution to the equation of the given function.

### 2.2.1 Intersection of a Linear Function and Coordinate Axes

As we know that linear function is a function in which the highest power of the variable is one. While the coordinate axes refers to $x$-axis and $y$-axis in the Cartesian coordinate system.

Example 7 Find the points of intersection of a linear function $y=2 x+6$ and coordinate axes graphically.
Solution Table of values of $y=2 x+6$ are given below:

| $x$ | $y=2 x+6$ |
| :--: | :--: |
| -1 | 4 |
| 0 | 6 |
| 1 | 8 |

Hence, from the above graph, the points $(-3,0)$ and $(0,6)$ are the points of intersection of $y=2 x+6$ and coordinate axes.

# 2.2.2 Intersection of Two Linear Functions

The point of intersection of two linear functions is the point where their graphs cross each other. This means the two functions have the same $x$ and $y$ values at that point.
Example 8 Find the point of intersection of $y=3 x+2$ and $y=-x+6$ graphically.
Solution Table of different values of $x$ and $y$ is given below:

| $x$ | $y=3 x+2$ | $y=-x+6$ |
| :--: | :--: | :--: |
| -1 | -1 | 7 |
| 0 | 2 | 6 |
| 1 | 5 | 5 |

By plotting the above points, we see that $(1,5)$ is the point of intersection of both the straight lines as shown in figure.
### 2.2.3 Intersection of a Linear Function and a Quadratic Function

A line and a parabola can either intersect at two points, one point or not as intersect at all. If there are two solutions, the system has two points of intersection. A single solution indicates that there is only one intersection point, suggesting that the line may be tangent to the parabola. If no solution exists, it means the line and the

parabola do not intersect.
Example 9 Solve the linear function $y=-x+3$ and quadratic function $y=x^{2}-6 x+3$ graphically.
Solution Clearly $(3,0)$ and $(0,3)$ are the $x$-intercept and $y$-intercept respectively of $y=-x+3$.

$$
y=x^{2}-6 x+3
$$

Put $x=0$ in (i), so $(0,3)$ is the $y$-intercept.
Put $y=0$ in (i), we have

$$
\begin{aligned}
0 & =x^{2}-6 x+3 \\
x & =\frac{-(-6) \pm \sqrt{(-6)^{2}-4(1)(3)}}{2(1)} \\
& =\frac{6 \pm \sqrt{36-12}}{2}=\frac{6 \pm \sqrt{24}}{2} \\
& =\frac{6 \pm 2 \sqrt{6}}{2}=3 \pm \sqrt{6} \\
& =3-\sqrt{6}, 3+\sqrt{6}=0.6,5.4
\end{aligned}
$$

So $(0.6,0)$ and $(5.4,0)$ are the $x$-intercepts.
Now we find vertex $(h, k)$ of the parabola

$$
\begin{aligned}
& h=-\frac{b}{2 a}=-\frac{-6}{2(1)}=3 \\
& k=(3)^{2}-6(3)+3=-6
\end{aligned}
$$

So, the vertex is $(3,-6)$.
Hence $(0,3)$ and $(5,-2)$ are the solutions (points of intersection) of the given functions.

# 2.3 Graph of the Square Root Function

Example 10 Graph the square root function $y=2 \sqrt{x}+1$
Solution Clearly the domain of $y=2 \sqrt{x}+1$ is $x \geq 0$, as the square root of a negative number is not a real number. The range of $y=2 \sqrt{x}+1$ is $y \geq 1$,
Table of values and the graph of the function are given below:

| $\boldsymbol{x}$ | $\boldsymbol{y}=\mathbf{2} \sqrt{\boldsymbol{x}}+\mathbf{1}$ |
| :--: | :--: |
| 0 | 1 |
| 1 | 3 |
| 2 | 3.8 |
| 3 | 4.5 |
| 4 | 5 |
| 5 | 5.5 |
| 6 | 5.9 |
| 7 | 6.3 |
| 8 | 6.7 |
| 9 | 7 |
| 10 | 7.3 |

### 2.4 Graph of the Cube Root Function

Example 11 Graph the cube root function $y=\sqrt[3]{x-1}$
Solution Table of values and the graph of the function are given below:

| $\boldsymbol{x}$ | $\boldsymbol{y}=\sqrt[3]{\boldsymbol{x}-1}$ |
| :--: | :--: |
| -5 | $-1.8$ |
| -4 | $-1.7$ |
| -3 | $-1.6$ |
| -2 | $-1.4$ |
| -1 | $-1.3$ |
| 0 | -1 |
| 1 | 0 |
| 2 | 1 |
| 3 | 1.3 |
| 4 | 1.4 |
| 5 | 1.6 |

# 2.5 Real Life Applications

## Growth and Decay in Finance (Predicting Long-Term Stock Prices)

When something increases in quantity or size over time, it is called growth. For example, money in a bank account earning interest (it grows larger), a population of rabbits is increasing over months.
When something decreases in quantity or size over time, it is called decay. For example, a radioactive substance is losing its strength over years, a cup of hot coffee is cooling down over time.
Example 12 The value of a stock follows the exponential growth model $P(t)=P_{0} e^{r t}$, where $P_{0}$ is the initial stock price, $r$ is the growth rate per year and $t$ is the time in years. Suppose a stock is currently valued at Rs. 5,000 , and it is expected to grow at a rate of $5 \%$ per year.
(i) Find the value of the stock after 10 years.
(ii) After how many years will the stock double in value?

Solution (i) The formula for the exponential growth is:

$$
P(t)=P_{0} e^{r t}
$$

Given $\quad P_{0}=5000, r=0.05(5 \%$ growth rate), and $t=10$ years.

$$
P(10)=5000 e^{0.05 \times 10}=5000 e^{0.5}
$$

Using $e^{0.5} \approx 1.6487$

$$
P(10)=5000 \times 1.6487=8244
$$

So, the value of the stock after 10 years is approximately Rs. 8244
(ii) We want to find $t$ when the stock doubles, i.e., when $P(t)=2 P_{0}$. Using the equation:

$$
2 P_{0}=P_{0} e^{r t}
$$

Dividing both sides by $P_{0}$, we have $2=e^{r t}$
Taking the natural logarithm on both sides: $\ln 2=r t$

$$
\text { and } \quad t=\frac{\ln 2}{r}
$$

$$
\begin{aligned}
& =\frac{0.6931}{0.05} \\
& =13.86
\end{aligned}
$$

So, the stock will double in value i.e., approximately 14 years.

Example 13 The concentration of a pollutant in a lake, in parts per million (ppm), decays over time according to the function

$$
C(t)=\frac{100}{\sqrt{t+1}}
$$

where $t$ is the time in days since the pollutant was introduced.
(i) What is the concentration of the pollutant after 4 days?
(ii) After how many days will the concentration drop below 10 ppm ?

Solution (i) The pollutant concentration function is $C(t)=\frac{100}{\sqrt{t+1}}$, where $t$ is the time in days.
Concentration after 4 days:

$$
\begin{aligned}
C(4) & =\frac{100}{\sqrt{4+1}} \\
& =\frac{100}{\sqrt{5}} \\
& \approx 44.72 \mathrm{ppm}
\end{aligned}
$$

The concentration after 4 days is about 44.72 ppm .
(ii) When will the concentration drop below 10 ppm ? Set $C(t)=10$ :

$$
\begin{aligned}
& 10=\frac{100}{\sqrt{t+1}} \\
& \Rightarrow \sqrt{t+1}=10 \\
& \Rightarrow \quad t+1=100 \\
& \Rightarrow \quad t=99
\end{aligned}
$$

After 99 days, the concentration will drop below 10 ppm .

# EXERCISE 2.2

1. Find the point of intersection of the coordinate axes and the following linear functions graphically:
(i) $y=-5 x+10$
(ii) $y=2 x-1$
(iii) $y=\frac{1}{2} x-3$
(iv) $y=3 x+\frac{3}{2}$
2. Find the point(s) of intersection of the following functions graphically:
(i) $f(x)=2 x+5, g(x)=-x+5$
(ii) $f(x)=3 x-2, g(x)=10-x$

(iii) $f(x)=2 x-4, g(x)=3 x-1$
(iv) $f(x)=-3 x-4, g(x)=\frac{1}{2} x+3$
(v) $f(x)=x-1, g(x)=x^{2}-4 x+3$
(vi) $f(x)=3 x+4, g(x)=x^{2}+2 x-8$
(vii) $f(x)=-2 x-1, g(x)=x^{2}-4 x$
(viii) $f(x)=-x^{2}-3 x+2, g(x)=x+6$
3. Graph the following functions:
(i) $y=\sqrt{3 x}$
(ii) $y=\sqrt{x}+5$
(iii) $y=-\frac{1}{2} \sqrt{x}$
(iv) $y=-\sqrt{x+1}+2$
(v) $y=\sqrt[3]{2 x+1}$
(vi) $y=2 \sqrt[3]{x}-3$
(vii) $y=\sqrt[3]{x^{2}+x-2}$
4. A building's height over time is modeled by $\mathrm{H}(t)=100+20 t$ which is in metres and $t$ is the time in months. The height of a growing tree nearby is given by $T(t)=50+10 t+t^{2}$.
(i) At what time will the building and tree have the same height?
(ii) What will that height be?

Sketch the graphs of both functions and determine the time when the tree will overtake the height of the building.
5. A radioactive substance has a half-life ( $h$ ) of 2 years. If the initial quantity $Q_{0}$ is 200 grams and the exponential decay function is $Q(t)=Q_{0}\left(\frac{1}{2}\right)^{t}$, then find the remaining quantity after 6 years graphically.

# Theory of <br> Quadratic Functions

## INTRODUCTION

This unit explores methods to find the maximum and minimum values of quadratic functions using completing the square and graphical analysis. It also covers the inverse of quadratic functions, determining their domain and range. Additionally, students will learn to solve absolute value quadratic equations and inequalities, as well as equations of rational, radical and exponential forms that can be reduced to quadratic equations. Finally, the unit demonstrates the practical applications of quadratic equations and inequalities in solving real-world problems, providing a strong foundation for problemsolving and analysis.

### 3.1 Quadratic Function

A quadratic function is a polynomial function of degree two. It is typically expressed in the standard form:

$$
f(x)=a x^{2}+b x+c
$$

where $a, b$ and $c$ are real numbers, and $a \neq 0$.

### 3.1.1 Analyzing Quadratic Fyaction by Sketching

As we know shape of the graph of a quadratic function $f(x)=a x^{2}+b x+c$ is a parabola. The parabola opens upward or downward, depending on the sign of the leading coefficient $a$, as shown in the given figure.
The tip of the parabola, labeled as $V$ in the diagrams above, is known as the vertex having coordinates $(h, k)$. The vertical line passing through the vertex serves as the axis of symmetry for the parabola. The vertex represents a turning point, where the graph changes direction.

- If $a>0$, then the vertex is a minimum point.
- If $a<0$, then the vertex is a maximum point.

For sketching the quadratic function, we need to find the $x$-intercept, $y$-intercept and the vertex. For analyzing the sketch of quadratic function, we find whether the vertex is a minimum or a maximum point and indicate the intervals where the function is increasing or decreasing.

Example 1 Sketch and analyze $y=-x^{2}-2 x+3$.
Solution $y=-x^{2}-2 x+3$
The $y$-intercept is $y=-(0)^{2}-2(0)+3=3$
The $x$-intercepts are found by solving the equation:

$$
\begin{aligned}
-x^{2}-2 x+3 & =0 \text { or } x^{2}+2 x-3=0 \\
x^{2}+3 x-x-3 & =0 \\
x(x+3)-1(x+3) & =0 \\
(x+3)(x-1) & =0 \\
x+3=0, x-1 & =0 \\
x & =-3, x=1
\end{aligned}
$$

Now, we find the vertex

$$
h=\frac{-b}{2 a}=-\frac{(-2)}{2(-1)}=-1
$$

$k=-(-1)^{2}-2(-1)+3=-1+2+3=4$
So, the vertex $(-1,4)$ is a maximum point. The function $y$ is increasing on $(-\infty,-1)$ and decreasing on $(-1, \infty)$.
# 3.1.2 Finding Maximum and Minimum Values of Quadratic

## Functions by Completing Square

Completing the square is a technique used to rewrite a quadratic function $f(x)=a x^{2}+b x+c$ in the following vertex form:

$$
f(x)=a(x-h)^{2}+k
$$

where vertex $=(h, k), h=-\frac{b}{2 a}$ and $k=c-\frac{b^{2}}{4 a}$

- If $a>0$, the minimum value of $f(x)$ at $x=h$ is $k$.
- If $a<0$, the maximum value of $f(x)$ at $x=h$ is $k$.

Example 2 Find the maximum or minimum value of $f(x)=-2 x^{2}+4 x+3$ by completing square.
$$
\begin{aligned}
& f(x)=-2\left(x^{2}-2 x\right)+3 \\
& f(x)=-2\left(x^{2}-2 x+1-1\right)+3 \\
& f(x)=-2\left[(x-1)^{2}-1\right]+3 \\
& f(x)=-2(x-1)^{2}+2+3 \\
& f(x)=-2(x-1)^{2}+5
\end{aligned}
$$

Here $a=-2<0$
Therefore, the maximum value is 5 , which occurs when $x=1$.
Example 3 Find the maximum or minimum value of $f(x)=x^{2}-2 x-3$.
Solution Given that $f(x)=x^{2}-2 x-3$
Here $a=1, b=-2, c=-3$

$$
h=-\frac{b}{2 a}=-\frac{(-2)}{2(1)}=1
$$

and

$$
k=c-\frac{b^{2}}{4 a}=-3-\frac{(-2)^{2}}{4(1)}=-4
$$

Here $a=1>0$
Therefore, the minimum value of $f(x)$ at $x=1$ is -4 .

# 3.2 Inverse of Quadratic Function

Quadratic functions are typically not one-to-one over their entire domain. To find an inverse for a quadratic function, we must restrict its domain to a portion where it is one-to-one. Commonly, we restrict the domain to either $x \geq h$ (where $h$ is the $x$-coordinate of the vertex) or $x \leq h$.
Example 4 Find the inverse of $f(x)=x^{2}+4 x+3, x \geq-2$. Also find its domain and range.
Solution $f(x)=x^{2}+4 x+3, \quad x \geq-2$
Let

$$
\begin{aligned}
y & =x^{2}+4 x+3 \\
x & =y^{2}+4 y+3 \\
y^{2}+4 y+3-x=0 & \text { (Interchange } x \text { and } y \text { ) } \\
y & =\frac{-4 \pm \sqrt{(4)^{2}-4(1)(3-x)}}{2(1)} \\
y & =\frac{-4 \pm \sqrt{16-12+4 x}}{2} \\
y & =\frac{-4 \pm \sqrt{4+4 x}}{2} \\
y & =\frac{-4 \pm 2 \sqrt{1+x}}{2} \\
f^{-1}(x) & =-2 \pm \sqrt{1+x}
\end{aligned}
$$

(Replace $y$ with $f^{-1}(x)$ )
The above inverse function has both a positive and a negative component. To determine which is the inverse, we find domain and range of the given function.

$$
\text { Domain } f=[-2, \infty)
$$

To find range, we proceed as:

$$
\begin{aligned}
& f(x)=x^{2}+4 x+3 \\
& \Rightarrow \quad f(x)=(x+2)^{2}-1
\end{aligned}
$$

Therefore, minimum value of $f(x)$ is -1 and hence

$$
\text { Range } f=[-1, \infty)
$$

Domain $f^{-1}=[-1, \infty)$, Range $f^{-1}=[-2, \infty)$
Now, we substitute any value of $x$ that falls within the domain of $f^{-1}(x)$. We choose the value $x=0$.

$$
\begin{aligned}
& f^{-1}(0)=-2+\sqrt{1+0}=-1 \\
& f^{-1}(0)=-2-\sqrt{1+0}=-3
\end{aligned}
$$

We notice only -1 lies in the range of $f$. Therefore, we discard negative component.
Hence $f^{-1}(x)=-2+\sqrt{1+x}$

# 3.3 Absolute Value

The absolute value of $x$, is defined as

$$
|x|=\left\{\begin{array}{ll}
x & , x \geq 0 \\
-x, & x<0
\end{array}\right.
$$

### 3.3.1 Absolute Value Quadratic

## Equations

To solve the absolute value quadratic equations, all answers must be substituted back into the original equation to verify whether they are valid or not. Sometimes, "extraneous" solutions may appear which are not valid and must be eliminated from the final answer.
Example 5 Solve $\left|x^{2}-4\right|=5$
Solution $\left\{\begin{array}{l}x^{2}-4=5 \\ x^{2}-4= \pm 5\end{array}\right.$

$$
\begin{aligned}
x^{2}-4 & =5 \text { or } x^{2}-4=-5 \\
x^{2} & =9 \text { or } x^{2}=-1 \\
x & = \pm 3 \text { or } x= \pm \sqrt{-1}=\text { imaginary }
\end{aligned}
$$

Check: For $x=3$

$$
\begin{array}{r}
\text { For } \quad x=-3 \\
\left|3^{2}-4\right|=5 \\
|5|=5 \\
5=5
\end{array}\left\lvert\, \begin{array}{l}
\left(-3^{2}\right)-4 \mid=5 \\
|5|=5 \\
5=5
\end{array}\right.
$$

Hence solution set $=\{ \pm 3\}$

# 3.3.2 Absolute Value Quadratic Inequalities

Absolute value quadratic inequalities are inequalities that involve a quadratic expression within absolute value bars. They are generally of the following forms:
$\left|a x^{2}+b x+c\right|<d,\left|a x^{2}+b x+c\right|>d,\left|a x^{2}+b x+c\right| \leq d,\left|a x^{2}+b x+c\right| \geq d$
Example 6 Solve $\left|x^{2}-6 x-4\right|<3$
Solution $\left|x^{2}-6 x-4\right|<3$
$-3<x^{2}-6 x-4<3$
$-3<x^{2}-6 x-4$
and $\quad x^{2}-6 x-4<3$
$x^{2}-6 x-4+3>0$
and $\quad x^{2}-6 x-4-3<0$
$x^{2}-6 x-1>0$
(i) , $x^{2}-6 x-7<0$
(ii)

Here we solve $x^{2}-6 x-1=0$

$$
\begin{aligned}
& x=\frac{-(-6) \pm \sqrt{(-6)^{2}-4(1)(-1)}}{2(1)} \\
& x=\frac{6 \pm \sqrt{36+4}}{2} \\
& x=\frac{6 \pm \sqrt{40}}{2} \\
& x=\frac{6 \pm 2 \sqrt{10}}{2} \\
& x=3 \pm \sqrt{10} \\
& x=3-\sqrt{10} \quad 3+\sqrt{10} \\
& x=-0.16 \quad 6.16
\end{aligned}
$$

Hence critical values divide the number line into three regions.
Test $x=-1$ in (i), we have

$$
(-1)^{2}-6(-1)-1>0 \Rightarrow+6>0 \quad \text { (True) }
$$

Test $x=0$ in (i), we have

$$
(0)^{2}-6(0)-1>0 \quad \Rightarrow \quad-1>0 \quad \text { (False) }
$$

Test $x=7$ in (i), we have

$$
(7)^{2}-6(7)-1>0 \quad \Rightarrow \quad 6>0 \quad \text { (True) }
$$

Solution set is $(-\infty, 3-\sqrt{10}) \cup(3+\sqrt{10}, \infty)$

Now, we consider (ii) and solve

$$
\begin{aligned}
x^{2}-6 x-7 & =0 \\
x^{2}+x-7 x-7 & =0 \\
x(x+1)-7(x+1) & =0 \\
(x+1)(x-7) & =0 \\
x+1 & =0, \quad x-7=0 \\
x & =-1, \quad x=7
\end{aligned}
$$

These critical values divide the number line into three regions.
Solution set is $(-1,7)$
Hence the solution set of the given absolute value quadratic inequality is

$$
\{(-\infty, 3-\sqrt{10}) \cup(3+\sqrt{10}, \infty)\} \cap(-1,7)=(-1,3-\sqrt{10}) \cup(3+\sqrt{10}, 7)
$$

# EXERCISE 3.1

1. Find the maximum or minimun value of the following quadratic functions by completing square:
(i) $f(x)=x^{2}+6 x+13$
(ii) $f(x)=x^{2}+4 x$
(iii) $f(x)=-x^{2}+8 x+13$
(iv) $f(x)=-x^{2}-3 x-5$
(v) $f(x)=3 x^{2}+6 x-13$
(vi) $f(x)=-2 x^{2}-x+21$
2. Find the maximum or minimum point by sketching the following quadratic functions. Also find their domain and range:
(i) $f(x)=x^{2}-4 x$
(ii) $f(x)=x^{2}-5 x+6$
(iii) $f(x)=-x^{2}+2 x-8$
(iv) $f(x)=x^{2}-4 x+4$
(v) $f(x)=x^{2}+2 x-8.3$
(vi) $f(x)=6-x-x^{2}$
3. Find the inverse of the following quadratic functions. Also find their domain and range:
(i) $f(x)=x^{2}-3, x \leq 0$
(ii) $f(x)=x^{2}+6 x+4, x<-3$
(iii) $f(x)=2 x^{2}-8 x+11, x \geq 2$
(iv) $f(x)=3 x^{2}-2 x+6, x \geq 5$
(v) $f(x)=2(x-3)^{2}+1, x \geq 3$
(vi) $f(x)=-3(x+4)^{2}-5, x<-4$

4. Solve the following absolute value quadratic equations and inequalities:
(i) $\left|x^{2}+1\right|=5$
(ii) $\left|x^{2}+5 x+4\right|=0$
(iii) $\left|x^{2}-6 x+8\right|=4$
(iv) $\left|3 x^{2}-7 x+2\right|=x^{2}-x+1$
(v) $\left|x^{2}-4\right|<5$
(vi) $\left|x^{2}-3 x+2\right|>4$
(vii) $\left|x^{2}-5 x+6\right| \leq x+2$
(viii) $\left|2 x^{2}-3 x-5\right|<4$

# 3.4 Solutions of Equations Reducible to the Quadratic Equation

There are certain types of equations, which do not look to be of degree 2 , but they can be reduced to the quadratic equation. We shall discuss the solutions of the rational and radical equations.

### 3.4.1 Rational Equations Reducible to the Quadratic Equation

A rational equation is an equation containing one or more rational expressions, where rational expressions typically contain a variable in the denominator.
Example 7 Solve $\frac{1}{x}+\frac{2}{x+1}=1, x \neq 0, x \neq-1$
Solution $\frac{1}{x}+\frac{2}{x+1}=1$
Multiplying both sides by $x(x+1)$, we have

$$
\begin{aligned}
(x+1)+2 x & =x(x+1) \\
x+1+2 x & =x^{2}+x \\
3 x+1 & =x^{2}+x \\
x^{2}+x-3 x-1 & =0 \\
x^{2}-2 x-1 & =0 \\
x & =\frac{-(-2) \pm \sqrt{(-2)^{2}-4(1)(-1)}}{2(1)} \\
& =\frac{2 \pm \sqrt{4+4}}{2} \\
x & =\frac{2 \pm \sqrt{8}}{2} \\
& =\frac{2 \pm 2 \sqrt{2}}{2} \\
& =1 \pm \sqrt{2}
\end{aligned}
$$

Hence, Solution Set $=\{1 \pm \sqrt{2}\}$

# 3.4.2 Radical Equations Reducible to the Quadratic Equation

Equations involving radical expressions of the variable are called radical equations. To solve a radical equation, we first obtain an equation free from radicals. Every solution of radical equation is also a solution of the radical-free equation but the new equation has solutions that are not solutions of the original radical equation. Such extra solutions (roots) are called extraneous roots.
Example 8 Solve $\sqrt{x+8}+\sqrt{x+3}=\sqrt{12 x+13}$
Solution $\sqrt{x+8}+\sqrt{x+3}=\sqrt{12 x+13}$
Squaring both sides, we get

$$
\begin{aligned}
x+8+x+3+2(\sqrt{x+8})(\sqrt{x+3}) & =12 x+13 \\
2(\sqrt{x+8})(\sqrt{x+3}) & =10 x+2 \\
\Rightarrow \quad \sqrt{(x+8)(x+3)} & =5 x+1
\end{aligned}
$$

Squaring again, we have

$$
\begin{aligned}
x^{2}+11 x+24 & =25 x^{2}+10 x+1 \\
\Rightarrow \quad 24 x^{2}-x-23 & =0 \\
\Rightarrow \quad(24 x+23)(x-1) & =0 \\
x & =-\frac{23}{24} \text { or } x=1
\end{aligned}
$$

On checking we find that $-\frac{23}{24}$ is an extraneous root. Hence solution set $=\{1\}$

### 3.5 Real World Problems of Quadratic Equations and Inequalities

We shall now proceed to solve the problems which, when expressed symbolically, lead to quadratic equations in one variables.
In order to solve such problems, we must:
(i) Suppose the unknown quantities to be $x$ or $y$ etc.
(ii) Translate the problem into symbols and form the equation or inequality satisfying the given conditions.
The method of solving the problems will be illustrated through the following examples:

Example 9 The length of a room is 3 metres greater than its breadth. If the area of the room is 180 square metres, find length and the breadth of the room.
Solution Let the breadth of room $=x$ metres
and the length of room $=(x+3)$ metres
$\therefore \quad$ Area of the room $=x(x+3)$ square metres
By the given condition, we have

$$
\begin{aligned}
x(x+3) & =180 \\
\Rightarrow \quad x^{2}+3 x-180 & =0 \\
\Rightarrow \quad(x+15)(x-12) & =0 \\
\therefore \quad x=-15 \text { or } x & =12
\end{aligned}
$$

As breadth cannot be negative so $x=-15$ is not admissible.
When $x=12$, we get $x+3=12+3=15$
Hence breadth of the room $=12$ metres and length of the room $=15$ metres.
Example 10 A company manufactures laptops and its weekly profit function (in thousands of dollars) is $P(x)=-x^{2}+2 x+3$, where $x$ is the number of laptops produced (in hundreds). Find the range of production levels where the company makes at least $\$ 4,000$ profit.
Solution Here $P(x) \geq 4$

$$
\begin{aligned}
& -x^{2}+2 x+3 \geq 4 \\
& -x^{2}+2 x+3-4 \geq 0 \\
& -x^{2}+2 x-1 \geq 0 \\
& x^{2}-2 x+1 \leq 0 \\
& (x-1)^{2} \leq 0
\end{aligned}
$$

This only holds true when $(x-1)^{2}=0 \Rightarrow x=1$
The company makes exactly $\$ 4,000$ profit when 100 laptops are produced (since $x=1$ means 100 laptops). There is no production level where profit is more than $\$ 4,000$.

# EXERCISE 3.2

1. Solve the following equations:
(i) $\frac{1}{3 x}+\frac{4 x}{6}=1, x \neq 0$
(ii) $\frac{x}{x+1}+\frac{x+1}{x}=\frac{5}{2} ; x \neq-1,0$
(iii) $\frac{1}{x+1}+\frac{2}{x+2}=\frac{7}{x+5} ; x \neq-1,-2,-5$

(iv) $\frac{a}{a x-1}+\frac{b}{b x-1}=a+b ; x \neq \frac{1}{a}, \frac{1}{b}$
(v) $\frac{x+1}{x-1}+\frac{x-1}{x+1}=2, x \neq 1, x \neq-1$
(vi) $3 x^{2}+15 x-2 \sqrt{x^{2}+5 x+1}=2$
(vii) $\sqrt{2 x+8}+\sqrt{x+5}=7$
(viii) $\sqrt{3 x+4}=2+\sqrt{2 x-4}$
(ix) $\sqrt{x+7}+\sqrt{x+2}=\sqrt{6 x+13}$
(x) $\sqrt{x+5}-\sqrt{x-3}=2$

2 A farmer bought some sheep for Rs. 9000. If he had paid Rs. 100 less for each, he would have got 3 sheep more for the same money. How many sheep did he buy, when the rate in each case is uniform?
3. A man sold his stock of eggs for Rs. 2400 . If he had 2 dozen more, he would have got the same money by selling the whole for Rs. 0.50 per dozen cheaper. How many dozen eggs did he sell?
4. A cyclist travelled 48 km at a uniform speed. If he had travelled $2 \mathrm{~km} /$ hour slower, he would have taken 2 hours more to perform the journey. How long did he take to cover 48 km ?
5. To do a piece of work, Abdullah takes 10 days more than Abdul Hadi. Together they finish the work in 12 days. How long would Abdul Hadi take to finish it alone?
6. The braking distance (in metres) of a car is modeled by:
$d(s)=0.02 s^{2}+0.1 s$, where $s$ is the speed of car in $\mathrm{km} / \mathrm{h}$
If the maximum safe braking distance is 50 metres, find the range of speed where braking is safe.
7. A rocket follows the height function $h(t)=-5 t^{2}+20 t+30$, where $h(t)$ is the height in metres and $t$ is the time in seconds. Find the time interval during which the rocket is at least 40 metres above the ground.