# Chapter 4: Permutations and Combinations

## INTRODUCTION

In our daily life, permutations and combinations play a vital role in counting total number of possibilities, as well as in arrangements and selections of objects. They are used in many fields of science. For example,

- In probability theory, permutations and combinations are used to compute how many times an event can occur in various scenarios and to estimate the odds of winning a lottery.
- In biology, these are used to find out the total numbers of possible DNA sequences.
- In computer science, these are used to count the possible number of passwords of a given length by using some specific characters.
- Moreover, these are the important parts of many encryption algorithms to ensure the privacy and integrity of a data set.

### 7.1 Fundamental Principle of Counting

Danish wants to prepare invitation cards of 5 different colours (red, blue, green, orange and yellow) by changing any of 3 shapes (circle, square and rectangle). How many cards can Danish make?
The problem is to count the total number of ways in which Danish can make cards. One way to find the solution is by making tree diagram. Let us discuss another scenario: Danish's father wants to buy a table and has asked his son to help him decide. He narrowed down his options for manufacturer, types of material (wood, plastic, glass and marble) and types of shape (circle, square and rectangle). Find the total number of table choices from the above options.
Again the problem is to count the total number of ways in which Danish's father can choose a table.

$1^{\text {st }}$ Way: By making tree diagram.
From tree diagram, it is clearer there are 12 choices for Danish's father to buy a table with one type of material and one type of shape.
$2^{\text {nd }}$ Way: By multiplying, Danish's father can find the total number of table choices to buy a table with one kind of material and shape.
Total number of table choices $=$ Total types of material $\times$ Total types of shape

$$
=4 \times 3=12 \text { choices }
$$

These examples show that when making a choice involving multiple stages or categories, we can find the total number of outcomes by multiplying the number of options at each stage.

# Statement

Suppose $A$ and $B$ are two events, the event $A$ occurs in $m$ different ways, and the event $B$ occurs in $n$ different ways then the total number of ways that the two events one after another can occur in $m \times n$ ways.

$$
\text { Total number of ways }=m n
$$

Proof: Let $A=\left\{a_{1}, a_{2}, a_{3}, \cdots, a_{m}\right\}$ and $B=\left\{b_{1}, b_{2}, b_{3}, \cdots, b_{n}\right\}$. Let $P$ denotes the event that both events $A$ and $B$ occur together then $P=\left\{\left(a_{i}, b_{j}\right): a_{i} \in A, b_{j} \in B, 1 \leq i \leq m\right.$, $1 \leq j \leq n\}=A \times B$. Hence the number of ways in which both events $A$ and $B$ can occur is the number of elements in $A \times B$ which is $m n$.
This principle can be extended to three or more events. For instance, if event $A$ can occur in $m$ ways, event $B$ can occur in $n$ ways and event $C$ can occur in $k$ ways, the number of ways that three events can occur all together is the

## If three dice are rolled together, how many total numbers of ways occur?

product $m \cdot n \cdot k$.

## Factorial (I)

Suppose there are four chairs to be occupied by four students and we are interested in counting all the possible ways the students can be seated.
To occupy the first chair there are 4 options. For the second chair, only 3 students remain, so there are 3 options. Similarly, for the third and fourth chairs, there are 2 and 1 options respectively.

## History

The factorial notation (I) was introduced by Christian Kramp (1760-1826) in 1808
This notation is frequently used to solve permutation and combination.

In this way, we have to perform four independent events with $4,3,2$, and 1 options respectively.
By the Fundamental Principle of Counting, the total number of ways to occupy all the chairs is $4 \cdot 3 \cdot 2 \cdot 1=24$
Such problems frequently occur in daily life, where we have to multiply the first $n$ natural numbers: $1,2,3, \cdots, n$.
We call this product the factorial of $n$ and denote it by $n$ ! or $\mid n$, thus for a natural number $n$ :

$$
n!\text { or } \quad \underline{n}=n(n-1)(n-2) \cdots 3 \cdot 2 \cdot 1
$$

For some reason we also define $0!=1$. In general, if $n$ is a non-negative integer, then its factorial is denoted and defined as

$$
n!=\mid \underline{n}= \begin{cases}1 & \text { if } n=0 \\ n(n-1)(n-2) \ldots 3 \cdot 2 \cdot 1 & \text { if } n \geq 1\end{cases}
$$

For example,

