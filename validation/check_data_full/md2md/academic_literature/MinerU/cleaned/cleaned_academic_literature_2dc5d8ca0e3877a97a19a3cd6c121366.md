# Joint Relay Selection and Beam Management Based on Deep Reinforcement Learning for Millimeter Wave Vehicular Communication  

Dohyun Kim, Miguel R. Castellanos,  Member, IEEE , and Robert W. Heath Jr.,  Fellow, IEEE  

# Abstract  

Cooperative relays improve reliability and coverage in wireless networks by providing multiple paths for data transmission. Relaying will play an essential role in vehicular networks at higher frequency bands, where mobility and frequent signal blockages cause link outages. To ensure connectivity in a relay-aided vehicular network, the relay selection policy should be designed to efﬁciently ﬁnd unblocked relays. Inspired by recent advances in beam management in mobile millimeter wave (mmWave) networks, this paper address the question:  how can the best relay be selected with minimal overhead from beam management?  In this regard, we formulate a sequential decision problem to jointly optimize relay selection and beam management. We propose a joint relay selection and beam management policy based on deep reinforcement learning (DRL) using the Markov property of beam indices and beam measurements. The proposed DRL-based algorithm learns time-varying thresholds that adapt to the dynamic channel conditions and trafﬁc patterns. Numerical experiments demonstrate that the proposed algorithm outperforms baselines without prior channel knowledge. Moreover, the DRL-based algorithm can maintain high spectral efﬁciency under fast-varying channels.  

# Keywords  

mmWave MIMO, 3GPP NR V2X, relay selection, deep reinforcement learning  

Dohyun Kim is with the Wireless Networking and Communications Group, the University of Texas at Austin, TX 78712- 1687, USA (e-mail: dohyun.kim@utexas.edu). Miguel R. Castellanos and Robert W. Heath Jr. are with the Department of Electrical  d Computer Engineering, North Carolina State University, 890 Oval Dr., Raleigh, NC 27606 USA (email:  { mrcastel, rwheathjr } @ncsu.edu). This work was partially supported by the U.S. Army Research Labs under grant W911NF-19-1-0221 and by the National Science Foundation under grant No. NSF-EECS-2153698.  

# I. I NTRODUCTION  

MmWave multiple-input multiple-output (MIMO) communication is a key technology for sensor data sharing to support automation in transportation systems [1]. Data sharing between self-driving vehicles can increase the safety of autonomous driving by enabling exchanges of trafﬁc conditions and collision warnings. Safety-critical automated driving applications may re- quire a maximum communication delay of tens-of-milliseconds to prevent catastrophic accidents [2]. Communication at gigabit-per-second data rates will be pivotal to transmit high-resolution data, either raw or processed, from sources such as cameras and radars [3], [4]. MmWave MIMO systems can meet the data rate requirements of vehicular networks with beamforming by taking advantage of wide bandwidth communication between 30 and 300 GHz.  

Unfortunately, high mobility and frequent blockages in mmWave vehicular networks create a lack of link resilience that may disrupt automotive applications [5]. High mobility systems are subject to fast fading channels, Doppler effects, and frequent handovers. Blockages due to mobile obstacles such as people and cars can induce shadowing losses up to 30-40 dB [6], while blockages due to static objects such as large buildings may result in penetration losses of 40-80 dB [7]. Issues stemming from mobility and blockage can deteriorate the system throughput, and these challenges must be addressed to enable the success of mmWave MIMO networks [8].  

Link vulnerability due to mobility can be partially overcome with careful beam management. Though Doppler frequencies are high at mmWave, directional beamforming reduces the effect of Doppler spread by restricting the range of Doppler frequency shifts according to the received beam directions [9]. While narrow beamwidths can mitigate Doppler spread, narrow codebooks increase the training overhead of exhaustive and hierarchical beam alignment methods. Although prior research has proposed fast beam adaptation in vehicular networks, which addresses the beam alignment overhead [10]–[12], most of this work has only considered cellular networks and one-hop transmission links between base stations and vehicles. Few studies have addressed beam alignment overhead in the context of vehicular networks with multi-hop links, despite the beneﬁts of connected vehicles on cooperative decision making such as lane changing and deceleration/acceleration [13].  

Multi-hop communication, enabled by relaying, can enhance link connectivity by providing multiple transmission paths that can be leveraged to avoid link blockages. In this context, recent studies have shown that a proper selection of unblocked relays can maintain stable data rates with low latency and drop rates [14]–[17]. Recent work on relay selection, however, either has approximated the beamforming gain using an ideal directional antenna pattern [14]–[16] or assumed the overhead from beam alignment is negligible [17]. Because of this, prior research on relay selection has not accounted for the overhead or the beamforming gain after beam alignment when switching relays.  

While a variety of solutions have addressed beam management and relay selection in mmWave MIMO vehicular networks separately [10], [15], [17], [18], the extension to the joint formulation of beam management and relay selection is nontrivial. Beam alignment is needed to establish a robust link when switching to a new relay. The training overhead required for beam alignment, however, may outweigh the beneﬁt of the new relay over the present link. In this context, we develop a DRL-based algorithm that chooses between when to select new relays and when to perform beam management.  

DRL is an online learning method that has been successfully applied to many communication applications, such as network access, caching, and connectivity preservation [19]. In mmWave vehicular networks, DRL has been used for resource allocation and radio access to enhance throughput while maintaining data security [20]. DRL resolves the exploration-exploitation trade- off, which appears in many control layer tasks such as dynamic beam selection [10], power allocation [15], and handover [21]. DRL enjoys small control overhead by adaptively balancing between testing new control actions versus choosing the actions deemed to have the maximum expected return according to prior actions deployed. The beneﬁts of DRL make it a suitable approach for solving the joint beam management and relay selection problem.  

In this paper, we propose a DRL algorithm for joint relay selection and beam management that uses beam measurements, which are the rate estimates fed back from the receiver to the transmitter, to decide when to switch relays and when to perform beam alignment. We presume the available relays, which can change over time due to the varying network topology, are identiﬁed and at most a two-hop link is allowed. We also assume the communication nodes employ Orthogonal Frequency Division Multiplexing (OFDM), an analog MIMO architecture, codebook-based beamforming, and that the beam measurements are fed back to the transmitter without quantization or overhead. The feedback may be available through a dedicated channel in the sub-6 GHz frequency range or may be sent on the reverse link with reduced coding and spreading. The choice of relay selection or beam management is made by comparing the rate feedback from beam measurements to two adaptive thresholds determined by the algorithm. We use one threshold to determine to either keep or switch the current link, where the links include the direct link and the indirect link through relays. We use the other threshold to decide between data transmission and beam management, which includes initial access, beam tracking, and data transmission [22]. The DRL-based policy uses the best known relay until the performance degrades under the learned threshold, in which case the policy tries out other relays according to beam management procedure. We summarize our contributions as follows:  

1) We formulate a joint relay selection and beam management problem for mmWave MIMO vehicular networks that accounts for the effect of the beam management overhead on the cumulative spectral efﬁciency. We devise a sequential decision-making model of the joint relay selection and beam management problem, reducing the state space by employing codebook-based beamforming. 2) We propose a DRL-based algorithm to solve the joint relay selection and beam management problem. The proposed algorithm uses the spectral efﬁciency feedback from the receiver to learn two thresholds, where one threshold corresponds to relay selection and the other to beam management. 3) We demonstrate the numerical performance between the proposed algorithm versus a base- line with prior knowledge on the channel. The heuristic selects ﬁxed thresholds based on an ofﬂine simulation instead of using the DRL algorithm. Note that the heuristic is analgous to the threshold-based relay selection previously studied for cellular device-to- device networks [23]. The proposed algorithm is able to outperform the heuristic approach even without the prior knowledge of the channel. Further, we analyze the impact of various system, channel, and beam management parameters on the performance. We ﬁnd that the proposed DRL-based policy is especially beneﬁcial over baselines under dense vehicular networks with highly-variant channels.  

Relevant studies on relay selection include [12], [14], [16], [24]–[26], which focus on the effective system throughput affected by time overhead. For example, the work in [12] addressed packet overhead and proposed to minimize the average delay of successfully delivered packets. The work in [14] characterized latency in mmWave vehicular networks as the sum of transmission delay and alignment delay. The work in [16] followed the latency characterization in [14] to maximize the effective rate assuming zero rate is achievable during beam alignment. The beam alignment delay throughout [12], [14], [16], though, is dependent only on the beamwidth. Our work uses the number of training beams and a practical 5G new radio (NR) beam alignment procedure [22] to calculate the overhead induced by both initial access and tracking. In [24],an overhead constraint is formulated as a bound on the total broadcasting and relaying time. The overhead has been measured in prior studies on buffer-aided relay selection using the queue length [25] and packet retransmissions [26]. The overhead in [24]–[26] does not incorporate the beamforming overhead. Our work penalizes latency due to excessive beam training by assuming exhaustive beam sweeping.  

DRL has previously been applied for relay selection in wireless communication networks [15], [17], [27]. In vehicular networks, DRL has also been applied for simultaneous power level allocation and relay selection. In the line of this work, deep Q-learning (DQL) was used in [15] for discrete power allocation to minimize the transmission latency. A deep deterministic policy gradient (DDPG) algorithm for continuous power level allocation to maximize the communication success rate was investigated in [17]. Our paper addresses beam management overhead, where transmit power is fully devoted to a selected relay according to the beam measurement feedback. In this context, [15] and [17] are complementary to our work. In [27], DRL is applied for relay selection in wireless sensor networks with static nodes using a utility function deﬁned by the system throughput and power usage. Our paper includes mobile nodes in a dynamic mmWave wideband channel and also accounts for the beam training overhead. Our paper also applies DRL with beam measurements as the states instead of the channel matrices, which can greatly improve the runtime because of the smaller state space that facilitates learning. Other online learning algorithms that have been applied to the relay selection problem include the multi- armed bandit framework [28], [29]. Notably, fast beam alignment algorithms based on bandits can exploit environmental awareness [10], sparsity of mmWave channels [18], and correlation structure among beams [11]. Our work assumes exhaustive beam sweeping as in [22], and we leave the extension to more sophisticated beam alignment algorithms for future work.  

The rest of the paper is structured as follows. In Section II, we present the system model used to represent the mmWave MIMO vehicular network. In Section III, we formulate the joint relay selection and beam management problem. In Section IV, we develop a DRL-based algorithm to solve the joint relay selection and mode selection problem. In Section V, we numerically evaluate the proposed algorithm compared to baselines with prior knowledge of the channel.  

Finally, we conclude the paper in Section VI.  

