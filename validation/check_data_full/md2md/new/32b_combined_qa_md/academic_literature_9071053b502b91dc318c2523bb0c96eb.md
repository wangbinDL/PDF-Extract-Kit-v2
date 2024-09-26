# High-dimensional copula-based Wasserstein dependence. 

Steven De Keyser ${ }^{\mathrm{a}}$, Irène Gijbels ${ }^{\mathrm{a}, *}$<br>${ }^{a}$ Department of Mathematics, KU Leuven, Celestijnenlaan 200B, B-3001 Leuven (Heverlee), Belgium


#### Abstract

We generalize 2-Wasserstein dependence coefficients to measure dependence between a finite number of random vectors. This generalization includes theoretical properties, and in particular focuses on an interpretation of maximal dependence and an asymptotic normality result for a proposed semi-parametric estimator under a Gaussian copula assumption. In addition, we discuss general axioms for dependence measures between multiple random vectors, other plausible normalizations, and various examples. Afterwards, we look into plug-in estimators based on penalized empirical covariance matrices in order to deal with high dimensionality issues and take possible marginal independencies into account by inducing (block) sparsity. The latter ideas are investigated via a simulation study, considering other dependence coefficients as well. We illustrate the use of the developed methods in two real data applications.


Keywords: Copula, Normal scores rank correlation, Regularization, Sparsity, Wasserstein dependence
2020 MSC: Primary 62Axx, 62Hxx; Secondary 62Exx, 62Gxx.

## 1. Introduction

A prominent line of research in statistics considers measuring dependence between groups of variables. In case of two groups, greatly celebrated is the canonical correlation analysis of [27] relying on the Pearson correlation coefficient. To step away from the assumption of Gaussianity, concordance measures as studied in, e.g., [22, 37, 42] among many others, are also used for quantifying general monotonic associations between two random vectors in [23]. In [26], measures of association computed from collapsed random variables are used to measure the dependence between random vectors. Fundamental is copula theory (e.g., [38,43]), allowing to split multivariate distributions into marginal distributions on the one hand, and a dependence structure described by the copula on the other hand. Especially when the marginals are continuous, the preference often goes to copula-based dependence measures since then, by Sklar's theorem [43], the copula is unique, and hence margin-free dependence can unequivocally be quantified.

Statistical independence between random vectors holds if and only if the true underlying copula is the product of the marginal copulas (where a one dimensional copula is basically a uniform distribution on $[0,1]$ ), yielding zero dependence. However, the dependence measures mentioned above do not detect all types of departure from independence, meaning that they might vanish while the independence product copula is misspecified. Since the work of [44], there has been a growing interest for dependence measures that completely characterize independence. Some recent developments are, e.g., the Hoeffding's Phi-Square measure of [35], the $\Phi$-dependence measures of [11] (of which the Hellinger correlation [20] and essential dependence [51] are particular cases), the coefficient of Chatterjee $[1,2,8,18]$, and the 2-Wasserstein coefficients of [36].

The aim of this article is to elaborate further on the optimal transport measures of [36]. First, the focus will be on extending their dependence coefficients from two to finitely many random vectors. We do this from a copula point of view. This includes generalizing the results of [36], and also verifying the axioms stated in [11] (see also Appendix A). Some additional examples, focusing on, e.g., the impact of the normalization, are provided as well. Afterwards, we dive into the Bures-Wasserstein dependence making a Gaussian copula assumption. This yields dependence measures

[^0]
[^0]:    *Corresponding author. Email address: irene.gijbels@kuleuven.be




---

that are attractive, and more amenable for estimation. The results are a far from straightforward extension of results of [36] to the case of a finite number of random vectors, and require significant mathematical care.

The proposed semi-parametric estimation approach of the Bures-Wasserstein coefficients relies on the sample matrix of normal scores rank correlations (see, e.g., [24]). Since we extend the theory to a general finite amount of groups of variables, high dimensional cases with a large number of variables compared to the sample size are of study interest as well. Acclaimed penalization techniques are known to significantly improve (inverse) covariance matrix estimation (see, e.g., [29] and references therein). We utilize these ideas in our Gaussian copula context in order to correct for high dimensionality bias and possibly enforce sparsity at the individual level or group level to take plausible marginal independencies into account.

The outline of this paper is the following. Section 2 explains how optimal transport theory is combined with copula theory in order to arrive at a dependence measure between multiple groups of random variables that completely characterizes independence and is invariant with respect to the univariate marginal distributions. The verification of the properties postulated in [11] for such dependence measures is also part of this section. The Gaussian copula approach is discussed in Section 3, with special attention to the meaning of maximal dependence, and asymptotic normality of the proposed semi-parametric estimator. Afterwards, different regularization techniques for Gaussian copula covariance matrices are discussed in Section 4. Next to an empirical illustration of the asymptotic normality result, simulations are performed in Section 5 to investigate the performance of these regularization techniques on various dependence coefficients for random vectors. Two real data applications are discussed in Section 6. All proofs are deferred to the Appendix. Any experiments reported can be reproduced via the source code available at https://github.com/StevenDeKeyser98/VecDep. Additional figures are included in the Supplementary Material.

# 2. General 2-Wasserstein dependence 

We consider a $q$-dimensional random vector $X=\left(X_{1}, \ldots, X_{k}\right)$ defined on $\left(\mathbb{R}^{q}, \mathcal{B}\left(\mathbb{R}^{q}\right), \lambda^{q}\right)$ consisting of $k$ marginal random vectors $X_{i}=\left(X_{i 1}, \ldots, X_{i d_{i}}\right)$ for $i=1, \ldots, k$ having $d_{i}$ continuous univariate marginal random variables $X_{i j}$ for $j=1, \ldots, d_{i}$. The numbers $d_{1}, \ldots, d_{k} \in \mathbb{Z}_{>0}$ are such that $q=d_{1}+\cdots+d_{k}$, and $\lambda^{q}$ denotes the $q$-dimensional Lebesgue measure defined on $\mathcal{B}\left(\mathbb{R}^{q}\right)$, the Borel sigma-algebra on $\mathbb{R}^{q}$. Let $P: \mathcal{B}\left(\mathbb{R}^{q}\right) \rightarrow \mathbb{R}$ be a probability measure. Our aim is to measure the dependence between $X_{1}, \ldots, X_{k}$. For $I=[0,1]$ and $\mathbb{P}\left(I^{q}\right)$ the set of Borel probability measures on $I^{q}$, the random vector $X$ is assigned a copula probability law $\mu_{C} \in \mathbb{P}\left(I^{q}\right)$ having corresponding marginal copula laws $\mu_{C_{i}} \in \mathbb{P}\left(I^{d_{i}}\right)$ of $X_{i}$ for $i=1, \ldots, k$. Note that in case $d_{i}=1$, the law $\mu_{C_{i}}$ is that of a uniform distribution on $I$. We denote $\Gamma\left(\mu_{C_{1}}, \ldots, \mu_{C_{k}}\right)$ for the set of measures $\gamma \in \mathbb{P}\left(I^{q}\right)$ such that

$$
\mu_{C_{i}}\left(B_{i}\right)=\gamma\left(I^{d_{1}} \times \cdots \times I^{d_{i-1}} \times B_{i} \times I^{d_{i+1}} \times \cdots \times I^{d_{k}}\right)
$$

for all $B_{i} \in \mathcal{B}\left(I^{d_{i}}\right)$ and $i=1, \ldots, k$. This is a natural generalization of the set of coupling measures. Obviously, $\mu_{C} \in$ $\Gamma\left(\mu_{C_{1}}, \ldots, \mu_{C_{k}}\right)$. Quantifying the intensity of relation between $X_{1}, \ldots, X_{k}$ can be done by measuring the difference between $\mu_{C}$ and the product measure $\mu_{C_{1}} \times \cdots \times \mu_{C_{k}}$. We use the 2-Wasserstein distance, whose square is, for certain measures $\pi, \widetilde{\pi} \in \mathbb{P}\left(I^{q}\right)$ given by

$$
W_{2}^{2}(\pi, \widetilde{\pi})=\inf _{\gamma \in \Gamma(\pi, \widetilde{\pi})} \int_{I^{2 q}}\|u-v\|^{2} \mathrm{~d} \gamma(u, v)=\inf _{\substack{U \sim \pi \\ V \sim \widetilde{\pi}}} \mathbb{E}\left(\|U-V\|^{2}\right)
$$

The interpretation of the metric (1) is optimal transport, see, e.g., [39]. It is the minimal effort (cost) required to transform the mass of $\pi$ into the mass of $\widetilde{\pi}$, i.e., for every $(u, v)$ transport an infinitesimal amount of mass $\mathrm{d} \gamma(u, v)$ from $u$ to $v$ at a distance cost of $\|u-v\|^{2}$. Aggregating the mass $\gamma\left(\{u\} \times I^{q}\right)$ that leaves $u$ gives $\pi(u)$ and the total mass $\gamma\left(I^{q} \times\{v\}\right)$ that reaches $v$ equals $\widetilde{\pi}(v)$. For certain non-degenerate (i.e. not Dirac delta distributions) reference laws $\nu_{i} \in \mathbb{P}\left(I^{d_{i}}\right)$ for $i=1, \ldots, k$, we now define

$$
\begin{array}{r}
T_{d_{1}, \ldots, d_{k}}\left(\mu_{C} ; \nu_{1}, \ldots, \nu_{k}\right)=W_{2}^{2}\left(\mu_{C}, \nu_{1} \times \cdots \times \nu_{k}\right)-W_{2}^{2}\left(\mu_{C_{1}} \times \cdots \times \mu_{C_{k}}, \nu_{1} \times \cdots \times \nu_{k}\right) \\
\quad=W_{2}^{2}\left(\mu_{C}, \nu_{1} \times \cdots \times \nu_{k}\right)-\sum_{i=1}^{k} W_{2}^{2}\left(\mu_{C_{i}}, \nu_{i}\right)
\end{array}
$$




---

where the second identity is known to be true (see, e.g., [39]). We call a subset $A \subset \mathcal{P}\left(\mathrm{I}^{q}\right) W_{2}$-compact if every sequence in the metric space $\left(A, W_{2}\right)$ has a convergent subsequence with limit in $A$. Lemma 1 gives the main properties of $\mathcal{T}_{d_{1}, \ldots, d_{k}}$. Proofs of Lemma 1, and all other theoretical results of Section 2, can be found in Appendix B.

Lemma 1. It holds that
(a) $\mathcal{T}_{d_{1}, \ldots, d_{k}}\left(\mu_{C} ; \nu_{1}, \ldots, \nu_{k}\right) \geq 0$
(b) $\mathcal{T}_{d_{1}, \ldots, d_{k}}\left(\mu_{C_{1}} \times \cdots \times \mu_{C_{k}} ; \nu_{1}, \ldots, \nu_{k}\right)=0$
(c) If either $\mu_{C_{i}}=\nu_{i}$ for all $i=1, \ldots, k$ or $\nu_{i}$ is absolutely continuous (with respect to $\lambda_{d_{i}}$ ) for all $i=1, \ldots, k$, then $\mathcal{T}_{d_{1}, \ldots, d_{k}}\left(\mu_{C} ; \nu_{1}, \ldots, \nu_{k}\right)=0$ implies $\mu_{C}=\mu_{C_{1}} \times \cdots \times \mu_{C_{k}}$
(d) The set $\Gamma\left(\mu_{C_{1}}, \ldots, \mu_{C_{k}}\right)$ is $W_{2}$-compact in $\mathcal{P}\left(\mathrm{I}^{q}\right)$ and the mapping $\mathcal{T}_{d_{1}, \ldots, d_{k}}\left(\cdot ; \nu_{1}, \ldots, \nu_{k}\right):\left(\Gamma\left(\mu_{C_{1}}, \ldots, \mu_{C_{k}}\right), W_{2}\right) \rightarrow$ $(\mathbb{R},|\cdot|)$ is continuous.

Its interpretation, together with its mathematical properties, make $\mathcal{T}_{d_{1}, \ldots, d_{k}}\left(\mu_{C} ; \nu_{1}, \ldots, \nu_{k}\right)$ an appealing measure of dependence between $k$ random vectors $X_{1}, \ldots, X_{k}$. In what follows, we assume that $\nu_{i}$ is absolutely continuous for $i=1, \ldots, k$, and let $G_{C} \subset \Gamma\left(\mu_{C_{1}}, \ldots, \mu_{C_{k}}\right)$ be a compact set such that $\mu_{C} \in G_{C}$. General axioms for dependence measures between multiple random vectors are formulated in [11], see also Appendix A. Lemma 1 offers aid in proving them here, see Proposition 1.

Proposition 1. Consider Axioms (A1)-(A8) given in Appendix A, and a normalized version of $\mathcal{T}_{d_{1}, \ldots, d_{k}}\left(\mu_{C} ; \nu_{1}, \ldots, \nu_{k}\right)$ given by

$$
\mathcal{D}\left(\mu_{C} ; \nu_{1}, \ldots, \nu_{k}\right)=\frac{\mathcal{T}_{d_{1}, \ldots, d_{k}}\left(\mu_{C} ; \nu_{1}, \ldots, \nu_{k}\right)}{\sup _{\pi \in G_{C}} \mathcal{T}_{d_{1}, \ldots, d_{k}}\left(\pi ; \nu_{1}, \ldots, \nu_{k}\right)}
$$

Then, $\mathcal{D}$ satisfies (A1)-(A3) and (A5)-(A7). Axioms (A4) and (A8) are satisfied by the non-normalized version $\mathcal{T}_{d_{1}, \ldots, d_{k}}$.
The supremum in (2) is attained when $G_{C}$ is $W_{2}$-compact (e.g., $G_{C}=\Gamma\left(\mu_{C_{1}}, \ldots, \mu_{C_{k}}\right)$ ) because of (d) in Lemma 1. It represents the case of maximal dependence, which characterization (and hence the overall behaviour of (2)), largely depends on $G_{C}$. There is still freedom in choosing the normalization by picking the set $G_{C}$. It might impose additional constraints (in addition to having marginals $\mu_{C_{i}}$ ) on the $\pi \in \Gamma\left(\mu_{C_{1}}, \ldots, \mu_{C_{k}}\right)$ that characterizes maximal dependence (for example $\pi$ should be in the same copula family as $\mu_{C}$ ). Strictly speaking, we can have a different $G_{C}$ for every copula $C$, even if the marginals are the same.
Regarding axioms (A4) and (A8), we make the following remark.
Remark 1. While (2) does not satisfy axiom (A4) in general (that is for every possible choice of $G_{C}$ ), there might still be some specific choices for $G_{C}$ such that (A4) is satisfied. We illustrate this further in Example 1.

Also, when considering $C_{n} \rightarrow C$ uniformly as $n \rightarrow \infty$, axiom (A8) can be satisfied by (2) under some extra constraints. The numerator converges if $G_{C}$ is chosen such that $C \mapsto \sup _{\pi \in G_{C}} \mathcal{T}_{d_{1}, \ldots, d_{k}}\left(\pi ; \nu_{1}, \ldots, \nu_{k}\right)$ is continuous (considering the uniform metric on the space of copulas). In Section 3, we see that this holds in the class of Gaussian copulas when taking $G_{C}=\Gamma\left(\mu_{C_{1}}, \ldots, \mu_{C_{k}}\right)$.

We now arrive at a natural generalization of the Wasserstein dependence coefficients of [36], which come from (2) with two particular choices of reference measures.
Definition 1. For $m \in \mathbb{Z}_{>0}$, let $\gamma_{m}$ denote the measure of an $m$-variate Gaussian copula with identity correlation matrix (i.e., the $m$-variate independence copula). For $q=d_{1}+\cdots+d_{k}$ with $d_{1}, \ldots, d_{k} \in \mathbb{Z}_{>0}$ and for $\mu_{C} \in G_{C} \subset \Gamma\left(\mu_{C_{1}}, \ldots, \mu_{C_{k}}\right)$, where $G_{C}$ is $W_{2}$-compact and non-degenerate $\mu_{C_{i}} \in \mathcal{P}\left(\mathbb{I}^{d_{i}}\right)$ for $i=1, \ldots, k$, define

$$
\begin{aligned}
& \mathfrak{D}_{1}^{d_{1}, \ldots, d_{k}}\left(\mu_{C}\right)=\mathcal{D}\left(\mu_{C} ; \gamma_{d_{1}}, \ldots, \gamma_{d_{k}}\right)=\frac{W_{2}^{2}\left(\mu_{C}, \gamma_{q}\right)-\sum_{i=1}^{k} W_{2}^{2}\left(\mu_{C_{i}}, \gamma_{d_{i}}\right)}{\sup _{\pi \in G_{C}} W_{2}^{2}\left(\pi, \gamma_{q}\right)-\sum_{i=1}^{k} W_{2}^{2}\left(\mu_{C_{i}}, \gamma_{d_{i}}\right)} \\
& \mathfrak{D}_{2}^{d_{1}, \ldots, d_{k}}\left(\mu_{C}\right)=\mathcal{D}\left(\mu_{C} ; \mu_{C_{1}}, \ldots, \mu_{C_{k}}\right)=\frac{W_{2}^{2}\left(\mu_{C}, \mu_{C_{1}} \times \cdots \times \mu_{C_{k}}\right)}{\sup _{\pi \in G_{C}} W_{2}^{2}\left(\pi, \mu_{C_{1}} \times \cdots \times \mu_{C_{k}}\right)}
\end{aligned}
$$




---

If the context is clear, we just write $\mathcal{D}_{r}\left(\mu_{C}\right)$ for $r \in\{1,2\}$, or also $\mathcal{D}_{r}\left(X_{1} ; \cdots ; X_{k}\right)$ to emphasize that we are measuring the dependence between $k$ random vectors (having joint copula $C$ ).

Let us consider an example illustrating that $\mathcal{D}$ does not necessarily satisfy Axiom (A4) in general.
Example 1. Consider a random vector $\left(X_{1}, X_{2}, X_{3}\right)$ having a trivariate Gaussian copula $\mu_{C}$ with correlation matrix

$$
R=\left(\begin{array}{ccc}
1 & \rho & 0 \\
\rho & 1 & 0 \\
0 & 0 & 1
\end{array}\right), \text { where }-1 \leq \rho \leq 1
$$

Let $\mu_{C_{i}}$ be the marginal copula measure of $X_{i}$ for $i=1,2,3$, which in this case is in fact the Lebesgue measure corresponding to a $U[0,1]$ distribution. The product measure $\mu_{C_{1}} \times \mu_{C_{2}} \times \mu_{C_{3}}$ is the three dimensional independence copula, being equal to the trivariate Gaussian copula with identity correlation matrix $I_{3}$. Also note that $X_{3}$ is independent of $\left(X_{1}, X_{2}\right)$. One can quickly check that (using (3), see further)

$$
\mathcal{D}_{2}\left(X_{1} ; X_{2} ; X_{3}\right)=\frac{W_{2}^{2}\left(\mu_{C} ; \mu_{C_{1}} \times \mu_{C_{2}} \times \mu_{C_{3}}\right)}{\sup _{\pi \in \mathbb{G}_{C}} W_{2}^{2}\left(\pi, \mu_{C_{1}} \times \mu_{C_{2}} \times \mu_{C_{3}}\right)}=\frac{4-2 \sqrt{1-\rho}-2 \sqrt{1+\rho}}{\sup _{\pi \in \mathbb{G}_{C}} W_{2}^{2}\left(\pi, \mu_{C_{1}} \times \mu_{C_{2}} \times \mu_{C_{3}}\right)}
$$

The remaining question is what to pick for $\mathbb{G}_{C}$, i.e., which quantity do we put in the denominator and defines the maximal amount of dependence. Well, if $\mathbb{G}_{C}=\Gamma\left(\mu_{C_{1}}, \mu_{C_{2}}, \mu_{C_{3}}\right)$, we should find the squared 2-Wasserstein distance between the independence copula and any other trivariate distribution having $\mu_{C_{1}}, \mu_{C_{2}}$ and $\mu_{C_{3}}$ as marginals, that is every possible trivariate copula. This is, as far as we are concerned, an open problem. However, in this context, it is reasonable to restrict $\mathbb{G}_{C}$ to the Gaussian copula family. Doing so, one has

$$
\sup _{\pi \in \mathbb{G}_{C}} W_{2}^{2}\left(\pi, \mu_{C_{1}} \times \mu_{C_{2}} \times \mu_{C_{3}}\right)=W_{2}^{2}\left(\mu_{C^{c o}}, \mu_{C_{1}} \times \mu_{C_{2}} \times \mu_{C_{3}}\right)=6-2 \sqrt{3}
$$

where $\mu_{C^{c o}}$ stands for the comonotonicity copula measure, i.e., the limit of an equicorrelated $\left(R=(1-\rho) I_{3}+\rho \mathbb{1}_{3} \mathbb{1}_{3}^{T}\right.$, where $\mathbb{1}_{3}^{T}=(1,1,1)$ and $\left.\rho \in(-1 / 2,1)\right)$ Gaussian copula with correlation $\rho$ tending to 1 . With this choice of $\mathbb{G}_{C}$, $\left(X_{1}, X_{2}, X_{3}\right)$ can never reach the maximum dependence, since

$$
4-2 \sqrt{1-\rho}-2 \sqrt{1+\rho} \leq 4-2 \sqrt{2}<6-2 \sqrt{3}
$$

Another way to put it, is that

$$
\mathcal{D}_{2}\left(X_{1} ; X_{2} ; X_{3}\right)=\frac{2-\sqrt{1-\rho}-\sqrt{1+\rho}}{3-\sqrt{3}}<\frac{2-\sqrt{1-\rho}-\sqrt{1+\rho}}{2-\sqrt{2}}=\mathcal{D}_{2}\left(X_{1} ; X_{2}\right)
$$

where $\mathcal{D}_{2}\left(X_{1} ; X_{2}\right)$ is computed in a similar way, also restricting the couplings $\Gamma\left(\mu_{C_{1}}, \mu_{C_{2}}\right)$ to Gaussian ones. We thus see that, when adding an independent component $X_{3}$ into consideration, the dependence has decreased and hence axiom (A4) is definitely not fulfilled. Taking a look at $R$, it is maybe more tempting to have maximal dependence when $|\rho|=1$ and restrict $\mathbb{G}_{C}$ further to only those $\pi \in \Gamma\left(\mu_{C_{1}}, \mu_{C_{2}}, \mu_{C_{3}}\right)$ that are Gaussian and furthermore satisfy $\pi\left(B_{1} \times B_{2} \times B_{3}\right)=\pi\left(B_{1} \times B_{2} \times I\right) \cdot \pi\left(I \times I \times B_{3}\right)$ for all $B_{1}, B_{2}, B_{3} \in \mathcal{B}(I)$. Then, it is quickly seen that

$$
\sup _{\pi \in \mathbb{G}_{C}} W_{2}^{2}\left(\pi, \mu_{C_{1}} \times \mu_{C_{2}} \times \mu_{C_{3}}\right)=2-\sqrt{2}
$$

and hence $\mathcal{D}_{2}\left(X_{1} ; X_{2} ; X_{3}\right)=\mathcal{D}_{2}\left(X_{1} ; X_{2}\right)$, in harmony with axiom (A4). So, for actual computation, it is better to restrict $\mathbb{G}_{C}$ to the Gaussian copula family, and if some additional information is given (like zeroes in the correlation matrix), incorporating this in $\mathbb{G}_{C}$ can lead to a more interpretative dependence quantification.

Except for some families like normal distributions, computing the Wasserstein distance is very involved and tools and theory for statistical inference are still scarce. The authors of [36] give an overview of the literature so far, concluding that additional theory is still needed, and propose a quasi-Gaussian (based on covariance matrices) approach instead. We assume that the copula of $\mathbf{X}$ is Gaussian.




---

# 3. A Gaussian copula approach 

In this section, we assume a Gaussian copula model for $X$, elaborate more on maximal dependence, and discuss statistical inference within this framework.

### 3.1. The Bures-Wasserstein distance

The main incentive is the well-known formula for the squared 2-Wasserstein distance between Gaussian distributions, say with covariance matrices $R$ and $S$, becoming the so-called squared Bures-Wasserstein distance (see, e.g., [45]) between $R$ and $S$ :

$$
d_{W}^{2}(R, S)=\operatorname{tr}(R)+\operatorname{tr}(S)-2 \operatorname{tr}\left\{\left(R^{1 / 2} S R^{1 / 2}\right)^{1 / 2}\right\}
$$

were $t r$ stands for the trace of a matrix. We denote by $\mathcal{S}^{q}=\left\{R \in \mathbb{R}^{q \times q}: R^{\mathrm{T}}=R\right\}$ the set of symmetric $q \times q$ matrices, $\mathcal{S}_{\geq}^{q} \subset \mathcal{S}^{q}$ the set of positive semi-definite ones and $\mathcal{S}_{>}^{q} \subset \mathcal{S}_{\geq}^{q}$ the set of positive definite ones. Let again $q=d_{1}+\cdots+d_{k}$ and consider $R_{i i} \in \mathcal{S}_{\geq}^{d_{i}}$ for $i=1, \ldots, k$. We also define the set

$$
\Gamma\left(R_{11}, \ldots, R_{k k}\right)=\left\{A \in \mathcal{S}_{\geq}^{q}: A=\left(\begin{array}{cccl}
R_{11} & \Psi_{12} & \cdots & \Psi_{1 k} \\
\Psi_{12}^{\top} & R_{22} & \cdots & \Psi_{2 k} \\
\vdots & \vdots & \ddots & \vdots \\
\Psi_{1 k}^{\top} & \Psi_{2 k}^{\top} & \cdots & R_{k k}
\end{array}\right) \quad \text { for some } \Psi_{i j} \in \mathbb{R}^{d_{i} \times d_{j}}\right\}
$$

as the set of all covariance matrices of random vectors $Z=\left(Z_{1}, \ldots, Z_{k}\right)$ such that the covariance matrix of $Z_{i}$, being $R_{i i}$, remains fixed for all $i=1, \ldots, k$ and

$$
R_{0}=\left(\begin{array}{cccc}
R_{11} & 0_{12} & \ldots & 0_{1 k} \\
0_{12}^{\mathrm{T}} & R_{22} & \ldots & 0_{2 k} \\
\vdots & \vdots & \ddots & \vdots \\
0_{1 k}^{\mathrm{T}} & 0_{2 k}^{\mathrm{T}} & \ldots & R_{k k}
\end{array}\right)
$$

with $0_{i j} \in \mathbb{R}^{d_{i} \times d_{j}}$ a matrix of zeroes, as the covariance matrix when the $Z_{i}$ are all independent.
Consider now a random vector $X=\left(X_{1}, \ldots, X_{k}\right)$ having a Gaussian copula with covariance matrix

$$
R=\left(\begin{array}{cccc}
R_{11} & R_{12} & \ldots & R_{1 k} \\
R_{12}^{\mathrm{T}} & R_{22} & \ldots & R_{2 k} \\
\vdots & \vdots & \ddots & \vdots \\
R_{1 k}^{\mathrm{T}} & R_{2 k}^{\mathrm{T}} & \ldots & R_{k k}
\end{array}\right)
$$

This means that (5) is the usual covariance matrix of the random vector $Z=\left(Z_{1}, \ldots, Z_{k}\right)$, with $Z_{i}=\left(Z_{i 1}, \ldots, Z_{i d_{i}}\right)$ and $Z_{i j}=\left(\Phi^{-1} \circ F_{i j}\right)\left(X_{i j}\right)$ for $i=1, \ldots, k$ and $j=1, \ldots, d_{i}$, where $F_{i j}$ is the marginal distribution of $X_{i j}$ and $\Phi^{-1}$ the univariate standard normal quantile function. Measuring the dependence between $X_{1}, \ldots, X_{k}$ can be done by utilizing the 2-Wasserstein dependence coefficients of Definition 1 , now taking $d_{W}$ for $W_{2}$.

Definition 2. For $q=d_{1}+\cdots+d_{k}$ with $d_{1}, \ldots, d_{k} \in \mathbb{Z}_{>0}, R \in \Gamma\left(R_{11}, \ldots, R_{k k}\right)$ with $R_{i i} \in \mathcal{S}_{\geq}^{d_{i}} \backslash\{0\}$ for $i=1, \ldots, k$ and a $d_{W}$-compact set $\mathcal{G}_{R} \subset \Gamma\left(R_{11}, \ldots, R_{k k}\right)$ with $R \in \mathcal{G}_{R}$, define

$$
\begin{aligned}
& D_{1}\left(R ; d_{1}, \ldots, d_{k}\right)=\frac{d_{W}^{2}\left(R, I_{q}\right)-\sum_{i=1}^{k} d_{W}^{2}\left(R_{i i}, I_{d_{i}}\right)}{\sup _{A \in \mathcal{G}_{R}} d_{W}^{2}\left(A, I_{q}\right)-\sum_{i=1}^{k} d_{W}^{2}\left(R_{i i}, I_{d_{i}}\right)} \\
& D_{2}\left(R ; d_{1}, \ldots, d_{k}\right)=\frac{d_{W}^{2}\left(R, R_{0}\right)}{\sup _{A \in \mathcal{G}_{R}} d_{W}^{2}\left(A, R_{0}\right)}
\end{aligned}
$$

where $R_{0}$ is the matrix given in (4). If the context is clear, we also write $D_{r}(R)$ or $D_{r}\left(X_{1} ; \cdots ; X_{k}\right)$ for $r \in\{1,2\}$.




---

If the true copula is indeed Gaussian, the adequacy of the Bures-Wasserstein dependence remains, and we obtain something way more easy to handle. In order to make them fully practically usable, that is to say suitably attractive for estimation, we ought to find explicit expressions for the suprema in the denominator of the dependence measures. When $\mathcal{G}_{\boldsymbol{R}}=\Gamma\left(R_{11}, \ldots, R_{k k}\right)$ and $k=2$, the authors of [36] found elegant solutions to this problem, which we generalize to general $k$.

# 3.2. Maximal Bures-Wasserstein dependence 

We need the definition of majorization of two vectors and its behaviour under convex functions, as studied in [33].
Definition 3. For two vectors $x, y \in \mathbb{R}^{q}$, we say that $y$ majorizes $x$, denoted as $x \prec y$, if

