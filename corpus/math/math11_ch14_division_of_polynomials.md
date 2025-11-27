# Chapter 14: Division of Polynomials

## INTRODUCTION

Polynomials play a fundamental role in algebra and have wide-ranging applications in various fields, including engineering, data science and digital communication. This unit explores polynomial division to determine the quotient and remainder. The remainder theorem is introduced as a powerful tool for evaluating polynomials efficiently, while the factor theorem is applied to factorize cubic polynomials. These concepts extend beyond theoretical mathematics, finding practical applications in polynomial regression, signal processing and coding theory. By mastering these techniques, students will develop a deeper understanding of polynomials and their significance in solving real-world problems.

### 9.1 Polynomial Function

A polynomial in $x$ is an expression of the form

$$
a_{n} x^{n}+a_{n-1} x^{n-1}+a_{n-2} x^{n-2}+\ldots+a_{2} x^{2}+a_{1} x+a_{0}
$$

where $n$ is a non-negative integer and the coefficients $a_{n}, a_{n-1}, a_{n-2}, \ldots, a_{1}$ and $a_{0}$ are real numbers. It can be considered as a polynomial function of $x$, the highest power of $x$ in a polynomial is called the degree of the polynomial. In the expression (i) if $a_{n} \neq 0$ then it is a polynomial of degree $n$. The polynomials $x^{2}-2 x+3$, $3 x^{3}+2 x^{2}-5 x+4$ are of degree 2 and 3 respectively.
Example 1 Divide the cubic polynomial $3 x^{3}-10 x^{2}+13 x-6$ by the linear polynomial $x-2$. Also find quotient and remainder.
$$
\begin{aligned}
& 3 x^{3}-4 x+5 \\
& \begin{array}{r}
x-2 \\
3 x^{3}-10 x^{2}+13 x-6 \\
3 x^{3}+6 x^{2}
\end{array} \\
& \begin{array}{r}
-4 x^{2}+13 x \\
+8 x
\end{array} \\
& \frac{5 x-6}{5 x+10}
\end{aligned}
$$

Hence, we can write: $3 x^{3}-10 x^{2}+13 x-6=(x-2)\left(3 x^{2}-4 x+5\right)+4$
So, quotient $-3 x^{2}-4 x+5$ and remainder $-4$.

Example 2 Divide the polynomial $x^{4}-3 x^{3}+5 x^{2}-7 x+2$ by $x^{2}-x+1$. Also find quotient and remainder.

# Soation

$$
\begin{aligned}
& x^{3}-x+1 \begin{array}{c}
x^{3}-2 x+2 \\
x^{4}-3 x^{3}+5 x^{2}-7 x+2 \\
x^{4}+x^{3}+x^{2} \\
-2 x^{3}+4 x^{2}-7 x \\
\mp 2 x^{3}+2 x^{2} \mp 2 x \\
2 x^{2}-5 x+2 \\
-2 x^{2}+2 x+2 \\
-3 x
\end{array} \\
& \text { So, quotient }=x^{2}-2 x+2 \text { and remainder }=-3 x
\end{aligned}
$$

### 9.1.1 Remainder Theorem

Statement: If a polynomial $f(x)$ of degree $n \geq 1$ is divided by $x-a$ till no $x$-term exists in the remainder, then $f(a)$ is the remainder.
Proof: Suppose we divide the polynomial $f(x)$ by $(x-a)$. Then there exists a unique quotient $q(x)$ and a unique remainder $R$ such that

$$
f(x)=(x-a) q(x)+R
$$

Substituting $x=a$ in equation (i), we get

$$
\begin{aligned}
& f(x)=(a-a) q(a)+R \\
& f(a)=R
\end{aligned}
$$

Hence remainder $=f(a)$
Example 3 Find the remainder without performing division when $f(x)=x^{4}+x^{3}+x^{2}+1$ is divided by $x+1$.
Solution Here $f(x)=x^{4}+x^{3}+x^{2}+1$ and $x-a=x+1 \Rightarrow a=-1$

$$
\begin{aligned}
\text { Remainder } & =f(-1) \\
& =(-1)^{4}+(-1)^{3}+(-1)^{2}+1 \\
& =1+(-1)+1+1=2
\end{aligned}
$$

(By remainder theorem)

