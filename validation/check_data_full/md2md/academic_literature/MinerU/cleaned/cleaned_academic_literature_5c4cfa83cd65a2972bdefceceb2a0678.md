# Non-Stationary Stochastic Global Optimization Algorithms  

Jonatan Gomez  $\cdot$   Carlos Rivera  

the date of receipt and acceptance should be inserted later  

Abstract  Gomez (2019) proposes a formal and systematic approach for char- acterizing stochastic global optimization algorithms. Using it, Gomez formal- izes algorithms with a ﬁxed next-population stochastic method, i.e., algorithms deﬁned as stationary Markov processes. These are the cases of standard ver- sions of hill-climbing, parallel hill-climbing, generational genetic, steady-state genetic, and diﬀerential evolution algorithms. This paper continues such a sys- tematic formal approach. First, we generalize the suﬃcient conditions conver- gence lemma from stationary to non-stationary Markov processes. Second, we develop Markov kernels for some selection schemes. Finally, we formalize both simulated-annealing and evolutionary-strategies using the systematic formal approach.  

Keywords  Evolutionary Algorithms  ·  Non-stationary Markov Kernel Convergence Analysis  ·  Evolutionary Strategies  ·  Simulated Annealing Selection Mechanism  

Mathematics Subject Classiﬁcation (2010)  MSC 68T20  ·  MSC 65K10  

<td><table  border="1"><thead><tr><td></td><td><b>Algorithm 1 Stochastic Global Optimization Algorithm - SGoAL.</b></td><td><b>t=t+1</b></td><td><b>t=t+1</b></td></tr></thead><tbody><tr><td>SGoAL(n)</td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td>1: t= 0</td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td>2: Po = INITPoP(n)</td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td></td><td>3: while -END(Pt , t) do</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td>4:</td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td>5:</td><td>Pt+1 = NExTPoP( Pt )</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td>5:</td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td>5:</td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td>6: return BEsT(Pt)</td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td></td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td></td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr><tr><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td><td>t=t+1</td></tr></tbody></table></td>  

# 1 Introduction  

This section provides a brief introduction to the systematic formalization pro- posed by Gomez (2019). Such systematic formalization of stochastic global SGoal optimization algorithms ( s  in short), is carried on Markov kernels terms. Gomez can formalize  SGoal s with ﬁxed  NextPop  stochastic method, i.e.,  SGoal s that can be characterized as stationary Markov processes. That is the case of the hill-climbing (Russell and Norvig (2009)), the parallel hill- climbing, the generational genetic (De Jong (1975); Holland (1975); Mitchell (1996)), the steady-state genetic (Goldberg and Deb (1991)), and the diﬀeren- tial evolution (Das and Suganthan (2011); Storn and Price (1997)) algorithms. However,  SGoal s such as the Simulated Annealing (Kirkpatrick et al. (1983)), Evolutionary Strategies (Beyer and Schwefel (2002)), or any algorithm using parameter control/adaptation techniques (Eiben et al. (1999)) cannot be char- acterized as stationary Markov processes.  

# 1.1 Stochastic Global Optimization  

The problem of ﬁnding a point    $x^{*}\in\varOmega\subseteq\varPhi$   where a function    $f:\varPhi\rightarrow\mathbb{R}$   reaches its best/optimal value   $\left(f^{*}\right)$  , is considered as a global optimization problem, see equation 1. Here,    $\varPhi$   is the solution space,    $\varOmega$  is the feasible region,    $x^{*}$  is the optimizer,    $f$   is the objective function, and    $\vartriangleleft$  is the optimization relation:    $\vartriangleleft$  is  $<$   if minimizing and it is    $>$   if maximizing.  

$$
o p t i m i z e\left(f:\varPhi\rightarrow\mathbb{R}\right)=x^{*}\in\varOmega\subseteq\varPhi\mid\left(\forall y\in\varOmega\right)\left(f\left(x^{*}\right)\leq f\left(y\right)\right)
$$  

A stochastic global optimization algorithm ( SGoal ) iteratively generates a (possibly) better population of candidate solutions using a stochastic oper- ation, see algorithm 1. Here,  InitPop  :    $\mathbb{N}\,\rightarrow\,\Omega^{n}$    initializes a population    $P$  having size    $n$  ,  NextPop  :    $\varOmega^{n}\rightarrow\varOmega^{n}$    stochastically generates a new popula- tion from the current one,    $\mathrm{BEST:}\,\varOmega^{n}\to\varOmega$  obtains the ﬁttest individual (see equation 2), and    $\mathrm{END}:\varOmega^{n}\times\mathbb{N}\rightarrow B o o l$   is a stopping condition. Notice that if there is a Markov kernel characterizing the  NextPop  method, the stochastic sequence  (  $P_{t}:t\geq0$  )  becomes a Markov process.  

