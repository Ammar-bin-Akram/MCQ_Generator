# Chapter 5: <br> Mathematical Inductions and Binomial Theorem

## INTRODUCTION

Francesco Mourolico (1494-1575) devised the method of induction and applied this device first to prove that the sum of the first $n$ odd positive integers equals $n^{2}$. He presented many properties of integers and proved some of these properties using the method of mathematical induction. In theoretical computer science, it bears the pivotal role of developing the appropriate cognitive skills necessary for the effective design and implementation of algorithms, assessing for both their correctness and complexity. We are aware of the fact that even one exception or case to a mathematical formula is enough to prove it to be false. Such a case or exception which fails the mathematical formula or statement is called a counter example.
The validity of a formula or statement depending on a variable belonging to a certain set is established if it is true for each element of the set under consideration.
For example, we consider the statement $S(n)=n^{2}-n+41$ is a prime number for every natural number $n$. The values of the expression $n^{2}-n+41$ for some first natural numbers are given in the table as shown below:

| $n$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| $S(n)$ | 41 | 43 | 47 | 53 | 61 | 71 | 83 | 97 | 113 | 131 | 151 |

From the table, it appears that the statement $S(n)$ has enough chance of being true. If we go on trying for the next natural numbers, we find $n=41$ as a counter example which fails the claim of the above statement. So we conclude that to derive a general formula without proof from some special cases is not a wise step. This example was discovered by Euler (1707-1783).
Now we consider another example and try to formulate the result. Our task is to find the sum of the first $n$ odd natural numbers. We write first few sums to see the pattern of sums.

| Unit 4 Mathematical Inductions and Binomial Theorem | $<141$ | Mathematics (1) |
| :--: | :--: | :--: |
| $n$ (The number of terms) | Sum |  |
| 1 | $1=1^{2}$ |  |
| 2 | $1+3=4=2^{2}$ |  |
| 3 | $1+3+5=9=3^{2}$ |  |
| 4 | $1+3+5+7=16=4^{2}$ |  |
| 5 | $1+3+5+7+9=25=5^{2}$ |  |
| 6 | $1+3+5+7+9+11=36=6^{2}$ |  |

The sequence of sums is $(1)^{2},(2)^{2},(3)^{2},(4)^{2}, \ldots$
We see that each sum is the square of the number of terms in the sum. So the following statement seems to be true.
For each natural number $n$,

$$
1+3+5+\cdots+(2 n-1)=n^{2} \ldots \text { (i) } \quad \because \quad n^{\text {th }} \text { term }=1+2(n-1)
$$

But it is not possible to verify the statement (i) for each positive integer $n$, because it involves infinitely many calculations which never end.
The method of mathematical induction is used to avoid such situations. Usually it is used to prove the statements or formulae relating to the set $\{1,2,3, \ldots\}$ but in some cases, it is also used to prove the statements relating to the set $\{0,1,2,3, \ldots\}$.
Hypothesis: A hypothesis is an educated guess or proposed explanation for a statement based on limited evidence. It serves as a starting point for further investigation and can be tested through experiments and observations. In scientific research, a hypothesis is usually framed as a statement that can be tested and either supported or rejected by data.
Induction of Hypothesis: It refers to the process of formulating a general statement or hypothesis based on specific examples or patterns observed in particular cases. This technique is often employed in mathematical reasoning to propose conjectures that can later be proven rigorously using deductive methods.

# 8.1 Principle of Mathematical Induction

The principle of mathematical induction is stated as follows:
If a proposition or statement $S(n)$ for each positive integer $n$ is such that

1. Base Case: $S(1)$ is true i.e., $S(n)$ is true for $n=1$.
2. Induction of Hypothesis: $S(k+1)$ is true whenever $S(k)$ is true for any positive integer $k$.
3. Conclusion: $S(n)$ is true for all positive integers.

Procedure for Induction of Hypothesis

- Substituting $n=1$, show that the statement is true for $n=1$.
- Assuming that the statement is true for any positive integer $k$, then show that it is true for the next higher integer.
For the second condition, one of the following two methods can be used:
$S(k+1)$ is proved using $S(k)$.
$S(k+1)$ is established by performing algebraic operations on $S(k)$.
Example 1 Use mathematical induction to prove that $3+6+9+\ldots+3 n=\frac{3 n(n+1)}{2}$ for every positive integer $n$.
Solution Let $S(n)$ be the given statement, that is,

$$
S(n): 3+6+9+\ldots+3 n=\frac{3 n(n+1)}{2}
$$

Base Case: When $n=1, S(1): 3=\frac{3(1)(1+1)}{2}=3$. Thus $S(1)$ is true i.e., The base case is satisfied.
Induction of Hypothesis: Let us assume that $S(n)$ is true for any $n=k \in N$, that is,

$$
S(k): 3+6+9+\ldots+3 k \approx \frac{3 k(k+1)}{2}
$$

The statement for $n=k+1$ becomes

$$
\begin{aligned}
3+6+9+\ldots+3 k+3(k+1) & =\frac{3(k+1)[(k+1)+1]}{2} \\
& =\frac{3(k+1)(k+2)}{2}
\end{aligned}
$$

Adding $3(k+1)$ on both the sides of (A) gives

$$
\begin{aligned}
3+6+9+\ldots+3 k+3(k+1) & =\frac{3 k(k+1)}{2}+3(k+1) \\
& =3(k+1)\left(\frac{k}{2}+1\right) \\
& =\frac{3(k+1)(k+2)}{2}
\end{aligned}
$$

Thus $S(k+1)$ is true if $S(k)$ is true.
Conclusion: Since both the conditions are satisfied, therefore, $S(n)$ is true for each positive integer $n$.

Example 2 Use mathematical induction to prove that for any positive integer $n$,

$$
1^{2}+2^{2}+3^{2}+\ldots+n^{2}=\frac{n(n+1)(2 n+1)}{6}
$$

Solution Let $S(n)$ be the given statement,

$$
S(n): 1^{2}+2^{2}+3^{2}+\ldots+n^{2}=\frac{n(n+1)(2 n+1)}{6}
$$

Base Case: If $n=1, S(1):(1)^{2}=\frac{1(1+1)(2 \times 1+1)}{6}=\frac{1 \times 2 \times 3}{6}=1$, which is true. Thus $S(1)$ is true, i.e., The base case is satisfied.
Induction of Hypothesis: Let us assume that $S(k)$ is true for any $k \in N$, that is,

$$
\begin{aligned}
S(k): 1^{2}+2^{2}+3^{2}+\ldots+k^{2} & =\frac{k(k+1)(2 k+1)}{6} \\
S(k+1): 1^{2}+2^{2}+3^{2}+\ldots+k^{2}+(k+1)^{2} & =\frac{(k+1)(k+1+1)(2 k+1+1)}{6} \\
& =\frac{(k+1)(k+2)(2 k+3)}{6}
\end{aligned}
$$

Adding $(k+1)^{2}$ to both the sides of equation (4), we have

$$
\begin{aligned}
1^{2}+2^{2}+3^{2}+\ldots+k^{2}+(k+1)^{2} & =\frac{k(k+1)(2 k+1)}{6}+(k+1)^{2} \\
& =\frac{(k+1)[k(2 k+1)+6(k+1)]}{6} \\
& =\frac{(k+1)\left(2 k^{2}+k+6 k+6\right)}{6} \\
& =\frac{(k+1)\left(2 k^{2}+7 k+6\right)}{6} \\
& =\frac{(k+1)(k+2)(2 k+3)}{6}
\end{aligned}
$$

Thus, formula holds for $k+1$.
Conclusion: Since both the conditions are satisfied, therefore, by mathematical induction, the given statement holds for all positive integers.
Example 3 Show that $\frac{n^{2}+2 n}{3}$ represents an integer $\forall n \in N$.
Solution Let $S(n)=\frac{n^{2}+2 n}{3} \in Z \forall n \in N$
Base Case: When $n=1, S(1)=\frac{1^{2}+2(1)}{3}=\frac{3}{3}=1 \in Z$. The base case is satisfied.

