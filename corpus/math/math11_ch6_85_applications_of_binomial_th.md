# Chapter 6: 8.5 Applications of Binomial Theorem

### 8.5.1 Finding Approximate Value Using Binomial Theorem

Approximations: We have seen in the particular cases of the expansion of $(1+x)^{n}$ that the power of $x$ goes on increasing in each expansion. Since $|x|<1$, so

$$
|x|^{r}<|x| \text { for } r=2,3,4, \ldots
$$

This fact shows that terms in each expansion go on decreasing numerically if $|x|<1$. Thus, some initial terms of the binomial series are enough for determining the approximate values of binomial expansions having indices as negative integers or fractions.
Summation of infinite series: The binomial series are conveniently used for summation of infinite series. The series (whose sum is required) is compared with

$$
1+n x+\frac{n(n-1)}{2!} x^{2}+\frac{n(n-1)(n-2)}{3!} x^{3}+\ldots
$$

to find out the values of $n$ and $x$. Then the sum is calculated by putting the values of $n$ and $x$ in $(1+x)^{n}$.

Example 24 Expand $(1-2 x)^{1 / 3}$ to four terms and apply it to evaluate $(0.8)^{1 / 3}$ correct to three places of decimal.

Solution This expansion is valid only if $|2 x|<1$ or $2|x|<1$ or $|x|<\frac{1}{2}$, that is

$$
\begin{aligned}
(1-2 x)^{1 / 3} & =1+\frac{1}{3}(-2 x)+\frac{\frac{1}{3}\left(\frac{1}{3}-1\right)}{2!}(-2 x)^{2}+\frac{\frac{1}{3}\left(\frac{1}{3}-1\right)\left(\frac{1}{3}-2\right)}{3!}(-2 x)^{3} \ldots \\
& =1-\frac{2}{3} x+\frac{\frac{1}{3}\left(-\frac{2}{3}\right)}{2.1}\left(4 x^{2}\right)+\frac{\frac{1}{3}\left(-\frac{2}{3}\right)\left(-\frac{5}{3}\right)}{3.2 .1}\left(-8 x^{3}\right) \ldots \\
& =1-\frac{2}{3} x-\frac{4}{9} x^{2}-\frac{1.2 .5}{3.3 .3} \cdot \frac{1}{3.2 .1}\left(8 x^{3}\right)-\ldots \\
& =1-\frac{2}{3} x-\frac{4}{9} x^{2}-\frac{40}{81} x^{3}-\ldots
\end{aligned}
$$

Putting $x=.1$ in the above expansion we have

$$
\begin{aligned}
(1-2(0.1))^{1 / 3} & =1-\frac{2}{3}(0.1)-\frac{4}{9}(0.1)^{2}-\frac{40}{81}(0.1)^{3}-\ldots \\
& =1-\frac{0.2}{3}-\frac{0.04}{9}-\frac{0.04}{81} \\
& \approx 1-0.06666-0.00444-0.00049=1-0.07159=0.92841
\end{aligned}
$$

Thus $(.8)^{1 / 3} \approx .928$
Alternative method:

Simplify onward by yourself.
Example 25 Evaluate $3 / 30$ correct to three places of decimal.
Solution $\sqrt{30}=(30)^{1 / 3}=(27+3)^{\frac{1}{3}}$

$$
\begin{aligned}
& =\left[27\left(1+\frac{3}{27}\right)\right]^{1 / 3}=(27)^{1 / 3}\left(1+\frac{1}{9}\right)^{1 / 3} \\
& =3\left(1+\frac{1}{9}\right)^{1 / 3}
\end{aligned}
$$

$$
\begin{aligned}
& =3\left[1+\frac{1}{3} \cdot \frac{1}{9}+\frac{\left(\frac{1}{3}\right)\left(-\frac{2}{3}\right)}{2!}\left(\frac{1}{9}\right)^{2}+\frac{\frac{1}{3}\left(-\frac{2}{3}\right)\left(-\frac{5}{3}\right)}{3!}\left(\frac{1}{9}\right)^{3}+\cdots\right] \\
& =3\left[1+\frac{1}{3} \cdot \frac{1}{9}-\frac{1}{9}\left(\frac{1}{9}\right)^{2}+\frac{5}{81}\left(\frac{1}{9}\right)^{3}+\cdots\right]=3\left[1+\frac{1}{27}-\left(\frac{1}{27}\right)^{2}+\cdots\right] \\
& \approx 3[1+0.03704-0.001372]=3[1.035668]=3.107004
\end{aligned}
$$

Thus $\sqrt[3]{30} \approx 3.107$

# 8.5.2 Finding the Remainder Using Binomial Theorem

Example 26 Using binomial theorem, find the remainder when $5^{99}$ is divided by 13. Solution $5^{99}=5 \cdot 5^{98}=5 \cdot\left(5^{2}\right)^{49}=5 \cdot(25)^{49}$

