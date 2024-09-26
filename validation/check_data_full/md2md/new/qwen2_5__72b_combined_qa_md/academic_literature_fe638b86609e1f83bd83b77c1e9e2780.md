# FROM NAIVE TREES TO RANDOM FORESTS: A GENERAL APPROACH FOR PROOFING CONSISTENCY OF TREE-BASED METHODS 

Nico Föge<br>Department of Mathematics<br>Otto-von-Guericke Universität Magdeburg<br>nico.foege@ovgu.de<br>Markus Pauly<br>Department of Statistics<br>TU Dortmund University<br>markus.pauly@tu-dortmund.de<br>Lena Schmid<br>Department of Statistics<br>TU Dortmund University<br>lena*@tu-dortmund.de<br>Marc Ditzhaus<br>Department of Mathematics<br>Otto-von-Guericke Universität Magdeburg<br>marc.ditzhaus@ovgu.de

April 11, 2024


#### Abstract

Tree-based methods such as Random Forests are learning algorithms that have become an integral part of the statistical toolbox. The last decade has shed some light on theoretical properties such as their consistency for regression tasks. However, the usual proofs assume normal error terms as well as an additive regression function and are rather technical. We overcome these issues by introducing a simple and catchy technique for proofing consistency under quite general assumptions. To this end, we introduce a new class of naive trees, which do the subspacing completely at random and independent of the data. We then give a direct proof of their consistency. Using them to bound the error of more complex tree-based approaches such as univariate and multivariate CARTs, Extra Randomized Trees, or Random Forests, we deduce the consistency of all of them. Since naive trees appear to be too simple for actual application, we further analyze their finite sample properties in a simulation and small benchmark study. We find a slow convergence speed and a rather poor predictive performance. Based on these results, we finally discuss to what extent consistency proofs help to justify the application of complex learning algorithms.


## 1 Introduction

Due to their capacity to handle complex relationships while also offering possibilities for interpretability [19, 27], treebased learning algorithms, especially Random Forests [7], are among the most popular machine learning approaches. Their possible applications include predictive tasks [44], variable selection [20, 36], uncertainty quantification [9, 26, 34], imputation [35, 41] as well as inference [24, 44]. Moreover, they are still one of the state-of-the-art approaches for tabular data despite the ubiquity of deep learning approaches [17]. Thus, there is a lot of empirical evidence for the good performance of Random Forests and other tree-based learners. We nevertheless don't know enough about the underlying mathematical reasons, despite several theoretical investigations from the last ten to fifteen years. Here, several papers focused on the mathematical study of the consistency of Random Forests. This started with the seminal paper by [3] who were the first to prove consistency for the Random Forest, though for a simplified version. The work was continued by [14] and [2] until [40] finally provided a consistency proof for the original regression estimator introduced by [7]. The paper quickly gained scientific recognition and is one of the most cited Annals of Statistics papers of the last decade. The stated result is valid for the class of additive models with normally distributed errors




---

given by the regression model

$$
Y=\sum_{j=1}^{p} m_{j}\left(X^{(j)}\right)+\varepsilon
$$

where $Y \in \mathbb{R}$ is the univariate output variable, $X=\left(X^{(1)}, \ldots, X^{(p)}\right)^{\top}$ is uniformly distributed on $[0,1]^{p}, \varepsilon$ is an independent centered Gaussian error with finite variance and each additive regression function $m_{j}$ is assumed to be continuous. The consistency results were later extended from the i.i.d. setting to dependent [16] and spatial-dependent data [37] as well as settings with missing observations [18], still assuming Gaussianity and an additive regression function. The result from [40] was also used to construct valid prediction intervals [33] or to prove consistency of residual variance estimators $[25,35]$ and of certain variable importance measures [36,39]. More recently, the preprint [5] studied consistency of tree-based methods by means of a new probabilistic impurity decrease condition. This way, they were able to prove consistency of tree-based ensembles such as Extremely Randomized Trees [15, ExtraTrees] under technical but quite general assumptions. However, the classical Random Forest was not covered. Another line of research focused on generalized Random Forests [1] fulfilling the honesty condition [42]. The corresponding regressions estimators were also shown to be consistent and even asymptotically normal [1, 42]. Moreover, [10] even established rates of consistency for the Random Forest [7] based on the CART (Classification And Rregression Tree) algorithm of [8]. While there are various theoretical results for the univariate Random Forest and other tree-based learners, the imposed conditions for consistency are often technical and quite strong. Moreover, there is a lack of mathematical theory for multivariate extensions [38]. In the present paper we therefore propose

1. a simple proof technique for the consistency of general univariate and multivariate tree-based regression learner that
2. neither requires Gaussianity of error terms nor an additive regression function.

To this end, we construct a naive tree, which does the splitting of the feature space independent of the data and completely at random and prove its $L^{2}$-consistency. We then compare the quadratic error of the naive tree and other existing trees, such as CART within the Random Forest, from which we deduce the consistency of the respective tree and the corresponding ensemble-learner. The technique is straightforward and also applicable for multivariate trees and ensembles thereof. Unlike [12], who created completely random decision trees to maximize the diversity of the trees in a forest, our naive tree does not show good finite sample performance and is only a theoretical tool to show the consistency of more accurate methods.

The rest of the present paper is organized as follows. In Section 2 we introduce our general statistical model and the assumptions. Moreover, we define the naive tree, which splits the feature space independent of the data. Our main asymptotic results are given in Section 3. We derive consistency of the naive tree from which we deduce consistency of the uni- and multivariate ExtraTrees or Random Forest algorithm in Section 4. To analyze the finite sample performance of the naive trees with respect to well-known approaches, we conduct a simulation (Section 5) and a small benchmark study (Section 6). The paper closes with a conclusion and outlook (Section 7). All proofs are given in the Appendix.

# 2 Mathematical Framework 

We consider a regression model with a multivariate $d$-dimensional output variable $\boldsymbol{Y}=\left(Y^{(1)}, \ldots, Y^{(d)}\right)^{\top} \in \mathbb{R}^{d}$ and and error vector $\varepsilon=\left(\varepsilon^{(1)}, \ldots, \varepsilon^{(d)}\right)^{\top} \in \mathbb{R}^{d}$. The output variable is linked to a uniformly distributed feature vector $X \sim \mathcal{U}\left[0,1]^{p}\right.$ through a continuous function $m:[0,1]^{p} \longrightarrow \mathbb{R}^{d}$, i.e.

$$
\boldsymbol{Y}=m(X)+\varepsilon
$$

where $\mathbb{E}[\varepsilon]=0$ and $\operatorname{Cov}(\varepsilon)=\operatorname{diag}\left(\sigma_{1}^{2}, \ldots, \sigma_{d}^{2}\right) \in \mathbb{R}^{d \times d}$ with $\sigma_{j}>0$ for all $j=1, \ldots, d$. As in classical CLTs for nonparametric regression models. We only assume that $\varepsilon$ is independent of $X$ and possesses finite second marginal moments, i.e. $\mathbb{E}\left[\left(\varepsilon^{(j)}\right)^{2}\right] \leqslant K_{\varepsilon}$ for all $j=1, \ldots, d$ and a fixed $K_{\varepsilon}>0$. Thus, this model is a generalization of the regression model (1) utilized in [40] in three directions (error distribution, regression function, output dimensionality).

The function $m$ can be estimated by a regression tree. To formulate this mathematically, we follow [36,40] who describe the tree generation by a random vector $\Theta$. At each node of the regression tree, $m_{t r y} \in\{1, \ldots, p\}$ features are randomly selected. The selected features determine the direction during the feature subspacing at each node. In our situation, the training set

$$
\mathcal{D}_{n}=\left\{\left[\boldsymbol{X}_{i}^{\top}, \boldsymbol{Y}_{i}^{\top}\right]^{\top} \in[0,1]^{p} \times \mathbb{R}^{d} ; i=1, \ldots, n\right\}
$$

contains independent random vectors $\left[\boldsymbol{X}_{i}^{\top}, \boldsymbol{Y}_{i}^{\top}\right]^{\top}$ that have the same distribution as $\left[\boldsymbol{X}^{\top}, \boldsymbol{Y}^{\top}\right]^{\top}$. The iid errors are denoted by $\varepsilon_{1}, \ldots, \varepsilon_{n}$ and have the same distribution as $\varepsilon$.




---

For the CART algorithm used within Random Forests, $\Theta$ can be decomposed into two subvectors $\Theta=$ $\left(\Theta^{(1)}, \Theta^{(2)}\right)$, where $\Theta^{(1)} \in \mathbb{R}^{n}$ models the bootstrap sampling mechanism prior to tree construction and $\Theta^{(2)}$ models the feature subspacing in the tree construction [36]. To describe this step more formally, for each node the algorithm selects $m_{\text {try }} \in\{1, \ldots, p\}$ features from

$$
\left\{\left(\Theta_{1}^{(2)}, \ldots, \Theta_{p}^{(2)}\right) \in\{0,1\}^{p}: \sum_{j=1}^{p} \Theta_{j}^{(2)}=m_{\mathrm{try}}\right\}
$$

where $\Theta_{j}^{(2)}$ denotes whether the $j$-th component was selected $\left(\Theta_{j}^{(2)}=1\right)$ or not $\left(\Theta_{j}^{(2)}=0\right)$ based upon optimizing the CART-split criterion (minimizing the squared prediction error) within Random Forest. It is described in detail in Algorithm 3 in the Supplement. For the tree construction in the ExtraTrees algorithm [15], we have to re-define $\Theta$, since there is no bootstrap of the training data and a random selection of the splits as described in Section 4 and Algorithm 2 below.
Regression trees use the training set to approximate $m$ by a piece-wise constant function. For this purpose, the feature space is partitioned into subspaces through a tree-based procedure. We denote the number of subspaces with $t_{n} \in\{1, \ldots, n\}$ and the resulting subspaces as $A_{n, 1}\left(\Theta, \mathcal{D}_{n}\right), \ldots, A_{n, t_{n}}\left(\Theta, \mathcal{D}_{n}\right)$. Moreover, let $A_{n}\left(x, \Theta, \mathcal{D}_{n}\right)$ be the subspace containing $x \in[0,1]^{p}$. As an estimator for $m$, we use a step function $m_{n, 1}\left(x, \Theta, \mathcal{D}_{n}\right)$ over these subsets, which heights are determined by averaging the output variable over all individuals, that fall into the same cell as $x$, i.e.

$$
m_{n, 1}\left(x, \Theta, \mathcal{D}_{n}\right)=\sum_{i=1}^{n} W_{i}\left(x, \Theta, \mathcal{D}_{n}\right) Y_{i}
$$

This covers various tree-based algorithms, that differ in the construction of the cells $A_{n, 1}\left(\Theta, \mathcal{D}_{n}\right), \ldots, A_{n, t_{n}}\left(\Theta, \mathcal{D}_{n}\right)$ via $\Theta$. In particular, we study CART, CART within Random Forest and the ExtraTree (i.e. a single tree used in the ExtraTrees ensemble) regression tree. For CART [8] and a single ExtraTree [15], the corresponding weights $W_{i}$ in (3) are given by $W_{i}\left(x, \Theta, \mathcal{D}_{n}\right)=\mathbb{1}\left\{X_{i} \in A_{n}\left(x, \Theta, \mathcal{D}_{n}\right)\right\} / N_{n}\left(x, \Theta, \mathcal{D}_{n}\right)$, where $N_{n}\left(x, \Theta, \mathcal{D}_{n}\right)$ denotes the number of observations in $\mathcal{D}_{n}$ that fall into the same cell as $x$. For a single CART within the Random Forest, the definition slightly changes as the tree is only build based upon a subsample of $D_{n}$, see Algorithm 3 in the supplement and [4]. More general as before, we thus have to define the denominator $N_{n}\left(x, \Theta, \mathcal{D}_{n}\right)$ as the number of observations from the subsample of $\mathcal{D}_{n}$ that fall into the same cell as $x$ and work with the weights

$$
W_{i}\left(x, \Theta, \mathcal{D}_{n}\right)= \begin{cases}\frac{\mathbb{1}\left\{X_{i} \in A_{n}\left(x, \Theta, \mathcal{D}_{n}\right)\right\}}{N_{n}\left(x, \Theta, \mathcal{D}_{n}\right)} & \text { if } X_{i} \text { is drawn during feature selection } \\ 0 & \text { else }\end{cases}
$$

Here, and throughout we use the convention $0 / 0=0$ for the weights. In all three cases, we can rewrite $m_{n, 1}$ as the mean

$$
m_{n, 1}\left(x, \Theta, \mathcal{D}_{n}\right)=\bar{Y}_{A_{n}\left(x, \Theta, \mathcal{D}_{n}\right)}
$$

where the right-hand side denotes the mean of all output vectors $Y_{i}$ of the sample (subsample in case of CART within Random Forest), whose corresponding feature vector $X_{i}$ lies in $A_{n}\left(x, \Theta, \mathcal{D}_{n}\right)$.

As stated above, the algorithms differ in the construction of the cells $A_{n, 1}\left(\Theta, \mathcal{D}_{n}\right), \ldots, A_{n, t_{n}}\left(\Theta, \mathcal{D}_{n}\right)$. To establish their consistency, and subsequently of the corresponding ensembles of Random Forest and ExtraTrees, our approach is to construct a naive tree, which partitions the feature space completely at random and independent of the data i.e. we set $A_{n, t}\left(\Theta, \mathcal{D}_{n}\right)=A_{n, t}(\Theta), t=1, \ldots, t_{n}$, where $\Theta$ is described in the algorithm below.
The algorithm constructs a partition $A_{n, 1}(\Theta), \ldots, A_{n, t_{n}}(\Theta)$, that is independent of the data and thus simplifies the theoretical handling of the tree. In the next section, we prove that even this simple approach can deliver a consistent estimator for $m$. Through the comparison with this naive approach, we get the consistency of more complex tree-based regression learners like CART, (single) ExtraTree and corresponding ensembles.

# 3 Consistency of the Naive Tree 

In this section, we present our main consistency result for naive trees described in Algorithm 1. We will later use this as a new tool for proving consistency for different tree-based learners. To be more flexible, we prove the results for naive trees built upon a subsample of size $a_{n} \in\{1, \ldots, n\}$ as described in Algorithm 1 drawn prior to tree construction. This contains no subsampling $\left(a_{n}=n\right)$ as special case.
For consistent estimation of $m$, cells must become become small as $n \rightarrow \infty$ to take advantage of the continuity of $m$. The shrinking of the cells is guaranteed, with a growing number of splits, as we show in Lemma 1 of the Appendix.