We use the following notation throughout this paper:  A  is a matrix,  a  is a vector,    $a$   is a scalar, and    $\mathcal{A}$   is a set. We denote    ${\bf a}^{\mathrm{T}}$    the transpose of  a ,    $\mathbf{a}^{*}$  the conjugate transpose, and    $\left\|\mathbf{a}\right\|$  the 2-norm. We denote    $\lceil a\rceil$  the ceiling function. We denote    $\nabla_{x}$   the gradient with respect to a variable    $x$  . A scalar random variable    $a\sim\mathcal D$   follows distribution    $\mathcal{D}$  . We denote the Gaussian distribution    ${\mathcal{N}}(a,b)$   and the complex Gaussian distribution    ${\mathcal{N}}_{C}(a,b)$   with mean    $a$   and variance  $b$  .  

# II. S YSTEM MODEL  

In this section, we describe the system model representing a mmWave vehicular network with V2V communication. We ﬁrst provide a generic view of the network and beam management procedure in Section II-A. We then describe the signal model in Section II-B. We outline the beam management procedure in Section II-C.  

# A. Network model  

Consider a mmWave vehicular network as shown in Fig. 1. We assume that the vehicles communicate based on OFDM. The transmitter generates data trafﬁc requested by the receiver, where other vehicles serve as potential relays. The transmitter selects one of two modes, beam alignment or data transmission, for each OFDM frame over the subcarriers and time. We assume the transmitter sends pilots during beam alignment and symbols during data transmission. Whenever the mode is beam alignment, the transmitter performs beam training to send pilots for  $M_{\mathrm{BA}}$   discrete time slots to establish the transmitter-to-receiver link. Otherwise, the transmitter sends data symbols to a single receiver via the transmitter-to-receiver link for    $M_{\mathrm{DT}}$   discrete time slots. This indicates that the sequence of modes can be consecutive beam alignments, consecutive data transmissions, or alternating with an arbitrary number of consecutive modes.  

Nearby vehicles can degrade the link quality by blocking the  direct  transmitter-to-receiver path, as shown in Fig. 1. We assume the transmitter has already discovered a ﬁxed number  $N_{\mathrm{REL}}$   of nearby relay nodes, given as the set of indices    $\{0,1,.\cdot\cdot,N_{\mathrm{REL}}\}$   where index  0  denotes the direct transmitter-to-receiver link. Given the indices, the transmitter can establish a two-hop indirect  transmitter-to-receiver V2V link via the transmitter-to-relay and relay-to-receiver V2V links to overcome the blockage of the direct path.  

  
Fig. 1. Snapshot illustration of an example system model consisting of four types of vehicles; i) the blue vehicle is the transmitter, ii) the yellow vehicle is an available relay, iii) the orange vehicle is the receiver, and iv) the purple vehicles are mobile blockages. Two-sided arrows indicate vehicular links; solid green links are unblocked and dashed red links are blocked.  

# B. Signal model  

We describe the signal model from the transmitter to the receiver under the data transmis- sion mode. The signal model also applies to other one-hop communication links, such as the transmitter-to-relay and relay-to-receiver link. The signal model under the beam alignment mode is similar to that under the data transmission mode, with the difference that a pilot signal is communicated instead of a data symbol [22].  

We assume an analog beamforming OFDM-MIMO architecture at both the transmitter and receiver. Hybrid and digital architectures allow sweeping over multiple beams simultaneously at the cost of higher energy consumption [22]. Under the analog architecture, the transmitter and receiver communicate via a single data stream. The transmitter consists of    $N_{\mathrm{TX}}$   antennas communicating with a receiver with    $N_{\mathrm{RX}}$   antennas. We denote    ${\bf f}_{\mathrm{RF}}[m]$   the    $N_{\mathrm{TX}}\times1$   complex RF beamformer vector and    ${\pmb w}_{\mathrm{RF}}[m]$   the    $N_{\mathrm{RX}}\times1$   complex RF combiner vector at time slot    $m$  . We assume frequency ﬂat RF precoder and combiners, such that  ${\bf f}_{\mathrm{RF}}[m]$   and    $\pmb{\upomega}_{\mathrm{RF}}[m]$   are constant over subcarriers, as in [30]. We assume that the power constraints    $\|\boldsymbol{\mathsf{f}}_{\mathrm{RF}}[m]\|^{2}=1$   and    $\|\pmb{\mathsf{w}}_{\mathrm{RF}}[m]\|^{2}=1.$  , for all    $m$  , on the beamforming vectors  ${\bf f}_{\mathrm{RF}}[m]$   and  $\pmb{\upomega}_{\mathrm{RF}}[m]$  . No other hardware-related constraints are assumed.  

We assume a time-varying frequency-selective channel between the transmitter and the re- ceiver. Let us denote    $K$   as the number of subcarriers and    $k=1,\ldots,K$   as the subcarrier index. We denote the    $N_{\mathrm{RX}}\times N_{\mathrm{TX}}$   channel matrix as    $\mathsf{H}[k,m]$   between the transmitter and the receiver for each    $k=1,\ldots,K$  . The channels used throughout the paper consist of the transmitter-to-receiver channel    $\mathsf{H}_{\mathrm{TX\toRX}}[k,m]$  , transmitter-to-relay channel    $\mathsf{H}_{\mathrm{TX\toREL}}[k,m]$  , and relay-to-receiver channel  $\mathsf{H}_{\mathrm{REL}\rightarrow\mathrm{REX}}[k,m]$  , where we omit the subscripts unless needed. We further assume the channel matrix    $\mathsf{H}[k,m]$   models the small-scale fading, while the averaged received power denoted by  $G[m]$   represents the large-scale fading [31]. Let us also denote the    $N_{\mathrm{RX}}\times1$   independently and identically distributed (IID)    $\mathcal{N}_{C}(0,\sigma_{\mathrm{n}}^{2})$   noise vector by    $\mathsf{n}$  . Then, at subcarrier    $k$   and time slot  $m$  , given the complex scalar    ${\sf s}[k,m]$   of transmitted symbols such that    $\mathbb{E}[|{\sf s}[k,m]|^{2}]\;=\;1$  , the processed received signal at subcarrier    $k$   and time slot    $m$   is [32]  

$$
\begin{array}{r}{{\boldsymbol{\mathsf{y}}}[k,m]=\sqrt{G[m]}{\boldsymbol{\mathsf{w}}}_{\mathrm{RF}}^{*}[m]\mathsf{H}[k,m]\mathsf{f}_{\mathrm{RF}}[m]\mathsf{s}[k,m]+{\boldsymbol{\mathsf{w}}}_{\mathrm{RF}}^{*}[m]\mathsf{n}[k,m].}\end{array}
$$  

Note that these normalizations imply that the signal-to-noise-ratio (SNR) prior to beamforming is  $G[m]/\sigma_{\mathrm{n}}^{2}$  . As the performance metric, we use the instantaneous spectral efﬁciency [31] averaged over the subcarriers  

$$
S(\boldsymbol{\mathsf{f}}_{\mathrm{RF}}[m],\boldsymbol{\mathsf{w}}_{\mathrm{RF}}[m],\boldsymbol{\mathsf{H}}[k,m])=\frac{1}{K}\sum_{k=1}^{K}\log_{2}\left(1+\frac{G[m]}{\sigma_{\mathrm{n}}^{2}}|\boldsymbol{\mathsf{w}}_{\mathrm{RF}}^{*}[m]\boldsymbol{\mathsf{H}}[k,m]\boldsymbol{\mathsf{f}}_{\mathrm{RF}}[m]|^{2}\right).
$$  

The receiver can measure the instantaneous spectral efﬁciency and feed back the beam measure- ment to the transmitter, as discussed in Section II-C.  

# C. Beam management procedure  

In this section, we outline the codebook-based beam management procedure. We follow a general approach as in commercial mmWave systems like IEEE 802.11ad and 5G. We assume the transmitter and receiver use beams from beam codebooks. We further assume the system employs a feedback mechanism to estimate the spectral efﬁciency. For simplicity, we assume the feedback is perfect with no quantization and no additional overhead is induced from the feedback procedure. When the receiver successfully decodes one or more successful transmissions, it feeds back the beam measurement to the transmitter. Otherwise, it feeds back a beam measurement of zero to the transmitter. Note that this is is analogous to the automatic repeat-request (ARQ) used in 802.11 standards.  

We describe the overall duration of the beam alignment procedure, which is a dominant factor in the beam management overhead. The beam alignment is performed by iterating over predeﬁned beams to aggregate the beam measurements and select the best beam. Each iteration is controlled by synchronization signal (SS) bursts, where a single SS burst consists of multiple SS blocks [22]. Denoting    $N_{S S}$   as the number of SS blocks per burst, the system can examine    $N_{S S}$  pairs of beams when exchanging a single SS burst. Whenever a single SS burst is exchanged, the next SS burst is exchanged after time    $M_{S S}$   slots, which we denote as the periodicity of SS bursts. When beam alignment starts at time    $m$  , the ﬁrst beam pair in the SS burst is exchanged at time    $m+\lceil M_{\mathrm{SS}}/N_{\mathrm{SS}}\rceil$  , the second beam pair at time    $m+2\lceil M_{\mathrm{SS}}/N_{\mathrm{SS}}\rceil$  , continuing up to the last beam pair at time    $m+N_{\mathrm{SS}}\lceil M_{\mathrm{SS}}/N_{\mathrm{SS}}\rceil$  . The duration of the beam alignment period depends on the number of beam pairs that should be examined, which can be categorized into four cases depending on the mode and the number of hops. The mode can be either initial access or beam tracking. The direct link has one hop, and the indirect link has two hops. Let us denote the transmitter codebook with size    $N_{\mathsf{c}}$   as    $\mathcal{F}=\{\mathbf{f}_{1},\mathbf{f}_{2},.\ .\ .\ ,\mathbf{f}_{N_{\mathrm{c}}}\}$  , and similarly the receiver codebook as    $\mathcal{W}$   and    $n$  th relay codebook as    ${\mathcal{G}}_{n}$  . For initial access via direct link, the duration of beam alignment can be expressed as  

$$
M_{\mathrm{IA,direct}}=M_{\mathrm{SS}}\left[\frac{|\mathcal{F}|\cdot|\mathcal{W}|}{N_{\mathrm{SS}}}\right],
$$  

due to the exhaustive beam sweeping over    $\mathcal{F}\times\mathcal{W}$  . Let us denote    $N_{\mathrm{{BT}}}$   as the number of best beams fed back to the transmitter from the receiver during beam tracking. Unlike in initial access where    $|\mathcal F|\cdot|\mathcal W|$   beams are swept, only    $N_{\mathrm{{BT}}}<<|{\mathcal F}|\cdot|{\mathcal W}|$   beams are processed in beam tracking. The duration of the beam alignment period for beam tracking via direct link is  

$$
M_{\mathrm{{BT,direct}}}=M_{\mathrm{{SS}}}\left\lceil\frac{N_{\mathrm{{BT}}}}{N_{\mathrm{{SS}}}}\right\rceil.
$$  

For simplicity, let us assume perfect time synchronization between the transmitter and the relay. Then, the duration of the beam alignment procedure is  

