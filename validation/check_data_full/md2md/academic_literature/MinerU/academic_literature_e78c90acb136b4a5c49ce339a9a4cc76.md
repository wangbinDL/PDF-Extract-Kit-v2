# A sharp uniform-in-time error estimate for Stochastic Gradient Langevin Dynamics  

Lei Li  $^{\mathrm{a,b,}}$    and Yuliang Wang  $\cdot\mathrm{a,b}$  

$^\mathrm{a}$  School of Mathematical Sciences, Shanghai Jiao Tong University, Shanghai, 200240, P.R.China.  $^\mathrm{b}$  Institute of Natural Sciences, MOE-LSC, Shanghai Jiao Tong University, Shanghai, 200240, P.R.China. c Qing Yuan Research Institute, Shanghai Jiao Tong University, Shanghai, 200240, P.R.China.  

# Abstract  

We establish a sharp uniform-in-time error estimate for the Stochastic Gradient Langevin Dynamics (SGLD), which is a popular sampling algorithm. Under mild as- sumptions, we obtain a uniform-in-time    $O(\eta^{2})$   bound for the KL-divergence between the SGLD iteration and the Langevin diﬀusion, where    $\eta$   is the step size (or learning rate). Our analysis is also valid for varying step sizes. Based on this, we are able to obtain an    $O(\eta)$   bound for the distance between the SGLD iteration and the distribution of the Langevin diﬀusion, in terms of Wasserstein or total variation distances.  

# 1 Introduction  

The Stochastic Gradient Langevin Dynamics (SGLD) [ 49 ], ﬁrst proposed by Welling and Teh, has drawn great attention of researchers when dealing with optimization or sampling tasks [ 2 ,  33 ,  40 ]. As a sampling algorithm, SGLD can be viewed as a “random batch” version of the Unadjusted Langevin Algorithm (ULA), which is the Euler-Maruyama discretization of the Langevin diﬀusion, a stochastic process converging to a target Gibbs’ distribution under suitable settings. As an optimization algorithm, SGLD can be viewed as a variant of the classical Stochastic Gradient Descent (SGD) [ 44 ], by adding independent Gaussian noise in each iteration of SGD. At recent decades, SGD and its variants [ 44 ,  25 ,  11 ,  37 ] have received a great deal of attention when solving high-dimensional tasks, ranging from computer vision, natural language processing, to high dimensional sampling, statistical opti- mization, etc. Also much theoretical analysis for SGD has been done by former researchers, including loss landscape of SGD iteration [ 46 ,  47 ], its dynamical stability [ 50 ] and diﬀusion approximation [ 32 ,  21 ,  17 ]. The combination of the SGD algorithm and the Langevin diﬀu- sion, can improve the behavior of both methods: for SGD, by taking another independent diﬀusion term into consideration, though not converging to a ﬁxed point, the algorithm may be able to admit better ergodic properties and obtain better performance near sad- dle points [ 26 ,  52 ]. Besides, the application of the methodology of random mini-batch to Langevin diﬀusion could result in some eﬃcient methods that could reduce computational cost while preserving the dynamical and statistical properties. Examples include the SGLD algorithm we study in the paper and the random batch methods for interacting particle systems [ 22 ,  23 ].  

In this paper, we consider the error estimate of SGLD for sampling from the target distribution    $\pi\propto e^{-\beta U}$  , where the function    $U(x)$   of the form  

$$
U(\boldsymbol{x}):=\mathbb{E}_{\boldsymbol{\xi}}\left[U(\boldsymbol{x};\boldsymbol{\xi})\right],\quad\boldsymbol{x}\in\mathbb{R}^{d}.
$$  

Here,    $\xi\sim\nu$   is a random variable/vector for some distribution    $\nu$  . A typical form of ( 1.1 ) arising from applications like Bayesian inference or machine learning [ 49 ] is given by  

$$
U(x):=U_{0}(x)+\frac{1}{N}\sum_{i=1}^{N}U_{i}(x).
$$  

We remark that in [ 49 ], there was no   $1/N$   factor. Such a factor can be obtained by suitable scaling, like choosing suitable    $\beta$   or rescaling the time in the Langevin diﬀusion, and it is helpful so that it can be written as an expectation over a probability distribution. Then the random vector    $\xi$   can be taken as a random batch with size    $S$   and then    $U(x;\xi)=U_{0}(x)+$   $\textstyle{\frac{1}{S}}\sum_{i\in\xi}U_{i}(x)$  P ). The associated (overdamped) Langevin diﬀusion (a stochastic diﬀerential equation (SDE)) for the target distribution    $\pi$   is given by:  

$$
d X=b(X)d t+\sqrt{2\beta^{-1}}d W,
$$  

where  

$$
b(\boldsymbol{x}):=-\nabla U(\boldsymbol{x}),
$$  

and    $W$   is the standard Brownian Motion in    $\mathbb{R}^{d}$  , and    $\beta^{-1}\ >\ 0$   is the ﬁxed temperature constant. The target distribution    $\pi(x)\propto e^{-\beta U(x)}$    is exactly the invariant distribution of the Langevin diﬀusion [ 41 ]. We also denote  

$$
b^{\xi}(x)=-\nabla U(x;\xi)
$$  

in this paper. Then the SGLD algorithm with time step    at    $k$  -th iteration is:  $\eta_{k}$  

$$
\bar{X}_{T_{k+1}}=\bar{X}_{T_{k}}+\eta_{k}b^{\xi_{k}}(\bar{X}_{T_{k}})+\sqrt{2\beta^{-1}\eta_{k}}Z_{k},\quad Z_{k}\sim N(0,I_{d})\quad i.i.d.,
$$  

with    $\begin{array}{r}{T_{k}\,:=\,\sum_{i=0}^{k-1}\eta_{i}}\end{array}$  . Here,    $\xi_{k}$   are i.i.d. sampled. Also we have the following continuous version which coincides with the discrete SGLD at grid point    $T_{k}$  :  

$$
\Bar{X}_{t}:=\Bar{X}_{T_{k}}+(t-T_{k})b^{\xi_{k}}(\Bar{X}_{T_{k}})+\sqrt{2\beta^{-1}}\left(W_{t}-W_{T_{k}}\right),\quad t\in[T_{k},T_{k+1})\,.
$$  

At time    $t$  , denote densities of    $X_{t}$  ,  $X_{t}$  t  by    $\rho_{t}$  ,   $\rho_{t}$  , respectively. In this paper, our main results focus on the “distance” between    $\rho_{t}$   and   $\rho_{t}$  . In our main results, we consider the Kullback- Leibler (KL) divergence [ 28 ], deﬁned by  

$$
D_{K L}(\mu||\nu):=\int_{\mathbb{R}^{d}}\log\frac{d\mu}{d\nu}\,\mu(d x),
$$  

where    $\mu$  ,    $\nu$   are probability measures on    $\mathbb{R}^{d}$  . Note that the KL-divergence is not a distance (a metric) in mathematics. Furthermore, based on this estimate, convergence rate to the invariant distribution of the Langevin diﬀusion ( 1.3 ) and results for particular time step sequences will be discussed.  

A great deal of theoretical research for the SGLD algorithm has been done. In [ 51 ], the authors studied the hitting time of SGLD for non-convex optimization problem. Diﬀerent from the goal of our work, instead of analyzing the convergence to a target distribution, the authors focused on ﬁnding a local minimum and the corresponding convergence results. For sampling-aimed tasks, much SGLD-related research has been done when the target distri- bution is log-concave [ 10 ,  9 ,  8 ]. Convergence analysis for SGLD under non-convex settings is a bit more technical. In [ 43 ], the authors obtained an error bound for the Wasserstein-2 distance between the SGLD iteration and the target distribution of order    $O(k\eta+e^{-k\eta})$  , where    $k$   is the number of iterations and    is the constant time step. In [ 36 ], assuming the  $\eta$  boundedness of the drift function, the authors proved the error is of order    $O(\sqrt{k\eta})$   in terms of Wasserstein-2 distance. In [ 53 ], assuming the second-order smoothness of the drift func- tion, the authors obtain  an improved bound of order    $O(\sqrt\eta/S+\eta+(1-\eta)^{k})$   in terms of total variance, where  S  is the batch size. Diﬀerent from most former work, where the error bounds had an at least polynomial dependency on the time    $T$   , in [ 16 ], the authors obtained a uniform-in-time bound, enabling more long time analysis for SGLD. One point worth emphasizing is that, observing the time step    $\eta$  , none of the former work can get esti- mation better than    $O({\sqrt{\eta}})$   in terms of Wasserstein distances or total variation distance. In this paper, we resolve this issue and obtain a sharp bound in terms of    $\eta$  .  

As has been mentioned, SGLD can be viewed as the “random batch” version of the Euler- Maruyama scheme for the Langevin diﬀusion ( 1.3 ), which is also known as the Unadjusted Langevin Algorithm (ULA), or the Langevin Monte Carlo (LMC). In this paper, the main part of our result for SGLD is built upon our analysis for ULA, since it can be viewed as the simpler full-batch version of SGLD. Based on this observation, the convergence rate with respect to the time step    $\eta$   for SGLD would not exceed that for ULA. Much work on ULA has been done before, some of which are found useful for our sharp analysis for SGLD. In [ 8 ], using the ﬁrst order smoothness assumption, the authors showed that    $D_{K L}(\hat{\rho}_{T}||\rho_{T})=$   ||  $O(\eta T d)$  , where   $\hat{\rho}_{t}$  t  denotes the density of the continuous version ULA (similar with   $\rho_{t}$  ) at time    $t$  ,    $T$   is the length of the (ﬁnite) time interval, and    $d$   is the dimension of the Euclidean space. However, this is not the optimal rate, since this result implies that    $W_{2}(\hat{\rho}_{T},\rho_{T})\,=$   $O({\sqrt{\eta}})$   rather than the well-known    $O(\eta)$   [ 3 ,  9 ]. In [ 35 ], Mou improved the KL divergence  $D_{K L}(\hat{\rho}_{T}||\rho_{T})$   ||  ) fro  $O(\eta T d)$   to    $O(\eta^{2}d^{2}T)$  , so the Wasserstein distance is of    $O(\eta)$  . Compared with the former “  $O(\eta T d)^{,}$  )” result, the improved result in [ 35 ] needs second order smoothness of the drift function    $b(x)$  .  

Our work is naturally motivated by the following two questions:  

•  For ULA, the error in terms of KL-divergence can be improved from    $O(\eta)$   to    $O(\eta^{2})$   if we add the second order smoothness assumption for the drift. Can we do the same for SGLD to obtain a sharp bound? •  Most error analysis for ULA and SGLD has at least polynomial dependency for the time interval    $T$   , which prevents us from digging deeper into the asymptotic behaviors as    $T\to\infty$  of these stochastic algorithms. Are we able to establish a uniform-in-time error bound?  

In this paper, we give positive answers to both questions above.  

The main contribution of this paper is to establish a uniform-in-time    $O(\eta^{2})$   bound for the KL-divergence between SGLD iterates and the Langevin diﬀusion, namely, in Theorem 3.2  we show that  

$$
D_{K L}\big(\bar{\rho}_{T_{k}}||\rho_{T_{k}}\big)\leq c_{1}\eta_{0}^{2}e^{-A_{0}T_{k}}+c_{2}\int_{0}^{T_{k}}e^{-A_{0}(T_{k}-s)}f\big(s\big)d s,
$$  

where  

$$
T_{k}=\sum_{i=0}^{k-1}\eta_{i},\quad f(s)=\sum_{i=0}^{\infty}\eta_{i}^{2}\mathbf{1}_{[T_{i},T_{i+1})}(s).
$$  

If we simply consider the constant step size (or learning rate), then a uniform-in-time  $O(\eta^{2})$   error bound is obtained in Corollary  3.1 :  

$$
\operatorname*{sup}_{t\geq0}D_{K L}\big(\bar{\rho}_{t}||\rho_{t}\big)\leq c\eta^{2}.
$$  

The proof of our main results are based on the Markov property of SGLD. Indeed, the discrete SGLD process in our setting is a Markov Chain [ 13 ], and it is a time homogeneous one if the step size (or learning rate) is constant. Let    $\rho_{t}^{\xi}$    be the probability density of the ﬁxed-batch version of SGLD ( 1.7 ) for a given sequence of batches    $\pmb{\xi}:=(\xi_{0},\xi_{1},\cdot\cdot\cdot\ ,\xi_{k},\cdot\cdot\cdot)$  (which is actually the ULA with the drift    $b^{\xi}(x)$  ). Consequently, we have the following expression of the density:  

$$
\bar{\rho}_{t}(\cdot)=\mathbb{E}_{\xi}[\rho_{t}^{\pmb\xi}(\cdot)].
$$  

Here,  $\mathbb{E}_{\xi}[\rho_{t}^{\pmb{\xi}}(\cdot)]$  · )] means taking expectation for all possible choice of batch    $\xi$  . Note that    $\rho_{t}^{\xi}$  satisﬁes a Fokker-Planck equation, whose explicit expression will be derived in Lemma  2.1 .  

By the Markov property, we are able to ﬁnd that  

$$
\mathbb{E}\left[\rho_{t}^{\xi}\Big|\xi_{i},\,i\geq k\right]=\mathcal{S}_{T_{k},t}^{\xi_{k}}\bar{\rho}_{T_{k}},\quad t\in[T_{k},T_{k+1}),
$$  

where the operator    $S_{T_{k},t}^{\xi_{k}}$    is the evolution operator from    $T_{k}$   to    $t$   for the Fokker-Planck equation. Based on this observation, we are able to estimate the time derivative of the KL-divergence    $D_{K L}\big(\bar{\rho}_{t}||\rho_{t}\big)$  || ), and then obtain the desired second-order error bound after a Gr¨ onwall’s inequality. Also, while handling the details, techniques including integration by parts (to eliminate the Gaussian noise that would possibly lower the convergence rate) and Girsanov transform are adopted.  

We also have some corollaries of our results:  

First, we consider the special case    $\eta_{i}=(\ell+i)^{-\theta}$  ,    $i=0,1,2,\ldots$  , with    $\theta\in(0,1)$   being the decaying coeﬃcient, which is common in many practical tasks [ 31 ]. In Section  3 , we analyze the asymptotic convergence rate of    $D_{K L}(\bar{\rho}_{T_{k}}||\rho_{T_{k}})$  ) as    $k\to+\infty$  for diﬀerent    $\theta$  .  

Second, we estimate the Wasserstein-2 distance [ 45 ] between the SGLD iteration and the target distribution    $\pi$  , and after comparison with former work, our result is conﬁrmed to be a great improvement.  

The rest of the paper is organized as follows. Before our main results, we introduce some preliminaries in Section  2  including the basic background and properties of the (overdamped) Langevin diﬀusion and its Euler-Maruyama discretization, ULA. In Section  3 , we present and prove our main result: a sharp uniform-in-time estimate for SGLD, and some useful corollaries are also included. In Section  4 , we provide the proof for a crucial local estimate, which is omitted in Section  3  for the convenience of readers. Some technical details that are not so important are moved to the Appendix. In Section  5 , we perform discussion on our analysis on the Wasserstein-2 distance between the SGLD iteration and the target distribution    $\pi$   based on our main results. The ergodicity of SGLD algorithm as well as the reason why our analysis is “sharp” are also discussed in Section  5 .  

# 2 Preliminaries  

For the convenience of readers, let us begin with some basic deﬁnitions and properties that would be useful in this paper.  

# 2.1 (Overdamped) Langevin Diﬀusion  

Derived from the Langevin equation, the (overdamped) Langevin diﬀusion has strong, well- known physical background [ 41 ]. Let us ﬁrst consider the following second-order SDE called Langevin equation:  

$$
\ddot{X}=-\nabla U(X)-\gamma\dot{X}+\sqrt{2\gamma/\beta}\,\dot{W},
$$  

where    $\gamma$   is the friction coeﬃcient,    $\beta^{-1}:=k_{B}T$   with  k  $k_{B}$   being the Boltzmann constant and  $T$   being the (physical) temperature. The term    $\gamma\dot{X}$   here describes the linear dissipation damping, and the term  $\sqrt{2\gamma/\beta}\dot{W}$   describes the ﬂuctuation stochastic forcing. Note that the Brownian Motion    $W$   is not pointwise diﬀerentiable, and so  $\dot{W}$   should be understood in the distributional sense and is in fact the white noise [ 38 ]. Moreover, thanks to the Fluctuation-Dissipation Theorem [ 27 ], we are able to relate the dissipation and the ﬂuctua- tion by considering the covariance of the ﬂuctuation term.  

Langevin equation ( 2.1 ) describes a particle moving according the Newton’s second law and being in contact with a heat reservoir that is at equilibrium at temperature    $T$  . This physical is called an open classical system. To see this more clearly, we rewrite the Langevin  $Y={\dot{X}}$  equation ( 2.1 ) into an SDE system. Letting   , we have  

$$
\left\{\begin{array}{l}{d X=Y d t}\\ {d Y=-\nabla U(X)d t-\gamma Y d t+\sqrt{2\gamma\beta^{-1}}d W}\end{array}\right.
$$  

It is also well-known that if we consider the time rescaling    $X^{\gamma}(t)\;=\;X(\gamma t)$  , and let  $\gamma\to+\infty$  , the Langevin equation ( 2.1 ) turns into the overdamped Langevin diﬀusion [ 41 ]:  

$$
\begin{array}{r}{d X=-\nabla U(X)d t+\sqrt{2\beta^{-1}}d W.}\end{array}
$$  

The derived (overdamped) Langevin diﬀusion above has some pretty properties. First, it has invariant distribution    $\pi\;\propto\;e^{-\beta U}$  , which is trivial to check. Second, the invariant distribution    $\pi$   satisﬁes the detailed balance since the probability ﬂux    $\begin{array}{r}{J(\pi):=b\!\cdot\!\pi\!-\!\frac{1}{2}\nabla\!\cdot\!\left(\Sigma\pi\right)}\end{array}$  equals zero with    $b\,=\,-\nabla U$   and   $\Sigma\:=\:\sqrt{2\beta^{-1}}I$  p  here, and thus the stationary diﬀusion is reversible [ 41 ]. Third, the density of the Langevin diﬀusion satisﬁes the following Fokker- Planck equation:  

$$
\partial_{t}\rho_{t}=-\nabla\cdot\left(\rho_{t}\boldsymbol{b}\right)+\beta^{-1}\Delta\rho_{t},\quad\left.\rho_{t}\right|_{t=0}=\rho_{0}.
$$  

with    $b=-\nabla U$  . Moreover, if we add some mild assumptions to the function    $U$   like strongly log-concaveness, the Langevin diﬀusion above is guaranteed to converge to equilibrium [ 34 ]. Note that in this paper, instead of log-concaveness of the invariant distribution    $\pi$  , we add the much weaker assumption that    $\pi$   satisﬁes a Log-Sobolev inequality (LSI).  

# 2.2 Unadjusted Langevin Algorithm(ULA)  

Among the classical numerical schemes for the Langevin diﬀusion ( 1.3 ), the simplest one is the well-known Euler-Maruyama scheme, which is also known as the Unadjusted Langevin Algorithm (ULA) or the Langevin Monte Carlo (LMC). Consider this Euler-Maruyama scheme with constant time step for ( 1.3 )  

$$
\hat{X}_{T_{k+1}}=\hat{X}_{T_{k}}+\eta_{k}b(\hat{X}_{T_{k}})+\sqrt{2\beta^{-1}\eta_{k}}Z_{k},\quad Z_{k}\sim N(0,I_{d})\quad i.i.d.,
$$  

where    is the time step at    $k$  -th iteration and    $\begin{array}{r}{T_{k}:=\sum_{i=0}^{k-1}\eta_{i}}\end{array}$  . ( 2.5 ) naturally admits the  $\eta_{k}$  following continuous version:  

$$
\begin{array}{r}{\hat{X}_{t}:=\hat{X}_{T_{k}}+(t-T_{k})b(\hat{X}_{T_{k}})+\sqrt{2\beta^{-1}}\left(W_{t}-W_{T_{k}}\right),\quad t\in[T_{k},T_{k+1})\,,}\end{array}
$$  

where    $W_{t}$   is the Brownian Motion in    $\mathbb{R}^{d}$  We also denote   $\hat{\rho}_{t}(x)$  ) the probability density function of  $\hat{X}_{t}$  t . It is not diﬃcult to show that   $\hat{\rho}_{t}$   satisﬁes a Fokker-Planck equation, and we conclude it in the following lemma:  

Lemma 2.1.  Denote    $\hat{\rho}_{t}(x)$   the probability density function of  $\hat{X}_{t}$   deﬁned in  ( 2.6 ) . Then the following Fokker-Planck equation holds:  

$$
\begin{array}{r}{\partial_{t}\hat{\rho}_{t}=-\nabla\cdot\left(\hat{\rho}_{t}\hat{b}_{t}\right)+\beta^{-1}\Delta\hat{\rho}_{t},\quad\hat{\rho}_{t}|_{t=0}=\rho_{0},}\end{array}
$$  

where  

$$
\hat{b}_{t}(x):=\mathbb{E}\left[b\left(\hat{X}_{T_{k}}\right)|\hat{X}_{t}=x\right],\quad t\in[T_{k},T_{k+1})\,.
$$  

The derivation is not diﬃcult and has appeared in many classical work [ 35 ]. Indeed, for  $t\in[T_{k},T_{k+1})$  , consider the random variable   $\hat{\rho}_{t}|\hat{\mathcal{F}}_{T_{k}}$  | F , where  $\hat{\mathcal{F}}_{T_{k}}=\sigma(\hat{X}_{s},s\leq T_{k})$  F  ≤ ). Then, by deﬁnition of  $\hat{X}_{t}$  ,   $\hat{\rho}_{t}|\hat{\mathcal{F}}_{T_{k}}$  | F  satisﬁes:  

$$
\partial_{t}\bigl(\hat{\rho}_{t}\vert\hat{\mathcal{F}}_{T_{k}}\bigr)=-\nabla\cdot\Bigl(b\bigl(\hat{X}_{T_{k}}\bigr)\bigl(\hat{\rho}_{t}\vert\hat{\mathcal{F}}_{T_{k}}\bigr)\Bigr)+\beta^{-1}\Delta\bigl(\hat{\rho}_{t}\vert\hat{\mathcal{F}}_{T_{k}}\bigr),\quad t\in[T_{k},T_{k+1})\,.
$$  

Taking expectation, we have  

