# 一道不等式问题的探究  

刘浩宇（杭州市第二中学，310052）2017年秋季新星数学奥林匹克第4题是如下一道不等式  

题1．给定正整数 $n\geq2$ ，求最小的实数 $c$ ，使得对任意非负实数 $a_{1},a_{2},\cdot\cdot\cdot$  $a_{n}$ ，都存在 $i\in\{1,2,\cdots,n\}$ ，满足 $a_{i-1}+a_{i+1}\leq c a_{i}$ ，其中 $a_{0}=a_{n+1}=0$  

冷岗松教授指出，这道题是由2013年罗马尼亚国家队选拔考试的一道题改编而成，是一类KyFan型不等式  

题2．已知 $n$ 为正整数， $x_{1},x_{2},\cdot\cdot\cdot,x_{n}$ 为正实数，证明：  

$$
\begin{array}{c}{\displaystyle\operatorname*{min}\left\{x_{1},\frac{1}{x_{1}}+x_{2},\cdots,\frac{1}{x_{n-1}}+x_{n},\frac{1}{x_{n}}\right\}\leq2\cos\displaystyle\frac{\pi}{n+2}}\\ {\leq\,\operatorname*{max}\left\{x_{1},\frac{1}{x_{1}}+x_{2},\cdots,\frac{1}{x_{n-1}}+x_{n},\frac{1}{x_{n}}\right\}.}\end{array}
$$  

$\begin{array}{r}{\frac{a_{i-1}}{a_{i}}+\frac{a_{i+1}}{a_{i}}\leq c,}\end{array}$   $\begin{array}{r}{x_{i}=\frac{a_{i+1}}{a_{i}}\;1\leq i\leq n.}\end{array}$  就变成了与题2相同的结构，此时题2的下标 $n$ 应改为 $n-1$ ，从而题1的最佳常数 $\begin{array}{r}{c=2\cos{\frac{\pi}{n+1}}}\end{array}$  

吴尉迟博士在讲评试卷时利用归纳法证明了题1，而题2的官方解答中先 $\textstyle x_{1}={\frac{1}{x_{1}}}+x_{2}=\cdots={\frac{1}{x_{n-1}}}+x_{n}={\frac{1}{x_{n}}}$  了两边的不等式，而我的证明方法有所不同，  

设最佳常数 $c\,=\,c(n)$ ，对较小的 $n$ ，考虑一组使不等式的等号均成立的 $\left(a_{1},\cdot\cdot\cdot\,,a_{n}\right)$   $c(2)=1$   $c(3)={\sqrt{2}}$   $\begin{array}{r}{c(4)\,=\,\frac{\sqrt{5}+1}{2}}\end{array}$   $c(5)=\sqrt{3}$   $\begin{array}{r}{c(n)=2\cos{\frac{\pi}{n+1}}}\end{array}$ ．看到这个结果之后，我联想到了一道以前在学校里做过的不等式问题：  

题3．已知  $a_{1},a_{2},\cdot\cdot\cdot\mathbf{\Omega},a_{n}$  为不全为〇的实数，求  

$$
\frac{a_{1}a_{2}+a_{2}a_{3}+\cdot\cdot\cdot+a_{n-1}a_{n}}{a_{1}^{2}+a_{2}^{2}+\cdot\cdot\cdot+a_{n}^{2}}
$$  

的最大值.  

这道题的想法是利用均值不等式平衡系数，即利用如下 $n-1$ 个不等式  

$$
\begin{array}{c}{{2a_{1}a_{2}\leq\lambda_{1}a_{1}^{2}+\displaystyle\frac{1}{\lambda_{1}}a_{2}^{2},}}\\ {{2a_{2}a_{3}\leq\lambda_{2}a_{2}^{2}+\displaystyle\frac{1}{\lambda_{2}}a_{3}^{2},}}\end{array}
$$  

$$
2a_{n-1}a_{n}\leq\lambda_{n-1}a_{n-1}^{2}+\frac{1}{\lambda_{n-1}}a_{n}^{2}.
$$  

