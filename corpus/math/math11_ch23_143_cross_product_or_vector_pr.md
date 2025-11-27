# Chapter 23: 14.3 Cross Product or Vector Product

### 14.3.1 The Cross Product or Vector Product of Two Vectors and its Geometrical Interpretation

One of the key multiplication operations involving vectors in space is the cross product. Unlike the dot product, which results is a scalar, the cross product of two vectors yields a vector quantity. The vector product of two vectors is widely used in Physics, particularly in fields of mechanics and electricity. It is only defined for vectors in space. Let $\underline{u}$ and $\underline{v}$ be two non-zero vectors. The cross or vector product of $\underline{u}$ and $\underline{v}$ gives a

vector that is perpendicular to both the vectors $\underline{u}$ and $\underline{v}$, written as $\underline{u} \times \underline{v}$, is defined by

$$
\underline{u} \times \underline{v}=(\|\underline{u}\| \mid \underline{v} \mid \sin \theta) \underline{n}
$$

where $\theta$ is the angle between the vectors, such that $0 \leq \theta \leq \pi$ and $\underline{n}$ is a unit vector perpendicular to the plane of $\underline{u}$ and $\underline{v}$ with direction given by the right-hand rule.
Figure (a)
Right hand
Right hand rule
Figure (b)
(i) If the fingers of the right hand point along the vector $\underline{u}$ and then curl towards the vector $\underline{v}$, then the thumb will give the direction of $\underline{n}$ which is $\underline{u} \times \underline{v}$. It is shown in the figure (a).
(ii) In figure (b), the right hand rule shows the direction of $\underline{v} \times \underline{u}$.

# 14.3.2 Parallel Vectors

If $\underline{u}$ and $\underline{v}$ are parallel vectors, then $(\theta=0 \Rightarrow \sin 0=0)$.

$$
\begin{aligned}
& \underline{u} \times \underline{v}=\|\underline{u}\| \mid \underline{v}\| \sin \theta \underline{n} \\
& \underline{u} \times \underline{v}=0 \quad \text { or } \quad \mid \underline{u} \times \underline{v}=0
\end{aligned}
$$

And if $\underline{u} \times \underline{v}=0$, then either $\sin \theta=0 \quad$ or $\quad\|\underline{u}\|=0 \quad$ or $\quad\|\underline{v}\|=0$
(i) If $\sin \theta=0 \Rightarrow \theta=0^{\circ}$ or $180^{\circ}$. Which shows that the vectors $\underline{u}$ and $\underline{v}$ are parallel.
(ii) If $\underline{u}=\underline{0}$ or $\underline{v}=\underline{0}$, then since the zero vector has no specific direction, we adopt the convention that the zero vector is parallel to every vector.

## Note: Zero vector is both parallel and perpendicular to every vector. This apparent contradiction will cause no trouble, since the angle between two vectors is never applied when one of them is zero vector.

### 14.3.3 Derivation of Useful Results of Cross Products

By applying the definition of cross product to unit vectors $i, j$ and $k$, we have:
(a) $\underline{i} \times \underline{i}=\|\underline{i}\| \mid i\left\|\sin 0^{\circ} \underline{n}=\underline{0}\right.$
$\underline{j} \times \underline{j}=\|\underline{j}\| \mid \underline{j}\| \sin 0^{\circ} \underline{n}=\underline{0}$
$\underline{k} \times \underline{k}=\|\underline{k}\| \mid \underline{k}\left\|\sin 0^{\circ} \underline{n}=\underline{0}\right.$
(b) $\quad \underline{i} \times \underline{j}=|\underline{i}||\underline{j}| \sin 90^{\circ} \underline{k}=\underline{k}$

$$
\begin{aligned}
& \underline{j} \times \underline{k}=|\underline{j}||\underline{k}| \sin 90^{\circ} \underline{i}=\underline{i} \\
& \underline{k} \times \underline{i}=|\underline{k}||\underline{i}| \sin 90^{\circ} \underline{j}=\underline{j}
\end{aligned}
$$

(c) $\quad \underline{u} \times \underline{u}=|\underline{u}||\underline{u}| \sin 0 \underline{n}=\underline{0}$

# 14.3.4 Properties of Cross Product

