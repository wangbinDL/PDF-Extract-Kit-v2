# Computing Transition Pathways for the Study of Rare Events Using Deep Reinforcement Learning  

# Bo Lin   1   Yangzheng Zhong   1   Weiqing Ren  

# Abstract  

Understanding the transition events between metastable states in complex systems is an im- portant subject in the fields of computational physics, chemistry and biology. The transition pathway plays an important role in characteriz- ing the mechanism underlying the transition, for example, in the study of conformational changes of bio-molecules. In fact, computing the transi- tion pathway is a challenging task for complex and high-dimensional systems. In this work, we formulate the path-finding task as a cost mini- mization problem over a particular path space. The cost function is adapted from the Freidlin- Wentzell action functional so that it is able to deal with rough potential landscapes. The path-finding problem is then solved using a actor-critic method based on the deep deterministic policy gradient algorithm (DDPG). The method incorporates the potential force of the system in the policy for generating episodes and combines physical prop- erties of the system with the learning process for molecular systems. The exploitation and explo- ration nature of reinforcement learning enables the method to efficiently sample the transition events and compute the globally optimal transi- tion pathway. We illustrate the effectiveness of the proposed method using three benchmark sys- tems including an extended Mueller system and the Lennard-Jones system of seven particles.  

# 1. Introduction  

Understanding the transition events of dynamical systems is a fundamental but challenging task in many science prob- lems, including chemical reaction, conformational changes of bio-molecules and nucleation events during phase tran- sitions. For the system, the transition occurs by crossing a typical energy barrier separating two metastable states in the presence of random perturbations. The general disparity between the effective thermal energy and the energy barrier usually leads to a long-waiting period for the system around metastable states before a sudden transition from one state to another emerges. In this setting, we call the transition as a rare event. The major interest for the study of rare events is to compute the mechanism underlying the transi- tion events, such as the transition pathway and transition rate. In the past, a number of research works have been devoted to developing efficient approaches for investigating the transition mechanism. Well-known methods include the transition path sampling ( Bolhuis et al. ,  2002 ;  Dellago et al. ,  2002 ), the string method ( E et al. ,  2002 ;  2005 ;  Ren et al. ,  2005 ;  Maragliano et al. ,  2006 ;  E et al. ,  2007 ), the action-based method ( Olender & Elber ,  1996 ) and the accel- erated molecular dynamics ( Voter ,  1997 ). Also, the recent works in Ref. ( Khoo et al. ,  2019 ;  Li et al. ,  2019 ;  Rotskoff et al. ,  2022 ) proposed deep learning based methods for com- puting the committor function, which is a central object in the transition path theory for understanding the transition mechanism ( Ren et al. ,  2005 ;  E & Vanden-Eijnden ,  2010 ).  

The transition pathway in the zero-temperature limit is char- acterized by the minimum energy path (MEP). The MEP is a path defined in the configuration space along which the tangent of the path is parallel to the potential force. Classical methods for identifying the MEP include the nudged elastic band method ( J onsson et al. ,  1998 ), the string method ( E et al. ,  2002 ;  2005 ;  Ren et al. ,  2005 ;  Maragliano et al. , 2006 ;  E et al. ,  2007 ) and the conjugate peak refinement method ( Fischer & Karplus ,  1992 ). The Freidlin-Wentzell theory of large deviations provides a variational characteri- zation of the most likelihood path via a path-based action functional. Based on this characterization, Ref. ( E et al. , 2004 ;  Zhou et al. ,  2008 ;  Heymann & Vanden-Eijnden ,  2008 ) developed the minimum action methods for computing the minimum action path by minimizing the functional over a path space where the two ends of path are constrained to par- ticular states. Also, the Onsager-Machlup functional, first introduced by Onsager and Machlup ( Onsager & Machlup , 1953 ), was used to compute the most probable path associ- ated with a finite-time horizon for systems at finite noise in many applications ( Wang et al. ,  2010 ;  Fujisaki et al. ,  2010 ;  

Du et al. ,  2021 ). From another perspective, one can recast the variational formulation of the transition path as a finite- horizon optimal control problem ( Fleming ,  1977 ;  Grafke & Vanden-Eijnden ,  2019 ). The control problem was recently solved by a reinforcement learning algorithm ( Guo et al. , 2024 ).  

The situation is quite different when the potential energy surface is rough, which is the general case for practical molecular systems. In this case, the ensemble of transition paths can be characterized by a tube in the configuration space connecting the metastable states inside which the tran- sition occurs with high probability ( Ren et al. ,  2005 ). The rough potential energy surface contains numerous saddle points, most of which are separated by energy barriers com- parable to or less than the thermal energy and thus do not act as bottlenecks of the transition. As a consequence, the potential force should not be straightforwardly used in the variational characterization of the transition pathway.  

In this paper, we propose a deep reinforcement learning method for computing the transition pathway of the sys- tem with rough potential landscapes. We formulate the path-finding task as a cost minimization problem over a par- ticular path space. To tackle the difficulties arising from the roughness of the potential landscape, we adapt the Freidlin- Wentzell functional and propose a cost function involving an effective force function. In the zero-temperature limit, the effective force simply reduces to the potential force of the system. The formulated path-finding problem is over a con- strained sequence of states in the configuration space, where the optimal times slices are determined using numerical quadratures.  

In recent years, the advances in reinforcement learning algo- rithms have made successful applications in many sequential decision making problems, including video games, robotic control and autonomous driving. A general class of rein- forcement learning algorithms are based on computation of the state-action value function, such as the Deep Q Network (DQN) algorithm ( Mnih et al. ,  2013 ;  2015 ), the determinis- tic policy gradient (DPG) algorithm ( Silver et al. ,  2014 ) and the deep DPG (DDPG) algorithm ( Lillicrap et al. ,  2015 ). In particular, the DQN algorithm utilizes the deep neural net- works as the function approximators, where target networks and replay buffer are introduced to stabilize the algorithm. Furthermore, the DDPG algorithm combined the DQN with the actor-critic approach based on the policy gradient to adapt the algorithm to a broader case with continuous and high-dimensional action space.  

In this work, we solve the formulated cost minimization problem for identifying the transition pathway using the actor-critic method based on the DDPG algorithm. The critic and actor functions are parameterized by neural net- works. To target the exploration in the region of interest, the method employs a stochastic policy based on the actor function with random noise and the potential force of the system for generating episodes. Also, we utilize target net- works and a replay buffer to address the possible instability issue in the learning process. For molecular systems, to enhance the learning efficiency, we incorporate physical properties of the system into the critic and actor networks. The exploitation and exploration nature of reinforcement learning together with these techniques establish a stable and efficient algorithm for sampling transition events and computing the globally optimal transition pathway for high- dimensional systems with rough potential landscapes. We demonstrate the effectiveness of the method using three nu- merical examples including a two-dimensional system, an extended Mueller system and the Lennard-Jones system of seven particles.  

The paper is organized as follows. In Section  2 , we in- troduce the background and the formulated path-finding problem and propose the reinforcement learning algorithm. The numerical examples are presented in Section  3 . In Section  4 , we draw the conclusions.  

# 2. Method  

We consider a dynamical system in the configuration space  $\mathbb{R}^{d}$  , which is modelled by the over-damped Langevin equa- tion:  

$$
d x_{t}=-\nabla V(x_{t})d t+\sqrt{2\epsilon}d W_{t},\quad t>0
$$  

where  $V(x)$   is a potential function,    $W_{t}$   is a standard Brown- ian motion and    $\epsilon$   is a parameter specifying the strength of the noise which is called the temperature of the system. The equilibrium distribution of the system is known as the Boltz- mann density function    $\begin{array}{r}{\rho(x)=Z^{-1}\exp(-\frac{1}{\epsilon}V(x))}\end{array}$  , where  $Z$   is a normalization constant. Consider the general situa- tion where there are two metastable states  $A$   and  $B$   for the system. A transition pathway between the two metastable states    $A$   and    $B$   is defined as a curve in configuration space connecting the two states.  

For a time    $T>0$  , we denote by    $\mathbb{C}_{[0,T]}$   the set of all absolute continuous functions in the configuration space over the time interval    $[0,T]$   connecting the two metastable states    $A$  and  $B$  . The Freidlin-Wentzell action functional for a given path    $\varphi\in\mathbb{C}_{[0,T]}$   is defined as  

$$
S_{T}[\varphi]=\int_{0}^{T}{\frac{1}{4}}\left|\varphi^{\prime}(t)+\nabla V(\varphi(t))\right|^{2}d t.
$$  

According to the Freidlin-Wentzell theory of large devi- ations ( Freidlin & Wentzell ,  2012 ), when the noise    $\epsilon$   is sufficiently small, for small number  $\delta>0$  , the probability that the system  ( 1 )  stays in the neighborhood of a given path  $\varphi\in\mathbb{C}_{[0,T]}$   over the time interval  $[0,T]$   can be estimated by  

$$
\mathbb{P}\left[\operatorname*{max}_{0\leqslant t\leqslant T}\|x(t)-\varphi(t)\|<\delta\right]\approx\exp\left(-\frac{S_{T}[\varphi]}{\epsilon}\right).
$$  

Therefore, in the zero-temperature limit, the most probable transition path of the system within the time horizon  $[0,T]$  can be characterized by a minimizer of the functional ( 2 ):  

$$
\varphi_{T}^{*}=\underset{\varphi\in\mathbb{C}_{[0,T]}}{\arg\operatorname*{min}}\,S_{T}[\varphi].
$$  

The path    $\varphi_{T}^{*}$    is also referred to as the minimum action path. In the infinite-time limit by letting  $T$   goes to infinity, the action functional of the minimum action path,  $S_{T}[\varphi_{T}^{*}]$  , converges to the infimum value  

$$
\operatorname*{inf}_{T>0}\operatorname*{inf}_{\varphi\in\mathbb{C}_{[0,T]}}S_{T}[\varphi],
$$  

where the infimum is over all times  $T$   and the corresponding path space  $\mathbb{C}_{[0,T]}$  . Furthermore, the graph limit of the mini- mum action path is a minimum energy path (MEP) of the system. The MEP is, by definition, a curve in the configura- tion space along which the tangent of the curve is parallel to the potential force  $-\nabla V(x)$  .  

In this work, we aim to find the transition pathway with minimal action in a path space that is close to    $\cup_{T}\mathbb{C}_{[0,T]}$  To deal with rough potential landscapes, we propose a cost function by adapting the Freidlin-Wentzell functional. Then we propose a deep reinforcement learning algorithm to solve the path-finding problem.  

# 2.1. Formulation of the Problem  