$$
\begin{aligned}
& 1!=1 \\
& 2!=2 \cdot 1=2 \\
& 3!=3 \cdot 2 \cdot 1=6 \\
& 4!=4 \cdot 3 \cdot 2 \cdot 1=24 \\
& 5!=5 \cdot 4 \cdot 3 \cdot 2 \cdot 1=120 \\
& 6!=6 \cdot 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1=720
\end{aligned}
$$

Challenged
Can you find out $\frac{81}{3!}$ ?

It can be easily observed that

$$
n!=n(n-1)!\text { for } n \geq 1
$$

Example 1 Evaluate $\frac{8!}{6!}$
Solution $\frac{8!}{6!}=\frac{8 \cdot 7 \cdot 6 \cdot 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1}{6 \cdot 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1}=56$
Example 2 Write $8 \cdot 7 \cdot 6 \cdot 5$ in the factorial form.

Solution $8 \cdot 7 \cdot 6 \cdot 5=\frac{8 \cdot 7 \cdot 6 \cdot 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1}{4 \cdot 3 \cdot 2 \cdot 1}=\frac{8!}{4!}$ or $\frac{9!}{6!3!}=\frac{9 \cdot 8 \cdot 7 \cdot 6 \cdot 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1}{6 \cdot 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1 \cdot 3 \cdot 2 \cdot 1}=84$

# EXERCISE 7.1

1. Evaluate each of the following:
(i) $\frac{10!}{0!8!}$
(ii) $\frac{12!}{3!(12-3)!}$
(iii) $\frac{1440}{3!4!}+\frac{2400}{5!2!}$
(iv) $\frac{(n+2)!}{(n+1)!}$
2. Write each of the following in the factorial form:
(i) $n^{2}-n$
(ii) $n(n-1)(n-2) \cdots(n-r+1)$
3. Find $n$, if $(n+4)!=3024 \cdot n!$.
4. If $\frac{1}{7!}+\frac{1}{8!}=\frac{x}{9!}$, find $x$.
5. Prove that: $\frac{(2 n+1)!}{n!}=[1 \cdot 3 \cdot 5 \cdots(2 n-1)(2 n+1)] 2^{n}$
6. Express as a single fraction: $\frac{(n+2)!}{(r+2)!}+\frac{(n+1)!}{(r+1)!}$.
7. There are four distinct colored balls and four boxes of same colors as those of the balls. Determine the number of possible ways the balls, one each in a box, can be placed such that a ball does not go to a box of its own colour?

### 7.2 Permutations

One important application of the fundamental principle of counting is to determine the number of ways that objects can be arranged in order.
Definition: An arrangement of all or part of set of objects in a specific order is called a permutation. Number of permutations of $r(\leq n)$ objects taken from a set of $n$ objects is written as ${ }^{\circ} P_{r}$ or $P\left(n_{r} r_{r}\right)$.

$$
{ }^{\circ} P_{r}=\frac{n!}{(n-r)!} \quad \text { when } r \leq n
$$

According to fundamental principle of counting:
(i) Three books of mathematics for grades 1,2 and 3 can be arranged in a row taken all at a time (if books are distinct)

$$
\begin{aligned}
{ }^{\circ} P_{r} & ={ }^{3} P_{3} & \because n=r \approx 3 \\
& =\frac{3!}{(3-3)!}=\frac{3!}{0!} & \because 0!=1 \\
& =3!=3 \cdot 2 \cdot 1=6 \text { ways }
\end{aligned}
$$

(ii) Number of ways of writing the letters of the WORD taken all at a time
$$
\begin{aligned}
& { }^{n} P_{r}={ }^{4} P_{4} \\
& n=r=4 \\
& n=\text { Total number of things/objects } \\
& =\frac{4!}{(4-4)!}=\frac{4!}{0!} \\
& r=\text { The number of selected things / objects } \\
& =4!=4 \cdot 3 \cdot 2 \cdot 1=24 \text { ways }
\end{aligned}
$$

| Challenge! | Do you know! |
| :-- | :-- |
| Can you make total number of <br> permutations for the "WORD" <br> pictorially? | In 1974, "fimo Rubik" invented a popular <br> puzzle, each turn of the puzzle shows a <br> permutation of the different colours. The <br> name of this puzzle is "Rubik's Cube". |

