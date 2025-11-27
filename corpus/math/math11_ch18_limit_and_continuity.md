# Chapter 18: Limit and Continuity

## INTRODUCTION

In mathematics, the concept of limit and continuity is foundational in understanding the behaviour of functions and sequences, especially when applied to real-world scenarios. This unit will introduce and explore how to demonstrate and find the limit of a sequence and a function, understand continuous and discontinuous functions, and apply these concepts in various contexts such as economics, finance, and natural sciences.

### 12.1 Limit of a Function

The concept of limit of a function is the basis on which the structure of calculus rests. Before the definition of the limit of a function, it is necessary to have a clear understanding of the following phrases.

### 12.1.1 Meaning of the Phrase " $x$ approaches zero"

Suppose a sequence $x_{n}=\frac{1}{n^{2}}$ assumes a sequence of values as:

$$
\frac{1}{2}, \frac{1}{2^{2}}, \frac{1}{2^{3}}, \frac{1}{2^{4}} \cdots, \frac{1}{2^{n}}, \cdots
$$

We can see that the sequence $x_{n}=\frac{1}{n^{2}}$ is becoming smaller and smaller as $n$ increases and can be made as small as we please by taking " $n$ " sufficiently large. In other words, $x_{n}=\frac{1}{n^{2}}$ becoming closer and closer to 0 as $n$ becoming large. This unending decrease of $x_{n}$ is denoted by $x_{n} \rightarrow 0$ and read as " $x_{n}$ approaches zero" or " $x_{n}$ tends to zero as $n \rightarrow \infty$. That is, the limit of the sequence $x_{n}$ is 0 .

### 12.1.2 Meaning of the Phrase " $x$ approaches infinity"

Suppose a sequence $x_{n}=10^{n}$ assumes values as $1,10,10^{2}, 10^{3}, \ldots, 10^{n}, \ldots$
It is clear that the sequence $x_{n}$ is becoming larger and larger as $n$ increases and can be made as large as we please by taking $n$ sufficiently large. This unending increase of the sequence $x_{n}$ is symbolically written as " $x_{n} \rightarrow \infty$ " and is read as " $x_{n}$ approaches infinity" or " $x_{n}$ tends to infinity" as $n \rightarrow \infty$

# 12.1.3 Meaning of the Phrase " $x$ approaches $a$ "

Symbolically it is written as " $x \rightarrow a$ " which means that $x$ is sufficiently close to $a$ but different from the number $a$, from both the left and right sides of $a$ that is $x-a$ becomes smaller and smaller as we please but $x-a \neq 0$.

Point to remember:
The symbol $x \rightarrow 0$ is quite different from $x=0$.
$x \rightarrow 0$ means that $x$ is very close to zero but not actually zero.
$x=0$ means that $x$ is actually zero.

### 12.1.4 Concept of Limit of a Function

## (1) By Finding the Area of Circumscribed Regular Polygon

Consider a circle of unit radius which circumscribes a square (4-sided regular polygon) as shown in Figure 12.1.
The side of square is $\sqrt{2}$ and its area is 2 square units. It is clear that the area of inscribed 4 -sided polygon is less than the area of the circum-circle $\pi=3.142\left(\pi r^{2}=\pi(1)^{2}=\pi=3.142\right)$
Figure 12.1: 4 -sided polygon
Figure 12.2: 8 -sided polygon
Figure 12.3:16-sided polygon

Bisecting the arcs between the vertices of the square, we get an inscribed 8 -sided regular polygon as shown in Figure 12.2. Its area is $2 \sqrt{2}=2.828$ square units which is closer to the area of circum-circle. A further similar bisection of the arcs gives an inscribed 16 -sided regular polygon as shown in Figure 12.3 with area 3.061 square units which is more closer to the area of circum-circle.
It follows that as " $n$ ", the number of sides of the inscribed polygon increases, the area of polygon increases and becoming near to 3.142 which is the area of circle of unit radius.

We express this situation by saying that the limiting value of the area of the inscribed polygon is the area of the circle as $n$ approaches infinity, i.e.,

Area of inscribed polygon $\rightarrow$ Area of circle as $n \rightarrow \infty$

# (ii) Numerical Approach

Consider the function $f(x)=x^{3}$
The domain of $f(x)$ is the set of all real numbers.
Let us find the limit of $f(x)=x^{3}$ as $x$ approaches 2 .
The table of values of $f(x)$ for different values of $x$ as $x$ approaches 2 from left and right is as follows:

From left of $2 \longrightarrow 2$ from right of 2

| $x$ | 1 | 1.5 | 1.8 | 1.9 | 1.99 | 1.999 | 1.9999 | 2.0001 | 2.001 | 2.01 | 2.1 | 2.2 | 2.5 | 3 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| $f(x)=x^{3}$ | 1 | 3.375 | 5.832 | 6.859 | 7.8806 | 7.8806 | 7.9988 | 8.0012 | 8.012 | 8.1206 | 9.261 | 10.648 | 15.625 | 27 |

The table shows that, as $x$ gets closer and closer to 2 (sufficiently close to 2 ), from both sides, $f(x)$ gets closer and closer to 8 .
We say that 8 is the limit of $f(x)$ when $x$ approaches 2 and is written as:

$$
f(x) \rightarrow 8 \text { as } x \rightarrow 2 \quad \text { or } \quad \lim _{x \rightarrow 2} x^{2}=8
$$

