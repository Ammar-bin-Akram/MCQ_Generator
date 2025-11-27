# Chapter 3: Sequences and Series

## INTRODUCTION

In this unit, students will leam to analyze and solve problems involving arithmetic, geometric, and harmonic sequences and series, including their real-world applications. Students will identify various sequence types, compute finite and infinite sums, and utilize sigma notation. Additionally, they will explore practical scenarios such as motor vehicle leasing, investment planning, and financial calculations. This unit also emphasizes applying these concepts to diverse fields, including healtheare, finance, and traffic modeling. Finally, students will be able to solve both theoretical and reallife problems using sequences and series effectively.
Let us observe the following pattern of numbers:
(i) $5,11,17,23, \ldots$
(ii) $6,12,24,48, \ldots$
(iii) $4,2,0,-2,-4, \ldots$
(iv) $\frac{2}{3}, \frac{4}{9}, \frac{8}{27}, \frac{16}{81}, \ldots$

In example (i), every number (except 5) is formed by adding 6 to the previous numbers. Hence a specific pattern is followed in the arrangement of these numbers. Similarly, in example (ii), every number is obtained by multiplying the previous number by 2. Similar cases are followed in example (iii) and (iv). When a set of numbers follows a pattern and there is a clear rule for finding next number in the pattern, then we have sequence as in above examples.

### 6.1 Sequence

A sequence is a function whose domain is the set $N$ of all natural numbers, whereas the range may be any subset of real numbers or complex numbers. The numbers in a sequence are called its terms. We denote the first term of a sequence as $a_{1}$, second term as $a_{2}$ and so on. The $n^{\text {th }}$ term of a sequence is denoted by $a_{n}$, which may also be referred to as the general term of the sequence, and the terms immediately preceding it are called the $(n-1)^{\text {st }}$ term, the $(n-2)^{\text {nd }}$ term and so on.

### 6.1.1 Finite and Infinite Sequences

1. A sequence which consists of a finite number of terms is called a finite sequence. For example, $2,5,8,11,14,17,20,23$ is a finite sequence of 8 terms.
2. A sequence which consists of an infinite number of terms is called an infinite sequence. For example, $3,10,17,24, \ldots$ is an infinite sequence, or more generally as $3,10,17,24, \ldots, 7 n-4, \ldots$ to show how each term was generated.

Note If a sequence is given, then we can find its $n^{\text {th }}$ term and if the $n^{\text {th }}$ term of a sequence is given then we can find the terms of the sequence.
Example 1 Find the first four terms of the following sequences whose $n^{\text {th }}$ terms are given:
(i) $a_{n}=3 n+1$
(ii) $a_{n}=3 n^{2}-3$

Solution (i) $a_{n}=3 n+1$
Substituting $n=1,2,3$ and 4 we have

$$
a_{1}=3(1)+1=3+1=4
$$

Similarly, $\quad a_{2}=3(2)+1=6+1=7$

$$
\begin{aligned}
& a_{3}=3(3)+1=9+1=10 \\
& a_{4}=3(4)+1=12+1=13
\end{aligned}
$$

The first four terms of the sequence are $4,7,10,13$.
(ii) $a_{n}=3 n^{2}-3$

Substituting $n=1,2,3$ and 4 we have

$$
a_{1}=3(1)^{2}-3=0
$$

Similarly, $\quad a_{2}=3(2)^{2}-3=3(4)-3=12-3=9$

$$
\begin{aligned}
& a_{3}=3(3)^{2}-3=3(9)-3=27-3=24 \\
& a_{4}=3(4)^{2}-3=3(16)-3=48-3=45
\end{aligned}
$$

The first four terms of the sequence are $0,9,24,45$.
Sequences of numbers are also called progressions. Depending on the pattern, the progressions are classified as follows:
(i) Arithmetic progression
(ii) Geometric progression
(iii) Harmonic progression

# EXERCISE 6.1

1. Find the next four terms of each sequence.
(i) $12,16,20, \ldots$
(ii) $3,1,-1, \ldots$
2. Write down the first three terms of each of the following sequences:
(i) $a_{n}=3 n+5$
(ii) $a_{n+1}=4 a_{n}-7$ and $a_{1}=3$
(iii) $a_{n}=(n-3)(n+1)$
(iv) $a_{1}=-1, a_{n+1}=\frac{3}{a_{n}+2}$
(v) $a_{n}=8-\frac{20}{3+n}$
(vi) $a_{1}=1, a_{n+1}=\left(3 a_{n}+2\right)^{2}$
(vii) $a_{n}=(-2 n)^{2}$
(viii) $a_{n}=(-1)^{n} 7 n^{2}$
3. An expression for the $n^{\text {th }}$ triangular number is $\frac{n(n+1)}{2}$. Write down the $15^{\text {th }}$ triangular number. Make a triangle of dots by taking $n=5$.

4. Write down the $n^{\text {th }}$ term of each of the following sequences:
(i) $1,4,9, \ldots$
(ii) $1,1+2,1+2+3, \ldots$
(iii) $a_{1} b_{1}, a_{2} b_{2}, a_{3} b_{3}, \ldots$
(iv) $x, 2 x^{2}, 3 x^{3}, \ldots$
(v) $a_{1}, a_{1}+d, a_{1}+2 d, \ldots$
(vi) $a_{1}, a_{1} r, a_{1} r^{2}, \ldots$
(vii) $\frac{a_{1}}{b_{1}+c_{1}}, \frac{2 a_{2}}{b_{2}+c_{2}}, \frac{3 a_{3}}{b_{3}+c_{3}}, \ldots$
(viii) $\frac{1}{a_{1}}, \frac{1}{a_{1}+d}, \frac{1}{a_{1}+2 d}, \ldots$

# 6.2 Arithmetic Progression or Arithmetic Sequence (A.P.)

A sequence $\left\{a_{n}\right\}$ is called an arithmetic sequence or arithmetic progression (A.P.), if $a_{n}-a_{n-1}$ is the same number for all $n \in N$ and $n>1$. The difference $a_{n}-a_{n-1}(n>1)$ i.e., the difference of two consecutive terms of an A.P., is called the common difference and is usually denoted by $d$.
Thus, an arithmetic progression is a sequence in which each term after the first is obtained by adding fixed constant to the previous term. This fixed constant is called common difference of the arithmetic progression.
For example: Following sequences are in A.P.
(i) $1,3,5,7, \ldots$ (common difference is 2 )
(ii) $54,51,48, \ldots$ (common difference is -3 )

An arithmetic progression with $n$ terms can be written as:

$$
a_{1}, a_{1}+d, a_{1}+2 d, \ldots, a_{1}+(n-1) d
$$

The $n^{\text {th }}$ term of an arithmetic progression can be written as:

$$
a_{n}=a_{1}+(n-1) d
$$

## (i) $1^{n}, 2^{\text {nd }}, 3^{\text {rd }}$ and $n^{\text {th }}$ terms of an A.P. are denoted by $a_{1}, a_{2}, a_{3}$ and $a_{n}$ respectively.
(ii) $n^{\text {th }}$ term from the end of an $A . P$. is $(m-n+1)^{\text {th }}$ term where ' $m$ ' denotes the total number of terms of an A.P.
(iii) Three numbers $a, b, c$ are in $A . P$. if and only if $2 b=a+c$.
(iv) Any term (except first and last) in an A.P. is equal to half of the sum of two terms equidistant from it.
(v) If the term $a_{1}$ is unknown or not given, the $n^{\text {th }}$ term can be written as $a_{n}=a_{m}+(n-m) d, n \geq m$. Note that the subscript of the given term and coefficient of $d$ sum to $n$.
The middle term of an A.P. depends upon the number of terms, for example
(i) $1,3,5,7,9,11$ is an A.P. with $n=6$
(ii) $1,3,5,7,9,11,13$ is an A.P. with $n=7$

i.e., If the total number of terms of an A.P. is even, then there are two middle terms i.e., $\left(\frac{n}{2}\right)^{n}$ and $\left(\frac{n}{2}+1\right)^{n}$ where $n$ represent the number of terms. In example (i) 5,7 are two middle terms.
If the total number of terms of an A.P. is odd, then there is only one middle term i.e., $\left(\frac{n+1}{2}\right)^{n}$ term. In example (ii) 7 is the only middle term.

# 6.2.1 Selection of terms in A.P.

(i) Three consecutive terms of an A.P. can be chosen as $a-d, a, a+d$ or $a, a+d$, or $a+2 d$
(ii) Four consecutive term of an A.P. may be written like $a-3 d, a-d, a+d, a+3 d$ or $a, a+d, a+2 d, a+3 d$.
(iii) Last four consecutive terms if $\ell$ is the last term can be written as below:

$$
\ell-3 d, \ell-2 d, \ell-d, \ell
$$

If each term of an A.P. is increased or decreased, multiplied or divided by same non-zero number, then the resulting sequence is also an A.P. that is, if $a_{1}, a_{2}, a_{3}, \ldots, a_{n}, \ldots$ are in A.P. with common difference $d$ then
(i) $a_{1} \pm k, a_{2} \pm k, \ldots, a_{n} \pm k, \ldots$ are also in A.P. with common difference ' $d$ '.
(ii) $k a_{1}, k a_{2}, \ldots, k a_{n}, \ldots$ are also in A.P. with common difference ' $k d$ '.
(iii) $\frac{a_{1}}{k}, \frac{a_{2}}{k}, \ldots, \frac{a_{n}}{k}, \ldots$ are also in A.P. with common difference $\frac{d}{k}$.
(iv) Term by term addition or subtraction of two A.Ps. is also an A.P. i.e., If $a_{1}, a_{2}, a_{3}, \ldots a_{n}, \ldots$ and $b_{1}, b_{2}, b_{3}, \ldots b_{n}, \ldots$ are in A.P., then $a_{1} \pm b_{1}, a_{2} \pm b_{2}$, $a_{2} \pm b_{3}, \ldots$ are also in A.P.
Example 2 Find the general term and the eleventh term of the A.P. whose first term and the common difference are 2 and -3 respectively. Also write its first four terms.
Solution
Here, $a_{1}=2, d=-3$
We know that $a_{n}=a_{1}+(n-1) d$
So,

$$
\begin{aligned}
a_{n} & =2+(n-1)(-3)=2-3 n+3 \\
a_{n} & =5-3 n
\end{aligned}
$$

Thus, the general term of the A.P. is $5-3 n$

Putting $n=11$ in (i), we have

$$
\begin{aligned}
a_{11} & =5-3(11) \\
& =5-33=-28
\end{aligned}
$$

We can find $a_{2}, a_{3}, a_{4}$ by putting $n=2,3,4$ in (i), that is,

$$
\begin{aligned}
& a_{2}=5-3(2)=-1 \\
& a_{3}=5-3(3)=-4 \\
& a_{4}=5-3(4)=-7
\end{aligned}
$$

