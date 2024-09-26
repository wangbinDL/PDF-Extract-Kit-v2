# Maximum-Rate Optimization of Hybrid Intelligent Reﬂective Surface and Relay Systems  

Alberto Rech, Federico Moretto, and Stefano Tomasin Department of Information Engineering, University of Padova, Italy. Emails: rechalbert@dei.unipd.it, federico.moretto.1  $@$  unipd.it, tomasin@dei.unipd.it  

Abstract —We consider a wireless communication system, where a transmitting source is assisted by both a reconﬁgurable intelligent reﬂecting surface (IRS) and a decode-and-forward half-duplex relay ( hybrid IRS-relay scheme ) to communicate with a destination receiver. All devices are equipped with multiple antennas, and transmissions occur in two stages. In stage 1, the source splits the transmit message into two sub-messages, transmitted to the destination and the relay, respectively, using block diagonalization to avoid interference. Both transmissions will beneﬁt from the IRS. In stage 2, the relay re-encodes the received sub-message and forwards it (still through the IRS) to the destination. We optimize power allocations, beamformers, and conﬁgurations of the IRS in both stages, in order to maximize the achievable rate at the destination. We compare the proposed hybrid approach with other schemes (with/without relay and IRS), and conﬁrm that high data rate is achieved for the hybrid scheme in case of optimal IRS conﬁgurations.  

Index Terms —Beamforming, IRS, MIMO, rate optimization, relay.  

# I. I NTRODUCTION  

A reconﬁgurable intelligent reﬂecting surface (IRS) is a pro- grammable metasurface that can alter the phase and amplitude of an impinging signal by dynamically adjusting the reﬂection coefﬁcients of its elements. Recently, IRSs have drawn enor- mous research interest as a promising technology for the sixth generation (6G) of cellular networks [1], due to their ability of controlling the wireless propagation environment. Before the advent of IRSs, relays have been studied and used in cellular networks to increase coverage and improve the received signal quality. Among various solutions, decode-and-forward (DF) relays are half-duplex (HD) devices that alternate two stages, one wherein they receive a message from the source, and a second wherein they re-encode the message and transmit it to the destination.  

The alternative use of IRSs and relays has been widely investigated. In [2], IRSs and single-antenna DF relays are compared in terms of power consumption, whereas in [3] the energy efﬁciency of systems using IRSs is compared to a system with multi-antenna amplify-and-forward (AF) relays. A comparison between IRSs and DF HD/full-duplex (FD) relays is presented in [4], proving that sufﬁciently large IRSs yield higher spectral and energy efﬁciency than relay-aided systems. Nevertheless, due to the expensive deployment of IRSs,  hybrid IRS-relay systems , wherein both devices are jointly adopted, will be a cost-effective solution for the near future of smart electromagnetic environments. In [5], the combination of a HD DF relay and an IRS is investigated and tight upper bounds for the achievable rate (AR) are derived. A hybrid system with a FD DF relay is studied in [6], showing that the performance further improves, as long as the relay self-interference is low. However, both works consider source and destination equipped with a single antenna each. In [7], a system wherein an IRS assists both a relay and a destination (and the source has no direct link with either the relay and the destination) is considered, with source, relay, and destination again having all one antenna each. For a system with multiple relays, still in the presence of an IRS, the selection of one relay to assist communication between a source and a destination is solved by machine-learning in [8].  

In this paper, we consider a hybrid IRS-relay multiple- input multiple-output (MIMO) system, which generalizes the systems considered in [5], [6], and [7], as we now assume that all devices are equipped with multiple antennas. Moreover, contrary to [7], we also consider the link between the source and the relay. The relay is HD and operates in the DF mode. We propose a transmission protocol operating in two stages. In stage 1, the source splits the transmit message into two sub-messages, transmitted to the destination and the relay, respectively, using block diagonalization to avoid interference. Both transmissions will beneﬁt from the IRS. In stage 2, the relay re-encodes the received sub-message and forwards it (still through the IRS) to the destination. We optimize power allocations, beamformers, and conﬁgurations of the IRS in both stages, to maximize the AR at the destination. In particular, we split the AR optimization problem into two sub- problems, one for each stage, then coupled by the choice of the IRS conﬁguration and the power split between the signal for the relay and the destination in stage 1. Lastly, we compare the proposed hybrid approach with other schemes (with/without relay and IRS), and conﬁrm that a high data rate is achieved for the hybrid scheme in case of optimal IRS conﬁguration.  

The rest of this paper is organized as follows. Section II de- scribes transmission characteristics and the two-stage protocol. In Section III we formalize the maximum-rate optimization problem and describe the alternating optimization solution. In Section IV we discuss numerical results before the conclusions are taken in Section V.  

Notation:  Scalars are denoted by italic letters, vectors and matrices by boldface lowercase and uppercase letters, respec- tively, and sets are denoted by calligraphic uppercase letters.  $\operatorname{diag}(a)$   indicates a square diagonal matrix with the elements of    $^{a}$   on the principal diagonal.    $A^{H}$    denotes the conjugate  

![](images/c18fe8f6592de6549bcf0c6e6bef642096d460614767eec500d440e7ac2ca182.jpg)  

