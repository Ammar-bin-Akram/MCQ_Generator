# Chapter 1: CHAPTER

## 1

## FUNCTIONS AND LIMITS

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