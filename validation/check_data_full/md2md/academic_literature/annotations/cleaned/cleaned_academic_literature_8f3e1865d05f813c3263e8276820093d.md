# QUANTUM COHOMOLOGY AND CREPANT RESOLUTIONS: A CONJECTURE 

TOM COATES AND YONGBIN RUAN

Abstract.We give an expository account of a conjecture, developed by CoatesCorti-Iritani-Tseng and Ruan, which relates the quantum cohomology of a Gorenstein orbifold $\mathcal{X}$ to the quantum cohomology of a crepant resolution $Y$ of $\mathcal{X}$. We explore some consequences of this conjecture, showing that it implies versions of both the Cohomological Crepant Resolution Conjecture and of the Crepant Resolution Conjectures of Ruan and Bryan-Graber. We also give a 'quantized' version of the conjecture, which determines higher-genus Gromov-Witten invariants of $\mathcal{X}$ from those of $Y$.

## 1. Introduction

An orbifold is a space which is locally modelled on quotients of $\mathbb{R}^{n}$ by finite groups. Orbifolds are a natural class of spaces to study. Manifolds and smooth algebraic varieties are orbifolds but spaces of geometric interest, and particularly those obtained by quotient constructions, are often orbifolds rather than varieties or manifolds. Furthermore many geometric operations, including those transformations involved in spacetime topology change [4, treat orbifolds and smooth varieties on an equal footing. In this paper we study the quantum cohomology of orbifolds.

The quantum cohomology of a Kähler orbifold $\mathcal{X}$ is a family of algebras whose structure constants encode certain Gromov-Witten invariants of $\mathcal{X}$. These GromovWitten invariants are interesting from at least three points of view: symplectic topology, as they give invariants of $\mathcal{X}$ as a symplectic orbifold; algebraic geometry, as they give a 'virtual count' of the number of curves in $\mathcal{X}$ which are constrained to pass through various cycles; and physics, as they give rigorous meaning to instanton counting in a model of string theory with spacetime $\mathcal{X} \times \mathbb{R}^{4}$. In what follows we outline a conjecture which describes how the quantum cohomology of a Gorenstein orbifold $\mathcal{X}$ is related to that of a crepant resolution $Y$ of $\mathcal{X}$, and explore some of its consequences. The conjecture is of interest also from at least three points of view: Gromov-Witten invariants of orbifolds are difficult to compute, and the conjecture provides tools for doing this; crepant resolutions are simple examples of birational transformations, and an understanding of how quantum cohomology changes under birational transformations would be both interesting and useful; and the conjecture provides a version of the McKay Correspondence which reflects a well-known physical principle - that string theory on an orbifold and on a crepant resolution of that orbifold should be equivalent.

The conjecture, which is described in more detail in §4 below, was developed by Coates-Corti-Iritani-Tseng [13] and Ruan [33]. Following Givental, we encode all genus-zero Gromov-Witten invariants of $\mathcal{X}$ in the germ $\mathcal{L}_{\mathcal{X}}$ of a Lagrangian submanifold in a symplectic vector space $\mathcal{H}_{\mathcal{X}}$. This submanifold-germ $\mathcal{L}_{\mathcal{X}}$ has very special geometric properties (theorem 3.2below) which make it easy to determine the quantum cohomology of $\mathcal{X}$ from $\mathcal{L}_{\mathcal{X}}$ ( $\S 6$ below). A similar submanifold-germ $\mathcal{L}_{Y} \subset \mathcal{H}_{Y}$ encodes all genus-zero Gromov-Witten invariants of the crepant resolution $Y$. As $\mathcal{L}_{\mathcal{X}}$ and $\mathcal{L}_{Y}$ are germs of submanifolds, it makes sense to analytically continue them. We conjecture that there is a linear symplectic isomorphism $\mathbb{U}: \mathcal{H}_{\mathcal{X}} \rightarrow \mathcal{H}_{Y}$ such that after analytic continuation of $\mathcal{L}_{\mathcal{X}}$ and $\mathcal{L}_{Y}$ we have $\mathbb{U}\left(\mathcal{L}_{\mathcal{X}}\right)=\mathcal{L}_{Y}$. This gives, in particular, a conjectural relationship between the quantum cohomology of $\mathcal{X}$ and the quantum cohomology of $Y$.

The idea that the quantum cohomology of $\mathcal{X}$ should be in some sense equivalent to the quantum cohomology of $Y$ has been around for a while now, and is due to Ruan. He originally conjectured that the small quantum cohomology of $\mathcal{X}$ and the small quantum cohomology of $Y$ - two families of algebras which depend on so-called quantum parameters - become isomorphic after specializing some of the quantum parameters to particular values. This specialization may first require analytic continuation in the quantum parameters. Ruan's conjecture is discussed further and revised in $\$ 8$ and $\$ 11$ below. Bryan and Graber [7 recently proposed a refinement of Ruan's conjecture, applicable whenever $\mathcal{X}$ satisfies a Hard Lefschetz condition on orbifold cohomology [13]. They suggest that in this case the big quantum cohomology algebras of $\mathcal{X}$ and $Y$ coincide after analytic continuation and specialization of quantum parameters, via a linear isomorphism that also matches certain pairings on the algebras.

As we explain in $\S 88 \sqrt{9}$ below, under appropriate conditions on $\mathcal{X}$ our conjecture implies something very like the earlier conjectures of Ruan and Bryan-Graber. Our conjecture applies, however, in much greater generality. This fits with a general picture developed by Givental: that the submanifold-germ $\mathcal{L}_{\mathcal{X}}$ often transforms in a simple way under geometric operations on $\mathcal{X}$, even when those operations have a complicated effect on quantum cohomology. Our conjecture also fits well with Givental's approach to mirror symmetry. This was the essential point in the proof [13] of the conjecture for $\mathcal{X}=\mathbb{P}(1,1,2)$ and $\mathcal{X}=\mathbb{P}(1,1,1,3)$. Forthcoming work by Coates, Corti, Iritani, and Tseng will extend this line of argument, using mirror symmetry to prove our conjecture for crepant resolutions of toric orbifolds $\mathcal{X}$ such that $c_{1}(\mathcal{X}) \geq 0$.

An outline of the paper is as follows. We give introductions to the cohomology and quantum cohomology of orbifolds in $\$ 2$, and to Givental's framework in 93 We state the conjecture in 84. After giving some preparatory lemmas (\$55), we explain in $\$ 6$ how to extract quantum cohomology from the submanifold $\mathcal{L}_{\mathcal{X}}$. This allows us to draw conclusions about quantum cohomology from our conjecture. We do this in the next three sections, proving something like the Cohomological Crepant Resolution Conjecture in 87 , something like Ruan's conjecture in $\$ 8$ and something like the Bryan-Graber conjecture in 99 , We close by discussing a higher-genus version of the conjecture ( $\$ 10)$ and the role of flat gerbes ( $\$ 11)$.

We should emphasize that most of what follows is a new presentation of ideas and methods which are already in the literature; in particular we draw the reader's attention to [5, 13, 22, 32]. But we feel that these ideas are important enough to deserve a clear and accessible expository account. The main purpose of this article is to give such an account: we are, of course, entirely responsible for any mistakes or obscurities that it contains.

Acknowledgements. Both authors are very grateful to Hiroshi Iritani: most of the results in this paper we either learned from him or developed in conversations with him. We would have preferred that he join us as author of this note, but must respect his wishes in this regard. T.C. thanks Jim Bryan, Alessio Corti, Alexander Givental, and Hsian-Hua Tseng for useful discussions; and the Royal Society and the Clay Mathematics Institute for financial support. Y.R. thanks Paul Aspinwall for useful discussions. This work was partially supported by the National Science Foundation under grants DMS-0401275 and DMS-0072282.

## 2. Orbifold Cohomology and Quantum Cohomology

In this section we describe and fix notation for orbifold cohomology, GromovWitten invariants, and quantum cohomology. The non-expert reader should be able to follow the rest of the paper after reading the summary of these topics below; detailed accounts of the theory can be found in the work of Chen-Ruan [9, 10] and Abramovich-Graber-Vistoli [2]3]. We work in the algebraic category, so from now on 'orbifold' means 'smooth Deligne-Mumford stack over $\mathbb{C}$ ' and 'manifold' means 'smooth variety'.

Let $\mathcal{Z}$ be an orbifold. The Chen-Ruan orbifold cohomology $H_{\mathrm{CR}}^{\bullet}(\mathcal{Z} ; \mathbb{C})$ is the cohomology of the so-called inertia stack of $\mathcal{Z}$. If $\mathcal{Z}$ is a manifold then $H_{\mathrm{CR}}^{\bullet}(\mathcal{Z} ; \mathbb{C})$ is canonically isomorphic to the ordinary cohomology $H^{\bullet}(\mathcal{Z} ; \mathbb{C})$ and so a ChenRuan cohomology class can be represented, via Poincaré duality, as a cycle in $\mathcal{Z}$. In general a Chen-Ruan class can be represented as a linear combination of pairs $\left(A,\left[g_{A}\right]\right)$ where $A \subset \mathcal{Z}$ is a connected cycle and $\left[g_{A}\right]$ is a conjugacy class in the isotropy group of the generic point of $A$. Chen-Ruan cohomology contains ordinary cohomology as a subspace, represented by those decorated cycles $\left(A,\left[g_{A}\right]\right)$ where $g_{A}$ is the identity element; if $\mathcal{Z}$ is a manifold then this subspace is the whole of $H_{\mathrm{CR}}^{\bullet}(\mathcal{Z} ; \mathbb{C})$. The complementary subspace in $H_{\mathrm{CR}}^{\bullet}(\mathcal{Z} ; \mathbb{C})$ spanned by those decorated cycles $\left(A,\left[g_{A}\right]\right)$ such that $g_{A}$ is not the identity is called the twisted sector. ChenRuan cohomology carries a non-degenerate pairing, the orbifold Poincaré pairing, which functions exactly as the usual Poincaré pairing except that classes represented by $\left(A,\left[g_{A}\right]\right)$ and $\left(B,\left[g_{B}\right]\right)$ pair to zero unless $\left[g_{A}\right]=\left[g_{B}^{-1}\right]$.

In what follows we will consider maps $f: \mathcal{C} \rightarrow \mathcal{Z}$ from orbifold curves to $\mathcal{Z}$. The source curve $\mathcal{C}$ here may be nodal, and carries a number of marked points. We allow $\mathcal{C}$ to have isotropy at the marked points and nodes, but nowhere else, and insist that the map $f$ is representable: that it induces injections on all isotropy groups. (In particular, therefore, if $\mathcal{Z}$ is a manifold then we consider only maps $f: \mathcal{C} \rightarrow \mathcal{Z}$ from curves with trivial orbifold structure.) We take the degree of the map $f: \mathcal{C} \rightarrow \mathcal{Z}$ to be the degree of the corresponding map between coarse moduli spaces [25]. This means the following. Let $C$ and $Z$ be the coarse moduli spaces of $\mathcal{C}$ and $\mathcal{Z}$ respectively, and let $\bar{f}: C \rightarrow Z$ be the map induced by $f$. Consider the free part

$$
H_{2}(Z ; \mathbb{Z})_{\text {free }}=H_{2}(Z ; \mathbb{Z}) / H_{2}(Z ; \mathbb{Z})_{\text {tors }}
$$

of $H_{2}(Z ; \mathbb{Z})$; here $H_{2}(Z ; \mathbb{Z})_{\text {tors }}$ is the torsion subgroup of $H_{2}(Z ; \mathbb{Z})$. The degree $d$ of $f: \mathcal{C} \rightarrow \mathcal{Z}, d \in H_{2}(Z ; \mathbb{Z})_{\text {free }}$, is defined to be the equivalence class of $\bar{\star}_{\star}[C]$ where $[C]$ is the fundamental class of $C$.

We use correlator notation for the Gromov-Witten invariants of the orbifold $\mathcal{Z}$, writing

$$
\left\langle\delta_{1} \psi^{a_{1}}, \ldots, \delta_{n} \psi^{a_{n}}\right\rangle_{g, n, d}^{\mathcal{Z}}=\left\langle\tau_{a_{1}}\left(\delta_{1}\right), \ldots, \tau_{a_{n}}\left(\delta_{n}\right)\right\rangle_{g, d}
$$

where $\delta_{1}, \ldots, \delta_{n}$ are Chen-Ruan cohomology classes on $\mathcal{Z} ; a_{1}, \ldots, a_{n}$ are nonnegative integers; and the right-hand side is defined as on page 41 of [3]. If $\mathcal{Z}$ is a manifold; $a_{1}=\cdots=a_{n}=0$; and a very restrictive set of transversality assumptions hold then (1) gives the number of smooth $n$-pointed curves in $\mathcal{Z}$ of degree $d$ and genus $g$ which are incident at the $i$ th marked point, $1 \leq i \leq n$, to a chosen generic cycle Poincaré-dual to $\delta_{i}$ (see [19]). In general, one should interpret (1) as the 'virtual number' of possibly-nodal $n$-pointed orbifold curves in $\mathcal{Z}$ of genus $g$ and degree $d$ which are incident to chosen cycles as above. If any of the $a_{i}$ are non-zero then we count only curves which in addition satisfy certain constraints on their complex structure. If $\mathcal{Z}$ is an orbifold but not a manifold then, as discussed above, the curves we count are themselves allowed to be orbifolds; the orbifold structure at the $i$ th marked point of the curve is determined by the conjugacy class $\left[g_{i}\right]$ in a representative $\left(A_{i},\left[g_{i}\right]\right)$ of $\delta_{i}$. We write $\operatorname{Eff}(\mathcal{Z})$ for the set of possible degrees $d$ in (11), or in other words for the set of degrees of effective orbifold curves in $\mathcal{Z}$.

Henceforth let $\mathcal{X}$ be a Gorenstein orbifold with projective coarse moduli space $X$, and let $\pi: Y \rightarrow X$ be a crepant resolution. Assume that the isotropy group of the generic point of $\mathcal{X}$ is trivial. The cohomology and homology groups $H^{\bullet}(\mathcal{X} ; \mathbb{Q})$, $H_{\bullet}(\mathcal{X} ; \mathbb{Q})$ are canonically isomorphic to $H_{\bullet}(X ; \mathbb{Q})$ and $H_{\bullet}(X ; \mathbb{Q})$ respectively. The maps

$$
\pi^{\star}: H^{\bullet}(\mathcal{X} ; \mathbb{Q}) \rightarrow H^{\bullet}(Y ; \mathbb{Q}), \quad \pi_{\star}: H_{\bullet}(Y ; \mathbb{Q}) \rightarrow H_{\bullet}(\mathcal{X} ; \mathbb{Q})
$$

are respectively injective [6] and surjective, and there is a 'wrong-way' map

$$
\pi_{!}: H^{\bullet}(Y ; \mathbb{Q}) \rightarrow H^{\bullet}(\mathcal{X} ; \mathbb{Q})
$$

defined using Poincaré duality. We refer to elements of ker $\pi_{\text {! }}^{\text {as }}$ exceptional classes. For an orbifold $\mathcal{Z}$, we say that a basis for $H_{2}(Z ; \mathbb{Z})_{\text {free }}$ is positive if the degree of any map $f: \mathcal{C} \rightarrow \mathcal{Z}$ from an orbifold curve is a non-negative linear combination of basis elements. Let us fix bases for homology, cohomology, and orbifold cohomology as follows. Let $\beta_{1}, \ldots, \beta_{r}$ be a positive basis for $H_{2}(Y ; \mathbb{Z})_{\text {free }}$ such that

$\pi_{\star} \beta_{1}, \ldots, \pi_{\star} \beta_{s}$ is a positive basis for $H_{2}(X ; \mathbb{Z})_{\text {free }}$,

$\beta_{s+1}, \ldots, \beta_{r}$ is a basis for $\operatorname{ker} \pi_{\star} \subset H_{2}(Y ; \mathbb{Z})_{\text {free }}$.

Choose homogeneous bases $\varphi_{0}, \ldots, \varphi_{N}$ for $H^{\bullet}(Y ; \mathbb{Q})$ and $\phi_{0}, \ldots, \phi_{N}$ for $H_{\mathrm{CR}}^{\bullet}(\mathcal{X} ; \mathbb{Q})$ such that

$$
\begin{aligned}
& \varphi_{0}=\mathbf{1}_{Y}, \text { the identity element in } H^{\bullet}(Y ; \mathbb{Q}) ; \\
& \varphi_{1}, \ldots, \varphi_{r} \text { is the basis for } H^{2}(Y ; \mathbb{Q}) \text { dual to } \beta_{1}, \ldots, \beta_{r} ; \\
& \phi_{0}=\mathbf{1}_{\mathcal{X}}, \text { the identity element in } H^{0}(\mathcal{X} ; \mathbb{Q}) ; \\
& \phi_{1}, \ldots, \phi_{s} \text { is the basis for } H^{2}(\mathcal{X} ; \mathbb{Q}) \text { dual to } \pi_{\star} \beta_{1}, \ldots, \pi_{\star} \beta_{s} ; \\
& \phi_{1}, \ldots, \phi_{r} \text { is a basis for } H_{\mathrm{CR}}^{2}(\mathcal{X} ; \mathbb{Q})
\end{aligned}
$$

Note that $\varphi_{i}=\pi^{\star}\left(\phi_{i}\right), 1 \leq i \leq s$. Let $\varphi^{0}, \ldots, \varphi^{N}$ be the basis for $H^{\bullet}(Y ; \mathbb{C})$ which is dual to $\varphi_{0}, \ldots, \varphi_{N}$ under the Poincaré pairing $(\cdot, \cdot)_{Y}$, and let $\phi^{0}, \ldots, \phi^{N}$ be the basis for $H_{\mathrm{CR}}^{\bullet}(\mathcal{X} ; \mathbb{C})$ which is dual to $\phi_{0}, \ldots, \phi_{N}$ under the orbifold Poincaré pairing $(\cdot, \cdot)_{\mathcal{X}}$. We will use Einstein's summation convention for Greek indices, summing repeated Greek (but not Roman) indices over the range $0,1, \ldots, N$. For $d \in \operatorname{Eff}(Y)$, let

$$
Q^{d}=Q_{1}^{d_{1}} Q_{2}^{d_{2}} \cdots Q_{r}^{d_{r}} \quad \text { where } \quad d=d_{1} \beta_{1}+\cdots+d_{r} \beta_{r}
$$

and for $d \in \operatorname{Eff}(\mathcal{X})$, let

$$
U^{d}=U_{1}^{d_{1}} U_{2}^{d_{2}} \cdots U_{s}^{d_{s}} \quad \text { where } \quad d=d_{1} \pi_{\star} \beta_{1}+\cdots+d_{s} \pi_{\star} \beta_{s}
$$

The monomial $Q^{d}$ is an element of the Novikov ring for $Y, \Lambda_{Y}=\mathbb{C} \llbracket Q_{1}, \ldots, Q_{r} \rrbracket$; the monomial $U^{d}$ is an element of the Novikov ring for $\mathcal{X}, \Lambda_{\mathcal{X}}=\mathbb{C} \llbracket U_{1}, \ldots, U_{s} \rrbracket$.

The big quantum product for $\mathcal{X}$ is a family $\star$ of algebra structures on $H_{\mathrm{CR}}^{\bullet}\left(\mathcal{X} ; \Lambda_{\mathcal{X}}\right)$, parameterized by $\tau \in H_{\mathrm{CR}}^{\bullet}\left(\mathcal{X} ; \Lambda_{\mathcal{X}}\right)$, which is defined in terms of Gromov-Witten invariants of $\mathcal{X}$. Let $\tau=\tau_{\alpha} \phi_{\alpha}$, and consider the genus-zero Gromov-Witten potential for $\mathcal{X}$,

$$
\begin{aligned}
F_{\mathcal{X}} & =\sum_{d \in \operatorname{Eff}(\mathcal{X})} \sum_{n \geq 0}\langle\tau, \tau, \ldots, \tau\rangle_{0, n, d}^{\mathcal{X}} \frac{U^{d}}{n!} \\
& =\sum_{\substack{d \in \operatorname{Eff}(\mathcal{X}): \\
d=d_{1} \pi_{*} \beta_{1}+\cdots+d_{s} \pi_{*} \beta_{s}}} \sum_{n \geq 0}\left\langle\phi_{\epsilon_{1}}, \ldots, \phi_{\epsilon_{n}}\right\rangle_{0, n, d}^{\mathcal{X}} \frac{U_{1}^{d_{1}} \cdots U_{s}^{d_{s}} \tau_{\epsilon_{1}} \cdots \tau_{\epsilon_{n}}}{n!}
\end{aligned}
$$

(Recall that we always sum over repeated Greek indices, such as the $\epsilon_{i}$ here.) The Gromov-Witten potential $F_{\mathcal{X}}$ is a formal power series in the variables $\tau_{0}, \ldots, \tau_{N}$ and $U_{1}, \ldots, U_{s}$; it is a generating function for genus-zero Gromov-Witten invariants of $\mathcal{X}$. The potential $F_{\mathcal{X}}$ determines the big quantum product $\underset{\tau}{\star}$ on $H_{\mathrm{CR}}^{\bullet}\left(\mathcal{X} ; \Lambda_{\mathcal{X}}\right)$ via

$$
\phi_{\alpha} \underset{\tau}{\star} \phi_{\beta}=\frac{\partial^{3} F_{\mathcal{X}}}{\partial \tau_{\alpha} \partial \tau_{\beta} \partial \tau_{\gamma}} \phi^{\gamma}
$$

We can regard the RHS of (3) as a formal power series in $\tau_{0}, \ldots, \tau_{N}$ with coefficients in $H_{\mathrm{CR}}^{\bullet}\left(\mathcal{X} ; \Lambda_{\mathcal{X}}\right)$, and thus $\underset{\tau}{\star}$ gives a family, depending formally on $\tau$, of algebra structures on $H_{\mathrm{CR}}^{\bullet}\left(\mathcal{X} ; \Lambda_{\mathcal{X}}\right)$. Similarly, setting $t=t_{\alpha} \varphi_{\alpha}$, the genus-zero GromovWitten potential for $Y$

$$
\begin{aligned}
F_{Y} & =\sum_{d \in \operatorname{Eff}(Y)} \sum_{n \geq 0}\langle t, t, \ldots, t\rangle_{0, n, d}^{Y} \frac{Q^{d}}{n!} \\
& =\sum_{\substack{d \in \operatorname{Eff}(Y): \\
d=d_{1} \beta_{1}+\cdots+d_{r} \beta_{r}}} \sum_{n \geq 0}\left\langle\varphi_{\epsilon_{1}}, \ldots, \varphi_{\epsilon_{n}}\right\rangle_{0, n, d}^{Y} \frac{Q_{1}^{d_{1}} \cdots Q_{r}^{d_{r}} t_{\epsilon_{1}} \cdots t_{\epsilon_{n}}}{n!}
\end{aligned}
$$

is a formal power series in the variables $t_{0}, \ldots, t_{N}$ and $Q_{1}, \ldots, Q_{r}$. It determines the big quantum product for $Y$, which is a family $\star$ of algebra structures on $H^{\bullet}\left(Y ; \Lambda_{Y}\right)$ depending formally on $t \in H^{\bullet}\left(Y ; \Lambda_{Y}\right)$, via