---

```
Algorithm 1: Naive Tree Algorithm
    Data: The number of leaves $t_{n} \in \mathbb{N}$, the size of the subsample $a_{n} \in\{1, \ldots, n\}$ and the number of features during
        feature subsampling $m_{\text {try }} \in\{1, \ldots, p\}$
    Output: A partition of $[0,1]^{p}$ and a subset of $\mathcal{D}_{n}$
    Let $\Theta$ be the tree constructing random vector, and $A(\Theta)=\left[a_{1}(\Theta), b_{1}(\Theta)\right] \times \ldots \times\left[a_{p}(\Theta), b_{p}(\Theta)\right]$;
    Set $n_{\text {nodes }}=1$, level $=0$ and the starting partition $\mathcal{P}_{0}=\left\{[0,1]^{p}\right\}$ and $\mathcal{P}_{\text {level }}=\varnothing$ for all $1 \leqslant \operatorname{level} \leqslant n$;
    Draw and save a subsample of $\mathcal{D}_{n}$ of the size $a_{n}$ without replacement;
    while $n_{\text {nodes }}<t_{n}$ do
        if $\mathcal{P}_{\text {level }}=\varnothing$ then
            level $\leftarrow$ level +1 ;
        else
            Let $A(\Theta)$ be the first element of $\mathcal{P}_{\text {level }}$
            Draw a random subset $M_{t r y} \subset\{1, \ldots, p\}$ with $\left|M_{t r y}\right|=m_{t r y}$;
            Draw a dimension $J$ uniformly on $M_{\text {try }}$;
            Draw a cut-point $z_{J}(\Theta)$ uniformly on $\left[a_{J}(\Theta), b_{J}(\Theta)\right]$;
            Set
            \[
            \begin{aligned}
            \left(A_{J}(\Theta)\right)_{L}= & {\left[a_{1}(\Theta), b_{1}(\Theta)\right] \times \ldots \times\left[a_{J-1}(\Theta), b_{J-1}(\Theta)\right] \times\left[a_{J}(\Theta), z_{J}(\Theta)\right] } \\
            & \times\left[a_{J+1}(\Theta), b_{J+1}(\Theta)\right] \times \ldots \times\left[a_{p}(\Theta), b_{p}(\Theta)\right]
            \end{aligned}
            \]
            and
            \[
            \left(A_{J}(\Theta)\right)_{R}=\left[a_{1}(\Theta), b_{1}(\Theta)\right] \times \ldots \times\left[a_{J-1}(\Theta), b_{J-1}(\Theta)\right]
            \]
            \[
            \]
            where $\Theta$ contains the randomly drawn dimension $J$ and the corresponding $z_{J}$ for each split in the
        constructed tree;
        \[
        \begin{aligned}
            \mathcal{P}_{\text {level }} & \leftarrow \mathcal{P}_{\text {level }} \backslash\{A(\Theta)\} \\
            \mathcal{P}_{\text {level }+1} & \leftarrow \mathcal{P}_{\text {level }+1} \cup\left\{\left(A_{J}(\Theta)\right)_{L}\right\} \cup\left\{\left(A_{J}(\Theta)\right)_{R}\right\} \\
            n_{\text {nodes }} & \leftarrow n_{\text {nodes }}+1
        \end{aligned}
        \]
        end
    end
```

This is necessary because in the construction of the partition of the feature space, no information about the regression function $m$ is used. With an arbitrary fine partition, a step function can approximate $m$ on this partition. To obtain a good approximation of $m$ with the naive tree, it is not only necessary to obtain an arbitrarily fine partition of $[0,1]^{p}$, but also that sufficiently many observations lie in the individual cells as $a_{n} \rightarrow \infty$, so that the estimates for the values of $m$ can become consistent. Therefore, the number of leaves $t_{n}$ and the size of the subsample drawn prior to tree construction $a_{n}$ must be chosen in a suitable ratio. This is assumed in the following theorem to prove $L^{2}$-consistency.

Theorem 3.1. Let the feature subspacing be performed according to Algorithm 1. If $\lim _{n \rightarrow \infty} t_{n} / a_{n}=0$, then the corresponding naive tree estimator $m_{n, 1}\left(X_{1}, \Theta, \mathcal{D}_{n}\right)$ is $L^{2}$-consistent for the regression $m$ of Model (2), i.e.

$$
\mathbb{E}\left[\left\|m_{n, 1}\left(X_{1}, \Theta, \mathcal{D}_{n}\right)-m\left(X_{1}\right)\right\|^{2}\right] \rightarrow 0 \quad \text { if } t_{n} \rightarrow \infty \text { and } a_{n} \rightarrow \infty \text { as } n \rightarrow \infty
$$

The consistency on the training set $\mathcal{D}_{n}$ of the naive tree is sufficient to establish the consistency of other tree-based learners, because the training set becomes dense on $[0,1]^{p}$ for growing sample size $n$ as we'll see in the next section.

# 4 Consistency of the ExtraTree and CART algorithms and Deduced Ensembles 

The naive tree from Algorithm 1 has major weaknesses, particularly if there are a lot of non-informative predictors. To be concrete, assume that there are $\tilde{p} \in\{1, \ldots, p\}$ predictors $\left(X^{(1)}, \ldots, X^{(\tilde{p})}\right)$, which are independent of $Y$. Therefore, on average, a portion of $\tilde{p} / p$ of all splits would be completely without any gain of information. Thus, although Algorithm 1 leads to consistent estimation, it is strongly advised not to actually use them. We will elaborate on this in Section 5. Nevertheless, it is a very useful tool to prove consistency of more powerful algorithms. In particular, we use it to prove consistency of the multivariate ExtraTree and CART algorithms, as well as their corresponding ensemble learners.




---

# 4.1 ExtraTrees 

We start with the (single) ExtraTree algorithm, as the naive tree can be seen as its simplification in the case $a_{n}=$ $n$ (starting with the complete training set instead of true subsampling). The concrete procedure is provided in Algorithm 2 below. We will denote the resulting regression estimator constructed by the ExtraTree algorithm as $m_{n, 1}^{e x T}=m_{n, 1}^{e x T}\left(X, \Theta, \mathcal{D}_{n}\right)$. Heuristically, the regression estimator from the ExtraTree algorithm should be consistent under the consistency conditions of the naive tree given in Theorem 3.1. That this is indeed the case can be proven by bounding the quadratic error of the ExtraTree algorithm through the quadratic error of the naive tree.
Theorem 4.1. If $\lim _{n \rightarrow \infty} t_{n} / n=0$, then $m_{n, 1}^{e x T}$ is $L_{2}$-consistent for the regression function $m$ of Model (2), i.e.

$$
\mathbb{E}\left[\left\|m_{n, 1}^{e x T}\left(X, \Theta, \mathcal{D}_{n}\right)-m(X)\right\|^{2}\right] \rightarrow 0
$$

for $t_{n} \rightarrow \infty$ as $n \rightarrow \infty$.
The above result holds for a single regression tree constructed by the ExtraTree Algorithm 2. From this we'll derive the consistency of the corresponding ensemble of Extremely Randomized Trees (ExtraTrees) as proposed by [15] in Section 4.3.

### 4.2 CART

Breiman's [8] CART algorithm is probably the best-known single tree-based learner. In this subsection, we prove its consistency covering the original CART from [8] as well as the trees within Random Forest. The CART algorithm in Random Forest is built upon two true resampling steps. First, a sample of the size $a_{n} \in\{1, \ldots, n\}$ is drawn from $\mathcal{D}_{n}$. In the original Random Forest of [7], the subsample is a bootstrap sample drawn with replacement. However, we follow [40] and draw without replacement from $\mathcal{D}_{n}$. As discussed in [40], this change from sampling with to without replacement is harmless. For the feature subspacing, a random subset from all features is drawn and the feature optimizing an $L_{2}$-type splitting criterion is chosen for the split. The concrete definition of the CART within Random Forest approach is stated in Algorithm 3 in the Supplement. Setting $a_{n}=n$ and $p=m_{\text {try }}$ in Algorithm 3, becomes equivalent to the original CART in [8] which is thus contained as a special case. We denote the resulting regression estimator as $m_{n, 1}^{C A R T}(X, \Theta, \mathcal{D})$ and its consistency follows again by a comparison to the quadratic error of the naive tree. The resulting theorem is stated below.
Theorem 4.2. If $\lim _{n \rightarrow \infty} t_{n} / a_{n}=0$, then $m_{n, 1}^{C A R T}$ is $L_{2}$-consistent for the regression function $m$ of Model (2), i.e.

$$
\mathbb{E}\left[\left\|m_{n, 1}^{C A R T}\left(X, \Theta, \mathcal{D}_{n}\right)-m(X)\right\|^{2}\right] \rightarrow 0
$$

for $t_{n} \rightarrow \infty$ as $n \rightarrow \infty$.

### 4.3 Ensembles (including Random Forest)

In this subsection we prove the consistency of bagged-type ensembles based on consistent base learners, particularly covering the ExtraTrees [15] and Random Forest [7] approaches. It turns out that the consistency of the ensemble learner can be deduced rather easily from the consistency of its base learner. The ensemble learner (or forest) is defined as the average of a larger number, say $M$, of independent base learners. Mathematically, this means we have $M$ i.i.d. copies $\Theta_{1}, \ldots, \Theta_{M}$ of $\Theta$ (each corresponding to one tree) and define the ensemble of base learners $m_{n, 1}^{(\cdot)}$ as

$$
m_{n, M}^{(\cdot)}\left(X, \Theta_{1}, \ldots, \Theta_{M}, \mathcal{D}_{n}\right)=\frac{1}{M} \sum_{t=1}^{M} m_{n, 1}^{(\cdot)}\left(X, \Theta_{t}, \mathcal{D}_{n}\right)
$$

By an application of the finite Jensen's inequality, the consistency of the base learner is sufficient for the consistency of the corresponding ensemble.
Corollary 4.3. Let $m_{n, 1}^{(\cdot)}$ be an $L_{2}$-consistent estimator for $m$ in Model (2). Then, under the conditions of Theorem 4.1, we have

$$
\mathbb{E}\left[\left\|m_{n, M}^{(\cdot)}\left(X, \Theta_{1}, \ldots, \Theta_{M}, \mathcal{D}_{n}\right)-m(X)\right\|^{2}\right] \rightarrow 0
$$

for $t_{n} \rightarrow \infty$ as $n \rightarrow \infty$.




---

```
Algorithm 2: ExtraTree Algorithm
    Data: The training data $\mathcal{D}_{n}$, the maximum number of leaves $t_{n} \in\{1, \ldots, n\}$ and the number of features during the
            feature subsampling step $m_{\text {try }} \in\{1, \ldots, p\}$.
    Output: A partition of $[0,1]^{p}$
    Set nnodes $=1$, level $=0$, the starting partition $\mathcal{P}_{0}=\left\{[0,1]^{p}\right\}$ and $\mathcal{P}_{\text {level }}=\varnothing$ for all $1 \leqslant$ level $\leqslant n$;
    while nnodes $<t_{n}$ and at least one node contains at least two different feature- and output vectors in each case do
        if $\mathcal{P}_{\text {level }}=\varnothing$ then
            level(level +1
        else
            Let $A=A\left(\Theta, \mathcal{D}_{n}\right)=\left[a_{1}(\Theta), b_{1}(\Theta)\right] \times \ldots \times\left[a_{p}(\Theta), b_{p}(\Theta)\right]$ be the first element of $\mathcal{P}_{\text {level }}$.
            if $A$ contains exactly one element then
                $\mathcal{P}_{\text {level }} \Leftarrow \mathcal{P}_{\text {level }} \backslash\{A\}$
                $\mathcal{P}_{\text {level }+1} \Leftarrow \mathcal{P}_{\text {level }+1} \cup\{A\}$
            else
                Select $m_{\text {try }}$ dimensions uniformly from the feature space $\{1, \ldots, p\}$. Denote the resulting set with
                $\mathcal{M}_{\text {try }}$;
                for $j \in \mathcal{M}_{\text {try }}$ do
                    Draw a cut-point $z_{j}=z_{j}\left(\Theta, \mathcal{D}_{n}\right)$ uniformly on $\left[a_{j}\left(\Theta, \mathcal{D}_{n}\right), b_{j}\left(\Theta, \mathcal{D}_{n}\right)\right]$;
                    Set
                        $A_{j\left(\Theta, \mathcal{D}_{n}\right) L}=\left[a_{1}\left(\Theta, \mathcal{D}_{n}\right), b_{1}\left(\Theta, \mathcal{D}_{n}\right)\right] \times \ldots$
                            $\times\left[a_{j-1}\left(\Theta, \mathcal{D}_{n}\right), b_{j-1}\left(\Theta, \mathcal{D}_{n}\right)\right] \times\left[a_{j}\left(\Theta, \mathcal{D}_{n}\right), z_{j}\left(\Theta, \mathcal{D}_{n}\right)\right]$
                            $\times\left[a_{j+1}\left(\Theta, \mathcal{D}_{n}\right), b_{j+1}\left(\Theta, \mathcal{D}_{n}\right)\right] \times \ldots \times\left[a_{p}\left(\Theta, \mathcal{D}_{n}\right), b_{p}\left(\Theta, \mathcal{D}_{n}\right)\right]$
                    and
                        $A_{j\left(\Theta, \mathcal{D}_{n}\right) R}=\left[a_{1}\left(\Theta, \mathcal{D}_{n}\right), b_{1}\left(\Theta, \mathcal{D}_{n}\right)\right] \times \ldots$
                            $\times\left[a_{j-1}\left(\Theta, \mathcal{D}_{n}\right), b_{j-1}\left(\Theta, \mathcal{D}_{n}\right)\right] \times\left[z_{j}\left(\Theta, \mathcal{D}_{n}\right), b_{j}\left(\Theta, \mathcal{D}_{n}\right)\right]$
                            $\times\left[a_{j+1}\left(\Theta, \mathcal{D}_{n}\right), b_{j+1}\left(\Theta, \mathcal{D}_{n}\right)\right] \times \ldots \times\left[a_{p}\left(\Theta, \mathcal{D}_{n}\right), b_{p}\left(\Theta, \mathcal{D}_{n}\right)\right]$.
                    Determine
                            $$
                            \begin{aligned}
                            L_{n}\left(A_{j\left(\Theta, \mathcal{D}_{n}\right) L}\right)=L_{n} & \left(A_{j\left(\Theta, \mathcal{D}_{n}\right) L}, A_{j\left(\Theta, \mathcal{D}_{n}\right) R}\right) \\
                            = & \frac{1}{\left|\mathcal{G}_{n}\right|} \sum_{i=1}^{n} \mathbb{1}_{X_{i} \in A\left(\Theta, \mathcal{D}_{n}\right)}\left(\left\|Y_{i}-Y_{A\left(\Theta, \mathcal{D}_{n}\right)}\right\|^{2}\right. \\
                            \left.-\| Y_{i}-Y_{A_{j\left(\Theta, \mathcal{D}_{n}\right) L}} \mathbb{1}_{X_{i}^{(j)}} & \left.<z_{j}-Y_{A_{j\left(\Theta, \mathcal{D}_{n}\right) R}} \mathbb{1}_{X_{i}^{(j)}} \geqslant z_{j} \|^{2}\right)
                            \end{aligned}
                            $$
                            where $\left|\mathcal{G}_{n}\right|$ denotes the cardinality of $\left\{i: X_{i} \in A\right\}$.
                    end
                        Choose
                            $$
                            A_{\mathrm{exT}\left(\Theta, \mathcal{D}_{n}\right) L}=\underset{A_{j\left(\Theta, \mathcal{D}_{n}\right) L} \in \mathcal{A}\left(\mathcal{M}_{\text {try }}\right)}{\operatorname{argmax}} L_{n}\left(A_{j\left(\Theta, \mathcal{D}_{n}\right) L}\right)
                            $$
                            where $\mathcal{A}\left(\mathcal{M}_{\text {try }}\right)=\left\{A_{j\left(\Theta, \mathcal{D}_{n}\right) L}: j \in \mathcal{M}_{\text {try }}\right\} . A_{\mathrm{exT}\left(\Theta, \mathcal{D}_{n}\right) R}$ is chosen analogously ([15]). Denote
                            the resulting cells by $A_{\mathrm{exT}}^{L}$ and $A_{\mathrm{exT}}^{R}$.
                    $\mathcal{P}_{\text {level }} \Leftarrow \mathcal{P}_{\text {level }} \backslash\{A\}$
                    $\mathcal{P}_{\text {level }+1} \Leftarrow \mathcal{P}_{\text {level }+1} \cup\left\{A_{\mathrm{exT}}^{L}\right\} \cup\left\{A_{\mathrm{exT}}^{R}\right\}$
                    nnodes $\Leftarrow$ nnodes +1
                    end
            end
        end
```




