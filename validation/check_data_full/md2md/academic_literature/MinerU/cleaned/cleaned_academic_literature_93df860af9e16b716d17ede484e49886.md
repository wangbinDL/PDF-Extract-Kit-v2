# LIMIT BEHAVIOR OF THE INVARIANT MEASURE FOR LANGEVIN DYNAMICS  

GERARDO BARRERA  

Abstract.  In this manuscript, we consider the Langevin dynamics on    $\mathbb{R}^{d}$    with an overdamped vector ﬁeld and driven by multiplicative Brownian noise of small amplitude    $\sqrt{\epsilon}$  ,  $\epsilon>0$  . Under suitable assumptions on the vector ﬁeld and the diﬀusion coeﬃcient, it is well-known that it possesses a unique invariant probability measure    $\mu^{\epsilon}$  . As    $\epsilon$   tends to zero, we prove that the probability measure    $\epsilon^{d/2}\mu^{\epsilon}(\sqrt{\epsilon}\mathrm{d}x)$   converges in the  $p$  -Wasserstein distance for    $p\ \in\ [1,2]$   to a Gaussian measure with zero-mean vector and non-degenerate covariance matrix which solves a Lyapunov matrix equation. Moreover, the error term is estimated. We emphasize that generically no explicit formula for    $\mu^{\epsilon}$    can be found.  

# 1.  Introduction  

1.1.  The overdamped Langevin dynamics.  Random dynamical systems arise in the modeling of a (re- alistic) physical system subject to noise perturbations from its surrounding environments or from intrinsic uncertainties associated with the system. The Langevin dynamics was introduced by P. Langevin in 1908 in his celebrated article  Sur la th´ eorie du mouvement brownien,  C. R. Acad. Sci. Paris 146, pp. 530–533. It is perhaps one of the most popular models in molecular systems. For details about the history of the Langevin equation, see [31]. For a phenom eno logical treatment, we recommend the monography [7].  

In the last decades, there have been many applications of Markov chain Monte Carlo methods to complex systems in Computer Science and Statistical Physics. Since sampling high-dimensional distributions is typi- cally a diﬃcult task, the use of stochastic equations for sampling has become important in many applications such as artiﬁcial intelligence and Bayesian algorithms. Stochastic algorithms based on Langevin equations have been proposed to simulate and improve the rate of convergence to limiting distributions. For further details we refer to [8], [11], [13], [14], [19], [24], [35] and the references therein.  

Diﬀerential equations subject to small noise perturbations are one of the classic directions of modern mathematical physics. Let    $\epsilon\in(0,1]$  e a parameter that meas e perturbation strength and let   $(B_{t})_{t\geq0}$  be a standard Brownian motion on  $\mathbb{R}^{d}$  . For any (deterministic)  $\boldsymbol{x}\in\mathbb{R}^{d}$   ∈   we consi  the unique strong solution  $(X_{t}^{\epsilon}(x))_{t\geq0}$   of the following stochastic diﬀerential equation (SDE for short) on  $\mathbb{R}^{d}$  