$$
\mathbb{E}\left[\partial_{t}\big(\hat{\rho}_{t}\vert\hat{\mathcal{F}}_{T_{k}}\big)\right]=\partial_{t}\hat{\rho}_{t},\quad\mathbb{E}\left[\Delta\big(\hat{\rho}_{t}\vert\hat{\mathcal{F}}_{T_{k}}\big)\right]=\Delta\hat{\rho}_{t},
$$  

and for the drift term,  

$$
\begin{array}{l l}{\mathbb{E}\left[-\nabla\cdot\left((\hat{\rho}_{t}|\hat{\mathcal{F}}_{T_{k}})(x)b(\hat{X}_{T_{k}}^{\xi})\right)\right]=-\nabla\cdot\displaystyle\int(\hat{\rho}_{t}|\hat{\mathcal{F}}_{T_{k}})(x|y)b(y)\hat{\rho}_{T_{k}}(y)d y}\\ {=-\nabla\cdot\displaystyle\int b(y)\hat{\rho}_{t,T_{k}}(x,y)d y}\\ {=-\nabla\cdot\left(\hat{\rho}_{t}(x)\mathbb{E}\left[b(\hat{X}_{T_{k}}^{\xi})|\hat{X}_{t}=x\right]\right),}\end{array}
$$  

where   $\hat{\rho}_{t,T_{k}}$   indicates the joint distribution density of   $\hat{\rho}_{t}$   and   $\hat{\rho}_{T_{k}}$  . Note that we use Bayes’ law in the second equality. Combining all the above, we obtain the desired result ( 2.7 ).  

# 3 Main results  

In this section, we present our main result of this paper: a sharp uniform-in-time error estimate for SGLD. In Section  3.1 , we present the assumptions required by later analysis. In Section  3.2 , we give some auxiliary results, including propagation of LSI of Langevin diﬀusion, moment control for ULA, and estimation of the Fisher information for ULA. After these preparations, in Section  3.3 , we present the main theorem, Theorem  3.2 , by ﬁrst showing a crucial local result, Proposition  3.2 . Moreover, we give some corollaries including constant time step case, special decaying step size (or learning rate) case, and the special step size case,    $\eta_{i}=(\ell+i)^{-\theta}$  .  

# 3.1 Our assumptions  

Before the main results and proofs, we ﬁrstly give the following assumptions we use through- out this paper. Recall the deﬁnition of the drift function    $b$   in SGLD and its target distribution  $\pi$   in Section  1 . For technical reasons, we will need the following assumptions.  

# Assumption 3.1.  

(a) (1st order smoothness) For a.e.    $\xi\sim\nu$  ,    $b^{\xi}$    is Lipshitz with a uniform constant    $L$  , i.e. ξ ,  $\forall x,y\in\mathbb{R}^{d}$  ,  

$$
|b^{\xi}(x)-b^{\xi}(y)|\leq L|x-y|.
$$  

(b) (2nd order smoothness) For a.e.    $\xi\sim\nu$  ,    $\nabla b^{\xi}$    is Lipshitz with a uniform constant    $L_{2}$  , i.e.  $\forall\xi$  ,  $\forall x,y\in\mathbb{R}^{d}$  ,  

$$
|\nabla b^{\xi}(x)-\nabla b^{\xi}(y)|\leq L_{2}d^{-\frac{1}{2}}|x-y|.
$$  

(c) (distance dissipation) For a.e.    $\xi\sim\nu$  ,    $b^{\xi}$    is conﬁning in the sense that  

$$
x\cdot b^{\xi}(x)\leq-\mu|x|^{2}+\sigma
$$  

with    $\mu$  ,    $\sigma$   being positive constants.  

(d) (boundedness)    $b^{\xi}-b$   is uniformly bounded, namely,  

$$
\begin{array}{r}{\operatornamewithlimits{e s s u p}_{\xi}||b^{\xi}-b||_{L^{\infty}(\ensuremath{\mathbb{R}}^{d})}<+\infty.}\end{array}
$$  

Moreover, the coeﬃcient    $L$  ,    $L_{2}$  ,    $\mu$  ,    $\sigma$   are independent of    $\xi$   and    $d$  .  

In condition (a), the Lipschitz constant    $L$   is the upper bound of the spectrum norm

 (largest singular value) of the Jacobian matrix and it is insensitive to the dimension    $d$  . In

 ( 3.2 ) in condition (b), we have put    $d^{-1/2}$    in the constant and assumed    $L_{2}$   to be independent of    $d$  . The intuition is that the left hand side is the spectral norm of the Jacobian matrix, which can be assumed to be insensitive to    $d$   while    $|x-y|$   scales like  $\sqrt{d}$  . As we shall later, putting such a scaling can make the bounds of the relative entropy and Fisher information linear in    $d$   (see our discussion at the end of Section  5.2 ), which is the correct scaling. This is a diﬀerence from the result in [ 35 ].  

$b^{\xi}-b^{\xi}$   is also uniformly bounded Note that condition (d) is equivalent to saying that   for two diﬀerent    $\xi$  ,   $\ddot{\xi}$  . In (d) of Assumption  3.1 , we do not need the uniform boundedness for every    $b^{\xi}$  , though (d) naturally holds when   $\begin{array}{r l}{\mathrm{sessup}_{\xi}\|b^{\xi}(x)\|_{\infty}\,<\,\infty}\end{array}$  , which is a much stronger condition. Actually the condition (d) is natural in applications. In many problems in machine learning, the loss has the same asymptotics for diﬀerent data point.  

In our paper, conditions (c) is used only to control the moments. Actually condition (c) is the conﬁnement condition which is crucial in literature for ergodicity. In our case, the log Sobolev inequality later in Assumption  3.2  actually plays the role of conﬁnement for ergodicity. Moreover, it is not diﬃcult to see that if one has the stronger boundedness condition   $\begin{array}{r}{\operatornamewithlimits{e s s u p}_{\xi}\operatorname*{sup}_{x}|b^{\xi}(x)|<\infty}\end{array}$  , then conditions (c) and (d) can be removed since the only place we use the distance dissipation condition (c) is the moment control (Propostition 3.1 ), but the only place we use the moment control is bounding terms like    $b^{\xi}(X_{t})$  . Now if we assume each    $b^{\xi}$    is bounded, we do not need the result for moment control any more.  

# Assumption 3.2.  

(a) (  $\lambda$  -warm start) There exists    $\lambda\geq1$   such that the initial distribution    satisﬁes  $\rho_{0}$  

$$
\frac{1}{\lambda}\leq\frac{\rho_{0}}{\pi}\leq\lambda,
$$  

where    $\pi\;\propto\;e^{-\beta U}$    is the invaria   tribut n of   .3 ) . Note that    $\rho_{0}$   is the initial    $\hat{X}$    distribution for all the processes  X , , and X , and  λ  is independent of the dimension  $d$  .  

(b) (LSI for    $\pi$  ) The invariant distribution    $\pi\propto e^{-\beta U}$    satisﬁes a Log-Sobolev inequality with a constant    $C_{\pi}^{L S}$  , namely,    $\forall f\in C_{>0}^{\infty}$  ,  

$$
E n t_{\pi}(f):=\int f\log f d\pi-\left(\int f d\pi\right)\log\left(\int f d\pi\right)\leq C_{\pi}^{L S}\int\frac{|\nabla f|^{2}}{f}d\pi.
$$  

Here,    $C_{>0}^{\infty}$    consists of all nonnegative smooth functions.  

The Log-Sobolev inequality (LSI) was ﬁrst discussed by Gross in 1975 [ 20 ]. Besides the simplest Gaussian distribution, other distributions satisfying an LSI can be found following the Bakry-Emery criterion [ 4 ], including strongly log-concave ones. It is also shown that distributions that are strongly log-concave outside a compact set also satisfy the LSI [ 29 ]. We remark that the log-concaveness outside a compact set can imply both the distance dissipation and the log Sobolev inequality so the LSI assumption is much weaker than the log-concaveness assumption in many other literature. However, the distance dissipation condition    $\boldsymbol{x}\cdot\boldsymbol{b}\leq-\mu|\boldsymbol{x}|^{2}+\sigma$   outside a compact set can not derive the corresponding LSI so neither the distance dissipation nor the LSI assumption can be simply removed though they seem to have repetition somehow.  

# 3.2 Some auxiliary results  

Before presenting the main theorem, we give some useful auxiliary results ﬁrst, including the propagation of LSI for the Langevin diﬀusion ( 1.3 ), moment control for ULA ( 2.6 ), and estimation of Fisher information for ULA ( 2.6 ).  

# 3.2.1 Propagation of Log-Sobolev inequality  

In this section, we aim to establish a Log-Sobolev inequality (LSI) for    $\rho_{t}$  , which is the density of    $X_{t}$   in the Langevin diﬀusion ( 1.3 ).  

Theorem 3.1.  Consider the Fokker-Planck equation  ( 2.4 )  associated with the SDE  ( 1.3 ) . Suppose Assumption  3.2  holds. Then,    $\rho_{t}$   satisﬁes a LSI with a uniform LSI constant    $\lambda^{2}C_{\pi}^{L S}$  .  

The following Holley-Stroock perturbation lemma [ 5 ] is essential to our proof :  

Lemma 3.1  (Holley-Stroock perturbation) .  Suppose the probability measure    $\nu\,\in\,\mathcal{P}(\mathbb{R}^{d})$  satisﬁes an LSI with constant    $C_{\nu}^{L S}$  , and    $\mu\,\in\,\mathcal P(\mathbb{R}^{d})$   satisﬁes    $d\mu\,=\,h d\nu$   with the uniform bound    $\begin{array}{r}{\frac1\lambda\le h\le\lambda}\end{array}$  . Then    $\mu$   satisﬁes an LSI with constant    $\lambda^{2}C_{\nu}^{L S}$  .  

Proof of Theorem  3.1 :  

$$
\rho_{t}={\frac{\rho_{t}}{\pi}}\pi=:q_{t}\pi.
$$  

Since    $b\,=\,\beta^{-1}\nabla\log\pi$  , the detailed balanced is satisﬁed [ 34 ]. So it is well-known that    $q_{t}$  satisﬁes the following backwards Kolmogorov equation [ 30 ]:  

$$
\partial_{t}q_{t}=b\cdot\nabla q_{t}+\beta^{-1}\Delta q_{t},\quad q_{t}|_{t=0}=\frac{\rho_{0}}{\pi},
$$  

and    $q_{t}$   can be expressed by the following conditional expectation form:  

$$
q_{t}(x)=\mathbb{E}\left[q_{0}(X_{t})|X_{0}=x\right].
$$  

The sequence of ( 3.9 ), we know that at any time    $t>0$  ,  $\textstyle\operatorname*{inf}_{x}q_{t}\geq\operatorname*{inf}_{x}q_{0}$  , and sup  $\begin{array}{r}{\operatorname*{sup}_{x}q_{t}\,\leq\,\operatorname*{sup}_{x}q_{0}}\end{array}$   ≤ . Combining this fact and condition (a) in Assumption  3.2 , it holds that  

$$
\frac{1}{\lambda}\leq q_{t}\leq\lambda,\quad\forall t\geq0.
$$  

Then, combining ( 3.10 ) , Lemma  3.1 , and (b) in Assumption  3.2 , the conclusion holds.  

Note that the fact   $\textstyle\operatorname*{inf}_{x}q_{t}\geq\operatorname*{inf}_{x}q_{0}$  ,   $\begin{array}{r}{\operatorname*{sup}_{x}q_{t}\leq\operatorname*{sup}_{x}q_{0}}\end{array}$   can also be derived from classical results of PDE. Indeed, since the backward Kolmogorov equation ( 3.8 ) for    $q_{t}$   is of parabolic type, the maximal principle holds, whose details can be found in Chapter 7 of [ 15 ]. By maximal principle and condition (a) in Assumption  3.2 , we also obtain  

$$
\frac{1}{\lambda}\leq q_{t}\leq\lambda,\quad\forall t\geq0.
$$  

# 3.2.2 Moment control  

In this section, we aim to ﬁnd a uniform-in-time bound for the moments    $\mathbb{E}|\bar{X}_{t}^{\xi}|^{p}$    |  with  $X^{\xi}$  deﬁned in ( 1.12 ) of Section  1  and    $p=2,4$  . The details could be found in the proposition below:  

Proposition 3.1.  Consider the process  $X_{t}$   deﬁned in  ( 1.7 )  of Section  1 . Suppose (a), (c) of Assumption  3.1  holds. For all integer    $p\geq1$  , there exists positive constants    $c_{p}$   and    $\Delta_{p}$  independent of  t  and    $\xi$   such that if    $\eta_{k}\leq\Delta_{p}$   for all    $k$  , then  

$$
\mathbb{E}\left[|\bar{X}_{t}|^{p}\Big|\mathcal{F}_{\xi}\right]\leq c_{p}d^{\frac{p}{2}},\quad\forall t\geq0.
$$  

Moreover, for all integer    $p\geq1$  , there exists a positive constant    $\alpha_{p}$   such that when    $\alpha<\alpha_{p}$  ,  

$$
\operatorname*{sup}_{t\geq0}\mathbb{E}\left[e^{\alpha|\bar{X}_{t}|^{p}}\Big|\mathcal{F}_{\xi}\right]<+\infty.
$$  

Here,    $\mathcal{F}_{\xi}$   denotes the    $\sigma$  -algebra generated by  ${\pmb\xi}=(\xi_{k})_{k\geq0}$  .  

See Section  A.1  for the detailed proof.  

# 3.2.3 Estimate of the Fisher information  

The Fisher information for a probability measure    $\rho$   is deﬁned by  

$$
\mathcal{Z}(\rho):=\int|\nabla\log\rho|^{2}\rho d x.
$$  

In our analysis, we come up with the exponential-weighted sum of Fisher information at the grid point    $T_{k}$   of ULA (SGLD with ﬁxed batch), and a uniform-in-time order-one bound for this summation is required. To handle this, our strategy is to ﬁrstly estimate the continuous sum (i.e. integration) of the exponential-weighted Fisher information in Lemma  3.2 . Then, using the existing stability result (Lemma  3.3  below) for Fisher information of ULA [ 35 ], we are able to control the desired discrete summation with the integration of the exponential- weighted Fisher information along the time axis.  

Recall that    $\rho_{t}^{\xi}$    is the law of the SGLD ( 1.7 ) conditioning on the given sequence of batches  ${\pmb\xi}=(\xi_{0},\xi_{1},\allowbreak\cdot\cdot\allowbreak,\xi_{k},\allowbreak\cdot\cdot\allowbreak)$  . In Section  A.2 , we ﬁrst establish  

$$
\frac{d}{d t}D_{K L}(\rho_{t}^{\pmb{\xi}}||\pi)\leq-c_{0}\mathcal{Z}(\rho_{t}^{\pmb{\xi}})+c_{1}d,
$$  

where we recall    $\pi\propto e^{-\beta U}$    and consequently  

$$
\begin{array}{r}{D_{K L}(\rho_{t}^{\pmb{\xi}}||\pi)\leq c d,}\end{array}
$$  

where    $c_{0}$  ,    $c_{1}$  ,    $c$   are positive constants independent of    $t$   and    $\xi$  . Then, after simple calculation including integration by parts, we are able to prove the following Lemma:  

Lemma 3.2.  Let    $f$   be a non-increasing, nonnegative, piecewise-constant function. Then under Assumption  3.1 ,  3.2 , there exists    $\Delta_{0}>0$  , for any    $A_{0}>0$  , there exist positive constants  $M_{1}$  ,    $M_{2}$  , independent of    $T$   and    $\xi$   such that when the step size sequence    $\{\eta_{k}\}$   deﬁned in  ( 1.6 ) is bounded by    $\Delta_{0}$  , the followings hold:  

$$
\operatorname*{sup}_{t\geq0}D_{K L}(\rho_{t}^{\pmb{\xi}}||\pi)\leq c d,
$$  

where    $c$   is independent of    $T$   ,    $d$   and    $\xi$  . Moreover,  

$$
\begin{array}{l l}{\displaystyle\int_{0}^{T}e^{-A_{0}(T-s)}f(s)\mathcal{I}(\rho_{s}^{\xi})d s}\\ {\displaystyle\quad\leq M_{1}D_{K L}(\rho_{0}||\pi)f(0)e^{-A_{0}T}+M_{2}\left(1+\operatorname*{sup}_{s\geq0}D_{K L}(\rho_{s}^{\xi}||\pi)\right)\int_{0}^{T}e^{-A_{0}(T-s)}f(s)d s}\end{array}
$$  

The next lemma bounds the Fisher information    $\mathcal{Z}(\rho_{t}^{\xi})$  ) at time    $t$   with the Fisher infor- mation    $\mathcal{Z}(\rho_{T_{k}}^{\xi})$  ) at the grid point. The estimation is valid for small    $\eta_{k}$  , and we can view it as one kind of stability for the Fisher information of an only piecewise continuous process. The proof of the following lemma can be found in Lemma 6 of [ 35 ]  

Lemma 3.3.  U der the same se in  of L mma  3.2 , if    $\begin{array}{r}{\eta_{k}\,\leq\,\frac{1}{2L}}\end{array}$  ,    $k\geq0$  , then there is   $a$  positive constant  c  independent of  k ,  d , and  ξ  such that  

$$
\begin{array}{r}{\mathcal{Z}(\rho_{t}^{\xi})\leq8\mathcal{Z}(\rho_{t_{0}}^{\xi})+c\eta_{k}^{2}d,\quad\forall T_{k}\leq t_{0}\leq t\leq T_{k+1}.}\end{array}
$$  

$d^{-1/2}$    Clearly, with a factor   in the Lipschitz constant in Assumption  3.1 , the bounds of the relative entropy and Fisher information are linear in    $d$  .  

# 3.3 Main theorems  

Equipped with the preparation work before, we are then able to establish a sharp uniform- in-time second order error estimate for SGLD in terms of KL-divergence. Our analysis for SGLD is from local to global. The following local estimation is crucial to our main result, and the    $\eta^{2}$    term here is the core of our    $O(\eta^{2})$   bound in the main theorem. To avoid overloading the notation, the dependence on the size of function family  $N$  , the dimension    $d$  , the temperature    $\beta$  , and other parameters in Assumption  3.1 ,  3.2  are implicit.  

Proposition 3.2.  Consider the probability density functions    $\rho_{t}$  ,    $\rho_{t}$   for    $X_{t}$  ,  $X_{t}$  t  deﬁned in ( 1.3 ) ,  ( 1.7 ) . Then under Assumption  3.1 ,  3.2 , there exist positive constants    $A_{0}$  ,    $A_{1}$  ,    $\Delta_{0}$  independent of    $k$   and    $d$   such that when    $\eta_{k}<\Delta_{0}$  , the following local estimation holds:  

$$
\frac{d}{d t}D_{K L}\big(\bar{\rho}_{t}||\rho_{t}\big)\leq-A_{0}D_{K L}\big(\bar{\rho}_{t}||\rho_{t}\big)+A_{1}\eta_{k}^{2}\,\big(d+\mathcal{I}\big(\bar{\rho}_{T_{k}}\big)\big)\,,\quad\forall t\in[T_{k},T_{k+1}).
$$  

For the convenience of readers, we move the proof of Proposition  3.2  to the next section. Combining this local estimation for SGLD and the previous result for estimating the Fisher information of ULA (ﬁxed batch SGLD), it is not diﬃcult to obtain the following main theorem.  

Deﬁne the following piecewise-constant function    $f$  :  

$$
f(t):=\sum_{i=0}^{\infty}\eta_{i}^{2}\mathbf{1}_{[T_{i},T_{i+1})}(t),
$$  

where    $\mathbf{1}_{E}$   is the indicator function for set    $E$  .  

Theorem 3.2.  [Sharp error analysis for SGLD] Consider the probability density functions  $\rho_{t}$  ,    $\rho_{t}$   for    $X_{t}$  ,  $X_{t}$   deﬁned in  ( 1.3 ) ,  ( 1.7 ) . Suppose the time step sequence    $\{\eta_{k}\}$   is non- increasing. Then under Assumption  3.1 ,  3.2 , there exists positive constants    $\Delta_{0}$  ,    $A_{0}$  ,    $c_{1}$  ,    $c_{2}$  independent of    $k$   and    $d$   such that when    $\eta_{\mathrm{0}}\leq\Delta_{\mathrm{0}}$  ,  

$$
D_{K L}\big(\bar{\rho}_{T_{k}}||\rho_{T_{k}}\big)\leq c_{1}\eta_{0}^{2}e^{-A_{0}T_{k}}+c_{2}d\int_{0}^{T_{k}}e^{-A_{0}(T_{k}-s)}f\big(s\big)d s,
$$  

for    $f$   deﬁned in  ( 3.21 ) . Consequently, if the non-increasing time step sequence    $\{\eta_{k}\}$   con- verges to zero, and  $\begin{array}{r}{\sum_{i=0}^{+\infty}\eta_{i}=+\infty}\end{array}$  , the KL-divergence    $D_{K L}(\bar{\rho}_{T_{k}}||\rho_{T_{k}})$  ||  also tends to zero.  

Proof o eorem  3.2 :  By Proposition  3.2 , since    $\eta_{k}\leq\eta_{0}\leq\Delta_{0}$  , and since the Fisher infor- mation  I  $\mathcal{Z}(\rho)$  ) is a convex functional with respect to    $\rho$   (see [ 18 , Lemma 4.2]), we have  

$$
\begin{array}{r l r}{\lefteqn{\frac{d}{d t}D_{K L}(\bar{\rho}_{t}||\rho_{t})\leq-A_{0}D_{K L}(\bar{\rho}_{t}||\rho_{t})+A_{1}\eta_{k}^{2}\left(d+\mathcal{Z}(\bar{\rho}_{T_{k}})\right)}}\\ &{}&{\leq-A_{0}D_{K L}(\bar{\rho}_{t}||\rho_{t})+A_{1}\eta_{k}^{2}\left(d+\mathbb{E}_{\xi}\mathcal{Z}(\rho_{T_{k}}^{\xi})\right),\quad t\in[T_{k},T_{k+1}).}\end{array}
$$  

Then by Gr¨ onwall’s inequality, for all    $k$  , we have  