For a small number  $\gamma\,>\,0$  , we consider a path space    $\mathbb{C}_{\gamma}$  consisting of continuous piecewise linear functions, whose graph is a polygonal chain connecting the two states    $A$   and  $B$  . Each path    $\varphi(t)$   in the space    $\mathbb{C}_{\gamma}$   is represented by a sequence of states    $\left(z_{0},.\,.\,.\,,z_{N}\right)$   in the configuration space, together with the corresponding time points    $\left(t_{0},\ldots,t_{N}\right)$  (See Fig.  1 ). The sequence    $\left(z_{0},.\,.\,.\,,z_{N}\right)$   forms a polygonal chain connecting    $A$   and  $B$   where the line segments are of equal length  $\gamma$   except the last one,  i.e.  

$$
\begin{array}{r l}&{z_{0}=A;\quad z_{N}=B;}\\ &{\gamma=\left|z_{i}-z_{i+1}\right|,\;0\leqslant i\leqslant N-2;}\\ &{\gamma\geqslant\left|z_{N-1}-z_{N}\right|.}\end{array}
$$  

Over the time interval  $[t_{i},t_{i+1}]$  , the path    $\varphi(t)$   is a straight line connecting    $z_{i}$   and  $z_{i+1}$   with uniform derivatives,  

$$
\varphi(t)=z_{i}+\frac{z_{i+1}-z_{i}}{h_{i}}(t-t_{i}),\quad t_{i}\leqslant t\leqslant t_{i+1}
$$  

whe  $h_{i}=t_{i+1}-t_{i}$  We denote the func- tion  $\varphi^{i}(t)=\varphi(t+t_{i})$   for  $t\in[0,h_{i}]$   ∈ . One can show that  

![](images/83078955ebc9b132bc53a3a2588d292bbd069c4f3312a8a0a0fb3c94ae42aac5.jpg)  

Figure 1.  Schematic illustration of an absolute continuous path (black solid line) connecting the two metastable states    $A$   and  $B$  , which is approximated by a path    $\varphi(t)$   (green dashed line) in  $\mathbb{C}_{\gamma}$   represented by a polygonal chain with a sequence of states  $\left(z_{0},.\,.\,.\,,z_{N}\right)$  .  

the set  $\cup_{\gamma>0}\mathbb{C}_{\gamma}$   is a dense subset of    $\cup_{T>0}\mathbb{C}_{[0,T]}$   (See Ap- pendix  A ). Next, we consider the following action minimiza- tion problem restricted to the path space    $\mathbb{C}_{\gamma}$   for computing the transition pathway of the system,  

$$
\begin{array}{r l}&{\displaystyle\operatorname*{inf}_{\varphi\in\mathbb{C}_{\gamma}}\sum_{i=0}^{N-1}\tilde{L}(z_{i},z_{i+1};h_{i}),\quad\mathrm{where}}\\ &{\tilde{L}(z_{i},z_{i+1};h_{i})=\displaystyle\int_{0}^{h_{i}}\left\vert\frac{z_{i+1}-z_{i}}{h_{i}}+\nabla V(\varphi^{i}(t))\right\vert^{2}d t.}\end{array}
$$  

The optimization problem is, in principle, over a finite set of states    $\left(z_{0},.\cdot\cdot,z_{N}\right)$   in the configuration space sub- ject to the constraints  ( 5 ) , together with the time slices  $\left(h_{0},.\,.\,.\,,h_{N-1}\right)$  .  

Optimal Time Slices.  In the problem  ( 6 ) , for a particular sequence of states    $\left(z_{0},.\,.\,.\,,z_{N}\right)$  , each optimal time slice  $h_{i}^{*}$    is a minimizer to the individual integral  $\Tilde{L}(z_{i},z_{i+1};h_{i})$  However, it is not straightforward to obtain an analytical so- lution for  $h_{i}^{*}$    in general as the integral involves the potential force. Instead, one can compute an optimal solution    $h_{i}^{*}$    by approximating the integral    $\Tilde{L}(z_{i},z_{i+1};\Tilde{h}_{i})$   using a mid-point numerical quadrature,  

$$
\begin{array}{r l r}{\lefteqn{\operatorname*{min}_{h_{i}}\tilde{L}(z_{i},z_{i+1};h_{i})\approx\operatorname*{min}_{h_{i}}h_{i}\left|\frac{z_{i+1}-z_{i}}{h_{i}}+\nabla V(z_{i+1/2})\right|^{2}}}\\ &{}&{=2|z_{i+1}-z_{i}|\cdot|\nabla V(z_{i+1/2})|\quad}\\ &{}&{\quad+\,2\langle z_{i+1}-z_{i},\nabla V(z_{i+1/2})\rangle.\quad\quad\quad}&{(7)}\end{array}
$$  

where the mid-point    $z_{i+1/2}~=~(z_{i}\,+\,z_{i+1})/2$   and the minimum value for    $\tilde{L}$   is achieved at    $h_{i}^{*}\;\;=\;\;|z_{i+1}\;-$  |  −  $z_{i}|\left/|\nabla V(z_{i+1/2})|\right.$   | . We denote the minimum value in Eq. 7 )  by    $R(z_{i},z_{i+1})$   and refer to it as the cost between  $z_{i}$   and    $z_{i+1}$  . In principle, the integral    $\Tilde{L}(z_{i},z_{i+1};h_{i})$   in Eq.  ( 6 )  can be approximated using any suitable numerical quadratures (See Appendix  B ).  

Therefore, the task of finding the optimal transition path in the space    $\mathbb{C}_{\gamma}$   as in Eq.  ( 6 )  can be formulated as a cost minimization problem over the states    $\left(z_{0},.\,.\,.\,,z_{N}\right)$  :  

$$
\operatorname*{arg\,min}_{(z_{0},\dots,z_{N})}\sum_{i=0}^{N-1}R(z_{i},z_{i+1}),
$$  

where the states    $\left(z_{0},.\,.\,.\,,z_{N}\right)$   representing a transition path  $\varphi(t)$   are subject to the constraints in Eq. ( 5 ).  

Effective Force.  The situation is quite different when the potential energy surface is rough, which is the typical case for practical molecular systems. In this case, the rough po- tential energy surface may contain numerous saddle points, most of which do not act as bottleneck of the transition as potential barriers separating those saddle points are less than or comparable to the thermal energy ( Ren et al. ,  2005 ). As a consequence, the Freidlin-Wentzell path functional as in Eq.  ( 2 )  directly involving the potential force is no longer valid for quantifying the transition events.  

For a particular line segment connecting  $z_{i}$   and  $z_{i+1}$   in the path, consider the original dynamics  ( 1 )  starting from the mid-point    $z_{i+1/2}$  :  

$$
d x_{t}=-\nabla V(x_{t})d t+\sqrt{2\epsilon}d W_{t},\quad x_{0}=z_{i+1/2}.
$$  

For    $h>0$  , integrating both sides of the equation over the time interval    $[0,h]$   gives  

$$
x_{h}=z_{i+1/2}-\int_{0}^{h}\nabla V(x_{t})d t+\xi,\quad\xi\sim\mathcal{N}(0,2\epsilon h).
$$  

We treat the potential force in the integral as a uniform value around the state    $z_{i+1/2}$   and refer to it as the effective force at    $z_{i+1/2}$  . The formal definition of the effective force at  $z_{i+1/2}$   is given by  

$$
F_{\epsilon}(z_{i+1/2})=\mathbb{E}_{\epsilon}\left[\frac{x_{h}-x_{0}}{h}:x_{0}=z_{i+1/2}\right],
$$  

where the expectation is over a state ensemble of the system at time    $h$   starting from the state  $z_{i+1/2}$   at the temperature    $\epsilon$  . In practice, we approximate the effective force  $F_{\epsilon}\big(z_{i+1/2}\big)$  using  $M$   short trajectories following the dynamics  ( 9 )  over the time interval    $[0,h]$   where the state at time  $h$   for each trajectory is denoted by  $x_{j}^{e}$  ,  

$$
F_{\epsilon}(z_{i+1/2})\approx\frac{1}{M}\sum_{j=1}^{M}\frac{x_{j}^{e}-z_{i+1/2}}{h}.
$$  

We then define the cost function  

$$
\begin{array}{l}{{R_{\epsilon}(z_{i},z_{i+1})=\displaystyle\operatorname*{min}_{h_{i}}h_{i}\left|\frac{z_{i+1}-z_{i}}{h_{i}}-F_{\epsilon}(z_{i+1/2})\right|^{2}}}\\ {{{}~~~~~~~~~~~~~~~~~=2|z_{i+1}-z_{i}|\cdot\left|F_{\epsilon}(z_{i+1/2})\right|}}\\ {{{}~~~~~~~~~~~~~~~~~-2(z_{i+1}-z_{i})\cdot F_{\epsilon}(z_{i+1/2}).}}\end{array}
$$  

Note that the cost function reduces to the Freidlin-Wentzell cost in Eq.  ( 7 )  when  $\epsilon$   and  $h$   tends to zero since the expec- tation  ( 10 )  asymptotically converges to the potential force  $-\nabla V(z_{i+1/2})$  . For simpli ty, we denote by    $R_{0}$   the zero- temperature cost function  R  as defined in Eq.  ( 7 ) . For the system with rough potential landscapes at temperature  $\epsilon$  , the transition pathway connecting    $A$   and    $B$   can be computed by solving the cost minimization problem  

$$
\mathop{\mathrm{arg\,min}}_{(z_{0},\dots,z_{N})}\sum_{i=0}^{N-1}R_{\epsilon}(z_{i},z_{i+1}),
$$  

where the states    $\left(z_{0},.\,.\,.\,,z_{N}\right)$   in the configuration space are subject to the constraints in Eq. ( 5 ).  

# 2.2. Reinforcement Learning Method  

To solve the path-finding problem in Eq.  ( 13 ) , we define a Markov decision process   $\mathcal{X}\,=\,\mathbb{R}^{d}$  and continuous action space  A  $\mathcal{A}\,=\,\{x\,\in\,\mathbb{R}^{d}\,:\,|x|\,=\,1\}$   {  ∈  | | } During the process, an agent interacts with the environment at discrete time steps. At each step, the agent takes an action, observes the next state and receives a running cost (or reward). Specifically, we set the transition dynamics and cost function    $r(s,a)$   to be deterministic and consistent with the problem  ( 13 ) ,  i.e.  the next state after taking action    $a_{t}$   at state  $s_{t}$   is given by  $s_{t+1}=s_{t}+\gamma\cdot a_{t}$   and the rece ost is defined as    $r_{t}=R_{\epsilon}(s_{t},s_{t+1})$   as in Eq.  ( 7 )  for  ϵ  $\epsilon=0$   or Eq.  ( 12 )  for  $\epsilon>0$  . The terminal condition is that the agent arrives in the region  $\Omega_{\gamma}=\{x\in\mathbb{R}^{d}:|x-B|<\gamma\}$  .  

