# A New Statistic for Testing Covariance Equality in High-Dimensional Gaussian Low-Rank Models 

R. BEISSON, Student Member, IEEE, P. VALLET, Member, IEEE, A. GIREMUS, Member, IEEE, G. GINOLHAC, Member, IEEE

Abstract-In this paper, we consider the problem of testing equality of the covariance matrices of $L$ complex Gaussian multivariate time series of dimension $M$. We study the special case where each of the $L$ covariance matrices is modeled as a rank $K$ perturbation of the identity matrix, corresponding to a signal plus noise model. A new test statistic based on the estimates of the eigenvalues of the different covariance matrices is proposed. In particular, we show that this statistic is consistent and with controlled type I error in the high-dimensional asymptotic regime where the sample sizes $N_{1}, \ldots, N_{L}$ of each time series and the dimension $M$ both converge to infinity at the same rate, while $K$ and $L$ are kept fixed. We also provide some simulations on synthetic and real data (SAR images) which demonstrate significant improvements over some classical methods such as the GLRT, or other alternative methods relevant for the highdimensional regime and the low-rank model.

## I. INTRODUCTION

D ETECTING changes in the behaviour of multivariate time series is a fundamental problem in many applications going from remote sensing [2], [3], [4], [5] and wireless communications [6] to finance [7], climatology [8] or genomics [9]. In several of those applications, a usual approach consists in modeling the changes using the distribution of the time series, and in particular through an evolution in the structure of the covariance matrix.
Consider the context of $M$-dimensional time series $\left(\mathbf{y}_{n, 1}\right)_{n \in \mathbb{Z}}, \ldots,\left(\mathbf{y}_{n, L}\right)_{n \in \mathbb{Z}}$, assumed mutually independent and such that for all $\ell \in\{1, \ldots, L\}$,

$$
\left(\mathbf{y}_{n, \ell}\right)_{n \in \mathbb{Z}} \stackrel{\text { i.i.d. }}{\sim} \mathcal{N}_{\mathbb{C}^{M}}\left(\mathbf{0}, \mathbf{R}_{\ell}\right)
$$

where $\mathcal{N}_{\mathbb{C}^{M}}\left(\mathbf{0}, \mathbf{R}_{\ell}\right)$ denotes the zero-mean complex normal distribution with covariance matrix $\mathbf{R}_{\ell}$. Detecting the changes in the distribution of $\left(\mathbf{y}_{n, \ell}\right)_{n \in \mathbb{Z}}$, for all $\ell \in\{1, \ldots, L\}$, can be formalized as the following binary hypothesis test dealing with the equality of the $L$ covariance matrices $\mathbf{R}_{1}, \ldots, \mathbf{R}_{L}$,

$$
\begin{aligned}
& H_{0}: \quad \mathbf{R}_{1}=\ldots=\mathbf{R}_{L} \\
& H_{1}: \quad \exists(i, j) \in\{1, \ldots, L\}^{2}: \mathbf{R}_{i} \neq \mathbf{R}_{j}
\end{aligned}
$$

Assume that for all $\ell \in\{1, \ldots, L\}, N_{\ell}$ observations $\mathbf{y}_{1, \ell}, \ldots, \mathbf{y}_{N_{\ell}, \ell}$ are available and let $N=N_{1}+\cdots+N_{L}$. A large class of test statistics widely encountered in the literature [3] involves, provided that $M<N_{1}, \ldots, N_{L}$, linear spectral statistics of the matrices $\hat{\mathbf{R}}_{\ell}^{-1} \hat{\mathbf{R}}$ of the form:

$$
S=\sum_{\ell=1}^{L} \frac{N_{\ell}}{N} \frac{1}{M} \sum_{k=1}^{M} \phi\left(\lambda_{k}\left(\hat{\mathbf{R}}_{\ell}^{-1} \hat{\mathbf{R}}\right)\right)
$$

where $\lambda_{k}\left(\hat{\mathbf{R}}_{\ell}^{-1} \hat{\mathbf{R}}\right)$, for all $k \in\{1, \ldots, M\}$, are the eigenvalues of the matrix $\hat{\mathbf{R}}_{\ell}^{-1} \hat{\mathbf{R}}$ with

$$
\hat{\mathbf{R}}_{\ell}:=\frac{1}{N_{\ell}} \sum_{n=1}^{N_{\ell}} \mathbf{y}_{n, \ell} \mathbf{y}_{n, \ell}^{*}
$$

denoting the sample covariance matrix (SCM) associated with $\mathbf{R}_{\ell}$ and

$$
\hat{\mathbf{R}}=\sum_{\ell=1}^{L} \frac{N_{\ell}}{N} \hat{\mathbf{R}}_{\ell}
$$

In (3), $\phi$ denotes some continuous function defined on $(0,+\infty)$. In particular, the Generalized Likelihood Ratio (GLR) [3] with $\phi(x)=\log (x)$ or the Nagao statistic with $\phi(x)=(x-1)^{2}$ are included in the class of statistics (3). The presence of a change in the covariance is decided by comparing (3) to a threshold $\epsilon$ chosen to guarantee a certain type I error and the null hypothesis $H_{0}$ is rejected if $S>\epsilon$. Moreover, the test statistics based on (3) have the key property that the distribution of $S$ under $H_{0}$ is independent of $\mathbf{R}_{1}=\ldots=\mathbf{R}_{L}$, which allows to control its type I error. However, in practice, the distribution of statistics of type (3) under $H_{0}$ is untractable and only known in a few special cases for finite $M, N_{1}, \ldots, N_{L}$ (e.g. for the GLR, see [10]). To circumvent this issue, approximations in the low-dimensional (or large sample size) regime in which $N_{1}, \ldots, N_{L} \rightarrow \infty$ while $M, L$ are fixed can be derived, see e.g. [11, Th. 10.8.4]. While the latter are meant to be used in practical scenarios where $N_{1}, \ldots, N_{L} \gg M$, they may not be reliable in contexts involving high-dimensional (large $M$ ) observations or moderate sample sizes $N_{1}, \ldots, N_{L}$. Indeed, in that highdimensional case, it is often more reasonable to assume that $M, N_{1}, \ldots, N_{L}$ are of the same order of magnitude in which case the predictions of the distribution of (3) under $H_{0}$ in the low-dimensional regime become irrelevant.
The context where $M, N_{1}, \ldots, N_{L}$ are of the same order of magnitude can be modeled more realistically by the highdimensional regime in which it is assumed that $M$ converges to infinity together with $N_{1}, \ldots, N_{L}$ such that $\frac{M}{N_{\ell}} \rightarrow c_{\ell}>0$, R. Beisson, P. Vallet and A. Giremus are with Laboratoire de l'Intégration du Matériau au Système (CNRS, Univ. Bordeaux, Bordeaux INP), 351 Cours de la Libération, 33400 Talence (France)
G. Ginolhac is with Laboratoire d'Informatique, Systèmes, Traitement de l'Information et de la Connaissance (Univ. Savoie/Mont-Blanc, Polytech Annecy), 5 chemin de Bellevue, 74940 Annecy (France)
This work was partially supported by Agence de l'Innovation de Défense and Région Nouvelle-Aquitaine. The material of this paper was partly presented in the conference paper [1].




---

while $L$ is kept fixed. In this non-standard regime, the asymptotic distribution of the statistic $S$ can be derived using random matrix theory techniques (see e.g. [12] for the case $L=2$ ). Moreover, in several applications involving highdimensional observations, the potential changes in the covariance $\mathbf{R}_{\ell}$ may only be carried by a low-rank component (see e.g. [13], [14], [15]). This is the case, e.g., in array processing when dealing with a large array of $M$ sensors and a small number $K$ of source signals compared to $M$ [15]. In that case, we have the model

$$
\mathbf{R}_{\ell}=\boldsymbol{\Gamma}_{\ell}+\sigma^{2} \mathbf{I}
$$

with $\boldsymbol{\Gamma}_{\ell}$ the covariance matrix of rank $K<M$ of a useful signal and $\sigma^{2} \mathbf{I}$ the covariance matrix of a spatially white additive noise. When the rank $K$ remains constant in the high-dimensional regime, the matrices $\mathbf{R}_{\ell}^{-1} \mathbf{R}_{\ell^{\prime}}$ are fixed rank perturbations of the identity. Using well-known results [16], [17] on the asymptotic spectral distribution of the Fisher type random matrices $\hat{\mathbf{R}}_{\ell}^{-1} \hat{\mathbf{R}}$, one can show under both $\mathcal{H}_{0}$ and $\mathcal{H}_{1}$ that

$$
S \longrightarrow \sum_{\ell=1}^{L} \frac{c}{c_{\ell}} \int_{x_{\ell}^{-}}^{x_{\ell}^{+}} \phi\left(\frac{c}{c_{\ell}}(1+x)\right) f_{\ell}(x) d x
$$

almost surely (a.s.) where $c=\left(c_{1}^{-1}+\ldots+c_{L}^{-1}\right)^{-1}$ and where $f_{\ell}$ is the so-called Wachter distribution given by

$$
f_{\ell}(x)=\left(\frac{1}{c_{\ell}}-1\right) \frac{\sqrt{\left(x-x_{\ell}^{-}\right)\left(x_{\ell}^{+}-x\right)}}{2 \pi x(1+x)} \mathbf{1}_{\left[x_{\ell}^{-}, x_{\ell}^{+}\right]}(x)
$$

with $x_{\ell}^{ \pm}=\frac{c_{\ell}-c}{c\left(1-c_{\ell}\right)^{2}}\left(1 \pm \sqrt{\frac{c_{\ell}+c c_{\ell}}{c_{\ell}-c}-\frac{c c_{\ell}^{2}}{c_{\ell}-c}}\right)^{2}$. Thus $S$ converges to the same limit under both hypotheses $\mathcal{H}_{0}$ and $\mathcal{H}_{1}$, which indicates that test statistics relying on (3) might not be relevant in the high-dimensional regime and for the low-rank model in (6).

So far from our knowledge, the problem of covariance equality testing under low-rank models has not received much attention in the literature. The work of [18] considers the GLRT, under a low-rank Gaussian model, for a covariance equality test with a different alternative hypothesis $\mathcal{H}_{1}^{\prime}: \mathbf{R}_{1} \neq$ $\mathbf{R}_{2}=\ldots=\mathbf{R}_{L}$. An extension to the specific case of subspace equality test has also been proposed by the same authors in $[19]$.

Under the model (6), the information about a potential change is contained in the $K$ largest eigenvalues and associated eigenvectors of $\mathbf{R}_{\ell}$. Therefore, classical results on the spiked models for random matrices of the Fisher type [17] can be exploited to characterize the asymptotic behaviour of the extreme eigenvalues of $\left(\hat{\mathbf{R}}_{\ell}^{-1} \hat{\mathbf{R}}\right)_{\ell=1, \ldots, L}$, from which information about a potential change can be extracted. In the same way, the asymptotic behaviour of the largest eigenvalues of the spiked Wishart-type matrices [20] $\hat{\mathbf{R}},\left(\hat{\mathbf{R}}_{\ell}\right)_{\ell=1, \ldots, L}$ convey information about changes in the true covariances $\mathbf{R}_{1}, \ldots, \mathbf{R}_{L}$ [1], which can also be exploited to build test statistics relevant for the low-rank model in the high-dimensional regime. This latter option is the path followed in this paper.

