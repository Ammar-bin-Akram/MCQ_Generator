# Chapter 22: Vectors in Space

## INTRODUCTION

In this unit, we will look into the rectangular coordinate system in three-dimensional space and explore the fundamental mathematical operations involving vectors in space. We will begin by understanding the dot product (or scalar product) and the cross product (or vector product) of two vectors and learn about their geometric interpretation. Further, we emphasize their practical applications. For example, we will see how these concepts can be used to calculate the area of a triangle and the area of a parallelogram. Finally, we will explore the extensive use of vectors in three-dimensional space, particularly in physics, where they play an important role in determining forces, velocities, and other essential physical quantities. For example, determining the work done by a constant force when moving an object along a specified vector.

### 14.1 Vectors (Recall)

In previous classes, we learned about two fundamental quantities: scalars and vectors. A scalar is a quantity that has only magnitude or size, such as mass, time, density, temperature, length, volume, speed, work etc. On the other hand, a vector is a quantity that has both magnitude and direction, for example displacement, velocity, acceleration, weight, force, momentum, electric and magnetic fields, etc.
Geometrically, a vector is represented as a directed line segment $\overrightarrow{A B}$ with $A$ as its initial point and $B$ as the terminal point.
In two-dimension $\left(R^{2}\right)$ a vector has components that can be represented by an ordered pair $[x, y]$ of real numbers. For the vector $\underline{u}=[x, y], x$ and $y$ represent the components of $\underline{u}$.
Addition of Vectors: For any two vectors $\underline{u}=\left[x_{1}, y_{1}\right]$ and $\underline{y}=\left[x_{2}, y_{2}\right]$, we have

$$
\underline{u}+\underline{y}=\left[x_{1}, y_{1}\right]+\left[x_{2}, y_{2}\right]=\left[x_{1}+x_{2}, y_{1}+y_{2}\right]
$$

Scalar Multiplication of a Vector: For $\underline{u}=[x, y]$ and $a \in R$, we have

$$
a \underline{u}=a[x, y]=[a x, a y]
$$

Equal Vectors: Two vectors $\underline{u}=\left[x_{1}, y_{1}\right]$ and $\underline{y}=\left[x_{2}, y_{2}\right]$ of $R^{2}$ are said to be equal

if and only if they have the same components. That is, $\left[x_{1}, y_{1}\right]=\left[x_{2}, y_{2}\right]$ if and only if $x_{1}=x_{2}$ and $y_{1}=y_{2}$ and we write $\underline{u}=\underline{v}$
In other words, two vectors $\underline{u}$ and $\underline{v}$ are said to be equal, if they have same magnitude and same direction.
Parallel Vectors: Two vectors are parallel if and only if they are non-zero scalar multiple of each other.
For example, vectors $\overrightarrow{A B},-\overrightarrow{A B}$ and $\frac{3}{2} \overrightarrow{A B}$ are parallel.

# Magnitude of a Vector

The magnitude (or norm or length) of a vector in 2D represents the length of the vector from the origin to the point represented by the vector. For any vector $\underline{u}=[x, y]$ in $R^{2}$, we define the magnitude, as the distance of the point $P(x, y)$ from the origin $O$.

Magnitude of $\overrightarrow{O P}=|\overrightarrow{O P}|=|\underline{u}|=\sqrt{x^{2}+y^{2}}$
Now, we will learn some mathematical operations involving vectors in three-dimensional space.

### 14.1.1 Rectangular Coordinate System in Space

In space a rectangular coordinate system is constructed using three mutually orthogonal (perpendicular) axes, which have origin as their common point of intersection. When sketching figures, we follow the convention that the positive $x$-axis points towards the reader, the positive $y$-axis to the right and the positive $z$-axis points upwards.
These axes are also labeled in accordance with the righthand rule. The fingers of the right hand, pointing in the direction of the positive $x$-axis, curled images toward the positive $y$-axis, and the thumb will point in the direction of the positive $z$-axis. A point $P$ in space has three coordinates, one along $x$-axis, the second along $y$-axis and the third along $z$-axis. If the
Right hand rule

# Unit 44 Vectors in Space

directed distances along $x$-axis, $y$-axis and $z$-axis respectively are $a, b$ and $c$, then the point $P$ is written with a unique triple of real numbers as $P(a, b, c)$ (see figure).

### 14.1.2 Concept of a Vector in Space

The set $R^{3}=\{(x, y, z): x, y, z \in R\}$ is called 3-dimensional space. An element $(x, y, z)$ of $R^{3}$ represents a point $P(x, y, z)$, which is uniquely determined by its coordinates $x, y$ and $z$. Given a vector $\underline{u}$ in space, there exists a unique point $P(x, y, z)$ in space such that the vector $\overrightarrow{O P}$ is equal to $\underline{u}$ (see figure). Now each element $(x, y, z) \in R^{3}$ is associated with a unique ordered triple $(x, y, z)$, which represents the vector $\underline{u}=\overrightarrow{O P}=[x, y, z]$.

### 14.1.3 Fundamental Mathematical Operations for Vectors in Space

We define addition and scalar multiplication in $R^{3}$ by:
(i) Addition of Vectors: For any two vectors $\underline{u}=[x, y, z]$ and $\underline{y}=\left[x^{\prime}, y^{\prime}, z^{\prime}\right]$ we have $\underline{u}+\underline{v}=[x, y, z]+\left[x^{\prime}, y^{\prime}, z^{\prime}\right]=\left[x+x^{\prime}, y+y^{\prime}, z+z^{\prime}\right]$
(ii) Scalar Multiplication of a Vector: For $\underline{u}=[x, y, z]$ and $a \in R$, we have $a \underline{u}=a[x, y, z]=[a x, a y, a z]$
The set of all ordered triples $[x, y, z]$ of real numbers, together with the rules of addition and scalar multiplication is called the set of vectors in $R^{3}$. For the vector $\underline{u}=[x, y, z], x, y$ and $z$ are called the components of $\underline{u}$. The definition of vectors in $R^{3}$ states that vector addition and scalar multiplication are to be carried out also for vectors in space just as for vectors in the plane. Similarly, we define in $R^{3}$ :
(a) The negative of the vector $\underline{u}=[x, y, z]$ as $-\underline{u}=(-1) \underline{u}=[-x,-y,-z]$
(b) The difference of two vectors $\underline{y}=\left[x^{\prime}, y^{\prime}, z^{\prime}\right]$ and $\underline{w}=\left[x^{\prime \prime}, y^{\prime \prime}, z^{\prime \prime}\right]$ as