$$
\begin{array}{r l}&{D_{K L}\big(\bar{\rho}_{T_{k}}||\rho_{T_{k}}\big)\leq\mathbb{E}_{\xi}\displaystyle\sum_{i=0}^{k-1}\int_{T_{i}}^{T_{i+1}}e^{-A_{0}(T_{k}-s)}A_{1}\eta_{i}^{2}\left(d+\mathcal{I}(\rho_{T_{i}}^{\xi})\right)d s}\\ &{\qquad\qquad\qquad\qquad\qquad=A_{1}d\displaystyle\int_{0}^{T_{k}}e^{-A_{0}(T-s)}f(s)d s+A_{1}\mathbb{E}_{\xi}\int_{0}^{T_{k}}e^{-A_{0}(T-s)}\mathcal{I}(\rho_{T_{i}}^{\xi})f_{k}(s)d s}\\ &{\qquad\qquad\qquad\leq\tilde{A}_{1}d\displaystyle\int_{0}^{T_{k}}e^{-A_{0}(T-s)}f(s)d s+8A_{1}\mathbb{E}_{\xi}\int_{0}^{T_{k}}e^{-A_{0}(T-s)}\mathcal{I}(\rho_{s}^{\xi})f(s)d s}\end{array}
$$  

and the last inequality of ( 3.24 ) is due to Lemma  3.3 .  

Clearly,    $f$   is a piecewise constant, non-increasing, nonnegative function. Then by Lemma 3.2 , we are able to estimate the exponential-weighted sum of Fisher information along the path:  

$$
\int_{0}^{T_{k}}e^{-A_{0}(T-s)}\mathcal{I}(\rho_{s}^{\xi})f(s)d s\leq M_{1}^{\prime}\eta_{0}^{2}e^{-A_{0}T_{k}}+M_{2}^{\prime}d\int_{0}^{T_{k}}e^{-A_{0}(T-s)}f(s)d s.
$$  

Here, the positive constanes    $M_{1}^{\prime}$  ,    $M_{2}^{\prime}$    are independent of the batch    $\xi$   and the time    $T_{k}$  . Finally, combining ( 3.25 ) and ( 3.24 ), we have  

$$
D_{K L}\big(\bar{\rho}_{T_{k}}||\rho_{T_{k}}\big)\leq c_{1}\eta_{0}^{2}e^{-A_{0}T_{k}}+c_{2}d\int_{0}^{T_{k}}e^{-A_{0}(T_{k}-s)}f\big(s\big)d s,
$$  

where   ,   ,    $A_{0}$   are positive constant independent of the iteration number    $k$   and the di-  $c_{1}$   $c_{2}$  mension    $d$  .  

Clearly, by the sequence    $\{\eta_{k}\}$   decays to zero, and    $\textstyle\sum_{k=0}^{\infty}\eta_{k}\;=\;+\infty$  ∞ , t KL-divergence  $D_{K L}(\bar{\rho}_{T_{k}}||\rho_{T_{k}})$  || ) tends to zero. This then ends the proof.  $\sqsupset$  

As a direct corollary, if we consider the constant step size (or learning rate) case (  $\eta_{k}\equiv\eta$  ), the following sharp time-independent estimation can be established:  

Corollary 3.1  (Sharp uniform-in-time error analysis for SGLD, constant step size    $\eta$  ) .  Con- sider the probability density functions    $\rho_{t},\ \rho_{t}$   for    $X_{t}$  ,  $X_{t}$   deﬁned in  ( 1.3 ) ,  ( 1.7 ) . Suppose  $\eta_{k}=\eta$  ,  $\forall k$  . Then, under Assumption  3.1 ,  3.2 , there exist positive constants    $c$   ,    $\Delta_{0}$   indepen- dent of  t  such that for all    $\eta\in(0,\Delta_{0})$  ,  

$$
\operatorname*{sup}_{t>0}D_{K L}\mathopen{}\mathclose\bgroup\left(\bar{\rho}_{t}||\rho_{t}\aftergroup\egroup\right)\leq c d\eta^{2}.
$$  

Sin  ULA can be viewed as a special case of SGLD when    $b^{\xi}\equiv b$   (or the batch size    $S$  equals  N  for the special case ( 1.2 )), we have the following direct corollary:  

Corollary 3.2  (Sharp uniform-in-time error analysis for ULA, constant time step    $\eta$  ) .  Con- sider the probability density functions    $\rho_{t}$   and    $\hat{\rho}_{t}$   deﬁned in  ( 1.3 ) ,  ( 2.6 ) . Suppos    $\eta_{k}=\eta$  ,  $\forall k$  . Then, under Assumption  3.1 ,  3.2 , there is a positive constant  c  independent of  t  and    $\Delta_{0}>0$  such that for all    $\eta\in(0,\Delta_{0})$  ,  

$$
\operatorname*{sup}_{t>0}D_{K L}\mathopen{}\mathclose\bgroup\left(\hat{\rho}_{t}||\rho_{t}\aftergroup\egroup\right)\leq c d\eta^{2}.
$$  

Based on our main result, Theorem  3.2  or Corollary  3.1 , we are able to obtain the following corollaries, which are useful in many practical tasks.  

First, we choose special case for the decaying time step sequence    $\{\eta_{k}\}_{k=0}^{+\infty}$  , and applying Theorem  3.2 , we obtain the following asymptotic convergence rate:  

Corollary 3.3  (asymptotic rate for special case) .  Suppose Assumption  3.1 ,  3.2  hold. Set  $\eta_{i}\,=\,(\ell+i)^{-\theta}$  ,    $i\in\mathbf{N}$  , with    $\theta\,\in\,(0,1)$   being the decaying coeﬃcient. Here,    $\ell$  is a positive integer such that  $\eta_{\mathrm{0}}\,\leq\,\Delta_{\mathrm{0}}$  here    $\Delta_{0}\,>\,0$  positive constant obtained in Theorem  3.2 . Then there exist  k  $k_{0}>0$  ,  c >  such that  ∀  $\forall k>k_{0}$  ,  

$$
D_{K L}\big(\bar{\rho}_{T_{k}}||\rho_{T_{k}}\big)\leq c d\left(\frac{1}{k}\right)^{2\theta},
$$  

Proof of Corollary  3.3 :  For    $\theta\in(0,1)$  , by Theorem  3.2 , we have  

$$
\begin{array}{r l}&{D_{K L}\big(\bar{\rho}_{T_{k}}||\rho_{T_{k}}\big)\leq c_{1}e^{-A_{0}T_{k}}+c_{2}d\left(\displaystyle\sum_{i=1}^{\lfloor k/2\rfloor}+\displaystyle\sum_{i=1+\lfloor k/2\rfloor}^{k}\right)\left((\ell+i)^{-2\theta}\left(e^{-A_{0}(T_{k}-T_{i})}-e^{-A_{0}(T_{k}-T_{i-1})}\right)\right)}\\ &{\qquad\qquad\qquad\leq c_{1}e^{-A_{0}T_{k}}+c_{2}^{\prime}d\left(e^{-A_{0}(T_{k}-T_{\lfloor k/2\rfloor})}-e^{-A_{0}T_{k}}\right)+c_{2}^{\prime}d\left(\displaystyle\frac{2}{k}\right)^{2\theta}\left(1-e^{-A_{0}(T_{k}-T_{1+\lfloor k/2\rfloor})}\right)}\\ &{\qquad\qquad\qquad\leq c_{1}e^{-A_{0}T_{k}}+c_{2}^{\prime}d e^{-A_{0}(T_{k}-T_{\lfloor k/2\rfloor})}+c_{2}^{\prime}d\left(\displaystyle\frac{2}{k}\right)^{2\theta}.}\end{array}
$$  

As    $k\to+\infty$  ,    $\begin{array}{r}{T_{k}\sim\sum_{i=1}^{k}i^{-\theta}\sim k^{1-\theta}}\end{array}$   ∼ . Hence,    $e^{-A_{0}T_{k}}$   and    $e^{-A_{0}(T_{k}-T_{\lfloor k/2\rfloor})}$   decay much faster than  k  $k^{-2\theta}$    as  k  $k\to+\infty$   → ∞ . Therefore, there exists    $k_{0}>0$   such that when    $k>k_{0}$  ,  

$$
D_{K L}\big(\bar{\rho}_{T_{k}}||\rho_{T_{k}}\big)\leq c d\left(\frac{1}{k}\right)^{2\theta},
$$  

where    $c$   is a positive constant independent of    $k$  . This is what we want.  

# 4 Delayed proof for the local estimation  

In this section, we prove the crucial local analysis result of this paper, Proposition  3.2 . For convenience, the proof is still a high-level overview and more technical details can be found in the Appendix.  

Proof of Proposition  3.2 :  We prove this local result following three main steps.  

STEP 1:  estimate time derivative of KL-divergence  $\begin{array}{r}{\frac{d}{d t}D_{K L}\big(\bar{\rho}_{t}||\rho_{t}\big)}\end{array}$  ) via Fokker-Planck equations.  

Firstly, note that SGLD at discrete time points is a Markov chain (which is time- homogeneous when    $\eta/k$   is a constant), and   $\rho_{T_{k}}$   is the law at    $T_{k}$  . Recall that    $\rho_{t}^{\xi}$    is the probability density of the ﬁxed-batch version of SGLD ( 1.7 ) for a given sequence of batches  $\pmb{\xi}:=(\xi_{0},\xi_{1},\cdot\cdot\cdot\ ,\xi_{k},\cdot\cdot\cdot)$   so that   $\bar{\rho}_{T_{k}}=\mathbb{E}_{\xi}\left[\rho_{T_{k}}^{\xi}\right]$  î ó . Moreover, by Markov property, we are able to deﬁne  

$$
\bar{\rho}_{t}^{\xi_{k}}:=\mathbb{E}\left[\rho_{t}^{\xi}\middle|\xi_{i},\,i\geq k\right]=\mathcal{S}_{T_{k},t}^{\xi_{k}}\bar{\rho}_{T_{k}},\quad t\in[T_{k},T_{k+1}),
$$  

where the operator  $S_{T_{k},t}^{\xi_{k}}$    is the evolution operator from    $T_{k}$   to  $t$   for the Fokker-Planck equation of the continuous SGLD ( 1.7 ) derived in Lemma  2.1 , for some given    $\xi_{k}$  :  

$$
\begin{array}{r}{\partial_{t}\bar{\rho}_{t}^{\xi_{k}}=-\nabla\cdot\bigl(\bar{\rho}_{t}^{\xi_{k}}\bar{b}_{t}^{\xi_{k}}\bigr)+\beta^{-1}\Delta\bar{\rho}_{t}^{\xi_{k}},\quad\bar{\rho}_{T_{k}}^{\xi_{k}}=\bar{\rho}_{T_{k}},}\end{array}
$$  

where    $t\in[T_{k},T_{k+1})$   and  

$$
\bar{b}_{t}^{\xi_{k}}(x):=\mathbb{E}\left[b^{\xi_{k}}\left(\bar{X}_{T_{k}}\right)|\bar{X}_{t}=x,\xi_{k}\right],\quad t\in[T_{k},T_{k+1})\,.
$$  

Next, we calculate  $\begin{array}{r}{\frac{d}{d t}D_{K L}\big(\bar{\rho}_{t}||\rho_{t}\big)}\end{array}$  ) based on ( 4.2 ). Since   $\bar{\rho}_{t}=\mathbb{E}_{\xi_{k}}[\bar{\rho}_{t}^{\xi_{k}}]$  ] for    $t\in[T_{k},T_{k+1})$  , by ( 4.2 ) we have  

$$
\begin{array}{r}{\partial_{t}\bar{\rho}_{t}=\mathbb{E}_{\xi_{k}}\left[-\nabla\cdot\left(\bar{b}_{t}^{\xi_{k}}\bar{\rho}_{t}^{\xi_{k}}\right)+\beta^{-1}\Delta\bar{\rho}_{t}^{\xi_{k}}\right].}\end{array}
$$  

Then, using the Fokker-Planck equations ( 4.4 ), ( 2.4 ) for   $\rho_{t}$   and  $\rho_{t}$  , respectively, we are able to calculate the following time derivative of the KL-divergence in the time interval   $[T_{k},T_{k+1})$  :  

$$
\begin{array}{r l}&{\quad\frac{d}{d t}D_{K L}(\bar{\rho}_{t}||\rho_{t})=\displaystyle\int\left(\partial_{t}\bar{\rho}_{t}\right)\left(\log\frac{\bar{\rho}_{t}}{\rho_{t}}+1\right)d x+\displaystyle\int\left(\partial_{t}\rho_{t}\right)\left(-\frac{\bar{\rho}_{t}}{\rho_{t}}\right)d x}\\ &{=\left(\mathbb{E}_{\xi_{k}}(\bar{b}_{t}^{\xi_{k}}\bar{\rho}_{t}^{\xi_{k}})-\beta^{-1}\nabla\bar{\rho}_{t}\right)\cdot\left(\nabla\log\frac{\bar{\rho}_{t}}{\rho_{t}}\right)+(b\rho_{t}-\beta^{-1}\nabla\rho_{t})\cdot(-\nabla\frac{\bar{\rho}_{t}}{\rho_{t}})d x.}\\ &{=\displaystyle\int\left((b\bar{\rho}_{t}-\beta^{-1}\nabla\bar{\rho}_{t})\cdot\left(\nabla\log\frac{\bar{\rho}_{t}}{\rho_{t}}\right)+(b\rho_{t}-\beta^{-1}\nabla\rho_{t})\cdot\left(-\nabla\frac{\bar{\rho}_{t}}{\rho_{t}}\right)\right)d x}\\ &{\quad+\displaystyle\int\mathbb{E}_{\xi_{k}}\left[(\bar{b}_{t}^{\xi_{k}}-b^{\xi_{k}})\bar{\rho}_{t}^{\xi_{k}}\right]\cdot\left(\nabla\log\frac{\bar{\rho}_{t}}{\rho_{t}}\right)d x+\displaystyle\int\mathbb{E}_{\xi_{k}}\left[b^{\xi_{k}}\bar{\rho}_{t}^{\xi_{k}}-b\bar{\rho}_{t}\right]\cdot(\nabla\log\frac{\bar{\rho}_{t}}{\rho_{t}})d x}\end{array}
$$  

Note that    $|b^{\xi_{k}}\bar{\rho}_{t}^{\xi_{k}}-b\bar{\rho}_{t}|$    − |  is of order    $O(1)$  . The mechanism is that   $\bar{\rho}_{t}^{\xi_{k}}$  is close to   $\rho_{t}$   and using the consistency of random batch    $\mathbb{E}_{\xi_{k}}\,\left[b^{\xi_{k}}(x)\right]\:=\:b(x)$     = ). This can cancel the leading error. Hence, we rearrange the terms to get  

$$
\begin{array}{r l}&{\frac{d}{d t}D_{K L}(\bar{\rho}_{t}||\rho_{t})=\left(-\beta^{-1}\int|\nabla\log\frac{\bar{\rho}_{t}}{\rho_{t}}|^{2}\bar{\rho}_{t}d x\right)+\left(\int\mathbb{E}_{\xi_{k}}\left[(\bar{b}_{t}^{\xi_{k}}-b^{\xi_{k}})\bar{\rho}_{t}^{\xi_{k}}\right]\cdot(\nabla\log\frac{\bar{\rho}_{t}}{\rho_{t}})d x\right)}\\ &{\qquad\qquad\qquad+\left(\int\mathbb{E}_{\xi_{k}}\left[(b^{\xi_{k}}-b)(\bar{\rho}_{t}^{\xi_{k}}-\bar{\rho}_{t})\right]\cdot(\nabla\log\frac{\bar{\rho}_{t}}{\rho_{t}})d x\right)}\\ &{\qquad\qquad\qquad:=J_{1}+J_{2}+J_{3}.}\end{array}
$$  

For    $J_{2}$  , by Young’s inequality,  

$$
\begin{array}{l}{{J_{2}=\mathbb{E}_{\xi_{k}}\left[\displaystyle\int(\bar{b}_{t}^{\xi_{k}}-b^{\xi_{k}})\bar{\rho}_{t}^{\xi_{k}}\cdot(\nabla\log\frac{\bar{\rho}_{t}}{\rho_{t}})d x\right]}}\\ {{\quad\leq\beta\mathbb{E}_{\xi_{k}}\displaystyle\int|\bar{b}_{t}^{\xi_{k}}-b^{\xi_{k}}|^{2}\bar{\rho}_{t}^{\xi_{k}}d x+\frac{1}{4\beta}\displaystyle\int|\nabla\log\frac{\bar{\rho}_{t}}{\rho_{t}}|^{2}\bar{\rho}_{t}d x,}}\end{array}
$$  

where    $\gamma$   is a positive constant.  

For    $J_{3}$  , our approach is to introduce another copy of SGLD   $Y$   such that  

•    $Y_{T_{k}}=X_{T_{k}}$  ; •  the Browmian Motion are the same in   $[T_{k},T_{k+1})$  ; •  the batch   $\tilde{\xi}_{k}$   on   $[T_{k},T_{k+1})$   is independent of    $\xi_{k}$  .  

Consequently, the corresponding density of the law   $\bar{\rho_{t}}^{\ddot{\xi}_{k}}$   for   $Y$   satisfy both ( 4.1 ) and ( 4.2 ), with   $\bar{\rho}_{T_{k}}^{\xi_{k}}=\bar{\rho}_{T_{k}}$  . Using the consistency of the random batch, we are able to obtain  

$$
J_{3}=\mathbb{E}_{\xi_{k},\tilde{\xi}_{k}}\int\Big[\big(b^{\xi_{k}}-b\big)\big(\bar{\rho}_{t}^{\xi_{k}}-\bar{\rho}_{t}^{\tilde{\xi}_{k}}\big)\Big]\cdot\big(\nabla\log\frac{\bar{\rho}_{t}}{\rho_{t}}\big)d x
$$  

Then by Young’s inequality we have:  

$$
J_{3}\leq\beta\mathbb{E}_{\xi_{k},\tilde{\xi}_{k}}\left[\int|b^{\xi_{k}}-b|^{2}\frac{|\bar{\rho}_{t}^{\tilde{\xi}_{k}}-\bar{\rho}_{t}^{\xi_{k}}|^{2}}{\bar{\rho}_{t}^{\tilde{\xi}_{k}}}d x\right]+\frac{1}{4\beta}\int|\nabla\log\frac{\bar{\rho}_{t}}{\rho_{t}}|^{2}\bar{\rho}_{t}d x
$$  

where we applied the fact    $\begin{array}{r}{\mathbb{E}_{\xi_{k},\tilde{\xi}_{k}}|\nabla\log\frac{\bar{\rho}_{t}}{\rho_{t}}|^{2}\bar{\rho}_{t}^{\tilde{\xi_{k}}}\ =\ |\nabla\log\frac{\bar{\rho}_{t}}{\rho_{t}}|^{2}\bar{\rho}_{t}}\end{array}$      . The introduction of the independent copy of  $\ddot{\xi}_{k}$   is useful since we may apply the Girsanov transform later to estimate this quantitatively.  

Now by Theorem  3.1 ,    $\rho_{t}$   satisﬁes a LSI with a constant    $\lambda^{2}C_{\pi}^{L S}$  , namely,    $\forall f\in C_{>0}^{\infty}$  ,  

$$
E n t_{\rho_{t}}(f):=\int f\log f d\rho_{t}-\left(\int f d\rho_{t}\right)\log\left(\int f d\rho_{t}\right)\leq\lambda^{2}C_{\pi}^{L S}\int\frac{|\nabla f|^{2}}{f}d\rho_{t}.
$$  

Taking    $\begin{array}{r}{f=\frac{\bar{\rho}_{t}}{\rho_{t}}}\end{array}$    , one has  

$$
\int|\nabla\log\frac{\bar{\rho}_{t}}{\rho_{t}}|^{2}\bar{\rho}_{t}d x\geq\frac{1}{\lambda^{2}C_{\pi}^{L S}}D_{K L}\bigl(\bar{\rho}_{t}||\rho_{t}\bigr).
$$  

Then, combining ( 4.6 ), ( 4.7 ), ( 4.9 ), and ( 4.11 ), one has  

$$
\begin{array}{r l}&{\displaystyle\frac{d}{d t}D_{K L}\big(\bar{\rho}_{t}||\rho_{t}\big)\leq-A_{0}D_{K L}\big(\bar{\rho}_{t}||\rho_{t}\big)}\\ &{\qquad\qquad\qquad+\beta\,\mathbb{E}_{\xi_{k}}\left[\int|\bar{b}_{t}^{\xi_{k}}-b^{\xi_{k}}|^{2}\bar{\rho}_{t}^{\xi_{k}}d x\right]+\beta\,\mathbb{E}_{\xi_{k},\bar{\xi}_{k}}\left[\int|b^{\xi_{k}}-b|^{2}\frac{|\bar{\rho}_{t}^{\bar{\xi}_{k}}-\bar{\rho}_{t}^{\xi_{k}}|^{2}}{\bar{\rho}_{t}^{\bar{\xi}_{k}}}d x\right],}\end{array}
$$  

where  

$$
A_{0}=\frac{\beta^{-1}}{2\lambda^{2}C_{\pi}^{L S}}>0.
$$  

With ( 4.12 ), to obtain the ﬁnal estimate, one then needs to obtain an    $O(\eta^{2})$   estimate for the two terms:    $\mathbb{E}_{\xi_{k}}\mathbb{E}\left[|\bar{b}_{t}^{\xi_{k}}(\bar{X}_{t})-b^{\xi_{k}}(\bar{X}_{t})|^{2}\Big|\xi_{k}\right]$  h  i and  $\begin{array}{r}{\mathbb{E}_{\xi_{k},\tilde{\xi}_{k}}\left[\int|b^{\xi_{k}}-b|^{2}\frac{\vert\bar{\rho}_{t}^{\xi_{k}}-\bar{\rho}_{t}^{\xi_{k}}\vert^{2}}{\bar{\rho}_{t}^{\tilde{\xi}_{k}}}d x\right]}\end{array}$  .  

STEP 2:  estimate  $\mathbb{E}_{\xi_{k}}\mathbb{E}\left[|\bar{b}_{t}^{\xi_{k}}(\bar{X}_{t})-b^{\xi_{k}}(\bar{X}_{t})|^{2}\Big|\xi_{k}\right]$  

In this step, we aim to obtain an    $O(\eta_{k}^{2})$  ) bound for    $\mathbb{E}_{\xi_{k}}\mathbb{E}\left[|\bar{b}_{t}^{\xi_{k}}(\bar{X}_{t})-b^{\xi_{k}}(\bar{X}_{t})|^{2}\Big|\xi_{k}\right]$  h i based on Taylor expansion for    $b^{\xi_{k}}$  . Note that    $\xi_{k}$   is ﬁxed so we may follow the estimate for the Unadjusted Langevin Algorithm (ULA) in [ 35 ] in this step.  

