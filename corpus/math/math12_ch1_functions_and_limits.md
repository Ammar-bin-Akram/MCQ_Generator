# Chapter 1: FUNCTIONS AND LIMITS

# 1.1 INTRODUCTION

Functions are important tools by which we describe the real world in mathematical terms. They are used to explain the relationship between variable quantities and hence play a central role in the study of calculus.

## 1.1.1 Concept of Function

The term function was recognized by a German Mathematician Leibniz (1646 - 1716) to describe the dependence of one quantity on another. The following examples illustrate how this term is used:

- (i) The area "A" of a square depends on one of its sides "x" by the formula $$A = x^2$$, so we say that $$A$$ is a function of $$x$$.
- (ii) The volume "V" of a sphere depends on its radius "r" by the formula $$V = \frac{4}{3} \pi r^3$$, so we say that $$V$$ is a function of $$r$$.

A function is a rule or correspondence, relating two sets in such a way that each element in the first set corresponds to one and only one element in the second set. Thus in, (i) above, a square of a given side has only one area. And in, (ii) above, a sphere of a given radius has only one volume. Now we have a formal definition:

## 1.1.2 Definition (Function - Domain - Range)

A Function $$f$$ from a set $$X$$ to a set $$Y$$ is a rule or a correspondence that assigns to each element $$x$$ in $$X$$ a unique element $$y$$ in $$Y$$. The set $$X$$ is called the domain of $$f$$.

The set of corresponding elements $$y$$ in $$Y$$ is called the range of $$f$$.

Unless stated to the contrary, we shall assume hereafter that the set $$X$$ and $$Y$$ consist of real numbers.

## 1.1.3 Notation and Value of a Function

If a variable $$y$$ depends on a variable $$x$$ in such a way that each value of $$x$$ determines exactly one value of $$y$$, then we say that $$y$$ is a function of $$x$$.

Swiss mathematician Euler (1707-1783) invented a symbolic way to write the statement $$y$$ is a function of $$x$$ as $$y = f(x)$$, which is read as $$y$$ is equal to $$f$$ of $$x$$.

**Note:** Functions are often denoted by the letters such as $$f, g, h, x, o, u$$ and so on.

A function can be thought as a computing machine $$f$$ that takes an input $$x$$, operates on it in some way, and produces exactly one output $$f(x)$$. This output $$f(x)$$ is called the value of $$f$$ at $$x$$ or image of $$x$$ under $$f$$. The output $$f(x)$$ is denoted by a single letter, say $$y$$, and we write $$y = f(x)$$.

The variable $$x$$ is called the independent variable of $$f$$, and the variable $$y$$ is called the dependent variable of $$f$$. For now onward we shall only consider the function in which the variables are real numbers and we say that $$f$$ is a real valued function of real numbers.

**Example 1:** Given $$f(x) = x^3 - 2x^2 + 4x - 1$$, find

- (i) $$f(0)$$
- (ii) $$f(1)$$
- (iii) $$f(-2)$$
- (iv) $$f(1 + x)$$
- (v) $$f(1/x), x \neq 0$$

**Solution:** $$f(x) = x^3 - 2x^2 + 4x - 1$$

- (i) $$f(0) = 0 - 0 + 0 - 1 = -1$$
- (ii) $$f(1) = (1)^3 - 2(1)^2 + 4(1) - 1 = 1 - 2 + 4 - 1 = 2$$
- (iii) $$f(-2) = (-2)^2 - 2(-2)^2 + 4(-2) - 1 = -8 - 8 - 8 - 1 = -2.5$$
- (iv) $$f(1 + x) = (1 + x)^3 - 2(1 + x)^2 + 4(1 + x) - 1 = 1 + 3x + 3x^2 + x^3 - 2 - 4x - 2x^2 + 4 + 4x - 1 = x^3 + x^2 + 3x + 2$$

