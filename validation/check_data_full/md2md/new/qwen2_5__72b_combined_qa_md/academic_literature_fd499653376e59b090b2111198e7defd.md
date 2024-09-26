# A recursion formula for mixed trace moments of isotropic Wishart matrices and the Gaussian unitary/orthogonal ensembles 

Ben Deitmar<br>Department of Mathematical Stochastics, ALU Freiburg<br>Ernst-Zermelo-Str. 1, 79104 Freiburg, Germany<br>E-mail: ben.deitmar@stochastik.uni-freiburg.de


#### Abstract

Exact recursion formulas for mixed moments of four fundamental random matrix ensembles are derived. The reason such recursive formulas are possible is closely related to properties of polygon gluings studied by Harer and Zagier as well as Akhmedov and Shakirov. The proofs of the formulas are direct and written in such a way that they do not rely on understanding of polygon gluings.


## 1 Introduction

Let $X$ be a $(p \times n)$ random matrix with iid standard normal entries and let $Y$ be a $(p \times n)$ random matrix with iid standard complex normal entries. Further let $Z$ be an $(n \times n)$ random hermitian matrix, where the entries $\left(Z_{i, j}\right)_{i \leq j}$ are independent and $Z_{i, i} \sim \mathcal{N}(0,1)$ for all $i \leq n$ as well as $Z_{i, j}=\overline{Z_{j, i}} \sim \mathcal{C N}(0,1)$ for all $i<j \leq n$. Similarly, let $\tilde{Z}$ be an $(n \times n)$ random symmetric matrix, where the entries $\left(\tilde{Z}_{i, j}\right)_{i \leq j}$ are independent and $\tilde{Z}_{i, i} \sim \mathcal{N}(0,2)$ for all $i \leq n$ as well as $\tilde{Z}_{i, j}=\tilde{Z}_{j, i} \sim \mathcal{N}(0,1)$ for all $i<j \leq n$. The matrices $\frac{1}{\sqrt{n}} Z$ and $\frac{1}{\sqrt{n}} \tilde{Z}$ are of the Gaussian unitary and Gaussian orthogonal ensemble respectively. The matrices $\frac{1}{n} X X^{T}$ and $\frac{1}{n} Y Y^{*}$ are real and complex isotropic Wishart matrices.

In this paper we give exact recursive formulas for mixed trace moments of the type

$$
\begin{aligned}
\mathbb{E}^{X}(\mathbf{l}) & :=\mathbb{E}\left[\prod_{k=1}^{K} \operatorname{tr}\left(\left(X X^{T}\right)^{l_{k}}\right)\right] \\
\mathbb{E}^{Y}(\mathbf{l}) & :=\mathbb{E}\left[\prod_{k=1}^{K} \operatorname{tr}\left(\left(Y Y^{*}\right)^{l_{k}}\right)\right]
\end{aligned}
$$

Supported by the DFG Research Unit 5381




---

and

$$
\mathrm{E} Z(\mathbf{l}):=\mathrm{E}\left[\prod_{k=1}^{K} \operatorname{tr}\left(\mathbf{Z}^{l_{k}}\right)\right], \quad \mathrm{E} \tilde{Z}(\mathbf{l}):=\mathrm{E}\left[\prod_{k=1}^{K} \operatorname{tr}\left(\tilde{\mathbf{Z}}^{l_{k}}\right)\right]
$$

for arbitrary $p, n, K \in \mathbb{N}$ and layouts $\mathbf{l}=\left(l_{1}, \ldots, l_{K}\right) \in \mathbb{N}_{0}^{K}$.
Assuming $l_{1}>0$, the formulas are as follows.

1) Gaussian unitary ensemble:

$$
\begin{aligned}
\mathrm{E}\left[\prod_{r=1}^{K} \operatorname{tr}\left(\mathbf{Z}^{l_{r}}\right)\right]= & \sum_{q=1}^{l_{1}-1} \mathrm{E}\left[\operatorname{tr}\left(\mathbf{Z}^{q-1}\right) \operatorname{tr}\left(\mathbf{Z}^{l_{1}-q-1}\right) \prod_{r=2}^{K} \operatorname{tr}\left(\mathbf{Z}^{l_{r}}\right)\right] \\
& +\sum_{k=2}^{K} l_{k} \mathrm{E}\left[\operatorname{tr}\left(\mathbf{Z}^{l_{1}+l_{k}-2}\right) \prod_{\substack{r=1 \\
r \neq k}}^{K} \operatorname{tr}\left(\mathbf{Z}^{l_{r}}\right)\right]
\end{aligned}
$$

For a complete formulation and proof see Theorem 2.1.
2) Gaussian orthogonal ensemble:

$$
\begin{aligned}
\mathrm{E}\left[\prod_{r=1}^{K} \operatorname{tr}\left(\tilde{\mathbf{Z}}^{l_{r}}\right)\right]= & \left(l_{1}-1\right) \mathrm{E}\left[\operatorname{tr}\left(\tilde{\mathbf{Z}}^{l_{1}-2}\right) \prod_{r=2}^{K} \operatorname{tr}\left(\tilde{\mathbf{Z}}^{l_{r}}\right)\right] \\
& +\sum_{q=1}^{l_{1}-1} \mathrm{E}\left[\operatorname{tr}\left(\tilde{\mathbf{Z}}^{q-1}\right) \operatorname{tr}\left(\tilde{\mathbf{Z}}^{l_{1}-q-1}\right) \prod_{r=2}^{K} \operatorname{tr}\left(\tilde{\mathbf{Z}}^{l_{r}}\right)\right] \\
& +2 \sum_{k=2}^{K} l_{k} \mathrm{E}\left[\operatorname{tr}\left(\tilde{\mathbf{Z}}^{l_{1}+l_{k}-2}\right) \prod_{\substack{r=1 \\
r \neq k}}^{K} \operatorname{tr}\left(\tilde{\mathbf{Z}}^{l_{r}}\right)\right]
\end{aligned}
$$

For a complete formulation and proof see Theorem 4.1.
3) Complex isotropic Wishart ensemble:

$$
\begin{aligned}
\mathrm{E}\left[\prod_{r=1}^{K} \operatorname{tr}\left(\left(\mathbf{Y} \mathbf{Y}^{*}\right)^{l_{r}}\right)\right]= & n \mathrm{E}\left[\operatorname{tr}\left(\left(\mathbf{Y} \mathbf{Y}^{*}\right)^{l_{1}-1}\right) \prod_{r=2}^{K} \operatorname{tr}\left(\left(\mathbf{Y Y}^{*}\right)^{l_{r}}\right)\right] \\
& +\sum_{q=1}^{l_{1}-1} \mathrm{E}\left[\operatorname{tr}\left(\left(\mathbf{Y} \mathbf{Y}^{*}\right)^{q}\right) \operatorname{tr}\left(\left(\mathbf{Y} \mathbf{Y}^{*}\right)^{l_{1}-q-1}\right) \prod_{r=2}^{K} \operatorname{tr}\left(\left(\mathbf{Y} \mathbf{Y}^{*}\right)^{l_{r}}\right)\right] \\
& +\sum_{k=2}^{K} l_{k} \mathrm{E}\left[\operatorname{tr}\left(\left(\mathbf{Y} \mathbf{Y}^{*}\right)^{l_{1}+l_{k}-1}\right) \prod_{\substack{r=1 \\
r \neq k}}^{K} \operatorname{tr}\left(\left(\mathbf{Y} \mathbf{Y}^{*}\right)^{l_{r}}\right)\right]
\end{aligned}
$$

For a complete formulation and proof see Theorem 3.1.




---

4) Real isotropic Wishart ensemble:

$$
\begin{aligned}
& \mathbb{E}\left[\prod_{r=1}^{K} \operatorname{tr}\left(\left(X X^{T}\right)^{l_{r}}\right)\right]=\left(n+l_{1}-1\right) \mathbb{E}\left[\operatorname{tr}\left(\left(X X^{T}\right)^{l_{1}-1}\right) \prod_{r=2}^{K} \operatorname{tr}\left(\left(X X^{T}\right)^{l_{r}}\right)\right] \\
& +\sum_{q=1}^{l_{1}-1} \mathbb{E}\left[\operatorname{tr}\left(\left(X X^{T}\right)^{q}\right) \operatorname{tr}\left(\left(X X^{T}\right)^{l_{1}-q-1}\right) \prod_{r=2}^{K} \operatorname{tr}\left(\left(X X^{T}\right)^{l_{r}}\right)\right] \\
& +2 \sum_{k=2}^{K} l_{k} \mathbb{E}\left[\operatorname{tr}\left(\left(X X^{T}\right)^{l_{1}+l_{k}-1}\right) \prod_{\substack{r=1 \\
r \neq k}}^{K} \operatorname{tr}\left(\left(X X^{T}\right)^{l_{r}}\right)\right]
\end{aligned}
$$

For a complete formulation and proof see Theorem 3.2.
The recursive formulas are proved in order of increasing difficulty, so Theorem 2.1 proves (1), Theorem 3.1 proves (3), Theorem 3.2 proves (4) and Theorem 4.1 proves (2).

The only random matrix ensembles for which explicit and non-recursive formulas for mixed moments are known are the Haar unitary and the Haar orthogonal ensembles. Diaconis and Evans found the explicit formulas in [4] under an assumption roughly equivalent to $n \geq l_{1}+\ldots+l_{K}$. Achieving non-recursive formulas for the ensembles studied here would prove extremely useful in the study of their spectral properties. For example the asymptotic behavior of

$$
\mathbb{E}\left[\operatorname{tr}\left(Z^{\left\lfloor t_{1} n^{\frac{2}{3}}\right\rfloor}\right) \cdots \operatorname{tr}\left(Z^{\left\lfloor t_{K} n^{\frac{2}{3}}\right\rfloor}\right)\right]
$$

is known to determine the behavior of the largest eigenvalue of $Z$ at the Tracy-Widom scale, which is why such mixed trace moments were already extensively studied in [10], [12], [13], [14] and [15]. The strong universality results therein imply that a non-recursive result in any of the four cases studied here would already yield a greater understanding of Tracy-Widom laws in much more general settings. The fact that Akhmedov and Shakirov were able to find a non-recursive formula to a similar, but still different recursion in [1] suggests that non-recursive solutions may be achievable.

Explicit formulas for the (non-mixed) singular trace moments $\mathbb{E}\left[\operatorname{tr}\left(Z^{2 m}\right)\right]$ as well as


For the singular trace moments in the GOE case $\mathbb{E}\left[\operatorname{tr}\left(\tilde{Z}^{2 m}\right)\right]$ a five-term recurrence relation is known thanks to M. Ledoux in [9].

The recursion from Theorem 2.1 for the GUE is not new, as it also follows from Section 5 in [6] by Harer and Zagier. We however still prove it as a precursor to Theorems 3.1, 3.2 and 4.1. The real Wishart case from Theorem 3.2 was already studied by Pielaszkiewicz,




---

Von Rosen and Singull in [11], though they made a minor error in their formula. To the best of our knowledge the results of Theorems 3.1 and 4.1 for the complex Wishart ensemble and the GOE respectively are entirely new.

# 1.1 Trace moments and polygon gluings 

There is a well-known link between trace moments of the GUE and the number of ways to glue to edges of a polygon together to receive an orientable surface of a given genus. This link was first described by Harer and Zagier in [6] to prove the recursive formula

$$
\begin{aligned}
& (m+1) E\left[\operatorname{tr}\left(Z^{2 m}\right)\right] \\
& \quad=(4 m-2) n E\left[\operatorname{tr}\left(Z^{2 m-2}\right)\right)+(m-1)(2 m-1)(2 m-3) E\left[\operatorname{tr}\left(Z^{2 m-4}\right)\right]
\end{aligned}
$$