$$
M_{\mathrm{IA,indirect}}=M_{\mathrm{SS}}\left[\frac{|\mathcal{F}|\cdot|\mathcal{G}_{n}|}{N_{\mathrm{SS}}}\right]+M_{\mathrm{SS}}\left[\frac{|\mathcal{G}_{n}|\cdot|\mathcal{W}|}{N_{\mathrm{SS}}}\right],
$$  

for initial access via indirect link and  

$$
M_{\mathrm{{BT,direct}}}=2M_{\mathrm{{SS}}}\left\lceil\frac{N_{\mathrm{{BT}}}}{N_{\mathrm{{SS}}}}\right\rceil,
$$  

for beam tracking. The indirect link has a longer beam alignment period than the direct link both for initial access and beam tracking. Nonetheless, the effective spectral efﬁciency accounting the beamforming overhead may be high in the indirect link due to blockage of the direct link.  

During beam alignment, the transmitter and the receiver search for the best transmit and receive beam pair that maximizes SNR [22]. Due to the exhaustive beam sweeping procedure, beam indices are swept sequentially over time. Let us denote the time slot when codebook indices  $(i_{\mathcal{F}},i_{\mathcal{W}})$   are being swept as  

$$
m_{\mathrm{d}}(i_{\mathcal{F}},i_{\mathcal{W}})=\left\lceil\frac{N_{\mathrm{c}}(i_{\mathcal{F}}-1)+i_{\mathcal{W}}}{N_{\mathrm{SS}}}\right\rceil,
$$  

where the subscript d shows the delay due to the exhaustive beam sweeping is accounted. When beam alignment ends at time slot    $m$  , the system obtains the beamforming vectors  

$$
\mathbf{f}_{\mathrm{d},i_{\mathcal{F}}}[m],\mathbf{w}_{\mathrm{d},i_{\mathcal{W}}}[m])=\operatorname*{argmax}_{i_{\mathcal{F}}\in\mathcal{F},i_{\mathcal{W}}\in\mathcal{W}}S(\mathbf{f}_{i_{\mathcal{F}}}[m],\mathbf{w}_{i_{\mathcal{W}}}[m],\mathsf{H}_{\mathrm{TX}\to\mathbb{R}\mathrm{X}}[m-M_{\mathrm{BA}}+m_{\mathrm{d}}(i_{\mathcal{F}},i_{\mathcal{W}}[m],\mathbf{w}_{i_{\mathcal{W}}}[m])]).
$$  

and the achievable spectral efﬁciency is given by  

$$
S_{\mathrm{TX\rightarrowRX,0,p}}[m]=\frac{1}{K}\sum_{k=1}^{K}\log_{2}\left(1+\frac{G[m]}{\sigma_{\mathrm{n}}^{2}}\bigg|\mathbf{w}_{\mathrm{d},i\nu}^{*}[m]\mathsf{H}_{\mathrm{TX\rightarrowRX}}[k,m]\mathsf{f}_{\mathrm{d},i\mathcal{F}}[m]\bigg|^{2}\right),
$$  

where the subscript  0  indicates using the direct link. The subscript   $\mathfrak{p}$   indicates no measurement error is included in (9).  

To incorporate measurement error, we express the beam measurement assuming the system uses MMSE estimator for the effective channel under a rectangular Doppler spectrum as in [31, Sec. 4.8]. As the MMSE estimator can be obtained in terms of the ratio of pilots per symbol transmission, we count the number of pilots over time and frequency frames between data transmission modes. For every block between data transmission modes, in this context, we denote the varying ratio of pilots as    $\beta$   and the total number of OFDM frames as    $N_{\mathfrak{b}}$  . Then, the MMSE can be written as  

$$
\mathrm{MMSE}=\frac{1}{1+\beta N_{\mathrm{b}}\mathrm{SNR}},
$$  

and the effective SNR as  

$$
\mathrm{SNR}_{\mathrm{eff}}=\frac{\mathrm{SNR}(1-\mathrm{MMSE})}{1+\mathrm{SNR}\cdot\mathrm{MMSE}}.
$$  

The estimated spectral efﬁciency, fed back from the receiver to the transmitter as a beam measurement, is  

$$
S_{\mathrm{TX\rightarrowRX,0}}[m]=\frac{1}{K}\sum_{k=1}^{K}\log_{2}\left(1+\mathrm{SNR}_{\mathrm{eff}}\bigg|\mathsf{w}_{\mathsf{d},i\nu}^{*}[m]\mathsf{H}_{\mathrm{TX\rightarrowRX}}[k,m]\mathsf{f}_{\mathsf{d},i\mathcal{F}}[m]\bigg|^{2}\right),
$$  

when the symbol is being sent at time slot    $m$   and zero during beam management. We similarly deﬁne the estimated spectral efﬁciency    $S_{\mathrm{TX\rightarrowREL},n}$   and    $S_{\mathrm{REL}\rightarrow\mathrm{REX},n}$   through transmitter-to-relay and relay-to-receiver link. For    $S_{\mathrm{TX\rightarrowREL},n}$  , the codebook pair    $(\mathcal{F},\mathcal{W})$   is replaced by    $({\mathcal{F}},{\mathcal{G}}_{n})$  and the channel    $\mathsf{H}_{\mathrm{TX\toRX}}[m]$   with    $\mathsf{H}_{\mathrm{TX\toREL},n}[m]$  . For    $S_{\mathrm{REL}\rightarrow\mathrm{REX},n}$  , the codebook pair    $(\mathcal{F},\mathcal{W})$   is replaced by    $(\mathcal{G}_{n},\mathcal{W})$   and the channel    $\mathsf{H}_{\mathrm{TX\toRX}}[m]$   with    $\mathsf{H}_{\mathrm{REL}\to\mathrm{REX},n}[m]$  . We replace the subscript 0  with    $n$   for the transmitter-to-relay and the relay-to-receiver link to indicate using the    $n$  th link. The overall spectral efﬁciency of the two-hop indirect path is  

$$
S_{\mathrm{TX}\rightarrow\mathrm{RX},n}[m]=\frac{S_{\mathrm{TX}\rightarrow\mathrm{REL},n}[m]S_{\mathrm{REL}\rightarrow\mathrm{RX},n}[m]}{S_{\mathrm{TX}\rightarrow\mathrm{REL},n}[m]+S_{\mathrm{REL}\rightarrow\mathrm{RX},n}[m]},
$$  

following the optimal time resource allocation for decode-and-forward relaying as in [33]. The beam measurement of the transmitter-to-relay and relay-to-receiver link may be individually available to the transmitter via the relay-to-transmitter and the receiver-to-transmitter feedback channel.  

# III. F ORMULATING THE JOINT RELAY SELECTION AND BEAM MANAGEMENT PROBLEM  

In this section, we formulate the joint relay selection and beam management problem for the mmWave MIMO vehicular network from the perspective of sequential decision theory. Based on this formulation, we discuss how to choose actions for each time steps. To do this, we devise a Markov Decision Process (MDP), which is a well-studied model for sequential decision making.  

The transmitter aims to maximize the data rate by selecting the best relay and beam at each time slot. We say that the transmitter needs to decide  actions    $\mathcal{A}[m]$   for each time slot. The actions consist of a chosen relay index    $n[m]\in\{0,1,.\,.\,,N_{\mathrm{REL}}\}$   and a beam management mode  $n_{\mathrm{mode}}[m]\in\{0,1\}$   which dictates whether to perform beam alignment or data transmission. We set    $n_{\mathrm{mode}}=1$   to indicate data transmission and    $n_{\mathrm{mode}}=0$   to indicate beam alignment.  

The optimal set of actions are selected to maximize the running average of the spectral efﬁciency over    $M$   time slots. We assume a ﬁnite    $M$   to ensure the sum of spectral efﬁciency is bounded, as in other sequntial decision formulations in wireless applications [19]. On top of the spectral efﬁciency depending on the channel and beamforming vectors, as given in (12), the action affects the spectral efﬁciency due to the beam management procedure. In this context, we use a binary variable    $c(\mathcal{A}[m])$   to express the effect of the actions on the spectral efﬁciency. We set    $c(\mathcal{A}[m])=1$   when the action is data transmission and    $c(\mathcal{A}[m])=0$   when the action is beam alignment. Then, the optimization problem for maximizing the cumulative spectral efﬁciency can be written as  

$$
\operatorname*{max}_{\{a[m]\}}\sum_{m=1}^{M}\sum_{n=0}^{N_{\mathrm{REL}}}\bigg(c(\mathcal{A}[m])S_{\mathrm{TX}\rightarrow\mathrm{RX},n}[m]\bigg).
$$  

We ﬁrst analyze a genie-aided policy to approach (14). At time slot  $m$  , suppose the achievable spectral efﬁciency    $S_{\mathrm{TX}\rightarrow\mathrm{RX},n}[m]$   is known for all    $n$  . In this case, the optimal solution    $a_{\mathrm{OPT}}[m]$  of (14) is selecting the relay index    $n[m]=\operatorname{argmax}_{n}S_{\mathrm{TX}\rightarrow\mathbb{R}\mathrm{X},n}[m]$   with the mode    $n_{\mathrm{mode}}[m]=1$  . Note that the value obtained by    $a_{\mathrm{OPT}}$   is the expected upper bound of the system’s performance.  

The system is limited from achieving the performance of the genie-aided policy due to the tradeoff between the performance obtained from frequent beam alignment versus frequent data transmission. On one hand, frequent beam alignment is necessary due to the fast varying channel. On the other hand, frequent data transmission is required to realize the spectral efﬁciency. The tradeoff can be also explained in terms of the objective in (14). Frequent beam alignment can improve the accuracy of rate feedback leading to a higher    $S_{\mathrm{TX}\rightarrow\mathrm{RX},n}[m]$   at the expense of the coefﬁcient set to    $c(\mathcal{A}[m])=0$  . Conversely, frequent data transmission can achieve the coefﬁcient  $c(\mathcal{A}[m])=1$   at the cost of a lower    $S_{\mathrm{TX}\rightarrow\mathrm{RX},n}[m]$   due to beam misalignment.  

The system can address the performance tradeoff between beam alignment versus data trans- mission using sequential decision theory. Following the approach taken in sequential decision making formulations in wireless communication applications [19], we assume an MDP as the learning model for (14). The three components that must be speciﬁed in an MDP are the states, actions, and the reward:  

States:  The system state of interest is determined by the channel realizations. In codebook- • based directional beamforming, the beam indices (8) and measurements (12) can substitute the channel information [34]. Accordingly, we deﬁne the link vector of the communication  

link via the    $n$  th relay as  

$$
\begin{array}{r}{{\bf b}_{n}[m]=\left[i_{\mathcal{F},\mathrm{OPT}}[m],i_{\mathcal{G}_{n},\mathrm{OPT}}[m],S_{\mathrm{TX}\rightarrow\mathrm{REL},n}[m]\right].}\end{array}
$$  

The state can then be represented as  