Figure 1. Two-stage IRS- and relay-assisted MIMO system. Solid arrows represent the S-D link in stage 1, dashed arrows the S-R link in stage 1, and dotted arrows the R-D link in stage 2.  

nspose of matrix    $A.\;\mathbb{E}[\cdot]$   deno s the statistical expectation.  $I_{x}$   is the identity matrix of size  x .  

# II. SYSTEM MODEL  

We consider the narrowband single-user MIMO communi- cation system shown in Fig. 1, wherein the transmission from a source (S) to a destination (D) is assisted by both a relay (R) and an IRS (I). We assume that S and R have maximum transmit powers    $P_{\mathrm{{S}}}$   and    $P_{\mathrm{{R}}}$  , respectively.  

S, D, and  $\mathbf{R}$   are equipped with uniform linear arrays (ULAs) with    $N_{\mathrm{S}},\ N_{\mathrm{D}}$  , and    $N_{\mathrm{R}}$   antennas, respectively, whereas I is a uniform planar array (UPA) with    $N_{\mathrm{I}}$   passive reﬂective elements.  

We denote with    $H_{\mathrm{SI}}\,\in\,\mathbb{C}^{N_{\mathrm{I}}\times N_{\mathrm{S}}}$   $H_{\mathrm{SR}}\in\mathbb{C}^{N_{\mathrm{R}}\times N_{\mathrm{S}}}$   S-I channels, with  $H_{\mathrm{RI}}\ \in\ \mathbb{C}^{N_{\mathrm{I}}\times N_{\mathrm{R}}}$   ∈    $H_{\mathrm{RD}}\ \in$   $\mathbb{C}^{N_{\mathrm{D}}\times N_{\mathrm{R}}}$    the R-I and R-D channels, and with  $H_{\mathrm{IR}}\,=\,H_{\mathrm{RI}}^{T}$  and    $H_{\mathrm{ID}}\in\mathbb{C}^{N_{\mathrm{D}}\times N_{\mathrm{I}}}$    the I-R and I-D channels.  e consider narrowband mmWave channels [9], each having  M  non-line- of-sight (NLOS) components. Hence, channel matrix    $H_{\mathrm{XY}}$  between transmitter  X  and receiver    $\mathrm{Y}$   is  

$$
\pmb{H}_{\mathrm{XY}}=\frac{1}{\sqrt{M}}\sum_{m=1}^{M}g_{m}\rho(d)\pmb{a}\left(\omega_{\mathrm{X},m}\right)\pmb{a}^{H}\left(\omega_{\mathrm{Y},m}\right),
$$  

where    $g_{m}\;\sim\;{\mathcal{C N}}(0,1)$   is the gain of  e    $m$  -th path,    $\rho(d)$  is the path loss attenuation factor, with  d  being the distance between   $\mathrm{X}$   and   $\mathrm{Y}_{2}$     $\pmb{\omega}_{\cdot,m}\;\;=\;\;\left(\xi_{\cdot,m},\psi_{\cdot,m}\right)$   is the vector of azimuth   $(\xi_{\cdot,m})$   and elevation   $(\psi_{\cdot,m})$   angles, and    $\mathbfcal{\mathbf{a}}\left(\pmb{\omega}_{\underline{{\mathbf{\delta\}}},m}\right)\mathbf{\delta=}$   $\left(1,\ldots,e^{j\pi\left[x\sin\left(\psi_{\cdot,m}\right)\cos\left(\xi_{\cdot,m}\right)+y\sin\left(\psi_{\cdot,m}\right)\sin\left(\xi_{\cdot,m}\right)\right]},\ldots\right)^{T}$  arra for the    $m$  -th path, with  $1\leq x\leq N_{\mathrm{X}}-1$   ≤  ≤  − and  $1\leq y\leq N_{\mathrm{Y}}-1$   ≤  ≤  − . We assume all devices operate in HD and have perfect channel state information.  

# A. IRS Model  

Each element of the IRS acts as an omnidirectional antenna element that captures and reﬂects signals, introducing an atten- uation and a phase shift on the baseband-equivalent signal. Fol- lowing the model of [10], we denote with    $\phi_{n}=A_{n}(\theta_{n})e^{j\theta_{n}}$  the reﬂection coefﬁcient of the    $n$  -th IRS element, where  $\theta_{n}\in[-\pi,\pi)$   is the induced phase shift and    $A_{n}^{2}(\theta_{n})\in[0,1]$   ∈ is the corresponding power attenuation factor. Indicating with  $\pmb{x}\,\in\,\mathbb{C}^{1\times N_{\mathrm{I}}}$  mpinging signal on the IRS, the reﬂected signal  $\pmb{y}\in\mathbb{C}^{1\times N_{\mathrm{I}}}$   ∈   is    $\pmb{y}=\pmb{\Phi}\pmb{x}$  , with    $\Phi=\mathrm{diag}(\phi_{1},.\,.\,.\,,\phi_{N_{\mathrm{I}}})$  , which is the IRS reﬂection matrix, also denoted  IRS conﬁgu- ration .  

We consider the realistic baseband-equivalent model of the IRS described in [10], where  

