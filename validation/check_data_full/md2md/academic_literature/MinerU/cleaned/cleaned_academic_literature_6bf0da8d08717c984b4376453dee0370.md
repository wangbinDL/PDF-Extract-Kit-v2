# On Regression in Extreme Regions  

Stephan Cl´ emen¸ con, Nathan Huet, Anne Sabourin  

# Abstract  

In the classic regression problem, the value of a real-valued random variable    $Y$   is to be predicted based on the observation of a random vector    $X$  . The statistical learning problem consists in building a predictive function  $\hat{f}$   based on independent copies of   $(X,Y)$   so that    $Y$   is approximated by   ${\hat{f}}(X)$  ) with minimum (squared) error. Motivated by various applications, special attention is paid here to the case of extreme ( i.e. very large) observations    $X$  . Because of their rarity, the contributions of such observations to the (empirical) error is negligible, and the predictive performance of empirical risk minimizers can be consequently very poor in extreme regions. In this paper, we develop a general framework for regression on extremes. Under appropriate regular variation assumptions regarding the pair   $(X,Y)$  , we show that an asymptotic notion of risk can be tailored to summarize appropriately predictive performance in extreme regions. It is also proved that minimization of an empirical and nonasymptotic version of this ’extreme risk’, based on a fraction of the largest observations solely, yields good generalization capacity. In addition, numerical results providing strong empirical evidence of the relevance of the approach proposed are displayed.  

# Contents  

1 Introduction 2  

2 A Regular Variation Framework for Regression 3  

2.1 Least Squares Minimization on Extremes - Algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . 4 2.2 Background on Multivariate Regular Variation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4 2.3 Regular Variation with respect to the First Component . . . . . . . . . . . . . . . . . . . . . . . . . 5  

3.1 Structural Analysis of Minimizers: Conditional, Asymptotic and Extreme Risks . . . . . . . . . . . . 8 3.2 Statistical Learning Guarantees . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9  

4.1 Simulated data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12 4.2 Real data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14  

# 5 Conclusion 15  

# A Multivariate Regular Variation w.r.t. the First Component 17  

B Proofs for Section 2 18 B.1 Proof of Proposition 1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18 B.2 Proofs and Additional Results regarding Example 1 . . . . . . . . . . . . . . . . . . . . . . . . . . . 20 B.3 Proofs regarding Example 2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21  

C Proofs for Section 3 25 C.1 Proof of Theorem 1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25 C.2 Proof of Theorem 2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26 C.3 Proof of Proposition 2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28  

# 1 Introduction  

Regression is a predictive problem of crucial importance in statistical learning, covering a wide variety of applica- tions. In the standard setup,   $(X,Y)$   is a pair of random variables defined on the same probability space   $\left(\Omega,\,\mathcal{A},\,\mathbb{P}\right)$  with distribution    $P$  , where the target    $Y$   is a square integrable real-valued random variable (the output) and the predictor (or covariable)    $X$   is a random vector with marginal distribution    taking its values in some measurable  $\rho$  space  modeling some input information hopefully useful to predict  . The predictive learning problem consists in    $\mathcal{X}$     $Y$  building, from a training dataset    compo d of  independent copies of  ,    $\mathcal{D}_{n}=\{(X_{1},Y_{1})$  , . . . ,  $\left(X_{n},Y_{n}\right)\}$     $n\geq1$   $(X,Y)$  a mapping    $f:\mathcal{X}\to\mathbb{R}$   in order to compute a ’good’ prediction    $f(X)$   for  Y  , with the quadratic risk  

$$
R_{P}(f)=\mathbb{E}\left[\left(Y-f(X)\right)^{2}\right]
$$  

as close as possible to at of    $f^{*}(X)=\mathbb{E}[Y\mid X]$  , which obviously minimizes (1) over the space    $L_{2}(\rho)$   of square integrable functions of  X :    $\begin{array}{r}{R_{P}^{*}:=\operatorname*{min}_{f\in L_{2}(\rho)}R_{P}(f)=R_{P}(f^{*})}\end{array}$  .  A natural strategy consists in solving the Empirical ∈ Risk Minimization problem (ERM in abbreviated form)   $\begin{array}{r}{\operatorname*{min}_{f\in\mathcal{F}}R_{\hat{P}_{n}}(f)}\end{array}$  ), where    $\mathcal{F}\subset L_{2}\left(\rho\right)$   is a closed and convex class of functions sufficiently rich to include a reasonable approximant of    $f^{*}$  and  $\hat{P}_{n}$   is an empirical version of    $P$  based on  ${\mathcal{D}}_{n}$  .  

The performance of predictive functions   $\hat{f}$   obtained this way, by  least-square regression , has been extensively investigated in the statistical learning literature [31, 40]. Under the assumption that the tails of the random pairs  are subgaussian and appropriate complexity conditions are satisfied by the class , confidence upper  $(f(X),Y)$     $\mathcal{F}$  bounds for the excess of quadratic risk    $R_{P}(\hat{f})-R_{P}^{*}=\mathbb{E}[(Y-\hat{f}(X))^{2}\mid\mathcal{D}_{n}]-R_{P}^{*}$   −  −   | D  −   have been established in [36] by means of concentration inequalities for empirical processes [6].  

Here we consider the problem of building prediction functions which would be reliable in a a ‘crisis scenario’ where the covariates vector takes unusually large values and thus belongs to regions where few or even no such large examples have been observed in the past. Notice incidentally that it could be thus viewed as a specific, never tackled yet,  few sho earning problem , see  e.g.  [56]. We place ourselves in a finite-dimensional setting,    $\mathcal{X}\subset\mathbb{R}^{d}$  . The distribution of  X  is not subgaussian and in particular its support is unbounded. Covariates are considered as extreme when their norm    $\|X\|$  exceeds some (asymptotically) large threshold    $t>0$  . The choice of the norm is unimportant in theory, and is typically determined by the application context.  

The threshold    $t$   depends on the observations, since ‘large’ should be naturally understood as large with respect to the vast majority of data observed. Hence, extreme observations are rare by nature and severely underrepresented in the training dataset with overwhelming probability. Consequently, the impact of prediction errors in extreme regions of the input space on the global regression error of   $\hat{f}$   is generally negligible. Indeed, the law of total probability yields  

$$
R_{P}(f)=\mathbb{P}\{\|X\|\ge t\}\mathbb{E}\left[\left(Y-f(X)\right)^{2}\mid\|X\|\ge t\right]+\mathbb{P}\{\|X\|<t\}\mathbb{E}\left[\left(Y-f(X)\right)^{2}\mid\|X\|<t\right].
$$  

The above decomposition involves a conditional error term relative to excesses of    $\|x\|$  above    $t$  , which we term Conditional quadratic risk  (or simply  Conditional risk )  

$$
R_{t}(f):=\mathbb{E}\left[\left(Y-f(X)\right)^{2}\mid\|X\|\geq t\right].
$$  

It is the purpose of the subsequent analysis to construct a predictive function  $\hat{f}$   that (approximately) minimizes  $R_{t}(f)$   for all    $t>t_{0}$  , with    $t_{0}$   being a large threshold. It is important to note that an approximate minimizer of    $R_{t}$  might not be suitable for minimizing    $R_{t^{\prime}}$   when    $t^{\prime}>t$  . To ensure robust extrapolation performance for our learned function, we focus on obtaining a prediction function,  $\hat{f}$  , that minimizes the  asymptotic conditional quadratic risk defined as  

$$
R_{\infty}(f):=\operatorname*{lim}_{t\to+\infty}R_{t}(f)=\operatorname*{lim}_{t\to+\infty}\mathbb{E}\left[(Y-f(X))^{2}\mid\|X\|\geq t\right].
$$  

It is immediate to see that any function that coincides with the regression function    $f^{*}(x)=\mathbb{E}\left[Y\mid X=x\right]$   on the region    $\{x\in{\mathcal{X}},\|x\|\geq t\}$   minimizes the risk functional    $R_{t}$  , for all    $t\,>\,0$  , and thus also    $R_{\infty}$  . In other words  $\begin{array}{r}{R_{\infty}^{*}:=\operatorname*{inf}_{f}R_{\infty}(f)=R_{\infty}(f^{*})}\end{array}$  ). However, even though    $f^{*}$  provides a straightforward theoretical solution,    $f^{*}$  is of ∞ ∞ course unknown.  

In view of Equation (2) it is evident that an estimate   $\hat{f}$   of    $f^{*}$  produced by an ERM strategy with good overall empirical performances, may not necessarily enjoy good performances when restricted to extreme regions. Put another way, there is no guarantee that the conditional risk    $R_{t}(\hat{f})$  ) (or    $R_{\infty}(\hat{f}),$  )) would be small. However, accurate prediction in extreme regions turns out to be crucial in certain practical (safety) applications, in environmental sciences, dietary risk analysis or finance/insurance for instance.  

To summarize, the  Regression Problem on Extremes  refers here to the the task of constructing a prediction function  $\hat{f}$   based on    ${\mathcal{D}}_{n}$   which approximately minimizes    $R_{\infty}$  . Notice that our choice of the squared error is motivated by simplicity and for illustrative purpose, extensions to other losses may be achieved at the price of additional (minor) technicalities.  

In order to develop a specific ERM framework relative to    $R_{\infty}$  with provable guarantees, regularity assumptions are required regarding the tail behavior of the pair   $(X,Y)$  , with respect to the first component.  Multivariate regular variation  hypotheses are very flexible in the sense that they correspond to a large nonparametric class of heavy- tailed distributions. These assumptions, or slightly weaker ones such as  Maximum domain of attraction  conditions are at the heart of Extreme Value Analysis (EVA) ( e.g. , the monographs [5, 18, 49]). They are frequently used in applications where the impact of extreme observations should be enhanced, or not neglected at the minimum.  

Statistical learning approaches in EVA have recently garnered significant interest, particularly in unsupervised learning contexts. Examples include dimensionality reduction through multiple subspace clustering in [28, 29, 13, 50, 43, 44], as well as Principal Component Analysis in [15, 20]. In addition, there has been notable exploration in clustering methods [35, 55], graphical models [24], and applications such as Anomaly Detection [12, 54], to name just a few. In the supervised setting, unlike the current study, the predominant focus in the literature revolves around predicting extreme values of the target variable    $Y$   [3] or tackling extreme quantile regression through methods such as gradient boosting [53] or random forests [26].  

The work which is most related to ours is that of [34] (see also [14]), where an ERM framework for the (easier) binary classification problem on extreme covariates is developed. Precisely, it is assumed therein that the two class distributions are multivariate regularly varying with the same tail index (see (5) in the background section 2.2), and risk functionals    $R_{t}$  ,   $R_{\infty}$  are defined similarly with the 0-1 loss. One of the primary objectives of this paper is to establish sufficient and reasonable conditions for extending the results of [34] to a broader context encompassing statistical regression with a continuous target and an appropriate real-valued loss. It must be noted that the con- tinuous nature of the target in the regression problem considered here requires fundamentally different assumptions and proof techniques compared with the binary classification setting. In particular one natural generalization of the assumptions made in the cited reference would be to assume regular variation of the conditional distributions  ${\mathcal{L}}(X|Y=y)$  , almost everywhere. This somewhat intricate generalization leads to measure theoretic complications and is difficult to verify in practice and also on theoretical examples. We propose to bypass this issue by requiring instead a joint form of regular variation of the pair   $(X,Y)$  , see our Assumption 2. We show that this condition is satisfied in various examples worked out in Section 2.3. Another major improvement of the present work upon [34], with implications for applications related to climate extremes, is to offer a novel perspective upon extreme value prediction within regularly varying random vectors, see Example 2.  

The paper is organized as follows. The algorithmic approach we propose for Regression on Extremes is detailed in Section 2, extending [34]’s framework in order to handle continuous targets. Key notions pertaining to multivariate extreme value theory (MEVT) are also briefly recalled for clarity’s sake and the probability framework we consider for regression in extreme regions is described at length therein. In Section 3, we show that a predictive rule using the angular information only  i.e.  of the form    $f(X)=h(X/\|X\|)$  , where    $h$   is a real-valued function defined the hypersphere    $\mathbb{S}\,=\,\{x\,\in\,\mathbb{R}^{d}\,:\,\,\|x\|\,=\,1\}$  ∥ ∥ }  reaches the best possible performances w.r.t. the asymptotic risk. Subsequently, we study the performance of a predictive rule based on a training sample    $\{(X_{1},Y_{1})$  , . . . ,    $\left(X_{n},Y_{n}\right)\}$  composed of    $n\geq1$   independent copies of the pair   $(X,Y)$   and learned by minimizing an empirical version of (3) based on a fraction    $k/n$   of the training dataset, those corresponding to the largest    $||X_{i}||$  ’s. Nonasymptotic bounds for the excess of asymptotic risk of such an empirical (preasymptotic) risk minimizer are established, demonstrating its near optimality. Beyond these theoretical guarantees, the performance of empirical risk minimization on extreme covariates is supported by various numerical experiments displayed in Section 4. Some concluding remarks are collected in Section 5. In order to enhance readability, certain technical details are postponed to the Appendix section.  

# 2 A Regular Variation Framework for Regression  

In this section, we propose a probabilistic framework in which Regression on Extremes may be addressed, together with a dedicated algorithmic approach, the latter being analyzed next in the subsequent sections. Here and through- out,   $(X,Y)$   is a pair of random variables defined on a probability space   $\left(\Omega,\,\mathcal{A},\,\mathbb{P}\right)$   with  tribution    $P$  , where    $Y$   is real-valued with marginal distribution    $G$   and    $X=(X^{(1)},~.\,.\,,~X^{(d)})$   takes its values in  R ,    $d\geq1$  . We sometimes denote by    ${\mathcal{L}}(Z)$   the distribution of a random variable  Z . Recall from the Introduction section that    $||\cdot||$  is any norm on    $\mathbb{R}^{d}$  . We denote by    $\mathbb{S}$   the unit sphere for this norm and by    $\mathbb{B}:=\{x\,\in\,\mathbb{R}^{d},\|x\|\,\leq\,1\}$   the unit ball. Let  $E\,=\,\mathbb{R}^{d}\,\setminus\,\{0_{\mathbb{R}^{d}}\}$   be the punctured Euclidean space. For any measurable subset  A  of  R  $\mathbb{R}^{d}$    w denot by    ${\mathcal{B}}(A)$   the trace Borel    $\sigma$  -field on    $A$  . The boundary and the closure of    $A$   are respectively denoted by  ∂A  and  A ¯ , and we set  for all . By    is meant the indicator function of any event  and the integer part of  $t A=\{t x:\ x\in A\}$     $t\in\mathbb{R}$   $\mathbb{1}\{\mathcal{E}\}$     $\mathcal{E}$  any  is denoted by .    $u\in\mathbb{R}$     $\lfloor u\rfloor$  

# 2.1 Least Squares Minimization on Extremes - Algorithm  

In order to help the reader understand the general workflow of the paper, we begin immediately by introducing the algorithm that we promote to solve the Regression Problem on Extremes stated in the Introduction, formulated as the minimization of the risk functional    $R_{\infty}$  defined in (3). The remainder of this work aims at developing a framework that fully justifies Algorithm 1 below.  

# Algorithm 1  Least Squares Minimization on Extremes  

INPUT:  Training dat  $\mathcal{D}_{n}=\{(X_{1},Y_{1})$  ,    $\left(X_{n},Y_{n}\right)\}$   with   $(X_{i},Y_{i})\in[0,+\infty)^{d}\times\mathbb{R}$  ,    $i=1$  ,   ,   $n$  ; class    $\mathcal{H}$   $\cdot\cdot\cdot$  of predictive functions  h  $h:\mathbb{S}\rightarrow\mathbb{R}$   :  → R ; number  k  $k\leq n$   ≤  of ’extreme’ observations among training data. Truncation:  Sort the tr ning data by decreasing order of magnitude of the input information    $\lvert|X_{(1)}\rvert|\geq\cdot\cdot\cdot\geq$   $||X_{(n)}||$   and form a set of  k  extreme training observations  

$$
\left\{\left(X_{(1)},Y_{(1)}\right),\;\ldots,\;\left(X_{(k)},Y_{(k)}\right)\right\}.
$$  

Empirical quadratic risk minimization:  based on the extreme training dataset, solve the optimization problem  

$$
\operatorname*{min}_{h\in\mathcal{H}}\frac{1}{k}\sum_{i=1}^{k}\left(Y_{(i)}-h\left(\theta\left(X_{(i)}\right)\right)\right)^{2},
$$  

where    $\theta(x)=x/\|x\|$  is the angular component of any point    $x\in\mathbb{R}^{d}\setminus\{0\}$  .  

OUTPUT:  Solution   $\hat{h}$     problem ( ive function    ${\widehat{f}}(x)=({\widehat{h}}\circ\theta)(x)$   ◦ ) to be used for predictions of    $Y$  based on new examples  such that .  X  ∥  $\|X\|\geq\|X_{(k)}\|$  ∥≥∥ ∥  

Notice that any algorithm for quadratic risk minimization can be used to solve (4), refer to  e.g. , [31]. The study of dedicated numerical techniques is beyond the scope of the present paper.  

A key feature of Algorithm 1 is that its training step involves the  angular  component of extremes solely. It returns a prediction function    $\hat{f}$   which only depends on the angular component    $\theta(X)$   of a new input    $X$  . This apparently arbitrary choice turns out to be fully justified under regular variation assumptions, which are introduced and discussed in the following subsections. To wit, the main theoretical advantage of considering angular prediction function is to ensure the convergence of the conditional risk    $R_{t}$  , as    $t\to+\infty$  . In practice, rescaling all extremes (in the training set and in new examples) onto a bounded set allows a drastic increase in the density of available training examples and a clear extrapolation method beyond the envelope of observed examples.  

After recalling some background on multivariate regular variation in subsection 2.2, we introduce a modified version of the standard framework ( regular variation with respect to the first component ) in subsection 2.3 which is suitable for the regression problem considered here, in the sense that Algorithm 1 turns out to enjoy probabilistic and statistical guarantees in this context. We thoroughly discuss the relevance of our assumptions by working out several sufficient conditions and examples. We state our main probabilistic results in subsection 3.1, establishing connections between different risks and their corresponding minimizers, thus bringing a first (probabilistic) justification regarding the angular nature of the prediction function in Algorithm 1. Statistical guarantees are deferred to subsection 3.2.  

# 2.2 Background on Multivariate Regular Variation  

The goal of heavy-tail analysis is to study phenomena that are not ruled by averaging effects but determined by extreme values. To investigate the behavior of a random vector    $X$   far from the center of its mass, an usual assumption is that    $X$  ’s distribution is  multivariate regularly varying  with tail index    $\alpha>0$  ,  i.e.  there exist a nonzero Borel measure    on    $E$  , finite on all Borel measurable subsets of    $E$   bounded away from zero and a  regularly varying  $\mu$  function    $b(t)$   with index    $\alpha$  ,  i.e.    $b(t x)/b(t)\to x^{\alpha}$    as    $t\to+\infty$  , such that  

$$
b(t)\mathbb{P}\left\{X\in t A\right\}\to\mu(A){\mathrm{~as~}}t\to+\infty,
$$  

for any Borel measurable set    $A\subset E$   bounded away from zero and such that    $\mu(\partial A)=0$  . The latter convergence  referred to as vague convergence in   $[-\infty,+\infty]^{d}\setminus\{0_{\mathbb{R}^{d}}\}$   (see [49], sec. 3.4), or equivalently as    ${\mathbb M}_{0}$  -convergence in  E (see [33, 38]). The  limit measure  is provably homogeneous of degree :  for all  and Borel    $\mu$     $-\alpha$     $\mu(t A)=t^{-\alpha}\mu(A)$     $t>0$  set    $A\subset E$   bounded away from the origin. One may refer to [49] for alternative formulations/characterizations of the regular variation property and its application to MEVT. It follows from the homogeneity property that the pushforward measure of    $\mu$   by the polar coordinates transformation    $x\in E\mapsto(\|x\|,\theta(x))$   is the tensor product given by:  

$$
\mu\left\{x\in E:\;\|x\|\geq r,\;\theta(x)\in B\right\}=r^{-\alpha}\Phi(A),
$$  

for all    $B\,\in\,{\mathcal{B}}(\mathbb{S})$   and    $r\geq1$  , where   $\Phi$   is a finite positive measure on    $\mathbb{S}$  , referred to as the  angular measure  of the limit measure    $\mu$  . The regular variation assumption (5) implies that the conditional distribution of   $(\|X\|/t,\theta(X))$  given    $\|X\|\geq t$   converges as    $t\to+\infty$  : for all    $r\geq1$   and    $B\in{\mathcal{B}}(\mathbb{S})$   with   $\Phi(\partial B)=0$  , we have  

$$
\mathbb{P}\Big\{t^{-1}\|X\|\geq r,\theta(X)\in B\mid\|X\|\geq t\Big\}\underset{t\to+\infty}{\longrightarrow}c r^{-\alpha}\Phi(B),
$$  

where    $c=\Phi(\mathbb{S})^{-1}=\mu(E\setminus\mathbb{B})^{-1}$    Hence, the radial and angular components of the random variable    $X$   are asymp- totically independent with standard Pareto distribution of parameter    $\alpha$   and normalized angular measure    $c\Phi$   as respective asymptotic marginal distributions. The angular measure   $\Phi$   describes exhaustively the dependence struc- ture of the components    $X^{(j)}$  ’s given that    $\|X\|$  is large,  i.e.  the directions    $\theta(X)$   in which extremes occur with largest probability.  

Heavy-tailed models have been the subject of much attention in the statistical machine-learning literature. Among many other works, the regular variation assumption is used in [46] for rare event probability estimation, in [10] or [1] in the context of stochastic bandit problems, in [27] for the statistical recovery of the dependence structure in the extremes, in [29] for dimensionality reduction in extreme regions and in [8] for predictive problems with heavy-tailed losses.  

