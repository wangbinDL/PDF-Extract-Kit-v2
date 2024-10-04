# Filtering and smoothing estimation algorithms from uncertain nonlinear observations with time-correlated additive noise and random deception attacks 

R. Caballero-Águilaa ${ }^{a}$, J. Hub ${ }^{b}$ and J. Linares-Pérez ${ }^{c}$<br>${ }^{a}$ Departamento de Estadística. Universidad de Jaén. Paraje Las Lagunillas. 23071. Jaén. Spain;<br>${ }^{b}$ Key Laboratory of Advanced Manufacturing and Intelligent Technology, Ministry of Education,<br>Harbin University of Science and Technology, Harbin 150080, China;<br>${ }^{c}$ Departamento de Estadística. Universidad de Granada. Avenida Fuentenueva. 18071. Granada. Spain

## ARTICLE HISTORY

Compiled May 9, 2024


#### Abstract

This paper discusses the problem of estimating a stochastic signal from nonlinear uncertain observations with time-correlated additive noise described by a first-order Markov process. Random deception attacks are assumed to be launched by an adversary, and both this phenomenon and the uncertainty in the observations are modelled by two sets of Bernoulli random variables. Under the assumption that the evolution model generating the signal to be estimated is unknown and only the mean and covariance functions of the processes involved in the observation equation are available, recursive algorithms based on linear approximations of the real observations are proposed for the least-squares filtering and fixed-point smoothing problems. Finally, the feasibility and effectiveness of the developed estimation algorithms are verified by a numerical simulation example, where the impact of uncertain observation and deception attack probabilities on estimation accuracy is evaluated.


## KEYWORDS

Nonlinear observation models; least-squares estimation; missing measurements; time-correlated noise; random deception attacks

## 1. Introduction

Although state-space models can theoretically be divided into linear and nonlinear models, in practice there are no strictly linear models. So-called linear systems are nothing more than approximations, usually valid over a limited range of values of the variables involved in the model. Even though many systems have a sufficiently high degree of approximation to linearity, we eventually encounter systems that deviate significantly from linear behaviour, even within a limited operating range. In such cases, the accuracy of linear estimation techniques diminishes and it becomes necessary to explore nonlinear estimation approaches (Simon, 2006). Despite these considerations, there has been a huge amount of work on linear estimation for linear systems and the mathematical tools available for this kind of systems are much more accessible and well understood. For this reason, linear approximations are often used to adapt linear estimation techniques to the nonlinear problems that are encountered in



many branches of practical domains, such as computer vision, communications, navigation and tracking systems or econometrics and finance (Hu et al., 2015).

The performance of estimation algorithms is often affected by the occurrence of random uncertainties, a common one being the presence of missing measurements (also called uncertain observations). Indeed, this phenomenon is unavoidable in many real-world scenarios where the information received by the estimator side is usually incomplete, due to several causes (e.g., random failures in the measurement mechanism, accidental loss of some data packets or inaccessibility of data at certain times). In these situations, it is necessary to consider the influence of this incomplete information when designing estimation algorithms. In the context of linear systems, the estimation problem for multisensor stochastic uncertain systems with missing measurements and unknown measurement disturbances is addressed in Pang \& Sun (2015). Using a new augmented state approach, three robust Kalman-like filtering algorithms are proposed in Ran \& Deng (2020) for a class of multisensor systems with mixed uncertainties including random delays, missing measurements, multiplicative noises and uncertain noise variances. The distributed filtering problem for systems with missing measurements is studied in Wen et al. (2020), under the assumption that the state noises and the measurement noises are correlated. In the context of nonlinear systems, the impact of incomplete information on the estimation problem has also been analyzed, e.g., in Hu et al. (2023b), where a class of singular systems subject to random delays, packet dropouts and nonlinearities, and in Han et al. (2017), where a distributed $\mathcal{H}_{\infty}$-consensus filtering approach is proposed for nonlinear systems with missing measurements. More recently, a particle filter is proposed in Ma \& Wang (2022) for nonlinear systems with time-varying delays and unknown noise distribution and, in Hu et al. (2023a), a distributed resilient fusion filtering algorithm is designed for nonlinear systems with dynamic event-triggered mechanism under the missingmeasurement phenomenon. A complete survey on estimation algorithms for nonlinear systems with communication constraints causing random delays, missing/fading measurements or randomly occurring incomplete information can be found in Hu et al. (2020).

Many conventional estimation algorithms are typically based on the assumption that the additive noise in measurements is either white or finite-step correlated. However, in practical engineering applications, infinite-step correlated measurement noises can be prevalent, especially when the sampling frequency is sufficiently high, leading to significant correlation over two or more consecutive sampling periods. Over the past decade, the estimation problem has been widely studied under the assumption that the infinite-step time-correlated noise is a first-order Markov process. The state estimation problem for linear systems with multiplicative noise and time-correlated additive noise in the measurements has been investigated in Liu (2015) and an improved steady-state filter has been designed in Liu \& Shi (2019). Least-squares estimation algorithms are proposed in García-Ligero et al. (2020), considering random delays in the transmission connections that are modelled by Markov chains, and in Caballero-Águila et al. (2022), considering random parameter matrices in the measurement model and random packet dropouts for which two different compensation scenarios are compared. Distributed fusion filtering algorithms for uncertain systems with random delays and packet loss prediction compensation are designed in Caballero-Águila \& Linares-Pérez (2023a). Recursive estimation algorithms for linear stochastic uncertain systems with timecorrelated additive noises and packet dropout compensations are proposed in Ma \& Sun (2020) and a similar study for nonlinear systems is carried out in Cheng et al. (2021).

In addressing the estimation problem, security emerges as a crucial consideration that should not be disregarded. The vulnerability to cyber attacks is well-documented in the literature (see, for instance, Mahmoud et al., 2019; Sanchez et al., 2019). Particularly, the es-



timation problem in networked systems exposed to deception attacks has been the focus of numerous significant research endeavors. In general, deception attackers aim to compromise data integrity by maliciously introducing random falsifications into their information. Several research studies have delved into security-guaranteed filtering problems, such as the investigation of centralized solutions for linear time-invariant stochastic systems with multirate-sensor fusion under deception attacks in Wang et al. (2018). The exploration of the $H_{\infty}$-consensus filtering problem for discrete-time systems with multiplicative noises and deception attacks is documented in Han et al. (2019). Additionally, the study of the chance-constrained $H_{\infty}$ state estimation problem for a class of time-varying neural networks, subject to measurement degradation and randomly occurring deception attacks, is presented in Qu et al. (2022). Also, the distributed estimation problem in sensor networks has been addressed under various security threats. Examples include investigations under false data injection attacks in Yang et al. (2019) and under deception attacks in Caballero-Águila \& Linares-Pérez (2023b), Xiao et al. (2020), Ma \& Sun (2023) and Ma et al. (2021).

Motivated by the preceding discussion, our aim is to address the least-squares (LS) estimation problem of signals using nonlinear uncertain observations (missing measurements) with time-correlated additive noise modeled by a first-order Markov process, in the presence of random deception attacks. The proposed recursive algorithms, based on linear approximations, offer a novel approach to mitigating the impact of missing measurements and deception attacks in signal estimation. The main contributions of this paper are summarized as follows: (a) A covariance-based estimation approach is used, so the evolution model of the signal to be estimated does not need to be known. (b) The class of stochastic signals investigated in this paper is quite comprehensive, as the assumptions under which our study is valid are verified by a great variety of stationary and non-stationary signals. (c) The direct estimation of the time-correlated additive noise avoids the use of the differencing method or vector augmentation. (d) Despite the fact that the simultaneous consideration of uncertain observations, time-correlated noise and random attacks adds complexity to the model, the proposed filtering and fixed-point smoothing algorithms keep the advantages of recursivity and computational simplicity. (e) The proposed estimators have a satisfactory performance even in the presence of high probability of missing measurements and/or high probability of successful random deception attacks.

