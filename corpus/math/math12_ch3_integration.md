# Chapter 3: Integration

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