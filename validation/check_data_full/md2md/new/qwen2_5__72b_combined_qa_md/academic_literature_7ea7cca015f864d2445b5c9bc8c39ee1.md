# Quiver Laplacians and Feature Selection 

Otto Sumray ${ }^{1,2}$, Heather A. Harrington ${ }^{2,3,4,5}$, Vidit Nanda ${ }^{2}$


#### Abstract

The challenge of selecting the most relevant features of a given dataset arises ubiquitously in data analysis and dimensionality reduction. However, features found to be of high importance for the entire dataset may not be relevant to subsets of interest, and vice versa. Given a feature selector and a fixed decomposition of the data into subsets, we describe a method for identifying selected features which are compatible with the decomposition into subsets. We achieve this by re-framing the problem of finding compatible features to one of finding sections of a suitable quiver representation. In order to approximate such sections, we then introduce a Laplacian operator for quiver representations valued in Hilbert spaces. We provide explicit bounds on how the spectrum of a quiver Laplacian changes when the representation and the underlying quiver are modified in certain natural ways. Finally, we apply this machinery to the study of peak-calling algorithms which measure chromatin accessibility in single-cell data. We demonstrate that eigenvectors of the associated quiver Laplacian yield locally and globally compatible features.


## 1. Introduction

When working with large quantities of unstructured data, it is often convenient and on occasion, indispensable - to employ a family of real-valued features defined on the dataset. It has, for instance, become standard practice within natural language processing to embed words into Euclidean space based on their relative proximity to each other in a substantial corpus of text [23]. In this case, the coordinates serve as features. Regardless of how such an embedding has been obtained, one immediately seeks to simplify matters by identifying those features which are most relevant to the task at hand. There are several ways of quantifying the relevance of a given feature - one may use domain-specific context, optimise a statistical quantity such as variance, or exploit the presence of labelled training data, etc. This process of feature selection forms a cornerstone of data analysis. Examples of well-known feature selectors include principal components [26], LASSO [32] and recursive feature elimination [15], to name but a few.

[^0]
[^0]:    Email of corresponding author: otto.sumray@maths.ox.ac.uk
    ${ }^{1}$ LUDWIG CANCER RESEARCH, UNIVERSITY OF OXFORD
    ${ }^{2}$ MATHEMATICAL INSTITUTE, UNIVERSITY OF OXFORD
    ${ }^{3}$ MAX PLANCK INSTITUTE OF MOLECULAR CELL BIOLOGY AND GENETICS
    ${ }^{4}$ CENTRE FOR SYSTEMS BIOLOGY DRESDEN
    ${ }^{5}$ FACULTY OF MATHEMATICS, TECHNISCHE UNIVERSITÄT DRESDEN




---

We focus here on feature selection in the presence of an auxiliary decomposition of the given dataset. As a toy example of the situation which we have in mind, let us consider the plots in Figure 1 of two features defined on datasets which have been decomposed into two overlapping subsets $A$ and $B$.



FIGURE 1. Two features defined on a dataset equipped with a decomposition into two overlapping subsets.

Suppose we rank the relevance of features by their variance. In Figure 1.I, feature 1 is most relevant for subsets $A, B$, and $A \cap B$, but would not be more relevant than feature 2 on their union $A \cup B$. On the other hand in Figure 1.II, feature 1 is most relevant for $A$, and feature 2 for $B$, but both are equally relevant for $A \cap B$ and $A \cup B$. Such unfortunate inconsistencies arise quite frequently, especially in biological contexts - we are often interested in features defined on datasets that are naturally organised by types, sub-types and so forth, such as disease or cell types. For such data, any feature selection process (which remains agnostic to the decomposition) is liable to select features that are irrelevant to certain subsets while ignoring features that are relevant to certain subsets.

This Paper. Here we present a principled framework for selecting features on a finite set $X$ that are consistent with respect to a decomposition of $X$ into a cover $\mathcal{U}$. Crucially, the subsets of $X$ which comprise $\mathcal{U}$ are allowed to admit arbitrary overlaps. Given the immense diversity of available feature selectors and their inner workings, we adopt an abstract approach. Let $\mathbb{K}$ denote either the field $\mathbb{R}$ of real numbers or the field $\mathbb{C}$ of complex numbers. For our purposes, a feature selector $S$ is any deterministic process that
(1) accepts as input some finite collection $F$ of functions $X \rightarrow \mathbb{K}$, and
(2) outputs a subspace $S_{X}^{F}$ of the $\mathbb{K}$-linear span $V(F)$ of $F$.

We assume an inner product structure on $V(F)$, but impose no further constraints on $S$; as such, the results and constructions of this paper may be applied verbatim to any of the standard feature selectors. Similarly, there are no constraints on the cover $\mathcal{U}$ besides the requirement that $X=\bigcup_{U \in \mathcal{U}} U$.

For the purposes of these introductory remarks, let us call a nonempty subset $\sigma \subset \mathcal{U}$ admissible whenever the intersection $|\sigma|:=\bigcap_{U \in \sigma} U$ is nonempty. Our quest here is to isolate the largest subspace of $S_{X}^{F}$ that is compatible with respect to the decomposition of $X$ into admissible subsets. Two forms of compatibility are studied here: local and global.




---

Given an admissible subset $\sigma \subset U$, a feature $v:|\sigma| \rightarrow \mathbb{R}$ in $S_{|\sigma|}^{F}$ is locally compatible with $\mathcal{U}$ if for every admissible $\tau \subset \mathcal{U}$ with $|\tau| \supset|\sigma|$, there is some feature $v^{+}:|\tau| \rightarrow \mathbb{R}$ in $S_{|\tau|}^{F}$ whose restriction to $|\sigma|$ coincides with $v$. In other words, a locally compatible feature is one which continues to be selected as we pass to larger admissible subsets. Conversely, consider a collection of features $\left\{v_{\sigma}\right\}$, one for each admissible $\sigma$. Such a collection is globally compatible with $\mathcal{U}$ if for each pair $|\sigma| \subset|\tau|$ of admissible subsets, the orthogonal projection $\pi_{\tau}^{F}: V(F) \rightarrow S_{|\tau|}^{F}$ sends $v_{\sigma}$ to $v_{\tau}$. Thus, every globally compatible feature is generated by functions $\left\{v_{U}: U \rightarrow \mathbb{R} \mid U \in \mathcal{U}\right\}$ such that the orthogonality relation

$$
\left(v_{U}-v_{U^{\prime}}\right) \perp S_{U \cap U^{\prime}}^{F}
$$

holds in $V(F)$ for every $U, U^{\prime} \in \mathcal{U}$.
The first question addressed in our work here is:
Fix a feature selector $S$ and a cover $\mathcal{U}$ of $X$. Given an input $F$ family of func-
tions }X \rightarrow \mathbb{R}\mathrm{ , to what extent can we efficiently discover all of the locally and
globally compatible features output by }S\mathrm{ ?}
Fix a feature selector $S$ and a cover $\mathcal{U}$ of $X$. Given an input $F$ family of functions $X \rightarrow \mathbb{R}$, to what extent can we efficiently discover all of the locally and globally compatible features output by $S$ ?

We approach this problem by recasting it in the language of quiver representations. The underlying quiver $Q_{\mathcal{U}}$ is a directed graph whose vertices are admissible sets, with a single edge $\sigma \rightarrow \tau$ whenever $|\sigma| \subset|\tau|$. The output of $S$ with input $F$ induces a representation $A_{\bullet}=A_{\bullet}^{S, F}$ of $Q$ valued in the category of finite dimensional Hilbert spaces. Explicitly, each vertex $\sigma$ is assigned the Hilbert space $A_{\sigma}:=S_{|\sigma|}^{F}$, while each edge $\sigma \rightarrow \tau$ is assigned the linear map $A_{\sigma \rightarrow \tau}: A_{\sigma} \rightarrow A_{\tau}$ obtained by restricting $\pi_{\tau}^{F}$ to $S_{|\sigma|}^{F}$. We show that the sections of this representation (as introduced in [30] and generalised to the multilinear setting in [24]), recover all the globally compatible features. Similarly, sections of this representation over certain augmented sub-quivers yield all the locally compatible features of $S$.

The presence of noise severely impairs the compatibility framework described above. The main difficulty is that one never obtains an exact equality between (projections of) features selected over an admissible set $|\tau|$ and features selected over an admissible subset $|\sigma|$. The best-case scenario is that features in $A_{\sigma}$ lie near ${ }^{1}$ the restriction of some feature in $A_{\tau}$. In fact, exact equality may not even be desirable - often, features are highly correlated, and collapsing together such features will further reduce the dimension of the space of selected features. Thus, there are many compelling reasons to seek a less rigid compatibility framework built around approximate sections of quiver representations.

With this consideration in mind, the second question addressed in this paper is:
To what extent can we define and efficiently compute the approximate sections of a quiver representation?

We address this challenge by introducing a new Laplacian operator.
The quiver Laplacian $\mathcal{L}$ introduced here is a (Hermitian, positive semidefinite) endomorphism of the total space $\operatorname{Tot}\left(A_{\bullet}\right):=\prod_{\sigma} A_{\sigma}$. In the special case where every $A_{\sigma}$ is

[^0]
[^0]:    ${ }^{1}$ Here proximity is determined by the inner product metric on $V(F)$.




---

one-dimensional and all orthogonal projection maps are identities, $L$ coincides with the ordinary graph Laplacian of $\mathcal{Q}_{U}$. We note that Laplacians have been defined for several discrete algebraic/combinatorial objects: from the original case of graphs [3], to simplicial complexes [12, 17], hypergraphs [2] and principal bundles on graphs [10]. Most closely related to our quiver Laplacian are the analogous operators defined for cellular sheaves in [16] (but see also $[11,25]$ ). The space of sections of a quiver representation coincides precisely with the kernel of the affiliated quiver Laplacian. Armed with the quiver Laplacian, we are able to define, for every $\epsilon>0$, the $\epsilon$-approximate sections of a quiver representation as those normalised vectors $x \in \operatorname{Tot}\left(\mathcal{A}_{\mathcal{S}, \mathcal{F}}\right)$ which satisfy $\langle x, L x\rangle \leq \epsilon$. Thus, the spans of eigenvectors of $L$ associated to small nonzero eigenvalues of $L$ delineate special families of approximate sections. Motivated by these considerations, we establish a host of fundamental properties for quiver Laplacians and their spectra.

Finally, we use the spectrum of an appropriate quiver Laplacian to study feature selection (as given by a peak-calling algorithm) for chromatin accessibility ${ }^{2}$ data from [28]. Our dataset comes from single-cell sequencing. This type of data has several properties which make the Laplacian-driven approach particularly appropriate:
(1) The dimensionality is massive - a naïve estimate assumes that every genomic position might be accessible, giving around 3 billion features. Therefore, feature selection (via peak-calling) becomes a crucial intermediate step towards making the analysis tractable.
(2) Different cell types have different relevant features, and it is important to make the feature selection process compatible with the types of cells under consideration. This makes it necessary to consider peaks not only for the entire dataset, but also for certain distinguished subsets.
(3) In many relevant cases where the data arise from diseases such as cancer or from the immune system (e.g. T cells), the cells might exhibit plasticity and their type is therefore not well-defined. In such cases, our distinguished subsets might overlap and should be modelled by a cover rather than a partition.
(4) There is some stochasticity in the output of peak-calling algorithms - in particular, the accessible genomic positions are only known approximately. Thus, the accessibility status of nearby positions is not independent; we capture this phenomenon via the inner product structure on feature space.

Summary of Results. Let $\mathcal{Q}$ be a finite quiver with vertex set $\mathcal{Q}_{0}$, edge set $\mathcal{Q}_{1}$ and maps $s, t: \mathcal{Q}_{1} \rightarrow \mathcal{Q}_{0}$ which specify the source and target vertices of each edge. We consider representations of $\mathcal{Q}$ - each such representation $\mathcal{A}_{\bullet}$ assigns a finite-dimensional (real or complex) Hilbert space $\mathcal{A}_{v}$ to every vertex $v \in \mathcal{Q}_{0}$ and a linear map $\mathcal{A}_{e}: \mathcal{A}_{s(e)} \rightarrow$ $\mathcal{A}_{t(e)}$ to every edge $e \in \mathcal{Q}_{1}$. We write $L_{\mathcal{A}}$ for the Laplacian of $\mathcal{A}$. (see Definition 4.2 below

[^0]
[^0]:    ${ }^{2}$ Chromatin accessibility measures the extent to which regions within the genome (among a specific family of cells) are reachable by cellular machinery, such as transcription factors.




---

for details), and arrange its eigenvalues as

$$
0 \leq \lambda_{1}(A) \leq \lambda_{2}(A) \leq \cdots \leq \lambda_{n}(A)
$$

where $n:=\operatorname{dim} \operatorname{Tot}(A) \bullet$ is the total dimension of $A \bullet$.
Here is a simplified version of our first main result, which provides upper bounds on Laplacian eigenvalues of a representation $A^{\prime} \cdot$ in terms of eigenvalues of $A$. whenever there exists a family of vertex-indexed linear maps $A_{v} \rightarrow A_{v}^{\prime}$.

THEOREM (I). Let $A_{\bullet}$ and $A_{\bullet}^{\prime}$ be two representations of $Q$, and consider any vertex-indexed collection $\tau=\left\{\tau_{v}: A_{v} \rightarrow A_{v}^{\prime} \mid v \in Q_{0}\right\}$ of linear maps. Write $q$ for the dimension of ker $\tau$ viewed as a (block diagonal) map $\operatorname{Tot}(A) \bullet \rightarrow \operatorname{Tot}\left(A_{\bullet}^{\prime}\right)$. There exist positive constants $\alpha, \beta, \gamma-$ each dependent on $\tau-$ such that the inequality

$$
\lambda_{k}\left(A^{\prime}\right) \leq \alpha \cdot \lambda_{k+q}(A)+\beta \cdot \frac{q}{\lambda_{k+q}(A)}+\gamma
$$

holds for every $k$ in $\{1,2, \ldots, n-q\}$.
The full statement of this result, along with explicit formulas for $\alpha, \beta$ and $\gamma$, is recorded in Theorem 5.2. If $\tau$ is a morphism of quiver representations $A \bullet \rightarrow A_{\bullet}^{\prime}$, then both $\beta$ and $\gamma$ vanish and we are left with a much simpler bound $\lambda_{k}\left(A^{\prime}\right) \leq \alpha \cdot \lambda_{k+q}(A)$.

Our next main result takes the form of a spectral stability result for feature selectors. The main challenge here is that the total spaces of two representations $A^{S, \mathcal{F}} \cdot$ and $A^{T, \mathcal{F}}$. may have different dimensions, so even the number of eigenvalues of the corresponding Laplacians could be different. Nevertheless, let $\mu_{S}$ and $\mu_{T}$ be the probability measures on $\mathbb{R}$ given by taking the average of Dirac measures concentrated at the eigenvalues $\left\{\lambda_{i}\left(A^{S, \mathcal{F}}\right)\right\}$ and $\left\{\lambda_{j}\left(A^{T, \mathcal{F}}\right)\right\}$, respectively. We obtain, in Corollary 5.5, the following bound on the 1-Wasserstein distance $\mathcal{W}_{1}\left(\mu_{S}, \mu_{T}\right)$ between these two measures.

THEOREM (II). Let $S$ and $T$ be two feature selectors defined on a finite set $X$ which is equipped with a cover $\mathcal{U}$. Fix a finite collection $\mathcal{F}$ of functions $X \rightarrow \mathbb{K}$. For each admissible set $\sigma$, define

$$
c_{\sigma}:=\left|\frac{\operatorname{dim} S^{\mathcal{F}}}{|\sigma|}-\frac{\operatorname{dim} T^{\mathcal{F}}}{|\sigma|}\right| \quad \text { and } \quad \epsilon_{\sigma}:=\operatorname{dist}_{\mathrm{Gr}}\left(\frac{S^{\mathcal{F}}}{|\sigma|}, \frac{T^{\mathcal{F}}}{|\sigma|}\right)
$$

where the latter expression invokes the Grassmannian distance between subspaces of $\mathrm{V}(\mathcal{F})$. Define $c:=\sum_{\sigma} c_{\sigma}$ and $\epsilon:=\max _{\sigma} \epsilon_{\sigma}$. There exist trigonometric polynomials $f$ and $g$ such that

$$
\mathcal{W}_{1}\left(\mu_{S}, \mu_{T}\right) \leq \frac{\left|Q_{1}^{\cup}\right|}{m}[f(\epsilon) \cdot c+g(\epsilon) \cdot(m-c)]
$$

where $\left|Q_{1}^{u}\right|$ is the number of edges in $Q^{u}$ and $m=\max \left\{\operatorname{dim} \operatorname{Tot}\left(A^{S, \mathcal{F}}\right), \operatorname{dim} \operatorname{Tot}\left(A^{T, \mathcal{F}}\right)\right\}$
We note that $c=0$ if and only if the two feature selectors assign equidimensional spaces to each admissible set. Explicit formulas for $f$ and $g$ are provided in Section 5. Crucially, we have $g(0)=0$; in the equidimensional case, the first term in our bound vanishes and the second term approaches 0 as $\epsilon \rightarrow 0$.




---

Our next main result provides several flavours of eigenvalue interlacing inequalities for quiver Laplacians which hold when quivers (and the overlaid representations) are modified in certain natural ways.

THEOREM (III). Let $A_{\bullet}$ be a representation of $Q$. The following inequalities hold for appropriate integers $i$. The constants $k, r, w_{1}, w_{2}$ which appear below depend on $A_{\bullet}$ as well as the modification performed to create a new representation $A_{\bullet}^{\prime}$ of a new quiver $Q^{\prime}$.
(1) If $Q^{\prime}$ is obtained by removing edges from $Q$ and $A_{\bullet}^{\prime}$ is the restriction of $A_{\bullet}$ to $Q^{\prime}$, then

$$
\lambda_{k+i}\left(A_{\bullet}\right) \leq \lambda_{k+i}\left(A_{\bullet}^{\prime}\right) \leq \lambda_{k+r+i}\left(A_{\bullet}\right)
$$

(2) If $Q^{\prime}$ is obtained by removing vertices (and incident edges) from $Q$ and $A_{\bullet}^{\prime}$ is the restriction of $A_{\bullet}$ to $Q^{\prime}$ then

$$
\lambda_{i}\left(A_{\bullet}\right)-w_{1} \leq \lambda_{i}\left(A_{\bullet}^{\prime}\right) \leq \lambda_{k+i}\left(A_{\bullet}\right)-w_{2}
$$