$$
A_{n}(\theta_{n})=(1-A_{\operatorname*{min}})\left(\frac{\sin\theta_{n}-\zeta+1}{2}\right)^{\nu}+A_{\operatorname*{min}},
$$  

with    $A_{\mathrm{min}}~\geq~0,~\zeta~\geq~0.$  , and    $\nu~\geq~0$   being IRS-speciﬁc parameters, assumed to be identical for all IRS elements. The phase shifts    $\theta_{n}$   are controllable, thus indirectly con- trolling also the attenuations. Moreover, since continuous- phase shifts are hardly implementable [11]-[12], we assume  $\left\{0,{\frac{2\pi}{2^{b}}},\dot{\cdot}\cdot\cdot,{\frac{2\pi(2^{b}\!-\!1)}{2^{b}}}\right\}$  that the phase shifts are chosen from a discrete set o , where    $b\,>\,0$   is the IRS phase shift    $\mathcal{F}_{\theta}~=$  resolution, i.e., the number of bits employed to control the phase shifts. The source has full control of the phase shifts, which can be optimized together with beamforming.  

# B. Two-stage Communication Protocol  

For a HD DF relay, signal reception and transmission have to occur in two stages, here assumed to be of the same duration.  

Stage 1:  S splits the message into two sub-messages, and encodes/modulates them into the two signals    ${\pmb x}_{\mathrm{SR}}$   and  ${\pmb x}_{\mathrm{SD}}$  , intended for R and D, respectively. The two signals are precoded with block diagonalization (BD) precoders    $B_{\mathrm{SR}}$   and  $B_{\mathrm{SD}}$   before transmission, such that they are received only at the indented destination, without mutual interference. The signal transmitted by S is thus  

$$
\pmb{s}=B_{\mathrm{SR}}\pmb{x}_{\mathrm{SR}}+B_{\mathrm{SD}}\pmb{x}_{\mathrm{SD}}.
$$  

Then, for a given IRS conﬁguration    $\Phi_{1}$  , the received signals at   $\mathbf{R}$   and   $\mathrm{D}$   are, respectively,  

$$
\pmb{y}_{R,1}=\underbrace{(\pmb{H}_{\mathrm{SR}}+\pmb{H}_{\mathrm{IR}}\pmb{\Phi}_{1}\pmb{H}_{\mathrm{SI}})\pmb{B}_{\mathrm{SR}}}_{\tilde{H}_{\mathrm{SR}}(\pmb{\Phi}_{1})}\pmb{x}_{\mathrm{SR}}+\pmb{n}_{R,1},
$$  

$$
\pmb{y}_{D,1}=\underbrace{\pmb{H}_{\mathrm{ID}}\pmb{\Phi}_{1}\pmb{H}_{\mathrm{SI}}\pmb{B}_{\mathrm{SD}}}_{\tilde{H}_{\mathrm{SD}}(\pmb{\Phi}_{1})}\pmb{x}_{\mathrm{SD}}+\pmb{n}_{D,1},
$$  

where  $\tilde{H}_{\mathrm{SR}}(\Phi_{1})\;\;\;(\tilde{H}_{\mathrm{SD}}(\Phi_{1}))$  ) is the S-R (S-D) equiva- lent channel matrix (we highlight their dependency on the on), and    $\pmb{n}_{R,1}~\sim~\mathcal{C N}\left(0,\sigma^{2}\pmb{I}_{N_{\mathrm{R}}}\right){}~(\pmb{n}_{D,1}{}~\sim$    

  $\mathcal{C N}\left(0,\sigma^{2}\mathbf{\bar{I}}_{N_{\mathrm{D}}}\right))$  CN    ) is the complex Gaussian noise vector at R

 (D).  

Stage 2:  S remains silent, while R decodes the sub- message received by S in stage 1 and re-encodes/re-modulates it into the signal    ${\pmb x}_{\mathrm{RD}}$  . Then,   $\mathbf{R}$   transmits    ${\pmb x}_{\mathrm{RD}}$   to   $\mathrm{D}$   with the IRS using a new conﬁguration  $\Phi_{2}$  . D receives the signal vector  

$$
\pmb{y}_{D,2}=\underbrace{\left(\pmb{H}_{\mathrm{RD}}+\pmb{H}_{\mathrm{ID}}\Phi_{2}\pmb{H}_{\mathrm{RI}}\right)}_{\pmb{H}_{\mathrm{RD}}(\Phi_{2})}\pmb{x}_{\mathrm{RD}}+\pmb{n}_{D,2},
$$  

where  $\tilde{H}_{\mathrm{RD}}(\Phi_{2})$   is the R-D equivalent channel matrix, and  $\pmb{n}_{D,2}\sim\mathcal{C N}\left(0,\sigma^{2}\pmb{I}_{N_{\mathrm{D}}}\right)$     is the complex Gaussian noise vectors at  D .  

Note that, in both stages, the IRS conﬁgurations  $\Phi_{1}$   and    $\Phi_{2}$  are provided by S, which has full control of the phase shifts.  

# III. M AXIMUM -R ATE  P ROBLEM  

We now ﬁrst derive the AR and then, we formulate the problem of maximizing the AR.  

# A. Achievable Rate  