$$
\begin{aligned}
& =5(26-1)^{49} \\
& =5\left[\binom{49}{0} 26^{48} 1^{0}-\binom{49}{1} 26^{48} 1^{1}+\binom{49}{2} 26^{47} 1^{2}+\ldots-\binom{49}{49} 26^{0} 1^{49}\right] \\
& =5\left[26^{49}-\binom{49}{1} 26^{48}+\binom{49}{2} 26^{47}+\ldots-1\right] \\
& =5 \cdot 26^{49}-5 \cdot\binom{49}{1} 26^{48}+5 \cdot\binom{49}{2} 26^{47}+\ldots-5 \\
& =\left[5 \cdot 26^{49}-5 \cdot\binom{49}{1} 26^{48}+5 \cdot\binom{49}{2} 26^{47}+\ldots-13\right]+8 \\
& =13 k+8, \text { where } k \text { is an integer }
\end{aligned}
$$

Hence, 8 is the remainder when $5^{99}$ is divided by 13.
Example 27 Using the binomial theorem, show that $11^{n}-10 n$ leaves a remainder 1 when divided by 100 for all positive integers $n$.

## $$
\begin{aligned}
& 11^{n}=(1+10)^{n}=\binom{n}{0} 1^{n} 10^{0}+\binom{n}{1} 1^{n-1} 10^{1}+\binom{n}{2} 1^{n-2} 10^{2}+\binom{n}{3} 1^{n-3} 10^{3}+\cdots+\binom{n}{n} 1^{0} 10^{n} \\
& 11^{n}=1+10 n+\binom{n}{2} 100+\binom{n}{3} 1000+\cdots+10^{n} \\
& 11^{n}-10 n=1+100\left[\binom{n}{2}+\binom{n}{3}(10)+\cdots+10^{n-2}\right]
\end{aligned}
$$

$11^{n}-10 n=1+100 \times$ an integer
$11^{n}-10 n=100 \times$ an integer +1
This show that $11^{n}-10 n$ leaves a remainder 1 when divided by 100 .

# 8.5.3 Finding Last Digit of a Number

Example 28 Using binomial theorem, find the last two digits of the number $11^{12}$.
Solution $(11)^{12}=(10+1)^{12}$

$$
=\binom{12}{0} 10^{12} 1^{0}+\binom{12}{1} 10^{11} 1^{1}+\binom{12}{2} 10^{10} 1^{2}+\cdots+\binom{12}{11} 10^{1} 1^{11}+\binom{12}{12} 10^{0} 1^{12}
$$

The last two digits can be found by the last two terms, because the remaining terms are the multiples of 100 and hence do not affect the last two digits

$$
\binom{12}{11} 10^{1} 1^{11}+\binom{12}{12} 10^{0} 1^{12}=120+1=121
$$

The last two digits of 121 are 2,1 .
Hence the last two digits of $11^{12}$ are 2,1 .

## Divisibility Test

Example 29 Show that $(15)^{13}+(13)^{15}$ is divisible by 14 .
Solution $(15)^{13}+(13)^{15}=(14+1)^{13}+(14-1)^{15}$

$$
\begin{aligned}
&=\left[{ }^{13} C_{0}(14)^{13}+{ }^{13} C_{1}(14)^{12}+{ }^{13} C_{2}(14)^{11}+\cdots+{ }^{13} C_{13}\right] \\
&+\left[{ }^{15} C_{0}(14)^{15}-{ }^{15} C_{1}(14)^{14}+{ }^{15} C_{2}(14)^{13}-\cdots+{ }^{15} C_{14}(14)-{ }^{15} C_{15}\right] \\
&=\left[{ }^{13} C_{0}(14)^{13}+{ }^{13} C_{1}(14)^{12}+{ }^{13} C_{2}(14)^{11}+\cdots{ }^{13} C_{12}(14)+1\right. \\
&+{ }^{15} C_{0}(14)^{15}-{ }^{15} C_{1}(14)^{14}+\cdots+{ }^{15} C_{14}(14)-1] \\
&=14\left[{ }^{13} C_{0}(14)^{12}+{ }^{13} C_{1}(14)^{11}+{ }^{13} C_{2}(14)^{10}+\cdots+{ }^{13} C_{12}\right. \\
&+{ }^{15} C_{0}(14)^{14}-{ }^{15} C_{1}(14)^{13}+\cdots+{ }^{15} C_{14}]
\end{aligned}
$$

$=14 k$, where $k$ is an integer.
Thus, $14 k$ is divisible by 14 .

## Comparing Two Large Numbers

