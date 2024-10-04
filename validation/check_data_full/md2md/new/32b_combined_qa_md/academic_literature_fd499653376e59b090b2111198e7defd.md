# A recursion formula for mixed trace moments of isotropic Wishart matrices and the Gaussian unitary/orthogonal ensembles 

Ben Deitmar<br>Department of Mathematical Stochastics, ALU Freiburg<br>Ernst-Zermelo-Str. 1, 79104 Freiburg, Germany<br>E-mail: ben.deitmar@stochastik.uni-freiburg.de


#### Abstract

Exact recursion formulas for mixed moments of four fundamental random matrix ensembles are derived. The reason such recursive formulas are possible is closely related to properties of polygon gluings studied by Harer and Zagier as well as Akhmedov and Shakirov. The proofs of the formulas are direct and written in such a way that they do not rely on understanding of polygon gluings.


## 1 Introduction

Let $X$ be a $(p \times n)$ random matrix with iid standard normal entries and let $Y$ be a $(p \times n)$ random matrix with iid standard complex normal entries. Further let $Z$ be an $(n \times n)$ random hermitian matrix, where the entries $\left(Z_{i, j}\right)_{i \leq j}$ are independent and $Z_{i, i} \sim \mathcal{N}(0,1)$ for all $i \leq n$ as well as $Z_{i, j}=\overline{Z_{j, i}} \sim \mathcal{C N}(0,1)$ for all $i<j \leq n$. Similarly, let $\tilde{Z}$ be an $(n \times n)$ random symmetric matrix, where the entries $\left(\tilde{Z}_{i, j}\right)_{i \leq j}$ are independent and $\tilde{Z}_{i, i} \sim \mathcal{N}(0,2)$ for all $i \leq n$ as well as $\tilde{Z}_{i, j}=\tilde{Z}_{j, i} \sim \mathcal{N}(0,1)$ for all $i<j \leq n$. The matrices $\frac{1}{\sqrt{n}} Z$ and $\frac{1}{\sqrt{n}} \tilde{Z}$ are of the Gaussian unitary and Gaussian orthogonal ensemble respectively. The matrices $\frac{1}{n} X X^{T}$ and $\frac{1}{n} Y Y^{*}$ are real and complex isotropic Wishart matrices.

In this paper we give exact recursive formulas for mixed trace moments of the type

$$
\mathbb{E}_{X}(\mathbf{l}):=\mathbb{E}\left[\prod_{k=1}^{K} \operatorname{tr}\left(\left(X X^{T}\right)^{l_{k}}\right)\right], \quad \mathbb{E}_{Y}(\mathbf{l}):=\mathbb{E}\left[\prod_{k=1}^{K} \operatorname{tr}\left(\left(Y Y^{*}\right)^{l_{k}}\right)\right]
$$

[^0]
[^0]:    Supported by the DFG Research Unit 5381




---

and

$$
\mathbb{E} Z(l):=\mathbb{E}\left[\prod_{k=1}^{K} \operatorname{tr}\left(Z^{l_{k}}\right)\right], \quad \mathbb{E} \tilde{Z}(l):=\mathbb{E}\left[\prod_{k=1}^{K} \operatorname{tr}\left(\tilde{Z}^{l_{k}}\right)\right]
$$

for arbitrary $p, n, K \in \mathbb{N}$ and layouts $l=\left(l_{1}, \ldots, l_{K}\right) \in \mathbb{N}_{0}^{K}$.
Assuming $l_{1}>0$, the formulas are as follows.

1) Gaussian unitary ensemble:

$$
\begin{aligned}
& \mathbb{E}\left[\prod_{r=1}^{K} \operatorname{tr}\left(Z^{l_{r}}\right)\right]=\sum_{q=1}^{l_{1}-1} \mathbb{E}\left[\operatorname{tr}\left(Z^{q-1}\right) \operatorname{tr}\left(Z^{l_{1}-q-1}\right) \prod_{r=2}^{K} \operatorname{tr}\left(Z^{l_{r}}\right)\right] \\
& \quad+\sum_{k=2}^{K} l_{k} \mathbb{E}\left[\operatorname{tr}\left(Z^{l_{1}+l_{k}-2}\right) \prod_{\substack{r=1 \\
r \neq k}}^{K} \operatorname{tr}\left(Z^{l_{r}}\right)\right]
\end{aligned}
$$

For a complete formulation and proof see Theorem 2.1.
2) Gaussian orthogonal ensemble:

$$
\begin{aligned}
& \mathbb{E}\left[\prod_{r=1}^{K} \operatorname{tr}\left(\tilde{Z}^{l_{r}}\right)\right]=\left(l_{1}-1\right) \mathbb{E}\left[\operatorname{tr}\left(\tilde{Z}^{l_{1}-2}\right) \prod_{r=2}^{K} \operatorname{tr}\left(\tilde{Z}^{l_{r}}\right)\right] \\
& \quad+\sum_{q=1}^{l_{1}-1} \mathbb{E}\left[\operatorname{tr}\left(\tilde{Z}^{q-1}\right) \operatorname{tr}\left(\tilde{Z}^{l_{1}-q-1}\right) \prod_{r=2}^{K} \operatorname{tr}\left(\tilde{Z}^{l_{r}}\right)\right] \\
& \quad+2 \sum_{k=2}^{K} l_{k} \mathbb{E}\left[\operatorname{tr}\left(\tilde{Z}^{l_{1}+l_{k}-2}\right) \prod_{\substack{r=1 \\
r \neq k}}^{K} \operatorname{tr}\left(\tilde{Z}^{l_{r}}\right)\right]
\end{aligned}
$$

For a complete formulation and proof see Theorem 4.1.
3) Complex isotropic Wishart ensemble:

$$
\begin{aligned}
& \mathbb{E}\left[\prod_{r=1}^{K} \operatorname{tr}\left(\left(Y Y^{*}\right)^{l_{r}}\right)\right]=n \mathbb{E}\left[\operatorname{tr}\left(\left(Y Y^{*}\right)^{l_{1}-1}\right) \prod_{r=2}^{K} \operatorname{tr}\left(\left(Y Y^{*}\right)^{l_{r}}\right)\right] \\
& \quad+\sum_{q=1}^{l_{1}-1} \mathbb{E}\left[\operatorname{tr}\left(\left(Y Y^{*}\right)^{q}\right) \operatorname{tr}\left(\left(Y Y^{*}\right)^{l_{1}-q-1}\right) \prod_{r=2}^{K} \operatorname{tr}\left(\left(Y Y^{*}\right)^{l_{r}}\right)\right] \\
& \quad+\sum_{k=2}^{K} l_{k} \mathbb{E}\left[\operatorname{tr}\left(\left(Y Y^{*}\right)^{l_{1}+l_{k}-1}\right) \prod_{\substack{r=1 \\
r \neq k}}^{K} \operatorname{tr}\left(\left(Y Y^{*}\right)^{l_{r}}\right)\right]
\end{aligned}
$$

For a complete formulation and proof see Theorem 3.1.




---

4) Real isotropic Wishart ensemble:

$$
\begin{aligned}
\mathbb{E}\left[\prod_{r=1}^{K} \operatorname{tr}\left(\left(X X^{T}\right)^{l_{r}}\right)\right] & =\left(n+l_{1}-1\right) \mathbb{E}\left[\operatorname{tr}\left(\left(X X^{T}\right)^{l_{1}-1}\right) \prod_{r=2}^{K} \operatorname{tr}\left(\left(X X^{T}\right)^{l_{r}}\right)\right] \\
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

Explicit formulas for the (non-mixed) singular trace moments $\mathbb{E}\left[\operatorname{tr}\left(Z^{2 m}\right)\right]$ as well as $\mathbb{E}\left[\operatorname{tr}\left(\left(X X^{T}\right)^{m}\right)\right]$ and $\mathbb{E}\left[\operatorname{tr}\left(\left(Y Y^{*}\right)^{m}\right)\right]$ are known thanks to Haarer-Zagier in [6] and E. Vassilieva in [16]. The formula in the GUE case is not written explicitly in [6], but following their work we give the formula in (1.2). The formulas for the real and complex Wishart case can be found in Corollaries 1.8 and 1.9 of [16]. For the singular trace moments in the GOE case $\mathbb{E}\left[\operatorname{tr}\left(\tilde{Z}^{2 m}\right)\right]$ a five-term recurrence relation is known thanks to M. Ledoux in [9].

The recursion from Theorem 2.1 for the GUE is not new, as it also follows from Section 5 in [6] by Harer and Zagier. We however still prove it as a precursor to Theorems 3.1, 3.2 and 4.1. The real Wishart case from Theorem 3.2 was already studied by Pielaszkiewicz,




---

Von Rosen and Singull in [11], though they made a minor error in their formula. To the best of our knowledge the results of Theorems 3.1 and 4.1 for the complex Wishart ensemble and the GOE respectively are entirely new.

# 1.1 Trace moments and polygon gluings 

There is a well-known link between trace moments of the GUE and the number of ways to glue to edges of a polygon together to receive an orientable surface of a given genus. This link was first described by Harer and Zagier in [6] to prove the recursive formula

$$
(m+1) \mathbb{E}\left[\operatorname{tr}\left(Z^{2 m}\right)\right]=(4 m-2) n \mathbb{E}\left[\operatorname{tr}\left(Z^{2 m-2}\right)\right]+(m-1)(2 m-1)(2 m-3) \mathbb{E}\left[\operatorname{tr}\left(Z^{2 m-4}\right)\right]
$$

which allows for the explicit representation

$$
\mathbb{E}\left[\operatorname{tr}\left(Z^{2 m}\right)\right]=\frac{(2 m)!}{m!} \sum_{r=1}^{n \wedge(m+1)}\binom{n}{r}\binom{m}{r-1} 2^{m+1-r}
$$

These equalities were first found by Harer and Zagier and later simplified by Haagerup and Thorbjørnsen in [5], but the more readable formulation for (1.1) is from Theorem 1 in [9] by M. Ledoux, where he goes on to find an analogous recursion formula for $\mathbb{E}\left[\operatorname{tr}\left(\tilde{Z}^{2 m}\right)\right]$ in the GOE case.

Akhmedov and Shakirov took this approach further in [1] by considering 'incomplete' gulings of a polygon such that the unglued edges form polygons of given lengths $\left(l_{1}, \ldots, l_{K}\right)$. They were able to give a recursive formula for the number of such incomplete gluings with a given genus (for a certain definition of genus). Unfortunately, although they were able to derive the explicit expression from their recursive formula, their results do not seem applicable to random matrix theory and their solution to a similar recursion does not seem applicable for solving the recursive formulas derived in this article.

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
\mathbb{E} Z(l)=\sum_{g=0}^{\left\lfloor g_{L, K}(0)\right\rfloor} n^{V_{L, K}(g)} \varepsilon_{g}\left(l_{1}, \ldots, l_{K}\right)
$$

