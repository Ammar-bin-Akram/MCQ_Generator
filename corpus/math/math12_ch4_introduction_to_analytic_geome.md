# Chapter 4: Introduction to Analytic Geometry

## 4.1 INTRODUCTION

Geometry is one of the most ancient branches of mathematics. The Greeks systematically studied it about four centuries B.C. Most of the geometry taught in schools is due to Euclid who expounded thirteen books on the subject ( 300 B.C.). A French philosopher and $m$ athematician Rene Descartes (1596-1650 A.D.) introduced algebraic methods in geometry which gave birth to analytical geometry (or coordinate geometry). Our aim is to present fundamentals of the subject in this book.

## Coordinate System

Draw in a plane two mutually perpendicular number lines $x^{\prime} x$ and $y^{\prime} y$, one horizontal and the other vertical. Let their point of intersection be $O$, to which we call the origin and the real number 0 of both the lines is represented by $O$. The two lines are called the coordinate axes. The horizontal line $x^{\prime} O x$ is called the $\boldsymbol{x}$-axis and the vertical line $y^{\prime} O y$ is called the $\boldsymbol{y}$-axis.

As in the case of number line, we follow the convention that all points on the $y$-axis above $x^{\prime} O x$ are associated with positive real numbers, those below $x^{\prime} O x$ with negative real numbers. Similarly, all points on the $x$-axis and lying on the right of $O$ will be positive and those on the left of $O$ and lying on the $x$-axis will be negative.

Suppose $P$ is any point in the plane. Then $\boldsymbol{P}$ can be located by using an ordered pair of real numbers. Through $P$ draw lines parallel to the coordinates axes meeting $x$-axis at $R$ and $y$-axis at $S$.
Let the directed distance $\overline{O R}=x$ and the directed distance $\overline{O S}=y$.
The ordered pair $(x, y)$ gives us enough information to locate the point $P$. Thus, with every point $P$ in the plane, we can associate an ordered pair of real numbers $(x, y)$ and we say
version: 1.1
that $P$ has coordinates $(x, y)$. It may be noted that $x$ and $y$ are the directed distances of $P$ from the $y$-axis and the $x$-axis respectively. The reverse of this technique also provides method for associating exactly one point in the plane with any ordered pair $(x, y)$ of real numbers. This method of pairing off in a one-to-one fashion the points in a plane with ordered pairs of real numbers is called the two dimensional rectangular (or Cartesian) coordinate system.

If $(x, y)$ are the coordinates of a point $P$, then the first member (component) of the ordered pair is called the $\boldsymbol{x}$-coordinate or abscissa of $P$ and the second member of the ordered pair is called the $\boldsymbol{y}$-coordinate or ordinate of $P$. Note that abscissa is always first element and the ordinate is second element in an ordered pair.
The coordinate axes divide the plane into four equal parts called quadrants. They are defined as follows:

Quadrant I: All points $(x, y)$ with $x>0, y>0$
Quadrant II: All points $(x, y)$ with $x<0, y>0$
Quadrant III: All points $(x, y)$ with $x<0, y<0$
Quadrant IV: All points $(x, y)$ with $x>0, y<0$
The point $P$ in the plane that corresponds to an ordered pair $(x, y)$ is called the graph of $(x, y)$.
Thus given a set of ordered pairs of real numbers, the graph of the set is the aggregate of all points in the plane that correspond to ordered pairs of the set.

## i- Write down the coordinates of the points if not mentioned.
ii- Locate $(0,-1),(2,2),(-4,7)$ and $(-3,-3)$.

#### 4.1.1 The Distance Formula

Let *A* (*x*<sub>1</sub>, *y*<sub>1</sub>) and *B* (*x*<sub>2</sub>, *y*<sub>2</sub>) be two points in the plane. We can find the distance *d* = |*AB*| from the right triangle *AQB* by using the Pythagorean theorem. We have

$$
d = AB = AQ + QB^2 \tag{1}
$$

|*AQ*| = |*BS*| = |*BO* + *OS*|

|*OR* | *OS*|

|*SB*| = |*SB* - *SQ*|

|*y*<sub>1</sub> | *y*<sub>1</sub> | | || || | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |

or

$$
x = \frac{k_1 v_1 + k_2 v_2}{k_1 + k_2}
$$

Similarly, by drawing perpendiculars from *A*, *B* and *P* to the *y*-axis and proceeding as before, we can show that

$$
y = \frac{k_1 v_1 + k_2 v_2}{k_1 + k_2}
$$

#### **Note:**

(i) If the directed distances *AP* and *PB* have the same sign, then their ratio is positive and *P* is said to divide *AB* internally.

(ii) If the directed distances *AP* and *PB* have opposite signs i.e., *P* is beyond *AB*, then their ratio is negative and *P* is said to divide *AB* **externally**.

$$
\frac{AP}{BP} = \frac{k_1}{k_2} \quad \text{or} \quad \frac{AP}{PB} = \frac{k_2}{k_2}
$$

Proceeding as before, we can show in this case that

$$
x = \frac{k_1 v_1 - k_2 v_2}{k_1 - k_2} \quad \text{y} \quad \frac{k_1 v_2 - k_2 v_2}{k_1 - k_2}
$$

Thus *P* is said to divide the line segment *AB* in ratio *k₁*, *k₂*, **internally** or **externally** according as *P* lies between *AB* or beyond *AB*.

(iii) If *k₁* = *k₂* = 1:1, then *P* becomes **midpoint** of *AB* and coordinates of *P* are

$$
x = \frac{x_1 + x_2}{2}, \quad \text{y} \quad \frac{y_1 - y_2}{2}
$$

(iv) The above theorem is valid in whichever quadrant *A* and *B* lie.

**Example 1:** Find the coordinates of the point that divides the join of *A* (−6, 3) and *B* (5, −2) in the ratio 2 : 3.

(i) internally

(ii) externally

**Solution:** (i) Here *k₁* = 2, *k₂* = 3, *x₁* = 6, *x₂* = 5.

By the formula, we have

$$
x = \frac{2 \times 5 + 3 \times (-6)}{2 + 3} \quad \text{or} \quad \frac{-6}{5} \quad \text{and} \quad y = \frac{2(-2) + 3(3)}{2 + 3} \quad 1
$$

Coordinates of the required point are (−8, 5, 1)

(ii) In this case

$$
x = \frac{2 \times 5 - 3 \times (-6)}{2 - 3} \quad \text{or} \quad y = \frac{2(-2) - 3(3)}{2 + 3} \quad 13
$$

Thus the required point has coordinates (−28, 13)

#### **Theorem:**

The centroid of a *ΔABC* is a point that divides each median in the ratio 2 : 1. Using this show that medians of a triangle are concurrent.

**Proof:** Let the vertices of a *ΔABC* have coordinates as shown in the figure.

Midpoint of *BC* is *D* (x, y, z, x + y, z).

Let *G* (x, y) be the centroid of the *Δ*. Then *G* divides *AD* in the ratio 2 : 1. Therefore

$$
\frac{2 \cdot \frac{x_1 + x_2}{2}}{2 + 1} \quad \text{or} \quad \frac{x_1 + x_2 + x_3}{2 + 1}
$$

Similarly,

$$
y = \frac{y_1 + y_2 + y_3}{2 + 1} \quad \text{or} \quad \frac{y_1 + y_2 + y_3}{2 + 1}
$$

In the same way, we can show that coordinate of the point that divides *BE* and *CF* each in the ratio 2 : 1 are (x, y, z, x + y, z).

Thus (x, y) lies on each median and so the medians of the *ΔABC* are concurrent.

**Theorem:** Bisectors of angles of a triangle are concurrent.

**Proof:** Let the coordinates of the vertices of a triangle be as shown in the figure.

Suppose |*BC*| = *a*, |*CA*| = *b* and |*AB*| = *c*.

Let the bisector of *LA* meet *BC* at *D*. Then *D* divides *BC* in the ratio *c* : *b*. Therefore

coordinates of $D$ are $\left(\frac{c x_{1}+b x_{2}}{b+c} \cdot \frac{c y_{1}+b y_{2}}{b+c}\right)$
The bisector of $\angle B$ meets $A C$ at $I$ and $I$ divides $A D$ in the ratio $c:|B D|$
Now $\frac{|B D|}{|D C|}=\frac{c}{b}$ or $\frac{|D C|}{|B D|} \cdot \frac{b}{c}$
or $\frac{|D C|+|B D|}{|B D|}=\frac{b+c}{c}$
or $\frac{a}{|B D|}=\frac{b+c}{c}$ or $|B D| \cdot \frac{a c}{b+c}$
Thus $I$ divides $A D$ in the ratio $c: \frac{a c}{b+c}$ or in the ratio $b+c: a$ Coordinates of $I$ are

$$
\left(\frac{(b+c) \frac{b x_{2}+c x_{1}}{b+c}+a x_{1}}{a+b+c} \cdot \frac{(b+c) \frac{b y_{2}+c y_{1}}{b+c}+a y_{1}}{a+b+c}\right)
$$

i.e., $\quad\left(\frac{a x_{1}+b x_{2}+c x_{1}}{a+b+c} \cdot \frac{a y_{1}+b y_{2}+c y_{2}}{a+b+c}\right)$

The symmetry of these coordinates shows that the bisector of $\angle C$ will also pass through this point.

Thus the angle bisectors of a triangle are concurrent.

## EXERCISE 4.1

1. Describe the location in the plane of the point $P(x, y)$ for which
(i) $x>0$
(ii) $x>0$ and $y>0$
(iii) $x=0$
(iv) $y=0$
(v) $x<0$ and $y \geq 0$
(vi) $x=y$
(vii) $|x|=|y|$
(viii) $|x| \geq 3$
(ix) $x>2$ and $y=2$
(x) $x$ and $y$ have opposite signs.
version: 1.1
2. Find in each of the following:
(i) the distance between the two given points
(ii) midpoint of the line segment joining the two points
(a) $A(3,1) ; B(-2,-4)$
(b) $A(-8,3) ; B(2,-1)$
(c) $A\left(-\sqrt{5},-\frac{1}{3}\right) ; B(-3 \sqrt{5}, 5)$
3. Which of the following points are at a distance of 15 units from the origin?
(a) $(\sqrt{176}, 7)$
(b) $(10,-10)$
(c) $(1,15)$
(d) $\left(\frac{15}{2}, \frac{15}{2}\right)$
4. Show that
(i) the points $A(0,2), B(\sqrt{3}, 1)$ and $C(0,-2)$ are vertices of a right triangle.
(ii) the points $A(3,1), B(-2,-3)$ and $C(2,2)$ are vertices of an isosceles triangle.
(iii) the points $A(5,2), B(-2,3), C(-3,-4)$ and $D(4,-5)$ are vertices of a parallelogram. Is the parallelogram a square?
5. The midpoints of the sides of a triangle are $(1,-1),(-4,-3)$ and $(-1,1)$. Find coordinates of the vertices of the triangle.
6. Find $h$ such that the points $A(\sqrt{3},-1), B(0,2)$ and $C(h,-2)$ are vertices of a right triangle with right angle at the vertex $A$.
7. Find $h$ such that $A(-1, k), B(3,2)$ and $C(7,3)$ are collinear.
8. The points $A(-5,-2)$ and $B(5,-4)$ are ends of a diameter of a circle. Find the centre and radius of the circle.
9. Find $k$ such that the points $A(k, 1), B(2,7)$ and $C(-6,-7)$ are vertices of a right triangle with right angle at the vertex $A$.
10. A quadrilateral has the points $A(9,3), B(-7,7), C(-3,-7)$ and $D(5,-5)$ as its vertices. Find the midpoints of its sides. Show that the figure formed by joining the midpoints consecutively is a parallelogram.

11. Find *h* such that the quadrilateral with vertices *A* (–3, 0), *B* (1, –2), *C* (5, 0) and *D* (1, *h*) is parallelogram. Is it a square?
12. If two vertices of an equilateral triangle are *A* (–3, 0) and *B* (3, 0), find the third vertex. How many of these triangles are possible?
13. Find the points trisecting the join of *A* (–1, 4) and *B* (6, 2).
14. Find the point three-fifth of the way along the line segment from *A* (–5, 8) to *B* (5, 3).
15. Find the point *P* on the join of *A* (1, 4) and *B* (5, 6) that is twice as far from *A* as *B* is from *A* and lies
    - (i) on the same side of *A* as *B* does.
    - (ii) on the opposite side of *A* as *B* does.
16. Find the point which is equidistant from the points *A* (5, 3), *B* (–2, 2) and *C* (4, 2). What is the radius of the circumcircle of the ∆ABC?
17. The points (4, –2), (–2, 4) and (5, 5) are the vertices of a triangle. Find in-centre of the triangle.
18. Find the points that divide the line segment joining *A*(*x*<sub>*1*</sub>, *y*<sub>*1*</sub>) and *B*(*x*<sub>*2*</sub>, *y*<sub>*2*</sub>) into four equal parts.

## 4.2 TRANSLATION AND ROTATION OF AXES

### *Translation of Axes*

Let *xy*-coordinate system be given and *O'* (*h, k*) be any point in the plane. Through *O'* draw two mutually perpendicular lines *OX*, *OY* such that *OX* is parallel to *Ox*. The new axes *OX* and *OY* are called **translations** of the *Ox* – and *Oy* – axes through the point *O'*. In translation of axes, origin is shifted to another point in the plane but the axes remain parallel to the old axes.

Let *P* be a point with coordinates (*x, y*) referred to *xy*-coordinate system and the axes be translated through the point *O'*(*h, k*) and *OX*, *OY* be the new axes. If *P* has coordinates (*X, Y*) referred to the new axes, then we need to find *X, Y* in terms of *x, y*.

Draw *PM* and *O' N* perpendiculars to *Ox*. From the figure, we have

*OM* = *x*, *MP* = *y*, *ON* = *h*, *NO'* = *k* = *MM*<sup>+</sup>

Now *X* = *O'M'* = *NM* = *OM* – *OM* – *ON* = *x* – *h*

Similarly, *Y* = *M'P* = *MP* – *MM'* = *y* *k*

Thus the coordinates of *P* referred to *XY*-system are (*x* – *h*, *y* – *k*)

i.e. *X* = *x* – *h*

*Y* = *y* – *k*

Moreover, *x* = *X* + *h*, + *y* = *Y* *k*.

**Example 1:** The coordinates of a point *P* are (–6, 9). The axes are translated through the point *O'* (–3, 2). Find the coordinates of *P* referred to the new axes.

**Solution.** Here *h* = 3*x* *k* 2

Coordinates of *P* referred to the new axes are (*X, Y*) given by

*X* = –6 – (–3) = –3 and *Y* = 9 – 2 = 7

Thus *P* (*X, Y*) = *P* (–3, 7).

**Example 2:** The *xy*-coordinate axes are translated through the point *O'* (4, 6). The coordinates of the point *P* are (2, –3) referred to the new axes. Find the coordinates of *P* referred to the original axes.

**Solution:** Here *X* = –2, *Y* = 3, *h* = 4, *k* = 6.

We have *x* = *X* + *h* = 4 + 2 = 6

*y* = *Y* + *k* = –3 + 6 = 3

Thus required coordinates are *P* (6, 3).

### *Rotation of Axes*

Let *xy*-coordinate system be given. We rotate *Ox* and *Oy* about the origin through an angle *θ*(0 < *θ* < 90˚) so that the new axes are *OX* and *OY* as shown in the figure. Let a point *P* have coordinates (*x, y*) referred to the *xy*-system of

coordinates. Suppose $P$ has coordinates $(X, Y)$ referred to the $X Y$-coordinate system. We have to find $X, Y$ in terms of the given coordinates $x, y$. Let $\alpha$ be measure of the angle that $O P$ makes with $O$.

From $P$, draw $P M$ perpendicular to $O x$ and $P M^{\prime}$ perpendicular to $O X$. Let $|O P|=r$. From the right triangle $O P M^{\prime}$, we have

$$
\left.\begin{array}{l}
O M^{\prime}=X=r \cos (\alpha-\theta) \\
M^{\prime} P=Y=r \sin (\alpha-\theta)
\end{array}\right]
$$

Also from the $\triangle O P M$, we have

$$
x=r \cos \alpha, \quad y=r \sin \alpha
$$

System of equations (1) may be re-written as:

$$
\left.\begin{array}{l}
X=r \cos \alpha \cos \theta \quad r \sin \alpha \sin \theta \\
Y=r \sin \alpha \cos \theta \quad r \cos \alpha \sin \theta
\end{array}\right\}
$$

Substituting from (2) into the above equations, we have

$$
\left.\begin{array}{l}
X=x \cos \theta+y \sin \theta \\
Y=y \cos \theta-x \sin \theta
\end{array}\right\}
$$

i.e., $(X, Y)=(x \cos \theta \quad y \sin \theta, \min \theta \quad y \cos \theta)$
are the coordinates of $P$ referred to the new axes $O X$ and $O Y$.
Example 3: The $x y$-coordinate axes are rotated about the origin through an angle of $30^{\circ}$. If the $x y$-coordinates of a point are $(5,7)$, find its $X Y$-coordinates, where $O X$ and $O Y$ are the axes obtained after rotation.

Solution. Let $(X, Y)$ be the coordinates of $P$ referred to the $X Y$-axes. Here $\theta=30^{\circ}$.
From equations (3) above, we have

$$
\begin{aligned}
& X=5 \cos 30^{\circ}+7 \sin 30^{\circ} \text { and } \quad \forall=5 \sin 30^{\circ} 7 \cos 30^{\circ} \\
\text { or } & X=\frac{5 \sqrt{3}}{2}, \frac{7}{2}=\text { and } \quad Y=\frac{-5}{2}, \frac{7 \sqrt{3}}{2}
\end{aligned}
$$

i.e., $(X, Y) \quad\left(\frac{5 \sqrt{3}+7}{2}, \frac{-5+7 \sqrt{3}}{2}\right)$
are the required coordinates.

Example 4: $\quad$ The $x y$-axes are rotated about the origin through an angle of arctan $\frac{4}{3}$ lying in the first quadrant. The coordinates of a point $P$ referred to the new axes $O X$ and $O Y$ are $P(-1,-7)$. Find the coordinates of $P$ referred to the $x y$-coordinate system.

Solution. Let $P(x, y)$ be the coordinates of $P$ referred to the $x y$-coordinate system. Angle of rotation is given by arctan $\theta=\frac{4}{3}$. Therefore, $\sin \theta=\frac{4}{5}, \cos \theta=\frac{3}{5}$.

From equations (3) above, we have

$$
\begin{aligned}
& X=x \cos \theta+y \sin \theta \text { and } \quad \forall=x \sin \theta \quad y \cos \theta \\
\text { or } & -1=\frac{3}{5} x+\frac{4}{5} y \text { and }-7=-\frac{4}{5} x+\frac{3}{5} y \\
\text { or } & 3 x+4 y+5=0 \text { and }-4 x+3 y+35=0
\end{aligned}
$$

Solving these equations, we have

$$
\frac{x}{125}=-\frac{y}{-125}=\frac{1}{25} \quad \Rightarrow x=5, y=-5
$$

Thus coordinates of $P$ referred to the $x y$-system are $(5,-5)$.

## EXERCISE 4.2

1. The two points $P$ and $O^{\prime}$ are given in $x y$-coordinate system. Find the $X Y$-coordinates of $P$ reffered to the translated axes $O^{\prime} X$ and $O^{\prime} Y$.
(i) $P(3,2) ; O^{\prime}(1,3)$
(ii) $P(-2,6) ; O^{\prime}(-3,2)$
(iii) $P(-6,-8) ; O^{\prime}(-4,-6)$
(iv) $P\left(\frac{3}{2}, \frac{5}{2}\right) ; O^{\prime}\left(-\frac{1}{2}, \frac{7}{2}\right)$