The agent’s behaviour is described by a policy    $\pi$  , which gives the action  $\pi(s)$   for each state    $s$  . For a given policy    $\pi$  , the return from a state  $s_{t}$   is defined as the sum of future costs,  $R_{t}=r_{t}\!+\!\cdot\cdot\!+r_{T}$  , where  $T$   denotes th erminal time of the process. Our goal is to learn a policy  $\pi^{*}$  which minimizes the return for each state    $s\in\mathcal X$  . The state tion function  $Q(s,a)$   associated with the optimal policy  $\pi^{*}$  is defined as the return after taking action    $a$   at  $s$   and thereafter following the policy  $\pi^{*}$  . Many reinforcement learning algorithms for computing the function    $Q(s,a)$   are based on a recursive relationship known as the Bellman equation:  

$$
Q(s_{t},a_{t})=r(s_{t},a_{t})+\operatorname*{min}_{b\in\mathcal{A}}Q(s_{t+1},b).
$$  

To deal with the task with continuous action space, here we use an actor-critic approach based on the DDPG algo- rithm ( Lillicrap et al. ,  2015 ). The critic function is the state-action function  $Q(s,a)$   which is parameterized using a neural network  $\tilde{Q}_{\theta}(s,a):\mathcal{X}\times\mathcal{A}\to[0,1]$  ,  