### 12.1.5 Limit of a Function

Let a function $f(x)$ be defined in an open interval near the number " $a$ " (need not be at a). If, as $x$ approaches " $a$ " from both left and right side of " $a$ " $f(x)$ approaches a specific number "L" then "L", is called the limit of $f(x)$ as $x$ approaches $a$. Symbolically it is written as:
$\lim _{x \rightarrow a} f(x)=\mathrm{L}$ read as "limit of $f(x)$ as $x \rightarrow a$, is $L$ ".
It is neither desirable nor practicable to find the limit of a function by numerical approach. We must be able to evaluate a limit in some mechanical way. The theorems on limits will serve this purpose. Their proofs will be discussed in higher classes.

### 12.1.6 Theorems on Limits of Functions

Let $f$ and $g$ be two functions for which $\operatorname{Lim}_{x \rightarrow a} f(x)=L$ and $\operatorname{Lim}_{x \rightarrow a} g(x)=M$, then
Theorem 1: (i) $\lim _{x \rightarrow a} x^{p}=a^{p}$, where $p>0$ and $p \in R$
(ii) $\lim _{x \rightarrow a} c=c$

Theorem 2: (a) The limit of the sum of two functions is equal to the sum of their limits.

$$
\operatorname{Lim}_{x \rightarrow a}[f(x)+g(x)]=\operatorname{Lim}_{x \rightarrow a} f(x)+\operatorname{Lim}_{x \rightarrow a} g(x)=L+M
$$

For example, $\operatorname{Lim}_{x \rightarrow 1}(x+5)=\operatorname{Lim}_{x \rightarrow 1} x+\operatorname{Lim}_{x \rightarrow 1} 5=1+5=6$

(b) The limit of the difference of two functions is equal to the difference of their limits.

$$
\operatorname{Lim}_{x \rightarrow a}[f(x)-g(x)]=\operatorname{Lim}_{x \rightarrow a} f(x)-\operatorname{Lim}_{x \rightarrow a} g(x)=L-M
$$

For example, $\quad \operatorname{Lim}_{x \rightarrow 3}(x-5)=\operatorname{Lim}_{x \rightarrow 3}(x)-\operatorname{Lim}_{x \rightarrow 3} 5=3-5=-2$
(c) If $k$ is any real number, then

$$
\operatorname{Lim}_{x \rightarrow a}[k f(x)]=k \operatorname{Lim}_{x \rightarrow a} f(x)=k L
$$

For example, $\operatorname{Lim}_{x \rightarrow 2}(3 x)=3 \operatorname{Lim}_{x \rightarrow 2}(x)=3(2)=6$
(d) The limit of the product of the functions is equal to the product of their limits.

$$
\operatorname{Lim}_{x \rightarrow a}[f(x) g(x)]=\operatorname{Lim}_{x \rightarrow a} f(x) \cdot \operatorname{Lim}_{x \rightarrow a} g(x)=L M
$$

For example, $\operatorname{Lim}_{x \rightarrow 1}(2 x)(x+4)=\operatorname{Lim}_{x \rightarrow 1}(2 x) \cdot \operatorname{Lim}_{x \rightarrow 1}(x+4)=(2)(5)=10$
(e) The limit of the quotient of the functions is equal to the quotient of their limits provided the limit of denominator is non-zero.

$$
\begin{aligned}
& \operatorname{Lim}_{x \rightarrow a}\left[\frac{f(x)}{g(x)}\right]=\frac{\operatorname{Lim}_{x \rightarrow a} f(x)}{\operatorname{Lim}_{x \rightarrow a} g(x)}=\frac{L}{M}, \text { provided } g(x) \neq 0 \text { in a neighborhood of } \\
& a \text { and } M \neq 0
\end{aligned}
$$

For example: $\operatorname{Lim}_{x \rightarrow 2}\left[\frac{3 x+4}{x+3}\right]=\frac{\operatorname{Lim}_{x \rightarrow 2}(3 x+4)}{\operatorname{Lim}_{x \rightarrow 2}(x+3)}=\frac{6+4}{2+3}=\frac{10}{5}=2$
(f) Limit of $[f(x)]^{\prime}$, where $n$ is an integer

$$
\operatorname{Lim}_{x \rightarrow a}[f(x)]^{\prime \prime}=\left[\operatorname{Lim}_{x \rightarrow a} f(x)\right]^{\prime \prime}=L^{n}
$$

For example, $\operatorname{Lim}_{x \rightarrow 4}(2 x-3)^{3}=\left(\operatorname{Lim}_{x \rightarrow 4}(2 x-3)\right)^{3}=(5)^{3}=125$
We conclude from the theorems on limits that limits are evaluated by merely substituting the number that $x$ approaches into the function.

# 12.2 Limits of Important Functions

If by substituting the number that $x$ approaches into the function, we get $\binom{0}{0}$, then one possible way to evaluate the limits is as follows:
We simplify the given function by using algebraic techniques of making factors if possible and cancel the common factors. The method explained in the following important limits.

### 12.2.1 $\underline{\operatorname{Lim}} \frac{x^{n}-a^{n}}{x-a}=n a^{n-1}$ where $n$ is a non-zero integer and $a>0$

Case I: Suppose $n$ is a positive integer.
By substituting $x=a$, we get $\binom{0}{0}$ form, so we make factors as follows:

$$
\begin{aligned}
x^{n}-a^{n} & =(x-a)\left(x^{n-1}+a x^{n-2}+a^{2} x^{n-3}+\ldots+a^{n-1}\right) \\
\lim _{x \rightarrow a} \frac{x^{n}-a^{n}}{x-a} & =\lim _{x \rightarrow a} \frac{(x-a)\left(x^{n-1}+a x^{n-2}+a^{2} x^{n-3}+\ldots+a^{n-1}\right)}{x-a} \\
& =\operatorname{Lim}_{x \rightarrow a}\left(x^{n-1}+a x^{n-2}+a^{2} x^{n-3}+\ldots+a^{n-1}\right) \\
& =a^{n-1}+a \quad a^{n-2}+a^{2} a^{n-3}+a^{3} a^{n-4}+\ldots+a^{n-1} \\
& =a^{n-1}+a^{n-1}+a^{n-1}+a^{n-1} \ldots+a^{n-1}=n a^{n-1}
\end{aligned}
$$

Case II: Suppose $n$ is a negative integer (Say $n=-m$ ) where $m$ is a positive integer.

$$
\begin{aligned}
& \text { Now, } \quad \frac{x^{n}-a^{n}}{x-a}=\frac{x^{-n}-a^{-n}}{x-a}=\frac{\frac{1}{x^{m}}-\frac{1}{a^{m}}}{x-a}=\frac{\frac{a^{m}-x^{m}}{x^{n} a^{m}}}{x-a} \\
& \therefore \quad \operatorname{Lim}_{x \rightarrow a} \frac{x^{n}-a^{n}}{x-a}=\operatorname{Lim}_{x \rightarrow a}\left(\frac{-1}{x^{m} a^{m}}\right)\left(\frac{x^{n}-a^{m}}{x-a}\right) \\
& =\frac{-1}{a^{m} a^{m}}\left(m a^{m-1}\right) \quad \text { (by Case }-1 \text { ) } \\
& =-m a^{-m-1} \\
& \therefore \quad \operatorname{Lim}_{x \rightarrow a}\left(\frac{x^{n}-a^{n}}{x-a}\right)=n a^{n-1} \quad \because n=-m
\end{aligned}
$$

# 12.2.2 $\underline{\operatorname{Lim}}_{x \rightarrow 0} \frac{\sqrt{x+a}-\sqrt{a}}{x}=\frac{1}{2 \sqrt{a}}$, where $n$ is an integer and $a>0$.

By substituting $x=0$, we have $\left(\frac{0}{0}\right)$ form, so rationalizing the numerator.

$$
\begin{aligned}
\lim _{x \rightarrow 0} \frac{\sqrt{x+a}-\sqrt{a}}{x} & =\lim _{x \rightarrow 0}\left(\frac{\sqrt{x+a}-\sqrt{a}}{x}\right)\left(\frac{\sqrt{x+a}+\sqrt{a}}{\sqrt{x+a}+\sqrt{a}}\right)=\lim _{x \rightarrow 0} \frac{x+a-a}{x(\sqrt{x+a}+\sqrt{a})} \\
& =\lim _{x \rightarrow 0}\left(\frac{1}{\sqrt{x+a}+\sqrt{a}}\right) \\
& =\lim _{x \rightarrow 0} \frac{1}{\sqrt{x+a}+\sqrt{a}}=\frac{1}{\sqrt{a}+\sqrt{a}}=\frac{1}{2 \sqrt{a}}
\end{aligned}
$$

Example 1 Evaluate: (i) $\quad \lim _{x \rightarrow 1} \frac{x^{2}-1}{x^{2}-x}$
(ii) $\quad \lim _{x \rightarrow 3} \frac{x-3}{\sqrt{x}-\sqrt{3}}$

Solution (i) $\quad \lim _{x \rightarrow 1} \frac{x^{2}-1}{x^{2}-x} \quad\left(\frac{0}{0}\right)$ form.

$$
\begin{aligned}
\lim _{x \rightarrow 1} \frac{x^{2}-1}{x^{2}-x} & =\lim _{x \rightarrow 1} \frac{(x-1)(x+1)}{x(x-1)}=\lim _{x \rightarrow 1} \frac{x+1}{x} \\
& =\frac{1+1}{1}=\frac{2}{1}=2
\end{aligned}
$$

(ii) $\quad \lim _{x \rightarrow 3} \frac{x-3}{\sqrt{x}-\sqrt{3}}=\underline{\operatorname{Lim}}_{x \rightarrow 3} \frac{(\sqrt{x}+\sqrt{3})(\sqrt{x}=\sqrt{3})}{(\sqrt{x}=\sqrt{3})}=\operatorname{Lim}_{x \rightarrow 3}(\sqrt{x}+\sqrt{3})=\sqrt{3}+\sqrt{3}=2 \sqrt{3}$

### 12.2.3 Limit at Infinity

We have studied the limits of the functions $f(x), f(x) . g(x)$ and $\frac{f(x)}{g(x)}$, when $x \rightarrow c$ (a number)
Let us see what happens to the limit of the function $f(x)$ if $c$ is $+\infty$ or $-\infty$ (limits at infinity) i.e., when $x \rightarrow+\infty$ or $x \rightarrow-\infty$.
(a) Limit as $x \rightarrow+\infty$