Theorem: Prove that: ${ }^{n} P_{r}=n(n-1)(n-2) \cdots(n-r+1)=\frac{n!}{(n-r)!}$
Proof: As there are $n$ different objects to fill up $r$ places. So, the first place can be filled in $n$ ways. Since repetitions are not allowed, so after placing one object we are left with $(n-1)$ objects, thus the second place can be filled in $(n-1)$ ways. Similarly the third place can be filled in $(n-2)$ ways, and so on. This continues until the $r^{\text {th }}$ place which can be filled in $n-(r-1)=n-r+1$ ways. Therefore, by the Fundamental Principle of Counting, $r$ places can be filled by $n$ different objects in $n(n-1)(n-2) \cdots(n-r+1)$ ways.

$$
\begin{aligned}
{ }^{n} P_{r} & =n(n-1)(n-2) \ldots(n-r+1) \\
& =\frac{n(n-1)(n-2) \ldots(n-r+1)(n-r)!}{(n-r)!} \\
{ }^{n} P_{r} & =\frac{n!}{(n-r)!}
\end{aligned}
$$

Example 4 How many different 4-digit numbers can be formed out from the digits $1,2,3,4,5,6$, when no digit is repeated?
Solution The total number of digits $=6$
The digits forming each number $=4$
So, the required number of 4-digit numbers is given by:

$$
{ }^{6} P_{4}=\frac{6!}{(6-4)!}=\frac{6!}{2!}=\frac{6 \cdot 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1}{2.1}=6 \cdot 5 \cdot 4 \cdot 3=360
$$

Example 5 In how many ways can a set of 4 different mathematics books, 3 different physics books and 2 different chemistry books be placed on a shelf with a space for 9 books, if:
(a) all the books are kept without any restriction.

(b) all the books of the same subject are kept together.
(c) only the mathematics books are kept together.

# Soiation

(a) all the books are kept without any restriction.
Total number of books $=4+3+2=9$

$$
\begin{aligned}
& { }^{9} P_{2}=9!=9 \cdot 8 \cdot 7 \cdot 6 \cdot 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1 \quad 91 \text { ways } \\
& =362880 \text { ways }
\end{aligned}
$$

(b) all the books of the same subject are kept together.

$$
\begin{aligned}
& { }^{4} P_{4} \cdot{ }^{3} P_{3} \cdot{ }^{2} P_{2} \cdot{ }^{3} P_{1}=4!\cdot 3!\cdot 2!\cdot 3! \\
& =24 \cdot 6 \cdot 2 \cdot 6 \\
& =1728 \text { ways }
\end{aligned}
$$

(c) only the mathematics books are kept together.

$$
\begin{aligned}
& { }^{4} P_{4} \cdot{ }^{6} P_{3}=4!\cdot 6! \\
& =24 \cdot 720 \\
& =17280 \text { ways }
\end{aligned}
$$

Example 6 In how many ways 5 people are to be seated on a bench if:
(a) there are no restrictions
(b) two people can sit next to each other
(c) two people cannot sit next to each other.

## (a) when there is no restriction, then

$$
\text { Number of ways }={ }^{5} P_{2}=5!=120
$$

(b) when two people can sit next to each other, then

$$
\begin{aligned}
& ={ }^{4} P_{4} \cdot{ }^{2} P_{2} \\
& =4!\cdot 2!=24 \cdot 2 \\
& =48 \text { ways }
\end{aligned}
$$

## In how many ways 6 people are to seated on a table if 3 cannot sit next to each other?

# EXERCISE 7.2

