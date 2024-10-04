# Decomposition with Monotone B-splines: Fitting and Testing 

Lijun Wang* ${ }^{* 1,2}$, Xiaodan Fan ${ }^{\dagger 1}$, Hongyu Zhao ${ }^{\ddagger 2}$, and Jun S. Liu ${ }^{\S 3}$<br>${ }^{1}$ Department of Statistics, The Chinese University of Hong Kong, Hong Kong SAR, China<br>${ }^{2}$ Department of Biostatistics, Yale University, New Haven, Connecticut, USA<br>${ }^{3}$ Department of Statistics, Harvard University, Cambridge, Massachusetts, USA


#### Abstract

A univariate continuous function can always be decomposed as the sum of a non-increasing function and a non-decreasing one. Based on this property, we propose a non-parametric regression method that combines two spline-fitted monotone curves. We demonstrate by extensive simulations that, compared to standard spline-fitting methods, the proposed approach is particularly advantageous in high-noise scenarios. Several theoretical guarantees are established for the proposed approach. Additionally, we present statistics to test the monotonicity of a function based on monotone decomposition, which can better control Type I error and achieve comparable (if not always higher) power compared to existing methods. Finally, we apply the proposed fitting and testing approaches to analyze the single-cell pseudotime trajectory datasets, identifying significant biological insights for non-monotonically expressed genes through Gene Ontology enrichment analysis. The source code implementing the methodology and producing all results is accessible at https://github.com/szcf-weiya/ MonotoneDecomposition.jl.


Keywords: Function Decomposition; Monotone B-splines; Curve Fitting; Test of Monotonicity.
*Email: ljwang@link.cuhk.edu.hk, lijun.wang@yale.edu
${ }^{\dagger}$ Email: xfan@cuhk.edu.hk
${ }^{\ddagger}$ Email: hongyu.zhao@yale.edu
${ }^{\S}$ Email: jliu@stat.harvard.edu




---

# 1 Introduction 

Suppose we have $n$ pairs of observations $\left(\boldsymbol{x}_{i}, y_{i}\right), i=1, \ldots, n$, with $\boldsymbol{x}_{i} \in \mathbb{R}^{d}, y_{i} \in \mathbb{R}$, independent and identically distributed (i.i.d.) according to an unknown probability distribution $P(X, Y)$. Various methods exist for estimating the conditional expectation function $f(\boldsymbol{x})=E(Y \mid X=\boldsymbol{x})$, ranging from simple linear regressions (including ridge and lasso) to more sophisticated nonlinear techniques. Spline is one of the most popular methods, particularly when $d=1$. Unlike existing methods, we aim to estimate the monotonic components of $f(\boldsymbol{x})$ and then use their sum as an estimator for $f(\boldsymbol{x})$. This is because any general function can be decomposed into the sum of an increasing function $f^{\text {up }}(\boldsymbol{x})$ and a decreasing function $f^{\text {down }}(\boldsymbol{x})$ (a more formal proof is given in the Supplementary Material for self-contained).

The monotone decomposition idea has been exploited by Chipman et al. (2022) in their recent algorithm, where the monotone decomposition is incorporated into fitting monotone Bayesian additive regression trees (mBART). They found that fitting by monotone decomposition with mBART outperforms the corresponding BART algorithm proposed earlier in Chipman et al. (2010). We here focus on the case of $d=1$, and adopt B-spline basis functions to represent the monotone components,

$$
f^{\mathrm{up}}(x)=\sum_{j=1}^{J_{u}} \gamma_{j}^{u} B_{j}^{u}(x)+\varepsilon^{u}, \quad f^{\text {down }}(x)=\sum_{j=1}^{J_{d}} \gamma_{j}^{d} B_{j}^{d}(x)+\varepsilon^{d}
$$

where the superscripts and subscripts " $u$ " and " $d$ " indicate for up (increasing) and down (decreasing), respectively. The monotonicity of each monotone component is ensured by the monotonicity of the coefficients (L. Wang et al., 2023), i.e.,

$$
\gamma_{1}^{u} \leq \gamma_{2}^{u} \leq \cdots \leq \gamma_{J_{u}}^{u} ; \quad \gamma_{1}^{d} \geq \gamma_{2}^{d} \geq \cdots \geq \gamma_{J_{d}}^{d}
$$

This paper is organized as follows. In Section 2, we formulate monotone decomposition with cubic splines and establish properties of the solution, particularly for monotone functions. In Section 3, we propose the monotone decomposition with smoothing splines and establish similar properties and theoretical guarantees. In Section 4, we present simulation results to demonstrate how fitting via monotone decomposition can outperform the corresponding unconstrained fitting, particularly in high-noise scenarios. In Section 5, we propose statistics for testing monotonicity and, in Section 6, we demonstrate the power of the proposed method via simulations. In Section 7, we present the results of our analysis on single-cell pseudo-time trajectory datasets using the fitting and testing techniques based on monotone decomposition. Finally, we discuss the limitations and potential future work in Section 8.

## 2 Monotone Decomposition with Cubic Splines

Cubic splines are the most popular polynomial splines for practitioners. Presumably, cubic splines are the lowest-order splines for which the knot-discontinuity is not visible to the human eye, and there is scarcely any good reason to go beyond cubic splines (Hastie et al., 2009). On the other hand, although there are many equivalent bases for representing a spline function, the B-spline basis system developed by De Boor (1978) is attractive numerically (Ramsay \& Silverman, 2005). Thus, we take the order-4 B-spline basis to represent cubic splines, under which the problem




---

reduces to solving the following optimization problem:

$$
\begin{array}{r}
\min _{\boldsymbol{\gamma}^{u}, \boldsymbol{\gamma}^{d}}\left\|\boldsymbol{y}-\boldsymbol{B}^{u} \boldsymbol{\gamma}^{u}-\boldsymbol{B}^{d} \boldsymbol{\gamma}^{d}\right\|^{2} \\
\text { s.t. } \gamma_{1}^{u} \leq \gamma_{2}^{u} \leq \cdots \leq \gamma_{J}^{u} ; \gamma_{1}^{d} \geq \gamma_{2}^{d} \geq \cdots \geq \gamma_{J}^{d}
\end{array}
$$

where $\boldsymbol{y}=\left(y_{1}, \ldots, y_{n}\right)$ is an $n$-vector of the responses (note that we use round brackets to denote column vectors), $\left(\boldsymbol{B}^{u}\right)_{i k}=B_{k}^{u}\left(x_{i}\right), k=1, \ldots, J_{u},\left(\boldsymbol{B}^{d}\right)_{i \ell}=B_{\ell}^{d}\left(x_{i}\right), \ell=1, \ldots, J_{d}$ are the matrices constructed by evaluating the $B$-spline basis at $\left\{x_{i}\right\}_{i=1}^{n}$, and $\boldsymbol{\gamma}^{u}=\left(\gamma_{1}^{u}, \ldots, \gamma_{J}^{u}\right), \boldsymbol{\gamma}^{d}=\left(\gamma_{1}^{d}, \ldots, \gamma_{J}^{d}\right)$ are the coefficient vectors.

For simplicity, we consider $J_{u}=J_{d}=J$. Note that the knots for determining the $B$-spline basis are conventionally on the quantiles of $x$ 's, then the $B$-spline basis functions are also the same, $B_{k}^{u}=B_{\ell}^{d}$, so the above problem (1) becomes

$$
\begin{gathered}
\min _{\boldsymbol{\gamma}^{u}, \boldsymbol{\gamma}^{d}}\left\|\boldsymbol{y}-\boldsymbol{B}\left(\boldsymbol{\gamma}^{u}+\boldsymbol{\gamma}^{d}\right)\right\|^{2} \\
\text { s.t. } \gamma_{1}^{u} \leq \gamma_{2}^{u} \leq \cdots \leq \gamma_{J}^{u} ; \gamma_{1}^{d} \geq \gamma_{2}^{d} \geq \cdots \geq \gamma_{J}^{d}
\end{gathered}
$$

where $\boldsymbol{B}_{i j}=B_{j}\left(x_{i}\right), j=1, \ldots, J$.
First of all, Proposition 1 establishes the equivalence between problem (2) with the corresponding unconstrained $B$-spline fitting.

Proposition 1. Regardless of the component solutions $\hat{\boldsymbol{\gamma}}^{u}, \hat{\boldsymbol{\gamma}}^{d}$ to problem (2), the overall solution $\hat{\boldsymbol{\gamma}}^{u}+\hat{\boldsymbol{\gamma}}^{d}$ is equivalent to the unconstrained $B$-spline fitting, i.e., the least squares solution,

$$
\hat{\boldsymbol{\gamma}}_{l s}=\underset{\boldsymbol{\gamma}}{\arg \min }\|\boldsymbol{y}-\boldsymbol{B} \boldsymbol{\gamma}\|^{2}=\left(\boldsymbol{B}^{\top} \boldsymbol{B}\right)^{-1} \boldsymbol{B}^{\top} \boldsymbol{y}
$$

Specifically, $\hat{\boldsymbol{\gamma}}^{u}+\hat{\boldsymbol{\gamma}}^{d}=\hat{\boldsymbol{\gamma}}_{l s}$.
Note that the monotone components in (2) are not identifiable, since

$$
\boldsymbol{\gamma}^{u}+\boldsymbol{\gamma}^{d}=\boldsymbol{\gamma}^{u}+\boldsymbol{\delta}+\boldsymbol{\gamma}^{d}-\boldsymbol{\delta}
$$

where $\boldsymbol{\delta}$ is an arbitrary increasing sequence, $\delta_{1} \leq \cdots \leq \delta_{J}$. In other words, the decomposition for a general function is not unique since

$$
f_{\text {up }}(x)+f_{\text {down }}(x)=f_{\text {up }}(x)+h(x)+f_{\text {down }}(x)-h(x)
$$

where $h(x)$ is an arbitrary increasing function.
In order to have a unique decomposition, we consider the closest decomposition in some sense, such as the difference between two monotone components being the smallest in the $L_{2}$ norm. Thus, we consider imposing some discrepancy constraint on problem (2), as detailed in the following subsections, to help obtain a unique solution.

# 2.1 Discrepancy Constraint: A Motivating Example 

Consider the simple function $y=x^{3}, x \in[-1,1]$, which may be decomposed as

$$
x^{3}=\left\{x^{3}+h(x)\right\}+\{0-h(x)\} \triangleq f_{\text {up }}(x)+f_{\text {down }}(x)
$$

where $h(x)$ is an increasing function. If we set $h(0)=0$, then it is easy to show that the magnitude of the difference between the two monotone components is lower-bounded by $\left|x^{3}\right|$, i.e.,

$$
\left|x^{3}\right| \leq\left|x^{3}+2 h(x)\right|
$$




---

Since it is unreasonable to have a decreasing component for a strictly increasing function, the ideal decomposition should correspond to $h(x)=0$. Equation (4) suggests to us that such an ideal decomposition may be obtained by requiring the two monotone components to differ the least. In light of this observation, we introduce the following discrepancy constraint for the two monotone components in the decomposition:

$$
\left\|f_{\mathrm{up}}-f_{\text {down }}\right\|^{2} \leq s
$$

where $s \geq 0$ is a tuning parameter. The role of parameter $s$ can be summarized as follows,

- if $s \rightarrow 0$, then the solution is $\gamma^{\mathrm{u}}=\gamma^{\mathrm{d}}=c \mathbf{1}_{J}$, and hence $\hat{f}_{\mathrm{up}}=\hat{f}_{\text {down }}=c B \mathbf{1}_{J}=c \mathbf{1}_{n}$ are constant functions;
- if $s \rightarrow \infty$, then the problem reduces to be equivalent to the unconstrained B -spline fitting;
- a moderate $s$ imposes some regularization, which is preferable for a better fitting.


# 2.2 General Functions 

With the discrepancy constraint in (5), we can restate problem (2) as

$$
\begin{aligned}
\min _{\gamma^{\mathrm{u}}, \gamma^{\mathrm{d}}} & \left\|\boldsymbol{y}-B\left(\gamma^{\mathrm{u}}+\gamma^{\mathrm{d}}\right)\right\|^{2} \\
\text { s.t. } & \gamma_{1}^{\mathrm{u}} \leq \gamma_{2}^{\mathrm{u}} \leq \cdots \leq \gamma_{J}^{\mathrm{u}} ; \gamma_{1}^{\mathrm{d}} \geq \gamma_{2}^{\mathrm{d}} \geq \cdots \geq \gamma_{J}^{\mathrm{d}} \\
& \left\|B\left(\gamma^{\mathrm{u}}-\gamma^{\mathrm{d}}\right)\right\|^{2} \leq s
\end{aligned}
$$

Defining $\Upsilon \triangleq\left\{\gamma=\left(\gamma^{\mathrm{u}}, \gamma^{\mathrm{d}}\right) \in \mathbb{R}^{2 J}: \gamma_{1}^{\mathrm{u}} \leq \gamma_{2}^{\mathrm{u}} \leq \cdots \leq \gamma_{J}^{\mathrm{u}} ; \gamma_{1}^{\mathrm{d}} \geq \gamma_{2}^{\mathrm{d}} \geq \cdots \geq \gamma_{J}^{\mathrm{d}}\right\}$ and

$$
Z \triangleq\binom{B}{B}, \quad W \triangleq\left[\begin{array}{cc}
B^{\mathrm{T}} & -B^{\mathrm{T}}
\end{array}\right]\binom{B}{-B}
$$

we further rewrite problem (6) as

$$
\begin{aligned}
\min _{\gamma \in \Upsilon} & \|\boldsymbol{y}-Z \gamma\|_{2}^{2} \\
\text { s.t. } & \gamma^{\mathrm{T}} W \gamma \leq s^{2}
\end{aligned}
$$

It is more convenient to consider its Lagrangian form

$$
\min _{\gamma \in \Upsilon}\left[\|\boldsymbol{y}-Z \gamma\|_{2}^{2}+\mu\left(\gamma^{\mathrm{T}} W \gamma-s^{2}\right)\right]=\min _{\gamma \in \Upsilon}\|\boldsymbol{y}-Z \gamma\|_{2}^{2}+\mu \gamma^{\mathrm{T}} W \gamma
$$

where $\mu \geq 0$ is the Lagrange multiplier. By Lagrangian duality, there is a one-to-one correspondence between the constrained problem (7) and the Lagrangian form (8): for each value of $s$ in the range where the constraint $\gamma^{\mathrm{T}} W \gamma \leq s^{2}$ is active, there is a corresponding value of $\mu$ that yields the same solution from the Lagrangian form (8). Conversely, the solution $\hat{\gamma}_{\mu}$ to problem (8) solves the bound problem (7) with $s^{2}=\hat{\gamma}_{\mu}^{\mathrm{T}} W \hat{\gamma}_{\mu}$. Some basic properties of the solution to problem (8) are summarized in Proposition 2.
Proposition 2. Let $\hat{\gamma}=\left(\hat{\gamma}^{\mathrm{u}}, \hat{\gamma}^{\mathrm{d}}\right)$ be the monotone decomposition to problem (8) (or problem (13) discussed later).
(i) There must be ties in the solution $\hat{\gamma}^{\mathrm{u}}$ or $\hat{\gamma}^{\mathrm{d}}$, i.e., there exists $i$ or $j$ such that $\hat{\gamma}_{i}^{\mathrm{u}}=\hat{\gamma}_{i+1}^{\mathrm{u}}$ or $\hat{\gamma}_{j}^{\mathrm{d}}=\hat{\gamma}_{j+1}^{\mathrm{d}}$.
(ii) The mean values of two monotone components are equal, $\mathbf{1}^{\mathrm{T}} B \hat{\gamma}^{\mathrm{u}}=\mathbf{1}^{\mathrm{T}} B \hat{\gamma}^{\mathrm{d}}$.




---

# 2.3 Monotone Functions 

To delve deeper into the properties of the solution to problem (8), this section discusses the monotone decomposition of monotone functions. Without loss of generality, we consider increasing functions.

Proposition 3. Let $\hat{\gamma}=\left(\hat{\gamma}^{u}, \hat{\gamma}^{d}\right)$ be the monotone decomposition to problem (8). Suppose $\hat{\gamma}^{u}+\hat{\gamma}^{d}$ is increasing, then
(i) $\hat{\gamma}^{d}$ is a vector with identical elements, i.e., $\hat{\gamma}^{d}=c \mathbf{1}$, where the constant $c=\frac{\mathbf{1}^{T} B \hat{\gamma}^{u}}{n}$;
(ii) if there is no ties in $\hat{\gamma}^{u}$, i.e., $\hat{\gamma}_{1}^{u}<\hat{\gamma}_{2}^{u}<\ldots<\hat{\gamma}_{J}^{u}$, then

$$
\hat{\gamma}^{u}=\frac{1}{\mu+1} \hat{\gamma}^{\mathrm{ls}}+\frac{\mu-1}{\mu+1} c \mathbf{1}
$$

where the unconstrained $B$-spline solution $\hat{\gamma}^{\mathrm{ls}}$ is given in Equation (3);
(iii) if $\hat{\gamma}_{1}^{u}<\cdots<\hat{\gamma}_{k_{1}}^{u}=\cdots=\hat{\gamma}_{k_{2}}^{u}<\cdots<\hat{\gamma}_{k_{2 m-1}}^{u}=\cdots=\hat{\gamma}_{k_{2 m}}^{u}<\cdots<\hat{\gamma}_{J}^{u}$, where $1 \leq k_{1} \leq k_{2} \leq$ $\cdots \leq k_{2 m-1} \leq k_{2 m} \leq J$, then

$$
\hat{\gamma}^{u}=\frac{1}{\mu+1} G^{T}\left(G^{T} B G^{T}\right)^{-1} G^{T} y+\frac{\mu-1}{\mu+1} c \mathbf{1}
$$

where $G$ is a block diagonal matrix with elements

$$
\left\{I_{k_{1}-1}, \mathbf{1}_{k_{2}-k_{1}+1}^{T}, \ldots, I_{k_{2 m-1}-k_{2 m-2}-1}, \mathbf{1}_{k_{2 m}-k_{2 m-1}+1}^{T}, I_{J-k_{2 m}}\right\}
$$

The above result (ii) can be viewed as a special case when $k_{1}=k_{2}=J$.
Intuitively, solution (9) can be viewed as a shrinkage with offset applied to the unconstrained $B$-spline fitting $\hat{\gamma}^{\mathrm{ls}}$, where $\frac{1}{\mu+1}$ is the shrinkage factor, and $\frac{\mu-1}{\mu+1} c \mathbf{1}$ is the offset. Even with the general matrix $G$, solution (10) also exhibits a similar shrinkage with offset pattern.

### 2.4 MSE Comparisons

To quantify the performance of fitting by monotone decomposition, consider the model

$$
y=f(x)+\varepsilon, \quad \varepsilon \sim N\left(0, \sigma^{2}\right)
$$

Define the mean squared error of the fitness,

$$
\operatorname{MSE}(\hat{y})=E\left\|f-B\left(\hat{\gamma}^{u}+\hat{\gamma}^{d}\right)\right\|_{2}^{2}, \quad \operatorname{MSE}\left(\hat{y}^{\mathrm{ls}}\right)=E\left\|f-B \hat{\gamma}^{\mathrm{ls}}\right\|_{2}^{2}
$$

where $f=\left[f\left(x_{1}\right), \ldots, f\left(x_{n}\right)\right]^{T}$, and the expectations are taken over $y \sim N\left(f, \sigma^{2} I\right)$. Proposition 4 shows that the fitting with monotone decomposition can achieve better performance, particularly in high-noise scenarios, when the underlying function is monotone.

Proposition 4. Suppose the monotone decomposition $\hat{\gamma}=\left(\hat{\gamma}^{u}, \hat{\gamma}^{d}\right)$ satisfies that $\hat{\gamma}^{u}+\hat{\gamma}^{d}$ is increasing. Let $G$ be a $g \times J$ matrix defined in Proposition 3 such that $G^{T} \hat{\gamma}^{u}$ is the sub-vector with unique elements. If






---

where

$$
\begin{aligned}
C_{1} & =\boldsymbol{f}^{T} \boldsymbol{A} \boldsymbol{f}-\frac{\left(\mathbf{1}_{n}^{T} \boldsymbol{f}\right)^{2}}{n} \geq 0, \quad C_{2}=\boldsymbol{f}^{T}(\boldsymbol{I}-\boldsymbol{A}) \boldsymbol{f} \geq 0 \\
\boldsymbol{A} & =\mathbb{E}\left[\boldsymbol{B} \boldsymbol{G}^{T}\left(\boldsymbol{G}^{T} \boldsymbol{B} \boldsymbol{G}^{T}\right)^{-1} \boldsymbol{G}^{T}\right] \\
\Delta & =\left[C_{1}(\boldsymbol{J}-\mathbb{E} \boldsymbol{g})+C_{2}(\mathbb{E} \boldsymbol{g}+\mathbf{1})\right]^{2}+4 C_{1} C_{2}(\mathbb{E} \boldsymbol{g}-\mathbf{1})^{2}
\end{aligned}
$$

and the expectations are taken over $\boldsymbol{y}$ since $\boldsymbol{G}$ (and hence $\boldsymbol{g}$ ) depends on $\boldsymbol{y}$, then there exists monotone decomposition such that $\operatorname{MSE}(\hat{\boldsymbol{y}})<\operatorname{MSE}\left(\hat{\boldsymbol{y}}_{\mathrm{ls}}\right)$.

Particularly, if we assume there is no ties in $\hat{\boldsymbol{\gamma}}_{\mathrm{u}}$, i.e., $\boldsymbol{G} \equiv \boldsymbol{I}$ for different $\boldsymbol{y}$, then there always exists a monotone decomposition such that $\operatorname{MSE}(\hat{\boldsymbol{y}})<\operatorname{MSE}\left(\hat{\boldsymbol{y}}_{\mathrm{ls}}\right)$ regardless of the noise level.

The lower bound of $\sigma^{2}$ in Proposition 4 might not be easy to evaluate. Nonetheless, the pivotal implication is that the monotone decomposition fitting can achieve better performance when the noise level is large enough. Extensive simulations in Section 4 agree with this argument. Moreover, although Proposition 4 is specifically established for monotone functions, the simulations show that the monotone decomposition fitting with cubic splines can also outperform the corresponding unconstrained cubic splines applied to random functions, particularly in high-noise scenarios.

# 3 Monotone Decomposition with Smoothing Splines 

When dealing with cubic splines, it is typically necessary to ascertain both the number of basis functions, denoted as $J$, and the optimal placement of knots. In contrast, smoothing splines take a different approach by employing all unique data points as knots, thus bypassing the need for an optimization process to determine the knot placement and the number of knots required for B-spline basis functions.

With B-spline basis functions, the smoothing spline $f(x)=\sum_{j=1}^{J} \gamma_{j} B_{j}(x)$ can be estimated as follows,

$$
\hat{\boldsymbol{\gamma}}_{\mathrm{ss}}=\arg \min \|\boldsymbol{y}-\boldsymbol{B} \boldsymbol{\gamma}\|_{2}^{2}+\lambda \boldsymbol{\gamma}^{T} \boldsymbol{\Omega} \boldsymbol{\gamma}
$$

where $\{\boldsymbol{\Omega}\}_{j k}=\int B_{j}^{\prime \prime}(s) B_{k}^{\prime \prime}(s) d s$ is called the roughness penalty matrix and $\lambda>0$ is the penalty parameter. For this reason, smoothing splines are also referred to as penalized splines.

Imposing the roughness penalty $\boldsymbol{\gamma}^{T} \boldsymbol{\Omega} \boldsymbol{\gamma}=\left(\boldsymbol{\gamma}_{\mathrm{u}}+\boldsymbol{\gamma}_{\mathrm{d}}\right)^{T} \boldsymbol{\Omega}\left(\boldsymbol{\gamma}_{\mathrm{u}}+\boldsymbol{\gamma}_{\mathrm{d}}\right)=\boldsymbol{\gamma}^{T} \boldsymbol{\Sigma} \boldsymbol{\gamma}$ on problem (8), where $\boldsymbol{\Sigma} \triangleq\left[\begin{array}{ll}\boldsymbol{\Omega} & \boldsymbol{\Omega} \\ \boldsymbol{\Omega} & \boldsymbol{\Omega}\end{array}\right]$, we have the Lagrangian form of monotone decomposition with smoothing splines,