Hence, the first four terms of the sequence are: $2,-1,-4,-7$.
Example 3 If the $5^{\text {th }}$ term of an $A . P$. is 13 and $17^{\text {th }}$ term is 49 , find $a_{n}$ and $a_{13}$.
Solution Given that $a_{5}=13$ and $a_{17}=49$
Putting $n=5$ in $a_{n}=a_{1}+(n-1) d$, we have $a_{5}=a_{1}+(5-1) d$

$$
\begin{aligned}
& a_{5}=a_{1}+4 d \\
& 13=a_{1}+4 d \quad\left(\because a_{5}=13\right) \\
& \text { Also } \quad a_{17}=a_{1}+(17-1) d \\
& 49=a_{1}+16 d \quad\left(\because a_{1}+49\right) \\
& 49=\left(a_{1}+4 d\right)+12 d \\
& 49=13+12 d \quad \text { by (i) } \\
& \Rightarrow \quad 12 d=36 \quad \Rightarrow \quad d=3 \\
& \text { From (i), } a_{1}=13-4 d=13-4(3)=13-12=1 \\
& \text { Thus } \quad a_{n}=1+(n-1)(3)=3 n-2 \text { and } \\
& a_{13}=3(13)-2=39-2=37
\end{aligned}
$$

Example 4 Find the number of terms in the A.P. ; if $a_{1}=3, d=7$ and $a_{n}=59$
Solution Using $a_{n}=a_{1}+(n-1) d$, we have

$$
\begin{aligned}
& 59=3+(n-1) \times 7 \quad\left(\because a_{n}=59, a_{1}=3 \text { and } d=7\right) \\
& 56=(n-1) \times 7 \Rightarrow n-1=8 \Rightarrow n=9
\end{aligned}
$$

Thus, the terms in the A.P. are 9.
Example 5 If $a_{n-2}=3 n-11$ find the $n^{\text {th }}$ term of the sequence.
Solution Replacing $n$ by $n+2$, we have

$$
\begin{aligned}
a_{n+2-2} & =3(n+2)-11 \\
a_{n} & =3 n+6-11 \\
a_{n} & =3 n-5
\end{aligned}
$$

# EXERCISE 6.2

1. Find the common difference and write the next two terms of each arithmetic sequence.
(i) $9,16,23, \ldots$
(ii) $5,5+\sqrt{2}, 5+2 \sqrt{2}, \ldots$
2. Write the first three terms of each arithmetic sequence, with given information.
(i) $a_{1}=2, d=13$
(ii) $a_{1}=12, d=-13$
3. Find $a_{n+1}$ and $a_{2 n}$ if $a_{n}=4+3 n$
4. Find the indicated term of each of the following arithmetic sequenecs:
(i) $a_{1}=3, d=7, a_{14}$
(ii) $8,3,-2, \ldots, a_{12}$
5. The $18^{\text {th }}$ and $30^{\text {th }}$ terms of an arithmetic sequence are 367 and 499 respectively. How many terms of this sequence are less than 1000 ?
6. Is 301 a term of the A.P. $5,11,17, \ldots$ ?
7. If $2 x, x+8,3 x+1$ are in A.P., then find the value of $x$
8. Which term of the A.P., $3,8,13, \ldots$ is 123 ?
9. Which term of the A.P., $30,29.5,29, \ldots$ is the first negative term?
10. The $7^{\text {th }}$ and $21^{\text {st }}$ terms of an A.P., are 37 and 107 respectively. Find the A.P. and its $100^{\text {th }}$ term.
11. If $\frac{1}{a-c}, \frac{1}{b-c}, \frac{1}{b-a}$ are in A.P., the show that $\frac{a-b}{a-c}=\frac{a-c}{b-a}$.
12. How many numbers of three digits are divisible by 7 ?
13. Find the $8^{\text {th }}$ term from the end of the A.P., $8,11,14, \ldots, 185$.
14. Find the $n^{\text {th }}$ term of the progression $\left(\frac{3}{7}\right)^{10},\left(\frac{10}{7}\right)^{10},\left(\frac{17}{7}\right)^{10}, \ldots$. Is the progression an A.P.?
15. If the arithmetie progressions $3,10,17, \ldots$ and $63,65,67, \ldots$ are such that their $n^{\text {th }}$ terms are equal, then find the value of $n$.
16. If the $p^{\text {th }}$ term of an A.P. is $q$ and the $q^{\text {th }}$ term is $p$, prove that its $n^{\text {th }}$ term is $(p+q-n)$.
17. If $\frac{1}{a}, \frac{1}{b}$ and $\frac{1}{c}$ are in A.P., show that $b=\frac{2 a c}{a+c}$.
18. If $\frac{1}{a}, \frac{1}{b}$ and $\frac{1}{c}$ are in A.P., show that the common difference is $\frac{a-c}{2 a c}$.
19. If $a_{k}$ and $a_{m}$ denotes two different terms of an A.P., show that its $n^{\text {th }}$ term is $a_{k}+(n-k)\left(\frac{a_{k}-a_{m}}{k-m}\right)$.

20. If $a_{1}, a_{2}, a_{3}, \ldots, a_{n}$ are positive and in A.P., prove that

$$
\frac{1}{\sqrt{a_{1}}+\sqrt{a_{2}}}+\frac{1}{\sqrt{a_{2}}+\sqrt{a_{3}}}+\ldots+\frac{1}{\sqrt{a_{n-1}}+\sqrt{a_{n}}}=\frac{n-1}{\sqrt{a_{1}}+\sqrt{a_{n}}}
$$

21. If the roots of the equation $(b-c) x^{2}+(c-a) x+(a-b)=0$ are equal. Show that $a, b, c$ are in A.P.
22. If the sides of a right-angled triangle are in A.P., find the ratio of its sides.
23. If the $n^{\text {th }}$ term of a progression is a linear expression in $n$, then prove that this progression is an A.P.

# 6.3 Arithmetic Mean (A.M.)

A number $A$ is said to be the A.M. between the two numbers $a$ and $b$ if $a, A, b$ are in A.P. If $d$ is the common difference of this A.P., then $A-a=d$ and $b-A=d$.

$$
\begin{aligned}
& \text { Thus } A-a=b-A \\
& \text { or } \quad 2 A=a+b \\
& \Rightarrow \quad A=\frac{a+b}{2}
\end{aligned} \quad \text { Note if } A_{1} A_{2}, A_{3}, \ldots, A_{n} \text { are said to be } n \text { A.Ms. between two numbers } a \text { and } b \text {, then } \\
& a_{1} A_{1}, A_{2}, A_{3}, \ldots, A_{n}, b \text { are in A.P. }
$$

Example 6 Find three A.Ms. between $\sqrt{2}$ and $3 \sqrt{2}$.
Solution Let $A_{1}, A_{2}, A_{3}$ be three A.Ms. between $\sqrt{2}$ and $3 \sqrt{2}$. Then,

$$
\sqrt{2}, A_{1}, A_{2}, A_{3}, 3 \sqrt{2} \text { are in } A . P
$$

Here $a_{1}=\sqrt{2}, n=5, a_{2}=3 \sqrt{2}$ using $a_{2}=a_{1}+(5-1) d$, we have $3 \sqrt{2}=\sqrt{2}+4 d$

$$
\begin{aligned}
& \Rightarrow \quad d=\frac{2 \sqrt{2}}{4}=\frac{\sqrt{2}}{2}=\frac{1}{\sqrt{2}} \\
& \text { Now } \quad A_{1}=a_{1}+d=\sqrt{2}+\frac{1}{\sqrt{2}}=\frac{2+1}{\sqrt{2}}=\frac{3}{\sqrt{2}} \\
& A_{2}=A_{1}+d=\frac{3}{\sqrt{2}}+\frac{1}{\sqrt{2}}=\frac{4}{\sqrt{2}}=2 \sqrt{2} \\
& A_{3}=A_{2}+d=2 \sqrt{2}+\frac{1}{\sqrt{2}}=\frac{4+1}{\sqrt{2}}=\frac{5}{\sqrt{2}}
\end{aligned}
$$

Therefore, $\frac{3}{\sqrt{2}}, 2 \sqrt{2}, \frac{5}{\sqrt{2}}$ are the three A.Ms. between $\sqrt{2}$ and $3 \sqrt{2}$.

# EXERCISE 6.3

1. Find A.M. between the given numbers:
(i) $2+\sqrt{3} i, 2-\sqrt{3} i$
(ii) $(a+b)^{2},(a-b)^{2}$
2. If $6,11,16$ are three A.Ms. between $a$ and $b$, find $a$ and $b$.
3. Insert five A.Ms. between $\sqrt{2}$ and $\frac{15}{\sqrt{2}}$.
4. The A.M. of two numbers is 7 and their product is 45 . Find the numbers.
5. If $n$ arithmetic means are inserted between $a$ and $b$, prove that $a \geqslant \frac{b-a}{n+1}$, where $d$ is the common difference.
6. If $A$ is the A.M. between $a$ and $b$, prove that $(a-A)^{2}+(A-b)^{2}=\frac{1}{2}(a-b)^{2}$.
7. For what value of $n, \frac{a^{n+1}+b^{n+1}}{a^{n}+b^{n}}$ is the A.M. between $a$ and $b$, where $a \neq b$.

### 6.4 Series

The sum of the terms of a sequence is called the series of the corresponding sequence.
For example, $1+2+3+\cdots+n$ is a finite series of first $n$ natural numbers.
The sum of first $n$ terms of series is denoted by $S_{n}$.
We write, $S_{n}=a_{1}+a_{2}+\cdots+a_{n}$.
Here, $\quad S_{1}=a_{1}$

$$
\begin{aligned}
& S_{2}=a_{1}+a_{2} \\
& S_{3}=a_{1}+a_{2}+a_{3} \\
& S_{n}=a_{1}+a_{2}+a_{3}+\cdots+a_{n} \text { is known as } n^{\text {th }} \text { partial sum. }
\end{aligned}
$$

The sum of the terms of an arithmetic sequence is called an arithmetic series.
To develop a formula for the sum of any arithmetic series, consider

$$
\begin{aligned}
S_{n} & =a_{1}+\left(a_{1}+d\right)+\left(a_{1}+2 d\right)+\cdots+\left(a_{n}-2 d\right)+\left(a_{n}-d\right)+a_{n} \\
S_{n} & =a_{n}+\left(a_{n}-d\right)+\left(a_{n}-2 d\right)+\cdots+\left(a_{1}+2 d\right)+\left(a_{1}+d\right)+a_{1}
\end{aligned}
$$

Thus, $\quad 2 S_{n}=\left(a_{1}+a_{n}\right)+\left(a_{1}+a_{n}\right)+\left(a_{1}+a_{n}\right)+\cdots+\left(a_{1}+a_{n}\right)+\left(a_{1}+a_{n}\right)+\left(a_{1}+a_{n}\right)$

$$
=n\left(a_{1}+a_{n}\right) \quad\left[\text { We have } n \text { terms of }\left(a_{1}+a_{n}\right)\right]
$$

