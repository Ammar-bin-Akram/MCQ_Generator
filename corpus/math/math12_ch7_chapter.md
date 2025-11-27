# Chapter 7: CHAPTER

## 6

## Conic Sections

## 6.1 INTRODUCTION

Conic sections or simply conics, are the curves obtained by cutting a (double) right circular cone by a plane. Let $R S$ be a line through the centre $C$ of a given circle and perpendicular to its plane. Let $A$ be a fixed point on $R S$. All lines through $A$ and points on the circle generate a right circular cone. The lines are called rulings or generators of the cone. The surface generated consists of two parts, called nappes, meeting at the fixed point $A$, called the vertex or apex of the cone. The line $\boldsymbol{R} \boldsymbol{S}$ is called axis of the cone.

If the cone is cut by a plane perpendicular to the axis of the cone, then the section is a circle.
The size of the circle depends on how near the plane is to the vertex of the cone. If the plane passes through the vertex $A$, the intersection is just a single point or a point circle. If the cutting plane is slightly tilted and cuts only one nappe of the cone, the resulting section is an ellipse. If the intersecting plane is parallel to a generator of the cone, but intersects its one nappe only, the curve of intersection is a parabola. If the cutting plane is parallel to the axis of the cone and intersects both of its nappes, then the curve of intersection is a hyperbola.

The Greek mathematicians Apollonius' (260-200 B.C.) and Pappus (early fourth century) discovered many intersecting properties of the conic sections. They used the methods of Euclidean geometry to study conics. We shall not study conics from the point of view stated above, but rather approach them with the more powerful tools of analytic geometry.

The theory of conics plays an important role in modern space mechanics, occeangraphy and many other branches of science and technology.

We first study the properties of a Circle. Other conics will be taken up later.

### 6.1.1 Equation of a Circle

The set of all points in the plane that are equally distant from a fixed point is called a circle. The fixed point is called the centre of the circle and the distance from the center of the circle to any point on the circle is called the radius of the circle.

If $C(h, k)$ is centre of a circle, $r$ its radius and $P(x, y)$ any point on the circle, then the circle, denoted $S(C ; r)$ in set notation is

$$
S(C ; r)=\{P(x, y) \mid \overline{C P} \mid r\}
$$

By the distance formula, we get

$$
|\overline{C P}|=\sqrt{(x-h)^{2}+(y-k)^{2}}=r
$$

or $\quad(x-h)^{2}+(y-k)^{2}=r^{2}$
is an equation of the circle in standard form.
If the centre of the circle is the origin, then (1) reduces to

$$
x^{2}+y^{2}=r^{2}
$$

If $r=0$, the circle is called a point circle which consists of the centre only.

Let $P(x, y)$ be any point on the circle (2) and let the inclination of $O P$ be $\theta$ as shown in the figure. It is clear that

$$
\left.\begin{array}{l}
x=r \cos \theta \\
y=r \sin \theta
\end{array}\right\}
$$

The point $P(r \cos \theta, r \sin \theta)$ lies on (2) for all values of $\theta$. Equations (3) are called parametric equations of the circle (2).

Example 1: Write an equation of the circle with centre $(-3,5)$ and radius 7.
Solution: Required equation is

$$
(x+3)^{2}+(y-5)^{2}=7^{2}
$$

or

$$
x^{2}+y^{2}+6 x-10 y-15=0
$$

### 6.1.1 General Form of an Equation of a Circle

Theorem: The equation

$$
x^{2}+y^{2}+2 g x+2 f y+c=0
$$

represents a circle $g, f$ and $c$ being constants.
Equation (1) can be written as:

$$
\left(x^{2}+2 g x+g^{2}\right)+\left(y^{2}+2 f y+f^{2}\right)=g^{2}+f^{2}-c
$$

or

$$
[x-(-g)]^{2}+\left[y-(-f)\right]^{2}=\left(\sqrt{g^{2}+f^{2}-c}\right)^{2}
$$

which is standard form of an equation of a circle with centre $(-g,-f)$ and radius $\sqrt{g^{2}+f^{2}-c}$.
The equation (1) is called general form of an equation of a circle.

## 1. (1) is a second degree equation in which coefficient of each of $x^{2}$ and $y^{2}$ is 1 .
2. (1) contains no term involving the product $x y$.

Thus a second degree equation in which coefficients of $x^{2}$ and $y^{2}$ are equal and there is no product term $x y$ represents a circle.

If three non-collinear points through which a circle passes are known, then we can find the three constants $f, g$ and $c$ in (1).

Example 2: Show that the equation:

$$
5 x^{2}+5 y^{2}+24 x+36 y+10=0
$$

represents a circle. Also find its centre and radius.
Solution: The given equation can be written as:

$$
x^{2}+y^{2}+\frac{24}{5} x+\frac{36}{5} y+2=0
$$

which is an equation of a circle in the general form. Here

$$
g=\frac{12}{5} \cdot f=\frac{18}{5} \cdot c=2
$$

$$
\begin{aligned}
& \text { Thus centre of the circle }=(-g,-f)=\left(\frac{-12}{5}, \frac{-18}{5}\right) \\
& \text { Radius of the circle }=\sqrt{g^{2}+f^{2}-c}=\sqrt{\frac{144}{25}+\frac{324}{25}-2} \\
& =\sqrt{\frac{418}{25}}=\frac{\sqrt{418}}{5}
\end{aligned}
$$

### 6.1.2 Equations of Circles Determined by Given Conditions

The general equation of a circle $x^{2}+y^{2}+2 g x+2 f y+c=0$ contains three independent constants $g, f$ and $c$, which can be found if the equation satisfies three given conditions. We discuss different cases in the following paragraphs.

## 1. A Circle Passing Through Three Non-collincar Points.

If three non-collinear points, through which a circle passes, are known, then we can find the three independent constants $f, g$ and $c$ occurring in the general equation of a circle.

Example 3: Find an equation of the circle which passes through the points $A(5,10), B(6,9)$ and $C(-2,3)$.

Solution: Suppose equation of the required circle is

$$
x^{2}+y^{2}+2 g x+2 f y+c=0
$$

Since the three given points lie on the circle, they all satisfy (1). Substituting the three points into (1), we get

$$
\begin{aligned}
& 25+100+10 g+20 f+c=0 \\
& \Rightarrow \quad 10 g+20 f+c+125=0 \\
& 36+81+12 g+18 f+c+117=0 \\
& \Rightarrow \quad 12 g+18 f+c+117=0 \\
& 4+9-4 g+6 f+c=0 \\
& \quad-4 g+6 f+c+13=0
\end{aligned}
$$

Now we solve the equations (2), (3) and (4).
Subtracting (3) from (2), we have

$$
-2 g+2 f+8=0
$$

or

$$
g-f-4 = 0 \tag{5}
$$

Subtracting (4) from (2), we have.

$$
14g + 14f + 112 = 0 \tag{6}
$$

or

$$
g + f + 8 = 0 \tag{6}
$$

From (5) and (6), we have,

$$
f = -6 \text{ and } g = -2.
$$

Inserting the values of *f* and *g* into (2), we get *c* = 15

Thus equation of the circle is: *x*² + *y*² − 4*x* − 12*y* + 15 = 0

### 2. A circle passing through two points and having its centre on a given line.

**Example 4:** Find an equation of the circle having the join of *A* (*x*₁, *y*₁) and *B* (*x*₂, *y*₂) as a diameter.

**Solution:** Since *AB* is a diameter of the circle, its midpoint is the centre of the circle. The radius of the circle is known and standard form of an equation of the circle may be easily written. However, a more elegant procedure is to make use of the plane geometry. If (*x*, *y*) is any point on the circle, then *m*⊥*APB* = 90°.

Thus the lines *AP* and *BP* are perpendicular to each other.

$$
\text{Slope of } \quad AP = \frac{y - y_1}{x - x_1} \quad \text{and} \quad \text{Slope of } \quad BP \quad \frac{y - y_2}{x - x_2}
$$

By the condition of perpendicularity of two lines, we get

$$
\frac{y - y_1}{x - x_1} \times \frac{y - y_2}{x - x_2} = 1
$$

or

$$
(x - x_1)(x - x_2) + (y - y_1)(y - y_2) = 0
$$

This is required equation of the circle.

### 3. A circle passing through two points and equation of tangent at one of these points is known.

**Example 5:** Find an equation of the circle passing through the point (−2, −5) and touching the line 3*x* + 4*y* − 24 = 0 at the point (4, 3).

**Solution:** Let the circle be

$$
x^2 + y^2 + 2gx + 2fy + c = 0 \tag{1}
$$

The points (−2, −5) and (4, 3) lie on it. Therefore

$$
-4g - 10f + c + 29 = 0 \tag{2}
$$

$$
8g + 6f + c + 25 = 0 \tag{3}
$$

The line

$$
3x + 4y - 24 = 0 \tag{4}
$$

Touches the circle at (4, 3).

A line through (4, 3) and perpendicular to (4) is

$$
y - 3 = \frac{4}{3} \left( x - 4 \right) \quad \text{or} \quad 4x - 3y - 7 = 0
$$

This line being a normal through (4, 3) passes through the centre (−g, −f) of the circle (1). Therefore

$$
-4g + 3f - 7 = 0 \tag{5}
$$

From (2) − (3), we get

$$
-12g - 16f + 4 = 0
$$

or

$$
3g + 4f - 1 = 0 \tag{6}
$$

Solving (5) and (6), we have *g* = −1, *f* = 1. Inserting these values of *g* and *f* into (3), we find *c* = −23. Equation of the required circle is

$$
x^2 + y^2 - 2x + 2y - 23 = 0
$$

### 4. A circle passing through two points and touching a given line.

**Example 6:** Find an equation of the circle passing through the points *A*(1, 2) and *B*(1, −2) and touching the line *x* + 2*y* + 5 = 0.

**Solution:** Let *O*(*h, k*) be the centre of the required circle. Then

$$
\begin{aligned}
& |O A|=|O B|=\text { radius of the circle. } \\
& \text { i.e., } \quad(h-1)^{2}+(k-2)^{2}=(h-1)^{2}+(k+2)^{2} \\
& \text { or } 8 k=0 \quad \text { i.e., } k=0 \\
& \text { Hence }|O A|=|O B| \\
& =\sqrt{(h-1)^{2}+4}
\end{aligned}
$$

Now length of perpendicular from $(h, k)$ i.e., $(h, 0)$ to the line $x+2 y+5=0$ equals the radius of the circle and is given by

$$
\frac{|h+5|}{\sqrt{5}}
$$

Therefore, $\frac{|h+5|}{\sqrt{5}} \cdot|O A|=\sqrt{(h-1)^{2}+4}$
or $\frac{(h+5)^{2}}{5}=(h-1)^{2}+4$ or $4 h^{2}-20 h=0 \quad$ i.e., $h=0,5$
Thus centres of the two circles are at $(0,0)$ and $(5,0)$.
Radius of the first circle $=\sqrt{5} \quad$; Radius of the second circle $=\sqrt{20}$
Equations of the circles are

$$
\begin{array}{lll}
x^{2}+y^{2}=5 & \text { and } & (x-5)^{2}+y^{2}=20 \\
x^{2}+y^{2}=5 & \text { and } & x^{2}+y^{2}-10 x+5=0
\end{array}
$$

## EXERCISE 6.1

1. In each of the following, find an equation of the circle with
(a) centre at $(5,-2)$ and radius 4
(b) centre at $(\sqrt{2},-3 \sqrt{3})$ and radius $2 \sqrt{2}$
(c) ends of a diameter at $(-3,2)$ and $(5,-6)$.
2. Find the centre and radius of the circle with the given equation
(a) $x^{2}+y^{2}+12 x-10 y=0$
(b) $5 x^{2}+5 y^{2}+14 x+12 y-10=0$
(c) $x^{2}+y^{2}-6 x+4 y+13=0$
(d) $4 x^{2}+4 y^{2}-8 x+12 y-25=0$
3. Write an equation of the circle that passes through the given points
(a) $A(4,5), B(-4,-3), C(8,-3)$
(b) $A(-7,7), B(5,-1), C(10,0)$
(c) $A(a, 0), B(0, b), C(0,0)$
(d) $A(5,6), B(-3,2), C(3,-4)$
4. In each of the following, find an equation of the circle passing through
(a) $A(3,-1), B(0,1)$ and having centre at $4 x-3 y-3=0$
(b) $A(-3,1)$ with radius 2 and centre at $2 x-3 y+3=0$
(c) $A(5,1)$ and tangent to the line $2 x-y-10=0$ at $B(3,-4)$
(d) $A(1,4), B(-1,8)$ and tangent to the line $x+3 y-3=0$
5. Find an equation of a circle of radius $a$ and lying in the second quadrant such that it is tangent to both the axes.
6. Show that the lines $3 x-2 y=0$ and $2 x+3 y-13=0$ are tangents to the circle $x^{2}+y^{2}+6 x-4 y=0$
7. Show that the circles
$x^{2}+y^{2}+2 x-2 y-7=0$ and $x^{2}+y^{2}-6 x+4 y+9=0$ touch externally.
8. Show that the circles
$x^{2}+y^{2}+2 x-8=0$ and $x^{2}+y^{2}-6 x+6 y-46=0$ touch internally.
9. Find equations of the circles of radius 2 and tangent to the line $x-y-4=0$ at $A(1,-3)$.

### 6.2 TANGENTS AND NORMALS

A tangent to a curve is a line that touches the curve without cutting through it. We know that for any curve whose equation is given by $y=f(x)$ or $f(x, y)=0$, the derivative is slope of the tangent at any point $P(x, y)$ to the curve. The equation of the tangent to the curve can easily be written by the pointslope formula. The normal to the curve at $P$ is the line through $P$ perpendicular to the tangent to the curve at $P$. This method can be very

conveniently employed to find equations of tangent and normal to the circle $x^{2}+y^{2}+2 g x+2 f y+c=0$ at the point $P\left(x_{1}, y_{1}\right)$.
Here $\quad f\left(x_{1} y\right)=x^{2}+y^{2}+2 g x+2 f y+c=0$
Differentiating (1) w.r.t. $x$, we get

$$
\begin{aligned}
& 2 x+2 y \frac{d y}{d x}+2 g+2 f \frac{d y}{d x}=0 \text { or } \quad \frac{d y}{d x}=\frac{x+g}{y+f} \\
& \left.\frac{d y}{d x}\right]_{x, y, y_{1}}=-\frac{x_{1}+g}{y_{1}+f}=\text { Slope of the tangent at }\left(x_{1}, y_{1}\right)
\end{aligned}
$$

Equation of the Tangent at $P$ is given by

$$
\begin{aligned}
& y-y_{1}=-\frac{x_{1}+g}{y_{1}+f}\left(x-x_{1}\right) \quad \text { (Point-slope form) } \\
& \text { or } \quad y\left(y_{1}+f\right)-y_{1}^{2}-y_{1} f=-x\left(x_{1}+g\right)+x_{1}^{2}+x_{1} g \\
& \text { or } \quad x x_{1}+y y_{1}+g x+f y=x_{1}^{2}+y_{1}^{2}+g x_{1}+f y_{1} \\
& \text { or } \quad x x_{1}+y y_{1}+g x+f y+g x_{1}+f y_{1}+c=x_{1}^{2}+y_{1}^{2}+g x_{1}+f y_{1}+g x_{1}+f y_{1}+c \\
& \text { (adding } g x_{1}+f y_{1}+c \text { to both sides) } \\
& x x_{1}+y y_{1}+g\left(x+x_{1}\right)+f\left(y+y_{1}\right)+c=0 \\
& \text { since } \quad\left(x_{1}, y_{1}\right) \text { lies on (1) and so } \\
& x_{1}^{2}+y_{1}^{2}+2 g x_{1}+2 f y_{1}+c=0
\end{aligned}
$$

Thus $\frac{\left(x_{1}+y y_{1}+g\left(x+x_{1}\right)+f\left(y+y_{1}\right)+c=0\right)}{x_{1}+g}$ is the required equation of the tangent.
To find an equation of the normal at $P$, we note that slope of the normal is

$$
\frac{y_{1}+f}{x_{1}+g} \quad \text { (negative reciprocal of slope of the tangent) }
$$

Equation of the normal at $P\left(x_{1}, y_{1}\right)$ is

$$
y-y_{1}=\frac{y_{1}+f}{x_{1}+g}\left(x-x_{1}\right)
$$

or $\quad \frac{\left(y-y_{1}\right)\left(x_{1}+g\right)=\left(x-x_{1}\right)\left(y_{1}+f\right)}{x_{1}+g}$ is an equation of the normal at $\left(x_{1}, y_{1}\right)$.

## Theorem:

The point $P\left(x_{1}, y_{1}\right)$ lies outside, on or inside the circle $x^{2}+y^{2}+2 g x+2 f y+c=0$ according as

$$
x_{1}^{2}+y_{1}^{2}+2 g x_{1}+2 f y_{1}+c \stackrel{\infty}{\times} \mid 0
$$

Proof. Radius $r$ of the given circle is

$$
r=\sqrt{g^{2}+f^{2}-c}
$$

The point $P\left(x_{1}, y_{1}\right)$ lies outside, on or inside the circle, according as:

$$
m[C P] \stackrel{\infty}{\times} \mid r
$$

i.e., according as: $\quad \sqrt{\left(x_{1}+g\right)^{2}+\left(y_{1}+f\right)^{2}} \stackrel{\infty}{\times} \sqrt{g^{2}+f^{2}-c}$
or according as : $\quad x_{1}^{2}+2 g x_{1}+g^{2}+y_{1}^{2}+f^{2}+2 f y_{1} \stackrel{\infty}{\times} \sqrt[3]{g^{2}+f^{2}-c}$
or according as : $\quad x_{1}^{2}+y_{1}^{2}+2 g x_{1}+2 f y_{1}+c \stackrel{\infty}{\times} \mid 0$.
Example 1: Determine whether the point $P(-5,6)$ lies outside, on or inside the circle: $x^{2}+y^{2}+4 x-6 y-12=0$

Solution: Putting $x=-5$ and $y=6$ in the left hand member of the equation of the circle, we get

$$
25+36-20-36-12=-7<0
$$

Thus the point $P(-5,6)$ lies inside the circle.
Theorem: The line $y=m x+c$ intersects the circle $x^{2}+y^{2}=a^{2}$ in at the most two points.
Proof: It is known from plane geometry that a line can meet a circle in at the most two points.

To prove it analytically, we note that the coordinates of the points where the line