- (iv) *f*(1/*x*) = (1/*x*)² - 2(1/*x*)² + 4(1/*x*) - 1 = $$\frac{1}{x^2} \cdot \frac{2}{x^2} + \frac{4}{x} \cdot 1, x \neq 0$$

**Example 2:** Let *f*(*x*) = *x*². Find the domain and range of *f*.

**Solution:** *f*(*x*) is defined for every real number *x*. Further for every real number *x*, *f*(*x*) = *x*² is a non-negative real number. So

> Domain *f* = Set of all real numbers. Range *f* = Set of all non-negative real numbers.

**Example 3:** Let *f*(*x*) = $$\frac{x}{x^2 - 4}$$. Find the domain and range of *f*.

**Solution:** At *x* = 2 and *x* = -2, *f*(*x*) = $$\frac{x}{x^2 - 4}$$ is not defined. So

Domain *f* = Set of all real numbers except -2 and 2. Range *f* = Set of all real numbers.

**Example 4:** Let *f*(*x*) = $$\sqrt{x^2 - 9}$$. Find the domain and range of *f*.

**Solution:** We see that if *x* is in the interval -3 < *x* < 3, a square root of a negative number is obtained. Hence no real number *y* = $$\sqrt{x^2 - 9}$$ exists. So

> Domain *f* = (*x* ∈ *R* : |*x*| ≥ 3) = (-∞, -3] ∪ [3, + ∞) Range *f* = set of all positive real numbers = (0, + ∞)

### 1.1.4 Graphs of Algebraic functions

If *f* is a real-valued function of real numbers, then the graph of *f* in the *xy*-plane is defined to be the graph of the equation *y* = *f*(*x*).

The graph of a function *f* is the set of points {(*x*, *y*) | *y* = *f*(*x*)}, *x* is in the domain of *f* in the Cartesian plane for which (*x*, *y*) is an ordered pair of *f*. The graph provides a visual technique for determining whether the set of points represents a function or not. If a vertical line intersects a graph in more than one point, it is not the graph of a function.

Explanation is given in the figure.

### **Method to draw the graph:**

To draw the graph of *y* = *f*(*x*), we give arbitrary values of our choice to *x* and find the corresponding values of *y*. In this way we get ordered pairs (*x*, *y*, *y*₁), (*x*, *y*₂), (*x*, *y*₃), etc. These ordered pairs represent points of the graph in the Cartesian plane. We add these points and join them together to get the graph of the function.

**Example 5:** Find the domain and range of the function *f*(*x*) = *x*² + 1 and draw its graph.

**Solution:** Here *y* = *f*(*x*) = *x*² + 1

We see that *f*(*x*) = *x*² + 1 is defined for every real number. Further, for every real number *x*, *y* = *f*(*x*) = *x*² + 1 is a non-negative real number.

> Hence Domain *f* = set of all real numbers

and Range *f* = set of all non-negative real numbers except the points 0 ≤ *y* < 1.

For graph of *f*(*x*) = *x*² + 1, we assign some values to *x* from its domain and find the corresponding values in the range *f* as shown in the table:

|  *x* | -3 | -2 | -1 | 0 | 1 | 2 | 3  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  *y* = *f*(*x*) | 10 | 5 | 2 | 1 | 2 | 5 | 10  |

Plotting the points (*x*, *y*) and joining them with a smooth curve, we get the graph of the function *f*(*x*) = *x*² + 1, which is shown in the figure.

### **1.1.5 Graph of Functions Defined Piece-wise.**

When the function *f* is defined by two rules, we draw the graphs of two functions as explained in the following example:

**Example 7:** Find the domain and range of the function defined by:

$$f(x) = \begin{cases} x & \text{when } 0 \leq x \leq 1 \ x - 1 & \text{when } 1 < x \leq 2 \end{cases} \quad \text{also draw its graph.}$$

**Solution:** Here domain *f* = [0, 1] ∪ [1, 2] = [0, 2]. This function is composed of the following two functions:

(i) *f(x)* = *x* when 0 ≤ *x* ≤ 1

(ii) *f(x)* = *x* − 1, when 1 < *x* ≤ 2

To find the table of values of *x* and *y* = *f(x)* in each case, we take suitable values to *x* in the domain *f*. Thus

|  Table for *y* = *f(x)* = *x* |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  *x* | 0 | 0.5 | 0.8 | 1 |  |  |  |  |  |  |  |  |  |  |   |
|  *y* = *f(x)* | 0 | 0.5 | 0.8 | 1 |  |  |  |  |  |  |  |  |  |  |   |

Plotting the points (*x*, *y*) and joining them we get two straight lines as shown in the figure. This is the graph of the given function.

# **1.2 TYPES OF FUNCTIONS**

Some important types of functions are given below:

### **1.2.1 Algebraic Functions**

Algebraic functions are those functions which are defined by algebraic expressions. We classify algebraic functions as follows:

*version: 1.1*

### **(i) Polynomial Function**

A function *P* of the form *P(x)* = *a_{n} x^{n}* + *a_{n-1} x^{n-1}* + *a_{n-2} x^{n-2}* + ... + *a_{2} x^{2}* + *a_{1} x + a_{0}* for all *x*, where the coefficient *a_{n}*, *a_{n-1}*, *a_{n-2}*, ... , *a_{2}*, *a_{1}*, *a_{0}* are real numbers and the exponents are non-negative integers, is called a **polynomial function**.

The domain and range of *P(x)* are, in general, subsets of real numbers.

If *a_{n}* ≠ 0, then *P(x)* is called a polynomial function of degree *n* and *a_{n}* is the leading coefficient of *P(x)*.

For example, *P(x)* = 2*x^{4}* − 3*x^{3}* + 2*x* − 1 is a **polynomial function** of degree 4 with leading coefficient 2.

### **(ii) Linear Function**

If the degree of a polynomial function is 1, then it is called a **linear function**. A linear function is of the form: *f(x)* = *ax* + *b* (*a* ≠ 0), *a, b* are real numbers.

For example *f(x)* = 3*x* + 4 or *y* = 3*x* + 4 is a **linear function**. Its domain and range are the set of real numbers.

### **(iii) Identity Function**

For any set *X*, a function *I* : *X* → *X* of the form *I(x)* = *x* ∀ *x* ∈ *X*, is called an **identity function**. Its domain and range is the set *X* itself. In particular, if *X* = *R*, then *I(x)* = *x*, for all *x* ∈ *R*, is the identity function.

### **(iv) Constant Function**

Let *X* and *Y* be sets of real numbers. A function *C* : *X* → *Y* defined by *C(x)* = *a*, ∀ *x* ∈ *X*, *a* ∈ *Y* and fixed, is called a **constant function**.

For example, *C* : *R* → *R* defined by *C(x)* = 2, ∀ *x* ∈ *R* is a constant function.

### **(v) Rational Function**

A function *R(x)* of the form *Q(x) = 0*, where both *P(x)* and *Q(x)* are polynomial functions and *Q(x)* ≠ 0, is called a **rational function**.

The domain of a rational function *R(x)* is the set of all real numbers *x* for which *Q(x)* ≠ 0.

### **1.2.2 Trigonometric Functions**

We denote and define *trigonometric functions* as follows:

(i) $y=\sin x$, Domain $=R$, Range $-1 \leq y \leq 1$.
(ii) $y=\cos x$, Domain $=R$, Range $-1 \leq y \leq 1$.
(iii) $y=\tan x$, Domain $=(x: x \in R$ and $x=(2 n+1) \frac{\pi}{2}, n$ an integer), Range $=R$
(iv) $y=\cot x$, Domain $=(x: x \in R$ and $x \neq n \pi, n$ an integer), Range $=R$
(v) $y=\sec x$, Domain $=(x: x \in R$ and $x \neq(2 n+1) \frac{\pi}{2}, n$ an integer), Range $=R$
(vi) $y=\csc x$, Domain $=(x: x \in R$ and $x \neq n \pi, n$ an integer), Range $=y \geq 1, y \leq-1$

### 1.2.3 Inverse Trigonometric Functions

We denote and define inverse trigonometric functions as follows:
(i) $y=\sin ^{-1} x \Leftrightarrow x=\sin y$, where $-\frac{\pi}{2} \leq y \leq \frac{\pi}{2},-1 \leq x \leq 1$
(ii) $y=\cos ^{-1} x \Leftrightarrow x=\cos y$, where $0 \leq y \leq \pi,-1 \leq x \leq 1$
(iii) $y=\tan ^{-1} x \Leftrightarrow x=\tan y$, where $-\frac{\pi}{2}<y<\frac{\pi}{2},-\infty<x<\infty$

### 1.2.4 Exponential Function

A function, in which the variable appears as exponent (power), is called an exponential function. The functions, $y=e^{a x}, y=e^{x}, y=2^{x}=$ $e^{a \cdot x-2}$, etc are exponential functions of $x$.

### 1.2.5 Logarithmic Function

If $x=a^{x}$, then $y=\log _{a} x$, where $a>0, a \neq 1$ is called Logarithmic Function of $x$.
(i) If $a=10$, then we have $\log _{10} x$ (written as $\lg x$ ) which is known as the common logarithm of $x$.
(ii) If $a=e$, then we have $\log _{e} x$ (written as $\ln x$ ) which is known as the natural logarithm of $x$.

### 1.2.6 Hyperbolic Functions

(i) $\sinh x=\frac{1}{a}\left(e^{a}-e^{-a}\right)$ is called hyperbolic sine function. Its domain and range are the set of all real numbers.
(ii) $\cosh x=\frac{1}{a}\left(e^{a}+e^{-a}\right)$ is called hyperbolic cosine function. Its domain is the set of all real numbers and the range is the set of all numbers in the interval $[1,+\infty)$
(iii) The remaining four hyperbolic functions are defined in terms of the hyperbolic sine and the hyperbolic cosine function as follows:

$$
\begin{aligned}
& \tanh x=\frac{\sinh x}{\cosh x}=\frac{e^{a}-\mathrm{e}^{-a}}{e^{a}+\mathrm{e}^{-a}} \quad \operatorname{sech} x=\frac{1}{\cosh x} \quad \frac{2}{e^{a}+\mathrm{e}^{-a}} \\
& \operatorname{coth} x=\frac{\cosh x}{\sinh x}=\frac{e^{a}+\mathrm{e}^{-a}}{e^{a}-\mathrm{e}^{-a}} \quad \operatorname{csch} x=\frac{1}{\sinh x} \quad \frac{2}{e^{a}-\mathrm{e}^{-a}}
\end{aligned}
$$

The hyperbolic functions have same properties that resemble to those of trigonometric functions.

### 1.2.7 Inverse Hyperbolic Functions

The inverse hyperbolic functions are expressed in terms of natural logarithms and we shall study them in higher classes.
(i) $\quad \sinh ^{-1} x=\ln \left(x+\sqrt{x^{2}+1}\right)$, for all $x \quad$ (iv) $\operatorname{coth}^{-1} x=\frac{1}{x} \ln \left(\frac{x+1}{x-1}\right),|x|<1$
(ii) $\cosh ^{-1} x=\ln \left(x+\sqrt{x^{2}-1}\right) x \geq 1 \quad$ (v) $\operatorname{sech}^{-1} x=\ln \left(\frac{1}{x}+\frac{\sqrt{1-x^{2}}}{x}\right), 0<x \leq 1$
(iii) $\tanh ^{-1} x=\frac{1}{2} \ln \left(\frac{1+x}{1-x}\right),|x|<1 \quad$ (vi) $\operatorname{csch}^{-1} x=\ln \left(\frac{1}{x}+\frac{\sqrt{1+x^{2}}}{|x|}\right), x \neq 0$

### 1.2.8 Explicit Function

If $y$ is easily expressed in terms of the independent variable $x$, then $y$ is called an explicit function of $x$. For example
(i) $y=x^{2}+2 x-1 \quad$ (ii) $y=\sqrt{x-1}$ are explicit functions of $x$.

Symbolically it can be written as $y=f(x)$.

### 1.2.9 Implicit Function

If $x$ and $y$ are so mixed up and $y$ cannot be expressed in terms of the independent variable $x$, then $y$ is called an implicit function of $x$. For example,
(i) $x^{2}+x y+y^{2}=2$
(ii) $\frac{x y^{2}-y+9}{x y}=1$ are implicit functions of $x$ and $y$.

Symbolically it is written as $f(x, y)=0$.

## (ix) Parametric Functions

Some times a curve is described by expressing both $x$ and $y$ as function of a third variable " $t$ " or " $\theta$ " which is called a parameter. The equations of the type $x=f(t)$ and $y=g(t)$ are called the parametric equations of the curve.

The functions of the form:
(i) $\begin{aligned} x=a t^{2} & x=a \cos t \\ y=a t & y=a \sin t\end{aligned}$
(ii) $\begin{aligned} x=a \cos \theta & x=a \sec \theta \\ y=b \sin \theta & y=a \tan \theta\end{aligned}$ (iv) $\quad y=a \tan \theta$ are called parametric functions. Here the variable $t$ or $\theta$ is called parameter.

### 1.2.10 Even Function

A function $f$ is said to be even if $f(-x)=f(x)$, for every number $x$ in the domain of $f$. For example: $\quad f(x)=x^{2}$ and $f(x)=\cos x$ are even functions of $x$.
Here

$$
f(-x)=(-x)^{2}=x^{2}=f(x) \text { and } f(-x)=\cos (-x)=\cos x=f(x)
$$

### 1.2.11 Odd Function

A function $f$ is said to be odd if $f(-x)=-f(x)$, for every number $x$ in the domain of $f$. For example, $\quad f(x)=x^{2}$ and $f(x)=\sin x$ are odd functions of $x$. Here

$$
f(-x)=(-x)^{2}=-x^{2}=-f(x) \text { and } f(-x)=\sin (-x)=-\sin x=-f(x)
$$

## Note: In both the cases, for each $x$ in the domain of $f,-x$ must also be in the domain of $f$

Example 1: Show that the parametric equations $x=a \cos t$ and $y=a \sin t$ represent the equation of the circle $x^{2}+y^{2}=a^{2}$

Solution: The parametric equations are

$$
\begin{aligned}
x=a \cos t & \text { (i) } \\
y=a \sin t & \text { (ii) }
\end{aligned}
$$

We eliminate the parameter " $t$ " from equations (i) and (ii).
By squaring we get, $\quad x^{2}=a^{2} \cos ^{2} t$

$$
y^{2}=a^{2} \sin ^{2} t
$$

By adding we get, $\quad x^{2}+y^{2}=a^{2} \cos ^{2} t+a^{2} \sin ^{2} t$

$$
=a^{2}\left(\cos ^{2} t+\sin ^{2} t\right)
$$

$\therefore x^{2}+y^{2}=a^{2}$, which is equation of the circle.
Example 2: $\quad$ Prove the identities
(i) $\cosh ^{2} x-\sinh ^{2} x=1$
(ii) $\cosh ^{2} x+\sinh ^{2} x=\cosh 2 x$

Solution: We know that $\sinh x=\frac{e^{x}-e^{-x}}{2}$

$$
\text { and } \quad \cosh x=\frac{e^{x}+e^{-x}}{2}
$$

Squaring (1) and (2) we have

$$
\begin{aligned}
& \sinh ^{2} x=\frac{e^{2 x}+e^{-2 x}-2}{4} \text { and } \cosh ^{2} x=\frac{e^{2 x}+e^{-2 x}+2}{4} \\
& \text { Now (i) } \quad \cosh ^{2} x-\sinh ^{2} x=\frac{e^{2 x}+e^{-2 x}+2}{4}-\frac{e^{2 x}+e^{-2 x}-2}{4} \\
& =\frac{e^{2 x}+e^{-2 x}+2-e^{2 x}-e^{-2 x}+2}{4}=\frac{4}{4} \\
& \therefore \quad \cosh ^{2} x-\sinh ^{2} x=1
\end{aligned}
$$

and (ii) $\cosh ^{2} x+\sinh ^{2} x=\frac{e^{2 x}+e^{-2 x}+2}{4}+\frac{e^{2 x}+e^{-2 x}-2}{4}$

$$
\begin{aligned}
& =\frac{e^{2 x}+e^{-2 x}+2+e^{2 x}+e^{-2 x}-2}{4} \\
& =\frac{2 e^{2 x}+2 e^{-2 x}}{4}=\frac{e^{2 x}+e^{-2 x}}{2} \\
\therefore \cosh ^{2} x+\sinh ^{2} x & =\cosh 2 x
\end{aligned}
$$

Example 3: Determine whether the following functions are even or odd.
(a) $f(x)=3 x^{4}-2 x^{2}+7$
(b) $f(x)=\frac{3 x}{x^{2}+1}$
(c) $f(x)=\sin x+\cos x$

## (a) $f(-x)=3(-x)^{4}-2(-x)^{2}+7=3 x^{4}-2 x^{2}+7=f(x)$

Thus $\quad f(x)=3 x^{4}-2 x^{2}+7$ is even.
(b) $\quad f(-x)=\frac{3(-x)}{(-x)^{2}+1}-\frac{3 x}{x^{2}+1}=-f(x)$

Thus $\quad f(x)=\frac{3 x}{x^{2}+1}$ is odd
(c) $\quad f(-x)=\sin (-x)+\cos (-x)=-\sin x+\cos x \neq \pm f(x)$

Thus $f(x)=\sin x+\cos x$ is neither even nor odd

## EXERCISE 1.1

1. Given that:
(a) $f(x)=x^{2}-x$
(b) $f(x)=\sqrt{x+4}$

Find
(i) $f(-2)$
(ii) $f(0)$
(iii) $f(x-1)$
(iv) $f\left(x^{2}+4\right)$
2. Find $\frac{f(a+h)-f(a)}{h}$ and simplify where,
(i) $f(x)=6 x-9$
(ii) $f(x)=\sin x$
(iii) $f(x)=x^{3}+2 x^{2}-1$
(iv) $f(x)=\cos x$
3. Express the following:
(a) The perimeter $P$ of square as a function of its area $A$.
(b) The area $A$ of a circle as a function of its circumference $C$.
(c) The volume $V$ of a cube as a function of the area $A$ of its base.
4. Find the domain and the range of the function $g$ defined below, and
(i) $g(x)=2 x-5$
(ii) $g(x)=\sqrt{x^{2}-4}$
(iii) $g(x)=\sqrt{x+1}$
(iv) $g(x)=|x-3|$
(v) $g(x)=\left\{\begin{array}{lll}6 x+7 & , & x \leq-2 \\ 4-3 x & , & -2<x\end{array}\right.$
(vi) $g(x)=\left\{\begin{array}{lll}x-1 & , & x<3 \\ 2 x+1 & , & 3 \leq x\end{array}\right.$
(vii) $g(x)=\frac{x^{3}-3 x+2}{x+1}, x \neq-1$
(viii) $g(x)=\frac{x^{3}-16}{x-4}, x \neq 4$
5. Given $f(x)=x^{3}-a x^{2}+b x+1$

If $f(2)=-3$ and $f(-1)=0$. Find the values of $a$ and $b$.
6. A stone falls from a height of 60 m on the ground, the height $h$ after $x$ seconds is approximately given by $h(x)=40-10 x^{2}$
(i) What is the height of the stone when:.
(a) $x=1 \mathrm{sec}$ ?
(b) $x=1.5 \mathrm{sec}$ ?
(c) $x=1.7 \mathrm{sec}$ ?
(ii) When does the stone strike the ground?
7. Show that the parametric equations:
(i) $x=a t^{2}, y=2 a t$ represent the equation of parabola $y^{2}=4 a x$
(ii) $x=a \cos \theta, y=b \sin \theta$ represent the equation of ellipse $\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1$
(iii) $x=a \sec \theta, y=b \tan \theta$ represent the equation of hyperbola $\frac{x^{2}}{a^{2}}-\frac{y^{2}}{b^{2}}=1$
8. Prove the identities:
(i) $\sinh 2 x=2 \sinh x \cosh x$
(ii) $\operatorname{sech}^{2} x=1-\tanh ^{2} x$
(iii) $\operatorname{csch}^{2} x=\operatorname{coth}^{2} x-1$

9. Determine whether the given function *f* is even or odd.
   - (i) *f*(*x*) = *x*^2 + *x* (ii) *f*(*x*) = (*x* + 2)^2
   - (iii) *f*(*x*) = *x*√*x*^2 + 5 (iv) *f*(*x*) = *x* − 1/*x* + 1, *x* ≠ -1
   - (v) *f*(*x*) = *x*^2 + 6 (vi) *f*(*x*) = *x*^2 − *x*/*x* + 1

# **1.3 COMPOSITION OF FUNCTIONS AND INVERSE OF AFUNCTION**

Let *f* be a function from set *X* to set *Y* and *g* be a function from set *Y* to set *Z*. The composition of *f* and *g* is a function, denoted by *gof*, from *X* to *Z* and is defined by

(*gof*(*x*) = *g*(*f*(*x*)) = *gf*(*x*), for all *x* ∈ *X*).

### **1.3.1 Composition of Functions**

#### **Explanation**

Consider two real valued functions *f* and *g* defined by

*f*(*x*) = 2*x* + 3 and *g*(*x*) = *x*^2

then *gof*(*x*) = *g*(*f*(*x*)) = *g*(2*x* + 3) = (2*x* + 3)^2

The arrow diagram of two successive mappings, *f*, *g*, is denoted by *gf* and is shown in the figure.

Thus a single composite function *gf*(*x*) is equivalent to two successive functions *f* followed by *g*.

**Example 1:** Let the real valued functions *f* and *g* be defined by

*f*(*x*) = 2*x* + 1 and *g*(*x*) = *x*^2 − 1

Obtain the expressions for (i) *fg* (*x*) (ii) *gf*(*x*) (iii) *f*^2 (*x*) (iv) *g*^2 (*x*)

#### **Solution:**

- (i) *fg*(*x*) = *f*(*g*(*x*)) = *f*(*x*^2 − 1) = 2(*x*^2 − 1) + 1 = 2*x*^2 − 1
- (ii) *gf*(*x*) = *g*(*f*(*x*)) = *g*(2*x* + 1) = (2*x* + 1)^2 − 1 = 4*x*^2 + 4*x*
- (iii) *f*^2(*x*) = *f*(*f*(*x*)) = *f*(2*x* + 1) = 2(2*x* + 1) + 1 = 4*x* + 3
- (iv) *g*^2(*x*) = *g*(*g**x*) = *g*(*x*^2 − 1) = (*x*^2 − 1)^2 − 1 = *x*^4 − 2*x*^2

We observe from (i) and (ii) that *fg*(*x*) ≠ *gf*(*x*).

#### **Note:**

- It is important to note that, in general, *gf*(*x*) ≠ *fg*(*x*), because *gf*(*x*) means that *f* is applied first then followed by *g*, whereas *fg*(*x*) means that *g* is applied first then followed by *f*.
- We usually write *ff* as *f*^2 and *fff* as *f*^3 and so on.

### **1.3.2 Inverse of a Function**

Let *f* be a one-one function from *X* onto *Y*. The **inverse function** of *f* denoted by *f*⁻¹, is a function from *Y* onto *X* and is defined by:

*x* = *f*⁻¹(*y*), ∀ *y* ∈ *Y* if and only if *y* = *f*(*x*), ∀ *x* ∈ *X*.

#### **Illustration by arrow diagram**

The inverse function reverses the correspondence of the original function, so that

*f*⁻¹(*y*) = *x*, when *f*(*x*) = *y*

and *f*(*x*) = *y*, when *f*⁻¹(*y*) = *x*.

We can find the composition of the functions *f* and *f*⁻¹ as follows:

and (*fof*⁻¹)(*y*) = *f*(*f*⁻¹(*y*)) = *f*(*x*) = *y*.

We note that *f*⁻¹ *of* and *fof*⁻¹ are identity mappings on the domain and range of *f* and *f*⁻¹ respectively.

### **1.3.3 Algebraic Method to find the Inverse Function**

The inverse function can be found by using the algebraic method as explained in the following example:

Example 2: Let $f: R \rightarrow R$ be the function defined by

$$
f(x)=2 x+1 \text {. Find } f^{-1}(x)
$$

## Remember that:

The change of name of variable in the definition of function does not change that function where the domain and range coincide.

Solution: We find the inverse of $f$ as follows:
Write $f(x)=2 x+1=y$
So that $y$ is the image of $x$ under $f$.
Now solve this equation for $x$ as follows:

$$
\begin{aligned}
& y=2 x+1 \\
& \Rightarrow \quad 2 x=y-1 \\
& \Rightarrow \quad x=\frac{y-1}{2} \\
& \therefore \quad f^{-1}(y)=\frac{1}{2}(y-1) \quad \text {; } \quad x=f^{-1}(y)
\end{aligned}
$$

To find $f^{-1}(x)$, replace $y$ by $x$.

$$
\therefore \quad f^{-1}(x)=\frac{1}{2}(x-1)
$$

## Verification:

$$
\begin{gathered}
f\left(f^{-1}(x)\right)=f\left(\frac{1}{2}(x-1)\right)=2\left[\frac{1}{2}(x-1)\right]+1=x \\
\text { and } \quad f^{-1}(f(x))=f^{-1}(2 x+1)=\frac{1}{2}(2 x+1-1)=x
\end{gathered}
$$

Example 3: Without finding the inverse, state the domain and range of $f^{-1}$, where

$$
f(x)=2+\sqrt{x-1}
$$

Solution: We see that $f$ is not defined when $x<1$.
$\therefore \quad$ Domain $f=[1,+\infty)$
As a varies over the interval $[1,+\infty)$, the value of $\sqrt{x-1}$ varies over the interval $[0,+\infty)$.

So the value of $f(x)=2+\sqrt{x-1}$ varies over the interval $[2,+\infty)$. Therefore range $f=[2,+\infty)$
By definition of inverse function $f^{-1}$, we have
domain $f^{-1}=$ range $f=[2,+\infty)$
and range $f^{-1}=$ domain $f=[1,+\infty)$

## EXERCISE 1.2

1. The real valued functions $f$ and $g$ are defined below. Find
(a) $f \circ g(x)$
(b) $g \circ f(x)$
(c) $f \circ f(x)$
(d) $g \circ g(x)$
(i) $f(x)=2 x+1$
; $\quad g(x)=\frac{3}{x-1}, x \neq 1$
(ii) $f(x)=\sqrt{x+1}$
; $\quad g(x)=\frac{1}{x^{2}}, x \neq 0$
(iii) $f(x)=\frac{1}{\sqrt{x}-1}, x \neq 1$
; $\quad g(x)=\left(x^{2}+1\right)^{2}$
(iv) $f(x)=3 x^{4}-2 x^{2}$
; $\quad g(x)=\frac{2}{\sqrt{x}}, x \neq 0$
2. For the real valued function, $f$ defined below, find
(a) $f^{-1}(x)$
(b) $f^{-1}(-1)$ and verify $f\left(f^{-1}(x)\right)=f^{-1} f(x))=x$
(i) $f(x)=-2 x+8$
(ii) $f(x)=3 x^{2}+7$
(iii) $f(x)=(-x+9)^{3}$
(iv) $f(x)=\frac{2 x+1}{x-1}, x>1$
3. Without finding the inverse, state the domain and range of $f^{-1}$.
(i) $f(x)=\sqrt{x+2}$
(iii) $f(x)=\frac{1}{x+3}, x \neq-3$
(ii) $f(x)=\frac{x-1}{x-4}, x \neq 4$
(iv) $f(x)=(x-5)^{2}, x \geq 5$

