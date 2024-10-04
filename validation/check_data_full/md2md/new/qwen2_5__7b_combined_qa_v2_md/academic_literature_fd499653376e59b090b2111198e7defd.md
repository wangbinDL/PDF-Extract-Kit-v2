# A RECURSION FORMULA FOR MIXED TRACE MOMENTS OF ISOTropic WISHART MATRICES AND THE GAUSSIAN UNITARY/ORTHOGONAL ENSEMBLES 

Ben Deitmar<br>Department of Mathematical Stochastics, ALU Freiburg<br>Ernst-Zermelo-Str. 1, 79104 Freiburg, Germany<br>E-mail: ben.deitmar@stochastik.uni-freiburg.de


#### Abstract

Exact recursion formulas for mixed moments of four fundamental random matrix ensembles are derived. The reason such recursive formulas are possible is closely related to properties of polygon gluings studied by Harer and Zagier as well as Akhmedov and Shakirov. The proofs of the formulas are direct and written in such a way that they do not rely on understanding of polygon gluings.


## 1 Introduction

Let $X$ be a $(p \times n)$ random matrix with iid standard normal entries and let $Y$ be a $(p \times n)$ random matrix with iid standard complex normal entries. Further let $Z$ be an $(n \times n)$ random hermitian matrix, where the entries $\left(Z_{i, j}\right)_{i \leq j}$ are independent and $Z_{i, i} \sim \mathcal{N}(0,1)$ for all $i \leq n$ as well as $Z_{i, j}=\overline{Z_{j, i}} \sim \mathcal{C} \mathcal{N}(0,1)$ for all $i<j \leq n$. Similarly, let $\tilde{Z}$ be an $(n \times n)$ random symmetric matrix, where the entries $\left(\tilde{Z}_{i, j}\right)_{i \leq j}$ are independent and $\tilde{Z}_{i, i} \sim \mathcal{N}(0,2)$ for all $i \leq n$ as well as $\tilde{Z}_{i, j}=\tilde{Z}_{j, i} \sim \mathcal{N}(0,1)$ for all $i<j \leq n$.

The matrices $\frac{1}{\sqrt{n}} Z$ and $\frac{1}{\sqrt{n}} \tilde{Z}$ are of the Gaussian unitary and Gaussian orthogonal ensemble respectively. The matrices $\frac{1}{n} X X^{T}$ and $\frac{1}{n} Y Y^{*}$ are real and complex isotropic Wishart matrices.

In this paper we give exact recursive formulas for mixed trace moments of the type

$$
\mathbf{E}^{X}(l):=\mathbf{E}\left[\prod_{k=1}^{K} \operatorname{tr}\left(\left(X X^{T}\right)^{l_{k}}\right)\right], \quad \mathbf{E}^{Y}(l):=\mathbf{E}\left[\prod_{k=1}^{K} \operatorname{tr}\left(\left(Y Y^{*}\right)^{l_{k}}\right)\right]
$$

Supported by the DFG Research Unit 5381



and

$$
\mathbf{E}^{Z}(\underline{l}):=\mathbf{E}\left[\prod_{k=1}^{K} \operatorname{tr}\left(\mathrm{Zl}_{k}\right)\right], \quad \mathbf{E}^{\tilde{\mathrm{Z}}}(\underline{l}):=\mathbf{E}\left[\prod_{k=1}^{K} \operatorname{tr}\left(\tilde{\mathbf{Z}}_{l_{k}}\right)\right]
$$

for arbitrary $p, n, K \in \mathbb{N}$ and layouts $\underline{l}=\left(l_{1}, \ldots, l_{K}\right) \in \mathbb{N}_{0}^{K}$.
Assuming $l_{1}>0$, the formulas are as follows.

# 1) Gaussian unitary ensemble: 

$$
\begin{aligned}
& \mathbf{E}\left[\prod_{r=1}^{K} \operatorname{tr}\left(\mathrm{Zl}_{r}\right)\right] \\
& =\sum_{q=1}^{l_{1}-1} \mathbf{E}\left[\operatorname{tr}\left(\mathrm{Z}_{q-1}\right) \operatorname{tr}\left(\mathrm{Zl}_{l_{1}-q-1}\right) \prod_{r=2}^{K} \operatorname{tr}\left(\mathrm{Z} l_{r}\right)\right] \\
& \quad+\sum_{k=2}^{K} l_{k} \mathbf{E}\left[\operatorname{tr}\left(\mathrm{Zl}_{l_{1}+l_{k}-2}\right) \prod_{\substack{1=1 \\
r \neq k}}^{K} \operatorname{tr}\left(\mathrm{Z} l_{r}\right)\right]
\end{aligned}
$$

For a complete formulation and proof see Theorem 2.1.
2) Gaussian orthogonal ensemble:

$$
\begin{aligned}
\mathbf{E} & {\left[\prod_{r=1}^{K} \operatorname{tr}\left(\tilde{\mathbf{Z}}_{l_{r}}\right)\right] } \\
= & \left(l_{1}-1\right) \mathbf{E}\left[\operatorname{tr}\left(\tilde{\mathbf{Z}}_{l_{1}-2}\right) \prod_{r=2}^{K} \operatorname{tr}\left(\tilde{\mathbf{Z}}_{l_{r}}\right)\right] \\
& +\sum_{q=1}^{l_{1}-1} \mathbf{E}\left[\operatorname{tr}\left(\tilde{\mathbf{Z}}_{q-1}\right) \operatorname{tr}\left(\tilde{\mathbf{Z}}_{l_{1}-q-1}\right) \prod_{r=2}^{K} \operatorname{tr}\left(\tilde{\mathbf{Z}}_{l_{r}}\right)\right] \\
& +2 \sum_{k=2}^{K} l_{k} \mathbf{E}\left[\operatorname{tr}\left(\tilde{\mathbf{Z}}_{l_{1}+l_{k}-2}\right) \prod_{\substack{r=1 \\
r \neq k}}^{K} \operatorname{tr}\left(\tilde{\mathbf{Z}} l_{r}\right)\right]
\end{aligned}
$$

For a complete formulation and proof see Theorem 4.1.
3) Complex isotropic Wishart ensemble:

$$
\begin{aligned}
\mathbf{E} & {\left[\prod_{r=1}^{K} \operatorname{tr}\left(\left(\mathbf{Y} \mathbf{Y}^{*}\right)_{l_{r}}\right)\right] } \\
= & n \mathbf{E}\left[\operatorname{tr}\left(\left(\mathrm{YY}^{*}\right)_{l_{1}-1}\right) \prod_{r=2}^{K} \operatorname{tr}\left(\left(\mathbf{Y} \mathbf{Y}^{*}\right)_{l_{r}}\right)\right] \\
& +\sum_{q=1}^{l_{1}-1} \mathbf{E}\left[\operatorname{tr}\left(\left(\mathbf{Y} \mathbf{Y}^{*}\right)_{q}\right) \operatorname{tr}\left(\left(\mathbf{Y} \mathbf{Y}^{*}\right)_{l_{1}-q-1}\right) \prod_{r=2}^{K} \operatorname{tr}\left(\left(\mathbf{Y} \mathbf{Y}^{*}\right)_{l_{r}}\right)\right] \\
& +\sum_{k=2}^{K} l_{k} \mathbf{E}\left[\operatorname{tr}\left(\left(\mathrm{YY}^{*}\right)_{l_{1}+l_{k}-1}\right) \prod_{\substack{r=1 \\
r \neq k}}^{K} \operatorname{tr}\left(\left(\mathbf{Y} \mathbf{Y}^{*}\right)_{l_{r}}\right)\right]
\end{aligned}
$$

For a complete formulation and proof see Theorem 3.1.



4) Real isotropic Wishart ensemble:

$$
\begin{aligned}
\mathbb{E}\left[\prod_{r=1}^{K} \operatorname{tr}\left(\left(\boldsymbol{X} \boldsymbol{X}^{T}\right)^{l_{r}}\right)\right]= & \left(n+l_{1}-1\right) \mathbb{E}\left[\operatorname{tr}\left(\left(\boldsymbol{X} \boldsymbol{X}^{T}\right)^{l_{1}-1}\right) \prod_{r=2}^{K} \operatorname{tr}\left(\left(\boldsymbol{X} \boldsymbol{X}^{T}\right)^{l_{r}}\right)\right] \\
& +\sum_{q=1}^{l_{1}-1} \mathbb{E}\left[\operatorname{tr}\left(\left(\boldsymbol{X} \boldsymbol{X}^{T}\right)^{q}\right) \operatorname{tr}\left(\left(\boldsymbol{X} \boldsymbol{X}^{T}\right)^{l_{1}-q-1}\right) \prod_{r=2}^{K} \operatorname{tr}\left(\left(\boldsymbol{X} \boldsymbol{X}^{T}\right)^{l_{r}}\right)\right] \\
& +2 \sum_{k=2}^{K} l_{k} \mathbb{E}\left[\operatorname{tr}\left(\left(\boldsymbol{X} \boldsymbol{X}^{T}\right)^{l_{1}+l_{k}-1}\right) \prod_{\substack{r=1 \\
r \neq k}}^{K} \operatorname{tr}\left(\left(\boldsymbol{X} \boldsymbol{X}^{T}\right)^{l_{r}}\right)\right]
\end{aligned}
$$

For a complete formulation and proof see Theorem 3.2.
The recursive formulas are proved in order of increasing difficulty, so Theorem 2.1 proves (1), Theorem 3.1 proves (3), Theorem 3.2 proves (4) and Theorem 4.1 proves (2).

The only random matrix ensembles for which explicit and non-recursive formulas for mixed moments are known are the Haar unitary and the Haar orthogonal ensembles. Diaconis and Evans found the explicit formulas in [4] under an assumption roughly equivalent to $n \geq l_{1}+\ldots+l_{K}$. Achieving non-recursive formulas for the ensembles studied here would prove extremely useful in the study of their spectral properties. For example the asymptotic behavior of

$$
\mathbb{E}\left[\operatorname{tr}\left(\boldsymbol{Z}^{\left\lfloor\frac{t_{1} n}{2}\right\rfloor}\right) \cdots \operatorname{tr}\left(\boldsymbol{Z}^{\left\lfloor\frac{t_{K} n}{2}\right\rfloor}\right)\right]
$$

is known to determine the behavior of the largest eigenvalue of $\boldsymbol{Z}$ at the Tracy-Widom scale, which is why such mixed trace moments were already extensively studied in [10], [12], [13], [14] and [15]. The strong universality results therein imply that a non-recursive result in any of the four cases studied here would already yield a greater understanding of Tracy-Widom laws in much more general settings. The fact that Akhmedov and Shakirov were able to find a non-recursive formula to a similar, but still different recursion in [1] suggests that non-recursive solutions may be achievable.

Explicit formulas for the (non-mixed) singular trace moments $\mathbb{E}\left[\operatorname{tr}\left(\boldsymbol{Z}^{2 m}\right)\right]$ as well as $\mathbb{E}\left[\operatorname{tr}\left(\left(\boldsymbol{X} \boldsymbol{X}^{T}\right)^{m}\right)\right]$ and $\mathbb{E}\left[\operatorname{tr}\left(\left(\boldsymbol{Y} \boldsymbol{Y}^{*}\right)^{m}\right)\right]$ are known thanks to Haarer-Zagier in [6] and E. Vassilieva in [16]. The formula in the GUE case is not written explicitly in [6], but following their work we give the formula in (1.2). The formulas for the real and complex Wishart case can be found in Corollaries 1.8 and 1.9 of [16]. For the singular trace moments in the GOE case $\mathbb{E}\left[\operatorname{tr}\left(\tilde{\boldsymbol{Z}}^{2 m}\right)\right]$ a five-term recurrence relation is known thanks to M. Ledoux in [9].