Let $f(x)=\frac{1}{x}$, when $x \neq 0$
This function has the property that the value of $f(x)$ can be made as close as we please to zero when the number $x$ is sufficiently large.
We express this phenomenon by writing $\operatorname{Lim}_{x \rightarrow \infty} \frac{1}{x}=0$

(b) Limit as $x \rightarrow-\infty$

This type of limits are handled in the same way as limits as $x \rightarrow+\infty$.
i.e., $\operatorname{Lim}_{x \rightarrow-\infty} \frac{1}{x}=0$, where $x \neq 0$.

The following theorem is useful for evaluating limit at infinity.
Theorem: Let $p$ be a positive rational number. If $x^{p}$ is defined, then
$\operatorname{Lim}_{x \rightarrow+\infty} \frac{a}{x^{p}}=0$ and $\operatorname{Lim}_{x \rightarrow-\infty} \frac{a}{x^{p}}=0$, where $a$ is any real number.
For example, $\quad \operatorname{Lim}_{x \rightarrow+\infty} \frac{6}{x^{3}}=0$ and $\operatorname{Lim}_{x \rightarrow+\infty} \frac{-5}{\sqrt[3]{x}}=0$

# 12.2.4 Limit of a Sequence

Let $\left\{a_{n}\right\}$ be a sequence, the limit of a sequence $\left\{a_{n}\right\}$ is the value $L$ that the terms of the sequence approach as $n \rightarrow \infty$, that is,

$$
\operatorname{Lim}_{n \rightarrow \infty} a_{n}=L
$$

If such an $L$ exists, the sequence is said to converge to $L$ and $\left\{a_{n}\right\}$ is called convergent sequence. If no such $L$ exists, the sequence is said to diverge.
For example, consider the sequence $\left\{a_{n}=\frac{1}{n}\right\}$ : As $n \rightarrow \infty, \frac{1}{n} \rightarrow 0$
So, we write $\operatorname{Lim}_{n \rightarrow \infty} a_{n}=\operatorname{Lim}_{n \rightarrow \infty} \frac{1}{n}=0$.
Example 2 Find the limit of the sequence $a_{n}=\frac{2 n+3}{n+1}$.
Solution We can simplify the sequence:

$$
a_{n}=\frac{2 n+3}{n+1}=\frac{n\left(2+\frac{3}{n}\right)}{n\left(1+\frac{1}{n}\right)}=\frac{2+\frac{3}{n}}{1+\frac{1}{n}}
$$

As $n \rightarrow \infty, \frac{3}{n} \rightarrow 0$ and $\frac{1}{n} \rightarrow 0$, so we are left with: $\operatorname{Lim}_{n \rightarrow \infty} a_{n}=\frac{2+0}{1+0}=2$

$$
\text { Thus, } \operatorname{Lim}_{n \rightarrow \infty} \frac{2 n+3}{n+1}=2
$$

Divergent Sequences: A sequence is divergent if it is not convergent. Divergence can occur in the following ways:

- The sequence may increase or decrease without bound (e.g., $a_{n}=n^{2}$ diverges to infinity).
- The sequence may oscillate between different values and not settle near any one value (e.g., $a_{n}=(-1)^{n}$ oscillates between -1 and 1 , so it does not converge).

# 12.2.5 Methods for Evaluating the Limits at Infinity

In this case we first divide each term of both the numerator and the denominator by the highest power of $x$ that appears in the denominator and then use the theorems on limit.

Example 3 Evaluate $\operatorname{Lim}_{x \rightarrow+\infty} \frac{5 x^{4}-10 x^{2}+1}{-3 x^{3}+10 x^{2}+50}$
Solution Dividing numerator and denominator by $x^{3}$, we get
$\operatorname{Lim}_{x \rightarrow+\infty} \frac{5 x^{4}-10 x^{2}+1}{-3 x^{3}+10 x^{2}+50}=\operatorname{Lim}_{x \rightarrow+\infty} \frac{5 x-\frac{10}{x}+\frac{1}{x^{3}}}{-3+\frac{10}{x}+\frac{50}{x^{3}}}=\frac{\infty-0+0}{-3+0+0}=-\infty: \lim _{x \rightarrow \infty} \frac{a}{x^{a}}=0$
Example 4 Evaluate $\operatorname{Lim}_{x \rightarrow-\infty} \frac{4 x^{4}-5 x^{3}}{-3 x^{3}+2 x^{2}+1}$
Solution Dividing numerator and denominator by $x^{2}$, we get

$$
\operatorname{Lim}_{x \rightarrow-\infty} \frac{4 x^{4}-5 x^{3}}{-3 x^{3}+2 x^{2}+1}=\operatorname{Lim}_{x \rightarrow-\infty} \frac{\frac{4}{x}-\frac{5}{x^{2}}}{-3+\frac{2}{x^{3}}+\frac{1}{x^{3}}}=\frac{0-0}{-3+0+0}=0
$$

Example 5 Evaluate:
(i) $\quad \operatorname{Lim}_{x \rightarrow-\infty} \frac{2-3 x}{\sqrt{3}+4 x^{3}}$
(ii) $\quad \operatorname{Lim}_{x \rightarrow+\infty} \frac{2-3 x}{\sqrt{3}+4 x^{2}}$

Solution
(i) Here $\sqrt{x^{2}}=|x|=-x$ as $x<0$
$\therefore \quad$ Dividing numerator and denominator by $-x$, we get