The paper is structured as follows. Section 2 details the characteristics of the observation model under consideration. The main results are presented in Section 3, which includes the problem statement (subsection 3.1) and the derivation of the proposed filtering and fixed-point smoothing algorithms (subsections 3.2 and 3.3, respectively). Section 4 conducts a simulation study to showcase the effectiveness of the proposed filtering and fixed-point smoothing estimators, additionally exploring the impact of uncertain observation and random deception attacks probabilities on estimation performance. Finally, Section 5 provides some concluding remarks.

The notations and acronyms that are used throughout the paper are summarized in Table 1.

# 2. Mathematical model and preliminaries 

### 2.1. Signal process

Consider a signal process $\left\{x_{k}\right\}_{k \geq 1}$ that must be estimated from a set of noisy measurements. Assume that the mathematical model describing the evolution of this signal process is not known, but its mean and covariance functions satisfy the following hypothesis:



Table 1. Notations and acronyms used throughout the paper. All vector and matrix dimensions are assumed to be compatible with algebraic operations unless explicitly stated.


(H1) The $n_{\mathrm{x}}$-dimensional signal $\left\{\mathbf{x}_{k}\right\}_{k>1}$ is a second-order zero-mean random process and its covariance function, $\Sigma_{k, s}^{x}=\operatorname{Cov}\left[\mathbf{x}_{k}, \mathbf{x}_{s}\right]$, can be factorized as

$$
\Sigma_{k, s}^{x}=\mathbf{A}_{k} \mathbf{B}_{s}^{T}, s \leq k
$$

where $\mathbf{A}_{k}, \mathbf{B}_{s} \in \mathbb{R}^{n_{\mathrm{x}} \times p}$ are known matrices.
Remark 1. Hypothesis (H1) on the signal covariance function is verified by a great variety of stationary and non-stationary signals (Caballero-Águila et al., 2022). Estimation approaches based on this hypothesis, rather than the state-space model, thus provide a comprehensive framework to obtain general algorithms that cover a wide range of practical situations.

# 2.2. Nonlinear uncertain measurements with time-correlated additive noise 

The signal estimation will be performed from $n_{\mathrm{z}}$-dimensional nonlinear outputs that are perturbed by additive noise and subject to random failures, causing that some measured outputs are only noise. This phenomenon is described by a sequence of Bernoulli random variables, $\left\{\gamma_{k}\right\}_{k \geq 1}$. When $\gamma_{k}=1$, the actual measurement value is equal to the original measurement value, while $\gamma_{k}=0$ means that the actual measurement is only noise. More specifically, the actual measurements are described by the following mathematical model:

$$
\mathbf{z}_{k}=\gamma_{k} \mathbf{h}_{k}\left(\mathbf{x}_{k}\right)+\mathbf{v}_{k}, \quad k \geq 1
$$

with the following hypotheses:
(H2) $\left\{\gamma_{k}\right\}_{k \geq 1}$ is a sequence of independent Bernoulli random variables with known mean function $\gamma_{k}=\mathbb{E}\left[\gamma_{k}\right], k \geq 1$.
(H3) For all $k \geq 1$, the function $\mathbf{h}_{k}: \mathbb{R}^{n_{\mathrm{x}}} \rightarrow \mathbb{R}^{n_{\mathrm{z}}}$ is an analytic function.

Remark 2. Hypothesis (H3) guarantees that $\mathbf{h}_{k}$ is infinitely differentiable and, for every $\mathbf{x}_{0} \in$ $\mathbb{R}^{n_{\mathrm{x}}}$, its Taylor series about $\mathbf{x}_{0}$ converges to the function in some neighborhood of $\mathbf{x}_{0}$. Typical examples of analytic functions are: polynomials, exponential functions, logarithmic functions, trigonometric functions and power functions (Krantz, 2022).



In many engineering applications, the additive noise perturbing the observations has an infinite-step correlation; to better model such situations, the following first-order Markov model is used:

$$
\mathbf{v}_{k}=D_{k-1} \mathbf{v}_{k-1}+\mathbf{u}_{k-1}, \quad k \geq 1
$$

where $D_{k}$ is non-singular for all $k \geq 0$ and the following hypotheses hold:
$\left(\mathbf{H}_{4}\right) \mathbf{v}_{0}$ is a zero-mean random vector with known covariance $\boldsymbol{\Sigma}_{0}^{v}=\operatorname{Cov}\left[\mathbf{v}_{0}\right]$.
$\left(\mathbf{H}_{5}\right)$ The noise process $\left\{\mathbf{u}_{k}\right\}_{k \geq 0}$ is a zero-mean white sequence with known covariance function $\boldsymbol{\Sigma}_{k}^{u}=\operatorname{Cov}\left[\mathbf{u}_{k}\right], k \geq 0$, and it is independent of the initial vector $\mathbf{v}_{0}$.

Remark 3. Hypotheses ( $\mathbf{H}_{4}$ ) and ( $\mathbf{H}_{5}$ ), together with the non-singularity of $D_{k}$, guarantee that the covariance function of the time-correlated additive noise, $\boldsymbol{\Sigma}_{k, s}^{v}=\operatorname{Cov}\left[\mathbf{v}_{k}, \mathbf{v}_{s}\right]$, admits the following factorization:

$$
\boldsymbol{\Sigma}_{k, s}^{v}=\mathbf{E}_{k} \mathbf{F}_{s}^{T}, \quad s \leq k
$$

where $\mathbf{E}_{k}=D_{k-1} \cdots D_{0}, \mathbf{F}_{s}=\boldsymbol{\Sigma}_{s}^{v}\left(\mathbf{E}_{s}^{-1}\right)^{T}$ and $\boldsymbol{\Sigma}_{s}^{v}=\operatorname{Cov}\left[\mathbf{v}_{s}\right]$ is recursively obtained as

$$
\boldsymbol{\Sigma}_{s}^{v}=D_{s-1} \boldsymbol{\Sigma}_{s-1}^{v} D_{s-1}^{T}+\boldsymbol{\Sigma}_{s-1}^{u}, \quad s \geq 1
$$

# 2.3. Random deception attacks 

In many practical situations, a crucial issue that cannot be ignored in the study of the estimation problem is the possible occurrence of cyber-attacks. In particular, deception attacks constitute a significant threat that attempts to compromise data integrity by maliciously and randomly falsifying information. In this type of attacks, the signal injected by the attacker, $\breve{\boldsymbol{z}}_{k}$, aims to neutralise the actual measurement, $\boldsymbol{z}_{k}$, and replace it with a deceptive noise, $\boldsymbol{w}_{k}$. Specifically,

$$
\breve{\mathbf{z}}_{k}=-\mathbf{z}_{k}+\mathbf{w}_{k}, \quad k \geq 1
$$

where
$\left(\mathbf{H}_{6}\right)$ The noise process $\left\{\mathbf{w}_{k}\right\}_{k \geq 1}$ is a zero-mean white sequence with known covariance function $\boldsymbol{\Sigma}_{k}^{w}=\operatorname{Cov}\left[\mathbf{w}_{k}\right], k \geq 1$.

To describe the fact that, in practice, cyber-attacks are often unpredictable and random, a sequence of Bernoulli random variables is adopted. More specifically, the following model with stochastic deception attacks is considered to describe the measurements processed for the estimation:

$$
\mathbf{y}_{k}=\mathbf{z}_{k}+\lambda_{k} \breve{\mathbf{z}}_{k}, \quad k \geq 1
$$

which can be equivalently rewritten as

