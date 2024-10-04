# Maximum-Rate Optimization of Hybrid Intelligent Reflective Surface and Relay Systems 

Alberto Rech, Federico Moretto, and Stefano Tomasin<br>Department of Information Engineering, University of Padova, Italy.<br>Emails: rechalbert@dei.unipd.it, federico.moretto.1@unipd.it, tomasin@dei.unipd.it


#### Abstract

We consider a wireless communication system, where a transmitting source is assisted by both a reconfigurable intelligent reflecting surface (IRS) and a decode-and-forward half-duplex relay (hybrid IRS-relay scheme) to communicate with a destination receiver. All devices are equipped with multiple antennas, and transmissions occur in two stages. In stage 1, the source splits the transmit message into two sub-messages, transmitted to the destination and the relay, respectively, using block diagonalization to avoid interference. Both transmissions will benefit from the IRS. In stage 2 , the relay re-encodes the received sub-message and forwards it (still through the IRS) to the destination. We optimize power allocations, beamformers, and configurations of the IRS in both stages, in order to maximize the achievable rate at the destination. We compare the proposed hybrid approach with other schemes (with/without relay and IRS), and confirm that high data rate is achieved for the hybrid scheme in case of optimal IRS configurations.


Index Terms-Beamforming, IRS, MIMO, rate optimization, relay.

## I. INTRODUCTION

A reconfigurable intelligent reflecting surface (IRS) is a programmable metasurface that can alter the phase and amplitude of an impinging signal by dynamically adjusting the reflection coefficients of its elements. Recently, IRSs have drawn enormous research interest as a promising technology for the sixth generation ( 6 G ) of cellular networks [1], due to their ability of controlling the wireless propagation environment. Before the advent of IRSs, relays have been studied and used in cellular networks to increase coverage and improve the received signal quality. Among various solutions, decode-and-forward (DF) relays are half-duplex (HD) devices that alternate two stages, one wherein they receive a message from the source, and a second wherein they re-encode the message and transmit it to the destination.
The alternative use of IRSs and relays has been widely investigated. In [2], IRSs and single-antenna DF relays are compared in terms of power consumption, whereas in [3] the energy efficiency of systems using IRSs is compared to a system with multi-antenna amplify-and-forward (AF) relays. A comparison between IRSs and DF HD/full-duplex (FD) relays is presented in [4], proving that sufficiently large IRSs yield higher spectral and energy efficiency than relay-aided systems. Nevertheless, due to the expensive deployment of IRSs, hybrid IRS-relay systems, wherein both devices are jointly adopted, will be a cost-effective solution for the near future of smart electromagnetic environments. In [5], the combination of a HD DF relay and an IRS is investigated and tight upper bounds for the achievable rate (AR) are derived. A hybrid system with a FD DF relay is studied in [6], showing that the performance further improves, as long as the relay self-interference is low. However, both works consider source and destination equipped with a single antenna each. In [7], a system wherein an IRS assists both a relay and a destination (and the source has no direct link with either the relay and the destination) is considered, with source, relay, and destination again having all one antenna each. For a system with multiple relays, still in the presence of an IRS, the selection of one relay to assist communication between a source and a destination is solved by machine-learning in [8].

In this paper, we consider a hybrid IRS-relay multipleinput multiple-output (MIMO) system, which generalizes the systems considered in [5], [6], and [7], as we now assume that all devices are equipped with multiple antennas. Moreover, contrary to [7], we also consider the link between the source and the relay. The relay is HD and operates in the DF mode. We propose a transmission protocol operating in two stages. In stage 1, the source splits the transmit message into two sub-messages, transmitted to the destination and the relay, respectively, using block diagonalization to avoid interference. Both transmissions will benefit from the IRS. In stage 2, the relay re-encodes the received sub-message and forwards it (still through the IRS) to the destination. We optimize power allocations, beamformers, and configurations of the IRS in both stages, to maximize the AR at the destination. In particular, we split the AR optimization problem into two subproblems, one for each stage, then coupled by the choice of the IRS configuration and the power split between the signal for the relay and the destination in stage 1 . Lastly, we compare the proposed hybrid approach with other schemes (with/without relay and IRS), and confirm that a high data rate is achieved for the hybrid scheme in case of optimal IRS configuration.

The rest of this paper is organized as follows. Section II describes transmission characteristics and the two-stage protocol. In Section III we formalize the maximum-rate optimization problem and describe the alternating optimization solution. In Section IV we discuss numerical results before the conclusions are taken in Section V.

