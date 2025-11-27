# Chapter 16: ALTERNATING CURRENT

## Learning Objectives

At the end of this chapter the students will be able to:

1. Understand and describe time period, frequency, the peak and root mean square values of an alternating current and voltage.
2. Know and use the relationship for the sinusoidal wave.
3. Understand the flow of A.C. through resistors, capacitors and inductors.
4. Understand how phase lags and leads in the circuit.
5. Apply the knowledge to calculate the reactances of capacitors and inductors.
6. Describe impedance as vector summation of resistances.
7. Know and use the formulae of A.C. power to solve the problems.
8. Understand the function of resonant circuits.
9. Appreciate the principle of metal detectors used for security checks.
10. Describe the three phase A.C. supply.
11. Become familiar with electromagnetic spectrum (ranging from radio waves to $\gamma$ rays).
12. Know the production, transmission and reception of electromagnetic waves.

We have read in the last chapter that an A.C. generator produces alternating voltage/current. Now a days most of the electrical energy is produced by A.C. generators using water power or huge steam turbines. The main reason for the world wide use of A.C. is that it can be transmitted to long distances easily and at a very low cost.

### 16.1 ALTERNATING CURRENT

Alternating current (A.C.) is that which is produced by a voltage source whose polarity keeps on reversing with time (Fig.16.1 a,b). In Fig.16.1 (a), the terminal A of the source is positive with respect to terminal $B$ and it remains so during a time interval 0 to $T / 2$. At $t=T / 2$, the terminals change their polarity. Now A becomes negative with respect to B (Fig.16.1 b). This state continues during the time interval $T / 2$ to $T$, after which terminal $A$ again becomes positive with respect to $B$ and the next cycle starts. As a result of this change of polarity, the direction of the current flow in the circuit also changes. During the time $0-T / 2$, it flows in one direction and during the interval $T / 2-T$ in opposite direction (Fig.16.1 a,b). This time interval $T$

(a)
(b)

Fig. 16.1
(a)
(b)

Fig. 16.2
during which the voltage source changes its polarity once is known as period $T$ of the alternating current or voltage. Thus an alternating quantity is associated with a frequency $f$ given by

$$
f=\frac{1}{T}
$$

The most common source of alternating voltage is an A.C. generator which has been described in the previous chapter. The output $V$ of this A.C. generator at any instant is given by

$$
V=V_{0} \sin \frac{2 \pi}{T} \times t
$$

where $T$ is period of the rotation of the coil and is equal to the period of A.C. and $\frac{2 \pi}{T}=2 \pi f=\omega$ is angular frequency of rotation of the coil. Thus $\frac{2 \pi}{T} \times t=\omega t$ is the angle $\theta$ through which the coil rotates in time $t$. Eq.16.2 shows that the value of alternating voltage $V$ is not constant. It changes with time $t$.
When $t=0, \theta=\frac{2 \pi}{T} \times t$ is 0 and $V$ is zero. When $t=T / 4$, $\theta=\frac{2 \pi}{T} \times \frac{T}{4}=\frac{\pi}{2}$ and $V$ attains its maximum value $V_{0}$ at this instant. At $t=T / 2, \theta=\pi$ and $V$ is zero. At this instant $V$ changes its polarity and becomes negative henceforth. When $t=\frac{3 T}{4}, \theta=\frac{3 \pi}{2}$ and $V=-V_{0}$ and finally at the end of the cycle when $t=T, \theta=2 \pi$ and $V=0$. The variation of $V$ with time $t$ and $\theta$ is shown in Fig. 16.2 (a,b). This graph between voltage and time is known as waveform of alternating voltage. It can be seen that it is a sine curve. Thus the output voltage of an A.C. generator varies sinusoidally with time. In our daily life we are mostly dealing with this type of voltage, so we will consider it in detail.

## 1. Instantaneous value

The value of voltage or current that exists in a circuit at any instant of time $t$ measured from some reference point is known as its instantaneous value. It can have any value between plus maximum value $+V_{0}$ and negative maximum

value $-V_{0}$ and is denoted by $V$. The entire waveform shown in Fig. 16.2 is actually a set of all the instantaneous values that exist during a period $T$. Mathematically, it is given by $V=V_{0} \sin \theta=V_{0} \sin \omega t$

$$
V=V_{0} \sin \frac{2 \pi}{T} \times t=V_{0} \sin 2 \pi f t
$$

# 2. Peak value

It is the highest value reached by the voltage or current in one cycle. For example, voltage shown in Fig. 16.2 has a peak value of $V_{0}$.

## 3. Peak to Peak Value

It is the sum of the positive and negative peak values usually written as p-p value. The p-p value of the voltage waveform shown in Fig. 16.2 is $2 V_{0}$.

## 4. Root Mean Square (rms) Value

If we connect an ordinary D.C. ammeter to measure alternating current, it would measure its value as averaged over a cycle. It can be seen in Fig. 16.2 that the average value of current and voltage over a cycle is zero, but the power delivered during a cycle is not zero because power is $I^{2} R$ and the values of $I^{2}$ are positive even for negative values of $I$. Thus the average value of $I^{2}$ is not zero and is called the mean square current. The alternating current or voltage is actually measured by square root of its mean square value known as root mean square (rms) value.
Fig. 16.3

Let us compute the average value of $V^{2}$ over a cycle. Fig.16.3 shows an alternating voltage and the way its $V^{2}$ values vary. Note that the values of $V^{2}$ are positive on the negative half cycle also. As the graph of $V^{2}$ is symmetrical about the line $\frac{1}{2} V_{0}^{2}$, so for thisfigure the mean or the average value of $V^{2}$ is $\frac{1}{2} V_{0}^{2}$. The root mean square value of $V$ is obtained bytaking

A.C. Waveform

the square root of $V_{0}^{2} / 2$ Therefore,

$$
V_{\mathrm{rms}}=\sqrt{\frac{V_{0}^{2}}{2}}=\frac{V_{0}}{\sqrt{2}}=0.7 V_{0}
$$

Similarly

$$
I_{\mathrm{rms}}=\frac{I_{0}}{\sqrt{2}}=0.7 I_{0}
$$