---

With the choice of $m_{n, 1}^{(\cdot)}\left(X, \Theta_{t}, \mathcal{D}_{n}\right)=m_{n, 1}\left(X, \Theta_{t}, \mathcal{D}_{n}\right)$ Corollary 4.3 guarantees the consistency of the ensemble of naive trees, which we call Naive Forest. For $m_{n, 1}^{(\cdot)}\left(X, \Theta_{t}, \mathcal{D}_{n}\right)=m_{n, 1}^{\text {exT }}\left(X, \Theta_{t}, \mathcal{D}_{n}\right)$, Corollary 4.3 also contains the consistency of the ExtraTrees algorithm from [15]. Moreover, the consistency of the original Random Forest from [7] is included as special case by setting $m_{n, 1}^{(\cdot)}\left(X, \Theta_{t}, \mathcal{D}_{n}\right)=m_{n, 1}^{\text {CART }}\left(X, \Theta_{t}, \mathcal{D}_{n}\right)$. Unlike the consistency result in [40], our result doesn't rely on an additive regression function nor on Gaussian errors and holds for multivariate output. Moreover, the Random Forest consistency Theorem 1 given in [40] requires the condition $\lim _{n \rightarrow \infty} t_{n}\left(\log \left(a_{n}\right)\right)^{9} / a_{n}=0$, which enforces our condition $\lim _{n \rightarrow \infty} t_{n} / a_{n}=0$. Thus, Corollary 4.3 is a generalization of Theorem 1 in [40] in four directions (regression function, error terms, output dimension and the choice of hyperparameters).

Moreover, we extend the consistency result for ExtraTrees from [5] by also covering multivariate outcomes and non-symmetric errors with finite second marginal moments. Since [5] also covers non-fixed dimensions and bounded non-continuous $m$, our Corollary 4.3 is not a generalization of their result.

# 5 Simulation Study 

The consistency results from Sections 3 and 4 hold asymptotically. But how much are these really worth in practice? This question is particularly interesting for the naive approaches. To answer this, we conduct a simulation study for the discussed ensemble methods. In particular, we compare the Naive Forest with the common ensemble approaches Random Forest and ExtraTrees.

### 5.1 Simulation setting

To this end, we perform $M C=1,000$ simulation runs. In each run we generate a dataset $\mathcal{D}_{n}^{m c}=\left\{\left[X_{i}^{m c}, Y_{i}^{m c}\right]^{J} \in\right.$ $\left.\left[0,1\right]^{p} \times \mathbb{R}^{d} ; i=1, \ldots, n\right\}$ for $m c=1, \ldots, M C$ according to Model (2). That is, we generate uniformly distributed

 discussed below.

Regression functions. To carry out the analysis for different scenarios, we use a variety of continuous functions $m$ as regression function:

1. Linear function: $m\left(x_{i}\right)=x_{i}^{J} \beta, i=1, \ldots, n$.
2. Polynomial function: $m\left(x_{i}\right)=\sum_{j=1}^{4} \beta_{j}\left(x_{i}^{(j)}\right)^{j}, i=1, \ldots, n$.
3. Trigonometric function: $m\left(x_{i}\right)=2 \cdot \sin \left(x_{i}^{J} \beta+2\right), i=1, \ldots, n$.

These three settings with a univariate output are motivated from [36]. In all three settings we set the parameter vector as $\beta=(2,4,-3,0)^{J}$, which should be disadvantageous for the Naive Forest because the last feature is non-informative. To also study a multivariate model, we consider the bivariate case ( $d=2$ ) with one non-informative feature:
4. Multivariate output function $m: \mathbb{R}^{4} \longrightarrow \mathbb{R}^{2}$ with

$$
m\left(x_{i}\right)=\left(3\left(x_{i}^{(1)}\right)^{2}+2\left(x_{i}^{(2)}\right)^{2},\left(x_{i}^{(3)}\right)^{4}+4 x_{i}^{(2)}\right)^{J}
$$

Error terms. We consider different distributional settings for the error terms $\varepsilon$ in the univariate cases 1. - 3. We first consider Gaussian noise with $\varepsilon_{i} \sim \mathcal{N}\left(0, \sigma^{2}\right)$ and then rerun the models with $t_{5}$ distributed noise, to underline that gaussianity is not necessary for the consistency. For the function in 4 . we generate bivariate error vectors $\left(\varepsilon_{1 i}, \varepsilon_{2 i}\right)^{J}$, with $\varepsilon_{1 i}$ and $\varepsilon_{2 i}$ independent and identically distributed. For the marginal distributions of $\varepsilon_{1 i}$ and $\varepsilon_{2 i}$ the same combinations as for the functions 1.-3. are used. We choose the variance of the Gaussian noise such that the signal-tonoise ratio $S N$ takes on the values $\{0.5,1,3,5\}$ as in [36]. Therefore, the choice of $\sigma^{2}=\operatorname{Var}\left(m\left(X_{i}\right)\right) / S N$ depends on $\operatorname{Var}\left(m\left(X_{i}\right)\right)$. Due to the independence of the covariates, the calculations for $\operatorname{Var}\left(m\left(X_{i}\right)\right)$ are straightforward in the first two settings. In the first setting we get $\operatorname{Var}\left(m\left(X_{i}\right)\right)=\operatorname{Var}\left(X_{i}^{J} \beta\right)=29 / 12$ while the variance in 2 . is given by $\operatorname{Var}\left(m\left(X_{i}\right)\right) \approx 0.7692$. For 3 we estimate $\operatorname{Var}\left(m\left(X_{i}\right)\right)$ by Monte Carlo simulation with 10,000 runs itself. The simulations provides the estimation $\widehat{\operatorname{Var}}\left(m\left(X_{i}\right)\right) \approx 1,9872$. For the multivariate function, we use $\operatorname{Var}\left(\left\|m\left(X_{i}\right)\right\|\right)$, which results in $\widehat{\operatorname{Var}}\left(\left\|m\left(X_{i}\right)\right\|\right) \approx 1,7925$. For the $t$ distribution, the variance is $5 / 3$ and not freely selectable. Hence,




---

since we fixed the regression function $m$, there is no differentiation in the Signal-to-Noise ratio for the $t$-distributed errors.
Hyperparameters. Our choice for the number of terminal nodes is $t_{n}=\left\lfloor 1 / 2 a_{n}\right\rfloor$. This choice also enforces the condition $\lim _{n \rightarrow \infty} t_{n} / a_{n}=0$ and we choose $a_{n}=\{2 / 3 n\}$ for Random Forest, which is close to the default value of 0.632 in the widespread R Package ranger ([45]). For simplicity, we set mtry $=2$ as suggested by [31]. For the Naive Forest and the ExtraTrees we use the complete dataset, i.e. choose $a_{n}=n$. We consider these three ensemble learners $m_{n, M}$ (Naive Forest), $m_{n, M}^{e x T}$ (ExtraTrees) and $m_{n, M}^{C A R T}$ (Random Forest) with varying numbers of trees $M=50,100,200$.

Training and Evaluation. For all combinations of $n$ and SN we generate training datasets $\mathcal{D}_{n}^{1}, \ldots, \mathcal{D}_{n}^{M C}$ and for each dataset we train the three different ensemble learners. For a new observation $x \in[0,1]$ we denote the prediction by the ensemble obtained from training on $\mathcal{D}_{n}^{m c}$ by $m_{n, M}^{(\cdot)}\left(x, \Theta_{1}, \ldots, \Theta_{M}, \mathcal{D}_{n}^{m c}\right)$, where $m_{n, M}^{(\cdot)}$ either stands for $m_{n, M}, m_{n, M}^{e x T}$ or $m_{n, M}^{C A R T}$, respectively. To evaluate the performance on test data, we generate an i.i.d set of new feature vectors $X_{1}^{\prime}, \ldots, X_{1000}^{\prime} \sim U\left([0,1]^{4}\right)$ for each run. Based on this set we compute

$$
\mathcal{L}_{m c}^{2}=\frac{1}{1000} \sum_{i=1}^{1000}\left\|m\left(X_{i}^{\prime}\right)-m_{n, M}^{(\cdot)}\left(X_{i}^{\prime}, \Theta_{1}, \ldots, \Theta_{M}, \mathcal{D}_{n}^{m c}\right)\right\|^{2}
$$

to estimate $\mathbb{E}\left[\left\|m(X)-m_{n, M}^{(\cdot)}\left(X, \Theta_{1}, \ldots, \Theta_{M}, \mathcal{D}_{n}^{m c}\right)\right\|^{2}\right]$. We finally use the mean

$$
\widehat{\mathcal{L}^{2}}=\frac{1}{M C} \sum_{m c=1}^{M C} \mathcal{L}_{m c}^{2}
$$

as summarizing performance measure and to compare the three forests for each combination of signal-to-noise ratio, sample size and regression function.

# 5.2 Simulation Results 

For $M=50$ trees, we can see in Figure 2, that for most combinations of sample size, signal-to-noise ratios and considered functions $m$, the Random Forest performs best, closely followed by the ExtraTrees. In each setting, the Naive Forest is by far the worst performing method, reflecting our intuition to not use it for practical data analyses. The largest margin between errors occurs for the multivariate function, while the smallest margin occurs for the non-monotonic trigonometric function. Increasing the number of trees from $M=50$ to $M=100$ or $M=200$ (see Figure 5 and Figure 6 in the Appendix) doesn't change this conclusion, since the main problem of doing non-informative splits with probability $1 / 4$ in the Naive Forest stays the same. Furthermore, we observe that the proven convergence of the quadratic error is relatively slow in case of the Naive Forest. In contrast, the behavior of the quadratic errors of the Random Forest matches with the results of the simulation study conducted in [2]. Changing from Gaussian to more heavy-tailed $t_{5}$-distributed errors (Figure 1) also doesn't change much. In all simulated settings the error of the Naive Forest is far above the error of the Random Forest and ExtraTrees which lie close to each other. This indicates that the consistency statement alone, though certainly reassuring, doesn't indicate a good predictive performance. In fact, numerical analyses are essential to judge a method's performance.



Figure 1: Quadratic error $\widehat{\mathcal{L}^{2}}$ of the three esnemble learner for $M=50$ with $t_{5}$-distributed errors and different choices of sample sizes, regression functions (Random Forest $=$ green, ExtraTrees $=$ blue, Naive Forest $=$ red).




---



Figure 2: Quadratic error $\widehat{L}_{2}$ of the three esnemble learner for $M=50$ with Gaussian errors and different choices of sample sizes, SN-ratios, regression functions and univariate (first three columns) as well as multivariate (last column) output (Random Forest $=$ green, ExtraTrees $=$ blue, Naive Forest = red) .

# 6 A small benchmark study 

As recent discussion on neutral methods comparisons [e.g. 6,13] encourage 'to perform benchmarking analyses additionally to the traditional simulation study' [13], we compare the performance of the three ensemble learners (Naive Forest, ExtraTrees and Random Forest) on 6 different datasets (Airquality, Ames Housing, House Price, Possum, Quakes and Trees), that are suitable for regression tasks. Airquality, Quakes and Trees are build-in datasets in the base version of R. Possum is from the DAAG package [23], Ames Housing was provided by [11] and House Price was retrieved from Kaggle [29]. We are excluding non-binary categorical features from all datasets, as our theoretical framework in the preceding sections was specifically designed for numerical data. Additionally, we remove any features with missing values from the data and we omit six rows of the House Price dataset due to implausible entries. Furthermore, we transform the features into the interval $[0,1]$ by min-max normalization [30] and standardize the target variable for better comparability of the results. The datasets are from different fields and have a variety of properties, that are listed in Table 1. Each dataset is randomly divided into five datasets by the R function createFolds from the Package caret [22], to estimate $\widehat{L}_{2}$, via five-fold cross-validation.