Notation:Scalars are denoted by italic letters, vectors and matrices by boldface lowercase and uppercase letters, respectively, and sets are denoted by calligraphic uppercase letters. $\operatorname{diag}(a)$ indicates a square diagonal matrix with the elements of $a$ on the principal diagonal. $A^{\mathrm{H}}$ denotes the conjugate





Figure 1. Two-stage IRS- and relay-assisted MIMO system. Solid arrows represent the S-D link in stage 1, dashed arrows the S-R link in stage 1, and dotted arrows the R-D link in stage 2.
transpose of matrix $\mathbf{A} . \mathbb{E}[\cdot]$ denotes the statistical expectation. $\mathbf{I}_{x}$ is the identity matrix of size $x$.

## II. SYSTEM MODEL

We consider the narrowband single-user MIMO communication system shown in Fig. 1, wherein the transmission from a source $(\mathbf{S})$ to a destination $(\mathbf{D})$ is assisted by both a relay $(\mathbf{R})$ and an IRS $(\mathbf{I})$. We assume that $\mathbf{S}$ and $\mathbf{R}$ have maximum transmit powers $P_{\mathbf{S}}$ and $P_{\mathbf{R}}$, respectively.

S, D, and R are equipped with uniform linear arrays (ULAs) with $N_{\mathbf{S}}, N_{\mathbf{D}}$, and $N_{\mathbf{R}}$ antennas, respectively, whereas I is a uniform planar array (UPA) with $N_{\mathrm{I}}$ passive reflective elements.

We denote with $\mathbf{H}_{\mathbf{S I}} \in \mathbb{C}^{N_{\mathrm{I}} \times N_{\mathbf{S}}}$ and $\mathbf{H}_{\mathbf{S R}} \in \mathbb{C}^{N_{\mathbf{R}} \times N_{\mathbf{S}}}$ the S-R and S-I channels, with $\mathbf{H}_{\mathbf{R I}} \in \mathbb{C}^{N_{\mathrm{I}} \times N_{\mathbf{R}}}$ and $\mathbf{H}_{\mathbf{R D}} \in$ $\mathbb{C}^{N_{\mathbf{D}} \times N_{\mathbf{R}}}$ the R-I and R-D channels, and with $\mathbf{H}_{\mathbf{I R}}=\mathbf{H}_{\mathbf{R I}}^{H}$ and $\mathbf{H}_{\mathbf{I D}} \in \mathbb{C}^{N_{\mathbf{D}} \times N_{\mathbf{I}}}$ the I-R and I-D channels. We consider narrowband mmWave channels [9], each having $M$ non-lineof-sight (NLOS) components. Hence, channel matrix $\mathbf{H}_{\mathbf{X Y}}$ between transmitter $\mathbf{X}$ and receiver $\mathbf{Y}$ is

$$
\mathbf{H}_{\mathbf{X} \mathbf{Y}}=\frac{1}{\sqrt{M}} \sum_{m=1}^{M} g_{m} \rho(d) \mathbf{a}\left(\omega_{\mathbf{X}, m}\right) \mathbf{a}^{H}\left(\omega_{\mathbf{Y}, m}\right)
$$

where $g_{m} \sim \mathcal{C N}(0,1)$ is the gain of the $m$-th path, $\rho(d)$ is the path loss attenuation factor, with $d$ being the distance between $\mathbf{X}$ and $\mathbf{Y}, \omega_{., m}=\left(\xi_{., m}, \psi_{., m}\right)$ is the vector of azimuth $\left(\xi_{., m}\right)$ and elevation $\left(\psi_{., m}\right)$ angles, and $\mathbf{a}\left(\omega_{., m}\right)=$ $\left(1, \ldots, e^{j \pi\left[x \sin \left(\psi_{., m}\right) \cos \left(\xi_{., m}\right)+y \sin \left(\psi_{., m}\right) \sin \left(\xi_{., m}\right)\right]}, \ldots\right)^{T}$ is the array response vector for the $m$-th path, with $1 \leq x \leq N_{\mathbf{X}}-1$ and $1 \leq y \leq N_{\mathbf{Y}}-1$. We assume all devices operate in HD and have perfect channel state information.

## A. IRS Model

