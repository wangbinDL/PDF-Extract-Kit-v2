# Maximum-Rate Optimization of Hybrid Intelligent Reflective Surface and Relay Systems 

Alberto Rech, Federico Moretto, and Stefano Tomasin<br>Department of Information Engineering, University of Padova, Italy.<br>Emails: rechalbert@dei.unipd.it, federico.moretto.1@unipd.it, tomasin@dei.unipd.it


#### Abstract

We consider a wireless communication system, where a transmitting source is assisted by both a reconfigurable intelligent reflecting surface (IRS) and a decode-and-forward half-duplex relay (hybrid IRS-relay scheme) to communicate with a destination receiver. All devices are equipped with multiple antennas, and transmissions occur in two stages. In stage 1, the source splits the transmit message into two sub-messages, transmitted to the destination and the relay, respectively, using block diagonalization to avoid interference. Both transmissions will benefit from the IRS. In stage 2, the relay re-encodes the received sub-message and forwards it (still through the IRS) to the destination. We optimize power allocations, beamformers, and configurations of the IRS in both stages, in order to maximize the achievable rate at the destination. We compare the proposed hybrid approach with other schemes (with/without relay and IRS), and confirm that high data rate is achieved for the hybrid scheme in case of optimal IRS configurations.


Index Terms-Beamforming, IRS, MIMO, rate optimization, relay.

## I. InTRODUCTION

A reconfigurable intelligent reflecting surface (IRS) is a programmable metasurface that can alter the phase and amplitude of an impinging signal by dynamically adjusting the reflection coefficients of its elements. Recently, IRSs have drawn enormous research interest as a promising technology for the sixth generation ( 6 G ) of cellular networks [1], due to their ability of controlling the wireless propagation environment. Before the advent of IRSs, relays have been studied and used in cellular networks to increase coverage and improve the received signal quality. Among various solutions, decode-and-forward (DF) relays are half-duplex (HD) devices that alternate two stages, one wherein they receive a message from the source, and a second wherein they re-encode the message and transmit it to the destination.

The alternative use of IRSs and relays has been widely investigated. In [2], IRSs and single-antenna DF relays are compared in terms of power consumption, whereas in [3] the energy efficiency of systems using IRSs is compared to a system with multi-antenna amplify-and-forward (AF) relays. A comparison between IRSs and DF HD/full-duplex (FD) relays is presented in [4], proving that sufficiently large IRSs yield higher spectral and energy efficiency than relay-aided systems. Nevertheless, due to the expensive deployment of IRSs, hybrid IRS-relay systems, wherein both devices are jointly adopted, will be a cost-effective solution for the near future of smart electromagnetic environments. In [5], the combination of a HD DF relay and an IRS is investigated and tight upper bounds for the achievable rate (AR) are derived. A hybrid system with a FD DF relay is studied in [6], showing that the performance further improves, as long as the relay self-interference is low. However, both works consider source and destination equipped with a single antenna each. In [7], a system wherein an IRS assists both a relay and a destination (and the source has no direct link with either the relay and the destination) is considered, with source, relay, and destination again having all one antenna each. For a system with multiple relays, still in the presence of an IRS, the selection of one relay to assist communication between a source and a destination is solved by machine-learning in [8].

In this paper, we consider a hybrid IRS-relay multipleinput multiple-output (MIMO) system, which generalizes the systems considered in [5], [6], and [7], as we now assume that all devices are equipped with multiple antennas. Moreover, contrary to [7], we also consider the link between the source and the relay. The relay is HD and operates in the DF mode. We propose a transmission protocol operating in two stages. In stage 1 , the source splits the transmit message into two sub-messages, transmitted to the destination and the relay, respectively, using block diagonalization to avoid interference. Both transmissions will benefit from the IRS. In stage 2, the relay re-encodes the received sub-message and forwards it (still through the IRS) to the destination. We optimize power allocations, beamformers, and configurations of the IRS in both stages, to maximize the AR at the destination. In particular, we split the AR optimization problem into two subproblems, one for each stage, then coupled by the choice of the IRS configuration and the power split between the signal for the relay and the destination in stage 1. Lastly, we compare the proposed hybrid approach with other schemes (with/without relay and IRS), and confirm that a high data rate is achieved for the hybrid scheme in case of optimal IRS configuration.

The rest of this paper is organized as follows. Section II describes transmission characteristics and the two-stage protocol. In Section III we formalize the maximum-rate optimization problem and describe the alternating optimization solution. In Section IV we discuss numerical results before the conclusions are taken in Section V.

