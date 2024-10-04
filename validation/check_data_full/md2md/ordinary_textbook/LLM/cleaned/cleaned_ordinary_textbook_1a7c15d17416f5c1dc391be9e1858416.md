# 数学新星问题征解第九期解答 

2015.11

第一题：对任意实数集 $A$ ，定义 $A$ 的商集为

$$
Q(A)=\left\{\left.\frac{a-b}{c-d} \right\rvert\, a, b, c, d \in A, c \neq d\right\}
$$

求最小的正数 $\lambda$ ，使得对任意有限实数集 $A$ 有

$$
|Q(A)| \leq \lambda|A|^{4}
$$

(上海中学 王广廷 供题)

## 解法一 (根据湖南省雅礼中学刘哲成同学的解答整理):

所求 $\lambda$ 的最小值为 $\frac{1}{2}$.
一方面，我们证明对于任意的集合 $A$ ，均有 $|Q(A)| \leq \frac{1}{2}|A|^{4}$ 。
不妨设 $|A|=n$ 。
(i) 从 $A$ 中选出四个互不相同的元素，记为 $a, b, c, d$ 。则 $\binom{n}{4}$ 种选法，且每一种选法 $Q(A)$ 至多有 12 个值:
$\frac{a-b}{c-d}, \frac{b-a}{c-d}, \frac{c-d}{a-b}, \frac{d-c}{a-b}, \frac{a-c}{b-d}, \frac{c-a}{b-d}, \frac{b-d}{a-c}, \frac{d-b}{a-c}, \frac{a-d}{b-c}, \frac{d-a}{b-c}, \frac{b-c}{a-d}, \frac{c-b}{a-d}$.
(ii) 从 $A$ 中选出三个互不相同的元素, 记为 $a, b, c$ 。则共有 $\binom{n}{3}$ 种选法, 且每种选法 $Q(A)$ 至多有常数 0 及以下 12 个值:
$\frac{a-b}{a-c}, \frac{b-a}{a-c}, \frac{a-c}{a-b}, \frac{c-a}{a-b}, \frac{b-a}{b-c}, \frac{a-b}{b-c}, \frac{b-c}{a-b}, \frac{c-b}{a-b}, \frac{c-b}{c-a}, \frac{b-c}{c-a}, \frac{c-a}{c-b}, \frac{a-c}{c-b}$.
(iii) 从 $A$ 中选出两个互不相同的元素, 记为 $a, b$ 。从而至多有常数 1 和 0 属于 $Q(A)$.

综上，当 $n \geq 4$ 时，

$$
\begin{aligned}
|Q(A)| & \leq 12\binom{n}{4}+12\binom{n}{3}+2 \\
& =\frac{n(n-1)(n-2)(n-3)}{2}+2 n(n-1)(n-2)+2 \\
& =\frac{n^{4}}{2}-3 n^{3}+\frac{11}{2} n^{2}+3 n+2 n^{3}-6 n^{2}+4 n+2 \\
& =\frac{n^{4}}{2}-n^{3}-\frac{1}{2} n^{2}+7 n+2 \\
& \leq \frac{n^{4}}{2}
\end{aligned}
$$




---

又当 $n=1$ 时, $|Q(A)|=0 ; n=2$ 时, $|Q(A)|=2 ; n=3$ 时, $|Q(A)| \leq 14$ 均满足 $|Q(A)| \leq \frac{1}{2} n^{4}$. 所以 $(*)$ 成立.

另一方面, 我们证明 $\lambda$ 的最小值为 $\frac{1}{2}$ 。
为此，我们证明对于任意的 $n \in \mathbb{N}_{+}, n \geq 3$ ，均存在一个 $n$ 元子集 $A$ ，使得

$$
|Q(A)|=12\binom{n}{4}+12\binom{n}{3}+2
$$

