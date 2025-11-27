# Chapter 21: 13.3 Process of Finding Derivative $f^{\prime}(x)$ by Definition

### 12.3.1 Notation of Derivative

Several notations are used for derivatives. We have used the functional symbol $f^{\prime}(x)$, for the derivative of $f$ at $x$. For the function $y=f(x)$.

$$
y+\delta y=f(x+\delta x)
$$

Dividing both the sides of (iv) by $\delta x$, we get

$$
\frac{\delta y}{\delta x}=\frac{f(x+\delta x)-f(x)}{\delta x}
$$

Taking limit of both the sides of (v) as $\delta x \rightarrow 0$, we have

$$
\begin{aligned}
& \lim _{\delta x \rightarrow 0} \frac{\delta y}{\delta x}=\lim _{\delta x \rightarrow 0} \frac{f(x+\delta x)-f(x)}{\delta x} \\
& \lim _{\delta x \rightarrow 0} \frac{\delta y}{\delta x} \text { is denoted by } \frac{d y}{d x}, \text { so (vi) is written as } \frac{d y}{d x}=f^{\prime}(x)
\end{aligned}
$$

# The symbol $\frac{d y}{d x}$ is used for the derivative of $y$ with respect to $x$ and here it is not a quotient of $d y$ and $d x . \frac{d y}{d x}$ is also denoted by $y^{\prime}$.

Now we write, in a table the notations for derivative of $y=f(x)$ used by different mathematicians:

| Name of mathematician | Leibniz | Newton | Lagrange | Euler |
| :-- | :--: | :--: | :--: | :--: |
| Notation used for derivative | $\frac{d y}{d x}$ or $\frac{d f}{d x}$ | $f^{\prime \prime}(x)$ or $y^{\prime \prime}$ | $f^{\prime}(x)$ | $D f(x)$ |

If we replace $x+\delta x$ by $x$ and $x$ by $a$, then the expression $f(x+\delta x)-f(x)$ becomes $f(x)-f(a)$ and the change $\delta x$ in the independent variable, in this case, is $x-a$.
So, the expression $\frac{f(x+\delta x)-f(x)}{\delta x}$ is written as $\frac{f(x)-f(a)}{x-a}$
Taking the limit of the expression (vii) when $x \rightarrow a$, gives $\operatorname{Lim}_{x \rightarrow a} \frac{f(x)-f(a)}{x-a}=f^{\prime}(a)$.
Here $f^{\prime}(a)$ is called the derivative or gradient of $f$ at $x=a$.

### 13.3.2 Finding $f^{\prime}(x)$ by Definition of Derivative

Given a function $f$, then $f^{\prime}(x)$ if it exists, can be found by the following four steps:
Step I: Find $f(x+\delta x)$
Step II: Simplify $f(x+\delta x)-f(x)$
Step III: Divide $f(x+\delta x)-f(x)$ by $\delta x$ to get $\frac{f(x+\delta x)-f(x)}{\delta x}$ and simplify it.
Step IV: Find $\operatorname{Lim}_{\delta x \rightarrow 0} \frac{f(x+\delta x)-f(x)}{\delta x}$
The method of finding derivatives by this process is called differentiation by definition or by ab-initio or from first principle.

Example 3 Find the derivative of the following functions by definition
(a) $f(x)=c$
(b) $f(x)=x^{2}$

Solution
(a) $f(x)=c$
(i) $f(x+\delta x)=c$
(ii) $f(x+\delta x)-f(x)=c-c=0$
(iii) $\frac{f(x+\delta x)-f(x)}{\delta x}=\frac{0}{\delta x}=0$
(iv) $\operatorname{Lim}_{k \rightarrow 0} \frac{f(x+\delta x)-f(x)}{\delta x}=\operatorname{Lim}_{k \rightarrow-0}(0)=0$

Thus, $f^{\prime}(x)=0$, that is, $\frac{d}{d x}(c)=0$
(b) $f(x)=x^{2}$
(i) $f(x+\delta x)=(x+\delta x)^{2}$
(ii) $f(x+\delta x)-f(x)=(x+\delta x)^{2}-x^{2}=x^{2}+2 x \delta x+(\delta x)^{2}-x^{2}=(2 x+\delta x) \delta x$
(iii) $\frac{f(x+\delta x)-f(x)}{\delta x}=\frac{(2 x+\delta x) \delta x}{\delta x}=2 x+\delta x ;(\delta x \neq 0)$
(iv) $\operatorname{Lim}_{k \rightarrow 0} \frac{f(x+\delta x)-f(x)}{\delta x}=\operatorname{Lim}_{k \rightarrow 0}(2 x+\delta x)=2 x$
i.e., $\quad f^{\prime}(x)=2 x$

Example 4 Find the derivative of $\sqrt{x}$ at $x=a$ from first principle.
Solution If $f(x)=\sqrt{x}$, then
(i) $f(x+\delta x)=\sqrt{x+\delta x}$ and
(ii) $f(x+\delta x)-f(x)=\sqrt{x+\delta x}-\sqrt{x}$

$$
=\frac{(\sqrt{x+\delta x}-\sqrt{x})(\sqrt{x+\delta x}+\sqrt{x})}{\sqrt{x+\delta x}+\sqrt{x}} \quad \text { (rationalizing the } \text { numerator })
$$

$$
=\frac{x+\delta x-x}{\sqrt{x+\delta x}+\sqrt{x}}
$$

i.e., $f(x+\delta x)-f(x)=\frac{\delta x}{\sqrt{x+\delta x}+\sqrt{x}}$
(iii) Dividing both sides of (1) by $\delta x$, we have