For the ﬁrst stage, the transmit beamformers    $B_{\mathrm{SD}}$   and  $B_{\mathrm{SR}}$   are chosen such that    ${\pmb x}_{\mathrm{SR}}$   and    ${\pmb x}_{\mathrm{SD}}$   do not generate interference at   $\mathrm{D}$   and R, respectively. To this end, BD is applied (see [13]), using in general a reduced set of streams for the two links. Let    $H_{\mathrm{SD}}=U_{\mathrm{SD}}\mathbf{\Gamma}_{\mathrm{SD}}V_{\mathrm{SD}}$   and the singular value decomposition (SVD) of    $H_{\mathrm{SD}}$  ; a s    $S_{\mathrm{SD}}$   of streams (corresponding to diagonal elements of  $\Gamma_{S D.}$  ) is selected for transmission to D. The BD beamformer for transmission to   $\mathbf{R}$  is    $B_{\mathrm{SR}}=N_{\mathrm{SD}}B_{\mathrm{SR}}^{\prime}.$  , where    $N_{\mathrm{SD}}$   collects the columns of    $V_{\mathrm{SD}}$  with indices not in the set    $S_{\mathrm{SD}}$  , while    $B_{\mathrm{SR}}^{\prime}$    is the capacity- achieving precoder for the resulting S-R channel. A similar procedure is applied for the deﬁnition of the S-D precoder  $B_{\mathrm{SD}}$  , for which    $S_{\mathrm{SR}}$   streams are selected. We must also have  $|\mathcal{S}_{\mathrm{SR}}|+|\mathcal{S}_{\mathrm{SR}}|\,\leq\,N_{\mathrm{S}}$  . Lastly,    ${\pmb x}_{S D}$   and    ${\pmb x}_{S R}$  , are zero-mean complex Gaussian vectors with independent entries of size  $|S_{\mathrm{SD}}|$   and    $|S_{\mathrm{SR}}|$  .  

For the second stage, R applies capacity-achieving pre- coding, and    ${\bf x}_{R D}$   zero-mean complex Gaussian vectors with independent entries of size  $N_{\mathrm{R}}$  .  

As a result, the S-D MIMO equivalent channel can be decomposed into    $|S_{\mathrm{SD}}|$   independent parallel additive white Gaussian noise (AWGN) channels with gains    $\{\gamma_{\mathrm{SD}}(i)\}$  .   The capacity of the S-D channel is therefore  

$$
C_{\mathrm{SD}}=\sum_{i\in S_{\mathrm{SD}}}\log_{2}\left[1+\gamma_{\mathrm{SD}}(i)\frac{P_{\mathrm{SD}}(i)}{\sigma^{2}}\right],
$$  

where    $P_{\mathrm{SD}}(i)$   is the power allocated to channel    $i$  . Similarly, the S-R and R-D channels can be decomposed into    $|S_{\mathrm{SR}}|$  and    $|S_{\mathrm{RD}}|$   parallel AWGN channels, with gains    $\{\gamma_{\mathrm{SR}}(i)\}$   and  $\{\gamma_{\mathrm{RD}}(i)\}$     $C_{\mathrm{SR}}$  and  C  $C_{\mathrm{RD}}$   can be written as in (7), where subscript SD is replaced by subscripts SR and RD, respectively.  

The AR of the considered two-stage scheme is therefore  

$$
C_{\mathrm{HYB}}=\frac{1}{2}(C_{\mathrm{SD}}+\operatorname*{min}\{C_{\mathrm{SR}},C_{\mathrm{RD}}\}),
$$  

where the two stages requires twice the time of direct trans- mission, hence the factor   $1/2$  .  

Note that for a transmission using only the relay, the AR  $C_{\mathrm{relay}}$   is still given by (8), with the IRS switched off   $(A_{n}(\theta)=$   $0,\ \forall\theta)$  . A transmission using only the IR  be performed in a single stage and the AR is  $C_{\mathrm{IRS}}\,=\,C_{\mathrm{SD}}$  . In both cases, no BD is needed. Note also that IRS- or relay-only transmissions occur if no streams are selected for the S-R or S-D links, i.e., if  $|\mathcal{S}_{\mathrm{SR}}|=0$   or  $|\mathcal{S}_{\mathrm{SD}}|=0$  , respectively.  

B. Optimization Problem  

With this choice of beamformers, we are left with the problem of optimizing a) the transmit power, b) the IRS conﬁgurations in both stages, and c) the set of streams assigned to  $\mathbf{R}$   and   $\mathrm{D}$   in stage 1. The AR maximization problem can be formalized as follows:  

$$
\begin{array}{r l r}&{}&{\underset{\Phi_{1},\Phi_{2}}{\mathrm{argmax}}\quad\left(C_{\mathrm{SD}}+C_{\mathrm{SR}}\right),}\\ &{}&{\mathcal{S}_{\mathrm{SD}},\mathcal{S}_{\mathrm{SR}},\mathcal{S}_{\mathrm{RD}}}\\ &{}&{\{P_{\mathrm{SD}}(i)\},\{P_{\mathrm{SR}}(j)\},\{P_{\mathrm{RD}}(k)\}}\end{array}
$$  