The cross product possesses the following properties:
(i) $\underline{u} \times \underline{v}=\underline{0}$ if $\underline{u}=\underline{0}$ or $\underline{v}=\underline{0}$
(ii) $\underline{u} \times \underline{v}=-\underline{v} \times \underline{u}$
(iii) $\underline{u} \times(\underline{v}+\underline{w})=\underline{u} \times \underline{v}+\underline{u} \times \underline{w}$
(iv) $\underline{u} \times(\underline{k} \underline{v})=(\underline{k} \underline{u}) \times \underline{v}=\underline{k}(\underline{u} \times \underline{v})$
(v) $\underline{u} \times \underline{u}=\underline{0}$

The proofs of these properties are left as an exercise for the students.

### 14.3.5 Analytical Expressions of $\underline{u} \times \underline{v}$ (Determinant formula for $\underline{u} \times \underline{v}$ )

Let $\underline{u}=a_{1} \underline{i}+\underline{b}_{1} \underline{j}+\underline{c}_{1} \underline{k}$ and $\underline{v}=a_{2} \underline{i}+\underline{b}_{2} \underline{j}+\underline{c}_{2} \underline{k}$, then

$$
\begin{aligned}
\underline{u} \times \underline{v}= & \left(a_{1} \underline{i}+\underline{b}_{1} \underline{j}+\underline{c}_{1} \underline{k}\right) \times\left(a_{2} \underline{i}+\underline{b}_{2} \underline{j}+\underline{c}_{2} \underline{k}\right) \\
= & a_{1} a_{2}(\underline{i} \times \underline{i})+a_{1} \underline{b}_{2}(\underline{i} \times \underline{j})+a_{1} \underline{c}_{2}(\underline{i} \times \underline{k}) \\
& +\underline{b}_{1} a_{2}(\underline{j} \times \underline{i})+\underline{b}_{1} \underline{b}_{2}(\underline{j} \times \underline{j})+\underline{b}_{1} \underline{c}_{2}(\underline{j} \times \underline{k}) \\
& +\underline{c}_{1} \underline{a}_{2}(\underline{k} \times \underline{i})+\underline{c}_{1} \underline{b}_{2}(\underline{k} \times \underline{j})+\underline{c}_{1} \underline{c}_{2}(\underline{k} \times \underline{k}) \\
& =a_{1} \underline{b}_{2} \underline{k}-a_{1} \underline{c}_{2} \underline{j}-\underline{b}_{1} \underline{a}_{2} \underline{k}+\underline{b}_{1} \underline{c}_{2} \underline{i}+\underline{c}_{1} \underline{a}_{2} \underline{j}-\underline{c}_{1} \underline{b}_{2} \underline{i} \\
\Rightarrow \quad & \underline{u} \times \underline{v}=\left(\underline{b}_{1} \underline{c}_{2}-\underline{c}_{1} \underline{b}_{2}\right) \underline{i}-\left(\underline{a}_{1} \underline{c}_{2}-\underline{c}_{1} \underline{a}_{2}\right) \underline{j}+\left(\underline{a}_{1} \underline{b}_{2}-\underline{b}_{1} \underline{a}_{2}\right) \underline{k}
\end{aligned}
$$

The expression of $3 \times 3$ determinant

$$
=\left|\begin{array}{ccc}
\underline{i} & \underline{i} & \underline{k} \\
a_{1} & b_{1} & c_{1} \\
a_{2} & b_{2} & c_{2}
\end{array}\right|=\left(\underline{b}_{1} \underline{c}_{2}-\underline{c}_{1} \underline{b}_{2}\right) \underline{i}-\left(\underline{a}_{1} \underline{c}_{2}-\underline{c}_{1} \underline{a}_{2}\right) \underline{j}+\left(\underline{a}_{1} \underline{b}_{2}-\underline{b}_{1} \underline{a}_{2}\right) \underline{k}
$$

The terms on R.H.S of equation (i) are the same as the terms in the expansion of the above determinant.

$$
\text { Hence } \underline{u} \times \underline{v}=\left|\begin{array}{ccc}
\underline{i} & \underline{j} & \underline{k} \\
a_{1} & \underline{b}_{1} & \underline{c}_{1} \\
a_{2} & \underline{b}_{2} & \underline{c}_{2}
\end{array}\right|
$$

which is known as determinant formula for $\underline{u} \times \underline{v}$.

# Unit 44 Vectors in Space

Note The expression on R.H.S. of equation (ii) is not an actual determinant, since its entries are not all scalars. It is simply a way of remembering the complicated expression on R.H.S of equation (i).

