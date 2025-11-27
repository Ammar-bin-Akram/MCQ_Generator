# Chapter 17: 11.5.1 Real World Applications

## Ferris Wheel Problems

The first Ferris wheel was invented by George W. Ferris. He built the first one for 1893 World'a Fair. A Ferris wheel is an important example of periodic motion that can be described using trigonometric functions, specifically sinusoidal functions. When we model the height of a rider on a Ferris wheel over time, we can use these functions to capture the periodic nature of the motion. The motion of Ferris wheel can be modeled by $f(t)=a+b \sin (c t+d)$ or $f(t)=a+b \cos (c t+d)$.
Example 3 A Ferris wheel with a radius of 45 feet has its lowest point located 5 feet above the ground. It completes one full revolution every 60 seconds in counter clock wise direction. Model an equation that describes the height of a rider on the Ferris wheel as a function of time $t$. How high is the rider from the ground after 40 seconds?. Also graph the model equation. Solution Since it takes 60 seconds for the Ferris wheel to complete one full revolution

(one cycle), which is the period of the Ferris wheel, that is period $=60$

$$
\frac{2 \pi}{c}=60 \quad \Rightarrow \quad c=\frac{2 \pi}{60} \quad \Rightarrow \quad c=\frac{\pi}{30}
$$

The amplitude $b$ which is equal to the radius of a ferris wheel (in this case $b=45$ ).
The vertical shift $a$ is the height of the center of the Ferris wheel above the ground. Since the lowest point is 5 feet above the ground, so $a=5+b=5+45=50$.
we can model the height of a rider using (sine or cosine), because it reflects the periodic nature of the motion. We usually choose a cosine function if the rider starts at the maximum or minimum height, or a sine function if the rider starts at the midpoint.
Since the rider starts at the lowest point and goes up, we can easily model the required equation as a negative cosine function so,
$h(t)=-b \cos (c t)+a$, where $t$ is time and $h$ is height.
Now substituting the above values we get the function $h(t)=-45 \cos \left(\frac{\pi}{30} t\right)+50$,
which is the required equation of Ferris wheel.
Next, we find the height of the rider at $t=40$ seconds.

$$
h(t)=-45 \cos \left(\frac{\pi}{30} t\right)+50
$$

For $\quad t=40$, we have

$$
h(40)=-45 \cos \left(\frac{\pi}{30}, 40\right)+50=72.5 \text { feet }
$$

Thus, height of rider after 40 second is 72.5 feet.
The graph of the model equation is shown below.
Example 4 The water level L (in feet) of a tidal river varies throughout the day. Suppose the level of the tidal river can be modeled by the equation: $L(t)=8+4 \sin \left(\frac{\pi}{6} t\right)$, where $t$ denotes the time (in hours). The water level oscillates 4 feet above and below an average level of 8 feet.
(a) Find the water level at $t=3$ hours?
(b) What is the minimum water level?

Solution (a) Given equation of water level: $L(t)=8+4 \sin \left(\frac{\pi}{6} t\right)$
To find the water level, substitute $t=3$ into the equation

$$
\begin{aligned}
& L(3)=8+4 \sin \left(\frac{\pi}{6} \cdot 3\right)=8+4 \sin \left(\frac{\pi}{2}\right) \\
& L(3)=8+4(1)=12
\end{aligned}
$$

Thus, water level at $t=3$ hours is 12 feet.
(b) Now, to find the minimum water level, we need to determine when the sine function attains its minimum value. We know that the minimum value of $\sin t=-1$, substitute the $\sin \left(\frac{\pi}{6} t\right)=-1$ into the equation

$$
L(t)=8+4 \sin \left(\frac{\pi}{6} t\right)=8+4(-1)=8-4=4
$$

Thus, minimum water level of the tidal river is 4 feet.
Example 5 From a point 100 m above the surface of a lake, the angle of elevation of a peak of a cliff is found to be $15^{\circ}$ and the angle of depression of the image of the peak is $30^{\circ}$. Find the height of the peak.
Solution Let $A$ be the top of the peak $\overline{A M}$ and $\overline{M B}$ be its image. Let $P$ be the point of observation and $L$ be the point just below $P$ (on the surface of the lake).
From $P$, draw $\overline{P Q} \perp \overline{A M}$.
Let $m \overline{P Q}=y$ metres and $m \overline{A M}=h$ metres.
$\therefore \quad m \overline{A Q}=h-m \overline{Q M}=h-m \overline{P L}=h-100$
From the figure,

$$
\tan 15^{\circ}=\frac{A Q}{P Q}=\frac{h-100}{y} \text { and } \tan 30^{\circ}=\frac{B Q}{P Q}=\frac{100+h}{y}
$$