$$
\mathbf{y}_{k}=\left(1-\lambda_{k}\right) \mathbf{z}_{k}+\lambda_{k} \mathbf{w}_{k}, \quad k \geq 1
$$

where



(H7) $\left\{\lambda_{k}\right\}_{k \geq 1}$ is a sequence of independent Bernoulli random variables with known mean function $\lambda_{k}=\mathbb{E}\left[\lambda_{k}\right], k \geq 1$.

Remark 4. The binary values of $\lambda_{k}$ indicate if the adversary actually launch the attack $\left(\lambda_{k}=\right.$ $1)$ or not $\left(\lambda_{k}=0\right)$. When the actual measurement is attacked, $y_{k}=w_{k}$ and only noise will be processed. Otherwise, if no attack is injected, $y_{k}=z_{k}$ and the actual measurement is processed for the estimation.

Finally, the following independence hypotheses on the processes involved in the considered model is required to address the estimation problem.
(H8) The signal process $\left\{x_{k}\right\}_{k \geq 1}$ and the processes $\left\{\gamma_{k}\right\}_{k \geq 1},\left\{v_{k}\right\}_{k \geq 1},\left\{w_{k}\right\}_{k \geq 1}$ and $\left\{\lambda_{k}\right\}_{k \geq 1}$ are mutually independent.

# 2.4. Linearized observations 

Under hypotheses (H1)-(H8), our goal is to obtain recursive algorithms for the filtering and fixed-point smoothing problems; that is, to address the estimation problem of the signal $x_{k}$ given the nonlinear observations $\left\{y_{1}, \ldots, y_{L}\right\}, L \geq k$. To this end, we will use a similar reasoning to that used to derive the extended Kalman filter. The problem is thus reduced to linearizing the observation equation (1) and then inserting such linearized observations into (3) to calculate the LS linear estimator of the signal from the resulting measurements.

More precisely, from hypothesis (H3), assuming knowledge of a nominal trajectory of the signal, $\left\{x_{k}^{0}\right\}_{k \geq 1}$, the function $h_{k}$ can be expanded in Taylor series about $x_{k}^{0}$ :

$$
h_{k}(x)=h_{k}\left(x_{k}^{0}\right)+\left.\frac{\partial h_{k}(x)}{\partial x}\right|_{x=x_{k}^{0}}\left(x-x_{k}^{0}\right)+\cdots, k \geq 1
$$

Neglecting the terms of order greater than one in this Taylor expansion, equation (1) can be approximated by the following linearized observation equation

$$
z_{k}=\gamma_{k}\left(H_{k} x_{k}+C_{k}\right)+v_{k}, k \geq 1
$$

where

$$
H_{k}=\left.\frac{\partial h_{k}(x)}{\partial x}\right|_{x=x_{k}^{0}}, \quad C_{k}=h_{k}\left(x_{k}^{0}\right)-H_{k} x_{k}^{0}
$$

The above equation is a linear equation affected by the binary multiplicative noise, $\left\{\gamma_{k}\right\}_{k \geq 1}$, and the time-correlated additive noise, $\left\{v_{k}\right\}_{k \geq 1}$. Our aim is to derive recursive estimation algorithms by using the linear approximation (4) in the equation for the available observations (3).

## 3. Main results

### 3.1. Problem statement and innovation approach

Our goal is to obtain recursive algorithms for the LS linear filter and fixed-point smoother of the signal $x_{k}$ from the available observations (3), based on the linearized measurements



(4). For this purpose, we will use an innovation approach. According to this approach, the observation process is transformed into an equivalent innovation process and the LS linear estimator, $\widehat{\zeta}_{k / L}$, of a random vector $\boldsymbol{\zeta}_{k}$ based on a set of observations $\left\{\mathbf{y}_{j}, 1 \leq j \leq L\right\}$, can be expressed as a linear combination of the innovations as follows:

$$
\widehat{\boldsymbol{\zeta}}_{k / L}=\sum_{j=1}^{L} S_{k, j}^{\zeta}\left(\boldsymbol{\Sigma}_{j}^{\boldsymbol{\eta}}\right)^{-1} \boldsymbol{\eta}_{j, k}, L \geq 1
$$

where $\mathbf{S}_{k, j}^{\zeta}=\mathbb{E}\left[\boldsymbol{\zeta}_{k} \boldsymbol{\eta}_{j}^{\mathrm{T}}\right], \boldsymbol{\eta}_{j}=\mathbf{y}_{j}-\widehat{\mathbf{y}}_{j / j-1}$ is the innovation at time $j$ and $\boldsymbol{\Sigma}_{j}^{\boldsymbol{\eta}}=\operatorname{Cov}\left[\boldsymbol{\eta}_{j}\right]$. Using (3) and the model hypotheses, the innovation can be written as

$$
\boldsymbol{\eta}_{k}=\mathbf{y}_{k}-\left(1-\lambda_{k}\right) \widehat{\mathbf{z}}_{k / k-1}, k \geq 1
$$

and, from the linear approximation (4), it is clear that the prediction estimator of $\mathbf{z}_{k}$ can be approximated by

$$
\widehat{\mathbf{z}}_{k / k-1}=\boldsymbol{\gamma}_{k}\left(\mathbf{H}_{k} \widehat{\mathbf{x}}_{k / k-1}+\mathbf{C}_{k}\right)+\widehat{\mathbf{v}}_{k / k-1}
$$

Expressions (5)-(7) are the key points for the derivation of the recursive filtering and fixedpoint smoothing algorithms that will be presented in the following subsections.

# 3.2. Recursive filtering algorithm 

For the sake of convenience, we introduce the following notations:

$$
\Gamma_{k}^{a}= \begin{cases}\boldsymbol{\gamma}_{k} \mathbf{H}_{k} \mathbf{B}_{k}, & a=x \\ \mathbf{F}_{k}, & a=v\end{cases}
$$

Theorem 3.1. Consider the observation model (1)-(3), where the processes involved satisfy hypotheses (H1)-(H8). Then, the innovation $\boldsymbol{\eta}_{k}$ is calculated as

$$
\boldsymbol{\eta}_{k}=\mathbf{y}_{k}-\left(1-\lambda_{k}\right)\left(\Delta_{k}^{x} \mathbf{e}_{k-1}^{x}+\Delta_{k}^{v} \mathbf{e}_{k-1}^{v}+\boldsymbol{\gamma}_{k} \mathbf{C}_{k}\right), k \geq 1
$$

and its covariance matrix $\boldsymbol{\Sigma}_{k}^{\boldsymbol{\eta}}$ satisfies

$$
\begin{aligned}
\boldsymbol{\Sigma}_{k}^{\boldsymbol{\eta}}= & \boldsymbol{\Sigma}_{k}^{\mathbf{y}}-\left(1-\lambda_{k}\right)^{2}\left[\left(\Delta_{k}^{x} \mathbf{T}_{k}^{x x}+\Delta_{k}^{v} \mathbf{T}_{k}^{v x}\right)\left(\Delta_{k}^{x}\right)^{\mathrm{T}}\right. \\
& \left.+\left(\Delta_{k}^{x} \mathbf{T}_{k}^{x v}+\Delta_{k}^{v} \mathbf{T}_{k}^{v v}\right)\left(\Delta_{k}^{v}\right)^{\mathrm{T}}+\gamma_{k}^{2} \mathbf{C}_{k} \mathbf{C}_{k}^{\mathrm{T}}\right], k \geq 1
\end{aligned}
$$

with