(3) If $Q^{\prime}$ and $A_{\bullet}^{\prime}$ are the result of performing an admissible homotopy of $Q$, then

$$
\phi^{-2} \lambda_{i}\left(A_{\bullet}\right) \leq \lambda_{i}\left(A_{\bullet}^{\prime}\right) \leq \phi^{2} \lambda_{i}\left(A_{\bullet}\right)
$$

where $\phi$ is the golden ratio.
(4) If $Q^{\prime}$ and $A_{\bullet}^{\prime}$ are the result of performing an admissible Kron reduction of $A_{\bullet}$, then
$\lambda_{i}\left(A_{\bullet}\right) \leq \lambda_{i}\left(A_{\bullet}^{\prime}\right) \leq \lambda_{i+r}\left(A_{\bullet}\right)$
Detailed versions of these results, including explicit formulas for various constants as well as precise definitions of admissible homotopy and Kron reduction, are located in Section 6. In order to state and prove these results in an appropriately general setting, we define sheaves on quivers - these are almost identical to cellular sheaves $[6,5,16]$ on graphs, except that our graphs are allowed to have self-loops.

As mentioned above, much of our work here has been motivated by the desire to better understand and improve peak-calling algorithms on datasets $X$ which come naturally equipped with a decomposition $\mathcal{U}$ into subsets. For this purpose, it is convenient to combine the quiver representations whose sections give locally and globally compatible features of a given feature selector $\mathcal{S}$ into a single representation of a larger quiver. This combined representation, denoted $N_{\bullet}^{S, \mathcal{F}}$, is described in Section 3.1. By design, its sections correspond to features which are both locally and globally compatible with $\mathcal{U}$ along $\mathcal{F}$, and we naturally seek its approximate sections. Unfortunately, extracting spectral data for its Laplacian presents a serious computational challenge — both the underlying quiver and the total dimension are typically much larger than $Q^{\mathcal{U}}$ and $A_{\bullet}^{S, \mathcal{F}}$. The third main result of this paper is a remedy which takes the form of a reduction theorem.

THEOREM (IV). Let $\mathcal{S}$ be a feature selector on a set $X$ equipped with a cover $\mathcal{U}$ such that $Q^{\mathcal{U}}$ is weakly connected. Let $N_{\bullet}^{S, \mathcal{F}}$ be the combined representation associated to a finite collection $\mathcal{F}$ of functions $X \rightarrow \mathbb{K}$. Fix a vertex $\sigma \in Q_{0}^{\mathcal{U}}$. There exists a new quiver $Q^{\prime}$ with a single vertex and $\left|Q_{0}^{\mathcal{U}}\right|$ edges along with a representation $A_{\bullet}^{\prime}$ of $Q^{\prime}$ satisfying two properties:




---

(1) For each vertex $\tau$ of $\mathcal{Q}_{\mathcal{U}}$, let $\mathrm{id}_{\tau}$ be the identity map on $\mathbb{S}_{|\tau|}^{F}$ and let $\iota_{\tau}^{F}: \mathbb{S}_{|\tau|}^{F} \hookrightarrow \mathbb{V}(F)$ denote the inclusion map (which is adjoint to $\pi_{\tau}^{F}$ ). Then, the Laplacian of $A_{\bullet}^{\prime}$ is

$$
L_{A^{\prime}}=\sum_{\tau \in \mathcal{Q}_{\mathcal{U}}}^{0}\left[\operatorname{id}_{\sigma}-\pi_{\sigma}^{F} \iota_{\tau}^{F} \pi_{\tau}^{F} \iota_{\sigma}^{F}\right]
$$

(2) Let n be the total dimension of $\mathbb{N}_{\bullet}^{\mathrm{S}, F}$. There exist positive constants $C_{1}$ and $C_{2}$, which depend only on $\mathbb{A}_{\bullet}^{\mathcal{S}, F}$, such that the inequalities

$$
C_{1} \cdot \lambda_{i}\left(\mathbb{N}_{\bullet}^{\mathcal{S}, F}\right) \leq \lambda_{i}\left(A_{\bullet}^{\prime}\right) \leq C_{2} \cdot \lambda_{i+k}\left(\mathbb{N}_{\bullet}^{\mathcal{S}, F}\right)
$$

hold for every i in $\{1,2, \ldots, n\}$, with $k:=n-\operatorname{dim} \mathbb{S}_{|\sigma|}^{F}$.
The full statement of this result is recorded in Theorem 7.1.
Finally, we examined a single-cell chromatin accessibility (ATAC-seq) dataset from [28]; here $X$ is a dataset consisting of around $3 \times 10^{4}$ tumour-infiltrating T cells, while the input $F$ consists of 20,000 binary-valued features $X \rightarrow \mathbb{R}$. To build a cover $\mathcal{U}$ of $X$, we used a standard notion of genomic proximity between cells, constructed a 15-nearest neighbour graph, and expanded the communities of that graph by one hop. This produces a quiver $\mathcal{Q}_{\mathcal{U}}$ with 87 vertices. We then ran the MACS2 peak-calling algorithm [39] to find the 1,000 most accessible regions for each admissible set and built a quiver Laplacian for a variant of the combined representation of $\delta$ (as described in Theorem 7.2).
Observation (V). The first 3,000 eigenvectors of the quiver Laplacian described above had the following properties:
(1) The majority of eigenvectors displayed a tight grouping of genomic positions (around 150 consecutive base-pairs out of approximately 3 billion) across the vertices.
(2) Most eigenvectors were supported in most of the vector spaces assigned to vertices of the quiver. In particular, one such eigenvector that was supported on every vertex, lay near the gene FAM72D, which is involved in the cell cycle and hence active for every type of T cell.
(3) Conversely, the support of a handful of eigenvectors was localised to a very small subset of vertices. One such eigenvector lay near the gene STAT3, which regulates Th1, Th17 and Treg cells; this eigenvector was supported on just 3 vertices, each of which corresponds to admissible subpopulations particularly rich in these three types of T cells.
Thus, eigenvectors of the quiver Laplacian were able to isolate relevant and consistent meta-features across different scales within the given dataset.

Outline. The paper is structured as follows: $\S 2$ describes how a feature selector together with a cover of the data yields a quiver representation. In $\S 3$ we describe both local and global compatibility of features with respect to the cover. We also describe how these features can be computed simultaneously as sections of a larger quiver representation. $\S 4$ introduces the quiver Laplacian and how its eigenvectors may be used to approximate the space of sections. $\S 5$ studies how a transformation of quiver representations relates




---

the spectra of the respective representations and bounds their spectral distance. This then gives a stability of the spectrum of the representation associated to a feature selector. $\S 6$ bounds the changes in the spectrum of a quiver Laplacian when the underlying quiver undergoes various operations. $\S 7$ then uses these operations to simplify the computation of approximate sections of a feature selector. Finally, in $\S 8$ we use quiver Laplacians to extract (approximately) compatible peaks in single-cell chromatin accessibility data.

# ACKNOWLEDGEMENTS 

OS is supported by Ludwig Cancer Research. VN and HAH are grateful for the support provided by the UK Centre for Topological Data Analysis EPSRC grant EP/R018472/1. HAH gratefully acknowledges funding from the Royal Society. VN is partially supported by US AFOSR grant FA9550-22-1-0462. OS would like to thank Renee Hoekzema, Ka Man (Ambrose) Yim, Phil Xie, and Xin Lu for many helpful conversations. For the purpose of Open Access, the authors have applied a CC BY public copyright licence to any Author Accepted Manuscript (AAM) version arising from this submission.

## 2. From FEATURE SELECTION to Quiver Representations

Given a finite set $X$ and a field $\mathbb{K}$, let $X^{*}$ be the $\mathbb{K}$-vector space which consists of all functions $X \rightarrow \mathbb{K}$. Denote by $\operatorname{Sub}\left(X^{*}\right)$ the collection of all subsets of $X^{*}$ (not necessarily subspaces), and for each such subset $\mathcal{F}$ write $V(\mathcal{F})$ to indicate the subspace of $X^{*}$ given by the $\mathbb{K}$-linear span of $\mathcal{F}$. Let $\operatorname{Gr}_{k}\left(X^{*}\right)$ be the Grassmannian of $k$-dimensional subspaces of $X^{*}$ for each $k \geq 0$, and consider the disjoint union

$$
\operatorname{Gr}_{\infty}\left(X^{*}\right):=\bigsqcup_{k \geq 0} \operatorname{Gr}_{k}\left(X^{*}\right)
$$

Here is the main object of study in this work.
DEfinition 2.1. A feature selector on $X$ is any map $\mathcal{S}: \operatorname{Sub}\left(X^{*}\right) \rightarrow \operatorname{Gr}_{\infty}\left(X^{*}\right)$, such that for each input $\mathcal{F} \subset X^{*}$, the corresponding output $\mathcal{S}_{X}^{\mathcal{F}}$ is a subspace of $V(\mathcal{F})$.

We now fix a feature selector $\mathcal{S}$ on $X$; readers may wish to keep the following concrete example in mind throughout the remainder of $\S 2$.

EXAMPLE 2.2. Among the most well-known and ubiquitous feature selectors is principal components analysis [19] - here,

- $X$ is a finite origin-centered subset of some real Euclidean space $\mathbb{R}^{n}$,
- $\mathbb{K}$ is the field $\mathbb{R}$ of real numbers, and
- $\mathcal{F}$ is the set $\{x \mapsto\langle x, p\rangle\}$ of maps given by taking inner products with the unit vectors $p$.

For a fixed $k \ll n$, the output $\mathcal{S}_{X}^{\mathcal{F}}$ is the vector space spanned by the $k$ inner product functions (or equivalently, the $k$ unit vectors) along which the variance in $X$ is maximised.




---

Our goal here is to find a principled framework for relating the vector subspaces $S_{Y}^{F}$ to each other for a fixed $F$ as $Y$ ranges over subsets of $X$. Already for principal components analysis, it is clear that there need not be any coherent relationship between $S_{X}^{F}$ and $S_{Y}^{F}$ for arbitrary $Y \subset X$-for instance, neither one is guaranteed to be a subspace of the other within $V(F)$. It therefore becomes necessary to constrain the family of subsets under consideration. Here we will describe how to relate the subspaces $S_{Y}^{F}$ for $Y$ ranging over the lattice of subsets generated from a chosen cover $\mathcal{U}$ of $X$. We recall that any such $\mathcal{U}$ is a finite collection of nonempty subsets satisfying $X=\bigcup_{U \in \mathcal{U}} U$.

DEFinition 2.3. The quiver associated to a cover $\mathcal{U}$ of $X$ is the directed graph $Q_{\mathcal{U}}$ whose
(1) vertices are subsets $\sigma \subset \mathcal{U}$ whose support $|\sigma|:=\bigcap_{U \in \sigma} U$ is nonempty; and,
(2) there is a unique directed edge $\sigma \rightarrow \tau$ whenever $\sigma$ properly contains $\tau$ (and hence $|\sigma| \subset|\tau|)$

We now re-assemble the algebraic data of $S$ to produce a representation of $Q_{\mathcal{U}}$, i.e., an assignment of vector spaces to vertices and linear maps to edges [29]. Implicit in the construction below is the choice of an inner product structure on $X^{*}$, which allows us to define adjoints of linear maps, and hence, orthogonal projections onto subspaces. For each vertex $\sigma$ of $Q_{\mathcal{U}}$, let $\iota_{\sigma}^{F}: S_{|\sigma|}^{F} \hookrightarrow V(F)$ denote the inclusion map and let $\pi_{\sigma}^{F}$ : $V(F) \rightarrow S_{|\sigma|}^{F}$ denote its adjoint, i.e., the orthogonal projection in $X^{*}$ with respect to our chosen inner product.

DEfinition 2.4. For each subset $F \subset X^{*}$, the $S$-representation of $Q_{\mathcal{U}}$ along $F$ consists of the following assignments $A_{\bullet}=A_{\bullet}^{S, F}$ :
(1) every vertex $\sigma$ of $Q_{\mathcal{U}}$ is assigned the vector space $A_{\sigma}:=S_{|\sigma|}^{F}$, which is a subspace of $V(F \mid|\sigma|)$ and hence ${ }^{3}$ of $V(F)$; moreover,
(2) every edge $\sigma \rightarrow \tau$ of $Q_{\mathcal{U}}$ is assigned the $\mathbb{K}$-linear map $A_{\sigma \rightarrow \tau}: A_{\sigma} \rightarrow A_{\tau}$ given by $\pi_{\tau}^{F} \circ \iota_{\sigma}^{F}$.

It may be worth noting that the vertices of $Q_{\mathcal{U}}$ are simplices in the nerve of the cover $\mathcal{U}$ [8], and every edge $\sigma \rightarrow \tau$ in $Q_{\mathcal{U}}$ corresponds to a face relation (where the simplex $\tau$ lies in the boundary of the simplex $\sigma$ ). In particular, it follows from the definition of $Q_{\mathcal{U}}$ above that the existence of adjacent edges $\sigma \rightarrow \tau \rightarrow \gamma$ forces the existence of the edge $\sigma \rightarrow \gamma$. We call $A_{\bullet}$ a sheaf on the nerve of $\mathcal{U}$ if it satisfies the following associativity criterion: for every such pair of adjacent edges, the map $A_{\sigma \rightarrow \gamma}$ must equal the composite $A_{\tau \rightarrow \gamma} \circ A_{\sigma \rightarrow \tau}$. In general, we do not expect this associative property to hold when $A_{\bullet}$ arises from a feature selector. The next section contains our attempt to rectify this shortcoming.

[^0]
[^0]:    ${ }^{3}$ Here we adopt the convention that any function $f:|\sigma| \rightarrow \mathbb{K}$ extends to all of $X$ by setting $f=0$ on $X \backslash|\sigma|$. Conversely, any function $X \rightarrow \mathbb{K}$ automatically restricts to a function on $|\sigma|$.




---

# 3. COMPATIBILITY AND SECTIONS 

Here we use the $S$-representation to define and study two notions of compatibility for a feature selector $S$ on $X$ against a cover $\mathcal{U}$ when invoked with input $F \subset X^{*}$ :
(1) Fix a vertex $\sigma \in Q_{0}^{\mathcal{U}}$. An element $v_{\sigma} \in A_{\sigma}^{S, F}$ is locally compatible with $\mathcal{U}$ if

$$
\iota_{\sigma}^{F}\left(v_{\sigma}\right)=\iota_{\tau}^{F} \circ A_{\sigma \rightarrow \tau}\left(v_{\sigma}\right)
$$

holds for every edge $\sigma \rightarrow \tau$ in $Q_{1}$.
(2) A collection

$$
\left\{v_{\sigma} \in A_{\sigma} \mid \sigma \in Q_{0}^{\mathcal{U}}\right\}
$$

is globally compatible with $\mathcal{U}$ if the equality

$$
A_{\sigma \rightarrow \tau}\left(v_{\sigma}\right)=v_{\tau}
$$

holds for every edge $\sigma \rightarrow \tau$ in $Q^{\mathcal{U}}$.
This notion of local compatibility checks whether or not (the orthogonal projections of) a given feature $v_{\sigma}$ which has been selected by $S$ over $|\sigma|$ continue to be selected over all greater subsets $|\tau| \supset|\sigma|$ generated by the cover $\mathcal{U}$. In this sense, local compatibility tests the robustness of selected features as we decrease the depth of the cover. Already for principal component analysis, it is clear that not every feature will be locally compatible, i.e., in general $A_{\sigma \rightarrow \tau}$ has a non-trivial kernel. Global compatibility, on the other hand, tests features horizontally across the quiver - to be globally compatible, the vectors of a family $\left\{v_{\sigma}\right\}$ must map coherently onto each other under the linear maps of $A_{\bullet}$ as we traverse zigzag paths in $Q^{\mathcal{U}}$ of the form

$$
\sigma_{1} \rightarrow \tau_{1} \leftarrow \sigma_{2} \rightarrow \tau_{2} \leftarrow \cdots \leftarrow \sigma_{k} \rightarrow \tau_{k}
$$



FIGURE 2. Example of different compatibility conditions.

We defer the study of local compatibility for now, and will focus on global compatibility.
3.1. Global Compatibility and Sections. Let $Q=\left(s, t: Q_{1} \rightarrow Q_{0}\right)$ be a finite quiver and let $A_{\bullet}$ be a representation of $Q$ valued in the category $\operatorname{FdHilb}(\mathbb{K})$ of finite-dimensional Hilbert spaces over the field $\mathbb{K} \in\{\mathbb{R}, \mathbb{C}\}$. The total space of $A_{\bullet}$ is defined as the product

$$
\operatorname{Tot}\left(A_{\bullet}\right):=\prod_{i \in Q_{0}} A_{i}
$$




---

Since $Q$ is finite, $\operatorname{Tot}\left(A_{\bullet}\right)$ inherits a finite-dimensional Hilbert space structure from its $A_{i}$ factors. Motivated by the global compatibility criterion from Definition 3.2, we highlight a relevant subspace of the total space below.

DEfinition 3.1. A tuple $\gamma:=\left(\gamma_{i} \in A_{i} \mid i \in Q_{0}\right)$ in $\operatorname{Tot}\left(A_{\bullet}\right)$ is called a section of $A_{\bullet}$ if for every edge $e$ in $Q_{1}$ we have $A_{e}\left(\gamma_{s(e)}\right)=\gamma_{t(e)}$.

Sections of quiver representations were introduced in [30] along with an effective algorithm for their computation - see [30, Sec 5.2]. Sections are closely related to the compatibility criteria from Definition 3.2. In particular, if $\mathcal{S}$ is a feature selector on a set $X$, then the sections of $A_{\bullet}^{\mathcal{S}, F}$ are exactly globally compatible features of $\mathcal{S}$ against the cover $\mathcal{U}$. Sections can also be used to compute locally compatible features, as we will now describe.

# 3.2. Local Compatibility. 

DEfinition 3.2. A feature selector $\mathcal{S}$ on $X$ is locally compatible with $\mathcal{U}$ on $F \subset X^{*}$ if the following triangle of vector spaces commutes for each edge $\sigma \rightarrow \tau$ of $Q_{\mathcal{U}}$ :