# 2.3 Regular Variation with respect to the First Component  

We now describe rigorously the framework we consider for regression in extreme regions, which may be seen as a natural, ‘one-component’ extension of standard multivariate regular variation assumptions recalled in Section 2.2.  

For simplicity, we suppose that    $Y$   is bounded through this paper. This assumption can be naturally relaxed at the price of additional technicalities ( i.e.  tail decay hypotheses).  

Assumption 1  The random variable    $Y$   is bounded: there exists    $M\;\in\;(0,+\infty)$   such that with probability one,  $Y\in I=[-M,M]$  .  

The following hypothesis concerns the asymptotics, as    $t\to+\infty$  , of the conditional distribution of the pair   $(X,Y)$  given that . It may be viewed as one-component extension of (5).    $\|X\|>t$  

Assumption 2  There exists a non null Borel measure    $\mu$   on    $\mathbb{O}=E\times I$  , which is finite on sets bounded away from  $\mathbb{C}=\{0\}\times I$  , and a regularly varying function    $b(t)$   with index  α >  0  such that  

$$
\operatorname*{lim}_{t\to+\infty}b(t)\mathbb{P}\left\{t^{-1}X\in A,Y\in C\right\}=\mu(A\times C),
$$  

for all    $A\in{\mathcal{B}}(E)$   bounded away from zero and    $C\in{\mathcal{B}}(I)$   such that    $\mu(\partial(A\times C))=0$  .  

Assumption 2 could be understood as a multivariate extension of the  One-Component Regular Variation  framework developed in [32]. It should be noticed that Assumption 2 fits into the framework if Regular Variation in  M  $\mathbb{Q}$  developed in [38] as an extension of [33], where    $\mathbb{O}=E\times I=\left(\mathbb{R}^{d}\times I\right)\backslash\left(\{0\}\times I\right)$   and where the scalar multiplication is defined as    $\lambda(x,y)=(\lambda x,y)$  . More details regarding the connections between Assumption 2 and [38] are provided in the Supplementary Material, Section A.  

Remark 1 (Pre-Processing)  Because the goal of this paper is to explain main ideas to tackle the problem of regression on extremes, the input are assumed to be regularly varying with same marginal index while in practice, this condition may be satisfied only after some marginal standardization. This is a recurrent theme in multivariate extreme value theory. For binary-valued    $Y$  , in the classification setting, [14] consider a marginal standardization based on ranks, following [21, 22]. They prove an upper bound on the statistical error term induced by this trans- formation which is of the same order of magnitude as the error when marginal distributions are known, a simplified case considered in [34]. In our experiments with real data, this pre-processing step is not necessary. We leave this technical question outside the scope of this paper.  

In the sequel we refer to the limit measure    as the  joint limit measure  of   $(X,Y)$  . Under Assumption 2,    $X$  ’s  $\mu$  marginal distribution is regularly varying with  marginal limit measure  

$$
\mu_{X}(A)=\operatorname*{lim}_{t\to+\infty}b(t)\mathbb{P}\left\{X\in t A\right\}=\operatorname*{lim}_{t\to+\infty}b(t)\mathbb{P}\left\{X\in t A,Y\in I\right\}=\mu(A\times I),
$$  

with    $A\,\in\,\mathcal{B}(E)$   bounded away from z o and such that    $\mu(\partial(A\times I))\,=\,0$  . We also naturally introduce the  joint angular measure  of   $(X,Y)$   denoted by Φ, which is a finite measure on    $\mathbb{S}\times I$   given by  

$$
\Phi(B\times C)=\mu\{(x,y)\in E\times I:\|x\|\geq1,\theta(x)\in B,y\in C\}.
$$  

With this notation, under Assumption 2 it holds that  

$$
\frac{\mathbb{P}\{\theta(X)\in B,\,Y\in C,\,\|X\|\ge t r\}}{\mathbb{P}\{\|X\|\ge t\}}\underset{t\to+\infty}{\longrightarrow}\,c\,r^{-\alpha}\Phi(B\times C),
$$  

where    $c=\Phi(\mathbb{S}\times I)^{-1}=\mu((E\setminus\mathbb{B})\times I)^{-1}$  , for all    $C\in{\mathcal{B}}(I)$  ,    $B\in{\mathcal{B}}(\mathbb{S})$  , such that   $\Phi(\partial(B\times A))=0$   and    $r\geq1$  . The latter statement is proved in the Supplementary Material, Section A, Theorem A.1. To lighten the notation, we assume with oss of generality that    $b$   is chosen so that    $\mu((E\setminus\mathbb{B})\times I)=1$   and thus    $c=1$   and   $\Phi$   is a probability measure on  S  $\mathbb{S}\times I$   × . In particular, the joint limit measure    and the joint angular measure Φ are linked through the  $\mu$  relation  

$$
\mu(\{x\in E:\;\|x\|\geq r,\theta(x)\in B\}\times C)=r^{-\alpha}\Phi(B\times C)
$$  

for all    $C\in\mathcal{B}(I),B\in\mathcal{B}(\mathbb{S})$   and    $r>0$  . Observe that  

$$
\operatorname*{lim}_{t\to+\infty}{\frac{\mathbb{P}\left\{\theta(X)\in B,Y\in C,\|X\|\geq t\right\}}{\mathbb{P}\left\{\|X\|\geq t\right\}}}=\Phi(B\times C),
$$  

for all    $B\in{\mathcal{B}}(\mathbb{S}),C\in{\mathcal{B}}(I)$  ,  such that   $\Phi(\partial(B\times C))=0$  . In word  $\Phi$   is the asymptotic joint probability distribution of   given that  as . Notice also that ’s angular (probability) measure writes   $(\theta(X),Y)$     $\|X\|\geq t$     $t\to+\infty$   X  $\Phi_{\theta}(B)=$   $\Phi(B\times I)$  .  

Let    $P_{\infty}$  denote the limit conditional distribution on    $E\setminus\mathbb{B}\times I$   of the pair   $(X/t,Y)$   given that    $\|X\|\geq t$  ,  i.e.  

$$
P_{\infty}(\,A\times C\,)=\operatorname*{lim}_{t\to+\infty}\mathbb{P}\left\{X/t\in A\,,Y\in C\ \mid\|X\|\ge t\right\}
$$  

for all    $A\,\in\,\mathcal{B}(E\setminus\mathbb{B})$   and    $C\,\in\,\mathcal{B}(I)$   such that    $\mu(\partial(A\times C))\,=\,0$  ,  et   $(X_{\infty},Y_{\infty})$   denote a random pair with distribution    $P_{\infty}$  . It follows immediately from (8) and from our choice  c  = 1, that    $P_{\infty}$  indeed exists and is determined by   $(\Phi,\alpha)$  , namely  

$$
\begin{array}{r l r}{\lefteqn{P_{\infty}\{(x,y):\|x\|>r,\theta(x)\in B,y\in C\}=\operatorname*{lim}_{t\to+\infty}\mathbb{P}\left\{\|X\|/t\ge r,\theta(X)\in B,Y\in C\ |\ \|X\|\ge t\right\}}}\\ &{}&{=r^{-\alpha}\Phi(B\times C),}\end{array}
$$  

where    $B,C,r$   are as in Equation (8). In other words, if    $T$   denotes the pseudo-polar transformation with respect to the first component    $T(x,y)=(\lVert x\rVert,\theta(x),y)$   on    $E\setminus\mathbb{B}\times I$  , and if    $\nu_{\alpha}$   is the Pareto measure    $\nu_{\alpha}([x,\infty))=x^{-\alpha}$  , then the following tensor product decomposition holds true in polar coordinates,  

$$
{\cal P}_{\infty}\circ{\cal T}^{-1}=\nu_{\alpha}\otimes\Phi.
$$  

Observe that, under Assumptions 1 and 2, the random variable    $Y_{\infty}$  is almost-surely bounded in amplitude by  $M<+\infty$  .  

Equipped with these notations, it is natural to consider the squared error loss of a prediction function    $f$  , under the distribution    $P_{\infty}$  . We call this key quantity the  extreme quadratic risk , denoted by    $R_{P_{\infty}}$  , defined as  

$$
R_{P_{\infty}}(f):=\mathbb{E}\left[\left(Y_{\infty}-f(X_{\infty})\right)^{2}\right],
$$  

for    $f\,\in\,{\mathcal{F}}$   a class of real-valued bounded Borel-measurable functions defined on    $E\setminus\mathbb{B}$  . As will become clear in the subsequent analysis, although our objective    $R_{\infty}$  and the extreme risk    $R_{P_{\infty}}$  are two different functionals, they turn out to be connected through their minimizers under an additional technical assumption stated below. In the sequel we let    $f_{P_{\infty}}^{*}$  denote the minimizer pf    $R_{P_{\infty}}$  among all measurable functions. Standard arguments from statistical learning theory show immediately that    $f_{P_{\infty}}^{*}$  is defined (up to a negligible set) by a conditional expectation, ]. ∞  $f_{P_{\infty}}^{*}(X_{\infty})=\mathbb{E}[Y_{\infty}\mid X_{\infty}]$  | ∞ ∞ ∞  

Remark 2 (Heavy-tailed input vs heavy-tailed output)  Attention should be paid to the fact that the heavy- tail assumption is here on the distribution of the input/explanatory random variable    $X$  , in contrast to other works devoted to regression such as [8], [42] or [39] where it is the loss/response that is supposedly heavy-tailed. In the EVT literature, similarly, the vast majority of existing works in a regression context are concerned with extreme values of the target, in particular for extreme quantiles regression ([23, 16, 11, 17])  

Assumption 3  The extreme regression function    $f_{P_{\infty}}^{\ast}$  is continuous on    $\mathbb{R}^{d}\setminus\{0_{\mathbb{R}^{d}}\}$   and as    $t$   tends to infinity,  

$$
\mathbb{E}\left[|f^{*}(X)-f_{P_{\infty}}^{*}(X)|\;\big|\;\|X\|\geq t\right]\to0.
$$  

The next proposition highlights the weakness of Assumption 3, as long as Assumptions 1 and 2 are satisfied.  

Proposition 1 (Sufficient conditions for Assumption 3)  Let    $(X,Y)$   satisfy Assumptions 1 and 2. Then As- sumption 3 also holds if one of the three conditions   $(i)$  , (ii), (iii) below holds  

(i) The regression function    $f^{*}$  is continuous on    $\{x\in\mathbb{R}^{d}:\|x\|\geq1\}$   and as    $t\to+\infty$  ,  

$$
\operatorname*{sup}_{\|\boldsymbol{x}\|\ge t}|f^{*}(\boldsymbol{x})-f_{P_{\infty}}^{*}(\boldsymbol{x})|\ge0,
$$  

(ii) The conditional distributions of    $Y$   given    $X\,=\,x$   ( resp.    $Y_{\infty}$  given    $X_{\infty}\,=\,x_{\}$  ) admit densities    $p_{Y\mid x}(y)$   ( resp.  $p_{Y\mid x}^{\infty}(y))$  ) w.r.t. the Lebesgue measure on    $I$  , for all    $x\neq0$  . In addition for all    $y\in I$  , the mapping    $x\mapsto p_{Y\mid x}(y)$   | ( resp.  $x\;\mapsto\;p_{Y\mid x}(y))$   is continuous, and    $\begin{array}{r}{\operatorname*{sup}_{\|x\|\ge1,y\in I}\operatorname*{max}p_{Y|x}(y),p_{Y|x}^{\infty}(y)\;<\;+\infty}\end{array}$  . Finally the following  | uniform convergence holds true,  

$$
\operatorname*{sup}_{\|x\|\geq t,y\in I}|p_{Y|x}(y)-p_{Y|x}^{\infty}(y)|\underset{t\to+\infty}{\longrightarrow}0.
$$  

(iii) The random pair    $(X,Y)$   (resp.    $(X_{\infty},Y_{\infty})_{\lambda}$  ) has a continuous density    $p$   (resp.  q ) w.r.t. the Lebesgue measure, and the densities converge uniformly, in the sense that  

$$
\operatorname*{sup}_{(\omega,y)\in\mathbb{S}\times I}\big|\,b(t)t^{d}p(t\omega,y)-q(\omega,y)\,\big|\,\underset{t\to+\infty}{\longrightarrow}0.
$$  

where    $b(t)\,=\,\mathbb{P}\,\{\|X\|\geq t\}^{-1}$  . In addition,    $q$   is uniformly lower bounded on the unit sphere by a positive constant,  

$$
\operatorname*{inf}_{\omega\in\mathbb{S},y\in I}q(\omega,y)>0.
$$  

It should be noticed that Condition (iii) in Proposition 1 is a ‘one-component variant’ of standard assumptions regarding regular variations of densities ([19, 9]), further discussed in Example 2 below. We refer to Section B.1 in the Supplementary Material for a proof of Proposition 1.  

We now work out several examples of regression settings in which our Assumptions 1, 2 and 3 are satisfied.  

Example 1 (Noise model with heavy-tailed random design)  Suppose that    $X$   is a regularly varying random vector in    $\mathbb{R}^{d}$  , independent from a real-valued random variable    $\varepsilon$   modeling some noise and consider a target  

$$
Y=g(X,\varepsilon),
$$  

where    $g:\mathbb{R}^{d}\times\mathbb{R}\rightarrow\mathbb{R}$   is a bounded, continuous mapping. Assume also that there exists a function    $g_{\theta}:\mathbb{S}\times\mathbb{R}\to\mathbb{R}$  such that, for all    $z\in\mathbb R$  

$$
\operatorname*{sup}_{\|x\|\geq t}|g(x,z)-g_{\theta}(x/\|x\|,z)|\to0,
$$  

as    $t\to+\infty$  . Then, the random pair    $(X,Y)$   fulfills Assumptions 1, 2 and 3.  

The proof of the claim made in Example 1 is deferred to the Supplementary Material, Section B.2. Concrete examples arise within the broader context of this generic example, such as the additive noise model    $Y={\tilde{g}}(X)+\varepsilon$  and the multiplicative noise model    $Y=\varepsilon{\tilde{g}}(X)$  ). In both cases, Condition (14) holds true whenever  g  satisfies the similar condition  

$$
\operatorname*{sup}_{\|x\|\geq t}|\tilde{g}(x)-\tilde{g}_{\theta}(\theta(x))|\to0,
$$  

for some angular function   ${\tilde{g}}_{\theta}$  , with minor additional regularity assumptions. We work out the details of these two sub-examples in Section B.2, Propositions B.2 and B.3, from the Supplementary Material.  

Example 2 (Predicting a missing component in a regularly varying random vector))  In this example, we show that our assumptions are met when considering a random vector  $\tilde{X}$   with a regularly varying  density , where the target    $Y$   is one missing component from the vector, or more precisely a normalized version of that miss- ing component. The normalization allows to satisfy our boundedness constraint Assumption 1. We believe this example could be particularly useful in applications, for imputation of missing data with heavy tails.  

Let  $\tilde{X}\in\mathbb{R}^{d+1}$   ∈   have continuou  density   , and    $b(t)=\mathbb{P}\left\{\|\tilde{X}\|\ge t\right\}^{-1}$   	 , wh  $||\cdot||$  is the    $L^{p}$   norm on    $\mathbb{R}^{d+1}$   for  $p$  some    $p\in[1,+\infty)$   Assume that  b  is regularly varying with index    $\alpha$   for some  α >  0 , and that there exists a positive function    $q$   on  R  $\mathbb{R}^{d+1}$  +1   such that for all    $\tilde{x}\neq0_{\mathbb{R}^{d+1}}$   0 ,  

$$
t^{d+1}b(t)p(t\tilde{x})-q(\tilde{x})\underset{t\to+\infty}{\longrightarrow}0.
$$  

Assume in addition that the convergence is uniform on the sphere,  

$$
\operatorname*{sup}_{\omega\in\mathbb{S}_{d+1}}\left\vert t^{d+1}b(t)p(t\omega)-q(\omega)\right\vert\underset{t\to+\infty}{\longrightarrow}0,
$$  

where    $\mathbb{S}_{d+1}$   denotes the unit sphere of    $\mathbb{R}^{d+1}$  . This assumption is used in [19, 9]. It is shown in these references that  (15)  and (16) imply that  $\tilde{X}$   is regularly varying with index  ˜    $\alpha$  . More precisely with    $\begin{array}{r}{\mu(A)\,=\,\int_{A}q(\tilde{x})\,\mathrm{d}\tilde{x}}\end{array}$  R  for any measurable set    $A\subset E$  ave    $b(t)\mathbb{P}\left\{\tilde{X}/t\in\mathbf{\beta}\cdot\right\}\rightarrow\mu(\mathbf{\beta})$    ∈· 	 →  ·  in the sense of vague convergence. Necessarily    $q$   is homogeneous of order  −  $-\alpha-d-1$   −  − 1 . Also the continuity of    $p$   implies that of    $q$  . Assume finally that  

$$
\operatorname*{min}_{\omega\in\mathbb{S}_{d+1}}q(\omega)>0.
$$  

Another useful feature of this setting is that, if  (15)  and (16) hold, then also  

$$
\operatorname*{sup}_{\|\tilde{x}\|\geq1}|p(t\tilde{x})t^{d+1}b(t)-q(\tilde{x})|\underset{t\to+\infty}{\longrightarrow}0.
$$  

Let    $X\,=\,(\tilde{X}_{1},\dots,\tilde{X}_{d})$   and    $Y\,=\,\tilde{X}_{d+1}/\|\tilde{X}\|$  ∥ ∥ . The norm    $\|x\|$  also denotes the    $L^{p}$    norm in    $\mathbb{R}^{d}$    when it is clear from the context that    $\boldsymbol{x}\in\mathbb{R}^{d}$  . Then  

(i) The pair    $(X,Y)$   satisfies Assumptions 1,   $\mathcal{Q}$   and 3;  

(ii) The limit pair    $(X_{\infty},Y_{\infty})$   for    $(X,Y)$   defined in  (9)  has distribution  

$$
\mathcal{L}\Big(\big(\tilde{X}_{\infty,1:d},\frac{\tilde{X}_{\infty,d+1}}{\|\tilde{X}_{\infty}\|}\big)\,\big|\,\|\tilde{X}_{\infty,1:d}\|\geq1\Big),
$$  

where  $\tilde{X}_{\infty,1:d}$   denotes the    $d$  -dimensional vector    $(\tilde{X}_{\infty,1},\allowbreak\cdot\cdot,\tilde{X}_{\infty,d})$  . ∞  

It is important to observe that predicting    $Y$   allows to predict  $\tilde{X}_{d+1}$  , as  

$$
Y=\frac{\tilde{X}_{d+1}}{\|\tilde{X}\|_{p}}\quad\Longleftrightarrow\quad\tilde{X}_{d+1}=\frac{Y\|X\|_{p}}{(1-\vert Y\vert^{p})^{1/p}}.
$$  

In our experiments with real data we consider this prediction example on a financial dataset.  

As will be shown in the forthcoming sections, Assumptions 1, 2 and 3 provide sufficient regularity and stability conditions allowing to justify the  angular  ERM approach taken in Algorithm 1.  

# 3 Regression on Extremes - Main Results  

# 3.1 Structural Analysis of Minimizers: Conditional, Asymptotic and Extreme Risks  

The main purposes of this subsection are to show that under the assumptions previously listed,   $(i)$   the extreme quadratic risk    $R_{P_{\infty}}$  is minimized by angular prediction functions, that is functions depending on the input through the angle only ;   $(i i)$   Although    $R_{\infty}$  and    $R_{P_{\infty}}$  are different risk functionals, they are connected through their respective minimizers and minimum values.  

The first objective   $(i)$   above is easily tackled. Indeed, the discussion below Equation (9) shows that, under Assumption 2, letting   $\Theta_{\infty}=\theta(X_{\infty})$   denote the angular component of  $X_{\infty}$  , the random pair   $(\Theta_{\infty},Y_{\infty})$   is independent from the norm , and in particular and are independent. Hence, the only useful piece of information    $\|X_{\infty}\|$     $Y_{\infty}$     $\|X_{\infty}\|$  carried by    $X_{\infty}$  to predict    $Y_{\infty}$  is its angular component   $\Theta_{\infty}$  . As a consequence the Bayes regression function satisfies ] almost-surely. As a consequence we may write  for some  $f_{P_{\infty}}^{*}(X_{\infty})=\mathbb{E}\left[Y_{\infty}\mid X_{\infty}\right]=\mathbb{E}\left[Y_{\infty}\mid\Theta_{\infty}\right]$  | |    $f_{P_{\infty}}^{*}\,=\,h_{\infty}\circ\theta$  ◦ ∞ ∞ ∞ ∞ ∞ function    $h_{\infty}$  defined on the sphere    $\mathbb{S}$  . Finally, Assumption 3 ensures that    $h_{\infty}$  may be chosen as a continuous function. We summarize the discussion:  

Lemma 1  Under Assumptions   $\mathit{1}$  ,   $\mathcal{Q}$  , 3, the extreme risk    $R_{P_{\infty}}$  has a minimizer (among all measurable functions) which may be written as )  where  is a bounded, continuous function.    $f_{P_{\infty}}^{*}(x)=h_{\infty}\circ\theta(x)$  ◦    $h_{\infty}:\mathbb{S}\rightarrow I$  ∞  