$$
\left\{\begin{array}{l}{\,\mathrm{d}X_{t}^{\epsilon}(x)=-F(X_{t}^{\epsilon}(x))\mathrm{d}t+\sqrt{\epsilon}\sigma(X_{t}^{\epsilon}(x))\mathrm{d}B_{t}\quad\mathrm{~for~any~}\quad t\geq0,}\\ {\ X_{0}^{\epsilon}(x)=x,}\end{array}\right.
$$  

where the vector ﬁeld    $F\,\in\,\mathcal{C}^{2}(\mathbb{R}^{d},\mathbb{R}^{d})$   and the diﬀu on coeﬃcient    $\sigma\,\in\,\mathcal{C}^{2}(\mathbb{R}^{d},\mathbb{R}^{d\times d})$   satisfy the follow g assumptions. We assume that   $0_{d}$   is a ﬁxed point for  F , i.e.,    $F(0_{d})=0_{d}$   and the following hypotheses for  F . Bakry– Emery condition:  there exists a positive constant    $\delta$   such that  

$$
\begin{array}{r}{\langle F(x_{1})-F(x_{2}),x_{1}-x_{2}\rangle\geq\delta\Vert x_{1}-x_{2}\Vert^{2}\quad\mathrm{~for~any~}\quad x_{1},x_{2}\in\mathbb{R}^{d},}\end{array}
$$  

where    $\langle\cdot,\cdot\rangle$  denotes the standard inner product on    $\mathbb{R}^{d}$    and    $\|\cdot\|$  denotes the standard Euclidean norm on    $\mathbb{R}^{d}$  . Exponential growth condition:  there exist positive constants    $c_{0}$   and    $c_{1}$   satisfying  

$$
\|D^{2}F(x)\|\leq c_{0}e^{c_{1}\|x\|^{2}}\quad\mathrm{~for~any~}\quad x\in\mathbb{R}^{d},
$$  

where    $D^{2}F$   denotes the second order derivative of    $F$  . For the diﬀusion coeﬃcient    $\sigma$   we assume the following standard hypotheses.  

Lipschitz continuity:  there exists a positive constant    $\ell$  such that  

$$
\begin{array}{r}{\|\sigma({\boldsymbol x})-\sigma({\boldsymbol x}_{0})\|_{\mathrm{F}}\leq\ell\|{\boldsymbol x}-{\boldsymbol x}_{0}\|\quad\mathrm{~for~all~}\quad{\boldsymbol x},{\boldsymbol x}_{0}\in\mathbb{R}^{d},}\end{array}
$$  

where    $||\cdot||_{\mathrm{F}}$   denotes the Frobenius norm. Ellipticity:  there is a positive constant    $\kappa$   such that  

$$
\begin{array}{r}{\langle\sigma(x_{0})\sigma^{*}(x_{0})x,x\rangle\geq\kappa\|x\|^{2}\quad\mathrm{~for~all~}\quad x,x_{0}\in\mathbb{R}^{d},}\end{array}
$$  

where    $^*$  denotes the transpose operator.  

Hypotheses ( A ) and ( C ) imply the monotone condition (3.14) given in Theorem 3.5, p. 58 in [26], and hence the existence and uniqueness of the unique strong solution of (1. . Along this manuscript, let   $(\Omega,{\mathcal{F}},\mathbb{P})$   E  P be a complete probability space where (1.1) is deﬁned and denote by  the expectation with respect to .  

1.2.  Invariant distribution.  Existence of invariant measures for stochastic processes are an important feature in probability theory and mathematical physics; and typically they are not so easy to describe explicitly. By Theorem 3.3.4, p. 91 in [22], it is not hard to verify that Hypotheses ( A ), (  $\mathbf{C}$  ) and (  $\mathbf{D}$  ) yield the existence and uniqueness of an invariant (absolutely continuous with respect to the Lebesgue measure on    $\mathbb{R}^{d}$  ) probabilit ure    $\mu^{\epsilon}$    for the stochastic dynamics (1.1). If in addit  $F(x)=\nabla V(x)+b(x)$   and  $\sigma(x)=I_{d}$  y  x  $\boldsymbol{x}\in\mathbb{R}^{d}$   ∈ , where    $I_{d}$   is the identity matrix of dimension    $d\times d$  ,  V  $V:\mathbb{R}^{d}\rightarrow\mathbb{R}$    →  is a scalar function and  b  $b:\mathbb{R}^{d}\rightarrow\mathbb{R}^{d}$    →   is a vector ﬁeld which satisﬁes the divergence-free condition  

$$
\sum_{j=1}^{d}\frac{\partial}{\partial x_{j}}\left(b(x)\exp(-(2/\epsilon)V(x))\right)=0\mathrm{\\\\\~for~any~\\\}x=(x_{1},\ldots,x_{d})\in\mathbb{R}^{d},
$$  

one can verify that   $\mathrm{exp}\big({-}\big(2/\epsilon\big)V(x)\big)\mathrm{d}x$   is a stationary measure for the random  namics (1.1). However, it might not be a probability measure. Under some appropriate assumptions on  V  for    $\|x\|\gg1$  , the unique invariant probability measure    $\mu^{\epsilon}$    of (1.1) is of the Gibbs type  

$$
\mu^{\epsilon}(\mathrm{d}x)=\frac{\exp\!\left(-(2/\epsilon)V(x)\right)}{\mathcal{Z}^{\epsilon}}\mathrm{d}x,
$$  

where    $\mathcal{Z}^{\epsilon}$  is the so-called partition function (normalizing constant). See for instance Chapter 2, Convergence of the Langevin process, p. 21-23 in [34]. Using the Laplace Method (Saddle-point Method), asymptotics as  $\epsilon\rightarrow0^{+}$    for the density of    $\mu^{\epsilon}$    can be carried out, see for instance [2] and [18].  

If w the free-divergence condition (1.2) and replace it by the transversal condition    $\langle\nabla V(x),b(x)\rangle=0$  for all  x  $\boldsymbol{x}\in\mathbb{R}^{d}$   ∈ , in [33] for additive noise it is shown a beautiful expansion on    $\epsilon$   for the density of    $\mu^{\epsilon}$  . However, this expansion requires smoothness of the so-called Freidlin–Wentzell quasipotential. The latter is a nontrivial mathematical problem since it is expressed by a variational principle. Using calculus of variations, in [10] it is shown various results about the smoothness of the quasipotential under the assumptions of smoothness, boundedness and ellipticity of the coeﬃcients of (1.1). In Section 5 of [9] it is proved that the asymptotic expansion given in [33] remains valid in  y open set in which the quasipotential is    $\mathcal{C}^{2}$  . For additive noise, and bounded and dissipative vector ﬁeld  F , in [27], by way of Watanabe’s theory and Malliavin calculus, an asymptotic expansion of    $\mu^{\epsilon}$    has been proved. Later, in [28] it is shown that    $\mu^{\epsilon}$    can be expanded in Wentzel– Kramers–Brillouin (W.K.B.) type, as    $\epsilon~\rightarrow~0^{+}$  , in the set in which the quasipotential is of    ${\mathcal{C}}^{\infty}$  -class and each coeﬃcient which appears in the expansion is of    ${\mathcal{C}}^{\infty}$  -class. More recently, in [6], using control theoretic methods, it is proved that    $\mu^{\epsilon}(\mathrm{d}x)\approx\exp\bigl(-V_{*}(x)\bigr/\epsilon\bigr)$  ,    $\epsilon\ll1$  , where    $V_{*}$  is characterized as the optimal cost of a deterministic control problem. Nevertheless, the control problem is not easy to solve explicitly.  

In (1.1) we consider multiplicative noise, and no transverse condition on the vector ﬁeld    $F$   is assumed. Moreover, we do not need that the Gibbs measure (1.3) remains stationary, and no smoothness on    $\mu^{\epsilon}$    and the Freidlin–Wentzell quasipotential are needed. We remark that  generically  it is not possible to compute an explicit formula for    $\mu^{\epsilon}$  .  

1.3.  Informal result.  Our goal is to prove that the probability    $\epsilon^{d/2}\mu^{\epsilon}(\sqrt{\epsilon}\mathrm{d}x)$  ) has a Gaussian shape in the small noise limit. To be more precise, under Hypotheses ( A ), ( B ), ( C ) and (  $\mathbf{D}$  ), it follows that the probability measure  

$$
\epsilon^{d/2}\mu^{\epsilon}(\sqrt{\epsilon}\mathrm{d}x)
$$  

converges in the    $p$  -Wasserstein (  $p\in[1,2]$  ) to a Gaussian    $\mathcal{N}$   distribution with zero-mean vector and covariance  X matrix given by the unique solution  of the Lyapunov matrix equation  

$$
D F(0_{d}){\mathbb X}+{\mathbb X}(D F(0_{d}))^{*}=\sigma(0_{d})(\sigma(0_{d}))^{*}.
$$  

Generically, it is hard to ﬁnd an explicit formula for the solution of the (1.5). Nevertheless, it can be estimated via numerical algorithms, see for instance [4], [32] and the references therein. More precisely, it is shown an asymptotic expansion (in the Wasserstein distance) of    $\mu^{\epsilon}$    as follows  

$$
\frac{\mathcal{I}^{\epsilon}}{\sqrt{\epsilon}}=\mathcal{N}+\mathcal{O}(\sqrt{\epsilon})~~~~\mathrm{for}~~~~\epsilon\rightarrow0^{+},
$$  

where  $\mathcal{I}^{\epsilon}$    denotes a random variable with law    $\mu^{\epsilon}$  

We anticipate that the proof of (1.6) does not rely on explicit computations of the distribution    $\mu^{\epsilon}$  . It is based on the linearization of the nonlinear dynamics around the stationary point   $0_{d}$  . It is not hard to see that the resulting linear process has the target Gaussian as invariant distribution. It is then necessary to control the diﬀerence between this linear process and the nonlinear dynamics. This is done using the so-called synchronous coupling techniques with the help of Hypotheses ( A ), (  $\mathbf{B}$  ) and (  $\mathbf{C}$  ). The proof of (1.6) is  purely dynamic  and it does not require techniques as Malliavin calculus, large deviation theory for SDEs as in [15], smoothness of the quasipotential, smoothness of the density    $\mu^{\epsilon}$  , analysis of the inﬁnitesimal generator or the W.K.B. expansion.  

Quantitative bounds on the rate of convergence of Markov processes to their limiting distribution are an important and widely studied topic, particularly in the context of Markov chains, see for instance [12], [16], [25] and the references therein. We  quantify  in the Wasserstein distance the implicit error term given in (1.6). We point out that the critical regime analyzed in Section 5.1 of [1] implies for additive noise the total variation convergence of (1.4) to a Gaussian distribution. However, it seems hard to obtain bounds for the total variation error term, even under our assumptions on    $F$   and    $\sigma$  .  

1.4.  Wasserstein distance.  Let    $\mathcal{P}$   be the s of probability measures in the measurable space   $\big(\mathbb{R}^{d},\mathcal{B}(\mathbb{R}^{d})\big)$  , where  $\mathcal{B}(\mathbb{R}^{d})$   denotes the Borel    $\sigma$  -algebra of  $\mathbb{R}^{d}$  . For    $p\geq1$   we deﬁne  

$$
\mathcal{P}_{p}:=\left\{\mu\in\mathcal{P}:\int_{\mathbb{R}^{d}}||x||^{p}\mu(\mathrm{d}x)<\infty\right\},
$$  

the space of probability measures with ﬁnite    $p$  -moment. For any    $\mu,\nu\in\mathcal P$   we say that a probability measure  $\pi_{*}$  in the measurable space   $\big(\mathbb{R}^{d}\times\mathbb{R}^{d},\mathcal{B}(\mathbb{R}^{d}\times\mathbb{R}^{d})\big)$   is a  coupling  between    $\mu$   and    $\nu$   if the marginals of    $^\prime/\ell*$  are    $\mu$  and    $\nu$  , that is, for any    $B\in{\mathcal{B}}(\mathbb{R}^{d})$   it follows that    $\pi_{*}(B\times\mathbb{R}^{d})=\mu(B)$   and    $\pi_{*}(\mathbb{R}^{d}\times B)=\nu(B)$  . Let   $\Pi(\mu,\nu)$  be the set of all coupling between    $\mu$   and    $\nu$  . For any    $\mu,\nu\in\mathcal{P}_{p}$  , the Wasserstein distance of order    $p$   between  $\mu$   and    $\nu$  ,    $\mathcal{W}_{p}(\mu,\nu)$  , is deﬁned by  

$$
\mathcal{W}_{p}(\mu,\nu):=\operatorname*{inf}\left\{\left(\int_{\mathbb R^{d}\times\mathbb R^{d}}\|x-y\|^{p}\pi_{*}(\mathrm{d}x,\mathrm{d}y)\right)^{1/p}:\pi_{*}\in\Pi(\mu,\nu)\right\}.
$$  

Let    $X$   and    $Y$   be two random vectors on    $\mathbb{R}^{d}$    d ned o  the probability space   $(\Omega,{\mathcal{F}},\mathbb{P})$   with ﬁnite   -moment.  $p$  The Wasserstein distance of order    $p$   between  X  and  Y  ,    ${\mathfrak{V}}_{p}(X,Y)$  , is deﬁned by    $\mathfrak{W}_{p}(X,Y):=\mathcal{W}_{p}(\mathbb{P}_{X},\mathbb{P}_{Y})$  , where    $\mathbb{P}_{X}$   and    $\mathbb{P}_{Y}$   are the push-forward probability measures    $\mathbb{P}_{X}(B):=\mathbb{P}(X\in B)$   and    $\mathbb{P}_{Y}(B):=\mathbb{P}(Y\in B)$  for any    $B\in{\mathcal{B}}(\mathbb{R}^{d})$  . For short, we write    $\mathcal{W}_{p}(X,Y)$   in place of    ${\mathfrak{V}}_{p}(X,Y)$  . A remarkable property that we use along this manuscript is the following scaling property  

$$
\mathcal{W}_{p}({\mathfrak{c}}X,{\mathfrak{c}}Y)=|{\mathfrak{c}}|\mathcal{W}_{p}(X,Y)\quad{\mathrm{~for~any~}}\quad{\mathfrak{c}}\in\mathbb{R}.
$$  

The Wasserstein distance metrizes the weak convergence in the space of probabilities with ﬁnite    $p$  -moment. It is a fundamental concept in optimal transport theory, probability theory and partial diﬀerential equations.  

The Wasserstein distance is a natural way to compare the law of two random variables    $X$   and    $Y$   (even for degenerate cases), where one variable is derived from the other by a small perturbation. For further details and properties of the Wassertein distance, we refer to the monographies [29] and [34].  

1.5.  Results.  We denote by    $\mathcal{N}(v,\Xi)$   the Gaussian distribution in    $\mathbb{R}^{d}$    with vect  $v$   and posit deﬁnite covariance matrix   $\Xi$  . Let    $I_{d}$   be the identity    $d\times d$  -matrix. Given a matrix  A  $A\in\mathbb{R}^{d\times d}$   ∈ , denote by  A ∗ the transpose matrix of    $A$   and denote by   $\operatorname{Tr}(A)$   the trace of    $A$  .  

The main result of this manuscript is the following.  

Theorem 1.1  (Gaussian    $\mathcal{W}_{2}$  -approximation of the in iant measure    $\mu^{\epsilon}$  ) .  Assume Hypotheses  ( A ) ,  ( B ) , ( C )  and  (  $\mathbf{D}$  )  are valid. Let    $\mathcal{I}^{\epsilon}$    be a random vector on  R  $\mathbb{R}^{d}$    with distribution    $\mu^{\epsilon}$  . Then there exists a positive constant    $K:=K(\delta,\ell,d,c_{0},\sigma(0_{d}))$   such that for any    $\epsilon\in(0,\epsilon_{*})$   with  

$$
\epsilon_{*}=\operatorname*{min}\left\{\frac{\delta}{8c_{1}\|\sigma(0_{d})(\sigma(0_{d}))^{*}\|_{\mathrm{F}}\cdot d^{2}},\frac{\delta}{2\ell^{2}}\right\}
$$  

it follows that  

$$
\mathcal{W}_{2}\left(\frac{\mathcal{I}^{\epsilon}}{\sqrt{\epsilon}},\mathcal{N}\right)\leq K\sqrt{\epsilon},
$$  

where    $\mathcal{N}$   denotes the Gaussian distribution on    $\mathbb{R}^{d}$    with zero-mean vector and covariance matrix    $\Sigma$   which is the unique solution of the Lyapunov matrix equation  

$$
D F(0_{d})\Sigma+\Sigma(D F(0_{d}))^{*}=\sigma(0_{d})(\sigma(0_{d}))^{*}.
$$  

Using the coupling approach, rates of convergence of the time evolution to equilibrium in the Wasserstein distance for Langevin processes are given in [13] for the underdamped dynamics and in [14] for the overdamped dynamics. In [5], linking functional inequalities with the dissipation to ensure a spectral gap, it is shown that the solution of the Fokker–Planck equation converges in Wasserstein distance of order 2 to its equilibrium as the time evolution goes by. However, the authors in [5], [13] and [14] do not study small random perturbations of dynamical systems, and hence, an asymptotic analysis for the invariant measure is not needed there.  

The proof of Theorem 1.1 does not rely on explicit computations of    $\mu^{\epsilon}$    neither on explicit formula of the Wasserstein distance of order 2 between Gaussian distributions. The Itˆ o formula with the help of ( A ) and ( C ) implies that the    $p$  -moments are bounded recursively as a function of moments of order    $p$   and    $p-2$  . Consequently, by an analogous reasoning (but more involved) one can see that the proof of Theorem 1.1 can be adapted for any    $L^{p}$  -Wasserstein distance for any    $p\geq1$  .  

Remark 1.1  (A comment about total variation convergence for additive noise) .  We stress that  (1.8)  does not imply directly any convergence of the corresponding densities. In other words, the following approximation of densities  

$$
\begin{array}{r}{\mu^{\epsilon}(\mathrm{d}x)\approx\epsilon^{-d/2}\mathcal{N}\left(\mathrm{d}x\big/\sqrt{\epsilon}\right)\,\,\,\,\,\,\,\,\,f o r\,\,\,\,\,\,\,\epsilon\ll1.}\end{array}
$$  

cannot be straightforward deduced from  (1.8) . For additive noise, that is,    $\sigma(x)\,=\,I_{d}$   for all    $\boldsymbol{x}\,\in\,\mathbb{R}^{d}$  , us- ing Theorem 5.1,   $p$  . 30 in  [21]  (implicitly the celebrated Cameron–Martin–Girsanov Theorem) it is shown that  (1.10)  is valid, see Proposition 3.7,   $p$  . 1190 in  [3]  for further details. However, no rate of convergence is given there. Multiplicative noise is implicitly discussed in   $p$  . 123 of  [9] .  

Remark 1.2  (A word about the constant    $K$  ) .  The constant    $K$   given in the right-hand side of  (1.8)  can be taken as  

$$
K=\frac{96c_{0}d^{2}\|\sigma(0_{d})(\sigma(0_{d}))^{*}\|_{\mathrm{F}}}{\delta^{2}}+\frac{2\ell C_{0}^{1/2}}{\delta}\ \ \ \ w i t h\ \ \ \ C_{0}=2\mathrm{Tr}\big((\sigma(0_{d}))^{*}\sigma(0_{d})\big).
$$  

We emphasize that the error term    $K\sqrt{\epsilon}$   may not be optimal  

Remark 1.3  (Existence, uniqueness and integral representation for the covariance matrix   $\Sigma$  ) .  By  ( A ) and  ( D ) , Theorem 1,   $p$  . 44  $\mathcal{B}$   of  [23]  implies that  (1.9)  possesses a unique solution. Moreover, Theorem   $\mathcal{B}$  , p. 414 of  [23]  yields the integral representation for its solution  

$$
\Sigma=\int_{0}^{\infty}e^{-D F(0_{d})s}\sigma(0_{d})(\sigma(0_{d}))^{*}e^{-(D F(0_{d}))^{*}s}\mathrm{d}s.
$$  

As a consequence of Theorem 1.1 we have the following corollaries.  

Corlay 1.1 ( $\mathcal{W}_{p}$  convergence for  $p\in[1,2]$ ). Assume Hypotheses (A), (B), (C) and (D) are valid. Let $\mathcal{I}^{\epsilon}$  ,  N ,  K  and    $\epsilon_{*}$  be as in Theorem 1.1. For any    $p\in[1,2]$   it follows that  

$$
\mathcal{W}_{p}\left(\frac{\mathcal{I}^{\epsilon}}{\sqrt{\epsilon}},\mathcal{N}\right)\leq K\sqrt{\epsilon}\:\:\:\:\:\:\:f o r\:\:a l l\:\:\:\:\:\:\epsilon\in(0,\epsilon_{*}).
$$  

Proof.  The proof follows immediately by the H¨ older inequality and (1.8).  

Corollary 1.2  (Concentration) .  Assume Hypotheses  ( A ) ,  ( B ) ,  ( C )  and  ( D )  are valid. Let    $\mathcal{I}^{\epsilon}$    be as in Theorem 1.1. For any    $p\in[1,2]$   and    $\beta<1/2$   it follows that  

$$
\operatorname*{lim}_{\epsilon\to0^{+}}\frac{1}{\epsilon^{\beta}}\mathcal{W}_{p}(\mathcal{I}^{\epsilon},0_{d})=0.
$$  

Proof.  The proof follows by the triangle inequality for    $\mathcal{W}_{p}$  , Property (1.7) and Theorem 1.1.  

The study of the concentration of the equilibrium measure has been of considerable interest to physicists.   Theorem 1 in [6] implies that    ${\mathcal T}^{\epsilon}\,\rightarrow\,0_{d}$   as    $\epsilon\,\rightarrow\,0^{+}$  in distribution sense. However, it does not say any- thing about its rate of convergence as Corollary 1.2. Results about quantitative concentration of stationary measures on attractors and repellers for multiplicative noise are given in [17] and [20].  

The rest of the manuscript is organized as follows. Section 2 describes the outline of the proof for the main Theorem 1.1. Section 3 is devoted to the proofs of the results skipped in Section 2. Finally, in the Appendix A we provide polynomials and exponential moments estimates for the Ornstein–Uhlenbeck process that we use in Section 3.  

# 2.  Outline of the proof  

2.1.  Linear diﬀusion approximation.  Due to the dissipativity condition (  $\mathbf{A}$  ), the nonlinear random dy- namics   $(X_{t}^{\epsilon}(x))_{t\geq0}$   is pushed-back to the origin with high probability. In a neighbourhood of the origin, it ≥ is reasonable that an Ornstein–Uhlenbeck process helps us to understand   $(X_{t}^{\epsilon}(x))_{t\geq0}$   for large times. Let ≥  $(Y_{t}(x))_{t\geq0}$   be the unique strong solution of the following linear SDE  

$$
\left\{\begin{array}{l}{\,\mathrm{d}Y_{t}^{\epsilon}(x)=-D F(0_{d})Y_{t}^{\epsilon}(x)\mathrm{d}t+\sqrt{\epsilon}\sigma(0_{d})\mathrm{d}B_{t}\quad\mathrm{~for~any~}\quad t\ge0,}\\ {\;Y_{0}^{\epsilon}(x)=x,}\end{array}\right.
$$  

where   $(B_{t})_{t\geq0}$   is a standard Brownian motion on    $\mathbb{R}^{d}$    and    $D F(0_{d})$   denotes the Jacobian matrix at the point  $0_{d}$  . The method of variation of parameters yields  

$$
Y_{t}^{\epsilon}(x)=e^{-D F(0_{d})t}x+\sqrt{\epsilon}\,e^{-D F(0_{d})t}\int_{0}^{t}e^{D F(0_{d})s}\sigma(0_{d}){\mathrm{d}}B_{s}\quad\mathrm{~for~any~}\quad t\geq0.
$$  

Formula (2.2) implies that for any    $t>0$  ,    $Y_{t}^{\epsilon}(x)$  ) possesses Gaussian distribution with vector mean    $m_{t}(x):=$   $e^{-D F(0_{d})t}x$   and covariance matrix   $\Sigma_{t}^{\epsilon}:=\;\epsilon\Sigma_{t}$   for any    $t~\geq~0$  , where   $(\Sigma_{t})_{t\geq0}$   solves the following matrix diﬀerential equation  

$$
\left\{\begin{array}{r}{\frac{\mathrm{d}}{\mathrm{d}t}\Sigma_{t}=-D F(0_{d})\Sigma_{t}-\Sigma_{t}(D F(0_{d}))^{*}+\sigma(0_{d})(\sigma(0_{d}))^{*}\quad\mathrm{~for~any~}\quad t\geq0,}\\ {\Sigma_{0}=0_{d\times d},}\end{array}\right.
$$  

where   $0_{d\times d}$   is the    $d$  -squared zero matrix. We refer to Section 3.7 in [30] for further details. By ( A ) one can easily see that the eigenvalues of    $D F(0_{d})$   are contained in the set    $\{z\in\mathbb{C}:\Re(z)\geq\delta\}$  . As a consequence, we have  

$$
\|m_{t}(x)\|\leq e^{-\delta t}\|x\|\to0\quad{\mathrm{~as~}}\quad t\to\infty.
$$  

If in addition, we assume that    $\sigma(0_{d})$   is invertible, Lemma A.2 in Appendix A implies  

$$
\Vert\Sigma_{t}-\Sigma\Vert_{\mathrm{F}}\leq\Vert\Sigma\Vert_{\mathrm{F}}^{2}\,e^{-2\delta t}\to0\quad\mathrm{~as~}\quad t\to\infty,
$$  

where   $\Sigma$   is the unique solution of the matrix Lyapunov equation (1.9). Therefore, the limiting distribution of    $Y_{t}^{\epsilon}(x)$  ) is a Gaussian law with zero-mean vector and positive deﬁnite covariance matrix    $\epsilon\Sigma$  . Moreover, Proposition 3.5 in [30] implies that    $\mathcal{N}(0_{d},\epsilon\Sigma)$   is the unique invariant probability measure for the dynamics given by (2.1).  

2.2 isintegration.  For short we write    $\mathcal{N}$   in a place of    $\mathcal{N}(0_{d},\Sigma)$  . Recall that    $\mathcal{I}^{\epsilon}$    denotes a random vector on  $\mathbb{R}^{d}$    with distribution    $\mu^{\epsilon}$  . Let    $t\geq0$   and    $\boldsymbol{x}_{0}\in\mathbb{R}^{d}$  . The triangle inequality for the distance    $\mathcal{W}_{2}$   yields  

$$
\begin{array}{r}{\mathcal{W}_{2}\left(\mathcal{I}^{\epsilon},\sqrt{\epsilon}\mathcal{N}\right)\leq\mathcal{W}_{2}\left(\mathcal{I}^{\epsilon},X_{t}^{\epsilon}(x_{0})\right)+\mathcal{W}_{2}\left(X_{t}^{\epsilon}(x_{0}),Y_{t}^{\epsilon}(x_{0})\right)+\mathcal{W}_{2}\left(Y_{t}^{\epsilon}(x_{0}),\sqrt{\epsilon}\mathcal{N}\right).}\end{array}
$$  

Since    $\mu^{\epsilon}$  is invariant for the dynamics (1.1), for any    $t\geq0$  ,    $X_{t}^{\epsilon}(\mathcal{I}^{\epsilon})$  J ) has distribution    $\mu^{\epsilon}$  . By disintegration, the ﬁrst-term of the right-hand side of (2.4) can be estimated as follows  