Notation: Scalars are denoted by italic letters, vectors and matrices by boldface lowercase and uppercase letters, respectively, and sets are denoted by calligraphic uppercase letters. $\operatorname{diag}(\mathbf{a})$ indicates a square diagonal matrix with the elements of $\mathbf{a}$ on the principal diagonal. $\mathbf{A}^{H}$ denotes the conjugate




---



Figure 1. Two-stage IRS- and relay-assisted MIMO system. Solid arrows represent the S-D link in stage 1, dashed arrows the S-R link in stage 1, and dotted arrows the R-D link in stage 2.
transpose of matrix $\mathbf{A} . \mathbb{E}[\cdot]$ denotes the statistical expectation. $\mathbf{I}_{x}$ is the identity matrix of size $x$.

## II. SyStEM MODEL

We consider the narrowband single-user MIMO communication system shown in Fig. 1, wherein the transmission from a source $(\mathrm{S})$ to a destination (D) is assisted by both a relay (R) and an IRS (I). We assume that S and R have maximum transmit powers $P_{\mathrm{S}}$ and $P_{\mathrm{R}}$, respectively.
S, D, and R are equipped with uniform linear arrays (ULAs) with $N_{\mathrm{S}}, N_{\mathrm{D}}$, and $N_{\mathrm{R}}$ antennas, respectively, whereas I is a uniform planar array (UPA) with $N_{\mathrm{I}}$ passive reflective elements.

We denote with $\mathbf{H}_{\mathrm{SI}} \in \mathbb{C}^{N_{\mathrm{I}} \times N_{\mathrm{S}}}$ and $\mathbf{H}_{\mathrm{SR}} \in \mathbb{C}^{N_{\mathrm{R}} \times N_{\mathrm{S}}}$ the S-R and S-I channels, with $\mathbf{H}_{\mathrm{RI}} \in \mathbb{C}^{N_{\mathrm{I}} \times N_{\mathrm{R}}}$ and $\mathbf{H}_{\mathrm{RD}} \in$ $\mathbb{C}^{N_{\mathrm{D}} \times N_{\mathrm{R}}}$ the R-I and R-D channels, and with $\mathbf{H}_{\mathrm{IR}}=\mathbf{H}_{\mathrm{RI}}^{T}$ and $\mathbf{H}_{\mathrm{ID}} \in \mathbb{C}^{N_{\mathrm{D}} \times N_{\mathrm{I}}}$ the I-R and I-D channels. We consider narrowband mmWave channels [9], each having $M$ non-lineof-sight (NLOS) components. Hence, channel matrix $\mathbf{H}_{\mathrm{XY}}$ between transmitter $X$ and receiver $Y$ is

$$
\mathbf{H}_{\mathrm{XY}}=\frac{1}{\sqrt{M}} \sum_{m=1}^{M} g_{m} \rho(d) \mathbf{a}\left(\boldsymbol{\omega}_{X, m}\right) \mathbf{a}^{H}\left(\boldsymbol{\omega}_{Y, m}\right)
$$

where $g_{m} \sim \mathcal{C N}(0,1)$ is the gain of the $m$-th path, $\rho(d)$ is the path loss attenuation factor, with $d$ being the distance between $X$ and $Y, \boldsymbol{\omega}_{\text {・ }, m}=\left(\xi_{\text {・ }, m}, \psi_{\text {・ }, m}\right)$ is the vector of azimuth $\left(\xi_{\text {., }, m}\right)$ and elevation $\left(\psi_{i, m}\right)$ angles, and $\mathbf{a}\left(\boldsymbol{\omega}_{\cdot, m}\right)=$ $\left(1, \ldots, e^{j \pi\left[x \sin \left(\psi_{., m}\right) \cos \left(\xi_{., m}\right)+y \sin \left(\psi_{., m}\right) \sin \left(\xi_{., m}\right)\right]}, \ldots\right)^{T}$ is the array response vector for the $m$-th path, with $1 \leq x \leq N_{X}-1$ and $1 \leq y \leq N_{\gamma}-1$. We assume all devices operate in HD and have perfect channel state information.

## A. IRS Model