只需证明从 $(i),(i i)$ 中得到的数各不相同且不为 0 或 1 。
我们用数学归纳法证明。
(1) 当 $n=3$ 时, 取 $A=\{1,2,4\}$, 即满足要求.
(2) 若 $n=k$ 时, $A=\left\{a_{1}, a_{2}, \cdots, a_{k}\right\}\left(a_{1}, a_{2}, \cdots, a_{k}\right.$ 互不相同 $)$ 满足要求.

考虑 $A^{\prime}=A \cup a_{k+1}$, 则 $\left|A^{\prime}\right|=k+1$. 设 $Q(A)$ 中的元素为 $x_{1}, x_{2}, \cdots, x_{m}$,又 $Q\left(A^{\prime}\right)$ 中包含 $a_{k+1}$ 的式子只有 $a_{k+1} a_{k+1}$ ，要求它们不等于 $0,1, x_{1}, \cdots, x_{m}$ ，至多解出有有限个 $a_{k+1}$ 不能取的值，但 $a_{k+1}$ 为实数，所以必有 $a_{k+1} \in \mathbb{R}$ 使得

$$
\left|Q\left(A^{\prime}\right)\right|=12\binom{n}{4}+12\binom{n}{3}+2
$$

所以 $(* *)$ 得证.
又由题意知, 对于任意的 $n \in \mathbb{N}_{+}$, 均有

$$
\frac{n^{4}}{2}-n^{3}-\frac{1}{2} n^{2}+\frac{7 n+2}{2} \leq \lambda n^{4}
$$

所以

$$
\lambda \geq \frac{1}{2}-\frac{1}{n}-\frac{1}{2 n^{2}}+\frac{7}{n^{3}}+\frac{2}{n^{4}}
$$

当 $n$ 充分大时, $\lambda \geq \frac{1}{2}$. 故 $\lambda_{\min }=\frac{1}{2}$.

# 解法二 (根据湖南省雅礼中学汤继尧同学的解答整理): $\lambda_{\text {min }}=\frac{1}{2}$. 

定义: $P(A)=\left\{\left.\frac{a}{b} \right\rvert\, a, b \in A, b \neq 0\right\}, \Delta(A)=\{a-b \mid a, b \in A\}, \Delta^{*}(A)=\{a-b \mid a, b \in A, a \neq b\}$, $\Delta^{+}(A)=\{a-b \mid a, b \in A, a>b\}, \Delta^{-}(A)=\Delta^{*}(A) \backslash \Delta^{+}(A)$.

所以由定义,

$$
Q(A)=P(\Delta(A)), \Delta(A)=\Delta^{*}(A) \cup\{0\}, \Delta^{*}(A)=\Delta^{+}(A) \cup \Delta^{-}(A)
$$

设 $A=\left\{a_{i} \mid i=1,2, \cdots, n, n \in \mathbb{N}^{*}\right\}$. 若 $n=1$, 则 $A=\left\{a_{1}\right\}$, 于是任取 $c, d \in A, c=d=a_{1}$, 则 $c-d=0, Q(A)=\varnothing$, 从而 $|Q(A)|=0<\lambda \cdot 1^{4}$ 对 $\lambda>0$恒成立。

下设 $n \geq 2, n \in \mathbb{N}^{*}$ ，考虑 $\Delta^{+}(A)$ 。不妨设 $a_{i}<a_{j}, 1 \leq i<j \leq n$ 。于是对




---

任意的 $x \in \Delta^{+}(A)$ ，存在 $i, j \in\{1,2, \cdots, n\}, i<j, x=a_{j}-a_{i}$ 。且对任给的 $1 \leq i<j \leq n, a_{j}-a_{i}>0$, 故 $a_{j}-a_{i} \in \Delta^{+}(A)$. 所以

$$
\Delta^{+}(A)=\left\{a_{j}-a_{i} \mid 1 \leq i<j \leq n\right\},\left|\Delta^{+}(A)\right| \leq \frac{n(n-1)}{2}
$$

类似知

$$
\Delta^{-}(A)=\left\{-x \mid x \in \Delta^{+}(A)\right\},\left|\Delta^{-}(A)\right| \leq \frac{n(n-1)}{2}
$$