$$
\begin{aligned}
\boldsymbol{\Sigma}_{k}^{\mathbf{y}} & =\left(1-\lambda_{k}\right) \boldsymbol{\Sigma}_{k}^{\mathbf{z}}+\lambda_{k} \boldsymbol{\Sigma}_{k}^{\mathbf{w}}, \quad k \geq 1 \\
\boldsymbol{\Sigma}_{k}^{\mathbf{z}} & =\gamma_{k}\left(\mathbf{H}_{k} \mathbf{A}_{k} \mathbf{B}_{k}^{\mathrm{T}} \mathbf{H}_{k}^{\mathrm{T}}+\mathbf{C}_{k} \mathbf{C}_{k}^{\mathrm{T}}\right)+\mathbf{E}_{k} \mathbf{F}_{k}^{\mathrm{T}}, \quad k \geq 1
\end{aligned}
$$



The vectors $\mathbf{e}_{k}^{a}(\mathrm{a}=\mathrm{x}, \mathrm{v})$ are recursively obtained by

$$
\mathbf{e}_{k}^{a}=\mathbf{e}_{k-1}^{a}+\Psi_{k}^{a}\left(\Sigma_{k}^{\eta}\right)^{-1} \boldsymbol{\eta}_{k}, k \geq 1 ; \mathbf{e}_{0}^{a}=\mathbf{0}
$$

where

$$
\Psi_{k}^{a}=\left(1-\lambda_{k}\right)\left(\boldsymbol{\Gamma}_{k}^{a}-\Delta_{k}^{x} \mathbf{T}_{k} \mathbf{x}_{k-1}^{a}-\Delta_{k}^{v} \mathbf{T}_{k} \mathbf{v}_{k-1}^{a}\right)^{T}, k \geq 1
$$

The matrices $\mathbf{T}_{k}^{a b}=\mathrm{E}\left[\mathbf{e}_{k}^{a}\left(\mathbf{e}_{k}^{b}\right)^{T}\right](a, b=\mathrm{x}, \mathrm{v})$ are also recursively calculated by

$$
\mathbf{T}_{k}^{a b}=\mathbf{T}_{k-1}^{a b}+\Psi_{k}^{a}\left(\Sigma_{k}^{\eta}\right)^{-1}\left(\Psi_{k}^{b}\right)^{T}, k \geq 1 ; \mathbf{T}_{0}^{a b}=\mathbf{0}
$$

The filtering estimator of the signal, $\widehat{\mathbf{x}}_{k} / k$, is then computed by

$$
\widehat{\mathbf{x}}_{k}=A_{k} \mathbf{e}_{k}^{\mathrm{x}}, k \geq 1
$$

Proof. According to (5), the estimator of the signal $\mathbf{x}_{k}$ based on a set of observations $\left\{\mathbf{y}_{1}, \ldots, \mathbf{y}_{L}\right\}$, with $L \leq k$, is given by

$$
\widehat{\mathbf{x}}_{k / L}=\sum_{j=1}^{L} S_{k, j}^{\mathbf{x}}\left(\Sigma_{j}^{\eta}\right)^{-1} \boldsymbol{\eta}_{j}, L \leq k
$$

where $S_{k, j}^{\mathbf{x}}=\mathrm{E}\left[\mathbf{x}_{k} \boldsymbol{\eta}_{j}^{T}\right]$. From (6), it is clear that

$$
S_{k, j}^{\mathbf{x}}=\mathrm{E}\left[\mathbf{x}_{k} \mathbf{y}_{j}^{T}\right]-\left(1-\lambda_{j}\right) \mathrm{E}\left[\mathbf{x}_{k} \widehat{\mathbf{z}}_{j-1}^{T} / j^{-1}\right]
$$

Using (3) and (4), and taking into account hypotheses (H1) and (H8), we have

$$
\mathrm{E}\left[\mathbf{x}_{k} \mathbf{y}_{j}^{T}\right]=\left(1-\lambda_{j}\right) \gamma_{j} A_{k} \mathbf{B}_{j}^{T} \mathbf{H}_{j}^{T}, 1 \leq j \leq k
$$

and, from (7), the following expression is deduced

$$
\mathrm{E}\left[\mathbf{x}_{k} \widehat{\mathbf{z}}_{j-1}^{T} / j^{-1}\right]=\gamma_{j} \mathrm{E}\left[\mathbf{x}_{k} \widehat{\mathbf{x}}_{j-1}^{T} / j^{-1}\right] \mathbf{H}_{j}^{T}+\mathrm{E}\left[\mathbf{x}_{k} \widehat{\mathbf{v}}_{j-1}^{T} / j^{-1}\right], 1 \leq j \leq k
$$

Using again the general expression (5) for the estimators $\widehat{\mathbf{x}}_{j / j-1}^{T}$ and $\widehat{\mathbf{v}}_{j / j-1}^{T}$, we can write

$$
\mathrm{E}\left[\mathbf{x}_{k} \widehat{\mathbf{a}}_{j / j-1}^{T}\right]=\sum_{i=1}^{j-1} S_{k, i}^{\mathbf{x}}\left(\Sigma_{i}^{\eta}\right)^{-1}\left(\mathbf{S}_{j, i}^{a}\right)^{T}, \quad j \geq 2, a=x, v
$$

Consequently, $S_{k, j}^{\mathbf{x}}$ admits the following expression

$$
S_{k, j}^{\mathbf{x}}=\left(1-\lambda_{j}\right)\left[\gamma_{j} A_{k} \mathbf{B}_{j}^{T} \mathbf{H}_{j}^{T}-\left(1-\delta_{j, 1}\right) \sum_{i=1}^{j-1} S_{k, i}^{\mathbf{x}}\left(\Sigma_{i}^{\eta}\right)^{-1}\left(\gamma_{j} \mathbf{H}_{j} S_{j, i}^{\mathbf{x}}+\mathbf{S}_{j, i}^{\mathbf{v}}\right)^{T}\right], \quad j \geq 1
$$

from which the following factorization is easily deduced:

$$
S_{k, j}^{\mathbf{x}}=A_{k} \Psi_{j}^{\mathbf{x}}, \quad j \leq k
$$



just defining

$$
\Psi_{j}^{x}=\left(1-\lambda_{j}\right)\left[\gamma_{j} B_{j}^{T} H_{j}^{T}-\left(1-\delta_{j, 1}\right) \sum_{i=1}^{j-1} \Psi_{i}^{x}\left(\Sigma_{i}^{\eta}\right)^{-1}\left(\gamma_{j} H_{j} A_{j} \Psi_{i}^{x}+S_{j, i}^{v}\right)^{T}\right], \quad j \geq 1
$$

Similarly, the following identity is derived

$$
S_{k, j}^{v}=E_{k} \Psi_{j}^{v}, \quad j \leq k
$$

with

$$
\Psi_{j}^{v}=\left(1-\lambda_{j}\right)\left[F_{j}^{T}-\left(1-\delta_{j, 1}\right) \sum_{i=1}^{j-1} \Psi_{i}^{v}\left(\Sigma_{i}^{\eta}\right)^{-1}\left(\gamma_{j} H_{j} A_{j} \Psi_{i}^{x}+E_{j} \Psi_{i}^{v}\right)^{T}\right], \quad j \geq 1
$$

Thus, defining the following vectors:

$$
e_{k}^{a}=\sum_{j=1}^{k} \Psi_{j}^{a}\left(\Sigma_{j}^{\eta}\right)^{-1} \eta_{j}, \quad k \geq 1, a=x, v
$$

and using (17) and (19), we have that

$$
\hat{x}_{k} / k=A_{k} e_{k}^{x}, \quad \hat{x}_{k} / k-1=A_{k} e_{k-1}^{x}, \quad \hat{v}_{k} / k-1=E_{k} e_{k-1}^{v}, \quad k \geq 1
$$

Substituting these expressions for $\widehat{x}_{k} / k-1$ and $\widehat{v}_{k} / k-1$ in (7) and taking into account the definition of $\Delta_{k}^{a}(a=x, v)$ given in (9) we have that