By Taylor expansion,  $\forall t\in|T_{k},T_{k+1}$  ),  

$$
\begin{array}{l}{\begin{array}{r l}&{\bar{b}_{t}^{\xi_{k}}(x)-b^{\xi_{k}}(x)=\mathbb{E}\left[b^{\xi_{k}}(\bar{X}_{T_{k}})-b^{\xi_{k}}(\bar{X}_{t})|\bar{X}_{t}=x,\xi_{k}\right]}\end{array}}\\ &{=\mathbb{E}[\bar{X}_{T_{k}}-\bar{X}_{t}|\bar{X}_{t}=x,\xi_{k}]\cdot\nabla b^{\xi_{k}}(x)}\\ &{\begin{array}{r l}&{+\displaystyle\cfrac{1}{2}\mathbb{E}\left[\left(\bar{X}_{T_{k}}-\bar{X}_{t}\right)^{\otimes2}:\int_{0}^{1}\nabla^{2}b^{\xi_{k}}\left((1-s)\bar{X}_{t}+s\bar{X}_{T_{k}}\right)d s\Big|\bar{X}_{t}=x,\xi_{k}\right].}\end{array}}\end{array}
$$  

For simplicity, we denote  

$$
\bar{r}_{t}(x):=\frac{1}{2}\mathbb{E}\left[\left(\bar{X}_{T_{k}}-\bar{X}_{t}\right)^{\otimes2}:\int_{0}^{1}\nabla^{2}b^{\xi_{k}}\left((1-s)\bar{X}_{t}+s\bar{X}_{T_{k}}\right)d s\Big|\bar{X}_{t}=x,\xi_{k}\right].
$$  

In Lemma  A.2  , we show that for    $t\in[T_{k},T_{k+1})$  ,  

$$
{\mathbb{E}}\left[|\bar{r}_{t}(\bar{X}_{t})|^{2}\Big|\xi_{k}\right]\leq c d(t-T_{k})^{2},
$$  

where    $c$   is a positive constant independent of    $k$  ,    $d$   and    $\xi_{k}$  . For the ﬁrst term    $\mathbb{E}[X_{T_{k}}-X_{t}|X_{t}=$   − |  $x,\xi_{k}]\cdot\nabla b^{\xi_{k}}(x)$  , by Bayes’ law we have  

$$
\begin{array}{r l r}&{}&{\mathbb{E}[\bar{X}_{T_{k}}-\bar{X}_{t}|\bar{X}_{t}^{\xi}=x,\xi_{k}]=\displaystyle\int(y-x)P(\bar{X}_{T_{k}}=y|\bar{X}_{t}=x,\xi_{k})d y\mathrm{~\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
$$  

Clearly, the distribution    $P(X_{t}=x|X_{T_{k}}=y,\xi_{k})$  | ) is Gaussian, namely,  

$$
P\left({{{\bar{X}}_{t}}=x|{{\bar{X}}_{{{T_{k}}}}}=y,{{\xi_{k}}}}\right)={\left({4\pi{\beta^{-1}}(t-{T_{k}})}\right)^{-{\frac{d}{2}}}}\exp\left({-{\frac{{|x-y-b^{{\xi_{k}}}(y)(t-{T_{k}})|^{2}}}{{4{\beta^{-1}}(t-{T_{k}})}}}}\right),
$$  

which motivates us to calculate ( 4.16 ) via integration by parts. Indeed, we show in Lemma A.3  that  

$$
\int\left|\mathbb{E}\left[\bar{X}_{T_{k}}-\bar{X}_{t}\vert\bar{X}_{t}=x,\xi_{k}\right]\right|^{2}\bar{\rho}_{t}^{\xi_{k}}(x)d x\leq c\eta_{k}^{2}\left(d+\mathcal{I}(\bar{\rho}_{T_{k}})\right),\quad\forall t\in[T_{k},T_{k+1}),
$$  

where  I  $\begin{array}{r}{\mathcal{Z}(\rho):=\int\rho|\nabla\log\rho|^{2}d x}\end{array}$  R  is the Fisher information, and    $c$   is a positive constant inde- pendent of    $k$  ,    $d$   and    $\xi_{k}$  . Then, it is left to give an    $O(1)$   estimate for each Fisher information  $\mathcal{Z}\big(\bar{\rho}_{T_{k}}\big)$  ) in ULA, which has been done in Section  3.2 .  

STEP 3:  estimate  $\begin{array}{r}{\mathbb{E}_{\xi_{k},\tilde{\xi_{k}}}\left[\int|b^{\xi_{k}}-b|^{2}\frac{\vert\bar{\rho}_{t}^{\tilde{\xi}_{k}}-\bar{\rho}_{t}^{\xi_{k}}\vert^{2}}{\bar{\rho}_{t}^{\tilde{\xi}_{k}}}d x\right].}\end{array}$  .  

By the boundedness assumption in Assumption  3.1 , we only need to estimate  $\begin{array}{r}{\int\frac{\vert\bar{\rho}_{t}^{\xi_{k}}-\bar{\rho}_{t}^{\xi_{k}}\vert^{2}}{\bar{\rho}_{t}^{\xi_{k}}}d x}\end{array}$  . Recall that  $\bar{\rho}_{t}^{\xi_{k}}$    and   $\bar{\rho}_{t}^{\xi_{k}}$    are the densities of the laws of X  and  $Y$   with two independent batches  $\xi_{k}$   and  $\tilde{\xi}_{k}$   for interval   $[T_{k},T_{k+1})$  . Hence the problem is again reduced to the ULA case.  

We ﬁrst note that  

$$
\int\frac{|\bar{\rho}_{t}^{\tilde{\xi}_{k}}-\bar{\rho}_{t}^{\xi_{k}}|^{2}}{\bar{\rho}_{t}^{\tilde{\xi}_{k}}}d x=\int\left|\frac{\bar{\rho}_{t}^{\xi_{k}}}{\bar{\rho}_{t}^{\tilde{\xi}_{k}}}-1\right|^{2}\bar{\rho}_{t}^{\tilde{\xi}_{k}}d x,
$$  

and the property of path measures gives  

$$
\frac{\bar{\rho}_{t}^{\xi_{k}}}{\bar{\rho}_{t}^{\tilde{\xi}_{k}}}(x)=\mathbb{E}\left[\frac{d P_{\bar{X}}}{d P_{\bar{Y}}}\Bigg|\bar{Y}_{t}=x,\xi_{k},\tilde{\xi}_{k}\right],
$$  

where    $P_{\bar{X}}$    and    $P_{\bar{Y}}$    are path measures in    $C\left([T_{k},T_{k+1}];\mathbb{R}^{d}\right)$  . Let  

$$
\bar{X}_{T_{k}}=\bar{Y}_{T_{k}}=y\sim\bar{\rho}_{T_{k}}.
$$  

Then for    $t\in[T_{k},T_{k+1})$  , Girsanov transform gives:  

$$
\frac{d P_{\bar{X}}}{d P_{\bar{Y}}}(\bar{Y})=\exp{\left(\sqrt{\frac{\beta}{2}}\int_{T_{k}}^{T_{k+1}}(b^{\tilde{\xi}_{k}}-b^{\xi_{k}})(y)d W_{s}-\frac{\beta}{4}\int_{T_{k}}^{T_{k+1}}\left|(b^{\tilde{\xi}_{k}}-b^{\xi_{k}})(y)\right|^{2}d s\right)}\,.
$$  

Details for ( 4.20 ) and ( 4.21 ) can be found in Corollary  A.1  of Appendix  A . Denote  

$$
\tilde{b}(y):=\frac{1}{\sqrt{2\beta^{-1}}}\left(b^{\tilde{\xi}_{k}}-b^{\xi_{k}}\right)(y).
$$  

Then, for    $t\in[T_{k},T_{k+1})$  , the martingale property gives  

$$
\overline{{\rho}}_{t}^{\xi_{k}}(x)=\mathbb{E}\left[\exp{\left(\int_{T_{k}}^{t}\tilde{b}(y)d W_{s}-\frac{1}{2}\int_{T_{k}}^{t}|\tilde{b}(y)|^{2}d s\right)}\Bigg|\bar{Y}_{t}=x,\xi_{k},\tilde{\xi}_{k}\right].
$$  

Hence,  

$$
\begin{array}{r l}&{\quad\int\left|\frac{\bar{\rho}_{t}^{\xi_{k}}}{\bar{\rho}_{t}^{\xi_{k}}}-1\right|^{2}\bar{\rho}_{t}^{\xi_{k}}d x}\\ &{=\int\bar{\rho}_{t}^{\xi_{k}}(x)\left|\mathbb{E}\left[e^{\int_{T_{k}}^{t}\bar{b}(\bar{Y}_{T_{k}})d W_{s}-\frac{1}{2}\int_{T_{k}}^{t}|\bar{b}(\bar{Y}_{T_{k}})|^{2}d s}\Big|\bar{Y}_{t}=x,\xi_{k},\tilde{\xi}_{k}\right]-1\right|^{2}d x}\\ &{=\int\bar{\rho}_{t}^{\xi_{k}}(x)\left|\int\left(e^{\sqrt{\frac{a}{2}}\,\bar{b}(y)(x-y-(t-T_{k})b^{\xi_{k}}(y))-\frac{1}{2}|\bar{b}(y)|^{2}(t-T_{k})}-1\right)P(\bar{X}_{T_{k}}=y|\bar{Y}_{t}=x,\xi_{k},\tilde{\xi}_{k})d y\right|^{2}d x}\end{array}
$$  

Above we have used the fact that   $\bar{Y}_{t}=y+b^{\xi_{k}}(y)(t-T_{k})+\sqrt{2\beta^{-1}}(W_{t}-W_{T_{k}})$   − p  − ), resulting in that  

$$
\sqrt{2\beta^{-1}}(W_{t}-W_{T_{k}})=x-y-b^{\tilde{\xi}_{k}}(y)(t-T_{k}).
$$  

$e^{\sqrt{\frac{\beta}{2}}\tilde{b}(y)(x-y-(t-T_{k})b^{\tilde{\xi}_{k}}(y))-\frac{1}{2}|\tilde{b}(y)|^{2}(t-T_{k})}$  √ Now in order to handle the integration of the term  e , we split it by  

$$
\begin{array}{r l}&{\quad e^{\sqrt{\frac{\beta}{2}}\,\widetilde{b}(y)(x-y-(t-T_{k})b^{\widetilde{\xi}_{k}}(y))-\frac{1}{2}|\widetilde{b}(y)|^{2}(t-T_{k})}-1}\\ &{=\sqrt{\frac{\beta}{2}}\,\widetilde{b}(y)(x-y)+\left(-\sqrt{\frac{\beta}{2}}\,\widetilde{b}(y)b^{\widetilde{\xi}_{k}}(y)-\frac{1}{2}|\widetilde{b}(y)|^{2}\right)(t-T_{k})+\left(e^{z}-z-1\right)}\\ &{:=K_{1}+K_{2}+K_{3},}\end{array}
$$  

where  

$$
z:=\sqrt{\frac{\beta}{2}}\,\widetilde{b}(y)(x-y-(t-T_{k})b^{\widetilde{\xi}_{k}}(y))-\frac{1}{2}|\widetilde{b}(y)|^{2}(t-T_{k}).
$$  

Then  

$$
\int\left|\frac{\bar{\rho}_{t}^{\xi_{k}}}{\bar{\rho}_{t}^{\xi_{k}}}-1\right|^{2}\bar{\rho}_{t}^{\xi_{k}}d x=\int\bar{\rho}_{t}^{\xi_{k}}(x)\left|\int\left(K_{1}+K_{2}+K_{3}\right)P(\bar{X}_{T_{k}}=y|\bar{Y}_{t}=x,\xi_{k},\tilde{\xi}_{k})d y\right|^{2}d x.
$$  

For    $\begin{array}{r}{K_{1}=\sqrt{\frac{\beta}{2}}\,\widetilde{b}(y)(x-y)}\end{array}$  » ), using integration by parts again, we prove in Lemma  A.4  in Section  A  that for    $t\in|T_{k},T_{k+1}$  ),  

$$
\int\bar{\rho}_{t}^{\tilde{\xi}_{k}}(x)\left(\int K_{1}\,P(\bar{X}_{T_{k}}=y|\bar{Y}_{t}=x,\xi_{k},\tilde{\xi}_{k})d y\right)^{2}d x\leq c\eta_{k}^{2}\left(d+\mathcal{I}(\bar{\rho}_{T_{k}})\right).
$$  

where    $c$   is a positive constant independent of    $k$  ,    $d$  ,  $\tilde{\xi_{k}}$   and    $\xi_{k}$  

For    $\begin{array}{r}{K_{2}=(-\sqrt{\frac{\beta}{2}}\,\widetilde{b}(y)\cdot b^{\widetilde{\xi}_{k}}(y))-\frac{1}{2}|\widetilde{b}(y)|^{2})(t-T_{k})}\end{array}$  » ), using the boundedness and Lipshitz condition in Assumption  3.1 , we prove in Lemma  A.5  that for    $t\in[T_{k},T_{k+1})$  ,  

$$
\int\bar{\rho}_{t}^{\tilde{\xi}_{k}}(x)\left(\int K_{2}\,P(\bar{X}_{T_{k}}=y|\bar{Y}_{t}=x,\xi_{k},\tilde{\xi}_{k})d y\right)^{2}d x\leq c d\eta_{k}^{2},
$$  

where    $c$   is a positive constant independent of    $k$  ,    $d$  ,   $\ddot{\xi}_{k}$   and    $\xi_{k}$  

For the remaining term    $K_{3}$  , after applying Jensen’s inequality and the tower property of conditional expectation, we prove in Lemma  A.6  that for    $t\in[T_{k},T_{k+1})$  ),  

$$
\int\bar{\rho}_{t}^{\tilde{\xi}_{k}}(x)\left(\int K_{3}\,P(\bar{X}_{T_{k}}=y|\bar{Y}_{t}=x,\xi_{k},\tilde{\xi}_{k})d y\right)^{2}d x\leq c d\eta_{k}^{2}.
$$  

where    $c$   is a positive constant independent of    $k$  ,    $d$  ,   $\ddot{\xi}_{k}$   and    $\xi_{k}$  

Equipped with the estimation for the integration of    $K_{1}$  ,    $K_{2}$  , and    $K_{3}$  , one ﬁnally obtains  

$$
\int\left|\frac{\bar{\rho}_{t}^{\xi_{k}}}{\bar{\rho}_{t}^{\xi_{k}}}-1\right|^{2}\bar{\rho}_{t}^{\xi_{k}}d x\leq c\eta_{k}^{2}\left(1+\mathcal{I}(\bar{\rho}_{T_{k}})\right),\quad\forall t\in[T_{k},T_{k+1}),
$$  

where    $c$   is a positive constant independent of    $k$  ,    $d$  ,   $\ddot{\xi}_{k}$   and    $\xi_{k}$  . Combining with the estimate for Fisher information obtained in Section  3.2 , one is able to get an    $\eta_{k}^{2}$    estimation for the term  $\begin{array}{r}{\mathbb{E}_{\xi_{k},\tilde{\xi}_{k}}\left[\int|b^{\xi_{k}}-b|^{2}\frac{|\bar{\rho}_{t}^{\xi_{k}}-\bar{\rho}_{t}^{\xi_{k}}|^{2}}{\bar{\rho}_{t}^{\tilde{\xi}_{k}}}d x\right]}\end{array}$  ò . Note that after taking the expectation    $\mathbb{E}_{\xi_{k},\tilde{\xi}_{k}}[\cdot]$  ], the  

Combining the results in STEP 2 and STEP 3 ﬁnally leads to the desired result:  

$$
\frac{d}{d t}D_{K L}\big(\bar{\rho}_{t}||\rho_{t}\big)\leq-A_{0}D_{K L}\big(\bar{\rho}_{t}||\rho_{t}\big)+A_{1}d\eta_{k}^{2}\,\big(1+\mathcal{Z}(\bar{\rho}_{T_{k}})\big)\,,\quad\forall t\in[T_{k},T_{k+1}),
$$  

where    $A_{0}$  ,    $A_{1}$   are positive constants independent of    $k$  ,    $d$  , and    $\xi_{k}$  .  

# 5 Discussion  

# 5.1 Convergence to equilibrium and target distribution  

•  Convergence to the target distribution  

Viewing SGLD as a popular sampling algorithm, many researchers would care about the convergence rate to the target distribution. An important extension of Theorem 3.2  or Corollary  3.1  is about the distance between the SGLD iteration and the target distribution, namely, the invariant distribution of the Langevin diﬀusion ( 1.3 ). When we are doing sampling tasks, this result is an important measure for the eﬃciency of a sampling algorithm. Note that the rate in our result can be viewed as a great improvement compared with former work like [ 36 ,  53 ,  16 ], where the optimal bound so far is of order    $O({\sqrt{\eta}})$   in terms of Wasserstein distance or total variation. Meanwhile, as will be derived in the followings, we obtain a bound of order    $O(\eta)$  .  

To compare our result with former ones more directly, we consider the constant step size (or learning rate)  $\eta$  . We consider the Wasserstein-2 (  $W_{2}$  ) distance, the Wasserstein- 1 (  $W_{1}$  ) distance, and the total variation (TV) distance in the following discussion. Firstly let us recall the deﬁnition of    $W_{p}$   distance (  $p\,=\,1,2$   here) and TV distance between two distributions    $\mu$   and    $\nu$   [ 45 ]:  

$$
W_{p}(\mu,\nu):=\left(\operatorname*{inf}_{\gamma\in\Pi(\mu,v)}\int_{\mathbb{R}^{d}\times\mathbb{R}^{d}}|x-y|^{p}d\gamma\right)^{1/p},
$$  

and  

$$
D_{T V}(\mu,\nu):=\operatorname*{sup}_{A\in\mathcal{B}(\mathbb{R}^{d})}|\mu(A)-\nu(A)|.
$$  

Here,   $\Pi(\mu,\nu)$   means all joint distributions whose marginal distributions are    $\mu$   and    $\nu$  , respectively.  

Now, by Corollary  3.1 , we have  

$$
\begin{array}{r}{D_{K L}\big(\bar{\rho}_{t}||\rho_{t}\big)\leq c d\eta^{2},\quad t>0,}\end{array}
$$  

where    is independent of    $t$  , and    is the constant step size (or learning rate).  $c$   $\eta$  

Also, since the invariant distribution    $\pi$   satisﬁes a Log-Sobolev inequality by Assump- tion  3.2 , we have the following exponential convergence for the Langevin diﬀusion ( 1.3 ), which is a classical result [ 34 ]:  

$$
D_{K L}(\rho_{t}||\pi)\leq e^{-\gamma t}D_{K L}(\rho_{0}||\pi)
$$  

It is well-known that we can bound the    $W_{2}$  ,    $W_{1}$  , and TV distance with square root of the KL-divergence by Talagrand transportation inequality [ 39 ,  48 ], the weighted Csiszar-Kullback-Pinsker inequality [ 6 ], and the Pinsker’s inequality [ 42 ], respectively. Note that for    $W_{2}$   distance and TV distance, the constant  $c_{1}^{\prime}$    above is dimension-free; for  $W_{1}$   distance, the constant    $c_{1}^{\prime}$    above is of    $O(d^{\frac{1}{2}})$   ). Together with the triangle inequality for    $W_{2}$  ,    $W_{1}$  , and TV distances, one has the following:  

Corollary 5.1.  Consider the probability density functions    $\rho_{t}$  ,    $\rho_{t}$  t  for    $X_{t}$  ,  $X_{t}$  t  deﬁned in  ( 1.3 ) ,  ( 1.7 ) . Suppose Assumption  3.1 ,  3.2  hold. Then the following holds:  

(a) If    $\eta_{k}=\eta$  ,    $\forall k$  , then the e exi  positive constants    $c_{1}^{W_{1}}$  ,    $c_{2}^{W_{1}}$  ,    $c_{1}^{W_{2}}$  ,    $c_{2}^{W_{2}}$  ,    $c_{1}^{T V}$  ,    $c_{2}^{T V}$  ,  $\gamma$   ,    $\Delta_{0}$   independent of  t  and  d  such that for all    $\eta\in(0,\Delta_{0})$  ,  

$$
\begin{array}{r l}&{*\ W_{1}(\bar{\rho}_{t},\pi)\leq c_{1}^{W_{1}}d\eta+c_{2}^{W_{1}}d^{\frac{1}{2}}e^{-\frac{1}{2}\gamma t},}\\ &{*\ W_{2}(\bar{\rho}_{t},\pi)\leq c_{1}^{W_{2}}d^{\frac{1}{2}}\eta+c_{2}^{W_{2}}e^{-\frac{1}{2}\gamma t},}\\ &{*\ D_{T V}(\bar{\rho}_{t},\pi)\leq c_{1}^{T V}d^{\frac{1}{2}}\eta+c_{2}^{T V}e^{-\frac{1}{2}\gamma t}.}\end{array}
$$  

(b) If    $\eta_{i}\,=\,(\ell+i)^{-\theta}$  w  $\theta\,\in\,(0,1)$   being  he de y rate, then there exist positive constants  c  $c^{W_{1}}$  ,  c  $c^{W_{2}}$  ,  c  $c^{T V}$    independent of  k  and  d  such that  

$$
\begin{array}{r l}&{*\,\,\,W_{1}(\bar{\rho}_{T_{k}},\pi)\leq c^{W_{1}}d\left(\frac1k\right)^{\theta},}\\ &{*\,\,\,W_{2}(\bar{\rho}_{T_{k}},\pi)\leq c^{W_{2}}d^{\frac12}\left(\frac1k\right)^{\theta},}\\ &{*\,\,\,D_{T V}(\bar{\rho}_{T_{k}},\pi)\leq c^{T V}d^{\frac12}\left(\frac1k\right)^{\theta}.}\end{array}
$$  

By Corollary  5.1 , we can conclude the steps of simulations for SGLD needed to achieve a tolerance    $\epsilon$   under diﬀerent distances.  

Corollary 5.2.  Under Assumption  3.1 ,  3.2 , to achieve an error smaller than    $\epsilon$  , one needs the following numbers of simulations of SGLD respectively under the correspond- ing distances:  

These results are improved compared to existing results in literature.  

# •  Ergodicity of SGLD  