$$
\mathcal{T}[m]=\{\mathbf{b}_{0}[m],\ldots,\mathbf{b}_{N_{\mathrm{REL}}}[m]\},
$$  

which consists of the link vectors for all relay indices.  

Actions : The action of the transmitter is the decision variable in the optimization problem • (14). Though discrete actions can be used, continuous actions are often preferred in wireless applications due to scalability [19]. We follow this approach and defer the readers to Section IV-A for the speciﬁcation of the continuous action.  

Reward:  The reward is designed to maximize the objective in (14), which can be represented • as  

$$
r(\mathcal{T}[m],\mathcal{A}[m])=\sum_{n=0}^{N_{\mathrm{REL}}}\bigg(c(\mathcal{A}[m])S_{\mathrm{TX}\rightarrow\mathrm{RX},n}[m]\bigg).
$$  

Note that we follow the typical approach of choosing the reward as the objective at time index    $m$   [19].  

IV. P OLICY DESIGN FOR JOINT RELAY SELECTION AND BEAM MANAGEMENT  

In this section, we develop algorithms to solve the joint relay selection and beam management in mmWave MIMO vehicular networks. We develop a DRL-based algorithm based on a pure threshold policy [23], [35]. In Section IV-A, we ﬁrst describe a threshold-based heuristic (Algo- rithm 1) with ﬁxed    $\tau_{\mathrm{relay}}$   and    $\tau_{\mathrm{mode}}$   that determine the relay index and mode. We then specify the proposed DRL-based policy, as in Algorithm 2, which applies DRL based on a policy gradient approach to learn the thresholds and solve the joint relay selection and beam management in Section IV-B.  

# A. Threshold-based heuristic  

Threshold-based policies with one threshold have been studied for relay selection [23], [35]. One threshold is sufﬁcient for relay selection, as it can represent one of two behaviors: to either keep the relay or switch. For example, the receiver may switch relays if the estimated received SNR of the current link is below that of the best relay and hold otherwise [35]. With more behaviors to model, however, additional thresholds may be required. For example, threshold- based policies for data transmission through a Gilbert-Eilliot channel often required two separate thresholds to determine to whether send data, wait, or measure the channel [36].  

We follow the threshold-based policies as in [36] to use thresholds as actions. Two continuous thresholds  $\tau_{\mathrm{relay}}$   and    $\tau_{\mathrm{mode}}$   are deﬁned such that the action can be represented as  

$$
\mathcal{A}[m]=\left\{\tau_{\mathrm{relay}},\tau_{\mathrm{mode}}\right\}.
$$  

The transmitter compares the rate feedback in (12) to the thresholds and then chooses one of the following three behaviors: optimistic, opportunistic, and pessimistic action. When the transmitter is optimistic, believing that the channel is in an unblocked state with high achievable spectral efﬁciency, it keeps both the relay index and mode. When the transmitter is opportunistic, believing that the channel is in an unblocked state but with a low achievable spectral efﬁciency, it keeps the relay index but sets the mode to beam tracking. When the transmitter is pessimistic, believing the channel is in a blocked state, it changes the relay index and also sets the mode to beam alignment. We assume    $\tau_{\mathrm{relay}}<\tau_{\mathrm{mode}}$   due to the rate of blocked channels being worse than that of the unblocked and bad channels. The belief of the transmitter regarding the channel is determined by the beam measurements in (12). For a given beam measurement    $S$   of the current link, the transmitter takes the optimistic action if    $S>\tau_{\mathrm{mode}}$  , the opportunistic action if  $\tau_{\mathrm{mode}}>S>\tau_{\mathrm{relay}}$  , or the pessimistic action if    $\tau_{\mathrm{relax}}>S$  .  

The pseudocode of the proposed threshold-based heuristic is given in Algorithm 1. The algorithm requires the thresholds    $\tau_{\mathrm{relay}}$   and    $\tau_{\mathrm{mode}}$   as ﬁxed inputs. The algorithm is similar to a state transition matrix. It takes    $n[m]$  , mode    $n_{\mathrm{mode}}[m]$  , and link vectors    $\mathbf{b}_{0}[m],.\,.\,,\mathbf{b}_{N_{\mathrm{REL}}}[m]$   at the  m th time slot to obtain    $\mathcal{T}[m+1]$  . Due to the duration of beam management, the algorithm may need to continue the mode    $n_{\mathrm{mode}}[m]$   over multiple time slots. To do this, the algorithm tracks how long the current beam management mode has lasted using    $m_{\mathrm{BA}}[m]$   and    $m_{\mathrm{DT}}[m]$  . The variable    $m_{\mathrm{BA}}[m]$   can be thought as the number of beam indices swept in the current beam alignment mode (7). The variable    $m_{\mathrm{DT}}[m]$   relates to the number of time slots spent in the current data transmission. At the end of each beam management mode, when    $m_{\mathrm{BA}}\,=\,M_{\mathrm{BA}}$   or  $m_{\mathrm{DT}}=M_{\mathrm{DT}}$  , the algorithm updates the relay index and beam management mode depending on the transmitter’s belief of the channel.  

Algorithm 1  Threshold-based heuristic for joint relay selection and beam management problem 1:  Input: threshold    $\tau_{\mathrm{mode}}$   on mode selection, threshold    $\tau_{\mathrm{relax}}$   on relay selection, current time slot index    $k$  , current relay index    $n[m]$  , current mode    $\dot{n}_{\mathrm{mode}}[m]$  , and current link vectors  $\mathbf{b}_{0}[m],.\,.\,,\mathbf{b}_{N_{\mathrm{REL}}}[m]$  2:  if    $n_{\mathrm{mode}}[m]=0$   then  $\%$   Beam alignment 3:  $S[m]=0$  4: if    $m_{\mathrm{BA}}[m]<M_{\mathrm{BA}}[m]$   then 5:  $n_{\mathrm{mode}}[m+1]=0$  6: Update    $m_{\mathrm{BA}}[m+1]=m_{\mathrm{BA}}[m]+1$  7: else 8: Update beam indices    $\ensuremath{\mathbf{b}}_{n[m]}[m+1]$   according to (8) 9:  $n_{\mathrm{mode}}[m]=1$  10:  $m_{\mathrm{BA}}[m+1]=1$  11: end if 12:  else  $\%$   Data transmission 13: Set measured spectral efﬁciency    $S[m]$   according to    ${\bf b}_{n[m]}[m]$  14: if    $m_{\mathrm{DT}}[m]<M_{\mathrm{DT}}$   then 15:  $n_{\mathrm{mode}}[m+1]=1$  16: Update    $m_{\mathrm{DT}}[m+1]=m_{\mathrm{DT}}[m]+1$  17: else 18: if    $S[m]<\tau_{\mathrm{relay}}$   then 19:  $\begin{array}{r}{\boldsymbol{n}[m+1]=\operatorname*{argmax}_{\boldsymbol{n}\in\{0,1,\dots,n[m]-1,n[m]+1,\dots,N_{\mathrm{REL}}\}}S_{\mathrm{TX\rightarrowRX},n}[m]}\end{array}$  20:  $n_{\mathrm{mode}}[m]=0$  21: else if    $S[m]<\tau_{\mathrm{mode}}$   then 22:  $n_{\mathrm{mode}}[m]=0$  23: end if 24:  $m_{\mathrm{DT}}[m+1]=1$  25: end if 26:  end if  

and measured spectral efﬁciency    $S[m]$  

To deploy the threshold-based heuristic, the thresholds  $\tau_{\mathrm{relay}}$   and    $\tau_{\mathrm{mode}}$   are required as inputs. In practice, test results over varying    $\tau_{\mathrm{relay}}$   and    $\tau_{\mathrm{mode}}$   may be compared to choose the thresholds that provide the highest spectral efﬁciency. Considering dense vehicular networks with complex and dynamic trafﬁc patterns, the thresholds need to be computed efﬁciently both in terms of data and time resources [10]. For this reason, we apply DRL to ﬁnd the thresholds with short training time and without ofﬂine data.  

# B. Learning algorithm  

DRL algorithms aim to ﬁnd the sequence of actions that maximize the cumulative reward by training neural networks through trial-and-error. At each iteration an action is determined according to the output of the neural networks. The action is deployed on the environment resulting in a reward. The reward is then used to update the weights of neural networks, which will determine the next action.  

The following fundamental aspects are involved in the design of the DRL algorithms: the policy    $\mu$   and the Q-function    $Q$  . The policy is a mapping from the state space to the action space, such that    ${\mathcal{A}}=\mu({\mathcal{T}})$  . The aim of DRL is typically formulated as ﬁnding the best policy. The Q-function    $Q(\mathcal{T},\mathcal{A})$   is a measure of the expected reward from a state-action pair followed by the state-action pairs induced by the optimal policy. The Q-function    $Q(\mathcal{T},\mathcal{A})$   is often useful for policy search problems due to two properties: it provides a straightforward way to ﬁnd the optimal policy    $\mu^{\mathrm{OPT}}(s)=\operatorname{argmax}_{a}Q(\mathcal{T},\mathcal{A})$  , and it can be computed with Bellman updates [37].  

We use DDPG [38], which is a DRL algorithm that trains both the policy and  $\mathsf Q$   with neural networks, to solve the joint relay selection and beam management problem. It trains an actor  $\theta_{\mathrm{A,ON}}$   that takes states as inputs and actions as outputs. The actor network accordingly yields the policy    $\mu_{\theta_{\mathrm{A,ON}}}$  . DDPG also trains a critic    $\theta_{\mathrm{C,ON}}$   that takes state-action pairs as inputs and  $\mathrm{\DeltaQ}$  values as outputs. The critic network represents the Q-function    $Q(\cdot|\theta_{\mathrm{C,ON}})$  . For stable learning, DDPG reserves the delayed copy of    $\theta_{\mathrm{A,ON}}$   and    $\theta_{\mathrm{C,ON}}$   as the target networks    $\theta_{\mathrm{A,TAR}}$   and    $\theta_{\mathrm{C,TAR}}$  .  

DDPG is a suitable algorithm for the joint relay selection and beam management, as in other wireless applications, due to its fast convergence and capability of handling continuous action spaces [19]. We introduce the updating rule for the neural networks in DDPG. Let us denote the replay buffer as    $\mathcal{D}$  . Each element in the replay buffer is a tuple consisting of state, action, reward, and successor state. The tuple    $(\mathcal{T}[m],\mathcal{A}[m],r[m],\mathcal{T}[m\!+\!1])$   is denoted as a trajectory, referring to the deployment history. A    $B$  -element minibatch, which consist of trajectories randomly sampled with replacement from    $\mathcal{D}$  , is used for updating the online actor and critic networks. Speciﬁcally,  $\theta_{\mathrm{C,ON}}$   is updated by minimizing the loss  

