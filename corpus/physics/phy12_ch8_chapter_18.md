# Chapter 8: Chapter 18

## ELECTRONICS

## Learning Objectives

At the end of this chapter the students will be able to:

1. Describe forward and reserve biasing of a p-n junction.
2. Understand half and full wave rectification.
3. Know the uses of light emitting diode, photo diode and photo voltaic cell.
4. Describe the operation of transistor.
5. Know current equation and solve related problems.
6. Understand the use of transistors as an amplifier and a switch.
7. Understand operational amplifier and its characteristics.
8. Know the applications of an operational amplifier as inverting and non-inverting amplifier using virtual ground concept.
9. Understand the use of an operational amplifier as a comparator e.g., night switch.
10. Understand the function of each of the following logic gates: AND, NOT, OR and NAND gates and represent their functions by means of truth tables (limited to a maximum of two inputs).
11. Describe how to combine different gates to form XOR and XNOR gates.
12. Understand combinations of logic gates to perform control functions.

The huge advances in electronics over the recent past are due to discovery and use of semi-conductors. Silicon is one of the most commonly used semi-conductors, and is the basic material from which highly sophisticated integrated circuits known as 'chips' are made. The use of chips in analogue as well as in digital electronics is described in the form of the black boxes. This chapter is based on the preliminary concepts introduced in the secondary school physics course.

### 18.1 BRIEF REVIEW OF p-n JUNCTION AND ITS CHARACTERISTICS

A p-n junction is formed when a crystal of germanium or silicon is grown in such a way that its one half is doped with a trivalent impurity and the other half with a pentavalent impurity. One of the most important building blocks of electronic devices is the p-n junction. Its n-region contains free electrons as majority charge carriers and p-region contains holes as majority charge carriers. Just after the formation of the junction, the free electrons in the n-region, because of their random motion, diffuse into the p-region. As a result of this diffusion, a region is formed around the junction in which charge carriers are not present. This region is known as depletion region (Fig. 18.1 a). In this figure, blue dots represent the free electrons and the small circles show the holes whereas the circles with + and - signs show the positive and negative ions which constitute the depletion region. Due to charge on

these ions a potential difference develops across the depletion region (Fig. 18.1 b). Its value is 0.7 V in case of silicon and 0.3 V in case of germanium. This potential difference, called potential barrier, stops further diffusion of electrons into the p-region.

# Forward Biased p-n Junction

When an external potential difference is applied across a p-n junction such that p -side is positive and n -side is negative, then this external potential difference supplies energy to free electrons in the n-region and to holes in p-region. When this energy is sufficient to overcome the potential barrier, a current of the order of a few miliamperes begins to flow across the p-n junction. In this state the p-n junction is said to be forward biased (Fig. 18.2 a). The variation of current through the junction with the bias voltage can be studied by the circuit shown in Fig. 18.2 (b). The value of current for different values of bias voltage is noted and a current-bias voltage graph is plotted. Fig. 18.3 shows the graph for a typical low power silicon diode.
As shown in Fig.18.3, if forward bias voltage is increased by $\Delta V_{n}$ the current increases by $\Delta I_{r}$. The ratio $\Delta V_{r} / \Delta I_{r}$ is known as forward resistance of the p-n junction, i.e.,

$$
r_{r}=\frac{\Delta V_{L}}{\Delta I_{T}}
$$

It is the resistance offered by the p-n junction when it is conducting. The value of $r_{r}$ is only a few ohms.

## Reverse Biased p-n Junction

When the external source of voltage is applied across a p-n junction such that its positive terminal is connected to nregion and its negative terminal to p-region, the p-n junction is said to be reverse biased (Fig. 18.4). In this situation no current flows due to the majority charge carries. However a very small current, of the order of few microamperes flows across the junction due to flow of minority charge carriers (Fig.18.4). It is known as reverse current or leakage current. The variation of reverse current with the applied bias voltage can be studied by the circuit shown in Fig.18.5. Fig. 18.6 shows the reverse characteristic for the p-n junction. It can be seen that as the reverse voltage is increased from 0 , the reverse current quickly rises to its saturation value $I_{s}$. As the reverse voltage is further increased, the reverse current
Fig.18.4: Under a reversed biased condition there is almost no current through the diode.
remains almost constant. Here the resistance offered by the diode is very high - of the order of several mega ohms.
As the reverse voltage is increased, the kinetic energy of the minority charge carriers with which they cross the depletion region also increases till it is sufficient to break a covalent bond. As the covalent bond breaks, more electron-hole pairs are created. Thus, minority charge carriers begin to multiply due to which the reverse current begin to increase till a point is reached when the junction breaks down and reverse current rises sharply (Fig.18.6). After breakdown the reverse current will rise to very high value which will damage the junction.
P-n junction is also known as a semi-conductor diode whose symbolic representation is given in Fig.18.7. The arrow head represents the $p$ - region and is known as anode. The vertical line represents the n -region and is known as cathode. The current flows in the direction of arrow when the diode is forward biased.

# 18.2 RECTIFICATION

Conversion of alternating current into direct current is called rectification. Semi-conductor diodes are extensively used for this purpose. There are two very common types of rectification.
(i) Half-wave rectification and
(ii) Full-wave rectification