$$
\begin{aligned}
\frac{f(x+\delta x)-f(x)}{\delta x} & =\frac{\delta x}{\delta x(\sqrt{x+\delta x}+\sqrt{x})} \\
& =\frac{1}{\sqrt{x+\delta x}+\sqrt{x}},(\delta x \neq 0)
\end{aligned}
$$

(iv) Taking limit of both the sides as $\delta x \rightarrow 0$, we have

$$
\lim _{\delta x \rightarrow 0} \frac{f(x+\delta x)-f(x)}{\delta x}=\operatorname{Lim}_{\delta x \rightarrow 0}\left(\frac{1}{\sqrt{x+\delta x}+\sqrt{x}}\right)
$$

i.e., $\quad f^{\prime}(x)=\frac{1}{\sqrt{x}+\sqrt{x}}=\frac{1}{2 \sqrt{x}},(x>0)$ and $f^{\prime}(a)=\frac{1}{2 \sqrt{a}}$

Alternate method: Putting $x=a$ in $f(x)=\sqrt{x}$, gives $f(a)=\sqrt{a}$

$$
\text { So, } \quad f(x)-f(a)=\sqrt{x}-\sqrt{a}
$$

Using alternative form for the definition of the derivative, we have

$$
\begin{aligned}
\frac{f(x)-f(a)}{x-a} & =\frac{\sqrt{x}-\sqrt{a}}{x-a} \\
& =\frac{(\sqrt{x}-\sqrt{a})(\sqrt{x}+\sqrt{a})}{(x-a)(\sqrt{x}+\sqrt{a})} \quad \text { (rationalizing the numerator) } \\
& =\frac{x-a}{(x-a)(\sqrt{x}+\sqrt{a})}=\frac{1}{\sqrt{x}+\sqrt{a}},(x \neq a)
\end{aligned}
$$

Taking limit of both the sides of (2) as $x \rightarrow a$, gives

$$
\lim _{x \rightarrow \infty} \frac{f(x)-f(a)}{x-a}=\operatorname{Lim}_{x \rightarrow a} \frac{1}{\sqrt{x}+\sqrt{a}}=\frac{1}{\sqrt{a}+\sqrt{a}}
$$

i.e.,

$$
f^{\prime}(a)=\frac{1}{2 \sqrt{a}}
$$

which is the gradient of $f$ at $x=a$.
Example 5 If $y=\frac{1}{x^{2}}$, then find $\frac{d y}{d x}$ at $x=-1$ by ab-initio method.
Solution Here, $y=\frac{1}{x^{2}}$, so

$$
y+\delta y=\frac{1}{(x+\delta y)^{2}}
$$

Subtracting (i) from (ii), we get

$$
\begin{aligned}
\delta y & =\frac{1}{(x+\delta x)^{2}}-\frac{1}{x^{2}}=\frac{x^{2}-(x+\delta x)^{2}}{x^{2}(x+\delta x)^{2}} \\
& =\frac{\{x+(x+\delta x)\}\{x-(x+\delta x)\}}{x^{2}(x+\delta x)^{2}}
\end{aligned}
$$

$$
=\frac{(2 x+\delta x)(-\delta x)}{x^{2}(x+\delta x)^{2}}=\frac{-\delta x(2 x+\delta x)}{x^{2}(x+\delta x)^{2}}
$$

Dividing both sides of (iii) by $\delta x$, we have

$$
\frac{\delta y}{\delta x}=\frac{-\delta x(2 x+\delta x)}{x^{2}(x+\delta x)^{2} \cdot \delta x}=\frac{-(2 x+\delta x)}{x^{2}(x+\delta x)^{2}}, \quad(\delta x \neq 0)
$$

Taking limit as $\delta x \rightarrow 0$, gives

$$
\begin{aligned}
\lim _{\delta x \rightarrow 0} \frac{\delta y}{\delta x} & =\lim _{\delta x \rightarrow 0} \frac{-(2 x+\delta x)}{x^{2}(x+\delta x)^{2}} \\
& =\frac{-(2 x)}{x^{2}\left(x^{2}\right)} \quad \text { (Using quotient theorem of limits) }
\end{aligned}
$$

i.e., $\frac{d y}{d x}=\frac{-2}{x^{3}}$ and $\left.\frac{d y}{d x}\right|_{x=-1}=\frac{-2}{(-1)^{3}}=\frac{-2}{-1}=2$

# 13.4 Derivation of $x^{n}$ where $n \in Z$

(a) We find the derivative of $x^{n}$ when $n$ is positive integer.
(b) Let $y=x^{n}$. Then

$$
y+\delta y=(x+\delta y)^{n}
$$

and $\quad \delta y=(x+\delta x)^{n}-x^{n}$
Using the binomial theorem, we have

$$
\begin{aligned}
& \delta y=\left[x^{n}+n x^{n-1} \cdot \delta x+\frac{n(n-1)}{2!} x^{n-2}(\delta x)^{2}+\cdots+(\delta x)^{n}\right]-x^{n} \\
& \text { i.e., } \quad \delta y=\delta x\left[n x^{n-1}+\frac{n(n-1)}{2!} x^{n-2} \cdot \delta x+\cdots+(\delta x)^{n-1}\right]
\end{aligned}
$$

Dividing both sides of (i) by $\delta x$, gives

$$
\frac{\delta y}{\delta x}=n x^{n-1}+\frac{n(n-1)}{2!} x^{n-2} \cdot \delta x+\cdots+(\delta x)^{n-1}
$$