$$
\operatorname{Lim}_{x \rightarrow-\infty} \frac{2-3 x}{\sqrt{3}+4 x^{2}}=\operatorname{Lim}_{x \rightarrow-\infty} \frac{-\frac{2}{x}+3}{\sqrt{\frac{3}{x^{2}}+4}}=\frac{0+3}{\sqrt{0+4}}=\frac{3}{2}
$$

(ii) Here $\sqrt{x^{2}}=|x|=x$ as $x>0$
$\therefore \quad$ Dividing numerator and denominator by $x$, we get

$$
\lim _{x \rightarrow+\infty} \frac{2-3 x}{\sqrt{3+4 x^{2}}}=\operatorname{Lim}_{x \rightarrow+\infty} \frac{\frac{2}{x}-3}{\sqrt{\frac{3}{x^{2}}+4}}=\frac{0-3}{\sqrt{0+4}}=\frac{-3}{2}
$$

12.2.6 $\quad \operatorname{Lim}_{n \rightarrow+\infty}\left(1+\frac{1}{n}\right)^{n}=e$

By the binomial theorem, we have

$$
\begin{aligned}
\left(1+\frac{1}{n}\right)^{n} & =1+n\left(\frac{1}{n}\right)+\frac{n(n-1)}{2!}\left(\frac{1}{n}\right)^{2}+\frac{n(n-1)(n-2)}{3!}\left(\frac{1}{n}\right)^{3}+\ldots \\
& =1+1+\frac{1}{2!}\left(1-\frac{1}{n}\right)+\frac{1}{3!}\left(1-\frac{1}{n}\right)\left(1-\frac{2}{n}\right)+\ldots
\end{aligned}
$$

When $n \rightarrow+\infty, \frac{1}{n}, \frac{2}{n}, \frac{3}{n}, \ldots$ all tends to zero, therefore

$$
\begin{aligned}
\therefore \quad \operatorname{Lim}_{x \rightarrow+\infty}\left(1+\frac{1}{n}\right)^{n} & =1+1+\frac{1}{2!}+\frac{1}{3!}+\frac{1}{4!}+\ldots \\
& =1+1+0.5+0.166667+0.0416667+\ldots=2.718281 \ldots
\end{aligned}
$$

As approximate value of $e$ is 2.718281 .

$$
\therefore \quad \operatorname{Lim}_{n \rightarrow+\infty}\left(1+\frac{1}{n}\right)^{n}=e
$$

Deduction: $\quad \operatorname{Lim}_{x \rightarrow 0}(1+x)^{x}=e$
We know that $\operatorname{Lim}_{n \rightarrow \infty}\left(1+\frac{1}{n}\right)^{n}=e$
(i)

Put $n=\frac{1}{x}$ in (i) then $x=\frac{1}{n}$
When $n \rightarrow \infty, x \rightarrow 0 \quad$ so, $\quad \operatorname{Lim}_{n \rightarrow+\infty}\left(1+\frac{1}{n}\right)^{n}=\operatorname{Lim}_{x \rightarrow 0}(1+x)^{\frac{1}{x}}$

$$
e=\operatorname{Lim}_{x \rightarrow 0}(1+x)^{\frac{1}{x}} \quad \because \quad \operatorname{Lim}_{x \rightarrow 1}\left(1+\frac{1}{n}\right)^{n}=e
$$

Hence $\operatorname{Lim}_{x \rightarrow 0}(1+x)^{\frac{1}{x}}=e$

# 12.2.7 $\lim _{x \rightarrow 0} \frac{a^{x}-1}{x}=\log _{a} a$

Put $a^{x}-1=y$
then $\quad a^{x}=1+y$
So, $\quad x=\log _{a}(1+y)$
From (i) when $x \rightarrow 0, y \rightarrow 0$

$$
\begin{aligned}
\therefore \quad \lim _{x \rightarrow 0} \frac{a^{x}-1}{x} & =\lim _{y \rightarrow 0} \frac{y}{\log _{a}(1+y)}=\underline{\lim _{y \rightarrow 0}} \frac{1}{\frac{1}{y} \log _{a}(1+y)} \\
& =\underline{\lim _{y \rightarrow 0}} \frac{1}{\log _{a}(1+y)^{y}}=\frac{1}{\log _{a} e}=\log _{a} a \quad\left(\underline{\lim _{y \rightarrow 0}(1+y)^{y}}=e\right)
\end{aligned}
$$

Deduction: $\quad \underline{\lim _{x \rightarrow 0}}\left(\frac{e^{x}-1}{x}\right)=\log _{e} e=1$
We know that $\underline{\lim _{x \rightarrow 0}}\left(\frac{a^{x}-1}{x}\right)=\log _{a} a$
Put $a=e$ in (i) we know $\operatorname{Lim}_{x \rightarrow 0}\left(\frac{e^{x}-1}{x}\right)=\log _{e} e=1$
Important Results to Remember
(i) $\quad \operatorname{Lim}_{x \rightarrow \infty} e^{x}=\infty$
(ii) $\quad \operatorname{Lim}_{x \rightarrow-\infty} e^{x}=\operatorname{Lim}_{x \rightarrow \infty}\left(\frac{1}{e^{x}}\right)=0$

## Example 6 Express each limit in terms of $e$.

(i) $\quad \lim _{n \rightarrow \infty}\left(1+\frac{3}{n}\right)^{3 n}$
(ii) $\quad \operatorname{Lim}_{n \rightarrow 0}(1+2 n)^{\frac{1}{n}}$