$$
\operatorname{BEST}\left(x\right)=x_{i}\mid\forall_{k=1}^{n}f\left(x_{i}\right)\triangleleft f\left(x_{k}\right)\wedge f\left(x_{i}\right)\triangleleft\forall_{k=1}^{i-1}f\left(x_{k}\right)
$$  

# 1.2 Markov Process  

A function    $K\ :\ \varOmega_{1}\times\varSigma_{2}\ \rightarrow\ [0,1]$  , with    $\left(\varOmega_{1},\varSigma_{1}\right)$   and    $\left(\Omega_{2},\Sigma_{2}\right)$   measurable spaces, is called a  (Markov) kernel  if the following two conditions hold:  

1. Function    $K_{x,\bullet}:A\mapsto K(x,A)$   is a probability measure for each ﬁxed    $x\in\varOmega_{1}

$  2. Function    $K_{\bullet,A}\ :\ x\ \mapsto\ K(x,A)$   is a measurable function for each ﬁxed  $A\in\Sigma_{2}$  .  

Gomez considers kernels having transition densities. If the transition den- sity    $K\colon\varOmega_{1}\times\varOmega_{2}\rightarrow[0,1]$   exists, then the transition kernel can be deﬁned using equation 3.  

$$
K\left(x,A\right)=\int_{A}K\left(x,y\right)d y
$$  

Composition of two kernels (  $K_{1}$   and    $K_{2}$  ) is deﬁned in terms of the kernel multiplication operator, see equation 4. Since the kernel multiplication is an associative operator Fristedt and Gray (1997), the ordered composition of    $n$  transition kernels    $K_{1}$  , ...,    $K_{n}$   is the product kernel    $K_{n}\circ K_{n-1}\circ.\,.\,.\circ K_{1}$  .  

$$
\left(K_{2}\circ K_{1}\right)(x,A)=\int K_{2}\left(y,A\right)K_{1}\left(x,d y\right)
$$  

Finally, the probability to transit to some set    $A\in\Sigma$   within    $t$   steps when starting at state    $x\,\in\,\Omega$  , using kernel    $K$  , is given by equation 5. While the probability that such a Markov process is in set    $A\in\Sigma$   at step    $t\geq0$  , when  $p:\Sigma\to[0,1]$   is the initial distribution of subsets, is given by equation 6.  