$$
\underline{v}-\underline{w}=\underline{v}+(-\underline{w})=\left[x^{\prime}-x^{\prime \prime}, y^{\prime}-y^{\prime \prime}, z^{\prime}-z^{\prime \prime}\right]
$$

(c) The zero vector as $O=[0,0,0]$
(d) Equality of two vectors: Two vectors $\underline{y}=\left[x^{\prime}, y^{\prime}, z^{\prime}\right]$ and $\underline{w}=\left[x^{\prime \prime}, y^{\prime \prime}, z^{\prime \prime}\right]$ are equal that is $\underline{v}=\underline{w}$ if and only if $x^{\prime}=x^{\prime \prime}, y^{\prime}=y^{\prime \prime}$ and $z^{\prime}=z^{\prime \prime}$.
(e) Position Vector

For any point $P(x, y, z)$ in $R^{3}$, a vector $\underline{u}=[x, y, z]$ is represented by a directed line segment $\overrightarrow{O P}$, whose initial point is at origin. Such vectors are called position vectors in $R^{3}$.

# 14.1.4 Magnitude of a Vector in Space

We define the magnitude, norm, or length of a vector $\underline{u}=[x, y, z]$ in space by the distance of the point $P(x, y, z)$ from the origin $O$.

$$
\therefore \quad \overrightarrow{O P}=|u|=\sqrt{x^{2}+y^{2}+z^{2}}
$$

Example 1 For the vectors, $\underline{u}=[1,-2,3], \underline{y}=[2,1,3]$ and $\underline{w}=[-1,4,0]$, find the following:
(i) $\underline{y}+\underline{w}$
(ii) $2 \underline{w}$
(iii) $|u|$
(iv) $|\underline{v}-2 \underline{w}|$
(v) $|2 \underline{u}-\underline{y}+3 \underline{w}|$

Solution (i) $\underline{y}+\underline{w}=[2-1,1+4,3+0]=[1,5,3]$
(ii) $2 \underline{w}=2[-1,4,0]=[-2,8,0]$
(iii) $|u|=[1,-2,3]=\sqrt{(1)^{2}+(-2)^{2}+(3)^{2}}=\sqrt{1+4+9}=\sqrt{14}$
(iv) $|\underline{v}-2 \underline{w}|=|[2+2,1-8,3-0]|=|[4,-7,3]|$

$$
=\sqrt{(4)^{2}+(-7)^{2}+(3)^{2}}=\sqrt{16+49+9}=\sqrt{74}
$$

(v) $|2 \underline{u}-\underline{y}+3 \underline{w}|=|2[1,-2,3]-[2,1,3]+3[-1,4,0]|=|[2,-4,6]-[2,1,3]+[-3,12,0]|$

$$
=[-3,7,3]=\sqrt{(-3)^{2}+(7)^{2}+(3)^{2}}=\sqrt{9+49+9}=\sqrt{67}
$$

### 14.1.5 Components of a Vector

As in plane, we introduce three special vectors $i=[1,0,0]$, $j=[0,1,0]$ and $k=[0,0,1]$ in $R^{3}$

As magnitude of $i=\sqrt{1^{2}+0^{2}+0^{2}}=1$
magnitude of $j=\sqrt{0^{2}+1^{2}+0^{2}}=1$ and
magnitude of $k=\sqrt{0^{2}+0^{2}+1^{2}}=1$. So, $i, j$
and $k$ are called unit vectors along $x$-axis, $y$-axis and $z$-axis respectively. Using the definition of addition and scalar multiplication, the vector $[x, y, z]$ can be written as:

$$
\begin{aligned}
\underline{u}=[x, y, z] & =[x, 0,0]+[0, y, 0]+[0,0, z] \\
& =x[1,0,0]+y[0,1,0]+z[0,0,1]=x i+y j+z k
\end{aligned}
$$

Thus, each vector $[x, y, z]$ in $R^{3}$ can be uniquely represented by $x i+y i+z k$.

## Unit Vector

A unit vector is defined as a vector whose magnitude is unity. In three-dimensional space the unit vector of the vector $\underline{u}=x i+y j+z k$ is written as $\hat{u}$ (read as $u$ hat) and

is defined by

$$
\hat{u}=\frac{u}{|u|}=\frac{x}{\sqrt{x^{2}+y^{2}+z^{2}}} i+\frac{y}{\sqrt{x^{2}+y^{2}+z^{2}}} j+\frac{z}{\sqrt{x^{2}+y^{2}+z^{2}}} k
$$

In terms of unit vector $i, j$, and $k$, the sum $u+y$ of two vectors.
$\underline{u}=\left[x_{1}, y_{1}, z_{1}\right]$ and $y=\left[x_{2}, y_{2}, z_{2}\right]$ is written as:

$$
\begin{aligned}
\underline{u}+\underline{v} & =\left[x_{1}+x_{2}, y_{1}+y_{2}, z_{1}+z_{2}\right] \\
& =\left(x_{1}+x_{2}\right) i+\left(y_{1}+y_{2}\right) j+\left(z_{1}+z_{2}\right) k
\end{aligned}
$$

Example 2 Find the unit vector of $\underline{u}=2 i+5 j-k$.
Solution Given vector $\underline{u}=2 i+5 \underline{j}-k$, to find the unit vector

$$
\begin{aligned}
& \Rightarrow \quad|u|=\sqrt{(2)^{2}+(5)^{2}+(-1)^{2}}=\sqrt{30} \\
& \quad \text { The unit vector is: } \\
& \Rightarrow \quad \hat{u}=\frac{u}{|u|}=\frac{2 i+5 j-k}{\sqrt{30}}=\frac{1}{\sqrt{30}}(2 i+5 j-k)
\end{aligned}
$$

Thus, $\hat{u}=\frac{1}{\sqrt{30}}(2 i+5 j-k)$ is the required unit vector.
Example 3 If $\underline{u}=2 i+3 j+k, \underline{v}=4 i+6 j+2 k$ and $\underline{w}=-6 i-9 j-3 k$, then show that $\underline{u}, \underline{v}$ and $\underline{w}$ are parallel to each other.
Solution $\quad \underline{v}=4 i+6 j+2 k=2(2 i+3 j+k)$