which allows for the explicit representation

$$
E\left[\operatorname{tr}\left(Z^{2 m}\right)\right]=\frac{(2 m)!}{m!} \sum_{r=1}^{n \wedge(m+1)} \frac{\binom{n}{r}\binom{m}{r-1}}{2^{m+1-r}}
$$

These equalities were first found by Harer and Zagier and later simplified by Haagerup and Thorbjørnsen in [5], but the more readable formulation for (1.1) is from Theorem 1 in [9] by M. Ledoux, where he goes on to find an analogous recursion formula for $E\left[\operatorname{tr}\left(\tilde{Z}^{2 m}\right)\right]$ in the GOE case.

Akhmedov and Shakirov took this approach further in [1] by considering 'incomplete' gluings of a polygon such that the unglued edges form polygons of given lengths $\left(l_{1}, \ldots, l_{K}\right)$. They were able to give a recursive formula for the number of such incomplete gluings with a given genus (for a certain definition of genus). Unfortunately, although they were able to derive the explicit expression from their recursive formula, their results do not seem applicable to random matrix theory and their solution to a similar recursion does not seem applicable for solving the recursive formulas derived in this article.

In order to find formulas for mixed trace moments of the GUE for a layout $l=\left(l_{1}, \ldots, l_{K}\right)$, one instead would need to count the number of ways to glue the edges of multiple polygons $P_{l_{1}}, \ldots, P_{l_{K}}$ such that the resulting oriented surface is of a given genus. Here a possible pairing $\pi=\left\{\left\{e_{1}^{1}, e_{5}^{1}\right\},\left\{e_{2}^{1}, e_{1}^{2}\right\}, \ldots\right\}$ of edges for the gluing of $P_{8}, P_{5}, \ldots, P_{6}$ :





---

Euler's characteristic formula guarantees

$$
2-2 g=V-L / 2+K
$$

where $g$ is the genus of the resultant surface and $V$ is the number of vertices remaining in the ribbon graph determined by the pairing. Define $V_{L, K}(g)=2-2 g+\frac{L}{2}-K$ and

$$
g_{L, K}(V)=\frac{L}{4}+1-V+\frac{K}{2}
$$

Let $\varepsilon_{g}\left(l_{1}, \ldots, l_{K}\right)$ denote the number of different gluings/pairings of polygons $P_{l_{1}}, \ldots, P_{l_{K}}$ such that the resulting orientable surface is of genus $g$, then it is provable by Wick's Theorem (aka. Isserlis' Theorem) that

$$
E Z(\mathbf{l})=\sum_{g=0}^{\left\lfloor g_{L, K}(0)\right\rfloor} n^{V_{L, K}(g)} \varepsilon_{g}\left(l_{1}, \ldots, l_{K}\right)
$$

under the assumption $l_{1}, \ldots, l_{K}>0$.
A recursion formula for $E Z(\mathbf{l})$ can then be found by mapping such polygon gluings onto gluings of polygons with two less total edges. If the edge $e_{q}^{k}$ paired with $e_{1}^{1}$ is still part of the same polygon, i.e. $k=1$, then we can contract along the connection of the edges before removing both such that we are left with a gluing of polygons $P_{q-2}, P_{l_{1}-q}, P_{l_{2}}, \ldots, P_{l_{k}}$. Here a picture of what the above pairing would look like after removing $e_{1}^{1}$ and its paired edge $e_{5}^{1}$ :



The edges would of course have to be renamed and we have swapped the positions of the first two polygons such that the effects of contracting along the connection $\left\{e_{1}^{1}, e_{5}^{1}\right\}$ are more obvious.

Similarly, when the edge $e_{q}^{k}$ paired with $e_{1}^{1}$ is not in the first polygon, i.e. $k>1$, contraction along the pairing and removal of the two edges creates one new polygon $P_{l_{1}+l_{k}-2}$ from the two polygons $P_{l_{1}}$ and $P_{l_{k}}$. The rest of the pairing remains a valid gluing for the polygons $P_{l_{1}+l_{k}-2}, P_{2}, \ldots, \widehat{P_{l_{k}}}, \ldots, P_{l_{K}}$. Here an example before the contraction




---

and removal:



and after the contraction and removal:



This method of removing edges does not remove vertices of the ribbon graph, while it can happen that some of the new polygons are empty (i.e. they have length $l_{k}=0$ ). This only becomes a problem, if the first polygon is empty, since then there is no edge $e_{1}^{1}$ to use for the next recursive step of contraction and removal. We thus discard the first polygon, if it is empty. As this also constitutes a removal of an isolated vertex from the ribbon graph, we must keep a tally of how many vertices were removed this way. Luckily, in the recursive formula this tally is simply realized with an additional factor $n$. We have thus far heuristically argued the plausibility of Theorem 2.1.

# 1.2 Definition (Multigraphs by route) 

For a vertex set $V=[n]=\{1, \ldots, n\}$ and a give route $\mathbf{i}^{1} \in[n]^{m}$ we define the directed multi-graph $\mathcal{G}_{\mathbf{i}^{1}}=(V, E, f)$, with edge set $E=\left(e_{1}^{1}, \ldots, e_{m}^{1}\right)$ and

$$
f: E \rightarrow V \times V \quad ; \quad e_{q}^{1} \mapsto\left(i_{q}^{1}, i_{(q \bmod m)+1}^{1}\right)
$$

By construction the route $\mathbf{i}^{1}$ is an Euler path on $\mathcal{G}_{\mathbf{i}^{1}}$. Let $A\left(\mathcal{G}_{\mathbf{i}^{1}}\right) \in \mathbb{N}_{0}^{n \times n}$ denote the adjacency matrix of $\mathcal{G}_{\mathbf{i}^{1}}$, that is

$$
A_{v, w}\left(\mathcal{G}_{\mathbf{i}^{1}}\right)=\#\left\{e_{q}^{1} \in E \mid f\left(e_{q}^{1}\right)=(v, w)\right\}
$$

We can also define the undirected multi-graph $\tilde{\mathcal{G}}_{\mathbf{i}^{1}}=(V, E, \tilde{f})$ to a given route $\mathbf{i}^{1} \in[n]^{m}$ with the same edges, but ignorant of the edges direction. In this case we can define $\tilde{f}$ by

$$
\tilde{f}: E \rightarrow\{M \subset V \mid \# M \leq 2\} \quad ; \quad e_{q}^{1} \mapsto\left\{i_{q}^{1}, i_{(q \bmod m)+1}^{1}\right\}
$$




---

(If $\# f\left(e_{q}^{1}\right)=1$, the edge $e_{q}^{1}$ is a self-loop.) Again $A\left(\tilde{G}_{i_{1}}\right) \in \mathbb{N}_{0}^{n \times n}$ denotes the adjacency matrix of $\tilde{G}_{i_{1}}$, i.e.

$$
A_{v, w}\left(\tilde{G}_{i_{1}}\right)=\#\left\{e_{q}^{1} \in E \mid f\left(e_{q}^{1}\right)=\{v, w\}\right\}
$$

Note that for this definition of the adjacency matrix self-loops are only counted once.
For a sequence of routes $\mathbf{i}=\left(i_{1}, \ldots, i_{K}\right) \in \prod_{k=1}^{K}[n]^{l_{k}}$ define the joined adjacency matrices

$$
A(\mathbf{i}):=\sum_{k=1}^{K} A\left(G_{i_{k}}\right) ; \quad \tilde{A}(\mathbf{i}):=\sum_{k=1}^{K} A\left(\tilde{G}_{i_{k}}\right)
$$

In Section 3 the vertex set $V$ will be $[p+n]$, so we must exchange all above occurrences of $n$ with $p+n$.

# 2 Gaussian Unitary Ensemble 

### 2.1 Theorem (Recursion for mixed trace moments of the GUE)

For $K \in \mathbb{N}$ and any $\mathbf{l}=\left(l_{1}, \ldots, l_{K}\right) \in \mathbb{N}_{0}^{K}$ - with even $L:=l_{1}+\ldots+l_{K}$ - the following recursive properties hold.
a) If $l_{1}=0$, then $\mathbb{E} Z(\mathbf{l})=n \mathbb{E} Z\left(S_{0}(\mathbf{l})\right)$ for

$$
S_{0}\left(0, l_{2}, \ldots, l_{K}\right):=\left(l_{2}, \ldots, l_{K}\right)
$$

b) If $l_{1}>0$, then

$$
\mathbb{E} Z(\mathbf{l})=\sum_{q=1}^{l_{1}-1} \mathbb{E} Z\left(S_{2, q}(\mathbf{l})\right)+\sum_{k=2}^{K} l_{k} \mathbb{E} Z\left(S_{3, k}(\mathbf{l})\right)
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
\mathbb{E} Z(((),))=\mathbb{E}\left[\operatorname{tr}(Z)^{0}\right]=n
$$

for $(K, L)=(1,0)$ allows for the calculation of all mixed moments, when $L$ is even. When $L$ is odd, it is easy to see that the mixed trace moment must be zero.




---

Proof. The property (a) holds trivially, since the empty matrix product is here the $(n \times n)$ identity matrix. It remains to prove property (b).

For now assume $l_{1}, \ldots, l_{K}>0$, then expanding the sums in $\operatorname{tr}\left(Z^{l_{i}}\right)$ yields

$$
\mathbb{E} Z(\mathbf{l})=\sum_{\substack{i_{1} \in[n]^{l_{1}} \\ i K \in[n]^{K}}} \mathbb{E}\left[\prod_{k=1}^{K} Z_{i_{1}^{k}, i_{2}^{k}} \cdots Z_{i_{l_{k}-1}^{k}, i_{l_{k}}^{k}} Z_{i_{l_{k}}^{k}, i_{1}^{k}}\right]
$$

Extracting the first entries of each $i_{k}$ and summing over them first gives

$$
\mathbb{E} Z(\mathbf{l})=\sum_{b_{1}, \ldots, b_{K} \in[n]} \sum_{\forall k \leq K: i_{\forall} \in[n]^{l_{k}}}\left[\prod_{k=1}^{K} Z_{i_{1}^{k}, i_{2}^{k}} \cdots Z_{i_{l_{k}-1}^{k}, i_{i_{k}}^{k}} Z_{i_{l_{k}}^{k}, i_{1}^{k}}\right]
$$

For easier notation define

$$
I_{\mathbf{l}, \mathbf{b}}:=\left\{\mathbf{i}=\left(i_{1}, \ldots, i_{K}\right) \in \prod_{k=1}^{K}[n]^{l_{k}} \mid \forall k \leq K:\left(l_{k}>0 \Rightarrow i_{1}^{k}=b_{k}\right)\right\}
$$

then the above formula can be written as

$$
\mathbb{E} Z(\mathbf{l})=\sum_{b_{1}, \ldots, b_{K} \in[n]} \sum_{\mathbf{i} \in I_{\mathbf{l}, \mathbf{b}}} \mathbb{E}\left[\prod_{k=1}^{K} Z_{i_{1}^{k}, i_{2}^{k}} \cdots Z_{i_{l_{k}-1}^{k}, i_{l_{k}}^{k}} Z_{i_{l_{k}}^{k}, i_{1}^{k}}\right]
$$

The formula now also holds when some $l_{i}$ are zero, since then the summation over the corresponding $b_{i}$ brings the needed factors $n=\operatorname{tr}\left(Z^{0}\right)$.

