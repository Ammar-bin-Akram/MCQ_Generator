# Chapter 5: 3.1.2 Finding Maximum and Minimum Values of Quadratic

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