The next result brings answers regarding the objective   $(i i)$   outlined above, by establishing a key connection between the (seemingly) different problems of minimizing    $R_{\infty}$  on the one hand, and minimizing    $R_{P_{\infty}}$  on the other hand. Recall from Section 2.3 that the extreme risk    $R_{P_{\infty}}(f)=\mathbb{E}\left[(f(X_{\infty})-Y_{\infty})^{2}\right]$    and the asymptotic risk R  $_{\circ}(f)=\operatorname*{lim}\operatorname*{sup}_{t\to+\infty}\mathbb{E}\left[(f(X)-Y)^{2}\mid\|X\|\geq t\right.$      are two different functionals, so that the regression function ∞ ∞    $f_{P_{\infty}}^{*}$  is only defined as a minimizer of the extreme risk    $R_{P_{\infty}}$  and not the asymptotic risk    $R_{\infty}$  . In the sequel we denote by    $R_{P_{\infty}}^{*}$  the minimum value of the extreme risk,  i.e.    $R_{P_{\infty}}^{*}:=\operatorname*{inf}_{f}$   measurable  $R_{P_{\infty}}(f)=R_{P_{\infty}}(f_{P_{\infty}}^{*})$  ).  

Theorem 1  Under Assumptions 1 and 2, we have  

(i) For any angular function of the kind    $\begin{array}{r}{f(x)\,=\,h\circ\theta(x)}\end{array}$  , where    $h$   is a continuous function defined on    $\mathbb{S}$  , the conditional risk converges to the extreme risk, i.e.  

$$
R_{t}(f)\xrightarrow[t\to\infty]{}R_{P_{\infty}}(f).
$$  

Thus for such prediction functions,    $\begin{array}{r}{R_{\infty}(f)=\operatorname*{lim}_{t\rightarrow+\infty}R_{t}(f)=R_{P_{\infty}}(f).}\end{array}$  . If in addition Assumption   $\mathcal{B}$   is satisfied, then the following assertions hold true.

 (ii)   $A s\ t\to+\infty$  : the minimum value of    $R_{t}$   converges to that of    $R_{P_{\infty}}$  , i.e.    $R_{t\_t\rightarrow+\infty}^{*}\,R_{P_{\infty}}^{*}$  .

 (iii) The minimum values of    $R_{\infty}$  and    $R_{P_{\infty}}$  coincide, i.e.    $R_{\infty}^{*}=R_{P_{\infty}}^{*}

$  (iv) The regression function    $f_{P_{\infty}}^{*}$  minimizes the asymptotic conditional quadratic risk:  

$$
R_{\infty}^{*}=R_{\infty}(f_{P_{\infty}}^{*}).
$$  

The proof is deferred to Section C.1 in the Supplementary Material. Observe that Theorem 1 does not assert that  $R_{t}(f)$   converges to    $R_{P_{\infty}}(f)$   for all    $f$  , but the convergence holds true for angular predictors    $f=h\!\circ\!\theta$   (Property  (i)  in the statement). Property  (iv)  discloses that the solution    $f_{P_{\infty}}^{*}$  of the extreme risk minimization problem, which is of angular type, is also a minimizer of the asymptotic conditional quadratic risk    $R_{\infty}$  (and that the minima coincide). Because  is of angular type, we thus obtain, under Assumptions  , 2 and 3,    $f_{P_{\infty}}^{*}=h_{\infty}\circ\theta$  ◦  $1$  

$$
\operatorname*{inf}_{f\mathrm{measurable}}R_{\infty}(f)=\operatorname*{inf}_{h\mathrm{~measurable}}R_{\infty}(h\circ\theta).
$$  

In other words, the search for minimizers of    $R_{\infty}$  may indeed be restricted to angular prediction functions, which provides a first heuristic justification for Algorithm 1. However in order to provide rigorous guarantees regarding minimizers of the empirical criterion (4) from Algorithm 1, further assumptions regarding the class  of angular    $\mathcal{H}$  predictors are needed. In particular these additional assumptions ensure uniformity of the convergence result    $(i)$  from Theorem 1. This is the focus of the next section.  

# 3.2 Statistical Learning Guarantees  

This section provides a nonasymptotic analysis of the approach proposed for regression on extremes. An upper confidence bound for the excess of -risk of a solution of (4) is established, when the class  over which empirical    $R_{\infty}$     $\mathcal{H}$  minimization is performed is of controlled complexity, see Assumption 4 below.  

The rationale behind the approach proposed in Algorithm 1 is to find an angular predictive function that nearly minimizes the asymptotic conditional quadratic risk    $R_{\infty}$  (3). Our ERM strategy thus consists in solving an empirical version of the nonasymptotic optimization problem  

$$
\operatorname*{min}_{h\in\mathcal{H}}R_{t}\left(h\circ\theta\right).
$$  

Recall that a heuristic justification for considering angular classifiers is given by Identity (18), which is itself a consequence of Theorem 1. The radial threshold    $t$   is chosen as a relatively high quantile of the empirical distribution of the radii . In particular, let  denote the   quantile of the norm , where  is large enough    $\|X_{i}\|$     $t_{n,k}$   $1-k/n$     $\|X\|$     $k\ll n$  so that a statistical analysis remains realistic, but small enough so that the the distribution of   $(X,Y)$   given that  $\|X\|>t_{n,k}$   is close to the limit    $P_{\infty}$  , see (9). Then an empirical version of    $t_{n,k}$   is   $\hat{t}_{n,k}=\|X_{(k)}\|$  ∥ , the    $k^{t h}$    largest order statistic of the norm already introduced in Algorithm 1. In practice the number  k  of retained extreme values statistics in a recurrent issue in Extreme Value Analysis, for which no definite theoretical answer exists, but which is a standard bias/variance compromise. In our experiments, following standard practice we choose    $k$   by inspection of stability regions in Hill plots. In addition, in a regression setting we consider feature importance summaries relative to the radial variable, see Section 4 for details.  

Summarizing, the objective minimized in Algorithm 1 may be viewed as an empirical version of the conditional risk    $R_{t_{n,k}}$   for a predictive mapping of the form    $h\circ\theta$  . In the sequel we denote by  $\hat{R}_{k}$   this empirical objective,  

$$
{\hat{R}}_{k}(f)={\frac{1}{k}}\sum_{i=1}^{k}{\Big(}Y_{(i)}-f(X_{(i)}){\Big)}^{2}.
$$  

We point out that the statistic above is not an average of independent random variables, as it involves extreme order statistics of the norm. Thus investigating its concentration properties is far from straightforward. The minimum is taken over a class    $\mathcal{H}$   of continuous bounded functions on    $\mathbb{S}$   of controlled complexity but hopefully rich e ough to contain a reasonable approximant of introduced in Lemma 1. The following assumption regarding  will    $h_{\infty}$   H turn out to be sufficient to obtain a control of the deviations of the empirical risk. In order to avoid measurability issues regarding supremum deviations over the class , it is assumed throughout that  is   wise mea e    $\mathcal{H}$     $\mathcal{H}$  (see [52], Example  hat there e ble family , such that for all  and all ,    $\mathcal{H}_{0}\subset\mathcal{H}$   ω  $\omega\in\mathbb S$   ∈  h  ∈H there is a sequence (  s h that ). This mild condition is satisfied in practical cases,  $(h_{i})_{i\geq1}\in\mathcal{H}_{0}$   ∈H  $h_{i}(\omega)\rightarrow h(\omega)$   → ≥ in particular by parametric classes ,  i.e.  classes indexed by a finite dimensional parameter , which depend  H  $\beta\in\mathbb{R}^{p}$   ∈ continously on the parameter,  i.e.  such that    $\|h_{\beta}-h_{\beta_{n}}\|_{\infty,\mathbb{S}}\rightarrow0$   as    $\beta_{n}\rightarrow\beta$  .  

Assumption 4  The pointwise measurable class    $\mathcal{H}$   is a family of continuous, real-valued  nctions defined on    $\mathbb{S}$  ; of  VC  dimension    $V_{\mathcal{H}}<+\infty$  , and uniformly bounded by the same constant as the target  Y  (see Assumption 1),  $\forall h\in\mathcal{H},\forall\omega\in\mathbb{S}$  ,    $|h(\omega)|\leq M$  .  

Under the complexity hypothesis above, the following result provides an upper confidence bound for the maximal deviations between the conditional quadratic risk    $R_{t_{n,k}}$   and its empirical version  $\hat{R}_{k}$  , uniformly over the class    $\mathcal{H}$  .  

Notice that a similar result is obtained in [2] (Lemma A.3) in the more complex setting of cross validation. For the sake of completeness, we provide a detailed proof in Section C.2 of the Supplementary Material.  

orem 2  Suppose that Assumptions 1 and   $\mathit{4}$   are satisfied. Let    $\delta\in(0,1)$  . We have with probability larger than  $1-\delta$  1 :  

$$
\operatorname*{sup}_{c\in\mathcal{H}}\left|\hat{R}_{k}(h\circ\theta)-R_{t_{n,k}}(h\circ\theta)\right|\leq\frac{8M^{2}\,\sqrt{2\log(3/\delta)}+C\,\sqrt{V_{\mathcal{H}}}}{\sqrt{k}}+\frac{16M^{2}\log(3/\delta)/3+4M^{2}V_{\mathcal{H}}}{k},
$$  

where    $C$   is a universal constant.  

Notice that Theorem 2 controls only the statistical deviations between the sub-asymptotic risk    $R_{t_{n,k}}$   and its empirical version   $\hat{R}_{k}$  . A control of the bias  rm    $R_{t_{n,k}}\mathrm{~-~}R_{\infty}$  is given next, under appropriate complexity assumptions controlling the complexity of class . In particular Assumption 4 can be traded against a total boundedness  H assumption (Case 1. in Proposition 2 below) which is further discussed below (Remark 3). Regarding the second set of assumption (Case 2.), notice that for    $t\geq1$  , the conditional distribution   $\Phi_{\theta,t}={\mathcal{L}}(\theta(X)\,|\,\|X\|\geq t)$   is absolutely continuous w.r.t.   $\Phi_{\theta,1}\,=\,{\mathcal{L}}(\theta(X)\,|\,\|X\|\,\geq\,1)$  . Indeed for any measurable set    $A\subset\mathbb{S}$  , if    $\mathbb{P}\left\{\Theta\in A\,|\,\|X\|\ge1\right\}\,=\,0$  then also for any    $t\geq1$  ,    $\mathbb{P}\left\{\Theta\in A\,|\,\|X\|\ge t\right\}\,=\,0$  . Denote by    $\phi_{\theta,t}$   the probability density of the former angular distribution with respect to the latter.  

Proposition 2  Suppose that Assumptions 1 and 2 are satisfied. Let  be a class of real-valued, continuous functions    $\mathcal{H}$  on  S . Assume that one out of the two following conditions is satisfied.  

1.    $\mathcal{H}$   is totally bounded in the space    $({\mathcal{C}}(\mathbb{S}),\|\cdot\|_{\infty})$   of continuous functions on    $\mathbb{S}$   endowed with the supremum norm, or  

2.  fulfills Assumption 4 and in addition, suppose that the conditional densities  introduced above the state-  H    $\phi_{t}$  ment satisfy  

$$
\operatorname*{sup}_{t\geq1,\,\omega\in\mathbb{S}}\phi_{\theta,t}(\omega)=D,
$$  

for some    $0<D<\infty$  .  

Then, as  t  tends to infinity, we have  

$$
\operatorname*{sup}_{h\in\mathcal{H}}|R_{t}(h\circ\theta)-R_{\infty}(h\circ\theta)|\to0.
$$  

The proof of Proposition 2 is deferred to Section C.3 of the Supplementary Material.  

Remark 3 (Totally bounded family of regression functions)  Relying on a topological assumption on a set ression functions such as total boundedness (i.e.    $\mathcal{H}$   may be covered by finitely many balls of radius    $\varepsilon$  , for any  $\varepsilon\,>\,0$  ) is rather uncommon in statistical learning. However it turns out that this condition encompasses several standard  s. Namely, if  is a parametric family indexed by a bounded parameter set, i.e.    $\mathcal{H}$     $\mathcal{H}=\{h_{\beta},\beta\in B\}$  for some  B  $B\,\subset\,\mathbb{R}^{p}$   ⊂   of finite diameter, and if    $h_{\beta}$     Lipschitz-continuous with respect to    $\beta$  , i.e. for some  C >  0 ,  $\|h_{\beta}-h_{\gamma}\|_{\infty}\leq C\|\beta-\gamma\|$   $\beta,\gamma\in B$  , then  H  satisfies Condition 1  an example let  $p=d$   and fo  $\omega\in\mathbb S$  , let  $h_{\beta}(\omega)=\langle\beta,\omega\rangle$   ⟨ ,  a bounded p eter set  $B=\{\beta\in\mathbb{R}^{d}:\|\beta\|_{q}\leq\lambda\}$  {  ∈    ∥ ∥  ≤ }  for some fixed

  $\lambda>0$   0 , where  ∥· ∥ is the  L   norm on  R  $\mathbb{R}^{d}$  ,  q  $q\geq1$   ≥ 1 . The case  q  = 2  ( resp.  q  = 1 ) corresponds to a constrained Ridge

 ( resp.  Lasso) regression.  

Remark 4 (Bounded angular densities)  The second condition in Proposition   $\mathcal{Q}$   implies that the angular mea- sure    $\Phi_{\theta,t}$   for large    $t$   may not concentrate around sets that are negligible with respect to the ‘bulk’ angular mea- sure    $\Phi_{\theta,1}$  . This excludes situations where the limit angular measure    $\Phi_{\theta}$   concentrates on lower dimensional sub- cones of    $\mathbb{R}^{d}$  , whereas    $\Phi_{\theta,1}$   does not necessarily do so. This concentration phenomenon as    $t\,\rightarrow\,+\infty$  is precisely the framework considered in recent works on unsupervised dimension reduction for extremes where the goal is to uncover sparsity patterns in the limit angular measure    $\Phi_{\theta}$   which may not be representative of the bulk behav- ior ([28, 29, 43, 43, 13, 20, 15]). How to relax Condition 2. in order to encompass such frameworks even though the family  does not satisfy Condition 1. is left to future research.    $\mathcal{H}$  

The corollary below summarizes the main results of Sections 3.1 and 3.2 in the form of an upper confidence bound for the excess of    $R_{\infty}$  -risk for any solution  $\hat{f}_{k}$   of the problem  

$$
\operatorname*{min}_{h\in\mathcal{H}}\hat{R}_{k}(h\circ\theta).
$$  

Corollary 1 (Summary)  Let  $\hat{f}_{k}=\hat{h}_{k}{\circ}\theta$  ◦  be the prediction function issued by Algorithm 1. Let Assumptions 1, 2, 3 and 4 be satisfied. Recall    $h_{\infty}$  from Lemma 1 and that, from Theorem   $\mathit{1}$  ,    $R_{\infty}(h_{\infty}{\circ}\theta)={\mathrm{inf}}_{h}$   measurable    $R_{\infty}(h{\circ}\theta)=R_{\infty}^{*}$  . For any    $\delta>0$  , with probability at least    $1-\delta$  , the excess    $R_{\infty}$  -risk of    $\hat{f}_{k}$   satisfies ∞  

$$
\begin{array}{r}{R_{\infty}\big(\hat{f}_{k}\big)-R_{\infty}^{*}\leq D_{k}+B_{1}\big(t_{n,k}\big)+B_{2}\big(\mathcal{H}\big),}\end{array}
$$  

where    $D_{k},B_{1},B_{2}$   are respectively a deviation term and two bias terms,  

$$
\begin{array}{r}{\left\{\begin{array}{l l}{D_{k}=\big(16M^{2}\,\sqrt{2\log(3/\delta)}+2C\,\sqrt{V_{\mathcal{H}}}\big)/\,\sqrt{k}+\big(f\cdot\cdot\cdot}\\ {\qquad\big(32M^{2}\log(3/\delta)/3+8M^{2}V_{\mathcal{H}}\big)/k}&{(d e v i a t i o n s)}\\ {B_{1}(t)=2\operatorname*{sup}_{h\in\mathcal{H}}|R_{\infty}(h\circ\theta)-R_{t}(h\circ\theta)|}&{(t h r e s h o l d~b i a s)}\\ {B_{2}(\mathcal{H})=\operatorname*{inf}_{h\in\mathcal{H}}R_{\infty}(h\circ\theta)\ -\ R_{\infty}(h_{\infty}\circ\theta)}&{(c l a s s~b i a s).}\end{array}\right.}\end{array}
$$  

The first bias term    $B_{1}(t_{n,k})$   in the above bound converges to zero as    $n\to+\infty$  ,    $k\to+\infty$  ,    $k/n\rightarrow0$   whenever the conditions of Proposition 2 are met.  

proof. t the infimum of the    $R_{\infty}$  -risk over the class    $\mathcal{H}$  s reached,  i.e.    $\exists h_{\mathcal{H}}\,\in\,\mathcal{H}\,:$   $R_{\infty}(h_{\mathcal{H}}\circ\theta)=\operatorname*{inf}\{R_{\infty}(h\circ\theta),h\in\mathcal{H}\}$   ◦ {  ◦  ∈H}  (if this is not the case, consider an  ε -minimizer  h  $h_{\varepsilon}$   for arbitrarily small  ε , and ∞ H ∞ proceed). Thus  

$$
\begin{array}{r l}&{R_{\infty}(\widehat{f}_{k})-R_{\infty}^{*}\le R_{\infty}(\widehat{h}_{k}\circ\theta)-R_{t_{n,k}}(\widehat{h}_{k}\circ\theta)+R_{t_{n,k}}(\widehat{h}_{k}\circ\theta)-\hat{R}_{k}(\widehat{h}_{k}\circ\theta)}\\ &{\phantom{R_{\infty}(\widehat{h}_{k}\circ\theta)-R_{t_{n,k}}(\widehat{h}_{k}\circ\theta)+R_{k}(h_{\mathcal{H}}\circ\theta)-R_{t_{n,k}}(h_{\mathcal{H}}\circ\theta)}}\\ &{\phantom{R_{\infty}(\widehat{h}_{k}\circ\theta)-R_{\infty}(h_{\mathcal{H}}\circ\theta)+R_{\infty}(h_{\mathcal{H}}\circ\theta)-\underset{h\mathrm{~measurable}}{\operatorname*{inf}}R_{\infty}(h\circ\theta)}}\\ &{\phantom{R_{\infty}(\widehat{h}_{k}\circ\theta)-R_{\infty}(\widehat{h}_{k}\circ\theta)-\underset{f\mathrm{~measurable}}{\operatorname*{inf}}R_{\infty}(f).}}\end{array}
$$  

Because   $\hat{h}_{k}\circ\theta$   ◦  minimizes  $\hat{R}_{k}$   and considering identity (18) (which holds because of Assumptions 1, 2, 3), the above decomposition simplifies into  

$$
R_{\infty}(\widehat{f}_{k})-R_{\infty}^{*}\leq2\operatorname*{sup}_{h\in\mathcal{H}}|R_{\infty}-R_{t_{n,k}}|(h\circ\theta)+2\operatorname*{sup}_{h\in\mathcal{H}}|R_{t_{n,k}}-\widehat{R}_{k}|(h\circ\theta)+R_{\infty}(h_{\mathcal{H}}\circ\theta)-\operatorname*{inf}_{h\in\mathrm{~meas}}(h_{\mathcal{H}}\circ\theta)+R_{\infty}(h_{\mathcal{H}}\circ\theta).
$$  

The result follows by plugging in the deviation bound from Theorem 2.  

As it is generally the case in statistics of extremes, two types of bias terms are involved in the upper bound (20) of Corollary 1. The first bias term    $B_{1}(t)$   results from the substitution of the conditional quadratic risk    $R_{t_{n,k}}$   for its asymptotic limit    $R_{\infty}$  . While the weak additional assumptions of Proposition 2 ensure that this bais term vanishes fas    $k/n\to0$  , a quantification of its decay rate would require second-order conditions,  e.g.  by extending the second order regular variation setting of [48] to our context of joint regular variation.  

The second bias term is a model bias, induced by restricting the family of all measurable functions on    $\mathbb{S}$   to the class  of controlled combinatorial complexity. It should be noted that under the conditions of the statement,    $\mathcal{H}$  Identity (18) ensures that restricting to angular predictors does not induce any additional bias term compared with considering a standard class for predictors taking the full covariate (including the radius) as input.  

Remark 5 (Rate of convergence)  To establish the concentration bound stated in Theorem 2, we employ general concentration results that are not ideally tailored for a regression context. A more detailed investigation might yield a bound on the stochastic error term of order    $O(\log(k)/k)$  , as suggested by standard concentration results (refer to [31], sec. 11). This refined study is left to future work.  

Remark 6 (Extensions)  This article presents a rigorous formulation and investigation of the regression problem involving an output variable confronted to a heavy-tailed input variable, a so far unexplored topic in academic research. Subsequently, we anticipate that the straightforward adaptation of the proposed methodology to incorporate regularized risk formulations or diverse cost functions holds the potential for practical utility and improvements. These extensions lie outside the scope of this paper and are deferred to further works.  

Remark 7 (Alternative to ERM)  In the case where the output/response variable    $Y$   is heavy-tailed (or possibly contaminated by a heavy-tailed noise), robust alternatives to the ERM approach exist and are preferable ([39]). Extension of these robust alternatives to the present context of heavy-tailed input is beyond the scope of this paper but will be the subject of further research.  

# 4 Numerical Experiments  

We now investigate the performance of the approach previously described and theoretically analyzed for regression on extremes from an empirical perspective on several simulated and real datasets. The code used to run our experiments is available at  https://bitbucket.org/nathanhuet/extreme regression . The MSE in extreme regions of angular regression functions output by specific implementations of Algorithm 1 are compared to those of the classic regression functions, learned in a standard fashion. On this occasion we propose a simple graphical diagnostic procedure allowing to check visually whether the data meet our assumptions, in particular Assumption 2 which is central in our work. More precisely we inspect the relative importance of the radial variable    $\|X\|$  for predicting    $Y$   above increasing radial thresholds. We consider in Section 4.1 simulated data in the additive and multiplicative models which are particular instances of Example 1. In Section 4.2 we consider a real-life financial dataset which has already been studied in an EVA context [44].  

# 4.1 Simulated data  

Experimental Setting. As a first go, we focus on predictive performance of Algorithm 1 in terms of Mean Squared Error (MSE), with simulated data respectively from an additive noise model and from a multiplicative noise model with heavy-tailed design,    $Y=\tilde{g}_{0}(X)+\varepsilon_{0}$  , and    $Y=\varepsilon_{1}\tilde{g}_{1}(X)$  ), where    $|=|\cdot|_{2},\,\tilde{g}_{0}(x)=\beta^{T}\theta(x)(1+1/||x||)$  ∥ ∥ ), and   $\begin{array}{r}{\tilde{g}_{1}(x)=\cos(1/\|x\|)\sum_{i=1}^{d/2}(\theta(x)_{2i-1}-1/\|x\|^{2})\mathrm{sin}((\theta(x)_{2i}-1/\|x\|^{2})\pi)}\end{array}$  ), for    $\boldsymbol{x}\in\mathbb{R}^{d}$  .  