## **1.4 LIMIT OF A FUNCTION AND THEOREMS ON LIMITS**

The concept of limit of a function is the basis on which the structure of calculus rests. Before the definition of the limit of a function, it is essential to have a clear understanding of the meaning of the following phrases:

### **1.4.1 Meaning of the Phrase "x approaches zero"**

Suppose a variable *x* assumes in succession a series of values as

$$
1, \frac{1}{2}, \frac{1}{4}, \frac{1}{8}, \frac{1}{16}, \ldots
$$

i.e.,

$$
1, \frac{1}{2}, \frac{1}{2^2}, \frac{1}{2^3}, \frac{1}{2^4}, \ldots, \frac{1}{2^n}
$$

We notice that *x* is becoming smaller and smaller as *n* increases and can be made as small as we please by taking *n* sufficiently large. This unending decrease of *x* is symbolically written as *x* → 0 and is read as "*x* approaches zero" or "*x* tends to zero".

**Note:** The symbol *x* → 0 is quite different from *x* = 0

- (i) *x* → 0 means that *x* is very close to zero but not actually zero.
- (ii) *x* ≈ 0 means that *x* is actually zero.

### **1.4.2 Meaning of the Phrase "x approaches infinity"**

Suppose a variable *x* assumes in succession a series of values as

$$
1, 10, 100, 1000, 10000, \ldots
$$

i.e.,
1, 10, 10², 10³, 10⁴, 10⁵, 10⁶, 10⁷, 10⁸, 10⁹, 10⁴₋
It is clear that *x* is becoming larger and larger as *n* increases and can be made as large as we please by taking *n* sufficiently large. This unending increase of *x* is symbolically written as "*x* → ∞" and is read as "*x* approaches infinity" or "*x* tends to infinity".

### **1.4.3 Meaning of the Phrase "x approaches α"**

Symbolically it is written as "*x* → *α*" which means that *x* is sufficiently close to but different from the number *α*, from both the left and right sides of *α* i.e., *x* − *α* becomes smaller and smaller as we please but *x* − *α* ≠ 0.

### **1.4.4 Concept of Limit of a Function**

#### **(i) By finding the area of circumscribing regular polygon**

Consider a circle of unit radius which circumscribes a square (4-sided regular polygon) as shown in figure (1).

The side of square is √2 and its area is 2 square unit. It is clear that the area of inscribed 4-sided polygon is less than the area of the circum-circle.