## Half-Wave Rectification

A half-wave rectification is shown in Fig. 18.8 where an alternating voltage of period $T$ called input voltage is applied to a diode $D$ which is connected in series with a load resistance $R$. In this method only one half of alternating current cycle is converted into direct current.
During the positive half cycle of the input alternating voltage i.e., during the interval $0 \rightarrow T / 2$, the diode $D$ is forward biased, so it offers a very low resistance and current flows through $R$. The flow of current through $R$ causes a potential drop across it which varies in accordance with the alternating input (Fig. 18.8 c).
During the negative half cycle i.e., during the period $T / 2 \rightarrow T$, the diode is reverse biased. Now it offers a very high resistance, so practically no current flows through $R$ and potential drop across it is almost zero (Fig. 18.8 c). The same events repeat during the next cycle and so on. The current through $R$ flows in only one direction which means it is a direct current. However, this current flows in pulses (Fig. 18.8 c). The

voltage which appears across load resistance $R$ is known as output voltage.

# Full-Wave Rectification

We have seen that in a half-wave rectification, only one half of the alternating input voltage is used to send a unidirectional current through a resistance. However both halves of the input voltage cycle can be utilized using full-wave rectification. Its circuit consists of four diodes connected in a bridge type arrangement (Fig.18.9). To understand the operation of the circuit, recall that a diode conducts only when it is forward biased. During the positive half cycle, i.e., during the time $0 \rightarrow T / 2$, the terminal $A$ of the bridge is positive with respect to its other terminal $B$. Now the diodes $D_{1}$ and $D_{2}$, become forward biased and conduct. A current flows through the circuit in the direction shown by arrows in Fig. 18.9 (a). During the negative half cycle, i.e., during the time interval $T / 2 \rightarrow T$, terminal $A$ is negative and $B$ is positive. Now the diodes $D_{2}$ and $D_{2}$ conduct and current flows through the circuit in the path shown by arrows in Fig. 18.9 (b). By comparing Figs. 18.9 (a) and 18.9 (b), it can be seen that direction of current flow through the load resistance $R$ is the same in both the halves of the cycle. Thus both halves of the alternating input voltage send a unidirectional current through $R$. The input and output voltages are shown in Fig. 18.10. However the output voltage is not smooth but pulsating. It can be made smooth by using a circuit known as filter.

### 18.3 SPECIALLY DESIGNED p-n JUNCTIONS

In addition to the use of semi-conductor diode as rectifier, many types of p-n junctions have been developed for special purposes. Three most commonly used such diodes are
(i) Light emitting diode
(ii) Photo diode
(iii) Photo voltaic cell

## Light Emitting Diode

Light emitting diodes (LED) are made from special semi-conductors such as gallium arsenide and gallium arsenide phosphide in which the potential barrier between $p$ and $n$ sides is such that when an electron combines with a hole during forward bias conduction, a photon of visible light is emitted. These diodes are commonly used as small light
Fig. 18.9
Fig. 18.10

A seven segment display 0123456789

Fig. 18.11
sources. A specially formed array of seven LED's is used for displaying digits etc., in electronic appliances (Fig. 18.11).

## Photo Diode

Photo diode is used for the detection of light. It is operated in the reverse biased condition (Fig. 18.12 a). A photo diode symbol is shown in Fig. 18.12 (b). When no light is incident
(a)
(b)
on the junction, the reverse current $I$ is almost negligible but when its p-n junction is exposed to light, the reverse current increases with the intensity of light (Fig.18.12 c).
A photo diode can turn its current ON and OFF in nano-seconds. Hence it is one of the fastest photo detection devices. Applications of photo diode include
i. Detection of both visible and invisible radiations
ii. Automatic switching
iii. Logic circuits
iv. Optical communication equipment etc.

## Photo-Voltaic Cell

It consists of a thick n-type region covered by a thin p-type layer. When such a p-n junction having no external bias (Fig.18.13), is exposed to light, absorbed photons generate electron-hole pairs. It results into an increase percentage of minority charge carriers in both the p and n-regions and when they diffuse close to the junction, the electric field due to junction potential barrier sweeps them across the junction. It causes a current flow through the external circuit $R$. The current is proportional to intensity of light.

# 18.4 TRANSISTORS

A transistor consists of a single crystal of germanium or silicon which is grown in such a way that it has three regions (Figs. 18.14 \& 18.15).
In Fig. 18.14 the central region is $p$ type which is sandwiched between two $n$ type regions. It is known as $n-p-n$ transistor. In Fig.18.15, the $n$ type central region is sandwiched between two $p$ type regions. It forms a p-n-p transistor. The central region is known as base and the other two regions are called emitter and collector. Usually the base is very thin, of the order of $10^{-5} \mathrm{~m}$. The emitter and collector have greater concentration of impurity. The collector is comparatively larger than the emitter. The emitter has greater concentration of impurity as compared to the collector.

It can be seen in Figs. 18.14 and 18.15 that a transistor is a combination of two back to back p-n junctions: emitter-base junction and collector-base junction.
For normal operation of the transistor, batteries $V_{B B}$ and $V_{c c}$ are connected in such a way that its emitter-base junction is forward biased and its collector base junction is reverse biased. $V_{c c}$ is of much higher value than $V_{B B}$. Fig. 18.16 shows the biasing arrangement for $n-p-n$ transistor when the transistor has been represented by its symbolic form. Fig. 18.17 shows the same for a p-n-p transistor.
Fig. 18.14
Fig. 18.15
Fig. 18.15