相加后，为使右边 $a_{1}^{2},a_{2}^{2},\cdot\cdot\cdot\mathbf{\partial},a_{n}^{2}$ 的系数相同，考虑找出 $\lambda_{1},\cdot\cdot\cdot\,,\lambda_{n-1}\in\mathbb{R}$ ，使得  

$$
\lambda_{1}={\frac{1}{\lambda_{1}}}+\lambda_{2}={\frac{1}{\lambda_{2}}}+\lambda_{3}=\cdot\cdot\cdot={\frac{1}{\lambda_{n-2}}}+\lambda_{n-1}={\frac{1}{\lambda_{n-1}}}+\lambda_{n},
$$  

这里 $\lambda_{n}=0$ ，我们要求的最大值即为 $\frac{\lambda_{1}}{2}$  

这是一个递推数列，满足 $\begin{array}{r}{\lambda_{k+1}\:=\:\lambda_{1}\,-\,\frac{1}{\lambda_{k}}}\end{array}$  $(1\,\leq\,k\,\leq\,n\,-\,1)$ ．容易知道 $\begin{array}{r}{0<\frac{\lambda_{1}}{2}\leq1}\end{array}$ (因为最小值为 $\lambda_{1}$ ，显然不超过 2),我们可设 $\textstyle\lambda_{1}=2\cos\alpha,\,\alpha\in(0,\frac{\pi}{2}]$ 则有  

$$
\begin{array}{l c r}{\displaystyle{\lambda_{2}=2\cos\alpha-\frac{1}{2\cos\alpha}=\frac{3-4\sin^{2}\alpha}{2\cos\alpha}=\frac{\sin3\alpha}{\sin2\alpha},}}\\ {\displaystyle{\lambda_{3}=2\cos\alpha-\frac{\sin2\alpha}{\sin3\alpha}=\frac{2\sin3\alpha\cos\alpha-\sin2\alpha}{\sin3\alpha}=\frac{\sin4\alpha}{\sin3\alpha}.}}\end{array}
$$  

$\begin{array}{r}{\lambda_{k}=\frac{\sin(k+1)\alpha}{\sin k\alpha}}\end{array}$  

$$
\sin(k-1)\alpha+\sin(k+1)\alpha=2\sin k\alpha\cos\alpha.
$$  

$\lambda_{n}~=~0$   $\sin(n+1)\alpha\;=\;0$   $\begin{array}{r}{\alpha\ =\ \frac{\pi}{n+1}}\end{array}$   $\begin{array}{r}{\frac{\lambda_{1}}{2}=\cos\frac{\pi}{n+1}}\end{array}$   $\begin{array}{r}{\lambda_{k}a_{k}^{2}=\frac{1}{\lambda_{k}}a_{k+1}^{2}}\end{array}$   $1\leq k\leq n-1$  

$$
{\frac{a_{k+1}}{a_{k}}}=\lambda_{k}={\frac{\sin(k+1)\alpha}{\sin k\alpha}},\ 1\leq k\leq n-1,
$$  

也即  

这道题的答案与题1的答案如此相似，是否可以类似地完成？经过尝试，我发现是可以的.  

由于 $a_{1},\cdot\cdot\cdot\,,a_{n}\geq0$ ，故我们只需证明如下不等式  

$$
\begin{array}{l}{{a_{2}^{2}+(a_{1}+a_{3})^{2}\!+\!(a_{2}+a_{4})^{2}+\cdot\cdot\cdot+(a_{n-2}+a_{n})^{2}+a_{n-1}^{2}}}\\ {{\mathrm{~}\quad\quad\quad\leq4\cos^{2}{\displaystyle\frac{\pi}{n+1}}(a_{1}^{2}+a_{2}^{2}+\cdot\cdot\cdot+a_{n}^{2}).}}\end{array}
$$  