under the assumption $l_{1}, \ldots, l_{K}>0$.
A recursion formula for $\mathbb{E} Z(l)$ can then be found by mapping such polygon gluings onto gluings of polygons with two less total edges. If the edge $e_{q}^{k}$ paired with $e_{1}^{1}$ is still part of the same polygon, i.e. $k=1$, then we can contract along the connection of the edges before removing both such that we are left with a gluing of polygons $P_{q-2}, P_{l_{1}-q}, P_{l_{2}}, \ldots, P_{l_{k}}$. Here a picture of what the above pairing would look like after removing $e_{1}^{1}$ and its paired edge $e_{5}^{1}$ :

The edges would of course have to be renamed and we have swapped the positions of the first two polygons such that the effects of contracting along the connection $\left\{e_{1}^{1}, e_{5}^{1}\right\}$ are more obvious.
Similarly, when the edge $e_{q}^{k}$ paired with $e_{1}^{1}$ is not in the first polygon, i.e. $k>1$, contraction along the pairing and removal of the two edges creates one new polygon $P_{l_{1}+l_{k}-2}$ from the two polygons $P_{l_{1}}$ and $P_{l_{k}}$. The rest of the pairing remains a valid gluing for the polygons $P_{l_{1}+l_{k}-2}, P_{2}, \ldots, \widehat{P}_{l_{k}}, \ldots, P_{l_{K}}$. Here an example before the contraction




---

$$
\begin{array}{ccc}
e_{1}^{1} & & e_{3}^{1} \\
e_{2}^{1} & e_{1}^{2} & e_{5}^{2} \\
& e_{4}^{2} & e_{3}^{2} \\
& e_{2}^{2} & \cdots \\
e_{1}^{K} & e_{6}^{K} & e_{5}^{K} \\
& e_{4}^{K} & e_{3}^{K} \\
& e_{2}^{K} &
\end{array}
$$

and removal:

After the contraction and removal:
This method of removing edges does not remove vertices of the ribbon graph, while it can happen that some of the new polygons are empty (i.e. they have length $l_{k}=0$ ). This only becomes a problem, if the first polygon is empty, since then there is no edge $e_{1}^{1}$ to use for the next recursive step of contraction and removal. We thus discard the first polygon, if it is empty. As this also constitutes a removal of an isolated vertex from the ribbon graph, we must keep a tally of how many vertices were removed this way. Luckily, in the recursive formula this tally is simply realized with an additional factor $n$. We have thus far heuristically argued the plausibility of Theorem 2.1.

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
\tilde{f}: E \rightarrow\{M \subset V \mid \# M \leq 2\} \quad ; \quad e_{q}^{1} \mapsto\left\{i_{q}^{1}, i_{(q \bmod m)+1}^{1}\right\}
$$




---

(If $\# f\left(e_{q}^{1}\right)=1$, the edge $e_{q}^{1}$ is a self-loop.) Again $A\left(\tilde{G}_{i_{1}}\right) \in \mathbb{N}_{0}^{n \times n}$ denotes the adjacency matrix of $\tilde{G}_{i_{1}}$, i.e.

$$
A_{v, w}\left(\tilde{G}_{i_{1}}\right)=\#\left\{e_{q}^{1} \in E \mid f\left(e_{q}^{1}\right)=\{v, w\}\right\}
$$

Note that for this definition of the adjacency matrix self-loops are only counted once. For a sequence of routes $\mathbf{i}=\left(i_{1}, \ldots, i_{K}\right) \in \underset{k=1}{\Ktimes} \underset{n}{l_{k}}$ de define the joined adjacency matrices

$$
\mathcal{A}(\mathbf{i}):=\sum_{k=1}^{K} A\left(G_{i_{k}}\right) ; \quad \tilde{\mathcal{A}}(\mathbf{i}):=\sum_{k=1}^{K} A\left(\tilde{G}_{i_{k}}\right)
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
& S_{3, k}(\mathbf{l}):=\left(l_{1}+l_{k}-2, l_{2}, \ldots, \widehat{l}_{k}, \ldots, l_{K}\right)
\end{aligned}
$$

Since (a) reduces $K$ by one and (b) reduces $L=l_{1}+\ldots+l_{K}$ by two, the starting point

$$
\mathbb{E} Z((\langle\rangle))=\mathbb{E}\left[\operatorname{tr}(Z)_{0}\right]=n
$$

for $(K, L)=(1,0)$ allows for the calculation of all mixed moments, when $L$ is even. When $L$ is odd, it is easy to see that the mixed trace moment must be zero.




---

Proof. The property (a) holds trivially, since the empty matrix product is here the $(n \times n)$ identity matrix. It remains to prove property (b).
For now assume $l_{1}, \ldots, l_{K}>0$, then expanding the sums in $\operatorname{tr}\left(Z^{l_{i}}\right)$ yields

$$
\mathbb{E} Z(l)=\sum_{\substack{i_{1} \in[n]_{l} \\ i_{K} \in[n]_{K}}} \mathbb{E}\left[\prod_{k=1}^{K} Z_{i_{1}^{k}} Z_{i_{2}^{k}} \cdots Z_{i_{l_{k}-1}^{k}} Z_{l_{k}^{k}} Z_{i_{l_{k}}^{k}}\right]
$$

Extracting the first entries of each $i^{k}$ and summing over them first gives

$$
\mathbb{E} Z(l)=\sum_{b_{1}, \ldots, b_{K} \in[n]} \sum_{\substack{i \in \times \\ k=1}} \mathbb{E}\left[\prod_{k=1}^{K} Z_{i_{1}^{k}, i_{2}^{k}} \cdots Z_{i_{l_{k}-1}^{k}} Z_{l_{k}^{k}} Z_{i_{l_{1}}^{k}}\right]
$$

For easier notation define

$$
I_{l, b}:=\left\{i=\left(i^{1}, \ldots, i^{K}\right) \in \prod_{k=1}^{K}[n]_{l_{k}} \mid \forall k \leq K:\left(l_{k}>0 \Rightarrow i_{1}^{k}=b_{k}\right)\right\}
$$

then the above formula can be written as

$$
\mathbb{E} Z(l)=\sum_{b_{1}, \ldots, b_{K} \in[n]} \sum_{i \in I_{l, b}} \mathbb{E}\left[\prod_{k=1}^{K} Z_{i_{1}^{k}, i_{2}^{k}} \cdots Z_{i_{l_{k}-1}^{k}} Z_{l_{k}^{k}} Z_{i_{l_{1}}^{k}}\right]
$$

The formula now also holds when some $l_{i}$ are zero, since then the summation over the corresponding $b_{i}$ brings the needed factors $n=\operatorname{tr}\left(Z^{0}\right)$.
Since complex standard normal random variables satisfy $\mathbb{E}\left[X^{a} \bar{X}^{b}\right]=\mathbb{1}_{a=b} a$ ! and real standard normal random variables satisfy $\mathbb{E}\left[X^{a}\right]=\mathbb{1}_{a \text { even }}(a-1)!!$(with the convention $(-1)!!=1)$, the mean in (2.4) has the form

$$
\begin{aligned}
& \mathbb{E}\left[\prod_{k=1}^{K} Z_{i_{1}^{k}, i_{2}^{k}} \ldots Z_{i_{l_{k}-1}^{k}} Z_{l_{k}^{k}} Z_{i_{l_{1}}^{k}}\right] \\
= & \mathbb{1}_{A(i) \text { is symmetric }} \& \text { diag. entries even }\left(\prod_{\substack{v, w \in[n] \\
v<w}} A_{v, w}(i)!\right)\left(\prod_{v \in[n]}^{\prod_{v \in[n]}}\left(A_{v, v}(i)-1\right)!!\right) \\
= & W(A(i))
\end{aligned}
$$

where $A(i):=\sum_{k=1}^{K} A\left(G_{i^{k}}\right)$. Let $c:=i_{l_{1}}^{i_{1}}$ - here the assumption $l_{1}>0$ is needed - and define the symmetric matrix

$$
M_{b, c}:=\left(1_{i=b, j=c}+1_{i=c, j=b}\right)_{i, j \in[n]}
$$




---

For $c \neq b_{1}$, the above definition of $W\left(A^{(i)}\right)$ then yields

$$
\begin{aligned}
& W\left(A^{(i)}\right)=W\left(A^{(i)}\right)-M_{b_{1}, c}\right) A_{c, b_{1}}^{(i)} \\
& =W\left(A^{(i)}-M_{b_{1}, c}\right)\left(A_{c, b_{1}}\left(G_{i_{1}}\right)+\sum_{s=2}^{K} A_{c, b_{1}}\left(G_{i_{s}}\right)\right)
\end{aligned}
$$

where $A_{c, b_{1}}^{(i)}$ is at least 1 , since it counts the number of occurrences of the connection $\left(i_{l_{1}}^{1}, i_{1}^{1}\right)=\left(c, b_{1}\right)$. The fact that $W(A)$ is zero as soon as $A$ is not symmetric, allows us to swap $b_{1}$ and $c$ in arbitrary places of the formula, so we may also write

$$
W\left(A^{(i)}\right)=W\left(A^{(i)}-M_{b_{1}, c}\right)\left(A_{b_{1}, c}\left(G_{i_{1}}\right)+\sum_{s=2}^{K} A_{b_{1}, c}\left(G_{i_{s}}\right)\right)
$$

Similarly, when $c=b_{1}$, the weight satisfies

$$
\begin{aligned}
& W\left(A^{(i)}\right)=W\left(A^{(i)}\right)-M_{b_{1}, b_{1}}\right)\left(A_{b_{1}, b_{1}}^{(i)}-1\right) \\
& =W\left(A^{(i)}-M_{b_{1}, b_{1}}\right)\left(A_{b_{1}, b_{1}}\left(G_{i_{1}}\right)-1+\sum_{s=2}^{K} A_{b_{1}, b_{1}}\left(G_{i_{s}}\right)\right)
\end{aligned}
$$

and we can use these properties of the weight to decompose equality (2.4) into

$$
\begin{aligned}
& \mathbb{E}_{Z(l)}=\underbrace{\sum_{\substack{\mathbf{i} \in[n]^{K} \\
c \in[n]}} \sum_{i_{l_{1}}=c} W\left(A^{(i)}-M_{b_{1}, c}\right)\left(A_{b_{1}, c}\left(G_{i_{1}\langle}\right)-\mathbf{1}_{b_{1}=c}\right)}_{=: \mathbb{E}_{Z(l)}^{1}}+\underbrace{\sum_{\substack{\mathbf{b} \in[n]^{K} \\
c \in[n]}} \sum_{i \in I_{l, b}} W\left(A^{(i)}-M_{b_{1}, c}\right) \sum_{s=2}^{K} A_{b_{1}, c}\left(G_{i_{s}}\right)}_{\mathbb{E}_{Z(l)}^{2}} .
\end{aligned}
$$