$$
\begin{aligned}
& y=m x+c \\
& \text { intersects the circle } \\
& x^{2}+y^{2}=a^{2}
\end{aligned}
$$

are the simultaneous solutions of the equations (1) and (2).
Substituting the value of $y$ from equation (1) into equation (2), we get

$$
x^{2}+(m x+c)^{2}=a^{2}
$$

or $\quad x^{2}\left(1+m^{2}\right)+2 m c x+c^{2}-a^{2}=0$
This being quadratic in $x$, gives two values of $x$ say $x_{1}$ and $x_{2}$. Thus the line intersects the circle in at the most two points. For nature of the points we examine the discriminant of (3).

The discriminant of (3) is $\left(2 m c\right)^{2}-4\left(1+m^{2}\right)\left(c^{2}-a^{2}\right)$

$$
\begin{aligned}
& =4 m^{2} c^{2}-4\left(1+m^{2}\right)\left(c^{2}-a^{2}\right) \\
& =4 m^{2} c^{2}-4 m^{2} c^{2}-4\left(c^{2}-a^{2}-a^{2} m^{2}\right) \\
& =4\left[-c^{2}+a^{2}\left(1+m^{2}\right)\right]
\end{aligned}
$$

These points are
(i) Real and distinct, if $a^{2}\left(1+m^{2}\right)-c^{2}>0$
(ii) Real and coincident if $a^{2}\left(1+m^{2}\right)-c^{2}=0$
(iii) Imaginary if $a^{2}\left(1+m^{2}\right)-c^{2}<0$

## Condition that the line may be a tangent to the circle.

The line (1) is tangent to the circle (2) if it meets the circle in one point.
i.e., if $c^{2}=a^{2}\left(1+m^{2}\right)$ or $\varepsilon=\alpha \sqrt{1-m^{2}}$
is the condition for (1) to be a tangent to (2).
Example 2: Find the co-ordinates of the points of intersection of the line $2 x+y=5$ and the circle $x^{2}+y^{2}+2 x-9=0$. Also find the length of the intercepted chord.

Solution: From $2 x+y=5$, we have

$$
y=(5-2 x)
$$

Inserting this value of $y$ into the equation of the circle, we get

$$
\begin{aligned}
& x^{2}+(5-2 x)^{2}+2 x-9=0 \\
& \text { or } \quad 5 x^{2}-18 x+16=0 \\
& \Rightarrow \quad x=\frac{18 \pm \sqrt{324-320}}{10} \quad \frac{18 \pm 2}{10} \quad 2, \frac{8}{5}
\end{aligned}
$$

When $x=2, y=5-4=1$
When $x=\frac{8}{5}, y=5-\frac{16}{5}-\frac{9}{5}$

Thus the points of intersection are $P(2,1)$ and $Q\left(\frac{8}{5}, \frac{9}{5}\right)$
Length of the chord intercepted

$$
=\sqrt[3]{P Q}=\sqrt{\left(\frac{8}{5}-2\right)^{2}+\left(\frac{9}{5}-1\right)^{2}}=\sqrt{\frac{4}{25}-\frac{16}{25}}=\frac{2}{\sqrt{5}}
$$

Theorem: Two tangents can be drawn to a circle from any point $P\left(x_{1}, y_{1}\right)$. The tangents are real and distinct, coincident or imaginary according as the point lies outside, on or inside the circle.

Proof: Let an equation of the circle be $x^{2}+y^{2}=a^{2}$
We have already seen that the line

$$
y=m x+a \sqrt{1+m^{2}}
$$

is a tangent to the given circle for all values of $m$. If it passes through the point $P\left(x_{1}, y_{1}\right)$, then

$$
\begin{aligned}
& y_{1}=m x_{1}+a \sqrt{1+m^{2}} \\
& \text { or } \quad\left(y_{1}-m x_{1}\right)^{2}=a^{2}\left(1+m^{2}\right) \\
& \text { or } \quad m^{2}\left(x_{1}^{2}-a^{2}\right)-2 m x_{1} y_{1}+y_{1}^{2}-a^{2}=0
\end{aligned}
$$

This being quadratic in $m$, gives two values of $m$ and so there are two tangents from $P\left(x_{1}, y_{1}\right)$ to the circle. These tangents are real and distinct, coincident or imaginary according as the roots of (2) are real and distinct, coincident or imaginary
i.e., according as $x_{1}^{2} y_{1}^{2}-\left(x_{1}^{2}-a^{2}\right)\left(y_{1}^{2}-a^{2}\right) \stackrel{\text { o }}{=} 0$
or $\quad x_{1}^{2} a^{2}+y_{1}^{2} a^{2}+a^{2} \stackrel{\text { o }}{=} 0 \quad$ or $\quad x_{1}^{2}+y_{1}^{2}-a^{2} \stackrel{\text { o }}{=} 0$
i.e., according as the point $P\left(x_{1}, y_{1}\right)$ lies outside, on or inside the circle $x^{2}+y^{2}-a^{2}=0$

Example 3: Write equations of two tangents from $(2,3)$ to the circle $x^{2}+y^{2}=9$.
Solution. Any tangent to the circle is

$$
y=m x+3 \sqrt{1+m^{2}}
$$

If it passes through $(2,3)$, then

$$
\begin{aligned}
& 3=2 m+3 \sqrt{1+m^{2}} \\
\text { or } & (3-2 m)^{2} \equiv 9\left(1+m^{2}\right) \\
\text { or } & 9-12 m+4 m^{2} \equiv 9+9 m^{2} \\
& \text { or } \quad 5 m^{2}+12 m=0 \quad \text { i.e., } m=0, \frac{-12}{5}
\end{aligned}
$$

Inserting these values of $m$ into (1), we have equations of the tangents from $(2,3)$ to the circle as :

$$
\begin{aligned}
& \text { For } m=0: y=0 . x+3 \sqrt{1+0} \\
& \text { or } y=3 \\
& \text { For } m=\frac{-12}{5}: y=\frac{-12}{5} x+3 \sqrt{1+\frac{144}{25}}=\frac{-12}{5} x+\frac{39}{5} \\
& \text { or } \quad 5 y+12 x-39=0
\end{aligned}
$$

Example 4: Write equations of the tangents to the circle

$$
x^{2}+y^{2}-4 x+6 y+9 \equiv 0
$$

at the points on the circle whose ordinate is -2 .

Solution: Substituting $y=-2$ into (1), we get

$$
\begin{aligned}
& x^{2}-4 x+1 \equiv 0 \\
& \text { or } \quad x=\frac{4 \pm \sqrt{16-4}}{2} \quad \pm 2 \quad \sqrt{3}
\end{aligned}
$$

The points on the circle with ordinate -2 are

$$
(2+\sqrt{3},-2),(2-\sqrt{3},-2)
$$

Equations of the tangents to (1) at these points are

$$
\begin{aligned}
& (2+\sqrt{3}) x-2 y-2(x+2+\sqrt{3})+3(y-2)+9=0 \\
& \text { and } \quad(2-\sqrt{3}) x-2 y-2(x+2-\sqrt{3})+3(y-2)+9=0 \\
& \text { i.e., } \quad \sqrt{3} x+y-2 \sqrt{3}-1=0 \\
& \text { and } \quad-\sqrt{3} x+y+2 \sqrt{3}-1=0
\end{aligned}
$$

## Example 5: $\quad$ Find a joint equation to the pair of tangents drawn from $(5,0)$ to the circle:

$$
x^{2}+y^{2}=9
$$

Solution: Let $P(h, k)$ be any point on either of the two tangents drawn from $A(5,0)$ to the given circle (1). Equation of $P A$ is

$$
y-0=\frac{k-0}{h-5}(x-5) \quad \text { or } k x-(h-5) y-5 k=0
$$

Since (2) is tangent to the circle (1), the perpendicular distance of (2) from the centre of the circle equals the radius of the circle.
i.e., $\quad \frac{|-5 k|}{\sqrt{k^{2}+(h-5)^{2}}}=3$
or $\quad 25 k^{2}=9\left[k^{2}+(h-5)^{2}\right]$ or $16 k^{2}-9(h-5)^{2}=0$
Thus $(h, k)$ lies on

$$
9(x-5)^{2}-16 y^{2} \equiv 0
$$

But $(h, k)$ is any point of either of the two tangents.
Hence (3) is the joint equations of the two tangents.

### 6.2.1 Length of the tangent to a circle (Tangential Distance)

Let $P\left(x_{i}, y_{i}\right)$ be a point outside the circle

$$
x^{2}+y^{2}+2 g x+2 f y+c \equiv 0
$$

We know that two real and distinct tangents can be drawn to the circle from an external point $P$. If the points of contact of these tangents with the circle are $S$ and $T$, then each of the length $P S$ and $P T$ is called length of the tangent or tangential distance from $P$ to the circle (1).

The centre of the circle has coordinates $(-g,-f)$. Join $P O$ and $O T$. From the right triangle $O P T$ we have,

$$
\begin{aligned}
\text { length of the tangent } & =\frac{|P T|}{\sqrt{O P^{2}-O T^{2}}} \\
& =\sqrt{\left(x_{i}+g\right)^{2}+\left(y_{i}+f\right)^{2}-\left(g^{2}+f^{2}-c\right)}
\end{aligned}
$$

version: 1.1

$$
=\sqrt{x_{1}^{2}+y_{1}^{2}+2 g x_{1}+2 f y_{1}+c}
$$

It is easy to see that length of the second tangent $\overrightarrow{P S}$ also equals (2).
Example 6: Find the length of the tangent from the point $P(-5,10)$ to the circle

$$
5 x^{2}+5 y^{2}+14 x+12 y-10=0
$$

Solution: Equation of the given circle in standard form is

$$
x^{2}+y^{2}+\frac{14}{5} x+\frac{12}{5} y-2=0
$$

Square of the length of the tangent from $P(-5,10)$ to the circle (1) is obtained by substituting -5 for $x$ and 10 for $y$ in the left hand member of (1)

$$
\therefore \quad \text { Required length } \quad=\sqrt{(-5)^{2}+(10)^{2}-14+24-2}=\sqrt{133}
$$

Example 7: Write equations of the tangent lines to the circle $x^{2}+y^{2}+4 x+2 y=0$ drawn from $P(-1,2)$. Also find the tangential distance.

Solution: An equation of the line through $P(-1,2)$ having slope $m$ is

$$
y-2=m(x+1) \text { or } \quad m x-y+m+2=0
$$

Centre of the circle is $C(-2,-1)$.

$$
\text { Radius }=\sqrt{4+1}=\sqrt{5}
$$

If (1) is tangent to the circle, then its distance from the centre of the circle equals the radius of the circle. Therefore

$$
\frac{[-2 m+1+m+2]}{\sqrt{m^{2}+1}}=\sqrt{5}
$$

or $\quad(-m+3)^{2}=5\left(m^{2}+1\right)$
or $\quad 4 m^{2}+6 m-4=0$ or $2 m^{2}+3 m-2=0$

$$
m=\frac{-3 \pm \sqrt{9+16}}{4}=\frac{-3 \pm 5}{4}=-2, \frac{1}{2}
$$

Equations of the tangents are from equation (1)

$$
\text { version: } 1.1
$$

For $m=-2:-2 x-y=0$ or $2 x+y=0$
For $m=\frac{1}{2}: \frac{1}{2} x-y+\frac{5}{2}=0$ or $x-2 y+5=0$
Tangential distance $=\sqrt{1+4-4+4}=\sqrt{5}$
Example 8: Tangents are drawn from $(-3,4)$ to the circle $x^{2}+y^{2}=21$. Find an equation of the line joining the points of contact (The line is called the chord of contact).

Solution: Let the points of contact of the two tangents be $P\left(x_{1}, y_{1}\right)$ and $Q\left(x_{2}, y_{2}\right)$
An equation of the tangent at $P$ is

$$
x x_{1}+y y_{1}=21
$$

An equation of the tangent at $Q$ is

$$
x x_{2}+y y_{2}=21
$$

Since (1) and (2) pass through $(-3,4)$, so

$$
-3 x_{1}+4 y_{1}=21
$$

and $-3 x_{2}+4 y_{2}=21$
(3) and (4) show that both the points $P\left(x_{1}, y_{1}\right), Q\left(x_{2}, y_{2}\right)$ lie on $-3 x+4 y=21$ and so it is the required equation of the chord of contact.

## EXERCISE 6.2

1. Write down equations of the tangent and normal to the circle
(i) $x^{2}+y^{2}=25$ at $(4,3)$ and at $(5 \cos \theta, 5 \sin \theta)$
(ii) $3 x^{2}+3 y^{2}+5 x-13 y+2=0$ at $\left(1, \frac{10}{3}\right)$
2. Write down equations of the tangent and normal to the circle $4 x^{2}+4 y^{2}-16 x+24 y-117=0$
at the points on the circle whose abscissa is -4 .
3. Check the position of the point $(5,6)$ with respect to the circle
(i) $x^{2}+y^{2}=81$
(ii) $2 x^{2}+2 y^{2}+12 x-8 y+1=0$
4. Find the length of the tangent drawn from the point $(-5,4)$ to the circle $5 x^{2}+5 y^{2}-10 x+15 y-131=0$

**5.** Find the length of the chord cut off from the line 2*x* + 3*y* = 13 by the circle *x*<sup>2</sup> + *y*<sup>2</sup> = 26

**6.** Find the coordinates of the points of intersection of the line *x* + 2*y* = 6 with the circle: *x*<sup>2</sup> + *y*<sup>2</sup> – 2*x* – 2*y* – 39 = 0

**7.** Find equations of the tangents to the circle *x*<sup>2</sup> + *y*<sup>2</sup> = 2
- (i) parallel to the line *x* – 2*y* + 1 = 0
- (ii) perpendicular to the line 3*x* + 2*y* = 6

**8.** Find equations of the tangents drawn from
- (i) (0, 5) to *x*<sup>2</sup> + *y*<sup>2</sup> = 16
- (ii) (−1, 2) to *x*<sup>2</sup> + *y*<sup>2</sup> + 4*x* + 2*y* = 0
- (iii) (−7, −2) to (*x* + 1)<sup>2</sup> + (*y* – 2)<sup>2</sup> = 26

Also find the points of contact

**9.** Find an equation of the chord of contact of the tangents drawn from (4, 5) to the circle *2x*<sup>2</sup> + 2*y*<sup>2</sup> – 8*x* + 12*y* + 21 = 0

### **6.3 ANALYTIC PROOFS OF IMPORTANT PROPERTIES OF A CIRCLE**

A line segment whose end points lie on a circle is called a **chord** of the circle. A **diameter** of a circle is a chord containing the centre of the circle.

**Theorem:** Length of a diameter of the circle *x*<sup>2</sup> + *y*<sup>2</sup> = *a*<sup>2</sup> is 2*a*.

**Proof:** Let *AOB* be a diameter of the circle

*a*<sup>2</sup> + *y*<sup>2</sup> = *a*<sup>2</sup>

(1)

*O*(0,0) is center of (1).

Let the coordinates of *A* be (*x*<sub>*1*</sub>, *y*<sub>*1*</sub>).

Equation of *AOB* is

$$
y = \frac{y_1}{x_1} x \qquad \text{(2)}
$$

Substituting the value of *y* from (2) into (1), we have

$$
x^2 + \frac{y_1^2}{x_1^2} x^2 = a^2 \quad \text{or} \quad x^2 (x_1^2 + y_1^2) = a^2 x_1^2
$$

or

$$
a^2 x^2 = a^2 x_1^2 \qquad \qquad \qquad \qquad \text{(3/ } x_1^2 + y_1^2 = x^2)
$$

i.e.,

$$
x = \pm x_1
$$

If

$$
x = x_1, \quad \text{then} \quad y = y_1 \qquad \text{(4/ } y = \frac{y_1}{x_1} x)
$$

Similarly when

$$
x = -x_1, \quad \text{then} \qquad y = -y_1
$$

Thus *B* has coordinates (−*x*<sub>*1*</sub>, −*y*<sub>*1*</sub>).

Length of diameter *AB* = $$\sqrt{(x_1 + x_1)^2 + (y_1 + y_1)^2}$$

$$
= \sqrt{4(x_1^2 + y_1^2)} = \sqrt{4a^2} = 2a
$$

**Theorem 2:** Perpendicular dropped from the centre of a circle on a chord bisects the chord.

**Proof:** Let *x*<sup>2</sup> + *y*<sup>2</sup> = *a*<sup>2</sup> be a circle, in which *AB* is a chord with end points *A*(*x*<sub>*1*</sub>, *y*<sub>*1*</sub>), *B*(*x*<sub>*2*</sub>, *y*<sub>*2*</sub>) on the circle and *OM* is perpendicular from the centre to the chord. We need to show that *OM* bisects the chord *AB*.

$$
\text{Slop of } AB = \frac{y_2 - y_1}{x_2 - x_1}
$$

$$
\text{Slop of perpendicular to } AB = \frac{-(x_2 - x_1)}{y_2 - y_1} = \frac{x_2 - x_1}{y_2 - y_1} = m \text{ (say)}
$$

So equation of *OM* with slope *m* and point *O*(0,0) on it, is given by

$$
y - 0 = \frac{(x_1 - x_1)}{(y_2 - y_1)}(x - 0) \qquad \text{(point - slope form)}
$$

or

$$
y = \left(\frac{x_1 - x_1}{y_2 - y_1}\right)x \qquad \text{(1)}
$$

(1) is the equation of the perpendicular $O M$ from centre to the chord. We will show that it bisects the chord i.e., intersection of $O M$ and $A B$ is the midpoint of $A B$.

Equation of $A B$ is

$$
y-y_{1}=\frac{y_{1}-y_{2}}{x_{1}-x_{2}}\left(x-x_{1}\right)
$$

The foot of the perpendicular $O M$ is the point of intersection of (1) and (2). Inserting the value of $y$ from (1) into (2), we have