这样必存在一个 $i\in\{1,2,\cdot\cdot\cdot\ ,n\}$ 使得 $a_{i-1}+a_{i+1}\leq c a_{i}$ ，其中 $a_{0}=a_{n+1}=0$  

为证明式 (2)，我们考虑 $n-2$ 个局部的Cauchy不等式  

$$
\left(a_{k-1}+a_{k+1}\right)^{2}\leq\bigl(\frac1{\lambda_{k-1}}+\lambda_{k}\bigr)\bigl(\lambda_{k-1}a_{k-1}^{2}+\frac1{\lambda_{k}}a_{k+1}^{2}\bigr),\;\;k=2,3,\cdots,n-1.
$$  

利用类似的方法，我们可求得 $\begin{array}{r}{\lambda_{k}\;=\;\frac{\sin(k+1)\alpha}{\sin k\alpha}}\end{array}$  $k\,=\,1,2,\cdot\cdot\cdot\;,n\,-\,1$  $\textstyle\alpha={\frac{\pi}{n+1}}.$  

这时，注意到  

$$
{\frac{1}{\lambda_{k-1}}}+\lambda_{k}={\frac{\sin(k-1)\alpha}{\sin k\alpha}}+{\frac{\sin(k+1)\alpha}{\sin k\alpha}}=2\cos\alpha,
$$  

将 (3)对  $k=2,3,\cdot\cdot\cdot\;,n-1$  求和得  

$$
\begin{array}{l}{\displaystyle(a_{1}+a_{3})^{2}+(a_{2}+a_{4})^{2}+\cdot\cdot\cdot+(a_{n-2}+a_{n})^{2}}\\ {\displaystyle\leq2\cos\alpha\left((\frac{\sin2\alpha}{\sin\alpha}a_{1}^{2}+\frac{\sin2\alpha}{\sin3\alpha}a_{3}^{2})+(\frac{\sin3\alpha}{\sin2\alpha}a_{2}^{2}+\frac{\sin3\alpha}{\sin4\alpha}a_{4}^{2})\right.}\\ {\displaystyle\left.\quad+\cdot\cdot+(\frac{\sin(n-1)\alpha}{\sin(n-2)\alpha}a_{n-2}^{2}+\frac{\sin(n-1)\alpha}{\sin n\alpha}a_{n}^{2})\right),}\end{array}
$$  

两边加上 $a_{2}^{2}+a_{n-1}^{2}$ ，此时，(4)的左边即为(2)的左边，而右边 $a_{1}^{2}$ 的系数为

 $\begin{array}{r}{2\cos\alpha\cdot\frac{\sin2\alpha}{\sin\alpha}\,=\,4\cos^{2}\alpha}\end{array}$  $a_{n}^{2}$ 的系数为 $\begin{array}{r}{2\cos\alpha\cdot\frac{\sin\left(n-1\right)\alpha}{\sin n\alpha}\,=\,4\cos^{2}\alpha}\end{array}$ ， $a_{2}^{2}$ 的系数为

 $\begin{array}{r}{2\cos\alpha\!\cdot\!\frac{\sin3\alpha}{\sin2\alpha}\!+\!1=\frac{\sin3\alpha}{\sin\alpha}\!+\!1=2\cos\alpha,\,a_{n-1}^{2}}\end{array}$   $\begin{array}{r}{2\cos\alpha\!\cdot\!\frac{\sin(n-2)\alpha}{\sin(n-1)\alpha}\!+\!1=2\cos\alpha}\end{array}$  对 $3\leq k\leq n-2,$  $a_{k}^{2}$ 的系数为 $\begin{array}{r}{2\cos\alpha\cdot\big(\frac{\sin(k+1)\alpha}{\sin k\alpha}+\frac{\sin(k-1)\alpha}{\sin k\alpha}\big)=4\cos^{2}\alpha}\end{array}$  

