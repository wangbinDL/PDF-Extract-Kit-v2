# A New Statistic for Testing Covariance Equality in High-Dimensional Gaussian Low-Rank Models  

R. B EISSON ,  Student Member, IEEE , P. V ALLET ,  Member, IEEE , A. G IREMUS ,  Member, IEEE , G. G INOLHAC , Member, IEEE  

Abstract —In this paper, we consider the problem of testing equality of the covariance matrices of    $L$   complex Gaussian multivariate time series of dimension    $M.$  . We study the special case where each of the  $L$   covariance matrices is modeled as a rank  $K$   perturbation of the identity matrix, corresponding to a signal plus noise model. A new test statistic based on the estimates of the eigenvalues of the different covariance matrices is proposed. In particular, we show that this statistic is consistent and with controlled type I error in the high-dimensional asymptotic regime where the sample sizes    $N_{1},\dots,N_{L}$   of each time series and the dimension    $M$   both converge to infinity at the same rate, while  $K$   and    $L$   are kept fixed. We also provide some simulations on synthetic and real data (SAR images) which demonstrate significant improvements over some classical methods such as the GLRT, or other alternative methods relevant for the high- dimensional regime and the low-rank model.  

# I. I NTRODUCTION  

D ETECTING changes in the behaviour of multivariate time series is a fundamental problem in many appli- cations going from remote sensing [2], [3], [4], [5] and wireless communications [6] to finance [7], climatology [8] or genomics [9]. In several of those applications, a usual approach consists in modeling the changes using the distribution of the time series, and in particular through an evolution in the structure of the covariance matrix.  

Consider the context of  $M$  -dimensional time series  $\left(\mathbf{y}_{n,1}\right)_{n\in\mathbb{Z}},\cdot\cdot\cdot,\left(\mathbf{y}_{n,L}\right)_{n\in\mathbb{Z}}$  and such that for all  $\ell\in\check{\{1,\dots,L\}}$  ,  

$$
\left(\mathbf{y}_{n,\ell}\right)_{n\in\mathbb{Z}}\overset{\mathrm{i.i.d.}}{\sim}\mathcal{N}_{\mathbb{C}^{M}}\left(\mathbf{0},\mathbf{R}_{\ell}\right),
$$  

where    $\mathcal{N}_{\mathbb{C}^{M}}\left(\mathbf{0},\mathbf{R}_{\ell}\right)$   denotes the z -mean complex normal distribution with covariance matrix  $\mathbf{R}_{\ell}$  . Detecting the changes in the distribution of    $(\mathbf{y}_{n,\ell})_{n\in\mathbb{Z}}$  , for all    $\ell\in\{1,\ldots,L\}$  , can be formalized as the following binary hypothesis test dealing with the equality of the  $L$   covariance matrices    ${\bf R}_{1},\ldots,{\bf R}_{L}$  ,  

$$
\begin{array}{r l}{\mathcal{H}_{0}:}&{\mathbf{R}_{1}=.\,.\,.=\mathbf{R}_{L}}\\ {\mathcal{H}_{1}:}&{\exists(i,j)\in\{1,.\,.\,,L\}^{2}:\mathbf{R}_{i}\neq\mathbf{R}_{j}}\end{array}.
$$  