$$
\widehat{z}_{k} / k-1=\Delta_{k}^{x} e_{k-1}^{x}+\Delta_{k}^{v} e_{k-1}^{v}+\gamma_{k} C_{k}, k \geq 1
$$

So, using (6), expression (10) for the innovation is straightforward.
In order to obtain the innovation covariance matrix, $\Sigma_{k}^{\eta}=E\left[\eta_{k} \eta_{k}^{T}\right]$, we use (6) and the OPL to deduce that

$$
\Sigma_{k}^{\eta}=\Sigma_{k}^{y}-\left(1-\lambda_{k}\right)^{2} E\left[\widehat{z}_{k} / k-1 \widehat{z}_{k} / k-1^{T}\right], k \geq 1
$$

Defining $T_{k}^{a b}=E\left[e_{k}^{a}\left(e_{k}^{b}\right)^{T}\right], k \geq 1(a, b=x, v)$, and using (23), we can write

$$
\begin{aligned}
E & {\left[\widehat{z}_{k} / k-1 \widehat{z}_{k} / k-1^{T}\right]=} \\
& \Delta_{k}^{x} T_{k-1}^{x x}\left(\Delta_{k}^{x}\right)^{T}+\Delta_{k}^{x} T_{k-1}^{x v}\left(\Delta_{k}^{v}\right)^{T} \\
& +\Delta_{k}^{v} T_{k-1}^{v x}\left(\Delta_{k}^{x}\right)^{T}+\Delta_{k}^{v} T_{k-1}^{v v}\left(\Delta_{k}^{v}\right)^{T}+\gamma_{k}^{2} C_{k} C_{k}^{T}
\end{aligned}
$$

and expression (11) for the innovation covariance matrix is immediately obtained. The formulas for $\Sigma_{k}^{y}$ and $\Sigma_{k}^{z}$ given in (12) are easily derived from the model hypotheses.

Using (21), the recursion (13) is directly obtained and, also, the following expression for $T_{k}^{a b}$ is straightforward:

$$
T_{k}^{a b}=\sum_{j=1}^{k} \Psi_{j}^{a}\left(\Sigma_{j}^{\eta}\right)^{-1}\left(\Psi_{j}^{b}\right)^{T}, \quad k \geq 1
$$



which, together with the definitions (8) and (9), leads to expression (14) just by substitution in (18) and (20). Also, from the above expression, the recursion (15) is immediately obtained. Finally, the filter expression (16) has been already obtained in (22), so the proof is complete.

Remark 5. The derivation of the estimation algorithm presented in Theorem 3.1 is based on the linear approximation (4) of the nonlinear observations around a nominal trajectory of the signal. Hence, the first question that arises is what to do if we do not have a reliable nominal signal trajectory. In such cases, we can follow an EKF approach; in other words, we can use the prediction estimates $\left\{\widehat{\mathbf{x}}^{k / k-1}\right\}_{k \geq 1}$ as a nominal trajectory of the signal, because $\widehat{\mathbf{x}}^{k / k-1}$ is our best approximation of $\mathbf{x}^{k}$ before the observation at time $k$ is considered. When doing so, the matrices $\mathbf{H}^{k}$ and $\mathbf{C}^{k}$ in equation (4) are given by

$$
\mathbf{H}^{k}=\left.\frac{\partial h^{k}(\mathbf{x})}{\partial \mathbf{x}}\right|_{\mathbf{x}=\mathbf{A}_{k} \mathbf{e}_{k-1}^{x}}, \quad \mathbf{C}^{k}=h^{k}\left(\mathbf{A}_{k} \mathbf{e}_{k-1}^{x}\right)-\mathbf{H}^{k} \mathbf{A}_{k} \mathbf{e}_{k-1}^{x}
$$

since the prediction estimate at time $k$ is calculated as $\widehat{\mathbf{x}}^{k / k-1}=\mathbf{A}_{k} \mathbf{e}_{k-1}^{x}$ (see (22)). Substituting these matrices in (7) and taking into account that $\widehat{\mathbf{v}}^{k / k-1}=E_{k} \mathbf{e}_{k-1}^{\mathbf{v}}$ (see (22)), we obtain that

$$
\widehat{\mathbf{z}}^{k / k-1}=\gamma^{k} h^{k}\left(\mathbf{A}_{k} \mathbf{e}_{k-1}^{x}\right)+E_{k} \mathbf{e}_{k-1}^{\mathbf{v}}, k \geq 1
$$

from which expression (10) for the innovation admits the following simplified form:

$$
\eta^{k}=y^{k}-\left(1-\lambda^{k}\right)\left(\gamma^{k} h^{k}\left(\mathbf{A}_{k} \mathbf{e}_{k-1}^{x}\right)+E_{k} \mathbf{e}_{k-1}^{\mathbf{v}}\right), k \geq 1
$$

and the innovation covariance matrix, $\boldsymbol{\Sigma}_{k}^{\boldsymbol{\eta}}$, can be written as

$$
\boldsymbol{\Sigma}_{k}^{\boldsymbol{\eta}}=\left(1-\lambda^{k}\right) \boldsymbol{\Sigma}_{k / k-1}^{\widetilde{\mathbf{z}}}+\lambda^{k}\left(1-\lambda^{k}\right) \widehat{\mathbf{z}}^{k / k-1} \widehat{\mathbf{z}}_{k / k-1}^{T}+\lambda^{k} \boldsymbol{\Sigma}_{k}^{\mathbf{w}}, k \geq 1
$$

whith

$$
\begin{array}{r}
\boldsymbol{\Sigma}_{k / k-1}^{\widetilde{\mathbf{z}}}=\gamma^{k} \mathbf{H}^{k} \boldsymbol{\Sigma}_{k / k-1}^{\widetilde{\mathbf{x}}} \mathbf{H}_{k}^{T}+\gamma^{k}\left(1-\gamma^{k}\right) h^{k}\left(\mathbf{A}_{k} \mathbf{e}_{k-1}^{x}\right) \mathbf{h}_{k}^{T}\left(\mathbf{A}_{k} \mathbf{e}_{k-1}^{x}\right) \\
+\boldsymbol{\Sigma}_{k / k-1}^{\widetilde{\mathbf{v}}}, k \geq 1, \\
\boldsymbol{\Sigma}_{k / k-1}^{\widetilde{\mathbf{x}}}=\mathbf{A}_{k} \mathbf{B}_{k}^{T}-\mathbf{A}_{k}^{T} \mathbf{X}_{k-1}^{x} \mathbf{A}_{k}^{T}, k \geq 1, \\
\boldsymbol{\Sigma}_{k / k-1}^{\widetilde{\mathbf{v}}}=\mathbf{E}_{k} \mathbf{F}_{k}^{T}-\mathbf{E}_{k}^{T} \mathbf{V}_{k-1}^{v} \mathbf{E}_{k}^{T}, k \geq 1 .
\end{array}
$$

The following steps summarize the filtering algorithm and its computational procedure when the prediction estimates, $\widehat{\mathbf{x}}^{k / k-1}=\mathbf{A}_{k} \mathbf{e}_{k-1}^{x}$, are used as a nominal trajectory of the signal.

# Filtering algorithm using $\mathbf{x}_{k}^{0}=\mathbf{A}_{k} \mathbf{e}_{k-1}^{x}$ as a nominal trajectory of the signal 

Step 1. Set $k=1$ and initialize the algorithm with $\mathbf{e}_{0}^{a}=\mathbf{0}$ and $T_{0}^{a b}=\mathbf{0}(a, b=x, v)$.
Step 2. Compute $\mathbf{H}^{k}=\left.\frac{\partial h^{k}(\mathbf{x})}{\partial \mathbf{x}}\right|_{\mathbf{x}=\mathbf{A}_{k} \mathbf{e}_{k-1}^{x}}$ and, from it, compute $\Gamma_{k}^{a}$ and $\Delta_{k}^{a}(a=x, v)$ by (8) and (9), respectively.