Since complex standard normal random variables satisfy $\mathbb{E}\left[X^{a} X^{b}\right]=\mathbb{1}_{a=b} a$ ! and real standard normal random variables satisfy $\mathbb{E}\left[X^{a}\right]=\mathbb{1}_{a}$ even $(a-1)$ !! (with the convention $(-1)!!=1$ ), the mean in (2.4) has the form

$$
\begin{aligned}
& \mathbb{E}\left[\prod_{k=1}^{K} Z_{i_{1}^{k}, i_{2}^{k}} \cdots Z_{i_{l_{k}-1}^{k}, i_{l_{k}}^{k}} Z_{i_{l_{k}}^{k}, i_{1}^{k}}\right] \\
= & \mathbb{1}_{A(\mathbf{i}) \text { is symmetric }} \& \text { diag. entries even }\left(\prod_{\substack{v, w \in[n] \\
v<w}} A_{v, w}(\mathbf{i})!\right)\left(\prod_{v \in[n]}\left(A_{v, v}(\mathbf{i})-1\right)!!\right) \\
= & : W(A(\mathbf{i}))
\end{aligned}
$$

where $A(\mathbf{i}):=\sum_{k=1}^{K} A\left(G_{i_{k}}\right)$. Let $c:=i_{l_{1}}^{1}$ - here the assumption $l_{1}>0$ is needed - and define the symmetric matrix

$$
M_{b, c}:=\left(\mathbb{1}_{i=b, j=c}+\mathbb{1}_{i=c, j=b}\right)_{i, j \in[n]}
$$




---

For $c \neq b_{1}$, the above definition of $W\left(\mathbf{A}^{(\mathbf{i})}\right)$ then yields

$$
\begin{aligned}
W\left(\mathbf{A}^{(\mathbf{i})}\right) & =W\left(\mathbf{A}^{(\mathbf{i})}-M_{b_{1}, c}\right) A_{c, b_{1}}(\mathbf{i}) \\
& =W\left(\mathbf{A}^{(\mathbf{i})}-M_{b_{1}, c}\right)\left(A_{c, b_{1}}\left(G_{i^{1}}\right)+\sum_{s=2}^{K} A_{c, b_{1}}\left(G_{i^{s}}\right)\right)
\end{aligned}
$$

where $A_{c, b_{1}}(\mathbf{i})$ is at least 1, since it counts the number of occurrences of the connection $\left(i_{l_{1}}^{1}, i_{1}^{1}\right)=\left(c, b_{1}\right)$. The fact that $W(\mathbf{A})$ is zero as soon as $\mathbf{A}$ is not symmetric, allows us to swap $b_{1}$ and $c$ in arbitrary places of the formula, so we may also write

$$
W\left(\mathbf{A}^{(\mathbf{i})}\right)=W\left(\mathbf{A}^{(\mathbf{i})}-M_{b_{1}, c}\right)\left(A_{b_{1}, c}\left(G_{i^{1}}\right)+\sum_{s=2}^{K} A_{b_{1}, c}\left(G_{i^{s}}\right)\right)
$$

Similarly, when $c=b_{1}$, the weight satisfies

$$
\begin{aligned}
W\left(\mathbf{A}^{(\mathbf{i})}\right) & =W\left(\mathbf{A}^{(\mathbf{i})}-M_{b_{1}, b_{1}}\right) \underbrace{\left(A_{b_{1}, b_{1}}(\mathbf{i})-1\right)} \\
& =W\left(\mathbf{A}^{(\mathbf{i})}-M_{b_{1}, b_{1}}\right)\left(A_{b_{1}, b_{1}}\left(G_{i^{1}}\right)-1+\sum_{s=2}^{K} A_{b_{1}, b_{1}}\left(G_{i^{s}}\right)\right)
\end{aligned}
$$

and we can use these properties of the weight to decompose equality (2.4) into

$$
\begin{aligned}
& \mathbb{E} Z(l)= \\
& \underbrace{\sum_{\substack{b \in[n] K \\
c \in[n]}} \sum_{i \in \mathcal{I}_{l, b}} W\left(\mathbf{A}^{(\mathbf{i})}-M_{b_{1}, c}\right)\left(A_{b_{1}, c}\left(G_{i^{1}}\right)-\right.}_{=: \mathbb{E}_{1} Z(l)} \\
& \left.\mathbb{1}_{b_{1}=c}\right)+ \\
& \sum_{\substack{b \in[n] K \\
c \in[n]}} \sum_{\mathbf{i} \in \mathcal{I}_{l, \mathbf{b}}} \underbrace{W\left(\mathbf{A}^{(\mathbf{i})}-M_{b_{1}, c}\right) \sum_{s=2}^{K} A_{b_{1}, c}\left(G_{i^{s}}\right)}_{\left.i_{1}^{1}=c\right)} .
\end{aligned}
$$

For $\mathbb{E}_{\mathbb{Z}}^{1} Z(l)$ observe that $A_{b_{1}, c}\left(G_{i^{1}}\right)$ counts the number of occurrences of $\left(b_{1}, c\right)$ in $i^{1}=$ $\left(i_{1}^{1}, \ldots, i_{l_{1}}^{1}\right)$ and, if this number is $\mathbb{1}_{b_{1}=c}$, such an $\mathbf{i}$ will not contribute to $\mathbb{E}_{1} Z(l)$. Define

$$
Q_{b, c}^{1}\left(i^{1}\right)=\left\{q<l_{1} \mid i_{q}^{1}=b, i_{q+1}^{1}=c\right\}
$$

then $A_{b_{1}, c}\left(G_{i^{1}}\right)-\mathbb{1}_{b_{1}=c}=\# Q_{b_{1}, c}^{1}\left(i^{1}\right)$. For each $q \in Q_{b_{1}, c}^{1}\left(i^{1}\right)$ we give a unique way of splitting up $i^{1}$ into two new routes $\left\langle i^{1}\right\rangle_{q, 1}$ and $\left\langle i^{1}\right\rangle_{q, 2}$. Define

$$
\begin{array}{ll}
\left\langle i^{1}\right\rangle_{q, 1}:= & (\underbrace{i_{1}^{1}, \ldots, i_{q-1}^{1}}_{=b_{1}}) \in[n]^{q-1} \\
\left\langle i^{1}\right\rangle_{q, 2}:= & (\underbrace{i_{q+2}^{1}, \ldots, i_{l_{1}}^{1}}_{=c}) \in[n]^{l_{1}-q-1}
\end{array}
$$

and observe that when going from the multi-graph $G_{i^{1}}$ to $G_{\left\langle i^{1}\right\rangle_{q, 1}} \cup G_{\left\langle i^{1}\right\rangle_{q, 1}}$ we have only lost one edge in each direction (two edges without direction in the case of $b_{1}=c$ ) between the vertices $b_{1}$ and $c$ while all other edges remain. For

$$
J_{q}^{1}(\mathbf{i}):=\left(\left\langle i^{1}\right\rangle_{q, 1},\left\langle i^{1}\right\rangle_{q, 2}, i^{2}, \ldots, i^{K}\right)
$$




---

it follows that

$$
A\left(J_{q}^{1}(\mathbf{i})\right)=A(\mathbf{i})-M_{b_{1}, c}
$$

Since we sum over all choices of $c$ and all the other elements in $\mathbf{i}^{1}$, which were not specified can still be chosen freely, this for $\mathcal{E}_{l}^{1}$ implies

$$
\begin{aligned}
& \mathcal{E}_{Z}^{1}(\mathbf{l})=\sum_{\substack{c \in[n]}} \sum_{\substack{\mathbf{i} \in \mathcal{I}_{\mathbf{l}, \mathbf{b}} \\
i_{l_{1}}^{1}=c}} W\left(A\left(J_{q}^{1}(\mathbf{i})\right)\right) \\
& =\sum_{q=1}^{l_{1}-1} \sum_{\substack{c \in[n]}} \sum_{\substack{\mathbf{i} \in \mathcal{I}_{\mathbf{l}, \mathbf{b}} \\
i_{i_{1}}^{1}=c \\
q \in Q_{b_{1}, c}^{1}\left(\mathbf{i}^{1}\right)}} W\left(A\left(J_{q}^{1}(\mathbf{i})\right)\right) \\
& =\sum_{q=1}^{l_{1}-1} \sum_{\tilde{\mathbf{b}} \in[n]^{K+1}} \sum_{\mathbf{i} \in \mathcal{I}_{S_{2, q}(\mathbf{l}), \mathbf{\mathbf { b }}}} W(A(\mathbf{i})),
\end{aligned}
$$

where

$$
S_{2, q}(\mathbf{l}):=\left(q-1, l_{1}-q-1, l_{2}, \ldots, l_{K}\right)
$$

is defined in analogy to $J_{q}^{1}(\mathbf{i})$. We have thus shown

$$
\mathcal{E}_{Z}^{1}(\mathbf{l})=\sum_{q=1}^{l_{1}-1} \mathcal{E}_{Z}\left(S_{2, q}(\mathbf{l})\right)
$$

Next, for $\mathcal{E}_{Z}^{2}(\mathbf{l})$ observe that $\sum_{k=2}^{K} A_{b_{1}, c}\left(G \mathbf{i}^{k}\right)$ counts the number of occurrences of $\left(b_{1}, c\right)$ in

$$
\left(i_{1}^{2}, \ldots, i_{l_{2}}^{2}\right), \cdots,\left(i_{1}^{K}, \ldots, i_{l_{K}}^{K}\right)
$$

and define the set

$$
\begin{aligned}
Q_{b, c}^{2}(\mathbf{i}):=\{(k, q) \in\{2, \ldots, K\} \times \mathbb{N} \mid & q \leq l_{k} \text { and } \\
& \left.q<l_{k} \Rightarrow\left(i_{q}^{k}=b \wedge i_{q+1}^{k}=c\right), q=l_{k} \Rightarrow\left(i_{l_{k}}^{k}=b \wedge i_{1}^{k}=c\right)\right\}
\end{aligned}
$$

Again $\sum_{k=2}^{K} A_{b_{1}, c}\left(G \mathbf{i}^{k}\right)=\# Q_{b_{1}, c}^{2}(\mathbf{i})$ and this time for each $(k, q) \in Q_{b_{1}, c}^{2}(\mathbf{i})$ we give a unique way of joining the routes $\mathbf{i}^{1}$ and $\mathbf{i}^{k}$ into a new route

$$
\left\langle\mathbf{i}^{1}, \mathbf{i}^{k}\right\rangle_{q}:= \begin{cases}\left(i_{1}^{1}=b_{1}, \ldots, i_{l_{1}}^{1}=c, i_{q+2}^{k}, \ldots, i_{l_{k}}^{k}, \underbrace{i_{1}^{k}}_{=b_{k}}, \ldots, i_{q-1}^{k}\right) & \in[n]^{l_{1}+l_{s}-1} \\ \left(i_{1}^{1}=b_{1}, \ldots, i_{l_{1}}^{1}=c, i_{2}^{k}, \ldots, i_{l_{k}-1}^{k}\right) & \in[n]^{l_{1}+l_{s}-1}\end{cases}
$$




---

Going from the multigraph $G_{i_{1}} \cup G_{i_{k}}$ to $G_{\left\langle i_{1}, i_{k}\right\rangle_{q}}$ we only loose one edge in each direction between the vertices $b_{1}$ and $c$ (two undirected edges in the case $b_{1}=c$ ) while all other edges remain. For

$$
J_{(k, q)}^{2}(\mathbf{i}):=\left(\left\langle i_{1}, i_{k}\right\rangle_{q}, i_{2} \ldots, \widehat{i_{k}}, \ldots, i_{K}\right)
$$

it follows that

$$
A\left(J_{(k, q)}^{2}(\mathbf{i})\right)=A(\mathbf{i})-M_{b_{1}, c}
$$