$$
\begin{array}{r l}&{a_{2}^{2}+(a_{1}+a_{3})^{2}\!+\!(a_{2}+a_{4})^{2}+\cdot\cdot\cdot+(a_{n-2}+a_{n})^{2}+a_{n-1}^{2}}\\ &{\qquad\qquad\leq4\cos^{2}\alpha(a_{1}^{2}+a_{2}^{2}+\cdot\cdot\cdot+a_{n}^{2}).}\end{array}
$$  

这就是 (2)式  

$\begin{array}{r}{\frac{a_{k+1}}{a_{k-1}}=\frac{\sin(k+1)\alpha}{\sin(k-1)\alpha}}\end{array}$   $a_{k}=\sin{k\alpha}$   $1\leq k\leq n$  可得到 $c$ 的最大值就是 $2\cos{\frac{\pi}{n+1}}$ ，这就解决了题1.  

冷岗松教授同时还指出一道类似的问题  

题4.（第二期新星征解第4题）设 $a_{1},a_{2},\cdot\cdot\cdot\,,a_{n}$ 是实数，证明：  

$$
\sum_{k=1}^{n+1}(a_{k}-a_{k-1})^{2}\leq2(1+\cos{\frac{\pi}{n+1}})\sum_{k=1}^{n}a_{k}^{2},
$$  

其中 $a_{0}=a_{n+1}=0$  

事实上，题4等价于  

$$
2\cos{\frac{\pi}{n+1}}\sum_{k=1}^{n}a_{k}^{2}+2\sum_{k=2}^{n}a_{k-1}a_{k}\geq0.
$$  

当 $a_{1},a_{2},\cdot\cdot\cdot\,,a_{n}$ 不全为0时 (否则显然)，即为  

$$
{\frac{a_{1}a_{2}+a_{2}a_{3}+\cdot\cdot\cdot+a_{n-1}a_{n}}{a_{1}^{2}+a_{2}^{2}+\cdot\cdot\cdot+a_{n}^{2}}}\geq-\cos{\frac{\pi}{n+1}}.
$$  

左边就是题3中的左边表达式，其证明也是类似的．只需将题3证明中的均值不等式改为  

$$
-2a_{k}a_{k+1}\leq\frac{\sin\frac{k+1}{n+1}\pi}{\sin\frac{k}{n+1}\pi}a_{k}^{2}+\frac{\sin\frac{k}{n+1}\pi}{\sin\frac{k+1}{n+1}\pi}a_{k+1}^{2},\,\,\,1\leq k\leq n-1.
$$  

再对 $k=1,2,\cdot\cdot\cdot\,,n-1$ 求和即可．不等式的取等条件为 $\begin{array}{r}{a_{k}=(-1)^{k}\cdot c\cdot\sin{\frac{k\pi}{n+1}}}\end{array}$ 这里 $c$ 为不等于0的常数或 $a_{k}=0$  $0\leq k\leq n+1$ (这是平凡的)  

所以，我们有以下结论：  

对不全为〇的实数 $a_{1},a_{2},\cdot\cdot\cdot\,,a_{n}$ 有  

$$
-\cos\frac{\pi}{n+1}\leq\frac{a_{1}a_{2}+a_{2}a_{3}+\cdot\cdot\cdot+a_{n-1}a_{n}}{a_{1}^{2}+a_{2}^{2}+\cdot\cdot\cdot+a_{n}^{2}}\leq\cos\frac{\pi}{n+1}.
$$  

这个表达式  

$$
\frac{a_{1}a_{2}+a_{2}a_{3}+\cdot\cdot\cdot+a_{n-1}a_{n}}{a_{1}^{2}+a_{2}^{2}+\cdot\cdot\cdot+a_{n}^{2}}
$$  

的上下界互为相反数，这也是从它的形式中可以预见到的  

通过以上几个问题，我们发现在一些利用二元均值，柯西不等式证明的不等式中，等式 $\sin(k-1)\alpha+\sin(k+1)\alpha=2\sin k\alpha\cos\alpha$ 起着关键作用.  

我们再来研究一些形式类似的问题.以下两题均出自《不等式的秘密》一书.  