$$
K^{(t)}\left(x,A\right)=\left\{\int_{\Omega}K^{\left(t-1\right)}\left(y,A\right)K\left(x,d y\right)\right.\ \mathrm{~if~}t>1
$$  

$$
P r\left\{X_{t}\in A\right\}={\left\{\begin{array}{l l}{p\left(A\right)}&{{\mathrm{if~}}t=0}\\ {\displaystyle{\int_{\Omega}}K^{(t)}\left(x,A\right)p\left(d x\right)}&{{\mathrm{if~}}t>0}\end{array}\right.}
$$  

# 1.3 Convergence  

Gomez (2019) amends the convergence approach of Rudolph (1996) by deﬁning the set of    $\epsilon$  -states, i.e., a set with closeness function value less than    $\epsilon\in\mathbb{R}^{+}$  . Let  $\varOmega\subseteq\varPhi$   be a set,    $f:\varPhi\rightarrow\mathbb{R}$   be an objective function,    $\epsilon>0$   be a real number,  $x\in\varOmega^{m}$  , with    $m$   the size of the population, and    $d\left(x\right)=f\left({\mathrm{BET}}\left(x\right)\right)-f^{*}$  .  

1.    $x$   is an    $\epsilon$  -state  iﬀ  $x\in\varOmega^{m}=\{x\in\varOmega^{m}:d\left(x\right)<\epsilon\}$  ,

 2.    $x$   is an  ǫ -state (closed)  iﬀ  $x\in\varOmega_{\epsilon}^{m}=\left\{x\in\varOmega^{m}:d\left(x\right)\leq\epsilon\right\}$  ,

 3.    $x$   is an  $\widehat{\epsilon}\cdot$  -state (adherent)  iﬀ  $x\in\varOmega_{\widehat{\epsilon}}^{m}=\left\{x\in\varOmega^{m}:d\left(x\right)=\epsilon\right\}$  .  

Proposition 1.  Let    $P_{t}\,\in\,\Omega^{n}$    be the population maintained by an  SGoal .  $A$   SGoal  converges to the global optimum if its associated random sequence (  $\dot{\left(D_{t}=d\left(P_{t}\right):t\geq0\right)}$  , converges completely to zero, i.e., equation 7 holds for every    $\epsilon>0$  .  

$$
\operatorname*{lim}_{t\to\infty}\sum_{i=1}^{t}P r\left\{|D_{t}|>\epsilon\right\}<\infty
$$  

# 2 Generalizing the Systematic Formal Approach to Non-Stationary SGoal s  

For a  non-stationary (or non-homogeneous)  Markov process, the transi- tion probabilities (kernel) may change over time (Bowerman (1974)). Suppose that    $K_{t}$   is the transition kernel applied at time    $t\ >\ 0$   of a non-stationary Markov process. Then, the transition kernel of such non-stationary Markov process at time    $t$   is deﬁned as    $K^{(t)}\,=\,K_{t}\circ K_{t-1}\circ.\,.\,.\circ K_{1}$  . Clearly, we can rewrite the transition kernel of a non-stationary Markov process (equation 8) to resemble equation 5.  

$$
K^{(t)}\left(x,A\right)=\left\{\int_{\varOmega}\!\!K^{(t-1)}\left(y,A\right)K_{t}\left(x,d y\right)\right.\ \mathrm{~if~}t>1
$$  

Now we are in the position of generalizing Lemma 71 in Gomez (2019) to non-stationary Markov processes.  

Lemma 2.  If for all    $t\geq1$   we have that    $K_{t}\left(x,\varOmega_{\epsilon}\right)\geq\delta>0$   for all    $x\in\Omega_{\epsilon}^{c}$    and  $K_{t}\left(x,\varOmega_{\epsilon}\right)=1$   for all    $x\in\varOmega_{\epsilon}$  , then    $K^{(t)}\left(x,\varOmega_{\epsilon}\right)\geq1-\left(1-\delta\right)^{t}$    holds for    $t\geq1$  .  

Proof.  We just rewrite the proof of Lemma 71 in Gomez (2019) (Gomez uses induction on    $t$  ) but taking care of the non-stationary property of the Markov process. For    $t\,=\,1$   we have that    $K^{(t)}\left(x,\varOmega_{\epsilon}\right)\,=\,K_{t}\left(x,\varOmega_{\epsilon}\right)$   (equation 5), so  $K^{(t)}\left(x,\varOmega_{\epsilon}\right)\geq\delta$   (condition lemma), therefore    $K^{(t)}\left(x,\varOmega_{\epsilon}\right)\geq1-\left(1-\delta\right)^{t}$    (  $t=$  1  and numeric operations). Here, we will use the notation (as Gomez did)  $K^{(t)}\left(y,\varOmega_{\epsilon}\right)=K_{y}^{(t)}\left(\varOmega_{\epsilon}\right)$   to reduce the visual length of the equations.  

$\begin{array}{r l}&{K_{i}^{(k+1)}\left(\varOmega_{i}\right)}\\ &{=\int K_{i}^{(k)}\left(\varOmega_{i}\right)K_{i}\left(x,d y\right)}\\ &{=\int K_{i}^{(k)}\left(\varOmega_{i}\right)K_{i}\left(x,d y\right)+\int K_{i}^{(k)}\left(\varOmega_{i}\right)K_{i}\left(x,d y\right)}\\ &{=\int K_{i}\left(x,d y\right)+\int K_{i}^{(k)}\left(\varOmega_{i}\right)K_{i}\left(x,d y\right)}\\ &{=K_{i}\left(x,d z\right)+\int K_{i}^{(k)}\left(\varOmega_{i}\right)K_{i}\left(x,d y\right)}\\ &{\stackrel{K_{i}}{\geq}K_{i}\left(x,d z\right)+\int K_{i}^{(k)}\left(\varOmega_{i}\right)K_{i}\left(x,d y\right)}\\ &{\geq K_{i}\left(x,d z\right)+\int K_{i}^{(k)}\left(1-\delta_{i}^{(k)}\right)\int K_{i}\left(x,d y\right)}\\ &{\geq K_{i}\left(x,d z\right)+\int K_{i}^{(k)}\left(1-\delta_{i}^{(k)}\right)\frac{K_{i}^{(k)}}{4\pi}}\\ &{\geq K_{i}\left(x,d z\right)+K_{i}\left(x,d y\right)-\delta K_{i}\left(x,d z\right)}\\ &{\geq1-(1-\delta_{i}^{(k)})\left(1-K_{i}\left(x,d z\right)\right)}\\ &{\geq1-(1-\delta_{i}^{(k)})\left(1-\delta_{i}^{(k)}\right)}\end{array}$   $\left(\Omega=\Omega_{\epsilon}\bigcup\Omega_{\epsilon}^{c}\right)$  S  Ω (If    $y\in\Omega_{\epsilon}$  ,   $K_{y}^{(t)}\left(\varOmega_{\epsilon}\right)=1$  (def kernel) (Induction hypothesis) (Probability) (condition lemma)  

Finally, Theorem 72 in Gomez (2019) also holds for non-stationary Markov processes. So, in order to show convergence of a non-stationary  SGoal  it is suﬃcient to prove that the  SGoal  satisﬁes the condition of lemma 2.  

Theorem 3.  (Theorem 72 in Gomez (2019) - a corrected version of Theorem 1 in Rudolph (1996))   $A$   SGoal  whose stochastic kernel satisﬁes    $K^{(t)}\left(x,\varOmega_{\epsilon}\right)\geq$   $1-(1-\delta)^{t}$    for all    $t\geq1$   will converge to the global optimum   $(f^{*})$   of a well- deﬁned real-valued function    $f:\varPhi\rightarrow\mathbb{R}$  , deﬁned in an arbitrary space    $\varOmega\subseteq\varPhi$  , regardless of the initial distribution    $p\left(\cdot\right)$  .  

Proof.  See proof of Theorem 72 in Gomez (2019).  

# 3 Selection Schemes Formalization  

A  Selection Scheme , is a method of selecting a group of individuals from a population (Blickle and Thiele (1996)). Many schemes deﬁne an individual selection mechanism  s1  $\colon\Omega^{\lambda}\rightarrow\Omega$  , and selects a group of individuals by re- peatedly applying  s1 . In this paper, we study the uniform, ﬁtness proportional, tournament (Miller et al. (1995)), roulette, and ranking selection schemes:  

1. A  uniform  scheme ( Uniform1 :    $\varOmega^{\lambda}\rightarrow\varOmega$  ) gives to each candidate solution  $i=1,2,\dots,\lambda$  , the same selection’s probability    $\begin{array}{r}{p\left(x_{i}\right)=\frac{1}{\lambda}}\end{array}$  .

 2. A  ﬁtness proportional  scheme ( Proportional1 :    $\dot{\Omega}^{\lambda}\;\rightarrow\;\Omega$  ) gives to each candidate solution    $i=1,2,\dots,\lambda$  , a selection’s probability    $p\left(x_{i}\right)$   such that    $p\left(x_{i}\right)<p\left(x_{j}\right)$   if    $f\left(x_{j}\right)\triangleleft f\left(x_{i}\right)$   and    $p\left(x_{i}\right)=p\left(x_{j}\right)$   if    $f\left(x_{i}\right)=f\left(x_{j}\right)$  .  

3. A  tournament  scheme   $\bigl(\mathrm{TOTRNAMENT}1^{m}\colon\varOmega^{\lambda}\rightarrow\varOmega\bigr)$  ) of size    $m$   chooses    $m$  individuals using a  Uniform  scheme and selects an individual from these using a  Proportional1  scheme,  Tournament1  $^m=$   Proportional1  ◦ m   Uniform .

 4. A  roulette  scheme ( Roulette1 :    $\varOmega^{\lambda}\rightarrow\varOmega$  ) is a ﬁtness proportional one where    $\begin{array}{r}{p\left(x_{i}\right)=\frac{r a t e\left(x_{i}\right)}{\sum_{i=1}^{\lambda}r a t e\left(x_{i}\right)}}\end{array}$   with    $r a t e\left(x_{i}\right)<r a t e\left(x_{j}\right)$   if    $f\left(x_{j}\right)\triangleleft f\left(x_{i}\right)$   and rate  $\left(x_{i}\right)=r a t e\left(x_{j}\right)$   if    $f\left(x_{i}\right)=f\left(x_{j}\right)$  . If    $f\left(x_{i}\right)\geq0$   for all    $i=1,2,\dots,\lambda$  and maximizing then    $r a t e\left(x_{i}\right)$   can be set to    $f\left(x_{i}\right)$  .

 5. A  ranking  scheme ( Ranking1 :    $\varOmega^{\lambda}\rightarrow\varOmega$  ) is a roulette one with  rate    $(x_{i})=$   $1+|\{x_{k}\!:f\left(x_{i}\right)\triangleleft f\left(x_{k}\right)\}|$  . Proposition 4.  If  s1 :    $\varOmega^{\lambda}\rightarrow\varOmega$  is a selection scheme with kernel    $K_{\mathrm{s1}}$   then  $\mathrm{S}\colon\varOmega^{\lambda}\rightarrow\varOmega^{\mu}$     $K_{\mathrm{s}}=\circledast_{i=1}^{\mu}K_{\mathrm{s}1}$  has kernel   . Corollary 5.  If  s1  is based on a probability function then  $K_{\mathrm{s}}$   is a kernel. Corollary 6.  The  Uniform, Proportional, Tournament, Roulette and  Ranking  selection schemes have Markov kernels.  

# sa 4 Simulated Annealing ( )  

# 4.1 Concept  

The Simulated Annealing algorithm ( sa ) considers the idea behind the process of heating and cooling a material to recrystallize it, see algorithm 2. When the temperature decreases, the material settles into a more ordered state, and the state into which they settle is not always the same. This state tends to have low energy compared when the material is in the presence of high temperature (Simon (2013)). If we consider energy as a cost function, we can use this approach to minimize cost functions. Therefore, SA is an stochastic algorithm that works with a single-individual that generates a single candidate- solution    $x$   (parent) and sets a high temperature to explore the search space. Then, some variation mechanism generates a new candidate-solution    $x^{\prime}$    (child) and measures its cost. A replacement policy, that ﬁtness function and the temperature, picks one individual between the father and the child. Finally, a process decreases the temperature looking for each new solution having less energy.  

Clearly, the replacement policy in algorithm 2 (lines 6,...,11) is not elitist. This allows  sa  to expand the search but can lead to the loss of some good candidate-solutions. In practice, it is normal to keep track of the best solution found so farSimon (2013). If this is done, the replacement policy is an elitist one.  

# 4.2 Formalization  

To formalize and characterize ( sa ), we use the approach proposed by Gomez (2019). We rewrite algorithm 2 in terms of individual non-stationary stochas-  

<td><table  border="1"><thead><tr><td><b>Algorithm 2 Simulated Annealing Simon (2013)</b></td></tr></thead><tbody><tr><td>SIMULATED ANNEALING</td></tr><tr><td>l: T = initial temperature > 0</td></tr><tr><td>2: α(T) = cooling function: α(T) E [0, T] for all T</td></tr><tr><td>3: Initialize a candidate solution co to minimization problem f(αc)</td></tr><tr><td>4: while -TERMINATIONCoNDITION() do</td></tr><tr><td>Generate a candidate solution </td></tr><tr><td>6:</td></tr><tr><td>7:</td></tr><tr><td>8:</td></tr><tr><td>9:</td></tr><tr><td>r = U[0, 1] if r < eap[(f(ro) - f(c)/T)</td></tr><tr><td>10:</td></tr><tr><td>11: 12:</td></tr></tbody></table></td>  

# Algorithm 3  Simulated Annealing in terms of  VR  methods  

SA (x) 1:    ${\boldsymbol{x}}^{\prime}=\scriptstyle\mathrm{VaRIATE}_{S A}(\mathrm{\boldsymbol{x}})$  2:    ${\boldsymbol{x}}^{\prime}=\scriptstyle\mathrm{REPLACE}_{S A_{T}}(\mathbf{x}^{\prime},\mathbf{x})$   UpdateParameters 3: (T) 4:  return    $x^{\prime}$  

tic methods, see algorithm 3. This new algorithm is in terms of  Variation - Replacement  methods. Observe that algorithms 2 and 3 are equivalents. Line 5 of algorithm 2 is the method  Variate  $S A$   (line 1) of algorithm 3; lines 6 to 11 of algorithm 2 is the method  Replace  $S A$   (line 2) of algorithm 3. Finally, line 12 of algorithm 2 and method  UpdateParameters  (line 3) perform the same task.  

Now, we concentrate on characterizing ( sa ) as a VR stochastic method and analyzing its convergence through non-stationary Markov kernels.  

Proposition 7.  If  Replace  $_{S A}(x,x)$   is an elitist method, then it can be char- acterized by the Markov Kernel    $R_{S A}\colon\varOmega^{2}\times\varSigma\longrightarrow[1,0]$   deﬁned as  

$$
K_{R_{S A}}=\pi_{1}\circ s_{2}
$$  

Proof.  It is deﬁned in the same way that the method of    $\mathrm{R}_{H C}$   in Gomez (2019). So the proof uses the same argument that lemma 75 of Gomez (2019).  

Proposition 8.  if the stochastic method  Variate  $A S_{T}$   can be characterized by a non-stationary Markov kernel    $V_{S A_{T}}^{(t)}\colon\varOmega\times\varSigma\longrightarrow[1,0]$   and condition of proposition 7 are fulﬁlled then method the  NextPop  $s A(x)$   can be described as  VR  $a$   non-stationary Markov Kernel deﬁned as  

$$
K_{S A}^{(t)}=K_{R}\circ K_{V_{S A_{T}}}^{(t)}
$$  

Proof.    $K_{S A}^{(t)}$    is a kernel composition under the given conditions. SA  

Proposition 9.  if  Replace  $_{S A}$   is an elitist method, then  NextPop  $S A$   can be characterized by an elitist non-stationary Markov kernel.  

Proof.  This proof uses the same argument as proposition 77 in Gomez (2019).  

4.3 Convergence  

Corollary 10.  if conditions of propositions 7, 8 and 9, are fulﬁlled and method Variate  $A S_{T}$   is optimal strictly bounded from zero then  NextPop  $_{S A}$   is opti- mal strictly bounded from zero.  

Proof.  Follows from deﬁnition 67, lemma 68, and deﬁnition 69 in Gomez (2019) and proposition 9 that establish that  NextPop  $S A$   can be characterized by an elitist kernel, and this is optimal strictly bounded from zero.  

Theorem 11.  sa  will converge to the global optimum if  Replace S A  is elitist and if  Variate  $A S_{T}$   is optimal strictly bounded from zero.  

Proof.  Follows from corollary 10, and propositions 7, 8 and 9.  

# es 5 Evolutionary Strategies ( )  

# 5.1 Concept  

Evolutionary Strategies   $(\mu/\rho+\lambda)$  )- es  are a type of Evolutionary Algorithms that apply mutation, recombination, and selection operators to a popula- tion of individuals Beyer and Schwefel (2002), see algorithm 4. Every indi- vidual is an  es  that has two parts: the candidate solution (  $x$  ) and the set of endogenous strategy parameters ( s ) used to control the mutation operator (Beyer and Schwefel (2002)). An  es  randomly initializes the population, line 2, and evolves both parts of the individual (lines 5-9) up to certain ending- condition is fulﬁlled (line 3). The set of endogenous parameters are exposed to evolution (lines 6 and 8) before producing a child candidate solution (line 7 and 9) to introduce variety. The new individual is a composition of a set of selected candidate solutions (line 5).  es  generates a new population of    $\lambda$  new individuals each generation (line 4). Finally,  es  selects a ﬁnal population using two possible approaches. The   $(\mu+\lambda)$  - es  approach that selects the best  individuals among the    parents and    $\lambda$   children or the   $(\mu,\lambda)$  - es  that selects  $\mu$   $\mu$  the best    $\mu$   individuals from the    $\lambda$   children (notice that    $\lambda\geq\mu$   in this case). In this work, we study both of them.  

<td><table  border="1"><thead><tr><td><b>Algorithm 4 Evolutionary strategies described by Beyer and Schwefel (2002)</b></td></tr></thead><tbody><tr><td>ES(μ/p+^)</td></tr><tr><td>1: g=0</td></tr><tr><td>αl = MARRIAGE(P, p)</td></tr><tr><td>3: while -TERMINATIONCoNDITION() do</td></tr><tr><td>4:</td></tr><tr><td>5: </td></tr><tr><td>6:</td></tr><tr><td>7:</td></tr><tr><td>8:</td></tr><tr><td>9:</td></tr><tr><td>Fl = F(yi) ui,- MUTATIONs(yl, s))</td></tr><tr><td>10:</td></tr><tr><td>11:</td></tr><tr><td>12:</td></tr><tr><td>13: 14:</td></tr><tr><td>else (μ + ^)</td></tr><tr><td>15:</td></tr></tbody></table></td>  

5.2 Formalization  

To formalize and characterize   $(\mu/\rho\,{\overset{+}{,}}\,\lambda)$  )- es , we rewrite algorithm 4 in terms of individual non-stationary stochastic methods, see algorithm 5. This follows the approach in Gomez (2019) that express the algorithms in terms of Variation- Replacement methods to study their convergence properties.  

Notice that algorithms 4 and 5 are equivalents: lines 4-11 in algorithm 4 is method  Variate (P) (line 1) in the  NextPop  method of algorithm 5. Also, lines 12-15 in algorithm 4 are line 2 in the  NextPop  method of algorithm 5. Using this characterization, we proceed to characterize each method of algo- rithm 5 through non-stationary Markov kernels.  

With the object of characterizing   $\left(\mu/\rho\,\vec{;}\,\lambda\right)$  )-ES we need to establish some non-stationary Markov kernels. First, we study the  Variate  method (line 1, method  NextPop , algorithm 5).  

Following deﬁnition 53 in Gomez (2019), we can express the variation method  Variate :    $\varOmega^{\mu}\longrightarrow\varOmega^{\lambda}$    as a joined stochastic method.  

$$
\begin{array}{r}{\operatorname{VaRIAE}(P)=\prod_{i=1}^{\lambda}\operatorname{NEXYT S U BPOP}_{i}(P)}\end{array}
$$  

Where  NextSubPop :    $\Omega^{\mu}\implies\Omega$  chooses    $\rho$   individuals from the popu- lation, combines the    $\rho$   individuals, generates a child and ﬁnally mutates the strategy and the child.  

Proposition 12.  If lines   $^{8}$   and   $g$   of method  UpdateStrategies  of algorithm  $\it5$   can be characterized by non-stationary kernels    $X\colon\mathbb{R}^{\rho}\times\mathcal{B}(\mathbb{R})^{\otimes\rho}\longrightarrow[0,1]$  and    $V S^{(t)}\colon\mathbb{R}\times\mathcal{B}(\mathbb{R})\longrightarrow[0,1]$   respectively.  UpdateStrategies  can be char- acterized by a non-stationary kernel    $U S^{(t)}\colon\mathbb{R}^{\rho}\times\mathcal{B}(\mathbb{R})\longrightarrow[0,1]$   deﬁned as:  

$$
K_{U S}^{(t)}=K_{V S}^{(t)}\circ K_{X S}
$$  

<td><table  border="1"><thead><tr><td><b>NEXTSUBPOP;(P)</b></td><td><b>in terms of VR methods</b></td><td><b>in terms of VR methods</b></td><td><b>in terms of VR methods</b></td></tr></thead><tbody><tr><td colspan="5">NEXTSUBPOP;(P)</td></tr><tr><td>1: α = PICKPARENTs(P)</td><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>2: q = XoVERa(P)</td><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>3: UPDATESTRATEGIESa(s, i)</td><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>in terms of VR methods</td><td>4: q' = VARIATEs(q)</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>5: return q'</td><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>UPDATESTRATEGIESa(s, i)</td><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>in terms of VR methods</td><td>1: s' = XOVERSTRATEGIEa(s)</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>in terms of VR methods</td><td>2: Si = VARIATESTRATEGIE(s')</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>VARIATE(P)</td><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>l: for i= 1 to ^ do</td><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>3: return Q</td><td>Qi = NEXTSUBPOPi(P)</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>NEXTPOP(P)</td><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>1: Q' = VARIATE(P)</td><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>2: Q = REPLACE(P, Q')</td><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>3: return Q</td><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr><tr><td>in terms of VR methods</td><td>in terms of VR methods</td><td>in terms of VR methods</td></tr></tbody></table></td>  