Equivalently, the identity $\iota_{\sigma}^{F}=\iota_{\tau}^{F} \circ \pi_{\tau}^{F} \circ \iota_{\sigma}^{F}$ holds for every edge $\sigma \rightarrow \tau$ of $Q_{\mathcal{U}}$.
It will be useful to rephrase this compatibility condition entirely within the realm of quiver representations by blowing up the above triangle to a square. To this end, we introduce another representation $C_{\bullet}=C_{\bullet}^{F}$ of $Q_{\mathcal{U}}$ which may be associated to every $F \subset$ $X^{*}$ (and which does not depend on $\mathcal{S}$ ). This constant representation assigns $C_{\sigma}:=V(F)$ to every vertex $\sigma$ and the identity map to each edge $\sigma \rightarrow \tau$. For each vertex $\sigma$, there is an evident inclusion map

$$
\iota_{\sigma}^{F}: A_{\sigma}^{\mathcal{S}, F} \hookrightarrow C_{\sigma}^{F}
$$

since the codomain is $V(F)$ and the domain is its subspace $\left.\mathcal{S}_{F}\right|_{|\sigma|}$. Now, for every edge $\sigma \rightarrow \tau$ we have a diagram of four linear maps:



The vertical maps $\iota^{F}$ prescribe a morphism of quiver representations from $A_{\bullet}^{\mathcal{S}, F}$ to $C_{\bullet}^{F}$ if and only if the above diagram commutes for every edge $\sigma \rightarrow \tau$ in $Q_{\mathcal{U}}$. By definition of $C_{\bullet}^{F}$, the bottom edge of this diagram is precisely $V(F) \xrightarrow{=} V(F)$, so this square is an




---

elementary modification of the triangle from Definition 3.2. Thus, we have arrived at the following straightforward result.

Proposition 3.3. The feature selector $\mathcal{S}$ is locally compatible with $\mathcal{U}$ on $F \subset X^{*}$ if and only if the collection of maps

$$
\left\{\iota_{\sigma}^{F}: A_{\sigma}^{S, F} \hookrightarrow C_{\sigma}^{F}\right\}
$$

indexed by vertices $\sigma$ of $\mathcal{Q}^{U}$ prescribe a morphism of quiver representations $A_{\bullet}^{S, F} \rightarrow C_{\bullet}^{F}$.
As described earlier, a morphism $\tau$ between quiver representations $A_{\bullet}$ and $A_{\bullet}^{\prime}$ is a collection

$$
\tau=\left\{\tau_{v}: A_{v} \rightarrow A_{v}^{\prime} \mid v \in Q_{0}\right\}
$$

of linear maps $\tau_{v}$ such that

$$
A_{e}^{\prime} \circ \tau_{s(e)}=\tau_{t(e)} \circ A_{t(e)}
$$

for each edge $e \in Q_{1}$. The commutivity condition in (3) can be too strong for quiver representations obtained from data, so we will define a transformation $\tau$ between quiver representations as a collection of linear maps

$$
\tau=\left\{\tau_{v}: A_{v} \rightarrow A_{v}^{\prime} \mid v \in Q_{0}\right\}
$$

without the commutivity condition.
Definition 3.4. Let $Q$ be a quiver. For each vertex $u \in Q_{0}$ define the floret of based at $u$ to be the following quiver $F^{Q, u}$ :
(1) the set of vertices is the disjoint union

$$
{F_{0}^{Q, u}=\{u\} \sqcup\left\{v_{e} \mid(e: u \rightarrow v) \in Q_{1}\right\} .}
$$

In other words, there is a distinguished copy of $u$, which we label $u_{0}$ henceforth, and an additional object denoted $v_{e}$ for every edge in $Q_{1}$ from $u$ to $v$.
(2) Define the set of edges of $F^{Q, u}$ as

$$
F_{1}^{Q, u}=\left\{e_{L D}, e_{D L}: u_{0} \rightarrow v_{e} \mid(e: u \rightarrow v) \in Q_{1}\right\}
$$

In other words, for each edge $e: u \rightarrow v$ in $Q$ there are two distinct edges $e_{L D}$ and $e_{D L}$ from $u_{0}$ to $v_{e}$ in $F^{Q, u}$.

Now suppose $A_{\bullet}$ and $A_{\bullet}^{\prime}$ are representations of the quiver $Q$ with a transformation $\tau$ : $A_{\bullet} \rightarrow A_{\bullet}^{\prime}$. Define the following representation $F_{\bullet}^{\tau, u}$ of $F^{Q, u}$ :

$$
\begin{aligned}
F_{u_{0}}^{\tau, u} & =A_{u} \\
F_{v_{e}}^{\tau, u} & =A_{v}^{\prime} \\
F_{e_{L D}}^{\tau, u} & =A_{e}^{\prime} \circ \tau_{u} \\
F_{e_{D L}}^{\tau, u} & =\tau_{t(e)} \circ A_{e}
\end{aligned}
$$

See Figure 3.4 for an illustration.
Constructing the floret now allows us to compute locally compatible features: in the case where the transformation is $\iota^{F}: A_{\bullet}^{S, F} \rightarrow C_{\bullet}^{F}$ as in Proposition 3.3, the sections $\Gamma\left(\mathcal{F}_{\bullet}^{\iota^{F} \sigma}\right)$ are exactly the locally compatible features at $\sigma$.




---



The quiver $Q$



The quiver $F_{Q, u}$



The representation $F_{\tau, u}$
FIGURE 3. An illustration of the floret based at $u$ and its representation.
3.3. Bicompatible features. In Section 4 below, we will consider the problem of discovering features which satisfy approximate versions of the local and global compatibility criteria. For this purpose, it will be helpful to construct a single quiver whose sections correspond to features which are both locally and globally compatible. The first step in this construction is a method for gluing quivers and their representations. Let $Q=\left(s, t: Q_{1} \rightarrow Q_{0}\right)$ and $Q^{\prime}=\left(s^{\prime}, t^{\prime}: Q_{1}^{\prime} \rightarrow Q_{0}^{\prime}\right)$ be two quivers.

DEFINITION 3.5. For each subset $R \subset Q_{0} \times Q_{0}^{\prime}$, let $Q \cup_{R} Q^{\prime}$ be the merged quiver whose
(1) vertex set is the quotient $V:=\left(Q_{0} \sqcup Q_{0}^{\prime}\right) / R$,
(2) edge set is the disjoint union $E:=Q_{1} \sqcup Q_{1}^{\prime}$,
and source/target maps are given as follows. Let $\rho$ be the composite $Q_{0} \hookrightarrow Q_{0} \sqcup Q_{0}^{\prime} \rightarrow V$, and define $\rho^{\prime}: Q_{0}^{\prime} \rightarrow V$ similarly. If $e \in E$ lies in $Q_{1}$, then its source and target vertices are $\rho \circ s(e)$ and $\rho \circ t(e)$; and if $e$ lies in $Q_{1}^{\prime}$, then its source and target vertices are $\rho^{\prime} \circ s^{\prime}(e)$ and $\rho^{\prime} \circ t^{\prime}(e)$ respectively.

Fix representations $A_{\bullet}$ of a quiver $Q$ and $A_{\bullet}^{\prime}$ of another quiver $Q^{\prime}$.
DEFINITION 3.6. Let $R \subset Q_{0} \times Q_{0}^{\prime}$ be any subset for which we have $A_{i}=A_{j}^{\prime}$ whenever $(i, j)$ lies in $R$. The merged representation of $A_{\bullet}$ and $A_{\bullet}^{\prime}$, denoted $\left(A \cup_{R} A^{\prime}\right)_{\bullet}$, is the following representation of $Q \cup_{R} Q^{\prime}$. To vertices, it assigns

$$
\left(A \cup_{R} A^{\prime}\right)_{i}:= \begin{cases}A_{i} & i \in Q_{0} \text { and }(i, j) \notin R \text { for any } j \in Q_{0}^{\prime} \\ A_{i}^{\prime} & i \in Q_{0}^{\prime} \text { and }(j, i) \notin R \text { for any } j \in Q_{0} \\ A_{i}=A_{j}^{\prime} & \text { if }(i, j) \in R \\ A_{j}=A_{i}^{\prime} & \text { if }(j, i) \in R\end{cases}
$$




---

And on edges, we have

$$
\left(A \cup_{R} A^{\prime}\right)_{e}:= \begin{cases}A_{e} & \text { if } e \in Q_{1} \\ A_{e}^{\prime} & \text { if } e \in Q_{1}^{\prime}\end{cases}
$$

One may embed both $\operatorname{Tot}\left(A_{\bullet}\right)$ and $\operatorname{Tot}\left(A_{\bullet}^{\prime}\right)$ within the total space of the merged representation in the natural way, and it is readily seen that the space of sections of $\left(A \cup_{R} A^{\prime}\right)_{\bullet}$ is (isomorphic to) the intersection $\Gamma\left(A_{\bullet}\right) \cap \Gamma\left(A_{\bullet}^{\prime}\right)$.



Figure 4. Illustration of the merged quiver

Returning to the case of interest, let $\mathcal{S}$ be a feature selector on a finite set $X$; consider a cover $\mathcal{U}$ of $X$ and a subset $\mathcal{F} \subset X^{*}$. Let $\widehat{Q}^{\mathcal{U}}$ be the quiver given by the disjoint union of florets $I^{\sigma}$ indexed by vertices $\sigma \in Q_{0}^{\mathcal{U}}$, and let $\widehat{A}_{\bullet}^{\mathcal{S}, \mathcal{F}}$ be the representation of $\widehat{Q}^{\mathcal{U}}$ given by the floret functors $B_{\sigma}$. We define $R \subset\left(Q^{\mathcal{U}}\right)_{0} \times \widehat{Q}_{0}^{\mathcal{U}}$ as the collection

$$
R:=\left\{\left(\sigma, \sigma_{0}\right) \mid \sigma \in Q_{0}^{\mathcal{U}}\right\}
$$

where $\sigma_{0}$ is the central vertex of $I^{\sigma}$.
DEFINITION 3.7. The combined $\mathcal{S}$-representation (of $Q^{\cup} \cup_{R} \widehat{Q}^{\mathcal{U}}$, along $\mathcal{F}$ ) is the merged representation $N_{\bullet}^{\mathcal{S}, \mathcal{F}}:=\left(A^{\mathcal{S}, \mathcal{F}} \cup_{R} \widehat{A}^{\mathcal{S}, \mathcal{F}}\right)_{\bullet}$.

By design, the sections of $N_{\bullet}^{\mathcal{S}, \mathcal{F}}$ correspond to relevant features which are both locally and globally compatible with $\mathcal{U}$. We call these sections the bicompatible features of $\mathcal{S}$.

EXAMPLE 3.8. Suppose $\mathcal{U}=\left\{U_{1}, U_{2}\right\}$ is a cover of $X$, such that $U_{1} \cap U_{2} \neq \emptyset$. Define $\tau_{1}=\left\{U_{1}\right\}, \tau_{2}=\left\{U_{2}\right\}$ and $\sigma=\left\{U_{1}, U_{2}\right\}$. The quiver $Q^{\mathcal{U}}$ is

$$
\tau_{1} \longleftarrow \sigma \longrightarrow \tau_{2}
$$

Consider a bicompatible feature, i.e., a section $\mathbf{x} \in \Gamma\left(N_{\bullet}^{\mathcal{S}, \mathcal{F}}\right)$. By definition, we have $\iota_{\tau_{2}}^{\mathcal{F}}\left(\mathbf{x}_{\tau_{2}}\right)=\iota_{\sigma}^{\mathcal{F}}\left(\mathbf{x}_{\sigma}\right)=\iota_{\tau_{1}}^{\mathcal{F}}\left(\mathbf{x}_{\tau_{1}}\right)$, hence



Thus, bicompatible features are the ones which are relevant for every $U \in \mathcal{U}$.




---

3.4. Dual Representations. If one is also interested in features which are relevant for some - but not all $-U \in \mathscr{U}$, then it becomes necessary to consider a different notion of bicompatibility. Given a quiver $Q=\left(s, t: Q_{1} \rightarrow Q_{0}\right)$, its dual $Q^{*}$ is the quiver with the same vertices and edges but with source and target maps interchanged, i.e., $s^{*}:=$ $t$ and $t^{*}:=s$. Every representation $A_{\bullet}$ of $Q$ valued in $\operatorname{FdHilb}(\mathbb{K})$ induces a unique dual representation $A_{\bullet}^{*}$ of $Q^{*}$, which is obtained by taking the adjoint of every edge map: namely, $\left(A^{*}\right)_{e}:=\left(A_{e}\right)^{*}$ for each $e \in Q_{1}$.
When $A_{\bullet}$ is the $S$-representation (from Definition 2.4) of a feature selector $S_{\bullet}$ along some input $F$, the fact that $\iota_{\sigma}^{F}$ and $\pi_{\sigma}^{F}$ form an adjoint pair for each vertex $\sigma \in Q_{0}^{\mathscr{Y}}$ implies that for every edge $\sigma \rightarrow \tau$ in $Q^{\mathscr{U}}$, we have

$$
\left(A^{S, F}\right)_{\tau \rightarrow \sigma}^{*}=\left(\pi_{\tau}^{F} \circ \iota_{\sigma}^{F}\right)^{*}=\pi_{\sigma}^{F} \circ \iota_{\tau}^{F}
$$

DEFINITION 3.9. The mixed $S$-representation (of $\left(Q^{\mathscr{U}}\right)^{*} \cup_{R} \widehat{Q}^{\mathscr{U}}$, along $F$ ) is the merged representation $M_{\bullet}^{S, F}:=\left(\left(A^{S, F}\right)^{*} \cup_{R} \widehat{A}^{S, F}\right)_{\bullet}$.

Let us revisit Example 3.8 with a view towards understanding the sections of $M_{\bullet}^{S, F}$. These sections are given by the direct sum

$$
\Gamma\left(M_{\bullet}^{S, F}\right) \cong\left(\iota_{\tau_{1}}\left(S_{\left|\tau_{1}\right|}^{F}\right) \cap \iota_{\sigma}\left(S_{|\sigma|}^{F}\right)^{\perp}\right) \oplus\left(\iota_{\tau_{2}}\left(S_{\left|\tau_{2}\right|}^{F}\right) \cap \iota_{\sigma}\left(S_{|\sigma|}^{F}\right)^{\perp}\right) \oplus \Gamma\left(N_{\bullet}^{S, F}\right)
$$

In this case, $\iota_{\tau_{1}}\left(S_{\left|\tau_{1}\right|}^{F}\right) \cap \iota_{\sigma}\left(S_{|\sigma|}^{F}\right)^{\perp}$ corresponds to features that are relevant to $U_{1}$ but not to $U_{1} \cap U_{2}$. Note that

$$
\left(\iota_{\tau_{1}}\left(S_{\left|\tau_{1}\right|}^{F}\right) \cap \iota_{\sigma}\left(S_{|\sigma|}^{F}\right)^{\perp}\right) \cap\left(\iota_{\tau_{2}}\left(S_{\left|\tau_{2}\right|}^{F}\right) \cap \iota_{\sigma}\left(S_{|\sigma|}^{F}\right)^{\perp}\right)
$$

might not be trivial, i.e. there could be a feature relevant to both $U_{1}$ and $U_{2}$ but not to $U_{1} \cap U_{2}$, and hence this feature corresponds to two independent sections.

# 4. The Quiver Laplacian and Approximate Sections 

So far, we have reframed compatibility-testing of feature selectors in terms of finding the sections of a quiver representation. However, the space of sections might be trivial [30, Sec 5.1]. Rather than seeking exact solutions, we endeavour to find approximate sections.
4.1. The Quiver Laplacian. Let $\operatorname{FdHilb}(\mathbb{K})$ denote the category of finite-dimensional Hilbert spaces over the field $\mathbb{K} \in\{\mathbb{R}, \mathbb{C}\}$; every morphism $A: U \rightarrow V$ in this category admits an adjoint morphism $A^{*}: V \rightarrow U$ characterised by $\langle A u, v\rangle=\left\langle u, A^{*} v\right\rangle$ for all $(u, v)$ in $U \times V$. Here we fix a finite quiver $Q=\left(s, t: Q_{1} \rightarrow Q_{0}\right)$ and consider a representation $A_{\bullet}$ of $Q$ valued in $\operatorname{FdHilb}(\mathbb{K})$. We recall the total space from (1) and define target space of $A_{\bullet}$ as the direct product

$$
\operatorname{Tar}\left(A_{\bullet}\right):=\prod_{e \in Q_{1}} A_{t(e)}
$$

Since we have assumed that $Q$ is finite, both these spaces inherit a Hilbert space structure from the individual factors of the form $A_{v}$. We will denote the identity map on $A_{v}$ by $\mathrm{id}_{v}$ rather than $\operatorname{id}_{A_{v}}$.




---

DEFINITION 4.1. Given an $\mathrm{FdHilb}(\mathbb{K})$-valued quiver representation $A$. of $Q$, its boundary operator

$$
B_{A}: \operatorname{Tot}(A) \longrightarrow \operatorname{Tar}(A)
$$

is the linear map given in component form by

$$
\left(B_{A}\right)_{e, v}= \begin{cases}A_{e}-i d_{v} & \text { if } s(e)=t(e)=v \\ A_{e} & \text { if } s(e)=v \text { and } t(e) \neq v \\ -i d_{v} & \text { if } s(e) \neq v \text { and } t(e)=v \\ 0 & \text { otherwise }\end{cases}
$$

If the quiver $Q$ is finite, then it follows from a simple calculation that ker $B_{A}$ is isomorphic (as a Hilbert space) to the space $\Gamma\left(Q ; A_{\bullet}\right)$ of $A_{\text {. }}$ 's sections. From the boundary operator of a quiver representation, we can construct another associated operator, the Laplacian, which will allow us to compute approximate sections.

DEFINITION 4.2. The Laplacian of $A$.$\cdot is the endomorphism \mathcal{L}_{A}: \operatorname{Tot}(A) \rightarrow \operatorname{Tot}(A)$ given by

$$
\mathcal{L}_{A}=B_{A}^{*} B_{A}
$$

In component form, we have

$$
\left(\mathcal{L}_{A}\right)_{v, v}=\sum_{\substack{e \in Q_{1} \\ s(e)=v}} A_{e}^{*} A_{e}+\sum_{\substack{e \in Q_{1} \\ t(e)=v}} i d_{v}-\sum_{\substack{e \in Q_{1} \\ s(e)=t(e)=v}}\left[A_{e}^{*}+A_{e}\right]
$$

and for $u \neq v$

$$
\left(\mathcal{L}_{A}\right)_{u, v}=-\sum_{\substack{e \in Q_{1} \\ s(e)=u \\ t(e)=v}} A_{e}^{*}-\sum_{\substack{e \in Q_{1} \\ s(e)=v \\ t(e)=u}} A_{e}
$$