1. Evaluate the following:
(i) ${ }^{10} P_{2}$
(ii) ${ }^{3} P_{2}$
(iii) ${ }^{7} P_{7}$
(iv) ${ }^{10} P_{2}$
2. Find the value of $n$ when:
(i) ${ }^{n} P_{3}=504$
(ii) ${ }^{15} P_{n}=15 \cdot 14 \cdot 13 \cdot 12 \cdot 11$
(iii) ${ }^{n} P_{3}:^{n-2} P_{2}=540: 1$
3. Prove from the first principle that:
(i) ${ }^{n} P_{r}=n \cdot{ }^{n-1} P_{r-1}$
(ii) ${ }^{n} P_{r}={ }^{n-1} P_{r}+r \cdot{ }^{n-1} P_{r-1}$
4. How many words can be formed from the letters of the following words using all letters when no letter is to be repeated:
(i) PYTHON
(ii) NETWORK
(iii) COMPUTER
5. How many signals can be given by 6 flags of different colours, using 2 flags at a time?
6. How many signals can be given by 5 flags of different colours, when any number of flags are used at a time.
7. How many 4 digit numbers can be formed, with distinct digits, with each digit odd?
8. How many numbers between 100 and 1000 can be formed by using the digits $0,1,2,3,4,5$ without repetition? How many of them are divisible by 5 ?
9. Find the numbers greater than 35000 that can be formed from the digits $1,2,3,4,5,6$, without repeating any digit.
10. Find the number of 5-digit numbers that can be formed from the digits $1,2,4,6$, 8 (when no digit is repeated), but
(i) the digits 2 and 8 are next to each others;
(ii) the digits 2 and 8 are not next to each other.
11. How many 6-digit numbers can be formed, without repeating any digit from the digits $0,1,2,3,4,5$ ? In how many of them will 0 be at the tens place?
12. How many 5-digit multiples of 5 can be formed from the digits $2,3,5,7,9$, when no digit is repeated.
13. In how many ways can 8 different books including 2 on English be arranged on a shelf in such a way that the English books are never together?
14. Find the number of arrangements of 3 different books on English and 5 different books on Urdu for placing them on a shelf such that the books on the same subject are together.
15. In how many ways can 5 boys and 4 girls be seated on a bench so that the girls and the boys occupy alternate seats?

# 7.3 Permutation of Objects Not All Different

Suppose we have to find the permutations of the letters of the word BITTER using all the letters. The word BIT ${ }_{1} \mathrm{~T}_{2}$ ER consists of 6 different letters which can be permuted among themselves in 6 ! ways.
We can see that all the letters of the word BITTER are not different. It has 2Ts in it. We can see there are 2 ! ways of replacing two $\mathrm{T}_{8}$ :

BITT $T_{1}$ ER
BITT $T_{1}$ ER
The replacement of the two $\mathrm{T}_{8}$ by $\mathrm{T}_{1}$ and $\mathrm{T}_{2}$ in any other permutation will give rise to 2 permutations.
Hence, the number of permutations of the letters of the word BITTER taken all at a time.

$$
\frac{6!}{2!}=\frac{6 \cdot 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1}{2.1}=360 \text { ways }
$$

## If there are $n_{1}$ alike objects of one kind, $n_{2}$ alike objects of second kind and $n_{n}$ alike objects are of third kind, then the number of permutations of $n$ objects taken all at a time is given by:

$$
\frac{n!}{n_{1}!\cdot n_{2}!\cdot n_{3}!}=\binom{n}{n_{1}, n_{2}, n_{3}}
$$

Example 7 In how many ways can the letters of the word MISSISSIPPI be arranged when all the letters are to be used?
Solution Total number of letters in the word $=11$

## MISSISSIPPI

I is repeated 4 times $=4$ I ways
$S$ is repeated 4 times $=4$ I ways
$P$ is repeated 2 times $=2$ I ways
$M$ comes once only $=11$ ways
Required number of permutations $=\frac{11!}{4!\cdot 4!\cdot 2!\cdot 1!}=34650$ ways

## Circular Permutations

The permutations in which the object are arranged in a circular order are known as circular permutations.

## The following circular arrangements are reflection of each other and considered same when anticlockwise and clockwise arrangements are considered identical.
Circular permutations can occur in two cases:
Case-I: When clockwise and anticlockwise arrangements are considered different In a linear arrangement, changing the order of objects results in a new arrangement. However, in a circular arrangement, rotating the entire circle does not produce a new, distinct arrangement.

For example, suppose three people $\mathrm{A}, \mathrm{B}$ and C are sitting around a round table. The following three linear arrangements
$\mathrm{A}-\mathrm{B}-\mathrm{C}, \mathrm{B}-\mathrm{C}-\mathrm{A}$ and $\mathrm{C}-\mathrm{A}-\mathrm{B}$ are considered the same in circular permutations because each one is simply a rotation of the other.
We conclude that:
3 linear permutations gives 1 circular permutation.
3 ! linear permutations gives $\frac{1}{3} \cdot 3!=\frac{3!}{3}=2$ ! permutations.
Generalizing the above idea if $n$ objects are arranged in a circle, the number of distinct circular permutations is $\frac{n!}{n}=(n-1)!$.

