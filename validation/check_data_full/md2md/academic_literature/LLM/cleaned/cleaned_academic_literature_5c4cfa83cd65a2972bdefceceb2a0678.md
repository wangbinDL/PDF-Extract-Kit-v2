# Non-Stationary Stochastic Global Optimization Algorithms 

Jonatan Gomez ${ }^{*}$ Universidad Nacional de Colombia Carlos Rivera


#### Abstract

Gomez (2019) proposes a formal and systematic approach for characterizing stochastic global optimization algorithms. Using it, Gomez formalizes algorithms with a fixed next-population stochastic method, i.e., algorithms defined as stationary Markov processes. These are the cases of standard versions of hill-climbing, parallel hill-climbing, generational genetic, steady-state genetic, and differential evolution algorithms. This paper continues such a systematic formal approach. First, we generalize the sufficient conditions convergence lemma from stationary to non-stationary Markov processes. Second, we develop Markov kernels for some selection schemes. Finally, we formalize both simulated-annealing and evolutionary-strategies using the systematic formal approach.


Keywords Evolutionary Algorithms - Non-stationary Markov Kernel - Convergence Analysis - Evolutionary Strategies - Simulated Annealing - Selection Mechanism

Mathematics Subject Classification (2010) MSC 68T20 MSC 65K10

[^0]
[^0]:    *Corresponding author




---

```
Algorithm 1 Stochastic Global Optimization Algorithm - SGoal.
    SGoal(n)
    1: $t=0$
    2: $P_{0}=\operatorname{InitPop}(n)$
    3: while $\neg \operatorname{End}\left(P_{t}, t\right)$ do
        4: $\quad P_{t+1}=\operatorname{NextPop}\left(P_{t}\right)$
        5: $\quad t=t+1$
    6: return best $\left(P_{t}\right)$
```

# 1 Introduction 

This section provides a brief introduction to the systematic formalization proposed by Gomez (2019). Such systematic formalization of stochastic global optimization algorithms (SGoals in short), is carried on Markov kernels terms. Gomez can formalize SGoals with fixed NextPop stochastic method, i.e., SGoals that can be characterized as stationary Markov processes. That is the case of the hill-climbing (Russell and Norvig (2009)), the parallel hillclimbing, the generational genetic (De Jong (1975); Holland (1975); Mitchell (1996)), the steady-state genetic (Goldberg and Deb (1991)), and the differential evolution (Das and Suganthan (2011); Storn and Price (1997)) algorithms. However, SGoals such as the Simulated Annealing (Kirkpatrick et al. (1983)), Evolutionary Strategies (Beyer and Schwefel (2002)), or any algorithm using parameter control/adaptation techniques (Eiben et al. (1999)) cannot be characterized as stationary Markov processes.

### 1.1 Stochastic Global Optimization

The problem of finding a point $x^{*} \in \Omega \subseteq \Phi$ where a function $f: \Phi \rightarrow \mathbb{R}$ reaches its best/optimal value $\left(f^{*}\right)$, is considered as a global optimization problem, see equation 1 . Here, $\Phi$ is the solution space, $\Omega$ is the feasible region, $x^{*}$ is the optimizer, $f$ is the objective function, and $\triangle$ is the optimization relation: $\triangle$ is $<$ if minimizing and it is $>$ if maximizing.

$$
\operatorname{optimize}(f: \Phi \rightarrow \mathbb{R})=\left.x^{*} \in \Omega \subseteq \Phi \right\rvert\,(\forall y \in \Omega)\left(f\left(x^{*}\right) \nabla f(y)\right)
$$

A stochastic global optimization algorithm (SGoal) iteratively generates a (possibly) better population of candidate solutions using a stochastic operation, see algorithm 1. Here, InitPop : $\mathbb{N} \rightarrow \Omega^{n}$ initializes a population $P$ having size $n$, NextPop $: \Omega^{n} \rightarrow \Omega^{n}$ stochastically generates a new population from the current one, Best $: \Omega^{n} \rightarrow \Omega$ obtains the fittest individual (see equation 2), and End : $\Omega^{n} \times \mathbb{N} \rightarrow$ Bool is a stopping condition. Notice that if there is a Markov kernel characterizing the NextPop method, the stochastic sequence $\left(P_{t}: t \geq 0\right)$ becomes a Markov process.

$$
\operatorname{Best}(x)=x_{i} \mid \forall_{k=1}^{n} f\left(x_{i}\right) \nabla f\left(x_{k}\right) \wedge f\left(x_{i}\right) \triangle \forall_{k=1}^{i-1} f\left(x_{k}\right)
$$




---

# 1.2 Markov Process 