$$
Q_{\theta}(s,a)=\left\{\lambda\tilde{Q}_{\theta}(s,a),\quad s\notin\Omega_{\gamma}\right.
$$  

where    $\lambda>0$   is predefined parameter which specifies the range of the critic function as    $[0,\lambda]$  . The actor function  $\begin{array}{r}{\mu(s)=\arg\operatorname*{min}_{a}Q(s,a)}\end{array}$   corresponding to the optimal pol- icy specifies the optimal action at each state. To construct an actor network mapping states to unit vectors in  $\mathbb{R}^{d}$  , we represent the actor function as a normalized vector based the cosines of a hidden actor    $\tilde{\mu}_{\theta}:\mathbb{R}^{d}\rightarrow\mathbb{R}^{d}$    ,  

$$
\begin{array}{r}{\mu_{\theta}(s)=\Theta[\cos(\tilde{\mu}_{\theta}(s))],}\end{array}
$$  

where    $\Theta[v]=v/|v|$   is the normalization function with an input vector  $v\in\mathbb R^{d}$   ∈ .  hat the actor  ction is periodic over the hidden actor  ${\tilde{\mu}}_{\theta}(s)$   with period  $2\pi$  .  

Data Generation.  We sample data by generating episodes where the initial states are produced from a particular dis- tribution    $p(s)$   and subsequently the action of the agent is selected based on a stochastic policy. To facilitate the explo- ration of possible transition pathways, we add noise to the hidden actor function  ${\tilde{\mu}}_{\theta}$   in the selection of action. Mean- while, we aim to target the exploration in the region of interest which excludes states in the configuration space with low equilibrium densities    $\rho(x)$  . Thus, we take the action conducted at step    $t$   as    $a_{t}=\Theta[\tilde{a}_{t}]$  , where  

$$
\tilde{a}_{t}=\left\{\begin{array}{l l}{\cos(\tilde{\mu}_{\theta}(s_{t})),}&{\mathrm{with~probability~}p_{1}}\\ {-\nabla V(s_{t}),}&{\mathrm{with~probability~}p_{2}}\\ {\cos(\tilde{\mu}_{\theta}(s_{t})+\xi_{t}),}&{\mathrm{with~probability~}1-p_{1}-p_{2}}\end{array}\right.
$$  

$\xi_{t}\in\mathbb{R}^{d}$   Gaussian distribution and  $p_{1}\geqslant0,p_{2}\geqslant0,1-p_{1}-p_{2}\geqslant0$   − .  

We use a replay buffer    $\mathcal{R}$   with fixed size    $N_{R}$   to store the sampled transitions, where the oldest ones will be discarded when new samples are appended to the buffer. The critic function    $Q(s,a)$   can be learned off-policy, allowing us to maintain a large-size replay buffer and sample a mini-batch from the buffer for training neural networks at each step.  

Policy Evaluation.  Target neural networks are often em- ployed in reinforcement learning algorithms to address the instability issue when nonlinear and large scale neural net- works are used. Here we duplicate the critic and actor net- works as the target networks    $Q_{\theta}^{\prime}(s,a)$  ,    $\mu_{\theta}^{\prime}(s)$   each time after a particular number of steps. The target networks will be used to compute the target values in the temporal-difference (TD) loss function for training the critic network,  

$$
\begin{array}{l}{\displaystyle L_{\boldsymbol Q}(\boldsymbol\theta)=\frac{1}{\left|\mathcal B\right|}\sum_{\left(s_{t},a_{t},r_{t},s_{t+1}\right)\in\mathcal B}\left|Q_{\boldsymbol\theta}(s_{t},a_{t})-y_{t}\right|^{2},}\\ {\displaystyle y_{t}=r_{t}+Q_{\boldsymbol\theta}^{\prime}\big(s_{t+1},\mu_{\boldsymbol\theta}^{\prime}\big(s_{t+1}\big)\big).}\end{array}
$$  

Here we use the stochastic gradient descent to train the neural networks, and    $\mathcal{B}=\{\left(s_{t},a_{t},r_{t},s_{t+1}\right)\}$   is a batch of transitions sampled from the replay buffer.  

Policy Gradient.  The actor network is trained using the gradient of an average return    $J_{\mu}$   over the batch states with Algorithm 1  Reinforcement learning for computing the optimal transition pathway at temperature  $\epsilon$  .  

Initialize critic and actor networks  $Q_{\theta}(s,a)$   and  $\mu_{\theta}(s)$  . Initialize target networks:  $Q_{\theta}^{\prime}\leftarrow Q_{\theta}$  ,    $\mu_{\theta}^{\prime}\leftarrow\mu_{\theta}$  , and initial-  

ize replay buffer  $\mathcal{R}$  . for  $s t e p=1$   to  maxstep  do Sample initial state  $s_{0}$   from distribution  $p(s)$  . for  $t=0$   to  maxtime  do Select action  $a_{t}$   according to policy ( 16 ); Update n  state    $s_{t+1}=s_{t}+\gamma\cdot a_{t}$  ; Sample  M  trajectories starting from    $s_{t+1/2}~=$   $\textstyle{\frac{1}{2}}{\big(}s_{t}+s_{t+1}{\big)}$   with time  $h$   and estimate    $F_{\epsilon}\big(s_{t+1/2}\big)$  as in Eq. ( 11 ); Compute cost  $r_{t}=R_{\epsilon}(s_{t},s_{t+1})$  ; Store    $\left({{s_{t}},{a_{t}},{r_{t}},{s_{t+1}}}\right)$   in  $\mathcal{R}$  ; Sample a batch  $\mathcal{B}=\{(s_{t}^{i},a_{t}^{i},r_{t}^{i},s_{t+1}^{i})\}$   from    $\mathcal{R}$  ; Compute target values  $y_{t}^{i}=r_{t}^{i}+Q_{\theta}^{\prime}(s_{t+1}^{i},\mu_{\theta}^{\prime}(s_{t+1}^{i}));$  Update critic  $Q_{\theta}$   using the loss function ( 17 ); Update actor  $\mu_{\theta}$   using the sampled policy gradients in Eq. ( 18 ); Exit if terminal condition  $s_{t+1}\in\Omega_{\gamma}$   is met. end  

if  mod   $(s t e p,s t e p_{0})=0$   then Update target networks  $Q_{\theta}^{\prime}\leftarrow Q_{\theta},\mu_{\theta}^{\prime}\leftarrow\mu_{\theta}$  ← ←  

# end  

end Output : The critic and actor functions    $Q_{\theta}(s,a),\mu_{\theta}(s)$  .  

respect to the actor parameters by applying the chain rule,  

$$
\nabla_{\theta}J_{\mu}=\frac{1}{|\mathcal{B}|}\sum_{s_{t}\in\mathcal{B}}\nabla_{a}Q_{\theta}(s_{t},a)|_{a=\mu_{\theta}(s_{t})}\cdot\nabla\mu_{\theta}(s_{t}).
$$  

Physics-based Learning.  General molecular systems are usually invariant to certain transformations of the system, such as translation, rotation of the configuration and re- indexing of particles of the same species in the system. The physical properties can be described by a transformation function    $x^{\prime}=\mathcal{T}(x)$   mapping a given configuration  $x$   and its equivalent ones to a representative configuration  $x^{\prime}$  . We make the learning process respect the physical properties. In the critic and actor networks, the state-action input    $(s,a)$  is transformed into    $(s^{\prime},a^{\prime})$   by    $\mathcal{T}$  before fed in net For the actor network, we restore the output  $\tilde{a}\in\mathcal{A}$   ∈A  to  $\tilde{a}^{\prime}\in$    ∈  $\mathcal{A}$   by the inverse of    $\mathcal{T}$  , where  $\mathcal{A}$   denotes the action space. Learning over an effective manifold of the configuration space can enhance the efficiency of the algorithm.  

A pseudocode for describing the reinforcement learning al- gorithm is presented in Algorithm  1 . Once the actor network is trained, one can compute a transition pathway with states  $\{z_{t}\}_{0\leqslant t\leqslant T}$   by performing the iterative procedure:  

$$
z_{t+1}=z_{t}+\gamma\cdot\mu_{\theta}\big(z_{t}\big),\;t\geq0;\quad z_{0}=A
$$  

unt minal condition  $z_{T-1}\in\Omega_{\gamma}$   is satisfied and we set  $z_{T}=B$  .  

Remark 1 :  The proposed method is able to compute the globally optimal transition pathway. Traditional meth- ods for computing the transition pathway including the nudged elastic band method ( J onsson et al. ,  1998 ), the string method (  $^ Ḋ E Ḍ$   et al. ,  2002 ;  2007 ) and the minimum ac- tion method ( E et al. ,  2004 ;  Heymann & Vanden-Eijnden 2008 ) are suffering from the issue of metastability, as they are performing an iterative procedure in the path space starting from a particular path. The solution relies on the initial guess of path. In the general case with multi- ple transition pathways (for example, in conformational changes of bio-molecules), suitable initial guess is usually not straightforwardly available. In this case, these methods may get trapped in the neighborhood of a locally optimal solution and produce a path that is far away from the glob- ally optimal one. On the other hand, as in the stochastic policy  ( 16 ) , the proposed reinforcement learning algorithm is able to explore the entire configuration space due to the randomness term and focus on the transition region of in- terest based on the optimal policy introduced by the actor function. The exploration-exploitation balance makes the proposed method able to compute the globally optimal path in the whole configuration space.  

Remark 2 :  There are a number of reinforcement learning al- gorithms developed recently with substantial improvements over the DDPG algorithm, such as the twin delayed deep deterministic policy gradient algorithm (TD3) ( Fujimoto et al. ,  2018 ) and the soft actor-critic algorithm ( Haarnoja et al. ,  2018 ). In this work, we propose a framework of for- mulating the path-finding problem for dynamical systems and employing RL algorithms to solve the problem. Besides the basic DDPG algorithm, the proposed method enjoys the flexibility of combining with advanced techniques from other RL algorithms, for instance, twin  $Q$  -functions and target pol- icy smoothing in TD3, to improve the performance of the method. This might be helpful in specific implementations and will be tested in future works.  

# 3. Numerical Examples  

To illustrate the effectiveness of the proposed method, we apply Algorithm  1  to three benchmark systems including a two-dimensional system, a ten-dimensional system with an extended Mueller potential and the Lennard-Jones system of seven particles. The first system is adapted from Ref. ( E et al. ,  2007 ) which exhibits two typical transition pathways connecting the metastable states. The latter two systems have been extensively studied in previous works ( Khoo et al. ,  2019 ;  Li et al. ,  2019 ;  Dellago et al. ,  1998 ;  Evans et al. , 2023 ). To validate the accuracy of the computed transition pathway, one can compute a reference solution of the tran- sition pathway using the string method or transition tube by constructing the committor function landscape. Thus, the three examples can be used to benchmark the proposed method.  

We parameterize the critic and actor functions using fully- connected neural networks with two hidden layers and put the hyperbolic tangent function  (tanh)  as the activation unit in the network. In the critic network  ${\tilde{Q}}_{\theta}$  , as specified in Eq.  ( 14 ) , we put a sigmoid function on the output layer and set  $\lambda=1000$  . In the hidden actor    ${\tilde{\mu}}_{\theta}$   as in Eq.  ( 15 ) , there is no activation function acting on the output layer.  

In the three examples, we generate episodes in parallel with initial states sampled from a mixed distribution. Specifically,  $30\%$   of the initial states are taken as the metastable state  $A$   while the remaining are sampled from the equilibrium distribution of the system at a particular temperature    $\epsilon^{\prime}$  . The latter part of initial states are collected by simulating the Langevin equation  ( 1 )  of the system. In the exploration policy  ( 16 ) , we take    $p_{1}=1/3$  ,  $p_{2}=1/3$   and  $\xi_{t}$   is sampled from the Gaussian distribution    $\mathcal{N}(0,\pi/4)$  . The neural net- works are trained using the stochastic gradient descent with the Adam optimizer ( Kingma & Ba ,  2015 ) and batch size 5000 . With a batch of data points sampled from the replay buffer, we train the critic and actor networks repeatedly for 10  times using the temporal-difference loss function  ( 17 ) and the sampled policy gradient in Eq.  ( 18 ) , respectively. The target networks are updated every  10  training steps. The parameters in Algorithm  1  used for the three examples are shown in the table in Appendix  C .  

# 3.1. A Two-dimensional System  

To illustrate the ability of the method for predicting the globally optimal transition pathway, we first consider a two- dimensional (2D) system with two typical transition path- ways. The potential function of the system, as adapted from Ref. ( E et al. ,  2007 ), is given by  

$$
V(x,y)=\left[(1-x^{2}-y^{2})^{2}+\frac{y^{2}}{x^{2}+y^{2}}\right](1+g(y)),
$$  

where    $g(y)=1/(1+\exp(-y))$   denotes the sigmoid func- tion. For the system, there are two metastable states at  $A=(-1,0)$   and  $B\,=\,(1,0)$  , corresponding to two local minima of the potential  V  .  

The system has two minimum energy paths (MEP) connect- ing    $A$   and    $B$  . We first compute reference solutions for the two paths using the string method ( E et al. ,  2007 ). The string is represented by  501  points in the 2D plane. We perform the string method twice, in which the initial strings are taken as straight lines connecting the two points    $(-0.5,0.5)$   and (0 . 5 ,  0 . 5)  and connecting    $(-0.5,-0.5)$   and    $(0.5,-0.5)$  , re- spectively. Plots of the two computed MEPs are shown in the upper panel of Fig.  2 , which resemble upper/lower semicircles connecting    $A$   and    $B$   in the 2D plane. For con- venience, we refer to the two curves as upper/lower MEPs. Also shown in the lower panel of Fig.  2  is the potential energy  ( 19 )  of the system along the two paths, from which one can observe that the upper MEP has a energy barrier of  $\Delta V\simeq2$  , whereas lower MEP has a barrier of    $\Delta V\simeq1$  . Therefore, the lower MEP is the globally optimal transition pathway between    $A$   and    $B$  , especially when the magnitude of noise is much less than  1 ,  i.e.  $\epsilon\ll1$  .  

With the lower MEP, denoted by  $\varphi$  , one can quantitatively evaluate the path    $\varphi_{\theta}$   computed by the proposed method. Note that  $\varphi$   is parameterized by the normalized arc-length  $\alpha$  of the path. We first re-parameterize    $\varphi_{\theta}$   with its normalized arc-length and then evaluate    $\varphi_{\theta}$   using the relative error:  

$$
e_{\varphi}={\frac{\|\varphi_{\theta}(\alpha)-\varphi(\alpha)\|}{\|\varphi(\alpha)\|}},
$$  

where the norm is defined as  $\begin{array}{r l r}{\|\phi(\alpha)\|}&{{}}&{=}\end{array}$   $\begin{array}{r}{\sqrt{\frac{1}{n_{e}}\sum_{i=1}^{n_{e}}|\phi(i/n_{e})|^{2}}}\end{array}$  P  for a function    $\phi$   using    $n_{e}\,=\,100$  discrete points.  

We apply Algorithm  1  with  700  training steps to compute the transition pathway, in  20  independent runs with ran- dom initialization on the critic and actor networks. In the path-finding problem  ( 13 ) , we take the path space  $C_{\gamma}$   with  $\gamma\:=\:0.1$   and set    $\epsilon\,=\,0$  . All of the computed paths us- ing the proposed method are close to the lower MEP, as shown in the upper panel of Fig.  2 . The lower panel of the figure shows the potential function along the computed path, which agrees well with the potential along the lower MEP. The statistics of relative error for the paths defined in Eq.  ( 20 )  in the  20  runs is    $e_{\varphi}=0.0060{\pm}0.0020$  . The results demonstrate the accuracy of the methods for computing the transition pathway.  

As a comparison, we also apply the string method with random initialization to the system in  20  independent runs. On each run, the initial string is taken as a straight line randomly sampled on the 2D plane. Specif- ically, one end point    $x_{a}$   of the line is sampled from  $\mathcal{U}\left([-1.5,0\right)\times[-1.5,1.5]\right)$   and the other end point    $x_{b}$   is sampled from  $\mathcal{U}\left((0,1.5]\times\left[-1.5,1.5\right]\right)$  , where  $\mathcal{U}(\cdot)$   indi- cates the uniform distribution. In the total  20  runs, the string method is convergent to the lower MEP for  11  runs and to the upper MEP for the remaining runs. The results demon- strate that the proposed method statistically outperforms the string method for computing the globally optimal transition pathway.  

![](images/54516c0da2f9a5c0eb9e3babc8fe5fdf41c7fd1b80989c9765f34691e14221e4.jpg)  
Figure 2.  Plots of the MEPs computed using the string method and the transition pathway computed from the actor network    $\mu_{\boldsymbol{\theta}}(s)$  ( Upper ). Plots of the potential function  $V(x)$   along the three paths ( Lower ). The two MEPs are referred to as the upper/lower MEPs. The contour lines in the upper panel indicate the potential function  $V(x)$   in Eq. ( 19 ).  

# 3.2. Extended Mueller System  

To illustrate the effectiveness of the method for dealing with high-dimensional systems and rough energy landscapes, we consider the Mueller potential embedded in the ten- dimensional space,  

$$
V(x)=V_{m}(x_{1},x_{2})+\frac{1}{2\sigma^{2}}\sum_{i=3}^{10}x_{i}^{2},\quad x\in\mathbb{R}^{10}
$$  

![](images/8a85770ac799493df6e4188bf66e4c8248d6315c08266952e7a89f9ed4090ee3.jpg)  

Figure 3.  Plots of the computed transition pathway    $\varphi_{\theta}(\alpha)$   between the metastable states  $A$   and    $B$   and the minimum energy path (MEP)  $\varphi(\alpha)$   which are projected on the    $(x_{1},x_{2})$   plane. The inset plot shows the potential function along the two paths. The contour lines indicate the potential function    $V(x)$   in Eq. ( 21 ).  

where    $V_{m}(x_{1},x_{2})$   is the Mueller potential for the first two dimensions,  

$$
\begin{array}{l}{{V_{m}(x_{1},x_{2})=\displaystyle\sum_{i=1}^{4}D_{i}\exp[a_{i}(x_{1}-X_{i})^{2}}}\\ {{\mathrm{}+b_{i}(x_{1}-X_{i})(x_{2}-Y_{i})+c_{i}(x_{2}-Y_{i})^{2}]}}\\ {{\mathrm{}+\omega\sin(2k\pi x_{1})\sin(2k\pi x_{2}){,}}}\end{array}
$$  

and another  8  harmonic functions are added for the remain- ing dimensions with the parameter  $\sigma$   specifying the strength of the harmonic terms. The parameters    $\omega$   and    $k$   control the roughness of the potential landscape. We take the two metastable states as    $A\ =\ (-0.558,1.441,0,.\,.\,,0)$   and  $B\,=\,(0.623,0.028,0,.\,.\,.\,,0)$  , which corresponds to two local minimum points of the potential function    $V(x)$  .  

In this example, we take the parameters except  $\omega$  ,  $k$   from Ref. ( Li et al. ,  2019 ) and consider two cases for the potential function  ( 21 )  with different values of  $\omega$  . In the first case  $\omega=0$  ), the potential landscape is smooth and we apply the method to compute the transition pathway for the system in the zero-temperature limit. In the second case   $\langle\omega\ >$  0 ), the potential landscape is rather rugged with numerous saddle points and we compute the transition pathway at the temperature  $\epsilon=10$  .  