Most of the alternating current and voltage meters are calibrated to read rms values. When we speak of A.C. meter reading, we usually mean rms values unless stated otherwise.

Example 16.1 : An A.C. voltmeter reads 250 V . What is its peak and instantaneous values if the frequency of alternating voltage is 50 Hz ?

# rms value of alternating voltage $=V_{\text {rms }}=250 \mathrm{~V}$
Its peak value $V_{0}$ is given by the relation
or

$$
\begin{aligned}
V_{\mathrm{rms}} & =\frac{V_{0}}{\sqrt{2}} \\
V_{0} & =\sqrt{2} V_{\mathrm{rms}}=\sqrt{2} \times 250 \mathrm{~V}=353.5 \mathrm{~V}
\end{aligned}
$$

Angular frequency $\omega=2 \pi f$

$$
=2 \times \pi \times 50 \mathrm{~Hz}=100 \pi \mathrm{~Hz}
$$

Therefore, instantaneous value is given by

$$
\begin{aligned}
V & =V_{0} \sin \omega t \\
& =353.5 \sin (100 \pi t) \mathrm{V}
\end{aligned}
$$

## Phase of A.C.

We have seen that the instantaneous value of the alternating voltage is given by
or

$$
\begin{aligned}
& V=V_{0} \sin \omega t \\
& V=V_{0} \sin \theta
\end{aligned}
$$

This angle $\theta$ which specifies the instantaneous value of the alternating voltage or current is known as its phase. In Fig. 16.2 (b), we can say that the phase at the points $A, B, C, D$ and $E$ is $0, \pi / 2, \pi, 3 \pi / 2$ and $2 \pi$ respectively because these angles are the values of $\theta$ at these points. Thus each point on the A.C. waveform corresponds to a certain phase.

The phase at the positive peak is $\pi / 2=90^{\circ}$ and it is $3 \pi / 2=270^{\circ}$ at the negative peak. The points where the waveform crosses the time axis correspond to phase 0 and $\pi$.

# Phase Lag and Phase Lead

In practice, the phase difference between two alternating quantities is more important than their absolute phases. Fig. 16.4 shows two waveforms 1 and 2. The phase angles of the waveform 1 at the points $A, B, C, D$ and $E$ have been shown above the axis and those of waveform 2 below the axis. At the point $B$, the phase of 1 is $\pi / 2$ and that of 2 is 0 . Similarly it can be seen that at each point the phase of waveform 2 is less than the phase of waveform 1 by an angle of $\pi / 2$. We say that A.C. 2 is lagging behind A.C. 1 by an angle of $\pi / 2$. It means that at each instant, the phase of A.C. 2 is less than the phase of A.C. 1 by $\pi / 2$. Similarly it can be seen in Fig. 16.5, that the phase at each point of the waveform of A.C. 2 is greater than that of waveform 1 by an angle $\pi / 2$. In this case, it is said that A.C. 2 is leading the A.C. 1 by $\pi / 2$. It means that at each instant of time, the phase of A.C. 2 is greater than that of 1 by $\pi / 2$.
Phase lead and lag between two alternating quantities is conveniently shown by representing the two A.C. quantities as vectors.

## Vector Representation of an Alternating Quantity

A sinusoidally alternating voltage or current can be graphically represented by a counter clockwise rotating vector provided it satisfies the following conditions.

1. Its length on a certain scale represents the peak or rms value of the alternating quantity.
2. It is in the horizontal position at the instant when the alternating quantity is zero and is increasing positively.
3. The angular frequency of the rotating vector is the same as the angular frequency $\omega$ of the alternating quantity.
Fig. 16.6 (a) shows a sinusoidal voltage waveform leading an alternating current waveform by $\pi / 2$. The same fact has been shown vectorially in Fig.16.6 (b). Here vector OI represents the peak or rms value of the current which is taken as the reference quantity. Similarly OV represents the rms or peak value of the alternating voltage which is leading the current by $90^{\circ}$. Both vectors are supposed to be rotating in the counter
Fig. 16.4
Fig. 16.5
(a)
(b)

Fig. 16.6

clockwise direction at the angular frequency $\omega$ of the two alternating quantities. Fig. 16.6 (b) shows the position of voltage and current vector at $t=0$.

# 16.2 A.C. CIRCUITS

The basic circuit element in a D.C. circuit is a resistor $(R)$ which controls the current or voltage and the relationship between them is given by Ohm's law that is $V=I R$.

In A.C. circuits, in addition to resistor $R$, two new circuit elements namely INDUCTOR ( $L$ ), and CAPACITOR ( $C$ ) become relevant. The current and voltages in A.C. circuits are controlled by three elements $R, L$ and $C$. We would study the response of an A.C. circuit when it is excited by an alternating voltage.

### 16.3 A.C. THROUGH A RESISTOR

Fig. 16.7 (a) shows a resistor of resistance $R$ connected with an alternating voltage source.
At any time $t$ the potential difference across the terminals of the resistor is given by

$$
V=V_{0} \sin \omega t
$$

where $V_{0}$ is the peak value of the alternating voltage. The current / flowing through the circuit is given by Ohm's law

$$
I=\frac{V}{R}=\frac{V_{0}}{R} \sin \omega t
$$

or

$$
I=I_{0} \sin \omega t
$$

where $I$ is the instantaneous current and $I_{0}=\frac{V_{0}}{R}$ is the
peak value of the current. It follows from Eqs. 16.5 and 16.6 that the instantaneous values of both voltage and current are sine functions which vary with time (Fig.16.7b). This figure shows that when voltage rises, the current also rises. If the voltage falls, the current also does so - both pass their maximum and minimum values at the same instant. Thus in a purely resistive A.C. circuit, instantaneous values of voltage and current are in phase. This behaviour is shown graphically in Fig. 16.7 (b) and vectorially in Fig. 16.7 (c).
Fig. 16.7 (c) shows $\mathbf{V}$ and $\mathbf{I}$ vectors for resistance. They are drawn parallel because there is no phase difference between them. The opposition to A.C. which the circuit

presents is the resistance

$$
R=\frac{V}{I}
$$

