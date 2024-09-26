# AirGNNs: Graph Neural Networks over the Air 

Zhan Gao ${ }^{\dagger}$ and Deniz Gündüz ${ }^{\ddagger}$<br>${ }^{\dagger}$ Department of Computer Science and Technology, University of Cambridge, Cambridge, UK<br>${ }^{\ddagger}$ Department of Electrical and Electronic Engineering, Imperial College London, London, UK<br>E-mails: zg292@cam.ac.uk, d.gunduz@@imperial.ac.uk


#### Abstract

Graph neural networks (GNNs) are information processing architectures that model representations from networked data and allow for decentralized implementation through localized communications. Existing GNN architectures often assume ideal communication links and ignore channel effects, such as fading and noise, leading to performance degradation in real-world implementation. This paper proposes graph neural networks over the air (AirGNNs), a novel GNN architecture that incorporates the communication model into the architecture. AirGNN modifies the graph convolutional operation that shifts graph signals over random communication graphs to take into account channel fading and noise when aggregating features from neighbors, thus, improving the architecture robustness to channel impairments during testing. We propose a stochastic gradient descent based method to train the AirGNN, and show that the training procedure converges to a stationary solution. Numerical simulations on decentralized source localization and multi-robot flocking corroborate theoretical findings and show superior performance of the AirGNN over wireless communication channels.


Index Terms—Graph neural networks, decentralized implementation, wireless channel fading, Gaussian noise

## I. INTRODUCTION

Graph neural networks (GNNs) are one of the key tools to extract features from networked data [1]-[4], and have found wide applications in wireless communications [5], [6], multiagent coordination [7]-[9] and recommendation systems [10][12]. GNNs extend conventional convolutional neural networks (CNNs) to graph structures by employing a multi-layered architecture with each layer comprising a graph filter bank and a pointwise nonlinearity [13]. With the distributed nature of graph filters, GNNs can compute output features with local neighborhood information. This makes GNNs suitable candidates for decentralized implementation, where each node takes actions by only sensing its local environment and communicating with its neighboring nodes [14], [15].

On the other hand, when implemented in a decentralized fashion, information exchanges among neighboring nodes of GNNs require wireless transmissions. Existing works often assume ideal communications and ignore channel impairments, such as fading and noise, which affect all wireless transmissions [16]-[18]. In real-world wireless networks, each node receives faded/noisy messages from its neighbors and computes its output that mismatches the one assuming ideal communications during training; hence, resulting in performance degradation during testing. The work in [19] studied the privacy-preserving problem in decentralized implementation of GNNs over wireless communication channels and used channel state information (CSI) to design signaling strategies for privacy enhancement, while [20] considered the decentralized power allocation problem and estimated CSI to generate transmitted power with GNNs. However, these works require CSI to design signaling strategies for decentralized implementation, which may be inaccurate or unavailable, and focus on specific problems, which are not applicable for general decentralized tasks. In addition, they apply the message passing mechanism of GNNs based on direct adjacencies, i.e., immediate neighbors, without higherorder/multi-hop information.

This paper proposes the AirGNN which incorporates wireless communication channels directly into the GNN architecture. This is inspired by [21], which showed that incorporating channel noise into training can make deep neural networks more robust when network parameters are delivered over noisy communication channels. The AirGNN accounts for channel fading effects and Gaussian noise among the nodes of a GNN during training, where each node generates features based on faded/noisy neighborhood information from multi-hop communications. This yields the learned parameters robust to wireless channel impairments during implementation and improves performance in decentralized tasks without requiring CSI to modulate signals. Our contributions are summarized as follows:
(i) We develop the AirGNN framework as a multi-layered architecture where each layer consists of graph filters over the air (AirGFs) and a pointwise nonlinearity (Sec. II). The AirGF shifts graph signals over wireless communication channels in an uncoded fashion to collect multi-hop neighborhood information and generates higher-level features by aggregating faded/noisy information. These features are passed to the nonlinearity and subsequently to successive layers to generate the output of the AirGNN.
(ii) We formulate the cost function with respect to (w.r.t.) channel fading effects and Gaussian noise, and develop a stochastic gradient descent (SGD) based method to train the AirGNN (Sec. III). We show that this training procedure is equivalent to solving an associated stochastic optimization problem with SGD and prove its convergence to a stationary solution at a rate proportional to the inverse square root of the number of iterations (Sec. IV).
(iii) We evaluate AirGNNs numerically on the decentralized tasks of source localization and multi-robot flocking to corroborate theoretical findings, and show that they consistently outperform the conventional GNN implemented over noisy communication channels, i.e., when channel effects are ignored during training (Sec. V).

## II. GNNs OVER The AIR (AIrGNNs)