$$
\therefore \quad \underline{v}=2 \underline{u}
$$

$\Rightarrow \underline{u}$ and $\underline{v}$ are parallel vectors.

$$
\begin{aligned}
& \underline{w}=-6 i-9 j-3 k \\
& =-3(2 i+3 j+k) \quad \therefore \quad \underline{w}=-3 \underline{u}
\end{aligned}
$$

$\Rightarrow \underline{u}$ and $\underline{w}$ are parallel vectors.
Hence $\underline{u}, \underline{v}$ and $\underline{w}$ are parallel to each other.

# 14.1.6 Properties of Vectors

Let $\underline{u}, \underline{v}$ and $\underline{w}$ be vectors in the plane or in space and let $a, b \in R$, then they have the following properties:
(i) $\underline{u}+\underline{v}=\underline{v}+\underline{u}$
(Commutative property)
(ii) $(\underline{u}+\underline{v})+\underline{w}=\underline{u}+(\underline{v}+\underline{w})$
(Associative property)
(iii) $\underline{u}+\underline{o}=\underline{u}$
(Additive Identity)
(iv) $\underline{u}+(-1) \underline{u}=\underline{u}-\underline{u}=\underline{o}$
(Inverse for vector addition)
(v) $a(\underline{v}+\underline{w})=a \underline{v}+\alpha \underline{w}$
(Distributive property)
(vi) $a(b \underline{u})=(a b) \underline{u}$
(Scalar multiplication)

Proof: (i) Since for any two real numbers $a, b \in R, a+b=b+a$, it follows that for any two vectors $\underline{u}=[x, y, z]$ and $\underline{y}=\left[x^{\prime}, y^{\prime}, z^{\prime}\right]$ in $R^{3}$, where components of $\underline{u}$ and $\underline{y}$ belong to $R$.
We have

$$
\begin{aligned}
\underline{u}+\underline{y} & =[x, y, z]+\left[x^{\prime}, y^{\prime}, z^{\prime}\right] \\
& =\left[x+x^{\prime}, y+y^{\prime}, z+z^{\prime}\right] \\
& =\left[x^{\prime}+x, y^{\prime}+y, z^{\prime}+z\right] \quad \because \quad a+b=b+a \\
& =\left[x^{\prime}, y^{\prime}, z^{\prime}\right]+[x, y, z] \\
& =\underline{y}+\underline{u}
\end{aligned}
$$

So, addition of vectors in $R^{3}$ is commutative.
(ii) Since for any three real numbers $a, b, c \in R,(a+b)+c=a+(b+c)$, it follows that for any three vectors, $\underline{u}=[x, y, z], \underline{y}=\left[x^{\prime}, y^{\prime}, z^{\prime}\right]$ and $\underline{w}=\left[x^{\prime \prime}, y^{\prime \prime}, z^{\prime \prime}\right]$ in $R^{3}$. Where components of $\underline{u}, \underline{y}$ and $\underline{w}$ belong to $R$.
We have

$$
\begin{aligned}
(\underline{u}+\underline{y})+\underline{w} & =\left[x+x^{\prime}, y+y^{\prime}, z+z^{\prime}\right]+\left[x^{\prime \prime}, y^{\prime \prime}, z^{\prime \prime}\right] \\
& =\left[\left(x+x^{\prime}\right)+x^{\prime \prime},\left(y+y^{\prime}\right)+y^{\prime \prime},\left(z+z^{\prime}\right)+z^{\prime \prime}\right] \\
& =\left[x+\left(x^{\prime}+x^{\prime \prime}\right), y+\left(y^{\prime}+y^{\prime \prime}\right), z+\left(z^{\prime}+z^{\prime \prime}\right)\right] \\
& \because \quad(a+b)+c=a+(b+c) \\
& =[x, y, z]+\left[x^{\prime}+x^{\prime \prime}, y^{\prime}+y^{\prime \prime}, z^{\prime}+z^{\prime \prime}\right] \\
& =\underline{u}+(\underline{y}+\underline{w})
\end{aligned}
$$

So, addition of vectors in $R^{3}$ is associative.
(iii) Since for any real number $a$ and 0

$$
a+0=a, \text { it follows that }
$$

for any vectors, $\underline{u}=[x, y, z]$, and $\underline{o}=[0,0,0]$, where $\underline{o}$ is the zero vector in $R^{3}$.
We have

$$
\begin{aligned}
\underline{u}+\underline{o} & =[x, y, z]+[0,0,0] \\
& =[x+0, y+0, z+0] \\
& =[x, y, z]=\underline{u} \\
\underline{u}+\underline{o} & =\underline{u}
\end{aligned}
$$

Thus, $\underline{o}$ is the additive identity in $\mathrm{R}^{3}$
(iv) Since for any real number $a$, there exist $-a$ such that

$$
a+(-a)=a-a=0 \quad, \quad \text { it follows that }
$$

for any vector, $\underline{u}=[x, y, z]$, there exists $-\underline{u}=[-x,-y,-z]$ in $R^{3}$
Such that

$$
\begin{aligned}
\underline{u}+(-\underline{u}) & =[x, y, z]+[-\infty x,-y,-z]=[x+(-x), y+(-y), z+(-z)] \\
& =[x-x, y-y, z-z] \\
& =[0,0,0]=\underline{o}, \text { where } \underline{o} \text { is the additive identity } \\
\underline{u}+(-\underline{u}) & =\underline{o}
\end{aligned}
$$

Thus $-\underline{u}$ is the additive inverse of $\underline{u}$ in $\mathrm{R}^{3}$
The proofs of the other parts are left as an exercise for the students.

# 14.1.7 Distance Between Two Points in Space

If $\overrightarrow{O P_{1}}$ and $\overrightarrow{O P_{2}}$ are the position vectors of the points $P_{1}\left(x_{1}, y_{1}, z_{1}\right)$ and $P_{2}\left(x_{2}, y_{2}, z_{2}\right)$
The vector $\overrightarrow{P_{1} P_{2}}$ is given by

$$
\overrightarrow{P_{1} P_{2}}=\overrightarrow{O P_{2}}-\overrightarrow{O P_{1}}=\left[x_{2}-x_{1}, y_{2}-y_{1}, z_{2}-z_{1}\right]
$$

Distance between $P_{1}$ and $P_{2}=\left|\overrightarrow{P_{1} P_{2}}\right|$