A function $K: \Omega_{1} \times \Sigma_{2} \rightarrow[0,1]$, with $\left(\Omega_{1}, \Sigma_{1}\right)$ and $\left(\Omega_{2}, \Sigma_{2}\right)$ measurable spaces, is called a (Markov) kernel if the following two conditions hold:

1. Function $K_{x, \bullet}: A \mapsto K(x, A)$ is a probability measure for each fixed $x \in \Omega_{1}$
2. Function $K_{\bullet, A}: x \mapsto K(x, A)$ is a measurable function for each fixed $A \in \Sigma_{2}$.
Gomez considers kernels having transition densities. If the transition density $K: \Omega_{1} \times \Omega_{2} \rightarrow[0,1]$ exists, then the transition kernel can be defined using equation 3 .

$$
K(x, A)=\int_{A} K(x, y) d y
$$

Composition of two kernels $\left(K_{1}\right.$ and $\left.K_{2}\right)$ is defined in terms of the kernel multiplication operator, see equation 4 . Since the kernel multiplication is an associative operator Fristedt and Gray (1997), the ordered composition of $n$ transition kernels $K_{1}, \ldots, K_{n}$ is the product kernel $K_{n} \circ K_{n-1} \circ \ldots \circ K_{1}$.

$$
\left(K_{2} \circ K_{1}\right)(x, A)=\int K_{2}(y, A) K_{1}(x, d y)
$$

Finally, the probability to transit to some set $A \in \Sigma$ within $t$ steps when starting at state $x \in \Omega$, using kernel $K$, is given by equation 5 . While the probability that such a Markov process is in set $A \in \Sigma$ at step $t \geq 0$, when $p: \Sigma \rightarrow[0,1]$ is the initial distribution of subsets, is given by equation 6 .

$$
\begin{gathered}
K^{(t)}(x, A)= \begin{cases}K(x, A) & \text { if } t=1 \\
\int_{\Omega} K^{(t-1)}(y, A) K(x, d y) & \text { if } t>1\end{cases} \\
\operatorname{Pr}\left\{X_{t} \in A\right\}= \begin{cases}p(A) & \text { if } t=0 \\
\int_{\Omega} K^{(t)}(x, A) p(d x) & \text { if } t>0\end{cases}
\end{gathered}
$$

### 1.3 Convergence

Gomez (2019) amends the convergence approach of Rudolph (1996) by defining the set of $\epsilon$-states, i.e., a set with closeness function value less than $\epsilon \in \mathbb{R}^{+}$. Let $\Omega \subseteq \Phi$ be a set, $f: \Phi \rightarrow \mathbb{R}$ be an objective function, $\epsilon>0$ be a real number, $x \in \Omega^{m}$, with $m$ the size of the population, and $d(x)=f(\operatorname{Best}(x))-f^{*}$.

1. $x$ is an $\epsilon$-state iff $x \in \Omega_{\epsilon}^{m}=\left\{x \in \Omega^{m}: d(x)<\epsilon\right\}$,
2. $x$ is an $\epsilon$-state (closed) iff $x \in \bar{\Omega}_{\epsilon}^{m}=\left\{x \in \Omega^{m}: d(x) \leq \epsilon\right\}$,
3. $x$ is an $\widehat{\epsilon}$-state (adherent) iff $x \in \widehat{\Omega}_{\epsilon}^{m}=\left\{x \in \Omega^{m}: d(x)=\epsilon\right\}$.



---

Proposition 1. Let $P_{t} \in \Omega^{n}$ be the population maintained by an SGoal. A SGoal converges to the global optimum if its associated random sequence $\left(D_{t}=d\left(P_{t}\right): t \geq 0\right)$, converges completely to zero, i.e., equation 7 holds for every $\epsilon>0$.

$$
\lim _{t \rightarrow \infty} \sum_{i=1}^{t} \operatorname{Pr}\left\{\left|D_{t}\right|>\epsilon\right\}<\infty
$$

# 2 Generalizing the Systematic Formal Approach to Non-Stationary SGoals 

For a non-stationary (or non-homogeneous) Markov process, the transition probabilities (kernel) may change over time (Bowerman (1974)). Suppose that $K_{t}$ is the transition kernel applied at time $t>0$ of a non-stationary Markov process. Then, the transition kernel of such non-stationary Markov process at time $t$ is defined as $K^{(t)}=K_{t} \circ K_{t-1} \circ \ldots \circ K_{1}$. Clearly, we can rewrite the transition kernel of a non-stationary Markov process (equation 8 ) to resemble equation 5 .