The recursion from Theorem 2.1 for the GUE is not new, as it also follows from Section 5 in [6] by Harer and Zagier. We however still prove it as a precursor to Theorems 3.1, 3.2 and 4.1. The real Wishart case from Theorem 3.2 was already studied by Pielaszkiewicz,



Von Rosen and Singull in [11], though they made a minor error in their formula. To the best of our knowledge the results of Theorems 3.1 and 4.1 for the complex Wishart ensemble and the GOE respectively are entirely new.

# 1.1 Trace moments and polygon gluings 

There is a well-known link between trace moments of the GUE and the number of ways to glue to edges of a polygon together to receive an orientable surface of a given genus. This link was first described by Harer and Zagier in [6] to prove the recursive formula

$$
(m+1) \mathrm{E}\left[\operatorname{tr}\left(\mathbf{Z}^{2 m}\right)\right]=(4 m-2) n \mathrm{E}\left[\operatorname{tr}\left(\mathbf{Z}^{2 m-2}\right)\right]+(m-1)(2 m-1)(2 m-3) \mathrm{E}\left[\operatorname{tr}\left(\mathbf{Z}^{2 m-4}\right)\right]
$$

which allows for the explicit representation

$$
\mathrm{E}\left[\operatorname{tr}\left(\mathbf{Z}^{2 m}\right)\right]=\frac{(2 m)!}{m!} \sum_{r=1}^{n \wedge(m+1)}\binom{n}{r}\binom{m}{r-1} 2^{m+1-r}
$$

These equalities were first found by Harer and Zagier and later simplified by Haagerup and Thorbjørnsen in [5], but the more readable formulation for (1.1) is from Theorem 1 in [9] by M. Ledoux, where he goes on to find an analogous recursion formula for $\mathrm{E}\left[\operatorname{tr}\left(\tilde{\mathbf{Z}}^{2 m}\right)\right]$ in the GOE case.

Akhmedov and Shakirov took this approach further in [1] by considering 'incomplete' gluings of a polygon such that the unglued edges form polygons of given lengths $\left(l_{1}, \ldots, l_{K}\right)$. They were able to give a recursive formula for the number of such incomplete gluings with a given genus (for a certain definition of genus). Unfortunately, although they were able to derive the explicit expression from their recursive formula, their results do not seem applicable to random matrix theory and their solution to a similar recursion does not seem applicable for solving the recursive formulas derived in this article.

In order to find formulas for mixed trace moments of the GUE for a layout $\boldsymbol{l}=\left(l_{1}, \ldots, l_{K}\right)$, one instead would need to count the number of ways to glue the edges of multiple polygons $P_{l_{1}}, \ldots, P_{l_{K}}$ such that the resulting oriented surface is of a given genus. Here a possible pairing $\pi=\left\{\left\{e_{1}^{1}, e_{5}^{1}\right\},\left\{e_{2}^{1}, e_{1}^{2}\right\}, \ldots\right\}$ of edges for the gluing of $P_{8}, P_{5}, \ldots, P_{6}$ :





Euler's characteristic formula guarantees

$$
2-2 g=V-L / 2+K
$$

where $g$ is the genus of the resultant surface and $V$ is the number of vertices remaining in the ribbon graph determined by the pairing. Define $V_{L, K}(g)=2-2 g+\frac{L}{2}-K$ and

$$
g_{L, K}(V)=\frac{L}{4}+\frac{1-V+K}{2}
$$

Let $\varepsilon_{g}\left(l_{1}, \ldots, l_{K}\right)$ denote the number of different gluings/pairings of polygons $P_{l_{1}}, \ldots, P_{l_{K}}$ such that the resulting orientable surface is of genus $g$, then it is provable by Wick's Theorem (aka. Isserlis' Theorem) that

$$
E Z(\mathbf{l})=\sum_{g=0}^{\left\lfloor g_{L, K}(0)\right\rfloor} v_{L, K}(g) \varepsilon_{g}\left(l_{1}, \ldots, l_{K}\right)
$$

under the assumption $l_{1}, \ldots, l_{K}>0$.
A recursion formula for $E Z(\mathbf{l})$ can then be found by mapping such polygon gluings onto gluings of polygons with two less total edges. If the edge $e_{q}^{k}$ paired with $e_{1}^{1}$ is still part of the same polygon, i.e. $k=1$, then we can contract along the connection of the edges before removing both such that we are left with a gluing of polygons $P_{q-2}, P_{l_{1}-q}, P_{l_{2}}, \ldots, P_{l_{k}}$. Here a picture of what the above pairing would look like after removing $e_{1}^{1}$ and its paired edge $e_{5}^{1}$ :


The edges would of course have to be renamed and we have swapped the positions of the first two polygons such that the effects of contracting along the connection $\left\{e_{1}^{1}, e_{5}^{1}\right\}$ are more obvious.

Similarly, when the edge $e_{q}^{k}$ paired with $e_{1}^{1}$ is not in the first polygon, i.e. $k>1$, contraction along the pairing and removal of the two edges creates one new polygon $P_{l_{1}+l_{k}-2}$ from the two polygons $P_{l_{1}}$ and $P_{l_{k}}$. The rest of the pairing remains a valid gluing for the polygons $P_{l_{1}+l_{k}-2}, P_{2}, \ldots, \widehat{P}_{l_{k}}, \ldots, P_{l_{K}}$. Here an example before the contraction



and removal:



This method of removing edges does not remove vertices of the ribbon graph, while it can happen that some of the new polygons are empty (i.e. they have length $l_{k}=0$ ). This only becomes a problem, if the first polygon is empty, since then there is no edge $e_{1}^{1}$ to use for the next recursive step of contraction and removal. We thus discard the first polygon, if it is empty. As this also constitutes a removal of an isolated vertex from the ribbon graph, we must keep a tally of how many vertices were removed this way. Luckily, in the recursive formula this tally is simply realized with an additional factor $n$.

We have thus far heuristically argued the plausibility of Theorem 2.1.

# 1.2 Definition (Multigraphs by route) 

For a vertex set $V=[n]=\{1, \ldots, n\}$ and a give route $i^{1} \in[n]^{m}$ we define the directed multi-graph $G_{i^{1}}=(V, E, f)$, with edge set $E=\left(e_{1}^{1}, \ldots, e_{m}^{1}\right)$ and

$$
f: E \rightarrow V \times V \quad ; \quad e_{q}^{1} \mapsto\left(i_{q}^{1}, i_{(q \bmod m)+1}^{1}\right)
$$

By construction the route $i^{1}$ is an Euler path on $G_{i^{1}}$. Let $A\left(G_{i^{1}}\right) \in \mathbb{N}_{0}^{n \times n}$ denote the adjacency matrix of $G_{i^{1}}$, that is

$$
A_{v, w}\left(G_{i^{1}}\right)=\#\left\{e_{q}^{1} \in E \mid f\left(e_{q}^{1}\right)=(v, w)\right\}
$$

We can also define the undirected multi-graph $\tilde{G}_{i^{1}}=(V, E, \tilde{f})$ to a given route $i^{1} \in[n]^{m}$ with the same edges, but ignorant of the edges direction. In this case we can define $\tilde{f}$ by

$$
\tilde{f}: E \rightarrow\{\mathcal{M} \subset V \mid \# \mathcal{M} \leq 2\} ; \quad e_{q}^{1} \mapsto\left\{i_{q}^{1}, i_{(q \bmod m)+1}^{1}\right\}
$$



(If $\# f\left(e_{q}^{1}\right)=1$, the edge $e_{q}^{1}$ is a self-loop.) Again $A\left(\tilde{G}_{i_{1}}\right) \in \mathbb{N}_{0}^{n \times n}$ denotes the adjacency matrix of $\tilde{G}_{i_{1}}$, i.e.

$$
A_{v, w}\left(\tilde{G}_{i_{1}}\right)=\#\left\{e_{q}^{1} \in E \mid f\left(e_{q}^{1}\right)=\{v, w\}\right\}
$$

Note that for this definition of the adjacency matrix self-loops are only counted once. For a sequence of routes $i=\left(i_{1}, \ldots, i_{K}\right) \in \underset{k=1}{\times}[n]^{l_{k}}$ define the joined adjacency matrices

$$
A(i):=\sum_{k=1}^{K} A\left(G_{i_{k}}\right) ; \quad \tilde{A}(i):=\sum_{k=1}^{K} A\left(\tilde{G}_{i_{k}}\right)
$$

In Section 3 the vertex set $V$ will be $[p+n]$, so we must exchange all above occurrences of $n$ with $p+n$.

# 2 Gaussian Unitary Ensemble 

2.1 Theorem (Recursion for mixed trace moments of the GUE) For $K \in \mathbb{N}$ and any $\mathbf{l}=\left(l_{1}, \ldots, l_{K}\right) \in \mathbb{N}_{0}^{K}$ - with even $L:=l_{1}+\ldots+l_{K}$ - the following recursive properties hold.
a) If $l_{1}=0$, then $\mathbb{E} Z^{(\mathbf{l})}=n \mathbb{E} Z^{\left(S_{0}(\mathbf{l})\right)}$ for

$$
S_{0}\left(0, l_{2}, \ldots, l_{K}\right):=\left(l_{2}, \ldots, l_{K}\right)
$$

b) If $l_{1}>0$, then

$$
\mathbb{E} Z^{(\mathbf{l})}=\sum_{q=1}^{l_{1}-1} \mathbb{E} Z^{\left(S_{2, q}(\mathbf{l})\right)}+\sum_{k=2}^{K} l_{k} \mathbb{E} Z^{\left(S_{3, k}(\mathbf{l})\right)}
$$

where

$$
\begin{aligned}
& S_{2, q}(\mathbf{l}):=\left(q-1, l_{1}-q-1, l_{2}, \ldots, l_{K}\right) \\
& S_{3, k}(\mathbf{l}):=\left(l_{1}+l_{k}-2, l_{2}, \ldots, \widehat{l_{k}}, \ldots, l_{K}\right)
\end{aligned}
$$

Since (a) reduces $K$ by one and (b) reduces $L=l_{1}+\ldots+l_{K}$ by two, the starting point

$$
\mathbb{E} Z^{((),)}=\mathbb{E}\left[\operatorname{tr}(Z)^{0}\right]=n
$$

for $(K, L)=(1,0)$ allows for the calculation of all mixed moments, when $L$ is even. When $L$ is odd, it is easy to see that the mixed trace moment must be zero.



Proof. The property (a) holds trivially, since the empty matrix product is here the $(n \times n)$ identity matrix. It remains to prove property (b).

For now assume $l_{1}, \ldots, l_{K}>0$, then expanding the sums in $\operatorname{tr}\left(Z^{l_{i}}\right)$ yields

$$
\mathbb{E} Z^{(\mathbf{l})}=\sum_{\subsup{i_{1}}{}{i_{K} \in[n]^{K}} \in[n]^{l_{1}}} \mathbb{E}\left[\prod_{k=1}^{K} Z_{1, i_{2}^{k}}^{i_{k}} \cdots Z_{l_{k-1,}, i_{l k}^{k}}^{i_{k}} Z_{l_{k}, 1}^{i_{k}}\right]
$$