Both models satisfy our assumptions (see Proposition B.2 in the Supplementary Material). In the additive model ( resp.  in the multiplicative model) the design    $X$   is generated according to a multivariate extreme value distribution from the logistic family [51] with dependence parameter    $\xi=1$  , which means that extreme observations occur very close to the axes ( resp .  $\xi\,=\,0.7$  , meaning that the angular component of extreme observations is relatively spread-out in the positive orthant of the unit sphere). The input 1-d marginals are standard Pareto with shape parameter    $\alpha\:=\:1$   ( resp.  $\alpha~=~3$  ) and the noise    $\varepsilon_{0}$   is defined as a truncated Gaussian variable on Table 1: Average MSE (and standard deviation) for regression functions trained using all observations, extreme observations and angles of extreme observations, over 10 independent replications of the dataset generated in the additive and the multiplicative noise models.  

<td><table  border="1"><thead><tr><td><b>METHODS/MODELS</b></td><td><b>TRAIN ON X</b></td><td><b>TRAIN ON XIX LARGE</b></td><td><b>TRAIN ON O IIX LARGE</b></td></tr></thead><tbody><tr><td>ADD.: OLS</td><td>23±29</td><td>3±6</td><td>0.003±0.001</td></tr><tr><td>SVR</td><td>0.13±0.01</td><td>0.05±0.02</td><td>0.003±0.001</td></tr><tr><td>RF</td><td>0.012±0.004</td><td>0.007±0.002</td><td>0.004±0.001</td></tr><tr><td>MULT.: OLS</td><td>0.006±0.001</td><td>0.003±0.001</td><td>0.001±0.001</td></tr><tr><td>RF SVR</td><td>0.0041±0.0002</td><td>0.0038±0.0004</td><td>0.0034±0.0003</td></tr><tr><td>RF</td><td>0.0020±0.0001</td><td>0.0013±0.0001</td><td>0.0004±0.0001</td></tr></tbody></table></td>  

$[-1,1]$   with zero mean and standard deviation    $\sigma_{0}=0.1$  ,  i.e.    $\varepsilon_{0}$   admits the probability density    $f_{\varepsilon_{0}}(x)=\mathbb{1}\{|x|\leq

$   $\begin{array}{r}{{1}\}\exp(-x^{2}/(2\sigma_{0}^{2}))/\int_{-1}^{1}\exp(-z^{2}/(2\sigma_{0}^{2}))d z}\end{array}$  . For the multiplicative model,    $\varepsilon_{1}$    is again a truncated Gaussian variable − on   $[0,2]$   with mean  µ  = 1 and standard deviation    $\sigma_{1}=0.1$  ,  i.e.    $\varepsilon_{1}$   has density    $f_{\varepsilon_{1}}(x)=\mathbb{1}\{0\le x\le2\}\exp(-(x-$   2  $\begin{array}{r}{\mu)^{2}/(2\sigma_{1}^{2}))/\int_{0}^{2}\exp(-(z-\mu)^{2}/(2\sigma_{1}^{2}))d z}\end{array}$  .  

The simulated data are of dimension    $d=7$   ( resp.    $d=14$  ). For both models, the size of the training dataset is  $n_{t r a i n}=10\,000$  , and the number of extreme observations retained for training Algorithm 1 is set to    $k_{t r a i n}=1000$   $(=n_{t r a i n}/10$  ). The size of the test dataset is    $n_{t e s t}=100\,000$   and the    $k_{t e s t}=10\,000$   (  $=n_{t e s t}/10$  ) largest instances are used to evaluate predictive performance on extreme covariates. We consider three different regression algorithms implemented in the  scikit-learn  library [47] with the default parameters, namely Ordinary Least Squares (OLS), Support Vector Regression (SVR), and Random Forest (RF). Predictive functions are learned using respectively  $(i)$   the full training dataset,   $(i i)$   a reduced dataset composed of the    $k_{t r a i n}$   largest observations    $X_{(1)},\dots.X_{(k_{t r a i n})}$  , and   $(i i i)$   an angular dataset   $\Theta_{(1)},.\,.\,.\,\Theta_{\left(k_{t r a i n}\right)}$   consisting of the angles of the    $k_{t r a i n}$   largest observations. These three options correspond respectively to   $(i)$   the default strategy (using the full dataset),   $(i i)$   a ‘reasonable’ naive strategy (training on extreme covariates for the purpose of predicting from extreme covariates),   $(i i i)$   the strategy that we promote in this paper, corresponding to Algorithm 1. We evaluate the performance of the outputs using the MSE computed on the test set. Table 1 shows the average MSE’s when repeating this experiment across    $E=10$  independent replications of the dataset. For the additive model the regression parameter    $\beta$   is randomly chosen for each replication, namely each entry of    $\beta$   is drawn uniformly at random over the interval   $[0,1]$  .  

With both models, the approach we promote for regression on extremes clearly outperforms its competitors, no matter the algorithm ( i.e.  the model bias) considered. This paper being the first to consider regression on extremes (see Remark 7 for a description of regression problems of different nature with heavy-tailed data), no other alternative approach is documented in the literature.  

Besides prediction performance, we propose to assess the validity of our main modeling assumption (Assump- tion 2) by inspecting the  variable importance  ( a.k.a. feature importance , see  e.g.  [30] and the references therein) of the radial variable compared with the angular variables  , for the purpose of predicting the target .    $\|X\|$   $\Theta_{j},j\leq d$     $Y$  Indeed, under Assumption 2, the variables  and are asymptotically independent conditional on  as    $Y$     $\|X\|$     $\|X\|>t$  , so that the variable importance of , when restricting the training set to regions above increasingly  $t\to+\infty$     $\|X\|$  large radial thresholds, should in principle vanish.  

We consider here two widely used measures of feature importance, Gini importance (or Mean Decrease of Impu- rity, [45, 7]) and Permutation feature importance [4] in the context of Random Forest prediction, as implemented in the  scikit-learn  library. Gini importance measures a mean decrease of impurity in a forest of trees, between parent nodes involving a split on the considered variables, and their child nodes. Permutation importance compares the prediction performance of the original input dataset with the same dataset where the values of the considered variable have been randomly shuffled. Both scores are normalized so that the sum of all importance scores across variables equals 1. A large score indicates a high predictive value of the variable.  

The aim of this second experiment is to illustrate the decrease of the radial feature importance for reduced datasets involving increasingly (relatively) large inputs. To cancel out the perturbation effect of reduced sample sizes, we fix a training size    $k_{i m p}=1000$   and we simulate increasingly large datasets of size  

$$
n_{i m p}\in\{k_{i m p},2k_{i m p},.\,.\,.\,,10k_{i m p}\}
$$  

in the additive and multiplicative models described above. Then for    $j\in\{1,\dots,10\}$   the    $k_{i m p}$   largest observations in terms of    $\|X\|$  among    $n_{i m p}=j k_{i m p}$   are retained, a random forest is fitted with input variables   $\left(\lVert X\rVert,\Theta_{1},.\,.\,,\Theta_{d}\right)$  , and the Gini and Permutation scores are computed. Figure 1 shows the average scores obtained over 10 independent experiments, together with interquantile ranges, as a function of the full sample size    $n_{i m p}$  . In both models, the decrease of both scores is obvious. In particular in terms of Gini measure, the relative importance of the radius decreases from 38% to   $1\%$   for the additive model and from   $6\%$   to    $<1\%$   for the multiplicative model.  

  
Figure 1: Average permutation and Gini importance measures of the radial variable using the RF algorithm in the additive noise model (left) and the multiplicative noise model (right) over 10 replications, as a function of the total sample size    $n_{i m p}$  for fixed extreme training size    $k_{i m p}$  . Solid black line: average Gini importance. Solid grey line: average Permutation importance. Dashed lines: empirical 0.8-interquantile ranges.  

# 4.2 Real data  

Encouraged by this first agreement between theoretical and numerical results, experiments on real data are con- ducted. We place ourselves in the setting of Example 2 where the target is one particular variable in a multivariate regularly varying random vector. We consider a financial dataset, namely  49 Industry Portfolios [Daily]  from Ken- neth R. French - Data Library ( https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library. html ). A study of extremal clustering properties within this dataset has already been carried out by [44]. This dataset comprises daily returns of 49 industry portfolios, within the time span from January 5th, 1970 to October 31st, 2023. Rows containing any NA values are removed, resulting in a dataset of dimension    $d\,=\,49$   and size . Figu plays lot of the radial variable (w.r.t. ), with a rather wide stability region,  $n=13577$     $\|\cdot\|_{2})$  roughly between  k  = 500 and  k  = 2000, which suggests that regular variation is indeed present, with regular varia- tion index    $\alpha\approx3.2$  . We consider separately the first three variables as output (target) variables, namely  Agric  ( i.e. ”Agriculture”),  Food  ( i.e.  ”Food Products”), and  Soda  ( i.e.  ”Candy and Soda”). Each choice of a target variable yields a regression problem consisting of predicting the target based on a covariate vector of dimension    $d=10$   com- posed of the 10 variables   $(\tilde{X}_{1},\hdots,\tilde{X}_{d})$  ) which are the most correlated with the target  $\tilde{X}_{d+1}$  . Following the workflow of Examp 2, as an intermediate step, Algorithm 1 is used to predict    $Y=X_{d+1}/\|\tilde{X}\|$  ∥ where  $\tilde{X}=(\tilde{X}_{1},.\,.\,.\,,\tilde{X}_{d+1})$  ). The output   $\hat{Y}$   of Algorithm 1 is then plugged in the formula  $\tilde{X}_{d+1}=Y\|X\|/\sqrt{1-Y^{2}}$   ∥ ∥ √  −   where    $X=\left(X_{1},\ldots,X_{d}\right)$  , which yields an estimate  $\hat{X}_{d+1}$   for the target variable. The dataset is randomly split into a test set of size    $n_{t e s t}=4073$  (  $30\%$   of the data), and a train set of size    $n_{t r a i n}\,=\,9504\,=\,n\,-\,n_{t e s t}$  . As suggested by the Hill plot (Figure 2), the number    $k_{t r a i n}$   of extreme observations used at the training step is set to    $k_{t r a i n}=\lfloor n_{t r a i n}/5\rfloor=1900$  . On the other hand, at the testing step, to evaluate the extrapolation performance of our method, we fix    $k_{t e s t}$   to a smaller fraction of the test set,    $k_{t e s t}=\lfloor n_{t e s t}/10\rfloor=407$  . In this setting, paralleling our experiments with simulated data, we compare the performance of regression functions learned using the full training dataset, the truncated version composed of the the    $k_{t r a i n}$   largest observations and the angles of the truncated version. For the sake of realism, we report the MSE regarding prediction of the original target variable be of greater interest in applications than the error in the transformed variable (  $\tilde{X}_{d+1}$  ,  i.e.  $(Y-{\hat{Y}})^{2}$     −  $(\tilde{X}_{d+1}-\hat{X}_{d+1})^{2}$  2 . Notice that our theory  − , which would provides guarantees for the latter, not the former. The results gathered in Table 2 are the average MSE’s obtained when repeating 10 times the procedure described above with random splits of the dataset into a train and a test set. These results provide evidence that conditionally on the other (covariate) variables being large, our method ensures, in most cases, better reconstruction of the target variable than the default strategy (first column) and the intermediate strategy (second column). For predicting the  Soda  variable however, the default strategy with OLS obtains the best scores. This suggests that convergence of the conditional distribution of excesses towards its limit as in (5) is somewhat slower for the subvector   $(\tilde{X}_{1},\dots,\tilde{X}_{d+1})$  ) where   $\tilde{X}_{d+1}$   is  Soda  and  $\tilde{X}_{1},\dots,\tilde{X}_{d}$  ˜  are the 10 selected variables based on their correlation with  Soda . This intuition is confirmed by the graphs of variable  

  
Figure 2: Hill plot for the radial variable of the 49 Industry Portfolio Daily dataset: estimation of the extreme value index    $\gamma=1/\alpha$   with the Hill estimator using the    $k$   largest order statistics of    $\|X\|$  , as a function of    $k$  .  

importance displayed in Figure 3, again paralleling the ones of Figure 1 and fully described in Section 4.1. In Figure 3, for simplicity, the importance scores are computed in a prediction task where the covariate vector includes all the available variables, except from the target (48 of them). Also the target variable for the RF algorithm is the rescaled variable    $Y\,=\,\tilde{X}_{d+1}/\|\tilde{X}\|$  ∥ ∥ . Whereas the radial importances decreases monotonically when the target variable in  Agric  and  Food , the third panel dedicated to the target variable  Soda  displays a local maximum in radial importance around    $n=11\,000$  . This value corresponds to a ratio    $k/n\approx1/12$   which is near the ratio   $1/10$  considered for the testing step in our experimental results reported in Table 2. This may explain our comparatively poor results for this particular variable. However for all three target variables, overall, both Gini and Permutation importance score decrease significantly, as the ratio    $k/n$   decreases. In particular for Gini importance, the relative radial importances are approximately   $2\%\approx1/48$   when    $n=k$  , which is to be expected when all variables have equal importance. On the other hand when  n  = 10 , all three Gini importances are less than   $1\%$  .  

# 5 Conclusion  

We have provided a sound ERM approach to the generic problem of statistical regression on extreme values. The asymptotic framework we have developed crucially relies on the (novel) notion of  joint regular variation  w.r.t. some multivariate component. When the distribution of the couple   $(X,Y)$   is regularly varying w.r.t.    $X$  ’s component, the problem can be stated and analyzed in a rigorous manner. We have described the optimal solution and proved that it can be nearly recovered with nonasymptotic guarantees by implementing a variant of the ERM principle, based on the angular information carried by a fraction of the largest observations only. We have also carried out numerical experiments to support the approach promoted, highlighting the necessity of using a dedicated methodology to perform regression on extreme samples with guarantees.  

<td><table  border="1"><thead><tr><td><b>METHODS/MODELS</b></td><td><b>TRAIN ON X</b></td><td><b>TRAIN ON X</b></td><td><b>TRAIN ON X LIXII LARGE</b></td><td><b>TRAIN ON IIXI</b></td><td><b>TRAIN ON IIXI</b></td></tr></thead><tbody><tr><td rowspan="3">AGRIC: OLS</td><td>LARGE</td><td>3.30±0.47</td><td>3.26±0.47</td><td></td><td>3.25±0.44</td></tr><tr><td>SVR</td><td>4.76±0.56</td><td>3.98±0.51</td><td></td><td>3.74±0.50</td></tr><tr><td>RF</td><td>3.47±0.47</td><td>3.48±0.47</td><td></td><td>3.28±0.52</td></tr><tr><td rowspan="3">FoOD: OLS</td><td>LARGE</td><td>0.69±0.087</td><td>0.678±0.082</td><td></td><td>0.680±0.085</td></tr><tr><td>SVR</td><td>1.8±0.4</td><td>1.3±0.4</td><td></td><td>0.87±0.08</td></tr><tr><td>RF</td><td>0.70±0.13</td><td>0.72±0.12</td><td></td><td>0.63±0.08</td></tr><tr><td rowspan="3">SODA: OLS</td><td>LARGE</td><td>2.35±0.21</td><td>2.37±0.21</td><td></td><td>2.42±0.21</td></tr><tr><td>SVR</td><td>4.0±0.5</td><td>3.1±0.5</td><td></td><td>2.8±0.2</td></tr><tr><td>RF</td><td>2.46±0.28</td><td>2.46±0.25</td><td></td><td>2.34±0.18</td></tr></tbody></table></td>  

  
Soda  

# SUPPLEMENTARY MATERIAL  

The Supplementary Material is structured as follows. In Section A, the Regular Variation with respect to the first component introduced in Assumption 2 is rephrased into equivalent conditions. Section B ( resp.  Section C) gathers the proofs of the results from Section 2 ( resp.  Section 3.2).  

# A Multivariate Regular Variation w.r.t. the First Component  

This section makes explicit the connection between Assumption 2 and the regular variation framework on a metric space developed in [38]. We also provide alternative formulations of Assumption 2. Following whenever possible the notations of [38], let    $\mathcal{Z}=\mathbb{R}^{d}\times I$   where we recall    $I=[-M,M]$   (in [38]  e ambient space    $\mathcal{Z}$   is denoted by    $\mathbb{S}$   which interferes with our notation for the unit sphere). The ambient space  is endowed with the Euclidean product  Z metric,  

$$
d((x_{1},y_{1}),(x_{2},y_{2}))=\,\sqrt{\|x_{1}-x_{2}\|^{2}+(y_{1}-y_{2})^{2}},
$$  

at   $(\mathcal{Z},d)$   is a complete separable metric space. Define a scalar ‘multiplication’ on    $\mathcal{Z}$   a  $\lambda.(x,y)\,=\,(\lambda x,y)$  ,  $\lambda>0$   0, which is continuous and satisfies the associativity property    $\lambda_{1}.(\lambda_{2}.z)=(\lambda_{1}\lambda_{2}).z$  , and 1  $1.z=z$   = . This scalar multi cation induces a scaling operation on sets,    $\lambda A=\{\lambda.z,z\in A\}$   for    $A\subset\mathcal{Z}$  . Consider the set    $\mathbb{C}=\{0_{\mathbb{R}^{d}}\}{\times}I\subset\mathcal{Z}$  . Then  C  is a closed set which is preserved by the above scaling operation,  i.e.  it is a closed cone. For    $z=(x,y)$  we have    $d(z,\mathbb{C})=\|x\|$  , whence    $d(x,\mathbb{C})<d(\lambda x,\mathbb{C})$   for    $\lambda>1$  . Thus Assumptions A1, A2, A3 in [38], Section 3, a satisfied. Let    $\mathbb{O}=\mathcal{Z}\setminus\mathbb{C}$   and introduce    $\mathbb{C}^{r}=\{z\in\mathbb{O}:d(z,\mathbb{C})>r\},r\geq0$  . In [38], the class of Borel measures on  O whose restriction to    $\mathcal{Z}\setminus\mathbb{C}^{r}$    is finite for any  r >  0 is denoted by    $\mathbb{M}_{\mathbb{O}}$  . Then convergence of a sequence of measures  $\mu_{n}\in{\mathbb{M}}_{\mathbb{O}}$   towards    $\mu\in{\mathbb{M}}_{\mathbb{O}}$     defined as convergence of functional valuations    $\mu_{n}(f)\to\mu(f)$   for    $f\in\mathcal{C}_{\mathbb{O}}$   the class of continuous functions on  Z  which vanish on a neighborhood of  C ,  i.e.  whose support is a subset of  C   for some  $r>0$  . A measure    $\nu\in\mathbb{M}_{\mathbb{O}}$   is called  r ularly varying  with limit measure  $\mu\in{\mathbb{M}}_{\mathbb{O}}$   and scaling  uence    $b_{n}\in\mathbb{R}$  , if  $b_{n}$  n  is increasing, regularly varying in  R  and if the sequence of measures  b  $b_{n}\ensuremath{\boldsymbol\nu}(n\ensuremath{\boldsymbol{\cdot}})$   ·  ) converges in  $\mathbb{M}_{\mathbb{O}}$   towards    $\mu$   (see Definitions 3.1, 3.2 in [38]). From the Portmanteau Theorem 2.1 in [38] and the series of equivalences in Theorem

 3.1 of the same reference, our Assumption 2 is equivalent to assuming that the distribution    $P$   of the random pair

  $(X,Y)$   is regularly varying in    $\mathbb{M}_{\mathbb{O}}$   with scaling sequence    $b_{n}$   and limit measure    $\mu$  , with the notations of Section 2.3.  

Theorem A.1  Let    $\mathbb{O},\mathbb{C}$   be d ed as above the statement, let    $\mu\,\in\,\mathbb{M}_{\mathbb{O}}$   be a nonnull measure and  $b(t)$   be a regularly varying function on  R  $\mathbb{R}^{+}$  +   with index    $\alpha\:>\:0$  . Let    $(X,Y)\,\sim\,P$   be a random pair valued in  R  $\mathbb{R}^{d}\times I$    × . The following assertions are equivalent.  

(i) The random pair    $(X,Y)$   satisfies Assumption 2 from the main paper with limit measure    $\mu$   and normalizing function    $b$  .  

(ii) For any bound  and conti  function    $h:\mathbb{O}\to\mathbb{R}$   that vanishes in a neighborhood of    $\mathbb{C}$  , i.e. whose support is included in  C   for some  r >  0 ,  

$$
\operatorname*{lim}_{t\to+\infty}b(t)\mathbb{E}\left[h(t^{-1}X,Y)\right]=\int_{\mathbb{O}}h\,\mathrm{d}\mu.
$$  

(iii) There exists a finite measure    $\Phi$   on    $\mathbb{S}\times I$   such that  