and similarly to (2.10) we get

$$
\begin{aligned}
E_{Z}^{2}(\mathbf{l}) & =\sum_{\substack{b \in[n]^{K} \\
c \in[n]}} \sum_{\mathbf{i} \in I_{\mathbf{l}, \mathbf{b}}} \sum_{(k, q) \in \mathcal{Q}_{b_{1}, c}^{2}} A\left(J_{(k, q)}^{2}(\mathbf{i})\right) \\
& =\sum_{k=2}^{K} \sum_{q=1}^{l_{k}} \sum_{\substack{b \in[n]^{K} \\
c \in[n]}} \sum_{\substack{\mathbf{i} \in I_{\mathbf{l}, \mathbf{b}} \\
i_{1}=l_{1}=c}} A\left(J_{(k, q)}^{2}(\mathbf{i})\right) \\
& =\sum_{k=2}^{K} \sum_{q=1}^{l_{k}} \sum_{\tilde{\mathbf{b}} \in[p]^{K-1}} \sum_{\mathbf{i} \in I_{S_{3, k}(\mathbf{l}), \tilde{\mathbf{b}}}} A(\mathbf{i}) \\
& =\sum_{k=2}^{K} \sum_{r=1}^{l_{k}} E Z\left(S_{3, k}(\mathbf{l})\right)=\sum_{k=2}^{K} l_{k} E Z\left(S_{3, k}(\mathbf{l})\right)
\end{aligned}
$$

where

$$
S_{3, k}(\mathbf{l}):=\left(l_{1}+l_{k}-2, l_{2}, \ldots, \widehat{l_{k}}, \ldots, l_{K}\right)
$$

is defined in analogy to $J_{(k, q)}^{2}$.
Equalities (2.7), (2.11) and (2.14) together show

$$
E Z(\mathbf{l})=\sum_{q=1}^{l_{1}-1} E Z\left(S_{2, q}(\mathbf{l})\right)+\sum_{k=2}^{K} l_{k} E Z\left(S_{3, k}(\mathbf{l})\right)
$$

2.2 Remark (Translation to polygon gluings)

In terms of $\varepsilon_{g}(\mathbf{l})$ from (1.3) the recursion can be written as

$$
\sum_{g=0}^{\left\lfloor\frac{L-K}{2}\right\rfloor} n_{V_{L, K}}(g) \varepsilon_{g}(\mathbf{l})
$$




---

$$
=\sum_{q=1}^{l_{1}-1} \sum_{g=0}^{\left\lfloor g_{L-2, K+1}(0)\right\rfloor} n_{V_{L-2, K+1}(g)} \varepsilon_{g}\left(S_{2, q}(\mathbf{l})\right)+\sum_{k=2}^{K} l_{k} \sum_{g=0}^{\left\lfloor g_{L-2, K-1}(0)\right\rfloor} n_{V_{L-2, K-1}(g)} \varepsilon_{g}\left(S_{3, k}(\mathbf{l})\right)
$$

With

$$
V_{L, K}(g)=2-2 g+\frac{L}{2}-K=V_{L-2, K+1}(g)=V_{L-2, K-1}(g-1)
$$

it implies

$$
\varepsilon_{g}(\mathbf{l})=\sum_{q=1}^{l_{1}-1} \varepsilon_{g}\left(S_{2, q}(\mathbf{l})\right)+\sum_{k=2}^{K} l_{k} \varepsilon_{g-1}\left(S_{3, k}(\mathbf{l})\right)
$$

when $l_{1}>0$, and $\varepsilon_{g}\left(0, l_{2}, \ldots, l_{K}\right)=\varepsilon_{g}\left(l_{2}, \ldots, l_{K}\right)$ otherwise.

# 3 Wishart Ensemble 

For ease of notation in the following proofs we write the matrices $X$ and $Y$ as

$$
X=: \overline{\left(X_{i, j}\right)}_{i \in[p], j \in[p+n] \backslash[p]} \text { and } Y=: \overline{\left(Y_{i, j}\right)}_{i \in[p], j \in[p+n] \backslash[p]}
$$

### 3.1 Theorem (Recursion for mixed trace moments of complex isotropic Wishart matrices)

For $K \in \mathbb{N}$ and any $\mathbf{l}=\left(l_{1}, \ldots, l_{K}\right) \in \mathbb{N}_{0}^{K}$ the following recursive properties hold.
a) If $l_{1}=0$, then $\mathbb{E}_{Y}(\mathbf{l})=p \mathbb{E}_{Y}\left(S_{0}(\mathbf{l})\right)$ for

$$
S_{0}\left(0, l_{2}, \ldots, l_{K}\right):=\left(l_{2}, \ldots, l_{K}\right)
$$

b) If $l_{1}>0$, then

$$
\mathbb{E}_{Y}(\mathbf{l})=n \mathbb{E}_{Y}\left(S_{1}(\mathbf{l})\right)+\sum_{r=1}^{l_{1}-1} \mathbb{E}_{Y}\left(S_{2, r}(\mathbf{l})\right)+\sum_{k=2}^{K} l_{k} \mathbb{E}_{Y}\left(S_{3, l_{k}}(\mathbf{l})\right)
$$

where

$$
\begin{aligned}
S_{1}(\mathbf{l}) & :=\left(l_{1}-1, l_{2}, \ldots, l_{K}\right) \\
S_{2, r}(\mathbf{l}) & :=\left(r, l_{1}-r-1, l_{2}, \ldots, l_{K}\right) \\
S_{3, k, q}(\mathbf{l}) & :=\left(l_{1}+l_{k}-1, l_{2}, \ldots, \widehat{l_{k}}, \ldots, l_{K}\right)
\end{aligned}
$$

Since (a) reduces $K$ by one and (b) reduces $L:=\sum_{k=1}^{K} l_{k}$ by one, the end point

$$
\mathbb{E}_{Y}(()(,))=\mathbb{E}\left[\operatorname{tr}\left(\left(Y Y^{*}\right)^{0}\right)\right]=p
$$

for $(K, L)=(1,0)$ allows for the calculation of all mixed moments.




---

Proof. The property (a) holds trivially, since the empty matrix product is here the $(p \times p)$ identity matrix. The proof of property (b) will take most of the section.

For now assume $l_{1}, \ldots, l_{K}>0$, then by expanding the sums in $\operatorname{tr}\left(S^{l_{i}}\right)$ we see

$$
\mathbb{E} Y(\mathbf{l})=\sum_{\substack{i_{1} \in \mathcal{B}_{p, n, l_{1}} \\ i_{K} \in \mathcal{B}_{p, n, l_{K}}}} \mathbb{E}\left[\prod_{k=1}^{K}\left(Y_{i_{1}^{k}, i_{2}^{k}} Y_{i_{3}^{k}, i_{2}^{k}}\right) \cdots\left(Y_{i_{2 l_{k}-1}^{k}, i_{2 l_{k}}^{k}} Y_{i_{1}^{k}, i_{2 l_{k}}^{k}}\right)\right]
$$

where

$$
\mathcal{B}_{p, n, l}:=\left\{\left(i_{1}, \ldots, i_{2 l}\right) \in \mathbb{N}^{2 l} \mid\left\{i_{1}, i_{3}, \ldots, i_{2 l-1}\right\} \in[p],\left\{i_{2}, i_{4}, \ldots, i_{2 l}\right\} \in[p+n] \backslash[p]\right\}
$$

Extracting the first entries of each $\mathbf{i}_{k}$ and summing over them first yields

$$
\mathbb{E} Y(\mathbf{l})=\sum_{b_{1}, \ldots, b_{K} \in[p]} \sum_{\substack{i_{1} \in \mathcal{B}_{p, n, l_{1}} \\ i_{K} \in \mathcal{B}_{p, n, l_{K}} \\ \forall k \leq K: i_{1}^{k}=b_{k}}} \mathbb{E}\left[\prod_{k=1}^{K}\left(Y_{i_{1}^{k}, i_{2}^{k}} Y_{i_{3}^{k}, i_{2}^{k}}\right) \cdots\left(Y_{i_{2 l_{k}-1}^{k}, i_{2 l_{k}}^{k}} Y_{i_{1}^{k}, i_{2 l_{k}}^{k}}\right)\right]
$$

For ease of notation define

$$
\mathcal{B}_{\mathbf{l}, \mathbf{b}}:=\left\{\mathbf{i}=\left(\mathbf{i}_{1}, \ldots, \mathbf{i}_{K}\right) \in \underset{k=1}{\stackrel{K}{\times}} \mathcal{B}_{p, n, l_{k}} \mid \forall k \leq K:\left(l_{k}>0 \Rightarrow i_{1}^{k}=b_{k}\right)\right\}
$$

then the above formula for $\mathbb{E} Y(\mathbf{l})$ becomes

$$
\mathbb{E} Y(\mathbf{l})=\sum_{b_{1}, \ldots, b_{K} \in[p]} \sum_{\mathbf{i} \in \mathcal{B}_{\mathbf{l}, \mathbf{b}}} \mathbb{E}\left[\prod_{k=1}^{K}\left(Y_{i_{1}^{k}, i_{2}^{k}} Y_{i_{3}^{k}, i_{2}^{k}}\right) \cdots\left(Y_{i_{2 l_{k}-1}^{k}, i_{2 l_{k}}^{k}} Y_{i_{1}^{k}, i_{2 l_{k}}^{k}}\right)\right]
$$

Just as (2.4) in the GUE case, this formula now also holds for any $l_{1}, \ldots, l_{K} \in \mathbb{N}_{0}^{K}$. This time the mean is seen to have the form

$$
\mathbb{E}\left[\prod_{k=1}^{K} Y_{i_{1}^{k}, i_{2}^{k}} Y_{i_{3}^{k}, i_{2}^{k}} \cdots Y_{i_{2 l_{k}-1}^{k}, i_{i_{k}}^{k}} Y_{i_{1}^{k}, i_{2 l_{k}}^{k}}\right]=\frac{1_{A(\mathbf{i}) \text { is symmetric }}}{\prod_{\substack{v \in[p] \\ w \in[p+n] \backslash[p]}} A_{v, w}(\mathbf{i})!}=: W(A(\mathbf{i}))
$$

where again $A(\mathbf{i}):=\sum_{k=1}^{K} A\left(G_{\mathbf{i}_{k}}\right)$. Let $c:=i_{2 l_{1}}^{1}$ and define the symmetric matrix

$$
M_{b, c}:=\left(1_{i=b, j=c \text { or } i=c, j=b}\right)_{i, j \in[p+n]}
$$




---

With the very same argument as the one leading up to (2.7) - except that this time only the case $b_{1} \neq c$ is needed - we can decompose equality (3.5) into

$$
\begin{aligned}
\mathrm{E}_{Y}(l)= & \overbrace{\sum_{\substack{b \in[p] K \\
c \in[p+n] \backslash[p]}} \sum_{i \in B_{l, b}} W\left(A(i)-M_{b_{1}, c}\right) A_{b_{1}, c}\left(G_{i^{1}}\right)}^{=: E_{Y}^{1}(l)} \\
& +\sum_{\substack{b \in[p] K \\
c \in[p+n] \backslash[p]}} \sum_{i \in B_{l, b}} W\left(A(i)-M_{b_{1}, c}\right) \underbrace{\sum_{s=k}^{K} A_{b_{1}, c}\left(G_{i^{k}}\right)}_{i_{1}^{1}=c}
\end{aligned}
$$