Fig. 18.17
It may be noted that polarities of the biasing batteries $V_{B B}$ and $V_{c c}$ are opposite in the two types of the transistors. In actual practice, it is the n-p-n transistor that is generally used. So we will discuss n-p-n transistors only.

# Current Flow in a n-p-n Transistor

Fig. 18.18 (a) shows a n-p-n transistor at the instant when the biasing voltage is applied. Electrons in the emitter, shown by black dots, have not yet entered the base region. After the application of the biasing voltage, emitter base junction is forward biased, so emitter injects a large number of electrons in base region (Fig. 18.18 b). These free electrons in the base can flow in either of two directions. They can either flow out of the base to the positive terminal of $\mathrm{V}_{\mathrm{cc}}$ or they can be attracted towards the collector because of battery $\mathrm{V}_{\mathrm{cc}}$. Since the base is extremely thin, very few electrons manage to recombine with holes and escape out of the base. Almost all of the free electrons injected from the emitter into the base are attracted by the collector due to the large positive potential $\mathrm{V}_{\mathrm{cc}}$ (Fig. 18.18 c ). Thus, in a normally biased transistor due to above mentioned flow of electrons, we can say, that an electronic current $I_{E}$, flows from the emitter into the base. A very small part of it, current $I_{B}$, flows out of the base, the rest of it $I_{c}$ flows out of the collector (Fig. 18.19).
Fig. 18.19

The flow of conventional current is shown in Fig. 18.20. In future we will use conventional current only. From the figure, it can be seen that

$$
I_{E}=I_{C}+I_{B}
$$

As very few electrons flow out of base, so $I_{B}$ is very small as compared to $I_{C}$.
It is also found that for a given transistor the ratio of collector current $I_{C}$ to base current $I_{B}$ is nearly constant i.e.,

$$
\beta=\frac{I_{C}}{I_{B}}
$$

The ratio $\beta$ is called current gain of transistor. Its value is quite large - of the order of hundreds. Eqs. 18.2 and 18.3 are

fundamental equations of all transistors.
Example 18.1: In a certain circuit, the transistor has a collector current of 10 mA and a base current of $40 \mu \mathrm{~A}$. What is the current gain of the transistor?

# $$
\beta=\frac{I_{\mathrm{C}}}{I_{\mathrm{B}}}=\frac{10 \times 10^{-3} \mathrm{~A}}{40 \times 10^{-6} \mathrm{~A}}=250
$$

### 18.5 TRANSISTOR AS AN AMPLIFIER

In majority of electronic circuits, transistors are basically used as amplifiers. An amplifier is thus the building block of every complex electronic circuit. It is for this reason that study of transistor amplifier is important.

The circuit in Fig. 18.21 is a transistor voltage amplifier. The battery $\mathrm{V}_{\mathrm{se}}$ forward biases the base-emitter junction and $\mathrm{V}_{\mathrm{cc}}$ reverse biases the collector-base junction. $\mathrm{V}_{\mathrm{se}}$ and $\mathrm{V}_{\mathrm{ce}}$ are the input and output voltages respectively. The base current is $I_{\mathrm{B}}=\mathrm{V}_{\mathrm{se}} / \mathrm{r}_{\mathrm{w}}$ where $\mathrm{r}_{\mathrm{w}}$ is base emitter resistance of the transistor. The transistor amplifies it $\beta$ times. So

$$
I_{\mathrm{c}}=\beta I_{\mathrm{B}}=\beta \mathrm{V}_{\mathrm{se}} / \mathrm{r}_{\mathrm{w}}
$$

The output voltage $V_{\mathrm{o}}=\mathrm{V}_{\mathrm{ce}}$ is determined by applying KVL equation in the output loop which gives
$V_{c c}=I_{c} R_{c}+V_{c e} \quad$ or $\quad V_{c e}=V_{c c}-I_{c} R_{c}$
Substituting the value of $I_{c}$ and replacing $V_{c e}$ by $V_{0}$

$$
V_{0}=V_{c c}-\beta V_{s e} R_{c} / r_{w}
$$

When small signal voltage $\Delta V_{o}$ is applied at the input terminal $B$, the input voltage changes from $V_{s e}$ to $V_{s e}+\Delta V_{o}$. This causes a little change in base current from $I_{0}$ to $\left(I_{0}+\Delta I_{0}\right)$ due to which the collector current changes from $I_{c}$ to $\left(I_{c}+\Delta I_{c}\right)$. As the collector current changes, the voltage drop across $R_{c}$ i.e. $\left(I_{c} R_{c}\right)$ also changes due to which the output voltage $V_{0}$ changes by $\Delta V_{0}$. Substituting the changed values in Eq. 18.4(a)

$$
V_{0}+\Delta V_{0}=V_{c c}-\beta\left(V_{s e}+\Delta V_{o}\right) R_{c} / r_{w}
$$

Subtracting Eq. 18.4(a) from Eq. 18.4(b)

$$
\Delta V_{0}=-\beta \Delta V_{0} R_{c} / r_{w}
$$