An important property of SGLD that remains to be studied is its ergodicity, which then ensures the existence of the invariant distribution of the SGLD dynamic and enables us to explore the convergence of the algorithm itself. In [ 7 ], the authors considered the ergodicity of SGLD under  $W_{2}$   distance with the assumptions of global strong convexity of    $U$   and 4-th order Lipshitz condition.  

In our setup, we do not have the global strong convexity of    $U$   and only have second order Lipschitz condition. Luckily, the ergodicity could be studied using reﬂection coupling [ 14 ,  24 ], under mild assumptions. In particular, we have the following claim. In fact, we need to assume the followings, which can be understood as the positive upper and lower bound of    $\nabla^{2}U$   outside the circle    $B(0,R)$   in    $\mathbb{R}^{d}$  .  

Assumption 5.1.  There exist    $R_{0}>0$  ,    $\kappa_{\mathrm{0}}>0$  ,    $K>0$   such that the followings hold:  

(a) (locally nonconvex) The Hessian matrix of    $U$   is uniformly positive deﬁnite outside  $B(0,R_{0})$  , namely,  

$$
\nabla^{2}U(\boldsymbol{x})\succeq\kappa_{0}I_{d},\quad\forall\boldsymbol{x}\in\mathbb{R}^{d}\setminus B(0,R_{0});
$$  

(b) (global uniform-in-batch Lipshitz)    $\forall x,y\in\mathbb{R}^{d}$  ,    $\forall\xi$  ,  

$$
\begin{array}{r}{\left|\nabla U^{\xi}(x)-\nabla U^{\xi}(y)\right|\leq K|x-y|^{2}.}\end{array}
$$  

Then the following claim holds.  

Proposition 5.1.  Suppose Assumption  5.1  holds. Denote    $\Delta_{0}:=\mathrm{sup}_{k}\,\eta_{k}$  . There exist positive constants ∆ ,    $c_{0}$  ,    $c_{1}$   such that if    $\Delta_{0}<\Delta$  , then for any two initial distributions  $\mu_{0}$   and    $\nu_{0}$  , denoting    $\mu_{t}$   and    $\nu_{t}$   to be the corresponding time marginal distributions for the time continuous interpolation of   $S G L D$   algorithm  ( 1.7 ) , it holds that  

$$
W_{1}\big(\bar{\mu}_{T_{k}},\bar{\nu}_{T_{k}}\big)\leq c_{0}e^{-c_{1}T_{k}}W_{1}\big(\mu_{0},\nu_{0}\big).
$$  

Consequently, if the step size (or learning rate) is constant    $\eta_{k}~\equiv~\eta$   such that the discrete chain is time-homogeneous, then the SGLD as a discrete time Markov chain has an invariant measure  π  by the Banach contraction mapping theorem. Then, we have the following conclusion  

Corollary 5.3.  L  $\eta_{k}=\eta$  . Under Assumption  5.1 , there exist positive constants   ∆ ,  $c_{0}$  ,    $c_{1}$  h that if  $\eta\leq\Delta$   ≤ , then for any initial distribution    $\rho_{0}$   with ﬁnite ﬁrst moment, the SGLD iteration has an invariant measure   π  time marginal distribution    $\rho_{t}$   of  ( 1.7 ) convergences exponentially to   π  in terms of W-1 distance:  

$$
W_{1}(\bar{\rho}_{n\eta},\tilde{\pi})\le c_{0}e^{-c n\eta}W_{1}(\rho_{0},\tilde{\pi}).
$$  

Equipped with the ergodicity results for SGLD and combining the results in Corollary 5.1 , we are able to estimate the distance between the target distribution and the invariant distribution of SGLD itself:  

$$
W_{1}(\tilde{\pi},\pi)\leq c\eta.
$$  

This is improved compared to existing results in literature. Detailed derivation can be found in [ 1 ].  

# 5.2 Other discussions  

# •  Justiﬁcation of sharpness  

A natural question for our results is: is this bound we obtained really a “sharp” one? To answer this question, we simply consider the following Ornstein-Uhlenbeck (O-U) process in    $\mathbb{R}^{1}$  , which satisﬁes all our assumptions.  

$$
d X=-X d t+d W.
$$  

Its solution has an explicit expression:  

$$
X_{t}=e^{-t}X_{0}+\int_{0}^{t}e^{s-t}d W_{s}.
$$  

Consider the full-batch SGLD, namely, the Euler-Maruyama scheme for ( 5.10 ) with constant step size    $\eta$  :  

$$
\begin{array}{r}{\hat{X}_{T_{k+1}}=\hat{X}_{T_{k}}-\eta\hat{X}_{T_{k}}+\bigl(W_{T_{k+1}}-W_{T_{k}}\bigr).}\end{array}
$$  

Suppose    $X_{t}$  ,  $\hat{X}_{t}$   are Gaussion, and    $\mathbb{E}[X_{0}]\neq0$  , then we are able to calculate the KL- divergence without much diﬃculty. Indeed, by deﬁnition, at    $T:=k\eta$  , their mean and variance are given by  

$$
\mu_{1}:=\mathbb{E}\left[X_{T}\right]=e^{-T}\mathbb{E}\left[X_{0}\right],
$$  

$$
\sigma_{1}^{2}:=\mathrm{Var}(X_{T})=e^{-2T}\mathrm{Var}(X_{0})+\frac{1}{2}\left(1-e^{-2T}\right),
$$  

and  

$$
\mu_{2}:=\mathbb{E}\left[\hat{X}_{T}\right]=(1-\eta)^{(T/\eta)}\mathbb{E}\left[X_{0}\right],
$$  

$$
\sigma_{2}^{2}:=\mathrm{Var}(\hat{X}_{T})=(1-\eta)^{2(T/\eta)}\mathrm{Var}(X_{0})+\frac{1}{2-\eta}\left(1-(1-\eta)^{2(T/\eta)}\right).
$$  

Clearly, for small    $\eta$  ,  

$$
\begin{array}{c}{{|\mu_{1}-\mu_{2}|=|\mathbb{E}\left[X_{0}\right]|\left(e^{-T}-{\left(1-\eta\right)^{(T/\eta)}}\right)\geq|\mathbb{E}\left[X_{0}\right]|\left(e^{-t}-e^{-t-t\eta/2}\right)}}\\ {{\mathrm{}}}\\ {{\mathrm{}}}\\ {{\mathrm{}}}\\ {{\mathrm{}}}\\ {{\mathrm{}}}\end{array}
$$  

and    $\sigma_{2}^{2}<2\sigma_{1}^{2}$  .  

Also by direct calculation, the KL-divergence between two Gaussian distributions  $N(\mu_{1},\sigma_{1}^{2})$  ),    $N(\mu_{2},\sigma_{2}^{2})$  ) is given by  

$$
\begin{array}{c}{{D_{K L}\left(N(\mu_{1},\sigma_{1}^{2})||N(\mu_{2},\sigma_{2}^{2})\right)=\left(\displaystyle\frac12\log\frac{\sigma_{2}^{2}}{\sigma_{1}^{2}}+\displaystyle\frac12\left(\frac{\sigma_{1}^{2}}{\sigma_{2}^{2}}-1\right)\right)+\frac{(\mu_{1}-\mu_{2})^{2}}{2\sigma_{2}^{2}}}}\\ {{\geq0+\displaystyle\frac{(\mu_{1}-\mu_{2})^{2}}{2\sigma_{2}^{2}}.}}\end{array}
$$  

Therefore,  

$$
D_{K L}(\bar{\rho}_{T}||\rho_{T})\geq\frac{(1/16)\left|\mathbb{E}\left[X_{0}\right]\right|^{2}e^{-2T}T^{2}}{4\sigma_{1}(T)^{2}}\,\eta^{2}.
$$  

This then indicates that our    $\eta^{2}$    bound is a sharp one.  

# •  The role of consistency of random batch technique  

As a variant of ULA, the key diﬀerence of SGLD is the introduction of the mini- batch technique, which reduces the computational cost. To understand the error and mechanism for the sharp error estimate, let us take    $\eta_{k}\equiv\eta$  .  

For each single step, the error of the drift is    $O(1)$  . The methods involving random batches (such as the SGD and the random batch methods) have a strong error like (see for example [ 22 ])  

$$
\sqrt{\mathbb{E}\|X-\bar{X}\|^{2}}\sim\sqrt{(e^{k\eta}-1)\eta}.
$$  

Clearly, the strong error decays like    $\sqrt{\eta}$  , which is actually sharp. As mentioned in [ 22 ], the averaging eﬀect in time ensures a convergence like ”law of large numbers” in time so the convergence rate is    $\sqrt{\eta}$  . The strong error estimate can imply that  

$$
(\mathbb{E}_{\xi}W_{2}^{2}(\rho_{t}^{\pmb{\xi}},\rho_{t}))^{1/2}\sim\sqrt{(e^{k\eta}-1)\eta}.
$$  

This indicates that the ﬂuctuation of the trajectory and    $\rho_{t}^{\pmb\xi}$    is really like    $\sqrt{\eta}$  . Hence, the existing error estimates of SGLD based on the trajectory estimates can achieve  $\sqrt{\eta}$   at most. Moreover, such an estimate based on trajectory estimate can only give an    $O(\eta)$   one step error of the SGLD under Wasserstein distance (the    $O({\sqrt{\eta}})$   global error is due to the time averaging over multiple intervals).  

The most important property of the random batch is its consistency:  

$$
\begin{array}{r}{\mathbb{E}_{\xi}\left[b^{\xi}(x)\right]=b(x),}\end{array}
$$  

which can be interpreted as an unbiased approximation of the original drift function, as has been mentioned in ( 1.1 ). Consider one step. Starting from a common    $\rho_{0}$  , after one step, formally each    $\rho_{\eta}^{\xi}$    has the following expression  

$$
\rho_{\eta}=\rho_{0}+\eta\mathcal{L}_{\xi}^{*}\rho_{0}+O(\eta^{2}),
$$  

where    $\mathcal{L}_{\xi}$   is the generator corresponding to batch    $\xi$  , while  

$$
\rho_{\eta}=\rho_{0}+\eta\mathcal{L}^{*}\rho_{0}+O(\eta^{2}).
$$  

Hence, the error is like    $O(\eta)$  . Since the error of the drift can cancel if one takes average across batches and thus one is motivated to take the average of all possible    $\rho_{t}^{\xi}$    :  

$$
\bar{\rho}_{t}=\mathbb{E}_{\xi}\left[\rho_{t}^{\pmb\xi}\right],
$$  

which is the true law of the SGLD. The obtained   $\rho_{t}$  t  is then expected to have    $O(\eta^{2})$  local error compared to    $\rho_{t_{n+1}}$  . Of course, direct proof using Wasserstein distances has some diﬃculty and we make use of the KL divergence to accomplish the proof motivated by the recent work [ 35 ]. Anyway, this intuition lays the foundation of our proof and is reﬂected in treating the terms in ( 4.5 ). In fact, the last term in ( 4.5 ), or    $b^{\xi_{k}}\bar{\rho}_{t}^{\xi_{k}}-b\bar{\rho}_{t}$    − , can be as    $O(1)$  . The intuition is that the averaged drift should be    $b$  and one may cancel the error:    $\mathbb{E}(b^{\xi_{k}})\rho_{t}^{\xi_{k}}-b\bar{\rho}_{t}$    −  is small and one may have convergence. With this intuition, we rearrange  

$$
b^{\xi_{k}}\bar{\rho}_{t}^{\xi_{k}}-b\bar{\rho}_{t}=\mathbb{E}(b^{\xi_{k}}-b)(\bar{\rho}_{t}^{\xi_{k}}-\bar{\rho}_{t})
$$  

in ( 4.6 ).  

At last, we remark that though   $\rho_{t}$   is close to    $\rho_{t}$  , in practice we do not repeat the experiment for many times and take the average. Instead, we only generate a sequence the batches   $\left(\xi^{0},\cdot\cdot\cdot\ ,\xi^{k},\cdot\cdot\cdot\right)$   and generate the samples. Even though we use a single  $b^{\xi_{k}}$    each step, the empirical distribution by the generated samples converges weakly to the invariant measure with error    $O(\eta)$   under Wasserstein distance to the interested distribution, due to the ergodicity of SGLD. Hence, one does not have to run SGLD for many experiments to approximate   $\rho_{t}$   and further to approximate the invariant distribution with error    $O(\eta)$  .  

# •  Dependence on the dimensionality  

The linear scaling with respect to    $d$   arising in ( 3.17 ) and ( 3.19 ) is quite natural for the entropy and Fisher information. In fact, if one considers cases where the dynamics in diﬀerence dimensions are decouple so that    $\begin{array}{r}{\rho_{t}(x)=\prod_{i=1}^{d}\rho_{t}^{(i)}(x_{i})}\end{array}$  ), the dependence on dimension in the entropy and Fisher information would be linear.  

As we have mentioned, the linear dependence in the our error bounds largely comes from with the factor    $d^{-1/2}$    in the Lipschitz constant in Assumption  3.1 , and we have justiﬁed this below Assumption  3.1 . A slight discrepancy of this intuition comes from  $D_{K L}(\rho_{0}||\pi)$  , which by by condition (a) in Assumption  3.2  satisﬁes  

$$
\begin{array}{r}{D_{K L}(\rho_{0}||\pi)\leq\log\lambda.}\end{array}
$$  

This independence of the dimension is a consequence of the strong assumption As- sumption  3.2 . However, if we use a weaker assumption like    $\rho_{0}/\pi\leq\lambda^{d}$  , there would be dimension dependence in the constant for log-Sobolev inequality of the Hooley-Stroock perturbation lemma. This may indicate that the Hooley-Stroock perturbation lemma is not sharp regarding the scalability in    $d$  .  

# 6 Acknowledgement  

This work is ﬁnancially supported by the National Key R&D Program of China, Project Number 2021YFA1002800 and Project Number 2020YFA0712000. The work of L. Li was partially supported by NSFC 11901389 and 12031013, Shanghai Municipal Science and Technology Major Project 2021SHZDZX0102, Shanghai Science and Technology Commis- sion Grant No. 21JC1402900, and Shanghai Sailing Program 19YF1421300.  

# A Omitted details in Section  3  and  4  

In this section, we prove the details omitted in Section  3  and  4 . Lemma  A.2 ,  A.3  have been proved in [ 35 ].  

# A.1 Proof of Proposition  3.1  

The method for bounding the    $p$  -th moment of ﬁxed-batch SGLD is based on direct Itˆ calculation a sic inequalities. In the followings, we denote    $\mathcal{F}_{\xi}$   the    $\sigma$  -algebra generated by    $\xi_{k}$   for all  k  $k\in\mathbb N$   ∈ N .  

Proof of Proposition  3.1 :  By deﬁnition, for ﬁxed batch sequence    $\xi$  ,  

$$
l\bar{X}_{t}=b^{\xi_{k}}\big(\bar{X}_{T_{k}}\big)d t+\sqrt{2\beta^{-1}}d W,\quad t\in[T_{k},T_{k+1})\,,
$$  

where we recall    $\begin{array}{r}{T_{k}=\sum_{i=0}^{k-1}\eta_{i}}\end{array}$  . For    $p\geq2$  , by It o’s formula, we have  

$$
\begin{array}{r l}&{d|\bar{X}_{t}|^{p}=p|\bar{X}_{t}|^{p-2}\bar{X}_{t}\cdot\left(b^{\xi}(\bar{X}_{T_{k}})d t+\sqrt{2\beta^{-1}}d W\right)}\\ &{\qquad\qquad\qquad\qquad\qquad+\beta^{-1}p|\bar{X}_{t}|^{p-2}\left(I_{d}+(p-2)\frac{\bar{X}_{t}\otimes\bar{X}_{t}}{|\bar{X}_{t}|^{2}}\right):I_{d}d t.}\end{array}
$$  

So  

$$
\begin{array}{l}{\displaystyle\frac{d}{d t}\mathbb E\left[|\bar{X}_{t}|^{p}\Big|\mathcal F_{\xi}\right]\leq p\mathbb E\left[|\bar{X}_{t}|^{p-2}\bar{X}_{t}\cdot b^{\xi_{k}}(\bar{X}_{t})\Big|\mathcal F_{\xi}\right]}\\ {\displaystyle\qquad+\,p\mathbb E\left[|\bar{X}_{t}|^{p-2}\bar{X}_{t}\cdot\left(b^{\xi_{k}}(\bar{X}_{T_{k}})-b^{\xi_{k}}(\bar{X}_{t})\right)\Big|\mathcal F_{\xi}\right]+\beta^{-1}p(p-1)d\mathbb E\left[|\bar{X}_{t}|^{p-2}\Big|\mathcal F_{\xi}\right].}\end{array}
$$  

Using the dissipation condition in Assumption  3.1 , we can control the ﬁrst term above, namely,  

$$
p\mathbb{E}\left[\left.|\bar{X}_{t}|^{p-2}\bar{X}_{t}\cdot b^{\xi_{k}}(\bar{X}_{t})\right|\mathcal{F}_{\xi}\right]\lesssim-p\mathbb{E}\left[\left.|\bar{X}_{t}|^{p}\right|\mathcal{F}_{\xi}\right]+p\mathbb{E}\left[\left.|\bar{X}_{t}|^{p-2}\right|\mathcal{F}_{\xi}\right].
$$  

By Young’s inequality, for any  $\delta>0$   0,  

$$
\mathbb{E}\left[\left|\bar{X}_{t}\right|^{p-2}\middle|\mathcal{F}_{\xi}\right]\leq\delta d^{-1}\frac{p-2}{p}\mathbb{E}\left[\left|\bar{X}_{t}\right|^{p}\middle|\mathcal{F}_{\xi}\right]+\delta^{-\frac{p-2}{2}}d^{\frac{p-2}{2}}\frac{2}{p}
$$  

For the second term, direct estimate gives  

$$
\begin{array}{r l}&{\quad\mathbb{E}\left[|\bar{X}_{t}|^{p-2}\bar{X}_{t}\cdot\left(b^{\xi_{k}}(\bar{X}_{T_{k}})-b^{\xi_{k}}(\bar{X}_{t})\right)\Big|\mathcal{F}_{\xi}\right]\leq c\mathbb{E}\left[|\bar{X}_{t}|^{p-1}|\bar{X}_{t}-\bar{X}_{T_{k}}|\Big|\mathcal{F}_{\xi}\right]}\\ &{\lesssim(t-T_{k})\mathbb{E}\left[|b^{\xi_{k}}(\bar{X}_{T_{k}})||\bar{X}_{t}|^{p-1}\Big|\mathcal{F}_{\xi}\right]+\sqrt{2\beta^{-1}}\mathbb{E}\left[|\bar{X}_{t}|^{p-1}|\mathcal{N}(0,t-T_{k})|\Big|\mathcal{F}_{\xi}\right]}\end{array}
$$  

Note that    $b(\cdot)$   grows linearly only. Then, by Young’s inequality, together with the fact that  $t-T_{k}\le\eta_{k}$  , one has  

$$
\begin{array}{r l}&{\mathbb{E}\left[|\bar{X}_{t}|^{p-2}\bar{X}_{t}\cdot\left(b^{\xi_{k}}(\bar{X}_{T_{k}})-b^{\xi_{k}}(\bar{X}_{t})\right)\Big|\mathcal{F}_{\xi}\right]}\\ &{\qquad\qquad\qquad\qquad\lesssim(\eta_{k}^{p/(2(p-1))}+\eta_{k})\mathbb{E}\left[|\bar{X}_{t}|^{p}\Big|\mathcal{F}_{\xi}\right]+\eta_{k}\mathbb{E}\left[|\bar{X}_{T_{k}}|^{p}\Big|\mathcal{F}_{\xi}\right]+d_{}^{\frac{p}{2}}.}\end{array}
$$  

Hence,  

$$
\frac{d}{d t}\mathbb{E}\left[\left|\bar{X}_{t}\right|^{p}\middle|\mathcal{F}_{\xi}\right]\leq-c_{1}\mathbb{E}\left[\left|\bar{X}_{t}\right|^{p}\middle|\mathcal{F}_{\xi}\right]+c_{3}\eta_{k}\mathbb{E}\left[\left|\bar{X}_{T_{k}}\right|^{p}\middle|\mathcal{F}_{\xi}\right]+c_{2}d^{\frac{p}{2}},\quad t\in[T_{k},T_{k+1})\,.
$$  

Here,    $c_{1}$  ,    $c_{2}$  ,  c  $c_{3}$  3  are positive constants independent of  $t$  ,    $d$   and    $\xi$   but possibly dependent of  $p$  .  

We claim that since there exists    $c_{1}^{\prime}>0$   0 such that  

$$
-c_{1}+c_{3}\eta_{k}\leq-c_{1}^{\prime},\quad\forall k,
$$  

the moment is uniformly bounded.  

In fact, applying the Gr¨ onwall inequality,  

$$
\mathbb{E}\left[|\bar{X}_{t}|^{p}\Big|\mathcal{F}_{\xi}\right]\leq e^{-c_{1}(t-T_{k})}\mathbb{E}\left[|\bar{X}_{T_{k}}|^{p}\Big|\mathcal{F}_{\xi}\right]+\int_{T_{k}}^{t}e^{-c_{1}(t-s)}\left(c_{3}\eta_{k}\mathbb{E}\left[|\bar{X}_{T_{k}}|^{p}\Big|\mathcal{F}_{\xi}\right]+c_{2}d^{\frac{p}{2}}\right)d s.
$$  

Deﬁning  

$$
u^{\pm}(t):=\operatorname*{sup}_{0\leq s\leq t}\mathbb{E}\left[|\bar{X}_{s}|^{p}\bigg|\mathcal{F}_{\xi}\right],
$$  

one thus ﬁnds  

$$
u^{\pmb\xi}(t)\leq e^{-c_{1}(t-T_{k})}u^{\pmb\xi}(T_{k})+\int_{T_{k}}^{t}e^{-c_{1}(t-s)}[c_{3}\eta_{k}u^{\pmb\xi}(s)+c_{2}d^{\frac{p}{2}}]d s.
$$  

Then, it is not hard to ﬁnd that    $u^{\pmb{\xi}}(t)\leq v^{\pmb{\xi}}(t)$   where  

$$
\frac{d}{d t}{v}^{\xi}(t)=-c_{1}^{\prime}{v}^{\xi}(t)+c_{2}d^{\frac{p}{2}},\quad t\in[T_{k},T_{k+1}),\ {v}^{\xi}(T_{k})\geq{u}^{\xi}(T_{k}).
$$  

Remark A.1.  One may use an intermediate function satisfying the following to justify the above comparison principle:  