Example 4 Find the value of $k$ if the polynomial $x^{3}+k x^{2}-7 x+6$ has a remainder
-4 , when divided by $x+2$.
Solution Let $f(x)=x^{3}+k x^{2}-7 x+6$ and $x-a=x+2$, we have, $a=-2$
Remainder $=f(-2)$
(By remainder theorem)

$$
\begin{aligned}
& =(-2)^{3}+k(-2)^{2}-7(-2)+6 \\
& =-8+4 k+14+6 \\
& =4 k+12
\end{aligned}
$$

Given that remainder $=-4$

$$
\begin{aligned}
& 4 k+12=-4 \\
& \Rightarrow \quad 4 k=-16 \\
& \Rightarrow \quad k=-4
\end{aligned}
$$

# 9.1.2 Factor Theorem

Statement: The polynomial $x-a$ is a factor of the polynomial $f(x)$ iff $f(a)=0$. In other words $x-a$ is a factor of $f(x)$ if and only if $x=a$ is the root of the polynomial equation $f(x)=0$.
Proof: Suppose $q(x)$ is the quotient and $R$ is the remainder when the polynomial $f(x)$ is divided by $x-a$, till no $x$-term exists in the remainder, then:

$$
f(x)=(x-a) q(x)+R
$$

Suppose $f(a)=0 \Rightarrow R=0$

$$
f(x)=(x-a) q(x)
$$

$(x-a)$ is a factor of $f(x)$
Conversely, if $(x-a)$ is a factor of $f(x)$, then $f(x)=(x-a) q(x)$ for some polynomial $q(x)$

$$
f(a)=0
$$

which proves the theorem.
Example 5 Show that $x-2$ is a factor of $f(x)=x^{3}-7 x+6$ without factorizing.
Solution Here, $f(x)=x^{3}-7 x+6$ and $a=2$

$$
\begin{aligned}
f(2) & =2^{3}-7(2)+6 \\
& =8-14+6=0
\end{aligned}
$$

(By factor theorem)
So, $x-2$ is a factor of $f(x)$.
Note To determine if a given linear polynomial $x-a$ is a factor of $f(x)$, we need to check whether $f(a)=0$.
Example 6 If $x+1$ and $x-2$ are factors of $x^{3}+p x^{2}+q x+2$. Find the values of $p$ and $q$.
Solution Let $f(x)=x^{3}+p x^{2}+q x+2$
Since, $x+1$ is a factor of $f(x)$.
So, $\quad f(-1)=0 \Rightarrow-1+p-q+2=0$

$$
p-q=-1
$$

Similarly, $x-2$ is also a factor of $f(x)$.
So, $\quad f(2)=0$

$$
\begin{aligned}
& 8+4 p+2 q+2=0 \\
& 4 p+2 q=-10 \\
& 2 p+q=-5
\end{aligned}
$$

By adding (i) and (ii), we have

$$
\begin{aligned}
& p=-2 \\
& \text { Put } \quad p=-2 \text { in (i), we have } \\
& q=p+1=-2+1=-1
\end{aligned}
$$

# 9.1.3 Synthetic Division

There is a nice shortcut method for long division of a polynomial $f(x)$ by a polynomial of the form $x-a$. This process of division is called Synthetic Division.

To divide the polynomial $p x^{3}+q x^{3}+c x+d$ by $x-a$
## Outline of the Method

(i) Write down the coefficients of the dividend $f(x)$ from left to right in decreasing order of powers of $x$. Insert 0 for any missing term.
(ii) To the left of the first line, write $a$ of the divisor $(x-a)$.
(iii) Use the following patterns to write the second and third lines:

Vertical pattern $(\downarrow) \quad$ Add terms
Diagonal pattern $(\nearrow)$ Multiply by $a$.
Example 7 If $(x-2)$ and $(x+2)$ are factors of $x^{4}-13 x^{2}+36$. Using synthetic division, find the other two factors.
Solution Let $f(x)=x^{8}-13 x^{3}+36$

$$
=x^{4}+0 x^{3}-13 x^{2}+0 x+36
$$

Here $x-a=x-2 \Rightarrow a=2$ and $x-a=x+2=x-(-2) \Rightarrow a=-2$
By synthetic Division:

| 2 | 1 | 0 | -13 | 0 | 36 |
| :--: | :--: | :--: | :--: | :--: | :--: |
|  |  | 2 | 4 | -18 | -36 |
| -2 | 1 | 2 | -9 | -18 | 0 |
|  |  | -2 | 0 | 18 |  |
|  | 1 | 0 | -9 | 0 |  |

$\therefore$ Quotient $=x^{2}+0 x-9=x^{3}-9=(x+3)(x-3)$
Therefore, other two factors are $(x+3)$ and $(x-3)$.

# EXERCISE 9.1

1. Find remainder and quotient by simplifying the following:
(i) $\left(3 x^{2}-x+2\right) \div(x-1)$
(ii) $\left(x^{3}+12 x^{2}-3 x+4\right) \div(x-2)$
(iii) $\left(x^{4}-5 x^{3}-8 x^{2}+13 x+12\right) \div(x-6)$
(iv) $\left(5 x^{4}-3 x^{3}+2 x^{2}-1\right) \div\left(x^{2}+4\right)$
(v) $\left(3 x^{4}-5 x^{3}+4 x-6\right) \div\left(x^{2}-3 x+5\right)$
2. Use the remainder theorem to find the remainder when the first polynomial is divided by the second polynomial.
(i) $x^{2}+5 x+6, x-2$
(ii) $x^{3}+5 x^{2}+6, x+1$
(iii) $x^{4}+x^{3}+x^{2}+x+1, x-1$
(iv) $x^{4}+x^{3}+1, x+3$
(v) $x^{4}+x^{3}+2, x+2$
3. Use the factor theorem to determine if the first polynomial is a factor of the second polynomial.
(i) $x+1, x^{2}-1$
(ii) $x-2, x^{2}-5 x+6$
(iii) $x+1, x^{2}+x^{2}+x-3$
(iv) $x-2, x^{3}+x^{2}-7 x+2$
(v) $x-3, x^{4}-3 x^{3}+x^{2}-x+1$
4. Use synthetic division to show that $x$ is the zero of the polynomial and use the result to factorize the polynomial completely.
(i) $x^{3}-7 x+6, x=2$
(ii) $x^{3}-28 x-48, x=-4$
(iii) $2 x^{4}+7 x^{3}-4 x^{2}-27 x-18, x=2, x=-3$
5. Use synthetic division to find the quotient and the remainder when the polynomial $x^{4}-10 x^{2}-2 x+4$ is divided by $x+3$.
6. If $x+1$ and $x-2$ are factors of $x^{2}-p x^{2}+q x+2$. Using synthetic division, find the values of $p$ and $q$.
7. When the polynomial $4 x^{4}+2 x^{3}+k x^{3}+13$ is divided by $x+1$, the remainder is 16. Find the value of $k$.
8. When the polynomial $x^{3}+x^{2}+x+k$ is divided by $x+1$, the reminder is 7 . Find the value of $k$.

9. Use factor theorem to find the values of $p$ and $q$ if $x+1$ and $x-2$ are the factors of the polynomial $x^{3}+p x^{2}+q x+3$.
10. Use factor theorem to find the values of $a$ and $b$ if -2 and 2 are the roots of the polynomial $2 x^{3}+4 x^{2}+a x+b$.

# 9.2 Real Life Applications of Remainder and Factor Theorems

In this article, we shall demonstrate how remainder and factor theorems are applied in different areas such as polynomial regression (used in statistical modeling), signal processing (used for filtering and error detection) and coding theory (used in data encryption and error correction in communication systems). These applications highlight the significance of polynomial analysis beyond theoretical mathematics.
Regression Analysis: It is a statistical method used to model the relationship between a dependent variable and one or more independent variables.
Polynomial Regression: It is a type of regression analysis where the relationship between the independent and dependent variables is modeled as an $n^{\text {th }}$-degree polynomial. It is used when the data shows a curved (non-linear) relationship, but we still want to fit a smooth, continuous function. Factor theorem is useful for reducing polynomial regression degree and remainder theorem helps in evaluating polynomials at given points.
Example 8 Consider a data set of monthly sales figures. A polynomial regression model $P(x)=x^{3}+x^{2}+2 x+1$ is fitted to this data. If the observed sales in the $3^{\text {rd }}$ month are 40 units, find the percentage error.

## Salation

$$
\text { Error }=\text { Observed }- \text { Predicted }=40-P(3)
$$

Now,