$$
\min _{\gamma \in \Upsilon}\|\boldsymbol{y}-\boldsymbol{Z} \boldsymbol{\gamma}\|_{2}^{2}+\mu \boldsymbol{\gamma}^{T} \boldsymbol{W} \boldsymbol{\gamma}+\lambda \boldsymbol{\gamma}^{T} \boldsymbol{\Sigma} \boldsymbol{\gamma}
$$

For general functions, the properties in Proposition 2 also hold for the monotone decomposition with smoothing splines.

### 3.1 Monotone Functions

Likewise, we delve deeper into the characteristics of monotone decomposition with smoothing splines on monotone functions. The solutions demonstrate analogous shrinkage with offset patterns, akin to those observed in Proposition 3 for monotone decomposition with cubic splines, and the results are articulated in the following Proposition 5.

Proposition 5. Let $\hat{\boldsymbol{\gamma}}=\left(\hat{\boldsymbol{\gamma}}_{\mathrm{u}}, \hat{\boldsymbol{\gamma}}_{\mathrm{d}}\right)$ be the monotone decomposition to problem (13). Suppose $\hat{\boldsymbol{\gamma}}_{\mathrm{u}}+\hat{\boldsymbol{\gamma}}_{\mathrm{d}}$ is increasing, then




---

(i) $\hat{\gamma}_{d}$ is a vector with identical elements, i.e., $\hat{\gamma}_{d}=c \mathbf{1}$, where the constant $c=\frac{\mathbf{1}^{T} \boldsymbol{B} \hat{\gamma}_{u}}{n}$;
(ii) if there is no ties in $\hat{\gamma}_{u}$, i.e., the inequalities hold strictly, $\hat{\gamma}_{1}^{u}<\hat{\gamma}_{2}^{u}<\ldots<\hat{\gamma}_{J}^{u}$, then

$$
\hat{\gamma}_{u}=\frac{1}{1+\mu} \hat{\gamma}_{s s}\left(\frac{\lambda}{1+\mu}\right)-c\left((1+\mu) \boldsymbol{B}^{T} \boldsymbol{B}+\lambda \boldsymbol{\Omega}\right)^{-1}\left((1-\mu) \boldsymbol{B}^{T} \boldsymbol{B}+\lambda \boldsymbol{\Omega}\right) \mathbf{1}_{J}
$$

where $\hat{\gamma}_{s s}\left(\frac{\lambda}{1+\mu}\right)$ is the solution to smoothing spline with penalty parameter $\frac{\lambda}{1+\mu}$,

$$
\hat{\gamma}_{s s}\left(\frac{\lambda}{1+\mu}\right)=\left(\boldsymbol{B}^{T} \boldsymbol{B}+\frac{\lambda}{1+\mu} \boldsymbol{\Omega}\right)^{-1} \boldsymbol{B}^{T} \boldsymbol{y}
$$

(iii) if $\hat{\gamma}_{1}^{u}<\cdots<\hat{\gamma}_{k_{1}}^{u}=\cdots=\hat{\gamma}_{k_{2}}^{u}<\cdots<\hat{\gamma}_{k_{2 m}-1}^{u}=\cdots=\hat{\gamma}_{k_{2 m}}^{u}<\hat{\gamma}_{J}^{u}$, where $1 \leq k_{1} \leq k_{2} \leq \cdots \leq$ $k_{2 m-1} \leq k_{2 m} \leq J$, then

$$
\begin{aligned}
\hat{\gamma}_{u}= & \boldsymbol{G}^{T}\left((1+\mu) \boldsymbol{G} \boldsymbol{B}^{T} \boldsymbol{B} \boldsymbol{G}+\lambda \boldsymbol{G} \boldsymbol{\Omega} \boldsymbol{G}^{T}\right)^{-1} \boldsymbol{G} \boldsymbol{B}^{T} \boldsymbol{y}- \\
& c \boldsymbol{G}^{T}\left((1+\mu) \boldsymbol{G} \boldsymbol{B}^{T} \boldsymbol{B} \boldsymbol{G}+\lambda \boldsymbol{G} \boldsymbol{\Omega} \boldsymbol{G}^{T}\right)^{-1}\left((1-\mu) \boldsymbol{G} \boldsymbol{B}^{T} \boldsymbol{B} \boldsymbol{G}+\lambda \boldsymbol{G} \boldsymbol{\Omega} \boldsymbol{G}^{T}\right) \mathbf{1}_{g},
\end{aligned}
$$

where $\boldsymbol{G}$ is defined in Proposition 3. The above result (ii) can be viewed as a special case when $k_{1}=k_{2}=J$.

For the no-tie solution (14), the shrinkage is on the ridge solution $\hat{\gamma}_{s s}\left(\frac{\lambda}{1+\mu}\right)$, but different from the constant offset in Equation (9), the offset $c\left((1+\mu) \boldsymbol{B}^{T} \boldsymbol{B}+\lambda \boldsymbol{\Omega}\right)^{-1}\left((1-\mu) \boldsymbol{B}^{T} \boldsymbol{B}+\lambda \boldsymbol{\Omega}\right) \mathbf{1}_{J}$ depends on $\boldsymbol{B}$ and $\boldsymbol{\Omega}$.

# 3.2 MSE Comparisons 

Based on model (11), for a comparative analysis of the fitting performance between monotone decomposition with smoothing splines and their smoothing splines counterparts, we further define the mean squared error for smoothing splines,

$$
\operatorname{MSE}\left(\hat{y}_{s s}(\lambda)\right)=\mathbb{E}\left\|\boldsymbol{f}-\boldsymbol{B} \hat{\gamma}_{s s}(\lambda)\right\|_{2}^{2}
$$

where $\hat{\boldsymbol{\gamma}}_{s s}(\lambda)$ is the solution to smoothing splines with penalty parameter $\lambda$.
Proposition 6 shows that employing monotone decomposition with smoothing splines can result in a superior mean squared error (MSE) compared to smoothing splines in the context of monotone functions, particularly when the noise level is sufficiently high. While the condition (15) outlined in Proposition 6 may appear intricate, the simulations presented in the next section empirically substantiate this assertion. Furthermore, although the proposition is specifically formulated for monotone functions, the simulations show that the monotone decomposition applied to general functions can still achieve better performance in high-noise scenarios.
Proposition 6. Consider the smoothing spline with penalty parameter $\lambda_{0}$. Let $\hat{\boldsymbol{\gamma}}_{s s}\left(\lambda_{0}\right)$ be the coefficient vector and denote its hat matrix by $\boldsymbol{Q}=\boldsymbol{B}\left(\boldsymbol{B}^{T} \boldsymbol{B}+\lambda_{0} \boldsymbol{\Omega}\right)^{-1} \boldsymbol{B}^{T}$. If

$$
\sigma^{2}>\frac{\boldsymbol{f}^{T} \boldsymbol{Q}\left(\boldsymbol{I}-\frac{1}{n} \mathbf{1}_{n} \mathbf{1}_{n}^{T} \boldsymbol{Q}\right)(\boldsymbol{I}-\boldsymbol{Q}) \boldsymbol{f}}{\operatorname{tr}\left[\left(\boldsymbol{I}-\frac{1}{n} \mathbf{1}_{n} \mathbf{1}_{n}^{T} \boldsymbol{Q}\right) \boldsymbol{Q}^{2}\right]}
$$

and suppose the monotone decomposition $\hat{\gamma}_{u}+\hat{\gamma}_{d}$ is increasing with no ties, then there exists a monotone decomposition with parameters $\lambda=\lambda_{0} / k, \mu=1 / k-1$, where $k \in(0,1)$, that achieves smaller mean squared error than $\operatorname{MSE}\left(\hat{y}_{s s}\left(\lambda_{0}\right)\right)$.




---

# 4 Simulations for Fitting 

In this section, we compare the performance of monotone decomposition using simulated examples. We generate data from function $f$ with standard Gaussian noises,

$$
y=f(x)+N\left(0, \sigma^{2}\right), x \in[-1,1]
$$

To cover a diverse range of functional forms, we consider the following different types of functions.

- monotone functions: (i) polynomial function: $y=x^{3}$; (ii) exponential function: $y=\exp (x)$; (iii) sigmoid function: $y=\frac{1}{1+\exp (-5 x)}$.
- general functions: (i) unimodal: $y=x^{2}$; (ii) random functions, where the kernel can be Squared Exponential (SE), Rational Quadratic (RQ), Matérn (Mat) and Periodic (Rasmussen \& Williams, 2006). The numerical values appended to the kernel names in Tables 6 and 8 are the kernel parameters. For example, "Mat12" refers to the Matérn kernel with parameter $\nu=1 / 2$. The detailed procedure for generating a random function and a visualization of those curves can be found in the Supplementary Material.

To compare the performance of different methods, we adopt the mean squared fitting error (MSFE), i.e., the residual sum of squares (RSS) divided by sample size, and the mean squared prediction error (MSPE),

$$
\operatorname{MSFE}=\frac{1}{n} \sum_{i=1}^{n}\left(y_{i}-\hat{f}\left(x_{i}\right)\right)^{2}, \quad \operatorname{MSPE}=\frac{1}{N} \sum_{i=1}^{N}\left(\hat{f}\left(t_{i}\right)-f\left(t_{i}\right)\right)^{2}
$$

where $t_{i}=x_{(1)}+(i-1) \cdot \frac{x_{(N)}-x_{(1)}}{N}, i=1, \ldots, N$ are equally spaced within the same range of $x$. Based on $R=100$ replications, we estimate the mean MSFE and MSPE, together with their respective standard errors. To judge how significant the differences of MSPE between the fitting by monotone decomposition and the corresponding spline fitting, we consider

$$
\Delta=\operatorname{MSPE}(\text { Monotone decomposition })-\operatorname{MSPE}(\text { Spline fitting })
$$