Fig. 18.21

## Various shapes of transistors.

Therefore the gain of the amplifier $A=\Delta V_{n} / \Delta V_{m}=\beta R_{c} / r_{m}$ The value of the factor $\beta R_{c} / r_{m}$ is of the order of hundreds, so the input voltage is amplified. The negative sign shows that there is a phase shift of $180^{\circ}$ between the input and the output signals.

# 18.6 TRANSISTOR AS A SWITCH

Fig. 18.22 (a) shows the circuit in which a transistor is used as a switch. The collectors $C$ and emitter $E$ behave as the terminals of the switch. The circuit in which the current is to be tuned OFF and ON, is connected across these terminals. The base B and emitter E act as control terminals which decide the state of the switch.
In order to turn on the switch, a potential $V_{B}$ is applied between control terminals B-E (Fig. 18.22 a). This injects a large current $I_{B}$ into the base circuit due to which a very heavy current $I_{C}$ begins to flow in the CE circuit. This large value of collector current is possible only when the resistance between $C$ and $E$ drops down to such a small value that the potential drop across CE is nearly 0.1 volt. In Fig. 18.22 (a) emitter is at ground, so we can assume that collector is also at ground and collector emitter circuit of Fig. 18.22 (a) can be drawn as shown in Fig. 18.22 (b). CE switch is closed and the bulb glows due to flow of large collector current. To turn the switch OFF the base current $I_{B}$ is set zero by opening the base circuit (Fig. 18.22 c). As $I_{c}=\beta I_{B}$, so $I_{c}$ becomes zero and C-E circuit becomes open (Fig. 18.22 d). Now the resistance between $C$ and $E$ becomes nearly infinity which opens the CE switch.
An electronic computer is basically a vast arrangement of electronic switches which are made from transistors.

### 18.7 OPERATIONAL AMPLIFIER

As stated earlier, amplifier is an important electronic circuit that is used in almost every electronic instrument. So instead of making amplifier circuit by discrete components, the whole amplifier is integrated on a small silicon chip and enclosed in a capsule. Pins connected with working terminals such as input, output and power supply project outside the capsule (Fig.18.23 a). The enclosed circuit of the amplifier is used by making requisite connections with these pins. Such an

integrated amplifier is known as operational amplifier (op-amp), as it is some times used to perform mathematical operations electronically.
The op-amp is usually represented by its symbol shown in Fig. 18.23 (b). It has two input terminals. One is known as inverting input (-) and the other non-inventing input (+). A signal that is applied at the inverting (-) input, appears after amplification, at the output terminal with a phase shift of $180^{\circ}$ (Fig. 18.24 a). It can be seen that the signal is inverted as it appears at the output. This is why this terminal is known as inverting. If the signal is applied at non-inverting input ( + ), it is amplified at the output without any change of phase (Fig. 18.24 b).
Fig. 18.24
Fig. 18.24
Fig. 18.23
Fig. 18.25

# Characteristics of op-amp

An op-amp has a large number of characteristic parameters. We will discuss only three of them.

## (i) Input Resistance

It is the resistance between the $(+)$ and $(-)$ inputs of the amplifier (Fig. 18.25). Its value is very high - of the order of several mega ohms. Due to high value of the input resistance $R_{n}$, practically no current flows between the two input terminals. It is a very important feature of op-amps.
Fig. 18.26

## (ii) Output Resistance

It is the resistance between the output terminal and ground (Fig. 18.26). Its value is only a few ohms.

## (iii) Open Loop Gain

It is the ratio of output voltage $V_{v}$ to the voltage difference between non-inverting and inverting inputs when there is no external connection between the output and the inputs (Fig. 18.27) i.e.,

$$
A_{\mathrm{OL}}=\frac{V_{n}}{V_{v}-V_{-}}=\frac{V_{n}}{V_{i}}
$$

Fig. 18.27

Fig. 18.28

The open loop gain of the amplifier is very high. It is of the order of $10^{5}$.

# 18.8 OP-AMP AS INVERTING AMPLIFIER

Fig. 18.28 shows the circuit of an op-amp when used as an inverting amplifier. The input signal $V_{i n}$ which is to be amplified, is applied at inverting terminal (-) through a resistance $R_{1}, V_{0}$ is its output. The non-inverting terminal ( + ) is grounded, i.e., its potential is zero. We know that $A_{0 k}$ is $V_{0}$ very high, of the order of $10^{5}$. As $V_{0}$ may have any value between $+V_{c c}(+12 \mathrm{~V})$ and $-V_{c c}(-12 \mathrm{~V})$ so according to Eq.18.5, for finite ( $\pm 12 \mathrm{~V}$ ) value of $V_{0}, V_{n}-V_{n} \approx 0$ or $V_{n} \approx V_{n}$. Since $V_{n}$ is at ground so $V_{1}$ is virtually at ground potential i.e., $V_{n} \approx 0$. Referring to Fig. 18.28,