$$
\begin{aligned}
& -\frac{x_{1}-x_{2}}{y_{1}-y_{2}} x-y_{1}=\frac{y_{1}-y_{2}}{x_{1}-x_{2}}\left(x-x_{1}\right) \\
\text { or } & x\left(\frac{y_{1}-y_{2}}{x_{1}-x_{2}}+\frac{x_{1}-x_{2}}{y_{1}-y_{2}}\right)=\frac{x_{1}\left(y_{1}-y_{2}\right)}{x_{1}-x_{2}}-y_{1} \\
\text { or } & \frac{x\left[y_{1}^{2}+y_{2}^{2}-2 y_{1} y_{2}+x_{1}^{2}+x_{2}^{2}-2 x_{1} x_{2}\right]}{\left(x_{1}-x_{2}\right)\left(y_{1}-y_{2}\right)}=\frac{x_{2} y_{1}-x_{1} y_{2}}{x_{1}-x_{2}} \\
\text { or } & x\left(2 a^{2}-2 x_{1} x_{2}-2 y_{1} y_{2}\right)=x_{2} y_{1}^{2}-x_{1} y_{1} y_{2}-x_{2} y_{1} y_{2}+x_{1} y_{2}^{2} \\
\text { or } & 2 x\left(a^{2}-x_{1} x_{2}-y_{1} y_{2}\right)=x_{2}\left(a^{2}-x_{1}^{2}\right)-y_{1} y_{2}\left(x_{1}+x_{2}\right)+x_{1}\left(a^{2}-x_{2}^{2}\right) \\
& \quad=a^{2}\left(x_{1}+x_{2}\right)-x_{1} x_{2}\left(x_{1}+x_{2}\right)-y_{1} y_{2}\left(x_{1}+x_{2}\right) \\
& \quad=\left(x_{1}+x_{2}\right)\left(a^{2}-x_{1} x_{2}-y_{1} y_{2}\right)
\end{aligned}
$$

(The points $\left(x_{1}, y_{1}\right)$ and $\left(x_{2}, y_{2}\right)$ lie on the circle)
or $\quad x=\frac{x_{1}+x_{2}}{2}$
Putting $\quad x=\frac{x_{1}+x_{2}}{2} \quad$ into (1), we get

$$
y=\frac{\left(x_{1}-x_{2}\right)}{y_{2}-y_{1}} \frac{\left(x_{1}+x_{2}\right)}{2} \quad \frac{x_{1}^{2}-x_{2}^{2}}{2\left(y_{2}-y_{1}\right)}
$$

or $\quad y=\frac{y_{2}^{2}-y_{1}^{2}}{2\left(y_{2}-y_{1}\right)}=\frac{\left(y_{2}-y_{1}\right)\left(y_{2}+y_{1}\right)}{2\left(y_{2}-y_{1}\right)} \quad\left[\begin{array}{l}x_{1}^{2}+y_{2}^{2}=a^{2} \\ x_{2}^{2}+y_{2}^{2}=a^{2} \\ \Rightarrow x_{1}^{2}-x_{2}^{2}=y_{1}^{2}-y_{2}^{2}\end{array}\right]$
So, $\quad\left(\frac{x_{1}+x_{2}}{2}, \frac{y_{1}+y_{2}}{2}\right)$ is the point of intersection of $O M$ and $A B$ which is the midpoint of $A B$.
version: 1.1

## Theorem 3:

The perpendicular bisector of any chord of a circle passes through the centre of the circle.

Proof: $\quad$ Let $x^{2}+y^{2}=a^{2}$ be a circle and $A\left(x_{1}, y_{1}\right)$,
$B\left(x_{2}, y_{2}\right)$ be the end points of a chord of this circle. Let $M$ be the mid point of $A B$, i.e.
$M\left(\frac{x_{1}+x_{2}}{2}, \frac{y_{1}+y_{2}}{2}\right)$
The slop of $A B=\frac{y_{2}-y_{1}}{x_{2}-x_{1}}$
The slope of perpendicular bisector of $A B$ is
$$
-\left(\frac{x_{2}-x_{1}}{y_{2}-y_{1}}\right)
$$

So, equation of perpendicular bisector in point-slope form, is

$$
y-\frac{y_{1}+y_{2}}{2}=\left(\frac{x_{2}-x_{1}}{y_{2}-y_{1}}\right)\left(x-\frac{x_{1}+x_{2}}{2}\right)
$$

We check whether the centre $(0,0)$ of the circle lies on (1) or not

$$
\begin{aligned}
& 0-\frac{y_{1}+y_{2}}{2}=\frac{-\left(x_{2}-x_{1}\right)}{\left(y_{2}-y_{1}\right)}\left(0-\frac{x_{1}+x_{2}}{2}\right) \\
\text { or } & -\left(\frac{y_{1}+y_{2}}{2}\right)\left(y_{2}-y_{1}\right)=\left(x_{2}-x_{1}\right) \frac{\left(x_{1}+x_{2}\right)}{2} \\
\text { or } & -\left(y_{2}^{2}-y_{1}^{2}\right)=x_{2}^{2}-x_{1}^{2} \text { or } x_{1}^{2}+y_{1}^{2}=x_{2}^{2}+y_{2}^{2} \\
\text { or } & a^{2}=a^{2} \quad \text { which is true }
\end{aligned}
$$

Hence the perpendicular bisector of any chord passes through the centre of the circle.

## Theorem 4:

The line joining the centre of a circle to the midpoint of a chord is perpendicular to the chord.

Proof: $\quad$ Let $A\left(x_{1}, y_{1}\right), B\left(x_{2}, y_{2}\right)$ be the end points of any chord the circle $x^{2}+y^{2}=a^{2} . O(0,0)$

is centre of the circle and *M* [ *x*<sup>1</sup> + *x*<sup>2</sup> + *y*<sup>1</sup> + *y*<sup>2</sup> ] is the midpoint of *AB*. Join the centre *O* with the mid point *M*. We need to show that *OM* is perpendicular to *AB* i.e., product of slopes of *AB* and *OM* is –1.

Slope of *AB* = *m*<sup>1</sup> = *x*<sup>1</sup> − *y*<sup>1</sup> *x*<sup>2</sup> − *x*<sup>1</sup> Slope of *OM* *m*<sup>2</sup> = *x*<sup>2</sup> − *y*<sup>2</sup> *x*<sup>2</sup> − *x*<sup>1</sup> *x*<sup>2</sup> − *x*<sup>1</sup> *2*

$$\therefore m_m = \frac{y_2 - y_1}{x_2 - x_1} \cdot \frac{y_2 + y_1}{x_2 + x_1} = \frac{y_2^2 - y_1^2}{x_2^2 - x_1^2} \tag{1}$$

As *A* and *B* lie on the circle, so

$$x_1^2 + y_1^2 = a^2 \quad \text{and} \quad x_2^2 + y_2^2 = a^2$$

Their subtraction gives *x*<sup>1</sup> − *x*<sup>2</sup> + *y*<sup>1</sup> − *y*<sup>2</sup> = 0

or *y*<sup>2</sup> − *y*<sup>1</sup> = *x*<sup>1</sup> − *x*<sup>2</sup> = −(*x*<sup>2</sup> − *x*<sup>1</sup>)

Putting this value in (1), we get

$$m_m = \frac{(x_1^2 - x_1^1)}{(x_2^2 - x_2^1)} \quad \text{I}$$

So *OM* is perpendicular to *AB*.

**Theorem 5:** Congruent chords of a circle are equidistant from the centre.

**Proof:** Let *x*<sup>2</sup> + *y*<sup>2</sup> = *a*<sup>2</sup> be the circle in which *AB* and *CD* are two congruent chords i.e., |*AB*| = |*CD*| and the coordinates of *A*, *B*, *C* and *D* be as in the figure. Also let *OM* and *ON* be the perpendicular distances of the chords from the centre (0, 0)(*x*<sub>1</sub>, *y*<sub>1</sub>) of the circle.

We know from Theorem 2 that *M* and *N* are the midpoints of *AB* and *CD* respectively.

**Theorem 6:** Show that measure of the central angle of a minor arc is double the measure of the angle subtended in the corresponding major arc.

**Proof:** Let the circle be *x*<sup>2</sup> + *y*<sup>2</sup> = *a*<sup>2</sup>. *A*(*a* cosθ<sub>1</sub>, *a* sinθ<sub>1</sub>) and *B*(*a* cosθ<sub>2</sub>, *a* sinθ<sub>2</sub>) be end points of a minor arc *AB*. Let *P* (*a* cosθ, *a* sinθ) be a point on the major arc. Central angle subtended by the minor arc *AB* is ∠ *AOB* = θ<sub>2</sub> − θ<sub>1</sub>.

We need to show *m*∠*APB* = $$\frac{1}{2}(\theta_1 - \theta_1)$$

**6.** *Conic Sections* **eLearn.Punjab**

### 6. *Conic Sections* **eLearn.Punjab**

**Theorem 1.1**

**Theorem 1.1**

$$
\begin{aligned}
m_{1}= & \text { slope of } A P \quad \frac{a(\sin \theta-\sin \theta_{1})}{a(\cos \theta-\cos \theta_{1})} \quad \frac{2 \cos \theta+\theta_{1}}{2} \sin \frac{\theta-\theta_{1}}{2} \\
& =\cot \left(\frac{\theta+\theta_{1}}{2}\right)-\tan \left(\frac{\pi}{2}-\frac{\theta+\theta_{1}}{2}\right)
\end{aligned}
$$

Similarly, (by symmetry)

$$
\begin{aligned}
& m_{2}=\text { slope-of } B P \quad+\tan \left(\frac{\pi}{2}-\frac{\theta+\theta_{2}}{2}\right) \\
& \tan \angle A P B=\frac{m_{2}-m_{1}}{1+m_{1} m_{2}}=\frac{\tan \left(\frac{\pi}{2}+\frac{\theta+\theta_{2}}{2}\right)-\tan \left(\frac{\pi}{2}+\frac{\theta+\theta_{1}}{2}\right)}{1+\tan \left(\frac{\pi}{2}+\frac{\theta+\theta_{1}}{2}\right) \tan \left(\frac{\pi}{2}+\frac{\theta+\theta_{2}}{2}\right)} \\
& =\tan \left(\frac{\pi}{2}+\frac{\theta+\theta_{2}}{2}-\frac{\pi}{2}-\frac{\theta+\theta_{1}}{2}\right)=\tan \left(\frac{\theta_{2}-\theta_{1}}{2}\right) \\
& \text { Hence } m \angle A P B=\frac{1}{2}\left(\theta_{2}-\theta_{1}\right)
\end{aligned}
$$

Theorem 7: An angle in a semi-circle is a right angle.
Proof: Let $x^{2}+y^{2}=a^{2}$ be a circle, with centre $O$. Let $A O B$ be any diameter of the circle and $P\left(x_{1}, y_{1}\right)$ be any point on the circle.