Since $\operatorname{ker} \mathcal{L}_{A}=\operatorname{ker} B_{A}$, the kernel of $\mathcal{L}_{A}$ also computes the sections of $A_{\text {. }}$. The main advantage of considering $\mathcal{L}_{A}$ rather than $B_{A}$ in this context is that it is a Hermitian and positive semi-definite matrix. As such, it enjoys favourable spectral properties; in particular, all of its eigenvalues are all real and non-negative. We shall order these eigenvalues in increasing fashion, with multiplicity:

$$
\lambda_{1}\left(\mathcal{L}_{A}\right) \leq \cdots \leq \lambda_{n}\left(\mathcal{L}_{A}\right)
$$

where $n:=\operatorname{dim} \operatorname{Tot}(A \cdot)$. If $\varphi: A_{\bullet}^{1} \rightarrow A_{\bullet}^{2}$ is an isomorphism of quiver representations with each $\varphi_{v}$ a unitary map then

$$
\mathcal{L}_{A^{1}}=\Phi \circ \mathcal{L}_{A^{2}} \circ \Phi^{*}
$$

where $\Phi=\prod_{v \in Q_{0}} \varphi_{v}$, thus we may speak unambiguously of the eigenvalues $\lambda_{i}\left(A_{\bullet}\right):=$ $\lambda_{i}\left(\mathcal{L}_{A}\right)$ of a quiver representation $A_{\bullet}$.




---

4.2. Approximate Sections. To measure the distance in $\operatorname{Tot}\left(A_{\bullet}\right)$ between an arbitrary vector $x$ and the space $\Gamma\left(A_{\bullet}\right)$ of sections, we consider the Dirichlet energy:

$$
\mathcal{E}_{A}(x):=\left\langle x, L_{A} x\right\rangle=\sum_{e \in Q_{1}}\left\|A_{e}\left(x_{s(e)}\right)-x_{t(e)}\right\|_{A_{t(e)}}^{2} \in \mathbb{R}_{\geq 0}
$$

Here $\langle-,-\rangle$ is the induced inner product on $\operatorname{Tot}\left(A_{\bullet}\right)$, while and $x_{v}$ denotes the component of $x$ in $A_{v}$, and $\|-\|$ denotes the norm induced by the inner product. As $L_{A}$ is Hermitian, we can form an orthonormal eigenbasis $e_{1}, \ldots, e_{n}$ where $e_{i}$ corresponds to $\lambda_{i}\left(A_{\bullet}\right)$. Writing $x$ in this basis, we have

$$
\mathcal{E}_{A}(x)=\mathcal{E}_{A}\left(\sum_{i} x_{i} e_{i}\right)=\sum_{i} \lambda_{i}\left(A_{\bullet}\right) x_{i}^{2}
$$

Thus, $\sqrt{\mathcal{E}_{A}(x)}$ is the $\lambda_{\bullet}$-weighted distance from $x$ to $\Gamma\left(A_{\bullet}\right)$; and moreover,

$$
\sum_{i: \lambda_{i}(A)=0} x_{i} e_{i}
$$

is the closest vector to $x$ in $\Gamma\left(A_{\bullet}\right)$. This motivates the following definition. (A similar notion for cellular sheaves was introduced in [20]).
DEfinition 4.3. For a quiver $Q$ and an $\mathbf{F d H i l b}(\mathbb{K})$-valued representation $A_{\bullet}$ of $Q$, and $\varepsilon$-approximate section of $A_{\bullet}$ is an $x \in \operatorname{Tot}\left(A_{\bullet}\right)$ such that $\|x\|=1$ and $\mathcal{E}_{A}(x) \leq \varepsilon$.

By Theorem B.1, if $x \in \operatorname{span}\left\{e_{1}, \ldots, e_{k}\right\}$ and $\|x\|=1$, then $x$ is a $\lambda_{k}$-approximate section. Note this is not exhaustive: there can exist $\lambda_{k}$-approximate sections of $A_{\bullet}$ that are not in the span of the first $k$ eigenvectors, e.g. $\lambda_{1} x_{1} e_{1}+\lambda_{k+1} x_{k+1} e_{k+1}$ for small enough $x_{k+1}$. Regardless, to compute approximate sections of a quiver representation one can compute eigenvectors of $L_{A}$ with small eigenvalues. As we have connected approximate sections with the spectra of the quiver representation, we now want to understand how the spectra changes if we perturb the quiver representation (§5), or the underlying quiver (§6).

# 5. Spectral Stability of FeAture Selectors 

Let $Q$ be a quiver and suppose $A_{\bullet}$ and $\widehat{A}_{\bullet}$ are two representations of $Q$. Suppose $\tau$ is a collection $\left\{\left(\tau_{v}: A_{v} \rightarrow \widehat{A}_{v}\right): v \in Q_{0}\right\}$ of linear maps. Define the defect of $\tau$ at an edge $e \in Q_{1}$ to be

$$
\partial(\tau, e)=\left\|\widehat{A}_{e} \tau_{s(e)}-\tau_{t(v)} A_{e}\right\|
$$

Here, and henceforth, the expression $\|-\|$ when applied to a linear map between Hilbert spaces will always indicate the operator norm - for $M: V \rightarrow W$, the norm $\|M\|$ equals the supremum of $\|M x\|_{W}$ over unit vectors $x \in V$. Now the total defect of $\tau$ is:

$$
\partial(\tau)=\left(\sum_{e \in Q_{1}} \partial(\tau, e)^{2}\right)^{\frac{1}{2}}
$$

The defect of $\tau$ is zero if and only if when $\tau$ prescribes a morphism of quiver representations. Given bases of $\operatorname{Tot}\left(A_{\bullet}\right)$ and $\operatorname{Tot}\left(\widehat{A}_{\bullet}\right)$, we view $\tau$ as a block diagonal matrix. Let




---

$\tau^{+}$denote its Moore-Penrose pseudoinverse. The values $\|\tau\|$ and $\left\|\tau^{+}\right\|$are unique up to unitary transforms of $\operatorname{Tot}\left(A_{\bullet}\right)$ and $\operatorname{Tot}\left(\widehat{A}_{\bullet}\right)$. Finally, we let

$$
\kappa(\tau):=\|\tau\|\left\|\tau^{+}\right\|
$$

be the generalised condition number of $\tau$.
We seek to describe how the existence of $\tau$ forces a relationship between the Laplacian spectra of $A_{\bullet}$ and $\widehat{A}$. The first step in this direction is the following lemma.

LEMMA 5.1. For a matrix $\tau$, if $\mathbf{x} \in(\operatorname{ker} \tau)^{\perp}$ then

$$
\|\tau \mathbf{x}\| \geq\left\|\tau^{+}\right\|^{-1}\|\mathbf{x}\|
$$

Proof. Let $\mathbf{u}_{1}, \ldots, \mathbf{u}_{m}$ and $\mathbf{v}_{1}, \ldots, \mathbf{v}_{n}$ be left and right singular vectors of $\tau$ respectively. Let $\mathbf{x}=\sum_{i=1}^{n} x_{i} \mathbf{v}_{i}$. Then $\tau \mathbf{x}=\sum_{i=1}^{\min \{n, m\}} \sigma_{i} x_{i} \mathbf{u}_{i}$, but as $\mathbf{x} \in \operatorname{ker} \tau^{\perp}$ we have that $x_{j}=0$ when $\sigma_{j}=0$ or $j>\min \{m, n\}$. Thus

$$
\|\tau \mathbf{x}\| \geq\left\|\sum_{i=1}^{\min \{n, m\}} \sigma^{+} x_{i} \mathbf{u}_{i}\right\|=\sigma^{+}\|\mathbf{x}\|=\left\|\tau^{+}\right\|^{-1}\|\mathbf{x}\|
$$

where $\sigma^{+}$is the smallest non-zero singular value of $\tau$.
The next theorem describes how the existence of a transformation between quiver representations constrains their eigenvalues. In the statement below (and henceforth), we use $\operatorname{null}(f)$ as a shorthand for the dimension of the kernel of a linear map $f: U \rightarrow V$ of finite-dimensional Hilbert spaces.

THEOREM 5.2. Suppose $A_{\bullet}$ and $\widehat{A}_{\bullet}$ are two representations of a quiver $Q$ whose total spaces have dimensions $n$ and $m$ respectively. Let $\tau=\left\{\tau_{v}: A_{v} \rightarrow \widehat{A}_{v} \mid v \in Q_{0}\right\}$ be a collection of linear maps, viewed as a single map $\operatorname{Tot}\left(A_{\bullet}\right) \rightarrow \operatorname{Tot}\left(\widehat{A}_{\bullet}\right)$. Set $q:=\operatorname{null}(\tau)$; for every integer $k$ such that $1 \leq k \leq n-q$, we have

$$
\lambda_{k}(\widehat{A}) \leq \kappa(\tau)^{2} \lambda_{k+q}(A)+\partial(\tau)\left\|\tau^{+}\right\|\left[2 \kappa(\tau) \lambda_{k+q}(A)^{\frac{1}{2}}+\partial(\tau)\left\|\tau^{+}\right\|\right]
$$

In particular, if $\tau$ is a morphism of quiver representations, then $\partial(\tau)$ vanishes and hence

$$
\lambda_{k}(\widehat{A}) \leq \kappa(\tau)^{2} \lambda_{k+q}(A)
$$

Proof. Let $\mathbf{x}_{1}, \ldots, \mathbf{x}_{n}$ and $\mathbf{y}_{1}, \ldots, \mathbf{y}_{m}$ be eigenvectors of $A_{\bullet}$ and $\widehat{A}$. respectively, ordered by increasing eigenvalue. Suppose $k$ is an integer such that $1 \leq k \leq n-q$. Let $l=k+q$ and define $X_{l}=\operatorname{span}\left\{\mathrm{x}_{1}, \ldots, \mathbf{x}_{l}\right\}$ and $Y_{k}=\operatorname{span}\left\{\mathbf{y}_{k}, \ldots, \mathbf{y}_{m}\right\}$. As $l=k+q$ we have that $\operatorname{dim} \tau\left(X_{l}\right) \geq k$ thus $\operatorname{dim} \tau\left(X_{l}\right)+\operatorname{dim} Y_{k}$ is at least $m+1$ hence $\tau\left(X_{l}\right)$ and $Y_{k}$ intersect nontrivially. Thus there exists some non-zero $\mathbf{y} \in \tau\left(X_{l}\right) \cap Y_{k}$, and as $\mathbf{y} \in Y_{k}$, by Theorem B. 1 it holds that

$$
\lambda_{k}(\widehat{A}) \leq \frac{1}{\|\mathbf{y}\|^{2}} \sum_{e \in Q_{1}}\left\|\widehat{A}_{e} \mathbf{y}_{s(e)}-\mathbf{y}_{t(e)}\right\|^{2}
$$




---

Now we shall bound the right-hand side of the above. Since $y \in \tau\left(X_{l}\right)$ there exists some $x \in X_{l} \cap(\operatorname{ker} \tau)^{\perp}$ such that $\tau x=y$. Using Lemma 5.1 have that

$$
\frac{1}{\|\tau x\|^{2}} \sum_{e \in Q_{1}}\left\|\widehat{A}_{e} \tau_{s(e)} x_{s(e)}-\tau_{t(e)} x_{t(e)}\right\|^{2} \leq \frac{\left\|\tau^{+}\right\|^{2}}{\|x\|^{2}} \sum_{e \in Q_{1}}\left\|\widehat{A}_{e} \tau_{s(e)} x_{s(e)}-\tau_{t(e)} x_{t(e)}\right\|^{2}
$$

Then applying the triangle inquality gives us

$$
\begin{aligned}
& \frac{1}{\|\tau x\|^{2}} \sum_{e \in Q_{1}}\left\|\widehat{A}_{e} \tau_{s(e)} x_{s(e)}-\tau_{t(e)} x_{t(e)}\right\|^{2} \\
& \leq \frac{\left\|\tau^{+}\right\|^{2}}{\|x\|^{2}} \sum_{e \in Q_{1}}\left\|\tau_{t(e)} A_{e} x_{s(e)}-\tau_{t(e)} x_{t(e)}\right\|^{2} \\
& +\frac{2\left\|\tau^{+}\right\|^{2}}{\|x\|^{2}} \sum_{e \in Q_{1}}\left\|\tau_{t(e)} A_{e} x_{s(e)}-\tau_{t(e)} x_{t(e)}\right\|\left\|\widehat{A}_{e} \tau_{s(e)} x_{s(e)}-\tau_{t(e)} A_{e} x_{s(e)}\right\| \\
& +\frac{\left\|\tau^{+}\right\|^{2}}{\|x\|^{2}} \sum_{e \in Q_{1}}\left\|\widehat{A}_{e} \tau_{s(e)} x_{s(e)}-\tau_{t(e)} A_{e} x_{s(e)}\right\|^{2}
\end{aligned}
$$

and then with the Cauchy-Schwarz inequality we have

$$
\begin{aligned}
& \frac{1}{\|\tau x\|^{2}} \sum_{e \in Q_{1}}\left\|\widehat{A}_{e} \tau_{s(e)} x_{s(e)}-\tau_{t(e)} x_{t(e)}\right\|^{2} \\
& \leq \kappa(\tau)^{2} \frac{1}{\|x\|^{2}} \sum_{e \in Q_{1}}\left\|A_{e} x_{s(e)}-\tau_{t(e)} x_{t(e)}\right\|^{2} \\
& +\kappa(\tau)\left\|\tau^{+}\right\|\left[\frac{1}{\|x\|^{2}} \sum_{e \in Q_{1}}\left\|A_{e} x_{s(e)}-\tau_{t(e)} x_{t(e)}\right\|^{2}\right]^{\frac{1}{2}} \partial(\tau)+\left\|\tau^{+}\right\|^{2} \partial(\tau)^{2}
\end{aligned}
$$

and finally since $x \in X_{l}$, we may apply Theorem B. 1 to obtain

$$
\frac{1}{\|\tau x\|^{2}} \sum_{e \in Q_{1}}\left\|\widehat{A}_{e} \tau_{s(e)} x_{s(e)}-\tau_{t(e)} x_{t(e)}\right\|^{2} \leq \kappa(\tau)^{2} \lambda_{l}(A)+2 \kappa(\tau)\left\|\tau^{+}\right\| \lambda_{l}(A)^{\frac{1}{2}} \partial(\tau)+\left\|\tau^{+}\right\|^{2} \partial(\tau)^{2}
$$

completing the proof.
We shall now describe how Theorem 5.2 gives us a bound on the spectral pseudometric between quiver representations. If the total spaces of $A$ and $\widehat{A}_{\bullet}$ have the same dimension, then we can directly compare the associated Laplacian spectra. Following [14], we use the Wasserstein metric to perform such comparisons in order to account for the case where total spaces have different dimensions.

DEFINITION 5.3. For each real number $r \geq 0$, let $B(Q, r)$ be the set of representations $A_{\bullet}$ of $Q$ which satisfy $\max _{e \in Q_{1}}\left\|A_{e}\right\| \leq r$.




---

By design, if $A_{\bullet} \in \mathcal{B}(Q, r)$, then its eigenvalues are bounded by $\left|Q_{1}\right|(r+1)^{2}$.
Given a representation $A_{\bullet}$ of $Q$ with total dimension $n$, its spectral measure is

$$
\mu_{A}=\sum_{i=1}^{n} \delta_{\lambda_{i}(A)}
$$

where $\delta_{\lambda_{i}(A)}$ is the Dirac measure concentrated at $\lambda_{i}(A)$. Given two probability measures $\mu_{1}, \mu_{2}$ on $\mathbb{R}_{\geq 0}$, a coupling $\gamma$ of $\mu_{1}$ and $\mu_{2}$ is any probability measure on $\mathbb{R}_{\geq 0} \times \mathbb{R}_{\geq 0}$ whose marginals on each factor are $\mu_{1}$ and $\mu_{2}$ respectively. Denote by $\Gamma\left(\mu_{1}, \mu_{2}\right)$ the set of all such couplings. Then the Wasserstein $p$-metric between $\mu_{1}$ and $\mu_{2}$ is defined as

$$
W_{p}\left(\mu_{1}, \mu_{2}\right)=\inf _{\gamma \in \Gamma\left(\mu_{1}, \mu_{2}\right)}\left(\int_{\mathbb{R} \geq 0 \times \mathbb{R}_{0}}\|x-y\|^{p} d \gamma(x, y)\right)^{\frac{1}{p}}
$$

Adapting the proof of Theorem 6.3 in [14] we have the following:
THEOREM 5.4. Suppose $A_{\bullet}, \widehat{A}_{\bullet} \in \mathcal{B}(Q, r)$ with total dimensions $n$ and $m$ respectively, where $n \geq m$. Suppose $\tau$ is a non-zero transformation from $A_{\bullet}$ to $\widehat{A}_{\bullet}$. If $\operatorname{rank}(\eta) \geq \operatorname{null}\left(\eta^{*}\right)$ then

$$
W_{1}\left(\mu_{A}, \mu_{\widehat{A}}\right) \leq C
$$

where $C$ depends on $\tau, n$ and $r$. Moreover, if $\|\tau\|,\left\|\tau^{+}\right\| \leq 1+\varepsilon$ and $\partial(\tau), \partial\left(\tau^{*}\right) \leq \varepsilon$ for some $\varepsilon>0$, then we have

$$
\lim _{\varepsilon \rightarrow 0} C=\frac{2 \operatorname{null}(\tau)+2 \operatorname{null}\left(\tau^{*}\right)}{n}\left|Q_{1}\right|(r+1)^{2}
$$

which, if $\operatorname{null}(\tau)+\operatorname{null}\left(\tau^{*}\right)<n / 2$, will be less than naïve bound of $\left|Q_{1}\right|(r+1)^{2}$.
Proof. Define $c_{\tau}=\operatorname{null}(\tau)+\operatorname{null}\left(\tau^{*}\right)$. We will now define a coupling $\gamma$ between $\mu_{A}$ and $\mu_{\widehat{A}}$. For each positive integer $p$, let $[p]$ denote the set $\{1,2, \ldots, p-1, p\}$. Setting $\ell=\operatorname{null}\left(\tau^{*}\right)$ and and $u=n-\operatorname{null}(\tau)$, define the following partition of $[n] \times[m]$ :