$$
\frac{d}{d t}\tilde{v}^{\pmb{\xi}}(t)=-c_{1}\tilde{v}^{\pmb{\xi}}(t)+c_{3}\eta_{k}\tilde{v}^{\pmb{\xi}}(t)+c_{2}d^{\frac{p}{2}}.
$$  

Since ( A.3 ) holds for each time interval and the moment is continuous in time so one can concatenate them and conclude by induction that    $u^{\pmb{\xi}}(t)\leq v^{\pmb{\xi}}(t)$   with  

$$
\frac{d}{d t}v^{\pmb\xi}(t)=-c_{1}^{\prime}v^{\pmb\xi}(t)+c_{2}d^{\frac{p}{2}},\quad v(0)=u(0)=\mathbb{E}|\bar{X}_{0}|^{p}.
$$  

Hence,  

$$
\mathbb{E}\left[|\bar{X}_{t}|^{p}\Big|\mathcal{F}_{\xi}\right]\leq c_{p}d^{\frac{p}{2}},\quad\forall t>0,
$$  

where    is a positive constant independent of     $t$  ,    $d$   and    $\xi$   but possibly dependent of   . For the exponential moment  $c_{p}$     $\mathbb{E}\left[e^{\alpha|X|^{p}}\right]$    with small    $\alpha$  , after similar Itˆ o’s calculation, we  $p$  are able to obtain  

$$
\operatorname*{sup}_{t>0}\mathbb{E}\left[e^{\alpha|\bar{X}_{t}|^{p}}\Big|\mathcal{F}_{\xi}\right]<+\infty.
$$  

This then ends the proof.  

# A.2 Proof of Lemma  3.2  

Proof of Lemma  3.2 :  We ﬁrst claim the followings: •  There exist positive constants    $c_{0}$  ,    $c_{1}$   independent of the time    $t$   such that  

$$
\frac{d}{d t}D_{K L}(\rho_{t}^{\pmb{\xi}}||\pi)\leq-c_{0}\mathcal{Z}(\rho_{t}^{\pmb{\xi}})+c_{1}d.
$$  

•  There is a positive constant    $c_{2}$   independent of the time    $t$   (  $c_{2}$   is dependent on  $D_{K L}(\rho_{0}||\pi)$  , which is a dimension-free positive constant due to Assumption  3.2 ) such that  

$$
D_{K L}(\rho_{t}^{\pmb\xi}||\pi)\leq c_{2}d.
$$  

Indeed, for the ﬁrst claim ( A.6 ), using Fokker-Planck equation ( 2.7 ) for    $\rho_{t}^{\pmb\xi}$    , we can directly calculate the following:  

$$
\begin{array}{l}{\displaystyle\frac{d}{d t}D_{K L}(\rho_{t}^{\pmb{\xi}}||\pi)=\int\left(1+\log\frac{\rho_{t}^{\pmb{\xi}}}{\pi}\right)\partial_{t}\rho_{t}^{\pmb{\xi}}d x}\\ {\displaystyle\qquad\qquad\qquad=\int\left(\nabla\log\rho_{t}^{\pmb{\xi}}-\beta b\right)\cdot\left(\rho_{t}^{\pmb{\xi}}\hat{b}_{t}-\beta^{-1}\nabla\rho_{t}^{\pmb{\xi}}\right)d x,}\end{array}
$$  

where we recall    $b=-\nabla U=\beta\nabla\log\pi$  . By Young’s inequality, we have  

$$
\begin{array}{r l r}{\lefteqn{\frac{d}{d t}D_{K L}(\rho_{t}^{\xi}||\pi)\leq\left(\frac{\beta^{-1}}{4}\int|\nabla\log\rho_{t}^{\xi}|^{2}\rho_{t}^{\xi}d x+\beta\int|\hat{b}_{t}|^{2}\rho_{t}^{\xi}d x\right)-\beta^{-1}\int|\nabla\log\rho_{t}^{\xi}|^{2}\rho_{t}^{\xi}d x}}\\ &{}&{+\frac{\beta}{2}\int(|b|^{2}+|\hat{b}_{t}|^{2})\rho_{t}^{\xi}d x+\left(\beta\int|b|^{2}\rho_{t}^{\xi}d x+\frac{\beta^{-1}}{4}\int|\nabla\log\rho_{t}^{\xi}|^{2}\rho_{t}^{\xi}d x\right)}\\ &{}&{=-\frac{1}{2}\beta^{-1}\mathbb{Z}(\rho_{t}^{\xi})+\frac{3\beta}{2}\left(\mathbb{E}\left[|\hat{b}_{t}(\bar{X}_{t})|^{2}\Big|\mathcal{F}_{\xi}\right]+\mathbb{E}\left[|b(\bar{X}_{t})|^{2}\Big|\mathcal{F}_{\xi}\right]\right).\ \ \ \ \ \ \ \ }\end{array}
$$  

Using the Lipshitz assumption, the result for moment control Proposition  3.1 , and Jensen’s inequality, since    $\eta_{k}\leq\Delta_{0}$  , we know that for    $t\in|T_{k},T_{k+1})$  ,  

$$
\begin{array}{l l}{\mathbb{E}\left[|\bar{b}_{t}(\bar{X}_{t})|^{2}\Big|\mathcal{F}_{\xi}\right]=\displaystyle\int\rho_{t}^{\xi}(x)\left(\mathbb{E}\left[b(\bar{X}_{T_{k}})|\bar{X}_{t}=x,\mathcal{F}_{\xi}\right]\right)^{2}d x\displaystyle}\\ {\quad\quad\quad\quad\quad\leq\mathbb{E}\left[|b(\bar{X}_{T_{k}})|^{2}\Big|\mathcal{F}_{\xi}\right]\leq\mathbb{E}\left[\left(|b(0)|+|\bar{X}_{T_{k}}|\right)^{2}\Big|\mathcal{F}_{\xi}\right]\leq\tilde{c}_{1}d,}\end{array}
$$  

where    $c_{1}$   is a time-independent positive constant according to Proposition  3.1 . Hence by ( A.8 ) and ( A.9 ), the ﬁrst claim ( A.6 ) holds with    $\textstyle c_{0}={\frac{1}{2}}\beta^{-1}$   and    $c_{1}=3\beta\tilde{c}_{1}$  

For the second claim ( A.7 ), we ﬁrst observe that, we can control the negative Fisher information    $-\mathcal{Z}(\bar{\rho}_{t}^{\pmb\xi})$  ) by the negative relative information    $\begin{array}{r}{-\mathcal{Z}(\rho_{t}^{\pmb{\xi}}|\pi)\,:=\,-\int|\nabla\log\frac{\rho_{t}^{\pmb{\xi}}}{\pi}|^{2}\rho_{t}^{\pmb{\xi}}d x}\end{array}$    R  |∇   via Young’s inequality, namely,  

$$
\mathcal{Z}(\rho_{t}^{\xi}|\pi)=\int|\nabla\log\frac{\rho_{t}^{\xi}}{\pi}|^{2}\rho_{t}^{\xi}d x\leq2\mathcal{Z}(\rho_{t}^{\xi})+2\beta^{2}\mathbb{E}\left[|b(\bar{X}_{t})|^{2}\middle|\mathcal{F}_{\xi}\right].
$$  

So we have  

$$
-\,\mathcal{Z}(\rho_{t}^{\pmb\xi})\leq-\frac12\mathcal{Z}(\rho_{t}^{\pmb\xi}|\pi)+\beta^{2}\mathbb{E}\left[|b(\bar{X}_{t})|^{2}\Big|\mathcal{F}_{\xi}\right].
$$  

Then, combining ( A.8 ), ( A.9 ) and ( A.11 ), we have  

$$
\begin{array}{r l}&{\cfrac{d}{d t}D_{K L}(\rho_{t}^{\xi}||\pi)\leq-\cfrac{1}{4}\beta^{-1}\mathcal{Z}(\rho_{t}^{\xi}|\pi)+2\beta\mathbb{E}\left[\left|b(\bar{X}_{t})\right|^{2}\middle|\mathcal{F}_{\xi}\right]+\cfrac{3\beta}{2}\mathbb{E}\left[\left|\hat{b}_{t}(\bar{X}_{t})\right|^{2}\middle|\mathcal{F}_{\xi}\right]}\\ &{\qquad\qquad\leq-\cfrac{1}{4}\beta^{-1}\mathcal{Z}(\rho_{t}^{\xi}|\pi)+c_{1}^{\prime}d,}\end{array}
$$  

where    $c_{1}^{\prime}$    is a positive constant. Since    $\pi$   satisﬁes a Log-Sobolev inequality with constant  $C_{\pi}^{L S}$  , we have  

$$
\frac{d}{d t}D_{K L}\big(\rho_{t}^{\pmb{\xi}}||\pi\big)\leq-\frac{1}{4\beta C_{\pi}^{L S}}D_{K L}\big(\rho_{t}^{\pmb{\xi}}||\pi\big)+c_{1}^{\prime}d.
$$  

By Gr¨ onwall’s inequality, we have  

$$
\begin{array}{r l}&{D_{K L}(\rho_{t}^{\xi}||\pi)\leq e^{-\rho t}D_{K L}(\rho_{0}||\pi)+c_{1}^{\prime}\rho^{-1}(1-e^{-\rho t})}\\ &{\qquad\qquad\leq D_{K L}(\rho_{0}||\pi)+c_{1}^{\prime}\rho^{-1}d:=c_{2}d,}\end{array}
$$  

where    $\begin{array}{r}{\rho:=\frac{1}{4\beta C_{\pi}^{L S}}}\end{array}$  . Hence the second claim ( A.7 ) holds.  

Now, equipped with the two claims ( A.6 ) and ( A.7 ), using integration by parts, we know that for all diﬀerential, nonnegative, non-increasing    $f$  ,  

$$
\begin{array}{r l}&{\quad\displaystyle\int_{0}^{T}e^{-A_{0}(T-s)}f(s)Z(\rho_{s}^{\xi}||\pi)d s}\\ &{\leq-\tilde{c}_{0}\displaystyle\int_{0}^{T}e^{-A_{0}(T-s)}f(s)\left(\frac{d}{d s}D_{K L}(\rho_{s}^{\xi}||\pi)\right)d s+\tilde{c}_{1}d\displaystyle\int_{0}^{T}e^{-A_{0}(T-s)}f(s)d s}\\ &{=\tilde{c}_{1}d\displaystyle\int_{0}^{T}e^{-A_{0}(T-s)}f(s)d s-\tilde{c}_{0}f(T)D_{K L}(\rho_{s}^{\xi}||\pi)+\tilde{c}_{0}e^{-A_{0}T}f(0)D_{K L}(\rho_{0}||\pi)}\\ &{\quad+\tilde{c}_{0}\displaystyle\int_{0}^{T}e^{-A_{0}(T-s)}f^{\prime}(s)D_{K L}(\rho_{s}^{\xi}||\pi)d s+\tilde{c}_{0}A_{0}\displaystyle\int_{0}^{T}e^{-A_{0}(T-s)}f(s)D_{K L}(\rho_{s}^{\xi}||\pi)d s}\\ &{\leq\tilde{c}_{1}d\displaystyle\int_{0}^{T}e^{-A_{0}(T-s)}f(s)d s+0+\tilde{c}_{0}e^{-A_{0}T}f(0)D_{K L}(\rho_{0}||\pi)+0+\tilde{c}_{0}c_{2}d\displaystyle\int_{0}^{T}e^{-A_{0}(T-s)}f(s)d s}\\ &{=M_{1}D_{K L}(\rho_{0}||\pi)f(0)e^{-A_{0}T}+M_{2}d\displaystyle\left(1+\sum_{s\geq0}D_{K L}(\rho_{s}^{\xi}||\pi)\right)\displaystyle\int_{0}^{T}e^{-A_{0}(T-s)}f(s)d s.}\end{array}
$$  

Here,  $\tilde{c_{0}}$  ,  $\tilde{c_{1}}$  ,    $M_{1}$  ,    $M_{2}$   are positive constants independent of    $\xi$  . The last inequality is because 0 the KL-divergence is non-negative, and    $f$   is nonnegative and non-increasing.  

Now, we have already obtained the desired estimation  

$$
\begin{array}{r l}{\lefteqn{\int_{0}^{T}e^{-A_{0}(T-s)}f(s)\mathcal{I}(\rho_{s}^{\xi})d s}}\\ &{\leq M_{1}D_{K L}(\rho_{0}||\pi)f(0)e^{-A_{0}T}+M_{2}d\left(1+\operatorname*{sup}_{s\geq0}D_{K L}(\rho_{s}^{\xi}||\pi)\right)\int_{0}^{T}e^{-A_{0}(T-s)}f(s)d s}\end{array}
$$  

for all diﬀerential, non-increasing, nonnegative function    $f$  . Since piecewise-constant func- tions can be approximated by diﬀerential functions, we know that ( A.15 ) holds for all non- increasing, nonnegative, piecewise-constant function    $f$  . This then ends the proof.  

# A.3 Basics on path measure  

In this section, we review some basics of path measure. Consider the following two SDEs in  $\mathbb{R}^{d}$    with diﬀerent drifts but the same diﬀusion    $\sigma$  :  

$$
\begin{array}{r l}&{d X^{(1)}=b^{(1)}(X^{(1)},x_{0})d t+\sigma\cdot d W,\quad X_{0}^{(1)}=X_{0}^{(2)}=x_{0}.}\\ &{d X^{(2)}=b^{(2)}(X^{(2)},x_{0})d t+\sigma\cdot d W,}\end{array}
$$  

Here,    $W$   is a standard Brownian motion under the probability    $\mathbb{P}$   (the same for the two SDEs), and    $x_{0}\sim\mu_{0}$   is a common, but ran m, initial position. We allow the drifts to be possibly dependent on the initial position  x 0  for our application. For ﬁxed time interval  $[0,T]$  , the two processes    $X^{(1)}$    and    $X^{(2)}$    naturally induce two probability measures in the path space    $\begin{array}{r}{\mathcal{X}:=C([0,T];\mathbb{R}^{d})}\end{array}$  , denoted by    $P^{(1)}$    and    $P^{(2)}$  , respectively. To be more speciﬁc, for   $[s,t]\,\subset\,[0,T]$  ,    $A\,\in\,\mathcal{B}(\mathbb{R}^{d})$  ,    $P^{(i)}([s,t]\times A)=\mathbb{P}(X_{\tau}^{(i)}\in A,\tau\in[s,t]),\;i=1,2$  ∈  ∈ . It is also obvious that the two probability measures  P  $P^{(1)}$  ,  P  $P^{(2)}$    are mutually absolutely continuous, so we are able to deﬁne the Radon-Nikodym derivative    $\textstyle{\frac{d P^{(1)}}{d P^{(2)}}}\in L^{1}(P^{(2)},\chi)$  ).  

To obtain the formula for    $\textstyle{\frac{d P^{(1)}}{d P^{(2)}}}\,\in\,L^{1}(P^{(2)},\mathcal{X})$  , we ecall that the Girsanov transform [ 19 ,  12 ,  10 ] asserts that under the probability measure  Q  satisfying  

$$
\begin{array}{l}{\displaystyle\frac{d\mathbb Q}{d\mathbb P}(X^{(2)}(\omega))=\exp\Big(\int_{0}^{T}(b^{(1)}-b^{(2)})(X_{s}^{(2)},x_{0})\cdot G^{-1}\sigma\cdot d W_{s}}\\ {\displaystyle\qquad\qquad\qquad\qquad\qquad\qquad-\frac{1}{2}\int_{0}^{T}\left|(b^{(1)}-b^{(2)})(X_{s}^{(2)},x_{0})\cdot G^{-1}\sigma\right|^{2}d s\Big),}\end{array}
$$  

with the matrix    $G$   is deﬁned by  

$$
G:=\left(\sigma\sigma^{T}\right)^{-1},
$$  

the law of    $X^{(2)}$    is the same as the law of  X  $X^{(1)}$  under    $\mathbb{P}$  . In other words, for any Borel measurable set    $B\subset{\mathcal{X}}$  ,  

$$
\mathbb{E}_{\mathbb{P}}[1_{B}(X^{(1)})]=\mathbb{E}_{\mathbb{Q}}[1_{B}(X^{(2)})]=\mathbb{E}_{\mathbb{P}}\left[1_{B}(X^{(2)})\frac{d\mathbb{Q}}{d\mathbb{P}}\right].
$$  

Note that the expression of    $\begin{array}{r}{\frac{d\mathbb{Q}}{d\mathbb{P}}(\omega)=g(X^{(2)}(\omega))}\end{array}$   where (  $X_{0}:=X(0)$  )  

$$
\begin{array}{l}{\displaystyle{g(X)=\exp\Big(\int_{0}^{T}\Big(b^{(1)}-b^{(2)})(X,X_{0})\Big)\cdot G^{-1}\cdot d X}}\\ {\displaystyle{\qquad\qquad\qquad\qquad+\,\frac12\int_{0}^{T}\Big(b^{(2)}\cdot G^{-1}\cdot b^{(2)}-b^{(1)}\cdot G^{-1}\cdot b^{(1)}\Big)\,(X,X_{0})d s\Big),}}\end{array}
$$  

Since    $P^{(1)}\,=\,(X^{(1)})_{\#}\mathbb{P}$   and    $P^{(2)}\,=\,(X^{(2)})_{\#}\mathbb{P}$   are the laws of    $X^{(1)}$    and    $X^{(2)}$    respectively, then one has  

$$
P^{(1)}(B)=\mathbb{E}_{X\sim P^{(2)}}\left[\mathbf{1}_{B}(X)g(X)\right]
$$  

It follows that the Radon-Nikodym derivative is  

$$
{\frac{d P^{(1)}}{d P^{(2)}}}(X)=g(X).
$$  

Hence, since    $d X^{(2)}=b^{(2)}(X^{(2)},x_{0})d t+\sigma\cdot d W$  , we have derived that  

$$
\begin{array}{l}{\displaystyle\frac{d P^{(1)}}{d P^{(2)}}(X^{(2)}(\omega))=\frac{d\mathbb{Q}}{d\mathbb{P}}(\omega)=\exp\Big(\int_{0}^{T}(b^{(1)}-b^{(2)})(X_{s}^{(2)},x_{0})\cdot G^{-1}\sigma\cdot d W_{s}}\\ {\displaystyle\qquad\qquad\qquad\qquad\qquad-\frac{1}{2}\int_{0}^{T}\Big|(b^{(1)}-b^{(2)})(X_{s}^{(2)},x_{0})\cdot G^{-1}\sigma\Big|^{2}\,d s\Big),}\end{array}
$$  

which is a martingale under    $\mathbb{P}$   and its natural ﬁltration deﬁned by    $\mathcal{F}_{t}^{(2)}:=\sigma(X_{s}^{(2)},s\le t)$   ≤ ),  $t\in[0,T]$  . Note that ( A.17 ) will be used in our proof.  

Moreover, we can view the process    $X^{(i)}$    as an identical mapping:    $X^{(i)}=(X_{t}^{(i)})_{0\leq t\leq T}$  :  $\Omega\to\mathcal X$  . For ﬁxed    $t\in[0,T]$  ,    $X_{t}^{(i)}$  can be viewed as a measurable mapping from   $\Omega$  to    $\mathbb{R}^{d}$    and one in fact has    $X_{t}^{(i)}=\omega_{t}\circ X^{(i)}\in\mathbb{R}^{d}$   ◦   ∈ , w    $\omega_{t}:\mathcal{X}\to\mathbb{R}^{d}$    is the time marginal deﬁne y  $\omega_{t}(\gamma)=\gamma_{t}$  . Then the law of the solution  $X_{t}^{(i)}$  at time    $t$  , namely, the time marginal of  P  $P^{(i)}$  , is the push forward measures    $P_{t}^{(i)}:=(X_{t}^{(i)})_{\#}\mathbb{P}=(\omega_{t})_{\#}P^{(i)}$  ,    $\forall t\in[0,T]$  . This means    $P_{t}^{(i)}$  is a probability measure in    $\mathbb{R}^{d}$  , satisfying  

$$
P_{t}^{(i)}(A)=\mathbb{P}(X_{t}^{(i)}\in A),\quad\forall A\in\mathcal{B}(\mathbb{R}^{d}),\quad i=1,2.
$$  

Clearly, at any time    $t$  ,    $P_{t}^{(1)}$  and  $P_{t}^{(2)}$  are mutually absolutely continuous, the Radon-Nikodym derivative    $\begin{array}{r}{\frac{d P_{t}^{(1)}}{d P_{t}^{(2)}}\in L^{1}(P_{t}^{(2)},\mathbb{R}^{d})}\end{array}$  ) is well deﬁned.  

The following Lemma describes the relationship between the two Radon-Nikodym deriva- tives (of path measures and of push forward measures):  

Lemma A.1.  Let    $Q_{1}$  ,    $Q_{2}$   be two probability distributions on    $\mathcal{X}$  , and    $Q_{2}$   is absolutely con- tinuous with respect to    $Q_{1}$  . Let    $\phi:\mathcal{X}\rightarrow\mathbb{R}^{d}$    be a measurable mapping, and consider the push forward measure    $\phi_{\#}Q_{1}$   and    $\phi_{\#}Q_{2}$  , denoted by    $Q_{1,\phi}$   and    $Q_{2,\phi}$  , respectively. Then the Randon-Nikodym derivatives  $\begin{array}{r}{\frac{d Q_{1,\phi}}{d Q_{2,\phi}}\,\in\,L^{1}(d Q_{2,\phi},\mathbb{R}^{d}),\,\,\frac{d Q_{1}}{d Q_{2}}\,\in\,L^{1}(d Q_{2},\mathcal{X})}\end{array}$       are well-deﬁned, and  

$$
\frac{d Q_{1,\phi}}{d Q_{2,\phi}}(x)=\mathbb{E}_{X\sim Q_{2}}\left[\frac{d Q_{1}}{d Q_{2}}|\phi(X)=x\right],\quad Q_{2}-a.e.
$$  

Proof of Lemma  A.1 :  Using the deﬁnition of Radon-Nikodym derivative, it suﬃces to check that for any    $A\in\mathcal{B}(\mathbb{R}^{d})$  ,  

$$
\mathbb{E}_{x\sim Q_{1,\phi}}\left[\mathbf{1}_{A}(x)\right]=\mathbb{E}_{x\sim Q_{2,\phi}}\left[\mathbf{1}_{A}(x)\mathbb{E}_{X\sim Q_{2}}\left[\frac{d Q_{1}}{d Q_{2}}(X)|\phi(X)=x\right]\right].
$$  

Indeed, using the deﬁnition of push forward measure and Randon-Nikodym derivative, as well as the conditional expectation, we have  

$$
\begin{array}{l}{L H S=\mathbb{E}_{X\sim Q_{1}}\left[\mathbf{1}_{A}(\phi(X))\right]}\\ {\quad\quad=\mathbb{E}_{X\sim Q_{2}}\left[\displaystyle\frac{d Q_{1}}{d Q_{2}}(X)\mathbf{1}_{A}(\phi(X))\right]}\\ {\quad\quad=\mathbb{E}_{X\sim Q_{2}}\left[\mathbf{1}_{A}(\phi(X))\mathbb{E}_{X\sim Q_{2}}\left[\displaystyle\frac{d Q_{1}}{d Q_{2}}(X)|\phi(X)\right]\right]}\\ {\quad\quad=R H S.}\end{array}
$$  

This is what we want.  

Clearly, if we take    $\phi=\omega_{t}$   for    $t\in[0,T]$  , the time projection mapping, then we conclude the following result for Radon-Nikodym of time marginals.  

Corollary A.1.  For    $t\in[0,T]$  ] , recall the deﬁnition of    $P_{t}^{(i)}$  and    $P^{(i)}$  ,    $i=1,2$   above. Then the following holds:  