Let $\mathcal{G}=(\mathcal{V}, \mathcal{E})$ be a graph with node set $\mathcal{V}=\{1, \cdots, n\}$ and edge set $\mathcal{E}$. The graph structure can be represented by an $n \times n$ matrix $\mathbf{S}$, referred to as the graph shift operator, with $(i, j)$ th entry $[\mathbf{S}]_{i j}=s_{i j}$ non-zero only if node $j$ is connected to node $i$, i.e., $(j, i) \in \mathcal{E}$, or $i=j$, such as the adjacency matrix $\mathbf{A}$



and the Laplacian matrix $\mathbf{L}$ [22]. The graph signal is a vector defined on the nodes $\mathbf{x}=\left[x_{1}, \ldots, x_{n}\right]^{\top}$, where the $i$ th entry $x_{i}$ is the signal value associated to node $i$. The graph serves as a mathematical representation of the network topology and the graph signal captures the network states. For example, in a multi-agent system, nodes can correspond to agents, edges to communication links, and signal values to agent states.

The graph shift operation $\mathcal{S} \mathbf{x}$ is one of the key operations in graph signal processing. It assigns to each node $i$ the aggregated information from its neighboring nodes $[\mathbf{x}(1)]_{i}=[\mathcal{S} \mathbf{x}]_{i}$ and extends the signal shifting from the time/space domain to the graph domain. In the context of real-world networked systems (e.g., sensor networks and multi-agent systems), this corresponds to message exchanges between the neighboring sensors/agents over available communications links. However, $\mathcal{S} \mathbf{x}$ assumes perfect signal transmissions between nodes and ignores the fact that communication links suffer from channel fading and additive noise in practice.

Communication channel. We assume that each node exchanges information wirelessly with the neighboring nodes in its communication range. The channel between the nodes $i$ and $j$ is modeled as a slow fading channel, the signal value $[\mathbf{x}]_{j}$ is transmitted in an uncoded/analog manner, and the neighborhood information is aggregated at node $i$ with over-the-air computation, i.e.,

$$
[\mathbf{x}(1)]_{i}=\sum_{j:(i, j) \in \mathcal{E}} h_{i j}^{(1)}[\mathbf{x}]_{j}+n_{i}^{(1)}, \text { for } i=1, \ldots, n
$$

where $h_{i j}^{(1)}$ is the channel gain from node $j$ to node $i$ and $n_{i}^{(1)}$ is the zero-mean Gaussian noise at node $i$. The channel fading effects $\left\{h_{i j}\right\}$ are assumed independent across communication links, which are fixed throughout a single transmission but change from one transmission to the next in an independent and identically distributed (i.i.d.) manner. Hence, each node receives noisy and faded versions of the messages sent by its neighbors, and the graph shift operation becomes

$$
\mathbf{x}(1)=\mathcal{S}_{\text {air }}^{(1)} \mathbf{x}+\mathbf{n}^{(1)}
$$

where $\mathcal{S}_{\text {air }}^{(1)}$ is the graph shift operator with channel fading effects, i.e., $\left[\mathcal{S}_{\text {air }}^{(1)}\right]_{i j}=h_{i j}^{(1)}$ for any $(i, j) \in \mathcal{E}$, and $\mathbf{n}$ is the Gaussian noise vector with $[n]_{i}=n_{i}$ for $i=1, \ldots, n$. Different from its ideal counterpart $\mathcal{S} \mathbf{x}$, the signal shifting in (2) depends not only on the graph topology, but also on the communication channels, and we refer to the latter as the graph shift operation over the air (AirGSO).

Graph filter over the air (AirGF). AirGF is a linear combination of multi-shifted signals over the air. Specifically, an AirGSO shifts $\mathbf{x}$ over $\mathcal{S}$ through wireless communication channels and obtains the one-shifted signal $\mathbf{x}(1)$ that aggregates $1-$ hop neighborhood information [cf. (2)]. By recursively shifting $\mathbf{x}$, the $k$-shifted signal $\mathbf{x}(k)$ is

$$
\begin{aligned}
\mathbf{x}(k) & =\mathcal{S}_{\mathrm{air}}^{(k)}\left(\mathcal{S}_{\mathrm{air}}^{(k-1)}\left(\cdots+\mathbf{n}^{(1)}\right)+\mathbf{n}^{(k-1)}\right)+\mathbf{n}^{(k)} \\
& =\prod_{\kappa=1}^{k} \mathcal{S}_{\mathrm{air}}^{(\kappa)} \mathbf{x}+\sum_{i=1}^{k-1} \prod_{\kappa=i+1}^{k} \mathcal{S}_{\mathrm{air}}^{(\kappa)} \mathbf{n}^{(i)}+\mathbf{n}^{(k)}
\end{aligned}
$$