$$
\varphi_{\alpha} \underset{t}{\star} \varphi_{\beta}=\frac{\partial^{3} F_{Y}}{\partial t_{\alpha} \partial t_{\beta} \partial t_{\gamma}} \varphi^{\gamma}
$$

The small quantum products are algebra structures on $H_{\mathrm{CR}}^{\bullet}\left(\mathcal{X} ; \Lambda_{\mathcal{X}}\right)$ and $H^{\bullet}\left(Y ; \Lambda_{Y}\right)$ obtained from the big quantum products (3) and (5) by setting $\tau=0, t=0$ :

$$
\begin{array}{rlr}
\phi_{\alpha} \bullet \phi_{\beta} & =\sum_{d \in \operatorname{Eff}(\mathcal{X})}\left\langle\phi_{\alpha}, \phi_{\beta}, \phi^{\gamma}\right\rangle_{0,3, d}^{\mathcal{X}} U^{d} \phi_{\gamma} & \text { for } \mathcal{X} \\
\varphi_{\alpha} \bullet \varphi_{\beta} & =\sum_{d \in \operatorname{Eff}(Y)}\left\langle\varphi_{\alpha}, \varphi_{\beta}, \varphi^{\gamma}\right\rangle_{0,3, d}^{Y} Q^{d} \varphi_{\gamma} & \text { for } Y
\end{array}
$$

The variables $U_{1}, \ldots, U_{s}$ and $Q_{1}, \ldots, Q_{r}$ hidden here are the 'quantum parameters' described in the introduction. Setting $Q_{1}=\cdots=Q_{r}=0$ in (6) recovers the usual cup product on $H \bullet(Y ; \mathbb{C})$; setting $U_{1}=\cdots=U_{s}=0$ gives the Chen-Ruan product on $H_{\mathrm{CR}}^{\bullet}(\mathcal{X} ; \mathbb{C})$, which we denote by $\cup_{\mathrm{CR}}$. Unless otherwise indicated, all products of Chen-Ruan cohomology classes are taken using $\underset{\mathrm{CR}}{\cup}$.

It follows from the Divisor Equation (see e.g. [7]) that $\phi_{\alpha} \underset{\tau}{\star} \phi_{\beta}$ depends on the variables $\tau_{1}, \ldots, \tau_{s}, U_{1}, \ldots, U_{s}$ only through the combinations $U_{i} \mathrm{e}^{t_{i}}, 1 \leq i \leq s$, and that $\varphi_{\alpha}{ }_{t}^{\star} \varphi_{\beta}$ depends on the variables $t_{1}, \ldots, t_{r}, Q_{1}, \ldots, Q_{r}$ only through the combinations $Q_{i} \mathrm{e}^{t_{i}}, 1 \leq i \leq r$. Set

$$
\begin{array}{ll}
\tau_{\mathrm{two}}=\tau_{1} \phi_{1}+\cdots+\tau_{s} \phi_{s}, & \tau_{\text {rest }}=\tau_{0} \phi_{0}+\tau_{s+1} \phi_{s+1}+\cdots+\tau_{N} \phi_{N} \\
t_{\mathrm{two}}=t_{1} \varphi_{1}+\cdots+t_{r} \varphi_{r}, & t_{\text {rest }}=t_{0} \varphi_{0}+t_{r+1} \varphi_{r+1}+\cdots+t_{N} \varphi_{N}
\end{array}
$$

so that $\tau=\tau_{\text {two }}+\tau_{\text {rest }}$ and $t=t_{\text {two }}+t_{\text {rest }}$. Then

$$
\begin{aligned}
& \phi_{\alpha} \star \phi_{\tau}=\sum_{\substack{d \in \operatorname{Eff}(\mathcal{X}): \\
d=d_{1} \pi_{\star} \beta_{1}+\cdots+d_{s} \pi_{\star} \beta_{s}}} \sum_{n \geq 0}\left\langle\phi_{\alpha}, \phi_{\beta}, \tau_{\text {rest }}, \ldots, \tau_{\text {rest }}, \phi^{\gamma}\right\rangle_{0, n+3, d}^{\mathcal{X}} \\
& \times \frac{U_{1}^{d_{1}} \cdots U_{s}^{d_{s}} \mathrm{e}^{d_{1} \tau_{1}} \cdots \mathrm{e}^{d_{s} \tau_{s}}}{n!} \phi_{\gamma}
\end{aligned}
$$

and

(9) $\varphi_{\alpha}^{\star} \varphi_{\beta}=\sum_{\substack{d \in \operatorname{Eff}(Y): \\ d=d_{1} \beta_{1}+\cdots+d_{r} \beta_{r}}} \sum_{n \geq 0}\left\langle\varphi_{\alpha}, \varphi_{\beta}, t_{\text {rest }}, \ldots, t_{\text {rest }}, \varphi^{\gamma}\right\rangle_{0, n+3, d}^{Y}$

$$
\times \frac{Q_{1}^{d_{1}} \cdots Q_{r}^{d_{r}} \mathrm{e}^{d_{1} t_{1}} \cdots \mathrm{e}^{d_{r} t_{r}}}{n!} \varphi_{\gamma}
$$

Thus in the limit

$$
\begin{aligned}
\operatorname{Re} \tau_{i} & \rightarrow-\infty, & & 1 \leq i \leq s \\
\tau_{i} & \rightarrow 0, & & i=0 \text { and } s<i \leq N
\end{aligned}
$$

the big quantum product $\underset{\tau}{\star}$ on $H_{\mathrm{CR}}^{\bullet}\left(\mathcal{X} ; \Lambda_{\mathcal{X}}\right)$ becomes the Chen-Ruan product, and in the limit

$$
\begin{array}{cl}
\operatorname{Re} t_{i} \rightarrow-\infty, & 1 \leq i \leq r \\
t_{i} \rightarrow 0, & i=0 \text { and } r<i \leq N
\end{array}
$$

the big quantum product $\underset{t}{\star}$ on $H^{\bullet}\left(Y ; \Lambda_{Y}\right)$ becomes the usual cup product. We refer to the points