$$
K^{(t)}(x, A)= \begin{cases}K_{1}(x, A) & \text { if } t=1 \\ \int_{\Omega} K^{(t-1)}(y, A) K_{t}(x, d y) & \text { if } t>1\end{cases}
$$

Now we are in the position of generalizing Lemma 71 in Gomez (2019) to non-stationary Markov processes.

Lemma 2. If for all $t \geq 1$ we have that $K_{t}\left(x, \Omega_{\epsilon}\right) \geq \delta>0$ for all $x \in \Omega_{\epsilon}^{c}$ and $K_{t}\left(x, \Omega_{\epsilon}\right)=1$ for all $x \in \Omega_{\epsilon}$, then $K^{(t)}\left(x, \Omega_{\epsilon}\right) \geq 1-(1-\delta)^{t}$ holds for $t \geq 1$.
Proof. We just rewrite the proof of Lemma 71 in Gomez (2019) (Gomez uses induction on $t$ ) but taking care of the non-stationary property of the Markov process. For $t=1$ we have that $K^{(t)}\left(x, \Omega_{\epsilon}\right)=K_{t}\left(x, \Omega_{\epsilon}\right)$ (equation 5 ), so $K^{(t)}\left(x, \Omega_{\epsilon}\right) \geq \delta$ (condition lemma), therefore $K^{(t)}\left(x, \Omega_{\epsilon}\right) \geq 1-(1-\delta)^{t}(t=$ 1 and numeric operations). Here, we will use the notation (as Gomez did) $K^{(t)}\left(y, \Omega_{\epsilon}\right)=K_{y}^{(t)}\left(\Omega_{\epsilon}\right)$ to reduce the visual length of the equations.




---

$$
\begin{aligned}
& \mathbb{K}_{x}^{(t+1)}\left(\Omega_{\epsilon}\right) \\
& \quad=\int_{\Omega} \mathbb{K}_{y}^{(t)}\left(\Omega_{\epsilon}\right) \mathcal{K}_{t}(x, d y) \quad \text { (equation 5) } \\
& \quad=\int_{\Omega_{\epsilon}} \mathbb{K}_{y}^{(t)}\left(\Omega_{\epsilon}\right) \mathcal{K}_{t}(x, d y)+\int_{\Omega_{\epsilon}^{c}} \mathbb{K}_{y}^{(t)}\left(\Omega_{\epsilon}\right) \mathcal{K}_{t}(x, d y) \quad\left(\Omega=\Omega_{\epsilon} \bigcup \Omega_{\epsilon}^{c}\right) \\
& \quad=\int_{\Omega_{\epsilon}} \mathcal{K}_{t}(x, d y)+\int_{\Omega_{\epsilon}^{c}} \mathbb{K}_{y}^{(t)}\left(\Omega_{\epsilon}\right) \mathcal{K}_{t}(x, d y) \quad\left(\text { If } y \in \Omega_{\epsilon}, \mathbb{K}_{y}^{(t)}\left(\Omega_{\epsilon}\right)=1\right) \\
& \quad=\mathcal{K}_{t}\left(x, \Omega_{\epsilon}\right)+\int_{\Omega_{\epsilon}^{c}} \mathbb{K}_{y}^{(t)}\left(\Omega_{\epsilon}\right) \mathcal{K}_{t}(x, d y) \quad \text { (def kernel) } \\
& \quad \geq \mathcal{K}_{t}\left(x, \Omega_{\epsilon}\right)+\left[1-(1-\delta)^{t}\right] \int_{A_{\epsilon}^{c}} \mathcal{K}_{t}(x, d y) \quad \text { (Induction hypothesis) } \\
& \geq \mathcal{K}_{t}\left(x, \Omega_{\epsilon}\right)+\left[1-(1-\delta)^{t}\right] \mathcal{K}_{t}\left(x, \Omega_{\epsilon}^{c}\right) \quad \text { (def kernel) } \\
& \geq \mathcal{K}_{t}\left(x, \Omega_{\epsilon}\right)+\mathcal{K}_{t}\left(x, \Omega_{\epsilon}^{c}\right)-(1-\delta)^{t} \mathcal{K}_{t}\left(x, \Omega_{\epsilon}^{c}\right) \\
& \geq 1-(1-\delta)^{t}\left(1-\mathcal{K}_{t}\left(x, \Omega_{\epsilon}\right)\right) \quad \text { (Probability) } \\
& \geq 1-(1-\delta)^{t}(1-\delta) \quad \text { (condition lemma) } \\
& \geq 1-(1-\delta)^{t+1}
\end{aligned}
$$

Finally, Theorem 72 in Gomez (2019) also holds for non-stationary Markov processes. So, in order to show convergence of a non-stationary SGoal it is sufficient to prove that the SGoal satisfies the condition of lemma 2 .