Example 15 Find a vector perpendicular to each of the vectors. Also verify that $\underline{a}$ and $\underline{b}$ are $\perp$ to $\underline{a} \times \underline{b}$

$$
\underline{a}=2 \underline{i}-\underline{j}+\underline{k} \quad \text { and } \quad \underline{b}=4 \underline{i}+2 \underline{j}-\underline{k}
$$

Solution A vector perpendicular to both the vectors $\underline{a}$ and $\underline{b}$ is $\underline{a} \times \underline{b}$.

$$
\therefore \quad \underline{a} \times \underline{b}=\left|\begin{array}{ccc}
\underline{i} & \underline{j} & \underline{k} \\
2 & -1 & 1 \\
4 & 2 & -1
\end{array}\right|=-i+6 j+8 k
$$

Verification:

$$
\begin{gathered}
\underline{a} \cdot \underline{a} \times \underline{b}=(2 \underline{i}-\underline{j}+\underline{k}) \cdot(-i+6 \underline{j}+8 \underline{k})=(2)(-1)+(-1)(6)+(1)(8)=0 \\
\text { and } \quad \underline{b} \cdot \underline{a} \times \underline{b}=(4 \underline{i}+2 \underline{j}-\underline{k}) \cdot(-i+6 \underline{j}+8 \underline{k})=(4)(-1)+(2)(6)+(-1)(8)=0
\end{gathered}
$$

Hence $\underline{a} \times \underline{b}$ is perpendicular to both the vectors $\underline{a}$ and $\underline{b}$.

### 14.3.6 Angle Between Two Vectors (Cross Product)

The sine of the angle between two vectors $\underline{a}$ and $\underline{b}$ is determined from the definition of cross product.
If $\theta$ is the sine of the angle between $\underline{a}$ and $\underline{b}$, then $|\underline{a} \times \underline{b}|=|\underline{a}||\underline{b}| \sin \theta$

$$
\Rightarrow \quad \sin \theta=\frac{|\underline{a} \times \underline{b}|}{|\underline{a}||\underline{b}|}
$$

Example 16 If $\underline{a}=4 \underline{i}+3 \underline{j}+\underline{k}$ and $\underline{b}=2 \underline{i}-\underline{j}+2 \underline{k}$. Find a unit vector perpendicular to both $\underline{a}$ and $\underline{b}$. Also find the sine of the angle between the vectors $\underline{a}$ and $\underline{b}$.

$$
\begin{aligned}
& \underline{a} \times \underline{b}=\left|\begin{array}{ccc}
\underline{i} & \underline{j} & \underline{k} \\
4 & 3 & 1 \\
2 & -1 & 2
\end{array}\right|=7 \underline{i}-6 \underline{j}-10 \underline{k} \\
& \text { and } \quad|\underline{a} \times \underline{b}|=\sqrt{(7)^{2}+(-6)^{2}+(-10)^{2}}=\sqrt{185} \\
& \therefore \quad \text { A unit vector perpendicular to } \underline{a} \text { and } \underline{b}=\frac{\underline{a} \times \underline{b}}{|\underline{a} \times \underline{b}|}=\frac{7 \underline{i}-\underline{b} \underline{j}-10 \underline{k}}{\sqrt{185}} \\
& \text { Now } \quad|\underline{a}|=\sqrt{(4)^{2}+(3)^{2}+(1)^{2}}=\sqrt{26} \\
& \left\lvert\, \underline{b}\right|=\sqrt{(2)^{2}+(-1)^{2}+(2)^{2}}=3
\end{aligned}
$$

If $\theta$ is the angle between $\underline{a}$ and $\underline{b}$, then $|\underline{a} \times \underline{b}|=|\underline{a}||\underline{b}| \sin \theta$

$$
\Rightarrow \quad \sin \theta=\frac{|\underline{a} \times \underline{b}|}{|\underline{a}||\underline{b}|}=\frac{\sqrt{185}}{3 \sqrt{26}}
$$

Example17 Prove that $\sin (\alpha+\beta)=\sin \alpha \cos \beta+\cos \alpha \sin \beta$
Proof: Let $\overrightarrow{O A}$ and $\overrightarrow{O B}$ be two unit vectors in the $x y$-plane making angles $\alpha$ and $-\beta$ with the positive $x$-axis respectively.

So that $m \angle A O B=\alpha+\beta$
Now $\quad \overrightarrow{O A}=\cos \alpha i+\sin \alpha j$
and

