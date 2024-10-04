# SELF-ADJOINT AND MARKOVIAN EXTENSIONS OF INFINITE QUANTUM GRAPHS  

ALEKSEY KOSTENKO, DELIO MUGNOLO, AND NOEMA NICOLUSSI  

Abstract.  We investigate the relationship between one of the classical no- tions of boundaries for inﬁnite graphs,  graph ends , and self-adjoint extensions of the minimal Kir ch ho La plac ian on a metric graph. We introduce the no- tion of  ﬁnite volume  for ends of a metric graph and show that ﬁnite volume graph ends is the proper notion of a boundary for Markovian extensions of the Kir ch ho La plac ian. In contrast to manifolds and weighted graphs, this pro- vides a transparent geometric characterization of the uniqueness of Markovian extensions, as well as of the self-adjointness of the Gaﬀney Laplacian — the underlying metric graph does not have ﬁnite volume ends. If however ﬁnitely many ﬁnite volume ends occur (as is the case of edge graphs of normal, locally ﬁnite tessellations or Cayley graphs of amenable ﬁnitely generated groups), we provide a complete description of Markovian extensions upon introducing a suitable notion of traces of functions and normal derivatives on the set of graph ends.  

# Contents  

1. Introduction Notation

 2. Quantum graphs

 2.1. Combinatorial and metric graphs

 2.2. Graph ends

 2.3. KirchhoﬀLaplacian

 2.4. Deﬁciency indices

 3. Graph ends and    $H^{1}(\mathcal{G})

$  3.1.  $H^{1}(\mathcal{G})$   and boundary values

 3.2. Nontrivial and ﬁnite volume ends

 3.3. Description of    $H_{0}^{1}(\mathcal{G})

$  4. Deﬁciency indices

 4.1. Deﬁciency indices and graph ends

 4.2. Proof of Theorem 4.1

 5. Properties of self-adjoint extensions

 6. Finite energy self-adjoint extensions

 6.1. Normal derivatives at graph ends

 6.2. Properties of the trace and normal derivatives

 6.3. Description of self-adjoint extensions

 7. Deﬁciency indices of antitrees

 7.1. Antitrees 7.2. Harmonic functions 7.3. Finite deﬁciency indices 7.4. Inﬁnite deﬁciency indices 7.5. Proof of Theorem 7.1 Appendix A. Linear relations in Hilbert spaces Appendix B. A rope ladder graph Acknowledgments References  

# 1.  Introduction  

This paper is concerned with developing extension theory for inﬁnite  quantum graphs . Quantum graphs are Schr¨ odinger operators on  metric graphs , that is combi- natorial graphs where edges are considered as intervals with certain lengths. Moti- vated by a vast amount of applications in chemistry and physics, they have become a popular subject in the last decades (we refer to [8, 9, 26, 67] for an overview and further references). From the perspective of Dirichlet forms, quantum graphs play an important role as an intermediate setting between Laplacians on Riemannian manifolds and diﬀerence Laplacians on weighted graphs. On the one hand, being locally one-dimensional, quantum graphs allow to simplify considerations of compli- cated geometries. On the other hand, there is a close relationship between random walks on graphs and Brownian motion on metric graphs, however, in contrast to the discrete case, the corresponding quadratic form in the metric case is a strongly local Dirichlet form and in this situation more tools are available (see [7, 28, 58, 59] for various manifestations of this point of view). Let us also mention that metric graphs can be seen as non-Archimedian analogs of Riemann surfaces, which ﬁnds numerous applications in algebraic geometry (see [2, 5, 6, 70] for further references).  

The most studied quantum graph operator is the  KirchhoﬀLaplacian , which pro- vides the analog of the Laplace–Beltrami operator in the setting of metric graphs. Its spectral properties are crucial in connection with the heat equation and the Schr¨ odinger equation and any further analysis usually relies on the  self-adjointness of the Laplacian . Whereas on ﬁnite metric graphs the Kir ch ho La plac ian is always self-adjoint, the question is more subtle for  graphs with inﬁnitely many edges .  

For instance, a uniform lower bound for the edge lengths guarantees self-adjoint- ness (see [9, 67]), but this commonly used condition is independent of the com- binatorial graph structure and clearly excludes a number of interesting cases (the so-called  fractal metric graphs ). Moreover, most of the results on strongly local Dirichlet forms require completeness of a given metric space w.r.t. the “intrinsic” metric (cf., e.g., [74]), which coincides with the natural path (geodesic) metric in the case of metric graphs. Geodesic completeness (w.r.t. the natural path metric) guarantees self-adjointness of the (minimal) Kir ch ho La plac ian, however, this re- sult is far from being optimal (see [27,  § 4] and also Section 2.4 below). The search for self-adjointness criteria for inﬁnite quantum graphs is an open and – in our opinion – rather diﬃcult problem.  

If the (minimal) Kir ch ho La plac ian is not self-adjoint, the natural next step is to ask for a description of its self-adjoint extensions, which corresponds to possible descriptions of the system in quantum mechanics or, if we speak about Markovian extensions, possible descriptions of Brownian motions. Naturally, this question is tightly related to ﬁnding appropriate boundary notions for inﬁnite graphs. Our goal in this paper is to investigate the connection between extension theory and one particular notion, namely  graph ends , a concept which goes back to the work of Freudenthal [30] and Halin [38] and provides a rather reﬁned way of compactifying graphs. However, the deﬁnition of graph ends is purely combinatorial and naturally must be modiﬁed to capture the additional metric structure of our setting. Based on the correspondence between graph ends and topological ends of metric graphs, we introduce the concept of  ends of ﬁnite volume . First of all, it turns out that ﬁnite volume ends play a crucial role in describing the Sobolev spaces    $H^{1}$    and    $H_{0}^{1}$  on metric graphs. More speciﬁcally, we show that the presence of ﬁnite volume ends is the only reason for the strict inclusion    $H_{0}^{1}\subsetneq H^{1}$   to hold. This in particular provides a surprisingly transparent geometric characterization of the uniqueness of Markovian extensions of the minimal Kir ch ho La plac ian as well as the self- adjointness of the so-called  Gaﬀney Laplacian  (we are not aware of its analogs either in the manifold setting or in the context of weighted graph Laplacians, cf. [35, 37, 45, 52, 61, 62]). As yet another manifestation of the fact that ﬁnite volume graph ends represent the proper boundary for Markovian extensions of the Kirchhoﬀ Laplacian, we provide a complete description of  all ﬁnite energy extensions  (i.e., self-adjoint extensions with domains contained in    $H^{1}$  , and all Markovian extensions clearly satisfy this condition), however, under the additional assumption that there are only ﬁnitely many ﬁnite volume ends. Let us stress that this class of graphs includes a wide range of interesting models (Cayley graphs of a large class of ﬁnitely generated groups, tessellating graphs, rooted antitrees etc. have exactly one end and in this case there are no ﬁnite volume ends exactly when the total volume of the corresponding metric graph is inﬁnite). Moreover, we emphasize that in all those cases the dimension of the space of ﬁnite energy extensions is equal to the number of ﬁnite volume ends, however, for deﬁciency indices, i.e., the dimension of the space of self-adjoint extensions, this only gives a lower bound (for example, for Cayley graphs the dimension of the space of ﬁnite energy extensions is independent of the choice of a generating set, although deﬁciency indices do depend on this choice in a rather nontrivial way). On the other hand, it may happen that these dimensions coincide. The latter holds only if the maximal domain is contained in    $H^{1}$  , that is, if every self-adjoint extension is a ﬁnite energy extension. This is further equivalent to the validity of a certain non-trivial Sobolev-type inequality (see (1.1) below). The appearance of this condition demonstrates the mixed dimensional behavior of inﬁnite metric graphs since the analogous estimate holds true in the one-dimensional situation, but usually fails in the PDE setting.  

Let us now sketch the structure of the article and describe its content and our results in greater details.  

In Section 2 we collect basic notions and facts about graphs and metric graphs (Section 2.1); graph ends (Section 2.2); the minimal and maximal KirchhoﬀLapla- cians (Section 2.3); deﬁciency indices and their connection with the spaces of    $L^{2}$  harmonic and    $\lambda$  -harmonic functions (Section 2.4).  

The core of the paper is Section 3, where we discuss the Sobolev spaces    $H^{1}(\mathcal G)$  and    $H_{0}^{1}(\mathcal{G})$  G ) and introduce the set of ﬁnite vo e ends    $\mathfrak{C}_{0}(\mathcal{G})$   (Deﬁnition 3.8). We show that    $\mathfrak{C}_{0}(\mathcal{G})$   is the proper bou ry for  H  $H^{1}$    functions, which can also be seen as an ideal boundary by applying  C  $C^{*}$  -algebra techniques (see Remark 3.14). The central result of this section is Theorem 3.12, which shows that    $H^{1}(\mathcal{G})=H_{0}^{1}(\mathcal{G})$  G ) if and only if there are no ﬁnite volume ends. The latter also leads to a surprisingly transparent geometric characterization of the uniqueness of Markovian extensions of the Kir ch ho La plac ian (Corollary 5.5) as well as the self-adjointness of the Gaﬀney Laplacian    ${\mathbf{H}}_{G}$   (see Remark 5.6(ii) for details and the deﬁnition of    ${\mathbf{H}}_{G}$  ).  

Section 4 contains further applications of the above considerations. Namely, The- orem 4.1 demonstrates that deﬁciency indices of the minimal Kir ch ho La plac ian can be estimated from below by the number of ﬁnite volume ends. This estimate is sharp (e.g., if there are inﬁnitely many ﬁnite volume ends) and we also ﬁnd nec- essary and suﬃcient conditions for the equality to hold. In particular, if there are only ﬁnitely many ends of ﬁnite volume,   $\#\mathfrak{C}_{0}(\mathcal{G})<\infty$  , the latter is equivalent to the validity of the following Sobolev-type inequality (see Remark 4.2)  

$$
\|f^{\prime}\|_{L^{2}(\mathcal{G})}\leq C\big(\|f\|_{L^{2}(\mathcal{G})}+\|f^{\prime\prime}\|_{L^{2}(\mathcal{G})}\big)
$$  

for all    $f$   in the maximal domain of the Kir ch ho La plac ian. Metric graphs are locally one-dimensional and the corresponding inequality is trivially satisﬁed in the one- dimensional case, however, globally inﬁnite metric graphs are more complex and hence (1.1) rather resembles the multi-dimensional setting of PDEs (in particular, (1.1) does not hold true if  $\mathcal{G}$   has a  non-free  ﬁnite volume end, see Proposition 4.9).  

In the next sections, we focus on a particular class of self-adjoint extensions whose domains are contained in    $H^{1}$    (we call them  ﬁnite energy extensions ). These extensions have good properties and their importance stems from the fact that they contain the class of Markovian extensions (they also arise as self-adjoint restrictions of the Gaﬀney Laplacian). In Section 5 we show that (under some additional mild assumptions) their  resolvents and heat semigroups  are  integral operators  with con- tinuous, bounded kernels and they belong to the trace class if    $\mathcal{G}$   has ﬁnite total volume (Theorems 5.1 and 5.2).  

In Section 6 we proceed further and show that ﬁnite volume ends is the proper boundary for this class of extensions. Namely, under the additional and rather restrictive assumption of  ﬁnitely many ends with ﬁnite volume , in Sections 6.1– 6.2, we introduce a suitable notion of a  normal derivative  at graph ends (as a by-product, this also gives an explicit description of the domain of the Neumann extension, see Corollary 6.7). Section 6.3 contains a complete description of ﬁnite energy extensions and also of Markovian extensions (Theorem 6.11). Let us stress that the case of inﬁnitely many ends is incomparably more complicated and will be the subject of future work.  

In general, the inequality in (1.1) is diﬃcult to verify/contradict and even sim- ple examples can exhibit rather complicated behavior (see Appendix B). The only reason for which (1.1) fails to hold is the presence of    $L^{2}$    harmonic functions having inﬁnite energy, that is, not belonging to    $H^{1}$  . Moreover, in order to compute deﬁ- ciency indices of the Kir ch ho La plac ian one, roughly speaking, needs to ﬁnd the dimension of the space of    $L^{2}$    harmonic functions and description of self-adjoint ex- tensions requires a thorough understanding of the behavior of    $L^{2}$    harmonic functions at “inﬁnity”. Dictated by a distinguished role of harmonic functions in analysis, there is an enormous amount of literature dedicated to various classes of harmonic functions (positive, bounded etc.), which is further related to diﬀerent notions of boundaries (metric completion, Poisson and Martin boundaries, Royden and Ku- ramochi boundaries etc.) and search for a suitable notion in this context (namely,  $L^{2}$    harmonic functions) is a highly nontrivial problem, which seems not to be very well studied either in the context of  incomplete  manifolds (cf. [61, 62]) or in the case of weighted graphs (see [39, 45]). We further illustrate this by considering the case of rooted  antitrees , a special class of inﬁnite graphs with a particularly high degree of symmetry (see Section 7). Inﬁnite rooted antitrees have exactly one graph end, which makes them a good toy model for our purposes. The above considerations show that the space of ﬁnite energy    $L^{2}$    harmonic functions is nontrivial only if a given metric antitree has ﬁnite total volume and in this case the only such functions are constants. However, adjusting lengths in a suitable way for a concrete polyno- mially growing antitree (Figure 1) we can make the space of    $L^{2}$    harmonic functions as large as we please (even inﬁnite dimensional!).  

otation.    $\mathbb{Z}$  ,    $\mathbb{R}$  ,    $\mathbb{C}$   have their usual  ing;    $\mathbb{Z}_{\geq a}:=\mathbb{Z}\cap[a,\infty)$  .  $z^{*}$  denotes the complex conjugate of  z  $z\in\mathbb{C}$   ∈ . For a given set    $S$  ,   $\#S$   denotes its cardinality if    $S$   is ﬁnite; otherwise we set   $\#S=\infty$  . If it is not explicitly stated otherwise, we shall denote by (  $x_{n}$  ) a sequence   $(x_{n})_{n=0}^{\infty}$  .  $C_{b}(X)$   is the space of bounded, continuous functions on a locally compact space    $X$  .  $C_{0}(X)$   is the space of continuous functions vanishing at inﬁnity. For a ﬁnite or countable set    $X$  ,    $C(X)$   is the set of complex-valued functions on    $X$  .

  $\mathcal{G}_{d}=(\mathcal{V},\mathcal{E})$   is a discrete graph (satisfying Hypothesis 2.1).

  $\mathcal{G}=(\mathcal{G}_{d},|\cdot|)$   is a metric graph (see p. 6).

  $\varrho$   is the natural (geodesi  path metric on    $\mathcal{G}$   (see p. 6).

  $\varrho_{m}$   is the star metric on  V  corresponding to the star weight    $m$   (see (2.13)).

  $\Omega({\mathcal{G}}_{d})$   denotes the graph ends of    $\mathcal{G}_{d}$   (see Deﬁnition 2 ).

  ${\mathfrak{C}}({\mathcal{G}})$   denotes the topological ends of a metric graph  G  (see Deﬁnition 2.2).

  $\mathfrak{C}_{0}(\mathcal{G})$   stays for the ﬁnite volume topological ends of    $\mathcal{G}$   (see Deﬁnition 3.8). G  is the end (Freudenthal) compactiﬁcation of    $\mathcal{G}$   (see p. 7).

  $\mathbf{H}_{0}^{0}$    is the pre-minimal Kir ch ho La plac ian on    $\mathcal{G}$   (see (2.9)).

  $\mathbf{H}_{0}$   is the minimal Kir ch ho La plac ian, the closure of    $\mathbf{H}_{0}^{0}$    in    $L^{2}(\mathcal{G})$   (see (2.9)). 0

  $\mathrm{n}_{\pm}(\mathbf{H}_{0})$   are the deﬁciency indices of    $\mathbf{H}_{0}$   (see (2.15)).

  ${\bf{{H}}}_{F}$   and    ${\bf{H}}_{N}$   are the Friedrichs and Neumann extensions of    $\mathbf{H}_{0}$   (see p. 12 and, respectively, p. 24).

  $\mathbf{H}$   is the maximal Kir ch ho La plac ian on  $\mathcal{G}$   (see (2.8)).  

# 2.  Quantum graphs  

2.1.  Combinatorial and metric graphs.  In what follo ,    $\mathcal{G}_{d}=(\mathcal{V},\mathcal{E})$   will be an unorien aph with countably inﬁnite sets of vertices  V  and edges  E . For two ertices    $u$  ,  v  $v\in\mathcal V$    e shall write    $u\sim v$   if there is an edge    $e_{u,v}\in\mathcal{E}$   conn ctin  $u$   with v . For every  v  ∈V , we denote the set of edges incident to the vertex  v  by  E  $\mathcal{E}_{v}$   and  

$$
\deg_{\mathcal{G}}(v):=\#\{e|\,e\in\mathcal{E}_{v}\}
$$  

is called  the degree  ( valency  or  combinatorial degree ) of a vertex    $v\in\mathcal V$  . When there is no risk of confusion about which graph is involved, we shall simplify and write    $\deg_{\mathcal{G}}$  .    $A$   p  $\mathcal{P}$  ength    $n\in\mathbb{Z}_{\geq0}\cup\{\infty\}$   is a sequence of vertices  $(v_{0},v_{1},.\,.\,,v_{n})$  ) such that  v  $v_{k-1}\sim v_{k}$   for all  $k\in\{1,\cdot\cdot\cdot,n\}$   ∈{ } .  

The following assumption is imposed throughout the paper.  

Hypothesis 2.1.    $\mathcal{G}_{d}$   is  inﬁnite ,  locally ﬁnite  (  $\langle\deg(v)\ <\ \infty$  for every    $v\,\in\,\mathcal V$  ), connected  (for any two vertices    $u,v\in\mathcal{V}$   there is a path connecting  u  and    $v$  ), and simple  (there are no loops or multiple edges).  

Next, let us assign each edge    $e\in\mathcal E$   a ﬁnite length    $|e|\,\in\,(0,\infty)$  . We can then naturally associate with   $\left(\mathcal{G}_{d},|\cdot|\right)=\left(\mathcal{V},\mathcal{E},|\cdot|\right)$   a metric space    $\mathcal{G}$  : ﬁrst, we identify each edge    $e\in\mathcal E$   with a copy of the interval    $\mathcal{T}_{e}:=[0,|e|]$  . The topological space    $\mathcal{G}$  is then obtained by “gluing together” the ends of edges corresponding to the same vertex    $v$   (in the sense of a topological quotient, see, e.g., [13, Chapter 3.2.2]). The topology on    $\mathcal{G}$   is metrizable by the  natural path metric    $\varrho$   — the distance between two points    $x,y\in{\mathcal{G}}$   is deﬁned as the arc length of the “shortest path” connecting them (if    $x$   or    $y$   are not vertices, then we need to allow also paths which start or end in the middle of edges; the length of such paths is naturally deﬁned by taking the corresponding portion of the interval). The metric space    $\mathcal{G}$   arising from the above construction is called a  metric graph  (associated to   $(\mathcal{G}_{d},|\cdot|)=(\mathcal{V},\mathcal{E},|\cdot|))$  .  

Notice that, by deﬁnition,   $(\mathcal{G},\varrho)$   is a  length space  (see [13, Chapter 2.1] for deﬁnitions and further details). Moreover (see, e.g., [40, Chapter 1.1]), a metric graph    $\mathcal{G}$   is a Haus dor topological space with countable base and each    $x\in\mathcal{G}$   has a neighborhood isometric to a star-shaped set    $S(\deg(x),r_{x})$   of degree   $\deg(x)\in\mathbb{Z}_{\geq1}$  ,  

$$
\mathcal{S}(\deg(x),r_{x}):=\big\{z=r\mathrm{e}^{2\pi\mathrm{i}k/\deg(x)}|\,r\in[0,r_{x}),\ k=1,\ldots,\deg(x)\big\}\subset\mathbb{C}.
$$  

Notice that   $\deg(x)$   in (2.2) coincides with the combinatorial degree if    $x$   belongs to the vertex set, and   $\deg(x)=2$   for every non-vertex point    $x$   of    $\mathcal{G}$  .  

Sometimes, we will consider    $\mathcal{G}_{d}$   as a rooted graph with a ﬁxed root    $o\in\mathcal V$  . In this case we denote by    $S_{n}$  ,    $n\in\mathbb{Z}_{\geq0}$   the    $n$  -th combinatorial sphere with respect to the order induced by    $o$   (notice that    $S_{0}=\{o\}$  ).  

2.2.  Graph ends.  One possible deﬁnition of a boundary for an inﬁnite graph is the notion of the so-called  graph ends  (see [30, 38] and [76,  §  21]).  

Deﬁnition 2.1.  A sequence of distinct vertices   $(v_{n})_{n\in\mathbb{Z}_{\geq0}}$   (resp.,   $(v_{n})_{n\in\mathbb{Z}})$   such that    for all    $n\in\mathbb{Z}_{\geq0}$   (resp., for all    $n\in\mathbb{Z}$  ) is called a  ray  (resp.,  double  $v_{n}\sim v_{n+1}$  ray ). A subsequence of such a sequence is called a  tail .  

Two rays    $\mathcal{R}_{1},\mathcal{R}_{2}$   are called  equivalent  – and we w e    $\mathcal{R}_{1}\sim\mathcal{R}_{2}$   – if there is a   third ray containing inﬁnitely many vertices of both  R  and  R . An equivalence class of rays is called a  graph end of    $\mathcal{G}_{d}$   and the se f graph ends will be denoted by   $\Omega({\mathcal{G}}_{d})$  . Moreover, we will write    $\mathcal R\in\omega$   whenever  R  is a ray belonging to the end  $\omega\in\Omega({\mathcal{G}}_{d})$  .  

An important feature of graph ends is their relation to topological ends of a metric graph  $\mathcal{G}$  .  

Deﬁnition 2.2.  Consider sequences    ${\mathcal{U}}=(U_{n})_{n=0}^{\infty}$    of non-empty open connected subsets of    $\mathcal{G}$   with compact boundar s and uch that    $U_{n+1}\subseteq U_{n}$   for all    $n\geq0$   $\textstyle\bigcap_{n\geq0}{\overline{{U_{n}}}}=\emptyset$  . Two such sequences  U  and  U ′  are called  equivalent  if for all  n  $n\geq0$   ≥ there exist    $j$   and    $k$   such that    $U_{n}\supseteq U_{j}^{\prime}$    and    $U_{n}^{\prime}\supseteq U_{k}$  . An equivalence class    $\gamma$   of sequences is called a  topological end  of    $\mathcal{G}$   and  C  ${\mathfrak{C}}({\mathcal{G}})$  G ) denotes the set of topological ends of  $\mathcal{G}$  .  

For locally ﬁnite graphs, there is a bijection between topological ends of a metric graph    ${\mathfrak{C}}({\mathcal{G}})$  graph ends   $\Omega({\mathcal{G}}_{d})$   of the underlying combinatorial graph    $\mathcal{G}_{d}$   (see [76,  $\S~21]$  ], [23,  §  $\S~8.6$   8.6 and also p.277–278]; for the case of graphs which are not locally ﬁnite see [18, 24]).  

Theorem 2.3.  For every topological end    $\gamma\in{\mathfrak{C}}({\mathcal{G}})$   of a locally ﬁnite metric graph  $\mathcal{G}=\left(\mathcal{G}_{d},\lvert\cdot\rvert\right)$   there exists unique graph end    $\omega_{\gamma}\in\Omega\big(\mathcal{G}_{d}\big)$   such that for every sequenc U  representing   , each  U  $U_{n}$   contains a ray from   . Moreover, the map    is a  $\gamma$   $\omega_{\gamma}$   $\gamma\mapsto\omega_{\gamma}$  bijection between    ${\mathfrak{C}}({\mathcal{G}})$   and    $\Omega({\mathcal{G}}_{d})$  .  

Therefore, we may identify topological ends of a metric graph    $\mathcal{G}$   and graph ends of the underlying graph    $\mathcal{G}_{d}$  . We will simply speak of the  ends  of    $\mathcal{G}$  . One obvious advantage of this identiﬁcation is the fact that the deﬁnition of   $\Omega({\mathcal{G}}_{d})$   is purely combinatorial and does not depend on edge lengths.  

Deﬁnition 2.4.  An end    $\omega$   of a graph    $\mathcal{G}_{d}$   is called  free  if there is a ﬁnite set    $X$   of vertices which separates    $\omega$   from all other ends of the graph (i.e. the rays of all ends  $\omega^{\prime}\neq\omega$   end up in diﬀerent connected components of    $\mathcal{V}\setminus X$   than the rays of    $\omega$  ).  

Remark 2.5.  Let us mention several examples.  

(i)    $\mathbb{Z}$   has two ends both of which are free. (ii)    $\mathbb{Z}^{N}$  has one end for all    $N\geq2$  . (iii) A  k -regular tree,    $k\geq3$  , has uncountably many ends, none of w ich is free.  G (iv) If    $\mathcal{G}_{d}$   is a Cayley graph of a ﬁnitely generated inﬁnite group , then the number of ends of    $\mathcal{G}_{d}$   is independent of the generating set and    $\mathcal{G}_{d}$   has either ne, two, or inﬁnitely many ends. Moreover,    $\mathcal{G}_{d}$   has exactly two ends only if G  N  is virtually inﬁnite cyclic (it has a ﬁnite normal subgroup  such that the   quotient group  ${\mathsf{G}}/{\mathsf{N}}$   is isomorphic either to    $\mathbb{Z}$   or    $\mathbb{Z}_{2}*\mathbb{Z}_{2}$  ). These results are due to Freudenthal [30] and Hopf [42] (see also [75]). The classiﬁcation of ﬁnitely generated groups with inﬁnitely many ends is due to Stallings [73].   Let us mention that if  $\mathsf{G}$   has inﬁnitely many ends, then the result of Stallings implies that it contains a non-Abelian free subgroup and hence is non- amenable. For further details we refer to, e.g., [32, Chapter 13]. (v) Let us also mention that by Halin’s theorem [38] every locally ﬁnite graph  $\mathcal{G}_{d}$   with inﬁnitely many ends contains at least one end which is not free.  

One of the main features of graph ends is that they provide a rather reﬁned way of compactifying graphs (see [29] and [23,  §  8.6], [76]). Namely, we introduce a topolog on    $\widehat{\mathcal{G}}\,:=\,\mathcal{G}\cup\mathfrak{C}(\mathcal{G})$  G  G ∪ G ) as follows. For an open subset    $U\subseteq{\mathcal{G}}$  , denote its extension  to  by  

$$
\begin{array}{r}{\hat{U}:=U\cup\{\gamma\in\mathfrak{C}(\mathcal{G})\mid\exists\mathcal{U}=(U_{n})\in\gamma\mathrm{~such~that~}U_{0}\subset U\}.}\end{array}
$$  

Now we can introduce a neighborhood basis of    $\gamma\in{\mathfrak{C}}({\mathcal{G}})$   as follows  

$$
\{{\widehat{U}}\,|\,U\subseteq{\mathcal{G}}{\mathrm{~is~open}},\gamma\in{\widehat{U}}\}.
$$  

This turns    $\widehat{\mathcal G}$  G  into a compact topological space, called the  end (or Freudenthal) compactiﬁcation  of    $\mathcal{G}$  .  

Remark 2.6.  Notice that an end    $\gamma\,\in\,{\mathfrak{C}}({\mathcal{G}})$   is free exactly when    $\{\gamma\}$   is open as bset of    ${\mathfrak{C}}({\mathcal{G}})$   ${\mathfrak{C}}({\mathcal{G}})$   carries the induced topo   G ). This is furthe equivalent to the existence of a connected subgraph  G  $\mathcal G^{\gamma}$  γ   with compact boundary  $^\dagger$     $\partial\mathcal{G}^{\gamma}$  at  U  $U_{n}\subseteq\mathcal{G}^{\gamma}$   ⊆G eventually for an e  U  ${\mathcal{U}}=(U_{n})$  ) represent  $\gamma$  and  $U_{n}^{\prime}\cap\mathcal{G}^{\gamma}=\emptyset$  ∩G eventually for all sequences  U  ${\mathcal{U}}^{\prime}=(U_{n}^{\prime})$  ) representing an end  $\gamma^{\prime}\neq\gamma$   ̸ .  

Let us mention that topological ends can be obtained in a constructive way by means of compact exhaustions. Namely, a sequence of connected subgraphs   $\left(\mathcal{F}_{n}\right)$   $\mathcal{G}$  such   ${\mathcal{F}}_{n}$   has ﬁnitely many vertices and edges,    ${\mathcal{F}}_{n}\subseteq{\mathcal{F}}_{n+1}$   for all  $n\geq0$   ≥ 0 and    $\textstyle\bigcup_{n}{\mathcal{F}}_{n}={\mathcal{G}}$  S   F  G  is called a  co pact exhaustion  of  G . Clearly, each  F  ${\mathcal{F}}_{n}$    y be identiﬁed with a compact subset of  G . Now iteratively construct a sequence (  $U_{n}$  ) by choosing in each step a non-compact, connected component    $U_{n}$   of    ${\mathcal{G}}\backslash{\mathcal{F}}_{n}$   satisfying  $U_{n}\subseteq U_{n-1}$   is easy to check that   sequence (  $U_{n}$  ) deﬁnes a topological end  γ  $\gamma\,\in\,{\mathfrak{C}}({\mathcal{G}})$   ∈ G ) and in fact all ends  γ  $\gamma\,\in\,{\mathfrak{C}}({\mathcal{G}})$   ∈ G ) are obtained by this construction. Notice also that the open subsets    $U_{n}$   of such representations    $\gamma\,\sim\,(U_{n})$   (actually, their topological closures, since we need to add endpoints of edges which also belong to    $\mathcal{V}(\mathcal{F}_{n}).$  ) can again be identiﬁed with connected subgraphs    $\mathcal{G}_{n}(\gamma):=\overline{{U_{n}}}$   and we will frequently use this fact.  