where $\mathcal{S}_{\text {air }}^{(k)}$ and $\mathbf{n}^{(k)}$ are, respectively, the AirGSO and Gaussian noise vector at the $k$ th graph shift operation. ${ }^{1}$ The $k$-shifted

[^0]signal $\mathbf{x}(k)$ accesses farther nodes and aggregates the $k$-hop neighborhood information with communication noise. Given a sequence of shifted signals $\left\{\mathbf{x}, \mathbf{x}(1), \ldots, \mathbf{x}^{(K)}\right\}$, the AirGF aggregates them with a set of filter coefficients as

$$
\begin{aligned}
\mathbf{H}_{\mathrm{air}}(\mathcal{S}) \mathbf{x} & =\sum_{k=0}^{K} \alpha_{k} \mathbf{x}^{(k)}=\mathbf{P}_{\mathrm{air}}(\mathcal{S}, \mathbf{x})+\mathbf{N}_{\mathrm{air}}(\mathcal{S}, \mathbf{n}) \\
& =\sum_{k=0}^{K} \alpha_{k} \prod_{\kappa=1}^{k} \mathcal{S}_{\mathrm{air}}^{(\kappa)} \mathbf{x}+\sum_{k=1}^{K} \alpha_{k}\left(\sum_{i=1}^{k-1} \prod_{\kappa=i+1}^{k} \mathcal{S}_{\mathrm{air}}^{(\kappa)} \mathbf{n}^{(i)}+\mathbf{n}^{(k)}\right)
\end{aligned}
$$

where $\mathbf{x}^{(0)}=\mathbf{x}$ by default and $\boldsymbol{\alpha}=\left[\alpha_{0}, \ldots, \alpha_{K}\right]^{\top}$ are the filter coefficients. The first term in (4) captures the signal information perturbed by the communication channels, referred to as the signal component, while the second term in (4) is the accumulated noise, referred to as the noise component.

The AirGF is a shift-and-sum operator that extends graph convolution to wireless communication channels. It aggregates the neighborhood information up to a radius of $K$ and accounts for channel fading and Gaussian noise when shifting signals over the underlying graph. AirGF reduces to a conventional graph filter in ideal scenarios, where the communication links are perfect, i.e., $h_{i j}^{(1)}=1$ and $n_{i}^{(1)}=0$ in (1).

AirGNN. AirGNN is an information processing architecture that consists of multiple layers, where each layer comprises a bank of AirGFs and a pointwise nonlinearity. Specifically, at layer $\ell$, we have $F$ input signals $\left\{\mathbf{x}_{\ell-1}^{g}\right\}_{g=1}^{F}$ generated by the previous layer $\ell-1$. The latter are processed by a bank of AirGFs $\left\{\mathbf{H}_{\mathrm{air}, \ell}^{f g}\right\}_{f g}$, aggregated over the input index $g$, and passed through a pointwise nonlinearity $\sigma(\cdot)$ as

$$
\mathbf{x}_{\ell}^{f}=\sigma\left(\sum_{g=1}^{F} \mathbf{H}_{\mathrm{air}, \ell}^{f g}(\mathcal{S}) \mathbf{x}_{\ell-1}^{g}\right), \forall f=1, \ldots, F
$$

The outputs $\left\{\mathbf{x}_{\ell}^{f}\right\}_{f=1}^{F}$ are fed into layer $\ell+1$ until the final layer L. Without loss of generality, we consider a single input $\mathbf{x}_{0}^{1}=\mathbf{x}$ and a single output $\mathbf{x}_{L}^{1}$. The AirGNN can be represented as a nonlinear mapping $\Phi_{\text {air }}(\mathbf{x}, \mathcal{S}, A)$ of graph signals $\mathbf{x}$, where $A$ are the architecture parameters comprising all filter coefficients. AirGNN reduces to a conventional GNN if assuming ideal communications without channel fading or noise among the neighboring nodes.

Decentralized implementation. AirGNN and AirGF are ready for decentralized implementation, i.e., each node can compute its own output

full knowledge of the graph to compute the AirGNN/AirGF output, but only the ability to communicate local signals in a synchronized manner with their neighbors, in order to allow over-the-air aggregation, similarly to [23], [24].

With the consideration of wireless communication channels, the AirGNN output is a random variable w.r.t. channel state information (CSI) and Gaussian noise [cf. (1)]. It is unclear how to train the AirGNN, whether the training procedure converges to a stationary solution, and what solution it searches for. We address these aspects in the following sections.

## III. TRAINING