For $E_{Y}^{1}(l)$ observe that $A_{b_{1}, c}\left(G_{i^{1}}\right)$ counts the number of occurrences of $\left(b_{1}, c\right)$ in $i^{1}=$ $\left(i_{1}^{1}, \ldots, i_{2 l^{1}}^{1}\right)$ and, if this number is zero, such an $i$ will not contribute to $E_{l}^{1}$. Define

$$
Q_{b, c}^{1}\left(i^{1}\right)=\left\{q<2 l^{1} \mid i_{q}^{1}=b, i_{q+1}^{1}=c\right\}
$$

then clearly $A_{b_{1}, c}\left(G_{i^{1}}\right)=\# Q_{b_{1}, c}^{1}\left(i^{1}\right)$ and by the bipartite definition of $B_{p, n, l^{1}}$ all elements in $Q_{b, c}^{1}\left(i^{1}\right)$ must be odd. For each $q \in Q_{b_{1}, c}^{1}\left(i^{1}\right)$ we give a unique way of splitting up $i^{1}$ into two new routes $\left\langle i^{1}\right\rangle_{q, 1}$ and $\left\langle i^{1}\right\rangle_{q, 2}$. Define

$$
\begin{aligned}
& \left\langle i^{1}\right\rangle_{q, 1}:=\underbrace{\left(i_{q+2}^{1}, \ldots, \underbrace{i_{2 l^{1}}^{1}}_{=c}\right)}_{\in B_{p, n, l^{1}-\frac{q+1}{2}}} \\
& \left\langle i^{1}\right\rangle_{q, 2}:=\underbrace{\left(\underbrace{i_{1}^{1}}_{=b_{1}}, \ldots, i_{q-1}^{1}\right)}_{\in B_{p, n, \frac{q-1}{2}}}
\end{aligned}
$$

and observe that between the multi-graphs $G_{i^{1}}$ and $G_{\left\langle i^{i}\right\rangle_{q, 1}} \cup G_{\left\langle i^{1}\right\rangle_{q, 1}}$ we have only lost one edge in each direction between the vertices $b_{1}$ and $c$ while all other edges remain. For

$$
J_{q}^{1}(i):=\left(\left\langle i^{1}\right\rangle_{q, 1},\left\langle i^{1}\right\rangle_{q, 2}, i^{2}, \ldots, i^{K}\right)
$$

it follows that

$$
A\left(J_{q}^{1}(i)\right)=A(i)-M_{b_{1}, c}
$$

Since we sum over all choices of $c$ and all the other elements in $i^{1}$, which were not specified can still be chosen freely according the rules of $B_{l, b}$, this for $E_{l}^{1}$ implies

$$
\begin{aligned}
E_{Y}^{1}(l) & =\sum_{b \in[p] K} \sum_{c \in[p+n] \backslash[p]} \sum_{i \in B_{l, b}} \sum_{q \in Q_{b_{1}, c}^{1}\left(i^{1}\right)} i_{1}^{1}=c \\
& =\sum_{q=1 \text { odd }}^{2 l^{1}-1} \sum_{b \in[p]^{K}} \sum_{c \in[p+n] \backslash[p]} \sum_{i \in B_{l, b}} \sum_{q \in Q_{b_{1}, c}^{1}\left(i^{1}\right)} W\left(A\left(J_{q}^{1}(i)\right)\right)
\end{aligned}
$$




---

$$
\begin{aligned}
& =\sum_{r=0}^{l_{1}-1} \sum_{\substack{b \in[p]^{K} \\
b^{\prime} \in[p], \text { if } r>0}} \sum_{c \in[p+n] \backslash[p]} \sum_{j \in \mathrm{BS}_{2, r}(\boldsymbol{l}),\left(b^{\prime}, b_{1}, \ldots, b_{K}\right)} W\left(A^{(j)}\right) \\
& =\frac{n}{p} \sum_{\tilde{\mathbf{b}} \in[p]^{K+1}} \sum_{j \in \mathrm{BS}_{2,0}(\mathbf{l}), \tilde{\mathbf{b}}} W\left(A^{(j)}\right) \\
& +\sum_{r=1}^{l_{1}-1} \sum_{\tilde{\mathbf{b}} \in[p]^{K+1}} \sum_{j \in \mathrm{BS}_{2, r}(\mathbf{l}), \tilde{\mathbf{b}}} W\left(A^{(j)}\right) \\
& =n \mathbb{E}_{Y}\left(S_{1}(\mathbf{l})\right)+\sum_{r=1}^{l_{1}-1} \mathbb{E}_{Y}\left(S_{2, r}(\mathbf{l})\right)
\end{aligned}
$$

where

$$
\begin{aligned}
& S_{2, r}(\mathbf{l})=\left(r, l_{1}-r-1, l_{2}, \ldots, l_{K}\right) \text { is defined in analogy to } J_{q}^{1}(\boldsymbol{i}) \text { and } \\
& S_{1}(\mathbf{l})=\left(l_{1}-1, l_{2}, \ldots, l_{K}\right)
\end{aligned}
$$

The factor $n$ in the first summand comes from the summation over c, which no longer had an influence on the latter sum in the case $q=2 l_{1}-1 \Leftrightarrow r=0$. The temporary factor $\frac{1}{p}$ in the first summand was added and removed with the summation over $b^{\prime}=\tilde{b}_{1}$.

Next for $E_{Y}^{2}(\mathbf{l})$ observe that $\sum_{k=2}^{K} A_{b_{1}, c}\left(G_{i^{k}}\right)$ counts the number of occurrences of $\left(b_{1}, c\right)$ in

$$
\left(i_{1}^{2}, \ldots, i_{2 l_{2}}^{2}\right), \cdots,\left(i_{1}^{K}, \ldots, i_{2 l_{K}}^{K}\right)
$$

and define the set

$$
Q_{b, c}^{2}(\boldsymbol{i}):=\left\{(k, q) \in\{2, \ldots, K\} \times \mathbb{N} \mid i_{q}^{k}=b, i_{q+1}^{k}=c\right\}
$$

Again $\sum_{k=2}^{K} A_{b_{1}, c}\left(G_{i^{k}}\right)=\# Q_{b_{1}, c}^{2}$ and all tuples $(k, q) \in Q_{b, c}^{2}(\boldsymbol{i})$ must have odd $q$. This time for each $(k, q) \in Q_{b_{1}, c}^{2}(\boldsymbol{i})$ we give a unique way of joining the routes $\boldsymbol{i}^{1}$ and $\boldsymbol{i}^{k}$ into a new route

$$
\begin{gathered}
\left\langle\boldsymbol{i}^{1}, \boldsymbol{i}^{k}\right\rangle_{q}:=\left(\underbrace{i_{1}^{k}, \ldots, i_{q-1}^{k}, \underbrace{i_{1}^{1}}_{=b_{1}}, \ldots, \underbrace{i_{2 l_{1}}^{1}}_{=c}, i_{q+2}^{k}, \ldots, i_{2 l_{k}}^{k}}_{=b_{k}}\right) \\
\in B_{p, n, l_{1}+l_{s}-1}
\end{gathered}
$$

Again we between the multigraphs $G_{i^{1}} \cup G_{i^{k}}$ and $G_{\left\langle i^{1}, i^{k}\right\rangle_{q}}$ only loose one edge in each direction between the vertices $b_{1}$ and $c$ while all other edges remain. For

$$
J_{(k, q)}^{2}(\boldsymbol{i}):=\left(\left\langle\boldsymbol{i}^{1}, \boldsymbol{i}^{k}\right\rangle_{q,,}, \boldsymbol{i}^{2} \ldots, \widehat{\boldsymbol{i}^{k}}, \ldots, \boldsymbol{i}^{K}\right)
$$




---

it follows that

$$
A\left(J_{(k, q)}^{2}(i)\right)=A(i)-M_{b_{1}, c}
$$

and similarly to (2.14) we get

$$
\begin{array}{r}
E_{Y}^{2}(l)=\sum_{b \in[p]^{K}} \sum_{c \in[p+n] \backslash[p]} \sum_{i \in B_{i_{1}}^{l, b}}^{2} \sum_{\substack{i_{2}=c}} \sum_{r=\frac{q+1}{2}}^{A\left(J_{(k, q)}^{2}(i)\right)}=\sum_{k=2}^{K} \sum_{r=1}^{l_{k}} \sum_{\tilde{b} \in[p]^{K-1}} \sum_{i \in B^{S_{3, k}(l), y, \tilde{b}}} A(i, j)= \\
\sum_{k=2}^{K} l_{k} E_{Y}\left(S_{3, k}(l)\right)
\end{array}
$$

where

$$
S_{3, k}(l):=\left(l_{1}+l_{k}-1, l_{2}, \ldots, \widehat{l_{k}}, \ldots, l_{K}\right)
$$

is defined in analogy to $J_{k, 2 r-1}^{2}$.
Equalities (3.8), (3.11) and (3.14) together show

$$
E_{Y}(l)=n E_{Y}\left(S_{1}(l)\right)+\sum_{r=1}^{l_{1}-1} E_{Y}\left(S_{2, r}(l)\right)+\sum_{k=2}^{K} l_{k} E_{Y}\left(S_{3, l_{k}}(l)\right)
$$

# 3.2 Theorem (Recursion for mixed trace moments of real isotropic Wishart matrices) 

For $K \in \mathbb{N}$ and any $l=\left(l_{1}, \ldots, l_{K}\right) \in \mathbb{N}_{0}^{K}$ the following recursive properties hold.
a) If $l_{1}=0$, then $E_{Y}(l)=p E_{Y}\left(S_{0}(l)\right)$ for $S_{0}\left(0, l_{2}, \ldots, l_{K}\right):=\left(l_{2}, \ldots, l_{K}\right)$.
b) If $l_{1}>0$, then

$$
E_{X}(l)=\left(n+l_{1}-1\right) E_{X}\left(S_{1}(l)\right)+\sum_{r=1}^{l_{1}-1} E_{X}\left(S_{2, r}(l)\right)+2 \sum_{k=2}^{K} l_{k} E_{X}\left(S_{3, k}(l)\right)
$$

where $S_{1}, S_{2, q}$ and $S_{3, k}$ are as defined in Theorem 3.1. Again the end point

$$
E_{X}((()))=\mathbb{E}\left[\operatorname{tr}\left(\left(X X^{T}\right)^{0}\right)\right]=p
$$

for $(K, L)=(1,0)$ allows for the calculation of all mixed moments.




---

Proof. In complete analogy to the proof of Theorem 3.1 know (a) to hold and for the proof of (b) in the case $l_{1}>0$ have

$$
\mathbb{E} X(\boldsymbol{l})=\sum_{b_{1}, \ldots, b_{K} \in[p]} \sum_{i \in B_{\boldsymbol{l}, b}} \mathbb{E}\left[\prod_{k=1}^{K}\left(X_{i_{1, i_{2}^{k}} i_{3, i_{2}^{k}}}\right) \cdots\left(X_{i_{2}^{k} l_{k}-1, i_{2}^{k} l_{k}} X_{i_{1, i_{2}^{k} l_{k}}}\right)\right]
$$

for any $l_{1}, \ldots, l_{K} \in \mathbb{N}_{0}^{K}$. The weight is instead

$$
\mathbb{E}\left[\prod_{k=1}^{K} X_{i_{1, i_{2}^{k}} i_{3, i_{2}^{k}}} \cdots X_{i_{2}^{k} l_{k}-1, i_{2}^{k} l_{k}} X_{i_{1, i_{2}^{k} l_{k}}}\right]=\left(\bigwedge_{\tilde{A}(\boldsymbol{i}) \text { has even entries }} \prod_{\substack{v \in[p] \\ w \in[p+n] \backslash[p]}}\left(\tilde{A}_{v, w}(\boldsymbol{i})-1\right)\right) !=: W(\tilde{A}(\boldsymbol{i}))
$$