$$
\begin{array}{l}{\displaystyle{\cal L}=\frac{1}{B}\sum_{m^{\prime}}\bigg((r[m^{\prime}]+\gamma Q(\mathcal{T}[m^{\prime}+1],\mu_{\theta_{\tt A,T A R}}(\mathcal{T}[m^{\prime}+1])|\pmb{\theta}_{\mathrm{C,TAR}})}\\ {\displaystyle-Q(\mathcal{T}[m^{\prime}],\mathcal{A}[m^{\prime}]|\pmb{\theta}_{\mathrm{C,ON}}))^{2}\bigg).}\end{array}
$$  

Meanwhile, the sampled policy gradient, which updates    $\theta_{\mathrm{A,ON}}$  , is given as  

$$
\sum_{m^{\prime}}\frac{1}{B}\biggl(\nabla_{A}Q(\mathcal{T},\mathcal{A}|\theta_{\mathrm{C,ON}})|_{\mathcal{T}=\mathcal{T}_{[m^{\prime}]},\mathcal{A}=\mu_{\theta_{\mathrm{A,ON}}}(\mathcal{T}^{[m^{\prime}]})}\times\nabla_{\theta_{\mathrm{A,ON}}}\mu_{\theta_{\mathrm{A,ON}}}(\mathcal{T})|_{\mathcal{T}=\mathcal{T}_{[m^{\prime}]}}\biggr).
$$  

The target networks are slowly updated from the online networks, where the parameter    $\eta<<1$  controls the variance of the target networks:  

$$
\begin{array}{r}{\pmb{\theta}_{\mathrm{A,TAR}}\leftarrow\eta\pmb{\theta}_{\mathrm{A,ON}}+(1-\eta)\pmb{\theta}_{\mathrm{A,TAR}},}\\ {\quad}\\ {\pmb{\theta}_{\mathrm{C,TAR}}\leftarrow\eta\pmb{\theta}_{\mathrm{C,ON}}+(1-\eta)\pmb{\theta}_{\mathrm{C,TAR}}.}\end{array}
$$  

The parameter    $\eta$   can be used to suppress the overestimation of the Q-values [39].  

Implementing DDPG for joint relay selection and beam management, the following steps are repeated for the time slots    $m=1,.\hdots,M$  :  

1) Select the thresholds    $\tau_{\mathrm{relay}}[m]$   and    $\tau_{\mathrm{mode}}[m]$   according to the online actor network    $\theta_{\mathrm{A,TAR}}$  and exploration noise distribution    $\mathcal{N}$  , where the default exploration noise is the Ornstein- Uhlenbeck noise. 2) Deploy Algorithm 1 with the inputs    $\tau_{\mathrm{relay}}[m],\;\tau_{\mathrm{mode}}[m],\;{\bf b}_{0}[m],.\;.\;.\;,{\bf b}_{N_{\mathrm{EL}}}[m],\;I[m],\;n[m],$  and    $n_{\mathrm{mode}}[m]$  . As a result, obtain the successive    ${\bf b}_{0}[m+1],.\,.\,.\,,{\bf b}_{N_{\mathrm{EL}}}[m+1],\,n[m+1]$  ,  $n_{\mathrm{mode}}[m+1]$  , and    $S[m]$  . 3) Append the current state action pair to the successor state and reward pair to accumulate transition    $(\mathcal{T}[m],\mathcal{A}[m],r[m],\mathcal{T}[m+1])$   in replay buffer    $\mathcal{D}$  . 4) Update the online actor and critic networks    $\theta_{\mathrm{A,ON}}$   and    $\theta_{\mathrm{C,ON}}$   according to (19) and (20). 5) Update the target actor and critic networks    $\pmb{\theta}_{\mathrm{A,TAR}}$   and    $\theta_{\mathrm{C,TAR}}$   with respect to (21).  

We give the pseudocode in Algorithm 2 and the ﬂowchart in Fig. 2 for completeness. Note that, as shown in Fig. 2, we are using Algorithm 1 as the environment with respect to the DDPG agent.  

# V. E XPERIMENTAL RESULTS  

In this section, we present the numerical evaluation of the proposed DRL-based algorithm for joint relay selection and beam management problem in a mmWave MIMO vehicular network. We describe the simulation setup and the relevant parameters in Section V-A. We use two scenarios, one to focus on the line-of-sight (LOS) channel and the other to capture non-LOS (NLOS) paths in vehicular networks. We detail the baseline policies and the performance metric  

# Algorithm 2  DRL-based joint relay selection and beam management strategy  

1:   put: Length    $M$  f decision horizon, set    $\overline{{\{0,1,.\ldots,N_{\mathrm{REL}}\}}}$   o ays, minibatch sample size  $B$  , replay buffer  D , exploration noise distribution  N , length  $M_{\mathrm{BA}}$   of beam alignment period 2:  Randomly initialize online critic network    $Q(s,a|\theta_{\mathrm{C,ON}})$   and online actor network    $\mu(s|\theta_{\mathrm{A,ON}})$  with    $\theta_{\mathrm{C,ON}}$   and    $\theta_{\mathrm{A,ON}}$  3:  Init tic network    $\theta_{\mathrm{C,uparrow}}\leftarrow\theta_{\mathrm{C,ON}}$   and target actor network    $\theta_{\mathrm{A,TAR}}\leftarrow\theta_{\mathrm{A,ON}}$  4:  for  $m=1,.\;.\;.\;,M$   do 5: Select action    $a[m]=\{\tau_{\mathrm{relay}}[m],\tau_{\mathrm{mode}}[m]\}$   according to the current online actor network and exploration noise distribution  N 6: Deploy Algorithm 1 with inputs    $\tau_{\mathrm{relay}}[m]$  ,    $\tau_{\mathrm{mode}}[m]$  ,  n [ m ] ,    $n_{\mathrm{mode}}[m]$  , link vectors  ${\bf b}_{0}[m],.\,.\,.\,,{\bf b}_{M}[m]$  , and    $M_{\mathrm{BA}}[m]$  . 7: Compute reward    $r[m]=S$   from Algorithm 1 8: Update    $n[m+1]$   and    $n_{\mathrm{mode}}[m+1]$   from output of Algorithm 1 9: Get successor state    $s[m+1]$   from updated link vectors 10: Store transition    $(s[m],a[m],r[m],s[m+1])$   in    $\mathcal{D}$  11: Sample a random minibatch of  B  transitions from    $\mathcal{D}$  12: Update the online critic network by minimizing the loss (19) 13: Update the online actor network by policy gradient (20) 14: Update the target networks from the online networks according to (21) 15:  end for  

  

Fig. 2. Flowchart of the proposed DRL-based joint relay selection and beam management algorithm. The threshold-based heuristic (Algorithm 1) serves as the environment in each iteration.  

in Section V-B. We provide the numerical results on the LOS scenario in Section V-C. We then give the numerical results on the more realistic scenario with NLOS paths in Section V-D.  

A. Simulation setup  

We simulate a mmWave MIMO vehicular network using two scenarios. The ﬁrst scenario only considers a LOS channel with two relay nodes available to the transmitter. In the second scenario, the channels are calculated using vehicle trajectory data based on Simulator of Urban Mobility (SUMO) [40]. The ﬁrst scenario represents a simpliﬁed version of a conceptual deployment for mobile mmWave networks. It is used to analyze the effect of system parameters, such as angular spread    $\sigma_{\mathrm{a}}$  , on the spectral efﬁciency. The second scenario represents a more realistic deployment of mmWave vehicular networks and is used to analyze speciﬁc system parameters of the vehicular network, such as vehicle density per lane, on the spectral efﬁciency. We assume stationarity in the joint process of channel and blockage in both scenarios, which is commonly used in vehicular channel modeling [2].  

The simulation parameters for both scenarios, unless stated otherwise, are summarized as follows:  

Antenna array and codebook:  We assume uniform linear arrays with half-wavelength spac- • ing equipped at both transmitter and receivers. For simplicity of exposition, we focus on a case with uniform linear arrays (ULAs) at the transmitter and receiver, but it can be readily extended to other array geometry and multiple panels. Denoting    $\phi$   the steering angle and    $\lambda$  the carrier wavelength, the array response vector for a    $N$  -element ULA is given as  

$$
\mathbf{a}(\phi)=\frac{1}{\sqrt{N}}\left[1,e^{-\mathrm{j}\pi\cos(\phi)},.\.\,,e^{-\mathrm{j}(N-1)\pi\cos(\phi)}\right]^{\mathrm{T}}.
$$  

We select a codebook structure that equally partitions the angular domain    $[0,\pi]$  . The codebook vectors are given as    $\mathbf{f}_{i_{\mathcal{F}}}=\mathbf{a}(\pi i_{\mathcal{F}}/N_{\mathrm{TX}})$  ,  for    $i_{\mathcal{F}}=0,1,\dotsc,N_{\mathrm{TX}}-1$   and similarly  

for the receiver codebook  $\mathcal{W}$   and the    $m$  th relay codebook    $\mathcal{G}_{m}$   over    $m\in\{0,1,.\,.\,.\,,N_{\mathrm{{REL}}}\}$  .  Channel model:  We use a time-varying geometric channel composed of    $L[m]$   paths as in • [41]. For the  ℓ th path, we denote    $\alpha_{\ell}[m]$   as the complex path gain,    $\phi_{\ell,\mathrm{A}}[m]$   as the AOA,  $\phi_{\ell,\mathrm{D}}[m]$   as the AOD,    $\mathbf{a}_{\mathrm{t}}(\cdot)$   as the transmit array vector, and    $\mathbf{a}_{\mathrm{r}}(\cdot)$   as the receive array vector. To further express the wideband channel, we apply the delay-  $d$   channel model denoting the path delay as    $\tau_{\ell}$  , the bandlimited pulse shaping ﬁlter as    $p(\cdot)$  , the symbol period as    $T_{\mathrm{s}}$  , and the delay tap length as    $N_{\mathrm{d}}$   [42]. We select    $K=256$   subcarriers. We additionally denote the blockage coefﬁcient as    $c_{\mathrm{BL},\ell}[m]$  . The channel matrix at subcarrier  $k$   and time slot    $m$   can be  

<td><table  border="1"><thead><tr><td><b>Notation</b></td><td><b>Simulation parameter</b></td><td><b>Parameter value</b></td></tr></thead><tbody><tr><td>NREL</td><td>Number of candidate relays</td><td>2</td></tr><tr><td>NTx</td><td>Number of transmitter antennas</td><td>16</td></tr><tr><td>NRx</td><td>Number of receiver antennas</td><td>16</td></tr><tr><td>Op</td><td>Complex path gain spread</td><td>0.005</td></tr><tr><td>da</td><td>Angular spread</td><td>0.5</td></tr><tr><td>NBL</td><td>Number of time slots in a blockage</td><td>100</td></tr><tr><td>T</td><td>Symbol time</td><td>1/1760 μs</td></tr><tr><td>Mss</td><td>Number of time slots of a single SS burst</td><td>1</td></tr><tr><td>Nss</td><td>Number of SS blocks in single burst</td><td>64</td></tr><tr><td>Pu-→b</td><td>Transition probability from blocked state to unblocked state</td><td>0.01</td></tr><tr><td>Pb-u</td><td>Transition probability from unblocked state to blocked state</td><td>0.99</td></tr><tr><td>qb</td><td>Steady-state probability for the blocked state</td><td>0.01</td></tr><tr><td>K</td><td>Number of subcarriers</td><td>256</td></tr></tbody></table></td>  