Induction of Hypothesis: Let us assume that $S(n)$ is true for any $n=k \in N$, that is,

$$
S(k)=\frac{k^{2}+2 k}{3} \text { represents an integer. }
$$

Now we want to show that $S(k+1)$ is also an integer. For $n=k+1$, the statement becomes

$$
\begin{aligned}
S(k+1) & =\frac{(k+1)^{3}+2(k+1)}{3} \\
& =\frac{k^{3}+3 k^{2}+3 k+1+2 k+2}{3}=\frac{\left(k^{3}+2 k\right)+\left(3 k^{3}+3 k+3\right)}{3} \\
& =\frac{\left(k^{3}+2 k\right)+3\left(k^{2}+k+1\right)}{3}=\frac{k^{3}+2 k}{3}+\left(k^{2}+k+1\right)
\end{aligned}
$$

As $\frac{k^{3}+2 k}{3}$ is an integer by assumption and we know that $\left(k^{2}+k+1\right)$ is an integer as $k \in N . S(k+1)$ being sum of integers is an integer. Thus statements holds for $k+1$.
Conclusion: Since both the conditions are satisfied, therefore, we conclude by mathematical induction that $\frac{n^{2}+2 n}{3}$ represents an integer for all positive integral values of $n$.
Example 4 Use mathematical induction to prove that

$$
3+3 \cdot 5+3 \cdot 5^{2}+\cdots+3 \cdot 5^{n}=\frac{3\left(5^{n+1}-1\right)}{4} \text {, whenever } n \text { is non-negative integer. }
$$

Solution Let $S(n)$ be the given statement, that is,

$$
S(n): 3+3 \cdot 5+3 \cdot 5^{2}+\cdots+3 \cdot 5^{n}=\frac{3\left(5^{n+1}-1\right)}{4}
$$

The dot (.) between two numbers stands for multiplication symbol.

Base Case: For $n=0, S(0): 3 \cdot 5^{0}=\frac{3\left(5^{0+1}-1\right)}{4}$ or $3=\frac{3(5-1)}{4}=3$
Thus $S(0)$ is true i.e., The base case is satisfied.
Induction of Hypothesis: Let us assume that $S(k)$ is true for any $k \in W$, that is,

$$
S(k): 3+3 \cdot 5+3 \cdot 5^{2}+\cdots+3.5^{k}=\frac{3\left(5^{k+1}-1\right)}{4}
$$

Here $S(k+1)$ becomes

$$
\begin{aligned}
S(k+1): 3+3 \cdot 5+3 \cdot 5^{2}+\cdots+3 \cdot 5^{k}+3 \cdot 5^{k-1} & =\frac{3\left(5^{(k+1)+1}-1\right)}{4} \\
& =\frac{3\left(5^{k+2}-1\right)}{4}
\end{aligned}
$$

Adding $3.5^{k+1}$ on both sides of (A), we get

$$
\begin{aligned}
3+3 \cdot 5+3 \cdot 5^{2}+\cdots+3 \cdot 5^{k}+3 \cdot 5^{k+1} & =\frac{3\left(5^{k+1}-1\right)}{4}+3.5^{k+1} \\
& =\frac{3\left(5^{k+1}-1+4.5^{k+1}\right)}{4} \\
& =\frac{3\left[5^{k+1}(1+4)-1\right]}{4}=\frac{3\left(5^{k+2}-1\right)}{4}
\end{aligned}
$$

This shows that $S(k+1)$ is true when $S(k)$ is true.
Conclusion: Since both the conditions are satisfied, therefore, by the principle of mathematical induction, $S(n)$ in true for each $n \in W$.
Example 5 Prove that $4^{n}+6 n-1$ is divisible by 9 for all $n \in N$
Solution Let $S(n)$ be the given statement,

$$
S(n)=4^{n}+6 n-1 \text { is divisible by } 9 \text { for all } n \in N
$$

Base Case: Put $n=1, S(1)=4^{1}+6(1)-1=4+6-1=9$
Which is divisible by 9 . Hence it is true for $n=1$.
Induction of Hypothesis: Suppose the statement is true for $n=k$. i.e., $S(k)=4^{k}+6 k-1$ is divisible by 9
This implies $S(k)=4^{k}+6 k-1=9 k$, for some integer $k_{1}$

$$
4^{k}+6 k-1=9 k
$$

Now put $n=k+1$,

$$
\begin{aligned}
S(k+1) & =4^{k+1}+6(k+1)-1=4 \cdot 4^{k}+6 k+6-1 \\
& =4\left(9 k_{1}-6 k+1\right)+6 k+6-1 \\
& =36 k_{1}-24 k+4+6 k+5 \\
& =36 k_{1}-18 k+9 \\
& =9\left(4 k_{1}-2 k+1\right)
\end{aligned}
$$

Which is divisible by 9 .
Thus $S(k)$ is true for $n=k+1$.
Conclusion: Since both the conditions are satisfied, therefore, by the principle of mathematical induction, the given statement is true for all integers $n \geq 1$.
Example 6 Use mathematical induction to prove that

$$
\sum_{k=1}^{n} \frac{1}{(2 k-1)(2 k+1)}=\frac{n}{2 n+1}, \text { whenever } n \text { is a positive integer. }
$$

Solution Let $S(n)$ be the given statement, that is,

$$
S(n): \sum_{k=1}^{n} \frac{1}{(2 k-1)(2 k+1)}=\frac{n}{2 n+1}
$$

Base Case: For $n=1, S(1): \sum_{k=1}^{1} \frac{1}{(2 k-1)(2 k+1)}=\frac{1}{2.1+1}$,

$$
\frac{1}{1 \cdot 3}=\frac{1}{2 \cdot 1+1} \Rightarrow \frac{1}{3}=\frac{1}{3}
$$

Thus $S(1)$ is true i.e., The base case is satisfied.
Induction of Hypothesis: Let us assume that $S(n)$ is true for $n=m$, that is,

$$
S(m): \sum_{k=1}^{m} \frac{1}{(2 k-1)(2 k+1)}=\frac{m}{2 m+1}
$$

Here $S(m+1)$ becomes

$$
\begin{aligned}
S(m+1): & \sum_{k=1}^{m+1} \frac{1}{(2 k-1)(2 k+1)}=\frac{m}{2 m+1}+\frac{1}{(2 m+1)(2 m+3)} \\
& =\frac{m(2 m+3)+1}{(2 m+1)(2 m+3)}=\frac{2 m^{2}+3 m+1}{(2 m+1)(2 m+3)}=\frac{(m+1)(2 m+1)}{(2 m+1)(2 m+3)} \\
& =\frac{m+1}{2 m+3}=\frac{m+1}{2 m+2+1}=\frac{m+1}{2(m+1)+1}
\end{aligned}
$$

This shows that $S(k+1)$ is true when $S(k)$ is true.
Conclusion: Since both the conditions are satisfied, therefore, by the principle of mathematical induction, $S(n)$ in true for each $n \in N$.

# 8.1.1 Principle of Extended Mathematical Induction

Let $i$ be an integer. A formula or identity or statement $S(n)$ for $n \geq i$ is such that

1. Base Case: $S(i)$ is true and
2. Induction of Hypothesis: $S(k+1)$ is true whenever $S(k)$ is true for any integer $n \geq i$.
3. Conclusion: $S(n)$ is true for all integers $n \geq i$.

Example 7 Show that $1+3+5+\cdots+(2 n+5)=(n+3)^{2}$ for integral values of $n \geq-2$.

## Base Case: Let $S(n)$ be the given statement, then for $n=-2, S(-2)$ becomes,

$$
2(-2)+5=(-2+3)^{2} \text {, i.e., } 1=(1)^{2} \text { which is true. }
$$

Thus $S(-2)$ is true i.e., The base case is satisfied.
Induction of Hypothesis: Let the equation be true for any $n=k \in Z, k \geq-2$, so that $\mathrm{S}(k): 1+3+5+\cdots+(2 k+5)=(k+3)^{2}$