$$
=\sqrt{\left(x_{2}-x_{1}\right)^{2}+\left(y_{2}-y_{1}\right)^{2}+\left(z_{2}-z_{1}\right)^{2}}
$$

This is called distance formula between two points $P_{1}$ and $P_{2}$ in $R^{3}$.
Example 4 Suppose a butterfly's flight path passed through points $(2,4,7)$ and $(6,1,3)$, where each unit represents a metre. What is the magnitude of the displacement the butterfly experienced in traveling between these two points?
Solution Distance between two points in three-dimensional space is given by the formula

$$
d=\sqrt{\left(x_{2}-x_{1}\right)^{2}+\left(y_{2}-y_{1}\right)^{2}+\left(z_{2}-z_{1}\right)^{2}}
$$

Substitute the coordinates of the given points into the formula:

$$
\begin{aligned}
& d=\sqrt{(6-2)^{2}+(1-4)^{2}+(3-7)^{2}} \\
& d=\sqrt{16+9+16}=\sqrt{41}=6.40
\end{aligned}
$$

The magnitude of the displacement the butterfly experienced in traveling between these two points is approximately 6.40 metres.

### 14.1.8 Direction Angles and Direction Cosines of a Vector

Let $r=\overrightarrow{O P}=x i+y j+z k$ be a non-zero vector, let $\alpha, \beta$ and $\gamma$ denote the angles formed between $r$ and the unit coordinate vectors $i, j$ and $k$ respectively,
where $0 \leq \alpha \leq \pi, 0 \leq \beta \leq \pi$ and $0 \leq \gamma \leq \pi$
(i) The angles $\alpha, \beta$ and $\gamma$ are called the direction angles of the vector $r$.
(ii) The numbers $\cos \alpha, \cos \beta$ and $\cos \gamma$ are called direction cosines of the vector $r$.

# Important Result:

Prove that $\cos ^{2} \alpha+\cos ^{2} \beta+\cos ^{2} \gamma=1$
Proof: Let

$$
\begin{aligned}
& r=[x, y, z]=x i+y j+z k \\
& \therefore \quad|r|=\sqrt{x^{2}+y^{2}+z^{2}}=r
\end{aligned}
$$

then $\frac{r}{|r|}=\left[\frac{x}{r}, \frac{y}{r}, \frac{z}{r}\right]$ is the unit vector in the direction of the vector $\underline{r}=\overrightarrow{O P}$
It can be visualized that the triangle $O A P$ is a right triangle with $m \angle A=90^{\circ}$.
Therefore, in right triangle $O A P$,

$$
\begin{aligned}
& \cos \alpha=\frac{\overrightarrow{O A}}{O P}=\frac{x}{r}, \text { similarly } \\
& \cos \beta=\frac{y}{r}, \cos \gamma=\frac{z}{r}
\end{aligned}
$$

The numbers $\cos \alpha=\frac{x}{r}, \cos \beta=\frac{y}{r}$ and $\cos \gamma=\frac{z}{r}$ are called the direction cosines of $\overrightarrow{O P}$

$$
\cos ^{2} \alpha+\cos ^{2} \beta+\cos ^{2} \gamma=\frac{x^{2}}{r^{2}}+\frac{y^{2}}{r^{2}}+\frac{z^{2}}{r^{2}}=\frac{x^{2}+y^{2}+z^{2}}{r^{2}}=\frac{r^{2}}{r^{2}}=1
$$

## EXERCISE 14.1

1. Let $\underline{u}=3 \underline{i}+2 \underline{j}-5 \underline{k} \underline{y}=\underline{i}-5 \underline{j}-\underline{k}$ and $w=-4 \underline{i}-\underline{j}+7 \underline{k}$. Find the following:
(i) $\underline{u}+2 \underline{v}+\underline{w}$
(ii) $\underline{v}-3 \underline{w}$
(iii) $|3 \underline{v}+\underline{w}|$.
2. Find the magnitude of the vector $\underline{v}$ and write the direction cosines of $\underline{v}$.
(i) $\underline{v}=3 \underline{i}-2 \underline{j}+6 \underline{k}$
(ii) $\underline{v}=-4 \underline{i}+4 \underline{j}+2 \underline{k}$
(iii) $\underline{v}=-6 \underline{i}+8 \underline{j}$
3. Find $t$, so that $|2 i+(t-1) j+t k|=\sqrt{13}$
4. Find a unit vector in the direction of $\underline{v}=-i+4 \underline{j}-8 \underline{k}$
5. If $\underline{u}=2 \underline{i}+\underline{j}-3 \underline{k}, \underline{v}=-\underline{i}+4 \underline{j}+2 \underline{k}$ and $\underline{w}=3 \underline{i}-2 \underline{j}+\underline{k}$, Find a unit vector parallel to $4 \underline{u}-3 \underline{v}+2 \underline{w}$.
6. Find a vector whose
(i) magnitude is 5 and is parallel to $3 \underline{i}+4 \underline{j}-\underline{k}$
(ii) magnitude is 7 and is parallel to $-\underline{i}+\underline{j}+\underline{k}$.

7. If $u=x i+2 j+3 k, v=i+y j-3 k$ and $w=-2 i-3 j$ represent the sides of a triangle. Find the values of $x$ and $y$.
8. The position vectors of the points $A, B, C$ and $D$ are $u=i+2 j+k, v=7 i+8 j+4 k$, $w=-i+k$ and $z=i+2 j+2 k$ respectively. Show that $\overrightarrow{A B}$ is parallel to $\overrightarrow{C D}$.
9. We say that two vectors $v$ and $w$ in space are parallel if there is a scalar $c$ such that $v=c w$. The vectors point in the same direction if $c>0$ and the vectors point in the opposite direction if $c<0$
(a) Find two vectors of length 2 parallel to the vector $v=2 i-4 j+4 k$.
(b) Find the constant $a$ so that the vectors $v=i-3 j+4 k$ and $w=a i+9 j-12 k$ are parallel.
(c) Find a vector of length 5 in the direction opposite that of $v=i-2 j+3 k$.
(d) Find $a$ and $b$ so that the vectors $3 i-j+4 k$ and $a i+b j-2 k$ are parallel.
10. A spacecraft moves from point $(120,240, \rightarrow 50)$ to point $(130,210,80)$ in kilometres. What is the magnitude of the displacement vector in kilometres?
11. Find the direction cosines for the given vector:
(i) $u=-6 i+3 j+2 k$
(ii) $v=4 i+2 j-5 k$
(iii) $P Q$, where $P(9,3,13)$ and $Q(11,6,19)$.
12. Which of the following triple can be the direction angles of a single vector?
(i) $45^{\circ}, 45^{\circ}, 60^{\circ}$
(ii) $30^{\circ}, 45^{\circ}, 60^{\circ}$
(iii) $45^{\circ}, 60^{\circ}, 60^{\circ}$