Extracting the first entries of each $i_{k}$ and summing over them first gives

$$
\mathbb{E} Z^{(\mathbf{l})}=\sum_{b_{1}, \ldots, b_{K} \in[n]} \sum_{\substack{i \in \underset{k=1}{K}[n]^{l_{k}} \\ \forall k \leq K: i_{1}^{k}=b_{k}}} \mathbb{E}\left[\prod_{k=1}^{K} Z_{1, i_{2}^{k}}^{i_{k}} \cdots Z_{l_{k-1},, i_{l}^{k}}^{i_{k}} Z_{l_{k}, 1}^{i_{k}}\right] .
$$

For easier notation define

$$
\mathcal{I}_{\mathbf{l}, \mathbf{b}}:=\left\{i=\left(i_{1}, \ldots, i_{K}\right) \in \underset{k=1}{K}[n]^{l_{k}} \mid \forall k \leq K:\left(l_{k}>0 \Rightarrow i_{1}^{k}=b_{k}\right)\right\}
$$

then the above formula can be written as

$$
\mathbb{E} Z^{(\mathbf{l})}=\sum_{b_{1}, \ldots, b_{K} \in[n]} \sum_{i \in \mathcal{I}_{\mathbf{l}, \mathbf{b}}} \mathbb{E}\left[\prod_{k=1}^{K} Z_{1, i_{2}^{k}}^{i_{k}} \cdots Z_{l_{k-1},, i_{l}^{k}}^{i_{k}} Z_{l_{k}, 1}^{i_{k}}\right]
$$

The formula now also holds when some $l_{i}$ are zero, since then the summation over the corresponding $b_{i}$ brings the needed factors $n=\operatorname{tr}\left(Z^{0}\right)$.

Since complex standard normal random variables satisfy $\mathbb{E}\left[X_{a} \bar{X}_{b}\right]=\delta_{a=b} a$ ! and real standard normal random variables satisfy $\mathbb{E}\left[X_{a}\right]=\delta_{a \text { even }}(a-1)!!$ (with the convention $(-1)!!=1$ ), the mean in (2.4) has the form

$$
\begin{array}{r}
\mathbb{E}\left[\prod_{k=1}^{K} Z_{1, i_{2}^{k}}^{i_{k}} \cdots Z_{l_{k-1},, i_{l}^{k}}^{i_{k}} \bar{Z}_{l_{k}, 1}^{i_{k}}\right] \\
=\mathbb{1}_{\text { diag. entries even }}(A(i))\left(\prod_{\substack{v, w \in[n] \\
v<w}} \mathbb{A}_{v, w}(i)!\right)\left(\prod_{v \in[n]}\left(\mathbb{A}_{v, v}(i)-1\right)!!\right) \\
=: W(A(i))
\end{array}
$$

where $A(i):=\sum_{k=1}^{K} \mathcal{A}\left(G^{i_{k}}\right)$. Let $c:=i_{1}^{l_{1}}$ - here the assumption $l_{1}>0$ is needed - and define the symmetric matrix

$$
M_{b, c}:=\left(\mathbb{1}_{i=b, j=c}+\mathbb{1}_{i=c, j=b}\right)_{i, j \in[n]}
$$



For $c \neq b_{1}$, the above definition of $W\left(\overline{\mathbf{A}}^{(i)}\right)$ then yields

$$
\begin{aligned}
W\left(\overline{\mathbf{A}}^{(i)}\right) & =W\left(\overline{\mathbf{A}}^{(i)}\right)-M_{b_{1}, c}) \overline{A^{c, b_{1}}}(i) \\
& =W\left(\overline{\mathbf{A}}^{(i)}-M_{b_{1}, c}\right)\left(\overline{A^{c, b_{1}}}\left(G_{i_{1}}\right)+\sum_{s=2}^{K} \overline{A^{c, b_{1}}}\left(G_{i_{s}}\right)\right)
\end{aligned}
$$

where $\overline{A^{c, b_{1}}}(i)$ is at least 1 , since it counts the number of occurrences of the connection $\left(i_{l_{1}}^{1}, i_{1}^{1}\right)=\left(c, b_{1}\right)$. The fact that $W(\overline{\mathbf{A}})$ is zero as soon as $\overline{\mathbf{A}}$ is not symmetric, allows us to swap $b_{1}$ and $c$ in arbitrary places of the formula, so we may also write

$$
\begin{aligned}
& W\left(\overline{\mathbf{A}}^{(i)}\right)=W\left(\overline{\mathbf{A}}^{(i)}-M_{b_{1}, c}\right)\left(\overline{A^{b_{1}, c}}\left(G_{i_{1}}\right)+\sum_{s=2}^{K} \overline{A^{b_{1}, c}}\left(G_{i_{s}}\right)\right) .
\end{aligned}
$$



Similarly, when $c=b_{1}$, the weight satisfies

$$
\begin{aligned}
& W\left(\overline{\mathbf{A}}^{(i)}\right)=W\left(\overline{\mathbf{A}}^{(i)}-M_{b_{1}, b_{1}}\right)\left(\overline{A^{b_{1}, b_{1}}}(i)-1\right) \\
& =W\left(\overline{\mathbf{A}}^{(i)}-M_{b_{1}, b_{1}}\right)\left(\overline{A^{b_{1}, b_{1}}}\left(G_{i_{1}}\right)-1+\sum_{s=2}^{K} \overline{A^{b_{1}, b_{1}}}\left(G_{i_{s}}\right)\right)
\end{aligned}
$$

and we can use these properties of the weight to decompose equality (2.4) into



For $E_{Z}^{1}(l)$ observe that $\overline{A^{b_{1}, c}}\left(G_{i_{1}}\right)$ counts the number of occurrences of $\left(b_{1}, c\right)$ in $i_{1}=$ $\left(i_{1}^{1}, \ldots, i_{l_{1}}^{1}\right)$ and, if this number is $\mathbf{1}_{b_{1}=c}$, such an $i$ will not contribute to $E_{Z}^{1}(l)$. Define

$$
Q_{b, c}^{1}\left(i_{1}\right)=\left\{q<l_{1} \mid i_{q}^{1}=b, i_{q+1}^{1}=c\right\}
$$

then $\overline{A^{b_{1}, c}}\left(G_{i_{1}}\right)-\mathbf{1}_{b_{1}=c}=\# Q_{b_{1}, c}^{1}\left(i_{1}\right)$. For each $q \in Q_{b_{1}, c}^{1}\left(i_{1}\right)$ we give a unique way of splitting up $i_{1}$ into two new routes $\left\langle i_{1}\right\rangle_{q, 1}$ and $\left\langle i_{1}\right\rangle_{q, 2}$. Define

$$
\left\langle i_{1}\right\rangle_{q, 1}:=\underbrace{\left(i_{1}^{1}, \ldots, i_{q-1}^{1}\right)}_{=b_{1}} \in[n]^{q-1} ;\left\langle i_{1}\right\rangle_{q, 2}:=\underbrace{\left(i_{q+2}^{1}, \ldots, i_{l_{1}}^{1}\right)}_{=c} \in[n]^{l_{1}-q-1}
$$

and observe that when going from the multi-graph $G_{i_{1}}$ to $G_{\left\langle i_{1}\right\rangle_{q, 1}} \cup G_{\left\langle i_{1}\right\rangle_{q, 1}}$ we have only lost one edge in each direction (two edges without direction in the case of $b_{1}=c$ ) between the vertices $b_{1}$ and $c$ while all other edges remain. For

$$
J_{q}^{1}(i):=\left(\left\langle i_{1}\right\rangle_{q, 1},\left\langle i_{1}\right\rangle_{q, 2}, i_{2}, \ldots, i_{K}\right)
$$



it follows that

$$
A\left(J_{q}^{1}(\mathbf{i})\right)=A(\mathbf{i})-M_{\mathbf{b}_{1}, c}
$$

Since we sum over all choices of $c$ and all the other elements in $\mathbf{i}_{1}$, which were not specified can still be chosen freely, this for $E_{l}^{1}$ implies

$$
\begin{aligned}
E_{Z}^{1}(\mathbf{l}) & =\sum_{\substack{\mathbf{b} \in[n]^{K} \\
c \in[n]}} \sum_{\substack{\mathbf{i} \in I_{l, \mathbf{b}} \\
\mathbf{i}_{1}}} \sum_{\substack{J_{q}^{1}(\mathbf{i}) \\
c}} W(A(J_{q}^{1}(\mathbf{i}))) \\
& =\sum_{q=1}^{l_{l}-1} \sum_{\substack{\mathbf{b} \in[n]^{K} \\
c \in[n]}} \underset{\substack{\mathbf{i}_{1} \\
\mathbf{i}_{1} \in I_{l, \mathbf{b}}}} \sum_{\substack{\mathbf{i} \in I_{l, \mathbf{b}}} Q_{b_{1}, c}^{1}(\mathbf{i}_{1})} W(A(J_{q}^{1}(\mathbf{i}))) \\
& =\sum_{q=1}^{l_{l}-1} \sum_{\tilde{\mathrm{b}} \in[n]^{K+1}} \sum_{\mathbf{i} \in I_{S_{2}, q(\mathbf{l}), \tilde{\mathbf{b}}}} W(A(\mathbf{i}))
\end{aligned}
$$

where

$$
S_{2}, q(\mathbf{l}):=\left(q-1, l_{1}-q-1, l_{2}, \ldots, l_{K}\right)
$$

is defined in analogy to $J_{q}^{1}(\mathbf{i})$. We have thus shown

$$
E_{Z}^{1}(\mathbf{l})=\sum_{q=1}^{l_{1}-1} E_{Z}\left(S_{2}, q(\mathbf{l})\right)
$$

Next, for $E_{Z}^{2}(\mathbf{l})$ observe that $\sum_{k=2}^{K} A_{\mathbf{b}_{1}, c}\left(G_{i_{k}}\right)$ counts the number of occurrences of $\left(\mathbf{b}_{1}, c\right)$ in

$$
\left(i_{1}^{2}, \ldots, i_{l_{2}}^{2}\right), \cdots,\left(i_{1}^{K}, \ldots, i_{l_{K}}^{K}\right)
$$

and define the set

$$
Q_{b, c}^{2}(\mathbf{i}):=\left\{(k, q) \in\{2, \ldots, K\} \times \mathbb{N} \mid q \leq l_{k}\right. \text { and } \left.q<l_{k} \Rightarrow\left(i_{q}^{k}=b \wedge i_{q+1}^{k}=c\right), q=l_{k} \Rightarrow\left(i_{l_{k}}^{k}=b \wedge i_{1}^{k}=c\right)\right\}
$$

Again $\sum_{k=2}^{K} A_{\mathbf{b}_{1}, c}\left(G_{i_{k}}\right)=\# Q_{b_{1}, c}^{2}(\mathbf{i})$ and this time for each $(k, q) \in Q_{b_{1}, c}^{2}(\mathbf{i})$ we give a unique way of joining the routes $\mathbf{i}_{1}$ and $\mathbf{i}_{k}$ into a new route