2. The $x y$-coordinate axes are translated through the point whose coordinates are given in $x y$-coordinate system. The coordinates of $P$ are given in the $X Y$-coordinate system. Find the coordinates of $P$ in $x y$-coordinate system.
(i) $P(8,10) ; O^{\prime}(3,4)$
(ii) $P(-5,-3) ; O^{\prime}(-2,-6)$
(iii) $P\left(-\frac{3}{4},-\frac{7}{6}\right) ; O^{\prime}\left(\frac{1}{4},-\frac{1}{6}\right)$
(iv) $P(4,-3) ; O^{\prime}(-2,3)$
3. The $x y$-coordinate axes are rotated about the origin through the indicated angle. The new axes are $O X$ and $O Y$. Find the $X Y$-coordinates of the point $P$ with the given $x y$-coordinates.
(i) $P(5,3) ; \theta=45^{\circ}$
(ii) $P(3,-7) ; \quad \theta=30^{\circ}$
(iii) $P(11,-15) ; \theta=60^{\circ}$
(iv) $P(15,10): \theta=\arctan \frac{1}{3}$
4. The $x y$-coordinate axes are rotated about the origin through the indicated angle and the new axes are $O X$ and $O Y$.
Find the $x y$-coordinates of $P$ with the given $X Y$-coordinates.
(i) $P(-5,3) ; \quad \theta=30^{\circ}$
(ii) $P(-7 \sqrt{2}, 5 \sqrt{2}) ; \theta=45^{\circ}$

### 4.3 EQUATIONS OF STRAIGHT LINES

Inclination of a Line: The angle $\alpha\left(0^{\circ}<\alpha<180^{\circ}\right)$ measured counterclockwise from positive $x$-axis to a non-horizontal straight line $l$ is called the inclination of $l$.
Observe that the angle $\alpha$ in the different positions of the line $l$ is $\alpha_{1} 0^{\circ}$ and $90^{\circ}$ respectively.

## (i) If $l$ is parallel to $x$-axis, then $\alpha=0^{\circ}$
(ii) If $l$ is parallel to $y$-axis, then $\alpha=90^{\circ}$

Slope or gradient of a line: When we walk on an inclined plane, we cover horizontal distance (run) as well as vertical distance (rise) at the same time.
It is harder to climb a steeper inclined plane. The measure of steepness (ratio of rise to the run) is termed as slope or gradient of the inclined path and is denoted by $m$.
$$
m=\frac{r i s e}{r u n}=\frac{y}{x}=\tan \alpha
$$

In analytical geometry, slope or gradient $\boldsymbol{m}$ of a non-vertical straight line with $\alpha$ as its inclination is defined by: $m: \tan \alpha$

If $l$ is horizontal its slope is zero and if $l$ is vertical then its slope is undefined.
If $0<\alpha<90^{\circ}, \mathrm{m}$ is positive and if $90^{\circ}<\alpha<180^{\circ}$, then $m$ is negative

### 4.3.1 Slope or Gradient of a Straight Line Joining Two Points

If a non-vertical line $l$ with inclination $\alpha$ passes through two points $P\left(x_{1}, y_{1}\right)$ and $Q\left(x_{1}, y_{1}\right)$, then the slope or gradient $m$ of $l$ is given by $m=\frac{y_{1}-y_{1}}{x_{1}-x_{1}}=\tan \alpha$
Proof: Let $m$ be the slope of the line $l$.
Draw perpendiculars $P M$ and $Q M^{\prime}$ on $x$-axis and a perpendicular $P R$ on $Q M^{\prime}$
Then $\angle R P Q=\alpha, m \overline{P R}=x_{1}-x_{1}$ and $m \overline{Q R}=y_{1}-y_{1}$
The slope or gradient of $l$ is defined as: $m=\tan \alpha=\frac{y_{1}-y_{1}}{x_{1}-x_{1}}$

**Case (i).** When 0 < α < π/2

In the right triangle *PRQ*, we have

$$
m = \tan \alpha = \frac{y_2 - y_1}{x_2 - x_1}
$$

**Case (ii)** When π/2 < α < π

In the right triangle *PRQ*

$$
\tan (\pi - \alpha) = \frac{y_2 - y_1}{x_2 - x_1}
$$

or

$$
-\tan \alpha = \frac{y_2 - y_1}{x_2 - x_1}
$$

or

$$
\tan \alpha = \frac{y_2 - y_1}{x_2 - x_1}
$$

or

$$
m = \frac{y_2 - y_1}{x_2 - x_1}
$$

Thus if *P(x1, y1)* and *Q(x2, y2)* are two points on a line, then slope of *PQ* is given by:

$$
m = \frac{y_2 - y_1}{x_2 - x_1} \quad \text{or} \quad m \quad \frac{y_2 - y_2}{x_2 - x_2}
$$

**Note:**

- (i) $m \neq \frac{y_2 - y_1}{x_2 - x_1}$ and $m \neq \frac{y_2 - y_2}{x_2 - x_1}$.
- (ii) $f$ is horizontal, iff $m = 0$ (∀ α = 0).
- (iii) $f$ is vertical, iff $m$ is not defined (∀ α = 90).
- (iv) If slope of *AB* = slope of *BC*, then the points *A*, *B* and *C* are collinear.

**Theorem:** The two lines *l1* and *l2* with respective slopes *m1* and *m2* are