$$
\left\{\begin{array}{l}
\sum_{i=1}^{\ell} x_{[i]} \leq \sum_{i=1}^{\ell} y_{[i]} \quad \text { for } \ell=1, \ldots, q-1 \\
\sum_{i=1}^{q} x_{[i]}=\sum_{i=1}^{q} y_{[i]}
\end{array}\right.
$$

where $x_{[1]} \geq \cdots \geq x_{[q]}$ are the components of $x$ in decreasing order, and similarly for $y$.
When $\lambda$ and $\mu$ are the vectors of eigenvalues of two correlation matrices, $\lambda$ being majorized by $\mu$ means that the proportion of the total variance explained by the $\ell$ first principal components is larger for the correlation matrix with eigenvalues $\mu$, for any $\ell \in\{1, \ldots, q-1\}$, than for the correlation matrix with eigenvalues $\lambda$. Fixing $k$ covariance matrices $R_{11}, \ldots, R_{k k}$ with $R_{i i} \in \mathcal{S}_{\geq}^{d_{i}}$, the goal is now to find $R_{m} \in \Gamma\left(R_{11}, \ldots, R_{k k}\right)$ whose ordered eigenvalues majorize those of any matrix $A \in \Gamma\left(R_{11}, \ldots, R_{k k}\right)$. Together with Lemma 2 (see Proposition 3.C. 1 in [33]), this will enable us to characterize maximal dependence between $k$ random vectors in terms of covariance matrices.

Lemma 2. If $g: I \rightarrow \mathbb{R}$ is convex, with $I \subset \mathbb{R}$ an interval, then

$$
x \prec y \quad \Longrightarrow \quad \sum_{i=1}^{q} g\left(x_{i}\right) \leq \sum_{i=1}^{q} g\left(y_{i}\right) \quad \text { for all } x, y \in I^{q}
$$

Since the 2-Wasserstein dependence coefficients satisfy axiom (A1), we can assume that $d_{1} \leq d_{2} \leq \cdots \leq d_{k}$ without loss of generality. Suppose that

$$
R_{i i}=U_{i i} \Lambda_{i i} U_{i i}^{T}
$$

is the eigendecomposition of $R_{i i}$, i.e., with $\Lambda_{i i}=\operatorname{diag}\left(\lambda_{1, i i}, \lambda_{2, i i}, \ldots, \lambda_{d_{i}, i i}\right)$ the $d_{i} \times d_{i}$ diagonal matrix with $d_{i}$ ordered eigenvalues $\lambda_{1, i i} \geq \lambda_{2, i i} \geq \cdots \geq \lambda_{d_{i}, i i}$ on the diagonal (counting multiplicities), and $U_{i i}$ an orthogonal matrix containing the corresponding eigenvectors for $i=1, \ldots, k$. The proof of Proposition 2, and all other theoretical results of Section 3 , are provided in Appendix C.
Proposition 2. Let $R_{i i} \in \mathcal{S}_{\geq}^{d_{i}}$ have eigendecomposition (6) for $i=1, \ldots, k$. Define the matrix $R_{m}$ as

$$
R_{m}=\left(\begin{array}{cccc}
R_{11} & \Psi_{12} & \cdots & \Psi_{1 k} \\
\Psi_{12}^{T} & R_{22} & \cdots & \Psi_{2 k} \\
\vdots & \vdots & \ddots & \vdots \\
\Psi_{1 k}^{T} & \Psi_{2 k}^{T} & \cdots & R_{k k}
\end{array}\right) \in \mathbb{R}^{q \times q}
$$

with $q=d_{1}+\cdots+d_{k}$ and $d_{1} \leq d_{2} \leq \cdots \leq d_{k}$, and off-diagonal blocks

$$
\Psi_{i j}=U_{i i} \Lambda_{i i}^{1 / 2} \Pi_{i j} \Lambda_{j j}^{1 / 2} U_{j j}^{T} \in \mathbb{R}^{d_{i} \times d_{j}}, \quad \text { where } \quad \Pi_{i j}=\left(I_{d_{i}} 0_{d_{i} \times\left(d_{j}-d_{i}\right)}\right) \in \mathbb{R}^{d_{i} \times d_{j}}
$$




---

the $d_{i} \times d_{j}$ upper left block of $I_{d_{i}+d_{j}}$ for $i=1, \ldots, k, j=i+1, \ldots, k$ (denoting $0_{d_{i} \times\left(d_{j}-d_{i}\right)}$ for the $d_{i} \times\left(d_{j}-d_{i}\right)$ matrix of zeroes). If we define $\lambda_{j, i i}=0$ for $j=d_{i}+1, \ldots, q$, the eigenvalues of $R_{\mathrm{m}}$ are

$$
\lambda\left(R_{\mathrm{m}}\right)=\left(\lambda_{j, 11}+\lambda_{j, 22}+\cdots+\lambda_{j, k k}\right)_{j=1}^{q}
$$

Furthermore, for any $A \in \Gamma\left(R_{11}, \ldots, R_{k k}\right)$ with eigenvalues $\lambda(A)=\left(\lambda_{j}\right)_{j=1}^{q}$, it holds that

$$
\lambda(A) \prec \lambda\left(R_{\mathrm{m}}\right)
$$

Example 2 gives the matrix $R_{\mathrm{m}}$ for some specific cases.
Example 2. Some expressions for $R_{\mathrm{m}}$ in case $k=2$ can be found in [36]. If $d_{i}=1$ with $R_{i i}=1$ for all $i=1, \ldots, k$, the matrix $R_{\mathrm{m}}$ is obviously given by $1_{q \times q}$, a matrix full of ones. Consider next $Z_{i}=\left(Z_{i 1}, Z_{i 2}\right)$ for $i=1, \ldots, k$, i.e., $k$ bivariate random vectors, with covariance matrix of $\left(Z_{i 1}, Z_{i 2}\right)$ given by

$$
R_{i i}=\left(\begin{array}{ll}
1 & \rho_{i} \\
\rho_{i} & 1
\end{array}\right)
$$

Assuming $\rho_{i}, \rho_{j} \geq 0$, one can check that $\Psi_{i j}$ of $R_{\mathrm{m}}$ in (7) for $i=1, \ldots, k-1$ and $j=i+1, \ldots, k$ is given by

$$
\Psi_{i j}=\left(\begin{array}{ll}
\frac{\sqrt{1+\rho_{i}} \sqrt{1+\rho_{j}}+\sqrt{1-\rho_{i}} \sqrt{1-\rho_{j}}}{2} & \frac{\sqrt{1+\rho_{i}} \sqrt{1+\rho_{j}}-\sqrt{1-\rho_{i}} \sqrt{1-\rho_{j}}}{2} \\
\frac{\sqrt{1+\rho_{i}} \sqrt{1+\rho_{j}}-\sqrt{1-\rho_{i}} \sqrt{1-\rho_{j}}}{2} & \frac{\sqrt{1+\rho_{i}} \sqrt{1+\rho_{j}}+\sqrt{1-\rho_{i}} \sqrt{1-\rho_{j}}}{2}
\end{array}\right) .
$$

The result is similar in case $\rho_{i} \leq 0$ or $\rho_{j} \leq 0$ up to some signs (orthogonal transformations, to which $d_{\mathcal{W}}$ is invariant). The principal components of $\left(Z_{i 1}, Z_{i 2}\right)$ are

$$
Y_{i 1}=\frac{1}{\sqrt{2}}\left(Z_{i 1}+Z_{i 2}\right) \text { and } Y_{i 2}=\frac{1}{\sqrt{2}}\left(Z_{i 2}-Z_{i 1}\right)
$$

corresponding to the eigenvalues $1+\rho_{i} \geq 1-\rho_{i}$ respectively, with

$$
\operatorname{Corr}\left(Y_{i 1}, Y_{j 1}\right)=\frac{\operatorname{Corr}\left(Z_{i 2}, Z_{j 2}\right)+\operatorname{Corr}\left(Z_{i 2}, Z_{j 1}\right)+\operatorname{Corr}\left(Z_{i 1}, Z_{j 2}\right)+\operatorname{Corr}\left(Z_{i 1}, Z_{j 1}\right)}{2 \sqrt{1+\operatorname{Corr}\left(Z_{i 1}, Z_{i 2}\right)} \sqrt{1+\operatorname{Corr}\left(Z_{j 1}, Z_{j 2}\right)}}
$$

and

$$
\operatorname{Corr}\left(Y_{i 2}, Y_{j 2}\right)=\frac{\operatorname{Corr}\left(Z_{i 2}, Z_{j 2}\right)-\operatorname{Corr}\left(Z_{i 2}, Z_{j 1}\right)-\operatorname{Corr}\left(Z_{i 1}, Z_{j 2}\right)+\operatorname{Corr}\left(Z_{i 1}, Z_{j 1}\right)}{2 \sqrt{1-\operatorname{Corr}\left(Z_{i 1}, Z_{i 2}\right)} \sqrt{1-\operatorname{Corr}\left(Z_{j 1}, Z_{j 2}\right)}}
$$

A quick check then verifies that if $\left(\left(Z_{11}, Z_{12}\right), \ldots,\left(Z_{k 1}, Z_{k 2}\right)\right)$ has correlation matrix $R_{\mathrm{m}}$ with blocks (9), it holds that $\operatorname{Corr}\left(Y_{i 1}, Y_{j 1}\right)=\operatorname{Corr}\left(Y_{i 2}, Y_{j 2}\right)=1$ for all $i=1, \ldots, k-1$ and $j=i+1, \ldots, k$, i.e., all first principal components are perfectly correlated and all second principal components as well.
Proposition 3 states that the matrix $R_{\mathrm{m}}$ in (7) maximizes the intensity of dependence, i.e., $D_{1}\left(R_{\mathrm{m}}\right)=D_{2}\left(R_{\mathrm{m}}\right)=1$ when taking $\mathcal{G}_{R}=\Gamma\left(R_{11}, \ldots, R_{k k}\right)$ for fixed marginal covariance matrices $R_{11}, \ldots, R_{k k}$.
Proposition 3. Let $q=d_{1}+\cdots+d_{k}$ and $R_{i i} \in \mathcal{S}_{\geq}^{d_{i}} 4$ for $i=1, \ldots, k$. The matrix $R_{\mathrm{m}}$ in (7) maximizes $d_{\mathcal{W}}\left(R, I_{q}\right)$ and $d_{\mathcal{W}}\left(R, R_{0}\right)$ with $R_{0}$ given in (4) among all $R \in \Gamma\left(R_{11}, \ldots, R_{k k}\right)$.

A general interpretation of $R_{\mathrm{m}}$ is given in Remark 2. -
Remark 2. Assuming again that $d_{1} \leq d_{2} \leq \cdots \leq d_{k}$, the matrix $R_{\mathrm{m}}$ in (7) is the covariance matrix of

$$
\left(\begin{array}{c}
U_{11} \Lambda_{11}^{1 / 2} Z_{1} \\
U_{22} \Lambda_{22}^{1 / 2} Z_{2} \\
\vdots \\
U_{k k} \Lambda_{k k}^{1 / 2} Z_{k}
\end{array}\right) \in \mathbb{R}^{q \times 1}
$$




---

where $Z_{1}=\left(Z_{11}, \ldots, Z_{1 d_{1}}\right)^{T}, Z_{2}=\left(Z_{21}, \ldots, Z_{2 d_{2}}\right)^{T}, \ldots, Z_{k}=\left(\underset{k}{Z_{k 1}}, \ldots, Z_{d_{k}}\right)^{T}$ such that for all $i=1, \ldots, k$ we have $Z_{i} \sim N_{d_{i}}\left(0_{d_{i}}, I_{d_{i}}\right)$, and in addition $Z_{i j}=\left.Z_{(i+1) j}\right|_{i=1} ^{k-1} j=1, \ldots, d_{i}$, i.e., $Z_{i}$ and $Z_{j}$ have the first $\min \left\{d_{i}, d_{j}\right\}$ components in common for all $i, j \in\{1, \ldots, k\}$. The correlation matrix of the principal components of $U_{11} \Lambda_{11}^{1 / 2} Z_{1}, \ldots, U_{k k} \Lambda_{k k}^{1 / 2} Z_{k}$ is

$$
\left(\begin{array}{ccccc}
I_{d_{1}} & \Pi_{12} & \ldots & & \Pi_{1 k} \\
\Pi_{12}^{T} & I_{d_{2}} & \cdots & & \Pi_{2 k} \\
\vdots & \vdots & \ddots & & \vdots \\
& & & I_{d_{k}} & \\
\Pi_{1 k}^{T} & \Pi_{2 k}^{T} & \ldots & &
\end{array}\right)
$$

with $\Pi_{i j}$ as in Proposition 2. Hence, if $\left(X_{1}, \ldots, X_{k}\right)$ has a Gaussian copula with covariance matrix $R_{m}$, then for $\ell=1, \ldots, \min \left\{d_{i}, d_{j}\right\}$ the $\ell$-th principal components of $\left(\left(\Phi^{-1} \circ F_{i 1}\right)\left(X_{i 1}\right), \ldots,\left(\Phi^{-1} \circ F_{i d_{i}}\right)\left(X_{i d_{i}}\right)\right)$ and $\left(\left(\Phi^{-1} \circ F_{j 1}\right)\left(X_{j 1}\right), \ldots\right.$, $\left.\left(\Phi^{-1} \circ F_{j d_{j}}\right)\left(X_{j d_{j}}\right)\right)$ are perfectly correlated for all $i, j \in\{1, \ldots, k\}$. This is the interpretation of maximal dependence for the Bures-Wasserstein dependence measures.
In the upcoming section, we also assume that $G_{R}=\Gamma\left(R_{11}, \ldots, R_{k k}\right)$.

# 3.3. Statistical inference 

In practice, we have an i.i.d. sample $X^{(\ell)}=\left(X_{1}^{(\ell)}, \ldots, X_{k}^{(\ell)}\right)$ for $\ell=1, \ldots, n$ from $X$, where $X_{i}^{(\ell)}=\left(X_{i 1}^{(\ell)}, \ldots, X_{i d_{i}}^{(\ell)}\right)$ for $\ell=1, \ldots, n$ is a sample from $X_{i}$ for $i=1, \ldots, k$. A natural estimator for the Gaussian copula covariance matrix is known as the matrix of sample normal scores rank correlation coefficients (see, e.g., [24]),

$$
\widehat{R}_{n}=\left(\begin{array}{ccccc}
\widehat{R}_{11} & \widehat{R}_{12} & \cdots & & \widehat{R}_{1 k} \\
\widehat{R}_{12}^{T} & \widehat{R}_{22} & \cdots & & \widehat{R}_{2 k} \\
\vdots & \vdots & \ddots & & \vdots \\
& & \widehat{R}_{1 k}^{T} & & \\
\widehat{R}_{2 k}^{T} & \cdots & & & \widehat{R}_{k k}
\end{array}\right)
$$

with $\left(\widehat{R}_{i m}\right)_{p t}=\widehat{\rho}_{i j, m t}=\frac{\frac{1}{n^{2}} \sum_{\ell=1}^{n} \widehat{Z}_{i j}^{(\ell)} \widehat{Z}_{m t}^{(\ell)}}{\left(\frac{1}{n} \sum_{\ell=1}^{n}\left\{\Phi^{-1}\left(\frac{\ell}{n+1}\right)\right\}^{2}\right)}$
defined by computing normal scores

$$
\widehat{Z}_{i j}^{(\ell)}=\Phi^{-1}\left(\frac{n}{n+1} \widehat{F}_{i j}\left(X_{i j}^{(\ell)}\right)\right)
$$

obtained through the empirical $\operatorname{cdf} \widehat{F}_{i j}\left(x_{i j}\right)=\frac{1}{n} \sum_{\ell=1}^{n} \mathbb{1}_{\left\{X_{i j}^{(\ell)} \leq x_{i j}\right\}}$ for $i=1, \ldots, k$ and $j=1, \ldots, d_{i}$. The quantity $\widehat{\rho}_{i j, m t}$ is calculated as the conventional Pearson correlation of the bivariate scores $\left(\left(\hat{Z}_{i j}^{(1)}, \widehat{Z}_{m t}^{(1)}\right), \ldots,\left(\widehat{Z}_{i j}^{(n)}, \widehat{Z}_{m t}^{(n)}\right)\right)$ and by observing that

$$
\frac{1}{n} \sum_{\ell=1}^{n} \widehat{Z}_{i j}^{(\ell)}=\frac{1}{n} \sum_{\ell=1}^{n} \Phi^{-1}\left(\frac{\ell}{n+1}\right)=0 \text { and } \frac{1}{n} \sum_{\ell=1}^{n}\left(\widehat{Z}_{i j}^{(\ell)}\right)^{2}=\frac{1}{n} \sum_{\ell=1}^{n}\left\{\Phi^{-1}\left(\frac{\ell}{n+1}\right)\right\}^{2}
$$

which holds because $\Phi^{-1}(\alpha)=-\Phi^{-1}(1-\alpha)$ for $\alpha \in[0,1]$ and $n \widehat{F}_{i j}\left(X_{i j}^{(\ell)}\right)$ is the rank of $X_{i j}^{(\ell)}$ in the sample $X_{i j}^{(1)}, \ldots, X_{i j}^{(n)}$. A next natural step in estimating $\mathcal{D}_{r}(R)$ is to plug in $\widehat{R}_{n}$ for the unknown $R$. Define the map $\phi$ by $\phi(\Sigma)=$ $D_{\Sigma}^{-1 / 2} \Sigma D_{\Sigma}^{-1 / 2}$ for $\Sigma \in \mathbb{S}^{q}$, where $D_{\Sigma}$ is the diagonal matrix containing the diagonal of $\Sigma$, and let $\|\Sigma\|_{F}=\operatorname{tr}^{1 / 2}\left(\Sigma^{T} \Sigma\right)$ be the Frobenius norm. Fréchet differentiability of the mapping

$$
\left(\mathbb{S}^{q},\|\cdot\|_{F}\right) \rightarrow(\mathbb{R},|\cdot|): \Sigma \mapsto\left(\mathcal{D}_{r} \circ \phi\right)(\Sigma)
$$

on $\mathbb{S}_{>}^{q}$ suffices in order for the delta method to transform an asymptotic normality result for $\widehat{R}_{n}$ into an asymptotic normality result for $\mathcal{D}_{r}\left(\widehat{R}_{n}\right)$. We first highlight some notation. We assume $d_{1} \leq d_{2} \leq \cdots \leq d_{k}$, the matrix $R_{m}$ is again defined by (7) based on the eigendecompositions $R_{i i}=


---

be the projection matrix onto the $\mathfrak{d}_{i}$ coordinates, satisfying $\mathbf{R}_{\mathfrak{i i}}=\mathbf{P}_{\mathfrak{i}} \mathbf{R} \mathbf{P}_{\mathfrak{i}}^{\top}$. Partition the matrix $\boldsymbol{\Lambda}_{\mathfrak{i i}}$ as

$$
\boldsymbol{\Lambda}_{\mathfrak{i i}}=\left(\begin{array}{cccc}
\boldsymbol{\Lambda}_{\mathfrak{i i}, 1} & \mathbf{0}_{\mathfrak{d}_{1} \times\left(\mathfrak{d}_{2}-\mathfrak{d}_{1}\right)} & \cdots & \mathbf{0}_{\mathfrak{d}_{1} \times\left(\mathfrak{d}_{i}-\mathfrak{d}_{i-1}\right)} \\
\mathbf{0}_{\mathfrak{d}_{1} \times\left(\mathfrak{d}_{2}-\mathfrak{d}_{1}\right)}^{\top} & \boldsymbol{\Lambda}_{\mathfrak{i i}, 2} & \cdots & \mathbf{0}_{\left(\mathfrak{d}_{2}-\mathfrak{d}_{1}\right) \times\left(\mathfrak{d}_{i}-\mathfrak{d}_{i-1}\right)} \\
\vdots & \vdots & \ddots & \vdots \\
\mathbf{0}_{\mathfrak{d}_{1} \times\left(\mathfrak{d}_{i}-\mathfrak{d}_{i-1}\right)}^{\top} & \mathbf{0}_{\left(\mathfrak{d}_{2}-\mathfrak{d}_{1}\right) \times\left(\mathfrak{d}_{i}-\mathfrak{d}_{i-1}\right)}^{\top} & \cdots & \boldsymbol{\Lambda}_{\mathfrak{i i}, \mathfrak{i}}
\end{array}\right) \in \mathbb{R}^{\mathfrak{d}_{\mathfrak{i}} \times \mathfrak{d}_{\mathfrak{i}}}
$$

with $\boldsymbol{\Lambda}_{\mathfrak{i i}, \mathfrak{j}} \in \mathbb{R}^{\left(\mathfrak{d}_{\mathfrak{j}}-\mathfrak{d}_{\mathfrak{j}-1}\right) \times\left(\mathfrak{d}_{\mathfrak{j}}-\mathfrak{d}_{\mathfrak{j}-1}\right)}$ for $\mathfrak{j}=1, \ldots, \mathfrak{\imath}$ and defining $\mathfrak{d}_{0}=0$. Based on these partitions, further define

$$
\begin{aligned}
\boldsymbol{\Delta}_{1} & =\left(\boldsymbol{\Lambda}_{11,1}+\boldsymbol{\Lambda}_{22,1}+\cdots+\boldsymbol{\Lambda}_{\mathfrak{k k}, 1}\right)^{-1 / 2} \in \mathbb{R}^{\mathfrak{d}_{1} \times \mathfrak{d}_{1}} \\
\widetilde{\boldsymbol{\Delta}}_{1} & =\left(\boldsymbol{\Lambda}_{11,1}^{2}+\boldsymbol{\Lambda}_{22,1}^{2}+\cdots+\boldsymbol{\Lambda}_{\mathfrak{k} \mathfrak{k}, 1}^{2}\right)^{-1 / 2} \boldsymbol{\Lambda}_{11,1} \in \mathbb{R}^{\mathfrak{d}_{1} \times \mathfrak{d}_{1}} \\
\boldsymbol{\Delta}_{\mathfrak{i}} & =\left(\begin{array}{cc}
\boldsymbol{\Delta}_{\mathfrak{i}-1} & \mathbf{0}_{\mathfrak{d}_{\mathfrak{i}-1} \times\left(\mathfrak{d}_{\mathfrak{i}}-\mathfrak{d}_{\mathfrak{i}-1}\right)} \\
\mathbf{0}_{\mathfrak{d}_{\mathfrak{i}-1} \times\left(\mathfrak{d}_{\mathfrak{i}}-\mathfrak{d}_{\mathfrak{i}-1}\right)}^{\top} & \left(\boldsymbol{\Lambda}_{\mathfrak{i i}, \mathfrak{i}}+\boldsymbol{\Lambda}_{(\mathfrak{i}+1)(\mathfrak{i}+1), \mathfrak{i}}+\cdots+\boldsymbol{\Lambda}_{\mathfrak{k k}, \mathfrak{i}}\right)^{-1 / 2}
\end{array}\right) \in \mathbb{R}^{\mathfrak{d}_{\mathfrak{i}} \times \mathfrak{d}_{\mathfrak{i}}} \\
\widetilde{\boldsymbol{\Delta}}_{\mathfrak{i}} & =\left(\begin{array}{cc}
\widetilde{\boldsymbol{\Delta}}_{\mathfrak{i}-1} \mathbf{D}_{\mathbf{i}} & \mathbf{0}_{\mathfrak{d}_{\mathfrak{i}-1} \times\left(\mathfrak{d}_{\mathfrak{i}}-\mathfrak{d}_{\mathfrak{i}-1}\right)} \\
\mathbf{0}_{\mathfrak{d}_{\mathfrak{i}-1} \times\left(\mathfrak{d}_{\mathfrak{i}}-\mathfrak{d}_{\mathfrak{i}-1}\right)}^{\top} & \left(\boldsymbol{\Lambda}_{\mathfrak{i i}, \mathfrak{i}}^{2}+\boldsymbol{\Lambda}_{(\mathfrak{i}+1)(\mathfrak{i}+1), \mathfrak{i}}^{2}+\cdots+\boldsymbol{\Lambda}_{\mathfrak{k k}, \mathfrak{i}}^{2}\right)^{-1 / 2} \boldsymbol{\Lambda}_{\mathfrak{i i}, \mathfrak{i}}
\end{array}\right) \in \mathbb{R}^{\mathfrak{d}_{\mathfrak{i}} \times \mathfrak{d}_{\mathfrak{i}}}
\end{aligned}
$$

for $\mathfrak{\imath}=2, \ldots, \mathfrak{k}$ with $\mathbf{D}_{\mathfrak{i}}=\operatorname{diag}\left(\boldsymbol{\Lambda}_{(\mathfrak{i}-1)(\mathfrak{i}-1), 1}^{-1} \boldsymbol{\Lambda}_{\mathfrak{i i}, 1}, \ldots, \boldsymbol{\Lambda}_{(\mathfrak{i}-1)(\mathfrak{i}-1), \mathfrak{i}-1}^{-1} \boldsymbol{\Lambda}_{\mathfrak{i i}, \mathfrak{i}-1}\right) \in \mathbb{R}^{\mathfrak{d}_{\mathfrak{i}-1} \times \mathfrak{d}_{\mathfrak{i}-1}}$. Finally, we will need the matrices

$$
\begin{aligned}
\mathbf{J} & =\mathbf{R}_{0}^{-1 / 2}\left(\mathbf{R}_{0}^{1 / 2} \mathbf{R} \mathbf{R}_{0}^{1 / 2}\right)^{1 / 2} \mathbf{R}_{0}^{-1 / 2} \\
& =\left(\begin{array}{cccc}
\mathbf{J}_{11} & \mathbf{J}_{12} & \cdots & \mathbf{J}_{1 \mathfrak{k}} \\
\mathbf{J}_{21} & \mathbf{J}_{22} & \cdots & \mathbf{J}_{2 \mathfrak{k}} \\
\vdots & \vdots & \ddots & \vdots \\
\mathbf{J}_{\mathfrak{k} 1} & \mathbf{J}_{\mathfrak{k} 2} & \cdots & \mathbf{J}_{\mathfrak{k k}}
\end{array}\right) \in \mathbb{R}^{\mathfrak{q} \times \mathfrak{q}}
\end{aligned}
$$

with $\mathbf{J}_{\mathfrak{i j}} \in \mathbb{R}^{\mathfrak{d}_{\mathfrak{i}} \times \mathfrak{d}_{\mathfrak{j}}}$ and

$$
\mathbf{J}_{0}=\operatorname{diag}\left(\mathbf{J}_{1


---

Remark 3. When $\boldsymbol{R}=\boldsymbol{R}_{0}$, it holds that $\zeta_{r}=0$ and $\sqrt{n} \widehat{D}_{r, n} \xrightarrow{p} 0$ for $n \rightarrow \infty$. The higher-order delta method can however still provide a weak convergence result for $n \widehat{D}_{r, n}$. A detailed study of this is research in progress.

We look at another example, which is also studied in [12], but in the context of $\Phi$-dependence measures.
Example 3. Consider a four dimensional random vector $\left(X_{1}, X_{2}, X_{3}, X_{4}\right)$ having a Gaussian copula with covariance matrix

$$
\left(\begin{array}{cccc}
1 & \rho_{1} & \rho_{2} & \rho_{2} \\
\rho_{1} & 1 & \rho_{2} & \rho_{2} \\
\rho_{2} & \rho_{2} & 1 & \rho_{1} \\
\rho_{2} & \rho_{2} & \rho_{1} & 1
\end{array}\right), \quad \text { where } \quad \rho_{1} \geq 2\left|\rho_{2}\right|-1
$$

Then one can check that (recall also Example 2 for finding the matrix $R_{m}$ )

$$
\begin{aligned}
& D_{1}\left(\left(X_{1}, X_{2}\right) ;\left(X_{3}, X_{4}\right)\right) \\
& =\frac{2\left(1+\rho_{1}\right)^{1 / 2}-\left(\rho_{1}-2 \rho_{2}+1\right)^{1 / 2}-\left(\rho_{1}+2 \rho_{2}+1\right)^{1 / 2}}{(2-\sqrt{2})\left\{\left(1+\rho_{1}\right)^{1 / 2}+\left(1-\rho_{1}\right)^{1 / 2}\right\}}
\end{aligned}
$$


$$
\begin{aligned}
& D_{2}\left(\left(X_{1}, X_{2}\right) ;\left(X_{3}, X_{4}\right)\right) \\
& =\frac{4-2\left|1-\rho_{1}\right|-\left(\rho_{1}^{2}+2 \rho_{1}-2 \rho_{1} \rho_{2}-2 \rho_{2}+1\right)^{1 / 2}-\left(\rho_{1}^{2}+2 \rho_{1}+2 \rho_{1} \rho_{2}+2 \rho_{2}+1\right)^{1 / 2}}{4-\sqrt{2}\left\{\left|1-\rho_{1}\right|+\rho_{1}+1\right\}}
\end{aligned}
$$

Fig. 1 shows how (19) and (20) depend on $\rho_{2}$ for different values of $\rho_{1}$. Clearly, independence holds if and only if $\rho_{2}=0$, as it should. When $\rho_{1}=2\left|\rho_{2}\right|-1$, the second principal component of $\left(Z_{1}, Z_{2}\right)=\left(\left(\Phi^{-1} \circ F_{1}\right)\left(X_{1}\right),\left(\Phi^{-1} \circ F_{2}\right)\left(X_{2}\right)\right)$ is perfectly correlated with the second principal component of $\left(Z_{3}, Z_{4}\right)=\left(\left(\Phi^{-1} \circ F_{3}\right)\left(X_{3}\right),\left(\Phi^{-1} \circ F_{4}\right)\left(X_{4}\right)\right)$, where $F_{i}$ is the marginal distribution of $X_{i}$ for $i=1,2,3,4$, see also [12]. This causes the $\Phi$-dependence measures studied in [12] to reach their maximum value, because a singularity is attained. In particular, taking for instance $\rho_{1}=-0.4$ and $\rho_{2}=0.3$, all (normalized) $\Phi$-dependence measures equal 1 , while $D_{1}=0.396$ and $D_{2}=0.3$. The reason for $D_{1}$ and $D_{2}$ still being small, is that $\rho_{2}$ is pretty small and, recalling Remark 2 , not both first and second principal components of $\left(Z_{1}, Z_{2}\right)$ and $\left(Z_{3}, Z_{4}\right)$ are perfectly correlated, only one of them is. Only when $\left|\rho_{2}\right|=1$ and thus also $\rho_{1}=1$, we have $D_{1}=D_{2}=1$. Maximal Bures-Wasserstein dependence is not attainable for the family (18) if $\rho_{1} \neq 1$, because it imposes additional restrictions on the correlations (i.e., not every element in $\Gamma\left(R_{11}, \ldots, R_{k k}\right)$ is a member of (18)). Picking a set $\mathcal{G}_{R} \subset \Gamma\left(R_{11}, \ldots, R_{k k}\right)$ for a normalization that adjusts according to these restrictions, would lead to more cases of maximal dependence.




---



Fig. 2: Asymptotic standard deviation of dependence coefficients (19) (left) and (20) (right) as a function of $\rho_{2}$ for different values of $\rho_{1}$.

Fig. 2 depicts the asymptotic standard deviation $\zeta_{r}$ of $D_{r}$ for $r \in\{1,2\}$ as given in Theorem 1 for this specific example. We mainly observe increasing behaviour when the strength of dependence increases. However, in some cases where $\rho_{1}$ and $\rho_{2}$ get close to satisfying $\left|\rho_{2}\right|=\left(\rho_{1}+1\right) / 2$, we see the asymptotic standard deviation going down. For example, if $\rho_{1}=0$, the asymptotic standard deviation $\zeta_{1}$ is maximal $(\approx 0.275)$ at $\left|\rho_{2}\right| \approx 0.426$, after which it converges to $\approx 0.214$ for $\left|\rho_{2}\right| \rightarrow 0.5$. When keeping $\rho_{1}$ fixed and letting $\left|\rho_{2}\right| \rightarrow\left(\rho_{1}+1\right) / 2$, the dependence $D_{r}$ attains a local maximum, which it cannot transcend, resulting in (slightly) lower asymptotic variance. This behaviour was also noticed in the same example in [12] for their (normalized) $\Phi$-dependence measures, whose asymptotic variance tends to zero when $\left|\rho_{2}\right| \rightarrow\left(\rho_{1}+1\right) / 2$, because the singularity forces them to reach their global maximum. For the optimal transport dependence coefficients, the global maximum is only attained when $\left|\rho_{2}\right|, \rho_{1} \rightarrow 1$, in which case the asymptotic variance also tends to zero.

# 4. A Gaussian copula approach: regularized estimation 

Empirical covariance matrices are known to approach singularity when the dimension is close to the sample size. The estimator $\widehat{D}_{r, n}$ does not require an inverted covariance matrix, but it inquires about eigenvalue dispersion, and this tends to be biased when using the empirical covariance matrix, see, e.g., [31]. Typically, estimates of large eigenvalues tend to be biased upwards, and estimates of small eigenvalues tend to be biased downwards. Increasing dimensionality aggravates this, but penalization techniques can be used to restrain. We briefly discuss ridge regularization, as in [50], but now in a Gaussian copula context.

Of course, the ridge estimator will not completely shrink elements of the empirical covariance matrix to zero. However, the task might be to find a likely estimate for which multiple variables are marginally independent, i.e., a sparse estimate of the covariance matrix having zero entries. For this purpose, we look at a Gaussian copula formulation of the penalization ideas discussed in [29]. Finally, penalties can also be applied to groups of elements instead of just individual elements. A group lasso penalty, for instance, enables to shrink entire blocks of the covariance matrix to zero.

In Section 4.1, we discuss penalization methods for the Gaussian copula covariance matrix in case $q$ remains fixed with the sample size. Afterwards, in Section 4.2, we briefly touch upon the case where $q$ depends on $n$.

### 4.1. Fixed dimension

Denote $\widehat{\boldsymbol{\Sigma}}_{M L}$ for the maximum likelihood estimator of a $\mathcal{N}_{q}\left(\mathbf{0}_{q}, \boldsymbol{\Sigma}\right)$ model, and $\boldsymbol{R}=\phi(\boldsymbol{\Sigma})=\mathbf{D}_{\boldsymbol{\Sigma}}^{-1 / 2} \boldsymbol{\Sigma} \mathbf{D}_{\boldsymbol{\Sigma}}^{-1 / 2}$ the correlation matrix corresponding to $\boldsymbol{\Sigma}$ (recall that $\mathbf{D}_{\boldsymbol{\Sigma}}$ is the diagonal matrix containing the diagonal of $\boldsymbol{\Sigma}$ ). By adding a certain penalty, say $P_{\bullet}\left(\boldsymbol{\Sigma}, \omega_{n}\right)$ to the Gaussian log-likelihood, where $\omega_{n}$ is a certain penalty parameter depending on $n$, a general penalized optimization problem for estimating $\boldsymbol{\Sigma}$ (under the constraint of positive definiteness $\boldsymbol{\Sigma} \succ \mathbf{0}$ ), is given by




---

$$
\widehat{\boldsymbol{\Sigma}}_{\bullet} \in \arg \min _{\boldsymbol{\Sigma} \succ 0}\left\{\ln |\boldsymbol{\Sigma}|+\operatorname{tr}\left(\boldsymbol{\Sigma}^{-1} \widehat{\boldsymbol{\Sigma}}_{\mathrm{ML}}\right)+P_{\bullet}\left(\boldsymbol{\Sigma}, \omega_{n}\right)\right\}
$$

and corresponding correlation matrix $\widehat{\boldsymbol{R}}_{\bullet}=\phi\left(\widehat{\boldsymbol{\Sigma}}_{\bullet}\right)$. However, the core of this paper is that we merely assume a Gaussian copula. Hence, instead of making use of $\widehat{\boldsymbol{\Sigma}}_{\mathrm{ML}}$, we compute $\widehat{\boldsymbol{\Sigma}}_{n}$, being the (block) matrix of sample normal scores rank covariances with entries $n^{-1} \sum_{\ell=1}^{n} \widehat{Z}_{i j}^{(\ell)} \widehat{Z}_{m t}^{(\ell)}$ for $i, m \in\{1, \ldots, k\}, j \in\left\{1, \ldots, d_{i}\right\}, t \in\left\{1, \ldots, d_{m}\right\}$ (similar block notation as in (10)). The main difference is that we do not have true Gaussian scores, but only non-parametrically estimated Gaussian scores $\widehat{Z}_{i j}^{(\ell)}=\Phi^{-1}\left(n /(n+1) \widehat{F}_{i j}\left(X_{i j}^{(\ell)}\right)\right)$. The copula formulation of (21) becomes

$$
\widehat{\boldsymbol{\Sigma}}_{\bullet, n} \in \arg \min _{\boldsymbol{\Sigma} \succ 0}\left\{\ln |\boldsymbol{\Sigma}|+\operatorname{tr}\left(\boldsymbol{\Sigma}^{-1} \widehat{\boldsymbol{\Sigma}}_{n}\right)+P_{\bullet}\left(\boldsymbol{\Sigma}, \omega_{n}\right)\right\}
$$

where we use the additional subscript $n$ in $\widehat{\boldsymbol{\Sigma}}_{\bullet, n}$ to indicate that we are in the copula context. A genuine Gaussian copula correlation matrix is then $\widehat{\boldsymbol{R}}_{\bullet, n}=\phi\left(\widehat{\boldsymbol{\Sigma}}_{\bullet, n}\right)$.

We go deeper into three choices for the penalty $P_{\bullet}$ :

- the ridge penalty $P_{\mathrm{R}}\left(\boldsymbol{\Sigma}, \omega_{n}\right)=\left(1-\omega_{n}\right) \operatorname{tr}\left(\boldsymbol{R}^{-1}\right)$, where $\omega_{n} \in(0,1]$
- (adaptive) lasso-type penalties $P_{\mathrm{LT}}\left(\boldsymbol{\Sigma}, \omega_{n}\right)=\sum_{i, j, m, t} p_{\omega_{n}}\left(\Delta_{i j, m t}\left|\sigma_{i j, m t}\right|\right)$, where $\sigma_{i j, m t}$ is the $(j, t)$ 'th element of the $(i, m)^{\prime}$ th block of $\boldsymbol{\Sigma}$ (similar block notation as in (10)), $\Delta_{i j, m t} \geq 0$ is a weight (e.g., zero when $(i, j)=(m, t)$ in order to not shrink diagonal elements, or larger for smaller preliminary estimated entries in order to shrink these more) and $p_{\omega_{n}}$ is a certain penalty function depending on $\omega_{n} \geq 0$
- group lasso-type penalties $P_{\mathrm{GLT}}\left(\boldsymbol{\Sigma}, \omega_{n}\right)=2 \sum_{i, m=1, m>i}^{k} p_{\omega_{n}}\left(\sqrt{d_{i} d_{m}}\left\|\boldsymbol{\Sigma}_{i m}\right\|_{F}\right)+\sum_{i=1}^{k} p_{\omega_{n}}\left(\sqrt{d_{i}\left(d_{i}-1\right)}\left\|\overline{\boldsymbol{\Delta}}_{i} * \boldsymbol{\Sigma}_{i i}\right\|_{F}\right)$, where $\|\cdot\|_{F}$ is the Frobenius matrix norm, $\overline{\boldsymbol{\Delta}}_{i} \in \mathbb{R}^{d_{i} \times d_{i}}$ a matrix with ones as off-diagonal elements and zeroes on the diagonal (in order to avoid shrinking the variances), and $p_{\omega_{n}}$ a certain penalty function depending on $\omega_{n} \geq 0$.

The ridge penalty is different from the other ones (and will also be considered separately in the simulations in Section 5) in the sense that it only focuses on improving the estimation of the Gaussian copula covariance matrix (and corresponding dependence coefficients) when $q$ is large compared to $n$, and not on a sparsity assumption. Asymptotic properties are centred around consistency. Having $q>n$ is definitely manageable for ridge penalization. For the latter two penalties, the set $\mathcal{A}$ defined as $\mathcal{A}=\left\{\alpha: \sigma_{\alpha} \neq 0, \alpha=1, \ldots, \widetilde{q}\right\}$, where $\boldsymbol{\sigma}=\operatorname{vech}(\boldsymbol{\Sigma}) \in \mathbb{R}^{\tilde{q}}$ is the vector of upper diagonal elements of $\boldsymbol{\Sigma}$ and $\widetilde{q}=q(q-1) / 2$, is of crucial importance. Indeed, next to consistency, we hope that $\mathbb{P}\left(\mathcal{A}_{n}=\mathcal{A}\right) \rightarrow 1$ for $n \rightarrow \infty$, where $\mathcal{A}_{n}=\left\{\alpha: \hat{\sigma}_{n, \alpha} \neq 0, \alpha=1, \ldots, \widetilde{q}\right\}$, with $\widehat{\boldsymbol{\sigma}}_{n}=\operatorname{vech}\left(\widehat{\boldsymbol{\Sigma}}_{\bullet, n}\right)$, a property called sparsistency. Having $q>n$ leads to degeneracy of the lasso-type estimators, which is why we restrict ourselves to $q \leq n$ in the simulations.
Example 4 shows that the sparsity of $\boldsymbol{\Sigma}$ (which is obviously preserved by $\boldsymbol{R}$ ), i.e., the entries belonging to $\mathcal{A}^{c}$, can manifest itself in different forms, calling for different shrinkage penalties.

Example 4. A covariance graph is a graphical model that represents variables as nodes and marginal dependencies as edges (similar to a Markov random field representing conditional dependencies), see, e.g., Section 1 of [4] for several references. Marginal independencies correspond to individual zeroes in the correlation matrix and many different sparsity patterns can occur. The first plot of Fig. 3 shows the sparsity structure of a correlation matrix of a random covariance graph for a total of 20 variables, where $32.5 \%$ of the elements equal zero, corresponding to the TRUE entries. A penalty of the form $P_{\mathrm{LT}}$ allows reflecting these marginal independencies in the estimated correlation matrix, and could result in a better plug-in estimator for our dependence measures.

Next, imagine a person answering a total of twenty questions in the form of seven short questionnaires $\boldsymbol{X}_{1}, \ldots, \boldsymbol{X}_{7}$, all consisting of three questions, except for $\boldsymbol{X}_{7}$, which only contains two. The interest is in the relationship between the answers of the different questionnaires. Furthermore, assume that $\boldsymbol{X}_{1}, \ldots, \boldsymbol{X}_{6}$ are on completely different topics, and all three questions are each time self-contained. Only the very last two questions contained in $\boldsymbol{X}_{7}$ are related to each other, and to the other questions in the first six questionnaires as well. Then, it can be expected that only the blocks $\boldsymbol{R}_{i 7}$ for $i=1, \ldots, 6$ and $\boldsymbol{R}_{77}$ are different from zero (and the diagonal of $\boldsymbol{R}$, of course), i.e., $\boldsymbol{R}$ has a sparsity pattern as visualized in the second plot of Fig. 3, where $76.5 \%$ of the elements equal zero. Such a pattern calls for




---



Fig. 3: Different sparsity patterns of a 20 dimensional correlation matrix.
a PGLT penalty, enabling shrinkage of entire blocks, and possibly more accurate estimation of the Gaussian copula dependence coefficients compared to using the matrix of normal scores rank correlations $\widehat{R}_{n}$, or a PLT penalty.

We shall now elaborate more on the theoretical properties and computational aspects of the estimators $\widehat{\Sigma}_{R, n}, \widehat{\Sigma}_{L T, n}$ and $\widehat{\Sigma}_{G L T, n}$ given in (22) corresponding to the three types of penalties $P_{R}, P_{L T}$ and $P_{G L T}$.

# Ridge regularization 

Warton [50] extensively studies the estimator $\widehat{\Sigma}_{R}$, i.e., the estimator (21) under the assumption of a normal distribution, with penalty term $P_{R}\left(\Sigma, \omega_{n}\right)=\left(1-\omega_{n}\right) \operatorname{tr}\left(R^{-1}\right)$ for $R=\phi(\Sigma)=D_{\Sigma}^{-1 / 2} \Sigma D_{\Sigma}^{-1 / 2}$ and $\omega_{n} \in\left(0,1\right.$. His Theorem 1 tells us that

$$
\widehat{R}_{R}=\omega_{n} \widehat{R}_{M L}+\left(1-\omega_{n}\right) I_{q}
$$

where $\widehat{R}_{M L}=\phi\left(\widehat{\Sigma}_{M L}\right)$ is the corresponding maximum penalized likelihood estimator. The value of $\omega_{n}$ is picked through $K$-fold cross-validation with the normal likelihood as objective function. If $\widehat{\lambda}_{M L}$ is an eigenvalue of $\widehat{R}_{M L}$, then $\omega_{n} \widehat{\lambda}_{M L}+1-\omega_{n}$ is an eigenvalue of $\widehat{R}_{R}$, i.e., all eigenvalues smaller than one are expanded, and all eigenvalues larger than one are shrunk towards one (recall the discrepancy of biased eigenvalue dispersion of the non-regularized empirical covariance matrix), at a pace that increases as $\omega_{n}$ decreases. Furthermore, the value of $\omega_{n}$ tends to one in probability if $n \rightarrow \infty$, and there is zero probability that $\omega_{n}=1$ (no regularization) if $\widehat{R}_{M L}$ does not have full rank, i.e., $\widehat{R}_{R}$ is guaranteed to be non-singular, even if $q>n$ (see Theorem 2 and Theorem 3 in [50]). In our Gaussian copula context, we suggest the estimator

$$
\widehat{R}_{R, n}=\omega_{n} \widehat{R}_{n}+\left(1-\omega_{n}\right) I_{q}
$$

and the same $K$-fold cross-validation procedure for selecting $\omega_{n}$, but now based on an estimated Gaussian sample. Heuristically (we do not go into detail here), the asymptotic properties of $\widehat{R}_{R}$ carry over to $\widehat{R}_{R, n}$, since we know that (see, e.g., the proof of Theorem 1) $\left\|\widehat{R}_{M L}-\widehat{R}_{n}\right\|_{\infty}=O_{p}\left(n^{-1 / 2}\right)$ for $n \rightarrow \infty$.

## Regularized estimation and sparsity

Concentrating on the fully Gaussian setting, the general penalization criterion $P_{L T}\left(\Sigma, \omega_{n}\right)=\sum_{i, j, m, t} p_{\omega_{n}}\left(\Delta_{i j, m t}\left|\sigma_{i j, m t}\right|\right)$ is considered in [29]. Typically, one takes $\Delta_{i j, m t}=0$ if $(i, j)=(m, t)$ and 1 otherwise in order to avoid penalization of the diagonal elements, which do not vanish. Another possibility is $\Delta_{i j, m t}=\left|\widehat{\sigma}_{i j, m t}\right|^{-1} \mathbb{1}\left(\left|\widehat{\rho}_{i j, m t}\right|<\rho_{n}\right)$, where $\widehat{\sigma}_{i j, m t}$ is a preliminary estimate for $\sigma_{i j, m t}$ with corresponding correlation $\widehat{\rho}_{i j, m t}$ and $0<\rho_{n}<1$ a certain threshold value,




---

i.e., we only shrink those elements that have a sufficiently small preliminary estimated correlation, and the amount of shrinkage is proportional to the size of the preliminary estimated covariance. This is an idea similar to the adaptive lasso of [13] and used in, e.g., [16]. A similar problem often arises when estimation of the precision matrix (inverse covariance matrix) is of interest, think of graphical models for example (see, e.g., [29] for some specific references). It is usually solved by first performing a local linear approximation to the penalty function (see, e.g., [52] in case of a precision matrix):

$$
p_{\omega_{n}}\left(\Delta_{i j, m t}\left|\sigma_{i j, m t}\right|\right) \approx p_{\omega_{n}}\left(\Delta_{i j, m t}\left|\widehat{\sigma}_{i j, m t}^{(\mathrm{w})}\right|\right)+\Delta_{i j, m t} p_{\omega_{n}}^{\prime}\left(\Delta_{i j, m t}\left|\widehat{\sigma}_{i j, m t}^{(\mathrm{w})}\right|\right)\left(\left|\sigma_{i j, m t}\right|-\left|\widehat{\sigma}_{i j, m t}^{(\mathrm{w})}\right|\right),
$$

with $\widehat{\sigma}_{i j, m t}^{(\mathrm{w})}$ a current estimated entry of $\boldsymbol{\Sigma}$ in step w. Hence, $\widehat{\boldsymbol{\Sigma}}_{L T}^{(\mathrm{w}+1)}$ should be taken as (typically, one iteration already suffices for satisfactory results)

$$
\widehat{\boldsymbol{\Sigma}}_{L T}^{(\mathrm{w}+1)} \in \arg \min _{\boldsymbol{\Sigma}}\left\{\ln |\boldsymbol{\Sigma}|+\operatorname{tr}\left(\boldsymbol{\Sigma}^{-1} \widehat{\boldsymbol{\Sigma}}_{M L}\right)+\sum_{i, m, j, t} \Delta_{i j, m t} p_{\omega_{n}}^{\prime}\left(\Delta_{i j, m t}\left|\widehat{\sigma}_{i j, m t}^{(\mathrm{w})}\right|\right)\left|\sigma_{i j, m t}\right|\right\}
$$

which is a weighted covariance graphical lasso problem with weights

$$
\widetilde{\Delta}_{i j, m t}=\Delta_{i j, m t} p_{\omega_{n}}^{\prime}\left(\Delta_{i j, m t}\left|\widehat{\sigma}_{i j, m t}^{(\mathrm{w})}\right|\right)
$$

We can summarize the $\widetilde{\Delta}_{i j, m t}$ values in a block matrix $\widetilde{\Delta}$ (again similar as in (10)), allowing us to rewrite (24) as

$$
\widehat{\boldsymbol{\Sigma}}_{L T}^{(\mathrm{w}+1)} \in \arg \min _{\boldsymbol{\Sigma}}\left\{\ln |\boldsymbol{\Sigma}|+\operatorname{tr}\left(\boldsymbol{\Sigma}^{-1} \widehat{\boldsymbol{\Sigma}}_{M L}\right)+\|\widetilde{\Delta} * \boldsymbol{\Sigma}\|_{1}\right\}
$$

where $\|A\|_{1}=\|\operatorname{vec}(A)\|_{1}=\sum_{i j}\left|A_{i j}\right|$ is the $L_{1}$-norm of the vector of all elements contained in $A$, and $*$ stands for elementwise multiplication. As illustrated in [4], the optimization (25) consists of a convex part $\operatorname{tr}\left(\boldsymbol{\Sigma}^{-1} \widehat{\mathbf{\Sigma}}_{M L}\right)+\|\widetilde{\Delta} * \boldsymbol{\Sigma}\|_{1}$, and a concave part $\ln |\boldsymbol{\Sigma}|$, making the entire problem non-convex (big difference with the precision matrix case, where graphical lasso is convex), i.e., convergence to a global minimum is not guaranteed. Also, when $q>n$, the solution to (25) will be degenerate because $\widehat{\boldsymbol{\Sigma}}_{M L}$ is not full rank. The authors of [4] suggest to use $\widehat{\boldsymbol{\Sigma}}_{M L}+\delta \boldsymbol{I}_{q}$ for some $\delta>0$ in such cases, where $\delta$ is chosen such that, e.g., the resulting matrix has condition number equal to $q$. Still, they encounter difficulties of estimation when $q>n$. For this reason, we restrict ourselves to $q \leq n$ in the simulations.

Using a majorize approach, they propose in [4] to solve convex approximations to the original problem in an iterative way. Next to sparsity, their algorithm achieves positive definiteness. Another optimization technique for solving (25) is developed in [49], who uses coordinate descent, resulting in a faster and more stable algorithm. We use this algorithm as it is implemented in [16].

Under a set of typical assumptions, consistency and sparsistency results for the estimator $\widehat{\boldsymbol{\Sigma}}_{L T}$ are given in [29]. One of their main conclusions is the preference for non-convex penalty functions such as the scad penalty of [14]:
$p_{\omega_{n}}^{\text {scad }}(t)= \begin{cases}\omega_{n} t & \text { for } t \leq \omega_{n} \\ \frac{1}{2(a-1)}\left(2 a \omega_{n} t-t^{2}-\omega_{n}^{2}\right) & \text { for } \omega_{n}<t \leq a \omega_{n} \\ (a+1) \omega_{n}^{2} / 2 & \text { for } t>a \omega_{n}\end{cases}$
where $a>2$. We take $a=3.7$ because of the arguments given in [14]. Such penalties shrink less entries that are large in magnitude, and as such reduce the bias. Moreover, a strong theoretical upper bound on the tuning parameter $\omega_{n}$, as is needed for, e.g., the lasso penalty $p_{\omega_{n}}^{\text {lasso }}(t)=\omega_{n} t$ (being the limit of $p_{\omega_{n}}^{\text {scad }}(t)$ for $a \rightarrow \infty$ ) in order to guarantee consistency, is not needed, yielding better sparsity properties. So, also in case of sparse covariance matrix estimation, the scad has the oracle property in the sense of [14] (zeroes are asymptotically estimated as zero, and estimated non-zeroes are asymptotically normal).

So far, we have been assuming a multivariate normal model, while the core of this paper is that we merely assume a semi-parametric normal copula model, i.e., within reach is the estimator $\widehat{\boldsymbol{\Sigma}}_{L T, n}$, and not $\widehat{\boldsymbol{\Sigma}}_{L T}$. As mentioned in [15], who use the term sparse M-estimator, "such estimation problems have benefited from a very limited attention so




---

far", and "the large sample analysis amply differs from the fully parametric viewpoint". Recall the sets $\mathcal{A}_{n}$ and $\mathcal{A}$ introduced for the property of sparsistency. Define also

$$
a_{n}=\max _{1 \leq \alpha \leq \widetilde{q}}\left\{\frac{d p_{\omega_{n}}}{d t}\left(\left|\widehat{\sigma}_{n, \alpha}\right|\right): \alpha \in \mathcal{A}_{n}\right\} \quad \text { and } \quad b_{n}=\max _{1 \leq \alpha \leq \widetilde{q}}\left\{\frac{d^{2} p_{\omega_{n}}}{d t^{2}}\left(\left|\widehat{\sigma}_{n, \alpha}\right|\right): \alpha \in \mathcal{A}_{n}\right\}
$$

where $d p_{\omega_{n}}\left(\left|\widehat{\sigma}_{n, \alpha}\right|\right) / d t$ denotes the derivative of $p_{\omega_{n}}(t)$ with respect to $t$, evaluated in $\left|\widehat{\sigma}_{n, \alpha}\right|$, and similarly for the second derivative. The sequence $a_{n}$ is related to the asymptotic bias of the penalized estimator, and equals $a_{n}=\omega_{n}$ for the lasso penalty. Theorem 2 states the consistency and sparsistency of the estimator $\widehat{\Sigma}_{\text {LT }, n}$.
Theorem 2. Assume that there exist $M, \widetilde{M}>0$ such that

$$
\left|\frac{d^{2} p_{\omega_{n}}}{d t^{2}}\left(t_{1}\right)-\frac{d^{2} p_{\omega_{n}}}{d t^{2}}\left(t_{2}\right)\right| \leq M\left|t_{1}-t_{2}\right|
$$

for any $t_{1}, t_{2} \in \mathbb{R}$ such that $t_{1}, t_{2}>\widetilde{M} \omega_{n}$. Suppose that for $a_{n}$ and $b_{n}$ defined in (26), it holds that $a_{n}, b_{n} \rightarrow 0$ when $n \rightarrow \infty$. Then, there exists a solution $\widehat{\Sigma}_{L T, n}$ to (22) with penalty $P_{\bullet}=P_{L T}$, for each $n$, satisfying

$$
\left\|\widehat{\sigma}_{n}-\sigma\right\|^{2}=O_{p}\left(\ln (\ln (n)) n^{-1 / 2}+a_{n}\right)
$$

for $n \rightarrow \infty$, where $\widehat{\sigma}_{n}=\operatorname{vech}\left(\widehat{\Sigma}_{L T, n}\right)$ and $\sigma=\operatorname{vech}(\Sigma)$. If, in addition, $\omega_{n} \rightarrow 0, a_{n} \omega_{n}^{-1} \rightarrow 0, \sqrt{n} \omega_{n}(\ln (\ln (n)))^{-1} \rightarrow \infty$ when $n \rightarrow \infty$, and

$$
\liminf _{n \rightarrow \infty} \liminf _{t \rightarrow 0} \omega_{n}^{-1} \frac{d p_{\omega_{n}}}{d t}(|t|)>0
$$

it also holds that

$$
\lim _{n \rightarrow \infty} \mathbb{P}\left(\mathcal{A}_{n}=\mathcal{A}\right)=1
$$

Proof. This follows immediately from Theorem 3.1. and Theorem 3.2. in [15], noting that the necessary assumptions are satisfied, since they are verified for the Gaussian copula case and Gaussian likelihood loss function in Section E of the Appendix in [15].
The conditions (27) and (28) are satisfied by, e.g., the lasso and scad penalty. The condition in (27) is a smoothing condition on the penalty function, and (28) guarantees sparsity in the estimates. However, note that the condition $a_{n} \omega_{n}^{-1} \rightarrow 0$ for $n \rightarrow \infty$ cannot be fulfilled by the lasso since then $a_{n}=\omega_{n}$. Hence, Theorem 2 does not guarantee sparsistency of the lasso estimator.

# Regularized estimation and group sparsity 

Recall the second plot in Fig. 3 of Example 4 , where entire groups of variables are independent of each other, and/or have no dependence within, resulting in a correlation sparsity pattern with entire zero blocks. A penalty of the form $P_{\mathrm{GLT}}\left(\Sigma, \omega_{n}\right)=2 \sum_{i, m=1, m>i}^{k} p_{\omega_{n}}\left(\sqrt{d_{i} d_{m}}\left\|\Sigma_{i m}\right\|_{F}\right)+\sum_{i=1}^{k} p_{\omega_{n}}\left(\sqrt{d_{i}\left(d_{i}-1\right)}\left\|\Delta_{i} * \Sigma_{i i}\right\|_{F}\right)$, where $\|\cdot\|_{F}$ is the Frobenius norm and $\Delta_{i} \in \mathbb{R}^{d_{i} \times d_{i}}$ a matrix with ones as off-diagonal elements and zeroes on the diagonal in order to avoid shrinkage of the variances, might lead to an estimator $\widehat{\Sigma}_{\text {GLT }, n}$ that incorporates this sparsity structure. The non-differentiability of $\|\cdot\|_{F}$ at 0 allows to simultaneously shrink all entries of a certain block, and hence performs a group selection. For actually computing $\widehat{\Sigma}_{\mathrm{GLT}, n}$, a local linear approximation of $p_{\omega_{n}}$ can again be performed, which will boil down to a similar problem as finding $\widehat{\Sigma}_{\text {GLT }, n}$ in case of the lasso penalty $p_{\omega_{n}}^{\text {lasso }}(t)=\omega_{n} t$. So, let us assume from now on that $p_{\omega_{n}}=p_{\omega_{n}}^{\text {lasso }}$. The ideas explained in [49], which we use for numerically finding $\widehat{\Sigma}_{\mathrm{LT}, n}$, can in general not be used for finding $\widehat{\Sigma}_{\text {GLT }, n}$, because some of the arguments do not apply to the Frobenius norm. Nevertheless, the problem

$$
\widehat{\Sigma}_{\mathrm{GLT}, n}^{*}=\arg \min _{\Sigma}\left\{\frac{1}{2}\left\|\Sigma-\widehat{\Sigma}_{n}\right\|_{F}^{2}+2 \omega_{n} \sum_{i, m=1}^{k} p_{i>m} \sqrt{d_{i} d_{m}}\left\|\Sigma_{i m}\right\|_{F}+\omega_{n} \sum_{i=1}^{k} \sqrt{d_{i}\left(d_{i}-1\right)}\left\|\Delta_{i} * \Sigma_{i i}\right\|_{F}\right\}
$$




---

has a solution in the form of an elementwise soft thresholding operation. Denoting $\left(\widehat{\Sigma}_{\mathrm{GLT}, n}^{*}\right)_{i j, m t}$ for the $(j, t)$ 'th element of the $(i, m)$ 'th block of $\widehat{\Sigma}_{\mathrm{GLT}, n}^{*}$, similarly for $\widehat{\Sigma}_{n}$, and further

$$
S_{i, m}=\sqrt{\sum_{j=1}^{d_{i}} \sum_{t=1}^{d_{m}} \sum_{(i, j),(m, t)}\left\{\left(\widehat{\Sigma}_{n}\right)_{i j, m t}\right\}^{2}}
$$

and

$$
\gamma_{i, m}= \begin{cases}\sqrt{d_{i} d_{m}} & \text { if } i \neq m \\ \sqrt{d_{i}\left(d_{i}-1\right)} & \text { if } i=m\end{cases}
$$

it is known that (similar to, e.g., Proposition 1 in [6])

$$
\left(\widehat{\Sigma}_{\mathrm{GLT}, n}^{*}\right)_{i j, m t}= \begin{cases}0 & \text { if } S_{i, m} \leq \omega_{n} \gamma_{i, m} \text { and }(i, j) \neq(m, t) \\ \left(\widehat{\Sigma}_{n}\right)_{i j, m t} & \text { if }(i, j)=(m, t) \\ \left(\widehat{\Sigma}_{n}\right)_{i j, m t}\left(1-\frac{\omega_{n} \gamma_{i, m}}{S_{i, m}}\right) & \text { if } S_{i, m}>\omega_{n} \gamma_{i, m} \text { and }(i, j) \neq(m, t)\end{cases}
$$

Hence, we can numerically compute $\widehat{\Sigma}_{\mathrm{GLT}, n}$ by using ideas similar to the optimization approach of [4], i.e., by majorizing $\ln |\Sigma|$ by its tangent plane and using generalized gradient descent steps, which comes down to iteratively solving (convex) problems of the form (29). For the actual implementation, we used to code available in [5], and fine-tuned it such that it can also cope with a group lasso penalty. Regarding the asymptotic properties, it is intuitively clear that a result similar to Theorem 2 will hold, with sparsistency formulated at the level of blocks instead of individual elements. For asymptotic properties in case of truly independent copies, we refer to Section 3 of [6].

# 4.2. Dimension depending on the sample size 

So far, we have been assuming that the total dimension $q$ of the random vector $X$ remains fixed with $n$. When $X \in \mathbb{R}^{q_{n}}$ for $q_{n}$ depending on $n$, of primary interest might be the behaviour of the empirical Gaussian copula covariance matrix $\widehat{R}_{n}$ given in (10). Proposition 4 (see Appendix D for a proof) tells us how the dimension $q_{n}$ influences the consistency of the estimator $\widehat{R}_{n}$ in max norm $\|A\|_{\infty}=\max _{i, j}\left|A_{i j}\right|$.
Proposition 4. Let $q_{n}$ be a sequence of dimensions depending on $n$, and $R_{n} \in \mathbb{R}^{q_{n} \times q_{n}}$ corresponding Gaussian copula covariance matrices. Assume that $\sup _{n} \lambda_{\max }\left(R_{n}\right)<\infty$, where $\lambda_{\max }$ denotes the maximum eigenvalue, and let $\widehat{R}_{n}$ be the estimator given in (10) with $q=q_{n}$. Then, it holds that

$$
\left\|\widehat{R}_{n}-R_{n}\right\|_{\infty}=\mathcal{O}_{p}\left\{\left(\ln \left(q_{n}\right) / n\right)^{1 / 2}\right\}, \quad \text { for } n \rightarrow \infty
$$

So, Proposition 4 ensures that $\widehat{R}_{n}$ is a consistent estimator as long as $\ln \left(q_{n}\right) / n \rightarrow 0$ as $n \rightarrow \infty$, i.e., as long as we are not in an ultra-high dimensional setting. In the context of the penalization techniques, one can also assume that $q=q_{n}$ depends on $n$. For the ridge regularization, this will lead to inconsistencies in high-dimensional settings, see Section 3.1 in [50] (basically because sample eigenvalues are known to be inconsistent when $q_{n} \rightarrow \infty$ ). Regarding the PLT penalties, Theorem H.1. in [15] states that

$$
\left\|\widehat{\sigma}_{n}-\sigma\right\|_{2}=\mathcal{O}_{p}\left\{\sqrt{\widetilde{q}_{n}}\left(\ln (\ln (n)) n^{-1 / 2}+a_{n}\right)\right\}
$$

where $\widetilde{q}_{n}=q_{n}\left(q_{n}-1\right) / 2$, and under the additional conditions (next to those of Theorem 2) that $\widetilde{q}_{n}^{2} \ln (\ln (n)) n^{-1 / 2} \rightarrow 0$ and $\widetilde{q}_{n}^{2} n a_{n} \rightarrow 0$ for $n \rightarrow \infty$. Hence, $q_{n}$ is allowed to increase with $n$, but consistency requires $\widetilde{q}_{n}=\mathcal{O}\left(n^{1 / 4}\right)$. If, in addition (see Theorem H.2. in [15]), $\widetilde{q}_{n} n a_{n} \omega_{n}^{-1}$ and $\sqrt{n} \omega_{n}\left(\widetilde{q}_{n} \ln (\ln (n))\right)^{-1} \rightarrow \infty$ for $n \rightarrow \infty$, true zeroes are asymptotically identified with probability one (but there might still be some false positives).

## 5. Simulation study

The aim of this section is to empirically study the finite sample performance of the (non-)regularized plug-in estimators for the Gaussian copula based dependence coefficients $D_{1}$ and $D_{2}$ discussed in Section 3. The finite- sample distribution of the estimator of Section 3, is investigated in Section 5.1, and the regularized estimators are considered in Section 5.2.




---

# 5.1. Finite-sample performance of the estimator of Section 3 

Theorem 1 gives an asymptotic normality result with explicit asymptotic variance for the estimator $\widehat{D}_{r, n}=D_{r}\left(\widehat{R}_{n}\right)$ for $r \in\{1,2\}$, with $\widehat{R}_{n}$ the matrix of sample normal scores rank correlations given in (10). Let now $\widehat{\zeta}_{r, n}$ be the plug-in estimator of the asymptotic standard deviation $\zeta_{r}$ obtained by replacing $R$ with $\widehat{R}_{n}$. By simulating a sample from a certain multivariate distribution having a Gaussian copula, we can compute a realization of the actual sampling distribution of the studentized estimator $\sqrt{n}\left(\widehat{D}_{r, n}-D_{r}\right) / \widehat{\zeta}_{r, n}$, and several replications can be used to represent characteristics of the entire distribution, which should approximately (for large $n$ ) be a standard normal one according to Theorem 1.

We consider four settings which we can generate samples from:



Fig. 4: Standard normal $Q-Q$ plots for 1000 Monte Carlo runs of the studentized plug-in estimator for $D_{1}$ in four different settings with sample sizes $n=50,200,1000,5000$. The median ("Med") of the studentized estimates is given in blue.

- Setting 1: $k=2, d_{1}=d_{2}=2$, with standard normal marginals and a Gaussian copula having an autoregressive $A R(1)$ correlation matrix with $\rho=0.25$ (i.e., the $(i, j)$ 'th element of $R$ equals $\left.0.25^{|i-j|}\right)$.
- Setting 2: as Setting 1, but now with marginals
- a $t$ distribution with 3 degrees of freedom for $X_{11}$
- an exponential distribution with mean 1 for $X_{12}$
- a beta distribution with parameters 2 and 2 for $X_{21}$
- an $F$-distribution with degrees of freedom 2 and 6 for $X_{22}$.
- Setting 3: similar to Setting 1, but with $\rho=0.8$.
- Setting 4: $k=5, d_{1}=4, d_{2}=5, d_{3}=3, d_{4}=1, d_{5}=2$, with standard normal marginals and a Gaussian copula having an equicorrelated correlation matrix with $\rho=0.5$.




---

Each time, we draw 1000 samples of sizes $n=50,200,1000,5000$ and make standard normal Q-Q plots to assess the goodness-of-fit with a standard normal distribution. See Fig. 4 for the results in case of $D_{1}$. Similar plots are obtained for $D_{2}$. In each setting, there is a qualitative fit with the standard normal distribution for larger sample sizes. Changing the marginals has no influence (Setting 1 versus Setting 2). Small correlations (Settings 1 and 2), yield a more pronounced lack-of-fit than higher correlations (Setting 3). Increasing the total dimension to 15 (Setting 4) results in a large positive bias for small sample sizes, calling for regularization techniques.

Next, in Fig. 2, asymptotic standard deviations $\zeta_{1}$ and $\zeta_{2}$ were shown in the context of Example 3. Generating $N$ samples from, e.g., a multivariate normal distribution with mean zero and covariance matrix given in (18), we obtain $N$ estimates $\widehat{D}_{r, n}^{(1)}, \ldots, \widehat{D}_{r, n}^{(N)}$, whose sample standard deviation multiplied with $\sqrt{n}$, say $\widehat{\zeta}_{r}$, can be seen as an approximation for $\zeta_{r}$ when $n$ is large. Fig. 5 depicts $\widehat{\zeta}_{r}$ for different values of $\rho_{1}$ and $\rho_{2}$ in case $n=10000$ and $N=1000$. We see the same patterns popping up as in Fig. 2, illustrating the asymptotic variance formula given in Theorem 1 empirically in this particular setting.



Fig. 5: Empirical standard deviation (sample size $N=1000$ ) $\widehat{\zeta}_{r}$ for $r \in\{1,2\}$ in the setting of Example 3 when $n=10000$.

# 5.2. Penalization techniques 

We now turn our attention to the different covariance matrix penalization techniques discussed in Section 4. We start with illustrating ridge regularization, in particular the improvements it gives in plug-in estimation of Gaussian copula based dependence coefficients between multiple random vectors. We do this for increasing values of $q$, possibly larger than $n$. Recall that the ridge estimator is rather easy to compute, and there are no additional difficulties when $q>n$. This study thus also allows for an impression on how the dependence coefficients behave with increasing $q$. Afterwards, we go to sparsity inducing (group)-lasso type methods, and investigate for two fixed values of $q$ and different sample sizes (with $q<n$ ) their ability of recovering marginal independencies (interpretability) on the one hand, and whether this improves the estimation of the dependence coefficients (accuracy) on the other hand.

## Ridge regularization

As explained in Section 4, the ridge estimator $\widehat{\mathcal{R}}_{R, n}$ of the Gaussian copula correlation matrix tries to cope with biased eigenvalue dispersion of the empirical correlation matrix which aggravates when $q$ is large compared to $n$. Moreover, it is easy to implement (with a straightforward cross-validation procedure for selecting the penalty parameter $\left.\omega_{n}\right)$, and guarantees a positive definite outcome. One can expect that the performance of the estimator $D_{r}\left(\widehat{\mathcal{R}}_{R, n}\right)$ is




---

better than the performance of $D_{r}\left(\widehat{\mathbf{R}}_{n}\right)$ when $q$ is large compared to $n$. To demonstrate this, we consider the following two designs:

- Design 1: We let $q \in\{4,6,8, \ldots, 98\}$ and $k=q / 2$ with $d_{1}=d_{2}=\cdots=d_{k}=2$, e.g., if $q=30$, we are measuring the dependence between 15 random vectors of dimension 2
- Design 2: We let $q \in\{4,6,8, \ldots, 98\}$ and $k=2$ with $d_{1}=d_{2}=q / 2$, e.g., if $q=30$, we are measuring the dependence between 2 random vectors of dimension 15 .

In each design, we generate 1000 samples of sizes $n=50,100,500$ from a $\mathcal{N}_{q}\left(\mathbf{0}_{q}, \mathbf{R}\right)$ distribution (but, assume unknown marginals), where $\mathbf{R}$ is the correlation matrix of an $\operatorname{AR}(1)$ process with $\rho=0.5$, and compute the empirical mean squared error of $D_{r}\left(\widehat{\mathbf{R}}_{\mathrm{R}, n}\right)$ and $D_{r}\left(\widehat{\mathbf{R}}_{n}\right)$


The penalty parameter $\omega_{n}$ is determined by 5 -fold cross-validation (as described by equation (4) in [50]) on a grid of 50 equidistant elements in $[0.01,0.999]$. In addition, we do the same for two Gaussian copula-based $\Phi$-dependence measures discussed in [12], known as the (normalized) mutual information and Hellinger distance, respectively given by

$$
D_{t \ln (t)}(\mathbf{R})=\left(1-\frac{|\mathbf{R}|}{\prod_{i=1}^{k}\left|\mathbf{R}_{i i}\right|}\right)^{1 / 2}, \text { and } D_{(\sqrt{t}-1)^{2}}(\mathbf{R})=1-\frac{2^{q / 2}|\mathbf{R}|^{1 / 4}}{\left|\mathbf{I}_{q}+\mathbf{R}_{0}^{-1} \mathbf{R}\right|^{1 / 2} \prod_{i=1}^{k}\left|\mathbf{R}_{i i}\right|^{1 / 4}}
$$

where $\mathbf{R}_{0}$ is given in (4), and $|\cdot|$ denotes the determinant. Note that the dependence coefficients in (30) depend on products of eigenvalues (they are based on divergences of copula densities), while $D_{1}$ and $D_{2}$ depend on sums of eigenvalues (arising from the Bures-Wasserstein distance).

Fig. 6 shows plots of the logarithm of the Monte Carlo mean squared error of $D_{\bullet}\left(\widehat{\mathbf{R}}_{\mathrm{R}, n}\right)$ (penalty) and $D_{\bullet}\left(\widehat{\mathbf{R}}_{n}\right)$ (no penalty) for the four dependence measures for each sample size in both designs as a function of $q$. In all cases, we see vast improvements when using ridge regularization, especially when $n$ is small compared to $q$ (note that when $n=50$ and $q>50$, the estimators $D_{\bullet}\left(\widehat{\mathbf{R}}_{n}\right)$ are not defined because of singularity of $\left.\widehat{\mathbb{R}}_{n}\right)$. Fig. 7 shows boxplots of the selected values for the penalization parameter $\omega_{n}$. We clearly see compatibility with the theoretical property that $\omega_{n}$ tends to one in probability when $n \rightarrow \infty$, and higher dimensions require a larger correction of the eigenvalue dispersion, i.e., a smaller $\omega_{n}$.




---



Fig. 7: Boxplots of selected penalty parameter $\omega_{n}$ via a 5 -fold cross-validation search on a grid of 50 equidistant elements in $[0.01,0.999]$, for different values of $n$ and $q$.

Finally, Fig. 6 also indicates that it would be interesting to study the behaviour of the dependence coefficients when $q \rightarrow \infty$, which can happen in multiple ways. In the first design for example, $d_{i}$ remains fixed for all $i=$ $1, \ldots, k$, but $k \rightarrow \infty$. Because $\Phi$-dependence measures satisfy Axiom (A4) of Appendix A (see, e.g., [12]), we know that $\mathcal{D}_{\ln (t)}, \mathcal{D}_{(\sqrt{t}-1)^{2}} \rightarrow 1$ when $k \rightarrow \infty$, which is probably why the mean squared error of $\widehat{\mathcal{D}}_{\ln (t)}, \widehat{\mathcal{D}}_{(\sqrt{t}-1)^{2}}$ first increases and afterwards decreases/becomes constant (in particular, the variance tends to 0 when $k \rightarrow \infty$, and the bias decreases/becomes constant, see Fig. S1 and S2 of the Supplementary Material for plots of the bias and variance). Regarding the optimal transport dependence measures $\mathcal{D}_{1}$ and $\mathcal{D}_{2}$, we expect them (based on our simulations) to converge to 0 when $k \rightarrow \infty$, probably because the strong normalization (denominator) grows faster than the numerator does. We see the variance of $\widehat{\mathcal{D}}_{r}$ decreasing in $q$, and the biases increasing in $q$.

In the second design, $k=2$ remains fixed, but $d_{1}=d_{2} \rightarrow \infty$. The optimal transport measures seem (in our simulations) to converge to zero again, while the $\Phi$-dependence measures remain constant. We leave a formal study of the behaviour of these dependence coefficients when $q \rightarrow \infty$ for further research.

# (Adaptive/Group) lasso-type estimation 

Recall the two different sparsity patterns discussed in Example 4 for a $20 \times 20$ correlation matrix. By performing lasso-type estimation, we hope to recover zero entries (interpretability) on the one hand, and improve accuracy on the other hand. In particular, for the latter, we desire better performance of the plug-in estimator $\widehat{\mathcal{D}}=\mathcal{D}\left(\widehat{R}_{\bullet, n}\right)$ than of the non-penalized estimator $\mathcal{D}\left(\widehat{R}_{n}\right)$, where $\mathcal{D}$ is a certain correlation matrix based dependence coefficient.

For the simulation, we consider the following correlation structures

- Scenario 1: We take $q=20$ with $k=7, d_{1}=\cdots=d_{6}=3$ and $d_{7}=2$ having the non-block sparse correlation structure given in the left plot of Fig. 3, with $32.5 \%$ zeroes.




---

- Scenario 2: We take $q=20$ with $k=7, d_{1}=\cdots=d_{6}=3$ and $d_{7}=2$ such that $\boldsymbol{X}_{1}, \ldots, \boldsymbol{X}_{6}$ have independence within and between each other, but all components of $\boldsymbol{X}_{7}$ are related and all dependent on all components of $\boldsymbol{X}_{1}, \ldots, \boldsymbol{X}_{6}$, i.e., the block sparse correlation structure of Example 4, right plot in Fig. 3, with $76.5 \%$ zeroes.
- Scenario 3: We take $q=70$ with $k=4, d_{1}=d_{2}=d_{3}=21$ and $d_{4}=7$ such that there is only dependence with and within $\boldsymbol{X}_{4}$, yielding a block sparse correlation structure, with $79.7 \%$ zeroes.

Each time, we generate 1000 samples from a $\mathcal{N}_{q}\left(\mathbf{0}_{q}, \boldsymbol{R}\right)$ distribution (marginals are again assumed to be unknown), and compute the no penalty, lasso, adaptive lasso (of [16] with $\omega_{n}=1$ and tuning parameter $\rho_{n}$ ), scad, and group lasso estimator for $\boldsymbol{R}$. The considered sample sizes are $n=50,100,500$ for Scenarios 1 and 2 , and $n=100,500$ for Scenario 3. Based on the 1000 replications, we report on the average true positive rate (TPR), which we want to be close to one, and false positive rate (FPR), which we want to be close to zero. We also compute the empirical root mean squared error of $\|\widehat{\boldsymbol{R}}-\boldsymbol{R}\|_{\mathrm{F}} / q$ (where $\widehat{\boldsymbol{R}}$ is the estimated correlation matrix in question), and empirical mean squared error of $\widehat{\mathcal{D}}$, with $\mathcal{D}$ the mutual information $D t \ln (t)$, Hellinger distance $D(\sqrt{t}-1)^{2}$, or one of the optimal transport dependence measures $\mathcal{D}_{1}$ or $\mathcal{D}_{2}$.
For tuning $\omega_{n}$ (or $\rho_{n}$ in case of the adaptive lasso), we use the BIC criterion (see, e.g., [17] for the case of a precision matrix in Gaussian graphical models):

$$
\operatorname{BIC}\left(\widehat{\boldsymbol{\Sigma}}_{\omega_{n}}\right)=-n\left[\ln \left|\widehat{\boldsymbol{\Sigma}}_{\omega_{n}}\right|+\operatorname{tr}\left(\widehat{\boldsymbol{\Sigma}}_{\omega_{n}}^{-1} \widehat{\boldsymbol{\Sigma}}_{n}\right)\right]-\ln (n) \operatorname{df}\left(\widehat{\boldsymbol{\Sigma}}_{\omega_{n}}\right)
$$

where $\widehat{\boldsymbol{\Sigma}}_{\omega_{n}}$ is the estimated candidate covariance matrix using the penalty parameter $\omega_{n}$. We want to maximize (31) in $\omega_{n}$. We do this over an equidistant grid of 50 values in [0.01;0.6]. The number $\operatorname{df}\left(\widehat{\boldsymbol{\Sigma}}_{\omega_{n}}\right)$ stands for the degrees of freedom, and is estimated for the (adaptive) lasso and scad by the number of non-zero entries in $\widehat{\boldsymbol{\Sigma}}_{\omega_{n}}$, not taking the elements under the diagonal into account. For the group lasso, the degrees of freedom can be estimated in a similar spirit as equation (23) in [9]:

$$
\begin{aligned}
& \operatorname{df}\left(\widehat{\boldsymbol{\Sigma}}_{\omega_{n}}\right)=\sum_{i, m=1}^{k} \mathbb{1}\left(\left\|\widehat{\boldsymbol{\Sigma}}_{\omega_{n}, i m}\right\|_{\mathrm{F}}>0\right)\left(1+\frac{\left\|\widehat{\boldsymbol{\Sigma}}_{\omega_{n}, i m}\right\|_{\mathrm{F}}}{\left\|\widehat{\boldsymbol{\Sigma}}_{n, i m}\right\|_{\mathrm{F}}}\left(d_{i} d_{m}-1\right)\right) \\
& +\sum_{i=1}^{k} \mathbb{1}\left(\left\|\boldsymbol{\Delta}_{i} * \widehat{\boldsymbol{\Sigma}}_{\omega_{n}, i i}\right\|_{\mathrm{F}}>0\right)\left(1+\frac{\left\|\boldsymbol{\Delta}_{i} * \widehat{\boldsymbol{\Sigma}}_{\omega_{n}, i i}\right\|_{\mathrm{F}}}{\left\|\boldsymbol{\Delta}_{i} * \widehat{\boldsymbol{\Sigma}}_{n, i i}\right\|_{\mathrm{F}}}\left(\frac{d_{i}\left(d_{i}-1\right)}{2}-1\right)\right)+q,
\end{aligned}
$$

where $\widehat{\boldsymbol{\Sigma}}_{\omega_{n}, i m}$ is the $(i, m)^{\prime}$ th block of $\widehat{\boldsymbol{\Sigma}}_{\omega_{n}}$, similarly for $\widehat{\boldsymbol{\Sigma}}_{n, i m}$, and $\boldsymbol{\Delta}_{i i} \in \mathbb{R}^{d_{i} \times d_{i}}$ is a matrix with ones as off-diagonal elements and zeroes on the diagonal. The results are summarized in Table 1.
In Scenario 1 ( $q=20$, no block sparsity, $32.5 \%$ zeroes), there is no group sparsity, which results in low TPR (and also low FPR, since only few entries get shrunk to zero) for the group lasso estimator. The other penalization techniques are, as expected, preferred for recovering zeroes. Clearly, any type of considered penalization yields more accurate estimation of $\boldsymbol{R}$ in Frobenius norm than in case no penalty is used. However, this does not necessarily imply better estimation of the dependence coefficients, especially for lasso and scad. For good estimation of these, it is important not to lose sight of the $67.5 \%$ non-zero entries, which is why the adaptive lasso performs really well. Note that the mutual information is estimated very well in the non-penalized case, but this is mainly due to the fact that the true value equals 0.994 , which is very close to one, being an effect of the dimension (recall also Fig. 6). All non-penalized mutual information estimates are close to one because of a relatively large $q$, yielding low estimation error.
In Scenario 2 ( $q=20$, block sparsity, $76.5 \%$ zeroes), all penalization techniques perform well in identifying zeroes. For obtaining both high TPR and low FPR, the group lasso performs slightly better than lasso and scad. Also, when the focus is on estimating $\boldsymbol{R}$, penalization is clearly beneficial, and the group lasso outperforms the other techniques. Regarding the dependence coefficients, we see that, for the optimal transport measures, lasso and scad give improvement compared to using no penalty, especially for smaller sample sizes. The error of the $\Phi$-dependence




---

Table 1: True positive rate (TPR), false positive rate (FPR), and empirical mean squared error for the estimated correlation matrix and corresponding plug-in estimators of dependence coefficients based on 1000 replications in different scenarios, using different penalties.

| Scenario 1 ( $q=20$, no block sparsity, $32.5 \%$ zeroes) |  |  |  |  |  |  |  |  |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| n | TPR | FPR | $\|\widehat{R}-R\|_{\mathrm{F}} / q$ | $\widehat{D}_{t \ln (t)}$ | $\widehat{D}_{(\sqrt{t}-1)^{2}}$ | $\widehat{D}_{1}$ | $\widehat{D}_{2}$ |  |
| 50 | $\ $" | $不可$ | 0.137 | $3.993 \cdot 10^{-4}$ | 0.109 | 0.058 | 0.057 |  |
| 100 |  | $\ "$ | 0.096 | $2.898 \cdot 10^{-4}$ | 0.044 | 0.026 | 0.026 |  |
| 500 |  |  | 0.043 | $8.331 \cdot 10^{-5}$ | 0.009 | 0.005 | 0.005 |  |
| 50 | 0.831 | 0.592 | 0.105 | 0.209 | 0.327 | 0.054 | 0.052 |  |
| 100 | 0.724 | 0.355 | 0.077 | 0.005 | 0.153 | 0.032 | 0.031 | lasso |
| 500 | 0.554 | 0.121 | 0.039 | 0.001 | 0.054 | 0.014 | 0.014 |  |
| 50 | 0.818 | 0.565 | 0.122 | 0.002 | 0.075 | 0.025 | 0.025 | adaptive lasso |
| 100 | 0.848 | 0.480 | 0.092 | $2.640 \cdot 10^{-4}$ | 0.030 | 0.012 | 0.013 |  |
| 500 | 0.932 | 0.303 | 0.044 | $8.041 \cdot 10^{-5}$ | 0.010 | 0.003 | 0.004 |  |
| 50 | 0.831 | 0.592 | 0.105 | 0.209 | 0.327 | 0.054 | 0.053 |  |
| 100 | 0.744 | 0.373 | 0.078 | 0.006 | 0.165 | 0.035 | 0.034 |  |
| 500 | 0.432 | 0.091 | 0.039 | 0.001 | 0.054 | 0.014 | 0.014 |  |
| 50 | 0.074 | 0.038 | 0.091 | 0.045 | 0.116 | 0.024 | 0.023 | group lasso |
| 100 | 0.062 | 0.026 | 0.073 | 0.004 | 0.130 | 0.029 | 0.028 |  |
| 500 | 0.020 | 0.006 | 0.042 | 0.001 | 0.067 | 0.018 | 0.018 |  |
| Scenario 2 ( $q=20$, block sparsity, $76.5 \%$ zeroes) |  |  |  |  |  |  |  |  |
| n | TPR | FPR | $\|\widehat{R}-R\|_{\mathrm{F}} / q$ | $\widehat{D}_{t \ln (t)}$ | $\widehat{D}_{(\sqrt{t}-1)^{2}}$ | $\widehat{D}_{1}$ | $\widehat{D}_{2}$ |  |
| 50 | $\backslash$ | $\backslash$ | 0.138 | 0.006 | 0.178 | 0.065 | 0.064 |  |
| 100 | $\backslash$ | $不可$ | 0.097 | 0.004 | 0.077 | 0.030 | 0.030 |  |
| 500 |  |  | 0.043 | 0.001 | 0.016 | 0.006 | 0.006 |  |
| 50 | 0.940 | 0.340 | 0.058 | 0.108 | 0.246 | 0.026 | 0.026 |  |
| 100 | 0.903 | 0.135 | 0.033 | 0.020 | 0.139 | 0.013 | 0.013 | lasso |
| 500 | 0.888 | 0.048 | 0.013 | 0.004 | 0.048 | 0.005 | 0.005 |  |
| 50 | 0.858 | 0.431 | 0.101 | 0.010 | 0.103 | 0.024 | 0.024 | adaptive lasso |
| 100 | 0.860 | 0.329 | 0.076 | 0.004 | 0.053 | 0.013 | 0.013 |  |
| 500 | 0.900 | 0.164 | 0.032 | 0.001 | 0.013 | 0.003 | 0.003 |  |
| 50 | 0.940 | 0.340 | 0.058 | 0.108 | 0.246 | 0.026 | 0.026 |  |
| 100 | 0.906 | 0.137 | 0.033 | 0.021 | 0.142 | 0.013 | 0.013 |  |
| 500 | 0.846 | 0.051 | 0.016 | 0.005 | 0.062 | 0.006 | 0.006 |  |
| 50 | 0.889 | 0.011 | 0.035 | 0.021 | 0.138 | 0.013 | 0.013 | group lasso |
| 100 | 0.934 | 0.012 | 0.021 | 0.011 | 0.108 | 0.010 | 0.010 |  |
| 500 | 0.965 | 0.013 | 0.008 | 0.003 | 0.044 | 0.004 | 0.004 |  |




---

estimates is rather low in case no penalty is used, which is again an effect of the dimension. Aside from this, the group lasso or the adaptive lasso (especially for larger sample sizes) gives the lowest error.

In Scenario 3 ( $q=70$, block sparsity, $79.7 \%$ zeroes), the group lasso is again desirable for exploiting the sparsity structure, and even achieves zero FPR. For accurate estimation of $\mathbf{R}$ in Frobenius norm, the group lasso also performs best. Most accurate estimation of dependence (except for the mutual information, where no penalty performs best because the true value is again very close to one) is obtained by the group lasso when $n=100$, and by the adaptive lasso when $n=500$ is large compared to $q$.

In conclusion, when the true correlation matrix is sparse, interpretability can be enhanced by using a penalty that is able to completely shrink entries to zero. The group lasso is preferred for obtaining both good TPR and FPR when this sparsity is at the block level (Scenarios 2 and 3), and also performs well in estimating dependence in such cases, particularly when $n$ is rather small. The true $\mathbf{R}$ is estimated more accurately (compared to using no penalty) in Frobenius norm when using any penalty and in any scenario, but this does not necessarily result in better estimation of dependence. Especially when there are still quite some non-zeroes (Scenario 1), but also when $n$ is rather large, adaptive lasso is recommended for good accuracy of the estimated dependence coefficients. The $\Phi$-dependence measures are estimated with rather low error when using no penalty, but this is because they attain their upper bound of 1 rather quickly when the dimension increases.

# 6. Real data applications 

In Section 6.1, we look into an application of optimal transport dependence measures between possibly more than two random vectors to sensory analysis. In Section 6.2, we illustrate how these measures, together with the considered penalization techniques, can be useful in finding clusters among speech signal attributes used for detecting Parkinson's disease.

### 6.1. Application to sensory analysis

Consider a caterer who wants to sell eight different smoothies, say $S^{1}, \ldots, S^{8}$, on an event, and is looking for
Scenario 3 ( $q=70$, block sparsity, $79.7 \%$ zeroes)


three employees willing to take up this job. A total of 24 people, say $P_{1}, \ldots, P_{24}$, show up for this job opportunity, all equally qualified, and the caterer is looking for a fair way to pick three candidates. Every candidate is asked to taste each of the eight smoothies, and is given a sheet of paper in order to position the different smoothies, knowing that the closer certain smoothies are to each other, the more similar they are considered by the individual. For example, according to candidate $P_{j}$ in Fig. 8, the smoothies $S^{1}, S^{2}, S^{3}$ and $S^{4}$ are similar, but quite different from the similarly tasting smoothies $S^{5}, S^{6}$ and $S^{7}$, and none of them resembles $S^{8}$. As such, the caterer acquires 24 datasets, say




---



Fig. 8: Example of smoothie similarity rating by candidate $P_{j}$ on a sheet of paper and corresponding dataset $X_{j}$.
$X_{j} \in \mathbb{R}^{8 \times 2}$ for $j=1, \ldots, 24$, containing the smoothies as rows and the $X-Y$ coordinates on the sheet of paper for person $j$, denoted as a random vector $\left(X_{j}, Y_{j}\right)$, as columns, representing the smoothie similarities of each candidate. So, the dataset $X_{j}$ contains a sample from $\left(X_{j}, Y_{j}\right)$ of size eight, denoted as $\left(x_{i j}, y_{i j}\right)$ for $i=1, \ldots, 8$. The data is available in the R package SensoMineR ([30]). The criterion based on which three employees are picked consists of finding the three individuals that have the least similar spatial configurations, meaning three very diversified tastes (in the hope of not selling only a few smoothies because of prepossessed preferences by the sellers).

Typically, see, e.g., [32], the similarity between two configurations is measured by the RV coefficient

$$
R V\left(X_{j_{1}}, X_{j_{2}}\right)=\frac{\operatorname{tr}\left(X_{j_{1}} X_{j_{1}}^{\mathrm{T}} X_{j_{2}} X_{j_{2}}^{\mathrm{T}}\right)}{\sqrt{\operatorname{tr}\left\{\left(X_{j_{1}} X_{j_{1}}^{\mathrm{T}}\right)^{2}\right\} \operatorname{tr}\left\{\left(X_{j_{2}} X_{j_{2}}^{\mathrm{T}}\right)^{2}\right\}}}
$$

and for three configurations one can take, e.g., the average of all pairwise RV coefficients. Yet, pairwise coefficients feel unnatural and it would be better to compute a trivariate vector similarity. Note that (32) is actually the RV coefficient between two random vectors $\left(X_{j_{1}}, Y_{j_{1}}\right)$ and $\left(X_{j_{2}}, Y_{j_{2}}\right)$ of size two having joint, empirical covariance matrix

$$
\left(\begin{array}{l}
X_{j_{1}}^{\top} X_{j_{1}} \quad X_{j_{1}}^{\top} X_{j_{2}} \\
X_{j_{2}}^{\top} X_{j_{1}} \quad X_{j_{2}}^{\top} X_{j_{2}}
\end{array}\right) \in \mathbb{R}^{4 \times 4}
$$

and we get a similar (larger) block covariance matrix in $\mathbb{R}^{2 m \times 2 m}$ when taking $m$ individuals into account.
Since not restricted to two random vectors anymore, one can also opt for an (estimated) optimal transport dependence coefficient $D_{1}$ or $D_{2}$ between three vectors of size two for measuring the similarity between three individual spatial configurations. Note that the dispersion of the coordinates might differ among the individuals (some might use the entire sheet, while others only use the right corner), but since we use the normal scores rank correlations, we do not need any centering or scaling of the data. Pairwise scatterplots of the normal scores of the $X-Y$ coordinates of the 24 people are shown in Fig. S3 of the Supplementary Material, indicating that dependencies are mainly correlation based, i.e., a Gaussian copula model is suitable for modelling the dependencies. When zooming in on candidates $P_{12}, P_{13}, P_{18}$ and $P_{20}$, we get the pairwise scatterplots given in Fig. 9. From this, we expect for example that candidates $P_{12}$ and $P_{13}$ have quite independent smoothies preferences, while candidates $P_{18}$ and $P_{20}$ have rather strong correlations between their coordinates.

We denote $\widehat{D}_{r}\left(P_{j_{1}}, P_{j_{2}}\right)$ and $\widehat{D}_{r}\left(P_{j_{1}}, P_{j_{2}}, P_{j_{3}}\right)$ for the estimated similarity between two candidates $P_{j_{1}}, P_{j_{2}}$ or three candidates $P_{j_{1}}, P_{j_{2}}, P_{j_{3}}$ for $r=1,2$. Recall that these are actually dependencies between 2 and 3 random vectors of




---

Table 2: Arrangement of two and three candidates according to largest estimated similarity $\widehat{D}_{r}$ for $r=1,2$. The first two and last two are shown.

| two based on $\widehat{D}_{1}$ |  | two based on $\widehat{D}_{2}$ |  | three based on $\widehat{D}_{1}$ |  | three based on $\widehat{D}_{2}$ |  |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $\widehat{D}_{1}\left(P_{18}, P_{20}\right)$ | 0.561 | $\widehat{D}_{2}\left(P_{18}, P_{20}\right)$ | 0.561 | $\widehat{D}_{1}\left(P_{15}, P_{18}, P_{20}\right)$ | 0.585 | $\widehat{D}_{2}\left(P_{15}, P_{18}, P_{20}\right)$ | 0.595 |
| $\widehat{D}_{1}\left(P_{9}, P_{23}\right)$ | 0.542 | $\widehat{D}_{2}\left(P_{15}, P_{20}\right)$ | 0.521 | $\widehat{D}_{1}\left(P_{9}, P_{10}, P_{23}\right)$ | 0.550 | $\widehat{D}_{2}\left(P_{10}, P_{18}, P_{23}\right)$ | 0.561 |
| $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ |
| $\widehat{D}_{1}\left(P_{12}, P_{19}\right)$ | 0.020 | $\widehat{D}_{2}\left(P_{12}, P_{19}\right)$ | 0.016 | $\widehat{D}_{1}\left(P_{2}, P_{3}, P_{14}\right)$ | 0.080 | $\widehat{D}_{2}\left(P_{2}, P_{12}, P_{19}\right)$ | 0.075 |
| $\widehat{D}_{1}\left(P_{12}, P_{13}\right)$ | 0.015 | $\widehat{D}_{2}\left(P_{12}, P_{13}\right)$ | 0.013 | $\widehat{D}_{1}\left(P_{12}, P_{13}, P_{21}\right)$ | 0.069 | $\widehat{D}_{2}\left(P_{12}, P_{13}, P_{21}\right)$ | 0.074 |



Fig. 9: Pairwise scatterplots of normal scores of $X-Y$ coordinates of candidates $P_{12}, P_{13}, P_{18}$ and $P_{20}$ of the smoothies dataset.



Fig. 10: Boxplot of $p$-values of pairwise goodness-of-fit tests for Gaussian copula on 91 dysphonia measures of the LSVT dataset.
size 2 respectively, i.e., $q=4$ with $k=2, d_{1}=d_{2}=2$, or $q=6$ with $k=3, d_{1}=d_{2}=d_{3}=2$ respectively, estimated based on a sample of size $n=8$.

Table 2 shows the two strongest and two weakest couples or triplets according to $\widehat{D}_{1}$ or $\widehat{D}_{2}$. The caterer will definitely hire candidate $P_{12}, P_{13}$ and $P_{21}$. In [32], they cluster the candidates using the clustatis method, bringing forward three classes of individuals, see their Fig. 5. We see that $P_{12}$ belongs to class 2, while $P_{13}$ belongs to class 3 and $P_{21}$ to class 1 , also indicating their diversified smoothie similarity pattern. The optimal transport dependence measures give an unequivocal ordering of patterns based on similarities that go beyond two random vectors.
Note that we can also switch the role of the smoothies and the individuals, i.e., construct 8 datasets in $\mathbb{R}^{24 \times 2}$, and similarly look at the dependence between smoothies. Doing so, both $\widehat{D}_{1}(=0.0336)$ and $\widehat{D}_{2}(=0.0340)$ agree that $S_{6}, S_{7}$ and $S_{8}$ are the least similar among all possible triplets. They are respectively called Casino PBC, Innocent SB and Carrefour SB, and the biplots (based on various sensometrics methods) in Fig. 2. of [32] indeed also reveal angels between these smoothies that are close to $90^{\circ}$. So, $S_{6}, S_{7}$ and $S_{8}$ would be a good choice if the caterer wanted to limit his smoothie supply to three flavours that still have a satisfactory amount of diversity.

# 6.2. Clustering dysphonia measures 

In a second real data application, we study the LSVT voice rehabilitation dataset of [47], freely accessible at the UCI Machine Learning Repository (https://archive.ics.uci.edu/dataset/282/lsvt+voice+rehabilit




---

ation). Parkinson's disease frequently leads to vocal impairment, the extent of which can be assessed using sustained vowel phonations. In particular, the sustained vowel "ahh..." (denoted as /a/) is typically studied. Next, dysphonia measures are used to extract clinically useful information from speech signals. The dataset consists of $q=310$ such measurements on $n=126$ phonations. As mentioned in Section C of [47], several of these dysphonia measures are similar (algorithmic variations of the same basic ideas), e.g., there are many jitter (a measure of cycle-to-cycle variation in frequency) and shimmer (a measure of cycle-to-cycle variation in amplitude) variants. Hence, there is a large amount of redundancy among the attributes, which could worsen the performance of supervised learning (like, e.g., a classifier as studied in [47]), and some kind of preliminary feature selection is recommended.

There are indeed many dysphonia measures that exhibit a (very) strong sample normal scores rank correlation, see Fig. S4 of the Supplementary Material. In order to eliminate strong detrimental redundancies (that closely approach singularity), we iteratively search (pairwise) for attributes that have a normal scores rank correlation larger than 0.8 in absolute value, and each time discard one of them. Remaining are 91 dysphonia measures, whose (non-singular) sample normal scores rank correlation matrix is given in the left panel of Fig. S5 of the Supplementary Material.

For testing the adequacy of a Gaussian copula for modelling (at least pairwise) dependencies, we consider the test based on the statistic $S^{n}$ given in equation (2) of [21], where we test the null hypothesis that the copula between a pair of dysphonia measures is Gaussian, and compute the $p$-value based on 1000 bootstrap samples. In Fig. 10, a boxplot of $p$-values of pairwise (that is between all $91 \cdot 90 / 2=4095$ pairs of variables) goodness-of-fit tests is shown. Based on the boxplot, we see that is it reasonable to assume (at least pairwise) Gaussian dependencies.

We still have quite a large amount of attributes compared to the sample size of $n=126$, and we still see some quite large correlations between several first and last dysphonia measures (right upper corner of left panel in Fig. S5), so further feature selection is desired. With this objective in mind, we decide to cluster the remaining 91 attributes in order to get an idea about how they can be divided into properly separated groups that have rather strong similarity within.



Fig. 11: Dendrogram (left) and redundancy (right) for the clustering of 91 dysphonia measures.
In particular, we opt for agglomerative hierarchical variable clustering based on similarity measures (see, e.g., [19] and references within for a survey), where the main task is to measure the similarity, say $D\left(X_{1}, X_{2}\right)$ (or alternatively dissimilarity), between two groups of variables $X_{1}$ and $X_{2}$. Denote $X_{1}, \ldots, X_{91}$ for the 91 dysphonia measures, which are initially considered to be clusters on their own. In the first step, the two variables $X_{i}$ and $X_{j}$ (for certain $i, j \in$ $\{1, \ldots, 91\}$ with $i \neq j)$ that exhibit the largest similarity according to $D\left(\left\{X_{i}\right\},\left\{X_{j}\right\}\right)$, i.e., taking $X_{1}=\left\{X_{i}\right\}$ and $X_{2}=\left\{X_{j}\right\}$, are merged together forming one single cluster. Next, all similarities between the current clusters are again computed, and the two clusters showing the largest similarity are merged. One keeps repeating this until only one big cluster (composed of all the 91 attributes) remains, yielding a total of 91 partitions of the attribute space. In general, the main task is thus to compute (for $X_{1}=\left\{X_{i_{1}}, \ldots, X_{i_{m}}\right\}$ and $X_{2}=\left\{X_{j_{1}}, \ldots, X_{j_{r}}\right\}$ )

$$
D\left(X_{1}, X_{2}\right)=D\left(\left\{X_{i_{1}}, \ldots, X_{i_{m}}\right\},\left\{X_{j_{1}}, \ldots, X_{j_{r}}\right\}\right)
$$




---

for certain mutually exclusive $i_{1}, \ldots, i_{m}, j_{1}, \ldots, j_{r} \in\{1, \ldots, 91\}$. Typically, one specifies a certain (estimated) bivariate dependence coefficient and a certain link function (overlooking multivariate dependence structures) for computing (33), or (estimated) multivariate concordance measures (between univariate random variables) have also been studied (see, e.g., [19]). We decide to take $\widehat{D}_{1}\left(\left(X_{i_{1}}, \ldots, X_{i_{m}}\right),\left(X_{j_{1}}, \ldots, X_{j_{r}}\right)\right)$ for (33), and as such measure the similarity between clusters (in spite of possible similarity within), which feels more natural and does not require a link function. This $\widehat{D}_{1}$ is taken to be $D_{1}(\widehat{\mathcal{R}} \mathcal{R}, n)$, where $\widehat{\mathcal{R}} \mathcal{R}, n$ is the ridge penalized estimated Gaussian copula correlation matrix (23), keeping in mind that the total dimension $m+r$ in (33) might be large compared to $n$. The tuning parameter $\omega_{n}$ is again determined by a 5-fold cross-validation search on a grid of 50 equidistant elements in $[0.01,0.999]$.

We obtain 91 partitions, and one of these should be picked as preferable clustering of the attributes. Since not restricted to two groups, we can also use $\widehat{D}_{1}$ for measuring the similarity $D\left(\boldsymbol{X}_{1}, \ldots, \boldsymbol{X}_{k}\right)$ between $k$ clusters $\boldsymbol{X}_{1}, \ldots, \boldsymbol{X}_{k}$ comprising a specific partition. This in fact measures how separated the obtained clusters of that particular partition are, i.e., it is a measure of redundancy among the clusters of attributes, which we want to be rather small. The dendrogram of the clustering procedure and redundancy $D\left(\boldsymbol{X}_{1}, \ldots, \boldsymbol{X}_{k}\right)$ as a function of the number of clusters $k$ (for each of the 91 obtained partitions) are shown in Fig. 11. Based on this, we decide to look deeper into the 36 cluster partition (where the dotted line cuts the dendrogram), since the redundancy is minimal here (in particular, $\left.D\left(\boldsymbol{X}_{1}, \ldots, \boldsymbol{X}_{36}\right)=0.07265\right)$. Next, we rearrange the attributes such that dysphonia measures that belong to the same cluster follow each other in the dataset, and the cluster dimensions are

$$
\left(d_{1}, \ldots, d_{36}\right)=(1,1,53,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,1,1,1,1)
$$

i.e., there is a big cluster of size 53 , two smaller clusters of size 2 and 3 , and 33 clusters of size 1 . The sample normal scores rank correlation matrix after rearrangement, estimated without a penalty and with a ridge penalty are respectively given in the middle and right panel of Fig. S5 in the Supplementary Material.

Denote now the 36 clusters as random vectors $\boldsymbol{X}_{1}, \ldots, \boldsymbol{X}_{36}$. We already know that $\widehat{D}_{1}\left(\boldsymbol{X}_{1}, \ldots, \boldsymbol{X}_{36}\right)=0.07265$ when using ridge penalization $\left(\omega_{n}=0.696\right)$, which is already way closer to 0 than when using no penalization (then $\left.\widehat{D}_{1}\left(\boldsymbol{X}_{1}, \ldots, \boldsymbol{X}_{36}\right)=0.19013\right)$. Moreover, the rationale behind variable clustering is that clusters are truly separated, i.e., there is (block) sparsity in the Gaussian copula correlation matrix at levels corresponding to attributes belonging to different clusters. Therefore, we also consider lasso, adaptive lasso, and group lasso estimation of the Gaussian



Fig. 12: Sparsity patterns of estimated Gaussian copula correlation matrix of 91 dysphonia measures using different penalties.
copula correlation matrix. For the lasso and group lasso, we search for an optimal $\omega_{n}$ on an equidistant grid of 50 values in $[0.01 ; 0.8]$, and for the adaptive lasso, we search for an optimal $\rho_{n}$ on an equidistant grid of 50 values in $[0.01 ; 0.6]$, each time aiming to maximize the BIC (31).

The first panel in Fig. 12 shows the sparse structure of the estimated normal scores rank correlation matrix of the 91 clustered attributes when using the lasso. To a certain extent, we recognize the diagonal blocks corresponding to the within cluster correlations, and observe many zeroes between attributes belonging to different clusters. The estimated inter-cluster dependence equals $\widehat{D}_{1}\left(\boldsymbol{X}_{1}, \ldots, \boldsymbol{X}_{36}\right)=0.0014$. Using the adaptive lasso (second panel), we get $\widehat{D}_{1}\left(\boldsymbol{X}_{1}, \ldots, \boldsymbol{X}_{36}\right)=0.0141$, and a group lasso estimator (third panel) results in $\widehat{D}_{1}\left(\boldsymbol{X}_{1}, \ldots, \boldsymbol{X}_{36}\right)=0.0130$. Note that the group lasso estimator did not shrink any of the diagonal blocks, reflecting the stronger intra-cluster similarities.




---

In the fourth panel of Fig. 12, we visualize a group lasso estimate with a larger penalty parameter (not determined through BIC). When forcing more sparsity by increasing $\omega_{n}$, we see more off-diagonal blocks (and not diagonal blocks) getting shrunk, and this leads to $\widehat{D}_{1}\left(\mathbf{X}_{1}, \ldots, \mathbf{X}_{36}\right)=0.0001$. More detailed images are given in Fig. S6 of the Supplementary Material.

Further feature selection can now be done via replacing each cluster by a single (or maybe multiple) attribute that represents the cluster well (e.g., the attribute within the cluster that has largest similarity with the cluster).

# 7. Discussion 

In this paper, we proposed to use the 2-Wasserstein distance between the joint copula measure and the product of the marginal copula measures for quantifying dependence between a finite, arbitrary amount of random vectors. The obtained dependence coefficients satisfy several desirable properties and especially have the powerful theoretical quality of detecting any departure from independence. Examples illustrate that the choice of normalization strongly influences the overall dependence quantification. Whether or not one can explicitly calculate the infimum for the optimal transport map and/or the supremum required for the normalization, depends on the specific form of the copula, and a great deal of interesting work remains to be done (also when no explicit copula can be assumed, i.e., when nonparametric estimators need to be considered).

A Gaussian copula approach yields explicit formulas with a clear interpretation. Using the sample matrix of normal scores rank correlation coefficients results in an easily computable plug-in estimator for which we obtained an asymptotic normality result with explicit asymptotic variance in arbitrary dimensions. Expectedly, higher dimensions aggravate the finite sample estimation performance. To cope with this, we studied rank-invariant penalization techniques for estimating the Gaussian copula correlation matrix, leading to estimators that are able to improve accuracy on the one hand, and enhance interpretability by detecting marginal independencies on the other hand. Such estimation challenges have enjoyed rather little attention, and further research would definitely be worthwhile.

Another interesting theoretical challenge is to study the optimal transport (and others as well) dependence coefficients when the dimension grows unboundedly. In the Gaussian copula context, random matrix theory could definitely be useful, and, as also touched upon in our simulations, various behaviours can be expected depending on the nature of the dependence measure, the normalisation, whether letting $d_{i} \rightarrow \infty$ for some $i$, or $k \rightarrow \infty$. Keeping the dimension fixed, our simulations illustrated the asymptotic normality result and the benefits of using penalization techniques when the sample size is rather small and/or when (group) sparsity is pursued.

Finally, in a first real data application, we illustrated the use of the dependence coefficients in evaluating and comparing (possibly more than two) consumer products or similarities in sensory analysis. Alongside, on a second real dataset containing expressions on sustained vowel phonations, we demonstrated how attributes can be hierarchically clustered via multivariate similarities between random vectors (despite similarities within), disposing of traditional link functions. Ridge penalization is preferred when the number of attributes is large compared to the sample size, and (group)-lasso type penalties can be used to reflect the homogeneity and separation of a partition of, in general $k$, groups of variables.

Acknowledgments. The authors thank Dr Gilles Mordant, Georg-August-Universität Göttingen, for scientific discussions during the startup phase of this research. The authors gratefully acknowledge support from the Research Fund KU Leuven [C16/20/002 project].




---

# Appendix A. Axioms for dependence measures between random vectors 

In [11], a list of axioms is stated for a dependence measure $D_{d_{1} \ldots,}, d_{k}(\boldsymbol{X})=D\left(\boldsymbol{X}_{1}, \ldots, \boldsymbol{X}_{k}\right)$. Up to some minor differences (small corrections and simplifications), the axioms are given as follows.
(A1) For every permutation $\{\pi(1), \ldots, \pi(k)\}$ of $\{1, \ldots, k\}: D_{d_{1}, \ldots, d_{k}}(\boldsymbol{X})=D\left(\boldsymbol{X}_{\pi(1)}, \ldots, \boldsymbol{X}_{\pi(k)}\right)$ : and for every permutation $\left\{\pi_{i}(1), \ldots, \pi_{i}\left(d_{i}\right)\right\}$ of $\left\{1, \ldots, d_{i}\right\}, i \in\{1, \ldots, k\}: D_{d_{1}, \ldots, d_{k}}(\boldsymbol{X})=D\left(\boldsymbol{X}_{1}, \ldots,\left(\boldsymbol{X}_{i \pi, 1(1)}, \ldots, \boldsymbol{X}_{i \pi_{i}\left(d_{i}\right)}\right), \ldots, \boldsymbol{X}_{k}\right)$ :
(A2) $0 \leq D_{d_{1}, \ldots, d_{k}}(\boldsymbol{X}) \leq 1$.
(A3) $D_{d_{1}, \ldots, d_{k}}(\boldsymbol{X})=0$ if and only if $\boldsymbol{X}_{1}, \ldots, \boldsymbol{X}_{k}$ are mutually independent.
(A4) $D\left(\boldsymbol{X}_{1}, \ldots, \boldsymbol{X}_{k}, \boldsymbol{X}_{k+1}\right) \geq D\left(\boldsymbol{X}_{1}, \ldots, \boldsymbol{X}_{k}\right)$ with equality if and only if $\boldsymbol{X}_{k+1}$ is independent of $\left(\boldsymbol{X}_{1}, \ldots, \boldsymbol{X}_{k}\right)$.
(A5) $D_{d_{1}, \ldots, d_{k}}(\boldsymbol{X})$ is well-defined for any $q$-dimensional random vector $\boldsymbol{X}$ (even if there is a singular part in the distribution of $\boldsymbol{X})$.
(A6) $D_{d_{1}, \ldots, d_{k}}(\boldsymbol{X})$ is a function of solely the copula $C$ of $\boldsymbol{X}$ (which is equivalent to $D_{d_{1}, \ldots, d_{k}}(\boldsymbol{X})$ being invariant under strictly increasing transformations of any of the components of $\boldsymbol{X}$ ).
(A7) Let $T_{i j}$ be a strictly decreasing, continuous transformation for a fixed $i \in\{1, \ldots, k\}$ and a fixed $j \in\left\{1, \ldots, d_{i}\right\}$. Then

$$
D\left(\boldsymbol{X}_{1}, \ldots, T_{i}\left(\boldsymbol{X}_{i}\right), \ldots, \boldsymbol{X}_{k}\right)=D\left(\boldsymbol{X}_{1}, \ldots, \boldsymbol{X}_{k}\right)
$$

where $T_{i}\left(\boldsymbol{X}_{i}\right)=\left(X_{i 1}, \ldots, T_{i j}\left(X_{i j}\right), \ldots, X_{i d_{i}}\right)$.
(A8) Let $\left(\boldsymbol{X}_{n}\right)_{n \in \mathbb{N}}$ be a sequence of $q$-dimensional random vectors with corresponding copulas $\left(C_{n}\right)_{n \in \mathbb{N}}$, then

$$
\lim _{n \rightarrow \infty} D_{d_{1}, \ldots, d_{k}}\left(\boldsymbol{X}_{n}\right)=D_{d_{1}, \ldots, d_{k}}(\boldsymbol{X})
$$

if $C_{n} \rightarrow C$ uniformly, where $C$ denotes the copula of $\boldsymbol{X}$.

## Appendix B. Proofs of theoretical results of Section 2

## ApPEndix B.1. Proof of Lemma 1

For (a), let $\boldsymbol{V}=\left(\boldsymbol{V}_{1}, \ldots, \boldsymbol{V}_{k}\right)$ with $\boldsymbol{V}_{i}=\left(V_{i 1}, \ldots, V_{i d_{i}}\right)$ be a random vector with distribution $\nu_{1} \times \cdots \times \nu_{k}$ and let $\boldsymbol{U}=\left(\boldsymbol{U}_{1}, \ldots, \boldsymbol{U}_{k}\right)$ with $\boldsymbol{U}_{i}=\left(U_{i 1}, \ldots, U_{i d_{i}}\right)$ be a random vector with distribution $\mu_{C}$, as marginal distribution of an arbitrary coupling $\gamma \in \Gamma\left(\mu_{C}, \nu_{1} \times \cdots \times \nu_{k}\right)$ of $(\boldsymbol{U}, \boldsymbol{V})$, and having marginals $\mu_{C_{1}}, \ldots, \mu_{C_{k}}$ itself. Then, the distribution of $\left(\boldsymbol{U}_{i}, \boldsymbol{V}_{i}\right)$ is a coupling of $\mu_{C_{i}}$ and $\nu_{i}$ for all $i=1, \ldots, k$ such that

$$
\mathbb{E}\left(\|\boldsymbol{U}-\boldsymbol{V}\|^{2}\right)=\mathbb{E}\left(\sum_{i=1}^{k} \sum_{j=1}^{d_{i}}\left(U_{i j}-V_{i j}\right)^{2}\right)=\sum_{i=1}^{k} \mathbb{E}\left(\left\|\boldsymbol{U}_{i}-\boldsymbol{V}_{i}\right\|^{2}\right) \geq \sum_{i=1}^{k} \mathcal{W}_{2}^{2}\left(\mu_{C_{i}}, \nu_{i}\right)
$$

Taking the infimum over all couplings $\gamma \in \Gamma\left(\mu_{C}, \nu_{1} \times \cdots \times \nu_{k}\right)$ yields the result. Part (b) follows immediately from the definition.

Regarding (c), if $\mu_{C_{i}}=\nu_{i}$ for all $i=1, \ldots, k$, we have $T_{d_{1}, \ldots, d_{k}}\left(\mu_{C} ; \nu_{1}, \ldots, \nu_{k}\right)=\mathcal{W}_{2}^{2}\left(\mu_{C}, \mu_{C_{1}} \times \cdots \times \mu_{C_{k}}\right)$, making the statement trivial since $\mathcal{W}_{2}$ defines a metric. Suppose now that $\nu_{i}$ is absolutely continuous for all $i=1, \ldots, k$ and $T_{d_{1}, \ldots, d_{k}}\left(\mu_{C} ; \nu_{1}, \ldots, \nu_{k}\right)=0$. The latter means that, working further on the proof of (a), there exists a $\gamma \in \Gamma\left(\mu_{C}, \nu_{1} \times\right.$ $\cdots \times \nu_{k}$ ) minimizing the left-hand side of (B.1), and with equality instead of inequality. Hence, the 2-Wasserstein distance between $\mu_{C_{i}}$ and $\nu_{i}$ is obtained at the coupling distribution of $\left(\boldsymbol{U}_{i}, \boldsymbol{V}_{i}\right)$ coming from $\gamma$, for all $i=1, \ldots, k$. However, Brenier's theorem (see, e.g., Theorem 2.12 in [48]) tells us that, since $\nu_{i}$ is absolutely continuous, this optimum is uniquely and deterministically attained, i.e., (denoting $\nabla$ for the gradient) there must exist convex functions $\psi_{i}: I^{d_{i}} \rightarrow \mathbb{R} \cup\{\infty\}$ such that $\boldsymbol{U}_{i}=\nabla \psi_{i}\left(\boldsymbol{V}_{i}\right)$ almost


---

Take an arbitrary $\widetilde{\pi} \in \Gamma\left(\mu_{C_{1}}, \ldots, \mu_{C_{k}}\right)$ such that $W_{2}(\pi, \widetilde{\pi})<\delta$, where we pick $\delta>0$ such that $\delta<\min \left\{1, \epsilon /\left(1+2 D_{\pi}\right)\right\}$ with $D_{\pi}=W_{2}\left(\pi ; \nu_{1} \times \cdots \times \nu_{k}\right)$. We also denote $D_{\widetilde{\pi}}=W_{2}\left(\widetilde{\pi} ; \nu_{1} \times \cdots \times \nu_{k}\right)$. It holds that

$$
\begin{aligned}
\left|T_{d_{1}, \ldots, d_{k}}\left(\pi ; \nu_{1}, \ldots, \nu_{k}\right)-T_{d_{1}, \ldots, d_{k}}\left(\widetilde{\pi} ; \nu_{1}, \ldots, \nu_{k}\right)\right| & =\left|D_{\pi}^{2}-D_{\widetilde{\pi}}^{2}\right|=\left|D_{\widetilde{\pi}}-D_{\pi}\right| \cdot\left|D_{\widetilde{\pi}}-D_{\pi}+2 D_{\pi}\right| \\
& \leq\left|D_{\widetilde{\pi}}-D_{\pi}\right|\left(\left|D_{\widetilde{\pi}}-D_{\pi}\right|+2 D_{\pi}\right) \\
& <\epsilon,
\end{aligned}
$$

where we used that $\left|D_{\widetilde{\pi}}-D_{\pi}\right| \leq W_{2}(\pi, \widetilde{\pi})$ because of the triangle inequality (recall that $W_{2}$ defines a metric). This finishes the proof of statement $(d)$.

# Appendix B.2. Proof of Proposition 1 

We start with proving (A4) for $T_{d_{1}, \ldots, d_{k}}$. Suppose we consider an additional random vector $\mathbf{X}_{k+1}$ having copula measure $\mu_{C_{k+1}}$, an additional absolutely continuous reference measure $\nu_{k+1}$, and let $\mu_{\widetilde{C}}$ be the copula measure of $\left(\mathbf{X}_{1}, \ldots, \mathbf{X}_{k+1}\right)$. If we first assume that $\mathbf{X}_{k+1}$ is independent of $\left(\mathbf{X}_{1}, \ldots, \mathbf{X}_{k}\right)$, we have $\mu_{\widetilde{C}}=\mu_{C} \times \mu_{C_{k+1}}$ and hence

$$
\begin{aligned}
T_{d_{1}, \ldots, d_{k+1}}\left(\mu_{\widetilde{C}} ; \nu_{1}, \ldots, \nu_{k+1}\right) & =W_{2}^{2}\left(\mu_{C} \times \mu_{C_{k+1}}, \nu_{1} \times \cdots \times \nu_{k+1}\right)-\sum_{i=1}^{k+1} W_{2}^{2}\left(\mu_{C_{i}}, \nu_{i}\right) \\
& =W_{2}^{2}\left(\mu_{C}, \nu_{1} \times \cdots \times \nu_{k}\right)+W_{2}^{2}\left(\mu_{C_{k+1}}, \nu_{k+1}\right)-\sum_{i=1}^{k+1} W_{2}^{2}\left(\mu_{C_{i}}, \nu_{i}\right) \\
& =W_{2}^{2}\left(\mu_{C}, \nu_{1} \times \cdots \times \nu_{k}\right)-\sum_{i=1}^{k} W_{2}^{2}\left(\mu_{C_{i}}, \nu_{i}\right) \\
& =T_{d_{1}, \ldots, d_{k}}\left(\mu_{C} ; \nu_{1}, \ldots, \nu_{k}\right)
\end{aligned}
$$

such that the Wasserstein dependence measure remains unchanged when adding $\mathbf{X}_{k+1}$ into consideration. In general, suppose that $\gamma \in \Gamma\left(\mu_{\widetilde{C}}, \nu_{1} \times \cdots \times \nu_{k+1}\right)$ is an optimal transport map from $\mu_{\widetilde{C}}$ to $\nu_{1} \times \cdots \times \nu_{k+1}$, as joint distribution of $(\widetilde{\mathbf{U}}, \widetilde{\mathbf{V}})$ with $\widetilde{\mathbf{U}}=\left(\mathbf{U}, \mathbf{U}_{k+1}\right)=\left(\mathbf{U}_{1}, \ldots, \mathbf{U}_{k+1}\right)$ and $\widetilde{\mathbf{V}}=\left(\mathbf{V}, \mathbf{V}_{k+1}\right)=\left(\mathbf{V}_{1}, \ldots, \mathbf{V}_{k+1}\right)$, i.e.,

$$
\begin{aligned}
T_{d_{1}, \ldots, d_{k+1}}\left(\mu_{\widetilde{C}} ; \nu_{1}, \ldots, \nu_{k+1}\right) & =\mathbb{E}\left(\|\widetilde{\mathbf{U}}-\widetilde{\mathbf{V}}\|^{2}\right)-\sum_{i=1}^{k+1} W_{2}^{2}\left(\mu_{C_{i}}, \nu_{i}\right) \\
& =\mathbb{E}\left(\|\mathbf{U}-\mathbf{V}\|^{2}\right)+\mathbb{E}\left(\left\|\mathbf{U}_{k+1}-\mathbf{V}_{k+1}\right\|^{2}\right)-\sum_{i=1}^{k+1} W_{2}^{2}\left(\mu_{C_{i}}, \nu_{i}\right) \\
& \geq W_{2}^{2}\left(\mu_{C}, \nu_{1} \times \cdots \times \nu_{k}\right)-\sum_{i=1}^{k} W_{2}^{2}\left(\mu_{C_{i}}, \nu_{i}\right) \\
& =T_{d_{1}, \ldots, d_{k}}\left(\mu_{C} ; \nu_{1}, \ldots, \nu_{k}\right)
\end{aligned}
$$

where the inequality follows from the definition of the Wasserstein distance. If this inequality is an equality, it must hold that

$$
W_{2}^{2}\left(\mu_{C}, \nu_{1} \times \cdots \times \nu_{k}\right)=\mathbb{E}\left(\|\mathbf{U}-\mathbf{V}\|^{2}\right)+\mathbb{E}\left(\left\|\mathbf{U}_{k+1}-\mathbf{V}_{k+1}\right\|^{2}\right)-W_{2}^{2}\left(\mu_{C_{k+1}}, \nu_{k+1}\right) \geq \mathbb{E}\left(\|\mathbf{U}-\mathbf{V}\|^{2}\right)
$$

from which

$$
\mathbb{E}\left(\|\mathbf{U}-\mathbf{V}\|^{2}\right)=W_{2}^{2}\left(\mu_{C}, \nu_{1} \times \cdots \times \nu_{k}\right) \text { and } \mathbb{E}\left(\left\|\mathbf{U}_{k+1}-\mathbf{V}_{k+1}\right\|^{2}\right)=W_{2}^{2}\left(\mu_{C_{k+1}}, \nu_{k+1}\right)
$$

Because of the absolute continuity of the $\nu_{i}$, the latter implies (using Brenier's theorem) that there exists $T_{k+1}: I^{d_{k+1}} \rightarrow$ $\mathbb{R}^{d_{k+1}}$ such that $\mathbf{U}_{k+1}=T_{k+1}\left(\mathbf{V}_{k+1}\right)$ almost surely, while the former means that there exist $T_{i}: I^{q} \


---

In the context of property (A7), assume without loss of generality that $X_{11}$ gets transformed to $T_{11}\left(X_{11}\right)$ for a strictly decreasing transformation $T_{11}$ and let $\mu_{\widetilde{C}}$ be the copula distribution of $\left(T_{1}\left(X_{1}\right), X_{2}, \ldots, X_{k}\right)$ with $T_{1}\left(X_{1}\right)=$ $\left(T_{11}\left(X_{11}\right), X_{12}, \ldots, X_{1 d_{1}}\right)$. Then, $\tilde{C}\left(u_{1}, \ldots, u_{k}\right)=C\left(\boldsymbol{u}_{1}, u_{2}, \ldots, u_{k}\right)-C\left(\widetilde{u}_{1}, u_{2}, \ldots, u_{k}\right)$ with $\boldsymbol{u}_{1}=\left(1, u_{12}, \ldots, u_{1 d_{1}}\right)$ and $\widetilde{u}_{1}=\left(1-u_{11}, u_{12}, \ldots, u_{1 d_{1}}\right)$. Suppose now that $\gamma \in \Gamma\left(\mu_{C}, \nu_{1} \times \cdots \times \nu_{k}\right)$ is an optimal transport map from $\mu_{C}$ to $\nu_{1} \times \cdots \times \nu_{k}$, as joint distribution of $(U, V)$, i.e.,

$$
W_{2}^{2}\left(\mu_{C}, \nu_{1} \times \cdots \times \nu_{k}\right)=\mathbb{E}\left(\|U-V\|^{2}\right)=\int_{I^{2 q}}\|u-v\|^{2} d \gamma(u, v)
$$

Consider then $\widetilde{\gamma}(u, v)=\gamma\left(u_{1}, u_{2}, \ldots, u_{k}, v\right)-\gamma\left(\widetilde{u}_{1}, u_{2}, \ldots, u_{k}, v\right)$, which clearly is a coupling of $\mu_{\widetilde{C}}$ and $\nu_{1} \times \cdots \times \nu_{k}$, as joint distribution of $(\widetilde{U}, V)$ with $\widetilde{U}=\left(\widetilde{U}_{1}, U_{2}, \ldots, U_{k}\right)$ and $\widetilde{U}_{1}=\left(1-U_{11}, U_{12}, \ldots, U_{1 d_{1}}\right)$. Moreover, putting $\widetilde{u}=\left(\widetilde{u}_{1}, u_{2}, \ldots, u_{2}\right)$, we have
$W_{2}^{2}\left(\mu_{\widetilde{C}}, \nu_{1} \times \cdots \times \nu_{k}\right) \leq \mathbb{E}\left(\|\widetilde{U}-V\|^{2}\right)=\int_{I^{2 q}}\|\widetilde{u}-\|\|^{2} d \widetilde{\gamma}(u, v)=\int_{I^{2 q}}\|u-v\|^{2} d \gamma(u, v)=W_{2}^{2}\left(\mu_{C}, \nu_{1} \times \cdots \times \nu_{k}\right)$,
by simply doing a substitution $t_{11}=1-u_{11}$. Following a reversed reasoning, we also obtain $W_{2}^{2}\left(\mu_{C}, \nu_{1} \times \cdots \times\right.$ $\left.\nu_{k}\right) \leq W_{2}^{2}\left(\mu_{\widetilde{C}}, \nu_{1} \times \cdots \times \nu_{k}\right)$ and hence $W_{2}^{2}\left(\mu_{C}, \nu_{1} \times \cdots \times \nu_{k}\right)=W_{2}^{2}\left(\mu_{\widetilde{C}}, \nu_{1} \times \cdots \times \nu_{k}\right)$. Similarly, we can show that $W_{2}^{2}\left(\mu_{C_{1}}, \nu_{1}\right)=W_{2}^{2}\left(\mu_{\widetilde{C}_{1}}, \nu_{1}\right)$ where $\mu_{\widetilde{C}_{1}}$ is the copula distribution of $T_{1}\left(X_{1}\right)$ and hence conclude (A7).

Finally, for (A8), we want that if $C_{n} \rightarrow C$ uniformly for $n \rightarrow \infty$, it is true that

$$
\left|T_{d_{1}, \ldots, d_{k}}\left(\mu_{C_{n}} ; \nu_{1}, \ldots, \nu_{k}\right)-T_{d_{1}, \ldots, d_{k}}\left(\mu_{C} ; \nu_{1}, \ldots, \nu_{k}\right)\right| \rightarrow 0
$$

as $n \rightarrow \infty$. Note that if $C_{n} \rightarrow C$ uniformly, we also have $\int_{I^{q}}\|u\|^{p} d C_{n}(u) \rightarrow \int_{I^{q}}\|u\|^{p} d C(u)$ as $n \rightarrow \infty$ for every $p>0$ (Helly-Bray theorem). Since convergence in distribution together with convergence of the first two moments implies $W_{2}$-convergence, equation (B.2) is proven by using similar arguments as for (d) of Lemma 1.

# Appendix C. Proofs of theoretical results of Section 3 

## Appendix C.1. Proof of Proposition 2

The first step of the proof consists of showing that the eigenvalues of $R_{\mathrm{m}}$ are indeed given by (8). Therefore, already note that because of the orthogonality of the matrix

$$
U=\left(\begin{array}{lcccc}
U_{11} & 0_{12} & \cdots & 0_{1 k} & \\
0_{12}^{T} & U_{22} & \cdots & 0_{2 k} & \\
\vdots & \vdots & \ddots & \vdots & \\
0_{1 k}^{T} & 0_{2 k}^{T} & \cdots & U_{k k} &
\end{array}\right)
$$

denoting $0_{i j} \in \mathbb{R}^{d_{i} \times d_{j}}$ for a matrix of zeroes, the eigenvalues of $R_{\mathrm{m}}$ are the same as those of

$$
\Lambda_{\mathrm{m}}=U^{T} R_{\mathrm{m}} U=\left(\begin{array}{cccc}
\Lambda_{11} & \Lambda_{11}^{1 / 2} \Pi_{12} \Lambda_{22}^{1 / 2} & \cdots & \Lambda_{11}^{1 / 2} \Pi_{1 k} \Lambda_{k k}^{1 / 2} \\
\Lambda_{22}^{1 / 2} \Pi_{12}^{T} \Lambda_{11}^{1 / 2} & \Lambda_{22} & \cdots & \Lambda_{22}^{1 / 2} \Pi_{2 k} \Lambda_{k k}^{1 / 2} \\
\vdots & \vdots & \ddots & \vdots \\
\Lambda_{k k}^{1 / 2} \Pi_{1 k}^{T} \Lambda_{11}^{1 / 2} & \Lambda_{k k}^{1 / 2} \Pi_{2 k}^{T} \Lambda_{22}^{1 / 2} & \cdots & \Lambda_{k k}
\end{array}\right)
$$

which we can find explicitly. Let $e_{r, \ell}$ be the $r$-th canonical unit (column) vector in $\mathbb{R}^{\ell}$ and put $d_{0}=0$. For ease of notation, we also write $\Pi_{r \ell}=\Pi_{\ell r}^{T}$ if $r>\ell$. We now list the eigenvalues and eigenvectors of the matrix $\Lambda_{\mathrm{m}}$.

- For all $i=0, \ldots, k-2$ and all $j=d_{i}+1, \ldots, d_{i+1}$, the vector

$$
\left(0_{


---

Indeed, when fixing a certain $i \in\{0, \ldots, k-2\}$ and $j \in\left\{d_{i}+1, \ldots, d_{i+1}\right\}$, the $r$-th block row of (C.1) for $r \in\{1, \ldots, i\}$, multiplied with (C.2) equals

$$
\Lambda_{r r} \mathbf{0}_{d_{r}}+\sum_{\ell=1}^{\ell, r} \Lambda_{r r}^{1 / 2} \Pi_{r \ell} \Lambda_{\ell \ell}^{1 / 2} \mathbf{0}_{d_{\ell}}+\sum_{\ell=i+1}^{k} \Lambda_{r r}^{1 / 2} \Pi_{r \ell} \Lambda_{\ell \ell}^{1 / 2} \lambda_{j, \ell \ell}^{1 / 2} \mathbf{e}_{j, d_{\ell}}=\sum_{\ell=i+1}^{k} \lambda_{j, \ell} \Lambda_{r r}^{1 / 2} \Pi_{r \ell} \mathbf{e}_{j, d_{\ell}}=\mathbf{0}_{d_{r}}
$$

since $\Pi_{r \ell} \mathbf{e}_{j, d_{\ell}}=\mathbf{0}_{d_{r}}$, as $j>d_{r}$. If for $r \in\{i+1, \ldots, k\}$, we multiply the $r$-th block row of (C.1) with (C.2), we obtain

$$
\begin{aligned}
\sum_{\ell=1}^{i} \Lambda_{r r}^{1 / 2} \Pi_{r \ell} \Lambda_{\ell \ell}^{1 / 2} \mathbf{0}_{d_{\ell}}+\Lambda_{r r} \lambda_{j, r r}^{1 / 2} \mathbf{e}_{j, d_{r}}+\sum_{\ell=i+1}^{k} \widehat{\Lambda}_{r r}^{1 / 2} \Pi_{r \ell} \widehat{\Lambda}_{\ell \ell}^{1 / 2} \lambda_{j, \ell \ell}^{1 / 2} \mathbf{e}_{j, d_{\ell}} & =\lambda_{j, r r}^{3 / 2} \mathbf{e}_{j, d_{r}}+\sum_{\ell=i+1}^{k} \widehat{\lambda}_{j, \ell \ell} \Lambda_{r r}^{1 / 2} \Pi_{r \ell} \mathbf{e}_{j, d_{\ell}} \\
& =\lambda_{j, r r}^{3 / 2} \mathbf{e}_{j, d_{r}}+\lambda_{j, r r}^{1 / 2} \sum_{\ell=i+1}^{k} \widehat{\lambda}_{j, \ell \ell} \mathbf{e}_{j, d_{r}} \\
& =\lambda_{j, r r}^{1 / 2}\left(\sum_{\ell=i+1}^{k} \lambda_{j, \ell \ell}\right) \mathbf{e}_{j, d_{r}}
\end{aligned}
$$

since $\Pi_{r l} \mathbf{e}_{j, d_{\ell}}=\mathbf{e}_{j, d_{r}}$, as $j \leq d_{r}$. Hence, for every $r \in\{1, \ldots, k\}$, the $r$-th block element $\left(\in \mathbb{R}^{d_{r} \times 1}\right)$ of the matrix multiplication of $\Lambda_{m}$ with the vector (C.2), is equal to (C.3) multiplied with the vector (C.2). This shows what was desired, and delivers $d_{1}+\left(d_{2}-d_{1}\right)+\cdots+\left(d_{k-1}-d_{k-2}\right)=d_{k-1}$ eigenvalues.

- For all $j=d_{k-1}+1, \ldots, d_{k}$, the vector

$$
\left(\mathbf{0}_{d_{1}}^{T}, \ldots, \mathbf{0}_{d_{k-1}}^{T}, \mathbf{e}_{j, d_{k}}^{T}\right)^{T}
$$

is an eigenvector with eigenvalue $\lambda_{j, k k}$.
Indeed, following the previous result, it is straightforward to see that for $r \in\{1, \ldots, k-1\}$, the multiplication of the $r$-th block row of $\Lambda_{m}$ with the vector (C.4) equals $\mathbf{0}_{d_{r}}$, as $j>d_{r}$, while the last block row leads to $\Lambda_{k k} \mathbf{e}_{j, d_{k}}=\lambda_{j, k k} e_{j, d_{k}}$. This gives an additional amount of $\left(d_{k}-d_{k-1}\right)$ eigenvalues, resulting in an intermediate total of $d_{k-1}+\left(d_{k}-d_{k-1}\right)=d_{k}$ eigenvalues.

- For all $i=1, \ldots, k-1$ and all $j=1, \ldots, d_{i}$, the vector

$$
\left(\mathbf{0}_{d_{1}}^{T}, \ldots, \mathbf{0}_{d_{i-1}}^{T}, \lambda_{j,(i+1)(i+1)}^{1 / 2} \mathbf{e}_{j, d_{i}}^{T},-\lambda_{j, i i}^{1 / 2} \mathbf{e}_{j, d_{i+1}}^{T}, \mathbf{0}_{d_{i+2}}^{T}, \ldots, \mathbf{0}_{d_{k}}^{T}\right)
$$

is an eigenvector with eigenvalue 0 .
Indeed, when fixing a certain $i \in\{1, \ldots, k-1\}$ and $j \in\left\{1, \ldots, d_{i}\right\}$, the $r$-th block row of (C.1) for $r \in\{1, \ldots, i-1\}$ multiplied with (C.5) equals

$$
\begin{aligned}
\Lambda_{r r} \mathbf{0}_{d_{r}}+\sum_{\ell=1}^{i-1} \widehat{\Lambda}_{r r}^{1 / 2} \Pi_{r \ell} \widehat{\Lambda}_{\ell \ell}^{1 / 2} \mathbf{0}_{d_{\ell}}+\widehat{\Lambda}_{r r}^{1 / 2} \Pi_{r i} \widehat{\Lambda}_{i i}^{1 / 2} \lambda_{j,(i+1)(i+1)}^{1 / 2} \mathbf{e}_{j, d_{i}} & -\widehat{\Lambda}_{r r}^{1 / 2} \Pi_{r(i+1)} \widehat{\Lambda}_{(i+1)(i+1)}^{1 / 2} \lambda_{j, i i}^{1 / 2} \mathbf{e}_{j, d_{i+1}}+\sum_{\ell=i+2}^{k} \widehat{\Lambda}_{r r}^{1 / 2} \Pi_{r l} \widehat{\Lambda}_{\ell \ell}^{1 / 2} \mathbf{0}_{d_{\ell}} \\
& =\lambda_{j,(i+1)(i+1)}^{1 / 2} \lambda_{j, i i}^{1 / 2} \Lambda_{r r}^{1 / 2} \Pi_{r i} \mathbf{e}_{j, d_{i}}-\lambda_{j, i i}^{1 / 2} \lambda_{j,(i+1)(i+1)}^{1 / 2} \Lambda_{r r}^{1 / 2} \Pi_{r(i+1)} \mathbf{e}_{j, d_{i+1}} \\
& =\mathbf{0}_{d_{r}}
\end{aligned}
$$

since $\Pi_{r i} \mathbf{e}_{j, d_{i}}=\Pi_{r(i+1)} \mathbf{e}_{j, d_{i+1}}$. For $r=i$, we get

$$
\begin{aligned}
\sum_{\ell=1}^{i-1} \widehat{\Lambda}_{r r}^{1 / 2} \


---

since $\Pi_{i(i+1)} e_{j, d_{i+1}}=e_{j, d_{i}}$, as $j \leq d_{i}$. For $r=i+1$, we get

$$
\begin{aligned}
& \sum_{\ell=1}^{i-1} \Lambda_{r r}^{1 / 2} \Pi_{r \ell} \Lambda_{\ell \ell}^{1 / 2} \mathbf{0}_{d_{\ell}}+\lambda_{j,(i+1)(i+1)}^{1 / 2} \Lambda_{(i+1)(i+1)}^{1 / 2} \Pi_{(i+1) i} \Lambda_{i i}^{1 / 2} e_{j, d_{i}}-\lambda_{j, i i}^{1 / 2} \Lambda_{(i+1)(i+1)} e_{j, d_{i+1}}+\sum_{\ell=i+2}^{k} \Lambda_{r r}^{1 / 2} \Pi_{r l} \Lambda_{\ell \ell}^{1 / 2} \mathbf{0}_{d_{\ell}} \\
& =\lambda_{j,(i+1)(i+1)}^{1 / 2} \lambda_{j, i i}^{1 / 2} \Lambda_{(i+1)(i+1)}^{1 / 2} e_{j, d_{i+1}}-\lambda_{j, i i}^{1 / 2} \lambda_{j,(i+1)(i+1)} e_{j, d_{i+1}} \\
& =\lambda_{j,(i+1)(i+1)}^{1 / 2} \lambda_{j, i i}^{1 / 2} \lambda_{j,(i+1)(i+1)}^{1 / 2} e_{j, d_{i+1}}-\lambda_{j, i i}^{1 / 2} \lambda_{j,(i+1)(i+1)} e_{j, d_{i+1}} \\
& =\mathbf{0}_{d_{i+1}}
\end{aligned}
$$

since $\Pi_{(i+1) i} e_{j, d_{i}}=e_{j, d_{i+1}}$, as $j \leq d_{i}$. Finally, for $r \in\{i+2, \ldots, k\}$, we obtain

$$
\begin{aligned}
& \sum_{\ell=1}^{i-1} \Lambda_{r r}^{1 / 2} \Pi_{r l} \Lambda_{\ell \ell}^{1 / 2} \mathbf{0}_{d_{\ell}}+\Lambda_{r r}^{1 / 2} \Pi_{r i} \Lambda_{i i}^{1 / 2} \lambda_{j,(i+1)(i+1)}^{1 / 2} e_{j, d_{i}}-\Lambda_{r r}^{1 / 2} \Pi_{r(i+1)} \Lambda_{(i+1)(i+1)}^{1 / 2} \lambda_{j, i i}^{1 / 2} e_{j, d_{i+1}}+\Lambda_{r r} \mathbf{0}_{d_{r}}+\sum_{\substack{\ell=i+2 \\
\ell \neq r}}^{k} \Lambda_{r r}^{1 / 2} \Pi_{r \ell} \Lambda_{\ell \ell}^{1 / 2} \mathbf{0}_{d_{\ell}} \\
& =\lambda_{j,(i+1)(i+1)}^{1 / 2} \lambda_{j, i i}^{1 / 2} \Lambda_{r r}^{1 / 2} \Pi_{r i} e_{j, d_{i}}-\lambda_{j, i i}^{1 / 2} \lambda_{j,(i+1)(i+1)}^{1 / 2} \Lambda_{r r}^{1 / 2} \Pi_{r(i+1)} e_{j, d_{i+1}} \\
& =\mathbf{0}_{d_{r}}
\end{aligned}
$$

since $\Pi_{r i} e_{j, d_{i}}=\Pi_{r(i+1)} e_{j, d_{i+1}}$, and we come by $d_{1}+\cdots+d_{k-1}$ eigenvalues, resulting in the desired total of $d_{1}+\cdots+d_{k}=q$ eigenvalues. These are indeed given by

$$
\lambda\left(R_{m}\right)=\left(\lambda_{j, 11}+\lambda_{j, 22}+\cdots+\lambda_{j, k k}\right)_{j=1}^{q}
$$

Next, we need to show that for an arbitrary $A \in \Gamma\left(R_{11}, \ldots, R_{k k}\right)$ with eigenvalues $\lambda_{1} \geq \lambda_{2} \geq \cdots \geq \lambda_{q}$, it holds that

$$
\sum_{\ell=1}^{n} \lambda_{\ell} \leq \sum_{\ell=1}^{w} d_{\ell}+\sum_{\ell=1}^{n}\left(\lambda_{\ell,(w+1)(w+1)}+\cdots+\lambda_{\ell, k k}\right) \text { for all } w=0, \ldots, k-1, n=d_{w}+1, \ldots, d_{w+1}
$$

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
\end{array}\right) \text { and } C_{i}=\left(\begin{array}{cc}
R_{i i} & Q_{i} \\
Q_{i}^{T} & B_{i}
\end{array}\right)
$$

where $Q_{i}=\left(Q_{i(i+1)} \cdots Q_{i k}\right) \in \mathbb{R}^{d_{i} \times\left(d_{i+1} \cdots+d_{k}\right)}$, for all $i=1, \ldots, k-2$. We will approach $C_{i}$ as a block matrix consisting of four blocks. Note that $B_{i} \in \mathbb{R}^{\left(d_{i+1}+\ldots+d_{k}\right) \times\left(d_{i+1}+\ldots+d_{k}\right)}$ and $C_{i} \in \mathbb{R}^{\left(d_{i}+\ldots+d_{k}\right) \times\left(d_{i}+\ldots+d_{k}\right)}$. Further, put
$\gamma_{1, i} \geq \gamma_{2, i} \geq \cdots \geq \gamma_{m_{i}, i} \quad$ the eigenvalues of $C_{i}$ for $i=1, \ldots, k-2, m_{i}=d_{i}+\cdots+d_{k}$
$\lambda_{1, i i} \geq \lambda_{2, i i} \geq \cdots \geq \lambda_{d_{i}, i i} \quad$ the eigenvalues of $R_{i i}$ for $i=1, \ldots, k$
$\mu_{1, i} \geq \mu_{2, i} \geq \cdots \geq \mu_{t_{i


---

and integers

$$
\begin{aligned}
& 1 \leq r_{1, i}<\cdots<r_{\alpha_{i}, i} \leq d_{i}, \quad r_{\ell, i}=d_{i}-\alpha_{i}+\ell \text { for } \ell>\alpha_{i}, \quad \text { for } i=1, \ldots, k \\
& 1 \leq j_{1, i}<\cdots<j_{\beta_{i}, i} \leq t_{i}, \quad j_{\ell, i}=t_{i}-\beta_{i}+\ell \text { for } \ell>\beta_{i}, \quad \text { for } i=1, \ldots, k-2
\end{aligned}
$$

that, defined as such, will guarantee that

$$
\begin{array}{r}
\sum_{\ell=1}^{\alpha_{i}+\beta_{i}} \gamma_{r_{\ell, i}+j_{\ell, i}-\ell, i} \leq \sum_{\ell=1}^{\alpha_{i}} \lambda_{r_{\ell, i}, i i}+\sum_{\ell=1}^{\beta_{i}} \mu_{j_{\ell, i}, i} \text { for } i=1, \ldots, k-2 \\
\sum_{\ell=1}^{\alpha_{k-1}+\alpha_{k}} \mu_{r_{\ell, k-1}+r_{\ell, k}-\ell, k-2} \leq \sum_{\ell=1}^{\alpha_{k-1}} \lambda_{r_{\ell, k-1},(k-1)(k-1)}+\sum_{\ell=1}^{\alpha_{k}} \lambda_{r_{\ell, k}, k k}
\end{array}
$$

Notice that (C.7) describes a total of $k-1$ inequalities. We will now prove (C.6) by making an adequate choice for the $\alpha_{i}, \beta_{i}$ and corresponding indices $r_{\ell, i}, j_{\ell, i}$. In particular, when considering a fixed $w \in\{0, \ldots, k-1\}$ and fixed $n \in\left\{d_{w}+1, \ldots, d_{w+1}\right\}$, take

$$
\begin{aligned}
& \alpha_{i}=d_{i}, r_{\ell, i}=\ell \text { for } \ell=1, \ldots, d_{i}, i=1, \ldots, w \\
& \alpha_{i}=n, r_{\ell, i}=\ell \text { for } \ell=1, \ldots, n, i=w+1, \ldots, k \\
& \beta_{i}=t_{i}-t_{w}+(k-w) n, j_{\ell, i}= \begin{cases}\ell & \text { if } \ell \in\{1, \ldots, n\} \\
t_{w}-(k-w) n+\ell, & \text { if } \ell \in\left\{n+1, \ldots, \beta_{i}\right\}\end{cases}
\end{aligned}
$$

for $i=1, \ldots, \min \{k-2, w\}$

$$
\beta_{i}=(k-i) n, j_{\ell, i}= \begin{cases}\ell & \text { if } \ell \in\{1, \ldots, n\} \\ t_{i}-(k-i) n+\ell, & \text { if } \ell \in\left\{n+1, \ldots, \beta_{i}\right\}\end{cases}
$$

for $i=w+1, \ldots, k-2$.
Then, concerning the $k-2^{\prime}$ th and $k-1^{\prime}$ th inequality of (C.7), we see that if $w=k-1$, we have

$$
\begin{aligned}
\sum_{\ell=1}^{\beta_{k-2}} \mu_{j_{\ell, k-2}, k-2} & =\sum_{\ell=1}^{n} \mu_{\ell, k-2}+\sum_{\ell=n+1}^{\beta_{k-2}} \mu_{d_{k}-n+\ell, k-2} \\
& =\mu_{1, k-2}+\cdots+\mu_{n, k-2}+\mu_{d_{k}+1, k-2}+\cdots+\mu_{t_{k-2}, k-2}
\end{aligned}
$$

and,

$$
\begin{aligned}
& \sum_{\ell=1}^{\alpha_{k-1}+\alpha_{k}} \mu_{r_{\ell, k-1}+r_{\ell, k}-\ell, k-2}=\sum_{\ell=1}^{d_{k-1}+n} \mu_{r_{\ell, k-1}+r_{\ell, k}-\ell, k-2} \\
& =\sum_{\ell=1}^{d_{k-1}} \mu_{\ell, k-2}+\sum_{\ell=d_{k-1}+1}^{n} \mu_{\ell, k-2}+\sum_{\ell=n+1}^{n+d_{k-1}} \mu_{d_{k}-n+\ell, k-2} \\
& =\mu_{1, k-2}+\cdots+\mu_{n, k-2}+\mu_{d_{k}+1, k-2}+\cdots+\mu_{d_{k-1}+d_{k}, k-2}
\end{aligned}
$$

Since $t_{k-2}=d_{k-1}+d_{k}$, we see that (C.8) and (C.9) are equal. If on the other hand $w \in\{0, \ldots, k-2\}$, we get

$$
\begin{aligned}
\sum_{\ell=1}^{\beta_{k-2}} \mu_{j_{\ell, k-2}, k-2} & =\sum_{\ell=1}^{n} \mu_{\ell, k-2}+\sum_{\ell=n+1}^{\beta_{k-2}} \mu_{t_{k-2}-2 n+\ell, k-2} \\
& =\mu_{1, k-2}+\cdots+\mu_{n, k-2}+\mu_{t_{k-2}-n+1, k-2}+\cdots+\mu_{t_{k-2}, k-2}
\end{aligned}
$$

and,

$$
\begin{aligned}
& \sum_{\ell=1}^{\alpha_{k-1}+\alpha_{k}} \mu_{r_{\ell, k-1}+r_{\ell, k}-\ell, k-2}=\sum_{\ell=1}^{2 n} \mu_{r_{\ell, k-1}+r_{\ell, k}-\ell, k-2} \\
& =\sum_{\ell=1}^{n} \mu_{\ell, k-2}+\sum_{\ell=n+1}^{2 n} \mu_{d_{k-1}+d_{k}-2 n+\ell, k-2} \\
& =\mu_{1, k-2}+\cdots+\mu_{n, k-2}+\mu_{d_{k-1}+d_{k}-n+1, k-2}+\cdots+\mu_{d_{k-1}+d_{k}, k-2}
\end{aligned}
$$




---

Again because $t_{k-2}=d_{k-1}+d_{k}$, we have equality between (C.10) and (C.11). We thus have shown so far that the second term on the right side of the $k-2^{\prime}$ ' th inequality of (C.7) equals the term on the left side of the $k-1^{\prime}$ ' th inequality. Now, concerning the $i^{\prime}$ ' th and $i+1^{\prime}$ ' th inequality for $i \in\{1, \ldots, k-3\}$, we must have either both $i, i+1 \in\{w+1, \ldots, k-2\}$ or both $i, i+1 \in\{1, \ldots, w\}$, or $i \in\{1, \ldots, w\}, i+1 \in\{w+1, \ldots, k-2\}$ meaning $i=w$. In the first case, it holds that

$$
\begin{aligned}
\sum_{\ell=1}^{\alpha_{i+1}+\beta_{i+1}} \gamma_{r_{\ell, i+1}+\mathbf{j}_{\ell, i+1}-\ell, i+1} & =\sum_{\ell=1}^{n+\beta_{i+1}} \gamma_{r_{\ell, i+1}+\mathbf{j}_{\ell, i+1}-\ell, i+1} \\
& =\sum_{\ell=1}^{n} \gamma_{\ell, i+1}+\sum_{\ell=n+1}^{\beta_{i+1}} \gamma_{d_{i+1}-n+t_{i+1}-(k-i-1) n+\ell, i+1}+\sum_{\ell=\beta_{i+1}+1}^{n+\beta_{i+1}} \gamma_{d_{i+1}-n+t_{i+1}-(k-i-1) n+\ell, i+1} \\
& =\gamma_{1, i+1}+\cdots+\gamma_{n, i+1}+\gamma_{d_{i+1}+t_{i+1}-(k-i-1) n+1, i+1}+\cdots+\gamma_{d_{i+1}+t_{i+1}, i+1}
\end{aligned}
$$

and

$$
\sum_{\ell=1}^{\beta_{i}} \mu_{\mathbf{j}_{\ell, i}, i}=\sum_{\ell=1}^{n} \mu_{\ell, i}+\sum_{\ell=n+1}^{\beta_{i}} \mu_{t_{i}-(k-i) n+\ell, i}=\mu_{1, i}+\cdots+\mu_{n, i}+\mu_{t_{i}-(k-i) n+n+1, i}+\cdots+\mu_{t_{i}, i}
$$

Since $t_{i}=d_{i+1}+t_{i+1}$ and $C_{i+1}=B_{i}$ (by construction, hence they also have the same eigenvalues), we see that (C.12) is equal to (C.13). For the second case, i.e., both $i, i+1 \in\{1, \ldots, w\}$, we have

$$
\begin{aligned}
\sum_{\ell=1}^{\alpha_{i+1}+\beta_{i+1}} \gamma_{r_{\ell, i+1}}+\mathbf{j}_{\ell, i+1}-\ell, i+1 & =\sum_{\ell=1}^{d_{i+1}+\beta_{i+1}} \gamma_{r_{\ell, i+1}+\mathbf{j}_{\ell, i+1}-\ell, i+1} \\
& =\sum_{\ell=1}^{d_{i+1}} \gamma_{\ell, i+1}+\sum_{\ell=d_{i+1}+1}^{n} \gamma_{\ell, i+1}+\sum_{\ell=n+1}^{\beta_{i+1}} \gamma_{t_{w}-(k-w) n+\ell, i+1}+\sum_{\ell=\beta_{i+1}}^{d_{i+1}+\beta_{i+1}} \gamma_{t_{w}-(k-w) n+\ell, i+1} \\
& =\gamma_{1, i+1}+\cdots+\gamma_{n, i+1}+\gamma_{t_{w}-(k-w-1) n+1, i+1}+\cdots+\gamma_{d_{i+1}+t_{i+1}, i+1}
\end{aligned}
$$

and

$$
\sum_{\ell=1}^{\beta_{i}} \mu_{\mathbf{j}_{\ell, i}, i}=\sum_{\ell=1}^{n} \mu_{\ell, i}+\sum_{\ell=n+1}^{\beta_{i}} \mu_{t_{w}-(k-w) n+\ell, i}=\mu_{1, i}+\cdots+\mu_{n, i}+\mu_{t_{w}-(k-w-1) n+1, i}+\cdots+\mu_{t_{i}, i}
$$

For the same reasons as in the previous case, we clearly see that (C.14) and (C.15) are the same expressions. Finally, if $i=w$,

$$
\begin{aligned}
\sum_{\ell=1}^{\alpha_{i+1}+\beta_{i+1}} \gamma_{r_{\ell, i+1}}+\mathbf{j}_{\ell, i+1}-\ell, i+1 & =\sum_{\ell=1}^{n+\beta_{w+1}} \gamma_{r_{\ell, w+1}+\mathbf{j}_{\ell, w+1}-\ell, w+1} \\
& =\gamma_{1, w+1}+\cdots+\gamma_{n, w+1}+\gamma_{d_{w+1}+t_{w+1}-(k-w-1) n+1, w+1}+\cdots+\gamma_{d_{w+1}+t_{w+1}, w+1}
\end{aligned}
$$

and,

$$
\sum_{\ell=1}^{\beta_{i}} \mu_{\mathbf{j}_{\ell, i}, i}=\sum_{\ell=1}^{\beta_{w}} \mu_{\mathbf{j}_{\ell, w}, w}=\mu_{1, w}+\cdots+\mu_{n, w}+\mu_{t_{w}-(k-w-1) n+1, w}+\cdots+\mu_{t_{w}, w}
$$

Since $t_{w}=d_{w+1}+t_{w+1}$ and $C_{w+1}=B_{w}$, we also have equality between (C.16) and (C.17). All together, we have proven that the second term on the right hand side of the $i$ ' th inequality of (C.7) is equal to the term on the left hand side of the $i+1^{\prime}$ ' th inequality for all $i=1, \ldots, k-2$. Hence (C.7) can be reduced to

$$
\sum_{\ell=1}^{\alpha_{1}+\beta_{1}} \gamma_{r_{\ell, 1}}+\mathbf{j}_{\ell, 1}-\ell, 1 \leq \sum_{\ell=1}^{w} \mathrm{~d}_{\ell}+\sum_{\ell=1}^{n}\left(\lambda_{\ell,(w+1)(w+1)}+\cdots+\lambda_{\ell, k k}\right)
$$




---

Moreover, since by choice $r_{\ell, 1}=\ell$ for all $\ell=1, \ldots, n$ if $w=0$, or $r_{\ell, 1}=\ell$ for all $\ell=1, \ldots, \bar{d}_{1}$ and $r_{\ell, 1}=\underline{d}_{1}-\bar{d}_{1}+\ell=\ell$ for all $\ell>\bar{d}_{1}$ if $w>0$, and $j_{\ell, 1}=\ell$ for all $\ell=1, \ldots, n$, we definitely have

$$
\sum_{\ell=1}^{n} \gamma_{\ell, 1} \leq \sum_{\ell=1}^{\alpha_{1}+\beta_{1}} \gamma_{r_{\ell, 1}+j_{\ell, 1}-\ell, 1}
$$

The inequality in (C.19) is an equality if there are $\alpha_{1}+\beta_{1}-n$ eigenvalues equal to zero. If for example $w=k-1$ and $n=\underline{d}_{k}$, this means that $\bar{d}_{1}+t_{1}-t_{k-1}+\bar{n}-\underline{n}=q-\underline{d}_{k}$ eigenvalues should be zero, which is the case for the matrix $R_{\mathrm{M}}$. Combining (C.18) with (C.19) and realizing that the eigenvalues $\gamma_{\ell, 1}$ are the same as the eigenvalues $\lambda_{\ell}$, since $A=C_{1}$, finishes the proof.

# Appendix C.2. Proof of Proposition 3 

Consider an arbitrary $A \in \Gamma\left(R_{11}, \ldots, R_{k k}\right)$ having ordered eigenvalues $\lambda_{1} \geq \cdots \geq \lambda_{q}$. Then, by definition of the Bures-Wasserstein distance (3),

$$
d_{\mathrm{W}}^{2}\left(A, I_{q}\right)=q+\operatorname{tr}(A)-2 \operatorname{tr}\left(A^{1 / 2}\right)=q+\sum_{j=1}^{q} \lambda_{j}-2 \sum_{j=1}^{q} \lambda_{j}^{1 / 2}
$$

Notice that the function $\lambda \mapsto \lambda-2 \lambda^{1 / 2}$ is convex for $\lambda \in[0, \infty)$. By Proposition 2, we know that the eigenvalues of $R_{\mathrm{M}}$ majorize those of $A$. From Lemma 2, it follows that (C.20) is maximal if $A=R_{\mathrm{M}}$. Secondly, we have

$$
R_{0}^{1 / 2} A R_{0}^{1 / 2}=\left(\begin{array}{cccc}
R_{11}^{2} & R_{11}^{1 / 2} \Psi_{12} R_{22}^{1 / 2} & \cdots & R_{11}^{1 / 2} \Psi_{1 k} R_{k k}^{1 / 2} \\
R_{22}^{1 / 2} \Psi_{12}^{\mathrm{T}} R_{11}^{1 / 2} & R_{22}^{2} & \cdots & R_{22}^{1 / 2} \Psi_{2 k} R_{k k}^{1 / 2} \\
\vdots & \vdots & \ddots & \vdots \\
R_{k k}^{1 / 2} \Psi_{1 k}^{\mathrm{T}} R_{11}^{1 / 2} & R_{k k}^{1 / 2} \Psi_{2 k}^{\mathrm{T}} R_{22}^{1 / 2} & \cdots & R_{k k}^{2}
\end{array}\right)
$$

Recall that $R_{i i}^{\alpha}=U_{i i} \Lambda_{i i}^{\alpha} U_{i i}^{\mathrm{T}}$ is the eigendecomposition of $R_{i i}^{\alpha}$ for $\alpha>0$, and for $R_{\mathrm{M}}$ we have $\Psi_{i j}=U_{i i} \Lambda_{i i}^{1 / 2} \Pi_{i j} \Lambda_{j j}^{1 / 2} U_{i j}^{\mathrm{T}}$. Hence, we get

$$
R_{i i}^{1 / 2} \Psi_{i j} R_{j j}^{1 / 2}=\left(U_{i i} \Lambda_{i i}^{1 / 2} U_{i i}^{\mathrm{T}}\right)\left(U_{i i} \Lambda_{i i}^{1 / 2} \Pi_{i j} \Lambda_{j j}^{1 / 2} U_{j j}^{\mathrm{T}}\right)\left(U_{j j} \Lambda_{j j}^{1 / 2} U_{j j}^{\mathrm{T}}\right)=U_{i i} \Lambda_{i i} \Pi_{i j} \Lambda_{j j} U_{j j}^{\mathrm{T}}
$$

which is of the same form as $\Psi_{i j}$, but with $\Lambda_{i i}^{1 / 2}$ and $\Lambda_{j j}^{1 / 2}$ replaced by $\Lambda_{i i}$ and $\Lambda_{j j}$. Applying Proposition 2 with $R_{i i}^{2}$ instead of $R_{i i}$ for $i=1, \ldots, k$, it follows that the eigenvalues of an arbitrary matrix in $\Gamma\left(R_{11}^{2}, \ldots, R_{k k}^{2}\right)$ are majorized by those of the matrix $R_{0}^{1 / 2} R_{\mathrm{M}} R_{0}^{1 / 2}$. Hence,

$$
d_{\mathrm{W}}^{2}\left(A, R_{0}\right)=2 \operatorname{tr}(A)-2 \operatorname{tr}\left\{\left(R_{0}^{1 / 2} A R_{0}^{1 / 2}\right)^{1 / 2}\right\}=2 \operatorname{tr}(A)-2 \sum_{j=1}^{q} \kappa_{j}^{1 / 2}
$$

with $\kappa_{1}, \ldots, \kappa_{q}$ the eigenvalues of $R_{0}^{1 / 2} A R_{0}^{1 / 2}$. The fact that (C.21) is maximal if $A=R_{\mathrm{M}}$ now follows from the convexity of the function $\kappa \mapsto-\kappa^{1 / 2}$ on $[0, \infty)$ and Lemma 2.

## Appendix C.3. Additional lemmas and proof of Theorem 1



as $t \rightarrow 0$,

$$
\lim _{t \searrow 0} \frac{\operatorname{tr}\left\{\left(R+t H_{t}\right)_{m}^{1 / 2}\right\}-\operatorname{tr}\left(R_{m}^{1 / 2}\right)}{t}=\frac{1}{2} \operatorname{tr}\left(\Upsilon_{1} H\right)
$$

with $\left(R+t H_{t}\right)_{m}$ the matrix in (7) for $R$ replaced by $R+t H_{t}$ and $\Upsilon_{1}$ defined in (16).




---

Proof. Define the map $\mathcal{L}:\left(\mathbb{S}^{q},\|\cdot\|_{F}\right) \rightarrow\left(\mathbb{S}^{q},\|\cdot\|_{F}\right): A \mapsto \mathcal{L}(A)$ via $\mathcal{L}(A)$ being the diagonal matrix whose diagonal is equal to the $q$ eigenvalues (counting multiplicities) of $A$ in decreasing order. Then, we have $\mathcal{L}\left(R_{i i}\right)=\Lambda_{i i}=$ $\operatorname{diag}\left(\lambda_{1, i i}, \ldots, \lambda_{d_{i}, i i}\right)$ for $i=1, \ldots, k$. Also define the map

$$
\mathcal{M}:\left(\mathbb{S}_{>}^{d_{1}} \times \cdots \times \mathbb{S}_{>}^{d_{k}},\|\cdot\|_{F}\right) \rightarrow\left(\mathbb{S}_{>}^{d_{1}} \times \cdots \times \mathbb{S}_{>}^{d_{k}},\|\cdot\|_{F}\right):\left(A_{1}, \ldots, A_{k}\right) \mapsto\left(\mathcal{L}\left(A_{1}\right), \ldots, \mathcal{L}\left(A_{k}\right)\right)
$$

where the Frobenius norm is naturally defined for a certain $\left(A_{1}, \ldots, A_{k}\right) \in \mathbb{S}^{d_{1}} \times \cdots \times \mathbb{S}^{d_{k}}$ through $\left\|\left(A_{1}, \ldots, A_{k}\right)\right\|_{F}=$ $\left(\left\|A_{1}\right\|_{F}^{2}+\cdots+\left\|A_{k}\right\|_{F}^{2}\right)^{1 / 2}$. Using Lemma 3 of [36], it is then quickly seen that the Fréchet derivative of $\mathcal{M}$ at $\left(R_{11}, \ldots, R_{k k}\right)$ in the direction of a certain $\mathrm{H}=\left(H_{11}, \ldots, H_{k k}\right) \in \mathbb{S}_{>}^{d_{1}} \times \cdots \times \mathbb{S}_{>}^{d_{k}}$ is $\Delta(\mathrm{H})=\left(D U_{11}^{T} H_{11} U_{11}, \ldots, D U_{k k}^{T} H_{k k} U_{k k}\right)$, with $D U_{i i}^{T} \mathrm{H}_{i i} U_{i i}$ the diagonal matrix containing the diagonal of $U_{i i}^{T} H_{i i} U_{i i}$. Consider now (recalling that $d_{1} \leq \cdots \leq d_{k}$ )

$$
g:\left(\mathbb{S}_{>}^{d_{1}} \times \cdots \times \mathbb{S}_{>}^{d_{k}},\|\cdot\|_{F}\right) \rightarrow(\mathbb{R},|\cdot|):\left(B_{1}, \ldots, B_{k}\right) \mapsto \sum_{j=1}^{d_{k}}\left(\eta_{j, 11}+\cdots+\eta_{j, k k}\right)^{1 / 2}
$$

with $\eta_{j, i i}$ the eigenvalues of $B_{i}$ in decreasing order for $i=1, \ldots, k$ and $j=1, \ldots, d_{i}$, and putting $\eta_{j, i i}=0$ for $j=d_{i}+$ $1, \ldots, d_{k}$. We see that $\operatorname{tr}\left(R_{\mathrm{m}}^{1 / 2}\right)=g\left(\mathcal{L}\left(R_{11}\right), \ldots, \mathcal{L}\left(R_{k k}\right)\right)=g\left(\Lambda_{11}, \ldots, \Lambda_{k k}\right)$, also putting $\lambda_{j, i i}=0$ for $j=d_{i}+1, \ldots, d_{k}$.
The Fréchet derivative of $g$ at $\left(\Lambda_{11}, \ldots, \Lambda_{k k}\right)$ in the direction of $\Delta(\mathrm{H})$ equals $\Psi(\Delta(\mathrm{H}))$, where $\Psi: \mathbb{S}_{>}^{d_{1}} \times \cdots \times \mathbb{S}_{>}^{d_{k}} \rightarrow \mathbb{R}$ satisfies

$$
\lim _{\|\Delta(\mathrm{H})\|_{F} \rightarrow 0} \frac{\left|g\left(\Lambda_{11}+D U_{11}^{T} H_{11} U_{11}, \ldots, \Lambda_{k k}+D U_{k k}^{T} H_{k k} U_{k k}\right)-g\left(\Lambda_{11}, \ldots, \Lambda_{k k}\right)-\Psi(\Delta(\mathrm{H}))\right|}{\|\Delta(\mathrm{H})\|_{F}}=0
$$

Defining $t_{j, i i}=\left(U_{i i}^{T} H_{i i} U_{i i}\right)_{j j}$ for all $i=1, \ldots, k$ and $j=1, \ldots, d_{i}$, as well as $t_{j, i i}=0$ for $j=d_{i}+1, \ldots, d_{k}$, it is obvious that the eigenvalues of $\Lambda_{i i}+D U_{i i}^{T} H_{i i} U_{i i}$ are $\lambda_{j, i i}+t_{j, i i}$. Moreover, since we assumed that the eigenvalues $\lambda_{j, i i}$ are distinct over $j$, it will hold, for $\|\Delta(\mathrm{H})\|_{F}$ small enough, that $\lambda_{j, i i}+t_{j, i i}$ are in decreasing order again over $j$. Hence, using our definition of $g$, we see that (C.22) becomes

$$
\lim _{\|\Delta(\mathrm{H})\|_{F} \rightarrow 0} \frac{\left|\sum_{j=1}^{d_{k}}\left\{\sum_{i=1}^{k}\left(\lambda_{j, i i}+t_{j, i i}\right)\right\}^{1 / 2}-\sum_{j=1}^{d_{k}}\left(\sum_{i=1}^{k} \lambda_{j, i i}\right)^{1 / 2}-\Psi(\Delta(\mathrm{H}))\right|}{\|\Delta(\mathrm{H})\|_{F}}=0
$$

From expression (C.23), we observe that $\Psi(\Delta(\mathrm{H}))$ is nothing more than the total derivative of the function

$$
f: \mathbb{R}^{k d_{k}} \rightarrow \mathbb{R}:\left(x_{1,11}, x_{1,22}, \ldots, x_{d_{k}, k k}\right) \mapsto \sum_{j=1}^{d_{k}}\left(\sum_{i=1}^{k} x_{j, i i}\right)^{1 / 2}
$$

at $\left(\lambda_{1,11}, \lambda_{1,22}, \ldots, \lambda_{d_{k}, k k}\right)$ evaluated in $\left(t_{1,11}, t_{1,22}, \ldots, t_{d_{k}, k k}\right)$. Computing the Jacobian matrix of $f$, we find

$$
\begin{aligned}
\Psi(\Delta(\mathrm{H})) & =\sum_{j=1}^{d_{k}}\left(\sum_{i=1}^{k} \frac{1}{2\left(\lambda_{j, 11}+\cdots+\lambda_{j, k k}\right)^{1 / 2}} t_{j, i i}\right) \\
& =\sum_{i=1}^{k}\left(\sum_{j=1}^{d_{i}} \frac{1}{2\left(\lambda_{j, 11}+\cdots+\lambda_{j, k k}\right)^{1 / 2}} t_{j, i i}\right) \\
& =\sum_{i=1}^{k}\left(\sum_{j=1}^{d_{i}} \frac{1}{2


---

where $H_{t, i i}$ is the $d_{i} \times d_{i}$ diagonal block of $H_{t}$. Using the notations (11), (12) and (13), we can further simplify the above expression into

$$
\frac{1}{2} \sum_{i=1}^{k} \operatorname{tr}\left(\Delta_{i} U_{i i}^{T} H_{i i} U_{i i}\right)=\frac{1}{2} \sum_{i=1}^{k} \operatorname{tr}\left(P_{i}^{T} U_{i i} \Delta_{i} U_{i i}^{T} P_{i} H\right)=\frac{1}{2} \operatorname{tr}\left(\Upsilon_{1} H\right)
$$

where we used that $\operatorname{tr}(\operatorname{Adiag}(B))=\operatorname{tr}(\operatorname{diag}(A) B)$ for square matrices $A, B$, the cyclic permutation property of the trace operator, the fact that $H_{i i}=P_{i} H P_{i}^{T}$ and finally the identity $\sum_{i=1}^{k} P_{i}^{T} A_{i} P_{i}=\operatorname{diag}\left(A_{1}, \ldots, A_{k}\right)$ for $\left(d_{i} \times d_{i}\right)$ matrices $A_{i}$.

Lemma 4. The Fréchet derivative of the map

$$
\eta: \mathcal{S}_{>}^{q} \rightarrow \mathbb{R}: R \mapsto \operatorname{tr}\left\{\left(R_{0}^{1 / 2} R R_{0}^{1 / 2}\right)^{1 / 2}\right\}
$$

is given by

$$
\lim _{t \rightarrow 0} \frac{\eta\left(R+t H_{t}\right)-\eta(R)}{t}=\frac{1}{2} \operatorname{tr}\left\{\left(J_{0}+J^{-1}\right) H\right\}
$$

for $H_{t}, H \in \mathcal{S}^{q}$ with $\left\|H_{t} \rightarrow H\right\|_{F} \rightarrow 0$ as $t \rightarrow 0$ and $J$ and $J_{0}$ as in (14) and (15) respectively.
Proof. From Lemma 5 in [36], the Fréchet derivative of the map

$$
\phi: \mathcal{S}_{>}^{q} \times \mathcal{S}_{>}^{q} \rightarrow \mathbb{R}:(A, B) \mapsto 2 \operatorname{tr}\left\{\left(A^{1 / 2} B A^{1 / 2}\right)^{1 / 2}\right\}
$$

at $(A, B) \in \mathcal{S}_{>}^{q} \times \mathcal{S}_{>}^{q}$ in the direction of $(G, H) \in \mathcal{S}^{q} \times \mathcal{S}^{q}$ equals $\operatorname{tr}(J G)+\operatorname{tr}\left(J^{-1} H\right)$ with

$$
\begin{aligned}
J & =A^{-1 / 2}\left(A^{1 / 2} B A^{1 / 2}\right)^{1 / 2} A^{-1 / 2}=B^{1 / 2}\left(B^{1 / 2} A B^{1 / 2}\right)^{-1 / 2} B^{1 / 2} \\
J^{-1} & =A^{1 / 2}\left(A^{1 / 2} B A^{1 / 2}\right)^{-1 / 2} A^{1 / 2}=B^{-1 / 2}\left(B^{1 / 2} A B^{1 / 2}\right)^{1 / 2} B^{-1 / 2}
\end{aligned}
$$

Applying this to $(A, B)=\left(R_{0}, R\right)$ and $(G, H)=\left(H_{0}, H\right)$ with $H_{0}$ having the same $d_{i} \times d_{i}$ diagonal blocks as $H$, but zero off-diagonal blocks, yields $\frac{1}{2}\left(\operatorname{tr}\left(J H_{0}\right)+\operatorname{tr}\left(J^{-1} H\right)\right)$ as the Fréchet derivative of $\eta$ at $R$ in the direction of $H$, with $J$ given in (14). The result follows from $\operatorname{tr}\left(J H_{0}\right)=\operatorname{tr}\left(J_{0} H\right)$, with $J_{0}$ given in (15).

Lemma 5. Under the conditions of Theorem 1, it holds that, for $H_{t} \in \mathcal{S}^{q}$ for $t>0$ and $H \in \mathcal{S}^{q}$ such that $\left\|H_{t}-H\right\|_{F} \rightarrow 0$ as $t \rightarrow 0$,
$\lim _{t \rightarrow 0} \frac{\operatorname{tr}\left[\left\{\left(R+t H_{t}\right)_{0}^{1 / 2}\left(R+t H_{t}\right)_{m}\left(R+t H_{t}\right)_{0}^{1 / 2}\right\}^{1 / 2}-\left(R_{0}^{1 / 2} R_{m} R_{0}^{1 / 2}\right)^{1 / 2}\right]}{t}=\operatorname{tr}\left(\Upsilon_{2} H\right)$,
with $\left(R+t H_{t}\right)_{0}$ having the same $d_{i} \times d_{i}$ diagonal blocks as $R+t H_{t}$ but zero off-diagonal blocks, $\left(R+t H_{t}\right)_{m}$ the matrix in (7) with $R$ replaced by $R+t H_{t}$, and with $\Upsilon_{2}$ defined in (17).

Proof. Recall the proof of Lemma 3. Keep the same definition for the map $\mathcal{M}$ and define

$$
g:\left(\mathcal{S}_{>}^{d_{1}} \times \cdots \times \mathcal{S}_{>}^{d_{k}},\|\cdot\|_{F}\right) \rightarrow(\mathbb{R},|\cdot|):\left(B_{1}, \ldots, B_{k}\right) \mapsto \sum_{j=1}^{d_{k}}\left(\eta_{j, 11}^{2}+\cdots+\eta_{j, k k}^{2}\right)^{1 / 2}
$$

with again $\eta_{j, i i}$ the eigenvalues of $B_{i}$ in decreasing order for $i=1, \ldots, k$ and $j=1, \ldots, d_{i}$, and putting $\eta_{j, i i}=0$ if $j=d_{i}+1, \ldots, d_{k}$. Again applying the chain rule yields, in a very similar way and using the same notations,

$$
\begin{aligned}
& \lim _{t \rightarrow 0} \frac{g\left(\mathcal{M}\left(R_{11}+t H_{t, 11}, \ldots, R_{k k}+t H_{t, k k}\right)\right)-g\left(\mathcal{M}\left(R_{11}, \ldots, R_{k k}\right)\right)}{t} \\
& =\sum_{i=1}^{k}\left(\sum_{j=1}^{d_{i}} \frac{\lambda_{j, i i}}{\left(\lambda_{j, 11}^{2}+\cdots+\lambda_{j, k k}^{2}\right)^{1 / 2}}\left(U_{i i}^{T} H_{i i} U_{i i}\right)_{j j}\right)=\sum_{i=1}^{k} \operatorname{tr}\left(\tilde{\Delta}_{i i} U_{i i}^{T} H_{i i} U_{i i}\right)=\operatorname{tr}\left(\Upsilon_{2} H\right)
\end{aligned}
$$




---

# Proof of Theorem 1 

We start by showing the Fréchet differentiability of $D_{1}$ and $D_{2}$. To this end, we prove that they are Hadamard differentiable on $\mathcal{S}_{>}^{q}$ with

$$
\lim _{\substack{t \rightarrow 0^{+} \\ H_{t} \rightarrow H}} \frac{D_{r}\left(R+t H_{t}\right)-D_{r}(R)}{t}=\operatorname{tr}\left(M_{r} H\right)
$$

for $r \in\{1,2\}$ and $H_{t} \in \mathcal{S}^{q}$ for $t>0$ and $H \in \mathcal{S}^{q}$ such that $\left\|H_{t}-H\right\|_{F} \rightarrow 0$ as $t \rightarrow 0$.

## Differentiability of $D_{1}$

Consider the function

$$
f:(0, \infty)^{k+2} \rightarrow \mathbb{R}:\left(x_{1}, \ldots, x_{k}, y, z\right) \mapsto \frac{\sum_{i=1}^{k} x_{i}-y}{\sum_{i=1}^{k} x_{i}-z} .
$$

It is then quickly seen that $D_{1}(R)=f\left(x_{1}, \ldots, x_{k}, y, z\right)$ and $D_{1}\left(R+t H_{t}\right)=f\left(x_{1}^{t}, \ldots, x_{k}^{t}, y^{t}, z^{t}\right)$ with

$$
\begin{array}{lll}
y=\operatorname{tr}\left(R^{1 / 2}\right), & x_{i}=\operatorname{tr}\left(R_{i i}^{1 / 2}\right), & z=\operatorname{tr}\left(R_{m}^{1 / 2}\right), \\
y^{t}=\operatorname{tr}\left\{\left(R+t H_{t}\right)^{1 / 2}\right\}, & x_{i}^{t}=\operatorname{tr}\left\{\left(R+t H_{t}\right)_{i i}^{1 / 2}\right\}, & z^{t}=\operatorname{tr}\left\{\left(R+t H_{t}\right)_{m}^{1 / 2}\right\},
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
\begin{aligned}
& \lim _{\substack{t \rightarrow 0^{+} \\
H_{t} \rightarrow H}} \frac{y^{t}-y}{t}=\frac{1}{2} \operatorname{tr}\left(R^{-1 / 2} H\right) \text { and } \\
& \lim _{\substack{t \rightarrow 0^{+} \\
H_{t} \rightarrow H}} \frac{x_{i}^{t}-x_{i}}{t}=\frac{1}{2} \operatorname{tr}\left(R_{i i}^{-1 / 2} H_{i i}\right)
\end{aligned}
$$

for $i=1, \ldots, k$, where we used the notation $H_{i i}$ for the $d_{i} \times d_{i}$ diagonal block of $H$. Also, Lemma 3 guarantees that

$$
\lim _{\substack{t \rightarrow 0^{+} \\ H_{t} \rightarrow H}} \frac{z^{t}-z}{t}=\frac{1}{2} \operatorname{tr}\left(\Upsilon_{1} H\right)
$$

Putting this together, we see that the Fréchet derivative of the map

$$
g: \mathcal{S}^{q} \rightarrow(0, \infty)^{k+2}: A \mapsto\left(\operatorname{tr}\left(A_{11}^{1 / 2}\right), \ldots, \operatorname{tr}\left(A_{k k}^{1 / 2}\right), \operatorname{tr}\left(A^{1 / 2}\right), \operatorname{tr}\left(A_{m}^{1 / 2}\right)\right)
$$

at $R$ in the direction of $H$ equals

$$
\left(\frac{1}{2} \operatorname{tr}\left(R_{11}^{-1 / 2} H_{11}\right), \ldots, \frac{1}{2} \operatorname{tr}\left(R_{k k}^{-1 / 2} H_{k k}\right), \frac{1}{2} \operatorname{tr}\left(R^{-1 / 2} H\right), \frac{1}{2} \operatorname{tr}\left(\Upsilon_{1} H\right)\right)
$$

which we will call $\Delta(H)$. Next, the Jacobian matrix of the function $f$ is given by

$$
J_{f}=\left(\begin{array}{llll}
\frac{\partial f}{\partial x_{1}} & \cdots & \frac{\partial f}{\partial x_{k}} & \frac{\partial f}{\partial y} \\
\frac{\partial f}{\partial z}
\end{array}\right)=\left(\begin{array}{llll}
\frac{y-z}{\left(x_{1}+\cdots+x_{k}-z\right)^{2}} & \cdots & \frac{y-z}{\left(x_{1}+\cdots+x_{k}-z\right)^{2}} & \frac{-1}{x_{1}+\cdots+x_{k}-z} \\
\frac{x_{1}+\cdots x_{k}-y}{\left(x_{1}+\cdots+x_{k}-z\right)^{2}}
\end{array}\right)
$$




---

such that the Fréchet derivative (being nothing more than a total derivative) of the function $f$ at $g(\mathbf{R})$ in the direction of $\Delta(\mathbf{H})$ is equal to

$$
\begin{aligned}
\left.\mathbf{J}_{f}\right|_{g(\mathbf{R})} \Delta(\mathbf{H})^{T} & =\sum_{\ell=1}^{k}\left[\frac{\operatorname{tr}\left(\mathbf{R}_{\mathrm{m}}^{1 / 2}\right)}{-\operatorname{tr}\left(\mathbf{R}^{1 / 2}\right)+\operatorname{tr}\left(\mathbf{R}^{1 / 2}\right)}-\frac{n_{i=1}^{k} \operatorname{tr}\left(\mathbf{R}_{i i}^{1 / 2}\right)-\operatorname{tr}\left(\mathbf{R}_{\mathrm{m}}^{1 / 2}\right)}{\left\{n_{i=1}^{k} \operatorname{tr}\left(\mathbf{R}_{i i}^{1 / 2}\right)-\operatorname{tr}\left(\mathbf{R}_{\mathrm{m}}^{1 / 2}\right)\right\}^{2}} \frac{1}{2} \operatorname{tr}\left(\mathbf{R}_{\ell \ell}^{-1 / 2} \mathbf{H}_{\ell \ell}\right)\right]- \\
\frac{1}{p_{i=1} \operatorname{tr}\left(\mathbf{R}_{i i}^{1 / 2}\right)-\operatorname{tr}\left(\mathbf{R}_{\mathrm{m}}^{1 / 2}\right)} & \frac{1}{2} \operatorname{tr}\left(\mathbf{R}^{-1 / 2} \mathbf{H}\right)+\frac{n_{i=1}^{k} \operatorname{tr}\left(\mathbf{R}_{i i}^{1 / 2}\right)-\operatorname{tr}\left(\mathbf{R}^{1 / 2}\right)}{\left\{n_{i=1}^{k} \operatorname{tr}\left(\mathbf{R}_{i i}^{1 / 2}\right)-\operatorname{tr}\left(\mathbf{R}_{\mathrm{m}}^{1 / 2}\right)\right\}^{2}} \frac{1}{2} \operatorname{tr}\left(\boldsymbol{\Upsilon}_{1} \mathbf{H}\right) \\
& =\frac{1}{2 C_{1}}\left(1-D_{1}(\mathbf{R})\right) \operatorname{tr}\left(\mathbf{R}_{0}^{-1 / 2} \mathbf{H}\right)-\frac{1}{2 C_{1}} \operatorname{tr}\left(\mathbf{R}^{-1 / 2} \mathbf{H}\right)+\frac{1}{2 C_{1}} D_{1}(\mathbf{R}) \operatorname{tr}\left(\Upsilon_{1} \mathbf{H}\right) \\
& =\frac{1}{2 C_{1}}\left(-\operatorname{tr}\left(\mathbf{R}^{-1 / 2} \mathbf{H}\right)+\left(1-D_{1}(\mathbf{R})\right) \operatorname{tr}\left(\mathbf{R}_{0}^{-1 / 2} \mathbf{H}\right)+D_{1}(\mathbf{R}) \operatorname{tr}\left(\boldsymbol{\Upsilon}_{1} \mathbf{H}\right)\right)
\end{aligned}
$$

where we used the definition of $D_{1}$ and the fact that $\sum_{\ell=1}^{k} \operatorname{tr}\left(\mathbf{R}_{\ell \ell}^{-1 / 2} \mathbf{H}_{\ell \ell}\right)=\operatorname{tr}\left(\mathbf{R}_{\mathbf{0}}^{-1 / 2} \mathbf{H}\right)$. The result follows from the linearity of the trace operator and applying the chain rule to $f(g(\mathbf{R}))=D_{1}(\mathbf{R})$.

# Differentiability of $D_{2}$ 

Consider the function

$$
f:(0, \infty)^{3} \rightarrow \mathbb{R}:(x, y, z) \mapsto \frac{z-x}{z-y}
$$

Then, $D_{2}(\mathbf{R})=f(x, y, z)$ and $D_{2}\left(\mathbf{R}+t \mathbf{H}_{t}\right)=f\left(x_{t}, y_{t}, z_{t}\right)$, where

$$
x=\operatorname{tr}\left\{\left(\mathbf{R}_{0}^{1 / 2} \mathbf{R} \mathbf{R}_{0}^{1 / 2}\right)^{1 / 2}\right\}, y=\operatorname{tr}\left\{\left(\mathbf{R}_{0}^{1 / 2} \mathbf{R}_{\mathbf{m}} \mathbf{R}_{0}^{1 / 2}\right)^{1 / 2}\right\}, z=\operatorname{tr}(\mathbf{R})
$$

and similarly for $x_{t}, y_{t}$ and $z_{t}$ with $\mathbf{R}+t \mathbf{H}_{t}$ instead of $\mathbf{R}$. From Lemma 4 and Lemma 5, we have



Evidently

$$
\lim _{t \rightarrow 0^{+}} \frac{z_{t}-z}{t}=\operatorname{tr}(\mathbf{H}) .
$$

Hence, the Fréchet derivative of the map

$$
g: \mathbb{S}_{q} \rightarrow(0, \infty)^{3}: \mathbf{A} \mapsto\left(\operatorname{tr}\left\{\left(\mathbf{A}_{0}^{1 / 2} \mathbf{A} \mathbf{A}_{0}^{1 / 2}\right)^{1 / 2}\right\}, \operatorname{tr}\left\{\left(\mathbf{A}_{0}^{1 / 2} \mathbf{A}_{\mathbf{m}} \mathbf{A}_{0}^{1 / 2}\right)^{1 / 2}\right\}, \operatorname{tr}(\mathbf{A})\right)
$$

at $\mathbf{R}$ in the direction of $\mathbf{H}$ equals

$$
\left(\frac{1}{2} \operatorname{tr}\left\{\left(\mathbf{J}_{0}+\mathbf{J}_{-1}\right) \mathbf{H}\right\}, \operatorname{tr}\left(\Upsilon_{2} \mathbf{H}\right), \operatorname{tr}(\mathbf{H})\right)
$$

which we will call $\Delta(\mathbf{H})$. The Jacobian matrix of $f$ is given by

$$
\mathbf{J}_{f}=\left(\frac{\partial f}{\partial x} \frac{\partial f}{\partial y} \frac{\partial f}{\partial z}\right)=\left(-\frac{1}{z-y} \frac{z-x}{(z-y)^{2}} \frac{x-y}{(z-y)^{2}}\right)
$$




---

such that the total derivative of $f$ at $\mathbf{g}(\mathbf{R})$ in the direction of $\Delta(\mathbf{H})$ becomes

$$
\begin{aligned}
& \left.\mathrm{J}_{f}\right|_{\mathrm{g}(\mathrm{R})} \Delta(\mathrm{H})^{\mathrm{T}}=\frac{1}{2 \operatorname{tr}\left\{\left(\mathrm{R}_{0}^{1 / 2} \mathrm{R}_{\mathrm{m}} \mathrm{R}_{0}^{1 / 2}\right)^{1 / 2}\right\}-\operatorname{tr}(\mathrm{R})} \\
& +\frac{\operatorname{tr}(\mathbf{R})-\operatorname{tr}\left\{\left(\mathrm{R}_{0}^{1 / 2} \mathbf{R} \mathrm{R}_{0}^{1 / 2}\right)^{1 / 2}\right\}}{\left[\operatorname{tr}(\mathbf{R})-\operatorname{tr}\left\{\left(\mathbf{R}_{\mathbf{0}}^{1 / 2} \mathrm{R}_{\mathrm{m}} \mathrm{R}_{\mathbf{0}}^{1 / 2}\right)^{1 / 2}\right\}\right]^{2}} \operatorname{tr}\left(\Upsilon_{2} \mathbf{H}\right) \\
& +\frac{\operatorname{tr}\left\{\left(\mathrm{R}_{0}^{1 / 2} \mathbf{R R}_{0}^{1 / 2}\right)^{1 / 2}\right\}-\operatorname{tr}\left\{\left(\mathrm{R}_{0}^{1 / 2} \mathrm{R}_{\mathrm{m}} \mathrm{R}_{0}^{1 / 2}\right)^{1 / 2}\right\}}{\left[\operatorname{tr}(\mathrm{R})-\operatorname{tr}\left\{\left(\mathrm{R}_{0}^{1 / 2} \mathrm{R}_{\mathrm{m}} \mathrm{R}_{0}^{1 / 2}\right)^{1 / 2}\right\}\right]^{2}} \operatorname{tr}(\mathrm{H}) \\
& =\frac{1}{\mathrm{C}_{2}}\left(-\frac{1}{2} \operatorname{tr}\left\{\left(\mathbf{J}_{0}+\mathbf{J}_{-1}\right) \mathbf{H}\right\}+\mathrm{D}_{2}(\mathrm{R}) \operatorname{tr}\left(\Upsilon_{2} \mathbf{H}\right)+\left(1-\mathrm{D}_{2}(\mathrm{R})\right) \operatorname{tr}(\mathrm{H})\right)
\end{aligned}
$$

Applying the delta method
Next, we consider the estimator $\widehat{\mathbf{R}}_{\mathrm{n}}$. Theorem 3.1 in [28] tells us that

$$
\begin{aligned}
\sqrt{\mathrm{n}}\left(\widehat{\mathbf{R}}_{\mathrm{n}}-\mathbf{R}\right) & -\frac{1}{\sqrt{\mathrm{n}}} \sum_{\ell=1}^{\mathrm{n}}\left[\mathbf{Z}^{(\ell)}\left(\mathbf{Z}^{(\ell)}\right)^{\mathrm{T}}-\frac{1}{2}\left\{\operatorname{diag}\left(\mathbf{Z}^{(\ell)}\left(\mathbf{Z}^{(\ell)}\right)^{\mathrm{T}}\right) \mathbf{R}+\mathbf{R} \operatorname{diag}\left(\mathbf{Z}^{(\ell)}\left(\mathbf{Z}^{(\ell)}\right)^{\mathrm{T}}\right)\right\}\right] \\
& \xrightarrow{p} \mathbf{0}_{\mathrm{q} \times \mathrm{q}}
\end{aligned}
$$

as $\mathrm{n} \rightarrow \infty$, where $\mathbf{Z}^{(\ell)}=\left(\mathbf{Z}_{1}^{(\ell)}, \ldots, \mathbf{Z}_{k}^{(\ell)}\right)^{\mathrm{T}}$, with $\mathbf{Z}_{\mathrm{i}}^{(\ell)}=\left(\mathbf{Z}_{\mathrm{i} 1}^{(\ell)}, \ldots, \mathbf{Z}_{\mathrm{id}_{\mathrm{i}}}^{(\ell)}\right)$ for $\mathrm{i} \in\{1, \ldots, k\}$, for $\ell \in\{1, \ldots, \mathrm{n}\}$ is a sample from the $\mathcal{N}_{\mathrm{q}}\left(\mathbf{0}_{\mathrm{q}}, \mathbf{R}\right)$ distribution. The same expansion holds when $\widehat{\mathbf{R}}_{\mathrm{n}}$ is the empirical correlation matrix of $\mathbf{Z}^{(1)}, \ldots, \mathbf{Z}^{(\mathrm{n})}$, see, e.g., Lemma 8 in [36]. Hence

as $n \rightarrow \infty$, i.e., making use of the empirical correlation matrix based on a true Gaussian sample or based on a pseudo Gaussian sample, results in the same asymptotic expansion. Suppose further that $\mathbf{R}=\mathbf{U} \boldsymbol{\Lambda} \mathbf{U}^{\mathrm{T}}$ is the eigendecomposition of R . Then $\mathbf{Z}^{(\ell)}=\mathbf{U} \boldsymbol{\Lambda}^{1 / 2} \boldsymbol{\epsilon}^{(\ell)}$ for $\ell \in\{1, \ldots, n\}$ and $\boldsymbol{\epsilon}^{(1)}, \ldots, \boldsymbol{\epsilon}^{(\mathrm{n})}$ a sample from $\mathcal{N}_{\mathrm{q}}\left(\mathbf{0}_{\mathrm{q}}, \mathbf{I}_{\mathrm{q}}\right)$. From Lemma 7 of [36], we have

as $\mathrm{n} \rightarrow \infty$, where W is a random symmetric matrix with $\mathrm{W}_{\mathrm{jk}} \sim \mathcal{N}(0,2)$ if $\mathrm{j}=\mathrm{k} \in\{1, \ldots, \mathrm{q}\}$ and $\mathrm{W}_{\mathrm{jk}} \sim \mathcal{N}(0,1)$ if $1 \leq \mathrm{j}<\mathrm{k} \leq \mathrm{q}$ independently (and similarly for $\mathrm{k}<\mathrm{j}$ ). Moreover, for $\mathrm{A}, \mathrm{B} \in \mathcal{S}_{\mathrm{q}}$, it holds that

$$
\mathrm{E}\left(\operatorname{tr}(\mathrm{AW}) \operatorname{tr}(\mathrm{BW})\right)=2 \operatorname{tr}(\mathrm{AB})
$$

We find

as $\mathrm{n} \rightarrow \infty$. Applying the delta method (and using that $\phi(\mathbf{R})=\mathrm{D}_{\mathbf{R}}^{-1 / 2} \mathrm{RD}_{\mathbf{R}}^{-1 / 2}=\mathbf{R}$ ), we obtain

$$
\begin{aligned}
& \sqrt{\mathrm{n}}\left(\mathrm{D}_{\mathrm{r}}\left(\widehat{\mathbf{R}}_{\mathrm{n}}\right)-\mathrm{D}_{\mathrm{r}}(\mathrm{R})\right) \xrightarrow{\mathrm{d}} \operatorname{tr}\left\{\left(\mathbf{M}_{\mathrm{r}}-\mathbf{D}_{\mathbf{M}_{\mathbf{r}}} \mathbf{R}\right) \mathbf{U} \boldsymbol{\Lambda}^{1 / 2} \mathbf{W} \boldsymbol{\Lambda}^{1 / 2} \mathbf{U}^{\mathrm{T}}\right\} \\
& =\operatorname{tr}\left\{\Lambda^{1 / 2} \mathbf{U}^{\mathrm{T}}\left(\mathbf{M}_{\mathrm{r}}-\mathbf{D}_{\mathbf{M}_{\mathbf{r}}} \mathbf{R}\right) \mathbf{U} \Lambda^{1 / 2} \mathbf{W}\right\},
\end{aligned}
$$

as $\mathrm{n} \rightarrow \infty$. The latter asymptotic expression is centered Gaussian with asymptotic variance

$$
2 \operatorname{tr}\left[\left\{\boldsymbol{\Lambda}^{1 / 2} \mathbf{U}^{\mathrm{T}}\left(\mathbf{M}_{\mathrm{r}}-\mathbf{D}_{\mathbf


---

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
& =\int_{\mathbb{R}^{2}} \Phi^{-1}\left(\widehat{F}_{i j}^{*}(x)\right) \Phi^{-1}\left(\widehat{F}_{m t}^{*}(y)\right) d \widehat{H}(x, y)-\int_{\mathbb{R}^{2}} \Phi^{-1}\left(F_{i j}(x)\right) \Phi^{-1}\left(F_{m t}(y)\right) d H(x, y) \\
& =A_{1 n}+A_{2 n}+A_{3 n}+B_{1 n}+B_{2 n}+R_{n}
\end{aligned}
$$

where (denoting $\phi$ for the standard normal density function)

$$
\begin{aligned}
& A_{1 n}=\int_{\mathbb{R}^{2}} \Phi^{-1}\left(F_{i j}(x)\right) \Phi^{-1}\left(F_{m t}(y)\right) d(\widehat{H}-H)(x, y) \\
& A_{2 n}=\int_{\mathbb{R}^{2}} \frac{\widehat{F}_{i j}^{*}(x)-F_{i j}(x)}{\phi\left(\Phi^{-1}\left(F_{i j}(x)\right)\right)} \Phi^{-1}\left(F_{m t}(y)\right) d H(x, y) \\
& A_{3 n}=\int_{\mathbb{R}^{2}} \frac{\widehat{F}_{m t}^{*}(y)-F_{m t}(y)}{\phi\left(\Phi^{-1}\left(F_{m t}(y)\right)\right)} \Phi^{-1}\left(F_{i j}(x)\right) d H(x, y) \\
& B_{1 n}=\int_{\mathbb{R}^{2}}\left\{\Phi^{-1}\left(\widehat{F}_{i j}^{*}(x)\right)-\Phi^{-1}\left(F_{i j}(x)\right)\right\} \Phi^{-1}\left(F_{m t}(y)\right) d \widehat{H}(x, y)-A_{2 n} \\
& B_{2 n}=\int_{\mathbb{R}^{2}}\left\{\Phi^{-1}\left(\widehat{F}_{m t}^{*}(y)\right)-\Phi^{-1}\left(F_{m t}(y)\right)\right\} \Phi^{-1}\left(F_{i j}(x)\right) d \widehat{H}(x, y)-A_{3 n} \\
& R_{n}=\int_{\mathbb{R}^{2}}\left\{\Phi^{-1}\left(\widehat{F}_{i j}^{*}(x)\right)-\Phi^{-1}\left(F_{i j}(x)\right)\right\}\left\{\Phi^{-1}\left(\widehat{F}_{m t}^{*}(y)\right)-\Phi^{-1}\left(F_{m t}(y)\right)\right\} d \widehat{H}(x, y)
\end{aligned}
$$

Lemma A.3. in [3] tells us that

$$
\mathbb{P}\left[\left|A_{1 n}\right| \geq \epsilon\right] \leq C_{1} \exp \left(-C_{2} n \epsilon^{2}\right)
$$

for $\epsilon \leq \delta_{1}$, where $C_{1}, C_{2}>0$ and $\delta_{1}>0$ only depend on $\epsilon_{0}$. Next, since

$$
d H(x, y)=\phi_{G}\left(\Phi^{-1}\left(F_{i j}(x)\right), \Phi^{-1}\left(F_{m t}(y)\right)\right) d \Phi^{-1}\left(F_{i j}(x)\right) d \Phi^{-1}\left(F_{m t}(y)\right)
$$




---

with $\varphi_{\mathrm{G}}$ the density of $\Phi_{\mathrm{G}}$, we see that

$$
\begin{aligned}
& A_{2 n}=\int_{\mathbb{R}^{2}} \frac{\widehat{F}_{i j}^{*}(\mathbf{x})-F_{i j}(\mathbf{x})}{\varphi\left(\Phi^{-1}\left(F_{i j}(\mathbf{x})\right)\right.} \Phi^{-1}\left(F_{m t}(\mathbf{y})\right) \varphi_{\mathrm{G}}\left(\Phi^{-1}\left(F_{i j}(\mathbf{x})\right), \Phi^{-1}\left(F_{m t}(\mathbf{y})\right)\right) \mathrm{d} \Phi^{-1}\left(F_{i j}(\mathbf{x})\right) \mathrm{d} \Phi^{-1}\left(F_{m t}(\mathbf{y})\right)
\end{aligned}
$$


$$
\begin{aligned}
& =\rho_{i j, m t} \varphi\left(\Phi^{-1}\left(F_{i j}(\mathbf{x})\right)\right) \Phi^{-1}\left(F_{i j}(\mathbf{x})\right)
\end{aligned}
$$


since $\mathbb{E}\left(X_{2} \mid X_{1}=x_{1}\right)=\rho x_{1}$ when $\left(X_{1}, X_{2}\right)$ follows a bivariate standard normal distribution with correlation $\rho$. Hence

$$
\begin{aligned}
A_{2 n} & =\rho_{i j, m t} \int_{\mathbb{R}} \Phi^{-1}\left(F_{i j}(\mathbf{x})\right)\left(\widehat{F}_{i j}^{*}(\mathbf{x})-F_{i j}(\mathbf{x})\right) \mathrm{d} \Phi^{-1}\left(F_{i j}(\mathbf{x})\right) \\
& =-\frac{\rho_{i j, m t}}{2} \int_{\mathbb{R}}\left\{\Phi^{-1}\left(F_{i j}(\mathbf{x})\right)\right\}^{2} \mathrm{~d}\left(\widehat{F}_{i j}^{*}-F_{i j}\right)(\mathbf{x}) \\
& =-\frac{\rho_{i j, m t}}{2} \frac{1}{n} \sum_{\ell=1}^{n}\left(\left\{\Phi^{-1}\left(F_{i j}\left(X_{i j}^{(\ell)}\right)\right)\right\}^{2}-1\right)=-\frac{\rho_{i j, m t}}{2} \frac{1}{n} \sum_{\ell=1}^{n}\left(V_{\ell}^{2}-1\right)
\end{aligned}
$$

where we did partial integration, and $V_{\ell} \sim \chi_{1}^{2}$ for $\ell=1, \ldots, n$. Hence, using Theorem 3.2 on page 45 of [41] (noting that condition $(\mathrm{P})(3.12)$ on page 45 holds for $\chi_{1}^{2}$, see also the proof of Lemma A.3. in [3]), we have

$$
P\left[\left|A_{2 n}\right| \geq \epsilon\right] \leq C_{3} \exp \left(-C_{4} n \epsilon^{2}\right)
$$

for $\epsilon \leq \delta_{2}$, where $C_{3}, C_{4}$ and $\delta_{2}>0$ only depend on $\epsilon_{0}$. A very similar argument holds for $A_{3 n}$.
Next, we deal with the term $B_{1 n}$. By symmetry, the term $B_{2 n}$ can be dealt with similarly. We use the mean value theorem, giving that

$$
\Phi^{-1}\left(\widehat{F}_{i j}^{*}(\mathbf{x})\right)-\Phi^{-1}\left(F_{i j}(\mathbf{x})\right)=\frac{\widehat{F}_{i j}^{*}(\mathbf{x})-F_{i j}(\mathbf{x})}{\varphi\left(\Phi^{-1}\left(\widetilde{F}_{i j}^{*}(\mathbf{x})\right)\right)}
$$

for a certain $\widetilde{F}_{i j}^{*}(\mathbf{x})$ satisfying $\left|\widetilde{F}_{i j}^{*}(\mathbf{x})-F_{i j}(\mathbf{x})\right| \leq\left|\widehat{F}_{i j}^{*}(\mathbf{x})-F_{i j}(\mathbf{x})\right|$. Of course, $\left|\Phi^{-1}(t)\right| \rightarrow \infty$ when $t \rightarrow 0$ or $t \rightarrow 1$, and $\varphi(t) \rightarrow 0$ when $|t| \rightarrow \infty$, so we will need to further split up $B_{1 n}$ by defining the set $M_{\eta}=M_{\eta_{1}} \times M_{\eta_{2}}$, where

$$
\begin{aligned}
& M_{\eta_{1}}=\left[F_{i j}^{-1}(\eta), F_{i j}^{-1}(1-\eta)\right] \\
& M_{\eta_{2}}=\left[F_{m t}^{-1}(\eta), F_{m t}^{-1}(1-\eta)\right]
\end{aligned}
$$

for a certain small $\eta>0$. Doing so, we can write

$$
B_{1 n}=B_{\eta_{1} 1 n}+B_{\eta_{2} 1 n}+B_{\eta_{3} 1 n}+B_{\eta_{4} 1 n}
$$




---

where

$$
\begin{aligned}
& B_{\eta 11 n}=\int_{M_{n}^{\bar{\eta}}}\left\{\Phi^{-1}\left(\widehat{F}_{i j}^{*}(x)\right)-\Phi^{-1}\left(F_{i j}(x)\right)\right\} \Phi^{-1}\left(F_{m t}(y)\right) \mathrm{d} \widehat{H}(x, y) \\
& B_{\eta 21 n}=\int_{M_{\eta}}\left\{\left(\widehat{F}_{i j}^{*}(x)-F_{i j}(x)\right) \phi\left(\Phi^{-1}\left(\widetilde{F}_{i j}^{*}(x)\right)\right)-\left(\widehat{F}_{i j}^{*}(x)-F_{i j}(x)\right) \phi\left(\Phi^{-1}\left(F_{i j}(x)\right)\right)\right\} \Phi^{-1}\left(F_{m t}(y)\right) \mathrm{d} \widehat{H}(x, y) \\
& B_{\eta 31 n}=\int_{M_{\eta}}\left(\widehat{F}_{i j}^{*}(x)-F_{i j}(x)\right) \phi\left(\Phi^{-1}\left(F_{i j}(x)\right)\right) \Phi^{-1}\left(F_{m t}(y)\right) \mathrm{d}(\widehat{H}-H)(x, y) \\
& B_{\eta 41 n}=\int_{M_{\eta}}\left(\widehat{F}_{i j}^{*}(x)-F_{i j}(x)\right) \phi\left(\Phi^{-1}\left(F_{i j}(x)\right)\right) \Phi^{-1}\left(F_{m t}(y)\right) \mathrm{d} H(x, y)-A_{2 n}
\end{aligned}
$$

Notice that we did not apply the mean value theorem in the term $B_{\eta 11 n}$, because we will decompose $R_{n}$ as

$$
R_{n}=R_{\eta 1 n}+R_{\eta 2 n}+R_{\eta 3 n}
$$

where

$$
\begin{aligned}
& R_{\eta 1 n}=\int_{M_{n}^{\bar{\eta}}}\left\{\Phi^{-1}\left(\widehat{F}_{i j}^{*}(x)\right)-\Phi^{-1}\left(F_{i j}(x)\right)\right\} \Phi^{-1}\left(\widehat{F}_{m t}^{*}(y)\right) \mathrm{d} \widehat{H}(x, y) \\
& R_{\eta 2 n}=-\int_{M_{n}^{\bar{\eta}}}\left\{\Phi^{-1}\left(\widehat{F}_{i j}^{*}(x)\right)-\Phi^{-1}\left(F_{i j}(x)\right)\right\} \Phi^{-1}\left(F_{m t}(y)\right) \mathrm{d} \widehat{H}(x, y) \\
& R_{\eta 3 n}=\int_{M_{\eta}} \frac{\widehat{F}_{i j}^{*}(x)-F_{i j}(x)}{\phi\left(\Phi^{-1}\left(\widetilde{F}_{i j}^{*}(x)\right)\right)}\left\{\Phi^{-1}\left(F_{m t}^{*}(y)\right)-\Phi^{-1}\left(F_{m t}(y)\right)\right\} \mathrm{d} \widehat{H}(x, y)
\end{aligned}
$$

such that $B_{\eta 11 n}$ and $R_{\eta 2 n}$ cancel each other out. As for $B_{\eta 21 n}$, it holds almost surely that

$$
\left|B_{\eta 21 n}\right| \leq \sup _{x \in \mathbb{R}}\left|\widehat{F}_{i j}^{*}(x)-F_{i j}(x)\right| \sup _{x \in M_{\eta 1}}\left|\frac{1}{\phi\left(\Phi^{-1}\left(\widetilde{F}_{i j}^{*}(x)\right)\right)}-\frac{1}{\phi\left(\Phi^{-1}\left(F_{i j}(x)\right)\right)}\right| \sup _{y \in M_{\eta 2}} \Phi^{-1}\left(F_{m t}(y)\right)
$$

The function $\Phi^{-1} \circ F_{m t}$ is uniformly bounded on $M_{\eta_{2}}$ and since $\phi \circ \Phi^{-1}$ is continuous, it is uniformly continuous on $M_{\eta 1}$. This, and the fact that $\left|\widetilde{F}_{i j}^{*}-F_{i j}\right| \leq\left|\widehat{F}_{i j}^{*}-F_{i j}\right|$, results in

$$
\left|B_{\eta 21 n}\right| \leq K \sup _{x \in \mathbb{R}}\left|\widehat{F}_{i j}^{*}(x)-F_{i j}(x)\right|
$$

almost surely for a certain $K>0$. Hence, using (D.2), we obtain

$$
\begin{aligned}
& \mathbb{P}\left[\left|B_{\eta 21 n}\right| \geq \epsilon\right] \leq \mathbb{P}\left[\sup _{x \in \mathbb{R}}\left|\widehat{F}_{i j}^{*}(x)-F_{i j}(x)\right| \geq \frac{\epsilon}{K}\right] \\
& \leq \mathbb{P}\left[\sup _{x \in \mathbb{R}}\left|\widehat{F}_{i j}(x)-F_{i j}(x)\right| \geq \frac{\epsilon}{2 K}\right]+\mathbb{P}\left[\sup _{x \in \mathbb{R}}\left|\widehat{F}_{i j}^{*}(x)-\widehat{F}_{i j}(x)\right| \geq \frac{\epsilon}{2 K}\right] \\
& \leq 2 \exp \left(-\frac{n \epsilon^{2}}{2 K^{2}}\right)+\mathbb{P}\left[\frac{1}{n+1} \geq \frac{\epsilon}{2 K}\right] .
\end{aligned}
$$

Similar arguments hold for the terms $B_{\eta 31 n}, B_{\eta 41 n}$ and $R_{\eta 3 n}$.
The only term that is not discussed yet, is $R_{\eta 1 n}$. We want this term to converge to zero in probability when $\eta \rightarrow 0$ for every $n$. We can deal with this in a similar way as in Corollary 5.6. of [40] (in fact, we are even in the context of Section 6 on page 1133 since Assumption 2.3(b) holds), since the corresponding assumptions hold here (they are verified in the proof of Theorem 3.1 of [28]). In our setting, the key ingredient is that there exists $a=b=(1 / 2-\xi) / 2$ for a certain $0<\xi<1 / 2$ such that

$$
\left|\Phi^{-1}(t)\right| \leq M_{1} r^{a}(t), \quad \text { with } \quad r(t)=\frac{1}{t(1-t)}
$$




---

for all $t \in(0,1)$ and a certain $M_{1}>0$, i.e., $\left|\Phi^{-1}(t)\right| \rightarrow \infty$ as $t \rightarrow 0$ or $t \rightarrow 1$, but not too fast. Applying the mean value theorem again, we have

$$
\begin{aligned}
\left|\Phi^{-1}\left(\widehat{F}_{i j}^{*}(x)\right)-\Phi^{-1}\left(F_{i j}(x)\right)\right| & =\left|\left(\widehat{F}_{i j}^{*}(x)-F_{i j}(x)\right)\left[\Phi^{-1}\left(\widetilde{F}_{i j}^{*}(x)\right)\right]^{\prime}\right| \\
& \leq M_{1}\left|\widehat{F}_{i j}^{*}(x)-F_{i j}(x)\right| r_{a+1}\left(\widetilde{F}_{i j}^{*}(x)\right)
\end{aligned}
$$

Moreover, if we take $\widetilde{\epsilon}_{1}>0$ arbitrary, there exist $M_{2}, M_{3}, M_{4}>0$ such that, uniformly in $n$, the events

$$
\begin{aligned}
& E_{1 n}=\left\{\left|\widehat{F}_{i j}^{*}-F_{i j}\right| \leq M_{2} r_{-1 / 2+\xi / 4}\left(F_{i j}\right)\right\} \\
& E_{2 n}=\left\{r_{a}\left(\widehat{F}_{m t}^{*}\right) \leq M_{3} r_{a}\left(F_{m t}\right)\right\} \\
& E_{3 n}=\left\{r_{a+1}\left(\widetilde{F}_{i j}^{*}\right) \leq M_{4} r_{a+1}\left(F_{i j}\right)\right\}
\end{aligned}
$$

satisfy $\mathbb{P}\left(E^{C}\right)<\widetilde{\epsilon}_{1} / 2$, for $E=\cap_{i=1}^{3} E_{i n}$. Combining the inequalities, we also see that (similarly to expression (5.2) in $[40])$

$$
\mathbb{E}\left(\mathbb{1}(E)\left|R_{\eta 1 n}\right|\right) \leq M_{1}^{2} M_{2} M_{3} M_{4} \int_{M_{\eta}^{C}} r_{a+1 / 2+\xi / 4}\left(F_{i j}(x)\right) r_{a}\left(F_{m t}(y)\right) \mathrm{d} H(x, y)
$$

where $\mathbb{1}$ is the indicator function. By Hölder's inequality, the above integral is bounded by (noting that $M_{\eta}^{C} \subset$ $\left.\left(M_{\eta 1}^{C} \times \mathbb{R}\right) \cup\left(\mathbb{R} \times M_{\eta 2}^{C}\right)\right)$

$$
\begin{gathered}
\left(\int_{(0, \eta) \cup(1-\eta, 1)} r_{p_{1}(a+1 / 2+\xi / 4)}(t) \mathrm{d} t\right)^{1 / p_{1}}\left(\int_{0}^{1} r_{q_{1} a}(t) \mathrm{d} t\right)^{1 / q_{1}} \\
+\left(\int_{1}^{1} r_{p_{1}(a+1 / 2+\xi / 4)}(t) \mathrm{d} t\right)^{1 / p_{1}}\left(\int_{(0, \eta) \cup(1-\eta, 1)} r_{q_{1} a}(t) \mathrm{d} t\right)^{1 / q_{1}}<\infty
\end{gathered}
$$

where $p_{1}$ and $q_{1}$ are chosen such that $p_{1}^{-1}+q_{1}^{-1}=1, p_{1}(a+1 / 2+\xi / 4)<1$ and $q_{1} a<1$ (see equation (3.5) in [40] and corresponding explanation), making the integral bounded. Hence, by dominated convergence, we have that $\mathbb{1}(E)\left|R_{\eta 1 n}\right| \xrightarrow{p} 0$ as $\eta \rightarrow 0$ for each $n$. Hence, for our arbitrarily chosen $\widetilde{\epsilon}_{1}>0$, and another arbitrary $\widetilde{\epsilon}_{2}>0$, we see that

$$
\begin{aligned}
& \mathbb{P}\left[\left|R_{\eta 1 n}\right|>\widetilde{\epsilon}_{2}\right]=\mathbb{P}\left[\left|R_{\eta 1 n}\right|>\widetilde{\epsilon}_{2}, \mathbb{1}(E)=1\right]+\mathbb{P}\left[\left|R_{\eta 1 n}\right|>\widetilde{\epsilon}_{2}, \mathbb{1}(E)=0\right] \\
& =\mathbb{P}\left[\mathbb{1}(E)\left|R_{\eta 1 n}\right|>\widetilde{\epsilon}_{2}\right]+\mathbb{P}\left[\left|R_{\eta 1 n}\right|>\widetilde{\epsilon}_{2}, \mathbb{1}(E)=0\right] \\
& \leq \mathbb{P}\left[\mathbb{1}(E)\left|R_{\eta 1 n}\right|>\widetilde{\epsilon}_{2}\right]+\mathbb{P}[\mathbb{1}(E)=0] \\
& =\mathbb{P}\left[\mathbb{1}(E)\left|R_{\eta 1 n}\right|>\widetilde{\epsilon}_{2}\right]+\mathbb{P}\left(E^{C}\right)<\frac{\widetilde{\epsilon}_{1}}{2}+\frac{\widetilde{\epsilon}_{1}}{2}=\widetilde{\epsilon}_{1}
\end{aligned}
$$

for $\eta$ small enough, i.e., $\left|R_{\eta 1 n}\right| \xrightarrow{p} 0$ as $\eta \rightarrow 0$ for all $n$. This means that $\mathbb{P}\left[\left|R_{\eta 1 n}\right| \geq \epsilon\right]$ can be made zero for every $n$ by letting $\eta \rightarrow 0$, and, combining everything, we have shown that a concentration inequality (D.1) holds. In simplified form, we can say that (D.1) holds with

$$
f(\epsilon, n)=K_{1} \exp \left(-K_{2} n \epsilon^{2}\right)+K_{3} \mathbb{P}\left[\frac{1}{n+1} \geq \frac{\epsilon}{K_{4}}\right]
$$

for $0<\epsilon \leq \delta$, where $K_{1}, K_{2}, K_{3}, K_{4}, \delta>0$ possibly only depend on $\epsilon_{0}$.
We now show that $\left\|\widehat{R}_{n}-R_{n}\right\|_{\infty}=O_{p}\left(\{1 n(q n) / n\}^{1 / 2}\right)$. Take an arbitrary $\varepsilon>0$. Let $M, N>0$ be such that $2-K_{2} M^{2}<0, K_{1} q_{n}^{2-K_{2} M^{2}}<\varepsilon, M n^{-1 / 2} \ln (q n)^{1 / 2} \leq \delta$ and $1 /(n+1)<M n^{-1 / 2} \ln (q n)^{1 / 2} / K_{4}$ for all $n>N$. Then, by the




---

union bound, it holds that

$$
\begin{aligned}
P\left[\left\|\widehat{\Gamma}_{n}-\Gamma_{n}\right\|_{\infty} n^{-1 / 2} \ln \left(q_{n}\right)^{1 / 2}>M\right] & =P\left[\left\|\widehat{\Gamma}_{n}-\Gamma_{n}\right\|_{\infty}>M n^{-1 / 2} \ln \left(q_{n}\right)^{1 / 2}\right] \\
& \leq q_{n}^{2} K_{1} \exp \left\{-K_{2} n\left(M n^{-1 / 2} \ln \left(q_{n}\right)^{1 / 2}\right)^{2}\right\} \\
& +q_{n}^{2} K_{3} P\left[\frac{1}{n+1} \geq \frac{M n^{-1 / 2} \ln \left(q_{n}\right)^{1 / 2}}{K_{4}}\right] \\
& =K_{1} q^{2-K_{2} M_{n}^{2}} \\
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
[6] J. Bigot, R. J. Biscay, J.-M. Loubes, L. Muñiz-Alvarez, Group lasso estimation of high-dimensional covariance matrices, J. Mach. Learn. Res. 12 (2011) 3187-3225.
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
[22] I. Gijbels, V. Kika, M. Omelka, On the specification of multivariate association measures and their behaviour with increasing dimension, J. Multivar. Anal. 182 (2021) 104704.
[23] O. Grothe, J. Schnieders, J. Segers, Measuring association and dependence between random vectors, J. Multivar. Anal. 123 (2014) 96-110.
[24] J. Hájek, Z. Šidák, Theory of Rank Tests, Academia, Prague, 1967.
[25] N. J. Higham, Functions of Matrices, SIAM, 2008.
[26] M. Hofert, W. Oldford, A. Prasad, M. Zhu, A framework for measuring association of random vectors via collapsed random variables, J. Multivar. Anal. 172 (2019) 5-27.
[27] H. Hotelling, Relations between two sets of variates, Biometrika 28 (1936) 321-377.
[28] C. A. J. Klaassen, J. A. Wellner, Efficient estimation in the bivariate normal copula model: normal margins are least favourable, Bernoulli 3 (1997) $55-77$.
[29] C. Lam, J. Fan, Sparsistency and rates of convergence in large covariance matrix estimation, Ann. Stat. 37 (2009) 4254-4278.
[30] S. Lê, F. Husson, SensoMineR: A package for sensory data analysis, J. Sens. Stud. 23 (2008) 14-25.
[31] O. Ledoit, M. Wolf, A well-conditioned estimator for large-dimensional covariance matrices, J. Multivar. Anal. 88 (2004) 365-411.
[32] F. Llobell, V. Cariou, E. Vigneau, A. Labenne, E. M. Qannari, Analysis and clustering of multiblock datasets by means of the STATIS and CLUSTATIS methods. Application to sensometrics, Food


---

[35] I. Medovikov, A. Prokhorov, A new measure of vector dependence, with applications to financial risk and contagion, J. Financ. Econom. 15 (2017) $474-503$.
[36] G. Mordant, J. Segers, Measuring dependence between random vectors via optimal transport, J. Multivar. Anal. 189 (2022) 104912.
[37] R. B. Nelsen, Nonparametric measures of multivariate association, in: L. Rüschendorf, B. Schweizer, M. D. Taylor (Eds.), IMS Lecture Notes - Monograph Series Vol. 28, Distributions with Fixed Marginals and Related Topics, 1996, pp. 223-232.
[38] R. B. Nelsen, An Introduction to Copulas, Springer Science and Business Media, New York, 2006.
[39] V. M. Panaretos, Y. Zemel, Statistical aspects of Wasserstein distances, Annu. Rev. Stat. Appl. 6 (2019) 405-431.
[40] F. H. Ruymgaart, G. R. Shorack, W. R. van Zwet, Asymptotic normality of nonparametric tests for independence, Ann. Math. Stat. 43 (1972) $1122-1135$.
[41] L. Saulis, V. A. Statulevičius, Limit theorems for Large Deviations, Kluwer Academic Publishers, Dordrecht, 1991.
[42] F. Schmid, R. Schmidt, Multivariate extensions of Spearman's rho and related statistics, Stat. Probab. Lett. 77 (2007) 407-416.
[43] A. Sklar, Fonctions de repartition à n dimensions et leurs marges, Publications de l'Institut Statistique de l'Université de Paris 8 (1959) $229-231$.
[44] G. J. Székely, M. L. Rizzo, N. K. Bakirov, Measuring and testing dependence by correlation of distances, Ann. Stat. 35 (2007) 2769-2794.
[45] A. Takatsu, Wasserstein geometry of Gaussian measures, Osaka J. Math. 48 (2011) 1005-1026.
[46] R. C. Thompson, S. Therianos, Inequalities connecting the eigenvalues of a hermitian matrix with the eigenvalues of complementary principal submatrices, Bull. Aust. Math. Soc. 6 (1972) 117-132.
[47] A. Tsanas, M. A. Little, C. Fox, L. O. Ramig, Objective automatic assessment of rehabilitative speech treatment in Parkinson's disease, IEEE Trans. Neural Syst. Rehabil. Eng. 22 (2014) 181-190.
[48] C. Villani, Optimal Transport: Old and New, volume 338, Springer Science \& Business Media, 2008.
[49] H. Wang, Coordinate descent algorithm for covariance graphical lasso, Stat. Comput. 24 (2014) 521-529.
[50] D. I. Warton, Penalized normal likelihood and ridge regularization of correlation and covariance matrices, J. Am. Stat. Assoc. 103 (2008) $340-349$.
[51] L. Zhang, D. Lu, X. Wang, The essential dependence for a group of random vectors, Commun. Stat. - Theory Methods 50 (2020) 1-37.
[52] H. Zou, R. Li, One-step sparse estimates in nonconcave penalized likelihood models, Ann. Stat. 36 (2008) 1509-1533.




---

# Supplementary Material to 

## High-dimensional copula-based Wasserstein dependence

by
Steven De Keyser and Irène Gijbels



Fig. S1: Monte Carlo bias of the estimators $D_{\bullet}\left(\widehat{\mathcal{R}}_{R, n}\right)$ (penalty) and $D_{\bullet}\left(\widehat{\mathcal{R}}_{n}\right)$ (no penalty) for $D_{t \ln (t)}, D_{(\sqrt{t}-1)^{2}}, D_{1}$ and $D_{2}$, based on 1000 replications with sample sizes $n=50,100,500$ as a function of $q$, in two different designs.



Fig. S2: Monte Carlo variance of the estimators $D_{\bullet}\left(\widehat{\mathcal{R}}_{R, n}\right)$ (penalty) and $D_{\bullet}\left(\widehat{\mathcal{R}}_{n}\right)$ (no penalty) for $D_{t \ln (t)}, D_{(\sqrt{t}-1)^{2}}, D_{1}$ and $D_{2}$, based on 1000 replications with sample sizes $n=50,100,500$ as a function of $q$, in two different designs.




---