Theorem 3. (Theorem 72 in Gomez (2019) - a corrected version of Theorem 1 in Rudolph (1996)) A SGoal whose stochastic kernel satisfies $\mathbb{K}^{(t)}\left(x, \Omega_{\epsilon}\right) \geq$ $1-(1-\delta)^{t}$ for all $t \geq 1$ will converge to the global optimum $\left(f^{*}\right)$ of a welldefined real-valued function $f: \Phi \rightarrow \mathbb{R}$, defined in an arbitrary space $\Omega \subseteq \Phi$, regardless of the initial distribution $p(\cdot)$.

Proof. See proof of Theorem 72 in Gomez (2019).

# 3 Selection Schemes Formalization 

A Selection Scheme, is a method of selecting a group of individuals from a population (Blickle and Thiele (1996)). Many schemes define an individual selection mechanism $s_{1}: \Omega^{\lambda} \rightarrow \Omega$, and selects a group of individuals by repeatedly applying $s_{1}$. In this paper, we study the uniform, fitness proportional, tournament (Miller et al. (1995)), roulette, and ranking selection schemes:

1. A uniform scheme (Uniform $1: \Omega^{\lambda} \rightarrow \Omega$ ) gives to each candidate solution $i=1,2, \ldots, \lambda$, the same selection's probability $p\left(x_{i}\right)=\frac{1}{\lambda}$.
2. A fitness proportional scheme (Proportional1: $\Omega^{\lambda} \rightarrow \Omega$ ) gives to each candidate solution $i=1,2, \ldots, \lambda$, a selection's probability $p\left(x_{i}\right)$ such that $p\left(x_{i}\right)<p\left(x_{j}\right)$ if $f\left(x_{j}\right) \triangleright f\left(x_{i}\right)$ and $p\left(x_{i}\right)=p\left(x_{j}\right)$ if $f\left(x_{i}\right)=f\left(x_{j}\right)$.



---

3. A tournament scheme (Tournament ${ }^{1}{ }_{m}: \Omega^{\lambda} \rightarrow \Omega$ ) of size $m$ chooses $m$ individuals using a Uniform scheme and selects an individual from these using a Proportional ${ }^{1}$ scheme, Tournament $^{1}{ }_{m}=$ Proportional ${ }^{1} \circ$ Uniform $_{m}^{m}$.
4. A roulette scheme (Roulette ${ }^{1}: \Omega^{\lambda} \rightarrow \Omega$ ) is a fitness proportional one where $p\left(x_{i}\right)=\frac{\operatorname{rate}\left(x_{i}\right)}{\sum_{i=1}^{\lambda} \operatorname{rate}\left(x_{i}\right)}$ with rate $\left(x_{i}\right)<\operatorname{rate}\left(x_{j}\right)$ if $f\left(x_{j}\right) \triangleleft f\left(x_{i}\right)$ and rate $\left(x_{i}\right)=\operatorname{rate}\left(x_{j}\right)$ if $f\left(x_{i}\right)=f\left(x_{j}\right)$. If $f\left(x_{i}\right) \geq 0$ for all $i=1,2, \ldots, \lambda$ and maximizing then rate $\left(x_{i}\right)$ can be set to $f\left(x_{i}\right)$.
5. A ranking scheme (Ranking ${ }^{1}: \Omega^{\lambda} \rightarrow \Omega$ ) is a roulette one with rate $\left(x_{i}\right)=$ $1+\left|\left\{x_{k}: f\left(x_{i}\right) \triangleleft f\left(x_{k}\right)\right\}\right|$.

Proposition 4. If $s^{1}: \Omega^{\lambda} \rightarrow \Omega$ is a selection scheme with kernel $K_{s^{1}}$ then $s: \Omega^{\lambda} \rightarrow \Omega^{\mu}$ has kernel $K_{s}=\circledast_{i=1}^{\mu} K_{s^{1}}$.

Corollary 5. If $s^{1}$ is based on a probability function then $K_{s}$ is a kernel.
Corollary 6. The Uniform, Proportional, Tournament, Roulette and Ranking selection schemes have Markov kernels.

# 4 Simulated Annealing (sa) 

### 4.1 Concept

The Simulated Annealing algorithm (SA) considers the idea behind the process of heating and cooling a material to recrystallize it, see algorithm 2. When the temperature decreases, the material settles into a more ordered state, and the state into which they settle is not always the same. This state tends to have low energy compared when the material is in the presence of high temperature (Simon (2013)). If we consider energy as a cost function, we can use this approach to minimize cost functions. Therefore, SA is an stochastic algorithm that works with a single-individual that generates a single candidatesolution $x$ (parent) and sets a high temperature to explore the search space. Then, some variation mechanism generates a new candidate-solution $x^{\prime}$ (child) and measures its cost. A replacement policy, that fitness function and the temperature, picks one individual between the father and the child. Finally, a process decreases the temperature looking for each new solution having less energy.