$$
\begin{aligned}
& P_{1}=\{(i, i): i \in[u] \backslash[\ell]\} \\
& P_{2}=\{(i, j): i \in[\ell] \text { and } j \in[\ell]\} \\
& \cup\{(i, j): i \in[\ell] \text { and } j \in[m] \backslash[u]\} \\
& \cup\{(i, j): i \in[n] \backslash[u] \text { and } j \in[\ell]\} \\
& \cup\{(i, j): i \in[n] \backslash[u] \text { and } j \in[m] \backslash[u]\} \\
& P_{3}=\{(i, j): i \in[\ell] \text { and } j \in[u] \backslash[\ell]\} \\
& \cup\{(i, j): i \in[n] \backslash[u] \text { and } j \in[u] \backslash[\ell]\} \\
& P_{4}=([n] \times[m]) \backslash\left(P_{1} \cup P_{2} \cup P_{3}\right)
\end{aligned}
$$




---

Now define the desired coupling $\gamma$ as

$$
\gamma=\sum_{\substack{1 \leq i \leq n \\ 1 \leq j \leq m}} w_{i j} \delta\left(\lambda_{i}(A), \lambda_{j}(\widehat{A})\right)
$$

where

$$
w_{i j}= \begin{cases}\frac{1}{n} & (i, j) \in P_{1} \\ \frac{1}{m(n-c \tau)} & (i, j) \in P_{2} \\ \left(\frac{1}{m}-\frac{1}{n}\right) \frac{1}{n-c \tau} & (i, j) \in P_{3} \\ 0 & (i, j) \in P_{4}\end{cases}
$$

Set $R=\left|Q_{1}\right|(r+1)^{2}$, which is an upper bound for the eigenvalues of $A_{\bullet}$. Then using Theorem 5.2 for $\tau$ and $\tau^{*}$ and substituting $R$ gives us

$$
\kappa(\tau)^{-2} \lambda_{i-\operatorname{null}\left(\tau^{*}\right)}\left(A_{\bullet}\right)-a_{\tau^{*}, R} \leq \lambda_{i}\left(\widehat{A}_{\bullet}\right) \leq \kappa(\tau)^{2} \lambda_{i+\operatorname{null}(\tau)}\left(A_{\bullet}\right)+b_{\tau, R}
$$

with the constants

$$
\begin{aligned}
& a_{\tau^{*}, R}=2 \kappa(\tau)^{-1}\left\|\tau^{+}\right\|_{\partial\left(\tau^{*}\right)} \sqrt{R}+\kappa(\tau)^{-2}\left\|\tau^{+}\right\|_{\partial\left(\tau^{*}\right)}^{2} R, \text { and } \\
& b_{\tau, R}=2 \kappa(\tau)\left\|\tau^{+}\right\|_{\partial(\tau)} \sqrt{R}+\left\|\tau^{+}\right\|_{\partial(\tau)}^{2} R
\end{aligned}
$$

Computing cost of $\gamma$ gives us

$$
\begin{aligned}
\mathbf{W}_{1}\left(\mu_{A}, \mu_{\widehat{A}}\right) \leq \frac{1}{n} & {\left[\sum_{k=\operatorname{null}\left(\tau^{*}\right)+1}^{n-\operatorname{null}(\tau)}\left|\lambda_{k}\left(A_{\bullet}\right)-\lambda_{k}\left(\widehat{A}_{\bullet}\right)\right|+c_{\tau} R\right] } \\
& \leq \frac{1}{n}\left[\sum_{k=\operatorname{null}\left(\tau^{*}\right)+1}^{n-\operatorname{null}(\tau)}\left(\kappa(\tau)^{2} \lambda_{k+\operatorname{null}(\tau)}\left(A_{\bullet}\right)-\kappa(\tau)^{-2} \lambda_{k-\operatorname{null}\left(\tau^{*}\right)}(A)\right)\right. \\
& \left.+\left(n-c_{\tau}\right)\left(a_{\tau^{*}, R}+b_{\tau, R}\right)+c_{\tau} R\right]
\end{aligned}
$$

Rearranging the sum on the right side yields

$$
\frac{1}{n}\left[c_{\tau} \kappa(\tau)^{2} R+\left(n-2 c_{\tau}\right)\left(\kappa(\tau)^{2}-\kappa(\tau)^{-2}\right) R+\left(n-c_{\tau}\right)\left(a_{\tau^{*}, R}+b_{\tau, R}\right)+c_{\tau} R\right]
$$

which is the desired $C$.
Suppose $A, B$ are a pair of orthogonal matrices with dimensions $n \times k$ and $n \times l$ respectively. Then the matrix $A^{*} B$ is an orthogonal projection img $B \rightarrow \operatorname{img} A$, where img $A$ denotes the image of $A$. Let the singular values of $A^{*} B$ be $\sigma_{1}, \ldots, \sigma_{r}$ where $r=\min \{k, l\}$. Then the principal angles between img $A$ and img $B$ are defined by $\cos \theta_{i}=\sigma_{i}$ and the Grassmannian metric between img $A$ and img $B$ as defined by [37] is

$$
d_{\mathrm{Gr}_{\infty}}(\operatorname{img} A, \operatorname{img} B):=\left(\sum_{i=1}^{r} \theta_{i}^{2}\right)^{\frac{1}{2}}
$$

Corollary 5.5. Suppose $S, T: \operatorname{Sub}\left(X^{*}\right) \rightarrow \mathrm{Gr}_{\infty}\left(X^{*}\right)$ are two feature selectors on $X$ and suppose $\mathcal{U}$ is a cover of $X$ and $F \subset X^{*}$. Suppose that

$$
\max _{\sigma \in Q_{\mathcal{U}}} d_{\mathrm{Gr}_{\infty}}\left(\left.S F\right|_{\sigma}\right|,\left.T F\right|_{\sigma} \mid\right) \leq \varepsilon<\frac{\pi}{2}
$$




---

for some $\varepsilon>0$, and define

$$
c=\sum_{\sigma \in Q_{0}^{U}}\left|\operatorname{dim} S_{|\sigma|}^{F}-\operatorname{dim} T_{|\sigma|}^{F}\right|
$$

Then, $W_{1}\left(\mu_{A^{S, F}}, \mu_{A^{T, F}}\right)$ is no larger than

$$
\frac{4\left|Q_{1}\right|}{n}\left[\left(1+\cos ^{2} \varepsilon\right) c+\left(2 \sec \varepsilon \tan \varepsilon+\left(1+\sec ^{2} \varepsilon\right) \tan ^{2} \varepsilon+\sec ^{2} \varepsilon-\cos ^{2} \varepsilon\right)(n-c)\right]
$$

where $n=\max \left\{\operatorname{dim} \operatorname{Tot}\left(A_{\bullet}^{S, F}\right), \operatorname{dim} \operatorname{Tot}\left(A_{\bullet}^{T, F}\right)\right\}$
Proof. Assume that $\operatorname{dim} S_{\bullet}^{F} \geq \operatorname{dim} T_{\bullet}^{F}$. Define the transformation $\eta$ with components $\eta_{\sigma}=\pi_{\sigma}^{T} \iota_{\sigma}^{S}$. Then $\cos \varepsilon \leq\|\eta\| \leq 1$ and $1 \leq\left\|\eta^{+}\right\| \leq(\cos \varepsilon)^{-1}$. In order to bound $\partial(\eta)$ note that

$$
\left\|\iota_{\sigma}^{S} \pi_{\sigma}^{S}-\iota_{\sigma}^{T} \pi_{\sigma}^{T}\right\|^{2}=\sin \theta_{\sigma, \max } \leq \sin \varepsilon
$$

where $\theta_{\sigma, \max }$ is the largest principal angle between $S_{|\sigma|}$ and $T_{|\sigma|}$. This is known as the projection metric [37] where the equality can be seen from Theorem 2.6.1 in [13]. This then implies that, for each edge $\sigma \rightarrow \tau$, we have $\partial(\eta, \sigma \rightarrow \tau) \leq 2 \sin \varepsilon$ thus $\partial(\eta) \leq$ $2 \sqrt{\left|Q_{1}\right|} \sin \varepsilon$. Similarly, $\partial\left(\eta^{*}\right) \leq 2 \sqrt{\left|Q_{1}\right|} \sin \varepsilon$. Applying Theorem 5.4 together with these bounds provide the result.

# 6. Eigenvalue Inequalities for Quiver Operations 

So far, we have described our problem as computing sections of a quiver representation. Here we seek to simplify the representation and the underlying quiver whilst preserving its space of sections and bounding the change in its eigenvalues. We will establish similar eigenvalue inequalities when the quiver itself is deformed via certain natural operations. The most convenient framework for extracting such inequalities is to upgrade the given quiver representation to a sheaf, as described below.
6.1. Sheaves over Quivers. Fix a quiver $Q=\left(s, t: Q_{1} \rightarrow Q_{0}\right)$.

DEfinition 6.1. An $\mathbf{F d H i l b}(K)$-valued sheaf $A_{\bullet}$ over $Q$ consists of:

- A finite-dimensional Hilbert space $A_{v}$ for each vertex $v \in Q_{0}$,
- a finite-dimensional Hilbert space $A_{e}$ for each edge $e \in Q_{1}$, and
- for each for each edge $e \in Q_{1}$, a pair of linear maps

$$
A_{s(e) \rightarrow e}: A_{s(e)} \rightarrow A_{e} \quad \text { and } \quad A_{e \leftarrow t(e)}: A_{t(e)} \rightarrow A_{e}
$$

Such sheaves are closely related to representations of quivers. Every representation $A_{\bullet}$ over $Q$ induces a sheaf $\bar{A}_{\bullet}$ over $Q$ by setting $A_{s(e) \rightarrow e}=A_{e}$ and $A_{e \leftarrow t(e)}=\operatorname{id}_{t(e)}$. Conversely, every sheaf evidently induces a representation on the subdivision of $Q$ where every edge $e: u \rightarrow v$ is decomposed into the zigzag $u \rightarrow e \leftarrow v$. Thus, there is a natural notion of Laplacian for sheaves over a quiver, a special case ${ }^{4}$ of which appears in [16].

[^0]
[^0]:    ${ }^{4}$ The only difference between our quiver sheaf Laplacian and the sheaf Laplacians of [16] over onedimensional cell complexes is that we allow edges to have the same source and target vertex. On the other hand, cellular sheaves and their Laplacians are also defined over regular cell complexes of dimension $>1$.




---

DEFINITION 6.2. Suppose $\mathcal{A}_{\bullet}$ is a $\operatorname{FdHilb}(\mathbb{K})$-valued sheaf over a quiver $Q$. Define $\operatorname{Tot}\left(\mathcal{A}_{\bullet}\right)=\prod_{v \in Q_{0}} \mathcal{A}_{v}$ and $\operatorname{Tar}\left(\mathcal{A}_{\bullet}\right)=\prod_{e \in Q_{1}} \mathcal{A}_{e}$.
(1) The boundary operator of $\mathcal{A}_{\bullet}$ is the linear map $B_{\mathcal{A}}: \operatorname{Tot}\left(\mathcal{A}_{\bullet}\right) \rightarrow \operatorname{Tar}\left(\mathcal{A}_{\bullet}\right)$ of $\mathcal{A}_{\bullet}$ given in component form by

$$
\left(B_{\mathcal{A}}\right)_{e, v}= \begin{cases}\mathcal{A}_{v \rightarrow e}-\mathcal{A}_{e \leftarrow v} & \text { if } s(e)=t(e)=v \\ \mathcal{A}_{v \rightarrow e} & \text { if } s(e)=v \text { and } t(e) \neq v \\ -\mathcal{A}_{e \leftarrow v} & \text { if } s(e) \neq v \text { and } t(e)=v \\ 0 & \text { otherwise }\end{cases}
$$

(2) The Laplacian of $\mathcal{A}_{\bullet}$ is then defined as

$$
L_{\mathcal{A}}=B_{\mathcal{A}}^{*} B_{\mathcal{A}}
$$

(3) Finally, the Dirichlet energy for $\mathcal{A}_{\bullet}$ is the function $E_{\mathcal{A}}: \operatorname{Tot}\left(\mathcal{A}_{\bullet}\right) \rightarrow \mathbb{R}$ given by

$$
E_{\mathcal{A}}(x)=\sum_{e \in Q_{1}}\left\|\mathcal{A}_{s(e) \rightarrow e}\left(x_{s(e)}\right)-\mathcal{A}_{e \leftarrow t(e)}\left(x_{t(e)}\right)\right\|_{\mathcal{A}_{e}}^{2}
$$

If one constructs a sheaf $\mathcal{A}$. from a quiver representation $A_{\bullet}$ of $Q$ as described above, then the sheaf boundary operator $B_{\mathcal{A}}$ coincides exactly with the quiver boundary operator $B_{A}$; therefore the Laplacians of $A_{\bullet}$ and $\mathcal{A}_{\bullet}$, as well as their spectra, also coincide in this case.
6.2. Operations on the Quiver. This section describes how the spectrum of a sheaf, or indeed a representation, over a quiver changes under various combinatorial operations on the quiver. Removing an edge or a vertex gives bounds on the change in spectrum, as Proposition A. 1 describes, however these may reduce the dimension of the space of sections. Propositions 6.5, 6.7, and 6.9 describe operations on the quiver, dependent on the sheaf, that preserve the space of sections. These are described for sheaves over a quiver but all these operations also preserve quiver representations. These intermediate results are used to simplify quivers (while bounding the change in eigenvalues) in our Proofs of Theorems 7.1 and 7.2.

DEFINITION 6.3. For a quiver $Q$, define an edge pairing as a collection $P$ of pairs of distinct neighbouring edges $\left(e_{1}^{1}, e_{2}^{1}\right), \ldots\left(e_{1}^{m}, e_{2}^{m}\right)$ of $Q$ such no two edges are repeated, i.e. $e_{j}^{i} \neq e_{l}^{k}$ unless $i=k$ and $j=l$. To simplify notation assume that each pair $\left(e_{1}^{i}, e_{2}^{i}\right)$, the edges $e_{1}^{i}$ and $e_{2}^{i}$ are directed away from their common vertex $u_{i}$. Label the other vertices for $e_{1}^{i}$ and $e_{2}^{i}$, possibly the same vertex, as $v_{i}$ and $w_{i}$ respectively.






---

We then define $Q^{P}$ as the $P$-homotopic quiver to $Q$ where $Q^{P}$ has the same nodes and edges as $Q$ except with each edge $e_{2}^{i}$ replaced by an edge $e_{3}^{i}$ between $v_{i}$ and $w_{i}$.



For $A$. is a sheaf over $Q$ and a pairing $P$ of $Q$, say that $A$. is compatible with $P$ if for each pair $\left(e_{1}^{i}, e_{2}^{i}\right) \in P$ we have that $A_{e_{1}^{i}}=A_{e_{2}^{i}}$ and $A_{u_{i} \rightarrow e_{1}^{i}}=A_{u_{i} \rightarrow e_{2}^{i}}$. Such a compatible sheaf induces a sheaf on $Q^{P}$ as follows: define the sheaf $A^{P}$ on $Q^{P}$ as the same as $A$. on the common edges of $Q$ and $Q^{P}$ and otherwise by $A_{e_{3}^{i}}^{P}=A_{e_{2}^{i}}, A_{e_{3}^{i} \leftarrow e_{3}^{i}}^{P}=A_{e_{1}^{i} \leftarrow e_{1}^{i}}$ and $A_{w_{i} \rightarrow e_{3}^{i}}^{P}=A_{e_{2}^{i} \leftarrow w_{i}}$ for each $i$. The next proposition shows the $i$-th eigenvalue of $A_{\bullet}^{P}$ is bounded by a scalar multiple of the $i$-th eigenvalue of $A$. First we will need a lemma.

Lemma 6.4. Suppose $X, Y, Z \in \mathbb{R}^{n}$. Then

$$
\|X-Z\|^{2}+\|Z-Y\|^{2} \leq \phi^{2}\left(\|X-Y\|^{2}+\|Y-Z\|^{2}\right)
$$

where $\phi$ is the golden ratio $\phi=\frac{1+\sqrt{5}}{2}$. This is also true for any metric space $(M, d)$ and can be written as

$$
d(X, Z)^{2} \leq \phi^{2} d(X, Y)^{2}+\phi d(Y, Z)^{2}
$$

Proof. Let us abbreviate

$$
\begin{aligned}
& x=\|Y-Z\| \\
& y=\|X-Z\| \\
& z=\|X-Y\|
\end{aligned}
$$

If any of $x, y$ or $z$ are zero, then the proposition is immediately true, so assume that $x, y$ and $z$ are strictly positive. By the triangle inequality, we have

$$
\frac{x^{2}+y^{2}}{x^{2}+z^{2}} \leq \frac{x^{2}+(x+z)^{2}}{x^{2}+z^{2}}
$$

We then want to know when the expression on the right side is maximised. As $x, z>0$, there exists $u>0$ for which $x=u z$. Substituting this into the right side gives

$$
\frac{2 u^{2}+2 u+1}{u^{2}+1}
$$

which is maximised when $u=\phi$. Thus, the maximum value of the ratio is $\phi^{2}$. If $X, Y, Z$ are colinear with $Y$ between $X$ and $Z$ and $\|Y-Z\|=\phi\|X-Y\|$, then the maximum is attained, which shows that this inequality is sharp.

Proposition 6.5. For $Q$ a quiver and $P$ an edge pairing of $Q$, suppose that $A$ is a sheaf on $Q$ compatible with $P$. Then the eigenvalues of $A$. and $A^{P}$ are related by

$$
\phi^{-2} \lambda_{j}(A \bullet) \leq \lambda_{j}\left(A_{\bullet}^{P}\right) \leq \phi^{2} \lambda_{j}(A \bullet)
$$

and vice-versa for $j=1, \ldots, n$ where $n$ is the total dimension of $A$.




---

Proof. Using Lemma 6.4 we have

$$
\begin{aligned}
E_{\mathcal{A}}(x) & =\sum_{\left(e_{1}^{i}, e_{2}^{i}\right) \in \mathcal{P}}\left[\frac{\left\|A_{e_{1}^{i} \leftarrow v_{i}} x_{v_{i}}-A_{u_{i} \rightarrow e_{1}^{i}} x_{u_{i}}\right\|^{2}}{A_{e_{1}^{i}}}+\frac{\left\|A_{u_{i} \rightarrow e_{2}^{i}} x_{u_{i}}-A_{e_{2}^{i} \leftarrow w_{i}} x_{w_{i}}\right\|^{2}}{A_{e_{2}^{i}}}\right] \\
& +\sum_{\text {unpaired } e \in Q_{1}} \frac{\left\|A_{s(e) \rightarrow e} x_{s(e)}-A_{e \leftarrow t(e)} x_{t(e)}\right\|^{2}}{A_{s(e)}} \\
& \leq \phi^{2} \sum_{\left(e_{1}^{i}, e_{2}^{i}\right) \in \mathcal{P}}\left[\frac{\left\|A_{u_{i} \rightarrow e_{1}^{i}} x_{u_{i}}-A_{e_{1}^{i} \leftarrow v_{i}} x_{v_{i}}\right\|^{2}}{A_{e_{1}^{i}}}+\frac{\left\|A_{\sum_{3}^{i} \leftarrow v_{i}} x_{v_{i}}-A_{w_{i} \rightarrow e_{3}^{i}} x_{w_{i}}\right\|^{2}}{A_{e_{3}^{i}}}\right] \\
& +\sum_{\text {unpaired } e \in Q_{1}} \frac{\left\|A_{s(e) \rightarrow e} x_{s(e)}-A_{e \leftarrow t(e)} x_{t(e)}\right\|^{2}}{A_{s(e)}} \\
& \leq \phi^{2} E_{\mathcal{A}^{\mathcal{P}}}(x)
\end{aligned}
$$