Solution (i) Observe the resemblance of the limit with $\operatorname{Lim}_{n \rightarrow \infty}\left(1+\frac{1}{n}\right)^{n}=e$

$$
\begin{aligned}
& \left(1+\frac{3}{n}\right)^{2 n}=\left[\left(1+\frac{3}{n}\right)^{\frac{n}{3}}\right]^{6}=\left[\left(1+\frac{1}{\frac{n}{3}}\right)^{\frac{n}{3}}\right]^{6} \\
& \because \quad \operatorname{Lim}_{n \rightarrow+\infty}\left(1+\frac{3}{n}\right)^{3 n}=\operatorname{Lim}_{m \rightarrow+\infty}\left[\left(1+\frac{1}{m}\right)^{m}\right]^{6}=e^{6} \text { where, } m=\frac{n}{3}
\end{aligned}
$$

(ii) Observe the resemblance of the limit with $\operatorname{Lim}_{x \rightarrow 0}(1+x)^{\frac{1}{x}}=e$

$$
\begin{aligned}
& \operatorname{Lim}_{n \rightarrow 0}(1+2 n)^{\frac{1}{n}}=\operatorname{Lim}_{n \rightarrow 0}\left[(1+2 n)^{\frac{1}{2 n}}\right]^{2} \\
& \text { put } m=2 n \text {, when } n \rightarrow 0, m \rightarrow 0 \\
& \operatorname{Lim}_{n \rightarrow 0}(1+2 n)^{\frac{1}{n}}=\lim _{m \rightarrow 0}\left[(1+m)^{\frac{1}{m}}\right]^{2}=e^{2}
\end{aligned}
$$

# 12.2.8 The Sandwich Theorem

Let $f, g$ and $h$ be functions such that $f(x) \leq g(x) \leq h(x)$ for all numbers $x$ in some open interval containing " $c$ ", except possibly at $c$ itself.
If $\operatorname{Lim}_{x \rightarrow c} f(x)=L$ and $\operatorname{Lim}_{x \rightarrow c} h(x)=L$, then $\operatorname{Lim}_{x \rightarrow c} g(x)=L$
Many limit problems arise that cannot be directly evaluated by algebraic techniques. They require geometric arguments, so we evaluate an important theorem.

### 12.2.9 If $\theta$ is measured in radian, then $1 \operatorname{lin} \sin \theta=1$.

Proof: To evaluate this limit, we apply a new technique. Take $\theta$ be positive acute central angle of a sector of a circle with radius $r=1$. As shown in the figure, $O A B$ represents a sector of a circle. Join $A$ and $B$ and extend $O B$ to $D$ such that $O A \perp \overline{A D}$. Also draw $\overline{B C} \perp \overline{O C}$ on $\overline{O A}$.
Given $|O A|=|O B|=1 \quad$ (radii of unit circle)
In the right $\triangle O C B, \sin \theta=\frac{|\overline{B C}|}{\mid \overline{O B}} \mid=|\overline{B C}|$
In the right $\triangle O A D, \tan \theta=\frac{|\overline{A D}|}{|\overline{O A}|}=|\overline{A D}|$
(i) Area of $\triangle O A B=\frac{1}{2}|\overline{O A}||\overline{B C}|=\frac{1}{2}(1)(\sin \theta)=\frac{1}{2} \sin \theta$
(ii) Area of sector $O A B=\frac{1}{2} r^{2} \theta=\frac{1}{2}(1)(\theta)=\frac{1}{2} \theta \quad$ and
(iii) Area of $\triangle O A D=\frac{1}{2}|\overline{O A}||\overline{A D}|=\frac{1}{2}(1)(\tan \theta)=\frac{1}{2} \tan \theta$

From the figure we see that
Area of $\triangle O A B<$ Area of sector $O A B<$ Area of $\triangle O A D$
Figure 12.4
$\Rightarrow \quad \frac{1}{2} \sin \theta<\frac{\theta}{2}<\frac{1}{2} \tan \theta$

As $\sin \theta$ is positive, so on division by $\frac{1}{2} \sin \theta$, we get

$$
1<\frac{\theta}{\sin \theta}<\frac{1}{\cos \theta} \quad\left(0<\theta<\frac{\pi}{2}\right)
$$

i.e., $\quad 1>\frac{\sin \theta}{\theta}>\cos \theta \quad$ or $\quad \cos \theta<\frac{\sin \theta}{\theta}<1$
when $\theta \rightarrow 0, \cos \theta \rightarrow 1$
Since $\frac{\sin \theta}{\theta}$ is sandwiched between 1 and a quantity approaching 1 itself. So, by the sandwich theorem, it must also approach 1 that is, $\operatorname{Lim}_{\theta \rightarrow 0} \frac{\sin \theta}{\theta}=1$

# Example 7 Evaluate $\operatorname{Lim}_{\theta \rightarrow 0} \frac{\sin 7 \theta}{\theta}$

Solution
Let $x=7 \theta$, so that $\theta=\frac{x}{7}$
when $\theta \rightarrow 0$ we have $x \rightarrow 0$

$$
\therefore \quad \lim _{x \rightarrow 0} \frac{\sin 7 \theta}{\theta}=\operatorname{Lim}_{x \rightarrow 0} \frac{\sin x}{x}=7 \operatorname{Lim}_{x \rightarrow 0} \frac{\sin x}{x}=(7)(1)=7
$$