Current through $\quad R_{1}=I_{1}=\frac{V_{0}-V_{1}}{R_{1}}=\frac{V_{0}-0}{R_{1}}=\frac{V_{0}}{R_{1}}$
Current through $\quad R_{2}=I_{2}=\frac{V_{-}-V_{0}}{R_{2}}=\frac{0-V_{0}}{R_{2}}=-\frac{V_{0}}{R_{2}}$
As practically no current flows between $(-)$ and $(+)$ terminals, so according to Kirchhoff's current rule $\quad I_{1}=I_{2}$ or

$$
\frac{V_{0}}{R_{1}}=-\frac{V_{0}}{R_{2}} \quad \text { or } \quad \frac{V_{0}}{V_{0}}=-\frac{R_{2}}{R_{1}}
$$

As $V_{0} / V_{m}$ is defined as gain $G$ of the inverting amplifier, so

$$
G=-\frac{R_{2}}{R_{1}}
$$

The negative sign indicates that the output signal is $180^{\circ}$ out of phase with respect to input signal. It is interesting to note that the closed loop gain depends upon the two externally connected resistances $R_{1}$ and $R_{2}$. The gain is independent of what is happening inside the amplifier.
If $R_{1}=10 \mathrm{k} \Omega$ and $R_{2}=100 \mathrm{k} \Omega$, the gain of the amplifier is

$$
G=\frac{V_{0}}{V_{0}}=\frac{-R_{2}}{R_{1}}=\frac{-100 \Omega}{10 \mathrm{k} \Omega}=-10
$$

### 18.9 OP-AMP AS NON-INVERTING AMPLIFIER

The circuit diagram of op-amp as non-inverting amplified is shown in Fig. 18.29. In this case the input signal $V_{i n}$ is applied at the non-inverting terminal ( + ). As explained earlier, due to high open loop gain of amplifier, the inverting (-) and non

inverting ( + ) inputs are virtually at the same potential. That is,

$$
V_{+}=V_{+}=V_{\text {in }}
$$

Also, from Fig.18.29,

$$
\begin{aligned}
& \text { Current through } R_{1}=I_{1}=\frac{0-V_{-}}{R_{1}}=\frac{0-V_{\text {in }}}{R_{1}}=\frac{-V_{\text {in }}}{R_{1}} \\
& \text { Current through } R_{2}=I_{2}=\frac{V_{-}-V_{0}}{R_{2}}=\frac{V_{\text {in }}-V_{0}}{R_{2}}
\end{aligned}
$$

As practically no current flows between (-) and (+) terminals, so by Kirchhoff's current rule $I_{1}=I_{2}$

Hence

$$
\frac{-V_{\mathrm{in}}}{R_{1}}=\frac{V_{\mathrm{in}}-V_{0}}{R_{2}}
$$

or

$$
V_{\mathrm{in}}\left(\frac{1}{R_{1}}+\frac{1}{R_{2}}\right)=\frac{V_{\mathrm{in}}}{R_{2}}
$$

or

$$
\text { Gain }=\frac{V_{\mathrm{in}}}{V_{\mathrm{in}}}=1+\frac{R_{2}}{R_{1}}
$$

Again the gain of the amplifier is independent of the internal structure of the op-amp. It just depends upon the two externally connected resistances $R_{1}$ and $R_{2}$. The positive sign of gain indicates that the input and out put signals are in phase.
Example 18.2: Find the gain of the circuit as shown in Fig.18.30.

## As the input signal $V_{\text {in }}$ is connected to non-inverting input $(+)$, so the op-amp acts as a non-inverting amplifier. Comparing it with the circuit of non-inverting amplifier as shown in Fig. 18.29, we have

$$
\begin{aligned}
R_{1} & =\text { infinity } \\
\therefore \quad \text { Gain } & =1+\frac{R_{2}}{R_{1}}=1
\end{aligned}
$$

and $\quad R_{2}=0$

$$
\therefore \quad \text { Gain }=1+\frac{R_{2}}{R_{1}}=1
$$

### 18.10 OP-AMP AS A COMPARATOR

Op-amp usually requires two power supplies of equal voltage but of opposite polarity. Most op-amp operate with $V_{\mathrm{CC}}= \pm 12 \mathrm{~V}$ supply (Fig. 18.31).

An op amplifier - The circuits in the black box.
Fig. 18.30
Fig. 18.31

Integrated circuit (IC) chips are manufactured on wafers of semiconductor material.
Fig. 18.33

As the open loop gain of the op-amp is very high ( $10^{6}$ ), even a very small potential difference between the inverting and noninverting inputs is amplified to such a large extent that the amplifier gets saturated, i.e., its output either becomes equal to $+V_{\text {cc }}$ or $-V_{\text {cc }}$. This feature of op-amp is used to compare two voltages. Fig. 18.32 shows the circuit of an op-amp used as
Fig. 18.32
comparator. $V_{n}$ is reference voltage which is connected with $(+)$ terminal and $V$ is the voltage which is to be compared with the reference $V_{n}$. It is connected with (-) terminal.
When $\quad V_{1}>V_{1}$ or $V>V_{n}$, then $V_{v}=-V_{c c}$
and if $\quad V_{1}<V_{v}$ or $V<V_{n}$, then $V_{v}=+V_{c c}$

### 18.11 COMPARATOR AS A NIGHT SWITCH