Product of Two Vectors: Multiplication of two vectors is an important algebraic operation in vector algebra. This algebraic operation plays a fundamental role for understanding various physical and mathematical real-life situation. Unlike the multiplication of numbers, product of vector can be performed in two distinct ways. The two primary types of vector multiplication are the dot product and the cross product. The dot product is a scalar number while cross product is a vector quantity.

# 14.2 Dot or Scalar Product

14.2.1 Dot or Scalax Product of Two Vectors and Its Geometrical Interpretation We shall now consider products of two vectors that originated in the study of physics and engineering. The concept of angle between two vectors is expressed in terms of a scalar product of two vectors.

Definition 1: Let two non-zero vectors $\underline{u}$ and $\underline{v}$, in the plane or in space, have same initial point. The dot product of $\underline{u}$ and $\underline{v}$, written as $\underline{u} \cdot \underline{v}$, is defined by

$$
\underline{u} \cdot \underline{v}=|\underline{u}||\underline{v}| \cos 0
$$

Where $\theta$ in the angle between $\underline{u}$ and $\underline{v}$ and $0 \leq \theta \leq \pi$

# Definition 2:

(a) If $\underline{u}=a_{1} \underline{i}+\underline{b}_{1} \underline{j}$ and $\underline{v}=a_{2} \underline{i}+\underline{b}_{2} \underline{j}$ are two non-zero vectors in the plane. The dot product $\underline{u} \cdot \underline{v}$ is defined by:

$$
\underline{u} \cdot \underline{v}=a_{1} a_{2}+b_{1} b_{2}
$$

(b) If $\underline{u}=a_{1} \underline{i}+\underline{b}_{1} \underline{j}+\underline{c}_{1} \underline{k}$ and $\underline{v}=a_{2} \underline{i}+\underline{b}_{2} \underline{j}+\underline{c}_{2} \underline{k}$ are two non-zero vectors in space. The dot product $\underline{u} \cdot \underline{v}$ is defined by

$$
\underline{u} \cdot \underline{v}=a_{1} a_{2}+b_{1} b_{2}+c_{1} c_{2}
$$

Note The dot product is also referred as the scalar product or the inner product.
Example 5 Prove the equivalence of above two definitions of dot product of two vectors:
(i) If $\underline{v}=\left[x_{1}, y_{1}\right]$ and $\underline{w}=\left[x_{2}, y_{2}\right]$ are two vectors in the plane, then $\underline{v} \underline{w}=x_{1} x_{2}+y_{1} y_{2}$
(ii) If $\underline{v}$ and $\underline{w}$ are two non-zero vectors in the plane, then $\underline{v} \cdot \underline{w}=|\underline{v}||\underline{w}| \cos \theta$, where $\theta$ is the angle between $\underline{v}$ and $\underline{w}$ and $0 \leq \theta \leq \pi$.
Proof: Let $\underline{v}$ and $\underline{w}$ be the sides of a triangle then the third side opposite to the angle $\theta$, has length $|\underline{v}-\underline{w}|$ By law of cosines,

$$
\begin{aligned}
|\underline{v}-\underline{w}|^{2} & =|\underline{v}|^{2}+|\underline{w}|^{2}-2|\underline{v}||\underline{w}| \cos \theta \\
\text { if } \quad \underline{v} & =\left[x_{1}, y_{1}\right] \text { and } \underline{w}=\left[x_{2}, y_{2}\right] \text {, then } \\
\underline{v}-\underline{w} & =\left[x_{1}-x_{2}, y_{1}-y_{2}\right]
\end{aligned}
$$

The law of cosine: $a^{2}=b^{2}+c^{2}-2 b c \cos a$

So, equation (1) becomes:

$$
\begin{aligned}
& \left(x_{1}-x_{2}\right)^{2}+\left(y_{1}-y_{2}\right)^{2}=x_{1}^{2}+y_{1}^{2}+x_{2}^{2}+y_{2}^{2}-2|\underline{v}||\underline{w}| \cos \theta \\
& -2 x_{1} x_{2}-2 y_{1} y_{2}=-2|\underline{v}||\underline{w}| \cos \theta \\
& x_{1} x_{2}+y_{1} y_{2}=|\underline{v}||\underline{w}| \cos \theta=\underline{v} \cdot \underline{w}
\end{aligned}
$$

# 14.2.2 Deduction of the Important Results

By applying the definition of dot product to unit vectors $i, j$ and $k$, we have
(a) $i . i=|i| i \mid \cos 0^{\circ}=1$
$j . j=|j||j \cos 0^{\circ}=1$
$k . k=|k||k| \cos 0^{\circ}=1$
(b) $i . j=|i||j| \cos 90^{\circ}=0$
$j . k=|j||k| \cos 90^{\circ}=0$
$k . i=|k||i| \cos 90^{\circ}=0$

### 14.2.3 Projection of a Vector along Another Vector

In many physical applications, it is required to know "how much" of a vector is applied along a given direction. For this purpose, we find the projection of one vector along the other vector.
Let $\overrightarrow{O A}=\underline{u}$ and $\overrightarrow{O B}=\underline{v}$
Let $\theta$ be the angle between them, such that $0 \leq \theta \leq \pi$.
Draw $\overrightarrow{B M} \perp \overrightarrow{O A}$. Then $\overrightarrow{O M}$ is called the projection of $\underline{v}$ along $\underline{u}$.
From the figure: $\frac{\overrightarrow{O M}}{\overrightarrow{O B}}=\cos \theta$, that is,

$$
\overrightarrow{O M}=|\overrightarrow{O B}| \cos \theta=|\underline{v}| \cos \theta
$$