Let us ﬁnish this section with a few more notations. Suppose    $\mathcal{R}$   is a ray or a ﬁnite path without self-intersections in    $\mathcal{G}_{d}$  . We may identify    $\mathcal{R}$   with a subgraph of  $\mathcal{G}_{d}$  nd hence with a subset of    $\mathcal{G}$  , i.e., we can consider it as the union of all edges of  R . The latter can further be identiﬁed with the interval    $I_{\mathcal{R}}:=[0,|\mathcal{R}|)$   of length  $|\mathcal{R}|$  , where  

$$
|{\mathcal{R}}|:=\sum_{e\in{\mathcal{R}}}|e|.
$$  

Also, we need to consider paths – and in particular rays   $-$   in    $\mathcal{G}$   starting or ending at a non-vertex point. In particular, given a path   $(v_{0},v_{1},.\,.\,.\,,v_{N})$   and a point    $x$   in the interior of some edge    $e$   attached to    $v_{0}$  ,    $e\neq e_{v_{0},v_{1}}$  , we add the interval   $[x,v_{0}]\subseteq e$  to   $(v_{0},v_{1},.\,.\,.\,,v_{N})$  . For the resulting set, we shall write   $(x,v_{0},v_{1},.\,.\,,v_{N})$   and call it a  non-vertex path ; and likewise for rays. The set of all non-vertex rays will be denoted by    $\Re(\mathcal{G})$  .  

2.3.  KirchhoﬀLapla  Let    $\mathcal{G}$   be a metric graph satisfying Hypothesis 2.1. Upon identifying every  e  ∈E  with a copy of the interval    $\mathcal{T}_{e}=[0,|e|]$  , we denote by  

$$
L^{2}(e):=L^{2}(\mathcal{Z}_{e};d x_{e})
$$  

the    $L^{2}$  -space for the (unweighted) Lebesgue measure    $d x_{e}$   on    $\mathcal{L}_{e}$   and introduce the Hilbert space    $L^{2}(\mathcal{G})$   of functions    $f\colon G\to\mathbb{C}$   such that  

$$
L^{2}(\mathcal G):=\bigoplus_{e\in\mathcal E}L^{2}(e)=\Big\{f=\{f_{e}\}_{e\in\mathcal E}\,\big|\,f_{e}\in L^{2}(e),\,\sum_{e\in\mathcal E}\|f_{e}\|_{L^{2}(e)}^{2}<\infty\Big\}.
$$  

The subspace of compactly supported    $L^{2}(\mathcal{G})$   functions will be denoted by  

$$
L_{c}^{2}(\mathcal{G}):=\left\{f\in L^{2}(\mathcal{G})|\;f\neq0\;\mathrm{only~on~finitely~many~edges}\;e\in\mathcal{E}\right\}
$$  

For every    $e\in\mathcal E$   consider the maximal operator   $\mathrm{H}_{e,\operatorname*{max}}$   acting on functions    $f\in H^{2}(e)$  as a negative second derivative. Here and below    $H^{s}(e)$   for    $s\geq0$   denotes the usual Sobolev space on    $e$   (see, e.g., [12, Chapter 8]). In particular,    $H^{0}(e)=L^{2}(e)$   and  

$$
H^{1}(e)=\{f\in A C(e)|\,f^{\prime}\in L^{2}(e)\},\quad H^{2}(e)=\{f\in H^{1}(e)|\,f^{\prime}\in H^{1}(e)\}.
$$  

This deﬁnes the maximal operator on    $L^{2}(\mathcal{G})$   by  

$$
\mathbf{H}_{\mathrm{max}}:=\bigoplus_{e\in\mathcal{E}}\mathrm{H}_{e,\mathrm{max}},\qquad\mathrm{H}_{e,\mathrm{max}}=-\frac{\mathrm{d}^{2}}{\mathrm{d}x_{e}^{2}},\quad\mathrm{dom}(\mathrm{H}_{e,\mathrm{max}})=H^{2}(e).
$$  

If    $v$   is a vertex of the edge    $e\in\mathcal E$  , then for every    $f\in H^{2}(e)$   the following quantities  

$$
f_{e}(v):=\operatorname*{lim}_{x_{e}\to v}f(x_{e}),\qquad\qquad\qquad f_{e}^{\prime}(v):=\operatorname*{lim}_{x_{e}\to v}\frac{f(x_{e})-f(v)}{|x_{e}-v|},
$$  

are well deﬁned. Considering    $\mathcal{G}$   as the union of all edges glued together at certain endpoints, let us equip a metric graph with the Laplace operator. The Kirchhoﬀ (also called  standard  or  Kirchhoﬀ–Neumann ) boundary conditions at every vertex  $v\in\mathcal V$   are then given by  

$$
\left\{{\mathrm{~is~continuous~at~}}v,\right.
$$  

Imposing these boundary conditions on the maximal domain   $\mathrm{dom}(\mathbf{H}_{\mathrm{max}})$   yields the maximal KirchhoﬀLaplacian  

$$
\begin{array}{r l}&{\mathrm{\bf~H}:=\mathrm{\bf~H}_{\mathrm{max}}\mid\mathrm{dom}(\mathrm{\bfH}),}\\ &{\mathrm{dom}(\mathrm{\bfH})=\{f\in\mathrm{dom}(\mathrm{\bfH}_{\mathrm{max}})\mid f\mathrm{\satisfies\}(2.7)\mathrm{\for\any\}v\in\mathcal{V}\}.}\end{array}
$$  

Restricting further to compactly supported functions we end up with the pre- minimal operator  

$$
\begin{array}{r l}&{\qquad\qquad\mathbf{H}_{0}^{0}:=\mathbf{H}_{\operatorname*{max}}\mid\mathrm{dom}(\mathbf{H}_{0}^{0}),}\\ &{\mathrm{dom}(\mathbf{H}_{0}^{0})=\{f\in\mathrm{dom}(\mathbf{H}_{\operatorname*{max}})\cap L_{c}^{2}(\mathcal{G})|\,f\mathrm{~satisfies~(2.7)~for~any~}v\in\mathcal{V}\}.}\end{array}
$$  

Integrating by parts one obtains  

$$
\langle\mathbf{H}_{0}^{0}f,f\rangle_{L^{2}(\mathcal{G})}=\int_{\mathcal{G}}|f^{\prime}(x)|^{2}\ d x,\qquad f\in\mathrm{dom}(\mathbf{H}_{0}^{0}),
$$  

and hence    $\mathbf{H}_{0}^{0}$    is a non-negative symmetric operator. We call its closure    $\mathbf{H}_{0}:=\overline{{\mathbf{H}_{0}^{0}}}$  in    $L^{2}(\mathcal{G})$   the minimal Kir ch ho La plac ian . The following result is well-known (see, e.g., [16, Lemma 3.9]).  

Lemma 2.7.  Let  $\mathcal{G}$   be a metric graph. Then  

$$
\mathbf{H}_{0}^{*}=\mathbf{H}.
$$  

2.4.  Deﬁciency indices.  In the following we are interested in the question whether

  $\mathbf{H}_{0}$   is self-adjoint, or equivalently whether the equality    $\mathbf{H}_{0}=\mathbf{H}$   holds true. Let us recall one suﬃcient condition. Deﬁne the  star weight    $m(v)$   of a vertex    $v\in\mathcal V$   by  

$$
m(v):=\sum_{e\in\mathcal{E}_{v}}|e|=\mathrm{vol}(\mathcal{E}_{v}),
$$  

and also introduce the  star path metric  on  $\nu$   by  

$$
\varrho_{m}(u,v):=\operatorname*{inf}_{\stackrel{{\mathscr{P}}=(v_{0},\ldots,v_{n})}{u=v_{0},\ v=v_{n}}}\sum_{v_{k}\in{\mathscr{P}}}m(v_{k}).
$$  

Theorem 2.8  ([27]) .  I  $\boldsymbol{\mathscr{f}}\left(\mathcal{V},\varrho_{m}\right)$   is complete as a metric space, then    $\mathbf{H}_{0}^{0}$    is essentially self-adjoint and    $\overline{{\mathbf{H}_{0}^{0}}}=\mathbf{H}_{0}=\mathbf{H}$  .  

If a symmetric operator is not (essentially) self-adjoint, then the degree of its non- self-adjointness is determined by its  deﬁciency indices . Recall that the  deﬁciency subspace    $\mathcal{N}_{z}(\mathbf{H}_{0})$   of    $\mathbf{H}_{0}$   is deﬁned by  

$$
\begin{array}{r}{\mathcal{N}_{z}\big(\mathbf{H}_{0}\big):=\ker(\mathbf{H}_{0}^{*}-z)=\ker(\mathbf{H}-z),\quad z\in{\mathbb{C}}.}\end{array}
$$  

The numbers  

$$
\mathrm{n}_{\pm}(\mathbf{H}_{0}):=\mathrm{dim}\mathcal{N}_{\pm\mathrm{i}}(\mathbf{H}_{0})=\mathrm{dim}\,\mathrm{ker}(\mathbf{H}\mp\mathrm{i})
$$  

are called the deﬁciency indices of    $\mathbf{H}_{0}$  . Notice that   $\mathrm{n_{+}}(\mathbf{H}_{0})=\mathrm{n_{-}}(\mathbf{H}_{0})$   since    $\mathbf{H}_{0}$   is non-negative. Moreover,    $\mathbf{H}_{0}$   is self-adjoint exactly when   $\mathrm{n_{+}}(\mathbf{H}_{0})=\mathrm{n_{-}}(\mathbf{H}_{0})=0$  .  

Lemma 2.9.  If    $0$   is a point of regular type for    $\mathbf{H}_{0}$  , then †  

$$
\mathrm{n}_{\pm}(\mathbf{H}_{0})=\dim\ker(\mathbf{H}).
$$  

Proof.  The claim immediately follows from [1,  §  78] or [69, Prop. 3.3]. Indeed, the set of regular points of    $\mathbf{H}_{0}$   is an open subset of    $\mathbb{C}$  . Moreover, by the Krasnoselskii– Krein theorem (see, e.g., [1,  §  78] or [69, Prop. 2.4]),   $\mathrm{dim}\,\mathcal{N}_{z}\big(\mathbf{H}_{0}\big)$   is constant on each connected component of the set of regular type points of    $\mathbf{H}_{0}$  . Since    $\mathbf{H}_{0}$   is symmetric, each    $z\in\mathbb{C}\setminus\mathbb{R}$   is a point of regular type for    $\mathbf{H}_{0}$  . Therefore, if   $0$   is a point of regular type for    $\mathbf{H}_{0}$  , we immediately get  

$$
\dim\ker(\mathbf{H})=\dim{\mathcal{N}}_{0}(\mathbf{H}_{0})=\mathrm{n}_{+}(\mathbf{H}_{0})=\mathrm{n}_{-}(\mathbf{H}_{0}).
$$  

Using the Rayleigh quotient, deﬁne  

$$
\lambda_{0}(\mathcal{G}):=\operatorname*{inf}_{\substack{f\in\mathrm{dom}(\mathbf{H}_{0})}}\left\langle\mathbf{H}_{0}f,f\right\rangle_{L^{2}(\mathcal{G})}=\operatorname*{inf}_{\substack{f\in\mathrm{dom}(\mathbf{H}_{0})}}\int_{\mathcal{G}}|f^{\prime}|^{2}d x.
$$  

Noting that the operator    $\mathbf{H}_{0}$   is non-negative,   $0$   is a point of regular type for    $\mathbf{H}_{0}$   if  $\lambda_{0}(\mathcal{G})>0$  . Thus, we arrive at the following result.  

Corollary 2.10.  If    $\lambda_{0}(\mathcal{G})>0$  , then  (2.16)  holds true.  

The positivity of    $\lambda_{0}(\mathcal{G})$   is known in the following simple situation.  

Corollary 2.11.  If    $\mathcal{G}$   has ﬁnite total volume,  

$$
\operatorname{vol}(\mathcal{G}):=\sum_{e\in\mathcal{E}}|e|<\infty,
$$  

then    $\mathbf{H}_{0}$   is not self-adjoint and  (2.16)  holds true.  

Proof.  Indeed, by the Cheeger-type estimate [55, Corollary 3.5(iv)], we have  

$$
\lambda_{0}(\mathcal{G})\geq\frac{1}{4\,\mathrm{vol}(\mathcal{G})^{2}}>0,
$$  

and hence (2.16) holds true by Corollary 2.10. Moreover,  $\mathbb{1}_{\mathcal{G}}\,\in\,\ker(\mathbf{H})$  , where  $\mathbb{1}_{\mathcal{G}}$  denotes the constant function on  $\mathcal{G}$  , and hence  

$$
\begin{array}{r}{\mathrm{n}_{\pm}(\mathbf{H}_{0})=\dim(\ker\mathbf{H})\geq1.}\end{array}
$$  

It remains to notice that    $\mathbf{H}_{0}$   is self-adjoint exactly when   $\mathrm{n}_{\pm}(\mathbf{H}_{0})=0$  .  

Remark 2.12.  By [55, Theorem 3.4],    $\lambda_{0}(\mathcal{G})\,>\,0$   holds true if the isoperimetric constant    $\alpha(\mathcal{G})$   of the metric graph    $\mathcal{G}$   is positive. For antitrees, the isoperimetric constant is tightly related to the structure of its combinatorial spheres (see [56, Theorem 7.1]). If    $\mathcal{G}_{d}$   is the edge graph of a tessellation of    $\mathbb{R}^{2}$  , then positivity of  $\alpha(\mathcal{G})$   can be deduced from certain curvature-type quantities [65].  

On the other hand, by [55, Corollary 4.5(i)],    $\lambda_{0}(\mathcal{G})>0$   holds true if the combi- natorial isoperimetric constant of    $\mathcal{G}_{d}$   is positive and    $\begin{array}{r}{\ell^{*}(\mathcal{G}):=\operatorname*{sup}_{e\in\mathcal{E}}|e|<\infty}\end{array}$  . For example, this holds true if    $\mathcal{G}_{d}$   is an inﬁnite tree without leaves [55, Lemma 8.1] or if  $\mathcal{G}_{d}$   is a Cayley graph of a non-amenable ﬁnitely generated group [55, Lemma 8.12(i)].  

Finally, let us remark that   $\ker(\mathbf{H})\,=\,\mathbb{H}(\mathcal{G})\cap L^{2}(\mathcal{G})$  , where    $\mathbb{H}(\mathcal{G})$   denotes the space of  harmonic functions  on    $\mathcal{G}$  , that is, the set  “edgewise” aﬃne functions satisfying Kir ch ho conditions (2.7) at each vertex  ∈V . Notice that every function  $f\in\mathbb{H}(\mathcal{G})$   is uniquely determined by its vertex values    $\mathbf{f}:=f|\nu=(f(v))_{v\in\mathcal{V}}$  . Recall also the following result (see, e.g., [55, eq. (2.32)]).  

Lemma 2.13.  Let    $\mathcal{G}$   be a metric graph satisfying the assumptions in Hypothesis 2.1. If    $f\in\mathbb{H}({\mathcal{G}})$  , then    $f\in L^{2}(\mathcal G)$   if and only if    $\mathbf{f}\in\ell^{2}(\mathcal{V};m)$  , that is,  

$$
\sum_{v\in\mathcal{V}}|f(v)|^{2}m(v)<\infty.
$$  

Remark 2.14.  The above considerations indicate that in order to understand the deﬁciency indices of the Kir ch ho La plac ian one needs to ﬁnd the dimension of the space of    $L^{2}$    harmonic (or, more carefully,    $\lambda$  -harmonic) functions. Moreover, in order to describe self-adjoint extensions one has to understand the behavior of  $L^{2}$    harmonic functions at “inﬁnity”, that is, near a “boundary” of a given metric graph. However, graphs admit a lot of diﬀerent notions of boundary (ends, Poisson and Martin boundaries, Royden and Kuramochi boundary etc.) and search for a suitable notion in this context (namely,    $L^{2}$    harmonic functions) is a highly non- trivial problem, which seems to be not very well studied neither in the context of incomplete manifolds nor in the case of weighted graphs.  

Let us also mention that recently there has been a tremendous amount of work devoted to the study of harmonic functions and self-adjoint extensions of Laplacians on weighted graph (we only refer to a brief selection of articles [19, 35, 39, 43, 44, 45, 46, 51]).  

This section deals with the Sobolev space    $H^{1}$    on metric graphs. Its importance stems, in particular, from the fact that it serves as a form domain for a large class of self-adjoint extensions of    $\mathbf{H}_{0}$  .  

# 3.1.    $H^{1}(\mathcal G)$   and boundary values.  First recall that  

$$
H^{1}(\mathcal{G})=\big\{f\in L^{2}(\mathcal{G})\cap C(\mathcal{G})\big|\;f_{e}\in H^{1}(e)\;\mathrm{for~all}\;e\in\mathcal{E},\;\|f^{\prime}\|_{L^{2}(\mathcal{G})}^{2}<\infty\big\},
$$  

where    $C(\mathcal{G})$   is the space of continuous complex-valued functions on    $\mathcal{G}$   and  

$$
\lVert f^{\prime}\rVert_{L^{2}(\mathcal{G})}^{2}:=\sum_{e\in\mathcal{E}}\lVert f_{e}^{\prime}\rVert_{L^{2}(e)}^{2}.
$$  

Notice that   $\left(H^{1}(\mathcal{G}),\|\cdot\|_{H^{1}}\right)$   is a Hilbert space when equipped with the standard norm  

$$
\Vert f\Vert_{H^{1}(\mathcal{G})}^{2}:=\Vert f\Vert_{L^{2}(\mathcal{G})}^{2}+\Vert f^{\prime}\Vert_{L^{2}(\mathcal{G})}^{2}=\sum_{e\in\mathcal{E}}\Vert f_{e}\Vert_{H^{1}(e)}^{2},\quad f\in H^{1}(\mathcal{G}).
$$  

Moreover,   $\mathrm{dom}(\mathbf{H}_{0}^{0})\subset H^{1}(\mathcal{G})$   ⊂ G ) and we deﬁne    $H_{0}^{1}(\mathcal{G})$  G ) as the closure of   $\mathrm{dom}(\mathbf{H}_{0}^{0})$  ) with respect to    $\|\cdot\|_{H^{1}(\mathcal{G})}$  .  

Remark 3.1.  If    $\mathbf{H}_{0}^{0}$    is essentially self-adjoint, then    $H^{1}(\mathcal{G})=H_{0}^{1}(\mathcal{G})$  G ). However, the converse is not true in general. In fact this equality is tightly connected to the uniqueness of Markovian extensions of    $\mathbf{H}_{0}$   and, as we shall see, it is possible to characterize it in terms of topological ends of    $\mathcal{G}$   (see Corollary 5.5 below).  

Notice also that    $H_{0}^{1}(\mathcal G)$  G ) is the form domain of the Friedrichs extension    ${\bf{{H}}}_{F}$    of    $\mathbf{H}_{0}^{0}$  and    $\lambda_{0}(\mathcal{G})$   deﬁned by (2.17) is the bottom of the spectrum of    ${\bf{{H}}}_{F}$  .  

By deﬁnition,    $H^{1}(\mathcal G)$   is densely and continuously embedded in    $L^{2}(\mathcal{G})$  . Lemma 3.2.    $H^{1}(\mathcal G)$   is continuously embedded in    $C_{b}(\mathcal{G})=C(\mathcal{G})\cap L^{\infty}(\mathcal{G})$   and  

$$
\|f\|_{\infty}:=\operatorname*{sup}_{x\in\mathcal{G}}|f(x)|\le C_{\mathcal{G}}\|f\|_{H^{1}(\mathcal{G})}
$$  

holds for all    $f\,\in\,H^{1}(\mathcal G)$   with  $C_{\mathcal{G}}\,:=\,\sqrt{\coth\left({\textstyle{\frac{1}{2}}}\operatorname*{sup}_{\mathcal{R}}|\mathcal{R}|\right)}$  q    , where the supremum is taken over all non-vertex paths without self-intersections.  

Proof.  For every interval    $\mathcal{L}\subseteq\mathbb{R}$   the embedding of    $H^{1}(\mathcal{Z})$   into    $L^{\infty}(\mathcal{T})$   is bounded and  

$$
\operatorname*{sup}_{x\in\mathcal{Z}}|f(x)|\le C_{|\mathcal{Z}|}\|f\|_{H^{1}(\mathcal{Z})}
$$  

holds for all    $f\,\in\,H^{1}({\mathcal{T}})$   with  C  $C_{|\mathcal{Z}|}\,=\,\sqrt{\coth(|\mathcal{Z}|)}$   (see [60]). Notice that we may identify the  striction    $f|_{\mathcal{R}}$   of  f  $f\;\in\;H^{1}(\mathcal{G})$   ∈ G ) to a (non-vertex) path without self- intersections  R  with a function on    $\mathcal{T}_{\mathcal{R}}=[0,|\mathcal{R}|)$  . It is easy to check that upon this identiﬁcation    $f|_{\mathcal{R}}\in H^{1}(\mathcal{Z}_{\mathcal{R}})$   and   $(f|_{\mathcal{R}})^{\prime}=f^{\prime}|_{\mathcal{R}}$  .  

Suppose now that  R  is a ﬁxed non-vert  path without self-intersections in    $\mathcal{G}$  . Then for every    $x\,\in\,{\mathcal{G}}$  , connecting    $x$   and  R  by some ﬁnite non-vertex path    $\mathcal{R}_{0}$  , we see that there exists a non-vertex pa  without self-intersections    $\mathcal{R}_{x}$   such that  $x\,\in\,\mathcal{R}_{x}$   and    $|\mathcal{R}_{x}|\,\geq\,|\mathcal{R}|/2$   (if    $x$   lies on  R  already,  en the connecting argument is superﬂuous and we can simply take a portion of  R ). Applying (3.3) to    $\mathcal{R}_{x}$  ,  easily deduce the estimate (3.2). □  

Remark 3.3.  The diameter of    $\mathcal{G}$   (as a metric space   $(\mathcal{G},\varrho)$  ) is deﬁned by  

$$
\mathrm{diam}(\mathscr{G}):=\operatorname*{sup}_{x,y\in\mathscr{G}}\varrho(x,y).
$$  

Therefore,   $\begin{array}{r}{\mathrm{diam}(\mathscr{G})\leq\operatorname*{sup}_{\mathscr{R}}|\mathscr{R}|}\end{array}$   and hence  $C_{\mathcal{G}}\leq\sqrt{\coth\left(\frac{1}{2}\operatorname{diam}(\mathcal{G})\right)}$  .  

The above considerations, in particular, imply the following crucial property of  $H^{1}$  -functions: if    ${\mathcal{R}}=(v_{n})$   is a ray, then  

$$
f(\gamma_{\mathcal{R}}):=\operatorname*{lim}_{n\to\infty}f(v_{n})
$$  

exists. Indeed, upon the identiﬁcation of    $\mathcal{R}$   with the interval    $\mathcal{T}_{\mathcal{R}}\,=\,[0,|\mathcal{R}|)$  , the latter is an immediate corollary of the description of a Sobolev space  H  $H^{1}$    in one dimension — for a bounded interval this follows from [12, Theorem 8.2] and in the unbounded case see [12, Corollary 8.9]. Moreover, this limit only depends on the equivalence c  of    $\mathcal{R}$   (indeed, for any two equivalent rays  $\mathcal{R}$   and  $\mathcal{R}^{\prime}$    there   exists a third ray  R containing inﬁnitely many vertices of both  R  and  R , which immediately implies that    $f(\gamma_{\mathcal{R}})=f(\gamma_{\mathcal{R}^{\prime\prime}})=f(\gamma_{\mathcal{R}^{\prime}}))$  ). This enables us to introduce the following notion.  

Deﬁnition 3.4.  For every    $f\in H^{1}(\mathcal G)$   and a (topological) end    $\gamma\in{\mathfrak{C}}({\mathcal{G}})$  , we deﬁne  

$$
f(\gamma):=f(\gamma_{\mathscr{R}}),
$$  

where    $\mathcal{R}\in\omega_{\gamma}$   is any ray belonging to the corresponding graph end    $\omega_{\gamma}$   (see Theo- rem 2.3). Sometimes we shall also write    $f(\omega_{\gamma}):=f(\gamma)$  .  

It turns out that (3.5) enables us to obtain an extension by continuity of every function    $f\in\ H^{1}(\mathcal G)$   to the end compactiﬁc  $\widehat{\mathcal G}$  G  of    $\mathcal{G}$   (see Section 2.2).  

Lemma 3.5.  Let  G  be a metric graph and  $\gamma\in{\mathfrak{C}}({\mathcal{G}})$   ∈ G . If    $f\in H^{1}(\mathcal G)$  , then  

$$
\operatorname*{lim}_{n\to\infty}\operatorname*{sup}_{x\in U_{n}}|f(x)-f(\gamma)|=0
$$  

for every sequence    ${\mathcal{U}}=(U_{n})$   representing    $\gamma$  .  

Proof.  Let    $\gamma\in{\mathfrak{C}}({\mathcal{G}})$   and let    ${\mathcal{U}}=(U_{n})$   be a sequence representing    $\gamma$  . Let also  

$$
\mathfrak{R}_{n}(\gamma):=\{\mathcal{R}\in\mathfrak{R}(\mathcal{G})|\ \mathcal{R}\subseteq U_{n}\}
$$  

be the set of all non-vertex rays contained in    $U_{n}$  ,    $n\geq0$  .  

We proceed by case distinction. First, assume that for    $n$   suﬃciently large, all   rays in  $\Re_{n}(\gamma)$   have length at most one. If    $x\in U_{n}$  , then there exists a (non-vertex) ray    $\mathcal{R}_{x}\,\in\,\mathfrak{R}_{n}(\gamma)$   such that    ${\mathcal R}_{x}\;=\;(x,v_{0},.\,.\,.\,)$   and its tail    ${\mathcal{R}}\,:=\,\left(v_{0},v_{1},.\,.\,.\right)$   (see Deﬁnition 2.1) belong to    $\omega_{\gamma}$  .  

By our assumption,    $|\mathcal{R}_{x}|\leq1$   and hence  

$$
|f(\gamma)-f(x)|=|f(\gamma_{\mathcal{R}_{x}})-f(x)|=\Big|\int_{\mathcal{R}_{x}}f^{\prime}(y)\;d y\Big|\leq\|f^{\prime}\|_{L^{2}(\mathcal{R}_{x})}\leq\|f^{\prime}\|_{L^{2}(U_{n})}.
$$  

Since    $x\in U_{n}$   is arbitrary, this implies  

$$
\operatorname*{sup}_{x\in U_{n}}|f(\gamma)-f(x)|\leq\|f^{\prime}\|_{L^{2}(U_{n})}.
$$  

Since    ${\mathcal{U}}=(U_{n})$   represents    $\gamma$  ,  $\begin{array}{r}{\bigcap_{n}\overline{{U_{n}}}=\emptyset}\end{array}$  and hence   $\begin{array}{r}{\operatorname*{lim}_{n\to\infty}\|f^{\prime}\|_{L^{2}(U_{n})}=0}\end{array}$  . This implies (3.6).  

Assume now that for every    $n\in\mathbb{Z}_{\geq0}$   there is a ray    $\mathcal{R}\,\in\,\mathfrak{R}_{n}(\gamma)$   with    $|\mathcal{R}|\,>\,1$  . Take    $n\geq0$   and choose an    $x\in U_{n}$  . We can ﬁnd a ﬁnite (non-vertex) path without self-i rsections    ${\mathcal{R}}_{x}\,\subseteq\,U_{n}$   such that    $x\,\in\,\mathcal{R}_{x}$   and    $|\mathcal{R}_{x}|\,=\,1/2$   (take into account that  $U_{n}$   contains at least one ray of length greater than 1). Hence we get  

$$
|f(x)|\leq\operatorname*{sup}_{y\in{\mathcal{R}}_{x}}|f(y)|\leq C_{1/2}\|f\|_{H^{1}({\mathcal{R}}_{x})}\leq C_{1/2}\|f\|_{H^{1}(U_{n})},
$$  

where  $C_{1/2}=\sqrt{\coth(1/2)}$  2) is the constant from (3.3). Since    $x\in U_{n}$   is arbitrary,  

$$
\operatorname*{sup}_{x\in U_{n}}|f(x)|\leq C_{1/2}\|f\|_{H^{1}(U_{n})}.
$$  