Note that each term on the right hand side of (ii) involves $\delta x$ except the first term, so taking the limit as $\delta x \rightarrow 0$, we get $\frac{d y}{d x}=n x^{n-1}$

$$
\text { As } y=x^{n} \text {, so } \frac{d}{d x}\left(x^{n}\right)=n \cdot x^{n-1}
$$

(b) Let $y=x^{n}$ where $n$ is negative integer.

Let $n=-m$ ( $m$ is a positive integer). Then

$$
\begin{aligned}
y=x^{-m} & =\frac{1}{x^{m}} \\
\text { and } y+\delta y & =\frac{1}{(x+\delta x)^{m}}
\end{aligned}
$$

Subtracting (i) from (ii), gives

$$
\begin{aligned}
\delta y & =\frac{1}{(x+\delta x)^{m}}-\frac{1}{x^{m}}=\frac{x^{m}-(x+\delta x)^{m}}{x^{m}(x+\delta x)^{m}} \\
& =\frac{x^{m}-\left[x^{m}+m x^{m-1} \delta x+\frac{m(m-1)}{2!} x^{m-2}(\delta x)^{2}+\ldots \pm(\delta x)^{m}\right]}{x^{m}(x+\delta x)^{m}}
\end{aligned}
$$

(expanding $(x+\delta x)^{m}$ by binomial theorem)

$$
=-\delta x \frac{\left(m x^{m-1}+\frac{m(m-1)}{2!} x^{m-2} \delta x+\cdots+(\delta x)^{m-1}\right)}{x^{m}(x+\delta x)^{m}}
$$

and

$$
\frac{\delta y}{\delta x}=\frac{-1}{x^{m}(x+\delta x)^{m}} \cdot\left(m x^{m-1}+\frac{m(m-1)}{2!} x^{m-2} \cdot \delta x+\cdots+(\delta x)^{m-1}\right)
$$

Taking limit when $\delta x \rightarrow 0$, we get

$$
\begin{aligned}
& \frac{d y}{d x}=\frac{-1}{x^{m} \cdot x^{m}} \cdot m x^{m-1} \text { (all terms contaning } \delta x \text { vanish) } \\
& =-m x^{m-1} \cdot x^{-2 m} \\
& =-m x^{(-m)-1} \\
& \frac{d x}{d x}=n x^{n-1} \quad[\because-m=n] \\
& \text { or } \quad \frac{d(x)}{d x}=n x^{n-1}
\end{aligned}
$$

So, we have proved that $\frac{d}{d x}\left(x^{n}\right)=n x^{n-1}$, if $n \in Z$
The above rule also holds if $n \in Q-Z$, i.e. for rational powers.
For example, $\frac{d}{d x}\left(x^{\frac{2}{3}}\right)=\frac{2}{3} x^{\frac{2}{3}-1}=\frac{2}{3 x^{\frac{1}{3}}}$
The proof of $\frac{d}{d x}\left(x^{n}\right)=n x^{n-1}$ when $n \in Q-Z$ is left as an exercise.

# 13.5 Connection Between Derivatives and Continuity

Calculus is a powerful branch of mathematics that allows us to study change and motion. Two of its foundational concepts of continuity and derivatives are deeply connected. While each concept has its own definition and application, understanding how they relate to each other is essential for solving real-world problems in mathematics.
As discussed in previous units, a function is continuous at a point if its graph has no breaks, jumps, or holes at that point. On the other hand, the derivative of a function at a point measures the instantaneous rate of change or equivalently, the slope of the tangent line at that point. However, this definition depends on the function being wellbehaved around the point. This leads to a well-known result:
If a function is differentiable at a point, it must also be continuous there. This means that differentiability implies continuity, but the reverse is not necessarily true. For example, consider the function $f(x)=|x|$, clearly this function is continuous at $x=0$ (see Figure 13.3). Now we check the differentiability of $f(x)=|x|$ at $x=0$.

$$
\begin{aligned}
f(x) & =|x| \\
f(0) & =|0|=0 \text { and } \\
f(0+\delta x) & =|0+\delta x|=|\delta x| \\
f(0+\delta x)-f(0) & =|\delta x|-0 \\
f(0+\delta x)-f(0) & =|\delta x| \\
& =\frac{|\delta x|}{\delta x}
\end{aligned}
$$

so

$$
f^{\prime}(x)=\lim _{\delta x \rightarrow 0} \frac{\delta x}{\delta x}
$$

Thus $f^{\prime}(x)=\lim _{\delta x \rightarrow 0} \frac{\delta x}{\delta x}$
Because $|\delta x|=\delta x$ when $\delta x>0$
and $|\delta x|=-\delta x$ when $\delta x<0$,
Figure 13.3
so, we consider one-sided limits
$\operatorname{Lim}_{\delta x \rightarrow 0} \frac{|\delta x|}{\delta x}=\operatorname{Lim}_{\delta x \rightarrow 0} \frac{\delta x}{\delta x}=1$ and $\operatorname{Lim}_{\delta x \rightarrow 0} \frac{|\delta x|}{\delta x}=\operatorname{Lim}_{\delta x \rightarrow 0} \frac{-\delta x}{\delta x}=-1$
The right hand and left hand limits are not equal, therefore, the $\operatorname{Lim}_{\delta x \rightarrow 0} \frac{\delta x}{\delta x}$ does not exist. This implies that derivative of $f$ at $x=0$ does not exist, and thus, there is no tangent line to the graph of $f$ at this point (see Figure 13.3). However, the derivative exists at all other points of $f$ i.e., it is 1 on the right side and -1 on the left side. A function can be continuous at a point but not necessarily differentiable there.