Now, $u \cdot \underline{v}=|\underline{u}||\underline{v}| \cos \theta=|\underline{u}|(|\underline{v}| \cos \theta)=|\underline{u}|(\overrightarrow{O M})$
$=$ (magnitude of $\underline{u}$ ). (projection of $\underline{v}$ along $\underline{u}$ )
Thus, geometrically, the dot product of two vectors represents the product of the magnitude of one vector and the projection of the other vector onto it. In other words, the dot product of two vectors shows how much one vector extends in the direction of another.

Now, by definition, $\quad \cos \theta=\frac{u \cdot v}{|\underline{u}||\underline{v}|}$
From (1) and (2),

$$
\overrightarrow{O M}=|\underline{v}| \cdot \frac{u \cdot \underline{v}}{|\underline{u}||\underline{v}|}=\frac{u \cdot \underline{v}}{|\underline{u}|}
$$

$\therefore \quad$ Projection of $\underline{v}$ along $\underline{u}=\frac{\underline{u} \cdot \underline{v}}{|\underline{u}|}$
Similarly, projection of $\underline{u}$ along $\underline{v}=\frac{\underline{u} \cdot \underline{v}}{|\underline{v}|}$

# 14.2.4 Properties of Dot Product

Let $\underline{u}, \underline{v}$ and $\underline{w}$ be vectors and let $c$ be any real number, then
(i) $\underline{u} \cdot \underline{v}=0 \Rightarrow \underline{u}=0$ or $\underline{v}=0$ or $\underline{u} \perp \underline{v}$
(ii) $\underline{u} \cdot \underline{v}=\underline{v} \cdot \underline{u} \quad$ (Commutative property)
(iii) $\underline{u} \cdot(\underline{v}+\underline{w})=\underline{u} \cdot \underline{v}+\underline{u} \cdot \underline{w} \quad$ (Distributive property)
(iv) $(c \underline{u}) \cdot \underline{v}=c(\underline{u} \cdot \underline{v}) \quad$ (c is scalar)
(v) $\underline{u} \cdot \underline{u}=|\underline{u}|^{2}$

### 14.2.5 Dot Product of Vectors in terms of their components

Let $\underline{u}=a_{1} \underline{i}+b_{1} \underline{j}+c_{1} \underline{k}$ and $\underline{v}=a_{2} \underline{i}+b_{2} \underline{j}+c_{2} \underline{k}$ be two non-zero vectors.
From distributive law we can write:

$$
\begin{aligned}
\therefore \quad \underline{u} \cdot \underline{v}= & \left(a_{1} i+b_{1} \underline{j}+c_{1} \underline{k}\right) \cdot\left(a_{2} i+b_{2} \underline{j}+c_{2} \underline{k}\right) \\
= & a_{1} a_{2}(i \cdot i)+a_{1} b_{2}(i \cdot j)+a_{1} c_{2}(i \cdot k)+b_{1} a_{2}(j \cdot i)+b_{1} b_{2}(j \cdot j)+b_{1} c_{2}(j \cdot k) \\
& +c_{1} a_{2}(k \cdot i)+c_{1} b_{2}(k \cdot j)+c_{1} c_{2}(k \cdot k) \\
\Rightarrow \underline{u} \cdot \underline{v}= & a_{1} a_{2}+b_{1} b_{2}+c_{1} c_{2} \quad \because i \cdot i=\underline{j} \cdot \underline{j}=\underline{k} \cdot \underline{k}=1 \\
& i \cdot j=\underline{j} \cdot \underline{k}=\underline{k} \cdot \underline{i}=0
\end{aligned}
$$

Hence the dot product of two vectors is the sum of the product of their corresponding components.
Example 6 Show that the components of a vector are the projections of that vector along $i, j$ and $k$ respectively.
Proof: Let $\underline{v}=a \underline{i}+b \underline{j}+c \underline{k}$, then
Projection of $\underline{v}$ along $\underline{i}=\frac{\underline{v} \cdot \underline{i}}{|\underline{i}|}=(a \underline{i}+b \underline{j}+c \underline{k}) \cdot \underline{i}=a$
Projection of $\underline{v}$ along $\underline{j}=\frac{\underline{v} \cdot \underline{j}}{|\underline{j}|}=(a \underline{i}+b \underline{j}+c \underline{k}) \cdot \underline{j}=b$
Projection of $\underline{v}$ along $\underline{k}=\frac{\underline{v} \cdot \underline{k}}{|\underline{k}|}=(a \underline{i}+b \underline{j}+c \underline{k}) \cdot \underline{k}=c$
Hence components $a, b$ and $c$ of vector $\underline{v}=a \underline{i}+b \underline{j}+c \underline{k}$ are projections of vector $\underline{v}$ along $i, j$ and $k$ respectively.

Example 7 Prove that in any triangle $A B C$
(i) $\quad a^{2}=b^{2}+c^{2}-2 b c \cos A$
(ii) $\quad a=b \cos C+c \cos B$
(Cosine Law)
(Projection Law)
Proof: Let the vectors $\underline{a}, \underline{b}$ and $\underline{c}$ be along the sides $B C, C A$ and $A B$ of the triangle $A B C$ as shown in the figure.
(i) $\underline{a}+\underline{b}+\underline{c}=\underline{0}$
$\Rightarrow \quad \underline{a}=-(\underline{b}+\underline{c})$
Now $\quad \underline{a} \cdot \underline{a}=(\underline{b}+\underline{c}) \cdot(\underline{b}+\underline{c})$
$\Rightarrow \quad=\underline{b} \cdot \underline{b}+\underline{b} \cdot \underline{c}+\underline{c} \cdot \underline{b}+\underline{c} \cdot \underline{c}$
$\Rightarrow \quad a^{2}=b^{2}+2 \underline{b} \cdot \underline{c}+c^{2} \quad(\because \underline{b} \cdot \underline{c}=\underline{c} \cdot \underline{b})$
$\Rightarrow \quad a^{2}=b^{2}+c^{2}+2 b c \cos (\pi-A)$
$\therefore \quad a^{2}=b^{2}+c^{2}-2 b c \cos A$
(ii) $\underline{a}+\underline{b}+\underline{c}=\underline{0}$
$\Rightarrow \quad \underline{a}=-\underline{b}-\underline{c}$
Take dot product with $\underline{a}$

$$
\begin{aligned}
\underline{a} \cdot \underline{a} & =-\underline{a} \cdot \underline{b}-\underline{a} \cdot \underline{c} \\
& =-a b \cos (\pi-C)-a c \cos (\pi-B) \\
& =-a b(-\cos C)-a c(-\cos B) \\
a^{2} & =a b \cos C+a c \cos B \\
\Rightarrow \quad a & =b \cos C+c \cos B
\end{aligned}
$$