,    $\begin{array}{r}{\bigcap_{n}\overline{{U_{n}}}\,=\,\emptyset}\end{array}$  and hence   $\begin{array}{r}{\operatorname*{sup}_{x\in U_{n}}|f(x)|\,=\,o(1)}\end{array}$   as    $n\rightarrow\infty$  . It remains to notice that  f  $f(\gamma)\,=\,0$  ) = 0. Indeed, by Theorem 2.3, for every  n  $n\ \geq\ 0$   ≥ 0 there is a ray  $\widetilde{\mathcal{R}}_{n}\in\omega_{\gamma}$   such that  ${\widetilde{\mathcal{R}}}_{n}\subseteq U_{n}$  R  and hence  

$$
|f(\gamma)|=|f(\gamma_{\widetilde{\mathscr{R}}_{n}})|\leq\operatorname*{sup}_{x\in U_{n}}|f(x)|=o(1)
$$  

as    $n\to\infty$  . This ﬁnishes the proof.  

Taking into account the topology on  $\widehat{\mathcal{G}}=\mathcal{G}\cup\mathfrak{C}(\mathcal{G})$  G  G ∪ G ), the next result is a direct consequence of Lemma 3.2 and Lemma 3.5.  

Proposition 3.6.  Each    $f\in H^{1}(\mathcal G)$   has a unique continuous extension to the end compactiﬁcation G  of    $\mathcal{G}$   and this extension is given by  (3.5) . Moreover,  

$$
\Vert f\Vert_{\infty}=\operatorname*{sup}_{x\in\widehat{\mathcal{G}}}|f(x)|\leq C_{\mathcal{G}}\Vert f\Vert_{H^{1}(\mathcal{G})}.
$$  

3.2.  Nontrivial and ﬁnite volume ends.  Observe that some ends lead to trivial boundary values for    $H^{1}$    fu ctions. For example,    $f(\gamma)\,=\,0$   for all    $f\,\in\,H^{1}(\mathcal{G})$   if  $\omega_{\gamma}\in\Omega\big(\mathcal{G}_{d}\big)$   contains a ray  R  with inﬁnite length    $|\mathcal{R}|=\infty$  the oth might happen that all rays have ﬁnite length, however,  $f(\gamma)=0$  ) = 0 for all  f  $f\in H^{1}(\mathcal G)$   ∈ G (see, e.g., the second step in the proof of Lemma 3.5).  

Deﬁnition 3.7.  A topological end    $\gamma\,\in\,{\mathfrak{C}}({\mathcal{G}})$   is called  nontrivial  if    $f(\gamma)\,\neq\,0$   for some    $f\in H^{1}(\mathcal G)$  .  

We also need the following notion.  

Deﬁnition 3.8.  A topological end    $\gamma\in{\mathfrak{C}}({\mathcal{G}})$   has  ﬁnite volume  (or, more precisely, ﬁnite volume neighborhood)  if there is a sequence    ${\mathcal{U}}=(U_{n})$   representing    $\gamma$   such that   $\mathrm{vol}(U_{n})<\infty$  for some    $n$  . Otherwise    $\gamma$   has  inﬁnite volume . The set of all ﬁnite volume ends is denoted by    $\mathfrak{C}_{0}(\mathcal{G})$  . Here and below,   $\operatorname{vol}(A)$   is the Lebesgue measure of a measurable set    $A\subseteq{\mathcal{G}}$  .  

Remark 3.9.  If    ${\mathfrak{C}}({\mathcal{G}})$   contains only one end, then this end has ﬁnite volume exactly when   $\mathrm{vol}(\mathcal G)<\infty$  . Analogously, if    $\gamma\in{\mathfrak{C}}({\mathcal{G}})$   is a free end, then there is a ﬁnite set of vertices    $X$   separating    from all other ends and hence this end has ﬁnite volume  $\omega_{\gamma}$  exactly when the corresponding connected component  $\mathcal{G}_{\gamma}$   has ﬁnite total volume.  

If    $\gamma$   is not free, then the situation is more complicated. For example, for a rooted tree    $\mathcal{G}=\mathcal{T}_{o}$   the ends are in one-to-one correspondence with the rays from the root    $o$  and hence one may possibly confuse the notion of a ﬁnite/inﬁnite volume of an end with the ﬁnite/inﬁnite length of the corresponding ray. More speciﬁcally, let    $\gamma$   be an end of    $\mathcal{T}_{o}$   and let    $\mathcal{R}_{\gamma}=(o,v_{1},v_{2},.\,.\,.\,)$   be the corresponding ray. For each    $n\geq1$  , let    $\mathcal{T}_{n}$   be the subtree of    $\mathcal{T}_{o}$   having its root at    $v_{n}$   and containing all the “descendant” vertices of    $v_{n}$  . Then by deﬁnition    $\gamma$   has ﬁnite volume (neighborhood) if and only if there is    $n\geq1$   such that the corresponding subtree    $\mathcal{T}_{n}$   has ﬁnite total volume. In particular, this implies that    $\mathcal{G}$   would have uncountably many ﬁnite volume ends in this case (here we assume for simplicity that all vertices are essential, that is,  $\deg(v)>2$   for all    $v\in\mathcal V$  ). In particular,    $|\mathcal{R}_{\gamma}|<\infty$  is a necessary but not suﬃcient condition for    $\gamma$   to have ﬁnite volume.  

It turns out that nontrivial and ﬁnite volume ends are closely connected.  

Theorem 3.10.  Let    $\mathcal{G}$   be a metric graph. Then    $\gamma\in{\mathfrak{C}}({\mathcal{G}})$   is nontrivial if and only if    $\gamma$   has ﬁnite volume. Moreover, for any ﬁnite collection of distinct nontrivial ends  $\{\gamma_{j}\}_{j=1}^{N}$    there exists    $f\in H^{1}(\mathcal{G})\cap\mathrm{dom}(\mathbf{H})$   such that    $f(\gamma_{1})=1$   and    $f(\gamma_{2})=\cdot\cdot\cdot=$   $f(\gamma_{N})=0$  .  

Proof.  It is not diﬃcult to see that    $f(\gamma)\,=\,0$   for all    $f\,\in\,H^{1}(\mathcal G)$   if    $\gamma$   has inﬁnite volume. Indeed, assuming that there is    $f\in H^{1}(\mathcal G)$   such that    $f(\gamma)\neq0$  , Lemma 3.5 would imply that there exists  ${\mathcal{U}}=(U_{n})$   representing    $\gamma$   such that  

$$
|f(x)|\geq|f(\gamma)|/2>0
$$  

for all    $x\in U_{N}$   and some    $N\in\mathbb{Z}_{\geq0}$  . However, since   $\mathrm{vol}(U_{N})=\infty$  , we conclude that  $f$   is not in    $L^{2}(\mathcal{G})$   and this gives a contradiction.  

Suppose now that    $\gamma\in{\mathfrak{C}}({\mathcal{G}})$   has ﬁnite volume. Take a sequence    ${\mathcal{U}}=(U_{n})$   repre- senting    $\gamma$   with   $\mathrm{vol}(U_{0})<\infty$  . Pick a function    $\phi\in H^{2}(0,1)$   such that    $\phi(0)=\phi^{\prime}(0)=$   $\phi^{\prime}(1)=0$   and    $\phi(1)=1$   and then deﬁne    $f\colon G\to\mathbb{C}$   by  

$$
f(x_{e})=\left\{\begin{array}{l l}{1,}&{x_{e}\in e\mathrm{~and~both~vertices~of~}e\mathrm{~are~in~}U_{0},}\\ {0,}&{x_{e}\in e\mathrm{~and~both~vertices~of~}e\mathrm{~are~not~in~}U_{0},}\\ {\phi\Big(\frac{|x_{e}-u|}{|e|}\Big),}&{x_{e}\in e=e_{u,v}\mathrm{~and~}u\in\mathcal{V}\setminus U_{0},v\in U_{0}.}\end{array}\right.
$$  

Clearly,    $f\in H^{2}(e)$   for every    $e\in\mathcal E$  . Moreover, it is straightforward to check that    $f$  satisﬁes Kir ch ho conditions (2.7) at every    $v\in\mathcal V$  . By assumption,    $\partial U_{0}$   is compact and hence it is contained in ﬁnitely many edges. Thus there are only ﬁnitely many edges    $e\in\mathcal E$   such that one of its vertices belongs to    $U_{0}$   and the other one does not belong to    $U_{0}$  . This implies that    $f\,\in\,L^{2}(\mathcal G)$   and, moreover,    $f^{\prime}\not\equiv0$   only on ﬁnitely many edges, which proves the inclusion    $f\in\mathrm{dom}(\mathbf{H})\cap H^{1}(\mathcal{G})$  . Taking into account that    $f\equiv1$   on    $U_{n}$   for large enough    $n$  , we conclude that    $f(\gamma)=1$   and hence    $\gamma$   is nontrivial.  

It remains to prove the second claim.  t    $\gamma_{1},.\,.\,.\,,\gamma_{N}\,\in\,\mathfrak{C}(\mathcal{G})$   are dis- tinct nontrivial ends. Then we can ﬁnd  U  ${\mathcal{U}}^{j}~=~(U_{n}^{j})$  ), sequences representing    $\gamma_{j}$  ,  $j\;\in\;\{1,.\,.\,.\,,N\}$  , such that   $\mathrm{vol}(U_{0}^{1})\,<\,\infty$   ∞ and    $U_{0}^{1}\cap U_{0}^{j}\,=\,\emptyset$    ∩  ∅ for all    $j\,=\,2,\ldots,N$  (see [29, Satz 3] or [24, Lemma 3.1]). Using the above procedure, we can construct a function    $f\in\mathrm{dom}(\mathbf{H})\cap H^{1}(\mathcal{G})$   such that   $\operatorname{supp}(f)\subseteq U_{0}$   and    $f(\gamma)=1$  . The latter also implies that    $f(\gamma_{2})=\cdot\cdot\cdot=f(\gamma_{N})=0$  . □  

Remark 3.11.  If   $\begin{array}{r}{\mathrm{vol}(\mathcal{G})\,=\,\sum_{e\in\mathcal{E}}|e|\,<\,\infty}\end{array}$    | |  ∞ , then all ends have ﬁnite volume and the end compactiﬁcation   b  of  G  coincides with several other spaces, among them the  metric completion  of  G  and the  Royden compactiﬁcation  of a related discrete graph (see [35, Corollary 4.22] and also [34, p. 1526]). Notice that the natural path metric    $\varrho$   can be  ed to    ${\widehat{\mathcal{G}}}={\mathcal{G}}\cup{\mathfrak{C}}({\mathcal{G}})$  G  G ∪ G ) (see [34]). That is, the distance    $\varrho(x,\gamma)$  between a point  x  ∈G  and an end    $\gamma\,\in\,{\mathfrak{C}}({\mathcal{G}})$   is the inﬁmum over all lengths of rays starting at  x  and belonging to    $\gamma$  . Similarly, the distance    $\varrho(\gamma,\gamma^{\prime})$   between two ends is the inﬁmum over the lengths of all double rays with one tail part in    $\gamma$   and the other one in    $\gamma^{\prime}$  . Then   $(\widehat{\mathscr G},\varrho)$  G ) is a metric co pletion of    $\mathcal{G}$   and G  is compact and homeomorphic to the end compactiﬁcation of  (see [34] for further details).  

The metric completion was considered in connection with quantum graphs in [16, 17]; however, it can have a rather complicated structure if   $\mathrm{vol}({\mathcal G})\;=\;\infty$  and a further analysis usually requires additional assumptions. Moreover, there are clear indications that metric completion is not a good candidate for these purposes.  

3.3.  Description of    $H_{0}^{1}(\mathcal{G})$  G .  Recall that the space    $H_{0}^{1}(\mathcal{G})$  G ) is deﬁned as the closure of   $\mathrm{dom}(\mathbf{H}_{0}^{0})\subset H^{1}(\mathcal{G})$   ⊂ G ) wi respect to    $\|\cdot\|_{H^{1}(\mathcal{G})}$  . One can naturally conjecture that  $H_{0}^{1}(\mathcal{G})$  G ) consists of those  H  $H^{1}$  -functions which vanish on    ${\mathfrak{C}}({\mathcal{G}})$  . In fact, the results of the previous two sections enable us to show that this is indeed the case.  

Theorem 3.12.  Let    $\mathcal{G}$   be a metric graph and    ${\mathfrak{C}}({\mathcal{G}})$   be its ends. Then  

$$
H_{0}^{1}(\mathcal G)=\{f\in H^{1}(\mathcal G)\,|\,\,f(\gamma)=0\;f o r\;a l l\;\gamma\in\mathfrak{C}(\mathcal G)\}.
$$  

Proof.  First of all, it immediately follows from Proposition 3.6 that    $f\,\in\,H_{0}^{1}(\mathcal G)$  G vanishes at every end    $\gamma\in{\mathfrak{C}}({\mathcal{G}})$   (since this holds for each    $f\in\mathrm{dom}(\mathbf{H}_{0}^{0}).$  )).  

To prove the converse inclusion, we will follow the arguments of the proof of [35, Theorem 4.14]. Namely, suppose that    $f\,\in\,H^{1}(\mathcal G)$   and    $f(\gamma)\,=\,0$   for all    $\gamma\in{\mathfrak{C}}({\mathcal{G}})$  .  

Without loss of generality, we may assume that    $f$   is real-valued and    $f\,\geq\,0$  . To prove that    $f\,\in\,H_{0}^{1}(\mathcal G)$  G ), it suﬃces to construct a sequence of compactly supported functions    $f_{n}\in H^{1}(\mathcal G)$   which converges to    $f$   in    $H^{1}(\mathcal G)$  . Deﬁne    $\phi_{n}\colon[0,\infty)\to[0,\infty)$  by  

$$
\phi_{n}(s):={\binom{s-{\frac{1}{n}},\quad{\mathrm{~if~}}s\geq{\frac{1}{n}},}{0,\quad\qquad{\mathrm{~if~}}s<{\frac{1}{n}},}}
$$  

and then let    $f_{n}\colon\mathcal{G}\rightarrow[0,\infty)$   be the composition    $f_{n}:=\phi_{n}\circ f$  ,    $n\geq0$  . Since    $\phi_{n}(s)\leq s$  for all    $s\,\geq\,0$   and    $|\phi_{n}(s)\,-\,\phi_{n}(t)|\,\le\,|s\,-\,t|$   for all    $s,t\,\geq\,0$  ,    $|f_{n}(x)|\,\leq\,|f(x)|$   and  $|f_{n}^{\prime}(x)|\leq|f^{\prime}(x)|$  | ≤| |  for almost every    $x\in\mathcal{G}$  . Hence    $f_{n}\in H^{1}(\mathcal{G})$   and  

$$
\|f_{n}\|_{H^{1}(\mathcal{G})}\leq\|f\|_{H^{1}(\mathcal{G})}
$$  

for all    $n$  . Let us now show that    $f_{n}$   has compact support. Indeed, assuming the converse, there exist inﬁnitely many distinct edg    in    $\mathcal{E}$   such that    $f_{n}$   is non-zero  $e_{k}$  on each    $e_{k}$  . Taking into account (3.8), for each  k  we can ﬁnd a non-vertex point  $x_{k}$   on    $e_{k}$   such that    $f_{n}(x_{k})\;>\;{\textstyle\frac{1}{n}}$  . Since   G  is compact, the sequence   $\left(x_{k}\right)$   has an ccum ation point  $x\in{\widehat{\mathcal{G}}}$  G . By construction each edge    $e\in\mathcal E$   contains at most one of the  x k ’s. It follows that  $x\notin\mathcal{G}$  ∈G  and hence    $x\in{\widehat{\mathcal{G}}}$  G  is an end. On the other hand,  $f$   is continuous  n   b  by Proposition 3.6 and thus  $\textstyle f(x)\geq{\frac{1}{n}}$   ≥ , which contradicts our assumptions on  f .  

It remains to show that    $f_{n}$   converges to    $f$   in    $H^{1}(\mathcal G)$   as    $n\rightarrow\infty$  . Taking into account the above properties of    $f_{n}$  , we get  

$$
\begin{array}{r}{\|f-f_{n}\|_{L^{2}}^{2}+\|f^{\prime}-f_{n}^{\prime}\|_{L^{2}}^{2}\leq2\big(\|f\|_{L^{2}}^{2}+\|f_{n}\|_{L^{2}}^{2}+\|f^{\prime}\|_{L^{2}}^{2}+\|f_{n}^{\prime}\|_{L^{2}}^{2}\big)\leq4\|f\|_{H^{1}}^{2},}\end{array}
$$  

and hence by dom nated convergence it is enough to show  $f_{n}\to f$   $f_{n}^{\prime}\rightarrow f^{\prime}$    → pointwise a.e. on  G . The ﬁrst claim is clearly true since lim  $\begin{array}{r}{\operatorname*{lim}_{n\to\infty}\phi_{n}(s)=s}\end{array}$   for all  $s\,\in\,[0,\infty)$  . To prove the second claim, suppose that    $f$   is diﬀerentiable at a no vertex point    $x\in\mathcal{G}$  . If    $f(x)>0$  , then y continuity of    $f$  , there is ghborhood  U of    $x$   such that    $\textstyle f_{n}=f-{\frac{1}{n}}$    holds on  U  for all suﬃciently large  n >  0. Hence    $f_{n}$   is diﬀerentiable at    $x$   with    $f_{n}^{\prime}(x)=f^{\prime}(x)$  ) for all large enough    $n$  . Finally, if    $f(x)=0$  , then for each    $n$   there is a neighborhood    $U_{n}$   of    $x$   such that    $\textstyle f\,\leq\,{\frac{1}{n}}$    on    $U_{n}$  . Hence  $f_{n}\equiv0$   $U_{n}$   a d, in  articular,    $f_{n}$   is diﬀe entiable at    $x$   wit  $f_{n}^{\prime}(x)=0$  ) = 0. However, since  $f\geq0$   ≥ 0 on  G  and  f  is diﬀerentiable at  x , it follows that  f  $f^{\prime}(x)=0$  ) = 0 as well. This ﬁnishes the proof. □  

Combining Theorem 3.12 with Theorem 3.10, we arrive at the following fact.  

Corollary 3.13.  The equality    $H^{1}(\mathcal{G})\,=\,H_{0}^{1}(\mathcal{G})$  G  holds true if and only if all topo- logical ends of  $\mathcal{G}$   have inﬁnite volume.  

Remark 3.14.  In the related setting of (weighted) discrete graphs, an important concept is the construction of boundaries by employing    $C^{*}$  -algebra techniques (this includes both  Royden  and  Kuramochi boundaries , see [35, 48, 53, 64, 71] for fur- ther details and references). Finite volume graph ends can also be constructed by using this method. Indeed,    $\mathcal{A}:=H^{1}(\mathcal{G})\subset C_{b}(\mathcal{G})$   is a subalgebra by Lemma 3.2 and nce its    $\|\cdot\|_{\infty}$  -closure  $\widetilde{\mathcal{A}}:=\overline{{\mathcal{A}}}^{\parallel\cdot\parallel_{\infty}}$  A  A is isomorphic to    $C_{0}(\widetilde{X})$  ), w re  $\tilde{X}$   is the space of characters equipped with  e weak  $^*$  -topolog to   A e . In general, ﬁnding  $\widetilde{X}$  e  for some concrete  C ∗ -algebra is a rather complicated task. However, it turns  $\widetilde{X}$   $\widetilde{\mathcal{G}}:=\mathcal{G}\cup\mathfrak{C}_{0}(\mathcal{G})$   $\widetilde{\mathcal{G}}=\mathcal{G}\cup\mathfrak{C}_{0}(\mathcal{G})$  out that in our situation  coincides with  G ∪ G ). Indeed, G  G ∪ G  

equipped nduced topology of the end compactiﬁc tion G  is a locally com- pact Hausdorﬀspace. Proposition 3.6 together with Theorem 3.10 shows that each function  $f\in H^{1}(\mathcal G)$  G ) has a  tinuou sion to   e  and this extension be- longs to  $C_{0}(\widetilde{\mathcal{G}})$    e ). Moreover, by Theorem 3.10,  $H^{1}(\mathcal G)$  G ) is point-separating and nowhere vanishing on   e  and hence    $\widetilde{\mathcal{A}}=C_{0}(\widetilde{\mathcal{G}})$  A e   e ) by the Stone–Weierstrass theorem. Thus the resulting boundary notion is precisely the space of ﬁnite volume graph ends.  

Let us also mention that    $\widetilde{\mathcal G}$  e  is compact only if   $\mathrm{vol}(\mathcal G)<\infty$  and in this case one can show that the Royden compactiﬁcation of    $\mathcal{G}$  s well as its Kuramochi compact- iﬁcation coincide with the end compactiﬁcation   b  (see [35], [48, Theorem 7.11], [49, p.215] and also [41, p.2] for the discrete case).  

# 4.  Deficiency indices  

Intuitively, deﬁciency indices should be linked to  boundary notions  for underlying combinatorial graphs. However, spectral properties of the operator    $\mathbf{H}_{0}$   also depend on the edge lengths and this suggests that it is diﬃcult to expect a purely combi- natorial formula for the deﬁciency indices   $\mathrm{n}_{\pm}(\mathbf{H}_{0})$   of    $\mathbf{H}_{0}$  . Recall that throughout the paper we always assume that  $\mathcal{G}$   satisﬁes Hypothesis 2.1.  

4.1.  Deﬁciency indices and graph ends.  The main result of this section pro- vides criteria which allow to connect   $\mathrm{n}_{\pm}(\mathbf{H}_{0})$   with the number of graph ends.  

Theorem 4.1.  Let    $\mathcal{G}$   be a metric graph and let    $\mathbf{H}_{0}$   be the corresponding minimal KirchhoﬀLaplacian. Then  

$$
\mathrm{n}_{\pm}(\mathbf{H}_{0})\geq\#\mathfrak{C}_{0}(\mathcal{G}).
$$  

Moreover, the equality  

$$
\mathrm{n}_{\pm}\big(\mathbf{H}_{0}\big)=\#\mathfrak{C}_{0}(\mathcal{G})
$$  

holds true if and only if either    $\#\mathfrak{C}_{0}(\mathcal{G})=\infty$  or    $\mathrm{dom}(\mathbf{H})\subset H^{1}(\mathcal{G}).$  .  

Remark 4.2.  Since the map  

$$
D\colon\quad\begin{array}{c c c}{{H^{1}({\mathcal G})}}&{{\to}}&{{L^{2}({\mathcal G})}}\\ {{f}}&{{\mapsto}}&{{f^{\prime}}}\end{array}
$$  

is bounded, the inclusion   $\mathrm{dom}(\mathbf{H})\,\subset\,H^{1}(\mathcal{G})$   holds true if and only if there is a positive constant    $C>0$   such that  

$$
\begin{array}{r}{\|f^{\prime}\|_{L^{2}(\mathcal{G})}^{2}\leq C\big(\|f\|_{L^{2}(\mathcal{G})}^{2}+\|f^{\prime\prime}\|_{L^{2}(\mathcal{G})}^{2}\big)}\end{array}
$$  

holds for all    $f\in\mathrm{dom}(\mathbf{H})$  . It can be shown by examples that (4.3) may fail.  

Before proving Theorem 4.1, let us ﬁrst comment on some of its immediate consequences.  

Corollary 4.3.  If    $\mathcal{G}$   is a metric graph with ﬁnite total volume    $\mathrm{vol}(\mathcal G)<\infty$  , then  

$$
\mathrm{n}_{\pm}(\mathbf{H}_{0})\geq\#\Omega(\mathcal{G}_{d}).
$$  

Moreover,  

$$
\mathrm{n}_{\pm}\big(\mathbf{H}_{0}\big)=\#\Omega(\mathcal{G}_{d})
$$  

if and only if either    $\mathcal{G}$   contains a non-free end (and hence    $\#\Omega({\mathcal{G}}_{d})\,=\,\infty$  in this case) or    $\ker(\mathbf{H})\subset H^{1}(\mathcal{G})$  .  

In fact, we only need to mention that by Halin’s theorem [38] (see Remark 2.5(v)) and the ﬁnite total volume of    $\mathcal{G}$  ,   $\#\mathfrak{C}_{0}(\mathcal{G})=\infty$  only if    $\mathcal{G}$   contains a non-free end.  

G Recall that for a ﬁnitely generated group , the number of graph ends of a Cayley graph is independent of the generating set (see, e.g., [32]). Combining this fact with the above statement, we obtain the following result.  

Corollary 4.4.  Let  $\mathcal{G}_{d}$   be a Cayley graph of a ﬁnitely generated group  $\mathsf{G}$   with inﬁnitely many ends.  $^\dagger$     $I f\,\mathrm{vol}(\mathcal{G})<\infty$  , then    $\mathrm{n}_{\pm}(\mathbf{H}_{0})=\infty$  .  

4.2.  Proof of Theorem 4.1.  The proof of Theorem 4.1 is based on the following observation. Let    ${\bf{H}}_{F}$   be the Friedrichs extension of    $\mathbf{H}_{0}$  . Then   $\operatorname{dom}(\mathbf{H})$   admits the following decomposition  

$$
\mathrm{dom}(\mathbf{H})=\mathrm{dom}(\mathbf{H}_{F})+\mathrm{ker}(\mathbf{H}-z)=\mathrm{dom}(\mathbf{H}_{F})+\mathcal{N}_{z}(\mathbf{H}_{0}),
$$  

for every    $z$   in the resolvent set    $\rho({\bf H}_{F})$   of    ${\bf{H}}_{F}$   (see, e.g., [69, Proposition 14.11]). In particular, (4.6) holds for all    $z\,\in\,(-\infty,\lambda_{0}(\mathcal{G}))$  , where    $\lambda_{0}(\mathcal{G})\,\geq\,0$   is deﬁned by (2.17). Moreover,   $\mathrm{dom}(\mathbf{H}_{F})\,\subset\,H_{0}^{1}(\mathcal{G})$  G ) and hence the inclusion   $\mathrm{dom}(\mathbf{H})\,\subset\,H^{1}(\mathcal{G})$  depends only on the inclusion   $\ker(\mathbf{H}-z)\,\subset\,H^{1}(\mathcal{G})$   for some (and hence for all)  $z\in\rho({\bf H}_{F})$  . Let us stress that    $\begin{array}{r}{\mathcal{N}_{0}(\mathbf{H}_{0})=\ker(\mathbf{H})=\mathbb{H}(\mathcal{G})\cap L^{2}(\mathcal{G})}\end{array}$   and hence in the case    $\lambda_{0}(\mathcal{G})\,>\,0$  , one is interested in whether all  L  $L^{2}$    harmonic functions belong to  $H^{1}(\mathcal G)$   or not, which is known to depend on the geometry of the underlying metric graph.  

We also need the fact that functions in    $\mathcal{N}_{\lambda}(\mathbf{H}_{0})$   with    $\lambda\in(-\infty,0)$   can be consid- ered as subharmonic functions and hence they should satisfy a maximum principle.  

Lemma 4.5.  Suppose    $\mathcal{G}$   is a metric graph and let    $\lambda\in(-\infty,0)$  

(i)  If    $f\in\mathcal{N}_{\lambda}(\mathbf{H}_{0})=\ker(\mathbf{H}-\lambda)$   is real-valued and    $f(x_{0})>0$   for some    $x_{0}\in\mathcal{G}$  , then  

$$
\operatorname*{sup}_{x\in{\mathcal{G}}}f(x)=\operatorname*{sup}_{v\in{\mathcal{V}}}f(v).
$$  

(ii)  If additionally    $f\in H^{1}(\mathcal G)$  , then  

$$
\operatorname*{sup}_{x\in{\mathcal{G}}}f(x)=\operatorname*{sup}_{\gamma\in{\mathfrak{C}}({\mathcal{G}})}f(\gamma).
$$  

(iii)  If (not necessarily real-valued)    $f\in\mathcal{N}_{\lambda}(\mathbf{H}_{0})\cap H^{1}(\mathcal{G})$   satisﬁes  

$$
f(\gamma)=0
$$  

for all    $\gamma\in{\mathfrak{C}}({\mathcal{G}})$  , then    $f\equiv0$  .  

Proof.  (i) Let    $f\in\mathcal{N}_{\lambda}(\mathbf{H}_{0})$   be real-valued. If    $x\in\mathcal{G}$   is such that    $f(x)>0$   and    $e\in\mathcal E$  is an edge with  x  $x\in e$   ∈ , t identifying    $e$   with the interval    $\mathcal{T}_{e}=[0,|e|]$   and taking into account that  −  $-f^{\prime\prime}=\lambda f$   on    $e$  , we get  

$$
f(y)=f(x)\cosh\left(\sqrt{-\lambda}(y-x)\right)+\frac{f^{\prime}(x)}{\sqrt{-\lambda}}\sinh\left(\sqrt{-\lambda}(y-x)\right)
$$  

for all    $y\in e$  . If    $f^{\prime}(x)\geq0$  , then obviously    $f(e_{i})\geq f(x)$  , where    $e_{i}$   is the vertex of    $e$  identiﬁed with the right endpoint of    $\mathcal{L}_{e}$  . Similarly,    $f(e_{o})\geq f(x)$   for the other vertex  $e_{o}$   of    $e$   if    $f^{\prime}(x)<0$  . Hence    $f$   attains its maximum on    $e$   at the vertices of    $e$  , which clearly implies (4.7).  

(ii) Now let    $v\in\mathcal V$   b rtex with    $f(v)>0$  . By (2.7), there is an edge    $e\in\mathcal E_{v}$  such that    $f_{e}^{\prime}(v)\geq0$   ≥ 0. If  u  ∈V  is the other vertex of    $e$  , then by (4.10) we get  