因此

$$
\left|\Delta^{*}(A)\right| \leq n(n-1)
$$

现在考虑 $Q(A)=P(\Delta(A))$ 中的元素 $\frac{x}{y}, y \neq 0$ ，其必以下列形式之一：

1) $x=0, y \neq 0$ ，此时 $\frac{x}{y}=0$ ，
2) $x \neq 0,|x|=|y|$ ，此时 $\frac{x}{y}= \pm 1$ ，
3) $x \neq 0,|x| \neq|y|$ 此时, 记 $m=|x|, n=|y|$, 于是 $m, n \in \Delta^{+}(A)$.

这样的 $\left|\frac{x}{y}\right|=\frac{m}{n}$ 至多有 $2\binom{\Delta^{+}(A)}{2}$ 个, 从而 $\frac{x}{y}$ 的值 $\frac{m}{n},-\frac{m}{n}$ 至多有 $2 \times 2\binom{\left|\Delta^{+}(A)\right|}{2}$ 个,而 $2 \times 2\binom{\left|\Delta^{+}(A)\right|}{2} \leq 2\binom{\frac{n(n-1)}{2}}{\frac{n(n-1}{2}-\left.1\right)}$

$$
=\frac{1}{2} n(n-1)\left(n^{2}-n-2\right)
$$

故

$$
|Q(A)| \leq 3+\frac{1}{2} n(n-1)\left(n^{2}-n-2\right)=\frac{1}{2} n^{4}-n^{3}-\frac{1}{2} n^{2}+n+3 \text {. }
$$

注意到当 $A=\left\{2,2^{2}, \cdots, 2^{n}\right\}(n \geq 2)$ 时，由任意的 $1 \leq i_{1}<j_{1} \leq n, 1 \leq i_{2}<$ $j_{2} \leq n,\left(i_{1}, j_{1}\right) \neq\left(i_{2}, j_{2}\right)$ ，有 $2^{j_{1}}-2^{i_{1}} \neq 2^{j_{2}}-2^{i_{2}}$ ，所以 $\left|\Delta^{+}(A)\right|=\frac{n(n-1)}{2}$ ，从而 $|Q(A)|=\frac{1}{2} n(n-1)\left(n^{2}-n-2\right)+3$ ，故 $(1)$ 可取等.

为使 $|Q(A)| \leq \lambda|A|^{4}$ 恒成立，只要

$$
\frac{1}{2} n^{4}-n^{3}-\frac{1}{2} n^{2}+n+3 \leq \lambda n^{4}
$$

恒成立。
当 $\lambda=\frac{1}{2}$ 时， $(2)$ 式等价于 $\left(n^{3}-3\right)+\left(\frac{1}{2} n^{2}-n\right) \geq 0$ 成立。
当 $0<\lambda<\frac{1}{2}$ 时, $(2)$ 式等价于 $\left(\frac{1}{2}-\lambda\right) n^{4} \leq n^{3}+\frac{1}{2} n^{2}-n-3$.
但当 $n=\max \left\{\left[\frac{1}{\frac{1}{2}-\lambda} \cdot \frac{3}{2}\right]+1,2\right\}$ 时, $\left(\frac{1}{2}-\lambda\right) n^{4}>\frac{3}{2} n^{3}>n^{3}+\frac{1}{2} n^{2}-n-3$, 矛盾!
故 $\lambda \geq \frac{1}{2}$. 因此 $\lambda_{\min }=\frac{1}{2}$.
评注 昆明市第三中学杨怡嘉同学和昆明市滇池中学张晋源同学也给出了本题的正确解答.




---

第二题：一只青蛙生活在直角坐标平面上的格点上，它若跳跃，则从原点跳到距离为 1 的一个未经拜访的格点，并且使得海拔高度的绝对值之和最小，若这样的格点不存在，则任意跳到其中一点. 证明：这隻青蛙一定能回到原点.
(湖北武钢三中学生 王逸轩 供题)