Example 8 Prove that: $\cos (\alpha-\beta)=\cos \alpha \cos \beta+\sin \alpha \sin \beta$
Proof: Let $\overrightarrow{O A}$ and $\overrightarrow{O B}$ be the unit vectors in the $x y$-plane making angles $\alpha$ and $\beta$ with the positive $x$-axis.
So that $m \angle A O B=\alpha-\beta$
Now $\overrightarrow{O A}=\cos \alpha \underline{i}+\sin \alpha \underline{j}$
and $\overrightarrow{O B}=\cos \beta \underline{i}+\sin \beta \underline{j}$
$\therefore \quad \overrightarrow{O A} \cdot \overrightarrow{O B}=(\cos \alpha \underline{i}+\sin \alpha \underline{j}) \cdot(\cos \beta \underline{i}+\sin \beta \underline{j})$
$\Rightarrow|\overrightarrow{O A}||\overrightarrow{O B}| \cos (\alpha-\beta)=\cos \alpha \cos \beta+\sin \alpha \sin \beta$
$\therefore \quad \cos (\alpha-\beta)=\cos \alpha \cos \beta+\sin \alpha \sin \beta$
$(\because|\overrightarrow{O A}|=|\overrightarrow{O B}|=1)$

# 14.2.6 Orthogonality of Two Vectors

Definition: Two non-zero vectors $\underline{u}$ and $\underline{v}$ are orthogonal (perpendicular) if and only if $\underline{u} \cdot \underline{v}=0$.
The dot product of two vectors $\underline{u}$ and $\underline{v}$ becomes zero when $\underline{u} \perp \underline{v}, \theta=90^{\circ}$ or $\frac{\pi}{2}$ radius.

$$
\underline{u} \cdot \underline{v}=|\underline{u}| \perp|\underline{v}| \cos 90^{\circ}=0
$$

The zero vector $\underline{o}$ is orthogonal to every vector because:

$$
\underline{o} \cdot \underline{b}=0 \forall \underline{b}
$$

Thus, $\underline{u} \cdot \underline{v}=0 \Leftrightarrow \underline{u} \perp \underline{v}$
Example 9 If $\underline{u}=3 \underline{i}-j-2 \underline{k}$ and $\underline{v}=i+2 j-\underline{k}$, then find $\underline{u} \cdot \underline{v}$.
Solution $\underline{u} \cdot \underline{v}=(3)(1)+(-1)(2)+(-2)(-1)=3$
Example 10 If $\underline{u}=2 \underline{i}-4 \underline{j}+5 \underline{k}$ and $\underline{v}=4 \underline{i}-3 \underline{j}-4 \underline{k}$, then prove that $\underline{u}$ and $\underline{v}$ are orthogonal.
Solution $\underline{u} \cdot \underline{v}=(2)(4)+(-4)(-3)+(5)(-4)=0$
$\Rightarrow \quad \underline{u}$ and $\underline{v}$ are perpendicular
Example 11 Find a scalar $a$ so that the vectors $2 \underline{i}+\alpha \underline{j}+5 \underline{k}$ and $3 \underline{i}+\underline{j}+\alpha \underline{k}$ are orthogonal.
Solution Let $\underline{u}=2 \underline{i}+\alpha \underline{j}+5 \underline{k}$ and $\underline{v}=3 \underline{i}+\underline{j}+\alpha \underline{k}$
It is given that $\underline{u}$ and $\underline{v}$ are orthogonal

$$
\begin{aligned}
& \therefore \quad \underline{u} \cdot \underline{v} \\
& \Rightarrow \quad(2 \underline{i}+\alpha \underline{j}+5 \underline{k}) \cdot(3 \underline{i}+\underline{j}+\alpha \underline{k})=0 \\
& \Rightarrow \quad 6+\alpha+5 \alpha=0 \\
& \quad \therefore \quad \alpha=-1
\end{aligned}
$$

### 14.2.7 Angle Between Two Vectors

The angle between two vectors $\underline{u}$ and $\underline{v}$ is determined from the definition of dot product, that is
(a) $\underline{u} \cdot \underline{v}=|\underline{u}||\underline{v}| \cos 0, \quad$ where $0 \leq \theta \leq \pi$

$$
\Rightarrow \quad \cos \theta=\frac{\underline{u} \cdot \underline{v}}{|\underline{u}||\underline{v}|}
$$

(b) If $\underline{u}=a_{1} \underline{i}+\underline{b}_{1} \underline{j}+\underline{c}_{1} \underline{k} \quad$ and $\quad \underline{v}=a_{2} \underline{i}+\underline{b}_{2} \underline{j}+\underline{c}_{2} \underline{k}$, then

$$
\begin{aligned}
\underline{u} \cdot \underline{v} & =a_{1} a_{2}+b_{1} b_{2}+c_{1} c_{2} \\
|\underline{u}| & =\sqrt{a_{1}^{2}+b_{1}^{2}+c_{1}^{2}} \quad \text { and } \quad|\underline{v}|=\sqrt{a_{2}^{2}+b_{2}^{2}+c_{2}^{2}}
\end{aligned}
$$

$$
\begin{aligned}
\therefore \quad & \cos \theta=\frac{u \cdot \psi}{|u||v|} \\
\therefore \quad & \cos \theta=\frac{a_{1} a_{2}+b_{1} b_{2}+c_{1} c_{2}}{\sqrt{a_{1}^{2}+b_{1}^{2}+c_{1}^{2}} \sqrt{a_{2}^{2}+b_{2}^{2}+c_{2}^{2}}}
\end{aligned}
$$

Example 12 Find the angle between the vectors.

$$
u=2 i-j+k \quad \text { and } \quad v=-i+j
$$

Solution $u \cdot v=(2 i-j+k) \cdot(-i+j+0 k)$

$$
=(2)(-1)+(-1)(1)+(1)(0)=-3
$$

and

$$
\begin{aligned}
|\underline{u}| & =|2 i-j+k|=\sqrt{(2)^{2}+(-1)^{2}+(1)^{2}}=\sqrt{6} \\
|\underline{v}| & =|-i+j+0 k|=\sqrt{(-1)^{2}+(1)^{2}+(0)^{2}}=\sqrt{2}
\end{aligned}
$$