$$
\begin{aligned}
P(3) & =3^{3}+3^{2}+2(3)+1 \\
& =27+9+6+1 \\
& =43
\end{aligned}
$$

Error $=40-43$

$$
=-3
$$

So, Percentage Error $=\left|\frac{-3}{40}\right| \times 100$

$$
=7.5 \%
$$

Example 9 Suppose a polynomial regression model $P(x)=3 x^{3}-4 x^{2}+2 x-5$. If a data point at $x=-1$ is missing. What should be its predicted value?
Solution By remainder theorem

$$
\begin{aligned}
P(-1) & =3(-1)^{3}-4(-1)^{2}+2(-1)-5 \\
& =-3-4-2-5 \\
& =-14
\end{aligned}
$$

So, the predicted value of given polynomial regression model at $x=-1$ is -14 .
Digital Signal Processing (DSP): It is the used in computers or digital devices to analyze, change or improve signals like sound, images or sensor data. In the context of DSP, we often deal with systems represented by transfer functions in the z-domain, denoted as $\mathrm{H}(\mathrm{z})$. These transfer functions are rational functions, meaning they are ratios of two polynomials in $z$ i.e., $H(z)=\frac{B(z)}{A(z)}$, where $B(z)$ represents the numerator polynomial (related to the system's zeros) and $A(z)$ represents the denominator polynomial (related to the system's poles).
In signal processing, finding the roots of the numerator polynomial $B(z)$ provides the zeros of the system. If $B\left(z_{0}\right)=0$, then $\left(z-z_{0}\right)$ is a factor of $B(z)$. If $\left|z_{0}\right|=1$, this corresponds to a frequency that the system blocks.
Similarly, finding the roots of the denominator polynomial $A(z)$ provides the poles of the system. If $A\left(p_{0}\right)=0$, then $\left(z-p_{0}\right)$ is a factor of $A(z)$. The locations of these poles in the complex $z$-plane are crucial for determining the stability of the system. For a stable system, all poles must lie inside the unit circle $\left(\left|p_{0}\right|<1\right)$.
Example 10 A signal processing system has a transfer function with a denominator $A(z)=z^{2}-0.25$. Use factor theorem to find the poles of the system and determine if the system is stable.
Solution The poles occur when $A(z)=0$.

$$
\begin{aligned}
z^{2}-0.25 & =0 \\
z^{2}-(0.5)^{2} & =0 \\
(z-0.5)(z+0.5) & =0 \\
z-0.5 & =0 \text { or } z+0.5=0 \\
z & =0.5 \\
\text { or } z & =-0.5
\end{aligned}
$$

Thus, the system has poles at $z=0.5$ and $z=-0.5$. For stable system, all poles must lie inside the unit circle $(|z|<1)$. Here, $|0.5|=0.5<1$ and $|-0.5|=0.5<1$. Since both poles are inside the unit circle, the system is stable.

# EXERCISE 9.2

1. Consider a data set at monthly sales figures. A polynomial regression model $P(x)=x^{3}+2 x^{2}+x-3$ is fitted to this data. If the observed sales in the $5^{\text {th }}$ month are 240 units, find the percentage error.
2. A retailer company has developed a polynomial regression model to predict weekly product demand: $D(w)=w^{3}-2 w^{2}+5 w-4$, where $D(w)$ represents predicted demand(in units) and $w$ is the week number. Use the remainder theorem to predict demand for $3^{\text {rd }}$ week. If the observe demand is 22 units, calculate the prediction error.
3. A digital signal processing system has a transfer function with a numerator $B(z)=z^{2}-z-2$. Use the factor theorem to find the zeros of the system.
4. A signal process system has a transfer function $H(z)=\frac{z^{2}+3 z+2}{z^{2}-0.2 z+0.9}$. Find the zero(s) of the transfer function by using factor theorem.
5. A signal process system has a transfer function $H(z)=\frac{z^{2}-0.5 z-0.5}{z^{3}+1}$. Find the zero(s) of the transfer function by using factor theorem.
6. A signal processing system has a transfer function with a denominator $A(z)=z^{2}-0.3 z-0.4$. Use factor theorem to find the poles of the system and determine if the system is stable.
7. The denominator of signal processing system's transfer function equal to $A(z)=z^{2}+1.2 z+0.35$ Use factor theorem to determine the location of the corresponding poles and assess the stability of the system.