$S(k+1): 1+3+5+\ldots+(2 k+5)+(2 k+1+5)=(k+1+3)^{2}=(k+4)^{2}$
Adding $(2 k+1+5)=(2 k+7)$ on both sides of equation (A) we get,

$$
\begin{aligned}
1+3+5+\cdots+(2 k+5)+(2 k+7) & =(k+3)^{2}+(2 k+7) \\
& =k^{2}+6 k+9+2 k+7 \\
& =k^{2}+8 k+16=(k+4)^{2}
\end{aligned}
$$

The formula holds for $k+1$.
Conclusion: As both the conditions are satisfied, so we conclude that the $S(n)$ is true for all integers $n \geq-2$.
Example 8 Show that the inequality $4^{n}>3^{n}+4$ is true, for integral values of $n \geq 2$.
Solution Let $S(n)$ represents the given statement i.e., $S(n): 4^{n}>3^{n}+4$ for integral values of $n \geq 2$
Base Case: For $n=2, S(2)$ becomes
$S(2): 4^{3}>3^{3}+4$, i.e., $16>13$ which is true.
Thus $S(2)$ is true, i.e., The base case is satisfied.
Induction of Hypothesis: Let the statement be true for any $n=k(\geq 2) \in Z$, that is

$$
S(k): 4^{k}>3^{k}+4
$$

Multiplying both sides of inequality (A) by 4 , we get

$$
4.4^{k}>4\left(3^{k}+4\right)
$$

or

$$
4^{k+1}>(3+1) 3^{k}+16
$$

or

$$
4^{k+1}>3^{k+1}+4+3^{k}+12
$$

or

$$
4^{k+1}>3^{k+1}+4 \quad\left(\because 3^{k}+12>0\right)
$$

The inequality (B), The formula holds for $k+1$.
Conclusion: Since both the conditions are satisfied, therefore, by the principle of extended mathematical induction, the given inequality is true for all integers $n \geq 2$.
Example 9 If $a_{n}=2^{2^{n}}+1$, then for $n>1$, show that last digit of $a_{n}$ is 7 .
Solution We will prove the statement by mathematical induction.
Base case: For $n=2$
$a_{2}=2^{2^{2}}+1=2^{4}+1=17$. Clearly unit digit is 7 .
Inductive Hypothesis: Assume that $a_{k}=2^{2^{k}}+1=10 m+7$ where $k>1$ and $m$ is some positive integer.

Now, $a_{k+1}=2^{2^{k+1}}+1=2^{2^{k} \cdot 3}+1$

$$
\begin{aligned}
& =\left(2^{2^{k}}\right)^{2}+1=(10 m+6)^{2}+1 \\
& =100 m^{2}+120 m+36+1 \\
& =100 m^{2}+120 m+30+7 \\
& =10\left(10 m^{2}+12 m+3\right)+7
\end{aligned}
$$

Thus, last digit of $a_{n}$ is 7 for all $n>1$.
Conclusion: Since both the conditions are satisfied, therefore, by the principle of mathematical induction, the given statement is true for all integers $n>1$.

# 8.1.2 Real Life Application of Mathematical Induction

Mathematical induction is a powerful method used to prove statements that are formulated for natural numbers. It is often used in mathematics to justify conclusions about sequences, series, and other constructs that involve integer values.
Example10 Faris starts a savings plan where he deposits 1,000 rupees into his bank account every month. Using mathematical induction, prove that the total amount saved after $n$ months is given by:

$$
S(n)=1000 \times n \text { rupees }
$$

where $n$ is a positive integer representing the number of months.
Solution Given statement $S(n)=1000 \times n$
Base Case: For $n=1$ : After the first month, Faris save 1000 rupees. Therefore, the total savings after one month is $1000 \times 1=1000$ rupees. The base case $S(1)$ holds true.
Induction of Hypothesis: Assume the statement is true for some positive integer $k$, i.e., after $k$ months, the total savings is $S(k)=1000 \times k$ rupees.
Now, prove that the statement holds for $k+1$ months: After $k+1$ months, you would save an additional Rs. 1000, so the total savings becomes: $S(k+1)=1000 \times k+1000$ $=1000 \times(k+1)$ rupees. Thus, if the statement holds for $k$, it also holds for $k+1$.
Justification and Communication: Using mathematical induction, we prove that saving Rs. 1000 monthly for $n$ months totals $1000 \times n$ rupees.
The base case $(n=1)$ holds, and assuming it's true for $k$ months, we show it for $k+1$. Thus, the statement is valid for all natural numbers $n$, making it reliable for real-life applications.
Example 11 Ali starts a daily exercise routine where each day he increases the number of push-ups he does by 2 . On the first day, he does 10 push-ups. Prove that after $n^{\text {th }}$ day, the total number of push-ups Ali has done is $n^{2}+9 n$
Solution Base Case: For $n=1$ : On the first day, Ali do 10 push-ups. Total push-ups $(1)^{2}+9(1)=10$. The base case $S(1)$ holds true.

Induction of Hypothesis: Assume the statement is true for some positive integer $k$, i.e., the total number of push-ups after k days is $S(k)=k^{2}+9 k$.

Now, prove it for $k+1$ days: On the $(k+1)$ th day, you do $10+2 \times k$ push-ups. The total after $k+1$ days becomes: $k^{2}+9 k+(10+2 k)=k^{2}+2 k+1+9 k+9$

$$
=(k+1)^{2}+9(k+1)
$$

The formula holds for $S(k+1)$.
Conclusion: By mathematical induction, the total number of push-ups after $n$ days is

$$
n^{2}+9 n
$$

Example 12 Suppose you aim to lose weight by reducing your calories intake by 50 calories each week. If you start at 2500 calories, prove that after $n$ weeks, your daily intake is $2500-50 n$ calories.
Solution Base Case: For $n=1$ : After 1 week, your intake is $2500-50=2450$ calories. The base case $S(1)$ holds true.
Induction of Hypothesis: Assume the statement is true for some positive integer $k$, i.e., after $k$ : weeks, your intake is $S(k): 2500-50 \mathrm{k}$ calories.

Now, prove it for $k+1$ weeks: After $\mathrm{k}+1$ weeks, your intake will be:

$$
2500-50 k-50=2500-50(k+1) \text { calories. The formula holds for } k+1
$$

Conclusion: By mathematical induction, your daily intake after $n$ weeks is $2500-50 n$ calories.

# EXERCISE 8.1

1. Use mathematical induction to prove the following formulae for every positive integer $n$.
(i) $\log x^{2}=n \log x$, where $x$ is positive
(ii) $2+5+8+\ldots+(3 n-1)=\frac{n}{2}(3 n+1)$
(iii) $2+(2+5)+(2+5+8)+\cdots+\frac{n}{2}(3 n+1)=\frac{n}{4}(n+1)^{2}$
(iv) $2+6+18+\cdots+2 \times 3^{n-1}=3^{n}-1$
(v) $1 \times 3+2 \times 5+3 \times 7+\cdots+n \times(2 n+1)=\frac{n(n+1)(4 n+5)}{6}$
(vi) $\frac{1}{1 \times 2}+\frac{1}{2 \times 3}+\frac{1}{3 \times 4}+\cdots+\frac{1}{n(n+1)}=1-\frac{1}{n+1}$