$$
\tau_{i}=\left\{\begin{array}{ll}
-\infty & 1 \leq i \leq s \\
0 & \text { otherwise }
\end{array} \quad \text { and } \quad t_{i}= \begin{cases}-\infty & 1 \leq i \leq r \\
0 & \text { otherwise }\end{cases}\right.
$$

as the large-radius limit points for $\mathcal{X}$ and $Y$ respectively.

An Analyticity Assumption and Its Consequences. The goal of this paper is to describe a relationship between the big quantum products on $H_{\mathrm{CR}}^{\bullet}\left(\mathcal{X} ; \Lambda_{\mathcal{X}}\right)$ and $H^{\bullet}\left(Y ; \Lambda_{Y}\right)$. The first obstacle to overcome is that the ground rings $\Lambda_{\mathcal{X}}$ and $\Lambda_{Y}$ are in general not isomorphic: $\Lambda_{Y}$ contains more quantum parameters $\left(Q_{i}: 1 \leq i \leq r\right)$ than $\Lambda_{\mathcal{X}}$ does $\left(U_{i}: 1 \leq i \leq s\right)$. We now describe an analyticity assumption on the big quantum product $\underset{t}{\star}$ for $Y$ which allows us to regard $\underset{t}{\star}$ as a family of algebra structures on $H^{\bullet}\left(Y ; \Lambda_{\mathcal{X}}\right)$ : it allows us to set $Q_{i}=U_{i}, 1 \leq i \leq s$, and to specialize the extra quantum parameters $Q_{s+1}, \ldots, Q_{r}$ to 1 . Roughly speaking, we assume henceforth that the genus-zero Gromov-Witten potential $F_{Y}$, which is a formal power series in the variables $t_{0}, \ldots, t_{N}$ and $Q_{1}, \ldots, Q_{r}$, is convergent in the 'exceptional variables' $Q_{s+1}, \ldots, Q_{r}$.

Definition. Let $F \in \mathbb{C} \llbracket x_{0}, x_{1}, x_{2}, \ldots \rrbracket$ be a formal power series in the variables $x_{0}, x_{1}, x_{2}, \ldots$ Given distinct variables $x_{i_{1}}, \ldots, x_{i_{n}}$ we can write $F$ uniquely in the form

$$
F=\sum_{J \subset \mathbb{N} \backslash\left\{i_{1}, \ldots, i_{n}\right\}} \sum_{a: J \rightarrow \mathbb{N} \backslash\{0\}} \mathfrak{f}_{J, a} \prod_{j \in J} x_{j}^{a(j)}
$$

where each $\mathfrak{f}_{J, a}$ is a formal power series in the variables $x_{i_{1}}, \ldots, x_{i_{n}}$. Let $D$ be a domain in $\mathbb{C}^{n}$ which contains the origin. We say that $F$ depends analytically on $x_{i_{1}}, \ldots, x_{i_{n}}$ in the domain $D$ if each $\mathfrak{f}_{J, a}$ is the Taylor expansion at the origin of $f_{J, a}\left(x_{i_{1}}, \ldots, x_{i_{n}}\right)$ for some analytic function $f_{J, a}: D \rightarrow \mathbb{C}$.

The genus-zero Gromov-Witten potential $F_{Y}$ is a formal power series in the variables $t_{0}, \ldots, t_{N}$ and $Q_{1}, \ldots, Q_{r}$. Henceforth, we impose:

Convergence Assumption 2.1. There are strictly positive real numbers $R_{i}, s<$ $i \leq r$, such that $F_{Y}$ depends analytically on $Q_{s+1}, \ldots, Q_{r}$ in the domain

$$
\left|Q_{i}\right|<R_{i}, \quad s<i \leq r
$$

This assumption holds, for instance, whenever $Y$ is a compact semi-positive toric manifold. As we will see, even though the radii of convergence $R_{i}$ need not all be greater than 1 , this assumption will allow us to set $Q_{s+1}=\cdots=Q_{r}=1$. It follows from (9) that under Convergence Assumption [2.1, $F_{Y}$ in fact depends analytically on $t_{1}, t_{2}, \ldots, t_{r}$ and $Q_{s+1}, \ldots, Q_{r}$ in the domain

$$
\begin{array}{ll}
\left|t_{i}\right|<\infty & 1 \leq i \leq s \\
\left|Q_{i} \mathrm{e}^{t_{i}}\right|<R_{i} & s<i \leq r
\end{array}
$$

Thus we can write $F_{Y}$ as

$$
\sum_{\substack{J \subset\{0, r+1, r+2, \ldots, N\} \\ K \subset\{1,2, \ldots, s\}}} \sum_{\substack{a: J \rightarrow \mathbb{N} \backslash\{0\} \\ b: K \rightarrow \mathbb{N} \backslash\{0\}}} g_{J, a ; K, b}\left(t_{1}, \ldots, t_{r} ; Q_{s+1}, \ldots, Q_{r}\right) \prod_{j \in J} t_{j}^{a(j)} \prod_{k \in K} Q_{k}^{b(k)}
$$

where $g_{J, a ; K, b}$ are analytic functions defined in the domain (10), and then set

$$
Q_{i}= \begin{cases}U_{i} & 1 \leq i \leq s \\ 1 & s<i \leq r\end{cases}
$$

obtaining a well-defined power series

$$
F_{Y}^{\circledast}=\sum_{\substack{J \subset\{0, r+1, r+2, \ldots, N\} \\ K \subset\{1,2, \ldots, s\}}} \sum_{\substack{a: J \rightarrow \mathbb{N} \backslash\{0\} \\ b: K \rightarrow \mathbb{N}\{0\}}} g_{J, a ; K, b}\left(t_{1}, \ldots, t_{r} ; 1, \ldots, 1\right) \prod_{j \in J} t_{j}^{a(j)} \prod_{k \in K} U_{k}^{b(k)}
$$

in the variables $t_{0}, t_{r+1}, t_{r+2}, \ldots, t_{N}$ and $U_{1}, \ldots, U_{s}$, with coefficients which are analytic functions of $t_{1}, \ldots, t_{r}$ defined in the region

$$
\begin{array}{ll}
\left|t_{i}\right|<\infty & 1 \leq i \leq s \\
\left|\mathrm{e}^{t_{i}}\right|<R_{i} & s<i \leq r
\end{array}
$$

We can also make the substitution (11) in the big quantum product (55), obtaining a well-defined family of products $\underset{t}{\circledast}$ on $H^{\bullet}\left(Y ; \Lambda_{\mathcal{X}}\right)$ which depends formally on the variables $t_{0}, t_{r+1}, t_{r+2}, \ldots, t_{N}$ and analytically on the variables $t_{1}, \ldots, t_{r}$ in the domain (12). The product $\underset{t}{\circledast}$ satisfies

$$
\varphi_{\alpha} \underset{t}{\circledast} \varphi_{\beta}=\frac{\partial^{3} F_{Y}^{\circledast}}{\partial t_{\alpha} \partial t_{\beta} \partial t_{\gamma}} \varphi^{\gamma}
$$

and

$$
\begin{aligned}
& \varphi_{\alpha} \circledast \varphi_{\beta}=\sum_{\substack{d \in \operatorname{Eff}(Y): \\
d=d_{1} \beta_{1}+\cdots+d_{r} \beta_{r}}} \sum_{n \geq 0}\left\langle\varphi_{\alpha}, \varphi_{\beta}, t_{\text {rest }}, \ldots, t_{\text {rest }}, \varphi^{\gamma}\right\rangle_{0, n+3, d}^{Y} \\
& \times \frac{U_{1}^{d_{1}} \cdots U_{s}^{d_{s}} \mathrm{e}^{d_{1} t_{1}} \cdots \mathrm{e}^{d_{r} t_{r}}}{n!} \varphi_{\gamma}
\end{aligned}
$$

where $t_{\text {rest }}$ is defined in (7).

We do not impose any convergence assumption on the Gromov-Witten potential $F_{\mathcal{X}}$, which is a formal power series in $\tau_{0}, \ldots, \tau_{N}$ and $U_{1}, \ldots, U_{s}$, but nonetheless it depends analytically on the variables $\tau_{1}, \ldots, \tau_{s}$ in the domain $\mathbb{C}^{s}$. This is clear from equation (8).

## 3. Givental's Lagrangian Cone

The key objects in conjecture 4.1 are certain Lagrangian submanifold-germs $\mathcal{L}_{\mathcal{X}}$ and $\mathcal{L}_{Y}$. In this section we define $\mathcal{L}_{\mathcal{X}}$ and $\mathcal{L}_{Y}$ and describe some of their properties.

A Symplectic Vector Space. Throughout this section, let $\mathcal{Z}$ denote either $\mathcal{X}$ or $Y$. We work over the ground ring $\Lambda=\Lambda_{\mathcal{X}}$. Let

$$
\begin{aligned}
\mathcal{H}_{\mathcal{Z}} & =H_{\mathrm{CR}}^{\bullet}(\mathcal{Z} ; \Lambda) \otimes \mathbb{C}\left(\left(z^{-1}\right)\right) \\
\Omega_{\mathcal{Z}}(f, g) & =\operatorname{Res}_{z=0}(f(-z), g(z))_{\mathcal{Z}} d z
\end{aligned}
$$

We think of $\mathcal{H}_{\mathcal{Z}}$ as a sort of 'symplectic vector space', but defined over the ring $\Lambda$ rather than over a field. $\mathcal{H}_{\mathcal{Z}}$ is a free graded $\Lambda$-module, where $\operatorname{deg} z=2$, and $\Omega_{\mathcal{Z}}$ is a $\Lambda$-linear, $\Lambda$-valued supersymplectic form on $\mathcal{H}_{\mathcal{Z}}$ :

$$
\Omega_{\mathcal{Z}}\left(\theta_{1} z^{k}, \theta_{2} z^{l}\right)=(-1)^{a_{1} a_{2}+1} \Omega_{\mathcal{Z}}\left(\theta_{2} z^{l}, \theta_{1} z^{k}\right) \quad \text { for } \theta_{i} \in H_{\mathrm{CR}}^{a_{i}}(\mathcal{Z} ; \mathbb{C})
$$

There is a decomposition $\mathcal{H}_{\mathcal{Z}}=\mathcal{H}_{\mathcal{Z}}^{+} \oplus \mathcal{H}_{\mathcal{Z}}^{-}$, where the subspaces

$$
\mathcal{H}_{\mathcal{Z}}^{+}=H_{\mathrm{CR}}^{\bullet}(\mathcal{Z} ; \Lambda) \otimes \mathbb{C}[z] \quad \text { and } \quad \mathcal{H}_{\mathcal{Z}}^{-}=z^{-1} H_{\mathrm{CR}}^{\bullet}(\mathcal{Z} ; \Lambda) \otimes \mathbb{C} \llbracket z^{-1} \rrbracket
$$

are Lagrangian. We can write a general point in $\mathcal{H}_{\mathcal{Z}}$ as

$$
\sum_{k=0}^{\infty} \sum_{a=0}^{N} q_{k, a} \Phi_{a} z^{k}+\sum_{l=0}^{\infty} \sum_{b=0}^{N} p_{l, b} \Phi^{b}(-z)^{-1-l}
$$

where $\Phi_{a}=\phi_{a}$ and $\Phi^{a}=\phi^{a}$ if $\mathcal{Z}=\mathcal{X}$, and $\Phi_{a}=\varphi_{a}$ and $\Phi^{a}=\varphi^{a}$ if $\mathcal{Z}=Y$; this defines $\Lambda$-valued Darboux co-ordinates $\left\{q_{k, a}, p_{l, b}\right\}$ on $\mathcal{H}_{\mathcal{Z}}$, with $q_{k, a}$ dual to $p_{k, a}$. Set $q_{k}=\sum_{a} q_{k, a} \Phi_{a}$, so that $\mathbf{q}(z)=q_{0}+q_{1} z+q_{2} z^{2}+\cdots$ is a general point in $\mathcal{H}_{\mathcal{Z}}^{+}$.

The Genus-Zero Descendant Potentials. We consider now the genus-zero descendant potentials $\mathcal{F}_{\mathcal{X}}^{0}$ and $\mathcal{F}_{\mathcal{Y}}^{0}$, which are generating functions for all genus-zero Gromov-Witten invariants of $\mathcal{X}$ and $Y$. Set $\tau_{a}=\tau_{a, \alpha} \phi_{\alpha}, a=0,1,2, \ldots$ Then

$$
\begin{aligned}
\mathcal{F}_{\mathcal{X}}^{0} & =\sum_{d \in \operatorname{Eff}(\mathcal{X})} \sum_{n \geq 0} \sum_{a_{1}, \ldots, a_{n} \geq 0}\left\langle\tau_{a_{1}} \psi^{a_{1}}, \tau_{a_{2}} \psi^{a_{2}}, \ldots, \tau_{a_{n}} \psi^{a_{n}}\right\rangle_{0, n, d}^{\mathcal{X}} \frac{U^{d}}{n!} \\
& =\sum_{d \in \operatorname{Eff}(\mathcal{X})} \sum_{n \geq 0} \sum_{a_{1}, \ldots, a_{n} \geq 0}\left\langle\phi_{\epsilon_{1}} \psi^{a_{1}}, \ldots, \phi_{\epsilon_{n}} \psi^{a_{n}}\right\rangle_{0, n, d}^{\mathcal{X}} \frac{U_{1}^{d_{1}} \cdots U_{s}^{d_{s}} \tau_{a_{1}, \epsilon_{1}} \cdots \tau_{a_{n}, \epsilon_{n}}}{n!}
\end{aligned}
$$

where $d=d_{1} \pi_{\star} \beta_{1}+\cdots+d_{s} \pi_{\star} \beta_{s}$. The descendant potential $\mathcal{F}_{\mathcal{X}}^{0}$ is a formal power series in the variables $U_{1}, \ldots, U_{s}$ and $\tau_{a, \epsilon}, 0 \leq \epsilon \leq N, 0 \leq a<\infty$. We show in the appendix that $\mathcal{F}_{X}^{0}$ in fact depends analytically on $\tau_{0,1}, \ldots, \tau_{0, s}$ in the domain $\mathbb{C}^{s}$. Similarly, set $t_{a}=t_{a, \alpha} \varphi_{\alpha}, a=0,1,2, \ldots$ Then

$$
\begin{aligned}
\mathcal{F}_{Y}^{0} & =\sum_{d \in \operatorname{Eff}(Y)} \sum_{n \geq 0} \sum_{a_{1}, \ldots, a_{n} \geq 0}\left\langle t_{a_{1}} \psi^{a_{1}}, t_{a_{2}} \psi^{a_{2}}, \ldots, t_{a_{n}} \psi^{a_{n}}\right\rangle_{0, n, d}^{Y} \frac{Q^{d}}{n!} \\
& =\sum_{d \in \operatorname{Eff}(Y)} \sum_{n \geq 0} \sum_{a_{1}, \ldots, a_{n} \geq 0}\left\langle\varphi_{\epsilon_{1}} \psi^{a_{1}}, \ldots, \varphi_{\epsilon_{n}} \psi^{a_{n}}\right\rangle_{0, n, d}^{Y} \frac{Q_{1}^{d_{1}} \cdots Q_{r}^{d_{r}} t_{a_{1}, \epsilon_{1}} \cdots t_{a_{n}, \epsilon_{n}}}{n!}
\end{aligned}
$$

where $d=d_{1} \beta_{1}+\cdots+d_{r} \beta_{r}$. The descendant potential $\mathcal{F}_{Y}^{0}$ is a formal power series in the variables $Q_{1}, \ldots, Q_{r}$ and $t_{a, \epsilon}, 0 \leq \epsilon \leq N, 0 \leq a<\infty$. We will show in the appendix that under convergence assumption [2.1] $\mathcal{F}_{Y}^{0}$ in fact depends analytically on $t_{0,1}, \ldots, t_{0, r}$ and $Q_{s+1}, \ldots, Q_{r}$ in the domain

$$
\begin{array}{ll}
\left|t_{0, i}\right|<\infty & 1 \leq i \leq s \\
\left|Q_{i} \mathrm{e}^{t_{0, i}}\right|<R_{i} & s<i \leq r
\end{array}
$$

This will allow us, as before, to set $Q_{s+1}=\cdots=Q_{r}=1$ : we can write $\mathcal{F}_{Y}^{0}$ as

$$
\begin{array}{cc}
\sum_{\substack{J \subset \mathbb{N} \times\{0,1,2, \ldots, N\}: \\
J \cap\{(0,1),(0,2), \ldots,(0, r)\}=\varnothing}} \sum_{\substack{K \subset\{1,2, \ldots, s\} \\
b: J \rightarrow \mathbb{N} \backslash\{0\} \\
b: K \rightarrow \mathbb{N} \backslash\{0\}}} g_{J, a ; K, b}\left(t_{0,1}, \ldots, t_{0, r} ; Q_{s+1}, \ldots, Q_{r}\right) \\
\times \prod_{(j, e) \in J} t_{j, e}^{a(j, e)} \prod_{k \in K} Q_{k}^{b(k)}
\end{array}
$$

where $g_{J, a ; K, b}$ are analytic functions defined in the domain (17), and making the substitution (11) yields a well-defined power series

$$
\begin{aligned}
& \mathcal{F}_{Y}^{\circledast}=\sum_{\substack{J \subset \mathbb{N} \times\{0,1,2, \ldots, N\}: \\
J \cap\{(0,1),(0,2), \ldots,(0, r)\}=\varnothing}} \sum_{\substack{K \subset\{1,2, \ldots, s\}}} \sum_{\substack{a: J \rightarrow \mathbb{N} \backslash\{0\} \\
b: K \rightarrow \mathbb{N} \backslash\{0\}}} g_{J, a ; K, b}\left(t_{0,1}, \ldots, t_{0, r} ; 1, \ldots, 1\right) \\
& \times \prod_{(j, e) \in J} t_{j, e}^{a(j, e)} \prod_{k \in K} U_{k}^{b(k)}
\end{aligned}
$$

in the variables $t_{0,0} ; t_{0, r+1}, t_{0, r+2}, \ldots, t_{0, N} ; t_{a, \epsilon}, 0 \leq \epsilon \leq N, 1 \leq a<\infty$; and $U_{1}, \ldots, U_{s}$, with coefficients which are analytic functions of $t_{0,1}, \ldots, t_{0, r}$ defined in the domain

$$
\begin{array}{ll}
\left|t_{0, i}\right|<\infty & 1 \leq i \leq s \\
\left|\mathrm{e}^{t_{0, i}}\right|<R_{i} & s<i \leq r
\end{array}
$$

Thus, exactly as before, Convergence Assumption 2.1 allows us to work over the Novikov ring $\Lambda=\Lambda_{\mathcal{X}}$ for $\mathcal{X}$, even when we are thinking about Gromov-Witten invariants of $Y$.

The Definition of $\mathcal{L}_{\mathcal{X}}$ and $\mathcal{L}_{Y}$. We regard the genus-zero descendant potential $\mathcal{F}_{\mathcal{X}}^{0}$ as the germ of a function on $\mathcal{H}_{\mathcal{X}}^{+}$via the identification

$$
q_{k, \alpha}= \begin{cases}\tau_{1,0}-1 & (k, \alpha)=(1,0) \\ \tau_{k, \alpha} & \text { otherwise }\end{cases}
$$

which we abbreviate as $\mathbf{q}(z)=\boldsymbol{\tau}(z)-z$. We regard $\mathcal{F}_{Y}^{\circledast}$ as the germ of a function on $\mathcal{H}_{Y}^{+}$via the identification

$$
q_{k, \alpha}= \begin{cases}t_{1,0}-1 & (k, \alpha)=(1,0) \\ t_{k, \alpha} & \text { otherwise }\end{cases}
$$

which we abbreviate as $\mathbf{q}(z)=\mathbf{t}(z)-z$. The identifications (20) and (21) are examples of the dilaton shift; this is discussed further in [11]. Let $\mathcal{F}_{\mathcal{Z}}=\mathcal{F}_{\mathcal{X}}^{0}$ if $\mathcal{Z}=\mathcal{X}$ and $\mathcal{F}_{\mathcal{Z}}=\mathcal{F}_{Y}^{\circledast}$ if $\mathcal{Z}=Y$. We define $\mathcal{L}_{\mathcal{Z}}$ by the equations

$$
\begin{array}{ll}
p_{k, \alpha}=\frac{\partial \mathcal{F}_{\mathcal{Z}}}{\partial q_{k, \alpha}} & 0 \leq k<\infty \\
& 0 \leq \alpha \leq N
\end{array}
$$

As $\mathcal{F}_{\mathcal{Z}}$ is the germ of a function on $\mathcal{H}_{\mathcal{Z}}^{+}$(depending analytically on some variables and formally on other variables), $\mathcal{L}_{\mathcal{Z}}$ is the germ of a Lagrangian submanifold of $\mathcal{H}_{\mathcal{Z}}$.

Remark 3.1. The polarization $\mathcal{H}_{\mathcal{Z}}=\mathcal{H}_{\mathcal{Z}}^{+} \oplus \mathcal{H}_{\mathcal{Z}}^{-}$ identifies $\mathcal{H}_{\mathcal{Z}}^{-}$ with the $\Lambda$-module $\left(\mathcal{H}_{\mathcal{Z}}^{+}\right)^{\star}:=\operatorname{Hom}\left(\mathcal{H}_{\mathcal{Z}}^{+}, \Lambda\right)$ dual to $\mathcal{H}_{\mathcal{Z}}^{+}$, and hence identifies $\mathcal{H}_{\mathcal{Z}}$ with the cotangent bundle $T^{\star} \mathcal{H}_{\mathcal{Z}}^{+}:=\mathcal{H}_{\mathcal{Z}}^{+} \oplus\left(\mathcal{H}_{\mathcal{Z}}^{+}\right)^{\star}$. Under this identification, $\mathcal{L}_{\mathcal{Z}}$ becomes the graph of the differential of $\mathcal{F}_{\mathcal{Z}}$.

The Gromov-Witten invariants which participate in the definition of $\mathcal{L}_{\mathcal{Z}}$ satisfy a large number of identities: the String Equation, the Dilaton Equation, and the Topological Recursion Relations. These identities place very strong constraints on the geometry of $\mathcal{L}_{\mathcal{Z}}$ :

Theorem $3.2\left([\overline{15}, 22,34) \cdot \mathcal{L}_{\mathcal{Z}}\right.$ is the germ of a Lagrangian cone with vertex at the origin such that each tangent space $T$ to $\mathcal{L}_{\mathcal{Z}}$ is tangent to the cone exactly along $z T$. In other words:

(1) if $T$ is a tangent space to $\mathcal{L}_{\mathcal{Z}}$ then $z T \subset T$;

(2) if $T=T_{x} \mathcal{L}_{\mathcal{Z}}$ then the germ at $x$ of the linear subspace $z T$ is contained in $\mathcal{L}_{\mathcal{Z}}$

(3) if $T$ is a tangent space to $\mathcal{L}_{\mathcal{Z}}$ and $x \in \mathcal{L}_{\mathcal{Z}}$ then $T_{x} \mathcal{L}_{\mathcal{Z}}=T$ if and only if $x \in z T$.

In particular, theorem 3.2 implies that each tangent space $T$ to $\mathcal{L}_{\mathcal{Z}}$ is closed under multiplication by elements of $\mathbb{C}[z]$ (because $z T \subset T$ ), and that $\mathcal{L}_{\mathcal{Z}}$ is the union, over all tangent spaces $T$ to $\mathcal{L}_{\mathcal{Z}}$, of the infinite-dimensional linear subspacegerms $z T \cap \mathcal{L}_{\mathcal{Z}}$. It is the germ of a 'ruled cone'. Note that as $\mathcal{L}_{\mathcal{Z}}$ is the germ of a submanifold of $\mathcal{H}_{\mathcal{Z}}$, it makes sense to analytically continue $\mathcal{L}_{\mathcal{Z}}$.

## 4. The Crepant Resolution Conjecture

We are now in a position to make our conjecture.

Conjecture 4.1 (Coates-Corti-Iritani-Tseng; Ruan). There is a degree-preserving $\mathbb{C}\left(\left(z^{-1}\right)\right)$-linear symplectic isomorphism $\mathbb{U}: \mathcal{H}_{\mathcal{X}} \rightarrow \mathcal{H}_{Y}$ and a choice of analytic continuations of $\mathcal{L}_{\mathcal{X}}$ and $\mathcal{L}_{Y}$ such that $\mathbb{U}\left(\mathcal{L}_{\mathcal{X}}\right)=\mathcal{L}_{Y}$. Furthermore, $\mathbb{U}$ satisfies:

(a) $\mathbb{U}\left(\mathbf{1}_{\mathcal{X}}\right)=\mathbf{1}_{Y}+O\left(z^{-1}\right)$;

(b) $\mathbb{U} \circ\left(\rho \rho_{C R}\right)=\left(\pi^{\star} \rho \cup\right) \circ \mathbb{U}$ for every untwisted degree-two class $\rho \in H^{2}(\mathcal{X} ; \mathbb{C})$;

(c) $\mathbb{U}\left(\mathcal{H}_{\mathcal{X}}^{+}\right) \oplus \mathcal{H}_{Y}^{-}=\mathcal{H}_{Y}$

(d) the matrix entries of $\mathbb{U}$ with respect to the bases $\left\{\phi_{\alpha}\right\}$ and $\left\{\varphi_{\beta}\right\}$, which a priori are elements of $\Lambda\left(\left(z^{-1}\right)\right)$, in fact lie in $\mathbb{C}\left(\left(z^{-1}\right)\right)$.

Remark 4.2. This conjecture emerged in two different contexts during the "New Topological Structures in Physics" program at the Mathematical Sciences Research Institute, Berkeley, in the spring of 2006. Conversations between the authors led to the idea that the relationship between the quantum cohomology of $\mathcal{X}$ and $Y$ should be expressed as the assertion that $\mathbb{U}\left(\mathcal{L}_{\mathcal{X}}\right)=\mathcal{L}_{Y}$ for some $\mathbb{C}\left(\left(z^{-1}\right)\right)$-linear symplectic isomorphism $\mathbb{U}$. At the same time, guided by mirror symmetry, Hiroshi Iritani found such a symplectic transformation in toric examples (as a part of a project [13] with Coates, Corti, and Tseng). Condition (c) here is a stronger version of the condition (c) given in [13, §5]. We will need this stronger version for the Cohomological Crepant Resolution Conjecture below.

Remark 4.3. Variants of conjecture 4.1 apply to the $G$-equivariant quantum cohomology of $G$-equivariant crepant resolutions, and to crepant resolutions of certain non-compact orbifolds (c.f. [7]). We leave the necessary modifications to the reader.

What Do The Conditions Mean? Without condition (a) any non-zero scalar multiple of $\mathbb{U}$ would also satisfy the conjecture, because $\mathcal{L}_{\mathcal{X}}$ and $\mathcal{L}_{Y}$ are germs of cones. The fact that $\mathbb{U}$ is degree-preserving forces $\mathbb{U}\left(\mathbf{1}_{\mathcal{X}}\right)=\lambda \mathbf{1}_{Y}+O\left(z^{-1}\right)$ for some scalar $\lambda$, and so condition (a) just fixes this overall scalar multiple.

Condition (b) is a compatibility of monodromy. The A-model connection - a system of differential equations associated to the small quantum cohomology of $Y$ [16. $\S 8.5]$ - is regular singular along the normal-crossing divisor $Q_{1} Q_{2} \cdots Q_{r}=0$, and the $\log$-monodromy around $Q_{i}=0$ is given by cup product with $\varphi_{i}$; a similar statement holds for $\mathcal{X}$. Condition (b) asserts that $\mathbb{U}$ matches up these monodromies.

Condition (c) ensures that both the quantum cohomology of $\mathcal{X}$ and the analytic continuation of the quantum cohomology of $Y$ make sense near the large-radius limit point for $\mathcal{X}$. This is explained in detail in Remark 6.18 below.

Condition (d) says that $\mathbb{U}$ is 'independent of Novikov variables'.

## 5. Basic Properties of the Transformation $\mathbb{U}$

Before we explore the implications of conjecture 4.1 we list various basic properties of the transformation $\mathbb{U}$. As we have chosen homogeneous bases for $H_{\mathrm{CR}}^{\bullet}(\mathcal{X} ; \mathbb{C})$ and $H^{\bullet}(Y ; \mathbb{C})$ and as $\mathbb{U}$ is grading-preserving, we can represent the transformation $\mathbb{U}$ by an $(N+1) \times(N+1)$ matrix, each entry of which is a Laurent monomial in $z$ of fixed degree. The matrix entries are independent of Novikov variables, so each entry is the product of a complex number and a fixed power of $z$. $\mathbb{U}$ is therefore a Laurent polynomial in $z$. For example, if $\mathcal{X}=\mathbb{P}(1,1,1,3), Y=\mathbb{F}_{3}$, and we choose bases as in [13], then

$$
\mathbb{U}=\left(\begin{array}{cccccc}
1 & 0 & 0 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 & 0 & 0 \\
0 & 0 & 1 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & -\frac{2 \sqrt{3} \pi}{3 \Gamma\left(\frac{1}{3}\right)^{3}} z & \frac{2 \sqrt{3} \pi}{3 \Gamma\left(\frac{2}{3}\right)^{3}} \\
-\frac{\pi^{2}}{3} z^{-2} & 0 & 0 & 0 & \frac{2 \pi^{2}}{3 \Gamma\left(\frac{1}{3}\right.} & \frac{2 \pi^{2}}{3 \Gamma\left(\frac{2}{3}\right)^{3}} z^{-1} \\
-8 \zeta(3) z^{-3} & 0 & 0 & 1 & -\frac{2 \sqrt{3} \pi^{3}}{9 \Gamma\left(\frac{1}{3}\right)^{3}} z^{-1} & \frac{2 \sqrt{3} \pi^{3}}{9 \Gamma\left(\frac{2}{3}\right)^{3}} z^{-2}
\end{array}\right) .
$$

This illustrates the fact that even if the Gromov-Witten invariants of $\mathcal{X}$ and $Y$ are defined over $\mathbb{Q}$, the transformation $\mathbb{U}$ may only be defined over $\mathbb{C}$. Note that some of the matrix entries here are 'highly transcendental'.

Lemma 5.1. Suppose that $\omega_{i} \in H_{\mathrm{CR}}^{i}(\mathcal{X} ; \mathbb{C})$. Then:

(a) $\mathbb{U}\left(\omega_{2 r}\right)=z^{r} \rho_{0}+O\left(z^{r-1}\right)$ for some $\rho_{0} \in H^{0}(Y ; \mathbb{C})$, and if $\rho_{0} \neq 0$ then $r=0$;

(b) $\mathbb{U}\left(\omega_{2 r+1}\right)=z^{r} \rho_{1}+O\left(z^{r-1}\right)$ for some $\rho_{1} \in H^{1}(Y ; \mathbb{C})$, and if $\rho_{1} \neq 0$ then $r=0$.

(c) $\mathbb{U}\left(\omega_{2 r+2}\right)=z^{r} \rho_{2}+O\left(z^{r-1}\right)$ for some $\rho_{2} \in H^{2}(Y ; \mathbb{C})$, and if $\rho_{2} \notin \operatorname{ker} \pi_{!}$then $r=0$.

Proof. (a) As $\mathbb{U}$ is grading-preserving, $\mathbb{U}\left(\omega_{2 r}\right)=z^{r} \lambda \mathbf{1}_{Y}+O\left(z^{r-1}\right)$ for some $\lambda \in \mathbb{C}$. Write $D=\operatorname{dim}_{\mathbb{C}}(\mathcal{X})$ and suppose that $\lambda \neq 0$. Then, as $\mathcal{X}$ is Kähler and as the map $\pi^{\star}: H^{\bullet}(\mathcal{X} ; \mathbb{C}) \rightarrow H^{\bullet}(Y ; \mathbb{C})$ is injective, there exists $\omega \in H^{2}(\mathcal{X} ; \mathbb{C})$ such that $\left(\pi^{\star} \omega\right)^{D} \in H^{2 D}(Y ; \mathbb{C})$ is non-zero. We have

$$
\begin{aligned}
\mathbb{U}(\overbrace{\omega \bigcup_{\mathrm{CR}}^{\bigcup} \cdots \cup_{\mathrm{CR}} \omega}^{D} \cup \omega_{\mathrm{CR}} \omega_{2 r}) & =z^{r} \lambda\left(\pi^{\star} \omega\right)^{D}+O\left(z^{r-1}\right) \\
& \neq 0
\end{aligned}
$$

and hence $\left(\omega \cup_{\mathrm{CR}}\right)^{D} \underset{\mathrm{CR}}{\bigcup} \omega_{2 r} \neq 0$. For degree reasons, $r$ must be zero.

(b) As $\mathbb{U}$ is grading-preserving, $\mathbb{U}\left(\omega_{2 r+1}\right)=z^{r} \rho_{1}+O\left(z^{r-1}\right)$ for some $\rho_{1} \in$ $H^{1}(Y ; \mathbb{C})$. As $\pi^{\star}: H^{1}(\mathcal{X} ; \mathbb{C}) \rightarrow H^{1}(Y ; \mathbb{C})$ is an isomorphism, we have $\rho_{1}=\pi^{\star} \theta_{1}$ for some $\theta_{1} \in H^{1}(\mathcal{X} ; \mathbb{C})$. Suppose that $\rho_{1} \neq 0$. By Hard Lefschetz for $H^{\bullet}(\mathcal{X} ; \mathbb{C})$ (ordinary cohomology not Chen-Ruan cohomology), there exists $\omega \in H^{2}(\mathcal{X} ; \mathbb{C})$ such that $\omega^{D-1} \theta_{1} \in H^{2 D-1}(\mathcal{X} ; \mathbb{C})$ is non-zero. Injectivity of $\pi^{\star}$ gives $\left(\pi^{\star} \omega\right)^{D-1} \rho_{1} \neq 0$, and so

$$
\begin{aligned}
\mathbb{U}(\overbrace{\omega \underset{\mathrm{CR}}{\bigcup} \cdots \bigcup_{\mathrm{CR}}^{\cup} \omega}^{D-1} \cup \omega_{\mathrm{CR}} \omega_{2 r+1}) & =z^{r}\left(\pi^{\star} \omega\right)^{D-1} \rho_{1}+O\left(z^{r-1}\right) \\
& \neq 0
\end{aligned}
$$

As before, this forces $r=0$.

(c) As $\mathbb{U}$ is grading-preserving, $\mathbb{U}\left(\omega_{2 r+2}\right)=z^{r} \rho_{2}+O\left(z^{r-1}\right)$ for some $\rho_{2} \in$ $H^{2}(Y ; \mathbb{C})$. Suppose that $\rho_{2} \notin \operatorname{ker} \pi!$. Then there exist $\omega, \omega^{\prime} \in H^{2}(\mathcal{X} ; \mathbb{C})$ such that $\int_{\mathcal{X}} \pi!\rho_{2} \cup \omega^{D-2} \cup \omega^{\prime} \neq 0$; here we used the non-degeneracy of the Poincaré pairing and Hard Lefschetz for $H^{\bullet}(\mathcal{X} ; \mathbb{C})$. Thus $\int_{Y} \rho_{2} \cup \pi^{\star} \omega^{D-2} \cup \pi^{\star} \omega^{\prime} \neq 0$, and so $\mathbb{U}\left(\omega_{2 r+2}\right) \cup \pi^{\star} \omega^{D-2} \cup \pi^{\star} \omega^{\prime} \neq 0$. But

$$
\mathbb{U}\left(\omega_{2 r+2}\right) \cup \pi^{\star} \omega^{D-2} \cup \pi^{\star} \omega^{\prime}=\mathbb{U}(\overbrace{\omega \underset{\mathrm{CR}}{\bigcup} \cdots \bigcup_{\mathrm{CR}} \omega}^{D-2} \bigcup_{\mathrm{CR}} \omega^{\prime} \bigcup_{\mathrm{CR}} \omega_{2 r+2})
$$

and as this is non-zero we must, for degree reasons, have $r=0$.

Lemma 5.2. Suppose that $\mathbb{U}$ sends $\mathcal{H}_{\mathcal{X}}^{-}$to $\mathcal{H}_{Y}^{-}$, so that

$$
\mathbb{U}=U_{0}+U_{1} z^{-1}+\cdots+U_{k} z^{-k}
$$

for some non-negative integer $k$ and some linear maps $U_{i}: H_{\mathrm{CR}}^{\bullet}(\mathcal{X} ; \mathbb{C}) \rightarrow H^{\bullet}(Y ; \mathbb{C})$. Then:

(i) $U_{0}$ is grading-preserving;

(ii) $U_{0}$ maps $\mathbf{1}_{\mathcal{X}}$ to $\mathbf{1}_{\mathcal{Y}}$;

(iii) $U_{0}$ maps $\rho \in H^{2}(\mathcal{X} ; \mathbb{C})$ to $\pi^{\star} \rho \in H^{2}(Y ; \mathbb{C})$;

(iv) $U_{0}$ identifies the orbifold Poincaré pairing on $H_{\mathrm{CR}}^{\bullet}(\mathcal{X} ; \mathbb{C})$ with the Poincare pairing on $H^{\bullet}(Y ; \mathbb{C})$.

Proof. (i) $\mathbb{U}$ is grading-preserving. (ii) conjecture 4.1(a). (iii) conjecture 4.1(b). (iv) $\mathbb{U}$ is a symplectic isomorphism.

## 6. From Givental's Cone to Quantum Cohomology

Since $\mathcal{L}_{\mathcal{X}}$ encodes all genus-zero Gromov-Witten invariants of $\mathcal{X}$, it implicitly encodes the big quantum product for $\mathcal{X}$. In the same way, $\mathcal{L}_{Y}$ encodes the big quantum product for $Y$. In this section we describe how to determine the quantum products from $\mathcal{L}_{\mathcal{X}}$ and $\mathcal{L}_{Y}$, using the geometric structure described in theorem 3.2, The big quantum products can be regarded in three different ways:

(1) as families of Frobenius algebras, since

$$
(u \underset{\tau}{\star v}, w)_{\mathcal{X}}=(u, v \underset{\tau}{\star w})_{\mathcal{X}} \quad \text { and } \quad\left(u^{\prime} \underset{t}{\circledast v^{\prime}, w^{\prime}}\right)_{Y}=\left(u^{\prime}, v^{\prime} \underset{t}{\circledast} w^{\prime}\right)_{Y}
$$

for all $u, v, w \in H_{\mathrm{CR}}^{\bullet}(\mathcal{X} ; \mathbb{C})$ and $u^{\prime}, v^{\prime}, w^{\prime} \in H^{\bullet}\left(Y ; \Lambda_{\mathcal{X}}\right)$.

(2) as F-manifolds. An F-manifold is, roughly speaking, a Frobenius manifold without a pairing. It is a manifold equipped with a supercommutative associative multiplication on the tangent sheaf and a global unit vector field such that the multiplication o satisfies

$$
\operatorname{Lie}_{X \circ Y}(\circ)=X \circ \operatorname{Lie}_{Y}(\circ)+Y \circ \operatorname{Lie}_{X}(\circ)
$$

for any two local vector fields $X$ and $Y$. F-manifolds are studied in [23,24].

(3) as Frobenius manifolds. A Frobenius manifold is a manifold $M$ equipped with the structure of a unital Frobenius algebra on each tangent space $T_{x} M$ such that the associated metric on $T M$ is flat, the identity vector field is flat, and certain integrability conditions hold (these include the celebrated WDVV equations). Frobenius manifolds are studied in [17,28.

Once again, write $\mathcal{Z}$ for either $\mathcal{X}$ or $Y$. In this section, we will see how to pass from $\mathcal{L}_{\mathcal{Z}}$ to:

(1) a family of Frobenius algebras. This family is intrinsic to $\mathcal{L}_{\mathcal{Z}}$ in that it depends only on the symplectic space $\mathcal{H}_{\mathcal{Z}}$ and on $\mathcal{L}_{\mathcal{Z}} \subset \mathcal{H}_{\mathcal{Z}}$ satisfying the conclusions of theorem [3.2) it is independent of the polarization $\mathcal{H}_{\mathcal{Z}}=$ $\mathcal{H}_{\mathcal{Z}}^{+} \oplus \mathcal{H}_{\mathcal{Z}}^{-}$ used to define $\mathcal{L}_{\mathcal{Z}}$.

(2) an F-manifold. This depends, up to isomorphism, only on $\mathcal{H}_{\mathcal{Z}}, \mathcal{L}_{\mathcal{Z}}$, and a choice of point on $\mathcal{L}_{\mathcal{Z}}$.

(3) a Frobenius manifold. This depends on $\mathcal{H}_{\mathcal{Z}}, \mathcal{L}_{\mathcal{Z}}$, a point $x$ of $\mathcal{L}_{\mathcal{Z}}$, and a choice of opposite subspace $\mathcal{H}_{\mathcal{Z}}^{\text {opp }} \subset \mathcal{H}_{\mathcal{Z}}$. Choosing $ x \in \mathcal{L}_{\mathcal{Z}}$ appropriately and taking $\mathcal{H}_{\mathcal{Z}}^{\text {opp }}=\mathcal{H}_{\mathcal{Z}}^{-}$ gives the Frobenius manifold corresponding to the quantum cohomology of $\mathcal{Z}$; we explain this in $\S \widehat{6}(\mathrm{~d}-\mathrm{e})$ below.

The ideas presented in this section are due to Barannikov and Givental. Closelyrelated discussions can be found in [5, 13, 22].

6.1. From Givental's Cone to a Family of Frobenius Algebras. Given $\mathcal{L}_{\mathcal{Z}} \subset$ $\mathcal{H}_{\mathcal{Z}}$ satisfying the conclusions of theorem 3.2 and a point $x \in \mathcal{L}_{\mathcal{Z}}$, the quotient $T_{x} / z T_{x}$, where $T_{x}=T_{x} \mathcal{L}_{\mathcal{Z}}$, inherits the structure of a Frobenius algebra as follows. The $\Lambda$-bilinear form

$$
\begin{aligned}
& T_{x} \otimes T_{x} \longrightarrow \Lambda \\
& v \otimes w \longmapsto \Omega\left(v, z^{-1} w\right)
\end{aligned}
$$

is symmetric and vanishes whenever $v$ or $w$ lies in $z T_{x}$, so it descends to give a symmetric bilinear form

$$
g\left(v+z T_{x}, w+z T_{x}\right)=\Omega\left(v, z^{-1} w\right)
$$

on $T_{x} / z T_{x}$. This form is non-degenerate as $T_{x}$ is maximal isotropic. Choosing a Lagrangian subspace $V$ such that $\mathcal{H}_{\mathcal{Z}}=T_{x} \oplus V$ - one could, for instance, take $V=\mathcal{H}_{\mathcal{Z}}^{-}$- identifies $V$ with $T_{x}^{\star}:=\operatorname{Hom}\left(T_{x}, \Lambda\right)$ and $\mathcal{H}_{\mathcal{Z}}$ with the cotangent bundle $T_{x} \oplus T_{x}^{\star}$. As $\mathcal{L}_{\mathcal{Z}}$ is Lagrangian, there is the germ of a function $\phi: T_{x} \rightarrow \Lambda$ such that $\phi(x)=0$ and that $\mathcal{L}_{\mathcal{Z}}$ coincides, in a formal neighbourhood of $x$, with the graph of the differential of $\phi$. The third derivative $\left.d^{3} \phi\right|_{x}$ defines a cubic tensor on $T_{x}$; it is easy to see that this is independent of the choice of $V$. Theorem 3.2 implies that $\phi$ vanishes identically along the germ of $z T_{x} \subset T_{x}$, and as $\left.d^{3} \phi\right|_{x}(u, v, w)$ vanishes whenever one of $u, v, w$ lies in $z T_{x}$ we obtain a cubic tensor $c$ on $T_{x} / z T_{x}$ :

$$
c\left(u+z T_{x}, v+z T_{x}, w+z T_{x}\right)=\left.d^{3} \phi\right|_{x}(u, v, w)
$$

The tensors $c$ and $g$ together define a supercommutative product $\star$ on $T_{x} / z T_{x}$, via

$$
g\left(\left(u+z T_{x}\right) \star\left(v+z T_{x}\right), w+z T_{x}\right)=c\left(u+z T_{x}, v+z T_{x}, w+z T_{x}\right)
$$

The product $\star$ automatically has the Frobenius property with respect to $g$. We will see in the next section that it is associative and unital; the unit depends upon the point $x \in \mathcal{L}_{\mathcal{Z}}$, so even if the tangent spaces $T_{x_{1}}=T_{x_{1}} \mathcal{L}_{\mathcal{Z}}$ and $T_{x_{2}}=T_{x_{2}} \mathcal{L}_{\mathcal{Z}}$ coincide, the algebra structures on $T_{x_{1}} / z T_{x_{1}}$ and $T_{x_{2}} / z T_{x_{2}}$ will in general differ. Thus we have obtained from $\mathcal{L}_{\mathcal{Z}}$ a vector bundle

$$
T \mathcal{L}_{\mathcal{Z}} / z T \mathcal{L}_{\mathcal{Z}} \rightarrow \mathcal{L}_{\mathcal{Z}}
$$

such that the fibers of this vector bundle form a family of Frobenius algebras.

Remark 6.1. The construction here resembles the construction of the Yukawa coupling in the B-model of topological string theory associated to a Calabi-Yau 3fold (see [16] and e.g. [20, §6]). This is not an accident. The tangent spaces $T$ to $\mathcal{L}_{\mathcal{Z}}$ form a variation of semi-infinite Hodge structure in the sense of Barannikov [5], and part of the power of Barannikov's theory is that it can describe A-model phenomena (like quantum cohomology) and B-model phenomena in the same language.

Remark 6.2. If we take $\mathcal{X}$ to be a manifold, $\mathcal{Z}=\mathcal{X}, V=\mathcal{H}_{\mathcal{X}}^{-}$, and the point $x \in \mathcal{L}_{\mathcal{X}}$ to be $J_{\mathcal{X}}(\tau,-z)$, defined in $\S$ (d) below, then the function-germ $\phi$ described above is Givental's genus-zero ancestor potential $\overline{\mathcal{F}}_{\tau}^{0}$ of $\mathcal{X}$ [21, §5].

6.2. From Givental's Cone to an F-Manifold. Given $\mathcal{L}_{\mathcal{Z}} \subset \mathcal{H}_{\mathcal{Z}}$ satisfying the conclusions of theorem 3.2 and a point $x \in \mathcal{L}_{\mathcal{Z}}$, we construct an F-manifold as follows. Let $T_{x}=T_{x} \mathcal{L}_{\mathcal{Z}}$ and choose a Lagrangian subspace $V \subset \mathcal{H}_{\mathcal{Z}}$ such that $\mathcal{H}_{\mathcal{Z}}=T_{x} \oplus V$. Let $M=T_{x} \cap z V$. Our F-manifold will be based on a formal neighbourhood of the origin in $M$.

As $\mathcal{L}_{\mathcal{Z}}$ is the graph of a germ of a map from $T_{x}$ to $V$, there is a unique germ of a function $K: M \rightarrow \mathcal{H}_{\mathcal{Z}}$ such that $K(t) \in \mathcal{L}_{\mathcal{Z}}$ and $K(t)=x+t+v(t)$ for some $v(t) \in V$. Choose a basis $e_{0}, \ldots, e_{N}$ for $M$ and denote the corresponding linear co-ordinates on $M$ by $t_{a}, 0 \leq a \leq N$.

Proposition 6.3. For t in a formal neighbourhood of the origin in $M$, the elements

$$
\frac{\partial K}{\partial t_{a}}(t)+z T_{K(t)}, \quad a=0,1, \ldots, N
$$

form a basis for $T_{K(t)} / z T_{K(t)}$.

Proof. It suffices to prove this at $t=0$. But $K(0)=x$ and, since $T_{x}$ is tangent to $\mathcal{L}_{\mathcal{Z}}$ at $x, \frac{\partial K}{\partial t_{a}}(0)$ has no component along $V: \frac{\partial K}{\partial t_{a}}(0)=e_{a}$. So we need to show that

$$
e_{a}+z T_{x} \quad a=0,1, \ldots, N
$$

form a basis for $T_{x} / z T_{x}$. This holds because $\mathcal{H}_{\mathcal{Z}}=z T_{x} \oplus z V$, and so the projection $M=T_{x} \cap z V \rightarrow T_{x} / z T_{x}$ is an isomorphism.

Thus for $t$ in a formal neighbourhood $M_{0}$ of the origin in $M$, the map $\left.D K\right|_{t}$ : $T_{t} M \rightarrow T_{K(t)} / z T_{K(t)}$ is an isomorphism. Pulling back the Frobenius algebra structure defined in the previous section via the map $D K$ gives a pairing

$$
g_{\alpha \beta}(t)=\Omega\left(\frac{\partial K}{\partial t_{\alpha}}(t), z^{-1} \frac{\partial K}{\partial t_{\beta}}(t)\right)
$$

and a symmetric 3 -tensor

$$
c_{\alpha \beta \gamma}(t)=\Omega\left(\frac{\partial^{2} K}{\partial t_{\beta} \partial t_{\gamma}}(t), \frac{\partial K}{\partial t_{\alpha}}(t)\right)
$$

on $T_{t} M_{0}$. Denote the induced product on $T_{t} M_{0}$ by $\circ_{t}$ :

$$
e_{\alpha} \circ_{t} e_{\beta}=c_{\alpha \beta}^{\gamma}(t) e_{\gamma}
$$

where $c_{\alpha \beta \gamma}(t)=c_{\alpha \beta}{ }^{\epsilon}(t) g_{\epsilon \gamma}(t)$.

## Proposition 6.4.

(a) $\nabla_{u 0_{t} v} K(t)+z T_{K(t)}=-z \nabla_{u} \nabla_{v} K(t)+z T_{K(t)}$, where $\nabla_{u}=u^{\alpha} \frac{\partial}{\partial t_{\alpha}}$ denotes the directional derivative along $u=u^{\alpha} e_{\alpha}$.

(b) The tensor $c_{\alpha \beta}{ }^{\epsilon}(t) c_{\epsilon \gamma \delta}(t)$ is symmetric in $\alpha, \beta, \gamma, \delta$.

(c) The product $\circ_{t}$ is associative.

Proof. As $c_{\gamma \beta \alpha}(t)=c_{\alpha \beta}{ }^{\epsilon}(t) g_{\gamma \epsilon}(t)$, we have

$$
\Omega\left(\frac{\partial^{2} K}{\partial t_{\beta} \partial t_{\alpha}}(t), \frac{\partial K}{\partial t_{\gamma}}(t)\right)=\Omega\left(\frac{\partial K}{\partial t_{\gamma}}(t), z^{-1} c_{\alpha \beta}{ }^{\epsilon}(t) \frac{\partial K}{\partial t_{\epsilon}}(t)\right)
$$

The pairing (24) is non-degenerate, and (25) is a basis for $T_{K(t)} / z T_{K(t)}$, so

$$
-z \frac{\partial^{2} K}{\partial t_{\alpha} \partial t_{\beta}}(t)+z T_{K(t)}=c_{\alpha \beta}{ }^{\epsilon}(t) \frac{\partial K}{\partial t_{\epsilon}}(t)+z T_{K(t)}
$$

This proves (a). Theorem 3.2 implies that if $y(t) \in T_{K(t)}$ then $z \frac{\partial y}{\partial t_{a}}(t) \in T_{K(t)}$ too, so differentiating (26) yields

$$
\begin{aligned}
z^{2} \frac{\partial^{3} K}{\partial t_{\alpha} \partial t_{\beta} \partial t_{\gamma}}(t)+z T_{K(t)} & =-c_{\alpha \beta}{ }^{\epsilon}(t) z \frac{\partial^{2} K}{\partial t_{\epsilon} \partial t_{\gamma}}(t)+z T_{K(t)} \\
& =c_{\alpha \beta}{ }^{\epsilon}(t) c_{\epsilon \gamma}{ }^{\delta}(t) \frac{\partial K}{\partial t_{\delta}}(t)+z T_{K(t)}
\end{aligned}
$$

Thus $c_{\alpha \beta}{ }^{\epsilon}(t) c_{\epsilon \gamma}{ }^{\delta}(t)$ is symmetric in $\alpha, \beta, \gamma$. As $c_{\epsilon \gamma \delta}(t)$ is symmetric as well, part (b) follows. Part (c) is an immediate consequence of part (b).

So far, we have constructed a family of supercommutative associative products on the fibers of $T M_{0}$, depending on $\mathcal{L}_{\mathcal{Z}} \subset \mathcal{H}_{\mathcal{Z}}$, a point $x \in \mathcal{L}_{\mathcal{Z}}$, and a Lagrangian subspace $V$. To prove that this makes $M_{0}$ into an F-manifold we need to show that the algebras $\left(T_{t} M_{0}, \circ_{t}\right)$ are unital and that the integrability condition (23) holds. After that we will show that, up to isomorphism, the F-manifold we have constructed is independent of the choice of Lagrangian subspace $V$.

Define a vector field $e$ on $M_{0}$ by

$$
\nabla_{e(t)} K(t)+z T_{K(t)}=-z^{-1} K(t)+z T_{K(t)}
$$

This makes sense, as $z^{-1} K(t) \in T_{K(t)}$ by theorem 3.2.

Proposition 6.5. $e(t)$ is the identity element in the algebra $\left(T_{t}\left(M_{0}\right), \circ_{t}\right)$.

Proof. Let $v$ be any vector field on $M_{0}$. Then

$$
\begin{aligned}
\nabla_{e(t) \circ_{t} v(t)} K(t)+z T_{K(t)} & =-z \nabla_{v}(t) \nabla_{e(t)} K(t)+z T_{K(t)} \\
& =\nabla_{v(t)} K(t)+z T_{K(t)}
\end{aligned}
$$

and so $e(t) \circ_{t} v(t)=v(t)$.

Corollary 6.6. The product on $T_{x} / z T_{x}$ constructed in $\sqrt{6(}(a)$ is associative and unital.

Proof. Set $t=0$ in propositions 6.4(c) and 6.5 .

Proposition 6.7. The triple $\left(M_{0}, \circ, e\right)$ is an F-manifold.

Proof. It remains only to establish the integrability condition (23), and for this the argument of [24, §2] applies. The essential ingredients there are proposition [6.4(b) and that the quantity $\frac{\partial}{\partial t_{\delta}} c_{\alpha \beta \gamma}(t)$ is symmetric in $\alpha, \beta, \gamma, \delta$ : the latter assertion holds here as $\frac{\partial}{\partial t_{\delta}} c_{\alpha \beta \gamma}(t)$ is the fourth derivative of a function $\phi: M_{0} \rightarrow \Lambda$.

Proposition 6.8. Suppose that $\mathcal{L}_{\mathcal{Z}} \subset \mathcal{H}_{\mathcal{Z}}$ satisfies the conclusions of theorem 3.2. that $x \in \mathcal{L}_{\mathcal{Z}}$, that $T_{x}=T_{x} \mathcal{L}_{\mathcal{Z}}$, and that $V, V^{\prime} \subset \mathcal{H}_{\mathcal{Z}}$ are Lagrangian subspaces such that $T_{x} \oplus V=T_{x} \oplus V^{\prime}=\mathcal{H}_{\mathcal{Z}}$. Let $\left(M_{0}, \circ, e\right)$ and $\left(M_{0}^{\prime}, o^{\prime}, e^{\prime}\right)$ be the corresponding F-manifolds, and

$$
K: M_{0} \rightarrow \mathcal{H}_{\mathcal{Z}}, \quad K^{\prime}: M_{0}^{\prime} \rightarrow \mathcal{H}_{\mathcal{Z}}
$$

be the corresponding functions (constructed just above proposition 6.3). Then there is a unique map $f: M_{0} \rightarrow M_{0}^{\prime}$ and a unique section $w$ of $K^{\star} T \mathcal{L}_{\mathcal{Z}}$ (i.e. a unique choice of $\left.w(t) \in T_{K(t)} \mathcal{L}_{\mathcal{Z}}\right)$ such that

$$
K^{\prime}(f(t))=K(t)+z w(t), \quad \text { for all } t \in M_{0}
$$

The map $f$ gives an isomorphism of $F$-manifolds between $\left(M_{0}, \circ, e\right)$ and $\left(M_{0}^{\prime}, \circ^{\prime}, e^{\prime}\right)$.

Proof. Let $\pi^{\prime}: \mathcal{H}_{\mathcal{Z}} \rightarrow T_{x}$ denote the projection along $V^{\prime}$, and for $y \in \mathcal{L}_{\mathcal{Z}}$ write $T_{y}=T_{y} \mathcal{L}_{\mathcal{Z}}$. Recall that $M_{0}, M_{0}^{\prime}$ are formal neighbourhoods of the origins in

$$
M=T_{x} \cap z V, \quad M^{\prime}=T_{x} \cap z V^{\prime}
$$

respectively, and that $K(t), K^{\prime}\left(t^{\prime}\right)$ are the unique elements of $\mathcal{L}_{\mathcal{Z}}$ of the form

$$
K(t)=x+t+v(t), \quad K^{\prime}\left(t^{\prime}\right)=x^{\prime}+t^{\prime}+v^{\prime}\left(t^{\prime}\right)
$$

where $t \in M_{0}, v(t) \in V, t^{\prime} \in M_{0}^{\prime}$, and $v^{\prime}\left(t^{\prime}\right) \in V^{\prime}$

We begin by showing that, for all $t \in M_{0}, T_{x}=\pi^{\prime}\left(z T_{K(t)}\right) \oplus M^{\prime}$. It suffices to prove this at $t=0$, and since $K(0)=x$ we need to show that $T_{x}=z T_{x} \oplus M^{\prime}$. This follows from the fact that the projection $M^{\prime} \rightarrow T_{x} / z T_{x}$ is an isomorphism (c.f. the proof of proposition 6.3). So $T_{x}=\pi^{\prime}\left(z T_{K(t)}\right) \oplus M^{\prime}$ for all $t \in M_{0}$.

There is therefore a unique element $w(t) \in T_{K(t)}$ such that

$$
\pi^{\prime}[K(t)+z w(t)] \in x+M^{\prime}
$$

Theorem 3.2 implies that $K(t)+z w(t) \in \mathcal{L}_{\mathcal{Z}}$, and so setting

$$
f(t)=\pi^{\prime}[K(t)+z w(t)]-x
$$

gives a map $f: M_{0} \rightarrow M_{0}^{\prime}$ such that

$$
K^{\prime}(f(t))=K(t)+z w(t)
$$

This shows existence of a map $f: M_{0} \rightarrow M_{0}^{\prime}$ and a section $w$ of $K^{\star} T \mathcal{L}_{\mathcal{Z}}$ satisfying (27); uniqueness is clear.

It remains to show that $f$ gives an isomorphism of $\mathrm{F}$-manifolds. Note first that $T_{K(t)}=T_{K^{\prime}(f(t))}$ : theorem 3.2 implies that $K(t) \in z T_{K(t)}$, so $K^{\prime}(f(t))$ is also in
$z T_{K(t)}$, and so $T_{K(t)}=T_{K^{\prime}(f(t))}$ by theorem[3.2 again. Write $T=T_{K(t)}=T_{K^{\prime}(f(t))}$. Using proposition 6.3, we can write $w(t) \in T$ uniquely in the form

$$
w(t)=\nabla_{g(t)} K(t)+z h(t)
$$

for some vector field $g$ on $M_{0}$ and some element $h(t) \in T$. Thus for any vector field $v$ on $M_{0}$,

$$
\begin{aligned}
\nabla_{f_{\star} v(t)} K^{\prime}(f(t))+z T & =\nabla_{v(t)}(K(t)+z w(t))+z T \\
& =\nabla_{v(t)} K(t)+z \nabla_{v(t)} \nabla_{g(t)} K(t)+z T \\
& =\nabla_{v(t)} K(t)+\nabla_{v(t) \circ_{t} g(t)} K(t)+z T
\end{aligned}
$$

As the maps $\left.D K\right|_{t}: T_{t} M_{0} \rightarrow T / z T$ and $\left.D K^{\prime}\right|_{f(t)}: T_{f(t)} M_{0}^{\prime} \rightarrow T / z T$ are isomorphisms, equation (29) determines the pushforward $f_{\star} v$. Differentiating again, along a vector field $w$ on $M_{0}$, gives

$$
z \nabla_{f_{\star} v(t)} \nabla_{f_{\star} w(t)} K^{\prime}(f(t))+z T=z \nabla_{v(t)} \nabla_{w(t)} K(t)+z \nabla_{w(t)} \nabla_{v(t) \circ_{t} g(t)} K(t)+z T
$$

and hence

$$
\nabla_{\left(f_{\star} v(t)\right) \circ_{f(t)}^{\prime}\left(f_{*} w(t)\right)} K^{\prime}(f(t))+z T=\nabla_{v(t) \circ_{t} w(t)} K(t)+\nabla_{v(t) \circ_{t} w(t) \circ_{t} g(t)} K(t)+z T
$$

Comparing with (29), we find

$$
f_{\star}\left(v(t) \circ_{t} w(t)\right)=\left(f_{\star} v(t)\right) \circ_{f(t)}^{\prime}\left(f_{\star} w(t)\right)
$$

The map $f$ is certainly invertible (this follows from uniqueness) and so $f$ gives an isomorphism of $\mathrm{F}$-manifolds.

Remark 6.9. It was pointed out to us by Hiroshi Iritani that the arguments in this section show that the moduli space of tangent spaces to $\mathcal{L}_{\mathcal{Z}}$ carries a canonical F-manifold structure; see [13, §2.2] for a different point of view on this.

6.3. From Givental's Cone to a Frobenius Manifold. Consider $\mathcal{L}_{\mathcal{Z}} \subset \mathcal{H}_{\mathcal{Z}}$ satisfying the conclusions of theorem 3.2 and $x \in \mathcal{L}_{\mathcal{Z}}$. As before, write $T_{x}=T_{x} \mathcal{L}_{\mathcal{Z}}$. To construct a Frobenius manifold, we need to choose also an opposite subspace at $x$.

Definition. Let $x \in \mathcal{L}_{\mathcal{Z}}$. A subspace $\mathcal{H}^{\text {opp }} \subset \mathcal{H}_{\mathcal{Z}}$ is called opposite at $x$ or opposite to $T_{x}$ if $\mathcal{H}^{\text {opp }}$ is Lagrangian, $T_{x} \oplus \mathcal{H}^{\text {opp }}=\mathcal{H}_{\mathcal{Z}}$, and $z^{-1} \mathcal{H}^{\text {opp }} \subset \mathcal{H}^{\text {opp }}$.

For example, $\mathcal{H}_{\mathcal{Z}}^{-}$is opposite at $x$ for all $x \in \mathcal{L}_{\mathcal{Z}}$. Our Frobenius manifold will be based on a formal neighbourhood of zero in $z \mathcal{H}^{\text {opp }} / \mathcal{H}^{\text {opp }}$.

We note the following immediate consequence of oppositeness.

Lemma 6.10. If $\mathcal{H}^{\text {opp }}$ is opposite to $T_{x}$ then the projections



are both isomorphisms.

Consider the 'slice' $\left(x+z \mathcal{H}^{\text {opp }}\right) \cap \mathcal{L}_{\mathcal{Z}}$. This is the germ (at $x$ ) of a finitedimensional submanifold of $\mathcal{L}_{\mathcal{Z}}$, and lemma $6.10 \mathrm{implies} \mathrm{that} \mathrm{the} \mathrm{map}$

$$
\begin{aligned}
p:\left(x+z \mathcal{H}^{\text {opp }}\right) \cap \mathcal{L}_{\mathcal{Z}} & \longrightarrow z \mathcal{H}^{\text {opp }} / \mathcal{H}^{\text {opp }} \\
y & \longmapsto y-x+\mathcal{H}^{\text {opp }}
\end{aligned}
$$

has bijective derivative at $x$. Thus there is a map from the formal neighbourhood $N_{0}$ of zero in $z \mathcal{H}^{\text {opp }} / \mathcal{H}^{\text {opp }}$

$$
J: N_{0} \longrightarrow\left(x+z \mathcal{H}^{\text {opp }}\right) \cap \mathcal{L}_{\mathcal{Z}}
$$

such that $p \circ J=\mathrm{id}$. If we identify $N_{0}$ with a formal neighbourhood of the origin in $z \mathcal{H}^{\text {opp }} \cap T_{x}$ via the isomorphism $\pi$ in (30), then

$$
J(t)=x+t+h(t)
$$

for some $h(t) \in \mathcal{H}^{\text {opp }}$, and so $J$ coincides with the map $K$ defined in $\S \underline{6}$ (b) by taking $V=\mathcal{H}^{\text {opp }}$.

As in $\sqrt[9]{6}(\mathrm{~b})$, the derivative $\left.D J\right|_{t}: T_{t} N_{0} \rightarrow T_{J(t)} / z T_{J(t)}$ is an isomorphism for all $t \in N_{0}$. Pick a basis $e_{0}, \ldots, e_{N}$ for $z \mathcal{H}^{\text {opp }} \cap T_{x}$ and denote the corresponding linear co-ordinates on $N_{0}$, produced using lemma 6.10, by $t_{a}, 0 \leq a \leq N$. Pulling back the Frobenius algebra structure on $T_{J(t)} / z T_{J(t)}$ defined in $\$ 6$ (a) along the map $D J$ gives a pairing

$$
g_{\alpha \beta}(t)=\Omega\left(\frac{\partial J}{\partial t_{\alpha}}(t), z^{-1} \frac{\partial J}{\partial t_{\beta}}(t)\right)
$$

and a symmetric 3 -tensor

$$
c_{\alpha \beta \gamma}(t)=\Omega\left(\frac{\partial^{2} J}{\partial t_{\beta} \partial t_{\gamma}}(t), \frac{\partial J}{\partial t_{\alpha}}(t)\right)
$$

on $T_{t} N_{0}$. We again denote the corresponding product on $T_{t} N_{0}$ by $\circ_{t}$ and the identity vector field, constructed in proposition 6.5] by $e$. As before the product $o_{t}$ can be determined by differentiating $J(t)$, but this time the relationship between $\circ_{t}$ and $J(t)$ is more direct:

Proposition 6.11. $\nabla_{u \circ_{t} v} J(t)=-z \nabla_{u} \nabla_{v} J(t)$.

Proof. Proposition 6.4(a) shows that the quantity

$$
\nabla_{u \circ_{t} v} J(t)+z \nabla_{u} \nabla_{v} J(t)
$$

lies in $z T_{J(t)}$. On the other hand $J(t)=x+t+h(t)$, where $t \in z \mathcal{H}^{\text {opp }} \cap T_{x}$ and $h(t) \in \mathcal{H}^{\text {opp }}$, so (33) lies in $z \mathcal{H}^{\text {opp }}$. As $z \mathcal{H}^{\text {opp }} \cap z T_{J(t)}=\{0\}$ for all $t \in N_{0}$, the statement follows.

Proposition 6.12. The quadruple $\left(N_{0}, \circ, e, g\right)$ is a Frobenius manifold. In other words:

(a) each tangent space $\left(T_{t} N_{0}, \circ_{t}\right)$ is a unital supercommutative Frobenius algebra;

(b) the metric $g_{\alpha \beta}(t)$ is flat and the co-ordinates $t_{0}, \ldots, t_{N}$ are flat co-ordinates;

(c) the identity vector field e is flat;

(d) $c_{\alpha \beta \gamma}(t)$ is the third derivative of some function $\phi: N_{0} \rightarrow \Lambda$.

Proof. Part (a) was proved in $\$ 6$ (b). Part (d) is immediate from the construction of the tensor $c$. For (b) we have

$$
\frac{\partial J}{\partial t_{\alpha}}(t)=e_{\alpha}+h_{\alpha}(t), \quad \text { where } e_{\alpha} \in z \mathcal{H}^{\text {opp }} \text { and } h_{\alpha}(t) \in \mathcal{H}^{\text {opp }}
$$

and so

$$
g_{\alpha \beta}(t)=\Omega\left(e_{\alpha}+h_{\alpha}(t), z^{-1} e_{\beta}+z^{-1} h_{\beta}(t)\right)
$$

As $\mathcal{H}^{\text {opp }}$ is Lagrangian and $z^{-1} \mathcal{H}^{\text {opp }} \subset \mathcal{H}^{\text {opp }}, g_{\alpha \beta}(t)=\Omega\left(e_{\alpha}, e_{\beta}\right)$ is independent of $t$. This shows that $g$ is flat, and that $\left\{t_{a}\right\}$ are flat co-ordinates.

For (c) we need to show that $e(t)$ is constant in flat co-ordinates. In view of (34), we need to show that $\nabla_{e(t)} J(t)+\mathcal{H}^{\text {opp }}$ is constant with respect to $t$. Proposition 6.11 shows that $z \nabla_{e(t)} \nabla_{v(t)} J(t)=\nabla_{v(t)} J(t)$ for any vector field $v$ on $N_{0}$, and hence that $\nabla_{e(t)} J(t)=z^{-1} J(t)+C$ for some $C$ independent of $t$. Thus

$$
\begin{aligned}
\nabla_{e(t)} J(t)+\mathcal{H}^{\mathrm{opp}} & =z^{-1}(x+t+h(t))+C+\mathcal{H}^{\mathrm{opp}} \\
& =z^{-1} x+C+\mathcal{H}^{\mathrm{opp}}
\end{aligned}
$$

is independent of $t$. This completes the proof.

6.4. Example: the Quantum Cohomology of $\mathcal{X}$. We now show that if we take $x$ to be the point $\mathcal{L}_{\mathcal{X}} \cap\left(-z+\mathcal{H}_{\mathcal{X}}^{-}\right)$ and set $\mathcal{H}^{\text {opp }}=\mathcal{H}_{\mathcal{X}}^{-}$, then the Frobenius manifold constructed in the previous section is the quantum cohomology Frobenius manifold of $\mathcal{X}$. Set $\tau=\tau_{\alpha} \phi_{\alpha}$, and consider the element $ J_{\mathcal{X}}(\tau,-z)$ of $\mathcal{L}_{\mathcal{X}}$ such that its projection to $\mathcal{H}_{\mathcal{X}}^{+}$ along $\mathcal{H}_{\mathcal{X}}^{-}$ is equal to $-z+\tau$. We call $J_{\mathcal{X}}(\tau,-z)$ the $J$-function of $\mathcal{X}$. It is obtained by substituting $\tau_{0, a}=\tau_{a}, 0 \leq a \leq N ; \tau_{k, a}=0,0 \leq a \leq N$, $0<k<\infty$; and

$$
p_{l, b}=\left.\frac{\partial \mathcal{F}_{\mathcal{X}}^{0}}{\partial \tau_{l, b}}\right|_{\boldsymbol{\tau}(z)=\tau}=\sum_{d \in \operatorname{Eff}(\mathcal{X})} \sum_{n \geq 0}\left\langle\tau, \ldots, \tau, \phi_{b} \psi^{l}\right\rangle_{0, n+1, d}^{\mathcal{X}} \frac{U^{d}}{n!}
$$

into (14), via (20). Thus

$$
J_{\mathcal{X}}(\tau,-z)=-z+\tau+\sum_{d \in \operatorname{Eff}(\mathcal{X})} \sum_{n \geq 0} \sum_{l \geq 0}\left\langle\tau, \ldots, \tau, \phi_{\epsilon} \psi^{l}\right\rangle_{0, n+1, d}^{\mathcal{X}} \frac{U^{d} \phi^{\epsilon}}{n!(-z)^{l+1}}
$$

we abbreviate this to

$$
J_{\mathcal{X}}(\tau,-z)=-z+\tau+\sum_{d \in \operatorname{Eff}(\mathcal{X})} \sum_{n \geq 0}\left\langle\tau, \ldots, \tau, \frac{\phi_{\epsilon}}{-z-\psi}\right\rangle_{0, n+1, d}^{\mathcal{X}} \frac{U^{d} \phi^{\epsilon}}{n!}
$$

$J_{\mathcal{X}}(\tau,-z)$ is an element of $\mathcal{L}_{\mathcal{X}}$ - a formal power series in variables $\tau_{0}, \ldots, \tau_{N}$ taking values in $\mathcal{H}_{\mathcal{X}}$ - which depends analytically on $\tau_{1}, \ldots, \tau_{s}$ in the domain $\mathbb{C}^{s}$. We can see this analyticity explicitly:

## Proposition 6.13.

$$
\begin{aligned}
& J_{\mathcal{X}}(\tau,-z)=\mathrm{e}^{-\tau_{\mathrm{two}} / z} \times \\
& \left(-z+\tau_{\text {rest }}+\sum_{d \in \operatorname{Eff}(\mathcal{X})} \sum_{n \geq 0}\left\langle\tau_{\text {rest }}, \ldots, \tau_{\text {rest }}, \frac{\phi_{\epsilon}}{-z-\psi}\right\rangle_{0, n+1, d}^{\mathcal{X}} \frac{U^{d} \mathrm{e}^{d_{1} \tau_{1}} \cdots \mathrm{e}^{d_{s} \tau_{s} \phi^{\epsilon}}}{n!}\right)
\end{aligned}
$$

where $\tau_{\text {two }}$ and $\tau_{\text {rest }}$ are defined in (7).

Proof. This follows easily from the Divisor Equation, as in [14, lemma 2.5].

Our Frobenius manifold is based on a formal neighbourhood $N_{0}(\mathcal{X})$ of the origin in $z \mathcal{H}_{\mathcal{X}}^{-} / \mathcal{H}_{\mathcal{X}}^{-} \cong H_{\mathrm{CR}}^{\bullet}(\mathcal{X} ; \Lambda)$. Choose a point $ x \in \mathcal{L}_{\mathcal{X}} \cap\left(-z+z \mathcal{H}_{\mathcal{X}}^{-}\right)$ and write $x=-z+\sigma+h_{-}$ with $\sigma \in H_{\mathrm{CR}}^{\bullet}(\mathcal{X} ; \Lambda)$ and $h_{-} \in \mathcal{H}_{\mathcal{X}}^{-}$. Then the map $p$ defined in (31) satisfies

$$
p \circ J_{\mathcal{X}}(\sigma+\tau,-z)=\tau
$$

and so the map $J$ defined in (32) is

$$
J(\tau)=J_{\mathcal{X}}(\sigma+\tau,-z)
$$

The basis $\phi_{0}, \ldots, \phi_{N}$ for $H_{\mathrm{CR}}^{\bullet}(\mathcal{X} ; \Lambda)$ gives co-ordinates $\tau_{a}, 0 \leq a \leq N$, on $N_{0}(\mathcal{X})$ and these are flat co-ordinates for the Frobenius manifold:

$$
\begin{array}{rlr}
g_{\alpha \beta}(\tau) & =\Omega\left(\frac{\partial J_{\mathcal{X}}}{\partial \tau_{\alpha}}(\tau+\sigma,-z), z^{-1} \frac{\partial J_{\mathcal{X}}}{\partial \tau_{\beta}}(\tau+\sigma,-z)\right) \\
& =\Omega\left(\phi_{\alpha}+h_{\alpha}, z^{-1} \phi_{\beta}+z^{-1} h_{\beta}\right) \\
& =\left(\phi_{\alpha}, \phi_{\beta}\right)_{\mathcal{X}} . & \text { where } h_{\alpha}, h_{\beta} \in \mathcal{H}_{\mathcal{X}}^{-}
\end{array}
$$

To calculate the structure constants of the product $\circ_{\tau}$, we will need

$$
\begin{aligned}
& \frac{\partial J_{\mathcal{X}}}{\partial \tau_{\alpha}}(\sigma+\tau)=\phi_{\alpha}+h_{\alpha} \\
& \frac{\partial^{2} J_{\mathcal{X}}}{\partial \tau_{\beta} \partial \tau_{\gamma}}(\sigma+\tau)=-z^{-1} \sum_{d \in \operatorname{Eff}(\mathcal{X})} \sum_{n \geq 0}\left\langle\phi_{\beta}, \phi_{\gamma}, \sigma+\tau, \ldots, \sigma+\tau, \phi_{\epsilon}\right\rangle_{0, n+3, d}^{\mathcal{X}} \frac{U^{d} \phi^{\epsilon}}{n!} \\
&+z^{-1} h_{\beta \gamma}
\end{aligned}
$$

for some $h_{\alpha}, h_{\beta \gamma} \in \mathcal{H}_{\mathcal{X}}^{-} ;$this gives

$$
\begin{aligned}
c_{\alpha \beta \gamma}(\tau) & =\Omega\left(\frac{\partial^{2} J_{\mathcal{X}}}{\partial \tau_{\beta} \partial \tau_{\gamma}}(\sigma+\tau), \frac{\partial J_{\mathcal{X}}}{\partial \tau_{\alpha}}(\sigma+\tau)\right) \\
& =\sum_{d \in \operatorname{Eff}(\mathcal{X})} \sum_{n \geq 0}\left\langle\phi_{\beta}, \phi_{\gamma}, \sigma+\tau, \ldots, \sigma+\tau, \phi_{\alpha}\right\rangle_{0, n+3, d}^{\mathcal{X}} \\
& =\frac{\partial^{3} F_{\mathcal{X}}}{\partial \tau_{\alpha} \partial \tau_{\beta} \partial \tau_{\gamma}}(\sigma+\tau)
\end{aligned}
$$

Thus the product $\circ_{\tau}$ on the Frobenius manifold is a shifted version of the big quantum product for $\mathcal{X}$ :

$$
v \circ_{\tau} w=v \underset{\sigma+\tau}{\star} w .
$$

We have proved:

Proposition 6.14. The Frobenius manifold produced from $\mathcal{L}_{\mathcal{X}} \subset \mathcal{H}_{\mathcal{X}}$ by choosing $x=\mathcal{L}_{\mathcal{X}} \cap\left(-z+\sigma+\mathcal{H}_{\mathcal{X}}^{-}\right)$, where $\sigma \in H_{\mathrm{CR}}^{\bullet}(\mathcal{X} ; \Lambda)$, and $\mathcal{H}^{\mathrm{opp}}=\mathcal{H}_{\mathcal{X}}^{-}$ is the Frobenius manifold corresponding to the quantum cohomology of $\mathcal{X}$ with the product 'shifted' by $\sigma$. It has flat metric given by the orbifold Poincaré pairing $(\cdot, \cdot)_{\mathcal{X}}$ and product given by the shifted big quantum product (35). In particular, choosing $\sigma=0$ gives the usual quantum cohomology Frobenius manifold for $\mathcal{X}$.

For later use, we note a stronger version of proposition 6.3

Proposition 6.15. For all $\tau \in N_{0}(\mathcal{X})$, the elements

$$
\frac{\partial J_{\mathcal{X}}}{\partial \tau_{a}}(\tau,-z) \quad a=0,1, \ldots, N
$$

form a $\Lambda[z]$-basis for $T_{J_{\mathcal{X}}(\tau,-z)}$.

Proof. Every element of $T_{J_{\mathcal{X}}(\tau,-z)}$ can be uniquely written in the form $h_{+}+h_{-}$for $h_{+} \in \mathcal{H}_{\mathcal{X}}^{+}, h_{-} \in \mathcal{H}_{\mathcal{X}}^{-}$. The element $h_{+}$is a polynomial in $z$. Since $\frac{\partial J_{\mathcal{X}}}{\tau_{a}}(\tau,-z)=$ $\phi_{a}+h_{-}^{\prime}$ for some $h_{-}^{\prime} \in \mathcal{H}_{\mathcal{X}}^{-}$, since $\left\{\phi_{a}\right\}$ is a $\Lambda$-basis for $H_{\mathrm{CR}}^{\bullet}(\mathcal{X} ; \Lambda)$, and since $T_{J_{\mathcal{X}}(\tau,-z)}$ is closed under multiplication by $z$, the result follows by induction on the degree of $h_{+}$.

We will also need to know the behaviour of $J_{\mathcal{X}}(\tau,-z)$ as $\tau$ approaches the large radius limit point of $\mathcal{X}$.

Proposition 6.16. Write $\tau=\tau_{\text {two }}+\tau_{\text {rest }}$, as in (7). As $\tau$ approaches the large radius limit point for $\mathcal{X}$,

$$
\begin{array}{cl}
\operatorname{Re} \tau_{i} \rightarrow-\infty, & 1 \leq i \leq s \\
\tau_{i} \rightarrow 0, & i=0 \text { and } s<i \leq N
\end{array}
$$

$J_{\mathcal{X}}(\tau,-z) \rightarrow-z \mathrm{e}^{-\tau_{\text {two }} / z}$ and the tangent space $T_{J_{\mathcal{X}}(\tau,-z)} \rightarrow \mathrm{e}^{-\tau_{\text {two }} / z} \mathcal{H}_{\mathcal{X}}^{+}$.

Proof. Look at proposition 6.13. As $\tau$ approaches the large radius limit point, all terms in $J_{\mathcal{X}}(\tau,-z)$ with $d \neq 0$ and all terms involving $\tau_{\text {rest }}$ vanish. Thus

$$
J_{\mathcal{X}}(\tau,-z) \rightarrow-z \mathrm{e}^{-\tau_{\mathrm{two}} / z} \quad \text { and } \quad \frac{\partial J_{\mathcal{X}}}{\partial \tau_{a}}(\tau,-z) \rightarrow \phi_{a} \mathrm{e}^{-\tau_{\mathrm{two}} / z}
$$

As $T_{J_{\mathcal{X}}(\tau,-z)}$ is the $\Lambda[z]$-span of $\left\{\frac{\partial J_{\mathcal{X}}}{\partial \tau_{a}}(\tau,-z): 0 \leq a \leq N\right\}$, it follows that

$$
T_{\mathcal{J}_{\mathcal{X}}(\tau,-z)} \rightarrow \mathrm{e}^{-\tau_{\text {two }} / z} \mathcal{H}_{\mathcal{X}}^{+}
$$

6.5. Example: the Modified Quantum Cohomology of $Y$. We now show that, as one might expect, the Frobenius manifold constructed from $\mathcal{L}_{Y} \subset \mathcal{H}_{Y}$ by choosing $ x \in \mathcal{L}_{Y} \cap\left(-z+z \mathcal{H}_{Y}^{-}\right)$ and $\mathcal{H}^{\text {opp }}=\mathcal{H}_{Y}^{-}$ is the Frobenius manifold based on the modified big quantum product $\circledast$ for $Y$. The argument is very similar to that in the previous section, but there are some additional complications caused by our having made the substitution

$$
Q_{i}= \begin{cases}U_{i} & 1 \leq i \leq s \\ 1 & s<i \leq r\end{cases}
$$

Set $t=t_{\alpha} \varphi_{\alpha}$ and let $t_{\mathrm{two}}$ and $t_{\text {rest }}$ be as in (7). Consider the element $J_{Y}^{\circledast}(t,-z)$ of $\mathcal{L}_{Y}$ such that its projection to $\mathcal{H}_{Y}^{+}$along $\mathcal{H}_{Y}^{-}$is equal to $-z+t$. This is the modified $J$-function of $Y$. It is obtained by setting $t_{0, a}=t_{a}, 0 \leq a \leq N ; t_{k, a}=0$, $0 \leq a \leq N, 0<k<\infty ;$ and

$$
p_{l, b}=\left.\frac{\partial \mathcal{F}_{Y}^{0}}{\partial t_{l, b}}\right|_{\mathbf{t}(z)=t}=\sum_{d \in \operatorname{Eff}(Y)} \sum_{n \geq 0}\left\langle t, \ldots, t, \varphi_{b} \psi^{l}\right\rangle_{0, n+1, d}^{Y} \frac{Q^{d}}{n!}
$$

in (14), and then making the substitution (36). Before making the substitution (36) we have

$$
-z+t+\sum_{d \in \operatorname{Eff}(Y)} \sum_{n \geq 0}\left\langle t, \ldots, t, \frac{\varphi_{\epsilon}}{-z-\psi}\right\rangle_{0, n+1, d}^{Y} \frac{Q^{d} \varphi^{\epsilon}}{n!}
$$

and using the Divisor Equation, as in proposition[6.13 we can write this as

$$
\begin{aligned}
& \mathrm{e}^{-t_{\mathrm{tw}} / z}\left(-z+t_{\text {rest }}+\right. \\
& \left.\quad \sum_{d \in \operatorname{Eff}(Y)} \sum_{n \geq 0}\left\langle t_{\text {rest }}, \ldots, t_{\mathrm{rest}}, \frac{\varphi_{\epsilon}}{-z-\psi}\right\rangle_{0, n+1, d}^{Y} \frac{Q^{d \mathrm{e}^{d_{1} t_{1}} \cdots \mathrm{e}^{d_{r} t_{r}} \varphi^{\epsilon}}}{n!}\right)
\end{aligned}
$$

Thus

$$
\begin{aligned}
& J_{Y}^{\circledast}(t,-z)=\mathrm{e}^{-t_{\mathrm{two}} / z}\left(-z+t_{\mathrm{rest}}+\right. \\
& \left.\quad \sum_{d \in \mathrm{Eff}(Y)} \sum_{n \geq 0}\left\langle t_{\mathrm{rest}}, \ldots, t_{\mathrm{rest}}, \frac{\varphi_{\epsilon}}{-z-\psi}\right\rangle_{0, n+1, d}^{Y} \frac{U_{1}^{d_{1}} \cdots U_{s}^{d_{s}} \mathrm{e}^{d_{1} t_{1}} \cdots \mathrm{e}^{d_{r} t_{r}} \varphi^{\epsilon}}{n!}\right)
\end{aligned}
$$

where $d=d_{1} \beta_{1}+\cdots+d_{r} \beta_{r}$. The modified $J$-function $J_{Y}^{\circledast}(t,-z)$ is an element of $\mathcal{L}_{Y}$ which depends formally on the variables $t_{0}, t_{r+1}, t_{r+2}, \ldots, t_{N}$ and analytically on $t_{1}, \ldots, t_{r}$ in the domain (12). It is the unique element of $\mathcal{L}_{Y}$ of the form

$$
-z+t+h_{-}(t) \quad \text { with } h_{-}(t) \in \mathcal{H}_{Y}^{-}
$$

The Frobenius manifold we seek is based on a formal neighbourhood $ N_{0}(Y)$ of the origin in $ z \mathcal{H}_{Y}^{-} / \mathcal{H}_{Y}^{-} \cong H^{\bullet}(Y ; \Lambda)$. Choose a point $x \in \mathcal{L}_{Y} \cap\left(-z+z \mathcal{H}_{Y}^{-}\right)$ and
write $ x=-z+s+h_{-}^{\prime}$ with $s \in H^{\bullet}(Y ; \Lambda)$ and $h_{-}^{\prime} \in \mathcal{H}_{Y}^{-}$. Then the map $p$ defined in (31) satisfies

$$
p \circ J_{Y}^{\circledast}(s+t,-z)=t
$$

and so the map $J$ defined in (32) is

$$
J(t)=J_{Y}^{\circledast}(s+t,-z)
$$

Now, using the co-ordinates $t_{0}, \ldots, t_{N}$ given by the basis $\varphi_{0}, \ldots, \varphi_{N}$ for $H \bullet(Y ; \Lambda)$ and arguing exactly as in $\sqrt{6}$ (d), we find that the flat metric on $N_{0}(Y)$ is given by the Poincaré pairing:

$$
g_{\alpha \beta}(t)=\left(\varphi_{\alpha}, \varphi_{\beta}\right)_{Y}
$$

and that the structure constants of the product $\circ_{\tau}$ are

$$
c_{\alpha \beta \gamma}(t)=\frac{\partial^{3} F_{Y}^{\circledast}}{\partial t_{\alpha} \partial t_{\beta} \partial t_{\gamma}}(s+t)
$$

Thus the product $\circ_{\tau}$ on the Frobenius manifold $N_{0}(Y)$ is a shifted version of the modified big quantum product for $Y$ :

$$
v \circ_{t} w=v \underset{s+t}{\circledast} w
$$

We have proved:

Proposition 6.17. The Frobenius manifold produced from $\mathcal{L}_{Y} \subset \mathcal{H}_{Y}$ by choosing $x=\mathcal{L}_{Y} \cap\left(-z+s+\mathcal{H}_{Y}^{-}\right)$, for some $s \in H^{\bullet}(Y ; \Lambda)$, and $\mathcal{H}^{\text {opp }}=\mathcal{H}_{Y}^{-}$is the Frobenius manifold corresponding to the modified quantum cohomology of $Y$ with the product 'shifted' by s. It has flat metric given by the Poincaré pairing $(\cdot, \cdot)_{Y}$ and product given by (37).

Remark 6.18. We now explain why condition (c) in conjecture 4.1 ensures that there is a neighbourhood of the large-radius limit point for $\mathcal{X}$ in which both the big quantum product $\star$ for $\mathcal{X}$ and the analytic continuation of the modified big quantum product $\circledast$ for $Y$ are well-defined. Let us write $V_{1} \pitchfork V_{2}$ if and only if $V_{1} \oplus V_{2}=\mathcal{H}_{\mathcal{X}}$, so that condition (c) is the assertion $\mathcal{H}_{\mathcal{X}}^{+} \pitchfork \mathbb{U}^{-1}\left(\mathcal{H}_{Y}^{-}\right)$. In $\S \underline{6}(\mathrm{~d})$ we saw that by choosing $x \in \mathcal{L}_{\mathcal{X}}$ of the form $x=-z+\sigma+h_{-}$, where $\sigma \in$ $H_{\mathrm{CR}}^{\bullet}(\mathcal{X} ; \Lambda)$ and $h_{-} \in \mathcal{H}_{\mathcal{X}}^{-}$, and taking opposite subspace $\mathcal{H}^{\text {opp }}=\mathcal{H}_{\mathcal{X}}^{-}$ we obtain a Frobenius manifold with product a shifted version of the big quantum product for $\mathcal{X}: v \circ_{\tau} w=v{ }_{\sigma+\tau}^{\star} w$. Suppose now that conjecture 4.1 holds. In proposition 6.17 we saw that by choosing $y \in \mathcal{L}_{Y}$ of the form $-z+s+h_{-}^{\prime}$, where $s \in H^{\bullet}(Y ; \Lambda)$ and $h_{-}^{\prime} \in \mathcal{H}_{Y}^{-}$, and taking opposite subspace $\mathcal{H}^{\text {opp }}=\mathcal{H}_{Y}^{-}$we obtain a Frobenius manifold with product $v \circ_{t} w=v \underset{s+t}{\circledast} w$. The analytic continuation of $\mathcal{L}_{Y}$ chosen as part of conjecture 4.1 defines, via proposition 6.17 an analytic continuation of the product $\underset{s+t}{\circledast}$. (Here we analytically continue $\underset{s+t}{\circledast}$ in $s$; the variable $s$ determines and is determined by the basepoint $y=-z+s+h_{-}^{\prime} \in \mathcal{L}_{Y}$.) We can obtain this analytically continued product either by choosing $y$ in the analytic continuation of $\mathcal{L}_{Y}$ and taking opposite subspace $\mathcal{H}^{\text {opp }}=\mathcal{H}_{Y}^{-}$or - and this is equivalent via $y=\mathbb{U}(x)$ - by choosing $x \in \mathcal{L}_{\mathcal{X}}$ and taking opposite subspace $\mathcal{H}^{\text {opp }}=\mathbb{U}^{-1}\left(\mathcal{H}_{Y}^{-}\right)$. For this to give a Frobenius manifold, we need $\mathbb{U}\left(\mathcal{H}_{Y}^{-}\right)$to be opposite to $T_{x}=T_{x} \mathcal{L}_{\mathcal{X}}$; in other words we need $T_{x} \pitchfork \mathbb{U}^{-1}\left(\mathcal{H}_{Y}^{-}\right)$. Let $x=\mathcal{L}_{\mathcal{X}} \cap\left(-z+\sigma+\mathcal{H}_{\mathcal{X}}^{-}\right)$. We know from proposition 6.16 that as $\sigma$ approaches the large-radius limit point for $\mathcal{X}$,

$$
T_{x} \rightarrow \mathrm{e}^{-\sigma_{\mathrm{two}} / z} \mathcal{H}_{\mathcal{X}}^{+} . \text {But }
$$

$$
\begin{aligned}
\left(\mathrm{e}^{-\sigma_{\mathrm{two}} / z} \mathcal{H}_{\mathcal{X}}^{+}\right) \pitchfork \mathbb{U}^{-1}\left(\mathcal{H}_{Y}^{-}\right) & \Longleftrightarrow \mathcal{H}_{\mathcal{X}}^{+} \pitchfork \mathrm{e}^{\sigma_{\mathrm{two}} / z} \mathbb{U}^{-1}\left(\mathcal{H}_{Y}^{-}\right) \\
& \Longleftrightarrow \mathcal{H}_{\mathcal{X}}^{+} \pitchfork \mathbb{U}^{-1}\left(\mathrm{e}^{\pi^{\star} \sigma_{\mathrm{two}} / z} \mathcal{H}_{Y}^{-}\right) \\
& \Longleftrightarrow \mathcal{H}_{\mathcal{X}}^{+} \pitchfork \mathbb{U}^{-1}\left(\mathcal{H}_{Y}^{-}\right)
\end{aligned}
$$

and this holds by conjecture 4.1(c). Thus for $\sigma$ in a neighbourhood of the largeradius limit point for $\mathcal{X}, T_{x} \pitchfork \mathbb{U}^{-1}\left(\mathcal{H}_{Y}^{-}\right)$ and so both the Frobenius manifold defined by the big quantum product for $\mathcal{X}$ (basepoint $=x \in \mathcal{L}_{\mathcal{X}}, \mathcal{H}^{\text {opp }}=\mathcal{H}_{\mathcal{X}}^{-}$) and the Frobenius manifold defined by the analytic continuation of the modified big quantum product for $Y\left(\right.$ basepoint $\left.=x, \mathcal{H}^{\text {opp }}=\mathbb{U}^{-1}\left(\mathcal{H}_{Y}^{-}\right)\right)$ are well-defined.

## 7. A Version of the Cohomological Crepant Resolution Conjecture

The Cohomological Crepant Resolution Conjecture [32] describes a relationship between the Chen-Ruan cohomology ring of $\mathcal{X}$ and the small quantum cohomology ring of the crepant resolution $Y$. Conjecture 4.1 implies such a relationship, as we now explain. The family of Frobenius algebras constructed in $9 \underline{6}$ (a) depends only on the submanifold-germ $\mathcal{L}_{\mathcal{Z}}$ and the symplectic space $\mathcal{H}_{\mathcal{Z}}$. The transformation $\mathbb{U}$ from conjecture 4.1, which is a $\mathbb{C}((z))$-linear symplectic isomorphism and satisfies $\mathbb{U}\left(\mathcal{L}_{\mathcal{Z}}\right)=\mathcal{L}_{Y}$, therefore induces an isomorphism between the families of Frobenius algebras

$$
T \mathcal{L}_{\mathcal{X}} / z T \mathcal{L}_{\mathcal{X}} \rightarrow \mathcal{L}_{\mathcal{X}} \quad \text { and } \quad T \mathcal{L}_{Y} / z T \mathcal{L}_{Y} \rightarrow \mathcal{L}_{Y}
$$

By choosing $x \in \mathcal{L}_{\mathcal{X}}$ appropriately - by taking $x=\mathcal{L}_{\mathcal{X}} \cap\left(-z+\sigma+\mathcal{H}_{\mathcal{X}}^{-}\right)$and letting $\sigma$ approach the large-radius limit point for $\mathcal{X}$ - we can obtain the ChenRuan cohomology of $\mathcal{X}$ as the Frobenius algebra $T_{x} / z T_{x}$. Let $y \in \mathcal{L}_{Y}$ be such that $y=\mathbb{U}(x)$, and let $T_{y}$ denote the tangent space $T_{y} \mathcal{L}_{Y}$. Then $\mathbb{U}$ induces an isomorphism of Frobenius algebras $T_{x} / z T_{x} \cong T_{y} / z T_{y}$, and this expresses the ChenRuan cohomology ring of $\mathcal{X}$ in terms of the quantum cohomology of $Y$.

Let $\sigma \in H^{2}(\mathcal{X} ; \mathbb{C})$ and let $x=\mathcal{L}_{\mathcal{X}} \cap\left(-z+\sigma+\mathcal{H}_{\mathcal{X}}^{-}\right)$. Then $T_{x} / z T_{x}$ is isomorphic as a Frobenius algebra to the quantum cohomology of $\mathcal{X},\left(H_{\mathrm{CR}}^{\bullet}(\mathcal{X} ; \Lambda),{ }_{\sigma}^{\star}\right)$. As $\sigma$ approaches the large-radius limit point for $\mathcal{X}$, therefore, $T_{x} / z T_{x}$ approaches the Chen-Ruan cohomology ring $\left(H_{\mathrm{CR}}^{\bullet}(\mathcal{X} ; \Lambda), \cup \mathrm{CR}\right)-$ see the discussion below equation 8 , Let $y=\mathbb{U}(x)$.

Proposition 7.1. As $\sigma$ approaches the large-radius limit point for $\mathcal{X}$

$$
y \rightarrow J_{Y}\left(\pi^{\star} \sigma+c,-z\right)
$$

where $\mathbb{U}\left(\mathbf{1}_{\mathcal{X}}\right)=\mathbf{1}_{Y}-c z^{-1}+O\left(z^{-2}\right)$.

Proof. We have $x=J_{\mathcal{X}}(\sigma,-z)$ so, by proposition 6.16, $x \rightarrow-z \mathrm{e}^{-\sigma / z}$ as $\sigma$ approaches the large-radius limit point for $\mathcal{X}$. Thus

$$
\begin{aligned}
y & \rightarrow \mathbb{U}\left(-z \mathrm{e}^{-\sigma / z}\right) & & \\
& =-z \mathrm{e}^{\pi^{\star} \sigma / z} \mathbb{U}\left(\mathbf{1}_{\mathcal{X}}\right) & & \text { by conjecture } 4.1(\mathrm{~b}) \\
& =-z+\pi^{\star} \sigma+c+h_{-} & & \text {for some } h_{-} \in \mathcal{H}_{\mathcal{X}}^{-}
\end{aligned}
$$

There is a unique point on $\mathcal{L}_{Y}$ of the form $-z+\pi^{\star} \sigma+c+h_{-}, h_{-} \in \mathcal{H}_{\mathcal{X}}^{-}$, and that is $J_{Y}\left(\pi^{\star} \sigma+c,-z\right)$. Thus as $\sigma$ approaches the large-radius limit point for $\mathcal{X}$, $y \rightarrow J_{Y}\left(\pi^{\star} \sigma+c,-z\right)$.

It follows that as $\sigma$ approaches the large-radius limit point for $\mathcal{X}$,

$$
\operatorname{Re} \sigma_{i} \rightarrow-\infty, \quad 1 \leq i \leq s
$$

the Frobenius algebra $T_{y} / z T_{y}$ approaches the quantum cohomology algebra

$$
\lim _{\substack{\operatorname{Re} \sigma_{i} \rightarrow-\infty \\ 1 \leq i \leq s}}\left(H^{\bullet}(Y ; \Lambda), \underset{\pi^{*} \sigma+c}{\circledast}\right) .
$$

By assumption $\mathbb{U}$ is grading preserving and so $c \in H^{2}(Y ; \mathbb{C})$; let us write $c=$ $c_{1} \varphi_{1}+\ldots+c_{r} \varphi_{r}$. Note that there is analytic continuation hidden in (39): if $t=t_{1} \varphi_{1}+\ldots+t_{r} \varphi_{r} \in H^{2}(Y ; \mathbb{C})$ then the product $\circledast$ is defined as a power series (13) which converges only when $\left|\mathrm{e}^{t_{i}}\right|<R_{i}, s<i \leq r$. In general $t=\pi^{\star} \sigma+c$ will be outside this domain of convergence. But the analytic continuation of $\mathcal{L}_{Y}$ defines, via proposition 6.17, an analytic continuation of the product $\circledast$ and it is this analytically-continued product which we use in (39). We compute the limit (39) as follows. From (13) we have

$\varphi_{\alpha} \underset{t}{*} \varphi_{\beta}=\sum_{\substack{d \in \operatorname{Eff}(Y): \\ d=d_{1} \beta_{1}+\cdots+d_{r} \beta_{r}}}\left\langle\varphi_{\alpha}, \varphi_{\beta}, \varphi^{\epsilon}\right\rangle_{0,3, d}^{Y} U_{1}^{d_{1}} \cdots U_{s}^{d_{s}} \mathrm{e}^{d_{1} t_{1}} \cdots \mathrm{e}^{d_{r} t_{r}} \varphi_{\epsilon}$

whenever $\left|\mathrm{e}^{t_{i}}\right|<R_{i}$ for $s<i \leq r ;$ taking the limit $\operatorname{Re} t_{i} \rightarrow-\infty, 1 \leq i \leq s$, gives

$$
\varphi_{\alpha} \underset{t}{\circledast} \varphi_{\beta} \rightarrow \sum_{\substack{d \in \operatorname{ker} \pi_{*}: \\ d=d_{s+1} \beta_{s+1}+\cdots+d_{r} \beta_{r}}}\left\langle\varphi_{\alpha}, \varphi_{\beta}, \varphi^{\epsilon}\right\rangle_{0,3, d}^{Y} \mathrm{e}^{d_{s+1} t_{s+1}} \cdots \mathrm{e}^{d_{r} t_{r}} \varphi_{\epsilon}
$$

We can obtain the algebra (39) which we seek from (40) by analytic continuation in $t_{s+1}, \ldots, t_{r}$ followed by the substitution $t_{i}=c_{i}, s<i \leq r$. This proves:

Theorem 7.2. If conjecture 4.1 holds then the Chen-Ruan product $\bigcup_{C R}$ on $H_{\mathrm{CR}}^{\bullet}(\mathcal{X} ; \mathbb{C})$ can be obtained from the small quantum product (6) for $Y$ by analytic continuation in the quantum parameters $Q_{s+1}, \ldots, Q_{r}$ (if necessary) followed by the substitution

$$
Q_{i}= \begin{cases}0 & 1 \leq i \leq s \\ \mathrm{e}^{c_{i}} & s<i \leq r\end{cases}
$$

The small quantum cohomology with quantum parameters $Q_{i}$ specialized like this is known as quantum corrected cohomology [32]. In Ruan's original Cohomological Crepant Resolution Conjecture, the exceptional $Q_{i}$ were specialized to -1 . Calculations by Perroni [31] and Bryan-Graber-Pandharipande [8] have shown that we must relax this, allowing the exceptional $Q_{i}$ to be specialized to other roots of unity. Here, we allow arbitrary choice. It should be noted that the specialization $Q_{i}=\mathrm{e}^{c_{i}}=\mathrm{e}^{\left\langle c, \beta_{i}\right\rangle}$ is independent of our choice of bases (see $\$ 11$ for more on this).

## 8. A Version of Ruan's Conjecture

Ruan's original Crepant Resolution Conjecture (implicit in 32), as modified in light of the calculations of Perroni and Bryan-Graber-Pandharipande, was that the small quantum cohomology algebra of the crepant resolution $Y$ becomes isomorphic to the small quantum cohomology algebra of $\mathcal{X}$ after analytic continuation in the quantum parameters $Q_{s+1}, \ldots, Q_{r}$ followed by a change-of-variables

$$
Q_{i}= \begin{cases}\omega_{i} U_{i} & 1 \leq i \leq s \\ \omega_{i} & s<i \leq r\end{cases}
$$

where the $\omega_{i}$ are roots of unity. Conjecture 4.1 implies something very like this, at least when $\mathcal{X}$ is semi-positive, as we now explain.

Definition. A Kähler orbifold $\mathcal{X}$ is called semi-positive if and only if there does not exist $d \in \operatorname{Eff}(\mathcal{X})$ such that

$$
3-\operatorname{dim}_{\mathbb{C}} \mathcal{X} \leq c_{1}(T \mathcal{X}) \cdot d<0
$$

All Kähler orbifolds of complex dimension 3 or less are semi-positive, as are all Fano and Calabi-Yau orbifolds. Semi-positive Gorenstein orbifolds $\mathcal{X}$ have the property that if $c_{1}(T \mathcal{X}) \cdot d<0$ then all genus-zero Gromov-Witten invariants in degree $d$ vanish:

Proposition 8.1. Suppose that $\mathcal{X}$ is a semi-positive Gorenstein Kähler orbifold and that $\left\langle\delta_{1} \psi^{a_{1}}, \ldots, \delta_{n} \psi^{a_{n}}\right\rangle_{0, n, d}^{\mathcal{X}} \neq 0$. Then $c_{1}(T \mathcal{X}) \cdot d \geq 0$.

Proof. Suppose not, so that $c_{1}(T \mathcal{X}) \cdot d<0$. Without loss of generality we may assume that the marked points $1,2, \ldots, n^{\prime}$ carry classes $\delta_{i}$ from the twisted sectors and that the remaining marked points carry untwisted classes. Let $\pi: \mathcal{X}_{0, n, d} \rightarrow$ $\mathcal{X}_{0, n^{\prime}, d}$ be the map induced by forgetting all the untwisted marked points. Then $\left\langle\delta_{1} \psi^{a_{1}}, \ldots, \delta_{n} \psi^{a_{n}}\right\rangle_{0, n, d}^{\mathcal{X}}$ is the degree-zero part of

$$
\left[\mathcal{X}_{0, n^{\prime}, d}\right]^{\mathrm{vir}} \cap\left(\prod_{k=1}^{n^{\prime}} \mathrm{ev}_{k}^{\star} \delta_{k}\right) \cup \pi_{\star}\left(\prod_{k=n^{\prime}+1}^{n} \mathrm{ev}_{k}^{\star} \delta_{k} \cup \prod_{k=1}^{n} \psi_{k}^{a_{k}}\right)
$$

As $\mathcal{X}$ is Gorenstein, we know that $\operatorname{deg} \delta_{k} \geq 1,1 \leq k \leq n^{\prime}$, where deg denotes the age-shifted degree on $H_{\mathrm{CR}}^{\bullet}(\mathcal{X} ; \mathbb{C})$. The non-vanishing of (43) therefore implies that the virtual (complex) dimension of $\mathcal{X}_{0, n^{\prime}, d}$ is at least $n^{\prime}$, and so

$$
n^{\prime}+\operatorname{dim}_{\mathbb{C}} \mathcal{X}-3+c_{1}(T \mathcal{X}) \cdot d \geq n^{\prime}
$$

It follows that

$$
3-\operatorname{dim}_{\mathbb{C}} \mathcal{X} \leq c_{1}(T \mathcal{X}) \cdot d<0
$$

which contradicts semi-positivity. The proposition is proved.

The small quantum cohomology of $\mathcal{X}$ is the Frobenius algebra $\left(H_{\mathrm{CR}}^{\bullet}(\mathcal{X} ; \Lambda), \star\right)$ at $\tau=0$. This is the Frobenius algebra $T_{x} / z T_{x}$ where $x=\mathcal{L}_{\mathcal{X}} \cap\left(-z+\mathcal{H}_{\mathcal{X}}^{-}\right)$and $T_{x}=T_{x} \mathcal{L}_{\mathcal{X}}$. Let $y=\mathbb{U}(x)$ and $T_{y}=T_{y} \mathcal{L}_{Y}$. The map $\mathbb{U}$ induces an isomorphism between the Frobenius algebras $T_{x} / z T_{x}$ and $T_{y} / z T_{y}$, and this isomorphism expresses the small quantum cohomology of $\mathcal{X}$ in terms of the quantum cohomology of $Y$. To see that it relates the small quantum cohomology of $\mathcal{X}$ to the small quantum cohomology of $Y$, we need to calculate $y$.

Proposition 8.2. Suppose that $\mathcal{X}$ is semi-positive and that conjecture 4.1 holds. Let $x=\mathcal{L}_{\mathcal{X}} \cap\left(-z+\mathcal{H}_{\mathcal{X}}^{-}\right)$, and define $c \in H^{2}(Y ; \mathbb{C})$ by $\mathbb{U}\left(\mathbf{1}_{\mathcal{X}}\right)=\mathbf{1}_{Y}-c z^{-1}+O\left(z^{-2}\right)$. Then there is a unique element $f \in H^{2}(Y ; \mathbb{C}) \otimes \Lambda$,

$$
f=f_{1} \varphi_{1}+\cdots+f_{r} \varphi_{r} \quad \text { for some } f_{1}, \ldots, f_{r} \in \Lambda
$$

such that $\mathbb{U}(x)=J_{Y}(c+f,-z)$. Furthermore, the class $f$ is exceptional: $\pi_{!} f=0$.

Proof. Uniqueness is obvious. For existence, we need to find $f \in H^{2}(Y ; \mathbb{C}) \otimes \Lambda$ such that

$$
\mathbb{U}(x)=-z+c+f+h_{-}
$$

for some $h_{-} \in \mathcal{H}_{Y}^{-}$. We have $x=J_{\mathcal{X}}(0,-z)$, so

$$
x=-z+\sum_{\substack{d \in \operatorname{Eff}(\mathcal{X}): \\ d \neq 0}} \sum_{k \geq 0}(-1)^{k+1}\left\langle\phi^{\epsilon} \psi^{k}\right\rangle_{0,1, d}^{\mathcal{X}} U^{d} \phi_{\epsilon} z^{-k-1}
$$

If we set $\operatorname{deg} U^{d}=c_{1}(T \mathcal{X}) \cdot d, \operatorname{deg} z=2$, and give the Chen-Ruan class $\phi_{\epsilon}$ its ageshifted degree then $x \in \mathcal{H}_{\mathcal{X}}$ is homogeneous of degree two. As $\mathcal{X}$ is semi-positive,
any monomial $U^{d}$ which occurs in (45) has non-negative degree, and so each term $\phi_{\epsilon} z^{-k-1}$ in (45) has degree at most two. If $\phi_{\epsilon} z^{-k-1}$ is of negative degree then $\mathbb{U}\left(\phi_{\epsilon} z^{-k-1}\right)$ is also of negative degree and so $\mathbb{U}\left(\phi_{\epsilon} z^{-k-1}\right) \in \mathcal{H}_{Y}^{-}$. If $\phi_{\epsilon} z^{-k-1}$ is of degree zero or one then, by parts (a) and (b) of lemma 5.1 $\mathbb{U}\left(\phi_{\epsilon} z^{-k-1}\right) \in \mathcal{H}_{Y}^{-}$as well. If $\phi_{\epsilon} z^{-k-1}$ is of degree two then

$$
\mathbb{U}\left(\phi_{\epsilon} z^{-k-1}\right)=b_{\epsilon}+h_{\epsilon}
$$

for some exceptional class $b_{\epsilon} \in H^{2}(Y ; \mathbb{C})$ and some $h_{\epsilon} \in \mathcal{H}_{Y}^{-}$, by lemma 5.1(c). Also, if $\phi_{\epsilon} z^{-k-1}$ is of degree two then $\operatorname{deg} \phi_{\epsilon} \geq 4$ and $k=\frac{1}{2} w_{\epsilon}-2$ where $w_{\epsilon}=\operatorname{deg} \phi_{\epsilon}$. Thus

$$
\mathbb{U}(x)=-z+c+\sum_{\substack{d \in \operatorname{Eff}(\mathcal{X}): d \neq 0, c_{1}(T \mathcal{X}) \cdot d=0}} \sum_{e=r+1}^{N}(-1)^{\frac{1}{2} w_{e}+1}\left\langle\phi^{e} \psi^{\frac{1}{2} w_{e}-2}\right\rangle_{0,1, d}^{\mathcal{X}} U^{d} b_{e}+h_{-}
$$

for some $h_{-} \in \mathcal{H}_{Y}^{-}$. Defining

$$
f=\sum_{\substack{d \in \operatorname{Eff}(\mathcal{X}): d \neq 0, c_{1}(T \mathcal{X}) \cdot d=0}} \sum_{e=r+1}^{N}(-1)^{\frac{1}{2} w_{e}+1}\left\langle\phi^{e} \psi^{\frac{1}{2} w_{e}-2}\right\rangle_{0,1, d}^{\mathcal{X}} U^{d} b_{e}
$$

we are done.

We have seen that the small quantum cohomology of $\mathcal{X}$ is isomorphic as a Frobenius algebra to $T_{y} / z T_{y}$ where $y=\mathbb{U}(x)$. Proposition 8.2 shows that $T_{y} / z T_{y}$ is isomorphic as a Frobenius algebra to

$$
\left(H^{\bullet}(Y ; \Lambda), \underset{c+f}{\circledast}\right)
$$

Once again there is analytic continuation hidden here: the product $\underset{c+f}{\circledast}$ is obtained from the product

$$
\varphi_{\alpha} \underset{t}{\circledast} \varphi_{\beta}=\sum_{\substack{d \in \operatorname{Eff}(Y): \\ d=d_{1} \beta_{1}+\cdots+d_{r} \beta_{r}}}\left\langle\varphi_{\alpha}, \varphi_{\beta}, \varphi^{\epsilon}\right\rangle_{0,3, d}^{Y} U_{1}^{d_{1}} \cdots U_{s}^{d_{s}} \mathrm{e}^{d_{1} t_{1}} \cdots \mathrm{e}^{d_{r} t_{r}} \varphi_{\epsilon}
$$

where $t=t_{1} \varphi_{1}+\cdots+t_{r} \varphi_{r} \in H^{2}(Y ; \mathbb{C})$ and $\left|\mathrm{e}^{t_{i}}\right|<R_{i}$ for $s<i \leq r$, by analytic continuation in $t_{s+1}, \ldots, t_{r}$ followed by the substitution

$$
t_{i}=c_{i}+f_{i} \quad 1 \leq i \leq r
$$

where $f=f_{1} \varphi_{1}+\cdots+f_{r} \varphi_{r}$. This proves:

Theorem 8.3. Suppose that $\mathcal{X}$ is semi-positive and that conjecture 4.1 holds. Let $f_{1}, \ldots, f_{r} \in \mathbb{C} \llbracket U_{1}, \ldots, U_{s} \rrbracket$ be as in proposition 8.2 and define $c=c_{1} \varphi_{1}+\cdots+c_{r} \varphi_{r} \in$ $H^{2}(Y ; \mathbb{C})$ by $\mathbb{U}\left(\mathbf{1}_{\mathcal{X}}\right)=\mathbf{1}_{Y}-c z^{-1}+O\left(z^{-2}\right)$. Then the Frobenius algebra given by the small quantum cohomology of $\mathcal{X}$ is isomorphic to the Frobenius algebra obtained from the small quantum cohomology of $Y$ by analytic continuation in the exceptional quantum parameters $Q_{s+1}, \ldots, Q_{r}$ (if necessary) followed by the change-of-variables

$$
Q_{i}= \begin{cases}\mathrm{e}^{c_{i}+f_{i}} U_{i} & 1 \leq i \leq s \\ \mathrm{e}^{c_{i}+f_{i}} & s<i \leq r\end{cases}
$$

The conclusion of Theorem 8.3 is almost Ruan's original Crepant Resolution Conjecture, except that the changes-of-variables (42) and (47) differ. As $f_{i}=0$ when $U_{1}=\ldots=U_{s}=0$, theorem 8.3 is a 'quantum-corrected' version of Ruan's original conjecture. The quantum corrections $f_{1}, \ldots, f_{r}$ often vanish - for example they vanish whenever $\mathcal{X}$ is Fano or when $\mathcal{X}=\left[\mathbb{C}^{n} / G\right]$, as then the sum on the RHS of (46) is empty. But $f_{1}, \ldots, f_{r}$ do not vanish in general: they are non-zero, for instance, when $\mathcal{X}$ is the cotangent bundle $K_{\mathbb{P}(1,1,3)}$ [12].

## 9. A Version of the Bryan-Graber Conjecture

Suppose now that conjecture 4.1 holds and that $\mathbb{U}: \mathcal{H}_{\mathcal{X}} \rightarrow \mathcal{H}_{Y}$ sends $\mathcal{H}_{\mathcal{X}}^{-}$to $\mathcal{H}_{Y}^{-}$, so that

$$
\mathbb{U}=U_{0}+U_{1} z^{-1}+\cdots+U_{k} z^{-k}
$$

for some non-negative integer $k$ and some linear maps $U_{i}: H_{\mathrm{CR}}^{\bullet}(\mathcal{X} ; \mathbb{C}) \rightarrow H^{\bullet}(Y ; \mathbb{C})$. In this case $\mathbb{U}$ induces an isomorphism between the Frobenius manifolds defined by the quantum cohomology of $\mathcal{X}$ and the quantum cohomology of $Y$, as we now explain.

Let $x=\mathcal{L}_{\mathcal{X}} \cap\left(-z+\mathcal{H}_{\mathcal{X}}^{-}\right)$and let $y=\mathbb{U}(x)$. Then

$$
\begin{aligned}
y & =\mathcal{L}_{Y} \cap \mathbb{U}\left(-z+\mathcal{H}_{\overline{\mathcal{X}}}^{-}\right) \\
& =\mathcal{L}_{Y} \cap\left(-z+c+\mathcal{H}_{Y}^{-}\right)
\end{aligned}
$$

where $\mathbb{U}\left(\mathbf{1}_{\mathcal{X}}\right)=\mathbf{1}_{Y}-c z^{-1}+O\left(z^{-2}\right)$. Again, write $c=c_{1} \varphi_{1}+\cdots+c_{r} \varphi_{r}$. In view of the discussion in ⑥ $\mathbb{U}$ induces an isomorphism between the Frobenius manifold

$$
\left(H_{\mathrm{CR}}^{\bullet}(\mathcal{X} ; \Lambda),{ }_{\tau}^{\star}\right)
$$

obtained by taking basepoint $x \in \mathcal{L}_{\mathcal{X}}$ and using opposite subspace $\mathcal{H}_{\mathcal{X}}^{-}$, and the Frobenius manifold

$$
\left(H^{\bullet}(Y ; \Lambda), \underset{c+t}{\circledast}\right)
$$

obtained by taking basepoint $y \in \mathcal{L}_{Y}$ and using opposite subspace $\mathcal{H}_{Y}^{-}$. The parameters $\tau \in H_{\mathrm{CR}}^{\bullet}(\mathcal{X} ; \Lambda)$ and $t \in H^{\bullet}(Y ; \Lambda)$ here are identified via the diagram



so $t=U_{0}(\tau)$. Comparing (13) with (9), we see that the product $\underset{c+t}{\circledast}$ can be obtained from the big quantum product $\underset{t}{\star}$ on $H^{\bullet}\left(Y ; \Lambda_{Y}\right)$ by analytic continuation in the variables $Q_{s+1}, \ldots, Q_{r}$ followed by the change-of-variables

$$
Q_{i}= \begin{cases}\mathrm{e}^{c_{i}} U_{i} & 1 \leq i \leq s \\ \mathrm{e}^{c_{i}} & s<i \leq r\end{cases}
$$

This proves:

Theorem 9.1. Suppose that conjecture 4.1 holds and that $\mathbb{U}: \mathcal{H}_{\mathcal{X}} \rightarrow \mathcal{H}_{Y}$ sends $\mathcal{H}_{\mathcal{X}}^{-}$ to $\mathcal{H}_{Y}^{-}$. Then there is a linear map $U_{0}: H_{\mathrm{CR}}^{\bullet}(\mathcal{X} ; \mathbb{C}) \rightarrow H^{\bullet}(Y ; \mathbb{C})$ which identifies the Frobenius manifold given by the big quantum cohomology (3) of $\mathcal{X}$ with the Frobenius manifold obtained from the big quantum cohomology (5) of $Y$ by analytic continuation in the quantum parameters $Q_{s+1}, \ldots, Q_{r}$ (if necessary) followed by the substitution (48). In addition, the map $U_{0}$ preserves the gradings and Poincaré pairings, sends $\mathbf{1}_{\mathcal{X}}$ to $\mathbf{1}_{Y}$, and satisfies $U_{0} \circ\left(\rho \cup \cup_{C R}\right)=\left(\pi^{\star} \rho \cup\right) \circ U_{0}$ for every untwisted degree-two class $\rho \in H^{2}(\mathcal{X} ; \mathbb{C})$.

The statements about $U_{0}$ here come from lemma[5.2. As discussed above, if conjecture 4.1 holds and $\mathcal{X}$ satisfies the Hard Lefschetz condition1ㅣㄹ postulated by BryanGraber [7] then $\mathbb{U}$ automatically sends $\mathcal{H}_{\mathcal{X}}^{-}$to $\mathcal{H}_{Y}^{-}$.

The conclusion of Theorem 9.1 is almost the same as the Crepant Resolution Conjecture of Bryan and Graber. They ask that $U_{0}: H_{\mathrm{CR}}^{\bullet}(\mathcal{X} ; \mathbb{C}) \rightarrow H \bullet(Y ; \mathbb{C})$ agree with $\pi^{\star}$ on the untwisted sector $H^{\bullet}(\mathcal{X} ; \mathbb{C}) \subset H_{\mathrm{CR}}^{\bullet}(\mathcal{X} ; \mathbb{C})$, whereas we only have that for the subalgebra of $H^{\bullet}(\mathcal{X} ; \mathbb{C})$ generated by $H^{2}(\mathcal{X} ; \mathbb{C})$. Furthermore their change-of-variables has $Q_{i}=U_{i}, 1 \leq i \leq s$, omitting our factor of $\mathrm{e}^{c_{i}}$, and for us the substitution $Q_{i}=\mathrm{e}^{c_{i}}, s<i \leq r$, need not involve roots of unity)2.

## 10. Quantization and Higher Genus Gromov-Witten Invariants

So far we have considered genus-zero Gromov-Witten invariants of $\mathcal{X}$ and $Y$. This corresponds to considering the tree-level part of the topological A-model with target space $\mathcal{X}$ or $Y$. But the full partition function of the topological A-model is also of significant interest, and this corresponds to the full descendant potential of $\mathcal{X}$,

$$
\mathcal{D}_{\mathcal{X}}=\exp \left(\sum_{g \geq 0} \hbar^{g-1} \mathcal{F}_{\mathcal{X}}^{g}\right)
$$

or, similarly, to the full descendant potential $\mathcal{D}_{Y}$ of $Y$. The quantity $\mathcal{F}_{X}^{g}$ in (49) is the genus- $g$ descendant potential of $\mathcal{X}$ : this is defined in the same way as the genus-zero descendant potential $\mathcal{F}_{\mathcal{X}}^{0}$ but with integration over the moduli stack of stable maps to $\mathcal{X}$ of genus $g$ rather than genus zero. The variable $\hbar$ is a formal parameter. In this section we give a generalization of our conjecture which applies to Gromov-Witten invariants of all genera. Roughly speaking, we conjecture that $\mathcal{D}_{Y}=\widehat{\mathbb{U}}\left(\mathcal{D}_{\mathcal{X}}\right)$, where $\widehat{\mathbb{U}}$ is the quantization of the symplectic transformation $\mathbb{U}$ from conjecture 4.1. This idea occurred simultaneously and independently in both mathematics and physics [1, 13] [33]; it is a consequence of fundamental insights due to Givental [21] and Witten [35].

Work of Givental [15,21,22] and others [18,26,27, 29)|34] strongly suggests that the full descendant potential $\mathcal{D}_{\mathcal{X}}$ of $\mathcal{X}$ should be regarded as an element of the Fock space for the geometric quantization of $\mathcal{H}_{\mathcal{X}}$. This point of view is described for manifolds in 21 and extended to orbifolds in [34. The Fock space for $\mathcal{X}$ consists of certain formal germs of functions on $\mathcal{H}_{\mathcal{X}}^{+}$. We regard $\mathcal{D}_{\mathcal{X}}$, which depends formally on the variables $\tau_{a, \epsilon}, 0 \leq \epsilon \leq N, 0 \leq a<\infty$ (c.f. equation 15), as the germ of a function on $\mathcal{H}_{\mathcal{X}}^{+}$ via the dilaton shift (20). This makes $\mathcal{D}_{\mathcal{X}}$ into an element of the Fock space for $\mathcal{X}$. In the same way, using the dilaton shift (21), we regard $\mathcal{D}_{Y}$ as the germ of a function on $\mathcal{H}_{Y}^{+}$and hence as an element of the Fock space for $Y$.

Suppose now that conjecture 4.1 holds. As we have chosen bases for $H_{\mathrm{CR}}^{\bullet}(\mathcal{X} ; \mathbb{C})$ and $H^{\bullet}(Y ; \mathbb{C})$, we can represent the transformation $\mathbb{U}: \mathcal{H}_{\mathcal{X}} \rightarrow \mathcal{H}_{Y}$ by a matrix $U$ with entries that are Laurent polynomials in $z$. Let $U=U_{-} U_{0} U_{+}$be the Birkhoff factorization of this matrix, so that

$$
\begin{aligned}
& U_{-}=I+U_{-1} z^{-1}+\cdots+U_{-k} z^{-k} \\
& U_{0}=\text { constant diagonal matrix } \\
& U_{+}=I+U_{1} z+\cdots+U_{l} z^{l}
\end{aligned}
$$

for some $k, l>0$. (The fact that $U_{0}$ is a constant diagonal matrix, not a diagonal matrix of Laurent monomials in $z$, follows from condition (c) in conjecture 4.1.)[^0]

Remark 10.1. The Birkhoff factorization here can easily be computed using row and column operations. For example, as $U=U_{-} U_{0} U_{+}$we see that $U_{+}^{-1}$ is the unique matrix of the form $I+A_{1} z+\cdots+A_{m} z^{m}$ such that $U U_{+}^{-1}$ contains only negative powers of $z$. This can be computed using column operations on $U$. The transformation $A_{i}$ lowers degree by $2 i$, as $\mathbb{U}$ is degree-preserving, and hence $A_{i}$ is nilpotent; $I+A_{1} z+\cdots+A_{m} z^{m}$ is therefore invertible with polynomial inverse. This determines $U_{+}$. The matrices $U_{-}$and $U_{0}$ can be determined similarly.

If we change our choice of bases for $H_{\mathrm{CR}}^{\bullet}(\mathcal{X} ; \mathbb{C})$ and $H^{\bullet}(Y ; \mathbb{C})$ then the factorization

$$
U=U_{-} U_{0} U_{+} \quad \text { becomes } \quad A U B^{-1}=\left(A U_{-} A^{-1}\right)\left(A U_{0} B^{-1}\right)\left(B U_{+} B^{-1}\right)
$$

where $A$ and $B$ are appropriate change-of-basis matrices, and so the factorization defines linear symplectic isomorphisms

$$
\mathbb{U}_{-}: \mathcal{H}_{Y} \rightarrow \mathcal{H}_{Y}, \quad \mathbb{U}_{0}: \mathcal{H}_{\mathcal{X}} \rightarrow \mathcal{H}_{Y}, \quad \mathbb{U}_{+}: \mathcal{H}_{\mathcal{X}} \rightarrow \mathcal{H}_{\mathcal{X}}
$$

which are independent of our choice of bases. Let us identify the Fock space for $\mathcal{X}$ with the Fock space for $Y$ via the isomorphism $\mathbb{U}_{0}: \mathcal{H}_{\mathcal{X}} \rightarrow \mathcal{H}_{Y}$. In this way we regard $\mathcal{D}_{\mathcal{X}}$ as an element of the Fock space for $Y$; concretely, this means that we regard $\mathcal{D}_{\mathcal{X}}$ as a formal power series in the variables $t_{a, \epsilon}, 0 \leq \epsilon \leq N, 0 \leq a<\infty$ via the identification $t_{a, \epsilon} \varphi_{\epsilon}=\mathbb{U}_{0}\left(\tau_{a, \mu} \phi_{\mu}\right)$. Consider now the $\mathbb{C}\left(\left(z^{-1}\right)\right)$-linear symplectic transformations $\mathbb{T}_{-}, \mathbb{T}_{+}: \mathcal{H}_{Y} \rightarrow \mathcal{H}_{Y}$ defined by

$$
\mathbb{T}_{-}=\mathbb{U}_{-}, \quad \mathbb{T}_{+}=\mathbb{U}_{0} \mathbb{U}_{+} \mathbb{U}_{0}^{-1}
$$

Propositions 5.3 and 7.3 in [21] give formulas for the quantizations $\widehat{\mathbb{T}}_{-}, \widehat{\mathbb{T}}_{+}$ of $\mathbb{T}_{-}$ and $\mathbb{T}_{+}$: these quantizations are endomorphisms of the Fock space for $Y$.

Conjecture 10.2. Conjecture 4.1 holds, and in addition

$$
\mathcal{D}_{Y} \propto \widehat{\mathbb{T}}_{-} \widehat{\mathbb{T}}_{+}\left(\mathcal{D}_{\mathcal{X}}\right)
$$

after an appropriate analytic continuation of $\mathcal{D}_{\mathcal{X}}$ and $\mathcal{D}_{Y}$. The symbol ' $\propto$ ' here means 'is a scalar multiple of'.

Remark 10.3. The scalar multiple in conjecture 10.2 is determined by the condition that the genus-one descendant potential of $Y$ vanishes when all the $t_{a, \epsilon}$ are zero. Thus conjecture 10.2 determines the higher-genus Gromov-Witten invariants of $\mathcal{X}$ in terms of those of $Y$.

Remark 10.4. In order for the analytic continuation indicated in conjecture 10.2 to make sense, we need assume some convergence of the total descendant potential $\mathcal{D}_{Y}$. For example, if we require that there are strictly positive real numbers $R_{i}$, $s<i \leq r$, such that each $\mathcal{F}_{Y}^{g}, g \geq 0$, depends analytically on $Q_{s+1}, \ldots, Q_{r}$ in the domain

$$
\left|Q_{i}\right|<R_{i}, \quad s<i \leq r
$$

then (as above) the Divisor Equation implies that each $\mathcal{F}_{Y}^{g}$ in fact depends analytically on $t_{0,1}, \ldots, t_{0, r}$ and $Q_{s+1}, \ldots, Q_{r}$ in the domain

$$
\begin{array}{ll}
\left|t_{0, i}\right|<\infty & 1 \leq i \leq s \\
\left|Q_{i} \mathrm{e}^{t_{0, i}}\right|<R_{i} & s<i \leq r
\end{array}
$$

This allows us to set $Q_{s+1}=\cdots=Q_{r}=1$, defining $\mathcal{F}_{Y}^{g, \circledast}, g \geq 0$, exactly as we defined $\mathcal{F}_{Y}^{\circledast}$ above. We can then use $\mathcal{D}_{Y}^{\circledast}=\exp \left(\sum_{g \geq 0} \mathcal{F}_{Y}^{g, \circledast}\right)$ in place of $\mathcal{D}_{Y}$ in
conjecture 10.2. But this convergence assumption is difficult to check in practice З $^{3}$, and it would be useful to have a higher-genus analog of assumption 2.1.

Remark 10.5. Bryan and Graber have suggested [7, remark 1.8] that when $\mathcal{X}$ satisfies the Hard Lefschetz condition, the higher-genus non-descendant GromovWitten potentials

$$
F_{\mathcal{X}}^{g}(\tau)=\left.\mathcal{F}_{\mathcal{X}}^{g}\right|_{\tau_{0}=\tau ; \tau_{1}=\tau_{2}=\cdots=0} \quad \text { and } \quad F_{Y}^{g}(t)=\left.\mathcal{F}_{Y}^{g}\right|_{t_{0}=t ; t_{1}=t_{2}=\cdots=0}
$$

might coincide after analytic continuation in the quantum parameters $Q_{s+1}, \ldots, Q_{r}$, the substitution (48), and the change-of-variables $t=U_{0}(\tau)$ from theorem 0.1 If conjecture 10.2 and the above convergence assumption hold then this is the case. The Hard Lefschetz condition ensures that the transformation $\mathbb{U}_{+}$ is the identity, and conjecture 10.2 then becomes

$$
\mathcal{D}_{Y}^{\circledast} \propto \widehat{\mathbb{U}}_{-}\left(\mathcal{D}_{\mathcal{X}}\right)
$$

Applying Givental's formula [21, proposition 5.3] for the operator $\widehat{\mathbb{U}_{-}}$shows that the non-descendant potentials $F_{\mathcal{X}}^{g}(\tau)$ and $F_{Y}^{g, \circledast}(t)$ are related by analytic continuation and a change-of-variables; taking account of the substitution (36), exactly as in $\$ 9$, shows that $F_{X}^{g}$ and $F_{Y}^{g}$ are related as claimed.

## 11. Specializations, $B$-Fields, and Flat Gerbes

An issue of particular importance for the various Crepant Resolution Conjectures is to determine the values to which the exceptional quantum parameters $Q_{i}$ should be specialized. These values have physical significance and are referred in the physics literature as the $B$-field. Calculating the correct value of the $B$-field is a subtle problem even in physics, and although this is understood in some examples (Hilbert scheme of points, surface singularities, K3 surfaces, etc.) there is not yet a procedure to determine the value of the $B$-field in general. One advantage of our approach is that it gives such a procedure: we can interpret the values of the specialization (and hence the value of the B-field) as coming from a shift in basepoint on Givental's cone. In this section we study this issue and relate it to the physical point of view on the B-field. First we propose a further conjecture to constrain the choice of shift.

Conjecture 11.1. Suppose that conjecture 4.1 holds, so that

$$
\mathbb{U}\left(\mathbf{1}_{\mathcal{X}}\right)=\mathbf{1}_{Y}-c z^{-1}+O\left(z^{-2}\right)
$$

for some $c \in H^{2}(Y ; \mathbb{C})$. Then in fact $c \in H^{2}(Y ; \mathbb{Q} \sqrt{-1})$.

Note that this implies that the quantities $\mathrm{e}^{c_{i}}$ occurring in theorems $7.2,8.3$, and 9.1 are roots of unity.

Now we introduce the notion of Gromov-Witten invariants twisted by a flat gerbe. Twisting by a flat gerbe is believed to be the correct mathematical analog of 'turning on a $B$-field' in physics. The general construction in the orbifold case has been worked out by Pan-Ruan-Yin [30]. In the smooth case it is particularly easy. For a smooth manifold $Y$, giving a flat gerbe on $Y$ is equivalent to giving its holonomy, which is a cohomology class $\theta \in H^{2}(Y, U(1))$. Gromov-Witten invariants twisted by this flat gerbe coincide with the usual Gromov-Witten invariants of $Y$, but multiplied by a phase factor given by the holonomy:

$$
\left\langle\delta_{1} \psi^{a_{1}}, \ldots, \delta_{n} \psi^{a_{n}}\right\rangle_{0, n, d}^{Y, \theta}=\theta(d)\left\langle\delta_{1} \psi^{a_{1}}, \ldots, \delta_{n} \psi^{a_{n}}\right\rangle_{0, n, d}^{Y}
$$[^1]

We will only need the case when $Y$ is smooth, so the reader unfamiliar with $\theta$-twisted Gromov-Witten invariants can take (50) as the definition. It is clear that on smooth manifolds the set of all $\theta$-twisted Gromov-Witten invariants, for any flat gerbe $\theta$, contains the same information as the set of ordinary Gromov-Witten invariants. The class $c$ in conjecture 4.2 induces a flat gerbe $\theta_{c}$ through the coefficient exact sequence

$$
0 \longrightarrow \sqrt{-1} \mathbb{Z} \longrightarrow \sqrt{-1} \mathbb{R} \xrightarrow{x \mapsto \exp (2 \pi x)} U(1) \longrightarrow 0
$$

On the other hand, if $H^{3}(Y, \sqrt{-1} \mathbb{Z})=0$ then any flat gerbe $\theta$ has a lift $\rho_{\theta} \in$ $H^{2}(Y ; \sqrt{-1} \mathbb{R})$.

We can define $\theta$-twisted versions $F_{Y, \theta}, F_{Y, \theta}^{\circledast}$, and $\mathcal{L}_{Y, \theta}$ of $F_{Y}, F_{Y}^{\circledast}$, and $\mathcal{L}_{Y}$ respectively, by replacing ordinary Gromov-Witten invariants with $\theta$-twisted GromovWitten invariants.

Lemma 11.2. Suppose that $\rho_{\theta}$ is a lifting of $\theta$. Then multiplication by $e^{\rho_{\theta} / z}$ defines a symplectic transformation $\mathcal{H}_{Y} \rightarrow \mathcal{H}_{Y}$ such that $e^{\theta_{\theta} / z} \mathcal{L}_{Y}=\mathcal{L}_{Y, \theta}$.

Proof. Combine the Divisor Equation (see [15), equation 8]) with (50).

Corollary 11.3. If conjectures 4.1 and 11.1 hold then the symplectic transformation $\mathbb{U}_{c}: \mathcal{H}_{\mathcal{X}} \rightarrow \mathcal{H}_{Y}$ defined by $\mathbb{U}_{c}=\mathrm{e}^{c / z} \mathbb{U}$ satisfies properties (a-d) of conjecture 4.1 and also:

$$
\mathbb{U}_{c}\left(\mathcal{L}_{\mathcal{X}}\right)=\mathcal{L}_{Y, \theta_{c}} \quad \mathbb{U}_{c}\left(\mathbf{1}_{\mathcal{X}}\right)=\mathbf{1}_{Y}+O\left(z^{-2}\right) .
$$

Recall from $\S \$ 79$ that the cohomology class $c \in H^{2}(Y ; \mathbb{C})$ defined by $\mathbb{U}\left(\mathbf{1}_{\mathcal{X}}\right)=$ $\mathbf{1}_{Y}-c z^{-1}+O\left(z^{-2}\right)$ gives rise to the values $\mathrm{e}^{c_{i}}$ to which the exceptional quantum parameters are specialized: in other words $\mathbb{U}$ picks out the $B$-field. It does this because $c$ produces the 'shift in basepoint' $\circledast \rightsquigarrow \circledast$ visible, for instance, in equation (39). If we repeat the analysis of $\S \S 709$ but using the symplectic transformation $\mathbb{U}_{c}$ rather than $\mathbb{U}$ then on the one hand we should replace each $\mathrm{e}^{c_{i}}$ by 1 (because $\mathbb{U}_{c}\left(\mathbf{1}_{\mathcal{X}}\right)=\mathbf{1}_{Y}+O\left(z^{-2}\right)$ and so now there is no shift in basepoint) and on the other hand we should replace the quantum cohomology of $Y$ by the $\theta_{c}$-twisted quantum cohomology (because we consider the submanifold-germ $\mathcal{L}_{Y, \theta}$ not $\mathcal{L}_{Y}$ ). In other words, our conjectures predict the emergence of a flat gerbe $\theta_{c}$. We can use this to give a very clean version of the Cohomological Crepant Resolution Conjecture:

Conjecture (Modified CCRC). There is a flat gerbe $\theta$ on $Y$ such that the ChenRuan product $\bigcup_{C R}$ on $H_{\mathrm{CR}}^{\bullet}(\mathcal{X} ; \mathbb{C})$ can be obtained from the $\theta$-twisted small quantum product for $Y$ by analytic continuation in the quantum parameters $Q_{s+1}, \ldots, Q_{r}$ (if necessary) followed by the substitution

$$
Q_{i}= \begin{cases}0 & 1 \leq i \leq s \\ 1 & s<i \leq r\end{cases}
$$

Conjectures 4.1 and 11.1 together imply the Modified CCRC with $\theta=\theta_{c}$. We can give a similarly-improved version of Ruan's Crepant Resolution Conjecture, which again follows from Conjectures 4.1 and 11.1

Conjecture. (Modified CRC) Suppose that $\mathcal{X}$ is semi-positive. Then there is a flat gerbe $\theta$ over $Y$ and a choice of elements $f_{1}, \ldots, f_{r} \in \mathbb{C} \llbracket U_{1}, \ldots, U_{s} \rrbracket$ such that $f_{i}=0$ when $U_{1}=\cdots=U_{s}=0$, such that the class $f=f_{1} \varphi_{1}+\cdots+f_{r} \varphi_{r}$ is exceptional, and such that the Frobenius algebra given by the small quantum cohomology of $\mathcal{X}$ is isomorphic to the Frobenius algebra obtained from the $\theta$-twisted small quantum
cohomology of $Y$ by analytic continuation in the exceptional quantum parameters $Q_{s+1}, \ldots, Q_{r}$ (if necessary) followed by the change-of-variables

$$
Q_{i}= \begin{cases}\mathrm{e}^{f_{i}} U_{i} & 1 \leq i \leq s \\ \mathrm{e}^{f_{i}} & s<i \leq r\end{cases}
$$

The corrections $f_{i}$ here and in (47) are an example of what physicists call a 'mirror map'.

## Appendix: Proofs of Analyticity Results

Lemma A.1. The descendant potential $\mathcal{F}_{\mathcal{X}}^{0}$, which is a formal power series in the variables $U_{1}, \ldots, U_{s}$ and $\tau_{a, \epsilon}, 0 \leq \epsilon \leq N, 0 \leq a<\infty$, in fact depends analytically on $\tau_{0,1}, \ldots, \tau_{0, s}$ in the domain $\mathbb{C}^{s}$.

Proof. Set

$$
\begin{aligned}
& \tau_{0, \mathrm{two}}=\tau_{0,1} \phi_{1}+\cdots+\tau_{0, s} \phi_{s} \\
& {\left[\phi_{e_{1}} \psi^{a_{1}}, \ldots, \phi_{e_{k}} \psi^{a_{k}}\right]_{0, d}^{\mathcal{X}}=\sum_{n \geq 0} \frac{1}{n!}\left\langle\phi_{e_{1}} \psi^{a_{1}}, \ldots, \phi_{e_{k}} \psi^{a_{k}}, \tau_{0, \mathrm{two}}, \ldots, \tau_{0, \mathrm{two}}\right\rangle_{0, n+k, d}^{\mathcal{X}},} \\
& \left\langle\phi_{e_{1}} \psi^{a_{1}}, \ldots, \phi_{e_{k}} \psi^{a_{k}}\right\rangle_{0}^{\mathcal{X}}=\sum_{d \in \operatorname{Eff}(\mathcal{X})}\left[\phi_{e_{1}} \psi^{a_{1}}, \ldots, \phi_{e_{k}} \psi^{a_{k}}\right]_{0, d}^{\mathcal{X}} U^{d},
\end{aligned}
$$

and call the quantity $\left[\phi_{e_{1}} \psi^{a_{1}}, \ldots, \phi_{e_{k}} \psi^{a_{k}}\right]_{0, d}^{\mathcal{X}}$ a $k$-point descendant. We need to show that each $k$-point descendant is an entire function of $\tau_{0,1}, \ldots, \tau_{0, s}$; let us call this property entireness. The Topological Recursion Relations [34, §2.5.5] express any $k$-point descendant $\left[\phi_{e_{1}} \psi^{a_{1}}, \ldots, \phi_{e_{k}} \psi^{a_{k}}\right]_{0, d}^{\mathcal{X}}$ with $k \geq 3$ and at least one nonzero $a_{i}$ as a linear combination of $l$-point descendants with $l<k$. Thus we need to establish entireness for $k$-point descendants with $k=0, k=1, k=2$, or $k$ arbitrary but $a_{1}=\cdots=a_{k}=0$. The cases $k=0$ and $k$ arbitrary but $a_{1}=\cdots=a_{k}=0$ follow from the entireness of the potential $F_{\mathcal{X}}$ (see equation 8 ). The cases $k=1$ and $k=2$ but $a_{2}=0$ follow from proposition 6.13. The remaining case $-k=2$ but $a_{1}, a_{2} \neq 0$ - follows from the WDVV-like identity

$$
\left\langle\left\langle\frac{\phi_{\alpha}}{z-\psi}, 1, \frac{\phi_{\beta}}{w-\psi}\right)\right\rangle_{0}^{\mathcal{X}}=\left\langle\left\langle\frac{\phi_{\alpha}}{z-\psi}, 1, \phi_{\epsilon}\right\rangle\right\rangle_{0}^{\mathcal{X}}\left\langle\left\langle\phi^{\epsilon}, 1, \frac{\phi_{\beta}}{w-\psi}\right\rangle\right\rangle_{0}^{\mathcal{X}}
$$

and the String Equation

$$
\begin{aligned}
& \left\langle\left\langle\frac{\phi_{\alpha}}{z-\psi}, 1, \frac{\phi_{\beta}}{w-\psi}\right)\right\rangle_{0}^{\mathcal{X}}=\frac{1}{z w}\left(\phi_{\alpha}, \phi_{\beta}\right) \mathcal{X}+\left(\frac{1}{z}+\frac{1}{w}\right)\left\langle\left\langle\frac{\phi_{\alpha}}{z-\psi}, \frac{\phi_{\beta}}{w-\psi}\right)\right\rangle_{0}^{\mathcal{X}} \\
& \left\langle\left\langle\frac{\phi_{\alpha}}{z-\psi}, 1, \phi_{\epsilon}\right\rangle\right\rangle_{0}^{\mathcal{X}}=\frac{1}{z}\left(\phi_{\alpha}, \phi_{\epsilon}\right)_{\mathcal{X}}+\frac{1}{z}\left\langle\left\langle\frac{\phi_{\alpha}}{z-\psi}, \phi_{\epsilon}\right)\right\rangle_{0}^{\mathcal{X}}
\end{aligned}
$$

Thus $\mathcal{F}_{\mathcal{X}}^{0}$ depends analytically on $\tau_{0,1}, \ldots, \tau_{0, s}$ in the domain $\mathbb{C}^{s}$.

Lemma A.2. Assume that convergence assumption 2.1 holds. Then the descendant potential $\mathcal{F}_{Y}^{0}$, which is a formal power series in the variables $Q_{1}, \ldots, Q_{r}$ and $t_{a, \epsilon}, 0 \leq \epsilon \leq N, 0 \leq a<\infty$, in fact depends analytically on $t_{0,1}, \ldots, t_{0, r}$ and $Q_{s+1}, \ldots, Q_{r}$ in the domain

$$
\begin{array}{ll}
\left|t_{0, i}\right|<\infty & 1 \leq i \leq s \\
\left|Q_{i} \mathrm{e}^{t_{0, i}}\right|<R_{i} & s<i \leq r
\end{array}
$$

Proof. This is very similar to the proof of the preceding lemma. As before, set

$$
\begin{aligned}
& t_{0, \mathrm{two}}=t_{0,1} \varphi_{1}+\cdots+t_{0, r} \varphi_{r} \\
& {\left[\varphi_{e_{1}} \psi^{a_{1}}, \ldots, \varphi_{e_{k}} \psi^{a_{k}}\right]_{0, d}^{Y}=\sum_{n \geq 0} \frac{1}{n!}\left\langle\varphi_{e_{1}} \psi^{a_{1}}, \ldots, \varphi_{e_{k}} \psi^{a_{k}}, t_{0, \mathrm{two}}, \ldots, t_{0, \mathrm{two}}\right\rangle_{0, n+k, d}^{Y}} \\
& \left\langle\varphi_{e_{1}} \psi^{a_{1}}, \ldots, \varphi_{e_{k}} \psi^{a_{k}}\right\rangle_{0}^{Y}=\sum_{d \in \operatorname{Eff}(Y)}\left[\varphi_{e_{1}} \psi^{a_{1}}, \ldots, \varphi_{e_{k}} \psi^{a_{k}}\right]_{0, d}^{Y} Q^{d} .
\end{aligned}
$$

We need to show that, for each choice of $d_{1}, \ldots, d_{s} \in \mathbb{Q}$ with $d_{i} \geq 0$, the coefficient of $Q_{1}^{d_{1}} \cdots Q_{s}^{d_{s}}$ in $\left\langle\varphi_{e_{1}} \psi^{a_{1}}, \ldots, \varphi_{e_{k}} \psi^{a_{k}}\right\rangle_{0}^{Y}$ defines an analytic function of $t_{0,1}, \ldots, t_{0, r}$ and $Q_{s+1}, \ldots, Q_{r}$ in the domain (53). Let us call this property analyticity of $\left\langle\left\langle\varphi_{e_{1}} \psi^{a_{1}}, \ldots, \varphi_{e_{k}} \psi^{a_{k}}\right\rangle_{0}^{Y}\right.$.

The Topological Recursion Relations [16, lemma 10.2.2] show that it suffices to establish analyticity of $\left\langle\varphi_{e_{1}} \psi^{a_{1}}, \ldots, \varphi_{e_{k}} \psi^{a_{k}}\right\rangle_{0}^{Y}$ in the cases where $k=0, k=1$, $k=2$, or $k$ arbitrary but $a_{1}=\cdots=a_{k}=0$. The cases $k=0$ and $k$ arbitrary but $a_{1}=\cdots=a_{k}=0$ follow from convergence assumption 2.1 (see the discussion above equation (10). The cases $k=1$ and $k=2$ with $a_{1}, a_{2} \neq 0$ follow from the case $k=2$ but $a_{2}=0$, in view of identities (51), (52), and the String Equation

$$
\left\langle\left\langle\frac{\varphi_{\alpha}}{z-\psi}, 1\right\rangle\right\rangle_{0}^{Y}=\frac{1}{z}\left(\varphi_{\alpha}, t_{0, \mathrm{two}}\right)_{Y}+\frac{1}{z}\left\langle\left\langle\frac{\varphi_{\alpha}}{z-\psi}\right\rangle_{0}^{Y}\right.
$$

It remains to establish the analyticity of $\left\langle\frac{\phi_{\alpha}}{z-\psi}, \phi_{\beta}\right\rangle_{0}^{Y}$ for all $\alpha$ and $\beta$; this holds as these quantities are solutions to a system of differential equations (the 'quantum differential equations' [16, proposition 10.2.1]) with coefficients which are known, by convergence assumption [2.1, to be analytic functions defined in the domain (53)). The lemma is proved.

## REFERENCES

[1] M. Aganagic, V. Bouchard, and A. Klemm, Topological Strings and (Almost) Modular Forms. Preprint, available at hep-th/0607100.

[2] D. Abramovich, T. Graber, and A. Vistoli, Algebraic orbifold quantum products, in Orbifolds in mathematics and physics (Madison, WI, 2001), pp. 1-24. Contemp. Math., 310. Amer. Math. Soc., Providence, RI, 2002.

[3] , Gromov-Witten theory of Deligne-Mumford stacks. Preprint (2006), available at arXiv:math.AG/0603151.

[4] P. S. Aspinwall, B. R. Greene, and D. R. Morrison, Calabi-Yau moduli space, mirror manifolds and spacetime topology change in string theory, Nuclear Phys. B, 416 (1994), $414-480$.

[5] S. Barannikov, Quantum periods. I. Semi-infinite variations of Hodge structures, Internat. Math. Res. Notices (2001), 1243-1264.

[6] A. A. BeIllinson, J. Bernstein, and P. Deligne, Faisceaux pervers, in Analysis and topology on singular spaces, I (Luminy, 1981), pp. 5-171. Astérisque, 100. Soc. Math. France, Paris, 1982.

[7] J. Bryan and T. Graber, The Crepant Resolution Conjecture. Preprint, available at arXiv:math.AG/0610129.

[8] J. Bryan, T. Graber, and R. Pandharipande, The orbifold quantum cohomology of $\mathbb{C}^{2} / \mathbb{Z}_{3}$ and Hurwitz-Hodge integrals. Preprint, available at arXiv:math.AG/0510335.

[9] W. Chen and Y. Ruan, A new cohomology theory of orbifold, Comm. Math. Phys., 248 (2004), 1-31.

[10] , Orbifold Gromov-Witten theory, in Orbifolds in mathematics and physics (Madison, WI, 2001), pp. 25-85. Contemp. Math., 310. Amer. Math. Soc., Providence, RI, 2002.

[11] T. Coates, Givental's Lagrangian Cone and $S^{1}$-Equivariant Gromov-Witten Theory. Preprint, available at arXiv:math.AG/0607808.

[12] _, Wall-Crossings in Toric Gromov-Witten Theory II: Local Examples. Preprint, available at arXiv:0804.2592v1.

[13] T. Coates, A. Corti, H. Iritani, and H.-H. Tseng, Wall-Crossings in Toric Gromov-Witten Theory I: Crepant Examples. Preprint, available at arXiv:math.AG/0611550.

[14] T. Coates, A. Corti, Y.-P. Lee, and H.-H. Tseng, The Quantum Orbifold Cohomology of Weighted Projective Space. Preprint, available at arXiv:math.AG/0608481.

[15] T. Coates and A. Givental, Quantum Riemann-Roch, Lefschetz and Serre, Ann. of Math. (2), 165 (2007), 15-53.

[16] D. A. Cox and S. Katz, Mirror symmetry and algebraic geometry. Mathematical Surveys and Monographs, 68. American Mathematical Society, Providence, RI, 1999.

[17] B. Dubrovin, Geometry of 2D topological field theories, in Integrable systems and quantum groups (Montecatini Terme, 1993), pp. 120-348. Lecture Notes in Math., 1620. Springer, Berlin, 1996.

[18] C. Faber, S. Shadrin, and D. Zvonkine, Tautological relations and the r-spin Witten conjecture. Preprint, available at arXiv:math/0612510.

[19] W. Fulton and R. Pandharipande, Notes on stable maps and quantum cohomology, in Algebraic geometry-Santa Cruz 1995, pp. 45-96. Proc. Sympos. Pure Math., 62. Amer. Math. Soc., Providence, RI, 1997.

[20] A. B. Givental, Homological geometry. I. Projective hypersurfaces, Selecta Math. (N.S.), 1 $(1995), 325-345$.

[21] , Gromov-Witten invariants and quantization of quadratic Hamiltonians, Mosc. Math. J., 1 (2001), 551-568, 645.

[22] , Symplectic geometry of Frobenius structures, in Frobenius manifolds, pp. 91-112. Aspects Math., E36. Vieweg, Wiesbaden, 2004.

[23] C. Hertling, Frobenius manifolds and moduli spaces for singularities. Cambridge Tracts in Mathematics, 151. Cambridge University Press, Cambridge, 2002.

[24] C. Hertling and Yu. Manin, Weak Frobenius manifolds, Internat. Math. Res. Notices (1999), 277-286.

[25] S. KeEl and S. Mori, Quotients by groupoids, Ann. of Math. (2), 145 (1997), 193-213.

[26] Y.-P. LeE, Invariance of tautological equations I: conjectures and applications. Preprint, available at arXiv:math/0604318.

[27] _, Invariance of tautological equations II: Gromov-Witten theory. Preprint, available at arXiv:math/0605708.

[28] Y. I. Manin, Frobenius manifolds, quantum cohomology, and moduli spaces. American Mathematical Society Colloquium Publications, 47. American Mathematical Society, Providence, RI, 1999.

[29] T. E. Milanov, Gromov-Witten Theory of $\mathbb{C P}^{1}$ and Integrable Hierarchies. Preprint, available at arXiv:math-ph/0605001.

[30] J. Pan, Y. Ruan, and X. Yin, Gerbes and twisted orbifold quantum cohomology. Preprint, available at arXiv:math.AG/0504369.

[31] F. Perroni, Orbifold Cohomology of ADE-singularities. Preprint, available at arXiv:math.AG/0510528.

[32] Y. Ruan, The cohomology ring of crepant resolutions of orbifolds, in Gromov-Witten theory of spin curves and orbifolds, pp. 117-126. Contemp. Math., 403. Amer. Math. Soc., Providence, RI, 2006.

$[33]$ , unpublished.

[34] H.-H. Tseng, Orbifold Quantum Riemann-Roch, Lefschetz and Serre. Preprint, available at arXiv:math.AG/0506111

[35] E. Witten, Quantum Background Independence In String Theory. Preprint, available at arXiv:hep-th/9306122.