Clearly, the replacement policy in algorithm 2 (lines 6,...,11) is not elitist. This allows $s a$ to expand the search but can lead to the loss of some good candidate-solutions. In practice, it is normal to keep track of the best solution found so far Simon (2013). If this is done, the replacement policy is an elitist one.

### 4.2 Formalization

To formalize and characterize (SA), we use the approach proposed by Gomez (2019). We rewrite algorithm 2 in terms of individual non-stationary stochas-




---

```
Algorithm 2 Simulated Annealing Simon (2013)
    Simulated annealing
1:    T}= initial temperature > 0
2:    \alpha(T)= cooling function: \alpha(T) \in[0, T] for all T
3:    Initialize a candidate solution x0 to minimization problem f(x)
4:    while ~TerminationCondition() do
5:        Generate a candidate solution x
6:        if f(x)<f(x0)
7:            x0 = x
8:        else
            r = U[0,1]
10:        if r < exp[(f(x0) -f(x))/T]
11:            x0 = x
12:        T = \alpha(T)
```

```
Algorithm 3 Simulated Annealing in terms of VR methods
NextPopSA(x)
    x' = VariateSA(x)
    x' = ReplaceSAT (x',x)
    UpdateParameters(T)
    return x'
```

tic methods, see algorithm 3. This new algorithm is in terms of VariationReplacement methods. Observe that algorithms 2 and 3 are equivalents. Line 5 of algorithm 2 is the method VariateSA (line 1) of algorithm 3; lines 6 to 11 of algorithm 2 is the method ReplaceSA (line 2) of algorithm 3. Finally, line 12 of algorithm 2 and method UpdateParameters (line 3) perform the same task.

Now, we concentrate on characterizing (sa) as a VR stochastic method and analyzing its convergence through non-stationary Markov kernels.

Proposition 7. If $R e p l a c e_{S A}(x, x)$ is an elitist method, then it can be characterized by the Markov Kernel $K_{R S A}: \Omega^{2} \times \Sigma \longrightarrow[1,0]$ defined as

$$
K_{R S A}=\pi_{1} \circ s^{2}
$$

Proof. It is defined in the same way that the method of RHC in Gomez (2019). So the proof uses the same argument that lemma 75 of Gomez (2019).

Proposition 8. if the stochastic method VariateAST can be characterized by a non-stationary Markov kernel $V_{S A T}^{(t)}: \Omega \times \Sigma \longrightarrow[1,0]$ and condition of proposition 7 are fulfilled then method the NextPopSA(x) can be described as a VR non-stationary Markov Kernel defined as

$$
K_{S A}^{(t)}=K_{R} \circ K_{V S A T}^{(t)}
$$

Proof. $K_{S A}^{(t)}$ is a kernel composition under the given conditions.




---

Proposition 9. if ReplaceSA is an elitist method, then NextPopSA can be characterized by an elitist non-stationary Markov kernel.

Proof. This proof uses the same argument as proposition 77 in Gomez (2019).

# 4.3 Convergence 

Corollary 10. if conditions of propositions 7,8 and 9 , are fulfilled and method VariateAST is optimal strictly bounded from zero then NextPopSA is optimal strictly bounded from zero.

Proof. Follows from definition 67, lemma 68, and definition 69 in Gomez (2019) and proposition 9 that establish that NextPopSA can be characterized by an elitist kernel, and this is optimal strictly bounded from zero.

Theorem 11. sa will converge to the global optimum if ReplaceSA is elitist and if VariateAST is optimal strictly bounded from zero.

Proof. Follows from corollary 10, and propositions 7,8 and 9 .

## 5 Evolutionary Strategies (es)

### 5.1 Concept

Evolutionary Strategies $(\mu / \rho+$,入)-es are a type of Evolutionary Algorithms that apply mutation, recombination, and selection operators to a population of individuals Beyer and Schwefel (2002), see algorithm 4 . Every individual is an es that has two parts: the candidate solution $(\mathbf{x})$ and the set of endogenous strategy parameters ( $\mathbf{s}$ ) used to control the mutation operator (Beyer and Schwefel (2002)). An es randomly initializes the population, line 2 , and evolves both parts of the individual (lines 5-9) up to certain endingcondition is fulfilled (line 3). The set of endogenous parameters are exposed to evolution (lines 6 and 8 ) before producing a child candidate solution (line 7 and 9) to introduce variety. The new individual is a composition of a set of selected candidate solutions (line 5). es generates a new population of $\lambda$ new individuals each generation (line 4). Finally, es selects a final population using two possible approaches. The $(\mu+\lambda)$-es approach that selects the best $\mu$ individuals among the $\mu$ parents and $\lambda$ children or the $(\mu, \lambda)$-es that selects the best $\mu$ individuals from the $\lambda$ children (notice that $\lambda \geq \mu$ in this case). In this work, we study both of them.