Step 3. Compute $\Psi_{k}^{a}(a=x, v)$ by (14).
Step 4. Compute $\widehat{\mathbf{z}}^{k / k-1}$ by (25) and, from it, compute the innovation $\boldsymbol{\eta}^{k}$ by (26).
Step 5. Compute the matrices $\boldsymbol{\Sigma}_{k / k-1}^{\tilde{\mathbf{z}}}$ by (28) and, from them, compute the innovation covariance matrix $\boldsymbol{\Sigma}_{k}^{\boldsymbol{\eta}}$ by (27).



Step 6. Compute $e_{k}^{a}(a=x, v)$ by (13) and $T_{k}^{a b}(a, b=x, v)$ by (15).
Step 7. Compute the filter, $\widehat{x}_{k / k}$, by (16).
Step 8. Set $k=k+1$ and return to Step 2.

# 3.3. Recursive fixed-point smoothing algorithm 

The following algorithm allows us to update the filter at any time $k$ as the measurements keep rolling in. More precisely, it allows us to obtain the fixed-point smoothing estimators $\widehat{x}_{k / k+1}, \widehat{x}_{k / k+2}, \ldots$
Theorem 3.2. Starting from the filter, $\widehat{x}_{k / k}$, at a fixed sampling time $k \geq 1$, the fixed-point smoothers, $\widehat{x}_{k / L}, L>k$, satisfy the following recursion:

$$
\widehat{x}_{k / L}=\widehat{x}_{k / L-1}+S_{k, L}^{x}\left(\Sigma_{L}^{\eta}\right)^{-1} \eta_{L}, \quad L>k
$$

with

$$
S_{k, L}^{x}=\left(1-\lambda_{L}\right)\left[\left(B_{k}-M_{k, L}^{x}\right)\left(\Delta_{L}^{x}\right)^{T}-M_{k, L}^{v}\left(\Delta_{L}^{v}\right)^{T}\right], \quad L>k
$$

The matrices $M_{k, L}^{a}=E\left[x_{k}\left(e_{L}^{a}\right)^{T}\right], a=x, v$ are recursively calculated by

$$
M_{k, L}^{a}=M_{k, L-1}^{a}+S_{k, L}^{x}\left(\Sigma_{L}^{\eta}\right)^{-1}\left(\Psi_{L}^{a}\right)^{T}, L>k ; \quad M_{k, k}^{a}=A_{k}^{T} x_{k}^{a}
$$

Proof. The recursion (29) is immediately deduced from (5), so we must find an expression for $S_{k, L}^{x}=E\left[x_{k} \eta_{L}^{T}\right], L>k$. A similar reasoning to that used to obtain $S_{k, j}^{x}(j \leq k)$ in Theorem 3.1 yields

$$
S_{k, L}^{x}=\left(1-\lambda_{L}\right)\left[\gamma_{L} B_{k} A_{L}^{T} H_{L}^{T}-\sum_{i=1}^{L-1} S_{k, i}^{x}\left(\Sigma_{i}^{\eta}\right)^{-1}\left(\gamma_{L} H_{L} S_{L, i}^{x}+S_{L, i}^{v}\right)^{T}\right], \quad L>k
$$

Taking into account that, from (17) and (19), $S_{L, i}^{x}=A_{L} \Psi_{i}^{x}$ and $S_{L, i}^{v}=E_{L} \Psi_{i}^{v}$, respectively, and using (9), the above expression can be rewritten as

$$
S_{k, L}^{x}=\left(1-\lambda_{L}\right)\left[B_{k}\left(\Delta_{L}^{x}\right)^{T}-\sum_{i=1}^{L-1} S_{k, i}^{x}\left(\Sigma_{i}^{\eta}\right)^{-1}\left(\Delta_{L}^{x} \Psi_{i}^{x}+\Delta_{L}^{v} \Psi_{i}^{v}\right)^{T}\right], \quad L>k
$$

Then, defining $M_{k, L}^{a}=E\left[x_{k}\left(e_{L}^{a}\right)^{T}\right]$ and using (21), we have that

$$
M_{k, L}^{a}=\sum_{i=1}^{L} S_{k, i}^{x}\left(\Sigma_{i}^{\eta}\right)^{-1}\left(\Psi_{i}^{a}\right)^{T}, a=x, v
$$

from which the formula (30) for $S_{k, L}^{x}$ is straightforward and also the recursion (31) is immediately deduced. Its initial condition is derived just using that, for $i \leq k, S_{k, i}^{x}=A_{k} \Psi_{i}^{x}$ and taking into account expression (24). The proof is then complete.



# 4. Numerical simulation example 

In this section, a simple numerical simulation example concerning the phase modulation of analogue communication systems is presented with a dual purpose: on the one hand, to illustrate the implementation and performance of the proposed filtering and fixed-point smoothing algorithms and, on the other hand, to analyze the effect of missing measurements and deception attacks on the estimation accuracy.

Scalar signal process: $\mathrm{AR}(2)$ model. Consider that the modulating signal $\left\{x_{k}\right\}_{k \geq 1}$ is a stationary stochastic process with autocovariance function

$$
\Sigma_{k, s}^{x}=Q_{1} \beta_{1}^{k-s}+Q_{2} \beta_{2}^{k-s}, \quad k, s \geq 1
$$

where, for $b_{1}=0.1, b_{2}=-0.5$ and $\sigma^{2}=0.25$, the values of $\beta_{i}$ and $Q_{i}, i=1,2$, are given by:

$$
\begin{aligned}
\beta_{1}, \beta_{2} & =\frac{-b_{1} \pm \sqrt{b_{1}^{2}-4 b_{2}^{2}}}{2} \\
Q_{1} & =\frac{\sigma^{2} \beta_{1}\left(\beta_{2}^{2}-1\right)}{\left(\beta_{2}-\beta_{1}\right)\left(\beta_{1} \beta_{2}+1\right)} \\
Q_{2} & =-\frac{\sigma^{2} \beta_{2}\left(\beta_{1}^{2}-1\right)}{\left(\beta_{2}-\beta_{1}\right)\left(\beta_{1} \beta_{2}+1\right)}
\end{aligned}
$$

According to hypothesis (H1), this autocovariance function can be expressed in a separable form defining, for example, $\mathbf{A}_{k}=\left[Q_{1} \beta_{1}^{k} Q_{2} \beta_{2}^{k}\right]$ and $\mathbf{B}_{k}=\left[\beta_{1}^{-k} \beta_{2}^{-k}\right]^{\top}$.

For simulation purposes, the signal is assumed to be generated from the following secondorder autoregressive model:

$$
\begin{aligned}
& x_{k}=-b_{1} x_{k-1}-b_{2} x_{k-2}+\varepsilon_{k}, k \geq 3 \\
& x_{2}=-b_{1} x_{1}+\varepsilon_{2} \\
& x_{1}=\varepsilon_{1}
\end{aligned}
$$

where $\left\{\varepsilon_{k}\right\}_{k \geq 1}$ is a zero-mean white Gaussian noise with variance $\Sigma_{k}^{\varepsilon}=\sigma^{2}, \forall k$.
Uncertain measurements of the carrier signal. Consider the following scalar carrier signal:

$$
h_{k}\left(x_{k}\right)=\cos \left(2 \pi f_{p} k \Delta+m_{A} x_{k}\right), k \geq 1
$$

where $f_{p}=10[\mathrm{~Hz}]$ is the carrier frequency, $\Delta=0.01$ is the sampling period of the modulating signal $x_{k}$ and $m_{A}=2$ represents the phase sensitivity. Clearly, if we use the prediction estimates as a nominal trajectory of the signal, the functions $H_{k}$ in equation (4) are