(vii) $r+r^{2}+r^{3}+\cdots+r^{n}=\frac{r\left(1-r^{n}\right)}{1-r}, \quad(r \neq 1)$
(viii) $a+(a+d)+(a+2 d)+\cdots+[a+(n-1) d]=\frac{n}{2}[2 a+(n-1) d]$
(ix) $a_{n}=a_{1}+(n-1) d \quad$ when, $a_{1}, a_{1}+d, a_{1}+2 d, \ldots$ form an A.P.
(x) $a_{n}=a_{1} r^{n-1} \quad$ when $a_{1}, a_{1} r, a_{1} r^{2}, \ldots$ form a G.P.
(xi) $\binom{3}{3}+\binom{4}{3}+\binom{5}{3}+\cdots+\binom{n+2}{3}=\binom{n+3}{4}$
(xii) The sum of first $n$ odd natural numbers is $n^{2}$.
2. Prove by mathematical induction that for all positive integral values of $n$
(i) $n^{2}+n$ is divisible by 2
(ii) $5^{n}-2^{n}$ is divisible by 3
(iii) $8 \times 10^{n}-2$ is divisible by 6
3. Prove that $\sum_{i=1}^{n} r^{n}=\frac{r^{n+1}-1}{r-1}$, whenever $n$ is a positive integer.
4. $x-y$ is a factor of $x^{n}-y^{n}$ for all positive integral values of $n,(x \neq y)$.
5. $n!>2^{n}-1$ for integral values of $n \geq 4$.
6. $4^{n}>3^{n}+2^{n-1}$ for integral values of $n \geq 2$.
7. $1+n x \leq(1+x)^{n}$ for $n \geq 2$ and $x \geq-1$.
8. Aliza invests Rs. $1,000,000$ in a business that promises a $6 \%$ return compounded annually. Prove by mathematical induction that the amount of money after $n$ years is $1,000,000(1.06)$
9. A bank offers an investment with an annual interest rate $r$. If $P$ rupees are invested, the amount after $n$ years is given by: $A(n)=P(1+r)$
Prove by induction that this formula holds for all $n \geq 0$.
10. Sikander saves Rs. 500 in the first month and increases his savings by Rs. 500 every subsequent month. Using mathematical induction, determine whether his total savings will reach at least Rs. 12,000 after 24 months.
11. Prove by mathematical induction that if Ali takes a loan of Rs. 2,000,000 and pay Rs. 50,000 at the end of each year, the remaining balance after $n$ years is $R_{n}=2,000,000-50,000 n$.
12. If Salman start savings with Rs. 5,000 and saves an additional Rs. 1,000 at the end of every month, derive a formula $S(n)$ for his total savings after $n$ months. Prove the correctness of year formula using mathematical induction.

# 8.2 Binomial Theorem

An algebraic expression consisting of two terms such as $a+x, x-2 y, a x+b$ etc., is called a binomial or a binomial expression.
We know by actual multiplication that

$$
\begin{aligned}
& (a+b)^{2}=a^{2}+2 a b+b^{2} \\
& (a+b)^{3}=a^{3}+3 a^{2} b+3 a b^{2}+b^{3}
\end{aligned}
$$

The right sides of (i) and (ii) are called binomial expansions of the binomial $a+b$ for the indices 2 and 3 respectively.
In general, the rule or formula for expansion of a binomial raised to any positive integral power $n$ is called the binomial theorem for positive integral index $n$.
For any positive integer $n$,

$$
\begin{aligned}
(a+b)^{n}= & \binom{n}{0} a^{n}+\binom{n}{1} a^{n-1} b+\binom{n}{2} a^{n-2} b^{2}+\cdots+\binom{n}{r-1} a^{n-(r-1)} b^{r-1} \\
& +\binom{n}{r} a^{n-r} b^{r}+\cdots+\binom{n}{n-1} a b^{n-1}+\binom{n}{n} b^{n}
\end{aligned}
$$

or briefly $(a+b)^{n}=\sum_{r=1}^{n}\binom{n}{r} a^{n-r} b^{r}$, where $a$ and $b$ are real numbers.
The rule of expansion given above is called the binomial theorem and it also holds if $a$ or $b$ is complex.
Now we prove the binomial theorem for any positive integer $n$, using the principle of mathematical induction.
Proof: Let $S(n)$ be the statement given above as (A).
Base Case: If $n=1$, we obtain $S(1):(a+b)^{1}=\binom{1}{0} a^{1}+\binom{1}{1} a^{1-1} b=a+b$ which is true.
The base case is satisfied.
Induction of Hypothesis: Let us assume that the statement is true for any $n=k \in N$, then

$$
\begin{aligned}
& S(k):(a+b)^{k}=\binom{k}{0} a^{k}+\binom{k}{1} a^{k-1} b+\binom{k}{2} a^{k-2} b^{2}+\cdots+\binom{k}{r-1} a^{k-(r-1)} b^{r-1}+\binom{k}{r} a^{k-r} b^{r} \\
& +\cdots+\binom{k}{k-1} a b^{k-1}+\binom{k}{k} b^{k} \\
& S(k+1):(a+b)^{k+1}=\binom{k+1}{0} a^{k+1}+\binom{k+1}{1} a^{k} \times b+\binom{k+1}{2} a^{k-1} \times b^{2}+\cdots \\
& +\binom{k+1}{r-1} a^{k-r+2} \times b^{r-1}+\binom{k+1}{r} a^{k-r+1} \times b^{r}+\cdots+\binom{k+1}{k} a \times b^{k}+\binom{k+1}{k+1} b^{k+1}
\end{aligned}
$$

Multiplying both sides of equation (B) by $(a+b)$, we have

$$
\begin{aligned}
& (a+b)(a+b)^{k}=(a+b)\left[\binom{k}{0} a^{k}+\binom{k}{1} a^{k-1} b+\binom{k}{2} a^{k-2} b^{2}+\cdots+\binom{k}{r-1} a^{k-r+1} b^{r-1}\right. \\
& \left.+\binom{k}{r} a^{k-r} b^{r}+\cdots+\binom{k}{k-1} a b^{k-1}+\binom{k}{k} b^{k}\right] \\
& =\left[\binom{k}{0} a^{k+1}+\binom{k}{1} a^{k} b+\binom{k}{2} a^{k-1} b^{2}+\cdots+\binom{k}{r-1} a^{k-r+2} b^{r-1}\right. \\
& \left.+\binom{k}{r} a^{k-r+1} b^{r}+\cdots+\binom{k}{k-1} a^{k} b^{k-1}+\binom{k}{k} a b^{k}\right] \\
& +\left[\binom{k}{0} a^{k} b+\binom{k}{1} a^{k-1} b^{2}+\binom{k}{2} a^{k-2} b^{2}+\cdots+\binom{k}{r-1} a^{k-r-1} b^{r}\right. \\
& \left.+\binom{k}{r} a^{k-r} b^{r+1}+\cdots+\binom{k}{k-1} a b^{k}+\binom{k}{k} b^{k+1}\right] \\
& =\binom{k}{0} a^{k+1}+\left[\binom{k}{1}+\binom{k}{0}\right] a^{k} b+\left[\binom{k}{2}+\binom{k}{1}\right] a^{k-1} b^{2}+\cdots \\
& +\left[\binom{k}{r}+\binom{k}{r-1}\right] a^{k-r+1} b^{r}+\cdots+\left[\binom{k}{k}+\binom{k}{k-1}\right] a b^{k}+\binom{k}{k} b^{k+1}
\end{aligned}
$$

As $\binom{k}{0}=\binom{k+1}{0},\binom{k}{k}=\binom{k+1}{k+1}$ and $\binom{k}{r}+\binom{k}{r-1}=\binom{k+1}{r}$ for $0 \leq r \leq k$

$$
\begin{aligned}
& \therefore(a+b)^{k+1}=\binom{k+1}{0} a^{k+1}+\binom{k+1}{1} a^{k} b+\binom{k+1}{2} a^{k-1} b^{2}+\cdots \\
& +\binom{k+1}{r} a^{k-r+1} b^{r}+\cdots+\binom{k+1}{k} a b^{k}+\binom{k+1}{k+1} b^{k+1}
\end{aligned}
$$

We find that if the statement is true for $n=k$, then it is also true for $n=k+1$.
Conclusion: Hence, we conclude that the statement is true for all positive integral values of $n$.

## $\left(\binom{n}{0},\binom{n}{1},\binom{n}{2} \ldots,\binom{n}{n}\right.$ are called the binomial coefficients.

The following points can be observed in the expansion of $(a+b)^{n}$
(i) The number of terms in the expansion is one greater than its index.
(ii) The sum of exponents of $a$ and $x$ in each term of the expansion is equal to its index.
(iii) The exponent of $a$ decreases from index to zero.

