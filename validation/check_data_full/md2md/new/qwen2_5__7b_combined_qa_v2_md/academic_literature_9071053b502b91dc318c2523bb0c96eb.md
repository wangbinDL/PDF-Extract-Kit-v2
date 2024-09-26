# High-dimensional copula-based Wasserstein dependence. 

Steven De Keyser ${ }^{\mathrm{a}}$, Irène Gijbels ${ }^{\mathrm{a}, *}$<br>${ }^{a}$ Department of Mathematics, KU Leuven, Celestijnenlaan 200B, B-3001 Leuven (Heverlee), Belgium


#### Abstract

We generalize 2-Wasserstein dependence coefficients to measure dependence between a finite number of random vectors. This generalization includes theoretical properties, and in particular focuses on an interpretation of maximal dependence and an asymptotic normality result for a proposed semi-parametric estimator under a Gaussian copula assumption. In addition, we discuss general axioms for dependence measures between multiple random vectors, other plausible normalizations, and various examples. Afterwards, we look into plug-in estimators based on penalized empirical covariance matrices in order to deal with high dimensionality issues and take possible marginal independencies into account by inducing (block) sparsity. The latter ideas are investigated via a simulation study, considering other dependence coefficients as well. We illustrate the use of the developed methods in two real data applications.


Keywords: Copula, Normal scores rank correlation, Regularization, Sparsity, Wasserstein dependence
2020 MSC: Primary 62Axx, 62Hxx; Secondary 62Exx, 62Gxx.

## 1. Introduction

A prominent line of research in statistics considers measuring dependence between groups of variables. In case of two groups, greatly celebrated is the canonical correlation analysis of [27] relying on the Pearson correlation coefficient. To step away from the assumption of Gaussianity, concordance measures as studied in, e.g., [22, 37, 42] among many others, are also used for quantifying general monotonic associations between two random vectors in [23]. In [26], measures of association computed from collapsed random variables are used to measure the dependence between random vectors. Fundamental is copula theory (e.g., [38, 43]), allowing to split multivariate distributions into marginal distributions on the one hand, and a dependence structure described by the copula on the other hand. Especially when the marginals are continuous, the preference often goes to copula-based dependence measures since then, by Sklar's theorem [43], the copula is unique, and hence margin-free dependence can unequivocally be quantified.

Statistical independence between random vectors holds if and only if the true underlying copula is the product of the marginal copulas (where a one dimensional copula is basically a uniform distribution on $[0,1]$ ), yielding zero dependence. However, the dependence measures mentioned above do not detect all types of departure from independence, meaning that they might vanish while the independence product copula is misspecified. Since the work of [44], there has been a growing interest for dependence measures that completely characterize independence. Some recent developments are, e.g., the Hoeffding's Phi-Square measure of [35], the $\Phi$-dependence measures of [11] (of which the Hellinger correlation [20] and essential dependence [51] are particular cases), the coefficient of Chatterjee $[1,2,8,18]$, and the 2 -Wasserstein coefficients of [36].

The aim of this article is to elaborate further on the optimal transport measures of [36]. First, the focus will be on extending their dependence coefficients from two to finitely many random vectors. We do this from a copula point of view. This includes generalizing the results of [36], and also verifying the axioms stated in [11] (see also Appendix A). Some additional examples, focusing on, e.g., the impact of the normalization, are provided as well. Afterwards, we dive into the Bures-Wasserstein dependence making a Gaussian copula assumption. This yields dependence measures

[^0]
[^0]:    *Corresponding author. Email address: irene.gijbels@kuleuven.be



that are attractive, and more amenable for estimation. The results are a far from straightforward extension of results of [36] to the case of a finite number of random vectors, and require significant mathematical care.

The proposed semi-parametric estimation approach of the Bures-Wasserstein coefficients relies on the sample matrix of normal scores rank correlations (see, e.g., [24]). Since we extend the theory to a general finite amount of groups of variables, high dimensional cases with a large number of variables compared to the sample size are of study interest as well. Acclaimed penalization techniques are known to significantly improve (inverse) covariance matrix estimation (see, e.g., [29] and references therein). We utilize these ideas in our Gaussian copula context in order to correct for high dimensionality bias and possibly enforce sparsity at the individual level or group level to take plausible marginal independencies into account.

The outline of this paper is the following. Section 2 explains how optimal transport theory is combined with copula theory in order to arrive at a dependence measure between multiple groups of random variables that completely characterizes independence and is invariant with respect to the univariate marginal distributions. The verification of the properties postulated in [11] for such dependence measures is also part of this section. The Gaussian copula approach is discussed in Section 3, with special attention to the meaning of maximal dependence, and asymptotic normality of the proposed semi-parametric estimator. Afterwards, different regularization techniques for Gaussian copula covariance matrices are discussed in Section 4. Next to an empirical illustration of the asymptotic normality result, simulations are performed in Section 5 to investigate the performance of these regularization techniques on various dependence coefficients for random vectors. Two real data applications are discussed in Section 6. All proofs are deferred to the Appendix. Any experiments reported can be reproduced via the source code available at https://github.com/StevenDeKeyser98/VecDep. Additional figures are included in the Supplementary Material.

# 2. General 2-Wasserstein dependence 

We consider a q-dimensional random vector $X=\left(X^{1}, \ldots, X^{k}\right)$ defined on $\left(\mathbb{R}^{q}, \mathcal{B}\left(\mathbb{R}^{q}\right), \lambda_{q}\right)$ consisting of $k$ marginal random vectors $X^{i}=\left(X_{i 1}, \ldots, X_{i d_{i}}\right)$ for $i=1, \ldots, k$ having $d_{i}$ continuous univariate marginal random variables $X_{i j}$ for $j=1, \ldots, d_{i}$. The numbers $d_{1}, \ldots, d_{k} \in \mathbb{Z}_{>0}$ are such that $q=d_{1}+\cdots+d_{k}$, and $\lambda_{q}$ denotes the $q$-dimensional Lebesgue measure defined on $\mathcal{B}\left(\mathbb{R}^{q}\right)$, the Borel sigma-algebra on $\mathbb{R}^{q}$. Let $P: \mathcal{B}\left(\mathbb{R}^{q}\right) \rightarrow \mathbb{R}$ be a probability measure. Our aim is to measure the dependence between $X^{1}, \ldots, X^{k}$. For $I=[0,1]$ and $\mathcal{P}\left(I^{q}\right)$ the set of Borel probability measures on $I^{q}$, the random vector $X$ is assigned a copula probability law $\mu_{C} \in \mathcal{P}\left(I^{q}\right)$ having corresponding marginal copula laws $\mu_{C_{i}} \in \mathcal{P}\left(I^{d_{i}}\right)$ of $X^{i}$ for $i=1, \ldots, k$. Note that in case $d_{i}=1$, the law $\mu_{C_{i}}$ is that of a uniform distribution on $I$. We denote $\Gamma\left(\mu_{C_{1}}, \ldots, \mu_{C_{k}}\right)$ for the set of measures $\gamma \in \mathcal{P}\left(I^{q}\right)$ such that

$$
\mu_{C_{i}}\left(B_{i}\right)=\gamma\left(I^{d_{1}} \times \cdots \times I^{d_{i-1}} \times B_{i} \times I^{d_{i+1}} \times \cdots \times I^{d_{k}}\right)
$$

for all $B_{i} \in \mathcal{B}\left(I^{d_{i}}\right)$ and $i=1, \ldots, k$. This is a natural generalization of the set of coupling measures. Obviously, $\mu_{C} \in$ $\Gamma\left(\mu_{C_{1}}, \ldots, \mu_{C_{k}}\right)$. Quantifying the intensity of relation between $X^{1}, \ldots, X^{k}$ can be done by measuring the difference between $\mu_{C}$ and the product measure $\mu_{C_{1}} \times \cdots \times \mu_{C_{k}}$. We use the 2 -Wasserstein distance, whose square is, for certain measures $\pi, \widetilde{\pi} \in \mathcal{P}\left(I^{q}\right)$ given by

$$
W_{2}^{2}(\pi, \widetilde{\pi})=\inf _{\gamma \in \Gamma(\pi, \widetilde{\pi})} \int_{I^{2 q}}\|u-v\|^{2} \mathrm{~d} \gamma(u, v)=\inf _{\substack{U \sim \pi \\ V \sim \tilde{\pi}}} \mathbb{E}\left(\|U-V\|^{2}\right)
$$

The interpretation of the metric (1) is optimal transport, see, e.g., [39]. It is the minimal effort (cost) required to transform the mass of $\pi$ into the mass of $\widetilde{\pi}$, i.e., for every $(u, v)$ transport an infinitesimal amount of mass $\mathrm{d} \gamma(u, v)$ from $u$ to $v$ at a distance cost of $\|u-v\|^{2}$. Aggregating the mass $\gamma\left(\{u\} \times I^{q}\right)$ that leaves $u$ gives $\pi(u)$ and the total mass $\gamma\left(I^{q} \times\{v\}\right)$ that reaches $v$ equals $\widetilde{\pi}(v)$. For certain non-degenerate (i.e. not Dirac delta distributions) reference laws $\nu_{i} \in \mathcal{P}\left(I^{d_{i}}\right)$ for $i=1, \ldots, k$, we now define

$$
\begin{aligned}
T_{d_{1}, \ldots, d_{k}}\left(\mu_{C} ; \nu_{1}, \ldots, \nu_{k}\right) & =W_{2}^{2}\left(\mu_{C}, \nu_{1} \times \cdots \times \nu_{k}\right)-W_{2}^{2}\left(\mu_{C_{1}} \times \cdots \times \mu_{C_{k}}, \nu_{1} \times \cdots \times \nu_{k}\right) \\
& =W_{2}^{2}\left(\mu_{C}, \nu_{1} \times \cdots \times \nu_{k}\right)-\sum_{i=1}^{k} W_{2}^{2}\left(\mu_{C_{i}}, \nu_{i}\right)
\end{aligned}
$$



where the second identity is known to be true (see, e.g., [39]). We call a subset $\mathcal{A} \subset \mathcal{P}\left(I_{q}\right) \mathrm{W}_{2}$-compact if every sequence in the metric space $\left(\mathcal{A}, \mathrm{W}_{2}\right)$ has a convergent subsequence with limit in $\mathcal{A}$. Lemma 1 gives the main properties of $T_{d_{1}, \ldots, d_{k}}$. Proofs of Lemma 1 , and all other theoretical results of Section 2 , can be found in Appendix B.
Lemma 1. It holds that
(a) $T_{d_{1}, \ldots, d_{k}}\left(\mu^{C} ; \nu_{1}, \ldots, \nu_{k}\right) \geq 0$
(b) $T_{d_{1}, \ldots, d_{k}}\left(\mu^{C_{1}} \times \cdots \times \mu^{C_{k}} ; \nu_{1}, \ldots, \nu_{k}\right)=0$
(c) If either $\mu^{C_{i}}=\nu_{i}$ for all $i=1, \ldots, k$ or $\nu_{i}$ is absolutely continuous (with respect to $\lambda_{d_{i}}$ ) for all $i=1, \ldots, k$, then $T_{d_{1}, \ldots, d_{k}}\left(\mu^{C} ; \nu_{1}, \ldots, \nu_{k}\right)=0$ implies $\mu^{C}=\mu^{C_{1}} \times \cdots \times \mu^{C_{k}}$
(d) The set $\Gamma\left(\mu^{C_{1}}, \ldots, \mu^{C_{k}}\right)$ is $\mathrm{W}_{2}$-compact in $\mathcal{P}\left(I_{q}\right)$ and the mapping $T_{d_{1}, \ldots, d_{k}}\left(\cdot ; \nu_{1}, \ldots, \nu_{k}\right):\left(\Gamma\left(\mu^{C_{1}}, \ldots, \mu^{C_{k}}\right), \mathrm{W}_{2}\right) \rightarrow$ $(\mathbb{R},|\cdot|)$ is continuous.

Its interpretation, together with its mathematical properties, make $T_{d_{1}, \ldots, d_{k}}\left(\mu^{C} ; \nu_{1}, \ldots, \nu_{k}\right)$ an appealing measure of dependence between $k$ random vectors $X_{1}, \ldots, X_{k}$. In what follows, we assume that $\nu_{i}$ is absolutely continuous for $i=1, \ldots, k$, and let $\mathcal{G}^{C} \subset \Gamma\left(\mu^{C_{1}}, \ldots, \mu^{C_{k}}\right)$ be a compact set such that $\mu^{C} \in \mathcal{G}^{C}$. General axioms for dependence measures between multiple random vectors are formulated in [11], see also Appendix A. Lemma 1 offers aid in proving them here, see Proposition 1.
Proposition 1. Consider Axioms (A1)-(A8) given in Appendix A, and a normalized version of $T_{d_{1}, \ldots, d_{k}}\left(\mu^{C} ; \nu_{1}, \ldots, \nu_{k}\right)$ given by

$$
D\left(\mu^{C} ; \nu_{1}, \ldots, \nu_{k}\right)=\frac{T_{d_{1}, \ldots, d_{k}}\left(\mu^{C} ; \nu_{1}, \ldots, \nu_{k}\right)}{\sup _{\pi \in \mathcal{G}^{C}} T_{d_{1}, \ldots, d_{k}}\left(\pi ; \nu_{1}, \ldots, \nu_{k}\right)}
$$

Then, $D$ satisfies (A1)-(A3) and (A5)-(A7). Axioms (A4) and (A8) are satisfied by the non-normalized version $T_{d_{1}}, \ldots, d_{k}$.
The supremum in (2) is attained when $\mathcal{G}^{C}$ is $\mathrm{W}_{2}$-compact (e.g., $\mathcal{G}^{C}=\Gamma\left(\mu^{C_{1}}, \ldots, \mu^{C_{k}}\right)$ ) because of (d) in Lemma 1 . It represents the case of maximal dependence, which characterization (and hence the overall behaviour of (2)), largely depends on $\mathcal{G}^{C}$. There is still freedom in choosing the normalization by picking the set $\mathcal{G}^{C}$. It might impose additional constraints (in addition to having marginals $\mu^{C_{i}}$ ) on the $\pi \in \Gamma\left(\mu^{C_{1}}, \ldots, \mu^{C_{k}}\right)$ that characterizes maximal dependence (for example $\pi$ should be in the same copula family as $\mu^{C}$ ). Strictly speaking, we can have a different $\mathcal{G}^{C}$ for every copula $C$, even if the marginals are the same.

Regarding axioms (A4) and (A8), we make the following remark.
Remark 1. While (2) does not satisfy axiom (A4) in general (that is for every possible choice of $\mathcal{G}^{C}$ ), there might still be some specific choices for $\mathcal{G}^{C}$ such that (A4) is satisfied. We illustrate this further in Example 1.

Also, when considering $C_{n} \rightarrow C$ uniformly as $n \rightarrow \infty$, axiom (A8) can be satisfied by (2) under some extra constraints. The numerator converges if $\mathcal{G}^{C}$ is chosen such that $C \mapsto \sup _{\pi \in \mathcal{G}^{C}} T_{d_{1}, \ldots, d_{k}}\left(\pi ; \nu_{1}, \ldots, \nu_{k}\right)$ is continuous (considering the uniform metric on the space of copulas). In Section 3, we see that this holds in the class of Gaussian copulas when taking $\mathcal{G}^{C}=\Gamma\left(\mu^{C_{1}}, \ldots, \mu^{C_{k}}\right)$.

We now arrive at a natural generalization of the Wasserstein dependence coefficients of [36], which come from (2) with two particular choices of reference measures.

Definition 1. For $m \in \mathbb{Z}_{>0}$, let $\gamma_{m}$ denote the measure of an $m$-variate Gaussian copula with identity correlation matrix (i.e., the $m$-variate independence copula). For $q=d_{1}+\cdots+d_{k}$ with $d_{1}, \ldots, d_{k} \in \mathbb{Z}_{>0}$ and for $\mu^{C} \in \mathcal{G}^{C} \subset \Gamma\left(\mu^{C_{1}}, \ldots, \mu^{C_{k}}\right)$, where $\mathcal{G}^{C}$ is $\mathrm{W}_{2}$-compact and non-degenerate $\mu^{C_{i}} \in \mathcal{P}\left(I_{d_{i}}\right)$ for $i=1, \ldots, k$, define