$$
f(u)=f(v)\cosh\left(\sqrt{-\lambda}|e|\right)+\frac{f_{e}^{\prime}(v)}{\sqrt{-\lambda}}\sinh\left(\sqrt{-\lambda}|e|\right)>f(v).
$$  

Observe that    $f_{e}^{\prime}(u)\,<\,0$   0. Hence, setting    $\boldsymbol{v}_{0}~=~\boldsymbol{v}$   and    $v_{1}\,=\,u$   and using induction, we can construct a ray    ${\mathcal R}=(v_{n})$   such that    $f(v_{n+1})>f(v_{n})$   for all    $n\geq0$  . Since  $f\in H^{1}(\mathcal G)$  , we get  

$$
0<f(v)<\operatorname*{lim}_{n\to\infty}f(v_{n})=f(\gamma_{\mathcal{R}})\leq\operatorname*{sup}_{\gamma\in\mathfrak{C}(\mathcal{G})}f(\gamma),
$$  

which proves (4.8).  

(iii) By considering    $\pm f$   (and splitting into real and imaginary part, if necessary), (4.9) clearly follows from (4.8). □  

Remark 4.6.  Notice that the arguments used in the proof of Lemma 4.5(ii) in fact show that functions in    $\mathcal{N}_{\lambda}(\mathbf{H}_{0})$  with    $\lambda\in(-\infty,0)$   admitting positive values on  $\mathcal{G}$   cannot attain global maxima in  G , tha f    $f$   attains a positive value at some  $x\in\mathcal{G}$  , then for every compact subgraph G ⊂G  the following holds  

$$
\operatorname*{sup}_{x\in\mathcal{G}}f(x)=\operatorname*{sup}_{x\in\mathcal{G}\backslash\tilde{\mathcal{G}}}f(x).
$$  

Clearly, analogous statements hold true for functions admitting negative values, however, then sup must be replaced with inf.  

Lemma 4.7.  Suppose    $\mathcal{G}$   is a metric graph and let    $\lambda\in(-\infty,0)$  . Then  

$$
\mathrm{dim}(\mathcal{N}_{\lambda}(\mathbf{H}_{0})\cap H^{1}(\mathcal{G}))=\#\mathfrak{C}_{0}(\mathcal{G}).
$$  

Proof.  Using (4.6) with    $z\,=\,\lambda\,\in\,(-\infty,0)$   and noting that   $\mathrm{dom}(\mathbf{H}_{F})\,\subset\,H_{0}^{1}(\mathcal{G})$  G ), Theorem 3.10 and Theorem 3.12 imply that   $\mathrm{dim}(\mathcal{N}_{\lambda}(\mathbf{H}_{0})\cap H^{1}(\mathcal{G}))\geq\#\mathfrak{C}_{0}(\mathcal{G})$  . The converse inequality follows from Lemma 4.5(iii), which shows that the mapping  $f\mapsto(f(\gamma))_{\gamma\in\mathfrak{C}_{0}(\mathcal G)}$   is injective on    $\mathcal{N}_{\lambda}(\mathbf{H}_{0})\cap H^{1}(\mathcal{G})$  . □  

After all these preparations, we are now in position to complete the proof of Theorem 4.1.  

Proof of Theorem 4.1.  Observe that the inequality (4.1) immediately follows from (4.6) and (4.11) since   $\mathrm{n}_{\pm}(\mathbf{H})=\mathrm{dim}(\mathcal{N}_{\lambda}(\mathbf{H}_{0}))$  .  

Clearly, the second claim is trivial if   $\#\mathfrak{C}_{0}(\mathcal{G})\,=\,\infty$  . Hence it remains to show that in the case   $\#\mathfrak{C}_{0}(\mathcal{G})<\infty$  equality (4.2) holds exactly when   $\mathrm{dom}(\mathbf{H})\subset H^{1}(\mathcal{G})$  . Applying (4.6) once again, the inclusion   $\mathrm{dom}(\mathbf{H})\subset H^{1}(\mathcal{G})$   holds true exactly when  $\mathcal{N}_{\lambda}(\mathbf{H}_{0})\subset H^{1}(\mathcal{G})$  . Taking into account once again that   $\mathrm{n}_{\pm}(\mathbf{H})=\mathrm{dim}\mathcal{N}_{\lambda}(\mathbf{H}_{0})$   a using (4.11), we arrive at the conclusion. □  

Remark 4.8.  Let us mention that one can prove the second claim of Theorem 4.1 in a diﬀerent way. Namely, if   $\#\mathfrak{C}_{0}(\mathcal{G})<\infty$  , then it is possible to reduce the problem to the study of a ﬁnite volume graph with a single end.  

Let us stress that in the proof of Theorem 4.1 the equivalence of equality (4.2) and the inclusion   $\mathrm{dom}(\mathbf{H})\subset H^{1}(\mathcal{G})$   was proved in the case when all ﬁnite volume ends are free. The next result shows that the inclusion never holds if there is a ﬁnite volume end which is not free.  

Proposition 4.9.  Let    $\mathcal{G}$   be a metric graph having a ﬁnite volume end which is not free. Then there exists a function    $f\in\mathrm{dom}(\mathbf{H})$   which does not belong to    $H^{1}(\mathcal G)$  .  

Proof.  First observe that we can restrict our considerations to the case of a metric graph    $\mathcal{G}$   having ﬁnite total volume. Indeed, if    $\gamma$   is a non-free ﬁnite volume end of    $\mathcal{G}$  , then there exists a sequence    ${\mathcal{U}}=(U_{n})$   representing    $\gamma$   such that   $\mathrm{vol}(U_{n})<\infty$  for all  $n$  . By deﬁnition, each    $U_{n}$   is  ompact boun  $\mathcal{G}_{0}\subset\mathcal{G}$  s the subgraph with vertex set  V  $\mathcal{V}(\mathcal{G}_{0})=\mathcal{V}\cap U_{0}$  G  V ∩  and edge set  E  ${\mathcal{E}}({\mathcal{G}}_{0})=\{e\in{\mathcal{E}}\,|\,e\subset U_{0}\}$  G  {  ∈E |  ⊂ } , it is easy to see that    $\mathcal{G}_{0}$   is a connected ﬁnite volume subgraph and    $\gamma$   is a non-free end of    $\mathcal{G}_{0}$   (see also the notion of graph representation of an end in Section 6.1). Moreover, by co struction the set    $\partial\mathcal{G}_{0}$   of boundary points (here,    $\mathcal{G}_{0}$   is seen as a closed subset of ) is ﬁnite.  

Let   G ⊂G  be a connected, compact subgraph and consider the ﬁnitely many connected c mponents of    $\mathcal{G}\backslash\widetilde{\mathcal{G}}$  G . Since    $\mathcal{G}$   has inﬁnitely many ends, there is a connected component  U  which contains at least two distinct graph ends    $\gamma,\gamma^{\prime}\in\mathfrak{C}(\mathcal{G})$  . Following orem 3 a uct a  funct  $f=f_{U}\in$   $\mathrm{dom}(\mathbf{H})\cap H^{1}(\mathcal{G})$   ∩ G ) with  f  $f(\gamma)\,=\,0$   f  $f(\gamma^{\prime})\,=\,1$  ) = 1 and 0  $0\,\leq\,f\,\leq\,1$   ≤  ≤ 1 on  C  ${\mathfrak{C}}({\mathcal{G}})$  G ) (in fact, it suﬃces to choose the corresponding function    $\phi$   with   $0\,\leq\,\phi\,\leq\,1$  ). Taking into account Theorem 3.12 and decomposition (4.6), we can assume that    $f$   belongs to  $H^{1}(\mathcal{G})\cap\mathcal{N}_{\lambda}(\mathbf{H}_{0})$   for some (ﬁxed)    $\lambda\in(-\infty,0)$  . However, Lemma 4.5 (iii) implies that  

$$
\|f\|_{\infty}=\operatorname*{sup}_{x\in\mathcal{G}}|f(x)|=\operatorname*{sup}_{x\in\mathcal{G}}f(x)=1.
$$  

On the other hand, there exist two  y  $\mathcal{R}$  ,    $\mathcal{R}^{\prime}\in\mathfrak{R}(\mathcal{G}_{d})$   re esenting the ends    $\gamma$  and, respectively,    $\gamma^{\prime}$    such that both  R ,  R ′   are contained in  U  and have the same initial vertex    $v_{0}$  . This leads to another estimate  

$$
\begin{array}{l}{1=\big|f(\gamma)-f(\gamma^{\prime})\big|=\big|f(\gamma)-f(v_{0})+f(v_{0})-f(\gamma^{\prime})\big|}\\ {\quad=\Big|\int_{\mathcal{R}}f^{\prime}(x)d x-\int_{\mathcal{R}^{\prime}}f^{\prime}(x)d x\Big|\leq2\sqrt{\mathrm{vol}(U)}\,\|f^{\prime}\|_{L^{2}(U)}\leq2\sqrt{\mathrm{vol}(U)}\,\|f^{\prime}\|_{L^{2}(\mathcal{G})}.}\end{array}
$$  

Assume now that (4.3) holds for all functions    $g\,\in\,\mathcal{N}_{\lambda}(\mathbf{H}_{0})$  . Then    $\|\cdot\|_{\infty}$  and  $\|\cdot\|_{H^{1}}$   are in fact equivalent norms on    $\mathcal{N}_{\lambda}(\mathbf{H}_{0})$  . Indeed, combining (4.3) and the ﬁnite volume property, we get  

$$
\|g\|_{H^{1}}^{2}\leq C(\|g\|_{L^{2}}^{2}+\|\mathbf H g\|_{L^{2}}^{2})=C(1+\lambda^{2})\|g\|_{L^{2}}^{2}\leq C(1+\lambda^{2})\mathrm{vol}(\mathcal G)\|g\|_{\infty}^{2}
$$  

for all    $g\in\mathcal{N}_{\lambda}(\mathbf{H}_{0})$  , whereas    $\|g\|_{\infty}\leq C_{\mathcal{G}}\|g\|_{H^{1}}$   by Lemma 3.2. Choosing compact  $\widetilde{\mathcal{G}}_{\varepsilon}$   $\mathrm{vol}(\mathcal{G}\setminus\widetilde{\mathcal{G}}_{\varepsilon})\leq\varepsilon^{2}$    G   G  ≤ (which is possible since    $\mathcal{G}$   has ﬁnite volume), we clearly get vol(  $\mathrm{vol}(U_{\varepsilon})\leq\varepsilon^{2}$   ≤   and hence the above constructed function    $f_{\varepsilon}:=f_{U_{\varepsilon}}\in$   $H^{1}(\mathcal{G})\cap\mathcal{N}_{\lambda}(\mathbf{H}_{0})$  G  ∩N ) satisﬁes  

$$
\|f_{\varepsilon}^{\prime}\|_{L^{2}(\mathcal{G})}\geq\|f_{\varepsilon}^{\prime}\|_{L^{2}(U_{\varepsilon})}\geq\frac{1}{2\sqrt{\operatorname{vol}(U_{\varepsilon})}}\geq\frac{1}{2\varepsilon}.
$$  

However, by construction,    $\|f_{\varepsilon}\|_{\infty}=1$  , which obviously contradicts to the equiva- lence of norms    $\|\cdot\|_{\infty}$  and    $\|\cdot\|_{H^{1}}$   on    $\mathcal{N}_{\lambda}(\mathbf{H}_{0})$   since    $\varepsilon>0$   is arbitrary. □  

We conclude this section by mentioning some explicit examples.  

Example 4.10  (Radially symmetri trees) .  Let    $\mathcal{G}\,=\,\mathcal{T}$   be a  radially symmetric (metric) tree : that is, a rooted tree  T  such that for each    $n\geq0$  , all vertices in the combinatorial sphere    $S_{n}$   have the same number of descendants    $d_{n}\geq2$   and all edges between the combinatorial spheres    $S_{n}$   and    $S_{n+1}$   have the same length. It is well- known that in this case    $\mathbf{H}$   is self-adjoint if and only if   $\mathrm{vol}(T)=\infty$  and deﬁciency indices are inﬁnite,   $\mathrm{n}_{\pm}(\mathbf{H}_{0})\,=\,\infty$  , otherwise (see, e.g., [15, 72]). Moreover, due to the symmetry assumptions, all graph ends are of ﬁnite volume simultaneously. Hence we arrive at the equality  

$$
\begin{array}{r}{\mathrm{n}_{\pm}(\mathbf{H}_{0})=\#\mathfrak{C}_{0}(\mathcal{G})=\left\{\begin{array}{l l}{\infty,}&{\mathrm{if}\ \mathrm{vol}(\mathcal{T})<\infty,}\\ {0,}&{\mathrm{if}\ \mathrm{vol}(\mathcal{T})=\infty.}\end{array}\right.}\end{array}
$$  

Moreover, by Theorem 4.1 and Proposition 4.9, the inclusion   $\mathrm{dom}(\mathbf{H})\,\subset\,H^{1}(\mathcal{G})$  holds true if and only if   $\mathrm{vol}(T)=\infty$  .  

Example 4.11  (Radially symmetric antitrees) .  Consider a metric antitree    $\mathcal{G}=\mathcal{A}$  (see Section 7.1 for deﬁnitions) and additionally suppose that    $\mathcal{A}$   is  radially sym- metric , that is, for each    $n\geq0$  , all edges between the combinatorial spheres    $S_{n}$   and  $S_{n+1}$   have the same length. Combining [56, Theorem 4.1] (see also Corollary 7.3 below) with the fact that antitrees have exactly one graph end,   $\#\mathfrak{C}(\mathcal{A})\,=\,1$  , we conclude that  

$$
\begin{array}{r}{\mathrm{n}_{\pm}(\mathbf{H}_{0})=\#\mathfrak{C}_{0}(\mathcal{G})=\left\{\begin{array}{l l}{1,}&{\mathrm{if}\,\,\mathrm{vol}(\mathcal{A})<\infty,}\\ {0,}&{\mathrm{if}\,\,\mathrm{vol}(\mathcal{A})=\infty.}\end{array}\right.}\end{array}
$$  

In particular,    $\mathbf{H}$   is self-adjoint if and only if   $\mathrm{vol}({\mathcal{A}})=\infty$  . Moreover, the inclusion  $\mathrm{dom}(\mathbf{H})\subset H^{1}(\mathcal{G})$   holds true for all radially symmetric antitrees by Theorem 4.1.  

Remark 4.12.  Both radially symmetric trees and antitrees are particular examples of the so-called  family preserving metric graphs  (see [11] and also [10]) . Employing the results from [11], it is in fact possible to extend the conclusions in Example 4.10 and Example 4.11 to this general setting. More precisely, for each  family preserving metric graph    $\mathcal{G}$   without horizontal edges , the Kir ch ho La plac ian    $\mathbf{H}$   is self-adjoint if and only if   $\mathrm{vol}(\mathcal G)=\infty$  and moreover  

$$
\begin{array}{r}{\mathrm{n}_{\pm}\big(\mathbf{H}_{0}\big)=\#\mathfrak{C}_{0}(\mathcal{G})=\left\{\begin{array}{l l}{\#\mathfrak{C}(\mathcal{G}),}&{\mathrm{if~}\mathrm{vol}(\mathcal{G})<\infty,}\\ {0,}&{\mathrm{if~}\mathrm{vol}(\mathcal{G})=\infty.}\end{array}\right.}\end{array}
$$  

If in addition    $\mathcal{G}$   has ﬁnitely many ends, then the inclusion   $\mathrm{dom}(\mathbf{H})\subset H^{1}(\mathcal{G})$   holds true. On the other hand, if    $\mathcal{G}$   has inﬁnitely many ends, then   $\mathrm{dom}(\mathbf{H})\,\subset\,H^{1}(\mathcal{G})$  holds true if and only if   $\mathrm{vol}({\mathcal{G}})=\infty$  . The last two statements are again immediate consequences of Theorem 4.1 and Proposition 4.9.  

In conclusion, let us also emphasize that the example of the rope ladder graph in Appendix B shows that the assumption on horizontal edges cannot be omitted. More precisely, the rope ladder graph is a  family preserving graph  in the sense of [10] with exactly one graph end. However, it possesses inﬁnitely many horizontal edges (i.e., edges connecting vertices in the same combinatorial sphere) and Example B.5 shows that in general  $\mathrm{n}_{\pm}(\mathbf{H}_{0})>\#\mathfrak{C}_{0}(\mathcal{G})$  , even if the edge lengths are chosen symmetrically to the root,    $|e_{n}^{+}|=|e_{n}^{-}|$    |  |   |  for all    $n\in\mathbb{Z}_{\geq0}$  .  

# 5.  Properties of self-adjoint extensions  

The Sobolev space    $H^{1}(\mathcal G)$   plays a distinctive role in the study of self-adjoint the minimal operat  $\mathbf{H}_{0}$  join sion  $\tilde{\bf H}$   of    $\mathbf{H}_{0}$   is called a ﬁnite energy extension  if its domain is contained in  $H^{1}(\mathcal G)$  G ), that is, every function  $f\,\in\,\mathrm{dom}(\widetilde{\mathbf{H}})$   ∈ ) has ﬁnite energy,  ∥  $\|f^{\prime}\|_{L^{2}(\mathcal G)}\;<\;\infty$  . The main result of this section already indicates that ﬁnite energy self-adjoint extensions of the minimal operator (notice that among those are the Friedrichs extension and, as we will see later in this section, all Markovian extensions) possess a number of important properties.  

Theorem 5.1.  Let    $\widetilde{\bf H}$   be a self-adjoint lower semi-bounded extension of    $\mathbf{H}_{0}$  . As- sume th  z  belongs to its re lvent set    $\rho(\tilde{\mathbf{H}})$  . Then the following assertions hold.  

(i) If the form domain of    $\widetilde{\bf H}$  e  is contained  $H^{1}(\mathcal G)$  , then the re  $\mathcal{R}(z,\tilde{\mathbf{H}})$  of    $\widetilde{\bf H}$  e  is an integral operator whose kernel  K  is both of class  $L^{\infty}(\mathcal{G}\times\mathcal{G})$  G × G  and jointly H¨ older continuous of exponent  $\beta=1/2$  .  

(ii) If additio lly    $\mathcal{G}$   has ﬁnite total volume, then    $\mathcal{R}(z,\widetilde{\mathbf{H}})$   is of trace class.  

Proof Let    $\widetilde{\bf H}$  e  be a self-adjoint low mi-bounded nsion of    $\mathbf{H}_{0}$  ,    $\widetilde{\mathbf{H}}\geq c$   ≥  for some  c  $c\in\mathbb{R}$   ∈ . Without loss of generality we may assume  c  = 0. Then we can consider tive semi-deﬁnite square root    $\widetilde{\mathbf{H}}^{1/2}$  e , which is again self-adjoint and whose    $\widetilde{\bf H}$  domain agrees with the form domain of . Accordingly, for all    $z\in\mathbb{C}\setminus[0,\infty)$   and  $\lambda={\sqrt{z}}$    √  we get  

$$
\begin{array}{r}{\left(\widetilde{\mathbf{H}}^{1/2}-\lambda\right)\left(\widetilde{\mathbf{H}}^{1/2}+\lambda\right)=\widetilde{\mathbf{H}}-z,}\end{array}
$$  

and hence  

$$
\mathcal{R}(z,\widetilde{\mathbf{H}})=\mathcal{R}(\lambda,\widetilde{\mathbf{H}}^{1/2})\mathcal{R}(-\lambda,\widetilde{\mathbf{H}}^{1/2}).
$$  

$\widetilde{\bf H}$  If th n of  is contained in    $H^{1}(\mathcal G)$  , and hence by Lemma 3.2 in    $C_{b}(\mathcal{G})$  , then  R  $\mathcal{R}(\pm\lambda,\tilde{\mathbf{H}}^{1/2})$  ±   e ) maps    $L^{2}(\mathcal{G})$   into    $L^{\infty}(\mathcal{G})$  , and hence by duality also maps    $L^{1}(\mathcal G)$   $L^{2}(\mathcal{G})$  G ). Thus (5.1) implies that    $\mathcal{R}(z,\tilde{\mathbf{H}})$  ) maps    $L^{1}(\mathcal G)$   into    $L^{\infty}(\mathcal G)$   and hence, by the Kantorovich–Vulikh theorem (see, e.g., [4, Theorem 1.3] or [63, Theorem 1.1]),  $\mathcal{R}(z,\tilde{\mathbf{H}})$  ) is an integral operator with the  L  $L^{\infty}$  ∞ -kernel  $\mathcal{K}(z;\cdot,\cdot)$  .  

In order to prove the assertion about joint H¨   e older continuity, we need to take a closer look at the kernel    $\mathcal{K}$   by adapting the proof of [3, Prop. 2.1]: as noticed before,  e resolvent    $\mathcal{R}(\lambda,\widetilde{\mathbf{H}}^{1/2})$  )  unded from    $L^{2}(\mathcal{G})$   to    $L^{\infty}(\mathcal{G})$   by Lemma 3.2    $\widetilde{\mathbf{H}}^{1/2}$  e for any  λ  in the resolvent set of . Applying the Kantorovich–Vulikh theorem (see, e.g., [4, page 113]) once again, we see that  

$$
\mathcal{R}(\lambda,\widetilde{\mathbf{H}}^{1/2})u(x)=\int_{\mathcal{G}}u(y)\kappa(\lambda;x,y)d y=\langle u,\kappa(\lambda;x,\cdot)^{*}\rangle_{L^{2}(\mathcal{G})}
$$  

for all    $x\in\mathcal{G}$   and some    $\kappa(\lambda;x,\cdot)\,\in\,L^{2}(\mathcal{G})$  at   $\begin{array}{r}{\operatorname*{sup}_{x\in\mathcal{G}}\|\kappa(\lambda;x,\cdot)\|_{L^{2}(\mathcal{G})}<\infty}\end{array}$  Moreover, observe that there exists  $C=C(\lambda)>0$   0 such that  

$$
\|\kappa(\lambda;x,\cdot)-\kappa(\lambda;x^{\prime},\cdot)\|_{L^{2}(\mathcal{G})}\leq C\sqrt{\varrho(x,x^{\prime})}
$$  

for all    $x,x^{\prime}\in\mathcal{G}$  , where    $\varrho({x},{x}^{\prime})$   denotes the distance in the natural path metric on  $\mathcal{G}$  . Indeed, for any function    $u\in L^{2}(\mathcal{G})$  ,  

$$
\begin{array}{r l}{\Big|\displaystyle\int_{\mathcal{G}}u(y)(\kappa(\lambda;x,y)-\kappa(\lambda;x^{\prime},y))d y\Big|=\big|\mathcal{R}(\lambda,\widetilde{\mathbf{H}}^{1/2})u(x)-\mathcal{R}(\lambda,\widetilde{\mathbf{H}}^{1/2})u(x^{\prime})\big|}&{}\\ {\le\sqrt{\varrho(x,x^{\prime})}\|\mathcal{R}(\lambda,\widetilde{\mathbf{H}}^{1/2})u\|_{H^{1}}}&{}\\ {\le C\sqrt{\varrho(x,x^{\prime})}\|u\|_{L^{2}},}&{}\end{array}
$$  

where we have used the Cauchy–Schwarz inequality and the fact that the resolvent  $\mathcal{R}(\lambda,\widetilde{\mathbf{H}}^{1/2})$  ) is a bounded operator from    $L^{2}$    to the domain of  $\widetilde{\mathbf{H}}^{1/2}$    equipped with the graph norm, and (5.2) immediately follows. Now, taking into account the equalities (5.1) and  $\mathcal{R}(\boldsymbol{\lambda},\widetilde{\mathbf{H}}^{1/2})^{*}=\mathcal{R}(\boldsymbol{\lambda}^{*},\widetilde{\mathbf{H}}^{1/2})$  ), we conclude that  

$$
\begin{array}{r l}&{\mathcal{R}(z,\tilde{\mathbf{H}})u(x)=\mathcal{R}(\lambda,\tilde{\mathbf{H}}^{1/2})\big(\mathcal{R}(-\lambda,\tilde{\mathbf{H}}^{1/2})u\big)(x)}\\ &{\quad\quad\quad\quad\quad=\big\langle\mathcal{R}(-\lambda,\tilde{\mathbf{H}}^{1/2})u,\kappa(\lambda;x,\cdot)^{*}\big\rangle_{L^{2}(\mathcal{G})}}\\ &{\quad\quad\quad\quad=\big\langle u,\mathcal{R}(-\lambda^{*},\tilde{\mathbf{H}}^{1/2})\kappa(\lambda;x,\cdot)^{*}\big\rangle_{L^{2}(\mathcal{G})}}\\ &{\quad\quad\quad\quad=\displaystyle\int_{\mathcal{G}}u(y)\int_{\mathcal{G}}\kappa(\lambda;x,s)\kappa(-\lambda^{*};y,s)^{*}d s\,d y}\\ &{\quad\quad\quad=:\displaystyle\int_{\mathcal{G}}u(y)\mathcal{K}(z;x,y)\,d y,}\end{array}
$$  

for all    $u\in L^{2}(\mathcal G)$  . It remains to prove that the mapping  

$$
\mathcal{K}:\mathcal{G}\times\mathcal{G}\ni(x,y)\mapsto\int_{\mathcal{G}}\kappa(\lambda;x,s)\kappa(-\lambda^{*};y,s)^{*}d s\in\mathbb{C}
$$  

is jointly H¨ older continuous. However, recalling that   $\begin{array}{r}{\operatorname*{sup}_{x\in\mathcal{G}}\|\kappa(\lambda,x;\cdot)\|_{L^{2}(\mathcal{G})}<\infty}\end{array}$  , this immediately follows from (5.2), since  

$$
\begin{array}{r}{|\mathcal{K}(x,y)-\mathcal{K}(x^{\prime},y^{\prime})|\leq\|\kappa(\lambda;x,\cdot)(\kappa(-\lambda^{*};y,\cdot)^{*}-\kappa(-\lambda^{*};y^{\prime},\cdot)^{*})\|_{L^{1}}}\\ {+\;\|\kappa(-\lambda^{*};y^{\prime},\cdot)^{*}(\kappa(\lambda;x,\cdot)-\kappa(\lambda;x^{\prime},\cdot))\|_{L^{1}}.}\end{array}
$$  

for all pairs   $(x,y),(x^{\prime},y^{\prime})\in\mathcal{G}\times\mathcal{G}$  .  

(ii) If    $\mathcal{G}$   has ﬁnite total volume, then    $L^{\infty}(\mathcal{G}\times\mathcal{G})\hookrightarrow L^{2}(\mathcal{G}\times\mathcal{G})$  → G × G ) and hence the resol  $\mathcal{R}(\pm\lambda,\widetilde{\mathbf{H}}^{1/2})$  ) are Hilbert–Schmidt operators. Thus, by (5.1) we conclude that  $\mathcal{R}(z,\tilde{\mathbf{H}})$  ) is of trace class. □  

Observe that the ﬁrst step in the proof of Theorem 5.1 is the factorization (5.1), which has the natural counterpart for semigroups  

$$
\mathrm{e}^{-z\tilde{\bf H}}\,\mathrm{e}^{-z\tilde{\bf H}}=\mathrm{e}^{-2z\tilde{\bf H}},\qquad\mathrm{Re}\,z>0.
$$  

Because the semi nerated by a self-adjoint semi-bounded extension    $\widetilde{\bf H}$   is analytic, it is a bounded operator from the Hilbert space into its generator’s form domain whenever Re  $\mathrm{Re}\,z>0$   0. A careful look at the proof of Theorem 5.1 shows that  $\mathrm{e}^{-z\tilde{\bf H}}$   is an integral operator; all further steps in this is suﬃcient to establish that  the proof of Theorem 5.1 carry over almost verbatim to the study of semigroups. We can hence easily deduce the following result.  

rem   $\widetilde{\bf H}$   be a self-adjoint lower semi-bounded extension of    $\mathbf{H}_{0}$   and let  $z\in\mathbb{C}$   with  Re  $\mathrm{Re}\,z>0$  . Then the following assertions hold.  

$\widetilde{\bf H}$   $\mathrm{e}^{-z\tilde{\bf H}}$   generated

 (i) If t  domain of  is contained in    $H^{1}(\mathcal G)$  , then the semigroup   by    $\tilde{\bf H}$  e  is an integral operator whose kernel is both of class    $L^{\infty}(\mathcal{G}\times\mathcal{G})$   and jointly H¨ older continuous of exponent    $\beta=1/2$  .  $\mathrm{e}^{-z\widetilde{\mathbf{H}}}$   is of trace class.

 (ii) If additionally    $\mathcal{G}$   has ﬁnite total volume, then  

$\mathrm{e}^{-z\tilde{\bf H}}$   yields the inequality Estimating as in (5.3) and using analyticity of  

$$
|p_{t}(x,y)-p_{t}(x^{\prime},y)|\leq\frac{C}{\sqrt{t}}\sqrt{\varrho(x,x^{\prime})},\qquad t>0,\ x,y,x^{\prime}\in\mathcal{G},
$$  

$\widetilde{\bf H}$  for the heat k  $p_{t}(x,y)$   of a nonnegat tension , where in contrast to (5.3) the constant  C >  0 is independent of  t >  0. Such H¨ older estimates are known to be related to Sobolev-type inequalities and also important for upper and lower Gaussian bounds (cf., e.g., [20], [66, Chapter 6]). However, we do not pursue this line of study here and this will be done elsewhere.  