The performance of all three ensemble learners with $M=50$ (Naive Forest, ExtraTrees and Random Forest) is evaluated. The hyperparameters $t_{n}$ and $a_{n}$ are chosen similar to Section 5. We choose $t_{n}=\left\lfloor n^{1 / 2}\right\rfloor$ as well as $a_{n}=\left\lfloor 2 / 3 n\right\rfloor$, see

Table 1: Properties of the six different datasets and chosen hyperparameters $t_{n}$ and mtry. The skewness of the output variable was estimated by the empirical skewness.

| Dataset | sample size | $p$ | $t_{n}$ | mtry | skewness of $Y$ |
| :--- | ---: | ---: | ---: | :--- | ---: | ---: |
| Airquality | 153 | 4 | 12 | 2 | -0.37 |
| Ames Housing | 2930 | 27 | 54 | 5 | 1.74 |
| House Price | 3740 | 6 | 61 | 2 | 4.78 |
| Possum | 101 | 13 | 10 | 3 | -0.24 |
| Quakes | 1000 | 5 | 31 | 2 | 0.77 |
| Trees | 31 | 3 | 5 | 2 | 1.01 |




---

Table 2: Cross-validated $\mathcal{L}$-loss estimates and runtimes (in seconds) for the three tree-based ensembles (Naive Forest, ExtraTrees, Random Forest).

| Dataset | Naive Forest |  | ExtraTrees |  | Random Forest |  |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|  | runtime | $\overline{\mathcal{L}_{2}}$ | runtime | $\overline{\mathcal{L}_{2}}$ | runtime | $\overline{\mathcal{L}_{2}}$ |
| Airquality | 0.1 | 0.5971215 | 0.3 | 0.5797349 | 5.7 | 1.096039 |
| Ames Housing | 3.8 | 0.6646426 | 6.1 | 0.3695726 | 546.4 | 0.3170644 |
| House Price | 5.2 | 0.8857712 | 7.0 | 0.7857531 | 117.4 | 0.5095062 |
| Possum | 0.0 | 0.8104764 | 0.3 | 0.7168872 | 6.3 | 0.5486962 |
| Quakes | 0.8 | 0.5182705 | 1.6 | 0.3357833 | 94.2 | 0.2575057 |
| Trees | 0.0 | 0.5675174 | 0.0 | 0.4964377 | 0.0 | 0.5220893 |

Table 1 for the resulting values. We follow the recommendation of [45] and set mtry $=\lfloor\sqrt{p}\rfloor$. The cross validated empirical $\overline{\mathcal{L}_{2}}$ errors as well as the runtimes are presented in Table 2. The predictive performance results are quite similar to our findings from the simulation study (Section 5): The Naive Forest shows the worst performance of all three approaches and every dataset except for the Airquality dataset, where the Random Forest was even worse. For four ot of six datasets, the Random Forest exhibit a better predictive accuracy than the ExtraTree which itself was better than the Naive Forest on all datasets. Regarding runtime, the results are also not surprising: the Random Forest is remarkably slower than the other two approaches due to the greediness of the involved CART splitting optimization. Moreover, the Naive Forest is even faster than the ExrtaTrees and had a runtime advanatge up to a factor of 144 compared to the Random Forest (dataset Quakes). Due to its poor predictive performance, which cannot be improved much by tuning as it only has the hyperparameter $M$, we nevertheless cannot recommend the Naive Forest as predictive algorithm.

# 7 Discussion 

Today, tree-based methods are an integral part of the statistical toolbox and serve as essential analysis and modeling techniques. This is especially true for Random Forests, which are often used as a reliable benchmark method [17]. Existing consistency proofs are rather technical and rely on rather restrictive model assumptions such as Gaussian errors and additive regression functions $[16,34,40]$. This is where the present paper comes in. We introduce naive trees as a straightforward and flexible proof technique for all kinds of tree-based learners. These naive trees are a simple regression approach that splits the feature space completely independent of the data. We prove that the resulting estimator is $\mathcal{L}_{2}$-consistent in general univariate and multivariate regression settings, which do not rely on Gaussian errors nor an additive regression function. From this, we deduce consistency of a variety of tree-based learners including the CART [8], the ExtraTrees [15] and the Random Forest [7] learner.
To investigate what this consistency statement actually means in real applications, we analyze ensembles of naive trees in simulations and a small benchmark study on real datasets. The results show a relative weakness compared to its more evolved counterparts (ExtraTrees and Random Forests). In particular, (ensembles of) naive trees can in general not be recommended for practical data analyses as very large sample sizes are needed to obtain quite accurate results. This is contrary to the Random Forest and the ExtraTrees algorithms which are both (more) powerful regression approaches. We thus conclude that while consistency results are reassuring in the sense that the approaches are roughly doing the right thing, they do not tell us anything about the practicality and predictive power in real-world scenarios. This finding also highlights the importance of numeric evaluations of theoretical results to make general practical recommendations as well as for method comparisons $[6,13,28]$.
Moreover, our consistency result does not tell us anything about the underlying estimation uncertainty. In principle, naive trees could be used here due to their fast and simple computability (e.g. via Monte Carlo). However, the bounds to other learners that we use in the consistency proof are not sharp and we will work on improving them in future work and also try to derive asymptotic relative efficiencies. Moreover, other approaches based upon bootstrapping or central limit theorems [43] need to be established for our general multivariate regression setting in future research.

## APPENDIX

This appendix contains the proof of all theorems (APPENDIX A-C) as well as additional simulation results (APPENDIX E). In particular, APPENDIX A derives the proof for the consistency of the naive tree, while APPENDIX B-C are concerned with the consistency of the more common tree-based learners and ensembles.




---

# A Proof of Theorem 3.1 

Lemma 1. Let $\mathcal{A}_{n}\left(X_{i}, \Theta\right)$ be the hyperrectangle, which is constructed by Algorithm 1 and containing $X_{i}, i=1, \ldots, n$. Then $\mathcal{A}_{n}\left(X_{i}, \Theta\right)$ fulfills for every $\xi>0$ that

$$
\lim _{t_{n} \rightarrow \infty} \mathbb{P}\left(\operatorname{diam}\left(\mathcal{A}_{n}\left(X_{i}, \Theta\right)\right)>\xi\right)=0
$$

where $\operatorname{diam}(A)=\sup \left\{\left\|a_{1}-a_{2}\right\|: a_{1}, a_{2} \in A\right\}$
Proof of Lemma 1. Let $\xi>0$ be arbitrarily small. For $j=1, \ldots, p$ the $j$-th component $\left(\mathcal{A}_{j}^{J}(\Theta)\right)_{L}$ of $\left(\mathcal{A}^{J}(\Theta)\right)_{L}$ is equal to $\left[a_{j}(\Theta), b_{j}(\Theta)\right]$ with probability $\mathbb{P}(J \neq j)=\frac{p-1}{p}$ and equal to $\left[a_{j}(\Theta), z_{j}(\Theta)\right]$ with probability $\mathbb{P}(J=j)=\frac{1}{p}$. Therefore, the expected squared length of the $j$-th component of $\left(\mathcal{A}^{J}(\Theta)\right)_{L}$ can be calculated as

$$
\begin{aligned}
& \mathbb{E}\left[\operatorname{diam}\left(\left(\mathcal{A}_{j}^{J}(\Theta)\right)_{L}\right)^{2}\right]=\frac{p-1}{p} \mathbb{E}\left[\left(b_{j}(\Theta)-a_{j}(\Theta)\right)^{2}\right]+\frac{1}{p} \mathbb{E}\left[\left(z_{j}(\Theta)-a_{j}(\Theta)\right)^{2}\right] \\
& =\frac{p-1}{p} \mathbb{E}\left[\left(b_{j}(\Theta)-a_{j}(\Theta)\right)^{2}\right]+\frac{1}{p} \mathbb{E}\left[\mathbb{E}\left[\left(z_{j}(\Theta)-a_{j}(\Theta)\right)^{2} \mid a_{j}(\Theta), b_{j}(\Theta)\right]\right] \\
& =\frac{p-1}{p} \mathbb{E}\left[\left(b_{j}(\Theta)-a_{j}(\Theta)\right)^{2}\right]+\frac{1}{p} \mathbb{E}\left[\left(b_{j}(\Theta)-a_{j}(\Theta)\right)^{3} \frac{3}{\left(b_{j}(\Theta)-a_{j}(\Theta)\right)}\right] \\
& =\frac{p-1}{p} \mathbb{E}\left[\left(b_{j}(\Theta)-a_{j}(\Theta)\right)^{2}\right]+\frac{1}{3 p} \mathbb{E}\left[\left(b_{j}(\Theta)-a_{j}(\Theta)\right)^{2}\right] \\
& =\frac{3 p-2}{3 p} \mathbb{E}\left[\left(b_{j}(\Theta)-a_{j}(\Theta)\right)^{2}\right],
\end{aligned}
$$

where the third equation holds true because for $X \sim \mathcal{U}([a, b])$ it holds $\mathbb{E}\left[X^{2}\right]=\frac{b^{3}-a^{3}}{3(b-a)}$ and $z_{j}(\Theta)-$ $\left.a_{j}(\Theta) \mid a_{j}(\Theta), b_{j}(\Theta) \sim \mathcal{U}\left(\left[0, b_{j}(\Theta)-a_{j}(\Theta)\right]\right)\right)$. By induction, we can conclude on the $k$-th layer $k \in \mathbb{N}$ of the tree

$$
\mathbb{E}\left[\operatorname{diam}\left(\left(\mathcal{A}_{j}^{J}(\Theta)\right)_{L}\right)^{2}\right]=\left(\frac{3 p-2}{3 p}\right)^{k}
$$

holds true. For $\mathcal{A}_{R}^{J}$ the same results holds. When the number of cells grows arbitrarily large, the depth of the tree also grows arbitrarily large, i.e. $k \rightarrow \infty$ as $t_{n} \rightarrow \infty$. Every interval in Algorithm 1 has the same expected length. Hence, with Markov inequality

$$
\begin{aligned}
\lim _{t_{n} \rightarrow \infty} \mathbb{P}\left(\operatorname{diam}\left(\mathcal{A}_{n}(X, \Theta)\right)>\xi\right) & \leqslant \lim _{t_{n} \rightarrow \infty} \frac{1}{\xi^{2}} \mathbb{E}\left[\operatorname{diam}\left(\mathcal{A}_{n}(X, \Theta)\right)^{2}\right]=\lim _{t_{n} \rightarrow \infty} \frac{p}{\xi^{2}} \mathbb{E}\left[\operatorname{diam}\left(\left(\mathcal{A}_{j}^{J}(\Theta)\right)_{L}\right)^{2}\right] \\
& =\lim _{t_{n} \rightarrow \infty} \frac{p}{\xi^{2}}\left(\frac{3 p-2}{3 p}\right)^{k}=0
\end{aligned}
$$

if $t_{n} \rightarrow \infty$ as $n \rightarrow \infty$.
Proof of Theorem 3.1. Let

$$
\mathbb{G}_{n}\left(\Theta, \mathcal{D}_{n}\right)=\left\{X_{i}:\left(X_{i}^{J}, Y_{i}^{J}\right)_{J \in \mathcal{D}_{n}} \text { and } W_{i}\left(X_{1}, \Theta, \mathcal{D}_{n}\right) \neq 0\right\}
$$

denote the set of all feature vectors lying in the same hyperrectangle as $X_{1}$. Then we have $N_{n}\left(X_{1}, \Theta, \mathcal{D}_{n}\right)=$ $\sum_{i=1}^{n} \mathbb{1}_{\mathbb{G}_{n}\left(\Theta, \mathcal{D}_{n}\right)}\left(X_{i}\right)$. Without loss of generality let $X_{1}, \ldots, X_{a_{n}}$ be the drawn subsample, then for every fixed $\theta$ we




---

have by the law of total expectation

$$
\begin{aligned}
\mathbb{E}\left[\left|\frac{1}{N_{n}\left(X_{1}, \theta, \mathcal{D}_{n}\right)} \sum_{i=1}^{n} \varepsilon_{i} \mathbb{1}_{G_{n}\left(\theta, \mathcal{D}_{n}\right)}\left(X_{i}\right)\right|^{2}\right] & =\sum_{N=1}^{a_{n}} \mathbb{E}\left[\frac{1}{N_{n}\left(X_{1}, \theta, \mathcal{D}_{n}\right)^{2}}\left|\sum_{i=1}^{n} \varepsilon_{i} \mathbb{1}_{G_{n}\left(\theta, \mathcal{D}_{n}\right)}\left(X_{i}\right)\right|^{2} \mathbb{1}_{\left\{N_{n}\left(X_{1}, \theta, \mathcal{D}_{n}\right)=N\right\}}\right] \\
& =\sum_{N=1}^{a_{n}} \frac{1}{N^{2}} \mathbb{E}\left[\left|\sum_{i=1}^{a_{n}} \varepsilon_{i} \mathbb{1}_{G_{n}\left(\theta, \mathcal{D}_{n}\right)}\left(X_{i}\right) \mathbb{1}_{\left\{N_{n}\left(X_{1}, \theta, \mathcal{D}_{n}\right)=N\right\}}\right|^{2}\right]
\end{aligned}
$$

The expectation can be rewritten as