(iv) The exponent of $b$ increases from zero to index.
(v) The coefficients of the terms equidistant from beginning and end of the expansion are equal as $\binom{n}{r}=\binom{n}{n-r}$
(vi) The $(r+1)^{\text {th }}$ term in the expansion is $\binom{n}{r} a^{n-r} b^{r}$ and we denote it as $T_{r+1}$ i.e.,

$$
T_{r+1}=\binom{n}{r} a^{n-r} b^{r}
$$

As all the terms of the expansion can be found from it by putting $r=0,1,2, \cdots, n$, so we call it as the general term of the expansion.
Example 13 Expand $\left(\frac{a}{2}-\frac{2}{a}\right)^{6}$ and also find its general term.

Solution $\left(\frac{a}{2}-\frac{2}{a}\right)^{6}=\left(\frac{a}{2}+\left(\frac{-2}{a}\right)\right)^{6}$

$$
\begin{aligned}
& =\left(\frac{a}{2}\right)^{6}+\binom{6}{1}\left(\frac{a}{2}\right)^{2}\left(-\frac{2}{a}\right)+\binom{6}{2}\left(\frac{a}{2}\right)^{4}\left(-\frac{2}{a}\right)^{2}+\binom{6}{3}\left(\frac{a}{2}\right)^{3}\left(-\frac{2}{a}\right)^{3} \\
& +\binom{6}{4}\left(\frac{a}{2}\right)^{2}\left(-\frac{2}{a}\right)^{4}+\binom{6}{5}\left(\frac{a}{2}\right)\left(-\frac{2}{a}\right)^{3}+\left(-\frac{2}{a}\right)^{6} \\
& =\frac{a^{6}}{64}+6\left(\frac{a^{2}}{32}\right)\left(-\frac{2}{a}\right)+\frac{6 \cdot 5}{2 \cdot 1} \cdot \frac{a^{4}}{16} \cdot \frac{4}{a^{2}}+\frac{6 \cdot 5 \cdot 4}{3 \cdot 2 \cdot 1} \cdot \frac{a^{3}}{8} \cdot\left(-\frac{8}{a^{4}}\right)+\frac{6 \cdot 5}{2 \cdot 1} \cdot \frac{a^{2}}{4} \cdot \frac{16}{a^{4}} \\
& +6 \cdot \frac{a}{2}\left(-\frac{32}{a^{2}}\right)+\frac{64}{a^{6}} \\
& =\frac{a^{6}}{64}-\frac{3}{8} a^{4}+\frac{15}{4} a^{2}-20+\frac{60}{a^{2}}-\frac{96}{a^{4}}+\frac{64}{a^{6}}
\end{aligned}
$$

$T_{r+1}$, the general term is given by

$$
\begin{aligned}
T_{r+1}= & \binom{6}{r}\left(\frac{a}{2}\right)^{6-r}\left(-\frac{2}{a}\right)^{r}=\binom{6}{r} \frac{a^{6-r}}{2^{6-r}}(-1)^{r} \frac{2^{r}}{a^{r}} \\
& =(-1)^{r}\binom{6}{r} \frac{a^{6-r}}{2^{6-r}} \frac{a^{-r}}{2^{-r}}=(-1)^{r}\binom{6}{r} \frac{a^{6-2 r}}{2^{6-2 r}}=(-1)^{r}\binom{6}{r}\left(-\frac{a}{2}\right)^{6-2 r}
\end{aligned}
$$

Example 14 Evaluate $(9.9)^{5}$ using binomial theorem.
Solution $(9.9)^{5}=(10-0.1)^{5}$

$$
\begin{aligned}
& =(10)^{5}+5 \times(10)^{4} \times(-0.1)+10(10)^{3} \times(-0.1)^{2}+10(10)^{2} \times(-0.1)^{3} \\
& +5(10)(-0.1)^{4}+(-0.1)^{5} \\
& =100000-(0.5)(10000)+(10000)(0.01)+1000(-0.001)+50(0.0001)-0.00001 \\
& =100000-5000+100-1+0.005-0.00001 \\
& =100100.005-5001.00001 \\
& =95099.00499
\end{aligned}
$$

Example 15 Find the specified term in the expansion of $\left(\frac{3}{2} x-\frac{1}{3 x}\right)^{11}$;
(i) the term involving $x^{5}$
(ii) the fifth term
(iii) the sixth term from the end
(iv) coefficient of the term involving $x^{-1}$.

# Sointion

(i) Let $T_{r+1}$ be the term involving $x^{5}$ in the expansion of $\left(\frac{3}{2} x-\frac{1}{3 x}\right)^{11}$, then

$$
\begin{aligned}
T_{r+1} & =\binom{11}{r}\left(\frac{3}{2} x\right)^{11-r}\left(-\frac{1}{3 x}\right)^{r} \\
& =\binom{11}{r} \frac{3^{11-r}}{2^{11-r}} x^{11-r} \cdot(-1)^{r} \cdot 3^{-r} x^{-r}=(-1)^{r} \cdot\binom{11}{r} \frac{3^{11-2 r}}{2^{11-r}} x^{11-2 r}
\end{aligned}
$$

As this term involves $x^{5}$ so the exponent of $x$ is 5 , that is,

$$
11-2 r=5 \text { or }-2 r=5-11 \Rightarrow r=3
$$

Thus $T_{4}$ involves $x^{5}$

$$
\begin{aligned}
\therefore T_{4} & =(-1)^{5}\binom{11}{3} \frac{3^{11-6}}{2^{11-3}} x^{11-6}=(-1) \frac{11 \cdot 10 \cdot 9}{3 \cdot 2 \cdot 1} \cdot \frac{3^{5}}{2^{6}} x^{5} \\
& =-\frac{165 \cdot 243}{256} x^{5}=-\frac{40095}{256} x^{5}
\end{aligned}
$$

(ii) Putting $r=4$ in $T_{r+1}$, we get $T_{5}$,

$$
\begin{aligned}
\therefore \quad T_{5} & =(-1)^{4}\binom{11}{4} \frac{3^{11-8}}{2^{11-4}} x^{11-8}=\frac{11 \cdot 10 \cdot 9 \cdot 8}{4 \cdot 3 \cdot 2 \cdot 1} \cdot \frac{3^{3}}{2^{7}} x^{5} \\
& =\frac{11 \cdot 10 \cdot 3}{1} \cdot \frac{27}{128} x^{5}=\frac{165 \cdot 27}{64} x^{5}=\frac{4455}{64} x^{5}
\end{aligned}
$$

(iii) The 6 th term from the end term will have $(11+1)-6$ that is, 6 terms before it, $\therefore$ It will be $(6+1)^{\text {th }}$ term, that is the $7^{\text {th }}$ term of the expansion.

$$
\begin{aligned}
\text { Thus } T_{7} & =(-1)^{6}\binom{11}{6} \frac{3^{11-12}}{2^{11-6}} x^{11-12}=\frac{11 \cdot 10 \cdot 9 \cdot 8 \cdot 7}{5 \cdot 4 \cdot 3 \cdot 2 \cdot 1} \cdot \frac{3^{-1}}{2^{5}} x^{-1} \\
& =\frac{11 \times 6 \times 7}{1} \cdot \frac{1}{3 \times 32} \cdot \frac{1}{x}=\frac{77}{16 x}
\end{aligned}
$$

(iv) $\frac{77}{16}$ is the coefficient of the term involving $x^{-1}$.

# 8.2.1 The Middle Term in the Expansion of $(a+b)^{n}$

In the expansion of $(a+b)^{n}$, the total number of terms is $n+1$
Case I: ( $\boldsymbol{n}$ is even) If $n$ is even then $n+1$ is odd, so $\left(\frac{n}{2}+\frac{1}{2}\right)^{1 / 2}$ term will be the only one middle term in the expansion.
Case II: ( $\boldsymbol{n}$ is odd) if $\boldsymbol{n}$ is odd then $\boldsymbol{n}+1$ is even so $\left(\frac{n+1}{2}\right)^{1 / 2}$ and $\left(\frac{n+3}{2}\right)^{1 / 2}$ terms of the expansion will be the two middle terms.