and denote the differences for each experiment as $\delta_{i}, i=1, \ldots, R$. We report the $p$-value for the one-sided $t$-test $H_{0}: \Delta=0$ versus $H_{1}^{<}: \Delta<0$ when $\sum_{i=1}^{n} \delta_{i}<0$ (or $H_{1}^{>}: \Delta>0$ when $\left.\sum_{i=1}^{n} \delta_{i}>0\right)$. Besides, we also count the proportion for the fitting by monotone decomposition that achieves better performance, prop $\triangleq \frac{\sum_{i=1}^{R} \#\left\{\delta_{i}<0\right\}}{R}$.

### 4.1 Cubic Splines

Firstly, we consider the monotone decomposition with cubic splines. There are two tuning parameters: the number of basis functions $J$, and the Lagrange multiplier $\mu$ for the discrepancy between the two components. We adopt two strategies to optimize these parameters:

Tune $\mu$ with fixed $J$ : We pick $J$, the tuning parameter for cubic splines, to be a minimizer of the cross-validation (CV) error, and then perform the monotone decomposition with cubic splines using the same $J$ while tuning the parameter $\mu$. Figure 1 shows an example, with $J=26$ selected by CV. The left panel shows the leave-one-out CV error plotted against $\mu$. The cubic spline fitting and the monotone decomposition fitting are displayed in the right panel, where the former achieves 0.102 MSPE, while the latter improves the MSPE to 0.066 .




---



Figure 1: Demo for monotone decomposition with cubic splines. The left panel shows the leaveone-out cross-validation error curve for each candidate $\mu$ when $J$ is CV-tuned for the cubic spline. The right panel shows the corresponding fitting curves, together with the truth and the noised observations. The values in the parentheses are the mean squared prediction error.

Tune $\mu$ and $J$ simultaneously: Instead of fixing $J$ in the monotone decomposition procedure, we also use cross-validation to choose it, together with $\mu$. Figure 2 displays an example of this process, where the left panel shows the CV error for each parameter pair $(\mu, J)$, and the right panel compares the fitting given the parameters that minimize the CV error to cubic spline fitting, whose parameter $J$ is separately tuned by CV.



Figure 2: Demo for monotone decomposition with cubic splines. The left panel shows the leaveone-out cross-validation error curve for each candidate pair $(\mu, J)$. The right panel shows the corresponding fitting curves, together with the truth and noised observations. The values in the parentheses are the mean squared prediction error.

Note that the right panels of Figures 1 and 2 depict the same training data. Although the MSPE of 0.079 by tuning $(\mu, J)$ simultaneously is slightly larger than the MSPE of 0.066 by tuning $\mu$ with fixed $J$, the monotone decomposition method achieves better performance than the cubic spline fitting, which has an MSPE of 0.102 .

To provide comprehensive comparisons, we conducted 100 repetitions for 12 types of curves under different noise levels. The results by tuning $\mu$ and $J$ simultaneously are summarized in Table 6, and the results by tuning $\mu$ with fixed $J$ can be found in the Supplementary Material. For some curves with small noises (e.g., $\sigma=0.2$ ), such as $y=x^{3}$, the decomposition method




---

performs slightly worse than cubic spline fitting. Nevertheless, the monotone decomposition always outperforms cubic spline fitting in higher noise (e.g., $\sigma=1.0$ ) scenarios, regardless of the optimization strategies.

Table 1: Results for comparing the cubic splines and the fitting by monotone decomposition with CV-tuned $(\mu, J)$. The values are averages over 100 replications, with the standard error of the average in parentheses. The bold values highlight the smaller mean squared prediction error. The complete table with finer noise levels can be found in the Supplementary Material.

| curve | $\sigma$ | MSFE |  | MSPE |  | p-value | prop. |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|  |  | CubicSpline | MonoDecomp | CubicSpline | MonoDecomp |  |  |
| $x^{2}$ | 1.0 | $9.71 \mathrm{e}+00(7.3 \mathrm{e}-02)$ | $9.73 \mathrm{e}+00(7.3 \mathrm{e}-02)$ | $7.50 \mathrm{e}+00(3.1 \mathrm{e}-01)$ | $\mathbf{6 . 9 3 e}+00(2.6 \mathrm{e}-01)$ | $5.91 \mathrm{e}-03$ (**) | 0.59 |
| $x^{3}$ | 1.0 | $9.65 \mathrm{e}+00(7.4 \mathrm{e}-02)$ | $9.60 \mathrm{e}+00(7.2 \mathrm{e}-02)$ | $7.63 \mathrm{e}+00(3.5 \mathrm{e}-01)$ | $\mathbf{7 . 1 7} \mathrm{e}+00(2.7 \mathrm{e}-01)$ | 2.21e-02 (*) | 0.6 |
| $\exp (x)$ | 1.0 | 9.57e+00 (5.9e-02) | 9.49e+00 (7.3e-02) | $7.56 \mathrm{e}+00(2.8 \mathrm{e}-01)$ | $7.08 \mathrm{e}+00(3.1 \mathrm{e}-01)$ | $3.59 \mathrm{e}-02$ (*) | 0.57 |
| sigmoid | 1.0 | $9.51 \mathrm{e}+00(8.5 \mathrm{e}-02)$ | $9.50 \mathrm{e}+00(8.7 \mathrm{e}-02)$ | $7.33 \mathrm{e}+00(3.2 \mathrm{e}-01)$ | $\mathbf{6 . 6 1} \mathrm{e}+00(2.6 \mathrm{e}-01)$ | 1.45e-03 (**) | 0.56 |
| SE-1 | 1.0 | $9.55 \mathrm{e}+00(7.0 \mathrm{e}-02)$ | $9.51 \mathrm{e}+00(7.6 \mathrm{e}-02)$ | $7.29 \mathrm{e}+00(3.2 \mathrm{e}-01)$ | $\mathbf{6 . 6 2} \mathrm{e}+00(2.7 \mathrm{e}-01)$ | $5.51 \mathrm{e}-03$ (**) | 0.63 |
| SE-0.1 | 1.0 | $9.29 \mathrm{e}+00(8.5 \mathrm{e}-02)$ | 9.20e+00 (9.3e-02) | $1.44 \mathrm{e}+01(2.6 \mathrm{e}-01)$ | 1.38e+01 (2.4e-01) | $5.93 \mathrm{e}-04$ (***) | 0.7 |
| Mat12-1 | 1.0 | $9.79 \mathrm{e}+00(8.9 \mathrm{e}-02)$ | $9.73 \mathrm{e}+00(9.1 \mathrm{e}-02)$ | $1.26 \mathrm{e}+01(2.9 \mathrm{e}-01)$ | 1.17e+01 (2.4e-01) | 9.31e-07 (***) | 0.68 |
| Mat12-0.1 | 1.0 | $1.04 \mathrm{e}+01(1.3 \mathrm{e}-01)$ | $1.04 \mathrm{e}+01(1.3 \mathrm{e}-01)$ | $2.07 \mathrm{e}+01(2.4 \mathrm{e}-01)$ | $2.01 \mathrm{e}+01(2.4 \mathrm{e}-01)$ | 1.85e-04 (***) | 0.73 |
| Mat32-1 | 1.0 | $9.62 \mathrm{e}+00(8.2 \mathrm{e}-02)$ | $9.61 \mathrm{e}+00(8.3 \mathrm{e}-02)$ | $9.01 \mathrm{e}+00(3.5 \mathrm{e}-01)$ | $\mathbf{8 . 0 0} \mathrm{e}+00(2.6 \mathrm{e}-01)$ | $1.46 \mathrm{e}-04$ (***) | 0.56 |
| Mat32-0.1 | 1.0 | $9.62 \mathrm{e}+00(1.1 \mathrm{e}-01)$ | 9.53e+00 (9.7e-02) | $1.68 \mathrm{e}+01(2.5 \mathrm{e}-01)$ | $1.58 \mathrm{e}+01(2.1 \mathrm{e}-01)$ | 4.67e-10 (***) | 0.72 |
| RQ-0.1-0.5 | 1.0 | $9.55 \mathrm{e}+00(1.1 \mathrm{e}-01)$ | 9.50e+00 (1.2e-01) | $1.50 \mathrm{e}+01(2.4 \mathrm{e}-01)$ | 1.44e+01 (2.6e-01) | $5.01 \mathrm{e}-03$ (**) | 0.68 |
| Periodic-0.1-4 | 1.0 | $9.41 \mathrm{e}+00(1.2 \mathrm{e}-01)$ | $9.31 \mathrm{e}+00(1.1 \mathrm{e}-01)$ | $1.72 \mathrm{e}+01(3.0 \mathrm{e}-01)$ | $1.60 \mathrm{e}+01(2.5 \mathrm{e}-01)$ | 2.03e-10 (***) | 0.63 |

# 4.2 Smoothing Splines 

This section compares the fitting performance of monotone decomposition with smoothing splines to the fitting of the smoothing splines. There are two tuning parameters: the penalty parameter $\lambda$ and the Lagrange multiplier $\mu$ for the discrepancy. We consider three strategies to optimize these parameters:

- Tune $\lambda$ for smoothing splines first, then tune $\mu$ for the monotone decomposition with smoothing splines using the tuned $\lambda$;
- According to Proposition 6, tune $\lambda$ for smoothing splines first, then tune the shrinkage factor $k=\frac{1}{1+\mu}$ for monotone decomposition with smoothing splines using penalty parameter $\lambda / k$
- Simultaneously tune $\lambda$ and $\mu$ for monotone decomposition with smoothing splines.

All strategies use cross-validation (CV) to determine the parameters. Specifically, we pick the tuning parameters that minimize the CV error.

For brevity, we only present the results using the third strategy in this section. Results based on the other two strategies can be found in the Supplementary Material. Figure 3 illustrates the simultaneous tuning of $(\mu


---



Figure 3: Demo for monotone decomposition with smoothing splines. The left panel shows the leave-one-out cross-validation error heatmap for each candidate pair $(\mu, \lambda)$. The right panel shows the corresponding fitting curves, together with the truth and the noised observations. The values in the parentheses are the mean squared prediction errors.
compared to the other two strategies. Regardless of the optimization strategies employed, all results consistently show that the monotone decomposition fitting can achieve a good performance, especially in high-noise scenarios.

Table 2: Results for comparing the smoothing splines with CV-tuned $\lambda$ and the fitting by monotone decomposition with CV-tuned $(\lambda, \mu)$. The values are averages over 100 replications, with the standard error of the average in parentheses. The bold values highlight the smaller mean squared prediction error. The complete table with finer noise levels can be found in the Supplementary Material.

| curve | $\sigma$ | MSFE |  | MSPE |  | $p$-value | prop. |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|  |  | SmoothSpline | MonoDecomp | SmoothSpline | MonoDecomp |  |  |
| $x^{2}$ | 1.0 | $9.65 \mathrm{e}+00(8.9 \mathrm{e}-02)$ | $9.69 \mathrm{e}+00(8.5 \mathrm{e}-02)$ | $6.44 \mathrm{e}+00(2.9 \mathrm{e}-01)$ | $6.35 \mathrm{e}+00(2.5 \mathrm{e}-01)$ | $1.68 e-01$ | 0.49 |
| $x^{3}$ | 1.0 | $9.75 \mathrm{e}+00(8.2 \mathrm{e}-02)$ | $9.77 \mathrm{e}+00(8.2 \mathrm{e}-02)$ | $6.47 \mathrm{e}+00(1.8 \mathrm{e}-01)$ | $6.21 \mathrm{e}+00(1.7 \mathrm{e}-01)$ | $1.18 \mathrm{e}-04(* * *)$ | 0.65 |
| $\exp (x)$ | 1.0 | $9.74 \mathrm{e}+00(8.4 \mathrm{e}-02)$ | $9.75 \mathrm{e}+00(8.4 \mathrm{e}-02)$ | $5.94 \mathrm{e}+00(2.3 \mathrm{e}-01)$ | $5.82 \mathrm{e}+00(2.1 \mathrm{e}-01)$ | $3.12 \mathrm{e}-02(*)$ | 0.58 |
| sigmoid | 1.0 | $9.60 \mathrm{e}+00(7.8 \mathrm{e}-02)$ | $9.64 \mathrm{e}+00(7.5 \mathrm{e}-02)$ | $5.99 \mathrm{e}+00(2.9 \mathrm{e}-01)$ | $5.68 \mathrm{e}+00(2.4 \mathrm{e}-01)$ | $4.47 \mathrm{e}-04(* * *)$ | 0.67 |
| SE-1 | 1.0 | $9.67 \mathrm{e}+00(8.3 \mathrm{e}-02)$ | $9.70 \mathrm{e}+00(8.1 \mathrm{e}-02)$ | $6.32 \mathrm{e}+00(2.8 \mathrm{e}-01)$ | $6.11 \mathrm{e}+00(2.5 \mathrm{e}-01)$ | $3.86 \mathrm{e}-03(* *)$ | 0.6 |
| SE-0.1 | 1.0 | $8.92 \mathrm{e}+00(9.2 \mathrm{e}-02)$ | $8.99 \mathrm{e}+00(9.0 \mathrm{e}-02)$ | $1.23 \mathrm{e}+01(2.1 \mathrm{e}-01)$ | $1.23 \mathrm{e}+01(2.1 \mathrm{e}-01)$ | $4.32 \mathrm{e}-01$ | 0.57 |
| Mat12-1 | 1.0 | $9.65 \mathrm{e}+00(9.5 \mathrm{e}-02)$ | $9.69 \mathrm{e}+00(9.2 \mathrm{e}-02)$ | $1.15 \mathrm{e}+01(2.3 \mathrm{e}-01)$ | $1.13 \mathrm{e}+01(2.1 \mathrm{e}-01)$ | $3.40 \mathrm{e}-04(* * *)$ | 0.56 |
| Mat12-0.1 | 1.0 | $9.76 \mathrm{e}+00(1.2 \mathrm{e}-01)$ | $9.92 \mathrm{e}+00(1.1 \mathrm{e}-01)$ | $1.90 \mathrm{e}+01(2.2 \mathrm{e}-01)$ | $1.90 \mathrm{e}+01(2.2 \mathrm{e}-01)$ | $2.06 \mathrm{e}-01$ | 0.58 |
| Mat32-1 | 1.0 | $9.59 \mathrm{e}+00(8.5 \mathrm{e}-02)$ | $9.64 \mathrm{e}+00(7.5 \mathrm{e}-02)$ | 7.20 e+00(2.4e-01) | $7.04 \mathrm{e}+00(2.0 \mathrm{e}-01)$ | $3.65 \mathrm{e}-02(*)$ | 0.49 |
| Mat32-0.1 | 1.0 | $8.96 \mathrm{e}+00(1.1 \mathrm{e}-01)$ | $9.14 \mathrm{e}+00(1.0 \mathrm{e}-01)$ | $1.48 \mathrm{e}+01(2.2 \mathrm{e}-01)$ | $1.47 \mathrm{e}+01(2.1 \mathrm{e}-01)$ | $1.44 \mathrm{e}-01$ | 0.54 |
| RQ-0.1-0.5 | 1.0 | $9.10 \mathrm{e}+00(1.1 \mathrm{e}-01)$ | $9.22 \mathrm{e}+00(1.1 \mathrm{e}-01)$ | $1.27 \mathrm{e}+01(2.4 \mathrm{e}-01)$ | $1.25 \mathrm{e}+01(2.2 \mathrm{e}-01)$ | $1.21 \mathrm{e}-03(* *)$ | 0.6 |
| Periodic-0.1-4 | 1.0 | $8.69 \mathrm{e}+00(1.0 \mathrm{e}-01)$ | $8.89 \mathrm{e}+00(9.1 \mathrm{e}-02)$ | $1.44 \mathrm{e}+01(2.1 \mathrm{e}-01)$ | $1.43 \mathrm{e}+01(1.9 \mathrm{e}-01)$ | $3.03 \mathrm{e}-01$ | 0.49 |

# 5 Test of Monotonicity 

Once obtaining two monotone components through monotone decomposition, in addition to utilizing the sum of these two components as a fitting method, we can also derive statistics for




---

the monotonicity testing. Consider the model $Y=f(X)+\epsilon$, where $X$ is a scalar covariate, $Y$ is a scalar dependent random variable, $\epsilon$ is the noise satisfying $\mathbb{E}[\epsilon \mid X]=0$, and $f$ is an unknown function. Testing of monotonicity aims to test

$$
\begin{aligned}
& H_{0}: f \text { is monotone } \\
& H_{1}: f \text { is not monotone }
\end{aligned}
$$

where "monotone" can be specifically (strictly) "increasing" or "decreasing".

# 5.1 Related Work 

There are many existing approaches for testing monotonicity. Bowman et al. (1998) constructed a test based on critical bandwidth. They fitted a local linear regression and determined the smallest bandwidth value such that the estimate becomes monotone. This critical bandwidth is then used as a test statistic, and the $p$-value is calculated by the bootstrap method. Hall and Heckman (2000) pointed out the shortcoming of the test when the true function has flat and nearly flat spots, and they proposed a test that estimates local slopes and approximates the distribution of the weighted minimum. Ghosal et al. (2000) proposed test statistics that are functionals of a U-process, which is based on the signs of $\left(Y_{i+k}-Y_{i}\right)\left(X_{i+k}-X_{i}\right)$. They approximated the limiting distribution by Gaussian processes and then derived the critical values for an asymptotic significance level $\alpha$. Chetverikov (2019) used the similar U-statistics, but he introduced a weighting function $Q\left(X_{i}, X_{j}\right)$ and proposed a statistic based on $\left(Y_{i}-Y_{j}\right) \operatorname{sign}\left(X_{j}-X_{i}\right) Q\left(X_{i}, X_{j}\right)$, where $Q$ is chosen from a large set of potentially useful weighting functions to maximize the statistic. J. C. Wang and Meyer (2011) used quadratic regression splines to fit the data, took the minimum of the slopes at the knots as the test statistic, and then estimated the null distribution of such a statistic by performing constrained quadratic regression splines.

### 5.2 Test by Monotone Decomposition

Suppose we have obtained the monotone components. Propositions 3 and 5 imply that the coefficients for one component would be constant if the function is monotone. Thus, we can test the monotonicity of a function by testing whether the coefficients of monotone components are constant. The equivalences are summarized in Table 3.

Table 3: Equivalent hypotheses.

| Original Hypothesis | Hypothesis in terms of Monotone Decomposition |
| :---: | :---: |
| $H^{u}{ }_{0}: f$ is increasing | $H_{0}^{u}: \gamma^{d}=c \mathbf{1}$ |
| $H_{0}^{d}: f$ is decreasing | $H_{0}^{d}: \gamma^{u}=c \mathbf{1}$ |
| $H_{0}^{s u}: f$ is strictly increasing | $H_{0}^{s u}: \gamma^{d}=c \mathbf{1}, \gamma^{u} \neq c \mathbf{1}$ |
| $H_{0}^{s d}: f$ is strictly decreasing | $H_{0}^{s d}: \gamma^{u}=c \mathbf{1}, \gamma^{d} \neq c \mathbf{1}$ |
| $H_{0}^{m}: f$ is monotone | $H_{0}^{m}$ : one monotone component is constant, |
|  | i.e., $\min \left(\gamma^{u}, \gamma^{d}\right)=c \mathbf{1}$. |
| $H_{0}^{s m}: f$ is strictly monotone | $H_{0}^{s m}$ : one and only one monotone component is constant, |
|  | i.e., $\min \left(\gamma^{u}, \gamma^{d}\right)=c \mathbf{1}, \max \left(\gamma^{u}, \gamma^{d}\right) \neq c \mathbf{1}$. |

In Table 3, the minimum (maximum) of two vectors $\boldsymbol{a}, \boldsymbol{b} \in \mathbb{R}^{J}$ are defined as:

$$
\begin{aligned}
& \min (\boldsymbol{a}, \boldsymbol{b}) \triangleq \underset{\boldsymbol{x} \in\{\boldsymbol{a}, \boldsymbol{b}\}}{\arg \min } V(\boldsymbol{x}) \\
& \max (\boldsymbol{a}, \boldsymbol{b}) \triangleq \underset{\boldsymbol{x} \in\{\boldsymbol{a}, \boldsymbol{b}\}}{\arg \max } V(\boldsymbol{x})
\end{aligned}
$$




---

where $V$ is the sample variance on the elements of a vector. To test $H_{0}^{u}, H_{0}^{d}$ and $H_{0}^{m}$, consider the test statistics

$$
T^{u}=V\left(\hat{\gamma}^{d}\right), T^{d}=V\left(\hat{\gamma}^{u}\right), T^{m}=V\left(\min \left(\hat{\gamma}^{u}, \hat{\gamma}^{d}\right)\right)
$$

Note that the null hypothesis will be rejected if the test statistic $T$ is large enough. Specifically, given a significance level $\alpha$, the respective null hypothesis would be rejected if $T^{u} \geq t^{u, 1-\alpha}, T^{d} \geq t^{d, 1-\alpha}$ or $T^{m} \geq t^{m, 1-\alpha}$, where $t^{u, 1-\alpha}, t^{d, 1-\alpha}$ and $t^{m, 1-\alpha}$ denote the critical values of the distributions of $T^{u}, T^{d}, T^{m}$ under the respective null hypotheses, respectively. The distributions of $T^{u}, T^{d}, T^{m}$ under their null hypotheses can be characterized by the bootstrap samples. Note that the $\epsilon$ and $\hat{\epsilon}$ can be heterogeneous, so we take the wild bootstrap (Davidson \& Flachaire, 2008). Without loss of generality, we focus on the test of increasing functions, and the procedure for testing $H_{0}^{u}$ is outlined in Algorithm 1.

```
Algorithm 1 Test of Monotonicity (Increasing): $H_{0}^{u}$
Input: Significance level $\alpha$, number of bootstrap samples $R$.
    : Fit $\left\{x_{i}, y_{i}\right\}_{i=1}^{n}$ by monotone decomposition, either with cubic splines or smoothing splines.
    Denote the increasing component as $\hat{y}^{u}$, let $\hat{c}=\frac{1^{T} \hat{y}^{u}}{n}$, and denote the fitting method as $\hat{m}$.
    2: Calculate the test statistic $T$.
    3: Calculate the errors, $\epsilon_{i}=y_{i}-\hat{y}_{i}$.
    4: for $r$ from 1 to $R$ do
            Sample $\eta_{i} \sim N(0,1)$ and construct $\epsilon_{i}^{\star}=\eta_{i} \epsilon_{i}$. [Wild Bootstrap]
            Construct bootstrap samples $y_{i}^{\star}=\hat{y}_{i}^{u}+\hat{c}+\epsilon_{i}^{\star}, i=1, \ldots, n$.
            Apply $\hat{m}$ on $\left\{x_{i}, y_{i}^{\star}\right\}_{i=1}^{n}$, and calculate the bootstrap statistic $\delta_{r}$
    end for
    The critical value $t^{1-\alpha}$ is the $1-\alpha$ quantile of $\left\{\delta_{r}\right\}_{r=1}^{R}$, then reject the null hypothesis if
    $T>t^{1-\alpha}$
    Alternatively, construct p-value $\frac{1}{R} \sum_{r=1}^{R} \#\left\{\delta_{r}>T\right\}$, and reject if $p<\alpha$.
```


# 6 Simulations for Testing 

Firstly, we want to check whether the methods can control the Type I error. Specifically, consider five monotone functions, $x, x^{3}, x^{1 / 3}, e^{x}$ and $\frac{1}{1+e^{-x}}$. We conducted 100 simulations and calculated the proportion of rejecting the null hypothesis. Ideally, the rejection proportion should be less than 0.05 if we pick the commonly used significance level $\alpha=0.05$. The results are reported in Table 4 .

Ghosal et al. (2000) always accepts the null hypothesis. J. C. Wang and Meyer (2011) fails to control the Type I error when the noise level is small on curve $x^{3}$, and Bowman et al. (1998) cannot control the Type I error when the noise level is large on curve $x^{3}$. In contrast, our proposed methods, monotone decomposition with cubic splines (MDCS) and monotone decomposition with smoothing splines (MDSS), demonstrate strong Type I error control in the majority of cases, even though the rejection rates are slightly elevated in a few instances.

Furthermore, the $p$-value should follow Uniform $[0,1]$ under the null hypothesis. To check the distribution of $p$-value for each approach, Figure 4 displays the uniform QQ plots of 1000 p -values for $x^{3}$ and $e^{x}$ with sample size $n=200$ and noise level $\sigma=0.01$, respectively. The uniform QQ




---

Table 4: Simulated size (the proportion of rejecting the null hypothesis) of monotone curves under different noise levels and different sample sizes given the significance level $\alpha=0.05$.

| Methods | Curves | $\sigma=0.001$ |  |  | $\sigma=0.01$ |  |  | $\sigma=0.1$ |  |  |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|  |  | $n=50$ | 100 | 200 | $n=50$ | 100 | 200 | $n=50$ | 100 | 200 |
| J. C. Wang and Meyer (2011) | x | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.01 | 0.0 |
|  | $x^{3}$ | 0.53 | 0.84 | 1.0 | 0.05 | 0.08 | 0.08 | 0.02 | 0.06 | 0.04 |
|  | $x^{1 / 3}$ | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.03 | 0.02 | 0.01 |
|  | $e^{x}$ | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
|  | $1 /\left(1+e^{-x}\right)$ | 0.0 | 0.0 | 0.0 | 0.01 | 0.0 | 0.0 | 0.04 | 0.06 | 0.05 |
| Ghosal et al. (2000) | x | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
|  | $x^{3}$ | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
|  | $x^{1 / 3}$ | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
|  | $e^{x}$ | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
|  | $1 /\left(1+e^{-x}\right)$ | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Bowman et al. (1998) | x | 0.0 | 0.0 | 0.0 | 0.02 | 0.0 | 0.01 | 0.01 | 0.0 | 0.01 |
|  | $x^{3}$ | 0.0 | 0.0 | 0.0 | 0.2 | 0.19 | 0.18 | 0.26 | 0.2 | 0.15 |
|  | $x^{1 / 3}$ | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.05 | 0.02 | 0.01 |
|  | $e^{x}$ | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.04 | 0.02 | 0.0 |
|  | $1 /\left(1+e^{-x}\right)$ | 0.0 | 0.0 | 0.0 | 0.02 | 0.0 | 0.02 | 0.02 | 0.01 | 0.0 |
| MDCS | x | 0.01 | 0.0 | 0.12 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
|  | $x^{3}$ | 0.0 | 0.0 | 0.0 | 0.01 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
|  | $x^{1 / 3}$ | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
|  | $e^{x}$ | 0.02 | 0.11 | 0.03 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
|  | $1 /\left(1+e^{-x}\right)$ | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| MDSS | x | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
|  | $x^{3}$ | 0.1 | 0.08 | 0.08 | 0.08 | 0.1 | 0.07 | 0.09 | 0.05 | 0.03 |
|  | $x^{1 / 3}$ | 0.0 | 0.02 | 0.02 | 0.01 | 0.03 | 0.07 | 0.05 | 0.06 | 0.05 |
|  | $e^{x}$ | 0.04 | 0.05 | 0.02 | 0.08 | 0.07 | 0.05 | 0.04 | 0.08 | 0.08 |
|  | $1 /\left(1+e^{-x}\right)$ | 0.03 | 0.03 | 0.03 | 0.0 | 0.01 | 0.0 | 0.0 | 0.0 | 0.0 |


(a) $x^{3}$


(b) $e^{x}$

Figure 4: Uniform QQ plots of 1000 p -values for five approaches on two curves with $n=200, \sigma=$ 0.01 , respectively.

Next, we compare the simulated size and power under the settings of two competitors. The




---

Table 5: Simulated size and power on curves from Bowman et al. (1998) and Ghosal et al. (2000) based on 100 repetitive experiments.

| Methods <br> n=50 | Bowman et al. (1998) |  |  |  |  |  |  | Ghosal et al. (2000) |  |  |  |  |  |  |  |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 100 <br> 200 | Curves <br> $\sigma=0.00$ |  | ${ }_{a}$ |  | $\dot{\sigma}$ | 200 | 100 <br> 20 <br> $\infty$ | Curves <br> $\sigma=0.001$ |  |  |  |  |  |  |
|  |  | $\sigma=0.01$ |  |  | 0.1 |  |  |  | $\sigma=0.01$ |  |  | $\sigma=0.1$ |  |  |
| J.C. Wang and Meyer (2011) <br> $\mathrm{a}=0.00$ | .0 | .0 <br> .0 | 0.0 <br> 0.0 | 0.0 <br> 0.0 | 0.0 <br> 0.0 | 0.0 <br> 0.0 | 1 | 0.01 <br> 0.01 | 0.01 <br> 0.01 | 0.01 <br> 0.01 | m | 0.1 <br> .04 | 0.04 <br> 0.06 | 0.02 <br> 0.06 | 0.07 <br> 0.07 |
| a $=0.15$ | .0 | .0 <br> .00 | 0.0 <br> 0.0 | 0.07 <br> 0.04 | 0.06 <br> 0.03 | 0.03 <br> $0.010$ | 2 | 1.0 <br> 1.0 | 1.0 <br> 1.0 | 0 | 1.0 |  |  |  |
| $\mathrm{a}=0.25$ | 1.0 <br> 1.0 | 1.0 <br> 1.0 | 1.0 <br> 1.0 | 1.0 <br> 1.0 | 1.0 <br> 1.0 | 1.0 <br> 1.0 | $m_{3}$ | 1.0 <br> 1.0 | 1.0 <br> 1.0 | 1.0 <br> 1.0 | 1.0 <br> 1.0 | 1.0 <br> 1.0 | 0.34 <br> 0.56 | 0.88 |
| $a=0.45$ | 1.0 <br> 1.0 | 1.0 <br> 1.0 | 1.0 <br> 1.0 | 1.0 <br> 1.0 | 1.0 <br> 1.0 | 1.0 <br> 1.0 | 4 | 0.36 <br> 0.57 | 0.98 <br> 0.9 | 0.39 <br> 0.5 | 0.57 <br> 0.9 | 0.98 <br> 1.0 | 0.23 <br> 0.38 | 0.78 |
| Ghosal et al. $(2000)$ <br> $\mathrm{a}=0.00$ | 0.0 | 0.0 <br> .0 | 0.0 <br> 0.0 | 0.0 <br> 0.0 | 0.0 <br> 0.0 | 0.0 <br> 0.0 | m | 0.01 <br> 0.0 | 0.01 <br> 0.04 | 0.01 <br> 0.02 | 0.0 <br> 0.0 | 0.01 <br> 0.0 | 0.02 <br> 0.02 | 0.0 <br> 0.01 |
| a $=0.15$ | 0.0 | .0 <br> .0 | 0.0 <br> 0.0 | 0.0 <br> 0.0 | 0.0 <br> 0.0 | 0.0 <br> 0.0 | 2 | 1.0 <br> 1.0 | 1.0 <br> 1.0 | 1.0 <br> 1.0 | 1.0 <br> 1.0 | 1.0 <br> 1.0 | 0.37 <br> 0.7 | 0.94 |
| $\mathrm{a}=0.25$ | 0.0 | .0 <br> .0 | 1.0 <br> 0.0 | 0.0 <br> 0.0 | 0.0 <br> 0.0 | 0.31 <br> 0.0 |  | 0.97 <br> 1.0 | 1.0 <br> 1.0 | 1.0 <br> 1.0 | 0.94 <br> 1.0 | 1.0 <br> 1.0 | 0.1 <br> 0.03 | 0.87 |
| $a=0.45$ | 1.0 <br> 1.0 | 1.0 <br> 1.0 | 1.0 <br> 1.0 | 1.0 <br> 1.0 | 1.0 <br> 1.0 | 1.0 <br> 1.0 | 4 | 0.01 <br> 0.19 | 0.53 <br> 1.0 | 0.02 <br> 0.13 | 0.53 <br> 1.0 | 0.0 <br> 0.0 | 0.06 <br> 0.71 | 0.99 |
| Bowman et al. (1998) <br> $\mathrm{a}=0.00$ | 0.0 | .0 <br> .0 | 0.0 <br> 0.0 | 0.02 <br> 0.01 | 0.0 <br> 0.0 | 0.0 <br> 0.0 | $m_{1}$ | 0.0 <br> 0.0 | 0.0 <br> 0.0 <br> .0 | 0.0 <br> 0.0 | 0.0 <br> 0.0 | 0.0 <br> 0.0 | 0.0 <br> 0.0 | 0.0 <br> 0.0 |
| a=0.15 | .0 | .0 <br> .0 | 0.0 <br> 0.0 | 0.03 <br> 0.0 | 0.0 <br> 0.0 | 0.01 <br> 0.02 | ~ | 0.0 <br> 0.0 | 0.0 <br> 0.0 | 0.0 <br> 0.0 | 0.0 <br> 0.0 | 0.0 <br> 0.0 | 0.0 <br> 0.0 | 0.0 <br> 0.0 |
| $\mathrm{a}=0.25$ | 1.0 <br> 1.0 | 1.0 <br> 1.0 | 1.0 <br> 1.0 | 1.0 <br> 1.0 | 1.0 <br> 1.0 | 1.0 <br> 1.0 |


---

# 7 Application: Monotonicity Test for scRNA-seq Trajectory Inference 

Single-cell transcriptome sequencing (scRNA-seq) is a powerful technique that allows researchers to profile transcript abundance at the resolution of individual cells. Trajectory inference aims first to allocate cells to lineages and then order them based on pseudotimes within these lineages. Based on trajectory inference, researchers can discover differentially expressed genes within lineages, such as Van den Berge et al. (2020)'s tradeSeq, Song and Li (2021)'s PseudotimeDE, and Hou et al. (2023)'s Lamian. These methods mostly focus on the differential genes by checking whether the trajectory is constant along the pseudotime. Once a gene is identified as differentially expressed, researchers may further check whether its expression exhibits a monotone pattern. A non-decreasing expression pattern indicates that the corresponding gene is turning on and needed thereafter along the cell lineage. A decreasing expression pattern indicates that the corresponding gene is needed less and less along the pseudotime. On the other hand, a non-monotone expression pattern indicates that the corresponding gene is part of a more complex dynamics. Such detailed dynamics may illuminate the critical regulatory mechanism of cell differentiation along the corresponding lineage.

As an analogy to the term differentially expressed (DE) gene when the null hypothesis that the expression of the gene along the trajectory is constant is rejected, we call a non-monotonically expressed (nME) gene when the null hypothesis that the expression is monotonic is rejected. We adopt tradeSeq to identify DE genes, and the monotonicity test via monotone decomposition with cubic spline (MDCS) to find nME genes. Both DE genes and nME genes are selected using the Benjamini-Hochberg (BH) procedure to control the false discovery rate (FDR) with cutoff $\alpha=0.05$.

To explore the biological functions of DE genes and nME genes, we examined the Gene Ontology (GO), which is a relational database of terms (concepts) used to describe gene functions, and conducted enrichment analysis (Boyle et al., 2004).

Suppose there are $N$ genes in the reference gene list, among which $n$ genes are in our analyzed gene set. For a GO term of interest, suppose there are $M$ and $k$ genes within the reference gene list and our analyzed gene set, respectively, that are annotated to have the GO term. The $p$-value for the one-sided Fisher's exact test of the null hypothesis that the GO term is not enriched in the analyzed gene set can be calculated based on the hypergeometric distribution:

$$
p=1-\sum_{i=0}^{k-1} \frac{\binom{M}{i}\binom{N-M}{k-i}}{\binom{N}{n}}
$$

We repeat this test for multiple GO terms of interest and correct for multiple comparisons via the BH procedure to control the FDR at the cutoff $\alpha=0.05$.

### 7.1 nME genes can identify significant GO terms when DE genes fail

We studied the leukocyte lineage of the mouse bone marrow data set (Paul et al., 2015), which consists of the expression measurements of 3004 genes at 1474 pseudotime points. Figure 5a shows the reduced two-dimensional representation of the data using uniform manifold approximation and projection (UMAP) (McInnes et al., 2018). Eight cell types are denoted with different colors and shapes. The solid curve is the pseudotime axis, which starts from the cell type Multipotent progenitors at the bottomright and ends at the cell type Neutrophils at the topleft. Note that although a monotone pattern is a special DE pattern, we do not perform the monotonicity test in a two-step manner, i.e., firstly find DE genes and then perform the monotonicity test among those found DE




---

genes. Instead, for each gene, we test whether it is a DE gene or an nME gene independently. Figure 5b displays the paired $p$-values $\left(p_{\mathrm{nME}}, p_{\mathrm{DE}}\right)$ in the logarithmic scale, where the dash lines denote the cutoff determined by the BH procedure. As a result, we identified 109 nME genes (it is 102 after GO analysis since 7 genes are not mapped in the GO database) and 767 DE genes, of which 53 genes are in common. These numbers are also noted in the titles of GO bar plots in Figure 6. Figure 5c illustrates the fitted trajectory for gene 2610029G23Rik, which is identified as an nME gene but not a DE gene, i.e., it lies in the bottom right green block of Figure 5b.



Figure 5: (a): Two-dimensional representation of the data using UMAP. Different cell types are denoted with different colors (and shapes). The pseudotime axis is displayed, which starts from the Multipotent progenitors cell type at the bottom-right to the Neutrophils cell type at the top-left. (b): the scatter plot of the paired $p$-values $\left(p_{\mathrm{nME}}, p_{\mathrm{DE}}\right)$, where the star symbols denote NA values when tradeSeq failed. (c): one example gene located in the bottom right green block of (b), which is identified as an nME gene but not a DE gene. (d): Trajectory curves of 109 nME genes. The curves of 22 genes annotated in the GO term "translation" are highlighted.

Figure 6 displays GO enrichment analysis on the DE genes and nME genes by R package clusterProfiler (Yu et al., 2023). Figures 6a, 6b and 6c take the whole 3004 genes as the reference gene list, but note that, because some genes are not mapped in the GO database, there are only 2665 genes after filtering. We cannot find significant GO terms for the DE gene list, as shown in Figure 6b, which is left blank deliberately due to no significant results. In contrast, we can identify several significant GO terms for the nME gene list. Figures 6c and 6d display the intersection of the DE gene list and the nME gene list with respect to the whole gene list or the DE gene list, respectively. Both can identify significant GO terms. One possible reason for DE genes failing to identify significant GO terms is that the range of DE genes might be too broad, thus different sub-categories of DE genes (the non-monotonic pattern is a special sub-category) might contribute to different GO terms, but the increased sample size due to incorporating unrelated genes might reduce the significance for determining the significant GO terms. Another potential reason is that the tradeSeq test is not robust enough. As shown by the star symbol in Figure 5b, there are many NA values returned by tradeSeq, which is a known issue discussed in their GitHub repository ${ }^{1}$.

We can further check whether the pattern of trajectory curves in the enriched GO terms agrees with the biological mechanism. Take the first GO term "translation" as an example. Figure 5d displays the trajectory curves of 109 nME genes along the pseudotime. Among these 109 nME genes, the curves of 22 genes annotated in the GO term "translation" are highlighted. These genes exhibit a coherent pattern, characterized by an initial increase in expression followed by a subsequent decrease. If we cast the pseudotime axis in Figure 5d back to Figure 5a, the curve pattern implies that the gene expression increases when the cell develops from Multipotent

[^0]
[^0]:    ${ }^{1}$ https://github.com/statOmics/tradeSeq/issues/209




---



Figure 6: GO enrichment analysis of four gene sets ((a): nME gene set; (b): DE gene set; (c): the intersection of nME and DE genes; (d): the same gene set as (c) but the reference list is the DE genes) with BH FDR cutoff $\alpha=0.05$. The numbers of genes are noted in the title of each subfigure. The enriched GO terms are sorted by the adjusted p-values. (b) is left empty deliberately since no significant GO terms are selected.
progenitors to Monocytes, and roughly after the gene expression reaching the peak, the cell evolves to Neutrophils. This behavior is consistent with the biological fact that specialized cell types (here Neutrophils) might reduce rates of translation (and hence protein synthesis), since their structure and function are relatively stable.

# 7.2 nME genes can fine-locate GO terms when DE genes identify too many terms 

In some scenarios, although GO enrichment analysis can identify significant GO terms given the DE genes, nME genes can further fine-locate GO terms and focus on a small but significant set of GO terms. We analyzed the cholangiocyte lineage from the mouse liver data studied in Ghazanfar et al. (2020) to demonstrate such an advantage of nME genes. In the dataset, there are 6038 genes and 308 pseudotime points.
tradeSeq identifies 767 DE genes (it is 801 before filtering due to unmapping in GO), and the monotonicity test identifies 67 nME genes (it is 69 before filtering due to unmapping in GO), of which 45 genes are in common. For the 767 DE genes, we identify 439 significant GO terms, whereas for the 67 nME genes, we find 39 significant GO terms. Between the two sets, 28 GO terms are in common. Figure 7a displays all GO terms returned by the 39 nME genes, where the star symbol indicates GO terms not shared by the DE genes. Figure 7b shows the enrichment map constructed by the GO terms from DE genes, in which the common GO terms shared by the nME genes are highlighted. In the enrichment map, an edge connects two GO terms if there are overlapped genes, and hence, mutually overlapping GO terms tend to cluster together, making it easy to identify functional modules. It is clear that the shared GO terms mainly focus on two clusters: one is isolated from others on the right side and forms a pentagon shape with the keyword "coagulation"; another cluster is located at the left corner of the biggest cluster, related to "catabolic process". In other words, nME genes can help fine-locate GO terms, which might help save time for researchers without checking too many GO terms from DE genes.

We further check the new GO terms enriched by the nME genes, which are annotated with the star symbol in Figure 7a. These new GO terms might be contributed by new genes that are not identified as DE genes. For example, we take the GO term "regulation of blood coagulation" as an example, which contains 5 genes $\{\mathrm{F} 11, K n g 2$, Serpinc1, Serpinf2, Vtn $\}$ in the nME gene set, where the first three are also in the DE gene set, but the last two are only in the nME gene set. Figures 8 c and 8 d display the fitted trajectory of the expression along pseudotime by our




---



Figure 8: Hypothesis testing on the cholangiocyte lineage of the mouse liver data. (a) The scatter plot of paired $p$-values $\left(p_{\text {nME }}, p_{\mathrm{DE}}\right)$, where the cutoffs selected by the BH procedure are 0.00053 and 0.00660 , respectively. (b) Trajectory curves of all nME genes. (c) and (d) are two genes in the GO term "regulation of blood coagulation", which are enriched by the nME genes but not DE genes.

Here, we consider the liver dataset in Section 7.2. Figure 9a shows the dendrogram from hierarchical clustering with complete linkage on 69 nME genes. We take the cutoff 2.0 to obtain 10 clusters with clear patterns. Figure 9b presents the trajectory curves of those 69 nME genes, and different colors denote different clusters. Notably, we have highlighted three representative clusters, each depicted in its respective figure, ranging from Figure 9c to Figure 9d. Figure 9c displays a peak on the right side, while Figure 9d showcases a peak on the left side.

On the other hand, we perform hierarchical clustering with a similar cutoff 1.5 and identify 12 clusters, as shown in Figure 9e. The trajectory curves of 801 DE genes with different colors representing different clusters are displayed in Figure 9f. It is worth noting that the presence of monotonic patterns has somewhat concealed the underlying wiggly patterns, as evidenced in Figure 9g, which combines non-monotonic patterns similar to those found in Figure 9c with numerous ascending curves. Similarly, Figure 9h combines the non-monotonic pattern observed in Figure 9d, illustrating the challenges in distinguishing these patterns.

Pure non-monotonic patterns hold the potential to identify significant patterns. For example, all three genes in Figure 9c are significantly annotated to GO terms "defense response to other organism", "response to external biotic stimulus", and "response to other organism", each accompanied by FDR adjusted $p$-value of 0.00278 .

# 8 Discussions 

We formulate the monotone decomposition with monotone splines. It can serve as a fitting method when we sum up two monotone components, and it can be used to conduct a test of monotonicity by checking whether one component is constant.

As a fitting method, the experiments have shown that the monotone decomposition with cubic splines improves the performance, especially in high noise cases. We can explain the better performance in monotone functions theoretically. Similar phenomena have been observed for the monotone decomposition with smoothing splines. However, there are also some limitations:

- The cross-validation procedure for simultaneously tuning two parameters is computationally extensive. The generative bootstrap sampler (GBS) proposed by Shin et al. (2023) might be an alternative to speed up the cross-validation step.
- Currently, the theoretical guarantees are only for monotone functions. It would be great if the theoretical results could be extended to general functions.




---



Figure 9: Clustering of trajectory curves of nME genes (first row) and DE genes (second row). (a): Hierarchical dendrogram of 69 nME genes. The cutoff (2.0) at the dashed line results in 10 clusters. (b): Trajectory curves of 69 nME genes. (c)-(d) display the curves of 2 out of 10 clusters from (b), respectively. The gene symbols are noted for clusters with few genes. (e): Hierarchical dendrogram of 801 DE genes. The cutoff (1.5) at the dashed line results in 12 clusters. (f): Trajectory curves of 801 DE genes. (g) and (h) are two distinct clusters from 12 clusters in (f). Different colors denote different clusters. The same color in (b) to (d) denotes the same cluster, and the same color in (g) to (h) denotes the same cluster, but there is no direct correspondence between the colors in (b) and (f).

For the test of monotonicity by monotone decomposition, the proposed statistics based on monotone decomposition show competitive performance and are even much better than the existing approaches.

We also apply the fitting and testing based on monotone decomposition to investigate the monotonic and non-monotonic trajectory patterns in several scRNA-seq datasets. In parallel with the conventional analysis of differentially expressed (DE) genes, we propose the concept of non-monotonically expressed (nME) genes, which might lead to new biological insights.

# Acknowledgement 

Lijun Wang was supported by the Hong Kong Ph.D. Fellowship Scheme from the University Grant Committee. Hongyu Zhao was supported in part by NIH grant P50 CA196530. JSL was supported in part by the NSF DMS/NIGMS 2 Collaborative Research grant (R01 GM152814).

## Supplementary Material

The Supplementary Material contains additional simulation results and technical proofs of propositions.




---

# References 

Bowman, A. W., Jones, M. C., \& Gijbels, I. (1998). Testing Monotonicity of Regression. Journal of Computational and Graphical Statistics, 7(4), 489-500. https://doi.org/10.1080/10618600. 1998.10474790

Boyle, E. I., Weng, S., Gollub, J., Jin, H., Botstein, D., Cherry, J. M., \& Sherlock, G. (2004). GO::TermFinder-open source software for accessing Gene Ontology information and finding significantly enriched Gene Ontology terms associated with a list of genes. Bioinformatics, 20(18), 3710-3715. https://doi.org/10.1093/bioinformatics/bth456

Chetverikov, D. (2019). Testing regression monotonicity in econometric models. Econometric Theory, 35(4), 729-776. https://doi.org/10.1017/S0266466618000282
Chipman, H. A., George, E. I., \& McCulloch, R. E. (2010). BART: Bayesian additive regression trees. The Annals of Applied Statistics, 4(1), 266-298. https://doi.org/10.1214/09-AOAS285
Chipman, H. A., George, E. I., McCulloch, R. E., \& Shively, T. S. (2022). mBART: Multidimensional Monotone BART. Bayesian Analysis, 17(2), 515-544. https://doi.org/10.1214/21-BA1259

Davidson, R., \& Flachaire, E. (2008). The wild bootstrap, tamed at last. Journal of Econometrics, 146(1), 162-169. https://doi.org/10.1016/j.jeconom.2008.08.003
De Boor, C. (1978). A practical guide to splines (Vol. 27). Springer.
Ghazanfar, S., Lin, Y., Su, X., Lin, D. M., Patrick, E., Han, Z.-G., Marioni, J. C., \& Yang, J. Y. H. (2020). Investigating higher-order interactions in single-cell data with scHOT. Nature Methods, 17(8), 799-806. https://doi.org/10.1038/s41592-020-0885-x
Ghosal, S., Sen, A., \& van der Vaart, A. W. (2000). Testing Monotonicity of Regression. The Annals of Statistics, 28(4), 1054-1082.
Gramacy, R. B. (2020). Surrogates: Gaussian Process Modeling, Design and Optimization for the Applied Sciences. Chapman Hall/CRC.
Hall, P., \& Heckman, N. E. (2000). Testing for Monotonicity of a Regression Mean by Calibrating for Linear Functions. The Annals of Statistics, 28(1), 20-39.
Hastie, T., Tibshirani, R., \& Friedman, J. (2009). The elements of statistical learning: Data mining, inference, and prediction (2nd ed.). Springer Science \& Business Media.
Hou, W., Ji, Z., Chen, Z., Wherry, E. J., Hicks, S. C., \& Ji, H. (2023). A statistical framework for differential pseudotime analysis with multiple single-cell RNA-seq samples. Nature Communications, 14(1), 7286. https://doi.org/10.1038/s41467-023-42841-y
Magnus, J. R., \& Neudecker, H. (2019). Matrix Differential Calculus with Applications in Statistics and Econometrics (1st ed.). John Wiley \& Sons, Ltd. https://doi.org/10.1002/9781119541219
McInnes, L., Healy, J., Saul, N., \& Großberger, L. (2018). UMAP: Uniform Manifold Approximation and Projection. Journal of Open Source Software, 3(29), 861. https://doi.org/10.21105/joss. 00861
Paul, F., Arkin, Y., Giladi, A., Jaitin, D. A., Kenigsberg, E., Keren-Shaul, H., Winter, D., Lara-Astiaso, D., Gury, M., Weiner, A., David, E., Cohen, N., Lauridsen, F. K. B., Haas, S., Schlitzer, A., Mildner, A., Ginhoux, F., Jung, S., Trumpp, A., . . . Amit, I. (2015). Transcriptional Heterogeneity and Lineage Commitment in Myeloid Progenitors. Cell, 163(7), 1663-1677. https://doi.org/10.1016/j.cell.2015.11.013
Ramsay, J. O., \& Silverman, B. W. (2005). Functional data analysis (Second edition). Springer.
Rasmussen, C. E., \& Williams, C. K. I. (2006). Gaussian processes for machine learning. MIT Press.
Shin, M., Wang, S., \& Liu, J. S. (2023). Generative Multi-purpose Sampler for Weighted Mestimation. Journal of Computational and Graphical Statistics, 0(ja), 1-53. https://doi.org/10. 1080/10618600.2023.2292668




---

Song, D., \& Li, J. J. (2021). PseudotimeDE: Inference of differential gene expression along cell pseudotime with well-calibrated p-values from single-cell RNA sequencing data. Genome Biology, 22(1), 124. https://doi.org/10.1186/s13059-021-02341-y
Van den Berge, K., Roux de Bézieux, H., Street, K., Saelens, W., Cannoodt, R., Saeys, Y., Dudoit, S., \& Clement, L. (2020). Trajectory-based differential expression analysis for single-cell sequencing data. Nature Communications, 11(1), 1201. https://doi.org/10.1038/s41467020-14766-3

Wang, J. C., \& Meyer, M. C. (2011). Testing the monotonicity or convexity of a function using regression splines. The Canadian Journal of Statistics / La Revue Canadienne de Statistique, 39(1), 89-107.

Wang, L., Fan, X., Li, H., \& Liu, J. S. (2023). Monotone Cubic B-Splines. https://doi.org/10.48550/ arXiv. 2307.01748

Yu, G., Wang, L.-G., Hu, E., Luo, X., Chen, M., Dall'Olio, G., Wei, W., \& Gao, C.-H. (2023). clusterProfiler: A universal enrichment tool for interpreting omics data. https://doi.org/ 10.18129/B9.bioc.clusterProfiler




---

# A More Simulation Results 

## A. 1 Candidate Kernels

Random functions with kernel $K$, including Squared Exponential (SE) kernel $K_{\mathrm{SE}}$, Rational Quadratic (RQ) kernel $K_{\mathrm{RQ}}$, Matérn (Mat) kernel $K_{\text {Mat }}$ and Periodic kernel $K_{\text {Periodic }}$ (Rasmussen \& Williams, 2006).

$$
\begin{gathered}
K_{\mathrm{SE}}\left(x, x^{\prime}\right)=\exp \left(-\frac{\left(x-x^{\prime}\right)^{2}}{2 \ell^{2}}\right), K_{\mathrm{Mat}}\left(x, x^{\prime}\right)=\frac{2^{1-\nu}}{\Gamma(\nu)}\left(\frac{\sqrt{2 \nu}\left|x-x^{\prime}\right|}{\ell}\right)^{\nu} \mathcal{S}_{\nu}\left(\frac{\sqrt{2 \nu}\left|x-x^{\prime}\right|}{\ell}\right) \\
K_{\mathrm{RQ}}\left(x, x^{\prime}\right)=\left(1+\frac{\left(x-x^{\prime}\right)^{2}}{2 \alpha \ell^{2}}\right)^{-\alpha}, K_{\text {Periodic }}\left(x, x^{\prime}\right)=\exp \left(-\frac{2 \sin ^{2}\left(\left|x-x^{\prime}\right| / T\right)}{\ell^{2}}\right)
\end{gathered}
$$

where $\ell, \nu, \alpha, T$ are the parameters, and $\mathcal{S}_{\nu}$ is a modified Bessel function. In particular, "Mat12" refers to the Matérn kernel with $\nu=1 / 2$, and similarly, "Mat32" and "Mat52" indicate $\nu=3 / 2$ and $5 / 2$, respectively. Any additional parameters are appended to the kernel name; for example, "SE-1" represents the Squared Exponential kernel with $\ell=1$, "Mat12-1" denotes the Matérn kernel with $\nu=1 / 2, \ell=1$, and "RQ-0.1-0.5" is the Rational Quadratic kernel with parameter $\ell=0.1, \alpha=0.5$.

## A. 2 Random Function Generation

A random function $f$ with kernel $K$ is generated as follows,

1. Generate $n$ random points, $x_{i} \sim \mathcal{U}[-1,1], i=1, \ldots, n$.
2. Calculate the covariance matrix $\boldsymbol{\Sigma}$ based on kernel $K, \Sigma_{i j}=K\left(x_{i}, x_{j}\right)$. Practically, add a small constant, say $10^{-7}$, on the diagonal of $\boldsymbol{\Sigma}$ to prevent numerically ill-conditioned matrix (Gramacy, 2020).
3. Generate a random Gaussian vector with the above covariance matrix, $\boldsymbol{f} \sim \mathcal{N}(\mathbf{0}, \boldsymbol{\Sigma})$.



Figure 10: Candidate functions. The left panel shows several regular functions, the middle panel displays the random functions drawn from Gaussian processes with the square exponential kernel, and the right panel shows the random functions generated from Gaussian processes with other kernels.




---

# A. 3 Monotone Decomposition with Cubic Splines 






---

Table 7: Results for comparing the cubic splines and the fitting by monotone decomposition with CV-tuned $\mu$ and fixed $J$. The values are averages over 100 replications, with the standard error of the average in parentheses. The bold values highlight the smaller mean squared prediction error.

| curve | $\sigma$ | MSFE |  | MSPE |  | p-value | prop. |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|  |  | CubicSpline | MonoDecomp | CubicSpline | MonoDecomp |  |  |
| $x^{2}$ | 0.1 | $9.68 \mathrm{e}-01(8.2 \mathrm{e}-03)$ | 9.71e-01 (8.2e-03) | $7.38 \mathrm{e}-01(3.6 \mathrm{e}-02)$ | 7.07e-01 (3.3e-02) | $1.47 \mathrm{e}-03$ (**) | 0.65 |
|  | 0.2 | $1.92 \mathrm{e}+00(1.6 \mathrm{e}-02)$ | $1.93 \mathrm{e}+00(1.6 \mathrm{e}-02)$ | $1.53 \mathrm{e}+00(7.7 \mathrm{e}-02)$ | $1.45 \mathrm{e}+00(7.2 \mathrm{e}-02)$ | $1.03 \mathrm{e}-03$ (**) | 0.74 |
|  | 0.5 | $4.88 \mathrm{e}+00(3.6 \mathrm{e}-02)$ | $4.90 \mathrm{e}+00(3.6 \mathrm{e}-02)$ | 3.67 e+00 (1.5e-01) | $3.37 \mathrm{e}+00(1.3 \mathrm{e}-01)$ | $2.20 \mathrm{e}-06$ (***) | 0.77 |
|  | 1.0 | $9.63 \mathrm{e}+00(8.2 \mathrm{e}-02)$ | $9.73 \mathrm{e}+00(8.0 \mathrm{e}-02)$ | $7.12 \mathrm{e}+00(3.2 \mathrm{e}-01)$ | $5.92 \mathrm{e}+00(2.5 \mathrm{e}-01)$ | $1.73 \mathrm{e}-10$ (***) | 0.77 |
| $x^{3}$ | 0.1 | 9.56e-01 (7.6e-03) | 9.58e-01 (7.1e-03) | 7.32e-01 (3.5e-02) | 6.98e-01 (2.9e-02) | $1.01 \mathrm{e}-03$ (**) | 0.61 |
|  | 0.2 | $1.93 \mathrm{e}+00(1.6 \mathrm{e}-02)$ | $1.94 \mathrm{e}+00(1.5 \mathrm{e}-02)$ | $1.47 \mathrm{e}+00(7.1 \mathrm{e}-02)$ | $1.38 \mathrm{e}+00(5.8 \mathrm{e}-02)$ | $2.88 \mathrm{e}-05$ (***) | 0.69 |
|  | 0.5 | 4.83e+00 (4.3e-02) | $4.86 \mathrm{e}+00(4.2 \mathrm{e}-02)$ | 3.66 e+00 (1.5e-01) | 3.41e+00 (1.4e-01) | $7.49 \mathrm{e}-03$ (***) | 0.64 |
|  | 1.0 | $9.55 \mathrm{e}+00(8.1 \mathrm{e}-02)$ | $9.68 \mathrm{e}+00(7.8 \mathrm{e}-02)$ | 8.03e+00 (3.7e-01) | $7.02 \mathrm{e}+00(2.7 \mathrm{e}-01)$ | $2.01 \mathrm{e}-06$ (***) | 0.69 |
| $\exp (x)$ | 0.1 | $9.56 \mathrm{e}-01(7.4 \mathrm{e}-03)$ | 9.57e-01 (7.3e-03) | $7.51 \mathrm{e}-01(3.3 \mathrm{e}-02)$ | $7.26 \mathrm{e}-01(3.0 \mathrm{e}-02)$ | $3.12 \mathrm{e}-04$ (***) | 0.61 |
|  | 0.2 | 1.93e+00 (1.5e-02) | $1.94 \mathrm{e}+00(1.5 \mathrm{e}-02)$ | 1.40e+00 (6.6e-02) | 1.32e+00 (5.9e-02) | $4.32 \mathrm{e}-07$ (***) | 0.67 |
|  | 0.5 | $4.82 \mathrm{e}+00(3.9 \mathrm{e}-02)$ | $4.84 \mathrm{e}+00(3.7 \mathrm{e}-02)$ | $3.52 \mathrm{e}+00(1.7 \mathrm{e}-01)$ | $3.02 \mathrm{e}+00(1.4 \mathrm{e}-01)$ | $9.36 \mathrm{e}-11$ (***) | 0.8 |
|  | 1.0 | $9.74 \mathrm{e}+00(7.6 \mathrm{e}-02)$ | $9.82 \mathrm{e}+00(7.5 \mathrm{e}-02)$ | $7.47 \mathrm{e}+00(3.3 \mathrm{e}-01)$ | $6.09 \mathrm{e}+00(2.5 \mathrm{e}-01)$ | $6.35 \mathrm{e}-11$ (***) | 0.8 |
| sigmoid | 0.1 | 9.53e-01 (7.3e-03) | $9.60 \mathrm{e}-01(7.5 \mathrm{e}-03)$ | $8.84 \mathrm{e}-01(2.4 \mathrm{e}-02)$ | 8.55e-01 (2.5e-02) | $3.16 \mathrm{e}-03$ (***) | 0.68 |
|  | 0.2 | 1.87e+00 (1.4e-02) | $1.89 \mathrm{e}+00(1.4 \mathrm{e}-02)$ | $1.81 \mathrm{e}+00(6.2 \mathrm{e}-02)$ | $1.67 \mathrm{e}+00(5.2 \mathrm{e}-02)$ | $5.12 \mathrm{e}-05$ (***) | 0.71 |
|  | 0.5 | $4.78 \mathrm{e}+00(3.8 \mathrm{e}-02)$ | $4.82 \mathrm{e}+00(3.6 \mathrm{e}-02)$ | $3.83 \mathrm{e}+00(1.7 \mathrm{e}-01)$ | 3.51e+00 (1.3e-01) | $2.42 \mathrm{e}-04$ (***) | 0.66 |
|  | 1.0 | $9.50 \mathrm{e}+00(


---

# A. 4 Monotone Decomposition Fitting with Smoothing Splines 

## A.4.1 A complete version for Table 2

Table 8: Results for comparing the smoothing splines with CV-tuned $\lambda$ and the fitting by monotone decomposition with CV-tuned $(\lambda, \mu)$. The values are averages over 100 replications, with the standard error of the average in parentheses. The bold values highlight the smaller mean squared prediction error.

| curve | $\sigma$ | MSFE |  | MSPE |  | $p$-value | prop. |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|  |  | SmoothSpline | MonoDecomp | SmoothSpline | MonoDecomp |  |  |
| $x^{2}$ | 0.1 | $9.57 \mathrm{e}-01(8.3 \mathrm{e}-03)$ | $9.73 \mathrm{e}-01(8.2 \mathrm{e}-03)$ | $7.38 \mathrm{e}-01(2.4 \mathrm{e}-02)$ | $8.67 e-01(2.4 e-02)$ | $1.74 \mathrm{e}-14{ }^{(* * *)}$ | 0.25 |
|  | 0.5 | $4.79 \mathrm{e}+00(4.1 \mathrm{e}-02)$ | $4.80 \mathrm{e}+00(4.1 \mathrm{e}-02)$ | $3.41 \mathrm{e}+00(1.2 \mathrm{e}-01)$ | $3.39 \mathrm{e}+00(1.1 \mathrm{e}-01)$ | 3.61e-01 | 0.46 |
|  | 1.0 | $9.65 \mathrm{e}+00(8.9 \mathrm{e}-02)$ | $9.69 \mathrm{e}+00(8.5 \mathrm{e}-02)$ | $6.44 \mathrm{e}+00(2.9 \mathrm{e}-01)$ | $6.35 \mathrm{e}+00(2.5 \mathrm{e}-01)$ | $1.68 \mathrm{e}-01$ | 0.49 |
|  | 1.5 | $1.44 \mathrm{e}+01(1.1 \mathrm{e}-01)$ | $1.45 \mathrm{e}+01(1.1 \mathrm{e}-01)$ | $9.31 \mathrm{e}+00(3.9 \mathrm{e}-01)$ | $9.14 \mathrm{e}+00(3.4 \mathrm{e}-01)$ | $4.68 \mathrm{e}-02{ }^{(*)}$ | 0.6 |
|  | 2.0 | $1.92 \mathrm{e}+01(1.6 \mathrm{e}-01)$ | $1.92 \mathrm{e}+01(1.5 e-01)$ | $1.23 \mathrm{e}+01(4.9 \mathrm{e}-01)$ | $1.15 \mathrm{e}+01(4.3 \mathrm{e}-01)$ | $4.45 \mathrm{e}-06{ }^{(*) * *}$ | 0.81 |
| $x^{3}$ | 0.1 | $9.46 \mathrm{e}-01(8.0 \mathrm{e}-03)$ | $9.89 \mathrm{e}-01(8.0 \mathrm{e}-03)$ | $8.65 \mathrm{e}-01(2.4 \mathrm{e}-02)$ | $1.11 \mathrm{e}+00(2.5 e-02)$ | $0.00 \mathrm{e}+00{ }^{(*) * *}$ | 0.2 |
|  | 0.5 | $4.86 \mathrm{e}+00(4.4 \mathrm{e}-02)$ | $4.88 \mathrm{e}+00(4.3 \mathrm{e}-02)$ | $3.65 \mathrm{e}+00(1.2 \mathrm{e}-01)$ | $3.55 \mathrm{e}+00(1.2 \mathrm{e}-01)$ | $9.06 \mathrm{e}-03{ }^{(*) * *}$ | 0.58 |
|  | 1.0 | $9.75 \mathrm{e}+00(8.2 \mathrm{e}-02)$ | $9.77 \mathrm{e}+00(8.2 \mathrm{e}-02)$ | $6.47 \mathrm{e}+00(1.8 \mathrm{e}-01)$ | $6.21 \mathrm{e}+00(1.7 \mathrm{e}-01)$ | $1.18 \mathrm{e}-04{ }^{(*) * *}$ | 0.65 |
|  | 1.5 | $1.45 \mathrm{e}+01(1.1 \mathrm{e}-01)$ | $1.46 \mathrm{e}+01(1.1 \mathrm{e}-01)$ | $9.16 \mathrm{e}+00(3.1 \mathrm{e}-01)$ | $8.67 \mathrm{e}+00(2.8 \mathrm{e}-01)$ | $1.67 \mathrm{e}-06{ }^{(*) * *}$ | 0.81 |
|  | 2.0 | $1.92 \mathrm{e}+01(1.8 \mathrm{e}-01)$ | $1.92 \mathrm{e}+01(1.6 \mathrm{e}-01)$ | $1.16 \mathrm{e}+01(5.9 \mathrm{e}-01)$ | $1.09 \mathrm{e}+01(4.9 \mathrm{e}-01)$ | $1.15 \mathrm{e}-04{ }^{(*) * *}$ | 0.78 |
| $\exp (x)$ | 0.1 | $9.53 \mathrm{e}-01(7.6 \mathrm{e}-03)$ | $9.64 \mathrm{e}-01(7.7 \mathrm{e}-03)$ | $7.96 \mathrm{e}-01(2.6 \mathrm{e}-02)$ | $9.13 \mathrm{e}-01(2.6 \mathrm{e}-02)$ | $5.02 \mathrm{e}-12{ }^{(*) * *}$ | 0.26 |
|  | 0.5 | $4.80 \mathrm{e}+00(4.3 \mathrm{e}-02)$ | $4.82 \mathrm{e}+00(3.9 \mathrm{e}-02)$ | $3.33 \mathrm{e}+00(1.5 \mathrm{e}-01)$ | $3.30 \mathrm{e}+00(1.3 \mathrm{e}-01)$ | 2.60e-01 | 0.51 |
|  | 1.0 | $9.74 \mathrm{e}+00(8.4 \mathrm{e}-02)$ | $9.75 \mathrm{e}+00(8.4 \mathrm{e}-02)$ | $5.94 \mathrm{e}+00(2.3 \mathrm{e}-01)$ | $5.82 \mathrm{e}+00(2.1 \mathrm{e}-01)$ | $3.12 \mathrm{e}-02{ }^{(*)}$ | 0.58 |
|  | 1.5 | $1.45 \mathrm{e}+01(1.3 \mathrm{e}-01)$ | $1.46 \mathrm{e}+01(1.3 \mathrm{e}-01)$ | $9.10 \mathrm{e}+00(4.4 \mathrm{e}-01)$ | $8.83 \mathrm{e}+00(4.1 \mathrm{e}-0


---

# A.4.2 Tune $\mu$ with fixed $\lambda$ 

First, we fix the parameter $\lambda$ for the roughness penalty as the CV-tuned one for the smoothing splines. Then, we choose the parameter $\mu$ to minimize the CV error. Figure 11 demonstrates the procedure. The left panel shows the CV-error curve for each candidate parameter $\mu$, and the right panel compares the monotone decomposition fitting given the parameter which minimized the curve in the left panel to the smoothing spline fitting. The monotone decomposition achieves a better MSPE, and it is obvious that the better performance is mainly due to the shrinkage on the local modes based on the shapes of fitting curves.



Figure 11: Demo for monotone decomposition with smoothing splines. The left panel shows the leave-one-out cross-validation error curve for each candidate $\mu$ when $\lambda$ is fixed to the one of smoothing splines. The right panel shows the corresponding fitting curves, together with the truth and the noised observations.

The average results based on 100 repetitions are summarized in Table 9. The table shows that we can obtain better performance in the high noise cases, and comparable results in the smaller noise scenarios.




---

# A. 6 Different Curves for Testing the Monotonicity 



Figure 21: Different curves for testing the monotonicity.

## B More GO Analysis

Figure 22 is the same as Figure 8except that panel (d) displays the GO terms identified by the interaction of DE genes and ME genes (the complementary of nME genes). Similar to DE genes, the interaction of DE genes and ME genes failed to identify significant GO terms.




---



Figure 22: GO enrichment analysis on the Paul et al. (2015) dataset of four gene sets ((a): nME gene set; (b): DE gene set; (c): the intersection of nME and DE genes; (d): the intersection of ME and DE genes) with BH FDR cutoff $\alpha=0.05$. The numbers of genes are noted in the title of each subfigure. The enriched GO terms are sorted by the adjusted p-value. (b) and (d) are left empty deliberately since no significant GO terms are selected.

For the liver dataset, the GO terms identified by different gene sets are shown in Figure 23. Most GO terms selected by the DE genes (Figure 23b) and by the ME\&DE genes (Figure 23d) are the same. The numbers of different GO terms are illustrated in the Venn diagram of Figure 24.




---



Figure 23: GO enrichment analysis on the liver dataset of four gene sets ((a): nME gene set; (b): DE gene set; (c): the intersection of nME and DE genes; (d): the intersection of ME and DE genes) with BH FDR cutoff $\alpha=0.05$. The numbers of genes are noted in the title of each subfigure. The enriched GO terms are sorted by the adjusted p-value. (b) is left empty deliberately since no significant GO terms are selected.




---



Figure 25: GO terms identified by DE genes but not ME genes.




---



Figure 26: GO terms identified by ME genes but not DE genes.




---

# C Theoretical proofs of some basic propositions 

## C. 1 A proposition

Proposition 7. Suppose $f(x)$ is a univariate continuous function in an interval $I$, there exists a decomposition

$$
f(x)=f^{\mathrm{up}}(x)+f^{\mathrm{down}}(x)
$$

where $f^{\text {up }}(x)$ and $f^{\text {down }}(x)$ are continuous increasing and decreasing functions, respectively.
Proof. Decompose the interval $I$ as

$$
I=\cup_{k=1}^{n}\left[a_{2 k-1}, a_{2 k}\right]
$$

Without loss of generality, suppose $f(x)$ is increasing in $\left[a_{2 k-1}, a_{2 k}\right]$ and decreasing in $\left[a_{2 k}, a_{2 k+1}\right]$. Then one feasible decomposition is

$$
f^{\text {up }}(x)= \begin{cases}f(x) & x \in\left[a_{1}, a_{2}\right] \\ f\left(a_{2}\right) & x \in\left[a_{2}, a_{3}\right] \\ f(x)-f\left(a_{3}\right)+f\left(a_{2}\right) & x \in\left[a_{3}, a_{4}\right] \\ f\left(a_{4}\right)-f\left(a_{3}\right)+f\left(a_{2}\right) & x \in\left[a_{4}, a_{5}\right] \\ \cdots & \cdots \\ f(x)+\sum_{i=2}^{k}\left(f\left(a_{2 i-2}\right)-f\left(a_{2 i-1}\right)\right) & x \in\left[a_{2 k-1}, a_{2 k}\right], k \geq 2 \\ f\left(a_{2 k}\right)+\sum_{i=2}^{k}\left(f\left(a_{2 i-2}\right)-f\left(a_{2 i-1}\right)\right) & x \in\left[a_{2 k}, a_{2 k+1}\right], k \geq 2\end{cases}
$$

and $f^{\text {down }}(x)=f(x)-f^{\text {up }}(x)$.

## C. 2 Proposition 1

Proof. Consider the problem

$$
\begin{aligned}
\min _{\boldsymbol{\gamma}^{u}, \boldsymbol{\gamma}^{d}} & \left\|\boldsymbol{y}-\boldsymbol{B}\left(\boldsymbol{\gamma}^{u}+\boldsymbol{\gamma}^{d}\right)\right\|^{2} \\
\text { s.t. } & \gamma_{1}^{u} \leq \gamma_{2}^{u} \leq \cdots \leq \gamma_{J}^{u} ; \gamma_{1}^{d} \geq \gamma_{2}^{d} \geq \cdots \geq \gamma_{J}^{d} \\
& \boldsymbol{\gamma}^{u}+\boldsymbol{\gamma}^{d}=\hat{\boldsymbol{\gamma}}
\end{aligned}
$$

where $\hat{\boldsymbol{\gamma}}$ is the unconstrained solution. Since we can always decompose a vector into the sum of an increasing vector and a decreasing vector. For $2 \leq i \leq J$, let

$$
\begin{aligned}
& \hat{\gamma}_{i}^{u}=\hat{\gamma}_{i-1}^{u}+\left(\hat{\gamma}_{i}-\hat{\gamma}_{i-1}\right)^{+} \\
& \hat{\gamma}_{i}^{d}=\hat{\gamma}_{i-1}^{d}+\left(\hat{\gamma}_{i}-\hat{\gamma}_{i-1}\right)^{-}
\end{aligned}
$$

where $t^{+}=\max (0, t)$ and $t^{-}=\min (0, t)$. And

$$
\hat{\gamma}_{1}^{u}+\hat{\gamma}_{1}^{d}=\hat{\gamma}_{1}
$$

for example, take $\hat{\gamma}_{1}^{u}=\hat{\gamma}_{1}$ and $\hat{\gamma}_{1}^{d}=0$. Thus the constraints are feasible, i.e., non-empty, and then any solution would satisfy

$$
\hat{\boldsymbol{\gamma}}^{u}+\hat{\boldsymbol{\gamma}}^{d}=\hat{\boldsymbol{\gamma}}
$$




---

# C. 3 Proposition 2 

Proof. Here we only prove the second property since the first property has been incorporated into the proof for the main propositions in Sections D. 2 and G.3.

We can also put the constraint $\gamma \in \Upsilon$ into the Lagrangian form. Define

$$
\begin{aligned}
& A \triangleq\left[I_{J-1}\right]-\left[\begin{array}{c}
0 \\
I_{J-1}
\end{array}\right]=\left[\begin{array}{ccccc}
1 & -1 & 0 & \cdots & 0 \\
0 & 1 & -1 & \cdots & 0 \\
0 & 0 & 1 & \cdots & 0 \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
0 & 0 & 0 & \cdots & 1 \\
-1
\end{array}\right]_{(J-1) \times J} \\
& H \triangleq\left[\begin{array}{cc}
A & 0 \\
0 & -A
\end{array}\right]
\end{aligned}
$$

and the Lagrange form is

$$
\mathcal{L}_{\mathrm{ls}}(\gamma, \nu, \mu)=\|y-Z \gamma\|_{2}^{2}+2 \nu^{\mathrm{T}} H \gamma+\mu \gamma^{\mathrm{T}} W \gamma
$$

where $2(J-1)$-vector $\nu$ and scalar $\mu$ are the Lagrange multipliers, and factor 2 is just for convenient formulas after taking the first derivatives. Take the derivatives on the Lagrange form,

$$
-2 Z^{\mathrm{T}}(y-Z \gamma)+2 H^{\mathrm{T}} \nu+2 \mu W \gamma+2 \lambda\left[\begin{array}{l}
\boldsymbol{\Omega} \\
\boldsymbol{\Omega}
\end{array}\right] \gamma=0
$$

where if $\lambda=0$, it reduces to the cubic spline. Then

$$
\begin{aligned}
& -B_{i}^{\mathrm{T}}(y-Z \gamma)+H_{i}^{\mathrm{T}} \nu+\mu B_{i}^{\mathrm{T}} B\left(\gamma_{u}-\gamma_{d}\right)+\lambda \Omega_{i}\left(\gamma_{u}+\gamma_{d}\right)=0 \\
& -B_{i}^{\mathrm{T}}(y-Z \gamma)+H_{i+J}^{\mathrm{T}} \nu+\mu B_{i}^{\mathrm{T}} B\left(-\gamma_{u}+\gamma_{d}\right)+\lambda \Omega_{i}\left(\gamma_{u}+\gamma_{d}\right)=0
\end{aligned}
$$

Note that

$$
\sum_{i=1}^{J} H_{i}^{\mathrm{T}} \nu=0, \quad \text { and } \quad \sum_{i=1}^{J} H_{i+J}^{\mathrm{T}} \nu=0
$$

then we have

$$
\mu \mathbf{1}^{\mathrm{T}} B^{\mathrm{T}} B\left(\gamma_{u}-\gamma_{d}\right)=\mu \mathbf{1}^{\mathrm{T}} B^{\mathrm{T}} B\left(-\gamma_{u}+\gamma_{d}\right)
$$

which implies

$$
\mu \mathbf{1}^{\mathrm{T}} B\left(\gamma_{u}-\gamma_{d}\right)=\mu \mathbf{1}^{\mathrm{T}} B\left(-\gamma_{u}+\gamma_{d}\right)
$$

so

$$
2 \mu \mathbf{1}^{\mathrm{T}} B \gamma_{u}=2 \mu \mathbf{1}^{\mathrm{T}} B \gamma_{d}
$$

If $\mu=0$, by KKT condition, then $B \gamma_{u}-B \gamma_{d}=0$. If $\mu \neq 0$, then $\mathbf{1}^{\mathrm{T}} B \gamma_{u}=\mathbf{1}^{\mathrm{T}} B \gamma_{d}$.
Thus, $\mathbf{1}^{\mathrm{T}} B \gamma_{u}=\mathbf{1}^{\mathrm{T}} B \gamma_{d}$ always holds.




---

# D Proof of Proposition 3 

Lemma 1 (Chebyshev Sum Inequality). If $a_{1} \geq a_{2} \geq \cdots \geq a_{n}$, and $b_{1} \geq b_{2} \geq \cdots \geq b_{n}$, then

$$
n \sum_{k=1}^{n} a_{k} b_{k} \geq\left(\sum_{k=1}^{n} a_{k}\right)\left(\sum_{k=1}^{n} b_{k}\right)
$$

Proof. Since these two sequences are decreasing, then the sum

$$
S=\sum_{j=1}^{n} \sum_{k=1}^{n}\left(a_{j}-a_{k}\right)\left(b_{j}-b_{k}\right) \geq 0
$$

Note that

$$
\begin{aligned}
S & =\sum_{j=1}^{n}\left(n a_{j} b_{j}-b_{j} \sum_{k=1}^{n} a_{k}-a_{j} \sum_{k=1}^{n} b_{k}+\sum_{k=1}^{n} a_{k} b_{k}\right) \\
& =n \sum_{j=1}^{n} a_{j} b_{j}+n \sum_{k=1}^{n} a_{k} b_{k}-\sum_{j=1}^{n} b_{j} \sum_{k=1}^{n} a_{k}-\sum_{j=1}^{n} a_{j} \sum_{k=1}^{n} b_{k} \\
& =2 n \sum_{k=1}^{n} a_{k} b_{k}-2 \sum_{k=1}^{n} b_{k} \sum_{k=1}^{n} a_{k}
\end{aligned}
$$

hence

$$
n \sum_{k=1}^{n} a_{k} b_{k} \geq\left(\sum_{k=1}^{n} a_{k}\right)\left(\sum_{k=1}^{n} b_{k}\right)
$$

## D. 1 (i)

Proof. Suppose $\boldsymbol{\gamma}=\boldsymbol{\gamma}_{u}+\boldsymbol{\gamma}_{d}$ is increasing, then we have a decomposition in which $\boldsymbol{\gamma}_{d}$ is a vector with identical elements. Write the decomposition as $\boldsymbol{\gamma}=\boldsymbol{\gamma}_{u}+c \mathbf{1}$, where $c$ is a constant. If there exists a non-zero non-decreasing vector $\boldsymbol{\delta}$ such that the non-increasing part is not a constant, i.e.,

$$
\boldsymbol{\gamma}=\left(\boldsymbol{\gamma}_{u}+\boldsymbol{\delta}\right)+(c \mathbf{1}-\boldsymbol{\delta}) \triangleq \tilde{\boldsymbol{\gamma}}_{u}+\tilde{\boldsymbol{\gamma}}_{d}
$$

Then

$$
\left\|\boldsymbol{y}-\boldsymbol{B}\left(\boldsymbol{\gamma}_{u}+c \mathbf{1}\right)\right\|=\left\|\boldsymbol{y}-\boldsymbol{B}\left(\tilde{\boldsymbol{\gamma}}_{u}+\tilde{\boldsymbol{\gamma}}_{d}\right)\right\|
$$

and if we impose the roughness penalty, we have

$$
\left(\boldsymbol{\gamma}_{u}+\boldsymbol{\gamma}_{d}\right)^{T} \boldsymbol{\Omega}\left(\boldsymbol{\gamma}_{u}+\boldsymbol{\gamma}_{d}\right)=\left(\tilde{\boldsymbol{\gamma}}_{u}+\tilde{\boldsymbol{\gamma}}_{d}\right)^{T} \boldsymbol{\Omega}\left(\tilde{\boldsymbol{\gamma}}_{u}+\tilde{\boldsymbol{\gamma}}_{d}\right)
$$

So the first two terms in the Lagrange objective function (13) are the same, and we only need to compare the difference between these two components,

$$
\begin{aligned}
\left\|\boldsymbol{B}\left(\tilde{\boldsymbol{\gamma}}_{u}-\tilde{\boldsymbol{\gamma}}_{d}\right)\right\|_{2}^{2}- & \left\|\boldsymbol{B}\left(\boldsymbol{\gamma}_{u}-\boldsymbol{\gamma}_{d}\right)\right\|_{2}^{2} \\
& =\left(\tilde{\boldsymbol{\gamma}}_{u}-\tilde{\boldsymbol{\gamma}}_{d}-\left(\boldsymbol{\gamma}_{u}-\boldsymbol{\gamma}_{d}\right)\right)^{T} \boldsymbol{B}^{T} \boldsymbol{B}\left(\tilde{\boldsymbol{\gamma}}_{u}-\tilde{\boldsymbol{\gamma}}_{d}+\left(\boldsymbol{\gamma}_{u}-\boldsymbol{\gamma}_{d}\right)\right) \\
& =2 \boldsymbol{\delta}^{T} \boldsymbol{B}^{T} \boldsymbol{B}\left(2 \boldsymbol{\gamma}_{u}+2 \boldsymbol{\delta}-2 c \mathbf{1}\right) \\
& =4\left\{\boldsymbol{\delta}^{T} \boldsymbol{B}^{T} \boldsymbol{B} \boldsymbol{\delta}+\boldsymbol{\delta}^{T} \boldsymbol{B}^{T} \boldsymbol{B}\left(\boldsymbol{\gamma}_{u}-c \mathbf{1}\right)\right\}
\end{aligned}
$$




---

By Proposition 2, we have

$$
\mathbf{1}^{T} \boldsymbol{B} \gamma_{u}=\mathbf{1}^{T} \boldsymbol{B} \gamma_{d} \quad \mathbf{1}^{T} \boldsymbol{B} \tilde{\gamma}_{u}=\mathbf{1}^{T} \boldsymbol{B} \tilde{\gamma}_{d}
$$

then

$$
\mathbf{1}^{T} \boldsymbol{B}\left(\gamma_{u}-c \mathbf{1}\right)=\mathbf{1}^{T} \boldsymbol{B} \delta=0
$$

Let $a=\boldsymbol{B} \delta, b=\boldsymbol{B}\left(\gamma_{u}-c \mathbf{1}\right)$, then by Fact 1 ,

$$
a^{T} b \geq \frac{1}{n}\left(\mathbf{1}^{T} a\right)\left(\mathbf{1}^{T} b\right)=0
$$

And $\delta^{T} \boldsymbol{B}^{T} \boldsymbol{B} \delta>0$ for non-zero $\delta$, thus,

$$
\left\|\boldsymbol{B}\left(\tilde{\gamma}_{u}-\tilde{\gamma}_{d}\right)\right\|_{2}^{2}>\left\|\boldsymbol{B}\left(\gamma_{u}-\gamma_{d}\right)\right\|_{2}^{2}
$$

So if $\gamma_{u}+\gamma_{d}$ is increasing, the best decomposition is $\gamma_{d}=c \mathbf{1}$.
Note that

$$
\mathbf{1}^{T} \boldsymbol{B} \gamma_{u}=\mathbf{1}^{T} \boldsymbol{B} c \mathbf{1}=c \mathbf{1}^{T} \mathbf{1}
$$

the constant $c$ is

$$
c=\frac{\mathbf{1}^{T} \boldsymbol{B} \gamma_{u}}{n}
$$

# D. 2 (ii) 

Proof. Take the derivatives on the Lagrange form,

$$
-2 \boldsymbol{Z}^{T}(\boldsymbol{y}-\boldsymbol{Z} \gamma)+2 \boldsymbol{H}^{T} \nu+2 \mu \boldsymbol{W} \gamma=0
$$

then

$$
\begin{aligned}
\hat{\gamma} & =\left(\boldsymbol{Z}^{T} \boldsymbol{Z}+\mu \boldsymbol{W}\right)^{-1}\left(\boldsymbol{Z}^{T} \boldsymbol{y}-\boldsymbol{H}^{T} \nu\right) \\
& \triangleq\left(\boldsymbol{Z}^{T} \boldsymbol{Z}+\mu \boldsymbol{W}\right)^{-1} \boldsymbol{Z}^{T} \boldsymbol{y}-\left(\boldsymbol{Z}^{T} \boldsymbol{Z}+\mu \boldsymbol{W}\right)^{-1} \xi
\end{aligned}
$$

where $\xi \triangleq \boldsymbol{H}^{T} \nu$. Note that

$$
\left(\boldsymbol{Z}^{T} \boldsymbol{Z}+\mu \boldsymbol{W}\right)^{-1}=\left[\begin{array}{cc}
1+\mu & 1-\mu \\
1-\mu & 1+\mu
\end{array}\right]^{-1} \otimes\left(\boldsymbol{B}^{T} \boldsymbol{B}\right)^{-1}=\frac{1}{4 \mu}\left[\begin{array}{cc}
\mu+1 & \mu-1 \\
\mu-1 & \mu+1
\end{array}\right] \otimes\left(\boldsymbol{B}^{T} \boldsymbol{B}\right)^{-1}
$$

then
$\left(\boldsymbol{Z}^{T} \boldsymbol{Z}+\mu \boldsymbol{W}\right)^{-1} \boldsymbol{Z}^{T} \boldsymbol{y}=\left\{\frac{1}{4 \mu}\left[\begin{array}{cc}\mu+1 & \mu-1 \\ \mu-1 & \mu+1\end{array}\right]\left[\begin{array}{l}1 \\ 1\end{array}\right]\right\} \otimes\left(\boldsymbol{B}^{T} \boldsymbol{B}\right)^{-1} \boldsymbol{B}^{T} \boldsymbol{y}=\frac{1}{2}\left[\begin{array}{l}1 \\ 1\end{array}\right] \otimes\left(\boldsymbol{B}^{T} \boldsymbol{B}\right)^{-1} \boldsymbol{B}^{T} y$.
Consider the $i$-th element of (23),

$$
-\boldsymbol{Z}_{i}^{T}(\boldsymbol{y}-\boldsymbol{Z} \gamma)+\boldsymbol{H}_{i}^{T} \nu+\mu \boldsymbol{W}_{i}^{T} \gamma=0
$$

where $\boldsymbol{Z}_{i}, \boldsymbol{H}_{i}, \boldsymbol{W}_{i}$ are the $i$-th column of $\boldsymbol{Z}, \boldsymbol{H}, \boldsymbol{W}$, respectively. Note that for $1 \leq i \leq J$,

$$
\boldsymbol{W}_{i}=\left[\begin{array}{c}
\boldsymbol{B}^{T} \boldsymbol{B}_{i} \\
-\boldsymbol{B}^{T} \boldsymbol{B}_{i}
\end{array}\right], \quad \boldsymbol{W}_{i+J}=\left[\begin{array}{c}
-\boldsymbol{B}^{T} \boldsymbol{B}_{i} \\
\boldsymbol{B}^{T} \boldsymbol{B}_{i}
\end{array}\right]
$$




---

and

$$
Z_{i}=B_{i}, \quad Z_{i+J}=B_{i}
$$

where $B_{i}$ is the $i$-th column of $B$. Then (24) turns out to be

$$
\begin{aligned}
& -B_{i}^{T}(y-Z \gamma)+H_{i}^{T} \nu+\mu B_{i}^{T} B\left(\gamma^{u}-\gamma^{d}\right)=0 \\
& -B_{i}^{T}(y-Z \gamma)+H_{i+J}^{T} \nu+\mu B_{i}^{T} B\left(-\gamma^{u}+\gamma^{d}\right)=0
\end{aligned}
$$

$(25)+(26)$ yields

$$
\left(H_{i}^{T}-H_{i+J}^{T}\right) \nu=-2 \mu B_{i}^{T} B\left(\gamma^{u}-\gamma^{d}\right)
$$

and $(25)-(26)$ yields

$$
\left(H_{i}^{T}+H_{i+J}^{T}\right) \nu=2 B_{i}^{T}(y-Z \gamma)
$$

If there is no ties in the solution, i.e.,

$$
\gamma_{1}^{u}<\gamma_{2}^{u}<\cdots<\gamma_{J}^{u}, \quad \gamma_{1}^{d}>\gamma_{2}^{d}>\cdots>\gamma_{J}^{d}
$$

by the KKT condition, $\nu=0$, and then (27) implies $\mu=0$. Then it reduces to unconstrained B-spline fitting. This argument proves the first point of Proposition 2.

If

$$
\gamma_{1}^{u}<\gamma_{2}^{u}<\ldots<\gamma_{J}^{u}
$$

then from (27), we have

$$
\xi_{i+J}=2 \mu B_{i}^{T} B\left(\gamma^{u}-\gamma^{d}\right)
$$

then

$$
\xi=\left[\begin{array}{l}
0 \\
1
\end{array}\right] \otimes 2 \mu B^{T} B\left(\gamma^{u}-\gamma^{d}\right)
$$

it follows that

$$
\left(Z^{T} Z+\mu W\right)^{-1} \xi=\frac{1}{2}\left[\begin{array}{c}
\mu-1 \\
\mu+1
\end{array}\right] \otimes\left(\gamma^{u}-\gamma^{d}\right)
$$

So

$$
\left[\begin{array}{l}
\gamma^{u} \\
\gamma^{d}
\end{array}\right]=\frac{1}{2}\left[\begin{array}{c}
\left(B^{T} B\right)^{-1} B^{T} y-(\mu-1)\left(\gamma^{u}-\gamma^{d}\right) \\
\left(B^{T} B\right)^{-1} B^{T} y-(\mu+1)\left(\gamma^{u}-\gamma^{d}\right)
\end{array}\right]
$$

both yield

$$
(\mu+1) \gamma^{u}-(\mu-1) \gamma^{d}=\left(B^{T} B\right)^{-1} B^{T} y
$$

On the other hand, from (25), we have

$$
-B^{T}(y-Z \gamma)+\mu B^{T} B\left(\gamma^{u}-\gamma^{d}\right)=0
$$

that is,

$$
\left(\gamma^{u}+\gamma^{d}\right)+\mu\left(\gamma^{u}-\gamma^{d}\right)=\left(B^{T} B\right)^{-1} B^{T} y
$$

that is,

$$
(\mu+1) \gamma^{u}-(\mu-1) \gamma^{d}=\left(B^{T} B\right)^{-1} B^{T} y \triangleq \hat{\gamma}_{l s}
$$

Incorporate with the result in Section D.1, we have

$$
\gamma^{d}=c_{1}, \gamma^{u}=\frac{1}{\mu+1} \hat{\gamma}_{l s}+\frac{\mu-1}{\mu+1} c_{1}
$$




---

# D. 3 (iii) 

Proof. Note that

$$
\left\{\begin{array}{l}
\xi_{1}=\nu_{1} \\
\xi_{2}=\nu_{2}-\nu_{1} \\
\vdots \\
\xi_{J-1}=\nu_{J-1}-\nu_{J-2} \\
\xi_{J}=-\nu_{J-1}
\end{array}\right.
$$

If $\hat{\gamma}_{1}^{u}<\cdots<\hat{\gamma}_{k_{1}}^{u}=\cdots=\hat{\gamma}_{k_{2}}^{u}<\cdots<\hat{\gamma}_{k_{2 m-1}}^{u}=\cdots=\hat{\gamma}_{k_{2 m}}^{u}<\hat{\gamma}_{J}$, then

$$
\left\{\begin{array}{l}
\nu_{1}=\cdots=\nu_{k_{1}-1}=0 \\
\vdots \\
\nu_{k_{2 m}-2}=\cdots=\nu_{k_{2 m}-1}=0 \\
\nu_{k_{2 m}}=\cdots=\nu_{J-1}=0
\end{array} \Longrightarrow \begin{array}{l}
\xi_{1}=\cdots=\xi_{k_{1}-1}=0 \\
\vdots \\
\sum_{i=k_{1}}^{k_{2}-1} \xi_{i}=0 \\
\vdots \\
\sum_{i=k_{2 m-1}}^{k_{2 m}-1} \xi_{i}=0 \\
\xi_{k_{2 m}}=\cdots=\xi_{J}=0
\end{array}\right.
$$

Thus,

$$
\begin{aligned}
& B_{1}^{T} y=(\mu+1) B_{1}^{T} B \gamma^{u}-(\mu-1) B_{1}^{T} B \gamma^{d} \\
& \vdots \\
& B_{k_{1}-1}^{T} y=(\mu+1) B_{k_{1}-1}^{T} B \gamma^{u}-(\mu-1) B_{k_{1}-1}^{T} B \gamma^{d} \\
& \sum_{i=k_{1}}^{k_{2}-1} B_{i}^{T} y=(\mu+1) \sum_{i=k_{1}}^{k_{2}-1} B_{i}^{T} B \gamma^{u}-(\mu-1) \sum_{i=k_{1}}^{k_{2}-1} B_{i}^{T} B \gamma^{d} \\
& \vdots \\
& \sum_{i=k_{2 m-2}}^{k_{2 m-1}} B_{i}^{T} y=(\mu+1) \sum_{i=k_{2 m-2}}^{k_{2 m-1}} B_{i}^{T} B \gamma^{u}-(\mu-1) \sum_{i=k_{2 m-2}}^{k_{2 m-1}} B_{i}^{T} B \gamma^{d} \\
& B_{k_{2 m}}^{T} y=(\mu+1) B_{k_{2 m}}^{T} B \gamma^{u}-(\mu-1) B_{k_{2 m}}^{T} B \gamma^{d} \\
& \vdots \\
& B_{J}^{T} y=(\mu+1) B_{J}^{T} B \gamma^{u}-(\mu-1) B_{J}^{T} B \gamma^{d}
\end{aligned}
$$

Then

$$
G^{T} y=(\mu+1) G^{T} B \gamma^{u}-(\mu-1) G^{T} B \gamma^{d}
$$




---

where

$$
\mathbf{G}=\left[\begin{array}{cccc}
\mathbf{I}_{k_{1}-1} & & & \\
\mathbf{1}_{k_{2}-k_{1}+1}^{T} & \ddots & & \\
& \ddots & \mathbf{I}_{k_{2 m-1}-k_{2 m-2}-1} & \\
& & \mathbf{1}_{k_{2 m}-k_{2 m-1}+1}^{T} & \\
& & & \mathbf{I}_{J-k_{2 m}}
\end{array}\right]
$$

Let $\boldsymbol{\gamma}^{u}=\mathbf{G}^{T} \boldsymbol{\beta}$, where $\boldsymbol{\beta}$ is the sub-vector of $\boldsymbol{\gamma}^{u}$ constructed by the unique elements. Since $\boldsymbol{\gamma}^{d}=\mathrm{c} \mathbf{1}$, and $\mathbf{G}^{T} \mathbf{1}=\mathbf{1}$, then

$$
\mathbf{G}^{T} \mathbf{y}=(\mu+1) \mathbf{G}^{T} \mathbf{B G}^{T} \boldsymbol{\beta}-(\mu-1) \mathbf{G}^{T} \mathbf{B G}^{T} \boldsymbol{\gamma}^{d} \mathrm{c} \mathbf{1}
$$

then

$$
\boldsymbol{\beta}=\frac{1}{\mu+1}\left(\mathbf{G}^{T} \mathbf{B G}^{T}\right)^{-1} \mathbf{G}^{T} \mathbf{y}+\frac{\mu-1}{\mu+1} \mathrm{c} \mathbf{1}
$$

thus


# D. 4 Corollary 1 

The monotone decomposition for decreasing functions can be straightforward to derive, as summarized in Corollary 1.

Corollary 1. Let $\hat{\boldsymbol{\gamma}}=\left(\hat{\boldsymbol{\gamma}}^{u}, \hat{\boldsymbol{\gamma}}^{d}\right)$ be the monotone decomposition to problem (6). Suppose $\hat{\boldsymbol{\gamma}}^{u}+\hat{\boldsymbol{\gamma}}^{d}$ is decreasing, then
(i) $\hat{\boldsymbol{\gamma}}^{u}$ is a vector with identical elements;
(ii) if $\hat{\gamma}_{1}^{d}>\cdots>\hat{\gamma}_{k_{1}}^{d}=\cdots=\hat{\gamma}_{k_{2}}^{d}>\cdots>\hat{\gamma}_{k_{2 m-1}}^{d}=\cdots=\hat{\gamma}_{k_{2 m}}^{d}>\cdots>\hat{\gamma}_{J}$, where $1 \leq k_{1} \leq k_{2} \leq$ $\cdots \leq k_{2 m-1} \leq k_{2 m} \leq J$, then

$$
\hat{\boldsymbol{\gamma}}^{d}=\frac{1}{\mu+1} \mathbf{G}^{T}\left(\mathbf{G}^{T} \mathbf{B G}^{T}\right)^{-1} \mathbf{G}^{T} \mathbf{y}+\frac{\mu-1}{\mu+1} c \mathbf{1}, \quad \hat{\boldsymbol{\gamma}}^{u}=1^{T} \mathbf{B} \hat{\boldsymbol{\gamma}}^{d} / n
$$

Proof. With $(\mathbf{X}, \mathbf{y})$, the solution is $\hat{\boldsymbol{\gamma}}^{u}+\hat{\boldsymbol{\gamma}}^{d}$, then the solution for $(\mathbf{X},-\mathbf{y})$ is $-\hat{\boldsymbol{\gamma}}^{u}-\hat{\boldsymbol{\gamma}}^{d}$.
If $\boldsymbol{\gamma}^{u}+\boldsymbol{\gamma}^{d}$ is decreasing, then $-\boldsymbol{\gamma}^{u}-\boldsymbol{\gamma}^{d}$ is increasing. Note that $-\boldsymbol{\gamma}^{u}$ is non-increasing, and $-\boldsymbol{\gamma}^{d}$ is non-decreasing, then by Proposition 1, firstly, $-\boldsymbol{\gamma}^{u}$ is a constant, and hence $\boldsymbol{\gamma}^{u}$ is a constant. If $\hat{\gamma}_{1}^{d}>\cdots>\hat{\gamma}_{k_{1}}^{d}=\cdots=\hat{\gamma}_{k_{2}}^{d}>\cdots>\hat{\gamma}_{k_{2 m-1}}^{d}=\cdots=\hat{\gamma}_{k_{2 m}}^{d}>\hat{\gamma}_{J}$, then

$$
-\hat{\gamma}_{1}^{d}<\cdots<-\hat{\gamma}_{k_{1}}^{d}=\cdots=-\hat{\gamma}_{k_{2}}^{d}<\cdots<-\hat{\gamma}_{k_{2 m-1}}^{d}=\cdots=-\hat{\gamma}_{k_{2 m}}^{d}<-\hat{\gamma}_{J}
$$

Thus,

$$
-\hat{\boldsymbol{\gamma}}^{d}=\frac{1}{\mu+1} \mathbf{G}\left(\mathbf{G}^{T} \mathbf{B G}^{T}\right)^{-1} \mathbf{G}^{T}(-\mathbf{y})+\frac{\mu-1}{\mu+1} \tilde{c} \mathbf{1}, \quad \tilde{c}=\mathbf{1}^{T} \mathbf{B}\left(-\boldsymbol{\gamma}^{d}\right) / n
$$

it follows that

$$
\hat{\boldsymbol{\gamma}}^{d}=\frac{1}{\mu+1} \mathbf{G}\left(\mathbf{G}^{T} \mathbf{B G}^{T}\right)^{-1} \mathbf{G}^{T} \mathbf{y}+\frac{\mu-1}{\mu+1} c \mathbf{1}, \quad c=\mathbf{1}^{T} \mathbf{B} \boldsymbol{\gamma}^{d} / n, \quad \hat{\boldsymbol{\gamma}}^{u}=c \mathbf{1}
$$




---

# E A Side Product: Unimodal Functions 

We explore the solution for more general unimodal functions, as summarized in Proposition 8. Specifically, the second point of Proposition 3 can be viewed as a special instance with $k=\ell=1$ of Proposition 8.

Proposition 8. Let $\hat{\gamma}=\left(\hat{\gamma}^{u}, \hat{\gamma}^{d}\right)$ be the monotone decomposition to problem (8). If

$$
\begin{gathered}
\hat{\gamma}_{1}^{u}=\hat{\gamma}_{2}^{u}=\cdots=\hat{\gamma}_{k}^{u}<\hat{\gamma}_{k+1}^{u}<\cdots<\hat{\gamma}_{J}^{u} \\
\hat{\gamma}_{1}^{d}>\hat{\gamma}_{2}^{d}>\cdots>\hat{\gamma}_{\ell}^{d}=\hat{\gamma}_{\ell+1}^{d}=\cdots=\hat{\gamma}_{J}^{d}
\end{gathered}
$$

suppose $\ell \leq k$, then

$$
\left[\begin{array}{c}
I_{\ell-1} \\
1_{k-\ell+1} \\
I_{J-k}
\end{array}\right] B^{T} y=A B^{T} B \hat{\gamma}^{u}+(2 I-A) B^{T} B \hat{\gamma}^{d}
$$

where

$$
A=\left[\begin{array}{c}
(1-\mu) I_{\ell-1} \\
2 \mu 1_{\ell-1}^{\top} \\
1+\mu \\
(1+\mu) I_{J-k}
\end{array}\right]
$$

Proof. If

$$
\gamma_{1}^{u}=\gamma_{2}^{u}=\cdots=\gamma_{k}^{u}<\gamma_{k+1}^{u}<\cdots<\gamma_{J}^{u}
$$

and

$$
\gamma_{1}^{d}>\gamma_{2}^{d}>\cdots>\gamma_{\ell}^{d}=\gamma_{\ell+1}^{d}=\cdots=\gamma_{J}^{d}
$$

Suppose $\ell \leq k$, then

$$
\nu_{k}=\nu_{k+1}=\cdots=\nu_{J-1}=0
$$

and

$$
\nu_{J-1+i}=0, i=1, \ldots, \ell-1
$$

Then from (28), we have $\xi_{i}=0, k+1 \leq i \leq J$, and then

$$
\begin{gathered}
\sum_{i=1}^{k} B_{i}^{T} y=(\mu+1) \sum_{i=1}^{k} B_{i}^{T} B \gamma^{u}-(\mu-1) \sum_{i=1}^{k} B_{i}^{T} B \gamma^{d} \\
B_{i}^{T} y=(\mu+1) B_{i}^{T} B \gamma^{u}-(\mu-1) B_{i}^{T} B \gamma^{d} \quad k+1 \leq i \leq J
\end{gathered}
$$

Similarly, $\xi_{i+J}=0,1 \leq i \leq \ell-1$, and hence

$$
\begin{gathered}
B_{i}^{T} y=(\mu+1) B_{i}^{T} B \gamma^{d}-(\mu-1) B_{i}^{T} B \gamma^{u} \quad 1 \leq i \leq \ell-1 \\
\sum_{i=\ell}^{J} B_{i}^{T} y=(\mu+1) \sum_{i=\ell}^{J} B_{i}^{T} B \gamma^{d}-(\mu-1) \sum_{i=\ell}^{J} B_{i}^{T} B \gamma^{u}
\end{gathered}
$$

Note that

$$
\begin{aligned}
\sum_{i=1}^{J} B_{i}^{T} y & =(\mu+1) \sum_{i=1}^{J} B_{i}^{T} B \gamma^{u}-(\mu-1) \sum_{i=1}^{J} B_{i}^{T} B \gamma^{d} \\
& =(\mu+1) \sum_{i=1}^{J} B_{i}^{T} B \gamma^{d}-(\mu+1) \sum_{i=1}^{J} B_{i}^{T} B \gamma^{u}
\end{aligned}
$$




---

then $(29)+(32)-(33)$ yields

$$
\begin{aligned}
\sum_{\ell}^{k} \mathbf{B}_{i}^{T} \mathbf{y} & =\sum_{i=1}^{k} \mathbf{B}_{i}^{T} \mathbf{y}+\sum_{i=\ell}^{J} \mathbf{B}_{i}^{T} \mathbf{y}-\sum_{i=1}^{J} \mathbf{B}_{i}^{T} \mathbf{y} \\
& =(\mu+1) \sum_{i=1}^{k} \mathbf{B}_{i}^{T} \mathbf{B} \boldsymbol{\gamma}^{u}-(\mu-1) \sum_{i=1}^{k} \mathbf{B}_{i}^{T} \mathbf{B} \gamma^{d}+ \\
& (\mu+1) \sum_{i=\ell}^{J} \mathbf{B}_{i}^{T} \mathbf{B} \boldsymbol{\gamma}^{d}-(\mu-1) \sum_{i=\ell}^{J} \mathbf{B}_{i}^{T} \mathbf{B} \gamma^{u}- \\
& {\left[(1-\mu) \mathbf{1}^{T} \mathbf{B} \boldsymbol{\gamma}^{u}+(\mu+1) \mathbf{1}^{T} \mathbf{B} \boldsymbol{\gamma}^{d}\right] } \\
& =(\mu+1) \sum_{i=1}^{k} \mathbf{B}_{i}^{T} \mathbf{B} \boldsymbol{\gamma}^{u}-(\mu-1) \sum_{i=1}^{k} \mathbf{B}_{i}^{T} \mathbf{B} \gamma^{d}+ \\
& (\mu-1) \sum_{i=1}^{\ell-1} \mathbf{B}_{i}^{T} \mathbf{B} \gamma^{u}-(\mu+1) \sum_{i=1}^{\ell-1} \mathbf{B}_{i}^{T} \mathbf{B} \gamma^{d} \\
& =2 \mu \sum_{i=1}^{\ell-1} \mathbf{B}_{i}^{T} \mathbf{B} \gamma^{u}+(\mu+1) \sum_{i=\ell}^{k} \mathbf{B}_{i}^{T} \mathbf{B} \gamma^{u}-2 \mu \sum_{i=1}^{\ell-1} \mathbf{B}_{i}^{T} \mathbf{B} \gamma^{d}-(\mu-1) \sum_{i=\ell}^{k} \mathbf{B}_{i}^{T} \mathbf{B} \gamma^{d}
\end{aligned}
$$

then
$\left[\begin{array}{c}\mathbf{B}_{1}^{T} \mathbf{y} \\ \vdots \\ \mathbf{B}_{\ell-1}^{T} \mathbf{y} \\ \sum_{i=\ell}^{k} \mathbf{B}_{i}^{T} \mathbf{y} \\ \mathbf{B}_{k+1}^{T} \mathbf{y} \\ \vdots \\ \mathbf{B}_{J}^{T} \mathbf{y}\end{array}\right]=\left[\begin{array}{ccccccc}1-\mu & \ldots & 0 & 0 & 0 & \ldots & 0 \\ \vdots & \ddots & 0 & 0 & 0 & \ldots & 0 \\ 0 & \ldots & 1-\mu & 0 & 0 & \ldots & 0 \\ 2 \mu & \ldots & 2 \mu & 1+\mu & 0 & \ldots & 0 \\ 0 & \ldots & 0 & 0 & 1+\mu & \ldots & 0 \\ \vdots & \vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & \ldots & 0 & 0 & 0 & \ldots & 1+\mu\end{array}\right] \mathbf{B}^{T} \mathbf{B} \boldsymbol{\gamma}^{u}+$



If $\ell=k$, then

$$
\mathbf{B}^{T} \mathbf{y}=\mathbf{A B}^{T} \mathbf{B} \gamma^{u}+(2 \mathbf{I}-\mathbf{A}) \mathbf{B}^{T} \mathbf{B} \gamma^{d}
$$




---

# F Proof of Proposition 4 

Proof. The fitting vector is

$$
\begin{aligned}
\hat{\boldsymbol{f}} & =\boldsymbol{B} \hat{\boldsymbol{\gamma}}_{u}+\boldsymbol{B} \hat{\boldsymbol{\gamma}}_{d} \\
& =\frac{1}{\mu+1} \boldsymbol{B} \boldsymbol{G}^{T}\left(\boldsymbol{G}^{T} \boldsymbol{B}^{T} \boldsymbol{B} \boldsymbol{G}^{T}\right)^{-1} \boldsymbol{G}^{T} \boldsymbol{y}+\frac{2 \mu}{\mu+1} \frac{\mathbf{1}_{n}^{T} \hat{\boldsymbol{f}}}{2 n} \mathbf{1}_{n} \\
& \triangleq k \boldsymbol{A} \boldsymbol{y}+\frac{1}{n}(1-k) \mathbf{1}_{n}^{T} \hat{\boldsymbol{f}} \mathbf{1}_{n}
\end{aligned}
$$

then

$$
\mathbf{1}_{n}^{T} \hat{\boldsymbol{f}}=k \mathbf{1}_{n}^{T} \boldsymbol{A} \boldsymbol{y}+(1-k) \mathbf{1}_{n}^{T} \hat{\boldsymbol{f}}
$$

It follows that

$$
\mathbf{1}_{n}^{T} \hat{\boldsymbol{f}}=\mathbf{1}_{n}^{T} \boldsymbol{A} \boldsymbol{y}
$$

then

$$
\hat{\boldsymbol{f}}=k \boldsymbol{A} \boldsymbol{y}+\frac{1-k}{n} \mathbf{1}_{n}^{T} \boldsymbol{A} \boldsymbol{y} \mathbf{1}_{n}=\left[k \boldsymbol{I}+\frac{1-k}{n} \mathbf{1}_{n} \mathbf{1}_{n}^{T}\right] \boldsymbol{A} \boldsymbol{y}
$$

Note that $\boldsymbol{G}$ depends on $\boldsymbol{y}$, and hence $\boldsymbol{A}$ also depends on $\boldsymbol{y}$. Take expectation on (36) and by the law of total expectation, we have

$$
\mathbb{E} \hat{\boldsymbol{f}}=\mathbb{E}[\mathbb{E}[\hat{\boldsymbol{f}} \mid \boldsymbol{G}]]=\mathbb{E}\left[k \boldsymbol{A} \boldsymbol{f}+\frac{1-k}{n} \mathbf{1}_{n}^{T} \boldsymbol{A} \boldsymbol{f} \mathbf{1}_{n}\right]
$$

Note that $\boldsymbol{A} \boldsymbol{A}^{T}=\boldsymbol{A}=\boldsymbol{A}^{T}$ and $\mathbf{1}_{n}=\boldsymbol{B} \mathbf{1}_{J}=\boldsymbol{G}^{T} \mathbf{1}_{g}=\boldsymbol{B}^{T} \boldsymbol{G}^{T} \mathbf{1}_{g}$, then

$$
\begin{aligned}
\mathbf{1}_{n}^{T} \boldsymbol{A} & =\mathbf{1}_{n}^{T} \boldsymbol{B} \boldsymbol{G}^{T}\left(\boldsymbol{G}^{T} \boldsymbol{B}^{T} \boldsymbol{B} \boldsymbol{G}^{T}\right)^{-1} \boldsymbol{G}^{T} \\
& =\mathbf{1}_{g}^{T} \boldsymbol{G}^{T} \boldsymbol{B}^{T} \boldsymbol{B} \boldsymbol{G}^{T}\left(\boldsymbol{G}^{T} \boldsymbol{B}^{T} \boldsymbol{B} \boldsymbol{G}^{T}\right)^{-1} \boldsymbol{G}^{T} \\
& =\mathbf{1}_{g}^{T} \boldsymbol{G}^{T} \\
& =\mathbf{1}_{n}^{T}
\end{aligned}
$$

and hence $\mathbf{1}_{n}^{T} \boldsymbol{A} \boldsymbol{A}^{T} \mathbf{1}_{n}=n$. It follows that

$$
\mathbb{E} \hat{\boldsymbol{f}}=k \boldsymbol{E} \boldsymbol{A} \boldsymbol{f}+\frac{1-k}{n} \mathbf{1}_{n}^{T} \boldsymbol{f} \mathbf{1}_{n}
$$

The square of bias is

$$
\begin{aligned}
\|\boldsymbol{f}-\mathbb{E} \hat{\boldsymbol{f}}\|^{2} & =\left\|\boldsymbol{f}-k \mathbb{E} \boldsymbol{A} \boldsymbol{f}-\frac{1-k}{n} \mathbf{1}_{n}^{T} \boldsymbol{f} \mathbf{1}_{n}\right\|^{2} \\
& =\boldsymbol{f}^{T}(I-k \mathbb{E} \boldsymbol{A})^{2} \boldsymbol{f}-\frac{2(1-k)}{n} \boldsymbol{f}^{T}(I-k \mathbb{E} \boldsymbol{A}) \mathbf{1}_{n}^{T} \boldsymbol{f} \mathbf{1}_{n}+\frac{(1-k)^{2}}{n^{2}}\left(\mathbf{1}_{n}^{T} \boldsymbol{f}\right)^{2} \mathbf{1}_{n}^{T} \mathbf{1}_{n} \\
& =\boldsymbol{f}^{T}(I-k \mathbb{E} \boldsymbol{A})^{2} \boldsymbol{f}-\frac{2(1-k)}{n}\left(\mathbf{1}_{n}^{T} \boldsymbol{f}\right) \boldsymbol{f}^{T}(I-k \mathbb{E} \boldsymbol{A}) \mathbf{1}_{n}+\frac{(1-k)^{2}}{n}\left(\mathbf{1}_{n}^{T} \boldsymbol{f}\right)^{2} \\
& =\boldsymbol{f}^{T}(I-k \mathbb{E} \boldsymbol{A})^{2} \boldsymbol{f}-\frac{(1-k)^{2}}{n}\left(\mathbf{1}_{n}^{T} \boldsymbol{f}\right)^{2} \\
& =\boldsymbol{f}^{T} \boldsymbol{f}-2 k \boldsymbol{f}^{T} \mathbb{E} \boldsymbol{A} \boldsymbol{f}+k^{2} \boldsymbol{f}^{T}[\mathbb{E} \boldsymbol{A}]^{2} \boldsymbol{f}-\frac{(1-k)^{2}}{n}\left(\mathbf{1}_{n}^{T} \boldsymbol{f}\right)^{2}
\end{aligned}
$$

Note that

$$
[\mathbb{E} \boldsymbol{A}]^{2}=\mathbb{E} \boldsymbol{A}^{2}-\operatorname{Var}(\boldsymbol{A})
$$




---

and $\mathbf{A}^{2}=\mathbf{A}$, we can write

$$
k^{2} \mathbf{f}^{\top}[\mathbb{E} \mathbf{A}]^{2} \mathbf{f}=k^{2} \mathbf{f}^{\top}[\mathbb{E} \mathbf{A}-\operatorname{Var}(\mathbf{A})] \mathbf{f}
$$

It follows that

$$
\begin{aligned}
\|\mathbf{f}-\mathbb{E} \hat{\mathbf{f}}\|^{2} & =\mathbf{f}^{\top} \mathbb{E} \mathbf{A} \mathbf{f}-2 k \mathbf{f}^{\top} \mathbb{E} \mathbf{A} \mathbf{f}+k^{2} \mathbf{f}^{\top} \mathbb{E} \mathbf{A} \mathbf{f}+\mathbf{f}^{\top} \mathbf{f}-\mathbf{f}^{\top} \mathbb{E} \mathbf{A} \mathbf{f}-k^{2} \mathbf{f}^{\top} \operatorname{Var}(\mathbf{A}) \mathbf{f}-\frac{(1-k)^{2}}{n}\left(\mathbf{1}_{n}^{\top} \mathbf{f}\right)^{2} \\
& =(1-k)^{2} \mathbf{f}^{\top} \mathbb{E} \mathbf{A} \mathbf{f}+\mathbf{f}^{\top}(I-\mathbb{E} \mathbf{A}) \mathbf{f}-k^{2} \mathbf{f}^{\top} \operatorname{Var}(\mathbf{A}) \mathbf{f}-\frac{(1-k)^{2}}{n}\left(\mathbf{1}_{n}^{\top} \mathbf{f}\right)^{2} \\
& =(1-k)^{2}\left(\mathbf{f}^{\top} \mathbb{E} \mathbf{A} \mathbf{f}-\frac{\left(\mathbf{1}_{n}^{\top} \mathbf{f}\right)^{2}}{n}\right)+\mathbf{f}^{\top}(I-\mathbb{E} \mathbf{A}) \mathbf{f}-k^{2} \mathbf{f}^{\top} \operatorname{Var}(\mathbf{A}) \mathbf{f} \\
& \triangleq(1-k)^{2} C_{1}+C_{2}-k^{2} C_{3}
\end{aligned}
$$

Since for each $\mathbf{A}$, we have $(\mathbf{I}-\mathbf{A})^{2}=(\mathbf{I}-\mathbf{A})$ and $\left(\mathbf{A}-\mathbf{1 1}^{\top} / n\right)^{2}=\mathbf{A}-\mathbf{1 1}^{\top} / n$, then both $\mathbf{I}-\mathbf{A}$ and $\mathbf{A}-\mathbf{1 1}^{\top}$ are idempotent, and hence are positive semi-definite. It follows that both $\mathbf{I}-\mathbb{E A}$ and $\mathbb{E A}-\mathbf{1 1}^{\top} / n$ are also positive semi-definite. Hence $C_{1} \geq 0$ and $C_{2} \geq 0$.

On the other hand, by the law of total variance, we have

$$
\operatorname{Var}(\hat{\mathbf{f}})=\mathbb{E}[\operatorname{Var}(\hat{\mathbf{f}} \mid \mathbb{G})]+\operatorname{Var}[\mathbb{E}[\hat{\mathbf{f}} \mid \mathbb{G}]]
$$

For the first term of (37), we have

$$
\begin{aligned}
\operatorname{Var}(\hat{\mathbf{f}} \mid \mathbb{G}) & =\sigma^{2}\left[k \mathbf{I}+\frac{1-k}{n} \mathbf{1}_{n} \mathbf{1}_{n}^{\top}\right] \mathbf{A} \mathbf{A}^{\top}\left[k \mathbf{I}+\frac{1-k}{n} \mathbf{1}_{n} \mathbf{1}_{n}^{\top}\right] \\
& =\sigma^{2}\left[k^{2} \mathbf{A} \mathbf{A}^{\top}+\frac{1-k}{n} \mathbf{1}_{n} \mathbf{1}_{n}^{\top} \mathbf{A} \mathbf{A}^{\top}+\frac{1-k}{n} \mathbf{A} \mathbf{A}^{\top} \mathbf{1}_{n} \mathbf{1}_{n}^{\top}+\frac{(1-k)^{2}}{n^{2}} \mathbf{1}_{n} \mathbf{1}_{n}^{\top} \mathbf{1}_{n} \mathbf{1}_{n}^{\top}\right] .
\end{aligned}
$$

Since

$$
\begin{aligned}
\operatorname{tr}\left(\mathbf{A} \mathbf{A}^{\top}\right) & =\operatorname{tr}(\mathbf{A}) \\
& =\operatorname{tr}\left(\mathbf{B}_{G^{\top}}\left(\mathbf{G}^{\top} \mathbf{B}_{G^{\top}}\right)^{-1} \mathbf{G}^{\top}\right) \\
& =\operatorname{tr}\left(\left(\mathbf{G}^{\top} \mathbf{B}_{G^{\top}}\right)^{-1} \mathbf{G}^{\top} \mathbf{B}_{G^{\top}}\right) \\
& =g
\end{aligned}
$$

then

$$
\operatorname{tr}[\operatorname{Var}(\hat{\mathbf{f}} \mid \mathbb{G})]=\sigma^{2}\left[k^{2} g+2(1-k)+(1-k)^{2}\right]
$$

For the second term of (37), we have

$$
\operatorname{Var}[\mathbb{E}[\hat{\mathbf{f}} \mid \mathbb{G}]]=\operatorname{Var}\left[k \mathbb{A f}+\frac{1-k}{n} \mathbf{1}_{n}^{\top} \mathbf{f} \mathbf{1}_{n}\right]=k^{2} \operatorname{Var}[\mathbb{A}] \mathbf{f f}^{\top}
$$

Thus,

$$
\begin{aligned}
\operatorname{tr}[\operatorname{Var}(\hat{\mathbf{f}})] & =\operatorname{tr}[\mathbb{E}[\operatorname{Var}(\hat{\mathbf{f}} \mid \mathbb{G})]]+\operatorname{tr}[\operatorname{Var}[\mathbb{E}[\hat{\mathbf{f}} \mid \mathbb{G}]]] \\
& =\mathbb{E}[\operatorname{tr}[\operatorname{Var}(\hat{\mathbf{f}} \mid \mathbb{G})]]+\operatorname{tr}\left[k^{2} \operatorname{Var}[\mathbb{A}] \mathbf{f f}^{\top}\right] \\
& =\sigma^{2}\left[k^{2} \mathbb{E} g+2(1-k)+(1-k)^{2}\right]+k^{2} \mathbf{f}^{\top} \operatorname{Var}(\mathbf{A}) \mathbf{f} \\
& \triangleq \sigma^{2}\left[k^{2} \mathbb{E} g+2(1-k)+(1-k)^{2}\right]+k^{2} C_{3}
\end{aligned}
$$




---

It follows that the mean square error is

$$
\begin{aligned}
\operatorname{MSE} & =\|\operatorname{Bias}\|^{2}+\operatorname{tr}[\operatorname{Var}(\hat{f})] \\
& =(1-k)^{2} C_{1}+C_{2}+\sigma^{2}\left[k^{2} E_{g}+2(1-k)+(1-k)^{2}\right]
\end{aligned}
$$

The unconstrained B-spline fitting has

$$
\operatorname{MSE}_{\mathrm{ls}}=J \sigma^{2}
$$

To have $\operatorname{MSE}<\operatorname{MSE}_{\mathrm{ls}}$,

$$
(1-k)^{2} C_{1}+C_{2}+\sigma^{2}\left[k^{2} E_{g}+2(1-k)+(1-k)^{2}\right]<J \sigma^{2}
$$

that is

$$
h(k) \triangleq\left[C_{1}+\left(E_{g}+1\right) \sigma^{2}\right] k^{2}-\left[2 C_{1}+4 \sigma^{2}\right] k+C_{1}+C_{2}+3 \sigma^{2}-J \sigma^{2}<0
$$

Note that the minimum is obtained at

$$
k_{\min }=\frac{\left[2 C_{1}+4 \sigma^{2}\right]}{2\left[C_{1}+\left(E_{g}+1\right) \sigma^{2}\right]}=\frac{C_{1}+2 \sigma^{2}}{C_{1}+\left(E_{g}+1\right) \sigma^{2}} \in(0,1)
$$

since $g \geq 1$, and the minimum value is

$$
\begin{aligned}
& h_{\min }=C_{1}+C_{2}+3 \sigma^{2}-J \sigma^{2}-\frac{\left[2 C_{1}+4 \sigma^{2}\right]^{2}}{4\left[C_{1}+\left(E_{g}+1\right) \sigma^{2}\right]} \\
= & \frac{\sigma^{4}\left[(3-J)\left(E_{g}+1\right)-4\right]+\sigma^{2}\left[-C_{1}\left(J-E_{g}\right)+C_{2}\left(E_{g}+1\right)\right]+C_{1} C_{2}}{C_{1}+\left(E_{g}+1\right) \sigma^{2}} \\
= & \frac{-\sigma^{4}\left[\left(J-E_{g}\right)\left(E_{g}+1\right)+\left(E_{g}-1\right)^{2}\right]+\sigma^{2}\left[-C_{1}\left(J-E_{g}\right)+C_{2}\left(E_{g}+1\right)\right]+C_{1} C_{2}}{C_{1}+\left(E_{g}+1\right) \sigma^{2}} \\
= & \frac{u\left(\sigma^{2}\right)}{C_{1}+\left(E_{g}+1\right) \sigma^{2}},
\end{aligned}
$$

where

$$
u(t)=-t^{2}\left[\left(J-E_{g}\right)\left(E_{g}+1\right)+\left(E_{g}-1\right)^{2}\right]+t\left[-C_{1}\left(J-E_{g}\right)+C_{2}\left(E_{g}+1\right)\right]+C_{1} C_{2}
$$

Since $C_{1}, C_{2} \geq 0$,

$$
\begin{aligned}
\Delta & =\left[-C_{1}\left(J-E_{g}\right)+C_{2}\left(E_{g}+1\right)\right]^{2}+4 C_{1} C_{2}\left[\left(J-E_{g}\right)\left(E_{g}+1\right)+\left(E_{g}-1\right)^{2}\right] \geq 0 \\
& =\left[C_{1}\left(J-E_{g}\right)+C_{2}\left(E_{g}+1\right)\right]^{2}+4 C_{1} C_{2}\left(E_{g}-1\right)^{2} \geq 0
\end{aligned}
$$

then $u(t)<0$ if






---

# F. $1 G=I$ 

If $G=I$, that is, no ties in the solution,

$$
\begin{gathered}
A f=A B \gamma=B\left(B^{T} B\right)^{-1} B^{T} B \gamma=B \gamma=f \\
\|f-\mathbb{E} \hat{f}\|^{2}=\left\|f-k f-\frac{1-k}{n} \mathbf{1}^{T} f \mathbf{1}\right\|^{2} \\
=(1-k)^{2}\left\|f-\frac{1}{n} \mathbf{1}^{T} f \mathbf{1}\right\|^{2} \\
=(1-k)^{2}\left[\|f\|^{2}-\frac{1}{n}\left(\mathbf{1}_{n}^{T} f\right)^{2}\right]
\end{gathered}
$$

If $G=I, J=g, C_{2}=0$, then

$$
h_{\min }=\frac{-\sigma^{4}(g-1)^{2}}{C_{1}+(g+1) \sigma^{2}}<0
$$

## G Proof of Proposition 5

## G. 1 (i)

Proof. Since if $\gamma_{u}+\gamma_{d}=\tilde{\gamma}_{u}+\tilde{\gamma}_{d}$, then the roughness penalty does not change,

$$
\left(\gamma_{u}+\gamma_{d}\right)^{T} \Omega\left(\gamma_{u}+\gamma_{d}\right)=\left(\tilde{\gamma}_{u}+\tilde{\gamma}_{d}\right)^{T} \Omega\left(\tilde{\gamma}_{u}+\tilde{\gamma}_{d}\right)
$$

Then we can repeat the procedure in Section D.1.

## G. 2 (ii)

Proof. A special case when $G=I$ in the following result.

## G. 3 (iii)

Proof. Take the derivatives on the Lagrange form,

$$
-2 Z^{T}(y-Z \gamma)+2 H^{T} \nu+2 \mu W \gamma+2 \lambda\left[\begin{array}{l}
\Omega \\
\Omega
\end{array}\right] \gamma=0
$$

Then

$$
\begin{aligned}
& -B_{i}^{T}(y-Z \gamma)+H_{i}^{T} \nu+\mu B_{i}^{T} B\left(\gamma_{u}-\gamma_{d}\right)+\lambda \Omega_{i}\left(\gamma_{u}+\gamma_{d}\right)=0 \\
& -B_{i}^{T}(y-Z \gamma)+H_{i+J}^{T} \nu+\mu B_{i}^{T} B\left(-\gamma_{u}+\gamma_{d}\right)+\lambda \Omega_{i}\left(\gamma_{u}+\gamma_{d}\right)=0
\end{aligned}
$$

Rewrite them as

$$
\begin{aligned}
& B_{i}^{T} y+\xi_{i}=\left((1+\mu) B_{i}^{T} B+\lambda \Omega_{i}\right) \gamma_{u}+\left((1-\mu) B_{i}^{T} B+\lambda \Omega_{i}\right) \gamma_{d} \\
& B_{i}^{T} y+\xi_{i+J}=\left((1-\mu) B_{i}^{T} B+\lambda \Omega_{i}\right) \gamma_{u}+\left((1+\mu) B_{i}^{T} B+\lambda \Omega_{i}\right) \gamma_{d}
\end{aligned}
$$




---

If there are no ties in the solution, i.e.,

$$
\begin{aligned}
& \gamma_{1}^{u}<\gamma_{2}^{u}<\cdots<\gamma_{J}^{u} \\
& \gamma_{1}^{d}>\gamma_{2}^{d}>\cdots>\gamma_{J}^{d}
\end{aligned}
$$

by the KKT condition, $\nu=0$, and hence $\xi_{i}=\xi_{i+J}=0$, then (40) - (41) yields

$$
0=2 \mu B_{i}^{T} B \gamma^{u}-2 \mu B_{i}^{T} B \gamma^{d}
$$

that is

$$
0=2 \mu B^{T} B\left(\gamma^{u}-\gamma^{d}\right)
$$

which implies $\mu=0$ since $\gamma^{u}>\gamma^{d}$. Then it reduces to unconstrained B -spline fitting. This argument proves the first point of Proposition 2.

If $\hat{\gamma}_{1}^{u}<\cdots<\hat{\gamma}_{k_{1}}^{u}=\cdots=\hat{\gamma}_{k_{2}}^{u}<\cdots<\hat{\gamma}_{k_{2 m}-1}^{u}=\cdots=\hat{\gamma}_{k_{2 m}}^{u}<\hat{\gamma}_{J}$, then similar to Section D, we have

$$
G B^{T} y=\left((1+\mu) G B^{T} B+\lambda G \Omega\right) \gamma^{u}+\left((1-\mu) G B^{T} B+\lambda G \Omega\right) \gamma^{d}
$$

Let $\gamma^{u}=G^{T} \beta$, where $\beta$ is the sub-vector of $\gamma^{u}$ constructed by the unique elements. By G.1, $\gamma^{d}=c 1_{J}$, and note that $G^{T} 1_{g}=1_{J}$, then

$$
G B^{T} y=\left((1+\mu) G B^{T} B G^{T}+\lambda G \Omega G^{T}\right) \beta+c\left((1-\mu) G B^{T} B G^{T}+\lambda G \Omega G^{T}\right) 1_{g}
$$

it follows that

$$
\beta=\left((1+\mu) G B^{T} B G^{T}+\lambda G \Omega G^{T}\right)^{-1} G B^{T} y-
$$

$$
c\left((1+\mu) G B^{T} B G^{T}+\lambda G \Omega G^{T}\right)^{-1}\left((1-\mu) G B^{T} B G^{T}+\lambda G \Omega G^{T}\right) 1_{g}
$$

and

$$
c=\frac{1_{n}^{T} B \gamma_{n}^{u}}{n}=\frac{1_{n}^{T} B G^{T} \beta}{n}
$$

# G. 4 Corollary 2 

Analogously, we can obtain the monotone decomposition with smoothing splines on decreasing functions, as summarized in Corollary 2.
Corollary 2. Let $\hat{\gamma}=\left(\hat{\gamma}^{u}, \hat{\gamma}^{d}\right)$ be the monotone decomposition to problem (11). Suppose $\hat{\gamma}^{u}+\hat{\gamma}^{d}$ is decreasing, then
(i) $\hat{\gamma}^{u}$ is a vector with identical elements;
(ii) if $\hat{\gamma}_{1}^{d}>\cdots>\hat{\gamma}_{k_{1}}^{d}=\cdots=\hat{\gamma}_{k_{2}}^{d}>\cdots>\hat{\gamma}_{k_{2 m-1}}^{d}=\cdots=\hat{\gamma}_{k_{2 m}}^{d}>\hat{\gamma}_{J}$, where $1 \leq k_{1} \leq k_{2} \leq \cdots \leq$ $k_{2 m-1} \leq k_{2 m} \leq J$, then

$$
\begin{aligned}
& \hat{\gamma}^{d}=G^{T}\left((1+\mu) G B^{T} B G^{T}+\lambda G \Omega G^{T}\right)^{-1} G B^{T} y- \\
& c G^{T}\left((1+\mu) G B^{T} B G^{T}+\lambda G \Omega G^{T}\right)^{-1}\left((1-\mu) G B^{T} B G^{T}+\lambda G \Omega G^{T}\right) 1_{g} \\
& \hat{\gamma}^{u}=c 1_{J}=\frac{1_{n}^{T} B \hat{\gamma}^{d}}{n} 1_{J}
\end{aligned}
$$

Proof. Similar to the proof D. 4 for Corollary 1.




---

# H Proof of Proposition 6 

## H. 1 Lemmas

Lemma 2 (Magnus and Neudecker, 2019). Let A, B be two real matrices of the same size, then

$$
[\operatorname{tr}(\mathbf{A B})]^{2} \leq\left[\operatorname{tr}\left(\mathbf{A}^{2}\right)\right]\left[\operatorname{tr}\left(\mathbf{B}^{2}\right)\right]
$$

Lemma 3. Let A be a real positive semi-definite matrix, then

$$
\operatorname{tr}\left(\mathbf{A}^{2}\right) \leq[\operatorname{tr}(\mathbf{A})]^{2}
$$

Proof. Let $\lambda_{i}$ be the eigenvalues of $\mathbf{A}$, then $\lambda_{i}^{2}$ are the eigenvalues of $\mathbf{A}^{2}$. Note that

$$
\operatorname{tr}\left[\mathbf{A}^{2}\right]=\sum \lambda_{i}^{2} \leq\left(\sum \lambda_{i}\right)^{2}=[\operatorname{tr}(\mathbf{A})]^{2}
$$

Lemma 4. The eigenvalues of $\mathbf{1}_{n} \mathbf{1}_{n}^{T}$ is

$$
\lambda_{1}=n, \lambda_{2}=\cdots=\lambda_{n}=0
$$

Proof. Since $\mathbf{1}_{n} \mathbf{1}_{n}^{T}$ is a rank-1 matrix, which implies that it has $n-1$ eigenvalues which are zero. Denote the eigenvectors as $\xi_{i}, i=1, \ldots, n$. Suppose the nonzero eigenvalues is $\lambda_{1}$ with associated eigenvectors $\xi_{1}$, then

$$
\mathbf{1}_{n} \mathbf{1}_{n}^{T} \xi_{1}=\lambda_{1} \xi_{1}
$$

left multiplying $\mathbf{1}_{n}^{T}$ yields

$$
n \mathbf{1}_{n}^{T} \xi_{1}=\lambda_{1} \mathbf{1}^{T} \xi_{1}
$$

which implies that $\lambda_{1}=n$.

## H. $2 \mathbf{G}=\mathbf{I}$

Proof. If $\mathbf{G}=\mathbf{I}$, the solution is

$$
\begin{aligned}
\hat{\boldsymbol{\gamma}}_{u} & =\frac{1}{1+\mu}\left[\mathbf{B}^{T} \mathbf{B}+\frac{\lambda}{1+\mu} \boldsymbol{\Omega}\right]^{-1} \mathbf{B}^{T} \mathbf{y}-c\left((1+\mu) \mathbf{B}^{T} \mathbf{B}+\lambda \boldsymbol{\Omega}\right)^{-1}\left((1-\mu) \mathbf{G B}^{T} \mathbf{B}+\lambda \boldsymbol{\Omega}\right) \mathbf{1}_{J} \\
& \triangleq \frac{1}{1+\mu}\left[\mathbf{B}^{T} \mathbf{B}+\lambda_{0} \boldsymbol{\Omega}\right]^{-1} \mathbf{B}^{T} \mathbf{y}-c \boldsymbol{K} \mathbf{1}_{J} \\
\hat{\boldsymbol{\gamma}}_{d} & =c \mathbf{1}_{J}=\frac{\mathbf{1}_{n}^{T} \hat{\mathbf{f}}}{2 n} \mathbf{1}_{J}
\end{aligned}
$$

then the fitting vector is

$$
\begin{aligned}
\hat{\mathbf{f}} & =\mathbf{B} \hat{\boldsymbol{\gamma}}_{u}+\mathbf{B} \hat{\boldsymbol{\gamma}}_{d} \\
& =\frac{1}{1+\mu} \hat{\mathbf{f}}_{s s}+c \mathbf{B}(-\boldsymbol{K}+\mathbf{I}) \mathbf{1}_{J} \\
& =\frac{1}{1+\mu} \hat{\mathbf{f}}_{s s}+\frac{\mathbf{1}_{n}^{T} \hat{\mathbf{f}}}{2 n} \mathbf{B}\left[(1+\mu) \mathbf{B}^{T} \mathbf{B}+\lambda \boldsymbol{\Omega}\right]^{-1} 2 \mu \mathbf{B}^{T} \mathbf{B} \mathbf{1}_{J} \\
& =\frac{1}{1+\mu} \hat{\mathbf{f}}_{s s}+\frac{\mu}{1+\mu} \frac{\mathbf{1}_{n}^{T} \hat{\mathbf{f}}}{n} \mathbf{B}\left[\mathbf{B}^{T} \mathbf{B}+\frac{\lambda}{1+\mu} \boldsymbol{\Omega}\right]^{-1} \mathbf{B}^{T} \mathbf{1}_{n} \\
& \triangleq k \hat{\mathbf{f}}_{s s}+(1-k) \frac{\mathbf{1}_{\mathbf{n}}^{T} \hat{\mathbf{f}}}{n} \mathbf{Q} \mathbf{1}_{n}
\end{aligned}
$$




---

where $Q=B\left(B^{T} B+\lambda_{0} \Omega\right)^{-1} B^{T}$. In practice, $\lambda_{0}$ is given as a constant, so $Q$ does not depend on $k$. Left multiplying $\mathbf{1}_{n}^{T}$ yields

$$
\mathbf{1}_{n}^{T} \hat{f}=k \mathbf{1}_{n}^{T} \hat{f}_{\mathrm{ss}}+\frac{(1-k) \mathbf{1}_{n}^{T} \hat{f} \mathbf{1}_{n}^{T} Q \mathbf{1}_{n}}{n}
$$

that is,

$$
\mathbf{1}_{n}^{T} \hat{f}=\frac{k \mathbf{1}_{n}^{T} \hat{f}_{\mathrm{ss}}}{1-\frac{1_{n}^{T} Q \mathbf{1}_{n}}{n}(1-k)} \triangleq \frac{k \mathbf{1}_{n}^{T} \hat{f}_{\mathrm{ss}}}{1-\eta(1-k)}
$$

It follows that

$$
\hat{f}=\left[k I+\frac{1-k}{k} \frac{1-\eta(1-k)}{Q_{n} \mathbf{1}_{n} \mathbf{1}_{n}^{T}}\right] \hat{f}_{\mathrm{ss}} \triangleq\left(k I+\alpha Q \mathbf{1}_{n} \mathbf{1}_{n}^{T}\right) \hat{f}_{\mathrm{ss}}
$$

Then the squared bias is

$$
\begin{aligned}
\|f-\mathbb{E} \hat{f}\|_{2}^{2}= & \left\|f-\left(k I+\alpha Q \mathbf{1}_{n} \mathbf{1}_{n}^{T}\right) \mathbb{E} \hat{f}_{\mathrm{ss}}\right\|_{2}^{2} \\
= & \left\|\left(k I+\alpha Q \mathbf{1}_{n} \mathbf{1}_{n}^{T}\right)\left(f-\mathbb{E} \hat{f}_{\mathrm{ss}}\right)+\left((1-k) I-\alpha Q \mathbf{1}_{n} \mathbf{1}_{n}^{T}\right) f\right\|^{2} \\
= & \left(f-\mathbb{E} \hat{f}_{\mathrm{ss}}\right)^{T}\left(k I+\alpha \mathbf{1}_{n} \mathbf{1}_{n}^{T} Q\right)\left(k I+\alpha Q \mathbf{1}_{n} \mathbf{1}_{n}^{T}\right)\left(f-\mathbb{E} \hat{f}_{\mathrm{ss}}\right)+ \\
& 2\left(f-\mathbb{E} \hat{f}_{\mathrm{ss}}\right)^{T}\left(k I+\alpha Q \mathbf{1}_{n} \mathbf{1}_{n}^{T}\right)^{T}\left((1-k) I-\alpha Q \mathbf{1}_{n} \mathbf{1}_{n}^{T}\right) f+ \\
& f^{T}\left((1-k) I-\alpha Q \mathbf{1}_{n} \mathbf{1}_{n}^{T}\right)^{T}\left((1-k) I-\alpha Q \mathbf{1}_{n} \mathbf{1}_{n}^{T}\right) f \\
\triangleq & C_{1}+2 C_{2}+C_{3}
\end{aligned}
$$

First for term $C_{1}$, we have

$$
\begin{aligned}
C_{1}= & \left(f-\mathbb{E} \hat{f}_{\mathrm{ss}}\right)^{T}\left(k I+\alpha \mathbf{1}_{n} \mathbf{1}_{n}^{T} Q\right)\left(k I+\alpha Q \mathbf{1}_{n} \mathbf{1}_{n}^{T}\right)\left(f-\mathbb{E} \hat{f}_{\mathrm{ss}}\right) \\
= & k^{2}\left\|f-\mathbb{E} \hat{f}_{\mathrm{ss}}\right\|^{2}+2 k \alpha\left(f-\mathbb{E} \hat{f}_{\mathrm{ss}}\right)^{T} \mathbf{1}_{n} \mathbf{1}_{n}^{T} Q\left(f-\mathbb{E} \hat{f}_{\mathrm{ss}}\right)+ \\
& \alpha^{2}\left(f-\mathbb{E} \hat{f}_{\mathrm{ss}}\right)^{T} \mathbf{1}_{n} \mathbf{1}_{n}^{T} Q^{2} \mathbf{1}_{n} \mathbf{1}_{n}^{T}\left(f-\mathbb{E} \hat{f}_{\mathrm{ss}}\right)
\end{aligned}
$$

Take the derivative with respect to $k$,

$$
\begin{aligned}
\frac{\partial C_{1}}{\partial k}= & 2 k\left\|f-\mathbb{E} \hat{f}_{\mathrm{ss}}\right\|^{2}+2\left(k \frac{\partial \alpha}{\partial k}+\alpha\right)\left(f-\mathbb{E} \hat{f}_{\mathrm{ss}}\right)^{T} \mathbf{1}_{n} \mathbf{1}_{n}^{T} Q\left(f-\mathbb{E} \hat{f}_{\mathrm{ss}}\right) \\
& +2 \alpha \frac{\partial \alpha}{\partial k}\left(f-\mathbb{E} \hat{f}_{\mathrm{ss}}\right)^{T} \mathbf{1}_{n} \mathbf{1}_{n}^{T} Q^{2} \mathbf{1}_{n} \mathbf{1}_{n}^{T}\left(f-\mathbb{E} \hat{f}_{\mathrm{ss}}\right)
\end{aligned}
$$

Note that $\left.\frac{\partial \alpha}{\partial k}\right|_{k=1}=-\frac{1}{n}$ and $\alpha(1)=0$, then

$$
\left.\frac{\partial C_{1}}{\partial k}\right|_{k=1}=2\left\|f-\mathbb{E} \hat{f}_{\mathrm{ss}}\right\|^{2}-\frac{2}{n}\left(f-\mathbb{E} \hat{f}_{\mathrm{ss}}\right)^{T} \mathbf{1}_{n} \mathbf{1}_{n}^{T} Q\left(f-\mathbb{E} \hat{f}_{\mathrm{ss}}\right)
$$

Similarly, for term $C_{2}$ and $C_{3}$, we have

$$
\begin{aligned}
C_{2}= & \left(f-\mathbb{E} \hat{f}_{\mathrm{ss}}\right)^{T}\left(k I+\alpha Q \mathbf{1}_{n} \mathbf{1}_{n}^{T}\right)^{T}\left((1-k) I-\alpha Q \mathbf{1}_{n} \mathbf{1}_{n}^{T}\right) f \\
= & f^{T}(I-Q)^{T}\left(k I+\alpha Q \mathbf{1}_{n} \mathbf{1}_{n}^{T}\right)^{T}\left((1-k) I-\alpha Q \mathbf{1}_{n} \mathbf{1}_{n}^{T}\right) f \\
= & k(1-k) f^{T}(I-Q) f+(1-k) \alpha f^{T}(I-Q) \mathbf{1}_{n} \mathbf{1}_{n}^{T} Q f-k \alpha f^{T}(I-Q) Q \mathbf{1}_{n} \mathbf{1}_{n}^{T} f+ \\
& \alpha^{2} f^{T}(I-Q) \mathbf{1}_{n} \mathbf{1}_{n}^{T} Q^{2} \mathbf{1}_{n} \mathbf{1}_{n}^{T} f \\
C_{3}= & f^{T}\left((1-k) I-\alpha Q \mathbf{1}_{n} \mathbf{1}_{n}^{T}\right)^{T}\left((1-k) I-\alpha Q \mathbf{1}_{n} \mathbf{1}_{n}^{T}\right) f \\
= & (1-k)^{2} f^{T} f-2 \alpha(1-k) f^{T} \


---

and then take their derivatives with respect to $k$,

$$
\begin{aligned}
\frac{\partial C_{2}}{\partial k}= & (1-2 k) \mathbf{f}^{T}(\mathbf{I}-\mathbf{Q}) \mathbf{f}+\left((1-k) \frac{\partial \alpha}{\partial k}-\alpha\right) \mathbf{f}^{T}(\mathbf{I}-\mathbf{Q}) \mathbf{1}_{n} \mathbf{1}_{n}^{T} \mathbf{Q} \mathbf{f}-\left(\frac{\partial \alpha}{\partial k}+\alpha\right) \\
& \mathbf{f}^{T}(\mathbf{I}-\mathbf{Q}) \mathbf{Q} \mathbf{1}_{n} \mathbf{1}_{n}^{T} \mathbf{f}+2 \alpha \frac{\partial \alpha}{\partial k} \mathbf{f}^{T}(\mathbf{I}-\mathbf{Q}) \mathbf{1}_{n} \mathbf{1}_{n}^{T} \mathbf{Q}^{2} \mathbf{1}_{n} \mathbf{1}_{n}^{T} \mathbf{f} \\
\frac{\partial C_{3}}{\partial k}= & -2(1-k) \mathbf{f}^{T} \mathbf{f}-2\left((1-k) \frac{\partial \alpha}{\partial k}-\alpha\right) \mathbf{f}^{T} \mathbf{1}_{n} \mathbf{1}_{n}^{T} \mathbf{Q f}+2 \alpha \frac{\partial \alpha}{\partial k} \mathbf{f}^{T} \mathbf{1}_{n} \mathbf{1}_{n}^{T} \mathbf{Q}^{2} \mathbf{1}_{n} \mathbf{1}_{n}^{T} \mathbf{f}
\end{aligned}
$$

it follows that

$$
\left.\frac{\partial C_{2}}{\partial k}\right|_{k=1}=-\mathbf{f}^{T}(\mathbf{I}-\mathbf{Q}) \mathbf{f}+\frac{1}{n} \mathbf{f}^{T}(\mathbf{I}-\mathbf{Q}) \mathbf{Q} \mathbf{1}_{n} \mathbf{1}_{n}^{T} \mathbf{f},\left.\quad \frac{\partial C_{3}}{\partial k}\right|_{k=1}=0
$$

On the other hand, the variance is

$$
\begin{aligned}
\operatorname{Var}(\hat{\mathbf{f}}) & =\left(k \mathbf{I}+\alpha \mathbf{Q} \mathbf{1}_{n} \mathbf{1}_{n}^{T}\right) \operatorname{Var}\left(\hat{\mathbf{f}}_{\mathrm{ss}}\right)\left(k \mathbf{I}+\alpha \mathbf{Q} \mathbf{1}_{n} \mathbf{1}_{n}^{T}\right)^{T} \\
& =k^{2} \operatorname{Var}\left(\hat{\mathbf{f}}_{\mathrm{ss}}\right)+k \alpha \mathbf{Q} \mathbf{1}_{n} \mathbf{1}_{n}^{T} \operatorname{Var}\left(\hat{\mathbf{f}}_{\mathrm{ss}}\right)+k \alpha \operatorname{Var}\left(\hat{\mathbf{f}}_{\mathrm{ss}}\right) \mathbf{1}_{n} \mathbf{1}_{n}^{T} \mathbf{Q}+\alpha^{2} \mathbf{Q} \mathbf{1}_{n} \mathbf{1}_{n}^{T} \operatorname{Var}\left(\hat{\mathbf{f}}_{\mathrm{ss}}\right) \mathbf{1}_{n} \mathbf{1}_{n}^{T} \mathbf{Q}
\end{aligned}
$$

and

$$
\operatorname{tr}[\operatorname{Var}(\hat{\mathbf{f}})]=k^{2} \operatorname{tr}\left[\operatorname{Var}\left(\hat{\mathbf{f}}_{\mathrm{ss}}\right)\right]+2 k \alpha \operatorname{tr}\left[\mathbf{Q} \mathbf{1}_{n} \mathbf{1}_{n}^{T} \operatorname{Var}\left(\hat{\mathbf{f}}_{\mathrm{ss}}\right)\right]+\alpha^{2} \operatorname{tr}\left[\mathbf{Q} \mathbf{1}_{n} \mathbf{1}_{n}^{T} \operatorname{Var}\left(\hat{\mathbf{f}}_{\mathrm{ss}}\right) \mathbf{1}_{n} \mathbf{1}_{n}^{T} \mathbf{Q}\right]
$$

then its derivative with respect to $k$ is

$$
\begin{aligned}
\frac{\partial \operatorname{tr}[\operatorname{Var}(\hat{\mathbf{f}})]}{\partial k}= & 2 k \operatorname{tr}\left[\operatorname{Var}\left(\hat{\mathbf{f}}_{\mathrm{ss}}\right)\right]+2\left(k \frac{\partial \alpha}{\partial k}+\alpha\right) \operatorname{tr}\left[\mathbf{Q} \mathbf{1}_{n} \mathbf{1}_{n}^{T} \operatorname{Var}\left(\hat{\mathbf{f}}_{\mathrm{ss}}\right)\right]+ \\
& 2 \alpha \frac{\partial \alpha}{\partial k} \mathbf{Q} \mathbf{1}_{n} \mathbf{1}_{n}^{T} \operatorname{Var}\left(\hat{\mathbf{f}}_{\mathrm{ss}}\right) \mathbf{1}_{n} \mathbf{1}_{n}^{T} \mathbf{Q}
\end{aligned}
$$

Evaluate at $k=1$,

$$
\left.\frac{\partial \operatorname{tr}[\operatorname{Var}(\hat{\mathbf{f}})]}{\partial k}\right|_{k=1}=2 \operatorname{tr}\left[\operatorname{Var}\left(\hat{\mathbf{f}}_{\mathrm{ss}}\right)\right]-\frac{2}{n} \operatorname{tr}\left[\mathbf{Q} \mathbf{1}_{n} \mathbf{1}_{n}^{T} \operatorname{Var}\left(\hat{\mathbf{f}}_{\mathrm{ss}}\right)\right]
$$

Thus

$$
\begin{aligned}
& \left.\frac{\partial \operatorname{MSE}(k)}{\partial k}\right|_{k=1}=2\left\|\mathbf{f}-\mathrm{E} \hat{\mathbf{f}}_{\mathrm{ss}}\right\|^{2}-\frac{2}{n}\left(\mathbf{f}-\mathrm{E} \hat{\mathbf{f}}_{\mathrm{ss}}\right)^{T} \mathbf{1}_{n} \mathbf{1}_{n}^{T} \mathbf{Q}\left(\mathbf{f}-\mathrm{E} \hat{\mathbf{f}}_{\mathrm{ss}}\right)+ \\
& 2\left[-\mathbf{f}^{T}(\mathbf{I}-\mathbf{Q}) \mathbf{f}+\frac{1}{n} \mathbf{f}^{T}(\mathbf{I}-\mathbf{Q}) \mathbf{Q} \mathbf{1}_{n} \mathbf{1}_{n}^{T} \mathbf{f}\right]+ \\
& 2 \operatorname{tr}\left[\operatorname{Var}\left(\hat{\mathbf{f}}_{\mathrm{ss}}\right)\right]-\frac{2}{n} \operatorname{tr}\left[\mathbf{Q} \mathbf{1}_{n} \mathbf{1}_{n}^{T} \operatorname{Var}\left(\hat{\mathbf{f}}_{\mathrm{ss}}\right)\right] \\
& =2 \mathbf{f}^{T} \frac{\mathbf{Q} \mathbf{1}_{n} \mathbf{1}_{n}^{T} \mathbf{Q}}{n}(\mathbf{I}-\mathbf{Q}) \mathbf{f}-2 \mathbf{f}^{T} \mathbf{Q}(\mathbf{


---

Next, we will prove the first term on the right-hand side of (43) is positive. By the Cauchy-Schwarz inequality for trace in Lemma 2,

$$
\begin{aligned}
\operatorname{tr}\left[\mathbf{Q} \mathbf{1}_{n} \mathbf{1}_{n}^{T} \operatorname{Var}\left(\hat{\boldsymbol{f}}_{s s}\right)\right] & \leq \sqrt{\operatorname{tr}\left[\left(\mathbf{Q} \mathbf{1}_{n} \mathbf{1}_{n}^{T}\right)^{2}\right] \operatorname{tr}\left[\left(\operatorname{Var}\left(\hat{\boldsymbol{f}}_{s s}\right)\right)^{2}\right]} \\
& =\frac{\mathbf{1}_{n}^{T} \mathbf{Q} \mathbf{1}_{n}}{\sqrt{\operatorname{tr}\left[\left(\operatorname{Var}\left(\hat{\boldsymbol{f}}_{s s}\right)\right)^{2}\right]}}
\end{aligned}
$$

and since $\operatorname{Var}\left(\hat{\boldsymbol{f}}_{s s}\right)=\sigma^{2} \mathbf{Q}^{2}$ is a positive semi-definite matrix, then by Lemma 3,

$$
\operatorname{tr}\left[\left(\operatorname{Var}\left(\hat{\boldsymbol{f}}_{s s}\right)\right)^{2}\right] \leq\left[\operatorname{tr}\left(\operatorname{Var}\left(\hat{\boldsymbol{f}}_{s s}\right)\right)\right]^{2}
$$

Note that

$$
\eta=\frac{\mathbf{1}_{n}^{T} \mathbf{Q} \mathbf{1}_{n}}{n}=\frac{\mathbf{1}_{n}^{T} \mathbf{Q} \mathbf{1}_{n}}{\mathbf{1}_{n}^{T} \mathbf{1}_{n}} \leq \lambda_{\max }(\mathbf{Q})=\lambda_{\max }\left(\mathbf{B}\left(\mathbf{B}^{T} \mathbf{B}+\lambda_{0} \boldsymbol{\Omega}\right)^{-1} \mathbf{B}^{T}\right)
$$

Perform singular value decomposition (SVD) on $\mathbf{B}, \mathbf{B}=\mathbf{U D V}^{T}$, where $\mathbf{U}$ and $\mathbf{V}$ are $n \times J$ and $J \times J$ orthogonal matrices, and $\mathbf{D}$ is a $J \times J$ diagonal matrix, with diagonal entries $d_{1} \geq d_{2} \geq \cdots d_{p} \geq 0$. Then

$$
\mathbf{Q}=\mathbf{U D V}^{T}\left(\mathbf{V D}^{2} \mathbf{V}^{T}+\lambda_{0} \boldsymbol{\Omega}\right)^{-1} \mathbf{V D U}^{T}=\mathbf{U}\left(\mathbf{I}+\lambda_{0} \mathbf{D}^{-1} \mathbf{V}^{T} \boldsymbol{\Omega} \mathbf{V D}^{-1}\right)^{-1} \mathbf{U}^{T}
$$

it follows that

$$
\begin{aligned}
\eta & \leq \lambda_{\max }\left(\mathbf{U}\left(\mathbf{I}+\lambda_{0} \mathbf{D}^{-1} \mathbf{V}^{T} \boldsymbol{\Omega} \mathbf{V D}^{-1}\right)^{-1} \mathbf{U}^{T}\right) \\
& =\lambda_{\max }\left(\left(\mathbf{I}+\lambda_{0} \mathbf{D}^{-1} \mathbf{V}^{T} \boldsymbol{\Omega} \mathbf{V D}^{-1}\right)^{-1}\right) \\
& =\frac{1}{\lambda_{\min }\left(\mathbf{I}+\lambda_{0} \mathbf{D}^{-1} \mathbf{V}^{T} \boldsymbol{\Omega} \mathbf{V D}^{-1}\right)} \\
& =\frac{1}{1+\lambda_{\min }\left(\lambda_{0} \mathbf{D}^{-1} \mathbf{V}^{T} \boldsymbol{\Omega} \mathbf{V D}^{-1}\right)}<1
\end{aligned}
$$

thus

$$
\frac{1}{n} \operatorname{tr}\left[\mathbf{Q} \mathbf{1}_{n} \mathbf{1}_{n}^{T} \operatorname{Var}\left(\hat{\boldsymbol{f}}_{s s}\right)\right]<\operatorname{tr}\left[\operatorname{Var}\left(\hat{\boldsymbol{f}}_{s s}\right)\right]
$$

Note that if $\frac{\partial \operatorname{MSE}(k)}{\partial k}>0$, that is,

$$
\sigma^{2}>\frac{\boldsymbol{f}^{T} \mathbf{Q}\left(\mathbf{I}-\frac{\mathbf{1}_{n} \mathbf{1}_{n}^{T} \mathbf{Q}}{n}\right)(\mathbf{I}-\mathbf{Q}) \boldsymbol{f}}{\operatorname{tr}\left[\left(\mathbf{I}-\frac{\mathbf{1}_{n} 1_{n}^{T} \mathbf{Q}}{n}\right) \mathbf{Q}^{2}\right]}
$$

then there exists $k \in(0,1)$ such that $\operatorname{MSE}(k)<\operatorname{MSE}(1)$.
If $\lambda_{0}=0$, then $(\mathbf{I}-\mathbf{Q}) \boldsymbol{f}=\mathbf{0}$, and

$$
\begin{gathered}
\mathbf{1}_{n} \mathbf{1}_{n}^{T} \mathbf{Q}=\mathbf{1}_{n}\left(\mathbf{B} \mathbf{1}_{J}\right)^{T} \mathbf{B}\left(\mathbf{B}^{T} \mathbf{B}\right)^{-1} \mathbf{B}^{T}=\mathbf{1}_{n} \mathbf{1}_{J}^{T} \mathbf{B}^{T}=\mathbf{1}_{n} \mathbf{1}_{n}^{T} \\
\mathbf{I}-\frac{\mathbf{1}_{n} \mathbf{1}_{n}^{T} \mathbf{Q}}{n}=\mathbf{I}-\frac{\mathbf{1}_{n}\left(\mathbf{B} \mathbf{1}_{J}\right)^{T} \mathbf{B}\left(\mathbf{B}^{T} \mathbf{B}\right)^{-1} \mathbf{B}^{T}}{n}=\mathbf{I}-\frac{\mathbf{1}_{n} \mathbf{1}_{J}^{T} \mathbf{B}^{T}}{n}=\mathbf{I}-\frac{\mathbf{1}_{n} \mathbf{1}_{n}^{T}}{n}
\end{gathered}
$$

then

$$
\operatorname{tr}\left[\left(\mathbf{I}-\frac{\mathbf{1}_{n} \mathbf{1}_{n}^{T} \mathbf{Q}}{n}\right) \mathbf{Q}^{2}\right]=\operatorname{tr}\left[\left(\mathbf{I}-\frac{\mathbf{1}_{n} \mathbf{1}_{n}^{\boldsymbol{T}}}{n}\right) \mathbf{Q}\right]=\frac{J-1}{n} \operatorname{tr}\left[\mathbf{1}_{n} \mathbf{1}_{n}^{T} \mathbf{Q}\right]=J-1
$$

and hence $\frac{\partial \operatorname{MSE}(k)}{\partial k}>0$ if $\sigma^{2}>0$, which always holds.




---