expressed as  

$$
\begin{array}{r}{\boldsymbol{\mathsf{H}}[k,m]=\displaystyle\sum_{\ell=1}^{L[m]}c_{\mathrm{BL},\ell}[m]\alpha_{\ell}[m]\sum_{d=0}^{N_{\mathsf{d}}-1}p(d T_{\mathrm{s}}-\tau_{\ell})e^{-\mathrm{j}\frac{2\pi k}{K}}\mathbf{a}_{\mathsf{r}}(\phi_{\ell,\mathrm{A}}[m])\mathbf{a}_{\mathsf{t}}^{*}(\phi_{\ell,\mathrm{D}}[m]).}\end{array}
$$  

We assume that the complex path gain, angle of arrival, and angle of departure evolves according to a ﬁrst order Gauss-Markov equation, as in [41, Eq. 7]. We denote the angular spread as    $\sigma_{\mathrm{a}}$  , and the complex path gain spread as  $\sigma_{\mathfrak{p}}$  .  

Beam management and algorithm initialization:  We apply beam management with    $M_{S S}=1$  • and    $N_{\mathrm{SS}}=64$  . We assume the transmitter initially uses the direct link and performs initial access. We accordingly initialize the relay index as    $n[1]=0$   and the mode as    $n_{\mathrm{mode}}[1]=0$  . We initialize the link vectors as    $\mathbf{b}[1]=\{1,1,0,.\,.\,,1,1,0\}$  . We assume the data transmission takes a single time slot and accordingly set    $M_{\mathrm{DT}}=1$  .  

The parameter values used in both scenarios are organized in Table I.  

# B. Performance metrics and baseline policies  

We use the ensemble average spectral efﬁciency to track the performance metric. We approx- imate the ensemble mean by averaging over 1,000 identically distributed channel samples. For the performance of the DRL-based policy, we measure the average of the last 20 iterations out of the    $M=200$   total iterations to represent the converged reward. We compare the proposed DRL-based algorithm to three baseline policies:  

Genie-aided  policy: This algorithm has perfect knowledge of the channel. Subsequently, • this policy chooses the data transmission action with the correct relay index and the best beam indices. Therefore, the performance achieved by the genie-aided policy is the expected upper bound of the system.  Algorithm 1 with  optimal threshold : This algorithm applies Algorithm 1 with the optimal • thresholds    $\tau_{\mathrm{relay}}^{\mathrm{OPT}}$    and    $\tau_{\mathrm{mode}}^{\mathrm{OPT}}$  , where    $\tau_{\mathrm{relay}}^{\mathrm{OPT}}$    and    $\tau_{\mathrm{mode}}^{\mathrm{OPT}}$    are found by exhaustively searching over  $\tau_{\mathrm{relay}}$   and    $\tau_{\mathrm{mode}}$  ; we return the best result from the tests with varying    $\tau_{\mathrm{mode}}$   and    $\tau_{\mathrm{relay}}$   from  0 up to    $\tau_{\mathrm{max}}$   where    $\tau_{\mathrm{max}}$   is the   $99\%$   percentile of the achievable spectral efﬁciency.  Direct  policy: This algorithm chooses an action in each iteration following the genie- • aided policy and expect the relay index ﬁxed to zero. This policy represents the expected performance using suitable beam tracking and alignment without the aid of available relays.  

Selected implementation details that may be useful for reproduction are summarized as follows. To implement the proposed learning algorithm based on policy gradients, we use OpenAI Gym [43] as the environment template with Python TensorFlow. We set the action arguments    $a_{1}$  and    $a_{2}$   as real numbers such that    $\tau_{\mathrm{relay}}\,=\,10^{a_{1}/10}$    and    $\tau_{\mathrm{mode}}\,=\,10^{a_{1}/10}+10^{a_{2}/10}$  ; we learn the dB representation of the threshold    $\tau_{\mathrm{relay}}$   and the dB representation of the difference between thresholds  $\tau_{\mathrm{mode}}-\tau_{\mathrm{relay}}$  . We found this useful since it allows the  tanh  activation function which is known for its stable convergence in training the neural network. An implementation of our method is available on our github page [44].  

# C. Numerical evaluation with LOS channels  

In this section, we provide the experimental results for the scenario that only considers LOS channels between the vehicles. We observe the change in spectral efﬁciency when varying system parameters. We select the transmit SNR, complex path gain spread    $\sigma_{\mathrm{p}}$  , angular spread  $\sigma_{\mathrm{a}}$  , codebook size    $N_{\mathsf{c}}$  , beam management parameters    $N_{S S}$  ,    $M_{S S}$  , and blockage parameter    $q_{\mathfrak{b}}$   as the parameters of interest.  

We assume that the time-varying blockage model of the LOS channel scenario can be described by a Markov chain, as in [45]. The blockage model, depicted in Fig. 3, consists of two states indicating the path being blocked or unblocked. We denote the transition probabilities    $p_{\mathfrak{b}\to\mathfrak{u}}$   from blocked to unblocked state and  $p_{\mathtt{u}\rightarrow\mathtt{b}}$   from unblocked to blocked state. The transition probabilities determine the steady-state distribution of the two states. Denoting    $q_{\mathrm{u}}$   the steady-state probability of the unblocked state and    $q_{\mathfrak{b}}$   the steady-state probability of the blocked state,    $\begin{array}{r}{q_{\mathrm{u}}\,=\,\frac{p_{\mathrm{b}\to\mathrm{u}}}{p_{\mathrm{b}\to\mathrm{u}}+p_{\mathrm{u}\to\mathrm{b}}}}\end{array}$  → → and    $\begin{array}{r}{q_{\tt b}=\frac{p_{\tt u\to b}}{p_{\tt b\to u}+p_{\tt u\to b}}}\end{array}$  . We apply the blockage model along with the evolution of the time-varying  

  
Fig. 3. LOS blockage evolution model represented as a two-state Markov chain. The steady state probability of blocked state can be computed as    $q_{\mathsf{b}}=p_{\mathsf{u\to b}}/(p_{\mathsf{b\to u}}+p_{\mathsf{u\to b}})$  , given the transition probabilities    $p_{\mathfrak{b}\to\mathfrak{u}}$   from blocked to unblocked state and  $p_{\mathtt{u}\rightarrow\mathtt{b}}$   from unblocked to blocked state.  

propagation channel in (23). We assume that a state transition in the blockage model takes    $N_{\mathrm{{BL}}}$  time slots. Typically,    $N_{\mathrm{{BL}}}>>1$   since the duration of a blockage is much longer than the symbol period [45]. For each path    $\ell$  ,  $c_{\mathrm{BL},\ell}[m]=1$   for    $N_{\mathrm{{BL}}}$   time slots if the state transits to the unblocked state. If the state transits to the blocked state,    $c_{\mathrm{BL},\ell}[m]=0$   for    $N_{\mathrm{{BL}}}$   time slots.  

In Fig. 4 we illustrate the average spectral efﬁciency versus SNR, ranging over    $-20$   dB to  10 dB under the parameters speciﬁed in Table I. Fig. 4 shows that the proposed learning-based relay selection algorithm achieves spectral efﬁciency surpassing Algorithm 1 and the direct policy. This implies that the DRL-based policy is accurately choosing relay indexes to overcome the blockage of the direct LOS path. Furthermore, the DRL-based policy using    $\epsilon\cdot$  -greedy method efﬁciently balances the tradeoff between spectral efﬁciency gain from frequent beam alignment and loss from beam management overhead. When compared to Algorithm 1 using relays, the DRL-based policy achieves non-negligible spectral efﬁciency increase due to resolving the tradeoff.  

Fig. 5 illustrates the performance of the policies per channel parameters, complex path gain spread    $\sigma_{\mathfrak{p}}$   and angular spread    $\sigma_{\mathrm{a}}$  . Low    $\sigma_{\mathrm{p}}$   and high    $\sigma_{\mathrm{a}}$   translates to a fast-varying system with complex trafﬁc; the noise term becomes dominant in the recurrence relations of complex path gain, AOA, and AOD. For ﬁxed SNR at    $0\ \mathrm{dB}$  , we vary    $\sigma_{\mathrm{p}}$   and    $\sigma_{\mathrm{a}}$   within    $[0,1]$  . We ﬁx the  

  
Fig. 4. Average spectral efﬁciency vs. transmit SNR for (i) the genie-aided policy, (ii) the DRL-based policy, (iii) the relay selection heuristic with optimal threshold, and (iv) the policy that only use the direct link. Allowing the use of relays improve spectral efﬁciency overcoming the blockage of LOS path. Relay selection based on DRL further increases spectral efﬁciency over random selection by balancing exploration and exploitation with    $\epsilon$  -greedy method.  

  
Fig. 5. Average spectral efﬁciency vs. channel parameters (a) complex path gain spread    $\sigma_{\mathrm{p}}$   and (b) angular spread    $\sigma_{\mathrm{a}}$  . The DRL-based policy achieves more spectral efﬁciency compared to the baselines under low complex path gain spread  $\sigma_{\mathrm{p}}$  . Spectral efﬁciency achieved by the DRL-based policy degrades slower as the    $\sigma_{\mathrm{a}}$   increases compared to that of the baseline with prior channel knowledge.  

angular spread to  0 . 5  when varying    $\sigma_{\mathrm{p}}$   and we ﬁx the standard deviation of complex path gain noise to  0 . 005  when varying    $\sigma_{\mathrm{a}}$  . The DRL-based policy still outperforms Algorithm 1 and the direct policy for varying    $\sigma_{\mathfrak{p}}$   and    $\sigma_{\mathrm{a}}$  . We observe interesting behaviors for speciﬁc    $\sigma_{\mathfrak{p}}$   and    $\sigma_{\mathrm{a}}$  regimes. For instance, the DRL-based policy gain more performance per decreased    $\sigma_{\mathrm{p}}$   compared to the baselines. This indicates that the DRL-based policy may be further enhanced with power allocation designs that address variant complex path gain. The performance of the DRL-based policy is resilient against increasing    $\sigma_{\mathrm{a}}$   compared to that of Algorithm 1 and direct policy. This implies that the DRL-based policy is particularly beneﬁcial under highly-variant channels.  

  
Fig. 6. Average spectral efﬁciency vs. transmit SNR for different codebook sizes. The relay codebook sizes and receiver codebook size are set equal to    $N_{\mathsf{c}}$  . Increasing the codebook size from small    $N_{\mathsf{c}}$   results an increase of spectral efﬁciency due to accurate quantization of the beam angles. For high  $N_{\mathsf{c}}$  , however, the overhead from beam management dominates the quantization accuracy resulting in a decrease of spectral efﬁciency.  

  
Fig. 7. Average spectral efﬁciency vs. different beam management parameters: (a)    $N_{S S}$   and (b)    $M_{S S}$  . Decreasing    $N_{S S}$   and increasing    $M_{S S}$   results in larger overhead spent in initial access and beam tracking. While the DRL-based policy outperforms the baselines in most  $N_{S S}$   and    $M_{S S}$   condition, it may underperform under extreme overhead.  