Then by Theorem B. 2

$$
\lambda_{i}\left(\mathcal{A}_{\bullet}\right)=\min _{\operatorname{dim} V=i}\left[\max _{x \in V \backslash 0} \frac{E_{\mathcal{A}}(x)}{\langle x, x\rangle}\right] \leq \min _{\operatorname{dim} V=i}\left[\max _{x \in V \backslash 0} \frac{\phi^{2} E_{\mathcal{A}^{\mathcal{P}}}(x)}{\langle x, x\rangle}\right]=\phi^{2} \lambda_{i}\left(\mathcal{A}_{\bullet}^{\mathcal{P}}\right)
$$

proving the proposition.
We note that Proposition 6.5 directly applies to graphs. Although we make no use of the following corollary, we hope that it will be of independent interest to spectral graph theorists.

Corollary 6.6. Suppose $G=(V, E)$ is a multigraph with $n$ vertices. Suppose we have an edge pairing $\mathcal{P}=\left(e_{1}^{1}, e_{2}^{1}\right), \ldots\left(e_{1}^{m}, e_{2}^{m}\right)$ on $G$ as in Definition 6.3. Let $\widehat{G}$ with the same nodes and edges as $G$ except with each edge $e_{2}^{i}$ replaced by an edge $e_{3}^{i}$ between $v_{i}$ and $w_{i}$. Then the eigenvalues of $L_{\widehat{G}}$ and $L_{G}$ are related by

$$
\phi^{-2} \lambda_{j}\left(L_{G}\right) \leq \lambda_{j}\left(L_{\widehat{G}}\right) \leq \phi^{2} \lambda_{j}\left(L_{G}\right)
$$

and vice-versa for $j=1, \ldots, n$.
Proposition 6.7. Suppose $\mathcal{A}_{\bullet}$ is a sheaf over a quiver $Q$ with total dimension $n$. Given a subquiver $Q^{\prime}$, let $\mathcal{A}_{\bullet}^{\prime}$ denote the restriction of $\mathcal{A}_{\bullet}$ to $Q^{\prime}$.
6.7(a) If $e \in Q_{1}$ is an edge such that $s(e)=t(e)$ and $A_{s(e)}=A_{t(e)}=$ id then $\lambda_{i}\left(\mathcal{A}_{\bullet}^{\prime}\right)=$ $\lambda_{i}\left(\mathscr{A}_{\bullet}\right)$ for $i=1, \ldots, n$ where $\mathcal{A}_{\bullet}^{\prime}$ is $\mathcal{A}_{\bullet}$ restricted to the subquiver $Q^{\prime}$ of $Q$ with the edge e removed.
6.7(b) Suppose we have an edge pairing $\mathcal{P}=\left(e_{1}^{1}, e_{2}^{1}\right), \ldots\left(e_{1}^{m}, e_{2}^{m}\right)$ of $Q$ such that for each $i$, the edges $e_{1}^{i}, e_{2}^{i}$ have the same source and target vertices. Assume that for each $i$, there exists a linear map $M_{i}: A_{e_{2}^{i}} \rightarrow A_{e_{1}^{i}}$ satisfying both

$$
A_{s\left(e_{1}^{i}\right) \rightarrow e_{1}^{i}}=M_{i} A_{s\left(e_{2}^{i}\right) \rightarrow e_{2}^{i}} \quad \text { and } \quad A_{e_{1}^{i} \leftarrow t\left(e_{1}^{i}\right)}=M_{i} A_{e_{2}^{i} \leftarrow t\left(e_{2}^{i}\right)}
$$




---

Let $Q^{\prime}$ be the subquiver of $Q$ with all the edges $e_{2}^{1}, \ldots, e_{2}^{n}$ removed, and let $\mathcal{A}_{\bullet}^{\prime}$ be the restriction of $\mathcal{A}_{\bullet}$ to $Q^{\prime}$. Then, we have

$$
\left(1+\Gamma_{P}\right)^{-1} \lambda_{i}\left(\mathcal{A}_{\bullet}\right) \leq \lambda_{i}\left(\mathcal{A}_{\bullet}^{\prime}\right) \leq \lambda_{i}\left(\mathcal{A}_{\bullet}\right)
$$

for all $i=1, \ldots, n$, where $\Gamma_{P}:=\max _{i}\left\{|| M_{i} \|_{2}\right\}$.
Proof. For 6.7(a), observe that $E_{\mathcal{A}}(x)=E_{\mathcal{A}^{\prime}}(x)$ and thus the result follows from Theorem B.2. For 6.7(b), we have

$$
\begin{aligned}
E_{\mathcal{A}}(x) \leq & \sum_{\left(e_{1}^{i}, e_{2}^{i}\right) \in P}\left(1+\left\|M_{i}\right\|_{2}\right)\left\|A s\left(e_{1}^{i}\right) \rightarrow e_{1}^{i} x_{s\left(e_{1}^{i}\right)}-\right. \\
& \left.\mathcal{A} e_{1}^{i} \leftarrow t\left(e_{1}^{i}\right) x_{t\left(e_{1}^{i}\right)}\right\|^{2} \\
& +\sum_{\text {unpaired } e \in Q_{1}}\left\|A s(e) \rightarrow e x_{s(e)}-\mathcal{A} e \leftarrow t(e) x_{t(e)}\right\|^{2} \frac{A s(e)}{\mathcal{A} e} \\
\leq & \left(1+\Gamma_{P}\right) E_{\mathcal{A}}(x) .
\end{aligned}
$$

and the result follows from Theorem B.2.
In the following, at the risk of causing ambiguity with self-loops, we will ignore the direction of edges in and use the relation $v \sim e$ if either $s(e)=v$ or $t(e)=v$.

DEfinition 6.8. Let $Q$ be a quiver and let $V$ be a subset of vertices such that there are no edges in $Q$ between vertices of $V$. The $V$-reduced quiver $Q_{V}$ is defined as follows. For each vertex $v \in V$,
(1) first remove $v$ and any associated edges from $Q$;
(2) then, for each pair of edges $(p, q)$ in $Q$ such that $u \sim p \sim v \sim q \sim w$ for vertices $u, w \in Q_{0} \backslash V$, add a new edge $p q$ between $u$ and $w$.
(We note in the second step above that if $u=w$, then $p q$ forms a self-loop.) The resulting quiver is the desired $Q_{V}$.


We now describe an analogue of the Kron reduction of a graph [7] for sheaves over a quiver. As discussed in [16], Kron reduction does not work in general for sheaves over a (loopless) graph. However, as the next proposition shows, if one restricts the type of




---

vertex removed, dependent on the sheaf, and moreover allows for loops in the underlying quiver, then Kron reduction is possible.
Proposition 6.9. Given a sheaf $\mathcal{A}_{\bullet}$ over a quiver $Q$, assume that $V \subset Q_{0}$ is a subset of vertices such that there are no edges in $Q$ between vertices of $V$. Further suppose that for each $v \in V$ there exists some real number $\alpha_{v}>0$ such that for each edge $e \sim v$, we have

$$
\text { either } \quad \mathcal{A}_{v \rightarrow e}^{*} \mathcal{A}_{v \rightarrow e}=\alpha_{v} \mathbf{i d}_{v} d_{v} \quad \text { or } \quad \mathcal{A}_{e \leftarrow v}^{*} \mathcal{A}_{e \leftarrow v}=\alpha_{v} \mathbf{i d}_{v} d_{v}
$$

as appropriate. Then there exists a sheaf $\mathcal{A}_{\bullet}^{V}$ over $Q^{V}$ such that $\Gamma\left(\mathcal{A}_{\bullet}^{V}\right) \cong \Gamma\left(\mathcal{A}_{\bullet}\right)$ and

$$
\lambda_{i}\left(\mathcal{A}_{\bullet}\right) \leq \lambda_{i}\left(\mathcal{A}_{\bullet}^{V}\right) \leq \lambda_{i+r}\left(\mathcal{A}_{\bullet}\right)
$$

for $i=1, \ldots, n-r$ where $n$ is the total dimension of $\mathcal{A}_{\bullet}$ and $r=\sum_{v \in V} \operatorname{dim} \mathcal{A}_{v}$.
Proof. Consider the Laplacian $L^{\mathcal{A}}$. It can be written in a block form as

$$
L^{\mathcal{A}}=\underset{\substack{Q_{0} \backslash V \\ V}}{\left(\begin{array}{cc}
X & Y^{*} \\
Y & D
\end{array}\right)}
$$

As there are no edges between vertices of $V, D$ is a diagonal matrix where the $(v, v)$ block is $d_{v} \alpha_{v} \mathrm{id}_{v}$ where $d_{v}$ is the degree of $v$. Thus $D$ is invertible, and we can form the Schur complement

$$
L^{\mathcal{A}} / D:=X-Y^{*} D^{-1} Y
$$

A vector $\left[\begin{array}{ll}x & z\end{array}\right]^{T}$ satisfies

$$
\left[\begin{array}{cc}
X & Y^{\dagger} \\
Y & D
\end{array}\right]\left[\begin{array}{l}
x \\
z
\end{array}\right]=\left[\begin{array}{l}
0 \\
0
\end{array}\right]
$$

if and only if $X x+Y^{\dagger} z=0$ and $Y x+D z=0$. As $D$ is invertible this can be rearranged to $X x-Y D^{-1} Y^{\dagger} x=0$ hence $\operatorname{ker}\left(L^{\mathcal{A}} / D\right) \cong \operatorname{ker} L^{\mathcal{A}}$. For the interlacing, we can directly apply Theorem B.5.

We will now define the sheaf $\mathcal{A}_{\bullet}^{V}$. As in Definition 6.8, we will ignore orientation of the edges and write $u \sim e$ if either $s(e)=v$ or $t(e)=v$ and $\mathcal{A}_{v \sim e}$ for the corresponding assigned linear map. If $p \neq q$, define $\mathcal{A}_{u \sim p q}^{V}=\left(d_{v} \alpha_{v}\right)^{-1 / 2} \mathcal{A}_{v \sim p}^{*} \mathcal{A}_{u \sim p}$ and likewise for $w$. Otherwise, if $p=q$, define $\mathcal{A}_{u \rightarrow p p}^{V}=Z_{p} \mathcal{A}_{u \sim p}$ and $\mathcal{A}_{p p \leftarrow u}^{V}=0$ for a linear map $Z_{p}$ which we will now define. First observe that for every non-zero vector $x$, we have

$$
\frac{1}{\alpha_{v}} x^{*} \mathcal{A}_{v \sim p} \mathcal{A}_{v \sim p}^{*} x \leq \frac{1}{\alpha_{v}}\left\|\mathcal{A}_{v \sim p}^{*}\right\|^{2}\|x\|^{2}=\frac{1}{\alpha_{v}}\left\|\mathcal{A}_{v \sim p}^{*} \mathcal{A}_{v \sim p}\right\|\|x\|^{2}=\|x\|^{2}
$$

thus there exists some $Z_{p}$ such that

$$
\mathrm{id}-\frac{1}{\alpha_{v}} \mathcal{A}_{v \sim p} \mathcal{A}_{v \sim p}^{*}=Z_{p}^{*} Z_{p}
$$

since the left-hand side is positive semi-definite.




---

Now we claim that $L^{A^{V}}=L^{A} / D$. To do so, consider vertices $u \in Q_{0} \backslash V$ and $v \in V$. For each edge $u \sim p \sim v$, the contribution to the diagonal block indexed by $(u, u)$ of $L^{A} / D$ is

$$
A_{u \sim p}^{*} A_{u \sim p}-\frac{1}{d_{v} \alpha_{v}} \sum_{u \sim q \sim v} A_{u \sim p}^{*} A_{v \sim p} A_{v \sim q}^{*} A_{u \sim q}
$$

We need to show this is equal to the contribution from the new edges of $A^{\bullet}$. For each vertex $u \in Q_{0} \backslash V$, the contribution to the diagonal block is

$$
\begin{aligned}
\sum_{v \in V} \sum_{u \sim p \sim v} & {\left[A_{u \sim p}^{*} A_{u \sim p}-\frac{1}{d_{v} \alpha_{v}} \sum_{u \sim q \sim v} A_{u \sim p}^{*} A_{v \sim p} A_{v \sim q}^{*} A_{u \sim q}\right] } \\
& =\sum_{v \in V}\left[\sum_{u \sim p \sim v}\left[A_{u \sim p}^{*} A_{u \sim p}-\frac{d_{v}^{u}}{d_{v} \alpha_{v}} A_{u \sim p}^{*} A_{v \sim p} A_{v \sim p}^{*} A_{u \sim p}\right]\right. \\
& \left.\quad+\sum_{\substack{u \sim p \sim v \\
u \sim q \sim v}} \frac{1}{d_{v \alpha_{v}}} p \neq q\right] \\
& \left(A_{v \sim p}^{*} A_{u \sim p}-A_{v \sim q}^{*} A_{u \sim q}\right)^{*}\left(A_{v \sim p}^{*} A_{u \sim p}-A_{v \sim q}^{*} A_{u \sim q}\right)
\end{aligned}
$$

where $d_{v}^{u}$ is the number of edges between $u$ and $v$. The term on the last line corresponds to the new self-loops on $u$ given by $v$. By the defining property of $Z_{p}$, the term

$$
\sum_{u \sim p \sim v}\left[A_{u \sim p}^{*} A_{u \sim p}-\frac{d_{v}^{u}}{d_{v} \alpha_{v}} A_{u \sim p}^{*} A_{v \sim p} A_{v \sim p}^{*} A_{u \sim p}\right]
$$

equals

$$
\sum_{u \sim p \sim v}\left[\frac{d_{v}-d_{v}^{u}}{d_{v} \alpha_{v}} A_{u \sim p}^{*} A_{\nu \sim p} A_{v \sim p}^{*} A_{u \sim p}+A_{u \sim p}^{*} Z_{p}^{*} Z_{p} A_{u \sim p}\right]
$$

and thus corresponds with the contribution of the self-loop $p p$ and the new edges to different vertices, as required.

# 7. Reduction of the Feature Selector Problem 

Using the quiver operations in $\S 6$, we can reduce the number of vertices in the quiver whilst preserving the space of sections; this allows us to reduce the difficulty of computing approximate sections.

THEOREM 7.1. Let $S$ be a feature selector on $X, \mathcal{U}$ a cover of $X$ such that $Q^{\mathcal{U}}$ is (weakly) connected, and $F \subset X^{*}$. Fix a vertex $\sigma_{0} \in Q_{0}^{F}$. Then there exists a quiver $Q^{\prime}$ and a representation $A^{\prime}$ 。 of $Q^{\prime}$ satisfying the following properties:
(1) The quiver $Q^{\prime}$ has only one vertex and $\left|Q_{0}^{F}\right|$ edges.
(2) The Laplacian of $A^{\prime}bullet$ is:

$$
\sum_{\tau \in Q_{0}^{\mathcal{U}}}\left[\operatorname{id}_{\sigma_{0}}-\pi_{\sigma_{0}}^{F} \iota_{\tau}^{F} \pi_{\tau}^{F} \iota_{\sigma_{0}}^{F}\right]
$$




---

(3) There exist constants $C_{1}, C_{2}>0$ that depend on $\mathcal{S}, \mathcal{U}$ and $F$ such that

$$
C_{1} \lambda_{i}\left(\mathcal{N}_{\bullet}^{S, F}\right) \leq \lambda_{i}\left(\mathcal{A}_{\bullet}^{\prime}\right) \leq C_{2} \lambda_{i+k}\left(\mathcal{N}_{\bullet}^{S, F}\right)
$$

for $i=1, \ldots, n-k$.
Here n is the total dimension of $\mathcal{N}_{\bullet}^{S, F}$ and $k:=n-\operatorname{dim} \mathcal{A}_{\sigma_{0}}^{S, F}$.

Proof. We view $\mathcal{N}_{\bullet}^{S, F}$ as a sheaf $\mathcal{A}_{\bullet}$ over a quiver $Q$, defined as follows:

$$
\begin{aligned}
& Q_{0}=\left\{v_{\sigma}: \sigma \in \mathcal{Q}_{0}^{\cup}\right\} \cup\left\{v_{\sigma \tau}:(\sigma \rightarrow \tau) \in \mathcal{Q}_{1}^{\cup}\right\}, \\
& Q_{1}=\left\{e_{\sigma \tau}, r_{\sigma \tau}^{D L}, r_{\sigma \tau}^{L D}:(\sigma \rightarrow \tau) \in \mathcal{Q}_{1}^{U}\right\}, \\
& s\left(e_{\sigma \tau}\right)=v_{\sigma}, \quad t\left(e_{\sigma \tau}\right)=v_{\tau}, \quad s\left(r_{\sigma \tau}^{D L}\right)=s\left(r_{\sigma \tau}^{L D}\right)=v_{\sigma}, \quad t\left(r_{\sigma \tau}^{D L}\right)=t\left(r_{\sigma \tau}^{L D}\right)=v_{\sigma \tau} \text {. }
\end{aligned}
$$

This is precisely the merged quiver on which $\mathcal{N}_{\bullet}^{S, F}$ is defined, except that we have dispensed with identity self-loops in light of Proposition 6.7(a). The desired sheaf $\mathcal{A}_{\bullet}$ assigns the following data to vertices and edges of $Q$ for each $\sigma \in \mathcal{Q}_{0}^{U}$ :