# 解 (根据湖南省南雅中学刘其灵同学的解答整理): 

将青蛙经过的点染为红色，其余为蓝色.
记 $Q\left(a_{1} \sim b_{1}, a_{2} \sim b_{2}\right)=\left\{(x, y) \mid a_{1} \leq x \leq b_{1}, a_{2} \leq y \leq b_{2}, x, y \in \mathbb{Z}\right\}$.
引理1. 设 $a \in \mathbb{N}$, 若 $(a, 0)$ 在"岛"内，则由此向左走， $Q(0 \sim a, 0)$ 中点全部变红色时青蛙恰好?\ $Q(0 \sim a, 0)$ 以外部分。

证明：当 $a=0$ 时，已成立。
假设 $a=k$ 时，结论成立.
则当 $a=k+1$ 时, 青蛙跳到 $(k+1,0)$ 后:
若 $(k, 0)$ 已被"染红", 则由于 $(k+1,0)$ 在 $Q(0 \sim k, 0)$ 之外, 所以 $Q(0 \sim k, 0)$中点已全部被"染红"，此时 $Q(0 \sim k+1,0)$ 中点全部为红色。

若 $(k, 0)$ 未被染红，则由假设规则，若下一步至 $(k, 0)$ 。所以 $Q(0 \sim k, 0)$ 上被"染红"，青蛙恰好离开 $Q(0 \sim k, 0)$. 即无论怎样， $Q(0 \sim k+1,0)$ 上被"染红"，青蛙恰好离开 $Q(0 \sim k+1,0)$.

所以 $a=k+1$ 也成立, 故对任意 $a \in \mathbb{N}$, 引理1均成立.
引理2. 若 $Q(0 \sim a, b)$ 上被"染红"，且青蛙跳跃至 $(a, b+1)$ 。则由此向左走， $Q(0 \sim a, b+1)$ 上被"染红"，青蛙恰好离开 $Q(0 \sim a, b+1)$ 。

证法同引理1.
引理 3. 青蛙从 $x$ 轴正方向跳起直至跳至 $x$ 轴负方向，若青蛙经过点 $(a, b)$ ，则从其正东方向最远， $Q(0 \sim a, 0 \sim b)$ 上被"染红"，青蛙恰好离开 $Q(0 \sim a, 0 \sim b)$.

证明：设青蛙路径为 $A_{0} A_{1} \cdots A_{m}$ ( $A_{0}$ 在坐标轴上, 即 $x$ 轴正方向)。

当 $n=0$ 时，对 $A_{0}$ ，由引理1知其成立。
假设当 $n=k$ 时，对 $A_{k}$ ，由结论成立。则当 $n=k+1$ 时，
(1) 若 $A_{k+1}$ 由 $A_{k}$ 向上跳跃，设 $A_{k}\left(a_{k}, b_{k}\right), A_{k+1}\left(a_{k}, b_{k}+1\right), a_{k}, b_{k} \in \mathbb{N}$ 。则由于 $A_{k+1}$ 不在 $Q\left(0 \sim a_{k}, 0 \sim b_{k}\right)$ 中，所以青蛙跳到 $A_{k+1}$ 时 $Q\left(0 \sim a_{k}, 0 \sim b_{k}\right)$ 已全部为红色。由引理 2 ，得 $Q\left(0 \sim a_{k}, b_{k}+1\right)$ 上为红色青蛙恰好离开 $Q\left(0 \sim a_{k}, b_{k}+1\right)$ ，所以此时得证。




---

同理，若 $A_{k+1}$ 为 $A_{k}$ 往右下方格均可证。
(2) 若 $A_{k+1}$ 由 $A_{k}$ 往左上方格，则至少证命题仅包含归纳假设的一个时刻命题，已得证。