The instantaneous power in the resistance is given by

$$
P=I^{2} R=V I=V^{2} / R
$$

$P$ is in watts, $V$ is in volts, $I$ is in amperes and $R$ is in ohms. It is very important to note that the Eq. 16.8 holds only when the current and voltage are in phase.

# 16.4 A.C. THROUGH A CAPACITOR

Alternating current can flow through a resistor, but it is not obvious that how it can flow through a capacitor. This can be demonstrated by the circuit shown in Fig.16.8. A low power bulb is connected in series with a $1 \mu \mathrm{~F}$ capacitor to supply mains through a switch. When the switch is closed, the bulb lights up showing that the current is flowing through the capacitor. Direct current cannot flow through a capacitor continuously because of the presence of an insulating medium between the plates of the capacitor. Now let us see how does A.C. flows through a capacitor. The current flows because the capacitor plates are continuously charged, discharged and charged the other way round by the alternating voltage (Fig. 16.9 a). The basic relation between the charge $q$ on a capacitor and the voltage $V$ across its plates i.e. $q=C V$ holds at every instant. If $V=V_{o}$ sin $u t$ is the applied alternating voltage, the charge on the capacitor at any instant will be given by

$$
q=C V=C V_{0} \sin \omega t
$$

Fig. 16.8
(a)
(b)

Fig. 16.9

Referring to the Fig. 16.2 (b) it can be seen that the phase at $O$ is zero and the phase at the upper maximum is $\pi / 2$. So in Fig. 16.9 (b) the phase of $V$ at $O$ is zero but the current at this point is maximum so its phase is $\pi / 2$. Thus, the current is leading the applied voltage by $90^{\circ}$ or $\pi / 2$. Now consider the points $A$ and $N$. The phase of alternating voltage at $A$ is $\pi / 2$ but the phase of current at $N$ is $\pi$. Again the current is leading the voltage by $90^{\circ}$ or $\pi / 2$. Similarly by comparing the phase at the pair of points $(B, R),(C, S)$ and $(D, T)$ it can be seen that at all these points the current leads the voltage by $90^{\circ}$ or $\pi / 2$. This is vectorially represented in Fig. 16.9 (c).
Reactance of a capacitor is a measure of the opposition offered by the capacitor to the flow of A.C. It is usually represented by $X_{\mathrm{C}}$. Its value is given by

$$
X_{\mathrm{C}}=\frac{V_{\mathrm{me}}}{I_{\mathrm{me}}}
$$

where $V_{\text {me }}$ is the rms value of the alternating voltage across the capacitor and $I_{\text {me }}$ is the rms value of current passing through the capacitor. The unit of reactance is ohm. In case of capacitor

$$
X_{\mathrm{C}}=\frac{1}{2 \pi f C}=\frac{1}{\omega C}
$$

According to Eq.16.11, a certain capacitor will have a large reactance at low frequency. So the magnitude of the opposition offered by it will be large and the current in the circuit will be small. On the other hand at high frequency, the reactance will be low and the high frequency current through the same capacitor will be large.
Example 16.2: A $100 \mu \mathrm{~F}$ capacitor is connected to an alternating voltage of 24 V and frequency 50 Hz . Calculate
(a) The reactance of the capacitor, and
(b) The current in the circuit

# (a) Reactance of the capacitor $X_{\mathrm{C}}=\frac{1}{2 \pi f C}$

$$
=\frac{1}{2 \times 3.14 \times 50 \mathrm{~s}^{-1} \times 100 \times 10^{-5} \mathrm{~F}}
$$

$$
X_{\mathrm{C}}=31.8 \frac{\mathrm{~V}}{\mathrm{Cs}}=31.8 \Omega
$$

(b) From the equation $X_{C}=\frac{V_{\text {ma }}}{I_{\text {ma }}}$
or

$$
I_{\mathrm{ma}}=\frac{V_{\mathrm{ma}}}{X_{\mathrm{C}}} \frac{24 \mathrm{~V}}{31.8 \Omega}=0.75 \mathrm{~A}
$$

# 16.5 A.C. THROUGH AN INDUCTOR

An inductor is usually in the form of a coil or a solenoid wound from a thick wire so that it has a large value of self inductance and has a negligible resistance. We have already seen how self inductance opposes changes of current. So when an alternating source of voltage is applied across an inductor, it must oppose the flow of A.C. which is continuously changing (Fig. 16.10). Let us assume that the resistance of the coil is negligible. We can simplify the theory by considering first, the current and then finding the potential difference across the inductor which will cause this current. Suppose the current is . $I=I_{0} \sin 2 \pi f t$. If $L$ is the inductance of the coil, the changing current sets up a back emf in the coil of magnitude

$$
\varepsilon_{\mathrm{L}}=L \frac{\Delta I}{\Delta t}
$$

To maintain the current, the applied voltage must be equal to the back e.m.f. The applied voltage across the coil must, therefore, be equal to

$$
V=L \frac{\Delta I}{\Delta t}
$$

Since $L$ is a constant, $V$ is proportional to $\frac{\Delta I}{\Delta t}$. Fig. 16.10 (b) shows how the current $I$ varies with time. The value of $\Delta I / \Delta t$ is given by the slope of the $I-t$ curve at the various instants of time. At $O$, the value of the slope is maximum, so the maximum value of $V$ equal to $V_{0}$ occurs at $O$ and is represented by OP (Fig. 16.10 b). From $O$ to $A$ the slope of $I-t$ graph decreases to zero so the voltage decreases form $V_{0}$ to zero at Q. From A to B, the slope of the $I-t$ graph is negative, so the voltage curve goes from $Q$ to $R$. In this way the voltage is represented by the curve PQRST corresponding to current curve OABCD. By comparing the phases of the pair of points $(\mathrm{O}, \mathrm{P}),(\mathrm{A}, \mathrm{Q}),(\mathrm{B}, \mathrm{R}),(\mathrm{C}, \mathrm{S})$ and $(\mathrm{D}, \mathrm{T})$, it can be seen that the phase of the current is always less than the phase of voltage by $90^{\circ}$ or $\pi / 2$ i.e., current lags behind the applied voltage by $90^{\circ}$ or $\pi / 2$ or the applied voltage leads the current by $90^{\circ}$ or $\pi / 2$.
Inductors are made in many sizes to perform a wide variety of functions in business and industry.