$$
\begin{array}{ll}
\mathcal{A}_{v_{\sigma} \rightarrow e_{\sigma \tau}}=\pi_{\tau}^{F} \circ \iota_{\sigma}^{F}, & \mathcal{A}_{e_{\sigma \tau} \leftarrow v_{\tau}}=\mathrm{id} \\
\mathcal{A}_{v_{\sigma} \rightarrow r_{\sigma \tau}^{D L}}=\iota_{\tau}^{F} \circ \pi_{\tau}^{F} \circ \iota_{\sigma}^{F}, & \mathcal{A}_{r_{\sigma \tau}^{D L} \leftarrow v_{\sigma}}=\mathrm{id} \\
\mathcal{A}_{v_{\sigma} \rightarrow r_{\sigma \tau}^{L D}}=\iota_{\sigma}^{F}, & \mathcal{A}_{r_{\sigma \tau}^{L D} \leftarrow v_{\sigma}}=\mathrm{id}
\end{array}
$$

Use Proposition 6.7(b) to get a new copy $e_{\sigma \tau}^{2}$ of the edge $e_{\sigma \tau}$ with the maps multiplied by $\iota_{\tau}^{F}$. Use this edge with Proposition 6.5 to move the edge $r_{\sigma \tau}^{D L}$ to an edge between $v_{\tau}$ and $v_{\sigma \tau}$, then using the edge $r_{\sigma \tau}^{L D}$ with Proposition 6.5 move this edge between $v_{\tau}$ and $v_{\sigma \tau}$ to an edge between $v_{\sigma}$ and $v_{\tau}$ which has maps $\iota_{\sigma}$ and $\iota_{\tau}$ respectively. Call this edge $p_{\sigma \tau}$. Using Proposition 6.7(b) can remove both $e_{\sigma \tau}$ and $e_{\sigma \tau}^{2}$ since $\pi_{\tau}^{F}$ is the left inverse of $\iota_{\tau}^{F}$. Finally, we can remove the edge $r_{\sigma \tau}^{L D}$ with Proposition 6.9 as $\left(\iota_{\sigma}^{F}\right)^{*} \iota_{\sigma}^{F}=\mathrm{id}$. Now choose some vertex $\sigma_{0}$. As the nerve is connected, and each edge from each vertex has the same restriction maps to that vertex we can keep applying Proposition 6.5 until all edges have $\sigma_{0}$ as a boundary. There might be double edges, but these can be removed with Proposition 6.7(b). Then we apply Proposition 6.9 to reduce to just the vertex $\sigma_{0}$. The Laplacian is now

$$
\sum_{\tau \in \mathcal{Q}_{0}^{U}}\left[\operatorname{id}_{\sigma_{0}}-\pi_{\sigma_{0}}^{F} \iota_{\tau}^{F} \pi_{\tau}^{F} \iota_{\sigma_{0}}^{F}\right]
$$

and the eigenvalue relationship follows by tracking all the uses of Propositions 6.7(a), $6.7(\mathrm{~b}), 6.5,6.9$

THEOREM 7.2. Let $\mathcal{S}$ be a feature selector on a set $X$ equipped with a cover $\mathcal{U}$. For each subset $F \subset X^{*}$, here exists a sheaf $\mathcal{A}^{\prime}$ over a quiver $Q^{\prime}$ with Laplacian

$$
\left(L_{\mathcal{A}^{\prime}}\right)_{\sigma, \tau}= \begin{cases}\sum_{\tau \subset \sigma}\left(2 \mathrm{id}_{\sigma}-\pi_{\sigma}^{F} \iota_{\tau}^{F} \pi_{\tau}^{F} \iota_{\sigma}^{F}\right)+\sum_{\sigma \subset \gamma} \pi_{\sigma}^{F} \iota_{\gamma}^{F} \pi_{\gamma}^{F} \iota_{\sigma}^{F} & \text { if } \sigma=\tau \\ -\pi_{\sigma}^{F} \iota_{\tau}^{F} & \text { if } \tau \subset \sigma \text { or } \sigma \subset \tau \\ 0 & \text { otherwise }\end{cases}
$$




---

such that there is an isomorphism $\Gamma\left(\mathcal{A}_{\bullet}^{\prime}\right) \cong \Gamma\left(\mathcal{M}_{\bullet}^{S, \mathcal{F}}\right)$; and moreover, we have

$$
\lambda_{i}\left(\mathcal{M}_{\bullet}^{S, \mathcal{F}}\right) \leq \lambda_{i}\left(\mathcal{A}_{\bullet}^{\prime}\right) \leq \lambda_{i+k}\left(\mathcal{N}_{\bullet}^{S, \mathcal{F}}\right)
$$

for all $i \in\{1, \ldots, n-k\}$. Here $\mathcal{M}_{\bullet}^{S, \mathcal{F}}$ is the mixed representation of Definition 3.9, while $n$ is its total dimension and $k:=n-\sum_{\sigma \in \mathcal{Q}_{0}} \operatorname{dim} \mathcal{A}_{\sigma}^{S, \mathcal{F}}$.

Proof. Consider the representation $\left(\mathcal{A}_{\bullet}^{S, \mathcal{F}}\right)^{*} \sqcup_{R} \widehat{\mathcal{A}}_{\bullet}^{S, \mathcal{F}}$ as defined in Definition 3.9, and view it as a sheaf $\mathcal{A}_{\bullet}$ over a quiver $\mathcal{Q}$. We can immediately remove identity self-loops using Proposition 6.7(a). The quiver $\mathcal{Q}$ is as follows:

$$
\begin{gathered}
\mathcal{Q}_{0}=\left\{v_{\sigma}: \sigma \in \mathcal{Q}_{0}^{U}\right\} \cup\left\{v_{\sigma \tau}:(\sigma \rightarrow \tau) \in \mathcal{Q}_{1}^{U}\right\} \\
\mathcal{Q}_{1}=\left\{e_{\sigma \tau}, r_{\sigma \tau}^{D L}, r_{\sigma \tau}^{L D}:(\sigma \rightarrow \tau) \in \mathcal{Q}_{1}^{U}\right\} \\
s\left(e_{\sigma \tau}\right)=v_{\tau}, \quad t\left(e_{\sigma \tau}\right)=v_{\sigma}, \\
s\left(r_{\sigma \tau}^{D L}\right)=s\left(r_{\sigma \tau}^{L D}\right)=v_{\sigma}, \quad t\left(r_{\sigma \tau}^{D L}\right)=t\left(r_{\sigma \tau}^{L D}\right)=v_{\sigma \tau}
\end{gathered}
$$

The sheaf $\mathcal{A}$. consists of the following for each $\sigma \in \mathcal{Q}_{U}$ :

$$
\begin{array}{ll}
\mathcal{A}_{v_{\tau} \rightarrow e_{\sigma \tau}}=\pi_{\sigma}^{\mathcal{F}} \circ \iota_{\tau}^{\mathcal{F}}, & \mathcal{A}_{e_{\sigma \tau} \leftarrow v_{\sigma}}=\mathrm{id} \\
\mathcal{A}_{v_{\sigma} \rightarrow r_{\sigma \tau}^{D L}}=\iota_{\tau}^{\mathcal{F}} \circ \pi_{\tau}^{\mathcal{F}} \circ \iota_{\sigma}^{\mathcal{F}}, & \mathcal{A}_{r_{\sigma \tau}^{D L} \leftarrow v_{\sigma}}=\mathrm{id} \\
\mathcal{A}_{v_{\sigma} \rightarrow r_{\sigma \tau}^{L D}}=\iota_{\sigma}^{\mathcal{F}}, & \mathcal{A}_{r_{\sigma \tau}^{L D} \leftarrow v_{\sigma}}=\mathrm{id}
\end{array}
$$

We can use Proposition 6.9 to remove each $v_{\sigma \tau}$. In doing so, we add three new self-loops to $v_{\sigma}$; two identities and a self loop with maps $\iota_{\sigma}^{\mathcal{F}}$ and $\iota_{\tau}^{\mathcal{F}} \circ \pi_{\tau}^{\mathcal{F}} \circ \iota_{\sigma}^{\mathcal{F}}$. The two identity self loops can be removed with Proposition 6.7(a).
7.1. Remarks on computation. In Theorems 7.1 and 7.2 , we have assumed that $L$ is Hermitian with respect to some orthonormal basis. Often, however, the bases we would prefer to use are not orthogonal with respect to our chosen inner product. We will see such an example in $\S 8$, where computing inner products is straightforward whilst finding an orthonormal basis is computationally infeasible. It is then advantageous then to compute eigenvectors of a Laplacian without such a change of basis. Suppose, for each $\sigma \in U$, we have some basis $\mathcal{B}_{\sigma}$ of $\mathcal{S}_{|\sigma|}^{\mathcal{F}}$ and a Hermitian positive definite matrix $M_{\sigma}^{S, \mathcal{F}}$ representing the inner product in this basis. As $M_{\sigma}^{S, \mathcal{F}}$ is positive definite there exists an invertible $W_{\sigma}$ such that $M_{\sigma}^{S, \mathcal{F}}=W_{\sigma}^{*} W_{\sigma}$. Then, in this basis, we now have for $\sigma, \tau \in U$

$$
\begin{gathered}
\pi_{\sigma}^{\mathcal{F}} \iota_{\tau}^{\mathcal{F}}=W_{\sigma}^{-*} M_{\sigma \tau}^{S, \mathcal{F}} W_{\tau}^{-1} \\
\pi_{\sigma}^{\mathcal{F}} \iota_{\tau}^{\mathcal{F}} \pi_{\tau}^{\mathcal{F}} \iota_{\sigma}^{\mathcal{F}}=W_{\sigma}^{-*} M_{\sigma \tau}^{S, \mathcal{F}}\left(M_{\tau}^{S, \mathcal{F}}\right)^{-1} M_{\tau \sigma}^{S, \mathcal{F}} W_{\sigma}^{-1}
\end{gathered}
$$

where $M_{\sigma \tau}^{S, \mathcal{F}}$ is the matrix of inner products between $\mathcal{B}_{\sigma}$ and $\mathcal{B}_{\tau}$. Now computing eigenvectors of a Laplacian $L$ in this basis can be realised as the generalised eigenvector problem

$$
L x=\lambda M_{U}^{S, \mathcal{F}} x
$$

where $M_{U}^{S, \mathcal{F}}$ is the block diagonal matrix with blocks $M_{\sigma}^{S, \mathcal{F}}$ for $\sigma \in U$.




---

As the matrices $M_{\tau}^{S, F}$ are Hermitian and positive-definite, the products

$$
M_{\sigma \tau}^{S, F}\left(M_{\tau}^{S, F}\right)^{-1} M_{\tau \sigma}^{S, F}
$$

can be quickly computed using the Cholesky decomposition of $M_{\tau}^{S, F}$. Furthermore, as $L$ is Hermitian and usually sparse, there exist computationally efficient methods for calculating its smallest eigenvalues and their eigenvectors, e.g. variations on the Lanczos method [21], combined with the Cholesky decomposition (see e.g. [18]) of $L+\alpha I$ for some small $\alpha>0$.

# 8. Single-Cell Chromatin Accessibility 

Chromatin is a macromolecule consisting of DNA and certain proteins, primarily histones [4]. Histones facilitate the dense compaction of DNA, which allows it to fit inside limited space within the cell nucleus. The fundamental unit of chromatin is a nucleosome, which consists of approximately 147 base-pairs (namely, the usual A, C, G and T nucleotides) wound around histone molecules. The density of nucleosomes varies considerably across the genome; low density regions are more accessible to transcription factors and other binding proteins. Thus, understanding the relative accessibility of various parts of the genome is important in the study of gene regulation and its variation across different cell types.

Among the most promising experimental frameworks for measuring chromatin accessibility is ATAC-seq [1], which has been extended to single cell sequencing scATACseq (see e.g. [28]). The output of scATAC-seq may be viewed from a mathematical perspective as follows. Consider a set $X$ of cells $\left\{x_{1}, \ldots, x_{N}\right\}$, with $N$ being on the order of thousands. Each cell $x_{i}$ has a genome consisting of $M$ base pairs, where $M$ is approximately three billion. The output of ATAC-seq on $X$ is an $N \times M$ integer matrix. For each $1 \leq i \leq N$ and $1 \leq j \leq M$, the entry $\alpha_{i, j}$ is a number in $\{0,1,2\}$ representing the accessibility (for cell $x_{i}$ at the $j$-th genomic position). Such data is high-dimensional, noisy and sparse, and hence warrants feature selection. This is accomplished via a class of techniques called peak-calling algorithms [36]. The goal of these methods is to identify specific locations along the genome, called summits, which are significantly accessible across the cells in $X$ - see for instance the MACS2 algorithm [39].

REMARK 8.1. We are often interested in quantifying accessibility when one restricts to various sub-populations $Y \subset X$ of cell types. However, the peaks of various $Y$ may be lost when calling peaks on $X$, particularly when the cardinalities of the $X$ under consideration are unbalanced. The standard remedy is to first cluster the data and then call peaks on each cluster [28]. Subsequently, peaks from all the clusters are combined, with various rules beings applied for grouping and extending peaks which overlap. We show below how the quiver Laplacian provides a different mechanism for achieving similar results.




---

8.1. Pre-processing the data. We use the single-cell ATAC-seq data of [28], which consist of 28,274 tumour-infiltrating T cells. The pre-processing steps are the same as those of ibid:
(1) We align fragments to the GRCH37/HG19 assembly.
(2) We filter sample profiles to keep those with at least 1,000 fragments and a transcription start site (TSS) enrichment score of 8 .
(3) We create a count matrix by tiling the genome with 2,500 base-pair windows and counting overlaps of endpoints of fragments with the windows.
(4) Next, we binarise this matrix and retain only the top 20,000 most accessible sites; call the resulting $28,724 \times 20,000$ boolean matrix $B$.
(5) We then create a frequency-inverse document frequency matrix, apply truncated singular value decomposition to obtain the 2 nd to 25 th singular vectors. This results in a reduced matrix $E$ of size $28724 \times 24$.
8.2. Generating the quiver. We build an undirected graph $G$ from the reduced matrix $E$ as follows. Its vertices are the cells $C_{i}$, which correspond to rows of $E$. Treating each such row as a vector in $\mathbb{R}^{24}$, let $\delta_{i, j} \geq 0$ be the Euclidean distance between rows $i$ and $j$ for each $i<j$. We construct the 15 nearest neighbour graph generated by the $\delta_{i, j}$ distances. Our analysis now deviates from [28]. Using the Leiden algorithm [33] the vertex set $V$ of $G$ is partitioned into finitely many communities, $V=\amalg_{i} V_{i}$. As in ibid, communities of size $<200$ are excluded. We then generate a cover $\mathcal{U}$ of $X$ from the surviving communities as follows: each cover element $U_{i} \in \mathcal{U}$ has the form $V_{i} \cup W_{i}$, where $W_{i} \subset\left(V-V_{i}\right)$ consists of those vertices which share an edge with some vertex of $V_{i}$. The resulting quiver $Q_{\mathcal{U}}$ has 87 vertices, and is depicted in Figure 6A. Similarly, Figure 6B displays the contents of each vertex relative to the overall distribution, using the cell types identified in [28].
8.3. Building the representation. Having constructed $Q_{\mathcal{U}}$, we apply our feature selector $S$ - which in this case is the MACS2 peak-calling algorithm [39] - to the fragment profiles of cells corresponding to each individual vertex. In the notation of Section 2, the input $\mathcal{F}$ is given by the columns of the binarised matrix $B$; explicitly, the map $f_{j}: X \rightarrow \mathbb{R}$ associated to the $j$-th column of $E$ sends each $x_{i}$ to the entry $B_{i j} \in\{0,1\}$. Calling peaks on this set of features produces a vector space $S_{|\sigma|} \subset V(\mathcal{F})$ for every vertex $\sigma$ of $Q_{\mathcal{U}}$

We used the same parameters as in [28], and obtained several hundred thousand summits for each vertex as a result. For the purposes of this demonstration, we retained only the most significant 1,000 summits per vertex. Thus the total dimension of the selected vector spaces is 87,000. Since peak-calling on different sub-populations may change the true summit location on the genome slightly, we follow [38] and use a Gaussian kernel between summits (with bandwidth equal to 1,000 base-pairs) as the inner product on $V(\mathcal{F})$. This allows us to build the mixed representation $\underline{M}_{\bullet}^{S, \mathcal{F}}$ (see Definition 3.9).
8.4. Results. We computed the first 3,000 eigenvectors of the Laplacian of $\underline{M}_{\bullet}^{S, \mathcal{F}}$. Since the total space admits a distinguished basis whose vectors correspond to summits (i.e.,




---

certain genomic positions $\left\{\mathbf{p}_{k}\right\}$ ), we may associate to each eigenvector $\mathbf{v}=\sum_{k} \alpha_{k} \mathbf{p}_{k}$ the subset of supported genomic positions $P_{\mathbf{v}}:=\left\{k \mid \alpha_{k} \neq 0\right\}^{5}$. Figure 6D shows that for an overwhelming majority of eigenvectors $\mathbf{v}$, the diameter of $P_{\mathbf{v}}$ for most $\mathbf{v}$ approximately equals 147 base-pairs, which is the average length of DNA around a nucleosome. A small fraction of the eigenspaces had dimension $>1$; this resulted in a mixing of genomic positions, as shown by the blue outliers in Figure 6D. Nevertheless, in almost all cases, we observed that the genomic supports of eigenvectors are tightly aligned across the vertices of $\mathcal{Q}^{\cup}$.

We then performed a more detailed analysis of the sparsity pattern of the 3,000 eigenvectors. The outcome of this analysis has been summarised in Figure 6E, which plots the 3,000 eigenvectors against all 87 vertices of $\mathcal{Q}^{\cup}$ and highlights those vertices along which a given eigenvector has a non-zero component. We observe that the eigenvectors fall broadly into two classes. The first class, which is considerably larger, consists of those eigenvectors whose genomic support contains summits which are shared by most, if not all vertices: see, for instance, the components of eigenvector 11 in Figure 7. The second class contains eigenvectors whose genomic support contains summits which are shared by a small fraction of the vertices. A prime example of this type is eigenvector 2702, which has nonzero components along only 3 of the 87 vertices, and has also been depicted in Figure 7.

Finally, we note that (at least for these two examples) the size of the support of the eigenvector relates to biological function. Eigenvector 11, for instance, is concentrated in a regulatory region a few hundred base pairs downstream of the gene FAM72D. This gene is involved in the cell cycle [9], and is therefore relevant to most subpopulations of cells. On the other hand, eigenvector 2702 lies just downstream of the gene STAT3, which is a transcription factor known to be an important regulator for differentiation and proliferation in Th1, Th17, and Treg cells [27]. We also note that this eigenvector was only supported on the vertices $8,(8,11)$, and 11 (Figure 7). These vertices are particularly enriched in Th1, Th17 and Treg cells (see Figure 6B). Indeed, Figure 6E reveals that many other eigenvectors are also uniquely supported on the vertices $8,(8,11), 11$ and $(1,11)$. Since vertex 11 is relatively disconnected from the other vertices, our analysis highlights it as an unusual sub-population of $X$.