$$
\mathcal{W}_{2}\left(\mathcal{I}^{\epsilon},X_{t}^{\epsilon}(x_{0})\right)\leq\int_{\mathbb{R}^{d}}\mathcal{W}_{2}\left(X_{t}^{\epsilon}(x),X_{t}^{\epsilon}(x_{0})\right)\mu^{\epsilon}(\mathrm{d}x).
$$  

Analogously,  

$$
\mathcal{W}_{2}\left(\sqrt{\epsilon}\mathcal{N},Y_{t}^{\epsilon}(x_{0})\right)\leq\int_{\mathbb{R}^{d}}\mathcal{W}_{2}\left(Y_{t}^{\epsilon}(x),Y_{t}^{\epsilon}(x_{0})\right)\mathcal{N}(0_{d},\epsilon\Sigma)(\mathrm{d}x),
$$  

where    $\mathcal{N}(0_{d},\epsilon\Sigma)(\mathrm{d}x)$   denotes the density of    $\sqrt{\epsilon}\mathcal{N}$  . Combining (2.4), (2.5) and (2.6) we obtain  

$$
\begin{array}{r l r}{\lefteqn{\mathcal{W}_{2}\left(\mathcal{I}^{\epsilon},\sqrt{\epsilon}\mathcal{N}\right)\leq\int_{\mathbb{R}^{d}}\mathcal{W}_{2}\left(X_{t}^{\epsilon}(x),X_{t}^{\epsilon}(x_{0})\right)\mu^{\epsilon}(\mathrm{d}x)+\mathcal{W}_{2}\left(X_{t}^{\epsilon}(x_{0}),Y_{t}^{\epsilon}(x_{0})\right)}}\\ &{}&{+\int_{\mathbb{R}^{d}}\mathcal{W}_{2}\left(Y_{t}^{\epsilon}(x),Y_{t}^{\epsilon}(x_{0})\right)\mathcal{N}(0_{d},\epsilon\Sigma)(\mathrm{d}x)\,}\end{array}
$$  