Smooth Mueller Potential.  In the first case, we set the parameter  $\omega=0$  . For the example, we compute the optimal transition pathway in the path space    $\mathbb{C}_{\gamma}$   with  $\gamma=0.1$   and apply Algorithm  1  to solve the problem  ( 13 )  with  $\epsilon=0$  In the algorithm, we conduct  1000  training steps; at each step, we generate episodes according to the exploration policy ( 16 ) and train the critic and actor networks.  

![](images/fb8dacac9eba42bb094602f7308f607fcaf335a321259274f8446d41512e126b.jpg)  
Figure 4.  Plots of the temporal-difference (TD) loss function    $L_{Q}$  and the average return  $J_{\mu}$   versus the training steps in Algorithm  1  

![](images/dccd562a2e6f55b1a6d46edee66a31f6b7f027933527821494c9cf6b9ea8f47a.jpg)  
Figure 5.  Plot of the relative error for the path  $\varphi_{\theta}$   computed from the actor network  $\mu_{\boldsymbol{\theta}}(s)$   versus the training steps in Algorithm  1 The error is defined in Eq. ( 20 ).  

In Fig.  3 , we plot the transition pathway  $\varphi_{\theta}$   computed from the actor network  $\mu_{\theta}(s)$  , which is projected on the    $(x_{1},x_{2})$  plane. Also shown is the minimum energy path    $\varphi$   computed using the string method ( E et al. ,  2007 ). The inset plot in Fig.  3  shows the potential function along the two paths. In Fig.  3 , one can observe that the two paths are almost indistin- guishable to each other and the method accurately predicts the potential barrier separating the two metastable states via the computed transition pathway. With    $\varphi$  , the relative error for    $\varphi_{\theta}$   as defined in Eq.  ( 20 )  under  10  independent runs is  $e_{\varphi}=0.0203\pm0.0061$  . The results demonstrate the accuracy of the proposed reinforcement learning algorithm for predicting the transition pathway of high-dimensional systems.  

In Fig.  4 , we show plots of the temporal-difference loss func- tion    $L_{Q}$   and the average return    $J_{\mu}$   over the whole replay buffer versus the training step. Also, we show the perfor- mance of the actor network,  i.e.  the relative error for    $\varphi_{\theta}$  ,  

![](images/89d55100ccf7e1b2c34b2ca819bebbc52ac788c1ccd7da64d4b76bf5a9c2dd54.jpg)  
Figure 7.  Plots of the transition pathway between the metastable states    $A$   and  $B$   computed from the actor network  $\mu_{\boldsymbol{\theta}}(\boldsymbol{s})$   and the transition tube computed by mapping a committor function land- scape of the system, for the rugged potential case at    $\epsilon=10$  . The inset plot shows the potential function along the computed path.  

versus the training steps in Fig.  5 . From the figures, one can observe that the two losses and error are all convergent to low values after about  400  training steps, which indicates the stability of the algorithm for the system. A scatter plot of the states    $\left\{s_{t}^{i}\right\}$  }  in the replay buffer, projected on the    $(x_{1},x_{2})$  plane, at the last training step of the algorithm is shown in Fig.  6 , together with two generated episodes starting from the state    $A$  . We observe that the generated data points clus- ter around the minimum energy path (MEP) as shown in Fig.  3 , with adequate sampling densities everywhere along the path, and the two episodes are guided towards the state  $B$   along the MEP with exploration randomness. The results demonstrate that the proposed method is capable of explor- ing the region regarding transition and sampling transition events efficiently.  

Rugged Mueller Potential.  In the second case, we set the parameters    $\omega\,=\,9$  ,  $k\,=\,5$   and apply Algorithm  1  to compute the optimal transition pathway at    $\epsilon\,=\,10$  . The Plots of the transition pathway computed from the actor network    $\mu_{\theta}(s)$   and the potential function along the path are shown in Fig.  7 . We validate the solution using a transi- tion tube of the system inside which the transition occurs with high probability ( Ren et al. ,  2005 ). Specifically, we compute the transition tube at    $\epsilon=10$   by mapping a com- mittor function landscape of the system (See Appendix  D ). As observed from Fig.  7 , the computed transition pathway locates near the center of the transition tube, which demon- strates the proposed method is able to predict the transition pathway for high-dimensional systems with rough potential landscapes.  

# 3.3. Lennard-Jones System  

To illustrate the ability of the algorithm to deal with molec- ular systems, we apply the method to study a rearrangement process of the Lennard-Jones system, which is a cluster of seven particles on the plane. The system is relatively simple but serves as a good example to benchmark the proposed method.  

In the system, the particles are interacting via the Lennard- Jones potential function  

$$
V(y_{1},.\,.\,,y_{7})=\sum_{i<j}4\epsilon_{0}\left[\left(\frac{\sigma_{0}}{r_{i j}}\right)^{12}-\left(\frac{\sigma_{0}}{r_{i j}}\right)^{6}\right],
$$  

![](images/5cac448319134604f8ca61a6a0175a44a6e9a5abb6f804bcfd47f96e213f2902.jpg)  
Figure 8.  Two typical stable configurations of the Lennard-Jones cluster where particle  1  (in red color) is either at the center ( Left ) or surface ( Right ) of the cluster.  

where    $\left(y_{1},.\,.\,.\,,y_{7}\right)$   denotes the position-vector of the seven particles  $r_{i j}=|y_{i}-y_{j}|$   is t lidean distance between particle  i  and particle  j  and  $\epsilon_{0},\,\sigma_{0}$   specify the energy unit and distance unit in the potential function, respectively. In this example, we take  $\epsilon_{0}=1$   and  $\sigma_{0}=1$  . In a typical equi- librium state which minimizes the potential  ( 22 ) , the cluster of seven particles forms a hexagon. For the system, we are interested in studying the rearrangement process where a particular particle is escaping from the center of the cluster to its surface ( Dellago et al. ,  1998 ;  E et al. ,  2002 ). Specifi- cally, we look at particle  1  as the migrating particle during the process. Fig.  8  displays two typical stable configura- tions of the cluster corresponding to the transition process. We next apply Algorithm  1  to the system for computing a pathway for the transition.  

As indicated by the bond-based potential function in Eq.  ( 22 ) , the system is equivalent to any rotation or transla- tion of the cluster, as well as re-indexing of the particles in the system. Based on the properties, we construct a trans- ormation function    $\tau(x)$   which maps a given configuration x  and its equivalent ones to a representative configuration. We incorporate    $\tau(x)$   into the critic and actor networks to make the learning process reflect the physical properties. The details could be found in Appendix  E .  

In the example, we solve the path-finding problem  ( 13 )  over the path space    $\mathbb{C}_{\gamma}$   with  $\gamma=0.2$   at the temperature    $\epsilon=0$  . We use the the reinforcement learning algorithm  1  to solve the problem by generating episodes using the policy  ( 16 ) and training the critic and actor networks.  

The identified transition pathway as computed from the actor network  $\mu_{\theta}(s)$   is shown in Fig.  9 . The results agree well with one transition pathway identified in Ref. ( Dellago et al. ,  1998 ), which demonstrates that our method is able to predict the transition pathway for the cluster of particles.  

# 4. Conclusions  

In this work, we proposed a deep reinforcement learning algorithm for computing the transition pathway between the  

![](images/7ef5396b3f0732644f5b01f79dd410e0f21f1121c5d05186d4db8b2e66ae9cd7.jpg)  

Figure 9.  Plots of eight states along the computed transition path- way for the Lennard-Jones system   $((a){\sim}(h))$  . During the transition process, particle  1  is migrating from the center of the cluster to its surface.  

metastable states of dynamical systems. It was demonstrated that the proposed method is able to sample the transition events efficiently and thus to predict the globally optimal transition pathway. We illustrated the ability of the method using three model systems.  

The proposed method provides a new perspective for inves- tigating the transition mechanism of systems with rough potential energy surfaces. In the future works, we intend to apply the method to more complex systems. Another direc- tion for future works is to consider the generalized task of predicting the transition pathway for systems with varying or unseen parameters.  

# Acknowledgement  

The work of B. Lin and W. Ren is partially supported by A\*STAR under its AME Programmatic programme: Ex- plainable Physics-based AI for Engineering Modelling & Design (ePAI) [Award No. A20H5b0142].  

# References  

Bolhuis, P. G., Chandler, D., Dellago, C., and Geissler, P. L. Transition path sampling: Throwing ropes over rough mountain passes, in the dark.  Annu. Rev. Phys. Chem. , 53 (1):291–318, 2002.  

Dellago, C., Bolhuis, P. G., and Chandler, D. Efficient transition path sampling: Application to lennard-jones cluster rearrangements.  J. Chem. Phys. , 108(22):9236– 9245, 1998.  

Dellago, C., Bolhuis, P. G., and Geissler, P. L. Transition path sampling.  Adv. Chem. Phys. , 123:1–78, 2002. Du, Q., Li, T., Li, X., and Ren, W. The graph limit of the minimizer of the onsager-machlup functional and its  

computation.  Science China Mathematics , 64:239–280, 2021. E, W. and Vanden-Eijnden, E. Transition-path theory and path-finding algorithms for the study of rare events.  Annu. Rev. Phys. Chem. , 61:391–420, 2010. E, W., Ren, W., and Vanden-Eijnden, E. String method for the study of rare events.  Phys. Rev. B , 66(5):052301, 2002. E, W., Ren, W., and Vanden-Eijnden, E. Minimum action method for the study of rare events.  Commun. Pure Appl. Math. , 57(5):637–656, 2004. E, W., Ren, W., and Vanden-Eijnden, E. Finite temperature string method for the study of rare events.  J. Phys. Chem. B , 109(14):6688–6693, 2005. E, W., Ren, W., and Vanden-Eijnden, E. Simplified and im- proved string method for computing the minimum energy paths in barrier-crossing events.  J. Chem. Phys. , 126(16), 2007. Evans, L., Cameron, M. K., and Tiwary, P. Computing com- mittors in collective variables via mahalanobis diffusion maps.  Applied and Computational Harmonic Analysis , 64:62–101, 2023. Fischer, S. and Karplus, M. Conjugate peak refinement: an algorithm for finding reaction paths and accurate tran- sition states in systems with many degrees of freedom. Chem. Phys. Lett. , 194(3):252–261, 1992. Fleming, W. H. Exit probabilities and optimal stochastic control.  Applied Mathematics and Optimization , 4:329– 346, 1977. Freidlin, M. I. and Wentzell, A. D.  Random Perturbations of Dynamical Systems . Springer Press, Berlin, Heidelberg, 2012. Fujimoto, S., Hoof, H., and Meger, D. Addressing function approximation error in actor-critic methods. In  Proceed- ings of the 35th International Conference on Machine Learning , volume 80, pp. 1587–1596. PMLR, 2018. Fujisaki, H., Shiga, M., and Kidera, A. Onsager–machlup action-based path sampling and its combination with replica exchange for diffusive and multiple pathways. J. Chem. Phys. , 132(13), 2010. Grafke, T. and Vanden-Eijnden, E. Numerical computation of rare events via large deviation theory.  Chaos: An Interdisciplinary Journal of Nonlinear Science , 29(6), 2019.  