# Remark 5.3.  A few remarks are in order.  

(i) If   $\begin{array}{r}{\operatorname*{sup}_{\mathcal{R}}\left|\mathcal{R}\right|<\infty}\end{array}$  , where the supremum is take  over all non-vertex path without self-intersections, to the end compactiﬁc the metric completion of ( tion  $(\mathcal{G},\varrho)$  G   b . Moreover, in this case ( ). Indeed, the metric completion of ( the path metric  ̺  has   $(\widehat{\mathscr G},\widehat{\varrho})$    b  b ) coincides with ral ext  $(\mathcal{G},\varrho)$  G ) is n  b obtained by adding to  G  equivalence classes of rays of ﬁnite length (see [34, Section 2.3] for details) and the distance of    $x\in\mathcal{G}$   to a boundary point is deﬁned as the “shortest length” of a path in the corresponding equivalence class starting at    $x$  .  

Therefore, Theorem 5.1 and Theorem 5.2 imply that in this case the cor- responding resolvent and semigroup kernels have a bounded and uniformly cont case vol(  $\mathrm{vol}(\mathcal G)<\infty$  G  ∞ nsion to  (see Remark 3.11), the topolog  $(\widehat{\mathscr G},\widehat{\varrho})$  G  b ). However, we stress that in contrast to the by ̺  on G  can diﬀer from the end compactiﬁcation topology if vol(  $\mathrm{vol}({\mathcal{G}})=\infty$  .  

(ii) Discreteness of the spectrum of the Friedrichs extension  ${\bf{H}}_{F}$   is a standard fact in the case of ﬁnite total volume (see, e.g., [16, Prop. 3.11] or [56, Corollary   $3.5(\mathrm{{iv})]}$  ). However, Theorem 5.1(ii) implies the stronger assertion that the resolvent of    ${\bf{H}}_{F}$   belongs to the trace class if   $\mathrm{vol}(\mathcal G)<\infty$  . Let   also stress that it is not true in general that every self-adjoint extension of  H  will have a discrete spectrum if   $\mathrm{vol}(\mathcal G)<\infty$  , since in case of inﬁnite deﬁciency indices such a self-adjoint extension could have a domain large enough to make compactness of the embedding of    $H^{1}(\mathcal G)$   into    $L^{2}(\mathcal{G})$   irrelevant.  

Recall that a self-adjoint extension  $\widetilde{\bf H}$   of    $\mathbf{H}_{0}$   is called  Markovian  if    $\widetilde{\bf H}$   is a non- negative self-adjoint extension and the corresponding quadratic form is a  Dirichlet form  (for deﬁnitions and further details we refer to [31, Chapter 1]). Hence the associated semigroup   $\mathrm{e}^{-t\tilde{\mathbf{H}}}$     $t\ >\ 0$  , as well as resolvents    ${\mathcal{R}}(-\lambda,{\tilde{\mathbf{H}}})$  ),    $\lambda\;>\;0$  , are Markovian: i.e., are both  positivity preserving  (map non-negative functions to non- negative functions) and  L  $L^{\infty}$  -contractive  (map the unit ball of  $L^{\infty}(\mathcal{G})$  G ), and then by duality of    $L^{p}({\mathcal{G}})$   for all    $p\in[1,\infty]$  , into itself). Let us stress that the Friedrichs extension    ${\bf{{H}}}_{F}$   of    $\mathbf{H}_{0}$   is a Markovian extension. Consider also the following quadratic form in    $L^{2}(\mathcal{G})$  

$$
\mathfrak{t}_{N}[f]=\int_{\mathcal{G}}|f^{\prime}(x)|^{2}d x,\qquad\mathrm{dom}(\mathfrak{t}_{N})=H^{1}(\mathcal{G}).
$$  

This form is non-negative and closed, hence we can associate in    $L^{2}(\mathcal{G})$   a self-adjoint operator with it, let us denote it by    ${\bf{H}}_{N}$  . We will refer to it as the  Neumann extension . It is straightforward to check that    $\mathbf{t}_{N}$   is a Dirichlet form and    ${\bf{H}}_{N}$   is also a Markovian extension of    $\mathbf{H}_{0}$  .  

It turns out that Theorems 5.1 and 5.2 apply to all Markovian extensions of    $\mathbf{H}_{0}$  . More speciﬁcally, the analog of the results for discrete Laplacians [39, Theorem 5.2] and Laplacians in Euclidean domains [31, Chapter 3] and Riemannian manifolds [37, Theorem 1.7] holds true for quantum graphs as well.  

Theorem 5.4.  If  $\widetilde{\bf H}$   is a Markovian extension of    $\mathbf{H}_{0}$  , then    $\mathrm{dom}(\widetilde{\mathbf{H}})\subset H^{1}(\mathcal{G})$   ⊂ G  and, moreover,  

$$
\mathbf{H}_{N}\leq\widetilde{\mathbf{H}}\leq\mathbf{H}_{F},
$$  

where the inequalities are understood in the sense of forms.  

We omit the proof of Theorem 5.4 since the proofs of either [39, Theorem 5.2] or [37, Lemma 3.6] carry over verbatim to our setting (see also the proof of [31, Theorem 3.3.1]).  

Let us ﬁnish this section with the following observation. Corollary 5.5.  The following are equivalent:  

(i)    $\mathbf{H}_{0}$   has a unique Markovian extension, (ii)    $H_{0}^{1}(\mathcal{G})=H^{1}(\mathcal{G})$  G G , (iii)  all topological ends of    $\mathcal{G}$   have inﬁnite volume,    $\mathfrak{C}_{0}(\mathcal{G})=\varnothing$  .  

Proof.  The claimed equivalences follow from Theorem 5.4 and Corollary 3.13.  

Remark 5.6.  Let us ﬁnish this section with a few comments.  

(i) The equivalence   $(i)\Leftrightarrow(i i)$   in Corollary 5.5 is known for Riemannian man- ifolds [37, Theorem 1.7] (see also [31, Chapter 3], [62, Theorem 1]) as well as for weighted Laplacians on graphs [39, Corollary 5.6]. However, to the  

characterization. (ii) The list of equivalences in Corollary 5.5 can be extended by adding a claim on the self-adjointness of the so-called  Gaﬀney Laplacian . Namely, since  $H_{0}^{1}(\mathcal G)$  G ) and    $H^{1}(\mathcal G)$   are Hilbert spaces, the operators denoted by    $\nabla_{D}$   and  $\nabla_{N}$   and deﬁned in    $L^{2}(\mathcal{G})$   on the domains, respectively,    $H_{0}^{1}(\mathcal{G})$  G ) and    $H^{1}(\mathcal G)$  by    $f\ \mapsto\ f^{\prime}$    are closed. Notice that with this notation at hand we have  $\mathbf{H}_{F}\;=\;\nabla_{D}^{*}\nabla_{D}$  ∇  and    ${\bf H}_{N}\ =\ \nabla_{N}^{*}\nabla_{N}$  ∇ . Now we can introduce the  ﬀney Laplacian    $\mathbf{H}_{G}:=\nabla_{D}^{*}\nabla_{N}$  ∇  as the restriction of the maximal operator  H  onto the domain (compare with [37, p. 610] for the deﬁnition in the manifolds case)  

$$
\mathrm{dom}(\mathbf{H}_{G}):=\{f\in H^{1}(\mathcal{G})|\,\nabla_{N}f\in\mathrm{dom}(\nabla_{D}^{*})\}.
$$  

Clearly,   $\mathrm{dom}(\mathbf{H}_{F})\ \subseteq\ \mathrm{dom}(\mathbf{H}_{G})$  ,   $\mathrm{dom}(\mathbf{H}_{N})\ \subseteq\ \mathrm{dom}(\mathbf{H}_{G})$  , and    ${\mathbf{H}}_{G}$   is not necessarily symmetric. It turns out that    ${\mathbf{H}}_{G}$   is symmetric (and hence self- adjoint) if and only if the Kir ch ho La plac ian    $\mathbf{H}_{0}$   has a unique Markovian extension. Moreover, in this case    ${\bf H}_{F}={\bf H}_{N}={\bf H}_{G}$   (cf. [37, Theorem 1.7(ii)] in the manifold setting). Let us mention that the Markovian/ﬁnite energy extensions of    $\mathbf{H}_{0}$   are exactly the Markovian/self-adjoint restrictions of    ${\mathbf{H}}_{G}$  and hence the deﬁciency indices of    $\mathbf{H}_{G}^{*}=\nabla_{N}^{*}\nabla_{D}$   ∇ ∇  are equal to   $\#\mathfrak{C}_{0}(\mathcal{G})$  .  

# 6.  Finite energy self-adjoint extensions  

It turns out that ﬁnite volume (topological) ends provide the right notion of the boundary for metric graphs to deal with ﬁnite energy and also with Markovian ex- tensions of the minimal Kir ch ho La plac ian    $\mathbf{H}_{0}$  . In particular, we are going to show that this end space is well-behaved as concerns the introduction of both traces and normal derivatives. More speciﬁcally, the goal of this section is to give a description of ﬁnite energy self-adjoint extensions of    $\mathbf{H}_{0}$   in the case when the number of ﬁnite volume ends of    $\mathcal{G}$   is ﬁnite, that is,   $\#\mathfrak{C}_{0}(\mathcal{G})<\infty$  . Notice that in this case all ﬁnite volume ends are free.  

6.1 Normal derivati es at graph ends.  Let    $\mathcal{\widetilde{G}}=(\mathcal{\widetilde{V}},\mathcal{\widetilde{E}})$  G e   e ) be a (possibly inﬁnite) connected subgraph of  G . Recall that its boundary  $\partial\mathcal{\widetilde{G}}$  e  (w.r.t. the natural topology on  G , see Section 2.1) is given by  

$$
\partial\widetilde{\mathcal{G}}=\big\{v\in\widetilde{\mathcal{V}}|\;\deg_{\widetilde{\mathcal{G}}}(v)<\deg_{\mathcal{G}}(v)\big\}.
$$  

For a function    $f\in\mathrm{dom}(\mathbf{H})$  , we deﬁne its (inward)  normal derivative  at    $v\in\partial\widetilde{\mathcal{G}}$  G  by  

$$
\frac{\partial f}{\partial n_{\widetilde{\mathcal{G}}}}(v):=\sum_{e\in\mathcal{E}_{v}\cap\widetilde{\mathcal{E}}}f_{e}^{\prime}(v).
$$  

With this deﬁnition at hand, we end up with the following useful integration by parts formula.  

Lem a 6.1.  Let  $\tilde{\mathcal{G}}$  G  be a compact (not necessarily connected) subgraph of the metric graph  G . Then  

$$
-\int_{\widetilde{\mathcal{G}}}f^{\prime\prime}(x)g(x)d x=\int_{\widetilde{\mathcal{G}}}f^{\prime}(x)g^{\prime}(x)d x+\sum_{v\in\partial\widetilde{\mathcal{G}}}g(v)\frac{\partial f}{\partial n_{\widetilde{\mathcal{G}}}}(v)
$$  

for all    $f\in\mathrm{dom}(\mathbf{H})$   and    $g\in H^{1}(\widetilde{\mathcal G})$  G . In particular,  

$$
-\int_{\widetilde{\mathcal{G}}}f^{\prime\prime}(x)d x=\sum_{v\in\partial\widetilde{\mathcal{G}}}\frac{\partial f}{\partial n_{\widetilde{\mathcal{G}}}}(v).
$$  

Proof.  The claim follows immediately from integrating by parts, taking into account that    $f$   satisﬁes (2.7). Setting    $g\equiv1$   in (6.3), we arrive at (6.4). □  

In order to simplify our considerations, we need to introduce the following notion. Let    $\gamma\in{\mathfrak{C}}({\mathcal{G}})$  e a (topological) end of    $\mathcal{G}$  . Consider a sequence (  $\mathcal{G}_{n}$  ) of connected subgraphs  G  such that    ${\mathcal{G}}_{n}\supseteq{\mathcal{G}}_{n+1}$   and   $\#\dot{\partial}\mathcal{G}_{n}\,<\,\infty$  ll    $n$  . We say that the sequence (  $\mathcal{G}_{n}$  G ) is a  graph representation of the end  $\gamma\in{\mathfrak{C}}({\mathcal{G}})$   ∈ G ) if there is a sequence f open sets    ${\mathcal{U}}=(U_{n})$   representing    $\gamma$   such that for each    $n\geq0$   there exist    $j$   and k  such that    ${\mathcal{G}}_{n}\supseteq U_{j}$   and    $U_{n}\supseteq\mathcal{G}_{k}$  . It is easily seen that all graphs  $\mathcal{G}_{n}$  re inﬁnite (they have inﬁnitely many edges). Moreover, graph representations (  $\left(\mathcal{G}_{n}\right)$  G ) of an end can be constructed with the help of compact exhaustions; in particular each graph end    $\gamma\in{\mathfrak{C}}({\mathcal{G}})$   has a representation by subgraphs (see Section 2.2).  

Proposition 6.2.  Let    $\mathcal{G}$   be a metric graph and let    $\gamma\in{\mathfrak{C}}({\mathcal{G}})$   be a free end of ﬁnite volume. Then for every function    $f\in\mathrm{dom}(\mathbf{H})$   and any sequence  (  $\mathcal{G}_{k}$  )  of subgraphs representing    $\gamma$  , the limit  

$$
\operatorname*{lim}_{k\to\infty}\sum_{v\in\partial\mathcal{G}_{k}}\frac{\partial f}{\partial n_{\mathcal{G}_{k}}}(v)
$$  

exists and is independent of the choice of    $\left(\mathcal{G}_{k}\right)$  .  

Proof.  First of all, notice that uniqueness of the limit follows from the inclusion property in the deﬁnition of the graph representations of    $\gamma$  . Hence we only need to show that the limit in (6.5) indeed exists.  

Let (  $\mathcal{G}_{k}$  ) be a graph representation of a free ﬁnite volume end    $\gamma\in\mathfrak{C}_{0}(\mathcal{G})$  . Since    $\gamma$  is free, we can assume that   $\mathrm{vol}(\mathcal{G}_{0})<\infty$  and that    $\mathcal{G}_{0}\cap U_{k}=\emptyset$  eventually for every sequence    ${\mathcal{U}}=(U_{k})$   re g an end    $\gamma^{\prime}\neq\gamma$  .  rst obse t  $\widetilde{\mathcal{G}}=\mathcal{G}_{k}\setminus\mathcal{G}_{j}$   \ G  can again e identi mpact subgraph of  G   never  $k\leq j$   ≤ . Indeed, if   e  has inﬁnitely many edges  {  $\{e_{n}\}\subset{\mathcal{E}}$  } ⊂E , choose for each  n  a point  x  $x_{n}$   in the interior of the  $e_{n}$  . Since  $\widehat{\mathcal{G}}=\mathcal{G}\cup\mathfrak{C}(\mathcal{G})$  G  G ∪ G ) is compact, the set  {  $\{x_{n}\}$  }  has an accumulation point  $x\in{\widehat{\mathcal{G}}}$   ∈ b . By construction,    $x\notin\mathcal{G}$  ∈G  and hence    $x\in{\widehat{\mathcal{G}}}\setminus{\mathcal{G}}={\mathfrak{C}}({\mathcal{G}})$  G \ G G ) is an end. However, we have that  $x_{n}\,\notin\,\mathcal{G}_{j}$  ∈G  and recalling (2.3) and (2.4), this implies that    $x\,=\,\gamma^{\prime}$    for a topological nd    $\gamma^{\prime}\neq\gamma$  . On the other hand,  x  $x_{n}\,\in\,\mathcal{G}_{0}$   ∈G  for all    $n$   and using the properties of  G  $\mathcal{G}_{0}$   and (2.3)–(2.4) once again, we arrive at a contradiction. Now, using (6.1) it is straightforward to verify that  

$$
\sum_{v\in\partial\mathcal{G}_{k}}\frac{\partial f}{\partial n_{\mathcal{G}_{k}}}(v)-\sum_{v\in\partial\mathcal{G}_{j}}\frac{\partial f}{\partial n_{\mathcal{G}_{j}}}(v)=\sum_{v\in\partial\widetilde{\mathcal{G}}}\frac{\partial f}{\partial n_{\widetilde{\mathcal{G}}}}(v).
$$  

Hence by (6.4) and the Cauchy–Schwarz inequality, we get  

$$
\Big|\sum_{v\in\partial\mathcal{G}_{k}}\frac{\partial f}{\partial n_{\mathcal{G}_{k}}}(v)-\sum_{v\in\partial\mathcal{G}_{j}}\frac{\partial f}{\partial n_{\mathcal{G}_{j}}}(v)\Big|=\Big|\int_{\mathcal{G}_{k}\setminus\mathcal{G}_{j}}f^{\prime\prime}(x)d x\Big|\le\sqrt{\mathrm{vol}(\mathcal{G}_{k})}\,\|\mathbf{H}f\|_{L^{2}(\mathcal{G})},
$$  

wh  $k\leq j$  . This implies the existence of the limit in (6.5) since   $\mathrm{vol}\big(\mathcal{G}_{k}\big)=o(1)$  as  k . □  

Proposition 6.2 now enables us to introduce a normal derivative at graph ends.  

Deﬁnition 6.3.  Let    $\gamma\in{\mathfrak{C}}({\mathcal{G}})$   be a free end of ﬁnite volume and let (  $\mathcal{G}_{k}$  ) be a graph representation of    $\gamma$  . Then for every    $f\in\mathrm{dom}(\mathbf{H})$  

$$
\partial_{n}f(\gamma):={\frac{\partial f}{\partial n}}(\gamma):=\operatorname*{lim}_{k\to\infty}\sum_{v\in\partial{\mathcal{G}}_{k}}{\frac{\partial f}{\partial n_{{\mathcal{G}}_{k}}}}(v)
$$  

is called the  normal derivative  of    $f$   at    $\gamma$  .  

Remark 6.4.  In fact, it is not diﬃcult to extend the deﬁnitions (6.2) and (6.7) to general sequences    ${\mathcal{U}}=(U_{n})$   of open sets representing the free end    $\gamma\,\in\,\mathfrak{C}_{0}(\mathcal{G})$  . However, while the idea of the proof of Proposition 6.2 naturally carries over, the analysis becomes more technical and we restrict to the case of subgraphs for the sake of a clear exposition.  

Let us mention that the normal derivative can also be expressed in terms of compact exhaustions.  

Lemma 6.5.  Let    $\mathcal{G}$   be a metric graph having ﬁnite total volume and only one end  $\gamma$  ,    ${\mathfrak{C}}({\mathcal{G}})=\{\gamma\}$  . If    $\left(\mathcal{F}_{k}\right)$   is a compact exhaustion of    $\mathcal{G}$   and    $f\in\mathrm{dom}(\mathbf{H})$  , then  

$$
\partial_{n}f(\gamma)=-\operatorname*{lim}_{k\to\infty}\sum_{v\in\partial\mathcal F_{k}}\frac{\partial f}{\partial n_{\mathcal F_{k}}}(v).
$$  

The fact that we are not approximating    $\gamma$   by its neighborhoods, but rather by compact subgraphs, is responsible for the diﬀerent sign in (6.7) and (6.8).  

Proof.  First of all, notice that    $\mathcal{G}\setminus\mathcal{F}_{k}$   can be identiﬁed with a subgraph of    $\mathcal{G}$   and  

$$
-\sum_{v\in\partial\mathcal{F}_{k}}\frac{\partial f}{\partial n_{\mathcal{F}_{k}}}(v)=\sum_{v\in\partial(\mathcal{G}\backslash\mathcal{F}_{k})}\frac{\partial f}{\partial n_{\mathcal{G}\backslash\mathcal{F}_{k}}}(v)
$$  

for all    $f\in\mathrm{dom}(\mathbf{H})$  . If, moreover,    $\mathcal{G}\backslash\mathcal{F}_{k}$   is a connected subgraph for all    $k\geq0$  , then it is clear that   $\left(\mathcal{G}_{k}\right)$   with    $\mathcal{G}_{k}:=\mathcal{G}\setminus\mathcal{F}_{k}$   for all    $k\geq0$  , is a graph representation of    $\gamma$  and this proves (6.8) in this case.  

If    $\mathcal{G}\backslash\mathcal{F}_{k}$   is not connected, then it has only one inﬁnite connected component    $\mathcal{G}_{k}^{\gamma}$    and ﬁnitely many compact components (since  ${\mathfrak{C}}({\mathcal{G}})=\{\gamma\}$  ). Adding these compact γ components to    $\mathcal{F}_{k}$  , we obtain a compact exhaustion (  $\mathcal{F}_{k}^{\prime}$  ) with    $\mathcal{G}\backslash\mathcal{F}_{k}^{\prime}=\mathcal{G}_{k}^{\gamma}$   G   . Arguing as in the proof of Proposition 6.2 (see (6.6)), we get  

$$
\Big|\sum_{v\in\partial\mathcal F_{k}^{\prime}}\frac{\partial f}{\partial n_{\mathcal F_{k}^{\prime}}}(v)-\sum_{v\in\partial\mathcal F_{k}}\frac{\partial f}{\partial n_{\mathcal F_{k}}}(v)\Big|=\Big|\int_{\mathcal F_{k}^{\prime}\setminus\mathcal F_{k}}f^{\prime\prime}(x)d x\Big|=o(1)
$$  

as    $k\to\infty$  . Hence (6.8) holds true also in the general case.  

6.2.  Properties of the trace and normal derivatives.  In this section, we col- lect some basic properties of the trace maps. We shall adopt the following notation. Since we shall always assume throughout this sectio  $\#\mathfrak{C}_{0}(\mathcal{G})<\infty$  , we set  $\mathcal{H}:=\ell^{2}(\mathfrak{C}_{0}(\mathcal{G}))$  , which can be further identiﬁed with  C  $\mathbb{C}^{\#\mathfrak{C}_{0}(\mathcal{G})}$  . Next, we introduce the maps   $\Gamma_{0}\colon H^{1}({\mathcal{G}})\to{\mathcal{H}}$   and   $\Gamma_{1}$  :   $\operatorname{dom}(\mathbf{H})\cap H^{1}(\mathcal{G})\to\mathcal{H}$   by  

$$
\Gamma_{0}\colon f\mapsto\big(f(\gamma)\big)_{\gamma\in\mathfrak{C}_{0}(\mathcal G)},\qquad\qquad\Gamma_{1}\colon f\mapsto\big(\partial_{n}f(\gamma)\big)_{\gamma\in\mathfrak{C}_{0}(\mathcal G)},
$$  

where the boundary values and normal derivative of  f  are deﬁned by (3.4) and (6.7), respectively.  

Proposition 6.6.  Let    $\mathcal{G}$   be a metric graph with    $\#\mathfrak{C}_{0}(\mathcal{G})<\infty$  . Then:

 (i) For every  $\widehat{f}\in\mathcal{H}$   ∈H , there exists    $f\in\mathrm{dom}(\mathbf{H})\cap H^{1}(\mathcal{G})$   such that  

$$
\Gamma_{0}f=\widehat{f},\qquad\qquad\qquad\qquad\Gamma_{1}f=0.
$$  

(ii) Moreover, the Gauss–Green formula  

$$
\langle\mathbf{H}f,g\rangle_{L^{2}(\mathcal{G})}=\langle f^{\prime},g^{\prime}\rangle_{L^{2}(\mathcal{G})}-\langle\Gamma_{1}f,\Gamma_{0}g\rangle_{\mathcal{H}}
$$  

holds true for every    $f\in\mathrm{dom}(\mathbf{H})\cap H^{1}(\mathcal{G})$   and    $g\in H^{1}(\mathcal G)$  .  

Proof.  (i) Since   $\#\mathfrak{C}_{0}(\mathcal{G})<\infty$  , each ﬁnite volume end    $\gamma\in\mathfrak{C}_{0}(\mathcal{G})$   is free. For every    $\gamma\in\mathfrak{C}_{0}(\mathcal{G})$  , let    $G^{\gamma}$  be a subgraph with the properties as in Remark 2.6. We can also assume that   $\mathrm{vol}({\mathcal{G}}^{\gamma})<\infty$  . Following the proof of Theorem 3.10, we can construct for each end    $\gamma\,\in\,\mathfrak{C}_{0}(\mathcal{G})$   a function    $f_{\gamma}\,\in\,\mathrm{dom}(\mathbf{H})\cap H^{1}(\mathcal{G})$  that    $f_{\gamma}$  constant only on ﬁnitely many edges (since #  $\#\dot{\partial}\mathcal{G}^{\gamma}<\infty$  G  ∞ ),  $f_{\gamma}(\gamma)=1$  ) = 1 and  $f_{\gamma}(\gamma^{\prime})=0$  for all other ends    $\gamma^{\prime}\in\mathfrak{C}_{0}(\mathcal{G})\setminus\{\gamma\}$  . Clearly,   $\Gamma_{1}f_{\gamma}=0$   for every    $\gamma\in\mathfrak{C}_{0}(\mathcal{G})$  . Thus, setting  

$$
f=\sum_{\gamma\in\mathfrak{C}_{0}(\mathcal{G})}\widehat{f}(\gamma)f_{\gamma}
$$  

for a given  ∈H , we clearly have   $\Gamma_{0}f={\hat{f}}$   and   $\Gamma_{1}f=0$  .  

(ii) Let us ﬁrst show that (6.10) holds true for all    $f~\in~\mathrm{dom}(\mathbf{H})\cap H^{1}(\mathcal{G})$   if  $g=f_{\gamma}\in H^{1}(\mathcal{G})$  . Take a compact exhaustion (  $\mathcal{F}_{k}$  ) of    $\mathcal{G}$  . Then by Lemma 6.1,  

$$
\begin{array}{r l r}{\lefteqn{\langle\mathbf{H}f,f_{\gamma}\rangle_{L^{2}(\mathcal{G})}-\langle f^{\prime},f_{\gamma}^{\prime}\rangle_{L^{2}(\mathcal{G})}=\underset{k\to\infty}{\operatorname*{lim}}\langle\mathbf{H}f,f_{\gamma}\rangle_{L^{2}(\mathcal{F}_{k})}-\langle f^{\prime},f_{\gamma}^{\prime}\rangle_{L^{2}(\mathcal{F}_{k})}}}\\ &{}&{=\underset{k\to\infty}{\operatorname*{lim}}\sum_{v\in\partial\mathcal{F}_{k}}\frac{\partial f}{\partial n_{\mathcal{F}_{k}}}(v)f_{\gamma}(v)^{*}=\underset{k\to\infty}{\operatorname*{lim}}\sum_{v\in\partial\mathcal{F}_{k}\cap\mathcal{V}^{\gamma}}\frac{\partial f}{\partial n_{\mathcal{F}_{k}}}(v),}\end{array}
$$  

where    $\mathcal{V}^{\gamma}$  is the set of vertices of    $G^{\gamma}$  . Notice that the subgraph  $G^{\gamma}$  itself is a connected inﬁnite graph having ﬁnite total volume and exactly one end, which can be identiﬁed  for all with    $\gamma$   in an obvious way. Moreover, setting    $\mathcal{F}_{k}^{\gamma}\;:=\;\mathcal{F}_{k}\cap\mathcal{G}^{\gamma}$   F  ∩G    $k\,\geq\,0$   and noting that    $\mathcal{F}_{k}^{\gamma}$    is connected for all suﬃciently large  k , the sequence   $\left(\mathcal{F}_{k}^{\gamma}\right)$  ) provides  and a compact exhaustion of    $G^{\gamma}$  . Since    $\partial_{\mathcal{G}^{\gamma}}\mathcal{F}_{k}^{\gamma}=\partial\mathcal{F}_{k}\cap\mathcal{V}^{\gamma}$  F  ∩V  

$$
\frac{\partial f}{\partial n_{\mathcal{F}_{k}^{\gamma}}}(v)=\frac{\partial f}{\partial n_{\mathcal{F}_{k}}}(v),\qquad v\in\partial_{\mathcal{G}^{\gamma}}\mathcal{F}_{k}^{\gamma},
$$  

for all large enough    $k\geq0$  , we get by applying Lemma 6.5  

$$
\langle\mathbf{H}f,f_{\gamma}\rangle_{L^{2}(\mathcal{G})}-\langle f^{\prime},f_{\gamma}^{\prime}\rangle_{L^{2}(\mathcal{G})}=\operatorname*{lim}_{k\to\infty}\sum_{v\in\mathcal{F}_{k}\cap\mathcal{V}^{\gamma}}\frac{\partial f}{\partial n_{\mathcal{F}_{k}^{\gamma}}}(v)=-\frac{\partial f}{\partial n}(\gamma).
$$  

Hence (6.10) holds true if    $g=f_{\gamma}\in H^{1}(\mathcal{G})$  .  

Now observe that a simple integration by parts implies that (6.10) is valid for all compactly supported    $g\in H^{1}(\mathcal G)$  . By continuity and Theorem 3.12 this extends further to all    $g\in H_{0}^{1}(\mathcal G)$  G ). Finally, setting   $\begin{array}{r}{\tilde{g}:=g-\sum_{\gamma\in\mathfrak{C}_{0}(\mathcal{G})}g(\gamma)f_{\gamma}}\end{array}$   for    $g\in H^{1}(\mathcal G)$  , it is immediate to check that, by Theorem 3.12, ˜  $\tilde{g}\in H_{0}^{1}(\mathcal G)$   ∈ G ). It remains to use the linearity of   $\Gamma_{0}$  . □  