$$
\begin{aligned}
& \sum_{\substack{\left(i_{1}, \ldots, i_{a_{n}}\right) \in\{0,1\}^{n} \\
i_{j=1}=N}} \mathbb{P}\left(\left(\mathbb{1}_{G_{n}\left(\theta, \mathcal{D}_{n}\right)}\left(X_{1}\right), \ldots, \mathbb{1}_{G_{n}\left(\theta, \mathcal{D}_{n}\right)}\left(X_{n}\right)\right)=\left(i_{1}, \ldots i_{n}\right)\right) \\
& \cdot \mathbb{E}\left[\left.\left|\sum_{j=1}^{N} \varepsilon_{i_{j}}\right|^{2} \right\rvert\,\left(\mathbb{1}_{G_{n}\left(\theta, \mathcal{D}_{n}\right)}\left(X_{1}\right), \ldots, \mathbb{1}_{G_{n}\left(\theta, \mathcal{D}_{n}\right)}\left(X_{n}\right)\right)=\left(i_{1}, \ldots i_{n}\right)\right] \\
& =\sum_{\substack{\left(i_{1}, \ldots, i_{a_{n}}\right) \in\{0,1\}^{n} \\
i_{j=1}^{n}=N}} \mathbb{P}\left(\left(\mathbb{1}_{G_{n}\left(\theta, \mathcal{D}_{n}\right)}\left(X_{1}\right), \ldots, \mathbb{1}_{G_{n}\left(\theta, \mathcal{D}_{n}\right)}\left(X_{n}\right)\right)=\left(i_{1}, \ldots i_{n}\right)\right) \mathbb{E}\left[\left|\sum_{i=1}^{N} \varepsilon_{i}\right|^{2}\right] \\
& =\mathbb{P}\left(N_{n}\left(X_{1}, \theta, \mathcal{D}_{n}\right)=N\right) \mathbb{E}\left[\left|\sum_{i=1}^{N} \varepsilon_{i}\right|^{2}\right]
\end{aligned}
$$

Hence with (4)

$$
\begin{aligned}
& \mathbb{E}\left[\left|\frac{1}{N_{n}\left(X_{1}, \theta, \mathcal{D}_{n}\right)} \sum_{i=1}^{n} \varepsilon_{i} \mathbb{1}_{G_{n}\left(\theta, \mathcal{D}_{n}\right)}\left(X_{i}\right)\right|^{2}\right]=\sum_{N=1}^{a_{n}} \frac{1}{N^{2}} \mathbb{P}\left(N_{n}\left(X_{1}, \theta, \mathcal{D}_{n}\right)=N\right) \mathbb{E}\left[\left|\sum_{i=1}^{N} \varepsilon_{i}\right|^{2}\right] \\
& =\sum_{N=1}^{a_{n}} \frac{1}{N^{2}} \mathbb{P}\left(N_{n}\left(X_{1}, \theta, \mathcal{D}_{n}\right)=N\right) \sum_{j=1}^{d} \mathbb{E}\left[\left|\sum_{i=1}^{N} \varepsilon_{i}^{(j)}\right|^{2}\right]=\sum_{N=1}^{a_{n}} \frac{d \sigma^{2}}{N} \mathbb{P}\left(N_{n}\left(X_{1}, \theta, \mathcal{D}_{n}\right)=N\right)=d \sigma^{2} \mathbb{E}\left[\frac{1}{N_{n}\left(X_{1}, \theta, \mathcal{D}_{n}\right)}\right] .
\end{aligned}
$$

Because of the independence of $X_{1}, \ldots, X_{a_{n}}$, we have that $N_{n}\left(X_{1}, \theta, \mathcal{D}_{n}\right)$ follows a shifted binomial distribution, i.e. $N_{n}\left(X_{1}, \theta, \mathcal{D}_{n}\right)-1 \sim \operatorname{Bin}\left(a_{n}-1, \mathbb{P}\left(X_{2} \in A_{n}\left(X_{1}, \theta\right)\right)\right)$. As [21] showed

$$
\mathbb{E}\left[\frac{1}{N_{n}\left(X_{1}, \theta, \mathcal{D}_{n}\right)}\right] \text { and } \frac{1}{\mathbb{E}\left[N_{n}\left(X_{1}, \theta, \mathcal{D}_{n}\right)\right]}=\frac{1}{a_{n} \mathbb{P}\left(X_{2} \in A_{n}\left(X_{1}, \theta\right)\right)}
$$

are asymptotically equivalent. Hence
If $t_{n}=2^{k}$ for some $k \in \mathbb{N}$, we have $\mathbb{P}\left(X_{2} \in A_{n}\left(X_{1}, \theta\right)\right)=1 / t_{n}$, because of the splitting of the naive tree. Otherwise, $t_{n} \in\left\{2^{k-1}+1,2^{k-1}+2, \ldots, 2^{k-1}\right\}$ for some $k \in \mathbb{N}$ for some and we get $\mathbb{P}\left(X_{2} \in A_{n}\left(X_{1}, \theta\right)\right) \in\left[2^{-k-1}, 2^{-k}\right]$ and consequently $t_{n} \mathbb{P}\left(X_{2} \in A_{n}\left(X_{1}, \theta\right)\right) \in[1 / 2,1]$. Therefore

$$
\lim _{n \rightarrow \infty} \mathbb{E}\left[\left|\frac{1}{N_{n}\left(X_{1}, \theta, \mathcal{D}_{n}\right)} \sum_{i=1}^{n} \varepsilon_{i} \mathbb{1}_{G_{n}\left(\Theta, \mathcal{D}_{n}\right)}\left(X_{i}\right)\right|^{2}\right]=0
$$




---

since $\lim _{n \rightarrow \infty} t_{n} / a_{n}=0$. Define

$$
m(X) A_{n}\left(X^{\prime}, \Theta\right):=\frac{1}{N_{n}\left(X^{\prime}, \Theta, \mathcal{D}_{n}\right)} \sum_{i=1}^{n} m\left(X_{i}\right) \mathbb{1}_{G_{n}\left(\Theta, \mathcal{D}_{n}\right)}\left(\Theta, \mathcal{D}_{n}\right)\left(X_{i}\right)
$$

and find an upper bound for the approximation error through

$$
\begin{aligned}
& \mathbb{E}\left[\left\|m\left(X^{\prime}\right)-m_{n, 1}\left(X^{\prime}, \Theta\right)\right\|^{2}\right] \\
= & \mathbb{E}\left[\left\|m\left(X^{\prime}\right)-\frac{1}{N_{n}\left(X^{\prime}, \Theta, \mathcal{D}_{n}\right)} \sum_{i=1}^{n} Y_{i} \mathbb{1}_{G_{n}\left(\Theta, \mathcal{D}_{n}\right)}\left(X_{i}\right)\right\|^{2}\right] \\
= & \mathbb{E}\left[\left\|m\left(X^{\prime}\right)-m(X) A_{n}\left(X^{\prime}, \Theta\right)-\frac{1}{N_{n}\left(X^{\prime}, \Theta, \mathcal{D}_{n}\right)} \sum_{i=1}^{n} \varepsilon_{i} \mathbb{1}_{G_{n}\left(\Theta, \mathcal{D}_{n}\right)}\left(X_{i}\right)\right\|^{2}\right] \\
\leqslant & 2 \mathbb{E}\left[\left\|m\left(X^{\prime}\right)-m(X) A_{n}\left(X^{\prime}, \Theta\right)\right\|^{2}\right]+2 \mathbb{E}\left[\left\|\frac{1}{N_{n}\left(X^{\prime}, \Theta, \mathcal{D}_{n}\right)} \sum_{i=1}^{n} \varepsilon_{i} \mathbb{1}_{G_{n}\left(\Theta, \mathcal{D}_{n}\right)}\left(X_{i}\right)\right\|^{2}\right] \\
\leqslant & 2 \mathbb{E}\left[\sup _{x, x^{\prime} \in A_{n}\left(X^{\prime}, \Theta\right)}\left\|m(x)-m\left(x^{\prime}\right)\right\|^{2}\right] \\
& +2 \mathbb{E}\left[\left\|\frac{1}{N_{n}\left(X^{\prime}, \Theta, \mathcal{D}_{n}\right)} \sum_{i=1}^{n} \varepsilon_{i} \mathbb{1}_{G_{n}\left(\Theta, \mathcal{D}_{n}\right)}\left(X_{i}\right)\right\|^{2}\right]
\end{aligned}
$$

The function $m$ is continuous and defined on a compact set, and therefore it exists $K>0$ such that $\|m(x)\| \leqslant K$ for all $x \in[0,1]^{p}$. Let $\xi>0$, then for $a_{n}$ sufficiently small $\delta>0$,

$$
\begin{aligned}
& \lim _{n \rightarrow \infty} \mathbb{P}\left[\sup _{x, x^{\prime} \in A_{n}\left(X^{\prime}, \Theta\right)}\left\|m(x)-m\left(x^{\prime}\right)\right\|^{2}>\xi\right] \\
& \leqslant \lim _{n \rightarrow \infty}\left(\mathbb{P}\left[\sup _{\substack{x, x^{\prime} \in A n\left(\bar{X}^{\prime}, \Theta\right) \\\left\|x-x^{\prime}\right\| \leqslant \delta}}\left\|m(x)-m\left(x^{\prime}\right)\right\|^{2}>\xi\right]+\mathbb{P}\left[\sup _{\substack{x, x^{\prime} \in A_{n}\left(X^{\prime}, \Theta\right) \\\left\|x-x^{\prime}\right\| \leqslant \delta}}\left\|m(x)-m\left(x^{\prime}\right)\right\|^{2}>\xi\right]\right) \\
& \leqslant \mathbb{P}\left[\sup _{\substack{x, x^{\prime} \in[0,1]^{p} \\\left\|x-x^{\prime}\right\| \leqslant \delta}}\left\|m(x)-m\left(x^{\prime}\right)\right\|^{2}>\xi\right]+\lim _{n \rightarrow \infty} \mathbb{P}\left[x, x^{\prime} \in A_{n}\left(X^{\prime}, \Theta\right),\left\|x-x^{\prime}\right\|>\delta\right] \\
& =0+\lim _{n \rightarrow \infty} \mathbb{P}\left[x, x^{\prime} \in A_{n}\left(X^{\prime}, \Theta\right),\left\|x-x^{\prime}\right\|>\delta\right] \\
& \leqslant \lim _{n \rightarrow \infty} \mathbb{P}\left[\operatorname{diam}\left(A_{n}\left(X_{i}, \Theta\right)\right)>\delta\right]=0
\end{aligned}
$$

where the first equality holds true because $m$ is continous and the last step holds true because of Lemma 1 . Consequently

$$
\begin{aligned}
& \mathbb{E}\left[\sup _{x, x^{\prime} \in A_{n}\left(X^{\prime}, \Theta\right)}\left\|m(x)-m\left(x^{\prime}\right)\right\|^{2}\right] \\
& \leqslant \mathbb{P}\left[\sup _{x, x^{\prime} \in A_{n}\left(X^{\prime}, \Theta\right)}\left\|m(x)-m\left(x^{\prime}\right)\right\|^{2}>\xi\right] 4 K^{2}+\xi \\
& <\left(4 K^{2}+1\right) \xi
\end{aligned}
$$

for $n$ large enough. Because of (5), (6) and (7) the proof is completed, when $\xi \rightarrow 0$.

# B Proof of Theorem 4.1 

Proof of Theorem 4.1. Let $A \subseteq[0,1]^{p}$ be a set on a node of a regression tree. Let $A_{L}, A_{R}$ be the partition made by Algorithm 1 and $A_{L}^{e x T}, A_{R}^{e x T}$ the partition made by the ExtraTree algorithm and the same $\Theta$. For clarity, the dependence of $A_{L}, A_{R}, A_{L}^{e x T}$ and $A_{R}^{e x T}$ on $\Theta$ and the data is omitted in the notation in this proof. We obviously get

$$
L_{n}\left(A_{L}\right) \leqslant L_{n}\left(A_{L}^{e x T}\right)
$$




---

almost surely for every realization of $\Theta$ because of the argmax-step in Algorithm 2. For this proof it's sufficient, that $L^{n}\left(A_{L}^{e x T}\right)$ is stochastically larger than $L^{n}\left(A_{L}\right)$. The inequality (8) holds for every $A \in\left\{\left[a_{1}, b_{1}\right] \times \ldots \times\left[a_{p}, b_{p}\right]\right.$ : $\left.0 \leqslant a_{k}<b_{k} \leqslant 1 \forall k \in\{1, \ldots, p\}\right\} \cup\{H\}$ and is equivalent to

$$
\begin{aligned}
& \sum_{i=1}^{n} \sum_{j=1}^{d}\left(Y_{i}^{(j)}-\mathbb{Y}_{A_{L}^{e x T}}^{(j)}\left(X_{i}\right)-\mathbb{Y}_{A_{R}^{e x T}}^{(j)}\left(X_{i}\right)\right)^{2} \mathbb{1}_{A}\left(X_{i}\right) \\
& \leqslant \sum_{i=1}^{n} \sum_{j=1}^{d}\left(Y_{i}^{(j)}-\mathbb{Y}_{A_{L}}^{(j)}\left(X_{i}\right)-\mathbb{Y}_{A_{R}}^{(j)}\left(X_{i}\right)\right)^{2} \mathbb{1}_{A}\left(X_{i}\right) \\
& =: \sum_{i=1}^{n} \sum_{j=1}^{d} h\left(A_{L}, A_{R}\right) \mathbb{1}_{A}\left(X_{i}\right)
\end{aligned}
$$

almost surely. That means, we have that the ExtraTree is splitwise "better" than the naive tree. By induction, we can show that the whole partition of the ExtraTree is better than the naive tree in the sense of our chosen quality criterion. Let $A$ be a cell at the $(\ell-1)$-th level of the tree from Algorithm 2 and $A_{\ell}(X)$ the cell containing $X$ on the $l$-th level of the tree from Algorithm 1. Analogously define $A^{e x \ell, \ell}(X)$ for the ExtraTree algorithm. Then