We have to show that $m \angle A P B=90^{\circ}$.
Suppose the coordinates of $A$ are $\left(x_{1}, y_{1}\right)$.
Then $B$ has coordinates
$\left\{-x_{1},-y_{1}\right\}$.
(Slope of $A P=\frac{y_{1}-y_{2}}{x_{1}-x_{2}}=m_{1}$, say
Slope of $B P=\frac{y_{1}+y_{2}}{x_{1}+x_{2}}=m_{2}$, say
Challenged
State and prove the converse of this Theorem.

$$
m_{1} m_{2}=\frac{y_{1}^{2}-y_{2}^{2}}{x_{1}^{2}-x_{2}^{2}}
$$

Since $A\left(x_{1}, y_{1}\right)$ and $P\left(x_{2}, y_{2}\right)$ lie on the circle, we have

$$
\begin{aligned}
& x_{1}^{2}+y_{1}^{2}=a^{2} \Rightarrow x_{1}^{2}=a^{2}-y_{1}^{2} \\
& x_{2}^{2}+y_{2}^{2}=a^{2} \Rightarrow x_{2}^{2}=a^{2}-y_{2}^{2}
\end{aligned}
$$

Substituting the values of $x_{1}^{2}$ and $x_{2}^{2}$ from (2) into (1), we get

$$
m_{1} m_{2}=\frac{y_{1}^{2}-y_{2}^{2}}{\left(a^{2}-y_{1}^{2}\right)-\left(a^{2}-y_{2}^{2}\right)}=\frac{y_{1}^{2}-y_{2}^{2}}{-\left(y_{1}^{2}-y_{2}^{2}\right)}=-1
$$

Thus $A P \perp B P$ and so $m \angle A P B=90^{\circ}$

Theorem 8: The tangent to a circle at any point of the circle is perpendicular to the radial segment at that point.

Proof: Let $P T$ be the tangent to the circle $x^{2}+y^{2}=a^{2}$ at any point $P\left(x_{1}, y_{1}\right)$ lying on it. We have to show that the radial segment $O P \perp P T$.

Differentiating $x^{2}+y^{2}=a^{2}$, we have

$$
2 x+2 y \frac{d y}{d x}=0 \Rightarrow \frac{d y}{d x}=\frac{x}{y}
$$

Slope of the tangent at $P=\frac{d y}{d x} \frac{1}{2}=\frac{-x_{1}}{y_{1}}$
Slope of $O P=\frac{y_{1}-0}{x_{1}-0}-\frac{y_{1}}{x_{1}}$
Product of slopes of $O P$ and $P T=\frac{-x_{1}}{y_{1}} \frac{y_{1}}{x_{1}}=-1$
Thus $O P \perp P T$.

Theorem 9: The perpendicular at the outer end of a radial segment is tangent to the circle.

Proof: Let $P T$ be the perpendicular to the outer end of the radial segment $O P$ of the circle $x^{2}+y^{2} \equiv a^{2}$. We have to show that $P T$ is tangent to the circle at $P$. Suppose the coordinates of $P$ are $\left(x_{1}, y_{1}\right)$.

Since $P T$ is perpendicular to $O P$ so
Slope of $P T=\frac{-1}{\text { slope of } O P} \cdot \frac{-1}{y_{1}} \cdot \frac{-x_{1}}{y_{1}}$
Equation of $P T$ is $y-y_{1}=\frac{-x_{1}}{y_{1}}\left(x-x_{1}\right)$
or $y y_{1}-y^{2}=-x x_{1}+x_{1}^{2}$
or $y y_{1}+x x_{1}=y_{1}^{2}+x_{1}^{2}=a^{2} \quad(\because P$ lies on the circle $)$
or $y y_{1}+x x_{1}-a^{2}=0$
Distance of $P T$ from $O$ (centre of the circle)

$$
=\frac{\left[y_{1}(0)+x_{1}(0)-a^{2}\right]}{\sqrt{x^{2}+y^{2}}} \cdot \frac{\left|a^{2}\right|}{\sqrt{a^{2}}} \cdot \frac{a^{2}}{a} \quad a \quad \text { (radius of the circle) }
$$

Thus $P T$ is tangent to the circle at $P\left(x_{1}, y_{1}\right)$.

## EXERCISE 6.3

1. Prove that normal lines of a circle pass through the centre of the circle.
2. Prove that the straight line drawn from the centre of a circle perpendicular to a tangent passes through the point of tangency.
3. Prove that the mid point of the hypotenuse of a right triangle is the circumcentre of the triangle.
4. Prove that the perpendicular dropped from a point of a circle on a diameter is a mean proportional between the segments into which it divides the diameter.

In the following pages we shall study the remaining three conics.
Let $L$ be a fixed line in a plane and $F$ be a fixed point not on the line $L$.

Suppose $|P M|$ denotes the distance of a point $P(x, y)$ from the line $L$. The set of all points $P$ in the plane such that

$$
\frac{|P F|}{|P M|}=e . \quad(\text { a positive constant })
$$

is called a conic section.
(i) If $e \equiv 1$, then the conic is a parabola.
(ii) If $0<e<1$, then the conic is an ellipse.
(iii) If $e>1$, then the conic is a hyperbola.

The fixed line $L$ is called a directrix and the fixed point $F$ is called a focus of the conic. The number e is called the eccentricity of the conic.

### 6.4 PARABOLA

We have already stated that a conic section is a parabola if $e \equiv 1$.
We shall first derive an equation of a parabola in the standard form and study its important properties.

If we take the focus of the parabola as $F(a, 0), a>0$ and its directrix as line $L$ whose equation is $x \equiv-a$, then its equation becomes very simple.

Let $P(x, y)$ be a point on the parabola. So, by definition

$$
\frac{|P F|}{|P M|}=4 . \quad \text { or } \quad|P F||P M|
$$

Now $|P M|=x+a$
and $|P F|=\sqrt{(x-a)^{2}+(y-0)^{2}}$
Substituting into (1), we get

$$
\begin{aligned}
& \sqrt{(x-a)^{2}+y^{2}}=x+a \\
& (x-a)^{2}+y^{2}=(x+a)^{2}
\end{aligned}
$$

or

$$
y^{2}=(x+a)^{2}-(x-a)^{2}=4 a x \quad \text { or } \quad y^{2}=4 a z
$$

which is standard equation of the parabola.

## Definitions

(i) The line through the focus and perpendicular to the directrix is called axis of the parabola. In case of (2), the axis is $y=0$.
(ii) The point where the axis meets the parabola is called vertex of the parabola. Clearly the equation (2) has vertex $A(0,0)$. The line through $A$ and perpendicular to the axis of the parabola has equation $x=0$. It meets the parabola at coincident points and so it is a tangent to the curve at $A$.
(iii) A line joining two distinct points on a parabola is called a chord of the parabola. A chord passing through the focus of a parabola is called a focal chord of the parabola. The focal chord perpendicular to the axis of the parabola (1) is called latusrectum of the parabola. It has an equation $x=a$ and it intersects the curve at the points where

$$
y^{2}=4 a^{2} \quad \text { or } \quad y= \pm 2 a
$$

Thus coordinates of the end points $L$ and $L^{\prime}$ of the latusrectum are

$$
L(a, 2 a) \text { and } L^{\prime}(a,-2 a)
$$

The length of the latusrectum is $\left|L L^{\prime}\right|=4 a$.
(iv) The point $\left(a t^{2}, 2 a t\right)$ lies on the parabola $y^{2}=4 a x$ for any real $t$.

$$
x=a t^{2}, y=2 a t
$$

are called parametric equations of the parabola $y^{2}=4 a x$.

### 6.4.1 General Form of an Equation of a Parabola

Let $F(h, k)$ be the focus and the line $l x+m y+n=0$ be the directrix of a parabola. An equation of the parabola can be derived by the definition of the parabola. Let $P(x, y)$ be a point on the parabola. Length of the perpendicular $P M$ from $P(x, y)$ to the directrix is given by;

$$
|P M|=\frac{|l x+m y+n|}{\sqrt{l^{2}+m^{2}}}
$$

By definition, $(x-h)^{2}+(y-k)^{2}=\frac{(l x+m y+n)^{2}}{l^{2}+m^{2}}$
is an equation of the required parabola.
A second degree equation of the form

$$
a x^{2}+b y^{2}+2 g x+2 f y+c=0
$$

with either $a=0$ or $b=0$ but not both zero, represents a parabola. The equation can be analyzed by completing the square.

### 6.4.2 Other Standard parabolas

There are other choices for the focus and directrix which also give standard equations of parabolas.
(i) If the focus lies on the $y$-axis with coordinates $F(0, a)$ and directrix of the parabola is $y=-a$, then equation of the parabola is

$$
x^{2}=4 a y
$$

The equation can be derived by difinition.
(ii) If the focus is $F(0,-a)$ and directrix is the line $y=a$, then equation of the parabola is

$$
x^{2}=-4 a y
$$

Opening of the parabola is upward in case of (3) and downward in case of (4). Both the curves are symmetric with respect to the $y$-axis.
The graphs of (3) and (4) are shown below.
(iii) If the focus of the parabola is $F(-a, 0)$, and its directrix is the line $x=a$, then equation of the parabola is

$$
y^{2}=-4 a x
$$

The curve is symmetric with respect to the $x$-axis and lies in the second and third quadrants only. Opening of the parabola is to the left as shown in the figure
## **6.4.3 Graph of the Parabola**

$$y^2 = 4ax$$

We note that corresponding to each positive value of *x* there are two equal and opposite values of *y*. Thus the curve is symmetric with respect to the *x*–axis. The curve passes through the origin and *x* = 0 is tangent to the curve at (0,0). If *x* is negative, then *y* is negative and so *y* is imaginary. Thus no portion of the curve lies on the left of the *y*–axis. As *x* increases, *y* also increases numerically so that the curve extends to infinity and lies in the first and fourth quadrants. Opening of the parabola is to the right of *y*–axis.

Sketching graphs of other standard parabolas is similar and is left as an exercise.

|  **S. No.** | **1** | **2** | **3** | **4**  |
| --- | --- | --- | --- | --- |
|  **Equation** | $$y^2 = 4ax$$ | $$y^2 = -4ax$$ | $$x^2 = 4ay$$ | $$x^2 = -4ay$$  |
|  **Focus** | (a, 0) | (-a, 0) | (0, a) | (0, -a)  |
|  **Directrix** | *x* = *-a* | *x* = *a* | *y* = *-a* | *y* = *a*  |
|  **Vertex** | (0,0) | (0,0) | (0,0) | (0,0)  |
|  **Axis** | *y* = 0 | *y* = 0 | *x* = 0 | *x* = 0  |
|  **Latusrectum** | *x* = *a* | *x* = *-a* | *y* = *a* | *y* = *-a*  |
|  **Graph** |  |  |  |   |

**Example 1:** Analyze the parabola *x* = -16*y* and draw its graph.

**Solution.** We compare the given equation with *x* = -4*ay*

**Version:** 1.1

Here: - 4*a* = 16 - *a* = 4.

The focus of the parabola lies on the *y*-axis and its opening is downward. Coordinates of the focus = (0, -4).

Equation of its axis is *x* = 0.

Length of the latusrectum is 16 and *y* = 0 is tangent to the parabola at its vertex. The shape of the curve is as shown in the figure.

**Example 2.** Find an equation of the parabola whose focus is *F* (-3, 4) and directrix is 3*x* - 4*y* + 5 = 0.

**Solution:** Let *P*(*x*, *y*) be a point on the parabola. Length of the perpendicular |*P*| from *P*(*x*, *y*) to the directrix 3*x* - 4*y* + 5 = 0 is

$$\left| \frac{3x - 4y + 5}{3^2 + (-4)^2} \right|$$

By definition, |*P*| = |*P*| or |*P*| = |*P*|

or

$$(x + 3)^2 + (y - 4)^2 = \frac{(3x - 4y + 5)^2}{25}$$

or

$$25(x^2 + 6x + 9 + y^2 - 8y + 16) = 9x^2 + 16y^2 + 25 - 24xy + 30x - 40y$$

or

$$16x^2 + 24xy + 9y^2 + 120x - 160y + 600 = 0$$

is an equation of the required parabola.

**Example 3.** Analyze the parabola

$$x^2 - 4x - 3y + 13 = 0$$

and sketch its graph.

**Solution.** The given equation may be written as

$$x^2 - 4x + 4 = 3y - 9$$

or

$$(x - 2)^2 = 3(y - 3)$$

Let: - 2 = *X*, - *y* - 3 = *Y*

The equation (2) becomes *X* = 3*Y*

**Version:** 1.1

which is a parabola whose focus lies on $X=0$ and whose directrix is $Y=\frac{-3}{4}$ Thus coordinates of the focus of (3) are

$$
\begin{aligned}
& X=0, Y=\frac{-3}{4} \\
& \text { i.e., } \quad x-2=0-\quad \text { and } \quad y \quad 3 \quad \frac{3}{4} \\
& \text { or } \quad x=2, y=\frac{15}{4}
\end{aligned}
$$

Thus coordinates of the focus of the parabola
(1) are $\left(2, \frac{15}{4}\right)$

Axis of (3) is $X=0$ or $x-2=0$ is the axis of (1).
Veitex of (3) has coordinates

$$
\begin{aligned}
& X=0, Y=0 \\
& \text { or } \quad x-2=0, y-3=0
\end{aligned}
$$

i.e., $x=2, y=3$ are coordinates of the vertex of (1).

Equation of the directrix of (3) is
$Y=\frac{-3}{4}$ i.e. $y-3=\frac{-3}{4}$ or $y=\frac{9}{4}$ is an equation of the directrix of (1).
Magnitude of the latusrectum of the parabola (3) and also of (1) is 3.
The graph of (1) can easily be sketched and is as shown in the above figure.

Theorem: The point of a parabola which is closest to the focus is the vertex of the parabola.
Proof: Let the parabola be

$$
x^{2}=4 a y, a>0
$$

with focus at $F(0, a)$ and $P(x, y)$ be any point on the parabola.

$$
\begin{aligned}
& |P F|=\sqrt{x^{2}+(y-a)^{2}} \\
& =\sqrt{4 a y+(y-a)^{2}} \\
& =y+a
\end{aligned}
$$

$$
\text { version: } 1.1
$$

Since $y$ can take up only non-negative values, $|P F|$ is minimum when $y=0$. Thus $P$ coincides with $A$ so that of all points on the parabola, its vertex $A$ is closest to the focus.

Example 4. A comet has a parabolic orbit with the sun at the focus. When the comet is 100 million km from the sun, the line joining the sun and the comet makes an angle of $60^{\circ}$ with the axis of the parabola. How close will the comet get to the sun?

Solution. Let the sun $S$ be the origin. If the vertex of the parabola has coordinates $(-a, 0)$ then directrix of the parabola is

$$
x=-2 a, \quad(a>0)
$$

if the comet is at $P(x, y)$, then
by definition $|P S|=|P M|$
i,e., $x^{2}+y^{2}=(x+2 a)^{2}$
or $y^{2}=4 a x+4 a^{2}$ is orbit of the comet
Now $|P S|=\sqrt{x^{2}+y^{2}}$

$$
=x+2 a=100,000,000
$$

The comet is closest to the sun when it is at $A$.
Now $\quad x=P S \cos 60^{\circ}$

$$
|x|=\frac{|P S|}{2}=\frac{x+2 a}{2}
$$

or $\quad \frac{x+2 a}{|x|}=\frac{2}{1} \quad$ or $\quad \frac{x+2 a}{2 a} \quad 2=,(|x| \quad|-2 a| \quad 2 a)$
or $\quad \frac{100,000,000}{2 a}=2$
or $\quad a=25,000,000$
Thus the comet is closest to the sun when it is $25,000,000 \mathrm{~km}$ from the sun.

## Reflecting Property of the parabola.

A frequently used property of a parabola is its reflecting property. If a light source is placed at the focus of a parabolic reflecting surface then a light ray travelling from $F$ to a point $P$ on the parabola will be reflected in the direction $P R$ parallel to the axis of the parabola.

The designs of searchlights, reflecting telescopes and microwave antenas are based on reflecting property of the parabola.

Another application of the parabola is in a Suspension bridge. The main cables are of parabolic shape. The total weight of the bridge is uniformly distributed along its length if the shape of the cables is parabolic. Cables in any other shape will not carry the weight evenly.

Example 6. A suspension bridge with weight uniformly distributed along the length has two towers of 100 m height above the road surface and are 400 m apart. The cables are parabolic in shape and are tangent to road surface at the centre of the bridge. Find the height of the cables at a point 100 m from the centre.

Solution. The parabola formed by the $P$ cables $(1,200,100)$ has $A(0,0)$ as vertex and focus on the $y$-axis. An equation of this parabola is $x^{2}=4 a y$.

The point $Q(200,100)$ lies on the parabola and so
$(200)^{2}=4 a \times 100$
or $\quad a=100$
Thus an equation of the parabola is

$$
x^{2}=400 y
$$

To find the height of the cables when $x=100$, we have from (1)

$$
(100)^{2}=400 y
$$

or $\quad y=25$
Thus required height $=25 \mathrm{~m}$

## EXERCISE 6.4

1. Find the focus, vertex and directrix of the parabola. Sketch its graph.
(i) $y^{2}=8 x$
(ii) $x^{2}=-16 y$
(iii) $x^{2}=5 y$
(iv) $y^{2}=-12 x$
(v) $x^{2}=4(y-1)$
(vi) $y^{2}=-8(x-3)$
(vii) $(x-1)^{2}=8(y+2)$
(viii) $y=6 x^{2}-1$
(ix) $x+8-y^{2}+2 y=0$
(x) $x^{2}-4 x-8 y+4=0$
version: 1.1
2. Write an equation of the parabola with given elements.
(i) Focus $(-3,1)$; directrix $x=3$
(ii) Focus $(2,5)$; directrix $y=1$
(iii) Focus $(-3,1)$; directrix $x-2 y-3=0$
(iv) Focus $(1,2)$; vertex $(3,2)$
(v) Focus $(-1,0)$; vertex $(-1,2)$
(vi) Directrix $x=-2$; Focus $(2,2)$
(vii) Directrix $y=3$; vertex $(2,2)$
(viii) Directrix $y=1$, length of latusrectum is 8 . Opens downward.
(ix) Axis $y=0$, through $(2,1)$ and $(11,-2)$
(x) Axis parallal to $y$-axis, the points $(0,3),(3,4)$ and $(4,11)$ lie on the graph.
3. Find an equation of the parabola having its focus at the origon and directrix, parallel to the (i) $x$-axis (ii) $y$-axis.
4. Show that an equation of the parabola with focus at ( $a \cos \alpha, a \sin \alpha$ ) and directrix $x \cos \alpha+y \sin \alpha+a=0$ is
$(x \sin \alpha-y \cos \alpha)^{2}=4 a(x \cos \alpha+y \sin \alpha)$
5. Show that the ordinate at any point $P$ of the parabola is a mean proportional between the length of the latus rectum and the abscissa of $P$.
6. A comet has a parabolic orbit with the earth at the focus. When the comet is 150,000 km from the earth, the line joining the comet and the earth makes an angle of $30^{\circ}$ with the axis of the parabola. How close will the comet come to the earth?
7. Find an equation of the parabola formed by the cables of a suspension bridge whose span is $a \mathrm{~m}$ and the vertical height of the supporting towers is $b \mathrm{~m}$.
8. A parabolic arch has a 100 m base and height 25 m . Find the height of the arch at the point 30 m from the centre of the base.
9. Show that tangent at any point $P$ of a parabola makes equal angles with the line $P F$ and the line through $P$ parallel to the axis of the parabola, $F$ being focus. (These angles are called respectively angle of incidence and angle of reflection).

### 6.5 ELLIPSE AND ITS ELEMENTS

We have already stated that a conic section is an ellipse if $e<1$.
Let $0<e<1$ and $F$ be a fixed point and $L$ be a fixed line not containing $F$. Let $P(x, y)$ be a point in the plane and $|P M|$ be the perpendicular distance of $P$ from $L$.
The set of all points $P$ such that

$$
\left|\frac{P F}{P M}\right|=e
$$

is called an ellipse.
The number e is eccentricity of the ellipse, $F$ a focus and $L$ a directrix.

### 6.5.1 Standard Form of an Ellipse

Let $F(-c, 0)$ be the focus and line $x=\frac{-c}{e^{2}}$ be the directix of an ellipse with eccentricity $e$, $(0<e<1)$. Let $P(x, y)$ be any point on the ellipse and suppose that $|P M|$ is the perpendicular distance of $P$ from the directrix. Then

$$
|P M|=x+\frac{c}{e^{2}}
$$

The condition $|P F|=e|P M|$ takes the analytic form

$$
(x+c)^{2}+y^{2}=e^{2}\left(x+\frac{c}{e^{2}}\right)^{2}
$$

$$
\text { or } \quad x^{2}+2 c x+c^{2}+y^{2}=e^{2} x^{2}+2 c x+\frac{c^{2}}{e^{2}} \quad \text { or } \quad x^{2}\left(4 e^{2}\right)+y^{2}=\frac{e^{2}}{e^{2}}\left(4 e^{2}\right)
$$

version: 1.1
or $x^{2}\left(1-e^{2}\right)+y^{2}=a^{2}\left(1-e^{2}\right)$. where $\frac{c}{e} a$
or $\quad \frac{x^{2}}{a^{2}}+\frac{y^{2}}{a^{2}\left(1-e^{2}\right)}=1$
If we write $b^{2}=a^{2}\left(1-e^{2}\right)$, then (1) takes the form

$$
\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1
$$

which is an equation of the ellipse in the standard form.
Moreover, eccentricity of the ellipse is $e=\frac{c}{a}$.
We have $b^{2}=a^{2}\left(1-e^{2}\right)$
(i) From the relation $b^{2}=a^{2}\left(1-e^{2}\right)$, we note that $b<a$
(ii) Since we set $\frac{c}{e}=a$, the focus $F$ has coordinates $(-a e, 0)$ and equation of the directrix is $x=\frac{-a}{e}$.
(iii) If we take the point $(a e, 0)$ as focus and the line $x=\frac{a}{e}$ as directrix, it can be seen easily that we again obtain equation (2). Thus the ellipse (2) has two foci $(-a e, 0)$ and $(a e, 0)$ and two directrices $x=\pm \frac{a}{e}$.
(iv) The point (acos $\theta$, bsin $\theta$ ) lies on (2) for all real $\theta . x=\operatorname{acos} \theta, y=b \sin \theta$ are called parametric equations of the ellipse (2).
(v) If in (2), $b=a$ then it becomes

$$
x^{2}+y^{2}=a^{2}
$$

which is a circle. In this case $b^{2}=a^{2}\left(1-e^{2}\right)=a^{2}$ and so $e=0$. Thus circle is a special case of an ellipse with eccenctricty 0 and foci tending to the centre.
Definitions: Let $F^{\prime}$ and $F$ be two foci of the ellipse

$$
\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1
$$

- (i) The midpoint *C* of *FF'* is called the **centre** of the ellipse. In case of (1) coordinates of *C* are (0,0).
- (ii) The intersection of (1) with the line joining the foci are obtained by setting *y* = 0 into (1). These are the points *A*<sup>0</sup>(−*a*, 0) and *A*(*a*, 0). The points *A* and *A'* are called **vertices** of the ellipse.
- (iii) The line segment *AA'* = 2*a* is called the **major axis** of the ellipse. The line through the centre of (1) and perpendicular to the major axis has its equation as *x* = 0. It meets (1) at points *B'* (0, *b*) and *B'* (0,−*b*). The line segment *BB'* = 2*b* is called the **minor axis** of the ellipse and *B'*, *B'* are some-times called the **covertices** of the ellipse. Since *b*<sup>2</sup> = *a*<sup>2</sup>(1 − *e*<sup>2</sup>) and *e* < 1, the length of the major axis is greater than the length of the minor axis. (See figure)
- (iv) Foci of an ellipse always lie on the major axis.
- (v) Each of the focal chords *LFL'* and *NF'N'* perpendicular to the major axis of an ellipse is called a **latusrectum** of the ellipse. Thus there are two **laterarecta** of an ellipse. It is an easy exercise to find that length of each latusrectum is *2b*<sup>2</sup> *a*. (See problem 5).
- (vi) If the foci lie on the *y*–axis with coordinates (0,−*ae*) and (0,*ae*), then equation of the ellipse is

$$
\frac{x^2}{b^2} + \frac{y^2}{a^2} = 1 \quad \text{or} \quad a > b.
$$

The reader is urged to derive this equation.

#### 6.5.2 Graph of an Ellipse

Let an equation of the ellipse be

$$
\frac{x^2}{a^2} + \frac{y^2}{b^2} > 1
$$

Since only even powers of both *x* and *y* occur in (1), the curve is symmetric with respect to both the axes.

From (1), we note that

$$
\frac{x^2}{a^2} \leq 1 \quad \text{and} \quad \frac{y^2}{b^2} \leq 1
$$

i.e.,

$$
\frac{x^2}{a^2} \leq a^2 \quad \text{and} \quad y^2 \leq b^2
$$

or

$$
-a \leq x \leq a \quad \text{and} \quad -b \leq y \leq b
$$

Thus all points of the ellipse lie on or within the rectangle (2). The curve meets the *x*-axis at *A*(−*a*, 0) and *A'*(*a*, 0) and it meets the *y*-axis at *B*(0,−*b*), *B'* (0, *b*). The graph of the ellipse can easily be drawn as shown in the following figure.

The graph of the ellipse

$$
\frac{x^2}{b^2} + \frac{y^2}{a^2} = 1, \quad a > b
$$

can be sketched as in the case of (1). Its shape is shown in above figure (ii).

# **6. Conic Sections**

|  **Summary of standard Ellipses** |  |   |
| --- | --- | --- |
|  **Equation** | $$ \frac{x^2}{a^2} + \frac{y^2}{b^2} = 1, a > b $$
$$ c^2 = a^2 - b^2 $$ | $$ \frac{x^2}{b^2} + \frac{y^2}{a^2} = 1, a > b $$
$$ c^2 = a^2 - b^2 $$  |
|  **Foci** | (∆c, 0) | (0, ∆c)  |
|  **Directrices** | $$ x = \pm \frac{c}{e^2} $$ | $$ y = \pm \frac{c}{e^2} $$  |
|  **Major axis** | $$ y = 0 $$ | $$ x = 0 $$  |
|  **Vertices** | (∆a, 0) | (0, ∆a)  |
|  **Convertices** | (0, ∆b) | (∆b, 0)  |
|  **Centre** | (0, 0) | (0, 0)  |
|  **Eccentricity** | $$ e = \frac{c}{a} < 1 $$ | $$ e = \frac{c}{a} < 1 $$  |
|  **Graph** |  |   |
|  |   |   |
|  |   |   |
|  **Note:** In each ellipse |  |   |
|  Length of major axis = 2a, Length of minor axis = 2b |  |   |
|  Length of Latusrectum = $$\frac{2b^2}{a}$$, Foci lie on the major axis |  |   |

**Example 1.** Find an equation of the ellipse having centre at (0,0), focus at (0,−3) and one vertex at (0,4). Sketch its graph.

**Solution.** The second vertex has coordinates (0, −4). Length of the semi-major axis is

$$ a = 4 $$

Also

$$ c = 3 $$

From $$ b^2 = a^2 - c^2 $$, we have

$$ b^2 = 16 - 9 = 7 $$

$$ b = \sqrt{7} $$ which is length of the semi-minor axis. Since the foci lie on the y-axis; equation of the ellipse is

$$ \frac{y^2}{16} + \frac{x^2}{7} = 1 $$

The graph is as shown above.

**Example 2.** Analyze the equation

$$ 4x^2 + 9y^2 = 36 $$

and sketch its graph.

**Solution:** The given equation may be written as

$$ \frac{x^2}{a} + \frac{y^2}{a} = 1 $$

which is standard form of an ellipse. Semi-major axis $$ a = 3 $$ Semi-minor axis $$ b = 2 $$ From $$ b^2 = a^2 - c^2 $$, we have

$$ c^2 = b^2 - a^2 = 9 - 4 = 5 $$

or

$$ c = \pm \sqrt{5} $$

For

$$ F(-\sqrt{5}, 0), \quad F'(\sqrt{5}, 0); \quad \text{Vertices:} \quad A(-3, 0), A'(3, 0) $$

**40**

**41**

C
Example 4. An arch in the form of half an ellipse is 40 m wide and 15 m high at the centre. Find the height of the arch at a distance of 10 m from its centre.

Solution: Let the $x$-axis be along the base of the arch and the $y$-axis pass through its centre. An equation of the ellipse representing the arch is

$$
\frac{x^{2}}{20^{2}}+\frac{y^{2}}{15^{2}}=1
$$

Let the height of an arch at a distance of 10 m from the centre be $y$. Then the points $(10, y)$ lies on (1)

For $x=10$, we have

$$
\begin{aligned}
& \frac{y^{2}}{15^{2}}=1-\frac{1}{4}=\left(\frac{\sqrt{3}}{2}\right)^{2} \\
& \text { so that } y=\frac{15 \sqrt{3}}{2} \\
& \text { Required height }=\frac{15 \sqrt{3}}{2} m
\end{aligned}
$$

## EXERCISE 6.5

1. Find an equation of the ellipse with given data and sketch its graph:
(i) Foci $( \pm 3,0)$ and minor axis of length 10
(ii) Foci $(0,-1)$ and $(0,-5)$ and major axis of length 6 .
(iii) Foci $(-3 \sqrt{3}, 0)$ and vertices $( \pm 6,0)$
(iv) Vertices $(-1,1),(5,1)$; foci $(4,1)$ and $(0,1)$
(v) Foci $( \pm \sqrt{5}, 0)$ and passing through the point $\left(\frac{3}{2}, \sqrt{3}\right)$
(vi) Vertices $(0, \pm 5)$, eccentricity $\frac{3}{5}$.
(vii) Centre $(0,0)$, focus $(0,-3)$, vertex $(0,4)$
(viii) Centre $(2,2)$, major axis parallel to $y$-axis and of length 8 units, minor axis parallel to $x$-axis and of length 6 units.
(ix) Centre $(0,0)$, symmetric with respect to both the axes and passing through the points $(2,3)$ and $(6,1)$.
(x) Centre $(0,0)$, major axis horizontal, the points $(3,1),(4,0)$ lie on the graph.
2. Find the centre, foci, eccentricity, vertices and directrices of the ellipse, whose equation is given:
(i) $x^{2}+4 y^{2}=16$
(ii) $9 x^{2}+y^{2}=18$
(iii) $25 x^{2}+9 y^{2}=225$
(iv) $\frac{(2 x-1)^{2}}{4}+\frac{(y+2)^{2}}{16}=1$
(v) $x^{2}+16 x+4 y^{2}-16 y+76=0$
(vi) $25 x^{2}+4 y^{2}-250 x-16 y+541=0$
3. Let $a$ be a positive number and $0<c<a$. Let $F(-c, 0)$ and $F^{\prime}(c, 0)$ be two given points. Prove that the locus of points $P(x, y)$ such that

$$
|P F|+\left|P F^{\prime}\right|=2 a, \text { is an ellipse. }
$$

4. Use problem 3 to find equation of the ellipse as locus of points $P(x, y)$ such that the sum of the distances from $P$ to the points $(0,0)$ and $(1,1)$ is 2 .
5. Prove that the lactusrectum of the ellipse.

$$
\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1 \text { is } \frac{2 b^{2}}{a}
$$

6. The major axis of an ellipse in standard form lies along the $x$-axis and has length $4 \sqrt{2}$. The distance between the foci equals the length of the minor axis. Write an equation of the ellipse.
7. An astroid has elliptic orbit with the sun at one focus. Its distance from the sun ranges from 17 million miles to 183 million miles. Write an equation of the orbit of the astroid.
8. An arch in the shape of a semi-ellipse is 90 m wide at the base and 30 m high at the centre. At what distance from the centre is the arch $20 \sqrt{2} \mathrm{~m}$ high?
9. The moon orbits the earth in an elliptic path with earth at one focus. The major and minor axes of the orbit are $768,806 \mathrm{~km}$ and $767,746 \mathrm{~km}$ respectively. Find the greatest and least distances (in Astronomy called the apogee and perigee respectively) of the moon from the earth.

### 6.6 HYPERBOLA AND ITS ELEMENTS

We have already stated that a conic section is a hyperbola if $e>1$. Let $e>1$ and $F$ be a fixed point and $L$ be a line not containing $F$. Also let $P(x, y)$ be a point in the plane and $|P M|$ be the perpendicular distance of $P$ from $L$.

The set of all points $P(x, y)$ such that

$$
\frac{|P F|}{|P M|}=e>1
$$

is called a hyperbola.
$F$ and $L$ are respectively focus and directrix of the hyperbola $e$ is the eccentricity.

### 6.6.1 Standard Equation of Hyperbola

Let $F(c, 0)$ be the focus with $c>0$ and $x=\frac{c}{c^{2}}$ be the directrix of the hyperbola. Also let $P(x, y)$ be a point on the hyperbola, then by definition

$$
\frac{|P F|}{|P M|}=e
$$

i.e. $(x-c)^{3}+y^{2}=e^{2}\left(x-\frac{c}{e^{2}}\right)^{2} \quad$ or $\quad x \frac{c}{e^{2}} \quad 2 c \neq \quad c \neq \quad y \frac{c}{e^{2}} \quad e^{2} x \frac{c}{e^{2}} \quad 2 c \neq \quad \frac{e^{2}}{a^{2}}$
or $\quad x^{2}\left(e^{2}-1\right)-y^{2}=c^{2}\left(1-\frac{1}{e^{2}}\right)=\frac{c^{2}}{e^{2}}\left(e^{2}-1\right)$
Let us set $a=\frac{c}{e}$, so that (2) becomes
$x^{2}\left(e^{2}-1\right)-y^{2}-a^{2}\left(e^{2}-1\right)=0-\quad$ or $\quad \frac{x^{2}}{a^{2}} \quad \frac{y^{2}}{a^{2}\left(e^{2}-1\right)} \quad 1$
or $\quad \frac{x^{2}}{a^{2}}-\frac{y^{2}}{b^{2}}=1$
where $\quad b^{2}=a^{2}\left(e^{2}-1\right) \approx c^{2}-a^{2} \quad \because c=a e$
(3) is standard equation of the hyperbola.

It is clear that the curve is symmetric with respect to both the axes.
If we take the point $(-c, 0)$ as focus
and the line $x=\frac{-c}{e^{2}}$ as directrix, then it is easy to see that the set of all points $P(x, y)$ such that

$$
|P F|=e|P M|
$$

is hyperbola with (3) as its equation.
Thus a hyperbola has two foci and two directrices.

If the foci lie on the $y$-axis, then roles of $x$ and $y$ are interchanged in (3) and the equation of the hyperbola becomes

$$
\frac{y^{2}}{a^{2}}-\frac{x^{2}}{b^{2}}=1
$$

Definition: The hyperbola

$$
\frac{x^{2}}{a^{2}}-\frac{y^{2}}{b^{2}}=1
$$

meets the $x$-axis at points with $y=0$ and $x= \pm a$. The points $A(-a, 0$ and $A \nmid a, 0)$ are called vertices of the hyperbola. The line segament $A A^{\prime}=2 a$ is called the transverse (or focal) axis of the hyperbola (3). The equation (3) does not meet the $y$-axis in real points. However the line segment joining the points $B(0,-b)$ and $B^{\prime}(0, b)$ is called the conjugate axis of the hyperbola. The midpoint $(0,0)$ of $A A^{\prime}$ is called the centre of the hyperbola.

In case of hyperbola (3), we have

$$
b^{2}=a^{2}\left(e^{2}-1\right)=c^{2}-a^{2} \text {. The eccentricity } e=\frac{c}{a}>1
$$

so that, unlike the ellipse, we may have $b>a$ or $b<a$ or $b=a$
(ii) The point ( $a$ sec $\theta, b$ tan $\theta$ ) lies on the hyperbola $\frac{x^{2}}{a^{2}}-\frac{y^{2}}{b^{2}}=1$ for all real values of $\theta$. The equations $x=a \sec \theta, y=b \tan \theta$ are called parametric equations of the hyperbola.
(iii) Since $y= \pm \frac{b}{a} \sqrt{x^{2}-a^{2}}$, when $|x|$, so that $x^{2} \quad a^{2} \quad \Rightarrow$, we have

$$
y:=\frac{b}{a} \cdot x \quad \text { i.e. } \quad \frac{x^{2}}{a^{2}}-\frac{y^{2}}{b^{2}}=0
$$

The lines (2) do not meet the curve but distance of any point on the curve from any of the two lines approaches zero. Such lines are called asymptotes of a curve. Joint equation of the asymptotes of (3) is obtained by writing 0 instead of 1 on the right hand side of the standard form (3). Asymptotes are very helpful in graphing a hyperbola.

The ellipse and hyperbola are called central conics because each has a centre of symmetry.

### 6.6.2 Graph of the hyperbola

$$
\frac{x^{2}}{a^{2}}-\frac{y^{2}}{b^{2}}=1
$$

The curve is symmetric with respect to both the axes. We rewrite (1) as

$$
\begin{aligned}
& \frac{y^{2}}{b^{2}}=\frac{x^{2}}{a^{2}} \quad 1 \quad \text { or } \quad-y^{2} \quad \frac{b^{2}}{a^{2}}\left(x^{2} \quad a^{2}\right) \cdot \\
& \text { or } \pm y=\frac{b}{a} \sqrt{x^{2} \quad a^{2}}
\end{aligned}
$$

If $|x|<a$, then $y$ is imaginary so that no portion of the curve lies between $-\alpha<x<\alpha$. For $x \geq a, y=\frac{b}{a} \sqrt{x^{2}-a^{2}} \leq \frac{b}{a} x$ so that points on the curve lie below the corresponding points on the line $y=\frac{b}{a} x$ in first quadrant.

$$
y=\frac{b}{a} \sqrt{x^{2}-a^{2}} \quad \frac{-b}{a} x \text { if } \geq x \quad a
$$

and in this case the points on the curve lie above the line $y=\frac{-b}{a} x$ in fourth quadrant. If $x \leq \alpha$, then by similar arguments, $y=\frac{b}{a} \sqrt{x^{2}-a^{2}}$ lies below the corresponding point on $y=\frac{-b}{a} x$ in second quadrant. If $y=\frac{-b}{a} \sqrt{x^{2}-a^{2}}$, then points on the curve lie above the correspondent point on $y=\frac{b}{a} x$ in third quadrant. Thus there are two branches of the curve. Moreover, from (2) we see that as $|x| \rightarrow \infty,|y| \rightarrow \infty$ so that the two branches extend to infinity

## Summary of Standard Hyperbolas

|  Equation | $\frac{x^{2}}{a^{2}}-\frac{y^{2}}{b^{2}}=1$ | $\frac{y^{2}}{a^{2}}-\frac{z^{2}}{b^{2}}=1$  |
| --- | --- | --- |
|  Foci | $(\pm c, 0)$ | $(0, \pm c)$  |
|  Directrices | $x= \pm \frac{c}{e^{2}}$ | $y= \pm \frac{c}{e^{2}}$  |
|  Transverse axis | $y=0$ | $x=0$  |
|  Vertices | $( \pm \alpha, 0)$ | $(0, \pm \alpha)$  |
|  Eccentricity | $e=\frac{c}{a}>1$ | $e=\frac{c}{a}>1$  |

version: 1.1

|  Centre | $(0,0)$ | $(0,0)$  |
| --- | --- | --- |
|  Graph |  |   |
|  |   |   |

Example 1. Find an equation of the hyperbola whose foci are ( $\pm 4,0$ ) and vertices ( $\pm 2,0$ ). Sketch its graph.

Solution: The centre of the hyperbola is the origin and the transverse axis is along the $x$-axis. Here $c=4$ and $\alpha=2$ so that $b^{2}=c^{2}-\alpha^{2}=16-4=12$. Therefore, the equation is $\frac{x^{2}}{4}-\frac{y^{2}}{12}=1$. The graph of the curve is as shown. Example 2. Discuss and sketch the graph of the equation $25 x^{2}-16 y^{2}=400$ Solution: The given equation is

$$
\frac{x^{2}}{16}-\frac{y^{2}}{25}=1-\text { or }=\frac{x^{2}}{4^{2}} \cdot \frac{y^{2}}{5^{2}}=1
$$

which is an equation of the hyperbola with transverse axis along the $x$-axis.

$$
\begin{aligned}
& \text { Here } \quad \alpha=4, b=5 \\
& \text { From } \quad b^{2}=c^{2}-a^{2}, \quad \text { we have } \\
& \quad c^{2}=34 \text { or } c= \pm \sqrt{34} \\
& \text { Foci of the hyperbola are: }( \pm \sqrt{34}, 0) \\
& \text { Vertices: }( \pm 4,0) \\
& \text { Ends of the conjugate axes are the points }(0, \pm 5)
\end{aligned}
$$

Eccentricity: $e=\frac{c}{a}=\frac{\sqrt{34}}{4}$
The curve is below the lines $\varepsilon=\frac{b}{a} x \quad x \quad \frac{5}{4} x$
which are its asymptotes. The sketch of the curve is as shown.
Example 3. Find the eccentricity, the coordinates of the vertices and foci of the asymptotes of the hyperbola

$$
\frac{\varepsilon^{2}}{16} \cdot \frac{x^{2}}{49}=1
$$

Also sketch its graph.
Solution. The transverse axis of (1) lies along the $y$-axis. Coordinates of the vertices are $(0, \pm 4)$.

$$
\begin{aligned}
& \text { Here } a=4, b=7 \text { so that from } \varepsilon^{2}=a^{2}+b^{2} \text {, we get } \\
& \varepsilon^{2}=16+49 \text { or } c=\sqrt{65} \\
& \text { Foci are: }(0, \pm \sqrt{65}) \\
& \text { Ends of the conjugate axis are }( \pm 7,0) \\
& \text { Eccentricity }=\frac{c}{a}=\frac{\sqrt{65}}{4} \\
& x= \pm 7, y= \pm 4
\end{aligned}
$$

The graph of the curve is as shown.
Example 4. Discuss and sketch the graph of the equation

$$
4 x^{2}-8 x-y^{2}-2 y-1=0
$$

Solution: Completing the squares in $x$ and $y$ in the given equation, we have

$$
\begin{aligned}
& 4\left(x^{2}-2 x+1\right)-\left(y^{2}+2 y+1\right)=4 \\
\text { or } & 4(x-1)^{2}-(y+1)^{2}=4 \\
\text { or } & \frac{(x-1)^{2}}{1^{2}}-\frac{(y+1)^{2}}{2^{2}}=1
\end{aligned}
$$

$$
\text { version: } 1.1
$$

We write $x-1=X, y+1=Y$ in (2), to have

$$
\frac{X^{2}}{1^{2}}-\frac{Y^{2}}{2^{2}}=1
$$

so that it is a hyperbola with centre at $X=0, Y=0$ i.e., the centre of (1) is $(1,-1)$. The transverse axis of (3) is $Y=0$ i.e., $y+1=0$ is the transverse axis of (1). Vertices of (3) are: $X= \pm 1, y=0$
i.e. $x-1= \pm 1, y+1=0 \quad$ or $\quad(0,-1)$ and $(2,-1)$

Here $a=1$ and $b=2$ so that, we have $c=\sqrt{a^{2}+b^{2}}=\sqrt{5}$
Eccentricity $e=\frac{c}{a}=\sqrt{5}$
Foci of (3) are: $\pm X=\sqrt{5}, Y \quad 0$
i.e., $\quad x=1 \sqrt{5} \quad$ and $\quad \varepsilon \quad 1$
i.e., $\quad(1+\sqrt{5},-1)$ and $(1-\sqrt{5},-1)$ are foci of (1).
Equations of the directrices of (3) are: $X= \pm \frac{c}{e^{2}}= \pm \frac{\sqrt{5}}{5}= \pm \frac{1}{\sqrt{5}}$

$$
\text { or } \quad x-1= \pm \frac{1}{\sqrt{5}} \quad \text { or } \quad x=1+\frac{1}{\sqrt{5}} \quad \text { and } \quad x=1-\frac{1}{\sqrt{5}}
$$

The sketch of the curve is as shown.

## EXERCISE 6.6

1. Find an equation of the hyperbola with the given data. Sketch the graph of each.
(i) Centre $(0,0)$, focus $(6,0)$, vertex $(4,0)$
(ii) Foci $( \pm 5,0)$, vertex $(3,0)$
(iii) Foci $(2 \pm 5 \sqrt{2},-7)$, length of the transverse axis 10 .
(iv) Foci $(0, \pm 6), e=2$.
(v) Foci $(0, \pm 9)$, directrices $y= \pm 4$

(vi) Centre $(2,2)$, horizontal transverse axis of length 6 and eccentricity $e=2$
(vii) Vertices $(2, \pm 3),(0,5)$ lies on the curve.
(viii) Foci $(5,-2),(5,4)$ and one vertex $(5,3)$
2. Find the centre, foci, eccentricity, vertices and equations of directrices of each of the following:
(i) $x^{2}-y^{2}=9$
(ii) $\frac{x^{2}}{4}-\frac{y^{2}}{9}=1$
(iii) $\frac{y^{2}}{16}-\frac{x^{2}}{9}=1$
(iv) $\frac{y^{2}}{4}-x^{2}=1$
(v) $\frac{(x-1)^{2}}{2}-\frac{(y-1)^{2}}{9}=1$
(vi) $\frac{(y+2)^{2}}{9}-\frac{(x-2)^{2}}{16}=1$
(vii) $9 x^{2}-12 x-y^{2}-2 y+2=0$
(viii) $4 y^{2}+12 y-x^{2}+4 x+1=0$
(ix) $x^{2}-y^{2}+8 x-2 y-10=0$
(x) $9 x^{2}-y^{2}-36 x-6 y+18=0$
3. Let $0<a<c$ and $F^{\prime}(-c, 0), F(c, 0)$ be two fixed points. Show that the set of points $P(x, y)$ such that
$|P F|-\left|P K^{\prime}\right|=2 a$, is the hyperbola $\frac{x^{2}}{a^{2}}-\frac{y^{2}}{c^{2}-a^{2}}=1$
( $F, F^{\prime}$ are foci of the hyperbola)
4. Using Problem 3, find an equation of the hyperbola with foci $(-5,-5)$ and $(5,5)$, vertices $(-3 \sqrt{2},-3 \sqrt{2})$ and $(3 \sqrt{2}, 3 \sqrt{2})$.
5. For any point on a hyperbola the difference of its distances from the points $(2,2)$ and $(10,2)$ is 6 . Find an equation of the hyperbola.
6. Two listening posts hear the sound of an enemy gun. The difference in time is one second. If the listening posts are 1400 feet apart, write an equation of the hyperbola passing through the position of the enemy gum. (Sound travels at $1080 \mathrm{ft} / \mathrm{sec}$ ).

### 6.7 TANGENTS AND NORMALS

We have already seen in the geometrical interpretation of the derivative of a curve $y=f(x)$ or $f(x, y)=0$ that $\frac{d y}{d x}$ represents the slope of the tangent line to the curve at the point $(x, y)$. In order to find an equation of the tangent to a given
conic at some point on the conic, we shall first find the slope of the tangent at the given point by calculating $\frac{d y}{d x}$ from the equation of the conic at that point and then using the point - slope form of a line, it will be quite simple to write an equation of the tangent. Since the normal to a curve at a point on the curve is perpendicular to the tangent through the point of tangency, its equation can be easily written.

Example 1. Find equations of the tangent and normal to
(i) $y^{2}=4 a x$
(ii) $\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1$
(iii) $\frac{x^{2}}{a^{2}}-\frac{y^{2}}{b^{2}}=1$
at the point $\left(x_{1}, y_{1}\right)$.
Solution: (i). Differentiating (1) w.r.t. $\quad x$, we get

$$
\begin{aligned}
& 2 y \frac{d y}{d x}=4 a \quad \text { or } \quad \frac{d y}{d x} \quad 2 a \\
& \left.\frac{d y}{d x}\right|_{\left(x_{1}, y_{1}\right)}=\frac{2 a}{y_{1}} \text { Slope of the tangent at }\left(x_{1}, y_{1}\right)
\end{aligned}
$$

Equation of the tangent to (1) at $\left(x_{1}, y_{1}\right)$ is

$$
y-y_{1}=\frac{2 a}{y_{1}}\left(x-x_{1}\right) \text { or } y y_{1}-y_{1}^{2}=2 a x-2 a x_{1} \text { or } y y_{1}-2 a x=y_{1}^{2}-2 a x_{1}
$$

Adding $-2 a x$, to both sides of the above equation, we obtain

$$
y y_{1}=2 a\left(x+x_{1}\right)=y_{1}^{2}-4 a x_{1}
$$

Since $\left(x_{1}, y_{1}\right)$ lies on $y^{2}=4 a x_{1}$ so $y_{1}^{2}-4 a x_{1}=0$
Thus equation of the required tangent is

$$
y y_{1}=2 a\left(x+x_{1}\right)
$$

Slope of the normal $=\frac{-y_{1}}{2 a} \quad$ (negative reciprocal of slope of the tangent)

Equation of the normal is

$$
y-y_{1}=\frac{-y_{1}}{2 a}\left(x-x_{1}\right)
$$

(ii) $\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1$

Differentiating the above equation, w.r.t. $x$, we have

$$
\frac{2 x}{a^{2}}+\frac{2 y}{b^{2}} \frac{d y}{d x}=0-\text { or } \frac{d y}{d x}=\frac{b^{2} x}{a^{2} y}
$$

or $\left.\frac{d y}{d x}\right|_{\left(x_{1}, y_{1}\right)}=\frac{-b^{2} x_{1}}{a^{2} y_{1}}$
Equation of the tangent to (2), at $\left(x_{1}, y_{1}\right)$ is

$$
y-y_{1}=\frac{-b^{2} x_{1}}{a^{2} y_{1}}\left(x-x_{1}\right)
$$

or $\quad \frac{y y_{1}}{b^{2}}, \frac{y_{1}^{2}}{b^{2}}=\frac{-x x_{1}}{a^{2}}+\frac{x_{1}^{2}}{a^{2}} \quad$ or $\quad \frac{x x_{1}}{a^{2}}+\frac{y y_{1}}{b^{2}}=\frac{x^{2}}{a^{2}}+\frac{y_{1}^{2}}{a^{2}}$
Since $\left(x_{1}, y_{1}\right)$ lie on (2) so, $\frac{x_{1}^{2}}{a^{2}}+\frac{y_{1}^{2}}{b^{2}}=1$
Hence an equation of the tangent to (2) at $\left(x_{1}, y_{1}\right)$ is $\frac{x x_{1}}{a^{2}}+\frac{y y_{1}}{b^{2}}=1$
Slope of the normal at $\left(x_{1}, y_{1}\right)$ is $\frac{a^{2} y_{1}}{b^{2} x_{1}}$.
Equation of the normal at $\left(x_{1}, y_{1}\right)$ is

$$
y-y_{1}=\frac{a^{2} y_{1}}{b^{2} x_{1}}\left(x-x_{1}\right)
$$

or $\quad b^{2} x_{1} y-b^{2} x_{1} y_{1}=a^{2} y_{1} x-a^{2} x_{1} y_{1} \quad$ or $\quad a^{2} y_{1} x-b^{2} x_{1} y=x_{1} y_{1}\left(a^{2}-b^{2}\right)$
Dividing both sides of the above equation by $x_{1} y_{1}$, we get
$\frac{a^{2} x}{x_{1}} \quad \frac{b^{2} y}{y_{1}}=a^{2}-b^{2}$, as an equation of the normal.
(iii) Proceeding as in (ii), it is easy to see that equations of the tangent and normal to (3) at $\left(x_{1}, y_{1}\right)$ are

$$
\frac{x x_{1}}{a^{2}}+\frac{y y_{1}}{b^{2}}=1 \quad \text { and } \quad \frac{a^{2} x}{x_{1}}+\frac{b^{2} y}{y_{1}}=a^{2}+b^{2}, \text { respectively. }
$$

## Remarks

An equation of the tangent at the point $\left(x_{1}, y_{1}\right)$ of any conic can be written by making replacements in the equation of the conic as under:

$$
\begin{array}{lll}
\text { Replace } & x^{2} & \text { by } & x x_{1} \\
& y^{2} & \text { by } & y y_{1} \\
& x & \text { by } & \frac{1}{2}\left(x+x_{1}\right) \\
& y & \text { by } & \frac{1}{2}\left(y+y_{1}\right)
\end{array}
$$

Example 1. Write equations of the tangent and normal to the parabola $x^{2}=16 y$ at the point whose abscissa is 8 .

Solution: Since $x=8$ lies on the parabola, substituting this value of $x$ into the given equation, we find

$$
64=16 y \quad \text { or } \quad y=4
$$

Thus we have to find equations of tangent and normal at $(8,4)$.
Slope of the tangent to the parabola at $(8,4)$ is 1 . An equation of the tangent the parabola at $(8,4)$ is

$$
y-4=x-8
$$

or $\quad x-y-4=0$
Slope of the normal at $(8,4)$ is -1 . Therefore, equation of the normal at the given point is

$$
y-4=-(x-8)
$$

or $\quad x+y-12=0$
Example 2. Write equations of the tangent and normal to the conic $\frac{x^{2}}{8}+\frac{y^{2}}{9}=1$ at the point $\left(\frac{8}{3}, 1\right)$.

Solution: The given equation is

$$
9 x^{2}+8 y^{2}-72=0
$$

Differentiating (1) w.r.t. $x$, we have
This is slope of the tangent to (1) at $\left(\frac{8}{3}, 1\right)$.
Equation of the tangent at this point is
$y-1=-3 \cdot\left(x-\frac{8}{3}\right)=-3 x+8$ or $3 x+y-9=0$.
The normal at $\left(\frac{8}{3}, 1\right)$ has the slope $\frac{1}{3}$.
Equation of the normal is
$y-1=\frac{1}{3}\left(x-\frac{8}{3}\right)$ or $3 y-3=x-\frac{8}{3}$ or $3 x-9 y+1=0$

Theorem: To show that a straight line cuts a conic, in general, in two points and to find the condition that the line be a tangent to the conic.

Let a line $y=m x+c$ cut the conics
(i) $y=4 a x$
(ii) $\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1$
(iii) $\frac{x^{2}}{a^{2}}-\frac{y^{2}}{b^{2}}=1$

We shall discuss each case separately.
(i) The points of intersection of

$$
y=m x+c
$$

and $\quad y^{2}=4 a x$
are obtained by solving (1) and (2) simultaneously for $x$ and $y$. Inserting the value of $y$ from (1) into (2), we get

$$
(m x+c)^{2}=4 a x
$$

or $\quad m^{2} x^{2}+(2 m c-4 a) x+c^{2}=0$
which being a quadratic in $x$ gives two values of $x$. These values are the $x$ coordinates of the common points of (1) and (2). Setting these values in (1), we obtain the corresponding
ordinates of the points of intersection. Thus the line (1) cuts the parabola (2) in two points. In order that (1) is a tangent to (2), the points of intersection of a line and the parabola must be conicident. In this case, the roots of (3) should be real and equal.
This means that the discriminant of (3) is zero. Thus

$$
4(m c-2 a)^{2}-4 m^{2} c^{2}=0 \quad \text { i.e., } \quad-4 m c a+4 a^{2}=0
$$

or $\quad c=\frac{a}{m}$, is. the required condition for (1) to be a tangent to (2). Hence

$$
y=m x+\frac{a}{m} \text {, is a tangent to } y^{2}=4 a x \text { for all nonzero values of } m \text {. }
$$

(ii) To determine the points of intersection of

$$
y=m x+c
$$

and

$$
\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1
$$

we solve (1) and (2) simultaneously. Putting the value of $y$ from (1) into (2), we have

$$
\frac{x^{2}}{a^{2}}+\frac{(m x+c)^{2}}{b^{2}}=1
$$

or

$$
\left(a^{2} m^{2}+b^{2}\right) x^{2}+2 m c a^{2} x+a^{2} c^{2}-a^{2} b^{2}=0
$$

which is a quardratic in $x$ and it gives the abscissas of the two points where (1) and (2) intersect. The corresponding values of $y$ are obtained by setting the values of $x$ obtained from (3) into (1). Thus (1) and (2) intersect in two points. Now (1) is a tangent to (2) if the point of intersection is a single point.
This requires (3) to have equal roots. Hence (1) is a tangent to (2) if

$$
\left(2 m c a^{2}\right)^{2}-4\left(a^{2} m^{2}+b^{2}\right)\left(a^{2} c^{2}-a^{2} b^{2}\right)=0
$$

i.e., $\quad m^{2} c^{2} a^{2}-\left(a^{2} m^{2}+b^{2}\right)\left(c^{2}-b^{2}\right)=0$
or $\quad m^{2} c^{2} a^{2}-a^{2} m^{2} c^{2}+a^{2} m^{2} b^{2}-b^{2} c^{2}+b^{4}=0$
or $\quad c^{2}=a^{2} m^{2}+b^{2}$
or $\quad c=\sqrt{a^{2} m^{2} b^{2}}$.
Putting the value of $c$ into (1), we have

$$
\frac{x=m x \sqrt{a^{2} m^{2} b^{2}}}{x}
$$

which are tangents to (2) for all non-zero values of $m$.

(iii) We replace $b^{2}$ by $-b^{2}$ in (ii) and the line $y=m x+c$ is a tangent to

$$
\frac{x^{2}}{a^{2}}-\frac{y^{2}}{b^{2}}=1 \quad \text { if } \quad c=\sqrt{a^{2} m^{2}-b^{2}}
$$

Thus $y=m x \sqrt{a^{2} m^{2}-b^{2}}$ are tangents to the hyperbola: $\frac{x^{2}}{a^{2}}-\frac{y^{2}}{b^{2}}=1$ for all non-zero values of $m$.

Example 4. Find an equation of the tangent to the parabola $y^{2}=-6 x$ which is parallel to the line $2 x+y+1=0$. Also find the point of tangency.

Solution: Slope of the required tangent is $\mathrm{m}=-2$
In the parabola $y^{2}=-6 x$

$$
a=\frac{-6}{4}=\frac{-3}{2}
$$

Equation of the tangent is

$$
y=m x+\frac{a}{m}=-2 x+\frac{3}{4}
$$

i.e., $8 x+4 y-3=0$

Inserting the value of $y$ from (2) viz $y=\frac{-8 x+3}{4}$ into (1), we have

$$
\left(\frac{-8 x+3}{4}\right)^{2}=-6 x
$$

or $\quad 64 x^{2}-48 x+9=-96 x \quad$ or $\quad 64 x^{2}+48 x+9=0$
or $\quad(8 x+3)^{2}=0 \quad$ i.e., $\quad x=\frac{-3}{8}$
Putting this value of $x$ into (2), we get

$$
y=\frac{-8\left(\frac{-3}{8}\right)+3}{4}-\frac{3}{2}
$$

The point of tangency is $\left(\frac{-3}{8}, \frac{3}{2}\right)$.

## Example 5. Find equations of the tangents to the ellipse

$$
\frac{x^{2}}{128}+\frac{y^{2}}{18}=1
$$

which are parallel to the line $3 x+8 y+1=0$. Also find the points of contact.
Solution: The slope of the required tangents is $\frac{-3}{8}$. Equations of the tangents are

$$
y=\frac{-3}{8} x \pm \sqrt{\left(128\left(\frac{-3}{8}\right)^{2}+18=\frac{-3}{8} x \pm 6\right.}
$$

Thus the two tangents are

$$
3 x+8 y+48=0
$$

and $3 x+8 y-48=0$
We solve (1) and (3) simultaneously to find the point of contact. Inserting the value of $y$ from (3) into (1), we get

$$
\begin{aligned}
& \frac{x^{2}}{128}+\frac{\left(\frac{-3}{8} x+6\right)^{2}}{18}=1 \quad \text { or } \quad \frac{x^{2}}{128}+\frac{9}{64} \frac{x^{2}+36}{18}-\frac{9}{2} x \\
& \text { or } \quad \frac{x^{2}}{128}+\frac{x^{2}}{128}+2-\frac{x}{4}=1-\text { or }=\frac{x^{2}}{64}-\frac{x}{4} \quad 1 \quad 0 \\
& \text { or } \quad\left(\frac{x}{8}-1\right)^{2}=0 \quad \text { i.e., } x=8 \quad \text { and so } \quad \frac{-3}{8} x \quad 6 \quad 3
\end{aligned}
$$

Thus $(8,3)$ is the point of tangency of $(3)$.
It can be seen in a similar manner that point of contact of (2) is $(-8,-3)$.
Example 6. Show that the product of the distances from the foci to any tangent to the hyperbola

$$
\frac{x^{2}}{a^{2}}-\frac{y^{2}}{b^{2}}=1
$$

is constant.

Solution: The line

$$
y=m x \sqrt{a^{2} m^{2}-b^{2}}
$$

is a tangent to (1).
Foci of (1) are $F(-c, 0)$ and $F^{\prime}(c, 0)$.
Distance of $F(-c, 0)$ from (2) is

$$
d_{1}=\frac{\left|-c m+\sqrt{a^{2} m^{2}-b^{2}}\right|}{\sqrt{1+m^{2}}}
$$

Distance of $F^{\prime}(c, 0)$ from (2) is

$$
\begin{aligned}
& d_{2}=\frac{\left|c m+\sqrt{a^{2} m^{2}-b^{2}}\right|}{\sqrt{1+m^{2}}} \\
& d_{1} \times d_{2}=\frac{\left|a^{2} m^{2}-b^{2}-c^{2} m^{2}\right|}{1+m^{2}}=\frac{\left|a^{2} m^{2}-c^{2}+a^{2}-c^{2} m^{2}\right|}{1+m^{2}} \text { as } b^{2}=c^{2}-a^{2} \\
& \left|a^{2}-c^{2}\right| \\
& =c^{2}-a^{2} \quad \text { since } \quad c>a
\end{aligned}
$$

which is constant.

## Intersection of Two Coincs

Suppose we are given two conics

$$
\frac{x^{2}}{a^{2}} \cdot \frac{y^{2}}{b^{2}}=1
$$

and $y^{2}=4 a x$
To find the points common to both (1) and (2), we need to solve (1) and (2) simultaneously. It is known from algebra, that the simultaneous solution set of two equations of the second degree consists of four points. Thus two conics will always intersect in four points. These points may be all real and distinct, two real and two imaginary or all imaginary. Two or more points may also coincide. Two conics are said to touch each other if they intersect in two or more coincident points.

Example 7. Find the points of intersection of the ellipse

$$
\frac{x^{2}}{43 / 3} \cdot \frac{y^{2}}{43 / 4}=1-(1)=\text { and the hyperbola } \quad \frac{x^{2}}{7} \cdot \frac{y^{2}}{14} 1
$$

Also sketch the graph of the two conics.
Solution: The two equations may be written as

$$
3 x^{2}+4 y^{2}=43 \quad \text { (1) and } 2 x^{2}-y^{2}=14
$$

Multiplying (2) by 4 and adding the result to (1), we get

$$
11 x^{2}=99 \quad \text { or } \quad x= \pm 3
$$

Setting $x=3$ in to (2), we have $18-y^{2}=14$ or $y= \pm 2$
Thus $(3,2)$ and $(3,-2)$ are two points of intersection of the two conics
Putting $x=-3$ into (2), we get

$$
y= \pm 2
$$

Therefore $(-3,2)$ and $(-3,-2)$ are also points of intersection of (1) and (2). The four points of intersection are as shown in the figure.
Example 8. Find the points of intersection of the conics

$$
y=1+x^{2}
$$

and $\quad y=1+4 x-x^{2}$
Also draw the graph of the conics.
Solution. From (1), we have

$$
x=\sqrt{y-1}
$$

Inserting these values of $x$ into (2), we get

$$
y=1 \pm 4 \sqrt{y-1}-(y-1)
$$

or

$$
2 y-2= \pm 4 \sqrt{y-1} \quad \text { or } \quad(y-1)^{2}=4(y-1)
$$

or

$$
(y-1)(y-1-4)=0
$$

Therefore, $\quad y=1,5$
When $\quad y=1, x=0$
When $\quad y=5, x= \pm 2$

But $(-2,5)$ does not satisfy (2).
Thus $(0,1)$ and $(2,5)$ are the points of intersections of (1) and (2). $y=1+x^{2}$ is a parabola with vertex at $(0,1)$ and opening upward, $y=1+4 x-x^{2}$ may be written as $y-5=-(x-2)^{2}$ which is a parabola with vertex. $(2,5)$ and opening downward
Example 9. Find equations of the common tangents to the two conics

$$
\frac{x^{2}}{16}+\frac{y^{2}}{25}=1 \quad+\quad \text { and } \quad \frac{x^{2}}{25}-\frac{y^{2}}{9}=1
$$

Solution. The tangents with slope $m$, to the two conics are respectively given by

$$
y=\pi n x \sqrt{16 m^{2} 25} \quad \text { and } \quad y=\pi n x \sqrt{25 m^{2} 9}
$$

For a tangent to be common, we must have

$$
16 m^{2}+25=25 m^{2}+9
$$

or $\quad 9 m=16 \quad$ or $\quad m= \pm \frac{4}{3}$.
Using these values of $m$, equations of the four common tangents are:

$$
\pi=\frac{4}{3} x \sqrt{481}
$$

## EXERCISE 6.7

1. Find equations of the tangent and normal to each of the following at the indicated point:
(i) $y^{2}=4 a x$
(ii) $\frac{x^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1$
(iii) $\frac{x^{2}}{a^{2}}-\frac{y^{2}}{b^{2}}=1$
at $\quad(a \cos \theta, b \sin \theta)$
at $\quad(a \sec \theta, b \tan \theta)$
2. Write equation of the tangent to the given conic at the indicated point
(i) $3 x^{2}=-16 y$ at the points whose ordinate is -3 .
(ii) $3 x^{2}-7 y^{2}=20$ at the points where $y=-1$.
(iii) $3 x^{2}-7 y^{2}+2 x-y-48=0$ at the point where $x=4$.
3. Find equations of the tangents to each of the following through the given point:
(i) $x^{2}+y^{2}=25$
(ii) $y^{2}=12 x$
(iii) $x^{2}-2 y^{2}=2$
through $(7,-1)$
through $(1,4)$
through $(1,-2)$
4. Find equations of the normals to the parabola $y^{2}=8 x$ which are parallel to the line $2 x+3 y=10$.
5. Find equations of the tangents to the ellipse $\frac{x^{2}}{4}+y^{2}=1$ which are parallel to the line $2 x-4 y+5=0$.
6. Find equations of the tangents to the conic $9 x^{2}-4 y^{2}=36$ parallel to $5 x-2 y+7=0$.
7. Find equations of the common tangents to the given conics
(i) $x^{2}=80 y$
(ii) $y^{2}=16 x$
and $x^{2}=2 y$
and $\quad \frac{x^{2}}{3}-\frac{y^{2}}{3}=1$
and $\quad x^{2}-y^{2}=1$
and $\quad 3 y^{2}-2 x^{2}=7$
and $\quad 9 x^{2}+y^{2}=124$
and $\quad x^{2}+y^{2}+y+8=0$

### 6.8 TRANSLATION AND ROTATION OF AXES

## Translation of Axes

In order to facilitate the investigation of properties of a curve with a given equation, it is sometimes necessary to shift the origin $O(0,0)$ to some other point $O^{\prime}(h, k)$. The axes $O^{\prime} X, O^{\prime} Y$ drawn through $O^{\prime}$ remain parallel to the original axes $O x$ and $O y$. The process is called translation of axes.

We have already obtained in Chapter 4 formulas showing relationships between the two sets of coordinates of a point referred to the two sets of coordinate axes.

Recall that if a point $P$ has coordinates $(x$, $y)$ referred to the $x y$-system and has coordinates $(X, Y)$ referred to the translated axes $O^{\prime} X, O^{\prime} Y$ through $O^{\prime}(h, k)$, then
$$
\left.\begin{array}{l}
x=X+h \\
y=T+k
\end{array}\right\}
$$

These are called equations of transformation.
From (1), we have

$$
\left.\begin{array}{l}
X=x-h \\
Y=y-k
\end{array}\right\}
$$

(1) and (2) will be used to transform an equation in one system into the other system. The axes $O x$ and $O y$ are referred to as the original (or old) axes and $O^{\prime} X, O^{\prime} Y$ are called the translated axes (or new axes).

Example 1: Transform the equation $x^{2}+6 x-8 y+17=0$
referred to $O^{\prime}(-3,1)$ as origin, axes remaining parallel to the old axes.

Solution. Equations of transformation are

$$
\begin{aligned}
& x=X-3 \\
& y=Y+1
\end{aligned}
$$

Substituting these values of $x, y$ into (1), we have

$$
(X-3)^{2}+6(X-3)-8(Y+1)+17=0
$$

or $\quad X^{2}-6 X+9+6 X-18-8 Y-8+17=0$
or $\quad X^{2}-8 Y=0$ is the required transformed equation.

Example 2: By transforming the equation

$$
x^{2}+4 y^{2}-4 x+8 y+4=0
$$

referred to a new origin and axes remaining parallel to the original axes, the first degree terms are removed. Find the coordinates of the new origin and the transformed equation.

Solution. Let the coordinates of the new origin be $(h, k)$. Equations of transformation are

$$
\begin{aligned}
& x=X+h \quad, \quad y=Y+k \\
& \text { Substituting these values of } x, y \text { into (1), we get } \\
& (X+h)^{2}+4(Y+k)^{2}-4(X+h)+8(Y+k)+4=0 \\
& \text { or } \quad X^{2}+4 Y^{2}+X(2 h-4)+Y(8 k+8)+h^{2}+4 k^{2}-4 h+8 k+4=0
\end{aligned}
$$

$(h, k)$ is to be so chosen that first degree terms are removed from the transformed equation.

Therefore, $2 h-4=0$ and $8 k+8=0$ giving $h=2$ and $k=-1$. New origin is $O^{\prime}(2,-1)$. Putting $h=2, k=-1$ into (2), the transformed equation is $X^{2}+4 Y^{2}-4=0$.

## Rotation of Axes

To find equations for a rotation of axes about the origin through an angle $\theta(0<\theta<90^{\circ})$. (origin remaining unaltered).

Let the axes be rotated about the origin through an angle $\theta$. The new axes $O X, O Y$ are as shown in the figure.

Let $P$ be any point in the plane with coordinates $P(x, y)$ referred to the $x y$-system and $P(X, Y)$ referred to the $X Y$-system. In either system the distance $r$ between $P$ and $O$ is the same. Draw $P M \perp O x$ and $P Q \perp O X$. Let $\alpha$ be the inclination of $O P$ with $O X$. From the figure, we have
$$
\begin{aligned}
& X=O Q=r \cos \alpha, Y=Q P=r \sin \alpha \\
& \text { and } \quad x=r \cos (\theta+\alpha), y=r \sin (\theta+\alpha) \\
& \text { or } \quad\left.\begin{array}{l}
x=r \cos \theta \cos \alpha \quad r \sin \theta \sin \alpha \\
y=r \sin \theta \cos \alpha+r \cos \theta \sin \alpha
\end{array}\right\}
\end{aligned}
$$