For $\mathbb{E}_{Z(l)}^{1}$ observe that $A_{b_{1}, c}\left(G_{i_{1}}\right)$ counts the number of occurrences of $\left(b_{1}, c\right)$ in $\mathbf{i}_{1}=$ $\left(i_{1}^{1}, \ldots, i_{l_{1}}^{1}\right)$ and, if this number is $\mathbf{1}_{b_{1}=c}$, such an $i$ will not contribute to $\mathbb{E}_{Z(l)}^{1}$. Define

$$
Q_{b, c}^{1}\left(\mathbf{i}_{1}\right)=\left\{q<l_{1} \mid i_{q}^{1}=b, i_{q+1}^{1}=c\right\}
$$

then $A_{b_{1}, c}\left(G_{i_{1}}\right)-\mathbf{1}_{b_{1}=c}=\# Q_{b_{1}, c}^{1}\left(\mathbf{i}_{1}\right)$. For each $q \in Q_{b_{1}, c}^{1}\left(\mathbf{i}_{1}\right)$ we give a unique way of splitting up $\mathbf{i}_{1}$ into two new routes $\left\langle\mathbf{i}_{1}\right\rangle_{q, 1}$ and $\left\langle\mathbf{i}_{1}\right\rangle_{q, 2}$. Define

$$
\left\langle\mathbf{i}_{1}\right\rangle_{q, 1}:=\left(\underbrace{i_{1}^{1}}_{=b_{1}}, \ldots, i_{q-1}^{1}\right) \in[n]^{q-1} ;\left\langle\mathbf{i}_{1}\right\rangle_{q, 2}:=\left(i_{q+2}^{1}, \ldots, \underbrace{i_{l_{1}}^{1}}_{=c}\right) \in[n]^{l_{1}-q-1}
$$

and observe that when going from the multi-graph $G_{\mathbf{i}_{1}}$ to $G_{\left\langle\mathrm{i}_{1}\right\rangle_{q, 1}} \cup G_{\left\langle\mathbf{i}_{1}\right\rangle_{q, 1}}$ we have only lost one edge in each direction (two edges without direction in the case of $b_{1}=c$ ) between the vertices $b_{1}$ and $c$ while all other edges remain. For

$$
\mathbf{J}_{q}^{1}(i):=\left(\left\langle\mathbf{i}_{1}\right\rangle_{q, 1},\left\langle\mathbf{i}_{1}\right\rangle_{q, 2}, \mathbf{i}_{2}, \ldots, \mathbf{i}_{K}\right)
$$




---

it follows that

$$
A\left(J_{q}^{1}(\boldsymbol{i})\right)=A(\boldsymbol{i})-M_{b_{1}, c}
$$

Since we sum over all choices of $c$ and all the other elements in $\boldsymbol{i}^{1}$, which were not specified can still be chosen freely, this for $E_{l}^{1}$ implies

$$
\begin{aligned}
E_{\mathbf{Z}(l)}^{1} & =\sum_{\substack{\boldsymbol{b} \in[n]^{K} \\
c \in[n]}} \sum_{\substack{\boldsymbol{i} \in I_{l, \boldsymbol{b}} \\
i_{l_{1}}^{1}=c}} \sum_{q \in Q_{b_{1}, c}^{1}\left(\boldsymbol{i}^{1}\right)} W\left(A\left(J_{q}^{1}(\boldsymbol{i})\right)\right) \\
& =\sum_{q=1}^{l_{1}-1} \sum_{\substack{\boldsymbol{b} \in[n]^{K} \\
c \in[n]}} \sum_{\substack{\boldsymbol{i} \in I_{l, \boldsymbol{b}} \\
i_{l_{1}}^{1}=c \\
q \in Q_{b_{1}, c}^{1}\left(\boldsymbol{i}^{1}\right)}} W\left(A\left(J_{q}^{1}(\boldsymbol{i})\right)\right) \\
& =\sum_{q=1}^{l_{1}-1} \sum_{\tilde{\boldsymbol{b}} \in[n]^{K+1}} \sum_{\boldsymbol{i} \in I_{S_{2}, q}(l), \tilde{\boldsymbol{b}}} W(A(\boldsymbol{i})),
\end{aligned}
$$

where

$$
S_{2, q}(l):=\left(q-1, l_{1}-q-1, l_{2}, \ldots, l_{K}\right)
$$

is defined in analogy to $J_{q}^{1}(\boldsymbol{i})$. We have thus shown

$$
E_{\mathbf{Z}(l)}^{1}=\sum_{q=1}^{l_{1}-1} \mathbb{E}_{\mathbf{Z}\left(S_{2, q}(l)\right)}
$$

Next, for $E_{\mathbf{Z}(l)}^{2}$ observe that $\sum_{k=2}^{K} A_{b_{1}, c}\left(G_{i^{k}}\right)$ counts the number of occurrences of $\left(b_{1}, c\right)$ in

$$
\left(i_{1}^{2}, \ldots, i_{l_{2}}^{2}\right), \cdots,\left(i_{1}^{K}, \ldots, i_{l_{K}}^{K}\right)
$$

and define the set

$$
Q_{b, c}^{2}(\boldsymbol{i}):=\left\{(k, q) \in\{2, \ldots, K\} \times \mathbb{N}\left|q \leq l_{k} \text { and }\right| q<l_{k} \Rightarrow\left(i_{q}^{k}=b \wedge i_{q+1}^{k}=c\right), q=l_{k} \Rightarrow\left(i_{l_{k}}^{k}=b \wedge i_{1}^{k}=c\right)\right\}
$$

Again $\sum_{k=2}^{K} A_{b_{1}, c}\left(G_{i^{k}}\right)=\# Q_{b_{1}, c}^{2}(\boldsymbol{i})$ and this time for each $(k, q) \in Q_{b_{1}, c}^{2}(\boldsymbol{i})$ we give a unique way of joining the routes $\boldsymbol{i}^{1}$ and $\boldsymbol{i}^{k}$ into a new route

$$
\left\langle\boldsymbol{i}^{1}, \boldsymbol{i}^{k}\right\rangle_{q}:= \begin{cases}\left(i_{1}^{1}, \underbrace{\ldots, i_{l_{1}}^{1}, k+2, \ldots, i_{l_{k}}}_{=b_{k}} i_{1}^{k}, \ldots, i_{q-1}^{k}\right) \in[n]^{l_{1}+l_{s}-1}, & \text {, if } q<l_{k} \\ \left(i_{1}^{1}, \underbrace{\ldots, i_{l_{1}}^{1}, k+2, \ldots, i_{l_{k}-1}^{k}}_{=b_{k}}\right) \in[n]^{l_{1}+l_{s}-1}, & \text {, if } q=l_{k}\end{cases}
$$




---

Going from the multigraph $G_{i_{1}} \cup G_{i_{k}}$ to $G_{\left\langle i_{1}, i_{k}\right\rangle_{q}}$ we only loose one edge in each direction between the vertices $b_{1}$ and $c$ (two undirected edges in the case $b_{1}=c$ ) while all other edges remain. For

$$
J_{(k, q)}^{2}(\boldsymbol{i}):=\left(\left\langle i_{1}, i_{k}\right\rangle_{q}, i_{2} \ldots, \widehat{i_{k}}, \ldots, i_{K}\right)
$$

it follows that

$$
A\left(J_{(k, q)}^{2}(\boldsymbol{i})\right)=A(\boldsymbol{i})-M_{b_{1}, c}
$$

and similarly to (2.10) we get

$$
\begin{aligned}
E_{Z}^{2}(\boldsymbol{l}) & =\sum_{\substack{\boldsymbol{b} \in[n]^{K} \\
c \in[n]}} \sum_{\substack{\boldsymbol{i} \in I_{\boldsymbol{l}, \boldsymbol{b}} \\
\boldsymbol{i}_{l_{1}}=c}} \sum_{(k, q) \in Q_{b_{1}, c}^{2}} A\left(J_{(k, q)}^{2}(\boldsymbol{i})\right) \\
& =\sum_{k=2}^{K} \sum_{q=1}^{l_{k}} \sum_{\substack{\boldsymbol{b} \in[n],{ }^{K} \\
c \in[n]}} \sum_{\substack{\boldsymbol{i} \in I_{l, b} \\
\boldsymbol{i}_{1}=c \\
(k, q) \in Q_{b_{1}, c}^{2}}} A\left(J_{(k, q)}^{2}(\boldsymbol{i})\right) \\
& =\sum_{k=2}^{K} \sum_{q=1}^{l_{k}} \sum_{\tilde{\boldsymbol{b}} \in[p]^{K-1}} \sum_{\boldsymbol{i} \in I_{S_{3, k}(\boldsymbol{l}), \tilde{\boldsymbol{b}}}} A(\boldsymbol{i}) \\
& =\sum_{k=2}^{K} \sum_{r=1}^{l_{k}} \operatorname{EZ}\left(S_{3, k}(\boldsymbol{l})\right)=\sum_{k=2}^{K} l_{k} \operatorname{EZ}\left(S_{3, k}(\boldsymbol{l})\right)
\end{aligned}
$$

where

$$
S_{3, k}(\boldsymbol{l}):=\left(l_{1}+l_{k}-2, l_{2}, \ldots, \widehat{l_{k}}, \ldots, l_{K}\right)
$$

is defined in analogy to $J_{(k, q)}^{2}$.
Equalities (2.7), (2.11) and (2.14) together show

$$
\operatorname{EZ}(\boldsymbol{l})=\sum_{q=1}^{l_{1}-1} \operatorname{EZ}\left(S_{2, q}(\boldsymbol{l})\right)+\sum_{k=2}^{K} l_{k} \operatorname{EZ}\left(S_{3, k}(\boldsymbol{l})\right)
$$

# 2.2 Remark (Translation to polygon gluings) 

In terms of $\varepsilon_{g}(\boldsymbol{l})$ from (1.3) the recursion can be written as

$$
\sum_{g=0}^{\left\lfloor g_{L, K}(0)\right\rfloor} n_{V_{L, K}}(g) \varepsilon_{g}(\boldsymbol{l})
$$




---

$$
=\sum_{q=1}^{l_{1}-1} \sum_{g=0}^{\left\lfloor g_{L-2, K+1}(0)\right\rfloor} n^{V_{L-2, K+1}(g)} \varepsilon_{g}\left(S_{2, q}(l)\right)+\sum_{k=2}^{K} l_{k} \sum_{g=0}^{\left\lfloor g_{L-2, K-1}(0)\right\rfloor} n^{V_{L-2, K-1}(g)} \varepsilon_{g}\left(S_{3, k}(l)\right)
$$

With

$$
V_{L, K}(g)=2-2 g+\frac{L}{2}-K=V_{L-2, K+1}(g)=V_{L-2, K-1}(g-1)
$$

it implies

$$
\varepsilon_{g}(l)=\sum_{q=1}^{l_{1}-1} \varepsilon_{g}\left(S_{2, q}(l)\right)+\sum_{k=2}^{K} l_{k} \varepsilon_{g-1}\left(S_{3, k}(l)\right)
$$

