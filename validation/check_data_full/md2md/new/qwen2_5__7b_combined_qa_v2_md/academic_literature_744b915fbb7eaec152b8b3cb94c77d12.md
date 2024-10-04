# SELF-ADJOINT AND MARKOVIAN EXTENSIONS OF INFINITE QUANTUM GRAPHS 

ALEKSEY KOSTENKO, DELIO MUGNOLO, AND NOEMA NICOLUSSI


#### Abstract

We investigate the relationship between one of the classical notions of boundaries for infinite graphs, graph ends, and self-adjoint extensions of the minimal Kirchhoff Laplacian on a metric graph. We introduce the notion of finite volume for ends of a metric graph and show that finite volume graph ends is the proper notion of a boundary for Markovian extensions of the Kirchhoff Laplacian. In contrast to manifolds and weighted graphs, this provides a transparent geometric characterization of the uniqueness of Markovian extensions, as well as of the self-adjointness of the Gaaffney Laplacian - the underlying metric graph does not have finite volume ends. If however finitely many finite volume ends occur (as is the case of edge graphs of normal, locally finite tessellations or Cayley graphs of amenable finitely generated groups), we provide a complete description of Markovian extensions upon introducing a suitable notion of traces of functions and normal derivatives on the set of graph ends.


## ContENTS

1. Introduction ..... 2
Notation ..... 5
2. Quantum graphs ..... 5
2.1. Combinatorial and metric graphs ..... 5
2.2. Graph ends ..... 6
2.3. Kirchhoff Laplacian ..... 8
2.4. Deficiency indices ..... 9
3. Graph ends and $H^{1}(\mathcal{G})$ ..... 11
3.1. $H^{1}(\mathcal{G})$ and boundary values ..... 11
3.2. Nontrivial and finite volume ends ..... 14
3.3. Description of $H_{0}^{1}(\mathcal{G})$ ..... 15
4. Deficiency indices ..... 17
4.1. Deficiency indices and graph ends ..... 17
4.2. Proof of Theorem 4.1 ..... 18
5. Properties of self-adjoint extensions ..... 21
6. Finite energy self-adjoint extensions ..... 25
6.1. Normal derivatives at graph ends ..... 26
6.2. Properties of the trace and normal derivatives ..... 28
6.3. Description of self-adjoint extensions ..... 30
7. Deficiency indices of antitrees ..... 33
7.1. Antitrees ..... 33
[^0]
[^0]:    2020 Mathematics Subject Classification. Primary 34B45; Secondary 47B25; 81Q10.
    Key words and phrases. Quantum graph, graph end, self-adjoint extension, Markovian extension, harmonic function.
    Research supported by the Austrian Science Fund (FWF) under Grants No. P 28807 (A.K. and N.N.) and W 1245 (N.N.), by the German Research Foundation (DFG) under Grant No. 397230547 (D.M.), and by the Slovenian Research Agency (ARRS) under Grant No. J1-1690 (A.K.). The authors would like to acknowledge that this article is based upon work from COST Action CA18232 MAT-DYN-NET, supported by COST (European Cooperation in Science and Technology).



7.2. Harmonic functions 34
7.3. Finite deficiency indices 36
7.4. Infinite deficiency indices 38
7.5. Proof of Theorem $7.1 \quad 40$
Appendix A. Linear relations in Hilbert spaces 40
Appendix B. A rope ladder graph 41
Acknowledgments 44
References 44

# 1. Introduction 

This paper is concerned with developing extension theory for infinite quantum graphs. Quantum graphs are Schrödinger operators on metric graphs, that is combinatorial graphs where edges are considered as intervals with certain lengths. Motivated by a vast amount of applications in chemistry and physics, they have become a popular subject in the last decades (we refer to $[8,9,26,67]$ for an overview and further references). From the perspective of Dirichlet forms, quantum graphs play an important role as an intermediate setting between Laplacians on Riemannian manifolds and difference Laplacians on weighted graphs. On the one hand, being locally one-dimensional, quantum graphs allow to simplify considerations of complicated geometries. On the other hand, there is a close relationship between random walks on graphs and Brownian motion on metric graphs, however, in contrast to the discrete case, the corresponding quadratic form in the metric case is a strongly local Dirichlet form and in this situation more tools are available (see $[7,28,58,59]$ for various manifestations of this point of view). Let us also mention that metric graphs can be seen as non-Archimedian analogs of Riemann surfaces, which finds numerous applications in algebraic geometry (see $[2,5,6,70]$ for further references).

The most studied quantum graph operator is the Kirchhoff Laplacian, which provides the analog of the Laplace-Beltrami operator in the setting of metric graphs. Its spectral properties are crucial in connection with the heat equation and the Schrödinger equation and any further analysis usually relies on the self-adjointness of the Laplacian. Whereas on finite metric graphs the Kirchhoff Laplacian is always self-adjoint, the question is more subtle for graphs with infinitely many edges. For instance, a uniform lower bound for the edge lengths guarantees self-adjointness (see $[9,67]$ ), but this commonly used condition is independent of the combinatorial graph structure and clearly excludes a number of interesting cases (the so-called fractal metric graphs). Moreover, most of the results on strongly local Dirichlet forms require completeness of a given metric space w.r.t. the "intrinsic" metric (cf., e.g., [74]), which coincides with the natural path (geodesic) metric in the case of metric graphs. Geodesic completeness (w.r.t. the natural path metric) guarantees self-adjointness of the (minimal) Kirchhoff Laplacian, however, this result is far from being optimal (see [27, §4] and also Section 2.4 below). The search for self-adjointness criteria for infinite quantum graphs is an open and - in our opinion - rather difficult problem.

If the (minimal) Kirchhoff Laplacian is not self-adjoint, the natural next step is to ask for a description of its self-adjoint extensions, which corresponds to possible descriptions of the system in quantum mechanics or, if we speak about Markovian extensions, possible descriptions of Brownian motions. Naturally, this question is tightly related to finding appropriate boundary notions for infinite graphs. Our goal in this paper is to investigate the connection between extension theory and



one particular notion, namely graph ends, a concept which goes back to the work of Freudenthal [30] and Halin [38] and provides a rather refined way of compactifying graphs. However, the definition of graph ends is purely combinatorial and naturally must be modified to capture the additional metric structure of our setting. Based on the correspondence between graph ends and topological ends of metric graphs, we introduce the concept of ends of finite volume. First of all, it turns out that finite volume ends play a crucial role in describing the Sobolev spaces $H^{1}$ and $H_{0}^{1}$ on metric graphs. More specifically, we show that the presence of finite volume ends is the only reason for the strict inclusion $H_{0}^{1} \subsetneq H^{1}$ to hold. This in particular provides a surprisingly transparent geometric characterization of the uniqueness of Markovian extensions of the minimal Kirchhoff Laplacian as well as the selfadjointness of the so-called Gaffney Laplacian (we are not aware of its analogs either in the manifold setting or in the context of weighted graph Laplacians, cf. [35, $37,45,52,61,62])$. As yet another manifestation of the fact that finite volume graph ends represent the proper boundary for Markovian extensions of the Kirchhoff Laplacian, we provide a complete description of all finite energy extensions (i.e., self-adjoint extensions with domains contained in $H^{1}$, and all Markovian extensions clearly satisfy this condition), however, under the additional assumption that there are only finitely many finite volume ends. Let us stress that this class of graphs includes a wide range of interesting models (Cayley graphs of a large class of finitely generated groups, tessellating graphs, rooted antitrees etc. have exactly one end and in this case there are no finite volume ends exactly when the total volume of the corresponding metric graph is infinite). Moreover, we emphasize that in all those cases the dimension of the space of finite energy extensions is equal to the number of finite volume ends, however, for deficiency indices, i.e., the dimension of the space of self-adjoint extensions, this only gives a lower bound (for example, for Cayley graphs the dimension of the space of finite energy extensions is independent of the choice of a generating set, although deficiency indices do depend on this choice in a rather nontrivial way). On the other hand, it may happen that these dimensions coincide. The latter holds only if the maximal domain is contained in $H^{1}$, that is, if every self-adjoint extension is a finite energy extension. This is further equivalent to the validity of a certain non-trivial Sobolev-type inequality (see (1.1) below). The appearance of this condition demonstrates the mixed dimensional behavior of infinite metric graphs since the analogous estimate holds true in the one-dimensional situation, but usually fails in the PDE setting.

Let us now sketch the structure of the article and describe its content and our results in greater details.

In Section 2 we collect basic notions and facts about graphs and metric graphs (Section 2.1); graph ends (Section 2.2); the minimal and maximal Kirchhoff Laplacians (Section 2.3); deficiency indices and their connection with the spaces of $L^{2}$ harmonic and $\lambda$-harmonic functions (Section 2.4).

The core of the paper is Section 3, where we discuss the Sobolev spaces $H^{1}(G)$ and $H_{0}^{1}(G)$ and introduce the set of finite volume ends $C_{0}(G)$ (Definition 3.8). We show that $C_{0}(G)$ is the proper boundary for $H^{1}$ functions, which can also be seen as an ideal boundary by applying $C^{*}$-algebra techniques (see Remark 3.14). The central result of this section is Theorem 3.12 , which shows that $H^{1}(G)=H_{0}^{1}(G)$ if and only if there are no finite volume ends. The latter also leads to a surprisingly transparent geometric characterization of the uniqueness of Markovian extensions



of the Kirchhoff Laplacian (Corollary 5.5) as well as the self-adjointness of the Gaffney Laplacian $\mathcal{H}_{G}$ (see Remark 5.6 (ii) for details and the definition of $\mathcal{H}_{G}$ ).

Section 4 contains further applications of the above considerations. Namely, Theorem 4.1 demonstrates that deficiency indices of the minimal Kirchhoff Laplacian can be estimated from below by the number of finite volume ends. This estimate is sharp (e.g., if there are infinitely many finite volume ends) and we also find necessary and sufficient conditions for the equality to hold. In particular, if there are only finitely many ends of finite volume, $\# \mathcal{C}_{0}(G)<\infty$, the latter is equivalent to the validity of the following Sobolev-type inequality (see Remark 4.2)

$$
\left\|f^{\prime}\right\|_{L^{2}(G)} \leq C\left(\|f\|_{L^{2}(G)}+\left\|f^{\prime \prime}\right\|_{L^{2}(G)}\right)
$$

for all $f$ in the maximal domain of the Kirchhoff Laplacian. Metric graphs are locally one-dimensional and the corresponding inequality is trivially satisfied in the onedimensional case, however, globally infinite metric graphs are more complex and hence (1.1) rather resembles the multi-dimensional setting of PDEs (in particular, (1.1) does not hold true if $G$ has a non-free finite volume end, see Proposition 4.9).

In the next sections, we focus on a particular class of self-adjoint extensions whose domains are contained in $H^{1}$ (we call them finite energy extensions). These extensions have good properties and their importance stems from the fact that they contain the class of Markovian extensions (they also arise as self-adjoint restrictions of the Gaffney Laplacian). In Section 5 we show that (under some additional mild assumptions) their resolvents and heat semigroups are integral operators with continuous, bounded kernels and they belong to the trace class if $G$ has finite total volume (Theorems 5.1 and 5.2 ).

In Section 6 we proceed further and show that finite volume ends is the proper boundary for this class of extensions. Namely, under the additional and rather restrictive assumption of finitely many ends with finite volume, in Sections 6.16.2, we introduce a suitable notion of a normal derivative at graph ends (as a by-product, this also gives an explicit description of the domain of the Neumann extension, see Corollary 6.7). Section 6.3 contains a complete description of finite energy extensions and also of Markovian extensions (Theorem 6.11). Let us stress that the case of infinitely many ends is incomparably more complicated and will be the subject of future work.

In general, the inequality in (1.1) is difficult to verify/contradict and even simple examples can exhibit rather complicated behavior (see Appendix B). The only reason for which (1.1) fails to hold is the presence of $L^{2}$ harmonic functions having infinite energy, that is, not belonging to $H^{1}$. Moreover, in order to compute deficiency indices of the Kirchhoff Laplacian one, roughly speaking, needs to find the dimension of the space of $L^{2}$ harmonic functions and description of self-adjoint extensions requires a thorough understanding of the behavior of $L^{2}$ harmonic functions at "infinity". Dictated by a distinguished role of harmonic functions in analysis, there is an enormous amount of literature dedicated to various classes of harmonic functions (positive, bounded etc.), which is further related to different notions of boundaries (metric completion, Poisson and Martin boundaries, Royden and Kuro):: boundaries etc.) and search for a suitable notion in this context (namely, $L^{2}$ harmonic functions) is a highly nontrivial problem, which seems not to be very well studied either in the context of incomplete manifolds (cf. [61, 62]) or in the case of weighted graphs (see [39, 45]). We further illustrate this by considering the case of rooted antitrees, a special class of infinite graphs with a particularly high degree



of symmetry (see Section 7). Infinite rooted antitrees have exactly one graph end, which makes them a good toy model for our purposes. The above considerations show that the space of finite energy $L^{2}$ harmonic functions is nontrivial only if a given metric antitree has finite total volume and in this case the only such functions are constants. However, adjusting lengths in a suitable way for a concrete polynomially growing antitree (Figure 1) we can make the space of $L^{2}$ harmonic functions as large as we please (even infinite dimensional!).

Notation. $\mathbb{Z}, \mathbb{R}, \mathbb{C}$ have their usual meaning; $\mathbb{Z}_{\geq a}:=\mathbb{Z} \cap[a, \infty)$. $z^{*}$ denotes the complex conjugate of $z \in \mathbb{C}$. For a given set $S, \# S$ denotes its cardinality if $S$ is finite; otherwise we set $\# S=\infty$. If it is not explicitly stated otherwise, we shall denote by $\left(x_{n}\right)$ a sequence $\left(x_{n}\right)_{n=0}^{\infty}$. $C_{b}(X)$ is the space of bounded, continuous functions on a locally compact space $X$. $C_{0}(X)$ is the space of continuous functions vanishing at infinity. For a finite or countable set $X, C(X)$ is the set of complex-valued functions on $X$. $\mathcal{G}_{\mathrm{d}}=(V, E)$ is a discrete graph (satisfying Hypothesis 2.1). $\mathcal{G}=\left(\mathcal{G}_{\mathrm{d}},|\cdot|\right)$ is a metric graph (see p. 6). $\varrho$ is the natural (geodesic) path metric on $\mathcal{G}$ (see p. 6 ). $\varrho_{m}$ is the star metric on $V$ corresponding to the star weight $m$ (see (2.13)). $\Omega\left(\mathcal{G}_{\mathrm{d}}\right)$ denotes the graph ends of $\mathcal{G}_{\mathrm{d}}$ (see Definition 2.1). $C(\mathcal{G})$ denotes the topological ends of a metric graph $\mathcal{G}$ (see Definition 2.2). $C_{0}(\mathcal{G})$ stays for the finite volume topological ends of $\mathcal{G}$ (see Definition 3.8). $\widehat{\mathcal{G}}$ is the end (Freudenthal) compactification of $\mathcal{G}$ (see p. 7 ). $H_{0}^{0}$ is the pre-minimal Kirchhoff Laplacian on $\mathcal{G}$ (see (2.9)). $H_{0}$ is the minimal Kirchhoff Laplacian, the closure of $H_{0}^{0}$ in $L^{2}(\mathcal{G})$ (see (2.9)). $n_{ \pm}\left(H_{0}\right)$ are the deficiency indices of $H_{0}($ see $(2.15))$. $H_{F}$ and $H_{N}$ are the Friedrichs and Neumann extensions of $H_{0}$ (see p. 12 and, respectively, p. 24). $H$ is the maximal Kirchhoff Laplacian on $\mathcal{G}$ (see (2.8)).

# 2. QUANTUM GRAPHS 

2.1. Combinatorial and metric graphs. In what follows, $\mathcal{G}_{\mathrm{d}}=(V, E)$ will be an unoriented graph with countably infinite sets of vertices $V$ and edges $E$. For two vertices $u, v \in V$ we shall write $u \sim v$ if there is an edge $e_{u, v} \in E$ connecting $u$ with $v$. For every $v \in V$, we denote the set of edges incident to the vertex $v$ by $E_{v}$ and

$$
\operatorname{deg}_{\mathcal{G}}(v):=\#\left\{e \mid e \in E_{v}\right\}
$$

is called the degree (valency or combinatorial degree) of a vertex $v \in V$. When there is no risk of confusion about which graph is involved, we shall simplify and write deg instead of $\operatorname{deg}_{\mathcal{G}}$. A path $\mathfrak{P}$ of length $n \in \mathbb{Z}_{\geq 0} \cup\{\infty\}$ is a sequence of vertices $\left(v_{0}, v_{1}, \ldots, v_{n}\right)$ such that $v_{k-1} \sim v_{k}$ for all $k \in\{1, \ldots, n\}$. The following assumption is imposed throughout the paper.
Hypothesis 2.1. $\mathcal{G}_{\mathrm{d}}$ is infinite, locally finite ( $\operatorname{deg}(v)<\infty$ for every $v \in V$ ), connected (for any two vertices $u, v \in V$ there is a path connecting $u$ and $v$ ), and simple (there are no loops or multiple edges).

Next, let us assign each edge $e \in E$ a finite length $|e| \in(0, \infty)$. We can then naturally associate with $\left(\mathcal{G}_{\mathrm{d}},|\cdot|\right)=(V, E,|\cdot|)$ a metric space $\mathcal{G}$ : first, we identify



each edge $e \in E$ with a copy of the interval $I_{e}:=[0,|e|]$. The topological space $\mathbb{G}$ is then obtained by "gluing together" the ends of edges corresponding to the same vertex $v$ (in the sense of a topological quotient, see, e.g., [13, Chapter 3.2.2]). The topology on $\mathbb{G}$ is metrizable by the natural path metric $\varrho$ - the distance between two points $x, y \in \mathbb{G}$ is defined as the arc length of the "shortest path" connecting them (if $x$ or $y$ are not vertices, then we need to allow also paths which start or end in the middle of edges; the length of such paths is naturally defined by taking the corresponding portion of the interval). The metric space $\mathbb{G}$ arising from the above construction is called a metric graph (associated to $\left(\mathbb{G}_{\mathrm{d}},|\cdot|)=(V, E,|\cdot|)\right.$ ).

Notice that, by definition, $(\mathbb{G}, \varrho)$ is a length space (see [13, Chapter 2.1] for definitions and further details). Moreover (see, e.g., [40, Chapter 1.1]), a metric graph $\mathbb{G}$ is a Hausdorff topological space with countable base and each $x \in \mathbb{G}$ has a neighborhood isometric to a star-shaped set $S\left(\operatorname{deg}(x), r_{x}\right)$ of degree $\operatorname{deg}(x) \in \mathbb{Z}_{\geq 1}$,

$$
S\left(\operatorname{deg}(x), r_{x}\right):=\left\{z=r e^{2 \pi i k / \operatorname{deg}(x)} \mid r \in\left[0, r_{x}\right), k=1, \ldots, \operatorname{deg}(x)\right\} \subset \mathbb{C}
$$

Notice that $\operatorname{deg}(x)$ in (2.2) coincides with the combinatorial degree if $x$ belongs to the vertex set, and $\operatorname{deg}(x)=2$ for every non-vertex point $x$ of $\mathbb{G}$.

Sometimes, we will consider $\mathbb{G}_{\mathrm{d}}$ as a rooted graph with a fixed root $o \in V$. In this case we denote by $S_{n}, n \in \mathbb{Z}_{\geq 0}$ the $n$-th combinatorial sphere with respect to the order induced by $o$ (notice that $S_{0}=\{o\})$.
2.2. Graph ends. One possible definition of a boundary for an infinite graph is the notion of the so-called graph ends (see $[30,38]$ and $[76, \S 21]$ ).

Definition 2.1. A sequence of distinct vertices $\left(v_{n}\right)_{n \in \mathbb{Z}_{\geq 0}}$ (resp., $\left(v_{n}\right)_{n \in \mathbb{Z}}$ ) such that $v_{n} \sim v_{n+1}$ for all $n \in \mathbb{Z}_{\geq 0}$ (resp., for all $n \in \mathbb{Z}$ ) is called a ray (resp., double ray). A subsequence of such a sequence is called a tail.

Two rays $\mathcal{R}_{1}, \mathcal{R}_{2}$ are called equivalent - and we write $\mathcal{R}_{1} \sim \mathcal{R}_{2}-$ if there is a third ray containing infinitely many vertices of both $\mathcal{R}_{1}$ and $\mathcal{R}_{2} .{ }^{\dagger}$ An equivalence class of rays is called a graph end of $\mathbb{G}_{\mathrm{d}}$ and the set of graph ends will be denoted by $\Omega\left(\mathbb{G}_{\mathrm{d}}\right)$. Moreover, we will write $\mathcal{R} \in \omega$ whenever $\mathcal{R}$ is a ray belonging to the end $\omega \in \Omega\left(\mathbb{G}_{\mathrm{d}}\right)$.

An important feature of graph ends is their relation to topological ends of a metric graph $\mathbb{G}$.

Definition 2.2. Consider sequences $\mathcal{U}=\left(U_{n}\right)_{n=0}^{\infty}$ of non-empty open connected subsets of $\mathbb{G}$ with compact boundaries and such that $\overline{U_{n+1}} \subseteq U_{n}$ for all $n \geq 0$ and $\bigcap_{n \geq 0} \overline{U_{n}}=\varnothing$. Two such sequences $\mathcal{U}$ and $\mathcal{U}^{\prime}$ are called equivalent if for all $n \geq 0$ there exist $j$ and $k$ such that $\overline{U_{n}} \supseteq U_{j}^{\prime}$ and $U_{n}^{\prime} \supseteq U_{k}$. An equivalence class $\gamma$ of sequences is called a topological end of $\mathbb{G}$ and $C(\mathbb{G})$ denotes the set of topological ends of $\mathbb{G}$.

For locally finite graphs, there is a bijection between topological ends of a metric graph $\mathbb{C}(\mathbb{G})$ and graph ends $\Omega\left(\mathbb{G}_{\mathrm{d}}\right)$ of the underlying combinatorial graph $\mathbb{G}_{\mathrm{d}}$ (see $[76$, $\S 21],[23, \S 8.6$ and also p.277-278]; for the case of graphs which are not locally finite see $[18,24])$.

[^0]
[^0]:    ${ }^{\dagger}$ Equivalently, $\mathcal{R}_{1} \sim \mathcal{R}_{2}$ if and only if $\mathcal{R}_{1}$ and $\mathcal{R}_{2}$ cannot be separated by a finite vertex set, i.e., for every finite subset $X \subset V$ the remaining tails of $\mathcal{R}_{1}$ and $\mathcal{R}_{2}$ in $V \backslash X$ belong to the same connected component of $V \backslash X$.



Theorem 2.3. For every topological end $\gamma \in \mathcal{C}(G)$ of a locally finite metric graph $G=\left(G_{d},|\cdot|\right)$ there exists a unique graph end $\omega_{\gamma} \in \Omega\left(G_{d}\right)$ such that for every sequence $\mathbf{U}$ representing $\gamma$, each $U_{n}$ contains a ray from $\omega_{\gamma}$. Moreover, the map $\gamma \mapsto \omega_{\gamma}$ is a bijection between $\mathcal{C}(G)$ and $\Omega\left(G_{d}\right)$.

Therefore, we may identify topological ends of a metric graph $G$ and graph ends of the underlying graph $G_{d}$. We will simply speak of the ends of $G$. One obvious advantage of this identification is the fact that the definition of $\Omega\left(G_{d}\right)$ is purely combinatorial and does not depend on edge lengths.
Definition 2.4. An end $\omega$ of a graph $G_{d}$ is called free if there is a finite set $X$ of vertices which separates $\omega$ from all other ends of the graph (i.e. the rays of all ends $\omega^{\prime} \neq \omega$ end up in different connected components of $V \backslash X$ than the rays of $\omega$ ).

Remark 2.5. Let us mention several examples.
(i) $\mathbb{Z}$ has two ends both of which are free.
(ii) $\mathbb{Z}^{N}$ has one end for all $N \geq 2$.
(iii) A $k$-regular tree, $k \geq 3$, has uncountably many ends, none of which is free.
(iv) If $G_{d}$ is a Cayley graph of a finitely generated infinite group $G$, then the number of ends of $G_{d}$ is independent of the generating set and $G_{d}$ has either one, two, or infinitely many ends. Moreover, $G_{d}$ has exactly two ends only if $G$ is virtually infinite cyclic (it has a finite normal subgroup $N$ such that the quotient group $G / N$ is isomorphic either to $\mathbb{Z}$ or $\mathbb{Z}_{2} * \mathbb{Z}_{2}$ ). These results are due to Freudenthal [30] and Hopf [42] (see also [75]). The classification of finitely generated groups with infinitely many ends is due to Stallings [73]. Let us mention that if $G$ has infinitely many ends, then the result of Stallings implies that it contains a non-Abelian free subgroup and hence is nonamenable. For further details we refer to, e.g., [32, Chapter 13].
(v) Let us also mention that by Halin's theorem [38] every locally finite graph $G_{d}$ with infinitely many ends contains at least one end which is not free.

One of the main features of graph ends is that they provide a rather refined way of compactifying graphs (see [29] and [23, §8.6], [76]). Namely, we introduce a topology on $\widehat{G}:=G \cup \mathcal{C}(G)$ as follows. For an open subset $U \subseteq G$, denote its extension $\widehat{U}$ to $\widehat{G}$ by

$$
\widehat{U}:=U \cup\left\{\gamma \in \mathcal{C}(G) \mid \exists \mathbf{U}=\left(U_{n}\right) \in \gamma \text { such that } U_{0} \subset U\right\}
$$

Now we can introduce a neighborhood basis of $\gamma \in \mathcal{C}(G)$ as follows

$$
\{\widehat{U} \mid U \subseteq G \text { is open, } \gamma \in \widehat{U}\}
$$