题5．对任意实数 $x_{1},x_{2},\cdot\cdot\cdot\mathbf{\Omega},x_{n}$  

$$
x_{1}^{2}+(x_{1}+x_{2})^{2}+\cdot\cdot\cdot+(x_{1}+x_{2}+\cdot\cdot\cdot+x_{n})^{2}\leq t(x_{1}^{2}+x_{2}^{2}+\cdot\cdot\cdot+x_{n}^{2})
$$  

均成立，求 $t$ 的最小值  

解待定 $c_{1},c_{2},\cdot\cdot\cdot\ ,c_{n}$ 为正实数，由 Cauchy 不等式  

$$
(x_{1}+x_{2}+\cdot\cdot\cdot+x_{k})^{2}\leq(c_{1}+c_{2}+\cdot\cdot\cdot+c_{n})(\frac{x_{1}^{2}}{c_{1}}+\frac{x_{2}^{2}}{c_{2}}+\cdot\cdot\cdot+\frac{x_{k}^{2}}{c_{k}}).
$$  

将(5)对 $k=1,2,\cdots,n$ 求和，可得  

$$
\begin{array}{r l}&{x_{1}^{2}\!+\!(x_{1}+x_{2})^{2}+\cdot\cdot\cdot+(x_{1}+x_{2}+\cdot\cdot\cdot+x_{n})^{2}}\\ &{\quad\leq\frac{s_{1}+s_{2}+\cdot\cdot\cdot+s_{n}}{c_{1}}x_{1}^{2}+\frac{s_{2}+\cdot\cdot\cdot+s_{n}}{c_{2}}x_{2}^{2}+\cdot\cdot\cdot+\frac{s_{n}}{c_{n}}x_{n}^{2},}\end{array}
$$  

这里 $s_{k}=c_{1}+c_{2}+\cdot\cdot\cdot+c_{k},k=1,2,\cdot\cdot\cdot,n.$ 下面考虑选取 $c_{1},c_{2},\cdot\cdot\cdot\ ,c_{n}$ 使得 (6)中各 $x_{i}^{2}$ 的系数相等．即  

$$
{\frac{s_{1}+s_{2}+\cdot\cdot\cdot+s_{n}}{c_{1}}}={\frac{s_{2}+\cdot\cdot\cdot+s_{n}}{c_{2}}}=\cdot\cdot\cdot={\frac{s_{n}}{c_{n}}}=t.
$$  

也即 $\begin{array}{r}{\frac{s_{1}}{c_{1}-c_{2}}=\frac{s_{2}}{c_{2}-c_{3}}=\cdot\cdot\cdot=\frac{s_{n-1}}{c_{n-1}-c_{n}}=\frac{s_{n}}{c_{n}-c_{n+1}}}\end{array}$ 这里 $c_{n+1}=0$  

利用 $c_{k}=s_{k}-s_{k-1}$ ， $k=1,2,\cdot\cdot\cdot\;,n$ ，这里 $s_{0}=0$ ．上面的等式可化为  

$$
{\frac{s_{2}}{s_{1}}}={\frac{s_{1}+s_{3}}{s_{2}}}=\cdot\cdot\cdot={\frac{s_{n-2}+s_{n}}{s_{n-1}}}={\frac{s_{n-1}+s_{n+1}}{s_{n}}}.
$$  

这里补充定义 $s_{n+1}=c_{1}+\cdot\cdot\cdot+c_{n}+c_{n+1}$  

注意到这个式子本质与题3的求解系数的等式是一致的，只不过有 $s_{n+1}=s_{n}$ ，考虑(1)中的 $\begin{array}{r}{\lambda_{n}=\frac{\sin(n+1)\alpha}{\sin n\alpha}=1}\end{array}$ 知 (7)就是 (1)在 $2n+1$ 下的情形故可取 $s_{k}=\sin{k\alpha}$ ，这里 $\textstyle\alpha={\frac{\pi}{2n+1}}$  $c_{k}=\sin k\alpha-\sin(k-1)\alpha$  