We develop a SGD based method to train the AirGNN. For a specific task with the training set $\mathbb{R}=\left\{\left(\boldsymbol{x}^{r}, y^{r}\right)\right\}_{r=1}^{R}$ and loss function $\ell(\cdot)$, we define the objective function as the expected loss over the training set

$$
\mathcal{L}(\mathbb{R}, \boldsymbol{S}, \boldsymbol{A})=\frac{1}{R} \sum_{r=1}^{R} \ell\left(y^{r}, \Phi_{\text {air }}\left(\boldsymbol{x}^{r}, \boldsymbol{S}, \boldsymbol{A}\right)\right)
$$

Since the AirGNN output $\Phi_{\mathrm{air}}\left(\boldsymbol{x}^{r}, \boldsymbol{S}, \boldsymbol{A}\right)$ is a random variable, the objective $\mathcal{L}(\mathbb{R}, \boldsymbol{S}, \boldsymbol{A})$ is a random function w.r.t. channel fading effects and Gaussian noise. The goal is to find the optimal architecture parameters $\boldsymbol{A}^{*}$ that minimize the objective function $\mathcal{L}(\mathbb{R}, \boldsymbol{S}, \boldsymbol{A})$ while accounting for channel impairments.

We propose to update $\boldsymbol{A}$ with gradient descent while incorporating the randomness of the communication channels during training. Specifically, let $\Phi_{\text {air }}(\boldsymbol{x}, \boldsymbol{S}, \boldsymbol{A} \mid h, n)$ be a sample of the AirGNN output on the graph signal $\boldsymbol{x}$, where $h$ and $\boldsymbol{n}$ are samples of the CSI and the Gaussian noise, respectively, throughout graph shift operations of all AirGFs in the architecture. The training procedure contains successive iterations to optimize the objective function, where each iteration $t$ consists of a forward and a backward phase. In the forward phase, it samples the CSI $h^{t}$ and the Gaussian noise $\boldsymbol{n}^{t}$ for a deterministic AirGNN architecture $\boldsymbol{\Phi}_{\text {air }}\left(\boldsymbol{x}, \boldsymbol{S}, \boldsymbol{A}^{t} \mid h^{t}, \boldsymbol{n}^{t}\right)$ with parameters $\boldsymbol{A}^{t}$. The latter processes a random set of the training data $\mathbb{R}^{t} \in \mathbb{R}$ to approximate the objective function as

$$
\mathcal{L}\left(\mathbb{R}^{t}, \boldsymbol{S}, \boldsymbol{A}^{t} \mid h^{t}, \boldsymbol{n}^{t}\right)=\frac{1}{\left|\mathbb{R}^{t}\right|} \sum_{r=1}^{\left|\mathbb{R}^{t}\right|} \ell\left(y^{r}, \Phi_{\mathrm{air}}\left(\boldsymbol{x}^{r}, \boldsymbol{S}, \boldsymbol{A}^{t} \mid h^{t}, \boldsymbol{n}^{t}\right)\right)
$$

where $\left(\boldsymbol{x}^{r}, y^{r}\right) \in \mathbb{R}^{t}$ and $\left|\mathbb{R}^{t}\right|$ is the number of data samples in set $\mathbb{R}^{t}$. In the backward phase, the parameters $\boldsymbol{A}^{t}$ are updated with SGD as

$$
\boldsymbol{A}^{t+1}=\boldsymbol{A}^{t}-\gamma^{t} \nabla_{\boldsymbol{A}} \mathcal{L}\left(\mathbb{R}^{t}, \boldsymbol{S}, \boldsymbol{A}^{t} \mid h^{t}, \boldsymbol{n}^{t}\right)
$$

where $\gamma^{t}$ is the step-size. It accounts for the effects of the communication channels by updating the parameters $\boldsymbol{H}^{t}$ with a stochastic gradient $\nabla_{\boldsymbol{A}} \mathcal{L}\left(\mathbb{R}^{t}, \boldsymbol{S}, \boldsymbol{A}^{t} \mid h^{t}, \boldsymbol{n}^{t}\right)$ at each iteration $t$. The stochasticity results from the randomness of the CSI $h^{t}$, the Gaussian noise $\boldsymbol{n}^{t}$, as well as the randomly chosen samples $\mathbb{R}^{t}$. Algorithm 1 summarizes the proposed training procedure.

AirGNN incorporates communication channel impairments into the training procedure, where each node relies on faded and noisy information from its neighbors [cf. (1)]. This matches the fading and noise distributions encountered in the decentralized implementation at the inference phase and renders the trained parameters more robust to transmission perturbations during testing; hence, yielding an improved performance and a robust