Case-II: When clockwise and anticlockwise arrangements are considered identical
In many real-life situations, a circular permutation and its mirror image are not considered different.
For example, if three beads red, blue, and black are arranged in a ring, then an arrangement and its reflection (as shown in the figure) are considered the same.
In such cases, we divide the total number of circular permutations by 2 to eliminate symmetrical duplicates.
Thus, in this case the number of distinct circular permutations is:

$$
\frac{(n-1)!}{2}
$$

Example 8 In how many ways can 4 persons be seated at a round table, while:
(i) clockwise and anticlockwise orders are different
(ii) clockwise and anticlockwise orders are identical.

Solution Let $A, B, C$ and $D$ be the 4 persons.
(i) If clockwise and anticlockwise orders are different

# According to Case-I

The possible number of ways are:

$$
\begin{aligned}
& =(n-1)!\text { ways } \\
& =(4-1)!=3! \\
& =3 \cdot 2 \cdot 1=6 \text { ways. }
\end{aligned}
$$

(ii) If clockwise and anticlockwise orders are identical

According to Case-II
The possible number of ways are $=\frac{(n-1)!}{2}$ ways

$$
\begin{aligned}
& =\frac{(4-1)!}{2}=\frac{31}{2} \\
& =\frac{3 \cdot 2}{2}=3 \text { ways }
\end{aligned}
$$

# EXERCISE 7.3

1. How many arrangements of the letters of the following words, taken all together can be made?
(i) PAKISTAN
(ii) CURRICULUM
(iii) PROBABILITY
2. How many permutations of the letters of the word "BANANA" can be made, if B must be the first letter in each arrangement?
3. How many arrangements of the letters of the word TRIGONOMETRY can be made, if each arrangement begins with T and ends with Y ?
4. Abdullah has a collection of 9 marbles consisting of 4 identical red marbles, 3 identical blue marbles and 2 identical green marbles. If he wants to arrange all of them is a straight row, how many distinct arrangements are possible?
5. In how many different ways can the following persons sit around a round table?
(a) 8 persons
(b) 7 persons
(c) 6 persons
6. In how many ways can 5 couples sit around a round table if no two women are sitting together?
7. How many 6 -digit numbers can be formed from the digits $7,7,8,8,9,9$ ?
8. 15 members of a club form 4 committees of $3,5,4$ and 3 members so that no member is a member of more than one committee. Find the number of committees.
9. The D.C.Os of 11 districts meet to discuss the law-and-order situation in their districts. In how many ways can they be seated at a round table, when two particular D.C.Os insist on sitting together?
10. The Governor of the Punjab calls a meeting of 14 officers. In how many ways can they be seated at a round table?
11. Fatima invites 14 people for a dinner. There are 9 males and 5 females who are seated at two different tables. Guests of one sex sit at one round table and the guests of the other sex sit at the second table. Find the number of ways in which all guests can be seated.

12. Find the number of ways in which 5 men and 5 women can be seated at a round table in such a way that no two persons of the same sex sit together.
13. In how many ways can 8 keys be arranged in a circular key ring?
14. How many necklaces can be made from 10 beads of different colours?

# 7.4 Combinations

Suppose, a teacher uses the names of few students to make a team for a writing competition. Such as Ahmad, Sana, Hamza and Danish. As a combination of team members, (Ahmad, Sana, Hamza and Danish) is equivalent to (Hamza, Ahmad, Danish and Sana). Because same students are in the combination. Consequently, you have the same team because the order of the name of the students does not matter.
So, we are interested in the membership of the

| Ahmad | Sana | Hamza | Danish |
| :-- | :-- | :-- | :-- |
| Hamza | Ahmad | Danish | Sana |

team and not in the ways the students are listed (arranged).

## Definition

A combination of $r$ objects taken out of $n$ objects is a subset of $r$ objects of a set of $n$ objects.
The number of combinations of $n$ different objects taken $r$ at a time is denoted by ${ }^{n} C_{r}$ or $C(n, r)$ or $\binom{n}{r}$ and is given by ${ }^{n} C_{r}=\frac{n!}{r!(n-r)!}$.
Theorem. Prove that ${ }^{n} C_{r}=\frac{n!}{r!(n-r)!}$.
Proof: Elements of a subset of $r$ objects of a set of $n$ objects can be arranged among themselves in $r$ ! ways. So, each combination will give rise to $r$ ! permutation. Thus, there will be ${ }^{n} C_{r} \times r$ ! permutations of $n$ different objects taken $r$ at a time that is:

$$
\begin{aligned}
& { }^{n} C_{r} \times r!={ }^{n} P_{r} \\
& \Rightarrow \quad{ }^{n} C_{r} \times r!=\frac{n!}{(n-r)!} \quad \therefore \quad{ }^{n} C_{r}=\frac{n!}{r!(n-r)!}
\end{aligned}
$$

Which completes the proof.

## Corollary:

(i) If $r=n$, then ${ }^{n} C_{n}=\frac{n!}{n!(n-n)!}=\frac{n!}{n!0!}=1$
(ii) If $r=0$, then ${ }^{n} C_{0}=\frac{n!}{0!(n-0)!}=\frac{n!}{0!n!}=1$

## The formulae ${ }^{n} P_{n}$ and ${ }^{n} C_{r}$ are also known as counting formulae. Because, they are used to count the possible number of ways without listing them all.

# 7.4.1 Applications of Combination in Real Life

Example 9 Zain has 8 different fruits. He wants to select 5 fruits out of 8 fruits to make a fruit chat. How many combinations of fruits he can select?
Solution To solve this problem, we have to find the number of combinations of 5 fruits out of 8 fruits. In this situation, $n=8$ and $r=5$.

$$
\begin{aligned}
{ }^{n} C_{r} & =\frac{n!}{r!(n-r)!} \\
\text { After putting values } & \\
\begin{aligned}
{ }^{8} C_{3} & =\frac{8!}{5!(8-5)!}=\frac{8!}{5!\cdot 3!} \\
& =\frac{8 \times 7 \times 6 \times 5!}{5!\cdot 3!}=\frac{8 \times 7 \times 6}{3 \cdot 2 \cdot 1} \\
& =8 \times 7=56 \text { ways }
\end{aligned}
$$

Zain has 56 different ways to select 5 different fruits to make a fruit chat.
Example10 In a school, a class consists of 12 girls and 8 boys. The teacher wants to select 5 students for an activity. In how many ways can the students be selected including? (i) 2 girls
(ii) 5 boys
(iii) 2 boys

| Solution | Number of girls $=12$ | Challenge! |
| :--: | :--: | :--: |
|  | Number of boys $=8$ | A restaurant offers 6 flavours of pizza. How many ways are there to select 2 flavours of pizza? |

(i) Now let's find the total number of ways to select students when exactly 2 are girls.
${ }^{12} C_{2}{ }^{8} C_{3}=\frac{12!}{2!10!} \cdot \frac{8!}{3!5!}=\frac{12 \cdot 11 \cdot 10!}{2 \cdot 10!} \cdot \frac{8 \cdot 7 \cdot 6 \cdot 5!}{3 \cdot 2 \cdot 1 \cdot 5!}=3696$
(ii) Let's find total number of ways to select students when exactly 5 students are boys.

$$
{ }^{8} C_{3}=\frac{8!}{5!(8-5)!}=\frac{8!}{5!3!}=\frac{8 \cdot 7 \cdot 6 \cdot 5!}{5!3 \cdot 2 \cdot 1}=56
$$

(iii) Let's find total number of ways to select students when exactly 2 students are boys.

$$
{ }^{8} C_{2}{ }^{12} C_{3}=\frac{8!}{2!6!} \cdot \frac{12!}{3!9!}=\frac{8 \cdot 7 \cdot 6!}{2 \cdot 6!} \cdot \frac{12 \cdot 11 \cdot 10 \cdot 9!}{3 \cdot 2 \cdot 1 \cdot 9!}=36960
$$

### 7.4.2 Complementary Combinations

Theorem. Prove that: ${ }^{n} C_{r}={ }^{n} C_{n-r}$
Proof: If from $n$ different objects, we select $r$ objects then $(n-r)$ objects are left. Corresponding to every combination of $r$ objects, there is a combination of $(n-r)$

objects and vice versa. Thus, the number of combinations of $n$ objects taken $r$ at a time is equal to the number of combinations of $n$ objects taken $(n-r)$ at a time.

$$
\begin{aligned}
\therefore \quad{ }^{n} C_{r} & ={ }^{n} C_{n-r} \\
{ }^{n} C_{n-r} & =\frac{n!}{(n-r)!(n-n+r)!} \\
& =\frac{n!}{r!(n-r)!} \\
{ }^{n} C_{n-r} & ={ }^{n} C_{r}
\end{aligned}
$$