Each element of the IRS acts as an omnidirectional antenna element that captures and reflects signals, introducing an attenuation and a phase shift on the baseband-equivalent signal. Following the model of [10], we denote with $\varphi_{n}=A_{n}\left(\theta_{n}\right) e^{j \theta_{n}}$ the reflection coefficient of the $n$-th IRS element, where $\theta_{n} \in[-\pi, \pi)$ is the induced phase shift and $A_{n}^{2}\left(\theta_{n}\right) \in[0,1]$ is the corresponding power attenuation factor. Indicating with $\mathbf{x} \in \mathbb{C}^{1 \times N_{\mathrm{I}}}$ the impinging signal on the IRS, the reflected signal $\mathbf{y} \in \mathbb{C}^{1 \times N_{\mathrm{I}}}$ is $\mathbf{y}=\boldsymbol{\Phi} \mathbf{x}$, with $\boldsymbol{\Phi}=\operatorname{diag}\left(\varphi_{1}, \ldots, \varphi_{N_{\mathrm{I}}}\right)$, which is the IRS reflection matrix, also denoted IRS configuration.
We consider the realistic baseband-equivalent model of the IRS described in [10], where

$$
A_{n}\left(\theta_{n}\right)=\left(1-A_{\min }\right)\left(\sin \theta_{n}-\zeta+\frac{1}{2}\right)^{v}+A_{\min }
$$

with $A_{\text {min }} \geq 0, \zeta \geq 0$, and $v \geq 0$ being IRS-specific parameters, assumed to be identical for all IRS elements.
The phase shifts $\theta_{n}$ are controllable, thus indirectly controlling also the attenuations. Moreover, since continuousphase shifts are hardly implementable [11]-[12], we assume that the phase shifts are chosen from a discrete set $\mathcal{F}_{\theta}=$ $\left\{0, \frac{2 \pi}{2^{b}}, \ldots, \frac{2 \pi\left(2^{b}-1\right)}{2^{b}}\right\}$, where $b>0$ is the IRS phase shift resolution, i.e., the number of bits employed to control the phase shifts. The source has full control of the phase shifts, which can be optimized together with beamforming.

## B. Two-stage Communication Protocol

For a HD DF relay, signal reception and transmission have to occur in two stages, here assumed to be of the same duration.

Stage 1: S splits the message into two sub-messages, and encodes/modulates them into the two signals $\mathbf{x}_{\mathrm{SR}}$ and $\mathbf{x}_{\mathrm{SD}}$, intended for R and D , respectively. The two signals are precoded with block diagonalization (BD) precoders $\mathbf{B}_{\mathrm{SR}}$ and $\mathbf{B}_{\mathrm{SD}}$ before transmission, such that they are received only at the indented destination, without mutual interference. The signal transmitted by S is thus

$$
\mathbf{s}=\mathbf{B}_{\mathrm{SR}} \mathbf{x}_{\mathrm{SR}}+\mathbf{B}_{\mathrm{SD}} \mathbf{x}_{\mathrm{SD}}
$$

Then, for a given IRS configuration $\boldsymbol{\Phi}_{1}$, the received signals at R and D are, respectively,

$$
\begin{aligned}
\mathbf{y}_{\mathrm{R}, 1} & =\underbrace{\left(\mathbf{H}_{\mathrm{SR}}+\mathbf{H}_{\mathrm{IR}} \boldsymbol{\Phi}_{1} \mathbf{H}_{\mathrm{SI}}\right) \mathbf{B}_{\mathrm{SR}}}_{\tilde{\mathbf{H}}_{\mathrm{SR}}\left(\boldsymbol{\Phi}_{1}\right)} \mathbf{x}_{\mathrm{SR}}+\mathbf{n}_{\mathrm{R}, 1} \\
\mathbf{y}_{\mathrm{D}, 1} & =\underbrace{\mathbf{H}_{\mathrm{ID}} \boldsymbol{\Phi}_{1} \mathbf{H}_{\mathrm{SI}} \mathbf{B}_{\mathrm{SD}}}_{\tilde{\mathbf{H}}_{\mathrm{SD}}\left(\boldsymbol{\Phi}_{1}\right)} \mathbf{x}_{\mathrm{SD}}+\mathbf{n}_{\mathrm{D}, 1}
\end{aligned}
$$