Fig. 6 shows the impact of codebook size on the performance of policies. We vary the codebook size for the transmitter, relay, and receiver from  4  to  64  for the 16-element ULA equipment. We observe that increasing the codebook size from  $N_{\mathrm{c}}=4$  , all strategies gain spectral efﬁciency. This is expected, since it is known that insufﬁcient quantization of beam angles results in performance degradation for analog beamforming [46]. At    $N_{\mathrm{c}}=16$  , increasing the codebook size results in a decrease of spectral efﬁciency except for the genie-aided policy. This indicates the spectral efﬁciency lost in the beam management procedure dominates the spectral efﬁciency gain from higher beam angle quantization. Fig. 6 suggests that there is a codebook size that maximizes the spectral efﬁciency. While we simulated a codebook equally partitioning the angular domain  

  
Fig. 8. Average spectral efﬁciency vs. different blockage parameter  $q_{\mathsf{b}}$  . Various blockage parameters  $q_{\mathfrak{b}}\quad\in\quad\in$  ∈  $\{0.0001,0.001,0.01,0.1,0.5\}$   are plotted to represent the negligible    $(q_{\tt b}<0.01)$  , low    $q_{\tt b}=0.01)$  ) , and high    $q_{\tt b}=0.5)$  )  trafﬁc densities. The DRL-based policy shows gradual slope similar to that of genie-aided policy’s, which implies that it effectively mitigates blockage similar to the optimal policy.  

$[0,\pi]$  , it is likely that a similar tradeoff between beam angle quantization and overhead from codebook size exists for other codebooks.  

In Fig. 7 we demonstrate the effect of the parameters related to SS bursts and blocks. We vary the number    $N_{S S}$   of SS blocks per burst in    $\{8,16,32,64\}$   and periodicity    $M_{S S}$   of SS bursts in  $\{1,2,4,8,16\}$  , as in [22]. Fig. 7 shows that the DRL-based policy outperforms baselines in most cases but it may underperform when    $N_{S S}$   is low or    $M_{S S}$   is high. For example, the DRL-based policy severely lose performance both at    $N_{S S}=4$   and    $M_{S S}=16$  . Such low performance of the DRL-based algorithm happens because the increased time slots required for exploration causes the learning algorithm to fail to converge. This implies that the DRL-based policy is sensitive to beam management parameters, but it works well under practical scenarios.  

Fig. 8 illustrates the effect of the blockage parameter. We vary the steady-probability    $q_{\tt b}$   of blocked state in    $\{0.0001,0.001,0.01,0.1,0.5\}$  . For a given    $q_{\tt b}$  , we use a Markov chain in Fig. 3 with transition probabilities set to    $p_{\mathtt{u}\to\mathtt{b}}=q_{\mathtt{b}}$   and    $p_{\mathsf{b}\to\mathsf{u}}=1\!-\!p_{\mathsf{u}\to\mathsf{b}}$  . We simulate the scenario with a high vehicular density by setting    $q_{\tt b}=0.5$  , low density by setting    $q_{\tt b}=0.01$  , and negligible density by setting  $q_{\tt b}<0.01$  . Fig. 8 depicts that DRL-based policy behaves similarly to the genie- aided policy over the change of    $q_{\mathfrak{b}}$   compared to baselines. Both baselines severely lose spectral efﬁciency compared to the DRL-based policy within the negligible density regime, whereas the genie-aided policy suggests high spectral efﬁciency can be maintained within the negligible density regime. This implies that the DRL-based policy is able to effectively mitigate blockage by jointly selecting the relay and the mode.  

D. Numerical evaluation on SUMO-generated channel  

In this section, we provide the experimental results for the scenario that represents a more realistic deployment of a mmWave MIMO vehicular network. We follow the approach in [47] to generate the channels based on the time-varying wideband channel (23) and the vehicle trajectories from SUMO. We apply a simple ray tracing method to obtain the number of paths  $L[m]$   and blockage coefﬁcient    $c_{\mathrm{BL},\ell}[m]$   assuming all vehicles have length of    $4.645\mathrm{~m~}$  , vehicles can block LOS, and the vehicle surfaces act as lossless reﬂectors to create reﬂected paths. We calculate the AOA/AOD and path gain assuming the ray propagation starts at the end of vehicles facing each other, the angle of the reﬂected ray by the vehicle surface is equal to the angle of incident ray, and the path loss exponent is 2. We report the change in spectral efﬁciency when varying system parameters. We select the transmit SNR, vehicle density, and average vehicle speed as the parameters of interest.  

In Fig. 9 we show the average spectral efﬁciency versus SNR, ranging over    $-20~\mathrm{dB}$   to  10  dB under the parameters speciﬁed in Table I. We set the trafﬁc density as 10 vehicles per km and the average vehicle speed as   $80~\mathrm{km/h}$  . Fig. 9 conﬁrms that the proposed DRL-based relay selection policy outperforms baselines in a realistic scenario. We observe the spectral efﬁciency obtained using Algorithm 1 is closer to the spectral efﬁciency using the direct policy decrease compared to that in Fig. 4. This highlights the model-free aspect of the proposed DRL algorithm, which may further outperform policies based on ﬁxed data in realistic scenarios due to the increased model complexity.  

Fig. 10 shows the effect of vehicle density. We vary the number of vehicles per kilometer from 10 to 50 in the SUMO simulation. We observe a loss spectral efﬁciency achieved by the proposed DRL-based policy as the vehicle density increases. Still, the performance loss of the DRL-based policy due to the increase in the vehicle density is minor compared to that of direct policy, which plummets in the congested case. Since the direct policy only uses the direct link, this indicates that cooperative relays become more beneﬁcial as the vehicular networks gets denser.  

Fig. 11 depicts the impact of average vehicle speed. We select the range of vehicle speed from  $80\ \mathrm{km/h}$   to   $120\ \mathrm{km/h}$  , following the common highway speed limit in the United States. The  

  
Fig. 9. Average spectral efﬁciency vs. transmit SNR for (i) the genie-aided policy, (ii) the DRL-based policy, (iii) the relay selection heuristic with optimal threshold, and (iv) the policy that only use the direct link. Similar to that observed in Fig. 4, the proposed DRL-based policy improves spectral efﬁciency over baseline methods.  

  
Fig. 10. Average spectral efﬁciency vs. different vehicle densities. Overall policies suffer spectral efﬁciency loss due to the increased chance of blockage from higher vehicle density. Still, the proposed DRL-based policy outperforms baselines, especially under dense vehicle networks, by efﬁciently using the indirect links to avoid the frequent blockage of the LOS paths.  

spectral efﬁciency of all the policies gradually improves as the average vehicle speed increases. The performance enhancement may be due to the decreased blockage duration from the increased vehicle speed, despite negative performance factors such as increased beam alignment frequencies [48]. The proposed DRL algorithm shows the steepest increase of spectral efﬁciency compared to the baselines. Fig. 11 indicates that proposed relay selection algorithm is suitable for mobile vehicular networks, especially those with high mobility.  

# VI. C ONCLUSIONS AND FUTURE WORK  

Future vehicular networks will beneﬁt from relay selection algorithms addressing the frequent blockages induced by dense deployment of mobile nodes. Regarding the higher frequency bands used at 5G at beyond, sources of overhead should be incorporated in the analysis of relay  

  
Fig. 11. Average spectral efﬁciency vs. average vehicle speeds. Increased mobility, which may decrease the blockage duration, shows an overall increase in spectral efﬁciency for all of the considered policies. The proposed DRL-based policy outperforms baselines, especially under highly mobile networks.  

selection algorithms. We derived an MDP and devised a DRL-based algorithm for the spectral efﬁciency optimization problem accounting both relay selection and beam management. We observed that the spectral efﬁciency achieved by the proposed method is greater than that of a ﬁxed threshold policy over different transmit SNRs. The simulation results show that the DRL-based algorithm can adapt to fast-varying channels using beam measurements, which are compared with thresholds, to determine actions. This indicates the proposed DRL algorithm can be implemented to vehicular networks to maximize spectral efﬁciency by exploiting the time- varying adaptive thresholds. For future work, we plan to extend our work to incorporate fast beam alignment algorithms and realistic beam measurement feedback procedures.  

# R EFERENCES  

[1] V. Va, T. Shimizu, G. Bansal, and R. W. Heath Jr, “Millimeter wave vehicular communications: A survey,”  Found. Trends Netw. , vol. 10, no. 1, pp. 1–118, 2016.

 [2] M. H. C. Garcia, A. Molina-Galan, M. Boban, J. Gozalvez, B. Coll-Perales, T. S ¸ahin, and A. Kousaridas, “A Tutorial on 5G NR V2X Communications,”  IEEE Commun. Surveys Tuts. , Feb. 2021.

 [3] S.-W. Kim, W. Liu, M. H. Ang, E. Frazzoli, and D. Rus, “The impact of cooperative perception on decision making and planning of autonomous vehicles,”  IEEE Intell. Transp. Syst. Mag. , vol. 7, no. 3, pp. 39–50, Jul. 2015.

 [4] J. Choi, V. Va, N. Gonzalez-Prelcic, R. Daniels, C. R. Bhat, and R. W. Heath, “Millimeter-wave vehicular communication to support massive automotive sensing,”  IEEE Commun. Mag. , vol. 54, no. 12, pp. 160–167, Dec. 2016.

 [5] A. Tassi, M. Egan, R. J. Piechocki, and A. Nix, “Modeling and design of millimeter-wave networks for highway vehicular communication,”  IEEE Trans. Veh. Technol. , vol. 66, no. 12, pp. 10 676–10 691, Dec. 2017.

 [6] M. Gapeyenko, A. Samuylov, M. Gerasimenko, D. Moltchanov, S. Singh, M. R. Akdeniz, E. Aryafar, N. Himayat, S. Andreev, and Y. Koucheryavy, “On the temporal effects of mobile blockers in urban millimeter-wave cellular scenarios,” IEEE Trans. Veh. Technol. , vol. 66, no. 11, pp. 10 124–10 138, Nov. 2017.  

