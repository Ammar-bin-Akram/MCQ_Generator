# Chapter 8: EXERCISE 5.1

## Resolve the following into partial fractions:

1. $\frac{2}{x^{2}-1}$
2. $\frac{a-b}{(x-a)(x-b)},(a \neq b)$
3. $\frac{x^{2}+1}{(x+1)(x-1)}$
4. $\frac{2 x+3}{(x+1)(x+2)(x+3)}$
5. $\frac{x^{2}+4 x+5}{(x+1)\left(x^{2}+5 x+6\right)}$
6. $\frac{4 x^{3}+5 x^{3}-3 x-2}{x^{2}-1}$
7. $\frac{3 x^{2}-12 x+11}{(x-1)(x-2)(x-3)}$
8. $\frac{(x-1)(x-2)(x-3)}{(x-4)(x-5)(x-6)}$
9. $\frac{x^{2}}{\left(x^{2}+a\right)\left(x^{2}+b\right)\left(x^{2}+c\right)}$
10. $\frac{x+1}{(x-1)^{2}}$
11. $\frac{x^{2}+x}{\left(x^{2}-1\right)^{2}}$
12. $\frac{3 x^{2}+4 x-5}{(x-1)^{3}}$
13. $\frac{1}{x(x+1)^{3}}$
14. $\frac{4 x^{2}-3 x+1}{(x+1)(x-1)^{2}}$
15. $\frac{12 x^{2}-48}{(x-2)^{2}(x+2)^{2}}$

## Case III: When $Q(x)$ contains non-repeated irreducible quadratic factors

Definition: A quadratic factor is irreducible if it cannot be written as the product of two linear factors with real coefficients. For example, $x^{2}+x+1$ and $x^{2}+3$ are irreducible quadratic factors.

If the polynomial $Q(x)$ contains non-repeated irreducible quadratic factors then $\frac{P(x)}{Q(x)}$ may be written as the identity having partial fractions of the form:

$$
\frac{A x+B}{a x^{2}+b x+c} \text { where } A \text { and } B \text { are the numbers to be found. }
$$

The method is explained by the following examples:
Example 6 Resolve $\frac{3 x-11}{\left(x^{2}+1\right)(x+3)}$ into partial fractions.
Solution Suppose $\frac{3 x-11}{\left(x^{2}+1\right)(x+3)}=\frac{A x+B}{x^{2}+1}+\frac{C}{x+3}$

$$
\begin{aligned}
& \Rightarrow \quad 3 x-11=(A x+B)(x+3)+C\left(x^{2}+1\right) \\
& \Rightarrow \quad 3 x-11=(A+C) x^{2}+(3 A+B) x+(3 B+C)
\end{aligned}
$$

For $C$, putting $x+3=0 \quad \Rightarrow \quad x=-3$ in (i), we get

$$
-9-11=C(9+1) \quad \Rightarrow \quad C=-2
$$

Equating the coefficients of $x^{2}$ and $x$ in (ii), we get

$$
\begin{aligned}
& 0=A+C \Rightarrow A=-C \quad \Rightarrow A=2 \\
& \text { and } \quad 3=3 A+B \Rightarrow B=3-3 A \Rightarrow B=3-6 \Rightarrow B=-3 \\
& \text { Hence, } \frac{3 x-11}{\left(x^{2}+1\right)(x+3)}=\frac{2 x-3}{x^{3}+1}-\frac{2}{x+3}
\end{aligned}
$$

Example 7 Resolve $\frac{4 x^{2}+8 x}{x^{4}+2 x^{2}+9}$ into partial fractions.
Solution Here, denominator $=x^{4}+2 x^{2}+9=\left(x^{2}+2 x+3\right)\left(x^{2}-2 x+3\right)$

$$
\therefore \quad \frac{4 x^{2}+8 x}{x^{4}+2 x^{2}+9}=\frac{4 x^{2}+8 x}{\left(x^{2}+2 x+3\right)\left(x^{2}-2 x+3\right)}
$$

Suppose