Suppose it is required that when intensity of light falls below a certain level, the street light is automatically switched on. This can be accomplished by using op-amp as a comparator. In Fig. 18.33 resistances $R_{1}$ and $R_{2}$ form a potential divider. The potential drop across $R_{2}$ provides the reference voltage $V_{n}$ to the $(+)$ input of the op-amp. Thus

$$
V_{n}=\frac{R_{2}}{R_{1}+R_{2}} \times V_{c c}
$$

LDR is a light dependent resistance. The value of its resistance $R_{1}$ depends upon the intensity of light falling upon it. $R_{1}$ and $R_{2}$ form another potential divider. The potential drop across $R_{3}$ is $V^{\prime}$ which is given by

$$
V^{\prime}=\frac{R_{3}}{R_{1}+R_{3}} \times V_{c c}
$$

$V^{\prime}$ provides the voltage to $(-)$ input of the op-amp. $V^{\prime}$ will not be

a constant voltage but it will vary with the intensity of light. During day time, when light is falling upon LDR, $R_{\mathrm{L}}$ is small. According to Eq.18.9, $V^{\prime}$ will be large such that $V^{\prime}>V_{n}$ so that $V_{n}=-V_{c c}$. The output of the op is connected with a relay system which energizes only when $V_{n}=+V_{c c}$ and then it turns on the street lights. Thus when $V_{n}=-V_{c c}$, the light will not be switched ON.

As it gets darker, $R_{\mathrm{L}}$ becomes larger and $V^{\prime}$ decreases. When $V^{\prime}$ becomes just less than $V_{n}$, the output of op-amp switches to $+V_{c c}$ which energizes the relay system and the street lights are turned ON.

# 18.12 DIGITAL SYSTEMS

A digital system deals with quantities or variables which have only two discrete values or states. Following are the examples of such quantities.
(i) A switch can be either open or closed.
(ii) The answer of a question can be either yes or no.
(iii) A certain statement can be either true or false.
(iv) A bulb can be either off or on.

Various designations are used to represent the two quantized states of such quantities. The most common of these are listed in Table 18.1.

| Table 18.1 |  |  |  |  |  |  |
| :-- | :--: | :--: | :--: | :--: | :--: | :--: |
|  | 1 | 2 | 3 | 4 | 5 | 6 |
| One of the states | True | High | 1 | Yes | On | Closed |
| The other state | False | Low | 0 | No | Off | Open |

Mathematical manipulation of these quantities can be best carried if they are represented by binary digits 1 and 0 . When we are dealing with voltages, designation No. 2 is also a convenient representation.
In describing functions of digital systems a closed switch will be shown as 1 and open switch will be shown as 0 . Similarly, a lighted bulb will be described as 1 and an off bulb will be described as 0 .
Just as we require two basic mathematical operations, i.e., addition and subtraction for the mathematical manipulation

Fig. 18.34
Fig. 18.35

| Table 18.2 |  |  |
| :--: | :--: | :--: |
| A | B | Output |
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

AND gate
Fig. 18.36
of ordinary quantities which can possess all continuous values, we require a special algebra, known as Boolean algebra for the manipulation of the quantities which have values 1 and 0 , now designated as Boolean variables. Boolean algebra is based upon three basic operations namely (i) AND operation, (ii) OR operation and (iii) NOT operation. You have already read about these operations. Here we would study about logic gates which implement these operations.

# 18.13 FUNDAMENTAL LOGIC GATES

The electronic circuits which implement the various logic operations are known as logic gates. In these gates the high and low states, i.e., 1 and 0 states are simulated by certain voltage levels. Ideally one particular voltage level represents a high (1) and another voltage level represents a low (0). In practical digital circuits, however a 1 or high can be any voltage between a specified minimum value and a specified maximum value. Likewise 0 or low can be any voltage between a specified minimum and a specified maximum. Fig. 18.34 shows the range 1 and 0 levels for a certain type of digital gates. Thus if voltage of 3.5 V is applied to a gate, it will accept it as high or 1 . If a voltage of 0.5 V is applied, the gate will recognize it as 0 or low.

## OR Gate

OR gate as symbolically represented in Fig.18.35, implements the logic of OR operation. It has two or more inputs and a single output $X$. The output has a value 1 when at least one of its inputs $A$ and $B$ is at 1 . Thus $X$ will be zero only when both the inputs are 0 . Thus it implements the truth table of OR operation (Table 18.2). The mathematical notation for OR operation is

$$
X=A+B
$$

## AND Gate

The AND gate shown in Fig. 18.36 has two or more inputs and a single output. It is designed such that it implements the truth table of AND operation, i.e., its output $X$ is 1 only when both of its inputs $A$ and $B$ are at 1 and for all other combinations of the values of $A$ and $B, X$ is zero (Table 18.3). The mathematical notation for AND operation is

$$
X=A \cdot B
$$

# NOT Gate

It performs the operation of inversion or complementation. That is why it is also known as inverter. It changes a logic level to its opposite level, i.e., it changes 1 to 0 and 0 to 1 . The symbolic representation of NOT gate is shown in Fig. 18.37. Whenever a bar is placed on any variable, it shows that the value of the variable has been inverted. For example $\overline{1}=0$ and $\overline{0}=1$. The "bubble" (o) in Fig. 18.37 indicates operation of inversion. Its truth table is given in Table 18.4. The mathematical notation for NOT operation is $\quad X=\bar{A}$