This is vectorially shown in Fig. 16.10(c) Inductive reactance is a measure of the opposition offered by the inductance coil to the flow ofA.C. It is usually denoted by $X_{L}$.

$$
X_{L}=\frac{V_{\mathrm{ms}}}{I_{\mathrm{ms}}}
$$

If $V_{\text {ms }}$ is rms value of the alternating voltage across an inductance and $I_{\mathrm{ms}}$, the rms value of the current passing through it, the value of $X_{L}$ is given by

$$
X_{L}=\frac{V_{\mathrm{ms}}}{I_{\mathrm{ms}}}=2 \pi f L=\omega L
$$

The reactance of a coil, therefore, depends upon the frequency of the A.C. and the inductance $L$. It is directly proportional to both $f$ and $L . L$ is expressed in henry, $f$ in hertz, and $X_{L}$ in ohms. It is to be noted that inductance and capacitance behave oppositely as a function of frequency. If $f$ is low $X_{L}$ is small but $X_{C}$ is large. For high $f, X_{L}$ is large but $X_{C}$ is small. The behaviour of resistance is independent of frequency.
Referring to Fig.16.10 (b), it can be seen that no power is dissipated in a pure inductor. In the first quarter of cycle both $V$ and $I$ are positive so the power is positive, which means energy is supplied to inductor. In the second quarter, $V$ is positive but / is negative. Now power is negative which implies that energy is returned by the inductor. Again in third quarter, it receives energy but returns the same amount in the fourth quarter. Thus, there is no net change of energy in a complete cycle. Since an inductor coil does not consume energy, the coil is often employed for controlling A.C. without consumption of energy. Such an inductance coil is known as choke.

### 16.6 IMPEDANCE

We already know that resistance $R$ offers opposition to the flow of current. In case of A.C. an inductance $L$ or a capacitance $C$ also offer opposition to the flow of A.C. which is measured by reactances $X_{L}$ and $X_{C}$ respectively. An A.C. circuit may consist of a resistance $R$, an inductance $L$, a capacitance $C$ or a combination of these elements. The combined effect of resistance and reactances in such a circuit is known as impedance and is denoted by $Z$.
It is measured by the ratio of the rms value of the applied voltage to the rms value of resulting A.C. Thus

$$
Z=\frac{V_{\mathrm{ms}}}{I_{\mathrm{ms}}}
$$

It is also expressed in ohms.
Example 16.3: When 10 V are applied to an A.C. circuit, the current flowing in it is 100 mA . Find its impedance.

# rms value of applied voltage $=V_{\text {mix }}=10 \mathrm{~V}$
rms value of current $=I_{\text {mix }}=100 \mathrm{~mA}=100 \times 10^{-3} \mathrm{~A}$
Impedance $Z=\frac{V_{\text {mix }}}{I_{\text {mix }}}=\frac{10 \mathrm{~V}}{100 \times 10^{-3} \mathrm{~A}}=100 \Omega$

### 16.7 R-C AND R-L SERIES CIRCUITS

Consider a series network of resistance $R$ and a capacitor $C$ excited by an alternating voltage (Fig.16.11 a). As $R$ and $C$ are in series, the same current would flow through each of them. If $I_{\text {mix }}$ is the value of current, the potential difference across the resistance $R$ would be $I_{\text {mix }} R$ and it would be in phase with current $I_{\text {mix }}$. The vector diagram of the voltage and current is shown in Fig. 16.11 (b). Taking the current as reference, the potential difference $I_{\text {mix }} R$ across the resistance is represented by a line along the current line because potential drop $I_{\text {mix }} R$ is in phase with current. The potential difference across the capacitor will be $I_{\text {mix }} X_{c}=I_{\text {mix }} / \omega C$. As this voltage lags the current by $90^{\circ}$, so the line representing the vector $I_{\text {mix }} / \omega C$ is drawn at right angles to the current line (Fig. 16.11 b).
The applied voltage $V_{\text {mix }}$ that will send the current $I$ in the circuit is obtained by the resultant of the vectors $I_{\text {mix }} R$ and $\frac{I_{\text {mix }}}{\omega C}$ i.e.,

$$
\begin{aligned}
& V_{\text {mix }}=\sqrt{\left(I_{\text {mix }} R\right)^{2}+\left(\frac{I_{\text {mix }}}{\omega C}\right)^{2}} \\
& V_{\text {mix }}=I_{\text {mix }} \sqrt{R^{2}+\left(\frac{1}{\omega C}\right)^{2}}
\end{aligned}
$$

Impedance $Z=\frac{V_{\text {mix }}}{I_{\text {mix }}}=\sqrt{R^{2}+\frac{1}{(\omega C)^{2}}}$
It can be seen in Fig. 16.11 (b) that the current and the applied voltage are not in phase. The current leads the applied voltage by an angle $\theta$ such that
(a)
(b)

Fig 16.11

$$
\theta=\tan ^{-1}\left(\frac{1}{\omega C R}\right)
$$

Eq.16.15 suggests that we can find the impedance of a series A.C. circuit by vector addition. The resistance $R$ is represented by a horizontal line in the direction of current which is taken as reference. The reactance $X_{C}=\frac{I}{\omega C}$ is shown by a line lagging the $\mathbf{R}$ - line by $90^{\circ}$ (Fig. 16.11 c). The impedance $\mathbf{Z}$ of the circuit is obtained by the vector summation of resistance and reactance. Fig.16.11 (c) is known as impedance diagram of the circuit. The angle which the line representing the impedance $\mathbf{Z}$ makes with $\mathbf{R}$ line gives the phase difference between the voltage and current. In Fig.16.11(c), the current is leading the voltage applied by an angle

$$
\theta=\tan ^{-1}\left(\frac{X_{C}}{R}\right)=\tan ^{-1}\left(\frac{1}{\omega C R}\right)
$$