[7] S. Rangan, T. S. Rappaport, and E. Erkip, “Millimeter-wave cellular wireless networks: Potentials and challenges,”  Proc. IEEE , vol. 102, no. 3, pp. 366–385, Mar. 2014.

 [8] F. J. Martin-Vega, M. C. Aguayo-Torres, G. Gomez, J. T. Entrambasaguas, and T. Q. Duong, “Key technologies, modeling approaches, and challenges for millimeter-wave vehicular communications,”  IEEE Commun. Mag. , vol. 56, no. 10, pp. 28–35, 2018.

 [9] V. Va, J. Choi, and R. W. Heath, “The impact of beamwidth on temporal channel variation in vehicular channels and its implications,”  IEEE Trans. Veh. Technol. , vol. 66, no. 6, pp. 5014–5029, Jun. 2017.

 [10] G. H. Sim, S. Klos, A. Asadi, A. Klein, and M. Hollick, “An online context-aware machine learning algorithm for 5G mmWave vehicular communications,”  IEEE/ACM Trans. Netw. , vol. 26, no. 6, pp. 2487–2500, Dec. 2018.

 [11] W. Wu, N. Cheng, N. Zhang, P. Yang, W. Zhuang, and X. Shen, “Fast mmwave beam alignment via correlated bandit learning,”  IEEE Trans. Wireless Commun. , vol. 18, no. 12, pp. 5894–5908, Dec. 2019.

 [12] C. Perfecto, J. Del Ser, and M. Bennis, “Millimeter-wave V2V communications: Distributed association and beam alignment,”  IEEE J. Sel. Areas Commun. , vol. 35, no. 9, pp. 2148–2162, Sep. 2017.

 [13] Y. Ma, Z. Wang, H. Yang, and L. Yang, “Artiﬁcial intelligence applications in the development of autonomous vehicles: a survey,”  IEEE/CAA J. Automatica Sinica , vol. 7, no. 2, pp. 315–329, Mar. 2020.

 [14] B. Fan, H. Tian, S. Zhu, Y. Chen, and X. Zhu, “Trafﬁc-aware relay vehicle selection in millimeter-wave vehicle-to-vehicle communication,”  IEEE Wireless Commun. Lett. , vol. 8, no. 2, pp. 400–403, Apr. 2019.

 [15] H. Zhang, S. Chong, X. Zhang, and N. Lin, “A deep reinforcement learning based D2D relay selection and power level allocation in mmWave vehicular networks,”  IEEE Wireless Commun. Lett. , vol. 9, no. 3, pp. 416–419, Mar. 2020.

 [16] Z. Li, L. Xiang, X. Ge, G. Mao, and H.-C. Chao, “Latency and reliability of mmWave multi-hop V2V communications under relay selections,”  IEEE Trans. Veh. Technol. , vol. 69, no. 9, pp. 9807–9821, Sep. 2020.

 [17] Y. Geng, E. Liu, R. Wang, Y. Liu, J. Wang, G. Shen, and Z. Dong, “Deep deterministic policy gradient for relay selection and power allocation in cooperative communication network,”  IEEE Commun. Lett. , vol. 10, no. 9, pp. 1969–1973, Sep. 2021.

 [18] M. B. Booth, V. Suresh, N. Michelusi, and D. J. Love, “Multi-armed bandit beam alignment and tracking for mobile millimeter wave communications,”  IEEE Commun. Lett. , vol. 23, no. 7, pp. 1244–1248, Jul. 2019.

 [19] N. C. Luong, D. T. Hoang, S. Gong, D. Niyato, P. Wang, Y.-C. Liang, and D. I. Kim, “Applications of deep reinforcement learning in communications and networking: A survey,”  IEEE Commun. Surveys Tuts. , vol. 21, no. 4, pp. 3133–3174, 4th Quart. 2019.

 [20] F. Tang, Y. Kawamoto, N. Kato, and J. Liu, “Future intelligent and secure vehicular network toward 6G: Machine-learning approaches,” in  Proc. IEEE , vol. 108, no. 2, Feb. 2019, pp. 292–307.

 [21] N. Van Huynh, D. N. Nguyen, D. T. Hoang, and E. Dutkiewicz, “Optimal beam association for high mobility mmWave vehicular networks: Lightweight parallel reinforcement learning approach,”  IEEE Trans. Commun. , vol. 69, no. 9, pp. 5948–5961, Sep. 2021.

 [22] M. Giordani, M. Polese, A. Roy, D. Castor, and M. Zorzi, “A tutorial on beam management for 3GPP NR at mmWave frequencies,”  IEEE Commun. Surveys Tuts. , vol. 21, no. 1, pp. 173–196, 1st Quart. 2019.

 [23] S. Wu, R. Atat, N. Mastronarde, and L. Liu, “Improving the coverage and spectral efﬁciency of millimeter-wave cellular networks using device-to-device relays,”  IEEE Trans. Commun. , vol. 66, no. 5, pp. 2251–2265, May 2017.

 [24] Y. Hu, C. Schnelling, M. C. Gursoy, and A. Schmeink, “Multi-relay-assisted low-latency high-reliability communications with best single relay selection,”  IEEE Trans. Veh. Technol. , vol. 68, no. 8, pp. 7630–7642, Aug. 2019.  

[25] Z. Tian, Y. Gong, G. Chen, and J. A. Chambers, “Buffer-aided relay selection with reduced packet delay in cooperative networks,”  IEEE Trans. Veh. Technol. , vol. 66, no. 3, pp. 2567–2575, Mar. 2017.

 [26] R. Ma, Y.-J. Chang, H.-H. Chen, and C.-Y. Chiu, “On relay selection schemes for relay-assisted D2D communications in LTE-A systems,”  IEEE Trans. Veh. Technol. , vol. 66, no. 9, pp. 8303–8314, Sep. 2017.

 [27] Y. Su, X. Lu, Y. Zhao, L. Huang, and X. Du, “Cooperative communications with relay selection based on deep reinforcement learning in wireless sensor networks,”  IEEE Sensors J. , vol. 19, no. 20, pp. 9561–9569, Oct. 2019.

 [28] J. Zhang, J. Tang, and F. Wang, “Cooperative relay selection for load balancing with mobility in hierarchical WSNs: A multi-armed bandit approach,”  IEEE Access , vol. 8, pp. 18 110–18 122, 2020.

 [29] H. Zhao, X. Li, S. Han, L. Yan, and J. Yu, “Adaptive relay selection strategy in underwater acoustic cooperative networks: a hierarchical adversarial bandit learning approach,”  IEEE Trans. Mobile Comput., early access , Sep. 2021, doi: 10.1109/ TMC.2021.3112967.

 [30] K. Venugopal, N. Gonz´ alez-Prelcic, and R. W. Heath, “Optimality of frequency ﬂat precoding in frequency selective millimeter wave channels,”  IEEE Commun. Lett. , vol. 6, no. 3, pp. 330–333, Jun. 2017.

 [31] R. W. Heath Jr and A. Lozano,  Foundations of MIMO communication . Cambridge, U.K.: Cambridge University Press, 2018.

 [32] S. Park, A. Alkhateeb, and R. W. Heath, “Dynamic subarrays for hybrid precoding in wideband mmWave MIMO systems,” IEEE Trans. Wireless Commun. , vol. 16, no. 5, pp. 2907–2920, May 2017.

 [33] T. Liu, C. Yang, and L.-L. Yang, “A uniﬁed analysis of spectral efﬁciency for two-hop relay systems with different resource conﬁgurations,”  IEEE Trans. Veh. Technol. , vol. 62, no. 7, pp. 3137–3148, Sep. 2013.

 [34] S. Noh, M. D. Zoltowski, and D. J. Love, “Multi-resolution codebook and adaptive beamforming sequence design for millimeter wave beam alignment,”  IEEE Trans. Wireless Commun. , vol. 16, no. 9, pp. 5689–5701, Sep. 2017.

 [35] P. S. Bithas, G. P. Efthymoglou, and A. G. Kanatas, “V2V cooperative relaying communications under interference and outdated CSI,”  IEEE Trans. Veh. Technol. , vol. 67, no. 4, pp. 3466–3480, Apr. 2017.

 [36] A. Laourine and L. Tong, “Betting on Gilbert-Elliot channels,”  IEEE Trans. Wireless Commun. , vol. 9, no. 2, pp. 723–733, Feb. 2010.

 [37] R. S. Sutton and A. G. Barto,  Reinforcement learning: An introduction . Cambridge, MA, USA: MIT press, 2018.

 [38] T. P. Lillicrap, J. J. Hunt, A. Pritzel, N. Heess, T. Erez, Y. Tassa, D. Silver, and D. Wierstra, “Continuous control with deep reinforcement learning,”  arXiv preprint arXiv:1509.02971 , 2015.

 [39] S. Fujimoto, H. Hoof, and D. Meger, “Addressing function approximation error in actor-critic methods,” in  Proc. Int. Conf. Mach. Learn. , vol. 80, Jul. 2018, pp. 1587–1596.

 [40] D. Krajzewicz, J. Erdmann, M. Behrisch, and L. Bieker, “Recent development and applications of SUMO-Simulation of Urban MObility,”  Int. J. Adv. Syst. Meas. , vol. 5, no. 3-4, 2012.

 [41] V. Va, H. Vikalo, and R. W. Heath, “Beam tracking for mobile millimeter wave communication systems,” in  Proc. IEEE Global Conf. Signal Inf. Process. , Dec. 2016, pp. 743–747.

 [42] S. Park, A. Ali, N. Gonz´ alez-Prelcic, and R. W. Heath, “Spatial channel covariance estimation for hybrid architectures based on tensor decompositions,”  IEEE Trans. Wireless Commun. , vol. 19, no. 2, pp. 1084–1097, Feb. 2020.

 [43] G. Brockman, V. Cheung, L. Pettersson, J. Schneider, J. Schulman, J. Tang, and W. Zaremba, “OpenAI gym,”  arXiv preprint arXiv:1606.01540 , 2016.

 [44] D. Kim, “Joint relay selection and beam management,” https://github.com/dohyunkim93/ Joint-relay-selection-beam-management, 2022.  

[45] M. Boban, X. Gong, and W. Xu, “Modeling the evolution of line-of-sight blockage for V2V channels,” in  Proc. IEEE Veh. Technol. Conf. , Jun. 2016, pp. 1–7.

 [46] O. El Ayach, S. Rajagopal, S. Abu-Surra, Z. Pi, and R. W. Heath, “Spatially sparse precoding in millimeter wave MIMO systems,”  IEEE Trans. Wireless Commun. , vol. 13, no. 3, pp. 1499–1513, Mar. 2014.

 [47] A. Klautau, P. Batista, N. Gonz´ alez-Prelcic, Y. Wang, and R. W. Heath, “5G MIMO data for machine learning: Application to beam-selection using deep learning,” in  Proc. Inf. Theory Appl. Workshop . IEEE, 2018, pp. 1–9.

 [48] C. Tunc, M. F.  Ozkoc ¸, F. Fund, and S. S. Panwar, “The blind side: Latency challenges in millimeter wave networks for connected vehicle applications,”  IEEE Trans. Veh. Technol. , vol. 70, no. 1, pp. 529–542, Jan. 2021.  