where $\tilde{A}(\boldsymbol{i})=\sum_{k=1}^{K} A\left(\tilde{G}_{\boldsymbol{i}^{k}}\right)$. Let $c:=i_{2 l_{1}}^{1}$ and define the matrix

$$
\tilde{M}_{b, c}:=2\left(\mathbb{1}_{i=b, j=c \text { or } i=c, j=b}\right)_{i, j \in[p+n]}
$$

By the definition of the weight $W(\tilde{A}(\boldsymbol{i}))$ it for all $\boldsymbol{i} \in B_{l, b}$ with $\tilde{A}(\boldsymbol{i})_{b_{1}, c} \geq 2$ follows that

$$
\begin{aligned}
W(\tilde{A}(\boldsymbol{i})) & =W\left(\tilde{A}(\boldsymbol{i})-\tilde{M}_{b_{1}, c}\right)\left(\tilde{A}(\boldsymbol{i})_{b_{1}, c}-1\right) \\
& =W\left(\tilde{A}(\boldsymbol{i})-\tilde{M}_{b_{1}, c}\right)\left(A_{b_{1}, c}\left(\tilde{G}_{\boldsymbol{i}^{1}}\right)-1+\sum_{k=2}^{K} A_{b_{1}, c}\left(\tilde{G}_{\boldsymbol{i}^{k}}\right)\right)
\end{aligned}
$$

Again this can be used to decompose equality (3.15) into

$$
\begin{aligned}
\mathbb{E} X(\boldsymbol{l})= & \underbrace{\sum_{\substack{b \in[p] \\
c \in[p+n] \backslash[p]}} \sum_{\substack{\boldsymbol{i} \in B_{l, b} \\
i_{l_{1}}^{1}=c}} W\left(\tilde{A}(\boldsymbol{i})-\tilde{M}_{b_{1}, c}\right)\left(A_{b_{1}, c}\left(\tilde{G}_{i^{1}}\right)-1\right)}_{=: \mathbb{E}_{1} X(\boldsymbol{l})} \\
& +\underbrace{\sum_{\substack{b \in[p]^{K} \\
c \in[p+n] \backslash[p]}} \sum_{\substack{\boldsymbol{i} \in B_{l, b} \\
i_{2 l_{1}}^{1}=c}} W\left(\tilde{A}(\boldsymbol{i})-\tilde{M}_{b_{1}, c}\right) \sum_{k=2}^{K} A_{b_{1}, c}\left(\tilde{G}_{i^{k}}\right)}_{=: \mathbb{E}_{2} X(\boldsymbol{l})}
\end{aligned}
$$

since all $\boldsymbol{i} \in B_{\boldsymbol{l}, \boldsymbol{b}}$ contributing to the sum must satisfy $\tilde{A}(\boldsymbol{i})_{b_{1}, c} \geq 2$. Define

$$
\begin{aligned}
& Q_{b, c}^{0}\left(i^{1}\right)=\left\{q<2 l_{1} \mid i_{q}^{1}=c, i_{q+1}^{1}=b\right\} \\
& Q_{b, c}^{1}\left(i^{1}\right)=\left\{q<2 l_{1} \mid i_{q}^{1}=b, i_{q+1}^{1}=c\right\}=Q_{c, b}^{0}(\boldsymbol{i})
\end{aligned}
$$




---

then $A_{b_{1}, c}\left(\tilde{G} i^{1}\right)^{-1}=\# Q_{b_{1}, c}^{0}\left(i^{1}\right)+\# Q_{b_{1}, c}^{1}\left(i^{1}\right)$ and by construction all elements of $Q_{b_{1}, c}^{0}\left(i^{1}\right)$ must be even and all elements of $Q_{b_{1}, c}^{1}\left(i^{1}\right)$ must be odd. For each $q \in Q_{b_{1}, c}^{1}\left(i^{1}\right)$ let $J_{q}^{1}(i)$ be just as in the proof of Theorem 3.1 and we also have $\tilde{A}\left(J_{q}^{1}(i)\right)=\tilde{A}(i)-\tilde{M}_{b_{1}, c}$. For each $q \in Q_{b_{1}, c}^{0}\left(i^{1}\right)$ let

$$
\left\langle i^{1}\right\rangle_{q}=(\underbrace{i_{1}^{1}, \ldots, i_{q-1}^{1}, \overbrace{i_{2 l_{1}}^{1}}^{i_{l}}, i_{2 l_{1}-1}^{1}, \ldots, i_{q+3}^{1}, i_{q+2}^{1}}_{=c} ) \in \mathcal{B}_{p, n, l_{1}-1}
$$

and

$$
J_{q}^{0}:=\left(\left\langle i^{1}\right\rangle_{q}, i^{2}, \ldots, i^{K}\right)
$$

then it also holds that $\tilde{A}\left(J_{q}^{0}(i)\right)=\tilde{A}(i)-\tilde{M}_{b_{1}, c}$ and we can similarly to (3.11) see

$$
\begin{aligned}
\mathbb{E}_{X}^{1}(\bar{l})= & \sum_{\substack{b \in[p]^{K} \\
c \in[p+n] \backslash[p]}} \sum_{\substack{i \in \mathcal{B}_{l, b} \\
i_{2 l_{1}}^{1}=c}}^{c} \sum_{q \in Q_{b_{1}, c}^{0}(i)} W\left(\tilde{A}\left(J_{q}^{0}(i)\right)\right) \\
& +\sum_{\substack{b \in[p]^{K} \\
c \in[p+n] \backslash[p]}} \sum_{\substack{i \in \mathcal{B}_{l, b} \\
i_{2 t_{1}}^{1}=c}} \sum_{q \in Q_{b_{1}, c}^{1}(i)} W\left(\tilde{A}\left(J_{q}^{1}(i)\right)\right)
\end{aligned}
$$

For the second summand the exact same steps as in (3.11) show that it must be equal to

$$
n \mathbb{E} X\left(S_{1}(\bar{l})\right)+\sum_{r=1}^{\bar{l}-1} \mathbb{E} X\left(S_{2, r}(\bar{l})\right)
$$

The first summand can likewise be calculated to be

$$
\begin{aligned}
& \sum_{q=2}^{2 l_{1}-2} \sum_{\substack{b \in[p]^{K} \\
c \in[p+n] \backslash[p]}} \sum_{\substack{i \in \mathcal{B}_{l, b} \\
i_{2 l_{1}}^{1}=c \\
q \in Q_{b_{1}, c}^{0}(i)}} W\left(\tilde{A}\left(J_{q}^{0}(i)\right)\right) \\
= & \left(l_{1}-1\right) \sum_{b \in[p]^{K}} \sum_{j \in \mathcal{B}_{S_{1}(\bar{l}), b}} W(\tilde{A}(j))=\left(l_{1}-1\right) \mathbb{E} X\left(S_{1}(\bar{l})\right)
\end{aligned}
$$

and we have shown

$$
\mathbb{E}_{X}^{1}(\bar{l})=\left(n+l_{1}-1\right) \mathbb{E} X\left(S_{1}(\bar{l})\right)+\sum_{r=1}^{l_{1}-1} \mathbb{E} X\left(S_{2, r}(\bar{l})\right)
$$

The same idea can be used to calculate $\mathbb{E}_{X}^{2}(\bar{l})$. First define

$$
Q_{b, c}^{2}(i)=\left\{(k, q) \in\{2, \ldots, K\} \times \mathbb{N} \mid q<2 l_{k}, i_{q}^{k}=b, i_{q+1}^{k}=c\right\}
$$




---

$$
\mathcal{Q}_{b, c}^{3}(\mathbf{i})=\left\{(k, q) \in\{2, \ldots, K\} \times \mathbb{N} \mid q \leq 2 l_{k}, i_{q}^{k}=c, i_{(q \bmod 2 l)}^{k}+1=b\right\}
$$

then again $\sum_{k=2}^{K} A_{b_{1}, c}\left(\tilde{G}_{i^{k}}\right)=\# \mathcal{Q}_{b_{1}, c}^{2}(\mathbf{i})+\# \mathcal{Q}_{b_{1}, c}^{3}(\mathbf{i})$ and all tuples $(k, q)$ from $\mathcal{Q}_{b, c}^{2}(\mathbf{i})$ must have odd $q$ while all tuples $(k, q)$ from $\mathcal{Q}_{b, c}^{3}(\mathbf{i})$ must have even q. For $J_{(k, q)}^{2}(\mathbf{i})$ as in the proof of Theorem 3.1, it holds that $\tilde{A}\left(J_{(k, q)}^{2}(\mathbf{i})\right)=\tilde{A}(\mathbf{i})-\tilde{M}_{b_{1}, c}$. Similarly for $(k, q) \in \mathcal{Q}_{b_{1}, c}^{3}(\mathbf{i})$ define