$$
\frac{\mathbb{P}\{\theta(X)\in B,Y\in A,\|X\|\ge t r\}}{\mathbb{P}\{\|X\|\ge t\}}\underset{t\to+\infty}{\longrightarrow}c r^{-\alpha}\Phi(B\times A)
$$  

for all    $r>0$   and    $A\in{\mathcal{B}}(I)$  ,    $B\in{\mathcal{B}}(\mathbb{S})$   such that    $\Phi(\partial(B\times A))=0$  , with    $\boldsymbol{c}=\Phi(\mathbb{S}\times\boldsymbol{I})^{-1}$  .  

proof.  $(i)\Leftrightarrow(i i)$  .  Condition  (ii)  in the statement is precisely Definition 3.2 of regular variation in    $\mathbb{M}_{\mathbb{O}}$   of [38], regarding the measure    $P$   restricted to    $\mathbb{O}$  . The equivalence with our Assumption 2 is a direct application of the Portmanteau theorem 2.1 in [38].  

$(i i i)\,\Leftrightarrow\,(i i)$  . We generalize the argument of [38], Example 3.4 and we verify that we fit into the context of Example 3.5 of the same reference. The argument in Example 3.5 (see also Example 3.4) in [38] relies on a continuous mapping argument (Theorem 2.3 in the same reference). Introduce the ‘polar coordinate transform’  $T(x,y)=(\lVert x\rVert,\theta(x),y)$  , for   $(x,y)\in\mathbb{O}$  , where we recall    $\theta(x)=x/\|x\|$  . Then    $T$   is homeomorphism from    $\mathbb{O}$   onto  $\mathbb{O}^{\prime}=\left(\mathbb{R}_{+}\setminus\left\{0\right\}\right)\times\mathbb{S}\times I=\mathcal{Z}^{\prime}\setminus\mathbb{C}^{\prime}$    with    $\mathcal{Z}^{\prime}=\mathbb{R}_{+}\times\mathbb{S}\times I$  ,    $\mathbb{C}^{\prime}=\{0\}\times\mathbb{S}\times I$  . The space  Z   is endowed with a continuous scalar multiplication    $\lambda.(r,\omega,y)=(\lambda r,\omega,y)$   for    $\lambda\geq0$  , which is compatible with the mapping    $T$   in the sense that  $\lambda.T(z)=T(\lambda.z)$  . The scalar multiplication on  Z ′   satis  same associativity and onotonicity properties as the one on    $\mathcal{Z}$  . The mapping    $T$   has the property that if  A  $A^{\prime}\subset\mathbb{O}^{\prime}$    ⊂ ′   is bounded away from  C   then also    $T^{-1}(A^{\prime})\subset\mathbb{O}$   is bounded away from    $\mathbb{C}$  . The conditions of Example 3.5 in [38] are thus satisfied, so that regular variation of the joint distribution    $P$   (restricted to    $\mathbb{O}$  ) in    $\mathbb{M}_{\mathbb{O}}$   is equivalent to regular variation of the image measure  $T_{\star}P$   (restricted to    $\mathbb{O}^{\prime}$  ), with limit measure    $\mu^{\prime}=T_{\star}\mu$  , and with the same scaling function    $b(t)$  . In other words Condition    $(i i)$   is equivalent to the fact that for any measurable sets  such that , where ,    $B\subset\mathbb{S},C\in I$     $\mu(\partial(\mathcal{C}_{B}\times C))=0$     $\mathcal{C}_{B}=\{t\omega,t\geq1,\omega\in B\}$  we have  

$$
\begin{array}{r l}&{b(t)\mathbb{P}\left\{\|X\|>t r,\theta(X)\in B,Y\in C\right\}\underset{t\rightarrow+\infty}{\longrightarrow}\mu\{(x,y):\|x\|\ge r,\theta(x)\in B,y\in C\}}\\ &{\qquad\qquad\qquad\qquad=\mu(r.\{(x,y):\|x\|\ge1,\theta(x)\in B,y\in C\})}\\ &{\qquad\qquad\qquad\qquad=r^{-\alpha}\mu\{(x,y):\|x\|\ge1,\theta(x)\in B,y\in C\},}\end{array}
$$  

where the last identity follows from the homogeneity of    (Theorem 3.1 in [38]). Define the angular measure   $\Phi$   on  $\mu$   $\mathbb{S}\times I$   as in (7) from the main paper,   $\Phi(B\times C)=\mu\{(x,y)\in\mathbb{O}:\|x\|\geq1,\theta(x)\in B,y\in C\}$  . Then   $\Phi$   is a finite measure and the latter display writes equivalently  

$$
b(t)\mathbb{P}\left\{\|X\|>t r,\theta(X)\in B,Y\in C\right\}\underset{t\to+\infty}{\longrightarrow}r^{-\alpha}\Phi(B\times C),
$$  

for all measurable sets    $B\subset\mathbb{S},C\in I$   such that   $\Phi(\partial(B\times C))=0$  . If (21) holds then also, taking    $B=\mathbb{S},C=I,r=1$  we have  

$$
b(t)\mathbb{P}\left\{\|X\|>t\right\}\underset{t\rightarrow+\infty}{\longrightarrow}\Phi(\mathbb{S}\times I),
$$  

and taking the ratio of (21) with the latter displays yields Condition  (iii)  of the statement. Conversely if  (iii)  holds, then letting    $b(t)=\Phi(\mathbb{S}\times I)/\mathbb{P}\left\{\|X\|>t\right\}$  , we obtain (21), which is equivalent to Condition  (ii) .  

# B Proofs for Section 2  

This section gathers the proofs of Proposition 1 and of the claims in Examples 1 and 2, as well as the proof of Theorem 1.  

# B.1 Proof of Proposition 1  

We show that if Assumptions 1 and 2 both hold true, then each condition (i), (ii), or (iii) of the statement imply Assumption 3. In fact we show that (iii)  $\Rightarrow$  (ii) (i) Assumption 3.  

Condition   $\mathbf{\Gamma}(\mathbf{i})\ \Rightarrow$  Assumption 3.  The continuity of    $f_{P_{\infty}}^{*}$  follows from the continuity of    $f^{*}$  and the uniform convergence (10). Also, the convergence in Assumption 3 is a direct consequence of convergence (10). Condition (ii)  $\Rightarrow$  Condition (i).  For    $\boldsymbol{x}\in\mathbb{R}^{d}$    such that    $\|x\|\geq t\geq1$  , we have  

$$
\begin{array}{r l}{\lefteqn{|f^{*}(x)-f_{P_{\infty}}^{*}(x)|=\Big|\int_{y\in I}y p_{Y|x}(y)d y-\int_{y\in I}y p_{Y|x}^{\infty}(y)d y\Big|}}\\ &{\le M^{2}\operatorname*{sup}_{\|x\|\ge t,y\in I}|p_{Y|x}(y)-p_{Y|x}^{\infty}(y)|.}\end{array}
$$  

Thus, uniform convergence in (10) follows from (11). The continuity of    $f^{*}$  is ensured by an application of the dominated convergence theorem to the parametric integral    $\begin{array}{r}{f^{*}(x)=\int_{I}y p_{Y\mid x}(y){\,\mathrm{{d}}}y}\end{array}$  R , using the fact that for all    $y\in I$  ,  |  $x\mapsto p_{Y\mid x}(y)$   is continuous and that   $\begin{array}{r}{\operatorname*{sup}_{\|x\|\geq1,y\in I}p_{Y|x}(y)<+\infty}\end{array}$  .  

Condition (iii) Condition (ii).  We first show that uniform convergence (11) holds true. Notice first that    $\Rightarrow$  the density    $q$   of    $\mu$   is necessarily homogeneous in its first component,    $q(t x,y)=t^{-\alpha-d}q(x,y)$   for    $x\neq0$   (This follows from the homogeneity of where    $A\subset\mathbb{R}^{d}\setminus\{0\}$   and      $B\subset I$   $\mu$   and a change o ). Thus for  x  $\boldsymbol{x}\in\mathbb{R}^{d}$   ∈ ble in the first component when integrating over a region   with    $\|x\|\geq1$   and    $y\in I$  , we have    $t A\times B$  

$$
p_{Y|x}(y)=\frac{p(x,y)}{p_{X}(x)}\quad\mathrm{and}\quad p_{Y|x}^{\infty}(y)=\frac{q(x,y)}{q_{X}(x)}=\frac{q(x/\|x\|,y)}{q_{X}(x/\|x\|)},
$$  

where we denote by    $p_{X}$   (resp.    $q_{X}$  ) the marginal density of    $X$   (resp.    $X_{\infty}$  ) given by  $\begin{array}{r}{p_{X}(x)\,=\,\int_{I}p(x,y)d y}\end{array}$  R  (resp.  $\begin{array}{r}{q_{X}(x)=\int_{I}q(x,y)d y)}\end{array}$  R ). Then, for    $x\in\mathbb{R}^{d}\setminus\{0\},y\in I$  , introducing the function    $h(t)=t^{d}b(t)$  , the left-hand side in Equation (11) writes as  

$$
\begin{array}{r l}{\left|\frac{p(x,y)}{p_{X}(x)}-\frac{q(x/\|x\|,y)}{q_{X}(x/\|x\|)}\right|=\frac{\left|h(\|x\|)p(x,y)\right|}{h(\|x\|)p_{X}(x)}-\frac{q(x/\|x\|,y)}{q_{X}(x/\|x\|)}\right|}&{}\\ &{\leq\underbrace{h(\|x\|)p(x,y)\left|\frac{1}{h(\|x\|)p_{X}(x)}-\frac{1}{q_{X}(x/\|x\|)}\right|}_{A(x,y)}+\dots}\\ &{\ \ \underbrace{\left|h(\|x\|)p(x,y)-q(x/\|x\|,y)\right|}_{q_{X}(x/\|x\|)}.}\end{array}
$$  

Regarding the numerator of the term    $B(x,y)$   above, notice that for  $\|x\|\geq t$  ,  

$$
\begin{array}{r l}&{|h(\|x\|)p(x,y)-q(x/\|x\|,y)|=|h(t(\|x\|/t))p(t(\|x\|/t)(x/\|x\|),y)-q(x/\|x\|,y)|}\\ &{\qquad\qquad\qquad\qquad\leq\underset{s\geq t,(\omega,y)\in\mathbb S\times I}{\operatorname*{sup}}|h(s)p(s\omega,y)-q(\omega,y)|\to0,}\end{array}
$$  

as    $t$   tends to infinity, by uniform convergence (12). This, together with the lower bound (13) on   , implies that as  $q$   $t\to\infty$  ,  

$$
\operatorname*{sup}_{\|x\|>t,y\in I}B(x,y)\to0.
$$  

Turning to the term    $A(x,y)$   in (22), observe first that  

$$
A(x,y)=h(\|x\|)p(x,y)\bigg\vert\frac{h(\|x\|)p_{X}(x)-q_{X}(x/\|x\|)}{h(\|x\|)p_{X}(x)q_{X}(x/\|x\|)}\bigg\vert.
$$  

Notice that for    $\|x\|>t$  ,  

$$
\begin{array}{r l}&{|h(\|x\|)p_{X}(x)-q_{X}(x/\|x\|)|=\Big|\displaystyle\int_{I}(h(\|x\|)p(x,y)-q(x/\|x\|,y))d y\Big|}\\ &{\qquad\qquad\qquad\qquad\leq2M\displaystyle\operatorname*{sup}_{s\geq t,(\omega,y)\in\mathbb{S}\times I}|h(s)p(s\omega,y)-q(\omega,y)|:=U(t),}\end{array}
$$  

where the upper bound  vanishes as because of (12). Now, for  and ,    $U(t)$     $t\to\infty$     $\|x\|>t$     $y\in I$  

$$
A(x,y)\leq\frac{\operatorname*{sup}_{\|x\|\geq t,y\in I}h(\|x\|)p(x,y)}{\operatorname*{inf}_{\|x\|>t}h(\|x\|)p_{X}(x)\operatorname*{inf}_{\omega\in\mathbb{S}}q_{X}(\omega)}U(t).
$$  

Regarding the numerator of the above display, recall that the density function    is continuous on the compact set    $\mathbb{S}$  ,  $q$  whence it is upper bounded. Because of uniform convergence (12), it is also true that   $\begin{array}{r}{\operatorname*{sup}_{\|\boldsymbol{x}\|\ge t,\boldsymbol{y}\in I}h(\|\boldsymbol{x}\|)p(\boldsymbol{x},\boldsymbol{y})}\end{array}$   is upper bounded by a finite constant for    $t$   large enough. In addition, our lower bound assumption (13) on    together  $q$  with uniform convergence (23) show that the denominator is ultimately (as    $t\rightarrow\infty$  ) lower bounded by a positive constant. Summarizing, we have shown that   $\begin{array}{r}{\operatorname*{sup}_{\|x\|>t,y\in\mathbb{S}}A(x,y)\to0}\end{array}$   as    $t\to\infty$  , finishing the proof of (11).  

It remains to prove that for all    $y\,\in\,I$  ,    $x\,\mapsto\,p(x,y)/p_{X}(x)$   is continuous and that    $p(x,y)/p_{X}(x)$   is uniformly ed. For all    $y\in I$  , the continuity of    $x\mapsto p(x,y)/p_{X}(x)$   follows from the continuity of    $p$  . Notice again that for  $\boldsymbol{x}\in\mathbb{R}^{d}$    and    $y\in I$  

$$
{\frac{p(x,y)}{p_{X}(x)}}={\frac{h(\|x\|)p(x,y)}{h(\|x\|)p_{X}(x)}}.
$$  

The numerator uniformly converges to    $q$  , which is uniformly bounded. The denominator uniformly converges to    $q_{X}$  , which is uniformly lower bounded by Equation (13). Then   $\begin{array}{r}{\operatorname*{sup}_{\vert\vert x\vert\vert\ge1,y\in I}(p(x,y)/p_{X}(x))}\end{array}$   is finite, which concludes the proof. ■  

# B.2 Proofs and Additional Results regarding Example 1  

In this section, we show that a generic heavy-tailed regression model (Example 1) satisfies the requirements of our assumptions. Subsequently, we establish that two widely used models, the additive and multiplicative noise models, constitute particular instances of that generic model.  

Proposition B.1  In the setting of Example   $\mathit{1}$  , the random pair    $(X,Y)$   satisfies Assumption 1, 2 and 3. In partic- ular, the limit distribution    $P_{\infty}$  in Equation  (9)  is given by  

$$
\begin{array}{r}{P_{\infty}=\mathcal{L}(X_{\infty},g_{\theta}(X_{\infty}/\|X_{\infty}\|,\varepsilon)),}\end{array}
$$  

where    $X_{\infty}$  follows the limit distribution  

$$
Q_{\infty}=\operatorname*{lim}_{t\to\infty}{\mathcal{L}}(t^{-1}X\mid\|X\|\geq t).
$$  

proof.  Assumption 1 is obviously fulfilled with    $M=\mathrm{sup}_{x,z\in\mathbb{R}^{d}\times\mathbb{R}}\left|g(x,z)\right|$  . Regar Assumption 2 and the limit distribution, we consider a bounded and Lipschitz function  l  $l:\mathbb{R}^{d}\times\mathbb{R}\rightarrow\mathbb{R}$    ×  → . For all  t >  0, writing   $\Theta=\|X\|^{-1}X$  , we have  

$$
\begin{array}{r l}&{\mathbb{E}\left[l(t^{-1}X,Y)\mid\|X\|\ge t\right]=\mathbb{E}\left[l(t^{-1}X,g(X,\varepsilon))\mid\|X\|\ge t\right]}\\ &{\qquad\qquad\qquad\qquad=\mathbb{E}\left[l(t^{-1}X,g_{\theta}(\Theta,\varepsilon))\mid\|X\|\ge t\right]+\ldots}\\ &{\qquad\qquad\qquad\quad\mathbb{E}\left[l(t^{-1}X,g(X,\varepsilon))-l(t^{-1}X,g_{\theta}(\Theta,\varepsilon))\mid\|X\|\ge t\right].}\end{array}
$$  

Since    $\varepsilon$   is independent from    $X$  , writing   $\Theta_{\infty}=\|X_{\infty}\|^{-1}\Theta_{\infty}$  , the regular variation of    $X$   and continuity of    $l$   and    $g_{\theta}$  imply that  

$$
\begin{array}{r}{\mathbb{E}\left[l(t^{-1}X,g_{\theta}(\Theta,\varepsilon))\mid\|X\|\ge t\right]\rightarrow\mathbb{E}\left[l(X_{\infty},g_{\theta}(\Theta_{\infty},\varepsilon))\right].}\end{array}
$$  

Because    $l$   is Lipschitz continuous (for some Lipschitz constant    $C$  ) and    $X$   and    $\varepsilon$   are independent, we have  

$$
\begin{array}{r l}&{\mathbb{E}\left[l(t^{-1}X,g(X,\varepsilon))-l(t^{-1}X,g_{\theta}(\Theta,\varepsilon))\mid\|X\|\ge t\right]\big|}\\ &{\le C\mathbb{E}\Big[|g(X,\varepsilon)-g_{\theta}(\Theta,\varepsilon)|\left|\|X\|\ge t\right]}\\ &{\le C\mathbb{E}\Big[\operatorname*{sup}_{\|x\|\ge t}|g(x,\varepsilon)-g_{\theta}(\theta(x),\varepsilon)|\Big].}\end{array}
$$  

The right-hand side tends to zero as    $t\,\rightarrow\,+\infty$  , from the dominated convergence theorem which applies because  $\begin{array}{r}{\operatorname*{sup}_{\|\boldsymbol{x}\|\ge t}|g(\boldsymbol{x},\boldsymbol{\varepsilon})-g_{\theta}(\boldsymbol{x}/\|\boldsymbol{x}\|,\boldsymbol{\varepsilon})|\le M}\end{array}$   and because of our model assumption (14). Thus Assumption 2 is satisfied and  $P_{\infty}=\mathcal{L}(X_{\infty},g_{\theta}(\Theta_{\infty},\varepsilon))$  )).  

We now show that Assumption 3 also holds true by proving the stronger condition (i) from Proposition 1. For  $\boldsymbol{x}\in\mathbb{R}^{d}$    with    $\|x\|\geq t$  , we have by independence of    $X$   and    $\varepsilon$  ,  

$$
\begin{array}{r l}&{|f^{*}(x)-f_{P_{\infty}}^{*}(\theta(x))|=\left|\mathbb{E}\left[g(x,\varepsilon)\right]-\mathbb{E}\left[g_{\theta}(\theta(x),\varepsilon)\right]\right|}\\ &{\qquad\qquad\qquad\leq\mathbb{E}\left[\underset{\|x\|\geq t}{\operatorname*{sup}}\left|g(x,\varepsilon)-g_{\theta}(\theta(x),\varepsilon)\right|\right],}\end{array}
$$  

which entails   in (24) that   $\begin{array}{r}{\operatorname*{sup}_{\|\boldsymbol{x}\|\ge t}|f^{*}(\boldsymbol{x})\,-\,f_{P_{\infty}}^{*}(\boldsymbol{x}/\|\boldsymbol{x}\|)|\,\rightarrow\,0}\end{array}$  0, as    $t\,\rightarrow\,+\infty$  .  ince    $g$   is assumed continuous and bounded,  f  $f^{*}$    ∗ is continuous. Thus, the sufficient condition (i) from Proposition 1 is satisfied, which shows that Assumption 3 holds true. ■  

We now turn to the two sub-examples given by the additive and multiplicative noise models mentioned after Example 1 from the main paper. We show that under mild assumptions, both sub-examples indeed satisfy the conditions specified in Proposition B.1.  

Proposition B.2  Consider the additive noise model  

$$
Y={\tilde{g}}(X)+\varepsilon,
$$  

where    $X$   is a regularly varying random vector in    $\mathbb{R}^{d}$    such that  

$$
{\mathcal{L}}(t^{-1}X\mid\|X\|\geq t)\to{\mathcal{L}}(X_{\infty}),
$$  

as    $t\to+\infty$  ,    $\varepsilon$   is a bounded real-valued rand  variable defined on the same probability space independent from    $X$  and  ˜ θ is a bounded, continuous function on  R  $\mathbb{R}^{d}$    which converges uniformly to some angular mapping    $\tilde{g}_{\theta}:\mathbb{S}\rightarrow\mathbb{R}$   :  → , in the sense that  

$$
\operatorname*{sup}_{\|x\|\geq t}|\widetilde{g}(x)-\widetilde{g}_{\theta}(\theta(x))|\to0\ a s\ t\to+\infty.
$$  

Then, the random ir    $(X,Y)$   satisfies the requirements of Proposition   $B.1$   with    $\begin{array}{r}{M=\operatorname*{sup}_{x\in\mathbb{R}^{d}}|\tilde{g}(x)|+||\varepsilon||_{\infty}}\end{array}$  |  || || . The ∞ limit distribution  P  $P_{\infty}$  in Equation  (9)  is  

$$
P_{\infty}=\mathcal{L}\big(X_{\infty},\tilde{g}_{\theta}(\theta(X_{\infty}))+\varepsilon\big).
$$  