---

Algorithm 4 Evolutionary strategies described by Beyer and Schwefel (2002) $\mathrm{ES}(\mu / \rho+, \lambda)$

1: $g=0$
2: $\operatorname{initialize}\left(\mathcal{P}_{q}^{(0)}:=\left\{\left(y_{m}^{(0)}, s_{m}^{(0)}, F\left(y_{m}^{(0)}\right)\right), m=1, \ldots, \mu\right\}\right)$
3: while $\neg \operatorname{TerminationCondition}()$ do
4: for $l=1$ to $\lambda$ do
5: $a_{l}=$ Marriage $\left(\mathcal{P}_{q}^{g}, \rho\right)$
6: $s_{l}=\operatorname{Recombinations}\left(a_{l}\right)$
7: $y_{l}=\operatorname{Recombinationy}\left(a_{l}\right)$
8: $s_{l}^{\prime}=\operatorname{Mutations}\left(s_{l}\right)$
9: $y_{l}^{\prime}=\operatorname{Mutations}\left(y_{l}, s_{l}^{\prime}\right)$
10: $F_{l}^{\prime}=F\left(y_{l}^{\prime}\right)$
11: $\mathcal{P}_{0}^{g}=\left\{\left(y_{l}^{\prime}, s_{l}^{\prime}, F_{l}^{\prime}\right), l=1, \ldots, \lambda\right\}$
12: if $(\mu, \lambda)$ then
$13: \quad \mathcal{P}_{q}^{g+1}=\operatorname{Selection}\left(\mathcal{P}_{0}^{g}, \mu\right)$
14: else $(\mu+\lambda)$
$15: \quad \mathcal{P}_{q}^{g+1}=\operatorname{Selection}\left(\mathcal{P}_{0}^{g}, \mathcal{P}_{q}^{g}, \mu\right)$
$16: \quad g=g+1$

# 5.2 Formalization 

To formalize and characterize $(\mu / \rho+, \lambda)$-es, we rewrite algorithm 4 in terms of individual non-stationary stochastic methods, see algorithm 5 . This follows the approach in Gomez (2019) that express the algorithms in terms of VariationReplacement methods to study their convergence properties.

Notice that algorithms 4 and 5 are equivalents: lines 4-11 in algorithm 4 is method $\operatorname{Variate}(\mathcal{P})$ (line 1) in the NextPop method of algorithm 5. Also, lines 12-15 in algorithm 4 are line 2 in the NextPop method of algorithm 5.

Using this characterization, we proceed to characterize each method of algorithm 5 through non-stationary Markov kernels.

With the object of characterizing $(\mu / \rho+, \lambda)$-ES we need to establish some non-stationary Markov kernels. First, we study the Variate method (line 1, method NextPop, algorithm 5).

Following definition 53 in Gomez (2019), we can express the variation method Variate: $\Omega_{\mu} \longrightarrow \Omega_{\lambda}$ as a joined stochastic method.

$$
\operatorname{Variate}(\mathcal{P})=\prod_{i=1}^{\lambda} \operatorname{NextSubPop}_{i}(\mathcal{P})
$$

Where NextSubPop: $\Omega_{\mu} \longrightarrow \Omega$ chooses $\rho$ individuals from the population, combines the $\rho$ individuals, generates a child and finally mutates the strategy and the child.

Proposition 12. If lines 8 and 9 of method UpdateStrategies of algorithm 5 can be characterized by non-stationary kernels $X: \mathbb{R}^{\rho} \times \mathcal{B}(\mathbb{R})^{\otimes \rho} \longrightarrow[0,1]$ and $V S(t): \mathbb{R} \times \mathcal{B}(\mathbb{R}) \longrightarrow[0,1]$ respectively. UpdateStrategies can be characterized by a non-stationary kernel $U S(t): \mathbb{R}^{\rho} \times \mathcal{B}(\mathbb{R}) \longrightarrow[0,1]$ defined as:

$$
K_{U S}^{(t)}=K_{V S}^{(t)} \circ K_{X S}
$$




---

# Algorithm 5 Evolutionary strategies algorithm - NextPop method described in terms of VR methods 