$$
S_{n}=\frac{n}{2}\left(a_{1}+a_{n}\right)
$$

But, $\quad a_{n}=a_{1}+(n-1) d$
Thus, $\quad S_{n}=\frac{n}{2}\left[a_{1}+a_{1}+(n-1) d\right]=\frac{n}{2}\left[2 a_{1}+(n-1) d\right]$

Example 7 Find the sum of the first 100 positive integers.
Solution The series is $1+2+3+\cdots+100$.
Since we can see that $a_{1}=1, a_{n}=100$ and $d=1$.

## Method-1

$$
\begin{aligned}
& S_{n}=\frac{n}{2}\left(a_{1}+a_{n}\right) \\
& S_{100}=\frac{100}{2}(1+100) \\
& S_{100}=50(101) \\
& S_{100}=5050
\end{aligned}
$$

## Method-2

$$
\begin{aligned}
& S_{n}=\frac{n}{2}\left[2 a_{1}+(n-1) d\right] \\
& S_{100}=\frac{100}{2}[2(1)+(100-1) 1] \\
& S_{100}=50(101) \\
& S_{100}=5050
\end{aligned}
$$

Example 8 Find the $19^{\text {th }}$ term and the partial sum of 19 terms of the arithmetic series:

$$
2+\frac{7}{2}+5+\frac{13}{2}+\cdots
$$

Solution Here, $a_{1}=2, a_{2}=\frac{7}{2}$ and $d=a_{2}=a_{1}=\frac{7}{2}-2=\frac{3}{2}$
Using $\quad a_{n}=a_{1}+(n-1) d$
Substitute $n=19$

$$
\begin{aligned}
& a_{19}=2+(19-1) \frac{3}{2} \\
& 2+18\left(\frac{3}{2}\right)=2+27=29
\end{aligned}
$$

Using $\quad S_{n}=\frac{n}{2}\left(a_{1}+a_{n}\right)$

$$
S_{19}=\frac{19}{2}\left(a_{1}+a_{19}\right)
$$

$$
S_{19}=\frac{19}{2}(2+29)=\frac{19}{2}(31)=\frac{589}{2}
$$

Example 9 Find the arithmetic series if its fifth term is 19 and $S_{4}=a_{9}+1$.
Solution Given that $a_{5}=19$, that is,

$$
a_{1}+4 d=19
$$

Using the other given condition, we have

$$
S_{4}=\frac{4}{2}\left[2 a_{1}+(4-1) d\right]=a_{9}+1
$$

$$
\begin{aligned}
4 a_{1}+6 d & =a_{1}+8 d+1 \\
3 a_{1}-1 & =2 d
\end{aligned}
$$

Substituting $2 d=3 a_{1}-1$ in (i), we have

$$
\begin{aligned}
a_{1}+2\left(3 a_{1}-1\right) & =19 \\
7 a_{1}=21 & \Rightarrow a_{1}=3
\end{aligned}
$$

From (i), we have,

$$
\begin{aligned}
4 d & =19-a_{1}=19-3=16 \\
\Rightarrow \quad d & =4
\end{aligned}
$$

Thus, the series is $3+7+11+\cdots$.
Example10 How many terms of the series $-9-6-3+0+\ldots$ amount to 66 ?
Solution Here, $a_{1}=-9$ and $d=-6-(-9)=3$.

$$
\text { Let } S_{n}=66
$$

Using $S_{n}=\frac{n}{2}\left[2 a_{1}+(n-1) d\right]$, we have

$$
\begin{aligned}
& 66=\frac{n}{2}[2(-9)+(n-1) 3] \\
& 132=n[3 n-21] \Rightarrow 132=3 n(n-7) \Rightarrow 44=n(n-7) \\
& n^{2}-7 n-44=0 \\
& \Rightarrow \quad n=\frac{7 \pm \sqrt{49+176}}{2} \\
& =\frac{7 \pm \sqrt{225}}{2}=\frac{7 \pm 15}{2} \Rightarrow n=11,-4
\end{aligned}
$$

But $n$ cannot be negative in this case, so $n=11$, that is, the sum of eleven terms is 66 .
Example11 Find the first three terms of an arithmetic series in which $a_{1}=9, a_{n}=105$ and $S_{n}=741$.
Solution Step - I: Since we know $a_{1}, a_{n}$ and $S_{n}$,
We use $S_{n}=\frac{n}{2}\left(a_{1}+a_{n}\right)$ to find $n$.

$$
741=\frac{n}{2}(9+105)
$$

$$
741=57 n
$$

$$
13=n
$$

Step - II: Find $d$.

$$
\begin{aligned}
& a_{n}=a_{1}+(n-1) d \\
& 105=9+(13-1) d \\
& 96=12 d \\
& 8=d
\end{aligned}
$$

Step - III: Use $d$ to determine $a_{2}$ and $a_{3}$.

$$
a_{2}=9+8=17, \quad a_{3}=17+8=25
$$

The first three terms are 9,17 and 25 .

# EXERCISE 6.4

1. Sum the series:
(i) $3+6+9+\cdots+a_{20}$
(ii) $\frac{4}{\sqrt{5}}+\sqrt{5}+\frac{6}{\sqrt{5}}+\cdots+a_{n}$
2. Find $S_{n}$ for each arithmetic series:
(i) $a_{1}=4, n=25, a_{n}=100$
(ii) $a_{1}=40, n=20, d=-1$
(iii) $a_{n}=52, n=21, d=-4$
3. Find $a_{1}$ for the arithmetic series: $d=8, n=19, S_{n}=1786$.
4. How many terms of the series: $96+93+90+\sim$ amount to 1071.
5. If the three sides of a right-angled triangle having perimeter 36 cm are in A.P., find them.
6. Sum the series
(i) $3+5-7+9+11-13+15+17-19+\cdots$ to $3 n$ terms.
(ii) $1+4-7+10+13-16+19+22-25+\cdots$ to $3 n$ terms.
7. Find the sum of 20 terms of the series whose $r^{\text {th }}$ term is $3 r+1$.
8. The $5^{\text {th }}$ and $9^{\text {th }}$ term of an A.P. are 11 and 17 respectively. Find the sum of 20 terms.
9. Obtain the sum of all integers in the first 1000 positive integers which are neither divisible by 5 nor by 2 .
10. The sum of 9 terms of an A.P. is 171 and its eighth term is 31 . Find the series.
11. The $5^{\text {th }}$ term of an arithmetic progression is 21 and the sum of first six terms is 90 . Find the $18^{\text {th }}$ term.
12. The sum of three numbers in an A.P. is 24 and their product is 440 . Find the numbers.
13. The first four terms of an A.P. are $2,6,10$ and 14 . Find the least number of terms needed so that the sum of the terms is greater than 2000.
14. Find four numbers in A.P. whose sum is 32 and the sum of whose squares is 276.
15. Find the five numbers in A.P. whose sum is 25 and the sum of whose squares is 135 .
16. If $\frac{1}{a+b} \cdot \frac{1}{c+a} \cdot \frac{1}{b+c}$ are in A.P. then show that $a^{2}, b^{2}, c^{2}$ are in A.P.

17. The sum of the first four terms of an A.P. is 56 . The sum of the last four terms is 112. If its first term is 11 , then find number of terms.
18. The first, second and last terms of an A.P. are $a, b$ and $c$ respectively. Show that the sum of A.P. is $\frac{(b+c-2 a)(c+a)}{2(b-a)}$.
19. Show that the sum of $n$ A.Ms. between $a$ and $b$ is $n$ times the single A.M. between them.

# 6.5 Geometric Progression (G.P.)

A geometric progression or geometric sequence is a sequence fixed in which each term after the first is found by multiplying the previous term by a non-zero constant $r$ called common ratio.
Like arithmetic progression, we can label the terms of a geometric sequence as $a_{1}, a_{2}, a_{3}$ and so on, $a_{1} \neq 0$. The $n^{\text {th }}$ term is $a_{n}$ and the previous term is $a_{n-1}$. So, $a_{n}=r\left(a_{n-1}\right)$. Thus, $r=\frac{a_{n}}{a_{n-1}}$. That is, the common ratio can be found by dividing any term by its previous term.

### 6.5.1 Rule for $n$th term of a G.P.

Each term after the first term is an $r$ multiple of its preceding term. Thus, we have,

$$
\begin{aligned}
& a_{2}=a_{1} r=a_{1} r^{2-1} \\
& a_{3}=a_{2} r=\left(a_{1} r\right) r=a_{1} r^{2}=a_{1} r^{3-1} \\
& a_{4}=a_{2} r=\left(a_{1} r^{2}\right) r=a_{1} r^{3}=a_{1} r^{4-1} \\
& \vdots \\
& a_{n}=a_{1} r^{n-1} \text { which is the general term of a G.P. }
\end{aligned}
$$

### 6.5.2 Properties of G.P.

(i) If each term of a G.P. is multiplied or divided by the same non-zero number, then the resulting sequence is also a G.P. that is if $g_{1}, g_{2}, g_{3}, \ldots, g_{n}, \ldots$ are in G.P. and $k$ is a non-zero number, then
(a) $k g_{1}, k g_{2}, k g_{3}, \ldots, k g_{n}, \ldots$ are also in G.P.
(b) $\frac{g_{1}}{k}, \frac{g_{2}}{k}, \frac{g_{3}}{k}, \ldots, \frac{g_{n}}{k}, \ldots$ are also in G.P.
(ii) The reciprocals of the term of a G.P. also form a G.P. that is if $a, b, c$ are in G.P., then $\frac{1}{a}, \frac{1}{b}, \frac{1}{c}$ are also in G.P.

(iii) If each term of a G.P. is raised to the same power, the resulting numbers also form a G.P. that is, if $a, b, c$ are in G.P., then $a^{n}, b^{n}, c^{n}$ are also in G.P.
(iv) Three numbers $a, b, c$ are in G.P. if and only if $b^{2}=a c$.
(v) If the set of positive numbers $a_{1}, a_{2}, a_{3}, \ldots, a_{n}, \ldots$ are in G.P., then $\log a_{1}, \log a_{2}$, $\log a_{3}, \ldots, \log a_{n}, \ldots$ are in A.P. and vice-versa.
(vi) Term by term multiplication or division of two G.Ps. are again in G.P. i.e., if $a_{1}, a_{2}, a_{3} \ldots, a_{n}$, and $b_{1}, b_{2}, b_{3}, \ldots, b_{n}$, are in G.P. then $a_{1} b_{1}, a_{2} b_{2}, a_{3} b_{3}, \ldots$, $a_{n} b_{n}$ and $\frac{a_{1}}{b_{1}}, \frac{a_{2}}{b_{2}}, \frac{a_{3}}{b_{3}}, \ldots, \frac{a_{n}}{b_{n}}$ are also in G.P.
Example 12 Find the eighth term of a geometric sequence for which $a_{1}=-3$ and $r=-2$.
Solution Here, $a_{1}=-3, r=-2, n=8$