# EXERCISE 13.1

1. Find by definition, the derivatives w.r.t. ' $x$ ' of the following functions defined as:
(i) $2 x^{2}+1$
(ii) $2-\sqrt{x}$
(iii) $\frac{1}{\sqrt{x}}$
(iv) $x(x-3)$
2. Find $\frac{d y}{d x}$ from first principle and find gradient of the curve at the given point:
(i) $\sqrt{x+2}$ at $x=6$
(ii) $\frac{1}{\sqrt{x+a}}$ at $x=a$
3. (i) Find the derivative of $x^{2}$ at $x=8$ from the first principle.
(ii) Find the derivative of $x^{2}+2 x+3$ by definition.
4. Find from first principle, the derivatives of the following expressions w.r.t. their respective independent variables:
(i) $(3 x-2)^{2}$
(ii) $(2 t+3)^{3}$
(iii) $(a w+b)^{7}$
5. Find the gradient and equation of the tangent line to $y=3 x^{2}-4 x+1$ at $x=2$.
6. For the function $f(x)=2 x^{2}+x$, calculate the equation of the tangent line at $x=-1$.
7. Find the coordinates of the point of tangency and the equation of the tangent line for $f(x)=x^{3}-2 x+1$ at $x=1$.
8. Find the gradient of the curve $f(x)=3 x^{2}+2 x$ at $x=1$.
9. Find the gradient and an equation of tangent line to the graph of $f(x)=\sqrt{x}$ at $x=9$
10. The position of a car after $t$ hours is given by: $s(t)=2 t^{2}-3 t^{2}+t$ (in kilometres)
(i) Find the average velocity over the interval $[1,4]$
(ii) Find the instantaneous velocity at $t=2$
11. A stone is thrown upwards and its height after $t$ seconds is given by: $s(t)=-16 t^{2}+32 t+10$ (in feet), Find the instantaneous velocity at $t=1$
12. The outdoor temperature (in ${ }^{\circ} \mathrm{C}$ ) over time is modeled by: $T(t)=-t^{2}+12 t+10$, where $t$ is the time in hours. Find the instantaneous rate of change at $t=2$.

### 13.6 Theorems on Differentiation

We have, so far, proved the following two formulas:

1. $\frac{d}{d x}(c)=0$ that is, the derivative of a constant function is zero.
2. $\frac{d}{d x}\left(x^{n}\right)=n x^{n-1}$, power formula (or rule) when $n$ is any real number.

Now we will prove other important formulas (or rules) which are used to determine derivatives of different functions efficiently. Henceforth, in all subsequent discussion, $f, g, h$ etc, all denote functions differentiable at $x$, unless stated otherwise.
3. Derivative of $y=c f(x)$

Proof: Let $y=c f(x)$, Then
(i) $y+\delta y=c f(x+\delta x)$ and
(ii) $y+\delta y-y=c f(x+\delta x)-c f(x)$
or $\delta y=c[f(x+\delta x)-f(x)]$
(Factoring out $c$ )
(iii) $\frac{\delta y}{\delta x}=c\left[\frac{f(x+\delta x)-f(x)}{\delta x}\right]$

Taking limit when $\delta x \rightarrow 0$
(iv) $\operatorname{Lim}_{\delta x \rightarrow 0} \frac{\delta y}{\delta x}=\operatorname{Lim}_{\delta x \rightarrow 0}\left|c-\frac{f(x+\delta x)-f(x)}{\delta x}\right|=c \operatorname{Lim}_{\delta x \rightarrow 0} \frac{f(x+\delta x)-f(x)}{\delta x}$

A constant factor can be taken out from a limit sign.
Thus, $\frac{d y}{d x}=c f^{\prime}(x)$, that is $[c f(x)]^{\prime}=c f^{\prime}(x)$ or $\frac{d}{d x}[c f(x)]=c \frac{d}{d x}[f(x)]$
Example 6 Calculate $\frac{d}{d x}\left(3 x^{\frac{4}{3}}\right)=3 \frac{d}{d x}\left(x^{\frac{4}{3}}\right)$
(Using Formula 3)
$$
3 \times \frac{4}{3} x^{\frac{4}{3}-1}=4 x^{\frac{1}{3}}
$$

(Using power rule)
4. Derivative of a sum or a difference of functions

If $f$ and $g$ are differentiable at $x$, then $f+g, f-g$ are also differentiable at $x$ and

$$
[f(x)+g(x)]=f^{\prime}(x)+g^{\prime}(x), \text { that is, } \frac{d}{d x}[f(x)+g(x)]=\frac{d}{d x}[f(x)]+\frac{d}{d x}[g(x)]
$$

Also $[f(x)-g(x)]=f^{\prime}(x)-g^{\prime}(x)$, that is, $\frac{d}{d x}[f(x)-g(x)]=\frac{d}{d x}[f(x)]-\frac{d}{d x}[g(x)]$
Proof: Let $\phi(x)=f(x)+g(x)$. Then
(i) $\phi(x+\delta x)=f(x+\delta x)+g(x+\delta x)$ and
(ii) $\phi(x+\delta x)-\phi(x)=f(x+\delta x)+g(x+\delta x)-[f(x)+g(x)]$