$$
\begin{aligned}
\overrightarrow{O B} & =\cos (-\beta) i+\sin (-\beta) j \\
& =\cos \beta i-\sin \beta j \\
\therefore \quad \overrightarrow{O B} \times \overrightarrow{O A} & =(\cos \beta i-\sin \beta j) \times(\cos \alpha i+\sin \alpha i) \\
\Rightarrow \quad & \left|\overrightarrow{O B}\right||\overrightarrow{O A}| \sin (\alpha+\beta) k=\left|\begin{array}{ccc}
i & j & k \\
\cos \beta & -\sin \beta & 0 \\
\cos \alpha & \sin \alpha & 0
\end{array}\right| \\
\Rightarrow \quad & \sin (\alpha+\beta) k=(\sin \alpha \cos \beta+\cos \alpha \sin \beta) k
\end{aligned}
$$

$\therefore \quad \sin (\alpha+\beta)=\sin \alpha \cos \beta+\cos \alpha \sin \beta$
Example18 In any triangle $A B C$, prove that

$$
\frac{a}{\sin A}=\frac{b}{\sin B}=\frac{c}{\sin C} \text { (Law of Sines) }
$$

Proof: Suppose vectors $\underline{a}, \underline{b}$ and $\underline{c}$ are along the sides $B C, C A$ and $A B$ respectively of the triangle $A B C$.

$$
\begin{aligned}
& \therefore \quad \underline{a}+\underline{b}+\underline{c}=\underline{0} \\
& \Rightarrow \quad \underline{b}+\underline{c}=-\underline{a}
\end{aligned}
$$

Take cross product with $\underline{c}$

$$
\begin{aligned}
& \underline{b} \times \underline{c}+\underline{c} \times \underline{c}=-a \times \underline{c} \\
& \underline{b} \times \underline{c}=\underline{c} \times \underline{a} \quad(\because \underline{c} \times \underline{c}=\underline{0}) \\
& \Rightarrow \quad|\underline{b} \times \underline{c}|=|\underline{c} \times \underline{a}| \\
& \begin{array}{l}
|\underline{b}||\underline{c}| \sin (\pi-A)=|\underline{c}||\underline{a}| \sin (\pi-B) \\
\Rightarrow \quad b c \sin A=c a \sin B \Rightarrow b \sin A=a \sin B
\end{array} \\
& \therefore \quad \frac{b}{\sin B}=\frac{a}{\sin A}
\end{aligned}
$$

Similarly, by taking cross product of (i) with $\underline{b}$, we have

$$
\frac{a}{\sin A}=\frac{c}{\sin C}
$$

From (ii) and (iii), we get $\frac{a}{\sin A}=\frac{b}{\sin B}=\frac{c}{\sin C}$
Example 19 If $\underline{u}=2 \underline{i}-\underline{j}+\underline{k}$ and $\underline{v}=4 \underline{i}+2 \underline{j}-\underline{k}$, find by determinant formula
(i) $\underline{u} \times \underline{u}$
(ii) $\underline{u} \times \underline{v}$
(iii) $\underline{v} \times \underline{u}$

Solution $\underline{u}=2 \underline{i}-\underline{j}+\underline{k}$ and $\underline{v}=4 \underline{i}+2 \underline{j}-\underline{k}$
By determinant formula
(i) $\quad \underline{u} \times \underline{u}=\left|\begin{array}{ccc}\underline{i} & \underline{j} & \underline{k} \\ 2 & -1 & 1 \\ 2 & -1 & 1\end{array}\right|=0 \quad$ ( $\therefore$ Two rows are same)
(ii) $\quad \underline{u} \times \underline{v}=\left|\begin{array}{ccc}\underline{i} & \underline{j} & \underline{k} \\ 2 & -1 & 1 \\ 4 & 2 & -1\end{array}\right|=(1-2) \underline{i}-(-2-4) \underline{j}+(4+4) \underline{k}=-\underline{i}+6 \underline{j}+8 \underline{k}$
(iii) $\underline{v} \times \underline{u}=\left|\begin{array}{ccc}\underline{i} & \underline{j} & \underline{k} \\ 4 & 2 & -1 \\ 2 & -1 & -1\end{array}\right|=(2-1) \underline{i}-(4+2) \underline{j}+(-4-4) \underline{k}=\underline{i}-6 \underline{j}-8 \underline{k}$