$$
\begin{aligned}
& a_{n}=a_{1} \cdot r^{n-1} \\
& a_{8}=(-3) \cdot(-2)^{8-1} \\
& a_{8}=(-3) \cdot(-128) \\
& a_{8}=384
\end{aligned}
$$

Example 13 Find the $n^{\text {th }}$ term of the G.P., 3, 12, 48, ...
Solution Here $a_{1}=3, r=4$

$$
\begin{aligned}
& a_{n}=a_{1} \cdot r^{n-1} \\
& a_{n}=3 \cdot 4^{n-1}
\end{aligned}
$$

Example 14 Find the tenth term of the G.P., for which $a_{4}=108$ and $r=3$.
Solution Step - 1: Find $a_{1}$.
Here, $n=4, r=3, a_{4}=108$

$$
\begin{aligned}
a_{n} & =a_{1} \cdot r^{n-1} \\
a_{4} & =a_{1} \cdot 3^{4-1} \\
108 & =27 a_{1} \\
4 & =a_{1} \\
a_{1} & =4
\end{aligned}
$$

Step - 2: Find $a_{10}$.
Here, $n=10, a_{1}=4, r=3$

$$
\begin{aligned}
& a_{n}=a_{1} \cdot r^{n-1} \\
& a_{10}=4 \cdot 3^{10-1} \\
& a_{10}=78,732
\end{aligned}
$$

Example 15 Find the $5^{\text {th }}$ term of the G.P., 3, 6, 12, ....
Solution Here $a_{1}=3, a_{2}=6$, therefore, $r=\frac{a_{2}}{a_{1}}=\frac{6}{3}=2$.

Using $a_{n}=a_{1} r^{n-1}$ for $n=5$, we have

$$
a_{5}=a_{1} r^{5-1}=3 \cdot 2^{5-1}=3 \cdot 2^{4}=48
$$

Example16 Find $a_{n}$ if $a_{6}=\frac{8}{27}$ and $a_{7}=\frac{-64}{729}$ of a G.P.
Solution: To find $a_{n}$ we have to find $a_{1}$ and $r$.

Using $\quad a_{n}=a_{1} r^{n-1}$

$$
a_{4}=a_{1} r^{4-1}=a_{1} r^{3}, \text { so } a_{1} r^{3}=\frac{8}{27}
$$

and $\quad a_{7}=a_{1} r^{7-1}=a_{1} r^{6}$, so $a_{1} r^{6}=\frac{-64}{729}$
(iii)

Thus, $\quad \frac{a_{1} r^{6}}{a_{1} r^{3}}=\frac{\frac{-64}{729}}{\frac{8}{27}}=\frac{-8}{27} \quad$ or $\quad r^{3}=\left(\frac{-2}{3}\right)^{3}$
$\Rightarrow \quad r=-\frac{2}{3}$
(taking only real value of $r$ )
Put $r^{3}=-\frac{8}{27}$ in (ii), to obtain $a_{1}$ that is,

$$
a_{1}\left(-\frac{8}{27}\right)=\frac{8}{27} \Rightarrow a_{1}=-1
$$

Now putting $a_{1}=-1$ and $r=\frac{-2}{3}$ in (i), we get

$$
a_{4}=(-1)\left(-\frac{2}{3}\right)^{n-1}=(-1)(-1)^{n-1} \cdot\left(\frac{2}{3}\right)^{n-1}=(-1)^{n}\left(\frac{2}{3}\right)^{n-1}
$$

# EXERCISE 6.5

1. Find the $6^{\text {th }}$ term of the G.P.: $-6,-3, \frac{-3}{2}, \cdots$.
2. Find the $8^{\text {th }}$ term of the sequence, $3,3^{2}, 3^{3}, \cdots$.
3. The $n^{\text {th }}$ terms of the sequences $1,2,4,8, \cdots$ and $256,128,64, \cdots$ are equal. Find the value of $n$.
4. Find the first five terms of each sequence described:
(i) $a_{1}=243, r=\frac{1}{3}$
(ii) $a_{1}=579, r=-\frac{1}{2}$

5. Find the $12^{\text {th }}$ term of $1+i, 2 i,-2+2 i, \cdots$.
6. If the $4^{\text {th }}$ and $9^{\text {th }}$ terms of a G.P. are 54 and 13122 respectively. Find the G.P. Also find its general term.
7. If $a, b, c, d$ are in G.P., prove that:
(i) $a-b, b-c, c-d$ are in G.P.
(ii) $a^{2}-b^{2}, b^{2}-c^{2}, c^{2}-d^{2}$ are in G.P.
(iii) $a^{2}+b^{2}, b^{2}+c^{2}, c^{2}+d^{2}$ are in G.P.
8. If $(p+q)^{\text {th }}$ term of a G.P. is $m$ and $(p-q)^{\text {th }}$ term is $n$, then find the $p^{\text {th }}$ term.
9. Find three consecutive numbers in G.P. whose sum is 26 and their product is 216.
10. The $3^{\text {rd }}$ term of a G.P. is the square of $1^{\text {st }}$ term. If the $2^{\text {nd }}$ term is 9 then find the $6^{\text {th }}$ term.
11. If $\frac{1}{a}, \frac{1}{b}$ and $\frac{1}{c}$ are in G.P. Show that the common ratio is $\pm \sqrt{\frac{a}{c}}$.
12. If the numbers 1,4 and 3 are subtracted from three consecutive terms of an A.P., the resulting numbers are in G.P. Find the original numbers if their sum is 21.
13. If three consecutive numbers in A.P. are increased by $1,4,15$ respectively, the resulting numbers are in G.P. Find the original numbers if their sum is 6 .
14. If $p^{\text {th }}, q^{\text {th }}$ terms of a G.P. are $q$ and $p$ respectively, show that $(p+q)^{\text {th }}$ term is $\left(q^{p}+p^{q}\right)^{\frac{1}{p-1}}$.
15. If $a, 2 a+2,3 a+3, \ldots$ are in G.P., then find the fifth term.

# 6.6 Geometric Mean (G.M.)

A number $G$ is said to be a geometric mean (G.M.) between two numbers $a$ and $b$ if $a$, $G, b$ are in G.P. Therefore

$$
\begin{aligned}
& \frac{G}{a}=\frac{b}{G} \\
& \Rightarrow \quad G^{2}=a b \\
& \Rightarrow \quad G= \pm \sqrt{a b}
\end{aligned} \quad \text { Note } G_{1}, G_{2}, G_{3}, \ldots, G_{a} \text { are said to be } n
$$

G.Ms. between two numbers $a$ and $b$ if $a$, $G_{1}, G_{2}, G_{3}, \ldots, G_{a}, b$ are in G.P.

Example 17 Insert three G.Ms. between 2 and $\frac{1}{2}$.
Solution Let $G_{1}, G_{2}, G_{3}$ be three G.Ms. between 2 and $\frac{1}{2}$. Therefore

$2, G_{1}, G_{2}, G_{3}, \frac{1}{2}$ are in G.P. Here $a_{1}=2, a_{2}=\frac{1}{2}$ and $n=5$.
Using $a_{n}=a_{1} r^{n-1}$ we have

$$
a_{2}=a_{1} r^{2-1} \text { that is, } a_{2}=a_{1} r^{4}
$$

Now substituting the values of $a_{2}$ and $a_{1}$ in (i) we have

$$
\frac{1}{2}=2 r^{4} \quad \text { or } \quad r^{4}=\frac{1}{4}
$$

Taking square root of (ii), we get

$$
r^{2}= \pm \frac{1}{2}
$$

We have, $r^{2}=\frac{1}{2} \quad$ or $\quad r^{2}=-\frac{1}{2}=\frac{i^{2}}{2}\left(\because-1=i^{1}\right)$
$\Rightarrow \quad r= \pm \frac{1}{\sqrt{2}} \quad$ or $\quad r= \pm \frac{1}{\sqrt{2}} i$
When $\quad r=\frac{1}{\sqrt{2}}$, then $G_{1}=2\left(\frac{1}{\sqrt{2}}\right)=\sqrt{2}, G_{2}=2\left(\frac{1}{\sqrt{2}}\right)^{2}=1, \quad G_{3}=2\left(\frac{1}{\sqrt{2}}\right)^{2}=\frac{1}{\sqrt{2}}$
When $\quad r=\frac{-1}{\sqrt{2}}$, then $G_{1}=2\left(\frac{-1}{\sqrt{2}}\right)=-\sqrt{2}, G_{2}=2\left(\frac{-1}{\sqrt{2}}\right)^{2}=1, \quad G_{3}=2\left(\frac{-1}{\sqrt{2}}\right)^{2}=-\frac{1}{\sqrt{2}}$
When $\quad r=\frac{i}{\sqrt{2}}$, then $G_{1}=2\left(\frac{i}{\sqrt{2}}\right)=\sqrt{2} i, G_{2}=2\left(\frac{i}{\sqrt{2}}\right)^{2}=-1, G_{3}=2\left(\frac{i}{\sqrt{2}}\right)^{2}=-\frac{i}{\sqrt{2}}$
When $\quad r=\frac{-i}{\sqrt{2}}$, then $G_{1}=2\left(\frac{-i}{\sqrt{2}}\right)=-\sqrt{2} i, G_{2}=2\left(\frac{-i}{\sqrt{2}}\right)^{2}=-1, G_{3}=2\left(\frac{-i}{\sqrt{2}}\right)^{2}=\frac{i}{\sqrt{2}}$
Note The real values of $r$ are usually taken but here other cases are considered to widen the outlook of the students.

# EXERCISE 6.6

1. Find G.M. between:
(i) -2 and 8
(ii) $-2 i$ and $8 i$
(iii) 6 and 9
2. Insert four real geometric means between 3 and 96 .
3. If both $x$ and $y$ are positive distinct real numbers, show that the geometric mean between $x$ and $y$ is less than their arithmetic mean.
4. For what value of $n, \frac{a^{n}+b^{n}}{a^{n-1}+b^{n-1}}$ is the positive geometric mean between $a$ and $b$ ?

5. The A.M. of two positive integral numbers exceeds their (positive) G.M. by 2 and their sum is 20 , find the numbers.
6. The A.M. between two numbers is 5 and their (positive) G.M. is 4 . Find the numbers.
7. The arithmetic mean between two positive numbers $a$ and $b$ is double their geometric mean. Prove that $a: b=2+\sqrt{3}: 2-\sqrt{3}$.
8. If one geometric mean $G$ and two arithmetic means $p$ and $q$ are inserted between two positive numbers, show that $G^{2}=(2 p-q)(2 q-p)$.

# 6.7 Geometric Series