Example 16 Find the following in the expansion of $\left(\frac{x}{2}+\frac{2}{x^{3}}\right)^{12}$;
(i) the term independent of $x$
(ii) the middle term

Solution (i) Let $T_{r+1}$ be the term independent of $x$ in the expansion of

$$
\begin{aligned}
& \left(\frac{x}{2}+\frac{2}{x}\right)^{12}, \text { then } \\
& T_{r+1}=\binom{12}{r}\left(\frac{x}{2}\right)^{12-r}\left(\frac{2}{x^{3}}\right)^{r} \\
& =\binom{12}{r} \frac{x^{12-r}}{2^{12-r}} \cdot 2^{r} \cdot x^{-3 r}=\binom{12}{r} 2^{2 r-12} \cdot x^{12-3 r}
\end{aligned}
$$

As the term is independent of $x$, so exponent of $x$, will be zero.
That is, $\quad 12-3 r=0 \Rightarrow r=4$.
Therefore, the required term $\mathrm{T}_{5}=\binom{12}{4} 2^{8-12} x^{13-13}=\frac{12 \cdot 11 \cdot 10 \cdot 9}{4 \cdot 3 \cdot 2 \cdot 1} \cdot 2^{-4} x^{0}$

$$
=\frac{11 \times 45}{2^{4}}=\frac{495}{16}
$$

(ii) In this case, $n=12$ which is even, so $\left(\frac{12}{2}+1\right)^{\text {th }}$ term is the middle term.

$$
\begin{aligned}
T_{7} & =\binom{12}{6}\left(\frac{x}{2}\right)^{12-6} \cdot\left(\frac{2}{x^{2}}\right)^{6} \text { Because } T_{7} \text { is the required term. } \\
& =\binom{12}{6} \frac{x^{6}}{2^{6}} \cdot \frac{2^{6}}{x^{12}}=\frac{12 \times 11 \times 10 \times 9 \times 8 \times 7}{6 \times 5 \times 4 \times 3 \times 2 \times 1} \cdot x^{6-12} \\
& =\frac{12 \times 11 \times 7}{x^{6}}=\frac{924}{x^{6}}
\end{aligned}
$$

# 8.2.2 Some Deductions from the binomial expansion of $(a+b)^{n}$

We know that

$$
\begin{aligned}
(a+b)^{n}=\binom{n}{0} a^{n}+\binom{n}{1} a^{n-1} b+\binom{n}{2} & a^{n-2} b^{2}+\cdots \\
& +\binom{n}{r} a^{n-r} b^{r}+\cdots+\binom{n}{n-1} a b^{n-1}+\binom{n}{n} b^{n}
\end{aligned}
$$

(i) If we put $a=1$, in (A), then we have;