同理， $A_{k+1}$ 为 $A_{k}$ 往下或往左下方格也可证。
所以 $n=k+1$ 也成立，归纳证毕。
同理可从 $y$ 到可命名混合一二划线情况。
由引理3得:
引理 $\mathbf{3}^{\prime}$ 。设 $a, b \in \mathbb{N}$ ，若既划过 $(a, b)$ ，则从其到 $(a, b)$ 路径，必$(0 \sim a, 0 \sim b)$ 上被染红, 划线'user 逆时针从 $\mathcal{Q}(0 \sim a, 0 \sim b)$.

证明：若 $(a, b)$ 在左标号上，由引理 $1=$ 证。
若 $(a, b)$ 在第一划线，考察其最后一次划过左标号，其只能为 $x$ 到可命名或 $y$到可命名，由引理 3 判断其是否划完证。

回到原题. 若既划到 $(a, b)$ 且其四面上均已染红，不妨设其在第一划线及 $x, y$ 到可命名中（否则用代替左标号）。

划线在到 $(a, b)$ 之前曾划过 $(a, b+1)$ 与 $(a+1, b)$ 。不妨设划线先划过 $(a+1, b)$ ，后划过 $(a, b+1)$ ，因为 $(a, b+1)$ 不在 $\mathcal{Q}(0 \sim a+1,0 \sim b)$ 中，由引理 $3 '$知有划线到 $(a, b+1)$ 时， $\mathcal{Q}(0 \sim a+1,0 \sim b)$ 上均已染红，而划线之后又会划过 $(a, b)$ ，矛盾。

所以划线可无穷哀竭。
(王海粟 供题)

第三题: 给定无理数 $\alpha$, 正整数 $n \geq 2$. 证明: 将 $\{\alpha\},\{2 \alpha\}, \cdots,\{n \alpha\}$ 从大到可重新排序后, 所有相邻两数之差的绝对值至多取 3 个不同的值. 其中 $\{x\}$表示 $x$ 的小数部分.
(湖北 边红平 供题)
证明 (根据上海中学张天怡同学的解答整理):
对 $1 \leq|p| \leq n$, 设
$\{p \alpha\}=\min \{-\{n \alpha\},\{-(n-1) \alpha\}, \cdots,-\{\alpha\},\{\alpha\},\{2 \alpha\}, \cdots,\{n \alpha\}\}$
不妨设 $1 \leq p \leq n$ ，否则用 $-\alpha$ 代替 $\alpha$ ，由于 $\alpha \notin \mathbb{Q}$ ，所以 $\{-k \alpha\}=1-\{k \alpha\}, k=$ $1,2, \cdots, n$.

再设
$\{-q \alpha\}=\min \{\{k \alpha\} \mid k \in \mathbb{Z}, 0<|k| \leq n, p \nmid k\}, 0<|q| \leq n, p \nmid q$.




---

对 q , 我们有如下性质:
(A) $\{-q \alpha\}>\{p \alpha\}$ 。否则由 $p$ 的定义得 $\{-q \alpha\}=\{p \alpha\}$ ，从而 $(p+q) \alpha \in \mathbb{Z}$.因为 $\alpha \notin \mathbb{Q}$, 所以 $p+q=0$, 这与 $p \nmid q$ 矛盾.
(B) $1 \leq q \leq n$. 否则 $q<0$, 考虑 $\{-(p+q) \alpha\}=\{-q \alpha\}-\{p \alpha\}<\{-q \alpha\}$,而 $|p+q|=|| p|-| q|| \leq \max \{|p|,|q|\} \leq n$ ， 且由于 $p \nmid q$ ，故 $p \nmid p+q$ 。特别地， $p+q \neq 0$ 。 这与 $\{-q \alpha\}$ 的最小性矛盾! 所以 $1 \leq q \leq n$, 特别地, 由上述证明可知 $p+q>n$.
(C) $\{q \alpha\}=\max \{\{k \alpha\} \mid k \in \mathbb{Z}, 1 \leq k \leq n\}$ 。若不然，设 $1 \leq q^{\prime} \neq q \leq n$ 满足 $\left\{q^{\prime} \alpha\right\}>\{q \alpha\}$ ，则由于 $\alpha \notin \mathbb{Q}$ ，得 $1-\left\{-q^{\prime} \alpha\right\}<1-\{q \alpha\}$ ，即 $0<\left\{-q^{\prime} \alpha\right\}<$ $\{-q \alpha\}$ 。 而由 $\left\{\left(q^{\prime}-q\right) \alpha\right\}=\{-q \alpha\}-\left\{-q^{\prime} \alpha\right\}$, 得 $\left\{\left(q^{\prime}-q\right) \alpha\right\}<\{-q \alpha\}$ 。因为 $0<\left|q^{\prime}\right| \leq n, 0<\left|q-q^{\prime}\right| \leq n-1<n$ ，故由 $\{q \alpha\}$ 的最小性， $p \mid q^{\prime}$ 且 $p \mid q^{\prime}-q$ ，得 $p \mid q$, 矛盾!