$$
\begin{aligned}
& \frac{4 x^{2}+8 x}{\left(x^{2}+2 x+3\right)\left(x^{2}-2 x+3\right)}=\frac{A x+B}{x^{2}+2 x+3}+\frac{C x+D}{x^{2}-2 x+3} \\
& \Rightarrow \quad 4 x^{2}+8 x=(A x+B)\left(x^{2}-2 x+3\right)+(C x+D)\left(x^{2}+2 x+3\right) \\
& \Rightarrow \quad 4 x^{2}+8 x=(A+C) x^{3}+(-2 A+B+2 C+D) x^{2} \\
&+(3 A-2 B+3 C+2 D) x+3 B+3 D
\end{aligned}
$$

which is an identity in $x$.
Equating the coefficients of $x^{3}, x^{2}, x, x^{0}$ in (i), we have

$$
\begin{aligned}
& 0=A+C \\
& 4=-2 A+B+2 C+D \\
& 8=3 A-2 B+3 C+2 D \\
& 0=3 B+3 D
\end{aligned}
$$

Solving (ii), (iii), (iv) and (v), we get

$$
A=1, B=2, C=-1 \text { and } D=-2
$$

Hence, $\frac{4 x^{2}+8 x}{x^{4}+2 x^{2}+9}=\frac{x+2}{x^{2}+2 x+3}+\frac{-x-2}{x^{2}-2 x+3}$
Case IV: When $Q(x)$ has repeated irreducible quadratic factors
If the polynomial $Q(x)$ contains a repeated irreducible quadratic factors $\left(a x^{2}+b x+c\right)^{n}$, $n \geq 2$ and $n$ is a positive integer, then $\frac{P(x)}{Q(x)}$ may be written as the following identity:

$$
\frac{P(x)}{Q(x)}=\frac{A_{1} x+B_{1}}{\alpha x^{2}+b x+c}+\frac{A_{2} x+B_{2}}{\left(a x^{2}+b x+c\right)^{2}}+\ldots+\frac{A_{n} x+B_{n}}{\left(a x^{2}+b x+c\right)^{n}}
$$

where $A_{1}, B_{1}, A_{2}, B_{2}, \ldots, A_{n}, B_{n}$ are numbers to be found. The method is explained through the following example:

Example 5 Resolve $\frac{4 x^{2}}{\left(x^{2}+1\right)^{2}(x-1)}$ into partial fractions.
Solution Let $\frac{4 x^{2}}{\left(x^{2}+1\right)^{2}(x-1)}=\frac{A x+B}{x^{2}+1}+\frac{C x+D}{\left(x^{2}+1\right)^{2}}+\frac{E}{x-1}$
$\Rightarrow 4 x^{2}=(A x+B)\left(x^{2}+1\right)(x-1)+(C x+D)(x-1)+E\left(x^{2}+1\right)^{2}$
$\Rightarrow \quad 4 x^{2}=(A+E) x^{4}+(-A+B) x^{3}+(A-B+C+2 E) x^{2}$

$$
+(-A+B-C+D) x+(-B-D+E)
$$

For $E$, putting $x-1=0 \quad \Rightarrow x=1$ in (i), we get

$$
4=E(1+1)^{2} \quad \Rightarrow \quad E=1
$$

Equating the coefficients of $x^{4}, x^{3}, x^{2}, x$, in (ii), we get

$$
\begin{aligned}
& 0=A+E \quad \Rightarrow \quad A=-E \quad \Rightarrow \quad A=-1 \\
& 0=-A+B \quad \Rightarrow \quad B=A \quad \Rightarrow \quad B=-1 \\
& 4=A-B+C+2 E \\
& \Rightarrow \quad C=4-A+B-2 E=4+1-1-2 \Rightarrow \quad C=2 \\
& \text { and } \quad 0=-A+B-C+D \\
& \Rightarrow \quad D=A-B+C=-1+1+2=2 \quad \Rightarrow \quad D=2
\end{aligned}
$$

Hence, $\frac{4 x^{2}}{\left(x^{2}+1\right)^{2}(x-1)}=\frac{x-1}{x^{2}+1}+\frac{2 x+2}{\left(x^{2}+1\right)^{2}}+\frac{1}{x-1}$