$$
\left[i^{1}, i^{k}\right]_{q}:= \begin{cases}\left(\overbrace{i_{1}^{1}, \ldots, i_{2 l_{1}}^{1}=c, i_{q}^{k}, i_{q-1}^{k}, \ldots, i_{1}^{k}, i_{2 l}^{k}=b, i_{2 l_{k}-1}^{k}, \ldots, i_{q+2}^{k}\right), \text { if } q<2 l_{k}\right. \\ \left(i_{1}^{1}=\overbrace{i_{2 l_{1}}^{1}=c, i_{2 l}^{k}, i_{2 l_{k}-1}^{k}, \ldots, i_{2}^{k}\right), \text { if } q=2 l_{k}\right.\end{cases}
$$

and

$$
J_{(k, q)}^{3}=\left(\left[i^{1}, i^{k}\right]_{q}, i^{2}, \ldots, \widehat{i^{k}}, \ldots, i^{K}\right)
$$

then we also have $\tilde{A}\left(J_{(k, q)}^{3}(\mathbf{i})\right)=\tilde{A}(\mathbf{i})-\tilde{M}_{b_{1}, c}$ and can further decompose $\mathcal{E}_{X}^{2}(l)$ into

$$
\begin{aligned}
\mathcal{E}_{X}^{2}(l)= & \sum_{\substack{b \in[p]^{K} \\
c \in[p K[p]}} \sum_{b \in B_{l, b}}^{i_{i_{1}}^{1}=c} \sum_{(k, q) \in Q_{b_{1}, c}^{2}(i)} W\left(\tilde{A}\left(J_{(k, q)}^{2}(\mathbf{i})\right)\right) \\
& +\sum_{\substack{b \in[p]^{K} \\
c \in[p+n] \backslash[p]}} \sum_{i \in B_{l, b}}^{i_{1}^{1}=c} \sum_{(k, q) \in \mathcal{Q}_{b_{1}, c}^{3}(i)} W\left(\tilde{A}\left(J_{(k, q)}^{3}(\mathbf{i})\right)\right)
\end{aligned}
$$

The first summand is by the same steps as in (3.14) equal to $\sum_{k=2}^{K} l_{k} \mathbb{E} X\left(S_{3, k}(l)\right)$. Note that $\left(k, 2 l_{k}\right) \in \mathcal{Q}_{b_{1}, c}^{3}$ is only possible, if $b_{k}=b_{1}$. This will ensure that we don't gain a factor of $n$ from the summation over $b_{k}$ in the case $q=2 l_{k}$ of the below calculation. The second summand is calculated to be

$$
\begin{aligned}
& \sum_{k=2}^{K} \sum_{q=2}^{2 l_{k}} \sum_{\substack{b \in(p]^{K} \\
c \in[p+n] \backslash[p}}} \sum_{\substack{i \in B_{l, b} \\
i_{1}^{1}=c \\
(k, q) \in \mathcal{Q}_{b_{1}, c}^{3}(i)}} W\left(\tilde{A}\left(J_{(k, q)}^{3}(\mathbf{i})\right)\right) \\
= & \sum_{k=2}^{K} \sum_{\substack{q=2 \\
\text { even }}}^{2 l_{k}} \sum_{\tilde{b} \in[p]^{K-1}} \sum_{j \in B_{S_{3, k}(l), \tilde{b}}} W(\tilde{A}(\mathbf{j})) \\
= & \sum_{k=2}^{K} l_{K} \mathbb{E} X\left(S_{3, k}(l)\right)
\end{aligned}
$$




---

and we have shown

$$
E_{2} X(\mathbf{l})=2 \sum_{k=2}^{K} l_{k} E X\left(S_{3, k}(\mathbf{l})\right)
$$

The equalities $(3.18),(3.22)$ and (3.26) together prove

$$
E X(\mathbf{l})=\left(n+l_{1}-1\right) E X\left(S_{1}(\mathbf{l})\right)+\sum_{r=1}^{l_{1}-1} E X\left(S_{2, r}(\mathbf{l})\right)+2 \sum_{k=2}^{K} l_{k} E X\left(S_{3, k}(\mathbf{l})\right)
$$

# 4 Gaussian Orthogonal Ensemble 

### 4.1 Theorem (Recursion for mixed trace moments of the GOE)

For $K \in \mathbb{N}$ and any $\mathbf{l}=\left(l_{1}, \ldots, l_{K}\right) \in \mathbb{N}_{0}^{K}$ - with even $L:=l_{1}+\ldots+l_{K}$ - the following recursive properties hold.
a) If $l_{1}=0$, then $E \tilde{Z}(\mathbf{l})=n E \tilde{Z}\left(S_{0}(\mathbf{l})\right)$ for

$$
S_{0}\left(0, l_{2}, \ldots, l_{K}\right):=\left(l_{2}, \ldots, l_{K}\right)
$$

b) If $l_{1}>0$, then

$$
E \tilde{Z}(\mathbf{l})=\left(l_{1}-1\right) E \tilde{Z}\left(S_{1}(\mathbf{l})\right)+\sum_{q=1}^{l_{1}-1} E \tilde{Z}\left(S_{2, q}(\mathbf{l})\right)+2 \sum_{k=2}^{K} l_{k} E \tilde{Z}\left(S_{3, k}(\mathbf{l})\right)
$$

where

$$
S_{1}(\mathbf{x}):=\left(l_{1}-2, l_{2}, \ldots, l_{K}\right)
$$

and $S_{2, q}$ as well as $S_{3, k}$ are as defined in Theorem 2.1.
As before in Theorem 2.1 the starting point

$$
E \tilde{Z}((,))=E\left[\operatorname{tr}(\tilde{Z})^{0}\right]=n
$$

for $(K, L)=(1,0)$ allows for the calculation of all mixed moments when $L$ is even and for odd $L$ the mixed trace moment must be zero.

Proof. Like before, only property (b) needs to be shown. In complete analogy to (2.4) we have

$$
E \tilde{Z}(\mathbf{l})=\sum_{b_{1}, \ldots, b_{K} \in[n]} \sum_{i \in I_{\mathbf{l}, \mathbf{b}}} E\left[\prod_{k=1}^{K} \tilde{Z}_{i_{1}^{k}, i_{2}^{k}} \ldots \tilde{Z}_{i_{l_{k}-1}^{k}, i_{l_{k}}^{k}} \tilde{Z}_{i_{l_{k}}^{k}, i_{1}^{k}}\right]
$$




---

This time the mean has the form

$$
\begin{aligned}
& \mathbb{E}\left[\prod_{k=1}^{K} \tilde{Z}_{i_{1}^{k}, i_{2}^{k}} \cdots \tilde{Z}_{i_{l_{k}-1}^{k}, i_{l_{k}}^{k}} \tilde{Z}_{i_{l_{k}}^{k}, i_{1}^{k}}\right] \\
& =\mathbb{1}_{\tilde{A}(\boldsymbol{i}) \text { has even entries }}\left(\prod_{\substack{v, w \in[n] \\
v<w}}\left(\tilde{A}_{v, w}(\boldsymbol{i})-1\right)!!\right)\left(\prod_{v \in[n]} \frac{2^{\tilde{A}_{v, v}(\boldsymbol{i})}}{2}\left(\tilde{A}_{v, v}(\boldsymbol{i})-1\right)!!\right) \\
& =: W(\tilde{A}(\boldsymbol{i}))
\end{aligned}
$$

which implies that it can with

$$
\tilde{M}_{b, c}:=2\left(\mathbb{1}_{i=b, j=c} \text { or } i=c, j=b\right)_{i, j \in[n]}
$$

be decomposed into

$$
\begin{aligned}
W(\tilde{A}(\boldsymbol{i})) & =W\left(\tilde{A}(\boldsymbol{i})-\tilde{M}_{b_{1}, c}\right) 2^{\mathbb{1}_{b_{1}=c}}\left(\tilde{A}_{b_{1}, c}(\boldsymbol{i})-1\right) \\
& =W\left(\tilde{A}(\boldsymbol{i})-\tilde{M}_{b_{1}, c}\right) 2^{\mathbb{1}_{b_{1}=c}}\left(A_{b_{1}, c}\left(\tilde{G}_{i_{1}}\right)-1+\sum_{k=2}^{K} A_{b_{1}, c}\left(\tilde{G}_{i_{k}}\right)\right)
\end{aligned}
$$

As is by now standard, we thus change (4.3) into

$$
\begin{aligned}
\mathbb{E} \tilde{Z}^{(l)}= & \overbrace{\sum_{\substack{b_{1}, \ldots, b_{K} \in[n] \\ c \in[n]} 2^{\mathbb{1}_{b_{1}=c}} \sum_{i \in I_{\underline{i_{1}}} \backslash b_{1}} l_{1}=c} W\left(\tilde{A}(\boldsymbol{i})-\tilde{M}_{b_{1}, c}\right)\left(A_{b_{1}, c}\left(\tilde{G}_{i_{1}}\right)-1\right)}^{\mathbb{E}_{1} \tilde{Z}^{(l)}} \\
& +\underbrace{\sum_{\substack{b_{1}, \ldots, b_{K} \in[n] \\
c \in[n]}} 2^{\mathbb{1}_{b_{1}=c}} \sum_{i \in I_{\xi} \backslash b}\left(\underline{i_{1}} l_{1}=c\right.}_{=: \mathbb{E}_{2} \tilde{Z}^{(l)}} W\left(\tilde{A}(\boldsymbol{i})-\tilde{M}_{b_{1}, c}\right) \sum_{k=2}^{K} A_{b_{1}, c}\left(\tilde{G}_{i_{k}}\right) .
\end{aligned}
$$

For

$$
\begin{aligned}
& Q_{b, c}^{0}\left(\underline{i_{1}}\right):=\left\{q<l_{1} \mid i_{q}^{1}=c, i_{q+1}^{1}=b\right\} \\
& Q_{b, c}^{1}\left(\underline{i_{1}}\right):=\left\{q<l_{1} \mid i_{q}^{1}=b, i_{q+1}^{1}=c\right\}=Q_{c, b}^{0}\left(\underline{i_{1}}\right)
\end{aligned}
$$

it holds that $2^{\mathbb{1}_{b_{1}=c}}\left(A_{b_{1}, c}\left(\tilde{G}_{i_{1}}\right)-1\right)=\# Q_{b_{1}, c}^{0}\left(\underline{i_{1}}\right)+\# Q_{b_{1}, c}^{1}\left(\underline{i_{1}}\right)$ and with $J_{q}^{1}(\boldsymbol{i})$ as in (2.9) we for each $q \in Q_{b_{1}, c}^{1}\left(\underline{i_{1}}\right)$ have

$$
\tilde{A}\left(J_{q}^{1}(\boldsymbol{i})\right)=\tilde{A}(\boldsymbol{i})-\tilde{M}_{b_{1}, c}
$$

For each $q \in Q_{b_{1}, c}^{0}\left(\underline{i_{1}}\right)$ we similarly to (3.21) define

$$
\left\langle\underline{i_{1}}\right\rangle_{q}=(\underbrace{i_{1}^{1}}_{=b_{1}}, \ldots, i_{q-1}^{1}, \underbrace{i_{l_{1}}^{1}}_{=c}, i_{l_{1}-1}^{1}, \ldots, i_{q+3}^{1}, i_{q+2}^{1}) \in[n]^{l_{1}-2}
$$




---

and

$$
J_{q}^{0}:=\left(\left\langle i^{1}\right\rangle_{q}, i^{2}, \ldots, i^{K}\right)
$$

then it also follows that $\tilde{A}\left(J_{q}^{0}(i)\right)=\tilde{A}(i)-\tilde{M}_{b 1, c}$, since only the connections between $\left(i_{q}^{1}, i_{q+1}^{1}\right)=(c, b)$ and $\left(i_{l_{1}}^{1}, i_{1}^{1}\right)=(c, b)$ are removed by $J_{q}^{0}$. Using $J^{0}$ and $J^{1}$ we write $\mathbb{E}_{\tilde{Z}}^{1}(\boldsymbol{l})$ as

$$
\begin{aligned}
\mathbb{E}_{\tilde{Z}}^{1}(\boldsymbol{l})= & \sum_{\substack{b_{1}, \ldots, b_{K} \in[n] \\
c \in[n]}} \sum_{\substack{i \in I_{\boldsymbol{l}, b} \\
i_{l_{1}}^{1}=c}} \sum_{q \in Q_{b_{1}, c}^{0}\left(i^{1}\right)} W\left(\tilde{A}\left(J_{q}^{0}\right)\right) \\
& +\sum_{\substack{b_{1}, \ldots, b_{K} \in[n] \\
c \in[n]}} \sum_{\substack{i \in I_{l, b} \\
i_{l_{1}}^{1}=c}} \sum_{q \in Q_{b_{1}, c}^{1}\left(i^{1}\right)} W\left(\tilde{A}\left(J_{q}^{1}\right)\right) .
\end{aligned}
$$

For the second summand the exact same steps as in (2.10) and (2.11) show that it must be equal to

$$
\sum_{q=1}^{l_{1}-1} \mathbb{E} \tilde{Z}\left(S^{2, q}(\boldsymbol{l})\right)
$$

Combining the ideas of (2.10) and (3.22) we for the first summand observe

$$
\begin{aligned}
\sum_{\substack{b_{1}, \ldots, b_{K} \in[n] \\
c \in[n]}} \sum_{\substack{i \in I_{l, b} \\
i_{l_{1}}^{1}=c}} \sum_{q \in Q_{b_{1}, c}^{0}\left(i^{1}\right)} W\left(\tilde{A}\left(J_{q}^{0}\right)\right) & =\sum_{q=1}^{l_{1}-1} \sum_{\substack{b_{1}, \ldots, b_{K} \in[n] \\
c \in[n]}} \sum_{\substack{i \in I_{l, b} \\
i_{l_{1}}^{1}=c \\
q \in Q_{b_{1}, c}^{0}\left(i^{1}\right)}} W\left(\tilde{A}\left(J_{q}^{0}\right)\right) \\
& =\left(l_{1}-1\right) \sum_{b_{1}, \ldots, b_{K} \in[n]} \sum_{j \in I_{S^{1}(\boldsymbol{l}), b}} W(\tilde{A}(j))=\left(l_{1}-1\right) \mathbb{E} \tilde{Z}\left(S^{1}(\boldsymbol{l})\right)
\end{aligned}
$$

where

$$
S^{1}(\boldsymbol{l}):=\left(l_{1}-2, l_{2}, \ldots, l_{K}\right)
$$

We have thus shown

$$
\mathbb{E}_{\tilde{Z}}^{1}(\boldsymbol{l})=\left(l_{1}-1\right) \mathbb{E} \tilde{Z}\left(S^{1}(\boldsymbol{l})\right)+\sum_{q=1}^{l_{1}-1} \mathbb{E} \tilde{Z}\left(S^{2, q}(\boldsymbol{l})\right)
$$

With analogous steps to those used for the proof of (3.26) we will now calculate $\mathbb{E}_{\tilde{Z}}^{2}(\boldsymbol{l})$. First define

$$
\begin{aligned}
Q_{b, c}^{2}(i) & :=\left\{(k, q) \in\{2, \ldots, K\} \times \mathbb{N} \mid q \leq l_{k}, i_{q}^{k}=b, i_{\left(q \bmod l_{k}\right)+1}^{k}=c\right\} \\
Q_{b, c}^{3}(i) & :=\left\{(k, q) \in\{2, \ldots, K\} \times \mathbb{N} \mid q \leq l_{k}, i_{q}^{k}=c, i_{\left(q \bmod l_{k}\right)+1}^{k}=b\right\}=Q_{c, b}^{2}(i)
\end{aligned}
$$




---

then we have $2 \mathbb{1}_{b_{1}=c} \sum_{k=2}^{K} A_{b_{1}, c}\left(\tilde{G}_{i_{k}}\right)=\# \mathcal{Q}_{b_{1}, c}^{2}(\mathbf{i})+\# \mathcal{Q}_{b_{1}, c}^{3}(\mathbf{i})$. For $\mathbf{J}_{(k, q)}^{2}(\mathbf{i})$ as in (2.13) it holds that $\tilde{A}\left(\mathbf{J}_{(k, q)}^{2}(\mathbf{i})\right)=\tilde{A}(\mathbf{i})-\tilde{M}_{b_{1}, c_{1}}$ and for each $(k, q) \in \mathcal{Q}_{b_{1}, c}^{3}(\mathbf{i})$ we similarly to (3.25) define

$$
\begin{gathered}
{\left[i_{1}, i_{k}\right]_{q}:= \begin{cases}(\overbrace{i_{1}^{1}, \ldots, \overbrace{i_{1}^{i_{1}}}^{b_{1}}}, i_{k}^{q}, i_{k}^{q-1}, \ldots, i_{k}^{1}, i_{k}^{l_{k}}, i_{k}^{l_{k-1}}, \ldots, i_{k}^{q+2}), \text { if } q<l_{k} \\
\left(\underbrace{i_{1}^{1}}_{c_{1}}, \ldots, i_{1}^{i_{1}}, i_{k}^{l_{k}}, i_{k}^{l_{k}-1}, \ldots, i_{k}^{2}\right), \text { if } q=l_{k}\end{cases}} \\
\text { and } \\
\mathbf{J}_{(k, q)}^{3}=\left(\left[i_{1}, i_{k}\right]_{q}, i_{2}, \ldots, \widehat{i_{k}}, \ldots, i_{K}\right)
\end{gathered}
$$

Again by construction of $\mathbf{J}^{3}$ it holds that $\tilde{A}\left(\mathbf{J}_{(k, q)}^{3}(\mathbf{i})\right)=\tilde{A}(\mathbf{i})-\tilde{M}_{b_{1}, c_{1}}$ and we can decompose $\mathbb{E}_{\tilde{Z}}^{2}(\underline{l})$ into

$$
\begin{aligned}
& \mathbb{E}_{\tilde{Z}}^{2}(\underline{l})=\sum_{\substack{b_{1}, \ldots, b_{K} \in[n] \\
c \in[n]}} \sum_{\substack{\mathbf{i} \in I_{\underline{l}, \underline{b}} \\
i_{1}^{l_{i}}=c}}^{b_{1}^{b_{1}}} \sum_{(k, q) \in \mathcal{Q}_{b_{1}, c}^{2}(\mathbf{i})} W\left(\tilde{A}\left(\mathbf{J}_{(k, q)}^{2}(\mathbf{i})\right)\right) \\
& +\sum_{\substack{b_{1}, \ldots, b_{K} \in[n] \\
c \in[n]}} \sum_{\substack{\mathbf{i} \in I_{\underline{i}, \mathbf{b}} \\
i_{1}^{l_{1}}=c}} \sum_{(k, q) \in \mathcal{Q}_{b_{1}, c}^{3}(\mathbf{i})} W\left(\tilde{A}\left(\mathbf{J}_{(k, q)}^{3}(\mathbf{i})\right)\right)
\end{aligned}
$$

The first summand is by the same steps as in (2.14) equal to

$$
\sum_{k=2}^{K} l_{k} \mathbb{E} \tilde{Z}\left(S_{3, k}(\underline{l})\right)
$$

and for the second summand the steps are again analogous to (2.14) and (3.26) and we find

$$
\begin{aligned}
& \sum_{\substack{b_{1}, \ldots, b_{K} \in[n] \\
c \in[n]}} \sum_{\substack{\mathbf{i} \in I_{l, \underline{b}} \\
i_{1}^{l_{1}}=c}} \sum_{(k, q) \in \mathcal{Q}_{b_{1}, c}^{3}(\mathbf{i})} W\left(\tilde{A}\left(\mathbf{J}_{(k, q)}^{3}(\mathbf{i})\right)\right) \\
= & \sum_{k=2}^{K} l_{k} \sum_{q=1} \sum_{\substack{b \in[n]^{K} \\
c \in[n]}} \sum_{\substack{\mathbf{i} \in I_{\underline{l}, \underline{b}} \\
i_{1}^{l_{1}}=c \\
(k, q) \in \mathcal{Q}_{b_{1}, \underline{c}}^{3}(\mathbf{i})}} W\left(\tilde{A}\left(\mathbf{J}_{(k, q)}^{3}(\mathbf{i})\right)\right) \\
= & \sum_{k=2}^{K} l_{k} \sum_{q=1} \sum_{\tilde{\mathbf{b}} \in[n]^{K-1}}^{K-1} \sum_{\mathbf{i} \in I_{l, \tilde{\mathbf{b}}}} W(\tilde{A}(\mathbf{j})) \\
= & \sum_{k=2}^{K} l_{k} \mathbb{E} \tilde{Z}\left(S_{3, k}(\underline{l})\right)
\end{aligned}
$$




---

so we have shown

$$
E_{\tilde{Z}}^{2}(\mathbf{l})=2 \sum_{k=2}^{K} l_{k} E \tilde{Z}\left(S_{3, k}(\mathbf{l})\right)
$$

Finally equalities (4.6), (4.10) and (4.14) together yield

$$
E \tilde{Z}(\mathbf{l})=\left(l_{1}-1\right) E \tilde{Z}\left(S_{1}(\mathbf{l})\right)+\sum_{q=1}^{l_{1}-1} E \tilde{Z}\left(S_{2, q}(\mathbf{l})\right)+2 \sum_{k=2}^{K} l_{k} E \tilde{Z}\left(S_{3, k}(\mathbf{l})\right)
$$

# List of symbols 





---





---

# REFERENCES 

[1] É. T. Akhmedov and Sh. R. Shakirov, Gluings of surfaces with polygonal boundaries, Funktsional. Anal. i Prilozhen. 43 (2009), no. 4, 3-13, DOI 10.1007/s10688-009-0033-y (Russian, with Russian summary); English transl., Funct. Anal. Appl. 43 (2009), no. 4, 245-253. MR2596651
[2] Greg W. Anderson, Alice Guionnet, and Ofer Zeitouni, An introduction to random matrices, Cambridge Studies in Advanced Mathematics, vol. 118, Cambridge University Press, Cambridge, 2010. MR2760897
[3] Olivier Bernardi, An analogue of the Harer-Zagier formula for unicellular maps on general surfaces, Adv. in Appl. Math. 48 (2012), no. 1, 164-180, DOI 10.1016/j.aam.2011.06.005. MR2845513
[4] Persi Diaconis and Steven N. Evans, Linear functionals of eigenvalues of random matrices, Trans. Amer. Math. Soc. 353 (2001), no. 7, 2615-2633, DOI 10.1090/S0002-9947-01-02800-8. MR1828463
[5] Uffe Haagerup and Steen Thorbjørnsen, Random matrices with complex Gaussian entries, Expo. Math. 21 (2003), no. 4, 293-337, DOI 10.1016/S0723-0869(03)80036-1. MR2022002
[6] J. Harer and D. Zagier, The Euler characteristic of the moduli space of curves, Invent. Math. 85 (1986), no. 3, 457-485, DOI 10.1007/BF01390325. MR848681
[7] D. M. Jackson, Some combinatorial problems associated with products of conjugacy classes of the symmetric group, J. Combin. Theory Ser. A 49 (1988), no. 2, 363-369, DOI 10.1016/00973165(88)90062-3. MR0964394
[8] Michel Ledoux and Brian Rider, Small deviations for beta ensembles, Electron. J. Probab. 15 (2010), no. 41, 1319-1343, DOI 10.1214/EJP.v15-798. MR2678393
[9] M. Ledoux, A recursion formula for the moments of the Gaussian orthogonal ensemble, Ann. Inst. Henri Poincaré Probab. Stat. 45 (2009), no. 3, 754-769, DOI 10.1214/08-AIHP184 (English, with English and French summaries). MR2548502
[10] Sandrine Péché, Universality results for the largest eigenvalues of some sample covariance matrix ensembles, Probab. Theory Related Fields 143 (2009), no. 3-4, 481-516, DOI 10.1007/s00440-0070133-7. MR2475670
[11] Jolanta Pielaszkiewicz, Dietrich Von Rosen, and Martin Singull, On $\mathrm{E}\left[\prod_{i=0}^{k} \operatorname{Tr}\left\{\mathbf{W}^{m_{i}}\right\}\right]$, where $\mathbf{W} \sim W_{p}(l, n)$, Comm. Statist. Theory Methods 46 (2017), no. 6, 2990-3005, DOI 10.1080/03610926.2015.1053942. MR3579781
[12] Ya. Sinai and A. Soshnikov, Central limit theorem for traces of large random symmetric matrices with independent matrix elements, Bol. Soc. Brasil. Mat. (N.S.) 29 (1998), no. 1, 1-24, DOI 10.1007/BF01245866. MR1620151
[13] Ya. G. Sinaĭ and A. B. Soshnikov, A refinement of Wigner's semicircle law in a neighborhood of the spectrum edge for random symmetric matrices, Funktsional. Anal. i Prilozhen. 32 (1998), no. 2, 5679, 96, DOI 10.1007/BF02482597 (Russian, with Russian summary); English transl., Funct. Anal. Appl. 32 (1998), no. 2, 114-131. MR1647832
[14] Alexander Soshnikov, Universality at the edge of the spectrum in Wigner random matrices, Comm. Math. Phys. 207 (1999), no. 3, 697-733, DOI 10.1007/s002200050743. MR1727234
[15] , A note on universality of the distribution of the largest eigenvalues in certain sample covariance matrices, J. Statist. Phys. 108 (2002), no. 5-6, 1033-1056, DOI 10.1023/A:1019739414239. Dedicated to David Ruelle and Yasha Sinai on the occasion of their 65th birthdays. MR1933444
[16] Ekaterina Vassilieva, Moments of normally distributed random matrices given by generating series for connection coefficients-explicit bijective computation, Ann. Comb. 21 (2017), no. 3, 445-477, DOI 10.1007/s00026-017-0356-y. MR3685122




---