for any    $t\geq0$   and    $\boldsymbol{x}_{0}\in\mathbb{R}^{d}$  . In particular, for any    $t\geq0$   we have  

$$
\begin{array}{r l r}{\lefteqn{\mathcal{W}_{2}\left(\mathcal{I}^{\epsilon},\sqrt{\epsilon}\mathcal{N}\right)\leq\int_{\mathbb{R}^{d}}\mathcal{W}_{2}\left(X_{t}^{\epsilon}(x),X_{t}^{\epsilon}(0_{d})\right)\mu^{\epsilon}(\mathrm{d}x)+\mathcal{W}_{2}\left(X_{t}^{\epsilon}(0_{d}),Y_{t}^{\epsilon}(0_{d})\right)}}\\ &{}&{+\int_{\mathbb{R}^{d}}\mathcal{W}_{2}\left(Y_{t}^{\epsilon}(x),Y_{t}^{\epsilon}(0_{d})\right)\mathcal{N}(0_{d},\epsilon\Sigma)(\mathrm{d}x).}\end{array}
$$  

In what follows, we provide the tools for estimating the right-hand side of (2.7). The following lemma allows us to couple two solutions of (1.1) starting in diﬀerent initial conditions.  

Lemma 2.1  (Synchronous coupling I) .  Assume Hypotheses  ( A )  and  ( C )  are valid. Let    $\boldsymbol{x},\boldsymbol{x}_{0}\in\mathbb{R}^{d}$  . Then  

$$
\mathcal{W}_{2}\left(X_{t}^{\epsilon}(x),X_{t}^{\epsilon}(x_{0})\right)\leq e^{-(\delta/2)t}\|x-x_{0}\|\quad\mathrm{~for~all~}\quad t\geq0,\,\epsilon\in(0,\delta/\ell^{2}],
$$  

where    $\delta\,>\,0$   is the dissipativity constant that appears in  ( A )  and    $\ell$  is the Lipschitz constant that appears in  ( C ) . In particular,  

$$
\begin{array}{r}{\mathscr{W}_{2}\left(X_{t}^{\epsilon}(x),X_{t}^{\epsilon}(0_{d})\right)\leq e^{-(\delta/2)t}\|x\|\quad\mathrm{~for~}a l l\quad\mathrm{~}t\geq0,\,\epsilon\in\big(0,\,\delta/\ell^{2}\big].}\end{array}
$$  

The following lemma provides second moment estimates for the marginals of the process (1.1) and also for its invariant probability measure    $\mu^{\epsilon}$  .  

Lemma 2.2  (Second moment estimates) .  Assume Hypotheses  ( A )  and  ( C )  are valid. For any    $\boldsymbol{x}\in\mathbb{R}^{d}$    we have  

$$
\mathbb{E}[\|X_{t}^{\epsilon}(x)\|^{2}]\le\|x\|^{2}e^{-\delta t}+\frac{\epsilon C_{0}}{\delta}\quad\mathrm{~for~}a l l\quad t\ge0,\,\epsilon\in\big(0,\,\delta/(2\ell^{2})\big],
$$  

where    $\delta>0$   is the dissipativity constant that appears in  ( A ) ,    $\ell$  is the Lipschitz constant that appears in  ( C ) and    $C_{0}=2\mathrm{Tr}((\sigma(0_{d}))^{*}\sigma(0_{d}))$  . In addition,  

$$
\int_{\mathbb R^{d}}\|x\|^{2}\mu^{\epsilon}(\mathrm{d}x)\leq\frac{\epsilon C_{0}}{\delta}\ \ \ \ \,f o r\ a l l\ \ \ \ \epsilon\in\big(0,\delta\big/(2\ell^{2})\big].
$$  

The next lemma is crucial in our argument. Due to the contracting nature of the dynamics, the random dynamics around zero,   $(X_{t}^{\epsilon}(0_{d}))_{t\geq0}$  , can be approximated from its linearization   $(Y_{t}^{\epsilon}(0_{d}))_{t\geq0}$  . ≥ ≥  

Lemma 2.3  (Synchronous coupling II) .  Assume Hypotheses  ( A ) ,  ( B ) ,  ( C )  and  ( D )  are valid. Then there exists a positive constant    $C:=C(\delta,\ell,d,c_{0},\sigma(0_{d}))$   such that for any    $\epsilon\in(0,\epsilon_{*})$   with  

$$
\epsilon_{*}:=\operatorname*{min}\left\{\frac{\delta}{8c_{1}\|\sigma(0_{d})(\sigma(0_{d}))^{*}\|_{\mathrm{F}}\cdot d^{2}},\frac{\delta}{2\ell^{2}}\right\},
$$  

and for all    $t\geq0$   we have  

$$
\begin{array}{r}{\mathcal{W}_{2}\left(X_{t}^{\epsilon}(0_{d}),Y_{t}^{\epsilon}(0_{d})\right)\leq C\epsilon,}\end{array}
$$  

where    $\delta\,>\,0$   is the dissipativity constant that appears in  ( A ) ,    $c_{0}$  ,    $c_{1}$   are the positive constants that appear in  (  $\mathbf{B}$  )  and    $\ell$  is the Lipschitz constant that appears in  ( C ) .  

We point out that the constant    $C$   can be taken as  

$$
C=\frac{48c_{0}d^{2}\|\sigma(0_{d})(\sigma(0_{d}))^{*}\|_{\mathrm{F}}}{\delta^{2}}+\frac{\ell C_{0}^{1/2}}{\delta}.
$$  

The latter is deduced from (3.17). Recall that   $\Sigma$   is the solution of (2.3). Since for any    $t\geq0$  ,    $Y_{t}^{\epsilon}(\mathcal{N}(0_{d},\epsilon\Sigma_{t}))$  N has distribution    $\mathcal{N}(0_{d},\epsilon\Sigma)$  , an analogous reasoning used in the proofs of Lemma 2.1 and Lemma 2.2 implies the following lemma.  

Lemma 2.4  (Synchronous coupling III) .  Assume Hypotheses  ( A )  and  ( C )  are valid. For any    $\boldsymbol{x}\,\in\,\mathbb{R}^{d}$    it follows that  

$$
\mathcal{W}_{2}\left(Y_{t}^{\epsilon}(x),Y_{t}^{\epsilon}(0_{d})\right)\leq e^{-(\delta/2)t}\|x\|\quad\mathrm{~for~}a l l\quad\mathrm{~}t\geq0,\,\epsilon\in\left(0,\,\delta/\ell^{2}\right]\!,
$$  

where    $\delta\,>\,0$   is the dissipativity constant that appears in  ( A )  and    $\ell$  is the Lipschitz constant that appears in  ( C ) . In addition, assume that    $\sigma(0_{d})$   is invertible. Then it follows that  

$$
\int_{\mathbb{R}^{d}}\|x\|^{2}\mathcal{N}(0_{d},\epsilon\Sigma)(\mathrm{d}x)\leq\epsilon d\|\Sigma^{1/2}\|_{\mathrm{F}}^{2}.
$$  

For simplicity we assume that    $\sigma(0_{d})$   is invertible in Lemma 2.4. Actually, it is not needed to obtain an estimate such as (2.9). Nevertheless, it is enforced to deﬁne the so-called generalized Gaussian distribution with degenerate covariance matrix and hence the notion of Moore–Penrose pseudoinverse is required. The assumption that    $\sigma(0_{d})$   is invertible can be removed and (2.8) in Lemma 2.4 remains valid replacing    $\mu^{\epsilon}$    by the law of  $\mathcal{N}(0_{d},\epsilon\Sigma)$  .  

In the sequel, we stress the fact that Theorem 1.1 is just a consequence of what we have already stated up to here.  

Theorem 1.1.  By (2.7), Lemma 2.1, Lemma 2.2, Lemma 2.3 and Lemma 2.4 we have  

$$
\mathcal{W}_{2}\left(\mathcal{I}^{\epsilon},\sqrt{\epsilon}\mathcal{N}\right)\leq\sqrt{\frac{\epsilon C_{0}}{\delta}}e^{-(\delta/2)t}+C\epsilon+\sqrt{\epsilon d\|\Sigma^{1/2}\|_{\mathrm{F}}^{2}}e^{-(\delta/2)t}
$$  

for any    $t\geq0$   and    $\epsilon\in(0,\epsilon_{*}]$  . Due to (1.7), (2.10) implies  

$$
\mathcal{W}_{2}\left(\frac{\mathcal{I}^{\epsilon}}{\sqrt{\epsilon}},\mathcal{N}\right)\leq\sqrt{\frac{C_{0}}{\delta}}e^{-(\delta/2)t}+C\sqrt{\epsilon}+\sqrt{d||\Sigma^{1/2}||_{\mathrm{F}}^{2}}e^{-(\delta/2)t}
$$  

for any    $t\geq0$   and    $\epsilon\in(0,\epsilon_{*}]$  . The cunning choice  

$$
t_{\epsilon}=\operatorname*{max}\left\{\frac{1}{\delta}\ln\left(\frac{4C_{0}}{\delta C^{2}\epsilon}\right),\frac{1}{\delta}\ln\left(\frac{4d\|\Sigma^{1/2}\|_{\mathrm{F}}^{2}}{C^{2}\epsilon}\right)\right\}
$$  

yields  

$$
\mathcal{W}_{2}\left(\frac{\mathcal{I}^{\epsilon}}{\sqrt{\epsilon}},\mathcal{N}\right)\leq2C\sqrt{\epsilon},
$$  

which concludes Theorem 1.1.  

# 3.  Proofs  

In this section, we give the proofs of Lemma 2.1, Lemma 2.2 and Lemma 2.3. Along their proofs, we use several times the celebrated Gr¨ onwall inequality. We state it here as a lemma for the sake of completeness.  

Lemma 3.1  (Gr¨ onwall’s inequality) .  Let    $T>0$   be ﬁxed,    ${\mathfrak{g}}:[0,T]\to\mathbb{R}$   be a    $\mathcal{C}^{\perp}$  -function and    ${\mathfrak{h}}:[0,T]\to\mathbb{R}$  be a    $\mathcal{C}^{\mathrm{0}}$  -function. Assume that  

$$
\frac{\mathrm{d}}{\mathrm{d}t}\mathfrak{g}(t)\leq-a\mathfrak{g}(t)+\mathfrak{h}(t)\,\,\,\,\,\,\,\,\,f o r\,\,a n y\,\,\,\,\,\,\,t\in[0,T],
$$  

where    $a\in\mathbb R$  , and the derivative at    $0$   and    $T$   are understood as the right and left derivatives, respectively. Then  

$$
\mathfrak{g}(t)\leq e^{-a t}\mathfrak{g}(0)+e^{-a t}\int_{0}^{t}e^{a s}\mathfrak{h}(s)\mathrm{d}s\quad\mathrm{~for~}a n y\quad\mathrm{~}t\in[0,T].
$$  