Substituting the values of $r \cos \alpha, r \sin \alpha$ from (1) into (2), we get

$$
\left.\begin{array}{l}
x=X \cos \theta-Y \sin \theta \\
y=X \sin \theta+y \cos \theta
\end{array}\right]
$$

as the required equations of transformation for a rotation of axes through an angle $\theta$.
Example 3: Find an equation of $5 x^{2}-6 x y+5 y^{2}-8=0$ with respect to new axes obtained by rotation of axes about the origin through an angle of $135^{\circ}$.

Solution. Here $\theta=135$. Equations of transformation are

$$
\begin{aligned}
& x=X \cos 135^{\circ}-Y \sin 135^{\circ}=\frac{-X}{\sqrt{2}}-\frac{Y}{\sqrt{2}}=\frac{-1}{\sqrt{2}}(X+Y) \\
& x=X \sin 135^{\circ}+Y \cos 135^{\circ}=\frac{X}{\sqrt{2}}-\frac{Y}{\sqrt{2}}=\frac{1}{\sqrt{2}}(X-Y)
\end{aligned}
$$

Substituting these expressions for $x, y$ into the given equation, we have

$$
\begin{aligned}
& 5\left(-\frac{X+Y}{\sqrt{2}}\right)^{2}-6\left(-\frac{X+Y}{\sqrt{2}}-\frac{X-Y}{\sqrt{2}}\right)+5\left(\frac{X-Y}{\sqrt{2}}\right)^{2}-8=0 \\
\text { or } \quad & \frac{5}{2}\left(X^{2}+2 X Y+Y^{2}\right)+3\left(X^{2}-Y^{2}\right)+\frac{5}{2}\left(X^{2}-2 X Y+Y^{2}\right)-8=0 \\
\text { or } & 8 x^{2}+2 y^{2}-8=0 \quad \text { or } \quad 4 x^{2}+y^{2}=4
\end{aligned}
$$

