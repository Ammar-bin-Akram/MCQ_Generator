# Chapter 18: ELECTRONICS

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

# DAWN OF MODERN PHYSICS

## Learning Objectives

At the end of this chapter the students will be able to:

1. Distinguish between inertial and non-inertial frames of references.
2. Describe the postulates of special theory of relativity and its results.
3. Understand the NAVASTAR navigation system.
4. Understand the concept of black body radiation.
5. Understand and describe how energy is distributed over the wavelength range for several values of source temperature.
6. Know Planck's assumptions.
7. Know the origin of quantum theory.
8. Show an appreciation of the particle nature of electromagnetic radiation.
9. Describe the phenomenon of photoelectric effect.
10. Explain photoelectric effect in terms of photon energy and work function.
11. Explain the function of photocell and describe its uses.
12. Describe Compton's effect.
13. Explain the phenomena of pair production and pair annihilation.
14. Describe de-Broglie's hypothesis of wave nature of particles.
15. Describe and interpret qualitatively the evidence provided by electron diffraction for the wave nature of particles.
16. Understand the working principle of electron microscope.
17. Understand and describe uncertainty principle.

In the early part of the twentieth century, many experimental and theoretical problems remained unresolved. Attempts to explain the behaviour of matter on the atomic level with the laws of classical physics were not successful. Phenomena such as black body radiation, the photoelectric effect, the emission of sharp spectral lines by atoms in a gas discharge tube, and invariance of speed of light, could not be understood within the framework of classical physics. To explain these observations a revolutionary framework of explanation was necessary which we call modern physics. Its two most significant features are relativity and quantum theory. The observations on objects moving very fast, approaching the speed of light, are well explained by the special theory of relativity. Quantum theory has been able to explain the behaviour of electromagnetic radiation as discrete packets of energy and the particles on a very small scale are dominated by wave properties.
Classical physics is still valid in ordinary processes of everyday life. But to explain the behaviour of tiny or very fast moving particles, we have to use the above mentioned theories. In this chapter, we shall discuss various aspects of theory of relativity and quantum

theory. Before introducing special theory of relativity, some related terms are discussed briefly.

# 19.1 RELATIVE MOTION

When we say a ball is thrown up, the 'up' direction is only for that particular place. It will be 'down' position for a person on the diametrically opposite side of the globe. The concept of direction is purely relative. Similarly, the rest position or the motion of an object is not same for different observers. For example, the walls of the cabin of a moving train are stationary with respect to the passengers sitting inside it but are in motion to a person stationary on the ground. So we cannot say whether an object is absolutely at rest or absolutely in motion. All motions are relative to a person or instrument observing it.
Let us perform an experiment in two cars moving with constant velocities in any direction. Suppose a ball is thrown straight up. It will come back straight down. This will happen in both cars. But if a person in one car observes the experiment done in the other car, will he observe the same? Suppose now one car is stationary. The person in the other car, which is moving with constant velocity, throws a ball straight up. He will receive the ball straight down. On the other hand, the fellow sitting in the stationary car observes that the path of the ball is a parabola. Thus, when experimenters observe what is going on in their own frame of reference, the same experiment gives identical observations. But if they look into other frames, they observe differently.

### 19.2 FRAMES OF REFERENCE

We have discussed the most commonly used Cartesian coordinate system. In effect, a frame of reference is any coordinate system relative to which measurements are taken. The position of a table in a room can be located relative to the walls of the room. The room is then the frame of reference. For measurements taken in the college laboratory, the laboratory is the reference frame. If the same experiment is performed in a moving train, the train becomes a frame of reference. The position of a spaceship can be described relative to the positions of the distant stars. A coordinate system based on these stars is then the frame of reference.
An inertial frame of reference is defined as a coordinate system in which the law of inertia is valid. That is, a body at

rest remains at rest unless an unbalanced force produces acceleration in it. Other laws of nature also apply in such a system. If we place a body upon Earth it remains at rest unless an unbalanced force is applied upon it. This observation shows that Earth may be considered as an inertial frame of reference. A body placed in a car moving with a uniform velocity with respect to Earth also remains at rest, so that car is also an inertial frame of reference. Thus any frame of reference which is moving with uniform velocity relative to an inertial frame is also an inertial frame.
When the moving car is suddenly stopped, the body placed in it, no longer remains at rest. So is the case when the car is suddenly accelerated. In such a situation, the car is not an inertial frame of reference. Thus an accelerated frame is a non-inertial frame of reference. Earth is rotating and revolving and hence strictly speaking, the Earth is not an inertial frame. But it can often be treated as an inertial frame without serious error because of very small acceleration.

# 19.3 SPECIAL THEORY OF RELATIVITY

The theory of relativity is concerned with the way in which observers who are in a state of relative motion describe physical phenomena. The special theory of relativity treats problems involving inertial or non-accelerating frames of reference. There is another theory called general theory of relativity which treats problems involving frames of reference accelerating with respect to one another. The special theory of relativity is based upon two postulates, which can be stated as follows:

1. The laws of physics are the same in all inertial frames.
2. The speed of light in free space has the same value for all observers, regardless of their state of motion.
The first postulate is the generalization of the fact that all physical laws are the same in frames of reference moving with uniform velocity with respect to one another. If the laws of physics were different for different observers in relative motion, the observer could determine from this difference that which of them were stationary in a space and which were moving. But such a distinction does not exist, so this postulate implies that there is no way to detect absolute uniform motion. The second postulate states an experimental fact that speed of light in free space is the universal constant ' $c$ ' ( $c=3 \times 10^{6} \mathrm{~ms}^{-1}$ ). These simple postulates have far-reaching consequences. These

## The speed of light emitted by flashlight is c measured by two observers, one on the moving track and the other on the road.

include such phenomena as the slowing down of clocks and contraction of lengths in moving reference frames as measured by a stationary observer. Some interesting results of the special theory of relativity can be summarized as follows without going into their mathematical derivations.

# Time Dilation

According to special theory of relativity, time is not absolute quantity. It depends upon the motion of the frame of reference.

Suppose an observer is stationary in an inertial frame. He measures the time interval between two events in this frame. Let it be $t_{0}$. This is known as proper time. If the observer is moving with respect to frame of events with velocity $v$ or if the frame of events is moving with respect to observer with a uniform velocity $v$, the time measured by the observer would not be $t_{0}$, but it would be $t$ given by

$$
t=\frac{t_{0}}{\sqrt{1-\frac{v^{2}}{c^{2}}}}
$$

As the quantity $\sqrt{1-\frac{v^{2}}{c^{2}}}$ is always less than one, so $t$ is greater than $t_{0}$ i.e., time has dilated or stretched due to relative motion of the observer and the frame of reference of events. This astonishing result applies to all timing processes -- physical, chemical and biological. Even aging process of the human body is slowed by motion at very high speeds.

## Length Contraction

The distance from Earth to a star measured by an observer in a moving spaceship would seem smaller than the distance measured by an observer on Earth. That is, if you are in motion relative to two points that are a fixed distance apart, the distance between the two points appears shorter than if you were at rest relative to them. This effect is known as length contraction. The length contraction happens only along the direction of motion. No such contraction would be observed perpendicular to the direction of motion. The length of an object or distance between two points measured by an observer who is relatively at rest is called proper length ' $l_{0}$ '. If an object and an observer are in relative motion with speed $v$, then the contracted length ' $l$ ' is given by

$$
\ell=\ell_{0} \sqrt{1-\frac{v^{2}}{c^{2}}}
$$

# Mass Variation

According to special theory of relativity, mass of an object is a varying quantity and depends upon the speed of the object. An object whose mass when measured at rest is $m_{n}$ will have an increased mass $m$ when observed to be moving at speed $v$. They are related by

$$
m=\frac{m_{n}}{\sqrt{1-\frac{v^{2}}{c^{2}}}}
$$

The increase in mass indicates the increase in inertia the object has at high speeds. As $v$ approaches $c$, it requires a larger and larger force to change the speed of the object.
As $\quad v \rightarrow c, \frac{v}{c} \rightarrow 1 \quad$ therefore $\sqrt{1-\frac{v^{2}}{c^{2}}} \rightarrow 0$
Thus

$$
\mathrm{m} \rightarrow \infty
$$

An infinite mass would require an infinite force to accelerate it. Because infinite forces are not available, hence, an object cannot be accelerated to the speed of light' $c^{\prime}$ in free space.
In our everyday life, we deal with extremely small speeds, compared to the speed of light. Even the Earth's orbital speed is only $30 \mathrm{kms}^{-1}$. On the other hand, the speed of light in free space is $300,000 \mathrm{kms}^{-1}$. This is the reason why Newton's laws are valid in everyday situations. However, when experimenting with atomic particles moving with velocities approaching speed of light, the relativistic effects are very prominent, and experimental results cannot be explained without taking Einstein's equations into account.

## Energy $\cdot$ Mass Relation

According to special theory of relativity, mass and energy are different entities but are interconvertible. The total energy $E$ and mass $m$ of an object are related by the expression

$$
E=m c^{2}
$$

where $m$ depends on the speed of the object. At rest, the energy equivalent of an object's mass $m_{n}$ is called rest mass energy $E_{n}$.

$$
E_{0}=m_{0} c^{2}
$$

As $m c^{2}$ is greater than $m_{0} c^{2}$, the difference of energy $\left(m c^{2}-m_{0} c^{2}\right)$ is due to motion, as such it represents the kinetic energy of the mass. Hence

$$
K . E_{1}=\left(m-m_{0}\right) c^{2}
$$

From equation 19.4 above, the change in mass $m$ due to change in energy $\Delta E$ is given by

$$
\Delta m=\frac{\Delta E}{c^{2}}
$$

Because $c^{2}$ is a very large quantity, this implies that small changes in mass require very large changes in energy. In our everyday world, energy changes are too small to provide measurable mass changes. However, energy and mass changes in nuclear reactions are found to be exactly in accordance with the above mentioned equations.

# NAVSTAR Navigation System

The results of special theory of relativity are put to practical use even in everyday life by a modern system of navigation satellites called NAVSTAR. The location and speed anywhere on Earth can now be determined to an accuracy of about $2 \mathrm{cms}^{-1}$. However, if relativity effects are not taken into account, speed could not be determined any closer than about $20 \mathrm{cms}^{-1}$. Using these results the location of an aircraft after an hour's flight can be predicted to about 50 m as compared to about 760 m determined by without using relativistic effects.

Example 19.1: The period of a pendulum is measured to be 3.0 s in the inertial reference frame of the pendulum. What is its period measured by an observer moving at a speed of 0.95 c with respect to the pendulum?

## $$
t_{0}=3.0 \mathrm{~s}, \quad v=0.95 \mathrm{c}, t=\text { ? }
$$

Using

$$
t=\frac{t_{0}}{\sqrt{1-v^{2}}}
$$