$$
\left\langle\mathbf{i}_{1}, \mathbf{i}_{k}\right\rangle_{q}:= \begin{cases}\left(\underbrace{i_{1}^{1}}_{=b_{1}}, \ldots, \underbrace{i_{l_{1}}^{1}}_{=c}, i_{q+2}^{k}, \ldots, i_{l_{k}}^{k}, \underbrace{i_{1}^{k}}_{=b_{k}}, \ldots, \underbrace{i_{q-1}^{k}}_{=b_{k}}\right) \in[n]^{l_{1}+l_{s}-1}, & \text { if } q<l_{k} \\ \left(\underbrace{i_{1}^{1}}_{=b_{1}}, \ldots, \underbrace{i_{l_{1}}^{1}}_{=c}, i_{2}^{k}, \ldots, i_{l_{k}-1}^{k}\right) \in[n]^{l_{1}+l_{s}-1}, & \text { if } q=l_{k}\end{cases}
$$



Going from the multigraph $G_{i_{1}} \cup G_{i_{k}}$ to $G_{\left\langle i_{1}, i_{k}\right\rangle q}$ we only loose one edge in each direction between the vertices $b_{1}$ and $c$ (two undirected edges in the case $b_{1}=c$ ) while all other edges remain. For

$$
J_{(k, q)}^{2}(i):=\left(\left\langle i_{1}, i_{k}\right\rangle q, i_{2} \ldots, \widehat{i}_{k}, \ldots, i_{K}\right)
$$

it follows that

$$
A\left(J_{(k, q)}^{2}(i)\right)=A(i)-M_{b_{1}, c}
$$

and similarly to (2.10) we get

$$
\begin{aligned}
\mathcal{E}_{2} Z(l) & =\sum_{\substack{b \in[n]^{K} \\
c \in[n]}} \sum_{\substack{i \in I_{l, b} \\
i_{1} l_{1}=c}} \sum_{\substack{(k, q) \in \mathcal{Q}_{2} \\
b_{1}, c}} A\left(J_{(k, q)}^{2}(i)\right) \\
& =\sum_{k=2}^{K} \sum_{q=1}^{l_{k}} \sum_{\substack{b \in[n]^{K} \\
c \in[n]}} \sum_{\substack{i \in I_{l, b} \\\left.i_{1} l_{1}=c\right) \\
(k, q) \in \mathcal{Q}_{b_{1}, c}^{2}}} A\left(J_{(k, q)}^{2}(i)\right) \\
& =\sum_{k=2}^{K} \sum_{r=1}^{l_{k}} \sum_{\tilde{b} \in[p]^{K-1}} \sum_{i \in I_{S_{3, k}(l), \tilde{b}}} A(i) \\
& =\sum_{k=2}^{K} \sum_{r=1}^{l_{k}} \mathbb{E} Z\left(S_{3, k}(l)\right)=\sum_{k=2}^{K} l_{k} \mathbb{E} Z\left(S_{3, k}(l)\right)
\end{aligned}
$$

where

$$
S_{3, k}(l):=\left(l_{1}+l_{k}-2, l_{2}, \ldots, \widehat{l}_{k}, \ldots, l_{K}\right)
$$

is defined in analogy to $J_{(k, q)}^{2}$.
Equalities (2.7), (2.11) and (2.14) together show

$$
\mathbb{E} Z(l)=\sum_{q=1}^{l_{1}-1} \mathbb{E} Z\left(S_{2, q}(l)\right)+\sum_{k=2}^{K} l_{k} \mathbb{E} Z\left(S_{3, k}(l)\right)
$$

# 2.2 Remark (Translation to polygon gluings) 

In terms of $\varepsilon_{g}(l)$ from (1.3) the recursion can be written as

$$
\sum_{g=0}^{\left\lfloor G_{L, K}(0)\right\rfloor} n^{V_{L, K}(g)} \varepsilon_{g}(l)
$$



$$
=\sum_{q=1}^{l_{1}-1} \sum_{g=0}^{\left\lfloor{ }^{L-2, K+1}(0)\right\rfloor} n^{\mathbf{V}_{L-2, K+1}}(g) \varepsilon_{g}\left(S_{2, q}(\mathbf{l})\right)+\sum_{k=2}^{K} l_{k} \sum_{g=0}^{\left\lfloor{ }^{L-2, K-1}(0)\right\rfloor} n^{\mathbf{V}_{L-2, K-1}}(g) \varepsilon_{g}\left(S_{3, k}(\mathbf{l})\right) .
$$

With

$$
\mathbf{V}_{L, K}(g)=2-2 g+\frac{L}{2}-K=\mathbf{V}_{L-2, K+1}(g)=\mathbf{V}_{L-2, K-1}(g-1)
$$

it implies

$$
\varepsilon_{g}(\mathbf{l})=\sum_{q=1}^{l_{1}-1} \varepsilon_{g}\left(S_{2, q}(\mathbf{l})\right)+\sum_{k=2}^{K} l_{k} \varepsilon_{g-1}\left(S_{3, k}(\mathbf{l})\right)
$$

when $l_{1}>0$, and $\varepsilon_{g}\left(0, l_{2}, \ldots, l_{K}\right)=\varepsilon_{g}\left(l_{2}, \ldots, l_{K}\right)$ otherwise.

# 3 Wishart Ensemble 

For ease of notation in the following proofs we write the matrices $\boldsymbol{X}$ and $\boldsymbol{Y}$ as

$$
\boldsymbol{X}=: \quad\left(X_{i, j}\right)_{i \in[p], j \in[p+n] \backslash[p]} \quad \text { and } Y=: \quad\left(Y_{i, j}\right)_{i \in[p], j \in[p+n] \backslash[p]}
$$

3.1 Theorem (Recursion for mixed trace moments of complex isotropic Wishart matrices)
For $K \in \mathbb{N}$ and any $\mathbf{l}=\left(l_{1}, \ldots, l_{K}\right) \in \mathbb{N}_{0}^{K}$ the following recursive properties hold.
a) If $l_{1}=0$, then $\mathbb{E} Y^{(\mathbf{l})}=p \mathbb{E} Y^{\left(S_{0}(\mathbf{l})\right)}$ for

$$
S_{0}\left(0, l_{2}, \ldots, l_{K}\right):=\left(l_{2}, \ldots, l_{K}\right)
$$

b) If $l_{1}>0$, then

$$
\mathbb{E} Y^{(\mathbf{l})}=n \mathbb{E} Y^{\left(S_{1}(\mathbf{l})\right)}+\sum_{r=1}^{l_{1}-1} \mathbb{E} Y^{\left(S_{2, r}(\mathbf{l})\right)}+\sum_{k=2}^{K} l_{k} \mathbb{E} Y^{\left(S_{3, l_{k}}(\mathbf{l})\right)}
$$

where

$$
\begin{aligned}
S_{1}(\mathbf{l}) & :=\left(l_{1}-1, l_{2}, \ldots, l_{K}\right) \\
S_{2, r}(\mathbf{l}) & :=\left(r, l_{1}-r-1, l_{2}, \ldots, l_{K}\right) \\
S_{3, k, q}(\mathbf{l}) & :=\left(l_{1}+l_{k}-1, l_{2}, \ldots, \widehat{l_{k}}, \ldots, l_{K}\right) .
\end{aligned}
$$

Since (a) reduces $K$ by one and (b) reduces $L:=\sum_{k=1}^{K} l_{k}$ by one, the end point

$$
\mathbb{E} Y^{((,))}=\mathbb{E}\left[\operatorname{tr}\left(\left(\boldsymbol{Y} \boldsymbol{Y}^{*}\right)^{0}\right)\right]=p
$$

for $(K, L)=(1,0)$ allows for the calculation of all mixed moments.



Proof. The property (a) holds trivially, since the empty matrix product is here the $(p \times p)$ identity matrix. The proof of property (b) will take most of the section.

For now assume $l_{1}, \ldots, l_{K}>0$, then by expanding the sums in $\operatorname{tr}\left(S_{l_{i}}\right)$ we see

$$
\mathbb{E} Y^{(l)}=\sum_{\substack{\mathbf{i}_{1} \in B_{p, n, l_{1}} \backslash \% \\ \mathbf{i}_{K} \in B_{p, n, l_{K}}}} \mathbb{E}\left[\prod_{k=1}^{K}\left(Y_{i_{1}^{k} i_{2}^{k}, i_{2}^{k} i_{3}^{k}}\right) \cdots\left(Y_{i_{2 l_{k}-1}^{k} i_{2 l_{k}}^{k}, i_{2 l_{k}}^{k} i_{2}^{k}}\right)\right]
$$

where

$$
B_{p, n, l}:=\left\{\left(i_{1}, \ldots, i_{2 l}\right) \in \mathbb{N}^{2 l} \mid\left\{i_{1}, i_{3}, \ldots, i_{2 l-1}\right\} \in[p],\left\{i_{2}, i_{4}, \ldots, i_{2 l}\right\} \in[p+n] \backslash[p]\right\}
$$

Extracting the first entries of each $i^{k}$ and summing over them first yields

$$
\mathbb{E} Y^{(l)}=\sum_{b_{1}, \ldots, b_{K} \in[p]} \sum_{\substack{\mathbf{i}_{1} \in B_{p, n, l_{1}} \\\mathbf{i}_{K} \in B_{p, n, l_{K}} \\ \forall k \leq K: i_{1}^{k}=b_{k}}} \mathbb{E}\left[\prod_{k=1}^{K}\left(Y_{i_{1}^{k} i_{2}^{k}, i_{2}^{k} i_{3}^{k}}\right) \cdots\left(Y_{i_{2 l_{k}-1}^{k} i_{2 l_{k}}^{k}, i_{2 l_{k}}^{k} i_{2}^{k}}\right)\right]
$$

For ease of notation define

$$
B_{l, \mathbf{b}}:=\left\{\mathbf{i}=\left(i^{1}, \ldots, i^{K}\right) \in \prod_{k=1}^{K} B_{p, n, l_{k}} \mid \forall k \leq K:\left(l_{k}>0 \Rightarrow i_{1}^{k}=b_{k}\right)\right\}
$$

then the above formula for $\mathbb{E} Y^{(l)}$ becomes

$$
\mathbb{E} Y^{(l)}=\sum_{b_{1}, \ldots, b_{K} \in[p]} \sum_{\mathbf{i} \in B_{l, \mathbf{b}}} \mathbb{E}\left[\prod_{k=1}^{K}\left(Y_{i_{1}^{k} i_{2}^{k}, i_{2}^{k} i_{3}^{k}}\right) \cdots\left(Y_{i_{2 l_{k}-1}^{k} i_{2 l_{k}}^{k}, i_{2 l_{k}}^{k} i_{2}^{k}}\right)\right]
$$

Just as (2.4) in the GUE case, this formula now also holds for any $l_{1}, \ldots, l_{K} \in \mathbb{N}_{0}^{K}$. This time the mean is seen to have the form

$$
\mathbb{E}\left[\prod_{k=1}^{K} Y_{i_{1}^{k}, i_{2}^{k} i_{2}^{k}} \cdots Y_{i_{2 l_{k}-1}^{k} i_{2 l_{k}}^{k}, i_{2 l_{k}}^{k} i_{2}^{k}}\right]=\prod_{\substack{v \in[p] \\ w \in[p+n] \backslash[p]}} A_{v, w}(\mathbf{i})!=: W(A(\mathbf{i}))
$$

where again $A(\mathbf{i}):=\sum_{k=1}^{K} A\left(\mathbf{G}^{i}\right)$. Let $c:=i_{2 l_{1}}^{1}$ and define the symmetric matrix

$$
M_{\mathbf{b}, c}:=\left(\mathbf{1}_{i=b, j=c \text { or } i=c, j=b}\right)_{i, j \in[p+n]}
$$