```
Algorithm 1 Training Procedure of AirGNN
    Input: training set $\mathbb{R}$, loss function $\ell$, initial parameters $\boldsymbol{A}^{0}$
    for $t=1, \ldots, T$ do
        Sample CSI $h^{t}$ and Gaussian noise $\boldsymbol{n}^{t}$
        Determine AirGNN architecture $\Phi_{\text {air }}\left(\cdot, \boldsymbol{S}, \boldsymbol{A}^{t} \mid h^{t}, \boldsymbol{n}^{t}\right)$
        Sample $\mathbb{R}^{t} \subseteq \mathbb{R}$ and compute AirGNN outputs
        $\left\{\Phi_{\mathrm{ Persistent},}\left(\boldsymbol{x}^{r}, \boldsymbol{S}, \boldsymbol{A}^{t} \mid h^{t}, \boldsymbol{n}^{t}\right)\right\}_{r=1}^{\left|\mathbb{R}^{t}\right|}$
        Compute objective $\mathcal{L}\left(\mathbb{R}^{t}, \boldsymbol{S}, \boldsymbol{A}^{t} \mid h^{t}, \boldsymbol{n}^{t}\right)$ as in (7)
        Compute stochastic gradient $\nabla_{\mathcal{A}} \mathcal{L}\left(\mathbb{R}^{t}, \boldsymbol{S}, \boldsymbol{A}^{t} \mid h^{t}, \boldsymbol{n}^{t}\right)$
        Update parameters $\boldsymbol{A}^{t}$ with step-size $\gamma^{t}$ as in (8)
    end for
```

transference for decentralized tasks. However, it remains unclear if this training procedure converges and what solution it searches for. In the next section, we conduct the convergence analysis and interpret the convergent solution.

## IV. CONVERGENCE

We begin by considering the following stochastic optimization problem as

$$
\min _{\boldsymbol{A}} \overline{\mathcal{L}}(\boldsymbol{A})=\min _{\boldsymbol{A}} \mathbb{E}_{h, n}[\mathcal{L}(\mathbb{R}, \boldsymbol{S}, \boldsymbol{A} \mid h, n)]
$$

where the expectation $\mathbb{E}_{h, n}[\cdot]$ is w.r.t. $h$ and $\boldsymbol{n}$. The standard method to solve problem (9) is the SGD, which approximates the true gradient with the gradient of some random sample and leverages the latter to update model parameters - see Algorithm 2. Theorem 1 relates the proposed training procedure to this stochastic optimization problem (9).

Theorem 1. Performing the proposed training procedure on the AirGNN model [Alg. 1] is equivalent to running SGD on the stochastic optimization problem (9) [Alg. 2].

Proof. See Appendix A.
Theorem 1 provides interpretations for the proposed training procedure, i.e., its goal is to search the solution of the stochastic optimization problem (9). Moreover, the result indicates that we can show the convergence of the proposed training procedure by proving that of the SGD on problem (9). Since AirGNN is a nonlinear parameterization, problem (9) is typically nonconvex. This motivates us to consider the convergence criterion as the gradient norm $\left\|\nabla_{\boldsymbol{A}} \overline{\mathcal{L}}(\boldsymbol{A})\right\|_{2}^{2}$, which is commonly used to quantify the first-order stationarity in the non

```
Algorithm 2 SGD for Problem (9)
    Input: training set $\mathcal{R}$, loss function $\ell$, initial parameters $\mathbf{A}_{0}$
    Set batch-size of training data $\mathcal{R}$ as $\left|\mathcal{R}_{t}\right|$ and batch-size of
    communication channels $(h, n)$ as 1
    for $t=1, \ldots, T$ do
        Sample a random objective function
        $\mathcal{L}\left(\mathcal{R}_{t}, \mathbf{S}, \mathbf{A}_{t} \mid \mathbf{h}_{t}, \boldsymbol{n}_{t}\right)[$ cf. (7)]
        Compute stochastic gradient $\nabla_{\mathbf{A}} \mathcal{L}\left(\mathcal{R}_{t}, \mathbf{S}, \mathbf{A}_{t} \mid \mathbf{h}_{t}, \boldsymbol{n}_{t}\right)$
        Update model parameters with step-size $\gamma_{t}$ as $\mathbf{A}_{t+1}=$
        $\mathbf{A}_{t}-\gamma_{t} \nabla_{\mathbf{A}} \mathcal{L}\left(\mathcal{R}_{t}, \mathbf{S}, \mathbf{A}_{t} \mid \mathbf{h}_{t}, \boldsymbol{n}_{t}\right)$
    end for
```