when $l_{1}>0$, and $\varepsilon_{g}\left(0, l_{2}, \ldots, l_{K}\right)=\varepsilon_{g}\left(l_{2}, \ldots, l_{K}\right)$ otherwise.

# 3 Wishart Ensemble 

For ease of notation in the following proofs we write the matrices $X$ and $Y$ as

$$
X=:\left(X_{i, j}\right)_{i \in[p], j \in[p+n] \backslash[p]} \text { and } Y=:\left(Y_{i, j}\right)_{i \in[p], j \in[p+n] \backslash[p]} .
$$

3.1 Theorem (Recursion for mixed trace moments of complex isotropic Wishart matrices)
For $K \in \mathbb{N}$ and any $l=\left(l_{1}, \ldots, l_{K}\right) \in \mathbb{N}_{0}^{K}$ the following recursive properties hold.
a) If $l_{1}=0$, then $\mathbb{E} Y(l)=p \mathbb{E} Y\left(S_{0}(l)\right)$ for

$$
S_{0}\left(0, l_{2}, \ldots, l_{K}\right):=\left(l_{2}, \ldots, l_{K}\right)
$$

b) If $l_{1}>0$, then

$$
\mathbb{E} Y(l)=n \mathbb{E} Y\left(S_{1}(l)\right)+\sum_{r=1}^{l_{1}-1} \mathbb{E} Y\left(S_{2, r}(l)\right)+\sum_{k=2}^{K} l_{k} \mathbb{E} Y\left(S_{3, l_{k}}(l)\right)
$$

where

$$
\begin{aligned}
S_{1}(l) & :=\left(l_{1}-1, l_{2}, \ldots, l_{K}\right) \\
S_{2, r}(l) & :=\left(r, l_{1}-r-1, l_{2}, \ldots, l_{K}\right) \\
S_{3, k, q}(l) & :=\left(l_{1}+l_{k}-1, l_{2}, \ldots, \widehat{l}_{k}, \ldots, l_{K}\right)
\end{aligned}
$$

Since (a) reduces $K$ by one and (b) reduces $L:=\sum_{k=1}^{K} l_{k}$ by one, the end point

$$
\mathbb{E} Y((()))=\mathbb{E}\left[\operatorname{tr}\left(\left(Y Y^{*}\right)^{0}\right)\right]=p
$$

for $(K, L)=(1,0)$ allows for the calculation of all mixed moments.




---

Proof. The property (a) holds trivially, since the empty matrix product is here the $(p \times p)$ identity matrix. The proof of property (b) will take most of the section.

For now assume $l_{1}, \ldots, l_{K}>0$, then by expanding the sums in $\operatorname{tr}\left(S_{l_{i}}\right)$ we see

$$
\mathbb{E} Y(l)=\sum_{\substack{i_{i} \in B_{p, n, l_{3}} \\ i_{i} \\ i_{i} \in B_{p, n, l K}}} \mathbb{E}\left[\prod_{k=1}^{K}\left(Y_{i_{1}^{k}, i_{2}^{k}} Y_{i_{3}^{k}, i_{2}^{k}}\right) \cdots\left(Y_{i_{2 l_{k}-1}^{k} i_{2 l_{k}}, i_{2 l_{k}}^{k}}\right)\right]
$$

where

$$
B_{p, n, l}:=\left\{\left(i_{1}, \ldots, i_{2 l}\right) \in \mathbb{N}^{2 l} \mid\left\{i_{1}, i_{3}, \ldots, i_{2 l-1}\right\} \in[p],\left\{i_{2}, i_{4}, \ldots, i_{2 l}\right\} \in[p+n] \backslash[p]\right\}
$$

Extracting the first entries of each $i^{k}$ and summing over them first yields

$$
\mathbb{E} Y(l)=\sum_{b_{1}, \ldots, b_{K} \in[p]} \sum_{\substack{i_{i} \in B_{p, n, l_{1}} \\ i_{i_{K} \in B_{p, n, l}} \\ \forall k \leq K: i_{i}^{k}=b_{k}}} \mathbb{E}\left[\prod_{k=1}^{K}\left(Y_{i_{1}^{k} i_{2}^{k}} Y_{i_{3}^{k}, i_{2}^{k}}\right) \cdots\left(Y_{i_{2 l_{k}-1}, i_{2 l_{k}}^{k}} Y_{i_{1}^{k}, i_{2 l_{k}}}\right)\right]
$$

For ease of notation define

$$
B_{l, b}:=\left\{i=\left(i^{1}, \ldots, i^{K}\right) \in \prod_{k=1}^{K} B_{p, n, l_{k}} \mid \forall k \leq K:\left(l_{k}>0 \Rightarrow i_{1}^{k}=b_{k}\right)\right\}
$$

then the above formula for $\mathbb{E} Y(l)$ becomes

$$
\mathbb{E} Y(l)=\sum_{b_{1}, \ldots, b_{K} \in[p]} \sum_{i \in B_{l, b}} \mathbb{E}\left[\prod_{k=1}^{K}\left(Y_{i_{1}^{k}, i_{2}^{K}} Y_{i_{3}^{k} i_{2}^{k}}\right) \cdots\left(Y_{i_{2 l_{k}-1}^{k} i_{2 l_{k}}^{k} Y_{i_{1}^{k} i_{2 l_{k}^{k}}}}\right)\right]
$$

Just as (2.4) in the GUE case, this formula now also holds for any $l_{1}, \ldots, l_{K} \in \mathbb{N}_{0}^{K}$. This time the mean is seen to have the form

$$
\mathbb{E}\left[\prod_{k=1}^{K} Y_{i_{1}^{k}, i_{2}^{k}} Y_{i_{3}^{k}, i_{2}^{k}} \cdots Y_{i_{2 l_{k}-1}^{k} i_{2 l_{k}}^{k}} Y_{i_{1}^{k}, i_{2 l_{k}}^{k}}\right]=\mathbb{1}_{A(i) \text { is symmetric }}\left(\prod_{\substack{v \in[p] \\ w \in[p+n] \backslash[p]}} A_{v, w}(i)\right)=: W(A(i))
$$

where again $A(i):=\sum_{k=1}^{K} A\left(G_{i^{K}}\right)$. Let $c:=i_{2 l_{1}}^{1}$ and define the symmetric matrix

$$
M_{b, c}:=\left(\mathbb{1}_{i=b, j=c \text { or } i=c, j=b}\right)_{i, j \in[p+n]}
$$




---

With the very same argument as the one leading up to (2.7) - except that this time only the case $b_{1} \neq c$ is needed - we can decompose equality (3.5) into

$$
\begin{aligned}
& \mathbb{E} Y^{(l)}= \\
& \underbrace{\sum_{\substack{b \in[p]^{K} \\
c \in[p+n] \backslash[p]}} \sum_{\substack{i \in B_{l, b} \\
i_{2 l_{1}}^{1}=c}} W\left(A(i)-M_{b_{1}, c}\right) A_{b_{1}, c}\left(G_{i_{1}}\right)}_{=: \mathbb{E}_{Y}^{1}(l)}+ \\
& \underbrace{\sum_{\substack{b \in[p]^{K} \\
c \in[p+n] \backslash[p]}} \sum_{\substack{i \in B_{l, b} \\
i_{1} \\
2 i_{1}=c}} W\left(A(i)-M_{b_{1}, c}\right) \sum_{s=k}^{K} A_{b_{1}, c}\left(G_{i_{k}}\right)}_{=: \mathbb{E}_{Y}^{2}(l)} .
\end{aligned}
$$

For $\mathbb{E}_{Y}^{1}(l)$ observe that $A_{b_{1}, c}\left(G_{i_{1}}\right)$ counts the number of occurrences of $\left(b_{1}, c\right)$ in $i_{1}=$ $\left(i_{1}^{1}, \ldots, i_{2 l_{1}}^{1}\right)$ and, if this number is zero, such an $i$ will not contribute to $\mathbb{E}_{l}^{1}$. Define

$$
Q_{b, c}^{1}\left(i_{1}\right)=\left\{q<2 l_{1} \mid i_{q}^{1}=b, i_{q+1}^{1}=c\right\}
$$

then clearly $A_{b_{1}, c}\left(G_{i_{1}}\right)=\# Q_{b_{1}, c}^{1}\left(i_{1}\right)$ and by the bipartite definition of $B_{p, n, l_{1}}$ all elements in $Q_{b, c}^{1}\left(i_{1}\right)$ must be odd. For each $q \in Q_{b_{1}, c}^{1}\left(i_{1}\right)$ we give a unique way of splitting up $i_{1}$ into two new routes $\left\langle i_{1}\right\rangle_{q, 1}$ and $\left\langle i_{1}\right\rangle_{q, 2}$. Define

$$
\begin{aligned}
& \left\langle i_{1}\right\rangle_{q, 1}:=\left(\underbrace{i_{q+2}^{1}, \ldots, i_{2 l_{1}}^{1}}_{=c}\right) \in B_{p, n, \frac{l_{1}-q+1}{2}} \\
& \left\langle i_{1}\right\rangle_{q, 2}:=\left(\underbrace{i_{1}^{1}}_{=b_{1}}, \ldots, i_{q-1}^{1}\right) \in B_{p, n, \frac{q-1}{2}}
\end{aligned}
$$

and observe that between the multi-graphs $G_{i_{1}}$ and $G_{\left\langle i_{1}\right\rangle_{q, 1}} \cup G_{\left\langle i_{1}\right\rangle_{q, 1}}$ we have only lost one edge in each direction between the vertices $b_{1}$ and $c$ while all other edges remain. For

$$
J_{q}^{1}(i):=\left(\left\langle i_{1}\right\rangle_{q, 1},\left\langle i_{1}\right\rangle_{q, 2}, i_{2}, \ldots, i_{K}\right)
$$

it follows that

$$
A\left(J_{q}^{1}(i)\right)=A(i)-M_{b_{1}, c}
$$

Since we sum over all choices of $c$ and all the other elements in $i_{1}$, which were not specified can still be chosen freely according the rules of $B_{l, b}$, this for $\mathbb{E}_{l}^{1}$ implies

$$
\begin{aligned}
\mathbb{E}_{Y}^{1}(l) & =\sum_{\substack{b \in[p]^{K} \\
c \in[p+n] \backslash[p]}} \sum_{\substack{i \in B_{l, b} \\
i_{2 l_{1}}^{1}=c}} \sum_{q \in Q_{b_{1}, c}^{1}\left(i_{1}\right)} W\left(A\left(J_{q}^{1}(i)\right)\right) \\
& =\sum_{q=1}^{2 l_{1}-1} \sum_{\substack{b \in[p]^{K} \\
c \in[p+n]\{p]}} \sum_{\substack{i \in B_{l, b} \\
i_{2 l_{1}}^{1}=c}} W\left(A\left(J_{q}^{1}(i)\right)\right)
\end{aligned}
$$




---