3.1.  The synchronous coupl ng I.  For any    $\boldsymbol{x},\boldsymbol{x}_{0}\in\mathbb{R}^{d}$  , let   $(X_{t}^{\epsilon}(x))_{t\geq0}$   and   $(X_{t}^{\epsilon}(x_{0}))_{t\geq0}$   be the solutions ≥ ≥ of (1.1) with initial conditions  x  and    $x_{0}$  , respectively. In the sequel, we consider the so-called synchronous coupling, i.e., both processes   $(X_{t}^{\epsilon}(x))_{t\geq0}$    and   $(X_{t}^{\epsilon}(x_{0}))_{t\geq0}$    have the same driving noise   $(B_{t})_{t\geq0}$  . ≥ ≥  

Lemma 2.1.  By the Itˆ o formula we have  

$$
\begin{array}{r l}&{\mathrm{d}\|X_{t}^{\epsilon}(x)-X_{t}^{\epsilon}(x_{0})\|^{2}=-2\langle X_{t}^{\epsilon}(x)-X_{t}^{\epsilon}(x_{0}),F(X_{t}^{\epsilon}(x))-F(X_{t}^{\epsilon}(x_{0}))\rangle\mathrm{d}t}\\ &{\phantom{x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x}+\epsilon\,\mathrm{Tr}[(\sigma(X_{t}^{\epsilon}(x))-\sigma(X_{t}^{\epsilon}(x_{0})))^{*}(\sigma(X_{t}^{\epsilon}(x))-\sigma(X_{t}^{\epsilon}(x_{0})))]\mathrm{d}t}\\ &{\phantom{x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x}+2\sqrt{\epsilon}\langle X_{t}^{\epsilon}(x)-X_{t}^{\epsilon}(x_{0}),(\sigma(X_{t}^{\epsilon}(x))-\sigma(X_{t}^{\epsilon}(x_{0})))\mathrm{d}B_{t}\rangle.}\end{array}
$$  

By ( C ) we have  

$$
\mathrm{Tr}[(\sigma(X_{t}^{\epsilon}(x))-\sigma(X_{t}^{\epsilon}(x_{0})))^{*}(\sigma(X_{t}^{\epsilon}(x))-\sigma(X_{t}^{\epsilon}(x_{0})))]\leq\ell^{2}\|X_{t}^{\epsilon}(x)-X_{t}^{\epsilon}(x_{0})\|^{2}.
$$  

A localization argument with the help of (  $\mathbf{A}$  ) and (3.1) implies  

$$
\begin{array}{r l}&{\frac{\mathrm{d}}{\mathrm{d}t}\mathbb{E}[\|X_{t}^{\epsilon}(x)-X_{t}^{\epsilon}(x_{0})\|^{2}]\leq-2\delta\mathbb{E}\left[\|X_{t}^{\epsilon}(x)-X_{t}^{\epsilon}(x_{0})\|^{2}\right]+\epsilon\ell^{2}\mathbb{E}\left[\|X_{t}^{\epsilon}(x)-X_{t}^{\epsilon}(x_{0})\|^{2}\right]}\\ &{\qquad\qquad\qquad\qquad\leq-(2\delta-\epsilon\ell^{2})\mathbb{E}\left[\|X_{t}^{\epsilon}(x)-X_{t}^{\epsilon}(x_{0})\|^{2}\right]}\end{array}
$$  

for all    $t\geq0$  . Since    $\mathbb{E}[\|X_{0}^{\epsilon}(x)-X_{0}^{\epsilon}(x_{0})\|^{2}]=\|x-x_{0}\|^{2}$   − ∥  ∥  − ∥ , Lemma 3.1 yields  

$$
\begin{array}{r}{\mathbb{E}[\|X_{t}^{\epsilon}(x)-X_{t}^{\epsilon}(x_{0})\|^{2}]\leq e^{-(2\delta-\epsilon\ell^{2})t}\|x-x_{0}\|^{2}\quad\mathrm{~for~any~}\quad t\geq0.}\end{array}
$$  

Therefore, for any    $\epsilon\in(0,\delta/\ell^{2}]$   we have  

$$
\begin{array}{r}{\mathcal{W}_{2}(X_{t}^{\epsilon}(x),X_{t}^{\epsilon}(x_{0}))\leq e^{-(\delta/2)t}\|x-x_{0}\|\quad\mathrm{~for~any~}\quad x,x_{0}\in\mathbb{R}^{d},\;t\geq0.}\end{array}
$$  

3.2.  Second moment estimates.  For any    $\boldsymbol{x}\;\in\;\mathbb{R}^{d}$  , let   $(X_{t}^{\epsilon}(x))_{t\geq0}$    be the solution of (1.1) with initial ≥ condition    $x$  .  

Lemma 2.2.  In the sequel, we estimate    $\mathbb{E}[\|X_{t}^{\epsilon}(x)\|^{2}]$  ∥ ]. The Itˆ o formula and ( A ) yield  

$$
\begin{array}{r l}&{\mathrm{d}\|X_{t}^{\epsilon}(x)\|^{2}=-2\langle X_{t}^{\epsilon}(x),F(X_{t}^{\epsilon}(x))\rangle\mathrm{d}t+\epsilon\,\mathrm{Tr}[(\sigma(X_{t}^{\epsilon}(x)))^{*}\sigma(X_{t}^{\epsilon}(x))]+M_{t}^{\epsilon}(x)}\\ &{\quad\quad\quad\quad\leq-2\delta\|X_{t}^{\epsilon}(x)\|^{2}\mathrm{d}t+\epsilon\,\mathrm{Tr}[(\sigma(X_{t}^{\epsilon}(x)))^{*}\sigma(X_{t}^{\epsilon}(x))]\mathrm{d}t+M_{t}^{\epsilon}(x),}\end{array}
$$  

√ where    $M_{t}^{\epsilon}(x):=\left\langle2\sqrt{\epsilon}X_{t}^{\epsilon}(x),\mathrm{d}B_{t}\right\rangle$   ⟨ ⟩ for every    $t\geq0$  . Since  

$$
\mathrm{Tr}[(\sigma(X_{t}^{\epsilon}(x)))^{*}\sigma(X_{t}^{\epsilon}(x))]\leq2\mathrm{Tr}[(\sigma(X_{t}^{\epsilon}(x))-\sigma(0_{d}))^{*}(\sigma(X_{t}^{\epsilon}(x))-\sigma(0_{d}))]+2\mathrm{Tr}((\sigma(0_{d}))^{*}\sigma(0_{d}))
$$  

Hypothesis   $(\mathbf{C})$   implies  

$$
\mathrm{Tr}[(\sigma(X_{t}^{\epsilon}(x)))^{*}\sigma(X_{t}^{\epsilon}(x))]\leq2\ell^{2}\|X_{t}^{\epsilon}(x)\|^{2}+C_{0},
$$  

where    $C_{0}:=2\mathrm{Tr}\big((\sigma(0_{d}))^{*}\sigma(0_{d})\big)$  . A localization argument with the help of ( A ) and (3.2) implies  

$$
\frac{\mathrm{d}}{\mathrm{d}t}\mathbb{E}[\|X_{t}^{\epsilon}(x)\|^{2}]\le-(2\delta-2\epsilon\ell^{2})\mathbb{E}[\|X_{t}^{\epsilon}(x)\|^{2}]+\epsilon C_{0}\quad\mathrm{~for~any~}\quad t\ge0.
$$  

Since    $\mathbb{E}[\|X_{0}^{\epsilon}(x)\|^{2}]=\|x\|^{2}$  ∥  ∥ ∥ , for any    $\epsilon\in(0,\delta/(2\ell^{2})]$   Lemma 3.1 yields  

$$
\mathbb{E}[\Vert X_{t}^{\epsilon}(x)\Vert^{2}]\leq e^{-\delta t}\Vert x\Vert^{2}+\frac{\epsilon C_{0}}{\delta}(1-e^{-\delta t})\leq e^{-\delta t}\Vert x\Vert^{2}+\frac{\epsilon C_{0}}{\delta}
$$  

for any    $t\geq0$   and    $\boldsymbol{x}\in\mathbb{R}^{d}$  . Following the same reasoning used on p. 39 in [3], it is not hard to see that (3.3) implies  

$$
\int_{\mathbb{R}^{d}}\|x\|^{2}\mu^{\epsilon}(\mathrm{d}x)\leq\frac{\epsilon C_{0}}{\delta}\quad\mathrm{~for~all~}\quad\epsilon\in(0,\delta/(2\ell^{2})].
$$  

3.3.  The synchronous coupling II.  We consider the solution of (1.1) with initial condition    $x~=~0_{d}$  ,

  $(X_{t}^{\epsilon}(0_{d}))_{t\geq0}$  . Let   $(Y_{t}^{\epsilon}(0_{d}))_{t\geq0}$   be as (2.1). In this section, we use the synchronous coupling between    $X_{t}^{\epsilon}(0_{d})$  ≥ ≥ and    $Y_{t}^{\epsilon}(0_{d})$  ), i.e., both processes   $(X_{t}^{\epsilon}(0_{d}))_{t\geq0}$   and   $(Y_{t}^{\epsilon}(0_{d}))_{t\geq0}$   have the same driving noise   $(B_{t})_{t\geq0}$  . ≥ ≥  

Lemma 2.3.  In the sequel, we estimate    $\mathbb{E}\left[\|X_{t}^{\epsilon}(0_{d})-Y_{t}^{\epsilon}(0_{d})\|^{2}\right]$    . Note that    $X_{0}^{\epsilon}(0_{d})\;=\;Y_{0}^{\epsilon}(0_{d})\;=\;0_{d}$  . Let  $\Delta_{t}^{\epsilon}(0_{d}):=X_{t}^{\epsilon}(0_{d})-Y_{t}^{\epsilon}(0_{d})$   − ),    $t\geq0$  . Then  

$$
\begin{array}{r}{\begin{array}{r l}&{\mathrm{d}\Delta_{t}^{\epsilon}(0_{d})=-\left[F(X_{t}^{\epsilon}(0_{d}))-F(Y_{t}^{\epsilon}(0_{d}))\right]\mathrm{d}t+\left[D F(0_{d})Y_{t}^{\epsilon}(0_{d})-F(Y_{t}^{\epsilon}(0_{d}))\right]\mathrm{d}t}\\ &{\qquad\qquad+\sqrt{\epsilon}(\sigma(X_{t}^{\epsilon}(0_{d}))-\sigma(0_{d}))\mathrm{d}B_{t}.}\end{array}}\end{array}
$$  

Hence, the Itˆ o formula reads  