Proof.  It is in terms of kernel composition, follows from deﬁnition 25 of Gomez (2019).  

Proposition 13.  If lines   $\mathcal{Q}$   and  $\it{4}$   of algorithm   $5$   can be characterized by non- stationary Markov kernels    $\mathrm{XOVER}_{a}\colon(\varOmega^{\rho}\times\varSigma)\longrightarrow[0,1]$   and    $\mathrm{VaRIATE}_{s}$   :   $(\varOmega\times$   $\Sigma)\longrightarrow[0,1]$   respectively, then the method  NextSubPop  can be characterized by the kernel  NextSubPop :   $\left(\varOmega^{\rho}\times\varSigma\right)\longrightarrow[0,1]$   deﬁned as the non-stationary kernel:  

$$
K_{\mathrm{NextPSUparrow}}=K_{\mathrm{VaRIAE}_{s}}^{(t)}\circ K_{X O V E R}\circ\pi_{\left\{1,\dots,\rho\right\}}\circ K_{\mathcal{P}}
$$  

Proof.  It is in terms of kernel composition, follows from deﬁnition 25 of Gomez (2019).  

Proposition 14.  If  NextSubPop  can be characterized by a non-stationary  $(t)$    Markov kernel, the stochastic method  Variate can be characterized by   $a$  kernel    $V\colon\varOmega^{\mu}\times\varSigma^{\otimes\mu}\longrightarrow[0,1]$   deﬁned as  