$$
H_{k}=-m_{A} \sin \left(2 \pi f_{p} k \Delta+m_{A} \mathcal{A}_{k e_{k}^{x}}\right), k \geq 1
$$

According to the theoretical model, let us suppose that the measurements of the carrier signal $h_{k}\left(x_{k}\right)$ are given by (1), where:

- $\left\{\gamma_{k}\right\}_{k \geq 1}$ is a sequence of independent Bernoulli random variables with probabilities $\mathbb{P}\left(\gamma_{k}=1\right)=\mathbb{E}\left[\gamma_{k}\right]=\gamma, k \geq 1$.
- The noise process $\left\{v_{k}\right\}_{k \geq 0}$ is generated by (2), where $D_{k}=0.75,\left\{u_{k}\right\}_{k \geq 0}$ is a zeromean white Gaussian noise with $\Sigma_{k}^{u}=0.01, \forall k \geq 0$, and $v_{0}$ is a zero-mean Gaussian variable with $\Sigma_{0}^{v}=0.1$.
Random deception attacks. Finally, also according to the theoretical model, let us suppose that the measurements are subject to deception attacks and the observations available for the estimation, $y_{k}$, are given by (3), where:



- The noise of the false data injection attacks $\left\{w_{k}\right\}_{k \geq 1}$ is a standard Gaussian white process.
- The status of the attacks is described by a white sequence of Bernoulli random variables $\left\{\lambda_{k}\right\}_{k \geq 1}$, with probabilities $P\left(\lambda_{k}=1\right)=\mathcal{E}\left[\lambda_{k}\right]=\lambda, k \geq 1$.

Under these conditions, using the proposed filtering and smoothing algorithms, the phase demodulation problem is considered. This problem consists of estimating the signal $x_{k}$ from the observed values $y_{k}$ and, for this purpose, we have implemented a MATLAB program that simulates the values of the signal, $x_{k}$, the uncertain measurements, $z_{k}$, and the available ones, $y_{k}$, considering different probabilities $\gamma$ and $\lambda$, and provides the filtering and fixed-point smoothing estimates of $x_{k}$ obtained from theorems 1 and 2, respectively.
Considering one thousand independent simulations, each with fifty iterations of the algorithms, in order to quantify the performance of the proposed estimators, we use the root mean square error (RMSE) criterion, which is widely used because it allows straightforward quantitative comparisons. Denoting $\left\{x_{k}^{(s)}\right\}_{k=1, \ldots, 50}$ the $s$-th set of the simulated data (which is taken as the $s$-th set of true values of the signal), and $\widehat{x}_{k / k+h}^{(s)}$ as the filtering $(h=0)$ and fixed-point smoothing $(h=2)$ estimates at time $k$ in the $s$-th simulation run, the RMSE at time $k$ is calculated by

$$
R M S E_{k}=\sqrt{\frac{1}{1000} \sum_{s=1}^{1000}\left(x_{k}^{(s)}-\widehat{x}_{k / k+h}^{(s)}\right)^{2}}, \quad 1 \leq k \leq 50, \quad h=0,2
$$

First, considering fixed probabilities $\gamma=0.7$ and $\lambda=0.3$, Figure 1 displays the values $R M S E_{k}$, for $k=1, \ldots, 50$, corresponding to the filtering $\left(\widehat{x}_{k / k}\right)$ and fixed-point smoothing $\left(\widehat{x}_{k / k+2}\right)$ estimates. From this figure, it can be seen that, at any time $k$, the $R M S E_{k}$ of the smoothing estimates is smaller than that of the filtering estimates; hence, according to the $R M S E_{k}$ criterion, the smoother outperforms the filter. Analogous results are obtained for other values of the probabilities $\gamma$ and $\lambda$.

In order to analyze the overall performance of the estimations provided by the filtering and smoothing algorithms as a function of the deception attack probability $\lambda$, Figure 2 shows the mean values of $R M S E_{k}$ corresponding to the 50 iterations, versus $\lambda=0.1$ to 0.9 , when $\gamma=0.7$ and 0.9. As expected, it is shown that the mean values of $R M S E_{k}$, for both filtering and smoothing estimates, become larger as the deception attack probability $\lambda$ increases, and this increase is less noticeable for high values of $\lambda$. Furthermore, this figure shows the superiority of the smoother over the filter and also that, for $\gamma=0.9$, the results of both estimators are better than those obtained for $\gamma=0.7$, and this improvement is more evident for values of $\lambda$ less than or equal to 0.5 .

Finally, to illustrate the influence of $\gamma$ (the probability that the observations contain the signal) on the performance of the estimators, Figure 3 shows the mean values of $R M S E_{k}$ corresponding to the 50 iterations, for a range of $\gamma$ values from 0.1 to 0.9 , when $\lambda=0.1$ and 0.3. For these values of $\lambda$, as expected, the mean values of $R M S E_{k}$, for both filtering and smoothing estimates, decrease as the probability $\gamma$ increases, meaning that better estimations are obtained as the probability that the signal is missing in the measurements, $1-\gamma$, decreases. Moreover, this improvement is more noticeable for high values of $\gamma$. This figure also shows the superiority of the smoother over the filter and that, for $\lambda=0.1$, the results of both estimators are better than those obtained for $\lambda=0.3$, being this improvement more significant for values of $\gamma$ greater than or equal to 0.5 .



# 5. Conclusions 

Recursive algorithms for the LS filtering and fixed-point smoothing problems from nonlinear observations perturbed by time-correlated additive noise and subject to random failures, causing that some measured outputs are only noise, have been proposed. The possibility of random deception attacks adds some complexity to the mathematical model considered. Using linear approximations of the actual observations, together with the projection theory and the innovation approach, the derivation of the estimation algorithms is based on the EKF approach. Some numerical results are used to examine the performance of the proposed estimators and to analyze the effect of missing measurement and deception attack success probabilities on the estimation accuracy.

Future research topics would include extending the proposed framework to deal with other nonlinear estimation approaches, such as unscented Kalman filtering, cubature Kalman filtering, particle filtering, Gaussian-Hermite filtering, divided differences filtering or Bayesian filtering. Another interesting further research direction would be considering nonlinear multisensor systems with different communication constraints (random delays, fading measurements and packet dropouts, among others) and different communication protocols (e.g., event triggering mechanisms, random communication protocol or round-robin protocol).

## Disclosure statement

The authors report there are no competing interests to declare.

## Data availability statement

Data sharing is not applicable to this article as no new data were created or analyzed in this study.

## Funding

Grant PID2021-124486NB-I00 funded by MCIN/AEI/ 10.13039/501100011033 and by "ERDF A way of making Europe".

## Notes on contributors

R. Caballero-Águila received the M.Sc. degree in Mathematics and Ph.D. degree in Polynomial Filtering in Systems with Uncertain Observations, both from the University of Granada (Spain), in 1997 and 1999, respectively. In 1997, she joined the University of Jaén (Spain), where she is currently a Professor with the Department of Statistics and Operations Research. Her current research interests include stochastic systems, filtering, prediction and smoothing.
Jun Hu received the B.Sc. degree in information and computing science and M.Sc. degree in Applied Mathematics from the Harbin University of Science and Technology, Harbin, China, in 2006 and 2009, respectively, and the Ph.D. degree in control science and engineering from the Harbin Institute of Technology, Harbin, in 2013. From 2010 to 2012, he was a Visiting Ph.D. Student with the Department of Information Systems and Computing, Brunel University, Uxbridge, U.K. From 2014 to 2016, he was an Alexander von Humboldt Research