Suppose you e-mail an Islamic quote to three friends on Monday. Each of those friends send it to three of their friends on Tuesday. Each person who receives the quote on Tuesday sends it to three more people on Wednesday and so on.
Notice that every day, the number of people who read your Islamic quote is three times the number that read it the day before. By Sunday, the number of people, including yourself, who have read the quote is $1+3+9+27+81+243+729+2187$ or 3280 . The numbers $1,3,9,27,81,243,729$ and 2187 form a geometric sequence in which $a_{1}=1$ and $r=3$. The indicated sum of the numbers in the sequence, $1+3+9+27+$ $81+243+729+2187$ is called a geometric series.

The sum of a geometric progression can be written as: $S_{n}=\frac{a_{1}\left(1-r^{n}\right)}{1-r}, r \neq 1$
To develop a formula for the sum of a geometric series, consider

$$
\begin{aligned}
& S_{n}=a_{1}+a_{1} r+a_{1} r^{2}+\cdots+a_{1} r^{n-3}+a_{1} r^{n-2}+a_{1} r^{n-1} \\
& r S_{n}=a_{1} r+a_{1} r^{2}+\cdots+a_{1} r^{n-3}+a_{1} r^{n-2}+a_{1} r^{n-1}+a_{1} r^{n}
\end{aligned}
$$

Subtracting (ii) from (i), we get

$$
S_{n}-r S_{n}=a_{1}-a_{1} r^{n}
$$

Note
If $r=1$, then $S_{n}=n a$.

$$
\begin{aligned}
S_{n}(1-r) & =a_{1}\left(1-r^{n}\right) \\
S_{n} & =\frac{a_{1}\left(1-r^{n}\right)}{1-r}, r \neq 1
\end{aligned}
$$

Example 18 Find the sum of $n$ terms of the geometric series if $a_{n}=(-3)\left(\frac{2}{5}\right)^{n}$.
Solution We can write $(-3)\left(\frac{2}{5}\right)^{n}$ as:

$$
-3\left(\frac{2}{5}\right)\left(\frac{2}{5}\right)^{n-1}=\left(-\frac{6}{5}\right)\left(\frac{2}{5}\right)^{n-1}, \text { that is } a_{n}=\left(-\frac{6}{5}\right)\left(\frac{2}{5}\right)^{n-1}
$$

comparing $\left(-\frac{6}{5}\right)\left(\frac{2}{5}\right)^{n-1}$ with $a_{1} r^{n-1}$, we have $a_{1}=-\frac{6}{5}$ and $r=\frac{2}{5}$
Thus,

$$
\begin{aligned}
S_{n} & =\frac{a_{1}\left(1-r^{n}\right)}{1-r}=\frac{-\frac{6}{5}\left[1-\left(\frac{2}{5}\right)^{n}\right]}{1-\frac{2}{5}} \\
& =\left(-\frac{6}{5}\right)\left(\frac{5}{3}\right)\left[1-\left(\frac{2}{5}\right)^{n}\right]=(-2)\left[1-\left(\frac{2}{5}\right)^{n}\right]
\end{aligned}
$$

# EXERCISE 6.7

1. Find the sum of first 15 terms of the G.P., $1, \frac{1}{3}, \frac{1}{9}, \cdots$.
2. The $3^{\text {rd }}$ term of a G.P. is 16 and the $6^{\text {th }}$ term is -128 . Find the first term and the sum of the first seven terms.
3. Sum to $n$ terms the series:
(i) $0.2+0.22+0.222+\cdots$
(ii) $3+33+333+\cdots$
4. Sum to $n$ terms the series:
(i) $1+(a+b)+\left(a^{2}+a b+b^{2}\right)+\left(a^{3}+a^{2} b+a b^{2}+b^{3}\right)+\cdots$
(ii) $r+(1+k) r^{2}+\left(1+k+k^{2}\right) r^{3}+\cdots$
5. Sum the series $2+(1-i)+\binom{1}{i}+\cdots$ to 8 terms.
6. Show that the ratio of the sum of first $n$ terms of a G.P. to the sum of terms from $(n+1)^{\text {th }}$ to $(2 n)^{\text {th }}$ term is $\frac{1}{r^{n}}$, where $r$ is the common ratio of the G.P.

# 6.8 Arithmetico-Geometric Progression (A.G.P.)

Suppose $a_{1}, a_{2}, a_{3}, \ldots, a_{n}, \ldots$ is an A.P., and $b_{1}, b_{2}, b_{3}, \ldots, b_{n}, \ldots$ is a G.P. then the sequence formed by multiplying the corresponding terms of A.P. and G.P., that is, $a_{1} b_{1}$, $a_{2} b_{2}, a_{3} b_{3}, \ldots, a_{n} b_{n}, \ldots$ is said to be an arithmetico-geometric sequence.
Consider an A.P., $a, a+d, a+2 d, \ldots,\{a+(n-1) d\}$ and a G.P., $b, b r, b r^{2}, \ldots, b r^{n-1}$ where $r \neq 1$.
Multiplying the corresponding terms of A.P. and G.P., we get an arithmeticogeometric sequence

$$
a b,(a+d) b r,(a+2 d) b r^{2}, \ldots,\{a+(n-1) d\} b r^{n-1}
$$

Note that the $n^{\text {th }}$ term of arithmetico-geometric sequence is product of $n^{\text {th }}$ term of A.P. and $n^{\text {th }}$ term of G.P.

### 6.8.1 Arithmetico-Geometric Series

Sum of the terms of arithmetico-geometric sequence is called arithmetico-geometric series. Thus, arithmetico-geometric series has the form

$$
a b+(a+d) b r+(a+2 d) b r^{2}+\cdots+\{a+(n-1) d\} b r^{n-1}
$$

Sum of first $n$ Terms of Arithmetico-Gemetric Series
Let $\quad S_{n}=a b+(a+d) b r+(a+2 d) b r^{2}+\cdots+[a+(n-1) d] b r^{n-1}$
Then $r S_{n}=\quad a b r+(a+d) b r^{2}+\cdots+[a+(n-2) d] b r^{n-1}+[a+(n-1) d] b r^{n} \quad$ (ii)
Subtracting (ii) from (i), we get

$$
\begin{aligned}
(1-r) S_{n} & =a b+\left[d b r+d b r^{2}+\cdots+d b r^{n-1}\right]-[a+(n-1) d] b r^{n} \\
& =a b+\frac{d b r\left(1-r^{n-1}\right)}{1-r}-[a+(n-1) d] b r^{n} \\
& =a b+\frac{d b r}{1-r}-\frac{d b r^{n}}{1-r}-[a+(n-1) d] b r^{n} \\
S_{n} & =\frac{a b}{1-r}+\frac{d b r}{(1-r)^{2}}-\frac{d b r^{n}}{(1-r)^{2}}-\frac{[a+(n-1) d] b r^{n}}{1-r}
\end{aligned}
$$

which is the sum of the $n$ terms of arithmetico-geometric series.

### 6.8.2 Sum to Infinity of Arithmetico-Geometric Series

If $|r|<1$, then $r^{n} \rightarrow 0$ and $n r^{n} \rightarrow 0$ as $n \rightarrow \infty$
Therefore, (iii) reduces to $S_{\infty}=\frac{a b}{1-r}+\frac{d b r}{(1-r)^{2}}$
which is the sum to infinity of arithmetico-geometric series.

Example 19 Sum the series upto $n$ terms: $2 \cdot 1+3 \cdot 2+4 \cdot 4+5 \cdot 8+\cdots$
Solution Let $S_{n}=2 \cdot 1+3 \cdot 2+4 \cdot 2^{2}+5 \cdot 2^{3}+\cdots$ to $n$ terms
$n^{\text {th }}$ term of the A.P., $2,3,4,5, \cdots$ is $a_{1}+(n-1) d=2+(n-1)(1)$

$$
=2+n-1=n+1
$$

$n^{\text {th }}$ term of the G.P., $1,2,2^{2}, 2^{3}, \cdots$ is $a_{1} r^{n-1}=1 \cdot 2^{n-1}=2^{n-1}$
So, $\quad S_{n}=2 \cdot 1+3 \cdot 2+4 \cdot 2^{2}+5 \cdot 2^{3}+\cdots+(n+1) 2^{n-1}$
Multiplying both sides by common ratio of G.P., we get

$$
2 S_{n}=\quad 2 \cdot 2+3 \cdot 2^{2}+4 \cdot 2^{3}+5 \cdot 2^{4}+\cdots+(n) 2^{n-1}+(n+1) 2^{n}
$$

Subtracting (ii) from (i), we get

$$
\begin{aligned}
S_{n}-2 S_{n} & =2 \cdot 1+(3-2) \cdot 2+(4-3) \cdot 2^{2}+(5-4) \cdot 2^{3}+\cdots+(n+1-n) 2^{n-1}-(n+1) 2^{n} \\
-S_{n} & =2 \cdot 1+1 \cdot 2+1 \cdot 2^{2}+1 \cdot 2^{3}+\cdots+1 \cdot 2^{n-1}-(n+1) 2^{n} \\
-S_{n} & =2+\left\{2+2^{2}+2^{3}+\cdots+2^{n-1}\right\}-(n+1) 2^{n} \\
-S_{n} & =2+\frac{2\left(2^{n-1}-1\right)}{2-1}-(n+1) \cdot 2^{n} \\
-S_{n} & =2+2^{n}-2-n \cdot 2^{n}-2^{n} \\
-S_{n} & =-n \cdot 2^{n} \\
S_{n} & =n \cdot 2^{n}
\end{aligned}
$$

Example 20 Sum the series upto $n$ terms: $2+\frac{4}{3}+\frac{6}{9}+\frac{8}{27}+\cdots$
Solution Let $S_{n}=2+\frac{4}{3}+\frac{6}{9}+\frac{8}{27}+\cdots$ to $n$ terms
$n^{\text {th }}$ term of the A.P., $2,4,6,8, \ldots$ is $2+(n-1)(2)$

$$
=2+2 n-2=2 n
$$

$n^{\text {th }}$ term of the G.P., $1, \frac{1}{3}, \frac{1}{9}, \frac{1}{27}, \cdots$ is $(1)\left(\frac{1}{3}\right)^{-1}=\frac{1}{3^{n-1}}$
So, $\quad S_{n}=2+\frac{4}{3}+\frac{6}{9}+\frac{8}{27}+\cdots+\frac{2 n}{3^{n-1}}$

$$
\frac{1}{3} S_{n}=\frac{2}{3}+\frac{4}{9}+\frac{6}{27}+\cdots+\frac{2 n-2}{3^{n-1}}+\frac{2 n}{3^{n}}
$$

Subtracting (ii) from (i), we get