Guo, J., Gao, T., Zhang, P., Han, J., and Duan, J. Deep reinforcement learning in finite-horizon to explore the most probable transition pathway.  Physica D: Nonlinear Phenomena , 458:133955, 2024. Haarnoja, T., Zhou, A., Abbeel, P., and Levine, S. Soft actor-critic: Off-policy maximum entropy deep reinforce- ment learning with a stochastic actor. In  Proceedings of the 35th International Conference on Machine Learning , volume 80, pp. 1861–1870. PMLR, 2018. Heymann, M. and Vanden-Eijnden, E. The geometric mini- mum action method: A least action principle on the space of curves.  Commun. Pure Appl. Math. , 61(8):1052–1117, 2008. J onsson, H., Mills, G., and Jacobsen, K. W. Nudged elastic band method for finding minimum energy paths of transi- tions. In  Classical and quantum dynamics in condensed phase simulations , pp. 385–404. World Scientific, 1998. Khoo, Y., Lu, J., and Ying, L. Solving for high-dimensional committor functions using artificial neural networks.  Re- search in the Mathematical Sciences , 6:1–13, 2019. Kingma, D. P. and Ba, J. Adam: A method for stochastic optimization. In  Proceedings of the 3rd International Conference on Learning Representations , 2015. Li, Q., Lin, B., and Ren, W. Computing committor functions for the study of rare events using deep learning.  J. Chem. Phys. , 151(5), 2019. Lillicrap, T. P., Hunt, J. J., Pritzel, A., Heess, N., Erez, T., Tassa, Y., Silver, D., and Wierstra, D. Continuous control with deep reinforcement learning.  arXiv preprint arXiv:1509.02971 , 2015. Maragliano, L., Fischer, A., Vanden-Eijnden, E., and Cic- cotti, G. String method in collective variables: Minimum free energy paths and isocommittor surfacesg.  J. Chem. Phys. , 125(2), 2006. Mnih, V., Kavukcuoglu, K., Silver, D., Graves, A., Antonoglou, I., Wierstra, D., and Riedmiller, M. Playing atari with deep reinforcement learning.  arXiv preprint arXiv:1312.5602 , 2013. Mnih, V., Kavukcuoglu, K., Silver, D., Rusu, A. A., Ve- ness, J., Bellemare, M. G., Graves, A., Riedmiller, M., Fidjeland, A. K., Ostrovski, G., Petersen, S., Beattie, C., Sadik, A., Antonoglou, I., King, H., Kumaran, D., Wier- stra, D., Legg, S., and Hassabis, D. Human-level control through deep reinforcement learning.  Nature , 518(7540): 529–533, 2015. Olender, R. and Elber, R. Calculation of classical trajecto- ries with a very large time step: Formalism and numerical examples.  J. Chem. Phys. , 105(20):9299–9315, 1996.  

Onsager, L. and Machlup, S. Fluctuations and irreversible processes.  Physical Review , 91(6):1505, 1953.  

Ren, W., Vanden-Eijnden, E., Maragakis, P., and E, W. Tran- sition pathways in complex systems: Application of the finite-temperature string method to the alanine dipeptide. J. Chem. Phys. , 123(13):6688–6693, 2005. Rotskoff, G. M., Mitchell, A. R., and Vanden-Eijnden, E. Active importance sampling for variational objectives dominated by rare events: Consequences for optimiza- tion and generalization. In  Mathematical and Scientific Machine Learning , pp. 757–780, 2022. Silver, D., Lever, G., Heess, N., Degris, T., Wierstra, D., and Riedmiller, M. Deterministic policy gradient algorithms. In  Proceedings of the 31st International Conference on Machine Learning , volume 32, pp. 387–395, 2014. Voter, A. F. Hyperdynamics: Accelerated molecular dynam- ics of infrequent events.  Phys. Rev. Lett. , 78(20):3908, 1997. Wang, J., Zhang, K., and Wang, E. Kinetic paths, time scale, and underlying landscapes: A path integral framework to study global natures of nonequilibrium systems and networks.  J. Chem. Phys. , 133(12), 2010. Zhou, X., Ren, W., and E, W. Adaptive minimum action method for the study of rare events.  J. Chem. Phys. , 128 (10), 2008.  

# A. The path space    $\mathbb{C}_{\gamma}$  .  

Theorem A.1.  T t  $\textstyle\bigcup_{\gamma>0}\mathbb{C}_{\gamma}$   a dense subset of  $\textstyle\bigcup_{T>0}\mathbb{C}_{[0,T]}$  .  

Proof.  F  $\varphi(t)$   in  $\textstyle\bigcup_{\gamma>0}\mathbb{C}_{\gamma}$  S  which is continuous and represented by a finite number of line segments, one can easily see that the path is absolute continuo us,  $\textstyle\bigcup_{\gamma>0}\mathbb{C}_{\gamma}$  is a subset of  $\textstyle\bigcup_{T>0}\mathbb{C}_{[0,T]}$  .  

Suppose  $\varphi(t)\in\mathbb{C}_{[0,T]}$   for a number  $T>0$  . Given  $\epsilon>0$  , we shall prove that there exists  $\gamma>0$   and a    $\psi(t)\in\mathbb{C}_{\gamma}$   such that  

$$
\operatorname*{max}_{t\in[0,T]}|\psi(t)-\varphi(t)|<3\epsilon.
$$  

In the following, when we consider a polygonal curve, we assume the time derivative of the curve on each line segment is constant.  

Since    $\varphi$   is absolute continuous, it is uniformly continuous. Thus, there exists  $\delta>0$   such that  

$$
\begin{array}{r}{|\varphi(t_{1})-\varphi(t_{2})|<\epsilon,\quad\forall\left|t_{1}-t_{2}\right|<\delta.}\end{array}
$$  

Let  $0=t_{0}<t_{1}<\cdot\cdot\cdot<t_{n}=T$   such that    $|t_{i}-t_{i-1}|<\delta$   and    $\varphi(t_{i-1})\neq\varphi(t_{i})$   for    $1\leqslant i\leqslant n$  . Then  $|\varphi(t_{i})-\varphi(t_{i-1})|<\epsilon$  for  $1\leqslant i\leqslant n$  .  

We first construct a polygonal curve    $\psi_{0}(t),\,0\leqslant t\leqslant T$   such that  

$$
\operatorname*{max}_{t\in[0,T]}|\psi_{0}(t)-\varphi(t)|<2\epsilon.
$$  

Let    $\psi_{0}(t)$   be a polygonal curve with vertices at the times  $\{t_{i}\}_{0\leqslant i\leqslant n}$   and  

$$
\psi_{0}(t_{i})=\varphi(t_{i}),\quad0\leqslant i\leqslant n.
$$  

Then for arbitrary time interval    $[t_{i-1},t_{i}]$   and    $t\in[t_{i-1},t_{i}]$  , we have  

$$
\begin{array}{r l}&{|\psi_{0}(t)-\varphi(t)|\leqslant|\psi_{0}(t)-\psi_{0}(t_{i-1})|+|\psi_{0}(t_{i-1})-\varphi(t_{i-1})|+|\varphi(t_{i-1})-\varphi(t)|}\\ &{\qquad\qquad=|\psi_{0}(t)-\psi_{0}(t_{i-1})|+|\varphi(t_{i-1})-\varphi(t)|}\\ &{\qquad\qquad\leqslant|\psi_{0}(t_{i})-\psi_{0}(t_{i-1})|+|\varphi(t_{i-1})-\varphi(t)|}\\ &{\qquad\qquad=|\varphi(t_{i})-\varphi(t_{i-1})|+|\varphi(t_{i-1})-\varphi(t)|}\\ &{\qquad\qquad<2\epsilon.}\end{array}
$$  

The last inequality is due to the uniform continuity ( 24 ) of    $\varphi$  . Hence, we have proved the inequality ( 25 ).  

Next, we construct a polygonal curve  $\psi(t),\;0\leqslant t\leqslant T$   with line segments of uniform length such that  

$$
\operatorname*{max}_{t\in[0,T]}|\psi(t)-\psi_{0}(t)|<\epsilon.
$$  

Denote the length of line segments in  $\psi_{0}$   by  

$$
\gamma_{i}=|\psi_{0}(t_{i})-\psi_{0}(t_{i-1})|,\quad1\leqslant i\leqslant n
$$  

and the minimum length by  

$$
\gamma=\operatorname*{min}_{1\leqslant i\leqslant n}|\psi_{0}(t_{i})-\psi_{0}(t_{i-1})|.
$$  

Since  $\gamma_{i}=|\varphi(t_{i})-\varphi(t_{i-1})|>0$  , we have    $\gamma>0$  . By the definition  ( 26 )  of    $\psi_{0}$   and the uniform continuity  ( 24 )  of    $\varphi$  , we have  $\gamma<\epsilon$  . We write the segment length in  $\psi_{0}$   as a sum of a multiple of the minimum length and a residual value,  i.e.  

$$
\gamma_{i}=k_{i}\gamma+2l_{i},\quad\mathrm{where~}k_{i}\in\mathbb{N}^{*}\mathrm{~and~}0\leqslant2l_{i}<\gamma.
$$  

To construct the polygonal curve  $\psi$  , we first let    $\psi(t_{i})=\psi_{0}(t_{i})$   for    $0\leqslant i\leqslant n$  . Then we shall carefully define  $\psi$   on each interval    $[t_{i-1},t_{i}]$   for    $1\leqslant i\leqslant n$  .  

We first consider th ase where    $l_{i}>0$  . Denote the time slice    $\Delta t=t_{i}-t_{i-1}$  . Let  $\beta$   be a unit vector that is normal to the  $i$  th line segment of  $\psi_{0}$  ,  i.e.  

$$
\left\langle\beta,\psi_{0}(t_{i-1})-\psi_{0}(t_{i})\right\rangle=0.
$$  

On the interval    $[t_{i-1},t_{i}]$  , we let the polygon curve    $\psi$   to have vertices  $\{\psi(t_{i-1}),\psi(t_{i-1}+\frac{l_{i}}{\gamma_{i}}\Delta t),\psi(t_{i}-\frac{l_{i}}{\gamma_{i}}\Delta t),\psi(t_{i})\}$  where  