where $\tilde{\mathbf{H}}_{\mathrm{SR}}\left(\boldsymbol{\Phi}_{1}\right)\left(\tilde{\mathbf{H}}_{\mathrm{SD}}\left(\boldsymbol{\Phi}_{1}\right)\right)$ is the S-R (S-D) equivalent channel matrix (we highlight their dependency on


---

Note that, in both stages, the IRS configurations $\boldsymbol{\Phi}_{1}$ and $\boldsymbol{\Phi}_{2}$ are provided by $\mathcal{S}$, which has full control of the phase shifts.

## III. MAXIMUM-RATE PROBLEM

We now first derive the AR and then, we formulate the problem of maximizing the AR.

## A. Achievable Rate

For the first stage, the transmit beamformers $\boldsymbol{B}_{\mathrm{SD}}$ and $\boldsymbol{B}_{\mathrm{SR}}$ are chosen such that $\boldsymbol{x}_{\mathrm{SR}}$ and $\boldsymbol{x}_{\mathrm{SD}}$ do not generate interference at $\mathcal{D}$ and $\mathcal{R}$, respectively. To this end, BD is applied (see [13]), using in general a reduced set of streams for the two links. Let $\boldsymbol{H}_{\mathrm{SD}}=\boldsymbol{U}_{\mathrm{SD}} \boldsymbol{\Gamma}_{\mathrm{SD}} \boldsymbol{V}_{\mathrm{SD}}$ and the singular value decomposition (SVD) of $\boldsymbol{H}_{\mathrm{SD}}$; a subset $\mathcal{S}_{\mathrm{SD}}$ of streams (corresponding to diagonal elements of $\boldsymbol{\Gamma}_{\mathrm{SD}}$ ) is selected for transmission to $\mathcal{D}$. The BD beamformer for transmission to $\mathcal{R}$ is $\boldsymbol{B}_{\mathrm{SR}}=\boldsymbol{N}_{\mathrm{SD}} \boldsymbol{B}_{\mathrm{SR}}^{\prime}$, where $\boldsymbol{N}_{\mathrm{SD}}$ collects the columns of $\boldsymbol{V}_{\mathrm{SD}}$ with indices not in the set $\mathcal{S}_{\mathrm{SD}}$, while $\boldsymbol{B}_{\mathrm{SR}}^{\prime}$ is the capacityachieving precoder for the resulting $\mathcal{S}-\mathcal{R}$ channel. A similar procedure is applied for the definition of the $\mathcal{S}-\mathcal{D}$ precoder $\boldsymbol{B}_{\mathrm{SD}}$, for which $S_{\mathrm{SR}}$ streams are selected. We must also have $\left|S_{\mathrm{SR}}\right|+\left|S_{\mathrm{SR}}\right| \leq N_{\mathrm{S}}$. Lastly, $\boldsymbol{x}_{\mathrm{SD}}$ and $\boldsymbol{x}_{\mathrm{SR}}$, are zero-mean complex Gaussian vectors with independent entries of size $\left|\mathcal{S}_{\mathrm{SD}}\right|$ and $\left|\mathcal{S}_{\mathrm{SR}}\right|$.

For the second stage, $\mathcal{R}$ applies capacity-achieving precoding, and $\boldsymbol{x}_{\mathrm{RD}}$ zero-mean complex Gaussian vectors with independent entries of size $N_{\mathrm{R}}$.

As a result, the $\mathcal{S}-\mathcal{D}$ MIMO equivalent channel can be decomposed into $\left|\mathcal{S}_{\mathrm{SD}}\right|$ independent parallel additive white Gaussian noise (AWGN) channels with gains $\left\{\gamma_{\mathrm{SD}}(i)\right\} .{ }^{1}$ The capacity of the $\mathcal{S}-\mathcal{D}$ channel is therefore

$$
C_{\mathrm{SD}}=\sum_{i \in \mathcal{S}_{\mathrm{SD}}} \log _{2}\left[1+\frac{\gamma_{\mathrm{SD}}(i) P_{\mathrm{SD}}(i)}{\sigma^{2}}\right]
$$

where $P_{\mathrm{SD}}(i)$ is the power allocated to channel $i$. Similarly, the $\mathcal{S}-\mathcal{R}$ and $\mathcal{R}-\mathcal{D}$ channels can be decomposed into $\left|S_{\mathrm{SR}}\right|$ and $\left|\mathcal{S}_{\mathrm{RD}}\right|$ parallel AWGN channels, with gains $\left\{\gamma_{\mathrm{SR}}(i)\right\}$ and $\left\{\gamma_{\mathrm{RD}}(i)\right\}$, respectively, and the $\mathcal{S}-\mathcal{R}$ and $\mathcal{R}-\mathcal{D}$ capacities $C_{\mathrm{SR}}$ and $C_{\mathrm{RD}}$ can be written as in (7), where subscript SD is replaced by subscripts SR and RD, respectively.

The AR of the considered two-stage scheme is therefore

$$
C_{\mathrm{HYB}}=\frac{1}{2}\left(C_{\mathrm{SD}}+\min \left\{C_{\mathrm{SR}}, C_{\mathrm{RD}}\right\}\right)
$$

where the two stages requires twice the time of direct transmission, hence the factor $1 / 2$.

Note that for a transmission using only the relay, the AR $C_{\text {relay }}$ is still given by (8), with the IRS switched off $\left(A_{n}(\theta)=\right.$ $0, \forall \theta)$. A transmission using only the IRS can instead be performed in a single stage and the AR is $C_{\text {IRS }}=C_{\mathrm{SD}}$. In both cases, no BD is needed. Note also that IRS- or relay-only transmissions occur if no streams are selected for the $\mathcal{S}-\mathcal{R}$ or $\mathcal{S}-\mathcal{D}$ links, i.e., if $\left|\mathcal{S}_{\mathrm{SR}}\right|=0$ or $\left|\mathcal{S}_{\mathrm{SD}}\right|=0$, respectively.
${ }^{1} \gamma_{\mathrm{SD}}(i)$ is the $i$-th singular value of $\tilde{\boldsymbol{H}}_{\mathrm{SD}}\left(\boldsymbol{\Phi}_{1}\right) \tilde{\boldsymbol{H}}_{\mathrm{SD}}^{\mathrm{H}}\left(\boldsymbol{\Phi}_{1}\right)$.

## B. Optimization Problem

With this choice of beamformers, we are left with the problem of optimizing a) the transmit power, b) the IRS configurations in both stages, and c) the set of streams assigned to $\mathcal{R}$ and $\mathcal{D}$ in stage 1 . The AR maximization problem can be formalized as follows:

$$
\begin{aligned}
\underset{\substack{\Phi_{1}, \Phi_{2} \\
\mathcal{S}_{\mathcal{S D}}, \mathcal{S}_{\mathrm{SR}}, \mathcal{S} R_{\mathrm{RD}} \\
\left\{P_{\mathrm{SD}}{ }^{(i)}\right\},\left\{P_{\mathrm{SR}}(j)\right\},\left\{P_{\mathrm{RD}}(k)\right\}}}{\operatorname{argmax}} & \left(C_{\mathrm{SD}}+C_{\mathrm{SR}}\right), \\
\text { s.t. } \Phi_{k}= & \operatorname{diag}\left(\varphi_{1, k}, \ldots, \varphi_{N_{\mathrm{I}}, k}\right), \\
& k=1,2 \\
\varphi_{n, k}= & A_{n, k}\left(\theta_{n, k}\right) \mathrm{e}^{\mathrm{j} \theta_{n, k}}, \quad 1 \leq n \leq N_{\mathrm{I}}, \\
& k=1,2 \\
\theta_{n, k} \in & \mathcal{F}_{\theta}, \quad 1 \leq n \leq N_{\mathrm{I}}, \quad k=1,2
\end{aligned}
$$

$$
\begin{aligned}
& \sum_{i \in S_{\mathrm{SD}}} P_{\mathrm{SD}}(i)+\sum_{j \in S_{\mathrm{SR}}} P_{\mathrm{SR}}(j) \leq P_{\mathrm{S}}, \\
& \sum_{k \in \mathcal{S}_{\mathrm{RD}}} P_{\mathrm{RD}}(k) \leq P_{\mathrm{R}}, \\
& \sum_{i \in \mathcal{S}_{\mathrm{SD}}} P_{\mathrm{SD}}(i)+\sum_{j \in S_{\mathrm{SR}}} P_{\mathrm{SR}}(j)+ \\
& \quad \quad \sum_{k \in S_{\mathrm{RD}}} P_{\mathrm{RD}}(k) \leq P_{\max }, \\
& C_{\mathrm{SR}} \leq C_{\mathrm{RD}} \\
& S_{\mathrm{SD}}, S_{\mathrm{SR}} \in\left\{1, \ldots, N_{\mathrm{S}}\right\}, \\
& 0<\left|S_{\mathrm{SD


---

these new definitions, (10) can be split into the two (coupled) problems, for given $P_{\mathrm{R}, \text { eff }}$,

$$
\begin{array}{cl}
C_{\mathrm{RD}}^{*}= & \max _{\left\{P_{\mathrm{RD}}(k)\right\}} C_{\mathrm{RD}} \\
\text { s.t. } & \sum_{k \in \mathcal{S}_{\mathrm{RD}}} P_{\mathrm{RD}}(k)=P_{\mathrm{R}, \text { eff }}
\end{array}
$$

and
$\operatorname{argmax}_{\left\{P_{\mathrm{SD}}(i)\right\},\left\{P_{\mathrm{SR}}(j)\right\}} \frac{1}{2}\left(C_{\mathrm{SD}}+C_{\mathrm{SR}}\right)$,
s.t. $C_{\mathrm{SR}} \leq C_{\mathrm{RD}}^{*}$

$$
\sum_{i \in \mathcal{S}_{\mathrm{SD}}} P_{\mathrm{SD}}(i)+\sum_{j \in \mathcal{S}_{\mathrm{SR}}} P_{\mathrm{SR}}(j)=P_{\mathrm{S} \text {,eff. }}
$$

Note that (12) and (13) are convex optimization problems and, therefore, they can be solved in closed-form, as detailed in the next sub-section.

Then, we need to optimize the IRS reflection coefficients $\mathbf{\Phi}_{1}$ and $\boldsymbol{\Phi}_{2}$, the stream sets $\mathcal{S}_{\mathrm{SR}}, \mathcal{S}_{\mathrm{SD}}$, and $\mathcal{S}_{\mathrm{RD}}$, and the auxiliary variable $P_{\mathrm{R}, \text { eff }}$, in what turns out to be a non-convary problem. Thus, we resort to the discrete genetic algorithm (GA) [14], which operates iteratively, solving sub-problems (13) and (12) for given IRS configurations, power $P_{\mathrm{R}, \text { eff }}$, stream sets $\mathcal{S}_{\mathrm{SR}}$, $\mathcal{S}_{\mathrm{SD}}$, and $\mathcal{S}_{\mathrm{RD}}$ at each iteration.

## D. Decoupled Problem Solution

Solution of Problem (12): Since the capacity $C_{\text {SR }}$ is upper bounded by $C_{\mathrm{RD}}^{*}$ from (13b), we first optimize the transmit powers $\left\{P_{\mathrm{RD}}(k)\right\}$ at R , given $P_{\mathrm{R}, \text { eff }}$. Indeed, (12) can be solved via the standard waterfilling algorithm [13] on channels with gains $\left\{\gamma_{\mathrm{RD}}(i)\right\}$ and total power $P_{\mathrm{R}, \text { eff }}$.
Solution of Problem (13): The Lagrangian function of (13) is (with $\lambda_{1}$ and $\lambda_{2}$ multipliers)

$$
\begin{array}{r}
L=\left(C_{\mathrm{SD}}+C_{\mathrm{SR}}\right)-\lambda_{2}\left(C_{\mathrm{SR}}-C_{\mathrm{RD}}^{*}+s\right) \\
-\lambda_{1}\left(\sum_{i \in \mathcal{S}_{\mathrm{SD}}} P_{\mathrm{SD}}(i)+\sum_{j \in \mathcal{S}_{\mathrm{SR}}} P_{\mathrm{SR}}(j)-P_{\mathrm{S}, \text { eff }}\right)
\end{array}
$$

where $s \geq 0$ is an additional slack variable. Setting to zero the derivative of the Lagrangian function, we obtain the following stationary points

$$
P_{\mathrm{SD}}(i)=\frac{1}{\ln (2) \lambda_{1}}-\frac{1}{\gamma_{\mathrm{SD}}(i)}, P_{\mathrm{SR}}(j)=\frac{1}{\ln (2) \lambda_{1}}-\frac{1}{\gamma_{\mathrm{SR}}(j)},
$$

with $\lambda_{1}$ such that (13c) is satisfied.
Now, letting $s=C_{\mathrm{RD}}^{*}-C_{\mathrm{SR}}$, if $s \geq 0$ we have found the optimal solution. If instead $s<0$, then we must assume $s=0$, i.e., the S-R rate in stage 1 equals the R-D rate in stage 2. Consequently, we allocate the minimum power that satisfies this constraint to the S-R link, while all the remaining power is assigned to the S-D link. Hence, we first solve the following problem

$$
\begin{array}{ll}
\operatorname{argmin} & \sum_{j \in \mathcal{S}_{\mathrm{SR}}} P_{\mathrm{SR}}(j) \\
\left\{P_{\mathrm{SR}}(j)\right\}, & \text { s.t. } C_{\mathrm{SR}}=C_{\mathrm{RD}}^{*}
\end{array}
$$



Figure 2. AR versus $b$, for $P_{\mathrm{S}} / P_{\max }=0.5, N_{\mathrm{I}}=36$, and $y_{\mathrm{I}}=20 \mathrm{~m}$.
with the Lagrangian multipliers method, providing

$$
P_{\mathrm{SR}}^{*}(j)=\left[\left(\frac{2 C_{\mathrm{RD}}^{*}}{\prod_{j \in \mathcal{S}_{\mathrm{SR}}} \gamma_{\mathrm{SR}}(j)}\right)^{\frac{1}{\left|\mathcal{S}_{\mathrm{SR}}\right|}}-\frac{1}{\gamma_{\mathrm{SR}}(j)}\right]^{+},
$$

where $(x)^{+}=x$ if $x \geq 0$, while $(x)^{+}=0$ otherwise. For the obtained optimal powers $P_{\mathrm{SR}}(j)^{*}$, we solve

$$
\operatorname{argmax}_{\left\{P_{\mathrm{SD}}(i)\right\}} \quad C_{\mathrm{SD}}, \quad \text { s.t. }(13 \mathrm{c})
$$

which is similar to (12) and can be solved likewise.

## IV. NUMERICAL RESULTS

In this section, we assess the performance of the proposed protocol. $\mathrm{S}, \mathrm{R}, \mathrm{D}$, and I have coordinates $(0,0,3),(10,-10,3)$, $(20,0,1.5)$, and $\left(10, y_{\mathrm{I}}, 3\right) \mathrm{m}$, respectively (see Fig. 1), and $y_{\mathrm{I}}$ is a parameter to be set. We consider $M=2$ NLOS components for each mmWave link. S, R, and D are equipped with ULAs of $N_{\mathrm{S}}=16, N_{\mathrm{R}}=8$, and $N_{\mathrm{D}}=4$ antennas, respectively, whereas the IRS is an UPA with $N_{\mathrm{I}}=36$ elements and parameters (see [10]) $A_{\min }=0.2, \zeta=0.43 \pi$, and $\nu=1.6$. Angles in the array response vector are chosen according to a uniform random distribution, in particular, $\psi_{\text {r.m }} \sim \mathcal{U}[0,2 \pi)$ and $\xi_{\mathrm{I}, m} \sim \mathcal{U}[0, \pi / 2)$ for the IRS, while $\xi_{\text {.m }}=0$ for other devices with ULA. The transmit signalto-noise ratio (SNR) is $P_{\max } / \sigma^{2}=10(10 \mathrm{~dB})$. The path loss term is modelled as $\rho(d)=K_{0}\left(d / d_{0}\right)^{-\alpha / 2}$, where $K_{0}=\rho\left(d_{0}\right)=0 \mathrm{~dB}$ is the path loss at the reference distance $d_{0}=10 \mathrm{~m}$, and $\alpha=5.76$ is the path loss exponent [15]. We compare five schemes: the proposed optimized hybrid IRSrelay scheme (Hyb. Opt.), a hybrid scheme with random IRS configuration (Hyb. Rand.), a scheme without relay and an optimized IRS (IRS Opt.), a scheme with a random IRS (IRS Rand.), and a scheme without IRS and a relay (Relay).
Fig. 2 shows the AR as a function


---



Figure 3. AR versus $P_{\mathrm{S}} / P_{\max }$, for $y_{\mathrm{I}}=20 \mathrm{~m}, N_{\mathrm{I}}=36$, and $b=2$.



Figure 4. AR versus $y_{\mathrm{I}}$, for $P_{\mathrm{S}} / P_{\max }=0.5, N_{\mathrm{I}}=36$, and $b=2$.
$\forall n$, corresponding to the maximum value of $A(\cdot)$. For all schemes, the AR saturates with just $b=1$ or 2 bits per element, thus, as already observed in the literature, a very limited number of configurations are enough to achieve the gains provided by the IRS. In the following, we will consider $b=2$. The schemes with randomly configured IRS show a penalty for higher resolution, since configurations with lower gains $A(\cdot)$ are used.
Fig. 3 shows the AR as a function of the fractional available power at S, i.e., $P_{\mathrm{S}} / P_{\max }$ for $y_{\mathrm{I}}=20 \mathrm{~m}$. The Hyb. Opt. scheme provides the highest AR for all values of $P_{\mathrm{S}} / P_{\max }$. Still, for low $P_{\mathrm{S}} / P_{\max }$, the relay has a considerable fraction of power, thus the Relay scheme is close to optimal. Instead, at high $P_{\mathrm{S}} / P_{\max }$, the constraint on $C_{R D}$ limits the AR at the relay, and the IRS Opt. scheme attains higher performance. The IRS Rand. scheme yields very poor performance, due to the absence of the relay and the random configuration of the IRS.
Fig. 4 shows the AR as a function of the IRS distance



Figure 5. $A R$ versus $N_{\mathrm{I}}$, for $P_{\mathrm{S}} / P_{\max }=0.5, y_{\mathrm{I}}=20 \mathrm{~m}$ and $b=2$.
$y_{\mathrm{I}}$, when $P_{\mathrm{S}} / P_{\max }=0.5$. For small $y_{\mathrm{I}}$ values, the IRS link is dominant with respect to the relay link, making the Hyb. Opt. scheme transmit exclusively towards the IRS, thus avoiding the half-rate penalty of the two-stage protocol, and approaching the AR. On the other hand, the IRS assistance becomes marginal as $y_{\mathrm{I}}$ grows, resulting in similar performance between Hyb. and Relay schemes.
Finally, Fig. 5 shows the AR as a function of the number of reflecting elements $N_{\mathrm{I}}$, for $P_{\mathrm{S}} / P_{\max }=0.5$ and $y_{\mathrm{I}}=20 \mathrm{~m}$. As expected, due to the huge beamforming gain introduced by large IRSs, the AR grows with the number of reflecting elements.

## V. CONCLUSIONS

In this paper, we considered an hybrid IRS-relay system, optimizing power allocation, IRS configurations, and stream sets to maximize the AR. Numerical results showed that, in the considered scenarios, large phase-optimized IRSs yield higher ARs than systems using only either the relay or the IRS. Indeed, the best performance is achieved by different uses of the relay and the IRS under different positions of the devices or power split among the source and the relay. This suggests that the proposed hybrid solution, which is able to switch among the various uses, is always advantageous.

## REFERENCES

[1] W. Long, R. Chen, M. Moretti, W. Zhang, and J. Li, "A promising technology for 6 G wireless networks: Intelligent reflecting surface," J. of Commun. and Inf. Net., vol. 6, no. 1, pp. 1-16, 2021.
[2] E. Bjornson, O. Ozdogan, and E. G. Larsson, "Intelligent reflecting surface versus decode-and-forward: How large surfaces are needed to beat relaying?" IEEE Wireless Commun. Lett., vol. 9, no. 2, pp. 244248, Oct. 2020.
[3] C. Huang, A. Zappone, G. C. Alexandropoulos, M. Debbah, and C. Yuen, "Reconfigurable intelligent surfaces for energy efficiency in wireless communication," IEEE Trans. on Wireless Commun., vol. 18, no. 8, pp. 4157-4170, Jun. 2019.
[4] M. Di Renzo et al., "Reconfigurable intelligent surfaces vs. relaying: Differences, similarities, and performance comparison," IEEE Open J. of the Commun. Soc., vol. 1, pp. 798-807, Jun. 2020.




---

[5] Z. Abdullah, G. Chen, S. Lambotharan, and J. A. Chambers, "A hybrid relay and intelligent reflecting surface network and its ergodic performance analysis," IEEE Wireless Commun. Lett., vol. 9, no. 10, pp. 1653-1657, Oct. 2020.
[6] , "Optimization of intelligent reflecting surface assisted full-duplex relay networks," IEEE Wireless Commun. Lett., vol. 10, no. 2, pp. 363367, Feb. 2021.
[7] I. Yildirim, F. Kilinc, E. Basar, and G. C. Alexandropoulos, "Hybrid RIS-empowered reflection and decode-and-forward relaying for coverage extension," IEEE Commun. Lett., pp. 1-1, 2021.
[8] C. Huang, G. Chen, Y. Gong, M. Wen, and J. A. Chambers, "Deep reinforcement learning based relay selection in intelligent reflecting surface assisted cooperative networks," IEEE Wireless Commun. Lett., pp. 1-1, 2021.
[9] M. R. Akdeniz et al., "Millimeter wave channel modeling and cellular capacity evaluation," IEEE J. on Sel. Areas in Commun., vol. 32, no. 6, pp. 1164-1179, 2014.
[10] S. Abeywickrama, R. Zhang, Q. Wu, and C. Yuen, "Intelligent reflecting surface: Practical phase shift model and beamforming optimization," IEEE Trans. Commun., vol. 68, no. 9, pp. 5849-5863, 2020.
[11] X. Tan, Z. Sun, J. M. Jornet, and D. Pados, "Increasing indoor spectrum sharing capacity using smart reflect-array," in Proc. Int. Conf. on Commun. (ICC). IEEE, May 2016.
[12] X. Tan, Z. Sun, D. Koutsonikolas, and J. M. Jornet, "Enabling indoor mobile millimeter-wave networks based on smart reflect-arrays," in Proc. Int. Conf. on Computer Commun. (INFOCOM). IEEE, Apr. 2018.
[13] N. Benvenuto, G. Cherubini, and S. Tomasin, Algorithms for Communication Systems and their applications, 2nd ed. Wiley, 2021.
[14] J. H. Holland, Adaptation in Natural and Artificial Systems: An Introductory Analysis with Applications to Biology, Control and Artificial Intelligence. MIT Press, 1992.
[15] Y. Azar et al., " 28 GHz propagation measurements for outdoor cellular communications using steerable beam antennas in new york city," in Proc. Int. Conf. on Commun. (ICC). IEEE, Jun. 2013, pp. 5143-5147.




---