during training. Theorem 2 characterizes the convergence of the proposed training procedure.
Theorem 2. Consider the AirGNN operation in (5) with the training procedure in Algorithm 1 and the stochastic optimization problem (9) with the objective function satisfying Assumptions 1-2 w.r.t. $C_{\mathcal{L}}$ and $C_{g}$. Let $T$ be the total number of training iterations and $\mathbf{A}^{*}$ the global optimal solution of problem (9). Then, for any initial parameters $\mathbf{A}_{0}$ and the step-size

$$
\gamma_{t}=\gamma=\sqrt{\frac{2\left(\overline{\mathcal{L}}\left(\mathbf{A}_{0}\right)-\overline{\mathcal{L}}\left(\mathbf{A}^{*}\right)\right)}{T C_{\mathcal{L}} C_{g}^{2}}}
$$

it holds that

$$
\min _{0 \leq t \leq T-1} \mathbb{E}\left[\left\|\nabla_{\mathbf{A}} \overline{\mathcal{L}}\left(\mathbf{A}_{t}\right)\right\|_{2}^{2}\right] \leq C \sqrt{T}
$$

with $C=\sqrt{2\left(\overline{\mathcal{L}}\left(\mathbf{A}_{0}\right)-\mathcal{\mathcal { L }}\left(\mathbf{A}^{*}\right)\right) C_{\mathcal{L}} C_{g}}$ a constant.
Proof. See Appendix B.
Theorem 2 states that the proposed AirGNN training procedure minimizes the stochastic optimization problem (9) and the architecture parameters converge to a stationary solution with a rate on the order of $\mathcal{O}(1 / \sqrt{T})$. The result characterizes the convergence behavior and validates the effectiveness of the proposed training procedure. The selection of the step-size $\gamma_{t}$ in (12) depends on the total number of iterations $T$, while it is typically selected as $\gamma_{t} \propto 1 / t$ or $1 / \sqrt{t}$ in practice. It is worth mentioning that Theorem 2 guarantees local convergence because of the non-convexity, i.e., the objective function converges to a local stationary minimum rather than a global one. The latter can be improved by training the AirGNN architecture multiple times and selecting the best solution.

## V. EXPERIMENTS

We evaluate AirGNN on the decentralized tasks of source localization (Sec. V-A) and multi-robot flocking (Sec. V-B). The ADAM optimizer is used with decaying factors $\beta_{1}=0.9, \beta_{2}=$ 0.999 [26] and the results are averaged over 10 simulations.

## A. Source Localization

This experiment considers a signal diffusion process over a stochastic block model (SBM) graph, where the intra- and the inter-community edge probabilities are 0.8 and 0.2 . The graph has $n=100$ nodes uniformly divided into 10 communities and each community has a source node $s_{c}$ for $c=1, \ldots, 10$. The goal is to find the source community of a diffused signal in a decentralized manner. The initial signal is a Kronecker delta $\delta_{c} \in \mathbb{R}^{n}$ originated at one of the source nodes $\left\{s_{c}\right\}_{c=1}^{10}$ and is diffused over the graph at time $\tau$ as $x_{c, \tau}=\mathbf{S}^{\tau} \delta_{c}+\boldsymbol{n}$ with $\mathbf{S}=\mathbf{A} / \lambda_{\max }(\mathbf{A})$ and $\boldsymbol{n}$ a zero-mean Gaussian noise. The dataset consists of $1.5 \times 10^{4}$ samples with the source node $s_{c}$ and the diffusion time $\tau$ selected randomly from $\left\{s_{1}, \ldots, s_{10}\right\}$ and $\{1, \ldots, 100\}$, which are split into $10^{4}$ samples for training, $2.5 \times 10^{3}$ for validation, and $2.5 \times 10^{3}$ for testing. The AirGNN has two layers, each comprising 64 filters of order 5 and ReLU nonlinearity. We consider independent Rayleigh fading channels between the nodes with distribution scale parameter $\delta$ and the Gaussian noise with signal-to-noise ratio (SNR) 40 dB . The learning rate is set to $10^{-3}$, the batch-size to 50 , and the performance is measured in terms of the classification accuracy.

Fig. 1a shows the training procedure of the AirGNN with the scale parameter $\delta=1$. We see that the training/validation cost decreases with the iteration and approaches a stationary solution, which corroborates the convergence analysis in Theorem 2. The convergence curve fluctuates, because the channel fading effects and mini-batch sampling render the AirGNN output random. Fig. 1b depicts the performance of the AirGNN with different scale parameters $\delta$ corresponding to different channel conditions. We compare with two baselines: (i) GNN without channel fading and noise, and (ii) GNN with channel fading and noise. The first considers a classical GNN with no fading and noise, i.e., $h_{i j}^{(k)}=1$ and $n_{i}^{(k)}=0$ for $k=1, \ldots, K$ [cf. (1)], during both training and inference. This is an ideal communication scenario, which may not hold in real-world wireless applications and serves as an upper bound only for reference. The second considers fading and noise during inference, which is the practical scenario considered in this paper, but ignores them during training. The GNN without fading and noise exhibits the best performance as expected as it does not consider any channel effects. The AirGNN consistently outperforms the GNN with fading and noise. This corroborates the theoretical analysis, i.e., the AirGNN accounts for the stochasticity of the communication channels during training, which provides robustness to channel fading effects during inference. Moreover, the AirGNN maintains a good performance in different channel conditions, while the GNN suffers more degradation in severe channels when $\delta$ is small or large. The latter highlights the importance of robustness to communication noise.

