# Chapter 2: 2.1.4 Types of Function

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