With the very same argument as the one leading up to (2.7) - except that this time only the case $b_{1} \neq c$ is needed - we can decompose equality (3.5) into

$$
\begin{aligned}
\mathbb{E}_{Y^{(l)}}= & \underbrace{\sum_{\substack{b \in[p]^{K} \\
c \in[p+n] \backslash[p]}} \sum_{\substack{i \in B^{l, b} \\
i_{2 l_{1}}^{1}=c}} W\left(\mathbf{A}(i)-M_{b_{1}, c}\right) A_{b_{1}, c}\left(G_{i^{l_{1}}}\right)}_{=: E_{Y}^{1}(l)} \\
& +\sum_{\substack{b \in[p]^{K} \\
c \in[p+n] \backslash[p]}} \sum_{\substack{i \in B^{l, b} \\
i_{i_{1}}^{1}=c}} \underbrace{\sum_{\substack{s=k \\
A_{b_{1}, c}\left(G_{i^{k}}\right) \\
K}} W\left(\mathbf{A}(i)-M_{b_{1}, c}\right) \underbrace{\sum_{s=k}^{2 l_{1}} A_{b_{1}, c}\left(G_{i^{k}}\right)}_{=: E_{Y}^{2}(l)}}_{\cdot}
\end{aligned}
$$

For $E_{Y}^{1}(l)$ observe that $A_{b_{1}, c}\left(G_{i^{i_{1}}}\right)$ counts the number of occurrences of $\left(b_{1}, c\right)$ in $i^{1}=$ $\left(i_{1}^{1}, \ldots, i_{2 l_{1}}^{1}\right)$ and, if this number is zero, such an $i$ will not contribute to $E_{l}^{1}$. Define

$$
Q_{b, c}^{1}\left(i^{1}\right)=\left\{q<2 l_{1} \mid i_{q}^{1}=b, i_{q+1}^{1}=c\right\}
$$

then clearly $A_{b_{1}, c}\left(G_{i^{i_{1}}}\right)=\# Q_{b_{1}, c}^{1}\left(i^{1}\right)$ and by the bipartite definition of $B^{p, n, l_{1}}$ all elements in $Q_{b, c}^{1}\left(i^{1}\right)$ must be odd. For each $q \in Q_{b_{1}, c}^{1}\left(i^{1}\right)$ we give a unique way of splitting up $i^{1}$ into two new routes $\left\langle i^{1}\right\rangle_{q, 1}$ and $\left\langle i^{1}\right\rangle_{q, 2}$. Define

$$
\begin{aligned}
& \left\langle i^{1}\right\rangle_{q, 1}:=\left(i_{q+2}^{1}, \ldots, \underbrace{i_{2 l_{1}}^{1}}_{=c}\right) \in B^{p, n, l_{1}-\frac{q+1}{2}} \\
& \left\langle i^{1}\right\rangle_{q, 2}:=\left(\underbrace{i_{1}^{1}}_{=b_{1}}, \ldots, i_{q-1}^{1}\right) \in B^{p, n, \frac{q-1}{2}}
\end{aligned}
$$

and observe that between the multi-graphs $G_{i^{1}}$ and $G_{\left\langle i^{1}\right\rangle_{q, 1}} \cup G_{\left\langle i^{1}\right\rangle_{q, 1}}$ we have only lost one edge in each direction between the vertices $b_{1}$ and $c$ while all other edges remain. For

$$
J_{q}^{1}(i):=\left(\left\langle i_{q, 1}^{1}\right\rangle_{q, 1},\left\langle i^{1}\right\rangle_{q, 2}, i^{2}, \ldots, i^{K}\right)
$$

it follows that

$$
\mathbf{A}\left(J_{q}^{1}(i)\right)=\mathbf{A}(i)-M_{b_{1}, c}
$$

Since we sum over all choices of $c$ and all the other elements in $i^{1}$, which were not specified can still be chosen freely according the rules of $B^{l}$, this for $E_{l}^{1}$ implies

$$
\begin{aligned}
E_{Y}^{1}(l) & =\sum_{\substack{b \in[p]^{K} \\
c \in[p+n] \backslash[p]}} \sum_{\substack{i \in B^{l}, b \\
i_{2 l_{1}}^{1}=c}} \sum_{q \in Q_{b_{1}, c}^{1}\left(i^{1}\right)} W\left(\mathbf{A}\left(J_{q}^{1}(i)\right)\right) \\
& =\sum_{\substack{q=1 \\
o d d}}^{2 l_{1}-1} \sum_{\substack{b \in[p]^{K} \\
c \in[p+n] \backslash[p]}} \sum_{\substack{i \in B^{l, b} \\
i_{2 l_{1}}^{1}=c}} \sum_{\substack{q \in Q_{b_{1}, c}^{1}\left(i^{1}\right)}} W\left(\mathbf{A}\left(J_{q}^{1}(i)\right)\right)
\end{aligned}
$$



$$
\begin{aligned}
& =\sum_{r=1}^{l_{1}-q-\frac{1}{2}} \sum_{\substack{r=0 \\
b \in[p]^{K} \\
b^{\prime} \in[p], \text { if } r>0 \\
c \in[p+n] \backslash[p]}}
^{\sum_{j \in B S_{2, r}(l),\left(b^{\prime}, b_{1}, \ldots, b_{K}\right)} W(A(j))} \\
& =n \sum_{\tilde{b} \in[p]^{K+1}} \sum_{j \in B S_{2,0}(l), \tilde{b}} W(A(j)) \\
& +\sum_{r=1}^{l_{1}-1}
\end{aligned}
$$




where

$$
S_{2, r}(\mathbf{l})=\left(r, l_{1}-r-1, l_{2}, \ldots, l_{K}\right)
$$

is defined in analogy to $J_{q}^{1}(i)$ and

$$
S_{1}(\mathbf{l})=\left(l_{1}-1, l_{2}, \ldots, l_{K}\right)
$$

The factor $n$ in the first summand comes from the summation over $c$, which no longer had an influence on the latter sum in the case $q=2 l_{1}-1 \Leftrightarrow r=0$. The temporary factor $\frac{1}{p}$ in the first summand was added and removed with the summation over $b^{\prime}=\tilde{b}_{1}$.

Next for $E_{Y}^{2}(\mathbf{l})$ observe that $\sum_{k=2}^{K_{1}} A_{b_{1}, c}\left(G_{i^{k}}\right)$ counts the number of occurrences of $\left(b_{1}, c\right)$ in

$$
\left(i_{1}^{2}, \ldots, i_{2 l_{2}}^{2}\right), \ldots,\left(i_{1}^{K}, \ldots, i_{2 l_{K}}^{K}\right)
$$

and define the set

$$
Q_{b, c}^{2}(i):=\left\{(k, q) \in\{2, \ldots, K\} \times \mathbb{N} \mid i_{q}^{k}=b, i_{q+1}^{k}=c\right\}
$$

Again $\sum_{k=2}^{K} A_{b_{1}, c}\left(G_{i^{k}}\right)=\# Q_{b_{1}, c}^{2}$ and all tuples $(k, q) \in Q_{b, c}^{2}(i)$ must have odd $q$. This time for each $(k, q) \in Q_{b_{1}, c}^{2}(i)$ we give a unique way of joining the routes $i^{1}$ and $i^{k}$ into a new route

$$
\left\langle i^{1}, i^{k}\right\rangle_{q}:=(\underbrace{i_{1}^{k}}_{=b_{k}}, \ldots, \underbrace{i_{q-1}^{k}}_{=b_{1}}, \underbrace{i_{1}^{1}}_{=c}, \ldots, \underbrace{i_{2 l_{1}}^{1}}_{=i_{q+2}^{k}}, \ldots, \underbrace{i_{2 l_{k}}^{k}}_{\in B_{p, n, l_{1}+l_{s}-1}}
$$

Again we between the multigraphs $G_{i^{1}} \cup G_{i^{k}}$ and $G_{\left\langle i^{1}, i^{k}\right\rangle_{q}}$ only loose one edge in each direction between the vertices $b_{1}$ and $c$ while all other edges remain. For

$$
J_{(k, q)}^{2}(i):=\left(\left\langle i^{1}, i^{k}\right\rangle_{q},, i^{2} \ldots, \widehat{i^{k}}, \ldots, i^{K}\right)
$$



it follows that

$$
A\left(J_{(k, q)}^{2}(i)\right)=A(i)-M_{b_{1}, c}
$$

and similarly to (2.14) we get

$$
\begin{aligned}
& E Y^{2}(l)=\sum_{\substack{b \in[p]^{K} \\
c \in[p+n] \backslash[p]}} \sum_{\substack{i \in \mathfrak{B}_{l, b} \\
i_{1} l_{1}=c}} \sum_{\substack{(k, q) \in \mathfrak{Q}_{b_{1}, c}^{2} \\
r=\frac{q+1}{2}}} A\left(J_{(k, q)}^{2}(i)\right) \\
&=\sum_{k=2}^{K} \sum_{r=1}^{l_{k}} \sum_{\tilde{b} \in[p]^{K-1}} \sum_{i \in \mathfrak{B}_{S_{3, k}(l), y, \tilde{b}}} A(i, j)=\sum_{k=2}^{K} l_{k} E Y\left(S_{3, k}(l)\right)
\end{aligned}
$$

where

$$
S_{3, k}(l):=\left(l_{1}+l_{k}-1, l_{2}, \ldots, \widehat{l_{k}}, \ldots, l_{K}\right)
$$

is defined in analogy to $J_{k, 2 r-1}^{2}$.
Equalities (3.8), (3.11) and (3.14) together show

$$
E Y^{2}(l)=n E Y\left(S_{1}(l)\right)+\sum_{r=1}^{l_{1}-1} E Y\left(S_{2, r}(l)\right)+\sum_{k=2}^{K} l_{k} E Y\left(S_{3, l_{k}}(l)\right)
$$

# 3.2 Theorem (Recursion for mixed trace moments of real isotropic Wishart matrices) 

For $K \in \mathbb{N}$ and any $l=\left(l_{1}, \ldots, l_{K}\right) \in \mathbb{N}_{0}^{K}$ the following recursive properties hold.
a) If $l_{1}=0$, then $E Y^{(l)}=p E Y\left(S_{0}(l)\right)$ for $S_{0}\left(0, l_{2}, \ldots, l_{K}\right):=\left(l_{2}, \ldots, l_{K}\right)$.
b) If $l_{1}>0$, then

$$
E X^{(l)}=\left(n+l_{1}-1\right) E X\left(S_{1}(l)\right)+\sum_{r=1}^{l_{1}-1} E X\left(S_{2, r}(l)\right)+2 \sum_{k=2}^{K} l_{k} E X\left(S_{3, k}(l)\right)
$$

where $S_{1}, S_{2, q}$ and $S_{3, k}$ are as defined in Theorem 3.1.
Again the end point