Example 30 Which number is larger $51^{25}$ or $49^{25}+50^{25}$ ?
$$
\begin{aligned}
51^{25} & =(50+1)^{25} \\
& =\binom{25}{0}(50)^{25}(1)^{0}+\binom{25}{1}(50)^{24}(1)^{1}+\binom{25}{2}(50)^{23}(1)^{2}+\binom{25}{3}(50)^{22}(1)^{2}+\cdots \\
& =(50)^{25}+25 \cdot(50)^{24}+\frac{25 \cdot 24}{1 \cdot 2}(50)^{23}+\frac{25 \cdot 24 \cdot 23}{1 \cdot 2 \cdot 3}(50)^{22}+\cdots
\end{aligned}
$$

Similarly

$$
49^{25}=(50-1)^{25}=(50)^{25}-25 \cdot(50)^{24}+\frac{25 \cdot 24}{1 \cdot 2}(50)^{25}-\frac{25 \cdot 24 \cdot 23}{1 \cdot 2 \cdot 3}(50)^{22}+\cdots
$$

By subtracting, we get

$$
\begin{aligned}
51^{25}-49^{25} & =2\left[25 \cdot(50)^{24}+\frac{25 \cdot 24 \cdot 23}{1 \cdot 2 \cdot 3} \cdot(50)^{22}+\cdots\right. \\
& =\left[(50)^{25}+2 \cdot \frac{25 \cdot 24 \cdot 23}{1 \cdot 2 \cdot 3} \cdot(50)^{22}+\cdots\right]>50^{25} \\
\Rightarrow(51)^{25}-(49)^{25} & >50^{25} \Rightarrow(51)^{25}>(49)^{25}+50^{25}
\end{aligned}
$$

Hence, $(51)^{25}$ is greater than $49^{25}+50^{25}$.
Economic Forecasting with Compound Interest
Example 31 A bank offers a compound interest rate of $5 \%$ per year. Sumaira invests Rs. 100,000 for 3 years. How much will her investment be worth at the end of 3 years? Solution Using the compound interest formula, the future value A of the investment is given by: $A=P\left(1+\frac{r}{n}\right)^{n}$
Where, $P=100,000$ (the principal), $r=0.05$ (the interest rate), $n=1$ (compounding once per year), $t=3$ (the time in years).
Substitute the values: $A=100000(1+0.05)^{1 \times 3}=1000(1.05)^{3}$
Using the binomial expansion for $(1.05)^{3}$ :

$$
\begin{aligned}
(1+0.05)^{3} & =1+3(0.05)+3(0.05)^{2}+(0.05)^{3} \\
& =1+0.15+0.0075+0.000125 \\
& =1.157625
\end{aligned}
$$

Now calculate the future value: $A=100000 \times 1.157625=115762.5$
So, after 3 years, the investment will be worth Rs. 115762.5.

# EXERCISE 8.4

1. Using binomial theorem find the value of the following to three places of decimals:
(i) $\sqrt{99}$
(ii) $(1.03)^{\frac{1}{3}}$
(iii) $\frac{1}{1 / 252}$
(iv) $\frac{\sqrt{7}}{\sqrt{8}}$
2. Find the remainder when $8^{100}$ is divided by 7 .
3. Find the remainder when $2^{100}$ is divided by 3 .
4. Using the binomial theorem, find which number is larger:
(i) $19^{10}+20^{10}$ or $21^{10}$
(ii) $29^{15}+30^{15}$ or $31^{15}$

5. Using the binomial theorem, show that:
(i) $5^{7}+7^{5}$ is divisible by 36 .
(ii) $(17)^{15}+(13)^{7}$ is divisible by 6
(iii) $(21)^{9}+(19)^{11}$ is divisible by 20
(iv) $(31)^{4}+(29)^{6}$ is divisible by 30
(v) $(101)^{5}+(99)^{7}$ is divisible by 100
6. Using the binomial theorem, find the remainder when $3^{101}$ is divided by 8 .
7. Using the binomial theorem, find the last digit of the number (32) ${ }^{32}$.
8. Using the binomial theorem, show that $7^{n}-6 n$ leaves remainder 1 when divided by 6 for all positive integers $n$.
9. By using Binomial Theorem show that for each $n \in N, 5^{n}-1$ is divisible by 4.
10. By using Binomial Theorem show that for each $n \in N, 5^{n}-2^{n}$ is divisible by 3.
11. Show that $a^{2}+(a+2)^{2}+(a+4)^{2}+1$ is divisible by 12 , whenever " $a$ " is an odd integer.
12. A company expects its annual revenue to grow at a fixed rate of $6 \%$ per year. The revenue in year 1 is $\mathrm{R}=\mathrm{Rs} .10,000,000$. Estimate the company's revenue after 4 years using the binomial theorem for small growth rates.
13. A bank offers a compound interest rate of $10 \%$ per year. Zafar invests Rs. $2,000,000$ for 4 years. How much will his investment be worth at the end of 4 years?
14. Zaid is organizing a sports competition with 8 teams. Every team plays against every other team exactly once. How many matches will be played in total? Use Pascal's triangle to solve this.