Now we will calculate the impedance of a $R-L$ series circuit by drawing its impedance diagram. Fig.16.12 (a) shows an $R-L$ series circuit excited by an A.C. source of frequency $\omega$. The current is taken as reference, so it is represented by a horizontal line. Resistance $R$ is drawn along this line because the potential drop $I_{\text {mix }} R$ is in phase with current. As the potential across the inductance $V_{L}=I_{\text {mix }} X_{L}=I_{\text {mix }}(\omega L)$ leads the current by $90^{\circ}$, so the vector line of reactance $X_{L}=\omega L$ is drawn at right angle to $R$ line (Fig. 16.12 b). The impedance $Z$ of the circuit is obtained by the vector sum of $R$ and $\omega L$ lines. Thus

$$
Z=\sqrt{R^{2}+(\omega L)^{2}}
$$

The angle $\theta=\tan ^{-1} \frac{\omega L}{R}$ which $Z$ makes with $R$ line gives the phase difference between the applied voltage and current. In this case the voltage leads the current by $\theta^{\circ}$. By comparing the impedance diagrams of $R-C$ and $L-R$ circuits, it can be seen that the vector lines of reactances $X_{C}$ and $X_{L}$ are directed opposite to each other with $R$ as reference.

# 16.8 POWER IN A.C. CIRCUITS

The expression for power is $P=V_{\text {mix }} I_{\text {mix }}$. This expression is true in case of A.C. circuits, only when $V$ and $I$ are in phase as in

case of a purely resistive circuit. We have already seen that the power dissipation in a pure inductive or in a pure capacitance circuit is zero. In these cases the current lags or leads the applied voltage by $90^{\circ}$ and component of applied voltage vector V along the current vector is zero (Fig. 16.9 c and 16.10 c ). In A.C. circuit the phase difference between applied voltage $V$ and the current $I_{\text {mix }}$ is $\theta$ (Fig. 16.11 b and 16.12 b ). The component of $\mathbf{V}$ along current $I_{\text {mix }}$ is $V_{\text {mix }} \cos \theta$. Actually it is this component of voltage vector which is in phase with current. So the power dissipated in A.C. circuit

$$
P=I_{\mathrm{mix}} \times V_{\mathrm{mix}} \cos \theta
$$

The factor $\cos \theta$ is known as power factor.
Example 16.4: At what frequency will an inductor of 1.0 H have a reactance of $500 \Omega$ ?

# $$
\begin{gathered}
L=1.0 \mathrm{H} \quad, \quad X_{\mathrm{L}}=500 \Omega \\
X_{\mathrm{L}}=\omega L=2 \pi f L=500 \Omega \\
f=\frac{500 \Omega}{2 \pi L}=\frac{500 \Omega}{2 \pi \times 1.0 \mathrm{H}}=80 \mathrm{~Hz}
\end{gathered}
$$

Example 16.5: An iron core coil of 2.0 H and $50 \Omega$ is placed in series with a resistance of $450 \Omega$. An A.C. supply of 100 V , 50 Hz is connected across the circuit. Find (i) the current flowing in the coil, (ii) phase angle between the current and voltage.

## Resistance $=R=50 \Omega+450 \Omega=500 \Omega$
Inductance $=L=2.0 \mathrm{H}$
Supply voltage $=V_{\text {mix }}=100 \mathrm{~V}$
Frequency $=f=50 \mathrm{~Hz}$
The reactance $=X_{\mathrm{L}}=\omega L=2 \pi f L$

$$
=2 \times 3.14 \times 50 \mathrm{~s}^{-1} \times 2.0 \mathrm{H}=628 \Omega
$$

Impedance $=Z=\sqrt{R^{2}+(\omega L)^{2}}$

$$
=\sqrt{(500 \Omega)^{2}+(628 \Omega)^{2}}=803 \Omega
$$

Current $I_{\text {mix }}=V_{\text {mix }}^{2}=\frac{100 \mathrm{~V}}{803 \Omega}=0.01245 \mathrm{~A}=12.45 \mathrm{~mA}$
Phase difference $\theta=\tan ^{-1}\left(\frac{\omega L}{R}\right)$
A metal detector is used to locate buried metal objects

$$
=\tan ^{-1}\left(\frac{628 \Omega}{500 \Omega}\right)=51.5^{\circ}
$$

Example 16.6: A circuit consists of a capacitor of $2 \mu \mathrm{~F}$ and a resistance of $1000 \Omega$ connected in series. An alternating voltage of 12 V and frequency 50 Hz is applied. Find (i) the current in the circuit, and (ii) the average power supplied.

# Resistance $=R=1000 \Omega$
Capacitance $=C=2 \mu \mathrm{~F}=2 \times 10^{-6} \mathrm{~F}$
Frequency $=f=50 \mathrm{~Hz}$
Reactance $=X_{\mathrm{C}}=\frac{1}{2 \pi f C}$

$$
=\frac{1}{2 \times 3.14 \times 50 \mathrm{~s}^{-1} \times 2 \times 10^{-6} \mathrm{~F}}=1592 \Omega
$$

Impedance $=Z=\sqrt{R^{2}+\left(X_{\mathrm{C}}\right)^{2}}$

$$
=\sqrt{(1000 \Omega)^{2}+(1592 \Omega)^{2}}=1880 \Omega
$$

Current $=I_{\text {mix }}=\frac{V_{\text {mix }}}{Z}=\frac{12 \mathrm{~V}}{1880 \Omega}=0.0064 \mathrm{~A}=6.4 \mathrm{~mA}$
Phase Difference $\theta=\tan ^{-1} \frac{X_{\mathrm{C}}}{R}=\tan ^{-1}\left(\frac{1592 \Omega}{1000 \Omega}\right)=57.87^{\circ}$
Average power $=V_{\text {mix }} I_{\text {mix }} \cos \theta$

$$
=12 \mathrm{~V} \times 0.0064 \mathrm{~A} \times 0.532=0.04 \mathrm{~W}
$$

### 16.9 SERIES RESONANCE CIRCUIT

(a)

