# Generalized measure Black-Scholes equation: Towards option self-similar pricing 

Nizar Riane:, Claire David;

April 9, 2024

- Université Mohammed V de Rabat, FSJESR-Agdal, Maroc ${ }^{1}$
; Sorbonne Université
CNRS, UMR 7598, Laboratoire Jacques-Louis Lions, 4, place Jussieu 75005, Paris, France ${ }^{2}$


#### Abstract

In this work, we give a generalized formulation of the Black-Scholes model. The novelty resides in considering the Black-Scholes model to be valid on 'average', but such that the pointwise option price dynamics depends on a measure representing the investors' 'uncertainty'. We make use of the theory of non-symmetric Dirichlet forms and the abstract theory of partial differential equations to establish well posedness of the problem. A detailed numerical analysis is given in the case of self-similar measures.


Keywords: Generalized measure Black-Scholes equation; self-similar measure; non-symmetric Dirichlet form; fractal differential equations; finite difference method.
AMS Classification: $28 \mathrm{~A} 80-91 \mathrm{G} 20-65 \mathrm{~L} 12-65 \mathrm{~L} 20$.

## 1 Introduction

The Black-Scholes model arises as one of the most important application of mathematics to economics and finance of the 20th century, allowing the emergence of the theory of financial partial differential equations and the associated numerical analysis.

Yet, despite its phenomenal success in the financial market, the model suffers from deficiencies, for instance, when it comes to the modeling of real market options with erratic behaviors [For96]. One can argue that the model does not capture all the factors influencing investor decisions.

From a practical point of view, investors employ technical analysis to detect patterns in price evolution graphs to beat the market; since those patterns seem to appear in small and large scales, this could justify a self-similar modelling of the market. Investigation of fractals in finance is not new, we can refer, for instance, to Benoît Mandelbrot's work in [Man97], the aspects of which are not taken

[^0]
[^0]:    ${ }^{1}$ nizar.riane@gmail.com
    ${ }^{2}$ Corresponding author: Claire.David@Sorbonne-Universite.fr



into account by the classical model.
In this paper, we give a definition of a general version of the Black-Scholes model, based on the theory of non-symmetric Dirichlet forms, and on the abstract theory of partial differential equations. The key point is to consider the Black-Scholes equation describing an average evolution, while the exact dynamics depends on uncertainty captured by a mathematical measure. The analysis goes so far as proving the existence of a Generalized Black-Scholes operator.
Special treatment is given to the self-similar case by writing an explicit formula, which enables computation of the solution. The CFL ${ }^{3}$ convergence condition for the associated finite difference scheme is determined and written explicitly. For the proper calibration, our model can avoid overpricing options at the money, and underpricing options at the ends, either deep in the money ${ }^{4}$, or deep out of the money ${ }^{5}$. This work opens the way to an empirical investigation and an inverse problem of the probability measure $\mu$.

# 2 Generalized Measure Black-Scholes Model 

## Definition 2.1 (Generalized Measure Black-Scholes Equation)

Let's introduce the generalized measure Black-Scholes equation, for European options, in the sense of distributions:

$$
\begin{cases}\frac{B u}{B t}(\underline{t, x}) d \mu & =\int\left(-r(t) \times \frac{B u}{B x}(\underline{t, x})-\frac{\sigma^{2}(t)}{2} \times \frac{x^{2}}{\Delta(\underline{u})} \Delta(\underline{u})+{\underline{r}(t)}^{(t, x)}\right) d x \\ & \forall(\underline{t, x}) \in[0, T] \times] L, M[ \\ u(T, x) & =h(x) \quad \forall x \in] L, M[,\end{cases}
$$

where the variable $0<L<x<M$ is the price of the underlying financial instrument, $\sigma$ denotes the volatility, $r$ the risk-free interest rate, $T$ the maturity of the option, $\mu$ a non atomic finite measure with total mass $M=M-L$ and $u$ represents the option price. The real valued function $h$ takes the values $h(x)=(x-K)^{+}$for a call ${ }^{6}$, and $h(x)=(K-x)^{+}$for a put ${ }^{7}$, given a constant $K$ : "the strike".

In order to prove that the problem has a solution, technical results associated to the classical Black-Scholes model are required. We refer to [AP05] for the proof of the following assertions.

[^0]
[^0]:    ${ }^{3}$ Courant-Friedrichs-Lewy.
    ${ }^{4}$ When the option has what is also called an intrinsic value, i.e. the real value of the option, that is to say the profit that could be made in the event of immediate exercise. It means that the value is at a favorable strike price relative to the prevailing market price of the underlying asset. Yet, this does not mean that the trader will be making profit, since the expense of buying, and the commission prices have also to be considered.
    ${ }^{5}$ When the option has what is also called an extrinsic value, i.e. a value at a strike price higher than the market price of the underlying asset. In such a case, the Delta, i.e. the Greek which quantifies the risk, is less than 50.
    ${ }^{6}$ The call is an option on a financial instrument, which consists in a right to buy. Concretely, it consists in a contract which allows the subscriber to get the targeted financial product, at a price fixed in advance - the strike price - at a given date - the expiry one, or maturity of the call.
    ${ }^{7}$ As for the put, it is this time a right to sell - or not - at the maturity date.



# 2.1 The Black-Scholes Model 

Notation (Space of Test Functions). Given a continuous subset $E$ of $\mathbb{R}$, we will denote by $\mathcal{D}(E)$ the space of test functions on $E$, i.e. the space of smooth functions with compact support in $E$.

Notation (Black-Scholes Bilinear Form). For any pair $(u, v) \in \mathcal{D}\left(\mathbb{R}^{+}\right) \times \mathcal{D}\left(\mathbb{R}^{+}\right)$, set:

$$
B(u, v)=\int_{\mathbb{R}^{+}} \frac{\sigma^{2} x^{2}}{2} \frac{\partial u}{\partial x} \frac{\partial v}{\partial x} d x+\int_{\mathbb{R}^{+}}\left(\sigma^{2}-r\right) x \frac{\partial u}{\partial x} v d x+\int_{\mathbb{R}^{+}} r u v d x
$$

and note $B(u, u)=B(u)$.
Property 2.1. The bilinear form $B(\cdot, \cdot)$ is non-symmetric.
Define its symmetric part, for any pair $(u, v) \in \mathcal{D}\left(\mathbb{R}^{+}\right) \times \mathcal{D}\left(\mathbb{R}^{+}\right)$, through:

$$
\begin{aligned}
\widetilde{B}(u, v) & =\frac{1}{2}(B(u, v)+B(v, u)) \\
& =\int_{\mathbb{R}^{+}} \frac{\sigma^{2} x^{2}}{2} \frac{\partial u}{\partial x} \frac{\partial v}{\partial x} d x+\frac{1}{2} \int_{\mathbb{R}^{+}}\left(\sigma^{2}-r\right) x\left(\frac{\partial u}{\partial x} v+u \frac{\partial v}{\partial x}\right) d x+\int_{\mathbb{R}^{+}} r u v d x \\
& =\frac{\sigma^{2}}{2} \int_{\mathbb{R}^{+}} x^{2} \frac{\partial u}{\partial x} \frac{\partial v}{\partial x} d x+\frac{3 r-\sigma^{2}}{2} \int_{\mathbb{R}^{+}} u v d x
\end{aligned}
$$

## Notations. Set

$$
\begin{aligned}
& V=\left\{v \in L^{2}\left(\mathbb{R}^{+}\right), \quad x \frac{\partial v}{\partial x} \in L^{2}\left(\mathbb{R}^{+}\right)\right\} \\
& W=\left\{v \in L^{2}\left(\mathbb{R}^{+}\right), \quad x^{2} \frac{\partial^{2} v}{\partial x^{2}} \in L^{2}\left(\mathbb{R}^{+}\right)\right\}
\end{aligned}
$$



Property 2.2. The space

$$
V=\left\{v \in L^{2}\left(\mathbb{R}^{+}\right), \frac{\delta v}{\delta x} \in L^{2}\left(\mathbb{R}^{+}\right)\right\}
$$

endowed with the inner product

$$
(u, v) \mapsto\langle u, v\rangle_{V}=\langle u, v\rangle_{L^{2}\left(\mathbb{R}^{+}\right)}+\left\langle\frac{\delta u}{\delta x}, \frac{\delta v}{\delta x}\right\rangle_{L^{2}\left(\mathbb{R}^{+}\right)}
$$

is a Hilbert space.
Definition 2.2 (Black-Scholes Weak Formula).
The Black-Scholes variational formula reads: find $u \in C\left([0, T] ; L^{2}\left(\mathbb{R}^{+}\right)\right) \cap L^{2}((0, T) ; V)$ such that $\partial_{t} u \in L^{2}\left((0, T) ; V^{\prime}\right)$, satisfying:

$$
\begin{cases}\frac{B(u, v)}{d t}=\int_{\mathbb{R}^{+}} u(t, x) v(x) d x & \forall v \in \mathcal{D}\left(\mathbb{R}^{+}\right) \\ u(T, x)=h(x) & \end{cases}
$$

where $V^{\prime}$ is the dual space of $V$.
Lemma 2.3 (Black-Scholes Operator).
There exists a unique bounded linear operator $\mathcal{B S}: V \rightarrow V^{\prime}$, which will be called Black-Scholes operator, such that:

$$
\forall(u, v) \in V^{2}: \quad B(u, v)=\langle\mathcal{B S}(u), v\rangle_{L^{2}\left(\mathbb{R}^{+}\right)}
$$

Definition 2.3.
Recall that the first derivative is always bounded in the Hilbert-Sobolev space $H^{1}\left(\mathbb{R}^{+}\right)$, and that the second derivative is always bounded in the Hilbert-Sobolev space $H^{2}\left(\mathbb{R}^{+}\right)$.

The Black-Scholes operator is given, for any $v$ in $W$, by

$$
\mathcal{B S}(v)=-\frac{x^{2} \sigma^{2}}{2} \frac{\delta^{2} v}{\delta x^{2}}-r\left(\frac{\delta v}{\delta x}+r v\right.
$$

Lemma 2.4.
The set

$$
W=\left\{v \in V, \frac{x^{2} \delta^{2} v}{\delta x^{2}} \in L^{2}\left(\mathbb{R}^{+}\right)\right\}
$$

is dense in $V$.



Lemma 2.5 (Black-Scholes Weak Solution). For $h$ in $L^{2}\left(\mathbb{R}^{+}\right)$, the Black-Scholes problem has a unique weak solution.

# 2.2 An Interpretation of the Generalized Measure Black-Scholes Model 

The generalized measure Black-Scholes equation, for a probability measure $\mu$, can be written, by choosing $v=u$, as

$$
\frac{\partial}{\partial t} \mathbb{E}\left(|u|^{2}\right)=2 \mathcal{M} \mathscr{B}(u)
$$

where $\mathcal{M}=\mathcal{M}-\mathcal{L}$, while $\mathbb{E}(.)$ is the expected value and $\mathscr{B}(\cdot, \cdot)$ denotes the involved Black-Scholes bilinear form. This equation can be understood in the following way: the expected value depreciation of $u^{2}$ (and, hence, of $u$, since it is positive) is proportional to the Black-Scholes energy $\mathscr{B}(u)$. This implies a law given by the classical Black-Scholes theory which holds on average and another induced by investors' perception of reality and reflected by $\mu$.

A direct implication of this vision is a local dependence of the option price dynamics on the probability measure $\mu$, which can be interpreted as "gzn confidencezuncertainty measure".

## 3 Non-Symmetric Dirichlet Forms and Generalized Measure BlackScholes Operators

Given two strictly positive numbers $L<M$, if one replaces $\mathbb{R}^{+}$with $M=[L, M]$ (where $M=$ $s L, M]$ ) in the generalized measure Black-Scholes model, it does not result in a dramatic effect on the mathematical or economical foundations of the model from the following two points of view:

1. Financial stability: One can suppose, in short run, boundedness of the underlying financial instrument price.
2. Numerical analysis: It is well known that infinite boundaries are replaced with finite ones for numerical simulations (See [KN01] for error estimates).
In section 5.3, a tolerance level associated with the choice of the bounds $L$ and $M$ is calculated.

Notations.
Let's introduce the following two spaces:

$$
\begin{aligned}
& V_{M}=\left\{v \in L^{2}(M), \quad \frac{\partial v}{\partial x} \in L^{2}(M)\right\} \\
& L_{\mu}^{2}(M)=\left\{v, \quad \int_{L}^{M} v^{2} d \mu<\infty\right\}
\end{aligned}
$$

The dual space of $V_{M}$ will be denoted by $V_{M}^{‘}$ and the closure of $\mathscr{D}(M)$ in $V_{M}$ by $V_{0, M}$.



Proposition 3.1. The space $\mathcal{D}(M)$ is dense in $L_{\mu}^{2}(M)$.
As in [HLN06], the fundamental conditions under which the solution exist are obtained thanks to the following assumptions:

# Assumptions 3.2. 

For any $u$ in $\mathcal{D}(M)$, there exists a positive constant $C_{0}$ :

$$
\begin{gathered}
\|u\|_{L_{\mu}^{2}(M)} \leqslant C_{0}\left\|\frac{\partial u}{\partial x}\right\|_{L^{2}(M)} \\
\sigma^{2}<4 r \cdot
\end{gathered}
$$

(Continuous injection condition)
(Coercivity condition)

Proposition 3.3. Under the first condition in assumption 3.2, there exists a unique $L_{\mu}^{2}(M)$-representative $\tilde{u}$ of each equivalence class of functions $u$ in $V_{M}$ such that the above condition holds. There also exists a $\mathcal{D}(M)$ sequence $\left(u_{n}\right)_{n \in \mathbb{N}}$ which converges towards $\tilde{u}$ both in $V_{M}$ and in $L_{\mu}^{2}(M)$, since $\mathcal{D}(M)$ is dense in $V_{M}$ and $L_{\mu}^{2}(M)$ [Kil94].

Consider the bilinear form $\mathfrak{B}(\cdot, \cdot)$ with domain $\operatorname{dom}(\mathfrak{B})$ on the Hilbert space $V_{M}$. We introduce the bilinear form:

$$
\mathfrak{B}^{\star}(\cdot, \cdot)=\mathfrak{B}(\cdot, \cdot)+\langle\cdot, \cdot\rangle_{L_{\mu}^{2}(M)}
$$

and the symmetric one:

$$
\tilde{\mathfrak{B}}^{\star}(\cdot, \cdot)=\mathfrak{\mathfrak { B }}(\cdot, \cdot)+\langle\cdot, \cdot\rangle_{L_{\mu}^{2}(M)}
$$

We refer to [MR92] for further details on the theory of non-symmetric Dirichlet forms.

Definition 3.1 (Symmetric Closed Form).
A pair $(\mathfrak{B}$, dom $(\mathfrak{B})$ ) is a symmetric closed form (on $\mathcal{H}$ ) if $\operatorname{dom}(\mathfrak{B})$ is a dense linear subspace of $\mathcal{H}$ and $\mathfrak{B}: \operatorname{dom}(\mathfrak{B}) \times \operatorname{dom}(\mathfrak{B}) \rightarrow \mathbb{R}$ is a positive definite bilinear which is symmetric and closed on $\mathcal{H}$ (i.e., $\operatorname{dom}(\mathfrak{B})$ is complete with respect to the norm $\left.\mathfrak{B}^{\star}(\cdot, \cdot)^{\frac{1}{2}}\right)$.

Definition 3.2 (Sector Condition).
Let us denote by $\mathfrak{B}$ a bilinear form on the Hilbert space $\mathcal{H}$, and by dom $(\mathfrak{B})$ its domain. The pair $(\mathfrak{B}, \operatorname{dom}(\mathfrak{B}))$ is said to satisfy:



i. The weak sector condition if there exists $K>0$ such that:

$$
\forall(u, v) \in \operatorname{dom}(B) \times \operatorname{dom}(B): \quad\left|B^{\star}(u, v)\right| \leqslant K \sqrt{B^{\star}(u, u) B^{\star}(v, v)}
$$

ii. The strong sector condition if there exists $K>0$ such that

$$
\forall(u, v) \in \operatorname{dom}(B) \times \operatorname{dom}(B):|B(u, v)| \leqslant K \sqrt{B(u, u) B(v, v)}
$$

Remark 3.1.
A coercive continuous bilinear form satisfies both conditions.

# Definition 3.3 (Coercive Closed Form). 

A pair $(B$, dom $(B)$ ) will be called a coercive closed form (on $H$ ) if $\operatorname{dom}(B)$ is a dense linear subspace of $H$ and $B: \operatorname{dom}(B) \times \operatorname{dom}(B) \rightarrow \mathbb{R}$ is a bilinear form such that the following two conditions hold:
i. Its symmetric part $(\tilde{B}, \operatorname{dom}(B))$ is a symmetric closed form on $H$.
ii. $(B, \operatorname{dom}(B))$ satisfies the weak sector condition inequality $i$. given in (3).

Definition 3.4 (Symmetric Vs Non-Symmetric Dirichlet Form). A coercive closed form $(B$, dom $(B))$ on $L_{\mu}^{2}(M)$, for a given measure $\mu$, will be called a Dirichlet form if, for any $u$ in $\operatorname{dom}(B)$, one has:

$$
\tilde{u} \in \operatorname{dom}(B) \quad \text { and } \quad \begin{cases}B(u+\tilde{u}, u-\tilde{u}) \geqslant 0 & \\ B(u-\tilde{u}, u+\tilde{u}) \geqslant 0 & \end{cases}
$$

where $\tilde{u}=\max (0, \min (u, 1))$. If $(B, \operatorname{dom}(B))$ is in addition symmetric, this is equivalent to:

$$
B(\tilde{u}, \tilde{u}) \leqslant B(u, u)
$$

$B$ will be called a symmetric Dirichlet form.

Theorem 3.4. [MR92]
Let us denote by $(B, \operatorname{dom}(B))$ a coercive closed form on $H$, and $J$ a continuous linear functional on $\operatorname{dom}(B)$. Then, there exists a unique $u \in \operatorname{dom}(B)$ such that

$$
\forall v \in \operatorname{dom}(B): \quad B^{\star}(u, v)=J(v)
$$



Definition 3.5 (Non-Symmetric Dirichlet Forms).
A coercive closed form on $H,(\mathcal{B}, \operatorname{dom}(\mathcal{B}))$, is said to be a non-symmetric Dirichlet form (on H), if there exists a one-to-one correspondence with a pair of bounded linear operators $(L, \tilde{L})$ :

$$
\forall(u, v) \in \operatorname{dom}(L) \times \operatorname{dom}(L): \quad \mathcal{B}(u, v)=(-L u, v)=(u,-\tilde{L} v)
$$

where $\operatorname{dom}(L)$ is the domain of $L$. Also, $\operatorname{dom}(L)$ is a dense subset of $\operatorname{dom}(\mathcal{B})$.
The operator L (respectively $\tilde{L}$ ) is the generator of a strongly continuous contraction semi-group $\left(T_{t}\right)_{t>0}$ (respectively $\left(\tilde{T}_{t}\right)_{t>0}$ ).

The following result follows from [AP05].

# Proposition 3.5 (Poincaré Inequality ). 

The space $\mathcal{D}(M)$ is dense in $V_{M}$, and, for any $v \in \mathcal{D}(M)$, the following inequality is satisfied:

$$
\|v\|_{L^{2}(M)} \leqslant 2\left\|\frac{\mathrm{d} v}{\mathrm{~d} x}\right\|_{L^{2}(M)}
$$

This inequality induces a second norm on $V_{M}$, given, for any $v$ in $V_{M}$, by:

$$
|v|_{V_{M}}=\left\|\frac{\mathrm{d} v}{\mathrm{~d} x}\right\|_{L^{2}(M)}
$$

Proposition 3.6. (Continuity and Gårding Inequality)
The bilinear form $\mathcal{B}(\cdot, \cdot)$ is continuous on $V_{M}$, and satisfies the Gårding inequality:

$$
\forall u \in V_{M}: \quad \mathcal{B}(u) \geqslant \frac{\sigma^{2}}{2}|u|_{V_{M}}^{2}-\lambda\|u\|_{L^{2}(M)}^{2}
$$

where $\lambda=\frac{\left(\sigma^{2}-3 r\right)^{2}}{2}$. Moreover, $\mathcal{B}(\cdot, \cdot)$ is coercive under the second assumption 3.2 .
$\overline{\text { Proof. }}$ For any pair $(u, v) \in \mathcal{D}(M) \times \mathcal{D}(M)$, by using the Poincaré inequality, we obtain that

$$
\begin{aligned}
|\mathcal{B}(u, v)| & =\left|\int_{M}\left(\frac{\sigma^{2} x^{2}}{2} \frac{\partial u}{\partial x} \frac{\partial v}{\partial x} d x+\int_{M}\left(\sigma^{2}-r\right) x \frac{\partial u}{\partial x} v d x+\int_{M} r u v d x\right|\right| \\
& \leqslant \frac{\sigma^{2}}{2}|u|_{V_{M}}|v|_{V_{M}}+\left(\sigma^{2}-r\right)|u|_{V_{M}}\|v\|_{L^{2}(M)}+r\|u\|_{L^{2}(M)}\|v\|_{L^{2}(M)} \\
& \leqslant C_{1}|u|_{V_{M}}|v|_{V_{M}}
\end{aligned}
$$

where $C_{1}=2 r+\frac{5 \sigma^{2}}{2}$. For the coercivity, we use again Poincaré inequality:



$$
\begin{aligned}
\mathcal{B}(u) & =\frac{\sigma^{2}}{2}|u|_{\mathcal{V}_{M}}^{2}+\int_{L}^{M}\left(\sigma^{2}-r\right) x \frac{\partial u}{\partial x} u d x+r\|u\|_{L^{2}(M)}^{2} \\
& =\frac{\sigma^{2}}{2}|u|_{\mathcal{V}_{M}}^{2}-\frac{\left(\sigma^{2}-3 r\right)}{2}\|u\|_{L^{2}(M)}^{2} \geqslant C_{2}|u|_{\mathcal{V}_{M}}^{2}
\end{aligned}
$$

where $C_{2}=6 r-\frac{3 \sigma^{2}}{2}$.

Definition 3.6. We introduce the mapping $\iota: \mathcal{V}_{M} \rightarrow L_{\mu}^{2}(M)$ by

$$
\iota(u)=\bar{u}
$$

where $\bar{u}$ is the unique $L_{\mu}^{2}(M)$-representative of $u$, along with the closed set:

$$
\mathcal{N}=\left\{v \in \mathcal{V}_{M}:\|v\|_{L_{\mu}^{2}(M)}=0\right\}
$$

# Theorem 3.7. The Black-Scholes Non-Symmetric Dirichlet Form 

Under the assumption 3.2:
i. $\operatorname{dom}(\mathcal{B})=\mathcal{V}_{M}$ is dense in $L_{\mu}^{2}(M)$.
ii. $\left(\tilde{\mathcal{B}}^{\star}, \mathcal{V}_{M}\right)$ is a Hilbert space.
iiii. $(\mathcal{B}, \operatorname{dom}(\mathcal{B}))$ is a (non-symmetric) Dirichlet form.

Proof. - Let us consider a sequence $\left(u_{n}\right)_{n \in \mathbb{N}}$ of $\mathscr{D}(M)$, which converges towards $u$ in $L_{\mu}^{2}(M)$. We then consider two sequences, $\left(a_{n}\right)_{n \in \mathbb{N}} \in \mathbb{N}^{\mathbb{N}}$, and $\left(b_{n}\right)_{n \in \mathbb{N}} \in \mathcal{V}_{M}{ }^{\mathbb{N}}$ such that, for any natural integer $n$,

$$
u_{n}=a_{n}+b_{n} \cdot
$$

Then, the sequence $\left(b_{n}\right)_{n \in \mathbb{N}}$ converges to $u$ in $L_{\mu}^{2}(M)$.

- Under the continuous injection condition (1) in assumption 3.2, the induced norm $\tilde{\mathcal{B}}^{\star}(\cdot, \cdot)^{\frac{1}{2}}$ is equivalent to the norm $|\cdot|_{\mathcal{V}_{M}}$. Hence, $\left(\mathcal{B}^{\star}, \operatorname{dom}(\mathcal{B})\right)$ is complete.



- It follows from the coercivity of $B$ that:

$$
0 \leqslant C_{2}\left|u_{2}-\tilde{u}_{2}\right|_{V_{M}}^{2} \leqslant B\left(u-\tilde{u}, u-\tilde{u}\right)
$$

Theorem 3.8 (Generalized Measure Black-Scholes Operator). Under the assumption 3.2, there exists a bounded linear operators $\mathcal{B} s_{\mu}$, that we will call generalized measure Black-Scholes operator, such that, for any pair $(u, v) \in \operatorname{dom}\left(\mathcal{B s}_{\mu}\right) \times \operatorname{dom}(\mathcal{B})$ :

$$
\mathcal{B}(u, v)=\left\langle\mathcal{B} s_{\mu}(u), v\right\rangle_{L_{\mu}^{2}(M)}
$$

Moreover, we will say that $u \in \operatorname{dom}\left(\mathcal{B}_{\mu}\right)$ and $\mathcal{B s}_{\mu}(u)=f$ if and only if

$$
\mathcal{B}(u, v)=\int_{M} f v d \mu \quad, \quad \forall v \in \mathcal{V}_{0, M}
$$

# Remark 3.2. 

The generalized measure Black-Scholes operator is bounded from $V_{M}$ to $V_{M}^{*}$ since, $\forall v \in \mathcal{V}_{0, M}$

$$
\left|\left\langle\mathcal{B} s_{\mu}(u), v\right\rangle_{L_{\mu}^{2}(M)}\right|=|\mathcal{B}(u, v)| \leqslant C_{1}|u|_{V_{M}}|v|_{V_{M}}
$$

by continuity of $\mathcal{B}(\cdot, \cdot)$
Notations (Sobolev Spaces).
Given a continuous subset $E$ of $\mathbb{R}, k \in \mathbb{N}$, and $p \geqslant 1$, we recall that the classical Sobolev spaces on $E$ are

$$
W_{p}^{k}(E)=\left\{f \in L_{p}(E), \forall j \leqslant k: f^{(j)} \in L_{p}(E)\right\}
$$

and

$$
H^{k}(E)=W_{2}^{k}(E)=\left\{f \in L_{2}(E), \forall j \leqslant k: f^{(j)} \in L_{2}(E)\right\}
$$

The subspace $H_{0}^{k}$ of functions which vanish on the boundary $\partial E$ is

$$
H_{0}^{k}(E)=\left\{f \in L_{2}(E),\left.f\right|_{\partial E}=0 \text { and } \forall j \leqslant k: f^{(j)} \in L_{2}(E)\right\}
$$

It directly comes form the abstract theory of partial differential equations [Zei90], [Wlo87], [LM68] that:



Theorem 3.9 (Generalized Measure Black-Scholes Weak Solution).
Let us define the Gelfand triple (or equipped Hilbert space) $V_{M} \subset L_{\mu}^{2}(M) \subset V_{M}^{\star}$. For $h$ in $L_{\mu}^{2}(M)$, the generalized measure Black-Scholes problem admits, under the assumptions 3.2, a unique weak solution. Moreover, for $k \geqslant 1$, the solution map:

$$
\begin{aligned}
L_{\mu}^{2}(M) & \longrightarrow W_{2}^{k}([0, T] ; V_{M}) \\
h(x) & \longrightarrow u(t, x), \quad x \in M \quad \text { and } \quad t \in[0, T]
\end{aligned}
$$

is continuous.

# 4 The Self-Similar Black-Scholes Operator - a Pointwise Formula 

Definition 4.1 (Self-Similar Measure on a Real Interval, Associated to a Set of Contraction [Str06]).

We hereafter consider the particular case where the real interval $M=[L, M] \subset \mathbb{R}^{+}$is self-similar with respect to the family of contractions $\left\{f_{1}, f_{2}\right\}$, and where $f_{1}$ and $f_{2}$ are defined, for any real number $x$, by:

$$
f_{1}(x)=\frac{1}{2}(x+L), \quad f_{2}(x)=\frac{1}{2}(x+M)
$$

A measure $\mu$ with full support on $M$ will be called self-similar measure on $M$, relative to the set of contractions $\left(f_{1}, f_{2}\right)$ if, given a family of strictly positive weights $\left(\mu_{1}, \mu_{2}\right)$ such that

$$
\mu_{1}+\mu_{2}=1
$$

one has, then,

$$
\mu=\mu_{1} \mu \circ f_{1}^{-1}+\mu_{2} \mu \circ f_{2}^{-1}
$$

Let us consider $u \in \operatorname{dom}\left(B S_{\mu}\right)$ where $\mu$ is a self-similar measure according to definition 4.1. $B S_{\mu}$ is now called the self-similar Black-Scholes operator and we set: $B S_{\mu}(u)=f$.

In order to compute the explicit formula of $B S_{\mu}$, we set $M=M-L$ and we recall the self similar construction of $M$ :

$$
M=f_{1}(M)+f_{2}(M)
$$

## Definition 4.2 (Prefractal Graph Approximation).

We denote by $V_{0}$ the ordered set of the (boundary) points:

$$
\{L, M\}
$$



We build the graph $M_{0}$ by connecting the two extremities of $V_{0}$.
For any strictly positive integer $m$, we set:

$$
V_{m}=f_{1}\left(V_{m-1}\right)+f_{2}\left(V_{m-1}\right)
$$

The set of points $V_{m}$, where consecutive points are connected, will be denoted by $M_{m}$.
The set $V_{m}$ is called the set of vertices of the graph $M_{m}$. By extension, we will write that

$$
M_{m}=f_{1}\left(M_{m-1}\right)+f_{2}\left(M_{m-1}\right)
$$

One can prove that the sequence $\left(V_{m}\right)_{m \in \mathbb{N}}$ is increasing and its limit is dense in $M([\operatorname{Kig} 01])$.

Proposition 4.1. Given a natural integer m, we will denote by $\mathrm{N}_{m}$ the number of vertices of the graph $\mathrm{M}_{\mathrm{m}}$. One has:

$$
N_{0}=2
$$

and, for any strictly positive integer $m$ :

$$
N_{m}=2 m+1
$$

We recall the following definitions:

# Definition 4.3 (Word). 

Given a strictly positive integer $m$, we will call number-letter any integer $W_{i}$ of $\{1,2\}$, and word of length $|W|=m$, on the graph $M_{m}$, any set of number-letters of the form:

$$
W=\left(W_{1}, \ldots, W_{m}\right)
$$

We will write:

$$
f_{W}=f_{W_{1}} \circ \ldots \circ f_{W_{m}}
$$

## Definition 4.4 (Addresses).

Given a natural integer $m$, and a vertex $X$ of $M_{m}$, we will call address of the vertex $X$ an expression of the form

$$
X=f_{W}(L) \quad \text { or } \quad X=f_{W_{1}}(M)
$$

where $W$ and $W 1$ denote words of length $m$. The vertex $X$ has thus a double address.



Property 4.2 (Space of Harmonic Splines). Given a strictly positive integer $m$, we introduce the space of harmonic splines of order $m$, denoted by $\mathcal{H}_{m}([L, M])$, as the space of functions $\psi_{X}^{m}, X \in[L, M]$, such that:

$$
\forall Y \in M_{m} \quad \psi_{X}^{m}(Y)=\delta_{X Y}
$$

For $k \in\{1, \ldots, 2 m-1\}$, and $Y \in[L, M]$ :

$$
\psi_{L+\frac{k M}{2 m}}^{m}(Y)=\left\{\begin{array}{lr}
\frac{2 m}{M}(Y-L)-(k-1) \frac{L+(k-1) M}{2 m} & \text { if } Y \leqslant L+\frac{k M}{2 m} \\
-\frac{2 m}{M}(Y-L)+(k+1) \frac{L+k M}{2 m} & \text { if } Y \geqslant L+\frac{k M}{2 m} \\
0 & \text { otherwise }
\end{array}\right.
$$

and

$$
\psi_{L}^{m}(Y)=\left\{\begin{array}{lr}
-\frac{2 m}{M}(Y-L)+1 & \text { if } L \leqslant Y \leqslant L+\frac{M}{2 m} \\
0 & \text { otherwise }
\end{array}, \quad \psi_{M}^{m}(Y)= \begin{cases}\frac{2 m}{M}(Y-M)+1 & \text { if } M-\frac{M}{2 m} \leqslant Y \leqslant M \\
0 & \text { otherwise }\end{cases}\right.
$$

# Proposition 4.3 (Integration of Harmonic Splines). 

Let us consider a strictly positive integer $m$. For $k \in\{1, \ldots, 2 m-1\}$, we denote by $V_{m k}$ and $W_{k}$ the unique indices such that

$$
f_{V_{m k}}([L, M])=\left[L+\frac{(k-1) M}{2 m}, L+\frac{k M}{2 m}\right]
$$

and

$$
f_{W_{k}}([L, M])=\left[L+\frac{k M}{2 m}, L+\frac{(k+1) M}{2 m}\right]
$$

Then,

$$
\int_{L}^{M} \psi_{L+\frac{k M}{2 m}}^{m} \mathrm{~d} \mu=\frac{\mu_{1}}{s_{V_{m k}}} \mu_{2}^{m+1-s_{V_{m k}}}+\frac{\mu}{s_{W_{k}+1}} \frac{1}{\mu_{2}^{m-s_{W_{k}}}}
$$

and

$$
\int_{L}^{M} \psi_{L}^{m} \mathrm{~d} \mu=\mu_{1}^{m+1}
$$

$\int_{L}^{M} \psi_{M}^{m} \mathrm{~d} \mu=\mu_{2}^{m+1}$.
In addition, if $\mu_{1}<\frac{1}{2}$ :

$$
\int_{L}^{M} \psi_{L}^{m} \mathrm{~d} \mu<\int_{L}^{M} \psi_{L+\frac{k M}{2 m}}^{m} \mathrm{~d} \mu<\int_{L}^{M} \psi_{M}^{m} \mathrm{~d} \mu
$$



Property 4.4. Given a strictly positive integer $m$, we set, for any integer $k \in\{0, \ldots, 2 m\}$ :

$$
x_{k}=L+\left(\frac{k}{2 m}\right) M
$$

and, for any $u \in \operatorname{dom}\left(\mathbb{B}_{\mathbb{S}_{\mu}}\right)$ :

$$
\begin{aligned}
& \mathbb{B}\left(u, \psi_{x_{k}}^{m}\right)=\int_{L}^{M}\left(-\frac{\sigma^{2} x^{2}}{2} \frac{\partial^{2} u}{\partial x^{2}}-\left[x \frac{\partial u}{\partial x}+r\right] u\right) \psi_{x_{k}}^{m} d x \\
& \quad=\lim _{m \rightarrow+\infty} \sum_{j=0}^{2 m} \mathbb{B}_{\mathbb{S}_{m}}\left(u\left(t, x_{j}\right)\right) \psi_{x_{k}}^{m}\left(\frac{M}{2 m}\right)=\lim _{m \rightarrow+\infty} \mathbb{B}_{\mathbb{S}_{m}}\left(u\left(t, x^{k}\right)\right)\left(\frac{M}{2 m}\right)
\end{aligned}
$$

where $\mathbb{B}_{\mathbb{S}_{m}}$ is the discrete Black-Scholes operator defined, for any $t$ in $[0, T]$, by:

$$
\begin{aligned}
& \mathbb{B}_{\mathbb{S}_{m}}\left(u\left(t, x^{k}\right)=-\frac{\sigma^{2}}{2} x_{k}^{2}\left(\frac{u\left(t, x^{k+1}\right)-2 u\left(t, x^{k}\right)+u\left(t, x^{k-1}\right)}{\left(\frac{M}{2 m}\right)^{2}}\right)\right. \\
& \left.-r x^{k}\left(\frac{u\left(t, x^{k+1}\right)-u\left(t, x^{k-1}\right)}{2 \frac{M}{2 m}}\right)+r C\left(t, x^{k}\right)\right) \\
&=-\frac{\sigma^{2}}{2} k^{2}\left(u\left(t, x^{k+1}\right)-2 u\left(t, x^{k}\right)+u\left(t, x^{k-1}\right)\right)\left(\frac{r k}{2 \frac{M}{2 m}}\right)+r C\left(t, x^{k}\right)
\end{aligned}
$$

The mean value formula yields asymptotically

$$
\int_{L}^{M} \mathbb{B}_{\mathbb{S}_{\mu}} u(x) \psi_{x_{k}}^{m} d \mu \approx \mathbb{B}_{\mathbb{S}_{\mu}} u\left(x^{k}\right) \int_{L}^{M} \psi_{x_{k}}^{m} d \mu \cdot
$$

Theorem 4.5 (Self-Similar Black-Scholes Operator Pointwise Formula).
Let us consider $u \in \operatorname{dom}\left(\mathbb{B}_{\mathbb{S}_{\mu}}\right)$. Then, for any $x \in M$, and any sequence $\left(x^{m}\right)_{m \in \mathbb{N}}$ of $V_{m} \backslash V_{0}$ which uniformly converges towards $x$ :

$$
\mathbb{B}_{\mathbb{S}_{\mu}}(u)(x)=\lim _{m \rightarrow+\infty} 2^{-m}\left(\int_{L}^{M} \psi_{x^{m}}^{m} d \mu\right)^{-1} \mathbb{B}_{\mathbb{S}_{m}}(u)\left(x^{m}\right) \cdot
$$

Proof. The uniform convergence directly comes from the fact that

$$
\left(\frac{M}{2 m}\right)\left(\int_{L}^{M} \psi_{x^{m}}^{m} d \mu\right)^{-1} \mathbb{B}_{\mathbb{S}_{m}}(u)\left(x^{m}\right)=C \int_{L}^{M} \mathbb{B}_{\mathbb{S}_{\mu}} \psi_{x^{m}}^{m} d \mu \int_{L}^{M} \psi_{x^{m}}^{m} d \mu=C \mathbb{B}_{\mathbb{S}_{\mu}}(u)(x) \cdot
$$



For $\mu_{1}=\mu_{2}=\frac{1}{2}$, one recovers the classical Black-Scholes operator, which implies that: $C=M$.

# 5 Proof of the Assumptions 

We hereafter consider the general case of non atomic finite measure $\mu$ with total mass $M=\bar{M}-\bar{L}$ (In the case of self-similar measures, it suffice to multiply the measure by $\bar{M}$ ).

### 5.1 First assumption 3.2

Notation (Space of Weighted Continuous Functions).
We will denote by $C(M)$ the space of weighted continuous functions on $M$ endowed with the norm

$$
\|u\|_{\eta, \infty}=\max _{x \in M}|x u(x)| \cdot
$$

Proof. of the first assumption
Let us consider $u \in \mathcal{V}_{0, \bar{M}}$. On the one hand, we have that

$$
\begin{aligned}
|x u(x)| & =\left|\int_{L}^{x}\left(s u^{2}(s)\right)^{\frac{1}{2}} d s\right| \\
& =\left|\int_{L}^{x} u(s) d s+\int_{L}^{x} s u^{1}(s) d s\right| \\
& \leqslant \sqrt{M}\left(\|u\|_{L^{2}}+|u|_{\mathcal{V}_{M}}\right) \\
& \leqslant \sqrt{M}\|u\|_{\mathcal{V}_{M}}
\end{aligned}
$$

We deduce the continuity of the injection $\iota:\left(\mathcal{V}_{M},\|\cdot\|_{\mathcal{V}_{M}}\right) \rightarrow\left(C_{\eta}(M),\|\cdot\|_{\eta, \infty}\right)$. On the other hand, for $u \in C_{\eta}(M)$, one also has that

$$
\|u\|_{L_{\mu}^{2}(M)}=\left(\int_{L}^{\bar{M}} \frac{1}{x^{2}}(x u)^{2} d \mu\right)^{\frac{1}{2}} \leqslant\|u\|_{\eta, \infty}\left(\int_{L}^{\bar{M}} \frac{1}{x^{2}} d \mu\right)^{\frac{1}{2}} \leqslant\|u\|_{\eta, \infty} \frac{\mu(M)^{\frac{1}{2}}}{L}
$$

the injection $\iota:\left(C_{\eta}(M),\|\cdot\|_{\eta, \infty}\right) \rightarrow\left(L_{\mu}^{2}(M),\|\cdot\|_{L_{\mu}^{2}(M)}\right)$ is continuous, so we obtain that

$$
\|u\|_{L_{\mu}^{2}(M)} \leqslant C_{0}\|u\|_{\mathcal{V} M}
$$

for $C_{0}=\frac{\sqrt{\bar{M}} \mu(M)}{L}=\frac{\bar{M}}{L}$.

### 5.2 Commentary on the second assumption 3.2

The assumption $4 r>\sigma^{2}$ is not that restrictive as it may seem in the first sight, for example, if we give a look to sample from Vance L. Martin data [LMM05]. The sample consist of $N=269$ observations on the European call options written on the S\&P500 stock index on the $4^{\text {th }}$ of April, 1995. One can calculate (see [RD21])



- The interest rate $r=0.0591$.
- The volatility $\sigma=0.076675$.

which means that

$$
4 r=0.2364 \ll 0.00587906=\sigma^{2}
$$

The second assumption could also be replaced by the following condition: for any $u$ in $\mathscr{D}(M)$,

$$
\|u\|_{L^{2}(M)} \leqslant C_{3}\|u\|_{L_{\mu}^{2}(M)}
$$

Given $u$ in $\operatorname{dom}(B)$, set, in the spirit of [Wlo87]:

$$
\tilde{\lambda}=\lambda C_{3} \quad, \quad w(t, x)=e^{-\tilde{\lambda} t} u(T-t, x)
$$

where $\lambda$ is Gårding's inequality constant in proposition 3.6. Then $\forall v \in \operatorname{dom}(B)$, with $w(0, x)=h(x)$, one has:

$$
\int_{M} \mathscr{L} \frac{d}{d t} w(t, x) \overline{v(x)} d \mu=-B(w, v)-\tilde{\lambda} \int_{M} \mathscr{L} w(t, x) \overline{v(x)} d \mu=-\hat{B}(w, v)
$$

Without affecting the solution space, one obtains the continuity and the coercivity of the form $\hat{B}$ :

$$
\begin{aligned}
|\hat{B}(u, v)| & \leqslant C|u|_{V_{M}}|v|_{V_{M}}+\tilde{\lambda}\|u\|_{L_{\mu}^{2}(M)}\|v\|_{L_{\mu}^{2}(M)} \\
& \leqslant\left(C+\tilde{\lambda} C_{0}\right)|u|_{V_{M}}|v|_{V_{M}}
\end{aligned}
$$

and:

$$
\begin{aligned}
\hat{B}(u, u) & \geqslant \frac{\sigma^{2}}{4}|u|_{V_{M}}^{2}-\lambda\|u\|_{L^{2}(M)}^{2}+\tilde{\lambda}\|u\|_{L_{\mu}^{2}(M)}^{2} \\
& \geqslant \frac{\sigma^{2}}{4}|u|_{V_{M}}^{2}
\end{aligned}
$$

# 5.3 Underlying asset price bounds 

An important question arises: how to choose $M$ and $L$ ? one answer is to use the law of $S_{t}$, the underlying asset price, then choose $M(\alpha)$ (respectively $L(\alpha)$ ) using the rule:

$$
1-P\left(L(\alpha) \leqslant S_{t} \leqslant M(\alpha)\right) \leqslant \alpha \quad 0 \leqslant t \leqslant T
$$

for some tolerance level $\alpha$.
One can deduce a similar rule in the case of boundary conditions. For example, in the case of a call option:

$$
P\left(S_{T}>K \mid S_{0}=L(\alpha)\right) \leqslant \alpha
$$

and

$$
P\left(S_{T} \leqslant K \mid S_{0}=M(\alpha)\right) \leqslant \alpha
$$



# 6 Numerical Simulation of Self-Similar European Options 

Let us consider as in section 4, the self-similar case, for an European options call, defined by the system:

$$
\begin{array}{ccc}
\frac{\partial C}{\partial t}(t, S)=B S \mu(C(t, S)) & \forall t \in[0, T], & \forall S \in \mathcal{M} \\
C(T, S)=h(S) & \forall S \in \mathcal{M} \\
C(t, L)=0 & \forall t \in[0, T] \\
C(t, M)=g(t) & \forall t \in[0, T]
\end{array}
$$

for a self-similar measure $\mu$ on $\mathcal{M}$, under the condition

$$
\left.4 r> \sigma^{2} \cdot\right
$$

where $h(S)=(S-K)^{+}$and $g(t)=M-K \exp (-r(T-t))$, and where the constant $\sigma$ is the volatility, $r$ the risk-free interest rate, $T$ the maturity of the option and $C$ represents the call price.

We will use the following change of variables: $\tau=T-t$, which leads to the following equation (with the same notations):

$$
\begin{array}{lll}
-\frac{\partial C}{\partial t}(t, S)=B S \mu(C(t, S)) & \forall t \in[0, T], & \forall S \in \mathcal{M} \\
C(0, S)=h(S) & \forall S \in \mathcal{M} \\
C(t, L)=0 & \forall t \in[0, T] \\
C(t, M)=g(t) & \forall t \in[0, T]
\end{array}
$$

for $g(t)=M-K \exp (-r t)$.
Remark 6.1.
The results of section 3 still hold, if we write $\tilde{C}=C-\tilde{g}$, where $\tilde{g}(t, x)=(x-L)\left(\frac{M-K \exp (-r t)}{M-L}\right)$, and replace the space $\mathcal{V}_{M}$ by $\mathcal{V}_{0, M}$, then we solve the non homogeneous problem

$$
\int_{L}^{M} \frac{\partial \tilde{C}}{\partial t} v d \mu+\mathcal{B}(\tilde{C}, v)=\int_{L}^{M} \frac{d \tilde{g}}{d t} v d \mu
$$

applying abstract theory of partial differential equations [Wlo87].

### 6.1 The Finite Difference Method

In the spirit of our previous work [RD19], we fix a strictly positive integer $N$, and set:

$$
h=\frac{T}{N}
$$

We will write, for a function $f, n \in\{0, \ldots, N\}$ and $k \in\{0, \ldots, 2 m\}$ :



$$
f(p, k)=f\left(n \frac{h, L+k M}{2 m}\right)
$$

We use the Euler implicit scheme, for any integer $n$ belonging to $\{0, \ldots, N-1\}$ :
$\forall k \in\{0, \ldots, 2 m\}: \quad \frac{\partial C}{\partial t}(n, k) \approx \frac{1}{h}(C(n+1, k)-C(n, k))$
The self-similar Black-Scholes operator for $k=\{0, \ldots, 2 m\}$ is approximated through

$$
\mathscr{B}^{\mu} C(n, k) \approx\left(2^{-m} \mu^{1_{s_{V_{M}}} \mu^{2 m-s_{V_{M}}}+\mu^{1_{s_{W_{+1}}} \mu^{2 m-s_{W}}} \mathscr{B}^{\bar{S}_{m}} C(n, k)\right.
$$

where $\mathscr{B}^{\bar{S}_{m}}$ is the discretized Black-Scholes operator given by

$$
\begin{aligned}
\mathscr{B}^{\bar{S}_{m}} C(n, k)= & \left.-\frac{\sigma^{2}}{2}\left(\frac{k M}{2 m}\right)^{2} \frac{C(n, k+1)-2 C(n, k)+C(n, k-1)}{\left(\frac{M}{2 m}\right)^{2}}\right) \\
& -\left[\left(\frac{k M}{2 m}\right) \frac{C(n, k+1)-C(n, k-1)}{2 \frac{M}{2 m}}\right]+[C(n, k)]
\end{aligned}
$$

For $0 \leqslant n \leqslant N-1$, and $1 \leqslant k \leqslant 2 m-1$, we define the following scheme:

$$
\left\{\begin{array}{l}
\frac{C^{h, m}(n+1, k)-C^{h, m}(n, k)}{h}=\delta_{m} \mathscr{B}^{\bar{S}_{m}} C^{h, m}(n, k) \\
\frac{C^{h, m}(n, 0)}{C^{h, m}(n, 2 m)}=0 \\
C^{h, m}(n, 2 m)=g(n) \\
\frac{C^{h, m}(0, k)}{C^{h, m}(n, k)}=h_{(k)}
\end{array}\right.
$$

For $n \in\{0, \ldots, N-1\}$, we set:

$$
\left.C(n)=\binom{C^{h, m}(n, 1) \ddots C^{h, m}(n, 2 m-1)}{C^{h, m}\left(n, f_{W_{1}}(M)\right) \ddots C^{h, m}\left(n, f_{W_{2 m-1}}(M)\right)}\right\} \quad W_{1}, \ldots, W_{2 m-1} \in\{1,2 m\}
$$

We have the following recurrence relation:

$$
C(n+1)=A C(n)+B(n)
$$

where the $(2 m-1) \times(2 m-1)$ matrix $A$ is given by:

$$
A=I_{2 m-1}-h 2^{-m} \Psi_{m}^{-1} \mathscr{B}^{\bar{S}_{m}}
$$

and where $I_{2 m-1}$ denotes the $(2 m-1) \times(2 m-1)$ identity matrix, $\Psi_{m}$ and $\mathscr{B}^{\bar{S}_{m}}$ the $(2 m-1) \times(2 m-1)$ matrices:

$$
\Psi_{m}=\left(\begin{array}{ccccc}
\cdots & 0 & \mu^{1_{s_{V_{M}}} \mu^{2 m+1-s_{V_{M}}}+\mu^{1_{s_{W_{+1}}} \mu^{2 m-s_{W}}} & 0 & \cdots \\
\vdots & & & & \\
\vdots & & & & \\
0 &
\end{array}\right)_{\infty}
$$



$$
\left(B_{S_{m}}\right)^{-1}=\left(\begin{array}{ccccc}
\frac{-\sigma^{2}-r}{\sigma^{2}} & 2 & 0 & \ldots & 0 \\
\frac{\sigma^{2}-r}{-4 \sigma^{2}-r} & \frac{2 \sigma^{2}+r}{\sigma^{2}} & 2 & \ldots & 0 \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
0 & 0 & 0 & \ldots & \frac{p_{2 m-2}^{2} \sigma^{2}-r}{\left(p_{2 m-2}\right)^{2} \sigma^{2}+r} \\
\frac{\left(p_{2 m-1}\right)^{2} \sigma^{2}-r}{-r} & 0 & 0 & \ldots & 0
\end{array}\right)
$$

and

$$
B_{(n)}=h^{2-m} \mu^{2-(m+1)}\binom{\left(p_{2 m-1}\right)^{2} \sigma^{2}+{ }_{2}^{2 m-1)}{0 \vdots 0 g(n)}
$$

# 6.2 Numerical Analysis 

### 6.2.0.1 The Scheme Error and Consistency

Let us consider a function $V_{M}$ defined on $M$. For any integer $n$ in $\{0, \ldots, N-1\}$, and any $X$ in $M$ :

$$
\frac{\partial v}{\partial t}(n h, X)=\frac{1}{h}(v((n+1) h, X)-v(n h, X))+O(h)
$$

As in [RD19], for any strictly positive integer m, and any $\mathbf{X}$ in $\mathcal{V}_{m} \backslash \mathcal{V}_{0}$, we can prove that:

$$
2^{-m}\left(\int_{M} \mathcal{L} \psi_{X}^{m} d \mu\right)^{-1} B S_{m} v(\mathbf{X})=\int_{M} \mathcal{L} B S \mu \psi_{X}^{m} d \mu \int_{M} \mathcal{L} \psi_{X}^{m} d \mu
$$

and that there exists a vertex $\mathbf{Z}$ in the $m$-cell $f_{W}([L, M])$ containing $\mathbf{X}$ such that

$$
\left|B S \mu v(X)-2^{-m}\left(\int_{M} \mathcal{L} \psi_{X}^{m} d \mu\right)^{-1} B S_{m} v(X)\right|=\left|B S \mu v(X)-B S \mu v(Z)\right| /|v(X)-v(Z)| /|\mathbf{X}-\mathbf{Z}| /(4{ }_{2})^{m}
$$

using remark 3.2 and the uniform continuity of $v \in V_{M}$. Thus,

$$
B S \mu v(\mathbf{X})=2^{-m}\left(\int_{M} \mathcal{L} \psi_{X}^{m} d \mu\right)^{-1} B S_{m} v(\mathbf{X})+O\left(2^{-m}\right)
$$

The consistency error of our scheme is given by :

$$
\varepsilon_{n, k}^{h, m}=O(h)+O\left(2^{-m}\right) \quad 0 \leqslant n \leqslant N, 0 \leqslant k \leqslant 2 m
$$



We can check that the scheme is consistent:
$\lim _{h \rightarrow 0, m \rightarrow \infty} \varepsilon_{n, k}^{h, m}=0 \cdot$

# 6.2.0.2 Stability 

We hereafter prove that the scheme is conditionally stable for the $\|\cdot\|_{\infty}$ norm.
Let us recall that, for $0 \leqslant n \leqslant N$, and $0 \leqslant k \leqslant 2 m$ :

$$
\begin{aligned}
C^{h, m}(n+1, k)= & C^{h, m}(n, k)\left(1-h \frac{\delta^{m} \sigma^{2}}{2} k^{2}\right) \\
& +C^{h, m}(n, k+1)\left(h \frac{\delta^{m}}{\sigma^{2}} 2 k^{2}+h \delta^{m} \frac{r}{2} k\right) \\
& +C^{h, m}(n, k-1)\left(h \frac{\delta^{m}}{\sigma^{2}} 2 k^{2}-h \delta^{m} \frac{r}{2} k\right)-C^{h, m}(n, k) h \delta^{r} \\
= & C^{h, m}(n, k)(1-\alpha k)+C^{h, m}(n, k+1)\left(-\frac{\alpha k}{2}+\beta k\right) \\
& +C^{h, m}(n, k-1)\left(-\frac{\alpha k}{2}-\beta k\right)-C^{h, m}(n, k) \gamma
\end{aligned}
$$

If we consider $\gamma=0$, this is just an affine combination. Moreover, we have:

$$
\begin{gathered}
1-\alpha k \geqslant 1-\frac{\sigma^{2}}{h} \frac{2 \delta^{m}}{2^{m}}\left(\int_{L}^{M} \psi_{X}^{m} d \mu\right) \geqslant 0 \\
\frac{\alpha k}{2}-\beta k \geqslant 0 \\
1-\gamma \geqslant 0
\end{gathered}
$$

May we suppose that $\sigma^{2} \geqslant r$ and that the following CFL condition

$$
h \frac{2^{m}}{2^{2 m}}\left(\int_{L}^{M} \psi_{X}^{m} d \mu\right) \leqslant \frac{1}{\sigma^{2}}
$$

is satisfied, the combination is then convex, and the scheme is stable for the norm $\|\cdot\|_{\infty}$.
For $\gamma \neq 0$, one has :

$$
\begin{aligned}
(1-\gamma) \min _{0 \leqslant j \leqslant 2 m} C^{h, m}(n, j) \leqslant C^{h, m}(n+1, k) \leqslant & \max _{0 \leqslant j \leqslant 2 m} C^{h, m}(n, j)-\gamma \\
\min _{0 \leqslant j \leqslant 2 m} C^{h, m}(n, j) & \leqslant \max _{0 \leqslant j \leqslant 2 m} C^{h, m}(n, j)-\gamma(1-\gamma)^{n} \\
\min _{0 \leqslant j \leqslant 2 m} C^{h, m}(0, j) & \leqslant \max _{0 \leqslant j \leqslant 2 m} C^{h, m}(n, j)
\end{aligned}
$$

and the scheme is $\|\cdot\|_{\infty}$-stable under the same conditions.



# 6.2.0.3 Convergence 

Theorem 6.1. If the above CFL condition holds, the scheme is convergent for the norm $\|\cdot\|_{2, \infty}$ given by:

$$
\left\|(\Delta h, m(n, k))_{0 \leqslant n \leqslant N, 0 \leqslant k \leqslant 2 m}\right\|_{2, \infty}=\max _{0 \leqslant n \leqslant N}\left(\sum_{0 \leqslant k \leqslant 2 m} \mu\left(f W_{k}(M)\right)(\Delta h, m(n, k))^{2}\right)^{\frac{1}{2}}
$$

where $\mu\left(f W_{k}(M)\right)$ is the measure of the $f W_{k}(M)$.
Proof. For $0 \leqslant n \leqslant N$ and $0 \leqslant k \leqslant 2 m$, we set:

$$
w_{k}^{n}=C(n, k)-\Delta h, m(n, k)
$$

and

$$
\Delta_{S m} C(n, k)=-\frac{\sigma^{2}}{2}\left(\frac{k \bar{M}}{2 m}\right)^{2}\left(C(n, k+1)-2 C(n, k)+C(n, k-1)\right.\left(\frac{\bar{M}}{2 m}\right)^{2})-\left[\left(\frac{k \bar{M}}{2 m}\right)(C(n, k+1)-C(n, k))\right]+\left[C(n, k) \cdot\right.
$$

We can check that

$$
\begin{aligned}
& \frac{w_{k}^{n+1}-w_{k}^{n}}{h}-\frac{\sigma^{2}}{2} k^{2} \delta_{m}\left(w_{k+1}^{n} \cdot 2 w_{k}^{n}+w_{k-1}^{n}\right)-r k \delta_{m}\left(w_{k+1}^{n}-w_{k}^{n}\right)+r \delta_{m} w_{k}^{n}=\varepsilon_{h, m}^{n, k} \\
& 0 \leqslant n \leqslant N-1,1 \leqslant k \leqslant 2 m-1 \\
& w_{0}^{n}=w_{2 m}^{n}=0 \quad 0 \leqslant n \leqslant N \\
& w_{k}^{0}=0 \quad 1 \leqslant k \leqslant 2 m-1
\end{aligned}
$$

Let us set, for any integer $n$ in $\{0, \ldots, N\}$ :

$$
W^{n}=\left(\begin{array}{c}
w_{1}^{n} \\
\vdots \\
w_{2 m-1}^{n}
\end{array}\right), \quad E^{n}=\left(\begin{array}{c}
\varepsilon_{h, m}^{n, 1} \\
\vdots \\
\varepsilon_{h, m}^{n, 2 m-1}
\end{array}\right)
$$

One has:

$$
W^{0}=0
$$

and

$$
\forall n \in\{0, \ldots, N-1\}: \quad W^{n+1}=A W^{n}+h E^{n}
$$

By induction, this yields, for any integer $n$ in $\{0, \ldots, N-1\}$ :

$$
W^{n+1}=A^{n} W^{0}+h \sum_{j=0}^{n} A^{j} E^{n-j}=h \sum_{j=0}^{n} A^{j} E^{n-j}
$$

Since $A$ is a symmetric matrix, the CFL stability condition yields, for any integer $n$ in $\{0, \ldots, N\}$ :



$$
\left|W^{n}\right| \lesssim h \sum_{j=0}^{n-1}\|A\|^{j}\left(\max _{0 \leqslant j \leqslant n-1}\left|\mathcal{E}_{j}\right|\right) \lesssim h n\left(\max _{0 \leqslant j \leqslant n-1}\left|\mathcal{E}_{j}\right|\right) \lesssim h N\left(\max _{0 \leqslant j \leqslant n-1}\left|\mathcal{E}_{j}\right|\right) \lesssim T\left(\max _{0 \leqslant j \leqslant n-1} \sum_{k=1}^{2 m-1}\left|\varepsilon_{j, k}^{h, m}\right|^{2}\right)^{\frac{1}{2}} \alpha
$$

By assuming $\mu_{1} \geqslant \frac{1}{2}$ (the same result holds for $\mu_{1} \lesssim \frac{1}{2}$ by changing $\mu_{1}$ into $\mu_{2}$ ), we deduce then that:

$$
\begin{aligned}
\max _{0 \leqslant n \leqslant N}\left(\sum_{k=1}^{2 m-1} \mu\left(f_{W_{k}}(M)\right)\left|w_{k}^{n}\right|^{2}\right)^{\frac{1}{2}} & \lesssim \max _{1 \leqslant k \leqslant 2 m-1}\left(\mu\left(f_{W_{k}}(M)\right)\right)^{\frac{1}{2}} \max _{1 \leqslant n \leqslant N}\left|W^{n}\right| \\
& \lesssim \max _{1 \leqslant k \leqslant 2 m-1}\left(\mu\left(f_{W_{k}}(M)\right)\right)^{\frac{1}{2}} T\left(\max _{0 \leqslant n \leqslant N-1}\left(\sum_{k=1}^{2 m-1}\left|\varepsilon_{n, k}^{h, m}\right|^{2}\right)^{1 / 2} \alpha\right) \\
& \lesssim \max _{1 \leqslant k \leqslant 2 m-1}\left(\mu\left(f_{W_{k}}(M)\right)\right)^{\frac{1}{2}} T\left((2 m-1)^{\frac{1}{2}} \max _{0 \leqslant n \leqslant N-1,1 \leqslant k \leqslant 2 m-1}\left|\varepsilon_{n, k}^{h, m}\right|\right) \\
& \lesssim \tilde{b}\left(\mu_{1} \times 2^{q}\right) m T\left(\max _{0 \leqslant n \leqslant N-1,1 \leqslant k \leqslant 2 m-1}\left|\varepsilon_{n, k}^{h, m}\right|\right) \\
& =\tilde{b}\left(\mu_{1} \times 2^{q}\right) m+O(h)+O\left(2^{-m}\right) \\
& =O\left(\left(c \mu_{1}^{2}\right)^{m}\right)
\end{aligned}
$$

The scheme is then convergent.

# 6.3 Self-Similar Pricing 

In the sequel, we give a numerical simulation of the self-similar pricing, in the case of a call:

$$
\begin{aligned}
& B_{t}^{\mathcal{C}}(t, S)=B_{\mathcal{S}}^{\mu}(\mathcal{C})(t, S) \quad \forall t \in[0, T], \forall S \in[L, M] \\
& \mathcal{C}(T, S)=(S-K)^{+} \quad \forall x \in[L, M] \\
& \mathcal{C}(t, L)=0 \quad \forall t \in \ewish[0, T] \\
& \mathcal{C}(t, M)=M-K \exp (-r(T-t)) \quad \forall t \in[0, T]
\end{aligned}
$$

for a self-similar measure $\mu$ on $[L, M]$. The solutions are generated using the finite difference method, for





Figure 1: Black-Scholes solution $u(0, x)$ for different values of the weights.
The self-similar Black-Scholes model generates an exotic pricing for different values of $\mu_{1}$, including the classical one for $\mu_{1}=\frac{1}{2}$.


Figure 2: The call value for different values of the weights.

# 6.4 The Greeks 

As in [Dav17], we recall that, in finance, the sensitivity of a portfolio to changes in parameters values can be measured through what commonly call "the Greeks", i.e.,
i. The Delta, $\Delta=\frac{d C}{d S} \in[0,1]$, which enables one to quantify the risk, and is thus the most important Greek. It can also be interpreted as a probability that the option will expire in the money.



ii. The Gamma, $\Gamma=\frac{\partial^{2} C}{\partial S^{2}} \geqslant 0$, which measures the rate of the acceleration of the option price, with respect to changes in the underlying price.
iii. The Vega (the name of which comes from the form of the Greek letter $\nu$ ), $\nu=\frac{\partial C}{\partial \sigma}$, which measures the sensitivity to volatility.
iv. The Theta $\Theta=\frac{\partial C}{\partial t}$, which is the time cost of holding an option.
v. The rho, $\rho=\frac{\partial C}{\partial r}$, which measures the sensitivity to the risk-free interest rate.

The good strategy, for traders, is to have delta-neutral positions at least once a day, and, whenever the opportunity arises, to improve the Gamma and the Vega.

# 6.4.1 The Delta 


6.4.2 The Gamma




# 6.5 Discussion 

Let us make a few remarks about the behavior of the solution with respect to the weight $\mu$ at $t=0$ :
i. For $\mu_{1}=\frac{1}{3}$ : the premium is greater than that of the classical model under the strike and smaller above. The Greeks value shows a drastic increase in the strike neighbor, and self-similarity clearly affects in the money region. The Theta shows a slower premium expected decrease.
ii. For $\mu_{1}=\frac{2}{3}$ : the premium is everywhere greater than that of the classical model. The Greeks value increases progressively in the strike neighbor, and self-similarity affects in the money region. The Theta indicates a slower premium expected decrease in the money and a greater decrease deep in the money.
The dynamic generated by the self-similar Black-Scholes model is exotic and enables the emergence of non-standard behaviors, the parameter $\mu_{1}$ can capture the behavior of non confident investors under uncertainty and other factors influencing their perception of future.
The self-similar Black-Scholes equation can be understood as a diffusion equation with a time change through self-similar probability $\mu$, where the cumulative distribution function satisfies for $x \in] 0,1[$,

$$
\left.r_{0, x}=[f W \mid 0,1]\right) \text { for some word } W, \quad \mu_{r} \mid\left[0, x\right]=\Pi_{i \in W} \mu_{i}
$$

depending on the address (path) of $x$. According to this remark, we can create more exotic behavior by using a self-similar measure $\mu$ with many weights or enable the weights to change over time.

## References

[AP05] Y. Achdou and O. Pironneau. Computational Methods for Option Pricing. Society for Industrial and Applied Mathematics, 2005.
[Dav17] C. David. Control of the Black-Scholes equation. Comput. Math. Appl., 73(7):1566-1575, 2017.
[For96] P. Fortune. Anomalies in option pricing: The black-scholes model revisited. New England Economic Review, March/April:17-40, 1996.
[HLN06] J. Hu, K.-S. Lau, and S.-M. Ngai. Laplace operators related to self-similar measures on $\mathbb{R}^{d}$. Journal of Functional Analysis, 239:542-565, 2006.
[Kig01] J. Kigami. Analysis on Fractals. Cambridge University Press, 2001.
[Kil94] T. Kilpeläinen. Weighted sobolev spaces and capacity. Annales Academiae Scientiarum Fennicae. Series A I. Mathematica, 19(1):95-113, 1994.
[KN01] R. Kangro and R. Nicolaides. Far field boundary conditions for black-scholes equations. SIAM Journal on Numerical Analysis, 38(4):1357-1368, 2001.



[LM68] J.-L. Lions and E. Magenes. Problèmes aux limites non homogènes et applications. Dunod, 1968.
[LMM05] G. C. Lim, G. M. Martin, and V. L. Martin. Parametric pricing of higher order moments in s\&p500 options. Journal of Applied Econometrics, 20(3):377-404, 2005.
[Man97] B. B. Mandelbrot. Fractals and Scaling in Finance. Springer New York, 1997.
[MR92] Z.-M. Ma and M. Röckner. Introduction to the Theory of (Non-Symmetric) Dirichlet Forms. Springer-Verlag, 1992.
[RD19] N. Riane and C. David. The finite difference method for the heat equation on sierpiński simplices. International Journal of Computer Mathematics, 96(7):1477-1501, 2019.
[RD21] N. Riane and C. David. An inverse black-scholes problem. Optimization and Engineering, 22:2183-2204, 2021.
[Str06] R. S. Strichartz. Differential Equations on Fractals. A Tutorial. Princeton University Press, 2006.
[Wlo87] J. Wloka. Partial differential equations. Cambridge University Press, 1987.
[Zei90] E. Zeidler. Nonlinear Functional Analysis and its Applications. II/A.: Linear Monotone Operators. Springer, 1990.