$$
\begin{aligned}
& r=\frac{l_{1}-q-1}{2}=\sum_{r=0}^{l_{1}-1} \sum_{\substack{\boldsymbol{b} \in[p]^{K} \\
b^{\prime} \in[p], \text { if } r>0}} \sum_{\substack{c \in[p+n] \backslash[p] \\
j \in \mathcal{B}_{\left(b^{\prime}, b_{1}, \ldots, b_{K}\right)} \\ \frac{r}{2} r>0 \Rightarrow j_{1}=c}} \mathcal{W}(A(j)) \\
& =\frac{n}{p} \sum_{\tilde{b} \in[p]^{K+1}} \sum_{j \in \mathcal{B}_{\tilde{b}} S_{2,0}(l)} \mathcal{W}(A(j)) \\
& +\sum_{r=1}^{l_{1}-1} \sum_{\tilde{b} \in[p]^{K+1}} \sum_{j \in \mathcal{B}_{\tilde{b}} S_{2}, r(l)} \mathcal{W}(A(j)) \\
& =n \mathbb{E}^{Y}\left(S_{1}(l)\right)+\sum_{r=1}^{l_{1}-1} \mathbb{E}^{Y}\left(S_{2, r}(l)\right),
\end{aligned}
$$

where

$$
S_{2, r}(l)=\left(r, l_{1}-r-1, l_{2}, \ldots, l_{K}\right)
$$

is defined in analogy to $J_{q}^{1}(i)$ and

$$
S_{1}(l)=\left(l_{1}-1, l_{2}, \ldots, l_{K}\right)
$$

The factor $n$ in the first summand comes from the summation over $c$, which no longer had an influence on the latter sum in the case $q=2 l_{1}-1 \Leftrightarrow r=0$. The temporary factor $\frac{1}{p}$ in the first summand was added and removed with the summation over $b^{\prime}=\tilde{b}_{1}$.
Next for $\mathbb{E}_{Y}^{2}(l)$ observe that ${ }_{k=2}^{K_{1}} A_{b_{1}, c}\left(G_{i^{k}}\right)$ counts the number of occurrences of $\left(b_{1}, c\right)$ in

$$
\left(i_{1}^{2}, \ldots, i_{2 l_{2}}^{2}\right), \cdots,\left(i_{1}^{K}, \ldots, i_{2 l_{K}}^{K}\right)
$$

and define the set

$$
\mathcal{Q}_{b, c}^{2}(i):=\left\{(k, q) \in\{2, \ldots, K\} \times \mathbb{N} \mid i_{q}^{k}=b, i_{q+1}^{k}=c\right\}
$$

Again $\sum_{k=2}^{K} A_{b_{1}, c}\left(G_{i^{k}}\right)=\# \mathcal{Q}_{b_{1}, c}^{2}$ and all tuples $(k, q) \in \mathcal{Q}_{b, c}^{2}(i)$ must have odd $q$. This time for each $(k, q) \in \mathcal{Q}_{b_{1}, c}^{2}(i)$ we give a unique way of joining the routes $i^{1}$ and $i^{k}$ into a new route

$$
\left\langle i^{1}, i^{k}\right\rangle_{q}:=\left(\underbrace{i_{1}^{k}}_{=b_{k}}, \ldots, i_{q-1}^{k}, \underbrace{i_{1}^{1}}_{=b_{1}}, \ldots, \underbrace{i_{2 l_{1}}^{1}}_{=c}, i_{q+2}^{k}, \ldots, i_{2 l_{k}}^{k}\right) \in \mathcal{B}_{p, n, l_{1}+l_{s}-1} .
$$

Again we between the multigraphs $G_{i^{1}} \cup G_{i^{k}}$ and $G_{\left\langle i^{1},{ }^{i}{ }^{k}\right\rangle_{q}}$ only loose one edge in each direction between the vertices $b_{1}$ and $c$ while all other edges remain. For

$$
J_{(k, q)}^{2}(i):=\left(\left\langle i^{1}, i^{k}\right\rangle_{q,,}, i^{2} \ldots, \widehat{i^{k}}, \ldots, i^{K}\right)
$$




---

it follows that

$$
A\left(J_{(k, q)}^{2}(i)\right)=A(\underline{i})-M_{b_{1}, c}
$$

and similarly to (2.14) we get

$$
\begin{aligned}
E_{Y}^{2}(l) & =\sum_{\substack{b \in[p]^{K} \\
c \in[p+n] \backslash[p]}} \sum_{\substack{i \in B_{i_{\mathrm{i}}^{1}}^{l} \\
i_{1}^{2}=c}} \sum_{(k, q) \in Q_{b_{1}, c}^{2}} A\left(J_{(k, q)}^{2}(i)\right)_{r=\frac{q+1}{2}} \\
& =\sum_{k=2}^{K} \sum_{r=1}^{l_{k}} \sum_{\tilde{b} \in[p]^{K-1}} \sum_{i \in B^{S_{3, k}(l), y, \tilde{b}}} A(i, j)=\sum_{k=2}^{K} l_{k} E_{Y}\left(S_{3, k}(l)\right)
\end{aligned}
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
E_{X}((\langle\rangle))=E\left[\operatorname{tr}\left(\left(X X^{T}\right)^{0}\right)\right]=p
$$

for $(K, L)=(1,0)$ allows for the calculation of all mixed moments.




---

Proof. In complete analogy to the proof of Theorem 3.1 know (a) to hold and for the proof of (b) in the case $l_{1}>0$ have

$$
\mathbb{E} X^{(l)}=\sum_{b_{1}, \ldots, b_{K} \in[p]} \sum_{i \in B_{l, \mathbf{b}}} \mathbb{E}\left[\prod_{k=1}^{K}\left(X_{i_{1}^{k}, i_{2}^{k}} X_{i_{3}^{k}, i_{2}^{k}}\right) \cdots\left(X_{i_{2 l_{k}-1}^{k}, i_{2 l_{k}}^{k}} X_{i_{1}^{k}, i_{2 l_{k}}^{k}}\right)\right]
$$

for any $l_{1}, \ldots, l_{K} \in \mathbb{N}_{0}^{K}$. The weight is instead

where $\tilde{A}^{(i)}=\sum_{k=1}^{K} A^{\left(\tilde{G}_{i}\right)}$. Let $c:=i_{2 l_{1}}^{1}$ and define the matrix

$$
\tilde{M}_{b, c}:=2\left(\mathbb{1}_{i=b, j=c \text { or } i=c, j=b}\right)_{i, j \in[p+n]}
$$

By the definition of the weight $W\left(\tilde{A}^{(i)}\right)$ it for all $i \in B_{l, \mathbf{b}}$ with $\tilde{A}^{(i)}_{b_{1}, c} \geq 2$ follows that

$$
\begin{aligned}
W\left(\tilde{A}^{(i)}\right) & =W\left(\tilde{A}^{(i)}-\tilde{M}_{b_{1}, c}\right)\left(\tilde{A}^{(i)}_{b_{1}, c}-1\right) \\
& =W\left(\tilde{A}^{(i)}-\tilde{M}_{b_{1}, c}\right)\left(A_{b_{1}, c}\left(\tilde{G}_{i_{1}}\right)-1+\sum_{k=2}^{K} A_{b_{1}, c}\left(\tilde{G}_{i_{k}}\right)\right)
\end{aligned}
$$

Again this can be used to decompose equality (3.15) into