Consider a $R-L-C$ series circuit which is excited by an alternating voltage source whose frequency could be varied (Fig.16.13 a). The impedance diagram of the circuit is shown in Fig.16.13 (b). As explained earlier, the inductive reactance $X_{\mathrm{L}}=\omega L$ and capacitor reactance $X_{\mathrm{C}}=\frac{1}{\omega C}$ are directed opposite to each other. When the frequency of A.C. source is very small $X_{\mathrm{C}}=\frac{1}{\omega \mathrm{C}}$ is much greater than $X_{\mathrm{L}}=\omega L$. So the capacitance dominates at low frequencies and the circuit

behaves like an $R-C$ circuit. At high frequencies $X_{L}=\omega L$ is much greater than $X_{C}=\frac{1}{\omega C}$. In this case the inductance dominates and the circuit behaves like $R-L$ circuit. In between these frequencies there will be a frequency $\omega_{r}$ at which $X_{L}=X_{C}$. This condition is called resonance. Thus at resonance the inductive reactance being equal and opposite to capacitor reactance, cancel each other and the impedance diagram assumes the form (Fig.16.13 c). The value of the resonance frequency can be obtained by putting

$$
\omega_{r} L=\frac{1}{\omega_{r} C}
$$

or

$$
\omega_{r}^{2}=\frac{1}{L C} \quad \text { or } \quad \omega_{r}=\frac{1}{\sqrt{L C}}
$$

$$
f_{r}=\frac{1}{2 \pi \sqrt{L C}}
$$

The following are the properties of the series resonance.
i) The resonance frequency is given by

$$
f_{r}=\frac{1}{2 \pi \sqrt{L C}}
$$

ii) The impedance of the circuit at resonance is resistive so the current and voltage are in phase. The power factor is 1 .
iii) The impedance of the circuit is minimum at this frequency and it is equal to $R$.
iv) If the amplitude of the source voltage $V_{s}$ is constant, the current is a maximum at the resonance frequency and its value is $V_{s} / R$. The variation of current with the frequency is shown in Fig. 16.14.
v) At resonance $V_{L}$, the voltage drop across inductance and $V_{C}$ the voltage drop across capacitance may be much larger than the source voltage.

### 16.10 PARALLELRESONANCE CIRCUIT

Fig. 16.15 shows an $L-C$ parallel circuit. It is excited by an alternating source of voltage whose frequency could be varied. The inductance coil $L$ has a resistance $r$ which is negligibly small. The capacitor draws a leading current,
(b)
(c)

Fig. 16.13
Fig. 16.14

Fig. 16.15
Fig. 16.16
whereas the coil draws a lagging current. The circuit resonates at a frequency $\omega=\omega_{1}$ which makes $X_{L}=X_{C}$, so that the two branch currents are equal but opposite Hence, they cancel out with the result that the current drawn from the supply is zero. In actual practice, the current is not zero but has a minimum value due to small resistance $r$ of the coil.

Properties of parallel resonant circuits are
i) Resonance frequency is $f_{1}=\frac{1}{2 \pi \sqrt{L C}}$
ii) At the resonance frequency, the circuit impedance is maximum. It is resistive.
iii) At the resonance the current is minimum and it is in phase with the applied voltage. So the power factor is one. The variation of current with the frequency of the source is shown in Fig. 16.16.
iv) At resonance, the branch currents $I_{L}$ and $I_{C}$ may each' be larger than the source current $I_{r}$.

Example 16.7: Find the capacitance required to construct a resonance circuit of frequency 1000 kHz with an inductor of 5 mH .

# Resonance frequency $=f_{1}=1000 \mathrm{kHz}$

$$
L=5 \mathrm{mH}=5 \times 10^{-3} \mathrm{H} \quad, \quad \mathrm{C}=?
$$

Resonance frequency $=f_{1}=\frac{1}{2 \pi \sqrt{L C}}$
$C=\frac{1}{4 \pi^{2} f_{1}^{2} L}=\frac{1}{4 \times(3.14)^{2} \times\left(10^{6} \mathrm{~s}^{-1}\right)^{2} \times 5 \times 10^{-3} \mathrm{H}}=5.09 \mathrm{pF}$

### 16.11 THREE PHASE A.C. SUPPLY

We have already studied that an A.C. generator consists of a coil with a pair of slip rings. As the coil rotates an alternating voltage is generated across the slip rings. In a three phase A.C. generator, instead of one coil, there are three coils inclined at $120^{\circ}$ to each other, each connected to its own pair of slip rings. When this combination of three coils rotate in the magnetic field, each coil generates an alternating voltage across its own pair of slip rings. Thus, three alternating voltages are generated. The phase difference between these voltages is $120^{\circ}$. It means that when voltage across the first

pair of slip rings is zero, having a phase of 0 , the voltage across the second pair of slip rings would not be zero but it will have a phase of $120^{\circ}$. Similarly at this instant the voltage generated across the third pair will have a phase $240^{\circ}$. This is shown in Fig. 16.17. The machine, instead of having six terminals, two for each pair of slip rings, has only four terminals because the starting point of all the three coils has a common junction which is often earthed to the shaft of the generator and the other three ends of the coils are connected to three separate terminals on the machine. These four terminals along with the lines and coils connected to them are shown in Fig.16.18. The voltage across each of lines connected to terminals $A, B, C$ and the neutral line is 230 V . Because of $120^{\circ}$ phase shift, the voltage across any two lines is about 400 V . The main advantage of having a three phase supply is that the total load of the house or a factory is divided in three parts, so that none of the line is over loaded. If heavy load consisting of a number of air conditioners and motors etc., is supplied power from a single phase supply, its voltage is likely to drop at full load. Moreover, the three phase supply also provides 400 V which can be used to operate some special appliances requiring 400 V for their operation.

# 16.12 PRINCIPLE OF METAL DETECTORS

A coil and a capacitor are electrical components which together can produce oscillations of current. An $L-C$ circuit behaves just like an oscillating mass - spring system. In this case energy oscillates between a capacitor and an inductor. The circuit is called an electrical oscillator. Two such oscillators $A$ and $B$ are used in the operation of a common type of metal detector (Fig.16.19). In the absence of any nearby
Fig. 16.18