$$
\phi_{n,k}=A_{n,k}(\theta_{n,k})e^{j\theta_{n,k}},\quad1\leq n\leq N_{\mathrm{I}},\quad k=1,2,
$$  

$$
\begin{array}{r l r}&{\theta_{n,k}\in\mathcal{F}_{\theta},\quad1\leq n\leq N_{\mathrm{I}},\quad k=1,2,}&{\quad{\quad\quad}(9\mathrm{d})}\\ &{\displaystyle\sum_{i\in S_{\mathrm{SD}}}P_{\mathrm{SD}}(i)+\displaystyle\sum_{j\in S_{\mathrm{SR}}}P_{\mathrm{SR}}(j)\leq P_{\mathrm{S}},}&{\quad{\quad\quad}(9\mathrm{c})}\\ &{\displaystyle\sum_{k\in S_{\mathrm{RD}}}P_{\mathrm{RD}}(k)\leq P_{\mathrm{R}},}&{\quad{\quad\quad}(9\mathrm{i})}\\ &{\displaystyle\sum_{i\in S_{\mathrm{SD}}}P_{\mathrm{SD}}(i)+\displaystyle\sum_{j\in S_{\mathrm{SR}}}P_{\mathrm{SR}}(j)+\displaystyle\sum_{k\in S_{\mathrm{RD}}}P_{\mathrm{RD}}(k)\leq P_{\mathrm{max}},}&\end{array}
$$  

$$
\begin{array}{r l}&{C_{\mathrm{SR}}\leq C_{\mathrm{RD}}}\\ &{S_{\mathrm{SD}},\mathcal{S}_{\mathrm{SR}}\in\{1,\ldots,N_{\mathrm{S}}\},}\\ &{0<|\mathcal{S}_{\mathrm{SD}}|+|\mathcal{S}_{\mathrm{SR}}|\leq N_{\mathrm{S}}.}\end{array}
$$  

The minimum in (8) is now reﬂected by constraint (9h). Constraints (9b)-(9d) are related to the control of IRS phase shifts, and constraints   $(9\mathrm{e})$   and   $(9\mathrm{g})$   are power constraints at the devices, and we added the total power constraint    $P_{\mathrm{max}}$  . This constraint will make the comparison with schemes using only the IRS more fair, by imposing  $P_{\mathrm{max}}$   the maximum power for S. Constraints (9i)-(9j) are relative to the stream assignment.  

# C. Alternating Optimization Solution  

Notice that constraint   $(9\mathrm{c})$   makes the problem non-convex, thus we resort to an alternating optimization solution, where we optimize over the IRS conﬁgurations and stream sets, and for each considered conﬁguration we optimize the transmis- sion powers.  

For ﬁxed IRS conﬁgurations and stream selections, the optimization problem (9) becomes  

$$
\begin{array}{r}{\underset{\{P_{\mathrm{SD}}(i)\},\{P_{\mathrm{SR}}(j)\},\{P_{\mathrm{RD}}(k)\}}{\mathrm{argmax}}\left(C_{\mathrm{SD}}+C_{\mathrm{SR}}\right),\quad\mathrm{s.t.~(9e)-(9h)}.}\end{array}
$$  

Observe that, due to constraint (9h), the problem is still non- convex. However, the powers in stage 1 and stage 2 are coupled only through the constraint   $(9\mathrm{g})$  . We can decouple the two problems by introducing the auxiliary variable    $P_{\mathrm{R,eff}}$  such that  

$$
\sum_{k\in\mathcal{S}_{\mathrm{RD}}}P_{\mathrm{RD}}(k)=P_{\mathrm{R,eff}},
$$  

so that the power that can be effectively used by S is, from (9e), (9f), and   $(9\mathrm{g})$  , as    $P_{\mathrm{S,eff}}=\mathrm{min}\{P_{\mathrm{S}},P_{\mathrm{max}}-P_{\mathrm{R,eff}}\}$  . With these new deﬁnitions, (10) can be split into the two (coupled) problems, for given    $P_{\mathrm{R,eff}}$  ,  

$$
C_{\mathrm{RD}}^{*}=\operatorname*{max}_{\{P_{\mathrm{RD}}(k)\}}C_{\mathrm{RD}},\quad\mathrm{s.t.}\sum_{k\in S_{\mathrm{RD}}}P_{\mathrm{RD}}(k)=P_{\mathrm{R,eff}},
$$  

and  

$$
\underset{\{P_{\mathrm{SD}}(i)\},\{P_{\mathrm{SR}}(j)\}}{\mathrm{argmax}}\,\frac{1}{2}\left(C_{\mathrm{SD}}+C_{\mathrm{SR}}\right),
$$  

$$
\begin{array}{r l r}{\lefteqn{C_{\mathrm{SR}}\leq C_{\mathrm{RD}}^{*},}}\\ &{}&{\sum_{i\in S_{\mathrm{SD}}}P_{\mathrm{SD}}(i)+\sum_{j\in S_{\mathrm{SR}}}P_{\mathrm{SR}}(j)=P_{\mathrm{S,eff}}.}\end{array}
$$  

Note that (12) and (13) are convex optimization problems and, therefore, they can be solved in closed-form, as detailed in the next sub-section.  