Bisecting the arcs between the vertices of the square, we get an inscribed 8-sided polygon as shown in figure 2. Its area is 2√2 square unit which is closer to the area of circum-circle. A further similar bisection of the arcs gives an inscribed 16-sided polygon as shown in figure (3) with area 3.061 square unit which is more closer to the area of circum-circle.

It follows that as '*n*' , the number of sides of the inscribed polygon increases, the area of polygon increases and becoming nearer to 3.142 which is the area of circle of unit radius i.e.,

$$
\pi^2 = \pi(1)^2 = \pi \approx 3.142.
$$

We express this situation by saying that the limiting value of the area of the inscribed polygon is the area of the circle as *n* approaches infinity, i.e.,

$$
\text{Area of inscribed polygon} \rightarrow \text{Area of circle} \tag{18}
$$

$$
\text{as } n \rightarrow \infty
$$

Thus area of circle of unit radius = π = 3.142 (approx.)

#### **(ii) Numerical Approach**

Consider the function *f*(*x*) = *x*²

The domain of *f*(*x*) is the set of all real numbers. Let us find the limit of *f*(*x*) = *x*² as *x* approaches 2.

The table of values of $f(x)$ for different values of $x$ as $x$ approaches 2 from left and right is as follows:

$$
\text { from left of } 2 \longrightarrow 2 \longleftarrow \text { from right of } 2
$$

| $x$ | 1 | 1.5 | 1.8 | 1.9 | 1.99 | 1.999 | 1.9999 | 2.0001 | 2.001 | 2.01 | 2.1 | 2.2 | 2.5 | 3 |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| $f(x)=a^{2}$ | 1 | 3.375 | 5.832 | 6.859 | 7.8806 | 7.988 | 7.9988 | 8.0012 | 8.012 | 8.1206 | 9.261 | 10.648 | 15.625 | 27 |

The table shows that, as $x$ gets closer and closer to 2 (sufficiently close to 2 ), from both sides, $f(x)$ gets closer and closer to 8 .

We say that 8 is the limit of $f(x)$ when $x$ approaches 2 and is written as:

$$
f(x) \rightarrow 8 \text { as } x \rightarrow 2 \quad \text { or } \quad \lim _{x \rightarrow 2}\left(x^{2}\right)=8
$$

### 1.4.5 Limit of a Function

Let a function $f(x)$ be defined in an open interval near the number " $a$ " (need not be at $a$ ).

If, as $x$ approaches " $a$ " from both left and right side of " $a$ ", $f(x)$ approaches a specific number " $L$ " then " $L$ ", is called the limit of $f(x)$ as $x$ approaches $a$.
Symbolically it is written as:

$$
\lim _{x \rightarrow a^{-}} f(x)=\mathrm{L} \text { read as "limit of } f(x) \text {, as } x \rightarrow a \text {, is } L \text { ". }
$$

It is neither desirable nor practicable to find the limit of a function by numerical approach. We must be able to evaluate a limit in some mechanical way. The theorems on limits will serve this purpose. Their proofs will be discussed in higher classes.

### 1.4.6 Theorems on Limits of Functions

Let $f$ and $g$ be two functions, for which $\underline{\operatorname{Lim}} f(x)=\mathrm{L}$ and $\underline{\operatorname{Lim}} \mathrm{g}(x)=\mathrm{M}$, then
Theorem 1: The limit of the sum of two functions is equal to the sum of their limits.

$$
\underline{\operatorname{Lim}}_{x \rightarrow 0}[f(x)+\mathrm{g}(x)]=\underline{\operatorname{Lim}}_{x \rightarrow 0} f(x)+\underline{\operatorname{Lim}}_{x \rightarrow 0} \mathrm{~g}(x)=\mathrm{L}+\mathrm{M}
$$

For example, $\quad \underline{\operatorname{Lim}}_{x \rightarrow 0}(x+5)=\underline{\operatorname{Lim}}_{x \rightarrow 0} x+\underline{\operatorname{Lim}}_{x \rightarrow 0} 5=1+5=6$

## Theorem 2: The limit of the difference of two functions is equal to the difference of their limits.

$$
\underline{\operatorname{Lim}}_{x \rightarrow 0}[f(x)-\mathrm{g}(x)]=\underline{\operatorname{Lim}}_{x \rightarrow 0} f(x)-\underline{\operatorname{Lim}}_{x \rightarrow 0} \mathrm{~g}(x)=\mathrm{L}-\mathrm{M}
$$

For example, $\quad \underline{\operatorname{Lim}}_{x \rightarrow 0}(x-5)=\underline{\operatorname{Lim}}_{x \rightarrow 0} x-\underline{\operatorname{Lim}}_{x \rightarrow 0} 5=3-5=-2$
Theorem 3: If $k$ is any real number, then

$$
\underline{\operatorname{Lim}}_{k \rightarrow k}[k f(x)]=k \underline{\operatorname{Lim}}_{k \rightarrow k} f(x)=k L
$$

For example: $\quad \underline{\operatorname{Lim}}_{k \rightarrow 0}(3 x)=3 \underline{\operatorname{Lim}}_{k \rightarrow 0}(x)=3(2)=6$
Theorem 4: The limit of the product of the functions is equal to the product of their limits.

$$
\underline{\operatorname{Lim}}_{x \rightarrow 0}[f(x) \mathrm{g}(x)]=\left[\underline{\operatorname{Lim}}_{x \rightarrow 0} f(x)\right]\left[\underline{\operatorname{Lim}}_{x \rightarrow 0} \mathrm{~g}(x)\right]=\mathrm{LM}
$$

For example: $\quad \underline{\operatorname{Lim}}_{x \rightarrow 0}(2 x)(x+4)=\left[\underline{\operatorname{Lim}}_{x \rightarrow 0}(2 x)\right]\left[\underline{\operatorname{Lim}}_{x \rightarrow 0}(x+4)\right]=(2)(5)=10$
Theorem 5: The limit of the quotient of the functions is equal to the quotient of their limits provided the limit of the denominator is non-zero.

$$
\underline{\operatorname{Lim}}_{x \rightarrow 0}\left(\frac{f(x)}{\mathrm{g}(x)}\right)=\frac{\underline{\operatorname{Lim}}_{x \rightarrow 0} f(x)}{\underline{\operatorname{Lim}}_{x \rightarrow 0} \mathrm{~g}(x)}=\frac{\mathrm{L}}{\mathrm{M}}, \quad \mathrm{~g}(x) \neq 0, \mathrm{M} \neq 0
$$

For example: $\quad \underline{\operatorname{Lim}}_{x \rightarrow 0}\left(\frac{3 x+4}{x+3}\right)=\frac{\underline{\operatorname{Lim}}_{x \rightarrow 0}(3 x+4)}{\underline{\operatorname{Lim}}_{x \rightarrow 0}(x+3)}=\frac{6+4}{2+3}=\frac{10}{5}=2$
Theorem 6: Limit of $[f(x)]^{\prime \prime}$, where $\mathbf{n}$ is an integer

$$
\underline{\operatorname{Lim}}_{x \rightarrow 0}[f(x)]^{\prime \prime}=\left(\underline{\operatorname{Lim}}_{x \rightarrow 0} f(x)\right)^{\prime \prime}=\mathrm{L}
$$

For example: $\quad \underline{\operatorname{Lim}}_{x \rightarrow 0}(2 x-3)^{2}=\left(\underline{\operatorname{Lim}}_{x \rightarrow 0}(2 x-3)\right)^{2}=(5)^{2}=125$
We conclude from the theorems on limits that limits are evaluated by merely substituting the number that $x$ approaches into the function.

Example: If $P(x)=\sigma_{n} x^{n}+\sigma_{n-1} x^{n-1}+\ldots .+\sigma_{1} x+\sigma_{0}$ is a polynomial function of degree $n$, then show that $\quad \underline{\operatorname{Lim}} P(x)=P(c)$

Solution: Using the theorems on limits, we have