$$
K_{\mathrm{VaRIATE}}^{(t)}=[\circledast_{i=1}^{\lambda}[K_{\mathrm{VaRTISUBPPO P}_{i}}]]
$$  

Proof.  It is a join stochastic method, follows from deﬁnition 55 and proposition 56 of Gomez (2019).  

Proposition 15.  The stochastic method  Replace  ${\binom{}{\mu+\lambda}}$   used in line   $\mathcal{Q}$   of method  NextPop , can be characterized by the kernel  $R_{\mu,\mu+\lambda}\colon\Omega^{\mu+\lambda}{\times}\Sigma^{\otimes\mu}\longrightarrow$   $[0,1]$   deﬁned as    $K_{R_{\mu,\mu+\lambda}}=\pi_{\left\{1,...,\mu\right\}}\circ s_{\mu+\lambda,\mu+\lambda-1}$   and the stochastic method  $\operatorname{REPLACE}_{(\mu,\lambda)}$  , can be characterized by the kernel    $R_{\mu,\lambda}\colon\varOmega^{\lambda}\times\varSigma^{\otimes\mu}\,\longrightarrow\,[0,1$  deﬁned as    $K_{R_{\mu,\lambda}}=\pi_{\left\{1,...,\mu\right\}}\circ s_{\lambda,\lambda-1}$  

Proof.    $K_{R_{\mu,\lambda}}$   and    $K_{R_{\mu+\lambda}}$   are kernels composition. Follows from deﬁnition 25 in Gomez (2019).  

Corollary 16.  If methods  PickParents ,  XOver  $^{-a}$  ,  XoverStrategie  $^{a}$  ,  Vari- ateStrategie  and,  Variate  $s$   can be described by Markov kernels fulﬁlling the conditions of   $\it{12}$   and 13, evolutionary Strategies can be described by a  VR kernel.  

$$
K_{E S}=K_{R}\circ K_{V}
$$  

where:  

$$
K_{V}=K_{\mathrm{VaRIATE}}
$$  

$$
K_{R}=K_{R_{\mu,\lambda}}\,\,\,o r\,\,K_{R}=K_{R_{\mu+\lambda}}
$$  

Proof.  Follows from propositions 12, 13, 14 and 15.  

# 5.3 Convergence  

Proposition 17.  The    $\operatorname{NEXP}(\mu/\rho+\lambda)\!-\!E S$   is an elitist stochastic method that can be characterized by an elitist stochastic kernel  

Proof.  Let    $k\ \in\ [1,\mu]$   be the index of the best individual in population    $P$  , then    $f(B E S T(P))=f(P_{k})$  . Since    $P\subseteq\{P\cup\operatorname{VARIE}(P)\}$   and the method Replace  is elitist. It is clear that    $f(B E S T(P\cup\operatorname{VARIOTE}(P)))\triangleleft f(P_{k})$  .  

Corollary 18.  If conditions of proposition 12 and 13 are satisﬁed and  Variate  $s$  is optimal strictly bounded from zero then the method    $\operatorname{NEXP}_{\mu+\lambda}$   is optimal strictly from zero.  

Proof.  Follows from deﬁnition 67, lemma 68, and deﬁnition 69 of Gomez (2019) and proposition 17 that establish that an elitist kernel is optimal strictly bounded from zero.  

Theorem 19.    $(\mu/\rho+\lambda)$  -ES will converge to the global optimum if meth- ods  PickParents  and  Variate  $_s^{(t)}$  can be characterized by stationary or non- stationary Markov kernels and  Variate  $s$   is optimal strictly bounded from zero.  

Proof.  Follows from theorem 3 and corollary 18.  

# 6 Conclusion  

In this paper we have generalized the conditions of convergence to the global optimum from stationary to non-stationary Markov process that are present in the work of stochastic global optimization algorithms: a systematic approach proposed by Gomez (2019). We formalize some selection schemes to generalize the theory to cover as many variations of each algorithm as possible. Also, we formalized and characterized both simulated-annealing and evolutionary- strategies using the developed theory. There, we established which conditions must be fulﬁlled to achieve a global convergence in both algorithms. Our fu- ture work will concentrate on using the proposed approach to formalize as many stationary and non-stationary  SGoal  as possible, and extending and developing the theory for several particular methods that can be considered SGoal s.  

# References  

Beyer HG, Schwefel HP (2002) Evolution strategies - a comprehensive intro- duction. Natural Computing 1:3–52, DOI 10.1023/A:1015059928466 Blickle T, Thiele L (1996) A comparison of selection schemes used in evolu- tionary algorithms. Evolutionary Computation 4(4):361–394, DOI 10.1162/ evco.1996.4.4.361, URL  https://doi.org/10.1162/evco.1996.4.4.361 , https://doi.org/10.1162/evco.1996.4.4.361 Bowerman BL (1974) Nonstationary markov decision processes and related topics in nonstationary markov chains. PhD thesis, University of Iowa, URL https://lib.dr.iastate.edu/rtd/6327 Das S, Suganthan PN (2011) Diﬀerential evolution: A survey of the state-of- the-art. IEEE Transactions on Evolutionary Computation 15(1):4–31, DOI 10.1109/TEVC.2010.2059031 De Jong K (1975) An analysis of the Behavior of a class of genetic adaptive systems. PhD thesis, University of Michigan Eiben AE, Hinterding R, Michalewicz Z (1999) Parameter control in evolution- ary algorithms. IEEE Transactions in Evolutionary Computation 3(2):124– 141 Fristedt BE, Gray LF (1997) A Modern Approach to Probability Theory. Springer Science & Business Media Goldberg DE, Deb K (1991) A comparative analysis of selection schemes used in genetic algorithms. In: Foundations of Genetic Algorithms, Morgan Kauf- mann, pp 69–93 Gomez J (2019) Stochastic global optimization algorithms: A systematic formal approach. Information Sciences 472:53 – 76, DOI https://doi.org/10.1016/j.ins.2018.09.021, URL http://www.sciencedirect.com/science/article/pii/S 0020025517305248 Holland JH (1975) Adaptation in Natural and Artiﬁcial Systems. The Univer- sity of Michigan Press  

Kirkpatrick S, Gelatt CD, Vecchi MP (1983) Optimization by simu- lated annealing. Science 220(4598):671–680, DOI 10.1126/science.220.4598. 671, URL https://science.sciencemag.org/content/220/4598/671 , https://science.sciencemag.org/content/220/4598/671.full.pdf Miller BL, Miller BL, Goldberg DE, Goldberg DE (1995) Genetic algorithms, tournament selection, and the eﬀects of noise. Complex Systems 9:193–212 Mitchell M (1996) An introduction to genetic algorithms. MIT Press Rudolph G (1996) Convergence of evolutionary algorithms in general search spaces. In: In Proceedings of the Third IEEE Conference on Evolutionary Computation, IEEE Press, Piscataway (NJ, pp 50–54 Russell S, Norvig P (2009) Artiﬁcial Intelligence: A Modern Approach, 3rd edn. Prentice Hall Press, Upper Saddle River, NJ, USA Simon D (2013) Evolutionary Optimization algorithms. Wiley Storn R, Price K (1997) Diﬀerential evolution - a simple and eﬃ- cient heuristic for global optimization over continuous spaces. J of Global Optimization 11(4):341–359, DOI 10.1023/A:1008202821328, URL https://doi.org/10.1023/A:1008202821328  