Example 8 Evaluate $\operatorname{Lim}_{\theta \rightarrow 0} \frac{1-\cos \theta}{\theta}$
Solution $\frac{1-\cos \theta}{\theta}=\frac{1-\cos \theta}{\theta} \cdot \frac{1+\cos \theta}{1+\cos \theta}=\frac{1-\cos ^{2} \theta}{\theta(1+\cos \theta)}$

$$
=\frac{\sin ^{2} \theta}{\theta(1+\cos \theta)}=\sin \theta\left(\frac{\sin \theta}{\theta}\right)\left(\frac{1}{1+\cos \theta}\right)
$$

$\operatorname{Lim}_{\theta \rightarrow 0}\left(\frac{1-\cos \theta}{0}\right)=\operatorname{Lim}_{\theta \rightarrow 0} \sin \theta \cdot \operatorname{Lim}_{\theta \rightarrow 0} \frac{\sin \theta}{\theta} \cdot \operatorname{Lim}_{\theta \rightarrow 0}\left(\frac{1}{1+\cos \theta}\right)=(0)(1)\left(\frac{1}{1+1}\right)=0$

## EXERCISE 12.1

1. Find the limit of the following sequences if exists:
(i) $a_{n}=\frac{2 n+3}{n+1}$
(ii) $b_{n}=\frac{2 n+3}{n^{2}+1}$
(iii) $c_{n}=\frac{5 n^{2}}{2 n+3}$
(iv) $d_{n}=\frac{n^{2}-3 n+1}{2 n^{2}+n+4}$

2. Evaluate each limit by using theorems of limits:
(i) $\quad \underline{\operatorname{Lim}}_{x \rightarrow 3}(2 x+4)$
(ii) $\quad \underline{\operatorname{Lim}}_{x \rightarrow 1}\left(3 x^{2}-2 x+4\right)$
(iii) $\underline{\operatorname{Lim}}_{x \rightarrow 3} \sqrt{x^{2}+x+4}$
(iv) $\underline{\operatorname{Lim}}_{x \rightarrow 2} \sqrt{x^{2}+4}$
(v) $\underline{\operatorname{Lim}}_{x \rightarrow 2}\left(\sqrt{x^{2}+1}-\sqrt{x^{2}+5}\right)$
(vi) $\underline{\operatorname{Lim}}_{x \rightarrow-2} \frac{2 x^{3}+5 x}{3 x-2}$
3. Evaluate each limit by using algebraic techniques:
(i) $\quad \underline{\operatorname{Lim}}_{x \rightarrow-1} \frac{x^{3}-x}{x+1}$
(ii) $\underline{\operatorname{Lim}}_{x \rightarrow 3}\left(\frac{x^{2}-5 x+6}{x^{2}-2 x-3}\right)$
(iii) $\quad \underline{\operatorname{Lim}}_{x \rightarrow 2}\left(\frac{x^{3}-8}{x^{2}-5 x+6}\right)$
(iv) $\underline{\operatorname{Lim}}_{x \rightarrow 1} \frac{x^{2}-3 x^{2}+3 x-1}{x^{2}-x}$
(v) $\underline{\operatorname{Lim}}_{x \rightarrow 2}\left(\frac{x^{3}-6 x^{2}+12 x-8}{x^{3}-4 x}\right)$
(vi) $\underline{\operatorname{Lim}}_{x \rightarrow 1}\left(\frac{x^{4}-1}{x^{2}-3 x+2}\right)$
(vii) $\underline{\operatorname{Lim}}_{x \rightarrow 2} \frac{x-2}{\sqrt{x+2}-\sqrt{6-x}}$
(viii) $\underline{\operatorname{Lim}}_{h \rightarrow 0} \frac{\sqrt{x+h}-\sqrt{x}}{h}$
(ix) $\quad \underline{\operatorname{Lim}}_{x \rightarrow \infty} \frac{x^{n}-a^{n}}{x^{n}-a^{m}}$
4. Evaluate the following limits:
(i) $\quad \underline{\operatorname{Lim}}_{x \rightarrow 0} \frac{\sin 5 x}{x}$
(ii) $\quad \underline{\operatorname{Lim}}_{x \rightarrow 0} \frac{\sin x^{\prime \prime}}{x}$
(iii) $\underline{\operatorname{Lim}}_{0 \rightarrow 0} \frac{1-\cos \theta}{\sin \theta}$
(iv) $\underline{\operatorname{Lim}}_{x \rightarrow \frac{\pi}{4}} \frac{\sin x-\cos x}{x-\frac{\pi}{4}}$
(v) $\underline{\operatorname{Lim}}_{x \rightarrow 0} \frac{\cos a x-\cos b x}{x^{2}}$
(vi) $\underline{\operatorname{Lim}}_{x \rightarrow \frac{\pi}{4}} \frac{\tan x-1}{x-\frac{\pi}{4}}$
(vii) $\underline{\operatorname{Lim}}_{x \rightarrow 0} \frac{1-\cos 2 x}{x^{2}}$
(viii) $\underline{\operatorname{Lim}}_{x \rightarrow 0} \frac{\cos a x-\cos b x}{\cos c x-\cos d x}$
(ix) $\quad \underline{\operatorname{Lim}}_{x \rightarrow 1} \frac{x^{3}-1}{x^{2}-1}$
(x) $\quad \underline{\operatorname{Lim}}_{x \rightarrow 3} \frac{x^{2}-x \log x+3 \log x-9}{x-3}$
(xi) $\quad \underline{\operatorname{Lim}}_{x \rightarrow 0} \frac{x\left(2^{x}-1\right)}{1-\cos x}$
5. Express each limit in terms of $e$.
(i) $\quad \underline{\operatorname{Lim}}_{n \rightarrow+\infty}\left(1+\frac{1}{n}\right)^{2 n}$
(ii) $\quad \underline{\operatorname{Lim}}_{n \rightarrow+\infty}\left(1+\frac{1}{n}\right)^{n}$
(iii) $\underline{\operatorname{Lim}}_{n \rightarrow+\infty}\left(1-\frac{1}{n}\right)^{n}$
(iv) $\quad \underline{\operatorname{Lim}}_{n \rightarrow+\infty}\left(1+\frac{1}{3 n}\right)^{n}$
(v) $\quad \underline{\operatorname{Lim}}_{n \rightarrow+\infty}\left(1+\frac{4}{n}\right)^{n}$
(vi) $\underline{\operatorname{Lim}}_{x \rightarrow 0}(1+3 x)^{\frac{2}{x}}$
(vii) $\underline{\operatorname{Lim}}_{x \rightarrow 0}\left(1+2 x^{2}\right)^{\frac{1}{x^{2}}}$
(viii) $\underline{\operatorname{Lim}}_{x \rightarrow 0} \frac{e^{a x}-e^{b x}}{a b x}$
(ix) $\quad \underline{\operatorname{Lim}}_{x \rightarrow \infty}\left(\frac{x}{1+x}\right)^{x}$
(x) $\quad \underline{\operatorname{Lim}}_{x \rightarrow 0} \frac{\frac{1}{x}-1}{e^{\frac{1}{x}}+1}, x<0$
(xi) $\quad \underline{\operatorname{Lim}}_{x \rightarrow 0} \frac{e^{\frac{1}{x}}-1}{e^{x}+1}, x>0$
(xii) $\quad \underline{\operatorname{Lim}}_{x \rightarrow 2} \frac{e^{x}-e^{2}}{x-2}$