$$
\begin{array}{r l}&{\mathrm{d}\|\Delta_{t}^{\epsilon}(0_{d})\|^{2}=-2\langle\Delta_{t}^{\epsilon}(0_{d}),F(X_{t}^{\epsilon}(0_{d}))-F(Y_{t}^{\epsilon}(0_{d}))\rangle\mathrm{d}t}\\ &{\quad\quad\quad\quad+2\langle\Delta_{t}^{\epsilon}(0_{d}),D F(0_{d})Y_{t}^{\epsilon}(0_{d})-F(Y_{t}^{\epsilon}(0_{d}))\rangle\mathrm{d}t}\\ &{\quad\quad\quad\quad\quad+\epsilon\operatorname{Tr}[(\sigma(X_{t}^{\epsilon}(0_{d}))-\sigma(0_{d}))^{\ast}(\sigma(X_{t}^{\epsilon}(0_{d}))-\sigma(0_{d}))]\mathrm{d}t}\\ &{\quad\quad\quad\quad\quad+2\sqrt{\epsilon}\langle\Delta_{t}^{\epsilon}(0_{d}),(\sigma(X_{t}^{\epsilon}(0_{d}))-\sigma(0_{d}))\mathrm{d}B_{t}\rangle.}\end{array}
$$  

By ( C ) we have  

$$
\mathrm{Tr}[(\sigma(X_{t}^{\epsilon}(0_{d}))-\sigma(0_{d}))^{*}(\sigma(X_{t}^{\epsilon}(0_{d}))-\sigma(0_{d})]\leq\ell^{2}\|X_{t}^{\epsilon}(0_{d})\|^{2}.
$$  

A localization argument with the help of (  $\mathbf{A}$  ), the Cauchy–Schwarz inequality and (3.4) implies  

$$
\begin{array}{r l}&{\frac{\mathrm{d}}{\mathrm{d}t}\mathbb{E}[\|\Delta_{t}^{\epsilon}(0_{d})\|^{2}]\leq-2\delta\mathbb{E}[\|\Delta_{t}^{\epsilon}(0_{d})\|^{2}]}\\ &{\qquad\qquad\qquad+\,2\mathbb{E}[\|\Delta_{t}^{\epsilon}(0_{d})\|\cdot\|F(Y_{t}^{\epsilon}(0_{d}))-D F(0_{d})Y_{t}^{\epsilon}(0_{d})\|]+\epsilon\ell^{2}\mathbb{E}[\|X_{t}^{\epsilon}(0_{d})\|^{2}].}\end{array}
$$  

Diﬀerential inequality (3.5) and the Young inequality (for    $p=2$  ) yield  

$$
\frac{\mathrm{d}}{\mathrm{d}t}\mathbb{E}[\|\Delta_{t}^{\epsilon}(0_{d})\|^{2}]\leq-\delta\mathbb{E}[\|\Delta_{t}^{\epsilon}(0_{d})\|^{2}]+\frac{1}{\delta}\mathbb{E}[\|F(Y_{t}^{\epsilon}(0_{d}))-D F(0_{d})Y_{t}^{\epsilon}(0_{d})\|^{2}]+\epsilon\ell^{2}\mathbb{E}[\|X_{t}^{\epsilon}(0_{d})\|^{2}]
$$  

By Lemma 2.2 we have  

$$
\mathbb{E}[\|X_{t}^{\epsilon}(0_{d})\|^{2}]\le\frac{\epsilon C_{0}}{\delta}\quad\mathrm{~for~all~}\quad t\ge0,\,\epsilon\in(0,\delta/(2\ell^{2})],
$$  

where    $C_{0}=2\mathrm{Tr}((\sigma(0_{d}))^{*}\sigma(0_{d}))$  . Since   $\Delta_{t}^{\epsilon}(0_{d})=0$  ) = 0, Lemma 3.1 implies  

$$
\begin{array}{l l}{\displaystyle\mathbb{E}[\|\Delta_{t}^{\epsilon}(0_{d})\|^{2}]\leq\frac{1}{\delta}e^{-\delta t}\int_{0}^{t}e^{\delta s}\mathbb{E}[\|F(Y_{s}^{\epsilon}(0_{d}))-D F(0_{d})Y_{s}^{\epsilon}(0_{d})\|^{2}]\mathrm{d}s+\frac{\epsilon^{2}\ell^{2}C_{0}}{\delta^{2}}}\\ {\displaystyle\qquad\leq\frac{1}{\delta^{2}}\operatorname*{sup}_{0\leq s\leq t}\mathbb{E}[\|F(Y_{s}^{\epsilon}(0_{d}))-D F(0_{d})Y_{s}^{\epsilon}(0_{d})\|^{2}]+\frac{\epsilon^{2}\ell^{2}C_{0}}{\delta^{2}}}\end{array}
$$  

for all    $t\geq0$   and    $\epsilon\in(0,\delta/(2\ell^{2})]$  . Next, we estimate  

$$
\operatorname*{sup}_{0\leq s\leq t}\mathbb{E}[\|F(Y_{s}^{\epsilon}(0_{d}))-D F(0_{d})Y_{s}^{\epsilon}(0_{d})\|^{2}].
$$  

Let    $s\in[0,t]$  . Recall that    $F\in\mathcal{C}^{2}(\mathbb{R}^{d},\mathbb{R}^{d})$  . Since    $F(0_{d})=0_{d}$  , The mean value theorem yields  

$$
F(Y_{s}^{\epsilon}(0_{d}))-F(0_{d})=\int_{0}^{1}{\cal D}F(\theta_{1}Y_{s}^{\epsilon}(0_{d}))\mathrm{d}\theta_{1}\cdot Y_{s}^{\epsilon}(0_{d}),
$$  

where    $D F$   denotes the derivative of    $F$  . Since    $F(0_{d})=0_{d}$  , we have  

$$
F(Y_{s}^{\epsilon}(0_{d}))-D F(0_{d})Y_{s}^{\epsilon}(0_{d})=\int_{0}^{1}\left[D F(\theta_{1}Y_{s}^{\epsilon}(0_{d}))-D F(0_{d})\right]\mathrm{d}\theta_{1}\cdot Y_{s}^{\epsilon}(0_{d}).
$$  

Applying The mean value theorem to (3.7) we deduce  

$$
\begin{array}{r}{\|F(Y_{s}^{\epsilon}(0_{d}))-D F(0_{d})Y_{s}^{\epsilon}(0_{d}))\|\le C_{s}^{\epsilon}\|Y_{s}^{\epsilon}(0_{d})\|^{2},}\end{array}
$$  

where  

$$
C_{s}^{\epsilon}:=\int_{0}^{1}\int_{0}^{1}\|D^{2}F(\theta_{1}\theta_{2}Y_{s}^{\epsilon}(0_{d}))\|\mathrm{d}\theta_{1}\mathrm{d}\theta_{2}
$$  

and    $D^{2}F$   denotes the second order derivative of    $F$  . Note that  

$$
Y_{t}^{\epsilon}(0_{d})=\sqrt{\epsilon}\,Y_{t}\quad\mathrm{~for~any~}\quad t\ge0,
$$  

where   $(Y_{t})_{t\geq0}$   is the unique strong solution of  

$$
\left\{\begin{array}{r}{\mathrm{d}Y_{t}=-D F(0_{d})Y_{t}\mathrm{d}t+\sigma(0_{d})\mathrm{d}B_{t}\quad\mathrm{~for~any~}\quad t\geq0,}\\ {Y_{0}=0_{d}.}\end{array}\right.
$$  

By (3.9) and (  $\mathbf{B}$  ) we have  

$$
\|D^{2}F(\theta_{1}\theta_{2}Y_{s}^{\epsilon}(0_{d}))\|=\|D^{2}F(\theta_{1}\theta_{2}\sqrt{\epsilon}Y_{s})\|\le c_{0}e^{c_{1}\theta_{1}^{2}\theta_{2}^{2}\epsilon\|Y_{s}\|^{2}}.
$$  

Since    $\theta_{1},\theta_{2}\in[0,1]$  , we obtain  

$$
\begin{array}{r}{\|D^{2}F(\theta_{1}\theta_{2}Y_{s}^{\epsilon}(0_{d}))\|\le c_{0}e^{c_{1}\epsilon\|Y_{s}\|^{2}}.}\end{array}
$$  

Inequality (3.11) with the help of inequality (3.8) and equality (3.9) yields  

$$
\|F(Y_{s}^{\epsilon}(0_{d}))-D F(0_{d})Y_{s}^{\epsilon}(0_{d})\|^{2}\leq c_{0}^{2}e^{2c_{1}\epsilon\|Y_{s}\|^{2}}\epsilon^{2}\|Y_{s}\|^{4}
$$  

for any    $s\geq0$  , where   $(Y_{t})_{t\geq0}$   is the solution of (3.10). By item i) of Lemma A.1 in Appendix A it follows that  

$$
\mathbb{E}[\|Y_{s}\|^{8}]\le24C_{*}^{4}\quad\mathrm{~for~any~}\quad s\ge0,
$$  

where  

$$
C_{*}=\frac{||\sigma(0_{d})(\sigma(0_{d}))^{*}||_{\mathrm{F}}\cdot d^{2}}{\delta}
$$  

and    $||\cdot||_{\mathrm{F}}$   denotes the Frobenius norm. Due to (  $\mathbf{D}$  ), we note that    $C_{*}>0$  . Moreover, by item ii) Lemma A.1 in Appendix A for    $\begin{array}{r}{\epsilon\in(0,\frac{1}{4c_{1}C_{*}})}\end{array}$  ) we have  

$$
\mathbb{E}[e^{4c_{1}\epsilon\|Y_{s}\|^{2}}]\le\frac{1}{1-4\epsilon c_{1}C_{*}}\mathrm{~\\\~for~any~\\\}s\ge0.
$$  

Estimate (3.12) with the help of the Cauchy–Schwarz inequality, (3.13) and (3.15) implies  

$$
F(Y_{s}^{\epsilon}(0_{d}))-D F(0_{d})Y_{s}^{\epsilon}(0_{d})\|^{2}]\leq\epsilon^{2}c_{0}^{2}\left(\mathbb{E}[e^{4c_{1}\epsilon\|Y_{s}\|^{2}}]\mathbb{E}[\|Y_{s}\|^{8}]\right)^{1/2}\tilde{C}(\delta,d,c_{0})\epsilon^{2}\left(\frac{1}{1-4\epsilon c_{1}C_{*}}\right)^{1/2}
$$  

for any    $s\,\geq\,0$  ,    $\epsilon\,\in\,\big(0,\frac{1}{4c_{1}C_{*}}\big)$  ), where  $\Ddot{C}(\delta,d,c_{0})\,=\,\sqrt{24}c_{0}^{2}C_{*}^{2}$  √ is a positive constant. Consequently, for    $\epsilon\in$  ∗  $(0,\frac{1}{4c_{1}C})$  ) we obtain  

$$
\operatorname*{sup}_{0\leq s\leq t}\mathbb{E}[\|F(Y_{s}^{\epsilon}(0_{d}))-D F(0_{d})Y_{s}^{\epsilon}(0_{d})\|^{2}]\leq\tilde{C}(\delta,d,c_{0})\epsilon^{2}\left(\frac{1}{1-4\epsilon c_{1}C_{*}}\right)^{1/2}.
$$  