is the required transformed equation.

Example 4: Find the angle through which the axes be rotated about the origin so that the product term $X Y$ is removed from the transformed equation of $5 x^{2}+2 \sqrt{3} x y+7 x^{2}-16=0$. Also find the transformed equation.

Solution. Let the axes be rotated through an angle $\theta$. Equations of transformation are

$$
x=X \cos \theta-Y \sin \theta \quad ; \quad y=X \sin \theta+Y \cos \theta
$$

Substituting into the given equation, we get

$$
\begin{aligned}
& 5(X \cos \theta-Y \sin \theta)^{2}+2 \sqrt{3}(X \cos \theta-Y \sin \theta)(X \sin \theta+Y \cos \theta) \\
& +7(X \sin \theta+y \cos \theta)^{2}-16=0
\end{aligned}
$$

Since this equation is to be free from the product term $X Y$, the coefficient of $X Y$ is zero, i.e. $-10 \sin \theta \cos \theta+2 \sqrt{3}\left(\cos ^{2} \theta-\sin ^{2} \theta\right)+14 \sin \theta \cos \theta=0$

$$
\text { or } \quad 2 \sin 2 \theta+2 \sqrt{3} \cos 2 \theta=0
$$

$$
\text { or } \quad \tan 2 \theta=\frac{-2 \sqrt{3}}{2}=\tan 120^{\circ} \quad \text { or } \quad \theta=60^{\circ}
$$