Contributions. In this paper, we derive a new test statistic, no longer based on the family of statistics $S$ studied in [3], but which relies on the $K$ largest eigenvalues of the matrices $\hat{\mathbf{R}}_{1}, \ldots, \hat{\mathbf{R}}_{L}, \hat{\mathbf{R}}$. More precisely, the test statistic compares in a certain sense estimates of the eigenvalues of the matrices $\boldsymbol{\Gamma}_{1}, \ldots, \boldsymbol{\Gamma}_{L}$ with estimates of the eigenvalues of the mixture $\boldsymbol{\Gamma}=\sum_{\ell=1}^{L} \frac{N_{\ell}}{N} \boldsymbol{\Gamma}_{\ell}$. We show that the proposed test statistic is consistent under the high-dimensional regime and the low-rank model (6), and with a controlled asymptotic type I error. To that purpose, the results of [21], which provides the asymptotic distribution of the $K$ largest eigenvalues of $\hat{\mathbf{R}}_{\ell}$ for a fixed $\ell$, are extended to provide the joint asymptotic distribution of the $K$ largest eigenvalues of the matrices $\hat{\mathbf{R}}, \hat{\mathbf{R}}_{1}, \ldots, \hat{\mathbf{R}}_{L}$. The proposed test statistic is then compared to various alternatives, including the GLRT for the low-rank model (6) as well as a statistic built from the results of [17] on the extreme eigenvalues of the spiked Fisher matrices $\left(\hat{\mathbf{R}}_{\ell}^{-1} \hat{\mathbf{R}}\right)_{\ell=1, \ldots, L}$. We also provide an empirical study of the proposed test statistic on Synthetic Aperture Radar (SAR) images for detecting changes between two scenes.
Organization. The paper is organized as follows. In Section II, we study an extension of the results of [21] on the asymptotic distribution of the largest eigenvalues of $\hat{\mathbf{R}}_{1}, \ldots, \hat{\mathbf{R}}_{L}, \hat{\mathbf{R}}$. In Section III, we exploit the results derived in the previous section to build a new test statistic, for which we study its performance in the high-dimensional regime. Sections IV and V are dedicated to compare, both theoretically and numerically, our proposed test statistic with alternative approaches. Simulations on synthetic data and on real data (SAR images) are provided.
Notations. For $a \in \mathbb{R}, a^{+}$denotes the positive part. Vectors and matrices are denoted with boldface lower case and upper case letters respectively. For a complex matrix $\mathbf{A}$, we denote by $\mathbf{A}^{T}$ and $\mathbf{A}^{*}$ its transpose and conjugate transpose. If $\mathbf{A}$ is a $n \times n$ complex matrix, $\operatorname{tr}(\mathbf{A})$ denotes its trace and $\lambda_{1}(\mathbf{A}), \ldots, \lambda_{n}(\mathbf{A})$ denote its eigenvalues. If $\mathbf{A}$ is Hermitian, the eigenvalues are considered in decreasing order $\lambda_{1}(\mathbf{A}) \geq$ $\ldots \geq \lambda_{n}(\mathbf{A})$. For matrices $\mathbf{A}_{1}, \ldots, \mathbf{A}_{n}, \operatorname{bdiag}\left(\mathbf{A}_{1}, \ldots, \mathbf{A}_{n}\right)$ denotes the the block diagonal matrix formed by $\mathbf{A}_{1}, \ldots, \mathbf{A}_{n}$. The complex circular Gaussian distribution on $\mathbb{C}^{n}$ with covariance matrix $\mathbf{R}$ is denoted as $\mathcal{N}_{\mathbb{C}^{n}}(\mathbf{0}, \mathbf{R})$, while the real Gaussian distribution on $\mathbb{R}^{n}$ with mean $\boldsymbol{\mu}$ and covariance matrix $\mathbf{R}$ is denoted as $\mathcal{N}_{


---

In comparison with the classical low-dimensional regime where $M$ is assumed fixed while $N_{1}, \ldots, N_{L} \rightarrow \infty$ (see e.g. [22], [11]), the high-dimensional regime described in Assumption 1 models practical scenarios where the sample sizes $N_{1}, \ldots, N_{L}$ are of the same order of magnitude as the dimension $M$ and where $K$ is small compared to $M$. This regime has been widely used in the high-dimensional statistics literature (see e.g. [23]), as well as in the signal processing applications (see e.g. [15], [24], [25]).
In what follows the high-dimensional regime described in Assumption 1 is represented by the notation $M \rightarrow \infty$. We also define

$$
c:=\left(\sum_{\ell=1}^{L} \frac{1}{c_{\ell}}\right)^{-1}
$$

as well as

$$
\bar{\Gamma}:=\sum_{\ell=1}^{L} \frac{N_{\ell}}{\bar{N}} \Gamma_{\ell}
$$

One can notice that $\bar{\Gamma}$ is the the pooling of the low-rank covariance matrices $\Gamma_{1}, \ldots, \Gamma_{L}$ and has rank at most $K L$. In the following, we also need to ensure the convergence of the eigenvalues of matrices $\Gamma_{\ell}, \bar{\Gamma}$ in the high-dimensional regime.
Assumption 2. For all $k \in\{1, \ldots, K\}, \ell \in\{1, \ldots, L\}$,

$$
\lambda_{k}\left(\Gamma_{\ell}\right)=\gamma_{k, \ell}+o\left(\frac{1}{\sqrt{M}}\right)
$$

and for all $k \in\{1, \ldots, K L\}$,

$$
\lambda_{k}(\bar{\Gamma})=\gamma_{k}+o\left(\frac{1}{\sqrt{M}}\right)
$$

We note that Assumption 2 is a purely technical assumption which is not restrictive in practice as the corresponding results derived from it are meant to be used for fixed values of $M, N, K$.
Under Assumptions 1 and 2 , the global behaviour of the eigenvalues of $\hat{R}$ can be described through its empirical spectral distribution defined as the random probability measure

$$
\hat{\mu}=\frac{1}{M} \sum_{k=1}^{M} \delta_{\lambda_{k}(\hat{R})}
$$

where $\delta_{x}$ is the Dirac measure centered at $x$. Under the model (6), each covariance matrix $R_{1}, \ldots, R_{L}$ is a fixed rank $K$ perturbation of the matrix $\sigma^{2} \mathrm{I}$ and it can be shown using standard perturbations arguments that $\hat{\mu}$ asymptotically behaves as the Marcenko-Pastur distribution, i.e. $\hat{\mu}$ converges weakly almost surely (a.s.) to the probability measure:

$$
\begin{aligned}
\mu(d x)= & \sqrt{\left(x-x_{-}\right)\left(x_{+}-x\right)} \frac{2 \pi \sigma^{2} c_{x} \mathbf{1}_{\left[x_{-}, x_{+}\right]}(x) d x}{} \\
& +\left(1-\frac{1}{c}\right)^{+} \delta_{0}(d x)
\end{aligned}
$$

where $x_{ \pm}=\sigma^{2}(1 \pm \sqrt{c})^{2}$. Consequently, any functional of the type

$$
\hat{\mu}(\phi):=\frac{1}{M} \sum_{k=1}^{M} \phi\left(\lambda_{k}(\hat{R})\right)
$$

where $\phi$ is a bounded continuous function, satisfies

$$
\hat{\mu}(\phi)=\int_{\mathbb{R}} \phi(\lambda) d \hat{\mu}(\lambda) \xrightarrow[M \rightarrow \infty]{\text { a.s. }} \int_{\mathbb{R}} \phi(\lambda) d \mu(\lambda)
$$

As the limit in (17) only depends on $\sigma^{2}$ and $c$, it is not possible to recover information on the low-rank matrices $\Gamma_{1}, \ldots, \Gamma_{L}$ in the high-dimensional regime from statistics of type (16). However, under the previous assumptions, it can be shown that the information related to the spectrum of $\bar{\Gamma}$ can be found in the largest $K L$ eigenvalues of $\hat{R}$, thanks to the following result.
Theorem 1. Under Assumptions 1 and $2, \forall k \in\{1, \ldots, K L\}$,

$$
\lambda_{k}(\hat{R}) \xrightarrow[M \rightarrow \infty]{\text { a.s. }} \varphi_{c}\left(\gamma_{k}, \sigma^{2}\right)
$$

with

$$
\varphi_{c}\left(\gamma, \sigma^{2}\right):= \begin{cases}\frac{\left(\gamma+\sigma^{2}\right)\left(\gamma+\sigma^{2} c\right)}{\gamma} & \text { if } \gamma>\sigma^{2} \sqrt{c} \\ \sigma^{2}(1+\sqrt{c})^{2} & \text { if } \gamma \leq \sigma^{2} \sqrt{c}\end{cases}
$$

Moreover, $\lambda_{K L+1}(\hat{R}) \rightarrow \sigma^{2}(1+\sqrt{c})^{2}$ a.s. when $M \rightarrow \infty$.
Proof. The proof of Theorem 1 is deferred to Appendix B.
The matrix $\hat{R}$ being a mixture of $L$ independent but not identically distributed Wishart matrices, we note that Theorem 1 provides an extension of the results of [21, Th. 2.7] (see also [26]) to the case $L>1$. It shows in particular that the largest eigenvalues of $\hat{R}$ converge to some limits depending directly of the eigenvalues of $\bar{\Gamma}$, provided that for all $k \in$ $\{1, \ldots, K L\}$ the ratios $\frac{\gamma_{k}}{\sigma^{2}}$ are above $\sqrt{c}$. The threshold $\sqrt{c}$ can be interpreted as a minimal SNR above which the $k$ th largest signal related eigenvalues of $\hat{R}$ splits from the largest noise related eigenvalue $\lambda_{K L+1}(\hat{R})$.
The next result shows, under hypothesis $\mathcal{H}_{0}$, a joint Central Limit Theorem (CLT) on the largest eigenvalues of $\hat{R}_{1}, \ldots, \hat{R}_{L}, \hat{R}$.
Theorem 2. Let Assumptions 1-2 hold. Assume moreover that $\Gamma_{1}=\ldots=\Gamma_{L}\left(\right.$ thus $\left.\gamma_{k, \ell}=\gamma_{k}\right)$ and that

$$
\gamma_{1}>\ldots>\gamma_{K}>\sigma^{2} \max \left\{\sqrt{c}, \sqrt{c_{1}}, \ldots, \sqrt{c_{L}}\right\}
$$

Then we have

$$
\sqrt{M}\left(\begin{array}{lll}
\lambda_{k}(\hat{R})-\varphi_{c}\left(\gamma_{k}, \sigma^{2}\right) & \left(\lambda_{k}\left(\hat{R}_{\ell}\right)-\varphi_{c_{\ell}}\left(\gamma_{k}, \sigma^{2}\right)\right)_{\ell=1, \ldots, L}
\end{array}\right)_{k=1, \ldots, K} \xrightarrow[M \rightarrow \infty]{\mathcal{D}} \mathcal{N}_{R^{K(L+1)}}(0, \Theta),
$$

where $\Theta$ is a positive definite block diagonal matrix given by $\Theta=\operatorname{bdiag}\left(\Theta_{1}, \ldots, \Theta_{K}\right)$ with

$$
\Theta_{k}:=\left(\begin{array}{cccc}
\theta_{k, 0}^{2} & \vartheta_{k, 1} & \ldots & \vartheta_{k, L} \\
\vartheta_{k, 1} & \ddots & & \vdots \\
& & \ddots & \vartheta_{k, L} \\
\vartheta_{k, L} & \ldots & \ldots & \theta_{k, L}^{2}
\end{array}\right)
$$

and by denoting $c_{0}=c$,

$$
\theta_{k, \ell}^{2}=


---

$$
\vartheta_{k, \ell}=\frac{c_{0}}{\left(\gamma_{k}^{2}-\sigma^{4} c_{\ell}\right)\left(\gamma_{k}+\sigma^{2}\right)^{2}} \gamma_{k}^{2}, \quad \ell \geq 1
$$

Proof. The proof is postponed to Appendix C.
The result of Theorem 2 provides an extension of [20, Th. 1.4] which studies a CLT for the $K$ largest eigenvalues of $\hat{\mathbf{R}}_{\ell}$. We note that the result of Theorem 2 cannot be inferred directly from [20, Th. 1.4] and requires a careful study due to the strong dependency between the eigenvalues of $\hat{\mathbf{R}}$ and the ones of $\hat{\mathbf{R}}_{1}, \ldots, \hat{\mathbf{R}}_{L}$.
Theorems 1 and 2 are exploited in the following section to build a new statistic for the test (2), relevant for the low-rank model (6).

# III. PROPOSED TEST STATISTIC 

Before introducing our new test statistic, we first notice that the test (2) can be reformulated as:

$$
\begin{aligned}
& \mathcal{H}_{0}: \quad \Gamma_{1}=\ldots=\Gamma_{L} \\
& \mathcal{H}_{1}: \quad \exists(i, j) \in\{1, \ldots, L\}^{2} \text { s.t. } \Gamma_{i} \neq \Gamma_{j}
\end{aligned}
$$

and we assume in the following that the rank $K$ is known (see also Remark 1 below in case the rank is unknown). Next, we consider the following lemma, which shows that hypothesis $\mathcal{H}_{0}$ can be verified by comparing the eigenvalues of matrix $\boldsymbol{\Gamma}$ with the ones of matrices $\Gamma_{1}, \ldots, \boldsymbol{\Gamma}_{L}$.
Lemma 1. The following assertions are equivalent:
(a) $\boldsymbol{\Gamma}_{1}=\ldots=\boldsymbol{\Gamma}_{L}$,
(b) For all $k=1, \ldots, K, \ell=1, \ldots, L, \lambda_{k}\left(\Gamma_{\ell}\right)=\lambda_{k}(\boldsymbol{\Gamma})$.

Proof. The proof of Lemma 1 can be found in [1].
From Lemma 1, one can equivalently formulate the test (25) as follows

$$
\begin{gathered}
\mathcal{H}_{0}: \quad \forall k, \ell, \lambda_{k}\left(\Gamma_{\ell}\right)=\lambda_{k}(\boldsymbol{\Gamma}) \\
\mathcal{H}_{1}: \quad \exists k, \ell: \lambda_{k}\left(\Gamma_{\ell}\right) \neq \lambda_{k}(\boldsymbol{\Gamma})
\end{gathered}
$$

Consequently, it is possible to discriminate between hypotheses $\mathcal{H}_{0}$ and $\mathcal{H}_{1}$ by exploiting only the eigenvalues of the matrices $\Gamma_{1}, \ldots, \Gamma_{L}, \Gamma$ for which we can also build consistent estimators in the high-dimensional regime as follows. Let us consider first the maximum likelihood estimator of the noise variance $\sigma^{2}$ given by

$$
\hat{\sigma}^{2}:=\sum_{\ell=1}^{L} \frac{N_{\ell}}{N} \frac{1}{M-K} \sum_{k=K+1}^{M} \lambda_{k}\left(\hat{\mathbf{R}}_{\ell}\right)
$$

From (6) and Theorem 1 , one can easily show that $\hat{\sigma}^{2} \longrightarrow \sigma^{2}$ a.s. as $M \rightarrow+\infty$ under both $\mathcal{H}_{0}$ and $\mathcal{H}_{1}$. Next, for all $k \in\{1, \ldots, K L\}$, let $\hat{\gamma}_{k}$ be the largest solution to the equation $\varphi_{c}\left(\gamma_{k}, \hat{\sigma}^{2}\right)=\lambda_{k}(\hat{\mathbf{R}})$ if $\lambda_{k}(\hat{\mathbf{R}})>\hat{\sigma}^{2}(1+\sqrt{c})^{2}$, or $\hat{\gamma}_{k}=\hat{\sigma}^{2} \sqrt{c}$ otherwise. Similarly, for all $k \in\{1, \ldots, K\}$, let $\hat{\gamma}_{k, \ell}$ be the largest solution to the equation $\varphi_{c_{\ell}}\left(\gamma_{k, \ell}, \hat{\sigma}^{2}\right)=\lambda_{k}\left(\hat{\mathbf{R}}_{\ell}\right)$ if $\lambda_{k}\left(\hat{\mathbf{R}}_{\ell}\right)>\hat{\sigma}^{2}\left(1+\sqrt{c_{\ell}}\right)^{2}$, or $\hat{\gamma}_{k, \ell}=\hat{\sigma}^{2} \sqrt{c_{\ell}}$ otherwise. Then we have the following immediate result, as a consequence of Theorem 1.
Corollary 1. Under Assumptions 1 and 2,

$$
\begin{aligned}
& \hat{\gamma}_{k} \xrightarrow[M \rightarrow \infty]{\text { a.s. }}\left\{\begin{array}{lr}
\gamma_{k} & \text { if } \gamma_{k}>\sigma^{2} \sqrt{c} \\
\sigma^{2} \sqrt{c} & \text { otherwise }
\end{array}\right. \\
& \hat{\gamma}_{k, \ell} \xrightarrow[M \rightarrow \infty]{\text { a.s. }}\left\{\begin{array}{ll}
\gamma_{k, \ell} & \text { if } \gamma_{k, \ell}>\sigma^{2} \sqrt{c_{\ell}} \\
\sigma^{2} \sqrt{c_{\ell}} & \text { otherwise }
\end{array}\right.
\end{aligned}
$$

Considering this result we propose the following test statistic

$$
T(\epsilon)=\mathbf{1}_{(\epsilon,+\infty)}\left(\|\hat{\boldsymbol{\gamma}}\|_{2}^{2}\right)
$$

where

$$
\hat{\boldsymbol{\gamma}}=\left(\hat{\gamma}_{k}-\hat{\gamma}_{k, \ell}\right)_{\substack{k=1, \ldots, K \\ \ell=1, \ldots, L}}
$$

To study the performance in terms of consistency and asymptotic type I error of the test statistic (30), we consider the following assumption which ensures that the signal and noise eigenvalues of matrices $\hat{\mathbf{R}}, \hat{\mathbf{R}}_{1}, \ldots, \hat{\mathbf{R}}_{L}$ are separated in the high-dimensional regime.
Assumption 3. For all $k \in\{1, \ldots, K\}$ and $\ell \in\{1, \ldots, L\}$,

$$
\begin{aligned}
& \gamma_{1, \ell}>\ldots>\gamma_{K, \ell}>\sigma^{2} \max \left\{\sqrt{c_{1}}, \ldots, \sqrt{c_{L}}\right\} \\
& \gamma_{1}>\ldots>\gamma_{K}>\sigma^{2} \sqrt{c}
\end{aligned}
$$

Moreover, under $\mathcal{H}_{1}$, there exist $k, \ell$ such that $\gamma_{k} \neq \gamma_{k, \ell}$.
As a consequence of Corollary 1, we have under Assumptions 1-3,

$$
\|\hat{\boldsymbol{\gamma}}\|_{2}^{2} \xrightarrow[M \rightarrow \infty]{\text { a.s. }}\|\boldsymbol{\gamma}\|_{2}^{2}
$$

with

$$
\boldsymbol{\gamma}=\left(\gamma_{k}-\gamma_{k, l}\right)_{\substack{k=1, \ldots, K \\ \ell=1, \ldots, L}}
$$

such that $\boldsymbol{\gamma}=\mathbf{0}$ under $\mathcal{H}_{0}$ and $\boldsymbol{\gamma} \neq \mathbf{0}$ under $\mathcal{H}_{1}$. This implies the following consistency result.

Theorem 3. Let Assumptions 1-3 hold and denote $\epsilon_{1}=$ $\|\boldsymbol{\gamma}\|_{2}^{2}>0$ under $\mathcal{H}_{1}$. Then for all $\epsilon \in\left(0, \epsilon_{1}\right)$,




---

and with

where

$$
\begin{aligned}
\omega_{k, \ell}^{2} & =c_{\ell} \frac{\gamma_{k}^{2}\left(\gamma_{k}+\sigma^{2}\right)^{2}}{\gamma_{k}^{2}-\sigma^{4} c_{\ell}}, \quad \ell=0, \ldots, L \\
\xi_{k} & =c_{0} \frac{\gamma_{k}^{2}\left(\gamma_{k}+\sigma^{2}\right)^{2}}{\gamma_{k}^{2}-\sigma^{4} c_{0}}
\end{aligned}
$$

Proof. The proof is deferred to Appendix D.
From Corollary 2, we can adjust the threshold $\epsilon$ in (30) to control the asymptotic type I error in the high-dimensional regime, as described in the next result. Let us define $\hat{\Upsilon}=$ $\operatorname{bdiag}\left(\hat{\Upsilon}_{1}, \ldots, \hat{\Upsilon}_{K}\right)$ with

$$
\hat{\boldsymbol{U}}_{k}=\left(\begin{array}{cccc}
\hat{\omega}_{k, 0}^{2} & \hat{\xi}_{k} & \ldots & \hat{\xi}_{k} \\
\hat{\xi}_{k} & \ddots & \ddots & \vdots \\
\vdots & \ddots & \ddots & \hat{\xi}_{k} \\
\hat{\xi}_{k} & \ldots & \hat{\xi}_{k} & \hat{\omega}_{k, L}^{2}
\end{array}\right)
$$

where

$$
\begin{aligned}
\hat{\omega}_{k, \ell}^{2} & =c_{\ell} \frac{\hat{\gamma}_{k}^{2}\left(\hat{\gamma}_{k}+\hat{\sigma}^{2}\right)^{2}}{\hat{\gamma}_{k}^{2}-\hat{\sigma}^{4} c_{\ell}}, \quad \ell \geq 0 \\
\hat{\xi}_{k} & =c_{0} \frac{\hat{\gamma}_{k}^{2}\left(\hat{\gamma}_{k}+\hat{\sigma}^{2}\right)^{2}}{\hat{\gamma}_{k}^{2}-\hat{\sigma}^{4} c_{0}}
\end{aligned}
$$

From Corollary 1, it is clear that $\hat{\Upsilon} \rightarrow \Upsilon$ a.s. as $M \rightarrow \infty$.
Theorem 4. Let $\mathbf{x} \in \mathcal{N}_{R}^{K L}(0, \mathbf{I})$ and $F(t, \Xi)=$ $\mathrm{P}\left(\mathbf{x}^{T} \Xi \mathbf{x} \leq t\right), \alpha \in(0,1)$ and set

$$
\hat{\epsilon}=\frac{1}{M} \inf \left\{t \in \mathbb{R}: F\left(t, \mathbf{H} \hat{\Upsilon} \mathbf{H}^{T}\right) \geq 1-\alpha\right\}
$$

Then under Assumptions 1 and 3, we have

$$
\mathrm{P}_{0}(T(\hat{\epsilon})=1) \underset{M \rightarrow \infty}{\longrightarrow} \alpha
$$

In practice, Theorem 4 is used as follows. For a fixed realization of $\hat{\Upsilon}$, we sample the distribution of the Gaussian quadratic form $\mathbf{x}^{T} \mathbf{H} \hat{\Upsilon} \mathbf{H}^{T} \mathbf{x}$ and the threshold $\hat{\epsilon}$ is then set as the $(1-\alpha)$-quantile of $\mathbf{x}^{T} \mathbf{H} \hat{\Upsilon} \mathbf{H}^{T} \mathbf{x}$.

Remark 1. For a more general approach where each $\Gamma_{\ell}$ has unknown rank $K_{\ell}$, one can obtain consistent estimates of $K_{1}, \ldots, K_{L}$ thanks to Theorem 1. Assuming $K_{1}, \ldots, K_{L}$ fixed with respect to $M$, and if for $\ell \in\{1, \ldots, L\}, \gamma_{K_{\ell}, \ell}>\sigma^{2} \sqrt{c_{\ell}}$, under Assumption 2 the quantity

$$
\hat{K}_{\ell}=\max \left\{k: \lambda_{k}\left(\hat{R}_{\ell}\right)>\sigma^{2}\left(1+\sqrt{c_{\ell}}\right)^{2}+\epsilon_{\ell}\right\}
$$

converges almost surely to $K_{\ell}$ in the high-dimensional regime, for all $\epsilon_{\ell} \in\left(0, \varphi_{c_{\ell}}\left(\gamma_{K_{\ell}, \ell}, \sigma^{2}\right)-\sigma^{2}\left(1+\sqrt{c_{\ell}}\right)^{2}\right)$. This shows that we can build consistent test statistics to capture changes in the rank (see further [27]).

Remark 2. It is easy to show that under Assumption 3, the matrix $\mathbf{H} \Upsilon \mathbf{H}^{T}$ is non singular. Therefore, an alternative approach to obtain a test statistic with controlled asymptotic type I error would be to consider the statistic

$$
\tilde{T}(\epsilon)=1_{(\epsilon,+\infty)}\left(M\left\|\left(\mathbf{H} \hat{\boldsymbol{U}} \mathbf{H}^{T}\right)^{-\frac{1}{2}} \hat{\gamma}\right\|_{2}^{2}\right)
$$

since from Corollary 2 , we have

$$
M\left\|\left(\mathbf{H} \hat{\Upsilon} \mathbf{H}^{T}\right)^{-\frac{1}{2}} \hat{\boldsymbol{\gamma}}\right\|_{2}^{2} \xrightarrow[M \rightarrow \infty]{\mathcal{D}} \chi^{2}(K L)
$$

Nevertheless, although this approach looks simpler, it appears that the covariance matrix $\mathbf{H} \Upsilon \mathbf{H}^{T}$ is ill-conditioned. This can be readily seen, e.g. in the special case where $c_{1}=\ldots=c_{L}$ and for a large SNR. If $\kappa\left(\Upsilon_{k}\right)$ denotes the condition number of $\Upsilon_{k}$ defined in (39), then we can verify (details are omitted) that $\kappa\left(\Upsilon_{k}\right)$ scales with $\gamma^{2}$ as $\gamma^{2} \rightarrow \infty$. Therefore, in practice, setting the threshold $\epsilon$ based on the $\chi^{2}(K L)$ distribution gives poor performance.

# IV. SOME COMPARISONS WITH ALTERNATIVE METHODS 

In this section, we compare the test statistic given in (30) with two relevant alternatives for the low-rank model (6) and the high-dimensional regime described in Assumption 1. To that purpose, we consider scenarios involving a change of subspace/eigenvalues for the rank $K=1$ model $\Gamma_{\ell}=\gamma_{1, \ell} \mathbf{u}_{\ell} \mathbf{u}_{\ell}^{*}$, where $\left\|\mathbf{u}_{\ell}\right\|_{2}=1$, and where $\gamma_{1, \ell}$ is independent of $M$.
We precise that our objective is not to provide an exhaustive analysis of all the possible scenarios under $\mathcal{H}_{1}$, but to draw some performance comparisons, in terms of consistency, out of a few simple cases. In the remainder of this section, we also assume that $L=2$ and $N_{1}=N_{2}$ so that $c_{1}=c_{2}=2 c$.

## A. A test based on spiked Fisher matrices

Although test statistics of the form (3) are not consistent in the high-dimensional regime, we can build consistent test statistics by exploiting the behaviour of the largest and smallest eigenvalues of the Fisher matrices $\hat{R}_{2}^{-\frac{1}{2}} \hat{R}_{1}$ (see [17]). We propose ${ }^{1}$ to use $T_{\text {Fisher }}(\epsilon)=1_{(\epsilon,+\infty)}(F)$ with

$$
\begin{aligned}
F= & \sum_{\substack{\ell, \ell^{\prime}=1 \\
\ell^{\prime} \neq \ell}}^{L} \sum_{k=1}^{K}\left[\left(\lambda_{k}\left(\hat{\mathbf{R}}_{\ell}^{-


---

$\Gamma_{1}$ and $\Gamma_{2}$ are only carried by the unit norm eigenvector $\mathbf{u}_{2}$. It is easily seen that

$$
\lambda_{k}\left(\mathbf{R}_{2}^{-1} \mathbf{R}_{1}\right) \xrightarrow[M \rightarrow \infty]{ } \begin{cases}\frac{\gamma_{1,1}+\sigma^{2}}{\sigma^{2}} & \text { if } k=1 \\ 1 & \text { if } k=2, \ldots, M-1 \\ \frac{\sigma^{2}}{\gamma_{1,1}+\sigma^{2}} & \text { if } k=M\end{cases}
$$

so that applying [17, Th. 3.1] shows that for all small $\epsilon>0$,

$$
\mathbb{P}_{i}\left(\lim \mathcal{T}_{\text {Fisher }}(\epsilon)=i\right)=1 \text { for } i \in\{0,1\} \text { as } M \rightarrow \infty \text { iff }
$$

$$
\frac{\gamma_{1,1}}{\sigma^{2}}>\beta=\frac{2\left(c+\sqrt{c-c^{2}}\right)}{1-2 c}
$$

One can see that $\beta>\sqrt{2 c}$ and therefore, from Assumption 3 and Theorem 3, we deduce that the Fisher based statistic requires a larger $\operatorname{SNR} \frac{\gamma_{1,1}}{\sigma^{2}}$ compared to the Wishart based statistic proposed in (30) to be consistent in the change of subspace scenario.
Change of eigenvalues. In that case, we assume that $\gamma_{1,2}=$ $\gamma_{1,1}(1+\delta)$ with $\delta>0$ and $\mathbf{u}_{1}=\mathbf{u}_{2}$, so that the changes are only carried by the largest eigenvalue of $\Gamma_{2}$. Note that under these settings, Assumption 2 is verified and it holds that

$$
\lambda_{k}\left(\mathbf{R}_{2}^{-1} \mathbf{R}_{1}\right) \xrightarrow[M \rightarrow \infty]{ } \begin{cases}\frac{\gamma_{1,1}+\sigma^{2}}{\gamma_{1,1}(1+\delta)+\sigma^{2}} & \text { if } k=1 \\ 1 & \text { if } k=2, \ldots, M\end{cases}
$$

Using again [17, Th. 3.1], we have that for all small $\epsilon>0$,

$$
\mathbb{P}\left(\lim \mathcal{T}_{\text {Fisher }}(\epsilon)=i\right)=1 \text { for } i \in 0,1 \text { as } M \rightarrow \infty \text { iff }
$$

$$
\delta>\frac{2\left(c+\sqrt{c-c^{2}}\right)}{1-2 c}
$$

and

$$
\frac{\gamma_{1,1}}{\sigma^{2}}>\beta=\frac{2\left(c+\sqrt{c-c^{2}}\right)}{(1+\delta)(1-2 c)-\left(1+2 \sqrt{c-c^{2}}\right)}
$$

In this scenario, one can see that the minimal $\operatorname{SNR} \beta$ decreases when $\delta$ increases, which can be exploited to produce conditions where the Fisher test statistic is consistent while the Wishart one is not. Indeed, choose $\sqrt{c}<\frac{\gamma_{1,1}}{\sigma^{2}}<\sqrt{2 c}$ and $\delta$ large enough so that (52) and (53) are verified. Then it can be seen from Corollary 1 that $\|\hat{\boldsymbol{\gamma}}\|_{2}^{2} \rightarrow 2\left(\gamma_{1,1}-\sigma^{2} \sqrt{2 c}\right)^{2}$ a.s. as $M$ $\rightarrow \infty$ and therefore for all small $\epsilon>0, \mathbb{P}_{0}(\lim \mathcal{T}(\epsilon)=1)=1$.

# B. The GLR for (25) 

As an alternative to the GLR for the general covariance equality test (2), the GLR for the low-rank test (25) can be derived. Classical computations (details are omitted) provide the following test statistic $\mathcal{T}_{\mathrm{GLR}-\mathrm{LR}}(\epsilon)=\mathbf{1}_{(\epsilon,+\infty)}(G)$ where

$$
\begin{aligned}
G= & -\sum_{\ell=1}^{L} \sum_{k=1}^{K} N_{\ell} \log \left(\frac{\lambda_{k}\left(\hat{\mathbf{R}}_{\ell}\right)}{\lambda_{k}(\hat{\mathbf{R}})}\right) \\
& -N(M-K) \log \left(\frac{\frac{1}{M-K} \sum_{\ell=1}^{L} \frac{N_{\ell}}{N}}{\frac{1}{M-K} \sum_{k=K+1}^{M}} \lambda_{k}\left(\hat{\mathbf{R}}_{\ell}\right)\right.
\end{aligned}
$$

Using Theorem 1, it can be shown that $G \rightarrow G_{\infty}$ a.s. as $M \rightarrow \infty$ where

$$
G_{\infty}=\sum_{\ell=1}^{L} \frac{c}{c_{\ell}} \sum_{k=1}^{K}\left(\psi\left(\frac{\varphi_{c}\left(\gamma_{k}\right)}{\sigma^{2}}\right)-\psi\left(\frac{\varphi_{c_{\ell}}\left(\gamma_{k, \ell}\right)}{\sigma^{2}}\right)\right)
$$

with $\psi(x)=x-\log (x)$.
Let us consider a change of eigenvalues with $\gamma_{1,2}=\gamma_{1,1}+\delta$ and $\mathbf{u}_{1}=\mathbf{u}_{2}$ under $\mathcal{H}_{1}$. Then it is easy to see that under both $\mathcal{H}_{0}$ and $\mathcal{H}_{1}, G_{\infty}=-c+\mathcal{O}\left(\frac{1}{\gamma_{1,1}}\right)$ as $\gamma_{1,1} \rightarrow+\infty$. Regarding the proposed test (30), we have $\|\boldsymbol{\gamma}\|_{2}^{2}=\frac{\delta^{2}}{2}$ under $\mathcal{H}_{1}$ which shows the limit (34) under $\mathcal{H}_{0}$ and $\mathcal{H}_{1}$ cannot be made arbitrarily close as $\gamma_{1,1} \rightarrow \infty$. This suggests that for a large $\gamma_{1,1}$ and a fixed change $\delta$, the GLR for the low-rank model might experience a performance loss compared to the test (30).

## V. SIMULATIONS

In this section, we provide simulations to illustrate the performance of the test statistic $\mathcal{T}$ proposed in (30), and to perform some comparisons with the alternative test statistics introduced in Section IV. We consider $\sigma^{2}=0.5, K=2, L=$ 2 as well as a Toeplitz model of rank $K=2$ for the covariance matrix $\Gamma_{\ell}$ which can therefore be written as

$$
\Gamma_{\ell}=\gamma_{1, \ell} \mathbf{a}\left(\theta_{1, \ell}\right) \mathbf{a}^{*}\left(\theta_{1, \ell}\right)+\gamma_{2, \ell} \mathbf{a}\left(\theta_{2, \ell}\right) \mathbf{a}^{*}\left(\theta_{2, \ell}\right)
$$

with $\mathbf{a}(\theta)=\frac{1}{\sqrt{M}}\left(1, e^{i \theta} \ldots, e^{i(M-1) \theta}\right)^{T}$. Note that the model (56) is common in spectral analysis and array processing [28].

## A. Empirical and asymptotic Type I error of $\mathcal{T}(\epsilon)$

We first illustrate the result of Theorem 4 and consider $\theta_{k, \ell}=0$ for $(k, \ell) \in\{1,2\}^{2}, \gamma_{1, \ell}=3$ and $\gamma_{2, \ell}=1.5$ for $\ell \in\{1,2\}$ and $N_{1}=N_{2}=2 M$. The threshold $\epsilon$ of (30) is set as the $(1-\alpha)$-quantile of the Gaussian quadratic form $\mathbf


---

hypothesis $\gamma_{1,1}=\gamma_{1,2}=2, \gamma_{2,1}=\gamma_{2,2}=1$ and $N_{1}=$ $N_{2}=2 M$ thus $c_{1}=c_{2}$.
(2) Change of Eigenvalues: under $\mathcal{H}_{0}, \gamma_{1,1}=\gamma_{1,2}=2$, $\gamma_{2,1}=\gamma_{2,2}=1.5$ and under $\mathcal{H}_{1}, \gamma_{1,1}=2, \gamma_{1,2}=5$, $\gamma_{2,1}=1.5, \gamma_{2,2}=4$. We will also consider under both hypothesis $\theta_{1,1}=\theta_{1,2}=0, \theta_{2,1}=\theta_{2,2}=0$ and $N_{1}=$ $N_{2}=4 M$ thus $c_{1}=c_{2}$

In the simulations that follow, for both scenarios, we compute the power of different test statistics for a given type I error $\alpha$ and different values of $M$. The statistic $T(\epsilon)$, which will be termed as "Wishart" below, will be compared to the statistics $T_{\text {Fisher }}(\epsilon)$ (termed as "Fisher"), $T_{\mathrm{GLR}-\mathrm{LR}}(\epsilon)$ (termed as "GLR-LR") and $T_{\mathrm{GLR}}(\epsilon)=\mathbf{1}_{(\epsilon,+\infty)}\left(S_{\mid \phi=\log }\right)$ where $S$ is given in (3) (termed as "GLR"). For each of the statistics, the threshold $\epsilon$ is adjusted separately to achieve a type I error of $\alpha$. Note that for both scenarios, Assumptions 2, 3 are verified and that the condition for the Fisher statistic to be consistent is verified as well.
We observe that in both scenarios,


the proposed Wishart statistic shows a significantly better performance as $M$ is increasing. Second, while the GLR-LR statistic outperforms the Wishart one for low dimensions $M$ in the change of subspace scenario, the Wishart statistic still demonstrates a higher power compared to the Fisher and GLR statistics for both scenarios.
The next simulation in Table IV shows the evolution of the power for different values of the noise variance in the change of eigenvalues scenario $(M=100)$. The same can be done for the change of subspace scenario in Table V. We observe that the test statistics designed for a low-rank scenario (Wishart, Fisher, GLR-LR) outperform the GLR in general. Additionally, when the noise variance $\sigma^{2}$ becomes too large, the conditions on the SNR ensuring the consistency of these statistics (Assumption 3 and the conditions of [17]) are not met anymore, and one observes in that case a significant drop of the performance $\left(\sigma^{2}=5.5\right.$ in Table IV and $\sigma^{2}=2.5$ in



Remark 3. In view of the simulations results described in Tables II-V, we observe that the proposed test statistic (30) performs poorly when the conditions described in Assumptions 1 and 3 are not met, i.e. when the dimension $M$ or the SNR are not large enough. Scenarios where the rank $K$ is also of the same order of magnitude than $M$, thus violating Assumption 1 , will also invalidate Theorem 4 and the asymptotic type I error will be poorly controlled in that case.

# C. An application to change detection in SAR images 

In this section, we evaluate the performance of the proposed test statistic on images drawn from the UAV-SAR dataset of NASA/JPL-Caltech (SanAnd 26524 03, Segment 4). We consider two scenes with respective sizes $2360 \times 600$ and $2300 \times 600$ pixels, which have been previously used in [4], [18], and which are formed of $L=2$ images acquired within a 5 years interval (see Figures 1 and 2). The azimuthal




---

TABLE V POWER FOR DIFFERENT VALUES OF $\sigma^{2}$ (CHANGE OF SUBSPACE SCENARIO)


Fig. 1. Scene 1 (Pauli representation) at two different times and its ground truth
resolution is approximately 0.6 m while the distance resolution is 1.67 m . The dimension of each pixel, which was initially of $M=3$, has been increased to $M=12$ using the wavelet decomposition technique of [29]. Local patches of sizes $5 \times 5$ centered around each pixel under test are used for estimation, that is $N_{1}=N_{2}=25$. In Figure 3, the ratio

$$
r(k)=\frac{\mathbb{E}\left[\sum_{i=1}^{k} \lambda_{i}\left(\hat{\mathbf{R}}_{1}\right)\right]}{\mathbb{E}\left[\operatorname{tr}\left(\hat{\mathbf{R}}_{1}\right)\right]}
$$

is plotted for both scenes, where the expectations are estimated by a sample mean over all the local patches. The rank $K$ is set to 5 in the following to reach a ratio of $r(K) \gtrsim 95 \%$.

In Figure 4 are plotted the ROC curves for scenes 1 and 2, where we have compared the performance of the proposed test statistic (30), the GLR, the GLR-LR and the method of [18]. We observe some improvement of the proposed test statistic for type I errors greater than $15 \%$ for the scene 1 or greater than $5 \%$ for the scene 2 .

# VI. CONCLUSION 

In this paper, the problem of covariance equality testing in low-rank Gaussian models has been studied. A new test statistic has been proposed, which is based on the asymptotic behaviour of the largest eigenvalues of certain Wishart matrices in the high-dimensional regime where the dimension of the observations and the number of samples both converge to infinity at the same rate. In particular, it is shown that the

Fig. 2. Scene 2 (Pauli representation) at two different times and its ground truth
(a) Scene 1
(b) Scene 2

Fig. 3. Ratio $k \mapsto r(k)$ for both scenes

(a) Scene 1

(b) Scene 2

Fig. 4. ROC plots for the two scenes




---

proposed statistic has a controlled type I error in the highdimensional regime. Simulations on both synthetic and real datasets have demonstrated that the proposed test statistic is relevant compared to other alternative approaches.

# APPENDIX 

Notations. Throughout this Appendix, we use the following notations. For a sequence of random matrices $\left(\mathbf{X}_{n}\right)_{n \geq 1}$, $\mathbf{X}_{n}=o_{\mathbb{P}}(1)$ denotes the convergence of $\left(\left\|\mathbf{X}_{n}\right\|_{2}\right)$ to 0 in probability, while $\mathbf{X}_{n}=O_{\mathbb{P}}(1)$ denotes the tightness of $\left(\left\|\mathbf{X}_{n}\right\|_{2}\right)$, as $n \rightarrow \infty$, where $\|$. $\|_{2}$ stands for the spectral norm. If $\mathbf{X}$ is a random matrix, we denote by $\mathbf{X}^{\circ}=\mathbf{X}-\mathbb{E}[\mathbf{X}]$. Finally, $\mathcal{C}^{1}(U)$ (resp. $\left.\mathcal{C}_{c}^{\infty}(U)\right)$ denotes the set of continuously differentiable functions (resp. infinitely differentiable functions with compact support) defined on an open set $U$.

## A. Useful results around the Marcenko-Pastur distribution

In this section, we provide well-known results on the Stieltjes transform

$$
m(z)=\int_{\mathbb{R}} \frac{d \mu(\lambda)}{\lambda-z}, \quad z \in \mathbb{C} \backslash \mathbb{R}
$$

of the Marcenko-Pastur distribution $\mu$ with parameters $\left(\sigma^{2}, c\right)$ defined in (15), having the interval $\left[x_{-}, x_{+}\right]$as support with $x_{ \pm}=\sigma^{2}(1 \pm \sqrt{c})^{2}$, and which will be of constant use for the proofs of Theorems 1, 2 and Corollary 2 below.

We first recall that the limit $m(x)=\lim _{z \in \mathbb{C}^{+}, z \rightarrow x} m(z)$ exists for all $x \in \mathbb{R} \backslash\left\{x_{-}, x_{+}\right\}$, and that for all $z \in \mathbb{C} \backslash\left\{x_{-}, x_{+}\right\}$, $m(z)$ satisfies the equation:

$$
m(z)=\frac{1+\sigma^{2} c m(z)}{\sigma^{2}-z}\left(1+\sigma^{2} c m(z)\right)=\frac{w(z)}{z\left(\sigma^{2}-w(z)\right)}
$$

with

$$
w(z)=z\left(1+\sigma^{2} c m(z)\right)
$$

Moreover, $m$ is continuously differentiable on $\mathbb{R} \backslash\left\{0, x_{-}, x_{+}\right\}$.
We now provide some results on the function $w$, which plays a central role in describing the behaviour of the largest eigenvalues of $\hat{\mathbf{R}}$. From (59), we observe that for all $z \in \mathbb{C} \backslash\left\{x_{-}, x_{+}\right\}$,

$$
\varphi(w(z))=z
$$

where $\varphi$ is defined as:

$$
\varphi(w)=w\left(1-\frac{\sigma^{2} c}{\sigma^{2}-w}\right)
$$

Function $\varphi$ is increasing on $\left(-\infty, w_{-}\right) \cup\left(w_{+}, \infty\right)$ and decreasing on $\left(w_{-}, \sigma^{2}\right) \cup\left(\sigma^{2}, w_{+}\right)$, with $w_{ \pm}=\sigma^{2}(1 \pm \sqrt{c})$ and $\varphi\left(w_{ \pm}\right)=x_{ \pm}$

Next, we consider the following lemma (see [30]) regarding $w$.

Lemma 2. For all $x \in \mathbb{R} \backslash\left\{x_{-}, x_{+}\right\}, w(x) \in \varphi^{-1}(\{x\})$. Moreover, among the preimages of $x$ under $\varphi$,

- if $x \in\left(x_{-}, x_{+}\right), w(x)$ is the unique one such that $\operatorname{Im}(w(x))>0$
- if $x \in \mathbb{R} \backslash\left[x_{-}, x_{+}\right], w(x)$ is real and is the unique preimage such that $\varphi^{\prime}(w(x))>0$.
Finally, $z \in \mathbb{C} \backslash \mathbb{R}$ implies that $w(z) \in \mathbb{C} \backslash \mathbb{R}$.
Let $\gamma \geq 0$. From Lemma 2, it is easily deduced that the equation $w(x)=\gamma+\sigma^{2}$ admits a solution iff $\gamma>\sigma^{2} \sqrt{c}$, and that the solution is unique and given by

$$
x=\varphi\left(\gamma+\sigma^{2}\right)=\frac{(\gamma+\sigma 2)\left(\gamma+\sigma^{2} c\right)}{\gamma}
$$

Finally, we also have the following result giving various useful formulas. Define $\tilde{m}(z)=-\frac{1}{z\left(1+\sigma^{2} c m(z)\right)}$ and $\tau(z)=$ $z m(z) \tilde{m}(z)$.
Lemma 3. If $\gamma>\sigma^{2} \sqrt{c}$, then we have

$$
\begin{aligned}
m\left(\varphi\left(\gamma+\sigma^{2}\right)\right) & =-\frac{1}{\gamma+\sigma^{2} c} \\
\tilde{m}\left(\varphi\left(\gamma+\sigma^{2}\right)\right) & =-\frac{1}{\gamma+\sigma^{2}} \\
m^{\prime}\left(\varphi\left(\gamma+\sigma^{2}\right)\right) & =\frac{\gamma^{2}}{\left(\gamma+\sigma^{2} c\right)^{2}\left(\gamma^{2}-\sigma^{4} c\right)} \\
\tilde{m}^{\prime}\left(\varphi\left(\gamma+\sigma^{2}\right)\right) & =\frac{\gamma^{2}}{\left(\gamma+\sigma^{2}\right)^{2}\left(\gamma^{2}-\sigma^{4} c\right)} \\
\tau\left(\varphi\left(\gamma+\sigma^{2}\right)\right) & =\frac{1}{\gamma} \\
\tau^{\prime}\left(\varphi\left(\gamma+\sigma^{2}\right)\right) & =-\frac{1}{\gamma^{2}-\sigma^{4} c}
\end{aligned}
$$

## B. Proof of Theorem 1

This proof is based on techniques developed in [21].
1) Some notations: Denote by $\mathbf{e}_{1}, \ldots, \mathbf{e}_{N}$ the column vectors of the standard basis of $\mathbb{C}^{N}$, and let

$$
\mathbf{J}_{1}=\sum_{n=1}^{N_{1}} \mathbf{e}_{n} \mathbf{e}_{n}^{*}
$$

and for $\ell=2, \ldots, L$,

$$
\mathbf{J}_{\ell}=\sum_{n=N_{1}+\ldots+N_{\ell-1}+1}^{N_{1}+\ldots+N_{\ell}} \mathbf{e}_{n} \mathbf{e}_{n}^{*}
$$

We also consider the following eigendecomposition of $\boldsymbol{\Gamma}_{\ell}$

$$
\boldsymbol{\Gamma}_{\ell}=\mathbf{U}_{\ell} \mathbf{D}_{\ell} \mathbf{U}_{\ell}^{*}
$$

with
$\mathbf{U}_{\ell} \quad M \times K \quad$ isometric matrix
and
$\mathbf{D}_{\ell}=\operatorname{diag}\left(\lambda_{1}\left(\boldsymbol{\Gamma}_{\ell}\right), \ldots, \lambda_{K}\left(\boldsymbol{\Gamma}_{\ell}\right)\right)$
2) Linearization: Let $\mathbf{Y}$ be the $M \times N$ matrix given by $\mathbf{Y}=\left[\mathbf{y}_{1,1}, \ldots,


---

while a.s.

$$
\limsup _{M \rightarrow \infty} \lambda_{\mathrm{KL}+1}(\hat{\mathbf{R}}) \leq \limsup _{M \rightarrow \infty} \lambda_{1}\left(\frac{1}{N} \mathbf{W} \mathbf{W}^{*}\right)=x_{+}
$$

To study the remaining eigenvalues of $\hat{\mathbf{R}}$, we use the linearization trick which consists in studying the following Hermitian block matrix

$$
\check{\mathbf{Y}}=\left[\begin{array}{cc}
\mathbf{0} & \frac{1}{\sqrt{N}} \mathbf{Y} \\
\frac{1}{\sqrt{N}} \mathbf{Y}^{*} & \mathbf{0}
\end{array}\right]
$$

for which it is well-known that [32, Th. 7.3.7]

$$
\operatorname{sp}(\check{\mathbf{Y}})=\left( \pm \sqrt{\lambda_{k}(\hat{\mathbf{R}})}\right) \cup\{0\} .
$$

3) Asymptotics for the characteristic polynomial of $\check{\mathbf{\mathbf { Y }}}$ : Obviously, we have:

$$
\check{\mathbf{Y}}=\mathbf{B} \check{\mathbf{I}} \mathbf{B}^{*}+\check{\mathbf{W}}
$$

where $\mathbf{B}, \check{\mathbf{I}}$ and $\check{\mathbf{W}}$ are given by:

$$
\mathbf{B}=\left[\begin{array}{cc}
\boldsymbol{\Omega} & \mathbf{0} \\
\mathbf{0} & \frac{1}{\sqrt{N}} \mathbf{S}
\end{array}\right], \quad \check{\mathbf{I}}=\left[\begin{array}{cc}
\mathbf{0} & \mathbf{I} \\
\mathbf{I} & \mathbf{0}
\end{array}\right], \quad \check{\mathbf{W}}=\left[\begin{array}{cc}
\mathbf{0} & \frac{1}{\sqrt{N}} \mathbf{W} \\
\frac{1}{\sqrt{N}} \mathbf{W}^{*} & \mathbf{0}
\end{array}\right]
$$

Let $\epsilon>0$ and let $D_{\epsilon}$ the $\epsilon$-neighborhood in $\mathbb{C}$ of the set $D=$ $\left[x_{-}, x_{+}\right]$. Let $\mathcal{K}$ be a compact subset of $\mathbb{C} \backslash\left(\bar{D}_{\epsilon} \cup(-\infty, 0)\right)$. Then (see again [31]), with probability one for all large $M$,

$$
\operatorname{sp}(\check{\mathbf{W}}) \cap \sqrt{\mathcal{K}}=\emptyset
$$

and the following factorization

$$
\operatorname{det}(\check{\mathbf{Y}}-\sqrt{z} \mathbf{I})=\operatorname{det}(\check{\mathbf{W}}-\sqrt{z} \mathbf{I}) \operatorname{det}(\check{\mathbf{I}}) \hat{P}(z)
$$

where

$$
\hat{P}(z)=\operatorname{det}(\check{\mathbf{I}}+\hat{\Xi}(z))
$$

and $\hat{\Xi}(z)=\mathbf{B}^{*}(\check{\mathbf{W}}-\sqrt{z} \mathbf{I})^{-1} \mathbf{B}$, holds for all $z \in \mathcal{K}$. Then from the block matrix inversion formula, we have

$$
\hat{\Xi}(z)=\left[\begin{array}{cc}
\sqrt{z} \boldsymbol{\Omega}^{*} \mathbf{Q}(z) \boldsymbol{\Omega} & \frac{1}{N} \boldsymbol{\Omega}^{*} \mathbf{Q}(z) \mathbf{W S} \\
\frac{1}{N} \mathbf{S}^{*} \mathbf{W}^{*} \mathbf{Q}(z) \boldsymbol{\Omega} & \sqrt{z} \frac{1}{N} \mathbf{S}^{*} \tilde{\mathbf{Q}}(z) \mathbf{S}
\end{array}\right]
$$

where $\mathbf{Q}(z)$ and $\tilde{\mathbf{Q}}(z)$ are the resolvent matrices of $\frac{1}{N} \mathbf{W} \mathbf{W}^{*}$ and $\frac{1}{N} \mathbf{W}^{*} \mathbf{W}$ given by

$$
\mathbf{Q}(z)=\left(\frac{1}{N} \mathbf{W} \mathbf{W}^{*}-z \mathbf{I}\right)^{-1}, \tilde{\mathbf{Q}}(z)=\left(\frac{1}{N} \mathbf{W}^{*} \mathbf{W}-z \mathbf{I}\right)^{-1}
$$

We then use the following result.
Proposition 1. We have

$$
\sup _{z \in \mathcal{K}}\left\|\boldsymbol{\Omega}^{*} \mathbf{Q}(z) \boldsymbol{\Omega}-m(z) \boldsymbol{\Omega}^{*} \boldsymbol{\Omega}\right\|_{2} \underset{M \rightarrow \infty}{\mathbb{P}_{M \rightarrow \infty}^{M}}
$$

as well as

and

$$
\sup _{z \in \mathcal{K}}\left\|\frac{1}{N} \mathbf{S}_{k}^{*} \mathbf{W}^{*} \mathbf{Q}(z) \boldsymbol{\Omega}\right\|_{2} \stackrel{\text { a.s. }}{\underset{M \rightarrow \infty}{\longrightarrow}} 0
$$

Proof. Proposition 1 is obtained as a trivial modification of standard results in random matrix theory regarding quadratic forms of resolvents of standard Wishart matrices (see e.g. [33, Sec. 5.5]) and the proof is therefore omitted.

Using Proposition 1, we deduce that:

$$
\sup _{z \in \mathcal{K}}\|\hat{\Xi}(z)-\Xi(z)\|_{2} \quad \stackrel{\text { a.s. }}{\underset{M \rightarrow \infty}{\longrightarrow}} 0
$$

where

$$
\Xi(z)=\left[\begin{array}{cc}
\sqrt{z} m(z) \boldsymbol{\Omega}^{*} \boldsymbol{\Omega} & \mathbf{0} \\
\mathbf{0} & \mathbf{A}(z)
\end{array}\right]
$$

with $\mathbf{A}(z)$ the $K L \times K L$ block diagonal matrix given by

$$
\mathbf{A}(z)=-\frac{1}{\sqrt{z}}\left(1+\sigma^{2} c m(z)\right)\left[\begin{array}{ccc}
\frac{N_{1}}{N} \mathbf{I} & & \\
& \ddots & \\
& & \frac{N_{L}}{N} \mathbf{I}
\end{array}\right]
$$

It is straightforward to check that

$$
\begin{aligned}
\operatorname{det}(\check{\mathbf{I}}+\Xi(z)) & =\operatorname{det}\left(\sqrt{z} m(z) \boldsymbol{\Omega}^{*} \boldsymbol{\Omega} \mathbf{A}(z)-\mathbf{I}\right) \\
& =\operatorname{det}\left(-\frac{m(z)}{1+\sigma^{2} c m(z)} \boldsymbol{\Gamma}-\mathbf{I}\right)
\end{aligned}
$$

where $\boldsymbol{\Gamma}$ is defined in (11). Consequently, from Assumption 2 , one has

$$
\sup _{z \in \mathcal{K}}|\hat{P}(z)-P(z)| \quad \stackrel{\text { a.s. }}{\underset{N \rightarrow \infty}{\longrightarrow}} 0
$$

where $P(z)=\prod_{k=1}^{K L}\left(-\frac{m(z)}{1+\sigma^{2} c m(z)} \gamma_{k}-1\right)$. Using the equation (59), one can rewrite $P(z)$ as $P(z)=$ $\prod_{k=1}^{K L}\left


---

one for all large M. Therefore, getting back to (81) and since $\epsilon$ can be made arbitrarily small, it follows that

$$
\lambda_{k}(\hat{\mathbf{R}}) \xrightarrow[M \rightarrow \infty]{\text { a.s. }} \varphi\left(\gamma_{k}+\sigma^{2}\right)=\frac{\left(\gamma_{k}+\sigma^{2}\right)\left(\gamma_{k}+\sigma^{2} c\right)}{\gamma_{k}}
$$

for all $k=1, \ldots, K L$ such that $\gamma_{k}>\sigma^{2} \sqrt{c}$. Moreover, with probability one for all large $M, \lambda_{k}(\hat{\mathbf{R}}) \in D_{\epsilon}$ for all $k=1, \ldots, K L$ such that $\gamma_{k} \leq \sigma^{2} \sqrt{c}$. Since the empirical spectral distribution $\hat{\mu}$ of $\hat{\mathbf{R}}$ converges a.s. to the MarcenkoPastur distribution as $M \rightarrow \infty$, this further implies that for all $k=1, \ldots, K L$ such that $\gamma_{k} \leq \sigma^{2} \sqrt{c}, \lambda_{k}(\hat{\mathbf{R}}) \xrightarrow[M \rightarrow \infty]{\text { a.s. }} x_{+}$ and similarly $\lambda_{K L+1}(\hat{\mathbf{R}}) \xrightarrow[M \rightarrow \infty]{\text { a.s. }} x_{+}$.

# C. Proof of Theorem 2 

1) Some notations.: Let us first recall that under hypothesis $\mathcal{H}_{0}$, we have $\boldsymbol{\Gamma}_{1}=\ldots=\boldsymbol{\Gamma}_{L}=\boldsymbol{\Gamma}$, and we denote by $\Gamma=\mathbf{U D U}^{*}$ its eigendecomposition with $\mathbf{U}$ a $M \times K$ isometric matrix and $\mathbf{D}=\operatorname{diag}\left(\lambda_{1}(\Gamma), \ldots, \lambda_{K}(\Gamma)\right)$. To unify some notations, define as in the previous section $\mathbf{Y}_{\ell}=$ $\left[\mathbf{y}_{1, \ell}, \ldots, \mathbf{y}_{N_{\ell}, \ell}\right]$ for all $\ell=1, \ldots, L$ so that we have

$$
\mathbf{Y}_{\ell}=\boldsymbol{\Omega} \mathbf{S}_{\ell}^{*}+\mathbf{W}_{\ell}
$$

where $\boldsymbol{\Omega}=\mathbf{U D}^{1 / 2}, \mathbf{S}_{1}, \ldots, \mathbf{S}_{L}$ are independent matrices such that $\mathbf{S}_{\ell}=\left[\mathbf{s}_{1, \ell}, \ldots, \mathbf{s}_{K, \ell}\right]$ is $N_{\ell} \times K$ with i.i.d. $\mathcal{N}_{\mathbb{C}}(0,1)$ entries, and where $\mathbf{W}_{1}, \ldots, \mathbf{W}_{L}$ are independent matrices with $\mathbf{W}_{\ell}$ having i.i.d. $\mathcal{N}_{\mathbb{C}}\left(0, \sigma^{2}\right)$ entries. We also define $\mathbf{Y}_{0}=\left[\mathbf{Y}_{1}, \ldots, \mathbf{Y}_{L}\right]$ so that

$$
\mathbf{Y}_{0}=\boldsymbol{\Omega} \mathbf{S}_{0}^{*}+\mathbf{W}_{0}
$$

with $\mathbf{S}_{0}=\left[\mathbf{S}_{1}^{*}, \ldots, \mathbf{S}_{L}^{*}\right]^{*}$ and $\mathbf{W}_{0}=\left[\mathbf{W}_{1}, \ldots, \mathbf{W}_{L}\right]$, and write $N_{0}=N_{1}+\ldots+N_{L}$, so that $\hat{\mathbf{R}}_{0}=\frac{\mathbf{Y}_{0} \mathbf{Y}_{0}^{*}}{N_{0}}=\hat{\mathbf{R}}$. Moreover, let $c_{0}=c=\left(\frac{1}{c_{1}}+\ldots+\frac{1}{c_{L}}\right)^{-1}$ and

$$
a=\sigma^{2} \min _{\ell=0, \ldots, L}\left(1-\sqrt{c_{\ell}}\right)^{2}, \quad b=\sigma^{2} \max _{\ell=0, \ldots, L}\left(1+\sqrt{c_{\ell}}\right)^{2}
$$

and consider $\phi \in \mathcal{C}_{c}^{\infty}(\mathbb{R})$ such that $\operatorname{supp}(\phi)=[a-\epsilon, b+\epsilon]$ and $\phi(t)=1$ for all $t \in\left[a-\frac{\epsilon}{2}, b+\frac{\epsilon}{2}\right]$, where $\epsilon<a$. The following quantity defined as

$$
\chi=\prod_{\ell=0}^{L} \operatorname{det} \phi\left(\frac{\mathbf{W}_{\ell} \mathbf{W}_{\ell}^{*}}{N_{\ell}}\right)
$$

verifies $\chi=1$ with probability 1 for all large $M$ from the classical results on the localization of the eigenvalues of Wishart matrices [31]. Recall also the definition of $m$ and $w$ in (58) and (60) respectively and denote for all $\ell=0, \ldots, L$ by $m_{\ell}$ the Stieltjes transform of the Marcenko-Pastur distribution with parameter $\left(c_{\ell}, \sigma^{2}\right)$, as well as for all $z \in \mathbb{C} \backslash\left[x_{\ell}^{-}, x_{\ell}^{+}\right]$

$$
\begin{aligned}
w_{\ell}(z) & =z\left(1+\sigma^{2} c_{\ell} m_{\ell}(z)\right) \\
\tilde{m}_{\ell}(z) & =-\frac{1}{z\left(1+\sigma^{2} c_{\ell} m_{\ell}(z)\right)} \\
\tau_{\ell}(z) & =z m_{\ell}(z) \tilde{m}_{\ell}(z)
\end{aligned}
$$

with $x_{\ell}^{ \pm}=\sigma^{2}\left(1 \pm \sqrt{c_{\ell}}\right)^{2}$.
2) Characteristic Polynomials Approximation: The first step of the proof consists in using the trick from [34] whose main idea is to relate the cumulative distribution function of the spiked eigenvalues with the determinant of certain random matrices.

Using Theorem 1 and the same arguments used to obtain the factorization (81) and (83) in Appendix B, we have that $\lambda_{1}\left(\hat{\mathbf{R}}_{\ell}\right), \ldots, \lambda_{K}\left(\hat{\mathbf{R}}_{\ell}\right)$ are the zeros of

$$
\hat{P}_{\ell}(z)=\operatorname{det}\left(\mathbb{I}+\hat{\Xi}_{\ell}(z)\right)
$$

for all $\ell \in\{0, \ldots, L\}$, with probability one for all large $M$, with

$$
\hat{\Xi}_{\ell}(z)=\left[\begin{array}{cc}
\sqrt{z} \boldsymbol{\Omega}^{*} \mathbf{Q}_{\ell}(z) \boldsymbol{\Omega} \chi & \frac{1}{N_{\ell}} \boldsymbol{\Omega}^{*} \mathbf{Q}_{\ell}(z) \mathbf{W}_{\ell} \mathbf{S}_{\ell} \chi \\
\frac{1}{N_{\ell}} \mathbf{S}_{\ell}^{*} \mathbf{W}_{\ell}^{*} \mathbf{Q}_{\ell}(z) \boldsymbol{\Omega} \chi & \sqrt{z} \frac{1}{N_{\ell}} \mathbf{S}_{\ell}^{*} \tilde{\mathbf{Q}}_{\ell}(z) \mathbf{S}_{\ell} \chi
\end{array}\right]
$$

where

$$
\mathbf{Q}_{\ell}(z)=\left(\frac{\mathbf{W}_{\ell} \math


---

From (108) and Proposition 2, it is clear that we have to study a CLT for the following generic quantity

$$
\eta=\sum_{\ell=0}^{L} \sum_{k=1}^{K}\left(\beta_{1, k, \ell} \eta_{1, k, \ell}+\beta_{2, k, \ell} \eta_{2, k, \ell}+\operatorname{Re}\left(\beta_{3, k, \ell} \eta_{3, k, \ell}\right)\right)
$$

where $\left(\beta_{i, k, \ell}\right)_{\substack{i=1,2 \\ k=1, \ldots, K \\ \ell=0, \ldots, L}} \in \mathbb{R}^{2 K(L+1)}$ and $\left(\beta_{3, k, \ell}\right)_{\substack{k=1, \ldots, K \\ \ell=0, \ldots, L}} \in$ $\mathbb{C}^{K(L+1)}$
3) Central Limit Theorem: Let us consider the characteristic function $\Psi(u)=\mathbb{E}[\xi(u)]$, with $\xi(u)=\exp (\mathrm{i} u \eta)$. Our approach consists in deriving a perturbed differential equation for $\Psi$ as shown in the following proposition. Let bdiag () denotes the block diagonal operator. Define $\mathbf{K}=\operatorname{bdiag}\left(\mathbf{K}_{1}, \ldots, \mathbf{K}_{K}\right)$ with $\mathbf{K}_{k}=\operatorname{bdiag}\left(\mathbf{K}_{1, k}, \ldots, \mathbf{K}_{4, k}\right)$ and where $\left(\mathbf{K}_{i, k}\right)_{i=1, \ldots, 4}$ are $(L+1) \times(L+1)$ symmetric matrices with entries given by

$$
\begin{gathered}
{\left[\mathbf{K}_{1, k}\right]_{\ell+1, \ell^{\prime}+1}= \begin{cases}\frac{\sigma^{4} c_{\ell}}{\left(\gamma_{k}+\sigma^{2} c_{\ell}\right)^{2}\left(\gamma_{k}^{2}-\sigma^{4} c_{\ell}\right)} & \text { if } \ell=\ell^{\prime} \\
\frac{\sigma^{4} c_{0}}{\left(\gamma_{k}+\sigma^{2} c_{0}\right)\left(\gamma_{k}+\sigma^{2} c_{\ell^{\prime}}\right)\left(\gamma_{k}^{2}-\sigma^{4} c_{0}\right)} & \text { if } \ell=0<\ell^{\prime} \\
0 & \text { if } 0<\ell<\ell^{\prime}\end{cases} } \\
{\left[\mathbf{K}_{2, k}\right]_{\ell+1, \ell^{\prime}+1}= \begin{cases}\frac{c_{\ell}}{\left(\gamma_{k}+\sigma^{2}\right)^{2}\left(\gamma_{k}^{2}-\sigma^{4} c_{\ell}\right)} & \text { if } \ell=\ell^{\prime} \\
\frac{c_{0}}{\left(\gamma_{k}+\sigma^{2}\right)^{2}\left(\gamma_{k}^{2}-\sigma^{4} c_{0}\right)} & \text { if } \ell=0<\ell^{\prime} \\
0 & \text { if } 0<\ell<\ell^{\prime}\end{cases} }
\end{gathered}
$$

and for $i \in\{3,4\}$,

$$
\left[\mathbf{K}_{i, k}\right]_{\ell+1, \ell^{\prime}+1}= \begin{cases}\frac{1}{2} \frac{\sigma^{2} c_{\ell}}{\gamma_{k}^{2}-\sigma^{4} c_{\ell}} & \text { if } \ell=\ell^{\prime} \\ \frac{1}{2} \frac{\sigma^{2} c_{0}}{\gamma_{k}^{2}-\sigma^{4} c_{0}} & \text { if } \ell=0<\ell^{\prime} \\ 0 & \text { if } 0<\ell<\ell^{\prime}\end{cases}
$$

Denote also $\boldsymbol{\beta}=\left(\beta_{1}^{T}, \ldots, \beta_{K}^{T}\right)^{T}$ with

$$
\begin{aligned}
\beta_{k}= & \left(\beta_{1, k, 0}, \ldots, \beta_{1, k, L}, \beta_{2, k, 0}, \ldots, \beta_{2, k, L}\right. \\
& \left.\operatorname{Re}\left(\beta_{3, k, 0}\right), \ldots, \operatorname{Re}\left(\beta_{3, k, L}\right), \operatorname{Im}\left(\beta_{3, k, 0}\right), \ldots, \operatorname{Im}\left(\beta_{3, k, L}\right)\right)^{T} .
\end{aligned}
$$

Proposition 3. The matrix $\mathbf{K}$ is positive definite and

$$
\Psi^{\prime}(u)=-u \boldsymbol{\beta}^{T} \mathbf{K} \boldsymbol{\beta} \Psi(u)+\frac{\Delta(u)}{\sqrt{M}}
$$

where $\Delta$ is a continuous function such that $|\Delta(u)|<P(u)$ for some polynomial $P$ with positive coefficients independent of $M$.

Proof. The proof is deferred to Appendix E2.
From Proposition 3, by solving the perturbed differential equation in (118), we deduce that

$$
\Psi(u) \underset{M \rightarrow \infty}{\longrightarrow} \exp \left(-\boldsymbol{\beta}^{T} \mathbf{K} \boldsymbol{\beta} \frac{u^{2}}{2}\right)
$$

which of course implies that

$$
\eta \underset{M \rightarrow \infty}{\stackrel{\mathcal{D}}{\longrightarrow}} \mathcal{N}_{\mathbb{R}}\left(0, \boldsymbol{\beta}^{T} \mathbf{K} \boldsymbol{\beta}\right)
$$

The final step of the proof consists in transferring the CLT to the $K$ largest eigenvalues of $\left(\hat{\mathbf{R}}_{\ell}\right)_{\ell=1, \ldots, L}$. From Proposition (2), we have that:

$$
\begin{aligned}
\hat{P}_{\ell}\left(\frac{\rho_{k, \ell}}{\sqrt{M}}\right)= & \frac{1}{\sqrt{M}} \frac{\gamma_{k} \tau_{\ell}^{\prime}\left(\rho_{k, \ell}\right)}{\left(\gamma_{k} \tau_{\ell}\left(\rho_{k, \ell}\right)-1\right)}\left(x-\zeta_{k, \ell}+o_{\mathbb{P}}(1)\right) \\
& \prod_{i \neq k}\left(\gamma_{i} \tau_{\ell}\left(\rho_{k, \ell}\right)-1\right)
\end{aligned}
$$

with

$$
\begin{aligned}
\zeta_{k, \ell}=\frac{1}{\gamma_{k} \tau_{\ell}^{\prime}\left(\rho_{k, \ell}\right)}\left(2 \sqrt{\gamma_{k}} \operatorname{Re}\left(\eta_{3, k, \ell}\right)\right. & -\left.\gamma_{k} \rho_{k, \ell} \tilde{m}_{\ell}\left(\rho_{k, \ell}\right) \eta_{1, k, \ell}\right. \\
& \left.-\gamma_{k} \rho_{k, \ell} m_{\ell}\left(\rho_{k, \ell}\right) \eta_{2, k, \ell}\right)
\end{aligned}
$$

Thus, going back to (108), we get

$$
\begin{aligned}
\mathbb{P}\left(\bigcap_{k=1}^{K}\right. & \left.\bigcap_{\ell=0}^{L}\left\{\sqrt{M}\left(\lambda_{k}\left(\hat{\mathbf{R}}_{\ell}\right)-\rho_{k, \ell}\right) \in\left[x_{k, \ell}, y_{k, \ell}\right]\right\}\right) \\
& =\math


---

so that $\hat{\lambda}_{k}\left(\hat{\mathbf{R}}_{\ell}\right)>\hat{\sigma}^{2} \sqrt{c_{\ell}}$ with probability one for all large $M$, and therefore $\hat{\gamma}_{k, \ell}+\hat{\sigma}^{2}$ coincides with the largest solution to the equation $\hat{\varphi}_{\ell}(w)=\lambda_{k}\left(\hat{\mathbf{R}}_{\ell}\right)$. From Lemma 2, we deduce that

with probability one for all large $M$, where $\hat{w}_{\ell}(z)=z\left(1+\hat{\sigma}^{2} c_{\ell} \hat{m}_{\ell}(z)\right)$ with $\hat{m}_{\ell}$
the Stieltjes transform of the Marcenko-Pastur distribution with parameter $\left(\hat{\sigma}^{2}, c_{\ell}\right)$. It is easy to see that $\hat{\sigma}^{2}=\sigma^{2}+O_{P}\left(\frac{1}{M}\right)$ and:

$$
\hat{m}_{\ell}\left(\hat{\lambda}_{k}\left(\hat{\mathbf{R}}_{\ell}\right)\right)=m_{\ell}\left(\hat{\lambda}_{k}\left(\hat{\mathbf{R}}_{\ell}\right)\right)+O_{P}\left(\frac{1}{M}\right)
$$

Therefore, we deduce that

$$
\hat{\gamma}_{k, \ell}=w_{\ell}\left(\hat{\lambda}_{k}\left(\hat{\mathbf{R}}_{\ell}\right)\right)-\sigma^{2}+O_{P}\left(\frac{1}{M}\right)
$$

As $w_{\ell}\left(\varphi_{\ell}\left(\gamma_{k}+\sigma^{2}\right)\right)=\gamma_{k}+\sigma^{2}$ and $w_{\ell}$ is differentiable at point $\gamma_{k}+\sigma^{2}$, a straightforward use of the delta-method provides
$\sqrt{M}\left(\hat{\gamma}_{k, \ell}-\gamma_{k}\right) \stackrel{\mathcal{D}}{\mathcal{G}} \ell=0, \ldots, L \quad k=1, \ldots, K \quad \mathcal{N}_{\mathbb{R}^{K(L+1)}}(\mathbf{0}, \mathbf{G} \Theta \mathbf{G})$,
where $\mathbf{G}=\operatorname{diag}\left(\left(w_{\ell}^{\prime}\left(\varphi_{\ell}\left(\gamma_{k}+\sigma^{2}\right)\right)\right)_{\substack{\ell=0, \ldots, L \\ k=1, \ldots, K}}\right)$. Noticing that $w_{\ell}^{\prime}\left(\varphi_{\ell}\left(\gamma_{k}+\sigma^{2}\right)\right)=\frac{\gamma_{k}^{2}}{\gamma_{k}^{2}-\sigma^{2}} c_{\ell}$ from Lemma 3, we end up with $\mathbf{G} \boldsymbol{\Theta} \mathbf{G}=\boldsymbol{\Omega}$, where $\boldsymbol{\Omega}$ is given in the statement of Corollary 2. Another immediate use of the delta-method allows to transfer the CLT from $\left(\hat{\gamma}_{k, \ell}\right)_{\substack{\ell=0, \ldots, L \\ k=1, \ldots, K}}$ to $\hat{\gamma}$.

# E. Additional proofs 

1) Proof of Proposition 2: It is easy to see using Proposition 1 that for all $x \in \mathbb{R}$,

$$
\hat{\Xi}_{\ell}\left(\rho_{k, \ell}+\frac{\underline{x}}{\sqrt{M}}\right)=\left(\begin{array}{cc}
\sqrt{\rho_{k, \ell}} m_{\ell}\left(\rho_{k, \ell}\right) \mathbf{D} & \mathbf{0} \\
\mathbf{0} & \sqrt{\rho_{k, \ell}} \tilde{m}_{\ell}\left(\rho_{k, \ell}\right) \mathbf{I}
\end{array}\right)+\boldsymbol{\Delta}
$$

where
$\boldsymbol{\Delta}=\left(\begin{array}{cc}\sqrt{\rho_{k, \ell}} \boldsymbol{\Omega}^{*}\left(\mathbf{Q}_{\ell}\left(\rho_{k, \ell}\right) \boldsymbol{\chi}\right) \circ \boldsymbol{\Omega} & \frac{1}{N_{\ell}} \boldsymbol{\Omega}^{*} \mathbf{Q}_{\ell}\left(\rho_{k, \ell}\right) \boldsymbol{\chi} \mathbf{W}_{\ell} \mathbf{S}_{\ell} \\ \frac{1}{N_{\ell}} \mathbf{S}_{\ell}^{*} \mathbf{W}_{\ell}^{*} \mathbf{Q}_{\ell}\left(\rho_{k, \ell}\right) \boldsymbol{\chi} \boldsymbol{\Omega} & \sqrt{\rho_{k, \ell}} \frac{1}{N_{\ell}}\left(\mathbf{S}_{\ell}^{*} \tilde{\mathbf{Q}}_{\ell}\left(\rho_{k, \ell}\right) \mathbf{S}_{\ell} \boldsymbol{\chi}\right) \circ\end{array}\right)$
$+\frac{\underline{x}}{\sqrt{M}}\left(\begin{array}{cc}h_{\ell}\left(\rho_{k, \ell}\right) \mathbf{D} & \mathbf{0} \\ \mathbf{0} & \tilde{h}_{\ell}\left(\rho_{k, \ell}\right) \mathbf{I}\end{array}\right)+o_{P}\left(\frac{1}{\sqrt{M}}\right)$
with $h_{\ell}(z)=\frac{m_{\ell}(z)}{2 \sqrt{z}}+\sqrt{z} m_{\ell}^{\prime}(z)$ and $\tilde{h}_{\ell}(z)=\frac{\tilde{m}_{\ell}(z)}{2 \sqrt{z}}+$ $\sqrt{z} \tilde{m}_{\ell}^{\prime}(z)$. Note that $\|\boldsymbol{\Delta}\|_{2}=O_{P}\left(\frac{1}{\sqrt{M}}\right)$ and we also consider the partition $\boldsymbol{\Delta}=\left(\Delta_{i, j}\right)_{i, j=1,2}$ where each block $\Delta_{i, j}$ is $K \times K$. Consider the event $\mathcal{A}=\left\{\left\|\Delta_{2,2}\right\|_{2}<\sqrt{\rho_{k, \ell}} \tilde{m}_{\ell}\left(\rho_{k, \ell}\right)\right\}$. From the block matrix determinant formula, we have:

$$
\hat{P}_{\ell}\left(\rho_{k, \ell}+\frac{x}{\sqrt{M}}\right) \mathbf{1}_{\mathcal{A}}=\Phi \operatorname{det}\left(\sqrt{\rho_{k, \ell}} \tilde{m}_{\ell}\left(\rho_{k, \ell}\right) \mathbf{I}+\Delta_{2,2}\right) \mathbf{1}_{\mathcal{A}}
$$

with
$\Phi=\operatorname{det}\left(\begin{array}{ccccc}\sqrt{\rho_{k, \ell}} m_{\ell}\left(\rho_{k, \ell}\right) \mathbf{D}+\boldsymbol{\Delta}_{1,1} & - & \left(\mathbf{I}+\boldsymbol{\Delta}_{2,1}\right) & \left(\sqrt{\rho_{k, \ell}} \tilde{m}_{\ell}\left(\rho_{k, \ell}\right) \mathbf{I}+\boldsymbol{\Delta}_{2,2}\right)^{-1} & \left(\mathbf{I}+\boldsymbol{\Delta}_{1,2}\right)\end{array}\right) \mathbf{1}_{\mathcal{A}}$
Moreover,

$$
\left(\sqrt{\rho_{k, \ell}} \tilde{m}_{\ell}\left(\rho_{k, \ell}\right) \mathbf{I}+\boldsymbol{\Delta}_{2,2}\right)^{-1} \mathbf{1}_{\mathcal{A}}=\left(\mathbf{I} \sqrt{\rho_{k, \ell}} \tilde{m}_{\ell}\left(\rho_{k, \ell


---

so that

$$
\begin{aligned}
& \hat{\mathbb{P}}^{\ell}\left(\rho_{k, \ell}+\frac{x}{\sqrt{M}}\right) \mathbf{1}_{\mathcal{A}}=\left[\frac{\sqrt{\rho_{k, \ell}} \tilde{m}_{\ell}\left(\rho_{k, \ell}\right) \Delta_{1,1}+\bar{\Delta}_{2,2}}{\sqrt{\rho_{k, \ell}} \tilde{m}_{\ell}\left(\rho_{k, \ell}\right)}-\left(\bar{\Delta}_{1,2}+\Delta_{2,1}\right)\right]_{k, k} \\
& \times \prod_{i \neq k}\left(\gamma_{i} \rho_{k, \ell} \underline{m}_{\ell}\left(\rho_{k, \ell}\right) \tilde{m}_{\ell}\left(\rho_{k, \ell}\right)-1\right)+o_{\mathbb{P}}\left(\frac{1}{\sqrt{M}}\right) .
\end{aligned}
$$

Since $\mathbf{1}_{\mathcal{A}}=1+o_{\mathbb{P}}(1)$, we also deduce that

$$
\hat{\mathbb{P}}^{\ell}\left(\rho_{k, \ell}+\frac{x}{\sqrt{M}}\right) \mathbf{1}_{\mathcal{A}^{c}}=o_{\mathbb{P}}\left(\frac{1}{\sqrt{M}}\right)
$$

and using Assumption 2 leads to the result of Proposition 2.
2) Proof of Proposition 3: The proof makes use of wellknown techniques specific to the Gaussian distribution, namely the Stein's lemma and the Poincaré's inequality which we recall below and which have already been exploited in e.g. [35], [15], [24]. Therefore, we only give the main steps of the proof and skip some details of the computations.
a) Useful tools.: A function $f: \mathbb{C}^{n} \rightarrow \mathbb{C}$ is said to be $\mathcal{C}^{1}\left(\mathbb{C}^{n}\right)$ if $f(\mathbf{z})=\tilde{f}(\operatorname{Re}(\mathbf{z}), \operatorname{Im}(\mathbf{z}))$ with $\tilde{f} \in \mathcal{C}^{1}\left(\mathbb{R}^{2 n}\right)$. Moreover, we also recall the definition of the standard complex differential operators

$$
\begin{aligned}
& \frac{\partial f}{\partial z_{k}}(\mathbf{z})=\frac{1}{2}\left(\frac{\partial \tilde{f}}{\partial x_{k}}(\mathbf{x}, \mathbf{y})-i \frac{\partial \tilde{f}}{\partial y_{k}}(\mathbf{x}, \mathbf{y})\right) \\
& \frac{\partial f}{\partial \bar{z}_{k}}(\mathbf{z})=\frac{1}{2}\left(\frac{\partial \tilde{f}}{\partial x_{k}}(\mathbf{x}, \mathbf{y})+i \frac{\partial \tilde{f}}{\partial y_{k}}(\mathbf{x}, \mathbf{y})\right)
\end{aligned}
$$

with $\mathbf{x}=\operatorname{Re}(\mathbf{z})$ and $\mathbf{y}=\operatorname{Im}(\mathbf{z})$.
Lemma 4 (Stein's lemma). Let $\mathbf{w} \sim \mathcal{N}_{\mathbb{C}^{n}}(\mathbf{0}, \mathbf{I})$ and $f \in$ $\mathcal{C}^{1}\left(\mathbb{C}^{n}\right)$, assumed polynomially bounded together with its partial derivatives. Then for all $k=1, \ldots, n$,

$$
\mathbb{E}\left[f(\mathbf{w}) w_{k}\right]=\mathbb{E}\left[\frac{\partial f}{\partial \bar{w}_{k}}(\mathbf{w})\right], \mathbb{E}\left[f(\mathbf{w}) \bar{w}_{k}\right]=\mathbb{E}\left[\frac{\partial f}{\partial w_{k}}(\mathbf{w})\right]
$$

Lemma 5 (Poincaré inequality). Let $\mathbf{w} \sim \mathcal{N}_{\mathbb{C}^{n}}(\mathbf{0}, \mathbf{I})$ and $f \in \mathcal{C}^{1}\left(\mathbb{C}^{n}\right)$, assumed polynomially bounded together with its partial derivatives. Then,

$$
V[f(\mathbf{w})] \leq \sum_{k=1}^{n}\left(\mathbb{E}\left|\frac{\partial f}{\partial w_{k}}(\mathbf{w})\right|^{2}+\mathbb{E}\left|\frac{\partial f}{\partial \bar{w}_{k}}(\mathbf{w})\right|^{2}\right)
$$

For ease of reading, we introduce the following differentiation operators with respect to the entries of the $M \times N_{\ell}$ matrix $\mathbf{W}_{\ell}$, which will be constantly used in the derivations below,

$$
\partial_{i, j}^{(\ell)}=\frac{\partial}{\partial\left[\mathbf{W}_{\ell}\right]_{i, j}}, \bar{\partial}_{i, j}^{(\ell)}=\frac{\partial}{\partial\left[\overline{\mathbf{W}_{\ell}}\right]_{i, j}}
$$

We will also need the following auxiliary result (see [33]) related to the quantity $\chi$ defined in (100).

Lemma 6. For all $p \in \mathbb{N}$ and $r \in \mathbb{N}, \mathbb{E}\left[\chi^{r}\right]=1+\mathcal{O}\left(\frac{1}{N^{p}}\right)$ and for $\ell \in\{0, \ldots, L\}$ and for any $i \in\{1, \ldots, M\}, j \in$ $\{1, \ldots, N_{\ell}\}$

$$
\mathbb{E}\left[\partial_{i, j}^{(\ell)} \chi^{r}\right]=\mathcal{O}\left(\frac{1}{N^{p}}\right) \text { and } \mathbb{E}\left[\bar{\partial}_{i, j}^{(\ell)} \chi^{r}\right]=\mathcal{O}\left(\frac{1}{N^{p}}\right)
$$

Lemma 6 shows in particular that the presence of the regularization term $\chi$ can be removed from expectations, up to an error term of arbitrary polynomial decay.
In the following, $\Delta$ is a generic notation for a continuous function such that $|\Delta(u)|<P(u)$ for some polynomial $P$ with positive coefficients independent of $M$, and whose value may change from one line to another.
b) Development of $\Psi^{\prime}$ : Write

$$
\begin{aligned}
\Psi^{\prime}(u)=i \sum_{k=1}^{K} \sum_{\ell=0}^{L} \mathbb{E} & {\left[\left(\beta_{1, k, \ell} \eta_{1, k, \ell}+\beta_{2, k, \ell} \eta_{2, k, \ell}\right)\right.} \\
& \left.+2 \operatorname{Re}\left(\beta_{3, k, \ell} \eta_{3, k, \ell}\right)\right) \xi(u)\right]
\end{aligned}
$$

In the following, we only provide some details for the development of $\mathbb{E}\left[\eta_{1, k, 0} \xi(u)\right]$, as the other terms can be obtained similarly. Using the resolvent identity, we start by writing

$$
\mathbb{E}\left[\eta_{1, k, 0} \xi(u)\right]=\frac{\sqrt{M}}{\rho_{k, 0}} \mathbb{E}\left[\left(\frac{\mathbf{u}_{k}^{*} \mathbf{Q}_{0}\left(\rho_{k, 0}\right) \mathbf{W}_{0} \mathbf{W}_{0}^{*}}{N_{0}} \mathbf{u}_{k} \chi\right) \circ \xi(u)\right]
$$

Next, we apply Stein's lemma, Poincaré's inequality and Lemma 6 to obtain

$$
\begin{aligned}



---

with

$$
\begin{aligned}
\kappa_{k, \ell} & = \begin{cases}\frac{\sigma^{2} m_{0}\left(\rho_{k, 0}\right) m_{0}^{\prime}\left(\rho_{k, 0}\right)}{1+\sigma^{2} c_{0} m_{0}\left(\rho_{k, 0}\right)} & \text { if } \ell=0 \\
\frac{\sigma^{2} m_{\ell}\left(\rho_{k, \ell}\right) m_{0}\left(\rho_{k, 0}\right)\left(1+\sigma^{2} c_{0} m_{0}\left(\rho_{k, 0}\right)\right)}{\sigma^{2}-\rho_{k, \ell}\left(1+\sigma^{2} c_{0} m_{0}\left(\rho_{k, 0}\right)\right)\left(1+\sigma^{2} c_{\ell} m_{\ell}\left(\rho_{k, \ell}\right)\right)} & \text { if } \ell \geq 1\end{cases} \\
& = \begin{cases}-\frac{\sigma^{2} \gamma_{k}}{\left(\gamma_{k}+\sigma^{2} c_{0}\right)^{2}\left(\gamma_{k}^{2}-\sigma^{2} c_{0}\right)} & \text { if } \ell=0 \\
-\frac{\sigma^{2} \gamma_{k}}{\left(\gamma_{k}+\sigma^{2} c_{0}\right)\left(\gamma_{k}+\sigma^{2} c_{\ell}\right)\left(\gamma_{k}^{2}-\sigma^{2} c_{0}\right)} & \text { if } \ell \geq 1\end{cases}
\end{aligned}
$$

where the second equality in the expression of $\theta_{k, \ell}$ can be obtained with Lemma 3. Moreover,

$$
\begin{aligned}
& \sum_{i, j} \mathbb{E}\left[\left[u_{k}^{*} \mathbf{Q}_{0}\left(\rho_{k, 0}\right)\right]_{i}\left[\mathbf{W}_{\ell} \mathbf{u}_{k}\right]_{j} \chi_{i, j}^{(0)}\left\{\eta_{2, k^{\prime}, \ell}\right\} \xi(u)\right] \\
& =-\frac{\sqrt{M}}{N_{\ell}^{2}} \mathbb{E}\left[u_{k}^{*} \mathbf{Q}_{0}\left(\rho_{k, 0}\right) \mathbf{W}_{\ell} \tilde{\mathbf{Q}}_{\ell}\left(\rho_{k^{\prime}, \ell}\right) \mathbf{s}_{k^{\prime}, \ell}\right. \\
& \left.\times \mathbf{s}_{k^{\prime}, \ell}^{*} \tilde{\mathbf{Q}}_{\ell}\left(\rho_{k^{\prime}, \ell}\right) \mathbf{W}_{\ell}^{*} \mathbf{u}_{k} \chi \xi(u)\right] \\
& \left.+\frac{\Delta(u) \sqrt{M}}{} \frac{\Delta(u)}{\sqrt{M}}
\end{aligned}
$$

and

$$
\begin{aligned}
& \sum_{i, j} \mathbb{E}\left[\left[u_{k}^{*} \mathbf{Q}_{0}\left(\rho_{k, 0}\right)\right]_{i}\left[\mathbf{W}_{\ell} \mathbf{u}_{k}\right]_{j} \chi_{i, j}^{(0)}\left\{\eta_{3, k^{\prime}, \ell}\right\} \xi(u)\right] \\
= & -\frac{\sqrt{M}}{N_{\ell}} \mathbb{E}\left[u_{k}^{*} \mathbf{Q}_{0}\left(\rho_{k, 0}\right) \mathbf{Q}_{\ell}\left(\rho_{k^{\prime}, \ell}\right) \mathbf{W}_{\ell} \mathbf{s}_{k^{\prime}, \ell}\right. \\
& \left.\times \mathbf{u}_{k^{\prime}}^{*} \mathbf{Q}_{\ell}\left(\rho_{k^{\prime}, \ell}\right) \mathbf{W}_{\ell} \frac{\mathbf{W}_{\ell}^{*}}{N_{\ell}} \mathbf{u}_{k} \chi \xi(u)\right] \\
& \left.+\frac{\Delta(u) \sqrt{M}}{} \frac{\Delta(u)}{\sqrt{M}}
\end{aligned}
$$

Finally, using again Lemma 3, we obtain

$$
\begin{aligned}
\mathbb{E} & {\left[\eta_{1, k, 0} \xi(u)\right] } \\
& =i u \sigma^{2} c_{0} \sum_{\ell=0}^{L} \beta_{1, k, \ell} \frac{\kappa_{k, \ell}}{\rho_{k, 0}\left(1+\sigma^{2} c_{0} m_{0}\left(\rho_{k, 0}\right)\right)}-\sigma^{2} \Psi(u)+\frac{\Delta(u)}{\sqrt{M}} \\
& =-i u\left(\beta_{1, k, 0} \frac{\sigma^{4} c_{0}}{\left(\gamma_{k}+\sigma^{2} c_{0}\right)^{2}\left(\gamma_{k}^{2}-\sigma^{2} c_{0}\right)}\right. \\
& \left.+\sum_{\ell=1}^{L} \beta_{1, k, \ell} \frac{\sigma^{4} c_{0}}{\left(\gamma_{k}+\sigma^{2} c_{0}\right)\left(\gamma_{k}+\sigma^{2} c_{\ell}\right)\left(\gamma_{k}^{2}-\sigma^{2} c_{0}\right)}\right) \Psi(u)+\frac{\Delta(u)}{\sqrt{M}}
\end{aligned}
$$

Using similar computations for the remaining terms $\left(\mathbb{E}\left[\eta_{i, k, \ell} \xi(u)\right]\right)_{\substack{\ell \geq 1 \\ i=2,3}}$ in $\Psi^{\prime}(u)$, we finally obtain the result of Proposition 3.

# REFERENCES 

[1] R. Beisson, P. Vallet, A. Giremus, and G. Ginolhac, "Change Detection in The Covariance Structure of High-Dimensional Gaussian Low-Rank Models," in Statistical Signal Processing Workshop (SSP). IEEE, 2021, pp. 421-425.
[2] K. Conradsen, A. Nielsen, J. Schou, and H. Skriver, "A test statistic in the complex Wishart distribution and its application to change detection in polarimetric SAR data," IEEE Trans. Geosci. Remote Sens., vol. 41, no. 1, pp. 4-19, 2003.
[3] D. Ciuonzo, V. Carotenuto, and A. De Maio, "On multiple covariance equality testing with application to SAR change detection," IEEE Trans. on Signal Process., vol. 65, no. 19, pp. 5078-5091, 2017.
[4] A. Mian, G. Ginolhac, J.-P. Ovarlez, and A. Atto, "New robust statistics for change detection in time series of multivariate SAR images," IEEE Trans. Signal Process., vol. 67, no. 2, pp. 520-534, 2018.
[5] A. Mian, A. Collas, A. Breloy, G. Ginolhac, and J.-P. Ovarlez, "Robust low-rank change detection for multivariate sar image time series," IEEE J. Sel. Top. Appl. Earth Obs. Remote Sens., vol. 13, pp. 3545-3556, 2020.
[6] R. Liu, L. Liu, D. He, W. Zhang, and E. G. Larsson, "Detection of abrupt change in channel covariance matrix for multi-antenna communication," in Global Communications Conference (GLOBECOM). IEEE, 2021.
[7] P. Galeano and D. Peña, "Covariance changes detection in multivariate time series," J. Stat. Plan. Inference, vol. 137, no. 1, pp. 194-211, 2


---

[28] P. Stoica and R. Moses, Spectral analysis of signals. Pearson Prentice Hall, 2005, vol. 452.
[29] A. Mian, J.-P. Ovarlez, A. Atto, and G. Ginolhac, "Design of new wavelet packets adapted to high-resolution SAR images with an application to target detection," IEEE Trans. Geosci. Remote Sens., vol. 57, no. 6, pp. 3919-3932, 2019.
[30] X. Mestre, "On the asymptotic behavior of the sample estimates of eigenvalues and eigenvectors of covariance matrices," IEEE Trans. Signal Process., vol. 56, no. 11, pp. 5353-5368, 2008.
[31] S. Geman, "A limit theorem for the norm of random matrices," Ann. Prob., pp. 252-261, 1980.
[32] R. Horn and C. Johnson, Matrix analysis. Cambridge university press, 2012.
[33] W. Hachem, P. Loubaton, X. Mestre, J. Najim, and P. Vallet, "Large information plus noise random matrix models and consistent subspace estimation in large sensor networks," Random Matrices: Theory Appl., vol. 1, no. 2, 2012.
[34] F. Benaych-Georges and R. Nadakuditi, "The singular values and vectors of low rank perturbations of large rectangular random matrices," J. Multivariate Anal., vol. 111, no. 0, pp. 120-135, 2012.
[35] W. Hachem, O. Khorunzhiy, P. Loubaton, J. Najim, and L. Pastur, "A new approach for capacity analysis of large dimensional multi-antenna channels," IEEE Trans. Inf. Theory, vol. 54, no. 9, pp. 3987-4004, 2008.




---

