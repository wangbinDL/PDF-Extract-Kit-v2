# The Projective Linear Supergroup and the SUSY-preserving automorphisms of  P 1 ∣ 1  

R. Fioresi † , S. D. Kwok  $\star$  

$\dagger$   Dipartimento di Matematica, Universit\` a di Bologna Piazza di Porta S. Donato, 5. 40126 Bologna. Italy. e-mail: rita.ﬁoresi@UniBo.it  

$\star$  Mathematics Research Unit, University of Luxembourg 6, Rue Richard Coudenhove-Kalergi, L-1359, Luxembourg e-mail: stephen.kwok@uni.lu  

# Abstract  

The purpose of this paper is to describe the projective linear su- pergroup, its relation with the automorphisms of the projective su- perspace and to determine the supergroup of SUSY preserving auto- morphisms of    $\mathbb{P}^{1|1}$  .  

# 1 Introduction  

The works of Manin [13, 14] and more recently of Witten et al. [16, 4] have drawn attention to projective supergeometry and more speciﬁcally to SUSY curves and their moduli superspaces.  

In this paper we study the automorphisms of the projective superspace  $\mathbb{P}^{m|n}$    and its SUSY-preserving subsupergroup. We start by deﬁning the pro- jective linear supergroup   $\mathrm{PGL}_{m|n}$  , using the functor of points formalism, and then we show that this supergroup functor is indeed representable, that is, it is the functor of points of a superscheme. We achieve this by realizing  $\mathrm{PGL}_{m|n}$   $\mathrm{GL}_{m^{2}+n^{2}|2m n}$  , mimicking the ordinary procedure.  

In relating this supergroup scheme to the automorphism supergroup of  $\mathbb{P}^{m|n}$    we encounter a diﬃculty, not present in the ordinary setting, namely the fact that the Picard group of the projective superspace is not known in general and involves some diﬃculties. This is a consequence of the fact that the supergroup of automorphism of the projective superspace is larger than  $\mathrm{PGL}_{m|n}$     $n>1$  . Neverthless, going to the special case of    $n\,=\,1$  , we are able to give quite explicitly the projective linear supergroup and to prove it coincides with the automorphisms of the projective superspace.  

The question of singling out the SUSY-preserving automorphisms inside this supergroup was already settled over the complex ﬁeld by Manin [13] and Witten [16], we extend their considerations to an arbitrary algebraically closed ﬁeld    $k$  ,   $\operatorname{char}(k)\neq2$  , and provide some extra details of their proofs.  

The organization of this paper is as follows. In Sec. 2 we start by review- ing some generally known facts on the projective superspace and its functor of points to establish our notation. We then discuss line bundles and projec- tive morphisms, proving, in Prop. 2.3, that the Picard group of    $\mathbb{P}^{m|1}$    is    $\mathbb{Z}$  . To our knowledge this result is new and gives insight into projective super- geometry. In Sec. 3 we deﬁne the projective linear supergroup in terms of functor of points and we prove its represent ability by realizing it as a closed subsuperscheme of the general linear supergroup. Then, in Sec. 4 we prove that the projective linear supergroup is the supergroup of automorphisms of the projective superspace in the case of one odd dimension. Though the approach in both Sec. 3 and 4 resembles closely the ordinary one, the results are novel in the supergeometric context. In Sec. 5, we use the machinery developed previously to prove that the subsupergroup of   $\operatorname{Aut}(\mathbb{P}^{1|1})$   of SUSY preserving automorphisms of    $\mathbb{P}^{1|1}$    consists precisely of the irreducible compo- nent    $(\mathrm{SpO_{2\vert1}})^{0}$    of the 2 ∣ 1-sym ple c tic orthogonal supergroup   $\mathrm{SpO_{2\vert1}}$   containing the identity. This section is a generalization of the claims made by Manin in [13] regarding complex supergeometry and provides proofs for such claims for a generic algebraically closed ﬁeld.  

Acknowledgements.  We are indebted to Prof. D. Gaitsgory for clari-   fying to us the structure of line bundles over  $\mathbb{P}_{A}^{n}$    in the ordinary setting. We also thank Prof. L. Migliorini for helpful discussions. We are also grateful to the anonymous Referee for his/her suggestions and remarks on the paper.  

# 2 The projective superspace    $\mathbb{P}^{m|n}$  

In this section we want to recall diﬀerent, but equivalent deﬁnitions of projec- tive superspace and we describe the line bundles on it. For all of our notation and main deﬁnitions of supergeometry, we refer the reader to [14, 3, 1].  

Let    $k$   be our ground ring.  

We recall that, by deﬁnition, the functor of points of a superscheme    $X=$   $(|X|,{\mathcal{O}}_{X})$   is the functor:  

$$
X:{\mathrm{(sselections)}}^{o}\longrightarrow{\mathrm{(s e t s)}},\quad X(S)={\mathrm{Hom}}_{\mathrm{(s e t h e m e s)}}(S,X),\quad X(\phi)(f)=f\circ\phi
$$  

where  ( sschemes )  denotes the category of superschemes (it is customary to use the same letter for    $X$   and its functor of points). Equivalently (see [1] Ch. 10), we can view the functor of points of    $X$   as:    $X:{\mathrm{(salg)}}\longrightarrow{\mathrm{(sets)}}$  :  

$$
X(R)={\mathrm{Hom}}_{({\mathrm{sech}})}({\mathrm{Spec}}\ R,X),\quad X(\phi)(f)=f\circ{\underline{{\operatorname{Spec}}}}\,(\phi)
$$  

where  ( salg )  denotes the category of superalgebras (over    $k$  ), (we shall use the same letter also for this functor). In fact the functor of points of a super- scheme is determined by its behaviour on the aﬃne superscheme subcategory, which in turn is equivalent to the category of superalgebras (see [1] Ch. 10, Theorem 10.2.5). If    $X={\underline{{\mathrm{Spec}}}}\,{\mathcal{O}}(X)$  , that is    $X$   is aﬃne, we have that  

$$
X(R)={\mathrm{Hom}}_{({\mathrm{sech}})}({\mathrm{Spec}}\ R,X)={\mathrm{Hom}}_{({\mathrm{salg}})}(\mathcal O(X),R)
$$  

where    ${\mathcal{O}}(X)$   denotes the superalgebra of global sections of the sheaf of su- peralgebras    ${\mathcal{O}}_{X}$  . We say that    $X(R)$   are the    $R$  -points  of the superscheme  $X$  .  

The algebraic superscheme    $\mathbb{P}^{m|n}$    is deﬁned as the patching of the    $m+1$  aﬃne superspaces    ${U_{i}}~=~{\mathrm{Spec}}\,{\mathcal{O}}(U_{i})$  , with    ${\mathcal{O}}(U_{i})\;=\;{\mathrm{Spec}}\,k[x_{0}^{i}$  , ...  ,    $\widehat{x_{i}^{i}}$  ,  ...  ,  $x_{m}^{i},\xi_{1}^{i},\ldots,\xi_{n}^{i}]$  ]  through the change of charts:  

$$
\begin{array}{r l r l r l}&{\phi_{i j}:}&{\mathcal{O}(U_{j})[(x_{i}^{j})^{-1}]}&{\mapsto}&{\mathcal{O}(U_{i})[(x_{j}^{i})^{-1}]}&\\ &{}&{x_{k}^{j}}&{\mapsto}&{x_{k}^{i}/x_{j}^{i}}&\\ &{}&{x_{i}^{j}}&{\mapsto}&{1/x_{j}^{j}}&\\ &{}&{\xi_{k}^{j}}&{\mapsto}&{\xi_{k}^{i}/x_{j}^{i}}&\end{array}
$$  

(as usual    $\widehat{x_{i}^{i}}$    means that we are omitting the indeterminate    $x_{i}^{i}$  ). Notice that

  $\mathcal{O}(U_{j})[(x_{i}^{j})^{-1}]$   is the superalgebra representing the open subscheme    $U_{j}\cap U_{i}$  of    $U_{j}$   (and similarly for    ${\mathcal{O}}(U_{i})[(x_{j}^{i})^{-1}]\big)$  ).  

Proposition 2.1.  The    $R$  -points of    $\mathbb{P}^{m|n}$  ,    $R\in\mathsf{\Gamma}(\mathrm{slg})$   are given equivalently by:  

$$
\mathbb{P}^{m|n}(\psi):R^{m+1|n}\otimes_{R}T\longrightarrow L\otimes_{R}T
$$  

where    $L$   is locally free of rank    $1|0$  ,    $\psi:R\longrightarrow T$   and    $\alpha:R^{m+1|n}\,\longrightarrow$   $L\sim\alpha^{\prime}:R^{m+1|n}\longrightarrow L^{\prime}$    if and only if    $k e r(\alpha)=k e r(\alpha^{\prime})$   (or equivalently,  $\alpha\sim\alpha^{\prime}$    if they diﬀer by an automorphism of    $L$   by multiplication of an element in    $R^{\times}$  ).  

$\mathcal{Q}$  .  

$$
\mathbb{P}^{m|n}(R)=\{\alpha:L\leftrightarrow R^{m+1|n}\,R\cdot l i n e a r,\,\,i n j e c t i v e\},
$$  

$$
\mathbb{P}^{m|n}(\psi):L\otimes_{R}T\longrightarrow R^{m+1|n}\otimes_{R}T
$$  

where    $L$   is locally free of rank    $1|0$  .  

Let    $\mathcal{O}_{S}^{m+1|n}=\mathcal{O}_{S}\otimes k^{m+1|n}$  . The    $S$  -points of    $\mathbb{P}^{m|n}$  ,    $S\in$  ( sschemes )  are given equivalently by:  

(a)  ${\mathbb{P}}^{m|n}\big(S\big)=\big\{\alpha:{\mathcal{O}}_{S}^{m+1|n}\longrightarrow{\mathcal{L}},\,s u r j e c t i v e\big\}\big/\sim,\,{\mathbb{P}}^{m|n}(\psi):(\psi^{*}{\mathcal{O}}_{S})^{m+1|n}\longrightarrow$   $\psi^{*}({\mathcal{L}})$   where    $\psi:T\longrightarrow S$  ,    $\mathcal{L}$   is   $a$   line bundle on    $S$   (of rank  1 ∣ 0 ) and  $\alpha:{\mathcal O}_{S}^{m+1|n}\longrightarrow{\mathcal L}\sim\alpha^{\prime}:{\mathcal O}_{S}^{m+1|n}\longrightarrow{\mathcal L}^{\prime}:\,i f$  if and only if    $k e r(\alpha)=k e r(\alpha^{\prime})$  (or equivalently,    $\alpha~\sim~\alpha^{\prime}$    if they diﬀer by an automorphism of    $\mathcal{L}$   by multiplication of an element in    ${\mathcal{O}}_{S.}^{\times}$  ).  

$$
(b)\,\ \mathbb{P}^{m|n}\big(S\big)=\big\{\alpha:\mathcal{L}\hookrightarrow\mathcal{O}_{S}^{m+1|n}\big\},\quad\mathbb{P}^{m|n}\big(\psi\big):\psi^{*}\mathcal{L}\longrightarrow(\psi^{*}\mathcal{O}_{S})^{m+1|n}
$$  

Proof.  The proof relative to (1) and (a) works as in the ordinary setting and it is detailed in [1] Ch. 10. The equivalence with (2) and (b) is immediate. The equivalence (1) and (2) is essentially the same as in the ordinary setting (see [5] Ch. III, Sec. 2 Prop. III-40, Cor. III-42).  

For every    $A\,\in\,(\mathrm{slg})$  , let    $(\operatorname{salg})_{A}$   denote the category of superalgebras    $\mathbb{P}_{A}^{m|n}$  over    $A$  . We will need to consider also that is the projective superspace over a base    $A\in({\mathrm{salg}})$  . This means that we are considering the superscheme obtained by patching the aﬃne superspaces    $U_{i}\,=\,A[x_{j}^{i},\xi_{k}^{i}]$  ,    $i,j\,=\,0,\hdots,m$  ,  $j\neq i,\;k=1,\ldots,n$   as above. For example, in the Case (2) of Prop. 2.1 each of the    $T$  -points,    $T\in(\mathrm{salg})_{A}$  , is identiﬁed with a morphisms    $\alpha:L\longrightarrow T^{m+1|n}$  of    $A$  -modules, where    $L$   and    $T^{m+1|n}$    are    $\mathit{(I)}$  -modules which become    $A$  -modules via the map    $\phi:A\longrightarrow T$  :  

$$
\mathbb{P}_{A}^{m|n}(T)=\operatorname{Hom}_{(\mathrm{sech})_{A}}(\operatorname{Spec}\,T,\mathbb{P}_{A}^{m+1|n})=\{\alpha:L\hookrightarrow T^{m+1|n}\}
$$  

Notice that the functor of points of    $\mathbb{P}_{A}^{m|n}$  is deﬁned on the category of    $A$  - superalgebras or equivalently on the category of    $A$  -superschemes (that is superschemes equipped with a morphism to the superscheme Spec  $A$   and morphisms compatible with it).  

We leave to the reader the generalization of the other cases of Prop. 2.1 since it is straightforward.  

We end this section with some observations on line bundles and mor-    $\mathbb{P}_{A}^{m|n}$  phisms on . We start with a result completely similar to the ordinary counterpart, that we leave to the reader as a simple exercise (see also [1] Ch. 9).  

Proposition 2.2.  We have a bijective correspondence between the following:  

1. The set of equivalence classes of  $m{+}n{+}2$  -tuples    $\left(L,s_{0},.\,.\,,s_{m},\sigma_{1},.\,.\,.\,,\sigma_{n}\right)$  ,    $\mathbb{P}_{A}^{m|n}$  where    $L$   is a line bundle on globally generated by the global sections  $s_{0},\ldots,s_{m},\sigma_{1},\ldots,\sigma_{n}$   of    $L$  , under the relation    $\left(L,s_{0},.\,.\,.\,s_{m},\sigma_{1},.\,.\,.\,\sigma_{n}\right)\sim$   $\left(L,s_{0}^{\prime},.\,.\,.\,s_{m}^{\prime},\sigma_{1}^{\prime},.\,.\,.\,\sigma_{n}^{\prime}\right)$  )  if and only if there exists some    $c\,\in\,\mathcal{O}(\mathbb{P}_{A}^{m\left|n\right.})_{0}^{*}$  such that    $s_{i}^{\prime}=c s_{i},\sigma_{i}^{\prime}=c\sigma_{i}$   for all    $i$  .  

2. The set of    $A$  -morphisms    $\mathbb{P}_{A}^{m|n}\to\mathbb{P}_{A}^{m|n}$  .  

In the ordinary setting we have that a line bundle on  $\mathbb{P}_{A}^{m}$    is of the form  $\mathcal{O}(n)\!\otimes\!\mathcal{L}$  , where    $\mathcal{L}$   is a line bundle on   $\operatorname{Spec}A$  . This non trivial fact is still true    $\mathbb{P}_{A}^{m|1}$  in supergeometry for , and it will turn out to be crucial in our treatment.  

Proposition 2.3.  Every line bundle on    $\mathbb{P}_{A}^{m|1}$  is isomorphic to    $\mathcal{O}(n)\otimes\mathcal{L}$  , where    $\mathcal{L}$   is a line bundle on    $\operatorname{Spec}A$  .  

Proof.  A line bundle on    $\mathbb{P}_{A}^{m|1}$  is determined once we know its transition func- tions, say    $g_{i j}\in{\mathcal{O}}_{\mathbb{P}_{A}^{m|1}}(U_{i}\cup U_{j})_{0}^{*}$  , which are even. We then need to prove that any such set of transition functions is equivalent, up to a coboundary, to a set of transition functions for a line bundle of the form    $\mathcal{O}(n)\otimes\mathcal{L}$  , for    $\mathcal{L}$   a line bundle on Spec  $A$  . In other words we need to show  

$$
h_{i}|_{U_{i}\cap U_{j}}\,g_{i j}\,h_{j}^{-1}|_{U_{i}\cap U_{j}}\:=\:(x_{j}^{i})^{n},\qquad h_{i}\in{\mathcal{O}}_{{\mathbb{P}}_{A}^{m|1}}(U_{i})_{0}^{*}
$$  

Notice that  

$$
{\mathcal O}_{{\mathbb P}_{A}^{m|1}}(U_{p})^{*}\,=\,(A\bigl[x_{k}^{p},\xi^{p}\bigr])_{0}^{*}\,=\,(A\bigl[\xi^{p}\bigr]\bigl[x_{k}^{p}\bigr])_{0}^{*},\qquad p=i,j.
$$  

Since    $\begin{array}{r}{\phi_{i j}\big(\xi^{j}\big)\,=\,\frac{\xi^{i}}{x_{j}^{i}}}\end{array}$  ,    $\phi_{i j}(x_{i}^{j})=1/x_{j}^{i}$    and    $\phi_{i j}\big(x_{k}^{j}\big)\,=\,\frac{x_{k}^{i}}{x_{j}^{i}}$    (  $\phi_{i j}$   being the change of chart as in (1)), we can view the restrictions of the    $h_{p}$  ’s   $\left(p=i,j\right)$   to    $U_{i}\cap U_{j}$  , through this identiﬁcation, as both belonging to    $(A[\xi^{i}][x_{j}^{i},(x_{j}^{i})^{-1}])_{0}^{*}$  . We now apply the classical result and obtain    $h_{p}^{\prime}\in(A[\xi^{i}][x_{j}^{i},(x_{j}^{i})^{-1}]\check{)}_{0}^{*}$    such that  

$$
h_{i}^{\prime}g_{i j}(h_{j}^{\prime})^{-1}=(x_{j}^{i})^{n}.
$$  

The    $h_{p}^{\prime}$  ’s thus obtained are not yet the sections we want; since the odd di- mension is one by hypothesis, the most general possible form for    $h_{j}^{\prime}$    is  

$$
h_{j}^{\prime}=a_{0}+\alpha_{0}\xi^{i}+\sum_{K}a_{K}x_{K}^{i}(x_{j}^{i})^{-|K|}+\sum_{L}\alpha_{L}x_{L}^{i}(x_{j}^{i})^{-|L|}\xi^{i}+\sum_{k}\beta_{k}(x_{j}^{i})^{-k}\xi^{i}
$$  

where    $K$   and    $L$   are multiindices,    $K=\left(k_{1},\ldots,k_{r}\right)$  ,  k  ≠ j  ( r  ∈ N )  and    $x_{K}^{i}:=$  l  $x_{k_{1}}^{i}\cdot\cdot\cdot x_{k_{r}}^{i}$    (similarly for    $L$  ).  

In order to eliminate the term    $\alpha_{0}\xi^{i}$    which is not well deﬁned on    $U_{j}$  , we deﬁne:  

$$
h_{i}:=\big(a_{0}+\alpha_{0}\xi^{i}\big)h_{i}^{\prime},\qquad h_{j}:=\big(a_{0}^{-1}-a_{0}^{-2}\alpha_{0}\xi^{i}\big)h_{j}^{\prime}.
$$  

and this gives the required sections.  

Notice that it was absolutely fundamental for our argument that there is only one odd dimension. This calculation will give us key information when we want to determine the automorphism supergroup of the projective linear supergroup.  

# 3 The Projective Linear Supergroup  

In this section we want to deﬁne the supergroup functor of the projective linear supergroup and to show it is representable by producing an embedding of it as a closed subgroup into the general linear supergroup.  

Let   ${\underline{{\mathrm{M}}}}_{m|n}(R)$   denote the associative superalgebra of supermatrices of or- der    $m|n$   by    $m|n$   with entries in a commutative superalgebra    $R$  . More intrin- sically,   $\operatorname{\underline{{M}}}_{m|n}(R)=\operatorname{\underline{{E n d}}}_{R}(R^{m|n})$  .  

Deﬁnition 3.1.  The  automorphism supergroup of supermatrices  is the su- pergroup functor   $\mathrm{Aut}(\underline{{\mathrm{M}}}_{m|n}):\mathrm{(salg)}\longrightarrow\mathrm{(grps)}$  

$$
\begin{array}{r l}&{\[\mathrm{Aut}(\underline{{\mathrm{M}}}_{m|n})](R):=\{f:\underline{{\mathrm{M}}}_{m|n}(R)\to\underline{{\mathrm{M}}}_{m|n}(R)\,|}\\ &{\qquad\qquad\qquad f\ \mathrm{is~an~}R\mathrm{-superalgebra~outcomes}\}.}\end{array}
$$  

In analogy with the ordinary setting we also will call this supergroup functor the  projective linear supergroup  and denote it with PGL  $(m|n)$  .  

Since   ${\underline{{\mathrm{M}}}}_{m|n}(R)$   is itself a free    $R$  -module of rank    $M|N$  , where    $M=m^{2}+n^{2}$  and    $N\,=\,2m n$  ,   $\operatorname{Aut}({\underline{{\mathrm{M}}}}_{m|n})$   is a subfunctor of   $\mathrm{GL}_{M|N}$   in a natural way. We want to prove this is the functor of points of a closed subsuperscheme of  $\mathrm{GL}_{M|N}$  . Before proceeding we need a lemma characterizing the morphisms of the superalgebra of supermatrices.  

Lemma 3.2. 1. An    $R$  -linear parity preserving map    $\psi\;:\underline{{{\mathrm{M}}}}_{m|n}(R)\;\longrightarrow\;$   ${\underline{{\mathrm{M}}}}_{m|n}(R)$   is a morphism of the superalgebra of supermatrices    ${\underline{{\mathrm{M}}}}_{m|n}(R)$  if and only if  

(a)    $\psi(\mathrm{id})=\mathrm{id}$  ;  $(b)\,\,\psi(e_{i j})\psi(e_{k l})=\delta_{k j}\psi(e_{i l}),$  , where    $e_{i j}$   are the elementary matrices in    ${\underline{{\mathrm{M}}}}_{m|n}(R)$  .  

2. If    $R$   is a local superalgebra, all of the automorphisms of the superalgebra  ${\underline{{\mathrm{M}}}}_{m|n}(R)$   are of the form:  

$$
\begin{array}{r c l}{\mathrm{M}_{m|n}(R)}&{\longrightarrow}&{\mathrm{M}_{m|n}(R)}\\ {\mathrm{}}&{}&{}\\ {\mathrm{(}T\mathrm{,}X\mathrm{)}}&{{}\mapsto}&{T X T^{-1}}\end{array}
$$  

for a suitable    $T\in\mathrm{GL}_{m\mid n}(R)$  .  

3.    $\operatorname{Aut}({\underline{{\mathrm{M}}}}_{m|n})$   is a closed subsuperscheme of    $\mathrm{GL}_{M|N}=\mathrm{Spec}\,k[x_{i j,k l}][d_{1}^{-1},d_{2}^{-1}]$    ,  $M=m^{2}+n^{2}$    and    $N=2m n$  , deﬁned by the equations:  

$$
\sum_{k}x_{i j,k k}=\delta_{i j},\qquad\sum_{s}x_{r s,i j}x_{s t,k l}=\delta_{j k}x_{r t,i l},
$$  

where    ${\mathrm{GL}}_{M|N}(R)$   is identiﬁed with the parity preserving automorphisms of the free    $R$  -module    ${\underline{{\mathrm{M}}}}_{m|n}(R)$  .  

Proof.  (1). If    $\psi$   is an    $R$  -superalgebra endomorphism of   ${\underline{{\mathrm{M}}}}_{m|n}(R)$   then the two relations are obviously satisﬁed and vice-versa.  

(2). Now assume    $\psi$   is an automorphism of   $\mathrm{M}_{m|n}(R)$  ,    $R$   local, which satisﬁes the relations    $(a)$   and    $(b)$  . We need to ﬁnd    $T\in\mathrm{GL}_{m\mid n}(R)$   such that    $\psi(e_{i j})=$   $T e_{i j}T^{-1}$  . This is an application of super Morita theory (see [12]), however we shall recall the main idea to make this proof self-contained. By    $(a)$   and  $(b)$   we have that  

$$
\sum\psi\big(e_{i i}\big)=\mathrm{id},\quad\psi\big(e_{i i}\big)^{2}=\psi\big(e_{i i}\big),\quad\psi\big(e_{i i}\big)\psi\big(e_{j j}\big)=0,\,i\neq j
$$  

hence we can write  

$$
R^{m|n}=\oplus\psi(e_{i i})R^{m|n}
$$  

Since by    $(b)$     $\psi(e_{j i})\psi(e_{i i})~=~\psi(e_{j i}){}~=~\psi(e_{j j})\psi(e_{j i})$   we have that    $\psi(e_{j i}):$   $\psi(e_{i i})R^{m|n}\longrightarrow\psi(e_{j j})R^{m|n}$    (recall that    $R$   is local so projective implies free). Hence there exists a basis    $\{t_{i}\}$   of the free module    $R^{m|n}$    such that  

$$
\psi(e_{i i})R^{m|n}=\operatorname{span}_{R}\{t_{i}\}
$$  

and  $\psi(e_{j i})t_{i}=t_{j}$  . Let    $T$   be the matrix whose columns are the    $t_{i}$  ’s,    $\begin{array}{r}{T=\sum t_{i}\mathbf{\otimes}e_{i}^{*}}\end{array}$  ,

  $\begin{array}{r}{T^{-1}=\sum e_{i}\otimes t_{i}^{*}}\end{array}$  . It is then immediate to verify    $\psi(e_{i j})=T e_{i j}T^{-1}$  .  

(3). This is immediate from (1).  

$\mathbb{G}_{m}^{1|0}\,:\,(\mathrm{salg})\,\longrightarrow$  Let us view the multiplicative algebraic supergroup

 ( grps )  as the following subsupergroup of   ${\mathrm{GL}}_{m|n}$  :  

$$
\mathbb{G}_{m}^{1|0}\bigl(R\bigr)=\{a I\,|\,a\in R_{0}^{*}\}\subset\mathrm{GL}_{m|n}(R).
$$  

(Here    $I$   denotes the identity matrix).  

We shall not specify the deﬁnition on the arrows whenever it is clear, as in this case.  

Deﬁnition 3.3.  We deﬁne the supergroup functor:  $\overline{{\mathrm{PGL}}}_{m|n}\,:\,(\mathrm{salg})\,\longrightarrow$  ( grps )  

$$
\begin{array}{r}{\overline{{\mathrm{PGL}}}_{m|n}(R)=\mathrm{GL}_{m|n}(R)/\mathbb{G}_{m}^{1|0}(R),}\end{array}
$$  

and we call its sheaﬁﬁcation (as customary)   $\mathrm{GL}_{m\vert n}/\mathbb{G}^{1\vert0}$  .  

We wish to show that   $\mathrm{GL}_{m\vert n}/\mathbb{G}^{1\vert0}$    is representable and coincides with the projective linear supergroup, that is with the automorphism supergroup of supermatrices.  

Deﬁnition 3.4.  We say that a functor    $F:(\mathrm{slg})\longrightarrow(\mathrm{grps})$  →( )  is  stalky  if for any superalgebra    $R$  , the natural map  

$$
\varinjlim_{f\notin\mathfrak{p}}F(R_{f})\longrightarrow F\big(R_{\mathfrak{p}}\big)
$$  

is an isomorphism for any prime ideal    ${\mathfrak{p}}\in R_{0}$  .  

The next two lemmas are standard and their proof is the same as in the ordinary case, see [15].  

Lemma 3.5.    $\mathrm{GL}_{m|n}/\mathbb{G}^{1|0}$    and    $\operatorname{Aut}({\underline{{\mathrm{M}}}}_{m|n})$   are stalky.  

Lemma 3.6.  Let    ${\mathcal{F}},{\mathcal{G}}$   be stalky Zariski sheaves    $(\mathrm{{slg})\rightarrow(\mathrm{{grp s})}}$  ,    $\alpha:{\mathcal{F}}\rightarrow{\mathcal{G}}$   a morphism. If    $\alpha_{R}:{\mathcal{F}}(R)\rightarrow{\mathcal{G}}(R)$   is an isomorphism for all local superrings  $R$  , then    $\alpha$   is an isomorphism of sheaves.  

Proposition 3.7.  The supergroup functor    $\mathrm{GL}_{m\vert n}/\mathbb{G}^{1\vert0}$    is representable and is realized as the closed subsupergroup    $\operatorname{Aut}({\underline{{\mathrm{M}}}}_{m|n})$   of    $\mathrm{GL}_{M|N}$   for    $M=m^{2}+n^{2}$  and    $N=2m n$  .  

Proof.  We need to establish an isomorphism of sheaves between   $\mathrm{GL}_{m\vert n}/\mathbb{G}^{1\vert0}$  and a closed subsupergroup of   ${\mathrm{GL}}_{M|N}$  . We will ﬁrst give a morphism of sheaves and then show it is an isomorphism on local superalgebras; since  $\mathrm{GL}_{m|n}/\mathbb{G}^{1|0}$    is a stalky sheaf, this will be enough. We start by giving a morphism of presheaves    ${\widehat{\mathrm{PGL}}}_{m|n}$   and   $\mathrm{GL}_{M|N}$  ; since   $\mathrm{GL}_{M|N}$   is a sheaf then such a morphism will factor through the sheaﬁﬁcation of    ${\widehat{\mathrm{PGL}}}_{m|n}$   thus giving us a sheaf morphism.  

Consider the action of   $\mathrm{GL}_{M|N}$   on supermatrices   ${\underline{{\mathrm{M}}}}_{m|n}$  , where    $M=m^{2}\!+\!n^{2}$  ,  $N=2m n$  :  

$$
\begin{array}{l l l}{\phi:}&{\mathrm{GL}_{m|n}(R)\times\underline{{\mathrm{M}}}_{m|n}(R)}&{\longrightarrow}&{\underline{{\mathrm{M}}}_{m|n}(R)}\\ &{}&{\ \ (T,X)}&{\mapsto}&{T X T^{-1}}\end{array}
$$  

$\mathbb{G}_{m}^{1|0}(R)$  This clearly factors through  hence gives a well deﬁned action    $\rho$   of  ${\widehat{\mathrm{PGL}}}_{m|n}$   and then in turn of   $\mathrm{GL}_{m\vert n}/\mathbb{G}^{1\vert0}$    (see comments at the beginning of the proof). Since    $X\mapsto T X T^{-1}$  ,    $T\in(\mathrm{GL}_{m\mid n}/\mathbb{G}^{1|0})(R)$   is a parity preserving  $R$  -superalgebra morphism, it is immediate to verify we have a morphism of sheaves  

$$
\mathrm{GL}_{m\vert n}/\mathbb{G}^{1\vert0}\to\mathrm{Aut}({\underline{{\mathrm{M}}}}_{m\vert n}).
$$  

By the ﬁrst part of Lemma 3.2,   $\operatorname{Aut}({\underline{{\mathrm{M}}}}_{m|n})$   is represented by the closed sub- superscheme    $H$   of   $\mathrm{GL}_{M|N}=\mathrm{Spec}\,k[x_{i j,k l}][d_{1}^{-1},d_{2}^{-1}]$    ]  deﬁned by the equations:  

$$
\sum_{k}x_{i j,k k}=\delta_{i j},\qquad\sum_{s}x_{r s,i j}x_{s t,k l}=\delta_{j k}x_{r t,i l}
$$  

(Here    $d_{i}$   denotes as usual the determinants of the diagonal blocks of indeter- minates). We want to show that the group homomorphism    $\bigl(\mathrm{GL}_{m|n}/\mathbb{G}^{1|0}\bigr)(R)\to$   $[\mathrm{Aut}(\underline{{\mathrm{M}}}_{m|n})](R)$   is an isomorphism for    $R$   local.    $\psi\in{\mathrm{GL}}_{M|N}(R)$   belongs to  $H(R)$   if and only its entries    $\psi(e_{i j})_{k l}$   satisfy the above relations (4) (where in our convention    $\boldsymbol{x}_{i j,k l}$   corresponds to    $\psi(e_{i j})_{k l})$  ). Hence by Lemma 3.2 we have the result for    $R$   local. By Lemmas 3.5 and 3.6, it is true for any superalgebra  $R$   and this concludes the proof.  

Remark 3.8.  The projective linear supergroup may also be obtained through the Chevalley supergroup recipe as detailed in [6, 7, 8]). It corresponds to the choice of the adjoint action of the Lie superalgebra    ${\mathfrak{s l}}_{m|n}$  . In fact one may readily check that the Lie superalgebra of   $\mathrm{PGL}_{m|n}$   is indeed    ${\mathfrak{s l}}_{m|n}$   and  $(\operatorname{PGL}_{m|n})_{0}=\operatorname{PGL}_{m}\times\operatorname{PGL}_{n}\times k^{\times}$  .  

# 4 The automorphisms of the projective su- perspace  

We want to deﬁne the automorphism supergroup of the superscheme    $\mathbb{P}^{m|n}$  .  

Deﬁnition 4.1.  We deﬁne the supergroup functor of  automorphisms of the projective superspace :  

$$
\operatorname{Aut}(\mathbb{P}^{m\vert n})(A):=\operatorname{Aut}_{A}(\mathbb{P}^{m\vert n}\times\operatorname{Spec}A)=\operatorname{Aut}_{A}\mathbb{P}_{A}^{m\vert n},\quad A\in(\operatorname{salg}).
$$  

$\operatorname{Aut}(\mathbb{P}^{m|n})$   is deﬁned in an obvious way on the morphisms.  

The equality in the deﬁnition is straightforward noticing that we can identify the    $T$  -points of    $\mathbb{P}^{m|n}\times\operatorname{Spec}A$   and of    $\mathbb{P}_{A}^{m|n}$  . In fact a    $T$  -point of

  $\mathbb{P}^{m|n}\times\operatorname{Spec}A$   is a morphism    $\phi:A\longrightarrow T$   and a morphism of    $A$  -modules via

  $\phi$  ,    $L\longrightarrow T^{m|n}$  . This is exactly an element of    $\mathbb{P}_{A}^{m\vert n}(T)$   and vice-versa.  

An automorphism    $\psi\,\in\,\mathrm{Aut}_{A}\mathbb{P}_{A}^{m|n}$  is a family of automorphisms    $\psi_{T}$   for all    $T\,\in\,(\mathrm{salg})_{A}$  , which is functorial in    $\mathit{(I)}$  .    $\psi_{T}:\mathbb{P}_{A}^{m|n}(T)\longrightarrow\mathbb{P}_{A}^{m|n}(T)$   must  

assign to a    $T$  -point of    $\mathbb{P}_{A}^{m\vert n}(T)$  , that is a morphism    $\alpha:L\longrightarrow T^{m|n}$  , another morphism    $\alpha^{\prime}:L^{\prime}\longrightarrow T^{m|n}$  , where    $L$  ,    $L^{\prime}$    are projective rank   $1|0$     $T$  -modules, where the morphisms are interpreted as    $A$  -module morphisms. Similarly for the other characterizations of    $\mathit{(I)}$  -points as in Prop. 2.1.  

We are now ready to relate the supergroup scheme   $\mathrm{PGL}_{m|n}$   with the automorphisms of    $\mathbb{P}^{m-1|n}$  .  

Proposition 4.2.  There is an embedding of supergroup functors    $\mathrm{PGL}_{m|n}\hookrightarrow$   $\operatorname{Aut}(\mathbb{P}^{m-1|n})$  .  

Proof.  We ﬁrst establish a morphism    $\phi^{\prime}:\mathrm{GL}_{m\left|n\right.}\longrightarrow\mathrm{Aut}(\mathbb{P}^{m-1\left|n\right.})$  . If    $X\,\in$   ${\mathrm{GL}}_{m|n}(A)$   and    $\alpha\in\mathbb{P}_{A}^{m-1|n}(T)=\left\{T^{m|n}\longrightarrow L\right\}/\sim,\,\psi:A\longrightarrow T$   we deﬁne  

$$
\phi^{\prime}(X)=\alpha\circ{\mathrm{GL}}_{m|n}(\psi)(X)
$$  

Clearly    $\phi^{\prime}$    factors through    $\mathbb{G}_{m}(A)$  . Since   $\operatorname{Aut}(\mathbb{P}^{m-1|1})$   is a sheaf, we have deﬁned a morphism  

$$
\phi:\mathrm{PGL}_{m|n}\longrightarrow\mathrm{Aut}(\mathbb{P}^{m-1|n})
$$  

The injectivity is clear.  

Remark 4.3.  In general we cannot expect to get an isomorphism between  $\mathrm{PGL}_{m|n}$   and   $\operatorname{Aut}(\mathbb{P}^{m-1|n})$   for    $n>1$   and this is because of the peculiarity of the odd elements. Let us see this in a simple example:    $\mathbb{P}^{1|2}$  . Consider the morphism    $\phi\in\mathbb{P}_{A}^{1|2}$    given on the aﬃne pieces    $U_{0}=\operatorname{Spec}A[u,\mu_{1},\mu_{2}]$   and  $U_{1}=A[v,\nu_{1},\nu_{2}]$   by  

$$
\phi|_{U_{0}}(u,\mu_{1},\mu_{2})=\left(u+\mu_{1}\mu_{2},\mu_{1},\mu_{2}\right),\qquad\phi|_{U_{1}}(v,\nu_{1},\nu_{2})=\left(v-\nu_{1}\nu_{2},\nu_{1},\nu_{2}\right)
$$  

As    $\phi$   is invertible,    $\phi\,\in\,\operatorname{Aut}(\mathbb{P}^{m|n})(A)$  , but is not obtained through an element of   $\mathrm{PGL_{2|2}}(A)$  . In fact the coeﬃcient in    $\phi|_{U_{0}}$   of    $\mu_{1}\mu_{2}$   in an automor- phism induced by a   $\mathrm{PGL_{2|2}}(A)$   transformation must be a nilpotent. Hence  $\phi\not\in\mathrm{PGL_{2|2}}(A)$  ) .  

We now want to show that we have an isomorphism between the projective linear supergroup and the automorphism of the super projective when    $n=1$  . The argument we give follows along the lines of the calculation of   $\operatorname{Aut}(\mathbb{P}^{n})$  given in [11] Ch. 2, Sec. 7.  

Proposition 4.4.  We have an isomorphism of supergroup functors:  

$$
\mathrm{PGL}_{m+1|1}\cong\operatorname{Aut}(\mathbb{P}^{m|1})
$$  

In particular,    $\operatorname{Aut}(\mathbb{P}^{m|1})$   is a supergroup scheme.  

Proof.  Proposition 4.2 gives us an embedding of supergroup functors   $\mathrm{PGL}_{m+1|1}$   $\hookrightarrow\operatorname{Aut}(\mathbb{P}^{m|1})$  . Now let    $f\in\operatorname{Aut}(\mathbb{P}_{A}^{m|1})$   and let    $g$   be its inverse. We want to show    $f\,\in\,\mathrm{PGL}_{m+1|1}(A)$  . The automorphism    $f$   induces the two line bundle morphisms    $f^{*}{\mathcal{O}}_{A}(1)\,\longrightarrow\,{\mathcal{O}}_{A}(1)$   and    $g^{*}{\mathcal{O}}_{A}(1)\longrightarrow{\mathcal{O}}_{A}(1)$  ) , where    $\mathcal{O}_{A}(1):=$   $p_{1}^{*}(\mathcal{O}(1))$  ,    $p_{1}:\mathbb{P}_{A}^{m|1}\longrightarrow\mathbb{P}^{m|1}$    being the natural projection. By Prop. 2.3, we know that    $f^{*}{\mathcal{O}}_{A}(1)={\mathcal{O}}(k)\otimes{\mathcal{L}}_{f}$   and    $g^{*}{\mathcal{O}}_{A}(1)={\mathcal{O}}(l)\otimes{\mathcal{L}}_{g}$  . Let us choose a suitable open cover of    $A$   in which both    $\mathcal{L}_{f}$   and    $\mathcal{L}_{g}$   are trivial. By a common abuse of notation we shall still write    $A$   to denote the ring of global sections of an element of the open cover, so we in fact are replacing    $A$   with its lo- calization. With such a choice we have    $f^{*}{\mathcal{O}}_{A}(1)\cong{\mathcal{O}}_{A}(k)$  ,    $g^{*}{\mathcal{O}}_{A}(1)\cong{\mathcal{O}}_{A}(l)$  . Since    $f$   and    $g$   are mutually inverse, we have:  

$$
{\mathcal{O}}_{A}(1)=(f^{*}\circ g^{*})({\mathcal{O}}_{A}(1))=f^{*}(g^{*}({\mathcal{O}}_{A}(1)))=f^{*}({\mathcal{O}}_{A}(l))={\mathcal{O}}_{A}(k l).
$$  

Hence    $k l=1$  , whence    $k=l=1$  , because for    $k=l=-1$   we do not have global sections.  

So    $f^{*}({\mathcal{O}}(1))\cong{\mathcal{O}}(1)$  , and choosing an isomorphism    $F:f^{*}({\mathcal{O}}(1))\to{\mathcal{O}}(1)$  yields an isomorphism of the global sections   $\Gamma(\mathbb{P}^{m},f^{*}\mathcal{O}_{A}(1))\cong\Gamma(\mathbb{P}^{m},\mathcal{O}_{A}(1))$  By composing such an isomorphism with the natural isomorphism  

$$
f^{*}:\Gamma(\mathbb{P}^{m},\mathcal{O}_{A}(1))\longrightarrow\Gamma(\mathbb{P}^{m},f^{*}\mathcal{O}_{A}(1))
$$  

we obtain an    $A$  -linear automorphism  

$$
T_{F}:\Gamma(\mathbb{P}^{m},\mathcal{O}_{A}(1))\longrightarrow\Gamma(\mathbb{P}^{m},\mathcal{O}_{A}(1))
$$  

and identifying   $\Gamma(\mathbb{P}^{m},\mathcal{O}_{A}(1))$   with    $A^{m+1|1}$    we see that    $T_{F}\in\mathrm{GL}_{m+1|1}(A)$  . How- ever,    $T_{F}$   depends on    $F$  . Suppose    $G:f^{*}({\mathcal{O}}(1))\to{\mathcal{O}}(1)$   is another isomor- phism, then    $F^{-1}{\circ}G$   is an automorphism of    $\mathcal{O}(1)$  . Since   $\operatorname{Hom}(L,L)=L^{*}\otimes L=$   $\mathcal{O}$   for any line bundle    $L$  , we see that an automorphism of    $\mathcal{O}(1)$   is the same    $\mathbb{P}_{A}^{m|1}$  thing as an invertible even function on , and    $F$   and    $G$   diﬀer by composing with multiplication by such a function.  

Therefore    $f$   determines    $T_{F}$   only up to multiplication by an invertible even function, i.e.    $f$   uniquely determines an element    $T:=[T_{F}]$   of   $\mathrm{PGL}_{m+1|1}(A)$  .  

Now in suitable coordinates we have that    $T$   induces (up to scalar mul-   tiplication) an automorphism of the  $\mathbb{Z}$  -graded superalgebra    $A[z_{0},.\,.\,.\,,z_{m},\zeta]$  . We leave to the reader the check that    $\phi(T)$   is indeed    $f$  .  

# 5 The SUSY-preserving automorphisms of    $\mathbb{P}_{k}^{1|1}$  

$\mathbb{P}_{k}^{1|1}$  In this section we want to consider those automorphisms of which pre- serve its unique (up to isomorphism) SUSY structure. For all of the standard notation of supergeometry refer to [1].  

Let    $k$   be our ground ﬁeld,   $\operatorname{char}(k)\neq2$  ,    $k$   algebraically closed. All algebraic supergroups discussed below will be algebraic supergroups over    $k$  .  

We recall that if,    $X$   is a smooth algebraic supervariety over    $k$   of dimension  $1|1$  , we deﬁne a  SUSY structure  on    $X$   as a   $0|1$   distribution    $\mathcal{D}$   on    $X$   such that the Frobenius map  

$$
\begin{array}{r}{\mathcal{D}\otimes\mathcal{D}\longrightarrow T X/\mathcal{D}}\\ {Y\otimes Z\mapsto[Y,Z]~\mathrm{mod}~\mathcal{D}}\end{array}
$$  

is an isomorphism (see, for example, [13] for the deﬁnition of SUSY-structure in the complex analytic case). If    $X\,\rightarrow\,S$   is a smooth family of algebraic supervarieties of relative dimension   $1|1$   over an algebraic    $k$  -supervariety    $S$  , then the notion of relative SUSY structure may be deﬁned in the analogous way, as a relative distribution in the relative tangent sheaf    $T X/S$  . In this case we say that    $X\rightarrow S$   is a  relative SUSY family .  

Our discussion is based on [16].  

Let us start by interpreting    $\mathbb{P}_{k}^{1|1}$  as a homogeneous superspace. Let    $\underline{{k}}^{2\vert1}=$   $(k^{2},\mathcal{O}_{\underline{{k}}^{2|1}})$   denote the aﬃne superspace canonically associated to the    $k$  -super vector space    $k^{2|1}$  . Let us consider the action of the algebraic group    $\underline{{\boldsymbol{k}}}^{\times}$    on  $\underline{{k}}^{2|1}\setminus\{0\}$  , given in the functor of points notation by:  

$$
\boldsymbol{t}\cdot\left(z_{0},z_{1},\zeta\right)=\left(t z_{0},t z_{1},t\zeta\right)
$$  

Consider the projection (as topological map):  

$$
\pi:k^{2}\setminus\{0\}\longrightarrow k^{2}\setminus\{0\}/\,k^{\times}\cong\mathbb{P}^{1}
$$  

Deﬁne the sheaf on the topological space    $\mathbb{P}_{k}^{1}$    consisting of the    $\underline{{\boldsymbol{k}}}^{\times}$  -invariant sections:  

$$
\mathcal{F}(U):={\mathcal{O}}_{k^{2\vert1}}(\pi^{-1}(U)))^{\underline{{k}}^{\times}}
$$  

$\mathbb{P}_{k}^{1|1}$  One can readily check that  $(\mathbb{P}_{k}^{1},\mathcal{F})$   is the superscheme as deﬁned in Sec. 2.  

Let    $\mathcal{Z}_{0}$  ,    $\mathcal{Z}_{1}$  ,    $\zeta$   be global coordinates on    $\underline{{k}}^{2\vert1}$  . We now consider the Euler vector ﬁeld    $E\,=\,z_{0}\partial_{z_{0}}+z_{1}\partial_{z_{1}}+\zeta\partial_{\zeta}$  , which represents (in the chosen coordi- nates) the inﬁnitesimal generator for the    $\underline{{k}}^{\times}$    action on    $\underline{{k}}^{2\vert1}\setminus\{0\}$  . Since    $E$  is everywhere nonsingular, it generates a trivial   $1|0$   line bundle. As in the    $\mathbb{P}_{k}^{1|1}$  classical case, we have the Euler exact sequence of vector bundles on :  

$$
0\to{\mathcal{O}}^{1|0}\to{\mathcal{O}}(1)\otimes\operatorname{Der}(S)\stackrel{j}{\to}T\mathbb{P}_{k}^{1|1}\to0
$$  

where    $i$   is the inclusion of the trivial   $1|0$   line bundle    $\left\langle E\right\rangle$  with global basis the Euler vector ﬁeld. Here   $\mathrm{Der}(S)$   is the    $k$  -super vector space of    $k$  -linear derivations on    $S:=\mathrm{Sym}((k^{2|1})^{*})$  ; it has as basis the derivations    $\partial_{z_{i}},\partial_{\zeta}$  . Thus  $\mathcal{O}(1)\otimes\mathrm{Der}(S)$   is the sheaf whose sections on    $U$   are the linear vector ﬁelds on    $\pi^{-1}(U)$  . Any local section of    $\mathcal{O}(1)\!\otimes\!\mathrm{Der}(S)$   induces a corresponding local  $k$  -linear derivation on    $\mathcal{O}_{\mathbb{P}_{k}^{1|1}}$    by restricting it to act on    $\underline{{\boldsymbol{k}}}^{\times}$  -invariant functions; this deﬁnes    $j$  . Injectivity of    $i$   and the inclusion   $\mathrm{im}(i)\subseteq\ker(j)$   follow from the fact that    $E$   is nonsingular and the inﬁnitesimal generator for the    $\underline{{k}}^{\times}$  -action; a standard calculation in the usual aﬃne cells shows that   $\ker(j)\subseteq\operatorname{im}(i)$  and that    $j$   is surjective. Note that the sequence continues to remain exact on    $\mathbb{P}_{A}^{1|1}$    after base change to any aﬃne    $k$  -supervariety   ${\underline{{\mathrm{Spec}}}}(A)$  , with    $T\mathbb{P}_{k}^{1|1}$  replaced by the relative tangent bundle    $T\mathbb{P}_{A}^{1|1}/{\mathrm{Spec}}(A)$  . We will denote the  $A$  -superalgebra    $S\otimes_{k}A$   by    $S_{A}$  .  

We now come to the SUSY structure.  

Deﬁnition 5.1.  Let  (  ${\cal X}\,\rightarrow\,{\cal S},{\mathcal D}_{\mathcal{L}}$  )  be a relative SUSY family. An    $S$  -auto- morphism    $f:X\to X$   is    $S U S Y$   structure-preserving  (or simply  SUSY-pre- serving ) if and only if    $(d f_{p})(\mathcal{D}_{p})=\mathcal{D}_{f(p)}$   for any    $p\in X$  .  

We will consider SUSY structures given by sections of    $\mathcal{O}_{A}(1){\otimes}\Omega_{S/A}$  . Here

  $\Omega_{S/A}$   denotes the    $A$  -module of K¨ ahler diﬀerentials on    $S_{A}$  , i.e. the    $A$  -dual to

  $\mathrm{Der}(S_{A})$  ; it has as basis the diﬀerentials    $d z_{i},d\zeta$  . When we speak of the kernel of a section    $\omega$   of    $\mathcal{O}_{A}(1){\otimes}\Omega_{S/A}$  , we mean the kernel of    $\omega$   when    $\omega$   is interpreted as a morphism of sheaves of    $\mathcal{O}_{\mathbb{P}_{A}^{1|1}}$  -modules from    $\mathcal{O}_{A}(1)\otimes\mathrm{Der}(S_{A})\to\mathcal{O}_{A}(2)$  .  

Proposition 5.2.  Let    $s:=z_{1}\,d z_{0}-z_{0}\,d z_{1}-\zeta\,d\zeta$  . Then the image of    $\ker(s)$     $\mathbb{P}_{k}^{1|1}$  under    $j$   is a SUSY structure on .  

Proof.  In the aﬃne open subsupervariety    $U_{1}:=\left\{z_{1}\neq0\right\}\subset\mathbb{P}_{k}^{1|1}$  , one calculates that the Euler vector ﬁeld    $E$   and the linear vector ﬁeld    $\widehat{Z}_{1}=\zeta\partial_{z_{0}}+z_{1}\partial_{\zeta}$   lie in  $\ker(s)$   and are linearly independent. At any point    $p\in\mathbb{P}_{k}^{1|1}$  ,    $s$   induces a linear map of super vector spaces    $s_{p}:[\mathcal{O}(1)\otimes\mathrm{Der}(S)]_{p}\to[\mathcal{O}(2)]_{p}$   on the ﬁbers. It is clear that    $s$   is a basepoint-free section, hence    $s_{p}$   is always surjective. By linear algebra,   $\ker(s_{p})$   is   $1|1$   dimensional and hence    $E_{p}$   and    $\widehat{Z_{1,p}}$   span   $\ker(s_{p})$  . By the super Nakayama’s lemma,    $E$   and    $\widehat{Z_{1}}$   span   $\ker(s)$   near   . Since    was  $p$   $p$  arbitrary,    $E$   and    $\widehat{Z_{1}}$   form a basis for   $\ker(s)$   in    $U_{1}$  .  

One sees that    $Z_{1}:=\,j\big(\widehat{Z_{1}}\big)\,=\,\partial_{\eta}+\eta\partial_{w}$  , where    $w\,=\,z_{0}/z_{1},\eta\,=\,\zeta/z_{1}$   are the usual aﬃne coordinates in    $U_{1}$  .    $Z_{1}^{2}=\partial_{w}$   and so    $Z_{1}$   deﬁnes a SUSY structure in    $U_{1}$  . A similar calculation with the linear vector ﬁeld    $\widehat{Z}_{0}:=-\zeta\partial_{z_{1}}+z_{0}\partial_{\zeta}$  shows that    $j(\ker(s))$   deﬁnes a SUSY structure on    $U_{0}\,=\,\bigl\{z_{0}\,\neq\,0\bigr\}$  , hence the    $\mathbb{P}_{k}^{1|1}$  image of   $\ker(s)$   under    $j$   deﬁnes a SUSY structure on .  

We note that by the considerations of [10], this is the unique SUSY struc-    $\mathbb{P}_{k}^{1|1}$  ture on , up to SUSY-isomorphism.  

We now need the following proposition. The proof is completely similar to the one in [10] Prop. 5.2, however since the context here is more general, we include it for completeness.  

Lemma 5.3.  Let    $A$   be an aﬃne    $k$  -superalgebra. Let    $\omega,\omega^{\prime}$    be two global sec- tions of    $\mathcal{O}_{A}(1)\otimes\Omega_{S/A}$   such that    ${\mathcal{D}}\;:=\;j\big(\mathrm{ker}\big(\omega\big)\big),{\mathcal{D}}^{\prime}\;:=\;j\big(\mathrm{ker}\big(\omega^{\prime}\big)\big)$   are    $0|1$  distributions on    $\mathbb{P}_{A}^{1|1}$  . Suppose    $\mathcal{D}=\mathcal{D}^{\prime}$  . Then    $\omega^{\prime}=h\omega$   for some even invertible function    $h$   on    $\mathbb{P}_{A}^{1|1}$  .  

Proof.  Let    $p\,\in\,\mathbb{P}_{A}^{1|1}$  be a point. Since    $\mathcal{D}$   is  locally a direct summand of  $T\mathbb{P}_{A}^{1|1}/{\underline{{\mathrm{Spec}}}}(A)$   , we have a local splitting    ${\mathcal{D}}|_{U}\oplus{\mathcal{E}}\,=\,(T{\mathbb{P}}_{A}^{1|1}/{\mathrm{Spec}}(A))|_{U}$   in some neighborhood    $U\,\ni\,p$  . Via the Euler exact sequence (base changed to  $\operatorname{Spec}(A))$  , we may lift    ${\mathcal{D}}|_{U}$   (resp.    $\mathcal{E}$  ) uniquely to a rank   $1|1$   (resp. 2 ∣ 0) sub- module  $\widehat{\mathcal{D}}$   (resp.    $\widehat{\mathcal E}$  ) of  $[\mathcal{O}_{A}(1){\otimes}\mathrm{Der}(S_{A})]|_{U}$   containing the   $1|0$   line bundle    $\left\langle E\right\rangle$  spanned by the Euler vector ﬁeld, such that    ${\widehat{\mathcal{D}}}\cap{\widehat{\mathcal{E}}}=\left\langle E\right\rangle$  . We may therefore ﬁnd local sections    $\widehat{Z}$   (resp. X ) of    $\widehat{\mathcal{D}}$   (resp    $\mathcal{\widehat{E}}$  ) such that    ${\widehat{Z}},E$   (resp.  ${\widehat{X}},E)$  form a basis for    $\widehat{\mathcal{D}}$   (resp.    $\mathcal{\widehat{E}}$  ). Note that the condition  $\widehat{\mathcal{D}}\cap\widehat{\mathcal{E}}=\left<E\right>$  implies  $\widehat{X},\widehat{Z},E$   form a basis of    $[\mathcal{O}_{A}(1)\otimes\mathrm{Der}(S_{A})]|_{U}$  .  

Viewing    $\omega|_{U}$   as an    $\mathcal{O}_{\mathbb{P}_{A}^{1|1}}$    -linear map from    $[\mathcal{O}_{A}(1)\!\otimes\!\mathrm{Der}(S_{A})]|_{U}$   to    $\mathcal{O}_{A}(2)|_{U}$  , we have an induced linear map of super vector spaces  

$$
\omega_{p}:({\mathcal{O}}_{A}(1)\otimes\operatorname{Der}(S_{A}))_{p}\to({\mathcal{O}}_{A}(2))_{p}.
$$  

As   $\ker(\omega_{p})_{\r}=s p a n\{\widehat{Z}_{p},E_{p}\}$  , we see by linear algebra that  $\omega_{p}$   is a surjection, and that    $\omega_{p}\big(\widehat{X}_{p}\big)$  )  is a basis for    $(\mathcal{O}_{A}(2))_{p}$  ; the analogous conclusion holds for  $\omega_{p}^{\prime}$    and    $\omega_{p}^{\prime}\big(\widehat{X}_{p}\big)$  . Hence by the super Nakayama’s lemma,    $\omega({\widehat{X}})$   is a basis for

  $\mathcal{O}_{A}(2)|_{U}$  , and the same is true of    $\omega^{\prime}\big(\widehat{X}\big)$  )  (shrinking    $U$   if necessary). Hence

  $\omega^{\prime}(\widehat{X})/\omega(\widehat{X})$  (   is an invertible even function on    $U$  ; let us denote it by    $h$  .  

To show that    $h$   is independent of the local complement    $\mathcal{E}$   and the choice of basis element  $\widehat{X}$  , suppose    $\mathcal{E}^{\prime}$    is another local complement to    $\mathcal{D}$   on    $U$  , and let  $\widehat{X}^{\prime},E$   be a basis of the lift  $\widehat{\mathcal{E}^{\prime}}$    of    $\mathcal{E}^{\prime}$  . Then we have  $\widehat{X}^{\prime}=a\widehat{X}+b E+\alpha\widehat{Z}$    ̂   ̂  for some    $a,b,\alpha\in{\mathcal{O}}_{\mathbb{P}_{A}^{1|1}}(U)$  ,    $a,b$   even and    $\alpha$   odd. As    $\widehat{X},E,\widehat{Z}$   and    $\widehat{X}^{\prime},E,\widehat{Z}^{\prime}$    are both local bases for    $\mathcal{O}_{A}(1)\otimes\mathrm{Der}(S_{A})$  ,    $a$   must be a unit.  

Then we have  

$$
\begin{array}{r l}&{\omega^{\prime}(\widehat{X}^{\prime})/\omega(\widehat{X}^{\prime})=\omega^{\prime}(a\widehat{X}+b E+\alpha\widehat{Z})/\omega(a\widehat{X}+b E+\alpha\widehat{Z})}\\ &{\qquad\qquad\qquad\qquad=\omega^{\prime}(\widehat{X})/\omega(\widehat{X})}\end{array}
$$  

since    $\omega,\omega^{\prime}$    both annihilate    $E$   and    $\widehat{Z}$  . This proves that the expression  $\omega^{\prime}(\widehat{X})/\omega(\widehat{X})$  (   is independent of all choices and hence    $h$   is a well-deﬁned func-    $\mathbb{P}_{A}^{1|1}$  tion on all of . The equality    $\omega^{\prime}=h\omega$   clearly holds locally, and since    $h$   is now known to be globally deﬁned, it holds globally.  

Proposition 5.4.  Let    $f$   be an automorphism of    $\mathbb{P}_{A}^{1|1}$  . Then    $f$   preserves the SUSY structure deﬁned by  s  if and only if for some (hence every) lift    $\widetilde{f}$   of    $f$  to    $\mathrm{GL_{2|1}}(A)$  ,    $\widetilde{f}^{*}(s)=t s$   for some invertible function    $t$  .  

Proof.  We begin by noting that   $\mathrm{GL_{2|1}}(A)$   preserves    $A_{0}^{*}$  -invariant open subsets of    $\mathbb{A}_{A}^{2|1}\backslash\{0\}$  , hence it acts naturally by pullback of functions on    $\mathcal{O}_{A}(1)\otimes$   $\mathrm{Der}(S_{A})$  , where we interpret the latter as the sheaf assigning to any open subset    $U\subseteq\mathbb{P}_{A}^{1|1}$    the linear vector ﬁelds on    $\pi^{-1}(U)\subseteq\mathbb{A}_{A}^{2|1}\backslash\{0\}$  .  

The subsupergroup of invertible scalar matrices    $\{c I\,:\,c\,\in\,A_{0}^{*}\}$   is cen- tral in   $\mathrm{GL_{2|1}}(A)$  , hence this   $\mathrm{GL_{2|1}}(A)$  -action preserves the subalgebra of    $A_{0}^{*}$  -    $\mathbb{A}_{A}^{2|1}\backslash\{0\}$  invariant functions on any    $A_{0}^{*}$  -invariant open subset of . Hence we have an induced   $\mathrm{GL_{2|1}}(A)$  -action on the sheaf    $\mathcal{O}_{\mathbb{P}^{1|1}}$    . Clearly, invertible scalar matrices act trivially on    ${\mathcal{O}}_{\mathbb{P}_{A}^{1|1}}$  , hence the   $\mathrm{GL_{2\vert1}}\overset{A}{(A)}$  -action on    $\mathcal{O}_{\mathbb{P}_{A}^{1|1}}$  factors through   $\mathrm{PGL_{2|1}}(A)$  .  

We see from the above that the action of   $\mathrm{GL_{2|1}}(A)$   on    $\mathcal{O}_{A}(1){\otimes}\mathrm{Der}(S_{A})$   by pullback of functions induces naturally a   $\mathrm{PGL_{2|1}}(A)$  -action on    $\mathcal{O}_{\mathbb{P}_{A}^{1|1}}$  , hence on    $T\mathbb{P}_{A}^{1|1}/{\underline{{\mathrm{Spec}}}}(A)$  , also given by pullback of functions. But this is precisely the   $\mathrm{PGL_{2|1}(\cal{A})}.$  -action on    $T\mathbb{P}_{A}^{1|1}/{\underline{{\mathrm{Spec}}}}(A)$  )  induced by the action of   $\mathrm{PGL_{2|1}}(A)$     $\mathbb{P}_{A}^{1|1}$  on   by automorphisms.  

Recalling that the sheaf morphism    $j:{\mathcal{O}}_{A}(1)\otimes\operatorname{Der}(S_{A})\to T{\mathbb{P}}_{A}^{1|1}/\operatorname{Spec}(A)$  is just given by restricting a linear vector ﬁeld to act on    $A_{0}^{*}$  -invariant func- tions, we see    $j$   is equivariant with respect to the   $\mathrm{GL_{2|1}}(A)$  - and   $\mathrm{PGL_{2|1}}(A)$  - actions previously deﬁned.  

We also have a   $\mathrm{GL_{2|1}}(A)$  -action on    $\mathcal{O}_{A}(1)\otimes\Omega_{S/A}$   by the natural action on both factors, and for    $\omega\in\Gamma(\mathcal{O}_{A}(1)\otimes\Omega_{S/A})=\Gamma(\mathcal{O}_{A}(1))\otimes\Omega_{S/A}$  , we write  $g^{*}(\omega)$   for    $g\cdot\omega$  .  

Since the action of   $\mathrm{GL_{2|1}}(A)$   on    $\mathcal{O}_{A}(1)\otimes\mathrm{Der}(S_{A})$   is the same as the natural action on the individual factors, and the   $\mathrm{GL_{2|1}}(A)$  -action on   $\Omega_{S/A}$  is dual to that on   $\operatorname{Der}(S_{A})$  , it follows that the evaluation pairing    $[\mathcal{O}_{A}(1)\otimes$   $\mathrm{Der}(S_{A})]\otimes[\mathcal{O}_{A}(1)\otimes\Omega_{S/A}]\rightarrow\mathcal{O}_{A}(2)$   is   $\mathrm{GL_{2|1}}(A)$  -equivariant, where    $\mathcal{O}_{A}(2)$  is endowed with the natural   $\mathrm{GL_{2\vert1}}(A)$  -action.  

From the preceding discussion, we see that    $f$   is SUSY-preserving if and only if    $j[\ker(\omega)]_{p}=j[\ker(\widetilde{f}^{*}(\omega)]_{p}$   for any point    $p$  .  

We claim this is true if and only if    $j[\ker(\omega)]=j[\ker(\widetilde{f}_{-}^{*}(\omega))]$  . One di- rection is clear. For the other, suppose    $j[\ker(\omega)]_{p}=j[\ker(\bar{f}^{*}(\omega))]_{p}$   for any point    $p$  . Then by the super Nakayama’s lemma    $j[\ker(\omega)]\,=\,j[\ker(\widetilde{f}^{*}(\omega))]$  in a neighborhood of    $p$  , hence globally. The claim then follows from Lemma 5.3.  

In order to determine the supergroup of SUSY-preserving automorphisms    $\mathbb{P}_{k}^{1|1}$  of we must discuss various other supergroups. We follow closely the discussion in [13].  

Deﬁnition 5.5.  The 2 ∣ 1-dimensional  conformal symplecticorthogonal super- group    $\mathrm{C_{2\lvert1}}$   is the subfunctor of   $\mathrm{GL_{2|1}}$   that preserves, up to multiplication by an even invertible constant, the split nondegenerate supersymplectic form on  $k^{2|1}$    given by    $(v,w)=v^{t}H w$  , where  

$$
H:=\left(\!\!{\begin{array}{l l l}{0}&{1}&{0}\\ {-1}&{0}&{0}\\ {0}&{0}&{-1}\end{array}}\!\!\right),
$$  

and    $t$    denotes the super transpose of a matrix. More precisely, for every  $k$  -superalgebra    $A$  ,   $\mathrm{C_{2\lvert1}}$   is the functor    $(\mathrm{slg})_{\mathrm{k}}\rightarrow(\mathrm{grps})$   given by  

$$
\mathrm{C}_{2|1}(A):=\{B\in\mathrm{GL}_{2|1}(A)\,:\,B^{t}H B=Z(B)H\},
$$  

where    $Z:\mathrm{GL_{2\vert1}}\rightarrow\mathbb{G}_{m}^{1\vert0}$    is a ﬁxed homomorphism.  

The   $2|1$  -dimensional  projective conformal sym ple c tic orthogonal supergroup  $\mathrm{PC_{2\vert1}}$   is the image of   $\mathrm{C_{2\lvert1}}$   in   $\mathrm{PGL_{2|1}}$  , i.e, it is the sheaﬁﬁcation of the group- valued functor    $A\to\mathrm{C}_{2\vert1}(A)/\{a I:a\in A_{0}^{*}\}$  .  

Proposition 5.6.    $\mathrm{C_{2\lvert1}}$   and  PC 2 ∣ 1  are representable.  

Proof.  Taking the Berezinian of both sides of (7), one sees that    $Z(B)\;=$   $\mathrm{Ber}(B)^{2}$  . Thus, given  

$$
B=\left(\!\!\begin{array}{c c c}{{a}}&{{b}}&{{\alpha}}\\ {{c}}&{{d}}&{{\beta}}\\ {{\gamma}}&{{\delta}}&{{e}}\end{array}\!\!\right)\in\mathrm{GL_{2\vert1}}(A),
$$  

a direct calculation shows that    $B$   satisﬁes (7) if and only if the following equations hold:  

$$
\begin{array}{l}{{e^{2}+2\alpha\beta=\mathrm{Ber}(B)^{2}}}\\ {{a d-b c-\gamma\delta=\mathrm{Ber}(B)^{2}}}\\ {{a\beta-c\alpha-e\gamma=0}}\\ {{b\beta-d\alpha-e\delta=0.}}\end{array}
$$  

Thus these equations deﬁne  $\mathrm{C_{2\lvert1}}$   as a closed aﬃne algebraic subsupergroup of   $\mathrm{GL_{2|1}}$  .  

To prove that   $\mathrm{PC_{2\vert1}}$   is representable, we use the trick of [13]. Let SC 2 ∣ 1 denote the functor    $(\mathrm{slg})_{\mathrm{k}}\rightarrow(\mathrm{grps})$   given by  

$$
\mathrm{SC}_{2|1}(A):=\{B\in\mathrm{C}_{2|1}(A):\mathrm{Ber}(B)=1\}.
$$  

Since its deﬁning equations are those of   $\mathrm{C_{2\lvert1}}$   together with the equation  $\mathrm{Ber}(B)=1$  ,   $\mathrm{SC_{2\lvert1}}$   is a closed aﬃne algebraic subsupergroup of   $\mathrm{GL_{2|1}}$  . There is a short exact sequence of supergroups  

$$
0\to\mathrm{SC}_{2\vert1}\to\mathrm{C}_{2\vert1}\xrightarrow{\mathrm{Ber}}\mathbb{G}_{m}^{1\vert0}\to0.
$$  

There is a splitting of this sequence, given on    $A$  -points by sending    $a\,\in\,A_{0}^{*}$     $\mathbb{G}_{m}^{1|0}$  to    $a I$  , and the image of   under the splitting is clearly normal in   $\mathrm{C_{2\lvert1}}$  , hence   $\mathrm{C_{2\lvert1}}$   is the internal direct product of SC 2  $\mathrm{!}$   and the subsupergroup  $\{a I:a\,\in\,A_{0}^{*}\}$  } . This direct product decomposition allows us to naturally identify the functor   $\mathrm{PC_{2\vert1}}$   with the functor of points of   $\mathrm{SC_{2\lvert1}}$  ; in particular, we see   $\mathrm{PC_{2\vert1}}$   is an aﬃne algebraic supergroup, isomorphic to   $\mathrm{SC_{2\lvert1}}$  .  

Deﬁnition 5.7.  The   $2|1$  -dimensional  sym ple c tic orthogonal supergroup  SpO  $^{2\vert1}$  is the functor    $(\mathrm{slg})_{\mathrm{k}}\rightarrow(\mathrm{grps})$  

$$
\mathrm{SpO}_{2|1}(A):=\{B\in\mathrm{GL}_{2|1}(A)\,:\,B^{t}H B=H\}.
$$  

Remark 5.8.  SpO  $^{2\vert1}$   is well-known to be representable; the reader may read- ily write down deﬁning equations for SpO , completely analogous to those  $^{2\vert1}$  for   $\mathrm{C_{2\lvert1}}$  , which show that   $\mathrm{SpO_{2\vert1}}$   is a closed aﬃne algebraic subsupergroup of  $\mathrm{GL_{2|1}}$  .  

Proposition 5.9.  PC 2 ∣ 1  is isomorphic to the irreducible component    $\mathrm{(SpO_{2\vert1})}$  ) 0 of  SpO  $2|1$   containing the identity.  

Proof.  Taking the Berezinian of both sides of (9) shows that   $\mathrm{Ber}(B)=\pm1$   for any    $B\in\mathrm{SpO_{2|1}}(A)$  . This yields a short exact sequence of supergroups  

$$
0\to\mathrm{SC}_{2\mid1}\to\mathrm{SpO}_{2\mid1}\overset{\mathrm{Ber}}{\longrightarrow}\{\pm1\}\rightarrow0.
$$  

which is split by the morphism    $\pm1\,\mapsto\,\pm I$   and    $\{\pm I\}$   is obviously normal in  $\mathrm{SpO_{2\vert1}}$  . Thus   $\mathrm{SpO_{2\vert1}}$   is the internal direct product of    $\{\pm I\}$   and   $\mathrm{SC_{2\lvert1}}$  . Note that   $\mathrm{SC_{2\lvert1}}$   is irreducible (one sees from its deﬁning equations that its reduced algebraic group is   $\mathrm{SL_{2}}$  , which is known to be irreducible). Let    $(\mathrm{SpO_{2\vert1}})^{0}$    de- note the irreducible component of   $\mathrm{SpO_{2\vert1}}$   that contains the identity. We claim  $\mathrm{SC_{2\lvert1}}=(\mathrm{SpO_{2\lvert1}})^{0}$  . Since    $I\in\mathrm{SC_{2\vert1}}\cap(\mathrm{SpO_{2\vert1}})^{0}$  , it is clear   $\mathrm{SC_{2\lvert1}\subseteq(S p O_{2\lvert1})^{0}}$  . Conversely, we see that    $(\mathrm{SpO_{2|1}})^{0}\subseteq\mathrm{SC_{2|1}}$  : the restriction of the morphism Ber to the irreducible supervariety    $(\mathrm{SpO_{2|1}})^{0}$    must be constant, hence equal to 1. Since we previously showed   $\mathrm{PC_{2\vert1}}$   is isomorphic to  $\mathrm{SC_{2\lvert1}}$  , the proposition is proven.  

Theorem 5.10.  The algebraic supergroup  Aut SUSY  $(\mathbb{P}_{k}^{1|1})$   of SUSY preserving automorphisms of    $\mathbb{P}_{k}^{1|1}$  is isomorphic to    $\mathrm{(SpO_{2\lvert1})^{\bullet}}$  0 .  

Proof.  As   $\operatorname{AutSY}\big(\mathbb{P}_{k}^{1|1}\big)$   is a sheaf, the theorem reduces to the case of calcu- lating   $\mathrm{Aut}_{\mathrm{SUSY}}(\mathbb{P}_{k}^{1|1})(A)$   where    $A$   is a    $k$  -superalgebra. For this, we note that  $\mathbb{P}_{A}^{1|1}$     $\mathbb{P}_{k}^{1|1}$    has the SUSY structure over    $A$   induced by base change from , given by    $s$  .  

$\mathbb{P}_{A}^{1|1}$    Let    $g\,\in\,\mathrm{PGL_{2|1}}(A)$   be an automorphism of , and  $\widehat{g}$   a lift of    $g$   to  $\mathrm{GL_{2|1}}(A)$  . Recall that we have a natural action of the group of    $A$  -points of   $\mathrm{GL_{2|1}}(A)$   on   $\Gamma(\mathcal{O}_{A}(1)\otimes\Omega_{S/A})$  . More concretely, in the given coordinates we have for any matrix    ${\widehat{g}}\in\mathrm{GL_{2\left|1\right.}}(A)$  :  

$$
\begin{array}{r}{\widehat{g}\!\cdot\!\left(\!\!\begin{array}{l}{z_{0}}\\ {z_{1}}\\ {\zeta}\end{array}\!\right)\!=\,\widehat{g}\!\left(\!\!\begin{array}{l}{z_{0}}\\ {z_{1}}\\ {\zeta}\end{array}\!\right),\qquad\widehat{g}\!\cdot\!\left(\!\!\begin{array}{l}{d z_{0}}\\ {d z_{1}}\\ {d\zeta}\end{array}\!\right)\!=\,\widehat{g}\!\left(\!\!\begin{array}{l}{d z_{0}}\\ {d z_{1}}\\ {d\zeta}\end{array}\!\right)}\end{array}
$$  

where we write    $z_{i}$   for    $z_{i}\otimes1$   and so on.  

By Prop. 5.3,    $g$   is SUSY-preserving if and only if    $\widehat{g}$   sends  

$$
s=z_{1}d z_{0}-z_{0}d z_{1}-\zeta d\zeta=\left(z_{0}\quad z_{1}\quad\zeta\right)H\left({d z_{0}\atop d\zeta}\right),\qquad H=\left({0\atop-1}\quad1\quad0\atop0\quad0\atop0\quad-1\right),
$$  

to a multiple of    $s$   by an invertible even function. Hence  

$$
\left(z_{0}\quad z_{1}\quad\zeta\right)\widehat{g}^{t}H\widehat{g}\left(\!\!\begin{array}{c}{{d z_{0}}}\\ {{d z_{1}}}\\ {{d\zeta}}\end{array}\!\!\right)=\left(z_{0}\quad z_{1}\quad\zeta\right)Z(\widehat{g})H\left(\!\!\begin{array}{c}{{d z_{0}}}\\ {{d z_{1}}}\\ {{d\zeta}}\end{array}\!\!\right),
$$  

i.e.    $\widehat{g}\in\mathrm{C_{2\left1}}(A\right)$  ) . It follows from equation (8) that    $g$   lies in   $\mathrm{PC}_{2\vert1}(A)$  , which is naturally identiﬁed with    $(\mathrm{SpO_{2|1}})^{0}(A)$   by Prop. 5.9.  

# References  

[1] C. Carmeli, L. Caston, R. Fioresi,  Mathematical Foundation of Super- symmetry , with an appendix with I. Dimitrov, EMS Ser. Lect. Math., European Math. Soc., Zurich, 2011. [2] L. Crane, J. Rabin,  Super Riemann surfaces: uniformization and Teich- muller theory , Comm. Math. Phys. Vol. 113, no. 4, 601-623, 1988. [3] J. Bernstein, notes by P. Deligne, J. Morgan,  Notes on supersymmetry (following J. Bernstein) , in: “Quantum Fields and Strings. A Course for Mathematicians”, Vol. 1, AMS, 1999.  

[4] R. Donagi, E. Witten, Supermoduli Space Is Not Projected , arXiv:1304.7798. [5] D. Eisenbud and J. Harris,  The geometry of schemes.  Springer Verlag, New York, 2000. [6] R. Fioresi, F. Gavarini,  Algebraic supergroups with Lie superalgebras of classical type . J. Lie Theory 23 (2013), no. 1, 143-158. [7] R. Fioresi, F. Gavarini,  Chevalley supergroups . Mem. Amer. Math. Soc. 215 (2012), no. 1014. [8] R. Fioresi, F. Gavarini,  On the construction of Chevalley supergroups . Supersymmetry in mathematics and physics, 101-123, Lecture Notes in Math., 2027, Springer, Heidelberg, 2011. [9] R. Fioresi, S. D. Kwok,  On SUSY curves , in “Advances in Lie Superal- gebras” M. Gorelik, Papi, P. (Eds.), Springer INdAM Series,  7  (2014).

 [10] R. Fioresi, M. A. Lledo.  The Minkowski and Conformal Superspaces , World Scientiﬁc Publishing, 2015.

 [11] R. Hartshorne, Algebraic Geometry. Springer, 1997.

 [12] S. D. Kwok,  Super Morita Theory , submitted.

 [13] Y. I. Manin,  Topics in Noncommutative Geometry ; Princeton University Press, 1991.

 [14] Y. I. Manin,  Gauge Field Theory and Complex Geometry ; translated by N. Koblitz and J.R. King. Springer-Verlag, Berlin-New York, 1988.

 [15] Y. Sun, PGL  $_n$  and automorphisms of projective space . www.math.harvard.edu/ ∼ gaitsgde/Schemes 2009/Yi-notes.pdf, 2009.

 [16] E. Witten, Notes on super Riemann surfaces and their moduli , arXiv:1209.2459.  