$$
{\frac{d P_{t}^{(1)}}{d P_{t}^{(2)}}}(x)=\mathbb{E}_{X\sim P^{(2)}}\left[{\frac{d P^{(1)}}{d P^{(2)}}}(X)|X_{t}=x\right],\quad\mathbb{P}-a.e.
$$  

Also note that Corollary  A.1  here is very useful. For instance, if we combine the result ( A.21 ) in Corollary  A.1  with the Girsanov transform in ( A.17 ), we can express the quotient of densities of two processes    $\rho^{(1)}/\rho^{(2)}$    by one process    $X^{(2)}$    alone. Meanwhile, the information coming from the process    $X^{(1)}$    is stored in the drift term    $b^{(1)}(\cdot)$  , which is usually a determin- istic function. Then we only need to look into one of these two processes instead of both of them, and this can often simplify the analysis.  

# A.4 Estimate of the remaining terms  

We estimate the remaining terms  

$$
\mathbb{E}_{\xi_{k}}\mathbb{E}\left[|\bar{b}_{t}^{\xi_{k}}(\bar{X}_{t})-b^{\xi_{k}}(\bar{X}_{t})|^{2}\Big|\xi_{k}\right]
$$  

, and  

$$
\mathbb{E}_{\xi_{k},\tilde{\xi}_{k}}\left[\int|b^{\xi_{k}}-b|^{2}\frac{|\bar{\rho}_{t}^{\tilde{\xi}_{k}}-\bar{\rho}_{t}^{\xi_{k}}|^{2}}{\bar{\rho}_{t}^{\tilde{\xi}_{k}}}d x\right]
$$  

in Section  4 . Note that in the followings we consider the behaviour of SGLD in a time subinterval   $[T_{k},T_{k+1})$  , and recall that   $\bar{\rho}^{\xi_{k}}$  ,   $\bar{\rho}^{\ddot{\xi}_{k}}$   are deﬁned in ( 4.1 ).  

Lemma A.2.  Recall the deﬁnition of  $\bar{r}_{t}(x)$   in  ( 4.14 ) . Then under the setting of Proposition 3.2 , there exists a positive constant    $c$   independent of the choice of the batch    $\xi_{k}$   such that for all    $t\in[T_{k},T_{k+1})$  , it holds that  

$$
{\mathbb{E}}\left[|{\bar{r}}_{t}({\bar{X}}_{t})|^{2}{\Big|}\xi_{k}\right]\leq c d(t-T_{k})^{2}.
$$  

Proof of Lemma  A.2 :  Since    $\nabla b^{\xi}$    is    $L_{2}$  -Lipshitz, we know that  

$$
\begin{array}{r}{|\bar{r}_{t}(x)|\leq L_{2}\mathbb{E}\left[|\bar{X}_{T_{k}}-\bar{X}_{t}|^{2}|\bar{X}_{t}=x,\xi_{k}\right].}\end{array}
$$  

Hence by Jensen’s inequality, and using the Lipshitz assumption for    $b^{\xi_{k}}$    in Assumption  3.1 , we have ddd  

$$
\begin{array}{r l}&{\mathbb{E}\left[\left|\bar{r}_{t}(\bar{X}_{t})\right|^{2}\middle|\xi_{k}\right]\leq L_{2}^{2}d^{-1}\mathbb{E}\left[\left|\mathbb{E}\left[\left|\bar{X}_{T_{k}}-\bar{X}_{t}\right|^{2}|\bar{X}_{t}=x\right]\right|^{2}\middle|\xi_{k}\right]}\\ &{\qquad\qquad\leq L_{2}^{2}d^{-1}\mathbb{E}\left[\mathbb{E}\left[\left|\bar{X}_{T_{k}}-\bar{X}_{t}\right|^{4}|\bar{X}_{t}=x\right]\middle|\xi_{k}\right]}\\ &{\qquad\qquad=L_{2}^{2}d^{-1}\mathbb{E}\left[\left|b^{\xi_{k}}(\bar{X}_{T_{k}})(t-T_{k})+\int_{T_{k}}^{t}d W\right|^{4}\middle|\xi_{k}\right]}\\ &{\qquad\qquad\leq L_{2}^{2}d^{-1}\left((t-T_{k})^{4}\left(\left|b^{\xi_{k}}(0)\right|+L\mathbb{E}\left[\left|\bar{X}_{T_{k}}\right|\middle|\xi_{k}\right]\right)^{4}+3(t-T_{k})^{2}d^{2}\right),}\end{array}
$$  

where we use the inequality   $(a+b)^{p}\leq2^{p-1}(a^{p}+b^{p})$   in the last inequality.  

which leads to the conclusion ( Finally, by Proposition  3.1 , we have a uniform bound for the moment A.22 ).  $\mathbb{E}\left[|\bar{X}_{T_{k}}|^{4}\middle|\mathcal{F}_{\xi}\right]$   i ,  

Lemma A.3.  Under the setting of Proposition  3.2 , there exists a positive constant    $c$   inde- pendent of    $k$   and    $\xi_{k}$   such that for    $t\in|T_{k},T_{k+1}\rangle$  ) ,  

$$
\int\left|\mathbb{E}[\bar{X}_{T_{k}}-\bar{X}_{t}|\bar{X}_{t}=x,\xi_{k}]\right|^{2}\bar{\rho}_{t}^{\xi_{k}}(x)d x\leq c\eta_{k}^{2}\left(d+\mathcal{I}(\bar{\rho}_{T_{k}})\right),
$$  

where  I  $\begin{array}{r}{\mathcal{Z}(\rho):=\int\rho|\nabla\log\rho|^{2}d x}\end{array}$   is the Fisher information.  

Proof of Lemma  A.3 :  By Bayes’ law, we have  

$$
\begin{array}{r l r}{\lefteqn{\mathbb{E}[\bar{X}_{T_{k}}-\bar{X}_{t}|\bar{X}_{t}=x,\xi_{k}]=\int(y-x)P(\bar{X}_{T_{k}}=y|\bar{X}_{t}=x,\xi_{k})d y}}\\ &{}&{\quad=\int(y-x)\frac{\bar{\rho}_{T_{k}}(y)P(\bar{X}_{t}=x|\bar{X}_{T_{k}}=y,\xi_{k})}{\bar{\rho}_{t}^{\xi_{k}}(x)}d y.}\end{array}
$$  

Since    $P(X_{t}\,=\,x|X_{T_{k}}\,=\,y,\xi_{k})$  | ) is Gaussian, and since its derivative is also similar to the Gaussian form, we split the term    $\mathbb{E}[X_{T_{k}}-X_{t}|X_{t}=x,\xi_{k}]$   − | ] into three parts and use integration by parts to handle them.  

and deﬁne  

$$
\begin{array}{r l}&{y-x=\big(I_{d}+(t-T_{k})\nabla b^{\xi_{k}}(y)\big)\cdot\big(y-x+(t-T_{k})b^{\xi_{k}}(y)\big)}\\ &{\qquad\qquad-\big(t-T_{k})\nabla b^{\xi_{k}}(y)\cdot\big(y-x+(t-T_{k})b^{\xi_{k}}(y)\big)}\\ &{\qquad\qquad-\big(t-T_{k}\big)\cdot b^{\xi_{k}}(y)}\\ &{\qquad\qquad:=a_{1}(x,y)-a_{2}(x,y)-a_{3}(x,y),}\end{array}
$$  

$$
I_{i}(x):=\mathbb{E}\left[a_{i}(\bar{X}_{t},\bar{X}_{T_{k}})|\bar{X}_{t}=x\right],\quad i=1,2,3.
$$  

Next, we will obtain an    $\eta_{k}^{2}$    estimate for  $\mathbb{E}\left[|I_{i}(\bar{X}_{t})|^{2}\bigg|\xi_{k}\right]$  h i ,    $i=1,2,3$  . We ﬁrst claim that, there exist positive constants    $c$  ,    $c^{\prime}$  ,    $c^{\prime\prime}$    independent of  k  and    $\xi$   such that for    $t\in[T_{k},T_{k+1})$  ),  

$$
\mathbb{E}\left[|I_{1}(\bar{X}_{t})|^{2}\Big|\xi_{k}\right]\leq c(t-T_{k})^{2}\mathcal{Z}(\bar{\rho}_{T_{k}}),
$$  

$$
\mathbb{E}\left[|I_{2}(\bar{X}_{t})|^{2}\Big|\xi_{k}\right]\leq c^{\prime}d(t-T_{k})^{3},
$$  

$$
{\mathbb{E}}\left[|I_{3}(\bar{X}_{t})|^{2}\Big|\xi_{k}\right]\leq c^{\prime\prime}d(t-T_{k})^{2},
$$  

where  $\begin{array}{r}{\mathcal{Z}(\rho):=\int\rho|\nabla\log\rho|^{2}d x}\end{array}$   is the Fisher information.  

R By the claims ( A.26 ), ( A.27 ), ( A.28 ) , we can easily obtain the following    $O\left(\eta_{k}^{2}(d+\mathcal{Z}(\bar{\rho}_{T_{k}})\right)$     bound:  

$$
\int|\mathbb{E}[\bar{X}_{T_{k}}-\bar{X}_{t}|\bar{X}_{t}=x,\xi_{k}]|^{2}\bar{\rho}_{t}^{\xi_{k}}(x)d x\leq3\sum_{i=1}^{3}\mathbb{E}\left[|I_{i}(\bar{X}_{t})|^{2}\Big|\xi_{k}\right]\leq\tilde{c}\eta_{k}^{2}\left(d+\mathcal{I}(\bar{\rho}_{T_{k}})\right),
$$  

where the positive constant  c  is independent of the batch    $\xi_{k}$  , and this is what we desire.  

For the the claims ( A.26 ), ( A.27 ), ( A.28 ), we prove them separately in the followings: (a) For the term    $I_{1}$  , since the distribution    $P(X_{t}=x|X_{T_{k}}=y,\xi_{k})$  | ) is Gaussian, namely,  

$$
P(\bar{X}_{t}=x|\bar{X}_{T_{k}}=y,\xi_{k})=\left(4\pi\beta^{-1}(t-T_{k})\right)^{-\frac{d}{2}}\exp\left(-\frac{|x-y-b^{\xi_{k}}(y)(t-T_{k})|^{2}}{4\beta^{-1}(t-T_{k})}\right).
$$  

Then, after integration by parts we obtain:  

$$
I_{1}(x)=2\beta^{-1}(t-T_{k})\int\frac{\nabla_{y}\bar{\rho}_{T_{k}}(y)}{\bar{\rho}_{t}^{\xi_{k}}(x)}P(\bar{X}_{t}=x|\bar{X}_{T_{k}}=y,\xi_{k})d y.
$$  

Using Bayes’ law again, we have  

$$
I_{1}(x)=2\beta^{-1}(t-T_{k})\int\frac{\nabla_{y}\bar{\rho}_{T_{k}}(y)}{\bar{\rho}_{T_{k}}(y)}P(\bar{X}_{T_{k}}=y|\bar{X}_{t}=x,\xi_{k})d y.
$$  

Hence, by Jensen’s inequality,  

$$
\begin{array}{r l r}&{}&{\mathbb{E}\left[|I_{1}(\bar{X}_{t})|^{2}\Big|\xi_{k}\right]\leq4\beta^{-2}(t-T_{k})^{2}\displaystyle\int\bar{\rho}_{t}^{\xi_{k}}(x)\int\left|\frac{\nabla_{y}\bar{\rho}_{T_{k}}(y)}{\bar{\rho}_{T_{k}}(y)}\right|^{2}P(\bar{X}_{T_{k}}=y|\bar{X}_{t}=x,\xi_{k})d y d x}\\ &{}&{\qquad\qquad=4\beta^{-2}(t-T_{k})^{2}\mathcal{I}(\bar{\rho}_{T_{k}}):=c(t-T_{k})^{2}\mathcal{I}(\bar{\rho}_{T_{k}}).\qquad\qquad\qquad}\\ &{}&{\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\quad}\end{array}
$$  

(b) For the term    $I_{2}$  , using the Lipshitz condition in Assumption  3.1  and Jensen’s in- equality, we have  

$$
\begin{array}{r l}&{\mathbb{E}\left[|I_{2}(\bar{X}_{t})|^{2}\Big|\xi_{k}\right]\leq\tilde{c}^{\prime}(t-T_{k})^{2}\mathbb{E}\left[\left|\mathbb{E}\left[\bar{X}_{t}-\bar{X}_{T_{k}}-(t-T_{k})b^{\xi_{k}}(\bar{X}_{t})\Big|\bar{X}_{T_{k}}\right]\right|^{2}\Big|\xi_{k}\right]}\\ &{\qquad\qquad\leq\tilde{c}^{\prime}(t-T_{k})^{2}\mathbb{E}\left[\left|\bar{X}_{t}-\bar{X}_{T_{k}}-(t-T_{k})b^{\xi_{k}}(\bar{X}_{t})\right|^{2}\Big|\xi_{k}\right]}\\ &{\qquad\qquad\leq\tilde{c}^{\prime}(t-T_{k})^{2}\mathbb{E}\left[\left|\int_{T_{k}}^{t}\sqrt{2\beta^{-1}}d W_{s}\right|^{2}\Big|\xi_{k}\right]=c^{\prime}d(t-T_{k})^{3}.}\end{array}
$$  

The constant    $c^{\prime}$    here is independent of    $\xi_{k}$   since the Lipshitz constant is uniform.  

(c) For the term    $I_{3}$  , still using Jensen’s inequality and Lipshitz assumption for    $b^{\xi_{k}}$  , it is clear that  

$$
\begin{array}{r l}&{\mathbb{E}\left[|I_{3}(\bar{X}_{t})|^{2}\Big|\xi_{k}\right]\leq(t-T_{k})^{2}\mathbb{E}\left[|b^{\xi_{k}}(\bar{X}_{T_{k}})|^{2}\Big|\xi_{k}\right]}\\ &{\qquad\qquad\qquad\leq2(t-T_{k})^{2}\left(|b^{\xi_{k}}(0)|^{2}+L_{2}\mathbb{E}\left[|\bar{X}_{T_{k}}|^{2}\Big|\xi_{k}\right]\right).}\end{array}
$$  

By Proposition  3.1 , for any ﬁxed batch    $\xi_{k}$  , the moment  $\mathbb{E}\left[|\bar{X}_{T_{k}}|^{2}\middle|\xi_{k}\right]$  i has a uniform-in-batch  $O(1)$   upper bound. Therefore, we are able to obtain the following batch-independent bound for the term  $I_{3}$  :  

$$
\mathbb{E}\left[|I_{3}(\bar{X}_{t})|^{2}\Big|\xi_{k}\right]\leq c^{\prime\prime}d(t-T_{k})^{2}.
$$  

Concluding the results we obtained in parts (a), (b), (c) yields the claims ( A.26 ), ( A.27 ), ( A.28 ).  

In the following lemmas, we prove some details for estimate of  $\begin{array}{r}{\mathbb{E}_{\xi_{k},\tilde{\xi}_{k}}\left[\int|b^{\xi_{k}}-b|^{2}\frac{\vert\bar{\rho}_{t}^{\xi_{k}}-\bar{\rho}_{t}^{\xi_{k}}\vert^{2}}{\bar{\rho}_{t}^{\bar{\xi}_{k}}}d x\right]}\end{array}$  ò  

Lemma A.4.  Recall the notations  

$$
K_{1}:=\sqrt{\frac{\beta}{2}}\,\tilde{b}(y)(x-y),\quad\tilde{b}(y):=(b^{\xi_{k}}-b^{\tilde{\xi}_{k}})(y).
$$  

Then under the conditions of Proposition  3.2 , there exists a positive constant  c  independent of    $k$   and    $\xi_{k},\tilde{\xi}_{k}$   such that for    $t\in|T_{k},T_{k+1}\rangle$  ) ,  

$$
\int\bar{\rho}_{t}^{\tilde{\xi}_{k}}(x)\left(\int K_{1}P(\bar{X}_{T_{k}}=y|\bar{Y}_{t}=x,\xi_{k},\tilde{\xi}_{k})d y\right)^{2}d x\leq c\eta_{k}^{2}\left(d+\mathcal{I}(\bar{\rho}_{T_{k}})\right).
$$  

Proof of Lemma  A.4 :  The technique here is similar to the one we use in the proof of Lemma A.3 . To begin with, we split the term    $K_{1}$   into the following three parts:  

$$
\begin{array}{r l}&{\tilde{b}(y)\cdot(y-x)=\tilde{b}(y)\cdot\left(I_{d}+(t-T_{k})\nabla b^{\tilde{\xi}_{k}}(y)\right)\cdot\left(y-x+(t-T_{k})b^{\tilde{\xi}_{k}}(y)\right)}\\ &{\phantom{a a a a}-(t-T_{k})\tilde{b}(y)\cdot\nabla b^{\tilde{\xi}_{k}}(y)\cdot\left(y-x+(t-T_{k})b^{\tilde{\xi}_{k}}(y)\right)}\\ &{\phantom{a a a a a}-(t-T_{k})\tilde{b}(y)\cdot b^{\tilde{\xi}_{k}}(y)}\\ &{:=\bar{a}_{1}(x,y)-\bar{a}_{2}(x,y)-\bar{a}_{3}(x,y),}\end{array}
$$  

and deﬁne  

$$
\bar{I}_{i}(x):=\mathbb{E}\left[\bar{a}_{i}(\bar{X}_{T_{k}},\bar{Y}_{t})\Big|\bar{Y}_{t}=x,\xi_{k},\tilde{\xi}_{k}\right],\quad i=1,2,3.
$$  

Then,  

$$
\int{\bar{\rho}_{t}^{\hat{\xi}_{k}}(x)\left(\int{K_{1}P(\bar{X}_{T_{k}}=y|\bar{Y}_{t}=x)d y}\right)^{2}d x}=\frac{\beta}{2}\mathbb{E}\left[|\bar{I}_{1}(\bar{Y}_{t})-\bar{I}_{2}(\bar{Y}_{t})-\bar{I}_{3}(\bar{Y}_{t})|^{2}\middle|\xi_{k},\hat{\xi}_{k}\right]
$$  

(a) For the ﬁrst term   $I_{1}$  , using Bayes’ formula and integration by parts, since    $P(Y_{t}=$   $x|\bar{X}_{T_{k}}=y,\xi_{k},\tilde{\xi}_{k})$  ) is Gaussian, we have  

$$
\begin{array}{l l l}{\displaystyle\bar{I}_{1}(x)=2\beta^{-1}\int\tilde{b}(y)\cdot\left(I_{d}+(t-T_{k})\nabla b^{\xi_{k}}(y)\right)\cdot\frac{\beta}{2}\left(y-x+(t-T_{k})b^{\xi_{k}}(y)\right)\frac{\bar{\rho}T_{T_{k}}(y)}{\bar{\rho}_{t}^{\xi_{k}}(x)}P(\bar{Y}_{t}=x|\bar{X}_{T_{k}}=y|\bar{X}_{T_{k}})}\\ {\displaystyle\qquad=2\beta^{-1}(t-T_{k})\int\frac{\nabla_{y}(\tilde{b}(y)\bar{\rho}_{T_{k}}(y))}{\bar{\rho}_{t}^{\xi_{k}}(x)}P(\bar{Y}_{t}=x|\bar{X}_{T_{k}}=y,\xi_{k},\tilde{\xi}_{k})d y}\\ {\displaystyle\qquad=2\beta^{-1}(t-T_{k})\int\left(\nabla\tilde{b}(y)+\tilde{b}(y)\frac{\nabla\bar{\rho}_{T_{k}}(y)}{\bar{\rho}_{T_{k}}(y)}\right)P(\bar{X}_{T_{k}}=y|\bar{Y}_{t}=x,\xi_{k},\tilde{\xi}_{k})d y.}\end{array}
$$  

Since    $\nabla\tilde{b}$   and   $\tilde{b}=[(b^{\xi_{k}}-b)-(b^{\tilde{\xi}_{k}}-b)]/\sqrt{2\beta^{-1}}$  −  − p   are uniformly bounded by Assumption  3.1 ,  

$$
\mathbb{E}\left[|\bar{I}_{1}(\bar{Y}_{t})|^{2}\Big|\xi_{k},\tilde{\xi}_{k}\right]\leq c\eta_{k}^{2}\left(1+\mathcal{Z}\big(\bar{\rho}_{T_{k}}\big)\right),
$$  

and the constant    $c$   is independent of  $\xi_{k}$   and  $\ddot{\xi}_{k}$  . (b) For the second term   $I_{2}$  , by Jensen’s inequality, it holds that  

$$
\mathbb{E}\left[|\bar{I}_{2}(\bar{Y}_{t})|^{2}\Big|\xi_{k},\tilde{\xi}_{k}\right]\leq(t-T_{k})^{2}\mathbb{E}\left[\left|\tilde{b}(\bar{X}_{T_{k}})\cdot\nabla b^{\tilde{\xi}_{k}}(\bar{X}_{T_{k}})\cdot\int_{T_{k}}^{t}d W\right|^{2}\Big|\xi_{k},\tilde{\xi}_{k}\right].
$$  