It turns out that the domain of the Neumann extension admits a simple descrip- tion.  

Corollary 6.7.  Let    $\mathcal{G}$   be a metric graph with    $\#\mathfrak{C}_{0}(\mathcal{G})<\infty$  . Then the Neumann extension    ${\bf{H}}_{N}$   is given as the restriction    ${\mathbf H}_{N}={\mathbf H}|_{\mathrm{dom}({\mathbf H}_{N})}$   to the domain  

$$
\mathrm{dom}(\mathbf{H}_{N})=\{f\in\mathrm{dom}(\mathbf{H})\cap H^{1}(\mathcal{G})|\ \Gamma_{1}f=0\}.
$$  

Proof.  By the ﬁrst representation theorem [50, Chapter VI.2.1],   $\mathrm{dom}(\mathbf{H}_{N})$   consists of all functions    $f\in H^{1}(\mathcal G)$   such that there exists    $h\in L^{2}(\mathcal G)$   with  

$$
\langle f^{\prime},g^{\prime}\rangle_{L^{2}(\mathcal{G})}=\langle h,g\rangle_{L^{2}(\mathcal{G})},\qquad\mathrm{for~all~}g\in H^{1}(\mathcal{G}).
$$  

Moreover, in this case    ${\bf H}_{N}f:=h$  . Taking into account Proposition 6.6 and the fact that    ${\bf{H}}_{N}$   is a restriction of    $\mathbf{H}$  , we immediately arrive at (6.11). □  

Our next goal is to prove surjectivity of the normal derivative map.  

Proposition 6.8.  If    $\mathcal{G}$   is a metric graph with  #  $\underline{{\boldsymbol{\mathfrak{c}}}}_{0}(\mathcal{G})<\infty$  , then the mapping    $\Gamma_{1}$  is surjective.  

In fact, Proposition 6.8 will follow from the following lemma.  

Lemma 6.9.  Suppose    $\mathcal{G}$   is a metric graph with    $\mathrm{vol}(\mathcal G)<\infty$  and only one end,  ${\mathfrak{C}}({\mathcal{G}})=\{\gamma\}$  . Then there exists    $f\in\mathrm{dom}(\mathbf{H})\cap H^{1}(\mathcal{G})$   such that  

$$
\partial_{n}f(\gamma)\neq0.
$$  

Proof.  We will proceed by contradiction. Suppose that    $\partial_{n}g(\gamma)\;=\;0$   for all    $g\ \in$   $\mathrm{dom}(\mathbf{H})\cap H^{1}(\mathcal{G})$  . Then, by Corollary 6.7,   $\mathrm{dom}(\mathbf{H}_{F})\,\subseteq\,\mathrm{dom}(\mathbf{H}_{N})\,=\,\mathrm{dom}(\mathbf{H})\cap$   $H^{1}(\mathcal G)$  . However, both    ${\bf{{H}}}_{F}$   and    ${\bf{H}}_{N}$   are self-adjoint restrictions of  H  and hence  $\mathrm{dom}(\mathbf{H}_{F})=\mathrm{dom}(\mathbf{H}_{N})$  . Therefore,    ${\bf H}_{F}={\bf H}_{N}$   and their quadratic forms also coin- cide, which implies that    $H_{0}^{1}(\mathcal{G})=H^{1}(\mathcal{G})$  G G ). This contradicts Corollary 3.13 and hence completes the proof. □  

Proof of Proposition 6.8.  Let    $G^{\gamma}$  ,    $\gamma\in\mathfrak{C}_{0}(\mathcal{G})$   be the subgraphs of    $\mathcal{G}$   constructed in   the proof of Proposition 6.6(i). Every    $G^{\gamma}$  is a connected graph with   $\mathrm{vol}({\mathcal{G}}^{\gamma})<\infty$  and only one end, which can be identiﬁed with    $\gamma$  . Hence we can apply Lemma 6.9 to obtain a function   $\tilde{g}_{\gamma}\,\in\,\mathrm{dom}(\mathbf{H}^{\gamma})\cap H^{1}(\mathcal{G}^{\gamma})$   ∈ G ) such that    $\partial_{n}\tilde{g}_{\gamma}(\gamma)\,=\,1$  ) = 1. Here    $\mathbf{H}^{\gamma}$  denotes the Kir ch ho La plac ian on  $G^{\gamma}$  .  

Since   $\#\dot{\partial}\mathcal{G}^{\gamma}<\infty$  , we can obviously extend   $\tilde{g}_{\gamma}$   to a function    $g_{\gamma}$   on    $\mathcal{G}$   such that  $g_{\gamma}\in\mathrm{dom}(\mathbf{H})\cap H^{1}(\mathcal{G})$   and    $g_{\gamma}$   is identically zero on a neighborhood of e  $\gamma^{\prime}\neq$   $\gamma$   (see also the proof of Theorem 3.10). In particular, this implies that  $\partial_{n}g_{\gamma}(\gamma^{\prime})=0$    for all    $\gamma^{\prime}\in\mathfrak{C}_{0}(\mathcal{G})\setminus\{\gamma\}$  . Upon identiﬁcation of    $\gamma$   with the single end of    $G^{\gamma}$  we also have that  

$$
\partial_{n}g_{\gamma}(\gamma)=\partial_{n}\tilde{g}_{\gamma}(\gamma)=1.
$$  

This immediately implies surjectivity.  

6.3.  Description of self-adjoint extensions.  Our next goal is a description of all ﬁnite energy self-adj    $\mathbf{H}_{0}$  , that is, self-adjoint extensions    $\widetilde{\bf H}$  satisfying  $\mathrm{dom}(\tilde{\mathbf{H}})\,\subset\,H^{1}(\mathcal{G})$    e  ⊂ G ). We will be able to do this under the additional assumption that  G  has ﬁnitely many ﬁnite volume ends. Recall that in this ca  $\mathcal{H}=\ell^{2}(\mathfrak{C}_{0}(\mathcal{G}))$  )) is a ﬁnite dime ional Hilbert space.  

Let  C ,  D  be two linear operators on  satisfying  Rofe-Beketov conditions  [68]:  

$$
C D^{*}=D C^{*},\qquad\qquad\mathrm{rank}(C|D)=\dim\mathcal{H}=\#\mathfrak{C}_{0}(\mathcal{G}).
$$  

Consider the quadratic form  $\mathfrak{t}_{C,D}$   deﬁned by  

$$
\mathfrak{t}_{C,D}[f]:=\int_{\mathcal{G}}|f^{\prime}(x)|^{2}d x+\langle D^{-1}C\Gamma_{0}f,\Gamma_{0}f\rangle_{\mathcal{H}}
$$  

on the domain  

$$
\mathrm{dom}(\mathfrak{t}_{C,D}):=\{f\in H^{1}(\mathcal{G})|\,\Gamma_{0}f\in\mathrm{ran}(D^{*})\}.
$$  

Here and in the following the mappings   $\Gamma_{0}$   and   $\Gamma_{1}$   are given by (6.9) and    $D^{-1}$    :   $\mathrm{ran}(D)\to$   $\mathrm{ran}(D^{*})$   denotes the inverse of the restriction    $D|_{\mathrm{ker}(D)^{\perp}}\colon\mathrm{ran}(D^{*})\,\to\,\mathrm{ran}(D)$  . In particular, (6.12) implies that    $\mathfrak{t}_{C,D}[f]$   is well-deﬁned for all    $f\in\mathrm{dom}(\mathfrak{t}_{C,D})$   (see also (A.4)).  

Remark 6.10.  It is straightforward to check that    $\mathfrak{t}_{I,0}=\mathfrak{t}_{F}$   and    $\mathfrak{t}_{0,I}=\mathfrak{t}_{N}$   are the quadratic forms corresponding to the Friedrichs extension    ${\bf{H}}_{F}$   and, respectively, Neumann extension    ${\bf{H}}_{N}$   (see Remark 3.1 and (5.5)).  

Now we are in position to state the main result of this section.  

Theorem 6.11.  Let    $\mathcal{G}$     a metric graph with ﬁnitely any ﬁnite volume ends,  $\#\mathfrak{C}_{0}(\mathcal{G})\;<\;\infty$  . Let also  C ,  D  be linear operators on  H  satisfying Rofe-Beketov conditions  (6.12) . Then:  

(i) The form    $\mathfrak{t}_{C,D}$   given by  (6.13) ,  (6.14)  is closed and lower semi-bounded in  $L^{2}(\mathcal{G})$  .  

(ii) The self-adjoint operator    ${\bf{H}}_{C,D}$   associated with the form    $\mathfrak{t}_{C,D}$   is a self-adjoint extension of    $\mathbf{H}_{0}$   and its domain is explicitly given by  

$$
\mathrm{dom}(\mathbf{H}_{C,D})=\{f\in\mathrm{dom}(\mathbf{H})\cap H^{1}(\mathcal{G})|\ C\Gamma_{0}f+D\Gamma_{1}f=0\}.
$$  

(iii) Conversely  $\widetilde{\bf H}$   is a self-adjoint extension of    $\mathbf{H}_{0}$     $\mathrm{dom}(\widetilde{\mathbf{H}})\subset H^{1}(\mathcal{G})$   ⊂ G , then there are  C, D th  $\widetilde{\mathbf{H}}=\mathbf{H}_{C,D}$  .  

(iv) Moreove  $\widetilde{\mathbf{H}}=\mathbf{H}_{C,D}$  e  is a Markovian extension if and only if the correspond- ing quadra  form   b  $\widehat{\mathfrak{t}}_{C,D}[y]=\langle D^{-1}C y,y\rangle_{\mathcal{H}}$   ⟨ ⟩ ,  $\mathrm{dom}(\hat{\mathfrak{t}})=\mathrm{ran}(D^{*})$  b  is a Dirichlet form on  in the wide sense.  

Proof.  (i) Since  H  is ﬁnite dimensional, it is straightforward to see that the form  $\mathfrak{t}_{C,D}$   is closed and lower semi-bounded in    $L^{2}(\mathcal{G})$   whenever    $C$   and    $D$   satisfy (6.12). (ii) By the ﬁrst representation theorem [50, Chapter VI.2.1],   $\mathrm{dom}(\mathbf{H}_{C,D})$   consists of all functions    $f\in\mathrm{dom}(\mathfrak{t}_{C,D})\subseteq H^{1}(\mathcal{G})$   for which there exists    $h\in L^{2}(\mathcal G)$   such that  

$$
\langle f^{\prime},g^{\prime}\rangle_{L^{2}(\mathcal{G})}+\langle D^{-1}C\Gamma_{0}f,\Gamma_{0}g\rangle_{\mathcal{H}}=\langle h,g\rangle_{L^{2}(\mathcal{G})}
$$  

for all    $g\in\mathrm{dom}(\mathfrak{t}_{C,D})$  . Moreover, in this case    $\mathbf{H}_{C,D}f:=h$  .  

The Gauss–Green identity (6.10) implies that for any    $f\in\mathrm{dom}(\mathbf{H}_{C,D})$   and    $g\in$   $\mathrm{dom}(\mathfrak{t}_{C,D})$  ,  

$$
\langle D^{-1}C\Gamma_{0}f,\Gamma_{0}g\rangle_{\mathcal{H}}=-\langle\Gamma_{1}f,\Gamma_{0}g\rangle_{\mathcal{H}}.
$$  

Taking into account the surjectivity property in Proposition   $6.6(\mathrm{i})$  , the inclusion ”  $\subseteq$  ” in (6.15) follows. The converse inclusion is then an immediate consequence of the Gauss–Green identity (6.10).  

(iii) To prove the claim, it suﬃces to show that  

$$
\Theta=\{(\Gamma_{0}f,\Gamma_{1}f)|\,f\in\mathrm{dom}(\widetilde{\mathbf{H}})\}\subseteq\mathcal{H}\times\mathcal{H}
$$  

is a self-adjoint linear relation (for further details we refer to Appendix A). By deﬁnition,   $\Theta^{*}$  is given by  

$$
\Theta^{*}=\{(g,h)\in\mathcal{H}\times\mathcal{H}|\,\langle\Gamma_{1}f,g\rangle_{\mathcal{H}}=\langle\Gamma_{0}f,h\rangle_{\mathcal{H}}\mathrm{~for~all~}f\in\mathrm{dom}(\widetilde{\mathbf{H}})\}.
$$  

The inclusion   $\Theta\subseteq\Theta^{*}$  foll s immediately from the Gauss–Green identity (6.10)  $\widetilde{\bf H}$  and the self-adjointness of . Indeed, we clearly have  

$$
0=\langle\widetilde{\mathbf{H}}f,\widetilde{f}\rangle_{L^{2}(\mathcal{G})}-\langle f,\widetilde{\mathbf{H}}\widetilde{f}\rangle_{L^{2}(\mathcal{G})}=-\langle\Gamma_{1}f,\Gamma_{0}\widetilde{f}\rangle_{\mathcal{H}}+\langle\Gamma_{0}f,\Gamma_{1}\widetilde{f}\rangle_{\mathcal{H}}
$$  

for all functions  $f,\tilde{f}\in\mathrm{dom}(\tilde{\mathbf{H}})$  ). On the other hand, by Proposition 6.8 and Propo- sition 6.6, for any (  $(g,h)\in\Theta^{*}$   ∈ there is a function   $\tilde{f}\in\mathrm{dom}(\mathbf{H})\cap H^{1}(\mathcal{G})$   ∈  ∩ G ) such that  $g=\Gamma_{0}\ddot{f}$   and  $h=\Gamma_{1}\ddot{f}$  ˜ . Employing the identity (6.10) once again, we see that  

$$
\begin{array}{r l}&{\langle\widetilde{\mathbf{H}}f,\widetilde{f}\rangle_{L^{2}(\mathcal{G})}=\langle f^{\prime},\widetilde{f}^{\prime}\rangle_{L^{2}(\mathcal{G})}-\langle\Gamma_{1}f,g\rangle_{\mathcal{H}}}\\ &{\qquad\qquad\qquad=\langle f^{\prime},\widetilde{f}^{\prime}\rangle_{L^{2}(\mathcal{G})}-\langle\Gamma_{0}f,h\rangle_{\mathcal{H}}=\langle f,\mathbf{H}\widetilde{f}\rangle_{L^{2}(\mathcal{G})}}\end{array}
$$  

for all    $f\in\mathrm{dom}(\widetilde{\mathbf{H}})$  ). Hence,   $\widetilde{f}\in\mathrm{dom}(\widetilde{\mathbf{H}})$  ∈   e ) and in particular   $(g,h)\in\Theta$  . Since   $\Theta$   is self-adjoint, there are    $C$   and  D  in  H  satisfying Rofe-Beketov conditions (6.12) and such that Θ =  $\Theta=\{(f,g)\in\mathcal{H}\times\mathcal{H}|\,C f+D g=0\}$   {  ∈H × H| } .  

(iv) The ﬁrst direction of the equivalence is clear: since the quadratic form  $\mathbf{t}_{N}$  associated with the Neumann extension    ${\bf{H}}_{N}$   is Markovian and  

$$
\Gamma_{0}\big(\varphi\circ f\big)=\big(\big(\varphi\circ f\big)(\gamma)\big)_{\gamma\in\mathfrak{C}_{0}(\mathcal{G})}=:\varphi\circ\big(\Gamma_{0}f\big)
$$  

for all functions    $f\in H^{1}(\mathcal G)$   and every normal contraction    $\varphi$  ,  $^\dagger$    the extension    ${\bf{H}}_{C,D}$  is Markovian if  $\widehat{\mathfrak{t}}_{C,D}$   is a Dirichlet form on    $\mathcal{H}$   in the wide sense.  

To prove the converse d   , for si  $f\in\mathrm{dom}(\widehat{\mathfrak{t}}_{C,D})$  ) be real-valued and ﬁx some real-valued   $\tilde{f}\,\in\,H^{1}(\mathcal G)$   ∈ G ) with Γ  $\Gamma_{0}\tilde{f}\,=\,f$   (the existence of such an   $\ddot{f}$  follows from Proposition 6.6). For any (real-valued) normal contraction    $\varphi\!:\mathbb{R}\to\mathbb{R}$  , we can construct a continuous and piecewise aﬃne function    $\psi\!:\mathbb{R}\rightarrow\mathbb{R}$   (i.e.,    $\psi$   is aﬃne on every component of    $\mathbb{R}\setminus\left\{x_{1},.\,.\,.\,,x_{M}\right\}$   for ﬁnitely many points    $x_{1},\cdot\cdot\cdot,x_{M},$  ) such t  $\psi(0)=0$  ,    $\psi(f(\gamma))=\varphi(f(\gamma))$   for all    $\gamma\in\mathfrak{C}_{0}(\mathcal{G})$   and    $|\psi^{\prime}(x)|=1$   for almost every  x  $x\in\mathbb{R}$   ∈ .   Notice that every function    $\psi$   with the above properties is a normal contraction. Hence, if    $\mathfrak{t}_{C,D}$   is Markovian, it follows that    $\psi\circ\tilde{f}\in\mathrm{dom}(\mathfrak{t}_{C,D})$   ∈ ). However, its boundary values are precisely given by  

$$
\Gamma_{0}(\psi\circ\tilde{f})=\psi\circ f=\varphi\circ f
$$  

an  conclude that    $\varphi\circ f$   belongs to   $\mathrm{dom}(\widehat{\mathfrak{t}}_{C,D})$  ). Finally, the Markovian property  t of  $\mathfrak{t}_{C,D}$   implies that  

$$
\mathfrak{t}_{C,D}[\psi\circ\tilde{f}]=\int_{\mathcal{G}}|(\psi\circ\tilde{f})^{\prime}|^{2}d x+\widehat{\mathfrak{t}}_{C,D}[\varphi\circ f]\leq\mathfrak{t}_{C,D}[\tilde{f}]=\int_{\mathcal{G}}|\tilde{f}^{\prime}|^{2}d x+\widehat{\mathfrak{t}}_{C,D}[f],
$$  

and noticing that    $|(\psi\!\circ\!\dot{f})^{\prime}|=|\ddot{f}^{\prime}|$  |  | |  almost everywhere on    $\mathcal{G}$  , the proof is complete.  

Let us demonstrate Theorem 6.11 by applying it to Cayley graphs.  

Corollary 6.12.  Let    $\mathcal{G}_{d}$   be a Cayley g h of a ﬁnitely generated group  $\mathsf{G}$   with one end. Then the Kir ch ho La plac ian  $\mathbf{H}_{0}$   admits a unique Markovian extension if and only if the underlyi g metric graph    $\mathcal{G}=\left(\mathcal{G}_{d},|\cdot|\right)$   has inﬁnite total volume,  $\mathrm{vol}({\mathcal{G}})=\infty$  . Moreover, if  G  has ﬁnite total volume, then the set of all Markovian extensions of    $\mathbf{H}_{0}$   forms a one-parameter family given explicitly by  

$$
\mathrm{dom}(\mathbf{H}_{\theta})=\{f\in\mathrm{dom}(\mathbf{H})\cap H^{1}(\mathcal{G})|\,\cos(\theta)\Gamma_{0}f+\sin(\theta)\Gamma_{1}f=0\},
$$  

where    $\theta\in[0,\pi/2]$  .  

Taking into account that amenable groups have ﬁnitely many ends, the above result applies to amenable ﬁnitely generated groups, which are not virtually inﬁnite cyclic (see Remark 2.5(iv)). In a similar way one can obtain a complete description of Markovian extensions in the case of virtually inﬁnite cyclic groups, however, they have two ends and the corresponding description looks a little bit more cumbersome and we leave it to the reader (cf. [31, p.147]). The case of groups with inﬁnitely many ends remains an open highly nontrivial problem.  

Remark 6.13.  A few remarks are in order.  

(i) Let us mention that in the case when the domain of the maximal operator  $\mathbf{H}$   is contained in    $H^{1}(\mathcal G)$   and    $\mathcal{G}$   has ﬁnitely many ﬁnite volume ends (n that by Theorem 4.1 in this case   $\mathrm{n}_{\pm}(\mathbf{H}_{0})=\#\mathfrak{C}_{0}(\mathcal{G})<\infty$  ),  Proposition 6.11 provides a complete description of all self-adjoint extensions of    $\mathbf{H}_{0}$  . Let us also mention that Proposition 6.11 provides a complete description of all self-adjoint restrictions of the Gaﬀney Laplacian    ${\mathbf{H}}_{G}$  , see Remark 5.6(ii).  

(ii) Some of the results of this section extend (to a certain extent) to the case of inﬁnitely many ends. Let us stress that by Proposition 4.9 in the case when    $\mathcal{G}$   has a ﬁnite volume end which is not free the above results would lead only to some (not all!) self-adjoint extensions of    $\mathbf{H}_{0}$  . In our opinion, even in the case of radially symmetric trees having ﬁnite total volume the description of all self-adjoint extensions of    $\mathbf{H}_{0}$   is a diﬃcult problem.  

(iii) Similar relations between Markovian realizations of elliptic operators on domains or ﬁnite metric graphs (with general couplings at the vertices) on one hand, and Dirichlet property of the corresponding quadratic form’s boundary term on the other hand, are of course well known in the literature (see, e.g., [14, Proposition 5.1], [47, Theorem 3.5], [57, Theorem 6.1]). How- ever, the setting of inﬁnite metric graphs additionally requires much more advanced considerations of combinatorial and topological nature. In par- ticular, it seems noteworthy to us that the results of the previous sections provide the right notion of the boundary for metric graphs, namely, the set of ﬁnite volume ends, to deal with ﬁnite energy and also with Markov- ian extensions of the minimal Kir ch ho La plac ian. In particular, this end space is well-behaved as concerns the introduction of traces and normal derivatives.  

(iv) Taking into account certain close relationships between quantum graphs and discrete Laplacians (see [27,  §  4]), one can easily obtain the results analogous to Theorem 4.1 and Theorem 6.11 for a particular class of discrete Laplacians on  $\mathcal{G}_{d}$   deﬁned by the following expression  

$$
(\tau f)(v):=\frac{1}{m(v)}\sum_{u\sim v}\frac{f(v)-f(u)}{|e_{u,v}|},\quad v\in\mathcal{V},
$$  

where    $m$   is the star weight (2.12). Markovian extensions of weighted dis- crete Laplacians were considered also in [52]. On the other hand, [52] does not contain a ﬁniteness assumption, however, the conclusion in our setting appears to be slightly stronger than in [52, Theorem 3.5], where the cor- respondence between Markovian extensions and Markovian forms on the boundary is in general not bijective.  

# 7.  Deficiency indices of antitrees  

The main aim of this section is to construct for any    $N\in\mathbb{Z}_{\geq1}\cup\{\infty\}$   a metric antitree such that the corresponding minimal Kir ch ho La plac ian  $\mathbf{H}_{0}$   has deﬁciency indices   $\mathrm{n}_{\pm}(\mathbf{H}_{0})=N$  . Our motivation stems from the fact that every antitree has exactly one end and hence, according to considerations in the previous sections,    $\mathbf{H}_{0}$  admits at most one-parameter family of Markovian extensions.  

7.1.  Antitree    $\mathcal{G}_{d}=(\mathcal{V},\mathcal{E})$   be a connected, simple combinatorial graph. Fix a root vertex  o  ∈V  and then order the graph with respect to the combinatorial spheres    $S_{n}$  ,    $n\geq0$   (notice that    $S_{0}=\{o\}$  ).    $\mathcal{G}_{d}$   is called an  antitree  if every vertex in  

![](images/3b3bdb66fa4e890d9cf56245ae9bb652c2c091783c3f5ae2f88367fecc90425b.jpg)  
Figure 1.  Antitree with sphere numbers    $s_{n}=n+1$  .  

$S_{n}$  ,    $n\geq1$  , is connected to all vertices in    $S_{n-1}$   and    $S_{n+1}$   and no vertices in    $S_{k}$   for all    $|k-n|\neq1$   (see Figure 1). Notice that each antitree is uniquely determined by its sequence of sphere numbers (  $s_{n}$  ),    $s_{n}:=\#S_{n}$   for    $n\geq0$  .  

While antitrees ﬁrst appeared in connection with random walks [25, 54, 77], they were actively studied from various diﬀerent perspectives in the last years (see [11, 22, 56] for quantum graphs and [21, Section 2] for further references).  

Let us enumerate the vertices in every combinatorial sphere    $S_{n}$   by   $(v_{i}^{n})_{i=1}^{s_{n}}$    and denote the edge connecting    $v_{i}^{n}$    with    $v_{j}^{n+1}$  by    $e_{i j}^{n}$  ,   $1\,\leq\,i\,\leq\,s_{n}$  ,   $1\,\leq\,j\,\leq\,s_{n+1}$  . We shall always use  $\mathcal{A}$   to denote (metric) antitrees.  

It is clear that every (inﬁnite) antitree has exactly one end. By Theorem 4.1, the deﬁciency indices of the corresponding minimal Kir ch ho La plac ian are at least 1  $\mathrm{vol}({\mathcal{A}})<\infty$  . On the other hand, under the additional symmetry assumption that A  is radially symmetric (that is, for each    $n\geq0$  , all edges connecting combinatorial spheres    $S_{n}$   and    $S_{n+1}$   have the same length), it is known that the deﬁciency indices are at most 1 (see [56, Theorem 4.1] and Example 4.11). It turns out that upon removing the symmetry assumption it is possible to construct antitrees such that the corresponding minimal Kir ch ho La plac ian has arbitrary ﬁnite or inﬁnite deﬁciency indices. More precisely, the main aim of this section is to prove the following result.  

Theorem 7.1.  Let    $\mathcal{A}$   be the antitree with sphere numbers    $s_{n}\:=\:n+1$  ,    $n\,\geq\,0$  (Figure 1). Then for each    $N\,\in\,\mathbb{Z}_{\geq1}\cup\{\infty\}$  there are edge lengths suc corresponding minimal Kir ch ho La plac ian  H 0  has the deﬁciency indices  $\mathrm{n}_{\pm}(\mathbf{H}_{0})=$   $N$  .  

7.2.  Harmonic functions.  As it was mentioned already, every harmonic function is uniquely determined by its values at the vertices. On the other hand,    $\mathbf{f}\in C({\mathcal{V}})$  deﬁnes a function    $f\in\mathbb{H}({\mathcal{A}})$   with    $f|_{\mathcal{V}}=\mathbf{f}$   if and only if the following conditions are satisﬁed:  

$$
\sum_{j=1}^{s_{n+1}}\frac{f(v_{j}^{n+1})-f(v_{k}^{n})}{|e_{k j}^{n}|}+\sum_{i=1}^{s_{n-1}}\frac{f(v_{i}^{n-1})-f(v_{k}^{n})}{|e_{i k}^{n-1}|}=0,
$$  

at each    $v_{k}^{n}$    ,   $1\leq k\leq s_{n}$   with    $n{\geq0}$  . We set    $s_{-1}:=0$  otational simplicity and hence the second summand in (7.1) is absent when  n  = 0. We can put the above diﬀerence equations into the more convenient matrix form. Denote    $\mathbf{f}_{n}\,:=\,f|_{S_{n}}\,=$   $(f(v_{i}^{n}))_{i=1}^{s_{n}}$    for all    $n\in\mathbb{Z}_{\geq0}$   and introduce matrices  

$$
\begin{array}{r l}&{M_{n+1}:=\left(\begin{array}{c c c c c}{\frac{1}{|e_{11}^{n}|}}&{\frac{1}{|e_{12}^{n}|}}&{\cdot\cdot\cdot}&{\frac{1}{|e_{1s_{n+1}}^{n}|}}\\ {\frac{1}{|e_{21}^{n}|}}&{\frac{1}{|e_{22}^{n}|}}&{\cdot\cdot\cdot}&{\frac{1}{|e_{2s_{n+1}}^{n}|}}\\ {\cdot\cdot\cdot}&{\cdot\cdot}&{\cdot\cdot}&{\cdot\cdot}\\ {\frac{1}{|e_{s_{n1}}^{n}|}}&{\frac{1}{|e_{s_{n2}}^{n}|}}&{\cdot\cdot\cdot}&{\frac{1}{|e_{s_{n}s_{n+1}}^{n}|}}\end{array}\right)\in\mathbb{R}^{s_{n}\times s_{n+1}},}\end{array}
$$  

and  

$$
D_{n}:=\operatorname{diag}(d_{k}^{n})\in\mathbb{R}^{s_{n}\times s_{n}},\qquad\quad d_{k}^{n}:=\sum_{j=1}^{s_{n+1}}\frac{1}{|e_{k j}^{n}|}+\sum_{i=1}^{s_{n-1}}\frac{1}{|e_{i k}^{n-1}|},
$$  

for all    $n\in\mathbb{Z}_{\geq0}$  . Notice the following useful identity  

$$
d_{1}^{0}=M_{1}\mathbb{1}_{s_{1}},\qquad\left(\begin{array}{c}{d_{1}^{n}}\\ {\vdots}\\ {d_{s_{n}}^{n}}\end{array}\right)=D_{n}\mathbb{1}_{s_{n}}=\left(M_{n+1}\ M_{n}^{*}\right)\left(\mathbb{1}_{s_{n+1}}\right),\quad n\geq1,
$$  

where  $\mathbb{1}_{s_{n}}:=(1,.\,.\,.\,,1)^{\top}\in\mathbb{R}^{s_{n}}$  . Hence (7.1) can be written as follows  

$$
\begin{array}{c}{{M_{1}{\bf f}_{1}=\displaystyle\sum_{j=1}^{s_{1}}\displaystyle\frac{1}{\vert e_{1j}^{0}\vert}{\bf f}_{0}=d_{1}^{0}{\bf f}_{0},}}\\ {{{\cal M}_{n+1}{\bf f}_{n+1}=D_{n}{\bf f}_{n}-M_{n}^{*}{\bf f}_{n-1},\quad n\geq1.}}\end{array}
$$  

Since    $D_{n}$   is invertible, we get  

$$
{\bf f}_{n}=D_{n}^{-1}(M_{n+1}~M_{n}^{*})\left(\!\!\begin{array}{c}{{{\bf f}_{n+1}}}\\ {{{\bf f}_{n-1}}}\end{array}\!\!\right)
$$  

for all    $n\geq1$  . In particular,    $\mathbf{f}_{n}\in\mathrm{ran}\left(D_{n}^{-1}(M_{n+1}\ M_{n}^{*})\right)$     for all    $n\geq1$  , which implies that the number of linearly independent solutions to the above diﬀerence equations (and hence the number of linearly independent harmonic functions) depends on the ranks of the matrices   $\left(M_{n+1}\ M_{n}^{*}\right)$  ),    $n\geq1$  . Let us demonstrate this by considering the following example.  