$$
\begin{aligned}
& D_{1}^{d_{1}, \ldots, d_{k}}\left(\mu^{C}\right)=D\left(\mu^{C} ; \gamma_{d_{1}}, \ldots, \gamma_{d_{k}}\right)=\frac{\mathrm{W}_{2}^{2}\left(\mu^{C}, \gamma_{q}\right)-\sum_{i=1}^{k} \mathrm{~W}_{2}^{2}\left(\mu^{C_{i}}, \gamma_{d_{i}}\right)}{\sup _{\pi \in \mathcal{G}^{C}} \mathrm{~W}_{2}^{2}\left(\pi, \gamma_{q}\right)-\sum_{i=1}^{k} \mathrm{~W}_{2}^{2}\left(\mu^{C_{i}}, \gamma_{d_{i}}\right)} \\
& D_{2}^{d_{1}, \ldots, d_{k}}\left(\mu^{C}\right)=D\left(\mu^{C} ; \mu^{C_{1}}, \ldots, \mu^{C_{k}}\right)=\frac{\mathrm{W}_{2}^{2}\left(\mu^{C}, \mu^{C_{1}} \times \cdots \times \mu^{C_{k}}\right)}{\sup _{\pi \in \mathcal

If the context is clear, we just write $D_{r}(\mu^{C})$ for $r \in\{1,2\}$, or also $D_{r}\left(X_{1} ; \cdots ; X_{k}\right)$ to emphasize that we are measuring the dependence between $k$ random vectors (having joint copula $C$ ).

Let us consider an example illustrating that $D$ does not necessarily satisfy Axiom (A4) in general.
Example 1. Consider a random vector $\left(X_{1}, X_{2}, X_{3}\right)$ having a trivariate Gaussian copula $\mu^{C}$ with correlation matrix

$$
R=\left(\begin{array}{lll}
1 & \rho & 0 \\
\rho & 1 & 0 \\
0 & 0 & 1
\end{array}\right), \quad \text { where }-1 \leq \rho \leq 1
$$

Let $\mu^{C_{i}}$ be the marginal copula measure of $X_{i}$ for $i=1,2,3$, which in this case is in fact the Lebesgue measure corresponding to a $U[0,1]$ distribution. The product measure $\mu^{C_{1}} \times \mu^{C_{2}} \times \mu^{C_{3}}$ is the three dimensional independence copula, being equal to the trivariate Gaussian copula with identity correlation matrix $I_{3}$. Also note that $X_{3}$ is independent of $\left(X_{1}, X_{2}\right)$. One can quickly check that (using (3), see further)

$$
D_{2}\left(X_{1} ; X_{2} ; X_{3}\right)=\frac{W_{2}^{2}\left(\mu^{C} ; \mu^{C_{1}} \times \mu^{C_{2}} \times \mu^{C_{3}}\right)}{\sup _{\pi \in \mathcal{G}^{C}} W_{2}^{2}\left(\pi, \mu^{C_{1}} \times \mu^{C_{2}} \times \mu^{C_{3}}\right)}=\frac{4-2 \sqrt{1-\rho}-2 \sqrt{1+\rho}}{\sup _{\pi \in \mathcal{G}^{C}} W_{2}^{2}\left(\pi, \mu^{C_{1}} \times \mu^{C_{2}} \times \mu^{C_{3}}\right)}
$$

The remaining question is what to pick for $\mathcal{G}^{C}$, i.e., which quantity do we put in the denominator and defines the maximal amount of dependence. Well, if $\mathcal{G}^{C}=\Gamma\left(\mu^{C_{1}}, \mu^{C_{2}}, \mu^{C_{3}}\right.$ ), we should find the squared 2 -Wasserstein distance between the independence copula and any other trivariate distribution having $\mu^{C_{1}}, \mu^{C_{2}}$ and $\mu^{C_{3}}$ as marginals, that is every possible trivariate copula. This is, as far as we are concerned, an open problem. However, in this context, it is reasonable to restrict $\mathcal{G}^{C}$ to the Gaussian copula family. Doing so, one has

$$
\sup _{\pi \in \mathcal{G}^{C}} W_{2}^{2}\left(\pi, \mu^{C_{1}} \times \mu^{C_{2}} \times \mu^{C_{3}}\right)=W_{2}^{2}\left(\mu^{C^{c o}}, \mu^{C_{1}} \times \mu^{C_{2}} \times \mu^{C_{3}}\right)=6-2 \sqrt{3}
$$

where $\mu^{C^{c o}}$ stands for the comonotonicity copula measure, i.e., the limit of an equicorrelated $\left(R=(1-\rho) I_{3}+\rho \mathbf{1}_{3} \mathbf{1}_{3}^{T}\right.$, where $\mathbf{1}_{3}^{T}=(1,1,1)$ and $\rho \in(-1 / 2,1))$ Gaussian copula with correlation $\rho$ tending to 1 . With this choice of $\mathcal{G}^{C}$, $\left(X_{1}, X_{2}, X_{3}\right)$ can never reach the maximum dependence, since

$$
4-2 \sqrt{1-\rho}-2 \sqrt{1+\rho} \leq 4-2 \sqrt{2}<6-2 \sqrt{3}
$$

Another way to put it, is that

$$
D_{2}\left(X_{1} ; X_{2} ; X_{3}\right)=\frac{2-\sqrt{1-\rho}-\sqrt{1+\rho}}{3-\sqrt{3}}<\frac{2-\sqrt{1-\rho}-\sqrt{1+\rho}}{2-\sqrt{2}}=D_{2}\left(X_{1} ; X_{2}\right)
$$

where $D_{2}\left(X_{1} ; X_{2}\right)$ is computed in a similar way, also restricting the couplings $\Gamma\left(\mu^{C_{1}}, \mu^{C_{2}}\right)$ to Gaussian ones. We thus see that, when adding an independent component $X_{3}$ into consideration, the dependence has decreased and hence axiom (A4) is definitely not fulfilled. Taking a look at $R$, it is maybe more tempting to have maximal dependence when $|\rho|=1$ and restrict $\mathcal{G}^{C}$ further to only those $\pi \in \Gamma\left(\mu^{C_{1}}, \mu^{C_{2}}, \mu^{C_{3}}\right)$ that are Gaussian and furthermore satisfy $\pi\left(B_{1} \times B_{2} \times B_{3}\right)=\pi\left(B_{1} \times B_{2} \times I\right) \cdot \pi\left(I \times I \times B_{3}\right)$ for all $B_{1}, B_{2}, B_{3} \in \mathcal{B}(I)$. Then, it is quickly seen that

$$
\sup _{\pi \in \mathcal{G}^{C}} W_{2}^{2}\left(\pi, \mu^{C_{1}} \times \mu^{C_{2}} \times \mu^{C_{3}}\right)=2-\sqrt{2}
$$

and hence $D_{2}\left(X_{1} ; X_{2} ; X_{3}\right)=D_{2}\left(X_{1} ; X_{2}\right)$, in harmony with axiom (A4). So, for actual computation, it is better to restrict $\mathcal{G}^{C}$ to the Gaussian copula family, and if some additional information is given (like zeroes in the correlation matrix), incorporating this in $\mathcal{G}^{C}$ can lead to a more interpretative dependence quantification.

Except for some families like normal distributions, computing the Wasserstein distance is very involved and tools and theory for statistical inference are still scarce. The authors of [36] give an overview of the literature so far, concluding that additional theory is still needed, and propose a quasi-Gaussian (based on covariance matrices) approach instead. We assume that the copula of $X$ is Gaussian.



# 3. A Gaussian copula approach 

In this section, we assume a Gaussian copula model for $\mathbf{X}$, elaborate more on maximal dependence, and discuss statistical inference within this framework.

### 3.1. The Bures-Wasserstein distance

The main incentive is the well-known formula for the squared 2-Wasserstein distance between Gaussian distributions, say with covariance matrices $R$ and $S$, becoming the so-called squared Bures-Wasserstein distance (see, e.g., [45]) between $R$ and $S$ :

$$
d_{W}^{2}(R, S)=\operatorname{tr}(R)+\operatorname{tr}(S)-2 \operatorname{tr}\left\{\left(R^{1 / 2} S R^{1 / 2}\right)^{1 / 2}\right\}
$$

were $\operatorname{tr}$ stands for the trace of a matrix. We denote by $\mathcal{S}_{q}=\left\{R \in \mathbb{R}^{q \times q}: R^{T}=R\right\}$ the set of symmetric $q \times q$ matrices, $\mathcal{S}_{q}^{\geq} \subset \mathcal{S}_{q}$ the set of positive semi-definite ones and $\mathcal{S}_{q}^{>}\left(\subset \mathcal{S}_{q}^{\geq}\right)$the set of positive definite ones. Let again $q=d_{1}+\cdots+d_{k}$ and consider $R_{i i} \in \mathcal{S}_{d_{i}}^{\geq}$for $i=1, \ldots, k$. We also define the set

$$
\Gamma\left(R_{11}, \ldots, R_{k k}\right)=\left\{A \in \mathcal{S}_{q}^{\geq}: A=\left(\begin{array}{ccccc}
R_{11} & \Psi_{12} & \cdots & \Psi_{1 k} \\
\Psi_{12}^{T} & R_{22} & \cdots & \Psi_{2 k} \\
\vdots & \vdots & \ddots & \vdots \\
\Psi_{1 k}^{T} & \Psi_{2 k}^{T} & \cdots & R_{k k}
\end{array}\right) \text { for some } \Psi_{i j} \in \mathbb{R}^{d_{i} \times d_{j}}\right\}
$$

as the set of all covariance matrices of random vectors $\mathbf{Z}=\left(\mathbf{Z}_{1}, \ldots, \mathbf{Z}_{k}\right)$ such that the covariance matrix of $\mathbf{Z}_{i}$, being $R_{i i}$, remains fixed for all $i=1, \ldots, k$ and

$$
R_{0}=\left(\begin{array}{llll}
R_{11} & 0_{12} & \ldots & 0_{1 k} \\
0_{12}^{T} & R_{22} & \ldots & 0_{2 k} \\
\vdots & \vdots & \ddots & \vdots \\
0_{1 k}^{T} & 0_{2 k}^{T} & \ldots & R_{k k}
\end{array}\right)
$$

with $0_{i j} \in \mathbb{R}^{d_{i} \times d_{j}}$ a matrix of zeroes, as the covariance matrix when the $\mathbf{Z}_{i}$ are all independent.
Consider now a random vector $\mathbf{X}=\left(\mathbf{X}_{1}, \ldots, \mathbf{X}_{k}\right)$ having a Gaussian copula with covariance matrix

$$
R=\left(\begin{array}{cccc}
R_{11} & R_{12} & \ldots & R_{1 k} \\
R_{12}^{T} & R_{22} & \ldots & R_{2 k} \\
\vdots & \vdots & \ddots & \vdots \\
R_{1 k}^{T} & R_{2 k}^{T} & \ldots & R_{k k}
\end{array}\right)
$$

This means that (5) is the usual covariance matrix of the random vector $\mathbf{Z}=\left(\mathbf{Z}_{1}, \ldots, \mathbf{Z}_{k}\right)$, with $\mathbf{Z}_{i}=\left(Z_{i 1}, \ldots, Z_{i d_{i}}\right)$ and $Z_{i j}=\left(\Phi^{-1} \circ F_{i j}\right)\left(X_{i j}\right)$ for $i=1, \ldots, k$ and $j=1, \ldots, d_{i}$, where $F_{i j}$ is the marginal distribution of $X_{i j}$ and $\Phi^{-1}$ the univariate standard normal quantile function. Measuring the dependence between $\mathbf{X}_{1}, \ldots, \mathbf{X}_{k}$ can be done by utilizing the 2-Wasserstein dependence coefficients of Definition 1, now taking $d_{W}$ for $W_{2}$.
Definition 2. For $q=d_{1}+\cdots+d_{k}$ with $d_{1}, \ldots, d_{k} \in \mathbb{Z}_{>0}, R \in \Gamma\left(R_{11}, \ldots, R_{k k}\right)$ with $R_{i i} \in \mathcal{S}_{d_{i}}^{\geq} \backslash\{0\}$ for $i=1, \ldots, k$ and a $d_{W}$-compact set $\mathcal{G}_{R} \subset \Gamma\left(R_{11}, \ldots, R_{k k}\right)$ with $R \in \mathcal{G}_{R}$, define

$$
\begin{aligned}
\mathbf{D}_{1}\left(R ; d_{1}, \ldots, d_{k}\right) & =\frac{d_{W}^{2}\left(R, I_{q}\right)-\sum_{i=1}^{k} d_{W}^{2}\left(R_{i i}, I_{d_{i}}\right)}{\sup _{A \in \mathcal{G}_{R}} d_{W}^{2}\left(A, I_{q}\right)-\sum_{i=1}^{k} d_{W}^{2}\left(R_{i i}, I_{d_{i}}\right)} \\
\mathbf{D}_{2}\left(R ; d_{1}, \ldots, d_{k}\right) & =\frac{d_{W}^{2}\left(R, R_{0}\right)}{\sup _{A \in \mathcal{G}_{R}} d_{W}^{2}\left(A, R_{0}\right)}
\end{aligned}
$$

where $R_{0}$ is the matrix given in (4). If the context is clear, we also write $\mathbf{D}_{r}(R)$ or $\mathbf{D}_{r}\left(\mathbf{X}_{1} ; \cdots ; \mathbf{X}_{k}\right)$ for $r \in\{1,2\}$.



If the true copula is indeed Gaussian, the adequacy of the Bures-Wasserstein dependence remains, and we obtain something way more easy to handle. In order to make them fully practically usable, that is to say suitably attractive for estimation, we ought to find explicit expressions for the suprema in the denominator of the dependence measures. When $\boldsymbol{G}_{R}=\Gamma\left(\boldsymbol{R}_{11}, \ldots, \boldsymbol{R}_{k k}\right)$ and $k=2$, the authors of [36] found elegant solutions to this problem, which we generalize to general $k$.

# 3.2. Maximal Bures-Wasserstein dependence 

We need the definition of majorization of two vectors and its behaviour under convex functions, as studied in [33].
Definition 3. For two vectors $\boldsymbol{x}, \boldsymbol{y} \in \mathbb{R}^{q}$, we say that $\boldsymbol{y}$ majorizes $\boldsymbol{x}$, denoted as $\boldsymbol{x} \prec \boldsymbol{y}$, if

$$
\left\{\begin{array}{r}
\sum_{i=1}^{\ell} x_{[i]} \leq \sum_{i=1}^{\ell} y_{[i]} \quad \text { for } \ell=1, \ldots, q-1 \\
\sum_{i=1}^{q} x_{[i]}=\sum_{i=1}^{q} y_{[i]}
\end{array}\right.
$$

where $x_{[1]} \geq \cdots \geq x_{[q]}$ are the components of $\boldsymbol{x}$ in decreasing order, and similarly for $\boldsymbol{y}$.
When $\boldsymbol{\lambda}$ and $\boldsymbol{\mu}$ are the vectors of eigenvalues of two correlation matrices, $\boldsymbol{\lambda}$ being majorized by $\boldsymbol{\mu}$ means that the proportion of the total variance explained by the $\ell$ first principal components is larger for the correlation matrix with eigenvalues $\boldsymbol{\mu}$, for any $\ell \in\{1, \ldots, q-1\}$, than for the correlation matrix with eigenvalues $\boldsymbol{\lambda}$. Fixing $k$ covariance matrices $\boldsymbol{R}_{11}, \ldots, \boldsymbol{R}_{k k}$ with $\boldsymbol{R}_{i i} \in \mathcal{S}_{\geq}^{d_{i}}$, the goal is now to find $\boldsymbol{R}_{m} \in \Gamma\left(\boldsymbol{R}_{11}, \ldots, \boldsymbol{R}_{k k}\right)$ whose ordered eigenvalues majorize those of any matrix $\boldsymbol{A} \in \Gamma\left(\boldsymbol{R}_{11}, \ldots, \boldsymbol{R}_{k k}\right)$. Together with Lemma 2 (see Proposition 3.C. 1 in [33]), this will enable us to characterize maximal dependence between $k$ random vectors in terms of covariance matrices.
Lemma 2. If $g: I \rightarrow \mathbb{R}$ is convex, with $I \subset \mathbb{R}$ an interval, then

$$
\boldsymbol{x} \prec \boldsymbol{y} \quad \Longrightarrow \quad \sum_{i=1}^{q} g\left(x_{i}\right) \leq \sum_{i=1}^{q} g\left(y_{i}\right) \quad \text { for all } \boldsymbol{x}, \boldsymbol{y} \in I^{q}
$$

Since the 2-Wasserstein dependence coefficients satisfy axiom (A1), we can assume that $d_{1} \leq d_{2} \leq \cdots \leq d_{k}$ without loss of generality. Suppose that

$$
\boldsymbol{R}_{i i}=\boldsymbol{U}_{i i} \boldsymbol{\Lambda}_{i i} \boldsymbol{U}_{i i}^{T}
$$

is the eigendecomposition of $\boldsymbol{R}_{i i}$, i.e., with $\boldsymbol{\Lambda}_{i i}=\operatorname{diag}\left(\lambda_{1, i i}, \lambda_{2, i i}, \ldots, \lambda_{d_{i}, i i}\right)$ the $d_{i} \times d_{i}$ diagonal matrix with $d_{i}$ ordered eigenvalues $\lambda_{1, i i} \geq \lambda_{2, i i} \geq \cdots \geq \lambda_{d_{i}, i i}$ on the diagonal (counting multiplicities), and $\boldsymbol{U}_{i i}$ an orthogonal matrix containing the corresponding eigenvectors for $i=1, \ldots, k$. The proof of Proposition 2, and all other theoretical results of Section 3, are provided in Appendix C.
Proposition 2. Let $\boldsymbol{R}_{i i} \in \mathcal{S}_{\geq}^{d_{i}}$ have eigendecomposition (6) for $i=1, \ldots, k$. Define the matrix $\boldsymbol{R}_{m}$ as

$$
\boldsymbol{R}_{m}=\left(\begin{array}{cccc}
\boldsymbol{R}_{11} & \boldsymbol{\Psi}_{12} & \cdots & \boldsymbol{\Psi}_{1 k} \\
\boldsymbol{\Psi}_{12}^{T} & \boldsymbol{R}_{22} & \cdots & \boldsymbol{\Psi}_{2 k} \\
\vdots & \vdots & \ddots & \vdots \\
\boldsymbol{\Psi}_{1 k}^{T} & \boldsymbol{\Psi}_{2 k}^{T} & \cdots & \boldsymbol{R}_{k k}
\end{array}\right) \in \mathbb{R}^{q \times q}
$$

with $q=d_{1}+\cdots+d_{k}$ and $d_{1} \leq d_{2} \leq \cdots \leq d_{k}$, and off-diagonal blocks

$$
\boldsymbol{\Psi}_{i j}=\boldsymbol{U}_{i i} \boldsymbol{\Lambda}_{i i}^{1 / 2} \boldsymbol{\Pi}_{i j} \boldsymbol{\Lambda}_{j j}^{1 / 2} \boldsymbol{U}_{j j}^{T} \in \mathbb{R}^{d_{i} \times d_{j}}
$$

where

$$
\boldsymbol{\Pi}_{i j}=\left(\boldsymbol{I}_{d_{i}} \mathbf{0}_{d_{i} \times\left(d_{j}-d_{i}\right)}\right) \in \mathbb{R}^{d_{i} \times d_{j}}
$$



the $d_{i} \times d_{j}$ upper left block of $I_{d_{i}+d_{j}}$ for $i=1, \ldots, k, j=i+1, \ldots, k$ (denoting $0_{d_{i} \times\left(d_{j}-d_{i}\right)}$ for the $d_{i} \times\left(d_{j}-d_{i}\right)$ matrix of zeroes). If we define $\lambda_{j, i i}=0$ for $j=d_{i}+1, \ldots, q$, the eigenvalues of $R^{m}$ are

$$
\lambda\left(R^{m}\right)=\left(\lambda_{j, 11}+\lambda_{j, 22}+\cdots+\lambda_{j, k k}\right)_{j=1}^{q}
$$

Furthermore, for any $A \in \Gamma\left(R_{11}, \ldots, R_{k k}\right)$ with eigenvalues $\lambda(A)=\left(\lambda_{j}\right)_{j=1}^{q}$, it holds that

$$
\lambda(A) \prec \lambda\left(R^{m}\right)
$$

Example 2 gives the matrix $R^{m}$ for some specific cases.
Example 2. Some expressions for $R^{m}$ in case $k=2$ can be found in [36]. If $d_{i}=1$ with $R_{i i}=1$ for all $i=1, \ldots, k$, the matrix $R^{m}$ is obviously given by $1_{q \times q}$, a matrix full of ones. Consider next $Z_{i}=\left(Z_{i 1}, Z_{i 2}\right)$ for $i=1, \ldots, k$, i.e., $k$ bivariate random vectors, with covariance matrix of $\left(Z_{i 1}, Z_{i 2}\right)$ given by

$$
R_{i i}=\left(\begin{array}{cc}
1 & \rho_{i} \\
\rho_{i} & 1
\end{array}\right)
$$

Assuming $\rho_{i}, \rho_{j} \geq 0$, one can check that $\Psi_{i j}$ of $R^{m}$ in (7) for $i=1, \ldots, k-1$ and $j=i+1, \ldots, k$ is given by

$$
\Psi_{i j}=\left(\begin{array}{cc}
\sqrt{1+\rho_{i}} \sqrt{1+\rho_{j}}+\sqrt{1-\rho_{i}} \sqrt{1-\rho_{j}} & 2 \\
\sqrt{1+\rho_{i}} \sqrt{1+\rho_{j}}-\sqrt{1-\rho_{i}} \sqrt{1-\rho_{j}} & 2 \\
\sqrt{1+\rho_{i}} \sqrt{1+\rho_{j}}-\sqrt{1-\rho_{i}} \sqrt{1-\rho_{j}} & 2 \\
\sqrt{1+\rho_{i}} \sqrt{1+\rho_{j}}+\sqrt{1-\rho_{i}} \sqrt{1-\rho_{j}} & 2
\end{array}\right)
$$

The result is similar in case $\rho_{i} \leq 0$ or $\rho_{j} \leq 0$ up to some signs (orthogonal transformations, to which $d_{W}$ is invariant).
The principal components of $\left(Z_{i 1}, Z_{i 2}\right)$ are

$$
Y_{i 1}=\frac{1}{\sqrt{2}}\left(Z_{i 1}+Z_{i 2}\right) \text { and } Y_{i 2}=\frac{1}{\sqrt{2}}\left(Z_{i 2}-Z_{i 1}\right)
$$

corresponding to the eigenvalues $1+\rho_{i} \geq 1-\rho_{i}$ respectively, with

$$
\operatorname{Corr}\left(Y_{i 1}, Y_{j 1}\right)=\frac{\operatorname{Corr}\left(Z_{i 2}, Z_{j 2}\right)+\operatorname{Corr}\left(Z_{i 2}, Z_{j 1}\right)+\operatorname{Corr}\left(Z_{i 1}, Z_{j 2}\right)+\operatorname{Corr}\left(Z_{i 1}, Z_{j 1}\right)}{2 \sqrt{1+\operatorname{Corr}\left(Z_{i 1}, Z_{i 2}\right) \rho^{1}}+\operatorname{Corr}\left(Z_{j 1}, Z_{j 2}\right)}
$$

and

$$
\operatorname{Corr}\left(Y_{i 2}, Y_{j 2}\right)=\frac{\operatorname{Corr}\left(Z_{i 2}, Z_{j 2}\right)-\operatorname{Corr}\left(Z_{i 2}, Z_{j 1}\right)-\operatorname{Corr}\left(Z_{i 1}, Z_{j 2}\right)+\operatorname{Corr}\left(Z_{i 1}, Z_{j 1}\right)}{2 \sqrt{1-\operatorname{Corr}\left(Z_{i 1}, Z_{i 2}\right) \rho^{1}-\operatorname{Corr}\left(Z_{j 1}, Z_{j 2}\right)}}
$$

A quick check then verifies that if $\left(\left(Z_{11}, Z_{12}\right), \ldots,\left(Z_{k 1}, Z_{k 2}\right)\right)$ has correlation matrix $R^{m}$ with blocks (9), it holds that $\operatorname{Corr}\left(Y_{i 1}, Y_{j 1}\right)=\operatorname{Corr}\left(Y_{i 2}, Y_{j 2}\right)=1$ for all $i=1, \ldots, k-1$ and $j=i+1, \ldots, k$, i.e., all first principal components are perfectly correlated and all second principal components as well.

Proposition 3 states that the matrix $R^{m}$ in (7) maximizes the intensity of dependence, i.e., $D_{1}\left(R^{m}\right)=D_{2}\left(R^{m}\right)=1$ when taking $\mathcal{G}_{R}=\Gamma\left(R_{11}, \ldots, R_{k k}\right)$ for fixed marginal covariance matrices $R_{11}, \ldots, R_{k k}$.

Proposition 3. Let $q=d_{1}+\cdots+d_{k}$ and $R_{i i} \in S_{\geq}^{d_{i}}$ for $i=1, \ldots, k$. The matrix $R^{m}$ in (7) maximizes $d_{W}\left(R, I_{q}\right)$ and $d_{W}\left(R, R_{0}\right)$ with $R_{0}$ given in (4) among all $R \in \Gamma\left(R_{11}, \ldots, R_{k k}\right)$.

A general interpretation of $R^{m}$ is given in Remark 2. .
Remark 2. Assuming again that $d_{1} \leq d_{2} \leq \cdots \leq d_{k}$, the matrix $R^{m}$ in (7) is the covariance matrix of

$$
\left(\begin{array}{c}
U_{11} \Lambda_{11}^{1 / 2} Z_{1} \\
U_{22} \Lambda_{22}^{1 / 2} Z_{2} \\
\vdots \\
U_{k k} \Lambda_{k k}^{1 / 2} Z_{k}
\end{array}\right) \in \mathbb{R}^{q \times 1}
$$



where $\boldsymbol{Z}_{1}=\left(Z_{11}, \ldots, Z_{1 d_{1}}\right)^{T}, \boldsymbol{Z}_{2}=\left(Z_{21}, \ldots, Z_{2 d_{2}}\right)^{T}, \ldots, \boldsymbol{Z}_{k}=\left(Z_{k 1}, \ldots, Z_{k d_{k}}\right)^{T}$ such that for all $i=1, \ldots, k$ we have $\boldsymbol{Z}_{i} \sim \mathcal{N}_{d_{i}}\left(\mathbf{0}_{d_{i}}, I_{d_{i}}\right)$, and in addition $Z_{i j}=Z_{(i+1) j}$ for all $i=1, \ldots, k-1, j=1, \ldots, d_{i}$, i.e., $\boldsymbol{Z}_{i}$ and $\boldsymbol{Z}_{j}$ have the first $\min \left\{d_{i}, d_{j}\right\}$ components in common for all $i, j \in\{1, \ldots, k\}$. The correlation matrix of the principal components of $\boldsymbol{U}_{11} \boldsymbol{\Lambda}_{11}^{1 / 2} \boldsymbol{Z}_{1}, \ldots, \boldsymbol{U}_{k k} \boldsymbol{\Lambda}_{k k}^{1 / 2} \boldsymbol{Z}_{k}$ is


with $\boldsymbol{\Pi}_{i j}$ as in Proposition 2. Hence, if $\left(\boldsymbol{X}_{1}, \ldots, \boldsymbol{X}_{k}\right)$ has a Gaussian copula with covariance matrix $\boldsymbol{R}_{m}$, then for $\ell=1, \ldots, \min \left\{d_{i}, d_{j}\right\}$ the $\ell$-th principal components of $\left(\left(\Phi^{-1} \circ F_{i 1}\right)\left(X_{i 1}\right), \ldots,\left(\Phi^{-1} \circ F_{i d_{i}}\right)\left(X_{i d_{i}}\right)\right)$ and $\left(\left(\Phi^{-1} \circ F_{j 1}\right)\left(X_{j 1}\right), \ldots\right.$, $\left(\Phi^{-1} \circ F_{j d_{j}}\right)\left(X_{j d_{j}}\right)$ ) are perfectly correlated for all $i, j \in\{1, \ldots, k\}$. This is the interpretation of maximal dependence for the Bures-Wasserstein dependence measures.

In the upcoming section, we also assume that $\mathrm{GR}=\Gamma\left(\boldsymbol{R}_{11}, \ldots, \boldsymbol{R}_{k k}\right)$.

# 3.3. Statistical inference 

In practice, we have an i.i.d. sample $\boldsymbol{X}^{(\ell)}=\left(\boldsymbol{X}_{1}^{(\ell)}, \ldots, \boldsymbol{X}_{k}^{(\ell)}\right)$ for $\ell=1, \ldots, n$ from $\boldsymbol{X}$, where $\boldsymbol{X}_{i}^{(\ell)}=\left(X_{i 1}^{(\ell)}, \ldots, X_{i d_{i}}^{(\ell)}\right)$ for $\ell=1, \ldots, n$ is a sample from $\boldsymbol{X}_{i}$ for $i=1, \ldots, k$. A natural estimator for the Gaussian copula covariance matrix is known as the matrix of sample normal scores rank correlation coefficients (see, e.g., [24]),

$$
\widehat{\boldsymbol{R}}_{n}=\left(\begin{array}{ccccc}
\widehat{R}_{11} & \widehat{R}_{12} & \ldots & \widehat{R}_{1 k} & \widehat{R}_{12}^{T} \\
\widehat{R}_{22} & \ldots & & \widehat{R}_{2 k} & \\
\vdots & & \ddots & & \vdots \\
\widehat{R}_{1 k}^{T} & \widehat{R}_{2 k}^{T} & \ldots & \widehat{R}_{k k} &
\end{array}\right)
$$

with $\left(\widehat{R}_{i m}\right)_{j t}=\widehat{\rho}_{i j, m t}=\frac{1}{n} \sum_{\ell=1}^{n} \widehat{Z}_{i j}^{(\ell)} \widehat{Z}_{m t}^{(\ell)} \frac{1}{\sqrt{n}} \sum_{\ell=1}^{n}\left\{\Phi^{-1}\left(\frac{\ell}{n+1}\right)\right\}^{2}$,
defined by computing normal scores

$$
\widehat{Z}_{i j}^{(\ell)}=\Phi^{-1}\left(\frac{n}{n+1} \widehat{F}_{i j}\left(X_{i j}^{(\ell)}\right)\right)
$$

defined by computing normal scores

$$
\widehat{Z}_{i j}^{(\ell)}=\Phi^{-1}\left(\frac{n}{n+1} \widehat{F}_{i j}\left(X_{i j}^{(\ell)}\right)\right)
$$

obtained through the empirical $\operatorname{cdf} \widehat{F}_{i j}\left(x_{i j}\right)=\frac{1}{n} \sum_{\ell=1}^{n} \mathbf{1}\left\{X_{i j}^{(\ell)} \leq x_{i j}\right\}$ for $i=1, \ldots, k$ and $j=1, \ldots, d_{i}$. The quantity $\widehat{\rho}_{i j, m t}$ is calculated as the conventional Pearson correlation of the bivariate scores $\left(\left(\widehat{Z}_{i j}^{(1)}, \widehat{Z}_{m t}^{(1)}\right), \ldots,\left(\widehat{Z}_{i j}^{(n)}, \widehat{Z}_{m t}^{(n)}\right)\right)$ and by observing that

$$
\frac{1}{n} \sum_{\ell=1}^{n} \widehat{Z}_{i j}^{(\ell)}=\frac{1}{n} \sum_{\ell=1}^{n} \Phi^{-1}\left(\frac{\ell}{n+1}\right)=0 \text { and } \frac{1}{n} \sum_{\ell=1}^{n}\left(\widehat{Z}_{i j}^{(\ell)}\right)^{2}=\frac{1}{n} \sum_{\ell=1}^{n}\left\{\Phi^{-1}\left(\frac{\ell}{n+1}\right)\right\}^{2}
$$

which holds because $\Phi^{-1}(\alpha)=-\Phi^{-1}(1-\alpha)$ for $\alpha \in[0,1]$ and $n \widehat{F}_{i j}\left(X_{i j}^{(\ell)}\right)$ is the rank of $X_{i j}^{(\ell)}$ in the sample $X_{i j}^{(1)}, \ldots, X_{i j}^{(n)}$. A next natural step in estimating $\operatorname{Dr}(\boldsymbol{R})$ is to plug in $\widehat{\boldsymbol{R}}_{n}$ for the unknown $\boldsymbol{R}$. Define the map $\boldsymbol{\phi}$ by $\boldsymbol{\phi}(\boldsymbol{\Sigma})=$ $\boldsymbol{D}_{\boldsymbol{\Sigma}}^{-1 / 2} \boldsymbol{\Sigma} \boldsymbol{D}_{\boldsymbol{\Sigma}}^{-1 / 2}$ for $\boldsymbol{\Sigma} \boldsymbol{\in} \mathcal{S}^{q}$, where $\boldsymbol{D}_{\boldsymbol{\Sigma}}$ is the diagonal matrix containing the diagonal of $\boldsymbol{\Sigma}$, and let $\|\boldsymbol{\Sigma}\|_{F}=\operatorname{tr}^{1 / 2}\left(\boldsymbol{\Sigma}^{T} \boldsymbol{\Sigma}\right)$ be the Frobenius norm. Fréchet differentiability of the mapping

$$
\left(\mathcal{S}^{q},\|\cdot\|_{F}\right) \rightarrow(\mathbb{R},|\cdot|): \boldsymbol{\Sigma} \mapsto(\operatorname{Dr} \circ \boldsymbol{\phi})(\boldsymbol{\Sigma})
$$

on $\mathcal{S}^{q}$
> suffices in order for the delta method to transform an asymptotic normality result for $\widehat{\boldsymbol{R}}_{n}$ into an asymptotic normality result

be the projection matrix onto the $d_{i}$ coordinates, satisfying $R_{i i}=P_{i} R P_{i}^{\top}$. Partition the matrix $\Lambda_{i i}$ as

$$
\Lambda_{i i}=\left(\begin{array}{lll}
\Lambda_{i i, 1} & \cdots & 0_{d_{1} \times\left(d_{2}-d_{1}\right)} \\
0_{d_{1} \times\left(d_{2}-d_{1}\right)}^{\top} & \Lambda_{i i, 2} & \cdots \\
\vdots & \vdots & \ddots \\
0_{d_{1} \times\left(d_{i}-d_{i-1}\right)}^{\top} & 0_{\left(d_{2}-d_{1}\right) \times\left(d_{i}-d_{i-1}\right)}^{\top} & \cdots \\
& & \Lambda_{i i, i}
\end{array}\right) \in \mathbb{R}^{d_{i} \times d_{i}}
$$

with $\Lambda_{i i, j} \in \mathbb{R}^{\left(d_{j}-d_{j-1}\right) \times\left(d_{j}-d_{j-1}\right)}$ for $j=1, \ldots, i$ and defining $d_{0}=0$. Based on these partitions, further define

$$
\begin{aligned}
\Delta_{1} & =\left(\Lambda_{11,1}+\Lambda_{22,1}+\cdots+\Lambda_{k k, 1}\right)^{-1 / 2} \in \mathbb{R}^{d_{1} \times d_{1}} \\
\widetilde{\Delta}_{1} & =\left(\Lambda_{11,1}^{2}+\Lambda_{22,1}^{2}+\cdots+\Lambda_{k k, 1}^{2}\right)^{-1 / 2} \Lambda_{11,1} \in \mathbb{R}^{d_{1} \times d_{1}} \\
\Delta_{i} & =\left(\begin{array}{cc}
\Delta_{i-1} & 0_{d_{i-1} \times\left(d_{i}-d_{i-1}\right)} \\
0_{d_{i-1} \times\left(d_{i}-d_{i-1}\right)}^{\top} & \left(\Lambda_{i i, i}+\Lambda_{(i+1)(i+1), i}+\cdots+\Lambda_{k k, i}\right)^{-1 / 2}
\end{array}\right) \in \mathbb{R}^{d_{i} \times d_{i}} \\
\widetilde{\Delta}_{i} & =\left(\begin{array}{cc}
\widetilde{\Delta}_{i-1} D_{i} & 0_{d_{i-1} \times\left(d_{i}-d_{i-1}\right)} \\
0_{d_{i-1} \times\left(d_{i}-d_{i-1}\right)}^{\top} & \left(\Lambda_{i i, i}^{2}+\Lambda_{(i+1)(i+1), i}^{2}+\cdots+\Lambda_{k k, i}^{2}\right)^{-1 / 2} \Lambda_{i i, i}
\end{array}\right) \in \mathbb{R}^{d_{i} \times d_{i}}
\end{aligned}
$$

for $i=2, \ldots, k$ with $D_{i}=\operatorname{diag}\left(\Lambda_{(i-1)(i-1), 1}^{-1} \Lambda_{i i, 1}, \ldots, \Lambda_{(i-1)(i-1), i-1}^{-1} \Lambda_{i i, i-1}\right) \in \mathbb{R}^{d_{i-1} \times d_{i-1}}$. Finally, we will need the matrices

$$
J=R_{0}^{-1 / 2}\left(R_{0}^{1 / 2} R R_{0}^{1 / 2}\right)^{1 / 2} R_{0}^{-1 / 2}=\left(\begin{array}{cccc}
J_{11} & J_{12} & \cdots & J_{1 k} \\
J_{21} & J_{22} & \cdots & J_{2 k} \\
\vdots & \vdots & \ddots & \vdots \\
J_{k 1} & J_{k 2} & \cdots & J_{k k}
\end{array}\right) \in \mathbb{R}^{q \times q}
$$

with $J_{i j} \in \mathbb{R}^{d_{i} \times d_{j}}$ and

$$
J_{0}=\operatorname{diag}\left(J_{11}, \ldots, J_{k k}\right) \in \mathbb{R}^{q \times q}
$$

Theorem 1 formally states an asymptotic normality result for the estimator $\operatorname{Dr}\left(\widehat{R}_{n}\right)$.
Theorem 1. Let $X$ have a Gaussian copula with correlation matrix $R \in \mathbb{S}_{>}^{q}$ with $R \neq R_{0}$ such that $R_{i i} \in \mathbb{S}_{>}^{d_{i}}$ has $d_{i}$ distinct eigenvalues, and let $\widehat{R}_{n}$ be given by (10) based on which the plug-in estimator $\widehat{\mathcal{D}}_{r, n}=\operatorname{Dr}\left(\widehat{R}_{n}\right)$ is constructed. Then for $r \in\{1,2\}$, it holds that $\sqrt{n}\left(\widehat{\mathcal{D}}_{r, n}-\mathcal{D}_{r}(R)\right) \xrightarrow{\mathrm{d}} N\left(0_{q}, \zeta_{r}^{2}\right)$ as $n \rightarrow \infty$, with asymptotic variance

$$
\zeta_{r}^{2}=2 \operatorname{tr}\left[\left\{R\left(M_{r}-\mathcal{D}_{M_{r}} R\right)\right\}^{2}\right]
$$

where $\mathcal{D}_{M_{r} R}$ is the diagonal matrix consisting of the diagonal of $M_{r} R$, and

$$
\begin{aligned}
& M_{1}=\frac{1}{2 C_{1}}\left(-R^{-1 / 2}+\left(1-D_{1}(R)\right) R^{-1 / 2}\right. \\
& \left.+\underline{D}_{1}(R) \Upsilon_{1}\right), \quad M_{2}=\frac{1}{C_{2}}\left(-\frac{1}{2}\left(J_{0}+J^{-1}\right)+\left(1-D_{2}(R)\right) I_{q}+\underline{D}_{2}(R) \Upsilon_{2}\right)
\end{aligned}
$$

with

$$
C_{1}=\sum_{i=1}^{k} \operatorname{tr}\left(R_{i i}^{1 / 2}\right)-\operatorname{tr}\left(R_{m}^{1 / 2}\right), \quad \Upsilon_{1}=\left(\begin{array}{cccc}
U_{11} \Delta_{1} U_{11}^{\top} & 0_{d_{1} \times d_{2}} & \cdots & 0_{d_{1} \times d_{k}} \\
0_{d_{1} \times d_{2}}^{\top} & U_{22} \Delta_{2} U_{22}^{\top} & \cdots & 0_{d_{2} \times d_{k}} \\
\vdots & \vdots & \ddots & \vdots \\
0_{d_{1} \times d_{k}}^{\top} & 0_{d_{2} \times d_{k}}^{\top} & \cdots & U_{k k} \Delta_{k} U_{k k}^{\top}
\end{array}\right)
$$

and

$$
C_{2}=\operatorname{tr}(R)-\operatorname{tr}\left\{\left(R_{0}^{1 / 2} R_{m} R_{0}^{1 / 2}\right)^{1 / 2}\right\}, \quad \Upsilon_{2}=\left(\begin{array}{cccc}
U_{11} \widetilde{\Delta}_{1} U_{11}^{\top} & 0_{d_{1

Remark 3. When $\mathbb{R}=\mathbb{R}_{0}$, it holds that $\underline{\zeta}^{r}=0$ and $\sqrt{n} \widehat{\mathbf{D}}_{r, n} \xrightarrow{p} 0$ for $n \rightarrow \infty$. The higher-order delta method can however still provide a weak convergence result for $\sqrt{n} \widehat{\mathbf{D}}_{r, n}$. A detailed study of this is research in progress.

We look at another example, which is also studied in [12], but in the context of $\Phi$-dependence measures.
Example 3. Consider a four dimensional random vector $\left(X_{1}, X_{2}, X_{3}, X_{4}\right)$ having a Gaussian copula with covariance matrix

$$
\left(\begin{array}{cccc}
1 & \rho_{1} & \rho_{2} & \rho_{2} \\
\rho_{1} & 1 & \rho_{2} & \rho_{2} \\
\rho_{2} & \rho_{2} & 1 & \rho_{1} \\
\rho_{2} & \rho_{1} & \rho_{1} & 1
\end{array}\right)
$$

where

$$
\rho_{1} \geq 2\left|\rho_{2}\right|-1
$$

Then one can check that (recall also Example 2 for finding the matrix $\mathbf{R}_{m}$ )



Fig. 1: Dependence coefficients (19) (left) and (20) (right) as a function of $\rho_{2}$ for different values of $\rho_{1}$.

$$
D_{1}\left(\left(X_{1}, X_{2}\right) ;\left(X_{3}, X_{4}\right)\right)=\frac{2\left(1+\rho_{1}\right)^{1 / 2}-\left(\rho_{1}-2 \rho_{2}+1\right)^{1 / 2}-\left(\rho_{1}+2 \rho_{2}+1\right)^{1 / 2}}{(2-\sqrt{2})\left\{\left(1+\rho_{1}\right)^{1 / 2}+\left(1-\rho_{1}\right)^{1 / 2}\right\}}
$$

and
$\mathfrak{D}_{\mathbf{2}}\left(\left(X_{1}, X_{2}\right) ;\left(X_{3}, X_{4}\right)\right)=\frac{4-2\left|1-\rho_{1}\right|-\left(\rho_{1}^{2}+2 \rho_{1}-2 \rho_{1} \rho_{2}-2 \rho_{2}+1\right)^{1 / 2}-\left(\rho_{1}^{2}+2 \rho_{1}+2 \rho_{1} \rho_{2}+2 \rho_{2}+1\right)^{1 / 2}}{4-\sqrt{2}\left\{\left|1-\rho_{1}\right|+\rho_{1}+1\right\}}$.

Fig. 1 shows how (19) and (20) depend on $\rho_{2}$ for different values of $\rho_{1}$. Clearly, independence holds if and only if $\rho_{2}=0$, as it should. When $\rho_{1}=2\left|\rho_{2}\right|-1$, the second principal component of $\left(Z_{1}, Z_{2}\right)=\left(\left(\Phi^{-1} \circ \mathbb{F}_{1}\right)\left(X_{1}\right),\left(\Phi^{-1} \circ \mathbb{F}_{2}\right)\left(X_{2}\right)\right)$ is perfectly correlated with the second principal component of $\left(Z_{3}, Z_{4}\right)=\left(\left(\Phi^{-1} \circ \mathbb{F}_{3}\right)\left(X_{3}\right),\left(\Phi^{-1} \circ \mathbb{F}_{4}\right)\left(X_{4}\right)\right)$, where $\mathbb{F}_{i}$ is the marginal distribution of $X_{i}$ for $i=1,2,3$, 4, see also [12]. This causes the $\Phi$-dependence measures studied in [12] to reach their maximum value, because a singularity is attained. In particular, taking for instance $\rho_{1}=-0.4$ and $\rho_{2}=0.3$, all (normalized) $\Phi$-dependence measures equal 1 , while $\mathfrak{D}_{1}=0.396$ and $\mathfrak{D}_{2}=0.3$. The reason for $\mathfrak{D}_{1}$ and $\mathfrak{D}_{2}$ still being small, is that $\rho_{2}$ is pretty small and, recalling Remark 2 , not both first and second principal components of $\left(Z_{1}, Z_{2}\right)$ and $\left(Z_{3}, Z_{4}\right)$ are perfectly correlated, only one of them is. Only when $\left|\rho_{2}\right|=1$ and thus also $\rho_{1}=1$, we have $\mathfrak{D}_{1}=\mathfrak{D}_{2}=1$. Maximal Bures-Wasserstein dependence is not attainable for the family (18) if $\rho_{1} \neq 1$, because it imposes additional restrictions on the correlations (i.e., not every element in $\Gamma\left(R_{11}, \ldots, R_{k k}\right)$ is a member of (18)). Picking a set $\mathcal{G}_{\mathbb{R}} \subset \Gamma\left(R_{11}, \ldots, R_{k k}\right)$ for a normalization that adjusts according to these restrictions, would lead to more cases of maximal dependence.





Fig. 2: Asymptotic standard deviation of dependence coefficients (19) (left) and (20) (right) as a function of $\rho_{2}$ for different values of $\rho_{1}$.

Fig. 2 depicts the asymptotic standard deviation $\zeta_{r}$ of $D_{r}$ for $r \in\{1,2\}$ as given in Theorem 1 for this specific example. We mainly observe increasing behaviour when the strength of dependence increases. However, in some cases where $\rho_{1}$ and $\rho_{2}$ get close to satisfying $\left|\rho_{2}\right|=\left(\rho_{1}+1\right) / 2$, we see the asymptotic standard deviation going down. For example, if $\rho_{1}=0$, the asymptotic standard deviation $\zeta_{1}$ is maximal $(\approx 0.275)$ at $\left|\rho_{2}\right| \approx 0.426$, after which it converges to $\approx 0.214$ for$\left|\rho_{2}\right| \rightarrow 0.5$. When keeping $\rho_{1}$ fixed and letting $\left|\rho_{2}\right| \rightarrow\left(\rho_{1}+1\right) / 2$, the dependence $D_{r}$ attains a local maximum, which it cannot transcend, resulting in (slightly) lower asymptotic variance. This behaviour was also noticed in the same example in [12] for their (normalized) $\Phi$-dependence measures, whose asymptotic variance tends to zero when $\left|\rho_{2}\right| \rightarrow\left(\rho_{1}+1\right) / 2$, because the singularity forces them to reach their global maximum. For the optimal transport dependence coefficients, the global maximum is only attained when $\left|\rho_{2}\right|, \rho_{1} \rightarrow 1$, in which case the asymptotic variance also tends to zero.

# 4. A Gaussian copula approach: regularized estimation 

Empirical covariance matrices are known to approach singularity when the dimension is close to the sample size. The estimator $\widehat{D}_{r, n}$ does not require an inverted covariance matrix, but it inquires about eigenvalue dispersion, and this tends to be biased when using the empirical covariance matrix, see, e.g., [31]. Typically, estimates of large eigenvalues tend to be biased upwards, and estimates of small eigenvalues tend to be biased downwards. Increasing dimensionality aggravates this, but penalization techniques can be used to restrain. We briefly discuss ridge regularization, as in [50], but now in a Gaussian copula context.

Of course, the ridge estimator will not completely shrink elements of the empirical covariance matrix to zero. However, the task might be to find a likely estimate for which multiple variables are marginally independent, i.e., a sparse estimate of the covariance matrix having zero entries. For this purpose, we look at a Gaussian copula formulation of the penalization ideas discussed in [29]. Finally, penalties can also be applied to groups of elements instead of just individual elements. A group lasso penalty, for instance, enables to shrink entire blocks of the covariance matrix to zero.

In Section 4.1, we discuss penalization methods for the Gaussian copula covariance matrix in case $q$ remains fixed with the sample size. Afterwards, in Section 4.2, we briefly touch upon the case where $q$ depends on $n$.

### 4.1. Fixed dimension

Denote $\widehat{\Sigma}_{\mathrm{ML}}$ for the maximum likelihood estimator of a $\mathcal{N}_{q}\left(\mathbf{0}_{q}, \Sigma\right)$ model, and $R=\varphi(\Sigma)=D_{\Sigma}^{-1 / 2} \Sigma D_{\Sigma}^{-1 / 2}$ the correlation matrix corresponding to $\Sigma$ (recall that $D_{\Sigma}$ is the diagonal matrix containing the diagonal of $\left.\Sigma\right)$. By adding a certain penalty, say $P_{\bullet}\left(\Sigma, \omega_{n}\right)$ to the Gaussian log-likelihood, where $\omega_{n}$ is a certain penalty parameter depending on $n$, a general penalized optimization problem for estimating $\Sigma$ (under the constraint of positive definiteness $\Sigma \succ 0$ ), is given by



$$
\widehat{\boldsymbol{\Sigma}}_{\bullet} \in \underset{\boldsymbol{\Sigma} \succ \mathbf{0}}{\arg \min _{n}}\left\{\ln |\boldsymbol{\Sigma}|+\operatorname{tr}\left(\boldsymbol{\Sigma}^{-1} \widehat{\boldsymbol{\Sigma}}_{M L}\right)+P_{\bullet}\left(\boldsymbol{\Sigma}, \omega_{n}\right)\right\}
$$

and corresponding correlation matrix $\widehat{\boldsymbol{R}}_{\bullet}=\phi\left(\widehat{\boldsymbol{\Sigma}}_{\bullet}\right)$. However, the core of this paper is that we merely assume a Gaussian copula. Hence, instead of making use of $\widehat{\boldsymbol{\Sigma}}_{M L}$, we compute $\widehat{\boldsymbol{\Sigma}}_{n}$, being the (block) matrix of sample normal scores rank covariances with entries $n^{-1} \sum_{\ell=1}^{n} \widehat{Z}_{i j}^{(\ell)} \widehat{Z}_{m t}^{(\ell)}$ for $i, m \in\{1, \ldots, k\}, j \in\left\{1, \ldots, d_{i}\right\}, t \in\left\{1, \ldots, d_{m}\right\}$ (similar block notation as in (10)). The main difference is that we do not have true Gaussian scores, but only non-parametrically estimated Gaussian scores $\widehat{Z}_{i j}^{(\ell)}=\Phi^{-1}\left(n /(n+1) \widehat{F}_{i j}\left(X_{i j}^{(\ell)}\right)\right)$. The copula formulation of (21) becomes

$$
\widehat{\boldsymbol{\Sigma}}_{\bullet, n} \in \underset{\boldsymbol{\Sigma} \succ \mathbf{0}}{\arg \min _{n}}\left\{\ln |\boldsymbol{\Sigma}|+\operatorname{tr}\left(\boldsymbol{\Sigma}^{-1} \widehat{\boldsymbol{\Sigma}}_{n}\right)+P_{\bullet}\left(\boldsymbol{\Sigma}, \omega_{n}\right)\right\}
$$

where we use the additional subscript $n$ in $\widehat{\boldsymbol{\Sigma}}_{\bullet, n}$ to indicate that we are in the copula context. A genuine Gaussian copula correlation matrix is then $\widehat{\boldsymbol{R}}_{\bullet, n}=\phi\left(\widehat{\boldsymbol{\Sigma}}_{\bullet, n}\right)$.
We go deeper into three choices for the penalty $P_{\bullet}$ :

- the ridge penalty $P_{R}\left(\boldsymbol{\Sigma}, \omega_{n}\right)=\left(1-\omega_{n}\right) \operatorname{tr}\left(\boldsymbol{R}^{-1}\right)$, where $\omega_{n} \in(0,1]$
- (adaptive) lasso-type penalties $P_{L T}\left(\boldsymbol{\Sigma}, \omega_{n}\right)=\sum_{i, j, m, t} p_{\omega_{n}}\left(\Delta_{i j, m t}\left|\sigma_{i j, m t}\right|\right)$, where $\sigma_{i j, m t}$ is the $(j, t)$ 'th element of the $(i, m)$ 'th block of $\boldsymbol{\Sigma}$ (similar block notation as in (10)), $\Delta_{i j, m t} \geq 0$ is a weight (e.g., zero when $(i, j)=(m, t)$ in order to not shrink diagonal elements, or larger for smaller preliminary estimated entries in order to shrink these more) and $p_{\omega_{n}}$ is a certain penalty function depending on $\omega_{n} \geq 0$
- group lasso-type penalties $P_{G L T}\left(\boldsymbol{\Sigma}, \omega_{n}\right)=2 \sum_{i, m=1, m>i}^{k} p_{\omega_{n}}\left(\sqrt{d_{i} d_{m}}\left\|\boldsymbol{\Sigma}_{i m}\right\|_{F}\right)+\sum_{i=1}^{k} p_{\omega_{n}}\left(\sqrt{d_{i}\left(d_{i}-1\right)}\left\|\boldsymbol{\Delta}_{i} * \boldsymbol{\Sigma}_{i i}\right\|_{F}\right)$, where $\|\cdot\|_{F}$ is the Frobenius matrix norm, $\boldsymbol{\Delta}_{i} \in \mathbb{R}^{d_{i} \times d_{i}}$ a matrix with ones as off-diagonal elements and zeroes on the diagonal (in order to avoid shrinking the variances), and $p_{\omega_{n}}$ a certain penalty function depending on $\omega_{n} \geq 0$.

The ridge penalty is different from the other ones (and will also be considered separately in the simulations in Section 5) in the sense that it only focuses on improving the estimation of the Gaussian copula covariance matrix (and corresponding dependence coefficients) when $q$ is large compared to $n$, and not on a sparsity assumption. Asymptotic properties are centred around consistency. Having $q>n$ is definitely manageable for ridge penalization. For the latter two penalties, the set $A$ defined as $A=\left\{\alpha: \sigma_{\alpha} \neq 0, \alpha=1, \ldots, \widetilde{q}\right\}$, where $\sigma=\operatorname{vech}(\boldsymbol{\Sigma}) \in \mathbb{R}^{\widetilde{q}}$ is the vector of upper diagonal elements of $\boldsymbol{\Sigma}$ and $\widetilde{q}=q(q-1) / 2$, is of crucial importance. Indeed, next to consistency, we hope that $P\left(A_{n}=A\right) \rightarrow 1$ for $n \rightarrow \infty$, where $A_{n}=\left\{\alpha: \widehat{\sigma}_{n, \alpha} \neq 0, \alpha=1, \ldots, \widetilde{q}\right\}$, with $\widehat{\sigma}_{n}=\operatorname{vech}\left(\widehat{\boldsymbol{\Sigma}}_{\bullet, n}\right)$, a property called sparsistency. Having $q>n$ leads to degeneracy of the lasso-type estimators, which is why we restrict ourselves to $q \leq n$ in the simulations.
Example 4 shows that the sparsity of $\boldsymbol{\Sigma}$ (which is obviously preserved by $\boldsymbol{R}$ ), i.e., the entries belonging to $A^{c}$, can manifest itself in different forms, calling for different shrinkage penalties.

Example 4. A covariance graph is a graphical model that represents variables as nodes and marginal dependencies as edges (similar to a Markov random field representing conditional dependencies), see, e.g., Section 1 of [4] for several references. Marginal independencies correspond to individual zeroes in the correlation matrix and many different sparsity patterns can occur. The first plot of Fig. 3 shows the sparsity structure of a correlation matrix of a random covariance graph for a total of 20 variables, where $32.5 \%$ of the elements equal zero, corresponding to the TRUE entries. A penalty of the form $P_{L T}$ allows reflecting these marginal independencies in the estimated correlation matrix, and could result in a better plug-in estimator for our dependence measures.

Next, imagine a person answering a total of twenty questions in the form of seven short questionnaires $\mathbf{X}_{1}, \ldots, \mathbf{X}_{7}$, all consisting of three questions, except for $\mathbf{X}_{7}$, which only contains two. The interest is in the relationship between the answers of the different questionnaires. Furthermore, assume that $\mathbf{X}_{1}, \ldots, \mathbf{X}_{6}$ are on completely different topics, and all three questions are each time self-contained. Only the very last two questions contained in $\mathbf{X}_{7}$ are related to each other, and to the other questions in the first six questionnaires as well. Then, it can be expected that only the blocks ${\underset{R}{R}}_{i 7}$ for $i=1, \ldots, 6$ and ${\underset{R}{R}}_{77}$ are different from zero (and the diagonal of $\boldsymbol{R}$, of course), i.e., $\boldsymbol{R}$ has a sparsity pattern as visualized in the second plot of Fig. 3, where $76.5 \%$ of the elements equal zero. Such a pattern calls for





Fig. 3: Different sparsity patterns of a 20 dimensional correlation matrix.
a PGLT penalty, enabling shrinkage of entire blocks, and possibly more accurate estimation of the Gaussian copula dependence coefficients compared to using the matrix of normal scores rank correlations $\widehat{R}_{n}$, or a PLT penalty.

We shall now elaborate more on the theoretical properties and computational aspects of the estimators $\widehat{\Sigma}_{R, n}, \widehat{\Sigma}_{L T, n}$ and $\widehat{\Sigma}_{\mathrm{GLT}, n}$ given in (22) corresponding to the three types of penalties $P_{R}, P_{L T}$ and $P_{\mathrm{GLT}}$.

# Ridge regularization 

Warton [50] extensively studies the estimator $\widehat{\Sigma}_{R}$, i.e., the estimator (21) under the assumption of a normal distribution, with penalty term $P_{R}\left(\Sigma, \omega_{n}\right)=\left(1-\omega_{n}\right) \operatorname{tr}\left(\mathcal{R}^{-1}\right)$ for $\mathcal{R}=\phi(\Sigma)=D_{\Sigma}^{-1 / 2} \Sigma D_{\Sigma}^{-1 / 2}$ and $\omega_{n} \in(0,1]$. His Theorem 1 tells us that

$$
\widehat{\mathcal{R}}_{R}=\omega_{n} \widehat{\mathbb{R}}_{M L}+\left(1-\omega_{n}\right) I_{q}
$$

where $\widehat{\mathcal{R}}_{M L}=\phi\left(\widehat{\Sigma}_{M L}\right)$ is the corresponding maximum penalized likelihood estimator. The value of $\omega_{n}$ is picked through $K$-fold cross-validation with the normal likelihood as objective function. If $\widehat{\lambda}_{M L}$ is an eigenvalue of $\widehat{\mathcal{R}}_{M L}$, then $\omega_{n} \widehat{\lambda}_{M L}+1-\omega_{n}$ is an eigenvalue of $\widehat{\mathcal{R}}_{R}$, i.e., all eigenvalues smaller than one are expanded, and all eigenvalues larger than one are shrunk towards one (recall the discrepancy of biased eigenvalue dispersion of the non-regularized empirical covariance matrix), at a pace that increases as $\omega_{n}$ decreases. Furthermore, the value of $\omega_{n}$ tends to one in probability if $n \rightarrow \infty$, and there is zero probability that $\omega_{n}=1$ (no regularization) if $\widehat{\mathcal{R}}_{M L}$ does not have full rank, i.e., $\widehat{\mathcal{R}}_{R}$ is guaranteed to be non-singular, even if $q>n$ (see Theorem 2 and Theorem 3 in [50]). In our Gaussian copula context, we suggest the estimator

$$
\widehat{\mathcal{R}}_{R, n}=\omega_{n} \widehat{R}_{n}+\left(1-\omega_{n}\right) I_{q}
$$

and the same $K$-fold cross-validation procedure for selecting $\omega_{n}$, but now based on an estimated Gaussian sample. Heuristically (we do not go into detail here), the asymptotic properties of $\widehat{\mathbb{R}}_{R}$ carry over to $\widehat{\mathcal{R}}_{R, n}$, since we know that (see, e.g., the proof of Theorem 1) $\left\|\widehat{\mathcal{R}}_{M L}-\widehat{R}_{n}\right\|_{\infty}=O_{p}\left(n^{-1 / 2}\right)$ for $n \rightarrow \infty$.

## Regularized estimation and sparsity

Concentrating on the fully Gaussian setting, the general penalization criterion $P_{L T}\left(\Sigma, \omega_{n}\right)=\sum_{i, j, m, t} p_{\omega_{n}}\left(\Delta_{i j, m t} \mid \sigma_{i j, m t}\right)$ is considered in [29]. Typically, one takes $\Delta_{i j, m t}=0$ if $(i, j)=(m, t)$ and 1 otherwise in order to avoid penalization of the diagonal elements, which do not vanish. Another possibility is $\Delta_{i j, m t}=\left|\widehat{\sigma}_{i j, m t}\right|^{-1} \mathbb{1}\left(\left|\widehat{\rho}_{i j, m t}\right|<\rho_{n}\right)$, where $\widehat{\sigma}_{i j, m t}$ is a preliminary estimate for $\sigma_{i j, m t}$ with corresponding correlation $\widehat{\rho}_{i j, m t}$ and $0<\rho_{n}<1$ a certain threshold value,



i.e., we only shrink those elements that have a sufficiently small preliminary estimated correlation, and the amount of shrinkage is proportional to the size of the preliminary estimated covariance. This is an idea similar to the adaptive lasso of [13] and used in, e.g., [16]. A similar problem often arises when estimation of the precision matrix (inverse covariance matrix) is of interest, think of graphical models for example (see, e.g., [29] for some specific references). It is usually solved by first performing a local linear approximation to the penalty function (see, e.g., [52] in case of a precision matrix):

$$
p_{\omega_{n}}\left(\Delta_{i j, m t} \mid \sigma_{i j, m t}\right) \approx p_{\omega_{n}}\left(\Delta_{i j, m t} \mid \widehat{\sigma}_{i j, m t}^{(w)}\right)+\Delta_{i j, m t} p_{\omega_{n}}^{\prime}\left(\Delta_{i j, m t} \mid \widehat{\sigma}_{i j, m t}^{(w)}\right)\left(\left|\sigma_{i j, m t}\right|-\left|\widehat{\sigma}_{i j, m t}^{(w)}\right|\right)
$$

with $\widehat{\sigma}_{i j, m t}^{(w)}$ a current estimated entry of $\Sigma$ in step $w$. Hence, $\widehat{\Sigma}_{L T}^{(w+1)}$ should be taken as (typically, one iteration already suffices for satisfactory results)

$$
\widehat{\Sigma}_{L T}^{(w+1)} \in \arg \min _{\Sigma}\left\{\ln |\Sigma|+\operatorname{tr}\left(\Sigma^{-1} \widehat{\Sigma}_{M L}\right)+\sum_{i, m, j, t} \Delta_{i j, m t} p_{\omega_{n}}^{\prime}\left(\Delta_{i j, m t} \mid \widehat{\sigma}_{i j, m t}^{(w)}\right)\left|\sigma_{i j, m t}\right|\right\}
$$

which is a weighted covariance graphical lasso problem with weights

$$
\widetilde{\Delta}_{i j, m t}=\Delta_{i j, m t} p_{\omega_{n}}^{\prime}\left(\Delta_{i j, m t} \mid \widehat{\sigma}_{i j, m t}^{(w)}\right)
$$

We can summarize the $\widetilde{\Delta}_{i j, m t}$ values in a block matrix $\widetilde{\Delta}$ (again similar as in (10)), allowing us to rewrite (24) as

$$
\widehat{\Sigma}_{L T}^{(w+1)} \in \arg \min _{\Sigma}\left\{\ln |\Sigma|+\operatorname{tr}\left(\Sigma^{-1} \widehat{\Sigma}_{M L}\right)+\left|\widetilde{\Delta} * \Sigma\right|_{1}\right\}
$$

where $\|A\|_{1}=\|\operatorname{vec}(A)\|_{1}=\sum_{i j}\left|A_{i j}\right|$ is the $\mathcal{L}_{1}$-norm of the vector of all elements contained in $A$, and $*$ stands for elementwise multiplication. As illustrated in [4], the optimization (25) consists of a convex part $\operatorname{tr}\left(\Sigma^{-1} \widehat{\Sigma}_{M L}\right)+\|\widetilde{\Delta} * \Sigma\|_{1}$, and a concave part $\ln |\Sigma|$, making the entire problem non-convex (big difference with the precision matrix case, where graphical lasso is convex), i.e., convergence to a global minimum is not guaranteed. Also, when $q>n$, the solution to (25) will be degenerate because $\widehat{\Sigma}_{M L}$ is not full rank. The authors of [4] suggest to use $\widehat{\Sigma}_{M L}+\delta I_{q}$ for some $\delta>0$ in such cases, where $\delta$ is chosen such that, e.g., the resulting matrix has condition number equal to $q$. Still, they encounter difficulties of estimation when $q>n$. For this reason, we restrict ourselves to $q \leq n$ in the simulations.

Using a majorize approach, they propose in [4] to solve convex approximations to the original problem in an iterative way. Next to sparsity, their algorithm achieves positive definiteness. Another optimization technique for solving (25) is developed in [49], who uses coordinate descent, resulting in a faster and more stable algorithm. We use this algorithm as it is implemented in [16].

Under a set of typical assumptions, consistency and sparsistency results for the estimator $\widehat{\Sigma}_{L T}$ are given in [29]. One of their main conclusions is the preference for non-convex penalty functions such as the scad penalty of [14]:

$$
p_{\omega_{n}}^{\operatorname{scadt}}(t)= \begin{cases}\omega_{n} t & \text { for } t \leq \omega_{n} \\ \frac{1}{2(a-1)}\left(2 a \omega_{n} t-t^{2}-\omega_{n}^{2}\right) & \text { for } \omega_{n}<t \leq a \omega_{n} \\ (a+1) \omega_{n}^{2} / 2 & \text { for } t>a \omega_{n}\end{cases}
$$

where $a>2$. We take $a=3.7$ because of the arguments given in [14]. Such penalties shrink less entries that are large in magnitude, and as such reduce the bias. Moreover, a strong theoretical upper bound on the tuning parameter $\omega_{n}$, as is needed for, e.g., the lasso penalty $p_{\omega_{n}}^{\text {lasso }}(t)=\omega_{n} t$ (being the limit of $p_{\omega_{n}}^{\text {scad }}(t)$ for $a \rightarrow \infty$ ) in order to guarantee consistency, is not needed, yielding better sparsity properties. So, also in case of sparse covariance matrix estimation, the scad has the oracle property in the sense of [14] (zeroes are asymptotically estimated as zero, and estimated non-zeroes are asymptotically normal).

So far, we have been assuming a multivariate normal model, while the core of this paper is that we merely assume a semi-parametric normal copula model, i.e., within reach is the estimator $\widehat{\Sigma}_{L T, n}$, and not $\widehat{\Sigma}_{L T}$. As mentioned in [15], who use the term sparse M-estimator, "such estimation problems have benefited from a very limited attention so



far", and "the large sample analysis amply differs from the fully parametric viewpoint". Recall the sets $\mathcal{A}_{n}$ and $\mathcal{A}$ introduced for the property of sparsistency. Define also


where $d p_{\omega_{n}}\left(\left|\widehat{\sigma}_{n, \alpha}\right|\right) / d t$ denotes the derivative of $p_{\omega_{n}}(t)$ with respect to $t$, evaluated in $\left|\widehat{\sigma}_{n, \alpha}\right|$, and similarly for the second derivative. The sequence $a_{n}$ is related to the asymptotic bias of the penalized estimator, and equals $a_{n}=\omega_{n}$ for the lasso penalty. Theorem 2 states the consistency and sparsistency of the estimator $\widehat{\Sigma}_{L T, n}$.

Theorem 2. Assume that there exist $M, \widetilde{M}>0$ such that

$$
\left|\frac{d^{2} p_{\omega_{n}}}{d t^{2}}\left(t_{1}\right)-\frac{d^{2} p_{\omega_{n}}}{d t^{2}}\left(t_{2}\right)\right| \leq M\left|t_{1}-t_{2}\right|
$$

for any $t_{1}, t_{2} \in \mathbb{R}$ such that $t_{1}, t_{2}>\widetilde{M} \omega_{n}$. Suppose that for $a_{n}$ and $b_{n}$ defined in (26), it holds that $a_{n}, b_{n} \rightarrow 0$ when $n \rightarrow \infty$. Then, there exists a solution $\widehat{\boldsymbol{\Sigma}}_{L T, n}$ to (22) with penalty $P^{\bullet}=P_{L T}$, for each $n$, satisfying $\left|\widehat{\boldsymbol{\sigma}}_{n}-\boldsymbol{\sigma}\right|_{2}=O_{p}\left(\ln (\ln (n)) n^{-1 / 2}+a_{n}\right)$ for $n \rightarrow \infty$, where $\widehat{\boldsymbol{\sigma}}_{n}=\operatorname{vech}\left(\widehat{\boldsymbol{\Sigma}}_{L T, n}\right)$ and $\boldsymbol{\sigma}=\operatorname{vech}(\boldsymbol{\Sigma})$. If, in addition, $\omega_{n} \rightarrow 0$, $a_{n} \omega_{n}^{-1} \rightarrow 0, \sqrt{n} \omega_{n}(\ln (\ln (n)))^{-1} \rightarrow \infty$ when $n \rightarrow \infty$, and

$$
\liminf _{n \rightarrow \infty} \liminf _{t \rightarrow 0} \omega_{n}^{-1} \frac{d p_{\omega_{n}}}{d t}(|t|)>0
$$

it also holds that

$$
\lim _{n \rightarrow \infty} \mathcal{P}\left(\mathcal{A}_{n}=\mathcal{A}\right)=1
$$

Proof. This follows immediately from Theorem 3.1. and Theorem 3.2. in [15], noting that the necessary assumptions are satisfied, since they are verified for the Gaussian copula case and Gaussian likelihood loss function in Section E of the Appendix in [15].

The conditions (27) and (28) are satisfied by, e.g., the lasso and scad penalty. The condition in (27) is a smoothing condition on the penalty function, and (28) guarantees sparsity in the estimates. However, note that the condition $a_{n} \omega_{n}^{-1} \rightarrow 0$ for $n \rightarrow \infty$ cannot be fulfilled by the lasso since then $a_{n}=\omega_{n}$. Hence, Theorem 2 does not guarantee sparsistency of the lasso estimator.

# Regularized estimation and group sparsity 

Recall the second plot in Fig. 3 of Example 4, where entire groups of variables are independent of each other, and/or have no dependence within, resulting in a correlation sparsity pattern with entire zero blocks. A penalty of the form $P_{G L T}\left(\boldsymbol{\Sigma}, \omega_{n}\right)=2 \sum_{i, m=1, m>i}^{k} p_{\omega_{n}}\left(\sqrt{d_{i} d_{m}}\left\|\Sigma_{i m}\right\|_{F}\right)+\sum_{i=1}^{k} p_{\omega_{n}}\left(\sqrt{d_{i}}\left(d_{i}-1\right)\left\|\Delta_{i} * \Sigma_{i i}\right\|_{F}\right)$, where $\|\cdot\|_{F}$ is the Frobenius norm and $\Delta_{i} \in \mathbb{R}^{d_{i} \times d_{i}}$ a matrix with ones as off-diagonal elements and zeroes on the diagonal in order to avoid shrinkage of the variances, might lead to an estimator $\widehat{\boldsymbol{\Sigma}}_{G L T, n}$ that incorporates this sparsity structure. The non-differentiability of $\|\cdot\|_{F}$ at 0 allows to simultaneously shrink all entries of a certain block, and hence performs a group selection. For actually computing $\widehat{\boldsymbol{\Sigma}}_{G L T, n}$, a local linear approximation of $p_{\omega_{n}}$ can again be performed, which will boil down to a similar problem as finding $\widehat{\boldsymbol{\Sigma}}_{G L T, n}$ in case of the lasso penalty $p_{\omega_{n}}^{\text {lasso }}(t)=\omega_{n} t$. So, let us assume from now on that $p_{\omega_{n}}=p_{\omega_{n}}^{\text {lasso }}$. The ideas explained in [49], which we use for numerically finding $\widehat{\Sigma}_{L T, n}$, can in general not be used for finding $\widehat{\boldsymbol{\Sigma}}_{G L T, n}$, because some of the arguments do not apply to the Frobenius norm. Nevertheless, the problem

$$
\widehat{\boldsymbol{\Sigma}} \underset{G L T, n}{*}=\arg \min _{\boldsymbol{\Sigma}}\left\{\frac{1}{2}\left\|\boldsymbol{\Sigma}-\widehat{\boldsymbol{\Sigma}}_{n}\right\|_{F}^{2}+2 \omega_{n} \sum_{\substack{i, m=1 \\ m>i}}^{k} \sqrt{d_{i} d_{m}}\left\|\Sigma_{i m}\right\|_{F}+\omega_{n} \sum_{i=1}^{k} \sqrt{d_{i}\left(d_{i}-1\right)}\left\|\Delta_{i} * \Sigma_{i i}\right\|_{F}\right\}
$$



has a solution in the form of an elementwise soft thresholding operation. Denoting $\left(\widehat{\boldsymbol{\Sigma}}_{G L T, n}^{*}\right)_{i j, m t}$ for the $(j, t)^{\prime}$ th element of the $(i, m)^{\prime}$ th block of $\widehat{\boldsymbol{\Sigma}}_{G L T, n}^{*}$, similarly for $\widehat{\boldsymbol{\Sigma}}_{n}$, and further

$$
S_{i, m}=\sqrt{\sum_{j=1}^{d_{i}} \sum_{t=1}^{d_{m}}_{(i, j),(m, t)}\left\{\left(\widehat{\boldsymbol{\Sigma}}_{n}\right)_{i j, m t}\right\}^{2}}
$$

and

$$
\gamma_{i, m}= \begin{cases}\sqrt{d_{i} d_{m}} & \text { if } i \neq m \\ \sqrt{d_{i}\left(d_{i}-1\right)} & \text { if } i=m,\end{cases}
$$

it is known that (similar to, e.g., Proposition 1 in [6])

$$
\left(\widehat{\boldsymbol{\Sigma}}_{G L T, n}^{*}\right)_{i j, m t}= \begin{cases}0 & \text { if } S_{i, m} \leq \omega_{n} \gamma_{i, m} \text { and }(i, j) \neq(m, t) \\ \left(\widehat{\boldsymbol{\Sigma}}_{n}\right)_{i j, m t} & \text { if }(i, j)=(m, t) \\ \left(\widehat{\boldsymbol{\Sigma}}_{n}\right)_{i j, m t}\left(1-\frac{\omega_{n} \gamma_{i, m}}{S_{i, m}}\right) & \text { if } S_{i, m}>\omega_{n} \gamma_{i, m} \text { and }(i, j) \neq(m, t)\end{cases}
$$

Hence, we can numerically compute $\widehat{\boldsymbol{\Sigma}}_{G L T, n}$ by using ideas similar to the optimization approach of [4], i.e., by majorizing $\ln |\boldsymbol{\Sigma}|$ by its tangent plane and using generalized gradient descent steps, which comes down to iteratively solving (convex) problems of the form (29). For the actual implementation, we used to code available in [5], and fine-tuned it such that it can also cope with a group lasso penalty. Regarding the asymptotic properties, it is intuitively clear that a result similar to Theorem 2 will hold, with sparsistency formulated at the level of blocks instead of individual elements. For asymptotic properties in case of truly independent copies, we refer to Section 3 of [6].

# 4.2. Dimension depending on the sample size 

So far, we have been assuming that the total dimension $q$ of the random vector $\mathbf{X}$ remains fixed with $n$. When $\mathbf{X} \in \mathbb{R}^{q_{n}}$ for $q_{n}$ depending on $n$, of primary interest might be the behaviour of the empirical Gaussian copula covariance matrix $\widehat{\boldsymbol{R}}_{n}$ given in (10). Proposition 4 (see Appendix D for a proof) tells us how the dimension $q_{n}$ influences the consistency of the estimator $\widehat{\boldsymbol{R}}_{n}$ in max norm $\|\boldsymbol{A}\|_{\infty}=\max _{i, j}\left|A_{i j}\right|$.

Proposition 4. Let $q_{n}$ be a sequence of dimensions depending on $n$, and $\boldsymbol{R}_{n} \in \mathbb{R}^{q_{n} \times q_{n}}$ corresponding Gaussian copula covariance matrices. Assume that $\sup _{n} \lambda_{\max }\left(\boldsymbol{R}_{n}\right)<\infty$, where $\lambda_{\max }$ denotes the maximum eigenvalue, and let $\widehat{\boldsymbol{R}}_{n}$ be the estimator given in (10) with $q=q_{n}$. Then, it holds that

$$
\left\|\widehat{\boldsymbol{R}}_{n}-\boldsymbol{R}_{n}\right\|_{\infty}=O_{p}\left\{\left(\ln \left(q_{n}\right) / n\right)^{1 / 2}\right\}, \quad \text { for } n \rightarrow \infty
$$

So, Proposition 4 ensures that $\widehat{\boldsymbol{R}}_{n}$ is a consistent estimator as long as $\ln \left(q_{n}\right) / n \rightarrow 0$ as $n \rightarrow \infty$, i.e., as long as we are not in an ultra-high dimensional setting. In the context of the penalization techniques, one can also assume that $q=q_{n}$ depends on $n$. For the ridge regularization, this will lead to inconsistencies in high-dimensional settings, see Section 3.1 in [50] (basically because sample eigenvalues are known to be inconsistent when $q_{n} \rightarrow \infty$ ). Regarding the PLT penalties, Theorem H.1. in [15] states that

$$
\left\|\widehat{\sigma}_{n}-\sigma\right\|_{2}=O_{p}\left\{\sqrt{\widetilde{q}_{n}}\left(\ln (\ln (n)) n^{-1 / 2}+a_{n}\right)\right\}
$$

where $\widetilde{q}_{n}=q_{n}\left(q_{n}-1\right) / 2$, and under the additional conditions (next to those of Theorem 2) that $\widetilde{q}_{n}^{2} \ln (\ln (n)) n^{-1 / 2} \rightarrow 0$ and $\widetilde{q}_{n}^{2} a_{n} \rightarrow 0$ for $n \rightarrow \infty$. Hence, $q_{n}$ is allowed to increase with $n$, but consistency requires $\widetilde{q}_{n}=O\left(n^{1 / 4}\right)$. If, in addition (see Theorem H.2. in [15]), $\widetilde{q}_{n} a_{n} \omega_{n}^{-1}$ and $\sqrt{n} \omega_{n}\left(\widetilde{q}_{n} \ln (\ln (n))\right)^{-1} \rightarrow \infty$ for $n \rightarrow \infty$, true zeroes are asymptotically identified with probability one (but there might still be some false positives).

## 5. Simulation study

The aim of this section is to empirically study the finite sample performance of the (non-)regularized plug-in estimators for the Gaussian copula based dependence coefficients $\mathcal{D}_{1}$ and $\mathcal{D}_{2}$ discussed in Section 3. The finitesample distribution of the estimator of Section 3, is investigated in Section 5.1, and the regularized estimators are considered in Section 5.2.



# 5.1. Finite-sample performance of the estimator of Section 3 

Theorem 1 gives an asymptotic normality result with explicit asymptotic variance for the estimator $\widehat{D}_{r, n}=D_{r}\left(\widehat{R}_{n}\right)$ for $r \in\{1,2\}$, with $\widehat{R}_{n}$ the matrix of sample normal scores rank correlations given in (10). Let now $\widehat{\zeta}_{r, n}$ be the plug-in estimator of the asymptotic standard deviation $\zeta_{r}$ obtained by replacing $R$ with $\widehat{R}_{n}$. By simulating a sample from a certain multivariate distribution having a Gaussian copula, we can compute a realization of the actual sampling distribution of the studentized estimator $\sqrt{n}\left(\widehat{D}_{r, n}-D_{r}\right) / \widehat{\zeta}_{r, n}$, and several replications can be used to represent characteristics of the entire distribution, which should approximately (for large $n$ ) be a standard normal one according to Theorem 1. We consider four settings which we can generate samples from:



Fig. 4: Standard normal Q-Q plots for 1000 Monte Carlo runs of the studentized plug-in estimator for $D_{1}$ in four different settings with sample sizes $n=50,200,1000,5000$. The median ("Med") of the studentized estimates is given in blue.

- Setting 1: $k=2, d_{1}=d_{2}=2$, with standard normal marginals and a Gaussian copula having an autoregressive $\mathrm{AR}(1)$ correlation matrix with $\rho=0.25$ (i.e., the $(i, j)^{\prime}$ th element of $R$ equals $0.25^{|i-j|}$ ).
- Setting 2: as Setting 1, but now with marginals
- a $t$ distribution with 3 degrees of freedom for $X_{11}$
- an exponential distribution with mean 1 for $X_{12}$
- a beta distribution with parameters 2 and 2 for $X_{21}$
- an F-distribution with degrees of freedom 2 and 6 for $X_{22}$.
- Setting 3: similar to Setting 1, but with $\rho=0.8$.
- Setting 4: $k=5, d_{1}=4, d_{2}=5, d_{3}=3, d_{4}=1, d_{5}=2$, with standard normal marginals and a Gaussian copula having an equicorrelated correlation matrix with $\rho=0.5$.



Each time, we draw 1000 samples of sizes $n=50,200,1000,5000$ and make standard normal $Q$ - $Q$ plots to assess the goodness-of-fit with a standard normal distribution. See Fig. 4 for the results in case of $D_{1}$. Similar plots are obtained for $D_{2}$. In each setting, there is a qualitative fit with the standard normal distribution for larger sample sizes. Changing the marginals has no influence (Setting 1 versus Setting 2). Small correlations (Settings 1 and 2), yield a more pronounced lack-of-fit than higher correlations (Setting 3). Increasing the total dimension to 15 (Setting 4) results in a large positive bias for small sample sizes, calling for regularization techniques.

Next, in Fig. 2, asymptotic standard deviations $\zeta_{1}$ and $\zeta_{2}$ were shown in the context of Example 3. Generating $N$ samples from, e.g., a multivariate normal distribution with mean zero and covariance matrix given in (18), we obtain $N$ estimates $\widehat{D}_{r, n}^{(1)}, \ldots, \widehat{D}_{r, n}^{(N)}$, whose sample standard deviation multiplied with $\sqrt{n}$, say $\widehat{\zeta}_{r}$, can be seen as an approximation for $\zeta_{r}$ when $n$ is large. Fig. 5 depicts $\widehat{\zeta}_{r}$ for different values of $\rho_{1}$ and $\rho_{2}$ in case $n=10000$ and $N=1000$. We see the same patterns popping up as in Fig. 2, illustrating the asymptotic variance formula given in Theorem 1 empirically in this particular setting.



Fig. 5: Empirical standard deviation (sample size $N=1000$ ) $\widehat{\zeta}_{r}$ for $r \in\{1,2\}$ in the setting of Example 3 when $n=10000$.

# 5.2. Penalization techniques 

We now turn our attention to the different covariance matrix penalization techniques discussed in Section 4. We start with illustrating ridge regularization, in particular the improvements it gives in plug-in estimation of Gaussian copula based dependence coefficients between multiple random vectors. We do this for increasing values of $q$, possibly larger than $n$. Recall that the ridge estimator is rather easy to compute, and there are no additional difficulties when $q>n$. This study thus also allows for an impression on how the dependence coefficients behave with increasing $q$. Afterwards, we go to sparsity inducing (group)-lasso type methods, and investigate for two fixed values of $q$ and different sample sizes (with $q<n$ ) their ability of recovering marginal independencies (interpretability) on the one hand, and whether this improves the estimation of the dependence coefficients (accuracy) on the other hand.

## Ridge regularization

As explained in Section 4, the ridge estimator $\widehat{\mathbf{R}}_{R, n}$ of the Gaussian copula correlation matrix tries to cope with biased eigenvalue dispersion of the empirical correlation matrix which aggravates when $q$ is large compared to $n$. Moreover, it is easy to implement (with a straightforward cross-validation procedure for selecting the penalty parameter $\omega_{n}$ ), and guarantees a positive definite outcome. One can expect that the performance of the estimator $D_{r}\left(\widehat{\mathbf{R}}_{R, n}\right)$ is



better than the performance of $D_{r}\left(\widehat{R}_{n}\right)$ when $q$ is large compared to $n$. To demonstrate this, we consider the following two designs:

- Design 1: We let $q \in\{4,6,8, \ldots, 98\}$ and $k=q / 2$ with $d_{1}=d_{2}=\cdots=d_{k}=2$, e.g., if $q=30$, we are measuring the dependence between 15 random vectors of dimension 2
- Design 2: We let $q \in\{4,6,8, \ldots, 98\}$ and $k=2$ with $d_{1}=d_{2}=q / 2$, e.g., if $q=30$, we are measuring the dependence between 2 random vectors of dimension 15 .

In each design, we generate 1000 samples of sizes $n=50,100,500$ from a $N_{q}\left(\mathbf{0}_{q}, \boldsymbol{R}\right)$ distribution (but, assume unknown marginals), where $\boldsymbol{R}$ is the correlation matrix of an $\operatorname{AR}(1)$ process with $\rho=0.5$, and compute the empirical mean squared error of $D_{r}\left(\widehat{R}_{R, n}\right)$ and $D_{r}\left(\widehat{R}_{n}\right)$.



Fig. 6: Logarithm of the Monte Carlo mean squared error of the estimators $D_{\bullet}\left(\widehat{R}_{R, n}\right)$ (penalty) and $D_{\bullet}\left(\widehat{R}_{n}\right)$ (no penalty) for $D_{t \ln (t)}, D_{(\sqrt{t}-1)^{2}}, D_{1}$ and $D_{2}$, based on 1000 replications with sample sizes $n=50,100,500$ as a function of $q$, in two different designs.

The penalty parameter $\omega_{n}$ is determined by 5 -fold cross-validation (as described by equation (4) in [50]) on a grid of 50 equidistant elements in [0.01, 0.999]. In addition, we do the same for two Gaussian copula-based $\Phi$-dependence measures discussed in [12], known as the (normalized) mutual information and Hellinger distance, respectively given by

$$
D_{t \ln (t)}(\boldsymbol{R})=\left(1-\frac{|\boldsymbol{R}|}{\prod_{i=1}^{k}\left|\boldsymbol{R}_{i i}\right|}\right)^{1 / 2} \text {, and } D_{(\sqrt{t}-1)^{2}}(\boldsymbol{R})=1-\frac{2^{q / 2}|\boldsymbol{R}|^{1 / 4}\left|\boldsymbol{I}_{q}+\boldsymbol{R}_{0}^{-1} \boldsymbol{R}\right|^{1 / 2}}{\prod_{i=1}^{k}\left|\boldsymbol{R}_{i i}\right|^{1 / 4}}
$$

where $\boldsymbol{R}_{0}$ is given in (4), and $|\cdot|$ denotes the determinant. Note that the dependence coefficients in (30) depend on products of eigenvalues (they are based on divergences of copula densities), while $D_{1}$ and $D_{2}$ depend on sums of eigenvalues (arising from the Bures-Wasserstein distance).

Fig. 6 shows plots of the logarithm of the Monte Carlo mean squared error of $D_{\bullet}\left(\widehat{R}_{R, n}\right)$ (penalty) and $D_{\bullet}\left(\widehat{R}_{n}\right)$ (no penalty) for the four dependence measures for each sample size in both designs as a function of $q$. In all cases, we see vast improvements when using ridge regularization, especially when $n$ is small compared to $q$ (note that when $n=50$ and $q>50$, the estimators $D_{\bullet}\left(\widehat{R}_{n}\right)$ are not defined because of singularity of $\widehat{\boldsymbol{R}}_{n}$ ). Fig. 7 shows boxplots of the selected values for the penalization parameter $\omega_{n}$. We clearly see compatibility with the theoretical property that $\omega_{n}$ tends to one in probability when $n \rightarrow \infty$, and higher dimensions require a larger correction of the eigenvalue dispersion, i.e., a smaller $\omega_{n}$.





Fig. 7: Boxplots of selected penalty parameter $\omega_{n}$ via a 5 -fold cross-validation search on a grid of 50 equidistant elements in $[0.01,0.999]$, for different values of $n$ and $q$.

Finally, Fig. 6 also indicates that it would be interesting to study the behaviour of the dependence coefficients when $q \rightarrow \infty$, which can happen in multiple ways. In the first design for example, $d_{i}$ remains fixed for all $i=$ $1, \ldots, k$, but $k \rightarrow \infty$. Because $\Phi$-dependence measures satisfy Axiom (A4) of Appendix A (see, e.g., [12]), we know that $D_{t \ln (t)}, D_{(\sqrt{t}-1)^{2}} \rightarrow 1$ when $k \rightarrow \infty$, which is probably why the mean squared error of $\widehat{D}_{t \ln (t)}, \widehat{D}_{(\sqrt{t}-1)^{2}}$ first increases and afterwards decreases/becomes constant (in particular, the variance tends to 0 when $k \rightarrow \infty$, and the bias decreases/becomes constant, see Fig. S1 and S2 of the Supplementary Material for plots of the bias and variance). Regarding the optimal transport dependence measures $D_{1}$ and $D_{2}$, we expect them (based on our simulations) to converge to 0 when $k \rightarrow \infty$, probably because the strong normalization (denominator) grows faster than the numerator does. We see the variance of $\widehat{D}_{r}$ decreasing in $q$, and the biases increasing in $q$.

In the second design, $k=2$ remains fixed, but $d_{1}=d_{2} \rightarrow \infty$. The optimal transport measures seem (in our simulations) to converge to zero again, while the $\Phi$-dependence measures remain constant. We leave a formal study of the behaviour of these dependence coefficients when $q \rightarrow \infty$ for further research.

# (Adaptive/Group) lasso-type estimation 

Recall the two different sparsity patterns discussed in Example 4 for a $20 \times 20$ correlation matrix. By performing lasso-type estimation, we hope to recover zero entries (interpretability) on the one hand, and improve accuracy on the other hand. In particular, for the latter, we desire better performance of the plug-in estimator $\widehat{D}=D\left(\widehat{R}_{\bullet, n}\right)$ than of the non-penalized estimator $D\left(\widehat{R}_{n}\right)$, where $D$ is a certain correlation matrix based dependence coefficient.
For the simulation, we consider the following correlation structures

- Scenario 1: We take $q=20$ with $k=7, d_{1}=\cdots=d_{6}=3$ and $d_{7}=2$ having the non-block sparse correlation structure given in the left plot of Fig. 3, with $32.5 \%$ zeroes.



- Scenario 2: We take $q=20$ with $k=7, d_{1}=\cdots=d_{6}=3$ and $d_{7}=2$ such that $X_{1}, \ldots, X_{6}$ have independence within and between each other, but all components of $X_{7}$ are related and all dependent on all components of $X_{1}, \ldots, X_{6}$, i.e., the block sparse correlation structure of Example 4, right plot in Fig. 3, with $76.5 \%$ zeroes.
- Scenario 3: We take $q=70$ with $k=4, d_{1}=d_{2}=d_{3}=21$ and $d_{4}=7$ such that there is only dependence with and within $X_{4}$, yielding a block sparse correlation structure, with $79.7 \%$ zeroes.
Each time, we generate 1000 samples from a $\mathcal{N}_{q}\left(\mathbf{0}_{q}, R\right)$ distribution (marginals are again assumed to be unknown), and compute the no penalty, lasso, adaptive lasso (of [16] with $\omega_{n}=1$ and tuning parameter $\rho_{n}$ ), scad, and group lasso estimator for $R$. The considered sample sizes are $n=50,100,500$ for Scenarios 1 and 2, and $n=100,500$ for Scenario 3. Based on the 1000 replications, we report on the average true positive rate (TPR), which we want to be close to one, and false positive rate (FPR), which we want to be close to zero. We also compute the empirical root mean squared error of $\|\widehat{R}-R\|_{F} / q$ (where $\widehat{R}$ is the estimated correlation matrix in question), and empirical mean squared error of $\widehat{D}$, with $D$ the mutual information $D_{t} \ln (t)$, Hellinger distance $D(\sqrt{t}-1)^{2}$, or one of the optimal transport dependence measures $D_{1}$ or $D_{2}$.

For tuning $\omega_{n}$ (or $\rho_{n}$ in case of the adaptive lasso), we use the BIC criterion (see, e.g., [17] for the case of a precision matrix in Gaussian graphical models):

$$
\operatorname{BIC}\left(\widehat{\Sigma}_{\omega_{n}}\right)=-n\left[\ln \left|\widehat{\Sigma}_{\omega_{n}}\right|+\operatorname{tr}\left(\widehat{\Sigma}_{\omega_{n}}^{-1} \widehat{\Sigma}_{n}\right)\right]-\ln (n) d f\left(\widehat{\Sigma}_{\omega_{n}}\right)
$$

where $\widehat{\Sigma}_{\omega_{n}}$ is the estimated candidate covariance matrix using the penalty parameter $\omega_{n}$. We want to maximize (31) in $\omega_{n}$. We do this over an equidistant grid of 50 values in $[0.01 ; 0.6]$. The number $d f\left(\widehat{\Sigma}_{\omega_{n}}\right)$ stands for the degrees of freedom, and is estimated for the (adaptive) lasso and scad by the number of non-zero entries in $\widehat{\Sigma}_{\omega_{n}}$, not taking the elements under the diagonal into account. For the group lasso, the degrees of freedom can be estimated in a similar spirit as equation (23) in [9]:

$$
\begin{aligned}
& \operatorname{df}\left(\widehat{\Sigma}_{\omega_{n}}\right)=\sum_{\substack{i, m=1 \\
m>i}}^{k} \mathbb{1}\left(\left|\widehat{\Sigma}_{\omega_{n}, i m}\right|_{F}>0\right)\left(1+\frac{\left|\widehat{\Sigma}_{\omega_{n}, i m}\right|_{F}}{\left|\widehat{\Sigma}_{n, i m}\right|_{F}}\left(d_{i} d_{m}-1\right)\right) \\
& +\sum_{i=1}^{k} \mathbb{1}\left(\left|\Delta_{i} * \widehat{\Sigma}_{\omega_{n}, i i}\right|_{F}>0\right)\left(1+\frac{\left|\Delta_{i} * \widehat{\Sigma}_{\omega_{n}, i i}\right|_{F}}{\left|\Delta_{i} * \widehat{\Sigma}_{n, i i}\right|_{F}}\binom{d_{i}\left(d_{i}-1\right)}{2}-1\right)+q,
\end{aligned}
$$

where $\widehat{\Sigma}_{\omega_{n}, i m}$ is the $(i, m)^{\prime}$ 'th block of $\widehat{\Sigma}_{\omega_{n}}$, similarly for $\widehat{\Sigma}_{n, i m}$, and $\Delta_{i i} \in \mathbb{R}^{d_{i} \times d_{i}}$ is a matrix with ones as off-diagonal elements and zeroes on the diagonal. The results are summarized in Table 1.

In Scenario 1 ( $q=20$, no block sparsity, $32.5 \%$ zeroes), there is no group sparsity, which results in low TPR (and also low FPR, since only few entries get shrunk to zero) for the group lasso estimator. The other penalization techniques are, as expected, preferred for recovering zeroes. Clearly, any type of considered penalization yields more accurate estimation of $R$ in Frobenius norm than in case no penalty is used. However, this does not necessarily imply better estimation of the dependence coefficients, especially for lasso and scad. For good estimation of these, it is important not to lose sight of the $67.5 \%$ non-zero entries, which is why the adaptive lasso performs really well. Note that the mutual information is estimated very well in the non-penalized case, but this is mainly due to the fact that the true value equals 0.994 , which is very close to one, being an effect of the dimension (recall also Fig. 6). All non-penalized mutual information estimates are close to one because of a relatively large $q$, yielding low estimation error.

In Scenario $2\left(q=20\right.$, block sparsity, $\left.76.5 \%\right.$ zeroes), all penalization techniques perform well in identifying zeroes. For obtaining both high TPR and low FPR, the group lasso performs slightly better than lasso and scad. Also, when the focus is on estimating $R$, penalization is clearly beneficial, and the group lasso outperforms the other techniques. Regarding the dependence coefficients, we see that, for the optimal transport measures, lasso and scad give improvement compared to using no penalty, especially for smaller sample sizes. The error of the $\Phi$-dependence



Table 1: True positive rate (TPR), false positive rate (FPR), and empirical mean squared error for the estimated correlation matrix and corresponding plug-in estimators of dependence coefficients based on 1000 replications in different scenarios, using different penalties.
Scenario $1(q=20$, no block sparsity, $32.5 \%$ zeroes)


Scenario $2(q=20$, block sparsity, $76.5 \%$ zeroes)




Scenario 3 ( $q=70$, block sparsity, $79.7 \%$ zeroes)


estimates is rather low in case no penalty is used, which is again an effect of the dimension. Aside from this, the group lasso or the adaptive lasso (especially for larger sample sizes) gives the lowest error.

In Scenario $3(q=70$, block sparsity, $79.7 \%$ zeroes), the group lasso is again desirable for exploiting the sparsity structure, and even achieves zero FPR. For accurate estimation of $\mathbf{R}$ in Frobenius norm, the group lasso also performs best. Most accurate estimation of dependence (except for the mutual information, where no penalty performs best because the true value is again very close to one) is obtained by the group lasso when $n=100$, and by the adaptive lasso when $n=500$ is large compared to $q$.

In conclusion, when the true correlation matrix is sparse, interpretability can be enhanced by using a penalty that is able to completely shrink entries to zero. The group lasso is preferred for obtaining both good TPR and FPR when this sparsity is at the block level (Scenarios 2 and 3 ), and also performs well in estimating dependence in such cases, particularly when $n$ is rather small. The true $\mathbf{R}$ is estimated more accurately (compared to using no penalty) in Frobenius norm when using any penalty and in any scenario, but this does not necessarily result in better estimation of dependence. Especially when there are still quite some non-zeroes (Scenario 1), but also when $n$ is rather large, adaptive lasso is recommended for good accuracy of the estimated dependence coefficients. The $\Phi$-dependence measures are estimated with rather low error when using no penalty, but this is because they attain their upper bound of 1 rather quickly when the dimension increases.

# 6. Real data applications 

In Section 6.1, we look into an application of optimal transport dependence measures between possibly more than two random vectors to sensory analysis. In Section 6.2, we illustrate how these measures, together with the considered penalization techniques, can be useful in finding clusters among speech signal attributes used for detecting Parkinson's disease.

### 6.1. Application to sensory analysis

Consider a caterer who wants to sell eight different smoothies, say $S_{1}, \ldots, S_{8}$, on an event, and is looking for three employees willing to take up this job. A total of 24 people, say $P_{1}, \ldots, P_{24}$, show up for this job opportunity, all equally qualified, and the caterer is looking for a fair way to pick three candidates. Every candidate is asked to taste each of the eight smoothies, and is given a sheet of paper in order to position the different smoothies, knowing that the closer certain smoothies are to each other, the more similar they are considered by the individual. For example, according to candidate $P_{j}$ in Fig. 8, the smoothies $S_{1}, S_{2}, S_{3}$ and $S_{4}$ are similar, but quite different from the similarly tasting smoothies $S_{5}, S_{6}$ and $S_{7}$, and none of them resembles $S_{8}$. As such, the caterer acquires 24 datasets, say





Fig. 8: Example of smoothie similarity rating by candidate $P_{j}$ on a sheet of paper and corresponding dataset $X_{j}$.
$X_{j} \in \mathbb{R}^{8 \times 2}$ for $j=1, \ldots, 24$, containing the smoothies as rows and the $X-Y$ coordinates on the sheet of paper for person $j$, denoted as a random vector $\left(X_{j}, Y_{j}\right)$, as columns, representing the smoothie similarities of each candidate. So, the dataset $X_{j}$ contains a sample from $\left(X_{j}, Y_{j}\right)$ of size eight, denoted as $\left(x_{i j}, y_{i j}\right)$ for $i=1, \ldots, 8$. The data is available in the R package SensoMineR ([30]). The criterion based on which three employees are picked consists of finding the three individuals that have the least similar spatial configurations, meaning three very diversified tastes (in the hope of not selling only a few smoothies because of prepossessed preferences by the sellers).

Typically, see, e.g., [32], the similarity between two configurations is measured by the RV coefficient

$$
\operatorname{RV}\left(X_{j_{1}}, X_{j_{2}}\right)=\frac{\operatorname{tr}\left(X_{j_{1}} X_{j_{1}}^{T} X_{j_{2}} X_{j_{2}}^{T}\right)}{\sqrt{\operatorname{tr}\left\{\left(X_{j_{1}} X_{j_{1}}^{T}\right)^{2}\right\} \operatorname{tr}\left\{\left(X_{j_{2}} X_{j_{2}}^{T}\right)^{2}\right\}}}
$$

and for three configurations one can take, e.g., the average of all pairwise RV coefficients. Yet, pairwise coefficients feel unnatural and it would be better to compute a trivariate vector similarity. Note that (32) is actually the RV coefficient between two random vectors $\left(X_{j_{1}}, Y_{j_{1}}\right)$ and $\left(X_{j_{2}}, Y_{j_{2}}\right)$ of size two having joint, empirical covariance matrix

$$
\left(\begin{array}{cc}
X_{j_{1}}^{T} X_{j_{1}} & X_{j_{1}}^{T} X_{j_{2}} \\
X_{j_{2}}^{T} X_{j_{1}} & X_{j_{2}}^{T} X_{j_{2}}
\end{array}\right) \in \mathbb{R}^{4 \times 4}
$$

and we get a similar (larger) block covariance matrix in $\mathbb{R}^{2 m \times 2 m}$ when taking $m$ individuals into account.
Since not restricted to two random vectors anymore, one can also opt for an (estimated) optimal transport dependence coefficient $\mathfrak{D}_{1}$ or $\mathfrak{D}_{2}$ between three vectors of size two for measuring the similarity between three individual spatial configurations. Note that the dispersion of the coordinates might differ among the individuals (some might use the entire sheet, while others only use the right corner), but since we use the normal scores rank correlations, we do not need any centering or scaling of the data. Pairwise scatterplots of the normal scores of the $X-Y$ coordinates of the 24 people are shown in Fig. S3 of the Supplementary Material, indicating that dependencies are mainly correlation based, i.e., a Gaussian copula model is suitable for modelling the dependencies. When zooming in on candidates $P_{12}, P_{13}, P_{18}$ and $P_{20}$, we get the pairwise scatterplots given in Fig. 9. From this, we expect for example that candidates $P_{12}$ and $P_{13}$ have quite independent smoothies preferences, while candidates $P_{18}$ and $P_{20}$ have rather strong correlations between their coordinates.

We denote $\widehat{\mathfrak{D}}_{r}\left(P_{j_{1}}, P_{j_{2}}\right)$ and $\widehat{\mathfrak{D}}_{r}\left(P_{j_{1}}, P_{j_{2}}, P_{j_{3}}\right)$ for the estimated similarity between two candidates $P_{j_{1}}, P_{j_{2}}$ or three candidates $P_{j_{1}}, P_{j_{2}}, P_{j_{3}}$ for $r=1,2$. Recall that these are actually dependencies between 2 and 3 random vectors of



Table 2: Arrangement of two and three candidates according to largest estimated similarity $\widehat{D}_{r}$ for $r=1,2$. The first two and last two are shown.

|  | two based on $\widehat{D}_{1}$ |  | two based on $\widehat{D}_{2}$ |  | three based on $\widehat{D}_{1}$ |  | three based on $\widehat{D}_{2}$ |  |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|  | $\widehat{D}_{1}(P 18, P 20$ ) | 0.561 | $\widehat{D}_{2}(P 18, P 20$ ) | 0.561 | $\widehat{D}_{1}(P 15, P 18, P 20)$ | 0.585 | $\widehat{D}_{2}(P 15, P 18, P 20$ ) | 0.595 |
|  | $\widehat{D}_{1}(P 9, \mathrm{P} 23)$ | 0.542 | $\widehat{D}_{2}(P 15, P 20)$ | 0.521 | $\widehat{D}_{1}(P 9, \mathrm{P} 10, \mathrm{P} 23)$ | 0.550 | $\widehat{D}_{2}(P 10, P 18, P 23)$ | 0.561 |
|  | $\widehat{D}_{1}(P 12, P 19)$ | 0.020 | $\widehat{D}_{2}(P 12, P 19)$ | 0.016 | $\widehat{D}_{1}(P 2, P 3, \mathrm{P} 14)$ | 0.080 | $\widehat{D}_{2}(P 2, P 12, P 19)$ | 0.075 |
|  | $\widehat{D}_{1}(P 12, P 13)$ | 0.015 | $\widehat{D}_{2}(P 12, P 13)$ | 0.013 | $\widehat{D}_{1}(P 12, P 13, P 21)$ | 0.069 | $\widehat{D}_{2}(P 12, P 13, P 21)$ | 0.074 |



Fig. 9: Pairwise scatterplots of normal scores of $X-Y$ coordinates of candidates P12, P13, P18 and P20 of the smoothies dataset.



Fig. 10: Boxplot of $p$-values of pairwise goodness-of-fit tests for Gaussian copula on 91 dysphonia measures of the LSVT dataset.
size 2 respectively, i.e., $q=4$ with $k=2, d_{1}=d_{2}=2$, or $q=6$ with $k=3, d_{1}=d_{2}=d_{3}=2$ respectively, estimated based on a sample of size $n=8$.
Table 2 shows the two strongest and two weakest couples or triplets according to $\widehat{D}_{1}$ or $\widehat{D}_{2}$. The caterer will definitely hire candidate P12, P13 and P21. In [32], they cluster the candidates using the clustatis method, bringing forward three classes of individuals, see their Fig. 5. We see that P12 belongs to class 2, while P13 belongs to class 3 and P21 to class 1, also indicating their diversified smoothie similarity pattern. The optimal transport dependence measures give an unequivocal ordering of patterns based on similarities that go beyond two random vectors.
Note that we can also switch the role of the smoothies and the individuals, i.e., construct 8 datasets in $\mathbb{R}^{24 \times 2}$, and similarly look at the dependence between smoothies. Doing so, both $\widehat{D}_{1}(=0.0336)$ and $\widehat{D}_{2}(=0.0340)$ agree that $\& 6, \& 7$ and $\& 8$ are the least similar among all possible triplets. They are respectively called Casino PBC, Innocent SB and Carrefour SB, and the biplots (based on various sensometrics methods) in Fig. 2. of [32] indeed also reveal angels between these smoothies that are close to $90^{\circ}$. So, $S 6, S 7$ and $S 8$ would be a good choice if the caterer wanted to limit his smoothie supply to three flavours that still have a satisfactory amount of diversity.

# 6.2. Clustering dysphonia measures 

In a second real data application, we study the LSVT voice rehabilitation dataset of [47], freely accessible at the UCI Machine Learning Repository (https://archive.ics.uci.edu/dataset/282/lsvt+voice+rehabilit



ation). Parkinson's disease frequently leads to vocal impairment, the extent of which can be assessed using sustained vowel phonations. In particular, the sustained vowel "ahh..." (denoted as /a/) is typically studied. Next, dysphonia measures are used to extract clinically useful information from speech signals. The dataset consists of $q=310$ such measurements on $n=126$ phonations. As mentioned in Section C of [47], several of these dysphonia measures are similar (algorithmic variations of the same basic ideas), e.g., there are many jitter (a measure of cycle-to-cycle variation in frequency) and shimmer (a measure of cycle-to-cycle variation in amplitude) variants. Hence, there is a large amount of redundancy among the attributes, which could worsen the performance of supervised learning (like, e.g., a classifier as studied in [47]), and some kind of preliminary feature selection is recommended.

There are indeed many dysphonia measures that exhibit a (very) strong sample normal scores rank correlation, see Fig. S4 of the Supplementary Material. In order to eliminate strong detrimental redundancies (that closely approach singularity), we iteratively search (pairwise) for attributes that have a normal scores rank correlation larger than 0.8 in absolute value, and each time discard one of them. Remaining are 91 dysphonia measures, whose (non-singular) sample normal scores rank correlation matrix is given in the left panel of Fig. S5 of the Supplementary Material.

For testing the adequacy of a Gaussian copula for modelling (at least pairwise) dependencies, we consider the test based on the statistic $S_{n}$ given in equation (2) of [21], where we test the null hypothesis that the copula between a pair of dysphonia measures is Gaussian, and compute the $p$-value based on 1000 bootstrap samples. In Fig. 10, a boxplot of $p$-values of pairwise (that is between all $91 \cdot 90 / 2=4095$ pairs of variables) goodness-of-fit tests is shown. Based on the boxplot, we see that is it reasonable to assume (at least pairwise) Gaussian dependencies.

We still have quite a large amount of attributes compared to the sample size of $n=126$, and we still see some quite large correlations between several first and last dysphonia measures (right upper corner of left panel in Fig. S5), so further feature selection is desired. With this objective in mind, we decide to cluster the remaining 91 attributes in order to get an idea about how they can be divided into properly separated groups that have rather strong similarity within.



Fig. 11: Dendrogram (left) and redundancy (right) for the clustering of 91 dysphonia measures.

In particular, we opt for agglomerative hierarchical variable clustering based on similarity measures (see, e.g., [19] and references within for a survey), where the main task is to measure the similarity, say $D\left(\mathcal{X}_{1}, \mathcal{X}_{2}\right)$ (or alternatively dissimilarity), between two groups of variables $\mathcal{X}_{1}$ and $\mathcal{X}_{2}$. Denote $\mathcal{X}_{1}, \ldots, \mathcal{X}_{91}$ for the 91 dysphonia measures, which are initially considered to be clusters on their own. In the first step, the two variables $\mathcal{X}_{i}$ and $\mathcal{X}_{j}$ (for certain $i, j \in$ $\{1, \ldots, 91\}$ with $i \neq j$ ) that exhibit the largest similarity according to $D\left(\left\{\mathcal{X}_{i}\right\},\left\{\mathcal{X}_{j}\right\}\right)$, i.e., taking $\mathcal{X}_{1}=\left\{\mathcal{X}_{i}\right\}$ and $\mathcal{X}_{2}=\left\{\mathcal{X}_{j}\right\}$, are merged together forming one single cluster. Next, all similarities between the current clusters are again computed, and the two clusters showing the largest similarity are merged. One keeps repeating this until only one big cluster (composed of all the 91 attributes) remains, yielding a total of 91 partitions of the attribute space. In general, the main task is thus to compute (for $\mathcal{X}_{1}=\left\{\mathcal{X}_{i_{1}}, \ldots, \mathcal{X}_{i_{m}}\right\}$ and $\mathcal{X}_{2}=\left\{\mathcal{X}_{j_{1}}, \ldots, \mathcal{X}_{j_{r}}\right\}$ )

$$
D\left(\mathcal{X}_{1}, \mathcal{X}_{2}\right)=D\left(\left\{\mathcal{X}_{i_{1}}, \ldots, \mathcal{X}_{i_{m}}\right\},\left\{\mathcal{X}_{j_{1}}, \ldots, \mathcal{X}_{j_{r}}\right\}\right)
$$



for certain mutually exclusive $i_{1}, \ldots, i_{m}, j_{1}, \ldots, j_{r} \in\{1, \ldots, 91\}$. Typically, one specifies a certain (estimated) bivariate dependence coefficient and a certain link function (overlooking multivariate dependence structures) for computing (33), or (estimated) multivariate concordance measures (between univariate random variables) have also been studied (see, e.g., [19]). We decide to take $\widehat{D}_{1}\left(\left(X_{i_{1}}, \ldots, X_{i_{m}}\right),\left(X_{j_{1}}, \ldots, X_{j_{r}}\right)\right)$ for (33), and as such measure the similarity between clusters (in spite of possible similarity within), which feels more natural and does not require a link function. This $\widehat{D}_{1}$ is taken to be $D_{1}(\widehat{\mathbf{R}} R, n)$, where $\widehat{\mathbf{R}} R, n$ is the ridge penalized estimated Gaussian copula correlation matrix (23), keeping in mind that the total dimension $m+r$ in (33) might be large compared to $n$. The tuning parameter $\omega_{n}$ is again determined by a 5 -fold cross-validation search on a grid of 50 equidistant elements in $[0.01,0.999]$.

We obtain 91 partitions, and one of these should be picked as preferable clustering of the attributes. Since not restricted to two groups, we can also use $\widehat{D}_{1}$ for measuring the similarity $D\left(X_{1}, \ldots, X_{k}\right)$ between $k$ clusters $X_{1}, \ldots, X_{k}$ comprising a specific partition. This in fact measures how separated the obtained clusters of that particular partition are, i.e., it is a measure of redundancy among the clusters of attributes, which we want to be rather small. The dendrogram of the clustering procedure and redundancy $D\left(X_{1}, \ldots, X_{k}\right)$ as a function of the number of clusters $k$ (for each of the 91 obtained partitions) are shown in Fig. 11. Based on this, we decide to look deeper into the 36 cluster partition (where the dotted line cuts the dendrogram), since the redundancy is minimal here (in particular, $D\left(X_{1}, \ldots, X_{36}\right)=0.07265)$. Next, we rearrange the attributes such that dysphonia measures that belong to the same cluster follow each other in the dataset, and the cluster dimensions are

$$
\left(d_{1}, \ldots, d_{36}\right)=(1,1,53,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,1,1,1)
$$

i.e., there is a big cluster of size 53 , two smaller clusters of size 2 and 3 , and 33 clusters of size 1. The sample normal scores rank correlation matrix after rearrangement, estimated without a penalty and with a ridge penalty are respectively given in the middle and right panel of Fig. S5 in the Supplementary Material.

Denote now the 36 clusters as random vectors $\mathbf{X}_{1}, \ldots, \mathbf{X}_{36}$. We already know that $\widehat{D}_{1}\left(\mathbf{X}_{1}, \ldots, \mathbf{X}_{36}\right)=0.07265$ when using ridge penalization $\left(\omega_{n}=0.696\right)$, which is already way closer to 0 than when using no penalization (then $\widehat{D}_{1}\left(\mathbf{X}_{1}, \ldots, \mathbf{X}_{36}\right)=0.19013$ ). Moreover, the rationale behind variable clustering is that clusters are truly separated, i.e., there is (block) sparsity in the Gaussian copula correlation matrix at levels corresponding to attributes belonging to different clusters. Therefore, we also consider lasso, adaptive lasso, and group lasso estimation of the Gaussian



Fig. 12: Sparsity patterns of estimated Gaussian copula correlation matrix of 91 dysphonia measures using different penalties.
copula correlation matrix. For the lasso and group lasso, we search for an optimal $\omega_{n}$ on an equidistant grid of 50 values in $[0.01 ; 0.8]$, and for the adaptive lasso, we search for an optimal $\rho_{n}$ on an equidistant grid of 50 values in [0.01;0.6], each time aiming to maximize the BIC (31).

The first panel in Fig. 12 shows the sparse structure of the estimated normal scores rank correlation matrix of the 91 clustered attributes when using the lasso. To a certain extent, we recognize the diagonal blocks corresponding to the within cluster correlations, and observe many zeroes between attributes belonging to different clusters. The estimated inter-cluster dependence equals $\widehat{D}_{1}\left(X_{1}, \ldots, X_{36}\right)=0.0014$. Using the adaptive lasso (second panel), we get $\widehat{D}_{1}\left(\mathbf{X}_{1}, \ldots, \mathbf{X}_{36}\right)=0.0141$, and a group lasso estimator (third panel) results in $\widehat{D}_{1}\left(\mathbf{X}_{1}, \ldots, \mathbf{X}_{36}\right)=0.0130$. Note that the group lasso estimator did not shrink any of the diagonal blocks, reflecting the stronger intra-cluster similarities.



In the fourth panel of Fig. 12, we visualize a group lasso estimate with a larger penalty parameter (not determined through BIC). When forcing more sparsity by increasing $\omega_{n}$, we see more off-diagonal blocks (and not diagonal blocks) getting shrunk, and this leads to $\widehat{D}_{1}\left(X^{1}, \ldots, X^{36}\right)=0.0001$. More detailed images are given in Fig. S6 of the Supplementary Material.

Further feature selection can now be done via replacing each cluster by a single (or maybe multiple) attribute that represents the cluster well (e.g., the attribute within the cluster that has largest similarity with the cluster).

# 7. Discussion 

In this paper, we proposed to use the 2-Wasserstein distance between the joint copula measure and the product of the marginal copula measures for quantifying dependence between a finite, arbitrary amount of random vectors. The obtained dependence coefficients satisfy several desirable properties and especially have the powerful theoretical quality of detecting any departure from independence. Examples illustrate that the choice of normalization strongly influences the overall dependence quantification. Whether or not one can explicitly calculate the infimum for the optimal transport map and/or the supremum required for the normalization, depends on the specific form of the copula, and a great deal of interesting work remains to be done (also when no explicit copula can be assumed, i.e., when nonparametric estimators need to be considered).

A Gaussian copula approach yields explicit formulas with a clear interpretation. Using the sample matrix of normal scores rank correlation coefficients results in an easily computable plug-in estimator for which we obtained an asymptotic normality result with explicit asymptotic variance in arbitrary dimensions. Expectedly, higher dimensions aggravate the finite sample estimation performance. To cope with this, we studied rank-invariant penalization techniques for estimating the Gaussian copula correlation matrix, leading to estimators that are able to improve accuracy on the one hand, and enhance interpretability by detecting marginal independencies on the other hand. Such estimation challenges have enjoyed rather little attention, and further research would definitely be worthwhile.

Another interesting theoretical challenge is to study the optimal transport (and others as well) dependence coefficients when the dimension grows unboundedly. In the Gaussian copula context, random matrix theory could definitely be useful, and, as also touched upon in our simulations, various behaviours can be expected depending on the nature of the dependence measure, the normalization, whether letting $d_{i} \rightarrow \infty$ for some $i$, or $k \rightarrow \infty$. Keeping the dimension fixed, our simulations illustrated the asymptotic normality result and the benefits of using penalization techniques when the sample size is rather small and/or when (group) sparsity is pursued.

Finally, in a first real data application, we illustrated the use of the dependence coefficients in evaluating and comparing (possibly more than two) consumer products or similarities in sensory analysis. Alongside, on a second real dataset containing expressions on sustained vowel phonations, we demonstrated how attributes can be hierarchically clustered via multivariate similarities between random vectors (despite similarities within), disposing of traditional link functions. Ridge penalization is preferred when the number of attributes is large compared to the sample size, and (group)-lasso type penalties can be used to reflect the homogeneity and separation of a partition of, in general $k$, groups of variables.

Acknowledgments. The authors thank Dr Gilles Mordant, Georg-August-Universität Göttingen, for scientific discussions during the startup phase of this research. The authors gratefully acknowledge support from the Research Fund KU Leuven [C16/20/002 project].



# Appendix A. Axioms for dependence measures between random vectors 

In [11], a list of axioms is stated for a dependence measure $D_{d_{1}, \ldots, d_{k}}(\mathbf{X})=D\left(X_{1}, \ldots, X_{k}\right)$. Up to some minor differences (small corrections and simplifications), the axioms are given as follows.
(A1) For every permutation $\{\pi(1), \ldots, \pi(k)\}$ of $\{1, \ldots, k\}: D_{d_{1}, \ldots, d_{k}}(\mathbf{X})=D\left(X_{\pi(1)}, \ldots, X_{\pi(k)}\right)$ : and for every permutation $\left\{\pi_{i}(1), \ldots, \pi_{i}\left(d_{i}\right)\right\}$ of $\left\{1, \ldots, d_{i}\right\}, i \in\{1, \ldots, k\}: D_{d_{1}, \ldots, d_{k}}(\mathbf{X})=D\left(X_{1}, \ldots,\left(X_{i \pi_{i}(1)}, \ldots, X_{i \pi_{i}\left(d_{i}\right)}\right), \ldots, X_{k}\right)$.
(A2) $0 \leq D_{d_{1}, \ldots, d_{k}}(\mathbf{X}) \leq 1$.
(A3) $D_{d_{1}, \ldots, d_{k}}(\mathbf{X})=0$ if and only if $X_{1}, \ldots, X_{k}$ are mutually independent.
(A4) $D\left(X_{1}, \ldots, X_{k}, X_{k+1}\right) \geq D\left(X_{1}, \ldots, X_{k}\right)$ with equality if and only if $X_{k+1}$ is independent of $\left(X_{1}, \ldots, X_{k}\right)$.
(A5) $D_{d_{1}, \ldots, d_{k}}(\mathbf{X})$ is well-defined for any $q$-dimensional random vector $\mathbf{X}$ (even if there is a singular part in the distribution of $\mathbf{X}$ ).
(A6) $D_{d_{1}, \ldots, d_{k}}(\mathbf{X})$ is a function of solely the copula $C$ of $\mathbf{X}$ (which is equivalent to $D_{d_{1}, \ldots, d_{k}}(\mathbf{X})$ being invariant under strictly increasing transformations of any of the components of $\mathbf{X}$ ).
(A7) Let $T_{i j}$ be a strictly decreasing, continuous transformation for a fixed $i \in\{1, \ldots, k\}$ and a fixed $j \in\left\{1, \ldots, d_{i}\right\}$.
Then

$$
D\left(X_{1}, \ldots, T_{i}\left(X_{i}\right), \ldots, X_{k}\right)=D\left(X_{1}, \ldots, X_{k}\right),
$$

where $T_{i}\left(X_{i}\right)=\left(X_{i 1}, \ldots, T_{i j}\left(X_{i j}\right), \ldots, X_{i d_{i}}\right)$.
(A8) Let $\left(X_{n}\right)_{n \in \mathbb{N}}$ be a sequence of $q$-dimensional random vectors with corresponding copulas $\left(C_{n}\right)_{n \in \mathbb{N}}$, then

$$
\lim _{n \rightarrow \infty} D_{d_{1}, \ldots, d_{k}}\left(\mathbf{X}_{n}\right)=D_{d_{1}, \ldots, d_{k}}(\mathbf{X})
$$

if $C_{n} \rightarrow C$ uniformly, where $C$ denotes the copula of $\mathbf{X}$.

## Appendix B. Proofs of theoretical results of Section 2

## Appendix B.1. Proof of Lemma 1

For (a), let $\mathbf{V}=\left(V_{1}, \ldots, V_{k}\right)$ with $V_{i}=\left(V_{i 1}, \ldots, V_{i d_{i}}\right)$ be a random vector with distribution $\nu_{1} \times \cdots \times \nu_{k}$ and let $\mathbf{U}=\left(U_{1}, \ldots, U_{k}\right)$ with $U_{i}=\left(U_{i 1}, \ldots, U_{i d_{i}}\right)$ be a random vector with distribution $\mu_{C}$, as marginal distribution of an arbitrary coupling $\gamma \in \Gamma\left(\mu_{C}, \nu_{1} \times \cdots \times \nu_{k}\right)$ of $(\mathbf{U}, \mathbf{V})$, and having marginals $\mu_{C_{1}}, \ldots, \mu_{C_{k}}$ itself. Then, the distribution of $\left(U_{i}, V_{i}\right)$ is a coupling of $\mu_{C_{i}}$ and $\nu_{i}$ for all $i=1, \ldots, k$ such that

$$
\mathbb{E}\left(\|\mathbf{U}-\mathbf{V}\|^{2}\right)=\mathbb{E}\left(\sum_{i=1}^{k} \sum_{j=1}^{d_{i}}\left(U_{i j}-V_{i j}\right)^{2}\right)=\sum_{i=1}^{k} \mathbb{E}\left(\left\|U_{i}-V_{i}\right\|^{2}\right) \geq \sum_{i=1}^{k} \mathbf{W}_{2}^{2}\left(\mu_{C_{i}}, \nu_{i}\right)
$$

Taking the infimum over all couplings $\gamma \in \Gamma\left(\mu_{C}, \nu_{1} \times \cdots \times \nu_{k}\right)$ yields the result. Part (b) follows immediately from the definition.

Regarding (c), if $\mu_{C_{i}}=\nu_{i}$ for all $i=1, \ldots, k$, we have $T_{d_{1}, \ldots, d_{k}}\left(\mu_{C} ; \nu_{1}, \ldots, \nu_{k}\right)=\mathbf{W}_{2}^{2}\left(\mu_{C}, \mu_{C_{1}} \times \cdots \times \mu_{C_{k}}\right)$, making the statement trivial since $\mathbf{W}_{2}$ defines a metric. Suppose now that $\nu_{i}$ is absolutely continuous for all $i=1, \ldots, k$ and $\mathbf{T}_{d_{1}, \ldots, d_{k}}\left(\mu_{C} ; \nu_{1}, \ldots, \nu_{k}\right)=0$. The latter means that, working further on the proof of (a), there exists a $\gamma \in \Gamma\left(\mu_{C}, \nu_{1} \times\right.$ $\left.\cdots \times \nu_{k}\right)$ minimizing the left-hand side of (B.1), and with equality instead of inequality. Hence, the 2-Wasserstein distance between $\mu_{C_{i}}$ and $\nu_{i}$ is obtained at the coupling distribution of $\left(U_{i}, V_{i}\right)$ coming from $\gamma$, for all $i=1, \ldots, k$. However, Brenier's theorem (see, e.g., Theorem 2.12 in [48]) tells us that, since $\nu_{i}$ is absolutely continuous, this optimum is uniquely and deterministically attained, i.e., (denoting $\nabla$ for the gradient) there must exist convex functions $\psi_{i}: \mathbb{I}^{d_{i}} \rightarrow \mathbb{R} \cup\{\infty\}$ such that $U_{i}=\nabla \psi_{i}\left(V_{i}\right)$ almost surely for all $i=1, \ldots, k$. Since $V_{1}, \ldots, V_{k}$ are independent, this implies that $U_{1}, \ldots, U_{k}$ are independent and thus $\mu_{C}=\mu_{C_{1}} \times \cdots \times \mu_{C_{k}}$.

We next prove statement (d). The $\mathbf{W}_{2}$-compactness of $\Gamma\left(\mu_{C_{1}}, \ldots, \mu_{C_{k}}\right)$ follows from the well-known result that if $\left(\gamma_{n}\right)_{n} \

Take an arbitrary $\widetilde{\pi} \in \Gamma\left(\mu^{C_{1}}, \ldots, \mu^{C_{k}}\right)$ such that $\mathbf{W}_{2}(\pi, \widetilde{\pi})<\delta$, where we pick $\delta>0$ such that $\delta<\min \left\{1, \epsilon /\left(1+2 D_{\pi}\right)\right\}$ with $D_{\pi}=\mathbf{W}_{2}\left(\pi ; \nu_{1} \times \cdots \times \nu_{k}\right)$. We also denote $D_{\widetilde{\pi}}=\mathbf{W}_{2}\left(\widetilde{\pi} ; \nu_{1} \times \cdots \times \nu_{k}\right)$. It holds that

$$
\begin{aligned}
\mid T_{d_{1}, \ldots, d_{k}}\left(\pi ; \nu_{1}, \ldots, \nu_{k}\right) & -T_{d_{1}, \ldots, d_{k}}\left(\widetilde{\pi} ; \nu_{1}, \ldots, \nu_{k}\right) \mid=\left|D_{\pi}^{2}-D_{\widetilde{\pi}}^{2}\right|=\left|D_{\widetilde{\pi}}-D_{\pi}\right| \cdot\left|D_{\widetilde{\pi}}-D_{\pi}+2 D_{\pi}\right| \\
& \leq\left|D_{\widetilde{\pi}}-D_{\pi}\right|\left(\left|D_{\widetilde{\pi}}-D_{\pi}\right|+2 D_{\pi}\right) \\
& <\epsilon
\end{aligned}
$$

where we used that $\left|D_{\widetilde{\pi}}-D_{\pi}\right| \leq \mathbf{W}_{2}(\pi, \widetilde{\pi})$ because of the triangle inequality (recall that $\mathbf{W}_{2}$ defines a metric). This finishes the proof of statement (d).

# Appendix B.2. Proof of Proposition 1 

We start with proving (A4) for $T_{d_{1}, \ldots, d_{k}}$. Suppose we consider an additional random vector $X_{k+1}$ having copula measure $\mu^{C_{k+1}}$, an additional absolutely continuous reference measure $\nu_{k+1}$, and let $\mu^{C}$ be the copula measure of $\left(X_{1}, \ldots, X_{k+1}\right)$. If we first assume that $X_{k+1}$ is independent of $\left(X_{1}, \ldots, X_{k}\right)$, we have $\mu^{C}=\mu^{C} \times \mu^{C_{k+1}}$ and hence

$$
\begin{aligned}
\mathcal{T}_{d_{1}, \ldots, d_{k+1}}\left(\mu^{C} ; \nu_{1}, \ldots, \nu_{k+1}\right) & =\mathbf{W}_{2}^{2}\left(\mu^{C} \times \mu^{C_{k+1}}, \nu_{1} \times \cdots \times \nu_{k+1}\right)-\sum_{i=1}^{k+1} \mathbf{W}_{2}^{2}\left(\mu^{C_{i}}, \nu_{i}\right) \\
& =\mathbf{W}_{2}^{2}\left(\mu^{C}, \nu_{1} \times \cdots \times \nu_{k}\right)+\mathbf{W}_{2}^{2}\left(\mu^{C_{k+1}}, \nu_{k+1}\right)-\sum_{i=1}^{k+1} \mathbf{W}_{2}^{2}\left(\mu^{C_{i}}, \nu_{i}\right) \\
& =\mathbf{W}_{2}^{2}\left(\mu^{C}, \nu_{1} \times \cdots \times \nu_{k}\right)-\sum_{i=1}^{k} \mathbf{W}_{2}^{2}\left(\mu^{C_{i}}, \nu_{i}\right) \\
& =\mathcal{T}_{d_{1}, \ldots, d_{k}}\left(\mu^{C} ; \nu_{1}, \ldots, \nu_{k}\right)
\end{aligned}
$$

such that the Wasserstein dependence measure remains unchanged when adding $X_{k+1}$ into consideration. In general, suppose that $\gamma \in \Gamma\left(\mu^{C}, \nu_{1} \times \cdots \times \nu_{k+1}\right)$ is an optimal transport map from $\mu^{C}$ to $\nu_{1} \times \cdots \times \nu_{k+1}$, as joint distribution of $(\widetilde{\mathbf{U}}, \widetilde{\mathbf{V}})$ with $\widetilde{\mathbf{U}}=\left(\mathbf{U}, U_{k+1}\right)=\left(U_{1}, \ldots, U_{k+1}\right)$ and $\widetilde{\mathbf{V}}=\left(\mathbf{V}, V_{k+1}\right)=\left(V_{1}, \ldots, V_{k+1}\right)$, i.e.,

$$
\begin{aligned}
\mathcal{T}_{d_{1}, \ldots, d_{k+1}}\left(\mu^{C} ; \nu_{1}, \ldots, \nu_{k+1}\right) & =\mathbb{E}\left(\|\widetilde{\mathbf{U}}-\widetilde{\mathbf{V}}\|^{2}\right)-\sum_{i=1}^{k+1} \mathbf{W}_{2}^{2}\left(\mu^{C_{i}}, \nu_{i}\right) \\
& =\mathbb{E}\left(\|\mathbf{U}-\mathbf{V}\|^{2}\right)+\mathbb{E}\left(\left\|U_{k+1}-V_{k+1}\right\|^{2}\right)-\sum_{i=1}^{k+1} \mathbf{W}_{2}^{2}\left(\mu^{C_{i}}, \nu_{i}\right) \\
& \geq \mathbf{W}_{2}^{2}\left(\mu^{C}, \nu_{1} \times \cdots \times \nu_{k}\right)-\sum_{i=1}^{k} \mathbf{W}_{2}^{2}\left(\mu^{C_{i}}, \nu_{i}\right) \\
& =\mathcal{T}_{d_{1}, \ldots, d_{k}}\left(\mu^{C} ; \nu_{1}, \ldots, \nu_{k}\right)
\end{aligned}
$$

where the inequality follows from the definition of the Wassertein distance. If this inequality is an equality, it must hold that

$$
\mathbf{W}_{2}^{2}\left(\mu^{C}, \nu_{1} \times \cdots \times \nu_{k}\right)=\mathbb{E}\left(\|\mathbf{U}-\mathbf{V}\|^{2}\right)+\mathbb{E}\left(\left\|U_{k+1}-V_{k+1}\right\|^{2}\right)-\mathbf{W}_{2}^{2}\left(\mu^{C_{k+1}}, \nu_{k+1}\right) \geq \mathbb{E}\left(\|\mathbf{U}-\mathbf{V}\|^{2}\right)
$$

from which

$$
\mathbb{E}\left(\|\mathbf{U}-\mathbf{V}\|^{2}\right)=\mathbf{W}_{2}^{2}\left(\mu^{C}, \nu_{1} \times \cdots \times \nu_{k}\right) \text { and } \mathbb{E}\left(\left\|U_{k+1}-V_{k+1}\right\|^{2}\right)=\mathbf{W}_{2}^{2}\left(\mu^{C_{k+1}}, \nu_{k+1}\right)
$$

Because of the absolute continuity of the $\nu_{i}$, the latter implies (using Brenier's theorem) that there exists $T_{k+1}: \mathbb{I}^{d_{k+1}} \rightarrow$ $\mathbb{R}^{d_{k+1}}$ such that $U_{k+1}=T_{k+1}\left(V_{k+1}\right)$ almost surely, while the former means that there exist $T_{i}: \mathbb{I}^{q} \rightarrow \mathbb{R}^{d_{i

In the context of property (A7), assume without loss of generality that $X_{11}$ gets transformed to $T_{11}\left(X_{11}\right)$ for a strictly decreasing transformation $T_{11}$ and let $\mu_{\widetilde{C}}$ be the copula distribution of $\left(T_{1}\left(X_{1}\right), X_{2}, \ldots, X_{k}\right)$ with $T_{1}\left(X_{1}\right)=$ $\left(T_{11}\left(X_{11}\right), X_{12}, \ldots, X_{1 d_{1}}\right)$. Then, $\widetilde{C}\left(u_{1}, \ldots, u_{k}\right)=C\left(u_{1}, u_{2}, \ldots, u_{k}\right)-C\left(\widetilde{u}_{1}, u_{2}, \ldots, u_{k}\right)$ with $u_{1}=\left(1, u_{12}, \ldots, u_{1 d_{1}}\right)$ and $\widetilde{u}_{1}=\left(1-u_{11}, u_{12}, \ldots, u_{1 d_{1}}\right)$. Suppose now that $\gamma \in \Gamma\left(\mu_{C}, \nu_{1} \times \cdots \times \nu_{k}\right)$ is an optimal transport map from $\mu_{C}$ to $\nu_{1} \times \cdots \times \nu_{k}$, as joint distribution of $(U, V)$, i.e.,

$$
W_{2}^{2}\left(\mu_{C}, \nu_{1} \times \cdots \times \nu_{k}\right)=\mathbb{E}\left(\|U-V\|^{2}\right)=\int_{I^{2 q}}\|u-v\|^{2} \mathrm{~d} \gamma(u, v)
$$

Consider then $\widetilde{\gamma}(u, v)=\gamma\left(u_{1}, u_{2}, \ldots, u_{k}, v\right)-\gamma\left(\widetilde{u}_{1}, u_{2}, \ldots, u_{k}, v\right)$, which clearly is a coupling of $\mu_{\widetilde{C}}$ and $\nu_{1} \times \cdots \times \nu_{k}$, as joint distribution of $(\widetilde{U}, V)$ with $\widetilde{U}=\left(\widetilde{U}_{1}, U_{2}, \ldots, U_{k}\right)$ and $\widetilde{U}_{1}=\left(1-U_{11}, U_{12}, \ldots, U_{1 d_{1}}\right)$. Moreover, putting $\widetilde{u}=\left(\widetilde{u}_{1}, u_{2}, \ldots, u_{2}\right)$, we have

$$
W_{2}^{2}\left(\mu_{\widetilde{C}}, \nu_{1} \times \cdots \times \nu_{k}\right) \leq \mathbb{E}\left(\|\widetilde{U}-V\|^{2}\right)=\int_{I^{2 q}}\|\widetilde{u}-v\|^{2} \mathrm{~d} \widetilde{\gamma}(u, v)=\int_{I^{2 q}}\|u-v\|^{2} \mathrm{~d} \gamma(u, v)=W_{2}^{2}\left(\mu_{C}, \nu_{1} \times \cdots \times \nu_{k}\right)
$$

by simply doing a substitution $t_{11}=1-u_{11}$. Following a reversed reasoning, we also obtain $W_{2}^{2}\left(\mu_{C}, \nu_{1} \times \cdots \times\right.$ $\left.\nu_{k}\right) \leq W_{2}^{2}\left(\mu_{\widetilde{C}}, \nu_{1} \times \cdots \times \nu_{k}\right)$ and hence $W_{2}^{2}\left(\mu_{C}, \nu_{1} \times \cdots \times \nu_{k}\right)=W_{2}^{2}\left(\mu_{\widetilde{C}}, \nu_{1} \times \cdots \times \nu_{k}\right)$. Similarly, we can show that $W_{2}^{2}\left(\mu_{\bar{C}_{1}}, \nu_{1}\right)=W_{2}^{2}\left(\mu_{\widetilde{C}_{1}}, \nu_{1}\right)$ where $\mu_{\widetilde{C}_{1}}$ is the copula distribution of $T_{1}\left(X_{1}\right)$ and hence conclude (A7).

Finally, for (A8), we want that if $C_{n} \rightarrow C$ uniformly for $n \rightarrow \infty$, it is true that

$$
\left|\mathfrak{T}_{d_{1}, \ldots, d_{k}}\left(\mu_{C_{n}} ; \nu_{1}, \ldots, \nu_{k}\right)-\mathfrak{T}_{d_{1}, \ldots, d_{k}}\left(\mu_{C} ; \nu_{1}, \ldots, \nu_{k}\right)\right| \rightarrow 0
$$

as $n \rightarrow \infty$. Note that if $C_{n} \rightarrow C$ uniformly, we also have $\int_{I^{q}}\|u\|^{p} \mathrm{~d} C_{n}(u) \rightarrow \int_{I^{q}}\|u\|^{p} \mathrm{~d} C(u)$ as $n \rightarrow \infty$ for every $p>0$ (Helly-Bray theorem). Since convergence in distribution together with convergence of the first two moments implies $W_{2}$-convergence, equation (B.2) is proven by using similar arguments as for (d) of Lemma 1.

# Appendix C. Proofs of theoretical results of Section 3 

## Appendix C.1. Proof of Proposition 2

The first step of the proof consists of showing that the eigenvalues of $R_{m}$ are indeed given by (8). Therefore, already note that because of the orthogonality of the matrix

$$
U=\left(\begin{array}{cccc}
U_{11} & \mathbf{0}_{12} & \cdots & \mathbf{0}_{1 k} \\
\mathbf{0}_{21}^{\mathrm{T}} & U_{22} & \cdots & \boldsymbol{0}_{2 k} \\
\vdots & \vdots & \ddots & \vdots \\
\mathbf{0}_{k 1}^{\mathrm{T}} & \mathbf{0}_{k 2}^{\mathrm{T}} & \cdots & U_{k k}
\end{array}\right)
$$

denoting $\mathbf{0}_{i j} \in \mathbb{R}^{d_{i} \times d_{j}}$ for a matrix of zeroes, the eigenvalues of $R_{m}$ are the same as those of

$$
\Lambda_{m}=U^{\mathrm{T}} R_{m} U=\left(\begin{array}{cccc}
\Lambda_{11} & \Lambda_{11}^{1 / 2} \Pi_{12} \Lambda_{22}^{1 / 2} & \cdots & \Lambda_{11}^{1 / 2} \Pi_{1 k} \Lambda_{k k}^{1 / 2} \\
\Lambda_{22}^{1 / 2} \Pi_{12}^{T} \Lambda_{11}^{1 / 2} & \Lambda_{22} & \cdots & \Lambda_{22}^{1 / 2} \Pi_{2 k} \Lambda_{k k}^{1 / 2} \\
\vdots & \vdots & \ddots & \vdots \\
\Lambda_{k k}^{1 / 2} \Pi_{1 k}^{T} \Lambda_{11}^{1 / 2} & \Lambda_{k k}^{1 / 2} \Pi_{2 k}^{T} \Lambda_{22}^{1 / 2} & \cdots & \Lambda_{k k}
\end{array}\right)
$$

which we can find explicitly. Let $\mathbf{e}_{r, \ell}$ be the $r$-th canonical unit (column) vector in $\mathbb{R}^{\ell}$ and put $d_{0}=0$. For ease of notation, we also write $\Pi_{r \ell}=\Pi_{\ell r}^{\mathrm{T}}$ if $r>\ell$. We now list the eigenvalues and eigenvectors of the matrix $\Lambda_{m}$.

- For

Indeed, when fixing a certain $i \in\{0, \ldots, k-2\}$ and $j \in\left\{d_{i}+1, \ldots, d_{i+1}\right\}$, the $r$-th block row of (C.1) for $r \in\{1, \ldots, i\}$, multiplied with (C.2) equals
$\boldsymbol{\Lambda}_{r r} \mathbf{0}_{d_{r}}+\sum_{\ell=1}^{i} \boldsymbol{\Lambda}_{r r}^{1 / 2} \boldsymbol{\Pi}_{r \ell} \boldsymbol{\Lambda}_{\ell \ell}^{1 / 2} \mathbf{0}_{d_{\ell}}+\sum_{\ell=i+1}^{k} \boldsymbol{\Lambda}_{r r}^{1 / 2} \boldsymbol{\Pi}_{r \ell} \boldsymbol{\Lambda}_{\ell \ell}^{1 / 2} \lambda_{j, \ell \ell}^{1 / 2} \mathbf{e}_{j, d_{\ell}}=\sum_{\ell=i+1}^{k} \lambda_{j, \ell \ell}^{1 / 2} \boldsymbol{\Lambda}_{r r}^{1 / 2} \boldsymbol{\Pi}_{r} \ell \mathbf{e}_{j, d_{\ell}}=\mathbf{0}_{d_{r}}$, since $\boldsymbol{\Pi}_{r \ell} \mathbf{e}_{j, d_{\ell}}=\mathbf{0}_{d_{r}}$, as $j>d_{r}$. If for $r \in\{i+1, \ldots, k\}$, we multiply the $r$-th block row of (C.1) with (C.2), we obtain

$$
\begin{aligned}
& \sum_{\ell=1}^{i} \boldsymbol{\Lambda}_{r r}^{1 / 2} \boldsymbol{\Pi}_{r \ell} \boldsymbol{\Lambda}_{\ell \ell}^{1 / 2} \mathbf{0}_{d_{\ell}}+\boldsymbol{\Lambda}_{r r} \lambda_{j, r r}^{1 / 2} \mathbf{e}_{j, d_{r}}+\sum_{\ell=i+1}^{k} \stackrel{\ell, r}{\boldsymbol{\Lambda}_{r r}^{1 / 2} \boldsymbol{\Pi}_{r}} \mathbf{\ell} \boldsymbol{\Lambda}_{\ell \ell}^{1 / 2} \lambda_{j, \ell \ell}^{1 / 2} \mathbf{e}_{j, d_{\ell}}=\lambda_{j, r r}^{3 / 2} \mathbf{e}_{j, d_{r}}+\sum_{\ell=i+1}^{k} \stackrel{\ell, r}{\boldsymbol{\lambda}_{r r}^{1}} \boldsymbol{\Pi}_{r \ell} \boldsymbol{e}_{j, d_{\ell}} \\
& =\lambda_{j, r r}^{3 / 2} \mathbf{e}_{j, d_{r}}+\lambda_{j, r r}^{1 / 2} \sum_{\ell=i+1}^{k} \boldsymbol{\lambda}_{j,} \boldsymbol{\ell} \boldsymbol{\ell} \mathbf{e}_{j, d_{r}} \\
& =\lambda_{j, r r}^{1 / 2}\left(\sum_{\ell=i+1}^{k} \lambda_{j, \ell \ell}\right) \mathbf{e}_{j, d_{r}},
\end{aligned}
$$

since $\Pi_{r l} \mathbf{e}_{j, d_{\ell}}=\mathbf{e}_{j, d_{r}}$, as $j \leq d_{r}$. Hence, for every $r \in\{1, \ldots, k\}$, the $r$-th block element (in $\mathbb{R}^{d_{r} \times 1}$ ) of the matrix multiplication of $\boldsymbol{\Lambda}_{m}$ with the vector (C.2), is equal to (C.3) multiplied with the vector (C.2). This shows what was desired, and delivers $d_{1}+\left(d_{2}-d_{1}\right)+\cdots+\left(d_{k-1}-d_{k-2}\right)=d_{k-1}$ eigenvalues.

- For all $j=d_{k-1}+1, \ldots, d_{k}$, the vector

$$
\left(\mathbf{0}_{d_{1}}^{T}, \ldots, \mathbf{0}_{d_{k-1}}^{T}, \mathbf{e}_{j, d_{k}}^{T}\right)^{T}
$$

is an eigenvector with eigenvalue $\lambda_{j, k k}$.
Indeed, following the previous result, it is straightforward to see that for $r \in\{1, \ldots, k-1\}$, the multiplication of the $r$-th block row of $\boldsymbol{\Lambda}_{m}$ with the vector $(C .4)$ equals $\mathbf{0}_{d_{r}}$, as $j>d_{r}$, while the last block row leads to $\Lambda_{k k} \mathbf{e}_{j, d_{k}}=\lambda_{j, k k} \mathbf{e}_{j, d_{k}}$. This gives an additional amount of $\left(d_{k}-d_{k-1}\right)$ eigenvalues, resulting in an intermediate total of $d_{k-1}+\left(d_{k}-d_{k-1}\right)=d_{k}$ eigenvalues.

- For all $i=1, \ldots, k-1$ and all $j=1, \ldots, d_{i}$, the vector

$$
\left(\mathbf{0}_{d_{1}}^{T}, \ldots, \mathbf{0}_{d_{i-1}}^{T}, \lambda_{j,(i+1)(i+1)}^{1 / 2} \mathbf{e}_{j, d_{i}}^{T},-\lambda_{j, i i}^{1 / 2} \mathbf{e}_{j, d_{i+1}}^{T}, \mathbf{0}_{d_{i+2}}^{T}, \ldots, \mathbf{0}_{d_{k}}^{T}\right)
$$

is an eigenvector with eigenvalue 0.
Indeed, when fixing a certain $i \in\{1, \ldots, k-1\}$ and $j \in\left\{1, \ldots, d_{i}\right\}$, the $r$-th block row of (C.1) for $r \in\{1, \ldots, i-1\}$ multiplied with (C.5) equals

$$
\begin{aligned}
& \boldsymbol{\Lambda}_{r r} \mathbf{0}_{d_{r}}+\sum_{\ell=1}^{i-1} \stackrel{\ell, r}{\boldsymbol{\Lambda}_{r r}^{1 / 2} \boldsymbol{\Pi}_{r \ell} \Lambda_{\ell \ell}^{1 / 2} \mathbf{0}_{d_{\ell}}}+\boldsymbol{\Lambda}_{r r}^{1 / 2} \boldsymbol{\Pi} \boldsymbol{\Lambda}_{i i}^{1 / 2} \lambda_{j,(i+1)(i+1)}^{1 / 2} \mathbf{e}_{j, d_{i}}-\boldsymbol{\Lambda}_{r r}^{1 / 2} \boldsymbol{\Pi}_{r(i+1)}^{1 / 2} \boldsymbol{\Lambda}_{(i+1)(i+1)}^{1 / 2} \lambda_{j, i i}^{1 / 2} \mathbf{e}_{j, d_{i+1}}+\sum_{\ell=i+2}^{k} \boldsymbol{\Lambda}_{r r}^{1 / 2} \boldsymbol{\Pi}_{r l} \boldsymbol{\Lambda}_{\ell \ell}^{1 / 2} \mathbf{0}_{d_{\ell}} \\
& =\lambda_{j,(i+1)(i+1)}^{1 / 2} \lambda_{i i}^{1 / 2} \boldsymbol{\Lambda}_{r r}^{1 / 2} \boldsymbol{\Pi}_{r i} \mathbf{e}_{j, d_{i}}-\lambda_{j, i i}^{1 / 2} \lambda_{j,(i+1)(i+1)}^{1 / 2} \boldsymbol{\Lambda}_{r r}^{1 / 2} \boldsymbol{\Pi}_{r(i+1)} \mathbf{e}_{j, d_{i+1}} \\
& =

since $\Pi_{i(i+1)} e_{j, d_{i}}=e_{j, d_{i}}$, as $j \leq d_{i}$. For $r=i+1$, we get

$$
\begin{aligned}
& \sum_{\ell=1}^{i-1} \Lambda_{r r}^{1 / 2} \Pi_{r \ell} \Lambda_{\ell \ell^{\prime}}^{1 / 2} d_{\ell}+\lambda_{j,(i+1)(i+1)}^{1 / 2} \Lambda_{(i+1)(i+1)}^{1 / 2} \Pi_{(i+1) i} \Lambda_{i i}^{1 / 2} e_{j, d_{i}}-\lambda_{j, i i}^{1 / 2} \Lambda_{(i+1)(i+1)} e_{j, d_{i}+1}+\sum_{\ell=i+2}^{k} \Lambda_{r r}^{1 / 2} \Pi_{r l} \Lambda_{\ell \ell^{\prime}}^{1 / 2} d_{\ell} \\
&=\lambda_{j,(i+1)(i+1)}^{1 / 2} \lambda_{j, i i}^{1 / 2} \Lambda_{(i+1)(i+1)}^{1 / 2} e_{j, d_{i}+1}-\lambda_{j, i i}^{1 / 2} \lambda_{j,(i+1)(i+1)} e_{j, d_{i}+1} \\
&=\lambda_{j,(i+1)(i+1)}^{1 / 2} \lambda_{j, i i}^{1 / 2} \lambda_{j,(i+1)(i+1)}^{1 / 2} e_{j, d_{i}+1}-\lambda_{j, i i}^{1 / 2} \lambda_{j,(i+1)(i+1)} e_{j, d_{i}+1} \\
&=0^{d_{i}+1},
\end{aligned}
$$

since $\Pi_{(i+1) i} e_{j, d_{i}}=e_{j, d_{i}+1}$, as $j \leq d_{i}$. Finally, for $r \in\{i+2, \ldots, k\}$, we obtain

$$
\begin{aligned}
& \sum_{\ell=1}^{i-1} \Lambda_{r r}^{1 / 2} \Pi_{r l} \Lambda_{\ell \ell^{\prime}}^{1 / 2} d_{\ell}+\Lambda_{r r}^{1 / 2} \Pi_{r i} \Lambda_{i i}^{1 / 2} \lambda_{j,(i+1)(i+1)}^{1 / 2} e_{j, d_{i}}-\Lambda_{r r}^{1 / 2} \Pi_{r(i+1)} \Lambda_{(i+1)(i+1)}^{1 / 2} \lambda_{j, i i}^{1 / 2} e_{j, d_{i}+1}+\Lambda_{r r^{\prime}} d_{r}+\sum_{\ell=i+2}^{k} \Lambda_{r r}^{1 / 2} \Pi_{r \ell} \Lambda_{\ell \ell^{\prime}}^{1 / 2} d_{\ell} \\
&=\lambda_{j,(i+1)(i+1)}^{1 / 2} \lambda_{j, i i}^{1 / 2} \Lambda_{r r}^{1 / 2} \Pi_{r i} e_{j, d_{i}}-\lambda_{j, i i}^{1 / 2} \lambda_{j,(i+1)(i+1)}^{1 / 2} \Lambda_{r r}^{1 / 2} \Pi_{r(i+1)} e_{j, d_{i}+1} \\
&=0^{d_{r}},
\end{aligned}
$$

since $\Pi_{r i} e_{j, d_{i}}=\Pi_{r(i+1)} e_{j, d_{i}+1}$, and we come by $d_{1}+\cdots+d_{k-1}$ eigenvalues, resulting in the desired total of $d_{1}+\cdots+d_{k}=q$ eigenvalues. These are indeed given by

$$
\lambda\left(R_{m}\right)=\left(\lambda_{j, 11}+\lambda_{j, 22}+\cdots+\lambda_{j, k k}\right)_{j=1}^{q}
$$

Next, we need to show that for an arbitrary $A \in \Gamma\left(R_{11}, \ldots, R_{k k}\right)$ with eigenvalues $\lambda_{1} \geq \lambda_{2} \geq \cdots \geq \lambda_{q}$, it holds that
$\sum_{\ell=1}^{n} \lambda_{\ell} \leq \sum_{\ell=1}^{w} d_{\ell}+\sum_{\ell=1}^{n} \lambda_{\ell,(w+1)(w+1)}+\cdots+\lambda_{\ell, k k}$ for all $w=0, \ldots, k-1, n=d_{w}+1, \ldots, d_{w+1}$.

For this, we first introduce some notation. We know that $A$ must be of the form

$$
A=\left(\begin{array}{cccc}
R_{11} & Q_{12} & \cdots & Q_{1 k} \\
Q_{12}^{T} & R_{22} & \cdots & Q_{2 k} \\
\vdots & \vdots & \ddots & \vdots \\
Q_{1 k}^{T} & Q_{2 k}^{T} & \cdots & R_{k k}
\end{array}\right) \in \mathbb{R}^{q \times q}
$$

with $Q_{i j} \in \mathbb{R}^{d_{i} \times d_{j}}$. Based on this, define the matrices

$$
B_{i}=\left(\begin{array}{cccc}
R_{(i+1)(i+1)} & Q_{(i+1)(i+2)} & \cdots & Q_{(i+1) k} \\
Q_{(i+1)(i+2)}^{T} & R_{(i+2)(i+2)} & \cdots & Q_{(i+2) k} \\
\vdots & \vdots & \ddots & \vdots \\
Q_{(i+1) k}^{T} & Q_{(i+2) k}^{T} & \cdots & R_{k k}
\end{array}\right)
$$

and

$$
C_{i}=\left(\begin{array}{ccc}
R_{i i} & Q_{i} & Q_{i}^{T} \\
& B_{i} &
\end{array}\right)
$$

where $Q_{i}=\left(Q_{i(i+1)} \cdots Q_{i k}\right) \in \mathbb{R}^{d_{i} \times\left(d_{i+1} \cdots+d_{k}\right)}$, for all $i=1, \ldots, k-2$. We will approach $C_{i}$ as a block matrix consisting of four blocks. Note that $B_{i} \in \mathbb{R}^{\left(d_{i+1}+\cdots+d_{k}\right) \times\left(d_{i+1}+\cdots+d_{k}\right)}$ and $C_{i} \in \mathbb{R}^{\left(d_{i}+\cdots+d_{k}\right) \times\left(d_{i}+\cdots+d_{k}\right)}$. Further, put
$\gamma_{1, i} \geq \gamma_{2, i} \geq \cdots \geq \gamma_{m_{i}, i} \quad$ the eigenvalues of $C_{i}$ for $i=1, \ldots, k-2, m_{i}=d_{i}+\cdots+d_{k}$
$\lambda_{1, i i} \geq \lambda_{2, i i} \geq \cdots \geq \lambda_{d_{i}, i i}$ the eigenvalues of $R_{i i}$ for $i=1, \ldots, k$
$\mu_{1, i} \geq \mu_{2, i} \geq \cdots \geq \mu_{t_{i}, i} \quad$ the eigenvalues of $B_{i}$ for $i=1, \ldots, k-2, t_{i}=d_{i+

and integers

$$
\begin{aligned}
& 1 \leq r_{1, i}<\cdots<r_{\alpha_{i}, i} \leq d_{i}, \quad r_{\ell, i}=d_{i}-\alpha_{i}+\ell \text { for } \ell>\alpha_{i}, \text { for } i=1, \ldots, k \\
& 1 \leq j_{1, i}<\cdots<j_{\beta_{i}, i} \leq t_{i}, \quad j_{\ell, i}=t_{i}-\beta_{i}+\ell \text { for } \ell>\beta_{i}, \text { for } i=1, \ldots, k-2
\end{aligned}
$$

that, defined as such, will guarantee that

$$
\begin{gathered}
\sum_{\ell=1}^{\alpha_{i}+\beta_{i}} \gamma_{r_{\ell, i}+j_{\ell, i}-\ell, i} \leq \sum_{\ell=1}^{\alpha_{i}} \lambda_{r_{\ell, i}, i i}+\sum_{\ell=1}^{\beta_{i}} \mu_{j_{\ell, i}, i} \text { for } i=1, \ldots, k-2 \\
\sum_{\ell=1}^{\alpha_{k-1}+\alpha_{k}} \mu_{r_{\ell, k-1}+r_{\ell, k}-\ell, k-2} \leq \sum_{\ell=1}^{\alpha_{k-1}} \lambda_{r_{\ell, k-1},(k-1)(k-1)}+\sum_{\ell=1}^{\alpha_{k}} \lambda_{r_{\ell, k}, k k}
\end{gathered}
$$

Notice that (C.7) describes a total of $k-1$ inequalities. We will now prove (C.6) by making an adequate choice for the $\alpha_{i}, \beta_{i}$ and corresponding indices $r_{\ell, i}, j_{\ell, i}$. In particular, when considering a fixed $w \in\{0, \ldots, k-1\}$ and fixed $n \in\left\{d_{w}+1, \ldots, d_{w+1}\right\}$, take

$$
\begin{gathered}
\alpha_{i}=d_{i}, r_{\ell, i}=\ell \text { for } \ell=1, \ldots, d_{i}, i=1, \ldots, w \\
\alpha_{i}=n, r_{\ell, i}=\ell \text { for } \ell=1, \ldots, n, i=w+1, \ldots, k \\
\beta_{i}=t_{w}-t_{w}+(k-w) n, j_{\ell, i}=\left\{\begin{array}{l}
\ell \quad \text { if } \ell \in\{1, \ldots, n\} \\
t_{w}-(k-w) n+\ell, \text { if } \ell \in\left\{n+1, \ldots, \beta_{i}\right\}
\end{array}\right. \\
\text { for } i=1, \ldots, \min \{k-2, w\} \\
\beta_{i}=(k-i) n, j_{\ell, i}=\left\{\begin{array}{l}
\ell \quad \text { if } \ell \in\{1, \ldots, n\} \\
t_{i}-(k-i) n+\ell, \text { if } \ell \in\left\{n+1, \ldots, \beta_{i}\right\}
\end{array}\right. \\
\text { for } i=w+1, \ldots, k-2 .
\end{gathered}
$$

Then, concerning the $k-2^{\prime}$ th and $k-1^{\prime}$ th inequality of (C.7), we see that if $w=k-1$, we have

$$
\begin{aligned}
\sum_{\ell=1}^{\beta_{k-2}} \mu_{j_{\ell}, k-2} & =\sum_{\ell=1}^{n} \mu_{\ell, k-2}+\sum_{\ell=n+1}^{\beta_{k-2}} \mu_{d_{k}-n+\ell, k-2} \\
& =\mu_{1, k-2}+\cdots+\mu_{n, k-2}+\mu_{d_{k}+1, k-2}+\cdots+\mu_{t_{k-2}, k-2}
\end{aligned}
$$

and,

$$
\begin{aligned}
\sum_{\ell=1}^{\alpha_{k-1}+\alpha_{k}} \mu_{r_{\ell, k-1}+r_{\ell, k}-\ell, k-2} & =\sum_{\ell=1}^{d_{k-1}+n} \mu_{r_{\ell, k-1}+r_{\ell, k}-\ell, k-2} \\
& =\sum_{\ell=1}^{d_{k-1}} \mu_{\ell, k-2}+\sum_{\ell=d_{k-1}+1}^{n} \mu_{\ell, k-2}+\sum_{\ell=n+d_{k-1}}^{n+d_{k}-1} \mu_{d_{k}-n+\ell, k-2} \\
& =\mu_{1, k-2}+\cdots+\mu_{n, k-2}+\mu_{d_{k}+1, k-2}+\cdots+\mu_{d_{k-1}+d_{k}, k-2} .
\end{aligned}
$$

Since $t_{k-2}=d_{k-1}+d_{k}$, we see that (C.8) and (C.9) are equal. If on the other hand $w \in\{0, \ldots, k-2\}$, we get

$$
\begin{aligned}
\sum_{\ell=1}^{\beta_{k}-2} \mu_{j_{\ell}, k-2} & =\sum_{\ell=1}^{n} \mu_{\ell, k-2}+\sum_{\ell=n+1}^{\beta_{k}-2} \mu_{t_{k-2}-2 n+\ell, k-2} \\
& =\mu_{1, k-2}+\cdots+\mu_{n, k-2}+\mu_{t_{k-2}-n+1, k-2}+\cdots+\mu_{t_{k-2}, k-2}
\end{aligned}
$$

and,

$$
\begin{aligned}
\sum_{\ell=1}^{\alpha_{k}+\alpha_{k}} \mu_{r_{\ell, k-1}+r_{\ell, k}-\ell, k-2} & =\sum_{\ell=1}^{2 n} \mu_{r_{\ell, k-1}+r_{\ell, k}-\ell, k-2} \\
& =\sum_{\ell=1}^{n} \mu_{\ell, k-2}+\sum_{\ell=n+1}^{2 n} \mu_{d_{k-1}+d_{k}-2 n+\ell, k-2} \\
& =\mu_{1, k-2}+\cdots+\mu_{n, k-2}+\mu_{d_{k-1}+d_{k}-n+1, k-2}+\cdots+\mu_{d_{k-1}+d_{k}, k-2} .
\end{aligned}
$$



Again because $t_{k-2}=d_{k-1}+d$, we have equality between (C.10) and (C.11). We thus have shown so far that the second term on the right side of the $k-2^{\prime}$ th inequality of (C.7) equals the term on the left side of the $k-1^{\prime}$ th inequality. Now, concerning the $i$ 'th and $i+1^{\prime}$ th inequality for $i \in\{1, \ldots, k-3\}$, we must have either both $i, i+1 \in\{w+1, \ldots, k-2\}$ or both $i, i+1 \in\{1, \ldots, w\}$, or $i \in\{1, \ldots, w\}, i+1 \in\{w+1, \ldots, k-2\}$ meaning $i=w$. In the first case, it holds that

$$
\begin{aligned}
\sum_{\ell=1}^{\alpha_{i}+\beta_{i}+1} \gamma_{r_{\ell}, i+1}+j_{\ell, i+1}-\ell, i+1 & =\sum_{\ell=1}^{n+\beta_{i}+1} \gamma_{r_{\ell}, i+1}+j_{\ell, i+1}-\ell, i+1 \\
& =\sum_{\ell=1}^{n} \gamma_{\ell, i+1}+\sum_{\ell=n+1}^{\beta_{i}+1} \gamma_{d_{i+1}-n+t_{i+1}-(k-i-1) n+\ell, i+1}+\sum_{\ell=\beta_{i}+1+1}^{n+\beta_{i}+1} \gamma_{d_{i+1}-n+t_{i+1}-(k-i-1) n+\ell, i+1} \\
& =\gamma_{1, i+1}+\cdots+\gamma_{n, i+1}+\gamma_{d_{i+1}+t_{i+1}-(k-i-1) n+1, i+1}+\cdots+\gamma_{d_{i+1}+t_{i+1}, i+1}
\end{aligned}
$$

and

$$
\sum_{\ell=1}^{\beta_{i}} \mu j_{\ell, i, i}=\sum_{\ell=1}^{n} \mu_{\ell, i}+\sum_{\ell=n+1}^{\beta_{i}} \mu_{t_{i}-(k-i) n+\ell, i}=\mu_{1, i}+\cdots+\mu_{n, i}+\mu_{t_{i}-(k-i) n+n+1, i}+\cdots+\mu_{t_{i}, i}
$$

Since $t_{i}=d_{i+1}+t_{i+1}$ and $C_{i+1}=B_{i}$ (by construction, hence they also have the same eigenvalues), we see that (C.12) is equal to (C.13). For the second case, i.e., both $i, i+1 \in\{1, \ldots, w\}$, we have

$$
\begin{aligned}
\sum_{\ell=1}^{\alpha_{i}+1+\beta_{i}+1} \gamma_{r_{\ell}, i+1}+j_{\ell, i+1}-\ell, i+1 & =\sum_{\ell=1}^{d_{i+1}+\beta_{i}+1} \gamma_{r_{\ell}, i+1}+j_{\ell, i+1}-\ell, i+1 \\
& =\sum_{\ell=1}^{d_{i+1}} \gamma_{\ell, i+1}+\sum_{\ell=d_{i+1}+1}^{n} \gamma_{\ell, i+1}+\sum_{\ell=n+1}^{\beta_{i}+1} \gamma_{t_{w}-(k-w) n+\ell, i+1}+\sum_{\ell=\beta_{i}+1+1}^{d_{i}+1+\beta_{i}+1} \gamma_{t_{w}-(k-w) n+\ell, i+1} \\
& =\gamma_{1, i+1}+\cdots+\gamma_{n, i+1}+\gamma_{t_{w}-(k-w-1) n+1, i+1}+\cdots+\gamma_{d_{i+1}+t_{i+1}, i+1}
\end{aligned}
$$

and

$$
\sum_{\ell=1}^{\beta_{i}} \mu j_{\ell, i, i}=\sum_{\ell=1}^{n} \mu_{\ell, i}+\sum_{\ell=n+1}^{\beta_{i}} \mu_{t_{w}-(k-w) n+\ell, i}=\mu_{1, i}+\cdots+\mu_{n, i}+\mu_{t_{w}-(k-w-1) n+1, i}+\cdots+\mu_{t_{i}, i}
$$

For the same reasons as in the previous case, we clearly see that (C.14) and (C.15) are the same expressions. Finally, if $i=w$,

$$
\begin{aligned}
\sum_{\ell=1}^{\alpha_{i}+1+\beta_{i}+1} \gamma_{r_{\ell}, i+1}+j_{\ell, i+1}-\ell, i+1 & =\sum_{\ell=1}^{n+\beta_{w}+1} \gamma_{r_{\ell}, w+1}+j_{\ell, w+1}-\ell, w+1 \\
& =\gamma_{1, w+1}+\cdots+\gamma_{n, w+1}+\gamma_{d_{w+1}+t_{w+1}-(k-w-1) n+1, w+1}+\cdots+\gamma_{d_{w+1}+t_{w+1}, w+1}
\end{aligned}
$$

and,

$$
\sum_{\ell=1}^{\beta_{i}} \mu j_{\ell, i, i}=\sum_{\ell=1}^{\beta_{w}} \mu j_{\ell, w, w}=\mu_{1, w}+\cdots+\mu_{n, w}+\mu_{t_{w}-(k-w-1) n+1, w}+\cdots+\mu_{t_{w}, w}
$$

Since $t_{w}=d_{w+1}+t_{w+1}$ and $C_{w+1}=B_{w}$, we also have equality between (C.16) and (C.17). All together, we have proven that the second term on the right hand side of the $i$ ' th inequality of (C.7) is equal to the term on the left hand side of the $i+1^{\prime}$ th inequality for all $i=1, \ldots, k-2$. Hence (C.7) can be reduced to

$$
\sum_{\ell=1}^{\alpha_{1}+\beta_{1}} \gamma_{r_{\ell}, 1}+j_{\ell, 1}-\ell, 1 \leq \sum_{\ell=1}^{w} d_{\ell}+\sum_{\ell=1}^{n}\left(\lambda_{\ell,(w+1)(w+1)}+\cdots+\lambda_{\ell, k k}\right)
$$



Moreover, since by choice $r_{\ell, 1}=\ell$ for all $\ell=1, \ldots, n$ if $\mathbf{w}=\mathbf{0}$, or $r_{\ell, 1}=\ell$ for all $\ell=1, \ldots, d_{1}$ and $r_{\ell, 1}=d_{1}-d_{1}+\ell=\ell$ for all $\ell>d_{1}$ if $\mathbf{w}>\mathbf{0}$, and $j_{\ell, 1}=\ell$ for all $\ell=1, \ldots, n$, we definitely have

$$
\sum_{\ell=1}^{n} \gamma_{\ell, 1} \leq \sum_{\ell=1}^{\alpha_{1}+\beta_{1}} \gamma_{r_{\ell, 1}+j_{\ell, 1}-\ell, 1}
$$

The inequality in (C.19) is an equality if there are $\alpha_{1}+\beta_{1}-n$ eigenvalues equal to zero. If for example $\mathbf{w}=\boldsymbol{k}-\mathbf{1}$ and $n=d_{k}$, this means that $d_{1}+t_{1}-t_{k-1}+n-n=q-d_{k}$ eigenvalues should be zero, which is the case for the matrix $R_{m}$. Combining (C.18) with (C.19) and realizing that the eigenvalues $\gamma_{\ell, 1}$ are the same as the eigenvalues $\lambda_{\ell}$, since $A=C_{1}$, finishes the proof.

# Appendix C.2. Proof of Proposition 3 

Consider an arbitrary $A \in \boldsymbol{\Gamma}\left(R_{11}, \ldots, R_{k k}\right)$ having ordered eigenvalues $\lambda_{1} \geq \cdots \geq \lambda_{q}$. Then, by definition of the Bures-Wasserstein distance (3),

$$
d_{W}^{2}\left(A, I_{q}\right)=q+\operatorname{tr}(A)-2 \operatorname{tr}\left(A^{1 / 2}\right)=q+\sum_{j=1}^{q} \lambda_{j}-2 \sum_{j=1}^{q} \lambda_{j}^{1 / 2}
$$

Notice that the function $\lambda \mapsto \lambda-2 \lambda^{1 / 2}$ is convex for $\lambda \in[0, \infty)$. By Proposition 2, we know that the eigenvalues of $R_{m}$ majorize those of $A$. From Lemma 2, it follows that (C.20) is maximal if $A=R_{m}$. Secondly, we have

$$
R_{0}^{1 / 2} A R_{0}^{1 / 2}=\left(\begin{array}{cccc}
R_{11}^{2} & R_{11}^{1 / 2} \Psi_{12} R_{22}^{1 / 2} & \cdots & R_{11}^{1 / 2} \Psi_{1 k} R_{k k}^{1 / 2} \\
R_{22}^{1 / 2} \Psi_{12}^{T} R_{11}^{1 / 2} & R_{22}^{2} & \cdots & R_{22}^{1 / 2} \Psi_{2 k} R_{k k}^{1 / 2} \\
\vdots & \vdots & \ddots & \vdots \\
R_{k k}^{1 / 2} \Psi_{1 k}^{T} R_{11}^{1 / 2} & R_{k k}^{1 / 2} \Psi_{2 k}^{T} R_{22}^{1 / 2} & \cdots & R_{k k}^{2}
\end{array}\right)
$$

Recall that $R_{i i}^{\alpha}=U_{i i} \Lambda_{i i}^{\alpha} U_{i i}^{T}$ is the eigendecomposition of $R_{i i}^{\alpha}$ for $\alpha>0$, and for $R_{m}$ we have $\Psi_{i j}=U_{i i} \Lambda_{i i}^{1 / 2} \Pi_{i j} \Lambda_{j j}^{1 / 2} U_{j j}^{T}$. Hence, we get

$$
R_{i i}^{1 / 2} \Psi_{i j} R_{j j}^{1 / 2}=\left(U_{i i} \Lambda_{i i}^{1 / 2} U_{i i}^{T}\right)\left(U_{i i} \Lambda_{i i}^{1 / 2} \Pi_{i j} \Lambda_{j j}^{1 / 2} U_{j j}^{T}\right)\left(U_{j j} \Lambda_{j j}^{1 / 2} U_{j j}^{T}\right)=U_{i i} \Lambda_{i i} \Pi_{i j} \Lambda_{j j} U_{j j}^{T}
$$

which is of the same form as $\Psi_{i j}$, but with $\Lambda_{i i}^{1 / 2}$ and $\Lambda_{j j}^{1 / 2}$ replaced by $\Lambda_{i i}$ and $\Lambda_{j j}$. Applying Proposition 2 with $R_{i i}^{2}$ instead of $R_{i i}$ for $i=1, \ldots, k$, it follows that the eigenvalues of an arbitrary matrix in $\boldsymbol{\Gamma}\left(R_{11}^{2}, \ldots, R_{k k}^{2}\right)$ are majorized by those of the matrix $R_{0}^{1 / 2} R_{m} R_{0}^{1 / 2}$. Hence,

$$
d_{W}^{2}\left(A, R_{0}\right)=2 \operatorname{tr}(A)-2 \operatorname{tr}\left\{\left(R_{0}^{1 / 2} A R_{0}^{1 / 2}\right)^{1 / 2}\right\}=2 \operatorname{tr}(A)-2 \sum_{j=1}^{q} \kappa_{j}^{1 / 2}
$$

with $\kappa_{1}, \ldots, \kappa_{q}$ the eigenvalues of $R_{0}^{1 / 2} A R_{0}^{1 / 2}$. The fact that (C.21) is maximal if $A=R_{m}$ now follows from the convexity of the function $\kappa \mapsto-\kappa^{1 / 2}$ on $[0, \infty)$ and Lemma 2 .

## Appendix C.3. Additional lemmas and proof of Theorem 1

Lemma 3. Under the conditions of Theorem 1, it holds that, for $H_{t} \in \mathcal{S}^{q}$ for $t>0$ and $H \in \mathcal{S}^{q}$ such that $\left\|H_{t}-H\right\|_{F} \rightarrow 0$ as $t \rightarrow 0$,

$$
\lim _{t \rightarrow 0} \frac{\operatorname{tr}\left\{\left(R+t H_{t}\right)_{m}^{1 / 2}\right\}-\operatorname{tr}\left(R_{m}^{1 / 2}\right)}{t}=\frac{1}{2} \operatorname{tr}\left(\Upsilon_{1} H\right)
$$

with $\left(R+t H_{t}\right)_{m}^{1 / 2}$ the matrix in (7) for $R$ replaced by $R+t H_{t}$ and $\Upsilon_{1}$ defined in (16).



Proof. Define the map $\mathcal{L}:\left(\mathcal{S}_{q},\|\cdot\|_{F}\right) \rightarrow\left(\mathcal{S}_{q},\|\cdot\|_{F}\right): A \mapsto \mathcal{L}(A)$ via $\mathcal{L}(A)$ being the diagonal matrix whose diagonal is equal to the $q$ eigenvalues (counting multiplicities) of $A$ in decreasing order. Then, we have $\mathcal{L}\left(R_{i i}\right)=\Lambda_{i i}=$ $\operatorname{diag}\left(\lambda_{1, i i}, \ldots, \lambda_{d_{i}, i i}\right)$ for $i=1, \ldots, k$. Also define the map

$$
\mathcal{M}:\left(\mathcal{S}_{>}^{d_{1}} \times \cdots \times \mathcal{S}_{>}^{d_{k}},\|\cdot\|_{F}\right) \rightarrow\left(\mathcal{S}_{>}{ }_{>}^{d_{1}} \times \cdots \times \mathcal{S}_{>}{ }_{>}^{d_{k}},\|\cdot\|_{F}\right):\left(A_{1}, \ldots, A_{k}\right) \mapsto\left(\mathcal{L}\left(A_{1}\right), \ldots, \mathcal{L}\left(A_{k}\right)\right)
$$

where the Frobenius norm is naturally defined for a certain $\left(A_{1}, \ldots, A_{k}\right) \in \mathcal{S}^{d_{1}} \times \cdots \times \mathcal{S}^{d_{k}}$ through $\left\|\left(A_{1}, \ldots, A_{k}\right)\right\|_{F}=$ $\left(\left\|A_{1}\right\|_{F}^{2}+\cdots+\left\|A_{k}\right\|_{F}^{2}\right)^{1 / 2}$. Using Lemma 3 of [36], it is then quickly seen that the Fréchet derivative of $\mathcal{M}$ at $\left(R_{11}, \ldots, R_{k k}\right)$ in the direction of a certain $H=\left(H_{11}, \ldots, H_{k k}\right) \in \mathcal{S}_{>}^{d_{1}} \times \cdots \times \mathcal{S}_{>}^{d_{k}}$ is $\Delta(H)=\left(D^{U_{11}^{T}} H_{11} U_{11}, \ldots, D^{U_{k k}^{T}} H_{k k} U_{k k}\right)$, with $D^{U_{i i}^{T}} H_{i i} U_{i i}$ the diagonal matrix containing the diagonal of $U_{i i}^{T} H_{i i} U_{i i}$. Consider now (recalling that $d_{1} \leq \cdots \leq d_{k}$ )

$$
g:\left(\mathcal{S}_{>}\right.\left.{ }^{d_{1}} \times \cdots \times \mathcal{S}_{>}^{d_{k}},\|\cdot\|_{F}\right) \rightarrow(\mathbb{R},|\cdot|):\left(B_{1}, \ldots, B_{k}\right) \mapsto \sum_{j=1}^{d_{k}}\left(\eta_{j, 11}+\cdots+\eta_{j, k k}\right)^{1 / 2}
$$

with $\eta_{j, i i}$ the eigenvalues of $B_{i}$ in decreasing order for $i=1, \ldots, k$ and $j=1, \ldots, d_{i}$, and putting $\eta_{j, i i}=0$ for $j=d_{i}+$ $1, \ldots, d_{k}$. We see that $\operatorname{tr}\left(R_{m}^{1 / 2}\right)=g\left(\mathcal{L}\left(R_{11}\right), \ldots, \mathcal{L}\left(R_{k k}\right)\right)=g\left(\Lambda_{11}, \ldots, \Lambda_{k k}\right)$, also putting $\lambda_{j, i i}=0$ for $j=d_{i}+1, \ldots, d_{k}$.
The Fréchet derivative of $g$ at $\left(\Lambda_{11}, \ldots, \Lambda_{k k}\right)$ in the direction of $\Delta(H)$ equals $\Psi(\Delta(H))$, where $\Psi: \mathcal{S}_{>}{ }_{>}^{d_{1}} \times \cdots \times \mathcal{S}_{>}{ }_{>}^{d_{k}} \rightarrow \mathbb{R}$ satisfies
$\lim _{\|\Delta(H)\|_{F} \rightarrow 0} \frac{\left|g\left(\Lambda_{11}+D^{U_{11}^{T}} H_{11} U_{11}, \ldots, \Lambda_{k k}+D^{U_{k k}^{T}} H_{k k} U_{k k}\right)-g\left(\Lambda_{11}, \ldots, \Lambda_{k k}\right)-\Psi(\Delta(H))\right|}{\|\Delta(H)\|_{F}}=0$.
Defining $t_{j, i i}=\left(U_{i i}^{T} H_{i i} U_{i i}\right)_{j j}$ for all $i=1, \ldots, k$ and $j=1, \ldots, d_{i}$, as well as $t_{j, i i}=0$ for $j=d_{i}+1, \ldots, d_{k}$, it is obvious that the eigenvalues of $\Lambda_{i i}+D^{U_{i i}^{T}} H_{i i} U_{i i}$ are $\lambda_{j, i i}+t_{j, i i}$. Moreover, since we assumed that the eigenvalues $\lambda_{j, i i}$ are distinct over $j$, it will hold, for $\|\Delta(H)\|_{F}$ small enough, that $\lambda_{j, i i}+t_{j, i i}$ are in decreasing order again over $j$. Hence, using our definition of $g$, we see that (C.22) becomes



From expression (C.23), we observe that $\Psi(\Delta(H))$ is nothing more than the total derivative of the function

$$
f: \mathbb{R}^{k d_{k}} \rightarrow \mathbb{R}:\left(x_{1,11}, x_{1,22}, \ldots, x_{d_{k}, k k}\right) \mapsto \sum_{j=1}^{d_{k}}\left(\sum_{i=1}^{k} x_{j, i i}\right)^{1 / 2}
$$

at $\left(\lambda_{1,11}, \lambda_{1,22}, \ldots, \lambda_{d_{k}, k k}\right)$ evaluated in $\left(t_{1,11}, t_{1,22}, \ldots, t_{d_{k}, k k}\right)$. Computing the Jacobian matrix of $f$, we find

$$
\begin{aligned}
\Psi(\Delta(H)) & =\sum_{j=1}^{d_{k}}\left(\sum_{i=1}^{k} \frac{1}{2}\left(\lambda_{j, 11}+\cdots+\lambda_{j, k k}\right)^{1 / 2} t_{j, i i}\right) \\
& =\sum_{i=1}^{k}\left(\sum_{j=1}^{d_{i}} \frac{1}{2}\left(\lambda_{j, 11}+\cdots+\lambda_{j, k k}\right)^{1 / 2} t_{j, i i}\right) \\
& =\sum_{i=1}^{k}\left(\sum_{j=1}^{d_{i}} \frac{1}{2}\left(\lambda_{j, 11}+\cdots+\lambda_{j, k k}\right)^{1 / 2}\left(U_{i i}^{T} H_{i i} U_{i i}\right)_{j j}\right)
\end{aligned}
$$

By the chain rule, we have just shown that





where $H_{t, i i}$ is the $d_{i} \times d_{i}$ diagonal block of $H_{t}$. Using the notations (11), (12) and (13), we can further simplify the above expression into

$$
\frac{1}{2} \sum_{i=1}^{k} \operatorname{tr}\left(\Delta_{i} U_{i i}^{T} H_{i i} U_{i i}\right)=\frac{1}{2} \sum_{i=1}^{k} \operatorname{tr}\left(P_{i}^{T} U_{i i} \Delta_{i} U_{i i}^{T} P_{i} H\right)=\frac{1}{2} \operatorname{tr}\left(\Upsilon_{1} H\right)
$$

where we used that $\operatorname{tr}\left(\operatorname{Adiag}(B)\right)=\operatorname{tr}\left(\operatorname{diag}(A) B\right)$ for square matrices $A, B$, the cyclic permutation property of the trace operator, the fact that $H_{i i}=P_{i} H P_{i}^{T}$ and finally the identity $\sum_{i=1}^{k} P_{i}^{T} A_{i} P_{i}=\operatorname{diag}\left(A_{1}, \ldots, A_{k}\right)$ for $\left(d_{i} \times d_{i}\right)$ matrices $A_{i}$.

Lemma 4. The Fréchet derivative of the map

$$
\eta: \mathbb{S}_{>}^{q} \rightarrow \mathbb{R}: R \mapsto \operatorname{tr}\left\{\left(R_{0}^{1 / 2} R R_{0}^{1 / 2}\right)^{1 / 2}\right\}
$$

is given by

$$
\lim _{t \rightarrow 0} \frac{\eta\left(R+t H_{t}\right)-\eta(R)}{t}=\frac{1}{2} \operatorname{tr}\left\{\left(J_{0}+J_{-1}\right) H\right\}
$$

for $H_{t}, H \in \mathbb{S}^{q}$ with $\left\|H_{t} \rightarrow H\right\|_{F} \rightarrow 0$ as $t \rightarrow 0$ and $J$ and $J_{0}$ as in (14) and (15) respectively.

Proof. From Lemma 5 in [36], the Fréchet derivative of the map

$$
\phi: \mathbb{S}_{>}^{q} \times \mathbb{S}_{>}^{q} \rightarrow \mathbb{R}:\left(H, R\right) \mapsto 2 \operatorname{tr}\left\{\left(H^{1 / 2} R H^{1 / 2}\right)^{1 / 2}\right\}
$$

at $(H, R) \in \mathbb{S}_{>}^{q} \times \mathbb{S}_{>}^{q}$ in the direction of $(G, H) \in \mathbb{S}^{q} \times \mathbb{S}^{q}$ equals $\operatorname{tr}(J G)+\operatorname{tr}\left(J_{-1} H\right)$ with

$$
\begin{aligned}
& J=H^{-1 / 2}\left(H^{1 / 2} R H^{1 / 2}\right)^{1 / 2} H^{-1 / 2}=R^{1 / 2}\left(R^{1 / 2} H R^{1 / 2}\right)^{-1 / 2} R^{1 / 2} \\
& J_{-1}=H^{1 / 2}\left(H^{1 / 2} R H^{1 / 2}\right)^{-1 / 2} H^{1 / 2}=R^{-1 / 2}\left(R^{1 / 2} H R^{1 / 2}\right)^{1 / 2} R^{-1 / 2}
\end{aligned}
$$

Applying this to $(H, R)=\left(R_{0}, R\right)$ and $(G, H)=\left(H_{0}, H\right)$ with $H_{0}$ having the same $d_{i} \times d_{i}$ diagonal blocks as $H$, but zero off-diagonal blocks, yields $\frac{1}{2}\left(\operatorname{tr}\left(J H_{0}\right)+\operatorname{tr}\left(J_{-1} H\right)\right)$ as the Fréchet derivative of $\eta$ at $R$ in the direction of $H$, with $J$ given in (14). The result follows from $\operatorname{tr}\left(J H_{0}\right)=\operatorname{tr}\left(J_{0} H\right)$, with $J_{0}$ given in (15).

Lemma 5. Under the conditions of Theorem 1, it holds that, for $H_{t} \in \mathbb{S}^{q}$ for $t>0$ and $H \in \mathbb{S}^{q}$ such that $\left\|H_{t}-H\right\|_{F} \rightarrow 0$ as $t \rightarrow 0$,

$$
\lim _{t \rightarrow 0} \frac{\operatorname{tr}\left[\left\{\left(R+t H_{t}\right)_{0}^{1 / 2}\left(R+t H_{t}\right)_{m}\left(R+t H_{t}\right)_{0}^{1 / 2}\right\}^{1 / 2}-\left(R_{0}^{1 / 2} R_{m} R_{0}^{1 / 2}\right)^{1 / 2}\right]}{t}=\operatorname{tr}\left(\Upsilon_{2} H\right)
$$

with $\left(R+t H_{t}\right)_{0}$ having the same $d_{i} \times d_{i}$ diagonal blocks as $R+t H_{t}$ but zero off-diagonal blocks, $\left(R+t H_{t}\right)_{m}$ the matrix in (7) with $R$ replaced by $R+t H_{t}$, and with $\Upsilon_{2}$ defined in (17).

Proof. Recall the proof of Lemma 3. Keep the same definition for the map $M$ and define

$$
g:\left(\mathbb{S}_{>}^{d_{1}} \times \cdots \times \mathbb{S}_{>}^{d_{k}},\|\cdot\|_{F}\right) \rightarrow(\mathbb{R},|\cdot|):\left(B_{1}, \ldots, B_{k}\right) \mapsto \sum_{j=1}^{d_{k}}\left(\eta_{j, 11}^{2}+\cdots+\eta_{j, k k}^{2}\right)^{1 / 2}
$$

with again $\eta_{j, i i}$ the eigenvalues of $B_{i}$ in decreasing order for $i=1, \ldots, k$ and $j=1, \ldots, d_{i}$, and putting $\eta_{j, i i}=0$ if
$j=d_{i}+1, \ldots, d_{k}$. Again applying the chain rule yields, in a very similar way and using the same notations,

$$
\begin{aligned}
& \lim _{t \rightarrow 0} \frac{g\left(M\left(R_{11}+t H_{t, 11}, \ldots, R_{k k}+t H_{t, k k}\right)\right)-g\left(M\left(R_{11}, \ldots, R_{k k}\right)\right)}{t} \\
= & \sum_{i=1}^{k}\left(\sum_{j=1}^{d_{i}} \lambda_{j, i i}\left(\lambda_{j, 11}^{2}+\cdots+\lambda_{j, k k}^{2}\right)^{1 / 2}\left(U_{i i}^{T} H_{i i} U_{i i}\right)_{j j}\right) \\
= & \sum_{i=1}^{k} \operatorname{tr}\left(\widetilde{\Delta}_{i i} U_{i i}^{T} H_{i i} U_{i i}\right)=\operatorname{tr}\left(\Upsilon_{2} H\right) .
\end{aligned}
$$



# Proof of Theorem 1 

We start by showing the Fréchet differentiability of $D_{1}$ and $D_{2}$. To this end, we prove that they are Hadamard differentiable on $\mathbb{S}_{>}^{q}$ with

$$
\lim _{t \rightarrow 0} \frac{D_{r}\left(R+t H_{t}\right)-D_{r}(R)}{t}=\operatorname{tr}\left(M_{r} H\right)
$$

for $r \in\{1,2\}$ and $H_{t} \in \mathbb{S}^{q}$ for $t>0$ and $H \in \mathbb{S}^{q}$ such that $\left\|H_{t}-H\right\|_{F} \rightarrow 0$ as $t \rightarrow 0$.

## Differentiability of $D_{1}$

Consider the function

$$
f:(0, \infty)^{k+2} \rightarrow \mathbb{R}:\left(x_{1}, \ldots, x_{k}, y, z\right) \mapsto \frac{\sum_{i=1}^{k} x_{i}-y}{\sum_{i=1}^{k} x_{i}-z}
$$

It is then quickly seen that $D_{1}(R)=f\left(x_{1}, \ldots, x_{k}, y, z\right)$ and $D_{1}\left(R+t H_{t}\right)=f\left(x_{1}^{t}, \ldots, x_{k}^{t}, y^{t}, z^{t}\right)$ with

$$
\begin{array}{ll}
y=\operatorname{tr}\left(R^{1 / 2}\right), & z=\operatorname{tr}\left(R_{m}^{1 / 2}\right) \\
x_{i}=\operatorname{tr}\left(R_{i i}^{1 / 2}\right), & y^{t}=\operatorname{tr}\left(\left(R+t H_{t}\right)^{1 / 2}\right) \\
x_{i}^{t}=\operatorname{tr}\left(\left(R+t H_{t}\right)_{i i}^{1 / 2}\right), & z^{t}=\operatorname{tr}\left(\left(R+t H_{t}\right)_{m}^{1 / 2}\right)
\end{array}
$$

for $i=1, \ldots, k$. Here, $\left(R+t H_{t}\right)_{i i}$ is the $d_{i} \times d_{i}$ diagonal block of $R+t H_{t}$ and $\left(R+t H_{t}\right)_{m}$ the matrix in (7) with $R$ replaced by $R+t H_{t}$. Since the matrix $R$ is positive definite, there exists a unique square root matrix $R^{1 / 2}$ having eigenvalues on the sector $\{z \in \mathbb{C}:-\pi / 2<\arg (z)<\pi / 2\}$ of the complex plane, where $\arg (z)$ denotes the argument of the complex number $z$. Moreover, since the mapping $z \mapsto z^{1 / 2}$ is infinitely differentiable on this sector, it follows from Theorem 3.8 of [25] that the Fréchet derivative of the matrix function $R \mapsto R^{1 / 2}$ exists. Furthermore, Lemma 2.2 in [7] tells us that this derivative in the direction of $H$ is equal to the unique solution $Y$ of the Sylvester equation

$$
R^{1 / 2} Y+Y R^{1 / 2}=H
$$

Hence, the Hadamard derivative in the direction of $H$ also equals $Y$ and from (C.24) we obtain

$$
\operatorname{tr}(Y)=\operatorname{tr}\left(R^{-1 / 2} H\right)-\operatorname{tr}\left(R^{-1 / 2} Y R^{1 / 2}\right)=\operatorname{tr}\left(R^{-1 / 2} H\right)-\operatorname{tr}(Y)
$$

i.e., $\operatorname{tr}(Y)=\operatorname{tr}\left(R^{-1 / 2} H\right) / 2$. This (and a similar reasoning with $R_{i i}$ instead of $R$ ) shows that

$$
\lim _{t \rightarrow 0} \frac{y^{t}-y}{t}=\frac{1}{2} \operatorname{tr}\left(R^{-1 / 2} H\right) \quad \text { and } \quad \lim _{t \rightarrow 0} \frac{x_{i}^{t}-x_{i}}{t}=\frac{1}{2} \operatorname{tr}\left(R_{i i}^{-1 / 2} H_{i i}\right)
$$

for $i=1, \ldots, k$, where we used the notation $H_{i i}$ for the $d_{i} \times d_{i}$ diagonal block of $H$. Also, Lemma 3 guarantees that

$$
\lim _{t \rightarrow 0} \frac{z^{t}-z}{t}=\frac{1}{2} \operatorname{tr}\left(\Upsilon_{1} H\right)
$$

Putting this together, we see that the Fréchet derivative of the map

$$
g: \mathbb{S}^{q} \rightarrow(0, \infty)^{k+2}: A \mapsto\left(\operatorname{tr}\left(A_{11}^{1 / 2}\right), \ldots, \operatorname{tr}\left(A_{k k}^{1 / 2}\right), \operatorname{tr}\left(A^{1 / 2}\right), \operatorname{tr}\left(A_{m}^{1 / 2}\right)\right)
$$

at $R$ in the direction of $H$ equals

$$
\left(\frac{1}{2} \operatorname{tr}\left(R_{11}^{-1 / 2} H_{11}\right), \ldots, \frac{1}{2} \operatorname{tr}\left(R_{k k}^{-1 / 2} H_{k k}\right), \frac{1}{2} \operatorname{tr}\left(R^{-1 / 2} H\right), \frac{1}{2} \operatorname{tr}\left(\Upsilon_{1} H\right)\right)
$$

which we will call $\Delta(H)$. Next, the Jacobian matrix of the function $f$ is given by

$$
J_{f}=\left(\begin{array}{llll}
\frac{\partial f}{\partial x_{1}} & \cdots & \frac{\partial f}{\partial x_{k}} & \frac{\partial f}{\partial y} \\
& \frac{\partial f}{\partial z}
\end{array}\right)=\left(\begin{array}{cccc}
\frac{y-z}{\left(x_{1}+\cdots+x_{k}-z\right)^{2}} & \cdots & \frac{y-z}{\left(x_{1}+\cdots+x_{k}-z\right)^{2}} & -\frac{1}{x_{1}+\cdots+x_{k}-z} \\
x_{1}+\cdots x_{k}-y & \left(x_{1}+\cdots+x_{k}-z\right)^{2}
\end{array}\right)
$$



such that the Fréchet derivative (being nothing more than a total derivative) of the function $f$ at $g(\mathbf{R})$ in the direction of $\Delta(\mathbf{H})$ is equal to

$$
\begin{aligned}
\left.\mathbf{J}_{f}\right|_{g(\mathbf{R})} \Delta(\mathbf{H})^{T} & =\sum_{\ell=1}^{k}\left[\operatorname{tr}\left(\mathbf{R}^{1 / 2}\right)-\operatorname{tr}\left(\mathbf{R}_{m}^{1 / 2}\right)\left\{\sum_{i=1}^{k} \operatorname{tr}\left(\mathbf{R}_{i i}^{1 / 2}\right)-\operatorname{tr}\left(\mathbf{R}_{m}^{1 / 2}\right)\right\}^{2} \frac{1}{2} \operatorname{tr}\left(\mathbf{R}_{\ell \ell}^{-1 / 2} \mathbf{H}_{\ell \ell}\right)\right] \\
& -\frac{1}{\sum_{i=1}^{k} \operatorname{tr}\left(\mathbf{R}_{i i}^{1 / 2}\right)-\operatorname{tr}\left(\mathbf{R}_{m}^{1 / 2}\right)} \frac{1}{2} \operatorname{tr}\left(\mathbf{R}^{-1 / 2} \mathbf{H}\right)+\frac{\sum_{i=1}^{k} \operatorname{tr}\left(\mathbf{R}_{i i}^{1 / 2}\right)-\operatorname{tr}\left(\mathbf{R}^{1 / 2}\right)}{\left\{\sum_{i=1}^{k} \operatorname{tr}\left(\mathbf{R}_{i i}^{1 / 2}\right)-\operatorname{tr}\left(\mathbf{R}_{m}^{1 / 2}\right)\right\}^{2}} \frac{1}{2} \operatorname{tr}\left(\Upsilon_{1} \mathbf{H}\right) \\
& =\frac{1}{2 C_{1}}\left(1-D_{1}(\mathbf{R})\right) \operatorname{tr}\left(\mathbf{R}_{0}^{-1 / 2} \mathbf{H}\right)-\frac{1}{2 C_{1}} \operatorname{tr}\left(\mathbf{R}^{-1 / 2} \mathbf{H}\right)+\frac{1}{2 C_{1}} D_{1}(\mathbf{R}) \operatorname{tr}\left(\Upsilon_{1} \mathbf{H}\right) \\
& =\frac{1}{2 C_{1}}\left(-\operatorname{tr}\left(\mathbf{R}^{-1 / 2} \mathbf{H}\right)+\left(1-D_{1}(\mathbf{R})\right) \operatorname{tr}\left(\mathbf{R}_{0}^{-1 / 2} \mathbf{H}\right)+D_{1}(\mathbf{R}) \operatorname{tr}\left(\Upsilon_{1} \mathbf{H}\right)\right)
\end{aligned}
$$

where we used the definition of $D_{1}$ and the fact that $\sum_{\ell=1}^{k} \operatorname{tr}\left(\mathbf{R}_{\ell \ell}^{-1 / 2} \mathbf{H}_{\ell \ell}\right)=\operatorname{tr}\left(\mathbf{R}_{0}^{-1 / 2} \mathbf{H}\right)$. The result follows from the linearity of the trace operator and applying the chain rule to $f(g(\mathbf{R}))=D_{1}(\mathbf{R})$.

# Differentiability of $D_{2}$ 

Consider the function

$$
f:(0, \infty)^{3} \rightarrow \mathbb{R}:(x, y, z) \mapsto \frac{z-x}{z-y}
$$

Then, $D_{2}(\mathbf{R})=f(x, y, z)$ and $D_{2}\left(\mathbf{R}+t \mathbf{H}_{t}\right)=f\left(x_{t}, y_{t}, z_{t}\right)$, where

$$
x=\operatorname{tr}\left\{\left(\mathbf{R}_{0}^{1 / 2} \mathbf{R} \mathbf{R}_{0}^{1 / 2}\right)^{1 / 2}\right\}, y=\operatorname{tr}\left\{\left(\mathbf{R}_{0}^{1 / 2} \mathbf{R}_{m} \mathbf{R}_{0}^{1 / 2}\right)^{1 / 2}\right\}, z=\operatorname{tr}(\mathbf{R})
$$

and similarly for $x_{t}, y_{t}$ and $z_{t}$ with $\mathbf{R}+t \mathbf{H}_{t}$ instead of $\mathbf{R}$. From Lemma 4 and Lemma 5, we have

$$
\lim _{t \rightarrow 0} \frac{x_{t}-x}{t}=\frac{1}{2} \operatorname{tr}\left\{\left(\mathbf{J}_{0}+\mathbf{J}_{-1}\right) \mathbf{H}\right\}
$$

and

$$
\lim _{t \rightarrow 0} \frac{y_{t}-y}{t}=\operatorname{tr}\left(\Upsilon_{2} \mathbf{H}\right)
$$

Evidently

$$
\lim _{t \rightarrow 0} \frac{z_{t}-z}{t}=\operatorname{tr}(\mathbf{H})
$$

Hence, the Fréchet derivative of the map

$$
g: \mathbf{S}_{q} \rightarrow(0, \infty)^{3}: \mathbf{A} \mapsto\left(\operatorname{tr}\left\{\left(\mathbf{A}_{0}^{1 / 2} \mathbf{A} \mathbf{A}_{0}^{1 / 2}\right)^{1 / 2}\right\}, \operatorname{tr}\left\{\left(\mathbf{A}_{0}^{1 / 2} \mathbf{A}_{m} \mathbf{A}_{0}^{1 / 2}\right)^{1 / 2}\right\}, \operatorname{tr}(\mathbf{A})\right)
$$

at $\mathbf{R}$ in the direction of $\mathbf{H}$ equals

$$
\left(\frac{1}{2} \operatorname{tr}\left\{\left(\mathbf{J}_{0}+\mathbf{J}_{-1}\right) \mathbf{H}\right\}, \operatorname{tr}\left(\Upsilon_{2} \mathbf{H}\right), \operatorname{tr}(\mathbf{H})\right)
$$

which we will call $\Delta(\mathbf{H})$. The Jacobian matrix of $f$ is given by

$$
\mathbf{J}_{f}=\left(\frac{\partial f}{\partial x} \frac{\partial f}{\partial y} \frac{\partial f}{\partial z}\right)=\left(\begin{array}{ccc}
-\frac{1}{z-y} & \frac{z-x}{(z-y)^{2}} & \frac{x-y}{(z-y)^{2}}
\end{array}\right)
$$



such that the total derivative of $f$ at $\mathrm{g}(\mathbf{R})$ in the direction of $\Delta(\mathbf{H})$ becomes

$$
\begin{aligned}
\left.\boldsymbol{J} f\right|_{\mathbf{g}(\mathbf{R})} \Delta(\mathbf{H})^{T}= & \frac{1}{2} \operatorname{tr}\left\{\left(\mathbf{J}_{0}+\mathbf{J}^{-1}\right) \mathbf{H}\right\} \operatorname{tr}\left\{\left(\mathbf{R}_{0}^{1 / 2} \mathbf{R} \mathbf{R}_{0}^{1 / 2}\right)^{1 / 2}\right\}-\operatorname{tr}(\mathbf{R}) \\
& +\operatorname{tr}(\mathbf{R})-\operatorname{tr}\left\{\left(\mathbf{R}_{0}^{1 / 2} \mathbf{R} \mathbf{R}_{0}^{1 / 2}\right)^{1 / 2}\right\}\left[\operatorname{tr}(\mathbf{R})-\operatorname{tr}\left\{\left(\mathbf{R}_{0}^{1 / 2} \mathbf{R} \mathbf{R}_{0}^{1 / 2}\right)^{1 / 2}\right\}\right]^{2} \operatorname{tr}\left(\Upsilon_{2} \mathbf{H}\right) \\
& +\operatorname{tr}\left\{\left(\mathbf{R}_{0}^{1 / 2} \mathbf{R} \mathbf{R}_{0}^{1 / 2}\right)^{1 / 2}\right\}-\operatorname{tr}\left\{\left(\mathbf{R}_{0}^{1 / 2} \mathbf{R m R}_{0}^{1 / 2}\right)^{1 / 2}\right\}\left[\operatorname{tr}(\mathbf{R})-\operatorname{tr}\left\{\left(\mathbf{R}_{0}^{1 / 2} \mathbf{R} \mathbf{R}_{0}^{1 / 2}\right)^{1 / 2}\right\}\right]^{2} \operatorname{tr}(\mathbf{H}) \\
= & \frac{1}{C_{2}}\left(-\frac{1}{2} \operatorname{tr}\left\{\left(\mathbf{J}_{0}+\mathbf{J}^{-1}\right) \mathbf{H}\right\}+D_{2}(\mathbf{R}) \operatorname{tr}\left(\Upsilon_{2} \mathbf{H}\right)+\left(1-D_{2}(\mathbf{R})\right) \operatorname{tr}(\mathbf{H})\right)
\end{aligned}
$$

Applying the delta method
Next, we consider the estimator $\widehat{\mathbf{R}}_{n}$. Theorem 3.1 in [28] tells us that

$$
\sqrt{n}\left(\widehat{\mathbf{R}}_{n}-\mathbf{R}\right)-\frac{1}{\sqrt{n}} \sum_{\ell=1}^{n}\left[\mathbf{Z}^{(\ell)}\left(\mathbf{Z}^{(\ell)}\right)^{T}-\frac{1}{2}\left\{\operatorname{diag}\left(\mathbf{Z}^{(\ell)}\left(\mathbf{Z}^{(\ell)}\right)^{T}\right) \mathbf{R}+\mathbf{R} \operatorname{diag}\left(\mathbf{Z}^{(\ell)}\left(\mathbf{Z}^{(\ell)}\right)^{T}\right)\right\}\right] \xrightarrow{p} 0_{q \times q}
$$

as $n \rightarrow \infty$, where $\mathbf{Z}^{(\ell)}=\left(\mathbf{Z}_{1}^{(\ell)}, \ldots, \mathbf{Z}_{k}^{(\ell)}\right)^{T}$, with $\mathbf{Z}_{i}^{(\ell)}=\left(\mathbf{Z}_{i 1}^{(\ell)}, \ldots, \mathbf{Z}_{i d_{i}}^{(\ell)}\right)$ for $i \in\{1, \ldots, k\}$, for $\ell \in\{1, \ldots, n\}$ is a sample from the $N_{q}\left(\mathbf{0}_{q}, \mathbf{R}\right)$ distribution. The same expansion holds when $\widehat{\mathbf{R}}_{n}$ is the empirical correlation matrix of $\mathbf{Z}^{(1)}, \ldots, \mathbf{Z}^{(n)}$, see, e.g., Lemma 8 in [36]. Hence

$$
\sqrt{n}\left(\widehat{\mathbf{R}}_{n}-\mathbf{R}\right)-\sqrt{n}\left(\boldsymbol{\phi}\left(\frac{1}{n} \sum_{\ell=1}^{n} \mathbf{Z}^{(\ell)}\left(\mathbf{Z}^{(\ell)}\right)^{T}\right)-\mathbf{R}\right) \xrightarrow{p} 0_{q \times q}
$$

as $n \rightarrow \infty$, i.e., making use of the empirical correlation matrix based on a true Gaussian sample or based on a pseudo Gaussian sample, results in the same asymptotic expansion. Suppose further that $\mathbf{R}=\mathbf{U} \boldsymbol{\Lambda} \mathbf{U}^{T}$ is the eigendecomposition of $\mathbf{R}$. Then $\mathbf{Z}^{(\ell)}=\mathbf{U} \boldsymbol{\Lambda}^{1 / 2} \boldsymbol{\epsilon}^{(\ell)}$ for $\ell \in\{1, \ldots, n\}$ and $\boldsymbol{\epsilon}^{(1)}, \ldots, \boldsymbol{\epsilon}^{(n)}$ a sample from $N_{q}\left(\mathbf{0}_{q}, \mathbf{I}_{q}\right)$. From Lemma 7 of [36], we have

$$
\mathbf{W}_{n}=\frac{1}{\sqrt{n}} \sum_{l=1}^{n}\left\{\boldsymbol{\epsilon}^{(\ell)}\left(\boldsymbol{\epsilon}^{(\ell)}\right)^{T}-\mathbf{I}_{q}\right\} \xrightarrow{d} \mathbf{W}
$$

as $n \rightarrow \infty$, where $\mathbf{W}$ is a random symmetric matrix with $\mathbf{W}_{j k} \sim N(0,2)$ if $j=k \in\{1, \ldots, q\}$ and $\mathbf{W}_{j k} \sim N(0,1)$ if $1 \leq j<k \leq q$ independently (and similarly for $k<j$ ). Moreover, for $\mathbf{A}, \mathbf{B} \in \mathbf{S}_{q}$, it holds that

$$
E(\operatorname{tr}(\mathbf{A} \mathbf{W}) \operatorname{tr}(\mathbf{B} \mathbf{W}))=2 \operatorname{tr}(\mathbf{A B})
$$

We find

$$
\mathbf{U} \boldsymbol{\Lambda}^{1 / 2} \mathbf{W}_{n} \boldsymbol{\Lambda}^{1 / 2} \mathbf{U}^{T}=\sqrt{n}\left(\frac{1}{n} \sum_{\ell=1}^{n}\left(\mathbf{Z}^{(\ell)}\left(\mathbf{Z}^{(\ell)}\right)^{T}\right)-\mathbf{R}\right) \xrightarrow{d} \mathbf{U} \boldsymbol{\Lambda}^{1 / 2} \mathbf{W} \boldsymbol{\Lambda}^{1 / 2} \mathbf{U}^{T}
$$

as $n \rightarrow \infty$. Applying the delta method (and using that $\boldsymbol{\phi}(\mathbf{R})=\mathbf{D}_{R}^{-1 / 2} \mathbf{R D}_{R}^{-1 / 2}=\mathbf{R}$ ), we obtain

$$
\begin{aligned}
\sqrt{n}\left(\mathbf{D}_{\mathbf{r}}\left(\widehat{\mathbf{R}}_{n}\right)-\mathbf{D}_{\mathbf{r}}(\mathbf{R})\right) & \xrightarrow{d} \operatorname{tr}\left\{\left(\math

# Appendix D. Proof of Proposition 4 

Consider the estimator given in (10). Notice first of all that the deterministic correction

$$
\left[\frac{1}{n} \sum_{\ell=1}^{n}\left(\Phi^{-1}\left(\frac{\ell}{n+1}\right)\right)^{2}\right]^{-1}=1+O\left(n^{-1} \ln (n)\right)
$$

is asymptotically insignificant. Suppose that $\sup _{n} \lambda_{\max }\left(R_{n}\right) \leq \epsilon_{0}^{-1}$ for a certain $\epsilon_{0}>0$. Fix now $i, m \in\{1, \ldots, k\}$, $j \in\left\{1, \ldots, d_{i}\right\}$ and $t \in\left\{1, \ldots, d_{m}\right\}$. We desire to find a non-asymptotic deviation inequality

$$
\mathbb{P}\left[\left|\frac{1}{n} \sum_{\ell=1}^{n}\left(\widehat{Z}_{i j}^{(\ell)} \widehat{Z}_{m t}^{(\ell)}-\rho_{i j, m t}\right)\right| \geq \epsilon\right] \leq f(\epsilon, n)
$$

holding for $0<\epsilon \leq \delta$, where $\delta>0$ is a positive constant only depending on $\epsilon_{0}$. Denote by $\widehat{F}_{i j}^{*}=n /(n+1) \widehat{F}_{i j}$ the rescaled empirical cdf of $X_{i j}$, and similarly for $X_{m t}$, en let $\widehat{H}$ be the joint empirical cdf of $\left(X_{i j}^{(1)}, X_{m t}^{(1)}\right), \ldots,\left(X_{i j}^{(n)}, X_{m t}^{(n)}\right)$, and $H$ be the true cdf of $\left(X_{i j}, X_{m t}\right)$. Recall that $\left(X_{i j}, X_{m t}\right)$ has a Gaussian copula, meaning that

$$
\left(\left(\Phi^{-1} \circ F_{i j}\right)\left(X_{i j}\right),\left(\Phi^{-1} \circ F_{m t}\right)\left(X_{m t}\right)\right) \sim \Phi_{G}
$$

where $\Phi_{G}$ stands for a bivariate normal distribution with means zero, unit variances and correlation $\rho_{i j, m t}$. We also need the Dvoretzky-Kiefer-Wolfowitz inequality (see, e.g., [34]):

$$
\mathbb{P}\left[\sup _{x \in \mathbb{R}}\left|\widehat{F}_{i j}(x)-F_{i j}(x)\right| \geq \epsilon\right] \leq 2 \exp \left(-2 n \epsilon^{2}\right)
$$

for any $\epsilon>0$. Now, consider the decomposition

$$
\begin{aligned}
& \frac{1}{n} \sum_{\ell=1}^{n}\left(\widehat{Z}_{i j}^{(\ell)} \widehat{Z}_{m t}^{(\ell)}-\rho_{i j, m t}\right) \\
& =\int_{\mathbb{R}^{2}} \Phi^{-1}\left(\widehat{F}_{i j}^{*}(x)\right) \Phi^{-1}\left(\widehat{F}_{m t}^{*}(y)\right) \mathrm{d} \widehat{H}(x, y)-\int_{\mathbb{R}^{2}} \Phi^{-1}\left(F_{i j}(x)\right) \Phi^{-1}\left(F_{m t}(y)\right) \mathrm{d} H(x, y) \\
& =A_{1 n}+A_{2 n}+A_{3 n}+B_{1 n}+B_{2 n}+R_{n}
\end{aligned}
$$

where (denoting $\varphi$ for the standard normal density function)

$$
\begin{aligned}
A_{1 n} & =\int_{\mathbb{R}^{2}} \Phi^{-1}\left(F_{i j}(x)\right) \Phi^{-1}\left(F_{m t}(y)\right) \mathrm{d}(\widehat{H}-H)(x, y) \\
A_{2 n} & =\int_{\mathbb{R}^{2}} \widehat{F}_{i j}^{*}(x)-F_{i j}(x) \frac{\varphi\left(\Phi^{-1}\left(F_{i j}(x)\right)\right)}{\Phi^{-1}\left(F_{m t}(y)\right)} \mathrm{d} H(x, y) \\
A_{3 n} & =\int_{\mathbb{R}^{2}} \widehat{F}_{m t}^{*}(y)-F_{m t}(y) \frac{\varphi\left(\Phi^{-1}\left(F_{m t}(y)\right)\right)}{\Phi^{-1}\left(F_{i j}(x)\right)} \mathrm{d} H(x, y)
\end{aligned}
$$

$$
\begin{aligned}
B_{1 n} & =\int_{\mathbb{R}^{2}}\left\{\Phi^{-1}\left(\widehat{F}_{i j}^{*}(x)\right)-\Phi^{-1}\left(F_{i j}(x)\right)\right\} \Phi^{-1}\left(F_{m t}(y)\right) \mathrm{d} \widehat{H}(x, y)-A_{2 n} \\
B_{2 n} & =\int_{\mathbb{R}^{2}}\left\{\Phi^{-1}\left(\widehat{F}_{m t}^{*}(y)\right)-\Phi^{-1}\left(F_{m t}(y)\right)\right\} \Phi^{-1}\left(F_{i j}(x)\right) \mathrm{d} \widehat{H}(x, y)-A_{3 n} \\
R_{n} & =\int_{\mathbb{R}^{2}}\left\{\Phi^{-1}\left(\widehat{F}_{i j}^{*}(x)\right)-\Phi^{-1}\left(F_{i j}(x)\right)\right\}\left\{\Phi^{-1}\left(\widehat{F}_{m t}^{*}(y)\right)-\Phi^{-1}\left(F_{m t}(y)\right)\right\} \mathrm{d} \widehat{H}(x, y)
\end{aligned}
$$

Lemma A.3. in [3] tells us that

$$
\mathbb{P}\left[\left|A_{1 n}\right| \geq \epsilon\right] \leq C_{1} \exp \left(-C_{2} n \epsilon^{2}\right)
$$

for $\epsilon \leq \delta_{1}$, where $C_{1}, C_{2}>0$ and $\delta_{1}>0$ only depend on $\epsilon_{0}$. Next, since

$$
\mathrm{d} H(x, y)=\varphi_{G}\left(\Phi^{-1}\left(F_{i j}(x)\right), \Phi^{-1}\left(F_{m t}(y)\right)\right) \mathrm{d} \Phi^{-1}\left(F_{i j}(x)\right) \mathrm{d} \Phi^{-1}\left(F_{m t}(y)\right)
$$



with $\varphi_{G}$ the density of $\Phi_{G}$, we see that

$$
A_{2 n}=\int_{\mathbb{R}^{2}} \frac{\widehat{F}_{i j}^{*}(x)-F_{i j}(x)}{\varphi\left(\Phi^{-1}\left(F_{i j}(x)\right)\right)} \Phi^{-1}\left(F_{m t}(y)\right) \varphi_{G}\left(\Phi^{-1}\left(F_{i j}(x)\right), \Phi^{-1}\left(F_{m t}(y)\right)\right) \mathrm{d} \Phi^{-1}\left(F_{i j}(x)\right) \mathrm{d} \Phi^{-1}\left(F_{m t}(y)\right)
$$

where

$$
\begin{aligned}
& \int_{\mathbb{R}} \Phi^{-1}\left(F_{m t}(y)\right) \varphi_{G}\left(\Phi^{-1}\left(F_{i j}(x)\right), \Phi^{-1}\left(F_{m t}(y)\right)\right) \mathrm{d} \Phi^{-1}\left(F_{m t}(y)\right) \\
& =\int_{\mathbb{R}} \varphi\left(\Phi^{-1}\left(F_{i j}(x)\right)\right) \varphi_{G}\left(\Phi^{-1}\left(F_{i j}(x)\right), s\right) \varphi\left(\Phi^{-1}\left(F_{i j}(x)\right)\right) s \mathrm{~d} s \\
& =\rho_{i j, m t} \varphi\left(\Phi^{-1}\left(F_{i j}(x)\right)\right) \Phi^{-1}\left(F_{i j}(x)\right)
\end{aligned}
$$

since $\mathbb{E}\left(X_{2} \mid X_{1}=x_{1}\right)=\rho x_{1}$ when $\left(X_{1}, X_{2}\right)$ follows a bivariate standard normal distribution with correlation $\rho$. Hence

$$
\begin{aligned}
A_{2 n} & =\rho_{i j, m t} \int_{\mathbb{R}} \Phi^{-1}\left(F_{i j}(x)\right)\left(\widehat{F}_{i j}^{*}(x)-F_{i j}(x)\right) \mathrm{d} \Phi^{-1}\left(F_{i j}(x)\right) \\
& =-\frac{\rho_{i j, m t}}{2} \int_{\mathbb{R}}\left\{\Phi^{-1}\left(F_{i j}(x)\right)\right\}^{2} \mathrm{~d}\left(\widehat{F}_{i j}^{*}-F_{i j}\right)(x) \\
& =-\frac{\rho_{i j, m t}}{2} \frac{1}{n} \sum_{\ell=1}^{n}\left(\Phi^{-1}\left(F_{i j}\left(X_{i j}^{(\ell)}\right)\right)\right)^{2}-1) \\
& =-\frac{\rho_{i j, m t}}{2} \frac{1}{n} \sum_{\ell=1}^{n}\left(V_{\ell}^{2}-1\right)
\end{aligned}
$$

where we did partial integration, and $V_{\ell} \sim \chi_{1}^{2}$ for $\ell=1, \ldots, n$. Hence, using Theorem 3.2 on page 45 of [41] (noting that condition $(\mathcal{P})(3.12)$ on page 45 holds for $\chi_{1}^{2}$, see also the proof of Lemma A.3. in [3]), we have

$$
\mathbb{P}\left[\left|A_{2 n}\right| \geq \epsilon\right] \leq C_{3} \exp \left(-C_{4} n \epsilon^{2}\right)
$$

for $\epsilon \leq \delta_{2}$, where $C_{3}, C_{4}$ and $\delta_{2}>0$ only depend on $\epsilon_{0}$. A very similar argument holds for $A_{3 n}$.
Next, we deal with the term $B_{1 n}$. By symmetry, the term $B_{2 n}$ can be dealt with similarly. We use the mean value theorem, giving that

$$
\Phi^{-1}\left(\widehat{F}_{i j}^{*}(x)\right)-\Phi^{-1}\left(F_{i j}(x)\right)=\frac{\widehat{F}_{i j}^{*}(x)-F_{i j}(x)}{\varphi\left(\Phi^{-1}\left(\widetilde{F}_{i j}^{*}(x)\right)\right)}
$$

for a certain $\widetilde{F}_{i j}^{*}(x)$ satisfying $\left|\widetilde{F}_{i j}^{*}(x)-F_{i j}(x)\right| \leq\left|\widehat{F}_{i j}^{*}(x)-F_{i j}(x)\right|$. Of course, $\left|\Phi^{-1}(t)\right| \rightarrow \infty$ when $t \rightarrow 0$ or $t \rightarrow 1$, and $\varphi(t) \rightarrow 0$ when $|t| \rightarrow \infty$, so we will need to further split up $B_{1 n}$ by defining the set $\mathbb{M}_{\eta}=\mathbb{M}_{\eta_{1}} \times \mathbb{M}_{\eta_{2}}$, where

$$
\begin{aligned}
& \mathbb{M}_{\eta_{1}}=\left[F_{i j}^{-1}(\eta), F_{i j}^{-1}(1-\eta)\right] \\
& \mathbb{M}_{\eta_{2}}=\left[F_{m t}^{-1}(\eta), F_{m t}^{-1}(1-\eta)\right]
\end{aligned}
$$

for a certain small $\eta>0$. Doing so, we can write

$$
B_{1 n}=B_{\eta_{1} 1 n}+B_{\eta_{2} 1 n}+B_{\eta_{3} 1 n}+B_{\eta_{4} 1 n}
$$



where

$$
\begin{aligned}
& B_{\eta 11 n}=\int_{M_{\bar{\eta}_{n}}^{\bar{C}}}\left\{\Phi^{-1}\left(\widehat{\mathbb{F}}_{i j}^{*}(x)\right)-\Phi^{-1}\left(\mathbb{F}_{i j}(x)\right)\right\} \Phi^{-1}\left(\mathbb{F}_{m t}(y)\right) \mathrm{d} \widehat{H}(x, y) \\
& B_{\eta 21 n}=\int_{M_{\eta}}\left\{\left(\widehat{\mathbb{F}}_{i j}^{*}(x)-\mathbb{F}_{i j}(x)\right) \varphi\left(\Phi^{-1}\left(\widetilde{\mathbb{F}}_{i j}^{*}(x)\right)\right)-\left(\widehat{\mathbb{F}}_{i j}^{*}(x)-\mathbb{F}_{i j}(x)\right) \varphi\left(\Phi^{-1}\left(\mathbb{F}_{i j}(x)\right)\right)\right\} \Phi^{-1}\left(\mathbb{F}_{m t}(y)\right) \mathrm{d} \widehat{H}(x, y) \\
& B_{\eta 31 n}=\int_{M_{\eta}}\left(\widehat{\mathbb{F}}_{i j}^{*}(x)-\mathbb{F}_{i j}(x)\right) \varphi\left(\Phi^{-1}\left(\mathbb{F}_{i j}(x)\right)\right) \Phi^{-1}\left(\mathbb{F}_{m t}(y)\right) \mathrm{d}(\widehat{H}-H)(x, y) \\
& B_{\eta 41 n}=\int_{M_{\eta}}\left(\widehat{\mathbb{F}}_{i j}^{*}(x)-\mathbb{F}_{i j}(x)\right) \varphi\left(\Phi^{-1}\left(\mathbb{F}_{i j}(x)\right)\right) \Phi^{-1}\left(\mathbb{F}_{m t}(y)\right) \mathrm{d} H(x, y)-A_{2 n} .
\end{aligned}
$$

Notice that we did not apply the mean value theorem in the term $B_{\eta 11 n}$, because we will decompose $R_{n}$ as

$$
R_{n}=R_{\eta 1 n}+R_{\eta 2 n}+R_{\eta 3 n}
$$

where

$$
\begin{aligned}
R_{\eta 1 n} & =\int_{M_{\bar{\eta}_{n}}^{\bar{C}}}\left\{\Phi^{-1}\left(\widehat{\mathbb{F}}_{i j}^{*}(x)\right)-\Phi^{-1}\left(\mathbb{F}_{i j}(x)\right)\right\} \Phi^{-1}\left(\mathbb{F}_{m t}^{*}(y)\right) \mathrm{d} \widehat{H}(x, y) \\
R_{\eta 2 n} & =-\int_{M_{\eta}^{\bar{e}_{n}}}\left\{\Phi^{-1}\left(\widehat{\mathbb{F}}_{i j}^{*}(x)\right)-\Phi^{-1}\left(\mathbb{F}_{i j}(x)\right)\right\} \Phi^{-1}\left(\mathbb{F}_{m t}(y)\right) \mathrm{d} \widehat{H}(x, y) \\
R_{\eta 3 n} & =\int_{M_{\eta}} \frac{\widehat{\mathbb{F}}_{i j}^{*}(x)-\mathbb{F}_{i j}(x)}{\varphi\left(\Phi^{-1}\left(\widetilde{\mathbb{F}}_{i j}^{*}(x)\right)\right)}\left\{\Phi^{-1}\left(\mathbb{F}_{m t}^{*}(y)\right)-\Phi^{-1}\left(\mathbb{F}_{m t}(y)\right)\right\} \mathrm{d} \widehat{H}(x, y)
\end{aligned}
$$

such that $B_{\eta 11 n}$ and $R_{\eta 2 n}$ cancel each other out. As for $B_{\eta 21 n}$, it holds almost surely that

$$
\left|B_{\eta 21 n}\right| \leq \sup _{x \in \mathbb{R}}\left|\widehat{\mathbb{F}}_{i j}^{*}(x)-\mathbb{F}_{i j}(x)\right| \sup _{x \in M_{\eta_{1}}}\left|\frac{1}{\varphi\left(\Phi^{-1}\left(\widetilde{\mathbb{F}}_{i j}^{*}(x)\right)\right)}-\frac{1}{\varphi\left(\Phi^{-1}\left(\mathbb{F}_{i j}(x)\right)\right)}\right| \sup _{y \in M_{\eta_{2}}} \Phi^{-1}\left(\mathbb{F}_{m t}(y)\right)
$$

The function $\Phi^{-1} \circ \mathbb{F}_{m t}$ is uniformly bounded on $M_{\eta_{2}}$ and since $\varphi \circ \Phi^{-1}$ is continuous, it is uniformly continuous on $M_{\eta_{1}}$. This, and the fact that $\left|\widetilde{\mathbb{F}}_{i j}^{*}-\mathbb{F}_{i j}\right| \leq\left|\widehat{\mathbb{F}}_{i j}^{*}-\mathbb{F}_{i j}\right|$, results in

$$
\left|B_{\eta 21 n}\right| \leq K \sup _{x \in \mathbb{R}}\left|\widehat{\mathbb{F}}_{i j}^{*}(x)-\mathbb{F}_{i j}(x)\right|
$$

almost surely for a certain $K>0$. Hence, using (D.2), we obtain

$$
\begin{aligned}
\mathbb{P}\left[\left|B_{\eta 21 n}\right| \geq \epsilon\right] & \leq \mathbb{P}\left[\sup _{x \in \mathbb{R}}\left|\widehat{\mathbb{F}}_{i j}^{*}(x)-\mathbb{F}_{i j}(x)\right| \geq \frac{\epsilon}{K}\right] \\
& \leq \mathbb{P}\left[\sup _{x \in \mathbb{R}}\left|\widehat{\mathbb{F}}_{i j}(x)-\mathbb{F}_{i j}(x)\right| \geq \frac{\epsilon}{2 K}\right]+\mathbb{P}\left[\sup _{x \in \mathbb{R}}\left|\widehat{\mathbb{F}}_{i j}^{*}(x)-\widehat{\mathbb{F}}_{i j}(x)\right| \geq \frac{\epsilon}{2 K}\right] \\
& \leq 2 \exp \left(-\frac{n \epsilon^{2}}{2 K^{2}}\right)+\mathbb{P}\left[\frac{1}{n+1} \geq \frac{\epsilon}{2 K}\right]
\end{aligned}
$$

Similar arguments hold for the terms $B_{\eta 31 n}, B_{\eta 41 n}$ and $R_{\eta 3 n}$.
The only term that is not discussed yet, is $R_{\eta 1 n}$. We want this term to converge to zero in probability when $\eta \rightarrow 0$ for every $n$. We can deal with this in a similar way as in Corollary 5.6. of [40] (in fact, we are even in the context of Section 6 on page 1133 since Assumption 2.3(b) holds), since the corresponding assumptions hold here (they are verified in the proof of Theorem 3.1 of [28]). In our setting, the key ingredient is that there exists $a=b=(1 / 2-\xi) / 2$ for a certain $0<\xi<1 / 2$ such that

$$
\left|\Phi^{-1}(t)\right| \leq M_{1} r^{a}(t)
$$

with

$$
r(t)=\frac{1}{t(1-t)}
$$



for all $t \in(0,1)$ and a certain $M_{1}>0$, i.e., $\left|\Phi^{-1}(t)\right| \rightarrow \infty$ as $t \rightarrow 0$ or $t \rightarrow 1$, but not too fast. Applying the mean value theorem again, we have

$$
\begin{aligned}
& \left|\Phi^{-1}\left(\widehat{F}_{i j}^{*}(\mathbf{x})\right)-\Phi^{-1}\left(F_{i j}(\mathbf{x})\right)\right|=\left|\left(\widehat{F}_{i j}^{*}(\mathbf{x})-F_{i j}(\mathbf{x})\right)\left[\Phi^{-1}\left(\widetilde{F}_{i j}^{*}(\mathbf{x})\right)\right]^{\prime}\right| \\
& \leq M_{1}\left|\widehat{F}_{i j}^{*}(\mathbf{x})-F_{i j}(\mathbf{x})\right|^{r a+1}\left(\widetilde{F}_{i j}^{*}(\mathbf{x})\right)
\end{aligned}
$$

Moreover, if we take $\widetilde{\epsilon}_{1}>0$ arbitrary, there exist $M_{2}, M_{3}, M_{4}>0$ such that, uniformly in $n$, the events

$$
\begin{aligned}
& \mathcal{E}_{1 n}=\left\{\left|\widehat{F}_{i j}^{*}-F_{i j}\right| \leq M_{2} r^{-1 / 2+\xi / 4}\left(F_{i j}\right)\right\} \\
& \mathcal{E}_{2 n}=\left\{r^{a}\left(\widehat{F}_{m_{t}}^{*}\right) \leq M_{3} r^{a}\left(F_{m_{t}}\right)\right\} \\
& \mathcal{E}_{3 n}=\left\{r^{a+1}\left(\widetilde{F}_{i j}^{*}\right) \leq M_{4} r^{a+1}\left(F_{i j}\right)\right\}
\end{aligned}
$$

satisfy $\mathbb{P}\left(\mathcal{E}^{C}\right)<\widetilde{\epsilon}_{1} / 2$, for $\mathcal{E}=\cap_{i=1}^{3} \mathcal{E}_{i n}$. Combining the inequalities, we also see that (similarly to expression (5.2) in [40])

$$
\mathbb{E}\left(\mathbf{1}(\mathcal{E})\left|R_{\eta_{1 n}}\right|\right) \leq M_{1}^{2} M_{2} M_{3} M_{4} \int_{\mathcal{M}_{\eta}^{C}} r^{a+1 / 2+\xi / 4}\left(F_{i j}(\mathbf{x})\right) r^{a}\left(F_{m_{t}}(\mathbf{y})\right) \mathrm{d} \mathcal{H}(\mathbf{x}, \mathbf{y})
$$

where $\mathbf{1}$ is the indicator function. By Hölder's inequality, the above integral is bounded by (noting that $\mathcal{M}_{\eta}^{C} \subset$ $\left.\left(\mathcal{M}_{\eta_{1}}^{C} \times \mathbb{R}) \cup\left(\mathbb{R} \times \mathcal{M}_{\eta_{2}}^{C}\right)\right)\right)$

$$
\begin{aligned}
& \left(\int_{(0, \eta) \cup(1-\eta, 1)} r^{p_{1}(a+1 / 2+\xi / 4)}(t) \mathrm{d} t\right)^{1 / p_{1}}\left(\int_{0}^{1} r^{q_{1} a}(t) \mathrm{d} t\right)^{1 / q_{1}} \\
& +\left(\int_{0}^{1} r^{p_{1}(a+1 / 2+\xi / 4)}(t) \mathrm{d} t\right)^{1 / p_{1}}\left(\int_{(0, \eta) \cup(1-\eta, 1)} r^{q_{1} a}(t) \mathrm{d} t\right)^{1 / q_{1}}<\infty
\end{aligned}
$$

where $p_{1}$ and $q_{1}$ are chosen such that $p_{1}^{-1}+q_{1}^{-1}=1, p_{1}(a+1 / 2+\xi / 4)<1$ and $q_{1} a<1$ (see equation (3.5) in [40] and corresponding explanation), making the integral bounded. Hence, by dominated convergence, we have that $\mathbf{1}(\mathcal{E})\left|R_{\eta_{1 n}}\right| \xrightarrow{p} 0$ as $\eta \rightarrow 0$ for each $n$. Hence, for our arbitrarily chosen $\widetilde{\epsilon}_{1}>0$, and another arbitrary $\widetilde{\epsilon}_{2}>0$, we see that

$$
\begin{aligned}
\mathbb{P}\left[\left|R_{\eta_{1 n}}\right|>\widetilde{\epsilon}_{2}\right] & =\mathbb{P}\left[\left|R_{\eta_{1 n}}\right|>\widetilde{\epsilon}_{2}, \mathbf{1}(\mathcal{E})=1\right]+\mathbb{P}\left[\left|R_{\eta_{1 n}}\right|>\widetilde{\epsilon}_{2}, \mathbf{1}(\mathcal{E})=0\right] \\
& =\mathbb{P}\left[\mathbf{1}(\mathcal{E})\left|R_{\eta_{1 n}}\right|>\widetilde{\epsilon}_{2}\right]+\mathbb{P}\left[\left|R_{\eta_{1 n}}\right|>\widetilde{\epsilon}_{2}, \mathbf{1}(\mathcal{E})=0\right] \\
& \leq \mathbb{P}\left[\mathbf{1}(\mathcal{E})\left|R_{\eta_{1 n}}\right|>\widetilde{\epsilon}_{2}\right]+\mathbb{P}[\mathbf{1}(\mathcal{E})=0] \\
& =\mathbb{P}\left[\mathbf{1}(\mathcal{E})\left|R_{\eta_{1 n}}\right|>\widetilde{\epsilon}_{2}\right]+\mathbb{P}\left[\mathcal{E}^{C}\right]<\frac{\widetilde{\epsilon}_{1}}{2}+\frac{\widetilde{\epsilon}_{1}}{2}=\widetilde{\epsilon}_{1}
\end{aligned}
$$

for $\eta$ small enough, i.e., $\left|R_{\eta_{1 n}}\right| \xrightarrow{p} 0$ as $\eta \rightarrow 0$ for all $n$. This means that $\mathbb{P}\left[\left|R_{\eta_{1 n}}\right| \geq \epsilon\right]$ can be made zero for every $n$ by letting $\eta \rightarrow 0$, and, combining everything, we have shown that a concentration inequality (D.1) holds. In simplified form, we can say that (D.1) holds with

$$
f(\epsilon, n)=K_{1} \exp \left(-K_{2} n \epsilon^{2}\right)+K_{3} \mathbb{P}\left[\frac{1}{n+1} \geq \frac{\epsilon}{K_{4}}\right]
$$

for $0<\epsilon \leq \delta$, where $K_{1}, K_{2}, K_{3}, K_{4}, \delta>0$ possibly only depend on $\epsilon_{0}$.
We now show that $\left\|\widehat{\mathcal{R}}_{n}-\mathcal{R}_{n}\right\|_{\infty}=O_{p}\left(\left\{\ln \left(q_{n}\right) / n\right\}^{1 / 2}\right)$. Take an arbitrary $\varepsilon>0$. Let $M, N>0$ be such that $2-K_{2} M^{2}<0, \frac{K_{1} q^{2-K_{2} M^{2}}}{n}<\varepsilon, M n^{-1 / 2} \ln \left(q_{n}\right)^{1 / 2} \leq \delta$ and $1 /(n+1)<M n^{-1 / 2} \

union bound, it holds that

$$
\begin{aligned}
\mathbb{P}\left[\left\|\widehat{\boldsymbol{R}}_{n}-\boldsymbol{R}_{n}\right\|_{\infty} n^{-1 / 2} \ln \left(q_{n}\right)^{1 / 2}>M\right] & =\mathbb{P}\left[\left\|\widehat{\boldsymbol{R}}_{n}-\boldsymbol{R}_{n}\right\|_{\infty}>M n^{-1 / 2} \ln \left(q_{n}\right)^{1 / 2}\right] \\
& \leq q_{n}^{2} K_{1} \exp \left\{-K_{2} n\left(M n^{-1 / 2} \ln \left(q_{n}\right)^{1 / 2}\right)^{2}\right\}+q_{n}^{2} K_{3} \mathbb{P}\left[\frac{1}{n+1} \geq \frac{M n^{-1 / 2} \ln \left(q_{n}\right)^{1 / 2}}{K_{4}}\right] \\
& =K_{1} q^{2}-K_{2} M_{n}^{2} \\
& <\varepsilon
\end{aligned}
$$

for all $n>N$, proving the desired result.

# References 

[1] J. Ansari, S. Fuchs, A simple extension of Azadkia \& Chatterjee's rank correlation to a vector of enogenous variables, preprint arxiv. 2212.01621 (2023).
[2] M. Azadkia, S. Chatterjee, A simple measure of conditional dependence, Ann. Stat. 49 (2021) 3070-3102.
[3] P. J. Bickel, E. Levina, Regularized estimation of large covariance matrices, Ann. Stat. 36 (2008) 199-227.
[4] J. Bien, R. J. Tibshirani, Sparse estimation of a covariance matrix, Biometrika 98 (2011) 807-820.
[5] J. Bien, R. J. Tibshirani, Spcov: Sparse Estimation of a Covariance Matrix, 2022. R package version 1.3.
[6] J. Bigot, R. J. Biscay, J.-M. Loubes, L. Muñiz-Alvarez, Group lasso estimation of high-dimensional covariance matrices, J. Mach. Learn. Res. 12 (2011) $3187-3225$.
[7] J. R. Cardoso, Evaluating the Fréchet derivative of the matrix $p$ th root, Electron. Trans. Numer. Anal. 38 (2011) 202-217.
[8] S. Chatterjee, A new coefficient of correlation, J. Am. Stat. Assoc. 116 (2021) 2009-2022.
[9] J. Chiquet, Y. Grandvalet, C. Charbonnier, Sparsity with sign-coherent groups of variables via the cooperative-lasso, Ann. Appl. Stat. 6 (2012) $795-860$.
[10] P. Clement, W. Desch, An elementary proof of the triangle inequality for the Wasserstein metric, Proc. Am. Math. Soc. 136 (2008) 333-339.
[11] S. De Keyser, I. Gijbels, Copula-based divergence measures for dependence between random vectors, in: L. A. García-Escudero, A. Gordaliza, A. Mayo, M. A. L. Gomez, M. A. Gil, P. Grzegorzewski, O. Hryniewicz (Eds.), Advances in Intelligent Systems and Computing, Vol. 1433, Building Bridges between Soft and Statistical Methodologies for Data Science, Springer, 2023, pp. 104-111.
[12] S. De Keyser, I. Gijbels, Parametric dependence between random vectors via copula-based divergence measures, preprint arxiv:2302.13611 (2023).
[13] J. Fan, Y. Feng, Y. Wu, Network exploration via the adaptive lasso and scad penalties, Ann. Appl. Stat. 3 (2009) 521-541.
[14] J. Fan, R. Li, Variable selection via nonconcave penalized likelihood and its oracle properties, J. Am. Stat. Assoc. 96 (2001) 1348-1360.
[15] J.-D. Fermanian, Sparse M-estimators in semi-parametric copula models, to appear in Bernoulli, URL: https://www.bernoullisociety.org/publications/bernoulli-journal/bernoulli-journal-papers (2024).
[16] M. Fop, Covglasso: sparse covariance matrix estimation, 2021. R package version 1.0.3.
[17] R. Foygel, M. Drton, Extended Bayesian information criteria for Gaussian graphical models, in: J. Lafferty, C. Williams, J. Shawe-Taylor, R. Zemel, A. Culotta (Eds.), Advances in Neural Information Processing Systems 23 (NIPS 2010), 2010, pp. 604-612.
[18] S. Fuchs, Quantifying directed dependence via dimension reduction, J. Multivar. Anal., in press, available online, 105266 (2023).
[19] S. Fuchs, F. M. L. Di Lascio, F. Durante, Dissimilarity functions for rank-invariant hierarchical clustering of continuous variables, Comput. Stat. Data Anal. 159 (2021) 107201.
[20] G. Geenens, P. Lafaye de Micheaux, The Hellinger correlation, J. Am. Stat. Assoc. 117 (2022) 639-653.
[21] C. Genest, B. Rémillard, D. Beaudoin, Goodness-of-fit tests for copulas: A review and a power study, Insur. Math. Econ. 44 (2009) 199-213.
[22] I. Gijbels, V. Kika, M. Omelka, On the specification of multivariate association measures and their behaviour with increasing dimension, $J$. Multivar. Anal. 182 (2021) 104704.
[23] O. Grothe, J. Schnieders, J. Segers, Measuring association and dependence between random vectors, J. Multivar. Anal. 123 (2014) 96-110.
[24] J. Hájek, Z. Šidák, Theory of Rank Tests, Academia, Prague, 1967.
[25] N.J. Higham, Functions of Matrices, SIAM, 2008.
[26] M. Hofert, W. Oldford, A. Prasad, M. Zhu, A framework for measuring association of random vectors via collapsed random variables, J. Multivar. Anal. 172 (2019) 5-27.
[27] H. Hotelling, Relations between two sets of variates, Biometrika 28 (1936) 321-377.
[28] C. A. J. Klaassen, J. A. Wellner, Efficient estimation in the bivariate normal copula model: normal margins are least favourable, Bernoulli 3 (1997) $55-77$.
[29] C. Lam, J. Fan, Sparsistency and rates of convergence in large covariance matrix estimation, Ann. Stat. 37 (2009) 4254-4278.
[30] S. Lê, F. Husson, SensoMineR: A package for sensory data analysis, J. Sens. Stud. 23 (2008) 14-25
[31] O. Ledoit, M. Wolf, A well-conditioned estimator for large-dimensional covariance matrices, J. Multivar. Anal. 88 (2004) 365-411.
[32] F. Llobell, V. Cariou, E. Vigneau, A. Labenne, E. M. Qannari, Analysis

[35] I. Medovikov, A. Prokhorov, A new measure of vector dependence, with applications to financial risk and contagion, J. Financ. Econom. 15 (2017) $474-503$.
[36] G. Mordant, J. Segers, Measuring dependence between random vectors via optimal transport, J. Multivar. Anal. 189 (2022) 104912.
[37] R. B. Nelsen, Nonparametric measures of multivariate association, in: L. Rüschendorf, B. Schweizer, M. D. Taylor (Eds.), IMS Lecture Notes - Monograph Series Vol. 28, Distributions with Fixed Marginals and Related Topics, 1996, pp. 223-232.
[38] R. B. Nelsen, An Introduction to Copulas, Springer Science and Business Media, New York, 2006.
[39] V. M. Panaretos, Y. Zemel, Statistical aspects of Wasserstein distances, Annu. Rev. Stat. Appl. 6 (2019) 405-431.
[40] F. H. Ruymgaart, G. R. Shorack, W. R. van Zwet, Asymptotic normality of nonparametric tests for independence, Ann. Math. Stat. 43 (1972) $1122-1135$.
[41] L. Saulis, V. A. Statulevičius, Limit theorems for Large Deviations, Kluwer Academic Publishers, Dordrecht, 1991.
[42] F. Schmid, R. Schmidt, Multivariate extensions of Spearman'srho and related statistics, Stat. Probab. Lett. 77 (2007) 407-416.
[43] A. Sklar, Fonctions de repartition à $n$ dimensions et leurs marges, Publications de l'Institut Statistique de l'Université de Paris 8 (1959) $229-231$.
[44] G. J. Székely, M. L. Rizzo, N. K. Bakirov, Measuring and testing dependence by correlation of distances, Ann. Stat. 35 (2007) 2769-2794.
[45] A. Takatsu, Wasserstein geometry of Gaussian measures, Osaka J. Math. 48 (2011) 1005-1026.
[46] R. C. Thompson, S. Therianos, Inequalities connecting the eigenvalues of a hermitian matrix with the eigenvalues of complementary principal submatrices, Bull. Aust. Math. Soc. 6 (1972) 117-132.
[47] A. Tsanas, M. A. Little, C. Fox, L. O. Ramig, Objective automatic assessment of rehabilitative speech treatment in Parkinson's disease, IEEE Trans. Neural Syst. Rehabil. Eng. 22 (2014) 181-190.
[48] C. Villani, Optimal Transport: Old and New, volume 338, Springer Science \& Business Media, 2008.
[49] H. Wang, Coordinate descent algorithm for covariance graphical lasso, Stat. Comput. 24 (2014) 521-529.
[50] D. I. Warton, Penalized normal likelihood and ridge regularization of correlation and covariance matrices, J. Am. Stat. Assoc. 103 (2008) $340-349$.
[51] L. Zhang, D. Lu, X. Wang, The essential dependence for a group of random vectors, Commun. Stat. - Theory Methods 50 (2020) 1-37.
[52] H. Zou, R. Li, One-step sparse estimates in nonconcave penalized likelihood models, Ann. Stat. 36 (2008) 1509-1533.





Fig. S1: Monte Carlo bias of the estimators $\boldsymbol{D} \cdot\left(\widehat{\mathbb{R}}_{R, n}\right.$ ) (penalty) and $\boldsymbol{D} \cdot\left(\widehat{\mathbb{R}}_{n}\right)$ (no penalty) for $D_{t \ln (t)}, D_{(\sqrt{t}-1)^{2}}, D_{1}$ and $D_{2}$, based on 1000 replications with sample sizes $n=50,100,500$ as a function of $q$, in two different designs.



Fig. S2: Monte Carlo variance of the estimators $\boldsymbol{D} \cdot\left(\widehat{\mathbb{R}}_{R, n}\right.$ ) (penalty) and $\boldsymbol{D} \cdot\left(\widehat{\mathbb{R}}_{n}\right)$ (no penalty) for $D_{t \ln (t)}, D_{(\sqrt{t}-1)^{2}}, D_{1}$ and $D_{2}$, based on 1000 replications with sample sizes $n=50,100,500$ as a function of $q$, in two different designs.