This turns $\widehat{G}$ into a compact topological space, called the end (or Freudenthal) compactification of $G$.
Remark 2.6. Notice that an end $\gamma \in \mathcal{C}(G)$ is free exactly when $\{\gamma\}$ is open as a subset of $\mathcal{C}(G)$ (here $\mathcal{C}(G)$ carries the induced topology from $\widehat{G}$ ). This is further equivalent to the existence of a connected subgraph $G_{\gamma}$ with compact boundary ${ }^{\dagger}$ $\partial G_{\gamma}$ such that $U_{n} \subseteq G_{\gamma}$ eventually for any sequence $\mathbf{U}=\left(U_{n}\right)$ representing $\gamma$ and $U_{n}^{\prime} \cap G_{\gamma}=\emptyset$ eventually for all sequences $\mathbf{U}^{\prime}=\left(U_{n}^{\prime}\right)$ representing an end $\gamma^{\prime} \neq \gamma$.

[^0]
[^0]:    ${ }^{\dagger}$ Notice that for a subgraph $\widetilde{G}$ of $G$ its boundary is $\partial \widetilde{G}=\left\{v \in V(\widetilde{G}) \mid \operatorname{deg}_{\widetilde{G}}(v)<\operatorname{deg}_{G}(v)\right\}$ and hence $\partial \widetilde{G}$ is compact only if $\# \partial \widetilde{G}<\infty$.



Let us mention that topological ends can be obtained in a constructive way by means of compact exhaustions. Namely, a sequence of connected subgraphs $\left(F_{n}\right)$ of $G$ such that each $F_{n}$ has finitely many vertices and edges, $F_{n} \subseteq F_{n+1}$ for all $n \geq 0$ and $\bigcup_{n} F_{n}=G$ is called a compact exhaustion of $G$. Clearly, each $F_{n}$ may be identified with a compact subset of $G$. Now iteratively construct a sequence $\left(U_{n}\right)$ by choosing in each step a non-compact, connected component $U_{n}$ of $G \backslash F_{n}$ satisfying $U_{n} \subseteq U_{n-1}$. It is easy to check that each such sequence $\left(U_{n}\right)$ defines a topological end $\gamma \in C(G)$ and in fact all ends $\gamma \in C(G)$ are obtained by this construction. Notice also that the open subsets $U_{n}$ of such representations $\gamma \sim\left(U_{n}\right)$ (actually, their topological closures, since we need to add endpoints of edges which also belong to $\left.V\left(F_{n}\right)\right)$ can again be identified with connected subgraphs $G_{n}(\gamma):=\bar{U}_{n}$ and we will frequently use this fact.

Let us finish this section with a few more notations. Suppose $R$ is a ray or a finite path without self-intersections in $\mathbb{G}_{d}$. We may identify $R$ with a subgraph of $\mathbb{G}_{d}$ and hence with a subset of $G$, i.e., we can consider it as the union of all edges of $R$. The latter can further be identified with the interval $I_{R}:=[0,|R|)$ of length $|R|$, where

$$
|R|:=\sum_{e \in R}|e|
$$

Also, we need to consider paths - and in particular rays - in $G$ starting or ending at a non-vertex point. In particular, given a path $\left(v_{0}, v_{1}, \ldots, v_{N}\right)$ and a point $x$ in the interior of some edge $e$ attached to $v_{0}, e \neq e_{v_{0}, v_{1}}$, we add the interval $\left[x, v_{0}\right] \subseteq e$ to $\left(v_{0}, v_{1}, \ldots, v_{N}\right)$. For the resulting set, we shall write $\left(x, v_{0}, v_{1}, \ldots, v_{N}\right)$ and call it a non-vertex path; and likewise for rays. The set of all non-vertex rays will be denoted by $\mathcal{R}(G)$.
2.3. Kirchhoff Laplacian. Let $G$ be a metric graph satisfying Hypothesis 2.1. Upon identifying every $e \in \mathcal{E}$ with a copy of the interval $I_{e}=[0,|e|]$, we denote by

$$
L^{2}(e):=L^{2}\left(I_{e} ; d x_{e}\right)
$$

the $L^{2}$-space for the (unweighted) Lebesgue measure $d x_{e}$ on $I_{e}$ and introduce the Hilbert space $L^{2}(G)$ of functions $f: G \rightarrow \mathbb{C}$ such that

$$
L^{2}(G):=\bigoplus_{e \in \mathcal{E}} L^{2}(e)=\left\{f=\left\{f_{e}\right\}_{e \in \mathcal{E}} \mid f_{e} \in L^{2}(e), \quad \sum_{e \in \mathcal{E}}\left\|f_{e}\right\|_{L^{2}(e)}^{2}<\infty\right\}
$$

The subspace of compactly supported $L^{2}(G)$ functions will be denoted by

$$
L_{c}^{2}(G):=\left\{f \in L^{2}(G) \mid f \neq 0 \text { only on finitely many edges } e \in \mathcal{E}\right\}
$$

For every $e \in \mathcal{E}$ consider the maximal operator $H_{e, \text { max }}$ acting on functions $f \in H^{2}(e)$ as a negative second derivative. Here and below $H^{s}(e)$ for $s \geq 0$ denotes the usual Sobolev space on $e$ (see, e.g., [12, Chapter 8]). In particular, $H^{0}(e)=L^{2}(e)$ and

$$
H^{1}(e)=\left\{f \in A C(e) \mid f^{\prime} \in L^{2}(e)\right\}, \quad H^{2}(e)=\left\{f \in H^{1}(e) \mid f^{\prime} \in H^{1}(e)\right\}
$$

This defines the maximal operator on $L^{2}(G)$ by

$$
H_{\max }:=\bigoplus_{e \in \mathcal{E}} H_{e, \max }, \quad H_{e, \max }=-\frac{d^{2}}{d x_{e}^{2}}, \quad \operatorname{dom}\left(H_{e, \max }\right)=H^{2}(e)
$$



If $v$ is a vertex of the edge $e \in \mathcal{E}$, then for every $f \in \mathrm{H}^{2}(e)$ the following quantities

$$
f_{e}(v):=\lim _{x_{e} \rightarrow v} f\left(x_{e}\right), \quad f_{e}^{\prime}(v):=\lim _{x_{e} \rightarrow v} \frac{f\left(x_{e}\right)-f(v)}{\left|x_{e}-v\right|}
$$

are well defined. Considering $\mathcal{G}$ as the union of all edges glued together at certain endpoints, let us equip a metric graph with the Laplace operator. The Kirchhoff (also called standard or Kirchhoff-Neumann) boundary conditions at every vertex $v \in \mathcal{V}$ are then given by