$$
\begin{aligned}
& \text { NextSubPop }_{i}(P) \\
& \text { 1: } \quad a=\operatorname{PickParents}(P) \\
& \text { 2: } \quad q=\operatorname{Xover}_{a}(P) \\
& \text { 3: } \quad \operatorname{UpdateStrategies}_{a}(s, i) \\
& \text { 4: } \quad q^{\prime}=\operatorname{Variates}(q) \\
& \text { 5: } \quad \text { return } q^{\prime}
\end{aligned}
$$


$$
\begin{aligned}
& \text { 2: } \quad s^{\prime}=\operatorname{XoverStrategie}_{a}(s) \\
& \text { 3: } \quad s_{i}=\operatorname{VariateStrategie}\left(s^{\prime}\right)
\end{aligned}
$$

```
Variate(P)
    for i=1 to $\lambda$ do
        $Q_{i}=\operatorname{NextSubPop} i(P)$
    return $Q$
NextPop $(P)$
    $Q^{\prime}=\operatorname{Variate}(P)$
    $Q=\operatorname{Replace}(P, Q^{\prime})$
}returnQ
    }
```

Proof. It is in terms of kernel composition, follows from definition 25 of Gomez (2019).

Proposition 13. If lines 2 and 4 of algorithm 5 can be characterized by nonstationary Markov kernels $\mathrm{Xover}_{a}:\left(\Omega_{\rho} \times \Sigma\right) \longrightarrow[0,1]$ and Variates : $(\Omega \times$ $\Sigma) \longrightarrow[0,1]$ respectively, then the method NextSubPop can be characterized by the kernel NextSubPop: $\left(\Omega_{\rho} \times \Sigma\right) \longrightarrow[0,1]$ defined as the non-stationary kernel:

$$
K_{\text {NextSubPop }}=K_{\text {Variates }}^{(t)} \circ K_{X O V E R} \circ \pi_{\{1, \ldots, \rho\}} \circ K_{P}
$$

Proof. It is in terms of kernel composition, follows from definition 25 of Gomez (2019).

Proposition 14. If NextSubPop can be characterized by a non-stationary Markov kernel, the stochastic method Variate $(t)$ can be characterized by a kernel $\mathcal{V}: \Omega_{\mu} \times \Sigma^{\otimes \mu} \longrightarrow[0,1]$ defined as

$$
K_{\text {Variate }}^{(t)}=\left[\prod_{i=1}^{\lambda}\left[K_{\text {NextSubPop } i}\right]\right]
$$

Proof. It is a join stochastic method, follows from definition 55 and proposition 56 of Gomez (2019).

Proposition 15. The stochastic method $\operatorname{Replace}(\lambda+\mu)$ used in line 2 of method NextPop, can be characterized by the kernel $R_{\mu, \mu+\lambda}: \Omega_{\mu+\lambda} \times \Sigma^{\otimes \mu} \longrightarrow$ $[0,1]$ defined as $K_{R_{\mu, \mu+\lambda}}=\pi_{\{1, \ldots, \mu\}} \circ s_{\mu+\lambda, \mu+\lambda-1}$ and the stochastic method




---