$$
E X((,(,)).newLine=E\left[\operatorname{tr}\left(\left(X X^{T}\right)^{0}\right)\right]=p
$$

for $(K, L)=(1,0)$ allows for the calculation of all mixed moments.



Proof. In complete analogy to the proof of Theorem 3.1 know (a) to hold and for the proof of (b) in the case $l^{1}>0$ have

$$
\underset{X^{(l)}}{\mathbb{E}}=\sum_{b_{1}, \ldots, b_{K} \in[p]} \sum_{i \in B^{l, b}} \mathbb{E}\left[\prod_{k=1}^{K}\left(X_{1, i_{2}^{k}}^{i k} X_{2, i_{2}^{k}}^{i k}\right) \cdots\left(X_{2 l_{k}-1, i_{2 l_{k}}}^{i k} X_{1, i_{2 l_{k}}}^{i k}\right)\right]
$$

for any $l^{1}, \ldots, l^{K} \in \mathbb{N}_{0}^{K}$. The weight is instead

$$
\mathbb{E}\left[\prod_{k=1}^{K} X_{1, i_{2}^{k}}^{i k} X_{3, i_{2}^{k}}^{i k} \cdots X_{2 l_{k}-1, i_{2 l_{k}}}^{i k} X_{1, i_{2 l_{k}}}^{i k}\right]=\left.\prod_{\substack{v \in[p] \\ w \in[p+n] \backslash[p]}}\left(\tilde{A}_{v, w}^{(i)}-1\right)\right)!!=: W(\tilde{A}^{(i)})
$$

where $\tilde{A}^{(i)}=\sum_{k=1}^{K} A^{\left(\tilde{G}_{i}\right)}$. Let $c:=i_{2 l^{1}}^{1}$ and define the matrix

$$
\tilde{M}^{b, c}:=2\left(\mathbb{1}_{i=b, j=c} \text { or } i=c, j=b\right)_{i, j \in[p+n]}
$$

By the definition of the weight $W(\tilde{A}^{(i)})$ it for all $i \in B^{l, b}$ with $\tilde{A}^{(i)}{ }_{b^{1}, c} \geq 2$ follows that

$$
\begin{aligned}
W\left(\tilde{A}^{(i)}\right) & =W\left(\tilde{A}^{(i)}-\tilde{M}^{b^{1}, c}\right)\left(\tilde{A}^{(i)} b^{1, c}-1\right) \\
& =W\left(\tilde{A}^{(i)}-\tilde{M}^{b^{1}, c}\right)\left(A^{b^{1}, c}\left(\tilde{G}_{i_{1}}\right)-1+\sum_{k=2}^{K} A^{b^{1}, c}\left(\tilde{G}_{i_{k}}\right)\right)
\end{aligned}
$$

Again this can be used to decompose equality (3.15) into

$$
\begin{aligned}
\underset{X^{(l)}}{\mathbb{E}}= & \underbrace{\sum_{b \in[p]^{K}} \sum_{c \in[p+n] \backslash[p]} \sum_{\substack{i \in B^{I, b} \\
i_{2 l}^{1}=c}} W\left(\tilde{A}^{(i)}-\tilde{M}^{b^{1}, c}\right)\left(A^{b^{1}, c}\left(\tilde{G}_{i_{1}}\right)-1\right)}_{=: E_{1}} \\
& +\underbrace{\sum_{b \in[p]^{K}} \sum_{c \in[p+n] \backslash[p]} \sum_{\substack{i \in B^{l, b} \\
i_{2 l^{1}}^{1}=c}} W\left(\tilde{A}^{(i)}-\tilde{M}^{b^{1}, c}\right) \underbrace{\sum_{k=2}^{K} A^{b^{1}, c}\left(\tilde{G}_{i_{k}}\right)}_{=: E_{2}}}_{\mathbb{X}\left(X^{(l)}\right)}
\end{aligned}
$$

since all $i \in B^{l, b}$ contributing to the sum must satisfy $\tilde{A}^{(i)} b^{1, c} \geq 2$. Define

$$
\begin{aligned}
Q_{b, c}^{0}\left(i^{1}\right) & =\left\{q<2^{l^{1}} \mid i_{q}^{1}=c, i_{q+1}^{1}=b\right\} \\
Q_{b, c}^{1}\left(i^{1}\right) & =\left\{q<2^{l^{1}} \mid i_{q}^{1}=b, i_{q+1}^{1}=c\right\}=Q_{c, b}^{0}(i)
\end{aligned}
$$



then $A_{b_{1}, c}\left(\tilde{G}_{i_{1}}\right)^{-1}=\# Q_{b_{1}, c}^{0}\left(i_{1}\right)+\# Q_{b_{1}, c}^{1}\left(i_{1}\right)$ and by construction all elements of $Q_{b_{1}, c}^{0}\left(i_{1}\right)$ must be even and all elements of $Q_{b_{1}, c}^{1}\left(i_{1}\right)$ must be odd. For each $q \in Q_{b_{1}, c}^{1}\left(i_{1}\right)$ let $J_{q}^{1}(i)$ be just as in the proof of Theorem 3.1 and we also have $\tilde{A}\left(J_{q}^{1}(i)\right)=\tilde{A}(i)-\tilde{M}_{b_{1}, c}$. For each $q \in Q_{b_{1}, c}^{0}\left(i_{1}\right)$ let

$$
\begin{aligned}
& \left\langle i_{1}\right\rangle^{q}=(i_{1}^{1}=b_{1}, \ldots, i_{\underbrace{q-1}_{2 l_{1} \mathrm{c}}}, \underbrace{i_{2 l_{1}-1}, \ldots, i_{q+3}, i_{q+2}}=c \mid, i_{2 l_{1} \mid c}^{+}) \in B_{p, n, l_{1}-1} \quad \text { and } \\
& J_{q}^{0}:=\left(\left\langle i_{1}\right\rangle^{q}, i_{2}, \ldots, i_{K}\right)
\end{aligned}
$$

then it also holds that $\tilde{A}\left(J_{q}^{0}(i)\right)=\tilde{A}(i)-\tilde{M}_{b_{1}, c}$ and we can similarly to (3.11) see

$$
\mathrm{E}_{X}^{1}(l)=\begin{aligned}
& \sum_{b \in[p]^{K}} \sum_{c \in[p+n] \backslash[p]} \sum_{i \in B_{l, b}^{2 l_{1}=c}} \sum_{q \in Q_{b_{1}, c}^{\sum}} \mathcal{W}\left(\tilde{A}\left(J_{q}^{0}(i)\right)\right) \\
& +\sum_{b \in[p]^{K}} \sum_{c \in[p+n] \backslash[p]} \sum_{i \in B_{l, b}^{2 l_{1}=c}} \sum_{q \in Q_{b_{1}, c}^{1}(i)} \mathcal{W}\left(\tilde{A}\left(J_{q}^{1}(i)\right)\right)
\end{aligned}
$$

For the second summand the exact same steps as in (3.11) show that it must be equal to

$$
n \mathbf{E}_{X}\left(S_{1}(l)\right)+\sum_{r=1}^{l-1} \mathbf{E}_{X}\left(S_{2, r}(l)\right)
$$

The first summand can likewise be calculated to be

$$
\begin{aligned}
& \sum_{\substack{q=2 \\
q \text { even }}}^{2 l_{1}-2} \sum_{b \in[p]^{K}} \sum_{c \in[p+n] \backslash[p]} \sum_{i \in B_{l, b}^{2 l_{1}=c}} \sum_{q \in Q_{\ONG}^{0}(i)} \mathcal{W}\left(\tilde{A}\left(J_{q}^{0}(i)\right)\right) \\
&=\left(l_{1}-1\right) \sum_{b \in[p]^{K}} \sum_{j \in B_{S_{1}(l), b}} \mathcal{W}(\tilde{A}(j))=\left(l_{1}-1\right) \mathbf{E}_{X}\left(S_{1}(l)\right)
\end{aligned}
$$

and we have shown

$$
\mathrm{E}_{X}^{1}(l)=\left(n+l_{1}-1\right) \mathbf{E}_{X}\left(S_{1}(l)\right)+\sum_{r=1}^{l_{1}-1} \mathbf{E}_{X}\left(S_{2, r}(l)\right)
$$

The same idea can be used to calculate $\mathbf{E}_{X}^{2}(l)$. First define

$$
Q_{b, c}^{2}(i)=\left\{(k, q) \in\{2, \ldots, K\} \times \mathbb{N} \mid q<2 l_{k}, i_{q}^{k}=b, i_{q+1}^{k}=c\right\}
$$



$$
Q_{b, c}^{3}(i)=\left\{(k, q) \in\left\{2, \ldots, K\right\} \times \mathbb{N} \mid q \leq 2 l_{k}, i_{q}^{k}=c, i_{\left(q \bmod 2 l_{k}\right)+1}^{k}=b\right\}
$$

then again $\sum_{k=2}^{K} A_{b_{1}, c}\left(\tilde{\mathbf{i}}^{i k}\right)=\# Q_{b_{1}, c}^{2}(i)+\# Q_{b_{1}, c}^{3}(i)$ and all tuples $(k, q)$ from $Q_{b, c}^{2}(i)$ must have odd $q$ while all tuples $(k, q)$ from $Q_{b, c}^{3}(i)$ must have even $q$. For $J_{(k, q)}^{2}(i)$ as in the proof of Theorem 3.1, it holds that $\tilde{A}\left(J_{(k, q)}^{2}(i)\right)=\tilde{A}(i)-\tilde{M}_{b_{1}, c}$. Similarly for $(k, q) \in Q_{b_{1}, c}^{3}(i)$ define

$$
\left[i^{1}, \mathbf{i}^{k}\right]_{q}:= \begin{cases}\overbrace{i_{1}^{1}, \ldots, i_{2 l_{1}}^{1}}^{=b_{1}}, \ldots, \overbrace{i_{q}^{k}, i_{q-1}^{k}, \ldots, i_{1}^{k}, i_{2 l_{k}}^{k}, i_{2 l_{k}-1}^{k}, \ldots, i_{q+2}^{k}}^{=}, & \text { if } q<2 l_{k} \\ (i_{1}^{1}\lfloor\ldots, i_{2 l_{1}}^{1}]_{\lfloor}^{=}, \ldots, i_{2 l_{k}}^{k}, i_{2 l_{k}-1}^{k}, \ldots, i_{2}^{k}), & \text { if } q=2 l_{k}\end{cases}
$$

and

$$
J_{(k, q)}^{3}=\left(\left[i^{1}, \mathbf{i}^{k}\right]_{q}, i^{2}, \ldots, \widehat{i^{k}}, \ldots, i^{K}\right)
$$

then we also have $\tilde{A}\left(J_{(k, q)}^{3}(i)\right)=\tilde{A}(i)-\tilde{M}_{b_{1}, c}$ and can further decompose $E_{\mathbf{X}}^{2}(l)$ into

$$
\begin{aligned}
E_{\mathbf{X}}^{2}(l)= & \sum_{b \in[p]^{K}} \sum_{c \in[p+n] \backslash[p]} \sum_{\substack{i \in \mathcal{B}_{l}} l_{1}=c} \sum_{(k, q) \in Q_{b_{1}, c}^{2}(i)} W\left(\tilde{A}\left(J_{(k, q)}^{2}(i)\right)\right) \\
& +\sum_{b \in[p]^{K}} \sum_{c \in[p+n] \backslash[p]} \sum_{\substack{i \in B_{l, b} l_{1}=c}} \sum_{(k, q) \in Q_{b_{1}, c}^{3}(i)} W\left(\tilde{A}\left(J_{(k, q)}^{3}(i)\right)\right)
\end{aligned}
$$

The first summand is by the same steps as in (3.14) equal to $\sum_{k=2}^{K} l_{k} E_{X}\left(S_{3, k}(l)\right)$. Note that $\left(k, 2 l_{k}\right) \in Q_{b_{1}, c}^{3}$ is only possible, if $b_{k}=b_{1}$. This will ensure that we don't gain a factor of $n$ from the summation over $b_{k}$ in the case $q=2 l_{k}$ of the below calculation. The second summand is calculated to be