Thus axes be rotated through an angle of $60^{\circ}$ so that $X Y$ term is removed from the transformed equation.

Setting $\theta=60^{\circ}$ into (1), the transformed equation is (after simplification)

$$
8 x^{2}+4 y^{2}-16=0 \quad \text { or } \quad 2 x^{2}+y^{2}-4=0
$$

## EXERCISE 6.8

1. Find an equation of each of the following with respect to new parallel axes obtained by shifting the origin to the indicated point:
(i) $x^{2}+16 y-16 \quad=0, \quad O^{\prime}(0,1)$
(ii) $4 x^{2}+y^{2}+16 x-10 y+37 \quad=0, \quad O^{\prime}(2,5)$
(iii) $9 x^{2}+4 x^{2}+18 x-16 y-11 \quad=0, \quad O^{\prime}(-1,2)$
(iv) $x^{2}-y^{2}+4 x+8 y-11 \quad=0, \quad O^{\prime}(-2,4)$
(v) $9 x^{2}-4 y^{2}+36 x+8 y-4 \quad=0, \quad O^{\prime}(2,1)$
2. Find coordinates of the new origin (axes remaining parallel) so that first degree terms are removed from the transformed equation of each of the following. Also find the transformed equation:
(i) $3 x^{2}-2 y^{2}+24 x+12 y+24=0$
(ii) $25 x^{2}+9 y^{2}+50 x-36 y-164=0$
(iii) $x^{2}-y^{2}-6 x+2 y+7=0$
3. In each of the following, find an equation referred to the new axes obtained by rotation of axes about the origin through the given angle:
(i) $x y=1, \quad \theta=45^{\circ}$
(ii) $7 x^{2}-8 x y+y^{2}-9=0, \quad \theta=\arctan 2$
(iii) $9 x^{2}+12 x y+4 y^{2}-x-y=0, \quad \theta=\arctan \frac{2}{3}$
(iv) $x^{2}-2 x y+y^{2}-2 \sqrt{2} x-2 \sqrt{2} y+2=0, \quad \theta=45^{\circ}$

4. Find measure of the angle through which the axes be rotated so that the product term $X Y$ is removed from the transformed equation. Also find the transformed equation:
(i) $2 x^{2}+6 x y+10 y^{2}-11=0$
(ii) $x y+4 x-3 y-10=0$
(iii) $5 x^{2}-6 x y+5 y^{2}-8=0$

### 6.9 THE GENERAL EQUATION OF SECOND DEGREE

Standard equations of conic sections, namely circle, parabola, ellipse and hyperbola have already been studied in the previous sections. Now we shall take up the general equation of second degree viz.

$$
A x^{2}+B y^{2}+G x+F y+C=0
$$

The nature of the curve represented by (1) can be determined by examining the coefficients $A, B$ in the above equation. The following cases arise:
(i) If $A=B \neq 0$, equation (1) may be written as

$$
\begin{aligned}
& A\left(x^{2}+y^{2}\right)+G x+F y+C=0 \text { or } \quad x^{2}+y^{2}+\frac{G}{A} x+\frac{F}{A} y+\frac{C}{A}=0 \\
& \text { which represents a circle with centre at }\left(-\frac{G}{2 A},-\frac{F}{2 A}\right) \text { and radius } \sqrt{\frac{G^{2}}{4 A^{2}}+\frac{F^{2}}{4 A}-\frac{C}{A}}
\end{aligned}
$$

(ii) If $\quad A \neq B$ and both are of the same sign, then we have $\left(A x^{2}+G x\right)+\left(B y^{2}+F y\right)+C=0$
or $\quad A\left(x^{2}+\frac{G}{A} x+\frac{G^{2}}{4 A^{2}}\right)+B\left(y^{2}+\frac{F}{B} y+\frac{F^{2}}{4 B^{2}}\right)=\frac{G^{2}}{4 A}+\frac{F^{2}}{4 B}-C$
or $\quad A\left(x+\frac{G}{2 A}\right)^{2}+B\left(y+\frac{F}{2 B}\right)^{2}=\frac{G^{2}}{4 A}+\frac{F^{2}}{4 B}-C$
If we write $X \Leftrightarrow x \quad \frac{G}{4 A}, Y \quad y \quad \frac{F}{2 B}$, then (2) can be written as
$A X^{2}+B Y^{2}=\frac{G^{2}}{4 A}+\frac{F^{2}}{4 B}-C=K$ (say) or $\frac{X^{2}}{(\sqrt{K / A})^{2}}-\frac{Y^{2}}{(\sqrt{K / B})^{2}}, \quad 1$
which is standard equation of an ellipse in $X Y$-coordinate system.
(iii) If $A \neq B$ and both have opposite signs (say $A$ is positive and $B$ is negative),
we can write (1) as
or $\quad A\left(x^{2}+\frac{G}{A} x+\frac{G^{2}}{4 A^{2}}\right)-B^{\prime}\left(y^{2}-\frac{F}{B^{\prime}} y+\frac{F^{2}}{4 B^{\prime 2}}\right)=\frac{G^{2}}{4 A}-\frac{F^{2}}{4 B^{\prime}}-C=M$ (say)
or $\quad A\left(x+\frac{G}{2 A}\right)^{2}-B^{\prime}\left(y-\frac{F}{2 B^{\prime}}\right)^{2}=M$
or $\quad A X^{2}-B^{\prime} Y^{2}=M$, where $X=x-\frac{G}{2 A}, \quad Y \quad y-\frac{F}{2 B^{\prime}}$
or $\quad \frac{X^{2}}{(\sqrt{M / A})^{2}}-\frac{Y^{2}}{\left(\sqrt{M / B^{2}}\right)^{2}}=1$
and this is standard equation of a hyperbola in $X Y$-coordinates system.
(iv) If $A=0$ or $B=0$ (both cannot be zero since in that case the equation (1) reduces to a linear equation). Assume $A \neq 0$ and $B=0$.
The equation (1) becomes $A x^{2}+G x+F y+C=0$
or $\quad A\left(x^{2}+\frac{G}{A} x+\frac{G^{2}}{4 A^{2}}\right)=-F y-C+\frac{G^{2}}{4 A}$
or $\quad A\left(x+\frac{G}{2 A}\right)^{2}=-F\left(y+\frac{C}{F}-\frac{G^{2}}{4 A F}\right)$
or $\quad A X^{2}=-F Y$, where $X=x+\frac{G}{2 A}, \quad Y=y+\frac{C}{F}-\frac{G^{2}}{4 A F}$
which is standard equation of a parabola in $X Y$-coordinates system.
We summarize these results as under:
Let an equation of second degree be of the form $A x^{2}+B y^{2}+G x+F y+C=0$. It represents:
(i) a circle if $A=B \neq 0$
(ii) an ellipse if $A \neq B$ and both are of the same sign
(iii) a hyperbola if $A \neq B$ and both are of opposite signs
(iv) a parabola if either $A=0$ or $B=0$.

### 6.9.1 Classification of Conics by the Discriminant

The most general equation of the second degree

$$
\alpha x^{2}+2 h x y+b y^{2}+2 g x+2 f y+c=0
$$