By Assumption  3.1 , both   $\tilde{b}=[(b^{\xi_{k}}-b)-(b^{\tilde{\xi}_{k}}-b)]/\sqrt{2\beta^{-1}}$  − − p   and    $\nabla b^{\ddot{\xi}_{k}}$   are uniformly bounded, so we can directly get  

$$
\mathbb{E}\left[|\bar{I}_{2}(\bar{Y}_{t})|^{2}\Big|\xi_{k},\tilde{\xi}_{k}\right]\leq c d(t-T_{k})^{3},
$$  

and the constant    $c$   is independent of    $\xi_{k}$   and  $\ddot{\xi}_{k}$  . (c) For the third term   ${\bar{I}}_{3}$  , by Jensen’s inequality,  

$$
\begin{array}{r}{\mathbb{E}\left[\left|\bar{I}_{3}(\bar{Y}_{t})\right|^{2}\left|\xi_{k},\tilde{\xi}_{k}\right.\right]\leq(t-T_{k})^{2}\mathbb{E}\left[\left|\tilde{b}(\bar{X}_{T_{k}})\cdot b^{\tilde{\xi}_{k}}(\bar{X}_{T_{k}})\right|^{2}\left|\xi_{k},\tilde{\xi}_{k}\right.\right].}\end{array}
$$  

Since   $\ddot{b}$   $b^{\ddot{\xi}_{k}}$   is Lipshitz by Assumption  is bounded, and since    3.1 , we have  

$$
\begin{array}{r l}&{\mathbb{E}\left[|\bar{I}_{3}(\bar{Y}_{t})|^{2}\Big|\xi_{k},\tilde{\xi}_{k}\right]\leq c(t-T_{k})^{2}\mathbb{E}\left[|b^{\tilde{\xi}_{k}}(\bar{X}_{T_{k}})|^{2}\Big|\xi_{k},\tilde{\xi}_{k}\right]}\\ &{\qquad\qquad\qquad\leq2c(t-T_{k})^{2}\left(|b^{\tilde{\xi}_{k}}(0)|^{2}+L^{2}\mathbb{E}\left[|\bar{X}_{T_{k}}|^{2}\Big|\xi_{k},\tilde{\xi}_{k}\right]\right).}\end{array}
$$  

Due to ( 3.4 ),    $|b^{\tilde{\xi}_{k}}(0)|\,\le\,|b(0)|\,+\,|b^{\tilde{\xi}_{k}}(0)\,-\,b(0)|$  | ≤| |  |  − |  is uniformly bounded almost surely. By Proposition  3.1 , there is a uniform-in-batch    $O(1)$   bound for the moment    $\mathbb{E}|X_{T_{k}}|^{2}$  | . Hence we obtain  

$$
\mathbb{E}\left[|\bar{I}_{3}(\bar{Y}_{t})|^{2}\Big|\xi_{k},\tilde{\xi}_{k}\right]\leq c d(t-T_{k})^{2},
$$  

and the constant    $c$   is independent of    $\xi_{k}$   and  $\tilde{\xi}_{k}$  .  

Finally, combining (a), (b) and (c), we get the desired result.  

Lemma A.5.  Recall the notations  

$$
K_{2}:=\left(-\sqrt{\frac{\beta}{2}}\,\tilde{b}(y)\cdot b^{\tilde{\xi}_{k}}(y)-\frac12|\tilde{b}(y)|^{2}\right)(t-T_{k}),\quad\tilde{b}(y):=\frac{1}{\sqrt{2\beta^{-1}}}\left(b^{\tilde{\xi}_{k}}-b^{\xi_{k}}\right)(y).
$$  

Then under the conditions of Proposition  3.2 , there exists a positive constant  c  independent of    $k$   and    $\xi_{k}$   such that for    $t\in|T_{k},T_{k+1}|$  ) ,  

$$
\int\bar{\rho}_{t}^{\tilde{\xi}_{k}}(x)\left(\int K_{2}P(\bar{X}_{T_{k}}=y|\bar{Y}_{t}=x,\xi_{k},\tilde{\xi}_{k})d y\right)^{2}d x\leq c d\eta_{k}^{2}.
$$  

The bound is independent of the choice of the batches    $\tilde{\xi}_{k}$   ,    $\xi_{k}$  .  

Proof of  A.5 :  By Jensen’s inequality, we have  

$$
\begin{array}{l}{\displaystyle\int\bar{\rho}_{t}^{\tilde{\xi}_{k}}(x)\left(\int K_{2}P(\bar{X}_{T_{k}}=y|\bar{Y}_{t}=x)d y\right)^{2}d x}\\ {\displaystyle\leq\int\bar{\rho}_{t}^{\tilde{\xi}_{k}}(x)\left(\int|K_{2}|^{2}P(\bar{X}_{T_{k}}=y|\bar{Y}_{t}=x)d y\right)d x}\\ {\displaystyle=(t-T_{k})^{2}\mathbb{E}\left[\left|\sqrt{\frac{\beta}{2}}\,\tilde{b}(\bar{X}_{T_{k}})\cdot b^{\tilde{\xi}_{k}}(\bar{X}_{T_{k}})+\frac{1}{2}|\tilde{b}(\bar{X}_{T_{k}})|^{2}\right|^{2}\Big|\xi_{k},\tilde{\xi}_{k}\right]}\end{array}
$$  

Since    $b^{\ddot{\xi}_{k}}$   is Lipshitz by Assumption  3.1 , we have  

$$
\mathbb{E}\left[\left|\sqrt{\frac{\beta}{2}}\,\tilde{b}(\bar{X}_{T_{k}})\cdot b^{\tilde{\xi}_{k}}(\bar{X}_{T_{k}})+\frac{1}{2}\vert\tilde{b}(\bar{X}_{T_{k}})\vert^{2}\right|^{2}\Big\vert\xi_{k},\tilde{\xi}_{k}\right]\leq\tilde{c}_{1}+\tilde{c}_{2}\mathbb{E}\left[\vert\bar{X}_{T_{k}}\vert^{2}\Big\vert\xi_{k},\tilde{\xi}_{k}\right].
$$  

Here, the positive constants   $\tilde{c_{1}}$  ,   $\tilde{c_{2}}$   are independent of the batch since the coeﬃcients in 1 conditions (a), (d) of A ption  3.1  are uniform-in-batch. By Proposition  3.1 ,    $\mathbb{E}\left[|X_{T_{k}}|^{2}\right]$   has a uniform-in-batch  $O(1)$  (1) upper bound. Combining this fact with ( A.47 ), one then has  

$$
\int\bar{\rho}_{t}^{\tilde{\xi}_{k}}(x)\left(\int K_{2}P(\bar{X}_{T_{k}}=y|\bar{Y}_{t}=x,\xi_{k},\tilde{\xi}_{k})d y\right)^{2}d x\leq c d\eta_{k}^{2}.
$$  

Here,    $c$   is a positive constant independent of    $k$  ,    $d$  ,    $\xi_{k}$   and  $\tilde{\xi}_{k}$  .  

Lemma A.6.  Recall the notations  

$$
K_{3}:=e^{z}-1-z,
$$  

with  

and  

$$
z:=\sqrt{\frac{\beta}{2}}\,\widetilde{b}(y)(x-y-(t-T_{k})b^{\widetilde{\xi}_{k}}(y))-\frac{1}{2}|\widetilde{b}(y)|^{2}(t-T_{k}),
$$  

$$
\tilde{b}(y):=\frac{1}{\sqrt{2\beta^{-1}}}\left(b^{\tilde{\xi}_{k}}-b^{\xi_{k}}\right)(y).
$$  

Then under the conditions of Proposition  3.2 , there exists a positive constant  c  independent of    $k$   and    $\xi_{k}$   such that for    $t\in[T_{k},T_{k+1}]$  ) ,  

$$
\int\bar{\rho}_{t}^{\tilde{\xi}_{k}}(x)\left(\int K_{3}P(\bar{X}_{T_{k}}=y|\bar{Y}_{t}=x,\xi_{k},\tilde{\xi}_{k})d y\right)^{2}d x\leq c d\eta_{k}^{2}.
$$  

Proof of Lemma  A.6 :  By Jensen’s inequality, it holds that  

$$
\begin{array}{r l}&{\quad\displaystyle\int\bar{\rho}_{t}^{\xi_{k}}(x)\left(\displaystyle\int K_{3}P(\bar{X}_{T_{k}}=y|\bar{Y}_{t}=x,\xi_{k},\tilde{\xi}_{k})d y\right)^{2}d x}\\ &{\leq\displaystyle\int\bar{\rho}_{t}^{\xi_{k}}(x)\displaystyle\int|K_{3}|^{2}P(\bar{X}_{T_{k}}=y|\bar{Y}_{t}=x)d y d x=\mathbb{E}\left[\left|e^{\hat{Y}_{t}}-1-\hat{Y}_{t}\right|^{2}\left|\xi_{k},\tilde{\xi}_{k}\right],}\end{array}
$$  

where we denote the process  

$$
\begin{array}{r l r}{\lefteqn{\hat{Y}_{t}:=\sqrt{\frac{\beta}{2}}\tilde{b}(\bar{X}_{T_{k}})\cdot\left(\bar{Y}_{t}-\bar{X}_{T_{k}}-(t-T_{k})b^{\tilde{\xi}_{k}}(\bar{X}_{T_{k}})\right)-\frac{1}{2}|\tilde{b}(\bar{X}_{T_{k}})|^{2}\Delta t}}\\ &{}&{=-\frac{1}{2}|\tilde{b}(\bar{X}_{T_{k}})|^{2}\Delta t+\tilde{b}(\bar{X}_{T_{k}})\cdot\int_{T_{k}}^{t}d W.~~~}\end{array}
$$  

with  

$$
\Delta t:=t-T_{k},\quad\forall t\in[T_{k},T_{k+1}).
$$  

Denote   $\bar{Z}_{t}:=e^{\hat{Y}_{t}}-1-\hat{Y}_{t}$   −  − t . In the following, we aim to obtain an    $O(\eta_{k}^{2})$  ) bound for the term  $\mathbb{E}\left[|\bar{Z}_{t}|^{2}\middle|\xi_{k},\tilde{\xi}_{k}\right]$  mainly via It o’s formula. In fact, for    $t\in[T_{k},T_{k+1}$  )  

$$
\bar{Z}_{t}=\frac{1}{2}|\tilde{b}|^{2}\Delta t+\tilde{b}\cdot\int_{T_{k}}^{t}\left(e^{\hat{Y}_{s}}-1\right)d W_{s}=\frac{1}{2}|\tilde{b}|^{2}\Delta t+\tilde{b}\cdot\int_{T_{k}}^{t}\left(\bar{Z}_{s}+\hat{Y}_{s}\right)d W_{s}.
$$  

So  

$$
\mathbb{E}\left[|\bar{Z}_{t}|^{2}\Big|\xi_{k},\tilde{\xi}_{k}\right]=\frac{1}{4}\mathbb{E}\left[|\tilde{b}|^{4}\Big|\xi_{k},\tilde{\xi}_{k}\right](\Delta t)^{2}+\int_{T_{k}}^{t}\mathbb{E}\left[|\tilde{b}|^{2}\left(\bar{Z}_{s}+\hat{Y}_{s}\right)^{2}\Big|\xi_{k},\tilde{\xi}_{k}\right]d s.
$$  

By Assumption  3.1 ,   $\ddot{b}$  b  is uniformly bounded. Then,    $\mathbb{E}[|\hat{Y}_{t}|^{2}|\xi_{k},\tilde{\xi}_{k}]\leq c d\Delta t$  | |  ≤ . Then, one has  

$$
\mathbb{E}\left[|\bar{Z}_{t}|^{2}\Big|\xi_{k},\tilde{\xi}_{k}\right]\leq c\int_{T_{k}}^{t}\mathbb{E}\left[|\bar{Z}_{s}|^{2}\Big|\xi_{k},\tilde{\xi}_{k}\right]\,d s+c d(\Delta t)^{2}.
$$  

By Gr¨ onwall’s inequality, when    $\eta_{k}$   is small, one thus has  

$$
\mathbb{E}\left[|\bar{Z}_{t}|^{2}\Big|\xi_{k},\tilde{\xi}_{k}\right]\leq c d(\Delta t)^{2}\leq c d\eta_{k}^{2}.
$$  

Above,    $c$   is a generative positive constant independent of    $k$   and    $\xi_{k}$  , with the concrete meaning varying from line to line. This then ends the proof.  

# References  

[1] Geometric ergodicity of SGLD via reﬂection coupling. 2022.

 [2] Gabriele Abbati, Alessandra Tosi, Michael Osborne, and Seth Flaxman. Adageo: Adap- tive geometric learning for optimization and sampling. In  International conference on artiﬁcial intelligence and statistics , pages 226–234. PMLR, 2018.

 [3] Aur´ elien Alfonsi, Benjamin Jourdain, and Arturo Kohatsu-Higa. Optimal transport bounds between the time-marginals of a multidimensional diﬀusion and its Euler scheme.  Electronic Journal of Probability , 20:1–31, 2015.

 [4] Dominique Bakry and Michel  Emery. Diﬀusions hyper contractive s. In  Seminaire de probabilit´ es XIX 1983/84 , pages 177–206. Springer, 1985.

 [5] Dominique Bakry, Ivan Gentil, Michel Ledoux, et al.  Analysis and geometry of Markov diﬀusion operators , volume 103. Springer, 2014.

 [6] Fran¸ cois Bolley and C´ edric Villani. Weighted Csisz´ ar-Kullback-Pinsker inequalities and applications to transportation inequalities. In  Annales de la Facult´ e des sciences de Toulouse: Math´ ematiques , volume 14, pages 331–352, 2005.

 [7] Nicolas Brosse, Alain Durmus, and Eric Moulines. The promises and pitfalls of stochas- tic gradient Langevin dynamics.  Advances in Neural Information Processing Systems , 31, 2018.

 [8] Arnak S Dalalyan. Theoretical guarantees for approximate sampling from smooth and log-concave densities. Journal of the Royal Statistical Society: Series   $B$   (Statistical Methodology) , 79(3):651–676, 2017.

 [9] Arnak S Dalalyan and Avetik Karagulyan. User-friendly guarantees for the Langevin Monte Carlo with inaccurate gradient. Stochastic Processes and their Applications , 129(12):5278–5311, 2019.

 [10] Arnak S Dalalyan and Alexandre B Tsybakov. Sparse regression learning by aggregation and Langevin Monte-Carlo.  Journal of Computer and System Sciences , 78(5):1423– 1443, 2012.

 [11] Christian Daniel, Jonathan Taylor, and Sebastian Nowozin. Learning step size con- trollers for robust neural network training. In  Thirtieth AAAI Conference on Artiﬁcial Intelligence , 2016.

 [12] Richard Durrett.  Stochastic calculus: a practical introduction . CRC press, 2018.

 [13] Rick Durrett.  Probability: theory and examples , volume 49. Cambridge university press, 2019.  

[14] Andreas Eberle. Reﬂection coupling and Wasserstein contractivity without convexity. Comptes Rendus Mathematique , 349(19-20):1101–1104, 2011.

 [15] Lawrence C Evans.  Partial diﬀerential equations , volume 19. American mathematical society, 2022.

 [16] Tyler Farghly and Patrick Rebeschini. Time-independent generalization bounds for SGLD in non-convex settings.  Advances in Neural Information Processing Systems , 34:19836–19846, 2021.

 [17] Yuanyuan Feng, Tingran Gao, Lei Li, Jian-Guo Liu, and Yulong Lu. Uniform-in-time weak error analysis for stochastic gradient descent algorithms via diﬀusion approxima- tion.  arXiv preprint arXiv:1902.00635 , 2019.

 [18] Nicolas Fournier, Maxime Hauray, and St´ ephane Mischler. Propagation of chaos for the 2d viscous vortex model.  Journal of the European Mathematical Society , 16(7):1423– 1466, 2014.

 [19] Igor Vladimirovich Girsanov. On transforming a certain class of stochastic processes by absolutely continuous substitution of measures.  Theory of Probability & Its Appli- cations , 5(3):285–301, 1960.

 [20] Leonard Gross. Logarithmic Sobolev inequalities.  American Journal of Mathematics , 97(4):1061–1083, 1975.

 [21] Wenqing Hu, Chris Junchi Li, Lei Li, and Jian-Guo Liu. On the diﬀusion approxima- tion of nonconvex stochastic gradient descent.  Annals of Mathematical Sciences and Applications , 4(1), 2019.

 [22] Shi Jin, Lei Li, and Jian-Guo Liu. Random batch methods (RBM) for interacting particle systems.  Journal of Computational Physics , 400:108877, 2020.

 [23] Shi Jin, Lei Li, Zhenli Xu, and Yue Zhao. A random batch Ewald method for par- ticle systems with Coulomb interactions. SIAM Journal on Scientiﬁc Computing , 43(4):B937–B960, 2021.

[24] Shi Jin, Lei Li, Xuda Ye, and Zhennan Zhou. Ergodicity and long-time behav- ior of the random batch method for interacting particle systems. arXiv preprint arXiv:2202.04952 , 2022.

 [25] Diederik P Kingma and Jimmy Ba. Adam: A method for stochastic optimization. arXiv preprint arXiv:1412.6980 , 2014.

 [26] Bobby Kleinberg, Yuanzhi Li, and Yang Yuan. An alternative view: When does SGD escape local minima? In  International Conference on Machine Learning , pages 2698– 2707. PMLR, 2018.

 [27] Rep Kubo. The ﬂuctuation-dissipation theorem. Reports on progress in physics , 29(1):255, 1966.

 [28] Solomon Kullback and Richard A Leibler. On information and suﬃciency.  The annals of mathematical statistics , 22(1):79–86, 1951.

 [29] Michel Ledoux. Concentration of measure and logarithmic Sobolev inequalities. In Seminaire de probabilites XXXIII , pages 120–216. Springer, 1999.

 [30] Lei Li and Jian-Guo Liu. Large time behaviors of upwind schemes and B-schemes for Fokker-Planck equations on R by jump processes.  Mathematics of Computation , 89(325):2283–2320, 2020.

 [31] Lei Li, Lin Liu, and Yuzhou Peng. A splitting Hamiltonian Monte Carlo method for eﬃcient sampling.  arXiv preprint arXiv:2105.14406 , 2021.  

[32] Lei Li and Yuliang Wang. On uniform-in-time diﬀusion approximation for stochastic gradient descent.  arXiv preprint arXiv:2207.04922 , 2022.

 [33] Wenzhe Li, Sungjin Ahn, and Max Welling. Scalable MCMC for mixed membership stochastic blockmodels. In  Artiﬁcial Intelligence and Statistics , pages 723–731. PMLR, 2016.

 [34] Peter A Markowich and C´ edric Villani. On the trend to equilibrium for the Fokker- Planck equation: an interplay between physics and functional analysis.  Mat. Contemp , 19:1–29, 2000.

 [35] Wenlong Mou, Nicolas Flammarion, Martin J Wainwright, and Peter L Bartlett. Im- proved bounds for discretization of Langevin diﬀusions: Near-optimal rates without convexity.  arXiv preprint arXiv:1907.11331 , 2019.

 [36] Wenlong Mou, Liwei Wang, Xiyu Zhai, and Kai Zheng. Generalization bounds of SGLD for non-convex learning: Two theoretical viewpoints. In  Conference on Learning Theory , pages 605–638. PMLR, 2018.

 [37] Arvind Neelakantan, Luke Vilnis, Quoc V Le, Ilya Sutskever, Lukasz Kaiser, Karol Kurach, and James Martens. Adding gradient noise improves learning for very deep networks.  arXiv preprint arXiv:1511.06807 , 2015.

 [38] David Nualart.  The Malliavin calculus and related topics , volume 1995. Springer, 2006.

 [39] Felix Otto and C´ edric Villani. Generalization of an inequality by Talagrand and links with the logarithmic Sobolev inequality.  Journal of Functional Analysis , 173(2):361– 400, 2000.

 [40] Sam Patterson and Yee Whye Teh. Stochastic gradient Riemannian Langevin dynamics on the probability simplex.  Advances in neural information processing systems , 26, 2013.

 [41] Grigorios A Pavliotis.  Stochastic processes and applications: diﬀusion processes, the Fokker-Planck and Langevin equations , volume 60. Springer, 2014.

 [42] MS Pinsker. Information and information stability of random quantities and processes. Holden-Day , 1964.

 [43] Maxim Raginsky, Alexander Rakhlin, and Matus Telgarsky. Non-convex learning via stochastic gradient Langevin dynamics: a nonasymptotic analysis. In  Conference on Learning Theory , pages 1674–1703. PMLR, 2017.

 [44] Herbert Robbins and Sutton Monro. A stochastic approximation method.  The annals of mathematical statistics , pages 400–407, 1951.

 [45] Filippo Santambrogio. Optimal transport for applied mathematicians.  Birk¨ auser, NY , 55(58-63):94, 2015.

 [46] Samuel Smith, Erich Elsen, and Soham De. On the generalization beneﬁt of noise in stochastic gradient descent. In  International Conference on Machine Learning , pages 9058–9067. PMLR, 2020.

 [47] Samuel L Smith, Benoit Dherin, David GT Barrett, and Soham De. On the origin of implicit regularization in stochastic gradient descent.  arXiv preprint arXiv:2101.12176 , 2021.

 [48] Michel Talagrand. A new isoperimetric inequality and the concentration of measure phenomenon. In  Geometric aspects of functional analysis , pages 94–124. Springer, 1991.

 [49] Max Welling and Yee W Teh. Bayesian learning via stochastic gradient Langevin dynamics. In  Proceedings of the 28th international conference on machine learning (ICML-11) , pages 681–688. Citeseer, 2011.  

[50] Lei Wu, Chao Ma, et al. How SGD selects the global minima in over-parameterized learning: A dynamical stability perspective.  Advances in Neural Information Processing Systems , 31, 2018.

 [51] Yuchen Zhang, Percy Liang, and Moses Charikar. A hitting time analysis of stochastic gradient Langevin dynamics. In  Conference on Learning Theory , pages 1980–2022. PMLR, 2017.

 [52] Liu Ziyin, Botao Li, James B Simon, and Masahito Ueda. SGD with a constant large learning rate can converge to local maxima.  arXiv preprint arXiv:2107.11774 , 2021.

 [53] Difan Zou, Pan Xu, and Quanquan Gu. Faster convergence of stochastic gradient Langevin dynamics for non-log-concave sampling. In  Uncertainty in Artiﬁcial Intelli- gence , pages 1152–1162. PMLR, 2021.  