- (i) parallel iff *m1 = m2*.
- (ii) perpendicular iff *m1 =* 1/*m2*

or

$$
m_1 m_2 + l = 0
$$

**Example 1:** Show that the points *A*(–3, 6), *B*(3, 2) and *C*(6, 0) are collinear.

**Solution:** We know that the points *A*, *B* and *C* are collinear if the line *AB* and *BC* have the same slopes. Here Slope of

$$
AB = \frac{2 - 6}{3 - (-3)} = \frac{-4}{3 + 3} = \frac{-4}{6} = \frac{-2}{3} \quad \text{and} \quad \text{slope of } BC = \frac{0 - 2}{6 - 3} = \frac{-2}{3}
$$

Slope of *AB* = Slope of *BC*

Thus *A*, *B* and *C* are collinear.

**Example 2:** Show that the triangle with vertices *A*(1, 1), *B*(4, 5) and *C*(12, –1) is a right triangle.

**Solution:** Slope of *AB* = *m1* = 5/1 + 4/3

$$
\text{and Slope of } BC = m_2 = \frac{-1 - 5}{12 - 4} = \frac{-6}{8} = \frac{-3}{4}
$$

Since *m1m2* = (4/3) - 3/4 = 1, therefore, *AB* ⊥ *BC*

So Δ*ABC* is a right triangle.

**4. Introduction to Analytic Geometry** *eLearn.Punjab*

**4.1 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.2 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.3 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.4 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.5 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.6 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.7 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.8 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.9 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.10 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.11 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.12 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.13 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.14 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.15 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.16 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.17 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.18 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.19 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.20 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.21 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.22 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.23 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.24 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.25 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.26 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.27 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.28 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.29 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.30 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.31 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.32 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.33 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.34 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.35 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.36 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.37 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.38 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.39 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.49 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.50 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.51 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.52 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.53 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.54 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.55 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.56 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.57 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.58 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.59 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.60 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.61 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.62 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.63 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.64 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.65 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.66 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.67 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.68 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.69 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.70 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.71 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.72 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.73 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.74 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.75 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.76 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.77 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.78 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.79 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.80 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.81 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.82 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.83 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.84 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.85 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.86 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.87 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.88 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.89 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.90 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.91 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.92 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.93 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.94 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.95 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.96 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.97 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.98 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.99 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.10 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.11 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.12 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.13 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.14 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.15 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.16 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.17 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.18 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.19 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.20 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.21 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.22 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.23 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.24 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.25 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.26 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.27 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.28 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.29 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.30 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.31 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.32 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.33 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.34 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.35 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.36 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.37 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.38 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.39 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.40 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.41 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.42 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.43 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.44 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.45 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.46 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.47 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.48 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.49 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.50 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.51 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.52 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.53 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.54 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.55 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.56 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.57 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.58 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.59 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.60 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.61 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.62 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.63 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.64 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.65 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.66 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.67 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.68 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.69 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.70 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.71 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.72 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.73 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.74 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.75 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.76 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.77 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.78 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.79 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.80 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.81 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.82 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.83 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.84 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.85 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.86 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.87 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.88 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.89 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.90 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.91 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.92 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.93 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.94 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.95 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.96 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.97 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.98 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.99 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.10 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.11 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.12 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.13 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.14 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.15 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.16 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.17 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.18 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.19 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.20 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.21 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.22 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.23 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.24 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.25 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.26 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.27 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.28 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.29 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.30 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.31 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.32 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.33 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.34 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.35 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.36 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.37 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.38 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.39 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.40 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.41 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.42 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.43 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.44 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.45 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.46 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.47 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.48 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.49 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.50 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.51 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.52 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.53 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.54 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.55 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.56 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.57 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.58 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.59 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.60 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.61 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.62 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.63 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.64 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.65 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.66 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.67 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.68 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.69 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.70 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.71 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.72 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.73 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.74 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.75 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.76 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.77 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.78 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.79 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.80 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.81 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.82 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.83 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.84 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.85 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.86 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.87 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.88 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.89 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.90 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.91 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.92 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.93 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.94 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.95 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.96 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.97 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.98 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.99 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.10 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.11 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.12 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.13 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.14 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.15 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.16 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.17 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.18 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.19 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.10 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.11 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.12 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.13 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.14 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.15 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.16 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.17 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.18 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.19 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.10 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.11 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.12 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.13 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.14 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.15 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.16 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.17 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.18 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.19 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.10 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.11 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.12 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.13 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.14 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.15 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.16 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.17 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.18 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.19 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.10 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.11 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.12 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.13 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.14 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.15 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.16 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.17 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.18 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.19 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.10 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.11 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.12 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.13 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.14 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.15 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.16 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.17 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.18 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.19 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.20 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.21 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.22 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.23 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.24 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.25 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.26 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.27 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.28 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.29 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.30 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.31 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.32 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.33 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.34 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.35 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.36 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.37 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.38 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.39 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.40 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.41 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.42 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.43 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.44 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.45 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.46 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.47 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.48 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.49 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.50 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.51 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.52 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.53 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.54 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.55 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.56 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.57 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.58 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.59 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.60 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.61 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.62 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.63 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.64 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.65 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.66 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.67 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.68 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.69 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.70 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.71 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.72 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.73 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.74 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.75 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.76 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.77 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.78 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.79 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.80 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.81 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.82 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.83 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.84 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.85 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.86 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.87 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.88 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.89 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.90 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.91 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.92 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.93 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.94 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.95 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.96 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.97 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.98 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.99 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.99 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.10 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.11 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.12 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.13 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.14 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.15 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.16 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.17 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.18 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.19 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.10 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.11 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.12 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.13 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.14 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.15 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.16 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.17 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.18 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.19 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.10 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.11 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.12 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.13 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.14 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.15 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.16 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.17 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.18 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.19 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.10 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.11 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.12 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.13 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.14 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.15 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.16 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.17 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.18 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.19 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.10 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.11 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.12 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.13 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.14 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.15 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.16 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.17 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.18 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.19 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.10 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.11 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.12 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.13 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.14 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.15 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.16 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.17 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.18 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.19 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.10 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.12 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.13 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.14 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.15 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.16 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.17 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.18 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.19 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.10 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.12 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.13 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.14 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.15 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.16 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.17 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.18 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.19 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.10 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.12 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.13 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.14 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.15 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.16 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.17 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.18 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.19 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.10 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.12 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.13 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.14 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.15 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.16 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.17 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.18 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.19 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.10 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.12 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.13 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.14 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.15 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.16 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.17 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.18 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.19 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.10 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.12 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.13 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.14 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.15 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.16 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.17 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.18 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.19 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.10 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.110 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.120 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.13 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.14 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.15 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.16 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.17 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.18 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.19 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.10 Introduction to Analytic Geometry** *eLearn.Punjab*

**4.110 Introduction to Analyticategory** *eLearn.Punjab*

**4.120 Introduction to Analyticategory** *eLearn.Punjab*

**4.13 Introduction to Analyticategory** *eLearn.Punjab*

**4.14 Introduction to Analyticategory** *eLearn.Punjab*

**4.15 Introduction to Analyticategory** *eLearn.Punjab*

**4.16 Introduction to Analyticategory** *eLearn.Punjab*

**4.17 Introduction to Analyticategory** *eLearn.Punjab*

**4.18 Introduction to Analyticategory** *eLearn.Punjab*

**4.19 Introduction to Analyticategory** *eLearn.Punjab*

**4.10 Introduction to Analyticategory** *eLearn.Punjab*

**4.14 Introduction to Analyticategory** *eLearn.Punjab*

**4.15 Introduction to Analyticategory** *eLearn.Punjab*

**4.16 Introduction to Analyticategory** *eLearn.Punjab*

**4.17 Introduction to Analyticategory** *eLearn.Punjab*

**4.18 Introduction to Analyticategory** *eLearn.Punjab*

**4.19 Introduction to Analyticategory** *eLearn.Punjab*

**4.10 Introduction to Analyticategory** *eLearn.Punjab*

**4.110 Introduction to Analyticategory** *eLearn.Punjab*

**4.120 Introduction to Analyticategory** *eLearn.Punjab*

**4.13 Introduction to Analyticategory** *eLearn.Punjab*

**4.14 Introduction to Analyticategory** *eLearn.Punjab*

**4.15 Introduction to Analyticategory** *eLearn.Punjab*

**4.16 Introduction to Analyticategory** *eLearn.Punjab*

**4.17 Introduction to Analyticategory** *eLearn.Punjab*

**4.18 Introduction to Analyticategory** *eLearn.Punjab*

**4.19 Introduction to Analyticategory** *eLearn.Punjab*

**4.10 Introduction to Analyticategory** *eLearn.Punjab*

**4.110 Introduction to Analyticategory** *eLearn.Punjab*

**4.120 Introduction to Analyticategory** *eLearn.Punjab*

**4.13 Introduction to Analyticategory** *eLearn.Punjab*

**4.14 Introduction to Analyticategory** *eLearn.Punjab*

**4.15 Introduction to Analyticategory** *eLearn.Punjab*

**4.16 Introduction to Analyticategory** *eLearn.Punjab*

**4.17 Introduction to Analyticategory** *eLearn.Punjab*

**4.18 Introduction to Analyticategory** *eLearn.Punjab*

**4.19 Introduction to Analyticategory** *eLearn.Punjab*

**4.10 Introduction to Analyticategory** *eLearn.Punjab*

**4.14 Introduction to Analyticocracy** *eLearn.Punjab*

**4.15 Introduction to Analyticocracy** *eLearn.Punjab*

**4.16 Introduction to Analyticocracy** *eLearn.Punjab*

**4.17 Introduction to Analyticocracy** *eLearn.Punjab*

**4.18 Introduction to Analyticocracy** *eLearn.Punjab*

**4.19 Introduction to Analyticocracy** *eLearn.Punjab*

**4.10 Introduction to Analyticocracy** *eLearn.Punjab*

**4.14 Introduction to Analyticocracy** *eLearn.Punjab*

**4.15 Introduction to Analyticocracy** *eLearn.Punjab*

**4.16 Introduction to Analyticocracy** *eLearn.Punjab*

**4.17 Introduction to Analyticocracy** *eLearn.Punjab*

**4.18 Introduction to Analyticocracy** *eLearn.Punjab*

**4.19 Introduction to Analyticocracy** *eLearn.Punjab*

**4.10 Introduction to Analyticocracy** *eLearn.Punjab*

**4.110 Introduction to Analyticocracy** *eLearn.Punjab*

**4.120 Introduction to Analyticocracy** *eLearn.Punjab*

**4.13 Introduction to Analyticocracy** *eLearn.Punjab*

**4.14 Introduction to Analyticocracy** *eLearn.Punjab*

**4.15 Introduction to Analyticocracy** *eLearn.Punjab*

**4.16 Introduction to Analyticocracy** *eLearn.Punjab*

**4.17 Introduction to Analyticocracy** *eLearn.Punjab*

**4.18 Introduction to Analyticocracy** *eLearn.Punjab*

**4.19 Introduction to Analyticocracy** *eLearn.Punjab*

**4.10 Introduction to Analyticocracy** *eLearn.Punjab*

**4.14 Introduction to Analyticocracy** *eLearn.Punjab*

**4.15 Introduction to Analyticocracy** *eLearn.Punjab*

**4.16 Introduction to Analyticocracy** *eLearn.Punjab*

**4.17 Introduction to Analyticocracy** *eLearn.Punjab*

**4.18 Introduction to Analyticocracy** *eLearn.Punjab*

**4.19 Introduction to Analyticocracy** *eLearn.Punjab*

**4.10 Introduction to Analyticocracy** *eLearn.Punjab*

**4.10 Introduction to Analyticocracy** *eLearn.Punjab*

**4.16 Introduction to Analyticocracy** *eLearn.Punjab*

**4.17 Introduction to Analyticocracy** *eLearn.Punjab*

**4.18 Introduction to Analyticocracy** *eLearn.Punjab*

**4.19 Introduction to Analyticocracy** *eLearn.Punjab*

**4.10 Introduction to Analyticocracy** *eLearn.Punjab*

**4.10 Introduction to Analyticocracy** *eLearn.Punjab*

**4.17 Introduction to Analyticocracy** *eLearn.Punjab*

**4.19 Introduction to Analyticocracy** *eLearn.Punjab*

**4.10 Introduction to Analyticocracy** *eLearn.Punjab*

**4.10 Introduction to Analyticocracy** *eLearn.Punjab*

**4.19 Introduction to Analyticocracy** *eLearn.Punjab*

**4.19 Introduction to Analyticocracy** *eLearn.Punjab*

**4.19 Introduction to Analyticocracy** *eLearn.Punjab*

**4.19 Introduction to Analyticocracy** *eLearn.Punjab*

**4.19 Introduction to Analyticocracy** *eLearn.Punjab*

**4.19 Introduction to Analyticocracy** *eLearn.Punjab*

**4.19 Introduction to Analyticocracy** *eLearn.Punjab*

**4.19 Introduction to Analyticocracy** *eLearn.Punjab*

**4.19 Introduction to Analyticocracy** *eLearn.Punjab*

**4.19 Introduction to Analyticocracy** *eLearn.Punjab*

**4.19 Introduction to Analyticocracy** *eLearn.Punjab*

**4.19 Introduction to Analyticocracy** *eLearn.Punjab*

**4.19 Introduction to Analyticocracy** *eLearn.Punjab*

**4.19 Introduction to Analyticocracy** *eLearn.Punjab*

**4.19 Introduction to Analyticocracy** *eLearn.Punjab*

**4.19 Introduction to Analyticocracy** *eLearn.Punjab*

**4.19 Introduction to Analyticocracy** *eLearn.Punjab*

**4.19 Introduction to Analyticocracy** *eLearn.Punjab*

**4.19 Introduction to Analyticocracy** *eLearn.Punjab*

**4.19 Introduction to Analyticocracy** *eLearn.Punjab*

**4.19 Introduction to Analyticocracy** *eLearn.Punjab*

**4.19 Introduction to Analyticocracy** *eLearn.Punjab*

**4.19 Introduction to Analyticocracy** *eLearn.Punjab*

**4.19 Introduction to Analyticocracy** *eLearn.Punjab*

**4.19 Introduction to Analyticocracy** *eLearn.Punjab*

**4.19 Introduction to Analyticocracy** *eLearn.Punjab*

**4.19 Introduction to Analyticocracy** *eLearn.Punjab*

**4.19 Introduction to Analyticocracy** *eLearn.Punjab*

**4.19 Introduction to Analyticocracy** *eLearn.Punjab*

**4.19 Introduction to Analyticocracy** *eLearn.Punjab*

**4.19 Introduction to Analyticocracy** *eLearn.Punjab*

All the points on the line *I* parallel to *x*-axis remain at a constant distance (say *a*) from *x*-axis. Therefore, each point on the line has its distance from *x*-axis equal to *a*, which is its *y*-coordinate (ordinate). So, all the points on this line satisfy the equation: *y* = *a*

|  Note: | (i) | If *a* > 0, then the line *I* is above the *x*-axis.  |
| --- | --- | --- |
|   | (ii) | If *a* < 0, then the line *I* is below the *x*-axis.  |
|   | (iii) | If *a* = 0, then the line *I* becomes the *x*-axis.  |
|   |  | Thus the equation of *x*-axis is *y* = 0  |

### 4.3.2 Equation of a Straight Line Parallel to the *x*-axis (or perpendicular to the *y*-axis)

### 4.3.4 Derivation of Standard Forms of Equations of Straight Lines

#### Intercepts:

- If a line intersects *x*-axis at (*a*, 0), then *a* is called *x*-intercept of the line.
- If a line intersects *y*-axis at (0, *b*), then *b* is called *y*-intercept of the line.

#### 1. Slope-Intercept form of Equation of a Straight Line:

**Theorem:** Equation of a non-vertical straight line with slope *m* and *y*-intercept *c* is given by:

$$ y = mx + c $$

**Proof:** Let *P*(*x*, *y*) be an arbitrary point of the straight line *I* with slope *m* and *y*-intercept *c*. As *C*(0, *c*) and *P*(*x*, *y*) lie on the line, so the slope of the line is:

$$ m = \frac{y - c}{x - 0} \quad \text{or} \quad y - c = mx \quad \text{and} \quad y = mx + c $$

is an equation of *I*.

The equation of the line for which

$$ c = 0 \text{ is } \qquad y = mc $$

In this case the line passes through the origin.

**Example 1:** Find an equation of the straight line if

- (a) its slope is 2 and *y*-intercept is 5
- (b) it is perpendicular to a line with slope –6 and its *y*-intercept is $$\frac{4}{3}$$

**Solution:** (a) The slope and *y*-intercept of the line are respectively:

$$ m = 2 \qquad \text{and} \qquad c = 5 $$

Thus *y* = 2*x* + 5 (Slope-intercept form: *y* = *mx* + *c*)

is the required equation.

- (b) The slope of the given line is

$$ m_i = -6 $$

The slope of the required line is:

$$ m_i = \frac{1}{m_i} \quad \frac{1}{6} $$

The slope and *y*-intercept of the required line are respectively:

$$ m = \frac{1}{6} \qquad \text{(slope of } \perp \text{ line is } -6) \quad \text{and} \qquad c = \frac{4}{3} $$

Thus *y* = $$\frac{1}{6}(*)$$ or *6y* *x* 8

is the required equation.

#### 2. Point-slope Form of Equation of a Straight Line:

**Theorem:** Equation of a non-vertical straight line *I* with slope *m* and passing through a point *Q*(*x*, *y*) is

$$
y-y_1 = m(x - x_1)
$$

**Proof:** Let \( P(x, y) \) be an arbitrary point of the straight line with slope \( m \) and passing through \( Q(x_1, y_1) \).

As \( Q(x_1, y_1) \) and \( P(x, y) \) both lie on the line, so the slope of the line is

$$
m = \frac{y - y_1}{x - x_1} \text{ or } y - y_1 = m(x - x_1)
$$

which is an equation of the straight line passing through \( x_1, y_1 \) with slope \( m \).

### 3. Symmetric Form of Equation of a Straight Line:

We have \( \frac{y - y_1}{x - x_1} = \tan \alpha \), where \( \alpha \) is the inclination of the line.

$$
\lim_{m \to \infty} \frac{x - x_1}{\cos \alpha} = \frac{y - y_1}{\sin \alpha} = r(\sin \alpha)
$$

This is called **symmetric** form of equation of the line.

**Example 2:** Write down an equation of the straight line passing through \( (5, 1) \) and parallel to a line passing through the points \( (0, -1) \), \( (7, -15) \).

**Solution:** Let \( m \) be the slope of the required straight line, then

$$
m = \frac{-15 - (-1)}{7 - 0} \qquad \text{(☞ Slopes of parallel lines are equal)}
$$

$$
= -2
$$

As the point \( (5, 1) \) lies on the required line having slope -2 so, by point-slope form of equation of the straight line, we have

$$
y - (1) = -2(x - 5)
$$

or

$$
y = -2x + 11
$$

or

$$
2x + y - 11 = 0
$$

is an equation of the required line.

### 4. Two-point Form of Equation of a Straight Line:

**Theorem:** Equation of a non-vertical straight line passing through two points \( Q(x_1, y_1) \) and \( R(x_2, y_2) \) is

$$
y - y_1 = \frac{y_2 - y_1}{x_2 - x_1} (x - x_1) \text{ or } y - y_2 = \frac{y_2 - y_1}{x_2 - x_1} (x - x_2)
$$

**Proof:** Let \( P(x, y) \) be an arbitrary point of the line passing through \( Q(x_1, y_1) \) and \( R(x_2, y_2) \). So

$$
\frac{y - y_1}{x - x_1} = \frac{y - y_2}{x - x_2} = \frac{y_2 - y_1}{x_2 - x_1} \qquad (P, Q \text{ and } R \text{ are collinear points})
$$

We take

$$
\frac{y - y_1}{x - x_1} = \frac{y_2 - y_1}{x_2 - x_1}
$$

or

$$
y - y_1 = \frac{y_2 - y_1}{x_2 - x_1} (x - x_1) \text{ the required equation of the line } PQ.
$$

or

$$
(y_2 - y_1) x - (x_2 - x_1) y + (x_2 y_2 - x_2 y_1) = 0
$$

We may write this equation in determinant form as:

$$
\left| \begin{array}{ccc}
x & y & 1 \\
x_1 & y_1 & 1 \\
x_2 & y_2 & 1
\end{array} \right|
$$

**Note:** (i) If \( x_1 = x_2 \) then the slope becomes undefined. So, the line is vertical.

(ii) \( y - y_2 = \frac{y_2 - y_1}{x_2 - x_1} (x - x_1) \) can be derived similarly.

Example 3: Find an equation of line through the points $(-2,1)$ and $(6,-4)$.

Solution: Using two-points form of the equation of straight line, the required equation is

$$
\begin{aligned}
& y-1=\frac{-4-1}{6-(-2)}[x-(-2)] \\
\text { or } \quad & y-1=\frac{-5}{9}(x+2) \text { or } 5 x+8 y+2=0
\end{aligned}
$$

## 5. Intercept Form of Equation of a Straight Line:

Theorem: Equation of a line whose non-zero $x$ and $y$-intercepts are $a$ and $b$ respectively is

$$
\frac{x}{a} \cdot \frac{y}{b}=1
$$

Proof: Let $P(x, y)$ be an arbitrary point of the line whose non-zero $x$ and $y$-intercepts are $a$ and $b$ respectively. Obviously, the points $A(a, 0)$ and $B(0, b)$ lie on the required line. So, by the two-point form of the equation of line, we have

$$
\begin{aligned}
& y-0=\frac{b-0}{0-a}(x-a) \quad(P, A \text { and } B \text { are collinear }) \\
& \text { or } \quad-a y=b(x-a) \\
& \text { or } \quad b x+a y=a b \\
& \text { or } \quad \frac{x}{a}+\frac{y}{b}=1 \quad \text { (dividing by } a b \text { ) } \\
& \text { Hence the result. }
\end{aligned}
$$

Example 4: Write down an equation of the line which cuts the $x$-axis at $(2,0)$ and $y$-axis at $(0,-4)$.

Solution: As 2 and -4 are respectively $x$ and $y$-intercepts of the required line, so by two-intercepts form of equation of a straight line, we have

$$
\frac{x}{2}+\frac{y}{-4}=1-\quad \text { or }=2 x \quad y \quad 4 \quad 0
$$

which is the required equation.

Example 5: Find an equation of the line through the point $P(2,3)$ which forms an isosceles triangle with the coordinate axes in the first quadrant.

Solution: Let $O A B$ be an isosceles triangle so that the line $A B$ passes through $A=(a, 0)$ and $B(0, a)$, where $a$ is some positive real number.
Slope of $A B=\frac{a-0}{0-a}=-1$. But $A B$ passes through $P(2,3)$.
$\because \quad$ Equation of the line through $P(2,3)$ with slope -1 is

$$
y-3=-1(x-2) \text { or } \quad x+y-5=0
$$

## 6. Normal Form of Equation of a Straight Line:

Theorem: An equation of a non-vertical straight line $I$, such that length of the perpendicular from the origin to $I$ is $p$ and $\alpha$ is the inclination of this perpendicular, is

$$
x \cos \alpha+y \sin \alpha=p
$$

Proof: Let the line $I$ meet the $x$-axis and $y$-axis at the points $A$ and $B$ respectively. Let $P(x, y)$ be an arbitrary point of $A B$ and let $O R$ be perpendicular to the line $I$. Then $|O R|=p$.

From the right triangles $O R A$ and $O R B$, we have,

$$
\cos \alpha=\frac{p}{O A} \quad \text { or } \quad O A=\frac{p}{\cos \alpha}
$$

and

$$
\cos \left(90^{\circ}-\alpha\right)=\frac{p}{O B} \quad \text { or } \quad O B=\frac{p}{\sin \alpha}
$$

$$
\left[:: \cos \left(90^{\circ}-\alpha\right)=\sin \alpha\right)\right]
$$

As $O A$ and $O B$ are the $x$ and $y$-intercepts of the line $A B$, so equation of $A B$ is

$$
\frac{x}{p / \cos \alpha}+\frac{y}{p / \sin \alpha}=1 \quad \text { (Two-intercept form) }
$$

That is $x \cos \alpha+y \sin \alpha=p$ is the required equation.

Example 6: The length of perpendicular from the origin to a line is 5 units and the inclination of this perpendicular is $120^{\circ}$. Find the slope and $y$-intercept of the line.

Solution. Here $p=5, \alpha=120^{\circ}$.
Equation of the line in normal form is

$$
\begin{aligned}
& x \cos 120^{\circ}+y \sin 120^{\circ}=5 \\
& \Rightarrow \quad-\frac{1}{2} x+\frac{\sqrt{3}}{2} y=5 \\
& \Rightarrow \quad x-\sqrt{3} y+10=0
\end{aligned}
$$

To find the slope of the line, we re-write (1) as: $y=\frac{x}{\sqrt{3}}+\frac{10}{\sqrt{3}}$
which is slope-intercept form of the equation.
Here $\quad m=\frac{1}{\sqrt{3}}$ and $c=\frac{10}{\sqrt{3}}$

### 4.3.5 A Linear Equation in two Variables Represents a Straight Line

Theorem: The linear equation $a x+b y+c=0$ in two variables $x$ and $y$ represents a straight line. A linear equation in two variables $x$ and $y$ is

$$
a x+b y+c=0
$$

where $a, b$ and $c$ are constants and $a$ and $b$ are not simultaneously zero.

## 4. Introduction to Analytic Geometry

## 4.3.5 A Linear Equation in two Variables Represents a Straight Line

Theorem: The linear equation $a x+b y+c=0$ in two variables $x$ and $y$ represents a straight line. A linear equation in two variables $x$ and $y$ is

$$
a x+b y+c=0
$$

where $a, b$ and $c$ are constants and $a$ and $b$ are not simultaneously zero.

## 24

## Remember that:

The equation (I) represents a straight line and is called the general equation of a straight line.
the $y$-axis at a directed distance $-\frac{c}{a}$ from the $y$-axis.
Case II: $\quad a=0, \quad b \neq 0$
In this case equation (1) takes the form:

$$
b x+c=0 \text { or } y=-\frac{c}{b}
$$

which is an equation of the straight line parallel to $x$-axis at a directed distance $\frac{-c}{b}$ from the $x$-axis.
Case III: $\quad a \neq 0 \quad, \quad b \neq 0$
In this case equation (1) takes the form:

$$
b y=-a x-c \quad \text { or } \quad y=\frac{-a}{b} x-\frac{c}{b}=m x+c
$$

which is the slope-intercept form of the straight line with slope $\frac{-a}{b}$ and $y$-intercept $\frac{-c}{b}$.
Thus the equation $a x+b y+c=0$, always represents a straight line.

### 4.3.6 To Transform the General Linear Equation to Standard Forms

Theorem: To transform the equation $a x+b y+c=0$ in the standard form

## 1. Slope-Intercept Form.

We have

$$
b y=-a x-c \quad \text { or } \quad y=\frac{-a}{b} \times-\frac{c}{b}=m x+c \text {, where } m=\frac{-a}{b}, c=\frac{-c}{b}
$$

## 2. Point - Slope Form

We note from (1) above that slope of the line $a x+b y+c=0$ is $\frac{-a}{b}$. A point on the line is $\left(\frac{-c}{a}, 0\right)$

Equation of the line becomes $y=\frac{-a}{b}\left(x+\frac{c}{a}\right)$
which is in the point-slope form.

## 3. Symmetric Form

$$
m=\tan \alpha=\frac{-a}{b} \cdot \sin \alpha=\frac{a}{\pm \sqrt{a^{2}+b^{2}}} \cdot \cos \alpha \quad \frac{b}{\pm \sqrt{a^{2}+b^{2}}}
$$

A point on $a x+b y+c=0$ is $\left(\frac{-c}{a}, 0\right)$
Equation in the symmetric form becomes

$$
\frac{x-\left(-\frac{c}{a}\right)}{b / \pm \sqrt{a^{2}+b^{2}}}=\frac{y-0}{a / \pm \sqrt{a^{2}+b^{2}}} \quad r
$$

is the required transformed equation. Sign of the radical to be properly chosen.

## 4. Two -Point Form

We choose two arbitrary points on $a x+b y+c=0$. Two such points are $\left(\frac{-c}{a}, 0\right)$ and $\left(0, \frac{-c}{b}\right)$. Equation of the line through these points is

$$
\frac{y-0}{0+\frac{c}{b}}=\frac{x+\frac{c}{a}}{-\frac{c}{a}-0} \quad \text { i.e., } y \quad 0 \quad \frac{-a}{b}\left(x \quad \frac{c}{a}\right)
$$

## 5. Intercept Form.

$$
a x+b y=-c \quad \text { or } \quad \frac{a x}{-c}+\frac{b y}{-c}=1 \quad \text { i.e } \quad \frac{x}{-c / a} \quad \frac{y}{-c / b} \quad 1=
$$

which is an equation in two intercepts form.

## 6. Normal Form.

The equation: $a x+b y+c=0$
can be written in the normal form as:

$$
\frac{a x+b y}{\pm \sqrt{a^{2}+b^{2}}}=\frac{-c}{\pm \sqrt{a^{2}+b^{2}}}
$$

The sign of the radical to be such that the right hand side of (2) is positive.
Proof. We know that an equation of a line in normal form is

$$
x \cos \alpha+y \sin \alpha=p
$$

If (1) and (3) are identical, we must have

$$
\frac{a}{\cos \alpha}=\frac{b}{\sin \alpha}=\frac{-c}{p}
$$

i.e.,

$$
\frac{p}{-c}=\frac{\cos \alpha}{a}=\frac{\sin \alpha}{b}=\frac{\sqrt{\cos ^{2} \alpha+\sin ^{2} \alpha}}{\pm \sqrt{a^{2}+b^{2}}} \quad \frac{1}{\pm \sqrt{a^{2}+b^{2}}}
$$

Hence, $\quad \cos \alpha=\frac{a}{\pm \sqrt{a^{2}+b^{2}}}$ and $\sin \alpha \quad \frac{b}{\pm \sqrt{a^{2}+b^{2}}}$
Substituting for $\cos \alpha, \sin \alpha$ and $p$ into (3), we have

$$
\frac{a x+b y}{\pm \sqrt{a^{2}+b^{2}}}=\frac{-c}{\pm \sqrt{a^{2}+b^{2}}}
$$

Thus (1) can be reduced to the form (2) by dividing it by $\pm \sqrt{a^{2}+b^{2}}$. The sign of the radical to be chosen so that the right hand side of (2) is positive.

Example 1: Transform the equation $5 x-12 y+39=0$ into
(i) Slope intercept form.
(ii) Two-intercept form.
(iii) Normal form.
(iv) Point-slope form.
(v) Two-point form.
(vi) Symmetric form.

## (i) We have $12 y=8 x \quad 39$ or $=y \quad \frac{5}{12} x \quad \frac{39}{12} y m \quad \frac{5}{12}, y$-intercept $c=\frac{39}{12}$
(ii) $5 x-12 y=39$ or $\frac{5 x}{-39} \quad \frac{12 y}{39} \quad 1$ or $\frac{x}{-39 / 5} \quad \frac{y}{39 / 12} \quad 1$ is the required equation.
(iii) $5 x-12 y=39$. Divide both sides by $\pm \sqrt{5^{2}+125}=13$. Since R.H.S is to be positive, we have to take negative sign.

Hence $=\frac{5 x}{-13}+\frac{12 y}{13}=3$ is the normal form of the equation.
(iv) A point on the line is $\left(\frac{-39}{5}, 0\right)$ and its slope is $\frac{5}{12}$.

Equation can be written as: $y-0=\frac{5}{12}\left(x+\frac{39}{5}\right)$
(v) Another point on the line is $\left(0, \frac{39}{12}\right)$. Line through $\left(\frac{-39}{5}, 0\right)$ and $\left(0, \frac{39}{12}\right)$ is

$$
\frac{y-0}{0-\frac{39}{12}}=\frac{x+\frac{39}{5}}{-\frac{39}{5}-0}
$$

(vi) We have $\tan \alpha=\frac{5}{12}=m, \sin \alpha=\frac{5}{13}, \cos \alpha=\frac{12}{13}$. A point of the line is $\left(\frac{-39}{5}, 0\right)$. Equation of the line in symmetric form is

$$
\frac{x+39 / 5}{12 / 13}=\frac{y-0}{5 / 13}=r(\text { say })
$$

Example 2: $\quad$ Sketch the line
$3 x+2 y+6=0$.

Solution: To sketch the graph of (1), we find two points on it. If $y=0, x=-2$ and if $x=0, y=-3$.

Thus $x$ intercept $=-2$
$y$ intercept $=-3$
The points $A(-2,0), B(0,-3)$ are on (1). Plot these points in the plane and draw the straight line through $A$ and $B$. It is the graph of (1).

Example 3: $\quad$ Find the distance between the parallel lines
$2 x+y+2=0$
and $\quad 6 x+3 y-8=0$
(1)

Sketch the lines. Also find an equation of the line parallel to the given lines and lying midway between them.

Solution: We first convert both the lines into normal form. (1) can be written as $2 x+y=-2$
Dividing both sides by $-\sqrt{4+1}$, we have

$$
\frac{-2}{\sqrt{5}} x+\frac{-y}{\sqrt{5}}=\frac{2}{\sqrt{5}}
$$

which is normal form of (1). Normal form of (2) is

$$
\frac{6 x}{\sqrt{45}}+\frac{3 y}{\sqrt{45}}=\frac{8}{\sqrt{45}}
$$

i.e., $\frac{2 x}{\sqrt{5}}+\frac{y}{\sqrt{5}}=\frac{8}{3 \sqrt{5}}$

Length of the perpendicular from $(0,0)$ to the line (1) is $\frac{-}{\sqrt{5}}[$ From (3)]
Similarly, length of the perpendicular from $(0,0)$ to the line (2) is $\frac{8}{3 \sqrt{5}}[$ From (4)]

From the graphs of the lines it is clear that the lines are on opposite sides of the origin, so the distance between them equals the sum of the two perpendicular lengths.
i.e., Required distance $=\frac{2}{\sqrt{5}}+\frac{8}{3 \sqrt{5}}=\frac{14}{3 \sqrt{5}}$

The line parallel to the given lines lying midway between them is such that length of the perpendicular
from $O$ to the line $=\frac{8}{3 \sqrt{5}}-\frac{7}{3 \sqrt{5}}\left(\right.$ or $\frac{7}{3 \sqrt{5}}-\frac{2}{\sqrt{5}}$ ) $=\frac{1}{3 \sqrt{5}}$
Required line is $=\frac{2 x}{\sqrt{5}}+\frac{y}{\sqrt{5}}=-\frac{1}{3 \sqrt{5}}$ or $6 x+3 y=1$

### 4.3.7 Position of a point with respect to a line

Consider a non-vertical line $I$

$$
I: a x+b y+c=0
$$

in the $x y$-plane. Obviously, each point of the plane is either above the line or below the line or on the line.

Theorem: Let $P\left(x_{i}, y_{i}\right)$ be a point in the plane not lying on $I$

$$
I: a x+b y+c=0
$$

then $P$ lies
a) above the line (1) if $a x_{i}+b y_{i}+c>0$
b) below the line (1) if $a x_{i}+b y_{i}+c<0$

Proof: We can suppose that $b>0$ (first multiply the equation by -1 if needed). Draw a perpendicular from $P$ on $x$-axis meeting the line at $\left\langle x_{i} x_{i}, y^{\prime}\right\rangle$.

Thus $a x_{i}+b y^{\prime}+c=0$ so that

$$
y^{\prime}=\frac{a}{b} x_{i} \frac{c}{b}
$$

The point $P\left(x_{i}, y_{i}\right)$ is above the line if $y_{i}>y^{\prime}$ that is

$$
\begin{aligned}
& y_{i}-y^{\prime}>0 \\
\text { i.e. } & y_{i}-\left(-\frac{a}{b} x_{i}-\frac{c}{b}\right)>0 \\
\Rightarrow \quad & a x_{i}+b y_{i}+c>0
\end{aligned}
$$

Similarly $P\left(x_{i}, y_{i}\right)$ is below the line if

$$
y_{i}-y^{\prime}<0 \quad \text { i.e. } y_{i}-\left(-\frac{a}{b} x_{i}-\frac{c}{b}\right)
$$

or

$$
a x_{i}+b y_{i}+c<0
$$

The point $P\left(x_{i}, y_{i}\right)$ is on the line if

$$
a x_{i}+b y_{i}+c=
$$

Corollary 1. The point $P$ is above or below $I$ respectively if $a x_{i}+b y_{i}+c$ and $b$ have the same sign or have opposite signs.

Proof. If $P$ is above $I$, then $y_{i}-y^{\prime}>0$ i.e., $\frac{a x_{i}+b y_{i}+c}{b}>0$
Thus $a x_{i}+b y_{i}+c$ and $b$ have the same sign.
Similarly, $P$ is below $I$ if

$$
y_{i}-y^{\prime}<0 \quad \text { i.e., } \frac{a x_{i}+b y_{i}+c}{b}<0
$$

Thus $a x_{i}+b y_{i}+c$ and $b$ have opposite signs.
Corollary 2. The point $P\left(x_{i}, y_{i}\right)$ and the origin are
(i) on the same side of $I$ according as $a x_{i}+b y_{i}+c$ and $c$ have the same sign.
(ii) on the opposite sides of $I$ according as $a x_{i}+b y_{i}+c$ and $c$ have opposite signs.

Proof. (i) The point $P\left(x_{i}, y_{i}\right)$ and $O(0,0)$ are on the same side of $I$ if $a x_{i}+b y_{i}+c$ and $a .0+b .0+c$ have the same sign.
(ii) Proof is left as an exercise

Example 1: Check whether the point $(-2,4)$ lies above or below the line $4 x+5 y-3=0$

Solution: Here $b=5$ is positive. Also
$4(-2)+5(4)-3=-8+20-3=9>0$
The coefficient of $y$ in (1) and the expression (2) have the same sign and so the point $(-2,4)$ lies above (1).

Example 2: $\quad$ Check whether the origin and the point $P(5,-8)$ lie on the same side or on the opposite sides of the line:

$$
3 x+7 y+15=0
$$

## Here $\quad c=15$
For $P(5,-8)$,
$3(5)+7(-8)+15=-26<0$
But $\quad c=15>0$
$c$ and the expression (2) have opposite signs. Thus $O(0,0)$ and $P(5,-8)$ are on the opposite sides of (1).

Note: To check whether a point $P\left(x_{1}, y_{1}\right)$ lies above or below the line $a x+b y+c=0$
we make the co-efficient of $y$ positive by multiplying the equation by $(-1)$ if needed.

### 4.4 TWO AND THREE STRAIGHT LINES

For any two distinct lines $l_{1}, l_{2}$.
$l_{1}: a_{1} x+b_{1} y+c=0$ and $l_{2}: a_{2} x+b_{2} y+c=0$, one and only one of the following holds:
(i) $l_{1} \| l_{2}$
(ii) $l_{1} \perp l_{2}$
(iii) $l_{1}$ and $l_{2}$ are not related as (i) or (ii).

The slopes of $l_{1}$ and $l_{2}$ are $m_{1}=\frac{a_{1}}{b_{1}}, m_{2} \quad \frac{a_{2}}{b_{2}}$
(iv) $l_{1} \leq l_{2} \Leftrightarrow$ slope of $l_{1}\left(m_{1}\right)=$ slope of $l_{2}\left(m_{2}\right)$.

$$
\begin{aligned}
& \Leftrightarrow \quad \frac{a_{1}}{b_{1}}=-\frac{a_{2}}{b_{2}} \\
& \Leftrightarrow \quad \frac{a_{1}}{b_{2}}=-\frac{a_{2}}{b_{2}} \quad \Leftrightarrow \quad a_{1} b_{2}-b_{1} a_{2}=0
\end{aligned}
$$

(ii) $l_{1} \perp l_{2} \Leftrightarrow m_{1} m_{2}=-1$

$$
\Leftrightarrow\left(-\frac{a_{1}}{b_{1}}\right)\left(-\frac{a_{2}}{b_{2}}\right)=-1 \quad \Leftrightarrow a_{1} a_{2}+b_{1} b_{2}=0
$$

(iii) If $l_{1}$ and $l_{2}$ are not related as in (i) and (ii), then there is no simple relation of the above forms.

### 4.4.1 The Point of Intersection of two Straight Lines

Let $\quad l_{1}: a_{1} x+b_{1} y+c_{1}=0$
and $\quad l_{2}: a_{2} x+b_{2} y+c_{2}=0$
be two non-parallel lines. Then $a_{1} b_{2}-b_{1} a_{2} \neq 0$
Let $P\left(x_{1}, y_{1}\right)$ be the point of intersection of $l_{1}$ and $l_{2}$. Then
$a_{1} x_{1}+b_{1} y_{1}+c_{1}=0$
$a_{2} x_{1}+b_{2} y_{1}+c_{2}=0$
Solving (3) and (4) simultaneously, we have

$$
\begin{aligned}
& \frac{x_{1}}{b_{1} c_{2}-b_{2} c_{1}}=\frac{y_{1}}{a_{1} c_{1}-a_{1} c_{2}}=\frac{1}{a_{1} b_{2}-a_{2} b_{1}} \\
& x_{1}=\frac{b_{1} c_{2}-b_{2} c_{1}}{a_{1} b_{2}-a_{2} b_{1}} \text { and } y_{1} \quad \frac{a_{1} c_{1}-a_{1} c_{2}}{a_{1} b_{2}-a_{2} b_{1}}
\end{aligned}
$$

is the required point of intersection.

Note: $a_{1} b_{2}-a_{2} b_{1} \neq 0$, otherwise $l_{1} \| l_{2}$

Examples 1: Find the point of intersection of the lines

$$
\begin{aligned}
& 5 x+7 y=35 \\
& 3 x-7 y=21
\end{aligned}
$$

(ii)

Solution: We note that the lines are not parallel and so they

$$
\begin{aligned}
& \text { * If the lines are parallel } \\
& \text { then solution does not } \\
& \text { must intersect at a point. Adding (i) and (ii), we have } \\
& 8 x=56 \quad \text { or } \quad x=7 \\
& \text { Setting this value of } x \text { into (1), we find, } y=0 \text {. } \\
& \text { Thus }(7,0) \text { is the point of intersection of the two lines. }
\end{aligned}
$$

exist ( $z a, b_{1}-a, b_{1}=0$ )

* Before solving equations one should ensure that lines are not parallel.

### 4.4.2 Condition of Concurrency of Three Straight Lines

Three non-parallel lines

$$
\begin{aligned}
& l_{1}: a_{1} x+b_{1} y+c_{1}=0 \\
& l_{2}: a_{1} x+b_{2} y+c_{2}=0 \\
& l_{3}: a_{1} x+b_{2} y+c_{3}=0
\end{aligned}
$$

are concurrent iff $\left|\begin{array}{ll}a_{1} & b_{1} \\ a_{2} & b_{2} \\ a_{3} & b_{3} & c_{3}\end{array}\right|=0$

Proof: If the lines are concurrent then they have a common point of intersection $P\left(x_{1}, y_{1}\right)$ say. As $l_{1} \not l_{2}$, so their point of intersection $(x, y)$ is

$$
x=\frac{b_{1} c_{1}-b_{2} c_{2}}{a_{1} b_{2}-a_{2} b_{1}} \text { and } y \quad \frac{a_{1} c_{1}-a_{2} c_{2}}{a_{1} b_{2}-a_{2} b_{1}}
$$

This point also lies on (3), so

$$
\begin{aligned}
& a_{1}\left(\frac{b_{1} c_{1}-b_{2} c_{2}}{a_{1} b_{2}-a_{2} b_{1}}\right)+b_{2}\left(\frac{a_{1} c_{1}-a_{2} c_{2}}{a_{1} b_{2}-a_{2} b_{1}}\right)+c_{3}=0 \\
& a_{1}\left(b_{1} c_{2}-b_{2} c_{2}\right)+b_{2}\left(a_{1} c_{1}-a_{2} c_{2}\right)+c_{3}\left(a_{1} b_{2}-a_{2} b_{1}\right)=0
\end{aligned}
$$

or

An easier way to write the above equation is in the following determinant form:

$$
\left|\begin{array}{lll}
a_{1} & b_{1} & c_{1} \\
a_{2} & b_{2} & c_{2}
\end{array}\right|=0
$$

This is a necessary and sufficient condition of concurrency of the given three lines.
Example 1: Check whether the following lines are concurrent or not. If concurrent, find the point of concurrency.

$$
\begin{aligned}
& 3 x-4 y-3=0 \\
& 5 x+12 y+1=0 \\
& 32 x+4 y-17=0
\end{aligned}
$$

Solution. The determinant of the coefficients of the given equations is

$$
\begin{aligned}
& \left|\begin{array}{lll}
3 & -4 & -3 \\
5 & 12 & 1 \\
32 & 4 & -17
\end{array}\right|=\left|\begin{array}{lll}
18 & 32 & 0 \\
5 & 12 & 1 \\
117 & 208 & 0
\end{array}\right| \cdot \text { by } \quad R_{1}+3 R_{2} \\
& =-1\left|\begin{array}{ll}
18 & 32 \\
117 & 208
\end{array}\right|=-\left(208 \times 18-117 \times 32\right)=0
\end{aligned}
$$

Thus the lines are concurrent.
The point of intersection of any two lines is the required point of concurrency. From (1) and (2), we have

$$
\begin{aligned}
& \frac{x}{-4+36}=\frac{y}{-15-3}=\frac{1}{36+20} \\
& x=\frac{32}{56}=\frac{4}{7} \text { and } y=\frac{-18}{56}=\frac{-9}{28} \text { i.e. }\left(\frac{4}{7}, \frac{-9}{28}\right)
\end{aligned}
$$

is the point of intersection.

### 4.4.3 Equation of Lines through the point of intersection of two lines

We can find a family of lines through the point of intersection of two non parallel lines $l_{1}$ and $l_{2}$.

Let $l_{1}: a_{1} x+b_{1} y+c_{1}=0$
and $l_{2}: a_{2} x+b_{2} y+c_{2}=0$
For a non-zero real $h$, consider the equation

$$
a_{1} x+b_{1} y+c_{1}+h\left(a_{1} x+b_{1} y+c_{2}\right)=0
$$

This, being a linear equation, represents a straight line. For different values of $h$, (3) represents different lines. Thus (3) is a family of lines.

If $\left(x_{1}, y_{1}\right)$ is any point lying on both (1) and (2), then it is their point of intersection. Since $\left(x_{1}, y_{1}\right)$ lies on both (1) and (2), we have

$$
a_{1} x+b_{1} y+c_{1}=0+\text { and }+a_{2} x \quad b_{2} y \quad c_{2} \quad 0
$$

From the above two equations, we note that $\left(x_{1}, y_{1}\right)$ also lies on (3).
Thus (3) is the required family of lines through the point of intersection of (1) and (2). Since $h$ can assume an infinite number of values, (3) represents an infinite number of lines.

A particular line of the family (3) can be determined if one more condition is given.
Example 2: Find the family of lines through the point of intersection of the lines

$$
\begin{aligned}
& 3 x-4 y-10=0 \\
& x+2 y-10=0
\end{aligned}
$$

Find the member of the family which is
(i) parallel to a line with slope $\frac{-2}{3}$
(ii) perpendicular to the line $l: 3 x-4 y+1=0$.

Solution: (i) A family of lines through the point of intersection of equations (1) and (2) is

$$
\begin{aligned}
& 3 x-4 y-10+k(x+2 y-10)=0 \\
& \text { or } \quad(3+k) x+(-4+2 k) y+(-10-10 k)=0
\end{aligned}
$$

Slope $m$ of (3) is given by: $m=-\frac{3+k}{-4+2 k}$
This is slope of any member of the family (3).
If (3) is parallel to the line with slope $-\frac{2}{3}$ then
$-\frac{3+k}{-4+2 k}=\frac{-2}{3}$ or $9+3 k=-8+4 k$ i.e., $k=17$
Substituting $k=17$ into (3), equation of the member of the family is
$20 x+30 y-180=0$ i.e., $2 x+3 y-18=0$
(ii) Slope of $3 x-4 y+1=0$
is $\frac{3}{4}$. Since (3) is to be perpendicular to (4), we have $-\frac{3+k}{-4+2 k} \times \frac{3}{4}=-1$
or $9+3 k=-16+8 k \quad$ or $\quad k=5$
Inserting this value of $k$ into (3), we get $4 x+3 y-30=0$ which is required equation of the line.

Theorem: Altitudes of a triangle are concurrent.
Proof. Let the coordinates of the vertices of $\triangle A B C$ be as shown in the figure.

Then slope of $B C=\frac{y_{2}-y_{1}}{x_{2}-x_{1}}$
Therefore slope of the altitude $A D=-\frac{x_{2}-x_{1}}{y_{2}-y_{1}}$

## Equation of the altitude $A D$ is

$$
\begin{aligned}
& y-y_{1}=-\frac{x_{2}-x_{1}}{y_{2}-y_{1}}\left(x-x_{1}\right) \quad \text { (Point-slope form) } \\
& \text { or } \quad x\left(x_{1}-x_{2}\right)+y\left(y_{2}-y_{1}\right)-x_{1}\left(x_{2}-x_{1}\right)-y_{1}\left(y_{2}-y_{2}\right)=0
\end{aligned}
$$

Equations of the altitudes $B E$ and $C F$ are respectively (by symmetry)

$$
x\left(x_{1}-x_{1}\right)+y\left(y_{1}-y_{1}\right)-x_{2}\left(x_{1}-x_{1}\right)-y_{2}\left(y_{2}-y_{1}\right)=0
$$

and $x\left(x_{1}-x_{2}\right)+y\left(y_{1}-y_{2}\right)-x_{1}\left(x_{1}-x_{2}\right)-y_{1}\left(y_{2}-y_{1}\right)=0$
The three lines (1), (2) and (3) are concurrent if and only if

$$
\mathrm{D}=\left|\begin{array}{ccc}
x_{2}-x_{1} & y_{2}-y_{1} & -x_{1}\left(x_{2}-x_{1}\right)-y_{1}\left(y_{2}-y_{1}\right) \\
x_{1}-x_{1} & y_{2}-y_{1} & -x_{2}\left(x_{1}-x_{1}\right)-y_{2}\left(y_{2}-y_{1}\right) \\
x_{1}-x_{2} & y_{1}-y_{2} & -x_{1}\left(x_{1}-x_{2}\right)-y_{1}\left(y_{1}-y_{2}\right)
\end{array}\right| \text { is zero }
$$

Adding 2nd and 3rd rows to the 1st row of the determihant, we have

$$
\left|\begin{array}{ccc}
0 & 0 & 0 \\
x_{1}-x_{1} & y_{1}-y_{1} & -x_{2}\left(x_{1}-x_{1}\right)-y_{2}\left(y_{1}-y_{1}\right) \\
x_{1}-x_{2} & y_{1}-y_{2} & -x_{3}\left(x_{1}-x_{2}\right)-y_{3}\left(y_{1}-y_{2}\right)
\end{array}\right| = 0
$$

Thus the altitudes of a triangle are concurrent.

**Theorem:** Right bisectors of a triangle are concurrent.

**Proof.** Let \( A\left(x_{1}, y_{1}\right), B\left(x_{2}, y_{2}\right) \) and \( C\left(x_{3}, y_{3}\right) \) be the vertices of \( \Delta ABC \).

The midpoint \( D \) of \( BC \) has coordinates

$$
\left(\frac{x_2 + x_1}{2}, \frac{y_2 + y_3}{2}\right)
$$

Since the slope of \( BC \) is \( \frac{y_2 - y_3}{x_2 - x_3} \), the slope of the right bisector \( DO \) of \( BC \) is \( -\frac{x_2 - x_3}{y_2 - y_3} \).

### *Equation of the right bisector \( DO \) of \( BC \) is*

$$
y - \frac{y_2 + y_3}{2} = \frac{x_2 - x_3}{y_2 - y_3} \left( x \frac{x_2 + x_3}{2} \right) \quad \text{(Point-slope form)}
$$

or

$$
x \left(x_2 - x_3\right) + y \left(y_2 - y_3\right) - \frac{1}{2} \left( y_2^2 - y_3^2 \right) - \frac{1}{2} \left( x_2^2 - x_3^2 \right) = 0 \quad (1)
$$

*By symmetry, equations of the other two right bisectors \( EO \) and \( FO \) are respectively:*

$$
x \left(x_2 - x_3\right) + y \left(y_2 - y_3\right) - \frac{1}{2} \left( y_2^2 - y_3^2 \right) - \frac{1}{2} \left( x_2^2 - x_3^2 \right) = 0 \quad (2)
$$

and

$$
x \left(x_2 - x_3\right) + y \left(y_2 - y_3\right) - \frac{1}{2} \left( y_2^2 - y_3^2 \right) - \frac{1}{2} \left( x_2^2 - x_3^2 \right) = 0 \quad (3)
$$

The lines (1), (2) and (3) will be concurrent if and only if

$$
\begin{vmatrix}
x_2 - x_3 & y_2 - y_3 & -\frac{1}{2} \left( y_2^2 - y_3^2 \right) - \frac{1}{2} \left( x_2^2 - x_3^2 \right) \\
x_3 - x_1 & y_2 - y_3 & -\frac{1}{2} \left( y_2^2 - y_3^2 \right) - \frac{1}{2} \left( x_2^2 - x_3^2 \right) \\
x_1 - x_2 & y_1 - y_2 & -\frac{1}{2} \left( y_1^2 - y_3^2 \right) - \frac{1}{2} \left( x_1^2 - x_3^2 \right)
\end{vmatrix} = 0
$$

Adding 2nd and 3rd rows to 1st row of the determinant, we have

$$
\left|\begin{array}{ccc}
0 & 0 & 0 \\
x_2 - x_1 & y_2 - y_1 & -\frac{1}{2} \left( y_2^2 - y_3^2 \right) - \frac{1}{2} \left( x_2^2 - x_3^2 \right) \\
x_1 - x_2 & y_1 - y_2 & -\frac{1}{2} \left( y_1^2 - y_3^2 \right) - \frac{1}{2} \left( x_1^2 - x_3^2 \right)
\end{array}\right| = 0
$$

Thus the right bisectors of a triangle are concurrent.

**Note:** If equations of sides of the triangle are given, then intersection of any two lines gives a vertex of the triangle.

### 4.4.4 Distance of a point from a line

**Theorem:** The distance \( d \) from the point \( P\left(x_1, y_1\right) \) to the line \( l \)

$$
l : ax + by + c = 0 \quad (1)
$$

is given by

$$
d = \frac{\left| ax_1 + by_1 + c \right|}{\sqrt{a^2 + b^2}}
$$

**Proof:** Let \( l \) be non-vertical and non-horizontal line.

From \( P \), draw

$$
PQR \perp Os \text{ and } PM \perp l.
$$

Let the ordinate of \( Q \) be \( y_1 \) so that coordinates of \( Q \) are \( (x_1, y_1) \). Since \( Q \) lies on \( l \), we have \( ax_1 + by_1 + c = 0 \).

or $\quad y_{2}=\frac{-a x_{1}-c}{b}$
From the figure it is clear that $\angle M P Q=\alpha=$ the inclination of $I$.

$$
\text { Now } \tan \alpha=\text { slope of } I \frac{-a}{b}
$$

Therefore, $|\cos \alpha|=\frac{|b|}{\sqrt{a^{2}+b^{2}}}$
Thus $\quad|P M|=d=|P Q||\cos \alpha|=\left|y_{1}-y_{2}\right||\cos \alpha|$

$$
\begin{aligned}
& =\left|y_{1}-\frac{-a x_{1}-c}{b}\right| \frac{|b|}{\sqrt{a^{2}+b^{2}}} \\
& =\frac{\left|b y_{1}+a x_{1}+c\right|}{|b| \sqrt{a^{2}+b^{2}}} \quad|b| \quad \frac{\left|a x_{1}+b y_{1}+c\right|}{\sqrt{a^{2}+b^{2}}}
\end{aligned}
$$

If $I$ is horizontal, its equation is of the form $y=-\frac{c}{b}$ and the distance from $P\left(x_{1}, y_{1}\right)$ to $I$ is simply the difference of the $y$-values.

$$
\therefore \quad d=\left|y_{1}-\left(-\frac{c}{b}\right)\right|=\left|\frac{b y_{1}+c}{b}\right|
$$

Similarly, if the line is vertical and has equation: $x=\frac{-c}{a}$ then $d \quad \frac{\left|a x_{1}+c\right|}{a}$.
Note: If the point $P\left(x_{1}, y_{1}\right)$ lies on $I$, then the distance $d$ is zero, since $\left(x_{1}, y_{1}\right)$ satisfies the equation i.e., $a x_{1}+b y_{1}+c=0$

### 4.4.5 Distance Between two Parallel Lines

The distance between two parallel lines is the distance from any point on one of the lines to the other line.

Example: Find the distance between the parallel lines
$I: 2 x-5 y+13=0$ and
$I_{1}: 2 x-5 y+6=0$

Solution: First find any point on one of the lines, say $I_{1}$. If $x=1$ lies on $I_{1}$, then
$y=3$ and the point $(1,3)$ lies on it. The distance $d$ from $(1,3)$ to $I_{2}$ is

$$
d=\frac{|2(1)-5(3)+6|}{\sqrt{(-2)^{2}+5^{2}}} \quad \frac{|2-15+6|}{\sqrt{4+25}} \quad \frac{7}{\sqrt{29}}
$$

The distance between the parallel lines is $\frac{7}{\sqrt{29}}$.

### 4.4.6 Area of a Triangular Region Whose Vertices are Given

To find the area of a triangular region whose vertices are: $P\left(x_{1}, y_{1}\right), Q\left(x_{2}, y_{2}\right)$ and $R\left(x_{3}, y_{3}\right)$.
Draw perpendiculars $\overline{P L}, \overline{Q N}$ and $\overline{R M}$ on $x$-axis.
Area of the triangular region $P Q R$

- Area of the trapezoidal region $P L M R$
+ Area of the trapezoidal region $R M N Q$
- Area of the trapezoidal region $P L N Q$.
$=\frac{1}{2}\left(\left|\overline{P L}\right|+\left|\overline{R M}\right|\right)\left(\left|\overline{L M}\right|\right)+\frac{1}{2}\left(\left|\overline{R M}\right|+\left|\overline{Q N}\right|\right)\left(\left|\overline{M N}\right|\right)-\frac{1}{2}\left(\left|\overline{P L}\right|+\left|\overline{Q N}\right|\right)\left(\left|\overline{L N}\right|\right)$
$=\frac{1}{2}\left[\left(y_{1}+y_{2}\right)\left(x_{3}-x_{1}\right)+\left(y_{2}+y_{3}\right)\left(x_{2}-x_{3}\right)-\left(y_{1}+y_{2}\right)\left(x_{2}-x_{1}\right)\right]$
$=\frac{1}{2}\left(x_{1} y_{1}+x_{2} y_{2}-x_{1} y_{1}+x_{1} y_{3}+x_{2} y_{2}+x_{2} y_{2}-x_{2} y_{3}-x_{2} y_{1}+x_{1} y_{1}+x_{1} y_{2}\right)$
$=\frac{1}{2}\left(x_{1} y_{1}-x_{1} y_{3}+x_{2} y_{2}-x_{2} y_{2}-x_{2} y_{1}+x_{1} y_{2}\right)$
Thus required area $A$ is given by:
$\Delta=\frac{1}{2}\left(x_{1}\left(y_{2}-y_{3}\right)+x_{2}\left(y_{3}-y_{1}\right)+x_{3}\left(y_{1}-y_{2}\right)\right)$

Forollary: If the points $P, Q$ and $R$ are collinear, then
$\Delta=0$

Note: In numerical problems, if sign of the area is negative, then it is to be omitted.
Example 1: Find the area of the region bounded by the triangle with vertices $(a, b+c)$, $(a, b-c)$ and $(-a, c)$.
Solution: Required area $\Delta$ is

$$
\begin{aligned}
& \Delta=\frac{1}{2}\left[\begin{array}{ll}
a & b+c \\
a & b-c
\end{array}\right] \\
& \left.\begin{array}{ll}
a \\
-a & c
\end{array}\right] \\
& =\frac{1}{2}\left[\begin{array}{ll}
a & b+c \\
a & c
\end{array}\right]
\end{aligned}
$$

Trapezium:
A quadrilateral having two parallel and two non-parallel sides.
Area of trapezoidal region:
$\frac{1}{2}$ (sum of $\|$ sides) /distance between $\|$ sides
$=\frac{1}{2}[-2 c(a+a)]$, expanding by the second row
$=-2 c a$
Thus $\Delta=2 c a$
Example 2: By considering the area of the region bounded by the triangle with vertices $A(1,4), B(2,-3)$ and $C(3,-10)$
check whether the three points are collinear or not.
Solution: Area $\Delta$ of the region bounded by the triangle $A B C$ is

$$
\begin{aligned}
& \Delta=\frac{1}{2}\left[\begin{array}{ll}
1 & 4 \\
2 & -3 \\
3 & -10
\end{array}\right] \quad=\frac{1}{2}\left[\begin{array}{cc}
1 & 4 \\
1 & -7 \\
3 & -14
\end{array}\right] \text { by } R_{2}-R_{1} \text { and } R_{3}-R_{1} \\
& =\frac{1}{2}[1(-14+14)] \text {, expanding by third column } \\
& =0
\end{aligned}
$$

Thus the points are collinear.

## EXERCISE 4.3

1. Find the slope and inclination of the line joining the points:
(i) $(-2,4) ;(5,11)$
(ii) $(3,-2) ;(2,7)$
(iii) $(4,6) ;(4,8)$

Sketch each line in the plane.
2. In the triangle $A(8,6) B(-4,2), C(-2,-6)$, find the slope of
(i) each side of the triangle
(ii) each median of the triangle
(iii) each altitude of the triangle.
3. By means of slopes, show that the following points lie on the same line:
(a) $(-1,-3) ;(1,5) ;(2,9)$
(b) $(4,-5) ;(7,5) ;(10,15)$
(c) $(-4,6) ;(3,8) ;(10,10)$
(d) $(a, 2 b):(c, a+b) ;(2 c-a, 2 a)$
4. Find $k$ so that the line joining $A(7,3) ; B(k,-6)$ and the line joining $C(-4,5) ; D(-6,4)$ are (i) parallel (ii) perpendicular.
5. Using slopes, show that the triangle with its vertices $A(6,1), B(2,7)$ and $C(-6,-7)$ is a right triangle.
6. The three points $A(7,-1), B(-2,2)$ and $C(1,4)$ are consecutive vertices of a parallelogram. Find the fourth vertex.
7. The points $A(-1,2), B(3,-1)$ and $C(6,3)$ are consecutive vertices of a rhombus. Find the fourth vertex and show that the diagonals of the rhombus are perpendicular to each other.
8. Two pairs of points are given. Find whether the two lines determined by these points are :
(i) parallel
(ii) perpendicular
(iii) none.
(a) $(1,-2),(2,4)$ and $(4,1),(-8,2)$
(b) $(-3,4),(6,2)$ and $(4,5),(-2,-7)$
9. Find an equation of
(a) the horizontal line through $(7,-9)$
(b) the vertical line through $(-5,3)$

(c) the line bisecting the first and third quadrants.
(d) the line bisecting the second and fourth quadrants.
10. Find an equation of the line
(a) through $A(-6,5)$ having slope 7
(b) through $(8,-3)$ having slope 0
(c) through $(-8,5)$ having slope undefined
(d) through $(-5,-3)$ and $(9,-1)$
(e) $y$-intercept: -7 and slope: -5
(f) $x$-intercept: -3 and $y$-intercept: 4
(g) $x$-intercept: -9 and slope: -4
11. Find an equation of the perpendicular bisector of the segment joining the points $A(3,5)$ and $B(9,8)$.
12. Find equations of the sides, altitudes and medians of the triangle whose vertices are $A(-3,2), B(5,4)$ and $C(3,-8)$.
13. Find an equation of the line through $(-4,-6)$ and perpendicular to a line having slope $\frac{-3}{2}$
14. Find an equation of the line through $(11,-5)$ and parallel to a line with slope -24 .
15. The points $A(-1,2), B(6,3)$ and $C(2,-4)$ are vertices of a triangle. Show that the line joining the midpoint $D$ of $A B$ and the midpoint $E$ of $A C$ is parallel to $B C$ and $D E=\frac{1}{2} B C$.
16. A milkman can sell 560 litres of milk at Rs. 12.50 per litre and 700 litres of milk at Rs. 12.00 per litre. Assuming the graph of the sale price and the milk sold to be a straight line, find the number of litres of milk that the milkman can sell at Rs. 12.25 per litre.
17. The population of Pakistan to the nearest million was 60 million in 1961 and 95 million in 1981. Using $t$ as the number of years after 1961, find an equation of the line that gives the population in terms of $t$. Use this equation to find the population in (a) 1947 (b) 1997.
18. A house was purchased for Rs. 1 million in 1980. It is worth Rs. 4 million in 1996. Assuming that the value increased by the same amount each year, find an equation that gives the value of the house after $t$ years of the date of purchase. What was its value in 1990?
19. Plot the Celsius $(C)$ and Fahrenheit $(F)$ temperature scales on the horizontal axis and the vertical axis respectively. Draw the line joining the freezing point and the boiling point of water. Find an equation giving $F$ temperature in terms of $C$.
20. The average entry test score of engineering candidates was 592 in the year 1998 while the score was 564 in 2002. Assuming that the relationship between time and score is linear, find the average score for 2006.
21. Convert each of the following equation into
(i) Slope intercept form
(ii) two intercept form
(iii) normal form
(a) $2 x-4 y+11=0$
(b) $4 x+7 y-2=0$
(c) $15 y-8 x+13=0$

Also find the length of the perpendicular from $(0,0)$ to each line.
22. In each of the following check whether the two lines are
(i) parallel
(ii) perpendicular
(iii) neither parallel nor perpendicular
(a) $2 x+y-3=0$
$4 x+2 y+5=0$
(b) $3 y+2 x+5$
$3 \# 2 y \# 0$
(c) $4 y+2 x-1=0$
$x-2 y-7=0$
(d) $4 x-y+2=0-$
$\triangleright \triangleleft 2 x \quad 3 y \quad 1 \quad 0$
(e) $12 x+35 y-7=0$
$105 x-36 y+11=0$
23. Find the distance between the given parallel lines. Sketch the lines. Also find an equation of the parallel line lying midway between them.
(a) $3 x-4 y+3=0$
$3 x-4 y+7=0$
(b) $12 x+5 y-6=0$
$12 x+5 y+13=0$
(c) $x+2 y-5=0+$
$\triangleright \quad 2 x \quad 4 y \quad 1$

**24.** Find an equation of the line through (−4, 7) and parallel to the line 2*x* − 7*y* + 4 = 0.

**25.** Find an equation of the line through (5, −8) and perpendicular to the join of *A* (−15, −8), *B* (10, 7).

**26.** Find equations of two parallel lines perpendicular to 2*x* − *y* + 3 = 0 such that the product of the *x*-and *y*-intercepts of each is 3.

**27.** One vertex of a parallelogram is (1, 4); the diagonals intersect at (2, 1) and the sides have slopes 1 and $$\frac{-1}{2}$$. Find the other three vertices.

**28.** Find whether the given point lies above or below the given line
- (a) (5, 8); 2*x* − 3*y* + 6 = 0
- (b) (−7, 6); 4*x* + 3*y* − 9 = 0

**29.** Check whether the given points are on the same or opposite sides of the given line.
- (a) (0, 0) and (−4, 7); 6*x* − 7*y* + 70 = 0
- (b) (2, 3) and (−2, 3); 3*x* − 5*y* + 8 = 0

**30.** Find the distance from the point *P*(6, −1) to the line 6*x* − 4*y* + 9 = 0.

**31.** Find the area of the triangular region whose vertices are *A* (5, 3), *B* (−2, 2), *C* (4, 2).

**32.** The coordinates of three points are *A*(2, 3), *B*(−1, 1) and *C*(4, −5). By computing the area bounded by *ABC* check whether the points are collinear.

### **4.5. ANGLE BETWEEN TWO LINES**

Let *l<sub>1</sub>* and *l<sub>2</sub>* be two intersecting lines, which meet at a point *P*. At the point *P* two supplementary angles are formed by the lines *l<sub>1</sub>* and *l<sub>2</sub>*.

Unless *l<sub>1</sub>* ⊥ *l<sub>2</sub>* one of the two angles is acute. The angle from *l<sub>1</sub>* to *l<sub>2</sub>* is the angle *θ* through which *l<sub>1</sub>* is rotated anti-clockwise about the point *P* so that it coincides with *l<sub>2</sub>*.

In the figure below *θ* is angle of intersection of the two lines and it is measured from *l<sub>1</sub>* to *l<sub>2</sub>* in counterclockwise direction, *ψ* is also angle of intersection but it is measured from *l<sub>1</sub>* to *l<sub>1</sub>*.

With this convention for angle of intersection, it is clear that the inclination of a line is the angle measured in the counterclockwise direction from the positive *x*-axis to the line, and it tallies with the earlier definition of the inclination of a line.

**Theorem:** Let *l<sub>1</sub>* and *l<sub>2</sub>* be two non-vertical lines such that they are not perpendicular to each other. If *m<sub>1</sub>* and *m<sub>2</sub>* are the slopes of *l<sub>1</sub>* and *l<sub>2</sub>* respectively: the angle *θ* from *l<sub>1</sub>* to *l<sub>2</sub>* is given by:

$$
\tan \theta = \frac{m_1 - m_1}{1 + m_1 m_2}
$$

**Proof:** From the figure, we have

$$
\alpha_2 = \alpha_1 + \theta
$$

or

$$
\theta = \alpha_2 - \alpha_1
$$

$$
\tan \theta = \tan(\alpha_2 - \alpha_1) = \frac{\tan \alpha_2 - \tan \alpha_1}{1 + \tan \alpha_1 \tan \alpha_2} = \frac{m_2 - m_1}{1 + m_1 m_2}
$$

$$
\therefore \quad \tan \theta = \tan(\alpha_2 - \alpha_1) = \frac{\tan \alpha_2 - \tan \alpha_1}{1 + \tan \alpha_1 \tan \alpha_2} = \frac{m_2 - m_1}{1 + m_1 m_2}
$$

**Corollary 1.** *l<sub>1</sub>* || *l<sub>2</sub>* if and only if *m<sub>1</sub>* = *m<sub>2</sub>*

$$
\Rightarrow \quad \tan \theta = 0 \quad \frac{m_1 - m_1}{1 + m_1 m_2}
$$

$$
\Rightarrow \quad m_2 = m_1
$$

**Corollary 2.** *l<sub>1</sub>* ⊥ *l<sub>2</sub>* iff 1 + *m<sub>1</sub>m<sub>2</sub>* = 0

$$
\Rightarrow \quad \tan \theta = \frac{m_2 - m_1}{1 + m_1 m_2} = \tan \frac{\theta}{2} = + \quad = 1 \quad m_1 m_2 \quad 0
$$

These two results have already been stated in 4.3.1.

**Example 1:** Find the angle from the line with slope $$\frac{-7}{3}$$ to the line with slope $$\frac{5}{2}$$.

**Solution:** Here *m<sub>2</sub>* = $$\frac{5}{2}$$, *m<sub>1</sub>* = $$\frac{-7}{3}$$. If *θ* is measure of the required angle, then

$$
\tan \theta=\frac{\frac{5}{2}-\left(\frac{-7}{3}\right)}{1+\frac{5}{2}\left(\frac{-7}{3}\right)}=\frac{29}{-29}=-1
$$

Thus $\theta=135^{\circ}$
Example 2: Find the angles of the triangle whose vertices are

$$
A(-5,4), B(-2,-1), C(7,-5)
$$

Solution: Let the slopes of the sides $A B, B C$ and $C A$ be denoted by $m_{x}, m_{y}, m_{z}$ respectively. Then

$$
m_{x}=\frac{4+1}{-5+2}-\frac{-5}{3}, m_{y}=\frac{-5+1}{7+2}=\frac{-4}{9}, m_{z}=\frac{-5-4}{7+5}=\frac{-3}{4}
$$

Now angle $A$ is measured from $A B$ to $A C$.

$$
\tan A=\frac{m_{x}-m_{y}}{1+m_{x} m_{y}}=\frac{\frac{-3}{4}+\frac{5}{3}}{1+\left(\frac{-3}{4}\right)\left(\frac{-5}{3}\right)} \quad \frac{11}{27} \quad \text { or } \quad m \underbrace{\underline{A}}_{22.2^{\circ}}
$$

The angle $B$ is measured from $B C$ to $B A$

$$
\therefore \quad \tan B=\frac{m_{x}-m_{y}}{1+m_{x} m_{y}}=\frac{\frac{-5}{3}+\frac{4}{9}}{1+\left(\frac{-5}{3}\right)\left(\frac{-4}{9}\right)}=\frac{-33}{47} \quad \text { or } \quad m \underbrace{B}_{B}=144.9^{\circ}
$$

The angle $C$ is measured from $C A$ to $C B$.

$$
\therefore \quad \tan A=\frac{m_{x}-m_{y}}{1+m_{x} m_{y}}=\frac{\frac{-4}{9}+\frac{3}{4}}{1+\left(\frac{-4}{9}\right)\left(\frac{-3}{4}\right)}=\frac{11}{48} \quad \text { or } \quad m \underbrace{C}_{C}=12.9^{\circ}
$$

# 4.5.1 Equation of a Straight Line in Matrix form

It is easy to solve two or three simultaneous linear equations by elementary methods. If the number of equations and variables become large, the solution of the equations by ordinary method becomes very difficult. In such a case, given equations are written in matrix form and solved.

## One Linear Equation:

A linear equation

$$
l: a x+b y+c=0
$$

in two variables $x$ and $y$ has its matrix form as:

$$
\begin{aligned}
& {[a x+b y]=[-c]} \\
& \text { or } \quad\left[\begin{array}{ll}
a & b
\end{array}\right]\left[\begin{array}{l}
x \\
y
\end{array}\right]=[-c] \\
& \text { or } \quad A X \times C
\end{aligned}
$$

where $\quad A=[a \quad b], \quad X=\left[\begin{array}{l}x \\ y\end{array}\right]$ and $C=[-c]$

## A System of Two Linear Equations:

A system of two linear equations

$$
\begin{aligned}
& l_{1}: a_{1} x+b_{1} y+c=0 \\
& l: a_{2} x+b_{2} y+c=0
\end{aligned}
$$

in two variables $x$ and $y$ can be written in matrix form as:

$$
\begin{aligned}
& {\left[\begin{array}{l}
a_{1} x+b_{1} y \\
a_{2} x+b_{2} y
\end{array}\right] \times\left[\begin{array}{l}
-c_{1} \\
-c_{2}
\end{array}\right]} \\
& \text { or } \\
& \left[\begin{array}{ll}
a_{1} & b_{1} \\
a_{2} & b_{2}
\end{array}\right]\left[\begin{array}{l}
x \\
y
\end{array}\right]=\left[\begin{array}{l}
-c_{1} \\
-c_{2}
\end{array}\right] \\
& \text { or } \\
& A X \times C
\end{aligned}
$$

$$
A X \times C
$$

where $\quad A=\left[\begin{array}{ll}a_{1} & b_{1} \\ a_{2} & b_{2}\end{array}\right], \quad X\left[\begin{array}{l}x \\ y\end{array}\right]$ and $C=\left[\begin{array}{l}-c_{1} \\ -c_{2}\end{array}\right]$
Equations (2) have a solution iff $\operatorname{det} A \neq 0$.

## A System of Three Linear Equations:

A system of three linear equations

$$
\begin{aligned}
& l_{1}: a_{1} x+b_{1} y+c_{1}=0 \\
& l_{2}: a_{2} x+b_{2} y+c_{2}=0 \\
& l_{3}: a_{3} x+b_{3} y+c_{3}=0
\end{aligned}
$$

in two variables $y$ and $y$ takes the matrix form as

$$
\begin{aligned}
& {\left[\begin{array}{lll}
a_{1} x+b_{1} y+c_{1} \\
a_{2} x+b_{2} y+c_{2}
\end{array}\right]=\left[\begin{array}{l}
0 \\
0 \\

\end{array}\right]} \\
& \text { or } \quad\left[\begin{array}{llll}
a_{1} & b_{1} & c_{1}
\end{array}\right]\left[\begin{array}{l}
x \\
y \\
a_{2}
\end{array}\right]=\left[\begin{array}{l}
0 \\
0 \\

\end{array}\right]
\end{aligned}
$$

or

$$
\left[\begin{array}{lll}
a_{1} & b_{1} & c_{1}
\end{array}\right]
$$

If the matrix

$$
\left[\begin{array}{lll}
a_{1} & b_{1} & c_{1}
\end{array}\right] \text { is singular, then the lines (5) are concurrent }
$$

is singular, then the lines (5) are concurrent
a $_{1} \quad b_{1} \quad c_{1}$ and so the system (5) has a unique solution.
Example 1: Express the system

$$
\begin{aligned}
& 3 x+4 y-7=0 \\
& 2 x-5 y+8=0 \\
& x+y-3=0
\end{aligned}
$$

in matrix form and check whether the three lines are concurrent
Solution. The matrix form of the system is

$$
\left[\begin{array}{rrrr}
3 & 4 & -7 \\
2 & -5 & 8 \\
1 & 1 & -3
\end{array}\right]\left[\begin{array}{l}
x \\
y \\

\end{array}\right]=\left[\begin{array}{l}
0 \\
0 \\

\end{array}\right]
$$

Coefficient matrix of the system is

$$
A=\left[\begin{array}{rrrr}
3 & 4 & -7 \\
2 & 5 & 8 \\
1 & 1 & -3
\end{array}\right] \text { and } \operatorname{det} A\left[\begin{array}{lll}
0 & 1 & 2 \\
0 & & 7 & 14 \\
1 & & 1 & -3
\end{array}\right] \begin{aligned}
& \text { by } R_{1}-3 R_{2} \\
& \text { and } R_{2}-2 R_{3}
\end{aligned}
$$

and $\operatorname{det} A=1(14+14)=28 \neq 0$
As $A$ is non-singular, so the lines are not concurrent.
Example 2: Find a system of linear equations corresponding to the matrix form

$$
\left[\begin{array}{llll}
1 & 2 & 5 \\
3 & 5 & 1 \\
4 & 7 & 6
\end{array}\right]\left[\begin{array}{l}
x \\
y \\

\end{array}\right]=\left[\begin{array}{l}
0 \\
0 \\

\end{array}\right]
$$

Are the lines represented by the system concurrent?
Solution: Multiplying the matrices on the L.H.S. of (1), we have

$$
\left[\begin{array}{l}
x+2 y+5 \\
3 x+5 y+1 \\
4 x+7 y+6
\end{array}\right]=\left[\begin{array}{l}
0 \\
0 \\

\end{array}\right]
$$

By using the definition of equality of two matrices, we have from (2),

$$
\begin{aligned}
& x+2 y+5=0 \\
& 3 x+5 y+1=0 \\
& 4 x+7 y+6=0
\end{aligned}
$$

as the required system of equations. The coefficient matrix $A$ of the system is such that

$$
\operatorname{det} A=\left[\begin{array}{llll}
1 & 2 & 5 \\
3 & 5 & 1 \\
4 & 7 & 6
\end{array}\right]=\left[\begin{array}{lll}
1 & 2 & 5 \\
0 & -1 & -14 \\
0 & -1 & -14
\end{array}\right]=0
$$

Thus the lines of the system are concurrent.

## EXERCISE 4.4

1. Find the point of intersection of the lines
(i) $x-2 y+1=0-\quad$ and $2 x \quad y \quad 2 \quad 0$
(ii) $3 x+y+12=0+\quad$ and $=\quad x \quad 2 y \quad 1 \quad 0$
(iii) $x+4 y-12=0-\quad$ and $=\quad x \quad 3 y \quad 3 \quad 0$
2. Find an equation of the line through
(i) the point $(2,-9)$ and the intersection of the lines $2 x+5 y-8=0-\quad$ and $=3 x \quad 4 y \quad 6 \quad 0$
(ii) the intersection of the lines $x-y-4=0+\quad+$ and $7 x \quad y \quad 20 \quad 0 \quad$ and
(a) parallel
(b) perpendicular to the line $6 x+y-14=0$
(iii) through the intersection of the lines $x+2 y+3=0,3 x+4 y+7=0$ and making equal intercepts on the axes.
3. Find an equation of the line through the intersection of $16 x-10 y-33=0 ; 12 x-14 y-29=0 \quad$ and the intersection of $x-y+4=0 \quad ; \quad x-7 y+2=0$
4. Find the condition that the lines $y=m_{1} x+c_{1} ; y=m_{2} x+c_{2}$ and $y=m_{3} x+c_{3}$ are concurrent.
5. Determine the value of $p$ such that the lines $2 x-3 y-1=0$, $3 x-y-5=0$ and $3 x+4 y+8=0$ meet at a point.
6. Show that the lines $4 x-3 y-8=0,3 x-4 y-6=0$ and $x-y-2=0$ are concurrent and the third-line bisects the angle formed by the first two lines.
7. The vertices of a triangle are $A(-2,3), B(-4,1)$ and $C(3,5)$. Find coordinates of the
(i) centroid
(ii) orthocentre
(iii) circumcentre of the triangle

Are these three points collinear?
8. Check whether the lines
$4 x-3 y-8=0 ; \quad 3 x-4 y-6=0 ; \quad x-y-2=0$
are concurrent. If so, find the point where they meet
9. Find the coordinates of the vertices of the triangle formed by the lines $x-2 y-6=0 ; \quad 3 x-y+3=0 ; \quad 2 x+y-4=0$
Also find measures of the angles of the triangle.
10. Find the angle measured from the line $l_{1}$ to the line $l_{2}$ where
(a) $l_{1}:$ Joining $(2,7)$ and $(7,10)$
$l_{2}:$ Joining $(1,1)$ and $(-5,3)$
(b) $l_{1}:$ Joining $(3,-1)$ and $(5,7)$
$l_{2}:$ Joining $(2,4)$ and $(-8,2)$
Also find the acute angle in each case.
(c) $l_{1}:$ Joining $(1,-7)$ and $(6,-4)$
$l_{2}:$ Joining $(-1,2)$ and $(-6,-1)$
(d) $l_{1}:$ Joining $(-9,-1)$ and $(3,-5)$
$l_{2}:$ Joining $(2,7)$ and $(-6,-7)$
11. Find the interior angles of the triangle whose vertices are
(a) $A(-2,11), B(-6,-3),(4,-9)$
(b) $A(6,1), \quad B(2,7), C(-6,-7)$
(c) $A(2,-5), \quad B(-4,-3),(-1,5)$
(d) $A(2,8), \quad B(-5,4), C(4,-9)$
12. Find the interior angles of the quadrilateral whose vertices are $A(5,2), B(-2,3)$, $C(-3,-4)$ and $D(4,-5)$
13. Show that the points
$A(0,0), B(2,1), C(3,3), D(1,2)$ are the vertices of a rhombus.
Find its interior angles.
14. Find the area of the region bounded by the triangle whose sides are $7 x-y-10=0 ; \quad 10 x+y-14=0 ; \quad 3 x+2 y+3=0$
15. The vertices of a triangle are $A(-2,3), B(-4,1)$ and $C(3,5)$. Find the centre of the circumcircle of the triangle.

16. Express the given system of equations in matrix form. Find in each case whether the lines are concurrent.
(a) $x+3 y-2=0 ; \quad 2 x-y+4=0 ; \quad x-11 y+14=0$
(b) $2 x+3 y+4=0 ; \quad x-2 y-3=0 ; \quad 3 x+y-8=0$
(c) $3 x-4 y-2=0 ; \quad x+2 y-4=0 ; \quad 3 x-2 y+5=0$.
17. Find a system of linear equations corresponding to the given matrix form. Check whether the lines represented by the system are concurrent.
(a) $\left[\begin{array}{cccc|c}1 & 0 & -1 & x \\ 2 & 0 & 1 & y & 0 \\ 0 & -1 & 6 & 1 & 0\end{array}\right]$
(b) $\left[\begin{array}{cccc|c}1 & 1 & 2 & x \\ 2 & 4 & -3 & y & 0 \\ 3 & 6 & -5 & 1\end{array}\right]$
$=\left[\begin{array}{c}0 \\ 0 \\ 0\end{array}\right]$

### 4.6 HOMOGENEOUS EQUATION OF THE SECOND DEGREE IN TWO VARIABLES

We have already seen that if a graph is a straight line, then its equation is a linear equation in the variables $x$ and $y$. Conversely, the graph of any linear equation in $x$ and $y$ is a straight line.

Suppose we have two straight lines represented by

$$
a_{x} x+b_{y} y+c_{z}=0
$$

and

$$
a_{y} x+b_{z} y+c_{x}=0
$$

Multiplying equations (1) and (2), we have

$$
\left(a_{x} x+b_{y} y+c_{z}\right)\left(a_{y} x+b_{z} y+c_{x}\right)=0
$$

It is a second degree equation in $x$ and $y$.
Equation (3) is called joint equation of the pair of lines (1) and (2). On the other hand, given an equation of the second degree in $x$ and $y$, say

$$
a x^{2}+2 h x y+b y^{2}+2 g x+2 f y+c=0
$$

where $a \neq 0$, represents equations of a pair of lines if (4) can be resolved into two linear factors. In this section, we shall study special joint equations of pairs of lines which pass through the origin.

Let $y=m_{1} x$ and $y=m_{2} x$ be two lines passing through the origin. Their joint equation is: $\left(y-m_{1} x\right)\left(y-m_{2} x\right)=0$
or $\quad y^{2}-\left(m_{1}+m_{2}\right) x y+m_{1} m_{2} x^{2}=0$
Equation (5) is a special type of a second degree homogeneous equation.

### 4.6.1 Homogeneous Equation

Let $f(x, y)=0$
be any equation in the variables $x$ and $y$. Equation (1) is called a homogeneous equation of degree $n$ (a positive integer) if

$$
f(k x, k y)=k^{n} f(x, y)
$$

for some real number $k$.
For example, in equation (5) above if we replace $x$ and $y$ by $k x$ and $k y$ respectively, we have

$$
\begin{aligned}
& k^{2} y^{2}-k^{2}\left(m_{1}+m_{2}\right) x y+k^{2} m_{1} m_{2} x^{2}=0 \\
\text { or } & k^{2}\left[y^{2}-\left(m_{1}+m_{2}\right) x y+m_{1} m_{2} x^{2}\right]=0 \quad \text { i.e., } \quad k^{2} f(x, y) \quad 0
\end{aligned}
$$

Thus (5) is a homogeneous equation of degree 2.

$$
a x^{2}+2 h x y+b y^{2}=0
$$

A general second degree homogeneous equation can be written as:

$$
a x^{2}+2 h x y+b y^{2}=0
$$

provided $a, h$ and $b$ are not simultaneously zero.

Theorem: Every homogenous second degree equation

$$
a x^{2}+2 h x y+b y^{2}=0
$$

represents a pair of lines through the origin. The lines are
(i) real and distinct, if $h^{2}>a b$
(ii) real and coincident, if $h \quad a b$
(iii) imaginary, if $h^{2}<a b$

Proof: Multiplying (1) by b and re-arranging the terms, we have

$$
b^{2} y^{2}+2 b k x y+a b x^{2}=0
$$

or $\quad b^{2} y^{2}+2 b k x y+h^{3} x^{2}-h^{3} x^{2}+a b x^{2}=0$
or $\quad(b y+h x)^{3}-x^{2}\left(h^{3}-a b\right)=0$
or $\quad(b y+h x+x \sqrt{h^{3}-a b})(b y+h x-x \sqrt{h^{3}-a b})=0$
Thus (1) represents a pair of lines whose equations are:

$$
b y+x\left(h+\sqrt{h^{3}-a b}\right)=0
$$

and $b y+x\left(h-\sqrt{h^{3}-a b}\right)=0$
Clearly, the lines (2) and (3) are
(i) real and distinct if $h^{3}>a b$. (ii) real and coincident, if $h^{3}=a b$.
(iii) imaginary, if $h^{3}<a b$.

It is interesting to note that even in case the lines are imaginary, they intersect in a real point viz $(0,0)$ since this point lies on their joint equation (1).

Example: Find an equation of each of the lines represented by

$$
20 x^{2}+17 x y-24 y^{2}=0
$$

Solution. The equation may be written as

$$
\begin{aligned}
& 24\left(\frac{y}{x}\right)^{2}-17\left(\frac{y}{x}\right)-20=0 \\
& \Rightarrow \quad \frac{y}{x}=\frac{17 \pm \sqrt{289+1920}}{48}-\frac{17 \pm 47}{48}-\frac{4}{3}-\frac{-5}{8} \\
& \Rightarrow \quad y=\frac{4}{3} x \quad \text { and } \quad y=\frac{-5}{8} x \\
& \Rightarrow \quad 4 x-3 y=0 \quad \text { and } \quad 5 x+8 y=0
\end{aligned}
$$

version: 1.1

### 4.6.2 To find measure of the angle between the lines represented by

$$
a x^{2}+2 h x y+b y^{2}=0
$$

We have already seen that the lines represented by (1) are

$$
b y+x\left(h+\sqrt{h^{3}-a b}\right)=0
$$

and $\quad b y+x\left(h-\sqrt{h^{3}-a b}\right)=0$
Now slopes of (2) and (3) are respectively given by:

$$
m_{1}=\frac{-\left(h+\sqrt{h^{3}-a b}\right)}{b}, \text { and } m_{2}=\frac{-\left(h-\sqrt{h^{3}-a b}\right)}{b}
$$

Therefore, $m_{1}+m_{2}=\frac{-2 h}{b} \quad$ and $m_{1} m_{2} \quad \frac{a}{b}$
If $\theta$ is measure of the angle between the lines (2) and (3), then

$$
\tan \theta=\frac{m_{1}-m_{2}}{1+m_{1} m_{2}}=\sqrt{\frac{\left(m_{1}+m_{2}\right)^{2}-4 m_{1} m_{2}}{1+m_{1} m_{2}}} \cdot \frac{\sqrt{\frac{4 h^{3}-4 a}{b^{3}}-\frac{a}{b}}}{1+\frac{a}{b}} \cdot \frac{2 \sqrt{h^{3}-a b}}{a+b}
$$

The two lines are parallel, if $\theta=0$, so that $\tan \theta=0$ which implies $\boldsymbol{h}^{2}-\boldsymbol{a} \boldsymbol{b}=\mathbf{0}$, which is the condition for the lines to be coincident.
If the lines are orthogonal, then $\theta=90^{\circ}$, so that $\tan \theta$ is not defined. This implies $\boldsymbol{a}+\boldsymbol{b}=\mathbf{0}$. Hence the condition for (1) to represent a pair of orthogonal (perpendicular) lines is that sum of the coefficients of $\boldsymbol{x}^{\mathbf{2}}$ and $\boldsymbol{y}^{\mathbf{2}}$ is $\mathbf{0}$.

Example 1: Find measure of the angle between the lines represented by

$$
x^{2}-x y-6 y^{2}=0
$$

Solution. Here $a=1 ; \quad b=\frac{1}{2}, b \quad 6$

If $\theta$ is measure of the angle between the given lines, then

$$
\tan \theta=\frac{2 \sqrt{b^{2}-a b}}{a+b}=\frac{2 \sqrt{\frac{1+6}{4}}}{-5}=-1 \Rightarrow \theta=135^{\circ}
$$

Acute angle between the lines $=180^{\circ}-\theta=180^{\circ}-135^{\circ}=45^{\circ}$
Example2: Find a joint equation of the straight lines through the origin perpendicular to the lines represented by

$$
x^{2}+x y-6 y^{2}=0
$$

Solution: (1) may be written as

$$
(x-2 y)(x+3 y)=0
$$

Thus the lines represented by (1) are

$$
x-2 y=0
$$

and $\quad x+3 y=0$
The line through $(0,0)$ and perpendicular to (2) is

$$
y \Rightarrow 2 x \text { or } \quad+y \quad \nRightarrow x \quad 0
$$

Similarly, the line through $(0,0)$ and perpendicular to (3) is

$$
y=3 x-\text { or } \quad y \quad 3 x \quad 0
$$

Joint equation of the lines (4) and (5) is

$$
(y+2 x)(y-3 x)=0 \quad \text { or } \quad y^{2}-x y-6 x^{2}=0
$$

## EXERCISE 4.5

Find the lines represented by each of the following and also find measure of the, angle between them (Problems 1-6):

1. $10 x^{2}-23 x y-5 y^{2}=0$
2. $3 x^{2}+7 x y+2 y^{2}=0$
3. $9 x^{2}+24 x y+16 y^{2}=0$
4. $2 x^{2}+3 x y-5 y^{2}=0$
5. $6 x^{2}-19 x y+15 y^{2}=0$
6. $x^{2}+2 x y \sec \alpha+y^{2}=0$
7. Find a joint equation of the lines through the origin and perpendicular to the lines:

$$
x^{2}-2 x y \tan \alpha-y^{2}=0
$$

8. Find a joint equation of the lines through the origin and perpendicular to the lines:

$$
a x^{2}+2 b x y+b y^{2}=0
$$

9. Find the area of the region bounded by:

$$
10 x^{2}-x y-21 y^{2}=0 \text { and } \quad x+y+1=0
$$

# CHAPTER

## Linear Inequalities and Linear Programming

## 5.1 INTRODUCTION

Many real life problems involve linear inequalities. Here we shall consider those problems (relating to trade, industry and agriculture etc.) which involve systems of linear inequalities in two variables. Linear inequalities in such problems are used to prescribe limitations or restrictions on allocation of available resources (material, capital, machine capacities, labour hours, land etc.). In this chapter, our main goal will be to optimize (maximize or minimize) a quantity under consideration subject to certain restrictions.

The method under our discussion is called the linear programming method and it involves solutions of certain linear inequalities.

### 5.2 LINEAR INEQUALITIES

Inequalities are expressed by the following four symbols;
$>$ (greater than); < (less than); $\geq$ (greater than or equal to); $\leq$ (less than or equal to)
For example (i) $a x<b$ (ii) $a x+b \geq c$ (iii) $a x+b y>c$ (iv) $a x+b y \leq c$ are inequalities. Inequalities (i) and (ii) are in one variable while inequalities (iii) and (iv) are in two variables.

The following operations will not affect the order (or sense) of inequality while changing it to simpler equivalent form:
(i) Adding or subtracting a constant to each side of it.
(ii) Multiplying or dividing each side of it by a positive constant.

Note that the order (or sense) of an inequality is changed by multiplying or dividing its each side by a negative constant.

Now for revision we consider inequality, $x<\frac{3}{2}$
All real numbers $<\frac{3}{2}$ are in the solution set of (A).
Thus the interval $\left(-\infty, \frac{3}{2}\right)$ or $-\infty<x<\frac{3}{2}$ is the solution set of the
inequality (A) which is shown in the figure 5.21

$$
-5 \quad-4 \quad-3 \quad-2 \quad-1 \quad 0 \quad 1 \quad 2 \quad 3 \quad 4 \quad 5
$$

We conclude that the solution set of an inequality consists of all solutions of the inequality.

### 5.2.1 Graphing of A Linear Inequality in Two Variables

Generally a linear inequality in two variables $x$ and $y$ can be one of the following forms: $a x+b y<c ; \quad a x+b y>c ; \quad a x+b y \leq c ; \quad a x+b y \geq c$
where $a, b, c$ are constants and $a, b$ are not both zero.
We know that the graph of linear equation of the form
$a x+b y=c$ is a line which divides the plane into two disjoint regions as stated below:
(1) The set of ordered pairs $(x, y)$ such that $a x+b y<c$
(2) The set of ordered pairs $(x, y)$ such that $a x+b y>c$

The regions (1) and (2) are called half planes and the line $a x+b y=c$ is called the boundary of each half plane.

Note that a vertical line divides the plane into left and right half planes while a nonvertical line divides the plane into upper and lower half planes.

A solution of a linear inequality in $x$ and $y$ is an ordered pair of numbers which satisfies the inequality.

For example, the ordered pair $(1,1)$ is a solution of the inequality $x+2 y<6$ because $1+2(1)=3<6$ which is true.

There are infinitely many ordered pairs that satisfy the inequality $x+2 y<6$, so its graph will be a half plane.

Note that the linear equation $a x+b y=c$ is called "associated or corresponding equation" of each of the above mentioned inequalities.

## Procedure for Graphing a linear Inequality in two Variables

(i) The corresponding equation of the inequality is first graphed by using 'dashes' if the inequality involves the symbols $>$ or $<$ and a solid line is drawn if the inequality involves the symbols $\geq$ or $\leq$.
(ii) A test point (not on the graph of the corresponding equation) is chosen which determines that the half plane is on which side of the boundary line.

Example 1. Graph the inequality $x+2 y<6$.
Solution. The associated equation of the inequality

$$
\begin{aligned}
& x+2 y<6 \\
& \text { is } \quad x+2 y=6
\end{aligned}
$$

The line (ii) intersects the $x$-axis and $y$-axis at $(6,0)$ and $(0.3)$ respectively. As no point of the line (ii) is a solution $x^{*}$ of the inequality (i), so the graph of the line (ii) is shown by using dashes. We take $O(0,0)$ as a test point because it is not on the line (ii).

Substituting $x=0, y=0$ in the expression $x+2 y$ gives $0-2(0)=0<6$, so the point $(0,0)$ satisfies the inequality (i).

Any other point below the line (ii) satisfies the inequality (i), that is all points in the half plane containing the point $(0,0)$ satisfy the inequality (i).
Thus the graph of the solution set of inequality (i) is the a region on the origin-side of the line (ii), that is, the region below the line (ii). A portion of the open halfplane below ${ }^{x^{*}}$ the line (ii) is shown as shaded region in figure 5.22(a)

All points above the dashed line satisfy the inequality $x+2 y>6$
(ii)

A portion of the open half plane above the line (ii) is shown by shading in figure $5.22(b)$

Note: 1. The graph of the inequality $x+2 y \leq 6$.(iv) includes the graph of the line (ii),' so the open half-plane below the line (ii) including the graph of the line (ii) is the graph of the inequality (iv). A portion of the graph of the inequality (iv) is shown by shading in figure $5.22(b)$.
Note: 2 All points on the line (ii) and above the line (ii) satisfy the inequality $x+2 y \geq 6 \ldots$. (v). This means that the solution set of the inequality (v) consists of all points above the line (ii) and all points on the lines (ii). The graph of the inequality (v) is partially shown as shaded region in figure $5.22(d)$
Note: 3 that the graphs of
$x+2 y \leq 6$ and $x+2 y \geq 6$ are closed half planes.

Example 2. Graph the following linear inequalities in $x y$-plane;
(i) $2 x \geq-3$
(ii) $y \leq 2$

Solution. The inequality (i) in $x y$-plane is considered as $2 x+0 y \geq-3$ and its solution set consists of all point $(x, y)$
such that $x, y \in R$ and $x \geq-\frac{3}{2}$
The corresponding equation of the inequality (i) is $2 x=-3$
which a vertical line (parallel to the $y$-axis) and its graph is drawn in figure 5.23(a).
The graph of the inequality $2 x>-3$ is the open half plane to the right of the line (1).
Thus the graph of $2 x \geq-3$ is the closed half-plane to the right of the line (1).
(ii) The associated equation of the inequality (ii) is $y=2$
which is a horizontal line (parallel to the $x$-axis) and its $x^{*}$ graph is shown in figure 5.23(b) Here the solution set of the inequality $y<2$ is the open half plane below the boundary line $y=2$. Thus the graph of $y \leq 2$ consists of the boundary line and the open half plane below it.
Fig. 5.23(b)
Note that the intersection of graphs of 2x ≥ –3 and y ≤ 2 is partially shown in the adjoining figure 5.23(c).

### 5.3 REGION BOUNDED BY 2 OR 3 SIMULTANEOUS INEQUALITIES

The graph of a system of inequalities consists of the set of all ordered pairs (x, y) in the xy-plane which simultaneously satisfy all the inequalities in the system. Find the graph of such a system, we draw the graph of each inequality in the system on the same coordinate axes and then take intersection of all the graphs. The common region so obtained is called the solution region for the system of inequalities.

#### Example 1: Graph the system of inequalities

$$
x - 2y \leq 6
$$

$$
2x + y \geq 2
$$

#### Solution.

The graph of the line x – 2y = 6 is drawn by joining the point (6, 0) and (0, –3). The point (0, 0) satisfies the inequality x – 2y < 6 because 0 – 2(0) = 0 < 6. Thus the graph of x – 2y ≤ 6 is the upper half-plane including the graph of the line x – 2y = 6. The closed half-plane is partially shown by shading in figure 5.31(a).

#### Solution.

The graph of the line x – 2y = 6 is drawn by joining the point (6, 0) and (0, –3). The point (0, 0) satisfies the inequality x – 2y < 6 because 0 – 2(0) = 0 < 6. Thus the graph of x – 2y ≤ 6 is the upper half-plane including the graph of the line x – 2y = 6. The closed half-plane is partially shown by shading in figure 5.31(a).

#### *version: 1.1*

We draw the graph of the line 2x + y = 2 joining the points (1, 0) and (0, 2). The point (0, 0) does not satisfy the inequality 2x + y > 2 because 2(0) + 0 = 0 ≠ 2. Thus the graph of the inequality 2x + y ≥ 2 is the closed half-plane not on the origin-side of the line 2x + y = 2.

Thus the closed half-plane is shown partially as a shaded region in figure 5.31(b). The solution region of the given system of inequalities is the intersection of the graphs indicated in figures 5.31(a) and 5.31(b) and is shown as shaded region in figure 5.31(c).

The intersection point (2, – 2) can be found by solving the equations x – 2y = 6 and 2x + y = 2.

Note that the line x – 2y = 6 and 2x + y = 2 divide the xy-plane into four regions bounded by these lines. These four (bounded) regions are displayed in the adjoining figure.

Example 2. Graph the solution region for the following system of inequalities:

$$x - 2y \leq 6, \quad 2x + y > 2, \quad x + 2y \geq 10$$

Solution: The graph of the inequalities $x-2 y \leq 6$ and $2 x+y \geq 2$ have already drawn in figure 5.31(a) and 5.31(b) and their intersection is partially shown as a shaded region in figure 5.31(c) of the example 1 Art (5.3). Following the procedure of the example 1 of Art (5.3) the graph of the inequality $x+2 y \leq 10$ is shown partially in the figure 5.32(a).

The intersection of three graphs is the required solution region which is the shaded triangular region $P Q R$ (including its sides) shown partially in the figure 5.32(b).

Now we define a corner point of a solution region.

## DEFINITION:

A point of a solution region where two of its boundary lines intersect, is called a corner point or vertex of the solution region.

Such points play a useful role while solving linear programming problems. In example 2, the following three corner points are obtained by corresponding equations (of linear inequalities) given in the example 2(a) pairs.

|  Corresponding lines of inequalities: | Corner Points  |
| --- | --- |
|  $x-2 y=6, \quad 2 x+y=2$ | $P(2,-2)$  |
|  $x-2 y=6, \quad x+2 y=10$ | $Q(8,1)$  |
|  $2 x+y=2, \quad x+2 y=10$ | $R(-2,6)$  |

Example 3. Graph the following systems of inequalities.

|  (i) | $2 x+y \geq 2$ | (ii) | $2 x+y \geq 2$ | (iii) | $2 x+y \geq 2$  |
| --- | --- | --- | --- | --- | --- |
|   | $x+2 y \leq 10$ |  | $x+2 y \leq 10$ |  | $x+2 y \leq 10$  |
|   | $y \geq 0$ |  | $x \geq 0$ |  | $x \geq 0, y \geq 0$  |

## (i) The corresponding equations of the inequalities

$$ \begin{array}{llll} 2 x+y \geq 2 & \text { and } & x+2 y \leq 10 & \text { are } \ 2 x+y=2 & \text { (I) and } & x+2 y=10 & \text { (II) } \end{array} $$

For the partial graph of $2 x+y \geq 2$ see figure 5.31(b) of the example 1 and the graph of the inequality $x+2 y \leq 10$ is partially shown in figure 5.32(a) of the example 2.

The solution region of the inequalities $2 x+y \geq 2$ and $x+2 y \leq 10$ is the intersection of their individual graphs. The common region of the graphs of inequalities is partially shown as a shaded region in $x^{2}$ figure 5.33(a).

The graph of $y \geq 0$ is the upper half plane including the graph of the corresponding line $y=0$ (the $x$-axis) of the linear inequality $y \geq 0$. The graph of $y \geq 0$ is partially displayed in figure 5.33(b).

The solution region of the system of inequalities in (i) is the intersection of the graphs shown in figure 5.33(a) and 5.33(b). This solution region is displayed in figure 5.33(c).

(ii) See figure 5.33(a) for the graphs of the inequalities 2*x* + *y* ≥ 2 and *x* + 2*y* ≤ 10.

The graph of *x* ≥ 0 consists of the open half-plane to the right of the corresponding line *x* = 0 (*y*-axis) of the inequality *x* ≥ 0 and its graph. See figure 5.34(a).

Thus the solution region of the inequalities in (ii) is partially shown in figure 5.34(b). This region is the intersection of graphs in figure 5.33(a) and 5.34(a).

## **EXERCISE 5.1**

- **1. Graph the solution set of each of the following linear inequality in xy-plane:**
  - (i) 2*x* + *y* ≤ 6
  - (ii) 3*x* + 7*y* ≥ 21
  - (iii) 3*x* − 2*y* ≥ 6
  - (iv) 5*x* − 4*y* ≤ 20
  - (v) 2*x* + 1 ≥ 0
  - (vi) 3*y* − 4 ≤ 0
- **2. Indicate the solution set of the following systems of linear inequalities by shading:**
  - (i) 2*x* − 3*y* ≤ 6
  - (ii) *x* + *y* ≥ 5
  - (iii) 3*x* + 7*y* ≥ 21
  - 2*x* + 3*y* ≤ 12
  - −*y* + *x* ≤ 1
  - *x* − *y* ≤ 2
  - (iv) 4*x* − 3*y* ≤ 12
  - (v) 3*x* + 7*y* ≥ 21
  - (*x*) 3*x* + 7*y* ≥ 21
  - (*y*) 3*x* + 7*y* ≥ 21
  - (*x*) 3*x* + 7*y* ≥ 21
  - (*y*) 3*x* − 3*y* ≥ 4
- **3. Indicate the solution region of the following systems of linear inequalities by shading:**
  - (i) 2*x* − 3*y* ≤ 6
  - (ii) *x* + *y* ≤ 5
  - (iii) *x* + *y* ≥ 5
  - 2*x* + 3*y* ≤ 12
  - *y* − 2*x* ≤ 2
  - *x* − *y* ≥ 1
  - *y* ≥ 0
  - (iv) 3*x* + 7*y* ≤ 21
  - (v) 3*x* + 7*y* ≤ 21
  - (vi) 3*x* + 7*y* ≤ 21
  - (vii) 3*x* + 7*y* ≤ 21
  - 2*x* − *y* ≥ −3
  - *x* ≥ 0
  - (*y*) ≥ 0
  - (*x*) ≥ 0

*version: 1.1*

4. Graph the solution region of the following system of linear inequalities and find the corner points in each case.
(i) $2 x-3 y \leq 6$
(ii) $x+y \leq 5$
(iii) $3 x+7 y \leq 21$
$2 x+3 y \leq 12$
$-2 x+y \leq 2$
$2 x-y \leq-3$
$x \geq 0$
$y \geq 0$
$y \geq 0$
(iv) $3 x+2 y \geq 6$
(v) $5 x+7 y \leq 35$
(vi) $5 x+7 y \leq 35$
$x+3 y \leq 6$
$-x+3 y \leq 3$
$x-2 y \leq 2$
$y \geq 0$
$x \geq 0$
$x \geq 0$
5. Graph the solution region of the following system of linear inequalities by shading.
(i) $3 x-4 y \leq 12$
(ii) $3 x-4 y \leq 12$
(iii) $2 x+y \leq 4$
$3 x+2 y \geq 3$
$x+2 y \leq 6$
$2 x-3 y \geq 12$
$x+2 y \leq 9$
$x+y \geq 1$
$x+2 y \leq 6$
(iv) $2 x+y \leq 10$
(v) $2 x+3 y \leq 18$
(vi) $3 x-2 y \geq 3$
$x+y \leq 7$
$2 x+y \leq 10$
$x+4 y \leq 12$
$-2 x+y \leq 4$
$-2 x+y \leq 2$
$3 x+y \leq 12$

### 5.4 PROBLEM CONSTRAINTS

In the beginning we described that linear inequalities prescribe limitations and restrictions on allocation of available sources. While tackling a certain problem from every day life each linear inequality concerning the problem is named as problem constraint. The system of linear inequalities involved in the problem concerned are called problem constraints. The variables used in the system of linear inequalities relating to the problems of every day life are non-negative and are called non-negative constraints. These nonnegative constraints play an important role for taking decision. So these variables are called decision variables.

### 5.5 Feasible solution set

We see that solution region of the inequalities in example 2 of Art 5.3 is not within the first quadrant. If the nonnegative constraints $x \geq 0$ and $y \geq 0$ are included with the system of inequalities given in the example 2, then the solution region is restricted to the first quadrant.

It is the polygonal region $A B C D E$ (including its sides) as shown in the figure 5.51.

Such a region (which is restricted to the first quadrant) is referred to as a feasible region for the set of given constraints. Each point of the feasible region is called a feasible solution of the system of linear inequalities (or for the set of a given constraints). A set consisting of all the feasible solutions of the system of linear inequalities is called a feasible solution set.

Example 1. Graph the feasible region and find the corner points for the following system of inequalities (or subject to the following constraints).

$$
\begin{aligned}
& x-y \leq 3 \\
& x+2 y \leq 6 \\
& x \geq 0, \quad y \geq 0
\end{aligned}
$$

Solution: The associated equations for the inequalities

$$
\begin{aligned}
& x-y \leq 3 \quad \text { (i) } \quad \text { and } x+2 y \leq 6 \quad \text { (ii) } \\
& \text { are } x-y=3 \quad \text { (1) and } x+2 y=6 \quad(2)
\end{aligned}
$$

As the point $(3,0)$ and $(0,-3)$ are on the line (1), so the graph of $x-y=3$ is drawn by joining the points $(3,0)$ and $(0,-3)$ by solid line.

Similarly line (2) is graphed by joining the points $(6,0)$ and $(0,3)$ by solid line. For $x=0$ and $y=0$, we have;

$$
0-0=0 \leq 3 \text { and } 0+2(0)=0 \leq 6
$$

so both the closed half-planes are on the origin sides of the lines (1) and (2). The intersection of these closed half-planes is partially displayed as shaded region in figure 5.52(a).

For the graph of *y* ≥ 0, see figure 5.33(b) of the example 3 of art 5.3.

The intersection of graphs shown in figures 5.52(a) and 5.33(b) is partially graphed as shaded region in figure 5.52(b).

The graph of *x* ≥ 0 is drawn in figure 5.34(a). The intersection of the graphs shown in figures 5.52(a) and 5.34(a) is graphed in figure 5.52(c).

Finally the graph of the given system of linear inequalities is displayed in figure 5.52(d) which is the feasible region for the given system of linear inequalities. The points (0, 0), (3, 0), (4, 1) and (0, 3) are corner points of the feasible region.

*version: 1.1*

**Example 2.** A manufacturer wants to make two types of concrete. Each bag of Agrade concrete contains 8 kilograms of gravel (small pebbles with coarse sand) and 4 kilograms of cement while each bag of B-grade concrete contains 12 kilograms of gravel and two kilograms of cement. If there are 1920 kilograms of gravel and 480 kilograms of cement, then graph the feasible region under the given restrictions and find corner points of the feasible region.

**Solution:** Let *x* be the number of bags of A-grade concrete produced and *y* denote the number of bags of B-grade concrete produced, then 8*x* kilograms of gravel will be used for A-grade concrete and 12*y* kilograms of gravel will be required for B-grade concrete so 8*x* + 12*y* should not exceed 1920, that is,

$$8x + 12y \leq 1920$$

Similarly, the linear constraint for cement will be

$$4x + 2y \leq 480$$

Now we have to graph the feasible region for the linear constraints

$$8x + 12y \leq 1920$$
$$4x + 2y \leq 480, \quad x \geq 0, \quad y \geq 0$$

Taking the one unit along *x*-axis and *y*-axis equal to 40 we draw the graph of the feasible region required.

The shaded region of figure 5.53(a) shows the graph of 8*x* + 12*y* ≤ 1920 including the nonnegative constraints *x* ≥ 0 and *y* ≥ 0.

In the figure 5.53(b), the graph of 4*x* + 2*y* ≤ 480 including the nonnegative constraints *x* ≥ 0 and *y* ≥ 0 is displayed as shaded region.

The intersection of these two graphs is shown as shaded region in figure 5.53(c), which is the feasible region for the given linear constraints.

The point (0, 0), (120, 0), (60, 120) and (0, 160) are the corner points of the feasible region.

**Example 3. Graph the feasible regions subject to the following constraints.**

(a) $$2x - 3y \leq 6$$
(b) $$2x - 3y \leq 6$$
$$2x + y \geq 2$$
$$2x + y \geq 2$$
$$x \geq 0, y \geq 0$$

$$2x + y \geq 2$$

$$x + 2y < 8, \quad x \geq 0, \quad y \geq 0$$

**Solution:** The graph of $$2x - 3y \leq 6$$ is the closed half-plane on the origin side of $$2x - 3y = 6$$. The portion of the graph of system $$2x - 3y \leq 6$$,

$$x \geq 0, \quad y \geq 0$$

is shown as shaded region in figure 5.54(a).

*version: 1.1*

The graph of $$2x + y \geq 2$$ is the closed half-plane not on the origin side of $$2x + y = 2$$. The portion of the graph of the system $$2x + y \geq 2$$,

$$x \geq 0, y \geq 0$$

is displayed as shaded region in figure 5.54(b).

The graph of the system

$$2x - 3y \leq 6, \quad 2x + y \leq 2,$$
$$x \geq 0, \quad y \geq 0$$

is the intersection of the graphs shown in figures 5.54(a) and 5.54(b) and it is partially displayed in figure 5.54(c) as shaded region.

(b) The graph of system $$x + 2y \leq 8, \quad x \geq 0, \quad y \geq 0$$ is a triangular region indicated in figure 5.45(d).

Thus the graph of the system

$$2x - 3y \leq 6$$
$$2x + y \geq 2$$
$$x + 2y \leq 8$$
$$x \geq 0, y \geq 0$$

is the intersection of the graphs shown in figures 5.54(c) and 5.54(d). It is the shaded region indicated in the figure 5.54(e).

**Note:** The corner points of feasible region the set of constraints in (a) are (1, 0), (3, 0) and (0, 2) while the corner points of the feasible region for the set of constraints in (b) are (1, 0):

$$(3, 0) \left( \frac{16}{7} \cdot \frac{10}{7} \right), (0, 4) \text{ and } (0, 2)$$

We see that the feasible solution regions in example 3(a) and 3(b) are of different types. The feasible region in example 3(a) is unbounded as it cannot be enclosed in any circle how large it may be while the feasible region in example 3(b) can easily be enclosed within a circle, so it is bounded. If the line segment obtained by joining any two points of a region lies entirely within the region, then the region is called **convex**.

Both the feasible regions of example 3(a) and 3(b) are convex but the regions such as shown in the adjoining figures are not convex.

## **EXERCISE 5.2**

**1. Graph the feasible region of the following system of linear inequalities and find the corner points in each case.**

(i) $$2x - 3y \leq 6$$ (ii) $$x + y \leq 5$$ (iii) $$x + y \leq 5$$ $$2x + 3y \leq 12$$ $$-2y + y \leq 2$$ $$x \geq 0, y \geq 0$$ $$x \geq 0, y \geq 0$$ (iv) $$3x + 7y \leq 21$$ (v) $$3x + 2y > 6$$ $$x - y \leq 3$$ $$x + y \leq 4$$ $$x \geq 0, y \geq 0$$ $$x \geq 0, y \geq 0$$ (vi) $$5x + 7y \leq 35$$ $$x - 2y \leq 4$$ $$x \geq 0, y \geq 0$$

**2. Graph the feasible region of the following system of linear inequalities and find the corner points in each case.**

(i) $$2x + y \leq 10$$ (ii) $$2x + 3y \leq 18$$ (iii) $$2x + 3y \leq 18$$ $$x + 4y \leq 12$$ $$x + 2y \leq 10$$ $$x + 4y \leq 12$$ $$x \geq 0, y \geq 0$$ $$x \geq 0, y \geq 0$$ (iv) $$x + 2y \leq 14$$ (v) $$x + 3y \leq 15$$ (vi) $$2x + y \leq 20$$ $$3x + 15y \leq 120$$ $$x + y \leq 11$$ $$x \geq 0, y \geq 0$$

## **5.6 LINEAR PROGRAMMING**

A function which is to be maximized or minimized is called an **objective function**. Note that there are infinitely many feasible solutions in the feasible region. The feasible solution which maximizes or minimizes the objective function is called the **optimal solution**. The theorem of linear programming states that the maximum and minimum values of the objective function occur at corner points of the feasible region.

#### **Procedure for determining optimal solution:**

(i) Graph the solution set of linear inequality constraints to determine feasible region.

(ii) Find the corner points of the feasible region.

(iii) Evaluate the objective function at each corner point to find the optimal solution.

**Example 1.** Find the maximum and minimum values of the function defined as:

$$f(x, y) = 2x + 3y \qquad \text{subject to the constraints;}$$

$$x - y \leq 2 \qquad x + y \leq 4 \qquad 2x - y \leq 6, \quad x \geq 0$$

**Solution.** The graphs of $$x - y \leq 2$$ is the closed half plane on the origin side of $$x - y = 2$$ and the graph of $$x + y \leq 4$$ is the closed half-plane not on the origin side of $$x + y = 4$$. The graph of the system

$$x - y \leq 2, x + y \geq 4$$

*version: 1.1*

*version: 1.1*

including the non-negative constraints *x* ≥ 0 is partially displayed as shaded region in the figure 5.61. The graph of 2*x* − *y* ≤ 6 consists of the graph of the line 2*x* − *y* = 6 and the half plane on the origin side of the line 2*x* − *y*=6. A portion of the solution region of the given system of inequalities is shaded in the figure 5.62.

We see that feasible region is unbounded upwards and its corner points are *A*(0, 4), *B*(3, 1) and *C*(4, 2). Note that the point at which the lines *x* + *y* = 4 and 2*x* − *y* = 6 intersect is not a corner point of the feasible region.

It is obvious that the expression 2*x* + 3*y* does not possess a maximum value in the feasible region because its value can be made larger than any number by increasing *x* and *y*. We calculate the values of *f* at the corner points to find its minimum value:

$$
\begin{array}{rcl}
f(0, 4) & = & 2(0) + 3 \times 4 & = & 12 \\
f(3, 1) & = & 2 \times 3 + 3 \times 1 & = & 6 + 3 = 9 \\
f(4, 2) & = & 2 \times 4 + 3 \times 2 & = & 8 + 6 = 14
\end{array}
$$

Thus the minimum value of 2*x* + 3*y* is 9 at the corner point (3, 1).

**Notes:** If *f*(*x*, *y*) = 2*x* + 3*y*, then *f*(0, 4) = 2*x* 0 + 2*x* 4 = 8, *f*(3, 1) = 2*x* 3 + 2*x* 4 = 6 + 2 = 9 and (4, 2) = 2*x* 4 + 2*x* 2 = 8 + 4 = 12. The minimum value of 2*x* + 3*y* is the same, at two corner points (0, 4) and (3, 1).

We observe that the minimum value of 2*x* + 2*y* at each point of the line segment *AB* is 8 as:

$$
\begin{array}{rcl}
f(x, y) & = & 2x + 2(4 - x) \quad (\because \quad x + y = 4 \Rightarrow y = 4 - x) \\
& = & 2x + 8 - 2x = 8
\end{array}
$$

**Example 2.** Find the minimum and maximum values of *f* and *φ* defined as:

$$
f(x, y) = 4x + 5y, \qquad \phi(x, y) = 4x + 6y
$$

under the constraints

$$
2x - 3y \leq 6 \qquad 2x + y \geq 2 \qquad 2x + 3y \leq 12 \qquad x \geq 0, \quad y \geq 0
$$

**Solution.** The graphs of 2*x* − 3*y* ≤ 6, 2*x* + *y* ≥ 2, are displayed in the example 3 of Art. 5.5. Joining the points (6, 0) and (0, 4), we obtain the graph of the line 2*x* + 3*y* = 12. As 2(0) + 3(0) = 0 < 12, so the graph of 2*x* + 3*y* < 12 is the half plane below the line 2*x* + 3*y* = 12. Thus the graph of 2*x* + 3*y* ≤ 12 consists of the graph of the line 2*x* + 3*y* = 12 and the half plane below the line 2*x* + 3*y* = 12. The solution region of 2*x* − 3*y* ≤ 6, 2*x* + *y* ≥ 2 and 2*x* + 3*y* ≤ 12 is the triangular region *PQR* shown in figure 5.63. The non-negative constraints *x* ≥ 0, *y* ≥ 0 indicated the first quadrant. Thus the feasible region satisfying all the constraints is shaded in the figure 5.63 and its corner points are (1, 0), (0, 2), (0, 4), (9, 2, 1) and (3, 0).

We find values of *f* at the corner points.

|  Corner point | *f*(*x*, *y*) = 4*x* + 5*y*  |
| --- | --- |
|  (1, 0) | *f*(1, 0) = 4 *x* 1 + 5.0 = 4  |
|  (0, 2) | *f*(0, 2) = 4 *x* 0 + 5.2 = 10  |
|  (0, 4) | *f*(0, 4) = 4 *x* 0 + 5.4 = 20  |
|  (9/2, 1) | *f*(9/2, 1) = 4 *x* 9/2 + 5.1 = 23  |
|  (3, 0) | *f*(3, 0) = 4 *x* 3 + 5.0 *x* 0 = 12  |

From the above table, it follows that the minimum value of *f* is 4 at the corner point (1, 0) and maximum value of *f* is 23 at the corner point (9, 2, 1). The values of *φ* at the corner points are given below in tabular form.

|  Corner point | *φ*(*x*, *y*) = 4*x* + 5*y*  |
| --- | --- |
|  (1, 0) | *φ*(1, 0) = 4.1 + 6.0 = 4  |
|  (0, 2) | *φ*(0, 2) = 4.0 + 6.2 = 12  |
|  (0, 4) | *φ*(0, 4) = 4.0 + 6.4 = 24  |
|  (9/2, 1) | *φ*(9/2, 1) = 4.9/2 + 6.1 = 24  |
|  (3, 0) | *φ*(3, 0) = 4 *x* 3 + 6.0 = 12  |

The minimum value of *φ* is 4 at the point (1, 0) and maximum value of *φ* is 24 at the corner points (0, 4) and (9, 2, 1). As observed in the above example, it follows that the function *φ* has maximum value at all the points of the line segment between the points

(0, 4) and $\left(\frac{9}{3}, 1\right)$.

Note 1. Some times it may happen that each point of constraint line gives the optimal value of the objective function.

Note 2. For different value of $k$, the equation $4 x+5 y=k$ represents lines parallel to the line $4 x+5 y=0$. For a certain admissible value of $k$, the intersection of $4 x+5 y=k$ with the feasible region gives feasible solutions for which the profit is $k$.

### 5.7 LINEAR PROGRAMMING PROBLEMS

Convert a linear programming problem to a mathematical form by using variables, then follow the procedure given in Art 5.6.

Example 1: A farmer possesses 100 canals of land and wants to grow corn and wheat. Cultivation of corn requires 3 hours per canal while cultivation of wheat requires 2 hours per canal. Working hours cannot exceed 240. If he gets a profit of Rs. 20 per canal for corn and Rs. 15/- per canal for wheat, how many canals of each he should cultivate to maximize his profit?

Solution: Suppose that he cultivates $x$ canals of corn and $y$ canals of wheat. Then constraints can be written as:

$$ \begin{aligned} & x+y \leq 100 \ & 3 x+2 y \leq 240 \end{aligned} $$

Non-negative constraints are $x \geq 0, y \geq 0$. Let $P(x, y) x^{*}$ be the profit function, then

$$ P(x, y)=20 x+15 y $$

Now the problem is to maximize the profit function $P$ under the given constraints. Graphing the inequalities, we obtain the feasible region which is shaded in the figure 5.71. Solving the equations $x+y=100$ and $3 x+2 y=240$ gives $x=240-2(x+y)=240-200=40$ and $y=100-40=60$, that is; their point of intersection is $(40,60)$. The corner points of the feasible region are $(0,0),(0,100),(40,60)$ and $(80,0)$. Now we find the values of $P$ at the corner points.

|  Corner point | $P(x, y)=20 x+15 y$  |
| --- | --- |
|  $(0,0)$ | $P(0,0)=20 \times 0+15 \times 0=0$  |
|  $(0,100)$ | $P(0,100)=20 \times 0+15 \times 100=1500$  |
|  $(40,60)$ | $P(40,60)=20 \times 40+15 \times 60=1700$  |
|  $(80,0)$ | $P(80,0)=20 \times 80+15 \times 0=1600$  |

From the above table, it follows that the maximum profit is Rs. 1700 at the corner point $(40,60)$. Thus the farmer will get the maximum profit if he cultivates 40 canals of corn and 60 canals of wheat.

Exam ple 2. A factory produces bicycles and motorcycles by using two machines $A$ and B. Machine $A$ has at most 120 hours available and machine $B$ has a maximum of 144 hours available. Manufacturing a bicycle requires 5 hours in machine $A$ and 4 hours in machine $B$ while manufacturing of a motorcycle requires 4 hours in machine $A$ and 8 hours in machine $B$. If he gets profit of Rs. 40 per bicycle and profit of Rs. 50 per motorcycle, how many bicycles and motorcycles should be manufactured to get maximum profit?

Solution: Let the number of bicycles to be manufactured be $x$ and the number of motor cycles to be manufactured be $y$.

Then the time required to use machine $A$ for $x$ bicycles and $y$ motorcycles is $5 x+4 y$ (hours) and the time required to use machine $B$ for $x$ bicycles and $y$ motorcycles in $4 x+8 y$ (hours). Thus the problem constraints are $5 x+4 y \leq 120$

$$ \begin{array}{ll} \text { And } & 4 x+8 y \leq 144 \ \Rightarrow & 2 x+4 y \leq 72 \end{array} $$

Since the numbers of articles to be produced cannot be negative, so $x \geq 0, y \geq 0$. Let $P(x, y)$ be the profit function, then $P(x, y)=40 x+50 y$. Now the problem is to maximize $P$ subject to the constraints:

$$
\begin{aligned}
& 5 x+4 y \leq 120 \\
& 2 x+4 y \leq 72 \quad ; \quad x \geq 0, y \geq 0
\end{aligned}
$$

Solving $5 x+4 y=120$ and $2 x+4 y=72$, gives $3 x=48 \Rightarrow x=16$ and $4 y=72-2 x=72-32=40 \Rightarrow y=10$.

Thus their point of intersection is $(16,10)$. Graphing the linear inequality constraints, the feasible region obtained is depicted in the figure 5.72 by shading. The corner points of the feasible region are $(0,0),(0,18),(16,10)$ and $(24,0)$. Now we find the values of $P$ at the corner points.

|  Corner point | $P(x, y)=40 x+50 y$  |
| --- | --- |
|  $(0,0)$ | $P(0,0)=40 \times 0+50 \times 0=0$  |
|  $(0,18)$ | $P(0,18)=40 \times 0+50 \times 18=900$  |
|  $(16,10)$ | $P(16,10)=40 \times 16+50 \times 10=1140$  |
|  $(24,0)$ | $P(24,0)=40 \times 24+50 \times 0=960$  |

From the above table, it follows, that the maximum profit is Rs. 1140 at the corner point $(16,10)$. Manufacturer gets the maximum profit if he manufactures 16 bicycles and 10 motorcycles.

## EXERCISE 5.3

1. Maximize $f(x, y)=2 x+5 y$ subject to the constraints $2 y-x \leq 8 ; \quad x-y \leq 4 ; \quad x \quad 0 \geq 0 ; \quad y \geq 0$
2. Maximize $f(x, y)=x+3 y$ subject to the constraints $2 x+5 y \leq 30 ; \quad 5 x+4 y \leq 20 ; \quad x \geq 0 ; \quad y \geq 0$
3. Maximize $z=2 x+3 y$; subject to the constraints: $3 x+4 y \leq 12 ; \quad 2 x+y \leq 4 ; \quad 4 x-y \leq 4 ; x \geq 0 ; y \geq 0$
4. Minimize $z=2 x+y$ : subject to the constraints: $x+y \geq 3 ; \quad 7 x+5 y \leq 35 ; \quad x \geq 0 ; \quad y \geq 0$
5. Maximize the function defined as; $f(x, y)=2 x+3 y$ subject to the constraints: $2 x+y \leq 8 ; \quad x+2 y \leq 14 ; \quad x \geq 0 ; \quad y \geq 0$
6. Minimize $z=3 x+y$; subject to the constraints: $3 x+5 y \geq 15 ; \quad x+6 y \geq 9 ; \quad x \geq 0 ; \quad y \geq 0$
7. Each unit of food $X$ costs Rs. 25 and contains 2 units of protein and 4 units of iron while each unit of food $Y$ costs Rs. 30 and contains 3 units of protein and 2 unit of iron. Each animal must receive at least 12 units of protein and 16 units of iron each day. How many units of each food should be fed to each animal at the smallest possible cost?
8. A dealer wishes to purchase a number of fans and sewing machines. He has only Rs. 5760 to invest and has space atmost for 20 items. A fan costs him Rs. 360 and a sewing machine costs Rs. 240. His expectation is that the can sell a fan at a profit of Rs. 22 and a sewing machine at a profit of Rs. 18. Assuming that he can sell all the items that he can buy, how should he invest his money in order to maximize his profit?
9. A machine can produce product $A$ by using 2 units of chemical and 1 unit of a compound or can produce product $B$ by using 1 unit of chemical and 2 units of the compound. Only 800 units of chemical and 1000 units of the compound are available. The profits per unit of $A$ and $B$ are Rs. 30 and Rs. 20 respectively, maximize the profit function.