Note that if    $\begin{array}{r}{\epsilon\in(0,\frac{1}{8c_{1}C_{*}})}\end{array}$  ), then   $(1-4\epsilon c_{1}C_{*})\geq1\slash2$  . Let    $\begin{array}{r}{\epsilon_{*}:=\operatorname*{min}\left\{\frac{1}{8c_{1}C_{*}},\frac{\delta}{2\ell^{2}}\right\}}\end{array}$   	 . By (3.6) and (3.16) we have for all    $\epsilon\in(0,\epsilon_{*}]$   and all    $t\geq0$  

$$
\mathbb{E}\left[\|X_{t}^{\epsilon}(0_{d})-Y_{t}^{\epsilon}(0_{d})\|^{2}\right]\leq\frac{\sqrt{2}}{\delta^{2}}\tilde{C}(\delta,d,c_{0})\epsilon^{2}+\frac{\epsilon^{2}\ell^{2}C_{0}}{\delta^{2}}.
$$  

As a consequence, for any    $\epsilon\in(0,\epsilon_{*}]$   and    $t\geq0$   we have  

$$
\mathcal{W}_{2}\left(X_{t}^{\epsilon}(0_{d}),Y_{t}^{\epsilon}(0_{d})\right)\leq\frac{\epsilon}{\delta}(\sqrt{2}\tilde{C}(\delta,d,c_{0})+\ell^{2}C_{0})^{1/2}\leq\frac{\epsilon}{\delta}(48c_{0}C_{*}+\ell C_{0}^{1/2}),
$$  

where in the last inequality we use the subadditivity property of the root-map. Inequality (3.17) with the help of (3.14) implies the statement. □  

In this section, we compute the even moments and exponential moments of the Ornstein–Uhlenbeck process starting at zero. Let   $(Z_{t})_{t\ge0}$   be the unique strong solution of the linear SDE  

$$
\left\{\begin{array}{r}{\mathrm{d}Z_{t}=-U Z_{t}\mathrm{d}t+V\mathrm{d}B_{t}\quad\mathrm{~for~any~}\quad t\geq0,}\\ {Z_{0}=0_{d},}\end{array}\right.
$$  

where    $U,V\in\mathbb{R}^{d\times d}$    are given matrices. The drift matrix    $U$   satisﬁes the following condition: there exists a positive  δ  such that  

$$
\langle U x,x\rangle\geq\delta\|x\|^{2}~~~~\mathrm{for~all}~~~~x\in\mathbb{R}^{d}.
$$  

We recall the deﬁnitions and properties of 1-norm    $||\cdot||_{1}$   and the Frobenius norm    $||\cdot||_{\mathrm{F}}$  . For a given matrix  $A=(a^{i,j})_{i,j\in\{1,...,d\}}$   they are given by  

$$
\|A\|_{1}:=\sum_{i,j=1}^{d}|a^{i,j}|\quad{\mathrm{~and~}}\quad\|A\|_{\mathrm{F}}:={\sqrt{\sum_{j=1}^{d}|a^{i,j}|^{2}}}.
$$  

Lemma A.1  (Polynomial and exponential moments) .  Assume that  (A.2)  is valid and let    $(Z_{t})_{t\ge0}$   be the unique strong solution of the   $S D E$   (A.1) . Then the following holds.  

i)  For each    $j\in\mathbb N$   it follows that  

$$
\mathbb{E}[\Vert Z_{t}\Vert^{2j}]\leq C_{*}^{j}j!~~~~f o r~a l l~~~~t\geq0,~~~~w h e r e~~~~C_{*}:=\frac{\Vert V V^{*}\Vert_{\mathrm{F}}\cdot d^{2}}{\delta}.
$$  

ii)  Let    $C_{*}$  be as in item   $i$  ). For any    $\lambda\in(0,1/C_{*})$   and all    $t\geq0$   it follows that  

$$
\mathbb{E}[e^{\lambda\|Z_{t}\|^{2}}]\le\frac{1}{1-\lambda C_{*}}.
$$  

Proof.  We start with the proof of item i). The proof is done by the induction method. We start the induction basis,    $j=1$  . The Itˆ o formula yields  

$$
\mathrm{d}\|Z_{t}\|^{2}=-2\langle Z_{t},U Z_{t}\rangle\mathrm{d}t+\mathrm{Tr}[V^{*}V]\mathrm{d}t+2\langle Z_{t},V\mathrm{d}B_{t}\rangle.
$$  

A localization argument in (A.4) with the help of (A.2) implies  

$$
\frac{\mathrm{d}}{\mathrm{d}t}\mathbb{E}[\|Z_{t}\|^{2}]\le-2\delta\mathbb{E}[\|Z_{t}\|^{2}]+\mathrm{Tr}[V^{*}V].
$$  

Since    $Z_{t}=0_{d}$  , Lemma 3.1 yields  

$$
\mathbb{E}[\|Z_{t}\|^{2}]\le\frac{\mathrm{Tr}[V^{*}V]}{2\delta}\quad\mathrm{~for~all~}\quad t\ge0.
$$  

Note that  

$$
\frac{\mathrm{Tr}[V^{*}V]}{2\delta}\leq\frac{\|V V^{*}\|_{1}}{2\delta}\leq\frac{d\,\|V V^{*}\|_{\mathrm{F}}}{2\delta}\leq\frac{d^{2}\,\|V V^{*}\|_{\mathrm{F}}}{\delta}.
$$  

Combining (A.5) and (A.6) we prove the induction basis.  

We assume that (A.3) holds for    $j=n$   and we prove that it remains valid for    $j=n+1$  . The Itˆ o formula for the function    $f(x)=\|x\|^{2(n+1)}$  ,    $x\in\mathbb{R}$  , reads  

$$
\begin{array}{r l}&{\mathrm{d}\|Z_{t}\|^{2(n+1)}=-2(n+1)\|Z_{t}\|^{2n}\langle Z_{t},U Z_{t}\rangle\mathrm{d}t+(^{1/2})\mathrm{Tr}[V^{*}H(Z_{t})V]\mathrm{d}t}\\ &{\qquad\qquad+\ 2(n+1)\|Z_{t}\|^{2n}\langle Z_{t},V\mathrm{d}B_{t}\rangle,}\end{array}
$$  

where the matrix valued function    $\mathbb{R}^{d}\ni x\mapsto H(x):=(H_{i,j}(x))_{i,j\in\{1,...,d\}}\in\mathbb{R}^{d\times d}$    is given by  

$$
H_{i,j}(x):={\left\{\begin{array}{l l}{4(n+1)n\|x\|^{2(n-1)}x_{i}^{2}+2(n+1)\|x\|^{2n}\quad}&{{\mathrm{~for~}}\quad i=j,}\\ {4(n+1)n\|x\|^{2(n-1)}x_{i}x_{j}}&{{\mathrm{~for~}}\quad i\neq j.}\end{array}\right.}
$$  

By deﬁnition of  $||\cdot||_{1}$   it follows that  

$$
\|H(x)\|_{1}\leq2d(n+1)\|x\|^{2n}+4d(n+1)n\|x\|^{2n}=2d(n+1)(1+2n)\|x\|^{2n}
$$  

for all    $\boldsymbol{x}\in\mathbb{R}^{d}$  . Note that   $\mathrm{Tr}[V^{*}H(Z_{t})V]=\mathrm{Tr}[H(Z_{t})V V^{*}]$  . By (A.8) we obtain  

$$
\begin{array}{r}{|\mathrm{Tr}[H(Z_{t})V V^{*}]|\leq d\|H(Z_{t})\|_{1}\|V V^{*}\|_{\mathrm{F}}\leq2d^{2}(n+1)(1+2n)\|V V^{*}\|_{\mathrm{F}}\|Z_{t}\|^{2n}.}\end{array}
$$  

Using a localization argument in (A.7) with the help of (A.2) and (A.9) yields  

$$
\frac{\mathrm{d}}{\mathrm{d}t}\mathbb{E}[\|Z_{t}\|^{2(n+1)}]\le-2(n+1)\delta\mathbb{E}[\|Z_{t}\|^{2(n+1)}]+d^{2}(n+1)(1+2n)\|V V^{\ast}\|_{\mathrm{F}}\mathbb{E}[\|Z_{t}\|^{2n}].
$$  

By induction hypothesis we have    $\mathbb{E}[\|Z_{t}\|^{2n}]\le C_{*}^{n}n!$  ! for all    $t\geq0$  . Since    $Z_{0}=0_{d}$  , Lemma 3.1 yields for all ∗  $t\geq0$  

$$
\mathbb{E}[\|Z_{t}\|^{2(n+1)}]\le\frac{d^{2}(n+1)(1+2n)\|V V^{*}\|_{\mathrm{F}}C_{*}^{n}\,n!}{2(n+1)\delta}\le C_{*}^{n+1}(n+1)!,
$$  

which ﬁnishes the induction step. This concludes the proof of item i). We continue with the proof of item ii). By the Monotone Convergence Theorem we have  

$$
\mathbb{E}[e^{\lambda\|Z_{t}\|^{2}}]=\sum_{j=0}^{\infty}\frac{\lambda^{j}\mathbb{E}[\|Z_{t}\|^{2j}]}{j!}\quad\mathrm{~for~all~}\quad\lambda\ge0.
$$  

By item i) for all    $\lambda\in(0,1/C_{*})$   and    $t\geq0$   it follows that  

$$
\mathbb{E}[e^{\lambda\|Z_{t}\|^{2}}]\le\sum_{j=0}^{\infty}(\lambda C_{*})^{j}=\frac{1}{1-\lambda C_{*}}.
$$  

Lemma A.2  (Covariance) .  Assume that  (A.2)  holds and that the diﬀusion matrix    $V$   is invertible. Let  $(Z_{t})_{t\ge0}$   be the unique strong solution of the   $S D E$   (A.1)  and let    $\Theta_{t}:=\mathbb{E}[Z_{t}Z_{t}^{\ast}]$   for any    $t\geq0$  . Then  

$$
\Vert\Theta_{t}-\Theta\Vert_{\mathrm{F}}\leq\Vert\Theta\Vert_{\mathrm{F}}^{2}\,e^{-2\delta t}\ \ \ \ \,f o r\ a l l\ \ \ \ t\geq0,
$$  

where    $\Theta\in\mathbb{R}^{d\times d}$    is the unique symmetric and positive deﬁnite solution of the Lyapunov matrix equation  

$$
U\Theta+\Theta U^{*}=V V^{*}.
$$  

Proof.  The proof follows by analogous reasoning used in the proof of Lemma C.4 in Appendix C of [3]. We state it here for completeness of the presentation.  

Hypothesis (A.2) and Theorem 1, p. 443 of [23] yield that (A.10) possesses a unique solution. By Proposition 3.5 in [30] we have  