# 14.3.7 Real World Applications on Cross or Vector Product

(a) Area of Parallelogram

Suppose $\underline{u}$ and $\underline{v}$ are two non-zero vectors and $\theta$ is the angle between them, and suppose that $|\underline{u}|$ and $|\underline{v}|$ represent the length of the adjacent sides of a parallelogram, (see figure). We know that:
Area of parallelogram $=$ Base $\times$ Height

$$
=(\text { Base })(h)=|\underline{u}||\underline{v}| \sin \theta
$$

$\therefore$ Area of parallelogram $=|\underline{u} \times \underline{v}|$

(b) Area of Triangle

From figure it is clear that
Area of triangle $=\frac{1}{2}$ (Area of parallelogram)
Area of triangle $=\frac{1}{2}|u \times v|$
where $\underline{u}$ and $\underline{v}$ are vectors along two adjacent sides of the triangle.
Example 20 Find area of the parallelogram whose vertices are $P(0,0,0), Q(-1,2,4), R(2,-1,4)$ and $S(1,1,8)$.
Solution Area of parallelogram $=|P \vec{Q} \times \overrightarrow{P R}|$
Where $|P \vec{Q}|$ and $|P \vec{R}|$ are two adjacent sides of the parallelogram

$$
\begin{aligned}
& \overrightarrow{P Q}=\overrightarrow{O Q}-\overrightarrow{O P}=(-1-0) \underline{i}+(2-0) \underline{j}+(4-0) \underline{k}=-\underline{i}+2 \underline{j}+4 \underline{k} \\
& \overrightarrow{P R}=\overrightarrow{O R}-\overrightarrow{O P}=(2-0) \underline{i}+(-1-0) \underline{j}+(4-0) \underline{k}=2 \underline{i}-\underline{j}+4 \underline{k} \\
& \text { Now } \quad \overrightarrow{P Q} \times \overrightarrow{P R}=\left|\begin{array}{ccc}
\underline{i} & \underline{j} & \underline{k} \\
-1 & 2 & 4 \\
2 & -1 & 4
\end{array}\right|=(8+4) i-(-4-8) j+(1-4) k \\
& =12 i+12 j-3 k
\end{aligned}
$$

$\therefore$ Area of parallelogram $=|\overrightarrow{P Q} \times \overrightarrow{P R}|=|12 i+12 j-3 k|$

$$
=\sqrt{144+144+9}=\sqrt{297} \text { square units }
$$

Example 21 Find the area of the triangle with vertices $A(1,-1,1), B(2,1,-1)$ and $C(-1,1,2)$. Also find a unit vector perpendicular to the plane of triangle $A B C$.
Solution $\overrightarrow{A B}=\overrightarrow{O B}-\overrightarrow{O A}=(2-1) \underline{i}+(1+1) \underline{j}+(-1-1) \underline{k}=\underline{i}+2 \underline{j}-2 \underline{k}$

$$
\begin{aligned}
\overrightarrow{A C} & =\overrightarrow{O C}-\overrightarrow{O A}=(-1-1) \underline{i}+(1+1) \underline{j}+(2-1) \underline{k}=-2 \underline{i}+2 \underline{j}+\underline{k} \\
\overrightarrow{A B} \times \overrightarrow{A C} & =\left|\begin{array}{ccc}
i & j & k \\
1 & 2 & -2 \\
-2 & 2 & 1
\end{array}\right|=(2+4) i-(1-4) j+(2+4) k=6 i+3 j+6 k
\end{aligned}
$$

The area of the parallelogram with adjacent sides $|\overrightarrow{A B}|$ and $|\overrightarrow{A C}|$ and is given by

$$
|\overrightarrow{A B} \times \overrightarrow{A C}|=|6 i+3 j+6 k|=\sqrt{36+9+36}=\sqrt{81}=9
$$

$\therefore \quad$ Area of triangle $=\frac{1}{2}|\overrightarrow{A B} \times \overrightarrow{A C}|=\frac{1}{2}|6 i+3 j+6 k|=\frac{9}{2}$ square units
A unit vector $\perp$ to the plane $A B C=\frac{\overrightarrow{A B} \times \overrightarrow{A C}}{|\overrightarrow{A B} \times \overrightarrow{A C}|}=\frac{1}{9}(6 i+3 j+6 k)=\frac{1}{3}(2 i+j+2 k)$