Fellow with the University of Kaiserslautern, Kaiserslautern, Germany. From 2018 to 2021, he was a Research Fellow with the University of South Wales, U.K. He is currently with the Department of Applied Mathematics, Harbin University of Science and Technology, and also with the School of Automation, Harbin University of Science and Technology, Harbin. His research interests include nonlinear control, filtering and fault estimation, time-varying systems and complex networks.
J. Linares-Pérez received the M.Sc. degree in Mathematics and Ph.D. in Stochastic Differential Equations, both from the University of Granada (Spain) in 1980 and 1982, respectively. She is currently a Professor with the Department of Statistics and Operations Research, University of Granada (Spain). Her research interests are related with stochastic calculus and estimation in stochastic systems.

## References

Caballero-Águila R, Hu J, Linares-Pérez J. Two Compensation Strategies for Optimal Estimation in Sensor Networks with Random Matrices, Time-Correlated Noises, Deception Attacks and Packet Losses. Sensors 2022;22:8505. https://doi.org/10.3390/s22218505.
Caballero-Águila R, Linares-Pérez J. Distributed fusion filtering for uncertain systems with coupled noises, random delays and packet loss prediction compensation. Int J Syst Sci 2023a;54(2):371390. https://doi.org/10.1080/00207721.2022.2122905

Caballero-Águila R, Linares-Pérez J. Quadratic estimation for stochastic systems in the presence of random parameter matrices, time-correlated additive noise and deception attacks. J Frankl Inst 2023b;360:11141-11164. https://doi.org/10.1016/j.jfranklin.2023.08.033.
Cheng G, Ma M, Tan L, Song S. Gaussian estimation for non-linear stochastic uncertain systems with time-correlated additive noises and packet dropout compensations. IET Control Theory Appl 2022;16:600-614. http://dx.doi.org/10.1049/cth2.12252.

García-Ligero, MJ, Hermoso-Carazo, A, Linares-Pérez, J. Least-squares estimators for systems with stochastic sensor gain degradation, correlated measurement noises and delays in transmission modelled by Markov chains. Int J Syst Sci 2020; 51(4):731-745. https://doi.org/10.1080/00207721.2020.1737757
Han F, Dong H, Wang Z, Li G. Local design of distributed $\mathcal{H}_{\infty}$-consensus filtering over sensor networks under multiplicative noises and deception attacks. Int J Robust Nonlinear Control 2019;29:22962314. https://doi.org/10.1002/rnc. 4493.

Han F, Song Y, Zhang S, Li W. Local condition-based finite-horizon distributed $\mathcal{H}_{\infty}$-consensus filtering for random parameter system with event-triggering protocols. Neurocomputing 2017;219:221-231. https://doi.org/10.1016/j.neucom.2016.09.022.
Hu J, Hu Z, Caballero-Águila R, Chen C, Fan S, Yi X. Distributed resilient fusion filtering for nonlinear systems with multiple missing measurements via dynamic event-triggered mechanism. Inf Sci 2023a;637:118950. https://doi.org/10.1016/j.ins.2023.118950.
Hu Z, Hu J, Yang G. A survey on distributed filtering, estimation and fusion for nonlinear systems with communication constraints: new advances and prospects. Syst Sci Control Eng 2020;8(1):189-205. https://doi.org/10.1080/21642583.2020.1737846.
Hu J, Wang C, Caballero-Águila R, Liu H. Distributed optimal fusion filtering for singular systems with random transmission delays and packet dropout compensations. Commun Nonlinear Sci Numer Simul 2023b;119:107093. https://doi.org/10.1016/j.cnsns.2023.107093.
Hu J, Wang Z, Gao H. Nonlinear Stochastic Systems with Network-Induced Phenomena: Recursive Filtering and Sliding-Mode Design. Springer, 2015. http://dx.doi.org/10.1007/978-3-319-08711-5.
Krantz S, Parks HR. A Primer of Real Analytic Functions, 2nd ed., Birkhäuser, Boston, 2002.
Liu W. Optimal estimation for discrete-time linear systems in the presence of multiplicative and time-correlated additive measurement noises. IEEE Trans Signal Process 2015;63(17):4583-4593. https://doi.org/10.1109/TSP.2015.2447491.



Liu W, Shi P. Convergence of optimal linear estimator with multiplicative and timecorrelated additive measurement noises. IEEE Trans Autom Control 2019;64(5):2190-2197. https://doi.org/10.1109/TAC. 2018.2869467.
Ma J, Sun S. Optimal linear recursive estimators for stochastic uncertain systems with timecorrelated additive noises and packet dropout compensations. Signal Process 2020;176:107704. http://dx.doi.org/10.1016/j.sigpro.2020.107704.
Ma Y, Sun S. Distributed Optimal and Self-Tuning Filters Based on Compressed Data for Networked Stochastic Uncertain Systems with Deception Attacks. Sensors 2023;23:335. https://doi.org/10.3390/s23010335.
Ma L, Wang M. State estimation of nonlinear time-varying complex networks with time-varying sensor delay for unknown noise distributions. Commun Nonlinear Sci Numer Simul 2022;114:106594. https://doi.org/10.1016/j.cnsns.2022.106594.
Ma L, Wang Z, Chen Y, Yi X. Probability-guaranteed distributed secure estimation for nonlinear systems over sensor networks under deception attacks on innovations. IEEE Trans Signal Inf Proc Netw 2021;7:465-477. https://doi.org/10.1109/TSIPN.2021.3097217.
Mahmoud MS, Hamdan MM, Baroudi UA. Modeling and control of Cyber-Physical Systems subject to cyber attacks: A survey of recent advances and challenges. Neurocomputing 2019;338:101-115. https://doi.org/10.1016/j.neucom.2019.01.099.
Pang C, Sun S. Fusion Predictors for Multisensor Stochastic Uncertain Systems With Missing Measurements and Unknown Measurement Disturbances. IEEE Sens J 2015;15(8):4346-4354. https://doi.org/10.1109/JSEN.2015.2416511.
Qu F, Tian E, Zhao X. Chance-Constrained $H_{\infty}$ State Estimation for Recursive Neural Networks Under Deception Attacks and Energy Constraints: The Finite-Horizon Case. IEEE Trans Neural Netw Learn Syst 2023;34(9):6492-6503. https://doi.org/10.1109/TNNLS.2021.3137426.
Ran C, Deng Z. Robust fusion Kalman estimators for networked mixed uncertain systems with random one-step measurement delays, missing measurements, multiplicative noises and uncertain noise variances. Inf Sci 2020;534:27-52. https://doi.org/10.1016/j.ins.2020.04.044.
Sánchez HS, Rotondo D, Escobet T, Puig V, Quevedo J. Bibliographical review on cyber attacks from a control oriented perspective. Annu Rev Control 2019;48:103-128. https://doi.org/10.1016/j.arcontrol.2019.08.002.
Simon D. Optimal state estimation. John Wiley \& Sons, Inc., Hoboken, New Jersey, 2006.
Wang Z, Wang D, Shen B, Alsaadi FE. Centralized security-guaranteed filtering in multirate-sensor fusion under deception attacks. J Franklin Inst 2018;355:406-420. https://doi.org/10.1016/j.jfranklin.2017.11.010.
Wen T, Wen C, Roberts C, Cai B. Distributed filtering for a class of discretetime systems over wireless sensor networks. J Franklin Inst 2020;357:3038-3055. https://doi.org/10.1016/j.jfranklin.2020.02.005.
Xiao S, Han Q, Ge X, Zhang Y. Secure distributed finite-time filtering for positive systems over sensor networks under deception attacks. IEEE Trans Cybern 2020;50:1200-1228. https://doi.org/10.1109/tcyb.2019.2900478.
Yang W, Zhang Y, Chen G, Yang C, Shi L. Distributed filtering under false data injection attacks. Automatica 2019;102:34-44. https://doi.org/10.1016/j.automatica.2018.12.027.