represents a conic. The quantity $h^{2}-a b$ is called the discriminant of (1). Nature of the conic can be determined by the discriminant as follows. (1) represents:
(i) an ellipse or a circle if $h^{2}-a b<0$
(ii) a parabola if $h^{2}-a b=0$
(iii) a hyperbola if $h^{2}-a b>0$

The equation (1) can be transformed to the form

$$
A X^{2}+B Y^{2}+2 G X+2 F y+C=0
$$

if the axes are rotated about the origin through an angle $\theta,\left(0<\theta<90^{\circ}\right)$ where $\theta$ is given by

$$
\tan 2 \theta=\frac{2 h}{a-b}
$$

If $a=b$ or $a=0=b$, then the axes are to be rotated through an angle of $45^{\circ}$.
Equations of transformation (as already found) are

$$
\left.\begin{array}{l}
x=X \cos \theta-Y \sin \theta \\
y=X \sin \theta+Y \cos \theta
\end{array}\right\}
$$

Substitution of these values of $x, y$ into (1) will result in an equation of the form (2) in which product term $X Y$ will be missing. Nature of the conic (2) has already been discussed in the last article.

Solving equations (3) for $X, Y$ we find

$$
\left.\begin{array}{l}
X=x \cos \theta+y \sin \theta \\
Y=\pi \sin \theta \quad y \cos \theta
\end{array}\right\}
$$

These equations will be useful in numerical problems.
Note: Under certain conditions equation (1) may not represent any conic, in such a case we say (1) represents a degenerate conic.

One such degenerate conic is a pair of straight lines represented by (1) if

$$
\left.\begin{array}{lll}
a & h & g \\
h & b & f \\
g & f & c
\end{array}\right\}=0
$$

The proofs of the above observations are beyond our scope and are omitted.

## Example 1: $\quad$ Discuss the conic $7 x^{2}-6 \sqrt{3} x y+13 y^{2}-16=0$ and find its elements.

Solution. In order to remove the term involving $x y$, the angle through which axes be rotated is given by

$$
\tan 2 \theta=\frac{-6 \sqrt{3}}{7-13}=\sqrt{3} \quad{ }^{\circ} \text { or } \quad \theta \approx 30
$$

Equations of transformation are

$$
\begin{aligned}
& x=X \cos 30^{\circ}-Y \sin 30^{\circ}=\frac{\sqrt{3} X-Y}{2} \\
& y=X \sin 30^{\circ}+Y \cos 30^{\circ}=\frac{X+\sqrt{3} Y}{2}
\end{aligned}
$$

Substituting these expressions in to the equation (1), we get

$$
\sqrt[3]{\left(\frac{\sqrt{3} X-Y}{2}\right)^{2}-6 \sqrt{3}\left(\frac{\sqrt{3} X-Y}{2}\right)\left(\frac{X+\sqrt{3} Y}{2}\right)}+13\left(\frac{X+\sqrt{3} Y}{2}\right)^{2}=16
$$

which simplifies to

$$
4 X^{2}+16 Y^{2}=16+\quad \text { or } \quad \frac{X^{2}}{4} \quad \frac{Y^{2}}{1} \quad 1
$$

This is an ellipse.
Solving equations (2) for $X$ and $Y$, (or as already found in (4) of 7.7.1, we have

$$
X=\frac{\sqrt{3} x+y}{2}, \quad Y \quad \frac{-x+\sqrt{3} y}{2}
$$

Centre of the ellipse (3) is $X=0, Y=0$
i.e., $\quad \sqrt{3} x+y=0-\quad+$ and $=\quad x \quad \sqrt{3} y \quad 0$
giving $\quad x=0, y=0$. Thus centre of (1) is $(0,0)$
Length of the major axis $=4$, length of minor axis $=2$
Vertices of (3) are: $\quad X=\pm 2, Y=0$

$$
\text { i.e., } \quad \frac{\sqrt{3} x+y}{2}=2 \quad \text { and } \quad \frac{-x+\sqrt{3} y}{2} \quad 0
$$

Solving these equations for $x, y$, we have

$$
(\sqrt{3}, 1),(-\sqrt{3},-1), \text { as vertices of }(1)
$$

Ends of the minor axis are $X=0$ and $Y=1$ i.e., $\frac{\sqrt{3} x+y}{2} \quad 0$ and $\frac{-x+\sqrt{3} y}{2}= \pm 1$. Solving these equations, we get $\left(\frac{1}{2}, \frac{-\sqrt{3}}{2}\right)$ and $\left(-\frac{1}{2}, \frac{\sqrt{3}}{2}\right)$
as ends of the minor axis of (1).
Equation of the major axis: $Y=0$,
i.e.,

$$
-x+\sqrt{3} y=0
$$

Equation of the minor axis: $X=0$,
i.e., $\sqrt{3} x+y=0$

Example 2: Analyze the conic $x y=4$ and write its elements.
Solution: Equation of the conic is

$$
x y-4=0
$$

Here $a=0=b$, so we rotate the axes through an angle of $45^{\circ}$. Equations of transformation are

$$
\begin{aligned}
& x=X \cos 45^{\circ}-Y \sin 45^{\circ}=\frac{X-Y}{\sqrt{2}} \\
& y=X \sin 45^{\circ}-Y \cos 45^{\circ}=\frac{X+Y}{\sqrt{2}}
\end{aligned}
$$

Substituting into (1), we have

$$
\left(\frac{X-Y}{\sqrt{2}}\right)\left(\frac{X+Y}{\sqrt{2}}\right)-4=0
$$

or $X^{2}-Y^{2}=8$

$$
\frac{X^{2}}{8} \cdot \frac{Y^{2}}{8}=1
$$

which is a hyperbola.
Solving equations (2) for $X, Y$, we have

$$
X=\frac{x+y}{\sqrt{2}}, \quad Y \quad \frac{-x+y}{\sqrt{2}}
$$

Centre of the hyperbola (3) is

$$
X=0, Y=0
$$

i.e., $\frac{x+y}{\sqrt{2}}=0, \quad$ and $\frac{-x+y}{\sqrt{2}} \quad 0$
or $\quad x=0, \quad y=0$ is the centre of (1)
Equation of the focal axis: $\quad Y=0$ i.e. $\quad y=x$.
Equation of the conjugate axis: $\quad X=0$ i.e. $\quad y=-x$.
Eccentricity $=\sqrt{2}$
Foci of (3): $X=2 \sqrt{2} \cdot \sqrt{2} \quad \pm Y \quad 0$
or $\quad x+y= \pm 4 \sqrt{2}$
and $-x+y=0$
Solving the above equations for $x, y$, we have the foci of (1) as $(2 \sqrt{2}, 2 \sqrt{2})$ and $(-2 \sqrt{2},-2 \sqrt{2})$ Vertices of (3): $X=2 \sqrt{2}, \quad Y \quad 0$
i.e., $\frac{x+y}{\sqrt{2}}= \pm 2 \sqrt{2}$ and $-x+y \neq 0$

Solving these equations, we have the foci of (1) as

$$
(2 \sqrt{2}, 2 \sqrt{2}) \text { and }(-2 \sqrt{2},-2 \sqrt{2})
$$

Vertices of (3): $X=2 \sqrt{2}, \quad Y \quad 0$

$$
\frac{x+y}{\sqrt{2}}= \pm 2 \sqrt{2} \quad \text { and } \quad-x+y=0
$$

Solving these equations, we have
$(2,2),(-2,-2)$ as vertices of (1).

Asymptotes of the hyperbola (3) are given by $X^{2}-Y^{2}=0$
or $\quad X-Y=0 \quad$ and $\quad X+Y=0$
i.e., $\frac{x+y}{\sqrt{2}}-\frac{-x+y}{\sqrt{2}}=0$ and $\frac{x+y}{\sqrt{2}}-\frac{-x+y}{\sqrt{2}}=0$
i.e., $x=0$ and $y=0$ are equations of the asymptotes of (1).

Example 3: By a rotation of axes, eliminate the $x y$-term in the equation

$$
9 x^{2}+12 x y+4 y^{2}+2 x-3 y=0
$$

Identify the conic and find its elements.

Solution: Here $a=9, b=4,2 h=12$. The angle $\theta$ through which axes be rotated to given by

$$
\begin{aligned}
& \tan 2 \theta=\frac{12}{9-4}=\frac{12}{5} \\
& \text { or } \quad \frac{2 \tan \theta}{1-\tan ^{2} \theta}=\frac{12}{5} \\
& \text { or } 5 \tan \theta=6-6 \tan ^{2} \theta \\
& \text { or } 6 \tan ^{2} \theta+5 \tan \theta-6=0 \\
& \tan \theta=\frac{-5 \pm \sqrt{25+144}}{12}=\frac{-5 \pm 13}{12} \quad \frac{2}{3}, \frac{-3}{2}
\end{aligned}
$$

Since $\theta$ lies in the first quadrant, $\tan \theta=-\frac{2}{3}$ is not admissible.

$$
\tan \theta=\frac{2}{3} \Rightarrow \quad \sin \theta \quad \frac{2}{\sqrt{13}}, \quad \cos \theta \quad \frac{3}{\sqrt{13}}
$$

Equations of transformation become

$$
\begin{aligned}
& x=X \cos \theta-Y \sin \theta=\frac{2}{\sqrt{13}} X-\frac{2}{\sqrt{13}} Y \\
& y=X \sin \theta+Y \cos \theta=\frac{2}{\sqrt{13}} X+\frac{3}{\sqrt{13}} Y
\end{aligned}
$$

Substituting these expressions for $x$ and $y$ into (1), we get

$$
\begin{aligned}
& \frac{9}{(\sqrt{13})^{2}}(3 X-2 Y)^{2}+\frac{12}{13}(3 X-2 Y)(3 X+3 Y)+\frac{4}{13}(2 X+3 Y)^{2} \\
& +\frac{2}{\sqrt{13}}(3 X-2 Y)-\frac{3}{\sqrt{13}}(2 X+3 Y)=0 \\
& \text { or } \quad \frac{9}{13}\left(9 X^{2}-12 X Y+9 Y^{2}\right)+\frac{12}{13}\left(6 X^{2}+5 X Y-6 Y^{2}\right) \\
& +\frac{4}{13}\left(4 X^{2}+12 X Y-9 Y^{2}\right)-\sqrt{13} Y=0 \\
& \text { or } \quad\left(\frac{81}{13}+\frac{72}{13}+\frac{16}{13}\right) X^{2}+\left(-\frac{108}{13}+\frac{60}{13}+\frac{48}{13}\right) X Y \\
& +\left(\frac{36}{13}, \frac{72}{13}+\frac{36}{13}\right) Y^{2}-\sqrt{13} Y=0
\end{aligned}
$$

or $13 X^{2}-\sqrt{13} Y=0 \quad$ or $\quad X^{2} \quad \frac{1}{\sqrt{13}} Y$
which is a parabola.
Solving equation (2) for $X, Y$, we have $X=\frac{3 x+2 y}{\sqrt{13}}, Y=\frac{-2 x+3 y}{\sqrt{13}}$
Elements of the parabola are:
Focus: $X=0, \quad Y=\frac{1}{4 \sqrt{13}}$
i.e., $\frac{3 x+2 y}{\sqrt{13}}=\theta \quad$ and $\quad \frac{-2 x+3 y}{\sqrt{13}} \quad \frac{1}{4 \sqrt{13}}$

Solving these equations, we have $x=\frac{1}{26}, y \quad \frac{3}{52}$ i.e., Focus $\left(\frac{1}{26}, \frac{3}{52}\right)$
Vertex: $\quad X=0, \quad Y=0 \quad$ i.e., $\quad 3 x+2 y=0$ and $-2 x+3 y=0$
i.e., $\quad x=0, \quad y=0 \quad$ i.e., $\quad(0,0)$

Axis: $\quad X=0 \quad$ i.e., $\quad 3 x+2 y=0$

$$
x \text {-intercept }=-\frac{2}{9}, \quad y \text {-intercept }=\frac{3}{4}
$$

Example 4: $\quad$ Show that $2 x^{2}-x y+5 x-2 y+2=0$ represents a pair of lines. Also find an equation of each line.

Solution: Here $a=2, b=0, h=\frac{1}{2}, g \quad \frac{5}{2}, f \quad 1, c=2$.

$$
\begin{gathered}
\left|\begin{array}{ccc}
a & h & g \\
h & b & f \\
g & f & c
\end{array}\right|=\left|\begin{array}{ccc}
2 & -\frac{1}{2} & \frac{5}{2} \\
\frac{1}{2} & 0 & 1 \\
\frac{5}{2} & -1 & 2 \\
\end{array}\right| \\
=\frac{1}{2}\left(-1+\frac{5}{2}\right)+1\left(-2+\frac{5}{4}\right)
\end{gathered}
$$

$$
-\frac{3}{4}-\frac{3}{4}=0
$$

The given equation represents a degenerate conic which is a pair of lines. The given equation is

$$
\begin{aligned}
& 2 x^{2}+x(5-y)+(-2 y+2)=0 \\
\text { or } \quad & x=\frac{y-5 \pm \sqrt{(y-5)^{2}-h(-2 y+2)}}{4} \\
& =\frac{y-5 \pm \sqrt{y^{2}-10 y+25+16 y-16}}{4} \\
& =\frac{y-5 \pm(y+3)}{4} \\
& =\frac{2 y-2}{4}, \quad-2
\end{aligned}
$$

Equations of the lines are $2 x-y+1=0$ and $x+2=0$.

## Tangent

Find an equation of the tangent to the conic

$$
a x^{2}+2 h x y+b y^{2}+2 g x+2 f y+c=0
$$

at the point $\left(x_{1}, y_{1}\right)$
Differentiating (1) w.r.t. $\quad x$, we have

$$
2 a x+2 h y+2 h x \frac{d y}{d x}+2 b y \frac{d y}{d x}+2 g+2 f \frac{d y}{d x}=0
$$

or $\quad \frac{d y}{d x}=-\frac{a x+h y+g}{h x+b y+f}$
or $\left.\frac{d y}{d x}\right|_{x_{1}, y_{1}}=-\frac{a x_{1}+h y_{1}+g}{h x_{1}+b y_{1}+f}$
Equation of the tangent at $\left(x_{1}, y_{1}\right)$ is

$$
y-y_{1}=-\frac{a x_{1}+h y_{1}+g}{h x_{1}+b y_{1}+f}\left(x_{1}, y_{1}\right)
$$

or $\quad(x-x_{1})\left(a x_{1}+h y_{1}+g\right)+(y-y_{1})\left(h x_{1}+b y_{1}+f\right)=0$
or $\quad a x x_{1}+h x y_{1}+g x++h x_{1} y+b y_{1} y+f y$

$$
=a x_{1}^{2}+2 h x_{1} y_{1}+g x_{1}+b y_{1}^{2}+f y_{1}
$$

Adding $g x_{1}+f y_{1}+c$ to both sides of the above equation and regrouping the terms, we have

$$
\begin{aligned}
& a x x_{1}+h\left(x y_{1}+y x_{1}\right)+b y y_{1}+g\left(x+x_{1}\right)+f\left(y+y_{1}\right)+c \\
& =a x_{1}^{2}+2 h x_{1} y_{1}+b y_{1}^{2}+2 g x_{1}+2 f y_{1}+c \\
& =0
\end{aligned}
$$

since the point $\left(x_{1}, y_{1}\right)$ lies on (1).
Hence an equation of the tangent to (1) at $\left(x_{1}, y_{1}\right)$ is

$$
a x x_{1}+h\left(x y_{1}+y x_{1}\right)+b y y_{1}+g\left(x+x_{1}\right)+f\left(y+y_{1}\right)+c=0
$$

Note: An equation of the tangent to the general equation of the second degree at the point $\left(x_{1}, y_{1}\right)$ may be obtained by replacing

$$
\begin{aligned}
& x^{2} \text { by } x x_{1} \\
& y^{2} \text { by } y y_{1} \\
& 2 x y \text { by } x y_{1}+y x_{1} \\
& 2 x \text { by } x+x_{1} \\
& 2 y \text { by } y+y_{1}
\end{aligned}
$$

in the equation of the conic
Example 5: Find an equation of the tangent to the conic $x^{2}-x y+y^{2}-2=0$ at the point whose ordinate is $\sqrt{2}$.

Solution: Putting $y=\sqrt{2}$ into the given equation, we have

$$
\begin{aligned}
& x^{2}-\sqrt{2} x=0 \\
& x(x-\sqrt{2})=0 \quad x=0, \sqrt{2}
\end{aligned}
$$

The two points on the conic are $(0, \sqrt{2})$ and $(\sqrt{2}, \sqrt{2})$.
Tangent at $(0, \sqrt{2})$ is

$$
0 . x-\frac{1}{2}(x . \sqrt{2}+0 . y)+\sqrt{2} y-2=0
$$

or $\quad x-2 y+2 \sqrt{2}=0$
Tangent at $(\sqrt{2}, \sqrt{2})$ is

$$
\sqrt{2} x-\frac{1}{2}(\sqrt{2} x+\sqrt{2} y)+\sqrt{2} y-2=0
$$

or $\quad \sqrt{2} x+\sqrt{2} y-4=0$

# EXERCISE 6.9

1. By a rotation of axes, eliminate the $x y$-term in each of the following equations. Identify the conic and find its elements:
(i) $4 x^{2}-4 x y+y^{2}-6=0$
(ii) $x^{2}-2 x y+y^{2}-8 x-8 y=0$
(iii) $x^{2}+2 x y+y^{2}+2 \sqrt{2}-2 \sqrt{2} y+2=0$
(iv) $x^{2}+x y+y^{2}-4=0$
(v) $7 x^{2}-6 \sqrt{3} x y+13 y^{2}-16=0$
(vi) $4 x^{2}-4 x y+7 y^{2}+12 x+6 y-9=0$
(vii) $x y-4 x-2 y=0$
(viii) $x^{2}+4 x y-2 y^{2}-6=0$
(ix) $x^{2}-4 x y-2 y^{2}+10 x+4 y=0$
2. Show that
(i) $10 x y+8 x-15 y-12=0 \quad$ and
(ii) $6 x^{2}+x y-y^{2}-21 x-8 y+9=0$
each represents a pair of straight lines and find an equation of each line.
3. Find an equation of the tangent to each of the given conics at the indicated point.
(i) $3 x^{2}-7 y^{2}+2 x-y-48=0$
at $(4,1)$
(ii) $x^{2}+5 x y-4 y^{2}+4=0$
at $\quad y=-1$
(iii) $x^{2}+4 x y-3 y^{2}-5 x-9 y+6=0$
at $\quad x=3$.