Then, we need to optimize the IRS reﬂection coefﬁcients  $\Phi_{1}$  and    $\Phi_{2}$  , the stream sets  $\mathcal{S}_{\mathrm{SR}},\mathcal{S}_{\mathrm{SD}}$  , and  $S_{\mathrm{RD}}$  , and the auxiliary variable  $P_{\mathrm{R,eff}}$  , in what turns out to be a non-convex problem. Thus, we resort to the discrete genetic algorithm (GA) [14], which operates iteratively, solving sub-problems (13) and (12) for given IRS conﬁgurations, power    $P_{\mathrm{R,eff}}$  , stream sets    $\ensuremath{\mathcal{S}}_{\mathrm{SR}}$  ,  $\ensuremath{\mathcal{S}}_{\mathrm{SD}}$  , and    $S_{\mathrm{RD}}$   at each iteration.  

#  $D$  . Decoupled Problem Solution  

Solution of Problem  (12) :  Since the capacity    $C_{\mathrm{SR}}$   is upper bounded by    $C_{\mathrm{RD}}^{\ast}$    from (13b), we ﬁrst optimize the transmit powers    $\{P_{\mathrm{RD}}(k)\}$   at   $\mathbf{R}$  , given    $P_{\mathrm{R,eff}}$  . Indeed, (12) can be solved via the standard waterﬁlling algorithm [13] on channels with gains  $\{\gamma_{\mathrm{RD}}(i)\}$   and total power    $P_{\mathrm{R,eff}}$  .  

Solution of Problem  (13) :  The Lagrangian function of (13) is (with    $\lambda_{1}$   and    $\lambda_{2}$   multipliers)  

$$
\begin{array}{l}{\mathcal{L}=\left(C_{\mathrm{SD}}+C_{\mathrm{SR}}\right)-\lambda_{2}\left(C_{\mathrm{SR}}-C_{\mathrm{RD}}^{*}+s\right)}\\ {\quad-\lambda_{1}\left(\sum_{i\in S_{\mathrm{SD}}}P_{\mathrm{SD}}(i)+\sum_{j\in S_{\mathrm{SR}}}P_{\mathrm{SR}}(j)-P_{\mathrm{S,eff}}\right),}\end{array}
$$  

where    $s\geq0$   is an additional slack variable. Setting to zero the derivative of the Lagrangian function, we obtain the following stationary points  

$$
P_{\mathrm{SD}}(i)=\frac{1}{\ln(2)\lambda_{1}}-\frac{1}{\gamma_{\mathrm{SD}}(i)},\;P_{\mathrm{SR}}(j)=\frac{1}{\ln(2)\lambda_{1}}-\frac{1}{\gamma_{\mathrm{SR}}(j)},
$$  

with    $\lambda_{1}$   such that (13c) is satisﬁed.  

Now, letting    $s\,=\,C_{\mathrm{RD}}^{*}\mathrm{~-~}C_{\mathrm{SR}}$    −  $s\,\geq\,0$   we have found the optimal solution. If instead  $s<0$  , then we must assume  $s\,=\,0$  , i.e., the S-R rate in stage  1  equals the R-D rate in stage  2 . Consequently, we allocate the minimum power that satisﬁes this constraint to the S-R link, while all the remaining power is assigned to the S-D link. Hence, we ﬁrst solve the following problem  

$$
\frac{\mathrm{argmin}}{\{P_{\mathrm{SR}}(j)\}}\sum_{j\in S_{\mathrm{SR}}}P_{\mathrm{SR}}(j),\quad\mathrm{~s.t.~}\,C_{\mathrm{SR}}=C_{\mathrm{RD}}^{*},
$$  

![](images/3cf34839d9ea0c8066efd4de4318af0d4febdcb550506c12b33e54850d068a28.jpg)  
Figure 2. AR versus    $b$  , for  $P_{\mathrm{S}}/P_{\mathrm{max}}=0.5$  ,    $N_{I}=36$  , and    $y_{\mathrm{I}}=20~\mathrm{m}$  .  

with the Lagrangian multipliers method, providing  

$$
P_{\mathrm{SR}}^{*}(j)=\left[\left(\frac{2^{C_{\mathrm{RD}}^{*}}}{\prod_{j\in\mathcal{S}_{\mathrm{SR}}}\gamma_{\mathrm{SR}}(j)}\right)^{\frac{1}{|\mathcal{S}_{\mathrm{SR}}|}}-\frac{1}{\gamma_{\mathrm{SR}}(j)}\right]^{+},
$$  

where    $(x)^{+}=x$   if  $x\ge0$  , while    $(x)^{+}=0$   otherwise. For the obtained optimal powers    $P_{\mathrm{SR}}(j)^{*}$  , we solve  

$$
\begin{array}{r l}{\mathrm{argmax}\ C_{\mathrm{SD}},}&{{}\ \ \mathrm{s.t.}\ \ (13\mathrm{c}),}\\ {\{P_{\mathrm{SD}}(i)\}}\end{array}
$$  

which is similar to (12) and can be solved likewise.  

# IV. N UMERICAL  R ESULTS  