回到原题. 下面我们证明：对任意 $1 \leq k \leq n, k \neq q$ ，介在 $\{k \alpha\}$ 后面的数与 $\{k \alpha\}$ 的差是 $\{p \alpha\},\{-q \alpha\}$ 与 $\{p \alpha\}+\{-q \alpha\}$ 之一。
(i) 若 $k \leq n-p$, 则 $k+p \leq n$ 。由 $\{(k+p) \alpha\} \geq\{p \alpha\}$, 得 $\{k \alpha\}=\{(k+p) \alpha\}-$ $\{p \alpha\}$ 。若存在 $k^{\prime} \in\{1,2, \cdots, n\}$ ，使得 $\{k \alpha\}<\left\{k^{\prime} \alpha\right\}<\{(k+p) \alpha\}$ ，则

$$
\left\{\left(k-k^{\prime}\right) \alpha\right\}=\left\{k^{\prime} \alpha\right\}-\{k \alpha\}<\{(k+p) \alpha\}-\{k \alpha\}=\{p \alpha\} .
$$

这与 $\left|k^{\prime}-k\right| \leq n-1<n$ 矛盾!
(ii) 若 $k>q>n-p$, 则 $k-q>0$. 由于 $k-q \leq n-q<p$, 得 $p \nmid k-q$ 。从而 $\{(k+p) \alpha\} \geq\{-q \alpha\}$ ，故 $\{k \alpha\}=\{(k-q) \alpha\}-\{-q \alpha\}$ 。 若存在 $k^{\prime} \in\{1,2, \cdots, n\}$ ，使得 $\{k \alpha\}<\left\{k^{\prime} \alpha\right\}<\{(k-q) \alpha\}$ ，则

$$
\left\{\left(k^{\prime}-k\right) \alpha\right\}=\left\{k^{\prime} \alpha\right\}-\{k \alpha\}<\{-q \alpha\}, \quad\left\{\left(k-k^{\prime}-q\right) \alpha\right\}=\{(k-q) \alpha\}-\left\{k^{\prime} \alpha\right\}<\{-q \alpha\}
$$

因为 $\left|k^{\prime}-k\right| \leq n-1<n,|(k-q)-k^{\prime}| \leq n-1<n$ ，故由 $\{-q \alpha\}$ 定义，得 $p \mid k^{\prime}-k, p \mid(k-q)-k^{\prime}$, 从而 $p \mid q$, 矛盾!
(iii) 若 $n-p<k<q$, 则 $\{k \alpha\} \leq\{q \alpha\}$ 。又由于 $1 \leq q-k<q-n+p \leq p$,故由 $\{p \alpha\}$ 定义及 $\alpha \notin \mathbb{Q}$ 知 $\{p \alpha\}<\{(q-k) \alpha\}=\{q \alpha\}-\{k \alpha\}$ 。从而

$$
\{k \alpha\}+\{p \alpha\}+\{-q \alpha\}<\{q \alpha\}+\{-q \alpha\}=1
$$