$$
{\begin{array}{r l}&{s_{k}+s_{k+1}+\cdot\cdot\cdot+s_{n}=\,\sin k\alpha+\sin(k+1)\alpha+\cdot\cdot\cdot+\sin n\alpha}\\ &{\qquad\qquad\qquad\qquad\qquad\qquad={\frac{\cos(k-{\frac{1}{2}})\alpha-\cos(n+{\frac{1}{2}})\alpha}{2\sin{\frac{\alpha}{2}}}}}\\ &{\qquad\qquad\qquad\qquad\qquad={\frac{\cos(k-{\frac{1}{2}})\alpha}{2\sin{\frac{\alpha}{2}}}}.}\end{array}}
$$  

从而  

$$
t={\frac{s_{k}+s_{k+1}+\cdot\cdot\cdot+s_{n}}{c_{k}}}={\frac{\cos(k-{\frac{1}{2}})\alpha}{2\sin{\frac{\alpha}{2}}(\sin k\alpha-\sin(k-1)\alpha)}}={\frac{1}{4\sin^{2}{\frac{\alpha}{2}}}}.
$$  

利用 (4)取等条件可知，等号成立时，应有  

$$
{\frac{x_{1}}{c_{1}}}={\frac{x_{2}}{c_{2}}}=\cdot\cdot\cdot={\frac{x_{n}}{c_{n}}},
$$  

即  

$$
{\frac{x_{1}}{\sin\alpha}}={\frac{x_{2}}{\sin2\alpha-\sin\alpha}}=\cdot\cdot={\frac{x_{n}}{\sin n\alpha-\sin(n-1)\alpha}}.
$$  

$\begin{array}{r}{t\geq\frac{1}{4\sin^{2}\frac{\pi}{2\left(2n+1\right)}}}\end{array}$ 故最佳常数为 $\begin{array}{r}{t={\frac{1}{4\sin^{2}{\frac{\pi}{2\left(2n+1\right)}}}}}\end{array}$ 口  

与题3，题4 的紧密联系相同，题5的不等式也有一个反向不等式  

题6．对任意实数 $x_{1},x_{2},\cdot\cdot\cdot\mathbf{\Omega},x_{n}$  

$$
x_{1}^{2}+(x_{1}+x_{2})^{2}+\cdot\cdot\cdot+(x_{1}+x_{2}+\cdot\cdot\cdot+x_{n})^{2}\geq t(x_{1}^{2}+x_{2}^{2}+\cdot\cdot\cdot+x_{n}^{2})
$$  

恒成立，求 $t$ 的最大值  

解待定 $c_{1},c_{2},\cdot\cdot\cdot\ ,c_{n-1}$ 为正实数，作换元 $y_{k}=x_{1}+x_{2}+\cdot\cdot\cdot+x_{k}$ ，由均值不等式，  

$$
\begin{array}{c}{{\displaystyle c_{1}y_{1}^{2}+\frac{1}{c_{1}}y_{2}^{2}\geq\,-\,2y_{1}y_{2},}}\\ {{\displaystyle c_{2}y_{2}^{2}+\frac{1}{c_{2}}y_{3}^{2}\geq\,-\,2y_{2}y_{3},}}\\ {{\vdots}}\\ {{\displaystyle c_{n-1}y_{n-1}^{2}+\frac{1}{c_{n-1}}y_{n}^{2}\geq\,-\,2y_{n-1}y_{n}.}}\end{array}
$$  

相加得  

$c_{1}y_{1}^{2}+(\frac{1}{c_{1}}+c_{2})y_{2}^{2}+\cdot\cdot\cdot+(\frac{1}{c_{n-2}}+c_{n-1})y_{n-1}^{2}+\frac{1}{c_{n-1}}y_{n}^{2}+2\sum_{i=1}^{n-1}y_{i}y_{i+1}\geq0.$  

而题中的不等式等价于  