$$
\mathbb{E} X^{(l)}=\sum_{\substack{\mathbf{b} \in[p]^{K_{1}} \\ c \in\left[p+n_{[p]}\right.}} \sum_{\substack{i \in B_{l, \mathbf{b}} \\ i_{2 l_{1}}^{1}=c}} \underbrace{W\left(\tilde{A}^{(i)}-\tilde{M}_{b_{1}, c}\right)\left(A_{b_{1}, c}\left(\tilde{G}_{i_{1}}\right)-1\right)}_{=: \mathbb{E}_{1} X^{(l)}}+\sum_{\substack{\mathbf{b} \in[p]^{K_{1}} \\ c \in\left[p+n_{[p]}\right.}} \sum_{\substack{i \in B_{l, \mathbf{b}} \\ i_{2 l_{1}}^{1}=c}} \underbrace{W\left(\tilde{A}^{(i)}-\tilde{M}_{b_{1}, c}\right) \sum_{k=2}^{K} A_{b_{1}, c}\left(\tilde{G}_{i_{k}}\right)}_{=: \mathbb{E}_{2} X^{(l)}}
$$

since all $i \in B_{l, \mathbf{b}}$ contributing to the sum must satisfy $\tilde{A}^{(i)}_{b_{1}, c} \geq 2$. Define

$$
\begin{aligned}
& Q_{b, c}^{0}\left(i_{1}\right)=\left\{q<2 l_{1} \mid i_{q}^{1}=c, i_{q+1}^{1}=b\right\} \\
& Q_{b, c}^{1}\left(i_{1}\right)=\left\{q<2 l_{1} \mid i_{q}^{1}=b, i_{q+1}^{1}=c\right\}=Q_{c, b}^{0}(i)
\end{aligned}
$$




---

then $\underline{A}_{\boldsymbol{b}_{1}, \boldsymbol{c}}\left(\tilde{G}_{\boldsymbol{i}^{1}}\right)^{-1}=\# Q_{\boldsymbol{b}_{1}, \boldsymbol{c}}^{0}\left(\boldsymbol{i}^{1}\right)+\# Q_{\boldsymbol{b}_{1}, \boldsymbol{c}}^{1}\left(\boldsymbol{i}^{1}\right)$ and by construction all elements of $Q_{\boldsymbol{b}_{1}, \boldsymbol{c}}^{0}\left(\boldsymbol{i}^{1}\right)$ must be even and all elements of $Q_{\boldsymbol{b}_{1}, \boldsymbol{c}}^{1}\left(\boldsymbol{i}^{1}\right)$ must be odd. For each $q \in Q_{\boldsymbol{b}_{1}, \boldsymbol{c}}^{1}\left(\boldsymbol{i}^{1}\right)$ let $J_{q}^{1}(\boldsymbol{i})$ be just as in the proof of Theorem 3.1 and we also have $\tilde{\mathcal{A}}\left(J_{q}^{1}(\boldsymbol{i})\right)=\tilde{\mathcal{A}}(\boldsymbol{i})-\tilde{\mathcal{M}}_{\boldsymbol{b}_{1}, \boldsymbol{c}}$. For each $q \in Q_{\boldsymbol{b}_{1}, \boldsymbol{c}}^{0}\left(\boldsymbol{i}^{1}\right)$ let

$$
\begin{gathered}
\left\langle\boldsymbol{i}^{1}\right\rangle^{q}=\left(i_{1}^{1} \underbrace{\left., \ldots, i_{q-1}^{1}, i_{2 l_{1}}^{1}\right)}_{=\boldsymbol{c}}, i_{2 l_{1}-1}^{1}, \ldots, i_{q+3}^{1}, i_{q+2}^{1}\right) \in \mathcal{B}^{p, n, l_{1}-1} \\
\text { and } \quad J_{q}^{0}:=\left(\left\langle\boldsymbol{i}^{1}\right\rangle^{q}, \boldsymbol{i}^{2}, \ldots, \boldsymbol{i}^{K}\right)
\end{gathered}
$$

then it also holds that $\tilde{\mathcal{A}}\left(J_{q}^{0}(\boldsymbol{i})\right)=\tilde{\mathcal{A}}(\boldsymbol{i})-\tilde{\mathcal{M}}_{\boldsymbol{b}_{1}, \boldsymbol{c}}$ and we can similarly to (3.11) see

$$
\begin{aligned}
\mathbb{E}_{X}^{1}(l) & =\sum_{\substack{\boldsymbol{b} \in[p]^{K} \\
\boldsymbol{c} \in[p+n] \backslash[p]}} \sum_{\substack{\boldsymbol{i} \in \mathcal{B}^{l, b} \\
i_{2 l_{1}}^{1}=\boldsymbol{c}}} \sum_{q \in Q_{\boldsymbol{b}_{1}, \boldsymbol{c}}^{0}(\boldsymbol{i})} W\left(\tilde{\mathcal{A}}\left(J_{q}^{0}(\boldsymbol{i})\right)\right) \\
& +\sum_{\substack{\boldsymbol{b} \in[p]^{K} \\
\boldsymbol{c} \in[p+n] \backslash[p]}} \sum_{\substack{i \in \mathcal{B}^{l, b} \\
i_{2 l_{1}}^{1}=\boldsymbol{c}}} \sum_{q \in Q_{\boldsymbol{b}_{1}, \boldsymbol{c}}^{1}(\boldsymbol{i})} W\left(\tilde{\mathcal{A}}\left(J_{q}^{1}(\boldsymbol{i})\right)\right) .
\end{aligned}
$$

For the second summand the exact same steps as in (3.11) show that it must be equal to

$$
n \mathbb{E}_{X}\left(S_{1}(l)\right)+\sum_{r=1}^{l-1} \mathbb{E}_{X}\left(S_{2, r}(l)\right)
$$

The first summand can likewise be calculated to be

$$
\begin{aligned}
& \sum_{q=2}^{\text {even }} W\left(\tilde{\mathcal{A}}\left(J_{q}^{0}(\boldsymbol{i})\right)\right) \\
= & \left(l_{1}-1\right) \sum_{\substack{\boldsymbol{b} \in[p]^{K} \\
\boldsymbol{j} \in \mathcal{B}_{S_{1}}(l), \boldsymbol{b}}} W(\tilde{\mathcal{A}}(\boldsymbol{j}))=\left(l_{1}-1\right) \mathbb{E}_{X}\left(S_{1}(l)\right)
\end{aligned}
$$


$$
\mathbb{E}_{X}^{1}(l)=\left(n+l_{1}-1\right) \mathbb{E}_{X}\left(S_{1}(l)\right)+\sum_{r=1}^{l_{1}-1} \mathbb{E}_{X}\left(S_{2, r}(l)\right)
$$

The same idea can be used to calculate $\mathbb{E}_{X}^{2}(l)$. First define

$$
Q_{\boldsymbol{b}, \boldsymbol{c}}^{2}(\boldsymbol{i})=\left\{(k, q) \in\{2, \ldots, K\} \times \mathbb{N} \mid q<2 l_{k}, \boldsymbol{i}_{q}^{k}=\boldsymbol{b}, \boldsymbol{i}_{q+1}^{k}=\boldsymbol{c}\right\}
$$




---

$$
Q_{b, c(i)}^{3}=\left\{(k, q) \in\{2, \ldots, K\} \times \mathbb{N} \mid q \leq 2^{l_{k}}, i_{q}^{k}=c, i_{\left(q \bmod 2^{l_{k}}\right)+1}^{k}=b\right\}
$$

then again $\sum_{k=2}^{K} A_{b_{1}, c}\left(\tilde{G}_{i^{k}}\right)=\# Q_{b_{1}, c(i)}^{2}+\# Q_{b_{1}, c(i)}^{3}$ and all tuples $(k, q)$ from $Q_{b, c(i)}^{2}$ must have odd $q$ while all tuples $(k, q)$ from $Q_{b, c(i)}^{3}$ must have even $q$. For $J_{(k, q)}^{2}(i)$ as in the proof of Theorem 3.1, it holds that $\tilde{A}\left(J_{(k, q)}^{2}(i)\right)=\tilde{A}(i)-\tilde{M}_{b_{1}, c}$. Similarly for $(k, q) \in Q_{b_{1}, c(i)}^{3}$ define

$$
\left[i^{1}, i^{k}\right]_{q}:= \begin{cases}\underbrace{\left(i_{1}^{1}, \ldots, \underbrace{i_{2 l_{1}}^{1}}_{=c}, i_{q}^{k}, i_{q-1}^{k}, \ldots, i_{1}^{k}, i_{2 l_{k}}^{k}, i_{2 l_{k}-1}^{k}, \ldots, i_{q+2}^{k}\right)}_{=b_{1}}, & \text { if } q<2^{l_{k}} \\ \left(\underbrace{i_{1}^{1}}_{=b_{1}}, \ldots, \underbrace{i_{2 l_{1}}^{1}}_{=c}, i_{2 l_{k}}^{k}, i_{2 l_{k}-1}^{k}, \ldots, i_{2}^{k}\right), & \text { if } q=2^{l_{k}}\end{cases}
$$

and

$$
J_{(k, q)}^{3}=\left(\left[i^{1}, i^{k}\right]_{q}, i^{2}, \ldots, \widehat{i^{k}}, \ldots, i^{K}\right)
$$

then we also have $\tilde{A}\left(J_{(k, q)}^{3}(i)\right)=\tilde{A}(i)-\tilde{M}_{b_{1}, c}$ and can further decompose $E_{X}^{2}(l)$ into

$$
\begin{aligned}
& E_{X}^{2}(l)=\sum_{\substack{b \in[p]^{K} \\
c \in[p+n] \backslash[p]}} \sum_{i \in B_{l, b}} i_{2 l_{1}}^{1}=c \sum_{(k, q) \in Q_{b_{1}, c(i)}^{2}} W\left(\tilde{A}\left(J_{(k, q)}^{2}(i)\right)\right) \\
&+\sum_{\substack{b \in[p]^{K} \\
c \in[p+n] \backslash[p]}} \sum_{i \in B_{l, b}} i_{2 l_{k}}^{1}=c \sum_{(k, q) \in Q_{b_{1}, c(i)}^{3}} W\left(\tilde{A}\left(J_{(k, q)}^{3}(i)\right)\right) .
\end{aligned}
$$

The first summand is by the same steps as in (3.14) equal to $\sum_{k=2}^{K} l_{k} E_{X}\left(S_{3, k}(l)\right)$. Note that $\left(k, 2^{l_{k}}\right) \in Q_{b_{1}, c}^{3}$ is only possible, if $b_{k}=b_{1}$. This will ensure that we don't gain a factor of $n$ from the summation over $b_{k}$ in the case $q=2^{l_{k}}$ of the below calculation. The second summand is calculated to be

$$
\begin{aligned}
& \sum_{k=2}^{K} \sum_{q=2}^{2^{l_{k}} \text { even }} \sum_{\substack{b \in[p]^{K} c \in[p+n] \backslash[p] \\
i \in B_{l, b} \\
(k, q) \in Q_{b_{1}, c(i)}^{3}}} W\left(\tilde{A}\left(J_{(k, q)}^{3}(i)\right)\right) \\
= & \sum_{k=2}^{K} \sum_{q=2}^{2^{l_{k}} \text { even }} \sum_{\tilde{b} \in[p]^{K-1}} \sum_{j \in B_{S_{3}, k}(l), \tilde{b}} W(\tilde{A}(j)) \\
= & \sum_{k=2}^{K} l_{K} E_{X}\left(S_{3, k}(l)\right)
\end{aligned}
$$




---

and we have shown

$$
\mathrm{E}_{2} \mathrm{X}(\underline{l})=2 \sum_{k=2}^{K} l_{k} \mathrm{E} \mathrm{X}\left(S_{3, k}(\underline{l})\right)
$$

The equalities (3.18), (3.22) and (3.26) together prove

$$
\mathrm{EX}(\underline{l})=\left(n+l_{1}-1\right) \mathrm{E}(\underline{l})+\sum_{r=1}^{l_{1}-1} \mathrm{EX}\left(S_{2, r}(\underline{l})\right)+2 \sum_{k=2}^{K} l_{k} \mathrm{EX}\left(S_{3, k}(\underline{l})\right)
$$

# 4 Gaussian Orthogonal Ensemble 

### 4.1 Theorem (Recursion for mixed trace moments of the GOE)

For $K \in \mathbb{N}$ and any $\underline{l}=\left(l_{1}, \ldots, l_{K}\right) \in \mathbb{N}_{0}^{K}$ - with even $L:=l_{1}+\ldots+l_{K}$ - the following recursive properties hold.
a) If $l_{1}=0$, then $\mathrm{E} \tilde{\mathrm{Z}}(\underline{l})=n \mathrm{E} \tilde{\mathrm{Z}}\left(S_{0}(\underline{l})\right)$ for

$$
S_{0}\left(0, l_{2}, \ldots, l_{K}\right):=\left(l_{2}, \ldots, l_{K}\right)
$$

b) If $l_{1}>0$, then

$$
\mathrm{E} \tilde{\mathrm{Z}}(\underline{l})=\left(l_{1}-1\right) \mathrm{E}_{\tilde{\mathrm{Z}}}\left(S_{1}(\underline{l})\right)+\sum_{q=1}^{l_{1}-1} \mathrm{E} \tilde{\mathrm{Z}}\left(S_{2, q}(\underline{l})\right)+2 \sum_{k=2}^{K} l_{k} \mathrm{E} \tilde{\mathrm{Z}}\left(S_{3, k}(\underline{l})\right)
$$

where

$$
S_{1}(\underline{x}):=\left(l_{1}-2, l_{2}, \ldots, l_{K}\right)
$$

and $S_{2, q}$ as well as $S_{3, k}$ are as defined in Theorem 2.1.
As before in Theorem 2.1 the starting point

$$
\mathrm{E} \tilde{\mathrm{Z}}((,*))=\mathrm{E}\left[\operatorname{tr}(\tilde{\mathrm{Z}})^{0}\right]=n
$$

for $(K, L)=(1,0)$ allows for the calculation of all mixed moments when $L$ is even and for odd $L$ the mixed trace moment must be zero.

Proof. Like before, only property $(b)$ needs to be shown. In complete analogy to (2.4) we have

$$
\mathrm{E} \tilde{Z}(\underline{l})=\sum_{b_{1}, \ldots, b_{K} \in[n]} \sum_{\underline{i} \in I_{\underline{l}, \underline{b}}} \mathrm{E}\left[\prod_{k=1}^{K} \tilde{Z}_{i_{1}^{k}, i_{2}^{k}} \cdots \tilde{Z}_{i_{l_{k}-1}^{k}, i_{l_{k}}^{k}} \tilde{Z}_{i_{l_{k}}^{k}, i_{1}^{k}}\right]
$$