# 12.3 Continuity and Discontinuity of Functions 12.3.1 One-Sided Limits

In defining $\operatorname{Lim}_{x \rightarrow c} f(x)$, we restricted $x$ in an open interval containing $c$ i.e., we studied the behaviour of $f$ on both sides of $c$. However, in some cases it is necessary to investigate one sided limits that is, the left hand limit and the right hand limit.

## (i) The Left Hand Limit

$\operatorname{Lim}_{x \rightarrow c^{\prime}} f(x)=L$ is read as the limit of $f(x)$ is equal to $L$ as $x$ approaches $c$ from the left i.e., for all $x$ sufficiently close to $c$, but less than $c$, the value of $f(x)$ can be made as close as we please to $L$.
(ii) The Right Hand Limit
$\operatorname{Lim}_{x \rightarrow c^{\prime}} f(x)=M$ is read as the limit of $f(x)$ is equal to $M$ as $x$ approaches $c$ from the right i.e., for all $x$ sufficiently close to $c$, but greater than $c$, the value of $f(x)$ can be made as close as we please to $M$.

### 12.3.2 Criterion for Existence of Limit of a Function

$$
\operatorname{Lim}_{x \rightarrow c} f(x)=L \text { if and only if } \operatorname{Lim}_{x \rightarrow c} f(x)=\operatorname{Lim}_{x \rightarrow c} f(x)=L
$$

Example 9 Determine whether $\operatorname{Lim}_{x \rightarrow 2} f(x)$ and $\operatorname{Lim}_{x \rightarrow 4} f(x)$ exist, when

$$
f(x)=\left\{\begin{array}{ll}
2 x+1 & \text { if } 0 \leq x \leq 2 \\
7-x & \text { if } 2<x<4 \\
x & \text { if } 4 \leq x \leq 6
\end{array}\right.
$$

Solution (i) $\quad \operatorname{Lim}_{x \rightarrow 2} f(x)=\operatorname{Lim}_{x \rightarrow 2}(2 x+1)=4+1=5$

$$
\begin{aligned}
& \operatorname{Lim}_{x \rightarrow 2^{\prime}} f(x)=\operatorname{Lim}_{x \rightarrow 2}(7-x)=7-2=5 \\
& \text { Since } \quad \operatorname{Lim}_{x \rightarrow 2} f(x)=\operatorname{Lim}_{x \rightarrow 2^{\prime}} f(x)=5 \\
& \Rightarrow \quad \operatorname{Lim}_{x \rightarrow 2} f(x) \text { exists and is equal to } 5 .
\end{aligned}
$$

(ii) $\quad \operatorname{Lim}_{x \rightarrow 4^{\prime}} f(x)=\operatorname{Lim}_{x \rightarrow 4^{\prime}}(7-x)=7-4=3$

$$
\operatorname{Lim}_{x \rightarrow 4^{\prime}} f(x)=\operatorname{Lim}_{x \rightarrow 4^{\prime}}(x)=4
$$

Since $\operatorname{Lim}_{x \rightarrow 4^{\prime}} f(x) \neq \operatorname{Lim}_{x \rightarrow 4^{\prime}} f(x)$
Therefore, $\operatorname{Lim}_{x \rightarrow 4} f(x)$ does not exist.