故 $\{k \alpha\}+\{p \alpha\}+\{-q \alpha\}<\{(k+p-q) \alpha\}$ 。此时，由 $n-p<k<q$ ，得 $0 \leq n-q<$ $k+p-q<p \leq n$ 。 若存在 $k^{\prime} \in\{1,2, \cdots, n\}$ ，使得 $\{k \alpha\}<\left\{k^{\prime} \alpha\right\}<\{(k+p-q) \alpha\}$ 。分情况讨论:




---

a) 若 $p \mid k^{\prime}-k$ ，则由 $p \nmid q$ 知 $p \nmid k+p-q-k^{\prime}$ 。由于 $-n<k^{\prime}-k<n-(n-p)=p$,故 $\left\{k^{\prime} \alpha\right\}-\{k \alpha\}=\left\{\left(k^{\prime}-k\right) \alpha\right\}>\{p \alpha\}$. 又

$$
\left|k+p-q-k^{\prime}\right|<\max \left\{|k+p-q|,\left|k^{\prime}\right|\right\} \leq n
$$

从而 $\{(k+p-q) \alpha\}-\left\{k^{\prime} \alpha\right\}=\left\{\left(k+p-q-k^{\prime}\right) \alpha\right\} \geq\{-q \alpha\}$ 。
诸入可known矛盾。
b) 若 $p \nmid k^{\prime}-k$ ，则由 $\left|k^{\prime}-k\right| \leq n-1<n$ ，得 $\left\{k^{\prime} \alpha\right\}-\{k \alpha\}=\left\{\left(k^{\prime}-k\right) \alpha\right\} \geq$ $\{-q \alpha\}$. 又 $-n \leq-k^{\prime}<k+p-q-k^{\prime}<p-k^{\prime}<p$, 故

$$
\{(k+p-q) \alpha\}-\left\{k^{\prime} \alpha\right\}=\left\{\left(k+p-q-k^{\prime}\right) \alpha\right\}>\{p \alpha\}
$$

诸入也可知矛盾。
综上知原命题成立，证毕!
第四题：命题：设 $0<x_{1} \leq x_{2} \leq \cdots \leq x_{n}$ 满足 $x_{1} x_{2} \cdots x_{n}=1$ ，则

$$
\frac{x_{1}}{1}+\frac{x_{2}}{2}+\cdots+\frac{x_{n}}{n} \geq \frac{x_{1}^{-1}}{1}+\frac{x_{2}^{-2}}{2}+\cdots+\frac{x_{n}^{-n}}{n}
$$

(1) 证明上述命题对 $n=3$ 成立;
(2)* 对一般的 $n$ 证明或否定上述命题.

(上海新星培训学校 供题)
证明（根据供题者的解答整理）：
（1）仅为凑趣，记 $a=x^{3} ， b=x^{2} ， c=x^{1}$ 。由条件得 $a \geq 1 \geq c, a \geq b, a \geq$ $\frac{1}{b^{2}}$ ，从而

$$
\begin{aligned}
a^{3}+b^{2}+c & -\frac{1}{a^{3}}-\frac{1}{b^{2}}-\frac{1}{c}=a^{3}+b^{2}+\frac{1}{a b}-\frac{1}{a^{3}}-\frac{1}{b^{2}}-\frac{a b}{a^{3}} \\
& \geq a^{3}+\frac{1}{a}+\frac{1}{a^{2}}-\frac{1}{a^{3}}-a-a^{2}=\frac{(a-1)^{3}(a+1)\left(a^{2}+a+1\right)}{a^{3}} \geq 0
\end{aligned}
$$

因此原不等式得证。
（2）对一般的 $n$ 的情形尚未有完整的正解，但部分结果是有的。而且该不等式比较强，即对于 $n=4$ 的情况要人们去思考可能是一个既有难度又有一定强度的问题。

评注 公开考税务局数据据显示全国近千万考生只有 1 人做对本题第一问的正解. 据说这考生同时被北大和清华录取。




---