$$
\begin{aligned}
& \left(1-\frac{1}{3}\right) S_{n}=2+\frac{4-2}{3}+\frac{6-4}{9}+\frac{8-6}{27}+\cdots+\frac{2 n-2 n+2}{3^{n-1}}-\frac{2 n}{3^{n}} \\
& \frac{2}{3} S_{n}=2+\left[\frac{2}{3}+\frac{2}{9}+\frac{2}{27}+\cdots+\frac{2}{3^{n-1}}\right]-\frac{2 n}{3^{n}} \\
& \frac{2}{3} S_{n}=2+\left[\frac{\frac{2}{3}\left\{1-\left(\frac{1}{3}\right)^{n-1}\right\}}{1-\frac{1}{3}}\right]-\frac{2 n}{3^{n}} \\
& =2+\frac{\frac{2}{3}\left\{1-\left(\frac{1}{3}\right)^{n-1}\right\}}{\frac{2}{3}}-\frac{2 n}{3^{n}} \\
& =2+1-\left(\frac{1}{3}\right)^{n-1}-2 n\left(\frac{1}{3}\right)^{n} \\
& \frac{2}{3} S_{n}=3-\left(\frac{1}{3}\right)^{n-1}-2 n\left(\frac{1}{3}\right)^{n} \\
& S_{n}=\frac{9}{2}-\frac{3}{2}\left(\frac{1}{3}\right)^{n-1}-3 n\left(\frac{1}{3}\right)^{n}
\end{aligned}
$$

Example 21 Find the sum to $n$ terms of the series: $1+2 x+3 x^{2}+4 x^{3}+\ldots$ where $x \neq 1$. If $|x|<1$, sum the series to infinity.
Solution Let $S_{n}=1+2 x+3 x^{2}+4 x^{3}+\cdots+n x^{n-1}$

$$
\therefore \quad x S_{n}=\quad x+2 x^{2}+3 x^{3}+\cdots+(n-1) x^{n-1}+n x^{n}
$$

Subtracting (ii) from (i), we get

$$
\begin{aligned}
(1-x) S_{n} & =1+x+x^{2}+x^{3}+\cdots+x^{n-1}-n x^{n} \\
& =\frac{1\left(1-x^{n}\right)}{1-x}-n x^{n} \\
& =\frac{1-x^{n}-n(1-x) x^{n}}{1-x}
\end{aligned}
$$

$$
\begin{aligned}
& =\frac{1-x^{n}-n x^{n}+n x^{n+1}}{1-x} \\
(1-x) S_{n} & =\frac{1-(n+1) x^{n}+n x^{n+1}}{1-x} \\
S_{n} & =\frac{1-(n+1) x^{n}+n x^{n+1}}{(1-x)^{2}}
\end{aligned}
$$

If $|x|<1$, then $x^{n} \rightarrow 0, n x^{n} \rightarrow 0$ as $n \rightarrow \infty$

$$
\therefore \quad S_{\infty}=\frac{1}{(1-x)^{2}}
$$

# EXERCISE 6.8

1. Find the $8^{\text {th }}$ term of the arithmetico-geometric sequence, where the arithmetic part is $1,4,7, \ldots$ and the geometric part is $5,10,20$.
2. Find the $n^{\text {th }}$ term of the arithmetico-geometric sequence, where the arithmetic part is $3,7,11, \ldots$ and the geometric part is $3,6,18, \cdots$.
3. Consider the arithmetico-geometric sequence defined by arithmetic part:
$a_{n+1}=2 n+5$ and geometric part $b_{n-2}=\frac{1}{9}(-3)^{n}$. Find the $n^{\text {th }}$ term and the sum of first three terms of the arithmetico-geometric sequence.
4. Sum to $n$ terms the following series:
(i) $1 \cdot 2+3 \cdot 4 \pm 5 \cdot 8+7 \cdot 16+\cdots$
(ii) $2 \cdot 3+4 \cdot 3^{2}+6 \cdot 3^{3}+8 \cdot 3^{4}+\ldots$
(iii) $2+\frac{5}{4}+\frac{8}{4^{2}}+\frac{11}{4^{3}}+\cdots$
(iv) $1+\frac{3}{5}+\frac{5}{5^{2}}+\frac{7}{5^{3}}+\cdots$
(v) $1+\frac{4}{3}+\frac{7}{9}+\frac{10}{27}+\cdots$
5. Sum the following infinite series:
(i) $1+\frac{3}{2}+\frac{5}{4}+\frac{7}{8}+\cdots$
(ii) $2+\frac{5}{3}+\frac{8}{9}+\frac{11}{27}+\cdots$
6. Show that $2^{\frac{1}{2}} \cdot 4^{\frac{1}{4}} \cdot 8^{\frac{1}{8}} \cdot 16^{\frac{1}{16}} \cdots \infty=4$
7. Show that $\sqrt{4} \cdot \sqrt[4]{16} \cdot \sqrt[8]{64} \cdot \sqrt[16]{256} \cdots \infty=16$

8. Sum to $n$ terms the series $2+4 x+6 x^{2}+8 x^{3}+\cdots$ where $x \neq 1$
9. Find the sum to $n$ terms of the series: $\frac{2 n+1}{2 n-1}+3\left(\frac{2 n+1}{2 n-1}\right)^{2}+5\left(\frac{2 n+1}{2 n-1}\right)^{3}+\cdots$
10. Prove that $1+2\left(1+\frac{1}{n}\right)+3\left(1+\frac{1}{n}\right)^{2}+\cdots$ to $n$ terms $=n^{2}$
11. Sum the series to $n$ terms $2+5 x+8 x^{2}+11 x^{3}+\cdots$ and deduce the sum to infinity if $|x|<1$.

# 6.9 Harmonic Progression (H.P.)

A sequence of numbers is called a Harmonic Sequence or Harmonic Progression if the reciprocals of its terms are in arithmetic progression. The sequence $1, \frac{1}{3}, \frac{1}{5}, \frac{1}{7}$ is a harmonic sequence since their reciprocals $1,3,5,7$ are in A.P.
Remember that the reciprocal of zero is not defined, so zero cannot be the term of a harmonic sequence.

The general form of the harmonic sequence is $\frac{1}{a_{1}}, \frac{1}{a_{1}+d}, \frac{1}{a_{1}+2 d}, \cdots, \frac{1}{a_{1}+(n-1) d}$.
Example 22 Find the $n^{\text {th }}$ and $8^{\text {th }}$ terms of H.P. : $\frac{1}{2}, \frac{1}{5}, \frac{1}{8}, \cdots$
Solution The reciprocals of the terms of the sequence,

$$
\frac{1}{2}, \frac{1}{5}, \frac{1}{8}, \cdots \quad \text { are } 2,5,8, \cdots
$$

The numbers $2,5,8, \cdots$ are in A.P., so

$$
a_{1}=2 \text { and } d=5-2=3
$$

Putting these values in $a_{n}=a_{1}+(n-1) d$, we have

$$
\begin{aligned}
a_{n} & =2+(n-1) 3 \\
& =3 n-1
\end{aligned}
$$

Thus, the $n^{\text {th }}$ term of the given sequence $=\frac{1}{a_{n}}=\frac{1}{3 n-1}$ and substituting $n=8$ in $\frac{1}{3 n-1}$,

we get the $8^{\text {th }}$ term of the given H.P. which is $\frac{1}{3 \times 8-1}=\frac{1}{23}$.
Alternatively, $a_{8}$ of the A.P. $=a_{1}+(8-\mathrm{I}) d$

$$
\begin{aligned}
& =2+7(3) \\
& =23
\end{aligned}
$$

Thus, the $8^{\text {th }}$ term of the given H.P. $=\frac{1}{23}$
Example 23 If the $4^{\text {th }}$ and $7^{\text {th }}$ terms of the H.P. are $\frac{2}{13}$ and $\frac{2}{25}$ respectively, find the sequence.
Solution Since the $4^{\text {th }}$ term of the H.P. $=\frac{2}{13}$ and its $7^{\text {th }}$ term $=\frac{2}{25}$, therefore the $4^{\text {th }}$ and $7^{\text {th }}$ terms of the corresponding A.P. are $\frac{13}{2}$ and $\frac{25}{2}$ respectively.
Now taking $a_{1}$, the first term and $d$, the common difference of the corresponding A.P., we have,

$$
a_{1}+3 d=\frac{13}{2}
$$

and $\quad a_{1}+6 d=\frac{25}{2}$
Subtracting (i) from (ii), gives

$$
3 d=\frac{25}{2}-\frac{13}{2}=6 \Rightarrow d=2
$$

From (i), we get

$$
\begin{aligned}
a_{1} & =\frac{13}{2}-3 d \\
& =\frac{13}{2}-6 \\
& =\frac{1}{2}
\end{aligned}
$$

Thus, $\quad a_{2}$ of the A.P. $=a_{1}+d=\frac{1}{2}+2=\frac{5}{2}$
and $\quad a_{3}$ of the A.P. $=a_{1}+2 d=\frac{1}{2}+2(2)$

$$
\begin{aligned}
& =\frac{1}{2}+4 \\
& =\frac{9}{2}
\end{aligned}
$$

Hence the required H.P. is $\frac{2}{1}, \frac{2}{5}, \frac{2}{9}, \frac{2}{13}, \ldots$

# 6.9.1 Harmonic Mean (H.M.)

A number $H$ is said to be the harmonic mean (H.M.) between two numbers $a$ and $b$ if $a, H, b$ are in H.P.

Let $a, b$ be the two numbers and $H$ be their H.M. Then $\frac{1}{a}, \frac{1}{H}, \frac{1}{b}$ are in A.P.
Therefore, $\quad \frac{1}{H}=\frac{\frac{1}{a}+\frac{1}{b}}{2}=\frac{b+a}{a b}=\frac{a+b}{2 a b}$.
and $\quad H=\frac{2 a b}{a+b}$
For example, H.M. between 3 and 7 is

$$
\frac{2 \times 3 \times 7}{3+7}=\frac{2 \times 21}{10}=\frac{21}{5}
$$

### 6.9.2 n Harmonic Means between two Numbers

$H_{1}, H_{2}, H_{3}, \cdots, H_{n}$ are called $n$ harmonic means (H.Ms.) between $a$ and $b$ if $a, H_{1}, H_{2}, H_{3}, \cdots, H_{n}, b$ are in H.P. If we want to insert $n$ H.Ms., between $a$ and $b$, we first find $n$ A.Ms. $A_{1}, A_{2}, \ldots, A_{n}$ between $\frac{1}{a}$ and $\frac{1}{b}$, then take their reciprocals to get $n$ H.Ms. between $a$ and $b$, that is, $\frac{1}{A_{1}}, \frac{1}{A_{2}}, \cdots, \frac{1}{A_{n}}$ will be the required $n$ H.Ms. between $a$ and $b$.
Example 24 Find three harmonic means between $\frac{1}{5}$ and $\frac{1}{17}$.
Solution Let $A_{1}, A_{2}, A_{3}$ be three A.Ms. between 5 and 17, that is,

$$
5, A_{1}, A_{2}, A_{3}, 17 \text { are in A.P. }
$$

Using $\quad a_{n}=a_{1}+(n-1) d$, we get

$$
\begin{aligned}
& 17=5+(5-1) d \quad\left(\because a_{5}=17 \text { and } a_{1}=5\right) \\
& 4 d=12 \\
& \Rightarrow \quad d=3
\end{aligned}
$$