$$
\begin{aligned}
(1+b)^{n} & =\binom{n}{0}+\binom{n}{1} b+\binom{n}{2} b^{2}+\cdots+\binom{n}{r} b^{r}+\cdots+\binom{n}{n-1} b^{n-1}+\binom{n}{n} b^{n} \\
& =1+n b+\frac{n(n-1)}{2!} b^{2}+\cdots+\frac{n(n-1)(n-2) \cdots(n-r+1)}{r!} b^{r}+\cdots+n b^{n-1}+b^{n} \\
\because\left\{\left(\begin{array}{l}
n \\
r
\end{array}\right)\right. & =\frac{n!}{r!(n-r)!}=\frac{n(n-1)}{r!(n-r)!}=\frac{(n-r+1)(n-r)!}{r!}=\frac{n(n-1) \cdots(n-r-1)}{r!}
\end{aligned}
$$

(ii) Putting $a=1$ and replacing $b$ by $-b$, in (A), we get.

$$
\begin{aligned}
(1-b)^{n} & =\binom{n}{0}+\binom{n}{1}(-b)+\binom{n}{2}(-b)^{2}+\binom{n}{3}(-b)^{3}+\cdots+\binom{n}{n-1}(-b)^{n-1}+\binom{n}{n}(-b)^{n} \\
& =\binom{n}{0}-\binom{n}{1} b+\binom{n}{2} b^{2}-\binom{n}{3} b^{3}+\cdots+(-1)^{n-1}\binom{n}{n-1} b^{n-1}+(-1)^{n}\binom{n}{n} b^{n}
\end{aligned}
$$

(iii) We can find the sum of the binomial coefficients by putting $a=1$ and $b=1$ in (A).
i.e., $(1+1)^{n}=\binom{n}{0}+\binom{n}{1}+\binom{n}{2}+\cdots+\binom{n}{n-1}+\binom{n}{n}$
or $2^{n}=\binom{n}{0}+\binom{n}{1}+\binom{n}{2}+\cdots+\binom{n}{n-1}+\binom{n}{n}$
Thus, the sum of coefficients in the binomial expansion equals to $2^{n}$.

(iv) Putting $a=1$ and $b=-1$, in (A), we have

$$
(1-1)^{n}=\binom{n}{0}=\binom{n}{1}+\binom{n}{2}=\binom{n}{3}+\cdots+(-1)^{n-1}\binom{n}{n-1}+(-1)^{n}\binom{n}{n}
$$

Thus $\binom{n}{0}=\binom{n}{1}+\binom{n}{2}=\binom{n}{3}+\cdots+(-1)^{n-1}\binom{n}{n-1}+(-1)^{n}\binom{n}{n}=0$
If $n$ is odd positive integer, then

$$
\binom{n}{0}+\binom{n}{2}+\cdots+\binom{n}{n-1}=\binom{n}{1}+\binom{n}{3}+\cdots+\binom{n}{n}
$$

If $n$ is even positive integer, then

$$
\binom{n}{0}+\binom{n}{2}+\cdots+\binom{n}{n}=\binom{n}{1}+\binom{n}{3}+\cdots+\binom{n}{n-1}
$$

Thus, sum of odd coefficients of a binomial expansion equals to the sum of its even coefficients.
Example 17 Show that: $\binom{n}{1}+2\binom{n}{2}+3\binom{n}{3}+\cdots+n\binom{n}{n}=n \cdot 2^{n-1}$
Solution $\binom{n}{1}+2\binom{n}{2}+3\binom{n}{3}+\cdots+n\binom{n}{n}=n+2 \frac{n(n-1)}{2!}+3 \frac{n(n-1)(n-2)}{3!}+\cdots+n \cdot 1$

$$
\begin{aligned}
& =n\left[1+(n-1)+\frac{(n-1)(n-2)}{2!}+\cdots+1\right] \\
& =n\left[\binom{n-1}{0}+\binom{n-1}{1}+\binom{n-1}{2}+\cdots+\binom{n-1}{n-1}\right]=n \cdot 2^{n-1}
\end{aligned}
$$

# EXERCISE 8.2

1. Using binqinal theorem, expand the following:
(i) $\left(\frac{x}{2}-\frac{2}{x^{2}}\right)^{4}$
(ii) $\left(2 a-\frac{x}{a}\right)^{7}$
(iii) $\left(\sqrt{\frac{a}{x}}-\sqrt{\frac{x}{a}}\right)^{6}$
2. Calculate the following by means of binomial theorem:
(i) $(0.97)^{3}$
(ii) $(2.02)^{4}$
(iii) $(9.98)^{4}$
(iv) $(2.1)^{5}$
3. Expand and simplify the following:
(i) $(a+\sqrt{2} x)^{4}+(a-\sqrt{2} x)^{4}$
(ii) $(2+\sqrt{3})^{5}+(2-\sqrt{3})^{5}$
4. Expand the following in ascending power of $x$ :
(i) $\left(2+x-x^{2}\right)^{4}$
(ii) $\left(1-x+x^{2}\right)^{4}$

5. Find the term involving:
(i) $x^{4}$ in the expansion of $(3-2 x)^{7}$
(ii) $x^{-2}$ in the expansion of $\left(x-\frac{2}{x^{2}}\right)^{13}$
(iii) $a^{4}$ in the expansion of $\left(\frac{2}{x}-a\right)^{9}$
(iv) $y^{3}$ in the expansion of $(x-\sqrt{y})^{11}$
6. Find the coefficient of;
(i) $x^{3}$ in the expansion of $\left(x^{2}-\frac{3}{2 x}\right)^{18}$
(ii) $x^{n}$ in the expansion of $\left(x^{2}-\frac{1}{x}\right)^{2 n}$
7. Find $6^{\text {th }}$ term in the expansion of $\left(x^{2}-\frac{3}{2 x}\right)^{10}$.
8. Find the term independent of $x$ in the following expansions;
(i) $\left(x-\frac{2}{x}\right)^{10}$
(ii) $\left(\sqrt{x}+\frac{1}{2 x^{2}}\right)^{10}$
(iii) $\left(1+x^{2}\right)^{3}\left(1+\frac{1}{x^{2}}\right)^{4}$
9. Determine the middle term in the following expansions:
(i) $\left(\frac{1}{x}-\frac{x^{2}}{2}\right)^{12}$
(ii) $\left(\frac{3}{2} x-\frac{1}{3 x}\right)^{11}$
(iii) $\left(2 x-\frac{1}{2 x}\right)^{2 m+1}$
10. Show that: $\binom{n}{1}+\binom{n}{2}+\binom{n}{3}+\ldots+\binom{n}{n}=2^{n}-1$

# 8.3 The Binomial Theorem (When the Index $n$ is a Negative Integer or a Fraction)

When $n$ is a negative integer or a fraction, then

$$
\begin{aligned}
(1+x)^{n}=1+n x & +\frac{n(n-1)}{2!} x^{2}+\frac{n(n-1)(n-2)}{3!} x^{3}+\ldots \\
& +\frac{n(n-1)(n-2) \cdots(n-r+1)}{r!} x^{r}+\ldots
\end{aligned}
$$

provided $|x|<1$.
The series of the type $1+n x+\frac{n(n-1)}{2!} x^{2}+\frac{n(n-1)(n-2)}{3!} x^{3}+\ldots$ is called the binomial series.

## - The proof of this theorem is beyond the scope of this book.
- Symbols $\binom{n}{0}\binom{n}{1}\binom{n}{2}$ etc are meaningless when $n$ is a negative integer or a fraction.
- The general term in the expansion is $T_{n 1}=\frac{n(n-1)(n-2) \cdots(n-r+1)}{r!} x^{r}$

Example 18 Find the general term in the expansion of $(1+x)^{-2}$ when $|x|<1$.
$$
\begin{aligned}
& T_{r+1}=\frac{(-3)(-4)(-5) \cdots(-3-r+1)}{r!} x^{r} \\
= & \frac{(-1)^{r} \cdot 3 \cdot 4 \cdot 5 \cdots(r+2)}{r!} x^{r} \quad=(-1)^{r} \frac{1 \cdot 2 \cdot 3 \cdot 4 \cdot 5 \cdots(r+2)}{1 \cdot 2 \cdot r!} x^{r} \\
= & (-1)^{r} \frac{r! \cdot(r+1)(r+2)}{2 \cdot r!} x^{r}=(-1)^{r} \frac{(r+1)(r-2)}{2} x^{r}
\end{aligned}
$$

Some particular cases of the expansion of $(1+x)^{n}, n<0$.
(i) $(1+x)^{-1}=1-x+x^{2}-x^{3}+\cdots+(-1)^{r} x^{r}+\cdots$
(ii) $(1+x)^{-2}=1-2 x+3 x^{2}-4 x^{3}+\ldots+(-1)^{r}(r+1) x^{r}+\cdots$
(iii) $(1+x)^{-3}=1-3 x+6 x^{2}-10 x^{3}+\cdots+(-1)^{r} \frac{(r+1)(r+2)}{2} x^{r}+\cdots$
(iv) $(1-x)^{-1}=1+x+x^{2}+x^{3}+\cdots+x^{r}+\cdots$
(v) $(1-x)^{-5}=1+2 x+3 x^{2}+4 x^{3}+\cdots+(r+1) x^{r}+\cdots$
(vi) $(1-x)^{-8}=1+3 x+6 x^{2}+10 x^{3}+\cdots+\frac{(r+1)(r+2)}{2} x^{r}+\cdots$

Example 19 Find the coefficient of $x^{n}$ in the expansion of $\frac{1-x}{(1+x)^{2}}$
Solution $\frac{1-x}{(1+x)^{2}}=(1-x)(1+x)^{-2}$

$$
\begin{aligned}
& =(-x+1)\left[1+(-2 x)+\frac{(-2)(-3)}{2!} x^{2}+\cdots+\frac{(-2)(-3) \cdots(-2-r+1)}{r!} x^{r}+\cdots\right] \\
& =(-x+1)\left[1+(-1) 2 x+(-1)^{2} 3 x^{2}+\cdots+(-1)^{r} \times(r+1) x^{r}+\cdots\right] \\
& =(-x+1)\left[1+(-1) 2 x+(-1)^{2} 3 x^{2}+\cdots+(-1)^{n-1} n x^{n-1}+(-1)^{n}(n+1) x^{n}+\cdots\right] \\
& \text { Coefficient of } x^{n}=(-1)(-1)^{n-1} n+(-1)^{n}(n+1) \\
& =(-1)^{n} n+(-1)^{n}(n+1)=(-1)^{n}[n+(n+1)]=(-1)^{n}(2 n+1)
\end{aligned}
$$

Example 20 If $x$ is so small that its cube and higher power can be neglected, show that $\sqrt{\frac{1-x}{1+x}} \approx 1-x+\frac{1}{2} x^{2}$
Solution $\sqrt{\frac{1-x}{1+x}}=(1-x)^{1 / 2}(1+x)^{-1 / 2}$

$$
=\left[1+\frac{1}{2}(-x)+\frac{\frac{1}{2}\left(\frac{1}{2}-1\right)}{2!}(-x)^{2}+\cdots\right]\left[1+\left(-\frac{1}{2}\right) x+\frac{\left(-\frac{1}{2}\right)\left(-\frac{1}{2}-1\right)}{2!} x^{2}+\cdots\right]
$$

$$
\begin{aligned}
& =\left[1-\frac{1}{2} x-\frac{1}{8} x^{2}+\ldots\right]\left[1-\frac{1}{2} x+\frac{3}{8} x^{2}+\cdots\right] \\
& =\left[\left(1-\frac{1}{2} x+\frac{3}{8} x^{2}\right)+\left(-\frac{1}{2} x+\frac{1}{4} x^{2}\right)-\frac{1}{8} x^{2}+\cdots\right] \\
& =1-\left(\frac{1}{2}+\frac{1}{2}\right) x+\left(\frac{3}{8}+\frac{1}{4}-\frac{1}{8}\right) x^{2}+\cdots \approx 1-x+\frac{1}{2} x^{2}
\end{aligned}
$$

Example:1 For $y=\frac{1}{2}\left(\frac{4}{9}\right)+\frac{1 \cdot 3}{2^{2} 2!}\left(\frac{4}{9}\right)^{2}+\frac{1.3 .5}{2^{3} 3!}\left(\frac{4}{9}\right)^{3}+\cdots$ show that $5 y^{2}+10 y-4=0$
Solution $y=\frac{1}{2}\left(\frac{4}{9}\right)+\frac{1.3}{4.2!}\left(\frac{4}{9}\right)^{2}+\frac{1.3 .5}{8.3!}\left(\frac{4}{9}\right)^{3}+\cdots$
Adding 1 to both sides of (A), we obtain

$$
1+y=1+\frac{1}{2}\left(\frac{4}{9}\right)+\frac{1 \cdot 3}{4 \cdot 2!}\left(\frac{4}{9}\right)^{2}+\frac{1 \cdot 3 \cdot 5}{8 \cdot 3!}\left(\frac{4}{9}\right)^{3}+\cdots
$$

Let the series on the right side of (B) be identical with

$$
1+n x+\frac{n(n-1)}{2!} x^{2}+\frac{n(n-1)(n-2)}{3!} x^{3}+\cdots
$$

which is the expansion of $(1+x)^{n}$ for $|x|<1$ and $n$ is not a positive integer.
By comparing terms of both the series, we get

$$
\begin{aligned}
n x & =\frac{1}{2}\left(\frac{4}{9}\right)^{2} \\
\frac{n(n-1)}{2!} x^{2} & =\frac{1 \cdot 3}{4 \cdot 2!}\left(\frac{4}{9}\right)^{2}
\end{aligned}
$$

From (i), $\quad x=\frac{2}{9 n}$
Substituting $x=\frac{2}{9 n}$ in (ii), we get
$\frac{n(n-1)}{2}\left(\frac{2}{9 n}\right)^{2}=\frac{3}{8} \cdot \frac{16}{81}$ or $\frac{n(n-1)}{2} \cdot \frac{4}{81 n^{2}}=\frac{3}{8} \cdot \frac{16}{81}$
or $\quad 2(n-1)=6 n \quad$ or $n-1=3 n \Rightarrow n=-\frac{1}{2}$

Putting

$$
n=-\frac{1}{2} \text { in (iii), we get } x=\frac{2}{9\left(-\frac{1}{2}\right)}=-\frac{4}{9}
$$

Thus

$$
1+y=\left(1-\frac{4}{9}\right)^{-1 / 2}=\left(\frac{5}{9}\right)^{-1 / 2}=\left(\frac{9}{5}\right)^{1 / 2}=\frac{3}{\sqrt{5}}
$$

or $\sqrt{5}(1+y)=3$
Squaring both the sides of (iv), we get

$$
5\left(1+2 y+y^{2}\right)=9 \quad \text { or } \quad 5 y^{2}+10 y-4=0
$$

# EXERCISE 8.3

1. Expand the following upto 4 terms, taking the values of $x$ such that the expansion in each case is valid:
(i) $(1+x)^{-1 / 3}$
(ii) $(4-3 x)^{1 / 2}$
(iii) $\frac{(1-x)^{-1}}{(1+x)^{2}}$
(iv) $\frac{\sqrt{1+2 x}}{1-x}$
2. Find the coefficient of $x^{n}$ in the expansion of:
(i) $\frac{1+x^{2}}{(1+x)^{2}}$
(ii) $\frac{(1+x)^{2}}{(1-x)^{2}}$
3. If $x$ is so small that its square and higher powers can be neglected, then show that:
(i) $\frac{1-x}{\sqrt{1+x}} \approx 1-\frac{3}{2} x$
(ii) $\frac{\sqrt{1+2 x}}{\sqrt{1-x}} \approx 1+\frac{3}{2} x$
(iii) $\frac{(9+7 x)^{1 / 2}-(16+3 x)^{1 / 4}}{4+5 x} \approx \frac{1}{4}-\frac{17}{384} x$
(iv) $\frac{\sqrt{4+x}}{(1-x)^{2}} \approx 2+\frac{25}{4} x$
4. If $x$ is so small that its cube and higher power can be neglected, show that:
(i) $\sqrt{1-x-2 x^{2}} \approx 1-\frac{1}{2} x-\frac{9}{8} x^{2}$
(ii) $\sqrt{\frac{1+x}{1-x}} \approx 1+x+\frac{1}{2} x^{2}$
5. If $x$ is very nearly equal 1 , then prove that $p x^{p}-q x^{q} \approx(p-q) x^{p+q}$
6. Identify the following series as binomial expansion and find the sum.

$$
1-\frac{1}{2}\left(\frac{1}{4}\right)+\frac{1 \cdot 3}{2!4}\left(\frac{1}{4}\right)^{2}-\frac{1 \cdot 3 \cdot 5}{3!8}\left(\frac{1}{4}\right)^{3}+\cdots
$$

7. Use binomial theorem to show that $1+\frac{1}{4}+\frac{1 \cdot 3}{4 \cdot 8}+\frac{1 \cdot 3 \cdot 5}{4 \cdot 8 \cdot 12}+\cdots=\sqrt{2}$

8. If $y=\frac{1}{3}+\frac{1 \cdot 3}{2!}\left(\frac{1}{3}\right)^{2}+\frac{1 \cdot 3 \cdot 5}{3!}\left(\frac{1}{3}\right)^{3}+\cdots$ prove that $y^{2}+2 y-2=0$.
9. If $2 y=\frac{1}{2^{2}}+\frac{1 \cdot 3}{2!} \cdot \frac{1}{2^{4}}+\frac{1 \cdot 3 \cdot 5}{3!} \cdot \frac{1}{2^{6}}+\cdots$, prove that $4 y^{2}+4 y-1=0$
10. Show that the coefficient of $x^{r}$ in $\frac{x}{(1-p x)(1-q x)}$ is $\frac{p^{r}-q^{r}}{p-q}$.

# 8.4 Binomial Coefficients Using Pascal's Triangle

Binomial coefficients arise in the binomial expansion of powers of a binomial expression, such as $(x+y)^{n}$. These coefficients are denoted by:

$$
\binom{n}{r}=\frac{n!}{r!(n-r)!}, \text { where } 0 \leq r \leq n
$$

Pascal's Triangle provides a combinatorial method to compute binomial coefficients without directly using factorials. The construction of Pascal's triangle follows these rules:

1. The first row (corresponding to $n=0$ ) consists of a single entry:1.
2. Each subsequent row begins and ends with 1 .
3. Every interior entry is the sum of the two entries directly above it from the previous row.
Mathematically, this is expressed by Pascal's Rule:

$$
\text { Pascal's Rule: }\binom{n}{k}=\binom{n-1}{k-1}+\binom{n-1}{k}, \quad \text { for } 0<k<n
$$

The entries in the $n^{\text {th }}$ row of Pascal's Triangle correspond to the binomial coefficients $\binom{n}{0},\binom{n}{1}, \ldots,\binom{n}{n}$
For example, the binomial coefficients corresponding to $n=4$ are:

$$
\binom{4}{0}=1,\binom{4}{1}=4,\binom{4}{2}=6,\binom{4}{3}=4,\binom{4}{4}=1
$$

Example 22 Expand $(x+y)^{4}$ using Pascal's triangle.
Solution The binomial coefficients for the expansion of correspond to the entries in the $n=4$ row of Pascal's triangle: 14641
Thus, the binomial expansion using Pascal's triangle is

$$
\begin{aligned}
& (x+y)^{4}=1 x^{4}+4 x^{3} y+6 x^{2} y^{2}+4 x y^{3}+1 y^{4} \\
& (x+y)^{4}=x^{4}+4 x^{3} y+6 x^{2} y^{2}+4 x y^{3}+y^{4}
\end{aligned}
$$

Example 23 Expand $(x-2)^{5}$ use the binomial theorem and using Pascal's triangle.
Solution Expand using Binomial Theorem:

$$
\begin{aligned}
(x-2)^{5} & ={ }^{5} C_{0} x^{5}(-2)^{0}+{ }^{5} C_{1} x^{5-1}(-2)^{1}+{ }^{5} C_{2} x^{5-2}(-2)^{2}+{ }^{5} C_{3} x^{5-3}(-2)^{3} \\
& =x^{5}-10 x^{4}+40 x^{3}-80 x^{2}+80 x-32
\end{aligned}
$$

The binomial coefficients for the expansion of correspond to the entries in the $n=5$ row of Pascal's triangle: 15101051
$(a+b)^{5}={ }^{5} C_{0} a^{5} b^{0}+{ }^{5} C_{1} a^{4} b^{1}+{ }^{5} C_{2} a^{3} b^{2}+{ }^{5} C_{3} a^{2} . b^{3}+{ }^{5} C_{4} a^{1} b^{4}+{ }^{5} C_{5} a^{0} b^{5}$
Replace binomial coefficient from Pascal triangle and $a=x, b=-2$

$$
\begin{aligned}
(x-2)^{5} & =x^{5}(-2)^{0}+5 x^{4}(-2)^{1}+10 x^{3}(-2)^{2}+10 x^{2}(-2)^{3}+5 x(-2)^{4}+(-2)^{5} \\
& =x^{5}-10 x^{4}+40 x^{3}-80 x^{2}+80 x-32
\end{aligned}
$$