Assume that for all    $\begin{array}{l l l}{\ell}&{\in}&{\{1,.\,.\,.\,,L\}}\end{array}$  ∈ {  $N_{\ell}$  ons  $\mathbf{y}_{1,\ell},\ldots,\mathbf{y}_{N_{\ell},\ell}$  are available and let  $N=N_{1}+\cdot\cdot\cdot+N_{L}$   · · · . A large class of test statistics widely encountered in the literature [3] involves, provided that    $M<N_{1},\dots,N_{L}$  , linear spectral statistics of the matrices  $\hat{\mathbf{R}}_{\ell}^{-1}\hat{\mathbf{R}}$   of the form:  

$$
S=\sum_{\ell=1}^{L}\frac{N_{\ell}}{N}\frac{1}{M}\sum_{k=1}^{M}\varphi\left(\lambda_{k}(\hat{\bf R}_{\ell}^{-1}\hat{\bf R})\right),
$$  

where    $\lambda_{k}\big(\hat{\mathbf{R}}_{\ell}^{-1}\hat{\mathbf{R}}\big)$  , for all    $k\in\{1,\ldots,M\}$  , are the eigenvalues of the matrix  $\hat{\mathbf{R}}_{\ell}^{-1}\hat{\mathbf{R}}$   with  

$$
\hat{\mathbf{R}}_{\ell}:=\frac{1}{N_{\ell}}\sum_{n=1}^{N_{\ell}}\mathbf{y}_{n,\ell}\mathbf{y}_{n,\ell}^{*},
$$  

denoting the sample covariance matrix (SCM) associated with  $\mathbf{R}_{\ell}$  and  

$$
\hat{\bf R}=\sum_{\ell=1}^{L}\frac{N_{\ell}}{N}\hat{\bf R}_{\ell}.
$$  

In (3),    $\varphi$   denotes some continuous function defined on

  $(0,+\infty)$  . In particular, the Generalized Likelihood Ratio

 (GLR) [3] with    $\varphi(x)\,=\,\log(x)$   or the  Nagao  statistic with

  $\varphi(x)\ =\ (x\,-\,1)^{2}$    are included in the class of statistics

 (3). The presence of a change in the covariance is decided by comparing (3) to a threshold    $\epsilon$   chosen to guarantee a n type I error and the null hypothesis    ${\mathcal{H}}_{0}$   is rejected if  $S>\epsilon$  . Moreover, the test statistics based on (3) have the key  distribution of    $S$   under    ${\mathcal{H}}_{0}$   is independent of

  ${\bf R}_{1}=.\,.\,.={\bf R}_{L}$  , which allows to control its type I error.  

However, in practice, the distribution of statistics of type

 (3) under    ${\mathcal{H}}_{0}$   i d only known in a few special cases for finite  $M,N_{1},\ldots,N_{L}$   (e.g. for the GLR, see [10]). To circumvent this issue, approximations in the  low-dimensional (or  la ample size ) regime in which    $N_{1},.\,.\,.\,,N_{L}\ \to\ \infty$  while  $M,L$   are fixed can be derived, see e.g. [11, Th. 10.8.4]. While the latter are meant to be used in practical scenarios where    $N_{1},.\,.\,.\,,N_{L}\quad\gg\quad M$  ≫ , they may not be reliable in contexts involving high-dimensional (large    $M$  ) observations or moderate sample sizes    $N_{1},\dots,N_{L}$  . Indeed, in that high- dimensional case, it is often more reasonable to assume that  $M,N_{1},.\ldots,N_{L}$   are of the same order of magnitude in which case the predictions of the distribution of (3) under  ${\mathcal{H}}_{0}$   in the low-dimensional  regime become irrelevant.  

The context where    $M,N_{1},\dots,N_{L}$   are of the same order of magnitude can be modeled more realistically by the  high- dimensional regime  in which it is assumed that    $M$   converges to infinity together with    $N_{1},\dots,N_{L}$   such that    $\begin{array}{r}{\frac{M}{N_{\ell}}\rightarrow c_{\ell}>0}\end{array}$  , while    $L$   is kept fixed. In this non-standard regime, the asymp- totic distribution of the statistic  $S$   can be derived using random matrix theory techniques (see e.g. [12] for the case    $L=2$  ).  

Moreover, in several applications involving high- dimensional observations, the potential changes in the covariance  $\mathbf{R}_{\ell}$  may only be carried by a low-rank component (see e.g. [13], [14], [15]). This is the case, e.g., in array processing when dealing with a large array of    $M$   sensors and a small number    $K$   of source signals compared to    $M$   [15].  

In that case, we have the model  

$$
\mathbf{R}_{\ell}=\mathbf{T}_{\ell}+\sigma^{2}\mathbf{I},
$$  

with    $\mathbf{T}_{\ell}$  the covariance matrix of rank    $K<M$   of a useful signal and    $\sigma^{2}\mathbf{I}$   the covariance matrix of a spatially white additive noise. When the rank    $K$   remains constant in the high-dimensional regime , the matrices    $\mathbf{R}_{\ell}^{-1}\mathbf{R}_{\ell^{\prime}}$   are fixed rank perturbations of the identity. Using well-known results [16], [17] on the asymptotic spectral distribution of the Fisher type random matrices  $\mathbf{\hat{R}}_{\ell}^{-1}\mathbf{\hat{R}}$  , one can show under both    ${\mathcal{H}}_{0}$   and  $\mathcal{H}_{1}$   that  

$$
S\rightarrow\sum_{\ell=1}^{L}\frac{c}{c_{\ell}}\int_{x_{\ell}^{-}}^{x_{\ell}^{+}}\varphi\left(\frac{c}{c_{\ell}}(1+x)\right)f_{\ell}(x)\mathrm{d}x,
$$  

almost surely (a.s.) where    $c=(c_{1}^{-1}+.\,.\,.+c_{L}^{-1})^{-1}$   and where  $f_{\ell}$  is the so-called  Wachter  distribution given by  

$$
f_{\ell}(x)=\left(\frac{1}{c_{\ell}}-1\right)\frac{\sqrt{(x-x_{\ell}^{-})(x_{\ell}^{+}-x)}}{2\pi x(1+x)}\mathbb{1}_{[x_{\ell}^{-},x_{\ell}^{+}]}(x),
$$  

converges to the same limit under both hypotheses    ${\mathcal{H}}_{0}$   and  $\mathcal{H}_{1}$  , which indicates that test statistics relying on (3) might not be relevant in the  high-dimensional regime  and for the low-rank model in (6).  

So far from our knowledge, the problem of covariance equality testing under low-rank models has not received much attention in the literature. The work of [18] considers the GLRT, under a low-rank Gaussian model, for a covariance h a different alternative hypothesis    $\mathcal{H}_{1}^{\prime}:{\mathbf{R}}_{1}\neq$     ${\bf R}_{2}=.\,.\,.={\bf R}_{L}$  . An extension to the specific case of subspace equality test has also been proposed by the same authors in [19].  

Under the model (6), the information about a potential change is contained in the    $K$   largest eigenvalues and asso- ciated eigenvectors of    $\mathbf{R}_{\ell}$  . Therefore, classical results on the spiked models  for random matrices of the Fisher type [17] can be exploited to characterize the asymptotic behaviour of the extreme eigenvalues of    $(\hat{\mathbf{R}}_{\ell}^{-1}\hat{\mathbf{R}})_{\ell=1,\dots,L}$  , from which infor- mation about a potential change can be extracted. In the same way, the asymptotic behaviour of the largest eigenvalues of the spiked Wishart-type matrices [20]  $\hat{\bf R},({\bf\bar{R}}_{\ell})_{\ell=1,\dots,L}$   convey information about changes in the true covariances    ${\bf R}_{1},\ldots,{\bf R}_{L}$  [1], which can also be exploited to build test statistics relevant for the low-rank model in the high-dimensional regime. This latter option is the path followed in this paper.  

Contributions.  In this paper, we derive a new test statistic, no longer based on the family of statistics    $S$   studied in [3], but which relies on the    $K$   largest eigenvalues of the matrices  $\hat{\mathbf{R}}_{1},.\,.\,.\,,\hat{\mathbf{R}}_{L},\hat{\mathbf{R}}$  . More precisely, the test statistic compares in a certain sense estimates of the eigenvalues of the matrices

  $\pmb{\Gamma}_{1},\dots,\pmb{\Gamma}_{L}$   with estimates of the eigenvalues of the mixture

  $\begin{array}{r}{\pmb{\Gamma}=\sum_{\ell=1}^{L}\frac{N_{\ell}}{N}\pmb{\Gamma}_{\ell}}\end{array}$  . We show that the proposed test statistic is consistent under the high-dimensional regime and the low-rank model (6), and with a controlled asymptotic type I error. To that purpose, the results of [21], which provides the asymptotic distribution of the    $K$   largest eigenvalues of  $\hat{\mathbf{R}}_{\ell}$  for a fixed    $\ell.$  , are extended to provide the joint asymptotic distribution of the  $K$   largest eigenvalues of the matrices  $[\hat{\mathbf{R}},\hat{\mathbf{R}}_{1},\hdots,\hat{\mathbf{R}}_{L}$  . The proposed test statistic is then compared to various alternatives, including the GLRT for the low-rank model (6) as well as a statistic built from the results of [17] on the extreme eigenvalues of the spiked Fisher matrices    $\bar{(\hat{\bf R}_{\ell}^{-1}\hat{\bf R})_{\ell=1,\dots,L}}.$  . We also provide an empirical study of the proposed test statistic on Synthetic Aperture Radar (SAR) images for detecting changes between two scenes.  

Organization.  The paper is organized as follows. In Section II, we study an extension of the results of [21] on the asymp- totic distribution of the largest eigenvalues of  $\mathbf{\dot{R}}_{1},\dots,\hat{\mathbf{R}_{L}},\dot{\hat{\mathbf{R}}}$  . In Section III, we exploit the results derived in the previous section to build a new test statistic, for which we study its performance in the  high-dimensional regime . Sections IV and  $\mathrm{v}$   are dedicated to compare, both theoretically and numeri- cally, our proposed test statistic with alternative approaches. Simulations on synthetic data and on real data (SAR images) are provided.  

Notations.  For    $a\in\mathbb{R}$  ,    $a^{+}$    denotes the positive part. Vectors and matrices are denoted with boldface lower case and upper case letters respectively. For a complex matrix  A , we denote by    ${\mathbf A}^{T}$    and    $\mathbf{A}^{*}$  its transpose and conjugate transpose. If  A is a    $n\ \times\ n$   complex matrix,    $\operatorname{tr}(\mathbf{A})$   denot its trace and  $\lambda_{1}(\mathbf{A}),\ldots,\lambda_{n}(\mathbf{A})$   denote its eigenvalues. If  A  is Hermitian, the eigenvalues are conside a  $\lambda_{1}(\mathbf{A})\geq$   $\cdot\cdot\geq\lambda_{n}(\mathbf{A})$  . For matrices  $\mathbf{A}_{1},\ldots,\mathbf{A}_{n}$  ,  $\operatorname{bdiag}(\mathbf{A}_{1},\dots,\mathbf{A}_{n})$  denotes the the block diagonal matrix formed by    $\mathbf{A}_{1},\ldots,\mathbf{A}_{n}$  . The complex circular Gaussian distribution on    $\mathbb{C}^{n}$    with co- variance matrix    $\mathbf{R}$   is den d as    ${\mathcal{N}}_{\mathbb{C}^{n}}(\mathbf{0},\mathbf{R})$  , while the real Gaussian distribution on  R  $\mathbb{R}^{n}$    with mean    $\pmb{\mu}$   and covariance matrix    $\mathbf{R}$   is denoted as  ${\mathcal{N}}_{\mathbb{R}^{n}}(\pmb{\mu},\mathbf{R})$  .  

# II. S PECTRUM OF  $\hat{\mathbf{R}}$  

In this section, we study the asymptotic behavior at    $1^{s t}$    and  $2^{n d}$    orders of the largest eigenvalues of  $\hat{\mathbf{R}}$   when the matrices  $\hat{\mathbf{R}}_{1},\hdots,\hat{\mathbf{R}}_{L}$   follow the low-rank model (6).  

Consider the following two assumptions, which describe the high-dimensional regime  and specify the asymptotic behavior of the eigenvalues of    $\pmb{\Gamma}_{1},\dots,\pmb{\Gamma}_{L}$  .  

Assumption 1.  The sample sizes    $N_{1}\,=\,N_{1}({\cal M}),.\,.\,.\,,N_{L}\,=$   $N_{L}(M)$   are functions of    $M$   such that  

$$
\frac{M}{N_{\ell}}=c_{\ell}+o\left(\frac{1}{\sqrt{M}}\right),
$$  

as  $M\rightarrow\infty$  , where    $c_{1},.\.\,.\,,c_{L}>0$   and    $K,L$   are independent of  M .  

In comparison with the classical  low-dimensional regime where    $M$   is assumed fixed while    $N_{1},.\,.\,.\,,N_{L}\ \to\ \infty$  (see e.g. [22], [11]), the high-dimensional regime described in Assumption 1 models practical scenarios where the sample sizes    $N_{1},\dots,N_{L}$   are of the same order of magnitude as the dimension    $M$   and where    $K$   is small compared to    $M$  . This regime has been widely used in the high-dimensional statistics literature (see e.g. [23]), as well as in the signal processing applications (see e.g. [15], [24], [25]).  

In what follows the  high-dimensional regime  described in Assumption 1 is represented by the notation    $M\,\rightarrow\,\infty$  . We also define  

$$
c:=\left(\sum_{\ell=1}^{L}\frac{1}{c_{\ell}}\right)^{-1},
$$  

as well as  

$$
\Gamma:=\sum_{\ell=1}^{L}\frac{N_{\ell}}{N}\Gamma_{\ell}.
$$  

One can notice that    $\mathbf{\deltaT}$   is the the pooling of the low-rank covariance matrices    $\pmb{\Gamma}_{1},\dots,\pmb{\Gamma}_{L}$   and has rank at most  $K L$  . In the following, we also need to ensure the convergence of the eigenvalues of matrices    $\mathbf{\Gamma}_{\ell},\mathbf{\Gamma}$   in the high-dimensional regime.  

Assumption 2.  For all    $k\in\{1,.\,.\,.\,,K\},\,\ell\in\{1,.\,.\,.\,,L\},$  ,  

$$
\lambda_{k}\big(\pmb{\Gamma}_{\ell}\big)=\gamma_{k,\ell}+o\left(\frac{1}{\sqrt{M}}\right),
$$  

and for all    $k\in\{1,.\.\.,K L\}$  ,  

$$
\lambda_{k}(\mathbf{T})=\gamma_{k}+o\left(\frac{1}{\sqrt{M}}\right).
$$  

We note that Assumption 2 is a purely technical assumption which is not restrictive in practice as the corresponding results derived from it are meant to be used for fixed values of  $M,N,K$  .  

Under Assumptions 1 and 2, the global behaviour of the eigenvalues of    $\mathbf{\dot{R}}$   can be described through its empirical spectral distribution defined as the random probability measure  

$$
\hat{\mu}=\frac{1}{M}\sum_{k=1}^{M}\delta_{\lambda_{k}\left(\hat{\mathbf{R}}\right)},
$$  

where    $\delta_{x}$   is the Dirac measure centered at    $x$  . Under the model (6), each covariance matrix    ${\bf R}_{1},\ldots,{\bf R}_{L}$   is a fixed rank    $K$   perturbation of the matrix    $\sigma^{2}\mathbf{I}$   and it can be shown using standard perturbations arguments that  $\hat{\mu}$   asymptotically behaves as the Marcenko-Pastur distribution, i.e.  $\hat{\mu}$   converges weakly almost surely    $(a.s.)$   to the probability measure:  

$$
\begin{array}{l}{\displaystyle\mu(\mathrm{d}x)=\frac{\sqrt{(x-x^{-})(x^{+}-x)}}{2\pi\sigma^{2}c x}\mathbb{1}_{[x^{-},x^{+}]}(x)\mathrm{d}x}\\ {\displaystyle\quad\quad+\left(1-\frac{1}{c}\right)^{+}\delta_{0}(\mathrm{d}x),}\end{array}
$$  

where    $x^{\pm}=\sigma^{2}(1\!\pm\!\sqrt{c})^{2}$  . Consequently, any functional of the type  

$$
{\hat{\mu}}(\varphi):={\frac{1}{M}}\sum_{k=1}^{M}\varphi(\lambda_{k}({\hat{\mathbf{R}}})),
$$  

where  $\varphi$   is a bounded continuous function, satisfies  

$$
\hat{\mu}(\varphi)=\int_{\mathbb{R}}\varphi(\lambda)\mathrm{d}\hat{\mu}(\lambda)\xrightarrow[M\to\infty]{a.s.}\int_{\mathbb{R}}\varphi(\lambda)\mathrm{d}\mu(\lambda).
$$  

As the limit in (17) only depends on  $\sigma^{2}$    and  $c$  , it is not possible to recover information on the low-rank matrices    $\pmb{\Gamma}_{1},\dots,\pmb{\Gamma}_{L}$  in the  high-dimensional regime  from statistics of type (16). However, under the previous assumptions, it can be shown that the information related to the spectrum of    $\mathbf{\deltaT}$   can be found in the largest    $K L$   eigenvalues of    $\mathbf{\dot{\hat{R}}}$  , thanks to the following result.  

Theorem 1.  Under Assumptions   $I$   and 2,    $\forall k\in\{1,.\,.\,.\,,K L\},$  ,  

$$
\begin{array}{r}{\lambda_{k}\left(\hat{\bf R}\right)\xrightarrow[M\rightarrow\infty]{a.s.}\phi_{c}\left(\gamma_{k},\sigma^{2}\right),}\end{array}
$$  

with  

$$
\phi_{c}(\gamma,\sigma^{2}):=\left\{\!\!\begin{array}{l l}{\frac{(\gamma+\sigma^{2})(\gamma+\sigma^{2}c)}{\gamma}}&{\,\,\,\,i f\,\gamma>\sigma^{2}\sqrt{c}}\\ {\sigma^{2}(1+\sqrt{c})^{2}}&{\,\,\,\,i f\,\gamma\le\sigma^{2}\sqrt{c}}\end{array}\!\!\right.,
$$  

Moreover,    $\lambda_{K L+1}(\hat{\mathbf{R}})\to\sigma^{2}\left(1+\sqrt{c}\right)^{2}\,{\mathrm{e}}$   →   a.s.  when    $M\rightarrow\infty$  . Proof.  The proof of Theorem 1 is deferred to Appendix B.  

The matrix  $\hat{\mathbf{R}}$   being a mixture of    $L$   independent but not identically distributed Wishart matrices, we note that Theorem 1 provides an extension of the results of [21, Th. 2.7] (see also [26]) to the case    $L>1$  . It shows in particular that the largest eigenvalues of  $\hat{\mathbf{R}}$   converge to some limits depending directly of the eigenvalues of    $\mathbf{\Gamma}$  , provided that for all    $k\,\in$   $\{1,\ldots,K L\}$   the ratios    $\frac{\gamma_{k}}{\sigma^{2}}$   are above    $\sqrt{c}$  . The threshold  $\sqrt{c}$  can be interpreted as a minimal SNR above which the  k  $k^{t h}$  largest  signal related  eigenvalues of  $\hat{\mathbf{R}}$   splits from the largest noise related  eigenvalue    $\lambda_{K L+1}(\hat{\mathbf{R}})$  .  

The next result shows, under hypothesis    ${\mathcal{H}}_{0}$  , a joint  Cen- tral Limit Theorem  (CLT) on the largest eigenvalues of  $\hat{\mathbf{R}}_{1},.\,.\,.\,,\hat{\mathbf{R}}_{L},\hat{\mathbf{R}}$  .  

Theorem 2.  Let Assumptions 1-2 hold. Assume moreover that  $\pmb{\Gamma}_{1}=.\,.\,.=\pmb{\Gamma}_{L}$   (thus  $\gamma_{k,\ell}=\gamma_{k,\ell}$  ) and that  

$$
\gamma_{1}>.\,.\,.>\gamma_{K}>\sigma^{2}\operatorname*{max}\{\sqrt{c},\sqrt{c}_{1},.\,.\,.\,,\sqrt{c}_{L}\}.
$$  

Then we have  

$$
\begin{array}{r l}&{\sqrt{M}\left(\underset{M\rightarrow\infty}{\underbrace{\lambda_{k}\left(\hat{\mathbf{R}}\right)}}-\phi_{c}(\gamma_{k},\sigma^{2})\right.\right.}\\ &{\qquad\qquad\left.\left(\lambda_{k}\left(\hat{\mathbf{R}}_{\ell}\right)-\phi_{c_{\ell}}(\gamma_{k},\sigma^{2})\right)_{\ell=1,\dots,L}\right)_{k=1,\dots,K}}\\ &{\qquad\qquad\xrightarrow[M\rightarrow\infty]{\mathcal{D}}\mathcal{N}_{\mathbb{R}^{K(L+1)}}\left(\mathbf{0},\Theta\right),}\end{array}
$$  

where    $\Theta$   is a positive definite block diagonal matrix given by  $\pmb{\Theta}=\mathrm{bdiag}\left(\pmb{\Theta}_{1},.\,.\,.\,,\pmb{\Theta}_{K}\right)$   with  

$$
\Theta_{k}:=\left(\begin{array}{c c c c}{{\theta_{k,0}^{2}}}&{{\vartheta_{k,1}}}&{{\ldots}}&{{\vartheta_{k,L}}}\\ {{}}&{{}}&{{}}&{{}}\\ {{\vartheta_{k,1}}}&{{\ddots}}&{{(0)}}&{{}}\\ {{\vdots}}&{{(0)}}&{{\ddots}}&{{}}\\ {{\vartheta_{k,L}}}&{{}}&{{}}&{{\theta_{k,L}^{2}}}\end{array}\right),
$$  

and by denoting    $c_{0}=c_{;}$  ,  

$$
\theta_{k,\ell}^{2}=c_{\ell}\frac{(\gamma_{k}^{2}-\sigma^{4}c_{\ell})(\gamma_{k}+\sigma^{2})^{2}}{\gamma_{k}^{2}},\quad\ell\geq0,
$$  

$$
\vartheta_{k,\ell}=c_{0}\frac{(\gamma_{k}^{2}-\sigma^{4}c_{\ell})(\gamma_{k}+\sigma^{2})^{2}}{\gamma_{k}^{2}},\quad\ell\ge1.
$$  

Proof.  The proof is postponed to Appendix C.  

The result of Theorem 2 provides an extension of [20, Th. 1.4] which studies a CLT for the    $K$   largest eigenvalues of  $\hat{\mathbf{R}}_{\ell}$  . We note that the result of Theorem 2 cannot be inferred directly from [20, Th. 1.4] and requires a careful study due to the strong dependency between the eigenvalues of  $\hat{\mathbf{R}}^{\dagger}$   and the ones of  $\check{\hat{\mathbf{R}}}_{1},\dots,\hat{\mathbf{R}}_{L}$  .  

Theorems 1 and 2 are exploited in the following section to build a new statistic for the test (2), relevant for the low-rank model (6).  

# III. P ROPOSED TEST STATISTIC  

Before introducing our new test statistic, we first notice that the test (2) can be reformulated as:  

$$
\begin{array}{r l}{\mathcal{H}_{0}:}&{\boldsymbol{\Gamma}_{1}=.\;.\;.=\boldsymbol{\Gamma}_{L}}\\ {\mathcal{H}_{1}:}&{\exists(i,j)\in\{1,.\;.\;.\;,L\}^{2}\ \mathrm{s.t.}\ \boldsymbol{\Gamma}_{i}\neq\boldsymbol{\Gamma}_{j}^{'}}\end{array}
$$  

and we assume in the following that the rank  $K$   is  known  (see also Remark 1 below in case the rank is unknown). Next, we consider the following lemma, which shows that hypothesis  ${\mathcal{H}}_{0}$   can be verified by com eigenvalues of matrix  $\mathbf{\Gamma}$  with the ones of matrices  $\pmb{\Gamma}_{1},\dots,\pmb{\Gamma}_{L}$  .  

Lemma 1.  The following assertions are equivalent:  

Proof.  The proof of Lemma 1 can be found in [1].  

From Lemma 1, one can equivalently formulate the test (25) as follows  

$$
\begin{array}{r l}{\mathcal{H}_{0}:}&{\forall k,\ell,\ \lambda_{k}\left(\mathbf{T}_{\ell}\right)=\lambda_{k}\left(\mathbf{T}\right)}\\ {\mathcal{H}_{1}:}&{\exists k,\ell:\lambda_{k}\left(\mathbf{T}_{\ell}\right)\neq\lambda_{k}\left(\mathbf{T}\right).}\end{array}
$$  

Consequently, it is possible to discriminate between hypothe- ses    ${\mathcal{H}}_{0}$   and    $\mathcal{H}_{1}$   by exploiting only the eigenvalues of the matrices  $\mathbf{\Gamma}_{1},\dots,\mathbf{\Gamma}_{L},\mathbf{\Gamma}$   for which we can also build consistent estimators in the high-dimensional regime as follows. Let us consider first the maximum likelihood estimator of the noise variance  $\sigma^{2}$    given by  

$$
{\hat{\sigma}}^{2}:=\sum_{\ell=1}^{L}{\frac{N_{\ell}}{N}}{\frac{1}{M-K}}\sum_{k=K+1}^{M}\lambda_{k}\left({\hat{\bf R}}_{\ell}\right).
$$  

From (6) and Theorem 1, one can easily show that    ${\hat{\sigma}}^{2}\to\sigma^{2}$    →  $M~\to~+\infty$  under both    ${\mathcal{H}}_{0}$   and    $\mathcal{H}_{1}$  . Next, for all  $k\in\{1,\ldots,K L\}$   ∈{ } , let  $\hat{\gamma}_{k}$   be the largest solution to the equation  $\phi_{c}\big(\gamma_{k},\hat{\sigma}^{2}\big)=\lambda_{k}\big(\hat{\mathbf{R}}\big)$   if    $\lambda_{k}(\hat{\bf R})>\bar{{\hat{\sigma}}^{2}}(1+\sqrt{c})^{2}$    , or  $\hat{\gamma}_{k}=\hat{\sigma}^{2}\sqrt{c}$  otherwise. Similarly, for all    $k\,\in\,\{1,\ldots,K\}$  , let    $\hat{\gamma}_{k,\ell}$  be the largest solution to the equation    $\phi_{c_{\ell}}\big(\gamma_{k,\ell},\hat{\sigma}^{2}\big)\ =\ \lambda_{k}\big(\hat{\bf R}_{\ell}\big)$   if  $\lambda_{k}\bar{(\mathbf{R}_{\ell})}>\hat{\sigma}^{2}(1+\sqrt{c}_{\ell})^{2}$    , or    $\hat{\gamma}_{k,\ell}\,=\,\hat{\sigma}^{2}\sqrt{c_{\ell}}$  otherwise. Then we have the following immediate result, as a consequence of Theorem 1.  

Corollary 1.  Under Assumptions   $I$   and 2,  

$$
\hat{\gamma}_{k}\xrightarrow[M\rightarrow\infty]{a.s.}\left\{\gamma_{k}\;\;\;\;\;\;\;\;\;\;\;i f\;\gamma_{k}>\sigma^{2}\sqrt{c}\;,\right.
$$  

$$
\hat{\gamma}_{k,\ell}\xrightarrow[M\rightarrow\infty]{a.s.}\left\{\gamma_{k,\ell}\quad\begin{array}{l l}{\gamma_{k,\ell}}&{i f\,\gamma_{k,\ell}>\sigma^{2}\sqrt{c_{\ell}}}\\ {\sigma^{2}\sqrt{c_{\ell}}}&{o t h e r w i s e}\end{array}\right..
$$  

Considering this result we propose the following test statis- tic  

$$
T(\epsilon)=\mathbb{1}_{(\epsilon,+\infty)}\left(\|\hat{\boldsymbol{\gamma}}\|_{2}^{2}\right),
$$  

where  

$$
\hat{\gamma}=(\hat{\gamma}_{k}-\hat{\gamma}_{k,\ell})_{\stackrel{k=1,\ldots,K}{\ell=1,\ldots,L}}.
$$  

To study the performance in terms of consistency and asymp- totic type I error of the test statistic (30), we consider the following assumption which ensures that the signal and noise eigenvalues of matrices  $\hat{\mathbf{R}},\hat{\mathbf{R}}_{1},\hdots,\hat{\mathbf{R}}_{L}$   are separated in the high-dimensional regime .  

Assumption 3.  For all    $k\in\{1,\ldots,K\}$   and    $\ell\in\{1,.\,.\,.\,,L\}$  

$$
\begin{array}{r l}&{\gamma_{1,\ell}>.\,.\,.>\gamma_{K,\ell}>\sigma^{2}\operatorname*{max}\{\sqrt{c}_{1},.\,.\,,\sqrt{c_{L}}\},}\\ &{\quad\gamma_{1}>.\,.\,.>\gamma_{K}>\sigma^{2}\sqrt{c}.}\end{array}
$$  

Moreover, under    $\mathcal{H}_{1}$  , there exist    $k,\ell$  such that    $\gamma_{k}\neq\gamma_{k,\ell}$  .  

As a consequence of Corollary 1, we have under Assump- tions 1-3,  

$$
\begin{array}{r}{\|\hat{\gamma}\|_{2}^{2}\xrightarrow[M\rightarrow\infty]{\mathrm{a.s.}}\|\gamma\|_{2}^{2}\,,}\end{array}
$$  

with  

$$
\gamma=(\gamma_{k}-\gamma_{k,l})_{\stackrel{k=1,\ldots,K}{\ell=1,\ldots,L}}\,,
$$  

such that    $\gamma=0$   under    ${\mathcal{H}}_{0}$   and  $\gamma\neq{\bf0}$   under    $\mathcal{H}_{1}$  . This implies the following consistency result.  

Theorem 3.  Let Assumptions   $_{l-3}$   hold and denote    $\epsilon_{1}~=$   $\|\gamma\|_{2}^{2}>0$   under    $\mathcal{H}_{1}$  . Then for all    $\epsilon\in(0,\epsilon_{1})$  ,  

$$
\mathbb{P}_{i}\left(\operatorname*{lim}_{M\to\infty}T(\epsilon)=i\right)=1,
$$  

for    $\textit{i}\in\{0,1\}$  , where    $\mathbb{P}_{i}$   is the probability measure under hypothesis  H .  

To control the asymptotic type I error of the proposed test statistic (30), we also need the following result which, as a consequence of Theorem 2, provides a CLT for (31).  

Corollary 2.  Under hypothesis    ${\mathcal{H}}_{0}$   and Assumptions 1-3, we have  

$$
\sqrt{M}\hat{\boldsymbol{\gamma}}\xrightarrow[M\rightarrow\infty]{\mathcal{D}}\mathcal{N}_{\mathbb{R}^{K L}}\left(\mathbf{0},\mathbf{H}\boldsymbol{\Upsilon}\mathbf{H}^{T}\right),
$$  

where    $\mathbf{H}$   is the    $K L\,\times\,K(L\,+\,1)$   matrix defined by    $\textbf{H}=$  bdiag  $\left(\tilde{\bf H},\cdot\,\cdot\,,\tilde{\bf H}\right)$   ,    ${\pmb{\Upsilon}}\ =\ \mathrm{bdiag}\left({\pmb{\Upsilon}}_{1},.\ldots,{\pmb{\Upsilon}}_{K}\right)$   with    $\tilde{\mathbf{H}}$   the  $L\times(\hat{L}+1)$   matrix given by  

$$
\tilde{\mathbf{H}}=\left(\begin{array}{l l l l l l}{1}&{-1}&{0}&{\hdots}&{\hdots}&{0}\\ {1}&{0}&{-1}&{\ddots}&&{\vdots}\\ {\vdots}&{\vdots}&{\ddots}&{\ddots}&{\ddots}&{\vdots}\\ {\vdots}&{\vdots}&&{\ddots}&{\ddots}&{0}\\ {1}&{0}&{\hdots}&{\hdots}&{0}&{-1}\end{array}\right),
$$  

and with  

$$
\begin{array}{r}{\pmb{\Upsilon}_{k}=\left(\begin{array}{l l l l}{\omega_{k,0}^{2}}&{\xi_{k}}&{\cdots}&{\xi_{k}}\\ {\xi_{k}}&{\ddots}&{(0)}\\ {\vdots}&{(0)}&{\ddots}\\ {\xi_{k}}&{}&{\omega_{k,L}^{2}}\end{array}\right),}\end{array}
$$  

where  

$$
\begin{array}{c}{{\omega_{k,\ell}^{2}=\displaystyle\frac{c_{\ell}\gamma_{k}^{2}(\gamma_{k}+\sigma^{2})^{2}}{\gamma_{k}^{2}-\sigma^{4}c_{\ell}},~~~\ell=0,.\,.\,.\,,L,}}\\ {{\xi_{k}=\displaystyle\frac{c_{0}\gamma_{k}^{2}(\gamma_{k}+\sigma^{2})^{2}}{\gamma_{k}^{2}-\sigma^{4}c_{0}}.}}\end{array}
$$  

Proof.  The proof is deferred to Appendix D.  

From Corollary 2, we can adjust the threshold    $\epsilon$   in (30) to control the asymptotic type I error in the  high-dimensional regime , as described in the next result. Let us define  $\hat{\textbf{Y}}=$  bdiag  $\left(\hat{\mathbf{\Upsilon}}_{1},\dots,\hat{\mathbf{\Upsilon}}_{K}\right)$   with  

$$
\begin{array}{r}{\hat{\mathbf{Y}}_{k}=\left(\begin{array}{l l l l}{\hat{\omega}_{k,0}^{2}}&{\hat{\xi}_{k}}&{\cdot\cdot\cdot}&{\hat{\xi}_{k}}\\ {\hat{\xi}_{k}}&{\cdot\cdot\cdot}&{(0)}\\ {\vdots}&{(0)}&{\cdot\cdot\cdot}\\ {\hat{\xi}_{k}}&{}&{\hat{\omega}_{k,L}^{2}}\end{array}\right),}\end{array}
$$  

where  

$$
\begin{array}{r l r}{\hat{\omega}_{k,\ell}^{2}=\frac{c_{\ell}\hat{\gamma}_{k}^{2}(\hat{\gamma}_{k}+\hat{\sigma}^{2})^{2}}{\hat{\gamma}_{k}^{2}-\hat{\sigma}^{4}c_{\ell}},}&{{}\ell\geq0}&{}\\ {\hat{\xi}_{k}=\frac{c_{0}\hat{\gamma}_{k}^{2}(\hat{\gamma}_{k}+\hat{\sigma}^{2})^{2}}{\hat{\gamma}_{k}^{2}-\hat{\sigma}^{4}c_{0}}.}\end{array}
$$  

From Corollary 1, it is clear that  $\hat{\mathbf{Y}}\rightarrow\mathbf{\hat{Y}}$   →  a.s. as    $M\rightarrow\infty$  .  

Theorem 4. Let  $\begin{array}{r l r}{\mathbf{x}}&{{}\in}&{\mathcal{N}_{\mathbb{R}^{K L}}(\mathbf{0},\mathbf{I})}\end{array}$  ∈ N and  $\begin{array}{r l}{F(t,\Xi)}&{{}=}\end{array}$   $\mathbb{P}\left(\mathbf{x}^{T}\Xi\mathbf{x}\leq t\right)\!,\:\alpha\in\left(0,1\right)$   and set  

$$
\hat{\epsilon}=\frac{1}{M}\operatorname*{inf}\left\{t\in\mathbb{R}:F\left(t,\mathbf{H}\mathbf{\hat{Y}}\mathbf{H}^{T}\right)\geq1-\alpha\right\}.
$$  

Then under Assumptions   $I$   and  $3$  , we have  

$$
\begin{array}{r}{\mathbb{P}_{0}\mathopen{}\mathclose\bgroup\left(T(\hat{\epsilon})=1\aftergroup\egroup\right)\xrightarrow[M\rightarrow\infty]{}\alpha.}\end{array}
$$  

In practice, Theorem 4 is used as follows. For a fixed realization of    $\hat{\mathbf Y}$  , we sample the distribution of the Gaussian quadratic form  $\mathbf{x}^{T}\mathbf{H}\hat{\mathbf{Y}}\mathbf{H}^{\hat{T}}\mathbf{x}$   and the threshold    $\hat{\epsilon}$   is then set as the    $(1-\alpha)$  -quantile of    $\mathbf{x}^{T}\mathbf{H}\mathbf{\hat{Y}}\mathbf{H}^{T}\mathbf{x}$  .  

Remark 1.  For a more general approach where each    $\mathbf{T}_{\ell}$  has unknown rank    $K_{\ell}$  , one can obtain consistent estimates of  $K_{1},\dots,K_{L}$   thanks to Theorem   $I$  . Assuming    $K_{1},\dots,K_{L}$   fixed with respect to  $M$  , and if for  $\ell\in\{1,.\,.\,.\,,L\}$  ,  $\gamma_{K_{\ell},\ell}>\sigma^{2}\sqrt c_{\ell}$  , under Assumption 2 the quantity  

$$
\hat{K}_{\ell}=\operatorname*{max}\left\{k:\lambda_{k}\left(\hat{\bf R}_{\ell}\right)>\sigma^{2}(1+\sqrt{c}_{\ell})^{2}+\epsilon_{\ell}\right\},
$$  

converges almost surely to  $K_{\ell}$  in the high-dimensional regime, for all    $\epsilon_{\ell}\,\in\,\big(0,\phi_{c_{\ell}}\,\big(\gamma_{K_{\ell},\ell},\sigma^{2}\big)-\sigma^{2}(1+\sqrt{c_{\ell}})^{2}\big)$          . This shows that we can build consistent test statistics to capture changes in the rank (see further  $I^{27J)}$  .  

Remark 2.  It is easy to show that under Assumption   $^3$  , the matrix    $\mathbf{H}\Upsilon\mathbf{H}^{T}$    is non singular. Therefore, an alternative approach to obtain a test statistic with controlled asymptotic type  $I$   error would be to consider the statistic  

$$
\tilde{T}(\epsilon)=\mathbb{1}_{(\epsilon,+\infty)}\left(M\left\|\left(\mathbf{H}\mathbf{\hat{Y}}\mathbf{H}^{T}\right)^{-\frac{1}{2}}\hat{\boldsymbol{\gamma}}\right\|_{2}^{2}\right),
$$  

since from Corollary 2, we have  

$$
M\left\|\left(\mathbf{H}\mathbf{\hat{Y}}\mathbf{H}^{T}\right)^{-\frac{1}{2}}\hat{\boldsymbol{\gamma}}\right\|_{2}^{2}\xrightarrow[M\rightarrow\infty]{\mathcal{D}}\boldsymbol{\chi}^{2}(K L).
$$  

Nevertheless, although this approach looks simpler, it appears that the covariance matrix    $\mathbf{H}\mathbf{Y}\mathbf{H}^{T}$    is ill-conditioned. This can be readily seen, e.g. in the special case where    $c_{1}=.\,.=c_{L}$  and for a large SNR. If    $\kappa(\Upsilon_{k})$   denotes the condition number of    $\Upsilon_{k}$   defined in  (39) , then we can verify (details are omitted) that    $\kappa(\Upsilon_{k})$   scales w h  $\gamma^{2}$    as  $\gamma^{2}\rightarrow\infty$  . Therefore, in practice, setting the threshold  ϵ  based on the  $\chi^{2}(K L)$   distribution gives poor performance.  

# IV. S OME COMPARISONS WITH ALTERNATIVE METHODS  

In this section, we compare the test statistic given in (30) with two relevant alternatives for the low-rank model (6) and the  high-dimensional regime  described in Assumption 1. To that purpose, we consider scenarios involving a change of sub- space/eigenvalues for the rank    $K=1$   model    $\mathbf{\Gamma}_{\ell}=\gamma_{1,\ell}\mathbf{u}_{\ell}\mathbf{u}_{\ell}^{*}$  , where    $\|\mathbf{u}_{\ell}\|_{2}~=~1$  , and where    $\gamma_{1,\ell}$  is independent of    $M$  . We precise that our objective is not to provide an exhaustive analysis of all the possible scenarios under    $\mathcal{H}_{1}$  , but to draw some performance comparisons, in terms of consistency, out of a few simple cases. In the remainder of this section, we also assume that    $L=2$   and    $N_{1}=N_{2}$   so that    $c_{1}=c_{2}=2c$  .  

# A. A test based on spiked Fisher matrices  

Although test statistics of the form (3) are not consistent in the  high-dimensional regime , we can build consistent test statistics by exploiting the behaviour of the largest and smallest eigenvalues of the Fisher matrices    $\hat{\bf R}_{2}^{-1}\hat{\bf R}_{1}$   (see [17]). We propose   1   to use    $T_{\mathrm{Fisper}}(\epsilon)=\mathbb{1}_{(\epsilon,+\infty)}(F)$   with  

$$
\begin{array}{r l}{F=\underset{\ell^{\prime}\neq\ell}{\sum^{L}}\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!
$$  

where  $\begin{array}{r}{\nu_{\ell,\ell^{\prime}}^{\pm}=\left(\frac{1\pm\sqrt{c_{\ell}+c_{\ell^{\prime}}-c_{\ell}c_{\ell^{\prime}}}}{1-c_{\ell}}\right)^{2}}\end{array}$  

Change of subspace. onsider that under  $\mathcal{H}_{1}$  ,    $\gamma_{1,1}=$   $\gamma_{1,2}$   and    $\mathbf{u}_{1}^{*}\mathbf{u}_{2}\rightarrow0$   as  $M\rightarrow\infty$  , so that the changes between  

1 Although outside the scope of this paper, we note that the results of [17, Th. 6.1] could be exploited to build a test statistic with controlled asymptotic type I error, which is not the case for (48).  

$\mathbf{T}_{1}$   and    $\Gamma_{2}$   are only carried by the unit norm eigenvector    $\mathbf{u}_{2}$  . It is easily seen that  

$$
\lambda_{k}\left(\mathbf{R}_{2}^{-1}\mathbf{R}_{1}\right)\xrightarrow[M\to\infty]{\begin{array}{r l}{\frac{\gamma_{1,1}+\sigma^{2}}{\sigma^{2}}}&{\mathrm{~if~}k=1,}\\ {1}&{\mathrm{~if~}k=2,\ldots,M-1,}\\ {\frac{\sigma^{2}}{\gamma_{1,1}+\sigma^{2}}}&{\mathrm{~if~}k=M,}\end{array}}\end{array}
$$  

so that applying [17, Th. 3.1] shows that for all small  $\epsilon>0$  ,  $\mathbb{P}_{i}(\operatorname*{lim}T_{\mathrm{Fisper}}(\epsilon)=i)=1$   for    $i\in\{0,1\}$   as    $M\rightarrow\infty$  iff  

$$
{\frac{\gamma_{1,1}}{\sigma^{2}}}>\beta={\frac{2\left(c+{\sqrt{c-c^{2}}}\right)}{1-2c}}.
$$  

One can see that    $\beta\,>\,\sqrt{2c}$   and therefore, from Assumption 3 and Theorem 3, we deduce that the Fisher based statistic requires a larger SNR  $\frac{\gamma_{1,1}}{\sigma^{2}}$  compared to the Wishart based statistic proposed in (30) to be consistent in the change of subspace scenario.  

Change of eigenvalues.  In that case, we assume that    $\gamma_{1,2}=$   $\gamma_{1,1}(1+\delta)$   with    $\delta>0$   and    $\mathbf{u}_{1}=\mathbf{u}_{2}$  , so that the changes are only carried by the largest eigenvalue of    $\Gamma_{2}$  . Note that under these settings, Assumption 2 is verified and it holds that  

$$
\lambda_{k}\left(\mathbf{R}_{2}^{-1}\mathbf{R}_{1}\right)\xrightarrow[M\to\infty]{}\left\{\frac{\gamma_{1,1}+\sigma^{2}}{\gamma_{1,1}(1+\delta)+\sigma^{2}}\right.\quad\mathrm{if}\ k=1,
$$  

Using again [17, Th. 3.1], we have that for all small    $\epsilon>0$  ,  $\mathbb{P}(\operatorname*{lim}T_{\mathrm{Fisper}}(\epsilon)=i)=1$   for  $i\in{0,1}$   as    $M\rightarrow\infty$  iff  

$$
\delta>\frac{2(c+\sqrt{c-c^{2}})}{1-2c},
$$  

and  

$$
\frac{\gamma_{1,1}}{\sigma^{2}}>\beta=\frac{2(c+\sqrt{c-c^{2}})}{(1+\delta)(1-2c)-(1+2\sqrt{c-c^{2}})}.
$$  

In this scenario, one can see that the minimal SNR    $\beta$   de- creases when    $\delta$   increases, which can be exploited to produce conditions where the Fisher test statistic is consistent while the Wishart one is not. Indeed, choose    $\begin{array}{r}{\sqrt{c}<\frac{\gamma_{1,1}}{\sigma^{2}}<\sqrt{2c}}\end{array}$   and  $\delta$   large enough so that (52) and (53) are verified. Then it can be seen lary 1 that    $\|\hat{\gamma}\|_{2}^{2}\;\to\;2(\gamma_{1,1}\,-\,\sigma^{2}\sqrt{2c})^{2}$  ∥   →   − a.s. as  M  $M\ \rightarrow\ \infty$  → ∞ and therefore for all small  ϵ  $\epsilon\mathrm{~\,~}>\mathrm{~\,~0~}$  ,  $\mathbb{P}_{0}\left(\operatorname*{lim}T(\epsilon)=1\right)=1$  .  

# B. The GLR for  (25)  

As an alternative to the GLR for the general covariance equality test (2), the GLR for the low-rank test (25) can be derived. Classical computations (details are omitted) provide the following test statistic  $T_{\mathrm{GLR-LR}}(\epsilon)=\mathbb{1}_{(\epsilon,+\infty)}(G)$   where  

$$
\begin{array}{r l}{\lefteqn{G=-\sum_{\ell=1}^{L}N_{\ell}\sum_{k=1}^{K}\log\left(\frac{\lambda_{k}(\hat{\mathbf{R}}_{\ell})}{\lambda_{k}(\hat{\mathbf{R}})}\right)}}\\ &{-\,N(M-K)\log\left(\frac{\frac{1}{M-K}\sum_{\ell=1}^{L}\frac{N_{\ell}}{N}\sum_{k=K+1}^{M}\lambda_{k}(\hat{\mathbf{R}}_{\ell})}{\frac{1}{M-K}\sum_{k=K+1}^{M}\lambda_{k}(\hat{\mathbf{R}})}\right)\,.}\end{array}
$$  

heorem 1, it can be shown that    $G~\to~G_{\infty}$  a.s. as  $M\rightarrow\infty$  where  

$$
G_{\infty}=\sum_{\ell=1}^{L}\frac{c}{c_{\ell}}\sum_{k=1}^{K}\left(\psi\left(\frac{\phi_{c}(\gamma_{k})}{\sigma^{2}}\right)-\psi\left(\frac{\phi_{c_{\ell}}(\gamma_{k,\ell})}{\sigma^{2}}\right)\right),
$$  

with    $\psi(x)=x-\log(x)$  .  

Let us consider a change of eigenvalues with    $\gamma_{1,2}=\gamma_{1,1}\,{+}\,\delta$  and    $\mathbf{u}_{1}~=~\mathbf{u}_{2}$   under    $\mathcal{H}_{1}$  . Then it is easy to see that under both    ${\mathcal{H}}_{0}$   and    $\mathcal{H}_{1}$  ,    $\begin{array}{r}{G_{\infty}\stackrel{\cdot}{=}-c+\mathcal{O}\left(\frac{1}{\gamma_{1,1}}\right)}\end{array}$    as    $\gamma_{1,1}~\rightarrow~+\infty$  . Regarding the proposed test (30), we     $\begin{array}{r}{\|\gamma\|_{2}^{2}=\frac{\delta^{2}}{2}}\end{array}$    under  $\mathcal{H}_{1}$   which shows the limit (34) under  H  ${\mathcal{H}}_{0}$   and  H  $\mathcal{H}_{1}$   cannot be made a arily close as    $\gamma_{1,1}~\rightarrow~\infty$  . This suggests that for a large  $\gamma_{1,1}$   and a fixed change  δ , the GLR for the low-rank model might experience a performance loss compared to the test (30).  

# V. S IMULATIONS  

In this section, we provide simulations to illustrate the performance of the test statistic    $T$   proposed in (30), and to perform some comparisons with the alternative test statistics introduced in Section IV. We consider    $\sigma^{2}=0.5$  ,    $K=2,L=$  2  as well as a Toeplitz model of rank  $K=2$   for the covariance matrix    $\mathbf{T}_{\ell}$  which can therefore be written as  

$$
\Gamma_{\ell}=\gamma_{1,\ell}\mathbf{a}\left(\theta_{1,\ell}\right)\mathbf{a}^{*}\left(\theta_{1,\ell}\right)+\gamma_{2,\ell}\mathbf{a}\left(\theta_{2,\ell}\right)\mathbf{a}^{*}\left(\theta_{2,\ell}\right),
$$  

with    $\begin{array}{r}{{\bf a}(\theta)=\frac{1}{\sqrt{M}}(1,\mathrm{e}^{\mathrm{i}\theta}\cdot\cdot\cdot,\mathrm{e}^{\mathrm{i}(M-1)\theta})^{T}}\\ {\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot\cdot}\end{array}$   . Note that the model

 (56) is common in spectral analysis and array processing [28].  

# A. Empirical and asymptotic Type  $I$   error of    $T(\epsilon)$  

We first illustrate the result of Theorem 4 and consider

  $\theta_{k,\ell}\,=\,0$   for    $(k,\ell)\,\in\,\{1,2\}^{2}$   $\gamma_{1,\ell}\:=\:3$   and    $\gamma_{2,\ell}\,=\,1.5$   for

  $\ell\,\in\,\{1,2\}$   a  $N_{1}\,=\,N_{2}\,=\,2M$  . The threshold    $\epsilon$   of (30)  $(1-\alpha)$   − -quantile of the Gaussian quadratic form

  $\mathbf{x}^{T}\mathbf{H}\mathbf{\hat{Y}}\mathbf{H}^{T}\mathbf{x}$   with  $\mathbf{x}\sim\mathcal{N}_{\mathbb{R}^{K L}}(\mathbf{0},\mathbf{I})$  , and we provide in T ABLE I the empirical Type I error of    $T(\epsilon)$   (evaluated over 100000 iterations) for    $M\in\{10,20,50,100\}$  . Table I thus shows that  

<td><table  border="1"><thead><tr><td><b>α</b></td><td rowspan="2"><b>0.005</b></td><td rowspan="2"><b>0.01</b></td><td rowspan="2"><b>0.02</b></td><td rowspan="2"><b>0.05</b></td><td rowspan="2"><b>0.10</b></td></tr><tr><td><b>T(e)</b></td></tr></thead><tbody><tr><td>M = 10</td><td>0.002</td><td>0.004</td><td>0.009</td><td>0.028</td><td>0.065</td></tr><tr><td>M = 20</td><td>0.0025</td><td>0.005</td><td>0.01</td><td>0.03</td><td>0.073</td></tr><tr><td>M = 50</td><td>0.003</td><td>0.006</td><td>0.013</td><td>0.038</td><td>0.083</td></tr><tr><td>M = 100</td><td>0.004</td><td>0.008</td><td>0.016</td><td>0.043</td><td>0.09</td></tr></tbody></table></td>  

the empirical type I error is close to the asymptotic type I error predicted in Theorem 4, when    $M$   is increasing.  

# B. Comparisons of powers  

In this section, we evaluate the proposed test statistic on synthetic data by considering the following two scenarios.  

(1)  Change of subspace:  under    ${\mathcal{H}}_{0}$  ,  $\theta_{1,1}=\theta_{1,2}=0.$  ,    $\theta_{2,1}=$   $\textstyle\theta_{2,2}\,=\,{\frac{\pi}{8}}$    and under    $\mathcal{H}_{1}$  ,    $\theta_{1,1}\,=\,0$  ,    $\textstyle\theta_{1,2}\,=\,{\frac{\pi}{2}}$    ,    $\theta_{2,1}\,=$   $\frac{\pi}{8}$    ,    $\textstyle\theta_{2,2}~=~{\frac{\pi}{2}}\,+\,{\frac{\pi}{8}}$    . We will also consider under both  

hypothesis    $\gamma_{1,1}=\gamma_{1,2}=2$  ,    $\gamma_{2,1}=\gamma_{2,2}=1$   and    $N_{1}=$   $N_{2}=2M$   thus    $c_{1}=c_{2}$  .  

(2)  Change of Eigenvalues:  unde  ${\mathcal{H}}_{0}$  ,    $\gamma_{1,1}\;=\;\gamma_{1,2}\;=\;2,$  ,  $\gamma_{2,1}\,=\,\gamma_{2,2}\,=\,1.5$   and under  H  $\mathcal{H}_{1}$  ,    $\gamma_{1,1}\,=\,2$  ,    $\gamma_{1,2}\,=\,5$  ,  $\gamma_{2,1}=1.5$  ,  $\gamma_{2,2}=4$  . We will also consider under both hypothesis    $\theta_{1,1}=\theta_{1,2}=0$  ,    $\theta_{2,1}=\theta_{2,2}=0$   and    $N_{1}=$   $N_{2}=4M$   thus    $c_{1}=c_{2}$  .  

In the simulations that follow, for both scenarios, we compute the power of different test statistics for a given type I error  $\alpha$   and different values of    $M$  . The statistic  $T(\epsilon)$  , which will be termed as ”Wishart” below, will be compared to the statis- tics    $T_{\mathrm{Fisper}}(\epsilon)$   (termed as ”Fisher”),    $T_{G L R-L R}(\epsilon)$   (termed as ”GLR-LR”) and    $T_{G L R}(\epsilon)~=~\mathbb{1}_{(\epsilon,+\infty)}(S_{|\varphi=\log})$   where    $S$   is given in (3) (termed as ”GLR”). For each of the statistics, the threshold    $\epsilon$   is adjusted separately to achieve a type I error of  $\alpha$  . Note that for both scenarios, Assumptions 2, 3 are verified and that the condition for the Fisher statistic to be consistent is verified as well. We observe that in both scenarios,  

<td><table  border="1"><thead><tr><td><b>Q</b></td><td rowspan="2"><b>0.005</b></td><td rowspan="2"><b>0.01</b></td><td rowspan="2"><b>0.02</b></td><td rowspan="2"><b>0.05</b></td><td rowspan="2"><b>0.1 </b></td></tr><tr><td><b>Statistics</b></td></tr></thead><tbody><tr><td colspan="6">M = 10</td></tr><tr><td>GLR</td><td>0.120</td><td>0.181</td><td>0.266</td><td>0.412</td><td>0.550</td></tr><tr><td>GLR-LR</td><td>0.381</td><td>0.483</td><td>0.588</td><td>0.734</td><td>0.832</td></tr><tr><td>Fisher</td><td>0.309</td><td>0.397</td><td>0.5</td><td>0.653</td><td>0.775</td></tr><tr><td>Wishart</td><td>0.998</td><td>0.999</td><td>0.999</td><td>1</td><td>1</td></tr><tr><td colspan="6">M  = 20</td></tr><tr><td>GLR</td><td>0.137</td><td>0.197</td><td>0.277</td><td>0.424</td><td>0.569</td></tr><tr><td>GLR-LR</td><td>0.736</td><td>0.808</td><td>0.87</td><td>0.934</td><td>0.967</td></tr><tr><td>Fisher</td><td>0.578</td><td>0.672</td><td>0.762</td><td>0.861</td><td>0.923</td></tr><tr><td>Wishart</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td colspan="6">M = 50</td></tr><tr><td>GLR</td><td>0.145</td><td>0.209</td><td>0.297</td><td>0.445</td><td>0.591</td></tr><tr><td>GLR-LR</td><td>0.992</td><td>0.996</td><td>1</td><td>1</td><td>1</td></tr><tr><td>Fisher</td><td>0.946</td><td>0.965</td><td>0.98</td><td>0.992</td><td>0.997</td></tr><tr><td>Wishart</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td colspan="6">M = 100</td></tr><tr><td>GLR</td><td>0.154</td><td>0.207</td><td>0.290</td><td>0.445</td><td>0.591</td></tr><tr><td>GLR-LR</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>Fisher</td><td>0.998</td><td>0.999</td><td>1</td><td>1</td><td>1</td></tr><tr><td>Wishart</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr></tbody></table></td>  

the proposed Wishart statistic shows a significantly better performance as    $M$   is increasing. Second, while the GLR-LR statistic outperforms the Wishart one for low dimensions    $M$  in the change of subspace scenario, the Wishart statistic still demonstrates a higher power compared to the Fisher and GLR statistics for both scenarios.  

The next simulation in Table IV shows the evolution of the power for different values of the noise variance in the change of eigenvalues scenario (  $M\,=\,100)$  ). The same can be done for the change of subspace scenario in Table V. We observe that the test statistics designed for a low-rank scenario (Wishart, Fisher, GLR-LR) outperform the GLR in general. Additionally, when the noise variance    $\sigma^{2}$    becomes too large, the conditions on the SNR ensuring the consistency of these statistics (Assumption 3 and the conditions of [17]) are not met anymore, and one observes in that case a significant drop of the performance (  $\sigma^{2}\,=\,5.5$   in Table IV and    $\sigma^{2}\,=\,2.5$   in  

<td><table  border="1"><thead><tr><td></td><td><b>α</b></td><td rowspan="2"><b>0.005</b></td><td rowspan="2"><b>0.01</b></td><td rowspan="2"><b>0.02</b></td><td rowspan="2"><b>0.05</b></td><td rowspan="2"><b>0.1 </b></td></tr><tr><td><b>Statistics</b></td><td></td></tr></thead><tbody><tr><td colspan="7">M = 10</td></tr><tr><td colspan="2">GLR</td><td>0.493</td><td>0.592</td><td>0.701</td><td>0.826</td><td>0.906</td></tr><tr><td colspan="2">GLR-LR</td><td>0.992</td><td>0.996</td><td>0.998</td><td>0.999</td><td>1</td></tr><tr><td colspan="2">Fisher</td><td>0.149</td><td>0.215</td><td>0.312</td><td>0.473</td><td>0.624</td></tr><tr><td colspan="2">Wishart</td><td>0.026</td><td>0.056</td><td>0.119</td><td>0.3</td><td>0.519</td></tr><tr><td colspan="7">M = 20</td></tr><tr><td colspan="2">GLR</td><td>0.757</td><td>0.829</td><td>0.89</td><td>0.949</td><td>0.978</td></tr><tr><td colspan="2">GLR-LR</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td colspan="2">Fisher</td><td>0.398</td><td>0.493</td><td>0.597</td><td>0.739</td><td>0.84</td></tr><tr><td colspan="2">Wishart</td><td>0.646</td><td>0.812</td><td>0.924</td><td>0.988</td><td>1</td></tr><tr><td colspan="7">M = 50</td></tr><tr><td colspan="2">GLR</td><td>0.832</td><td>0.883</td><td>0.927</td><td>0.968</td><td>0.987</td></tr><tr><td colspan="2">GLR-LR</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td colspan="2">Fisher</td><td>0.783</td><td>0.846</td><td>0.894</td><td>0.944</td><td>0.972</td></tr><tr><td colspan="2">Wishart</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td colspan="7">M = 100</td></tr><tr><td colspan="2">GLR</td><td>0.838</td><td>0.891</td><td>0.934</td><td>0.972</td><td>0.988</td></tr><tr><td colspan="2">GLR-LR</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td colspan="2">Fisher</td><td>0.955</td><td>0.971</td><td>0.984</td><td>0.993</td><td>0.997</td></tr><tr><td colspan="2">Wishart</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr></tbody></table></td>  

<td><table  border="1"><thead><tr><td></td><td><b>α</b></td><td rowspan="2"><b>0.005</b></td><td rowspan="2"><b>0.01</b></td><td rowspan="2"><b>0.02</b></td><td rowspan="2"><b>0.05</b></td><td rowspan="2"><b>0.1 </b></td></tr><tr><td><b>Statistics</b></td><td></td></tr></thead><tbody><tr><td colspan="7">a2 =  0.75</td></tr><tr><td colspan="2">GLR</td><td>0.1</td><td>0.153</td><td>0.226</td><td>0.368</td><td>0.512</td></tr><tr><td colspan="2">GLR-LR</td><td>0.999</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td colspan="2">Fisher</td><td>0.925</td><td>0.95</td><td>0.97</td><td>0.987</td><td>0.944</td></tr><tr><td colspan="2">Wishart</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td colspan="7">=1</td></tr><tr><td colspan="2">GLR</td><td>0.079</td><td>0.121</td><td>0.185</td><td>0.310</td><td>0.448</td></tr><tr><td colspan="2">GLR-LR</td><td>0.995</td><td>0.998</td><td>0.999</td><td>1</td><td>1</td></tr><tr><td colspan="2">Fisher</td><td>0.662</td><td>0.736</td><td>0.809</td><td>0.89</td><td>0.938</td></tr><tr><td colspan="2">Wishart</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td colspan="7">a2 = 5.5</td></tr><tr><td colspan="2">GLR</td><td>0.008</td><td>0.019</td><td>0.037</td><td>0.083</td><td>0.152</td></tr><tr><td colspan="2">GLR-LR</td><td>0.029</td><td>0.045</td><td>0.07</td><td>0.13</td><td>0.207</td></tr><tr><td colspan="2">Fisher</td><td>0.008</td><td>0.015</td><td>0.029</td><td>0.07</td><td>0.133</td></tr><tr><td colspan="2">Wishart</td><td>0.315</td><td>0.409</td><td>0.498</td><td>0.649</td><td>0.762</td></tr></tbody></table></td>  

# Table V).  

Remark 3.  In view of the simulations results described in Tables II-V, we observe that the proposed test statistic  (30) performs poorly when the conditions described in Assumptions 1 and 3 are not met, i.e. when the dimension  $M$   or the SNR are not large enough. Scenarios where the rank    $K$   is also of the same order of magnitude than    $M$  , thus violating Assumption 1, will also invalidate Theorem 4 and the asymptotic type   $I$  error will be poorly controlled in that case.  

# C. An application to change detection in SAR images  

In this section, we evaluate the performance of the proposed test statistic on images drawn from the UAV-SAR dataset of NASA/JPL-Caltech (SanAnd 26524 03, Segment 4). We o scenes with respective sizes    $2360\,\times\,600$   and  $2300\times600$   ×  pixels, which hav  previously used in [4], [18], and which are formed of  $L=2$   images acquired within a 5 years interval (see Figures 1 and 2). The azimuthal  

<td><table  border="1"><thead><tr><td><b>α</b></td><td rowspan="2"><b>0.005</b></td><td rowspan="2"><b>0.01</b></td><td rowspan="2"><b>0.02</b></td><td rowspan="2"><b>0.05</b></td><td rowspan="2"><b>0.1</b></td></tr><tr><td><b>Statistics</b></td></tr></thead><tbody><tr><td colspan="6">α2 = 0.75</td></tr><tr><td>GLR</td><td>0.4</td><td>0.496</td><td>0.602</td><td>0.749</td><td>0.849</td></tr><tr><td>GLR-LR</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>Fisher</td><td>0.329</td><td>0.414</td><td>0.510</td><td>0.625</td><td>0.763</td></tr><tr><td>Wishart</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td colspan="6">=1</td></tr><tr><td>GLR</td><td>0.172</td><td>0.246</td><td>0.34</td><td>0.505</td><td>0.646</td></tr><tr><td>GLR-LR</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>Fisher</td><td>0.077</td><td>0.119</td><td>0.18</td><td>0.297</td><td>0.424</td></tr><tr><td>Wishart</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td colspan="6">= 2.5 q2</td></tr><tr><td>GLR</td><td>0.017</td><td>0.031</td><td>0.057</td><td>0.120</td><td>0.209</td></tr><tr><td>GLR-LR</td><td>0.341</td><td>0.423</td><td>0.537</td><td>0.695</td><td>0.809</td></tr><tr><td>Fisher</td><td>0.007</td><td>0.015</td><td>0.03</td><td>0.068</td><td>0.129</td></tr><tr><td>Wishart</td><td>0.256</td><td>0.327</td><td>0.414</td><td>0.566</td><td>0.655</td></tr></tbody></table></td>  

![](images/2efe9704b23e096bd95ea8b5e65d12be63f872ed4c927348a1fbc79dfabb2157.jpg)  
Fig. 1. Scene 1 (Pauli representation) at two different times and its ground truth  

resolution is approximately  $0.6\:\mathrm{m}$   while the distance resolution is    $1.67\,\mathrm{~m~}$  . The dimension of each pixel, which was initially of    $M=3$  , has been increased to    $M=12$   using the wavelet decomposition technique of [29]. Local patches of sizes    $5\times5$  centered around each pixel under test are used for estimation,  

![](images/e8946bcea140b62570e6ad7f74133845dee602dbb20ad6aad672d062012bf85f.jpg)  
Fig. 2. Scene 2 (Pauli representation) at two different times and its ground truth  

![](images/48b16cb8f7c79131ffedede9eab94769c3bce24e857ccfa24bef6b2ba35525fa.jpg)  
Fig. 3. Ratio    $k\mapsto r(k)$   for both scenes  

![](images/40613bdf80d5685b590e95bd5715bece4441d4884d51f82b551a20f9ab764fcc.jpg)  
Fig. 4. ROC plots for the two scenes  

that is    $N_{1}=N_{2}=25$  . In Figure 3, the ratio  

$$
r(k)={\frac{\mathbb{E}\left[\sum_{i=1}^{k}\lambda_{i}\left({\hat{\mathbf{R}}}_{1}\right)\right]}{\mathbb{E}\left[\operatorname{tr}\left({\hat{\mathbf{R}}}_{1}\right)\right]}},
$$  

is plotted for both scenes, where the expectations are estimated by a sample mean over all the local patches. The rank    $K$   is set to 5 in the following to reach a ratio of    $r(K)\gtrapprox95\%$  . In Figure 4 are plotted the ROC curves for scenes 1 and 2, where we have compared the performance of the proposed test statistic (30), the GLR, the GLR-LR and the method of [18]. We observe some improvement of the proposed test statistic for type I errors greater than   $15\%$   for the scene 1 or greater than   $5\%$   for the scene 2.  

# VI. C ONCLUSION  

In this paper, the problem of covariance equality testing in low-rank Gaussian models has been studied. A new test statistic has been proposed, which is based on the asymptotic behaviour of the largest eigenvalues of certain Wishart matri- ces in the high-dimensional regime where the dimension of the observations and the number of samples both converge to infinity at the same rate. In particular, it is shown that the proposed statistic has a controlled type I error in the high- dimensional regime. Simulations on both synthetic and real datasets have demonstrated that the proposed test statistic is relevant compared to other alternative approaches.  

# A PPENDIX  

Notations.  Throughout this Appendix, we use the follow- ing notations. For a sequence of random matrices    $({\bf X}_{n})_{n\geq1}$  ,  ${\bf X}_{n}~=~o_{\mathbb{P}}(1)$   denotes the convergence of    $(\|\mathbf{X}_{n}\|_{2})$   to 0 in probability, while    ${\bf X}_{n}~=~{\mathcal O}_{\mathbb{P}}(1)$   denotes the tightness of  $(\|\mathbf{X}_{n}\|_{2})$  , as  $n\to\infty$  , where  $\lVert.\rVert_{2}$   stands fo . If  X  is a random matrix, we denote by  $\mathbf{X}^{\circ}\,=\,\mathbf{X}\,-\,\mathbb{E}[\mathbf{X}]$   − . Finally,    ${\mathcal{C}}^{1}(U)$   (resp.    ${\mathcal{C}}_{c}^{\infty}(U),$  ) denotes the set of continuously differentiable functions (resp. infinitely differentiable functions with compact support) defined on an open set    $U$  .  

A. Useful results around the Marcenko-Pastur distribution  

In this section, we provide well-known results on the Stieltjes transform  

$$
m(z)=\int_{\mathbb{R}}\frac{\mathrm{d}\mu(\lambda)}{\lambda-z},\quad z\in\mathbb{C}\backslash\mathbb{R},
$$  

of the Marcenko-Pastur distribution    $\mu$   with parameters    $(\sigma^{2},c)$  defined in (15), having the interval    $[x^{-},x^{+}]$   as support with  $x^{\pm}=\sigma^{2}(1\pm\sqrt{c})^{2}$  , and which will be of constant use for the proofs of Theorems 1, 2 and Corollary 2 below.  

We first recall that the limit  $\begin{array}{r}{m(x)=\operatorname*{lim}_{z\in\mathbb{C}^{+},z\to x}m(z)}\end{array}$   ex- ists for all    $x\in\mathbb{R}\backslash\{x^{-},x^{+}\}$  , and that for all  $z\in\mathbb{C}\backslash\{x^{-},x^{+}\}$  ,  $m(z)$   satisfies the equation:  

$$
m(z)=\frac{1+\sigma^{2}c m(z)}{\sigma^{2}-z\left(1+\sigma^{2}c m(z)\right)}=\frac{w(z)}{z(\sigma^{2}-w(z))},
$$  

with  

$$
w(z)=z\left(1+\sigma^{2}c m(z)\right).
$$  

Moreover,    $m$   is continuously differentiable o  $\mathbb{R}\backslash\{0,x^{-},x^{+}\}$  . We now provide some results on the function  w , which plays a central role in describing the behaviour of the largest eigenval- ues of  $\hat{\mathbf{R}}$  . From (59), we observe that for all  $z\in\mathbb{C}\backslash\{x^{-},x^{+}\}$  ,  

$$
\phi(w(z))=z,
$$  

where  $\phi$   is defined as:  

$$
\phi(w)=w\left(1-\frac{\sigma^{2}c}{\sigma^{2}-w}\right).
$$  

Function    $\phi$   is increasing on    $(-\infty,w^{-})\cup(w^{+},\infty)$   and de- creasing on    $(w^{-},\sigma^{2})\cup(\sigma^{2},\dot{w}^{+})$  , with    $w^{\pm}\;=\;\sigma^{2}\left(1\pm{\sqrt{c}}\right)$  and    $\phi(w^{\pm})=x^{\pm}$  .  

Next, we consider the following lemma (see [30]) regarding  $w$  .  

Lemma 2.  For all    $x\ \in\ \mathbb{R}\backslash\{x^{-},x^{+}\}$  ,    $w(x)~\in~\phi^{-1}(\{x\})$  . Moreover, among the preimages of  x  under    $\phi$  ,  

$i f\ x\ \in\ (x^{-},x^{+})$  ,    $w(x)$   is the unique one such that •  $\mathrm{Im}(w(x))>0$  ;  i  $f\ x\ \in\ \mathbb{R}\backslash\,[x^{-},x^{+}],\ w(x)$   is real and is the unique • preimage such that    $\phi^{\prime}(w(x))>0$  .  

Finally,    $z\in\mathbb{C}\backslash\mathbb{R}$   implies that    $w(z)\in\mathbb{C}\backslash\mathbb{R}.$  

Let    $\gamma\,\geq\,0$  mma 2, it is easily d t the equation  $w(x)=\gamma+\sigma^{2}$    admits a solution iff  $\gamma>\sigma^{2}{\sqrt{c}}$  , and that the solution is unique and given by  

$$
x=\phi(\gamma+\sigma^{2})=\frac{(\gamma+\sigma^{2})(\gamma+\sigma^{2}c)}{\gamma}.
$$  

Finally, we also have the following result giving various useful formulas. Define    $\begin{array}{r}{\tilde{m}(z)\,=\,-\frac{1}{z(1+\sigma^{2}c m(z))}}\end{array}$    and    $\tau(z)=$   $z m(z)\tilde{m}(z)$  .  

Lemma 3.  If    $\gamma>\sigma^{2}{\sqrt{c}},$  , then we have  

$$
\begin{array}{r l}&{m(\phi(\gamma+\sigma^{2}))=-\frac{1}{\gamma+\sigma^{2}c},}\\ &{\bar{m}(\phi(\gamma+\sigma^{2}))=-\frac{1}{\gamma+\sigma^{2}},}\\ &{m^{\prime}(\phi(\gamma+\sigma^{2}))=\frac{\gamma^{2}}{(\gamma+\sigma^{2}c)^{2}(\gamma^{2}-\sigma^{4}c)},}\\ &{\bar{m}^{\prime}(\phi(\gamma+\sigma^{2}))=\frac{\gamma^{2}}{(\gamma+\sigma^{2})^{2}(\gamma^{2}-\sigma^{4}c)},}\\ &{\tau(\phi(\gamma+\sigma^{2}))=\frac{1}{\gamma},}\\ &{\tau^{\prime}(\phi(\gamma+\sigma^{2}))=-\frac{1}{\gamma^{2}-\sigma^{4}c}.}\end{array}
$$  

B. Proof of Theorem   $I$  

This proof is based on techniques developed in [21].  

$l$  ) Some notations:  Denote by  ${\bf e}_{1},\ldots,{\bf e}_{N}$   the column vec- tors of the standard basis of    $\mathbb{C}^{N}$  , and let  

$$
\mathbf{J}_{1}=\sum_{n=1}^{N_{1}}\mathbf{e}_{n}\mathbf{e}_{n}^{*},
$$  

and for  $\ell=2,\ldots,L$  ,  

$$
\mathbf{J}_{\ell}=\sum_{n=N_{1}+\ldots+N_{\ell-1}+1}^{N_{1}+\ldots+N_{\ell}}\mathbf{e}_{n}\mathbf{e}_{n}^{*}.
$$  

We also consider the following ei gen decomposition of    $\mathbf{T}_{\ell}$  

$$
\Gamma_{\ell}=\mathbf{U}_{\ell}\mathbf{D}_{\ell}\mathbf{U}_{\ell}^{*},
$$  

with  $\mathbf{U}_{\ell}$  a  $M\ \times\ K$  isometric matrix and  $\begin{array}{r l}{\mathbf{D}_{\ell}}&{{}=}\end{array}$  d  $\mathrm{diag}\left(\lambda_{1}\!\left(\mathbf{T}_{\ell}\right)\!,\dots,\lambda_{K}\!\left(\mathbf{T}_{\ell}\right)\right)$  .  

2) Linearization:  Let    $\mathbf{Y}$   be the    $M\,\times\,N$   matrix given by    $\mathbf{Y}\;=\;\left[\mathbf{y}_{1,1},.\;.\;.\;,\mathbf{y}_{N_{1},1},.\;.\;.\;,\mathbf{y}_{1,L},.\;.\;.\;,\mathbf{y}_{N_{L},L}\right]$  . Due to the Gaussian model, one can assume, without loss of generality, that  

$$
\mathbf{Y}=\Omega\mathbf{S}^{\ast}+\mathbf{W},
$$  

where    $\mathbf{W}$   is    $M\times N$   matrix with i.i.d.    $\mathcal{N}_{\mathbb{C}}(0,\sigma^{2})$   entries and where    $\Omega=\left[\mathbf{U}_{1}\mathbf{D}_{1}^{\frac{1}{2}},\ldots,\mathbf{U}_{L}\mathbf{D}_{L}^{\frac{1}{2}}\right]$  h i and    $\mathbf{S}=[\mathbf{S}_{1},.\,.\,,\mathbf{S}_{L}]$  . with  $\mathbf{S}_{\ell}=\mathbf{J}_{\ell}\mathbf{X}$   and    $\mathbf{X}$   a  $N\times K$   matrix with i.i.d.    ${\mathcal{N}}_{\mathbb{C}}(0,1)$   entries and independent of  W . In particular, we have  $\begin{array}{r}{\hat{\mathbf{R}}=\frac{1}{N}\mathbf{Y}\mathbf{Y}^{*}}\end{array}$  , and    $\mathbf{Y}$   is a fixed rank (at most  $K L$  ) perturbation of  W  so that from  Weyl’s  inequality and the classical results on the extreme eigenvalues of  Wishart  matrices (see e.g. [31]), it holds that  

$$
\begin{array}{r}{\lambda_{M}(\hat{\bf R})\xrightarrow[M\rightarrow\infty]{a.s.}x^{-},}\end{array}
$$  

while  a.s.  

$$
\operatorname*{lim}_{M\to\infty}\lambda_{K L+1}\left(\hat{\mathbf{R}}\right)\leq\operatorname*{lim}_{M\to\infty}\lambda_{1}\left(\frac{1}{N}\mathbf{W}\mathbf{W}^{*}\right)=x^{+}.
$$  

To study the remaining eigenvalues of  $\hat{\mathbf{R}}$  , we use the lineariza- tion trick which consists in studying the following Hermitian block matrix  

$$
\check{\mathbf{Y}}=\left[\begin{array}{c c}{\mathbf{0}}&{\frac{1}{\sqrt{N}}\mathbf{Y}}\\ {\frac{1}{\sqrt{N}}\mathbf{Y}^{*}}&{\mathbf{0}}\end{array}\right],
$$  

for which it is well-known that [32, Th. 7.3.7]  

$$
\operatorname{sp}\left({\check{\mathbf{Y}}}\right)=\left\{\pm{\sqrt{\lambda_{k}\left({\hat{\mathbf{R}}}\right)}}\right\}\cup\{0\}.
$$  

3) Asymptotics for the characteristic polynomial of    $\check{\mathbf{Y}}$  Obviously, we have:  

$$
\begin{array}{r}{\check{\mathbf{Y}}=\mathbf{B}\check{\mathbf{I}}\mathbf{B}^{*}+\check{\mathbf{W}},}\end{array}
$$  

where  $\mathbf{B},\check{\mathbf{I}}$   and  $\check{\mathbf{W}}$   are given by:  

$$
\begin{array}{r}{\mathbf{B}=\left[\!\!\begin{array}{c c}{\Omega}&{\mathbf{0}}\\ {\mathbf{0}}&{\frac{1}{\sqrt{N}}\mathbf{S}}\end{array}\!\!\right],\check{\mathbf{I}}=\left[\!\!\begin{array}{c c}{\mathbf{0}}&{\mathbf{I}}\\ {\mathbf{I}}&{\mathbf{0}}\end{array}\!\!\right],\check{\mathbf{W}}=\left[\!\!\begin{array}{c c}{\mathbf{0}}&{\frac{1}{\sqrt{N}}\mathbf{W}}\\ {\frac{1}{\sqrt{N}}\mathbf{W}^{*}}&{\mathbf{0}}\end{array}\!\!\right].}\end{array}
$$  

Let    $\epsilon>0$   and t    $\mathcal{D}_{\epsilon}$   the  $\epsilon$  -neighborhood in  $\mathbb{C}$   of the set    $\mathcal{D}=$   $[x^{-},x^{+}]$  . Let  K  be a compact subset of    $\mathbb{C}\backslash\left(\mathscr{D}_{\epsilon}\cup(-\infty,0)\right)$  . Then (see again [31]), with probability one for all large  M ,  

$$
\mathrm{sp}\left(\breve{\mathbf{W}}\right)\cap\left\{\sqrt{z}:z\in\mathcal{K}\right\}=\varnothing,
$$  

and the following factorization  

$$
\operatorname*{det}\left(\check{\mathbf{Y}}-\sqrt{z}\mathbf{I}\right)=\operatorname*{det}\left(\check{\mathbf{W}}-\sqrt{z}\mathbf{I}\right)\operatorname*{det}\left(\check{\mathbf{I}}\right)\hat{P}(z),
$$  

where  

$$
\hat{P}(z)=\mathrm{det}\left(\check{\mathbf{I}}+\hat{\Xi}(z)\right),
$$  

and  $\hat{\pmb{\Xi}}(z)=\mathbf{B}^{*}\left(\check{\mathbf{W}}-\sqrt{z}\mathbf{I}\right)^{-1}\mathbf{B}$     −  , holds for all    $z\in\mathcal{K}$  . Then from the block matrix inversion formula, we have  

$$
\hat{\pmb{\Xi}}(z)=\left[\begin{array}{l l}{\sqrt{z}\Omega^{*}\mathbf{Q}(z)\Omega}&{\frac{1}{N}\Omega^{*}\mathbf{Q}(z)\mathbf{W}\mathbf{S}}\\ {\frac{1}{N}\mathbf{S}^{*}\mathbf{W}^{*}\mathbf{Q}(z)\Omega}&{\sqrt{z}\frac{1}{N}\mathbf{S}^{*}\tilde{\mathbf{Q}}(z)\mathbf{S}}\end{array}\right],
$$  

where    $\mathbf{Q}(z)$   and    $\tilde{\mathbf{Q}}(z)$   are the resolvent matrices of  $\scriptstyle{\frac{1}{N}}\mathbf{W}\mathbf{W}^{*}$  and  $\scriptstyle{\frac{1}{N}}\mathbf{W}^{*}\mathbf{W}$   given by  

$$
\mathbf{Q}(z)=\left(\frac{1}{N}\mathbf{W}\mathbf{W}^{*}-z\mathbf{I}\right)^{-1},\:\tilde{\mathbf{Q}}(z)=\left(\frac{1}{N}\mathbf{W}^{*}\mathbf{W}-z\mathbf{I}\right)_{\Omega,\ast}^{-1}.
$$  

We then use the following result.  

Proposition 1.  We have  

$$
\operatorname*{sup}_{z\in\mathcal{K}}\left\|\Omega^{*}\mathbf{Q}(z)\Omega-m(z)\Omega^{*}\Omega\right\|_{2}\xrightarrow[M\rightarrow\infty]{a.s.}0,
$$  

as well as  

$$
\operatorname*{sup}_{z\in\mathcal{K}}\left\|\frac{1}{N}\mathbf{S}_{k}^{\ast}\tilde{\mathbf{Q}}(z)\mathbf{S}_{\ell}+\frac{\delta_{k-\ell}\frac{N_{k}}{N}}{z\left(1+\sigma^{2}c m(z)\right)}\mathbf{I}\right\|_{2}\xrightarrow[M\rightarrow\infty]a.s.
$$  

and  

$$
\operatorname*{sup}_{\boldsymbol{z}\in\mathcal{K}}\left\|\frac{1}{N}\mathbf{S}_{k}^{\ast}\mathbf{W}^{\ast}\mathbf{Q}(\boldsymbol{z})\boldsymbol{\Omega}\right\|_{2}\xrightarrow[M\rightarrow\infty]{a.s.}0.
$$  

Proof.  Proposition 1 is obtained as a trivial modification of standard results in random matrix theory regarding quadratic forms of resolvents of standard Wishart matrices (see e.g. [33, Sec. 5.5]) and the proof is therefore omitted.  

Using Proposition 1, we deduce that:  

$$
\operatorname*{sup}_{z\in\mathcal{K}}\left\|\hat{\Xi}(z)-\Xi(z)\right\|_{2}\xrightarrow[M\rightarrow\infty]{a.s.}0,
$$  

where  

$$
\boldsymbol{\Xi}(z)=\left[\!\!\begin{array}{c c}{\sqrt{z}m(z)\boldsymbol{\Omega}^{*}\boldsymbol{\Omega}}&{\mathbf{0}}\\ {\mathbf{0}}&{\mathbf{A}(z)\}\end{array}\!\!\right],
$$  

with    $\mathbf{A}(z)$   the  $K L\times K L$   block diagonal matrix given by  

$$
\mathbf{A}(z)=-\frac{1}{\sqrt{z}\left(1+\sigma^{2}c m(z)\right)}\left[\begin{array}{l l l l}{\frac{N_{1}}{N}\mathbf{I}}&&&\\ &{\ddots}&&\\ &&{\frac{N_{L}}{N}\mathbf{I}}\end{array}\right].
$$  

It is straightforward to check that  

$$
\begin{array}{r}{\operatorname*{det}\left(\check{\mathbf{I}}+\Xi(z)\right)=\operatorname*{det}\left(\sqrt{z}m(z)\boldsymbol{\Omega}^{*}\boldsymbol{\Omega}\mathbf{A}(z)-\mathbf{I}\right)}\\ {=\operatorname*{det}\left(-\cfrac{m(z)}{1+\sigma^{2}c m(z)}\boldsymbol{\Gamma}-\mathbf{I}\right),}\end{array}
$$  

where    $\mathbf{\Gamma}$   is defined in (11). Consequently, from Assumption 2, one has  

$$
\operatorname*{sup}_{z\in\mathcal{K}}\left|\hat{P}(z)-P(z)\right|\xrightarrow[N\rightarrow\infty]{a.s.}0,
$$  

where    $\begin{array}{r l r}{P(z)}&{{}\!=\!}&{\prod_{k=1}^{K L}\left(-\frac{m(z)}{1+\sigma^{2}c m(z)}\gamma_{k}-1\right)}\end{array}$  Q   . Using the equation (59), one can rewrite  $P(z)$   $\begin{array}{r l}{P(z)}&{{}=}\end{array}$   $\begin{array}{r}{\prod_{k=1}^{\dot{\gamma}_{k}}\left(\frac{\dot{\gamma}_{k}}{w(z)-\sigma^{2}}-1\right)}\end{array}$   , with  $w$   defined in (60).  

4) Spectrum of    $\scriptstyle{\hat{\mathbf{R}}}$  :  Using Lemma 2 and the discussion below, we immediately obtain that the set of zeros of    $P$   is given by  

$$
\mathcal{Z}=\left\{\phi(\gamma_{k}+\sigma^{2}):k=1,.\,.\,.\,,K L,\ \gamma_{k}>\sigma^{2}\sqrt{c}\right\}.
$$  

Moreover, Lemma 2 also implies that    $P$   has no pole and thus  $P$   is holomorphic on    $\mathbb{C}\backslash[x^{-},x^{+}]$  .  

Let    $Q=|\mathcal{Z}|$    enote by  $x_{1}>\dots>x_{Q}$   the elements of  $\mathcal{Z}$  . We also set  $\epsilon>0$   small enough such that  

$$
\mathcal{D}_{\epsilon}\cap\bigcap_{q=1}^{Q}[x_{q}-\epsilon,x_{q}+\epsilon]=\emptyset.
$$  

For all    $q=1,\dots,Q$  , let    ${\mathcal{C}}_{q}$   be a continuously differentiable simple closed curve intersecting the real axis only at the two po  $x_{q}\pm\epsilon$  osing  $x_{q}$   so that  ${\mathcal{C}}_{q}$   is act subset of  $\mathbb{C}\backslash\left(\mathscr{D}_{\epsilon}\cup(-\infty,0)\right)$  \ D  ∪ −∞ . Applying (92) ith  K  $\mathcal{K}=\mathcal{C}_{q}$   C  provides that with probability one for all large  M ,  

$$
\left|\hat{P}(z)-P(z)\right|<\left|P(z)\right|,
$$  

$\hat{P}$  for all    $z\in\mathcal{C}_{q}$  , with both  and  P  being holomorphic on any open set enclosed by    ${\mathcal{C}}_{q}$  . Thus, r all    $q=1,\ldots,Q$  , we deduce from Rouch´ e’s Theorem that    $\hat{P}$   admits a unique zero in the interval    $[x_{q}-\epsilon,x_{q}+\epsilon]$  ning,  $\hat{P}$   does not have any zero in  $(0,x^{-}-\epsilon)\cup(x_{1}+\epsilon,\infty)$  −  ∪  ∞  with probability one for all large    $M$  . Therefore, getting back to (81) and since  $\epsilon$   can be made arbitrarily small, it follows that  

$$
\lambda_{k}\left(\hat{\bf R}\right)\xrightarrow[M\to\infty]{a.s.}\phi(\gamma_{k}+\sigma^{2})=\frac{(\gamma_{k}+\sigma^{2})(\gamma_{k}+\sigma^{2}c)}{\gamma_{k}},
$$  

for all    $k~=~1,.\ldots,K L$   such that    $\gamma_{k}~>~\sigma^{2}{\sqrt{c}}$  . Moreover, with probability one for all large    $M$  ,    $\lambda_{k}(\hat{\mathbf{R}})\;\in\;\mathcal{D}_{\epsilon}$   ∈D  for all  $k\,=\,1,.\,.\,.\,,K L$   suc tha  $\gamma_{k}\,\leq\,\sigma^{2}{\sqrt{c}}$  . Since the empirical spectral distribution  ˆ  of    $\hat{\mathbf{R}}$   converges a.s. to the Marcenko- Pastur distribution as    $M\rightarrow\infty$  , this further implies that for all    $k=1,\ldots,K L$   such that  $\begin{array}{r}{\gamma_{k}\leq\sigma^{2}\sqrt{c},\,\lambda_{k}\left(\hat{\bf R}\right)\xrightarrow[M\rightarrow\infty]{a.s.}x^{+}}\end{array}$      →∞ and similarly    $\lambda_{K L+1}\left({\hat{\mathbf{R}}}\right)\xrightarrow[M\rightarrow\infty]{a.s.}x^{+}$  . →∞  

C. Proof of Theorem 2  

1) Some notations.:  Let us first recall that under hypothesis

  ${\mathcal{H}}_{0}$   $\mathbf{\Gamma}_{1}~=~.\,.\,.~=~\mathbf{\Gamma}_{L}~=~\mathbf{\Gamma}$  , and e d

  $\mathbf{\Gamma}~=~\mathbf{{U}D U^{*}}$  its ei gen decomposition with  U  a  M  $M\,\times\,K$   × isometric matrix and    $\mathbf{D}=\operatorname{diag}\left(\lambda_{1}(\pmb{\Gamma}),.\,.\,,\lambda_{K}(\pmb{\Gamma})\right)$  . To unify some notations, define as in the previous section    $\begin{array}{r l}{\mathbf{Y}_{\boldsymbol{\ell}}}&{{}=}\end{array}$   $\left[\mathbf{y}_{1,\ell},\ldots,\mathbf{y}_{N_{\ell},\ell}\right]$   for all  $\ell=1,\ldots,L$   so that we have  

$$
\mathbf{Y}_{\ell}=\boldsymbol{\Omega}\mathbf{S}_{\ell}^{*}+\mathbf{W}_{\ell},
$$  

where    $\Omega=\mathbf{U}\mathbf{D}^{1/2}$  ,  $\mathbf{S}_{1},\dots,\mathbf{S}_{L}$   are independent matrices such that    $\mathbf{S}_{\ell}~=~\left[\mathbf{s}_{1,\ell},.~.~.~,\mathbf{s}_{K,\ell}\right]$   is    $N_{\ell}\,\times\,K$   with i.i.d.    ${\mathcal{N}}_{\mathbb{C}}(0,1)$  entries, and where    $\mathbf{W}_{1},\ldots,\mathbf{W}_{L}$   are independent matrices with    $\mathbf{W}_{\ell}$  having i.i.d.    $\mathcal{N}_{\mathbb{C}}(0,\sigma^{2})$   entries. We also define  $\mathbf{Y}_{0}=[\mathbf{Y}_{1},\dots,\mathbf{Y}_{L}]$   so that  

$$
\mathbf{Y}_{0}=\pmb{\Omega}\mathbf{S}_{0}^{*}+\mathbf{W}_{0},
$$  

with    $\mathbf{S}_{0}\ =\ [\mathbf{S}_{1}^{*},\dots,\mathbf{S}_{L}^{*}]^{*}$  and    $\mathbf{W}_{0}~=~[\mathbf{W}_{1},.\,.\,.\,,\mathbf{W}_{L}]$  , and write    $N_{0}~=~N_{1}+\ldots+N_{L}$  , so that    $\begin{array}{r}{\hat{\bf R}_{0}\ =\ \frac{{\bf Y}_{0}{\bf Y}_{0}^{*}}{N_{0}}\ =\ \hat{\bf R}}\end{array}$  . Moreover, let    $\begin{array}{r}{c_{0}=c=(\frac{1}{c_{1}}+.-.+\frac{1}{c_{L}})^{-1}}\end{array}$   and  

$$
a=\sigma^{2}\operatorname*{min}_{\ell=0,\ldots,L}\left(1-\sqrt{c_{\ell}}\right)^{2},\quad b=\sigma^{2}\operatorname*{max}_{\ell=0,\ldots,L}\left(1+\sqrt{c_{\ell}}\right)^{2},
$$  

and consider    $\varphi\in\mathcal{C}_{c}^{\infty}(\mathbb{R})$   such that    $\mathrm{supp}(\varphi)=[a-\epsilon,b+\epsilon]$  and    $\varphi(t)=1$   for all    $\begin{array}{r}{t\in\left[a-\frac{\epsilon}{2},b+\frac{\epsilon}{2}\right]}\end{array}$    , where    $\epsilon<a$   . The following quantity defined as  

$$
\chi=\prod_{\ell=0}^{L}\mathrm{det}\varphi\left(\frac{{\bf W}_{\ell}{\bf W}_{\ell}^{*}}{N_{\ell}}\right),
$$  

verifies    $\chi\ =\ 1$   with probability 1 for all large    $M$   from the classical results on the localization of the eigenvalues of Wishart  matrices [31]. Recall also the definition of    $m$   and    $w$   in (58) and (60) respectively and denote for all    $\ell=0,\ldots,L$   by  $m_{\ell}$  the  Stieltjes  transform of the  Marcenko-Pastur  distribution with parameter    $(c_{\ell},\sigma^{2})$  , as well as for all    $z\in\mathbb{C}\backslash[x_{\ell}^{-},x_{\ell}^{+}]$  

$$
\begin{array}{l}{{w_{\ell}(z)=z\left(1+\sigma^{2}c_{\ell}m_{\ell}(z)\right),}}\\ {{\tilde{m}_{\ell}(z)=-\displaystyle\frac{1}{z(1+\sigma^{2}c_{\ell}m_{\ell}(z))},}}\\ {{\tau_{\ell}(z)=z m_{\ell}(z)\tilde{m}(z),}}\end{array}
$$  

with    $x_{\ell}^{\pm}=\sigma^{2}\left(1\pm\sqrt{c_{\ell}}\right)^{2}$   ±  .  

2) Characteristic Polynomials Approximation: The first step of the proof consists in using the trick from [34] whose main idea is to relate the cumulative distribution function of the spiked eigenvalues with the determinant of certain random matrices.  

Using Theorem 1 and the same arguments used to obtain the factorization (81) and (83) in Appendix B, we have that  $\lambda_{1}(\hat{\mathbf{R}}_{\ell}),\dots,\lambda_{K}(\hat{\mathbf{R}}_{\ell})$   are the zeros of  

$$
\hat{P}_{\ell}(z)=\operatorname*{det}\left(\check{\mathbf{I}}+\hat{\Xi}_{\ell}(z)\right),
$$  

for all    $\ell\in\{0,\ldots,L\}$  , with probability one for all large    $M$  , with  

$$
\begin{array}{r}{\hat{\Xi}_{\ell}(z)=\left[\frac{\sqrt{z}\Omega^{*}{\mathbf{Q}}_{\ell}(z)\Omega\chi}{\frac{1}{N_{\ell}}\mathbf{S}_{\ell}^{*}\mathbf{W}_{\ell}^{*}\mathbf{Q}_{\ell}(z)\Omega\chi}\quad\frac{1}{N_{\ell}}\Omega^{*}{\mathbf{Q}}_{\ell}(z){\mathbf{W}_{\ell}}{\mathbf{S}_{\ell}}\chi\right],}\end{array}
$$  

where  $\begin{array}{r l r}{{\bf Q}_{\ell}(z)}&{{}=}&{\left(\frac{{\bf W}_{\ell}{\bf W}_{\ell}^{*}}{N_{\ell}}-z{\bf I}\right)^{-1}}\end{array}$   and  $\begin{array}{r l}{\tilde{\bf Q}_{\ell}(z)}&{{}=}\end{array}$   $\left(\frac{\mathbf{W}_{\ell}^{*}\mathbf{W}_{\ell}}{N_{\ell}}-z\mathbf{I}\right)^{-1}$   . For all    $\ell,k$  , let  −∞  $-\infty<x_{k,\ell}<y_{k,\ell}<+\infty$  ∞ and denote  

$$
\rho_{k,\ell}=\frac{\big(\gamma_{k}+\sigma^{2}\big)\big(\gamma_{k}+\sigma^{2}c_{\ell}\big)}{\gamma_{k}}.
$$  

Then with probability one for all large    $M$  , we have  

$$
\begin{array}{r l}&{\sqrt{M}\left(\lambda_{k}(\hat{\bf R}_{\ell})-\rho_{k,\ell}\right)\in[x_{k,\ell},y_{k,\ell}]}\\ &{\Leftrightarrow\hat{P}_{\ell}\left(\rho_{k,\ell}+\frac{x_{k,\ell}}{\sqrt{M}}\right)\!\hat{P}_{\ell}\left(\rho_{k,\ell}+\frac{y_{k,\ell}}{\sqrt{M}}\right)<0.}\end{array}
$$  

Therefore, as    $M\rightarrow\infty$  ,  

$$
\begin{array}{r l r}{\lefteqn{\mathbb{P}\left(\bigcap_{k=1}^{K}\bigcap_{\ell=0}^{L}\left\{\sqrt{M}\left(\lambda_{k}(\hat{\mathbf{R}}_{\ell})-\rho_{k,\ell}\right)\in[x_{k,\ell},y_{k,\ell}]\right\}\right)=}}\\ &{}&{\mathbb{P}\left(\bigcap_{k=1}^{K}\bigcap_{\ell=0}^{L}\left\{\hat{P}_{\ell}\left(\rho_{k,\ell}+\frac{x_{k,\ell}}{\sqrt{M}}\right)\hat{P}_{\ell}\left(\rho_{k,\ell}+\frac{y_{k,\ell}}{\sqrt{M}}\right)<0\right\}\right)}\\ &{}&{+\,o(1).}\end{array}
$$  

The following proposition provides the expansion of  $\begin{array}{r}{\hat{P}_{\ell}\left(\rho_{k,\ell}+\frac{x}{\sqrt{M}}\right)}\end{array}$    around    $\rho_{k,\ell}$  .  

# Proposition 2.  For all    $x\in\mathbb{R},$  ,  

$$
\begin{array}{l}{\displaystyle\hat{P}_{\ell}\left(\rho_{k,\ell}+\frac{x}{\sqrt{M}}\right)=\frac{1}{\sqrt{M}}\prod_{i\neq k}\left(\gamma_{i}\tau_{\ell}(\rho_{k,\ell})-1\right)\ ~}\\ {\displaystyle\quad\times\left(x\gamma_{k}\tau_{\ell}^{\prime}(\rho_{k,\ell})-2\sqrt{\gamma_{k}}\mathrm{Re}\left(\eta_{3,k,\ell}\right)+\gamma_{k}\rho_{k,\ell}\tilde{m}_{\ell}(\rho_{k,\ell})\eta_{1,k,\ell}\right.}\\ {\displaystyle\qquad\qquad\left.+\left.\gamma_{k}\rho_{k,\ell}m_{\ell}(\rho_{k,\ell})\eta_{2,k,\ell}\right)\right)+o_{\mathbb{P}}\left(\frac{1}{\sqrt{M}}\right),~~(109)}\end{array}
$$  

where    $\tau_{\ell}(z)=z m_{\ell}(z)\tilde{m}_{\ell}(z)$   and  

$$
\begin{array}{r l}&{\eta_{1,k,\ell}=\sqrt{M}\mathbf{u}_{k}^{*}\left(\mathbf{Q}_{\ell}(\rho_{k,\ell})\chi\right)^{\circ}\mathbf{u}_{k},}\\ &{\eta_{2,k,\ell}=\cfrac{\sqrt{M}}{N_{\ell}}\left(\mathbf{s}_{k,\ell}^{*}\mathbf{\tilde{Q}}_{\ell}(\rho_{k,\ell})\mathbf{s}_{k,\ell}\chi\right)^{\circ},}\\ &{\eta_{3,k,\ell}=\cfrac{\sqrt{M}}{N_{\ell}}\mathbf{u}_{k}^{*}\mathbf{Q}_{\ell}(\rho_{k,\ell})\mathbf{W}_{\ell}\mathbf{s}_{k,\ell}\chi.}\end{array}
$$  

Proof.  The proof is deferred to Appendix E1.  

From (108) and Proposition 2, it is clear that we have to study a CLT for the following generic quantity  

$$
\eta=\sum_{\ell=0}^{L}\sum_{k=1}^{K}\left(\beta_{1,k,\ell}\eta_{1,k,\ell}+\beta_{2,k,\ell}\eta_{2,k,\ell}+\mathrm{Re}\left(\overline{{\beta_{3,k,\ell}}}\eta_{3,k,\ell}\right)\right),
$$  

where    $\begin{array}{r l}{\left(\beta_{i,k,\ell}\right)\,\,\,{=}1,2}&{{}\,\,\,\in\,\,\mathbb{R}^{2K(L+1)}}\end{array}$  ∈   and    $(\beta_{3,k,\ell})_{k=1,\ldots,K}\;\in$  ∈  $k{=}1,{\ldots},K$   $\ell{=}0,\ldots,L$   $\ell{=}0,\ldots,L$   $\mathbb{C}^{K(L+1)}$  .  

3) Central Limit Theorem:  Let us consider the characteris- tic function    $\Psi(u)=\mathbb{E}\left[\xi(u)\right]$  , with    $\xi(u)=\exp\left(\mathrm{i}u\eta\right)$  . Our ap- proach consists in deriving a perturbed differential equation for  $\Psi$   as shown in the following proposition. Let  bdiag()  denotes the block diagonal operator. Define    $\mathbf{K}=\mathrm{bdiag}\left(\mathbf{K}_{1},.\.\,.\,,\mathbf{K}_{K}\right)$  with    $\mathbf{K}_{k}=\mathrm{bdiag}(\mathbf{K}_{1,k},.\,.\,.\,,\mathbf{K}_{4,k})$   and where    $(\mathbf{K}_{i,k})_{i=1,\dots,4}$  are    $(L+1)\times(L+1)$   symmetric matrices with entries given by  

$$
\begin{array}{r l}&{[\mathbf{K}_{1,k}]_{\ell+1,\ell^{\prime}+1}=}\\ &{\left\{\begin{array}{l l}{\frac{\sigma^{4}c_{\ell}}{(\gamma_{k}+\sigma^{2}c_{\ell})^{2}(\gamma_{k}^{2}-\sigma^{4}c_{\ell})}}&{\mathrm{if~}\ell=\ell^{\prime}}\\ {\frac{\sigma^{4}c_{0}}{(\gamma_{k}+\sigma^{2}c_{0})(\gamma_{k}+\sigma^{2}c_{\ell^{\prime}})(\gamma_{k}^{2}-\sigma^{4}c_{0})}}&{\mathrm{if~}\ell=0<\ell^{\prime}\ ,}\\ {0}&{\mathrm{if~}0<\ell<\ell^{\prime}}\end{array}\right.}\end{array}
$$  

$$
\begin{array}{r}{[\mathbf{K}_{2,k}]_{\ell+1,\ell^{\prime}+1}=\left\{\begin{array}{l l}{\frac{c_{\ell}}{(\gamma_{k}+\sigma^{2})^{2}(\gamma_{k}^{2}-\sigma^{4}c_{\ell})}}&{\mathrm{if~}\ell=\ell^{\prime}}\\ {\quad}\\ {\frac{c_{0}}{(\gamma_{k}+\sigma^{2})^{2}(\gamma_{k}^{2}-\sigma^{4}c_{0})}}&{\mathrm{if~}\ell=0<\ell^{\prime}\ ,}\\ {0}&{\mathrm{if~}0<\ell<\ell^{\prime}}\end{array}\right.}\end{array}
$$  

and for    $i\in\{3,4\}$  ,  

$$
[\mathbf{K}_{i,k}]_{\ell+1,\ell^{\prime}+1}=\left\{\begin{array}{l l}{\frac{1}{2}\frac{\sigma^{2}c_{\ell}}{\gamma_{k}^{2}-\sigma^{4}c_{\ell}}\quad\mathrm{if~}\ell=\ell^{\prime}}\\ {\quad}\\ {\frac{1}{2}\frac{\sigma^{2}c_{0}}{\gamma_{k}^{2}-\sigma^{4}c_{0}}\quad\mathrm{if~}\ell=0<\ell^{\prime}}\\ {0\quad\quad}\\ {\quad\mathrm{if~}0<\ell<\ell^{\prime}}\end{array}\right.
$$  

Denote also  ${\boldsymbol{\beta}}=\left({\boldsymbol{\beta}}_{1}^{T},.\,.\,.\,,{\boldsymbol{\beta}}_{K}^{T}\right)^{T}$   with  

$$
\begin{array}{r l}&{\beta_{k}=\Bigl(\beta_{1,k,0},\ldots,\beta_{1,k,L},\beta_{2,k,0},\ldots,\beta_{2,k,L},}\\ &{\quad\mathrm{Re}(\beta_{3,k,0}),\ldots,\mathrm{Re}(\beta_{3,k,L}),\mathrm{Im}(\beta_{3,k,0}),\ldots,\mathrm{Im}(\beta_{3,k,L})\Bigr)^{T}.}\end{array}
$$  

Proposition 3.  The matrix    $\mathbf{K}$   is positive definite and  

$$
\Psi^{\prime}(u)=-u\beta^{T}{\bf K}\beta\Psi(u)+\frac{\Delta(u)}{\sqrt M},
$$  

where    $\Delta$  is a contin us function such that    $|\Delta(u)|\,<\,\mathrm{P}(u)$  for some polynomial  P  with positive coefficients independent of    $M$  .  

From Proposition 3, by solving the perturbed differential equation in (118), we deduce that  

$$
\Psi(u)\xrightarrow[M\to\infty]{}\exp\left(-\beta^{T}\mathbf{K}\beta\frac{u^{2}}{2}\right),
$$  

which of course implies that  

$$
\eta\xrightarrow[M\rightarrow\infty]{\mathcal{D}}\mathcal{N}_{\mathbb{R}}\left(0,\beta^{T}\mathbf{K}\beta\right).
$$  

The final step of the proof consists in transferring the CLT to the    $K$   largest eigenvalues of    $(\hat{\bf R}_{\ell})_{\ell=1,\ldots,L}$  . From Proposition (2), we have that:  

$$
\begin{array}{r l r}{\lefteqn{\hat{P}_{\ell}\left(\rho_{k,\ell}+\frac{x}{\sqrt{M}}\right)=}}\\ &{}&{\frac{1}{\sqrt{M}}\gamma_{k}\tau_{\ell}^{\prime}(\rho_{k,\ell})\left(x-\zeta_{k,\ell}+o_{\mathbb{P}}\left(1\right)\right)\prod_{i\neq k}\left(\gamma_{i}\tau_{\ell}(\rho_{k,\ell})-1\right),}\end{array}
$$  

with  

$$
\begin{array}{c}{{\zeta_{k,\ell}=\displaystyle\frac{1}{\gamma_{k}\tau_{\ell}^{\prime}(\rho_{k,\ell})}\Big(2\sqrt{\gamma_{k}}\mathrm{Re}\,\big(\eta_{3,k,\ell}\big)-\gamma_{k}\rho_{k,\ell}\tilde{m}_{\ell}(\rho_{k,\ell})\eta_{1,k,\ell}\Big.}}\\ {{\Big.-\gamma_{k}\rho_{k,\ell}m_{\ell}(\rho_{k,\ell})\eta_{2,k,\ell}\Big).\quad\quad\quad\quad}}\end{array}\quad(122)
$$  

Thus, going back to (108), we get  

$$
\begin{array}{r l}&{\mathbb{P}\left(\displaystyle\bigcap_{k=1}^{K}\displaystyle\bigcap_{\ell=0}^{L}\left\{\sqrt{M}\left(\lambda_{k}(\hat{\bf R}_{\ell})-\rho_{k,\ell}\right)\in[x_{k,\ell},y_{k,\ell}]\right\}\right)=}\\ &{\quad\mathbb{P}\left(\displaystyle\bigcap_{k=1}^{K}\displaystyle\bigcap_{\ell=0}^{L}\left\{x_{k,\ell}<\zeta_{k,\ell}+o_{\mathbb{P}}(1)<y_{k,\ell}\right\}\right)+o(1).\ \ (\ref{e q u m a t i o n})}\end{array}
$$  

Using (120) with suitable values for    $\beta$   as well as the equal- ities of Lemma 3, we have  ζ  $\zeta\;\;=\;\;\left(\zeta_{k,\ell}\right)_{\ell=0,\ldots,L}\;\;\xrightarrow[M\rightarrow\infty]{\bar{\mathcal{D}}}$   $\mathcal{N}_{\mathbb{R}^{K(L+1)}}\left(\mathbf{0},\Theta\right)$  , where    $\Theta$   is given in the statement of Theo- rem 2. Finally, noticing that  

$$
\begin{array}{r l}&{\operatorname*{det}(\pmb{\Theta})=\displaystyle\prod_{k=1}^{K}\displaystyle\prod_{\ell=1}^{L}\theta_{k,\ell}^{2}\left(\theta_{0}^{2}-\displaystyle\sum_{\ell^{\prime}=1}^{L}\frac{\vartheta_{k,\ell^{\prime}}^{2}}{\theta_{k,\ell}^{2}}\right)}\\ &{\qquad\qquad=\left(\sigma^{4}c_{0}^{2}(L-1)\right)^{K}\displaystyle\prod_{k=1}^{K}\left(\frac{\gamma_{k}+\sigma^{2}}{\gamma_{k}}\right)^{2(L+1)}}\\ &{\qquad\qquad\qquad\qquad\qquad\qquad\qquad\times\displaystyle\prod_{\ell=1}^{L}c_{\ell}(\gamma_{k}^{2}-\sigma^{4}c_{\ell}),}\end{array}
$$  

we obtain that    $\operatorname*{det}(\Theta)\,>\,0$   thanks to Assumption 3 which concludes the proof of Theorem 2.  

D. Proof of Corollary 2  

Denote    $c_{0}~=~c$   and for all    $\ell\ =\ 0,\ldots,L$  , let    $\hat{\phi}_{\ell}(w)\;=\;$   $\begin{array}{r}{w\left(1-\frac{\hat{\sigma}^{2}c_{\ell}}{\hat{\sigma}^{2}-w}\right)}\end{array}$    . Denote as well  $\hat{\bf R}_{0}=\hat{\bf R}$   and    $\hat{\gamma}_{k,0}\,=\,\hat{\gamma}_{k}$   for ease of reading. Under Assumption 3, we first observe from Theorem 1 that  

$$
\lambda_{k}\left(\hat{\bf R}_{\ell}\right)\xrightarrow[M\to\infty]{a.s.}\phi_{\ell}(\gamma_{k}+\sigma^{2})=\frac{(\gamma_{k}+\sigma^{2})(\gamma_{k}+\sigma^{2}c_{\ell})}{\gamma_{k}},
$$  

Proof.  The proof is deferred to Appendix E2.  

so that  $\hat{\lambda}_{k}(\hat{\bf R}_{\ell})>\hat{\sigma}^{2}\sqrt{c_{\ell}}$  with probability one for all large    $M$  , and therefore    $\hat{\gamma}_{k,\ell}+\hat{\sigma}^{2}$    coincides with the largest solution to the equation  $\hat{\phi}_{\ell}(\mathcal{\dot{w}})=\lambda_{k}(\hat{\mathbf{R}}_{\ell})$  . From Lemma 2, we deduce that  $\hat{\gamma}_{k,\ell}=\hat{w}_{\ell}\left(\hat{\lambda}_{k}(\hat{\bf R}_{\ell})\right)-\hat{\sigma}^{2}$   . with probability one for all large  $M$  , where  $\begin{array}{r}{\grave{w}_{\ell}(z)=\,z\left(1+\hat{\sigma}^{2}c_{\ell}\hat{m}_{\ell}(z)\right)}\end{array}$     with  $\hat{m}_{\ell}$  the Stieltjes transform of the Marcenko-Pastur distribution with parameter  $(\hat{\sigma}^{2},c_{\ell})$  . It is easy to see that  $\begin{array}{r}{\hat{\sigma}^{2}=\sigma^{2}+\mathcal{O}_{\mathbb{P}}\left(\frac{1}{M}\right)}\end{array}$   O and:  

$$
{\hat{m}}_{\ell}\left({\hat{\lambda}}_{k}({\hat{\mathbf{R}}}_{\ell})\right)=m_{\ell}\left({\hat{\lambda}}_{k}({\hat{\mathbf{R}}}_{\ell})\right)+{\mathcal{O}}_{\mathbb{P}}\left({\frac{1}{M}}\right).
$$  

Therefore, we deduce that  

$$
\hat{\gamma}_{k,\ell}=w_{\ell}\left(\hat{\lambda}_{k}(\hat{\mathbf{R}}_{\ell})\right)-\sigma^{2}+\mathcal{O}_{\mathbb{P}}\left(\frac{1}{M}\right).
$$  

As  $w_{\ell}\big(\phi_{\ell}\big(\gamma_{k}\!+\!\sigma^{2}\big)\big)=\gamma_{k}\!+\!\sigma^{2}$    and  $w_{\ell}$  is differentiable at point  $\gamma_{k}+\sigma^{2}$  , a straightforward use of the delta-method provides  

$$
\sqrt{M}\left(\hat{\gamma}_{k,\ell}-\gamma_{k}\right)_{\stackrel{\ell=0,\ldots,L}{k=1,\ldots,K}}\xrightarrow[M\rightarrow\infty]{\mathcal{D}}\mathcal{N}_{\mathbb{R}^{K(L+1)}}\left(\mathbf{0},\mathbf{G}\pmb{\Theta}\mathbf{G}\right),
$$  

where    $\textbf{G}=\mathrm{~diag}\left((w_{\ell}^{\prime}(\phi_{\ell}(\gamma_{k}+\sigma^{2})))_{\ell=0,...,L}\right)$  . Noticing that    $\begin{array}{r l r}{w_{\ell}^{\prime}\big(\phi_{\ell}\big(\gamma_{k}\,+\,\sigma^{2}\big)\big)\!\!}&{{}=}&{\!\!\frac{\gamma_{k}^{2}}{\gamma_{k}^{2}-\sigma^{2}c_{\ell}}}\end{array}$  from Lemma 3, we end k up with    $\mathbf{G}\Theta\mathbf{G}\,=\,\Omega$  , where  Ω is given in the statement of Corollary 2. Another immediate use of the delta-method allows to transfer the CLT from    $\left(\hat{\gamma}_{k,\ell}\right)_{\ell=0,\dots,L}$  to    $\hat{\gamma}$  .  $k{=}1,{\ldots},K$  

E. Additional proofs  

1) Proof of Proposition 2:  It is easy to see using Proposi- tion 1 that for all    $x\in\mathbb{R}$  ,  

$$
\begin{array}{r l}{\hat{\boldsymbol{\Xi}}_{\ell}\left(\rho_{k,\ell}+\cfrac{x}{\sqrt{M}}\right)=}&{{}}\\ {\left[\sqrt{\rho_{k,\ell}}m_{\ell}(\rho_{k,\ell})\mathbf{D}\right.}&{{}\left.\mathbf{0}\right.}\\ {\left.\mathbf{0}\right.}&{{}\sqrt{\rho_{k,\ell}}\tilde{m}_{\ell}(\rho_{k,\ell})\mathbf{I}\right]+\Delta,}\end{array}
$$  

where  

$$
\begin{array}{r l}&{\mathbf{\Delta}=}\\ &{\left[\sqrt{\rho_{k,\ell}}\Omega^{*}\left(\mathbf{Q}_{\ell}(\rho_{k,\ell})\boldsymbol{\chi}\right)^{\circ}\Omega\qquad\frac{1}{N_{\ell}}\Omega^{*}\mathbf{Q}_{\ell}(\rho_{k,\ell})\boldsymbol{\chi}\mathbf{W}_{\ell}\mathbf{S}_{\ell}\right.}\\ &{\left.\left[\frac{1}{N_{\ell}}\mathbf{S}_{\ell}^{*}\mathbf{W}_{\ell}^{*}\mathbf{Q}_{\ell}(\rho_{k,\ell})\boldsymbol{\chi}\Omega\qquad\sqrt{\rho_{k,\ell}}\frac{1}{N_{\ell}}\left(\mathbf{S}_{\ell}^{*}\tilde{\mathbf{Q}}_{\ell}(\rho_{k,\ell})\mathbf{S}_{\ell}\boldsymbol{\chi}\right)^{\circ}\right]\right.}\\ &{+\left.\cfrac{x}{\sqrt{M}}\left[h\left(\rho_{k,\ell}\right)\mathbf{D}\qquad\mathbf{0}\qquad\right.}\\ &{\qquad\left.\mathbf{0}\qquad\qquad\tilde{h}\left(\rho_{k,\ell}\right)\mathbf{I}\right]+o_{\mathbb{P}}\left(\cfrac{1}{\sqrt{M}}\right),\qquad(130)}\end{array}
$$  

with    $\begin{array}{l}{{h_{\ell}(z)~=~\frac{m_{\ell}(z)}{2\sqrt{z}}\,+\,\sqrt{z}m_{\ell}^{\prime}(z)}}\end{array}$   and    $\begin{array}{r l r}{\tilde{h}_{\ell}(z)\!\!}&{{}=}&{\!\!\frac{\tilde{m}_{\ell}(z)}{2\sqrt{z}}\,+}\end{array}$   $\sqrt{z}\tilde{m}_{\ell}^{\prime}(z)$  . Note that  $\begin{array}{r}{\left\|\pmb{\Delta}\right\|_{2}=\mathcal{O}_{\mathbb{P}}\left(\frac{1}{\sqrt{M}}\right)}\end{array}$    and we also consider the partition    $\pmb{\Delta}\ =\ (\pmb{\Delta}_{i,j})_{i,j=1,2}$   where each block    $\Delta_{i,j}$   is  $K{\times}K$  . Consider the event  $\bar{\mathcal{A}}=\left\{\|\pmb{\Delta}_{2,2}\|_{2}<\sqrt{\rho_{k,\ell}}\tilde{m}_{\ell}(\rho_{k,\ell})\right\}$     	 . From the block matrix determinant formula, we have:  

$$
\hat{P}_{\ell}\left(\rho_{k,\ell}+\frac{x}{\sqrt{M}}\right)\mathbb{1}_{A}=\Phi\,\operatorname*{det}\left(\sqrt{\rho_{k,\ell}}\tilde{m}_{\ell}(\rho_{k,\ell})\mathbf{I}+\pmb{\Delta}_{2,2}\right)\mathbb{1}_{A},
$$  

with  

$$
\begin{array}{r l}&{\Phi=\operatorname*{det}\biggl(\sqrt{\rho_{k,\ell}}m_{\ell}(\rho_{k,\ell})\mathbf{D}+\pmb{\Delta}_{1,1}}\\ &{-\left(\mathbf{I}+\pmb{\Delta}_{2,1}\right)\Bigl(\sqrt{\rho}_{k,\ell}\tilde{m}_{\ell}(\rho_{k,\ell})\mathbf{I}+\pmb{\Delta}_{2,2}\Bigr)^{-1}\left(\mathbf{I}+\pmb{\Delta}_{1,2}\right)\biggr)\mathbb{1}_{A}.}\end{array}
$$  

Moreover,  

$$
\begin{array}{r l}&{\bigg(\sqrt{\rho}_{k,\ell}\tilde{m}_{\ell}(\rho_{k,\ell}){\mathbf I}+\pmb{\Delta}_{2,2}\bigg)^{-1}\mathbb{1}_{\mathcal{A}}=}\\ &{\bigg(\frac{\mathbf I}{\sqrt{\rho_{k,\ell}}\tilde{m}_{\ell}(\rho_{k,\ell})}-\frac{\pmb{\Delta}_{2,2}}{\rho_{k,\ell}\tilde{m}_{\ell}(\rho_{k,\ell})^{2}}\bigg)\mathbb{1}_{\mathcal{A}}+o_{\mathbb{P}}\left(\frac1{\sqrt{M}}\right),}\end{array}
$$  

which yields  

$$
\begin{array}{r l}&{\Phi=\mathrm{det}\bigg(\sqrt{\rho_{k,\ell}}m_{\ell}(\rho_{k,\ell}){\bf D}-\frac{{\bf I}}{\sqrt{\rho_{k,\ell}}\tilde{m}_{\ell}\left(\rho_{k,\ell}\right))}+\Delta_{1,1}}\\ &{\qquad\mathrm-\,\frac{\Delta_{1,2}+\Delta_{2,1}}{\sqrt{\rho_{k,\ell}}\tilde{m}_{\ell}\left(\rho_{k,\ell}\right)}+\frac{\Delta_{2,2}}{\rho_{k,\ell}\tilde{m}_{\ell}\left(\rho_{k,\ell}\right)^{2}}\bigg)\mathbb{1}_{A}+o_{\mathbb{P}}\left(\frac{1}{\sqrt{M}}\right).}\end{array}
$$  

Since    $\begin{array}{r}{\mathbf{D}=\mathrm{diag}(\gamma_{1},\dots,\gamma_{K})+o\left(\frac{1}{\sqrt{M}}\right)}\end{array}$    from Assumption 2, and from Lemma 3, we have  

$$
\operatorname*{det}\left(\sqrt{\rho_{k,\ell}}m_{\ell}(\rho_{k,\ell}){\bf D}-\frac{{\bf I}}{\sqrt{\rho_{k,\ell}}\tilde{m}_{\ell}(\rho_{k,\ell})}\right)=o\left(\frac{1}{\sqrt{M}}\right).
$$  

Using the differential of the determinant, we further have  

$$
\begin{array}{r l}&{\Phi=\mathrm{tr}\Bigg[\mathrm{com}\left(\sqrt{\rho_{k,\ell}}m_{\ell}(\rho_{k,\ell}){\bf D}-\frac{{\bf I}}{\sqrt{\rho_{k,\ell}}\tilde{m}_{\ell}(\rho_{k,\ell})}\right)^{T}}\\ &{\quad\times\left({\bf A}_{1,1}-\frac{{\bf A}_{1,2}+{\bf A}_{2,1}}{\sqrt{\rho_{k,\ell}}\tilde{m}_{\ell}(\rho_{k,\ell})}+\frac{{\bf A}_{2,2}}{\rho_{k,\ell}\tilde{m}_{\ell}(\rho_{k,\ell})^{2}}\right)\Bigg]\mathbb{1}_{A}}\\ &{\quad+\,o_{\mathbb{P}}\left(\frac{1}{\sqrt{M}}\right),\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad(1\}\end{array}
$$  

where    $\mathrm{{com}()}$   denotes the comatrix operation. A direct com- putation together with Assumption 2 provides  

$$
\begin{array}{r l r}{\lefteqn{\mathrm{com}\left(\sqrt{\rho_{k,\ell}}m_{\ell}(\rho_{k,\ell})\mathbf{D}-\frac{\mathbf{I}}{\sqrt{\rho_{k,\ell}}\tilde{m}_{\ell}\left(\rho_{k,\ell}\right)}\right)=}}\\ &{}&{\frac{\prod_{i\neq k}\left(\gamma_{i}\rho_{k,\ell}m_{\ell}(\rho_{k,\ell})\tilde{m}_{\ell}\left(\rho_{k,\ell}\right)-1\right)}{\left(\sqrt{\rho_{k,\ell}}\tilde{m}_{\ell}\left(\rho_{k,\ell}\right)\right)^{K-1}}\mathbf{e}_{k}\mathbf{e}_{k}^{*}+o\left(\frac{1}{\sqrt{M}}\right).}\end{array}
$$  

Consequently,  

$$
\begin{array}{r}{\Phi=o_{\mathbb{P}}\left(\displaystyle\frac{1}{\sqrt{M}}\right)+\displaystyle\frac{\prod_{i\neq k}\left(\gamma_{i}\rho_{k,\ell}m_{\ell}(\rho_{k,\ell})\tilde{m}_{\ell}(\rho_{k,\ell})-1\right)}{\left(\sqrt{\rho_{k,\ell}}\tilde{m}_{\ell}(\rho_{k,\ell})\right)^{K-1}}\ }\\ {\times\left[\pmb{\Delta}_{1,1}-\frac{\pmb{\Delta}_{1,2}+\pmb{\Delta}_{2,1}}{\sqrt{\rho_{k,\ell}}\tilde{m}_{\ell}(\rho_{k,\ell})}+\frac{\pmb{\Delta}_{2,2}}{\rho_{k,\ell}\tilde{m}_{\ell}(\rho_{k,\ell})^{2}}\right]_{k,k}\mathbb{1}_{\mathcal{A}}.}\end{array}
$$  

In the same way,  

$$
\begin{array}{r l}{\lefteqn{\operatorname*{det}\left(\sqrt{\rho_{k,\ell}}\tilde{m}_{\ell}(\rho_{k,\ell})\mathbf{I}+\pmb{\Delta}_{2,2}\right)=}}\\ &{\qquad\qquad\qquad\left(\sqrt{\rho_{k,\ell}}\tilde{m}_{\ell}(\rho_{k,\ell})\right)^{K}+\mathcal{O}_{\mathbb{P}}\left(\frac{1}{\sqrt{M}}\right),}\end{array}
$$  

so that  

$$
\begin{array}{r l}&{\hat{P}_{\ell}\left(\rho_{k,\ell}+\cfrac{x}{\sqrt{M}}\right)\mathbb{1}_{A}=}\\ &{\,\,\left[\sqrt{\rho_{k,\ell}}\tilde{m}_{\ell}(\rho_{k,\ell})\pmb{\Delta}_{1,1}+\cfrac{\pmb{\Delta}_{2,2}}{\sqrt{\rho_{k,\ell}}\tilde{m}_{\ell}\left(\rho_{k,\ell}\right)}-\left(\pmb{\Delta}_{1,2}+\pmb{\Delta}_{2,1}\right)\right]_{k,k}}\\ &{\times\displaystyle\prod_{i\neq k}\left(\gamma_{i}\rho_{k,\ell}m_{\ell}(\rho_{k,\ell})\tilde{m}_{\ell}(\rho_{k,\ell})-1\right)+o_{\mathbb{P}}\left(\cfrac{1}{\sqrt{M}}\right).\eqno(140)}\end{array}
$$  

Since    $\mathbb{1}_{\mathcal{A}}=1+o_{\mathbb{P}}(1)$  , we also deduce that  

$$
\hat{P}_{\ell}\left(\rho_{k,\ell}+{\frac{x}{\sqrt{M}}}\right)\mathbb{1}_{{\mathcal A}^{c}}=o_{\mathbb{P}}\left({\frac{1}{\sqrt{M}}}\right),
$$  

and using Assumption 2 leads to the result of Proposition 2. 2) Proof of Proposition   $3.$  :  The proof makes use of well- known techniques specific to the Gaussian distribution, namely the  Stein’s lemma  and the  Poincar´ e’s inequality  which we recall below and which have already been exploited in e.g. [35], [15], [24]. Therefore, we only give the main steps of the proof and skip some details of the computations.  

a) Useful  $f~:~\mathbb{C}^{n}~\to~\mathbb{C}$  o be    ${\mathcal{C}}^{1}(\mathbb{C}^{n})$   if  f  $f(\mathbf{z})\ =\ \tilde{f}(\mathrm{Re}(\mathbf{z}),\mathrm{Im}\dot{\mathbf{(z}}))$   with    $\tilde{f}\,\in\,\mathcal{C}^{1}(\mathbb{R}^{2n})$   ∈C . Moreover, we also recall the definition of the standard complex differential operators  

$$
\begin{array}{l}{\displaystyle\frac{\partial f}{\partial z_{k}}({\bf z})=\frac{1}{2}\left(\frac{\partial\widetilde{f}}{\partial x_{k}}({\bf x},{\bf y})-\mathrm{i}\frac{\partial\widetilde{f}}{\partial y_{k}}({\bf x},{\bf y})\right)}\\ {\displaystyle\frac{\partial f}{\partial\overline{{z_{k}}}}({\bf z})=\frac{1}{2}\left(\frac{\partial\widetilde{f}}{\partial x_{k}}({\bf x},{\bf y})+\mathrm{i}\frac{\partial\widetilde{f}}{\partial y_{k}}({\bf x},{\bf y})\right)}\end{array}
$$  

with    $\mathbf{x}=\operatorname{Re}(\mathbf{z})$   and    $\mathbf{y}=\operatorname{Im}(\mathbf{z})$  .  

a 4  (Stein’s lemma) .  Let  w    $\mathbf{\}\sim\ {\mathcal{N}}_{\mathbb{C}^{n}}(\mathbf{0},\mathbf{I})$   and    $f~\in$   ${\mathcal{C}}^{1}(\mathbb{C}^{n})$  C , assumed polynomially gether with its partial derivatives. Then for all  $k=1,\ldots,n,$  ,  

$$
\mathbb{E}[f(\mathbf{w})w_{k}]=\mathbb{E}\left[\frac{\partial f}{\partial\overline{{w_{k}}}}(\mathbf{w})\right],\ \mathbb{E}[f(\mathbf{w})\overline{{w_{k}}}]=\mathbb{E}\left[\frac{\partial f}{\partial w_{k}}(\mathbf{w})\right].
$$  

Lemma 5  (Poincar´ e inequality) .  Let    $\mathbf{w}\ \sim\ {\mathcal{N}}_{\mathbb{C}^{n}}(\mathbf{0},\mathbf{I})$   and  $f\,\in\,\mathcal{C}^{1}(\mathbb{C}^{n})$  , assumed polynomially bounded together with its partial derivatives. Then,  

$$
\mathbb{V}[f(\mathbf{w})]\leq\sum_{k=1}^{n}\left(\mathbb{E}\left|{\frac{\partial f}{\partial\overline{{w}}_{k}}}(\mathbf{w})\right|^{2}+\mathbb{E}\left|{\frac{\partial f}{\partial w_{k}}}(\mathbf{w})\right|^{2}\right).
$$  

For ease of reading, we introduce the following differentia-  operators with respect to the entries of the    $M\times N_{\ell}$  matrix  $\mathbf{W}_{\ell}$  , which will be constantly used in the derivations below,  

$$
\partial_{i,j}^{(\ell)}=\frac{\partial}{\partial[\mathbf{W}_{\ell}]_{i,j}},\quad\overline{{\partial}}_{i,j}^{(\ell)}=\frac{\partial}{\partial[\mathbf{W}_{\ell}]_{i,j}}.
$$  

We will also need the following auxiliary result (see [33]) related to the quantity    $\chi$   defined in (100).  

Lemma 6.  For all    $p\in\mathbb N$   and  $\begin{array}{r}{r\in\mathbb{N},\;\mathbb{E}\left[\chi^{r}\right]=1+\mathcal{O}\left(\frac{1}{N^{p}}\right)}\end{array}$  N and for    $\ell\,\in\,\{0,.\,.\,.\,,L\}$   and for any  $i\;\in\;\{1,.\,.\,.\,,M\},$   ∈{ }  $j\ \in$   ∈  $\{1,.\,.\,.\,,N_{\ell}\}$  ,  

$$
\mathbb{E}\left[\partial_{i,j}^{(\ell)}\chi^{r}\right]=\mathcal{O}\left(\frac{1}{N^{p}}\right)\:a n d\:\mathbb{E}\left[\overline{{\partial}}_{i,j}^{(\ell)}\chi^{r}\right]=\mathcal{O}\left(\frac{1}{N^{p}}\right).
$$  

Lemma 6 shows in particular that the presence of the regularization term    $\chi$   can be removed from expectations, up to an error term of arbitrary polynomial decay.  

In the following,    $\Delta$  is a generic notation for a continuous function such that  $|\Delta(u)|<\mathrm{P}(u)$   fo ome polynomial  $\mathrm{P}$   with positive coefficients independent of  M , and whose value may change from one line to another.  

$b$  ) Development of    $\Psi^{\prime}$  :  Write  

$$
\begin{array}{r l}&{\Psi^{\prime}(u)=\mathrm{i}\displaystyle\sum_{k=1}^{K}\sum_{\ell=0}^{L}\mathbb{E}\Bigg[\Bigg(\beta_{1,k,\ell}\eta_{1,k,\ell}+\beta_{2,k,\ell}\eta_{2,k,\ell}}\\ &{\qquad\qquad\qquad\quad+\operatorname{Re}\Bigg(\overline{{\beta_{3,k,\ell}}}\eta_{3,k,\ell}\Bigg)\Bigg)\xi(u)\Bigg].}\end{array}
$$  

In the following, we only provide some details for the devel- opment of    $\mathbb{E}[\eta_{1,k,0}\xi(u)]$  , as the other terms can be obtained similarly. Using the resolvent identity, we start by writing  

$$
\mathbb{E}\left[\eta_{1,k,0}\xi(u)\right]=\frac{\sqrt{M}}{\rho_{k,0}}\mathbb{E}\left[\left(\mathbf{u}_{k}^{*}\mathbf{Q}_{0}(\rho_{k,0})\frac{\mathbf{W}_{0}\mathbf{W}_{0}^{*}}{N_{0}}\mathbf{u}_{k}\chi\right)^{\circ}\xi(u)\right].
$$  

Next, we apply Stein’s lemma, Poincar´ e’s inequality and Lemma 6 to obtain  

$$
\begin{array}{r l}&{\mathbb{E}\left[\mathbf{u}_{k}^{*}\mathbf{Q}_{0}(\rho_{k,0})\frac{\mathbf{W}_{0}\mathbf{W}_{0}^{*}}{N_{0}}\mathbf{u}_{k}\chi\xi(u)\right]=}\\ &{\quad\quad\frac{\mathrm{i}u\sigma^{2}\sum_{i,j}\mathbb{E}\left[[\mathbf{u}_{k}^{*}\mathbf{Q}_{0}(\rho_{k,0})]_{i}[\mathbf{W}_{\ell}^{*}\mathbf{u}_{k}]_{j}\chi\overline{{\partial}}_{i,j}^{(0)}\{\eta\}\xi(u)\right]}{N_{0}(1+\alpha_{0}(\rho_{k,0}))}}\\ &{\quad\quad\quad+\frac{\sigma^{2}\mathbb{E}\left[\mathbf{u}_{k}^{*}\mathbf{Q}_{0}(\rho_{k,0})\mathbf{u}_{k}\chi\xi(u)\right]}{1+\alpha_{0}(\rho_{k,0})}+\frac{\Delta(u)}{M},\qquad\quad(\xi=\xi_{0})}\end{array}
$$  

where  $\begin{array}{r}{\alpha_{\ell}(z)=\mathbb{E}\left[\frac{\sigma^{2}}{N_{\ell}}\mathrm{tr}{\mathbf{Q}_{\ell}(z)\chi}\right]}\end{array}$  h for all    $\ell=0,\ldots,L$  . Using the fact that  $\begin{array}{r}{\alpha_{0}\big(\bar{\rho_{k,0}}\big)=\sigma^{2}c_{0}\bar{m_{0}}\big(\rho_{k,0}\big)+\mathcal{O}\big(\frac{1}{M^{2}}\big)}\end{array}$  , this gives  

$$
\begin{array}{r l r}&{}&{{\mathbb{E}}\left[\eta_{1,k,0}\xi(u)\right]=}\\ &{}&{\frac{\mathrm{i}u\sigma^{2}\sqrt{M}\sum_{i,j}{\mathbb{E}}\left[[{\bf u}_{k}^{*}{\bf Q}_{0}\left(\rho_{k,0}\right)]_{i}[{\bf W}_{\ell}^{*}{\bf u}_{k}]_{j}\chi\overline{{\partial}}_{i,j}^{(0)}\{\eta\}\xi(u)\right]}{N_{0}\left(\rho_{k,0}\left(1+\sigma^{2}c_{0}m_{0}\left(\rho_{k,0}\right)\right)-\sigma^{2}\right)}}\\ &{}&{+\,\frac{\Delta(u)}{\sqrt{M}}.\eqno(15}\end{array}
$$  

Developing further the derivatives and using Lemma 6, we have  

$$
\begin{array}{r l r}{\lefteqn{\sum_{i,j}\mathbb{E}\left[[\mathbf{u}_{k}^{*}\mathbf{Q}_{0}(\rho_{k,0})]_{i}[\mathbf{W}_{\ell}^{*}\mathbf{u}_{k}]_{j}\bar{\boldsymbol{\chi}}_{i,j}^{0(0)}\{\eta_{1,k^{\prime},\ell}\}\xi(u)\right]=}}\\ &{}&{-\sqrt{M}\mathbb{E}\Bigg[\mathbf{u}_{k}^{*}\mathbf{Q}_{0}(\rho_{k,0})\mathbf{Q}_{\ell}(\rho_{k^{\prime},\ell})\mathbf{u}_{k^{\prime}}\mathbf{u}_{k^{\prime}}^{*}\mathbf{Q}_{\ell}(\rho_{k^{\prime},\ell})}\\ &{}&{\times\frac{\mathbf{W}_{\ell}\mathbf{W}_{\ell}^{*}}{N_{\ell}}\mathbf{u}_{k}\boldsymbol{\chi}\xi(u)\Bigg]+\frac{\Delta(u)}{\sqrt{M}}}\\ &{}&{=\sqrt{M}\theta_{k,\ell}\delta_{k-k^{\prime}}\Psi(u)+\frac{\Delta(u)}{\sqrt{M}},}&{\quad{\mathrm{(for~}}k\neq1,2,3,\ldots\,.}\end{array}
$$  

$$
\begin{array}{r l}&{\kappa_{k,\ell}=}\\ &{\quad\quad\left\{\frac{\sigma^{2}m_{0}(\rho_{k,0})m_{0}^{\prime}(\rho_{k,0})}{1+\sigma^{2}c_{0}m_{0}(\rho_{k,0})}\right.\quad\mathrm{~if~}\ell=0,}\\ &{\quad\quad\left.\frac{\sigma^{2}m_{\ell}(\rho_{k,\ell})m_{0}(\rho_{k,0})\left(1+\sigma^{2}c_{0}m_{0}(\rho_{k,0})\right)}{\sigma^{2}-\rho_{k,\ell}\left(1+\sigma^{2}c_{0}m_{0}(\rho_{k,0})\right)\left(1+\sigma^{2}c_{\ell}m_{\ell}(\rho_{k,\ell})\right)}\right.\quad\mathrm{~if~}\ell\geq1}\end{array}
$$  

$$
\begin{array}{r l}&{=\left\{\begin{array}{l l}{-\frac{\sigma^{2}\gamma_{k}}{(\gamma_{k}+\sigma^{2}c_{0})^{2}(\gamma_{k}^{2}-\sigma^{2}c_{0})}}&{\mathrm{~if~}\ell=0}\\ {-\frac{\sigma^{2}\gamma_{k}}{(\gamma_{k}+\sigma^{2}c_{0})(\gamma_{k}+\sigma^{2}c_{\ell})(\gamma_{k}^{2}-\sigma^{2}c_{0})}}&{\mathrm{~if~}\ell\geq1}\end{array}\right.,}\end{array}
$$  

where the second equality in the expression of    $\theta_{\boldsymbol{k},\boldsymbol{\ell}}$  can be obtained with Lemma 3. Moreover,  

$$
\begin{array}{r l r}{\lefteqn{\sum_{i,j}\mathbb{E}\left[[\mathbf{u}_{k}^{*}\mathbf{Q}_{0}(\rho_{k,0})]_{i}[\mathbf{W}_{\ell}^{*}\mathbf{u}_{k}]_{j}\chi\overline{{\partial}}_{i,j}^{(0)}\{\eta_{2,k^{\prime},\ell}\}\xi(u)\right]}}\\ &{}&{=-\frac{\sqrt{M}}{N_{\ell}^{2}}\mathbb{E}\Bigg[\mathbf{u}_{k}^{*}\mathbf{Q}_{0}(\rho_{k,0})\mathbf{W}_{\ell}\tilde{\mathbf{Q}}_{\ell}(\rho_{k^{\prime},\ell})\mathbf{s}_{k^{\prime},\ell}}\\ &{}&{\qquad\qquad\times\mathbf{s}_{k^{\prime},\ell}^{*}\tilde{\mathbf{Q}}_{\ell}(\rho_{k^{\prime},\ell})\mathbf{W}_{\ell}^{*}\mathbf{u}_{k}\chi\xi(u)\Bigg]+\frac{\Delta(u)}{\sqrt{M}}}\\ &{}&{=\frac{\Delta(u)}{\sqrt{M}},\eqno{(15)}}\end{array}
$$  

$$
\begin{array}{r l r}{\lefteqn{\sum_{i,j}\mathbb{E}\left[[{\bf u}_{k}^{*}{\bf Q}_{\ell}(\rho_{k,0})]_{i}[{\bf W}_{\ell}^{*}{\bf u}_{k}]_{j}\bar{\lambda}_{i,j}^{(0)}\{\eta_{3,k^{\prime},\ell}\}\xi(u)\right]}}\\ &{}&{=-\frac{\sqrt{M}}{N_{\ell}}\mathbb{E}\Bigg[{\bf u}_{k}^{*}{\bf Q}_{0}(\rho_{k,0}){\bf Q}_{\ell}(\rho_{k^{\prime},\ell}){\bf W}_{\ell}{\bf s}_{k^{\prime},\ell}}\\ &{}&{\times\,{\bf u}_{k^{\prime}}^{*}{\bf Q}_{\ell}(\rho_{k^{\prime},\ell})\frac{{\bf W}_{\ell}{\bf W}_{\ell}^{*}}{N_{\ell}}{\bf u}_{k}\chi\xi(u)\Bigg]+\frac{\Delta(u)}{\sqrt{M}}}\\ &{}&{=\frac{\Delta(u)}{\sqrt{M}}.\eqno{(155)}}\end{array}
$$  

Finally, using again Lemma 3, we obtain  

$$
\begin{array}{r l}&{\mathbb{E}\left[\eta_{1,k,0}\xi(u)\right]}\\ &{=\cfrac{\mathrm{i}u\sigma^{2}c_{0}\sum_{\ell=0}^{L}\beta_{1,k,\ell}\kappa_{k,\ell}}{\rho_{k,0}(1+\sigma^{2}c_{0}m_{0}(\rho_{k,0}))-\sigma^{2}}\Psi(u)+\cfrac{\Delta(u)}{\sqrt{M}}}\\ &{=-\mathrm{i}u\bigg(\cfrac{\beta_{1,k,0}\sigma^{4}c_{0}}{(\gamma_{k}+\sigma^{2}c_{0})^{2}(\gamma_{k}^{2}-\sigma^{2}c_{0})}}\\ &{+\displaystyle\sum_{\ell=1}^{L}\cfrac{\beta_{1,k,\ell}\sigma^{4}c_{0}}{(\gamma_{k}+\sigma^{2}c_{0})(\gamma_{k}+\sigma^{2}c_{\ell})(\gamma_{k}^{2}-\sigma^{2}c_{0})}\bigg)\Psi(u)+\cfrac{\Delta(u)}{\sqrt{M}}.}\end{array}
$$  

Using similar computations for the remaining terms  $\left(\mathbb{E}\left[\eta_{i,k,\ell}\xi(u)\right]\right)_{i=2\ 3}$  in    $\Psi^{\prime}(u)$  , we finally obtain the result of  $i{=}2,3$  Proposition 3.  

# R EFERENCES  

[1] R. Beisson, P. Vallet, A. Giremus, and G. Ginolhac, “Change Detection in The Covariance Structure of High-Dimensional Gaussian Low-Rank Models,” in  Statistical Signal Processing Workshop (SSP) . IEEE, 2021, pp. 421–425.  

[2] K. Conradsen, A. Nielsen, J. Schou, and H. Skriver, “A test statistic in the complex Wishart distribution and its application to change detection in polarimetric SAR data,”  IEEE Trans. Geosci. Remote Sens. , vol. 41, no. 1, pp. 4–19, 2003.

 [3] D. Ciuonzo, V. Carotenuto, and A. De Maio, “On multiple covariance equality testing with application to SAR change detection,”  IEEE Trans. on Signal Process. , vol. 65, no. 19, pp. 5078–5091, 2017.

 [4] A. Mian, G. Ginolhac, J.-P. Ovarlez, and A. Atto, “New robust statistics for change detection in time series of multivariate SAR images,”  IEEE Trans. Signal Process. , vol. 67, no. 2, pp. 520–534, 2018.

 [5] A. Mian, A. Collas, A. Breloy, G. Ginolhac, and J.-P. Ovarlez, “Robust low-rank change detection for multivariate sar image time series,”  IEEE J. Sel. Top. Appl. Earth Obs. Remote Sens. , vol. 13, pp. 3545–3556, 2020.

 [6] R. Liu, L. Liu, D. He, W. Zhang, and E. G. Larsson, “Detection of abrupt change in channel covariance matrix for multi-antenna communication,” in  Global Communications Conference (GLOBECOM) . IEEE, 2021.

 [7] P. Galeano and D. Pe˜ na, “Covariance changes detection in multivariate time series,”  J. Stat. Plan. Inference , vol. 137, no. 1, pp. 194–211, 2007.

 [8] A. Ribes, J.-M. Azais, and S. Planton, “Adaptation of the optimal fingerprint method for climate change detection using a well-conditioned covariance matrix estimate,”  Clim. Dyn. , vol. 33, no. 5, pp. 707–722, 2009.

 [9] Y.-H. Zhou, “Set-based differential covariance testing for genomics,” Stat , vol. 8, no. 1, p. e235, 2019.

 [10] A. Gupta and J. Tang, “Distribution of likelihood ratio statistic for testing equality of covariance matrices of multivariate gaussian models,” Biometrika , vol. 71, no. 3, pp. 555–559, 1984.

 [11] R. Muirhead,  Aspects of multivariate statistical theory . Wiley Online Library, 1982.

 [12] S. Zheng, “Central limit theorems for linear spectral statistics of large dimensional F-matrices,”  Ann. Inst. H. Poincar´ e Probab. Statist. , vol. 48, no. 2, pp. 444–476, 2012.

 [13] I. Johnstone, “On the distribution of the largest eigenvalue in principal components analysis,”  Ann. Statist. , vol. 29, no. 2, pp. 295–327, 04 2001.

 [14] A. Combernoux, F. Pascal, and G. Ginolhac, “Performance of the low- rank adaptive normalized matched filter test under a large dimension regime,”  IEEE Trans. Aerosp. Electron. Syst. , vol. 55, no. 1, pp. 459– 468, 2018.

 [15] P. Vallet, X. Mestre, and P. Loubaton, “Performance analysis of an improved music doa estimator,”  IEEE Trans. Signal Process , vol. 63, no. 23, p. 6407–6422, 2015.

 [16] K. Wachter, “The limiting empirical measure of multiple discriminant ratios,”  Ann. Statist. , pp. 937–957, 1980.

 [17] Q. Wang and J. Yao, “Extreme eigenvalues of large-dimensional spiked fisher matrices with application,”  Ann. Statist. , vol. 45, no. 1, pp. 415– 460, 2017.

 [18] R. Abdallah, A. Mian, A. Breloy, A. Taylor, M. El Korso, and D. Lautru, “Detection methods based on structured covariance matrices for mul- tivariate SAR images processing,”  IEEE Geosci. Remote. Sens. Lett. , vol. 16, no. 7, pp. 1160–1164, 2019.

 [19] R. Abdallah, A. Breloy, A. Taylor, M. El Korso, and D. Lautru, “Signal subspace change detection in structured covariance matrices,” in  27th European Signal Processing Conference (EUSIPCO) . IEEE, 2019.

 [20] F. Benaych-Georges, A. Guionnet, and M. Maida, “Fluctuations of the Extreme Eigenvalues of Finite Rank Deformations of Random Matrices,” Electron. J. Probab. , vol. 16, pp. no. 60,1621–1662, 2011.

 [21] F. Benaych-Georges and R. Nadakuditi, “The eigenvalues and eigenvec- tors of finite, low rank perturbations of large random matrices,”  Adv. Math. , vol. 227, no. 1, pp. 494–521, 2011.

 [22] T. Anderson,  An introduction to multivariate statistical analysis . John Wiley & Sons, 1958.

 [23] I. Johnstone, “High dimensional statistical inference and random matri- ces,” in  International Congress of Mathematicians , Madrid, 2006.

 [24] X. Mestre and P. Vallet, “Correlation Tests and Linear Spectral Statistics of the Sample Correlation Matrix,”  IEEE Trans. Inf. Theory , vol. 63, no. 7, pp. 4585–4618, 2017.

 [25] R. Couillet, “Robust spiked random matrices and a robust G-MUSIC estimator,”  J. Multivariate Anal. , vol. 140, pp. 139–161, 2015, publisher: Elsevier.

 [26] J. B. G. A. S. P´ ech´ e, “Phase transition of the largest eigenvalue for nonnull complex sample covariance matrices,”  Ann. Probab. 33 (5) 1643 - 1697 , 2005.

 [27] P. Vallet, P. Loubaton, and X. Mestre, “On the consistency of likelihood penalization methods in large sensor networks,” in  7th Sensor Array and Multichannel Signal Processing Workshop (SAM) . IEEE, 2012, pp. 109–112.  

[28] P. Stoica and R. Moses,  Spectral analysis of signals . Pearson Prentice Hall, 2005, vol. 452.

 [29] A. Mian, J.-P. Ovarlez, A. Atto, and G. Ginolhac, “Design of new wavelet packets adapted to high-resolution sar images with an appli- cation to target detection,”  IEEE Trans. Geosci. Remote Sens. , vol. 57, no. 6, pp. 3919–3932, 2019.

 [30] X. Mestre, “On the asymptotic behavior of the sample estimates of eigenvalues and eigenvectors of covariance matrices,”  IEEE Trans. Signal Process. , vol. 56, no. 11, pp. 5353–5368, 2008.

 [31] S. Geman, “A limit theorem for the norm of random matrices,”  Ann. Prob. , pp. 252–261, 1980.

 [32] R. Horn and C. Johnson,  Matrix analysis . Cambridge university press, 2012.

 [33] W. Hachem, P. Loubaton, X. Mestre, J. Najim, and P. Vallet, “Large information plus noise random matrix models and consistent subspace estimation in large sensor networks,”  Random Matrices: Theory Appl. , vol. 1, no. 2, 2012.

 [34] F. Benaych-Georges and R. Nadakuditi, “The singular values and vectors of low rank perturbations of large rectangular random matrices,”  J. Multivariate Anal. , vol. 111, no. 0, pp. 120–135, 2012.

 [35] W. Hachem, O. Khorunzhiy, P. Loubaton, J. Najim, and L. Pastur, “A new approach for capacity analysis of large dimensional multi-antenna channels,”  IEEE Trans. Inf. Theory , vol. 54, no. 9, pp. 3987–4004, 2008.  