Thus, $\quad A_{1}=5+3=8, A_{2}=5+2(3)=11$ and $A_{3}=5+3(3)=14$
Hence $\frac{1}{8}, \frac{1}{11}, \frac{1}{14}$ are the required harmonic means.

# EXERCISE 6.9

1. Find the $9^{\text {th }}$ term of the following harmonic sequences:
(i) $\frac{1}{3}, \frac{1}{5}, \frac{1}{7}, \ldots$
(ii) $\frac{-1}{5}, \frac{-1}{3},-1, \ldots$
2. Insert five harmonic means between the following given numbers:
(i) $\frac{-2}{5}$ and $\frac{2}{13}$
(ii) $\frac{1}{4}$ and $\frac{1}{24}$
3. The first term of an H.P. is $-\frac{1}{3}$ and the fifth term is $\frac{1}{5}$. Find its $9^{\text {th }}$ term.
4. If 5 is the harmonic mean between 2 and $b$, find $b$.
5. If the numbers $\frac{1}{k}, \frac{1}{2 k+1}$ and $\frac{1}{4 k-1}$ are in harmonic sequence, find $k$.
6. Find $n$ so that $a^{n+1}+b^{n+1}$ may be H.M. between $a$ and $b$.
7. If $a^{2}, b^{2}$ and $c^{2}$ are in A.P., show that $a+b, c+a$ and $b+c$ are in H.P.
8. If the H.M. and A.M. between two numbers are 4 and $\frac{9}{2}$ respectively, find the numbers.
9. If the (positive) G.M. and H.M. between two numbers are 4 and $\frac{16}{5}$, find the numbers.
10. If $\frac{b+c-a}{a} \frac{c+a-b}{b}, \frac{a+b-c}{c}$ are in A.P., show that $a, b, c$ are in H.P.

11. If $a, b, c, d$ are in H.P., show that $3(a-b)(c-d)=(b-c)(a-d)$.
12. If between any two numbers there are inserted two A.Ms. $A_{1}, A_{2}$, two G.Ms. $G_{1}$, $G_{2}$ and two H.Ms. $H_{1}, H_{2}$; show that $\frac{A_{1}+A_{2}}{G_{1} G_{2}}=\frac{H_{1}+H_{2}}{H_{1} H_{2}}$.
13. The H.M. of two numbers is 4 . The A.M., $A$ and the G.M., $G$ satisfy the relation $2 A+G^{2}=27$. Find the numbers.
14. First three of the four numbers $a, b, c, d$ are in A.P., and the next three are in H.P., show that $a d=b c$.
15. If $a, b, c$ are in G.P., show that $\log _{a} x, \log _{b} x, \log _{c} x$ are in H.P.
16. If $a, b, c$ are in H.P., show that
(i) $\frac{a-b}{b-c}=\frac{a}{c}$
(ii) $(a-c)^{2}=(a+c)\left(a-2 b+c\right)$.
17. If $2+x, 5+x$ and $9+x$ are in H.P., find the value of $x$.
18. If the roots of the equation $a(b-c) x^{2}+b(c-a) x+c(a-b)=0$ are equal, prove that $a, b, c$ are in H.P.

# 6.10 Miscellaneous Series

The Greek letter $\Sigma$ (sigma) is used to denote sums of different types. For example, the notation $\sum_{i=m}^{n} a_{i}$ is used to express the $\operatorname{sum} a_{m}+a_{m+1}+a_{m+2}+\cdots+a_{n}$ and the sum expression $1+3+5+\cdots$ to $n$ terms is written as $\sum_{k=1}^{n}(2 k-1)$, where $2 k-1$ is the $k^{\text {th }}$ term of the sum and $k$ is called the index of summation. 1 and $n$ are called the lower limit and upper limit of summation respectively.
The sum of the first $n$ natural numbers, the sum of squares of the first $n$ natural numbers and the sum of the cubes of the first $n$ natural numbers are expressed in sigma notation as:

$$
1+2+3+\cdots+n=\sum_{k=1}^{n} k ; 1^{2}+2^{2}+3^{2}+\cdots+n^{2}=\sum_{k=1}^{n} k^{2} ; 1^{3}+2^{3}+3^{3}+\cdots+n^{3}=\sum_{k=1}^{n} k^{3}
$$

We evaluate $\sum_{k=1}^{n}\left[k^{m}-(k-1)^{m}\right]$ for any positive integer $m$ and we shall use this result to find out formulae for three expressions stated above.

$$
\begin{aligned}
\sum_{k=1}^{n}\left[k^{m}-(k-1)^{m}\right]=\left(1^{m}-0^{m}\right)+\left(2^{m}-1^{m}\right)+\left(3^{m}-2^{m}\right)+ & \cdots \\
& +\left[(n-1)^{m}-(n-2)^{m}\right]+\left[n^{m}-(n-1)^{m}\right]=n^{m}
\end{aligned}
$$