$t=\frac{3.0 \mathrm{~s}}{\sqrt{1-\frac{(0.95 c)^{2}}{c^{2}}}}=\frac{3.0 \mathrm{~s}}{\sqrt{1-(0.95)^{2}}}=9.6 \mathrm{~s}$

Example 19.2: A bar 1.0 m in length and located along $x$-axis moves with a speed of 0.75 c with respect to a stationary observer. What is the length of the bar as measured by the stationary observer?

# $$
\ell_{0}=1.0 \mathrm{~m}, \quad v=0.75 \mathrm{c}, \quad \ell=\text { ? }
$$

Using

$$
\ell=\ell_{0} \sqrt{1-\frac{v^{2}}{c^{2}}}
$$

$$
\ell=1.0 \mathrm{~m} \times \sqrt{1-\frac{(0.75 c)^{2}}{c^{2}}}=1.0 \mathrm{~m} \times \sqrt{1-(0.75)^{2}}=0.66 \mathrm{~m}
$$

Example 19.3: Find the mass $m$ of a moving object with speed 0.8 c .

## Using

$$
m=\frac{m_{0}}{\sqrt{1-\frac{v^{2}}{c^{2}}}}
$$

or

$$
m=\frac{m_{0}}{\sqrt{1-\frac{(0.8 c)^{2}}{c^{2}}}}=\frac{m_{0}}{\sqrt{1-(0.8)^{2}}}=1.67 m_{0}
$$

or

$$
m=1.67 m_{0}
$$

### 19.4 BLACK BODY RADIATION

When a body is heated, it emits radiation. The nature of radiation depends upon the temperature. At low temperature, a body emits radiation which is principally of long wavelengths in the invisible infrared region. At high temperature, the proportion of shorter wavelength radiation increases. Furthermore, the amount of emitted radiation is different for different wavelengths. It is of interest to see how the energy is distributed among different wavelengths at various temperatures. For example, when platinum wire is heated, it appears dull red at about $500^{\circ} \mathrm{C}$, changes to cherry red at $900^{\circ} \mathrm{C}$, becomes orange red at $1100^{\circ} \mathrm{C}$, yellow at $1300^{\circ} \mathrm{C}$ and finally white at about $1600^{\circ} \mathrm{C}$. This shows that as the temperature is increased, the radiation becomes richer in shorter wavelengths.

In order to understand the distribution of radiation emitted from a hot body, we consider a non-reflecting object such as a solid
(a) Absorption of radiation

Fig. 19.1

that has a hollow cavity within it. It has a small hole and the radiation can enter or escape only through this hole. The inside is blackened with soot to make it as good an absorber and as bad a reflector as possible. The small hole appears black because the radiation that enters is reflected from the inside walls many times and is partly absorbed at each reflection until none remains. Such a body is termed as black body and has the property to absorb all the radiation entering it. A black body is both an ideal absorber (Fig. 19.1 a) and an ideal radiator (Fig. 19.1 b).

# Intensity Distribution Diagram

Lummer and Pringsheim measured the intensity of emitted energy with wavelength radiated from a black body at different temperatures by the apparatus shown in Fig.19.2. The amount of radiation emitted with different wavelengths is shown in the form of energy distribution curves for each temperature in the Fig.19.3.
These curves reveal the following interesting facts.

1. At a given temperature, the energy is not uniformly distributed in the radiation spectrum of the body.
2. At a given temperature $T$, the emitted energy has maximum value for a certain wavelength $\lambda_{\text {max }}$ and the product $\lambda_{\text {max }} \times$ T remains constant .

$$
\lambda_{\max } \times T=\text { Constant }
$$

The value of the constant known as Wien's constant is about $2.9 \times 10^{-3} \mathrm{~m} \mathrm{~K}$. This equation means that as $T$

increases, $\lambda_{\text {max }}$ shifts to shorter wavelength.
3. For all wavelengths, an increase in temperature causes an increase in energy emission. The radiation intensity increases with increase in wavelengths and at a particular wavelength $\lambda_{\text {max }}$, it has a maximum value. With further increase in wavelength, the intensity decreases.
4 The area under each curve represents the total energy $(E)$ radiated per second per square metre over all wavelengths at a particular temperature. It is found that area is directly proportional to the fourth power of kelvin temperature $T$. Thus

$$
E \propto T^{4} \quad \text { or } \quad E=\sigma_{T}^{4}
$$

where $\sigma$ is called Stefen's constant. Its value is $5.67 \times 10^{-6}$ $\mathrm{Wm}^{-2} \mathrm{~K}^{-4}$ and the above relation is known as StefenBoltzmann law.

# Planck's Assumption

Electromagnetic wave theory of radiation cannot explain the energy distribution along the intensity-wavelengths curves. The successful attempts to explain the shape of energy distribution curves gave rise to a new and non-classical view of electromagnetic radiation. In 1900. Max Planck founded a mathematical model resulting in an equation that describes the shape of observed curves exactly. He suggested that energy is radiated or absorbed in discrete packets, called quanta rather than as a continuous wave. Each quantum is associated with radiation of a single frequency. The energy $E$ of each quantum is proportional to its frequency $f$, and

$$
E=\mathrm{hf}
$$

where $h$ is Planck's constant. Its value is $6.63 \times 10^{-34} \mathrm{Js}$. This fundamental constant is as important in physics as the constant $c$, the speed of light in vacuum.
Max Planck received the Nobel Prize in physics in 1918 for his discovery of energy quanta.

## The Photon

Planck suggested that as matter is not continuous but consists of a large number of tiny particles, so is the radiation energy from a source. He assumed that granular nature of

radiation from hot bodies was due to some property of the atoms producing it. Einstein extended his idea and postulated that packets or tiny bundles of energy are integral part of all electromagnetic radiation and that they could not be subdivided. These indivisible tiny bundles of energy he called photons. The beam of light with wavelength $\lambda$ consists of stream of photons travelling at speed $c$ and carries energy hf. From the theory of relativity momentum $p$ of the photon is related to energy as

$$
E=p c
$$

Thus $p c=\mathrm{hf} \quad$ or $\quad p=\frac{\mathrm{hf}}{c}=\frac{\mathrm{h}}{\lambda}$
The table 19.1 relates the quanta emitted in different regions of the electromagnetic spectrum with energy. At the high end, $\gamma$ - radiation with energy $\sim 1 \mathrm{MeV}$ is easily detected as quanta by a radiation detector and counter. At the other end, the energy of photon of radio waves is only about $10^{-10} \mathrm{eV}$. So millions of photons are needed to detect a signal and hence wave properties of radio waves predominate. The quanta are

Table: 19.1 Electromagnetic spectrum
so close together in energy value that radio waves are detected as continuous radiation.

The emission or absorption of energy in steps may be extended to include any system such as a mass oscillating on a spring. However, the energy steps are far too small to be detected and so any granular nature is invisible. Quantum effects are only important when observing atomic sized objects, where $h$ is a significant factor in any detectable energy change.
Example 19.4: Assuming you radiate as does a blackbody at your body temperature about $37^{\circ} \mathrm{C}$, at what wavelength do you emit the most energy?