Fig 16.20
metal object, the inductances $L_{A}$ and $L_{B}$ are the same and hence the resonance frequency of the two circuits is also same. When the inductor $B$, called the search coil comes near a metal object, its inductance $L_{B}$ decreases and corresponding oscillator frequency increases and thus a beat note is heard in the attached speaker. Such detectors are extensively used not only for various security checks but also to locate buried metal objects.

### 16.13 CHOKE

It is a coil which consists of thick copper wire wound closely in a large number of turns over a soft iron laminated cores. This makes the inductance $L$ of the coil quite large whereas its resistance $R$ is very small. Thus it consumes extremely small power. It is used in A.C. circuits to limit current with extremely small wastage of energy as compared to a resistance or a rheostat.

### 16.14 ELECTROMAGNETIC WAVES

It is a very important class of waves which requires no medium for transmission and which rapidly propagates through vacuum.
In 1864 British physicist James Clark Maxwell formulated a set of equations known as Maxwell's equations which explained the various electromagnetic phenomena. According to these equations, a changing magnetic flux creates an electric field and a changing electric flux creates a magnetic field. Consider a region of space $A B$ as shown in Fig.16.20. Suppose a change of magnetic flux is taking place through it. This changing magnetic flux will set up a changing electric flux in the surrounding region. The creation of electric field in the region $C D$ will cause a change of electric flux through it due to which a magnetic field would be set up in the space surrounding $C D$ and so on. Thus each field generates the other and the whole package of electric and magnetic fields will move along propelling itself through space. Such moving electric and magnetic fields are known as electromagnetic waves. The electric field, magnetic field and the direction of their propagation are mutually orthogonal (Fig.16.21). It can be seen in this figure that the electromagnetic waves are periodic, hence they have a wavelength $\lambda$ which is given by the relation $c=f \lambda$ where $f$ is the frequency and $c$ is the speed of the wave. In free space the speed of electromagnetic waves is $3 \times 10^{8} \mathrm{~ms}^{-1}$.

Fig. 16.21
Depending upon the values of wavelength and frequency, the electromagnetic waves have been classified into different types of waves as radiowaves, microwaves, infrared rays, visible light etc. Fig. 16.22 shows the complete spectrum of
Fig. 16.22
The electromagnetic spectrum
Electromagnetic waves from the low radio waves to high frequency gamma rays.

# 16.15 PRINCIPLE OF GENERATION, TRANSMISSION AND RECEPTION OF ELECTROMAGNETIC WAVES

We have seen that electromagnetic waves are generated when electric or magnetic flux is changing through a certain region of space. An electric charge at rest gives rise to a Coulomb's field which does not radiate in space because no change of flux takes place in this type of field. A charge moving with constant velocity is equivalent to a steady current which generates a constant magnetic field in the

Tit-bits
Shake an electrically charged object to and fro, and you produce electromagnet waves.

Fig. 16.23

## When electrons in the transmitting antenna vibrate 94,000 times each second, they produced radio waves having frequency 94 kHz .
Fig. 16.24
surrounding space, but such a field also does not radiate out because no changes of magnetic flux are involved. Thus only chance to generate a wave of moving field is when we accelerate the electrical charges.

A radio transmitting antenna provides a good example of generating electromagnetic waves by acceleration of charges. The piece of wire along which charges are made to accelerate is known as transmitting antenna (Fig.16.23). It is charged by an alternating source of potential of frequency $f$ and time period $T$. As the charging potential alternates, the charge on the antenna also constantly reverses. For example if the top has $+q$ charges at any instant, then after time $T / 2$ the charge on it will be $-q$. Such regular reversal of charges on the antenna gives rise to an electric flux that constantly changes with frequency $f$. This changing electric flux sets up an electromagnetic wave which propagates out in space away from the antenna. The frequency with which the fields alternate is always equal to the frequency of the source generating them. These electromagnetic waves which are propagated out in space from antenna of a transmitter are known as radio waves. In free space these waves travel with the speed of light.
Suppose these waves impinge on a piece of wire (Fig.16.24). The electrons in the wire move under the action of the oscillating electric field which give rise to an alternating voltage across the wire. The frequency of this voltage is the same as that of the wave intercepting the wire. This wire receiving the wave is known as receiving antenna. As the electric field of the wave is very weak at a distance of many kilometres from the transmitter, the voltage that appears across the receiving antenna is very small. Each transmitter propagates radio waves of one particular frequency. So when a number of transmitting stations operate simultaneously, we have a number of radio waves of different frequencies in the space. Thus the voltage that appears across a receiving antenna placed in space is usually due to the radio waves of large number of frequencies. The voltage of one particular frequency can be picked up by connecting an inductance $L$ and a variable capacitor $C$ in parallel with one end of the receiving antenna (Fig.16.24).
If one adjusts the value of the capacitor so that the natural frequency of $L-C$ circuit is the same as that of the transmitting station to be picked up, the circuit will resonate

under the driving action of the antenna. Consequently, the $L-C$ circuit will build up a large response to the action of only that radio wave to which it is tuned. In your radio receiver set when you change stations you actually adjust the value of $C$.

# 16.16 MODULATION

Speech and music etc. are transmitted hundred of kilometres away by a radio transmitter. The scene in front of a television camera is also sent many kilometres away to viewers. In all these uses, the carrier of the programme is a high frequency radio wave. The information i.e., light, sound or other data is impressed on the radio wave and is carried along with it to the destination.

Modulation is the process of combining the low frequency signal with a high frequency radio wave called carrier wave. The resultant wave is called modulated carrier wave. The low frequency signal is known as modulation signal. Modulation is achieved by changing the amplitude or the frequency of the carrier wave in accordance with the modulating signal. Thus we have two types of modulations which are

1. Amplitude modulation (A.M), 2. Frequency modulation (F.M)

## Amplitude Modulation

In this type of modulation the amplitude of the carrier wave is increased or diminished as the amplitude of the superposing modulating signal increases and decreases.
Fig. 16.25 (a) represents a high frequency carrier wave of constant amplitude and frequency. Fig.16.25(b) represents a low or audio frequency signal of a sine waveform. Fig. 16.25 (c) shows the result obtained by modulating thecarrier waves with the modulating wave. The A.M. transmission frequencies range from 540 kHz to 1600 kHz .