# Code and data availability 

Code produced for the analysis will be available at https://github.com/osumray/harmonic_feature_selection.
The data from [28] is available from the Gene Expression Omnibus with accession number GSE129785.

[^0]
[^0]:    ${ }^{5}$ Or more precisely, $\left|\alpha_{k}\right|>10^{-5}$, the tolerance parameter for ARPACK-NG [22] in our experiment.




---

# Appendix A. Removing Edges and Vertices 

The following extends known results from graphs, e.g. see [34] and [35] respectively.
Proposition A.1. Let $\mathcal{A}_{\bullet}$ be a sheaf over a quiver $Q$, and let $n$ be its total dimension.
A.1(a) Let $R \subset Q_{1}$ be a subset of edges of $Q$. Let $Q^{\prime}$ be the quiver with edges $Q_{1} \backslash R$ and $\mathcal{A}^{\prime}$ the restriction of $\mathcal{A}$ to $Q^{\prime}$. Then

$$
\lambda_{k+i}(\mathcal{A}_{\bullet}) \leq \lambda_{k+i}\left(\mathcal{A}_{\bullet}^{\prime}\right) \leq \lambda_{k+r+i}(\mathcal{A}_{\bullet})
$$

for $i=1, \ldots, n-k-r$ where $k=\operatorname{dim} \Gamma\left(\mathcal{A}_{\bullet}\right)$ and $r=\sum_{e \in R} \operatorname{dim} \mathcal{A}_{e}$.
A.1(b) Suppose $V \subset Q_{0}$ is a subset of vertices of $Q$. Let $Q^{\prime}$ be the quiver with vertices $Q_{0} \backslash V$ and all edges $e \in Q_{1}$ such that either $s(e) \in V$ or $t(e) \in V$, and $\mathcal{A}^{\prime} \cdot$ the restriction of $\mathcal{A}_{\bullet}$ to $Q^{\prime}$. Then

$$
\lambda_{i}\left(\mathcal{A}_{\bullet}\right)-w_{1} \leq \lambda_{i}\left(\mathcal{A}^{\prime} \bullet\right) \leq \lambda_{k+i}\left(\mathcal{A}_{\bullet}\right)-w_{2}
$$

for $i=1, \ldots, n-k$ where $k=\sum_{u \in Q_{0} \backslash V} \operatorname{dim} \mathcal{A}_{u}$ and

$$
\begin{aligned}
w_{1} & =\max _{v \in V}\left\{\sum_{\substack{s(e)=v \\
t(e) \notin V}} \sigma_{\max }\left(A_{v \rightarrow e}\right)^{2}+\sum_{\substack{t(e)=v \\
s(e) \notin V}} \sigma_{\max }\left(A_{e \leftarrow v}\right)^{2}\right\} \\
w_{2} & =\min _{v \in V}\left\{\sum_{\substack{s(e)=v \\
t(e) \notin V}} \sigma_{\min }\left(A_{v \rightarrow e}\right)^{2}+\sum_{\substack{t(e)=v \\
s(e) \notin V}} \sigma_{\min }\left(A_{e \leftarrow v}\right)^{2}\right\}
\end{aligned}
$$

Proof of Proposition A.1(A). Define $L_{\mathcal{A}, \mathrm{op}}=B_{\mathcal{A}} B_{\mathcal{A}}^{*}$. Let $k=\operatorname{dim} \operatorname{ker} L_{\mathcal{A}}$ and $c=\operatorname{dim} \operatorname{ker} L_{\mathcal{A}, \text { op }}$. Then for $i=1, \ldots, n-k$, we have that

$$
\lambda_{k+i}\left(L_{\mathcal{A}}\right)=\lambda_{c+i}\left(L_{\mathcal{A}, \mathrm{op}}\right)
$$

Now, removing the set of edges $R \subset Q_{1}$ corresponds to the $r \times r$ principal submatrix of $L_{\mathcal{A} \text {,op }}$, where $r:=\sum_{e \in R} \operatorname{dim} \mathcal{A}_{e}$. By Theorem B. 3 we have

$$
\lambda_{i}\left(L_{\mathcal{A}, \mathrm{op}}\right) \leq \lambda_{i}\left(L_{\mathcal{A}^{\prime}, \mathrm{op}}\right) \leq \lambda_{i+r}\left(L_{\mathcal{A}, \mathrm{op}}\right)
$$

where $i \in\{1, \ldots, m-r\}$ thus

$$
\lambda_{k+i}\left(\mathcal{A}_{\bullet}\right) \leq \lambda_{k+i}\left(\mathcal{A}_{\bullet}^{\prime}\right) \leq \lambda_{k+r+i}\left(\mathcal{A}_{\bullet}\right)
$$

for $i \in\{1, \ldots, n-k-r\}$.
Proof of Proposition A.1(B). The boundary matrix $B_{\mathcal{A}}$ has block form

$$
\left[\begin{array}{ll}
B_{11} & 0 \\
B_{21} & B_{22}
\end{array}\right]
$$

where $B_{11}=B_{\mathcal{A}^{\prime}}$. Here, $B_{\mathcal{A}}$ has row blocks indexed by edges between vertices in $V$ and column blocks indexed by vertices in $V$. Then Laplacian $L_{\mathcal{A}}=B_{\mathcal{A}}^{*} B_{\mathcal{A}}$ has block form

$$
\left[\begin{array}{cc}
B_{11}^{*} B_{11}+B_{21}^{*} B_{21} & B_{21}^{*} B_{22} \\
B_{22}^{*} B_{21} & B_{22}^{*} B_{22}
\end{array}\right]
$$




---

Define $L_{Q_{0} \backslash V}=B_{11}^{*} B_{11}+B_{21}^{*} B_{21}$ which is a principal submatrix of $L_{A}$. Note that $B_{21}^{*} B_{21}$ is a diagonal matrix: The $v, v$ block is

$$
\sum_{\substack{s(e)=v \\ t(e) \neq V}} A_{v \rightarrow e}^{*} A_{v \rightarrow e}+\sum_{\substack{t(e)=v \\ s(e) \neq V}} A_{e \leftarrow v}^{*} A_{e \leftarrow v}
$$

We now have that

$$
\begin{aligned}
\lambda_{i}\left(A_{\bullet}^{\prime}\right) & =\lambda_{i}\left(B_{11}^{*} B_{11}\right)=\lambda_{i}\left(L_{Q_{0} \backslash V}-B_{21}^{*} B_{21}\right) \leq \lambda_{i}\left(L_{Q_{0} \backslash V}\right)+\lambda_{n-k}\left(-B_{21}^{*} B_{21}\right) \\
& =\lambda_{i}\left(L_{Q_{0} \backslash V}\right)-\lambda_{1}\left(B_{21}^{*} B_{21}\right) \\
& =\lambda_{i}\left(L_{Q_{0} \backslash V}\right)-\min _{v \in V} \lambda_{1}\left(\sum_{\substack{s(e)=v \\
 muj(e) \neq V}} A_{v \rightarrow e}^{*} A_{v \rightarrow e}+\sum_{\substack{t(e)=v \\
 s(e)~\neq~V}} A_{e \leftarrow v}^{*} A_{e \leftarrow v}\right) \\
& \leq \lambda_{i}\left(L_{Q_{0} \backslash V}\right)-\min _{v \in V}\left\{\sum_{\substack{s(e)=v \\
 t(e) \neq V}} \lambda_{1}\left(A_{v \rightarrow e}^{*} A_{v \rightarrow e}\right)+\sum_{\substack{t(e)=v \\
 s(e) \neq V}} A_{e \leftarrow v}^{*} A_{e \leftarrow v}\right\} \\
& =\lambda_{i}\left(L_{Q_{0} \backslash V}\right)-\min _{v \in V}\left\{\sum_{\substack{s(e)=v \\
 t(e) \neq V}} \sigma_{\min }\left(A_{v \rightarrow e}\right)^{2}+\sum_{\substack{t(e)=v \\
 s(e) \neq V}} \sigma_{\min }\left(A_{e \leftarrow v}\right)^{2}\right\} \\
& \leq \lambda_{i+k}\left(L_{A}\right)-\min _{v \in V}\left\{\sum_{\substack{s(e)=v \\
 t(e) \neq V}} \sigma_{\min }\left(A_{v \rightarrow e}\right)^{2}+\sum_{\substack{t(e)=v \\
 s(e) \neq V}} \sigma_{\min }\left(A_{e \leftarrow v}\right)^{2}\right\}
\end{aligned}
$$

The first two inequalities are from Theorem B. 4 and the final inequality is due to Theorem B.3. The right inequality is proven similarly.

# APPEndix B. Classical Results on Eigenvalues of Hermitian Matrices 

In the following, for an $n \times n$ Hermitian matrix A, let $\lambda_{1}(A), \ldots, \lambda_{n}(A)$ be the eigenvalues ordered in increasing fashion.

THEOREM B. 1 (Rayleigh, see [18] Theorem 4.2.2). Let $A$ be a Hermitian matrix. Then for integers $1 \leq i_{1}, \ldots, i_{k} \leq n$ let $x_{i_{1}}, \ldots, x_{i_{k}}$ be orthonormal, where $x_{i_{j}}$ is an eigenvector corresponding to $\lambda_{i_{j}}(A)$. Define $S=\operatorname{span}\left\{x_{i_{1}}, \ldots, x_{i_{k}}\right\}$. Then for any $x \in S$

$$
\lambda_{i_{1}}(A) \leq \frac{x^{*} A x}{\|x\|^{2}} \leq \lambda_{i_{k}}(A)
$$

THEOREM B. 2 (Courant-Fischer, see [18] Theorem 4.2.6). Let $A$ be Hermitian matrix. Then

$$
\lambda_{k}(A)=\min _{\operatorname{dim} V=k}\left[\max _{x \in V \backslash 0} \frac{\langle x, A x\rangle}{\langle x, x\rangle}\right]
$$

THEOREM B. 3 (Cauchy's interlacing theorem, see [18] Theorem 4.3.17). Let A be a Hermitian matrix of size $n \times n$ and $B$ an $m \times m$ principal submatrix of A. Then

$$
\lambda_{i}(A) \leq \lambda_{i}(B) \leq \lambda_{i+n-m}(A)
$$

for $i=1, \ldots, m$.




---

ThEOREM B. 4 (Weyl's inequalities, see [18] Theorem 4.3.1). For $A, B$ Hermitian matrices of size $n \times n$ the following inequalities hold:

$$
\begin{aligned}
& \lambda_{i}(A+B) \leq \lambda_{i+j}(A)+\lambda_{n-j}(B) \quad \text { s for } j=0, \ldots, n-1 \text { and } \\
& \lambda_{i}(A+B) \geq \lambda_{i-j+1}(A)+\lambda_{j}(B) \quad \text { for } j=1, \ldots, i
\end{aligned}
$$

THEOREM B. 5 (See [31] Theorem 5). For $H$ a Hermitian matrix of dimension $n$ given in block form as

$$
H=\left[\begin{array}{cc}
A & B^{*} \\
B & D
\end{array}\right]
$$

where $D$ is non-singular let $H / D=A-B D^{-1} B^{*}$ be the Schur complement of $D$. Then the eigenvalues of $H$ and $H / D$ are interlaced:

$$
\lambda_{i}(H) \leq \lambda_{i}(H / D) \leq \lambda_{i+r}(H)
$$

for $i=1, \ldots, n-r$ where $r$ is the rank of $D$.

# REFERENCES 

[1] J. D. Buenrostro, P. G. Giresi, L. C. Zaba, H. Y. Chang, and W. J. Greenleaf. Transposition of native chromatin for fast and sensitive epigenomic profiling of open chromatin, DNA-binding proteins and nucleosome position. Nature methods, 10(12):1213-1218, 2013.
[2] F. R. Chung. The Laplacian of a hypergraph. Expanding graphs, 10:21-36, 1992.
[3] F. R. Chung. Spectral graph theory, volume 92. American Mathematical Soc., 1997.
[4] G. Cooper and K. Adams. The cell: a molecular approach. Oxford University Press, 2022.
[5] J. Curry, R. Ghrist, and V. Nanda. Discrete Morse theory for computing cellular sheaf cohomology. Foundations of Computational Mathematics, 16:875-897, 2016.
[6] J. M. Curry. Sheaves, cosheaves and applications. University of Pennsylvania, 2014.
[7] F. Dorfler and F. Bullo. Synchronization of power networks: Network reduction and effective resistance. IFAC Proceedings Volumes, 43(19):197-202, 2010.
[8] S. Eilenberg and N. Steenrod. Foundations of algebraic topology, volume 2193. Princeton University Press, 2015.
[9] M. Fischer, P. Grossmann, M. Padi, and J. A. DeCaprio. Integration of TP53, DREAM, MMB-FOXM1 and RB-E2F target gene analyses identifies cell cycle gene regulatory networks. Nucleic acids research, $44(13): 6070-6086,2016$.
[10] T. Gao, J. Brodzki, and S. Mukherjee. The geometry of synchronization problems and learning group actions. Discrete \& Computational Geometry, 65(1):150-211, 2021.
[11] R. Ghrist and H. Riess. Cellular sheaves of lattices and the Tarski Laplacian. arXiv preprint arXiv:2007.04099, 2020.
[12] T. E. Goldberg. Combinatorial Laplacians of Simplicial Complexes. Senior thesis, Bard College, 2002.
[13] G. H. Golub and C. F. Van Loan. Matrix Computations. Johns Hopkins Studies in the Mathematical Sciences. Johns Hopkins University Press, 3rd ed edition, 1996.
[14] J. Gu, B. Hua, and S. Liu. Spectral distances on graphs. Discrete Applied Mathematics, 190:56-74, 2015.
[15] I. Guyon, J. Weston, S. Barnhill, and V. Vapnik. Gene selection for cancer classification using support vector machines. Machine learning, 46:389-422, 2002.




---

[16] J. Hansen and R. Ghrist. Toward a Spectral Theory of Cellular Sheaves. Journal of Applied and Computational Topology, 3(4), 2019.
[17] A. N. Hirani. Discrete exterior calculus. California Institute of Technology, 2003.
[18] R. A. Horn and C. R. Johnson. Matrix Analysis. Cambridge University Press, second edition, corrected reprint edition, 2017.
[19] I. T. Jolliffe. Principal Components Analysis, 2nd Ed. Springer, 2002.
[20] C. A. Joslyn, L. Charles, C. DePerno, N. Gould, K. Nowak, B. Praggastis, E. Purvine, M. Robinson, J. Strules, and P. Whitney. A sheaf theoretical approach to uncertainty quantification of heterogeneous geolocation information. Sensors, 20(12):3418, 2020.
[21] C. Lanczos. An iteration method for the solution of the eigenvalue problem of linear differential and integral operators. United States Governm. Press Office Los Angeles, CA, 1950.
[22] R. Lehoucq, K. Maschhoff, D. Sorensen, C. Yang, F. Houssen, S. Ledru, et al. ARPACK-NG: Large scale eigenvalue problem solver. Astrophysics Source Code Library, pages ascl-2306, 2023.
[23] T. Mikolov, K. Chen, G. Corrado, and J. Dean. Efficient estimation of word representations in vector space. arXiv preprint arXiv:1301.3781, 2013.
[24] T. Muller, A. Seigal, and V. Nanda. Multilinear hyperquiver representations. arXiv:2305.05622v2 [math.AG], 2023.
[25] A. Parada-Mayorga, H. Riess, A. Ribeiro, and R. Ghrist. Quiver signal processing (QSP). arXiv preprint arXiv:2010.11525, 2020.
[26] K. Pearson F.R.S. On lines and planes of closest fit to systems of points in space. The London, Edinburgh, and Dublin Philosophical Magazine and Journal of Science, 2(11):559-572, 1901.
[27] C. Rébé and F. Ghiringhelli. STAT3, a master regulator of anti-tumor immune response. Cancers, 11(9):1280, 2019.
[28] A. T. Satpathy, J. M. Granja, K. E. Yost, Y. Qi, F. Meschi, G. P. McDermott, B. N. Olsen, M. R. Mumbach, S. E. Pierce, M. R. Corces, P. Shah, J. C. Bell, D. Jhutty, C. M. Nemec, J. Wang, L. Wang, Y. Yin, P. G. Giresi, A. L. S. Chang, G. X. Y. Zheng, W. J. Greenleaf, and H. Y. Chang. Massively parallel single-cell chromatin landscapes of human immune cell development and intratumoral T cell exhaustion. Nature Biotechnology, 37(8):925-936, 2019.
[29] R. Schiffler. Quiver Representations. Number 184 in CMS Books in Mathematics. Springer, 2014.
[30] A. Seigal, H. A. Harrington, and V. Nanda. Principal components along quiver representations. Foundations of Computational Mathematics, 23(4):1129-1165, 2023.
[31] R. L. Smith. Some interlacing properties of the Schur complement of a Hermitian matrix. Linear Algebra and its Applications, 177:137-144, 1992.
[32] R. Tibshirani. Regression shrinkage and selection via the lasso. Journal of the Royal Statistical Society Series B: Statistical Methodology, 58(1):267-288, 1996.
[33] V. A. Traag, L. Waltman, and N. J. Van Eck. From Louvain to Leiden: guaranteeing well-connected communities. Scientific reports, 9(1):5233, 2019.
[34] J. Van Den Heuvel. Hamilton cycles and eigenvalues of graphs. Linear algebra and its applications, 226:723-730, 1995.
[35] B. Wu, J. Shao, and X. Yuan. Deleting vertices and interlacing Laplacian eigenvalues. Chinese Annals of Mathematics, Series B, 31(2):231-236, 2010.
[36] F. Yan, D. R. Powell, D. J. Curtis, and N. C. Wong. From reads to insight: a hitchhiker's guide to ATAC-seq data analysis. Genome biology, 21:1-16, 2020.
[37] K. Ye and L.-H. Lim. Schubert varieties and distances between subspaces of different dimensions. SIAM Journal on Matrix Analysis and Applications, 37(3):1176-1197, 2016.
[38] J. Yu, D. Sun, Z. Hou, and L.-Y. Wu. Single-cell ATAC-seq analysis via network refinement with peaks location information. bioRxiv, page 2022.11.18.517159, 2022.




---