proof. ecause    $\varepsilon$   is almost surely  $m_{\varepsilon}\in\mathbb{R}_{+}$  negati  $\varepsilon\ \ \ \in$  a.s. ∈

  $[-m_{\varepsilon},+m_{\varepsilon}]$  − ]. Consider the mapping  g  $g:(x,z)\in\mathbb{R}^{d}\times[-m_{\varepsilon},+m_{\varepsilon}]\mapsto g(x)+z$   ∈   × −  7→  and  g  $g_{\theta}:(\omega,z)\in\mathbb{S}\times[-m_{\varepsilon},+m_{\varepsilon}]\mapsto$   : (  ∈  × −  7→

  $\tilde{g}_{\theta}(\omega)+z$  . The function    $g$   is continuous and bounded by    $M\,=\,\operatorname*{sup}_{x\in\mathbb{R}^{d}}\,|\tilde{g}(x)|+m_{\varepsilon}$  |  and the pair   $\left(g,g_{\theta}\right)$   satisfies Equation (14). Indeed for all    $z\in[-m_{\varepsilon},+m_{\varepsilon}]$  ,  

$$
\operatorname*{sup}_{\|x\|\geq t}|g(x,z)-g_{\theta}(\theta(x),z)|=\operatorname*{sup}_{\|x\|\geq t}|\widetilde{g}(x)-\widetilde{g}_{\theta}(\theta(x))|\rightarrow0,
$$  

as    $t\to+\infty$  , which concludes the proof.  

Proposition B.3  Consider the multiplicative noise model  

$$
Y=\varepsilon{\tilde{g}}(X),
$$  

where    $(X,\varepsilon)$   and    $\tilde{g}$   are as in Proposition B.2. Then, the random pair    $(X,Y)$   satisfies the requirements of Proposi- tion   $B.1$   with    $\begin{array}{r}{M=\operatorname*{sup}_{x\in\mathbb{R}^{d}}\left|\tilde{g}(x)\right|\times\|\varepsilon\|_{\infty}}\end{array}$  |×∥ ∥ and the limit distribution    $P_{\infty}$  in  (9)  is given by    $P_{\infty}=\mathcal{L}(X_{\infty},\varepsilon\tilde{g}_{\theta}(\theta(X_{\infty})))$  , ∞ ∞ where    $\tilde{g}_{\theta}$   and    $X_{\infty}$  are as in Proposition B.2.  

proof.  

Consider the mapping    $g(x,z)=z{\tilde{g}}(x)$  ) and    $g_{\theta}(\omega,z)=z\tilde{g}_{\theta}(\omega)$  ). Let    $m_{\varepsilon}$   be as in the proof of Proposition B.2. On the domain    $\mathbb{R}^{d}\times[-m_{\varepsilon},m_{\varepsilon}]$  , the function    $g$   is continuous and bounded by    $\begin{array}{r}{M=m_{\varepsilon}\operatorname*{sup}_{x\in\ensuremath{\mathbb{R}}^{d}}|\tilde{g}(x)|}\end{array}$  | . The pair   $\left(g,g_{\theta}\right)$  satisfies (14) since for all    $z\in[-m_{\varepsilon},+m_{\varepsilon}]$  

$$
\operatorname*{sup}_{\|x\|\ge t}|g(x,z)-g_{\theta}(x/\|x\|,z)|\le m_{\varepsilon}\operatorname*{sup}_{\|x\|\ge t}|\tilde{g}(x)-\tilde{g}_{\theta}(\theta(x))|\xrightarrow[t\to\infty]{}0,
$$  

which concludes the proof.  

# B.3 Proofs regarding Example 2  

Let  $\tilde{E}=\mathbb{R}^{d+1}\setminus\{0_{\mathbb{R}^{d+1}}\}$    \ { } ,    $E=\mathbb{R}^{d}\setminus\{0_{\mathbb{R}^{d}}\}$  for simplicity denote both by    $\mathbb{B}_{d}$   the    $d$  -dimensional unit ba image by the canonical e bedding  $\mathbb{R}^{d}\to\mathbb{R}^{d+1}$    → ,  i.e.    $\mathbb{B}_{d}=\{\tilde{x}\in\mathbb{R}^{d+1}:\|(\tilde{x}_{1},.\,.\,,\tilde{x}_{d})\|\leq1,\tilde{x}_{d+1}\in\mathbb{R}\}$   ∈    ∥ . For ˜  $\tilde{x}\in\mathbb{R}^{d+1}$  +1 we denote by    $x$   the first  d  coordinates of ˜ ,    $x=\left(\tilde{x}_{1},.\,.\,.\,,\tilde{x}_{d}\right)$  ). Denote by    $\varphi$   the continuous mapping sending  X ˜  to  $(X,Y)$  ,  i.e.  

$$
\begin{array}{r l}&{\varphi:\quad E\times\mathbb{R}\to E\times(-1,1)}\\ &{\quad\tilde{x}=(x,z)\mapsto(x,y)=(x,z/\|(x,z)\|).}\end{array}
$$  

Equipped with these notations, we may proceed with the proof.  

(a)  Assumption 1 is trivially satisfied because    $|Y|\leq1$  .  

(b)  We now show that Assumption 2 holds with limit pair   $(X_{\infty},Y_{\infty})$   as in the second part of the statement. Equipped with the notations introduced above, the pair defined in the statement may be written as   $(X_{\infty},Y_{\infty})=$   $\varphi(\tilde{X}_{\infty})$  ), where  $\tilde{X}_{\infty}$  is well defined by regular variation of the full vector  $\tilde{X}$  . We need to show that for any bounded, ∞ ∞ continuous function    $g$  ,  

$$
{\ensuremath{\mathbb E}}\left[g(X/t,Y)\,|\,\|\tilde{X}\|\geq t\right]\to{\ensuremath{\mathbb E}}\left[g\circ\varphi(\tilde{X}_{\infty})\,|\,\|\tilde{X}_{\infty,1:d}\|\geq1\right].
$$  

However   $(X/t,Y)=\varphi(\tilde{X}/t)$  ) and    $\|X\|\geq t\Rightarrow\|{\tilde{X}}\|\geq t$  ∥≥ . Thus  

$$
\begin{array}{r l}&{\mathbb{E}\left[g(X/t,Y)\,|\,\|X\|\geq t\right]=\frac{\mathbb{E}\left[g\circ\varphi(\tilde{X}/t)\mathbb{1}\{\|X/t\|\geq1\}\mathbb{1}\{\|\tilde{X}/t\|\geq1\}\right]}{\mathbb{P}\left\{\|\tilde{X}/t\|\geq1\right\}}\frac{\mathbb{P}\left\{\|\tilde{X}/t\|\geq1\right\}}{\mathbb{P}\left\{\|X/t\|\geq1\right\}}}\\ &{\qquad\qquad\qquad=\mathbb{E}\left[g\circ\varphi(\tilde{X}/t)\mathbb{1}\{\|X/t\|\geq1\}\,|\,\|\tilde{X}\|\geq t\right]\frac{\mathbb{P}\left\{\|\tilde{X}/t\|\geq1\right\}}{\mathbb{P}\left\{\|X/t\|\geq1\right\}}}\\ &{\qquad\qquad\qquad\to\mathbb{E}\left[g\circ\varphi(\tilde{X}_{\infty})\mathbb{1}\{\|\tilde{X}_{\infty,1:d}\|\geq1\}\right]\frac{1}{\mathbb{P}\left\{\|\tilde{X}_{\infty,1:d}\|\geq1\right\}},}\end{array}
$$  

where the convergence of the first term in the latter expression is obtained by approaching the (discontinuous) function    $\mathbb{1}\{\|z\|\ge1\}$   by continuous ones and using the fact that the boundary of    $\mathbb{B}_{d}$   in    $\mathbb{R}^{d+1}$    is not a cone, whence it cannot carry any positive    $\mu$  -mass (a standard feature of radially homogeneous measures).  

(c) We now prove that Assumption 3 holds true by proving the stronger condition (10) which rephrase in our setting as  

$$
\operatorname*{sup}_{\|x\|=1}|f^{*}(t x)-f_{P_{\infty}}^{*}(t x)|\underset{t\to+\infty}{\longrightarrow}0.
$$  

Indeed if (25) holds, then  0, so that  $\begin{array}{r}{\operatorname*{sup}_{s\geq t}\operatorname*{sup}_{\|x\|=1}|f^{*}(t x)-f_{P_{\infty}}^{*}(t x)|\underset{t\to+\infty}{\longrightarrow}0}\end{array}$  

$$
\operatorname*{sup}_{\|x\|\geq t}|f^{*}(x)-f_{P_{\infty}}^{*}(x)|=\operatorname*{sup}_{\|x\|\geq1}|f^{*}(t x)-f_{P_{\infty}}^{*}(t x)|=\operatorname*{sup}_{s\geq t}\operatorname*{sup}_{\|x\|=1}|f^{*}(s x)-f_{P_{\infty}}^{*}(s x)|\underset{t\to+\infty}{\longrightarrow}0.
$$  

Notice first that for    $\boldsymbol{x}\in\mathbb{R}^{d}$    such that    $\|x\|\geq1$  ,    $f^{*}(x)$   and    $f_{P_{\infty}}^{*}(x)$  ) may be written in terms of integrals  

$$
f^{*}(x)=\int_{z\in\mathbb{R}}\frac{z}{\Vert(x,z)\Vert}\frac{p(x,z)}{p(x)}\,\mathrm{d}z,
$$  

where for simplicity we denote by    $p(x)$   the marginal density of the first    $d$   components of  $\tilde{X}$   at    $x$  , and also    $p(x,z)$  the joint density at   $\tilde{x}=(x,z)$  ).  

In the present setting,    $f_{P_{\infty}}^{*}$  is defined as    $f_{P_{\infty}}^{*}(X_{\infty})=\mathbb{E}\left[Y_{\infty}\mid X_{\infty}\right]$  ]. Introduce  $\tilde{Z}=(\tilde{Z}_{1},.\,.\,.\,,\tilde{Z}_{d+1})$  ) distributed ˜ 1). Then ∞ as    $\mathcal{L}(\tilde{X}_{\infty}\,|\,\|\tilde{X}_{\infty,1:d}\|\geq1)$  | ∥ ∥≥  $\tilde{Z}$   has density    $C q(x,z)$   on    $\mathbb{B}_{d}^{c}\times\mathbb{R}$    × , and marginal density for its first    $d$   components, ∞ ∞

  $\begin{array}{r}{C q(x)\;:=\;\int_{\mathbb{R}}C q(x,z)\,\mathrm{d}z}\end{array}$   ˜ . With these notations we have   $\left(X_{\infty},Y_{\infty}\right)\ \stackrel{d}{=}\ \left(\tilde{Z}_{1:d},\tilde{Z}_{d+1}/\Vert\tilde{Z}_{1:d}\right)$  ∥ ), whence    $f_{P_{\infty}}^{\ast}(\tilde{Z}_{1:d})\;=$  ∞

  $\mathbb{E}\left[\tilde{Z}_{d+1}/\|\tilde{Z}\|\,|\,\tilde{Z}_{1:d}\right]$  ∥ ∥| almost surely. We obtain, for    $\|x\|\geq1$  ,  

$$
f_{P_{\infty}}^{*}(x)=\int_{\mathbb{R}}\frac{z}{\Vert(x,z)\Vert}\frac{C q(x,z)}{C q(x)}\,\mathrm{d}z=\int_{\mathbb{R}}\frac{z}{\Vert(x,z)\Vert}\frac{q(x,z)}{q(x)}\,\mathrm{d}z.
$$  

Combining the latter two displays we obtain  

$$
|f^{*}(x)-f_{P_{\infty}}^{*}(x)|\leq\int_{z\in\mathbb{R}}\left|\frac{p(x,z)}{p(x)}-\frac{q(x,z)}{q(x)}\right|\,\mathrm{d}z.
$$  

Introduce as in Lemma 2 the function    $h(t)\,=\,t^{d+1}/\mathbb{P}\left\{\|X\|\geq t\right\}$  . For    $\|{\boldsymbol{x}}\|\,=\,1$  , by a change of variable    $r\,=\,z/t$  in (26), we obtain  

$$
\begin{array}{r l r}&{}&{|f^{*}(t x)-f_{P_{\infty}}^{*}(t x)|\leq\displaystyle\int_{r\in\mathbb{R}}\left|\frac{p(t x,t r)}{p(t x)}-\frac{q(t x,t r)}{q(t)}\right|t\,\mathrm{d}r}\\ &{}&{\qquad\qquad\qquad=\displaystyle\int_{r\in\mathbb{R}}\left|\frac{h(t)p(t x,t r)}{t^{-1}h(t)p(t x)}-\frac{q(x,r)}{q(x)}\right|\,\mathrm{d}r,}\end{array}
$$  

since by homogeneity of    $q$  , it holds that    $q(t x,t r)=t^{-d-1-\alpha}q(x,r)$   while    $q(t x)=t^{-d-\alpha}q(x)$  . Thus  

$$
\operatorname*{sup}_{\|x\|=1}|f^{*}(t x)-f_{P_{\infty}}^{*}(t x)|\leq\int_{r\in\mathbb{R}}\operatorname*{sup}_{\|x\|=1}\left|\frac{h(t)p(t x,t r)}{t^{-1}h(t)p(t x)}-\frac{q(x,r)}{q(x)}\right|\,\mathrm{d}r.
$$  

We have the following controls over the quantities in the latter integrand:  

1.    $q(x)$   is lower bounded by a positive constant (Lemma 3)  

2.   $\begin{array}{r}{\operatorname*{sup}_{\|\boldsymbol{x}\|=1}\left|h(t)t^{-1}p(t\boldsymbol{x})-q(\boldsymbol{x})\right|\underset{t\rightarrow+\infty}{\longrightarrow}0\mathrm{~(Lemma~2)},}\end{array}

$  

3. For all fixed    $r$  , because of (17), and since    $\|(x,r)\|\geq\|x\|$  ,  

$$
\begin{array}{r l r}{\underset{\|\boldsymbol{x}\|=1}{\operatorname*{sup}}\,|h(t)p(t\boldsymbol{x},t\boldsymbol{r})-q(\boldsymbol{x},\boldsymbol{r})|\leq\underset{\|\boldsymbol{\tilde{u}}\|\geq1}{\operatorname*{sup}}\,|h(t)p(t\boldsymbol{\tilde{u}})-q(\boldsymbol{\tilde{u}})|}&{}\\ {\underset{t\to+\infty}{\longrightarrow}0.}&{}\end{array}
$$  

Thus, combining 1., 2., 3. above, for fixed    $r$  , the integrand    $J(t,r)$   in (27) converges to   $0$   as    $t\,\rightarrow\,+\infty$  . In order to apply the dominated convergence theorem, we verify that    $J(t,r)$   is upper bounded by an integrable function of    $r$  . The argument is somewhat similar to the one in the proof of Lemma 2. We decompose the integrand as  

$$
\begin{array}{r l}&{J(t,r)\leq\underbrace{\underset{\|x\|=1}{\operatorname*{sup}}\frac{h(t)}{h(t)\|(x,r)\|)}}_{A(t,r)}\underbrace{\underset{\|x\|=1}{\operatorname*{sup}}\frac{h(t)\|(x,r)\|)p\big(t\|(x,r)\|\theta(x,r)\big)}{t^{-1}h(t)p(t x)}}_{B(t,r)}+\,.\,.}\\ &{\qquad\underbrace{\cdot\,.\,\underset{\|x\|=1}{\operatorname*{sup}}\frac{q(x,r)}{q(x)}}_{C(t,r)}}\\ &{=A(t,r)B(t,r)+C(t,r).}\end{array}
$$  

From the proof of Lemma 2 (see Equation (28)) we have that for    $t\geq t_{0}$   large enough, and for all    $r\in\mathbb{R}$  ,  

$$
A(t,r)\leq2\|(x,r)\|^{-d-\alpha/2-1}\leq2(1+r^{p})^{\frac{-d-\alpha/2-1}{p}},
$$  

an integrable function of    $r$  .  

The numerator and the denominator in the definition of    $B(t,r)$   converge as    $t\to+\infty$  , uniformly over    $\|x\|\geq1$  and    $r\in\mathbb{R}$  , respectively to    $q(x,r)$   and    $q(x)$  . The latter quantity is lower bo (Lemma 3) and    $q(x,r)$   is uniformly bounded for    $\|x\|=1$   (by homogeneity). Thus, for some constant  C >  0, for all    $t\geq t_{1}$   with some large enough    $t_{1}\geq t_{0}$  , we have  

$$
B(t,r)\leq C.
$$  

By homogeneity of    $q$   and Lemma 3 again, we have  

$$
C(t,r)\leq\operatorname*{sup}_{\|x\|=1}\|(x,r)\|^{-\alpha-d-1}\frac{\operatorname*{max}_{\omega\in\mathbb{S}_{d+1}}q(\omega)}{c}=(1+r^{p})^{\frac{-\alpha-d-1}{p}}\frac{\operatorname*{max}_{\omega\in\mathbb{S}_{d+1}}q(\omega)}{c},
$$  

which is an integrable function of    $r$  .  

Combining the bounds regarding    $A(t,r),B(t,r),C(t,r)$  , we have shown that    $A(t,r)B(t,r)+C(t,r)$   is upper bounded by an integrable function of    $r$  . The proof of the condition (10) is complete. It remains to show that  $f_{P_{\infty}}^{*}$  is continuous on    $\|x\|\geq1$  . Recall that for    $x\in\mathbb{R}^{d}\setminus\{0_{\mathbb{R}^{d}}\}$  ,  

$$
f_{P_{\infty}}^{*}(x)=\frac{1}{q(x)}\int_{\mathbb{R}}\frac{z}{\|(x,z)\|}q(x,z)d z.
$$  

The continuity of    $p$   implies that of    $q$   by Equation (16). By homogeneity of    $q$  , we have  

$$
\frac{z}{\Vert(x,z)\Vert}q(x,z)\leq q(x,z)=\Vert(x,z)\Vert^{-d-\alpha-1}q\big(\theta(x,z)\big)\leq(1+z^{p})^{\frac{-d-\alpha-1}{p}}\operatorname*{max}_{\omega\in\mathbb S_{d+1}}q(\omega).
$$  

Since    $z\mapsto\left(1+z^{p}\right)^{\frac{-d-\alpha-1}{p}}$  is integrable over    $\mathbb{R}$  , the dominated convergence theorem for continuity applies twice and entails that R  and 1   are continuous and then is continuous. The proof    $\begin{array}{r}{x\mapsto\int_{\mathbb{R}}\frac{z}{\vert\vert(x,z)\vert\vert}q(x,z)d z}\end{array}$     $\begin{array}{r}{x\mapsto{\frac{1}{q(x)}}}\end{array}$     $f_{P_{\infty}}^{*}$  ∥ ∥ ∞ is complete.  

Lemma 2 (Uniform Convergence of marginals of    $p$  . ) Under the assumptions of Example 2, we have  

$$
\begin{array}{l}{\displaystyle\operatorname*{sup}_{\|x\|=1}\left|\int_{\mathbb{R}}t^{-1}h(t)p(t x,z)\,{\mathrm{d}}z-q(x)\right|\underset{t\to+\infty}{\longrightarrow}0,\quad w h e r e}\\ {\displaystyle q(x)=\int_{z}q(x,z)\,{\mathrm{d}}z,\quad a n d\;h(t)=t^{d+1}/\mathbb{P}\left\{\|\tilde{X}\|\ge t\right\}.}\end{array}
$$  

proof.  We adapt the arguments of the proof of Theorem 2.1 of [19] to our context. With the notation    $h$   from our statement, our uniform convergence assumption (16) becomes  

$$
\operatorname*{sup}_{\omega\in\mathbb{S}_{d+1}}\left|h(t)p(t\omega)-q(\omega)\right|\underset{t\to+\infty}{\longrightarrow}0.
$$  

Now  

$$
\int_{\mathbb R}t^{-1}h(t)p(t x,z)\,\mathrm{d}z=\int_{\mathbb R}h(t)p(t x,t r)\,\mathrm{d}r,
$$  

so that  

$$
\operatorname*{sup}_{\|x\|=1}\left|\int_{\mathbb{R}}t^{-1}h(t)p(t x,z)\,\mathrm{d}z-q(x)\right|\leq\int_{\mathbb{R}}\operatorname*{sup}_{\|x\|=1}|h(t)p(t x,t r)-q(x,r)|\,\,\mathrm{d}r.
$$  

For fixed , because , the integrand in the right-hand side is less than    $r\in\mathbb{R}$     $\|(x,r)\|\geq\|x\|\geq1$  

$$
\operatorname*{sup}_{\lVert\tilde{u}\rVert\geq1}\left|h(t)p(t\tilde{u})-q(\tilde{u})\right|.
$$  

The latter display tends to zero as    $t\to+\infty$  because of (17). To conclude, we need to upper bound the integrand by an integrable function of    $r$  , in order to apply dominated convergence. We thus write  

$$
\begin{array}{r l}&{\underset{\|x\|=1}{\operatorname*{sup}}\ |h(t)p(t x,t r)-q(x,r)|}\\ &{\leq\underset{\|x\|=1}{\operatorname*{sup}}h(t)p(t x,t r)+\ \underset{\|x\|=1}{\operatorname*{sup}}q(x,r).}\\ &{=\underset{\|x\|=1}{\operatorname*{sup}}\frac{h(t)}{h(t\,\|(x,r)\|)}\underset{\|x\|=1}{\operatorname*{sup}}\ h(t\,\|(x,r)\|)p\Big(t\,\|(x,r)\|\ \theta(x,r)\Big)+\ \underset{\|x\|=1}{\operatorname*{sup}}\ q(x,r),}\end{array}
$$  

where    $\theta(x,r)\in\mathbb{S}_{d+1}$  .  

• The function    $h$   is regularly varying with positive index    $d\!+\!1\!+\!\alpha$  . By Karamata representation (Proposition 0.5 of [49]), for    $t$   large enough (say    $t\geq t_{0}$  ), for any    $s\geq1$  , we have  

$$
\frac{h(t)}{h(t s)}\leq2s^{-d-\frac{\alpha}{2}+1}.
$$  

Thus for    $t\geq t_{0}$  , for all    $r\in\mathbb{R}$  ,  

$$
A(t,r)\leq2\|(x,r)\|^{-d-\alpha/2-1}\leq2(1+r^{p})^{\frac{-d-\alpha/2-1}{p}},
$$  