$$
\begin{aligned}
& \sum_{i=1}^{n} \sum_{j=1}^{d} h\left(A_{\ell}\left(X_{i}\right)_{L}, A_{\ell}\left(X_{i}\right)_{R}\right) \mathbb{1}_{A}\left(X_{i}\right) \\
= & \sum_{i=1}^{n} \sum_{j=1}^{d} h\left(\left(A_{L}\right)_{L},\left(A_{L}\right)_{R}\right) \mathbb{1}_{A_{L}}\left(X_{i}\right)+h\left(\left(A_{R}\right)_{L},\left(A_{R}\right)_{R}\right) \mathbb{1}_{A_{R}}\left(X_{i}\right) \\
= & \sum_{i=1}^{n} \sum_{j=1}^{d} h\left(\left(A_{L} \backslash A_{L}^{e x T}\right)_{L},\left(A_{L} \backslash A_{L}^{e x T}\right)_{R}\right) \mathbb{1}_{\left(A_{L} \backslash A_{L}^{e x T}\right)_{L}}\left(X_{i}\right) \\
+ & h\left(\left(A_{L} \cap A_{L}^{e x T}\right)_{L},\left(A_{L} \cap A_{L}^{e x T}\right)_{R}\right) \mathbb{1}_{A_{L} \cap A_{L}^{e x T}}\left(X_{i}\right) \\
+ & h\left(\left(A_{R} \backslash A_{R}^{e x T}\right)_{L},\left(A_{R} \backslash A_{R}^{e x T}\right)_{R}\right) \mathbb{1}_{\left(A_{R} \backslash A_{R}^{e x T}\right)_{L}}\left(X_{i}\right) \\
+ & h\left(\left(A_{R} \cap A_{R}^{e x T}\right)_{L},\left(A_{R} \cap A_{R}^{e x T}\right)_{R}\right) \mathbb{1}_{A_{R} \cap A_{R}^{e x B}}\left(X_{i}\right) \\
\stackrel{(9)}{\geqslant} & \sum_{i=1}^{n} \sum_{j=1}^{d} h\left(\left(A_{L} \backslash A_{L}^{e x T}\right)_{L}^{e x T},\left(A_{L} \backslash A_{L}^{e x T}\right)_{R}^{e x T}\right) \mathbb{1}_{\left(A_{L} \backslash A_{L}^{e x T}\right)_{L}^{e x T}}\left(X_{i}\right) \\
+ & h\left(\left(A_{L} \cap A_{L}^{e x T}\right)_{L}^{e x T},\left(A_{L} \cap A_{L}^{e x T}\right)_{R}^{e x T}\right) \mathbb{1}_{A_{L} \cap A_{L}^{e x T}}\left(X_{i}\right) \\
+ & h\left(\left(A_{R} \backslash A_{R}^{e x T}\right)_{L}^{e x T},\left(A_{R} \backslash A_{R}^{e x T}\right)_{R}^{e x T}\right) \mathbb{1}_{\left(A_{R} \backslash A_{R}^{e x T}\right)_{L}^{e x T}}\left(X_{i}\right) \\
+ & h\left(\left(A_{R} \cap A_{R}^{e x T}\right)_{L}^{e x T},\left(A_{R} \cap A_{R}^{e x T}\right)_{R}^{e x T}\right) \mathbb{1}_{A_{R} \cap A_{R}^{e x T}}\left(X_{i}\right) \\
= & \sum_{i=1}^{n} \sum_{j=1}^{d} h\left(\left(A_{L}^{e x T}\right)_{L}^{e x T},\left(A_{L}^{e x T}\right)_{R}^{e x T}\right) \mathbb{1}_{A_{L}^{e x T}}\left(X_{i}\right) \\
+ & h\left(\left(A_{R}^{e x T}\right)_{L}^{e x T},\left(A_{R}^{e x T}\right)_{R}^{e x T}\right) \mathbb{1}_{A_{R}^{e x T}}\left(X_{i}\right) \\
= & \sum_{i=1}^{n} \sum_{j=1}^{d} h\left(A^{e x T, \ell}\left(X_{i}\right)_{L}, A^{e x T, \ell}\left(X_{i}\right)_{R}\right) \mathbb{1}_{A}\left(X_{i}\right)
\end{aligned}
$$

holds true, where $A=\left(A_{L}^{e x T}\right)_{\cup}^{e x T}\left(A_{R}^{e x T}\right)$ denotes the partition of a set $A$ made by the ExtraTree algorithm. The inequality holds true because of the induction requirement (9) and $A_{L} \backslash A_{L}^{e x T}, A_{R} \backslash A_{R}^{e x T}, A_{L} \cap A_{L}^{e x T}, A_{R} \cap A_{R}^{e x} \in$ $\left\{\left[a_{1}, b_{1}\right] \times \ldots \times\left[a_{p}, b_{p}\right]: 0 \leqslant a_{k}<b_{k} \leqslant 1 \forall k \in\{1, \ldots, p\}\right\} \cup\{H\}$. Denote $A_{T}(X)=A_{n}(\mathrm{X}, \Theta)$ the leaf cell containing $X


---

Because of (10) the inequality can be extended to an arbitrary level of the tree and therefore

$$
\begin{aligned}
& \sum_{i=1}^{n} \sum_{j=1}^{d} \frac{\left(Y_{i}^{(j)}-Y_{A_{T-1}\left(X_{i}\right) L}^{(j)}\right)^{2} \mathbb{1}_{A_{T-1}\left(X_{i}\right) L}+Y_{A_{T-1}\left(X_{i}\right) R}^{(j)} \mathbb{1}_{A_{T-1}\left(X_{i}\right) R}}{\mathbb{1}_{A}\left(X_{i}\right)} \\
& \quad \geqslant \sum_{i=1}^{n} \sum_{j=1}^{d} \frac{\left(Y_{i}^{(j)}-Y_{A_{\text {ex } T, T-1}\left(X_{i}\right) L}^{(j)}\right)^{2} \mathbb{1}_{A_{\text {ex } T, T-1}\left(X_{i}\right) L}-Y_{A_{\text {ex } T, T-1}\left(X_{i}\right) R}^{(j)} \mathbb{1}_{A_{\text {ex } T, T-1}\left(X_{i}\right) R}}{\mathbb{1}_{A}\left(X_{i}\right)}
\end{aligned}
$$

The regression estimator $m_{n, 1}^{(j)}\left(X_{i}, \Theta, \mathcal{D}_{n}\right)$ is either $Y_{A_{\text {ex } T, T-1}\left(X_{i}\right) L}^{(j)}$ or $Y_{A_{\text {ex } T, T-1}\left(X_{i}\right) R}^{(j)}$ depending on the direction of the last split. Because $A_{\text {ex } T, T-1}\left(X_{i}\right) L$ and $A_{T-1}\left(X_{i}\right) L$ are disjoint (and the same argument for $A_{T-1}\left(X_{i}\right) L$ and $\left.A_{\text {ex } T, T-1}\left(X_{i}\right) L\right)$ the inequality (11) is for $A=[0,1]^{s}$ almost surely the same as

$$
\sum_{i=1}^{n} \sum_{j=1}^{d}\left(Y_{i}^{(j)}-m_{n, 1}^{(j)}\left(X_{i}, \Theta, \mathcal{D}_{n}\right)\right)^{2} \geqslant \sum_{i=1}^{n} \sum_{j=1}^{d}\left(Y_{i}^{(j)}-m_{n, 1}^{\operatorname{ex} T,(j)}\left(X_{i}, \Theta, \mathcal{D}_{n}\right)\right)^{2}
$$

Adding the expectation operator, multiplying out the summands and using $Y_{i}^{(j)}=m^{(j)}\left(X_{i}\right)+\varepsilon_{i}^{(j)}$ yields

$$
\begin{aligned}
& \mathrm{E}\left[\left(Y_{i}^{(j)}-m_{n, 1}^{(j)}\left(X_{i}, \Theta, \mathcal{D}_{n}\right)\right)^{2}\right] \\
& \quad=\mathrm{E}\left[\left(\varepsilon_{i}^{(j)}\right)^{2}+\left(m^{(j)}\left(X_{i}\right)_{i}-m_{n, 1}^{(j)}\left(X_{i}, \Theta, \mathcal{D}_{n}\right)\right)^{2}+2 \varepsilon_{i}^{(j)}\left(m^{(j)}\left(X_{i}\right)_{i}-m_{n, 1}^{(j)}\left(X_{i}, \Theta, \mathcal{D}_{n}\right)\right)\right] \\
& \quad=\mathrm{E}\left[\left(\varepsilon_{i}^{(j)}\right)^{2}+\left(m^{(j)}\left(X_{i}\right)_{i}-m_{n, 1}^{(j)}\left(X_{i}, \Theta, \mathcal{D}_{n}\right)\right)^{2}\right]+2 \mathrm{E}\left[\varepsilon_{i}^{(j)} m^{(j)}\left(X_{i}\right)\right]-2 \mathrm{E}\left[\varepsilon_{i}^{(j)} m_{n, 1}^{(j)}\left(X_{i}, \Theta, \mathcal{D}_{n}\right)\right]
\end{aligned}
$$

Due to the independence of $\varepsilon$ and $X$ we get for the last summand

$$
\begin{aligned}
\mathrm{E}\left[\varepsilon_{i}^{(j)} m_{n, 1}^{(j)}\left(X_{i}, \Theta, \mathcal{D}_{n}\right)\right] & =\mathrm{E}\left[\varepsilon_{i}^{(j)} \sum_{k=1}^{n} W_{k}\left(X_{i}, \Theta, \mathcal{D}_{n}\right) Y_{k}^{(j)}\right] \\
& =\mathrm{E}\left[\varepsilon_{i}^{(j)} \sum_{k=1}^{n} W_{k}\left(X_{i}, \Theta, \mathcal{D}_{n}\right)\left(m^{(j)}\left(X_{k}\right)+\varepsilon_{k}^{(j)}\right)\right] \\
& =\sum_{k=1}^{n} \mathrm{E}\left[\varepsilon_{i}^{(j)}\right] \mathrm{E}\left[W_{k}\left(X_{i}, \Theta, \mathcal{D}_{n}\right) m^{(j)}\left(X_{k}\right)\right] \\
& +\sum_{k=1}^{n} \mathrm{E}\left[\varepsilon_{i}^{(j)} W_{k}\left(X_{i}, \Theta, \mathcal{D}_{n}\right) \varepsilon_{k}^{(j)}\right] \\
& =\sum_{k=1}^{n} \mathrm{E}\left[\varepsilon_{i}^{(j)} W_{k}\left(X_{i}, \Theta, \mathcal{D}_{n}\right) \varepsilon_{k}^{(j)}\right] \\
& =\mathrm{E}\left[\left(\varepsilon_{i}^{(j)}\right)^{2} W_{i}\left(X_{i}, \Theta, \mathcal{D}_{n}\right)\right] \\
& =\sigma_{j}^{2} \mathrm{E}\left[W_{i}\left(X_{i}, \Theta, \mathcal{D}_{n}\right)\right]
\end{aligned}
$$

where $\varepsilon_{i}^{(j)}$ denotes the $j$-th component of $\varepsilon_{i}, i \in\{1, \ldots, n\}$ and $j \in\{1, \ldots, d\}$. Conditioned on $\Theta$ the expectation of the weights can be rewritten as

$$
\begin{aligned}
\mathrm{E}\left[W_{i}\left(X_{i}, \Theta, \mathcal{D}_{n}\right)\right] & =\mathrm{E}\left[\frac{1}{N_{n}\left(X_{i}, \Theta, \mathcal{D}_{n}\right)}\right] \\
& =\sum_{k=1}^{n} \frac{1}{k} \cdot \mathrm{P}\left(N_{n}\left(X_{i}, \Theta, \mathcal{D}_{n}\right)=k\right) \\
& =\sum_{k=0}^{n-1} \frac{1}{k+1} \cdot \mathrm{P}\left(N_{n}\left(X_{i}, \Theta, \mathcal{D}_{n}\right)=k+1\right) \\
& =\sum_{k=0}^{n-1} \frac{1}{k+1}\binom{n-1}{k} \mathrm{P}\left(X \in A_{n}\left(X_{1}, \Theta\right)\right)^{k}\left(1-\mathrm{P}\left(X \in A_{n}\left(X_{1}, \Theta\right)\right)\right)^{n-k-1}
\end{aligned}
$$


---

For every $\pi \in(0,1)$

$$
\begin{aligned}
\sum_{k=0}^{n-1} \frac{1}{k+1}\binom{n-1}{k} \pi^{k}(1-\pi)^{n-k-1} & =\frac{1}{n} \sum_{k=0}^{n-1}\binom{n}{k+1} \pi^{k}(1-\pi)^{n-k-1} \\
& =\frac{1}{n \pi} \sum_{k=1}^{n}\binom{n}{k} \pi^{k}(1-\pi)^{n-k}=\frac{1}{n \pi} \cdot\left(1-(1-\pi)^{n}\right)=: f(\pi)
\end{aligned}
$$

holds true. Because of

$$
\frac{\mathrm{B}}{\mathrm{B} \pi} f(\pi)=n \frac{(1-\pi)^{n-1} \pi+(1-\pi)^{n}-1}{n \pi^{2}} \leqslant 0
$$

$f$ is a decreasing function.
Note that the feature space $[0,1]^{p}$ is partitioned into disjoint subspaces



Figure 3: $f$ for different $n$
$A_{n, 1}(\Theta), \ldots, A_{n, t_{n}}(\Theta)$. The set $A_{n}(X, \Theta)$ containing $X$ is equal to one of those sets and the probability, that $X$ and $X^{\prime}$ are falling into the same cell is given as

$$
\mathbb{P}\left(X \in A_{n}\left(X^{\prime}, \Theta\right)\right)=\sum_{t=1}^{t_{n}} \mathbb{P}\left(X, X^{\prime} \in A_{n, t}(\Theta)\right)=\sum_{t=1}^{t_{n}} \mathbb{P}\left(X \in A_{n, t}(\Theta)\right)^{2}
$$

is minimized when $\mathbb{P}\left(X \in A_{n, t}(\Theta)\right)=\frac{1}{t_{n}}$ for all $t \in\left\{1, \ldots, t_{n}\right\}$, i.e $\frac{1}{t_{n}}$ is the minimal possible value for $\mathbb{P}\left(X \in A_{n, t}(\Theta)\right)$. As discussed in the proof of Proof of Theorem 3.1 for the naive tree $\mathbb{P}\left(X \in A_{n, t}(\Theta)\right) \in\left[\frac{1}{2}, 1\right]$ holds. Putting this together with (14) provides

$$
\lim _{n \rightarrow \infty} 2 \mathbb{E}\left[W_{i}\left(X_{i}, \Theta, \mathcal{D}_{n}\right)\right] \geqslant \lim _{n \rightarrow \infty} \mathbb{E}\left[W_{i}^{\text {exT }}\left(X_{i}, \Theta, \mathcal{D}_{n}\right)\right]
$$

From (14) we can conclude with $p_{n}=\mathbb{P}\left(X_{2} \in A_{n}\left(X_{1}, \Theta\right)\right)$, that

$$
\mathbb{E}\left[W_{i}\left(X_{i}, \Theta, \mathcal{D}_{n}\right)\right]=\frac{1}{n} \sum_{k=0}^{n-1} \frac{1}{k}\binom{n}{k}\left(p_{n}\right)^{k}\left(1-p_{n}\right)^{n-k-1} \leqslant \frac{1}{n}
$$




---

which enforces