In this section, we assess the performance of the proposed protocol. S, R, D, and I have coordinates    $(0,0,3)$  ,  $(10,-10,3)$  ,  $(20,0,1.5)$  , and    $(10,y_{\mathrm{I}},3)\textbf{m}$  , respectively (see Fig. 1), and  $y_{\mathrm{I}}$   is a parameter to be set. We consider    $M~=~2$   NLOS components for each mmWave link. S, R, and   $\mathrm{D}$   are equipped with ULAs of    $N_{\mathrm{S}}\,=\,16$  ,    $N_{\mathrm{R}}\,=\,8$  , and    $N_{\mathrm{D}}\,=\,4$   antennas, respectively, whereas the IRS is an UPA with    $N_{\mathrm{I}}~=~36$  elements and parameters (see [10])    $A_{\mathrm{min}}\,=\,0.2$  ,    $\zeta=0.43\pi$  , and    $\nu=1.6$  . Angles in the array response vector are chosen according to a uniform random distribution, in particular,

  $\psi_{\cdot,m}\,\sim\,\mathcal{U}[0,2\pi)$   and    $\xi_{\mathrm{I},m}\,\sim\mathcal{U}[0,\pi/2)$   for the IRS, while

  $\xi_{\cdot,m}\,=\,0$   for other devices with ULA. The transmit signal- · to-noise ratio (SNR) is    $P_{\mathrm{max}}/\sigma^{2}\;=\;10$   ( 10  dB). The path loss term is modelled as    $\rho(d)~=~K_{0}(d/d_{0})^{-\alpha/2}$  , where  $K_{0}=\rho(d_{0})=0$   dB is the path loss at the reference distance  $d_{0}=10\ \mathrm{m}$  , and    $\alpha=5.76$   is the path loss exponent [15]. We compare ﬁve schemes: the proposed optimized hybrid IRS- relay scheme ( Hyb. Opt. ), a hybrid scheme with random IRS conﬁguration ( Hyb. Rand. ), a scheme without relay and an optimized IRS ( IRS Opt. ), a scheme with a random IRS ( IRS Rand. ), and a scheme without IRS and a relay ( Relay ).  

Fig. 2 shows the AR as a function of the IRS phase shift resolution  $b$   for  $y_{\mathrm{I}}=20~\mathrm{m}$   and  $\mathrm{\mathit{P}_{S}}/\mathrm{\mathit{P}_{max}}=0.5.$  . For  $b=0$   we consider a ﬁxed IRS conﬁguration with phase shifts    $\theta_{n}=\pi$  ,  

![](images/609485715dc084e8c1538408acc947d6a5e6f57144dde6f6a2dc2d2d3535e76b.jpg)  
Figure 3. AR versus  $P_{\mathrm{S}}/P_{\mathrm{max}}$  , for  $y_{\mathrm{I}}=20~\mathrm{m}$  ,  $N_{I}=36$  , and  $b=2$  .  

![](images/3a3237bca410f94c2b095143bb4eeb14eb20627ad7934f27aa93d09adf384564.jpg)  
Figure 4. AR versus  $y_{\mathrm{I}}$  , for  $P_{\mathrm{S}}/P_{\mathrm{max}}=0.5$  ,    $N_{I}=36$  , and    $b=2$  .  

$\forall n$  , corresponding to the maximum     $A(\cdot)$  . For all schemes, the AR saturates with just  b  $b~=~1$   or  2  bits per element, thus, as already observed in the literature, a very limited number of conﬁgurations are enough to achieve the gains provided by the IRS. In the following, we will consider  $b\,=\,2$  . The schemes with randomly conﬁgured IRS show a penalty for higher resolution, since conﬁgurations with lower gains    $A(\cdot)$   are used.  

Fig. 3 shows the AR as a function of the fractional available power at S, i.e.,    $P_{\mathrm{S}}/P_{\mathrm{max}}$   for  $y_{\mathrm{I}}=20~\mathrm{m}$  . The  Hyb. Opt. scheme provides the highest AR for all values of    $P_{\mathrm{S}}/P_{\mathrm{max}}$  Still, for low    $P_{\mathrm{S}}/P_{\mathrm{max}}$  , the relay has a considerable fraction of power, thus the  Relay  scheme is close to optimal. Instead, at high    $P_{\mathrm{S}}/P_{\mathrm{max}}$  , the constraint on  $C_{\mathrm{RD}}$   limits the AR at the relay, and the  IRS Opt.  scheme attains higher performance. The  IRS Rand.  scheme yields very poor performance, due to the absence of the relay and the random conﬁguration of the IRS.  

Fig. 4 shows the AR as a function of the IRS distance  

![](images/7508981af3863a336bbbb638482994a6b833559e63c5b1b9f032e1022acaf0b4.jpg)  
Figure 5. AR versus    $N_{\mathrm{I}}$  , for    $P_{\mathrm{S}}/P_{\mathrm{max}}=0.5$  ,  $y_{\mathrm{I}}=20~\mathrm{m}$   and    $b=2$  .  