Replace $(\mu, \lambda)$, can be characterized by the kernel $R_{\mu, \lambda}: \Omega_{\lambda} \times \Sigma^{\otimes \mu} \longrightarrow[0,1$ defined as $K_{R_{\mu, \lambda}}=\pi_{1, \ldots, \mu} \circ s_{\lambda, \lambda-\lambda}$

Proof. $K_{R_{\mu, \lambda}}$ and $K_{R_{\mu+\lambda}}$ are kernels composition. Follows from definition 25 in Gomez (2019).

Corollary 16. If methods PickParents, XOvera, XoverStrategiea, VariateStrategie and, Variates can be described by Markov kernels fulfilling the conditions of 12 and 13, evolutionary Strategies can be described by a VR kernel.

$$
K_{E S}=K_{R} \circ K_{V}
$$

where:

$$
\begin{aligned}
& K_{V}=K_{V a r i a t e} \\
& K_{R}=K_{R_{\mu, \lambda}} \text { or } K_{R}=K_{R_{\mu+\lambda}}
\end{aligned}
$$

Proof. Follows from propositions 12, 13, 14 and 15.

# 5.3 Convergence 

Proposition 17. The $\operatorname{NextPop}(\mu / \rho+\lambda)-E S$ is an elitist stochastic method that can be characterized by an elitist stochastic kernel

Proof. Let $k \in[1, \mu]$ be the index of the best individual in population $P$, then $f(\operatorname{BEST}(P))=f\left(P_{k}\right)$. Since $P \subseteq\{\mathrm{P} \cup \operatorname{Variate}(\mathrm{P})\}$ and the method Replace is elitist. It is clear that $f(\operatorname{BEST}(P \cup \operatorname{Variate}(P))) \triangleleft-f\left(P_{k}\right)$.

Corollary 18. If conditions of proposition 12 and 13 are satisfied and Variates is optimal strictly bounded from zero then the method NextPop $\mu+\lambda$ is optimal strictly from zero.

Proof. Follows from definition 67, lemma 68, and definition 69 of Gomez (2019) and proposition 17 that establish that an elitist kernel is optimal strictly bounded from zero.

Theorem 19. $(\mu / \rho+\lambda)-E S$ will converge to the global optimum if methods PickParents and Variate(s) can be characterized by stationary or nonstationary Markov kernels and Variates is optimal strictly bounded from zero.

Proof. Follows from theorem 3 and corollary 18.




---

# 6 Conclusion 

In this paper we have generalized the conditions of convergence to the global optimum from stationary to non-stationary Markov process that are present in the work of stochastic global optimization algorithms: a systematic approach proposed by Gomez (2019). We formalize some selection schemes to generalize the theory to cover as many variations of each algorithm as possible. Also, we formalized and characterized both simulated-annealing and evolutionarystategies using the developed theory. There, we established which conditions must be fulfilled to achieve a global convergence in both algorithms. Our future work will concentrate on using the proposed approach to formalize as many stationary and non-stationary SGoal as possible, and extending and developing the theory for several particular methods that can be considered SGoals.

## References

Beyer HG, Schwefel HP (2002) Evolution strategies - a comprehensive introduction. Natural Computing 1:3-52, DOI 10.1023/A:1015059928466
Blickle T, Thiele L (1996) A comparison of selection schemes used in evolutionary algorithms. Evolutionary Computation 4(4):361-394, DOI 10.1162/ evco.1996.4.4.361, URL https://doi.org/10.1162/evco.1996.4.4.361, https://doi.org/10.1162/evco.1996.4.4.361

Bowerman BL (1974) Nonstationary markov decision processes and related topics in nonstationary markov chains. PhD thesis, University of Iowa, URL https://lib.dr.iastate.edu/rtd/6327

Das S, Suganthan PN (2011) Differential evolution: A survey of the state-ofthe-art. IEEE Transactions on Evolutionary Computation 15(1):4-31, DOI 10.1109/TEVC.2010.2059031

De Jong K (1975) An analysis of the Behavior of a class of genetic adaptive systems. PhD thesis, University of Michigan

Eiben AE, Hinterding R, Michalewicz Z (1999) Parameter control in evolutionary algorithms. IEEE Transactions in Evolutionary Computation 3(2):124141

Fristedt BE, Gray LF (1997) A Modern Approach to Probability Theory. Springer Science \& Business Media

Goldberg DE, Deb K (1991) A comparative analysis of selection schemes used in genetic algorithms. In: Foundations of Genetic Algorithms, Morgan Kaufmann, pp 69-93

Gomez J (2019) Stochastic global optimization algorithms: A systematic formal approach. Information Sciences 472:53 - 76, DOI https://doi.org/10.1016/j.ins.2018.09.021, URL http://www.sciencedirect.com/science/article/pii/S0020025517305248

Holland JH (1975) Adaptation in Natural and Artificial Systems. The University of Michigan Press




---

Kirkpatrick S, Gelatt CD, Vecchi MP (1983) Optimization by simulated annealing. Science 220(4598):671-680, DOI 10.1126/science.220.4598. 671, URL https://science.sciencemag.org/content/220/4598/671, https://science.sciencemag.org/content/220/4598/671.full.pdf
Miller BL, Miller BL, Goldberg DE, Goldberg DE (1995) Genetic algorithms, tournament selection, and the effects of noise. Complex Systems 9:193-212
Mitchell M (1996) An introduction to genetic algorithms. MIT Press
Rudolph G (1996) Convergence of evolutionary algorithms in general search spaces. In: In Proceedings of the Third IEEE Conference on Evolutionary Computation, IEEE Press, Piscataway (NJ, pp 50-54
Russell S, Norvig P (2009) Artificial Intelligence: A Modern Approach, 3rd edn. Prentice Hall Press, Upper Saddle River, NJ, USA
Simon D (2013) Evolutionary Optimization algorithms. Wiley
Storn R, Price K (1997) Differential evolution - a simple and efficient heuristic for global optimization over continuous spaces. J of Global Optimization 11(4):341-359, DOI 10.1023/A:1008202821328, URL https://doi.org/10.1023/A:1008202821328




---