$$
\begin{array}{c}{\displaystyle\psi(t_{i-1}+\frac{l_{i}}{\gamma_{i}}\Delta t)=\psi_{0}(t_{i-1}+\frac{l_{i}}{\gamma_{i}}\Delta t)+\sqrt{\gamma^{2}-l_{i}^{2}}\beta,}\\ {\displaystyle\psi(t_{i}-\frac{l_{i}}{\gamma_{i}}\Delta t)=\psi_{0}(t_{i}-\frac{l_{i}}{\gamma_{i}}\Delta t)+\sqrt{\gamma^{2}-l_{i}^{2}}\beta.}\end{array}
$$  

The specific form of  $\psi$   on    $[t_{i-1},t_{i}]$   is defined as  

$$
\psi(t_{i-1}+t)=\left\{\begin{array}{l l}{\displaystyle\psi_{0}(t_{i-1}+t)+\frac{\gamma_{i}t}{l_{i}\Delta t}\sqrt{\gamma^{2}-l_{i}^{2}}\beta,}&{t\in[0,\frac{l_{i}}{\gamma_{i}}\Delta t];}\\ {\displaystyle\psi_{0}(t_{i-1}+t)+\sqrt{\gamma^{2}-l_{i}^{2}}\beta,}&{t\in[\frac{l_{i}}{\gamma_{i}}\Delta t,\Delta t-\frac{l_{i}}{\gamma_{i}}\Delta t];}\\ {\displaystyle\psi_{0}(t_{i-1}+t)+\frac{\gamma_{i}(\Delta t-t)}{l_{i}\Delta t}\sqrt{\gamma^{2}-l_{i}^{2}}\beta,}&{t\in[\Delta t-\frac{l_{i}}{\gamma_{i}}\Delta t,\Delta t].}\end{array}\right.
$$  

One can verify that the following distance is equal to the minimum length  $\gamma$   as defined in Eq. ( 28 ),  

$$
\begin{array}{r l}&{~~~~\left|\psi(t_{i-1}+\frac{l_{i}}{\gamma_{i}}\Delta t)-\psi(t_{i-1})\right|}\\ &{=\left|\psi_{0}(t_{i-1}+\frac{l_{i}}{\gamma_{i}}\Delta t)-\psi_{0}(t_{i-1})+\sqrt{\gamma^{2}-l_{i}^{2}}\beta\right|}\\ &{=\left(|\psi_{0}(t_{i-1}+\frac{l_{i}}{\gamma_{i}}\Delta t)-\psi_{0}(t_{i-1})|^{2}+(\gamma^{2}-l_{i}^{2})\right)^{\frac{1}{2}}}\\ &{=\left(\left(\frac{l_{i}}{\gamma_{i}}\Delta t\frac{|\psi_{0}(t_{i})-\psi_{0}(t_{i-1})|}{\Delta t}\right)^{2}+(\gamma^{2}-l_{i}^{2})\right)^{\frac{1}{2}}}\\ &{=\gamma.}\end{array}
$$  

Similarly, we have  

$$
\left|{\psi(t_{i}-\frac{l_{i}}{\gamma_{i}}\Delta t)-\psi(t_{i})}\right|=\gamma.
$$  

Also, one can show that the distance between  $\psi(t_{i-1}+\frac{l_{i}}{\gamma_{i}}\Delta t)$   and  $\psi(t_{i}-\frac{l_{i}}{\gamma_{i}}\Delta t)$   is a multiple of  $\gamma$  ,  

$$
\begin{array}{r l}&{\left|\psi(t_{i}-\frac{l_{i}}{\gamma_{i}}\Delta t)-\psi(t_{i-1}+\frac{l_{i}}{\gamma_{i}}\Delta t)\right|}\\ &{=\left|\psi_{0}(t_{i}-\frac{l_{i}}{\gamma_{i}}\Delta t)-\psi_{0}(t_{i-1}+\frac{l_{i}}{\gamma_{i}}\Delta t)\right|}\\ &{=\frac{t_{i}-t_{i-1}-\frac{2l_{i}}{\gamma_{i}}\Delta t}{\Delta t}|\psi_{0}(t_{i})-\psi_{0}(t_{i-1})|}\\ &{=\frac{\Delta t-\frac{2l_{i}}{\gamma_{i}}\Delta t}{\Delta t}\gamma_{i}}\\ &{=k_{i}\gamma.}\end{array}
$$  

In sum, the curve    $\psi$   over  $[t_{t-1},t_{i}]$   as defined in Eq.  ( 29 )  is composed of three line segments with the lengths  $\gamma,k_{i}\gamma$   and  $\gamma$  , respectively. One can treat    $\psi$   over    $[t_{t-1},t_{i}]$   as a polygon curve of  $k_{i}+2$   line segments with uniform length  $\gamma$  . Thus, we see that the constructed curve  $\psi\in\mathbb{C}_{\gamma}$  .  

For another case where    ${{l}_{i}}\mathrm{~=~}0$  , we simply set    $\psi(t)=\psi_{0}(t),\,t\,\in\,[t_{i-1},t_{i}]$  . Then  $\psi$   over    $[t_{i-1},t_{i}]$   can be regarded as a polygon curve of  $k_{i}$   line segments with uniform length    $\gamma$  . Also in this case, the constructed curve  $\psi\in\mathbb{C}_{\gamma}$  .  

Moreover, in the latter case  ${{l}_{i}}=0$  , we have    $\begin{array}{r}{\operatorname*{max}_{t\in[t_{i-1},t_{i}]}|\psi(t)-\psi_{0}(t)|=0}\end{array}$  . In the case  $l_{i}>0$  , we have  

$$
\operatorname*{max}_{t\in[t_{i-1},t_{i}]}|\psi(t)-\psi_{0}(t)|=\left|\sqrt{\gamma^{2}-l_{i}^{2}}\beta\right|\leqslant\gamma<\epsilon.
$$  

This proves the inequality ( 27 ). Therefore, combing the inequality ( 25 ) and ( 27 ), we find a path    $\psi\in\mathbb{C}_{\gamma}$   such that  

$$
\begin{array}{r l}&{\displaystyle\operatorname*{max}_{t\in[0,T]}|\psi(t)-\varphi(t)|\leqslant\displaystyle\operatorname*{max}_{t\in[0,T]}|\psi(t)-\psi_{0}(t)|+\displaystyle\operatorname*{max}_{t\in[0,T]}|\psi_{0}(t)-\varphi(t)|}\\ &{\qquad\qquad\qquad\qquad<\epsilon+2\epsilon}\\ &{\quad\quad\quad\quad\quad\quad\quad=3\epsilon.}\end{array}
$$  

# B. Numerical quadratures for approximating the integral in problem  ( 6 ) .  

One can use a numerical quadrature with  $m$   grid points to approximate the integral as in problem  ( 6 ) , where  $m$   is a positive integer. We discretize the time interval    $[0,h_{i}]$   using    $m$   uniform points:    $t_{j}=(j-1/2)/m\cdot h_{i}$  ,    $1\leqslant j\leqslant m$  . Denote the position of the path    $\varphi^{i}(t)$   at time  $t_{j}$   by  

$$
z_{i}^{j}=\varphi^{i}(t_{j})=z_{i}+\frac{j-1/2}{m}(z_{i+1}-z_{i}),\quad1\leqslant j\leqslant m.
$$  

Then the integral in the problem ( 6 ) can be approximated by  

$$
\begin{array}{l}{\displaystyle\tilde{L}(z_{i},z_{i+1};h_{i})\approx\frac{h_{i}}{m}\sum_{j=1}^{m}\left|\frac{z_{i+1}-z_{i}}{h_{i}}+\nabla V(z_{i}^{j})\right|^{2}}\\ {\displaystyle\geqslant2|z_{i+1}-z_{i}|\cdot\sqrt{\frac{1}{m}\sum_{j=1}^{m}|\nabla V(z_{i}^{j})|^{2}}+2\langle z_{i+1}-z_{i},\frac{1}{m}\sum_{j=1}^{m}\nabla V(z_{i}^{j})\rangle.}\end{array}
$$  

where the minimum value is achieved by setting  

$$
h_{i}^{*}=|z_{i+1}-z_{i}|\left/\sqrt{\frac{1}{m}\sum_{j=1}^{m}|\nabla V(z_{i}^{j})|^{2}}\;.\right.
$$  

By setting  $m=1$  , the cost function ( 30 ) reduces to the one in Eq. ( 7 ) using the mid-point quadrature as in the paper.  

# C. The parameters in Algorithm  1  used for the numerical examples in Section  3 .  

<td><table  border="1"><thead><tr><td></td><td><b>Parameters</b></td><td><b>2D system</b></td><td><b>Mueller system</b></td><td><b>Lennard-Jones system</b></td></tr></thead><tbody><tr><td></td><td>Network structure Activation on hidden layers Activation on output layer ></td><td>tanh  sigmoid 1000 4-50-50-1</td><td>20-50-50-1 tanh  sigmoid 1000</td><td>tanh sigmoid 1000 24-100-100-1</td></tr><tr><td></td><td>Activation on output layer</td><td>1000</td><td>1000</td><td>12-100-100-12</td></tr><tr><td></td><td>1000</td><td>2-50-50-2</td><td>10-50-50-10</td><td>tanh</td></tr><tr><td>Activation on output layer</td><td>Activation on hidden layers Network structure</td><td>tanh  None</td><td>tanh  None</td><td>None</td></tr><tr><td>macstep (# of training steps) mactime (maximum length of one episode)</td><td> in the path space C</td><td>0.1</td><td> None</td><td>0.2</td></tr></tbody></table></td>  

# D. Computing the transition tube for the Mueller system.  

For the Mueller system with potential function  ( 21 ) , we define the two metastable set  $S_{A}$  ,  $S_{B}$   with radius  $r_{0}$   around the states    $A,B$   as  

$$
S_{A}=\{x\in\mathbb{R}^{10}:|(x_{1},x_{2})-(A_{1},A_{2})|<r_{0}\},\quad S_{B}=\{x\in\mathbb{R}^{10}:|(x_{1},x_{2})-(B_{1},B_{2})|<r_{0}\}
$$  

with    $r_{0}=0.1$  , where    $\left(A_{1},A_{2}\right)$   and    $(B_{1},B_{2})$   denote the first two numbers in the coordinates of    $A$   and    $B$  , respectively. The first hitting time of the two sets  $S_{A}$   and  $S_{B}$   is defined as  

$$
\tau_{A}(z)=\operatorname*{inf}_{t>0}\{x_{t}\in S_{A}:x_{0}=z\},\quad\tau_{B}(z)=\operatorname*{inf}_{t>0}\{x_{t}\in S_{B}:x_{0}=z\}.
$$  

The committor function  $q(x)$   is defined in the configuration space, which is the probability that the system starting from    $x$  first arrives in  $S_{B}$   rather than  $S_{A}$  :  

$$
q(x)=\mathrm{Prob}[\tau_{A}(x)>\tau_{B}(x)].
$$  

A mathematical description for the committor function is given by the backward Kolmogorov equation with the Dirichlet boundary conditions:  

$$
\begin{array}{r}{\left\{\nabla V(x)\cdot\nabla q(x)-\epsilon\Delta q(x)=0,\quad x\in\Omega\setminus(S_{A}\cup S_{B})\right.}\\ {\quad q(x)=0,\;x\in\partial S_{A};\quad q(x)=1,\;x\in\partial S_{B}.}\end{array}
$$  

We compute the committor function  $q_{m}(x_{1},x_{2})$   for the  2 D Mueller system with the potential  $V_{m}(x_{1},x_{2})$   at  $\epsilon=10$   by solving the partial differential equation  ( 31 )  using the finite element method. The computational domain is taken as  

![](images/15dc330f8bd0f37a30e01af054a734c52f487b3ae88fb434349d02fe3e2459f2.jpg)  
Figure 10.  Plots of the computed transition tube and its centerline for the potential function  $V_{m}(x_{1},x_{2})$   at  $\epsilon=10$   with different confidence levels,  $\nu=0.68$   ( Left ) and  $\nu=0.95$   ( Right ). The contour lines indicate the potential function.  

$\Omega=[-1.5,1]\times[-0.5,2]$  . Then the committor function  $q(x)$   for the  10 D Mueller system with the potential  ( 21 )  is given by  $q(x_{1},.\,.\,,x_{10})=q_{m}(x_{1},x_{2})$  .  

The committor function itself is a good reactive coordinate for describing the transition of the system. As illustrated in Ref. ( Ren et al. ,  2005 ), the transition tube can be characterized by the iso-committor surfaces of the committor function. For the  10 D Mueller system considered in the numerical example, the transition events can be characterized by the transition tube corresponding to the first two dimensions    $(x_{1},x_{2})$  .  

Next, we compute the transition tube for the two-dimensional potential    $V_{m}(x_{1},x_{2})$   at    $\epsilon=10$  . To approximate the iso- committor surfaces, we divide the configuration space into sub-regions using a transition pathway ( e.g.  the minimum energy path corresponding to the potential    $V_{m}(x_{1},x_{2})$   with    $\omega=0$  ). Specifically, the transition pathway  $\varphi$   is represented  $N_{p}=185$   $z_{1},.\.\.\,,z_{N_{p}}\in\mathbb{R}^{2}$  stance. Denote the co mittor function  $q_{m}(x_{1},x_{2})$   on these points by  $q_{i}=q_{m}(z_{i})$  ,  $1\leq i\leq N_{p}$   ≤  ≤ . Note that  $q_{1}<\cdot\cdot\cdot<q_{N_{p}}$  . We approximate the  $q_{i}$  -isocommittor surface using the region  

$$
\begin{array}{r}{\Omega_{i}=\{(x_{1},x_{2})\in\mathbb{R}^{2}:(q_{i-1}+q_{i})/2<q_{m}(x_{1},x_{2})<(q_{i}+q_{i+1})/2\},\quad1\leq i\leq N_{p}}\end{array}
$$  

where    $q_{0}=-q_{1}$   and    $q_{N_{p}+1}=2-q_{N_{p}}$  .  

We discretize the computational domain    $\Omega$  using a mesh with  $500\times500$   grid points. The set of grid points is denoted by  $\{X_{k}\}_{k\in\mathcal{Z}}$  . Denote by  $\mathcal{T}_{i}$   the indices of the grid points in    $\{X_{k}\}_{k\in\mathcal{Z}}$   which locate inside the region  $\Omega_{i}$  ,  

$$
\begin{array}{r}{\mathcal{Z}_{i}=\left\{k\in\mathcal{Z}:X_{k}\in\Omega_{i}\right\}\quad1\leq i\leq N_{p}.}\end{array}
$$  

We assign the following Gibbs-Boltzmann weight to each grid point in    $\{X_{k}\}_{k\in\mathcal{Z}_{i}}$   in the region  $\Omega_{i}$  ,  

$$
w_{k}=\frac{1}{Z_{i}}\exp\left[-\frac{V_{m}(X_{k})}{\epsilon}\right],\quad k\in\mathcal{Z}_{i}
$$  

where the normalization constant  $\begin{array}{r}{Z_{i}=\sum_{k\in\mathcal{Z}_{i}}\exp[-V_{m}(X_{k})/\epsilon]}\end{array}$  P . The centerline of the transition tube can be represented by the weighted average of the grid points on each region  $\Omega_{i}$  :  

$$
c_{i}=\sum_{k\in\mathcal{Z}_{i}}w_{k}\cdot X_{k},\quad1\leq i\leq N_{p}.
$$  

To represent the transition tube, we sort the weights and choose a subset  $\{X_{k}\}_{k\in\mathcal{I}_{i}}$   of    $\{X_{k}\}_{k\in\mathcal{Z}_{i}}$   containing the least number of gird points with the largest weights    $w_{k}$   such that  

$$
\sum_{k\in\mathcal{I}_{i}}w_{k}\ge\nu,
$$  

where  $\nu\in[0,1]$   denotes the confidence level. Then the transition tube is represented by a collection of grid point sets,  $\{X_{k}\}_{k\in\mathcal{I}_{i}}$  ,  $1\leq i\leq N_{p}$  .  

In Fig.  10 , we show the plots of the computed transition tube and its centerline using two different values for  $\nu$   (  $\nu=0.68$  and  $\nu=0.95$  ). In the numerical example, we take    $\nu=0.68$  , as shown in upper panel of Fig.  7 .  

# E. Construction of the transformation function  $\tau(x)$   for the Lennard-Jones system.  

Since the Lennard-Jones system is invariant to translation of the particles in the system, we fix the coordinate of particle  1  at the origin,  i.e.    $y_{1}=(0,0)$   in the example. Thus the system is defined in the  12 -dimensional space with the configuration  $x=(y_{2},.\,.\,.\,,y_{7})$  , where    $y_{i}$   denotes the coordinate of particle  $i$  .  

Before introducing the transformation function, we define two angle functions as follows.  

Definition.  The angle    $f(u,v)\in[0,\pi]$   between two nonzero vectors    $u=\left(u_{1},u_{2}\right)$   and    $v=(v_{1},v_{2})$   in  $\mathbb{R}^{2}$    is defined as  

$$
f(u,v)=\operatorname{arccos}\left({\frac{\langle u,v\rangle}{\left|u\right|\cdot\left|v\right|}}\right).
$$  

Then we define the oriented angle between  u  and  v  as  

$$
\eta(u,v)=\left\{\!\!\begin{array}{l l}{f(u,v),}&{\langle u^{\prime},v\rangle\geq0}\\ {2\pi-f(u,v),}&{\langle u^{\prime},v\rangle<0}\end{array}\right.
$$  

where the vector    $u^{\prime}=\left(-u_{2},u_{1}\right)$  . Note that    $\eta(u,v)\in[0,2\pi]$  .  

Next, we construct a transformation function  $\tau(x)$   for the system in a two-step procedure.  

# (1) Rotating the cluster  

We compute the mean vector  

$$
\bar{y}=\frac{1}{6}(y_{2}+\cdot\cdot\cdot+y_{7}).
$$  

Let    $k$   be the number that solves  

$$
k=\mathop{\underset{2\leq i\leq7}{\operatorname{arg\,min}}}f(y_{i},{\bar{y}}).
$$  

Using the particle  $k$  , we set the angle  

$$
\beta=\eta(y_{k},e_{x}),
$$  

where    $e_{x}$   denotes the unit vector    $e_{x}=(1,0)$  , and construct the rotation matrix  

$$
D_{\beta}=\left[\!\!\begin{array}{c c}{{\!\cos\beta}}&{{-\sin\beta}}\\ {{\!\sin\beta}}&{{\!\!\cos\beta}}\end{array}\!\!\right].
$$  

We rotate the cluster with configuration    $x$   to  $x^{\prime}=(y_{2}^{\prime},.\,.\,.\,,y_{7}^{\prime})$  ,  

$$
y_{i}^{\prime}=D_{\beta}\left[{y_{i1}\atop y_{i2}}\right],\quad2\leq i\leq7
$$  

where    $y_{i}=\left(y_{i1},y_{i2}\right)$   denotes the coordinates of particle  $i$  . In the new configuration  $x^{\prime}$  , the particle    $k$   is on the    $x$  -axis.  

![](images/8965cc1b24e43f0dab9e9f0c6b6f94c4231ab5b26b6dccd27a94ec4dbd813759.jpg)  
Figure 11.  Illustration of the two-step procedure for the transformation function  $\tau(x)$   using two example clusters of the Lennard-Jones system.  

# (2) Re-indexing the particles  

We sort the angles    $\{\eta(e_{x},y_{i}^{\prime})\}$  } ,    $2\,\leq\,i\,\leq\,7$   of the particles and obtain the particle sequence    $(y_{\tau(2)}^{\prime},\dots,y_{\tau(7)}^{\prime})$  , where  $(\tau(2),\dots,\tau(7))$   denote the indices of the sorted particles.  

Therefore, the transformation function is defined as:    $\mathcal{T}(x)=(y_{\tau(2)}^{\prime},.\,.\,.\,,y_{\tau(7)}^{\prime})$  . In Fig.  11 , we use two example clusters of the Lennard-Jones system to illustrate the above procedure for  $\tau(x)$  .  

To incorporate the transformatio n    $\tau(x)$   into he critic and actor netwo  We compute the critic function    $Q_{\theta}$  and actor function    $\mu_{\theta}$   at the state  $s\in\mathbb{R}^{12}$   ∈   and action  a  which is a unit vector in  R  $\mathbb{R}^{12}$    as follows We co pute    $s^{\prime}=\mathcal{T}(s)$  with rotation matrix    $D_{\beta}$   and indices    $(\tau(2),\dots,\tau(7))$  . Then we compute the transformed action  $a^{\prime}$    from  a  using the same rotation    $D_{\beta}$   and index function    $\tau$  . The critic function at    $(s,a)$   is given by    $Q_{\theta}(s^{\prime},a^{\prime})$  .  

Denote    ${\tilde{a}}=\mu_{\theta}(s^{\prime})$   and let  $\tau^{-1}$    be the inverse function of  $\tau$  . We compute the transformed action  $\tilde{a}^{\prime}$    from  $\tilde{a}$   using the rotation  $D_{-\beta}$   and index function    $\tau^{-1}$  . The actor function at  $s$   is given by  $\tilde{a}^{\prime}$  .  