### 18.14 OTHER LOGIC GATES

## NOR Gate

In NOR gate the output of OR gate is inverted. Its symbol is shown in Fig. 18.38 and its truth table is given in Table 18.5. The mathematical notation for NOR operation is

$$
X=\bar{A}+\bar{B}
$$

## NAND Gate

In NAND gate the output of an AND gate is inverted. Its symbol is shown in Fig. 18.39. The bubble in this figure shows that the output of AND gate is inverted. The truth table implemented by it is shown in Table 18.6. The mathematical notation for NAND operation is

$$
X=\bar{A} \cdot \bar{B}
$$

## Exclusive OR Gate(XOR)

Consider a Boolean function $X$ of two variables $A$ and $B$ such that

$$
X=A \bar{B}+\bar{A} B
$$

The first term of the function $X$ is obtained by ANDing the variable $A$ with NOT of $B$. The second term is NOT of $A$ ANDed with B. The function $X$ is obtained by ORing these two terms. It can be constructed by combining AND, OR and NOT gates according to the scheme shown in Fig. 18.40(a). The
Fig. 18.40 (a)
Making an XOR gate
Fig. 18.37

| Table 18.4 |  |  |
| :--: | :--: | :--: |
| A | Output |  |
| 0 | 1 |  |
| 1 | 0 |  |

Fig. 18.38

| Table 18.5 |  |  |
| :--: | :--: | :--: |
| A | B | Output |
| 0 | 0 | 1 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 0 |

| Input A |  | Output |
| :--: | :--: | :--: |
| Input B |  |  |
|  |  |  |

Fig. 18.40 (b)
| Table 18.8 |  |  |
| :--: | :--: | :--: |
| A | B | Output |
| 0 | 0 | 1 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

value of this function can be obtained by drawing the truth table (Table 18.7) which gives the value of $X$ for all the values of the variables $A$ and $B$. The value of $X$ is 0 when the two inputs have the same values and it is 1 when the inputs have different values. It can be verified that the circuit of Fig. 18.40 (a) implements this truth table. The symbol of XOR gate is shown in Fig. 18.40(b).

## Exclusive-NOR gate (XNOR)

The exclusive NOR gate is obtained by inverting the output of a XOR gate. Its symbol is shown in Fig. 18.41. The bubble shown at the output in this figure shows that the output of XOR gate has been inverted. So its Boolean expression is given by

$$
X=\overrightarrow{A B}+\overrightarrow{A B}
$$

The truth table of XNOR gate is given in the Table 18.8. Its output is 1 when its two inputs are identical and 0 when the two inputs are different. Like XOR gate, it is also constructed by a combination of NOT, AND and NOR gates by the scheme shown in Fig.18.42.
Fig. 18.42

### 18.15 APPLICATIONS OF GATES IN CONTROL SYSTEMS

Gates are widely used in control systems. They control the function of the system by monitoring some physical parameter such as temperature, pressure or some other physical quantity of the system. As gates operate with electrical voltages only, so some devices are required which can convert various physical quantities into electric voltage.

These devices are known as sensors. For example, in the example of night switch, Light Dependent Resistance (LDR) is a sensor for light because it can convert changes in the intensity of light into electric voltage. A thermister is a sensor for temperature. A microphone is a sound sensor. Similarly there are level sensors which give an electrical signal when the level of liquid in a vessel attains a certain limit. One such application is described here. For example sensors are used to monitor the pressure and temperature of a chemical solution stored in a vat. The circuitry for each sensor is such that it produces a HIGH, i.e., 1 when either the temperature or pressure exceeds a specified value. A circuit is to be designed which will ring an alarm when either the temperature or pressure or both cross the maximum specified limit. The alarm requires a LOW(0) voltage for its activation.
The block diagram of the problem is shown in Fig. 18.43 in which $C$ is the circuit to be designed. Its inputs $A$ and $B$ are fed by the temperature and pressure sensors $T$ and $P$ fitted into the vat. Whenever output of the circuit $C$ is LOW, the alarm is activated. So the circuit $C$ should be such that its output is 0 as soon as the limit for temperature or pressure is exceeded, i.e., when $A=0, B=1$ or when $A=1, B=0$ or when $A=B=1$. The output of $C$ should be HIGH when temperature and pressure are within the specified limit, i.e., when $A=B=0$. This gives the truth table 18.9 which the circuit $C$ has to implement. It can be seen that it is the truth table of NOR gate. So the circuit $C$ in Fig. 18.43 should be a NOR gate as shown in Fig. 18.44.
Fig. 18.43

| Table 18.9 |  |  |
| :--: | :--: | :--: |
| A | B | C |
| 0 | 0 | 1 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 0 |

Fig. 18.44

# GUMMARY

When an external potential difference is applied across a p-n junction such that p -side is positive and n -side is negative, it is called forward biased.
When the external source of voltage is applied across a p-n junction such that its positive terminal is connected to n-region and its negative terminal to p-region, the p-n junction is said to be reverse biased.
Conversion of alternating current into direct current is called rectification.
When only one half of alternating current cycle is converted into direct current, it is called half-wave rectification.
Transistor is a semiconductor device consisting of three electrodes, namely emitter, base and collector. For normal operation, the base-emitter junction is forward biased whereas the collector-base junction is reverse biased.