Lemma 7.2.  Let    $\mathcal{A}$   be a radially symmetric antitree. Then  

$$
\mathbb{H}(\mathcal{A})=\operatorname{span}\{\mathbb{1}_{\mathcal{G}}\}.
$$  

Proof.  Let for each    $n\geq0$  , all edges connecting combinatorial spheres    $S_{n}$   and    $S_{n+1}$  have the same length, say    $\ell_{n}>0$  . Clearly, in this case  

$$
\operatorname{ran}(M_{n+1})=\operatorname{ran}(M_{n}^{*})=\operatorname{span}\{\mathbb{1}_{s_{n}}\},
$$  

for all    $n\geq1$  . Moreover, each    $D_{n}$   is a scalar multiple of the identity matrix    $I_{s_{n}}$   and hence (7.7) implies that    $\mathbf f_{n}=c_{n}\mathbb I_{s_{n}}$   with some    $c_{n}\in\mathbb{C}$   for all    $n\geq0$  . Plugging this into (7.5)–(7.6), we get  

$$
c_{1}=c_{0},~~~~~~~~~~~~~c_{n+1}=c_{n}+\frac{s_{n-1}\ell_{n}}{s_{n+1}\ell_{n-1}}(c_{n}-c_{n-1}),~~n\geq1.
$$  

Hence    $c_{n}=c_{0}=f(o)$   for all    $n\geq0$  , which proves the claim.  

The latter in particular implies the following statement (cf. [56, Theorem 4.1]).  

Corollary 7.3.  If    $\mathcal{A}$   is a radial antitree with ﬁnite total volume, then    $\mathrm{n}_{\pm}(\mathbf{H}_{0})=1$  .  

Proof.  By Corollary 2.11, we only need to show that   $\mathrm{n}_{\pm}(\mathbf{H}_{0})\leq1$  . However,  

$$
\begin{array}{r}{\mathrm{n}_{\pm}(\mathbf{H}_{0})=\dim(\ker(\mathbf{H}))\leq\dim(\mathbb{H}(\mathcal{A}))=1.}\end{array}
$$  

7.3.  Finite deﬁciency indices.  We restrict our further considerations to a special case of polynomially growing antitrees. Namely, for every    $N\,\in\,\mathbb{Z}_{\geq1}$  , the antitree  $\mathcal{A}_{N}$   has sphere numbers    $s_{0}\,=\,1$   and    $s_{n}:=\,n+N$   for all    $n\in\mathbb{Z}_{\geq1}$  . To deﬁne its lengths, pick a sequence of positive numbers (  $\ell_{n}$  ) and set  

$$
|e_{i j}^{n}|:={\binom{2\ell_{n},\quad{\mathrm{if~}}1\leq i=j\leq N,}{\ell_{n},\quad{\mathrm{~otherwise}},}}
$$  

for all    $n\in\mathbb{Z}_{\geq0}$  .  

Lemma 7.4.  If a metric antitree    $\mathcal{A}_{N}$   has lengths given by  (7.9) , then  

$$
\dim\mathbb{H}({\mathcal{A}}_{N})=N+1.
$$  

Proof.  Denoting  

$$
B_{n,m}:=\left(\begin{array}{l l l l}{1}&{1}&{\ldots}&{1}\\ {1}&{1}&{\ldots}&{1}\\ {\ldots}&{\ldots}&{\ldots}&{\ldots}\\ {1}&{1}&{\ldots}&{1}\end{array}\right)\in\mathbb{R}^{n\times m},\qquad B_{n}:=B_{n,n}\in\mathbb{R}^{n\times n},
$$  

we get the following block-matrix form of the matrices    $M_{n+1}$  :  

$$
M_{n+1}=\frac{1}{\ell_{n}}\left(\!\!\begin{array}{c c}{{B_{N}-\frac{1}{2}I_{N}}}&{{B_{N,n+1}}}\\ {{B_{n,N}}}&{{B_{n,n+1}}}\end{array}\!\!\right)
$$  

for all    $n\geq1$  . Taking into account (7.3) and denoting  

$$
d_{n}^{1}:=\frac{n+N-3/2}{\ell_{n-1}}+\frac{n+N+1/2}{\ell_{n}},\quad d_{n}^{2}:=\frac{n+N-1}{\ell_{n-1}}+\frac{n+N+1}{\ell_{n}},
$$  

we get  

$$
D_{n}=\binom{d_{n}^{1}I_{N}\quad\;\;0}{0\quad\;\;d_{n}^{2}I_{n}}\,,
$$  

for all    $n\geq2$  . Since    $M_{1}\in\mathbb{C}^{1\times(N+1)}$    and  

$$
\mathrm{ran}(M_{n+1})=\mathrm{ran}(M_{n}^{*})=\mathrm{span}\left\{\left(\mathbf{f}_{N}\atop\mathbb{1}_{n}\right)\vert\;\mathbf{f}_{N}\in\mathbb{C}^{N}\right\},
$$  

for all    $n\geq2$  , (7.7) implies that every  f  solving (7.5)–(7.6) must be of the form  

$$
\mathbf{f}_{n}=\binom{\mathbf{f}_{n}^{N}}{c_{n}\mathbb{1}_{n}}\in\mathbb{C}^{N+n},\qquad\mathbf{f}_{n}^{N}\in\mathbb{C}^{N},\ \ c_{n}\in\mathbb{C},
$$  

for all    $n\geq1$  . Plugging (7.15) into (7.6) and taking into account that  

$$
B_{N}\mathbf{f}_{n}^{N}=\overline{{\mathbf{f}}}_{n}^{N}\mathbb{1}_{N},\qquad\qquad\qquad\overline{{\mathbf{f}}}_{n}^{N}:=\langle\mathbf{f}_{n}^{N},\mathbb{1}_{N}\rangle=B_{1,N}\mathbf{f}_{n}^{N},
$$  

we get after straightforward calculations  

$$
\overline{{\mathbf{f}}}_{n+1}^{N}+c_{n+1}(n+1)}\mathbb{1}_{N}-\frac{1}{2\ell_{n}}\mathbf{f}_{n+1}^{N}=d_{n}^{1}\mathbf{f}_{n}^{N}-\frac{\overline{{\mathbf{f}}}_{n-1}^{N}+c_{n-1}(n-1)}{\ell_{n-1}}\mathbb{1}_{N}+\frac{1}{2\ell_{n-1}}\mathbf{f}_{n-1}^{N},
$$  

$$
\frac{\overline{{\mathbf{f}}}_{n+1}^{N}+c_{n+1}(n+1)}{\ell_{n}}=c_{n}d_{n}^{2}-\frac{\overline{{\mathbf{f}}}_{n-1}^{N}+c_{n-1}(n-1)}{\ell_{n-1}},
$$  

for all    $n\geq2$  . Multiplying (7.17) with  $\mathbb{1}_{N}$   and then subtracting (7.16), we end up with  

$$
\mathbf{f}_{n+1}^{N}=2\ell_{n}(c_{n}d_{n}^{2}\mathbb{1}_{N}-d_{n}^{1}\mathbf{f}_{n}^{N})-\frac{\ell_{n}}{\ell_{n-1}}\mathbf{f}_{n-1}^{N},\quad n\geq2.
$$  

Next taking the inner product in (7.16) with  $\mathbb{I}_{N}$   and then subtracting (7.17) mul- tiplied by    $N-1/2$  , we ﬁnally get  

$$
c_{n+1}=\frac{\ell_{n}}{n+1}(2d_{n}^{1}\mathbf{\overline{{f}}}_{n}^{N}-(2N-1)d_{n}^{2}c_{n})-c_{n-1}\frac{(n-1)\ell_{n}}{(n+1)\ell_{n-1}},\quad n\geq2.
$$  

Taking into account that the value of    $f$   at the root    $o$   is determined by    $\mathbf{f}_{1}$   via  

$$
f(o)={\bf f}_{0}=\frac{2\ell_{0}}{2N+1}M_{1}{\bf f}_{1},
$$  

and noting that    $\mathbf{f}_{2}^{N}$    and    $c_{2}$    are also determined by    $\mathbf{f}_{1}$  , we conclude that (7.18)–(7.19) deﬁne  f  uniquely once    $\mathbf{f}_{1}\in\mathbb{C}^{N+1}$    is given. □  

Lemma 7.4 immediately implies that   $\mathrm{n}_{\pm}(\mathbf{H}_{0})\leq N+1$   if   $\mathrm{vol}(\mathcal{A}_{N})<\infty$  , where  $\mathbf{H}_{0}$   is the associated minimal operator. The next result shows that it can happen that   $\mathrm{n}_{\pm}\big(\mathbf{H}_{0}\big)=N+1$   upon choosing lengths    $\ell_{n}$   with a suﬃciently fast decay.  

Proposition 7.5.  Let    $\mathcal{A}_{N}$   be the antitree as in Lemma 7.4. If  (  $\ell_{n}$  )  is decreasing and  

$$
\sqrt{\ell_{n}}=\mathcal O\left(\frac{1}{(6\sqrt{N})^{n}(n+N+3)!}\right)
$$  

as    $n\to\infty$  , then    $\mathrm{n}_{\pm}\big(\mathbf{H}_{0}\big)=N+1$  .  

Proof.  It is immediate to see that   $\mathrm{vol}(\mathcal{A}_{N})<\infty$  if (7.21) is satisﬁed. Next, taking into account (7.9), observe that  

$$
m(v)=\sum_{v\in\mathcal{E}_{v}}|e|\leq(n+N)\ell_{n-1}+(n+N+2)\ell_{n}\lesssim n\ell_{n-1},\quad v\in S_{n},
$$  

as    $n\rightarrow\infty$  . Suppose    $f\,\in\,\mathbb{H}({\mathcal{A}})$   and set    $\mathbf f=f|\nu$  . Then    $\mathbf{f}$   has the form (7.15) and hence  

$$
||{\bf f}_{n}||^{2}=\sum_{v\in S_{n}}|f(v)|^{2}=||{\bf f}_{n}^{N}||^{2}+n|c_{n}|^{2},
$$  

for all    $n\geq1$  . This implies the following estimate  

$$
\sum_{v\in\mathcal{V}}|f(v)|^{2}m(v)=\sum_{n\geq0}\sum_{v\in S_{n}}|f(v)|^{2}m(v)\lesssim\sum_{n\geq1}n^{2}\ell_{n-1}(\|\mathbf{f}_{n}^{N}\|^{2}+|c_{n}|^{2}).
$$  

Next, (7.18)–(7.19) can be written as follows  

$$
\binom{\mathbf{f}_{n+1}^{N}}{c_{n+1}}=A_{1,n}\left(\binom{\mathbf{f}_{n}^{N}}{c_{n}}+A_{2,n}\left(\binom{\mathbf{f}_{n-1}^{N}}{c_{n-1}}\right),\right.
$$  

where the matrices    $A_{1,n},A_{2,n}\in\mathbb{R}^{(N+1)\times(N+1)}$    are given explicitly by  

$$
\begin{array}{r}{A_{1,n}:=\left(\!\!\begin{array}{c c}{-2\ell_{n}d_{n}^{1}I_{N}}&{2\ell_{n}d_{n}^{2}B_{N,1}}\\ {\frac{2\ell_{n}d_{n}^{1}}{n+1}B_{1,N}}&{-\frac{(2N-1)\ell_{n}d_{n}^{2}}{n+1}I_{1}\!}\end{array}\!\!\right),\quad A_{2,n}:=-\frac{\ell_{n}}{\ell_{n-1}}\left(\!\!\begin{array}{c c}{I_{N}}&{0}\\ {0}&{\frac{n-1}{n+1}I_{1}}\end{array}\!\!\right),}\end{array}
$$  

for all    $n\geq2$  . Since    $\ell_{n-1}\leq\ell_{n}$   and  

$$
d_{n}^{1}<d_{n}^{2}=\frac{n+N-1}{\ell_{n-1}}+\frac{n+N+1}{\ell_{n}}\leq\frac{2(n+N)}{\ell_{n}}
$$  

for all    $n\geq2$  , it is not diﬃcult to get the following rough bounds    $^\dagger$  

$$
\|A_{1,n}\|\leq6\sqrt{N}(n+N),\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \|A_{2,n}\|=\frac{\ell_{n}}{\ell_{n-1}}\leq1,
$$  

for all    $n\geq2N$  . Denoting  

$$
F_{n}:=\binom{\mathbf{f}_{n}^{N}}{c_{n}}\,,\quad n\ge1,
$$  

the recurrence relations (7.18)–(7.19) can be written in the following matrix form  

$$
\binom{F_{n+1}}{F_{n}}=\binom{A_{1,n}}{I_{N+1}}\,\binom{A_{2,n}}{F_{n-1}}=A_{n}\,\binom{F_{n}}{F_{n-1}}\,.
$$  

Taking into account (7.26), we get  ∥  $\|A_{n}\|\leq6{\sqrt{N}}(n+N+1)$  ∥≤ √  for all    $n\geq2N$  , which implies the estimate  

$$
\sqrt{\|\mathbf{f}_{n}^{N}\|^{2}+|c_{n}|^{2}}=\|F_{n}\|\leq C\prod_{k=1}^{n-1}\|A_{k}\|\lesssim(6\sqrt{N})^{n}(n+N)!
$$  

for all    $n\geq2$  . Combining this bound with (7.21), it is easy to see that the series on the right hand side in (7.22) converges and hence by Lemma 2.13 we conclude that  $\mathbb{H}({\mathcal{A}}_{N})\subset L^{2}({\mathcal{A}})$  . Thus   $\ker(\mathbf{H})=\mathbb{H}(\mathcal{A}_{N})$   and the use of Corollary 2.11 ﬁnishes the proof. □  

7.4.  Inﬁnite deﬁciency indices.  Consider the antitree    $\mathcal{A}$   with sphere numbers  $s_{n}:=n\!+\!1$  ,    $n\geq0$  . Next pick a sequence of positive numbers (  $\ell_{n}$  ) and deﬁne lengths as follows  

$$
|e_{i j}^{n}|=\binom{2\ell_{n},\quad1\leq i=j\leq n+1,}{\ell_{n},\quad\mathrm{otherwise},}
$$  

for all    $n\in\mathbb{Z}_{\geq0}$  . Thus, the corresponding matrix    $M_{n+1}$   given by (7.2) has the form  

$$
M_{n+1}=\frac{1}{\ell_{n}}\left(B_{n+1}-\frac{1}{2}I_{n+1}\quad B_{n+1,1}\right)\in\mathbb{R}^{(n+1)\times(n+2)}
$$  

for all    $n\geq0$  . Let us denote this antitree by    $\mathcal{A}_{\infty}$  .  

Lemma 7.6.    $\dim(\mathbb{H}({\mathcal{A}}_{\infty}))=\infty$  .  

Proof.  Consider the diﬀerence equations (7.5)–(7.6). Clearly, the matrix    $M_{n+1}$   has the maximal rank    $n+1$   for every    $n\geq0$  . Taking into account that  

$$
\Big(B_{n+1}-\frac{1}{2}I_{n+1}\Big)^{-1}=\frac{4}{2n+1}B_{n+1}-2I_{n+1}=:C_{n},\quad n\geq0,
$$  

(7.6) then reads  

$$
\begin{array}{r l}{\left(I_{n+1}\right.}&{{}\frac{2}{2n+1}B_{n+1,1}\right)\mathbf{f}_{n+1}=\ell_{n}C_{n}(D_{n}\mathbf{f}_{n}-M_{n}^{*}\mathbf{f}_{n-1})}\end{array}
$$  

for all    $n\geq1$  . Observe that  

$$
\left(I_{n+1}\quad{\textstyle\frac{2}{2n+1}}B_{n+1,1}\right)\left(\begin{array}{c}{{f_{1}}}\\ {{\vdots}}\\ {{f_{n+1}}}\\ {{0}}\end{array}\right)=\left(\begin{array}{c}{{f_{1}}}\\ {{\vdots}}\\ {{f_{n+1}}}\end{array}\right)
$$  

y    $\mathbf{f}_{n}\in\mathbb{C}^{n+1}$    and    $\mathbf{f}_{n-1}\in\mathbb{C}^{n}$    there always exis a unique    $\mathbf{f}_{n+1}=$   $(f_{1},\ldots,f_{n+1},0)^{\top}$  satisfying (7.31). Now pick a natural number  N  and deﬁne  f  $\mathbf{f}^{N}\in$    ∈  $C(\mathcal{A}_{\infty})$   by setting    $\mathbf{f}_{n}^{N}:=(0,.\,.\,,0)^{\top}\in\mathbb{C}^{n+1}$  ∈  for all    $n\in\{0,.\,.\,.\,,N\}$  ,  

$$
\mathbf{f}_{N+1}^{N}:=(1,.\,.\,,1,-N-1/2)^{\top},
$$  

and  

$$
\mathbf{f}_{n+1}^{N}:=\binom{\ell_{n}C_{n}\big(D_{n}\mathbf{f}_{n}^{N}-M_{n}^{*}\mathbf{f}_{n-1}^{N}\big)}{0}\in\mathbb{C}^{n+2}
$$  

for all    $n\geq N+1$  . Clearly,    $\mathbf{f}^{N}$    satisﬁes (7.5)–(7.6) and hence deﬁnes a harmonic function    $f^{N}\,\in\,\mathbb{H}(A_{\infty})$  . Moreover, it is easy to see that   $\operatorname{span}\{\mathbf{f}^{N}\}_{N\geq1}$   is inﬁnite dimensional, which proves the claim. □  

Proposition 7.7.  Let    $\mathbf{H}_{0}$   be the minimal Kir ch ho La plac ian associated with the antitree  $\mathcal{A}_{\infty}$  . If    $\ell_{n}$   is decreasing and  

$$
\sqrt{\ell_{n}}=\mathcal{O}\left(\frac{1}{6^{n}(n+3)!}\right)
$$  

as    $n\to\infty$  , then    $\mathrm{n}_{\pm}(\mathbf{H}_{0})=\infty$  .  

Proof.  Clearly, it suﬃces to show that every    $f^{N}$    constructed in the proof of Lemma 7.6 belongs to    $L^{2}(\mathcal{G})$   if    $\ell_{n}$   decays as in (7.33). To prove this we shall proceed as in the proof of Proposition 7.5. First, taking into account (7.29), observe that  

$$
m(v)\lesssim n\ell_{n-1},\quad v\in S_{n},
$$  

as    $n\to\infty$  . Since    $\begin{array}{r}{\|\mathbf{f}_{n}^{N}\|^{2}=\sum_{v\in S_{n}}|f^{N}(v)|^{2}}\end{array}$   for all    $n\geq0$  , we get the estimate  

$$
\sum_{\boldsymbol{v}\in\mathcal{V}}|f^{N}(\boldsymbol{v})|^{2}m(\boldsymbol{v})\lesssim\sum_{n\geq N+1}\sum_{\boldsymbol{v}\in S_{n}}|f^{N}(\boldsymbol{v})|^{2}m(\boldsymbol{v})\lesssim\sum_{n\geq N+1}n\ell_{n-1}\|\mathbf{f}_{n}^{N}\|^{2}.
$$  

Denoting    $F_{n}:=\mathbf{f}_{n}^{N}$    for all    $n\geq1$  , we can put (7.31) into the matrix form  

$$
{\binom{F_{n+1}}{F_{n}}}={\binom{A_{1,n}}{I_{n+1}}}\quad A_{0,n+1,n}{\binom{F_{n}}{F_{n-1}}}=A_{n}\left({F_{n}\atop F_{n-1}}\right)
$$  

for all    $n\geq N+1$  , where  

$$
\begin{array}{r}{A_{1,n}:=\left(\!\!\begin{array}{c}{\ell_{n}C_{n}D_{n}}\\ {0_{1,n+1}}\end{array}\!\!\right)\in\mathbb{R}^{(n+2)\times(n+1)},\quad A_{2,n}:=\left(\!\!\begin{array}{c}{-\ell_{n}C_{n}M_{n}^{*}}\\ {0_{1,n}}\end{array}\!\!\right)\in\mathbb{R}^{(n+2)\times n}.}\end{array}
$$  

Now observe that    $\|C_{n}\|\;=\;2$   and    $\|\ell_{n}D_{n}\|\;\leq\;2(n+1)$   for all    $n\geq1$  . Moreover,  $\|\ell_{n}M_{n}^{*}\|\leq n+1$  ∥≤  + 1 for all    $n\geq1$  , which immediately implies the following estimate  

$$
\begin{array}{r}{\|A_{n}\|\leq\sqrt{\|\ell_{n}C_{n}D_{n}\|^{2}+1+\|\ell_{n}C_{n}M_{n}^{*}\|^{2}}\leq6(n+1),\quad n\geq N+1.}\end{array}
$$  

Hence we get  

$$
\|\mathbf{f}_{n+1}^{N}\|\leq C\prod_{k=N+1}^{n}\|A_{k}\|\leq C6^{n-N}\frac{(n+1)!}{(N+1)!}\lesssim6^{n}(n+1)!
$$  

for all    $n\;\geq\;N\,+\,1$  . Combining this estimate with (7.34) and (7.33) and usi Lemma 2.13, we conclude that    $f^{N}\in L^{2}(\mathcal{A}_{\infty})$   for each    $N\geq1$  . □  

Remark 7.8.  It is not diﬃcult to show that    $f^{N}$    does not belong to    $H^{1}(\mathcal{A}_{\infty})$   for the above choices of edge lengths. In fact, it follows from the maximum principle for

  $\mathbb{H}(\mathcal{A})$   that if   $\mathrm{vol}({\mathcal{A}})<\infty$  , then    $\mathbb{H}(\mathcal{A})\cap H^{1}(\mathcal{A})$   consists only of constant functions.  

7.5.  Proof of Theorem 7.1.  Clearly, the case of inﬁnite deﬁciency indices follows from Proposition 7.7. On the other hand, since adding and/or removing ﬁnitely many edges and vertices to a graph does not change the deﬁciency indices of the minimal Kir ch ho La plac ian, Proposition 7.5 completes the proof of Theorem 7.1. Indeed, every antitree    $\mathcal{A}_{N}$   can be obtained from    $\mathcal{A}$   by ﬁrst ving all the edges between combinatorial spheres    $S_{0}$   and    $S_{N}$   and then adding  N  + 1 edges connecting the root    $o$   with the vertices in    $S_{N}$  . □  

Remark 7.9.  Since every inﬁnite antitree has exactly one end, Theorem 6.11(iv) implies that the Kir ch ho La plac ian    $\mathbf{H}_{0}$   in Theorem 7.1 has a unique Markovian extension exactly when   $\operatorname{vol}({\mathcal{A}})=\infty$  . If   $\mathrm{vol}({\mathcal{A}})<\infty$  , then Markovian extensions of    $\mathbf{H}_{0}$   form a one-parameter family explicitly given by (6.17). Notice that (6.17) looks similar to the description of self-adjoint extensions of the minimal Kirchhoﬀ Laplacian on radially symmetric antitrees obtained recently in [56].  

Let us also emphasize that the antitree constructed in Proposition 7.7 has ﬁnite total volume and    $\mathbf{H}_{0}$   has inﬁnite deﬁciency indices, however, the set of Markovian extensions of    $\mathbf{H}_{0}$   forms a one-parameter family.  

Let us ﬁnish this section with one more comment. As it was proved, the dimension of the space of Markovian extensions depends only on the space of graph ends and, moreover, it is equal to the number of ﬁnite volume ends. However, deﬁciency indices (dimension of the space of self-adjoint extensions) are in general independent of graph ends and we can only provide a lower bound. Moreover, the above example of a polynomially growing antitree shows that the space of non-constant harmonic functions heavily depends on the choice of edge lengths (in particular, its dimension may vary between zero and inﬁnity). In this respect let us also emphasize that in the case of Cayley graphs of ﬁnitely generated groups the end space is independent of the choice of a generating set, however, simple examples show that the space of harmonic functions does depend on this choice.  

# Appendix  A.  Linear relations in Hilbert spaces  

In this section we collect basic notions and facts on linear relations in Hilbert spaces, a very convenient concept of multi-valued linear operators. For simplicity, we shall assume tha  $\mathcal{H}$   is a ﬁnite dimensional Hilbert space ,    $N:=\dim({\mathcal{H}})<\infty$  .  

A  linear relation  Θ in    $\mathcal{H}$   is a linear subspace in    $\mathcal{H}\times\mathcal{H}$  . Linear operators become special linear relations (single valued) after identifying them with their graphs in  $\mathcal{H}\times\mathcal{H}$  . Consider linear relations in  $\mathcal{H}$   having the form  

$$
\begin{array}{r}{\Theta_{C,D}=\{(f,g)\in\mathcal{H}\times\mathcal{H}\,|\,C f=D g\},}\end{array}
$$  

where    $C,D$   are linear operators on    $\mathcal{H}$  . Notice that diﬀerent    $C$   and    $D$   may deﬁne the same linear relation. The  domain  and the  multi-valued part  of   $\Theta_{C,D}$   are given by  

$$
\begin{array}{r l}&{\operatorname{dom}(\Theta_{C,D})=\{f\in\mathcal{H}\,|\,\exists g\in\mathcal{H},C f=D g\}=\{f\in\mathcal{H}\,|\,C f\in\mathrm{ran}(D)\},}\\ &{\operatorname{mul}(\Theta_{C,D})=\{g\in\mathcal{H}\,|\,D g=0\}=\ker(D).}\end{array}
$$  

In particular,   $\Theta_{C,D}$   is a graph of a linear operator only if   $\ker(D)=\{0\}$  . The adjoint relation   $\Theta_{C,D}^{*}$    to   $\Theta_{C,D}$   is given by  

$$
\begin{array}{r l}&{\Theta_{C,D}^{*}=\big\{(f,g)\in\mathcal{H}\times\mathcal{H}\,\big|\,\langle\widetilde{g},f\rangle_{\mathcal{H}}=\langle\widetilde{f},g\rangle_{\mathcal{H}}\;\forall(\widetilde{f},\widetilde{g})\in\Theta_{C,D}\big\}}\\ &{\qquad=\big\{(D^{*}f,C^{*}f)\,\big|\,f\in\mathcal{H}\big\}.}\end{array}
$$  

Thus, a linear relation   $\Theta_{C,D}$   is self-adjoint,   $\Theta_{C,D}=\Theta_{C,D}^{*}$  , if and only if    $C$   and    $D$  satisfy the  Rofe-Beketov conditions  [68] (see also [69, Exercises 14.9.3-4]):  

$$
\begin{array}{r}{C D^{*}=D C^{*},\qquad\qquad\qquad0\in\rho(C^{*}C+D^{*}D).}\end{array}
$$  

Taking into account that every linear relation in    $\mathcal{H}$   admits one of the forms (A.1) or (A.2), this provides a description of self-adjoint linear relations in    $\mathcal{H}$  . Notice also that the second condition in (A.3) is equivalent to the fact that the matrix

  $(C|D)\in\mathbb{C}^{N\times2N}$    has the maximal rank    $N$  .  

Recall also that every self-adjoint linear relation admits the representation   $\Theta=

$   $\Theta_{\mathrm{op}}\oplus\Theta_{\mathrm{mul}}$  , where   $\Theta_{\mathrm{mul}}:=\{0\}\times\mathrm{mul}(\Theta)$   and   $\Theta_{\mathrm{op}}$  , called the operator part of   $\Theta$  , is a graph of a linear operator. In particular, for a self-adjoint linear relation   $\Theta_{C,D}$  one has  

$$
\mathrm{dom}(\Theta_{C,D})=\mathrm{mul}(\Theta_{C,D})^{\perp}=\mathrm{ker}(D)^{\perp}=\mathrm{ran}(D^{*}).
$$  

For further details on linear relations we refer the reader to, e.g., [69, Chapter 14.1].  

# Appendix  B.  A rope ladder graph  

Let us introduce a rope ladder graph depicted on Figure 2. Let    $\mathcal{G}_{d}=(\mathcal{V},\mathcal{E})$   be a simple graph with the vertex set    $\mathcal{V}:=\{o\}\cup\mathcal{V}^{+}\cup\mathcal{V}^{-}$  , where    $o\,=\,v_{0}$   is a root,  $\mathcal{V}^{+}=(v_{n}^{+})_{n\geq1}$  and    $\mathcal{V}^{-}=(v_{n}^{-})_{n\geq1}$   are two disjoint countably inﬁnite sets of vertices. The edge set  E  is deﬁned as follows:  

•    $o$   is connected to    $v_{1}^{+}$    and    $\displaystyle v_{1}^{-}$    by the “diagonal” edges    $e_{0}^{+}$    and    $e_{0}^{-}$  , respectively; •  for each    $n\geq1$  ,    $v_{n}^{\pm}$    is connected to    $v_{n+1}^{\pm}$    by the vertical edge    $e_{n}^{\pm}$    ; •  for each    $n\geq1$  ,    $v_{n}^{+}$    and    $v_{n}^{-}$    are connected by the horizontal edge    $e_{n}$  .  

![](images/0b6c5c0ca0ee882e974795c38944c73cceed73254a4bd7a0c124e9fead56ebe8.jpg)  
Figure 2.  The rope ladder graph.  

By construction,   $\deg(o)=2$   and   $\deg(v_{n}^{+})=\deg(v_{n}^{-})=3$  ) = 3 for all    $n\geq1$  . Moreover, an inﬁnite rope ladder graph has exactly one end. Notice also that a similar example was studied in [46, Section 7] (see also [33,  §  5]) in context with the construction of non-constant harmonic functions of ﬁnite energy.  