## B. Multi-Robot Flocking

This experiment considers the robot swarm control over the communication graph. The goal is to learn a decentralized controller that coordinates the robots to move together and avoid collision. The network has $n=50$ robots with initial velocities sampled randomly in $[-3 \mathrm{~m} / \mathrm{s}, 3 \mathrm{~m} / \mathrm{s}]^{2}$, and robot $i$ can communicate with robot $j$ if they are within a communication radius of $r=1.5 \mathrm{~m}$. The communication graph is $\mathcal{G}=(\mathcal{V}, \mathcal{E})$ with the node set $\mathcal{V}$ as the robots and the edge set $\mathcal{E}$ as available communication links, and the graph signal $\mathbf{x}$ is the relevant features of robot positions and velocities. We use imitation learning to train the AirGNN by mimicing the optimal centralized controller [7]. The dataset consists of 450 trajectories of 100 time steps, which are split into 400 trajectories for training, 25 for validation, and 25 for testing. We consider a single

## APPENDIX

## A. Proof of Theorem 1

Proof. The objective function $\mathcal{L}(R, S, \mathbf{A} \mid \mathbf{h}, \mathbf{n})$ is determined by the AirGNN architecture, which is, in turn, determined by the channel fading $\mathbf{h}$, the Gaussian noise $\mathbf{n}$ and the data $R$. This indicates that sampling an objective function $\mathcal{L}\left(R_{t}, \mathcal{S}, \mathbf{A}_{t} \mid \mathbf{h}_{t}, \mathbf{n}_{t}\right)$ is equivalent to sampling an AirGNN architecture $\Phi^{\text {air }}\left(\cdot, \mathcal{S}, \mathbf{A} \mid \mathbf{h}_{t}, \mathbf{n}_{t}\right)$, i.e., sampling $\mathbf{h}_{t}, \mathbf{n}_{t}$ and $R_{t}$. By leveraging this observation and comparing Algorithms 1-2, steps 3-6 in the proposed training procedure [Alg. 1] is equivalent to step 4 in the SGD on problem (9) [Alg. 2]. Since the other steps are the same, we conclude that the proposed training procedure of the AirGNN is equivalent to the SGD on problem (9) with the training data batch-size $R_{t}$ and the communication channel batch-size 1 .

## B. Proof of Theorem 2

Proof. By using the Taylor expansion of $\mathbb{E}\left[\bar{L}\left(\mathbf{A}_{t+1}\right)\right]$ at $\mathbf{H}_{t}$, we can represent $\mathbb{E}\left[\bar{L}\left(\mathbf{A}_{t+1}\right)\right]$ as

$$
\begin{aligned}
\mathbb{E}\left[\bar{L}\left(\mathbf{A}_{t+1}\right)\right]=\mathbb{E} & {\left[\bar{L}\left(\mathbf{A}_{t}\right)+\nabla_{\mathbf{A}} \bar{L}\left(\mathbf{A}_{t}\right)^{\top}\left(\mathbf{A}_{t+1}-\mathbf{A}_{t}\right)\right.} \\
& \left.+\frac{1}{2}\left(\mathbf{A}_{t+1}-\mathbf{A}_{t}\right)^{\top} \nabla_{\mathbf{A}}^{2} \bar{L}\left(\tilde{\mathbf{A}}_{t}\right)\left(\mathbf{A}_{t+1}-\mathbf{A}_{t}\right)\right]
\end{aligned}
$$

where $\tilde{\mathbf{A}}_{t}$ is in the line segment joining $\mathbf{A}_{t+1}$ and $\mathbf{A}_{t}$, which truncates the expansion series at the Hessian term. From the fact that $\mathbf{v}^{\top} \mathbf{M v} \leq \lambda_{\max }(\mathbf{M})\|\mathbf{v}\|_{2}^{2}$ for any vector $\mathbf{v}$ and matrix $\mathbf{M}$ with $\lambda_{\max }(\mathbf{M})$ the maximal eigenvalue of $\mathbf{M}$ and the Lipschitz continuity $\left\|\nabla_{\mathbf{A}}^{2} \bar{L}\left(\tilde{\mathbf{A}}_{t}\right)\right\|_{2} \leq C_{L}$ of Assumption 1, we have