- Input resistance is the resistance between the positive and negative inputs of the amplifier.
- Output resistance is the resistance between the output terminal and ground.
- Instead of making amplifier circuit by discrete components, the whole amplifier is integrated on a small silicon chip and enclosed in a capsule. Pins connected with working terminals such as inputs, outputs and power supply project outside the capsule. Such an integrated amplifier is known as operational amplifier.
- Open loop gain is the ratio of output voltage and the difference between noninverting and inverting inputs when there is no external connection between the outputs and inputs.
- A digital system deals with quantities or variables which have only two discrete values or states.
- The electronic circuits which implement the various logic operations are known as logic gates.

# QUESTIONS

18.1 How does the motion of an electron in a n-type substance differ from the motion of holes in a p-type substance?
18.2 What is the net charge on a n-type or a p-type substance?
18.3 The anode of a diode is 0.2 V positive with respect to its cathode. Is it forward biased?
18.4 Why charge carriers are not present in the depletion region?
18.5 What is the effect of forward and reverse biasing of a diode on the width of depletion region?
18.6 Why ordinary silicon diodes do not emit light?
18.7 Why a photo diode is operated in reverse biased state?
18.8 Why is the base current in a transistor very small?
18.9 What is the biasing requirement of the junctions of a transistor for its normal operation? Explain how these requirements are met in a common emitter amplifier?
18.10 What is the principle of virtual ground? Apply it to find the gain of an inverting amplifier.
18.11 The inputs of a gate are 1 and 0 . Identify the gate if its output is (a) 0 , (b) 1
18.12 Tick $(\checkmark)$ the correct answer
(i) A diode characteristic curve is a plot between
(a) current and time
(b) voltage and time
(c) voltage and current
(d) forward voltage and reverse voltage

(ii). The colour of light emitted by a LED depends on
(a) its forward bias
(b) its reverse bias
(c) the amount of
(d) the type of semi-conductor forward current material used.
(iii) In a half-wave rectifier the diode conducts during
a. both halves of the input cycle
b. a portion of the positive half of the input cycle
c. a portion of the negative half of the input cycle
d. One half of the input cycle
(iv) In a bridge rectifier of Fig. Q. 18.1 when $V$, is positive at point $B$ with respect to point $A$, which diodes are $O N$.
a. $\quad D_{2}$ and $D_{4}$
b.
$D_{1}$ and $D_{3}$
c. $\quad D_{2}$ and $D_{3}$
d. $\quad D_{1}$ and $D_{4}$
(v) The common emitter current amplification factor $\beta$ is given by
a. $\frac{I_{\mathrm{C}}}{I_{\mathrm{E}}}$
b. $\frac{I_{\mathrm{C}}}{I_{\mathrm{B}}}$
c. $\frac{I_{\mathrm{E}}}{I_{\mathrm{B}}}$
d. $\frac{I_{\mathrm{B}}}{I_{\mathrm{E}}}$
(vi) Truth table of logic function
a. summarizes its output values
b. tabulates all its input conditions only
c. display all its input/output possibilities
d. is not based on logic algebra
(vii) The output of a two inputs OR gate is 0 only when its
a. both inputs are 0
b. either input is 1
c. both inputs are 1
d. either input is 0
(viii) A two inputs NAND gate with inputs $A$ and $B$ has an output 0 if
a. Ais 0
b. Bis 0
c. both $A$ and $B$ are zero
d. both $A$ and $B$ are 1
(ix) The truth table shown below is for
a. XNOR gate
b. OR gate
c. AND gate
d. NAND gate

| A | B | X |
| :--: | :--: | :--: |
| 0 | 0 | 1 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

# PROBLEMS

18.1 The current flowing into the base of a transistor is 100 $\mu \mathrm{A}$. Find its collector current $I_{\mathrm{c}}$, its emitter current $I_{E}$ and the ratio $I_{c} / I_{E}$, if the value of current gain $\beta$ is 100 .
(Ans: $10 \mathrm{~mA}, 10.1 \mathrm{~mA}, 0.99$ )
18.2 Fig.P.18.2 shows a transistor which operates a relay as the switch $S$ is closed. The relay is energized by a current of 10 mA . Calculate the value $R_{\mathrm{R}}$ which will just make the relay operate. The current gain $\beta$ of the transistor is 200 . When the transistor conducts, its $V_{\text {BE }}$ can be assumed to be 0.6 V .
(Ans: $168 \mathrm{k} \Omega$ )
18.3 In circuit (Fig.P.18.3), there is negligible potential drop between $B$ and $E$, if, $\beta$ is 100 . Calculate
(i) base current
(ii) collector current
(iii) potential drop across $R_{c}$
(iv) $V_{\text {CE }}$,
(Ans: $11.25 \mu \mathrm{~A}, 1.125 \mathrm{~mA}, 1.125 \mathrm{~V}, 7.875 \mathrm{~V}$ )
Fig. P. 18.3
18.4 Calculate the output of the op-amp circuit shown in Fig.P.18.4.
(Ans: 0)
Fig. P. 18.4
18.5 Calculate the gain of non-inverting amplifier shown in Fig.P.18.5.
(Ans: 5)
Fig. P. 18.5