Note
This result will be found useful in evaluating
${ }^{n} C_{r}$ when $r>\frac{n}{2}$.
For example,
${ }^{12} C_{10}={ }^{12} C_{12-10}={ }^{12} C_{2}=\frac{(12) \cdot(11)}{2}=6 \cdot 11=66$

Note
${ }^{n} C_{r}$ and ${ }^{n} C_{n-r}$ are known as complementary combinations.
Example 11 Find the number of the diagonals of a 6 -sided figure.
Solution A 6 -sided figure has 6 vertices. By joining any two vertices, we get a line segment.
$\therefore \quad$ Number of line segments $={ }^{6} C_{2}=\frac{6!}{2!4!}=15$
But these line segments include 6 sides of the figure
$\therefore \quad$ number of diagonals $=15-6=9$
Difference between permutation and combination

| Permutation | Combination |
| :--: | :--: |
| - Order is important. <br> e.g., $a b$ and $b a$ are different (because order of any object is matter) | - Order is not important <br> e.g., $a b$ and $b a$ are same (because order does not matter) |
| - Arrangement of objects <br> e.g. arrangement of: | - Selection of objects <br> e.g. selection of: |
| - ball of different colours | - different colours |
| - English alphabet (letters) | - members in a team |
| - people while sitting on chairs | - food items |

# Application of Permutations and Combinations in Cryptography

Example 12 Zain wants to generate a password for his laptop to secure the data. He can take only 6 characters to generate a password. Each character can either be an upper case letter $(A-Z)$ or digits from $(0-9)$.
Can you tell how many passwords can be generated by using the above letters and digits:
(i) if repetition of characters is not allowed
(ii) if repetition of characters is allowed

Solution
Total number of letters $=26$
Total number of digits $=10$
Total number of letters and digits $=26+10=36$
$n=$ total number of characters $=36$
$r=$ required number of characters $=6$
(i) If repetition of characters is not allowed, we find out total possible permutations as.

$$
\begin{aligned}
{ }^{n} P_{r}={ }^{36} P_{0} & =\frac{36!}{(36-6)!}=\frac{36!}{30!} \\
& =\frac{36 \cdot 35 \cdot 34 \cdot 33 \cdot 32 \cdot 31 \cdot 30!}{30!} \\
& =36 \cdot 35 \cdot 34 \cdot 33 \cdot 32 \cdot 31 \\
& =1,402,410,240 \text { ways }
\end{aligned}
$$

Hence, $1,402,410,240$ passwords can be generated by using the 26 alphabet and 10 digits. (If repetition of the characters is not allowed)
(ii) If the repetition of the characters is allowed Using fundamental principle of counting:
The total number of possible combinations $=36 \times 36 \times 36 \times 36 \times 36 \times 36=36^{6}$ Hence, $36^{6}$ passwords can be generated by using the 26 alphabets and 10 digits, If repetition of characters is allowed.
Application of permutations to estimate the odd of winning the lottery.
Example 13 A box contains 15 cards from ( $1-15$ ). Danish is to select 5 cards. If all the selected cards are the first five multiples of 2 then Danish will win the game. Find Danish's chance of winning the game, when
(i) order is important
(ii) order is not important

Solution $n=$ total number of cards $=15$
$r=$ required number of cards $=5$
(i) When order is important,

$$
\begin{aligned}
\text { Total possible ways } & ={ }^{n} P_{r}={ }^{15} P_{0}=\frac{15!}{(15-5)!} \\
& =\frac{15!}{10!}=360,360 \text { ways }
\end{aligned}
$$

Hence, Danish's chance to win the game $=\frac{1}{360,360}=0.000002775$

(ii) When order is not important

$$
\begin{aligned}
& n=\text { Total number of cards }=15 \\
& r=\text { Required number of cards }=5
\end{aligned}
$$

Total possible ways $={ }^{a} C_{r}={ }^{15} C_{5}=\frac{15!}{5!(15-5)!}$

$$
\begin{aligned}
& =\frac{15!}{5!10!}=\frac{15 \times 14 \times 13 \times 12 \times 11 \times 10!}{51.10!} \\
& =\frac{15 \times 14 \times 13 \times 12 \times 11}{5 \times 4 \times 3 \times 2 \times 1}=3003 \text { ways }
\end{aligned}
$$

Hence, Danish's chance to win the game $=\frac{1}{3003}=0.00033$
Application of Permutation and Combination to choose different sets of songs for Certain Occasions
Example 14 On Independence Day, a DJ has a list of ten different national songs. He wants to select any five national songs for the day. Find how many ways he can select and play the songs:
(i) if the order of playing the songs matters
(ii) if the order of playing the songs does not matter