$$
\begin{aligned}
& \sum_{k=2}^{K} \sum_{\substack{q=2 \\
e v e n}}^{2 l_{k}} \sum_{b \in[p]^{K}} \sum_{c \in[p+n] \backslash p]} \sum_{\substack{i \in \mathcal{B}_{l, b} \\
l_{1}=c}} \sum_{(k, q) \in Q_{b_{1}, c}^{3}(i)} W\left(\tilde{A}\left(J_{(k, q)}^{3}(i)\right)\right) \\
& =\sum_{k=2}^{K} \sum_{q=2}^{2 l_{k}} \sum_{\tilde{b} \in[p]^{K-1}} \sum_{\tilde{\mathbf{j}} \in \mathcal{B}_{S_{3, k}(l), \tilde{\mathbf{b}}}} W(\tilde{\mathbf{A}}(\mathbf{j})) \\
& =\sum_{k=2}^{K} l_{K} E_{X}\left(S_{3, k}(l)\right)
\end{aligned}
$$



and we have shown

$$
\mathbb{E}^{2} \mathcal{X}^{\mathbf{l}}=\sum_{k=2}^{K} l_{k} \mathbb{E} \mathcal{X}\left(\mathcal{S}_{3, k}(\mathbf{l})\right)
$$

The equalities (3.18), (3.22) and (3.26) together prove

$$
\mathbb{E} \mathcal{X}^{(\mathbf{l})}=\left(n+l_{1}-1\right) \mathbb{E} \mathcal{X}\left(\mathcal{S}_{1}(\mathbf{l})\right)+\sum_{r=1}^{l_{1}-1} \mathbb{E} \mathcal{X}\left(\mathcal{S}_{2, r}(\mathbf{l})\right)+2 \sum_{k=2}^{K} l_{k} \mathbb{E} \mathcal{X}\left(\mathcal{S}_{3, k}(\mathbf{l})\right)
$$

# $4 \underline{\text { Gaussian Orthogonal Ensemble }}$ 

### 4.1 Theorem (Recursion for mixed trace moments of the GOE)

For $K \in \mathbb{N}$ and any $\mathbf{l}=\left(l_{1}, \ldots, l_{K}\right) \in \mathbb{N}_{0}^{K}$ - with even $L:=l_{1}+\ldots+l_{K}$ - the following recursive properties hold.
a) If $l_{1}=0$, then $\mathbb{E} \tilde{\mathcal{Z}}^{(\mathbf{l})}=n \mathbb{E} \tilde{\mathcal{Z}}\left(\mathcal{S}_{0}(\mathbf{l})\right)$ for

$$
\mathcal{S}_{0}\left(0, l_{2}, \ldots, l_{K}\right):=\left(l_{2}, \ldots, l_{K}\right)
$$

b) If $l_{1}>0$, then

$$
\mathbb{E} \tilde{\mathcal{Z}}^{(\mathbf{l})}=\left(l_{1}-1\right) \mathbb{E} \tilde{\mathcal{Z}}\left(\mathcal{S}_{1}(\mathbf{l})\right)+\sum_{q=1}^{l_{1}-1} \mathbb{E} \tilde{\mathcal{Z}}\left(\mathcal{S}_{2, q}(\mathbf{l})\right)+2 \sum_{k=2}^{K} l_{k} \mathbb{E} \tilde{\mathcal{Z}}\left(\mathcal{S}_{3, k}(\mathbf{l})\right)
$$

where

$$
\mathcal{S}_{1}(x):=\left(l_{1}-2, l_{2}, \ldots, l_{K}\right)
$$

and $\mathcal{S}_{2, q}$ as well as $\mathcal{S}_{3, k}$ are as defined in Theorem 2.1.
As before in Theorem 2.1 the starting point

$$
\mathbb{E} \tilde{\mathcal{Z}} требуется))=\mathbb{E}\left[\operatorname{tr}(\tilde{\mathcal{Z}})^{0}\right]=n
$$

for $(K, L)=(1,0)$ allows for the calculation of all mixed moments when $L$ is even and for odd $L$ the mixed trace moment must be zero.

Proof. Like before, only property (b) needs to be shown. In complete analogy to (2.4) we have

$$
\mathbb{E} \tilde{\mathcal{Z}}^{(\mathbf{l})}=\sum_{b_{1}, \ldots, b_{K} \in[n]} \sum_{i \in I_{l, \mathbf{b}}} \mathbb{E}\left[\prod_{k=1}^{K} \tilde{Z}_{i_{k}^{1}, i_{k}^{2}} \tilde{Z}_{i_{k}^{k-1}, i_{k}^{k}} \tilde{Z}_{i_{k}^{l_{k}}, i_{1}^{k}}\right]
$$



This time the mean has the form

$$
\begin{aligned}
\mathbb{E}\left[\prod_{k=1}^{K} \tilde{Z}_{i_{k}}^{1, i_{k}{ }_{k}^{k}} \cdots \tilde{Z}_{i_{k_{l-1}}, \bar{i}_{k_{l}}} \tilde{Z}_{i_{k_{l}},}^{1}\right] & \left.=\prod_{\bar{v}, w \in[n]} \frac{\overline{\tilde{A}}_{v}, w^{(i)}-1)}{!}\right)\left(\prod_{\bar{v} \in[n]} \frac{2 \overline{\tilde{A}}_{\tilde{v},}^{(i)}{ }_{!}}{2\left({\overline{\tilde{A}}_{v}, v}^{(i)}-1\right)!}\right) \\
& =: \mathcal{W}\left({\widetilde{A}}^{(i)}\right),
\end{aligned}
$$

which implies that it can with

$$
\tilde{\mathbf{M}}^{b, c}:=2\left(\mathbb{1}_{i=b, j=c} \text { or } i=c, j=b\right)_{i, j \in[n]}
$$

be decomposed into

$$
\begin{aligned}
\mathcal{W}\left({\widetilde{A}}^{(i)}\right) & =\mathcal{W}\left({\widetilde{A}}^{(i)}-\tilde{\mathbf{M}}^{b_{1}, c}\right) 2 \mathbb{1}_{b_{1}=c}\left(\widetilde{A}^{b_{1}, c}({\widetilde{i}}^{i})-1\right) \\
& =\mathcal{W}\left({\widetilde{A}}^{(i)}-\tilde{\mathbf{M}}^{b_{1}, c}\right) 2 \mathbb{1}_{b_{1}=c}\left(A^{b_{1}, c}\left({\widetilde{G}}^{i_{l}}\right)-1+\sum_{k=2}^{K} A^{b_{1}, c}\left({\widetilde{G}}^{i_{k}}\right)\right)
\end{aligned}
$$

As is by now standard, we thus change (4.3) into