Now $\cos \theta=\frac{u \cdot \psi}{|u| \cdot|v|}$
$\Rightarrow \quad \cos \theta=\frac{-3}{\sqrt{6} \cdot \sqrt{2}}$

$$
=-\frac{\sqrt{3}}{2}
$$

$$
\therefore \quad 0=\frac{5 \pi}{6}
$$

Example 13 Show that the vectors $\overrightarrow{A B}=2 i-j+k, \overrightarrow{B C}=i-3 j-5 k$ and $\overrightarrow{A C}=3 i-4 j-4 k$ are the sides of a right triangle.
Solution Given $\overrightarrow{A B}=2 i-j+k, \overrightarrow{B C}=i-3 j-5 k$ and

$$
\overrightarrow{A C}=3 i-4 j-4 k
$$

Now

$$
\begin{aligned}
\overrightarrow{A B}+\overrightarrow{B C} & =(2 i-j+k)+(i-3 j-5 k) \\
& =3 i-4 j-4 k=\overrightarrow{A C} \text { (third side) }
\end{aligned}
$$

$\therefore \quad \overrightarrow{A B}, \overrightarrow{B C}$ and $\overrightarrow{A C}$ form a triangle $A B C$.
Further we prove that $\triangle A B C$ is a right triangle

$$
\begin{aligned}
\overrightarrow{A B} \cdot \overrightarrow{B C} & =(2 i-j+k) \cdot(i-3 j-5 k) \\
& =(2)(1)+(-1)(-3)+(1)(-5)=2+3-5=0 \\
\therefore \quad \overrightarrow{A B} \perp \overrightarrow{B C} & \\
& \text { Hence, } \triangle A B C \text { is a right triangle. }
\end{aligned}
$$

# 14.2.8 Work Done By a Constant Force

If a constant force $F$, applied to a body, acts at an angle $\theta$ to the direction of motion, then the work done by $\underline{F}$ is defined to be the product of the component of $\underline{F}$ in the direction of the displacement and the distance that the body moves.
In figure, a constant force $\underline{F}$ acting on a body, displaces it from $A$ to $B$.
$\therefore \quad$ Work done $=($ component of $\underline{F}$ along $A B)$ (displacement)

$$
=(F \cos \theta)(A B)=\underline{F} \cdot \underline{A B}=\underline{F} \cdot \underline{d}
$$

Example 14 The constant forces $2 i+5 j+6 k$ and $-i-2 j-k$ act on a body displaced from position $P(4,-3,-2)$ to $Q(6,1,-3)$. Find the total work done.
Solution
Total force $=(2 i+5 j+6 k)+(-i-2 j-k)$

$$
\Rightarrow \quad \underline{F}=i+3 j+5 k
$$

The displacement of the body $=P \vec{Q}=(6-4) i+(1+3) j+(-3+2) k$

$$
\Rightarrow \quad \underline{d}=2 i+4 j-k
$$

$\therefore \quad$ Work done $=\underline{F} \cdot \underline{d}$

$$
=(i+3 j+5 k) \cdot(2 i+4 j-k)=2+12-5=9 \text { units }
$$

## EXERCISE 14.2

1. Find the coahues of the angle $\theta$ between $\underline{u}$ and $\underline{v}$ :
(i) $\underline{u}=2 i+3 j+k, \underline{v}=-i+2 j+2 k$
(ii) $\underline{u}=[-3,2,5], \underline{v}=[1,6,-2]$
2. If $a+b+c=0$ and $|a|=3,|b|=5$ and $|c|=7$. Find the angle between $a$ and $b$.
3. If $|a|=3,|b|=4$ and $|a+b|=5$. Find the angle between $a$ and $b$.
4. Calculate the projection of $a$ along $b$ and projection of $b$ along $a$ when:
(i) $a=2 i+3 j-k, b=i-2 j+4 k$ (ii) $a=4 i-2 j+3 k, b=i+j+k$
5. Find a real number $a$ so that the vectors $u$ and $v$ are perpendicular:
(i) $\underline{u}=\alpha i+3 j+k, \underline{v}=i-2 j+\alpha k$ (ii) $\underline{u}=\alpha i+2 \alpha j-k, \underline{v}=i+\alpha j+3 k$
6. Find the number $z$ so that the triangle with vertices $A(3,0,-2), B(0,3,1)$ and $C(1,1, z)$ is a right triangle with right angle at $C$.

7. If $\hat{a}$ and $\hat{b}$ are unit vectors and $2 \theta$ is the angle between them, show that $\sin \theta=\frac{1}{2}|\hat{a}-\hat{b}|$.
8. If $|a+b|=|a-b|$, then show that $a$ and $b$ are perpendicular.
9. (i) Show that the vectors $3 i-2 j+k, i-3 j+5 k$ and $2 i+j-4 k$ form a right triangle.
(ii) Show that the set of points $P(4,-1,2), Q(1,3,-1)$ and $R(-2,4,6)$ form a right triangle.
10. Prove that the $\cos (\alpha+\beta)=\cos \alpha \cos \beta-\sin \alpha \sin \beta$
11. Prove that in any triangle $A B C$.
(i) $b=c \cos A+a \cos C$
(ii) $c=a \cos B+b \cos A$
(iii) $b^{2}=c^{2}+a^{2}-2 c a \cos B$
(iv) $c^{2}=a^{2}+b^{2}-2 a b \cos C$
12. Show that for any vectors $a$ and $b, \quad|a|-|b| \leq|a+b| \leq|a|+|b|$
13. Find the work done, if the point at which the constant force $F=2 i+5 j+3 k$ is applied to an object, moves it from $P_{1}(2,-3,1)$ to $P_{2}(7,5,3)$.
14. A particle, acted by constant forces $F_{1}=3 i+4 j-3 k$ and $F_{2}=i+4 j-k$, is displaced from $A(2,1,3)$ to $B(5,4,4)$. Find the work done.
15. A particle is displaced from the point $A(5,-5,-7)$ to the point $B(6,2,-2)$ under the action of constant forces defined by $10 i-j+11 k, 4 i+5 j+9 k$ and $-2 i+j-9 k$. Show that the total work done by the force is 102 units.
16. A force of magnitude 6 units acting parallel to $4 i+3 j-k$ displace the point of application from $A(2,-1,3)$ to $B(7,3,2)$. Find the work done.