Each element of the IRS acts as an omnidirectional antenna element that captures and reflects signals, introducing an attenuation and a phase shift on the baseband-equivalent signal. Following the model of [10], we denote with $\phi_{n}=A_{n}\left(\theta_{n}\right) e^{j \theta_{n}}$ the reflection coefficient of the $n$-th IRS element, where $\theta_{n} \in[-\pi, \pi)$ is the induced phase shift and $A_{n}^{2}\left(\theta_{n}\right) \in[0,1]$ is the corresponding power attenuation factor. Indicating with $\mathbf{x} \in \mathbb{C}^{1 \times N_{\mathbf{I}}}$ the impinging signal on the IRS, the reflected signal $\mathbf{y} \in \mathbb{C}^{1 \times N_{\mathbf{I}}}$ is $\mathbf{y}=\boldsymbol{\Phi} \mathbf{x}$, with $\boldsymbol{\Phi}=\operatorname{diag}\left(\phi_{1}, \ldots, \phi_{N_{\mathbf{I}}}\right)$, which is the IRS reflection matrix, also denoted IRS configuration.

We consider the realistic baseband-equivalent model of the IRS described in [10], where

$$
\begin{array}{r}
A_{n}\left(\theta_{n}\right)=\left(1-A_{\text {min }}\right)\left(\frac{\sin \theta_{n}-\zeta+1}{2}\right)^{v}+A_{\min } \\
\text { with } \quad A_{\min } \geq 0, \quad \zeta \geq 0, \text { and } v \geq 0 \quad \text { being } \text { IRS-specific } \\
\text { parameters, assumed to be identical for all IRS elements. }
\end{array}
$$

The phase shifts $\theta_{n}$ are controllable, thus indirectly controlling also the attenuations. Moreover, since continuousphase shifts are hardly implementable [11]-[12], we assume that the phase shifts are chosen from a discrete set $\mathcal{F}_{\theta}=$ $\left\{0, \frac{2 \pi}{2^{b}}, \ldots, \frac{2 \pi\left(2^{b}-1\right)}{2^{b}}\right\}$, where $b>0$ is the IRS phase shift resolution, i.e., the number of bits employed to control the phase shifts. The source has full control of the phase shifts, which can be optimized together with beamforming.

## B. Two-stage Communication Protocol

For a HD DF relay, signal reception and transmission have to occur in two stages, here assumed to be of the same duration.

Stage 1: S splits the message into two sub-messages, and encodes/modulates them into the two signals $\mathbf{x}_{\mathrm{SR}}$ and $\mathbf{x}_{\mathrm{SD}}$, intended for $\mathbf{R}$ and $\mathbf{D}$, respectively. The two signals are precoded with block diagonalization (BD) precoders $\mathbf{B}_{\mathrm{SR}}$ and $\mathbf{B}_{\mathrm{SD}}$ before transmission, such that they are received only at the indented destination, without mutual interference. The signal transmitted by $\mathbf{S}$ is thus

$$
\mathbf{s}=\mathbf{B}_{\mathrm{SR}} \mathbf{x}_{\mathrm{SR}}+\mathbf{B}_{\mathrm{SD}} \mathbf{x}_{\mathrm{SD}}
$$

Then, for a given IRS configuration $\boldsymbol{\Phi}_{1}$, the received signals at $\mathbf{R}$ and $\mathbf{D}$ are, respectively,