$$
\begin{gathered}
\mathbb{E} \tilde{\mathcal{Z}}^{(l)}=\overbrace{\mathbb{E} 1}^{E} \mathcal{Z}^{(l)} \\
+\underset{b_{1}, \ldots, b_{K} \in[n]}{\sum} \underset{c \in[n]}{\sum} \underset{i \in \mathcal{J}^{l, b}}{\sum} \mathbb{1}_{l_{1}=c}\left(A^{b_{1}, c}\left({\widetilde{G}}^{i_{1}}\right)-1\right) \\
++ \underset{b_{1}, \ldots, b_{K} \in[n]}{\sum} \underset{c \in[n]}{\sum} \underset{\mathbf{i} \in \mathcal{J}^{l, b}}{\sum} \underset{\substack{b_{1}, \ldots, b_{K} \in[n]}}{\sum} \mathbb{1}\left(\widetilde{\mathbf{M}}^{b_{1}, c} \sum_{k=2}^{K} A^{b_{1}, c}\left({\widetilde{G}}^{i_{k}}\right)\right. \\
=: E_{2} \tilde{\mathcal{Z}}^{(l)}
\end{gathered}
$$

For

$$
\begin{aligned}
& Q_{b, c}^{0}\left(i_{1}\right):=\left\{q<l_{1} \mid i_{q}^{1}=c, i_{q+1}^{1}=b\right\} \\
& Q_{b, c}^{1}\left(i_{1}\right):=\left\{q<l_{1} \mid i_{q}^{1}=b, i_{q+1}^{1}=c\right\}=Q_{c, b}^{0}\left(i_{1}\right)
\end{aligned}
$$

it holds that $2 \mathbb{1}_{b_{1}=c}\left(A^{b_{1}, c}\left({\widetilde{G}}^{i_{1}}\right)-1\right)=\# Q_{b_{1}, c}^{0}\left(i_{1}\right)+\# Q_{b_{1}, c}^{1}\left(i_{1}\right)$ and with $\mathcal{J}_{q}^{1}(i)$ as in (2.9) we for each $q \in Q_{b_{1}, c}^{1}\left(i_{1}\right)$ have

$$
{\widetilde{A}}^{\left(\mathcal{J}_{q}^{1}(i)\right)}={\widetilde{A}}^{(i)}-\tilde{\mathbf{M}}^{b_{1}, c}
$$

For each $q \in Q_{b_{1}, c}^{0}\left(i_{1}\right)$ we similarly to (3.21) define

$$
\left\langle i_{1}\right\rangle_{q}=(\underbrace{i_{1}^{1}}_{=b_{1}^{1}}, \ldots, i_{q-1}^{1}, \underbrace{i_{l_{1}}^{1}}_{=c}, i_{l_{1}-1}^{1}, \ldots, i_{q+3}^{1}, \underbrace{i_{q+2}}_{\lceil 2} \in[n]^{l_{1}-2}
$$



and

$$
J_{q}^{0}:=\left(\left\langle i_{1}\right\rangle_{q}, i_{2}, \ldots, i_{K}\right)
$$

then it also follows that $\tilde{A}\left(J_{q}^{0}(i)\right)=\tilde{A}(i)-\tilde{M}_{b_{1}, c}$, since only the connections between $\left(i_{1}^{q}, i_{q+1}^{1}\right)=(c, b)$ and $\left(i_{1}^{l_{1}}, i_{1}^{1}\right)=(c, b)$ are removed by $J_{q}^{0}$. Using $J^{0}$ and $J^{1}$ we write $\mathbb{E}_{\tilde{Z}}^{1}(l)$ as

$$
\begin{aligned}
\mathbb{E}_{\tilde{\boldsymbol{Z}}}^{1}(l)= & \sum_{b_{1}, \ldots, b_{K} \in[n]} \sum_{c \in[n]} \sum_{\substack{n \in I_{l}, b \\
i_{1} \frac{l_{1}}{c}}} \sum_{q \in \bar{Q}_{b_{1}, c}\left(i_{1}\right)} W\left(\tilde{A}\left(J_{q}^{0}\right)\right) \\
& +\sum_{b_{1}, \ldots, b_{K} \in[n]} \sum_{c \in[n]} \sum_{\substack{i \in I_{l}, b \\
i_{1} \frac{1}{c}}} \sum_{q \in \bar{Q}_{b_{1}, c}\left(i_{1}\right)} W\left(\tilde{A}\left(J_{q}^{1}\right)\right)
\end{aligned}
$$

For the second summand the exact same steps as in (2.10) and (2.11) show that it must be equal to

$$
\sum_{q=1}^{l_{1}-1} \mathbb{E} \tilde{Z}\left(S^{2, q}(l)\right)
$$

Combining the ideas of (2.10) and (3.22) we for the first summand observe

$$
\begin{aligned}
\sum_{b_{1}, \ldots, b_{K} \in[n]} \sum_{c \in[n]} & \sum_{\substack{i \in I_{l, b} \\
i_{1}}} \sum_{q \in \bar{Q}_{b_{1}, c}\left(i_{1}\right)} W\left(\tilde{A}\left(J_{q}^{0}\right)\right)=\sum_{q=1}^{l_{1}-1} \sum_{\substack{b_{1}, \ldots, b_{K} \in[n] \\
c \in[n]}} \sum_{\substack{i \in I_{l}, b \\
i_{1} \frac{l_{1}}{c} \\

}} W\left(\tilde{A}\left(J_{q}^{0}\right)\right) \\
& =\left(l_{1}-1\right) \sum_{b_{1}, \ldots, b_{K} \subset[n]} \sum_{j \in I_{S^{1}(l), b}} W(\tilde{A}(j))=\left(l_{1}-1\right) \mathbb{E} \tilde{Z}\left(S^{1}(l)\right)
\end{aligned}
$$

where

$$
S^{1}(l):=\left(l_{1}-2, l_{2}, \ldots, l_{K}\right)
$$

We have thus shown

$$
\mathbb{E}_{\tilde{\boldsymbol{Z}}}^{1}(l)=\left(l_{1}-1\right) \mathbb{E} \tilde{Z}\left(S^{1}(l)\right)+\sum_{q=1}^{l_{1}-1} \mathbb{E} \tilde{Z}\left(S^{2, q}(l)\right)
$$

With analogous steps to those used for the proof of (3.26) we will now calculate $\mathbb{E}_{\tilde{Z}}^{2}(l)$. First define



$$
\begin{aligned}
& Q_{b, c}^{3}(i):=\left\{(k, q) \in\{2, \ldots, K\} \times \mathbb{N} \mid q \leq l_{k}, i_{q}^{k}=b, i_{\left(q \bmod l_{k}\right)+1}^{k}=c\right\} \\
& Q_{b, c}^{2}(i):=\left\{(k, q) \in\{2, \ldots, K\} \times \mathbb{N} \mid q \leq l_{k}, i_{q}^{k}=c, i_{\left(q \bmod l_{k}\right)+1}^{k}=b\right\}=Q_{c, b}^{2}(i),
\end{aligned}
$$



then we have $2 \mathbb{1}_{b_{1}=c} \sum_{k=2}^{K} A_{b_{1}, c}\left(\tilde{G}_{i_{k}}\right)=\# \mathcal{Q}_{b_{1}, c}^{2}(i)+\# \mathcal{Q}_{b_{1}, c}^{3}(i)$. For $J_{(k, q)}^{2}(i)$ as in (2.13) it holds that $\tilde{A}\left(J_{(k, q)}^{2}(i)\right)=\tilde{A}(i)-\tilde{M}_{b_{1}, c_{1}}$ and for each $(k, q) \in \mathcal{Q}_{b_{1}, c}^{3}(i)$ we similarly to (3.25) define



$$
J_{(k, q)}^{3}=\left(\left[i_{1}, i_{k}\right]_{q}, i_{2}, \ldots, \widehat{i_{k}}, \ldots, i_{K}\right)
$$

Again by construction of $J^{3}$ it holds that $\tilde{A}\left(J_{(k, q)}^{3}(i)\right)=\tilde{A}(i)-\tilde{M}_{b_{1}, c_{1}}$ and we can decompose $\mathbb{E}_{\tilde{\mathbf{Z}}}^{2}(\mathbf{l})$ into

$$
\begin{aligned}
\mathbb{E}_{\tilde{\mathbf{Z}}}^{2}(\mathbf{l}) & =\sum_{b_{1}, \ldots, b_{K} \in[n]}\left(\sum_{c \in[n]}\left(\left[\sum_{i \in I_{l, b}} \mathbb{1}_{l_{1}=c}\right]\left(\sum_{(k, q) \in \mathcal{Q}_{b_{1}, c}^{2}(i)} W\left(\tilde{A}\left(J_{(k, q)}^{2}(i)\right)\right)\right)\right.\right. \\
& \left.+\sum_{i \in I_{l}, b} \sum_{c \in[n]} \mathbb{1}_{l_{1}=c} \sum_{(k, q) \in \mathcal{Q}_{b_{1}, c}^{3}(i)} W\left(\tilde{A}\left(J_{(k, q)}^{3}(i)\right)\right)\right)
\end{aligned}
$$

The first summand is by the same steps as in (2.14) equal to

$$
\sum_{k=2}^{K} l_{k} \mathbb{E} \tilde{Z}\left(\mathfrak{S}_{3, k}(\mathbf{l})\right)
$$

and for the second summand the steps are again analogous to (2.14) and (3.26) and we find

$$
\begin{aligned}
& \sum_{b_{1}, \ldots, b_{K} \in[n]}\left(\sum_{c \in[n]}\left(\sum_{i \in I_{l, b}} \mathbb{1}_{l_{1}=c}\right)\left(\sum_{\genfrac{}{}{0}{}{(k, q) \in \mathcal{Q}_{b_{1}, c}^{3}(i)}}{ } W\left(\tilde{A}\left(J_{(k, q)}^{3}(i)\right)\right)\right)\right) \\
& =\sum_{k=2}^{K} l_{k} \sum_{q=1}^{K} \sum_{\substack{b \in[n]^{K} \\
c \in[n]}}\left(\sum_{\substack{i \in I_{l, b} \\
l_{1}=c}} \sum_{\genfrac{}{}{0}{}{(k, q) \in \mathcal{Q}_{b_{1}, c}^{3}(i)}{}} W\left(\tilde{A}\left(J_{(k, q)}^{3}(i)\right)\right)\right) \\
& =\sum_{k=2}^{K} l_{k} \sum_{q=1}^{K} \sum_{\tilde{b} \in[n]^{K-1}} \sum_{i \in I_{l, \widetilde{b}}} W(\tilde{A}(\mathbf{j})) \\
& =\sum_{k=2}^{K} l_{k} \mathbb{E} \tilde{Z}\left(\mathfrak{S}_{3, k}(\mathbf{l})\right),
\end{aligned}
$$



so we have shown

$$
\mathbb{E} \tilde{Z}^{2}(l)=2 \sum_{k=2}^{K} l_{k} \mathbb{E} \tilde{Z}\left(S_{3, k}(l)\right)
$$

Finally equalities (4.6), (4.10) and (4.14) together yield

$$
\mathbb{E} \tilde{Z}(l)=\left(l_{1}-1\right) \mathbb{E} \tilde{Z}\left(S_{1}(l)\right)+\sum_{q=1}^{l_{1}-1} \mathbb{E} \tilde{Z}\left(S_{2, q}(l)\right)+2 \sum_{k=2}^{K} l_{k} \mathbb{E} \tilde{Z}\left(S_{3, k}(l)\right)
$$

# List of symbols 







# REFERENCES 

[1] {\`E. T. Akhmedov and Sh. R. Shakirov, Gluings of surfaces with polygonal boundaries, Funktsional. Anal. i Prilozhen. 43 (2009), no. 4, 3-13, DOI 10.1007/s10688-009-0033-y (Russian, with Russian summary); English transl., Funct. Anal. Appl. 43 (2009), no. 4, 245-253. MR2596651
[2] Greg W. Anderson, Alice Guionnet, and Ofer Zeitouni, An introduction to random matrices, Cambridge Studies in Advanced Mathematics, vol. 118, Cambridge University Press, Cambridge, 2010. MR2760897
[3] Olivier Bernardi, An analogue of the Harer-Zagier formula for unicellular maps on general surfaces, Adv. in Appl. Math. 48 (2012), no. 1, 164-180, DOI 10.1016/j.aam.2011.06.005. MR2845513
[4] Persi Diaconis and Steven N. Evans, Linear functionals of eigenvalues of random matrices, Trans. Amer. Math. Soc. 353 (2001), no. 7, 2615-2633, DOI 10.1090/S0002-9947-01-02800-8. MR1828463
[5] Uffe Haagerup and Steen Thorbjørnsen, Random matrices with complex Gaussian entries, Expo. Math. 21 (2003), no. 4, 293-337, DOI 10.1016/S0723-0869(03)80036-1. MR2022002
[6] J. Harer and D. Zagier, The Euler characteristic of the moduli space of curves, Invent. Math. 85 (1986), no. 3, 457-485, DOI 10.1007/BF01390325. MR848681
[7] D. M. Jackson, Some combinatorial problems associated with products of conjugacy classes of the symmetric group, J. Combin. Theory Ser. A 49 (1988), no. 2, 363-369, DOI 10.1016/00973165(88)90062-3. MR0964394
[8] Michel Ledoux and Brian Rider, Small deviations for beta ensembles, Electron. J. Probab. 15 (2010), no. 41, 1319-1343, DOI 10.1214/EJP.v15-798. MR2678393
[9] M. Ledoux, A recursion formula for the moments of the Gaussian orthogonal ensemble, Ann. Inst. Henri Poincaré Probab. Stat. 45 (2009), no. 3, 754-769, DOI 10.1214/08-AIHP184 (English, with English and French summaries). MR2548502
[10] Sandrine Péché, Universality results for the largest eigenvalues of some sample covariance matrix ensembles, Probab. Theory Related Fields 143 (2009), no. 3-4, 481-516, DOI 10.1007/s00440-0070133-7. MR2475670
[11] Jolanta Pielaszkiewicz, Dietrich Von Rosen, and Martin Singull, On $\mathbb{E}\left[\prod_{i=0}^{k} \operatorname{Tr}\left\{W^{m_{i}}\right\}\right]$, where $W \sim W_{p}(l, n)$, Comm. Statist. Theory Methods 46 (2017), no. 6, 2990 - 3005, DOI 10.1080/03610926.2015.1053942. MR3579781
[12] Ya. Sinai and A. Soshnikov, Central limit theorem for traces of large random symmetric matrices with independent matrix elements, Bol. Soc. Brasil. Mat. (N.S.) 29 (1998), no. 1, 1-24, DOI 10.1007/BF01245866. MR1620151
[13] Ya. G. Sinaĭ and A. B. Soshnikov, A refinement of Wigner's semicircle law in a neighborhood of the spectrum edge for random symmetric matrices, Funktsional. Anal. i Prilozhen. 32 (1998), no. 2, 5679,96 , DOI 10.1007/BF02482597 (Russian, with Russian summary); English transl., Funct. Anal. Appl. 32 (1998), no. 2, 114-131. MR1647832
[14] Alexander Soshnikov, Universality at the edge of the spectrum in Wigner random matrices, Comm. Math. Phys. 207 (1999), no. 3, 697-733, DOI 10.1007/s002200050743. MR1727234
[15] , A note on universality of the distribution of the largest eigenvalues in certain sample covariance matrices, J. Statist. Phys. 108 (2002), no. 5-6, 1033-1056, DOI 10.1023/A:1019739414239. Dedicated to David Ruelle and Yasha Sinai on the occasion of their 65th birthdays. MR1933444
[16] Ekaterina Vassilieva, Moments of normally distributed random matrices given by generating series for connection coefficients-explicit bijective computation, Ann. Comb. 21 (2017), no. 3, 445-477, DOI 10.1007/s00026-017-0356-y. MR3685122