Equip now    $\mathcal{G}_{d}$   with edge lengths    $|\cdot|\colon{\mathcal{E}}\to(0,\infty)$   and consider the corresponding minimal KirchhoﬀLaplacian    $\mathbf{H}_{0}$   on the metric graph    $\mathcal{G}=\left(\mathcal{G}_{d},|\cdot|\right)$  . The next result immediately follows from Theorem 2.8 and Corollary 2.11.  

# Corollary B.1.  If  

$$
\sum_{n\geq1}\left|e_{n}^{+}\right|+\left|e_{n}\right|=\infty,\quad a n d\quad\sum_{n\geq1}\left|e_{n}^{-}\right|+\left|e_{n}\right|=\infty,
$$  

then the Kir ch ho La plac ian    $\mathbf{H}_{0}$   is self-adjoint. If  

$$
\operatorname{vol}(\mathcal{G})=\sum_{n\geq1}|e_{n}^{+}|+|e_{n}^{-}|+|e_{n}|<\infty,
$$  

then    $\mathrm{n}_{\pm}(\mathbf{H}_{0})\geq1$  .  

We omit the proof since it is easy to check that the ﬁrst condition is equivalent to the geodesic completeness of   $(\mathcal{V},\varrho_{m})$   (cf. Theorem 2.8). Due to the symmetry of the underlying combinatorial graph, the gap between the above two conditions is equivalent to the fact that the corresponding lengths satisfy  

$$
\sum_{n\geq1}|e_{n}^{+}|=\infty,\qquad\qquad\qquad\sum_{n\geq1}|e_{n}^{-}|+|e_{n}|<\infty.
$$  

Next, let us describe the space of harmonic functions    $\mathbb{H}(\mathcal{G})$  Lemma B.2.  Let    $a,b\in\mathbb{C}$  . Then there is exactly one    $f\in\mathbb{H}({\mathcal{G}})$   such that  

$$
f(v_{1}^{+})=a,\qquad\qquad\qquad\qquad f(v_{1}^{-})=b.
$$  

Moreover, this function    $f$   is recursively given by  

$$
f(o)=\frac{b|e_{0}^{+}|+a|e_{0}^{-}|}{|e_{0}^{+}|+|e_{0}^{-}|}
$$  

and  

$$
f(v_{n+1}^{\pm})=\left(1+\frac{|e_{n}^{\pm}|}{|e_{n-1}^{\pm}|}+\frac{|e_{n}^{\pm}|}{|e_{n}|}\right)f(v_{n}^{\pm})-\frac{|e_{n}^{\pm}|}{|e_{n-1}^{\pm}|}f(v_{n-1}^{\pm})-\frac{|e_{n}^{\pm}|}{|e_{n}|}f(v_{n}^{\mp}),
$$  

for all    $n\in\mathbb{Z}_{\geq1}$  , where we use the notation    $v_{0}^{+}:=v_{0}^{-}:=o$  .  

Proof.  Suppose    $a,b\in\mathbb{C}$   are given and    $f\in\mathbb{H}(\mathcal{G})$   satisﬁes (B.4). Since    $f$   is linear on every edge and satisﬁes (2.7) at    $v=o$  , we get  

$$
0=f_{e_{0}^{+}}^{\prime}(o)+f_{e_{0}^{-}}^{\prime}(o)=\frac{f(v_{1}^{+})-f(o)}{|e_{0}^{+}|}+\frac{f(v_{1}^{-})-f(o)}{|e_{0}^{-}|}=\frac{a-f(o)}{|e_{0}^{+}|}+\frac{b-f(o)}{|e_{0}^{-}|},
$$  

which implies (B.5). Moreover, Kir ch ho conditions (2.7) at    $v=v_{n}^{\pm}$    ,    $n\geq1$   read  

$$
\frac{f(v_{n+1}^{\pm})-f(v_{n}^{\pm})}{|e_{n}^{\pm}|}+\frac{f(v_{n-1}^{\pm})-f(v_{n}^{\pm})}{|e_{n-1}^{\pm}|}+\frac{f(v_{n}^{\mp})-f(v_{n}^{\pm})}{|e_{n}|}=0.
$$  

This implies that    $f$   is given by (B.6). Hence there is at most one    $f\in\mathbb{H}({\mathcal{G}})$   satisfying

 (B.4) for given    $a,b\,\in\,\mathbb{C}$  . However, the same calculation shows that    $f$   deﬁned by

 (B.5) and (B.6) has this property. Thus, existence follows as well. □ From Lemma B.2, it is clear that   $\dim(\mathbb{H}(\mathcal{G}))=2$  , and, moreover,  

$$
\begin{array}{r}{\mathbb{H}(\mathcal{G})=\operatorname{span}\{\mathbb{1}_{\mathcal{G}},g_{0}\},}\end{array}
$$  

where  $\mathbb{1}_{\mathcal{G}}$   denotes the constant function on    $\mathcal{G}$   and    $g_{0}\in\mathbb{H}(\mathcal{G})$   is the function deﬁned, for example, by the following normalization  

$$
g_{0}(0)=0,\qquad\qquad g_{0}(v_{1}^{+})=|e_{0}^{+}|,\qquad\qquad g_{0}(v_{1}^{-})=-|e_{0}^{-}|.
$$  

Notice that    $g_{0}(v_{n}^{\pm})$  ),    $n\geq1$   are then given recursively by (B.6).  

Lemma B.3.    $I f\,\mathrm{vol}(\mathcal{G})<\infty$  , then  

$$
\mathbb{H}(\mathcal{G})\cap H^{1}(\mathcal{G})=\operatorname{span}\{\mathbb{1}_{\mathcal{G}}\}.
$$  

The claim immediately follows from the fact that a rope ladder graph has exactly one end. However, let us present a direct proof based on the analysis of harmonic functions.  

Proof.  Taking into account (B.8), we only need to show that    $g_{0}\notin H^{1}(\mathcal{G})$  ∈ G ). First, ob- serve that   $(g_{0}(v_{n}^{+}))_{n\geq1}$    and   $(g_{0}(v_{n}^{-}))_{n\geq1}$    are strictly increasing positive, respectively, strictly decreasing negative sequences. Indeed,  

$$
-|e_{0}^{-}|=g_{0}(v_{1}^{-})<0=g_{0}(o)<g_{0}(v_{1}^{+})=|e_{0}^{+}|
$$  

by the very deﬁnition of    $g_{0}$  . Let    $n\geq1$   and assume now that we have already shown that   $(g_{0}(v_{k}^{+}))_{k=1}^{n}$    is strictly increasing and   $(g_{0}(v_{k}^{-}))_{k=1}^{n}$    is strictly decreasing. Since  $g_{0}(o)=0$  , (B.6) implies  

$$
\begin{array}{r l r}&{}&{g_{0}(v_{n+1}^{+})=\Big(1+\frac{|e_{n}^{+}|}{|e_{n-1}^{+}|}+\frac{|e_{n}^{+}|}{|e_{n}|}\Big)g_{0}(v_{n}^{+})-\frac{|e_{n}^{+}|}{|e_{n-1}^{+}|}g_{0}(v_{n-1}^{+})-\frac{|e_{n}^{+}|}{|e_{n}|}g_{0}(v_{n}^{-})}\\ &{}&{\quad>\left(1+\frac{|e_{n}^{+}|}{|e_{n}|}\right)g_{0}(v_{n}^{+})+\frac{|e_{n}^{+}|}{|e_{n-1}^{+}|}(g_{0}(v_{n}^{+})-g_{0}(v_{n-1}^{+}))>g_{0}(v_{n}^{+}).}\end{array}
$$  

A similar argument shows that    $g_{0}(v_{n+1}^{-})<g_{0}(v_{n}^{-})$  ) and hence the claim follows by induction. Now monotonicity immediately implies  

$$
\begin{array}{l l r}{\lefteqn{\|g_{0}^{\prime}\|_{L^{2}(\mathcal{G})}^{2}=\displaystyle\sum_{e\in\mathcal{E}}\int_{e}|g_{0}^{\prime}(x_{e})|^{2}\;d x_{e}\geq\displaystyle\sum_{n\geq0}\int_{e_{n}}|g_{0}^{\prime}(x_{e})|^{2}\;d x_{e}}}\\ &{}&{=\displaystyle\sum_{n=0}^{\infty}\frac{|g_{0}(v_{n}^{+})-g_{0}(v_{n}^{-})|^{2}}{|e_{n}|}\geq|g_{0}(v_{1}^{+})-g_{0}(v_{1}^{-})|^{2}\sum_{n=0}^{\infty}\frac{1}{|e_{n}|}=\infty,}\end{array}
$$  

since   $\mathrm{vol}(\mathcal G)<\infty$  . Thus    $g_{0}\notin H^{1}(\mathcal{G})$  ∈ G ).  

In particular, this also leads to the following result:  

Corollary B.4.  If    $\mathrm{vol}(\mathcal G)<\infty$  , then    $\mathrm{n}_{\pm}(\mathbf{H}_{0})\in\{1,2\}$  . Moreover,    $\mathrm{n}_{\pm}(\mathbf{H}_{0})=1$   if and only if    $g_{0}\notin L^{2}(\mathcal G)$  ∈ G .  

Proof.  The claim about the deﬁciency indices follows from Corollary 2.11 and the fact that  $\mathbb{1}_{\mathcal{G}}\in L^{2}(\mathcal{G})$  . The equivalences then follow from Lemma B.3. □  

As the next example shows, the inclusion    $g_{0}\,\in\,L^{2}(\mathcal{G})$   heavily depends on the choice of edge lengths.  

Example B.5.  Fix    $s>3$   and equip the rope ladder graph with edge lengths  

$$
|e_{n}^{+}|=|e_{n}^{-}|:={\frac{1}{(n+1)^{s}}},\qquad|e_{n}|:={\frac{2n}{(n+1)^{s}-n^{s}}},\quad n\in\mathbb{Z}_{\geq0}.
$$  

Then    $|e_{n}|\sim n^{2-s}$    for large    $n$   and hence   $\mathrm{vol}(\mathcal G)<\infty$  . Moreover, for this particular choice of edge lengths we have    $g_{0}(v_{n}^{\pm})=\pm n$   ±  for all    $n\geq1$  . Indeed,    $g_{0}(v_{1}^{\pm})=\pm1$   ± 1 by (B.7). Assuming we have already proven that    $g_{0}(v_{k}^{\pm})=\pm k$   for    $k\leq n$   with some  $n\geq1$  , we have by (B.6):  

$$
\begin{array}{l}{g_{0}(v_{n+1}^{+})=\Big(1+\displaystyle\frac{n^{s}}{(n+1)^{s}}+\displaystyle\frac{1}{(n+1)^{s}|e_{n}|}\Big)n-\displaystyle\frac{n^{s}(n-1)}{(n+1)^{s}}+\displaystyle\frac{n}{(n+1)^{s}|e_{n}|}}\\ {=n+\displaystyle\frac{n^{s}}{(n+1)^{s}}+\displaystyle\frac{2n}{(n+1)^{s}|e_{n}|}=n+\displaystyle\frac{n^{s}}{(n+1)^{s}}+\displaystyle\frac{(n+1)^{s}-n^{s}}{(n+1)^{s}}=n+1.}\end{array}
$$  

Analogously,    $g_{0}(v_{n+1}^{-})=-(n+1)$   + 1) and hence the claim follows by induction.  

Applying Lemma B.3 and using again that    $|e_{n}|\sim n^{2-s}$    as    $n\to\infty$  , we conclude that    $g_{0}\in L^{2}(\mathcal G)$   exactly (see Lemma 2.13) when  

$$
\sum_{n\geq1}|g_{0}(v_{n}^{\pm})|^{2}(|e_{n-1}^{\pm}|+|e_{n}^{\pm}|)=\sum_{n\geq1}n^{2}((n+1)^{-s}+n^{-s})<\infty
$$  

and  

$$
\sum_{n\geq1}|g_{0}(v_{n}^{\pm})|^{2}|e_{n-1}|=\sum_{n\geq1}\frac{2n^{3}}{(n+1)^{s}-n^{s}}<\infty.
$$  

Clearly, the latter holds only if    $s>5$  . Hence, by Lemma B.4,   $\mathrm{n}_{\pm}(\mathbf{H}_{0})=2$   for all  $s>5$  . In particular,   $\ker(\mathbf{H})\subset H^{1}(\mathcal{G})\Leftrightarrow s\leq5$  .  

# Acknowledgments  

We thank Matthias Keller, Daniel Lenz, Primoˇ z Moravec, Andrea Posilicano and Wolfgang Woess for useful discussions and hints with respect to the literature. We also thank the referees for their comments which have helped us to improve the manuscript. N.N. appreciates the hospitality at the Institute of Mathematics, University of Potsdam, during a research stay funded by the OeAD (Marietta Blau- grant, ICM-2019-13386), where a part of this work was done.  

# References  

[1] N. I. Akhiezer and I. M. Glazman,  Theory of Linear Operators in Hilbert Spaces. Vol. II , Dover Publ., New York, 1993. [2] O. Amini and L. Caporaso,  Riemann–Roch theory for weighted graphs and tropical curves ,  240 Adv. Math. , 1–23 (2013). [3] W. Arendt and A. F. M. ter Elst,  Operators with continuous kernels , Integr. Equ. Oper.  91 Theory , no. 5, Art. 45 (2019). [4] W. Arendt and A. V. Bukhvalov,  Integral representations of resolvents and semigroups ,  6 Forum. Math. , 111–135 (1994). [5] M. Baker and S. Norine,  Riemann–Roch and Abel–Jacobi theory on a ﬁnite graph , Adv.  215 Math. , no. 2, 766–788 (2007). [6] M. Baker and R. Rumely,  Potential Theory and Dynamics on the Berkovich Projective  159 Line , Math. Surv. Monographs, . Amer. Math. Soc., Providence, RI, 2010. [7] M. T. Barlow and R. F. Bass,  Stability of parabolic Harnack inequalities , Trans. Amer.  356 Math. Soc. , no. 4, 1501–1533 (2004). [8] G. Berkolaiko, R. Carlson, S. Fulling, and P. Kuchment,  Quantum Graphs and Their  415 Applications , Contemp. Math. , Amer. Math. Soc., Providence, RI, 2006.  

[9] G. Berkolaiko and P. Kuchment,  Introduction to Quantum Graphs , Amer. Math. Soc., Providence, RI, 2013.

 [10] J. Breuer and M. Keller,  Spectral analysis of certain spherically homogeneous graphs , Oper.  7 Matrices , no. 4, 825–847 (2013).

 [11] J. Breuer and N. Levi,  On the decomposition of the Laplacian on metric graphs , Ann.  22 Henri Poincar´ , no. 2, 499–537 (2020).

 [12] H. Brezis,  Functional Analysis, Sobolev Spaces and Partial Diﬀerential Equations , Uni- versitext, Springer, New York, 2011.

 [13] D. Burago, Yu. Burago, and S. Ivanov,  A Course in Metric Geometry , Graduate Stud.  33 Math. , Amer. Math. Soc., Providence, RI, 2001.

 [14] S. Cardanobile and D. Mugnolo,  Parabolic systems with coupled boundary conditions , J.  247 Diﬀerential Equations , 1229–1248 (2009).

 [15] R. Carlson,  Nonclassical Sturm–Liouville problems and Schr¨ odinger operators on radial  2000 trees , Electr. J. Diﬀerential Equations , no. 71, pp. 1–24 (2000).

 [16] R. Carlson,  Boundary value problems for inﬁnite metric graphs , in [26].

 [17] R. Carlson,  Dirichlet to Neumann maps for inﬁnite quantum graphs , Netw. Heterog. Media 7 , no. 3, 483–501 (2012).

 [18] D. I. Cartwright, P. M. Soardi, and W. Woess,  Martin and end compact i cations for  338 nonlocally ﬁnite graphs , Trans. Amer. Math. Soc. , no 2, 679–693 (1993).

 [19] Y. Colin de Verdi\` ere, N. Torki-Hamza, and F. Truc,  Essential self-adjointness for com- binatorial Schr¨ odinger operators II–metrically non complete graphs , Math. Phys. Anal.  14 Geom. , no. 1, 21–38 (2011).

 [20] T. Coulhon,  Oﬀ-diagonal heat kernel lower bounds without Poincar´ , J. London Math.  68 Soc. (2) , 795–816 (2003).

 [21] D. Cushing, S. Liu, F. M¨ unch, and N. Peyerimhoﬀ,  Curvature calculations for antitrees , in: M. Keller et. al. (Eds.), “Analysis and Geometry on Graphs and Manifolds”, London  461 Math. Soc. Lect. Notes Ser. , Cambridge Univ. Press, 2020.

 [22] D. Damanik, L. Fang, and S. Sukhtaiev,  Zero measure and singular continuous spectra for  21 quantum graphs , Ann. Henri Poincar´ , no. 7, 2167–2191 (2020).  173

 [23] R. Diestel,  Graph Theory , 5th edn., Grad. Texts in Math. , Springer-Verlag, Heidelberg, New York, 2017.

 [24] R. Diestel and D. K¨ uhn,  Graph-theoretical versus topological ends of graphs , J. Combin.  87 Theory, Ser. B , 197–206 (2003).

 [25] J. Dodziuk and L. Karp, Spectral and function theory for combinatorial Laplacians , in:  73 “Geometry of Random Motion” (Ithaca, N.Y., 1987), Contemp. Math. , Amer. Math. Soc., Providence, pp. 25–40 (1988).

 [26] P. Exner, J. P. Keating, P. Kuchment, T. Sunada, and A. Teplyaev,  Analysis on Graphs  77 and Its Applications , Proc. Symp. Pure Math. , Providence, RI, Amer. Math. Soc., 2008.

 [27] P. Exner, A. Kostenko, M. Malamud, and H. Neidhardt,  Spectral theory of inﬁnite quantum  19 graphs , Ann. Henri Poincar´ , no. 11, 3457–3510 (2018).

 [28] M. Folz,  Volume growth and stochastic completeness of graphs , Trans. Amer. Math. Soc. 366 , 2089–2119 (2014).    33

 [29] H. Freudenthal, Uber die Enden topologischer R¨ aume und Gruppen , Math. Z. , 692–713 (1931).

 [30] H. Freudenthal,   Uber die Enden diskreter R¨ aume und Gruppen , Comment. Math. Helv. 17 , 1–38 (1944).

 [31] M. Fukushima, Y. Oshima, and M. Takeda,  Dirichlet Forms and Symmetric Markov Pro- cesses , 2nd edn., De Gruyter, 2010.  243

 [32] R. Geoghegan,  Topological Methods in Group Theory , Grad. Texts in Math. , Springer, 2008.

 [33] A. Georgakopoulos,  Uniqueness of electrical currents in a network of ﬁnite total resistance ,  82 J. London Math. Soc. , 256–272 (2010).  311

 [34] A. Georgakopoulos,  Graph topologies induced by edge lengths , Discrete Math. , no. 15, 1523–1542 (2011).

 [35] A. Georgakopoulos, S. Haeseler, M. Keller, D. Lenz, and R. Wojciechowski,  Graphs of  103 ﬁnite measure , J. Math. Pures Appl. , S1093–S1131 (2015).  

[36] G. Golub and C. F. Van Loan,  Matrix Computations , 4th edn., The Johns Hopkins Uni- versity Press, Baltimore, 2012.

 [37] A. Grigor’yan and J. Masamune,  Parabolicity and stochastic completeness of manifolds in  100 terms of the Green formula , J. Math. Pures Appl. , 607–632 (2013).    157

 [38] R. Halin, Uber unendliche Wege in Graphen , Math. Ann. , 125–137 (1964).

 [39] S. Haeseler, M. Keller, D. Lenz, and R. Wojciechowski,  Laplacians on inﬁnite graphs:  2 Dirichlet and Neumann boundary conditions , J. Spectr. Theory , no. 4, 397–432 (2012).

 [40] S. Haeseler, Analysis of Dirichlet forms on graphs , PhD thesis, Jena, 2014; arXiv:1705.06322 (2017).

 [41] M. Hinz and M. Schwarz, A note on Neumann problems on graphs , preprint, arXiv:1803.08559 (2018).

 [42] H. Hopf,  Enden oﬀener R¨ aume und unendliche diskontinuierliche Gruppen , Comment.  16 Math. Helv. , 81–100 (1943).

 [43] B. Hua,  Liouville theorem for bounded harmonic functions on manifolds and graphs sat- isfying non-negative curvature dimension condition , Calc. Var. Partial Diﬀerential Equa-  58 tions , no. 2, Art. 42 (2019).

 [44] B. Hua and M. Keller,  Harmonic functions of general graph Laplacians , Calc. Var. Partial  51 Diﬀerential Equations , 343–362 (2014).

 [45] X. Huang, M. Keller, J. Masamune, and R. Wojciechowski,  A note on self-adjoint exten-  265 sions of the Laplacian on weighted graphs , J. Funct. Anal. , 1556–1578 (2013).

 [46] P. Jorgensen and E. Pearse,  Gel’fand triples and boundaries of inﬁnite networks , New  17 York J. Math. , 745–781 (2011).

 [47] U. Kant, T. Klauß, J. Voigt, and M. Weber,  Dirichlet forms for singular one-dimensional  9 operators and on graphs , J. Evol. Equ. , 637–659 (2009).  26

 [48] A. Kasue,  Convergence of metric graphs and energy forms , Rev. Mat. Iberoam. , no. 2, 367–448 (2010).

 [49] A. Kasue,  Convergence of Dirichlet forms induced on boundaries of transient networks ,  47 Potential Anal. , no. 2, 189–233 (2017).

 [50] T. Kato,  Perturbation Theory for Linear Operators , 2nd ed., Springer-Verlag, Berlin-New York, 1976.

 [51] M. Keller and D. Lenz,  Dirichlet forms and stochastic completeness of graphs and sub-  666 graphs , J. reine angew. Math. , 189–223 (2012).

 [52] M. Keller, D. Lenz, M. Schmidt, and M. Schwarz,  Boundary representation of Dirichlet  126 forms on discrete spaces , J. Math. Pures Appl. , 109–143 (2019).

 [53] M. Keller, D. Lenz, M. Schmidt, and R. K. Wojciechowski,  Note on uniformly transient  33 graphs , Rev. Mat. Iberoam. , no. 3, 831–860 (2017).

 [54] M. Keller, D. Lenz, and R. K. Wojciechowski,  Volume growth, spectrum and stochastic  274 completeness of inﬁnite graphs , Math. Z. , no. 3-4, 905–932 (2013).

 [55] A. Kostenko and N. Nicolussi,  Spectral estimates for inﬁnite quantum graphs , Calc. Var.  58 Partial Diﬀerential Equations , no. 1, Art. 15 (2019).

 [56] A. Kostenko and N. Nicolussi,  Quantum graphs on radially symmetric antitrees , J. Spectral  11 Theory , no. 2, 411–460 (2021).

 [57] V. Kostrykin, J. Potthoﬀ, and R. Schrader,  Contraction semigroups on metric graphs , in [26].

 [58] T. Lupu,  From loop clusters and random interlacements to the free ﬁeld , Ann. Probab. 44 , 2117–2146 (2016).

 [59] T. Lupu,  Convergence of the two-dimensional random walk loop-soup clusters to CLE , J.  21 Eur. Math. Soc. , 1201–1227 (2019).

 [60] J. T. Marti,  Evaluation of the least constant in Sobolev’s inequality for    $H^{1}(0,s)$  , SIAM J.  20 Numer. Anal. , 1239–1242 (1983).

 [61] J. Masamune,  Essential self-adjointness of Laplacians on Riemannian manifolds with  24 fractal boundary , Commun. Partial Diﬀ. Equ. , no. 3-4, 749–757 (1999).

 [62] J. Masamune,  Analysis of the Laplacian of an incomplete manifold with almost polar  25 boundary , Rend. Mat. Appl. (7) , no. 1, 109–126 (2005).

 [63] D. Mugnolo and R. Nittka,  Properties of representations of operators acting between spaces  15 of vector-valued functions , Positivity , 135–154 (2011).

 [64] A. Murakami and M. Yamasaki,  An introduction of Kuramochi boundary of an inﬁnite  30 network , Mem. Fac. Sci. Eng. Shimane Univ. Ser. B Math. Sci. , 57–89, 1997.  

[65] N. Nicolussi,  Strong isoperimetric inequality for tessellating quantum graphs , in: F. Fatih- can et. al. (Eds.), “Discrete and Continuous Models in the Theory of Networks”, 271–290,  64 Oper. Theory: Adv. Appl. , Birkh¨ auser, Basel, 2020. [66] E. M. Ouhabaz,  Analysis of Heat Equations on Domains , Princeton Univ. Press, Princeton and Oxford, 2005.  2039 [67] O. Post,  Spectral Analysis on Graph-Like Spaces , Lect. Notes in Math. , Springer- Verlag, Berlin, Heidelberg, 2012 [68] F. S. Rofe-Beketov,  Self-adjoint extensions of diﬀerential operators in a space of vector-  8 valued functions , Teor. Funkcii, Funkcional. Anal. i Priloˇ zen. , 3–24 (1969). (in Russian) [69] K. Schm¨ udgen,  Unbounded Self-Adjoint Operators on Hilbert Space , Grad. Texts in Math. 265 , Springer, Berlin, 2012. [70] F. Shokrieh and C. Wu,  Canonical measures on metric graphs and a Kazhdan’s theorem ,  215 Invent. Math. , 819–862 (2019).  1590 [71] P. M. Soardi,  Potential Theory on Inﬁnite Networks , Lect. Notes Math. , Springer, Berlin, 1994. [72] M. Solomyak,  On the spectrum of the Laplacian on regular metric trees , Waves Random  14 Media , S155–S171 (2004). [73] J. R. Stallings,  Group Theory and Three-Dimensional Manifolds , Yale Univ. Press, New Haven, Connecticut, 1971. [74] K.-T. Sturm,  Analysis on local Dirichlet spaces I. Recurrence, conservative ness and    $L^{p}$  -  456 Liouville properties , J. reine angew. Math. , 173–196 (1994).  86 [75] C. T. C. Wall,  Poincar´ e complexes: I , Ann. of Math. , no. 2, 213–245 (1967). [76] W. Woess,  Random Walks on Inﬁnite Graphs and Groups , Cambridge Univ. Press, Cam- bridge, 2000. [77] R. K. Wojciechowski,  Stochastically incomplete manifolds and graphs , in: D. Lenz et  64 al. (Eds.), “Random Walks, Boundaries and Spectra”, 163–179, Progr. Probab. , Birkh¨ auser/Springer Basel AG, Basel, 2011. Faculty of Mathematics and Physics, University of Ljubljana, Jadranska ul. 19, 1000 Ljubljana, Slovenia, and Institute for Analysis and Scientific Computing, Vienna Uni- versity of Technology, Wiedner Hauptstraße 8-10/101, 1040 Vienna, Austria Current address : Faculty of Mathematics and Physics, University of Ljubljana, Jadranska ul. 19, 1000 Ljubljana, Slovenia, and Faculty of Mathematics, University of Vienna, Oskar-Morgenstern- Platz 1, 1090 Vienna, Austria Email address :  Aleksey.Kostenko@fmf.uni-lj.si Lehrgebiet Analysis, Fakult¨ at Mathematik und Informatik, FernUniversit¨ at in Ha- gen, Hagen, Germany Email address :  delio.mugnolo@fernuni-hagen.de Faculty of Mathematics, University of Vienna, Oskar-Morgenstern-Platz 1, 1090 Vienna, Austria Email address :  noema.nicolussi@univie.ac.at  