$y_{\mathrm{I}}$  , when    $P_{\mathrm{S}}/P_{\mathrm{max}}~=~0.5$  . For small    $y_{\mathrm{I}}$   values, the IRS link is dominant with respect to the relay link, making the Hyb. Opt.  scheme transmit exclusively towards the IRS, thus avoiding the half-rate penalty of the two-stage protocol, and approaching the AR. On the other hand, the IRS assistance becomes marginal as    $y_{\mathrm{I}}$   grows, resulting in similar perfor- mance between  Hyb.  and  Relay  schemes.  

Finally, Fig. 5 shows the AR as a function of the number of reﬂecting elements    $N_{\mathrm{I}}$  , for    $P_{\mathrm{S}}/P_{\mathrm{max}}=0.5$   and    $y_{\mathrm{I}}=20~\mathrm{m}$  . As expected, due to the huge beamforming gain introduced by large IRSs, the AR grows with the number of reﬂecting elements.  

# V. C ONCLUSIONS  

In this paper, we considered an hybrid IRS-relay system, optimizing power allocation, IRS conﬁgurations, and stream sets to maximize the AR. Numerical results showed that, in the considered scenarios, large phase-optimized IRSs yield higher ARs than systems using only either the relay or the IRS. Indeed, the best performance is achieved by different uses of the relay and the IRS under different positions of the devices or power split among the source and the relay. This suggests that the proposed hybrid solution, which is able to switch among the various uses, is always advantageous.  

# R EFERENCES  

[1] W. Long, R. Chen, M. Moretti, W. Zhang, and J. Li, “A promising technology for 6G wireless networks: Intelligent reﬂecting surface,”  J. of Commun. and Inf. Net. , vol. 6, no. 1, pp. 1–16, 2021.

 [2] E. Bjornson, O. Ozdogan, and E. G. Larsson, “Intelligent reﬂecting surface versus decode-and-forward: How large surfaces are needed to beat relaying?”  IEEE Wireless Commun. Lett. , vol. 9, no. 2, pp. 244– 248, Oct. 2020.

 [3] C. Huang, A. Zappone, G. C. Alexandropoulos, M. Debbah, and C. Yuen, “Reconﬁgurable intelligent surfaces for energy efﬁciency in wireless communication,”  IEEE Trans. on Wireless Commun. , vol. 18, no. 8, pp. 4157–4170, Jun. 2019.

 [4] M. Di Renzo  et al. , “Reconﬁgurable intelligent surfaces vs. relaying: Differences, similarities, and performance comparison,”  IEEE Open J. of the Commun. Soc. , vol. 1, pp. 798–807, Jun. 2020.  

[5] Z. Abdullah, G. Chen, S. Lambotharan, and J. A. Chambers, “A hybrid relay and intelligent reﬂecting surface network and its ergodic performance analysis,”  IEEE Wireless Commun. Lett. , vol. 9, no. 10, pp. 1653–1657, Oct. 2020.

 [6] ——, “Optimization of intelligent reﬂecting surface assisted full-duplex relay networks,”  IEEE Wireless Commun. Lett. , vol. 10, no. 2, pp. 363– 367, Feb. 2021.

 [7] I. Yildirim, F. Kilinc, E. Basar, and G. C. Alexandropoulos, “Hybrid RIS-empowered reﬂection and decode-and-forward relaying for cover- age extension,”  IEEE Commun. Lett. , pp. 1–1, 2021.

 [8] C. Huang, G. Chen, Y. Gong, M. Wen, and J. A. Chambers, “Deep reinforcement learning based relay selection in intelligent reﬂecting surface assisted cooperative networks,”  IEEE Wireless Commun. Lett. , pp. 1–1, 2021.

 [9] M. R. Akdeniz  et al. , “Millimeter wave channel modeling and cellular capacity evaluation,”  IEEE J. on Sel. Areas in Commun. , vol. 32, no. 6, pp. 1164–1179, 2014.

 [10] S. Abeywickrama, R. Zhang, Q. Wu, and C. Yuen, “Intelligent reﬂecting surface: Practical phase shift model and beamforming optimization,” IEEE Trans. Commun. , vol. 68, no. 9, pp. 5849–5863, 2020.

 [11] X. Tan, Z. Sun, J. M. Jornet, and D. Pados, “Increasing indoor spectrum sharing capacity using smart reﬂect-array,” in  Proc. Int. Conf. on Commun. (ICC) . IEEE, May 2016.

 [12] X. Tan, Z. Sun, D. Koutsonikolas, and J. M. Jornet, “Enabling indoor mobile millimeter-wave networks based on smart reﬂect-arrays,” in  Proc. Int. Conf. on Computer Commun. (INFOCOM) . IEEE, Apr. 2018.

 [13] N. Benvenuto, G. Cherubini, and S. Tomasin,  Algorithms for Commu- nication Systems and their applications , 2nd ed. Wiley, 2021.

 [14] J. H. Holland,  Adaptation in Natural and Artiﬁcial Systems: An Intro- ductory Analysis with Applications to Biology, Control and Artiﬁcial Intelligence . MIT Press, 1992.

 [15] Y. Azar  et al. , “28 GHz propagation measurements for outdoor cellular communications using steerable beam antennas in new york city,” in Proc. Int. Conf. on Commun. (ICC) . IEEE, Jun. 2013, pp. 5143–5147.  