$$
\begin{aligned}
= & \underline{\operatorname{Lim}} P(x) \quad \underline{\operatorname{Lim}}\left(a_{n} x^{n} \quad a_{n-1} x^{0,1}+\ldots . \quad a_{1} x+a_{0}\right. \\
& =a_{1} \underline{\operatorname{Lim}} x^{n}+a_{n-1} \underline{\operatorname{Lim}} x^{n-1}+\ldots .+a_{1} \underline{\operatorname{Lim}} x+\underline{\operatorname{Lim}} a_{0} \\
& =a_{n} \mathrm{e}^{n}+a_{n-1} \mathrm{e}^{n-1}+\ldots .+a_{1} c+a_{0} \\
\therefore & \underline{\operatorname{Lim}} P(x)=P(c)
\end{aligned}
$$

### 1.5 LIMITS OF IMPORTANT FUNCTIONS

If, by substituting the number that $x$ approaches into the function, we get $\binom{0}{0}$, then we evaluate the limit as follows:

We simplify the given function by using algebraic technique of making factors if possible and cancel the common factors. The method is explained in the following important limits.

### 1.5.1 $\quad \underline{\operatorname{Lim}} \frac{x^{n}-a^{n}}{x-a}=n a^{n-1}$ where $n$ is an integer and $a>0$

Case 1: Suppose $n$ is a positive integer.
By substituting $x=a$, we get $\binom{0}{0}$ form. So we make factors as follows:

$$
x^{n}-a^{n}=(x-a)\left(x^{n-1}+a x^{n-2}+a^{2} x^{n-2}+\ldots .+a^{n-1}\right)
$$

$\therefore \quad \underline{\operatorname{Lim}} \frac{x^{n}-a^{n}}{x-a}=\underline{\operatorname{Lim}} \frac{(x-a)\left(a x^{n-1}+a x^{n-2} a^{2} x^{n-2}+\ldots .+a^{n-1}\right)}{x-a}$
$=\underline{\operatorname{Lim}}\left(x^{n-1}+a x^{n-2}+a^{2} x^{n-2}+\ldots .+a^{n-1}\right)$ (polynomial function)
$=a^{n-1}+a . a^{n-2}+a^{2} . a^{n-2}+\ldots .+a^{n-1}$
$=a^{n-1}+a^{n-1}+a^{n-1}+\ldots .+a^{n-1} \quad(n$ terms)
$=n a^{n-1}$

Case II: Suppose $n$ is a negative integer (say $n=-m$ ), where $m$ is a positive integer.

$$
\begin{aligned}
& \text { Now } \frac{x^{n}-\mathrm{a}^{n}}{x-\mathrm{a}}=\frac{x^{-n}-\mathrm{a}^{-n}}{x-\mathrm{a}} \\
& =\frac{-1}{x^{m} \mathrm{a}^{m}}\left(\frac{x^{m}-\mathrm{a}^{m}}{x-\mathrm{a}}\right) \quad(\mathrm{a} \neq 0) \\
& \therefore \quad \underline{\operatorname{Lim}} \frac{x^{n}-\mathrm{a}^{n}}{x-\mathrm{a}}=\underline{\operatorname{Lim}}\left(\frac{-1}{x^{m} \mathrm{a}^{m}}\right)\left(\frac{x^{m}-\mathrm{a}^{m}}{x-\mathrm{a}}\right) \\
& =\frac{-1}{a^{m} \mathrm{a}^{m}} \cdot\left(m a^{m-1}\right), \quad \quad \text { (By case 1) } \\
& =-m a^{-m-1} \\
& \therefore \quad \underline{\operatorname{Lim}} \frac{x^{n}-\mathrm{a}^{n}}{x-\mathrm{a}}=\mathrm{na}^{n-1} \quad(\mathrm{n}=-\mathrm{m})
\end{aligned}
$$

1.5.2 $\quad \underline{\operatorname{Lim}} \sqrt{\overline{+a}} \sqrt{a}=\frac{\sqrt{a}}{}$

By substituting $x=0$, we have $\binom{0}{0}$ form, so rationalizing the numerator.

$$
\begin{aligned}
\therefore \quad \underline{\operatorname{Lim}} \frac{\sqrt{x+a} \sqrt{a}}{x} & =\underline{\operatorname{Lim}} \frac{\sqrt{x+a} \sqrt{a}}{x}\left(\frac{\sqrt{x+a} \sqrt{a}}{x}\right)\left(\frac{\sqrt{x+a} \sqrt{a}}{\sqrt{x+a} \sqrt{a}}\right) \\
& =\underline{\operatorname{Lim}} \frac{x+a-a}{x(\sqrt{x+a}+\sqrt{a})} \\
& =\underline{\operatorname{Lim}} \frac{x}{x(\sqrt{x+a}+\sqrt{a})} \\
& =\underline{\operatorname{Lim}} \frac{1}{\sqrt{x+a}+\sqrt{a}} \\
& =\frac{1}{\sqrt{a}+\sqrt{a}}=\frac{1}{2 \sqrt{a}}
\end{aligned}
$$

Example 1: Evaluate
(i) $\quad \underline{L i m}_{\varepsilon \rightarrow 0} \frac{x^{2}-1}{x^{2}-x}$
(ii) $\quad \underline{L i m}_{\varepsilon \rightarrow 0} \frac{x-3}{\sqrt{x}-\sqrt{3}}$

Solution: (i) $\quad \underline{L i m}_{\varepsilon \rightarrow 0} \frac{x^{2}-1}{x^{2}-x} \quad\left(\frac{0}{0}\right)$ form (By making factors)
$\therefore \quad \underline{L i m}_{\varepsilon \rightarrow 0} \frac{x^{2}-1}{x^{2}-x}=\underline{L i m}_{\varepsilon \rightarrow 0} \frac{(x-1)(x+1)}{x(x-1)}=\underline{L i m}_{\varepsilon \rightarrow 0} \frac{x+1}{x}=\frac{1+1}{1}=2$
(ii) $\quad \underline{L i m}_{\varepsilon \rightarrow 0} \frac{x-3}{\sqrt{x}-\sqrt{3}}\left(\frac{0}{0}\right)$ form (By making factors of $x-3$ )
$\therefore \quad \underline{L i m}_{\varepsilon \rightarrow 0} \frac{x-3}{\sqrt{x}-\sqrt{3}}=\underline{L i m}_{\varepsilon \rightarrow 0} \frac{(\sqrt{x}+\sqrt{3}) /(\sqrt{x}-\sqrt{3})}{\sqrt{x}-\sqrt{3}}$

$$
\begin{aligned}
& =\underline{L i m}_{\varepsilon \rightarrow 0}(\sqrt{x}+\sqrt{3}) \\
& =(\sqrt{3}+\sqrt{3}) \\
& =2 \sqrt{3}
\end{aligned}
$$

### 1.5.3 Limit at Infinity

We have studied the limits of the functions $f(x), f(x) g(x)$ and $\frac{f(x)}{g(x)}$ when $x \rightarrow \mathrm{c}$ (a number)
Let us see what happens to the limit of the function $f(x)$ if c is $+\infty$ or $-\infty$ (limits at infinity) i.e. when $x \rightarrow+\infty$ and $x \rightarrow-\infty$.
(a) Limit as $x \rightarrow+\infty$

Let $f(x)=\frac{1}{x}$, when $x \neq 0$
This function has the property that the value of $f(x)$ can be made as close as we please to zero when the number $x$ is sufficiently large.

We express this phenomenon by writing $\underline{L i m}_{\varepsilon \rightarrow 0} \frac{1}{x}=0$
(b) Limit as $x \rightarrow-\infty$. This type of limits are handled in the same way as limits as $x \rightarrow+\infty$.
i.e. $\quad \underline{L i m}_{\varepsilon \rightarrow-\infty} \frac{1}{x}=0$, where $x \neq 0$

The following theorem is useful for evaluating limit at infinity.
Theorem: Let $p$ be a positive rational number. If $x^{p}$ is defined, then

$$
\underline{L i m}_{\varepsilon \rightarrow+\infty} \frac{a}{x^{p}}=0 \text { and } \underline{L i m}_{\varepsilon \rightarrow-\infty} \frac{a}{x^{p}}=0 \text {, where } a \text { is any real number. }
$$

For example, $\quad \underline{L i m}_{\varepsilon \rightarrow+\infty} \frac{6}{x^{3}}=0, \underline{L i m}_{\varepsilon \rightarrow-\infty} \frac{-5}{\sqrt{x}}=\underline{L i m}_{\varepsilon \rightarrow-\infty} \frac{-5}{x^{1 / 2}}=0$

$$
\text { and } \quad \underline{L i m}_{\varepsilon \rightarrow+\infty} \frac{1}{\sqrt[3]{x}}=\underline{L i m}_{\varepsilon \rightarrow+\infty} \frac{1}{x^{3}}=0
$$

### 1.5.4 Method for Evaluating the Limits at Infinity

In this case we first divide each term of both the numerator and the denominator by the highest power of $x$ that appears in the denominator and then use the above theorem.

Example 2: Evaluate $\underline{L i m}_{\varepsilon \rightarrow+\infty} \frac{5 x^{4}-10 x^{2}+1}{-3 x^{3}+10 x^{2}+50}$
Solution: $\quad$ Dividing up and down by $x^{3}$, we get

$$
\underline{L i m}_{\varepsilon \rightarrow+\infty} \frac{5 x^{4}-10 x^{2}+1}{-3^{3}+10 x^{2}+50}=\underline{L i}_{\varepsilon \rightarrow+\infty} \frac{5 x-10 / x+1 / x^{2}}{-3+10 / x+50 / 2}=\frac{\infty-0+0}{-3+0+0}=\infty
$$

Example 3: Evaluate $\underline{L i m}_{\varepsilon \rightarrow-\infty} \frac{4 x^{4}-5 x^{3}}{3 x^{2}+2 x^{2}+1}$
Solution: Since $x<0$, so dividing up and down by $(-x)^{3}=-x^{3}$, we get

$$
\underline{L i m}_{\varepsilon \rightarrow-\infty} \frac{4 x^{4}-5 x^{3}}{3 x^{2}+2 x^{2}+1}=\underline{L i m}_{\varepsilon \rightarrow-\infty} \frac{-4 / x+5 / x^{2}}{-3-2 / x^{2}-1 / x^{2}}=\frac{0+0}{-3-0-0}=0
$$

Example 4: Evaluate
(i) $\lim _{x \rightarrow \infty} \frac{2-3 x}{\sqrt{3+4 x^{2}}}$
(ii) $\quad \lim _{x \rightarrow \infty} \frac{2-3 x}{\sqrt{3+4 x^{2}}}$

Solution: (i) Here $\sqrt{x^{2}}=|x|=\infty$ as $x<0$
$\therefore \quad$ Dividing up and down by $-x$, we get
$\lim _{x \rightarrow \infty} \frac{2-3 x}{\sqrt{3+4 x^{2}}}=\lim _{x \rightarrow \infty} \frac{-2 / x+3}{\sqrt{3 / x^{2}+4}}=\frac{0+3}{\sqrt{0+4}}=\frac{3}{2}$
(ii) Here $\sqrt{x}=| |=x$ as $x>0$
$\therefore \quad$ Dividing up and down by $x$, we get
$\lim _{x \rightarrow \infty} \frac{2-3 x}{\sqrt{3+4 x^{2}}}=\lim _{x \rightarrow \infty} \frac{2 / x+3}{\sqrt{3 / x^{2}+4}}=\frac{0-3}{\sqrt{0+4}}=\frac{-3}{2}$
$1.5 .5 \quad \lim _{n \rightarrow+\infty}\left(1+\frac{1}{n}\right)^{n}=\mathrm{e}$.

By the Binomial theorem, we have

$$
\begin{aligned}
& \left(1+\frac{1}{n}\right)^{n}=1+n\left(\frac{1}{n}\right)+\frac{n(n-1)}{2!}\left(\frac{1}{n}\right)^{2}+\frac{n(n-1)(n-2)}{3!}\left(\frac{1}{n}\right)^{3}+\ldots \\
& =1+1+\frac{1}{2!}\left(1-\frac{1}{n}\right)+\frac{1}{3!}\left(1-\frac{1}{n}\right)\left(1-\frac{2}{n}\right)+\ldots \\
& \text { when } \mathrm{n} \longrightarrow \infty, \frac{1}{n} \cdot \frac{2}{n} \cdot \frac{3}{n} \cdot \ldots \text { all tend to zero. } \\
& \therefore \lim _{n \rightarrow \infty}\left(1+\frac{1}{n}\right)^{n}=1+1+\frac{1}{2!}+\frac{1}{3!}+\frac{1}{4!}+\frac{1}{5!}+\ldots \\
& =1+1+0.5+0.166667+0.0416667+\ldots=2.718281 \ldots
\end{aligned}
$$

As approximate value of $e$ is $=2.718281$.
$\therefore \lim _{x \rightarrow+\infty}\left(1+\frac{1}{n}\right)^{n}=\mathrm{e}$.
version: 1.1

Deduction $\lim _{x \rightarrow 0}(1+x)^{1 / x}=e$
We know that $\lim _{x \rightarrow \infty}\left(1+\frac{1}{n}\right)^{n}=\mathrm{e}$
put $\mathrm{n}=\frac{1}{x}$, then $\frac{1}{\mathrm{n}}=x \quad$ in (i)

When $x \rightarrow 0, \mathrm{n} \rightarrow \infty$
$A x \quad \lim _{x \rightarrow \infty}\left(1+\frac{1}{n}\right)^{x}=\mathrm{e}$
$\therefore \quad \lim _{x \rightarrow 0}(1+x)^{1 / x}=\mathrm{e}$
1.5.6 $\quad \lim _{x \rightarrow 0} \frac{a^{x}-1}{x}=\log _{e} a$

$$
\begin{aligned}
& \text { Put } a^{x}-1=y \\
& \text { then } a^{x}=1+y \\
& \text { So } \quad x=\log _{a}(1+y) \\
& \text { From (i) when } x \rightarrow 0, y \rightarrow 0
\end{aligned}
$$

$$
\begin{aligned}
\therefore \lim _{x \rightarrow 0} \frac{a^{x}-1}{x} & =\lim _{y \rightarrow 0} \frac{y}{\log _{a}(1+y)}=\lim _{y \rightarrow 0} \frac{1}{\frac{1}{\log _{a}(1+y)}} \\
& =\lim _{y \rightarrow 0} \frac{1}{\log _{a}(1+y)^{1 / y}}=\frac{1}{\log _{a} e}=\log _{e} a \quad\left(\sqrt{\frac{\lim }{y \rightarrow 0}}(1+y)^{1 / y}=\mathrm{e}\right)
\end{aligned}
$$

Deduction $\lim _{x \rightarrow 0}\left(\frac{e^{x}-1}{x}\right)=\log _{e} e=1$.
We know that $\lim _{x \rightarrow 0} \frac{a^{x}-1}{x}=\log _{e} a$

Put $a \equiv e$ in (1), we have
$\underline{\operatorname{Lim}} \frac{e^{x}-1}{x}=\log _{e} e=1$.

## Important Results to Remember

(i) $\operatorname{Lim}_{x \rightarrow \infty}\left(e^{x}\right)=\infty$
(ii) $\operatorname{Lim}_{x \rightarrow-\infty}\left(e^{x}\right)=\operatorname{Lim}_{x \rightarrow-\infty}\left(\frac{1}{e^{-x}}\right)=0$,
(iii) $\operatorname{Lim}_{x \rightarrow \infty}\left(\frac{a}{x}\right)=0$, where $a$ is any real number.

Example 5: Express each limit in terms of the number ' $e$ '
(a) $\operatorname{Lim}_{x \rightarrow \infty}\left(1+\frac{3}{n}\right)^{2 n}$
(b) $\operatorname{Lim}_{x \rightarrow \infty}(1+2 h)^{\frac{3}{n}}$

Solution: (a) Observe the resemblance of the limit with

$$
\begin{aligned}
& \operatorname{Lim}_{x \rightarrow \infty}\left(1+\frac{1}{n}\right)^{n}=\mathrm{e} \\
& \left(1+\frac{3}{n}\right)^{2 n}=\left[\left(1+\frac{3}{n}\right)^{\frac{n}{2}}\right]^{n}=\left[\left(1+\frac{1}{n / 3}\right)^{\frac{n}{2}}\right]^{n} \\
& \therefore \quad \operatorname{Lim}_{n \rightarrow \infty}\left(1+\frac{3}{n}\right)^{2 n}=\operatorname{Lim}_{n \rightarrow \infty}\left[\left(1+\frac{1}{m}\right)^{m}\right]^{n}=e^{n} \quad\left(\begin{array}{c}
\text { put } m=n / 3 \\
\text { when } n \rightarrow \infty, \\
m \rightarrow \infty
\end{array}\right)
\end{aligned}
$$

(b) Observe the resemblance of the limit with $\operatorname{Lim}_{x \rightarrow 0}(1+x)^{\frac{1}{n}}=\mathrm{e}$,

$$
\begin{aligned}
\therefore \operatorname{Lim}_{n \rightarrow 0}(1+2 h)^{\frac{3}{n}} & =\operatorname{Lim}_{x \rightarrow 0}\left[(1+2 h)^{\frac{3}{2 n}}\right]^{\frac{n}{2}} \quad(\text { put } m=2 h, \text { when } h \rightarrow 0, m \rightarrow 0 \\
& =\operatorname{Lim}_{m \rightarrow 0}\left[(1+m)^{\frac{1}{m}}\right]^{\frac{1}{n}}=e^{2}
\end{aligned}
$$

version: 1.1

### 1.5.7 The Sandwitch Theorem

Let $f, g$ and $h$ be functions such that $f(x) \leq g(x) \leq h(x)$ for all numbers $x$ in some open interval containing "c", except possibly at $c$ itself.

$$
\text { If } \quad \operatorname{Lim}_{x \rightarrow c} f(x)=L \text { and } \quad \operatorname{Lim}_{x \rightarrow c} h(x)=L, \text { then } \quad \operatorname{Lim}_{x \rightarrow c} g(x)=L
$$

Many limit problems arise that cannot be directly evaluated by algebraic techniques. They require geometric arguments, so we evaluate an important theorem.

### 1.5.8 If $\theta$ is measured in radian, then $\operatorname{Lim}_{\theta} \frac{\sin \theta}{\theta}=1$

Proof: To evaluate this limit, we apply a new technique. Take $\theta$ a positive acute central angle of a circle with radius $r=1$. As shown in the figure, $O A B$ represents a sector of the circle.

Given $|O A|=|O B|=1$
(radii of unit circle)
$\therefore \ln \pi \Delta O C B, \sin \theta=\frac{|B C|}{|O B|}=|B C| \quad(\because|O B|=1)$
$\ln \pi \Delta O A D, \tan \theta=\frac{|A D|}{|O A|}=|A D| \quad(\because|O A|=1)$
In terms of $\theta$, the areas are expressed as:
Produce OB to $\mathbf{D}$ so that $\mathbf{A D} \perp$ OA. Draw $\mathbf{B C} \perp$ OA. Join $\mathbf{A B}$
(i) Area of $\Delta O A B=\frac{1}{2}|O A||B C|=\frac{1}{2}(1)(\sin \theta)=\frac{1}{2} \sin \theta$
(ii) Area of sector $O A B=\frac{1}{2} r^{2} \theta=\frac{1}{2}(1)(\theta)=\frac{1}{2} \theta \quad(\because \tau=1)$
and (iii) Area of $\Delta O A D=\frac{1}{2}|O A||A D|=\frac{1}{2}(1)(\tan \theta)=\frac{1}{2} \tan \theta$

From the figure we see that
Area of $\triangle O A B<$ Area of sector $O A B<$ Area of $\triangle O A D$

$$
\Rightarrow \quad \frac{1}{2} \sin \theta<\frac{\theta}{2}<\frac{1}{2} \tan \theta
$$

As $\sin \theta$ is positive, so on division by $\frac{1}{2} \sin \theta$, we get

$$
\begin{aligned}
& 1<\frac{\theta}{\sin \theta}<\frac{1}{\cos \theta} \quad\left(0<\theta<\frac{\pi}{2}\right) \\
& \text { i.e., } \quad 1>\frac{\sin \theta}{\theta}>\cos \theta \quad \text { or } \quad \cos \theta<\frac{\sin \theta}{\theta}<1 \\
& \text { when } \theta \rightarrow 0, \cos \theta \rightarrow 1
\end{aligned}
$$

Since $\frac{\sin \theta}{\theta}$ is sandwitched between 1 and a quantity approaching 1 itself.
So, by the sandwitch theorem, it must also approach 1.
i.e., $\lim _{\theta \rightarrow 0} \frac{\sin \theta}{\theta}=1$

Note: The same result holds for $-\pi / 2<\theta<\theta$
Example 6: $\quad$ Evaluate: $\lim _{\theta \rightarrow 0} \frac{\sin 7 \theta}{\theta}$
Solution: Observe the resemblance of the limit with $\lim _{\theta \rightarrow 0} \frac{\sin \theta}{\theta}=1$
Let $\quad x=7 \theta \quad$ so that $\theta=x / 7$
when $\theta \rightarrow 0 \quad, \quad$ we have $x \rightarrow 0$
$\therefore \quad \lim _{\theta \rightarrow 0} \frac{\sin 7 \theta}{\theta}=\lim _{\theta \rightarrow 0} \frac{\sin x}{x / 7}=7 \lim _{\theta \rightarrow 0} \frac{\sin x}{x}=(7)(1)=7$
Example 7: $\quad$ Evaluate: $\lim _{\theta \rightarrow 0} \frac{1-\cos \theta}{\theta}$
Solution: $\frac{1-\cos \theta}{\theta}=\frac{1-\cos \theta}{\theta} \frac{1+\cos \theta}{1+\cos \theta}$

$$
=\frac{1-\cos ^{2} \theta}{\theta(1+\cos \theta})=\frac{\sin ^{2} \theta}{\theta(1+\cos \theta})=\sin \theta\left(\frac{\sin \theta}{\theta}\right)\left(\frac{1}{1+\cos \theta}\right)
$$

$\therefore \quad \lim _{\theta \rightarrow 0} \frac{1-\cos \theta}{\theta}=\lim _{\theta \rightarrow 0} \sin \theta \lim _{\theta \rightarrow 0} \frac{\sin \theta}{\theta} \lim _{\theta \rightarrow 0} \frac{1}{1+\cos \theta}$

$$
\begin{aligned}
& =(0)(1) \frac{1}{1+1} \\
& =(0)
\end{aligned}
$$

## EXERCISE 1.3

1. Evaluate each limit by using theorems of limits:
(i) $\lim _{x \rightarrow 3^{-}}(2 x+4)$
(ii) $\lim _{x \rightarrow 3^{-}}\left(3 x^{2}-2 x+4\right)$
(iii) $\lim _{x \rightarrow 3^{-}} \sqrt{x^{2}+x+4}$
(iv) $\lim _{x \rightarrow 3^{-}} \sqrt{x^{2}-4}$
(v) $\lim _{x \rightarrow 3^{-}}\left(\sqrt{x^{2}+1}-\sqrt{x^{2}+5}\right)$
(vi) $\lim _{x \rightarrow 3^{-}} \frac{2 x^{3}+5 x}{3 x-2}$
2. Evaluate each limit by using algebraic techniques.
(i) $\lim _{x \rightarrow 3^{-}} \frac{x^{3}-x}{x+1}$
(ii) $\lim _{x \rightarrow 0^{-}}\left(\frac{3 x^{3}+4 x}{x^{2}+x}\right)$
(iii) $\lim _{x \rightarrow 0^{-}} \frac{x^{3}-8}{x^{2}+x-6}$
(iv) $\lim _{x \rightarrow 3^{-}} \frac{x^{3}-3 x^{2}+3 x-1}{x^{3}-x}$
(v) $\lim _{x \rightarrow 0^{-}}\left(\frac{x^{3}+x^{2}}{x^{2}-1}\right)$
(vi) $\lim _{x \rightarrow 0^{-}} \frac{2 x^{3}-32}{x^{2}-4 x^{2}}$
(vii) $\lim _{x \rightarrow 0^{-}} \frac{\sqrt{x}-\sqrt{2}}{x-2}$
(viii) $\lim _{x \rightarrow 0^{-}} \frac{\sqrt{x+h}-\sqrt{x}}{h}$
(ix) $\lim _{x \rightarrow 0^{-}} \frac{x^{n}-a^{n}}{x^{m}-a^{m}}$
3. Evaluate the following limits
(i) $\lim _{x \rightarrow 0^{-}} \frac{\sin 7 x}{x}$
(ii) $\lim _{x \rightarrow 0^{-}} \frac{\sin x^{n}}{x}$
(iii) $\lim _{x \rightarrow 0^{-}} \frac{1-\cos \theta}{\sin \theta}$
(iv) $\lim _{x \rightarrow 0^{-}} \frac{\sin x}{\pi-x}$
(v) $\lim _{x \rightarrow 0^{-}} \frac{\sin a x}{\sinh x}$
(vi) $\lim _{x \rightarrow 0^{-}} \frac{-\pi}{\tan x}$
(vii) $\lim _{x \rightarrow 0^{-}} \frac{1-\cos 2 x}{x^{2}}$
(viii) $\lim _{x \rightarrow 0^{-}} \frac{1-\cos x}{\sin ^{2} x}$
(ix) $\lim _{\theta \rightarrow 0^{-}} \frac{\sin ^{2} \theta}{\theta}$
(x) $\lim _{x \rightarrow 0^{-}} \frac{\sec x-\cos x}{x}$
(xi) $\lim _{\theta \rightarrow 0^{-}} \frac{1-\cos p \theta}{1-\cos q \theta}$
(xii) $\lim _{\theta \rightarrow 0^{-}} \frac{\tan \theta-\sin \theta}{\sin ^{2} \theta}$
4. Express each limit in terms of $e$ :
(i) $\lim _{n \rightarrow \infty}\left(1+\frac{1}{n}\right)^{2 n}$
(ii) $\lim _{n \rightarrow \infty}\left(1+\frac{1}{n}\right)^{\frac{n}{2}}$
(iii) $\lim _{n \rightarrow \infty}\left(1-\frac{1}{n}\right)^{n}$
(iv) $\lim _{n \rightarrow \infty}\left(1+\frac{1}{3 n}\right)^{n}$
(v) $\lim _{n \rightarrow \infty}\left(1+\frac{4}{n}\right)^{n}$
(vi) $\lim _{x \rightarrow 0^{-}}(1+3 x)^{\frac{1}{n}}$

(vii) $\operatorname{Lim}_{x \rightarrow 0}\left(1+2 x^{2}\right)^{\frac{1}{x^{2}}}$
(viii) $\operatorname{Lim}_{x \rightarrow 0}(1-2 h)^{\frac{1}{x}}$
(ix) $\operatorname{Lim}_{x \rightarrow x}\left(\frac{x}{1+x}\right)^{x}$
(x) $\operatorname{Lim}_{x \rightarrow 0} \frac{e^{2 / x}-1}{e^{2 / x}+1} \cdot x<0$
(xi) $\operatorname{Lim}_{x \rightarrow 0} \frac{e^{2 / x}-1}{e^{2 / x}+1} \cdot x>0$

### 1.6 Continuous and Discontinuous Functions

### 1.6.1 One-Sided Limits

In defining $\operatorname{Lim}_{x \rightarrow 0} f(x)$, we restricted $x$ to an open interval containing $c$ i.e., we studied the behavior of $f$ on both sides of $c$. However, in some cases it is necessary to investigate one-sided limits i.e., the left hand limit and the right hand limit.

## (i) The Left Hand Limit

$\operatorname{Lim}_{x \rightarrow 0} f(x)=L$ is read as the limit of $f(x)$ is equal to $L$ as $x$ approaches $c$ from the left i.e., for all $x$ sufficiently close to $c$, but less than $c$, the value of $f(x)$ can be made as close as we please to $L$.

## (ii) The Right Hand Limit

$\operatorname{Lim}_{x \rightarrow 0} f(x)=M$ is read as the limit of $f(x)$ is equal to $M$ as $x$ approaches $c$ from the right i.e., for all $x$ sufficiently close to $c$, but greater than $c$, the value of $f(x)$ can be made as close as we please to $M$.

Note: The rules for calculating the left-hand and the right-hand limits are the same as we studied to calculate limits in the preceding section.

### 1.6.2 Criterion for Existence of Limit of a Function

$$
\operatorname{Lim}_{x \rightarrow c} f(x)=L \quad \text { if and only if } \quad \operatorname{Lim}_{x \rightarrow c} f(x) \quad \operatorname{Lim}_{x \rightarrow c} f(x) \quad L
$$

Example 1: Determine whether $\operatorname{Lim}_{x \rightarrow 0} f(x)$ and $\operatorname{Lim}_{x \rightarrow 0} f(x)$ exist, when

$$
f(x)=\left\{\begin{array}{lll}
2 x+1 & \text { if } & 0 \leq x \leq 2 \\
7-x & \text { if } & 2 \leq x \leq 4 \\
x & \text { if } & 4 \leq x \leq 6
\end{array}\right.
$$

## (i) $\operatorname{Lim}_{x \rightarrow 0} f(x)=\operatorname{Lim}_{x \rightarrow 0}(2 x+1)=4+1=5$

$$
\begin{aligned}
& \operatorname{Lim}_{x \rightarrow 0} f(x)=\operatorname{Lim}_{x \rightarrow 0}(7-x)=7-2=5 \\
& \text { Since } \operatorname{Lim}_{x \rightarrow 0} f(x)=\operatorname{Lim}_{x \rightarrow 0} f(x)=5 \\
& \Rightarrow \operatorname{Lim}_{x \rightarrow 0} f(x) \text { exists and is equal to } 5 \text {. }
\end{aligned}
$$

(ii) $\operatorname{Lim}_{x \rightarrow 0} f(x)=\operatorname{Lim}(7-x)=7-4=3$

$$
\operatorname{Lim}_{x \rightarrow 0} f(x)=\operatorname{Lim}_{x \rightarrow 0}(x)=4
$$

Since $\operatorname{Lim}_{x \rightarrow 0} f(x) \neq \operatorname{Lim}_{x \rightarrow 0} f(x)$
Therefore $\operatorname{Lim}_{x \rightarrow 0} f(x)$ does not exist.
We have seen that sometimes $\operatorname{Lim}_{x \rightarrow 0} f(x) \neq f(c)$ and sometimes it does not and also sometimes $f(c)$ is not even defined whereas $\operatorname{Lim}_{x \rightarrow 0} f(x)$ exists.

### 1.6.3 Continuity of a function at a number

## (a) Continuous Function

A function $f$ is said to be continuous at a number " $c$ " if and only if the following three conditions are satisfied:
(i) $f(c)$ is defined.
(ii) $\operatorname{Lim}_{x \rightarrow c} f(x)$ exists,
(iii) $\operatorname{Lim}_{x \rightarrow c} f(x) \neq f(c)$

## (b) Discontinuous Function

If one or more of these three conditions fail to hold at " $c$ ", then the function $f$ is said to be discontinuous at " $c$ ".

Example 2: Consider the function $f(x)=\frac{x^{2}-1}{x-1}$
Solution: $\quad$ Here $f(1)$ is not defined
$\Rightarrow \quad f(x)$ is discontinuous at 1 .
Further $\quad \lim _{x \rightarrow 1} f(x)=\lim _{x \rightarrow 1} \frac{x^{2}-1}{x-1}=\lim _{x \rightarrow 1}(x+1)=2$ (finite)
Therefore $f(x)$ is continuous at any other number $x \neq 1$
Example 3: $\quad$ For $f(x)=3 x^{2}-5 x+4$, discuss continuity of $f$ at $x=1$

Solution: $\quad \lim _{x \rightarrow 2} f(x)=\lim _{x \rightarrow 2}\left(3 x^{2}-5 x+4\right)=3 \quad=5+4 \quad 2$.
and $f(1)=3-5+4=2$
$\Rightarrow \quad \lim _{x \rightarrow 2} f(x)=f(1)$
$\therefore \quad f(x)$ is continuous at $x=1$
Example 4: $\quad$ Discuss the continuity of the function $f(x)$ and $g(x)$ at $x=3$.
(a) $f(x)= \begin{cases}\frac{x^{2}-9}{x-3} & \text { if } x \neq 3 \\ 6 & \text { if } x=3\end{cases}$
(b) $g(x)=\frac{x^{2}-9}{x-3}$ if $x \neq 3$

Solution: (a) Given $f(3)=6$
$\therefore$ the function $f$ is defined at $x=3$.
Now $\lim _{x \rightarrow 3^{-}} f(x)=\lim _{x \rightarrow 3} \frac{x^{2}-9}{x-3}$

$$
\begin{aligned}
& =\lim _{x \rightarrow 3} \frac{(x+3)(x-3)}{x-3} \\
& =\lim _{x \rightarrow 3}(x+3)=6
\end{aligned}
$$

As $\quad \lim _{x \rightarrow 3^{-}} f(x)=6=f(3)$
$\therefore f(x)$ is continuous at $x=3$

It is noted that there is no break in the graph. (See figure (i))
(b) $g(x)=\frac{x^{2}-9}{x-3}$ if $x \neq 3$

As $g(x)$ is not defined at $x=3$
$\Rightarrow g(x)$ is discontinuous at $x=3 \quad$ (See figure (ii)). It is noted that there is a break in the graph at $x=3$

Example 5: $\quad$ Discuss continuity of $f$ at 3 ,
Fig (ii)
when $f(x)= \begin{cases}x-1, & \text { if } \quad x<3 \\ 2 x+1, & \text { if } \quad 3 \leq x\end{cases}$
Solution: $\quad$ A sketch of the graph of $f$ is shown in the figure (iii). We see that there is a break in the graph at the point when $x=3$

$$
\begin{aligned}
& \text { Now } f(3)=2(3)+1=7 \\
\Rightarrow & \text { Condition (i) is satisfied. } \\
\lim _{x \rightarrow 3^{-}} f(x)=\lim _{x \rightarrow 3^{-}} f(x-1)=3-1=2 \\
\lim _{x \rightarrow 3^{-}} f(x)=\lim _{x \rightarrow 3^{-}} f(2 x+1)=6+1=7 \\
\therefore \quad \lim _{x \rightarrow 3^{-}} f(x) \neq \lim _{x \rightarrow 3^{-}} f(x) \\
& \text { i.e. condition (ii) is not satisfied } \\
\therefore \quad \lim _{x \rightarrow 3^{-}} f(x) \text { does not exist }
\end{aligned}
$$

Hence $f(x)$ is not continuous at $x=3$
Fig (iii)

# EXERCISE 1.4

1. Determine the left hand limit and the right hand limit and then, find the limit of the following functions when $x \rightarrow c$
(i) $f(x)=2 x^{2}+x-5, c=1$
(ii) $f(x)=\frac{x^{2}-9}{x-3}, \quad c=-3$
(iii) $f(x)=|x-5|, \quad c=5$

2. Discuss the continuity of $f(x)$ at $x=c$ :
(i) $f(x)=\left{\begin{array}{cccccc}2 x+5 & \text { if } & x \leq 2 \\ & & & , c=2 \\ 4 x+1 & \text { if } & x & 2\end{array}\right.$
(ii) $f(x)=\left{\begin{array}{cccccc}3 x-1 & \text { if } & x<1 \\ & 4 & \text { if } & x=1, c=1 \\ & 2 x & \text { if } & x>1\end{array}\right.$
3. If $f(x)=\left{\begin{array}{cccccc}3 x & \text { if } & x \leq-2 \\ x^{2}-1 & \text { if } & -2<x<2 \\ & 3 & \text { if } & x \geq 2\end{array}\right.$
Discuss continuity at $x=2$ and $x=-2$
4. If $f(x)=\left{\begin{array}{llllll}x+2 & , & x \leq-1 & \text {, } & \text { find " } c \text { " so that } \frac{\text { Lim }}{c+2}, f(x) \text { exists. } \\ c+2 & , & x>-1\end{array}\right.$
5. Find the values $m$ and $n$, so that given function $f$ is continuous at $x=3$.
(i) $f(x)=\left\{\begin{array}{cccccc}m x & \text { if } & x<3 \\ n & \text { if } & x=3 \\ -2 x+9 & \text { if } & x>3\end{array}\right.$ (ii) $f(x)=\left\{\begin{array}{cccc}m x & \text { if } & x<3 \\ x^{2} & \text { if } & x \geq 3\end{array}\right.$
6. If $f(x)=\left\{\begin{array}{cc}\frac{\sqrt{2 x+5}-\sqrt{x+7}}{x-2}, & x \neq 2 \\ \mathrm{k} & , & x=2\end{array}\right.$

Find value of $k$ so that $f$ is continuous at $x=2$.

# 1.7 Graphs

We now learn the method to draw the graphs of the Explicit Functions like $y=f(x)$, where $f(x)=a^{x}, e^{x}, \log _{a} x$, and $\log _{e} x$.

### 1.7.1 Graph of the Exponential Function $f(x)=a^{x}$

Let us draw the graph of $y=2^{x}$, here $a=2$.
We prepare the following table for different values of $x$ and $f(x)$ near the origin:

| $x$ | -4 | -3 | -2 | -1 | 0 | 1 | 2 | 3 | 4 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| $y=f(x)=2^{x}$ | 0.0625 | 0.125 | 0.25 | 0.5 | 1 | 2 | 4 | 8 | 16 |

Plotting the points $(x, y)$ and joining them with smooth curve as shown in the figure, we get the graph of $y=2^{x}$.

From the graph of $2^{x}$ the characteristics of the graph of $y=a^{x}$ are observed as follows:
If $a>1$, (i) $a^{x}$ is always +ve for all real values of $x$.
(ii) $a^{x}$ increases as $x$ increases.
(iii) $a^{x}=1$ when $x=0$
(iv) $a^{x} \rightarrow 0$ as $x \rightarrow-\infty$
### 1.7.2 Graph of the Exponential Function $f(x)=e^{x}$

As the approximate value of ' $e$ ' is 2.718
The graph of $e^{x}$ has the same characteristics and properties as that of $a^{x}$ when $a>1$ (discussed above).

We prepare the table of some values of $x$ and $f(x)$ near the origin as follows:

|  x | -3 | -2 | -1 | 0 | 1 | 2 | 3  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  y = f(x) = e^x | 0.05 | 0.135 | 0.36 | 1 | 2.718 | 7.38 | 20.07  |

Plotting the points (x, y) and joining them with smooth curve as shown, we get the graph of y = e^x.

### **1.7.3 Graph of Common Logarithmic Function f(x) = lg x.**

If x = 10^x, then y = lg x

Now for all real values of y, 10^x > 0 ⇒ x > 0

This means lg x exists only when x > 0

⇒ Domain of the lg x is +ve real numbers.

**Note:** lg x is undefined at x = 0.

For graph of f(x) = lg x, we find the values of lg x from the common logarithmic table for various values of x > 0.

Table of some of the corresponding values of x and f(x) is as under:

|  x | →0 | 0.1 | 1 | 2 | 4 | 6 | 8 | 10 | →+∞  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  y = f(x) = lg x | →−∞ | -1 | 0 | 0.30 | 0.60 | 0.77 | 0.90 | 1 | →+∞  |

Plotting the points (x, y) and joining them with a smooth curve we get the graph as shown in the figure.

### **1.7.4 Graphs of Natural Logarithmic Function f(x) = ln x:**

The graph of f(x) = ln x has similar properties as that of the graph of f(x) = lg x.

By using the table of natural logarithm for various values of x, we get the graph of y = ln x as shown in the figure.

### **1.7.5 Graphs of Implicit Functions**

**(a) Graph of the circle of the form** x^2 + y^2 = a^2

**Example 1:** Graph the circle x^2 + y^2 = 4

**Solution:** The graph of the equation x^2 + y^2 = 4 is a circle of radius 2, centered at the origin and hence there are vertical lines that cut the graph more than once. This can also be seen algebraically by solving (1) for y in terms of x.

$$y = \pm \sqrt{4 - x^2}$$

The equation does not define y as a function of x.

For example, if x = 1, then y = ±√3.

Hence ((1, √3)) and ((1, −√3)) are two points on the circle and vertical line passes through these two points.

We can regard the circle as the union of two semi-circles.

$$y = \sqrt{4 - x^2} \text{ and } y = -\sqrt{4 - x^2}$$

Each of which defines y as a function of x.

We observe that if we replace (x, y) in turn by (-x, y), (x, −y) and (-x, −y), there is no change in the given equation. Hence the graph is symmetric with respect to the y-axis, x-axis and the origin.

$$x = 0 \text{ implies } y^2 = 4 \Rightarrow y = \pm 2$$

$$x = 1 \text{ implies } y^2 = 3 \Rightarrow y = \pm \sqrt{3}$$

$$x = 2 \text{ implies } y^2 = 0 \Rightarrow y = 0$$

By assigning values of x, we find the values of y. So we prepare a table for some values of x and y satisfying equation (1).

|  x | 0 | 1 | $$\sqrt{3}$$ | 2 | -1 | -$$\sqrt{3}$$ | -2  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  y | ±2 | $$\pm$$\sqrt{3}$$ | ±1 | 0 | $$\pm$$\sqrt{3}$$ | ±1 | 0  |

Plotting the points (x, y) and connecting them with a smooth curve as shown in the figure, we get the graph of a circle.

**(b) The graph of ellipse of the form $$\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$$**

**Example 2:** Graph $$\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$$ i.e., 9x² + 4y² = 36

**Solution:** We observe that if we replace (x, y) in turn by (-x, y), (x, -y) and (-x, -y), there is no change in the given equation. Hence the graph is symmetric with respect to the y-axis, x-axis and the origin.

$$y = 0 \text{ implies } \quad x^2 = 4 \Rightarrow \quad x = \pm 2$$

$$x = 0 \text{ implies } \quad y^2 = 9 \Rightarrow \quad y = \pm 3$$

Therefore x-intercepts are 2 and -2 and y-intercepts are 3 and -3. By assigning values of x, we find the values of y. So we prepare a table for some values of x and y satisfying equation (1).

|  x | 0 | 1 | 2 | -1 | -2  |
| --- | --- | --- | --- | --- | --- |
|  y | ±3 | $$\pm$$\sqrt{\frac{27}{4}}$ | 0 | $$\pm$$\sqrt{\frac{27}{4}}$ | 0  |

Plotting the points (x, y), connecting these points with a smooth curve as shown in the figure, we get the graph of an ellipse.

### 1.7.5 Graph of Parametric Equations

**(a) Graph the curve that has the parametric equations**

$$x = t^2, y = t \quad -2 \leq t \leq 2 \tag{3}$$

**Solution:** For the choice of t in [-2, 2], we prepare a table for some values of x and y satisfying the given equation.

|  t | -2 | -1 | 0 | 1 | 2  |
| --- | --- | --- | --- | --- | --- |
|  x | 4 | 1 | 0 | 1 | 4  |
|  y | -2 | -1 | 0 | 1 | 2  |

We plot the points (x, y), connecting these points with a smooth curve shown in the figure, we obtain the graph of a parabola with equation $$y^2 = x$$.

### 1.7.6 Graphs of Discontinuous Functions

**Example 1:** Graph the function defined by $$y = \begin{cases} x & \text{when } 0 \leq x \leq 1 \ x - 1 & \text{when } 1 < x \leq 2 \end{cases}$$

**Solution:** The domain of the function is 0 ≤ x ≤ 2. For 0 ≤ x ≤ 1, the graph of the function is that of y = x and for 1 < x ≤ 2, the graph of the function is that of y = x - 1.

We prepare the table for some values of x and y in 0 ≤ x ≤ 2 satisfying the equations y = x and y = x - 1.

|  x | 0 | 0.5 | 0.8 | 1 | 1.5 | 1.8 | 2  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  y | 0 | 0.5 | 0.8 | 1 | 0.5 | 0.8 | 1  |

**40**

**41**

Plot the points (*x*, *y*). Connecting these points we get two straight lines, which is the graph of a discontinuous function.

**Example 2:** Graph the function defined by $$y = \frac{x^2 - 9}{x - 3}, \quad x \neq 3$$

**Solution:** The domain of the function consists of all real numbers except 3.

When *x* = 3, both the numerator and denominator are zero, and $$\frac{0}{0}$$ is undefined.

Simplifying we get $$y = \frac{x^2 - 9}{x - 3} = \frac{(x - 3)(x + 3)}{x - 3} = x + 3$$ provided *x* ≠ 3.

We prepare a table for different values of *x* and *y* satisfy the equation $$y = x + 3$$ and *x* ≠ 3.

|  *x* | -3 | -2 | -1 | 0 | 1 | 2 | 2.9 | 3 | 3.1 | 4  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  *Y* | 0 | 1 | 2 | 3 | 4 | 5 | 5.9 | 6 | 6.1 | 7  |

Plot the points (*x*, *y*) and joining these points we get the graph of the function which is a straight line except the point (3, 6).

The graph is shown in the figure. This is a broken straight line with a break at the point (3, 6).

### 1.7.7 Graphical Solution of the Equations

(i) $$\cos x = x$$ (ii) $$\sin x = x$$ (iii) $$\tan x = x$$

We solve the equation $$\cos x = x$$ and leave the other two equations as an exercise for the students.

**Solution:** To find the solution of the equation $$\cos x = x$$, we draw the graphs of the two functions $$y = x$$ and $$y = \cos x$$: $$-\pi \leq x \leq \pi$$

*version: 1.1*

### Scale for graphs

- Along *x*-axis, length of side of small square = $$\frac{\pi}{6}$$ radian
- Along *y*-axis, length of side of small square = 0.1 unit
- Two points (0, 0) and (π/3, 1) lie on the line *y* = *x*

We prepare a table for some values of *x* and *y* in the interval $$-\pi \leq x \leq \pi$$ it satisfies the equation $$y = \cos x$$.

|  *x* | $-\pi$ | -5π/6 | -2π/3 | $-\pi/2$ | $-\pi/3$ | $-\pi/6$ | 0 | $\pi/6$ | $\pi/3$ | $\pi/2$ | 2π/3 | 5π/6 | $\pi$  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  $y = \cos x$ | -1 | -.87 | -.5 | 0 | -.5 | .87 | 1 | .87 | .5 | 0 | -.5 | -.87 | -1  |

The graph shows that the equations $$y = x$$ and $$y = \cos x$$ intersect at only where $$x = \frac{43}{180} \pi$$ radian = 0.73

**Check:** $$\cos \left(\frac{43}{180} \pi\right) = \cos 43^\circ = 0.73$$

# Note: Since the scales along the two axes are different so the line $y=x$ is not equally inclined to both the axes.

## EXERCISE 1.5

1. Draw the graphs of the following equations
(i) $x^{2}+y^{2}=9$
(ii) $\frac{x^{2}}{16}+\frac{y^{2}}{4}=1$
(iii) $y=e^{2 x}$
(iv) $y=3^{x}$
2. Graph the curves that has the parametric equations given below
(i) $x=t, y=t^{2},-3 \leq t \leq 3$
where " $t$ " is a parameter
(ii) $x=t-1, y=2 t-1,-1<t<5$
where " $t$ " is a parameter
(iii) $x=\sec \theta, y=\tan \theta$
where " $\theta$ " is a parameter
3. Draw the graphs of the functions defined below and find whether they are continuous.
(i) $y=\left\{\begin{array}{ll}x-1 & \text { if } x<3 \\ 2 x+1 & \text { if } x \geq 3\end{array}\right.$
(ii) $y=\frac{x^{2}-4}{x-2} \quad x \neq 2$
(iii) $y=\left\{\begin{array}{ll}x+3 & \text { if } x \neq 3 \\ 2 & \text { if } x=3\end{array}\right.$
(iv) $y=\frac{x^{2}-16}{x-4} \quad x \neq 4$
4. Find the graphical solution of the following equations:
(i) $x=\sin 2 x$
(ii) $\frac{x}{2}=\cos x$
(iii) $2 x=\tan x$

CHAPTER
# DIFFERENTIATION

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