## Frequency Modulation

In this type of modulation the frequency of the carrier wave is increased or diminished as the modulating signal amplitude increases or decreases but the carrier wave amplitude remains constant. Fig. 16.26 shows frequency modulation. The frequency of the modulated carrier wave is highest (point H ) when the signal amplitude is at its maximum positive value and is at its lowest frequency (point $L$ ) when signal amplitude has maximum negative. When the signal amplitude is zero, the carrier frequency is at its normal frequency $f_{n}$.
The F.M. transmission frequencies are much higher and ranges between 88 MHz to 108 MHz . F.M. radio waves are affected less by electrical interference than A.M. radio waves and hence, provide a higher quality transmission of sound. However, they have a shorter range than A.M. waves and are less able to travel around obstacles such as hills and large buildings.

# SUMMARY

Alternating current is that which is produced by a voltage source whose polarity keeps on reversing with time.

The time interval during which the voltage source changes its polarity.once is known as period $T$ of the alternating current or voltage.

The value of voltage or current that exists in a circuit at any instant of time measured from some reference point is known as its instantaneous value.

The highest value reached by the voltage or current in one cycle is called the peak value of the voltage or current.

The sum of positive and negative peak values is called peak to peak value and is written a\$ p-p value.

The root mean square value (rms) is the square root of the average value of $V^{2}$ or $I^{2}$.
The angle $\theta$ which specifies the instantaneous value of the alternating voltage or current, gives the phase lag or phase lead of one quantity over the other.

An inductor is usually in the form of a coil or a solenoid wound from a thick wire so that it has a large value of self inductance and has negligible resistance.

The combined effect of resistance and reactance in a circuit is known as impedance and is denoted by $Z$.

Choke is a coil which consists of thick copper wire wound closely in a large number of turns over a soft iron laminated core.

Electromagnetic waves are those which require no medium for transmission and rapidly propagate through vacuum.

Modulation is the process of combining the low frequency signal with a high frequency radio wave, called carrier waves. The resultant wave is called modulated carrier wave.

## QUESTIONS

16.1 Asinusoidal current has rms value of 10 A . What is the maximum or peak value?

16.2 Name the device that will (a) permit flow of direct current but oppose the flow of alternating current (b) permit flow of alternating current but not the direct current.
16.3 How many times per second will an incandescent lamp reach maximum brilliance when connected to a 50 Hz source?
16.4 A circuit contains an iron-cored inductor, a switch and a D.C. source arranged in series. The switch is closed and after an interval reopened. Explain why a spark jumps across the switch contacts?
16.5 How does doubling the frequency affect the reactance of (a) an inductor (b) a capacitor?
16.6 In a $R-L$ circuit, will the current lag or lead the voltage? Illustrate your answer by a vector diagram.
16.7 A choke coil placed in series with an electric lamp in an A.C. circuit causes the lamp to become dim. Why is it so? A variable capacitor added in series in this circuit may be adjusted until the lamp glows with normal brilliance. Explain, how this is possible?
16.8 Explain the conditions under which electromagnetic waves are produced from a source?
16.9 How the reception of a particular radio station is selected on your radio set?
16.10 What is meant by A.M. and F.M.?

# PROBLEMS

16.1 An alternating current is represented by the equation $I=20 \sin 100 \pi t$. Compute its frequency and the maximum and rms values of current. (Ans: $50 \mathrm{~Hz}, 20 \mathrm{~A}, 14 \mathrm{~A}$ )
16.2 A sinusoidal A.C. has a maximum value of 15 A . What are its rms values? If the time is recorded from the instant the current is zero and is becoming positive, what is the instantaneous value of the current after $1 / 300 \mathrm{~s}$, given the frequency is 50 Hz .
(Ans: $I_{\text {rms }}=10.6 \mathrm{~A}$, Instantaneous current $=13.0 \mathrm{~A}$ )
16.3 Find the value of the current and inductive reactance when A.C. voltage of 220 V at 50 Hz is passed through an inductor of 10 H . (Ans: $I_{\text {rms }}=0.07 \mathrm{~A}, X_{\mathrm{L}}=3140 \Omega$ )
16.4 A circuit has an inductance of $1 / \pi \mathrm{H}$ and resistance of $2000 \Omega$. A 50 Hz A.C. is supplied to it. Calculate the reactance and impedance offered by the circuit.
(Ans: $X_{L}=100 \Omega, Z=2002.5 \Omega$ )
16.5 An inductor of pure inductance $3 / \pi \mathrm{H}$ is connected in series with a resistance of $40 \Omega$. Find (i) the peak value of the current(ii) the rms value, and (iii) the phase difference between the current and the applied voltage $V=350 \sin (100 \pi t)$.
(Ans: (i) 1.16 A , (ii) 0.81 A , (iii) $82.4^{\circ}$ )
16.6 A $10 \mathrm{mH}, 20 \Omega$ coil is connected across 240 V and $180 / \pi \mathrm{Hz}$ source. How much power does it dissipate?
(Ans: 2778 W )

16.7 Find the value of the current flowing through a capacitance $0.5 \mu \mathrm{~F}$ when connected to a source of 150 V at 50 Hz .
(Ans: $I_{\text {rms }}=0.024 \mathrm{~A}$ )
16.8 An alternating source of emf 12 V and frequency 50 Hz is applied to a capacitor of capacitance $3 \mu \mathrm{~F}$ in series with a resistor of resistance $1 \mathrm{k} \Omega$. Calculate the phase angle.
(Ans: 46.7)
16.9 What is the resonant frequency of a circuit which includes a coil of inductance 2.5 H and a capacitance $40 \mu \mathrm{~F}$ ?
(Ans: 15.9 Hz )
16.10 An inductor of inductance $150 \mu \mathrm{H}$ is connected in parallel with a variable capacitor whose capacitance can be changed from 500 pF to 20 pF . Calculate the maximum frequency and minimum frequency for which the circuit can be tuned.
(Ans: $2.91 \mathrm{MHz}, 0.58 \mathrm{MHz}$ )