---

This time the mean has the form

$$
\begin{aligned}
& \mathbb{E}\left[\prod_{k=1}^{K} \tilde{Z}_{i_{1}^{k}, i_{2}^{k}}^{i_{2}^{k}} \cdots \tilde{Z}_{i_{l_{k}-1}^{k} i_{i_{l_{k}}^{k}}}^{i_{l_{k}}^{k}} \tilde{Z}_{i_{l_{k}}^{k}, i_{1}^{k}}^{i_{1}^{k}}\right] \\
& =\mathbb{1} \tilde{\mathbf{A}}^{(i)} \text { has even entries }\left(\prod_{\substack{v, w \in[n] \\
v<w}}\left(\tilde{A}_{v, w}^{(i)}-1\right)!!\right)\left(\prod_{v \in[n]} 2^{\frac{\tilde{A}_{v, v}(i)}{2}}\left(\tilde{A}_{v, v}(i)-1\right)!!\right. \\
& =: W\left(\tilde{\mathbf{A}}^{(i)}\right)
\end{aligned}
$$

which implies that it can with

$$
\tilde{\mathbf{M}}^{b, c}:=2\left(\mathbb{1}_{i=b, j=c \text { or } i=c, j=b}\right)_{i, j \in[n]}
$$

be decomposed into

$$
\begin{aligned}
& W\left(\tilde{\mathbf{A}}^{(i)}\right)=W\left(\tilde{\mathbf{A}}^{(i)}-\tilde{\mathbf{M}}^{b_{1}, c}\right) 2^{\mathbb{1}_{b_{1}=c}\left(\tilde{A}_{b_{1}, c}^{(i)}-1\right)} \\
& =W\left(\tilde{\mathbf{A}}^{(i)}-\tilde{\mathbf{M}}^{b_{1}, c}\right) 2^{\mathbb{1}_{b_{1}=c}\left(A_{b_{1}, c}\left(\tilde{g}_{i_{1}}\right)-1+\sum_{k=2}^{K} A_{b_{1}, c}\left(\tilde{g}_{i^{k}}\right)\right)}
\end{aligned}
$$

As is by now standard, we thus change (4.3) into

$$
\begin{aligned}
& \mathbb{E} \tilde{Z}(l)=\underset{\tilde{Z}^{(l)}}{\mathbb{E}_{1}}=\sum_{\substack{i^{1}, \ldots, i^{K} \in[n] \\
c \in[n]}} 2^{\mathbb{1}_{b_{1}=c}} \sum_{\substack{i \in I_{l, \underline{i}_{1}^{l_{1}=c}}}}^{\sum_{c \in[n], \underline{s}_{i=1}^{K} \in[n]}} W\left(\tilde{\mathbf{A}}^{(i)}-\tilde{\mathbf{M}}^{b_{1}, c}\right)\left(A_{b_{1}, c}\left(\tilde{g}_{i^{1}}\right)-1\right) \\
& +\underbrace{\sum_{\substack{i^{1}, \ldots, i^{K} \in[n] \\
c \in[n], \underline{s}_{i=1}^{n}}} 2^{\mathbb{1}_{b_{1}=c}} \sum_{\substack{i \in I_{l} \\
\underline{i}_{1}^{l_{1}=c}}} W\left(\tilde{\mathbf{A}}^{(i)}-\tilde{\mathbf{M}}^{b_{1}, c}\right) \sum_{k=2}^{k} a_{b_{1}, c}\left(\tilde{g}_{i^{k}}\right)}_{=: \tilde{z}_{2}^{(l)}} .
\end{aligned}
$$

For

$$
\begin{aligned}
& Q_{b, c}^{0}\left(\underline{i}^{1}\right):=\left\{q<l_{1} \mid i_{q}^{1}=c, i_{q+1}^{1}=b\right\} \\
& Q_{b, c}^{1}\left(\underline{i}^{1}\right):=\left\{q<l_{1} \mid i_{q}^{1}=b, i_{q+1}^{1}=c\right\}=Q_{c, b}^{0}\left(\underline{i}^{1}\right)
\end{aligned}
$$

it holds that $2^{\mathbb{1}_{b_{1}=c}}\left(A_{b_{1}, c}\left(\tilde{g}_{i^{1}}\right)-1\right)=\# Q_{b_{1}, c}^{0}\left(\underline{i}^{1}\right)+\# Q_{b_{1}, c}^{1}\left(\underline{i}^{1}\right)$ and with $J_{q}^{1}(i)$ as in (2.9) we for each $q \in Q_{b_{1}, c}^{1}\left(\underline{i}^{1}\right)$ have

$$
\tilde{\mathbf{A}}\left(J_{q}^{1}(i)\right)=\tilde{\mathbf{A}}^{(i)}-\tilde{\mathbf{M}}^{b_{1}, c}
$$

For each $q \in Q_{b_{1}, c}^{0}\left(\underline{i}^{1}\right)$ we similarly to (3.21) define

$$
\left\langle\underline{i}^{1}\right\rangle_{q}=\left(i_{1}^{1}, \stackrel{z}{=} b_{1}, \ldots, i_{q-1}^{1}, i_{l_{1}}^{1}, \stackrel{z}{=} c, i_{l_{1}-1}^{1}, \ldots, i_{q+3}^{1}, i_{q+2}^{1}\right) \in[n]^{l_{1}-2}
$$




---

and

$$
J_{q}^{0}:=\left(\left\langle i_{1}\right\rangle_{q}, i_{2}, \ldots, i_{K}\right)
$$

then it also follows that $\tilde{A}\left(J_{q}^{0}(i)\right)=\tilde{A}(i)-\tilde{M}_{b_{1}, c}$, since only the connections between $\left(i_{q}^{1}, i_{q+1}^{1}\right)=(c, b)$ and $\left(i_{l_{1}}^{1}, i_{1}^{1}\right)=(c, b)$ are removed by $J_{q}^{0}$. Using $J^{0}$ and $J^{1}$ we write $E_{\tilde{\mathcal{Z}}}(l)$ as

$$
\begin{aligned}
E_{\tilde{\mathcal{Z}}}(l)= & \sum_{\substack{b_{1}, \ldots, b_{k} \in[n] \\
c \in[n]}} \sum_{i \in I_{l, b}} \sum_{q \in Q_{b_{1}, c}^{0}\left(i_{1}\right)} \mathcal{W}\left(\tilde{A}\left(J_{q}^{0}\right)\right) \\
& +\sum_{\substack{b_{1}, \ldots, b_{k} \in[n] \\
c \in[n]}} \sum_{\substack{i \in I_{l, b} \\
i_{l_{1}}^{1}=c}} \sum_{q \in Q_{b_{1}, c}^{1}\left(i_{1}\right)} \mathcal{W}\left(\tilde{A}\left(J_{q}^{1}\right)\right)
\end{aligned}
$$

For the second summand the exact same steps as in (2.10) and (2.11) show that it must be equal to

$$
\sum_{q=1}^{l_{1}-1} E_{\tilde{\mathcal{Z}}}\left(S_{2, q}(l)\right)
$$

Combining the ideas of (2.10) and (3.22) we for the first summand observe

$$
\begin{aligned}
& \sum_{\substack{b_{1}, \ldots, b_{K} \in[n] \\
c \in[n]}} \sum_{i \in I_{l, b}} \sum_{q \in Q_{b_{1}, c}^{0}\left(i_{1}\right)} \mathcal{W}\left(\tilde{A}\left(J_{q}^{0}\right)\right)=\sum_{q=1}^{l_{1}-1} \sum_{\substack{b_{1}, \ldots, b_{K} \in[n] \\
c \in[n]}} \sum_{i \in I_{l, b}} \sum_{\substack{i_{l_{1}}^{1}=c \\
q \in Q_{b_{1}, c}^{0}\left(i_{1}\right)}} \mathcal{W}\left(\tilde{A}\left(J_{q}^{0}\right)\right) \\
& =\left(l_{1}-1\right) \sum_{b_{1}, \ldots, b_{K} \in[n]} \sum_{j \in I_{S_{1}(l), b}} \mathcal{W}(\tilde{A}(j))=\left(l_{1}-1\right) E_{\tilde{\mathcal{Z}}}\left(S_{1}(l)\right)
\end{aligned}
$$

where

$$
S_{1}(l):=\left(l_{1}-2, l_{2}, \ldots, l_{K}\right)
$$

We have thus shown

$$
E_{\tilde{\mathcal{Z}}}(l)=\left(l_{1}-1\right) E_{\tilde{\mathcal{Z}}}\left(S_{1}(l)\right)+\sum_{q=1}^{l_{1}-1} E_{\tilde{\mathcal{Z}}}\left(S_{2, q}(l)\right)
$$

With analogous steps to those used for the proof of (3.26) we will now calculate $E_{\tilde{\mathcal{Z}}}^{2}(l)$. First define

$$
\begin{array}{r}
Q_{b, c}^{2}(i):=\left\{(k, q) \in\{2, \ldots, K\} \times \mathbb{N} \mid q \leq l_{k}, i_{q}^{k}=b, i_{\left(q \bmod l_{k}\right)+1}^{k}=c\right\} \\
Q_{b, c}^{3}(i):=\left\{(k, q) \in\{2, \ldots, K\} \times \mathbb{N} \mid q \leq l_{k}, i_{q}^{k}=c, i_{\left(q \bmod l_{k}\right)+1}^{k}=b\right\}=Q_{c, b}^{2}(i)
\end{array}
$$




---

then we have $2^{1_{b_{1}=c}} \sum_{k=2}^{K} A_{b_{1}, c}\left(\tilde{G}_{i_{k}}\right)=\# Q_{b_{1}, c}^{2}(i)+\# Q_{b_{1}, c}^{3}(i)$. For $J_{(k, q)}^{2}(i)$ as in (2.13) it holds that $\tilde{A}\left(J_{(k, q)}^{2}(i)\right)=\tilde{A}(i)-\tilde{M}_{b_{1}, c} \mathbb{1}$ and for each $(k, q) \in Q_{b_{1}, c}^{3}(i)$ we similarly to (3.25) define

$$
\left[i^{1}, i^{k}\right]_{q}:=\left\{\begin{array}{l}
\left(\underbrace{i_{1}^{1}, \ldots, i_{l_{1}^{1}}^{1}}_{=b_{1}}, \underbrace{i_{q}^{k}, i_{q-1}^{k}, \ldots, i_{1}^{k}}_{=c}, i_{l_{k}}^{k}, i_{l_{k}-1}^{k}, \ldots, i_{q+2}^{k}\right), \text { if } q<l_{k} \\
\left(\underbrace{i_{1}^{1}}_{=b_{1}}, \ldots, \underbrace{i_{l_{1}}^{1}}_{=c}, i_{l_{k}}^{k}, i_{l_{k}-1}^{k}, \ldots, i_{2}^{k}\right), \text { if } q=l_{k}
\end{array}\right.
$$

and

$$
J_{(k, q)}^{3}=\left(\left[i^{1}, i^{k}\right]_{q}, i^{2}, \ldots, \widehat{i}^{k}, \ldots, i^{K}\right)
$$

Again by construction of $J^{3}$ it holds that $\tilde{A}\left(J_{(k, q)}^{3}(i)\right)=\tilde{A}(i)-\tilde{M}_{b_{1}, c} \mathbb{1}$ and we can decompose $E_{\tilde{\mathcal{Z}}(l)}^{2}$ into

$$
\begin{aligned}
E_{\tilde{\mathcal{Z}}(l)}^{2}= & \sum_{\substack{b_{1}, \ldots, b_{K} \in[n] \\
c \in[n]}} \sum_{\substack{i \in I_{l, b} \\
i_{l_{1}}^{1}=c}} \sum_{(k, q) \in Q_{b_{1}, c}^{2}(i)} W\left(\tilde{A}\left(J_{(k, q)}^{2}(i)\right)\right) \\
& +\sum_{\substack{b_{1}, \ldots, b_{K} \in[n] \\
c \in[n]}} \sum_{\substack{i \in I_{l, b} \\
i_{l_{1}}^{1}=c}} \sum_{(k, q) \in Q_{b_{1}, c}^{3}(i)} W\left(\tilde{A}\left(J_{(k, q)}^{3}(i)\right)\right)
\end{aligned}
$$

The first summand is by the same steps as in (2.14) equal to

$$
\sum_{k=2}^{K} l_{k} E_{\tilde{\mathcal{Z}}}\left(S_{3, k}(l)\right)
$$

and for the second summand the steps are again analogous to (2.14) and (3.26) and we find

$$
\begin{aligned}
& \sum_{\substack{b_{1}, \ldots, b_{K} \in[n] \\
c \in[n]}} \sum_{\substack{i \in I_{l, b} \\
i_{l_{1}}^{1}=c}} \sum_{(k, q) \in Q_{b_{1}, c}^{3}(i)} W\left(\tilde{A}\left(J_{(k, q)}^{3}(i)\right)\right) \\
& =\sum_{k=2}^{K} l_{k} \sum_{q=1}^{l_{k}} \sum_{\substack{b \in[n]^{K} \\
c \in[n]}} \sum_{\substack{i \in I_{l, b} \\
i_{l_{1}}^{1}=c \\
(k, q) \in Q_{b_{1}, c}^{3}(i)}} W\left(\tilde{A}\left(J_{(k, q)}^{3}(i)\right)\right) \\
& =\sum_{k=2}^{K} l_{k} \sum_{q=1}^{l_{k}} \sum_{\tilde{b} \in[n]^{K-1}} \sum_{i \in I_{l, \tilde{b}}} W(\tilde{A}(j)) \\
& =\sum_{k=2}^{K} l_{k} E_{\mathcal{\mathcal { Z }}}\left(S_{3, k}(l)\right)
\end{aligned}
$$




---

so we have shown

$$
E \tilde{\mathscr{Z}}_{(\mathbf{l})}=2 \sum_{k=2}^{K} l_{k} E \tilde{\mathscr{Z}}\left(S_{3, k}(\mathbf{l})\right)
$$

Finally equalities (4.6), (4.10) and (4.14) together yield

$$
E \tilde{\mathscr{Z}}_{(\mathbf{l})}=\left(l_{1}-1\right) E \tilde{\mathscr{Z}}\left(S_{1}(\mathbf{l})\right)+\sum_{q=1}^{l_{1}-1} E \tilde{\mathscr{Z}}\left(S_{2, q}(\mathbf{l})\right)+2 \sum_{k=2}^{K} l_{k} E \tilde{\mathscr{Z}}\left(S_{3, k}(\mathbf{l})\right)
$$

# List of symbols 

| $\mathbf{A}(G)$ | Adjacency matrix to a graph $G$ (see Definition 1.2) |
| :---: | :---: |
| $\mathbf{A}_{(i)}$ | Sum of adjacency matrices $\mathbf{A}\left(G_{i_{1}}\right), \ldots, \mathbf{A}\left(G_{i_{K}}\right)$ (see Definition 1.2) |
| $\tilde{\mathbf{A}}_{(i)}$ | Sum of adjacency matrices $\mathbf{A}\left(\tilde{G}_{i_{1}}\right), \ldots, \mathbf{A}\left(\tilde{G}_{i_{K}}\right)$ (see Definition 1.2) |
| $e_{q}^{k}$ | an edge in a graph/polygon (see Subsection 1.1 or Definition 1.2) |
| $E \mathscr{X}$ | Mixed trace moment of $\mathbf{X X}^{*}$ (see Introduction) |
| $E \mathscr{Y}$ | Mixed trace moment of $\mathbf{Y Y}^{*}$ (see Introduction) |
| $E \mathscr{Z}$ | Mixed trace moment of $\mathbf{Z}$ (see Introduction) |
| $E \tilde{\mathscr{Z}}$ | Mixed trace moment of $\tilde{\mathbf{Z}}$ (see Introduction) |
| $\varepsilon_{g}$ | number of different ways to glue edges of polygons (see Subsection 1.1) |
| $g$ | genus of a surface resulting from a polygon-gluing (see Subsection 1.1) |
| $G_{i}$ | a directed multi-graph such that $\underline{i}$ is an Euler-tour (see Definition 1.2) |
| $\tilde{G}_{i}$ | an undirected multi-graph such that $\underline{i}$ is an Euler-tour (see Definition 1.2) |
| $J_{(k, q)}^{0}$ | a locally defined operator on route sequences (see (3.21) or (4.9)) |
| $J_{(k, q)}^{1}$ | a locally defined operator on route sequences (see (2.9) or (3.10)) |
| $J_{(k, q)}^{2}$ | a locally defined operator on route sequences (see (2.13) or (3.13)) |
| $J_{(k, q)}^{3}$ | a locally defined operator on route sequences (see (3.25) or (4.13)) |
| $K$ | number of components to a layout $\mathbf{l}=\left(l_{1}, \ldots, l_{K}\right) \in \mathbb{N}_{0}^{K}$ (see Introduction) |
| $\mathbf{l}$ | a 'layout' $\mathbf{l}=\left(l_{1}, \ldots, l_{K}\right) \in \mathbb{N}_{0}^{K}($ see Introduction $)$ |




---





---

# References 

[1] Э. T. Ахмедов и Ш. Р. Шакиров, Соединения поверхностей с многоугольными границами, Функционал. Анал. и Применеn. 43 (2009), no. 4, 3-13, DOI 10.1007/s10688-009-0033-y (Русский, с русским summary); English transl., Funct. Anal. Appl. 43 (2009), no. 4, 245-253. MR2596651
[2] Greg W. Anderson, Alice Guionnet, and Ofer Zeitouni, An introduction to random matrices, Cambridge Studies in Advanced Mathematics, vol. 118, Cambridge University Press, Cambridge, 2010. MR2760897
[3] Olivier Bernardi, An analogue of the Harer-Zagier formula for unicellular maps on general surfaces, Adv. in Appl. Math. 48 (2012), no. 1, 164-180, DOI 10.1016/j.aam.2011.06.005. MR2845513
[4] Persi Diaconis and Steven N. Evans, Linear functionals of eigenvalues of random matrices, Trans. Amer. Math. Soc. 353 (2001), no. 7, 2615-2633, DOI 10.1090/S0002-9947-01-02800-8. MR1828463
[5] Uffe Haagerup and Steen Thorbjørnsen, Random matrices with complex Gaussian entries, Expo. Math. 21 (2003), no. 4, 293-337, DOI 10.1016/S0723-0869(03)80036-1. MR2022002
[6] J. Harer and D. Zagier, The Euler characteristic of the moduli space of curves, Invent. Math. 85 (1986), no. 3, 457-485, DOI 10.1007/BF01390325. MR848681
[7] D. M. Jackson, Some combinatorial problems associated with products of conjugacy classes of the symmetric group, J. Combin. Theory Ser. A 49 (1988), no. 2, 363-369, DOI 10.1016/0097$3165(88) 90062-3$. MR0964394
[8] Michel Ledoux and Brian Rider, Small deviations for beta ensembles, Electron. J. Probab. 15 (2010), no. 41, 1319-1343, DOI 10.1214/EJP.v15-798. MR2678393
[9] M. Ledoux, A recursion formula for the moments of the Gaussian orthogonal ensemble, Ann. Inst. Henri Poincaré Probab. Stat. 45 (2009), no. 3, 754-769, DOI 10.1214/08-AIHP184 (English, with English and French summaries). MR2548502
[10] Sandrine Péché, Universality results for the largest eigenvalues of some sample covariance matrix ensembles, Probab. Theory Related Fields 143 (2009), no. 3-4, 481-516, DOI 10.1007/s00440-0070133-7. MR2475670
[11] Jolanta Pielaszkiewicz, Dietrich Von Rosen, and Martin Singull, On $\mathrm{E}\left[\prod_{i=0}^{k} \operatorname{Tr}\left\{\mathbf{W}^{m_{i}}\right\}\right]$, where $\mathbf{W} \sim \mathcal{W}_{p}(l, n)$, Comm. Statist. Theory Methods 46 (2017), no. 6, 2990-3005, DOI 10.1080/03610926.2015.1053942. MR3579781
[12] Ya. Sinai and A. Soshnikov, Central limit theorem for traces of large random symmetric matrices with independent matrix elements, Bol. Soc. Brasil. Mat. (N.S.) 29 (1998), no. 1, 1-24, DOI 10.1007/BF01245866. MR1620151
[13] Ya. G. Sinaĭ and A. B. Soshnikov, A refinement of Wigner's semicircle law in a neighborhood of the spectrum edge for random symmetric matrices, Funktsional. Anal. i Prilozhen. 32 (1998), no. 2, 5679, 96, DOI 10.1007/BF02482597 (Russian, with Russian summary); English transl., Funct. Anal. Appl. 32 (1998), no. 2, 114-131. MR1647832
[14] Alexander Soshnikov, Universality at the edge of the spectrum in Wigner random matrices, Comm. Math. Phys. 207 (1999), no. 3, 697-733, DOI 10.1007/s002200050743. MR1727234
[15] , A note on universality of the distribution of the largest eigenvalues in certain sample covariance matrices, J. Statist. Phys. 108 (2002), no. 5-6, 1033-1056, DOI 10.1023/A:1019739414239. Dedicated to David Ruelle and Yasha Sinai on the occasion of their 65th birthdays. MR1933444
[16] Ekaterina Vassilieva, Moments of normally distributed random matrices given by generating series for connection coefficients - explicit bijective computation, Ann. Comb. 21 (2017), no. 3, 445-477, DOI 10.1007/s00026-017-0356-y. MR3685122




---