$$
\left\{\begin{array}{c}{\frac{\mathrm{d}}{\mathrm{d}t}\Theta_{t}=-U\Theta_{t}-\Theta_{t}U^{*}+V V^{*}\quad\mathrm{~for~any~}\quad t\geq0,}\\ {\Theta_{0}=0_{d\times d},}\end{array}\right.
$$  

where   $0_{d\times d}\in\mathbb{R}^{d\times d}$  . Let    $t\geq0$   be ﬁxed. Write    $r_{t}:=\Vert\Theta_{t}-\Theta\Vert_{\mathrm{F}}^{2}$  ,   $\Theta_{t}=(\Theta_{t}^{i,j})_{i,j\in\{1,...,d\}}$  ,   $\Theta=(\Theta^{i,j}\,)_{i,j\in\{1,\dots,d\}}$  ,  $U=(U^{i,j})_{i,j\in\{1,...,d\}}$   and    $V V^{*}=((V V^{*})^{i,j})_{i,j\in\{1,...,d\}}$  . By (A.10) we obtain  

$$
\sum_{k=1}^{d}(U^{i,k}\Theta^{k,j}+\Theta^{i,k}U^{j,k})=(V V^{*})^{i,j}\quad{\mathrm{~for~all~}}\quad i,j\in\{1,\ldots,d\}.
$$  

The diﬀerential equation (A.11) with the help of (A.12) reads  

$$
\frac{\mathrm{d}}{\mathrm{d}t}\Theta_{t}^{i,j}=\sum_{k=1}^{d}(-U^{i,k}\Theta_{t}^{k,j}-\Theta_{t}^{i,k}U^{j,k}+(V V^{*})^{i,j})=-\sum_{k=1}^{d}(U^{i,k}(\Theta_{t}^{k,j}-\Theta^{k,j})+(\Theta_{t}^{i,k}-\Theta^{i,k})U^{j,k}).
$$  

The chain rule and (A.13) imply  

$$
\begin{array}{r l}{\lefteqn{\frac{1}{|t|}r_{t}=2\sum_{i,j=1}^{d}(\Theta_{t}^{i,j}-\Theta^{i,j})\frac{\mathrm{d}}{\mathrm{d}t}(\Theta_{t}^{i,j}-\Theta^{i,j})}}\\ &{=-2\sum_{i,j=1}^{d}(\Theta_{t}^{i,j}-\Theta^{i,j})\sum_{k=1}^{d}(U^{i,k}(\Theta_{t}^{k,j}-\Theta^{k,j})+(\Theta_{t}^{i,k}-\Theta^{i,k})U^{j,k})}\\ &{=-2\sum_{j=1}^{d}\sum_{i,k=1}^{d}(\Theta_{t}^{i,j}-\Theta^{i,j})U^{i,k}(\Theta_{t}^{k,j}-\Theta^{k,j})-2\sum_{i=1}^{d}\sum_{j,k=1}^{d}(\Theta_{t}^{i,j}-\Theta^{i,j})U^{j,k}(\Theta_{t}^{i,k}-\Theta^{i,k}),}\end{array}
$$  

where in the last equality we rearrange the sums. By (A.2) we deduce the following diﬀerential inequality  

$$
\frac{\mathrm{d}}{\mathrm{d}t}r_{t}\leq-4\delta\sum_{i,j=1}^{d}(\Theta_{t}^{i,j}-\Theta^{i,j})^{2}=-4\delta r_{t}\quad\mathrm{~for~all~}\quad t\geq0.
$$  

Lemma 3.1 yields    $r_{t}\leq r_{0}e^{-4\delta t}$    for all    $t\geq0$   and consequently the statement.  

# Acknowledgements  

The research of G. Barrera has been supported by the Academy of Finland via the Matter and Materials Proﬁ4 university proﬁling action. He gratefully acknowledges support from a post-doctorate grant (2020-2023) held at the Department of Mathematical and Statistical Sciences at University of Helsinki and expresses his gratitude for all the facilities used along with the realization of this work. The author is grateful to the reviewers for the thorough examination of the manuscript, which has lead to a signiﬁcant improvement.  

# References  

[1] Arapostathis, A., Biswas, A. and Borkar, V.:  Controlled equilibrium selection in stochastically perturbed dynamics,  Ann. Probab. 46-5 (2018), pp. 2749–2799.

 [2] Athreya, K. and Hwang, C.:  Gibbs measures asymptotics,  Sankhy¯ a Ser. A 72-A-1 (2018), pp. 191–207.

 [3] Barrera, G. and Jara, M.:  Thermalisation for small random perturbations of dynamical systems,  Ann. Appl. Probab. 30-3 (2020), pp. 1164–1208.

 [4] Benner, P., Li, J. and Penzl, T.:  Numerical solution of large-scale Lyapunov equations, Riccati equations, and linear- quadratic optimal control problems,  Numer. Linear Algebra Appl. 15-9 (2008), pp. 755–777.

 [5] Bolley, F., Gentil, I. and Guillin, A.:  Convergence to equilibrium in Wasserstein distance for Fokker–Planck equations,  J. Funct. Anal. 263-8 (2012), pp. 2430–2457.

 [6] Biswas, A. and Borkar, V.:  Small noise asymptotics for invariant densities for a class of diﬀusions: a control theoretic view,  J. Math. Anal. Appl. 360-2 (2009), pp. 476–484.

 [7] Coﬀey, W. and Kalmykov, Y.:  The Langevin equation: with applications in physics, chemistry and electrical engineering, Third edition. World Scientiﬁc Series in Contemporary Chemical Physics: Volume 27 (2012).

 [8] Dalalyan, A.:  Theoretical guarantees for approximate sampling from smooth and log-concave densities,  J. R. Stat. Soc. Ser. B. Stat. Methodol. 79-3 (2017), pp. 651–676.

 [9] Day, M.:  Recent progress on the small parameter exit problem,  Stochastics 20-2 (1987), pp. 121–150.

 [10] Day, M. and Darden, T.:  Some regularity results on the Ventcel–Freidlin quasi-potential function,  Appl. Math. Opt. 13-3 (1985), pp. 259–282.

 [11] Duncan, A., N¨ usken, N. and Pavliotis, G.:  Using perturbed underdamped Langevin dynamics to eﬃciently sample from probability distributions,  J. Stat. Phys. 169-6 (2017), pp. 1098–1131.

 [12] Durmus, A. and Moulines,  E.:  Quantitative bounds of convergence for geometrically ergodic Markov chain in the Wasser- stein distance with application to the Metropolis adjusted Langevin algorithm,  Stat. Comput. 25-1 (2015), pp. 5–19.

 [13] Eberle, A., Guillin, A. and Zimmer, R.:  Couplings and quantitative contraction rates for Langevin dynamics,  Ann. Probab. 47-4 (2019), pp. 1982–2010.

 [14] Eberle, A., Guillin, A. and Zimmer, R.:  Quantitative Harris-type theorems for diﬀusions and McKean–Vlasov processes, Trans. Amer. Math. Soc. 371-10 (2019), pp. 7135–7173.

 [15] Freidlin, M. and Wentzell, A.:  Random perturbations of dynamical systems,  Third edition. Springer Heidelberg (2012).

 [16] Gareth, R. and Rosenthal, J.:  Hitting time and convergence rate bounds for symmetric Langevin diﬀusions,  Methodol. Comput. Appl. Probab. 21-3 (2019), pp. 921–929.

 [17] Huang, W., Ji, M., Liu, Z. and Yingfei, Y.:  Concentration and limit behaviors of stationary measures,  Phys. D 369 (2018), pp. 1–17.  

[18] Hwang, C.:  Laplace’s method revisited: weak convergence of probability measures,  Ann. Probab. 8-6 (1980), pp. 1177–1182.

 [19] Hwang, C., Hwang-Ma, S. and Sheu, S.:  Accelerating Gaussian diﬀusions,  Ann. Appl. Probab. 3-3 (1993), pp. 897–913.

 [20] Ji, M., Zhongwei, S. and Yingfei, Y.:  Quantitative concentration of stationary measures,  Phys. D 399 (2019), pp. 73–85.

 [21] Kabanov, Y., Liptser, R. and Shiryaev, A.:  On the variation distance for probability measures deﬁned on a ﬁltered space, Probab. Theory Relat. Fields 71-1 (1986), pp. 19–35.

 [22] Kulik, A.:  Ergodic behavior of Markov processes with applications to limit theorems,  De Gruyter Studies in Mathematics 67  (2018).

 [23] Lancaster, P. and Tismenetsky, M.:  The theory of matrices,  Second edition. Computer Science and Applied Mathematics. Academic Press, Inc. (1985).

 [24] Leli\` evre, T., Nier, F. and Pavliotis, G.:  Optimal non-reversible linear drift for the convergence to equilibrium of a diﬀusion, J. Stat. Phys. 152-2 (2013), pp. 237–274.

 [25] Madras, N. and Sezer, D.:  Quantitative bounds for Markov chain convergence: Wasserstein and total variation distances, Bernoulli 16-3 (2010), pp. 882–908.

 [26] Mao, X.:  Stochastic diﬀerential equations and applications,  Second edition. Horwood Publishing Limited, Chichester (2008).

 [27] Mikami, T.:  Asymptotic expansions of the invariant density of a Markov process with a small parameter,  Ann. Inst. H. Poincar´ e Probab. Statist. 24-3 (1988), pp. 403–424.

 [28] Mikami, T.:  Asymptotic analysis of invariant density of randomly perturbed dynamical systems,  Ann. Probab. 18-2 (1990), pp. 524–536.

 [29] Panaretos, V. and Zemel, Y.:  An invitation to statistics in Wasserstein space,  Springer Briefs in Probability and Mathe- matical Statistics (2020).

 [30] Pavliotis, G.:  Stochastic processes and applications diﬀusion processes, the Fokker–Planck and Langevin equations,  Texts in Applied Mathematics. Springer-Verlag New York (2014).

 [31] Pomeau, Y. and Piasecki, J.:  The Langevin equation,  C. R. Phys. 18 9-10 (2017), pp. 570–582.

 [32] Scottedward, A., Tenison, B. and Poolla, K.:  Numerical solution of the Lyapunov equation by approximate power iteration, Linear Algebra Appl. 236-8 (1996), pp. 205–230.

 [33] Sheu, S.:  Asymptotic behavior of the invariant density of a diﬀusion Markov process with small diﬀusion,  SIAM J. Math. Anal. 17-2 (1986), pp. 451–460.

 [34] Villani, C.:  Optimal transport. Old and new,  Springer-Verlag, Volume 338 (2009).

 [35] Wu, S., Hwang, C. and Chu, M.:  Attaining the optimal Gaussian diﬀusion acceleration,  J. Stat. Phys. 155-3 (2014), pp. 571–590. University of Helsinki, Department of Mathematical and Statistical Sciences. PL 68, Pietari Kalmin katu 5. Postal Code: 00560. Helsinki, Finland. Email address :  gerardo.barreravargas@helsinki.fi  