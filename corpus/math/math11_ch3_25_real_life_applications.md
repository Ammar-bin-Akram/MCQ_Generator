# Chapter 3: 2.5 Real Life Applications

## Growth and Decay in Finance (Predicting Long-Term Stock Prices)

When something increases in quantity or size over time, it is called growth. For example, money in a bank account earning interest (it grows larger), a population of rabbits is increasing over months.
When something decreases in quantity or size over time, it is called decay. For example, a radioactive substance is losing its strength over years, a cup of hot coffee is cooling down over time.
Example 12 The value of a stock follows the exponential growth model $P(t)=P_{0} e^{r t}$, where $P_{0}$ is the initial stock price, $r$ is the growth rate per year and $t$ is the time in years. Suppose a stock is currently valued at Rs. 5,000 , and it is expected to grow at a rate of $5 \%$ per year.
(i) Find the value of the stock after 10 years.
(ii) After how many years will the stock double in value?

Solution (i) The formula for the exponential growth is:

$$
P(t)=P_{0} e^{r t}
$$

Given $\quad P_{0}=5000, r=0.05(5 \%$ growth rate), and $t=10$ years.

$$
P(10)=5000 e^{0.05 \times 10}=5000 e^{0.5}
$$

Using $e^{0.5} \approx 1.6487$

$$
P(10)=5000 \times 1.6487=8244
$$

So, the value of the stock after 10 years is approximately Rs. 8244
(ii) We want to find $t$ when the stock doubles, i.e., when $P(t)=2 P_{0}$. Using the equation:

$$
2 P_{0}=P_{0} e^{r t}
$$

Dividing both sides by $P_{0}$, we have $2=e^{r t}$
Taking the natural logarithm on both sides: $\ln 2=r t$

$$
\text { and } \quad t=\frac{\ln 2}{r}
$$

$$
\begin{aligned}
& =\frac{0.6931}{0.05} \\
& =13.86
\end{aligned}
$$

So, the stock will double in value i.e., approximately 14 years.

Example 13 The concentration of a pollutant in a lake, in parts per million (ppm), decays over time according to the function

$$
C(t)=\frac{100}{\sqrt{t+1}}
$$

where $t$ is the time in days since the pollutant was introduced.
(i) What is the concentration of the pollutant after 4 days?
(ii) After how many days will the concentration drop below 10 ppm ?

Solution (i) The pollutant concentration function is $C(t)=\frac{100}{\sqrt{t+1}}$, where $t$ is the time in days.
Concentration after 4 days:

$$
\begin{aligned}
C(4) & =\frac{100}{\sqrt{4+1}} \\
& =\frac{100}{\sqrt{5}} \\
& \approx 44.72 \mathrm{ppm}
\end{aligned}
$$

The concentration after 4 days is about 44.72 ppm .
(ii) When will the concentration drop below 10 ppm ? Set $C(t)=10$ :

$$
\begin{aligned}
& 10=\frac{100}{\sqrt{t+1}} \\
& \Rightarrow \sqrt{t+1}=10 \\
& \Rightarrow \quad t+1=100 \\
& \Rightarrow \quad t=99
\end{aligned}
$$

After 99 days, the concentration will drop below 10 ppm .

# EXERCISE 2.2

1. Find the point of intersection of the coordinate axes and the following linear functions graphically:
(i) $y=-5 x+10$
(ii) $y=2 x-1$
(iii) $y=\frac{1}{2} x-3$
(iv) $y=3 x+\frac{3}{2}$
2. Find the point(s) of intersection of the following functions graphically:
(i) $f(x)=2 x+5, g(x)=-x+5$
(ii) $f(x)=3 x-2, g(x)=10-x$

(iii) $f(x)=2 x-4, g(x)=3 x-1$
(iv) $f(x)=-3 x-4, g(x)=\frac{1}{2} x+3$
(v) $f(x)=x-1, g(x)=x^{2}-4 x+3$
(vi) $f(x)=3 x+4, g(x)=x^{2}+2 x-8$
(vii) $f(x)=-2 x-1, g(x)=x^{2}-4 x$
(viii) $f(x)=-x^{2}-3 x+2, g(x)=x+6$
3. Graph the following functions:
(i) $y=\sqrt{3 x}$
(ii) $y=\sqrt{x}+5$
(iii) $y=-\frac{1}{2} \sqrt{x}$
(iv) $y=-\sqrt{x+1}+2$
(v) $y=\sqrt[3]{2 x+1}$
(vi) $y=2 \sqrt[3]{x}-3$
(vii) $y=\sqrt[3]{x^{2}+x-2}$
4. A building's height over time is modeled by $\mathrm{H}(t)=100+20 t$ which is in metres and $t$ is the time in months. The height of a growing tree nearby is given by $T(t)=50+10 t+t^{2}$.
(i) At what time will the building and tree have the same height?
(ii) What will that height be?

Sketch the graphs of both functions and determine the time when the tree will overtake the height of the building.
5. A radioactive substance has a half-life ( $h$ ) of 2 years. If the initial quantity $Q_{0}$ is 200 grams and the exponential decay function is $Q(t)=Q_{0}\left(\frac{1}{2}\right)^{t}$, then find the remaining quantity after 6 years graphically.