$$
\lim _{n \rightarrow \infty} \mathbb{E}\left[W_{i}\left(X_{i}, \Theta, \mathcal{D}_{n}\right)\right]=\lim _{n \rightarrow \infty} \mathbb{E}\left[W_{i}^{\mathrm{exT}}\left(X_{i}, \Theta, \mathcal{D}_{n}\right)\right]=0
$$

Hence with the same calculations as in (13) and (15) one can see

$$
\begin{aligned}
& \lim _{n \rightarrow \infty} \mathbb{E}\left[\varepsilon_{i}^{(j)}\left(m^{(j)}\left(X_{i}\right)-m_{n, 1}^{\mathrm{exT},(j)}\left(X_{i}, \Theta, \mathcal{D}_{n}\right)\right)\right]=\mathbb{E}\left[\varepsilon_{i}^{(j)} m^{(j)}\left(X_{i}\right)\right]-\lim _{n \rightarrow \infty} \mathbb{E}\left[\varepsilon_{i}^{(j)} m_{n, 1}^{\mathrm{exT},(j)}\left(X_{i}, \Theta, \mathcal{D}_{n}\right)\right] \\
= & \mathbb{E}\left[\varepsilon_{i}^{(j)}\right] \mathbb{E}\left[m^{(j)}\left(X_{i}\right)\right]-\lim _{n \rightarrow \infty} \mathbb{E}\left[W_{i}^{\mathrm{exT}}\left(X_{i}, \Theta, \mathcal{D}_{n}\right)\right]=0
\end{aligned}
$$

Together with (12) this has the result that

$$
\begin{aligned}
& \lim _{n \rightarrow \infty} \mathbb{E}\left[\frac{1}{n} \sum_{i=1}^{n}\left\|m\left(X_{i}\right)-m_{n, 1}^{\mathrm{exT},(j)}\left(X_{i}, \Theta, \mathcal{D}_{n}\right)\right\|^{2}\right] \\
= & \lim _{n \rightarrow \infty} \mathbb{E}\left[\frac{1}{n} \sum_{i=1}^{n} \sum_{j=1}^{d}\left\{\left(m^{(j)}\left(X_{i}\right)-m_{n, 1}^{\mathrm{exT},(j)}\left(X_{i}, \Theta, \mathcal{D}_{n}\right)\right)^{2}+\left(\varepsilon_{i}^{(j)}\right)^{2}-\left(\varepsilon_{i}^{(j)}\right)^{2}+2 \varepsilon_{i}^{(j)}\left(m^{(j)}\left(X_{i}\right)-m_{n, 1}^{\mathrm{exT}, j)}\left(X_{i}, \Theta, \mathcal{D}_{n}\right)\right)\right\}\right] \\
= & \lim _{n \rightarrow \infty} \mathbb{E}\left[\frac{1}{n} \sum_{i=1}^{n} \sum_{j=1}^{d}\left(Y_{i}^{(j)}-m_{n, 1}^{\mathrm{exT},(j)}\left(X_{i}, \Theta, \mathcal{D}_{n}\right)\right)^{2}\right]-\mathbb{E}\left[\left(\varepsilon_{i}^{(j)}\right)^{2}\right] \\
\leqslant & \lim _{n \rightarrow \infty} \mathbb{E}\left[\sum_{i=1}^{n} \sum_{j=1}^{d}\left(Y_{i}^{(j)}-m_{n, 1}^{(j)}\left(X_{i}, \Theta, \mathcal{D}_{n}\right)\right)^{2}\right]-\mathbb{E}\left[\left(\varepsilon_{i}^{(j)}\right)^{2}\right] \\
= & \lim _{n \rightarrow \infty} \mathbb{E}\left[\frac{1}{n} \sum_{i=1}^{n} \sum_{j=1}^{d}\left\{\left(m^{(j)}\left(X_{i}\right)-m_{n, 1}^{(j)}\left(X_{i}, \Theta, \mathcal{D}_{n}\right)\right)^{2}+\left(\varepsilon_{i}^{(j)}\right)^{2}-\left(\varepsilon_{i}^{(j)}\right)^{2}+2 \varepsilon_{i}^{(j)}\left(m^{(j)}\left(X_{i}\right)-m_{n, 1}^{(j)}\left(X_{i}, \Theta, \mathcal{D}_{n}\right)\right)\right\}\right] \\
= & \lim _{n \rightarrow \infty} \mathbb{E}\left[\frac{1}{n} \sum_{i=1}^{n}\left\|m\left(X_{i}\right)-m_{n, 1}\left(X_{i}, \Theta, \mathcal{D}_{n}\right)\right\|^{2}\right]
\end{aligned}
$$

holds true. This leads to,

$$
\lim _{n \rightarrow \infty} \mathbb{E}\left[\left\|m\left(X_{i}\right)-m_{n, 1}^{\mathrm{exT}}\left(X_{i}, \Theta, \mathcal{D}_{n}\right)\right\|^{2}\right] \leqslant \lim _{n \rightarrow \infty} \mathbb{E}\left[\left\|m\left(X_{i}\right)-m_{n, 1}\left(X_{i}, \Theta, \mathcal{D}_{n}\right)\right\|^{2}\right]
$$

for every $i \in\{1, \ldots, n\}$, because of the i.i.d. assumption. Let $X_{n}^{*}=\operatorname{argmin}_{X_{i} \in A_{n}(X, \Theta)}\left\|X_{i}-X\right\|$ be the nearest neighbor of $X$ in $A_{n}(X, \Theta)$, then $m_{n, 1}^{\mathrm{exT}}\left(x, \Theta, \mathcal{D}_{n}\right)=m_{n, 1}^{\mathrm{exT}}\left(X_{i}, \Theta, \mathcal{D}_{n}\right)$ and

$$
\begin{aligned}
\lim _{n \rightarrow \infty} \mathbb{E}\left[\left\|m(X)-m_{n, 1}^{\mathrm{exT}}\left(X, \Theta, \mathcal{D}_{n}\right)\right\|^{2}\right] & \leqslant \lim _{n \rightarrow \infty} 2 \mathbb{E}\left[\left\|m(X)-m\left(X_{n}^{*}\right)\right\|^{2}\right] \\
& +\lim _{n \rightarrow \infty} 2 \mathbb{E}\left[\left\|m\left(X_{n}^{*}\right)-m_{n, 1}^{\mathrm{exT}}\left(X_{n}^{*}, \Theta, \mathcal{D}_{n}\right)\right\|^{2}\right] \\
& \leqslant \lim _{n \rightarrow \infty} 2 \mathbb{E}\left[\left\|m(X)-m\left(X_{n}^{*}\right)\right\|^{2}\right] \\
& +\lim _{n \rightarrow \infty} 2 \mathbb{E}\left[\left\|m\left(X_{n}^{*}\right)-m_{n, 1}\left(X_{n}^{*}, \Theta, \mathcal{D}_{n}\right)\right\|^{2}\right] \\
& =\lim _{n \rightarrow \infty} 2 \mathbb{E}\left[\left\|m(X)-m\left(X_{n}^{*}\right)\right\|^{2}\right] .
\end{aligned}
$$

In the second step (17) and in the last step Theorem 3.1 with $a_{n}=n$ was used. The distance between $X$ and $X_{n}^{*}$ becomes arbitrary small if $n$ grows large, because


---

# C Proof of Theorem 4.2 

Proof of Theorem 4.2. Let $Z \sim \mathcal{U}([0,1])$ and $X_{(1)}^{(j)}, \ldots, X_{\left(\left|\mathbb{G}_{n}\left(\Theta, \mathcal{D}_{n}\right)\right|\right)}^{(j)}$ be the ordered $j$-th components of the observations in the drawn subsample $\mathbb{G}_{n}\left(\Theta, \mathcal{D}_{n}\right)$. If $Z \in\left(X_{(k-1)}^{(j)}, X_{(k)}^{(j)}\right)$ for some $k \in\left\{2, \ldots, a_{n}\right\}$, then under the notation of Algorithm 3

$$
\sum_{i=1}^{n}\left\|Y_{i}-Y_{\mathcal{A}^{j}\left(X_{(k)}, \Theta, \mathcal{D}_{n}\right) L} X_{i}^{(j)}<X_{(k)}^{(j)},-Y_{\mathcal{A}^{j}\left(X_{(k)}, \Theta, \mathcal{D}_{n}\right) R} X_{i}^{(j)} \geq X_{(k)}^{(j)}\right\|^{2} \mathbb{1}_{X_{i} \in A}
$$

$$
=\sum_{i=1}^{n}\left\|Y_{i}-Y_{\mathcal{A}^{j}\left(X_{(k)}, \Theta, \mathcal{D}_{n}\right) L} X_{i}^{(j)}<Z-Y_{\mathcal{A}^{j}\left(X_{(k)}, \Theta, \mathcal{D}_{n}\right) R} X_{i}^{(j)} \geq Z\right\|^{2} \mathbb{1}_{X_{i} \in A}
$$

almost surely holds true. This implies $\mathcal{L}_{n}\left(\mathcal{A}^{j}\left(X_{(k)}, \Theta, \mathcal{D}_{n}\right) L\right)=\mathcal{L}_{n}\left(\mathcal{A}^{j}\left(Z, \Theta, \mathcal{D}_{n}\right) L\right)$ almost surely conditioned on $Z \in\left(X_{(k-1)}^{(j)}, X_{(k)}^{(j)}\right)$. We set $X_{(0)}^{(j)}=0$ and $X_{\left(\left|\mathbb{G}_{n}\left(\Theta, \mathcal{D}_{n}\right)\right|+1\right)}^{(j)}=1$. The cummulative probability density function of $\mathcal{L}_{n}\left(\mathcal{A}^{j}\left(Z, \Theta, \mathcal{D}_{n}\right) L\right)$ for an arbitrary $x \geqslant 0$ can be rewritten using the law of total probability

$$
\begin{aligned}
\mathbb{P}\left(\mathcal{L}_{n}\left(\mathcal{A}^{j}\left(Z, \Theta, \mathcal{D}_{n}\right) L\right) \leqslant x\right) & =\sum_{k=1}^{\left|\mathbb{G}_{n}\left(\Theta, \mathcal{D}_{n}\right)\right|+1} \mathbb{P}\left(\mathcal{L}_{n}\left(\mathcal{A}^{j}\left(Z, \Theta, \mathcal{D}_{n}\right) L\right) \leqslant x \mid Z \in\left(X_{(k-1)}^{(j)}, X_{(k)}^{(j)}\right)\right) \\
& \mathbb{P}\left(Z \in\left(X_{(k-1)}^{(j)}, X_{(k)}^{(j)}\right)\right) \\
& =\sum_{k=1}^{\left|\mathbb{G}_{n}\left(\Theta, \mathcal{D}_{n}\right)\right|+1} \mathbb{P}\left(\mathcal{L}_{n}\left(\mathcal{A}^{j}\left(X_{(k)}, \Theta, \mathcal{D}_{n}\right) L\right) \leqslant x \mid Z \in\left(X_{(k-1)}^{(j)}, X_{(k)}^{(j)}\right)\right) \\
& \mathbb{P}\left(Z \in\left(X_{(k-1)}^{(j)}, X_{(k)}^{(j)}\right)\right) \\
& =\mathbb{P}\left(\mathcal{L}_{n}\left(\mathcal{A}^{j}\left(X_{(k)}, \Theta, \mathcal{D}_{n}\right) L\right) \leqslant x\right) .
\end{aligned}
$$

Without loss of generality let $X_{(1)} \in \mathbb{G}_{n}\left(\Theta, \mathcal{D}_{n}\right)$, then (19) results in

$$
\begin{aligned}
\mathbb{P}\left(\mathcal{L}_{n}\left(\mathcal{A}^{\mathrm{CART}}\left(\Theta, \mathcal{D}_{n}\right) L\right) \leqslant x\right) & =\mathbb{P}\left(\max _{j \in \mathcal{M}_{\mathrm{try}, X_{k} \in \mathbb{G}_{n}\left(\Theta, \mathcal{D}_{n}\right)}} \mathcal{L}_{n}\left(\mathcal{A}^{j}\left(X_{k}, \Theta, \mathcal{D}_{n}\right) L\right) \leqslant x\right) \\
& \leqslant \mathbb{P}\left(\max _{j \in \mathcal{M}_{\mathrm{try}}} \mathcal{L}_{n}\left(\mathcal{A}^{j}\left(X_{(1)}, \Theta, \mathcal{D}_{n}\right) L\right) \leqslant x\right)=\mathbb{P}\left(\max _{j \in \mathcal{M}_{\mathrm{try}}} \mathcal{L}_{n}\left(\mathcal{A}^{j}\left(Z, \Theta, \mathcal{D}_{n}\right) L\right) \leqslant x\right) \\
& \leqslant \mathbb{P}\left(\mathcal{L}_{n}\left(\mathcal{A}(\Theta) L\right) \leqslant x\right)
\end{aligned}
$$

where $\mathcal{A}(\Theta) L$ denotes the left cell resulting from the naive splitting and $\mathcal{L}_{n}$ the splitting criterion on the set drawn without replacement. Because $\mathcal{L}_{n}\left(\mathcal{A}^{\mathrm{CART}}\left(\Theta, \mathcal{D}_{n}\right) L\right)$ is stochastically larger than $\mathcal{L}_{n}(\mathcal{A}(\Theta) L)$, the rest of the proof is analogously to the proof of Theorem 4.1.

Proof of Corollary 4.3. For this proof the finite form of Jensen's inequality is used, i.e. we use that for every convex function $f$, numbers $x_{1}, \ldots, x_{M} \in \mathbb{R}$ and weights $\lambda_{1}, \ldots, \lambda_{M}$ the inequality

$$
f\left(\frac{\sum_{t=1}^{M} \lambda_{t} x_{t}}{\sum_{t=1}^{M} \lambda_{t}}\right) \leqslant \frac{\sum_{t=1}^{M} \lambda_{t} f\left(x_{t}\right)}{\sum_{t=1}^{M} \lambda_{t}}
$$

holds true. Choosing $\lambda_{t}=\frac{1}{M}$ for $t=1, \ldots, M$ Jensen's inequality and the triangle inequality provide