By division, we get

$$
\frac{\tan 15^{\circ}}{\tan 30^{\circ}}=\frac{h-100}{h+100}
$$

By Componendo and Dividendo, we have

$$
\begin{aligned}
& \frac{\tan 15^{\circ}+\tan 30^{\circ}}{\tan 15^{\circ}-\tan 30^{\circ}}=\frac{h-100+h+100}{h-100-h-100}=\frac{2 h}{-200}=\frac{h}{-100} \\
& \therefore \quad h=\frac{\tan 30^{\circ}+\tan 15^{\circ}}{\tan 30^{\circ}-\tan 15^{\circ}} \times 100=[\begin{array}{c}
0.5774+0.2679 \\
0.5774-0.2679
\end{array}] \times 100 \\
& \Rightarrow h=273.1179
\end{aligned}
$$

Hence height of the peak $=273 \mathrm{~m}$. (approximately)

# EXERCISE 11.3

1. Find the maximum and minimum values of the following functions:
(i) $3-\sin 3 x$
(ii) $3+\sin 2 x$
(iii) $\frac{1}{2}+\sin (5 x+\pi)$
(iv) $\frac{3}{2}+\cos \left(x-\frac{\pi}{4}\right)$
(v) $1-3 \cos 2 x$
(vi) $1+2 \sin \left(x+\frac{\pi}{6}\right)$
(vii) $\frac{1}{10-2 \sin 3 x}$
(viii) $\frac{1}{7+3 \cos (-2 x)}$
(ix) $\frac{1}{5-3 \cos (3 x-1)}$
2. The temperature T in degrees Celsius of a certain city varies throughout the day according to the equation $T(t)=\frac{13}{2} \sin \left(\frac{\pi}{6} t-\frac{\pi}{9}\right)+15$, where $t$ is the time in hours, with $t=0$ corresponding to midnight.
(a) Find the maximum and minimum temperature during the day.
(b) Find the temperature at $t=9$ hours ( $9: 00$ a.m.).
3. A man on the top of a 100 m high light-house is in line with two ships on the same side of it, whose angles of depression from the man are $17^{\circ}$ and $19^{\circ}$ respectively. Find the distance between the ships.
4. $P$ and $Q$ are two points in line with a tree. If the distance between $P$ and $Q$ be 30 m and the angles of elevation of the top of the tree at $P$ and $Q$ are $12^{\circ}$ and $15^{\circ}$ respectively, find the height of the tree.
5. A giant Ferris wheel has a diameter of 60 feet. The lowest point of the wheel is located 6 feet above the ground. The wheel completes one full revolution every 80 seconds.

(a) Model an equation that represent the height $h(t)$ of a rider on the Ferris wheel at any given time $t$.
(b) Find the maximum height of the rider.
(c) Find the height of the rider from the ground after 35 seconds.
6. A child is playing on a swing in a playground. The height $h(t)$ of the swing seat above the ground (in metres) at time $t$ (in seconds) is modeled by the function:
$h(t)=1.5+1.2 \sin (3 \pi t)$
(a) What is the maximum height reached by the swing seat?
(b) What is the minimum height reached by the swing seat?
(c) How long does it take for the swing to complete one full-back-and-forth motion (period)?
(d) At what time(s) does the swing seat first reach a height of 2.12 metres?
7. A carnival ride consists of a vertical wheel with a diameter of 40 feet. The centre of the wheel is 28 feet above the ground. The wheel rotates at a constant speed and takes 120 seconds to make one complete revolution. Model an equation that describes the height $h(t)$ of a rider on the wheel as a function of time $t$. How high is the rider from the ground after 90 seconds? At what times will the rider be 36 feet above the ground?
8. Suppose the temperature $T$ in degrees Fahrenheit of Lahore city in a month of December throughout the day can be modeled by the equation: $T=64+8 \sin \left(\frac{\pi}{12}(t-8)\right)$, where $t$ is the time in hours. The temperature oscillates 8 degrees above and below an average temperature of 64 degrees.
(a) Find the temperature at $t=9$ hours?
(b) At what time the temperature will be maximum?
(c) Calculate the maximum temperature.
9. Suppose the population of a coastal city follows a sinusoidal pattern due to seasonal migration. The population of the city over the course of a year can be modeled by the equation: $P(t)=70000+10000 \cos \left(\frac{\pi}{6} t-\frac{\pi}{2}\right), P(t)$ is the population at time $t$ ( $t$ is the time in months, with $t=0$ corresponding to January $1^{\text {st }}$ ), where $t$ denoted the months in a year.
(a) Find the population of the city at $t=7$ months.
(b) Find the maximum population.