$$
\left\{\begin{array}{l}
f \text { is continuous at } v \\
\sum_{e \in \mathcal{E}_{v}} f_{e}^{\prime}(v)=0
\end{array}\right.
$$

Imposing these boundary conditions on the maximal domain $\operatorname{dom}\left(H_{\max }\right)$ yields the maximal KirchhoffLaplacian

$$
H:=H_{\max } \upharpoonright \operatorname{dom}(H), \quad \operatorname{dom}(H)=\left\{f \in \operatorname{dom}\left(H_{\max }\right) \mid f \text { satisfies (2.7) for any } v \in \mathcal{V}\right\}
$$

Restricting further to compactly supported functions we end up with the preminimal operator

$$
\begin{aligned}
& H_{0}^{0}:=H_{\max } \upharpoonright \operatorname{dom}\left(H_{0}^{0}\right) \\
& \quad \operatorname{dom}\left(H_{0}^{0}\right)=\left\{f \in \operatorname{dom}\left(H_{\max }\right) \cap \mathrm{L}_{c}^{2}(\mathcal{G}) \mid f \text { satisfies (2.7) for any } v \in \mathcal{V}\right\} .
\end{aligned}
$$

Integrating by parts one obtains

$$
\left\langle H_{0}^{0} f, f\right\rangle_{\mathrm{L}^{2}(\mathcal{G})}=\int_{\mathcal{G}}\left|f^{\prime}(x)\right|^{2} d x, \quad f \in \operatorname{dom}\left(H_{0}^{0}\right)
$$

and hence $H_{0}^{0}$ is a non-negative symmetric operator. We call its closure $H_{0}:=\overline{H_{0}^{0}}$ in $\mathrm{L}^{2}(\mathcal{G})$ the minimal KirchhoffLaplacian. The following result is well-known (see, e.g., $[16$, Lemma 3.9]).

Lemma 2.7. Let $\mathcal{G}$ be a metric graph. Then

$$
H_{0}^{*}=H
$$

2.4. Deficiency indices. In the following we are interested in the question whether $H_{0}$ is self-adjoint, or equivalently whether the equality $H_{0}=H$ holds true. Let us recall one sufficient condition. Define the star weight $m(v)$ of a vertex $v \in \mathcal{V}$ by

$$
m(v):=\sum_{e \in \mathcal{E}_{v}}|e|=\operatorname{vol}\left(\mathcal{E}_{v}\right)
$$

and also introduce the star path metric on $\mathcal{V}$ by

$$
\varrho_{m}(u, v):=\inf _{\mathcal{P}=\left(v_{0}, \ldots, v_{n}\right)} \sum_{v_{k} \in \mathcal{P}} m\left(v_{k}\right)
$$

Theorem 2.8 ([27]). If $\left(\mathcal{V}, \varrho_{m}\right)$ is complete as a metric space, then $H_{0}^{0}$ is essentially self-adjoint and $H_{0}^{0}=H_{0}=H$.

If a symmetric operator is not (essentially) self-adjoint, then the degree of its nonself-adjointness is determined by its deficiency indices. Recall that the deficiency subspace $\mathcal{N}_{z}\left(H_{0}\right)$ of $H_{0}$ is defined by

$$
\mathcal{N}_{z}\left(H_{0}\right):=\operatorname{ker}\left(H_{0}^{*}-z\right)=\operatorname{ker}(H-z), \quad z \in \mathbb{C}
$$



The numbers

$$
n_{ \pm}\left(H_{0}\right):=\operatorname{dim} N_{ \pm i}\left(H_{0}\right)=\operatorname{dim} \operatorname{ker}(H \mp i)
$$

are called the deficiency indices of $H_{0}$. Notice that $n_{+}\left(H_{0}\right)=n_{-}\left(H_{0}\right)$ since $H_{0}$ is non-negative. Moreover, $H_{0}$ is self-adjoint exactly when $n_{+}\left(H_{0}\right)=n_{-}\left(H_{0}\right)=0$.

Lemma 2.9. If 0 is a point of regular type for $H_{0}$, then ${ }^{\dagger}$

$$
n_{ \pm}\left(H_{0}\right)=\operatorname{dim} \operatorname{ker}(H)
$$

Proof. The claim immediately follows from $[1, \S 78]$ or $[69$, Prop. 3.3]. Indeed, the set of regular points of $H_{0}$ is an open subset of $\mathbb{C}$. Moreover, by the KrasnoselskiiKrein theorem (see, e.g., $[1, \S 78]$ or $[69$, Prop. 2.4]), $\operatorname{dim} \mathcal{N}_{z}\left(H_{0}\right)$ is constant on each connected component of the set of regular type points of $H_{0}$. Since $H_{0}$ is symmetric, each $z \in \mathbb{C} \backslash \mathbb{R}$ is a point of regular type for $H_{0}$. Therefore, if 0 is a point of regular type for $H_{0}$, we immediately get

$$
\operatorname{dim} \operatorname{ker}(H)=\operatorname{dim} \mathcal{N}_{0}\left(H_{0}\right)=n_{+}\left(H_{0}\right)=n_{-}\left(H_{0}\right)
$$

Using the Rayleigh quotient, define

$$
\lambda_{0}(\mathcal{G}):=\inf _{\substack{f \in \operatorname{dom}\left(H_{0}\right) \\\|f\|=1}}\left\langle H_{0} f, f\right\rangle_{L^{2}(\mathcal{G})}=\inf _{\substack{f \in \operatorname{dom}\left(H_{0}\right) \\\|f\|=1}} \int_{\mathcal{G}}\left|f^{\prime}\right|^{2} d x
$$

Noting that the operator $H_{0}$ is non-negative, 0 is a point of regular type for $H_{0}$ if $\lambda_{0}(\mathcal{G})>0$. Thus, we arrive at the following result.

Corollary 2.10. If $\lambda_{0}(\mathcal{G})>0$, then (2.16) holds true.
The positivity of $\lambda_{0}(\mathcal{G})$ is known in the following simple situation.
Corollary 2.11. If $\mathcal{G}$ has finite total volume,

$$
\operatorname{vol}(\mathcal{G}):=\sum_{e \in \mathcal{E}}|e|<\infty
$$

then $H_{0}$ is not self-adjoint and (2.16) holds true.
Proof. Indeed, by the Cheeger-type estimate [55, Corollary 3.5(iv)], we have

$$
\lambda_{0}(\mathcal{G}) \geq \frac{1}{4 \operatorname{vol}(\mathcal{G})^{2}}>0
$$

and hence (2.16) holds true by Corollary 2.10. Moreover, $\mathbf{1}_{\mathcal{G}} \in \operatorname{ker}(H)$, where $\mathbf{1}_{\mathcal{G}}$ denotes the constant function on $\mathcal{G}$, and hence

$$
n_{ \pm}\left(H_{0}\right)=\operatorname{dim}(\operatorname{ker} H) \geq 1
$$

It remains to notice that $H_{0}$ is self-adjoint exactly when $n_{ \pm}\left(H_{0}\right)=0$.
Remark 2.12. By [55, Theorem 3.4], $\lambda_{0}(\mathcal{G})>0$ holds true if the isoperimetric constant $\alpha(\mathcal{G})$ of the metric graph $\mathcal{G}$ is positive. For antitrees, the isoperimetric constant is tightly related to the structure of its combinatorial spheres (see [56, Theorem 7.1]). If $\mathcal{G}^{d}$ is the edge graph of a tessellation of $\mathbb{R}^{2}$, then positivity of $\alpha(\mathcal{G})$ can be deduced from certain curvature-type quantities [65].

On the other hand, by [55, Corollary 4.5(i)], $\lambda_{0}(\mathcal{G})>0$ holds true if the combinatorial isoperimetric constant of $\mathcal{G}^{d}$ is positive and $\ell^{*}(\mathcal{G}):=\sup _{e \in \mathcal{E}}|e|<\infty$. For

[^0]
[^0]:    ${ }^{\dagger}$ For an operator $T$ with dense domain in a Hilbert space $\mathcal{H}, \lambda \in \mathbb{C}$ is called a point of regular type of $T$ if there exists $c=c_{\lambda}>0$ such that $\|(T-\lambda) f\| \geq c\|f\|$ for all $f \in \operatorname{dom}(T)$.



example, this holds true if $\mathcal{G}_{d}$ is an infinite tree without leaves [55, Lemma 8.1] or if $\mathcal{G}_{d}$ is a Cayley graph of a non-amenable finitely generated group [55, Lemma 8.12(i)].

Finally, let us remark that $\operatorname{ker}(\mathcal{H})=\mathcal{H}(\mathcal{G}) \cap L^{2}(\mathcal{G})$, where $\mathcal{H}(\mathcal{G})$ denotes the space of harmonic functions on $\mathcal{G}$, that is, the set of all "edgewise" affine functions satisfying Kirchhoff conditions (2.7) at each vertex $v \in \mathcal{V}$. Notice that every function $f \in \mathcal{H}(\mathcal{G})$ is uniquely determined by its vertex values $f:=\left.f\right|_{\mathcal{V}}=(f(v))_{v \in \mathcal{V}}$. Recall also the following result (see, e.g., [55, eq. (2.32)]).
Lemma 2.13. Let $\mathcal{G}$ be a metric graph satisfying the assumptions in Hypothesis 2.1. If $f \in \mathcal{H}(\mathcal{G})$, then $f \in L^{2}(\mathcal{G})$ if and only if $f \in \ell^{2}(\mathcal{V} ; m)$, that is,

$$
\sum_{v \in \mathcal{V}}|f(v)|^{2} m(v)<\infty
$$

Remark 2.14. The above considerations indicate that in order to understand the deficiency indices of the Kirchhoff Laplacian one needs to find the dimension of the space of $L^{2}$ harmonic (or, more carefully, $\lambda$-harmonic) functions. Moreover, in order to describe self-adjoint extensions one has to understand the behavior of $L^{2}$ harmonic functions at "infinity", that is, near a "boundary" of a given metric graph. However, graphs admit a lot of different notions of boundary (ends, Poisson and Martin boundaries, Royden and Kuramochi boundary etc.) and search for a suitable notion in this context (namely, $L^{2}$ harmonic functions) is a highly nontrivial problem, which seems to be not very well studied neither in the context of incomplete manifolds nor in the case of weighted graphs.

Let us also mention that recently there has been a tremendous amount of work devoted to the study of harmonic functions and self-adjoint extensions of Laplacians on weighted graph (we only refer to a brief selection of articles $[19,35,39,43,44$, $45,46,51])$.

# 3. GRAPH ENDS AND $\mathcal{H}^{1}(\mathcal{G})$ 

This section deals with the Sobolev space $\mathcal{H}^{1}$ on metric graphs. Its importance stems, in particular, from the fact that it serves as a form domain for a large class of self-adjoint extensions of $\mathcal{H}_{0}$.
3.1. $\mathcal{H}^{1}(\mathcal{G})$ and boundary values. First recall that

$$
\mathcal{H}^{1}(\mathcal{G})=\left\{f \in L^{2}(\mathcal{G}) \cap \mathcal{C}(\mathcal{G}) \mid f_{e} \in H^{1}(e) \text { for all } e \in \mathcal{E},\left\|f^{\prime}\right\|_{L^{2}(\mathcal{G})}^{2}<\infty\right\}
$$

where $\mathcal{C}(\mathcal{G})$ is the space of continuous complex-valued functions on $\mathcal{G}$ and

$$
\left\|f^{\prime}\right\|_{L^{2}(\mathcal{G})}^{2}:=\sum_{e \in \mathcal{E}}\left\|f_{e}^{\prime}\right\|_{L^{2}(e)}^{2}
$$

Notice that $\left(\mathcal{H}^{1}(\mathcal{G}),\|\cdot\|_{\mathcal{H}^{1}}\right)$ is a Hilbert space when equipped with the standard norm

$$
\|f\|_{\mathcal{H}^{1}(\mathcal{G})}^{2}:=\|f\|_{L^{2}(\mathcal{G})}^{2}+\left\|f^{\prime}\right\|_{L^{2}(\mathcal{G})}^{2}=\sum_{e \in \mathcal{E}}\left\|f_{e}\right\|_{H^{1}(e)}^{2}, \quad f \in \mathcal{H}^{1}(\mathcal{G})
$$

Moreover, $\operatorname{dom}\left(\mathcal{H}_{0}^{0}\right) \subset \mathcal{H}^{1}(\mathcal{G})$ and we define $\mathcal{H}_{0}^{1}(\mathcal{G})$ as the closure of $\operatorname{dom}\left(\mathcal{H}_{0}^{0}\right)$ with respect to $\|\cdot\|_{\mathcal{H}^{1}(\mathcal{G})}$.



Remark 3.1. If $H_{0}^{0}$ is essentially self-adjoint, then $\mathcal{H}^{1}(G)=H_{0}^{1}(G)$. However, the converse is not true in general. In fact this equality is tightly connected to the uniqueness of Markovian extensions of $H_{0}$ and, as we shall see, it is possible to characterize it in terms of topological ends of $G$ (see Corollary 5.5 below).

Notice also that $H_{0}^{1}(G)$ is the form domain of the Friedrichs extension $H_{F}$ of $H_{0}^{0}$ and $\lambda_{0}(G)$ defined by (2.17) is the bottom of the spectrum of $H_{F}$.

By definition, $\mathcal{H}^{1}(G)$ is densely and continuously embedded in $L^{2}(G)$.
Lemma 3.2. $\mathcal{H}^{1}(G)$ is continuously embedded in $C_{b}(G)=C(G) \cap L^{\infty}(G)$ and

$$
\|f\|_{\infty}:=\sup _{x \in G}|f(x)| \leq C_{G}\|f\|_{\mathcal{H}^{1}(G)}
$$

holds for all $f \in \mathcal{H}^{1}(G)$ with $C_{G}:=\sqrt{\operatorname{coth}\left(\frac{1}{2} \sup _{\mathfrak{R}}|\mathfrak{R}|\right)}$, where the supremum is taken over all non-vertex paths without self-intersections.

Proof. For every interval $I \subseteq \mathbb{R}$ the embedding of $H^{1}(I)$ into $L^{\infty}(I)$ is bounded and

$$
\sup _{x \in I}|f(x)| \leq C_{|I|}\|f\|_{H^{1}(I)}
$$

holds for all $f \in H^{1}(I)$ with $C_{|I|}=\sqrt{\operatorname{coth}(|I|)}$ (see [60]). Notice that we may identify the restriction $\left.f\right|_{\mathfrak{R}}$ of $f \in \mathcal{H}^{1}(G)$ to a (non-vertex) path without selfintersections $\mathfrak{R}$ with a function on $\mathbb{I}_{\mathfrak{R}}=[0,|\mathfrak{R}|)$. It is easy to check that upon this identification $\left.f\right|_{\mathfrak{R}} \in H^{1}\left(\mathbb{I}_{\mathfrak{R}}\right)$ and $\left(\left.f\right|_{\mathfrak{R}}\right)^{\prime}=\left.f^{\prime}\right|_{\mathfrak{R}}$.

Suppose now that $\mathfrak{R}$ is a fixed non-vertex path without self-intersections in $G$. Then for every $x \in G$, connecting $x$ and $\mathfrak{R}$ by some finite non-vertex path $\mathfrak{R}_{0}$, we see that there exists a non-vertex path without self-intersections $\mathfrak{R}_{x}$ such that $x \in \mathfrak{R}_{x}$ and $\left|\mathfrak{R}_{x}\right| \geq|\mathfrak{R}| / 2$ (if $x$ lies on $\mathfrak{R}$ already, then the connecting argument is superfluous and we can simply take a portion of $\mathfrak{R}$ ). Applying (3.3) to $\mathfrak{R}_{x}$, we easily deduce the estimate (3.2).

Remark 3.3. The diameter of $G$ (as a metric space $(G, \varrho)$ ) is defined by

$$
\operatorname{diam}(G):=\sup _{x, y \in G} \varrho(x, y)
$$

Therefore, $\operatorname{diam}(G) \leq \sup _{\mathfrak{R}}|\mathfrak{R}|$ and hence $C_{G} \leq \sqrt{\operatorname{coth}\left(\frac{1}{2} \operatorname{diam}(G)\right)}$.
The above considerations, in particular, imply the following crucial property of $\mathcal{H}^{1}$-functions: if $\mathfrak{R}=\left(v_{n}\right)$ is a ray, then

$$
f\left(\gamma_{\mathfrak{R}}\right):=\lim _{n \rightarrow \infty} f\left(v_{n}\right)
$$

exists. Indeed, upon the identification of $\mathfrak{R}$ with the interval $\mathbb{I}_{\mathfrak{R}}=[0,|\mathfrak{R}|)$, the latter is an immediate corollary of the description of a Sobolev space $H^{1}$ in one dimension - for a bounded interval this follows from [12, Theorem 8.2] and in the unbounded case see [12, Corollary 8.9]. Moreover, this limit only depends on the equivalence class of $\mathfrak{R}$ (indeed, for any two equivalent rays $\mathfrak{R}$ and $\mathfrak{R}^{\prime}$ there exists a third ray $\mathfrak{R}^{\prime \prime}$ containing infinitely many vertices of both $\mathfrak{R}$ and $\mathfrak{R}^{\prime}$, which immediately implies that $f\left(\gamma_{\mathfrak{R}}\right)=f\left(\gamma_{\mathfrak{R}^{\prime \prime}}\right)=f\left(\gamma_{\mathfrak{R}^{\prime}}\right)$ ). This enables us to introduce the following notion.



Definition 3.4. For every $f \in H^{1}(\mathbb{G})$ and a (topological) end $\gamma \in \mathcal{C}(\mathbb{G})$, we define

$$
f(\gamma):=f\left(\gamma_{R}\right),
$$

where $R \in \omega_{\gamma}$ is any ray belonging to the corresponding graph end $\omega_{\gamma}$ (see Theorem 2.3). Sometimes we shall also write $f\left(\omega_{\gamma}\right):=f(\gamma)$.

It turns out that (3.5) enables us to obtain an extension by continuity of every function $f \in H^{1}(\mathbb{G})$ to the end compactification $\widehat{\mathbb{G}}$ of $\mathbb{G}$ (see Section 2.2).

Lemma 3.5. Let $\mathbb{G}$ be a metric graph and $\gamma \in \mathcal{C}(\mathbb{G})$. If $f \in H^{1}(\mathbb{G})$, then

$$
\lim _{n \rightarrow \infty} \sup _{x \in \mathcal{U}_{n}}|f(x)-f(\gamma)|=0
$$

for every sequence $\mathcal{U}=\left(U_{n}\right)$ representing $\gamma$.
Proof. Let $\gamma \in \mathcal{C}(\mathbb{G})$ and let $\mathcal{U}=\left(U_{n}\right)$ be a sequence representing $\gamma$. Let also

$$
\mathcal{R}_{n}(\gamma):=\left\{R \in \mathcal{R}(\mathbb{G}) \mid R \subseteq U_{n}\right\}
$$

be the set of all non-vertex rays contained in $U_{n}, n \geq 0$.
We proceed by case distinction. First, assume that for $n$ sufficiently large, all rays in $\mathcal{R}_{n}(\gamma)$ have length at most one. If $x \in U_{n}$, then there exists a (non-vertex) ray $R_{x} \in \mathcal{R}_{n}(\gamma)$ such that $R_{x}=\left(x, v_{0}, \ldots\right)$ and its tail $R:=\left(v_{0}, v_{1}, \ldots\right)$ (see Definition 2.1) belong to $\omega_{\gamma}$. By our assumption, $\left|R_{x}\right| \leq 1$ and hence

$$
|f(\gamma)-f(x)|=\left|f\left(\gamma_{R_{x}}\right)-f(x)\right|=\left|\int_{R_{x}} f^{\prime}(y) \mathrm{d} y\right| \leq\left\|f^{\prime}\right\|_{L^{2}\left(R_{x}\right)} \leq\left\|f^{\prime}\right\|_{L^{2}\left(U_{n}\right)}
$$

Since $x \in U_{n}$ is arbitrary, this implies

$$
\sup _{x \in \mathcal{U}_{n}}|f(\gamma)-f(x)| \leq\left\|f^{\prime}\right\|_{L^{2}\left(U_{n}\right)}
$$

Since $\mathcal{U}=\left(U_{n}\right)$ represents $\gamma, \bigcap_{n} U_{n}=\varnothing$ and hence $\lim _{n \rightarrow \infty}\left\|f^{\prime}\right\|_{L^{2}\left(U_{n}\right)}=0$. This implies (3.6).

Assume now that for every $n \in \mathbb{Z}_{\geq 0}$ there is a ray $R \in \mathcal{R}_{n}(\gamma)$ with $|R|>1$. Take $n \geq 0$ and choose an $x \in U_{n}$. We can find a finite (non-vertex) path without self-intersections $R_{x} \subseteq U_{n}$ such that $x \in R_{x}$ and $\left|R_{x}\right|=1 / 2$ (take into account that $U_{n}$ contains at least one ray of length greater than 1). Hence we get

$$
|f(x)| \leq \sup _{y \in R_{x}}|f(y)| \leq C_{1 / 2}\|f\|_{H^{1}\left(R_{x}\right)} \leq C_{1 / 2}\|f\|_{H^{1}\left(U_{n}\right)}
$$

where $C_{1 / 2}=\sqrt{\operatorname{coth}(1 / 2)}$ is the constant from (3.3). Since $x \in U_{n}$ is arbitrary,

$$
\sup _{x \in \mathcal{U}_{n}}|f(x)| \leq C_{1 / 2}\|f\|_{H^{1}\left(U_{n}\right)}
$$

However, $\bigcap_{n} U_{n}=\varnothing$ and hence $\sup _{x \in U_{n}}|f(x)|=o(1)$ as $n \rightarrow \infty$. It remains to notice that $f(\gamma)=0$. Indeed, by Theorem 2.3, for every $n \geq 0$ there is a ray $\widetilde{R}_{n} \in \omega_{\gamma}$ such that $\widetilde{R}_{n} \subseteq U_{n}$ and hence

$$
|f(\gamma)|=\left|f\left(\gamma_{\widetilde{R}_{n}}\right)\right| \leq \sup _{x \in \mathcal{U}_{n}}|f(x)|=o(1)
$$

as $n \rightarrow \infty$. This finishes the proof.
Taking into account the topology on $\widehat{\mathbb{G}}=\mathbb{G} \cup \mathcal{C}(\mathbb{G})$, the next result is a direct consequence of Lemma 3.2 and Lemma 3.5.



Proposition 3.6. Each $f \in H^{1}(G)$ has a unique continuous extension to the end compactification $\widehat{G}$ of $G$ and this extension is given by (3.5). Moreover,

$$
\|f\|_{\infty}=\sup _{x \in \widehat{G}}|f(x)| \leq C_{G}\|f\|_{H^{1}(G)}
$$

3.2. Nontrivial and finite volume ends. Observe that some ends lead to trivial boundary values for $H^{1}$ functions. For example, $f(\gamma)=0$ for all $f \in H^{1}(G)$ if $\omega_{\gamma} \in \Omega\left(\mathbb{G}_{d}\right)$ contains a ray $R$ with infinite length $|R|=\infty$. On the other hand, it might happen that all rays have finite length, however, $f(\gamma)=0$ for all $f \in H^{1}(G)$ (see, e.g., the second step in the proof of Lemma 3.5).
Definition 3.7. A topological end $\gamma \in \mathcal{C}(G)$ is called nontrivial if $f(\gamma) \neq 0$ for some $f \in H^{1}(G)$.

We also need the following notion.
Definition 3.8. A topological end $\gamma \in \mathcal{C}(G)$ has finite volume (or, more precisely, finite volume neighborhood) if there is a sequence $\mathcal{U}=\left(U_{n}\right)$ representing $\gamma$ such that $\operatorname{vol}\left(U_{n}\right)<\infty$ for some $n$. Otherwise $\gamma$ has infinite volume. The set of all finite volume ends is denoted by $\mathcal{C}_{0}(G)$. Here and below, $\operatorname{vol}(A)$ is the Lebesgue measure of a measurable set $A \subseteq G$.
Remark 3.9. If $\mathcal{C}(G)$ contains only one end, then this end has finite volume exactly when $\operatorname{vol}(G)<\infty$. Analogously, if $\gamma \in \mathcal{C}(G)$ is a free end, then there is a finite set of vertices $X$ separating $\omega_{\gamma}$ from all other ends and hence this end has finite volume exactly when the corresponding connected component $G_{\gamma}$ has finite total volume.

If $\gamma$ is not free, then the situation is more complicated. For example, for a rooted tree $G=T_{o}$ the ends are in one-to-one correspondence with the rays from the root $o$ and hence one may possibly confuse the notion of a finite/infinite volume of an end with the finite/infinite length of the corresponding ray. More specifically, let $\gamma$ be an end of $T_{o}$ and let $R_{\gamma}=\left(o, v_{1}, v_{2}, \ldots\right)$ be the corresponding ray. For each $n \geq 1$, let $T_{n}$ be the subtree of $T_{o}$ having its root at $v_{n}$ and containing all the "descendant" vertices of $v_{n}$. Then by definition $\gamma$ has finite volume (neighborhood) if and only if there is $n \geq 1$ such that the corresponding subtree $T_{n}$ has finite total volume. In particular, this implies that $G$ would have uncountably many finite volume ends in this case (here we assume for simplicity that all vertices are essential, that is, $\operatorname{deg}(v)>2$ for all $v \in V)$. In particular, $\left|R_{\gamma}\right|<\infty$ is a necessary but not sufficient condition for $\gamma$ to have finite volume.

It turns out that nontrivial and finite volume ends are closely connected.
Theorem 3.10. Let $G$ be a metric graph. Then $\gamma \in \mathcal{C}(G)$ is nontrivial if and only if $\gamma$ has finite volume. Moreover, for any finite collection of distinct nontrivial ends $\left\{\gamma_{j}\right\}_{j=1}^{N}$ there exists $f \in H^{1}(G) \cap \operatorname{dom}(H)$ such that $f\left(\gamma_{1}\right)=1$ and $f\left(\gamma_{2}\right)=\cdots=$ $f\left(\gamma_{N}\right)=0$.

Proof. It is not difficult to see that $f(\gamma)=0$ for all $f \in H^{1}(G)$ if $\gamma$ has infinite volume. Indeed, assuming that there is $f \in H^{1}(G)$ such that $f(\gamma) \neq 0$, Lemma 3.5 would imply that there exists $\mathcal{U}=\left(U_{n}\right)$ representing $\gamma$ such that

$$
|f(x)| \geq|f(\gamma)| / 2>0
$$

for all $x \in U_{N}$ and some $N \in \mathbb{Z}_{\geq 0}$. However, since $\operatorname{vol}\left(U_{N}\right)=\infty$, we conclude that $f$ is not in $L^{2}(G)$ and this gives a contradiction.



Suppose now that $\gamma \in C(G)$ has finite volume. Take a sequence $\mathcal{U}=\left(U_{n}\right)$ representing $\gamma$ with $\operatorname{vol}\left(U_{0}\right)<\infty$. Pick a function $\varphi \in H^{2}(0,1)$ such that $\varphi(0)=\varphi^{\prime}(0)=$ $\varphi^{\prime}(1)=0$ and $\varphi(1)=1$ and then define $f: G \rightarrow \mathbb{C}$ by

$$
f\left(x_{e}\right)= \begin{cases}1, & x_{e} \in e \text { and both vertices of } e \text { are in } U_{0} \\ 0, & x_{e} \in e \text { and both vertices of } e \text { are not in } U_{0} \\ \varphi\left(\frac{\left|x_{e}-u\right|}{|e|}\right), & x_{e} \in e=e_{u, v} \text { and } u \in \mathcal{V} \backslash U_{0}, v \in U_{0}\end{cases}
$$

Clearly, $f \in H^{2}(e)$ for every $e \in E$. Moreover, it is straightforward to check that $f$ satisfies Kirchhoff conditions (2.7) at every $v \in V$. By assumption, $\partial U_{0}$ is compact and hence it is contained in finitely many edges. Thus there are only finitely many edges $e \in E$ such that one of its vertices belongs to $U_{0}$ and the other one does not belong to $U_{0}$. This implies that $f \in L^{2}(G)$ and, moreover, $f^{\prime} \not \equiv 0$ only on finitely many edges, which proves the inclusion $f \in \operatorname{dom}(H) \cap H^{1}(G)$. Taking into account that $f \equiv 1$ on $U_{n}$ for large enough $n$, we conclude that $f(\gamma)=1$ and hence $\gamma$ is nontrivial.

It remains to prove the second claim. Suppose that $\gamma_{1}, \ldots, \gamma_{N} \in C(G)$ are distinct nontrivial ends. Then we can find $\mathcal{U}_{j}=\left(U_{n}^{j}\right)$, sequences representing $\gamma_{j}$, $j \in\{1, \ldots, N\}$, such that $\operatorname{vol}\left(U_{0}^{1}\right)<\infty$ and $U_{0}^{1} \cap U_{0}^{j}=\emptyset$ for all $j=2, \ldots, N$ (see [29, Satz 3] or [24, Lemma 3.1]). Using the above procedure, we can construct a function $f \in \operatorname{dom}(H) \cap H^{1}(G)$ such that $\operatorname{supp}(f) \subseteq U_{0}$ and $f(\gamma)=1$. The latter also implies that $f\left(\gamma_{2}\right)=\cdots=f\left(\gamma_{N}\right)=0$.

Remark 3.11. If $\operatorname{vol}(G)=\sum_{e \in E}|e|<\infty$, then all ends have finite volume and the end compactification $\widehat{G}$ of $G$ coincides with several other spaces, among them the metric completion of $G$ and the Royden compactification of a related discrete graph (see [35, Corollary 4.22] and also [34, p. 1526]). Notice that the natural path metric $\varrho$ can be extended to $\widehat{G}=G \cup C(G)$ (see [34]). That is, the distance $\varrho(x, \gamma)$ between a point $x \in G$ and an end $\gamma \in C(G)$ is the infimum over all lengths of rays starting at $x$ and belonging to $\gamma$. Similarly, the distance $\varrho\left(\gamma, \gamma^{\prime}\right)$ between two ends is the infimum over the lengths of all double rays with one tail part in $\gamma$ and the other one in $\gamma^{\prime}$. Then $(\widehat{G}, \varrho)$ is a metric completion of $G$ and $\widehat{G}$ is compact and homeomorphic to the end compactification of $G$ (see [34] for further details).

The metric completion was considered in connection with quantum graphs in [16, $17]$; however, it can have a rather complicated structure if $\operatorname{vol}(G)=\infty$ and a further analysis usually requires additional assumptions. Moreover, there are clear indications that metric completion is not a good candidate for these purposes.
3.3. Description of $H_{0}^{1}(G)$. Recall that the space $H_{0}^{1}(G)$ is defined as the closure of $\operatorname{dom}\left(H_{0}^{0}\right) \subset H^{1}(G)$ with respect to $\|\cdot\|_{H^{1}(G)}$. One can naturally conjecture that $H_{0}^{1}(G)$ consists of those $H^{1}$-functions which vanish on $C(G)$. In fact, the results of the previous two sections enable us to show that this is indeed the case.

Theorem 3.12. Let $G$ be a metric graph and $C(G)$ be its ends. Then

$$
H_{0}^{1}(G)=\left\{f \in H^{1}(G) \mid f(\gamma)=0 \text { for all } \gamma \in C(G)\right\}
$$

Proof. First of all, it immediately follows from Proposition 3.6 that $f \in H_{0}^{1}(G)$ vanishes at every end $\gamma \in C(G)$ (since this holds for each $f \in \operatorname{dom}\left(H_{0}^{0}\right)$ ).

To prove the converse inclusion, we will follow the arguments of the proof of [35, Theorem 4.14]. Namely, suppose that $f \in H^{1}(G)$ and $f(\gamma)=0$ for all $\gamma \in C(G)$.



Without loss of generality, we may assume that $f$ is real-valued and $f \geq 0$. To prove that $f \in H_{0}^{1}(G)$, it suffices to construct a sequence of compactly supported functions $f_{n} \in H^{1}(G)$ which converges to $f$ in $H^{1}(G)$. Define $\phi_{n}:[0, \infty) \rightarrow[0, \infty)$ by

$$
\phi_{n}(s):= \begin{cases}s-\frac{1}{n}, & \text { if } s \geq \frac{1}{n} \\ 0, & \text { if } s<\frac{1}{n}\end{cases}
$$

and then let $f_{n}: G \rightarrow[0, \infty)$ be the composition $f_{n}:=\phi_{n} \circ f, n \geq 0$. Since $\phi_{n}(s) \leq s$ for all $s \geq 0$ and $\left|\phi_{n}(s)-\phi_{n}(t)\right| \leq|s-t|$ for all $s, t \geq 0,\left|f_{n}(x)\right| \leq|f(x)|$ and $\left|f_{n}^{\prime}(x)\right| \leq\left|f^{\prime}(x)\right|$ for almost every $x \in G$. Hence $f_{n} \in H^{1}(G)$ and

$$
\left\|f_{n}\right\|_{H^{1}(G)} \leq\|f\|_{H^{1}(G)}
$$

for all $n$. Let us now show that $f_{n}$ has compact support. Indeed, assuming the converse, there exist infinitely many distinct edges $e_{k}$ in $\mathcal{E}$ such that $f_{n}$ is non-zero on each $e_{k}$. Taking into account (3.8), for each $k$ we can find a non-vertex point $x_{k}$ on $e_{k}$ such that $f_{n}\left(x_{k}\right)>\frac{1}{n}$. Since $\widehat{G}$ is compact, the sequence $\left(x_{k}\right)$ has an accumulation point $x \in \widehat{G}$. By construction each edge $e \in \mathcal{E}$ contains at most one of the $x_{k}$ 's. It follows that $x \notin G$ and hence $x \in \widehat{G}$ is an end. On the other hand, $f$ is continuous on $\widehat{G}$ by Proposition 3.6 and thus $f(x) \geq \frac{1}{n}$, which contradicts our assumptions on $f$.

It remains to show that $f_{n}$ converges to $f$ in $H^{1}(G)$ as $n \rightarrow \infty$. Taking into account the above properties of $f_{n}$, we get

$$
\left\|f-f_{n}\right\|_{L^{2}}^{2}+\left\|f^{\prime}-f_{n}^{\prime}\right\|_{L^{2}}^{2} \leq 2\left(\|f\|_{L^{2}}^{2}+\left\|f_{n}\right\|_{L^{2}}^{2}+\left\|f^{\prime}\right\|_{L^{2}}^{2}+\left\|f_{n}^{\prime}\right\|_{L^{2}}^{2}\right) \leq 4\|f\|_{H^{1}}^{2}
$$

and hence by dominated convergence it is enough to show that $f_{n} \rightarrow f$ and $f_{n}^{\prime} \rightarrow f^{\prime}$ pointwise a.e. on $G$. The first claim is clearly true since $\lim _{n \rightarrow \infty} \phi_{n}(s)=s$ for all $s \in[0, \infty)$. To prove the second claim, suppose that $f$ is differentiable at a nonvertex point $x \in G$. If $f(x)>0$, then by continuity of $f$, there is a neighborhood $U$ of $x$ such that $f_{n}=f-\frac{1}{n}$ holds on $U$ for all sufficiently large $n>0$. Hence $f_{n}$ is differentiable at $x$ with $f_{n}^{\prime}(x)=f^{\prime}(x)$ for all large enough $n$. Finally, if $f(x)=0$, then for each $n$ there is a neighborhood $U_{n}$ of $x$ such that $f \leq \frac{1}{n}$ on $U_{n}$. Hence $f_{n} \equiv 0$ on $U_{n}$ and, in particular, $f_{n}$ is differentiable at $x$ with $f_{n}^{\prime}(x)=0$. However, since $f \geq 0$ on $G$ and $f$ is differentiable at $x$, it follows that $f^{\prime}(x)=0$ as well. This finishes the proof.

Combining Theorem 3.12 with Theorem 3.10, we arrive at the following fact.
Corollary 3.13. The equality $H^{1}(G)=H_{0}^{1}(G)$ holds true if and only if all topological ends of $G$ have infinite volume.

Remark 3.14. In the related setting of (weighted) discrete graphs, an important concept is the construction of boundaries by employing $\mathrm{C}^{*}$-algebra techniques (this includes both Royden and Kuramochi boundaries, see $[35,48,53,64,71]$ for further details and references). Finite volume graph ends can also be constructed by using this method. Indeed, $\mathcal{A}:=H^{1}(G) \subset C_{b}(G)$ is a subalgebra by Lemma 3.2 and hence its $\|\cdot\|_{\infty}$-closure $\widetilde{\mathcal{A}}:=\overline{\mathcal{A}}^{\\|\cdot\\|_{\infty}}$ is isomorphic to $\mathrm{C}_{0}(\widetilde{X})$, where $\widetilde{X}$ is the space of characters equipped with the weak*-topology with respect to $\widetilde{\mathcal{A}}$. In general, finding $\widetilde{X}$ for some concrete $\mathrm{C}^{*}$-algebra is a rather complicated task. However, it turns out that in our situation $\widetilde{X}$ coincides with $\widetilde{G}:=G \cup C_{0}(G)$. Indeed, $\widetilde{G}=G \cup C_{0}(G)$



equipped with the induced topology of the end compactification $\widehat{\mathbb{G}}$ is a locally compact Hausdorff space. Proposition 3.6 together with Theorem 3.10 shows that each function $f \in H^{1}(\mathbb{G})$ has a unique continuous extension to $\widetilde{\mathbb{G}}$ and this extension belongs to $C_{0}(\widetilde{\mathbb{G}})$. Moreover, by Theorem 3.10, $H^{1}(\mathbb{G})$ is point-separating and nowhere vanishing on $\widetilde{\mathbb{G}}$ and hence $\widetilde{\mathcal{A}}=C_{0}(\widetilde{\mathbb{G}})$ by the Stone-Weierstrass theorem. Thus the resulting boundary notion is precisely the space of finite volume graph ends.

Let us also mention that $\widetilde{\mathbb{G}}$ is compact only if $\operatorname{vol}(\mathbb{G})<\infty$ and in this case one can show that the Royden compactification of $\mathbb{G}$ as well as its Kuramochi compactification coincide with the end compactification $\widehat{\mathbb{G}}$ (see [35], [48, Theorem 7.11], [49, p.215] and also [41, p.2] for the discrete case).

# 4. DEFICIENCY INDICES 

Intuitively, deficiency indices should be linked to boundary notions for underlying combinatorial graphs. However, spectral properties of the operator $H_{0}$ also depend on the edge lengths and this suggests that it is difficult to expect a purely combinatorial formula for the deficiency indices $n_{ \pm}\left(H_{0}\right)$ of $H_{0}$. Recall that throughout the paper we always assume that $\mathbb{G}$ satisfies Hypothesis 2.1.
4.1. Deficiency indices and graph ends. The main result of this section provides criteria which allow to connect $n_{ \pm}\left(H_{0}\right)$ with the number of graph ends.

Theorem 4.1. Let $\mathbb{G}$ be a metric graph and let $H_{0}$ be the corresponding minimal Kirchhoff Laplacian. Then

$$
n_{ \pm}\left(H_{0}\right) \geq \# \mathcal{C}_{0}(\mathbb{G})
$$

Moreover, the equality

$$
n_{ \pm}\left(H_{0}\right)=\# \mathcal{C}_{0}(\mathbb{G})
$$

holds true if and only if either $\# \mathcal{C}_{0}(\mathbb{G})=\infty$ or $\operatorname{dom}(H) \subset H^{1}(\mathbb{G})$.
Remark 4.2. Since the map

$$
\begin{aligned}
D: & H^{1}(\mathbb{G}) \rightarrow L^{2}(\mathbb{G}) \\
& f \quad \mapsto f^{\prime}
\end{aligned}
$$

is bounded, the inclusion $\operatorname{dom}(H) \subset H^{1}(\mathbb{G})$ holds true if and only if there is a positive constant $C>0$ such that

$$
\left\|f^{\prime}\right\|_{L^{2}(\mathbb{G})}^{2} \leq C\left(\|f\|_{L^{2}(\mathbb{G})}^{2}+\left\|f^{\prime \prime}\right\|_{L^{2}(\mathbb{G})}^{2}\right)
$$

holds for all $f \in \operatorname{dom}(H)$. It can be shown by examples that (4.3) may fail.
Before proving Theorem 4.1, let us first comment on some of its immediate consequences.

Corollary 4.3. If $\mathbb{G}$ is a metric graph with finite total volume $\operatorname{vol}(\mathbb{G})<\infty$, then

$$
n_{ \pm}\left(H_{0}\right) \geq \# \Omega\left(\mathbb{G}_{d}\right)
$$

Moreover,

$$
n_{ \pm}\left(H_{0}\right)=\# \Omega\left(\mathbb{G}_{d}\right)
$$

if and only if either $\mathbb{G}$ contains a non-free end (and hence $\# \Omega\left(\mathbb{G}_{d}\right)=\infty$ in this case) or $\operatorname{ker}(H) \subset H^{1}(\mathbb{G})$.



In fact, we only need to mention that by Halin's theorem [38] (see Remark 2.5(v)) and the finite total volume of $\mathrm{G}, \# \mathcal{C}_{0}(\mathrm{G})=\infty$ only if G contains a non-free end. Recall that for a finitely generated group $\mathcal{G}$, the number of graph ends of a Cayley graph is independent of the generating set (see, e.g., [32]). Combining this fact with the above statement, we obtain the following result.
Corollary 4.4. Let $\mathrm{G}_{d}$ be a Cayley graph of a finitely generated group $\mathcal{G}$ with infinitely many ends. ${ }^{\dagger}$ If $\operatorname{vol}(\mathrm{G})<\infty$, then $n_{ \pm}\left(H_{0}\right)=\infty$.
4.2. Proof of Theorem 4.1. The proof of Theorem 4.1 is based on the following observation. Let $H_{F}$ be the Friedrichs extension of $H_{0}$. Then $\operatorname{dom}(H)$ admits the following decomposition

$$
\operatorname{dom}(H)=\operatorname{dom}\left(H_{F}\right)+\operatorname{ker}(H-z)=\operatorname{dom}\left(H_{F}\right)+N_{z}\left(H_{0}\right)
$$

for every $z$ in the resolvent set $\rho\left(H_{F}\right)$ of $H_{F}$ (see, e.g., [69, Proposition 14.11]). In particular, (4.6) holds for all $z \in\left(-\infty, \lambda_{0}(\mathrm{G})\right)$, where $\lambda_{0}(\mathrm{G}) \geq 0$ is defined by (2.17). Moreover, $\operatorname{dom}\left(H_{F}\right) \subset H_{0}^{1}(\mathrm{G})$ and hence the inclusion $\operatorname{dom}(H) \subset H^{1}(\mathrm{G})$ depends only on the inclusion $\operatorname{ker}(H-z) \subset H^{1}(\mathrm{G})$ for some (and hence for all) $z \in \rho\left(H_{F}\right)$. Let us stress that $N_{0}\left(H_{0}\right)=\operatorname{ker}(H)=\mathcal{H}(\mathrm{G}) \cap L^{2}(\mathrm{G})$ and hence in the case $\lambda_{0}(\mathrm{G})>0$, one is interested in whether all $L^{2}$ harmonic functions belong to $H^{1}(\mathrm{G})$ or not, which is known to depend on the geometry of the underlying metric graph.

We also need the fact that functions in $N_{\lambda}\left(H_{0}\right)$ with $\lambda \in(-\infty, 0)$ can be considered as subharmonic functions and hence they should satisfy a maximum principle. Lemma 4.5. Suppose G is a metric graph and let $\lambda \in(-\infty, 0)$.
(i) If $f \in N_{\lambda}\left(H_{0}\right)=\operatorname{ker}(H-\lambda)$ is real-valued and $f\left(x_{0}\right)>0$ for some $x_{0} \in \mathrm{G}$, then

$$
\sup _{x \in \mathrm{G}} f(x)=\sup _{v \in \mathcal{V}} f(v)
$$

(ii) If additionally $f \in H^{1}(\mathrm{G})$, then

$$
\sup _{x \in \mathrm{G}} f(x)=\sup _{\gamma \in \mathcal{C}(\mathrm{G})} f(\gamma)
$$

(iii) If (not necessarily real-valued) $f \in N_{\lambda}\left(H_{0}\right) \cap H^{1}(\mathrm{G})$ satisfies

$$
f(\gamma)=0
$$

for all $\gamma \in \mathcal{C}(\mathrm{G})$, then $f \equiv 0$.
Proof. (i) Let $f \in N_{\lambda}\left(H_{0}\right)$ be real-valued. If $x \in \mathrm{G}$ is such that $f(x)>0$ and $e \in \mathcal{E}$ is an edge with $x \in e$, then upon identifying $e$ with the interval $I_{e}=[0,|e|]$ and taking into account that $-f^{\prime \prime}=\lambda f$ on $e$, we get

$$
f(y)=f(x) \cosh (\sqrt{-\lambda}(y-x))+f^{\prime}(x) \sqrt{-\lambda} \sinh (\sqrt{-\lambda}(y-x))
$$

for all $y \in e$. If $f^{\prime}(x) \geq 0$, then obviously $f\left(e_{i}\right) \geq f(x)$, where $e_{i}$ is the vertex of $e$ identified with the right endpoint of $I_{e}$. Similarly, $f\left(e_{o}\right) \geq f(x)$ for the other vertex $e_{o}$ of $e$ if $f^{\prime}(x)<0$. Hence $f$ attains its maximum on $e$ at the vertices of $e$, which clearly implies (4.7).

[^0]
[^0]:    ${ }^{\dagger}$ A classification of groups having infinitely many ends is given in Stallings's ends theorem [73] (see also $[32$, Theorem 13.5.10] and Remark 2.5(iv)).



(ii) Now let $v \in V$ be a vertex with $f(v)>0$. By (2.7), there is an edge $e \in \mathcal{E}_{v}$ such that $f_{e}^{\prime}(v) \geq 0$. If $u \in V$ is the other vertex of $e$, then by (4.10) we get

$$
f(u)=f(v) \cosh (\sqrt{-\lambda}|e|)+f_{e}^{\prime}(v) \sqrt{-\lambda} \sinh (\sqrt{-\lambda}|e|)>f(v)
$$

Observe that $f_{e}^{\prime}(u)<0$. Hence, setting $v_{0}=v$ and $v_{1}=u$ and using induction, we can construct a ray $R=\left(v_{n}\right)$ such that $f\left(v_{n+1}\right)>f\left(v_{n}\right)$ for all $n \geq 0$. Since $f \in H^{1}(\mathcal{G})$, we get

$$
0<f(v)<\lim _{n \rightarrow \infty} f\left(v_{n}\right)=f\left(\gamma_{R}\right) \leq \sup _{\gamma \in \mathrm{C}(\mathcal{G})} f(\gamma)
$$

which proves $(4.8)$.
(iii) By considering $\pm f$ (and splitting into real and imaginary part, if necessary), (4.9) clearly follows from (4.8).

Remark 4.6. Notice that the arguments used in the proof of Lemma 4.5(ii) in fact show that functions in $\mathcal{N}_{\lambda}\left(H_{0}\right)$ with $\lambda \in(-\infty, 0)$ admitting positive values on $\mathcal{G}$ cannot attain global maxima in $\mathcal{G}$, that is, if $f$ attains a positive value at some $x \in \mathcal{G}$, then for every compact subgraph $\widetilde{\mathcal{G}} \subset \mathcal{G}$ the following holds

$$
\sup _{x \in \mathcal{G}} f(x)=\sup _{x \in \mathcal{G} \backslash \widetilde{\mathcal{G}}} f(x)
$$

Clearly, analogous statements hold true for functions admitting negative values, however, then sup must be replaced with inf.

Lemma 4.7. Suppose $\mathcal{G}$ is a metric graph and let $\lambda \in(-\infty, 0)$. Then

$$
\operatorname{dim}\left(\mathcal{N}_{\lambda}\left(H_{0}\right) \cap H^{1}(\mathcal{G})\right)=\# \mathcal{C}_{0}(\mathcal{G})
$$

Proof. Using (4.6) with $z=\lambda \in(-\infty, 0)$ and noting that $\operatorname{dom}\left(H_{F}\right) \subset H_{0}^{1}(\mathcal{G})$, Theorem 3.10 and Theorem 3.12 imply that $\operatorname{dim}\left(\mathcal{N}_{\lambda}\left(H_{0}\right) \cap H^{1}(\mathcal{G})\right) \geq \# \mathcal{C}_{0}(\mathcal{G})$. The converse inequality follows from Lemma 4.5(iii), which shows that the mapping $f \mapsto(f(\gamma))_{\gamma \in \mathcal{C}_{0}(\mathcal{G})}$ is injective on $\mathcal{N}_{\lambda}\left(H_{0}\right) \cap H^{1}(\mathcal{G})$.

After all these preparations, we are now in position to complete the proof of Theorem 4.1.
Proof of Theorem 4.1. Observe that the inequality (4.1) immediately follows from (4.6) and (4.11) since $n_{ \pm}(H)=\operatorname{dim}\left(\mathcal{N}_{\lambda}\left(H_{0}\right)\right)$.

Clearly, the second claim is trivial if $\# \mathcal{C}_{0}(\mathcal{G})=\infty$. Hence it remains to show that in the case $\# \mathcal{C}_{0}(\mathcal{G})<\infty$ equality (4.2) holds exactly when $\operatorname{dom}(H) \subset H^{1}(\mathcal{G})$. Applying (4.6) once again, the inclusion $\operatorname{dom}(H) \subset H^{1}(\mathcal{G})$ holds true exactly when $\mathcal{N}_{\lambda}\left(H_{0}\right) \subset H^{1}(\mathcal{G})$. Taking into account once again that $n_{ \pm}(H)=\operatorname{dim} \mathcal{N}_{\lambda}\left(H_{0}\right)$ and using (4.11), we arrive at the conclusion.
Remark 4.8. Let us mention that one can prove the second claim of Theorem 4.1 in a different way. Namely, if $\# \mathcal{C}_{0}(\mathcal{G})<\infty$, then it is possible to reduce the problem to the study of a finite volume graph with a single end.

Let us stress that in the proof of Theorem 4.1 the equivalence of equality (4.2) and the inclusion $\operatorname{dom}(H) \subset H^{1}(\mathcal{G})$ was proved in the case when all finite volume ends are free. The next result shows that the inclusion never holds if there is a finite volume end which is not free.



Proposition 4.9. Let $G$ be a metric graph having a finite volume end which is not free. Then there exists a function $f \in \operatorname{dom}(\mathcal{H})$ which does not belong to $H^{1}(G)$.

Proof. First observe that we can restrict our considerations to the case of a metric graph $G$ having finite total volume. Indeed, if $\gamma$ is a non-free finite volume end of $G$, then there exists a sequence $\mathcal{U}=\left(U_{n}\right)$ representing $\gamma$ such that $\operatorname{vol}\left(U_{n}\right)<\infty$ for all $n$. By definition, each $U_{n}$ is open and has compact boundary. Choosing $G_{0} \subset G$ as the subgraph with vertex set $V\left(G_{0}\right)=V \cap U_{0}$ and edge set $E\left(G_{0}\right)=\left\{e \in E \mid e \subset U_{0}\right\}$, it is easy to see that $G_{0}$ is a connected finite volume subgraph and $\gamma$ is a non-free end of $G_{0}$ (see also the notion of graph representation of an end in Section 6.1). Moreover, by construction the set $\partial G_{0}$ of boundary points (here, $G_{0}$ is seen as a closed subset of $G$ ) is finite.

Let $\widetilde{G} \subset G$ be a connected, compact subgraph and consider the finitely many connected components of $G \backslash \widetilde{G}$. Since $G$ has infinitely many ends, there is a connected component $\mathcal{U}$ which contains at least two distinct graph ends $\gamma, \gamma^{\prime} \in C(G)$. Following the proof of Theorem 3.10, we readily construct a real-valued function $f=f_{\mathcal{U}} \in$ $\operatorname{dom}(\mathcal{H}) \cap H^{1}(G)$ with $f(\gamma)=0, f\left(\gamma^{\prime}\right)=1$ and $0 \leq f \leq 1$ on $\mathcal{C}(G)$ (in fact,

 account Theorem 3.12 and decomposition (4.6), we can assume that $f$ belongs to $H^{1}(G) \cap \mathcal{N}_{\lambda}\left(\mathcal{H}_{0}\right)$ for some (fixed) $\lambda \in(-\infty, 0)$. However, Lemma 4.5 (iii) implies that

$$
\|f\|_{\infty}=\sup _{x \in G}|f(x)|=\sup _{x \in G} f(x)=1
$$

On the other hand, there exist two rays $R, R^{\prime} \in \mathcal{R}\left(G_{d}\right)$ representing the ends $\gamma$ and, respectively, $\gamma^{\prime}$ such that both $R, R^{\prime}$ are contained in $\mathcal{U}$ and have the same initial vertex $v_{0}$. This leads to another estimate

$$
\begin{aligned}
1 & =\left|f(\gamma)-f\left(\gamma^{\prime}\right)\right|=\left|f(\gamma)-f\left(v_{0}\right)+f\left(v_{0}\right)-f\left(\gamma^{\prime}\right)\right| \\
& =\left|\int_{R} f^{\prime}(x) \mathrm{d} x-\int_{R^{\prime}} f^{\prime}(x) \mathrm{d} x\right| \leq 2 \sqrt{\operatorname{vol}(\mathcal{U})}\left\|f^{\prime}\right\|_{L^{2}(\mathcal{U})} \leq 2 \sqrt{\operatorname{vol}(\mathcal{U})}\left\|f^{\prime}\right\|_{L^{2}(G)}
\end{aligned}
$$

Assume now that (4.3) holds for all functions $g \in \mathcal{N}_{\lambda}\left(\mathcal{H}_{0}\right)$. Then $\|\cdot\|_{\infty}$ and $\|\cdot\|_{H^{1}}$ are in fact equivalent norms on $\mathcal{N}_{\lambda}\left(\mathcal{H}_{0}\right)$. Indeed, combining (4.3) and the finite volume property, we get

$$
\|g\|_{H^{1}}^{2} \leq C\left(\|g\|_{L^{2}}^{2}+\|H g\|_{L^{2}}^{2}\right)=C\left(1+\lambda^{2}\right)\|g\|_{L^{2}}^{2} \leq C\left(1+\lambda^{2}\right) \operatorname{vol}(G)\|g\|_{\infty}^{2}
$$

for all $g \in \mathcal{N}_{\lambda}\left(\mathcal{H}_{0}\right)$, whereas $\|g\|_{\infty} \leq C_{G}\|g\|_{H^{1}}$ by Lemma 3.2. Choosing compact subgraphs $\widetilde{G}_{\varepsilon}$ with $\operatorname{vol}\left(G \backslash \widetilde{G}_{\varepsilon}\right) \leq \varepsilon^{2}$ (which is possible since $G$ has finite volume), we clearly get $\operatorname{vol}\left(\mathcal{U}_{\varepsilon}\right) \leq \varepsilon^{2}$ and hence the above constructed function $f_{\varepsilon}:=f_{\mathcal{U}_{\varepsilon}} \in$ $H^{1}(G) \cap \mathcal{N}_{\lambda}\left(\mathcal{H}_{0}\right)$ satisfies

$$
\left\|f_{\varepsilon}^{\prime}\right\|_{L^{2}(G)} \geq\left\|f_{\varepsilon}^{\prime}\right\|_{L^{2}\left(\mathcal{U}_{\varepsilon}\right)} \geq \frac{1}{2 \sqrt{\operatorname{vol}\left(\mathcal{U}_{\varepsilon}\right)}} \geq \frac{1}{2 \varepsilon}
$$

However, by construction, $\left\|f_{\varepsilon}\right\|_{\infty}=1$, which obviously contradicts to the equivalence of norms $\|\cdot\|_{\infty}$ and $\|\cdot\|_{H^{1}}$ on $\mathcal{N}_{\lambda}\left(\mathcal{H}_{0}\right)$ since $\varepsilon>0$ is arbitrary.

We conclude this section by mentioning some explicit examples.
Example 4.10 (Radially symmetric trees). Let $G=T$ be a radially symmetric (metric) tree: that is, a rooted tree $T$ such that for each $n \geq 0$, all vertices in the combinatorial sphere $S_{n}$ have the same number of descendants $d_{n} \geq 2$ and all edges



between the combinatorial spheres $S_{n}$ and $S_{n+1}$ have the same length. It is wellknown that in this case $H$ is self-adjoint if and only if $\operatorname{vol}(T)=\infty$ and deficiency indices are infinite, $n_{ \pm}\left(H_{0}\right)=\infty$, otherwise (see, e.g., $[15,72]$ ). Moreover, due to the symmetry assumptions, all graph ends are of finite volume simultaneously. Hence we arrive at the equality

$$
n_{ \pm}\left(H_{0}\right)=\# \mathcal{C}^{0}(G)= \begin{cases}\infty, & \text { if } \operatorname{vol}(T)<\infty \\ 0, & \text { if } \operatorname{vol}(T)=\infty\end{cases}
$$

Moreover, by Theorem 4.1 and Proposition 4.9, the inclusion $\operatorname{dom}(H) \subset H^{1}(G)$ holds true if and only if $\operatorname{vol}(T)=\infty$.

Example 4.11 (Radially symmetric antitrees). Consider a metric antitree $G=\mathbb{A}$ (see Section 7.1 for definitions) and additionally suppose that $\mathbb{A}$ is radially symmetric, that is, for each $n \geq 0$, all edges between the combinatorial spheres $S_{n}$ and $S_{n+1}$ have the same length. Combining [56, Theorem 4.1] (see also Corollary 7.3 below) with the fact that antitrees have exactly one graph end, $\# \mathcal{C}(\mathbb{A})=1$, we conclude that

$$
n_{ \pm}\left(H_{0}\right)=\# \mathcal{C}^{0}(G)= \begin{cases}1, & \text { if } \operatorname{vol}(\mathbb{A})<\infty \\ 0, & \text { if } \operatorname{vol}(\mathbb{A})=\infty\end{cases}
$$

In particular, $H$ is self-adjoint if and only if $\operatorname{vol}(\mathbb{A})=\infty$. Moreover, the inclusion $\operatorname{dom}(H) \subset H^{1}(G)$ holds true for all radially symmetric antitrees by Theorem 4.1.
Remark 4.12. Both radially symmetric trees and antitrees are particular examples of the so-called family preserving metric graphs (see [11] and also [10]) . Employing the results from [11], it is in fact possible to extend the conclusions in Example 4.10 and Example 4.11 to this general setting. More precisely, for each family preserving metric graph $G$ without horizontal edges, the Kirchhoff Laplacian $H$ is self-adjoint if and only if $\operatorname{vol}(G)=\infty$ and moreover

$$
n_{ \pm}\left(H_{0}\right)=\# \mathcal{C}^{0}(G)= \begin{cases}\# \mathcal{C}(G), & \text { if } \operatorname{vol}(G)<\infty \\ 0, & \text { if } \operatorname{vol}(G)=\infty\end{cases}
$$

If in addition $G$ has finitely many ends, then the inclusion $\operatorname{dom}(H) \subset H^{1}(G)$ holds true. On the other hand, if $G$ has infinitely many ends, then $\operatorname{dom}(H) \subset H^{1}(G)$ holds true if and only if $\operatorname{vol}(G)=\infty$. The last two statements are again immediate consequences of Theorem 4.1 and Proposition 4.9.

In conclusion, let us also emphasize that the example of the rope ladder graph in Appendix B shows that the assumption on horizontal edges cannot be omitted. More precisely, the rope ladder graph is a family preserving graph in the sense of [10] with exactly one graph end. However, it possesses infinitely many horizontal edges (i.e., edges connecting vertices in the same combinatorial sphere) and Example B. 5 shows that in general $n_{ \pm}\left(H_{0}\right)>\# \mathcal{C}^{0}(G)$, even if the edge lengths are chosen symmetrically to the root, $\left|e_{n}^{+}\right|=\left|e_{n}^{-}\right|$for all $n \in \mathbb{Z}_{\geq 0}$.

# 5. Properties of self-adjoint extensions 

The Sobolev space $H^{1}(G)$ plays a distinctive role in the study of self-adjoint extensions of the minimal operator $H_{0}$. A self-adjoint extension $\widetilde{H}$ of $H_{0}$ is called a finite energy extension if its domain is contained in $H^{1}(G)$, that is, every function $f \in \operatorname{dom}(\widetilde{H})$ has finite energy, $\left\|f^{\prime}\right\|_{L^{2}(G)}<\infty$. The main result of this section



already indicates that finite energy self-adjoint extensions of the minimal operator (notice that among those are the Friedrichs extension and, as we will see later in this section, all Markovian extensions) possess a number of important properties.

THEOREM 5.1. Let $\widetilde{H}$ be a self-adjoint lower semi-bounded extension of $H_{0}$. Assume that $z$ belongs to its resolvent set $\rho(\widetilde{H})$. Then the following assertions hold.
(i) If the form domain of $\widetilde{H}$ is contained in $H^{1}(G)$, then the resolvent $R(z, \widetilde{H})$ of $\widetilde{H}$ is an integral operator whose kernel $K_{z}$ is both of class $L^{\infty}(G \times G)$ and jointly Hölder continuous of exponent $\beta=1 / 2$.
(ii) If additionally $G$ has finite total volume, then $R(z, \widetilde{H})$ is of trace class.

Proof. (i) Let $\widetilde{H}$ be a self-adjoint lower semi-bounded extension of $H_{0}, \widetilde{H} \geq c$ for some $c \in \mathbb{R}$. Without loss of generality we may assume $c=0$. Then we can consider its positive semi-definite square root $\widetilde{H}^{1 / 2}$, which is again self-adjoint and whose domain agrees with the form domain of $\widetilde{H}$. Accordingly, for all $z \in \mathbb{C} \backslash[0, \infty)$ and $\lambda=\sqrt{z}$ we get

$$
\left(\widetilde{H}^{1 / 2}-\lambda\right)\left(\widetilde{H}^{1 / 2}+\lambda\right)=\widetilde{H}-z
$$

and hence

$$
R(z, \widetilde{H})=R\left(\lambda, \widetilde{H}^{1 / 2}\right) R\left(-\lambda, \widetilde{H}^{1 / 2}\right)
$$

If the form domain of $\widetilde{H}$ is contained in $H^{1}(G)$, and hence by Lemma 3.2 in $C_{b}(G)$, then $R\left( \pm \lambda, \widetilde{H}^{1 / 2}\right)$ maps $L^{2}(G)$ into $L^{\infty}(G)$, and hence by duality also maps $L^{1}(G)$ into $L^{2}(G)$. Thus (5.1) implies that $R(z, \widetilde{H})$ maps $L^{1}(G)$ into $L^{\infty}(G)$ and hence, by the Kantorovich-Vulikh theorem (see, e.g., [4, Theorem 1.3] or [63, Theorem 1.1]), $R(z, \widetilde{H})$ is an integral operator with the $L^{\infty}$-kernel $K(z ; \cdot, \cdot)$.

In order to prove the assertion about joint Hölder continuity, we need to take a closer look at the kernel $K$ by adapting the proof of [3, Prop.2.1]: as noticed before, the resolvent $R\left(\lambda, \widetilde{H}^{1 / 2}\right)$ is bounded from $L^{2}(G)$ to $L^{\infty}(G)$ by Lemma 3.2 for any $\lambda$ in the resolvent set of $\widetilde{H}^{1 / 2}$. Applying the Kantorovich-Vulikh theorem (see, e.g., [4, page 113]) once again, we see that

$$
R\left(\lambda, \widetilde{H}^{1 / 2}\right) u(x)=\int_{G} u(y) \kappa(\lambda ; x, y) \mathrm{d} y=\left\langle u, \kappa(\lambda ; x, \cdot)^{*}\right\rangle_{L^{2}(G)}
$$

for all $x \in G$ and some $\kappa(\lambda ; x, \cdot) \in L^{2}(G)$ such that $\sup _{x \in G}\|\kappa(\lambda ; x, \cdot)\|_{L^{2}(G)}<\infty$. Moreover, observe that there exists $C=C(\lambda)>0$ such that

$$
\left\|\kappa(\lambda ; x, \cdot)-\kappa\left(\lambda ; x^{\prime}, \cdot\right)\right\|_{L^{2}(G)} \leq C \sqrt{\varrho\left(x, x^{\prime}\right)}
$$

for all $x, x^{\prime} \in G$, where $\varrho\left(x, x^{\prime}\right)$ denotes the distance in the natural path metric on $G$. Indeed, for any function $u \in L^{2}(G)$,

$$
\begin{aligned}
& \left|\int_{G} u(y)\left(\kappa(\lambda ; x, y)-\kappa\left(\lambda ; x^{\prime}, y\right)\right) \mathrm{d} y\right|=\left|R\left(\lambda, \widetilde{H}^{1 / 2}\right) u(x)-R\left(\lambda, \widetilde{H}^{1 / 2}\right) u\left(x^{\prime}\right)\right| \\
& \quad \leq \sqrt{\varrho\left(x, x^{\prime}\right)}\left\|R\left(\lambda, \widetilde{H}^{1 / 2}\right) u\right\|_{H_{1}} \\
& \quad \leq C \sqrt{\varrho\left(x, x^{\prime}\right)}\|u\|_{L^{2}}
\end{aligned}
$$

where we have used the Cauchy-Schwarz inequality and the fact that the resolvent $R\left(\lambda, \widetilde{H}^{1 / 2}\right)$ is a bounded operator from $L^{2}$ to the domain of $\widetilde{H}^{1 / 2}$ equipped with the



graph norm, and (5.2) immediately follows. Now, taking into account the equalities (5.1) and $R\left(\lambda, \widetilde{H}^{1 / 2}\right)^{*}=R\left(\lambda^{*}, \widetilde{H}^{1 / 2}\right)$, we conclude that

$$
\begin{aligned}
R(z, \widetilde{H}) u(x) & =R\left(\lambda, \widetilde{H}^{1 / 2}\right)\left(R\left(-\lambda, \widetilde{H}^{1 / 2}\right) u\right)(x) \\
& =\left\langle R\left(-\lambda, \widetilde{H}^{1 / 2}\right) u, \varkappa(\lambda ; x, \cdot)^{*}\right\rangle_{L^{2}(G)} \\
& =\left\langle u, R\left(-\lambda^{*}, \widetilde{H}^{1 / 2}\right) \varkappa(\lambda ; x, \cdot)^{*}\right\rangle_{L^{2}(G)} \\
& =\int_{G} u(y) \int_{G} \varkappa(\lambda ; x, s) \varkappa\left(-\lambda^{*} ; y, s\right)^{*} \mathrm{~d} s \mathrm{~d} y \\
& =: \int_{G} u(y) K(z ; x, y) \mathrm{d} y
\end{aligned}
$$

for all $u \in L^{2}(G)$. It remains to prove that the mapping

$$
K: G \times G \ni(x, y) \mapsto \int_{G} \varkappa(\lambda ; x, s) \varkappa\left(-\lambda^{*} ; y, s\right)^{*} \mathrm{~d} s \in \mathbb{C}
$$

is jointly Hölder continuous. However, recalling that $\sup _{x \in G}\|\varkappa(\lambda, x ; \cdot)\|_{L^{2}(G)}<\infty$, this immediately follows from (5.2), since

$$
\begin{aligned}
\left|K(x, y)-K\left(x^{\prime}, y^{\prime}\right)\right| \leq & \left\|\varkappa(\lambda ; x, \cdot)\left(\varkappa\left(-\lambda^{*} ; y, \cdot\right)^{*}-\varkappa\left(-\lambda^{*} ; y^{\prime}, \cdot\right)^{*}\right)\right\|_{L^{1}} \\
& +\left\|\varkappa\left(-\lambda^{*} ; y^{\prime}, \cdot\right)^{*}\left(\varkappa(\lambda ; x, \cdot)-\varkappa\left(\lambda ; x^{\prime}, \cdot\right)\right)\right\|_{L^{1}}
\end{aligned}
$$

for all pairs $(x, y),\left(x^{\prime}, y^{\prime}\right) \in G \times G$.
(ii) If $\mathcal{G}$ has finite total volume, then $L^{\infty}(G \times G) \hookrightarrow L^{2}(G \times G)$ and hence the resolvents $R\left( \pm \lambda, \widetilde{H}^{1 / 2}\right)$ are Hilbert-Schmidt operators. Thus, by (5.1) we conclude that $R(z, \widetilde{H})$ is of trace class.

Observe that the first step in the proof of Theorem 5.1 is the factorization (5.1), which has the natural counterpart for semigroups

$$
e^{-z \widetilde{H}} e^{-z \widetilde{H}}=e^{-2 z \widetilde{H}}, \quad \operatorname{Re} z>0
$$

Because the semigroup generated by a self-adjoint semi-bounded extension $\widetilde{H}$ is analytic, it is a bounded operator from the Hilbert space into its generator's form domain whenever $\operatorname{Re} z>0$. A careful look at the proof of Theorem 5.1 shows that this is sufficient to establish that $e^{-z \widetilde{H}}$ is an integral operator; all further steps in the proof of Theorem 5.1 carry over almost verbatim to the study of semigroups. We can hence easily deduce the following result.

Theorem 5.2. Let $\widetilde{H}$ be a self-adjoint lower semi-bounded extension of $H_{0}$ and let $z \in \mathbb{C}$ with $\operatorname{Re} z>0$. Then the following assertions hold.
(i) If the domain of $\widetilde{H}$ is contained in $H^{1}(\mathcal{G})$, then the semigroup $e^{-z \widetilde{H}}$ generated by $\widetilde{H}$ is an integral operator whose kernel is both of class $L^{\infty}(G \times G)$ and jointly Hölder continuous of exponent $\beta=1 / 2$.
(ii) If additionally $\mathcal{G}$ has finite total volume, then $e^{-z \widetilde{H}}$ is of trace class.

Estimating as in (5.3) and using analyticity of $e^{-z \widetilde{H}}$ yields the inequality

$$
\left|p_{t}(x, y)-p_{t}\left(x^{\prime}, y\right)\right| \leq \frac{C}{\sqrt{t}} \sqrt{\varrho\left(x, x^{\prime}\right)}, \quad t>0, x, y, x^{\prime} \in G
$$

for the heat kernel $p_{t}(x, y)$ of a nonnegative extension $\widetilde{H}$, where in contrast to (5.3) the constant $C>0$ is independent of $t>0$. Such Hölder estimates are known



to be related to Sobolev-type inequalities and also important for upper and lower Gaussian bounds (cf., e.g., [20], [66, Chapter 6]). However, we do not pursue this line of study here and this will be done elsewhere.

Remark 5.3. A few remarks are in order.
(i) If $\sup _{R}|R|<\infty$, where the supremum is taken over all non-vertex paths without self-intersections, then the path metric $\varrho$ has a natural extension $\widehat{\varrho}$ to the end compactification $\widehat{G}$. Moreover, in this case $(\widehat{G}, \widehat{\varrho})$ coincides with the metric completion of $(G, \varrho)$. Indeed, the metric completion of $(G, \varrho)$ is obtained by adding to $G$ equivalence classes of rays of finite length (see [34, Section 2.3 ] for details) and the distance of $x \in G$ to a boundary point is defined as the "shortest length" of a path in the corresponding equivalence class starting at $x$.

Therefore, Theorem 5.1 and Theorem 5.2 imply that in this case the corresponding resolvent and semigroup kernels have a bounded and uniformly continuous extension to $(\widehat{G}, \widehat{\varrho})$. However, we stress that in contrast to the case $\operatorname{vol}(G)<\infty$ (see Remark 3.11), the topology generated by $\widehat{\varrho}$ on $\widehat{G}$ can differ from the end compactification topology if $\operatorname{vol}(G)=\infty$.
(ii) Discreteness of the spectrum of the Friedrichs extension $H_{F}$ is a standard fact in the case of finite total volume (see, e.g., [16, Prop. 3.11] or [56, Corollary 3.5(iv)]). However, Theorem 5.1(ii) implies the stronger assertion that the resolvent of $H_{F}$ belongs to the trace class if $\operatorname{vol}(G)<\infty$. Let us also stress that it is not true in general that every self-adjoint extension of $H$ will have a discrete spectrum if $\operatorname{vol}(G)<\infty$, since in case of infinite deficiency indices such a self-adjoint extension could have a domain large enough to make compactness of the embedding of $H^{1}(G)$ into $L^{2}(G)$ irrelevant.

Recall that a self-adjoint extension $\widetilde{H}$ of $H_{0}$ is called Markovian if $\widetilde{H}$ is a nonnegative self-adjoint extension and the corresponding quadratic form is a Dirichlet form (for definitions and further details we refer to [31, Chapter 1]). Hence the associated semigroup $e^{-t \widetilde{H}}, t>0$, as well as resolvents $R(-\lambda, \widetilde{H}), \lambda>0$, are Markovian: i.e., are both positivity preserving (map non-negative functions to nonnegative functions) and $L^{\infty}$-contractive (map the unit ball of $L^{\infty}(G)$, and then by duality of $L^{p}(G)$ for all $p \in[1, \infty]$, into itself). Let us stress that the Friedrichs extension $H_{F}$ of $H_{0}$ is a Markovian extension. Consider also the following quadratic form in $L^{2}(G)$

$$
t_{N}[f]=\int_{G}\left|f^{\prime}(x)\right|^{2} d x, \quad \operatorname{dom}\left(t_{N}\right)=H^{1}(G)
$$

This form is non-negative and closed, hence we can associate in $L^{2}(G)$ a self-adjoint operator with it, let us denote it by $H_{N}$. We will refer to it as the Neumann extension. It is straightforward to check that $t_{N}$ is a Dirichlet form and $H_{N}$ is also a Markovian extension of $H_{0}$.

It turns out that Theorems 5.1 and 5.2 apply to all Markovian extensions of $H_{0}$. More specifically, the analog of the results for discrete Laplacians [39, Theorem 5.2] and Laplacians in Euclidean domains [31, Chapter 3] and Riemannian manifolds [37, Theorem 1.7] holds true for quantum graphs as well.



Theorem 5.4. If $\widetilde{H}$ is a Markovian extension of $H_{0}$, then $\operatorname{dom}(\widetilde{H}) \subset H^{1}(G)$ and, moreover,

$$
H_{\mathrm{N}} \leq \widetilde{H} \leq H_{\mathrm{F}}
$$

where the inequalities are understood in the sense of forms. ${ }^{\dagger}$
We omit the proof of Theorem 5.4 since the proofs of either [39, Theorem 5.2] or $[37$, Lemma 3.6] carry over verbatim to our setting (see also the proof of [31, Theorem 3.3.1]).

Let us finish this section with the following observation.
Corollary 5.5. The following are equivalent:
(i) $H_{0}$ has a unique Markovian extension,
(ii) $H_{0}^{1}(G)=H^{1}(G)$
(iii) all topological ends of $G$ have infinite volume, $\mathcal{C}_{0}(G)=\varnothing$.

Proof. The claimed equivalences follow from Theorem 5.4 and Corollary 3.13.
Remark 5.6. Let us finish this section with a few comments.
(i) The equivalence (i) $\Leftrightarrow$ (ii) in Corollary 5.5 is known for Riemannian manifolds [37, Theorem 1.7] (see also [31, Chapter 3], [62, Theorem 1]) as well as for weighted Laplacians on graphs [39, Corollary 5.6]. However, to the best of our knowledge these settings do not admit any further geometric characterization.
(ii) The list of equivalences in Corollary 5.5 can be extended by adding a claim on the self-adjointness of the so-called Gaffney Laplacian. Namely, since $H_{0}^{1}(G)$ and $H^{1}(G)$ are Hilbert spaces, the operators denoted by $\nabla_{D}$ and $\nabla_{N}$ and defined in $L^{2}(G)$ on the domains, respectively, $H_{0}^{1}(G)$ and $H^{1}(G)$ by $f \mapsto f^{\prime}$ are closed. Notice that with this notation at hand we have $H_{\mathrm{F}}=\nabla_{D}^{*} \nabla_{D}$ and $H_{\mathrm{N}}=\nabla_{N}^{*} \nabla_{N}$. Now we can introduce the Gaffney Laplacian $H_{\mathrm{G}}:=\nabla_{D}^{*} \nabla_{N}$ as the restriction of the maximal operator $H$ onto the domain (compare with [37, p. 610 ] for the definition in the manifolds case)

$$
\operatorname{dom}\left(H_{\mathrm{G}}\right):=\left\{f \in H^{1}(G) \mid \nabla_{N} f \in \operatorname{dom}\left(\nabla_{D}^{*}\right)\right\}
$$

Clearly, $\operatorname{dom}\left(H_{\mathrm{F}}\right) \subseteq \operatorname{dom}\left(H_{\mathrm{G}}\right), \operatorname{dom}\left(H_{\mathrm{N}}\right) \subseteq \operatorname{dom}\left(H_{\mathrm{G}}\right)$, and $H_{\mathrm{G}}$ is not necessarily symmetric. It turns out that $H_{\mathrm{G}}$ is symmetric (and hence selfadjoint) if and only if the Kirchhoff Laplacian $H_{0}$ has a unique Markovian extension. Moreover, in this case $H_{\mathrm{F}}=H_{\mathrm{N}}=H_{\mathrm{G}}$ (cf. [37, Theorem 1.7(ii)] in the manifold setting). Let us mention that the Markovian/finite energy extensions of $H_{0}$ are exactly the Markovian/self-adjoint restrictions of $H_{\mathrm{G}}$ and hence the deficiency indices of $H_{\mathrm{G}}^{*}=\nabla_{N}^{*} \nabla_{D}$ are equal to $\# \mathcal{C}_{0}(G)$.

# 6. Finite ENERgy SELF-ADJOINT EXTENSIONS 

It turns out that finite volume (topological) ends provide the right notion of the boundary for metric graphs to deal with finite energy and also with Markovian extensions of the minimal Kirchhoff Laplacian $H_{0}$. In particular, we are going to show that this end space is well-behaved as concerns the introduction of both traces and normal derivatives. More specifically, the goal of this section is to give a description

[^0]
[^0]:    ${ }^{\dagger}$ We shall write $A \leq B$ for two non-negative self-adjoint operators $A$ and $B$ if their quadratic forms $t_{A}$ and $t_{B}$ satisfy $\operatorname{dom}\left(t_{B}\right) \subseteq \operatorname{dom}\left(t_{A}\right)$ and $t_{A}[f] \leq t_{B}[f]$ for every $f \in \operatorname{dom}\left(t_{B}\right)$



of finite energy self-adjoint extensions of $H_{0}$ in the case when the number of finite volume ends of $G$ is finite, that is, $\# \mathcal{C}_{0}(G)<\infty$. Notice that in this case all finite volume ends are free.
6.1. Normal derivatives at graph ends. Let $\widetilde{G}=(\widetilde{V}, \widetilde{E})$ be a (possibly infinite) connected subgraph of $G$. Recall that its boundary $\partial \widetilde{G}$ (w.r.t. the natural topology on $G$, see Section 2.1) is given by

$$
\partial \widetilde{G}=\left\{v \in \widetilde{V} \mid \operatorname{deg} \widetilde{G}(v)<\operatorname{deg}_{G}(v)\right\}
$$

For a function $f \in \operatorname{dom}(H)$, we define its (inward) normal derivative at $v \in \partial \widetilde{G}$ by

$$
\frac{\partial f}{\partial n_{\widetilde{G}}}(v):=\sum_{e \in \operatorname{Ev} \cap \widetilde{E}} f_{e}^{\prime}(v)
$$

With this definition at hand, we end up with the following useful integration by parts formula.

Lemma 6.1. Let $\widetilde{G}$ be a compact (not necessarily connected) subgraph of the metric graph $G$. Then

$$
-\int_{\widetilde{G}} f^{\prime \prime}(x) g(x) \mathrm{d} x=\int_{\widetilde{G}} f^{\prime}(x) g^{\prime}(x) \mathrm{d} x+\sum_{v \in \partial \widetilde{G}} g(v) \frac{\partial f}{\partial n_{\widetilde{G}}}(v)
$$

for all $f \in \operatorname{dom}(H)$ and $g \in H^{1}(\widetilde{G})$. In particular,

$$
-\int_{\widetilde{G}} f^{\prime \prime}(x) \mathrm{d} x=\sum_{v \in \partial \widetilde{G}} \frac{\partial f}{\partial n_{\widetilde{G}}}(v)
$$

Proof. The claim follows immediately from integrating by parts, taking into account that $f$ satisfies (2.7). Setting $g \equiv 1$ in (6.3), we arrive at (6.4).

In order to simplify our considerations, we need to introduce the following notion. Let $\gamma \in \mathcal{C}(G)$ be a (topological) end of $G$. Consider a sequence $\left(G_{n}\right)$ of connected subgraphs of $G$ such that $G_{n} \supseteq G_{n+1}$ and $\# \partial G_{n}<\infty$ for all $n$. We say that the sequence $\left(G_{n}\right)$ is a graph representation of the end $\gamma \in \mathcal{C}(G)$ if there is a sequence of open sets $U=\left(U_{n}\right)$ representing $\gamma$ such that for each $n \geq 0$ there exist $j$ and $k$ such that $G_{n} \supseteq U_{j}$ and $U_{n} \supseteq G_{k}$. It is easily seen that all graphs $G_{n}$ are infinite (they have infinitely many edges). Moreover, graph representations $\left(G_{n}\right)$ of an end can be constructed with the help of compact exhaustions; in particular each graph end $\gamma \in \mathcal{C}(G)$ has a representation by subgraphs (see Section 2.2).

Proposition 6.2. Let $G$ be a metric graph and let $\gamma \in \mathcal{C}(G)$ be a free end of finite volume. Then for every function $f \in \operatorname{dom}(H)$ and any sequence $\left(G_{k}\right)$ of subgraphs representing $\gamma$, the limit

$$
\lim _{k \rightarrow \infty} \sum_{v \in \partial G_{k}} \frac{\partial f}{\partial n_{G_{k}}}(v)
$$

exists and is independent of the choice of $\left(G_{k}\right)$.
Proof. First of all, notice that uniqueness of the limit follows from the inclusion property in the definition of the graph representations of $\gamma$. Hence we only need to show that the limit in (6.5) indeed exists.



Let $\left(G_{k}\right)$ be a graph representation of a free finite volume end $\gamma \in C_{0}(G)$. Since $\gamma$ is free, we can assume that $\operatorname{vol}\left(G_{0}\right)<\infty$ and that $G_{0} \cap U_{k}=\emptyset$ eventually for every sequence $U=\left(U_{k}\right)$ representing an end $\gamma^{\prime} \neq \gamma$. First observe that $\widetilde{G}=G_{k} \backslash G_{j}$ can again be identified with a compact subgraph of $G$ whenever $k \leq j$. Indeed, if $\widetilde{G}$ has infinitely many edges $\left\{e_{n}\right\} \subset E$, choose for each $n$ a point $x_{n}$ in the interior of the edge $e_{n}$. Since $\widehat{G}=G \cup C(G)$ is compact, the set $\left\{x_{n}\right\}$ has an accumulation point $x \in \widehat{G}$. By construction, $x \notin G$ and hence $x \in \widehat{G} \backslash G=C(G)$ is an end. However, we have that $x_{n} \notin G_{j}$ and recalling (2.3) and (2.4), this implies that $x=\gamma^{\prime}$ for a topological end $\gamma^{\prime} \neq \gamma$. On the other hand, $x_{n} \in G_{0}$ for all $n$ and using the properties of $G_{0}$ and (2.3)-(2.4) once again, we arrive at a contradiction.

Now, using (6.1) it is straightforward to verify that

$$
\sum_{v \in \partial G_{k}} \frac{\partial f}{\partial n_{G_{k}}}(v)-\sum_{v \in \partial G_{j}} \frac{\partial f}{\partial n_{G_{j}}}(v)=\sum_{v \in \partial \widetilde{G}} \frac{\partial f}{\partial n_{\widetilde{G}}}(v)
$$

Hence by (6.4) and the Cauchy-Schwarz inequality, we get

$$
\left|\sum_{v \in \partial G_{k}} \frac{\partial f}{\partial n_{G_{k}}}(v)-\sum_{v \in \partial G_{j}} \frac{\partial f}{\partial n_{G_{j}}}(v)\right|=\left|\int_{G_{k} \backslash G_{j}} f^{\prime \prime}(x) d x\right| \leq \sqrt{\operatorname{vol}\left(G_{k}\right)}\|H f\|_{L^{2}(G)}
$$

whenever $k \leq j$. This implies the existence of the limit in (6.5) since $\operatorname{vol}\left(G_{k}\right)=o(1)$ as $k \rightarrow \infty$.

Proposition 6.2 now enables us to introduce a normal derivative at graph ends.
Definition 6.3. Let $\gamma \in C(G)$ be a free end of finite volume and let $\left(G_{k}\right)$ be a graph representation of $\gamma$. Then for every $f \in \operatorname{dom}(H)$

$$
\partial_{n} f(\gamma):=\frac{\partial f}{\partial n}(\gamma):=\lim _{k \rightarrow \infty} \sum_{v \in \partial G_{k}} \frac{\partial f}{\partial n_{G_{k}}}(v)
$$

is called the normal derivative of $f$ at $\gamma$.
Remark 6.4. In fact, it is not difficult to extend the definitions (6.2) and (6.7) to general sequences $U=\left(U_{n}\right)$ of open sets representing the free end $\gamma \in C_{0}(G)$. However, while the idea of the proof of Proposition 6.2 naturally carries over, the analysis becomes more technical and we restrict to the case of subgraphs for the sake of a clear exposition.

Let us mention that the normal derivative can also be expressed in terms of compact exhaustions.

Lemma 6.5. Let $G$ be a metric graph having finite total volume and only one end $\gamma, C(G)=\{\gamma\}$. If $\left(F_{k}\right)$ is a compact exhaustion of $G$ and $f \in \operatorname{dom}(H)$, then

$$
\partial_{n} f(\gamma)=-\lim _{k \rightarrow \infty} \sum_{v \in \partial F_{k}} \frac{\partial f}{\partial n_{F_{k}}}(v)
$$

The fact that we are not approximating $\gamma$ by its neighborhoods, but rather by compact subgraphs, is responsible for the different sign in (6.7) and (6.8).



Proof. First of all, notice that $G \backslash F_{k}$ can be identified with a subgraph of $G$ and

$$
-\sum_{v \in \partial F_{k}} \frac{\partial f}{\partial n_{F_{k}}}(v)=\sum_{v \in \partial\left(G \backslash F_{k}\right)} \frac{\partial f}{\partial n_{G \backslash F_{k}}}(v)
$$

for all $f \in \operatorname{dom}(H)$. If, moreover, $G \backslash F_{k}$ is a connected subgraph for all $k \geq 0$, then it is clear that $\left(G_{k}\right)$ with $G_{k}:=G \backslash F_{k}$ for all $k \geq 0$, is a graph representation of $\gamma$ and this proves (6.8) in this case.

If $G \backslash F_{k}$ is not connected, then it has only one infinite connected component $G_{k}^{\gamma}$ and finitely many compact components (since $\mathcal{C}(G)=\{\gamma\}$ ). Adding these compact components to $F_{k}$, we obtain a compact exhaustion $\left(F_{k}^{\prime}\right)$ with $G \backslash F_{k}^{\prime}=G_{k}^{\gamma}$. Arguing as in the proof of Proposition 6.2 (see (6.6)), we get

$$
\left|\sum_{v \in \partial F_{k}^{\prime}} \frac{\partial f}{\partial n_{F_{k}^{\prime}}}(v)-\sum_{v \in \partial F_{k}} \frac{\partial f}{\partial n_{F_{k}}}(v)\right|=\left|\int_{F_{k}^{\prime} \backslash F_{k}} f^{\prime \prime}(x) \mathrm{d} x\right|=o(1)
$$

as $k \rightarrow \infty$. Hence (6.8) holds true also in the general case.
6.2. Properties of the trace and normal derivatives. In this section, we collect some basic properties of the trace maps. We shall adopt the following notation. Since we shall always assume throughout this section that $\# \mathcal{C}_{0}(G)<\infty$, we set $H:=\ell^{2}\left(\mathcal{C}_{0}(G)\right)$, which can be further identified with $\mathbb{C}^{\# \mathcal{C}_{0}(G)}$. Next, we introduce the maps $\Gamma_{0}: H^{1}(G) \rightarrow H$ and $\Gamma_{1}: \operatorname{dom}(H) \cap H^{1}(G) \rightarrow H$ by

$$
\Gamma_{0}: f \mapsto(f(\gamma))_{\gamma \in \mathcal{C}_{0}(G)}, \quad \Gamma_{1}: f \mapsto\left(\partial_{n} f(\gamma)\right)_{\gamma \in \mathcal{C}_{0}(G)}
$$

where the boundary values and normal derivative of $f$ are defined by (3.4) and (6.7), respectively.

Proposition 6.6. Let $G$ be a metric graph with $\# \mathcal{C}_{0}(G)<\infty$. Then:
(i) For every $\widehat{f} \in H$, there exists $f \in \operatorname{dom}(H) \cap H^{1}(G)$ such that

$$
\Gamma_{0} f=\widehat{f}, \quad \Gamma_{1} f=0
$$

(ii) Moreover, the Gauss-Green formula

$$
\langle H f, g\rangle_{L^{2}(G)}=\left\langle f^{\prime}, g^{\prime}\right\rangle_{L^{2}(G)}-\left\langle\Gamma_{1} f, \Gamma_{0} g\right\rangle_{H}
$$

holds true for every $f \in \operatorname{dom}(H) \cap H^{1}(G)$ and $g \in H^{1}(G)$.
Proof. (i) Since $\# \mathcal{C}_{0}(G)<\infty$, each finite volume end $\gamma \in \mathcal{C}_{0}(G)$ is free. For every $\gamma \in \mathcal{C}_{0}(G)$, let $G_{\gamma}$ be a subgraph with the properties as in Remark 2.6. We can also assume that $\operatorname{vol}\left(G_{\gamma}\right)<\infty$. Following the proof of Theorem 3.10 , we can construct for each end $\gamma \in \mathcal{C}_{0}(G)$ a function $f_{\gamma} \in \operatorname{dom}(H) \cap H^{1}(G)$ such that $f_{\gamma}$ is nonconstant only on finitely many edges (since $\# \partial G_{\gamma}<\infty$ ), $f_{\gamma}(\gamma)=1$ and $f_{\gamma}\left(\gamma^{\prime}\right)=0$ for all other ends $\gamma^{\prime} \in \mathcal{C}_{0}(G) \backslash\{\gamma\}$. Clearly, $\Gamma_{1} f_{\gamma}=0$ for every $\gamma \in \mathcal{C}_{0}(G)$. Thus, setting

$$
f=\sum_{\gamma \in \mathcal{C}_{0}(G)} \widehat{f}(\gamma) f_{\gamma}
$$

for a given $\widehat{f} \in H$, we clearly have $\Gamma_{0} f=\widehat{f}$ and $\Gamma_{1} f=0$.



(ii) Let us first show that (6.10) holds true for all $f \in \operatorname{dom}(\mathcal{H}) \cap H^{1}(G)$ if $g=f_{\gamma} \in H^{1}(G)$. Take a compact exhaustion $\left(F_{k}\right)$ of $G$. Then by Lemma 6.1,

$$
\begin{aligned}
\left\langle\mathcal{H} f, f_{\gamma}\right\rangle_{L^{2}(G)}-\left\langle f^{\prime}, f_{\gamma}^{\prime}\right\rangle_{L^{2}(G)} & =\lim _{k \rightarrow \infty}\left\langle\mathcal{H} f, f_{\gamma}\right\rangle_{L^{2}\left(F_{k}\right)}-\left\langle f^{\prime}, f_{\gamma}^{\prime}\right\rangle_{L^{2}\left(F_{k}\right)} \\
& =\lim _{k \rightarrow \infty} \sum_{v \in \partial F_{k}} \frac{\partial f}{\partial n_{F_{k}}}(v) f_{\gamma}(v)^{*}=\lim _{k \rightarrow \infty} \sum_{v \in \partial F_{k} \cap V_{\gamma}} \frac{\partial f}{\partial n_{F_{k}}}(v)
\end{aligned}
$$

where $V_{\gamma}$ is the set of vertices of $G_{\gamma}$. Notice that the subgraph $G_{\gamma}$ itself is a connected infinite graph having finite total volume and exactly one end, which can be identified with $\gamma$ in an obvious way. Moreover, setting $F_{k}^{\gamma}:=F_{k} \cap G_{\gamma}$ for all $k \geq 0$ and noting that $F_{k}^{\gamma}$ is connected for all sufficiently large $k$, the sequence $\left(F_{k}^{\gamma}\right)$ provides a compact exhaustion of $G_{\gamma}$. Since $\partial_{G_{\gamma}} F_{k}^{\gamma}=\partial F_{k} \cap V_{\gamma}$ and

$$
\frac{\partial f}{\partial n_{F_{k}^{\gamma}}}(v)=\frac{\partial f}{\partial n_{F_{k}}}(v), \quad v \in \partial_{G_{\gamma}} F_{k}^{\gamma}
$$

for all large enough $k \geq 0$, we get by applying Lemma 6.5

$$
\left\langle\mathcal{H} f, f_{\gamma}\right\rangle_{L^{2}(G)}-\left\langle f^{\prime}, f_{\gamma}^{\prime}\right\rangle_{L^{2}(G)}=\lim _{k \rightarrow \infty} \sum_{v \in F_{k} \cap V_{\gamma}} \frac{\partial f}{\partial n_{F_{k}^{\gamma}}}(v)=-\frac{\partial f}{\partial n}(\gamma)
$$

Hence (6.10) holds true if $g=f_{\gamma} \in H^{1}(G)$.
Now observe that a simple integration by parts implies that (6.10) is valid for all compactly supported $g \in H^{1}(G)$. By continuity and Theorem 3.12 this extends further to all $g \in H_{0}^{1}(G)$. Finally, setting $\tilde{g}:=g-\sum_{\gamma \in \mathcal{C}_{0}(G)} g(\gamma) f_{\gamma}$ for $g \in H^{1}(G)$, it is immediate to check that, by Theorem $3.12, \tilde{g} \in H_{0}^{1}(G)$. It remains to use the linearity of $\Gamma_{0}$.

It turns out that the domain of the Neumann extension admits a simple description.

Corollary 6.7. Let $G$ be a metric graph with $\# \mathcal{C}_{0}(G)<\infty$. Then the Neumann extension $\mathcal{H}_{N}$ is given as the restriction $\mathcal{H}_{N}=\mathcal{H}_{\mid \operatorname{dom}\left(\mathcal{H}_{N}\right)}$ to the domain

$$
\operatorname{dom}\left(\mathcal{H}_{N}\right)=\left\{f \in \operatorname{dom}(\mathcal{H}) \cap H^{1}(G) \mid \Gamma_{1} f=0\right\}
$$

Proof. By the first representation theorem [50, Chapter VI.2.1], $\operatorname{dom}\left(\mathcal{H}_{N}\right)$ consists of all functions $f \in H^{1}(G)$ such that there exists $h \in L^{2}(G)$ with

$$
\left\langle f^{\prime}, g^{\prime}\right\rangle_{L^{2}(G)}=\langle h, g\rangle_{L^{2}(G)}, \quad \text { for all } g \in H^{1}(G)
$$

Moreover, in this case $\mathcal{H}_{N} f:=h$. Taking into account Proposition 6.6 and the fact that $\mathcal{H}_{N}$ is a restriction of $\mathcal{H}$, we immediately arrive at (6.11).

Our next goal is to prove surjectivity of the normal derivative map.
Proposition 6.8. If $G$ is a metric graph with $\# \mathcal{C}_{0}(G)<\infty$, then the mapping $\Gamma_{1}$ is surjective.

In fact, Proposition 6.8 will follow from the following lemma.
Lemma 6.9. Suppose $G$ is a metric graph with $\operatorname{vol}(G)<\infty$ and only one end, $\mathcal{C}(G)=\{\gamma\}$. Then there exists $f \in \operatorname{dom}(\mathcal{H}) \cap H^{1}(G)$ such that

$$
\partial_{n} f(\gamma) \neq 0
$$



Proof. We will proceed by contradiction. Suppose that $\partial_{n} g(\gamma)=0$ for all $g \in$ $\operatorname{dom}(H) \cap H^{1}(\mathcal{G})$. Then, by Corollary $6.7, \operatorname{dom}\left(H_{F}\right) \subseteq \operatorname{dom}\left(H_{N}\right)=\operatorname{dom}(H) \cap$ $H^{1}(\mathcal{G})$. However, both $H_{F}$ and $H_{N}$ are self-adjoint restrictions of $H$ and hence $\operatorname{dom}\left(H_{F}\right)=\operatorname{dom}\left(H_{N}\right)$. Therefore, $H_{F}=H_{N}$ and their quadratic forms also coincide, which implies that $H_{0}^{1}(\mathcal{G})=H^{1}(\mathcal{G})$. This contradicts Corollary 3.13 and hence completes the proof.
Proof of Proposition 6.8. Let $\mathcal{G}_{\gamma}, \gamma \in C_{0}(\mathcal{G})$ be the subgraphs of $\mathcal{G}$ constructed in the proof of Proposition $6.6(\mathrm{i})$. Every $\mathcal{G}_{\gamma}$ is a connected graph with $\operatorname{vol}\left(\mathcal{G}_{\gamma}\right)<\infty$ and only one end, which can be identified with $\gamma$. Hence we can apply Lemma 6.9 to obtain a function $\tilde{g}_{\gamma} \in \operatorname{dom}\left(H_{\gamma}\right) \cap H^{1}\left(\mathcal{G}_{\gamma}\right)$ such that $\partial_{n} \tilde{g}_{\gamma}(\gamma)=1$. Here $H_{\gamma}$ denotes the Kirchhoff Laplacian on $\mathcal{G}_{\gamma}$.

Since $\# \partial \mathcal{G}_{\gamma}<\infty$, we can obviously extend $\tilde{g}_{\gamma}$ to a function $g_{\gamma}$ on $\mathcal{G}$ such that $g_{\gamma} \in \operatorname{dom}(H) \cap H^{1}(\mathcal{G})$ and $g_{\gamma}$ is identically zero on a neighborhood of each end $\gamma^{\prime} \neq$ $\gamma$ (see also the proof of Theorem 3.10). In particular, this implies that $\partial_{n} g_{\gamma}\left(\gamma^{\prime}\right)=0$ for all $\gamma^{\prime} \in C_{0}(\mathcal{G}) \backslash\{\gamma\}$. Upon identification of $\gamma$ with the single end of $\mathcal{G}_{\gamma}$ we also have that

$$
\partial_{n} g_{\gamma}(\gamma)=\partial_{n} \tilde{g}_{\gamma}(\gamma)=1
$$

This immediately implies surjectivity.
6.3. Description of self-adjoint extensions. Our next goal is a description of all finite energy self-adjoint extensions of $H_{0}$, that is, self-adjoint extensions $\widetilde{H}$ satisfying the inclusion $\operatorname{dom}(\widetilde{H}) \subset H^{1}(\mathcal{G})$. We will be able to do this under the additional assumption that $\mathcal{G}$ has finitely many finite volume ends. Recall that in this case $\mathcal{H}=\ell^{2}\left(C_{0}(\mathcal{G})\right)$ is a finite dimensional Hilbert space.

Let $C, D$ be two linear operators on $\mathcal{H}$ satisfying Rofe-Beketov conditions [68]:

$$
C D^{*}=D C^{*}, \quad \operatorname{rank}(\underbrace{C \mid D}_{cal})=\operatorname{dim} \mathcal{H}=\# C_{0}(\mathcal{G})
$$

Consider the quadratic form $t_{C, D}$ defined by

$$
t_{C, D}[f]:=\int_{\mathcal{G}}\left|f^{\prime}(x)\right|^{2} d x+\left\langle D^{-1} C \Gamma_{0} f, \Gamma_{0} f\right\rangle_{\mathscr{H}}
$$

on the domain

$$
\operatorname{dom}\left(t_{C, D}\right):=\left\{f \in H^{1}(\mathcal{G}) \mid \Gamma_{0} f \in \operatorname{ran}\left(D^{*}\right)\right\}
$$

Here and in the following the mappings $\Gamma_{0}$ and $\Gamma_{1}$ are given by (6.9) and $D^{-1}: \operatorname{ran}(D) \rightarrow$ $\operatorname{ran}\left(D^{*}\right)$ denotes the inverse of the restriction $\left.D\right|_{\operatorname{ker}(D)^{\perp}}: \operatorname{ran}\left(D^{*}\right) \rightarrow \operatorname{ran}(D)$. In particular, (6.12) implies that $t_{C, D}[f]$ is well-defined for all $f \in \operatorname{dom}\left(t_{C, D}\right)$ (see also (A.4)).

Remark 6.10. It is straightforward to check that $t_{I, 0}=t_{F}$ and $t_{0, I}=t_{N}$ are the quadratic forms corresponding to the Friedrichs extension $H_{F}$ and, respectively, Neumann extension $H_{N}$ (see Remark 3.1 and (5.5)).

Now we are in position to state the main result of this section.
Theorem 6.11. Let $\mathcal{G}$ be a metric graph with finitely many finite volume ends, $\# C_{0}(\mathcal{G})<\infty$. Let also $C, D$ be linear operators on $\mathcal{H}$ satisfying Rofe-Beketov conditions (6.12). Then:
(i) The form $t_{C, D}$ given by (6.13), (6.14) is closed and lower semi-bounded in $L^{2}(\mathcal{G})$.



(ii) The self-adjoint operator $H_{C, D}$ associated with the form $\mathfrak{t}_{C, D}$ is a self-adjoint extension of $H_{0}$ and its domain is explicitly given by

$$
\operatorname{dom}\left(H_{C, D}\right)=\left\{f \in \operatorname{dom}(H) \cap H^{1}(G) \mid C \Gamma_{0} f+D \Gamma_{1} f=0\right\}
$$

(iii) Conversely, if $\widetilde{H}$ is a self-adjoint extension of $H_{0}$ such that $\operatorname{dom}(\widetilde{H}) \subset H^{1}(G)$, then there are $C, D$ satisfying (6.12) such that $\widetilde{H}=H_{C, D}$.
(iv) Moreover, $\widetilde{H}=H_{C, D}$ is a Markovian extension if and only if the corresponding quadratic form $\widehat{\mathfrak{t}}_{C, D}[y]=\left\langle D^{-1} C y, y\right\rangle_{\mathcal{H}}, \operatorname{dom}(\widehat{\mathfrak{t}})=\operatorname{ran}\left(D^{*}\right)$ is a Dirichlet form on $\mathcal{H}$ in the wide sense. ${ }^{\dagger}$

Proof. (i) Since $H$ is finite dimensional, it is straightforward to see that the form $\mathfrak{t}_{C, D}$ is closed and lower semi-bounded in $L^{2}(G)$ whenever $C$ and $D$ satisfy (6.12).
(ii) By the first representation theorem [50, Chapter VI.2.1], $\operatorname{dom}\left(H_{C, D}\right)$ consists of all functions $f \in \operatorname{dom}\left(\mathfrak{t}_{C, D}\right) \subseteq H^{1}(G)$ for which there exists $h \in L^{2}(G)$ such that

$$
\left\langle f^{\prime}, g^{\prime}\right\rangle_{L^{2}(G)}+\left\langle D^{-1} C \Gamma_{0} f, \Gamma_{0} g\right\rangle_{\mathcal{H}}=\langle h, g\rangle_{L^{2}(G)}
$$

for all $g \in \operatorname{dom}\left(\mathfrak{t}_{C, D}\right)$. Moreover, in this case $H_{C, D} f:=h$.
The Gauss-Green identity (6.10) implies that for any $f \in \operatorname{dom}\left(H_{C, D}\right)$ and $g \in$ $\operatorname{dom}\left(\mathfrak{t}_{C, D}\right)$

$$
\left\langle D^{-1} C \Gamma_{0} f, \Gamma_{0} g\right\rangle_{\mathcal{H}}=-\left\langle\Gamma_{1} f, \Gamma_{0} g\right\rangle_{\mathcal{H}}
$$

Taking into account the surjectivity property in Proposition 6.6(i), the inclusion " $\subseteq$ " in (6.15) follows. The converse inclusion is then an immediate consequence of the Gauss-Green identity (6.10).
(iii) To prove the claim, it suffices to show that

$$
\Theta=\left\{\left(\Gamma_{0} f, \Gamma_{1} f\right) \mid f \in \operatorname{dom}(\widetilde{H})\right\} \subseteq \mathcal{H} \times \mathcal{H}
$$

is a self-adjoint linear relation (for further details we refer to Appendix A). By definition, $\Theta^{*}$ is given by

$$
\Theta^{*}=\left\{(g, h) \in \mathcal{H} \times \mathcal{H} \mid\left\langle\Gamma_{1} f, g\right\rangle_{\mathcal{H}}=\left\langle\Gamma_{0} f, h\right\rangle_{\mathcal{H}} \text { for all } f \in \operatorname{dom}(\widetilde{H})\right\}
$$

The inclusion $\Theta \subseteq \Theta^{*}$ follows immediately from the Gauss-Green identity (6.10) and the self-adjointness of $\widetilde{H}$. Indeed, we clearly have

$$
0=\langle\widetilde{H} f, \tilde{f}\rangle_{L^{2}(G)}-\langle f, \widetilde{H} \tilde{f}\rangle_{L^{2}(G)}=-\left\langle\Gamma_{1} f, \Gamma_{0} \tilde{f}\right\rangle_{\mathcal{H}}+\left\langle\Gamma_{0} f, \Gamma_{1} \tilde{f}\right\rangle_{\mathcal{H}}
$$

for all functions $f, \tilde{f} \in \operatorname{dom}(\widetilde{H})$. On the other hand, by Proposition 6.8 and Proposition 6.6 , for any $(g, h) \in \Theta^{*}$ there is a function $\tilde{f} \in \operatorname{dom}(H) \cap H^{1}(G)$ such that $g=\Gamma_{0} \tilde{f}$ and $h=\Gamma_{1} \tilde{f}$. Employing the identity (6.10) once again, we see that

$$
\begin{aligned}
\langle\widetilde{H} f, \tilde{f}\rangle_{L^{2}(G)} & =\left\langle f^{\prime}, \tilde{f}^{\prime}\right\rangle_{L^{2}(G)}-\left\langle\Gamma_{1} f, g\right\rangle_{\mathcal{H}} \\
& =\left\langle f^{\prime}, \tilde{f}^{\prime}\right\rangle_{L^{2}(G)}-\left\langle\Gamma_{0} f, h\right\rangle_{\mathcal{H}}=\langle f, H \tilde{f}\rangle_{L^{2}(G)}
\end{aligned}
$$

for all $f \in \operatorname{dom}(\widetilde{H})$. Hence, $\tilde{f} \in \operatorname{dom}(\widetilde{H})$ and in particular $(g, h) \in \Theta$. Since $\Theta$ is self-adjoint, there are $C$ and $D$ in $\mathcal{H}$ satisfying Roĭfesh-Beketov conditions (6.12) and such that $\Theta=\{(f, g) \in \mathcal{H} \times \mathcal{H} \mid C f+D g=0\}$.

[^0]
[^0]:    ${ }^{\dagger}$ Here we do not assume that $\widehat{\mathfrak{t}}$ is densely defined, see [31, p.29]. We stress that in order for $\widehat{\mathfrak{t}}$ to be a Dirichlet form even merely in the wide sense, it is necessary that $\operatorname{dom}(\widehat{\mathfrak{t}})$ is a sublattice of $\mathcal{H}$, hence that the orthogonal projector onto $\operatorname{ran}\left(D^{*}\right)$ is a positivity preserving operator.



(iv) The first direction of the equivalence is clear: since the quadratic form $t_{N}$ associated with the Neumann extension $H_{N}$ is Markovian and

$$
\Gamma_{0}(\varphi \circ f)=((\varphi \circ f)(\gamma))_{\gamma \in \mathcal{C}_{0}(G)}=: \varphi \circ\left(\Gamma_{0} f\right)
$$

for all functions $f \in H^{1}(G)$ and every normal contraction $\varphi$, $\dagger$ the extension $H_{C, D}$ is Markovian if $\widehat{t}_{C, D}$ is a Dirichlet form on $\mathcal{H}$ in the wide sense.
To prove the converse direction, let, for simplicity, $f \in \operatorname{dom}\left(\widehat{t}_{C, D}\right)$ be real-valued and fix some real-valued $\tilde{f} \in H^{1}(G)$ with $\Gamma_{0} \tilde{f}=f$ (the existence of such an $\tilde{f}$ follows from Proposition 6.6). For any (real-valued) normal contraction $\varphi: \mathbb{R} \rightarrow \mathbb{R}$, we can construct a continuous and piecewise affine function $\psi: \mathbb{R} \rightarrow \mathbb{R}$ (i.e., $\psi$ is affine on every component of $\mathbb{R} \backslash\left\{x_{1}, \ldots, x_{M}\right\}$ for finitely many points $\left.x_{1}, \ldots, x_{M}\right)$ such that $\psi(0)=0, \psi(f(\gamma))=\varphi(f(\gamma))$ for all $\gamma \in \mathcal{C}_{0}(G)$ and $\left|\psi^{\prime}(x)\right|=1$ for almost every $x \in \mathbb{R} . \ddagger$ Notice that every function $\psi$ with the above properties is a normal contraction. Hence, if $t_{C, D}$ is Markovian, it follows that $\psi \circ \tilde{f} \in \operatorname{dom}\left(t_{C, D}\right)$. However, its boundary values are precisely given by

$$
\Gamma_{0}(\psi \circ \tilde{f})=\psi \circ f=\varphi \circ f
$$

and we conclude that $\varphi \circ f$ belongs to $\operatorname{dom}\left(\widehat{t}_{C, D}\right)$. Finally, the Markovian property of $t_{C, D}$ implies that

$$
t_{C, D}[\psi \circ \tilde{f}]=\int_{G}\left|(\psi \circ \tilde{f})^{\prime}\right|^{2} \mathrm{~d} x+\widehat{t}_{C, D}[\varphi \circ f] \leq t_{C, D}[\tilde{f}]=\int_{G}\left|\tilde{f}^{\prime}\right|^{2} \mathrm{~d} x+\widehat{t}_{C, D}[f],
$$

and noticing that $\left|(\psi \circ \tilde{f})^{\prime}\right|=\left|\tilde{f}^{\prime}\right|$ almost everywhere on $G$, the proof is complete.
Let us demonstrate Theorem 6.11 by applying it to Cayley graphs.
Corollary 6.12. Let $G_{d}$ be a Cayley graph of a finitely generated group $G$ with one end. Then the Kirchhoff Laplacian $H_{0}$ admits a unique Markovian extension if and only if the underlying metric graph $G=\left(G_{d},|\cdot|\right)$ has infinite total volume, $\operatorname{vol}(G)=\infty$. Moreover, if $G$ has finite total volume, then the set of all Markovian extensions of $H_{0}$ forms a one-parameter family given explicitly by

$$
\operatorname{dom}\left(H_{\theta}\right)=\left\{f \in \operatorname{dom}(H) \cap H^{1}(G) \mid \cos (\theta) \Gamma_{0} f+\sin (\theta) \Gamma_{1} f=0\right\}
$$

where $\theta \in[0, \pi / 2]$.
Taking into account that amenable groups have finitely many ends, the above result applies to amenable finitely generated groups, which are not virtually infinite cyclic (see Remark 2.5(iv)). In a similar way one can obtain a complete description of Markovian extensions in the case of virtually infinite cyclic groups, however, they have two ends and the corresponding description looks a little bit more cumbersome and we leave it to the reader (cf. [31, p.147]). The case of groups with infinitely many ends remains an open highly nontrivial problem.

Remark 6.13. A few remarks are in order.
$\dagger \mathrm{A}$ normal contraction is a function $\varphi: \mathbb{C} \rightarrow \mathbb{C}$ such that $\varphi(0)=0$ and $|\varphi(x)-\varphi(y)| \leq|x-y|$ for all $x, y \in \mathbb{C}$.
$\ddagger$ For instance, for any $s, L>0$ such that $s \leq L$, the function $\psi_{0}(x):=\frac{L+s}{2}-\left|x-\frac{L+s}{2}\right|$ satisfies $\psi_{0}(0)=0, \psi_{0}(L)=s$ and $\left|\psi_{0}^{\prime}\right| \equiv 1$. The construction in the general case follows easily from this example.



(i) Let us mention that in the case when the domain of the maximal operator $H$ is contained in $H^{1}(G)$ and $G$ has finitely many finite volume ends (notice that by Theorem 4.1 in this case $n_{ \pm}\left(H_{0}\right)=\# \mathcal{C}_{0}(G)<\infty$ ), Proposition 6.11 provides a complete description of all self-adjoint extensions of $H_{0}$. Let us also mention that Proposition 6.11 provides a complete description of all self-adjoint restrictions of the Gaffney Laplacian $H_{G}$, see Remark 5.6(ii).
(ii) Some of the results of this section extend (to a certain extent) to the case of infinitely many ends. Let us stress that by Proposition 4.9 in the case when $G$ has a finite volume end which is not free the above results would lead only to some (not all!) self-adjoint extensions of $H_{0}$. In our opinion, even in the case of radially symmetric trees having finite total volume the description of all self-adjoint extensions of $H_{0}$ is a difficult problem.
(iii) Similar relations between Markovian realizations of elliptic operators on domains or finite metric graphs (with general couplings at the vertices) on one hand, and Dirichlet property of the corresponding quadratic form's boundary term on the other hand, are of course well known in the literature (see, e.g., [14, Proposition 5.1], [47, Theorem 3.5], [57, Theorem 6.1]). However, the setting of infinite metric graphs additionally requires much more advanced considerations of combinatorial and topological nature. In particular, it seems noteworthy to us that the results of the previous sections provide the right notion of the boundary for metric graphs, namely, the set of finite volume ends, to deal with finite energy and also with Markovian extensions of the minimal Kirchhoff Laplacian. In particular, this end space is well-behaved as concerns the introduction of traces and normal derivatives.
(iv) Taking into account certain close relationships between quantum graphs and discrete Laplacians (see $[27, \S 4]$ ), one can easily obtain the results analogous to Theorem 4.1 and Theorem 6.11 for a particular class of discrete Laplacians on $G_{d}$ defined by the following expression

$$
(\tau f)(v):=\frac{1}{m(v)} \sum_{u \sim v} \frac{f(v)-f(u)}{\left|e_{u, v}\right|}, \quad v \in V
$$

where $m$ is the star weight (2.12). Markovian extensions of weighted discrete Laplacians were considered also in [52]. On the other hand, [52] does not contain a finiteness assumption, however, the conclusion in our setting appears to be slightly stronger than in [52, Theorem 3.5], where the correspondence between Markovian extensions and Markovian forms on the boundary is in general not bijective.

# 7. Deficiency indices of antitrees 

The main aim of this section is to construct for any $N \in \mathbb{Z}_{\geq 1} \cup\{\infty\}$ a metric antitree such that the corresponding minimal Kirchhoff Laplacian $H_{0}$ has deficiency indices $n_{ \pm}\left(H_{0}\right)=N$. Our motivation stems from the fact that every antitree has exactly one end and hence, according to considerations in the previous sections, $H_{0}$ admits at most one-parameter family of Markovian extensions.
7.1. Antitrees. Let $G_{d}=(V, E)$ be a connected, simple combinatorial graph. Fix a root vertex $o \in V$ and then order the graph with respect to the combinatorial spheres $S_{n}, n \geq 0$ (notice that $S_{0}=\{o\}$ ). $G_{d}$ is called an antitree if every vertex in





Figure 1. Antitree with sphere numbers $s_{n}=n+1$.
$S_{n}, n \geq 1$, is connected to all vertices in $S_{n-1}$ and $S_{n+1}$ and no vertices in $S_{k}$ for all $|k-n| \neq 1$ (see Figure 1). Notice that each antitree is uniquely determined by its sequence of sphere numbers $\left(s_{n}\right), s_{n}:=\# S_{n}$ for $n \geq 0$.

While antitrees first appeared in connection with random walks [25, 54, 77], they were actively studied from various different perspectives in the last years (see [11, 22, 56] for quantum graphs and [21, Section 2] for further references).

Let us enumerate the vertices in every combinatorial sphere $S_{n}$ by $\left(v_{i}^{n}\right)_{i=1}^{s_{n}}$ and denote the edge connecting $v_{i}^{n}$ with $v_{j}^{n+1}$ by $e_{i j}^{n}, 1 \leq i \leq s_{n}, 1 \leq j \leq s_{n+1}$. We shall always use $\mathcal{A}$ to denote (metric) antitrees.

It is clear that every (infinite) antitree has exactly one end. By Theorem 4.1, the deficiency indices of the corresponding minimal Kirchhoff Laplacian are at least 1 if $\operatorname{vol}(\mathcal{A})<\infty$. On the other hand, under the additional symmetry assumption that $\mathcal{A}$ is radially symmetric (that is, for each $n \geq 0$, all edges connecting combinatorial spheres $S_{n}$ and $S_{n+1}$ have the same length), it is known that the deficiency indices are at most 1 (see [56, Theorem 4.1] and Example 4.11). It turns out that upon removing the symmetry assumption it is possible to construct antitrees such that the corresponding minimal Kirchhoff Laplacian has arbitrary finite or infinite deficiency indices. More precisely, the main aim of this section is to prove the following result.

Theorem 7.1. Let $\mathcal{A}$ be the antitree with sphere numbers $s_{n}=n+1, n \geq 0$ (Figure 1). Then for each $N \in \mathbb{Z}_{\geq 1} \cup\{\infty\}$ there are edge lengths such that the corresponding minimal Kirchhoff Laplacian $H_{0}$ has the deficiency indices $n_{ \pm}\left(H_{0}\right)=$ $N$.
7.2. Harmonic functions. As it was mentioned already, every harmonic function is uniquely determined by its values at the vertices. On the other hand, $f \in C(V)$ defines a function $\mathfrak{f} \in \mathcal{H}(\mathcal{A})$ with $\left.\mathfrak{f}\right|_{V}=f$ if and only if the following conditions are satisfied:

$$
\sum_{j=1}^{s_{n+1}} \frac{f\left(v_{j}^{n+1}\right)-f\left(v_{k}^{n}\right)}{\left|e_{k j}^{n}\right|}+\sum_{i=1}^{s_{n-1}} \frac{f\left(v_{i}^{n-1}\right)-f\left(v_{k}^{n}\right)}{\left|e_{i k}^{n-1}\right|}=0
$$

at each $v_{k}^{n}, 1 \leq k \leq s_{n}$ with $n \geq 0$. We set $s_{-1}:=0$ for notational simplicity and hence the second summand in (7.1) is absent when $n=0$. We can put the above difference equations into the more convenient matrix form. Denote $\mathfrak{f}_{n}:=\left.\mathfrak{f}\right|_{S_{n}}=$



$\left(f\left(v_{i}^{n}\right)\right)_{s_{i=1}^{n}}$ for all $n \in \mathbb{Z}_{\geq 0}$ and introduce matrices

$$
M_{n+1}:=\left(\begin{array}{cccc}
\frac{1}{\left|e_{11}^{n}\right|} & \frac{1}{\left|e_{12}^{n}\right|} & \ldots & \frac{1}{\left|e_{1 s_{n+1}}^{n}\right|} \\
\frac{1}{\left|e_{21}^{n}\right|} & \frac{1}{\left|e_{22}^{n}\right|} & \ldots & \frac{1}{\left|e_{2 s_{n+1}}^{n}\right|} \\
\ldots & \ldots & \ldots & \ldots \\
\frac{1}{\left|e_{s_{n} 1}^{n}\right|} & \frac{1}{\left|e_{s_{n} 2}^{n}\right|} & \ldots & \frac{1}{\left|e_{s_{n s_{n+1}}}^{n}\right|}
\end{array}\right) \in \mathbb{R}^{s_{n} \times s_{n+1}}
$$

and

$$
D_{n}:=\operatorname{diag}\left(d_{k}^{n}\right) \in \mathbb{R}^{s_{n} \times s_{n}}, \quad d_{k}^{n}:=\sum_{j=1}^{s_{n+1}} \frac{1}{\left|e_{k j}^{n}\right|}+\sum_{i=1}^{s_{n-1}} \frac{1}{\left|e_{i k}^{n-1}\right|}
$$

for all $n \in \mathbb{Z}_{\geq 0}$. Notice the following useful identity

$$
\begin{aligned}
d_{1}^{0}= & M_{1} 1_{s_{1}} \\
\left(\begin{array}{c}
d_{1}^{n} \\
\vdots \\
d_{s_{n}}^{n}
\end{array}\right) & =D_{n} 1_{s_{n}}=\left(M_{n+1} M_{n}^{*}\right)\binom{1_{s_{n+1}}}{1_{s_{n-1}}}, \quad n \geq 1
\end{aligned}
$$

where $1_{s_{n}}:=(1, \ldots, 1)^{\top} \in \mathbb{R}^{s_{n}}$. Hence (7.1) can be written as follows

$$
\begin{aligned}
& M_{1} f_{1}=\sum_{j=1}^{s_{1}} \frac{1}{\left|e_{1 j}^{0}\right|} f_{0}=d_{1}^{0} f_{0} \\
& M_{n+1} f_{n+1}=D_{n} f_{n}-M_{n}^{*} f_{n-1}, \quad n \geq 1
\end{aligned}
$$

Since $D_{n}$ is invertible, we get

$$
f_{n}=D_{n}^{-1}\left(M_{n+1} M_{n}^{*}\right)\binom{f_{n+1}}{f_{n-1}}
$$

for all $n \geq 1$. In particular, $f_{n} \in \operatorname{ran}\left(D_{n}^{-1}\left(M_{n+1} M_{n}^{*}\right)\right)$ for all $n \geq 1$, which implies that the number of linearly independent solutions to the above difference equations (and hence the number of linearly independent harmonic functions) depends on the ranks of the matrices $\left(M_{n+1} M_{n}^{*}\right), n \geq 1$. Let us demonstrate this by considering the following example.

Lemma 7.2. Let $\mathcal{A}$ be a radially symmetric antitree. Then

$$
\mathcal{H}(\mathcal{A})=\operatorname{span}\left\{1_{G}\right\}
$$

Proof. Let for each $n \geq 0$, all edges connecting combinatorial spheres $S_{n}$ and $S_{n+1}$ have the same length, say $\ell_{n}>0$. Clearly, in this case

$$
\operatorname{ran}\left(M_{n+1}\right)=\operatorname{ran}\left(M_{n}^{*}\right)=\operatorname{span}\left\{1_{s_{n}}\right\}
$$

for all $n \geq 1$. Moreover, each $D_{n}$ is a scalar multiple of the identity matrix $I_{s_{n}}$ and hence (7.7) implies that $f_{n}=c_{n} 1_{s_{n}}$ with some $c_{n} \in \mathbb{C}$ for all $n \geq 0$. Plugging this into (7.5)-(7.6), we get

$$
c_{1}=c_{0}, \quad c_{n+1}=c_{n}+\frac{s_{n-1} \ell_{n}}{s_{n+1} \ell_{n-1}}\left(c_{n}-c_{n-1}\right), \quad n \geq 1
$$

Hence $c_{n}=c_{0}=f(o)$ for all $n \geq 0$, which proves the claim.

The latter in particular implies the following statement (cf. [56, Theorem 4.1]).
Corollary 7.3. If $\mathcal{A}$ is a radial antitree with finite total volume, then $n_{ \pm}\left(H_{0}\right)=1$.



Proof. By Corollary 2.11, we only need to show that $n^{ \pm}\left(H_{0}\right) \leq 1$. However,

$$
n^{ \pm}\left(H_{0}\right)=\operatorname{dim}(\operatorname{ker}(H)) \leq \operatorname{dim}(H(A))=1
$$

7.3. Finite deficiency indices. We restrict our further considerations to a special case of polynomially growing antitrees. Namely, for every $N \in \mathbb{Z}_{\geq 1}$, the antitree $A_{N}$ has sphere numbers $s_{0}=1$ and $s_{n}:=n+N$ for all $n \in \mathbb{Z}_{\geq 1}$. To define its lengths, pick a sequence of positive numbers $\left(\ell_{n}\right)$ and set

$$
\left|e_{i j}^{n}\right|:=\left\{\begin{array}{cl}
2 \ell_{n}, & \text { if } 1 \leq i=j \leq N, \\
\ell_{n}, & \text { otherwise }
\end{array} \quad \text { for all } n \in \mathbb{Z}_{\geq 0}\right.
$$

Lemma 7.4. If a metric antitree $A_{N}$ has lengths given by (7.9), then

$$
\operatorname{dim} H\left(A_{N}\right)=N+1
$$

Proof. Denoting

$$
B_{n, m}:=\left(\begin{array}{cccc}
1 & 1 & \ldots & 1 \\
1 & 1 & \ldots & 1 \\
\cdots & \cdots & \cdots & \cdots \\
1 & 1 & \ldots & 1
\end{array}\right) \in \mathbb{R}^{n \times m}, \quad B_{n}:=B_{n, n} \in \mathbb{R}^{n \times n}
$$

we get the following block-matrix form of the matrices $M_{n+1}$ :

$$
M_{n+1}=\frac{1}{\ell_{n}}\left(\begin{array}{cc}
B_{N}-\frac{1}{2} I_{N} & B_{N, n+1} \\
B_{n, N} & B_{n, n+1}
\end{array}\right)
$$

for all $n \geq 1$. Taking into account (7.3) and denoting

$$
d_{n}^{1}:=\frac{n+N-3 / 2}{\ell_{n-1}}+\frac{n+N+1 / 2}{\ell_{n}}, \quad d_{n}^{2}:=\frac{n+N-1}{\ell_{n-1}}+\frac{n+N+1}{\ell_{n}}
$$

we get

$$
D_{n}=\left(\begin{array}{cc}
d_{n}^{1} I_{N} & 0 \\
0 & d_{n}^{2} I_{n}
\end{array}\right)
$$

for all $n \geq 2$. Since $M_{1} \in \mathbb{C}^{1 \times(N+1)}$ and

$$
\operatorname{ran}\left(M_{n+1}\right)=\operatorname{ran}\left(M_{n}^{*}\right)=\operatorname{span}\left\{\binom{f_{N}}{\mathbf{1}_{n}} \mid f_{N} \in \mathbb{C}^{N}\right\}
$$

for all $n \geq 2$, (7.7) implies that every $f$ solving (7.5)-(7.6) must be of the form

$$
f_{n}=\binom{f_{n}^{N}}{c_{n} \mathbf{1}_{n}} \in \mathbb{C}^{N+n}, \quad f_{n}^{N} \in \mathbb{C}^{N}, \quad c_{n} \in \mathbb{C}
$$

for all $n \geq 1$. Plugging (7.15) into (7.6) and taking into account that

$$
B_{N} f_{n}^{N}=f_{n}^{\boldsymbol{N}} \mathbf{1}_{N}, \quad f_{n}^{\boldsymbol{N}}:=\left\langle f_{n}^{\boldsymbol{N}}, \mathbf{1}_{N}\right\rangle=B_{1, N} f_{n}^{N}
$$

we get after straightforward calculations

$$
\begin{aligned}
& \widetilde{f}_{n+1}^{\boldsymbol{N}}+\frac{c_{n+1}(n+1)}{\ell_{n}} \mathbf{1}_{N}-\frac{1}{2 \ell_{n}} f_{n+1}^{\boldsymbol{N}}=d_{n}^{1} f_{n}^{N}-f_{n-1}^{\boldsymbol{N}}+\frac{c_{n-1}(n-1)}{\ell_{n-1}} \mathbf{1}_{N}+\frac{1}{2 \ell_{n-1}} f_{n-1}^{\boldsymbol{N}} \\
& \widetilde{f}_{n+1}^{\boldsymbol{N}}+\frac{c_{n+1}(n+1)}{\ell_{n}}=c_{n} d_{n}^{2}-f_{n-1}^{\boldsymbol{N}}+\frac{c_{n-1}(n-1)}{\ell_{n-1}}
\end{aligned}
$$



for all $n \geq 2$. Multiplying (7.17) with $\mathbf{1}_{N}$ and then subtracting (7.16), we end up with

$$
f_{n+1}^{N}=2 \ell_{n}\left(c_{n} d_{n}^{2} \boldsymbol{1}_{N}-d_{n}^{1} f_{n}^{N}\right)-\frac{\ell_{n}}{\ell_{n-1}} f_{n-1}^{N}, \quad n \geq 2
$$

Next taking the inner product in (7.16) with $\mathbf{1}_{N}$ and then subtracting (7.17) multiplied by $N^{-1 / 2}$, we finally get

$$
c_{n+1}=\frac{\ell_{n}}{n+1}\left(2 d_{n}^{1} f_{n}^{N}-(2 N-1) d_{n}^{2} c_{n}\right)-c_{n-1} \frac{(n-1) \ell_{n}}{(n+1) \ell_{n-1}}, \quad n \geq 2
$$

Taking into account that the value of $f$ at the root $o$ is determined by $f_{1}$ via

$$
f(o)=f_{0}=\frac{2 \ell_{0}}{2 N+1} M_{1} f_{1}
$$

and noting that $f_{2}^{N}$ and $c_{2}$ are also determined by $f_{1}$, we conclude that (7.18)-(7.19) define $f$ uniquely once $f_{1} \in \mathbb{C}^{N+1}$ is given.

Lemma 7.4 immediately implies that $n_{ \pm}\left(H_{0}\right) \leq N+1$ if $\operatorname{vol}\left(\mathcal{A}_{N}\right)<\infty$, where $H_{0}$ is the associated minimal operator. The next result shows that it can happen that $n_{ \pm}\left(H_{0}\right)=N+1$ upon choosing lengths $\ell_{n}$ with a sufficiently fast decay.

Proposition 7.5. Let $\mathcal{A}_{N}$ be the antitree as in Lemma 7.4. If $\left(\ell_{n}\right)$ is decreasing and

$$
\sqrt{\ell_{n}}=O\left(\frac{1}{(6 \sqrt{N})^{n}(n+N+3)!}\right)
$$

as $n \rightarrow \infty$, then $n_{ \pm}\left(H_{0}\right)=N+1$.
Proof. It is immediate to see that $\operatorname{vol}\left(\mathcal{A}_{N}\right)<\infty$ if (7.21) is satisfied. Next, taking into account (7.9), observe that

$$
m(v)=\sum_{v \in \mathcal{E}_{v}}|e| \leq(n+N) \ell_{n-1}+(n+N+2) \ell_{n} \lesssim n \ell_{n-1}, \quad v \in \mathcal{S}_{n}
$$

as $n \rightarrow \infty$. Suppose $f \in H(\mathcal{A})$ and set $f=\left.f\right|_{V}$. Then $f$ has the form (7.15) and hence

$$
\left\|f_{n}\right\|^{2}=\sum_{v \in \mathcal{S}_{n}}|f(v)|^{2}=\left\|f_{n}^{N}\right\|^{2}+n\left|c_{n}\right|^{2}
$$

for all $n \geq 1$. This implies the following estimate

$$
\sum_{v \in V}|f(v)|^{2} m(v)=\sum_{n \geq 0} \sum_{v \in \mathcal{S}_{n}}|f(v)|^{2} m(v) \lesssim \sum_{n \geq 1} n^{2} \ell_{n-1}\left(\left\|f_{n}^{N}\right\|^{2}+\left|c_{n}\right|^{2}\right)
$$

Next, (7.18)-(7.19) can be written as follows

$$
\binom{f_{n+1}^{N}}{c_{n+1}}=A_{1, n}\binom{f_{n}^{N}}{c_{n}}+A_{2, n}\binom{f_{n-1}^{N}}{c_{n-1}}
$$

where the matrices $A_{1, n}, A_{2, n} \in \mathbb{R}^{(N+1) \times(N+1)}$ are given explicitly by

$$
A_{1, n}:=\left(\begin{array}{cc}
-2 \ell_{n} d_{n}^{1} \mathbb{I}_{N} & 2 \ell_{n} d_{n}^{2} \mathbb{B}_{N, 1} \\
2 \ell_{n} d_{n}^{1} \frac{n+1}{n+1} \mathbb{B}_{1, N} & -(2 N-1) \ell_{n} d_{n}^{2} \frac{n+1}{n+1} \mathbb{I}_{1}
\end{array}\right), \quad A_{2, n}:=-\frac{\ell_{n}}{\ell_{n-1}}\left(\begin{array}{cc}
\mathbb{I}_{N} & 0 \\
0 & \frac{n-1}{n+1} \mathbb{I}_{1}
\end{array}\right)
$$

for all $n \geq 2$. Since $\ell_{n-1} \leq \ell_{n}$ and

$$
d_{n}^{1}<d_{n}^{2}=\frac{n+N-1}{\ell_{n-1}}+\frac{n+N+1}{\ell_{n}} \leq \frac{2(n+N)}{\ell_{n}}
$$



for all $n \geq 2$, it is not difficult to get the following rough bounds ${ }^{\dagger}$

$$
\left\|A_{1, n}\right\| \leq 6 \sqrt{N}(n+N), \quad\left\|A_{2, n}\right\|=\frac{\ell_{n}}{\ell_{n-1}} \leq 1
$$

for all $n \geq 2 N$. Denoting

$$
F_{n}:=\binom{f_{n}^{N}}{c_{n}}, \quad n \geq 1
$$

the recurrence relations (7.18)-(7.19) can be written in the following matrix form

$$
\binom{F_{n+1}}{F_{n}}=\left(\begin{array}{cc}
A_{1, n} & A_{2, n} \\
I_{N+1} & 0_{N+1}
\end{array}\right)\binom{F_{n}}{F_{n-1}}=A_{n}\binom{F_{n}}{F_{n-1}}
$$

Taking into account (7.26), we get $\left\|A_{n}\right\| \leq 6 \sqrt{N}(n+N+1)$ for all $n \geq 2 N$, which implies the estimate

$$
\sqrt{\left\|f_{n}^{N}\right\|^{2}+\left|c_{n}\right|^{2}}=\left\|F_{n}\right\| \leq C \prod_{k=1}^{n-1}\left\|A_{k}\right\| \lesssim(6 \sqrt{N})^{n}(n+N)来宾
$$

for all $n \geq 2$. Combining this bound with $(7.21)$, it is easy to see that the series on the right hand side in (7.22) converges and hence by Lemma 2.13 we conclude that $\mathcal{H}\left(\mathcal{A}^{N}\right) \subset L^{2}(\mathcal{A})$. Thus $\operatorname{ker}(\mathcal{H})=\mathcal{H}\left(\mathcal{A}^{N}\right)$ and the use of Corollary 2.11 finishes the proof.
7.4. Infinite deficiency indices. Consider the antitree $\mathcal{A}$ with sphere numbers $s_{n}:=n+1, n \geq 0$. Next pick a sequence of positive numbers $\left(\ell_{n}\right)$ and define lengths as follows

$$
\left|e_{i j}^{n}\right|= \begin{cases}2 \ell_{n}, & 1 \leq i=j \leq n+1 \\ \ell_{n}, & \text { otherwise }\end{cases}
$$

for all $n \in \mathbb{Z}_{\geq 0}$. Thus, the corresponding matrix $M_{n+1}$ given by (7.2) has the form

$$
M_{n+1}=\frac{1}{\ell_{n}}\left(B_{n+1}-\frac{1}{2} I_{n+1} \quad B_{n+1,1}\right) \in \mathbb{R}^{(n+1) \times(n+2)}
$$

for all $n \geq 0$. Let us denote this antitree by $\mathcal{A}^{\infty}$.
Lemma 7.6. $\operatorname{dim}\left(\mathcal{H}\left(\mathcal{A}^{\infty}\right)\right)=\infty$.
Proof. Consider the difference equations (7.5)-(7.6). Clearly, the matrix $M_{n+1}$ has the maximal rank $n+1$ for every $n \geq 0$. Taking into account that

$$
\left(B_{n+1}-\frac{1}{2} I_{n+1}\right)^{-1}=\frac{4}{2 n+1} B_{n+1}-2 I_{n+1}=: C_{n}, \quad n \geq 0
$$

(7.6) then reads

$$
\left(I_{n+1} \quad \frac{2}{2 n+1} B_{n+1,1}\right) f_{n+1}=\ell_{n} C_{n}\left(D_{n} f_{n}-M_{n}^{*} f_{n-1}\right)
$$

[^0]
[^0]:    ${ }^{\dagger}$ Here and below to estimate norms, we use the equality $\|A\|=\sqrt{\left\|A^{*} A\right\|}$ and the following simple estimate for non-negative $2 \times 2$ block-matrices $A=\left(\begin{array}{cc}A_{11} & A_{12} \\ A_{12}^{*} & A_{22}\end{array}\right):\|A\| \leq\left\|A_{11}\right\|+\left\|A_{22}\right\|$. There are other estimates (e.g., [36, ineq. (2.3.8)]), however, they do not seem to work as good as the above approach.



for all $n \geq 1$. Observe that

$$
\left(I_{2 n+1}^{n+1} B_{n+1,1}\right)\left(\begin{array}{c}
f_{1} \\
\vdots \\
f_{n+1} \\
0
\end{array}\right)=\left(\begin{array}{c}
f_{1} \\
\vdots \\
f_{n+1}
\end{array}\right)
$$

and hence for any $f_{n} \in \mathbb{C}^{n+1}$ and $f_{n-1} \in \mathbb{C}^{n}$ there always exists a unique $f_{n+1}=$ $\left(f_{1}, \ldots, f_{n+1}, 0\right)^{\top}$ satisfying (7.31). Now pick a natural number $N$ and define $f^{N} \in$ $C\left(\mathcal{A}_{\infty}\right)$ by setting $f_{n}^{N}:=(0, \ldots, 0)^{\boldsymbol{\top}} \in \mathbb{C}^{n+1}$ for all $n \in\{0, \ldots, N\}$,

$$
f_{N+1}^{N}:=(1, \ldots, 1,-N-1 / 2)^{\top}
$$

and

$$
f_{n+1}^{N}:=\binom{\ell_{n} C_{n}\left(D_{n} f_{n}^{N}-M_{n}^{*} f_{n-1}^{N}\right)}{0} \in \mathbb{C}^{n+2}
$$

for all $n \geq N+1$. Clearly, $f^{N}$ satisfies (7.5)-(7.6) and hence defines a harmonic function $f^{N} \in \mathcal{H}\left(\mathcal{A}_{\infty}\right)$. Moreover, it is easy to see that $\operatorname{span}\left\{f^{N}\right\}_{N \geq 1}$ is infinite dimensional, which proves the claim.

Proposition 7.7. Let $H_{0}$ be the minimal Kirchhoff Laplacian associated with the antitree $\mathcal{A}_{\infty}$. If $\ell_{n}$ is decreasing and

$$
\sqrt{\ell_{n}}=O\left(\frac{1}{6^{n}(n+3)!}\right)
$$

as $n \rightarrow \infty$, then $n_{ \pm}\left(H_{0}\right)=\infty$.
Proof. Clearly, it suffices to show that every $f^{N}$ constructed in the proof of Lemma 7.6 belongs to $L^{2}(G)$ if $\ell_{n}$ decays as in (7.33). To prove this we shall proceed as in the proof of Proposition 7.5. First, taking into account (7.29), observe that

$$
m(v) \lesssim n \ell_{n-1}, \quad v \in S_{n}
$$

as $n \rightarrow \infty$. Since $\left\|f_{n}^{N}\right\|^{2}=\sum_{v \in S_{n}}\left|f^{N}(v)\right|^{2}$ for all $n \geq 0$, we get the estimate

$$
\sum_{v \in V}\left|f^{N}(v)\right|^{2} m(v) \lesssim \sum_{n \geq N+1} \sum_{v \in S_{n}}\left|f^{N}(v)\right|^{2} m(v) \lesssim \sum_{n \geq N+1} n \ell_{n-1}\left\|f_{n}^{N}\right\|^{2}
$$

Denoting $F_{n}:=f_{n}^{N}$ for all $n \geq 1$, we can put (7.31) into the matrix form

$$
\binom{F_{n+1}}{F_{n}}=\left(\begin{array}{cc}
A_{1, n} & A_{2, n} \\
I_{n+1} & 0_{n+1, n}
\end{array}\right)\binom{F_{n}}{F_{n-1}}=A_{n}\binom{F_{n}}{F_{n-1}}
$$

for all $n \geq N+1$, where

$$
A_{1, n}:=\left(\begin{array}{c}
\ell_{n} C_{n} D_{n} \\
0_{1, n+1}
\end{array}\right) \in \mathbb{R}^{(n+2) \times(n+1)}, \quad A_{2, n}:=\left(\begin{array}{c}
-\ell_{n} C_{n} M_{n}^{*} \\
0_{1, n}
\end{array}\right) \in \mathbb{R}^{(n+2) \times n}
$$

Now observe that $\left\|C_{n}\right\|=2$ and $\left\|\ell_{n} D_{n}\right\| \leq 2(n+1)$ for all $n \geq 1$. Moreover, $\left\|\ell_{n} M_{n}^{*}\right\| \leq n+1$ for all $n \geq 1$, which immediately implies the following estimate

$$
\left\|A_{n}\right\| \leq \sqrt{\left\|\ell_{n} C_{n} D_{n}\right\|^{2}+1+\left\|\ell_{n} C_{n} M_{n}^{*}\right\|^{2}} \leq 6(n+1), \quad n \geq N+1
$$

Hence we get

$$
\left\|f_{n+1}^{N}\right\| \leq C \prod_{k=N+1}^{n}\left\|A_{k}\right\| \leq C 6^{n-N} \frac{(n+1)!}{(N+1)!} \lesssim 6^{n}(n+1)!
$$



for all $n \geq N+1$. Combining this estimate with (7.34) and (7.33) and using Lemma 2.13, we conclude that $f_{N} \in L^{2}\left(A_{\infty}\right)$ for each $N \geq 1$.
Remark 7.8. It is not difficult to show that $f_{N}$ does not belong to $H^{1}\left(A_{\infty}\right)$ for the above choices of edge lengths. In fact, it follows from the maximum principle for $H(A)$ that if $\operatorname{vol}(A)<\infty$, then $H(A) \cap H^{1}(A)$ consists only of constant functions.
7.5. Proof of Theorem 7.1. Clearly, the case of infinite deficiency indices follows from Proposition 7.7. On the other hand, since adding and/or removing finitely many edges and vertices to a graph does not change the deficiency indices of the minimal Kirchhoff Laplacian, Proposition 7.5 completes the proof of Theorem 7.1. Indeed, every antitree $A_{N}$ can be obtained from $A$ by first removing all the edges between combinatorial spheres $S_{0}$ and $S_{N}$ and then adding $N+1$ edges connecting the root $o$ with the vertices in $S_{N}$.
Remark 7.9. Since every infinite antitree has exactly one end, Theorem 6.11(iv) implies that the Kirchhoff Laplacian $H_{0}$ in Theorem 7.1 has a unique Markovian extension exactly when $\operatorname{vol}(A)=\infty$. If $\operatorname{vol}(A)<\infty$, then Markovian extensions of $H_{0}$ form a one-parameter family explicitly given by (6.17). Notice that (6.17) looks similar to the description of self-adjoint extensions of the minimal Kirchhoff Laplacian on radially symmetric antitrees obtained recently in [56].

Let us also emphasize that the antitree constructed in Proposition 7.7 has finite total volume and $H_{0}$ has infinite deficiency indices, however, the set of Markovian extensions of $H_{0}$ forms a one-parameter family.

Let us finish this section with one more comment. As it was proved, the dimension of the space of Markovian extensions depends only on the space of graph ends and, moreover, it is equal to the number of finite volume ends. However, deficiency indices (dimension of the space of self-adjoint extensions) are in general independent of graph ends and we can only provide a lower bound. Moreover, the above example of a polynomially growing antitree shows that the space of non-constant harmonic functions heavily depends on the choice of edge lengths (in particular, its dimension may vary between zero and infinity). In this respect let us also emphasize that in the case of Cayley graphs of finitely generated groups the end space is independent of the choice of a generating set, however, simple examples show that the space of harmonic functions does depend on this choice.

# Appendix A. Linear relations in Hilbert spaces 

In this section we collect basic notions and facts on linear relations in Hilbert spaces, a very convenient concept of multi-valued linear operators. For simplicity, we shall assume that $\mathcal{H}$ is a finite dimensional Hilbert space, $N:=\operatorname{dim}(\mathcal{H})<\infty$. A linear relation $\Theta$ in $\mathcal{H}$ is a linear subspace in $\mathcal{H} \times \mathcal{H}$. Linear operators become special linear relations (single valued) after identifying them with their graphs in $\mathcal{H} \times \mathcal{H}$. Consider linear relations in $\mathcal{H}$ having the form

$$
\Theta_{C, D}=\{(f, g) \in \mathcal{H} \times \mathcal{H} \mid C f=D g\}
$$

where $C, D$ are linear operators on $\mathcal{H}$. Notice that different $C$ and $D$ may define the same linear relation. The domain and the multi-valued part of $\Theta_{C, D}$ are given



by

$$
\begin{aligned}
\operatorname{dom}\left(\Theta_{C, D}\right) & =\{f \in \mathcal{H} \mid \exists g \in \mathcal{H}, C f=D g\}=\{f \in \mathcal{H} \mid C f \in \operatorname{ran}(D)\} \\
\operatorname{mul}\left(\Theta_{C, D}\right) & =\{g \in \mathcal{H} \mid D g=0\}=\operatorname{ker}(D)
\end{aligned}
$$

In particular, $\Theta_{C, D}$ is a graph of a linear operator only if $\operatorname{ker}(D)=\{0\}$.
The adjoint relation $\Theta_{C, D}^{*}$ to $\Theta_{C, D}$ is given by

$$
\begin{aligned}
\Theta_{C, D}^{*} & =\left\{(f, g) \in \mathcal{H} \times \mathcal{H} \mid\langle\widetilde{g}, f\rangle_{\mathcal{H}}=\langle\widetilde{f}, g\rangle_{\mathcal{H}} \forall(\widetilde{f}, \widetilde{g}) \in \Theta_{C, D}\right\} \\
& =\left\{\left(D^{*} f, C^{*} f\right) \mid f \in \mathcal{H}\right\}
\end{aligned}
$$

Thus, a linear relation $\Theta_{C, D}$ is self-adjoint, $\Theta_{C, D}=\Theta_{C, D}^{*}$, if and only if $C$ and $D$ satisfy the Rofe-Beketov conditions [68] (see also [69, Exercises 14.9.3-4]):

$$
C D^{*}=D C^{*}, \quad 0 \in \rho\left(C^{*} C+D^{*} D\right)
$$

Taking into account that every linear relation in $\mathcal{H}$ admits one of the forms (A.1) or (A.2), this provides a description of self-adjoint linear relations in $\mathcal{H}$. Notice also that the second condition in (A.3) is equivalent to the fact that the matrix $(C \mid D) \in \mathbb{C}^{N \times 2 N}$ has the maximal rank $N$.

Recall also that every self-adjoint linear relation admits the representation $\Theta=$ $\Theta_{\text {op }} \oplus \Theta_{\mathrm{mul}}$, where $\Theta_{\text {mul }}:=\{0\} \times \operatorname{mul}(\Theta)$ and $\Theta_{\mathrm{op}}$, called the operator part of $\Theta$, is a graph of a linear operator. In particular, for a self-adjoint linear relation $\Theta_{C, D}$ one has

$$
\operatorname{dom}\left(\Theta_{C, D}\right)=\operatorname{mul}\left(\Theta_{C, D}\right)^{\perp}=\operatorname{ker}(D)^{\perp}=\operatorname{ran}\left(D^{*}\right)
$$

For further details on linear relations we refer the reader to, e.g., [69, Chapter 14.1].

# Appendix B. A rope ladder graph 

Let us introduce a rope ladder graph depicted on Figure 2. Let $\mathcal{G}_{d}=(V, \mathcal{E})$ be a simple graph with the vertex set $V:=\{o\} \cup V_{+} \cup V_{-}$, where $o=v_{0}$ is a root, $V_{+}=\left(v_{n}^{+}\right)_{n \geq 1}$ and $V_{-}=\left(v_{n}^{-}\right)_{n \geq 1}$ are two disjoint countably infinite sets of vertices. The edge set $\mathcal{E}$ is defined as follows:

- $o$ is connected to $v_{1}^{+}$and $v_{1}^{-}$by the "diagonal" edges $e_{0}^{+}$and $e_{0}^{-}$, respectively;
- for each $n \geq 1, v_{n}^{ \pm}$is connected to $v_{n+1}^{ \pm}$by the vertical edge $e_{n}^{ \pm}$;
- for each $n \geq 1, v_{n}^{+}$and $v_{n}^{-}$are connected by the horizontal edge $e_{n}$.



Figure 2. The rope ladder graph.



By construction, $\operatorname{deg}(o)=2$ and $\operatorname{deg}\left(v_{n}^{+}\right)=\operatorname{deg}\left(v_{n}^{-}\right)=3$ for all $n \geq 1$. Moreover, an infinite rope ladder graph has exactly one end. Notice also that a similar example was studied in [46, Section 7] (see also $[33, \S 5]$ ) in context with the construction of non-constant harmonic functions of finite energy.

Equip now $\mathcal{G}_{d}$ with edge lengths $|\cdot|: E \rightarrow(0, \infty)$ and consider the corresponding minimal Kirchhoff Laplacian $H_{0}$ on the metric graph $\mathcal{G}=\left(\mathcal{G}_{d},|\cdot|\right)$. The next result immediately follows from Theorem 2.8 and Corollary 2.11.

Corollary B.1. If

$$
\sum_{n \geq 1}\left|e_{n}^{+}\right|+\left|e_{n}\right|=\infty \quad \text { and } \quad \sum_{n \geq 1}\left|e_{n}^{-}\right|+\left|e_{n}\right|=\infty
$$

then the Kirchhoff Laplacian $H_{0}$ is self-adjoint. If

$$
\operatorname{vol}(\mathcal{G})=\sum_{n \geq 1}\left|e_{n}^{+}\right|+\left|e_{n}^{-}\right|+\left|e_{n}\right|<\infty
$$

then $n_{ \pm}\left(H_{0}\right) \geq 1$.
We omit the proof since it is easy to check that the first condition is equivalent to the geodesic completeness of $\left(V, \varrho_{m}\right)$ (cf. Theorem 2.8). Due to the symmetry of the underlying combinatorial graph, the gap between the above two conditions is equivalent to the fact that the corresponding lengths satisfy

$$
\sum_{n \geq 1}\left|e_{n}^{+}\right|=\infty, \quad \sum_{n \geq 1}\left|e_{n}^{-}\right|+\left|e_{n}\right|<\infty
$$

Next, let us describe the space of harmonic functions $\mathcal{H}(\mathcal{G})$.
Lemma B.2. Let $a, b \in \mathbb{C}$. Then there is exactly one $f \in \mathcal{H}(\mathcal{G})$ such that

$$
f\left(v_{1}^{+}\right)=a, \quad f\left(v_{1}^{-}\right)=b
$$

Moreover, this function $f$ is recursively given by

$$
f(o)=\frac{b\left|e_{0}^{+}\right|+a\left|e_{0}^{-}\right|}{\left|e_{0}^{+}\right|+\left|e_{0}^{-}\right|}
$$

and

$$
f\left(v_{n+1}^{ \pm}\right)=\left(1+\frac{\left|e_{n}^{ \pm}\right|}{\left|e_{n-1}^{ \pm}\right|}+\frac{\left|e_{n}^{ \pm}\right|}{\left|e_{n}\right|}\right) f\left(v_{n}^{ \pm}\right)-\frac{\left|e_{n}^{ \pm}\right|}{\left|e_{n-1}^{ \pm}\right|} f\left(v_{n-1}^{ \pm}\right)-\frac{\left|e_{n}^{ \pm}\right|}{\left|e_{n}\right|} f\left(v_{n}^{\mp}\right)
$$

for all $n \in \mathbb{Z}_{\geq 1}$, where we use the notation $v_{0}^{+}:=v_{0}^{-}:=o$.
Proof. Suppose $a, b \in \mathbb{C}$ are given and $f \in \mathcal{H}(\mathcal{G})$ satisfies (B.4). Since $f$ is linear on every edge and satisfies (2.7) at $v=o$, we get

$$
0=f_{e_{0}^{+}}^{\prime}(o)+f_{e_{0}^{-}}^{\prime}(o)=\frac{f\left(v_{1}^{+}\right)-f(o)}{\left|e_{0}^{+}\right|}+\frac{f\left(v_{1}^{-}\right)-f(o)}{\left|e_{0}^{-}\right|}=\frac{a-f(o)}{\left|e_{0}^{+}\right|}+\frac{b-f(o)}{\left|e_{0}^{-}\right|}
$$

which implies (B.5). Moreover, Kirchhoff conditions (2.7) at $v=v_{n}^{ \pm}, n \geq 1$ read

$$
\frac{f\left(v_{n+1}^{ \pm}\right)-f\left(v_{n}^{ \pm}\right)}{\left|e_{n}^{ \pm}\right|}+\frac{f\left(v_{n-1}^{ \pm}\right)-f\left(v_{n}^{ \pm}\right)}{\left|e_{n-1}^{ \pm}\right|}+\frac{f\left(v_{n}^{\mp}\right)-f\left(v_{n}^{ \pm}\right)}{\left|e_{n}\right|}=0
$$

This implies that $f$ is given by (B.6). Hence there is at most one $f \in \mathcal{H}(\mathcal{G})$ satisfying (B.4) for given $a, b \in \mathbb{C}$. However, the same calculation shows that $f$ defined by (B.5) and (B.6) has this property. Thus, existence follows as well.



From Lemma B.2, it is clear that $\operatorname{dim}(\mathcal{H}(\mathbb{G}))=2$, and, moreover,

$$
\mathcal{H}(\mathbb{G})=\operatorname{span}\left\{\mathbf{1}_{\mathbb{G}}, g_{0}\right\}
$$

where $\mathbf{1}_{\mathbb{G}}$ denotes the constant function on $\mathbb{G}$ and $g_{0} \in \mathcal{H}(\mathbb{G})$ is the function defined, for example, by the following normalization

$$
g_{0}(0)=0, \quad g_{0}\left(v_{1}^{+}\right)=\left|e_{0}^{+}\right|, \quad g_{0}\left(v_{1}^{-}\right)=-\left|e_{0}^{-}\right|
$$

Notice that $g_{0}\left(v_{n}^{ \pm}\right), n \geq 1$ are then given recursively by (B.6).
Lemma B.3. If $\operatorname{vol}(\mathbb{G})<\infty$, then

$$
\mathcal{H}(\mathbb{G}) \cap \mathcal{H}^{1}(\mathbb{G})=\operatorname{span}\left\{\mathbf{1}_{\mathbb{G}}\right\}
$$

The claim immediately follows from the fact that a rope ladder graph has exactly one end. However, let us present a direct proof based on the analysis of harmonic functions.

Proof. Taking into account (B.8), we only need to show that $g_{0} \notin \mathcal{H}^{1}(\mathbb{G})$. First, observe that $\left(g_{0}\left(v_{n}^{+}\right)\right)_{n \geq 1}$ and $\left(g_{0}\left(v_{n}^{-}\right)\right)_{n \geq 1}$ are strictly increasing positive, respectively, strictly decreasing negative sequences. Indeed,

$$
-\left|e_{0}^{-}\right|=g_{0}\left(v_{1}^{-}\right)<0=g_{0}(o)<g_{0}\left(v_{1}^{+}\right)=\left|e_{0}^{+}\right|
$$

by the very definition of $g_{0}$. Let $n \geq 1$ and assume now that we have already shown that $\left(g_{0}\left(v_{k}^{+}\right)\right)_{k=1}^{n}$ is strictly increasing and $\left(g_{0}\left(v_{k}^{-}\right)\right)_{k=1}^{n}$ is strictly decreasing. Since $g_{0}(o)=0$, (B.6) implies

$$
\begin{aligned}
& g_{0}\left(v_{n+1}^{+}\right)=\left(1+\frac{\left|e_{n}^{+}\right|}{\left|e_{n-1}^{+}\right|}+\frac{\left|e_{n}^{+}\right|}{\left|e_{n}\right|}\right) g_{0}\left(v_{n}^{+}\right)-\frac{\left|e_{n}^{+}\right|}{\left|e_{n-1}^{+}\right|} g_{0}\left(v_{n-1}^{+}\right)-\frac{\left|e_{n}^{+}\right|}{\left|e_{n}\right|} g_{0}\left(v_{n}^{-}\right) \\
&>\left(1+\frac{\left|e_{n}^{+}\right|}{\left|e_{n}\right|}\right) g_{0}\left(v_{n}^{+}\right)+\frac{\left|e_{n}^{+}\right|}{\left|e_{n-1}^{+}\right|}\left(g_{0}\left(v_{n}^{+}\right)-g_{0}\left(v_{n-1}^{+}\right)\right)>g_{0}\left(v_{n}^{+}\right)
\end{aligned}
$$

A similar argument shows that $g_{0}\left(v_{n+1}^{-}\right)<g_{0}\left(v_{n}^{-}\right)$and hence the claim follows by induction. Now monotonicity immediately implies

$$
\begin{aligned}
\left\|g_{0}^{\prime}\right\|_{L^{2}(\mathbb{G})}^{2} & =\sum_{e \in \mathbb{E}} \int_{e}\left|g_{0}^{\prime}\left(x_{e}\right)\right|^{2} d x_{e} \geq \sum_{n \geq 0} \int_{e_{n}}\left|g_{0}^{\prime}\left(x_{e}\right)\right|^{2} d x_{e} \\
& =\sum_{n=0}^{\infty} \frac{\left|g_{0}\left(v_{n}^{+}\right)-g_{0}\left(v_{n}^{-}\right)\right|^{2}}{\left|e_{n}\right|} \geq\left|g_{0}\left(v_{1}^{+}\right)-g_{0}\left(v_{1}^{-}\right)\right|^{2} \sum_{n=0}^{\infty} \frac{1}{\left|e_{n}\right|}=\infty
\end{aligned}
$$

since $\operatorname{vol}(\mathbb{G})<\infty$. Thus $g_{0} \notin \mathcal{H}^{1}(\mathbb{G})$.
In particular, this also leads to the following result:
Corollary B.4. If $\operatorname{vol}(\mathbb{G})<\infty$, then $n_{ \pm}\left(H_{0}\right) \in\{1,2\}$. Moreover, $n_{ \pm}\left(H_{0}\right)=1$ if and only if $g_{0} \notin L^{2}(\mathbb{G})$.

Proof. The claim about the deficiency indices follows from Corollary 2.11 and the fact that $\mathbf{1}_{\mathbb{G}} \in L^{2}(\mathbb{G})$. The equivalences then follow from Lemma B.3.

As the next example shows, the inclusion $g_{0} \in L^{2}(\mathbb{G})$ heavily depends on the choice of edge lengths.



Example B.5. Fix $s>3$ and equip the rope ladder graph with edge lengths

$$
\left|e_{n}^{+}\right|=\left|e_{n}^{-}\right|:=\frac{1}{(n+1)^{s}}, \quad\left|e_{n}\right|:=\frac{2 n}{(n+1)^{s}}-n^{s}, \quad n \in \mathbb{Z}_{\geq 0}
$$

Then $\left|e_{n}\right| \sim n^{2-s}$ for large $n$ and hence $\operatorname{vol}(G)<\infty$. Moreover, for this particular choice of edge lengths we have $g_{0}\left(v_{n}^{ \pm}\right)= \pm n$ for all $n \geq 1$. Indeed, $g_{0}\left(v_{1}^{ \pm}\right)= \pm 1$ by (B.7). Assuming we have already proven that $g_{0}\left(v_{k}^{ \pm}\right)= \pm k$ for $k \leq n$ with some $n \geq 1$, we have by (B.6):

$$
\begin{aligned}
g_{0}\left(v_{n+1}^{+}\right) & =\left(1+\frac{n^{s}}{(n+1)^{s}}+\frac{1}{(n+1)^{s}}\left|e_{n}\right|\right) \frac{n-n^{s}(n-1)}{(n+1)^{s}}+\frac{n}{(n+1)^{s}}\left|e_{n}\right| \\
& =n+\frac{n^{s}}{(n+1)^{s}}+\frac{2 n}{(n+1)^{s}}\left|e_{n}\right|=n+\frac{n^{s}}{(n+1)^{s}}+(n+1)^{s}-n^{s} \frac{}{(n+1)^{s}}=n+1
\end{aligned}
$$

Analogously, $g_{0}\left(v_{n+1}^{-}\right)=-(n+1)$ and hence the claim follows by induction.
Applying Lemma B. 3 and using again that $\left|e_{n}\right| \sim n^{2-s}$ as $n \rightarrow \infty$, we conclude that $g_{0} \in L^{2}(G)$ exactly (see Lemma 2.13) when

$$
\sum_{n \geq 1}\left|g_{0}\left(v_{n}^{ \pm}\right)\right|^{2}\left(\left|e_{n-1}^{ \pm}\right|+\left|e_{n}^{ \pm}\right|\right)=\sum_{n \geq 1} n^{2}\left((n+1)^{-s}+n^{-s}\right)<\infty
$$

and

$$
\sum_{n \geq 1}\left|g_{0}\left(v_{n}^{ \pm}\right)\right|^{2}\left|e_{n-1}\right|=\sum_{n \geq 1} \frac{2 n^{3}}{(n+1)^{s}}-n^{s}<\infty
$$

Clearly, the latter holds only if $s>5$. Hence, by Lemma B.4, $n_{ \pm}\left(H_{0}\right)=2$ for all $s>5$. In particular, $\operatorname{ker}(H) \subset H^{1}(G) \Leftrightarrow s \leq 5$.

# AcKnowledgMENTs 

We thank Matthias Keller, Daniel Lenz, Primož Moravec, Andrea Posilicano and Wolfgang Woess for useful discussions and hints with respect to the literature. We also thank the referees for their comments which have helped us to improve the manuscript. N.N. appreciates the hospitality at the Institute of Mathematics, University of Potsdam, during a research stay funded by the OeAD (Marietta Blaugrant, ICM-2019-13386), where a part of this work was done.

## REFERENCES

[1] N. I. Akhiezer and I. M. Glazman, Theory of Linear Operators in Hilbert Spaces. Vol. II, Dover Publ., New York, 1993.
[2] O. Amini and L. Caporaso, Riemann-Roch theory for weighted graphs and tropical curves, Adv. Math. 240, 1-23 (2013).
[3] W. Arendt and A. F. M. ter Elst, Operators with continuous kernels, Integr. Equ. Oper. Theory 91, no. 5, Art. 45 (2019).
[4] W. Arendt and A. V. Bukhvalov, Integral representations of resolvents and semigroups, Forum. Math. 6, 111-135 (1994).
[5] M. Baker and S. Norine, Riemann-Roch and Abel-Jacobi theory on a finite graph, Adv. Math. 215, no. 2, 766-788 (2007).
[6] M. Baker and R. Rumely, Potential Theory and Dynamics on the Berkovich Projective Line, Math. Surv. Monographs, 159. Amer. Math. Soc., Providence, RI, 2010.
[7] M. T. Barlow and R. F. Bass, Stability of parabolic Harnack inequalities, Trans. Amer. Math. Soc. 356, no. 4, 1501-1533 (2004).
[8] G. Berkolaiko, R. Carlson, S. Fulling, and P. Kuchment, Quantum Graphs and Their Applications, Contemp. Math. 415, Amer. Math. Soc., Providence, RI, 2006.



[9] G. Berkolaiko and P. Kuchment, Introduction to Quantum Graphs, Amer. Math. Soc., Providence, RI, 2013.
[10] J. Breuer and M. Keller, Spectral analysis of certain spherically homogeneous graphs, Oper. Matrices 7, no. 4, 825-847 (2013).
[11] J. Breuer and N. Levi, On the decomposition of the Laplacian on metric graphs, Ann. Henri Poincaré 22, no. 2, 499-537 (2020).
[12] H. Brezis, Functional Analysis, Sobolev Spaces and Partial Differential Equations, Universitext, Springer, New York, 2011.
[13] D. Burago, Yu. Burago, and S. Ivanov, A Course in Metric Geometry, Graduate Stud. Math. 33, Amer. Math. Soc., Providence, RI, 2001.
[14] S. Cardanabile and D. Mugnolo, Parabolic systems with coupled boundary conditions, J. Differential Equations 247, 1229-1248 (2009).
[15] R. Carlson, Nonclassical Sturm-Liouville problems and Schrödinger operators on radial trees, Electr. J. Differential Equations 2000, no. 71, pp. 1-24 (2000).
[16] R. Carlson, Boundary value problems for infinite metric graphs, in [26].
[17] R. Carlson, Dirichlet to Neumann maps for infinite quantum graphs, Netw. Heterog. Media $\mathbf{7}$, no. 3, 483-501 (2012).
[18] D. I. Cartwright, P. M. Soardi, and W. Woess, Martin and end compactifications for nonlocally finite graphs, Trans. Amer. Math. Soc. 338, no 2, 679-693 (1993).
[19] Y. Colin de Verdière, N. Torki-Hamza, and F. Truc, Essential self-adjointness for combinatorial Schrödinger operators II-metrically non complete graphs, Math. Phys. Anal. Geom. 14, no. 1, 21-38 (2011).
[20] T. Coulhon, Off-diagonal heat kernel lower bounds without Poincaré, J. London Math. Soc. (2) 68, 795-816 (2003).
[21] D. Cushing, S. Liu, F. Münch, and N. Peyerimhoff, Curvature calculations for antitrees, in: M. Keller et. al. (Eds.), "Analysis and Geometry on Graphs and Manifolds", London Math. Soc. Lect. Notes Ser. 461, Cambridge Univ. Press, 2020.
[22] D. Damanik, L. Fang, and S. Sukhtaiev, Zero measure and singular continuous spectra for quantum graphs, Ann. Henri Poincaré 21, no. 7, 2167-2191 (2020).
[23] R. Diestel, Graph Theory, 5th edn., Grad. Texts in Math. 173, Springer-Verlag, Heidelberg, New York, 2017.
[24] R. Diestel and D.asl Herm. Theort. Theory, Ser. B 87, 197-206 (2003).
[25] J. Dodziuk and L. Karp, Spectral and function theory for combinatorial Laplacians, in: "Geometry of Random Motion" (Ithaca, N.Y., 1987), Contemp. Math. 73, Amer. Math. Soc., Providence, pp. 25-40 (1988).
[26] P. Exner, J. P. Keating, P. Kuchment, T. Sunada, and A. Teplyaev, Analysis on Graphs and Its Applications, Proc. Symp. Pure Math. 77, Providence, RI, Amer. Math. Soc., 2008 .
[27] P. Exner, A. Kostenko, M. Malamud, and H. Neidhardt, Spectral theory of infinite quantum graphs, Ann. Henri Poincaré 19, no. 11, 3457-3510 (2018).
[28] M. Folz, Volume growth and stochastic completeness of graphs, Trans. Amer. Math. Soc. 366, 2089-2119 (2014).
[29] H. Freudenthal, Über die Enden topologischer Räume und Gruppen, Math. Z. 33, 692-713 (1931).
[30] H. Freudenthal, Über die Enden diskreter Räume und Gruppen, Comment. Math. Helv. 17, 1-38 (1944).
[31] M. Fukushima, Y. Oshima, and M. Takeda, Dirichlet Forms and Symmetric Markov Processes, 2nd edn., De Gruyter, 2010.
[32] R. Geoghegan, Topological Methods in Group Theory, Grad. Texts in Math. 243, Springer, 2008 .
[33] A. Georgakopoulos, Uniqueness of electrical currents in a network of finite total resistance, J. London Math. Soc. 82, 256-272 (2010).
[34] A. Georgakopoulos, Graph topologies induced by edge lengths, Discrete Math. 311, no. 15, $1523-1542$ (2011).
[35] A. Georgakopoulos, S. Haeseler, M. Keller, D. Lenz, and R. Wojciechowski, Graphs of finite measure, J. Math. Pures Appl. 103, S1093-S1131 (2015).



[36] G. Golub and C. F. Van Loan, Matrix Computations, 4th edn., The Johns Hopkins University Press, Baltimore, 2012.
[37] A. Grigor'yan and J. Masamune, Parabolicity and stochastic completeness of manifolds in terms of the Green formula, J. Math. Pures Appl. 100, 607-632 (2013).
[38] R. Halin, Über unendliche Wege in Graphen, Math. Ann. 157, 125-137 (1964).
[39] S. Haeseler, M. Keller, D. Lenz, and R. Wojciechowski, Laplacians on infinite graphs: Dirichlet and Neumann boundary conditions, J. Spectr. Theory 2, no. 4, 397-432 (2012).
[40] S. Haeseler, Analysis of Dirichlet forms on graphs, PhD thesis, Jena, 2014; arXiv:1705.06322 (2017).
[41] M. Hinz and M. Schwarz, A note on Neumann problems on graphs, preprint, arXiv: 1803.08559 (2018).
[42] H. Hopf, Enden offener Räume und unendliche diskontinuierliche Gruppen, Comment. Math. Helv. 16, 81-100 (1943).
[43] B. Hua, Liouville theorem for bounded harmonic functions on manifolds and graphs satisfying non-negative curvature dimension condition, Calc. Var. Partial Differential Equations 58, no. 2, Art. 42 (2019).
[44] B. Hua and M. Keller, Harmonic functions of general graph Laplacians, Calc. Var. Partial Differential Equations 51, 343-362 (2014).
[45] X. Huang, M. Keller, J. Masamune, and R. Wojciechowski, A note on self-adjoint extensions of the Laplacian on weighted graphs, J. Funct. Anal. 265, 1556-1578 (2013).
[46] P. Jorgensen and E. Pearse, Gel'fand triples and boundaries of infinite networks, New York J. Math. 17, 745-781 (2011).
[47] U. Kant, T. Klauß, J. Voigt, and M. Weber, Dirichlet forms for singular one-dimensional operators and on graphs, J. Evol. Equ. 9, 637-659 (2009).
[48] A. Kasue, Convergence of metric graphs and energy forms, Rev. Mat. Iberoam. 26, no. 2, $367-448$ (2010).
[49] A. Kasue, Convergence of Dirichlet forms induced on boundaries of transient networks, Potential Anal. 47, no. 2, 189-233 (2017).
[50] T. Kato, Perturbation Theory for Linear Operators, 2nd ed., Springer-Verlag, Berlin-New York, 1976.
[51] M. Keller and D. Lenz, Dirichlet forms and stochastic completeness of graphs and subgraphs, J. reine angew. Math. 666, 189-223 (2012).
[52] M. Keller, D. Lenz, M. Schmidt, and M. Schwarz, Boundary representation of Dirichlet forms on discrete spaces, J. Math. Pures Appl. 126, 109-143 (2019).
[53] M. Keller, D. Lenz, M. Schmidt, and R. K. Wojciechowski, Note on uniformly transient graphs, Rev. Mat. Iberoam. 33, no. 3, 831-860 (2017).
[54] M. Keller, D. Lenz, and R. K. Wojciechowski, Volume growth, spectrum and stochastic completeness of infinite graphs, Math. Z. 274, no. 3-4, 905-932 (2013).
[55] A. Kostenko and N. Nicolussi, Spectral estimates for infinite quantum graphs, Calc. Var. Partial Differential Equations 58, no. 1, Art. 15 (2019).
[56] A. Kostenko and N. Nicolussi, Quantum graphs on radially symmetric antitrees, J. Spectral Theory 11, no. 2, 411-460 (2021).
[57] V. Kostrykin, J. Potthoff, and R. Schrader, Contraction semigroups on metric graphs, in $[26]$.
[58] T. Lupu, From loop clusters and random interlacements to the free field, Ann. Probab. 44, 2117-2146 (2016).
[59] T. Lupu, Convergence of the two-dimensional random walk loop-soup clusters to CLE, $J$. Eur. Math. Soc. 21, 1201-1227 (2019).
[60] J. T. Marti, Evaluation of the least constant in Sobolev's inequality for $H^{1}(0, s)$, SIAM J. Numer. Anal. 20, 1239-1242 (1983).
[61] J. Masamune, Essential self-adjointness of Laplacians on Riemannian manifolds with fractal boundary, Commun. Partial Diff. Equ. 24, no. 3-4, 749-757 (1999).
[62] J. Masamune, Analysis of the Laplacian of an incomplete manifold with almost polar boundary, Rend. Mat. Appl. (7) 25, no. 1, 109-126 (2005).
[63] D. Mugnolo and R. Nittka, Properties of representations of operators acting between spaces of vector-valued functions, Positivity 15, 135-154 (2011).
[64] A. Murakami and M. Yamasaki, An introduction of Kuramochi boundary of an infinite network, Mem. Fac. Sci. Eng. Shimane Univ. Ser. B Math. Sci. 30, 57-89, 1997.



[65] N. Nicolussi, Strong isoperimetric inequality for tessellating quantum graphs, in: F. Fatihcan et. al. (Eds.), "Discrete and Continuous Models in the Theory of Networks", 271-290, Oper. Theory: Adv. Appl. 64, Birkhäuser, Basel, 2020.
[66] E. M. Ouhabaz, Analysis of Heat Equations on Domains, Princeton Univ. Press, Princeton and Oxford, 2005.
[67] O. Post, Spectral Analysis on Graph-Like Spaces, Lect. Notes in Math. 2039, SpringerVerlag, Berlin, Heidelberg, 2012
[68] F. S. Rofe-Beketov, Self-adjoint extensions of differential operators in a space of vectorvalued functions, Teor. Funkcii, Funkcional. Anal. i Priložen. 8, 3-24 (1969). (in Russian)
[69] K. Schmüdgen, Unbounded Self-Adjoint Operators on Hilbert Space, Grad. Texts in Math. 265, Springer, Berlin, 2012.
[70] F. Shokrieh and C. Wu, Canonical measures on metric graphs and a Kazhdan's theorem, Invent. Math. 215, 819-862 (2019).
[71] P. M. Soardi, Potential Theory on Infinite Networks, Lect. Notes Math. 1590, Springer, Berlin, 1994.
[72] M. Solomyak, On the spectrum of the Laplacian on regular metric trees, Waves Random Media 14, S155-S171 (2004).
[73] J. R. Stallings, Group Theory and Three-Dimensional Manifolds, Yale Univ. Press, New Haven, Connecticut, 1971.
[74] K.-T. Sturm, Analysis on local Dirichlet spaces I. Recurrence, conservativeness and $L^{p_{-}}$
Liouville properties, J. reine angew. Math. 456, 173-196 (1994).
[75] C. T. C. Wall, Poincaré complexes: I, Ann. of Math. 86, no. 2, 213-245 (1967).
[76] W. Woess, Random Walks on Infinite Graphs and Groups, Cambridge Univ. Press, Cambridge, 2000.
[77] R. K. Wojciechowski, Stochastically incomplete manifolds and graphs, in: D. Lenz et al. (Eds.), "Random Walks, Boundaries and Spectra", 163-179, Progr. Probab. 64, Birkhäuser/Springer Basel AG, Basel, 2011.
Faculty of Mathematics and Physics, University of Ljubljana, Jadranska ul. 19, 1000 Ljubljana, Slovenia, and Institute for Analysis and Scientific Computing, Vienna University of Technology, Wiedner Hauptstraße 8-10/101, 1040 Vienna, Austria

Current address: Faculty of Mathematics and Physics, University of Ljubljana, Jadranska ul. 19, 1000 Ljubljana, Slovenia, and Faculty of Mathematics, University of Vienna, Oskar-MorgensternPlatz 1, 1090 Vienna, Austria

Email address: Aleksey.Kostenko@fmf.uni-lj.si
Lehrgebiet Analysis, Fakultät Mathematik und Informatik, FernUniversität in Hagen, Hagen, Germany

Email address: delio.mugnolo@fernuni-hagen.de
Faculty of Mathematics, University of Vienna, Oskar-Morgenstern-Platz 1, 1090 Vienna, Austria

Email address: noema.nicolussi@univie.ac.at