Solution (i) When order matters

$$
\begin{aligned}
& n=\text { total number of national songs }=10 \\
& r=\text { required number of national songs }=5
\end{aligned}
$$

Total number of ways $={ }^{a} P_{1}={ }^{10} P_{5}$

$$
=\frac{10!}{(10-5)!}=\frac{10!}{5!}=30,240 \text { ways }
$$

Hence, the DJ can play the five national songs in 30,240 different ways.
(ii) When order is not matter
$n=$ total number of national songs $=10$
$r=$ total number of selected national songs $=5$

$$
\begin{aligned}
\text { Total number of ways } & ={ }^{a} C_{r}={ }^{10} C_{5}=\frac{10!}{5!(10-5)!} \\
& =\frac{10!}{51.5!}=252 \text { ways }
\end{aligned}
$$

Hence, the DJ can play the five national songs in 252 different ways.

# EXERCISE 7.4

1. Evaluate the following:
(i) ${ }^{20} C_{50}$
(ii) ${ }^{1000} C_{0}$
(iii) ${ }^{10} C_{7}$
(iv) ${ }^{20} C_{17}$
2. (i) If ${ }^{34} C_{2}:{ }^{4} C_{2}=15: 1$, find $n$. (ii) If ${ }^{8} P_{r}=120$ and ${ }^{n} C_{r}=20$, find $r$.
3. Find the values of $n$ and $r$, when
(i) ${ }^{n} C_{r}=56,{ }^{n} P_{r}=336$
(ii) ${ }^{n-1} C_{r-1}:{ }^{n} C_{r}:{ }^{n} C_{r}=1: 3: 7$
4. Prove that (i) ${ }^{4} C_{r}+{ }^{4} C_{r-1}={ }^{n+1} C_{r}$
(ii) $r \cdot{ }^{4} C_{r}=(n-r+1){ }^{4} C_{r-1}$
5. Prove that product or $r$ consecutive intergers is divisible by $r^{1}$.
6. In how many ways can five subjects be selected out of eight subjects to select a course programme?
7. Find the number of possible arrangements of vowel letters from the English alphabet?
8. In how many ways 3 dishes of Desi foods and 2 dishes of Chinese foods be selected from 6 dishes of desi foods and 8 dishes of Chinese foods?
9. From a standard deck of 52 playing cards, there are 26 black cards and 26 red cards. How many different ways can eight cards be selected if 3 are black and the remaining 5 are red?
10. A bag contains 8 red balls and 7 green balls. Find the total number of possible ways in which five balls are selected in a way:
(i) 3 red and 2 green
(ii) 1 red and 4 green
(iii) 4 red and 1 green
(iv) all the red balls
11. How many diagonals and triangles can be formed by joining the vertices of the polygon having 15 sides.
12. Find the number of sides of a polygon if the number of its diagonals is 104.
13. How many triangles can be formed by joining 15 points, 6 of which lie on the same straight line?
14. The members of a club are 10 boys and 8 girls. In how many ways can a committee of 6 boys and 3 girls be formed?
15. How many committees of 7 members can be chosen from a group of 10 persons when each committee must include 2 particular persons?
16. In how many ways can a cricket team of 11 players be selected out of 17 players? How many of them will include a particular player?

17. There are 6 men and 8 women members of a club. How many committees of seven can be formed:
(i) with 3 women
(ii) with at most 3 women
(iii) with at least 5 women
18. There are three sections in a question paper; each section has 3 questions. A student has to solve all 5 questions, choosing at least one question from each section. In how many ways can the student make his choice?
19. Consider a cryptographic system that generates an 8 -character password. Each character in the password can be either a lowercase letter ( $a \sim f$ ) or a digit ( $0-5$ ). How many passwords can be generated if each password must contain exactly 5 lowercase letters and 3 digits:
(a) with repetition allowed
(b) without repetition
20. On Defense Day, Teacher I compiles a list of 10 distinct national songs, while Teacher II prepares a separate list of 10 different national songs (with no overlap between the two lists). The principal needs to select 3 songs from Teacher I's list, and 3 songs from Teacher II's list.
Determine the number of possible selection methods when:
(i) the order/sequence of the selected songs is important.
(ii) the order/sequence of the selected songs is not important.