# $$
\begin{aligned}
T & =37^{\circ} \mathrm{C}=310 \mathrm{~K} \\
\text { Wien's constant } & =2.9 \times 10^{-3} \mathrm{mK} \\
\lambda_{\max } & =? \\
\text { Using } \lambda_{\max } \times T & =\text { Constant } \\
\lambda_{\max }=\frac{2.9 \times 10^{-3} \mathrm{mK}}{310 \mathrm{~K}} & =9.35 \times 10^{-6} \mathrm{~m}=9.35 \mu \mathrm{~m}
\end{aligned}
$$

The radiation lies in the invisible infrared region and is independent of skin colour.
Example 19.5: What is the energy of a photon in a beam of infrared radiation of wavelength 1240 nm ?

## $$
\lambda=1240 \mathrm{~nm} \quad E=? \text { }
$$

Using $\quad E=\mathrm{h} f=\frac{\mathrm{hc}}{\lambda}$

$$
E=\frac{6.63 \times 10^{-34} \mathrm{Js} \times 3 \times 10^{8} \mathrm{~ms}^{-1}}{1240 \times 10^{-9} \mathrm{~m}}=1.6 \times 10^{-19} \mathrm{~J}
$$

or $\quad E=1.0 \mathrm{eV}$

### 19.5 INTERACTION OF ELECTROMAGNETIC RADIATION WITH MATTER

Electromagnetic radiation or photons interact with matter in three distinct ways depending mainly on their energy. The three processes are

Fig 19.4 Experimental arrangement to observe photoelectric effect.
Fig 19.5 Characteristic curves of photocurrent vs. applied voltage for two intensities of monochromatic light.
Fig 19.8 Characteristic curves of photocurrent vs. applied voltage for light of differentfrequencies.
(i) Photoelectric effect
(ii) Compton effect
(iii) Pair production

## Photoelectric Effect * *

The emission of electrons from a metal surface when exposed to light of suitable frequency is called the photoelectric effect. The emitted electrons are known as photoelectrons.

The photoelectric effect is demonstrated by the apparatus shown in Fig. 19.4. An evacuated glass tube $X$ contains two electrodes. The electrode A connected to the positive terminal of the battery is known as anode. The electrode $C$ connected to negative terminal is known as cathode. When monochromatic light is allowed to shine on cathode, it begins to emit electrons. These photoelectrons are attracted by the positive anode and the resulting current is measured by an ammeter. The current stops when light is cut off, which proves, that the current flows because of incident light. This current is, hence, called photoelectric current. The maximum energy of the photoelectrons can be determined by reversing the connection of the battery in the circuit i.e., now the anode A is negative and cathode C is at positive potential. In this condition the photoelectrons are repelled by the anode and the photoelectric current decreases. If this potential is made more and more negative, at a certain value, called stopping potential $V_{0}$, the current becomes zero. Even the electrons of maximum energy are not able to reach collector plate. The maximum energy of photoelectrons is thus

$$
\frac{1}{2} m v_{\max }^{2}=V_{0} e
$$

where $m$ is mass, $v$ is velocity and $e$ is the charge on electron. If the experiment is repeated with light beam of higher intensity, the amount of current increases but the current stops for the same value of $V_{0}$. The Fig. 19.5 shows two curves of photoelectric current as a function of potential $V$ where $I_{2}>I_{1}$. If, however, the intensity is kept constant and experiment is performed with different frequencies of incident light, we obtain the curves shown in Fig.19.6. The current is same but stopping potential is different for each frequency of incident light, which indicates the proportionality of maximum kinetic energy with frequency of light $f$.

The important results of the experiments are
1. The electrons are emitted with different energies. The maximum energy of photoelectrons depends on the particular metal surface and the frequency of incident light.
2. There is a minimum frequency below which no electrons are emitted, however intense the light may be. This threshold frequency $f_{0}$ varies from metal to metal.
3. Electrons are emitted instantaneously, the intensity of light determines only their number.
These results could not be explained on the basis of electromagnetic wave theory of light. According to this theory, increasing the intensity of incident light should increase the K.E. of emitted electrons which contradicts the experimental result. The classical theory cannot also explain the threshold frequency of light.

## Explanation on the Basis of Quantum Theory

Einstein extended the idea of quantization of energy proposed by Max Planck that light is emitted or absorbed in quanta, known as photons. The energy of each photon of frequency $f$ as given by quantum theory is

$$
E=h f
$$

A photon could be absorbed by a single electron in the metal surface. The electron needs a certain minimum energy called the work function ' $\Phi$ ' to escape from the metal surface. If the energy of incident photon is sufficient, the electron is ejected instantaneously from the metal surface. A part of the photon energy (work function) is used by the electron to break away from the metal and the rest appears as the kinetic energy of the electron. That is,
Incident photon energy - Work function = Max. K.E. of photoelectron
or

$$
h f \cdot \Phi=\frac{1}{2} m v_{\max }^{2}
$$

This is known as Einstein's photoelectric equation.
When $K . E_{\text {max }}$ of the photoelectron is zero, the frequency $f$ is equal to threshold frequency $f_{0}$, hence the Eq. 19.12 becomes

$$
\mathrm{hf}_{\mathrm{o}}-\Phi=0 \quad \text { or } \quad \Phi=\mathrm{hf}_{\mathrm{o}}
$$

Hence, we can also write Einstein's photoelectric equation as

A graph of the maximum kinetic energy of photoelectrons vs. light frequency. Below a certain frequency, $f_{0}$, no photoemission occurs.

Fig 19.7 Simple photo-emissive cell
Fig 19.8 Sound track on a film which varies the intensity of light reaching the photo cell.
Fig. 19.8 Photocell detection circuit for sound track of movies.

It is to be noted that all the emitted electrons do not possess the maximum kinetic energy, some electrons come straight out of the metal surface and some lose energy in atomic collisions before coming out. The equation 19.14 holds good only for those electrons which come out with full surplus energy.
Albert Einstein was awarded Nobel Prize in physics in 1921 for his explanation of photoelectric effect.
Note that the phenomenon of photoelectric effect cannot be explained if we assume that light consists of waves and energy is uniformly distributed over its wavefront. It can only be explained by assuming light consists of corpuscles of energy known as photon. Thus it shows the corpuscular nature of light.

## Photocell

A photocell is based on photoelectric effect. A simple photocell is shown in Fig. 19.7. It consists of an evacuated glass bulb with a thin anode rod and a cathode of an appropriate metal surface. The material of the cathode is selected to suit to the frequency range of incident radiation over which the cell is operated. For example sodium or potassium cathode emits electrons for visible light, cesium coated oxidized silver emits electrons for infrared light and some other metals respond to ultraviolet radiation. When photo-emissive surface is exposed to appropriate light (Fig.19.8 a), electrons are emitted and a current flows in the external circuit which increases with the increase in light intensity. The current stops when the light beam is interrupted. The cell has wide range of applications. Some of these are to operate:

1. Security systems
2. Counting systems
3. Automatic door systems
4. Automatic street lighting
5. Exposure meter for photography
6. Sound track of movies (Fig. 19.8 b)

Example 19.6: A sodium surface is illuminated with light of wavelength 300 nm . The work function of sodium metal

is 2.46 eV .
(a) Find the maximum K.E. of the ejected electron.
(b) Determine the cut off wavelength for sodium.

# $$
\lambda=300 \mathrm{~nm}, \quad \Phi=2.46 \mathrm{eV}
$$

(a) Energy of incident photon $E=\mathrm{h} f=\frac{\mathrm{hc}}{\lambda}$
or $E=\frac{6.63 \times 10^{-34} \mathrm{Js} \times 3 \times 10^{8} \mathrm{~ms}^{-1}}{300 \times 10^{-9} \mathrm{~m}}=6.63 \times 10^{-19} \mathrm{~J}$

$$
E=4.14 \mathrm{eV}
$$

Now $K . E_{\max }=\mathrm{h} f-\Phi=4.14 \mathrm{eV}-2.46 \mathrm{eV}=1.68 \mathrm{eV}$
(b) $\Phi=2.46 \mathrm{eV}=3.94 \times 10^{-19} \mathrm{~J}$

Using

$$
\Phi=\mathrm{h} f_{0}=\frac{\mathrm{hc}}{\lambda_{0}}
$$

or $\lambda_{0}=\frac{h c}{\Phi}=\frac{6.63 \times 10^{-34} \mathrm{Js} \times 3 \times 10^{8} \mathrm{~ms}^{-1}}{3.94 \times 10^{-19} \mathrm{~J}}=5.05 \times 10^{-7} \mathrm{~m}$

$$
\lambda_{0}=505 \mathrm{~nm}
$$

The cut off wavelength is in the green region of the visible spectrum

## Ccmpton Effect

Arthur Holly Compton at Washington University in 1923 studied the scattering of X-rays by loosely bound electrons from a graphite target (Fig.19.9 a). He measured the wavelength of X-rays scattered at an angel $\theta$ with the original direction. He found that wavelength $\lambda_{0}$ of the scattered $X$-rays is larger than the wavelength $\lambda$ of the incident $X$-rays. This is known as Compton effect. The increase in wavelength of scattered $X$-rays could not be explained on the basis of classical wave theory. Compton suggested that X-rays consist of photons and in the process of scattering the photons suffer collision with electrons like billiard balls (Fig. 19.9 b \& c). In this collision, a part of incident photon energy and momentum is transferred to an electron. Applying energy and momentum conservation laws to the process, he derived an expression for the change in wavelength $\Delta \lambda$ known as Compton shift for scattering angle $\theta$ as
(a)
(a) Compton's scattering experiment

(b)
(c)
(b) A photon collides with an
electron and (c) Both are scattered

$$
\Delta \lambda=\frac{h}{m_{0} c}(1-\cos \theta)
$$

where $m_{0}$ is the rest mass of the electron. The factor $\frac{h}{m_{0} c}$ has dimensions of length and is called Compton wavelength and has the numerical value

$$
\frac{h}{m_{0} c}=\frac{6.63 \times 10^{-34} \mathrm{Js}}{9.1 \times 10^{-31} \mathrm{~kg} \times 3 \times 10^{8} \mathrm{~ms}^{-1}}=2.43 \times 10^{-12} \mathrm{~m}
$$

If the scattered X-ray photons are observed at $\theta=90^{\circ}$, the Compton shift $\Delta \lambda$ equals the Compton wavelength. The Eq. 19.15 was found to be in complete agreement with Compton's experimental result, which again is a striking confirmation of particle like interaction of electromagnetic waves with matter.
Arthur Holly Compton was awarded Nobel Prize in physics in 1927 for his discovery of the effect named after him.
Example 19.7: A 50 keV photon is Compton scattered by a quasi-free electron. If the scattered photon comes off at $45^{\circ}$, what is its wavelength?

# $$
E=50 \mathrm{keV}=50 \times 10^{3} \times 1.6 \times 10^{-19} \mathrm{~J}
$$

Using

$$
E=\mathrm{h} f=\frac{\mathrm{h} c}{\lambda} \quad \text { or } \quad \lambda=\frac{\mathrm{h} c}{E}
$$

$$
\lambda=\frac{6.63 \times 10^{-34} \mathrm{Js} \times 3 \times 10^{8} \mathrm{~ms}^{-1}}{50 \times 10^{3} \times 1.6 \times 10^{-19} \mathrm{~J}}=0.0248 \mathrm{~nm}
$$

Now

$$
\lambda^{\prime}-\lambda=\frac{h}{m c}\left(1-\cos 45^{\circ}\right)
$$

$$
\begin{gathered}
\lambda^{\prime}-\lambda=\frac{6.63 \times 10^{-34} \mathrm{Js}}{9.1 \times 10^{-31} \mathrm{~kg} \times 3 \times 10^{8} \mathrm{~ms}^{-1}}(1-0.707) \\
=0.2429 \times 10^{-11} \mathrm{~m} \times 0.293 \\
\lambda^{\prime}-\lambda=0.0007 \mathrm{~nm} \\
\lambda^{\prime}=\lambda+0.0007 \mathrm{~nm} \\
\lambda^{\prime}=0.0248 \mathrm{~nm}+0.0007 \mathrm{~nm}=0.0255 \mathrm{~nm}
\end{gathered}
$$

# Pair Production

In the previous sections you have studied that a low energy photon interacting with a metal is usually completely absorbed with the emission of electron (Photoelectric effect) and a high energy photon such as that of X-rays is scattered by an atomic electron transferring a part of its energy to the electron (Compton effect). A third kind of interaction of very high energy photon such as that of $\gamma$-rays with matter is pair production in which photon energy is changed into an electron-positron pair. A positron is a particle having mass and charge equal to that of electron but the charge being of opposite nature i.e. positive. The creation of two particles with equal and opposite charges is essential for charge conservation in the universe. The positron is also known as antiparticle of electron or anti-electron. The interaction usually takes place in the electric field in the vicinity of a heavy nucleus as shown in the Fig. 19.10 so that there is a particle to take up recoil energy and momentum is conserved.
In the process, radiant energy is converted into matter in accordance with Einstein's equation $E=m c^{2}$, and hence, is also known as materialization of energy. For an electron or positron, the rest mass energy $=m_{e} c^{2}=0.51 \mathrm{MeV}$. Thus to create the two particles $2 \times 0.51 \mathrm{MeV}$ or 1.02 MeV energy is required. For photons of energy greater than 1.02 MeV , the probability of pair production occurrence increases as the energy increases and the surplus energy is carried off by the two particles in the form of kinetic energy. The process can be represented by the equation
Energy of photon $=\left[\begin{array}{l}\text { Energy required } \\ \text { for pair production }\end{array}\right]+\left[\begin{array}{l}\text { Kinetic energy } \\ \text { of the particles }\end{array}\right]$

$$
\mathrm{h} f=2 m_{0} \mathrm{c}^{2}+\mathrm{K} . \mathrm{E} .\left(\mathrm{e}^{-}\right)+\mathrm{K} . \mathrm{E} .\left(\mathrm{e}^{+}\right)
$$

Pair Production
Fig. 19.10

### 19.6 ANNIHILATION OF MATTER

It is converse of pair production when a positron comes close to an electron they annihilate or destroy each other. The matter of two particles changes into electromagnetic energy producing two photons in the $\gamma$-rays range.

$$
e^{-}+e^{+} \longrightarrow \gamma+\gamma
$$

The two photons are produced travelling in opposite directions (Fig. 19.11) so that momentum is conserved. Each

photon has energy 0.51 MeV equivalent to rest mass energy of a particle.

The existence of positron was predicted by Dirac in 1928 and it was discovered in the cosmic radiation in 1932 by Carl Anderson. It gradually became clear that every particle has a corresponding antiparticle with the same mass and charge (if it is a charged particle) but of opposite sign. Particles and antiparticles also differ in the signs of other quantum numbers that we have not yet discussed. A particle and its antiparticle cannot exist together at one place. Whenever they meet, they annihilate each other. That is, the particles disappear, their combined rest energies appear in other forms. Proton and antiproton annihilation has also been observed at Lawrence Berkeley Laboratory.

# 19.7 WAVE NATURE OF PARTICLES

It has been observed that light displays a dual nature, it acts as a wave and it acts as a particle. Assuming symmetry in nature, the French physicist, Louis de Broglie proposed in 1924 that particles should also possess wavelike properties. As momentum $p$ of photon is given by equation 19.11.

$$
p=\frac{\mathrm{h}}{\lambda}
$$

de Broglie suggested that momentum of a material particle of mass $m$ moving with velocity $v$ should be given by the same expression. Thus

$$
\begin{aligned}
& p=\frac{\mathrm{h}}{\lambda}=m v \\
& \lambda=\frac{\mathrm{h}}{p}=\frac{\mathrm{h}}{m v}
\end{aligned}
$$

## where $\lambda$ is the wavelength associated with particle waves. Hence an electron can be considered to be a particle and it can also be considered to be a wave. The equation 19.17 is called de Broglie relation.
An object of large mass and ordinary speed has such a small wavelength that its wave effects such as interference and diffraction are negligible. For example, a rifle bullet of mass 20 g and flying with speed 330 ms " will have a wavelength $\lambda$ given by

$$
\lambda=\frac{\mathrm{h}}{m v}=\frac{6.63 \times 10^{-34} \mathrm{Js}}{2 \times 10^{-2} \mathrm{~kg} \times 330 \mathrm{~ms}^{-1}}=1 \times 10^{-34} \mathrm{~m}
$$

Light is, in short, the most refined form of matter (Louis de Broglie 1892-1987)

This wavelength is so small that it is not measurable or detectable by any of its effects.
On the other hand for an electron moving with a speed of $1 \times 10^{6} \mathrm{~ms}^{-1}$,

$$
\lambda=\frac{6.63 \times 10^{-34} \mathrm{Js}}{9.1 \times 10^{-31} \mathrm{~kg} \times 1 \times 10^{6} \mathrm{~ms}^{-1}}=7 \times 10^{-10} \mathrm{~m}
$$

This wavelength is in the X-rays range. Thus, diffraction effects for electrons are measurable whereas diffraction or interference effects for bullets are not.

# Davisson and Germer Experiment

A convincing evidence of the wave nature of electrons was provided by Clinton J. Davisson and Laster H. Germer. They showed that electrons are diffracted from metal crystals in exactly the same manner as X-rays or any other wave. The apparatus used by them is shown in Fig. 19.12, in which electrons from heated filament are accelerated by an adjustable applied voltage $V$. The electron beam of energy Ve is made incident on a nickel crystal. The beam diffracted from crystal surface enters a detector and is recorded as a current $I$. The gain in $K . E$. of the electron as it is accelerated by a potential $V$ in the electron gun is
given by

$$
\frac{1}{2} m v^{2}=V e
$$

or

$$
m v^{2}=2 \mathrm{Ve} ; \quad m^{2} v^{2}=2 \mathrm{mVe}
$$

or

$$
m v=\sqrt{2 m V e}
$$

From de Broglie equation

$$
\lambda=\frac{h}{m v}
$$

Thus

$$
\lambda=\frac{h}{\sqrt{2 m V e}}
$$

In one of the experiments, the accelerating voltage $V$ was 54 volts, hence

$$
\begin{gathered}
\lambda=\frac{h}{\sqrt{2 m V e}}=\frac{6.63 \times 10^{-34} \mathrm{Js}}{\sqrt{2 \times 9.1 \times 10^{-31} \mathrm{~kg} \times 54 \mathrm{JC}^{-1} \times 1.6 \times 10^{-19} \mathrm{C}}} \\
\lambda=1.66 \times 10^{-10} \mathrm{~m}
\end{gathered}
$$

This beam of electrons diffracted from crystal surface was obtained for a glancing angle of $65^{\circ}$. According to Bragg's
Fig. 19.12 Experimental arrangement of Davisson and Germer for electron diffraction.

equation

$$
2 d \sin \theta=m \lambda
$$

For 1st order diffraction $m=1$
For nickel

$$
d=0.91 \times 10^{-10} \mathrm{~m}
$$

Thus

$$
2 \times 0.91 \times 10^{-10} \mathrm{~m} \times \sin 65^{\circ}=\lambda
$$

which gives $\quad \lambda=1.65 \times 10^{-10} \mathrm{~m}$
Thus, experimentally observed wavelength is in excellent agreement with theoretically predicted wavelength.

(a)
(b)
(a) If electrons behaved as discrete particles with no wave properties. they would bass through one or the other of the two slits and strike the screen. causing it to glow and produce exact images of the slits. (b) In reality the screen reveals a pattern of bright and dark fringes similar to light is used and interference occurs between the light waves coming from each slit.
Diffraction patterns have also been observed with protons, neutrons, hydrogen atoms and helium atoms thereby giving substantial evidence for the wave nature of particles.

For his work on the dual nature of particles, Prince Louis Victor de Broglie received the 1929 Nobel Prize in physics. Clinton Joseph Davisson and George Paget Thomson shared the Nobel Prize in 1937 for their experimental confirmation of the wave nature of particles.

## Wave Particle Duality

Interference and diffraction of light confirm its wave nature, while photoelectric effect proves the particle nature of light. Similarly, the experiments of Davisson and Germer and G. P. Thomson reveal wave like nature of electrons and in the experiment of J. J. Thomson to find e/m we had to assume particle like nature of the electron. In the same way we are forced to assume both wavelike and particle like properties for all matter: electrons, protons, neutrons, molecules etc. and also light, X-rays, $\gamma$-rays etc. have to be included in this. In other words, matter and radiation have a dual 'waveparticle' nature and this new concept is known as wave particle duality. Niels Bohr pointed out in stating his principle of complementarity that both wave and particle aspects are required for the complete description of both radiation and matter. Both aspects are always present and either may be revealed by an experiment. However, both aspects cannot be revealed simultaneously in a single experiment, which aspect is revealed is determined by the nature of the experiment being done. If you put a diffraction grating in the path of a light beam, you reveal it as a wave. If you allow the light beam to hit a metal surface, you need to regard the beam as a stream of particles to explain your observations. There is no simple experiment that you can carry out with the

beam that will require you to interpret it as a wave and as a particle at the same time. Light behaves as a stream of photons when it interacts with matter and behaves as a wave in traveling from a source to the place where it is detected. In effect, all micro-particles (electrons, protons, photons, atoms etc.) propagate as if they were waves and exchange energies as if they were particles - that is the wave particle duality.
Example 19.8: A particle of mass 5.0 mg moves with speed of $8.0 \mathrm{~ms}^{-1}$. Calculate its de Broglie wavelength.

# $$
\begin{aligned}
m & =5.0 \mathrm{mg}=5.0 \times 10^{-4} \mathrm{~kg} \\
v & =8.0 \mathrm{~ms}^{-1} \\
\mathrm{~h} & =6.63 \times 10^{-34} \mathrm{Js}
\end{aligned}
$$

Using $\quad \lambda=\frac{\mathrm{h}}{m c}=\frac{6.63 \times 10^{-34} \mathrm{Js}}{5.0 \times 10^{-6} \mathrm{~kg} \times 8.0 \mathrm{~ms}^{-1}}=1.66 \times 10^{-29} \mathrm{~m}$
Example 19.9: An electron is accelerated through a Potential Difference of 50 V . Calculate its de Broglie wavelength.

## $$
\begin{aligned}
m & =9.1 \times 10^{-31} \mathrm{~kg}, \quad V_{0}=50 \mathrm{~V} \\
\lambda & =?, \quad e=1.6 \times 10^{-19} \mathrm{C} \\
\frac{1}{2} m v^{2} & =V_{0} e \\
p & =m v=\sqrt{2 m V_{0} e}
\end{aligned}
$$

then $\quad \lambda=\frac{h}{p}=\frac{h}{\sqrt{2 m V_{0} e}}$

$$
\begin{aligned}
& =\frac{6.63 \times 10^{-34} \mathrm{Js}}{\sqrt{2 \times 9.1 \times 10^{-31} \mathrm{~kg} \times 50 \mathrm{JC}^{-1} \times 1.6 \times 10^{-19} \mathrm{C}}} \\
\lambda & =1.74 \times 10^{-10} \mathrm{~m}
\end{aligned}
$$

## Uses of Wave Nature of Particles

The fact that energetic particles have extremely short de Broglie wavelengths has been put to practical use in many ultra-modern devices of immense importance such as electron microscope.

Fig. 19.13

## Oo You Know?

In the subatomic world few things can be predicted with $100 \%$ precision.

## Electron Microscope

Electron microscope makes practical use of the wave nature of electrons which is thousands of time shorter than visible light which enables the electron microscope to distinguish details not visible with optical microscope. In an electron microscope, electric and magnetic fields rather than optical lenses are used to focus electrons by means of electromagnetic forces that are exerted on moving charges. The resulting deflections of the electrons beams are similar to the refraction effects produced by glass lenses used to focus light in optical microscope. The electrons are accelerated to high energies by applying voltage from 30 kV to several megavolts. Such high voltages give extremely short wavelength and also give the electron sufficient energy to penetrate specimen of reasonable thickness. A resolution of 0.5 to 1 nm is possible with a 50 kV microscope as compared to best optical resolution of $0.2 \mu \mathrm{~m}$. A schematic diagram of the electron microscope is shown in the Figure 19.13. The magnetic conducting lens concentrates the beam from an electron gun on to the specimen. Electrons are scattered out of the beam from the thicker parts of the specimen. The transmitted beam therefore has spatial differences in density that correspond to the features of the specimen. The objective and intermediate lenses produce a real intermediate image and projection lens forms the final image which can be viewed on a fluorescent screen or photographed on special film known as electron micrograph. A three dimensional image of remarkable quality can be achieved by modern versions called scanning electron microscopes.

### 19.8 UNCERTAINTY PRINCIPLE

Position and momentum of a particle cannot both be measured simultaneously with perfect accuracy. There is always a fundamental uncertainty associated with any measurement. This uncertainty is not associated with the measuring instrument. It is a consequence of the wave particle duality of matter and radiation. This was first proposed by Werner Heisenberg in 1927 and hence is known as Heisenberg Uncertainty Principle. This fundamental uncertainty is completely negligible for measurements of position and momentum of macroscopic objects but is a predominant fact of life in the atomic domain. For example, a stream of light photons scattering from a flying tennis ball

hardly affects its path, but one photon striking an electron drastically alters the electron's motion. Since light has also wave properties, we would expect to be able to determine the position of the electron only to within one wavelength of the light being used. Hence, in order to observe the position of an electron with less uncertainty and also for minimizing diffraction effect, we must use light of short wavelength. But it will alter the motion drastically making momentum measurement less precise. If light of wavelength $\lambda$ is used to locate a micro particle moving along $x$-axis, the uncertainty in its position measurement is

$$
\Delta x \approx \lambda
$$

At most, the photon of light can transfer all its momentum $\left(\frac{\mathrm{h}}{\lambda}\right)$ to the micro particle whose own momentum will then be uncertain by an amount

$$
\Delta p \approx \frac{\mathrm{~h}}{\lambda}
$$

Multiplying these two uncertainties gives

$$
\Delta x \cdot \Delta p \approx \lambda\left(\frac{\mathrm{~h}}{\lambda}\right) \approx \mathrm{h}
$$

The equation 19.19 is the mathematical form of uncertainty principle. It states that the product of the uncertainty $\Delta x$ in the position of a particle at some instant and the uncertainty $\Delta p$ in the $x$-component of its momentum at the same instant approximately equals Planck's constant $h$.
There is another form of uncertainty principle which relates the energy of a particle and the time at which it had the energy. If the $\Delta E$ is the uncertainty in our knowledge of the energy of our particle and if the time interval during which
the particle had the energy $E \pm \frac{\Delta E}{2}$ is $t_{0} \pm \frac{\Delta t}{2}$, then

$$
\Delta E \cdot \Delta t \approx h
$$

Thus more accurately we determined the energy of a particle, the more uncertain we will be of the time during which it has that energy.
According to Heisenberg's more careful calculations, he found that at the very best

You can never accurately describe all aspects of a subatomic particle at once.

and

$$
\begin{aligned}
& \Delta x \cdot \Delta p \geq h \\
& \Delta E \cdot \Delta t \geq h
\end{aligned}
$$

where

$$
h=\frac{h}{2 \pi}=1.05 \times 10^{-34} \mathrm{Js}
$$

Werner Karl Heisenberg received Nobel Prize for physics in 1932 for the development of quantum mechanics.

Example 19.10: The life time of an electron in an excited state is about $10^{-6} \mathrm{~s}$. What is its uncertainty in energy during this time?

# Using uncertainty principle

$$
\begin{aligned}
& \Delta E \cdot \Delta t \approx h \\
& \Delta E=\frac{h}{\Delta t}=\frac{1.05 \times 10^{-34} \mathrm{Js}}{10^{-8} \mathrm{~s}} \\
& \Delta E=1.05 \times 10^{-28} \mathrm{~J}
\end{aligned}
$$

Example 19.11: An electron is to be confined to a box of the size of the nucleus ( $1.0 \times 10^{-4} \mathrm{~m}$ ). What would the speed of the electron be if it were so confined?

## Maximum uncertainty in the location of electron equals the size of the box itself that is $\Delta x=1.0 \times 10^{-14} \mathrm{~m}$. The minimum uncertainty in the velocity of electron is found from Heisenberg uncertainty principle

$$
\Delta p \approx \frac{\mathrm{~h}}{\Delta x}
$$

or

$$
m \Delta v \approx \frac{\mathrm{~h}}{\Delta x}
$$

$$
\Delta v=\frac{h}{m \Delta x}=\frac{1.05 \times 10^{-34} \mathrm{Js}}{9.1 \times 10^{-31} \mathrm{~kg} \times 1.0 \times 10^{-14} \mathrm{~m}}=1.15 \times 10^{10} \mathrm{~m} \mathrm{~s}^{-1}
$$

For confinement in the box, the speed should be greater than the speed of light. Because this is not possible, we must conclude that an electron can never be found inside the nucleus.

# SUMMARY

- An inertial frame of reference is defined as a coordinate system in which the law of inertia is valid. A frame of reference that is not accelerating is an inertial frame of reference.
- The special theory of relatively treats problems involving inertial or non-accelerating frames of reference. It is based upon two postulates.
(i) The laws of physics are the same in all inertial frames.
(ii) The speed of light in free space has the same value for all observers, regardless of their state of motion.
$E=m c$ is an important result of special theory of relativity
- A black body is a solid block having a hollow cavity within it. It has small hole and the radiation can enter or escape only through this hole.
- Stephen Boltzmann law states that total energy radiated over all wave length at a particular temperature is directly proportional to the fourth power of that Kelvin temperature.
- The emission of electrons from a metal surface when exposed to ultraviolet light is called photoelectric effect. The emitted electrons are known as photoelectrons.
- When X-rays are scattered by loosely bound electrons from a graphite target, it is known as Compton effect.
- The change of very high energy photon into an electron, positron pair is called pair production.
- When a positron comes close to an electron, they annihilate and produce two photons in the $\gamma$-rays range. It is called annihilation of matter.
- Position and momentum of a particle cannot both be measured simultaneously with perfect accuracy. There is always a fundamental uncertainty associated with any measurement. It is a consequence of the wave particle duality of matter and radiation. It is known as Heisenberg uncertainty principle.

## QUESTIONS

19.1 What are the measurements on which two observers in relative motion will always agree upon?
19.2 Does the dilation means that time really passes more slowly in moving system or that it only seems to pass more slowly?
19.3 If you are moving in a spaceship at a very high speed relative to the Earth, would you notice a difference (a) in your pulse rate (b) in the pulse rate of people on Earth?

19.4 If the speed of light were infinite, what would the equations of special theory of relativity reduce to?
19.5 Since mass is a form of energy, can we conclude that a compressed spring has more mass than the same spring when it is not compressed?
19.6 As a solid is heated and begins to glow, why does it first appear red?
19.7 What happens to total radiation from a blackbody if its absolute temperature is doubled?
19.8 A beam of red light and a beam of blue light have exactly the same energy. Which beam contains the greater number of photons?
19.9 Which photon, red, green, or blue carries the most (a) energy and (b) momentum?
19.10 Which has the lower energy quanta? Radiowaves or X-rays
19.11 Does the brightness of a beam of light primarily depends on the frequency of photons or on the number of photons?
19.12 When ultraviolet light falls on certain dyes, visible light is emitted. Why does this not happen when infrared light falls on these dyes?
19.13 Will bright light eject more electrons from a metal surface than dimmer light of the same colour?
19.14 Will higher frequency light eject greater number of electrons than low frequency light?
19.15 When light shines on a surface, is momentum transferred to the metal surface?
19.16 Why can red light be used in a photographic dark room when developing films, but a blue or white light cannot?
19.17 Photon A has twice the energy of photon B. What is the ratio of the momentum of A to that of B?
19.18 Why don't we observe a Compton effect with visible light?
19.19 Can pair production take place in vacuum? Explain
19.20 Is it possible to create a single electron from energy? Explain.
19.21 If electrons behaved only like particles, what pattern would you expect on the screen after the electrons passes through the double slit?
19.22 If an electron and a proton have the same de Broglie wavelength, which particle has greater speed?
19.23 We do not notice the de Broglie wavelength for a pitched cricket ball. Explain why?
19.24 If the following particles have the same energy, which has the shortest wavelength? Electron, alpha particle, neutron, proton.
19.25 When does light behave as a wave? When does it behave as a particle?
19.26 What advantages an electron microscope has over an optical microscope?
19.27 If measurements show a precise position for an electron, can those measurements show precise momentum also? Explain.

# PROBLEMS

19.1 A particle called the pion lives on the average only about $2.6 \times 10^{-6} \mathrm{~s}$ when at rest in the laboratory. It then changes to another form. How long would such a particle live when shooting through the space at 0.95 c ?
[Ans. $8.3 \times 10^{-6} \mathrm{~s}$ ]
19.2 What is the mass of a 70 kg man in a space rocket traveling at 0.8 c from us as measured from Earth?
[Ans. 116.7 kg ]
19.3 Find the energy of photon in
(b) Radiowave of wavelength 100 m
(c) Green light of wavelength 550 nm
(d) X-ray with wavelength 0.2 nm
[Ans. (a) $1.24 \times 10^{-6} \mathrm{eV}$ (b) 2.25 eV (c) 6200 eV ]
19.4 Yellow light of 577 nm wavelength is incident on a cesium surface. The stopping voltage is found to be 0.25 V . Find
(a) the Maximum K.E. of the photoelectrons
(b) the work function of cesium
[Ans. (a) $4 \times 10^{-20} \mathrm{~J}$ (b) 1.91 eV ]
19.5 X-rays of wavelength 22 pm are scattered from a carbon target. The scattered radiation being viewed at $85^{\circ}$ to the incident beam. What is Compton shift?
[Ans. $2.2 \times 10^{-12} \mathrm{~m}$ ]
19.6 A 90 keV X-ray photon is fired at a carbon target and Compton scattering occurs. Find the wavelength of the incident photon and the wavelength of the scattered photon for scattering angle of (a) $30^{\circ}$ (b) $60^{\circ}$
[Ans. 13.8 pm (a) 14.1 pm (b) 15 pm ]
$19.7^{\circ}$ What is the maximum wavelength of the two photons produced when a positron annihilates an electron? The rest mass energy of each is 0.51 MeV .
[Ans. $2.44 \times 10^{-12} \mathrm{~m}$ ]
19.8 Calculate the wavelength of
(a) a 140 g ball moving at $40 \mathrm{~ms}^{-1}$
(b) a proton moving at the same speed
(c) an electron moving at the same speed
[Ans. (a) $1.18 \times 10^{-34} \mathrm{~m}$ (b) 9.92 nm (c) $1.82 \times 10^{-5} \mathrm{~m}$ ]
19.9 What is the de Broglie wavelength of an electron whose kinetic energy is 120 eV ?
[Ans. $1.12 \times 10^{-10} \mathrm{~m}$ ]
19.10 An electron is placed in a box about the size of an atom that is about $1.0 \times 10^{-10} \mathrm{~m}$. What is the velocity of the electron?
[Ans. $7.29 \times 10^{6} \mathrm{~ms}^{-1}$ ]

# ATOMIC SPECTRA

## Learning Objectives

At the end of this chapter the students will be able to:

1. Know experimental facts of hydrogen spectrum.
2. Describe Bohr's postulates of hydrogen atom.
3. Explain hydrogen atom in terms of energy levels.
4. Describe de-Brogile's interpretation of Bohr's orbits.
5. Understand excitation and ionization potentials.
6. Describe uncertainty regarding position of electron in the atom.
7. Understand the production, properties and uses of X-rays.
8. Describe the terms spontaneous emission, stimulated emission, metastable states and population inversion.
9. Understand laser principle.

10 Describe the He-Ne gas laser.
11. Describe the application of laser including holography.

The branch of physics that deals with the investigation of wavelengths and intensities of electromagnetic radiation emitted or absorbed by atoms is called spectroscopy. It includes the study of spectra produced by atoms. In general there are three types of spectra called (i) continuous spectra, (ii) band spectra, and (iii) discrete or line spectra.

Black body radiation spectrum, as described in chapter 19 is an example of continuous spectra; molecular spectra are the examples of band spectra while the atomic spectra, which we shall investigate in detail in this chapter, are examples of discrete or line spectra.

### 20.1 ATOMIC SPECTRA

When an atomic gas or vapour at much less than atmospheric pressure is suitably excited, usually by passing an electric current through it, the emitted radiation has a spectrum, which contains certain specific wavelengths only. An idealized arrangement for observing such atomic spectra is shown in Fig. 20.1. Actual spectrometer uses diffraction grating for better results.

The impression on the screen is in the form of lines if the slit in front of the source $S$ is narrow rectangle. It is for this reason that the spectrum is referred to as line spectrum.
The fact that the spectrum of any element contains wavelengths that exhibit definite regularities was utilized in the second half of the $19^{\circ}$ century in identifying different elements.

Fig. 20.1 Line spectrum of hydrogen
These regularities were classified into certain groups called the spectral series. The first such series was identified by J.J Balmer in 1885 in the spectrum of hydrogen. This series, called the Balmer series, is shown in Fig.20.2, and is in the visible region of the electromagnetic spectrum.

The results obtained by Balmer were expressed in 1896 by J.R Rydberg in the following mathematical form

$$
\frac{1}{\lambda}=R_{H}\left(\frac{1}{2^{2}}-\frac{1}{n^{2}}\right)
$$

where $R_{H}$ is the Rydberg's constant. Its value is $1.0974 \times 10^{7} \mathrm{~m}^{-1}$. Since then many more series have been discovered and proved helpful in predicting the arrangement of the electrons in different atoms.

# Atomic Spectrum of Hydrogen

The Balmer series contain wavelengths in the visible portion of the hydrogen spectrum. The spectral lines of hydrogen in the ultraviolet and infrared regions fall into several other series. In the ultraviolet region, the Lyman series contains the wavelengths given by the formula

$$
\frac{1}{\lambda}=R_{H}\left(\frac{1}{1^{2}}-\frac{1}{n^{2}}\right)
$$

where

$$
n=2,3,4, \ldots \ldots
$$

In the infrared region, three spectral series have been found whose lines have the wavelengths specified by the formulae:
Fig. 20.2

## Different types of spectra
(a) Continuous spectrum
(b) Line spectrum
(c) Band spectrum

Line spectrum of atomic hydrogen. Only the Balmer series lies in the visible region of the electromagnetic spectrum.

Paschen series

$$
\frac{1}{\lambda}=R_{H}\left(\frac{1}{3^{2}}-\frac{1}{n^{2}}\right)
$$

where $\quad n=4,5,6, \ldots \ldots$
Brackett series

$$
\frac{1}{\lambda}=R_{H}\left(\frac{1}{4^{2}}-\frac{1}{n^{2}}\right)
$$

where $\quad n=5,6,7, \ldots \ldots$
Pfund series

$$
\frac{1}{\lambda}=R_{H}\left(\frac{1}{5^{2}}-\frac{1}{n^{2}}\right)
$$

where $\quad n=6,7,8, \ldots \ldots$
The existence of these regularities in the hydrogen spectrum together with similar regularities in the spectra of more complex elements, proposes a definite test for any theory of atomic structure.

# 20.2 BOHR'S MODEL OF THE HYDROGEN ATOM

In order to explain the empirical results obtained by Rydberg, Neils Bohr, in 1913, formulated a model of hydrogen atom utilizing classical physics and Planck's quantum theory. This semi classical theory is based on the following three postulates:
Postulate I: An electron, bound to the nucleus in an atom, can move around the nucleus in certain circular orbits without radiating. These orbits are called the discrete stationary states of the atom.

Postulate II: Only those stationary orbits are allowed for which orbital angular momentum is equal to an integral multiple of $\frac{\mathrm{h}}{2 \pi}$ i.e.,

$$
m v r=\frac{\mathrm{nh}}{2 \pi}
$$

where $n=1,2,3, \ldots$ and $n$ is called the principal quantum number, $m$ and $v$ are the mass and velocity of the orbiting electron respectively, and $h$ is Planck's constant.

Postulate III: Whenever an electron makes a transition, that is, jumps from high energy state $E_{n}$ to a lower energy state $E_{p}$, a photon of energy $h$ fis emitted so that

$$
h f=E_{n}-E_{p}
$$

where $f=c / \lambda$ is the frequency of the radiation emitted.

# de-Broglie's Interpretation of Bohr's Orbits

At the time of formulation of Bohr's theory, there was no justification for the first two postulates, while Postulate III had some roots in Planck's thesis. Later on with the development of de Broglie's hypothesis, some justification could be seen in Postulate II as explained below:
Standing de Broglie waves of electrons around the circumference of Bohr orbits.
Consider a string of length $\ell$ as shown in Fig. 20.3 (a). If this is put into stationary vibrations, we must have $\ell=n \lambda$ where $n$ is an integer. Suppose that the string is bent into circle of radius $r$, as demonstrated for $n=3$ and $n=6$ in Fig. 20.3 (b) and (c), so that

$$
\begin{aligned}
& \ell=2 \pi r=n \lambda \\
& \lambda=\frac{2 \pi r}{n}
\end{aligned}
$$

From de Broglie's hypothesis

$$
\lambda=\frac{h}{p}=\frac{h}{m v}
$$

thus

$$
\frac{h}{m v}=\frac{2 \pi r}{n}
$$

or

$$
m v r=\frac{n h}{2 \pi}
$$

which is Postulate II.

## Helium was identified in the Sun using spectroscopy before it was discovered on earth.
(a)

Fig. 20.3 Stationary wave for $n=3$ on a string.

Fig. 20.4

## The first Bohr orbit in the hydrogên atom has a radius $r_{1}=5.3 \times 10^{-1} \mathrm{~m}$. The second and third Bohr orbits have radii $r_{2}=4 r_{1}$ and $r_{3}=9 r_{1}$ respectively.

## Quantized Radii

Consider a hydrogen atom in which electron moving with velocity $v_{n}$ is in stationary circular orbit of radius $r_{n}$. From Eq. (20.6),

$$
v_{n}=\frac{n h}{2 \pi m r_{n}}
$$

For this electron to stay in the circular orbit, shown in Fig. 20.4, the centripetal force $F_{c}=\frac{m v_{n}^{2}}{r_{n}}$ is provided by the Coulomb's force $F_{x}=\frac{k e^{2}}{r_{n}^{2}}$, where $e$ is the magnitude of charge on electron as well as on the hydrogen nucleus consisting of a single proton. Thus,

$$
\frac{m v_{n}^{2}}{r_{n}}=\frac{k e^{2}}{r_{n}^{2}}
$$

where constant $k$ is equal to $\frac{1}{4 \pi \varepsilon_{0}}$.
After substituting for $v_{n}$ from Eq. 20.9, we have

$$
r_{1}=\frac{n^{2} h^{2}}{4 \pi^{2} \mathrm{kme}^{2}}=n^{2} r_{1}
$$

where $r_{1}=\frac{h^{2}}{4 \pi^{2} \mathrm{kme}^{2}}=0.053 \mathrm{~nm}$
This agrees with the experimentally measured values and is called the first Bohr orbit radius of the hydrogen atom. Thus according to Bohr's theory, the radii of different stationary orbits of the electrons in the hydrogen atom are given by

$$
r_{n}=r_{1}, 4 r_{1}, 9 r_{1}, 16 r_{1}, \ldots \ldots
$$

Substituting the value of $r_{n}$ from Eq. 20.11 in Eq. 20.9, the speed of electron in the nth orbit is

$$
v_{n}=\frac{2 \pi k e^{2}}{n h}
$$

## Quantized Energies

Let us now calculate the total energy $E_{n}$ of the electron in the Bohr orbit; $E_{n}$ is the sum of the kinetic energy K.E. and the potential energy U.i.e.,

$$
E_{n}=\text { K.E. }+U=\frac{1}{2} m v_{n}^{2}+\left(\frac{-k e^{2}}{r_{n}}\right)
$$

By rearranging Eq. (20.10), we get

$$
\begin{gathered}
\frac{1}{2} m v_{n}^{2}=\frac{k e^{2}}{2 r_{n}} \\
E_{n}=\frac{k e^{2}}{2 r_{n}} \frac{k e^{2}}{r_{n}}=-\frac{k e^{2}}{2 r_{n}}
\end{gathered}
$$

By substituting the value of $r_{n}$ from Eq. (20.11), we have

$$
E_{n}=-\frac{1}{n^{2}}\left(\frac{2 \pi^{2} k^{2} m e^{4}}{h^{2}}\right)=-\frac{E_{0}}{n^{2}}
$$

where

$$
E_{0}=\frac{2 \pi^{2} k^{2} m e^{4}}{h^{2}}=\text { constant }=13.6 \mathrm{eV}
$$

which is the energy required to completely remove an electron from the first Bohr orbit. This is called ionization energy. The ionization energy may be provided to the electron by collision with an external electron. The minimum potential through which this external electron should be accelerated so that it can supply the requisite ionization energy is known as ionization potential. Thus for $n=1,2,3, \ldots$ we get the allowed energy levels of a hydrogen atom to be

$$
E_{n}=-E_{0},-\frac{E_{0}}{4},-\frac{E_{0}}{9},-\frac{E_{0}}{16}
$$

The experimentally measured value of the binding energy of the electron in the hydrogen atom is in perfect agreement with the value predicted by Bohr theory.
Normally the electron in the hydrogen atom is in the lowest energy state corresponding to $n=1$ and this state is called the ground state or normal state. When it is in higher orbit, it is said to be in the excited state. The atom may be exited by collision with externally accelerated electron. The potential through which an electron should be accelerated so that, on collision it can lift the electron in the atom from its ground state to some higher state, is known as excitation potential.

# Hydrogen Emission Spectrum

The results derived above for the energy levels along with Postulate III can be used to arrive at the expression for the wavelength of the hydrogen spectrum. Suppose that the electron in the hydrogen atom is in the excited state $n$ with

## Photon must have energy exactly equal to the energy difference between the two shells for excitation of an atom but an electron with K.E greater that the required difference can excite the gas atoms.
Fig. 20.5 Energy level diagram for the hydrogen atom.
energy $E_{n}$ and makes a transition to a lower state $p$ with energy $E_{p}$, where $E_{p}<E_{n}$, then
where

$$
E_{n}=-\frac{E_{0}}{n^{2}} \quad \text { and } \quad E_{p}=-\frac{E_{0}}{p^{2}}
$$

hence

$$
h f=-E_{n}\left(\frac{1}{n^{2}}-\frac{1}{p^{2}}\right)
$$

Substituting for $f=c / \lambda$ and rearranging

$$
\frac{1}{\lambda}=\frac{E_{0}}{h c}\left(\frac{1}{p^{2}}-\frac{1}{n^{2}}\right)
$$

or

$$
\frac{1}{\lambda}=R_{H}\left(\frac{1}{p^{2}}-\frac{1}{n^{2}}\right)
$$

where $R_{H}$ is the Rydberg constant given by the equation

$$
R_{H}=\frac{E_{0}}{h c}=1.0974 \times 10^{7} \mathrm{~m}^{-1}
$$

which agrees well with the latest measured value for hydrogen atom.
Eq. 20.17 reduces to the empirical result derived by Rydberg and given by Eq 20.1, provided that we substitute $p=2$ and $n=3,4,5, \ldots \ldots$ The different energy levels corresponding to Eq. 20.17 are shown in Fig. 20.5.

Example 20.1: Find the speed of the electron in the first Bohr orbit.

## The speed found from Eq. (20.12) with $n=1$, is

$$
\begin{gathered}
v_{1}=\frac{2 \pi \mathrm{ke}^{2}}{\mathrm{~h}}=2 \times 3.14 \times\left(9 \times 10^{6} \mathrm{Nm}^{2} \mathrm{C}^{-2}\right)\left(\frac{\left(1.6 \times 10^{-19} \mathrm{C}\right)^{2}}{6.63 \times 10^{-34} \mathrm{Js}}\right) \\
v_{1}=2.19 \times 10^{6} \mathrm{~ms}^{-1}
\end{gathered}
$$

### 20.3 INNER SHELL TRANSITIONS AND CHARACTERISTIC X-RAYS

The transitions of electrons in the hydrogen or other light elements result in the emission of spectral lines in the infrared, visible or ultraviolet region of electromagnetic spectrum due to small energy differences in the transition levels.

In heavy atoms, the electrons are assumed to be arranged in concentric shells labeled as $\mathrm{K}, \mathrm{L}, \mathrm{M}, \mathrm{N}, \mathrm{O}$ etc., the K shell being closest to the nucleus, the $L$ shell next, and so on (Fig. 20.6). The inner shell electrons are tightly bound and large amount of energy is required for their displacement from their normal energy levels. After excitation, when an atom returns to its normal state, photons of larger energy are emitted. Thus transition of inner shell electrons in heavy atoms gives rise to the emission of high energy photons or Xrays. These X-rays consist of series of specific wavelengths or frequencies and hence are called characteristic X-rays. The study of characteristic $X$-rays spectra has played a very important role in the study of atomic structure and the periodic table of elements.

# Production of X-rays

Fig. 20.7 shows an arrangement of producing X-rays. It consists of a high vacuum tube called X-ray tube. When the cathode is heated by the filament $F$, it emits electrons which are accelerated towards the anode T. If $V$ is the
Incident
high energy
electron
Fig. 20.6
potential difference between $C$ and $T$, the kinetic energy $K . E$. with which the electron strike the target is given by

$$
\text { K.E. }=\text { Ve }
$$

Suppose that these fast moving electrons of energy Ve strike a target made of tungsten or any other heavy element. It is possible that in collision, the electrons in the innermost shells, such as K or L , will be knocked out. Suppose that one of the electrons in the K shell is removed, thereby producing a vacancy or hole in that shell. The electron from the $L$ shell

Fig. 20.8
jumps to occupy the hole in the K shell, thereby emitting a photon of energy h $f_{\text {ho }}$ called the $\mathrm{K}_{\mathrm{s}} \mathrm{X}$-ray given by

$$
\mathrm{h} f_{\mathrm{ho}}=E_{\mathrm{L}}-E_{\mathrm{K}}
$$

It is also possible that the electron from the $M$ shell might also jump to occupy the hole in the K shell. The photons emitted are $\mathrm{K}_{2} \mathrm{X}$-ray with energies

$$
\mathrm{h} f_{\mathrm{k} 2}=E_{\mathrm{M}}-E_{\mathrm{K}}
$$

these photons give rise to $\mathrm{K}_{2} \mathrm{X}$-ray and so on.
The photons emitted in such transitions i.e., inner shell transitions are called characteristic X-rays, because their energies depend upon the type of target material.
The holes created in the $L$ and $M$ shells are occupied by transitions of electrons from higher states creating more X-rays. The characteristic X-rays appear as discrete lines on a continuous spectrum as shown in Fig. 20.8.

# The Continuous X-ray Spectrum

The continuous spectrum is due to an effect known as bremsstrahlung or braking radiation. When the fast moving electrons bombard the target, they are suddenly slowed down on impact with the target. We know that an accelerating charge emits electromagnetic radiation. Hence, these impacting electrons emit radiation as they are strongly decelerated by the target. Since the rate of deceleration is so large, the emitted radiation correspond to short wavelength and so the bremsstrahlung is in the X-ray region. In the case when the electrons lose all their kinetic energy in the first collision, the entire kinetic energy appears as a X-ray photon of energy $\mathrm{h} f_{\text {max }}$, i.e.,

$$
\mathrm{K} . \mathrm{E} .=\mathrm{h} f_{\max }
$$

The wavelength $\lambda_{\text {min }}$ in Fig. 20.8 corresponds to frequency $f_{\text {max }}$. Other electrons do not lose all their energy in the first collision. They may suffer a number of collisions before coming to rest. This will give rise to photons of smaller energy or X-rays of longer wavelength. Thus the continuous spectrum is obtained due to deceleration of impacting electrons.

## Properties and Uses of X-rays

X-rays have many practical applications in medicine and industry. Because X-rays can penetrate several centimetres

into a solid matter, so they can be used to visualize the interiors of the materials opaque to ordinary light, such as fractured bones or defects in structural steel. The object to be visualized is placed between an X-ray source and a large sheet of photographic film; the darkening of the film is proportional to the radiation exposure. A crack or air bubble allows greater amount of X-rays to pass. This appears as a dark area on the photographic film. Shadow of bones appears lighter than the surrounding flesh. It is due to the fact that bones contain greater proportions of elements with high atomic number and so they absorb greater amount of incident X-rays than flesh. In flesh, light elements like carbon, hydrogen and oxygen predominate. These elements allow greater amount of incident X-rays to pass through them.

## CAT-Scanner

In the recent past, several vastly improved X-ray techniques have been developed. One widely used system is computerized axial tomography; the corresponding instrument is called CAT-Scanner. The X-ray source produces a thin fan-shaped beam that is detected on the opposite side of the subject by an array of several hundred detectors in a line. Each detector measures absorption of X-ray along a thin line through the subject. The entire apparatus is rotated around the subject in the plane of the beam during a few seconds. The changing reactions of the detector are recorded digitally; a computer processes this information and reconstructs a picture of different densities over an entire cross section of the subject. Density differences of the order of one percent can be detected with CAT-Scans. Tumors, and other anomalies much too small to be seen with older techniques can be detected.

## Biological Effects of X-rays

X-rays cause damage to living tissue. As X-ray photons are absorbed in tissues, they break molecular bonds and create highly reactive free radicals (such as H and OH ), which in turn can disturb the molecular structure of the proteins and especially the genetic material. Young and rapidly growing cells are particularly susceptible; hence X-rays are useful for selective destruction of cancer cells. On the other hand a cell may be damaged by radiation but survive, continue dividing and produce generation of defective cells. Thus X-rays can cause cancer. Even when the organism itself shows no apparent damage, excessive

An X-ray picture of a hand.

'In CAT scanning a "fanned-out" array of X-ray beams is directed through the patient from a number of different orientations.

(a)
(b)
(a) This two-dimensional CAT scan of a brain reveals a large intracranial tumor (colored purple). (b) Threedimensional CAT scans are now available and this example reveals an arachnoid cyst ( colored yellow) within a skull. In both photographs the colors are artificial having been computer generated to aid in distinguishing anatomical features.
radiation exposure can cause changes in their productive system that will affect the organism's offspring.

### 20.4 UNCERTAINTY WITHIN THE ATOM

One of the characteristics of dual nature of matter is a fundamental limitation in the accuracy of the simultaneous measurement of the position and momentum of a particle.
Heisenberg showed that this is given by the equation

$$
\Delta p \Delta x \geq \frac{h}{2 \pi}
$$

However, these limitations are significant in the realm of atom. One interesting question is whether electrons are present in atomic nuriei. As the typical nuclei are less than $10^{-14} \mathrm{~m}$ in diameter, for an electroh to be confined within such a nucleus, the uncertainty in its position is of the order of $10^{-14} \mathrm{~m}$. The corresponding uncertainty in the electron's momentum is

$$
\begin{gathered}
\Delta p \geq \frac{h}{\Delta x} \\
\geq \frac{6.63 \times 10^{-34} \mathrm{Js}}{10^{-14} \mathrm{~m}}=6.63 \times 10^{39} \mathrm{~kg} \mathrm{~ms}^{-1}
\end{gathered}
$$

As

$$
\Delta p=m \Delta v
$$

Hence

$$
\Delta v=\frac{6.63 \times 10^{-20} \mathrm{~kg} \mathrm{~ms}^{-1}}{9.11 \times 10^{-31} \mathrm{~kg}} \geq 7.3 \times 10^{10} \mathrm{~ms}^{-1}
$$

Hence, for the electron to be confined to a nucleus, its speed would have to be greater than $10^{10} \mathrm{~ms}^{-1}$ i.e., greater than the speed of light. Because this is impossible, we must conclude that an electron can never be found inside of a nucleus. But can an electron reside inside the atom? To find this, we again calculate the speed of an electron and if it turns to be less than the speed of light, we have reasonable expectation of finding the electron within the atom but outside the nucleus. The radius of the hydrogen atom is about $5 \times 10^{-11} \mathrm{~m}$. Applying the uncertainty principle to the momentum of electron in the atom we have

As

$$
\begin{aligned}
& \Delta p \geq \frac{h}{\Delta x} \\
& \Delta p=m \Delta v \\
& \Delta v=\frac{h}{m \Delta x}
\end{aligned}
$$

Therefore,

For an atom $\Delta x$ is given as $5 \times 10^{-11} \mathrm{~m}$
Thus

$$
\begin{aligned}
\Delta v & =\frac{6.63 \times 10^{-34} \mathrm{Js}}{9.11 \times 10^{-31} \mathrm{~kg} \times 5 \times 10^{-11} \mathrm{~m}} \\
& =1.46 \times 10^{7} \mathrm{~ms}^{-1}
\end{aligned}
$$

This speed of the electron is less than the speed of light, therefore, it can exist in the atom but outside the nucleus.

# 20.5 LASER

Laser is the acronym for Light Amplification by Stimulated Emission of Radiation. As the name indicates, lasers are used for producing an intense, monochromatic, and unidirectional coherent beam of visible light. To understand the working of a laser, terms such as stimulated emission and population inversion must be understood.

## Spontaneous and Stimulated Emissions

Consider a sample of free atoms some of which are in the ground state with energy $E_{1}$ and some in the excited state $E_{2}$ as shown in Fig. 20.9. The photons of energy h $f=E_{2}-E_{1}$ are incident on this sample. These incident photons can interact with atoms in two different ways. In Fig. 20.9 (a) the incident photon is absorbed by an atom in the ground state $E_{1}$, thereby leaving the atom in the excited state $E_{2}$. This process is called stimulated or induced absorption. Once in the excited state, two things can happen to the atom. (i) It may decay by spontaneous emission as shown in Fig. 20.9 (b), in which the atom emits a photon of energy h $f=E_{2}-E_{1}$ in any arbitrary direction.

The other alternative for the atom in the excited state $E_{2}$ is to decay by stimulated or induced emission as shown in Fig. 20.9 (c). In this case the incident photon of energy h $f=E_{2}-E_{1}$ induces the atom to decay by emitting a photon that travels in the direction of the incident photon. For each incident photon we will have two photons going in the same direction thus we have accomplished two things; an amplified as well as a unidirectional coherent beam. From a practical point this is possible only if there is more stimulated or induced emission than spontaneous emission. This can be achieved as described in the next section.
Fig 20.9

# Population Inversioa and Laser Action

Let us consider a simple case of a material whose atoms can reside in three different states as shown in Fig. 20.10, state
Fig. 20.10

## E.
(Larger energy)
E.
(Smaller energy)
(a) Normal population

A normal population of atomic energy state, with more atomic in the lower energy state $E_{2}$ than in the excited state $E_{2}$.
(b) Population inversion

A population inversion, in which the higher energy state has a greater population than the lower energy state.
$E$, which is ground state; the excited state $E_{1}$, in which the atoms can reside only for $10^{-5} \mathrm{~s}$ and the metastable state $E_{1}$, in which the atoms can reside for $\sim 10^{-5} \mathrm{~s}$. much longer than $10^{-5} \mathrm{~s}$. A metastable state is an excited state in which an excited electron is unusually stable and from which the electron spontaneously falls to lower state only after relatively longer time. The transition from or to this state are difficult as compared to other excited states. Hence, instead of direct excitation to this state, the electrons are excited to higher level for spontaneous fall to metastable state. Also let us assume that the incident photons of energy h $f=E_{1}-E_{1}$ raise the atom from the ground state $E_{1}$ to the excited state $E_{2}$, but the excited atoms do not decay back to $E_{1}$. Thus the only alternative for the atoms in the excited state $E_{2}$ is to decay spontaneously to state $E_{2}$, the atoms reach state $E_{2}$ much faster than they leave state $E_{2}$. This eventually leads to the situation that the state $E_{2}$ contains more atoms than state $E_{1}$. This situation is known as population inversion.

Once the population inversion has been reached, the lasing action of a laser is simple to achieve. The atoms in the metastable state $E_{2}$ are bombarded by photons of energy $\mathrm{h} f=E_{2}-E_{1}$, resulting in an induced emission, giving an intense, coherent beam in the direction of the incident photon.

The emitted photons must be confined in the assembly long enough to stimulate further emission from other excited atoms. This is achieved by using mirrors at the two ends of the assembly. One end is made totally reflecting, and the other end is partially transparent to allow the laser beam to escape (Fig.20.11). As the photons move back and forth between the reflecting mirrors they continue to stimulate other excited atoms to emit photons. As the process continues the number of photons multiply, and the resulting radiation is, therefore, much more intense and coherent than light from ordinary sources.

# Helium-Neon Laser

It is a most common type of lasers used in physics laboratories. Its discharge tube is filled with $85 \%$ helium and $15 \%$ neon gas. The neon is the lasing or active medium in this tube. By chance, helium and neon have nearly identical metastable states, respectively located 20.61 eV and 20.66 eV level. The high voltage electric discharge excites the electrons in some of the helium atoms to the 20.61 eV state. In this laser, population inversion in neon is achieved by direct collisions with same energy electrons of helium atoms. Thus excited helium atoms collide with neon atoms, each transferring its own 20.61 eV of energy to an electron in the neon atom along with 0.05 eV of K.E. from the moving atom. As a result, the electrons in neon atoms are raised to the 20.66 eV state. In this way, a population inversion is sustained in the neon gas relative to an energy level of 18.70 eV . Spontaneous emission from neon atoms initiate laser action and stimulated emission causes electrons in the neon to drop from 20.66 eV to the 18.70 eV level and red laser light of wavelength 632.8 nm corresponding to 1.96 eV energy is generated (Fig. 20.12).

## Uses of Laser in Medicine and Industry

1. Laser beams are used as surgical tool for "welding" detached retinas.
2. The narrow intense beam of laser can be used to destroy tissue in a localized area. Tiny organelles with a living cell have been destroyed by using laser to study how the absence of that organelle affects the behavior of the cell.
3. Finely focused beam of laser has been used to destroy cancerous and pre-cancerous cell.
Fig. 20.12

The helium-neon laser beam is being used to diagnose diseases of the eye. The use of laser technology in the field of ophthalmology is widespread.
4. The heat of the laser seals off capillaries and lymph vessels to prevent spread of the disease.
5. The intense heat produced in small area by a laser beam is also used for welding and machining metals and for drilling tiny holes in hard materials.
6. The precise straightness of a laser beam is also useful to surveyors for lining up equipment especially in inaccessible locations.
7. It is potential energy source for inducing fusion reactions.
8. It can be used for telecommunication along optical fibres.
9. Laser beam can be used to generate threedimensional images of objects in a process called holography.

## SUMMARY

- When an atomic gas or vapours at less than atmospheric pressure is suitably excited, usually by passing electric current through it, the emitted radiation has a spectrum which contains certain specific wavelenghts only.
- Postulates of Bohr's model of hydrogen atom are:
i. An electron, bound to the nucleus in an atom, can move around the nucleus in certain circular orbits without radiating. These orbits are callid the discrete stationary states of the atom.
ii. Only those stationary states are allowed for which orbital angular momentum is equal to an integral multiple of h i.e., $m v r=\frac{\pi h}{2 \pi}$
iii. Whenever an electron makes a transition, i.e., jumps from high energy state $E_{n}$ to a lower energy state $E_{p}$, a photon of energy $h f$ is emitted so that $h f=E_{n}-E_{p}$.
- The transition of electrons in the hydrogen or other light elements result in the emission of spectral lines in the infrared, visible or ultraviolet region of electromagnetic spectrum due to small energy differences in the transition levels.
- The X-rays emitted in inner shell transitions are called characteristic X-rays, because their energy depends upon the type of target material.
- The X-rays that are emitted in all directions and with a continuous range of frequencies are known as continuous X-rays.
- Laser is the acronym for Light Amplification by Stimulated Emission of Radiation.

The incident photon absorbed by an atom in the ground state $E_{1}$, thereby leaving the atom in the excited state $E_{2}$ is called stimulated or induced absorption.

Spontaneous or induced emission is that in which the atom emits a photon of energy $\mathrm{h} f=E_{2}-E_{1}$ in any arbitrary direction.

Stimulated or induced emission is that in which the incident photon of energy h $f=E_{2}-E_{1}$ induces the atom to decay by emitting a photon that travels in the direction of the incident photon. For each incident photon, we will have two photons going in the same direction giving rise to an amplified as well as a unidirectional coherent beam.

# QUESTIONS

20.1 Bohr's theory of hydrogen atom is based upon several assumptions. Do any of these assumptions contradict classical physics?
20.2 What is meant by a line spectrum? Explain, how line spectrum can be used for the identification of elements?
20.3 Can the electron in the ground state of hydrogen absorb a photon of energy 13.6 eV and greater than 13.6 eV ?
20.4 How can the spectrum of hydrogen contain so many lines when hydrogen contains one electron?
20.5 Is energy conserved when an atom emits a photon of light?
20.6 Explain why a glowing gas gives only certain wavelengths of light and why that gas is capable of absorbing the same wavelengths? Give a reason why it is transparent to other wavelengths?
20.7 What do we mean when we say that the atom is excited?
20.8 Can X-rays be reflected, refracted, diffracted and polarized just like any other waves? Explain.
20.9 What are the advantages of lasers over ordinary light?
20.10 Explain why laser action could not occur without population inversion between atomic levels?

## PROBLEMS

20.1 A hydrogen atoms is in its ground state ( $n=1$ ). Using Bohr's theory, calculate (a) the radius of the orbit, (b) the linear momentum of the electron, (c) the angular momentum of the electron (d) the kinetic energy (e) the potential.energy, and (f) the total energy.
[Ans: (a) $0.529 \times 10^{-10} \mathrm{~m}$ (b) $1.99 \times 10^{-24} \mathrm{~kg} \mathrm{~ms}^{-1}$ (c) $1.05 \times 10^{-34} \mathrm{~kg} \mathrm{~m}^{2} \mathrm{~s}^{-1}$
(d) 13.6 eV (e) - 27.2 eV (f) -13.6 eV$]$

20.2 What are the energies in eV of quanta of wavelength? $\lambda=400,500$ and 700 nm . (Ans: $3.10 \mathrm{eV}, 2.49 \mathrm{eV}, 1.77 \mathrm{eV}$ )
20.3 An electron jumps from a level $E_{1}=-3.5 \times 10^{-19} \mathrm{~J}$ to $E_{1}=-1.20 \times 10^{-19} \mathrm{~J}$. What is the wavelength of the emitted light?
(Ans: 234 nm )
20.4 Find the wavelength of the spectral line corresponding to the transition in hydrogen from $n=6$ state to $n=3$ state?
(Asn: 1094 nm )
20.5 Compute the shortest wavelength radiation in the Balmer series? What value of $n$ must be used?
(Ans: $364.5 \mathrm{~nm}, n=\infty$ )
20.6 Calculate the longest wavelength of radiation for the Paschen series.
(Ans: 1875 nm )
20.7 Electrons in an X-ray tube are accelerated through a potential difference of 3000 V . If these electrons were slowed down in a target, what will be the minimum wavelength of X-rays produced?
(Ans: $4.14 \times 10^{-10} \mathrm{~m}$ )
20.8 The wavelength of K X-ray from copper is $1.377 \times 10^{-10} \mathrm{~m}$. What is the energy difference between the two levels from which this transition results?
(Ans: 9.03 keV )
20.9 A tungsten target is struck by electrons that have been accelerated from rest through 40 kV potential difference. Find the shortest wavelength of the bremsstrahlung radiation emitted.
(Ans: $0.31 \times 10^{-10} \mathrm{~m}$ )
20.10 The orbital electron of a hydrogen atom moves with a speed of $5.456 \times 10^{1} \mathrm{~ms}^{-1}$ (a) Find the value of the quantum number $n$ associated with this electron. (b) Calculate the radius of this orbit.
(c) Find the energy of the electron in this orbit.
(Ans: $n=4, r_{e}=0.846 \mathrm{~nm} ; E_{e}=-0.85 \mathrm{eV}$ )