$$
y_{1}^{2}+y_{2}^{2}+\cdot\cdot\cdot+y_{n}^{2}\geq t(y_{1}^{2}+(y_{2}-y_{1})^{2}+(y_{n}-y_{n-1})^{2}),
$$  

即  

$2(y_{1}y_{2}+y_{2}y_{3}+\cdot\cdot\cdot+y_{n-1}y_{n})\geq\frac{2t-1}{t}(y_{1}^{2}+y_{2}^{2}+\cdot\cdot\cdot+y_{n-1}^{2})+\frac{t-1}{t}y_{n}^{2}.$  (9) 对比 (8)，(9)，可知应令 $c_{1},\cdot\cdot\cdot\ ,c_{n-1}$ 满足  

$$
c_{1}={\frac{1}{c_{1}}}+c_{2}=\cdot\cdot\cdot={\frac{1}{c_{n-2}}}+c_{n-1}={\frac{1}{c_{n-1}}}-1={\frac{1-2t}{t}}.
$$  

这个等式的形式与题3的求解系数的等式类似．利用相同的方法．可以得到 $\begin{array}{r}{c_{k}=\frac{\sin(k+1)\alpha}{\sin k\alpha}}\end{array}$ 其中 $\textstyle\alpha={\frac{2\pi}{2n+1}}$ .此时 $\begin{array}{r}{\frac{1-2t}{t}=2\cos\alpha}\end{array}$ 则  

$$
t={\frac{1}{2(\cos\alpha+1)}}={\frac{1}{4\cos^{2}{\frac{\alpha}{2}}}}={\frac{1}{4\cos^{2}{\frac{\pi}{2n+1}}}},
$$  

等号成立时，由均值不等式成立条件，知  

$$
\frac{y_{k}}{y_{k+1}}=-\frac{1}{c_{k}}=-\frac{\sin k\alpha}{\sin(k+1)\alpha},\;\;k=1,2,\cdot\cdot\cdot,n-1.
$$  

即 $y_{k}=(-1)^{k}\cdot c\cdot\sin k\alpha$ ，这里 $c$ 为不等于0的常数．从而  

$$
x_{k}=y_{k}-y_{k-1}=(-1)^{k}\cdot c\cdot(\sin{k\alpha}+\sin(k-1)\alpha),
$$  

即  

$$
x_{k}=(-1)^{k}\cdot c\cdot(\sin\frac{2k\pi}{2n+1}+\sin\frac{2(k-1)\pi}{n+1}),\;\;k=1,2,\cdot\cdot\cdot,n.
$$  

将这一组数代入不等式，可得 $\textstyle t\leq{\frac{1}{4\cos^{2}{\frac{\pi}{2n+1}}}}$ 故最佳常数为 $\textstyle t={\frac{1}{4\cos^{2}{\frac{\pi}{2n+1}}}}$  

由题5和题6，我们得到一个有趣的结果  

对不全为〇的实数 $x_{1},x_{2},\cdot\cdot\cdot,x_{n}$ 有  

$$
{\frac{1}{4\cos^{2}{\frac{\pi}{2n+1}}}}\leq{\frac{x_{1}^{2}+(x_{1}+x_{2})^{2}+\cdot\cdot\cdot+(x_{1}+x_{2}+\cdot\cdot\cdot+x_{n})^{2}}{x_{1}^{2}+x_{2}^{2}+\cdot\cdot\cdot+x_{n}^{2}}}\leq{\frac{1}{4\sin^{2}{\frac{\pi}{2(2n+1)}}}}.
$$  

我们发现这个结果在证明中配凑系数的过程和最终得到的上下界均与题3.题4类似．赵斌老师指出，这个不等式也可以直接利用 $(*)$ 证明  

以 $\big({**}\big)$ 右边的不等式为例  

$(*)$  式不等式左边  $\Leftrightarrow a_{1}^{2}+a_{2}^{2}+\cdot\cdot\cdot+a_{n}^{2}$  