which is an integrable function of    $r$   for any    $d\geq1,\alpha>0$  .  

• because    $\|(x,r)\|\geq\|x\|\geq1$   we have for all    $t\geq t_{0}$   large enough, uniformly over    $x$   such that    $\|x\|=1$   and    $r\in\mathbb{R}$  ,  

$$
\Big|h(t\,\|(x,r)\|)p\Big(t\,\|(x,r)\|\,\theta(x,r)\Big)-q\Big(\theta(x,r)\Big)\Big|\leq1,
$$  

thus for    $t\geq t_{0}$  , for all    $r$  ,  

$$
B(t,r)\leq\operatorname*{sup}_{\omega\in\mathbb{S}_{d+1}}q(\omega)+1,
$$  

which is a finite constant.  

• We may also upper bound    $C(t,r)$   by an integrable function of    $r$  , since by homogeneity of    $q$  ,  

$$
\begin{array}{r l}&{C(t,r)=\underset{\|x\|=1}{\operatorname*{sup}}\|(x,r)\|^{-d-\alpha-1}q\big(\theta(x,r)\big)}\\ &{\quad\quad\leq\underset{\omega\in\mathbb{S}_{d+1}}{\operatorname*{max}}\big(q(\omega)\big)(1+r^{p})^{\frac{-d-\alpha-1}{p}}}\end{array}
$$  

which is integrable for    $d\geq1$   and    $\alpha>0$  .  

As a consequence of the above three points, the quantity    $A(t,r)B(t,r)+C(t,r)$   is upper bounded by an integrable function of    $r$  . The result follows by dominated convergence. ■  

Lemma 3 (Upper and lower bounds for the marginals of    $q$  )  Under the conditions of Example 2, there ex- ists positive constants    $c,C>0$   such that for all    $\boldsymbol{x}\in\mathbb{R}^{d}$    such that    $\|x\|=1$  ,  

$$
c\leq\int q(x,z)\,\mathrm{d}z\leq C.
$$  

proof.  For    $\boldsymbol{x}\in\mathbb{R}^{d}$    such that    $\|x\|=1$  , and    $z\in\mathbb{R}$   we have  

$$
q(x,z)=(1+z^{p})^{\frac{-\alpha-d-1}{p}}q(\theta(x,z)).
$$  

The results follows with    $\begin{array}{r}{c=\left(\operatorname*{min}_{\omega\in\mathbb{S}_{d+1}}q(\omega)\right)\,\int(1+z^{p})^{\frac{-\alpha-d-1}{p}}\mathrm{d}z}\end{array}$   and  

$$
C=(\operatorname*{max}_{\omega\in\mathbb S_{d+1}}q(\omega))\;\int(1+z^{p})^{\frac{-\alpha-d-1}{p}}\,\mathrm{d}z.
$$  

# C Proofs for Section 3  

# C.1 Proof of Theorem 1  

(i) In view of Characterization (iii) from Theorem A.1 (see also (8) in the main paper), Assumption 2 implies that the conditional distribution  

$$
{\mathcal{L}}(\Theta,Y,\|X\|/t\mid\|X\|>t)
$$  

conver es weakly to the distribution of   $\left(\Theta_{\infty},Y_{\infty},\|X_{\infty}\|\right)$  . Now if    $f=h\circ\theta$   is a prediction function on    $\mathbb{R}^{d}$  , where  h  is a continuous function defined on  S , then by compactness of  S  the function   $(\theta,y)\mapsto(h(\theta)-y)^{2}$    is atically bounded and continuous on the domain    $\mathbb{S}\times[-M,M]$  . Thus by weak convergence we obtain as ,  

$$
R_{t}(f)=\mathbb{E}\left[(h(\Theta)-Y)^{2}\,|\,\|X\|>t\right]\rightarrow\mathbb{E}\left[(h(\Theta_{\infty})-Y_{\infty})^{2}\right]=R_{P_{\infty}}(f).
$$  

(ii) Recall that    $R_{t}^{*}=R_{t}(f^{*})$     ∗ ) where    $f^{*}$  is the regression function for the pair (  $(X,Y)$   ) and    $R_{P_{\infty}}^{*}=R_{P_{\infty}}(f_{P_{\infty}}^{*})$  ) where  $f_{P_{\infty}}^{*}$  is the regression function for the pair   $(X_{\infty},Y_{\infty})$   defined in Lemma 1. Now we decompose    $R_{t}^{*}$    as ∞  

$$
\begin{array}{r l}&{{R}_{t}^{*}=\mathbb{E}\left[(Y-f^{*}(X))^{2}\,|\,\|X\geq t\right]}\\ &{\quad=\underbrace{\mathbb{E}\left[(Y-f_{P_{\infty}}^{*}(X))^{2}\,|\,\|X\|\geq t\right]}_{A_{t}}+\underbrace{\mathbb{E}\left[(f_{P_{\infty}}^{*}(X)-f^{*}(X))^{2}\,|\,\|X\|\geq t\right]}_{B_{t}}+\cdot\cdot\cdot}\\ &{\qquad\qquad\cdot\underbrace{2\mathbb{E}\left[(Y-f_{P_{\infty}}^{*}(X))(f_{P_{\infty}}^{*}(X)-f^{*}(X))\,|\,\|X\|\geq t\right]}_{C_{t}}.}\end{array}
$$  

The first term    $A_{t}$   is simply    $R_{t}(f_{P_{\infty}}^{*})$  ). From Lemma   $1$  ,    $f_{P_{\infty}}^{*}$  is an angular function, thus Property (i) of the statement implies that    $A_{t}\to R_{P_{\infty}}(f_{P_{\infty}}^{*})$  ∞ ), which is    $R_{P_{\infty}}^{*}$  . ∞  

We now show that the second and third terms    $B_{t},C_{t}$   vanish. We use that, as a consequence of Assumption 1,  $\forall x\in\mathbb{R}^{d}$  ,    $|f_{P_{\infty}}^{*}(x)|\leq M$   and,    $|f^{*}(x)|\leq M$  . Thus  

$$
B_{t}\leq4M^{2}\mathbb{E}\left[|f_{P_{\infty}}^{*}(X)-f^{*}(X)|\,|\,\|X\|\geq t\right].
$$  

Assumption 3 ensures that the latter display converges to   $0$   as    $t\to\infty$  . Similarly, using Assumptions 1 and 3 again, we obtain  

$$
|C_{t}|\leq4M^{2}\mathbb{E}\left[|f_{P_{\infty}}^{*}(X)-f^{*}(X)|\,|\,\|X\|\geq t\right]\underset{t\to+\infty}{\longrightarrow}0.
$$  

We have proved that .    $R_{t\_t\rightarrow+\infty}^{*}\,R_{P_{\infty}}^{*}

$  

(iii) Recall from the introduction that    $R_{\infty}^{*}=R_{\infty}(f^{*})=\operatorname*{lim}\operatorname*{sup}_{t}R_{t}(f^{*})$  ). Because of (ii), in fact    $R_{t}(f^{*})$   converges ∞ ∞ to    $R_{P_{\infty}}^{*}$  . Thus  

$$
\operatorname*{lim}_{t}\operatorname*{sup}_{{\cal T}}R_{t}(f^{*})=\operatorname*{lim}_{t}R_{t}(f^{*})=R_{P_{\infty}}^{*},
$$  

and the result follows.  

(iv) From Property (iii) of the statement, we have    $R_{\infty}^{*}=R_{P_{\infty}}(f_{P_{\infty}}^{*})$  ). Now, Property (i) of the statement and the angular nature of    $f_{P_{\infty}}^{*}$  (Lemma 1) imply that    $R_{P_{\infty}}(f_{P_{\infty}}^{*})=R_{\infty}(f_{P_{\infty}}^{*})$  ∞ ∞ ).  

# C.2 Proof of Theorem 2  

We recall for convenience a Bernstein-type inequality due to C. McDiarmid (see Theorem 3.8 of [41]) which is a key ingredient of the proof of Theorem 2.  

Lemma 4 (Bernstein-type ine lity, [41])  Let  with  taking values in a set  and let  be    $X\,=\,\left(X_{1:n}\right)$     $X_{i}$     $\mathcal{X}$     $f$  a real-valued func ned on . Let . Consider the positive deviation functions, defined for  X  $\mathcal X^{n}$     $Z\,=\,f(X_{1:n})$   $1\leq i\leq n$   and for  $x_{1:i}\in\mathcal{X}^{i}$  ,  

$$
g_{i}(x_{1:i})=\mathbb{E}\left[Z|X_{1:i}=x_{1:i}\right]-\mathbb{E}\left[Z|X_{1:i-1}=x_{1:i-1}\right].
$$  

Denote by  b  the maximum deviation  

$$
b=\operatorname*{max}_{1\leq i\leq n}\operatorname*{sup}_{x_{1:i}\in\mathcal{X}^{i}}g_{i}(x_{1:i}).
$$  

Let   v  be the supremum of the sum of conditional variances,  

$$
\hat{v}=\operatorname*{sup}_{(x_{1},\ldots,x_{n})\in\chi^{n}}\sum_{i=1}^{n}\sigma_{i}^{2}(f,x_{1:i-1}),
$$  

where    $\sigma_{i}^{2}(f,x_{1:i-1}))=\mathbb{V}\mathrm{ar}[g_{i}(X_{1:i})\,|\,X_{1:i-1}=x_{1:i-1}]$   | . If    $b$   and   v  are both finite, then − − −  

$$
\mathbb{P}\{Z-\mathbb{E}\left[Z\right]\ge\varepsilon\}\le\exp{\left(\frac{-\varepsilon^{2}}{2(\hat{v}+b\varepsilon/3)}\right)},
$$  

for    $\varepsilon>0$  .  

Introduce an intermediate risk functional  

$$
\tilde{R}_{t_{n,k}}(h\circ\theta)=\frac{1}{k}\sum_{i=1}^{n}\Big(h(\theta(X_{i}))-Y_{i}\Big)^{2}\mathbb{1}\{\|X_{i}\|\geq t_{n,k}\},
$$  

and notice that    $\mathbb{E}\left[\tilde{R}_{t_{n,k}}(h\circ\theta)\right]=R_{t_{n,k}}(h\circ\theta)$  ). Our proof is based on the following risk decomposition,  

$$
\begin{array}{r}{\underset{h\in\mathcal{H}}{\operatorname*{sup}}\,\Big|\hat{R}_{k}(h\circ\theta)-R_{t_{n,k}}(h\circ\theta)\Big|\leq\underset{h\in\mathcal{H}}{\operatorname*{sup}}\,\Big|\hat{R}_{k}(h\circ\theta)-\tilde{R}_{t_{n,k}}(h\circ\theta)\Big|+.\,.}\\ {\underset{h\in\mathcal{H}}{\operatorname*{sup}}\,\Big|\tilde{R}_{t_{n,k}}(h\circ\theta)-R_{t_{n,k}}(h\circ\theta)\Big|.}\end{array}
$$  

Regarding the first term on the right-hand side of Inequality (29),  

$$
\begin{array}{r l}&{\underset{h\in\mathcal{H}}{\operatorname*{sup}}\Big|\hat{R}_{k}(h\circ\theta)-\tilde{R}_{t_{n,k}}(h\circ\theta)\Big|}\\ &{\qquad\qquad\qquad=\underset{h\in\mathcal{H}}{\operatorname*{sup}}\frac{1}{k}\Big|\sum_{i=1}^{n}\Big(h\circ\theta(X_{i})-Y_{i}\Big)^{2}\big(\mathbb{1}\{\|X_{i}\|\geq t_{n,k}\}-\mathbb{1}\{\|X_{i}\|\geq\|X_{(k)}\}\big)\Big|}\\ &{\qquad\qquad\leq\frac{4M^{2}}{k}\sum_{i=1}^{n}\big|\mathbb{1}\{\|X_{i}\|\geq t_{n,k}\}-\mathbb{1}\{\|X_{i}\|\geq\|X_{(k)}\}\big|.}\end{array}
$$  

The number of nonzero terms inside the sum in the above display is the number of indices  such that ‘  $i$     $\|X_{i}\|<\|X_{(k)}\|$  and ’, or the other way around. In other words    $\|X_{i}\|\geq t_{n,k}$  

$$
\begin{array}{r}{\left|\mathbb{1}\{\|X_{i}\|\ge t_{n,k}\}-\mathbb{1}\{\|X_{i}\|\ge\|X_{(k)}\}\right|\ne0\}\subset\Big(\big\{t_{n,k}\le X_{i}<X_{(k)}\big\}\cup\big\{X_{(k)}\le X_{i}<t_{n,k}\big\}\Big).}\end{array}
$$  

Considering separately the cases where  and  we obtain  $X_{(k)}\leq t_{n,k}$   ≤    $X_{(k)}>t_{n,k}$  

$$
\operatorname*{sup}_{h\in\mathcal{H}}\Big|\hat{R}_{k}\big(h\circ\theta\big)-\tilde{R}_{t_{n,k}}\big(h\circ\theta\big)\Big|\leq\frac{4M^{2}}{k}\Big|\sum_{i=1}^{n}\mathbb{1}\big\{\|X_{i}\|\geq t_{n,k}\big\}-k\Big|.
$$  

Notice that  ${\textstyle\sum_{i=1}^{n}1\!\!\!\mathrm{\Gamma}\{\|X_{i}\|\ge t_{n,k}\}}$  {∥ ∥≥ }  follows a Binomial distribution with parameters   $(n,k/n)$  . The (classical) Bernstein inequality as stated  e.g. , in [41], Theorem 2.7, yields  

$$
\begin{array}{r l r}{\lefteqn{\mathbb{P}\Big\{\operatorname*{sup}_{h\in\mathcal{H}}\Big|\hat{R}_{k}(h\circ\theta)-\tilde{R}_{t_{n,k}}(h\circ\theta)\Big|\geq\varepsilon\Big\}\leq\mathbb{P}\Big\{\Big|\sum_{i=1}^{n}\mathbb{1}\{\|X_{i}\|\geq t_{n,k}\}-k\Big|\geq k\varepsilon/(4M^{2})\Big\}}}\\ &{}&{\leq2\exp\Big(\frac{-k\varepsilon^{2}}{32M^{4}+8M^{2}\varepsilon/3}\Big).\ \ \ \ }\end{array}
$$  

We now turn to the second term of Inequality (29), and we apply Lemma 4 to the function  

$$
f((x_{1},y_{1}),...,(x_{n},y_{n}))=\operatorname*{sup}_{h\in\mathcal{H}}\Big|\frac{1}{k}\sum_{i=1}^{n}\Big(h\circ\theta(x_{i})-y_{i}\Big)^{2}\mathbb{1}\{\|x_{i}\|\geq t_{n,k}\}-R_{t_{n,k}}(h\circ\theta)\Big|,
$$  

so that    $\begin{array}{r}{f((X_{1},Y_{1}),...,(X_{n},Y_{n}))=\operatorname*{sup}_{h\in\mathcal{H}}\left|\Bar{R}_{t_{n,k}}(h\!\circ\!\theta)\!-\!R_{t_{n,k}}(h\!\circ\!\theta)\right|}\end{array}$  . With the notat ma 4,  of the positive deviations and the maximum sum of variances satisfy respectively  b  $b\,\leq\,4M^{2}/k$   ≤  and ˆ  $\hat{v}\,\leq\,16M^{4}\big/k$   ≤ . Thus  

$$
\begin{array}{r l r}{\lefteqn{\mathbb{P}\Big\{\operatorname*{sup}_{h\in\mathcal{H}}\left|\tilde{R}_{t_{n,k}}(h\circ\theta)-R_{t_{n,k}}(h\circ\theta)\right|-\mathbb{E}\left[\operatorname*{sup}_{h\in\mathcal{H}}\left|\tilde{R}_{t_{n,k}}(h\circ\theta)-R_{t_{n,k}}(h\circ\theta)\right|\right]\geq\varepsilon\Big\}}}\\ &{}&{\leq\exp\Big(\frac{-k\varepsilon^{2}}{32M^{4}+8M^{2}\varepsilon/3}\Big).\ \ \ \ \ }\end{array}
$$  

The last step consists in bounding from above the expected deviations in the above display, that is  

$$
\mathbb{E}\operatorname*{sup}_{h\in\mathcal{H}}\Big|\tilde{R}_{t_{n,k}}(h\circ\theta)-R_{t_{n,k}}(h\circ\theta)\Big|.
$$  

Let  be  independent, -valued Rademacher random variables and introduce the Rademacher average    $\varepsilon_{1},...,\varepsilon_{n}$     $n$     $\{0,1\}$  

$$
{\mathcal{R}}_{k}^{\varepsilon}=\operatorname*{sup}_{h\in{\mathcal{H}}}{\frac{1}{k}}\Big|\sum_{i=1}^{n}\varepsilon_{i}(h\circ\theta(X_{i})-Y_{i})^{2}{\mathbb{1}}\{\|X_{i}\|\geq t_{n,k}\}\Big|.
$$  

Following a standard symmetrization argument as  e.g.  in the proof of Lemma 13 in[27], we obtain  

$$
\mathbb{E}\operatorname*{sup}_{h\in\mathcal{H}}\left|\tilde{R}_{t_{n,k}}(h\circ\theta)-R_{t_{n,k}}(h\circ\theta)\right|\leq2\mathbb{E}\left[\mathcal{R}_{k}^{\varepsilon}\right].
$$  

Let   $(X_{1}^{k},Y_{1}^{k}),...,(X_{n}^{k},Y_{n}^{k})$  ) be independent replicates, also independent from the    $X_{i},Y_{i}$  ’s, such that    $\mathcal{L}(X_{i}^{k},Y_{i}^{k})=$   ${\mathcal{L}}{\big(}(X,Y)\,|\,\|X\|\geq t_{n,k}{\big)}$   | ∥ ∥≥ . By Lemma 2.1 of [37], we have  

$$
\sum_{i=1}^{n}\varepsilon_{i}(h\circ\theta(X_{i})-Y_{i})^{2}\mathbb{1}\{\|X_{i}\|\geq t_{n,k}\}\stackrel{d}{=}\sum_{i=1}^{\kappa}\varepsilon_{i}(h\circ\theta(X_{i}^{k})-Y_{i}^{k})^{2},
$$  

where  is independent from the ’s. Then, write    $\mathcal{K}\sim B i n(n,k/n)$     $\varepsilon_{i},X_{i},Y_{i}$  

$$
\mathbb{E}\left[\mathcal{R}_{k}^{\epsilon}\right]=\frac{1}{k}\mathbb{E}\bigg[\mathbb{E}\Big[\operatorname*{sup}_{h\in\mathcal{H}}\big|\sum_{i=1}^{\mathcal{K}}\varepsilon_{i}(h\circ\theta(X_{i}^{k})-Y_{i}^{k})^{2}\big|\,\bigg|\,\mathcal{K}\bigg]\bigg].
$$  

We first control the conditional expectation in the above display for any fixed value . For this    $\mathcal{K}\,=\,m\,\leq\,n$  purpose, we apply Proposition 2.1 of [25] to the class of functions  ${\mathcal{G}}=\{g(x,y)=(h\circ\theta(x)-y)^{2},h\in{\mathcal{H}}\}$  .  

Notice first that for    $g_{i}(x,y)=(h_{i}\circ\theta(x)-y)^{2},i=1,2$   and    $Q$   any probability measure on    $\mathbb{R}^{d}\times\left[-M,M\right]$   we have  

$$
\begin{array}{r l}&{\|g_{1}-g_{2}\|_{L^{2}(Q)}=\,\sqrt{\mathbb{E}_{Q}[(h_{1}\circ\theta(X)-h_{2}\circ\theta(X))(h_{1}\circ\theta(X)+h_{2}\circ\theta(X)-2Y)]^{2}}}\\ &{\qquad\qquad\qquad\leq4M\|h_{1}-h_{2}\|_{L^{2}(Q_{X}\circ\theta^{-1})},}\end{array}
$$  

where    $Q_{X}$   is the marginal distribution of    $Q$   regarding the first component    $X\,\in\,\mathbb{R}^{d}$  . Thus the covering number  ${\mathcal{N}}({\mathcal{G}},L_{2}(Q),\tau)$   for the class    $\mathcal{G}$  , relative to any    $L_{2}(Q)$   radius    $\tau$   is always less than than    $\mathcal{N}(\mathcal{H},L_{2}(\tilde{Q}),\tau/(4M))$  )) for the class  H , where  ${\tilde{Q}}=Q_{X}\circ\theta^{-1}$   ◦ . Now the class  H  has envelope function    $H\,=\,M1_{\mathbb{S}}(\,\cdot\,)$   and has VC-dimension  $V_{\mathcal{H}}<\infty$  , thus Theorem 2.6.7 in [52] yields a control of its covering number,  

$$
\mathcal{N}(\mathcal{H},L_{2}(\tilde{Q}),\tau M)\leq(A/\tau)^{2V_{\mathcal{H}}}
$$  

for some universal constant    $A>0$   not depending on  $\tilde{Q}$   nor    $\mathcal{H}$  . We obtain  

$$
\mathcal{N}(\mathcal{G},L_{2}(Q),\tau)\leq(4A M^{2}/\tau)^{2V_{\mathcal{H}}}.
$$  

Now    $\mathcal{G}$   has envelope function    $G=4M^{2}\mathbb{1}_{\mathbb{R}^{d}\times\mathbb{S}}$  . The previous display writes equivalently  

$$
\mathcal{N}(\mathcal{G},L_{2}(Q),\tau\|G\|_{L^{2}(Q)})\leq(A/\tau)^{2V_{\mathcal{H}}}.
$$  