$$
\begin{aligned}
& \mathbf{y}_{\mathbf{R}, 1}=\underbrace{\left(\mathbf{H}_{\mathbf{S R}}+\mathbf{H}_{\mathbf{I R}} \boldsymbol{\Phi}_{1} \mathbf{H}_{\mathbf{S I}}\right) \mathbf{B}_{\mathbf{S R}}}_{\tilde{\mathbf{H}}_{\mathbf{S R}}\left(\boldsymbol{\Phi}_{1}\right)} \mathbf{x}_{\mathbf{S R}}+\mathbf{n}_{\mathbf{R}, 1} \\
& \mathbf{y}_{\mathbf{D}, 1}=\underbrace{\mathbf{H}_{\mathrm{ID}} \boldsymbol{\Phi}_{1} \mathbf{H}_{\mathrm{RI}} \mathbf{B}_{\mathrm{SD

Note that, in both stages, the IRS configurations $\boldsymbol{\Phi}_{1}$ and $\boldsymbol{\Phi}_{2}$ are provided by $\mathcal{S}$, which has full control of the phase shifts.

## III. MAximum-RATE Problem

We now first derive the AR and then, we formulate the problem of maximizing the AR.

## A. Achievable Rate

For the first stage, the transmit beamformers $\mathbf{B}_{S D}$ and $\mathbf{B}_{S R}$ are chosen such that $\mathbf{x}_{S R}$ and $\mathbf{x}_{S D}$ do not generate interference at $\mathbf{D}$ and $\mathbf{R}$, respectively. To this end, BD is applied (see [13]), using in general a reduced set of streams for the two links. Let $\mathbf{H}_{S D}=\mathbf{U}_{S D} \boldsymbol{\Gamma}_{S D} \mathbf{V}_{S D}$ and the singular value decomposition (SVD) of $\mathbf{H}_{S D}$; a subset $\mathcal{S}_{S D}$ of streams (corresponding to diagonal elements of $\boldsymbol{\Gamma}_{S D}$ ) is selected for transmission to $\mathbf{D}$. The BD beamformer for transmission to $\mathbf{R}$ is $\mathbf{B}_{S R}=\mathbf{N}_{S D} \mathbf{B}_{S R}^{\prime}$, where $\mathbf{N}_{S D}$ collects the columns of $\mathbf{V}_{S D}$ with indices not in the set $\mathcal{S}_{S D}$, while $\mathbf{B}_{S R}^{\prime}$ is the capacityachieving precoder for the resulting S-R channel. A similar procedure is applied for the definition of the $\mathbf{S}-\mathbf{D}$ precoder $\mathbf{B}_{S D}$, for which $\mathcal{S}_{S R}$ streams are selected. We must also have $\left|\mathcal{S}_{S R}\right|+\left|\mathcal{S}_{S D}\right| \leq N_{S}$. Lastly, $\mathbf{x}_{S D}$ and $\mathbf{x}_{S R}$, are zero-mean complex Gaussian vectors with independent entries of size $\left|\mathcal{S}_{S D}\right|$ and $\left|\mathcal{S}_{S R}\right|$.

For the second stage, R applies capacity-achieving searching for $K$-QAM modulation as in (18-24) in [3]. For an i.i.d. $\mathcal{N}(0,1)$ inputs, the degrees of freedom are $n$ bits per dimension [12]. Thus, we have found that $\mathcal{S}_{R D}=\left\{\gamma_{S R}^{(i)}\right\}_{i=1}^{K}$. The R-D channel can be decomposed into $|\mathcal{S}_{R D}|$ parallel AWGN channels, with gains $\left\{\gamma_{R D}^{(i)}\right\}_{i=1}^{K}$. Then, the capacity of the R-D channel is $C_{R D}=\sum_{i=1}^{K} \log _{2}\left[1+\frac{P_{R D}^{(i)}}{\sigma^{2}}\right]$ [29], the $(i, k)$-th stream from $\mathbf{S}$ to $\mathbf{R}$ is given by $\mathcal{S}_{S R}(i, k)=\left\{\mathbf{b}_{S R, i}^{(k)}\right\}, k=1, \ldots, K$. The $(i, k)$-th stream from $\mathbf{R}$ to $\mathbf{D}$ is given by $\mathcal{S}_{R D}(i, k)=\left\{\overline{\mathbf{b}}_{R D, i}^{(k)}\right\}, k=1, \ldots, K$, so the matrix $\mathbf{B}_{R D}$ is 

$$
\begin{aligned}
\mathbf{B}_{R D}=\left[\begin{array}{lll}
\mathbf{b}_{R D, 1}^{(1)} & \cdots & \mathbf{b}_{R D, K_{R D}}^{(1)} \\
\vdots & \ddots & \vdots \\
\mathbf{b}_{R D, 1}^{(K)} & \cdots & \mathbf{b}_{R D, K_{R D}}^{(K)}
\end{array}\right]
\end{aligned}
$$



Scheme of the two-stage communication system.
Thread $K=3$ and $K_{R D}=K_{S R}=1, N_{S}=3, N_{D}=4, N_{R}=2$.

As a result, the S-D MIMO equivalent channel can be decomposed into $\left|\mathcal{S}_{S D}\right|$ independent parallel additive white Gaussian noise (AWGN) channels with gains $\left\{\gamma_{S D}{ }^{(i)}\right\}_{i=1}^{\mathcal{J}}{ }^{\mathcal{S}_{D}}$ The capacity of the $\mathbf{S}-\mathbf{D}$ channel is therefore

$$
C_{S D}=\sum_{i \in \mathcal{S}_{S D}} \log _{2}\left[1+\frac{\gamma_{S D}{ }^{(i)} P_{S D}^{(i)}}{\sigma^{2}}\right]
$$

where $P_{S D}^{(i)}$ is the power allocated to channel $i$. Similarly, the $\mathbf{S}-\mathbf{R}$ and $\mathbf{R}-\mathbf{D}$ channels can be decomposed into $\left|\mathcal{S}_{S R}\right|$ and $\left|\mathcal{S}_{R D}\right|$ parallel AWGN channels, with gains $\left\{\gamma_{S R}{ }^{(i)}\right\}$ and $\left\{\gamma_{R D}^{(i)}\right\}$, respectively, and the $\mathbf{S}-\mathbf{R}$ and $\mathbf{R}-\mathbf{D}$ capacities $C_{S R}$ and $C_{R D}$ can be written as in (7), where subscript $\mathcal{S}_{D}$ is replaced by subscripts $\mathcal{S}_{R}$ and $\mathcal{S}_{R D}$, respectively.

The AR of the considered two-stage scheme is therefore

$$
\mathcal{C}_{\text {HYB }}=\frac{1}{2}\left(C_{S D}+\min \left\{C_{S R}, C_{R D}\right\}\right)
$$

where the two stages requires twice the time of direct transmission, hence the factor $1 / 2$.

Note that for a transmission using only the relay, the AR $C_{\text {relay }}$ is still given by (8), with the IRS switched off $\left(A_{n}(\theta)=\right.$ $0, \forall \theta)$. A transmission using only the IRS can instead be performed in a single stage and the $\operatorname{AR}$ is $C_{I R S}=C_{S D}$. In both cases, no BD is needed. Note also that IRS- or relay-only transmissions occur if no streams are selected for the $\mathbf{S}-\mathbf{R}$ or $\mathbf{S}-\mathbf{D}$ links, i.e., if $\left|\mathcal{S}_{S R}\right|=0$ or $\left|\mathcal{S}_{S D}\right|=0$, respectively.

[^0]B. Optimization Problem

With this choice of beamformers, we are left with the problem of optimizing a) the transmit power, b) the IRS configurations in both stages, and c) the set of streams assigned to $\mathbf{R}$ and $\mathbf{D}$ in stage 1 . The AR maximization problem can be formalized as follows:


The minimum in (8) is now reflected by constraint (9h). Constraints (9b)-(9d) are related to the control of IRS phase shifts, and constraints (9e) and (9g) are power constraints at the devices, and we added the total power constraint $\mathcal{P}_{\max }$. This constraint will make the comparison with schemes using only the IRS more fair, by imposing $\mathcal{P}_{\max }$ the maximum power for $\mathbf{S}$. Constraints (9i)-(9j) are relative to the stream assignment.

## C. Alternating Optimization Solution

Notice that constraint (9c) makes the problem non-convex, thus we resort to an alternating optimization solution, where we optimize over the IRS configurations and stream sets, and for each considered configuration we optimize the transmission powers.

For fixed IRS configurations and stream selections, the optimization problem (9) becomes

$$
\begin{aligned}
& \underset{\left\{P_{S D}^{(i)}\right\},\left\{P_{S R}^{(j)}\

these new definitions, (10) can be split into the two (coupled) problems, for given $P_{R, \text { eff }}$,

$$
\begin{aligned}
\max _{\left\{P_{R \mathrm{D}}(k)\right\}} & C_{R \mathrm{D}} \\
\text { s.t. } & \sum_{k \in \mathcal{S}_{\mathrm{RD}}} P_{R \mathrm{D}}(k)=P_{R, \mathrm{eff}}
\end{aligned}
$$

and

$$
\begin{aligned}
\operatorname{argmax}_{\left\{P_{\mathrm{SD}}(i)\right\},\left\{P_{\mathrm{SR}}(j)\right\}} & \frac{1}{2}\left(C_{\mathrm{SD}}+C_{\mathrm{SR}}\right) \\
\text { s.t. } & C_{\mathrm{SR}} \leq C_{\mathrm{RD}}^{*} \\
& \sum_{i \in \mathcal{S}_{\mathrm{SD}}} P_{\mathrm{SD}}(i)+\sum_{j \in \mathcal{S}_{\mathrm{SR}}} P_{\mathrm{SR}}(j)=P_{\mathrm{S}, \mathrm{eff}}
\end{aligned}
$$

Note that (12) and (13) are convex optimization problems and, therefore, they can be solved in closed-form, as detailed in the next sub-section.

Then, we need to optimize the IRS reflection coefficients $\boldsymbol{\Phi}_{1}$ and $\boldsymbol{\Phi}_{2}$, the stream sets $\mathcal{S}_{\mathrm{SR}}, \mathcal{S}_{\mathrm{SD}}$, and $\mathcal{S}_{\mathrm{RD}}$, and the auxiliary variable $P_{\mathrm{R}, \text { eff }}$, in what turns out to be a non-convex problem. Thus, we resort to the discrete genetic algorithm (GA) [14], which operates iteratively, solving sub-problems (13) and (12) for given IRS configurations, power $P_{\mathrm{R}, \mathrm{eff}}$, stream sets $\mathcal{S}_{\mathrm{SR}}$, $\mathcal{S}_{\mathrm{SD}}$, and $\mathcal{S}_{\mathrm{RD}}$ at each iteration.

## D. Decoupled Problem Solution

Solution of Problem (12): Since the capacity $C_{\mathrm{SR}}$ is upper bounded by $C_{\mathrm{RD}}^{*}$ from (13b), we first optimize the transmit powers $\left\{P_{R \mathrm{D}}(k)\right\}$ at $R$, given $P_{\mathrm{R} \text {,eff. }}$. Indeed, (12) can be solved via the standard waterfilling algorithm [13] on channels with gains $\left\{\gamma_{\mathrm{RD}}(i)\right\}$ and total power $P_{\mathrm{R}, \text { eff }}$

Solution of Problem (13): The Lagrangian function of (13) is (with $\lambda_{1}$ and $\lambda_{2}$ multipliers)

$$
\begin{aligned}
\mathcal{L}=} & \left(C_{\mathrm{SD}}+C_{\mathrm{SR}}\right)-\lambda_{2}\left(C_{\mathrm{SR}}-C_{\mathrm{RD}}^{*}+s\right) \\
& -\lambda_{1}\left(\sum_{i \in \mathcal{S}_{\mathrm{SD}}} P_{\mathrm{SD}}(i)+\sum_{j \in \mathcal{S}_{\mathrm{SR}}} P_{\mathrm{SR}}(j)-P_{\mathrm{S}, \mathrm{eff}}\right)
\end{aligned}
$$

where $s \geq 0$ is an additional slack variable. Setting to zero the derivative of the Lagrangian function, we obtain the following stationary points

$$
P_{\mathrm{SD}}(i)=\frac{1}{\ln (2) \lambda_{1}}-\frac{1}{\gamma_{\mathrm{SD}}(i)}, P_{\mathrm{SR}}(j)=\frac{1}{\ln (2) \lambda_{1}}-\frac{1}{\gamma_{\mathrm{SR}}(j)}
$$

with $\lambda_{1}$ such that (13c) is satisfied.
Now, letting $s=C_{\mathrm{RD}}^{*}-C_{\mathrm{SR}}$, if $s \geq 0$ we have found the optimal solution. If instead $s<0$, then we must assume $s=0$, i.e., the S-R rate in stage 1 equals the R-D rate in stage 2 . Consequently, we allocate the minimum power that satisfies this constraint to the S-R link, while all the remaining power is assigned to the $S$-D link. Hence, we first solve the following problem

$$
\begin{aligned}
\underset{\left\{P_{\mathrm{SR}}(j)\right\}}{\operatorname{argmin}} & \sum_{j \in \mathcal{S}_{\mathrm{SR}}} P_{\mathrm{SR}}(j) \\
\text { s.t. } & C_{\mathrm{SR}}=C_{\mathrm{RD}}^{*}
\end{aligned}
$$



Figure 2. AR versus $b$, for $P_{\mathrm{S}} / P_{\max }=0.5, N_{\mathrm{I}}=36$, and $y_{\mathrm{I}}=20 \mathrm{~m}$.
with the Lagrangian multipliers method, providing

$$
P_{\mathrm{SR}}^{*}(j)=\left[\left(\frac{2 C_{\mathrm{RD}}^{*}}{\prod_{j \in \mathcal{S} \mathrm{SR}} \gamma_{\mathrm{SR}}(j)}\right)^{\frac{1}{\left|S_{\mathrm{SR}_{\mathrm{R}}}\right|}}-\frac{1}{\gamma_{\mathrm{SR}}(j)}\right]_{+}
$$

where $(x)_{+}=x$ if $x \geq 0$, while $(x)_{+}=0$ otherwise. For the obtained optimal powers $P_{\mathrm{SR}}(j)^{*}$, we solve

$$
\operatorname{argmax}_{\left\{P_{\mathrm{SD}}(i)\right\}} C_{\mathrm{SD}},
$$

which is similar to (12) and can be solved likewise.

## IV. NuMERICAL RESULTS

In this section, we assess the performance of the proposed protocol. $S, R, D$, and $I$ have coordinates $(0,0,3),(10,-10,3)$, $(20,0,1.5)$, and $\left(10, y_{I}, 3\right) \mathrm{m}$, respectively (see Fig. 1), and $y_{\mathrm{I}}$ is a parameter to be set. We consider $M=2$ NLOS components for each mmWave link. $S, R$, and $D$ are equipped with ULAs of $N_{\mathrm{S}}=16, N_{\mathrm{R}}=8$, and $N_{\mathrm{D}}=4$ antennas, respectively, whereas the IRS is an UPA with $N_{\mathrm{I}}=36$ elements and parameters (see [10]) $A_{\min }=0.2, \zeta=0.43 \pi$, and $v=1.6$. Angles in the array response vector are chosen according to a uniform random distribution, in particular, $\psi_{\cdot, m} \sim \mathcal{U}[0,2 \pi)$ and $\xi_{\cdot, m} \sim \mathcal{U}[0, \pi / 2)$ for the IRS, while $\xi_{., m}=0$ for other devices with ULA. The transmit signalto-noise ratio (SNR) is $P_{\max } / \sigma^{2}=10(10 \mathrm{~dB})$. The path loss term is modelled as $\rho(d)=K_{0}\left(d / d_{0}\right)^{-\alpha / 2}$, where $K_{0}=\rho\left(d_{0}\right)=0 \mathrm{~dB}$ is the path loss at the reference distance $d_{0}=10 \mathrm{~m}$, and $\alpha=5.76$ is the path loss exponent [15]. We compare five schemes: the proposed optimized hybrid IRСrelay scheme (Hyb. Opt.), a hybrid scheme with random IRS configuration (Hyb. Rand.), a scheme without relay and an optimized IRS (IRS Opt.), a scheme with a random IRS (IRS Rand.), and a scheme without IRS and a relay (Relay).

Fig. 2 shows the AR as a function of the IRS phase shift resolution $b$ for $y_{\mathrm



Figure 3. AR versus PS/Pmax, for $y_{I}=20 \mathrm{~m}, N_{I}=36$, and $b=2$.



Figure 4. AR versus $y_{I}$, for $\mathrm{PS} / \mathrm{P}_{\text {max }}=0.5, N_{I}=36$, and $b=2$.
$\forall n$, corresponding to the maximum value of $A(\cdot)$. For all schemes, the AR saturates with just $b=1$ or 2 bits per element, thus, as already observed in the literature, a very limited number of configurations are enough to achieve the gains provided by the IRS. In the following, we will consider $b=2$. The schemes with randomly configured IRS show a penalty for higher resolution, since configurations with lower gains $A(\cdot)$ are used.

Fig. 3 shows the AR as a function of the fractional available power at S, i.e., $\mathrm{PS} / \mathrm{P}_{\text {max }}$ for $y_{I}=20 \mathrm{~m}$. The Hyb. Opt. scheme provides the highest AR for all values of PS/Pmax. Still, for low $\mathrm{PS} / \mathrm{P}_{\max }$, the relay has a considerable fraction of power, thus the Relay scheme is close to optimal. Instead, at high $\mathrm{PS} / \mathrm{P}_{\text {max }}$, the constraint on CRD limits the AR at the relay, and the IRS Opt. scheme attains higher performance. The IRS Rand. scheme yields very poor performance, due to the absence of the relay and the random configuration of the IRS.

Fig. 4 shows the AR as a function of the IRS distance



Figure 5. AR versus $N_{I}$, for $\mathrm{PS} / \mathrm{P}_{\max }=0.5, y_{I}=20 \mathrm{~m}$ and $b=2$.
$y_{I}$, when $\mathrm{PS} / \mathrm{P}_{\max }=0.5$. For small $y_{I}$ values, the IRS link is dominant with respect to the relay link, making the Hyb. Opt. scheme transmit exclusively towards the IRS, thus avoiding the half-rate penalty of the two-stage protocol, and approaching the AR. On the other hand, the IRS assistance becomes marginal as $y_{I}$ grows, resulting in similar performance between Hyb. and Relay schemes.

Finally, Fig. 5 shows the AR as a function of the number of reflecting elements $N_{I}$, for $\mathrm{PS} / \mathrm{P}_{\max }=0.5$ and $y_{I}=20 \mathrm{~m}$. As expected, due to the huge beamforming gain introduced by large IRSs, the AR grows with the number of reflecting elements.

## V. CONCLUSIONS

In this paper, we considered an hybrid IRS-relay system, optimizing power allocation, IRS configurations, and stream sets to maximize the AR. Numerical results showed that, in the considered scenarios, large phase-optimized IRSs yield higher ARs than systems using only either the relay or the IRS. Indeed, the best performance is achieved by different uses of the relay and the IRS under different positions of the devices or power split among the source and the relay. This suggests that the proposed hybrid solution, which is able to switch among the various uses, is always advantageous.

## REFERENCES

[1] W. Long, R. Chen, M. Moretti, W. Zhang, and J. Li, "A promising technology for 6G wireless networks: Intelligent reflecting surface," J. of Commun. and Inf. Net., vol. 6, no. 1, pp. 1-16, 2021.
[2] E. Bjornson, O. Ozdogan, and E. G. Larsson, "Intelligent reflecting surface versus decode-and-forward: How large surfaces are needed to beat relaying?" IEEE Wireless Commun. Lett., vol. 9, no. 2, pp. 244248, Oct. 2020.
[3] C. Huang, A. Zappone, G. C. Alexandropoulos, M. Debbah, and C. Yuen, "Reconfigurable intelligent surfaces for energy efficiency in wireless communication," IEEE Trans. on Wireless Commun., vol. 18, no. 8, pp. 4157-4170, Jun. 2019.
[4] M. Di Renzo et al., "Reconfigurable intelligent surfaces vs. relaying: Differences, similarities, and performance comparison," IEEE Open J. of the Commun. Soc., vol. 1, pp. 798-807, Jun. 2020.



[5] Z. Abdullah, G. Chen, S. Lambotharan, and J. A. Chambers, "A hybrid relay and intelligent reflecting surface network and its ergodic performance analysis," IEEE Wireless Commun. Lett., vol. 9, no. 10, pp. 1653-1657, Oct. 2020.
[6] - , "Optimization of intelligent reflecting surface assisted full-duplex relay networks," IEEE Wireless Commun. Lett., vol. 10, no. 2, pp. 363367, Feb. 2021.
[7] I. Yildirim, F. Kilinc, E. Basar, and G. C. Alexandropoulos, "Hybrid RIS-empowered reflection and decode-and-forward relaying for coverage extension," IEEE Commun. Lett., pp. 1-1, 2021.
[8] C. Huang, G. Chen, Y. Gong, M. Wen, and J. A. Chambers, "Deep reinforcement learning based relay selection in intelligent reflecting surface assisted cooperative networks," IEEE Wireless Commun. Lett., pp. 1-1, 2021.
[9] M. R. Akdeniz et al., "Millimeter wave channel modeling and cellular capacity evaluation," IEEE J. on Sel. Areas in Commun., vol. 32, no. 6, pp. 1164-1179, 2014.
[10] S. Abeywickrama, R. Zhang, Q. Wu, and C. Yuen, "Intelligent reflecting surface: Practical phase shift model and beamforming optimization," IEEE Trans. Commun., vol. 68, no. 9, pp. 5849-5863, 2020.
[11] X. Tan, Z. Sun, J. M. Jornet, and D. Pados, "Increasing indoor spectrum sharing capacity using smart reflect-array," in Proc. Int. Conf. on Commun. (ICC). IEEE, May 2016.
[12] X. Tan, Z. Sun, D. Koutsonikolas, and J. M. Jornet, "Enabling indoor mobile millimeter-wave networks based on smart reflect-arrays," in Proc. Int. Conf. on Computer Commun. (INFOCOM). IEEE, Apr. 2018.
[13] N. Benvenuto, G. Cherubini, and S. Tomasin, Algorithms for Communication Systems and their applications, 2nd ed. Wiley, 2021.
[14] J. H. Holland, Adaptation in Natural and Artificial Systems: An Introductory Analysis with Applications to Biology, Control and Artificial Intelligence. MIT Press, 1992.
[15] Y. Azar et al., " 28 GHz propagation measurements for outdoor cellular communications using steerable beam antennas in new york city," in Proc. Int. Conf. on Commun. (ICC). IEEE, Jun. 2013, pp. 5143-5147.