$$
\begin{aligned}
& \mathbb{E}\left[\bar{L}\left(\mathbf{A}_{t+1}\right)\right] \\
& \leq \mathbb{E}\left[\bar{L}\left(\mathbf{A}_{t}\right)+\nabla_{\mathbf{A}} \bar{L}\left(\mathbf{A}_{t}\right)^{\top}\left(\mathbf{A}_{t+1}-\mathbf{A}_{t}\right)+\frac{C_{L}}{2}\left\|\mathbf{A}_{t+1}-\mathbf{A}_{t}\right\|_{2}^{2}\right]
\end{aligned}
$$

Substituting the update rule of the AirGNN $\mathbf{A}_{t+1}=\mathbf{A}_{t}-$ $\gamma_{t} \nabla_{\mathbf{A}} L\left(R_{t}, \mathcal{S}, \mathbf{A}_{t} \mid \mathbf{h}_{t}, \mathbf{n}_{t}\right)$ into (15) yields

$$
\begin{aligned}
\mathbb{E} & {\left[\bar{L}\left(\mathbf{A}_{t+1}\right)\right] \leq \mathbb{E}\left[\bar{L}\left(\mathbf{A}_{t}\right)+\gamma_{t}^{2} \frac{C_{L}}{2}\right.} \\
& \left.\left\|\nabla_{\mathbf{A}} L\left(R_{t}, \mathcal{S}, \mathbf{A}_{t} \mid \mathbf{h}_{t}, \mathbf{n}_{t}\right)\right\|_{2}^{2}-\gamma_{t} \nabla_{\mathbf{A}} \bar{L}\left(\mathbf{A}_{t}\right)^{\top} \nabla_{\mathbf{A}} L\left(R_{t}, \mathcal{S}, \mathbf{A}_{t} \mid \mathbf{h}_{t}, \mathbf{n}_{t}\right)\right]
\end{aligned}
$$

By using the linearity of expectation and the identity $\mathbb{E}\left[\nabla_{\mathbf{A}} L\left(R_{t}, \mathcal{S}, \mathbf{A}_{t} \mid \mathbf{h}_{t}, \mathbf{n}_{t}\right)\right]=\mathbb{E}\left[\nabla_{\mathbf{A}} \bar{L}\left(\mathbf{A}_{t}\right)\right]$, we can re-write (16) as

$$
\begin{aligned}
& \mathbb{E}\left[\bar{L}\left(\mathbf{A}_{t+1}\right)\right] \leq \mathbb{E}\left[\bar{L}\left(\mathbf{A}_{t}\right)\right]-\gamma_{t} \mathbb{E}\left[\left\|\nabla_{\mathbf{A}} \bar{L}\left(\mathbf{A}_{t}\right)\right\|_{2}^{2}\right] \\
& +\gamma_{t}^{2} \frac{C_{L}}{2} \mathbb{E}\left[\left\|\nabla_{\mathbf{A}} L\left(R_{t}, \mathcal{S}, \mathbf{A}_{t} \mid \mathbf{h}_{t}, \mathbf{n}_{t}\right)\right\|_{2}^{2}\right]
\end{aligned}
$$

From the gradient bound of Assumption 2, we can upper bound the third term of (17) as

$$
\gamma_{t}^{2} \frac{C_{L}}{2} \mathbb{E}\left[\left\|\nabla_{\mathbf{A}} L\left(R_{t}, \mathcal{S}, \mathbf{A}_{t} \mid \mathbf{h}_{t}, \mathbf{n}_{t}\right)\right\|_{2}^{2}\right] \leq \gamma_{t}^{2} \frac{C_{L} C_{g}^{2}}{2}
$$

By substituting (18) into (17), we have

$$
\mathbb{E}\left[\left\|\nabla_{\mathbf{A}} \bar{L}\left(\mathbf{A}_{t}\right)\right\|_{2}^{2}\right] \leq \frac{1}{\gamma_{t}} \mathbb{E}\left[\bar{L}\left(\mathbf{A}_{t}\right)-\bar{L}\left(\mathbf{A}_{t+1}\right)\right]+\gamma_{t} \frac{C_{L} C_{g}^{2}}{2}
$$

Since (19) holds for all iterations $t=0, \ldots, T-1$, by considering a constant step-size $\gamma_{t}=\gamma$ and summing up (19) over all iterations, we have

$$
\begin{aligned}
& \sum_{t=0}^{T-1} \mathbb{E}\left[\left\|\nabla_{\mathbf{A}} \bar