$$
\leq{\frac{1}{2-2\cos{\frac{\pi}{n+1}}}}\left(a_{1}^{2}+(a_{1}-a_{2})^{2}+\cdot\cdot\cdot+(a_{n-1}-a_{n})^{2}+a_{n}^{2}\right).
$$  

令 $n=2k$ ，并令 $a_{n+k}=a_{n+1-k}$ ， $k=1,2,\cdot\cdot\cdot\;,n$ ，即得  

$$
2(a_{1}^{2}+a_{2}^{2}+\cdot\cdot\cdot+a_{k}^{2})\leq\frac2{2-2\cos\frac\pi{2k+1}}\left(a_{1}^{2}+(a_{1}-a_{2})^{2}+\cdot\cdot\cdot+(a_{k-1}-a_{k})^{2}\right).
$$  

再令 $a_{i}=x_{1}+\cdot\cdot\cdot+x_{i},\,i=1,2,\cdot\cdot\cdot,k,$ 得  

$$
x_{1}^{2}+(x_{1}+x_{2})^{2}+\cdot\cdot\cdot+(x_{1}+\cdot\cdot\cdot+x_{k})^{2}\leq\frac{1}{4\sin^{2}\frac{\pi}{2(2k+1)}}\left(x_{1}^{2}+x_{2}^{2}+\cdot\cdot\cdot+x_{k}^{2}\right),
$$  

这就是 $\big({**}\big)$ 的右边  

这个证明的想法是将前 $i$ 项和的形式转化为相邻两项之间的关系利用差分代换，令 $y_{i}=x_{1}+\cdot\cdot\cdot+x_{i}$  $i=1,2,\cdot\cdot\cdot,k$ ：则不等式转化为  

$$
y_{1}^{2}+y_{2}^{2}+\cdot\cdot\cdot+y_{k}^{2}\leq\frac{1}{4\sin^{2}\frac{\pi}{2(2k+1)}}\left(y_{1}^{2}+(y_{1}-y_{2})^{2}+\cdot\cdot\cdot+(y_{k-1}-y_{k})^{2}\right).
$$  

这个不等式的右边缺少了项 $y_{k}^{2}$ ，我们考虑 $(*)$ 在 $n\:=\:2k$ 时的情形，若将 $y_{1},\cdot\cdot\cdot\mathbf{\cdot},y_{k}$  拓展为  $y_{1},\cdot\cdot\cdot,y_{k},\,y_{k},\cdot\cdot\cdot,y_{1}$  ，则中间项  $(y_{k}-y_{k})^{2}=0$  便消失了．这就 产生了上述的证明  

对 $\big({**}\big)$ 不等式作一些转化，可以得到一个与题2形式相似的不等式题7．已知 $n$ 为正整数， $x_{1},x_{2},\cdot\cdot\cdot,x_{n}$ 为正实数，证明：  

$$
\begin{array}{l}{\displaystyle\operatorname*{min}\left\{x_{1},\frac{1}{x_{1}}+x_{2},\cdots,\frac{1}{x_{n-1}}+x_{n},\frac{1}{x_{n}}+1\right\}\leq2\cos\frac{\pi}{2n+3}}\\ {\leq\displaystyle\operatorname*{max}\left\{x_{1},\frac{1}{x_{1}}+x_{2},\cdots,\frac{1}{x_{n-1}}+x_{n},\frac{1}{x_{n}}+1\right\}.}\end{array}
$$  

事实上,在题2 中令 $n=2k+1$ ，并令 $\textstyle x_{k+1+i}={\frac{1}{x_{k+1-i}}}$  $i=1,2,\cdot\cdot\cdot,k,$  $x_{k+1}=1$ (这是可行的，因为等号成立时恰有 $\begin{array}{r}{x_{k+1}=\frac{\sin(k+2)\cdot\frac{\pi}{2k+3}}{\sin(k+1)\cdot\frac{\pi}{2k+3}}=1)}\end{array}$ 便得到了题7.  