Inequality (34) is precisely the first step of the proof of Proposition 2.1 in [25] (see Inequality 2.2 in the cited references), so that their upper bound on the Rademacher process applies with VC constant    $v\ =\ 2V_{\mathcal{H}}$  . The of their statement involves    $\sigma^{2}\,=\,\operatorname*{sup}_{g}\mathbb{E}g^{2}\,\leq\,16M^{4}$    and    $U=\mathrm{sup}_{g}\;\|g\|_{\infty}\,\leq\,4M^{2}$  , thus we may take  $\sigma=U=4M^{2}$   =  = 4   .  We obtain  

$$
\mathbb{E}\operatorname*{sup}_{h\in\mathcal{H}}\Big|\sum_{i=1}^{m}\varepsilon_{i}(h\circ\theta(X_{i}^{k})-Y_{i}^{k})^{2}\Big|\leq C^{\prime}(4M^{2}V_{\mathcal{H}}+\,\sqrt{m V_{\mathcal{H}}}),
$$  

for some other universal constant    $C^{\prime}$  . Injecting the latter control into (33) yields, using the concavity of the squared root function and    $\mathbb{E}\left[{\mathcal{K}}\right]=k$  ,  

$$
\begin{array}{r l}&{\mathbb{E}\,[\mathcal{R}_{k}^{\varepsilon}]\leq\frac{1}{k}C^{\prime}(4M^{2}V_{\mathcal{H}}+\mathbb{E}\,[\,\sqrt{\mathcal{K}}]\,\sqrt{V_{\mathcal{H}}})}\\ &{\qquad\qquad\leq\frac{1}{k}C^{\prime}(4M^{2}V_{\mathcal{H}}+\,\sqrt{k}\,\sqrt{V_{\mathcal{H}}}).}\end{array}
$$  

Combining (32) and (35) we obtain  

$$
\mathbb{E}\operatorname*{sup}_{h\in\mathcal{H}}\Big|\tilde{R}_{t_{n,k}}(h\circ\theta)-R_{t_{n,k}}(h\circ\theta)\Big|\leq2\mathbb{E}\,[\mathcal{R}_{k}^{\epsilon}]\leq C\Big(\frac{4M^{2}V_{\mathcal{H}}}{k}+\sqrt{\frac{V_{\mathcal{H}}}{k}}\Big),
$$  

with    $C=2C^{\prime}$  . Finally, combining Equations (30), (31) and (36) yields  

$$
\begin{array}{r l}&{\mathbb{P}\Big\{\underset{h\in\mathcal{H}}{\operatorname*{sup}}\,\Big|\hat{R}_{k}\big(h\circ\Theta\big)-R_{t_{n,k}}\big(h\circ\Theta\big)\Big|\geq\varepsilon+C\Big(\frac{4M^{2}V_{\mathcal{H}}}{k}+\sqrt{\frac{V_{\mathcal{H}}}{k}}\Big)\Big\}}\\ &{\qquad\qquad\qquad\leq3\exp\Big(\frac{-k\varepsilon^{2}}{16\big(8M^{4}+M^{2}\varepsilon/3\big)}\Big),}\end{array}
$$  

which concludes the proof after solving for   $\begin{array}{r}{3\exp\left(\frac{-k\varepsilon^{2}}{16\left(8M^{4}+M^{2}\varepsilon/3\right)}\right)=\delta}\end{array}$  .  

# C.3 Proof of Proposition 2  

1. For    $t\geq1$   and    $h\in{\mathcal{H}}$  , write    $r_{t}(h)=R_{t}(h\circ\theta)$  . For all    $h_{1},h_{2}\in{\mathcal{H}}$  , and    $t\geq1$  , we have  

$$
\begin{array}{r l}&{|r_{t}(h_{1})-r_{t}(h_{2})|=|R_{t}(h_{1}\circ\theta)-R_{t}(h_{2}\circ\theta)|}\\ &{\ =\Bigm\lvert\mathbb{E}\left[h_{1}(X)^{2}-h_{2}(X)^{2}+2Y(h_{1}(X)-h_{2}(X))\mid\lVert X\rVert\geq t\right]\Bigm\rvert}\\ &{\leq\mathbb{E}\big[|(h_{1}(X)+h_{2}(X))(h_{1}(X)-h_{2}(X))|\mid\lVert X\rVert\geq t\big]+2\mathbb{E}\big[\lvert Y(h_{1}(X)-h_{2}(X))\rvert\mid\lVert X\rVert\geq t\big]}\\ &{\leq4M\lVert h_{1}-h_{2}\rVert_{\infty},}\end{array}
$$  

where we have used Assumption 1 to obtain the last inequality. Similarly,  

$$
\begin{array}{r l}&{R_{P_{\infty}}(h_{1}\circ\theta)-R_{P_{\infty}}(h_{2}\circ\theta)}\\ &{\ \leq\mathbb{E}|(h_{1}(\Theta_{\infty})+h_{2}(\Theta_{\infty}))(h_{1}(\Theta_{\infty})-h_{2}(\Theta_{\infty}))|+2\mathbb{E}|Y_{\infty}(h_{1}(\Theta_{\infty})-h_{2}(\Theta_{\infty}))|}\\ &{\ \leq4M\|h_{1}-h_{2}\|_{\infty},}\end{array}
$$  

Let . By to al b  such that . Here    $\varepsilon\,>\,0$   $\exists h_{1},.\,.\,.\,,h_{L}\,\in\,\mathcal{H}$     $\cup_{i=1,...,L}B(h_{i},\varepsilon)\supset\mathcal{H}$     $B(h,\varepsilon)$  the ball of radiu ).  ow because of Assumption  Theorem 1, (i)) we have  $\varepsilon$   $({\mathcal{C}}(\mathbb{S}),\|\cdot\cdot\cdot\|)$  C  ∥· · · ∥  $r_{t}(h_{i})\rightarrow$   →  $R_{P_{\infty}}(h_{i}\circ\theta)$   $t\,\rightarrow\,\infty$  for all fixed  i Thus there exists some  $T\;>\;0$   0 such that for all    $i\;\in\;\{1,.\,.\,.\,,L\}$  . Now for any  and , using (37) and (39) there exists  such that  $|r_{t}(h_{i})-R_{P_{\infty}}(h_{i}\circ\theta)|\leq\varepsilon$  |  −  ◦ | ≤  h  ∈H    $t\geq T$     $i\leq L$  ∞  

$$
\operatorname*{max}(|r_{t}(h)-r_{t}(h_{i})|,|R_{P_{\infty}}(h\circ\theta)-R_{P_{\infty}}(h_{i}\circ\theta)|\leq4M\varepsilon,
$$  

so that  

$$
\begin{array}{r l}&{|r_{t}(h)-R_{P_{\infty}}(h\circ\theta)|\leq|r_{t}(h)-r_{t}(h_{i})|+|r_{t}(h_{i})-R_{P_{\infty}}(h_{i}\circ\theta)|+[R_{P_{\infty}}(h_{i}\circ\theta)-R_{P_{\infty}}(h\circ\theta)]}\\ &{\qquad\qquad\qquad\leq8M\varepsilon+\varepsilon.}\end{array}
$$  

Because    $R_{P_{\infty}}(h\circ\theta)=R_{\infty}(h\circ\theta)$   (Theorem 1-(i)), the proof is complete.  

2. The VC-class property of    $\mathcal{H}$   (Assumption 4) ensures that for any probability measure    $Q$   on    $\mathbb{S}$  , and any    $\varepsilon>0$  , the covering number    ${\mathcal{N}}(\varepsilon,\ {\mathcal{H}},\ L_{1}(Q))$   is finite (see  e.g. , [52], Section 2.6.2). Our first step is to build such a prob  $Q$   which dominates both  $\Phi_{\theta,t}$   $\Phi_{\theta}$   that    $\mathbb{E}\left[|h_{1}-h_{2}|(\Theta)\,|\,\|X\|>t\right]$  d  $\mathbb{E}\left[|h_{1}-h_{2}|(\Theta_{\infty})\right]$  |  − | )] are both controlled by  $\begin{array}{r}{\int_{\mathbb{S}}|h_{1}-h_{2}|\,\mathrm{d}Q=\|h_{1}-h_{2}\|_{L_{1}(Q)}}\end{array}$    |  − | ∥ . Let  $\begin{array}{r}{Q=\frac{1}{2}\big(\Phi_{\theta,1}+\Phi_{\theta}\big)}\end{array}$  ). Then ∞ Φ  is absolutely continuous with respect to , and so is each 1, in view of the discussion above the θ  Q  $\phi_{t},t\geq1$   ≥ In addition we have   $\begin{array}{r}{\operatorname*{sup}_{\omega\in\mathbb{S}}|\,\mathrm{d}\Phi_{\theta}/\,\mathrm{d}Q(\omega)|\,\le\,2}\end{array}$   and from Condition 2. also .  $\begin{array}{r}{\operatorname*{sup}_{\omega\in\mathbb{S},t\geq1}\left|\,\mathrm{d}\Phi_{\theta,t}/\,\mathrm{d}Q(\omega)\right|\leq2D}\end{array}$   | ∈ ≥  

For any  in , following the argument leading to (37) we obtain    $h_{1},h_{2}$     $\mathcal{H}$  

$$
\left|r_{t}(h_{1})-r_{t}(h_{2})\right|\leq4M\int_{\mathbb{S}}\left|h_{1}-h_{2}\right|\,\mathrm{d}\Phi_{t}\leq8M D\int_{\mathbb{S}}\left|h_{1}-h_{2}\right|\,\mathrm{d}Q=8M D\left\|h_{1}-h_{2}\right\|_{L^{1}(Q)}.
$$  

Also,  

$$
\begin{array}{r l}&{\quad_{P_{\infty}}\bigl(h_{1}\circ\theta\bigr)-R_{P_{\infty}}(h_{2}\circ\theta)\bigr|\leq\mathbb{E}\bigl|\bigl(h_{1}g(\Theta_{\infty})+h_{2}(\Theta_{\infty})\bigr)\bigl(h_{1}(\Theta_{\infty})-h_{2}(\Theta_{\infty})\bigr)\bigr|+2\mathbb{E}\bigl|Y_{\infty}\bigl(h_{1}(\Theta_{\infty})-h_{2}(\Theta_{\infty})\bigr)\bigr|}\\ &{\qquad\qquad\qquad\leq4M\mathbb{E}\left[|h_{1}-h_{2}|(\Theta_{\infty})\right]}\\ &{\qquad\qquad\qquad\leq8M\|h_{1}-h_{2}\|_{L_{1}(Q)}.}\end{array}
$$  

Let    $\varepsilon>0$  . Since the covering number of the class    $\mathcal{H}$   for the    $L_{1}(Q)$  -norm is finite, for some  $L\leq\mathcal{N}(\varepsilon,\;\mathcal{H},\;L_{1}(Q))$  there exists    $h_{1}$  ,   ,   $h_{L}\in{\mathcal{H}}$   such that each    $h\in{\mathcal{H}}$   is at    $L_{1}(Q)$  -distance at most    $\varepsilon$   from one of the    $h_{i}$  ’s. The  $\cdot\cdot\cdot$  rest of the proof follows the same lines as the argument following (39), up to replacing the infinity norm with the    $L_{1}(Q)$  -norm on    $\mathcal{H}$  .  

# References  

[1] Mastane Achab, St´ ephan Cl´ emen¸ con, Aur´ elien Garivier, Anne Sabourin, and Claire Vernade. Max K-Armed Bandit: On the ExtremeHunter Algorithm and Beyond. Machine Learning and Knowledge Discovery in Databases ECML PKDD 2017 , pages 389–404, 2017.

 [2] Anass Aghbalou, Patrice Bertail, Fran¸ cois Portier, and Anne Sabourin. Cross validation for extreme value analysis. arXiv:2202.00488, 2023.

 [3] Anass Aghbalou, Fran¸ cois Portier, Anne Sabourin, and Chen Zhou. Tail inverse regression: Dimension reduc- tion for prediction of extremes.  Bernoulli , 30(1):503–533, 2024.

 [4] Andr´ e Altmann, Laura Tolo¸ si, Oliver Sander, and Thomas Lengauer. Permutation importance: a corrected feature importance measure.  Bioinformatics , 26(10):1340–1347, 2010.

 [5] Jan Beirlant, Yuri Goegebeur, Johan Segers, and Jozef L Teugels.  Statistics of extremes: theory and applica- tions . John Wiley & Sons, 2006.

 [6] St´ ephane Boucheron, G´ abor Lugosi, and Pascal Massart.  Concentration Inequalities: A Nonasymptotic Theory of Independence . Oxford University Press, 2013.

 [7] L. Breiman. Random forests.  Machine learning , 45:5–32, 2001.

 [8] Christian Brownlees, Emilien Joly, and G´ abor Lugosi. Empirical risk minimization for heavy-tailed losses.  The Annals of Statistics , 43(6):2507–2536, 2015.

 [9] Juan-Juan Cai, John H.J. Einmahl, and Laurens De Haan. Estimation of extreme risk regions under multi- variate regular variation.  The Annals of Statistics , 39(3):1803–1826, 2011.

 [10] Alexandra Carpentier and Michal Valko. Extreme bandits. In  Advances in Neural Information Processing Systems 27 , pages 1089–1097. Curran Associates, Inc., 2014.

 [11] Valerie Chavez-Demoulin, Paul Embrechts, and Sylvain Sardy. Extreme-quantile tracking for financial time series.  Journal of Econometrics , 181(1):44–52, 2014.

 [12] Ma¨ el Chiapino, St´ ephan Cl´ emen¸ con, Vincent Feuillard, and Anne Sabourin. A multivariate extreme value theory approach to anomaly clustering and visualization.  Computational Statistics , 35(2):607–628, 2020.

 [13] Ma¨ el Chiapino, Anne Sabourin, and Johan Segers. Identifying groups of variables with the potential of being large simultaneously.  Extremes , 22:193–222, 2019.

 [14] St´ ephan Cl´ emen¸ con, Hamid Jalalzai, St´ ephane Lhaut, Anne Sabourin, and Johan Segers. Concentration bounds for the empirical angular measure with statistical learning applications.  Bernoulli , 29(4):2797–2827, 2023.

 [15] Daniel Cooley and Emeric Thibaud. Decompositions of dependence for high-dimensional extremes.  Biometrika , 106(3):587–604, 2019.

 [16] A. Daouia, L. Gardes, and S. Girard. On kernel smoothing for extremal quantile regression. Bernoulli , 19:2557–2589, 2013.

 [17] Abdelaati Daouia, Simone A Padoan, Gilles Stupfler, et al. Optimal weighted pooling for inference about the tail index and extreme quantiles.  Bernoulli , 2023.

 [18] L. De Haan and A. Ferreira.  Extreme value theory: an introduction . Springer Science & Business Media, 2007.

 [19] Laurens De Haan and Sidney I. Resnick. On regular variation of probability densities.  Stochastic processes and their applications , 25:83–93, 1987.

 [20] Holger Drees and Anne Sabourin. Principal component analysis for multivariate extremes.  Electronic Journal of Statistics , 15:908–943, 2021.

 [21] J. H. J. Einmahl and J. Segers. Maximum empirical likelihood estimation of the spectral measure of an extreme-value distribution.  Ann. Stat. , 37:2953–2989, 2009.  

[22] J. HJ Einmahl, L. de Haan, and V. I Piterbarg. Nonparametric estimation of the spectral measure of an extreme value distribution.  Ann. Stat. , 29:1401–1423, 2001.

 [23] Jonathan El Methni, Laurent Gardes, St´ ephane Girard, and Armelle Guillou. Estimation of extreme quantiles from heavy and light tailed distributions.  Journal of Statistical Planning and Inference , 142(10):2735–2747, 2012.

 [24] Sebastian Engelke and Adrien S Hitz. Graphical models for extremes.  Journal of the Royal Statistical Society Series B: Statistical Methodology , 82(4):871–932, 2020.

 [25] Evarist Gin´ e and Armelle Guillou. On consistency of kernel density estimators for randomly censored data: rates holding uniformly over adaptive intervals.  Annales de l’IHP Probabilit´ es et statistiques , 37(4):503–522, 2001.

 [26] Nicola Gnecco, Edossa Merga Terefe, and Sebastian Engelke. Extremal random forests. arxiv:201.12865, 2022.

 [27] Nicolas Goix, Anne Sabourin, and Stephan Cl´ emen¸ con. Learning the dependence structure of rare events: a non-asymptotic study.  Conference on Learning Theory , pages 843–860, 2015.

 [28] Nicolas Goix, Anne Sabourin, and Stephan Cl´ emen¸ con. Sparse representation of multivariate extremes with applications to anomaly ranking.  Artificial Intelligence and Statistics , pages 75–83, 2016.

 [29] Nicolas Goix, Anne Sabourin, and Stephan Cl´ emen¸ con. Sparse representation of multivariate extremes with applications to anomaly detection.  Journal of Multivariate Analysis , 161:12–31, 2017.

 [30] Ulrike Gr¨ omping. Variable importance in regression models.  Wiley interdisciplinary reviews: Computational statistics , 7(2):137–152, 2015.

 [31] L´ aszl´ o Gy¨ orfi, Michael Kohler, Adam Krzyzak, and Harro Walk.  A Distribution-Free Theory of Nonparametric Regression . Springer, 2002.

 [32] Adrien Hitz and Robin Evans. One-component regular variation and graphical modeling of extremes.  Journal of Applied Probability , 53(3):733–746, 2016.

 [33] Henrik Hult and Filip Lindskog. Regular variation for measures on metric spaces.  Publications de l’Institut Math´ ematique , 80(94):121–140, 2006.

 [34] Hamid Jalalzai, Stephan Cl´ emen¸ con, and Anne Sabourin. On binary classification in extreme regions. In Advances in Neural Information Processing Systems , pages 3092–3100, 2018.

 [35] Anja Janßen and Phyllis Wan. k-means clustering of extremes.  Electronic Journal of Statistics , 14(1):1211– 1233, 2020.

 [36] Guillaume Lecu´ e and Shahar Mendelson. Learning subgaussian classes : Upper and minimax bounds. arXiv:1305.4825, 2013.

 [37] St´ ephane Lhaut, Anne Sabourin, and Johan Segers. Uniform concentration bounds for frequencies of rare events.  Statistics & Probability Letters , 189:109610, 2022.

 [38] Filip Lindskog, Sidney I Resnick, and Joyjit Roy. Regularly varying measures on metric spaces: Hidden regular variation and hidden jumps.  Probability Surveys , pages 270–314, 2014.

 [39] Gabor Lugosi and Shahar Mendelson. Risk minimization by median-of-means tournaments.  Journal of the European Mathematical Society , 22(3):925–965, 2019.

 [40] Pascal Massart.  Concentration Inequalities and Model Selection . Springer-Verlag, 2007.

 [41] Colin McDiarmid. Concentration.  Probabilistic methods for algorithmic discrete mathematics , pages 195–248, 1998.

 [42] Shahar Mendelson. On aggregation for heavy-tailed classes.  Probability Theory and Related Fields , 168(3- 4):641–674, 2017.  

[43] Nicolas Meyer and Olivier Wintenberger. Sparse regular variation.  Advances in Applied Probability , 53(4):1115– 1148, 2021.

 [44] Nicolas Meyer and Olivier Wintenberger. Multivariate sparse clustering for extremes.  Journal of the American Statistical Association , 0(just-accepted):1–23, 2023.

 [45] Stefano Nembrini, Inke R K¨ onig, and Marvin N Wright. The revival of the gini importance?  Bioinformatics , 34(21):3711–3718, 2018.

 [46] Mesrob I. Ohannessian and Munther A. Dahleh. Rare probability estimation under regularly varying heavy tails.  Conference on Learning Theory , pages 21.1–21.24, 2012.

 [47] Fabian Pedregosa, Gael Varoquaux, Alexandre Gramfort, Vincent Michel, Bertrand Thirion, Olivier Grisel, Mathieu Blondel, Peter Prettenhofer, Ron Weiss, Vincent Dubourg, Jake Vanderplas, Alexandre Passos, David Cournapeau, Matthieu Brucher, Matthieu Perrot, and Edouard Duchesnay. Scikit-learn: Machine learning in Python.  Journal of Machine Learning Research , 12:2825–2830, 2011.

 [48] Sidney Resnick and Laurens de Haan. Second-order regular variation and rates of convergence in extreme-value theory.  The Annals of Probability , 24(1):97 – 124, 1996.

 [49] Sidney I. Resnick.  Extreme values, regular variation and point processes . Springer, 2013.

 [50] Emma S Simpson, Jennifer L Wadsworth, and Jonathan A Tawn. Determining the dependence structure of multivariate extremes.  Biometrika , 107(3):513–532, 2020.

 [51] Alec Stephenson. Simulating multivariate extreme value distributions of logistic type.  Extremes , 6(1):49–59, 2003.

 [52] A. W. van der Vaart and Jon Wellner.  Weak Convergence and Empirical Processes: With Applications to Statistics . Springer Series in Statistics. Springer-Verlag, New York, 1996.

 [53] Jasper Velthoen, Cl´ ement Dombry, Juan-Juan Cai, and Sebastian Engelke. Gradient boosting for extreme quantile regression.  Extremes , 0(0):1–29, 2023.

 [54] Edoardo Vignotto and Sebastian Engelke. Extreme value theory for anomaly detection–the gpd classifier. Extremes , 23(4):501–520, 2020.

 [55] Edoardo Vignotto, Sebastian Engelke, and Jakob Zscheischler. Clustering bivariate dependencies of compound precipitation and wind extremes over great britain and ireland.  Weather and climate extremes , 32:100318, 2021.

 [56] Yaqing Wang, Quanming Yao, James T. Kwok, and Lionel M. Ni. Generalizing from a few examples: A survey on few-shot learning.  ACM Comput. Surv. , 53(3), jun 2020.  