$$
\begin{aligned}
\mathbb{E}\left[\left\|m(X)-m_{n, M}\left(X, \Theta_{1}, \ldots, \Theta_{M}, \mathcal{D}_{n}\right)\right\|^{2}\right] & =\mathbb{E}\left[\left\|m(X)-\frac{1}{M} \sum_{t=1}^{M} m_{n, 1}\left(X, \Theta_{t}, \mathcal{D}_{n}\right)\right\|^{2}\right]


---

# D CART Algorithm (within Random Forest) 

```
Algorithm 3: The CART algorithm (within Random Forest)
    Data: The training data $\mathcal{D}_{n}$, the size $a_{n} \in\left\{1, \ldots, n\right.$ \} of the subsample, the maximum number of leaves
        $t_{n} \in\left\{1, \ldots, a_{n}\right\}$, the number of features during the feature subsampling step $m_{t r y} \in\{1, \ldots, p\}$.
    Output: A partition of $[0,1]^{p}$
    Set $n_{\text {nodes }}=1$, level $=0$, the starting partition $\mathcal{P}_{0}=\left\{[0,1]^{p}\right\}$ and $\mathcal{P}_{l}=\varnothing$ for all $1 \leqslant l \leqslant n$;
    Draw a sample a subsample from $\breve{\mathcal{D}}_{n}$ without replacement from the size $a_{n}$;
    while $n_{\text {nodes }}<t_{n}$ and at least one node contains at least two different feature- and output vectors in each case do
        if $\mathcal{P}_{\text {level }}=\varnothing$ then
            level $\leftarrow$ level +1
        else
            Let $A$ be the first element of $\mathcal{P}_{\text {level }}$ if $A$ contains exactly one element then
                $\mathcal{P}_{\text {level }} \leftarrow \mathcal{P}_{\text {level }} \backslash\{A\}$
                $\mathcal{P}_{\text {level }+1} \leftarrow \mathcal{P}_{\text {level }+1} \cup\{A\}$
            else
                Select $m_{t r y}$ dimensions uniformly from $\{1, \ldots, p\}$. Denote the resulting set with $\mathcal{M}_{t r y}$;
                for $j \in \mathcal{M}_{t r y}$ do
                    for $X_{k} \in A$ do
                    Set
 
                        $A_{j}\left(X_{k}, \Theta, \mathcal{D}_{n}\right)^{R}=\left[a_{1}\left(\Theta, \mathcal{D}_{n}\right), b_{1}\left(\Theta, \mathcal{D}_{n}\right)\right] \times \ldots \times\left[a_{j-1}\left(\Theta, \mathcal{D}_{n}\right), b_{j-1}\left(\Theta, \mathcal{D}_{n}\right)\right] \times$
                            $\left.\left[X_{k}^{(j)}, b_{j}\left(\Theta, \mathcal{D}_{n}\right)\right) \times\left[a_{j+1}\left(\Theta, \mathcal{D}_{n}\right), b_{j+1}\left(\Theta, \mathcal{D}_{n}\right)\right] \times \ldots \times\left[a_{p}\left(\Theta, \mathcal{D}_{n}\right), b_{p}\left(\Theta, \mathcal{D}_{n}\right)\right]\right)$,

                    Determine

                    $$
                    \begin{aligned}
                    & L_{n}\left(A_{j}\left(X_{k}, \Theta, \mathcal{D}_{n}\right)^{L}\right)= \\
                    & L_{n}\left(A_{j}\left(X_{k}, \Theta, \mathcal{D}_{n}\right)^{L}, A_{j}\left(X_{k}, \Theta, \mathcal{D}_{n}\right)^{R}\right)= \\
                    & \frac{1}{\left|G_{n}\right|} \sum_{i=1}^{n} \mathbf{1}_{X_{i} \in A}\left(\left\|Y_{i}-Y_{A}\right\|^{2}-\right. \\
                    & \left.\left\|Y_{i}-Y_{A_{j}\left(X_{k}, \Theta, \mathcal{D}_{n}\right)^{L}} \mathbf{1}_{X_{i}^{(j)}}<X_{k}^{(j)}-Y_{A_{j}\left(X_{k}, \Theta, \mathcal{D}_{n}\right)^{R}} \mathbf{1}_{X_{i}^{(j)}} \geqslant X_{k}^{(j)}\right\|^{2}\right)
                    \end{aligned}
                    $$

                    where $\left|G_{n}\right|$ denotes the cardinality of $\left\{i: X_{i} \in A,\left(X_{i}^{J}, Y_{i}^{J}\right) \in \mathcal{D}_{n}\right\}$
                    end
                end
            Choose

            $$
            A^{\mathrm{CART}}\left(\Theta, \mathcal{D}_{n}\right)^{L}=\underset{A_{j}\left(X_{k}, \Theta, \mathcal{D}_{n}\right)^{L} \in \mathcal{A}\left(\mathcal{M}_{t r y}, X_{k}\right)}{\operatorname{argmax}} L_{n}\left(A_{j}\left(X_{k}, \Theta, \mathcal{D}_{n}\right)^{L}\right)
            $$

            where $\mathcal{A}\left(\mathcal{M}_{t r y}, X_{k}\right)=\left\{A_{j}\left(X_{k}, \Theta, \mathcal{D}_{n}\right)^{L}: j \in \mathcal{M}_{t r y}, X_{k} \in A\right\}([7],[8])$ and set $n_{n o d e s}=n_{n o d e s}+1$.
            Denote the resulting cells with $A_{L}^{\mathrm{CART}}$ and $A_{R}^{\mathrm{CART}}$
            $\mathcal{P}_{\text {level }} \leftarrow \mathcal{P}_{\text {level }} \backslash\{A\}$
            $\mathcal{P}_{\text {level }+1} \leftarrow \mathcal{P}_{\text {level }+1} \cup\left\{A_{L}^{\mathrm{CART}}\right\} \cup\left\{A_{R}^{\mathrm{CART}}\right\}$
            $n_{\text {nodes }} \leftarrow n_{\text {nodes }}+1$
            end
    end
    end
```




---



Figure 6: $\bar{x}_{L 2}$ for $M=200$ and $\mathcal{N}\left(0, \sigma^{2}\right)$-distributed errors (CART $=$ green, ExtraTree $=$ blue, naive $=$ red).

# Acknowledgements 

Nico Föge wants to thank Philipp Klein (Otto-von-Guericke Universität Magdeburg) for helpful discussion about the proofs of Theorem 3.1 and Theorem 4.1. This work has been partly supported by the Research Center Trustworthy Data Science and Security (https://rc-trust.ai), one of the Research Alliance Centers within the https://uaruhr.de.

## Funding

The first author was supported by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) 314838170, GRK 2297 MathCoRe. Parts of the simulations were done on the Linux HPC cluster at Technical University Dortmund (LiDO3), partially funded in the course of the Large-Scale Equipment Initiative by the German Research Foundation (DFG) as project 271512359.

## References

[1] S. Athey, J. Tibshirani, and S. Wager. Generalized random forests. Annals of Statistics, 47(2):1148-1178, 2019.
[2] G. Biau. Analysis of a random forests model. Journal of Machine Learning Research, 13:1063-1095, 2012.
[3] G. Biau, L. Devroye, and G. Lugosi. Consistency of random forests and other averaging classifiers. Journal of Machine Learning Research, 9:2015-2033, 2008.
[4] G. Biau and E. Scornet. A random forest guided tour. TEST, 25:197-227, 2016.
[5] R. Blum, M. Hiabu, E. Mammen, and J. T. Meyer. Consistency of random forest type algorithms under a probabilistic impurity decrease condition, 2024.
[6] A. Boulesteix, M. Baillie, D. Edelmann, L. Held, T.P. Morris, and W. Sauerbrei. Editorial for the special collection "towards neutral comparison studies in methodological research", 2024.
[7] L. Breiman. Random forests. Machine Learning, pages 5-32, 2001.




---

[8] L. Breiman, J. Friedman, R. Olshen, and C. Stone. Cart. Classification and regression trees, 1984.
[9] I. Castillo and V. Ročková. Uncertainty quantification for bayesian cart. The Annals of Statistics, 49(6):3482-3509, 2021 .
[10] C.M. Chi et al. Asymptotic properties of high-dimensional random forests. Annals of Statistics, 50(6):3415-3438, 2022 .
[11] Dean De Cock. Ames, iowa: Alternative to the boston housing data as an end of semester regression project. Journal of Statistics Education, 19(3), 2011. Dataset retrieved on $8^{\text {th }}$ of February 2024 from https://www.kaggle.com/datasets/marcopale/housing.
[12] T.L. Fey, M.T. Kai, and F. Wei. Maximizing tree diversity by building complete-random decision trees. In T.B. Ho, D. Cheung, and H. Liu, editors, Advances in Knowledge Discovery and Data Mining PAKDD 2005, volume 3518 of Lecture Notes in Computer Science, Berlin, Heidelberg, 2005. Springer.
[13] S. Friedrich and T. Friede. On the role of benchmarking data sets and simulations in method comparison studies. Biometrical Journal, 66(1):2200212, 2024.
[14] R. Genuer. Variance reduction in purely random forests. Nonparametric Statistics, 24:543-562, 2012.
[15] P. Geurts, D. Ernst, and L. Wehenkel. Extremely randomized trees. Machine Learning, pages 3-42, 2006.
[16] B. Goehry. Random forests for time-dependent processes. ESAIM: Probability and Statistics, pages 801-826, 2020 .
[17] L. Grinsztajn, E. Oyallon, and G. Varoquaux. Why do tree-based models still outperform deep learning on typical tabular data? In Thirty-sixth Conference on Neural Information Processing Systems Datasets and Benchmarks Track, 2022.
[18] I. Gómez-Méndez and E. Joly. On the consistency of a random forest algorithm in the presence of missing entries. Journal of Nonparametric Statistics, pages 983-999, 2023.
[19] M. Haddouchi and A. Berrado. A survey of methods and tools used for interpreting random forest. In 2019 1st International Conference on Smart Systems and Data Science (ICSSD), pages 1-6. IEEE, 2019.
[20] A. Hapfelmeier and K. Ulm. A new variable selection approach using random forests. Computational Statistics \& Data Analysis, 60:50-69, 2013.
[21] S. Hu, X. Wang, W. Yang, and X. Wang. A note on the inverse moment for the non negative random variables. Communications in Statistics-Theory and Methods, 43(8):1750-1757, 2014.
[22] Kuhn and Max. Building predictive models in r using the caret package. Journal of Statistical Software, 28(5):1-26, 2008.
[23] J. H. Maindonald and W. J. Braun. Data analysis and graphics using R. An Example-Based Approach. Cambridge University Press, Cambridge, 3 edition, 2011. The DAAG package was created to support this text.
[24] R.J. McAlexander and L. Mentch. Predictive inference with random forests: A new perspective on classical analyses. Research \& Politics, 7(1):2053168020905487, 2020.
[25] G. Mendez and S. Lohr. Estimating residual variance in random forest regression. Computational statistics \& data analysis, 55(11):2937-2950, 2011.
[26] L. Mentch and G. Hooker. Quantifying uncertainty in random forests via confidence intervals and hypothesis tests. The Journal of Machine Learning Research, 17(1):841-881, 2016.
[27] C. Molnar, G. Casalicchio, and B. Bischl. Interpretable machine learning-a brief history, state-of-the-art and challenges. In Joint European conference on machine learning and knowledge discovery in databases, pages 417-431. Springer, 2020.
[28] T. P. Morris, I. R. White, and M.J. Crowther. Using simulation studies to evaluate statistical methods. Statistics in medicine, 38(11):2074-2102, 2019.
[29] Ilya Nozary. house price in tehran(real data). Dataset retrieved on $8^{\text {th }}$ of February 2024 from https://www.kaggle.com/datasets/ilyanozary/house-price-in-tehranreal-data?select=housePrice.csv.




---

[30] S. Patro and K. Sahu. Normalization: A preprocessing stage. arXiv preprint arXiv:1503.06462, 2015.
[31] P. Probst, M. N. Wright, and A. Boulesteix. Hyperparameters and tuning strategies for random forest. Wiley Interdisciplinary Reviews: data mining and knowledge discovery, 9(3):e1301, 2019.
[32] R Core Team. A Language and Environment for Statistical Computing. R Foundation for Statistical Computing, Vienna, Austria, 2023. https://www.R-project.org/.
[33] B. Ramosaj. Interpretable machines: Constructing valid prediction intervals with random forests. arXiv preprint arXiv:2103.05766, 2021.
[34] B. Ramosaj and M. Pauly. Consistent estimation of residual variance with random forest out-of-bag errors. Statistics \& Probability Letters, 151:49-57, 2019.
[35] B. Ramosaj and M. Pauly. Predicting missing values: a comparative study on non-parametric approaches for imputation. ComputStat, pages 1741-1764, 2019.
[36] B. Ramosaj and M. Pauly. Consistent and unbiased variable selection under independent features using random forest permutation importance. Bernoulli, pages 2101-2118, 2023.
[37] A. Saha, S. Basu, and A. Datta. Random forests for spatially dependent data. Journal of the American Statistical Association, 118(541):665-683, 2023.
[38] L. Schmid, A. Gerharz, A. Groll, and M. Pauly. Tree-based ensembles for multi-output regression: Comparing multivariate approaches with separate univariate ones. Computational Statistics \& Data Analysis, 179:107628, March 2023.
[39] E. Scornet. Consistency of random forests. Poincaré Probab. Statist., 59(1):21-52, 2023.
[40] E. Scornet, G. Biau, and J.P. Vert. Consistency of random forests. Annals of Statistics, 43(4):1716-1741, 2015.
[41] D.J. Stekhoven and P. Bühlmann. Missforest-non-parametric missing value imputation for mixed-type data. Bioinformatics, pages 112-118, Jan 2011.
[42] S. Wager and S. Athey. Estimation and inference of heterogeneous treatment effects using random forests. Journal of the American Statistical Association, 113(523):1228-1242, 2018.
[43] S. Wager and S. Athey. Estimation and inference of heterogeneous treatment effects using random forests. Journal of the American Statistical Association, 113(523):1228-1242, 2018.
[44] Z. Wang, Y. Wang, R. Zeng, R.S. Srinivasan, and S. Ahrentzen. Random forest based hourly building energy prediction. Energy and Buildings, 171:11-25, 2018.
[45] M.N. Wright and A. Ziegler. ranger: A fast implementation of random forests for high dimensional data in c++ and r. Journal of Statistical Software, 77.1:1-17, 2015.




---