i.e., $\quad \sum_{k=1}^{n}\left[\left(k^{m}-(k-1)^{m}\right]=n^{m}\right.$
If $m=1$, then $\sum_{k=1}^{n}\left[\left(k^{1}-(k-1)^{1}\right]=n^{1}\right.$ i.e., $\sum_{k=1}^{n} 1=n$
If $m=2$, then $\sum_{k=1}^{n}\left[k^{2}-(k-1)^{2}\right]=n^{2}$

## Properties of Summation:

(i) $\sum_{s=1}^{n}\left(a_{s}+b_{s}\right)=\sum_{s=1}^{n} a_{s}+\sum_{s=1}^{n} b_{s}$
(ii) $\sum_{s=1}^{n} \alpha a_{s}=\alpha \sum_{s=1}^{n} a_{s}$

To Find the Formulae for the Sums
(i) $\sum_{k=1}^{n} k$
(ii) $\sum_{k=1}^{n} k^{2}$
(iii) $\sum_{k=1}^{n} k^{3}$
(i) We know that $(k-1)^{2}=k^{2}-2 k+1$ and this identity can be written as:

$$
k^{2}-(k-1)^{2}=2 k-1
$$

Taking summation on both sides of (A) from $k=1$ to $n$, we have

$$
\begin{aligned}
& \sum_{k=1}^{n}\left[\left(k^{2}-(k-1)^{2}\right]=\sum_{k=1}^{n}(2 k-1)\right. \\
& \text { i.e., } \\
& n^{2}=2 \sum_{k=1}^{n} k-n \\
& \text { or } \\
& 2 \sum_{k=1}^{n} k=n^{2}+n \\
& \text { Thus }
\end{aligned}
$$

$$
\sum_{k=1}^{n} k=\frac{n(n+1)}{2}
$$

Similarly, we can prove easily
(ii) $\sum_{k=1}^{n} k^{2}=\frac{n(n+1)(2 n+1)}{6}$
(iii) $\sum_{k=1}^{n} k^{3}=\left[\frac{n(n+1)}{2}\right]^{2}$

Example 25 Find the sum of the series $1^{3}+3^{3}+5^{3}+\ldots$ to $n$ terms.
Solution $T_{k}=(2 k-1)^{2} \quad(\because 1+2(k-1)=2 k-1)$

$$
=8 k^{3}-12 k^{2}+6 k-1
$$

Let $S_{n}$ denote the sum of $n$ terms of the given series, then

$$
S_{n}=\sum_{k=1}^{n} T_{k}
$$

or

$$
S_{n}=\sum_{k=1}^{n}\left(8 k^{3}-12 k^{2}+6 k-1\right)
$$

$$
\begin{aligned}
& =8 \sum_{k=1}^{n} k^{3}-12 \sum_{k=1}^{n} k^{2}+6 \sum_{k=1}^{n} k-\sum_{k=1}^{n} 1 \\
& =8\left[\frac{n(n+1)}{2}\right]^{2}-12\left[\frac{n(n+1)(2 n+1)}{6}\right]+6\left[\frac{n(n+1)}{2}\right]-n \\
& =2 n^{2}(n+1)^{2}-2 n(n+1)(2 n+1)+3 n(n+1)-n \\
& =2 n^{2}\left(n^{2}+2 n+1\right)-2 n\left(2 n^{2}+3 n+1\right)+n(3 n+3)-n \\
& =2 n\left[\left(n^{3}+2 n^{2}+n\right)-\left(2 n^{2}+3 n+1\right)\right]+n(3 n+3-1) \\
& =2 n\left(n^{3}-2 n-1\right)+n(3 n+2) \\
& =2 n\left(n^{3}-2 n-1\right)+n(3 n+2) \\
& =n\left[2 n^{3}-4 n-2+3 n+2\right] \\
& =n\left[2 n^{3}-n\right]=n\left[n\left(2 n^{2}-1\right)\right] \\
& =n^{2}\left[2 n^{2}-1\right]
\end{aligned}
$$

Example 26 Find the sum of $n$ terms of series whose $n^{\text {th }}$ terms is $n^{3}+\frac{3}{2} n^{2}+\frac{1}{2} n+1$.
Solution Given that

$$
T_{n}=n^{3}+\frac{3}{2} n^{2}+\frac{1}{2} n+1
$$

Thus

$$
T_{k}=k^{3}+\frac{3}{2} k^{2}+\frac{1}{2} k+1
$$

and

$$
5_{n}=\sum_{k=1}^{n}\left(k^{3}+\frac{3}{2} k^{2}+\frac{1}{2} k+1\right)
$$

$$
\begin{aligned}
& =\sum_{k=1}^{n} k^{3}+\frac{3}{2} \sum_{k=1}^{n} k^{2}+\frac{1}{2} \sum_{k=1}^{n} k+\sum_{k=1}^{n} 1 \\
& =\frac{n^{2}(n+1)^{2}}{4}+\frac{3}{2} \times \frac{n(n+1)(2 n+1)}{6}+\frac{1}{2} \times\left[\frac{n(n+1)}{2}\right]+n \\
& =\frac{n}{4}\left[n\left(n^{2}+2 n+1\right)+\left(2 n^{2}+3 n+1\right)+(n+1)+4\right] \\
& =\frac{n}{4}\left(n^{3}+2 n^{2}+n+2 n^{2}+3 n+1+n+1+4\right) \\
& =\frac{n}{4}\left(n^{3}+4 n^{2}+5 n+6\right)
\end{aligned}
$$

# EXERCISE 6.10

1. Sum the following series upto $n$ terms.
(i) $1 \times 3+2 \times 5+3 \times 7+\cdots$
(ii) $1 \times 5+2 \times 8+3 \times 11+\cdots$
(iii) $1 \times 2+2 \times 5+3 \times 8+\cdots$
(iv) $1 \times 3 \times 5+2 \times 4 \times 6+3 \times 5 \times 7+\cdots$
(v) $1 \times 2 \times 4+2 \times 3 \times 7+3 \times 4 \times 10+\cdots$
(vi) $2^{2}+4^{2}+6^{2}+\cdots$
(vii) $3^{2}+6^{2}+9^{2}+\cdots$
(viii) $4 \times 1^{2}+7 \times 2^{2}+10 \times 3^{2}+\cdots$
(ix) $3+(3+7)+(3+7+11)+\cdots$
(x) $1^{2}+\left(1^{2}+2^{2}\right)+\left(1^{2}+2^{2}+3^{2}\right)+\cdots$
2. Sum the series.
(i) $1^{2}-2^{2}+3^{2}-4^{2}+\ldots+(2 n-1)^{2}-(2 n)^{2}$
(ii) $\frac{1^{2}}{1}+\frac{1^{2}+2^{2}}{2}+\frac{1^{2}+2^{2}+3^{2}}{3}+\ldots$ to $n$ terms :
3. Find the sum to $n$ terms of the series whose $n^{\text {th }}$ terms are given.
(i) $5 n^{2}+2 n+3$
(ii) $n^{2}+2 n-3$
4. Given $n^{\text {th }}$ terms of the series, find the sum to $2 n$ terms:
(i) $3 n^{2}+5 n+2$
(ii) $n^{2}+n-2$

### 6.11 Real Life Problems involving Sequences and Series

## Example 27 Vehicle Arrival Sequence

Vehicles arrive at a toll booth at a rate of 4 cars every 5 minutes. Represent the number of cars arriving over time as a sequence and predict the total number of cars after an hour.
Solution The sequence of car arrivals is:

$$
4,8,12,16, \ldots
$$

This is an $A: P$, with
$a_{1}=4, d=4, n=\frac{60}{5}=12, a_{12}=?$
Using the formula for arithmetic sequence

$$
\begin{aligned}
a_{n} & =a_{1}+(n-1) d \\
a_{12} & =4+(12-1)(4) \\
& =4+11(4) \\
& =4+44=48
\end{aligned}
$$

Thus, after one hour there will be 48 cars.

Simple Interest on Loan (Arithmetic Sequence with Particular Term)
Example 28 To buy furniture for a new apartment Tayyab borrowed Rs. 50,000 at $8 \%$ simple interest for 11 years. How much interest will he pay?
Solution Since $8 \%$ is the yearly interest rate, we have

$$
\begin{aligned}
& \text { Interest after one year }=\text { Rs. } 50,000 \times \frac{8}{100} \times 1=\text { Rs. } 4000 \\
& \text { Interest after two years }=\text { Rs. } 50,000 \times \frac{8}{100} \times 2=\text { Rs. } 8000
\end{aligned}
$$

Therefore, we have the A.P.

$$
4000,8000,12000, \ldots
$$

Here, $a_{1}=4000, a_{2}=8000, d=a_{2}-a_{1}=4000, n=11$
Using the formula

$$
\begin{aligned}
a_{n} & =a_{1}+(n-1) d \\
a_{11} & =4000+(11-1)(4000) \\
& =4000+10(4000) \\
& =4000+40000 \\
& =\text { Rs. } 44000
\end{aligned}
$$

Thus, Tayyab will pay a total interest of Rs. 44000 on borrowed amount of Rs 50,000 after 11 years.
Compound Interest on Loan (Geometric Sequence with Particular Term)
Example 29 Amna invests Rs. 200000 at $5 \%$ interest compounded annually. What total amount will she get after 10 years?
Solution Let the principal amount be $P$. Then,
The interest for the first year $=P \times \frac{5}{100}=P(0.05)$
The total amount after first year $=P+P(0.05)=P(1+0.05)$
The interest for the second year $=P(1+0.05) \times 0.05$
The total amount after second year $=P(1+0.05)+P(1+0.05) \times 0.05$

$$
\begin{aligned}
& =P(1+0.05)(1+0.05) \\
& =P(1+0.05)^{2}
\end{aligned}
$$

Similarly, the total amount after third year $=P(1+0.05)^{3}$
Thus, we have sequence of amounts

$$
P(1.05), P(1.05)^{2}, P(1.05)^{3}, \ldots
$$

which is clearly a G.P., with

$$
a_{1}=P(1.05), r=1.05, n=10, a_{10}=?
$$

Using the geometric sequence formula

$$
\begin{aligned}
a_{n} & =a_{1} r^{n-1} \\
a_{10} & =a_{1} r^{10-1} \\
& =P(1.05) \times(1.05)^{9} \\
& =(200000)(1.05)^{10} \quad P=200000 \\
& =(200000)(1.62889) \\
& =325778.92
\end{aligned}
$$

Thus, the total amount Amna will get after 10 years will be Rs. 325778.92
Grid Column Distribution (Arithmetic Series Sum of Terms)
Example 30 A web designer is using a 12 -column grid system where each column increases in width by 10px from the previous one. The first column width is 50px wide. Find the total width occupied by all 12 columns.
Solution This follows an arithmetic series with:
First term $=a_{1}=50$, Common difference $=d=10$
Number of terms $=n=12$
Using the formula for the sum of an arithmetic series:

$$
\begin{aligned}
S_{n} & =\frac{n}{2}\left[2 a_{1}+(n-1) d\right] \\
S_{12} & =\frac{12}{2}[2(50)+(12-1)(10)] \\
& =6[100+110]=6[210] \\
& =1260 p x
\end{aligned}
$$

Thus, the total width of all 12 columns is 1260 px .
Example 31 Motor Vehicle Leasing Using Arithmetic Sequence
A company leases a motor vehicle with the following terms:

- The first monthly payment is Rs. 15,000
- Each subsequent payment increases by Rs. 500 due to inflation adjustments.
- The lease term is 24 months.

Find:
(i) What is the payment in the $24^{\text {th }}$ month?
(ii) What is the total amount paid over 24 months?
(iii) If the company can only afford to pay a total of Rs. 400,000 , can they complete the 24 -months lease?
(iv) Find maximum months $n$ such that total, payment $S_{n} \leq 400,000$.

# Solution Given:

$$
\begin{aligned}
\text { First term }=a_{1} & =15000 \\
\text { Common difference } & =d=500 \\
\text { Number of terms } & =n=24
\end{aligned}
$$

(i) Payment in $24^{\text {th }}$ month:

Using the formula

$$
\begin{aligned}
a_{n} & =a_{1}+(n-1) d \\
a_{24} & =15000+(24-1)(500) \\
& =15000+23 \times 500 \\
& =15000+11500=\text { Rs. } 26500
\end{aligned}
$$

(ii) Total payment over 24 months using the formula

$$
\begin{aligned}
S_{n} & =\frac{n}{2}\left(a_{1}+a_{n}\right) \\
& =\frac{24}{2}(15000+26500)=12(41500)=\text { Rs. } 498000
\end{aligned}
$$

(iii) Can the company afford the lease? No, total payments (Rs. 498000) exceed the budget of Rs. 400,000 by Rs. 98,000 .
(iv) Using: $S_{n}=\frac{n}{2}\left[2 a_{1}+(n-1) d\right] \leq 400,000$

Substituting the values:

$$
\begin{gathered}
\frac{n}{2}[2(15000)+(n-1)(500)] \leq 400,000 \\
n[15000+250 n-250] \leq 400,000 \\
n(250 n+14750) \leq 400,000 \\
250 n^{2}+14750 n-400000 \leq 0 \\
n^{2}+59 n-1600 \leq 0
\end{gathered}
$$

Associated equation is $n^{2}+59 n-1600=0$

$$
\begin{aligned}
& n=\frac{-59 \pm \sqrt{(59)^{2}-4(1)(-1600)}}{2(1)} \\
& n=\frac{-59 \pm 99.4}{2} \\
& n=\frac{-59-99.4}{2}, n=\frac{-59+99.4}{2} \\
& n=-79.2, n=20.2
\end{aligned}
$$

Clearly $n=20$ satisfy the inequality.
So, $n=20$ is the maximum months such that payment $S_{n} \leq 400,000$.

# EXERCISE 6.11

1. A sum of Rs. 10400 is paid off in 40 instalment such that each instalment is Rs. 10 more than the preceding instalment. Calculate the value of the first instalment.
2. An investor invests Rs. 150000 at an annual compound interest rate of $6 \%$ for 8 years. Find the total amount will he get after 8 years.
3. The population of a town is 4084101 at present and five years ago it was 3200000 . Find its rate of increase if it increased geometrically.
4. Determine the total worth of a yearly Rs. 5000 investment after 20 years if the interest rate is $5 \%$ compounded annually.
5. A water tank has a leakage. Each week, the tank loses 5 gallons of water due to the leakage. Initially, the tank is full and contains 2000 gallons.
(i) How many gallons are in the tank 20 weeks later?
(ii) How many weeks until the tank is half-full?
(iii) How many weeks until the tank is empty?
6. A drug company has manufactured 7 million doses of a vaccine to date. They promise additional production at a rate of 1.4 million doses/month over the next year.
(i) How many doses of the vaccine, in total, will have been produced after a year?
(ii) The general term $a_{n}$ describes the total number of doses of the vaccine produced. Describe the meaning of the variable $n$ in the context of this problem. Find the general term $a_{n}$
(iii) Find the value of $a_{10}$ and interpret its meaning in words.
7. At a toll-bent, the number of vehicles passing through during the first minute is 100 . Due to road congestion, each minute only $80 \%$ of the vehicles from the previous minute manage to pass.
(i) Represent the number of vehicles passing each minute as a sequence.
(ii) Find the total number of vehicles that pass through in 15 minutes.
(iii) What is the maximum number of vehicles that can pass in the long run (as time $t \rightarrow \infty$ )
8. A sum of Rs. 5000 is inverted at $8 \%$ simple interest per year. Calculate the interest at the end of each year. Do these interests form an A.P.? If so find the interest at the end of 20 years making use of this fact.

9. A machine is purchased for Rs.20,000. Depreciates at 6% per annum for the first four years and after that 8% per annum for the next six years. Depreciation being calculated on diminishing value. Find the value of the machine after a period of 10 years.
10. Two cars start together in the same direction from the same place. The first goes with uniform speed of 20km/h. The second goes at a speed of 12km/h in the first hour and increases the speed by 1 km/h each succeeding hour. After how many hours will the second car overtake the first car if both cars go non-stop?
11. 150 workers were engaged to finish a piece of work in a certain number of days. Five workers dropped the second day, five more workers dropped the third day and so on. It takes 10 more days to finish the work now. Find the number of days in which the work was completed.
12. A radioactive product has a half life of 5 years. If the radioactivity level is 68 microcuries after 20 years. Determine the original level of radioactivity.
13. An object moving in a line is given an initial velocity of 4.5 m/s and a constant acceleration of 2.5 m/s². How long will it take the object to reach a velocity of 20m/s?
14. In an integrated circuit with an initial current of 1080 mA, the temperature in the components decreases from 20% to 17% to 14%. Assuming that each temperature decrease is caused by a decrease in the initial current, what is the value of the current at fourth measurement?
15. Show that the amount of a certain sum of money at compound interest of r% per year for n years form a G.P.