$$
=[f(x+\delta x)-f(x)+[g(x+\delta x)-g(x)] \quad \text { (rearranging the terms) }
$$

(iii) $\frac{\phi(x+\delta x)-\phi(x)}{\delta x}=\frac{f(x+\delta x)-f(x)}{\delta x}+\frac{g(x+\delta x)-g(x)}{\delta x}$

Taking the limit when $\delta x \rightarrow 0$

(iv) $\operatorname{Lim}_{\delta x \rightarrow 0} \frac{\phi(x+\delta x)-\phi(x)}{\delta x}=\operatorname{Lim}_{\delta x \rightarrow 0}\left[\frac{f(x+\delta x)-f(x)}{\delta x}+\frac{g(x+\delta x)-g(x)}{\delta x}\right]$

$$
=\operatorname{Lim}_{\delta x \rightarrow 0} \frac{f(x+\delta x)-f(x)}{\delta x}+\operatorname{Lim}_{\delta x \rightarrow 0} \frac{g(x+\delta x)-g(x)}{\delta x}
$$

(The limit of a sum is the sum of the limits)

$$
\phi^{\prime}(x)=f^{\prime}(x)+g^{\prime}(x), \text { that is }[f(x)+g(x)]^{\prime}=f^{\prime}(x)+g^{\prime}(x)
$$

or $\quad \frac{d}{d x}[f(x)+g(x)]=\frac{d}{d x}[f(x)]+\frac{d}{d x}[g(x)]$
The proof for the second part is similar.
Note Sum or difference formula can be extended to find derivative of more than two functions.
Example 7 Find the derivative of $y=\frac{3}{4} x^{4}+\frac{2}{3} x^{3}+\frac{1}{2} x^{2}+2 x+5$ w.r.t. $x$.
Solution $y=\frac{3}{4} x^{4}+\frac{2}{3} x^{3}+\frac{1}{2} x^{2}+2 x+5$
Differentiating with respect to $x$, we have
$\frac{d y}{d x}=\frac{d}{d x}\left[\frac{3}{4} x^{4}+\frac{2}{3} x^{3}+\frac{1}{2} x^{2}+2 x+5\right]=\frac{d}{d x}\left(\frac{3}{4} x^{4}\right)+\frac{d}{d x}\left(\frac{2}{3} x^{3}\right)+\frac{d}{d x}\left(\frac{1}{2} x^{2}\right)+\frac{d}{d x}(2 x)+\frac{d}{d x}$
(Using formula 4)

$$
\begin{aligned}
& =\frac{3}{4} \frac{d}{d x}\left(x^{4}\right)+\frac{2}{3} \frac{d}{d x}\left(x^{3}\right)+\frac{1}{2} \frac{d}{d x}\left(x^{2}\right)+2 \frac{d}{d x}(x)+0 \quad \text { (Using formula } 3 \text { and } 1) \\
& =\frac{3}{4}\left(4 x^{4-1}\right)+\frac{2}{3}\left(3 x^{3-1}\right)+\frac{1}{2}\left(2 x^{2-1}\right)+2\left(1 . x^{1-1}\right) \quad \text { (By power formula) } \\
& =3 x^{3}+2 x^{2}+x+2
\end{aligned}
$$

Example 8 Find the derivative of $y=\left(x^{2}+5\right)\left(x^{3}+7\right)$ with respect to $x$.
Solution $y=\left(x^{2}+5\right)\left(x^{3}+7\right)=x^{5}+5 x^{3}+7 x^{2}+35$
Differentiating with respect to $x$, we get

$$
\begin{aligned}
\frac{d y}{d x} & =\frac{d}{d x}\left[x^{2}+5 x^{3}+7 x^{2}+35\right] \\
& =\frac{d}{d x}\left(x^{5}\right)+5 \frac{d}{d x}\left(x^{3}\right)+7 \frac{d}{d x}\left(x^{2}\right)+\frac{d}{d x}(35) \quad \text { (Using formulas } 3 \text { and } 4) \\
& =5 x^{5-1}+5 \times 3 x^{3-1}+7 \times 2 x^{2-1}+0 \\
& =5 x^{4}+15 x^{2}+14 x
\end{aligned}
$$

Example 5 Find the derivative of $y=(2 \sqrt{x}+2)(x-\sqrt{x})$

Solution $y=(2 \sqrt{x}+2)(x-\sqrt{x})$

$$
\begin{aligned}
& =2(\sqrt{x}+1) \cdot \sqrt{x}(\sqrt{x}-1)=2 \sqrt{x}(\sqrt{x}+1)(\sqrt{x}-1) \\
& =2 \sqrt{x}(x-1)=2\left(x^{\frac{3}{2}}-x^{\frac{1}{2}}\right)
\end{aligned}
$$

Differentiating with respect to $x$ we have

$$
\begin{aligned}
\frac{d y}{d x} & =\frac{d}{d x}\left[2\left(x^{\frac{3}{2}}-x^{\frac{1}{2}}\right)\right] \\
& =2\left[\frac{d}{d x} x^{\frac{3}{2}}-\frac{d}{d x} x^{\frac{1}{2}}\right]=2\left[\frac{3}{2} x^{\frac{3}{2}-1}-\frac{1}{2} x^{\frac{1}{2}-1}\right] \\
& =3 x^{\frac{1}{2}}-x^{-\frac{1}{2}}=3 \sqrt{x}-\frac{1}{\sqrt{x}}=\frac{3 x-1}{\sqrt{x}}
\end{aligned}
$$

# 5. Derivative of a Product (The Product Rule)

If $f$ and $g$ are differentiable at $x$, then $f g$ is also differentiable at $x$ and

$$
\begin{gathered}
{[f(x) g(x)]^{\prime}=f^{\prime}(x) g(x)+f(x) g^{\prime}(x) \text {, that is }} \\
\frac{d}{d x}[f(x) g(x)]=\left[\frac{d}{d x}[f(x)]\right] g(x)+f(x)\left[\frac{d}{d x}[g(x)]\right]
\end{gathered}
$$

Proof: Let $\phi(x)=f(x) g(x)$. Then
(i) $\phi(x+\delta x)=f(x+\delta x) g(x+\delta x)$ and
(ii) $\phi(x+\delta x)-\phi(x)=f(x+\delta x) g(x+\delta x)-f(x) g(x)$

Subtracting and adding $f(x) g(x+\delta x)$ in step (ii), gives

$$
\begin{gathered}
\phi(x+\delta x)-\phi(x)=f(x+\delta x) g(x+\delta x)-f(x) g(x+\delta x)+f(x) g(x+\delta x)-f(x) g(x) \\
=[f(x+\delta x)-f(x)] g(x+\delta x)+f(x)[g(x+\delta x)-g(x)]
\end{gathered}
$$

(iii) $\frac{\phi(x+\delta x)-\phi(x)}{\delta x}=\left[\frac{f(x+\delta x)-f(x)}{\delta x}\right] g(x+\delta x)+f(x)\left[\frac{g(x+\delta x)-g(x)}{\delta x}\right]$

Taking limit when $\delta x \rightarrow 0$

(iv) $\lim _{\delta x \rightarrow 0} \frac{\phi(x+\delta x)-\phi(x)}{\delta x}$

$$
\begin{aligned}
& =\lim _{\delta x \rightarrow 0}\left[\frac{f(x+\delta x)-f(x)}{\delta x} \cdot g(x+\delta x)+f(x) \cdot \frac{g(x+\delta x)-g(x)}{\delta x}\right] \\
& =\lim _{\delta x \rightarrow 0} \frac{f(x+\delta x)-f(x)}{\delta x} \cdot \lim _{\delta x \rightarrow 0} g(x+\delta x)+\lim _{\delta x \rightarrow 0} f(x) \cdot \lim _{\delta x \rightarrow 0} \frac{g(x+\delta x)-g(x)}{\delta x}
\end{aligned}
$$

(Using limit theorem)
Thus $\phi^{\prime}(x)=f^{\prime}(x) g(x)+f(x) g^{\prime}(x) \quad\left[\operatorname{Lim}_{\delta x \rightarrow 0} g(x+\delta x)=g(x)\right]$
or $\quad \frac{d}{d x}[f(x) \cdot g(x)]=\frac{d}{d x}[f(x)] \cdot g(x)+f(x)\left[\frac{d}{d x} g(x)\right]$
Example 10 Find derivative of $y=(2 \sqrt{x}+2)(x-\sqrt{x})$ with respect to $x$.
Solution $y=(2 \sqrt{x}+2)(x-\sqrt{x})$

$$
=2(\sqrt{x}+1)(x-\sqrt{x})
$$

Differentiating with respect to $x$, we get

$$
\begin{aligned}
\frac{d y}{d x} & =2 \frac{d}{d x}[(\sqrt{x}+1)(x-\sqrt{x})] \\
& =2\left[\left(\frac{d}{d x}(\sqrt{x}+1)\right)(x-\sqrt{x})+(\sqrt{x}+1) \frac{d}{d x}(x-\sqrt{x})\right] \\
& =2\left[\left(\frac{1}{2} x^{\frac{1}{2}-1}+0\right)(x-\sqrt{x})+(\sqrt{x}+1) \times\left(1-\frac{1}{2} x^{\frac{1}{2}-1}\right)\right] \\
& =2\left[\frac{1}{2 \sqrt{x}}(x-\sqrt{x})+(\sqrt{x}+1) \times\left(1-\frac{1}{2 \sqrt{x}}\right)\right] \\
& =2\left[\frac{x-\sqrt{x}}{2 \sqrt{x}}+(\sqrt{x}+1)\left(\frac{2 \sqrt{x}-1}{2 \sqrt{x}}\right)\right] \\
& =\frac{1}{\sqrt{x}}[x-\sqrt{x}+2 x-\sqrt{x}+2 \sqrt{x}-1] \\
& =\frac{3 x-1}{\sqrt{x}}
\end{aligned}
$$

# 6. Derivative of a Quotient (The Quotient Rule)

If $f$ and $g$ are differentiable at $x$ and $g(x) \neq 0$, for any $x \in D(g)$ then $\frac{f}{g}$ is differentiable at $x$ and $\left(\frac{f(x)}{g(x)}\right)^{\prime}=\frac{f^{\prime}(x) g(x)-f(x) g^{\prime}(x)}{[g(x)]^{2}}$
that is $\frac{d}{d x}\left[\frac{f(x)}{g(x)}\right]=\frac{\left[\frac{d}{d x}[f(x)] g(x)-f(x)\left[\frac{d}{d x}[g(x)]\right.\right.}{[g(x)]^{2}}$
Proof: Let $\phi(x)=\frac{f(x)}{g(x)}$. Then
(i) $\phi(x+\delta x)=\frac{f(x+\delta x)}{g(x+\delta x)}$ and
(ii) $\phi(x+\delta x)-\phi(x)=\frac{f(x+\delta x)}{g(x+\delta x)}-\frac{f(x)}{g(x)}=\frac{f(x+\delta x) g(x)-f(x) g(x+\delta x)}{g(x) g(x+\delta x)}$

Subtracting and adding $f(x) g(x)$ in the numerator of step (ii), gives

$$
\begin{aligned}
\phi(x+\delta x)-\phi(x) & =\frac{f(x+\delta x) g(x)-f(x) g(x)-f(x) g(x+\delta x)+f(x) g(x)}{g(x) g(x+\delta x)} \\
& =\frac{1}{g(x) g(x+\delta x)}[(f(x+\delta x)-f(x)) g(x)-f(x)(g(x+\delta x)-g(x))]
\end{aligned}
$$

(iii) $\frac{\phi(x+\delta x)-\phi(x)}{\delta x}=\frac{1}{g(x) g(x+\delta x)}\left[\frac{f(x+\delta x)-f(x)}{\delta x} \cdot g(x)-f(x) \cdot \frac{g(x+\delta x)-g(x)}{\delta x}\right]$

Taking limit when $\delta x \rightarrow 0$
(iv) $\lim _{\delta x \rightarrow 0} \frac{\phi(x+\delta x)-\phi(x)}{\delta x}$

$$
=\lim _{d x \rightarrow 0}\left[\frac{1}{g(x) g(x+\delta x)}\left(\frac{f(x+\delta x)-f(x)}{\delta x} \cdot g(x)-f(x) \cdot \frac{g(x+\delta x)-g(x)}{\delta x}\right)\right]
$$

Using limit theorems, we have

$$
\phi^{\prime}(x)=\frac{1}{g(x) \cdot g(x)}\left[f^{\prime}(x) g(x)-f(x) g^{\prime}(x)\right] \quad\left(\because \underset{\text { iix } \rightarrow 0}{ } g(x+\delta x)=g(x)\right)
$$

Thus $\quad\left(\frac{f(x)}{g(x)}\right)=\frac{f^{\prime}(x) g(x)-f(x) g^{\prime}(x)}{[g(x)]^{2}}$
or $\quad \frac{d}{d x}\left(\frac{f(x)}{g(x)}\right)=\frac{\left[\frac{d}{d x}(f(x))\right] g(x)-f(x)\left[\frac{d}{d x}(g(x))\right]}{[g(x)]^{2}}$
Example11 Differentiate $\frac{2 x^{2}-3 x^{2}+5}{x^{2}+1}$ with respect to $x$.
Solution Let $\phi(x)=\frac{2 x^{2}-3 x^{2}+5}{x^{2}+1}$. Then

$$
f(x)=2 x^{3}-3 x^{2}+5 \quad \text { and } \quad g(x)=x^{2}+1
$$

Now

$$
f^{\prime}(x)=\frac{d}{d x}\left[2 x^{3}-3 x^{2}+5\right]=2\left(3 x^{2}\right)-3(2 x)+0=6 x^{2}-6 x
$$

and

$$
g^{\prime}(x)=\frac{d}{d x}\left[x^{2}+1\right]=2 x+0=2 x
$$

Using the quotient formula $\phi^{\prime}(x)=\frac{f^{\prime}(x) g(x)-f(x) g^{\prime}(x)}{[g(x)]^{2}}$, We obtain

$$
\begin{aligned}
\frac{d}{d x}\left[\frac{2 x^{3}-3 x^{2}+5}{x^{2}+1}\right] & =\frac{\left(6 x^{2}-6 x\right)\left(x^{2}+1\right)-\left(2 x^{2}-3 x^{2}+5\right)(2 x)}{\left(x^{2}+1\right)^{2}} \\
& =\frac{6 x^{4}-6 x^{3}+6 x^{2}-6 x-\left(4 x^{4}-6 x^{3}+10 x\right)}{\left(x^{2}+1\right)^{2}} \\
& =\frac{6 x^{4}-6 x^{3}+6 x^{2}-6 x-4 x^{4}+6 x^{3}-10 x)}{\left(x^{2}+1\right)^{2}} \\
& =\frac{2 x^{4}+6 x^{3}-16 x}{\left(x^{2}+1\right)^{2}}
\end{aligned}
$$

# EXERCISE 13.2

1. Differentiate w.r.t ' $x$ '.
(i) $x^{4}+2 x^{3}+x^{2}$
(ii) $x^{-3}+2 \overline{x^{2}}+3$
(iii) $\frac{2 x-3}{2 x+1}$
(iv) $\frac{(1+\sqrt{x})(x-x)}{\sqrt{x}}$
(v) $\left(\sqrt{x} \frac{1}{\sqrt{x}}\right)^{2}$
(vi) $(x-5)(3-x)$

(vii) $\frac{\left(x^{2}+1\right)^{2}}{x^{2}-1}$
(viii) $\frac{x^{2}+1}{x^{2}-3}$
(ix) $\frac{2 x-1}{\sqrt{x^{2}+1}}$
(x) $\sqrt{\frac{a-x}{a+x}}$
(xi) $\frac{\sqrt{x^{2}+1}}{\sqrt{x^{2}-1}}$
2. Find $\frac{d y}{d x}$ if $y=\frac{(\sqrt{x}+1)\left(x^{\frac{3}{2}}-1\right)}{x^{\frac{1}{2}}-1},(x \neq 1)$
3. Differentiate $\frac{(\sqrt{x}+1)\left(x^{\frac{3}{2}}-1\right)}{x^{\frac{1}{2}}-x^{\frac{1}{2}}}$ with respect to $x$.
4. If $y=\sqrt{x}-\frac{1}{\sqrt{x}}$, show that $2 x \frac{d y}{d x}+y=2 \sqrt{x}$
5. If $y=x^{4}+2 x^{2}+2$, prove that $\frac{d y}{d x}=4 x \sqrt{y-1}$.

# 13.7 Application of Differentiation

We will apply concept of differentiatioñ to real-world problems such as (profits on diminishing returns, environmental factors, financial investments, population growth, spread of diseases, movement of particles, time-speed in transportation, structural stress, material required that is changes in construction).
Profits on Diminishing Returns
Example 12 A company's profit function is given by $P(x)=100 x-5 x^{2}$, where $x$ is the number of units produced. Determine the marginal profit when $x=8$ units.
Solution The marginal profit is the derivative of the profit function with respect to $x$.
$P^{\prime}(x)=\frac{d}{d x}\left(100 x-5 x^{2}\right)=100-10 x$
Now, substitute $x=8: P^{\prime}(8)=100-10(8)=20$
So, the marginal profit is 20 when 8 units are produced (in the given currency).
Movement of Particles
Example 13 A particle moves along a line according to the position function $s(t)=4 t^{3}-3 t^{2}+2 t$, where $s(t)$ is the position in metres and $t$ is the time in seconds. Find the velocity and acceleration at $t=2$ seconds.
Solution Velocity is the derivative of the position function:

$$
v(t)=\frac{d}{d t}\left(4 t^{3}-3 t^{2}+2 t\right)=12 t^{2}-6 t+2
$$

Substitute $t=2$ :

$$
v(2)=12(2)^{2}-6(2)+2=48-12+2=38
$$

So, the velocity at $t=2$ is $38 \mathrm{~m} / \mathrm{s}$.
Acceleration is the derivative of the velocity function:

$$
a(t)=\frac{d}{d t}\left(12 t^{2}-6 t+2\right)=24 t-6
$$

Substitute $t=2$

$$
a(2)=24(2)-6=48-6=42
$$

So, the acceleration at $t=2$ is $42 \mathrm{~m} / \mathrm{s}^{2}$.

# Financial Investments

Example 14 A bank offers a compound interest rate on an investment, and the value of the investment after $t$ years is given by $V(t)=5000(1+0.04 t)^{2}$. Find the rate of change of the investment value after 10 years.
Solution The rate of change of the investment is the derivative of $V(t)$ with respect to $t$.

$$
\begin{aligned}
& V^{\prime}(t)=\frac{d}{d t}\left(5000(1+0.04 t)^{2}\right)=5000(2)(1+0.04 t)(0.04) \\
& V^{\prime}(t)=400(1+0.04 t)
\end{aligned}
$$

Substitute $t=10$ :

$$
V^{\prime}(10)=400(1+0.04 \times 10)=400(1+0.40)=400 \times 1.4=560
$$

So, the investment is growing at a rate of Rs. 560 per year after 10 years.

## Structural Stress

Example 15 The stress on a beam under a varying load is modeled by $S(x)=500 x-2 x^{2}$, where $S(x)$ is the stress in pascals ( Pa ) and $x$ is the distance (in metres) from the beam's fixed end. Find the rate of change of stress at $x=5$ metres.
Solution The rate of change of stress is the derivative of $S(x)$ with respect to $x$.

$$
S^{\prime}(x)=\frac{d}{d x}\left(500 x-2 x^{2}\right)=500-6 x^{2}
$$

Substitute $x=5$ :

$$
S^{\prime}(5)=500-6(5)^{2}=500-6 \times 25=500-150=350
$$

So, the stress is increasing at a rate of 350 Pa per metre at $x=5$ metres.

## EXERCISE 13.3

1. A car's position at time $t$ is given by $s(t)=5 t^{2}-3 t^{2}+t$. Find the velocity by differentiating the position function with respect to time.
2. Structural stress on a bridge is modeled by the function $S(x)=100-5 x^{2}$, where $x$ is the distance from the center of the bridge. Calculate the rate of change of stress at that point.

3. A company's revenue function is given by $R(x)=1000 x-10 x^{2}$, where is the number of units produced. The cost function is $C(x)=300 x+2000$.
(i) Find the profit function $P(x)$
(ii) Determine the marginal profit when $x=15$
4. An investment grows according to the function $A(t)=10000(1+0.05 t)^{3}$, where $A(t)$ is the value of the investment and $t$ is the time in years.
(i) Find the rate of change of the investment after 8 years.
(ii) What is the investment value after 8 years?
5. The position of a particle moving along a line is given by $s(t)=5 t^{1}-12 t^{2}+8 t$, where $s(t)$ is the position in meters and $t$ is the time in seconds.
(i) Determine the velocity of the particle at $t=4$ seconds
(ii) Find the acceleration at $t=4$ seconds
(iii) When is the particle at rest?
6. The position of a car traveling along a straight highway is given by $x(t)=30 t^{2}-4 t^{3}$, where $x(t)$ is the distance traveled in kilometres and $t$ is the time in hours.
(i) Find the car's velocity at $t=3$ hours.
(ii) Determine the car's acceleration at $t=3$ hours
7. The stress on a beam under a varying load is given by $S(x)=400 x-x^{3}$, where $S(x)$ is the stress in pascals ( Pa ) and $x$ is the distance from the fixed end in metres. Calculate the rate of change of stress at 6 meters.
8. The cost $C(r)$ to construel a cylindrical tank depends on the radius of the base, and is given by $C(r) \leq 8000 \mathrm{~m}^{2}+\frac{150000}{r}$, where the first term represents the cost of the base and the second term represents the cost of the walls. Determine the rate of change of the cost at $r=4$ metres.