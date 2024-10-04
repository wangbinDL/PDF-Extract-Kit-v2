# A physics and data co-driven surrogate modeling method for high-dimensional rare event simulation 

Jianhua Xu ${ }^{\mathrm{a}}$, Ziqi Wang ${ }^{\mathrm{a}, *}$<br>${ }^{a}$ Department of Civil and Environmental Engineering, University of California, Berkeley, United States


#### Abstract

This paper presents a physics and data co-driven surrogate modeling method for efficient rare event simulation of civil and mechanical systems with high-dimensional input uncertainties. The method fuses interpretable low-fidelity physical models with data-driven error corrections. The hypothesis is that a welldesigned and well-trained simplified physical model can preserve salient features of the original model, while data-fitting techniques can fill the remaining gaps between the surrogate and original model predictions. The coupled physics-data-driven surrogate model is adaptively trained using active learning, aiming to achieve a high correlation and small bias between the surrogate and original model responses in the critical parametric region of a rare event. A final importance sampling step is introduced to correct the surrogate model-based probability estimations. Static and dynamic problems with input uncertainties modeled by random field and stochastic process are studied to demonstrate the proposed method.


Keywords: surrogate modeling, active learning, importance sampling, high-dimensional, rare event simulation, uncertainty quantification

## 1. Introduction

Uncertainty quantification (UQ) aims at quantifying and understanding the influence of ubiquitous uncertainties arising in science and engineering. Rare event simulation is a challenging branch of UQ with numerous engineering applications, such as the reliability of aerospace systems [1], resilience of critical infrastructures [2], and safety of nuclear power plants [3]. Sampling and surrogate modeling-based methods are two general approaches for rare event simulation, although other more specialized techniques exist [4-9]. Monte Carlo simulation [10,11] is typically insensitive to the dimensionality and nonlinearity of computational models. However, for rare event simulation, even the advanced variance-reduction techniques [12-19] would require thousands of samples, restricting their applications to expensive computational models.

Surrogate modeling seeks to replace the original expensive computational model with an efficient substitute. A non-intrusive data-fitting surrogate model is derived directly from training samples of the inputoutput pairs of the computational model. Examples of data-fitting surrogate models include the quadratic response surface [20, 21], polynomial chaos expansion [22-24], support vector machine [25, 26], and Gaussian process (also called Kriging) [27-32], among others. Unlike many regression models, a noise-free Gaussian

[^0]
[^0]:    *Corresponding author
    Email address: ziqiwang@berkeley.edu (Ziqi Wang)



process is an exact interpolation model, i.e., the predictions at the training points are exact. For non-training points, the Gaussian process offers estimations of prediction variability [33-35]. This feature facilitates the application of active learning, such that the training set can be adaptively enriched to reduce prediction variability for specified quantities of interest, resulting in improved accuracy and efficiency for Gaussian process-based rare event simulation [28, 29]. The active learning-based metamodeling approach can be further combined with advanced sampling techniques [30,31], or adapted to estimate probability distribution functions [32].

Despite the remarkable success of Gaussian process-based methods in various UQ applications, the model training becomes increasingly challenging, ultimately infeasible, with a growing number of input variables-a phenomenon known as the curse of dimensionality [36]. To alleviate this problem, specialized unsupervised [37-40] and supervised [41-44] dimensionality reduction techniques have been proposed to couple with Gaussian process modeling. However, the effectiveness of these techniques is problem-dependent. More critically, many real-world high-dimensional problems do not admit simple low-dimensional representations [45]. Qualitatively speaking, for a "high-dimensional input-low-dimensional output" problem, an "optimal" dimensionality reduction is the computational model itself. It follows that constructing an effective dimensionality reduction can be as challenging as finding an accurate high-dimensional surrogate model. An alternative approach is to inject domain/problem-specific prior knowledge into the surrogate modeling process. This idea is reflected in the emerging paradigms of scientific machine learning [46-49] and multi-fidelity UQ [50-52], enabling them to handle high-dimensional problems.

In this paper, we leverage physics-based surrogate modeling to solve high-dimensional rare event estimation problems. This idea is under the broad umbrella of multi-fidelity UQ. A physics-based surrogate model can be adapted from the original high-fidelity model in various ad hoc ways, such as domain-specific simplifications [53-55], reduced-order modelings [56-58], and relaxations of numerical solvers [50]. In this study, we address static and dynamic problems with a random field/process as input, typically discretized by 1,000 random variables. We construct physics-based surrogate models equipped with the properties of (i) parsimonious: the surrogate model is parameterized by a few tunable control parameters, and (ii) compatible with high-dimensional input uncertainties: the surrogate model can accept high-dimensional input uncertainties either directly as input of the model or indirectly through filtering and coarse-graining operations. For example, the classic equivalent linearization method $[59,60]$ for nonlinear random vibration analysis involves constructing linear physical models with random processes as input and output. Therefore, the equivalent linearization method can be reformulated into a physics-based surrogate modeling approach for nonlinear random vibration problems [61]. In other engineering applications such as computational fluid dynamics [53], aerodynamic design [54], and climate modeling [55], there exist various domain-specific approaches in constructing simplified physics-based models.

Physics-based surrogate models may have inherent errors due to simplifications; therefore, it is promising to introduce a data-driven error correction to fill the gap between the surrogate and original model predictions. This idea has been investigated recently in [62,63], where an active learning-based Gaussian process is trained to correct the low-fidelity model predictions. Inspired by the success of existing works, this study is devoted to low probability estimations with high-dimensional input uncertainties. Different from existing works [62, 63], we construct the data-driven error correction as a function of the output of the physics-based surrogate model, thereby mitigating the curse of dimensionality associated with high-dimensional input



uncertainties. Three critical ingredients-parametric optimization for physics-based surrogate models, heteroscedastic Gaussian process for error corrections, and active learning for effective training-are leveraged to construct and train coupled physics-data-driven surrogate models. Finally, one can apply an importance sampling to couple the surrogate model simulations with limited evaluations of the original model, known as multi-fidelity importance sampling [51, 52]. The common practice of multi-fidelity importance sampling uses parametric distribution models such as the Gaussian mixture as the importance density, which scales poorly with dimensionality [14]. In this work, we adopt an importance sampling formulation [61] tailored to high-dimensional rare event simulations.

This paper is organized as follows. Section 2 introduces the general formulation of the coupled physicsdata-driven surrogate model. Section 3 develops a training process for the surrogate model, including optimization of parametric physical models, error corrections using an heteroscedastic Gaussian process, and adaptive training by active learning. Section 4 introduces an importance sampling scheme to correct the surrogate model-based probability estimations. Section 5 demonstrates the performance of the proposed method for high-dimensional rare event simulation problems. Section 6 discusses limitations. Section 7 provides concluding remarks. The implementation details are provided in Appendix A.

# 2. Coupled physics-data-driven surrogate model 

Consider an end-to-end computational model $M: \boldsymbol{x} \in \mathbb{R}^{n} \mapsto y \in \mathbb{R}$ that maps a $n$-dimensional input $\boldsymbol{x}$ into a 1-dimensional output $y$. The input $\boldsymbol{x}$ is an outcome of a random vector $X$ defined in the probability space $\left(\mathbb{R}^{n}, \mathscr{B}^{n}, \mathbb{P}_{X}\right)$, where $\mathscr{B}^{n}$ is the Borel $\sigma$-algebra on $\mathbb{R}^{n}$, and $\mathbb{P}_{X}$ is the probability measure of $X$ with the distribution function $f_{X}$. The output $y$ is a performance variable such that it defines the rare event of interest through $\{y \leq 0\}$, without loss of generality. Since the source of randomness is from $X$, the rare event probability is typically formulated in the space of $X$, expressed by $\mathbb{P}_{X}(M(X) \leq 0)$. This problem is challenging in real-world applications, because (i) the dimension of $\boldsymbol{x}$ is high, (ii) the computational model $M$ involves expensive physics-based simulations, and (iii) the probability to be estimated is small. To reduce the computational cost of $M$, we construct a simplified (end-to-end) computational model expressed by:

$$
\begin{aligned}
y_{p} & =\left(M_{p} \circ \psi\right)(\boldsymbol{x} ; \boldsymbol{\theta}_{p}) \\
M_{p}: \boldsymbol{x}^{\prime} & \in \mathbb{R}^{n^{\prime}} \mapsto y_{p} \in \mathbb{R}, \quad \boldsymbol{x} \in \mathbb{R}^{n} \mapsto \boldsymbol{x}^{\prime} \in \mathbb{R}^{n^{\prime}}, n^{\prime} \leq n
\end{aligned}
$$

where $M_{p}$ represents a cheaper physics-based model derived from the original model $M, \psi$ is a filtering or coarse-graining function of the input $\boldsymbol{x}$, " $\circ$ " denotes function composition, and $\boldsymbol{\theta}_{p}$ are tunable parameters of $M_{p}$ and/or $\psi$. Depending on the selection of $M_{p}$, the filtering function $\psi$ can be a trivial identity mapping if $M_{p}$ and $M$ share the same input space, or it can be a dimensionality reduction mapping if $M_{p}$ is defined on a coarser/different input space. However, it is important to notice that $M_{p} \circ \psi$ and $M$ share the same source of randomness from $X$, enabling a tuning of $M_{p} \circ \psi$ (via adjusting $\boldsymbol{\theta}_{p}$ ) to maximize the statistical correlation between $Y$ and $Y_{p}$.

To improve the accuracy of Eq. (1), a data-driven error correction can be introduced, leading to a coupled physics-data-driven surrogate model expressed by:

$$
\hat{y}=y_{p}+\epsilon\left(y_{p} ; \boldsymbol{\theta}_{\epsilon}\right)=\left(M_{p} \circ \psi\right)\left(\boldsymbol{x} ; \boldsymbol{\theta}_{p}\right)+\left(\epsilon \circ M_{p} \circ \psi\right)\left(\boldsymbol{x} ; \boldsymbol{\theta}_{p}, \boldsymbol{\theta}_{\epsilon}\right)
$$



where $\epsilon: y^{p} \in \mathbb{R} \mapsto \varepsilon \in \mathbb{R}$ is the error correction function constructed using data-fitting methods, and $\theta_{\epsilon}$ are parameters of the data-fitting model. It is worth highlighting that the input of the error correction function is the output of the physics-based surrogate model. This construction is different from existing works [62, 63], where the error correction term was constructed on the product space of $x$ and $x^{\prime}$. The methodology of $[62,63]$ may face difficulties for problems with high-dimensional input uncertainties, due to the weak scalability of conventional data-fitting methods such as Gaussian process and polynomial regression [36]. In comparison, our construction of the surrogate model can mitigate the curse of dimensionality. However, it comes with a price of having inherent noises in the error correction term, even at the training points of $y^{p}$. This is because the mapping from $y^{p}$ to $y$ can be one-to-many. An intuitive restatement is that the physicsbased surrogate model cannot capture all details of the original model. To quantify and mitigate the impact of the inherent noises, we use the heteroscedastic Gaussian process [64-66] to model $\epsilon\left(y^{p}\right)$. This differs from the noise-free and homoscedastic Gaussian process models, as the heteroscedastic Gaussian process model no longer performs exact interpolations and the noise is input-dependent.



Figure 1: Physics and data co-driven surrogate modeling for rare event simulation. The physics-based surrogate model $y^{p}=M_{p}\left(x^{\prime} ; \theta_{p}\right)$ contains tunable control parameters $\theta_{p}$ to be optimized in the training process. The error correction function $\epsilon\left(y^{p}\right)$ is modeled in the space of $y^{p}$ by heteroscedastic Gaussian process to account for input-dependent noises. The active learning adaptively enriches the training set with a learning criterion to highlight contributions from the rare event. The importance sampling estimates the correction factor $c_{\mathcal{P}}$ to improve the probability estimation from the surrogate model.

Figure 1 presents a schematic of the proposed surrogate modeling method for rare event simulation. The technical details for optimizing the physics-based surrogate and error correction models are introduced in Sections 3.1 and 3.2, respectively. The active learning approach for efficient surrogate model training



is described in Section 3.3. Section 4 details the importance sampling method for rare event probability estimations.

# 3. Training of the coupled physics-data-driven surrogate model 

### 3.1. Optimization of parametric physical models

In physics-based surrogate modeling, the response predictions of the surrogate model can be inaccurate but still be mildly/highly correlated with that of the original model. The statistical correlation between the surrogate and original model responses has a decisive impact on the noise of the error correction term (see Figure 2 for a simple illustration)-higher correlation indicates smaller noise. Pearson, Spearman's Rank, and Kendall's Tau correlation coefficients are popular indices for quantifying the correlation between two random variables [67]. The Pearson correlation coefficient can only reflect the linear correlation, while the Spearman's Rank and Kendall's Tau correlation coefficients can handle the nonlinear dependency. In our context, the physics-based surrogate model, by construction, is a simplification of the original model. Thus, a mildly nonlinear correlation is expected. Consequently, the Pearson correlation coefficient is sufficient. The Spearman's Rank and Kendall's Tau correlation coefficients can be readily implemented into the proposed surrogate modeling method, but we did not observe an improvement in performance for the numerical examples we have studied. It is worth mentioning that mutual information $[68,69]$ is a more general metric for measuring dependency between two random variables, but the sample estimate of mutual information involves additional assumptions on the joint distributions.



Figure 2: Impact of the correlation between surrogate and original model responses on the noise of the error correction function. For illustration, $Y$ and $Y_{p}$ are assumed to be lognormal with a Pearson correlation coefficient varying among $\rho=0.895,0.946,0.987$, and 0.998 . It is seen that the noise in the error $\epsilon=y-y_{p}$ decreases with the increase of the correlation coefficient. It is also clear that an exact interpolation model should be avoided when $\epsilon$ is noisy.

Because rare event probabilities are dominated by conditional distributions, the correlation between $Y$ and $Y_{p}$ generated by $\boldsymbol{X} \sim f_{\boldsymbol{X}}(\boldsymbol{x})$ may not be an ideal objective for optimizing the surrogate model. The issue is that limited samples from $f_{\boldsymbol{X}}(\boldsymbol{x})$ are unlikely to fall near to the boundary of the rare event, where most of the misclassifications happen. In this work, we adopt active learning to adaptively enrich the training set $\mathcal{D}=\left\{\left(\boldsymbol{x}^{i}, M\left(\boldsymbol{x}^{(i)}\right)\right)\right\}$ toward the critical region around $\{M(\boldsymbol{x})=0\}$. Using the training set $\mathcal{D}$, the sample correlation coefficient emphasizes the contribution from the rare event. This is essentially equivalent to



redefining the correlation between $M(\boldsymbol{X})$ and $\left(M_{p} \circ \psi\right)(\boldsymbol{X})$ using an active learning-controlled importance sampling distribution rather than the original $f_{\boldsymbol{X}}(\boldsymbol{x})$. To summarize, the optimization for the physics-based surrogate model $\left(M_{p} \circ \psi\right)\left(\boldsymbol{x} ; \boldsymbol{\theta}_{p}\right)$ is formulated as:

$$
\begin{aligned}
& \boldsymbol{\theta}_{p}^{*}=\arg \max _{\theta_{p}} \rho_{Y Y_{p}}\left(\boldsymbol{\theta}_{p} \mid \mathcal{D}\right) \\
& =\arg \max _{\boldsymbol{\theta}_{p}} \frac{\left\langle\left(M(\boldsymbol{X})-\left\langle\left.M(\boldsymbol{X})\right\rangle_{\mathcal{D}}\right) \left\langle\left.\left(M_{p} \circ \psi\right)(\boldsymbol{X} ; \boldsymbol{\theta}_{p})-\left\langle\left(M_{p} \circ \psi\right)(\boldsymbol{X} ; \boldsymbol{\theta}_{p})\right\rangle_{\mathcal{D}}\right)_{\mathcal{D}}\right\rangle_{\mathcal{D}}\right.}{\sqrt{\left\langle\left(M(\boldsymbol{X})-\left\langle M(\boldsymbol{X})\right\rangle_{\mathcal{D}}\right)^{2}\right\rangle_{\mathcal{D}}}}\left\langle\left(\left(M_{p} \circ \psi\right)\left(X ; \boldsymbol{\theta}_{p}\right)-\left\langle\left(M_{p} \circ \psi\right)\left(X ; \boldsymbol{\theta}_{p}\right)\right\rangle_{\mathcal{D}}\right)^{2}\right\rangle_{\mathcal{D}}
\end{aligned}
$$

where $\langle\cdot\rangle$ denotes sample mean.
Before solving Eq. (3), we need to design $\boldsymbol{\theta}_{p}$ for the physics-based surrogate model, i.e., determine which parameters are tunable. For specific applications, engineering judgement can be used to design $\boldsymbol{\theta}_{p}$. A more objective approach is to adopt a parsimonious principle to select a minimum number of parameters that can achieve a relatively high $\max _{\theta_{p}} \rho_{Y Y_{p}}\left(\boldsymbol{\theta}_{p} \mid \mathcal{D}\right)$. This principle can be materialized as an incremental approach to start with a single tunable parameter and iteratively augment if $\max _{\theta_{p}} \rho_{Y Y_{p}}\left(\theta_{p} \mid \mathcal{D}\right)$ can be significantly improved. In the simulation test cases of civil and mechanical systems, we have investigated the use of elastic modulus, damping ratio, stiffness, and yield displacement as tunable parameters, where $\max _{\theta_{p}} \rho_{Y Y_{p}}\left(\theta_{p} \mid \mathcal{D}\right)$ can typically achieve 0.95 .

Finally, the optimization in Eq. (3) can be solved by gradient-free metaheuristic algorithms [70]. Provided with a training set $\mathcal{D}$, solving Eq. (3) does not involve additional simulations of the original model, but it requires simulations of the physics-based surrogate model. If $\mathcal{D}$ is enriched by active learning, Eq. (3) needs to be re-solved; the solution from the previous training set can be used as a warm initial guess.

# 3.2. Error corrections using heteroscedastic Gaussian process 

Given a training set $\mathcal{D}=\left\{\left(\boldsymbol{x}^{i}, M\left(\boldsymbol{x}^{(i)}\right)\right)\right\}$ and the solution of Eq. (3), we obtain the training set for the error correction, $\mathcal{D}_{\epsilon}=\left\{\left(y_{p}^{(i)}, \varepsilon^{(i)}\right)\right\}$, where $y_{p}^{(i)}=\left(M_{p} \circ \psi\right)\left(\boldsymbol{x}^{(i)} ; \boldsymbol{\theta}_{p}^{*}\right)$ and $\varepsilon^{(i)}=M\left(\boldsymbol{x}^{(i)}\right)-\left(M_{p} \circ \psi\right)\left(\boldsymbol{x}^{(i)} ; \boldsymbol{\theta}_{p}^{*}\right)$.

Using $\mathcal{D}_{\epsilon}$, we train a heteroscedastic Gaussian process: [64-66] to model $\epsilon\left(y_{p}\right)$, expressed by:

$$
\epsilon\left(y_{p} ; \boldsymbol{\theta}_{\epsilon}\right)=f\left(y_{p} ; \boldsymbol{\theta}_{f}\right)+\tau\left(y_{p} ; \boldsymbol{\theta}_{\tau}\right)
$$

where $\boldsymbol{\theta}_{\epsilon}=\boldsymbol{\theta}_{f} \cup \boldsymbol{\theta}_{\tau}, f\left(y_{p}\right) \sim \mathcal{G} \mathcal{P}\left(\mu_{f}\left(y_{p}\right), k_{f}\left(y_{p}, y_{p}^{\prime}\right) ; \boldsymbol{\theta}_{f}\right)$ is a Gaussian process with hyperparameters $\theta_{f}$ to model the mean $\mu_{f}\left(y_{p}\right)$ and kernel $k_{f}\left(y_{p}, y_{p}^{\prime}\right), \tau\left(y_{p}\right) \sim \mathcal{N}\left(0, \exp \left(g\left(y_{p}\right)\right)\right)$ is an input-dependent Gaussian noise with zero mean and variance $\exp \left(g\left(y_{p}\right)\right)$, and $g\left(y_{p}\right) \sim \mathcal{G} \mathcal{P}\left(\mu_{g}, k_{g}\left(y_{p}, y_{p}^{\prime}\right) ; \boldsymbol{\theta}_{g}\right)$ is another Gaussian process with hyperparameters $\boldsymbol{\theta}_{g}$ to model the mean $\mu_{g}$ and kernel $k_{g}\left(y_{p}, y_{p}^{\prime}\right)$.

The introduction of the heteroscedastic Gaussian noise is essential in this study because the mapping from $y_{p}$ to $y$ can be one-to-many. The use of heteroscedastic Gaussian process comes with a price of increasing the number of hyperparameters, and the analytical marginal likelihood and prediction equations for the homoscedastic Gaussian process are no longer useful [64-66]. The hyperparameters $\theta_{f}$ and $\boldsymbol{\theta}_{g}$ can be approximated by maximizing the following lower bound of the exact marginal likelihood [64]:

$$
\mathcal{F}(\boldsymbol{\mu}, \boldsymbol{\Sigma})=\log f_{\mathcal{N}}\left(\boldsymbol{\varepsilon} ; \mathbf{0}, \mathbf{K}_{f}+\mathbf{R}\right)-\frac{1}{4} \operatorname{tr}(\boldsymbol{\Sigma})-\mathrm{KL}\left(f_{\mathcal{N}}(\mathbf{g} ; \boldsymbol{\mu}, \boldsymbol{\Sigma}) \| f_{\mathcal{N}}\left(\mathbf{g} ; \boldsymbol{\mu}_{g} \mathbf{1}, \mathbf{K}_{g}\right)\right)
$$

where $\boldsymbol{\mu}$ and $\boldsymbol{\Sigma}$ are the variational mean vector and covariance matrix to be determined alongside with the hyperparameters $\boldsymbol{\theta}_{f}$ and $\boldsymbol{\theta}_{g} ; \boldsymbol{\varepsilon}=\left[\varepsilon^{(1)}, \varepsilon^{(2)}, \ldots\right]^{\top}$ are from the training set $\mathcal{D}_{\epsilon} ; \mathbf{0}$ and $\mathbf{1}$ are vectors of zeros and



ones; $\mathbf{K}_{f}$ and $\mathbf{K}_{g}$ are respectively the covariance matrices of the Gaussian processes $f\left(\mathbf{y}_{p}\right)$ and $g\left(\mathbf{y}_{p}\right) ; \mathbf{R}$ is a diagonal matrix with diagonal entries $\mathbf{R}_{i i}=\exp \left(\mu_{i}-\boldsymbol{\Sigma}_{i i} / 2\right) ; f_{N}$ denotes the probability density function of a multivariate Gaussian distribution; $\operatorname{tr}(\cdot)$ denotes matrix trace; and $\mathcal{K}_{L}(\cdot \| \cdot)$ denotes the Kullback-Leibler divergence between two probability density functions.

Once the hyperparameters $\boldsymbol{\theta}_{f}$ and $\boldsymbol{\theta}_{g}$ are estimated, the predictions for the mean and variance of $\boldsymbol{\epsilon}\left(\mathbf{y}_{p}^{*}\right)$ at $\mathbf{y}_{p}^{*}$ are obtained from $[64]$ :

$$
\boldsymbol{\mu}_{\boldsymbol{\epsilon}}\left(\mathbf{y}_{p}^{*}\right)=\mathbf{k}_{f *}{ }^{\top}\left(\mathbf{K}_{f}+\mathbf{R}\right)^{-1} \boldsymbol{\varepsilon}
$$

and



respectively, where $\mathbf{k}_{f * *}=\mathbf{k}_{f}\left(\mathbf{y}_{p}^{*}, \mathbf{y}_{p}^{*}\right), \mathbf{k}_{g * *}=\mathbf{k}_{g}\left(\mathbf{y}_{p}^{*}, \mathbf{y}_{p}^{*}\right), \mathbf{k}_{f *}=\left[\mathbf{k}_{f}\left(\mathbf{y}_{p}^{(1)}, \mathbf{y}_{p}^{*}\right), \mathbf{k}_{f}\left(\mathbf{y}_{p}^{(2)}, \mathbf{y}_{p}^{*}\right), \ldots\right]^{\top}$ and $\mathbf{k}_{g *}=\left[\mathbf{k}_{g}\left(\mathbf{y}_{p}^{(1)}, \mathbf{y}_{p}^{*}\right), \mathbf{k}_{g}\left(\mathbf{y}_{p}^{(2)}, \mathbf{y}_{p}^{*}\right), \ldots\right]^{\top}, \mathbf{I}$ is the identity matrix, and $\boldsymbol{\Lambda}$ is a positive semi-definite diagonal matrix introduced to re-parameterize $\boldsymbol{\mu}$ and $\boldsymbol{\Sigma}$ in a reduced order.

The mean $\boldsymbol{\mu}_{\boldsymbol{\epsilon}}\left(\mathbf{y}_{p}^{*}\right)$ can be used as the prediction of the surrogate modeling error at $\mathbf{y}_{p}^{*}$, and $\sigma_{\boldsymbol{\epsilon}}^{2}\left(\mathbf{y}_{p}^{*}\right)$ quantifies the uncertainty of this prediction. The latter quantity is desirable in active learning. It is worth noting that the roles of the heteroscedastic Gaussian process involve quantifying the noise and correcting the (mean) predictions of the physics-based surrogate model (see Figure 3); it cannot reduce the noise.



Figure 3: Heteroscedastic Gaussian process for error correction. Following Figure 2, for $\rho=0.946$, a heteroscedastic Gaussian process is trained to fit the error. It is seen that the heteroscedastic errors are well-captured, and the heteroscedastic Gaussian process corrects the surrogate model predictions. The mean absolute relative errors between the surrogate model predictions and the true responses, before and after error correction, are $12.19 \%$ and $7.08 \%$, respectively.

# 3.3. Adaptive training by active learning 

Given an initial training set $\mathbf{D}=\left\{\left(\mathbf{x}^{(i)}, M\left(\mathbf{x}^{(i)}\right)\right)\right\}_{i=1}^{N_{0}} \equiv \mathbf{D}_{x} \times \mathbf{D}_{y}$, we sequentially train the physics-based surrogate model $\mathbf{y}_{p}=\left(M_{p} \circ \psi\right)\left(\mathbf{x} ; \boldsymbol{\theta}_{p}\right)$ and the error correction function $\boldsymbol{\epsilon}\left(\mathbf{y}_{p} ; \boldsymbol{\theta}_{\boldsymbol{\epsilon}}\right)$ to obtain the initial surrogate model $\hat{\mathbf{y}}=\left(M_{p} \circ \psi\right)\left(\mathrm{x} ; \boldsymbol{\theta}_{p}\right)+\boldsymbol{\epsilon}\left(\mathbf{y}_{p} ; \boldsymbol{\theta}_{\boldsymbol{\epsilon}}\right)$. Subsequently, we initiate an active learning process to iteratively enrich the training set $\mathbf{D}$ and update the surrogate model. Hereafter, we develop an active learning process tailored to the physics-data-driven surrogate modeling.

Provided with the current surrogate model, we first define a critical learning region $\Omega_{c}$ as:

$$
\Omega_{c}=\left\{\mathbf{x} \in \mathbb{R}^{n}: \frac{\left|\mathbf{y}_{p}+\boldsymbol{\mu}_{\epsilon}\left(\mathbf{y}_{p}\right)\right|}{\sigma_{\epsilon}\left(\mathbf{y}_{p}\right)} \leqslant \delta, \mathbf{y}_{p}=\left(M_{p} \circ \psi\right)\left(\mathbf{x} ; \boldsymbol{\theta}_{p}\right)\right\}
$$



where $\delta>0$ is a cutoff value for the learning region, and $\mu_{\epsilon}\left(y_{p}\right)$ and $\sigma_{\epsilon}\left(y_{p}\right)$ are respectively the mean and standard deviation of the Gaussian process error correction at $y_{p}$.

Next, we generate a candidate training set $\mathbb{X}_{\mathrm{c}}=\left\{x^{(i)}\right\}_{i=1}^{N}$ through:

$$
X^{(i)} \sim I_{\Omega_{\mathrm{c}}}(x) f_{\mathbb{X}}(x)
$$

where $I_{\Omega_{\mathrm{c}}}: \mathbb{R}^{n} \mapsto\{0,1\}$ is an indicator function for $\left\{x \in \Omega_{\mathrm{c}}\right\}$ and the normalizing constant for the density $I_{\Omega_{\mathrm{c}}}(x) f_{\mathbb{X}}(x)$ is omitted for simplicity. To reduce surrogate model simulations and improve the scalability toward low probability estimations, the sequential Monte Carlo [17-19] is used to generate $\mathbb{X}_{\mathrm{c}}$.

Given $\mathbb{X}_{\mathrm{c}}$, the next training point $x^{*}$ is identified by:

$$
x^{*}=\underset{x \in \mathbb{X}_{c}}{\arg \max }\left(\min _{y_{p}^{\prime} \in Y_{p}}\left\|y_{p}-y_{p}^{\prime}\right\|\right), y_{p}=\left(M_{p} \circ \psi\right)(x ; \theta_{p})
$$

where $Y_{p}=\left\{y_{p}=\left(M_{p} \circ \psi\right)\left(x ; \theta_{p}\right): x \in \mathbb{D}_{x}\right\}$ is a set of $y_{p}$ predictions from existing training samples. This equation picks the point in $\mathbb{X}_{\mathrm{c}}$ that differs (in terms of $y_{p}$ ) the most from the existing training points, aiming to achieve sparsely distributed training points in the space of $y_{p}$. This learning criterion is a relaxation of the classic $U$-function-based learning [29] through introducing additional, seemingly redundant, distance-based selection to enforce sparsity. This relaxation is necessary because the prediction uncertainty term $\sigma_{\epsilon}\left(y_{p}\right)$ of the $U$-function, which influences the "sparsity" of the $U$-function-based training point selection, is not only affected by the distance to existing training points, but also contributed, sometimes dominantly, by the inherent noise of the surrogate model. In the conventional application [29-31] of active learning-based Gaussian process modeling, the training data does not have inherent stochastic noise, and the distancebased selection in Eq. (10) can be unnecessary. Incidentally, the constructions of Eq. (8) and Eq. (9) are still meaningful even for noise-free scenarios, because they facilitate the use of efficient sampling methods to identify the low-probability critical region to propose training points.

Provided with the next training point $x^{*}$, the original model is simulated to obtain $y^{*}=M\left(x^{*}\right)$, the training set $\mathbb{D}$ is augmented to include $\left(x^{*}, y^{*}\right)$, and the surrogate model is updated. The learning process is stopped if the mean prediction is stable and/or the prediction uncertainty is small [71, 72]. In our context, the inherent noise originated from the imperfection of the physics-based surrogate model cannot be reduced through training. Additionally, the magnitude of this inherent noise varies with the problem. Thus, the conventional prediction uncertainty-based stopping criterion is not suitable. To address this, we adopt a stopping criterion that monitors the stability of prediction uncertainty, expressed as follows:

$$
\frac{\left|\hat{P}_{\Delta}^{(m+1)}-\hat{P}_{\Delta}^{(m)}\right|}{\hat{P}_{\Delta}^{(m+1)}} \leqslant \eta, m=0,1, \ldots
$$

where $\hat{P}_{\Delta}^{(m)}=\hat{P}^{+}-\hat{P}^{-}$measures the prediction uncertainty, and $\hat{P}^{+}$and $\hat{P}^{-}$are respectively the upperand lower- confidence limits of the rare event probability at the $m$-th learning step, estimated from the surrogate models $y_{p}+\mu_{\epsilon}\left(y_{p}\right)-\sigma_{\epsilon}\left(y_{p}\right)$ and $y_{p}+\mu_{\epsilon}\left(y_{p}\right)+\sigma_{\epsilon}\left(y_{p}\right)$, respectively. The mechanism of the stopping criterion is that the epistemic uncertainty from insufficient training is minimized when $\hat{P}_{\Delta}^{(m)}$ is stabilized; the remaining component of $\hat{P}_{\Delta}^{(m)}$ is the aleatory uncertainty that cannot be reduced by training, unless another physics-based surrogate model is used.

The implementation details for the training of the coupled physics-data-driven surrogate model are presented in Appendix A.19. Due to the presence of inherent noises, there is no guarantee that the probability



prediction from the surrogate model will converge to the true value. To address this issue, a final importance sampling step will be introduced in the following section.

# 4. Importance sampling using the coupled physics-data-driven surrogate model 

The target rare event probability can be formulated as

$$
P=\int_{\mathbf{x} \in \mathbb{R}^{n}} I_{\leq 0}(M(\mathbf{x})) f_{\mathbf{X}}(\mathbf{x}) \mathrm{d} \mathbf{x}
$$

The importance sampling rewrites the integral in Eq. (12) by introducing an importance density $h(\mathbf{x})$, i.e.,

$$
P=\int_{\mathbf{x} \in \mathbb{R}^{n}} I_{\leq 0}(M(\mathbf{x})) \frac{f_{\mathbf{X}}(\mathbf{x})}{h(\mathbf{x})} h(\mathbf{x}) \mathrm{d} \mathbf{x}
$$

The support of the importance density $h(\mathbf{x})$ should cover the rare event, and the optimal importance density is $[10]$

$$
h^{*}(\mathbf{x})=I_{\leq 0}(M(\mathbf{x})) \frac{f_{\mathbf{X}}(\mathbf{x})}{P}
$$

Due to the high correlation between the original and surrogate model responses, it is tempting to use the following importance density from the surrogate model as an approximation for the optimal density.

$$
\hat{h}(\mathbf{x})=\frac{I_{\leq 0}\left(\hat{M}\left(\mathbf{x} ; \theta^{p}, \theta^{\epsilon}\right)\right)}{\hat{P}}
$$

where $\hat{M}\left(\mathbf{x} ; \theta^{p}, \theta^{\epsilon}\right) \equiv\left(M^{p} \circ \psi\right)\left(\mathbf{x} ; \theta^{p}\right)+\mu^{\epsilon}\left(\left(M^{p} \circ \boldsymbol{\psi}\right)\left(\mathbf{x} ; \theta^{p}\right) ; \theta^{\epsilon}\right)$ is the integrated surrogate model, and $\hat{P}$ is its rare event probability. However, there is no guarantee that the target rare event is an improper subset of the support of $\hat{h}(\mathbf{x})$. Therefore, $\hat{h}(\mathbf{x})$ cannot be directly employed as an importance density. One remedy is to replace the binary indicator function in Eq. (15) by a smooth approximation [17, 61], so that $\hat{h}(\mathbf{x})$ becomes nonzero everywhere. This approach requires the tuning of a relaxation parameter associated with the smooth approximation of the indicator function.

An alternative remedy, which is adopted in this paper, is to use the following identity derived from properties of conditional probability $[61]:$

$$
P=c_{P} \cdot \hat{P} \equiv \frac{\int_{\mathbf{x} \in \mathbb{R}^{n}} I_{\leq 0}(M(\mathbf{x})) \hat{h}(\mathbf{x}) \mathrm{d} \mathbf{x}}{\int_{\mathbf{x} \in \mathbb{R}^{n}} I_{\leq 0}\left(\hat{M}\left(\mathbf{x} ; \theta^{p}, \theta^{\epsilon}\right)\right) h^{*}(\mathbf{x}) \mathrm{d} \mathbf{x}} \hat{P}
$$

where $c_{P}$ is the correction factor for the surrogate model-based rare event probability estimation. The numerator represents the conditional probability of the original rare event given the surrogate rare event, while the denominator represents the conditional probability of the surrogate rare event given the original rare event. Ideally, the correction factor $c_{P}$ should be close to 1 ; therefore, $c_{P}$ can be used as a performance measure of the surrogate model. The conditional probabilities in Eq. (16) can be estimated by Monte Carlo simulation with Markov Chain Monte Carlo algorithms [73,74] to generate samples from $h^{*}(\mathbf{x})$ and $\hat{h}(\mathbf{x})$. For a well-trained surrogate model, the overlap between $h^{*}(\mathbf{x})$ and $\hat{h}(\mathbf{x})$ is expected to be significant; consequently, the computational cost to estimate $c_{P}$ would be small. However, theoretically speaking, Eq. (16) implies that the surrogate model solution $\hat{P}$ can be highly accurate even when the surrogate rare



event does not largely overlap with the actual rare event; this is illustrated by Figure 4. Finally, the implementation details of the importance sampling using Eq. (16) are presented in Appendix A.20.



Figure 4: Importance sampling for the coupled physics-data-driven surrogate model. The true rare event from the original model is $\mathcal{E}_{1} \cup \mathcal{E}_{3}$, and the "surrogate" rare event from the surrogate model is $\mathcal{E}_{2} \cup \mathcal{E}_{3}$. Eq. (16) is derived from the identity $P\left(\mathcal{E}_{1} \cup \mathcal{E}_{3}\right)=P\left(\mathcal{E}_{2} \cup \mathcal{E}_{3}\right) \frac{P\left(\mathcal{E}_{3}\right) / P\left(\mathcal{E}_{2} \cup \mathcal{E}_{3}\right)}{P\left(\mathcal{E}_{3}\right) / P\left(\mathcal{E}_{1} \cup \mathcal{E}_{3}\right)}$. It follows that if $P\left(\mathcal{E}_{1}\right)=P\left(\mathcal{E}_{2}\right), \mathcal{P}=\hat{\mathcal{P}}$, i.e., $\hat{\mathcal{P}}$ can be accurate even when the overlap $\mathcal{E}_{3}$ is not significant. This condition can be met if $\hat{Y}$ is an unbiased estimator of $Y$ for the region $\mathcal{E}_{1} \cup \mathcal{E}_{2} \cup \mathcal{E}_{3}$, supporting the proposed approach of training a Gaussian process to correct the bias in the critical region identified by active learning.

# 5. Numerical examples 

In this section, we will investigate (1) a static problem of a linear elastic cantilever beam with material properties modeled by a Gaussian random field, (2) a dynamic problem of a nonlinear viscous damper under white noise excitation, and (3) a dynamic problem of a multi-degree-of-freedom hysteretic system under white noise excitation. Three schemes are investigated to construct physics-based surrogate models. Specifically, homogenization of material properties is considered in the first example, statistical linearization is used in the second example, and relaxation of the numerical solver is adopted in the third example.

### 5.1. Example 1: A linear elastic cantilever beam

Consider a linear elastic cantilever beam of length 5 m and width 2 m subjected to 20 evenly spaced concentrated loads on the upper edge with magnitudes $Q=500 \mathrm{kN}$, shown in Figure 5. The Poisson ratio of the beam is $\nu=0.3$. The reference/original computational model is represented by a discretization of the beam into $50 \times 20=1000$ four-node quadrilateral elements, and the elastic modulus of the beam is characterized by a homogeneous random field $E(x, y)$ with a discretization of 1000 Gaussian random variables compatible with the spatial discretization. The autocorrelation function of the Gaussian random field is modeled by the isotropic exponential model $R_{E}(\Delta x, \Delta y)=\exp \left(-\sqrt{\Delta_{x}^{2}+\Delta_{y}^{2}} / l\right)$ with the correlation length $l=10 \mathrm{~m}$. The mean value and standard deviation of the marginal Gaussian distribution are $\mu_{E}=200 \mathrm{GPa}$ and



$\sigma_{E}=30 \mathrm{GPa}$, respectively. The physics-based surrogate model is constructed via a simple homogenization of the random field of the elastic modulus:

$$
E_{p}=a_{E} \bar{E}+b_{E}
$$

where $\left\{a_{E}, b_{E}\right\}=\theta_{p}$ are tunable parameters of the physics-based surrogate model, and $\bar{E}$ represents the average of the 1000 Gaussian random variables. The initial values of $a_{E}$ and $b_{E}$ are set to be 1 and 0 , respectively. The rare event of interest is defined as the vertical displacement of point $A$ exceeds a prescribed threshold of 0.0032 m , expressed by

$$
\left\{y=0.0032-d_{A} \leq 0\right\}
$$

where $d_{A}$ is the vertical displacement of point A .



Figure 5: Physics-based surrogate model of a linear elastic cantilever beam. (a) original model: the spatial domain of the beam is discretized into $50 \times 20=1000$ four-node quadrilateral elements. The elastic modulus of the beam is characterized by a homogeneous random field $E(x, y)$ with a discretization of 1000 Gaussian random variables compatible with the spatial discretization; (b) physics-based surrogate model: the whole beam is represented by a single four-node quadrilateral element. The elastic modulus is assumed to be a homogenization of the random field, i.e., $E_{p}=a_{E} \bar{E}+b_{E}$, where $a_{E}$ and $b_{E}$ are tunable parameters, and $\bar{E}$ is the average of the 1000 Gaussian random variables.

The performance of the proposed method is investigated across different sizes of the initial training set, $N_{0}=30,50,100$. We found that 30 initial points are typically required for stable training. During the active learning process, around 33 new training points are identified, insensitive to $N_{0}$. This is expected because the initial training set may not offer sufficient information on the rare event-starting from 30 or 100 training points may not make much difference. The heteroscedastic Gaussian process model for the error correction at the final learning stage is shown in Figure 6. It is seen that the heteroscedastic Gaussian process can model the noisy errors. The optimization histories of the correlation coefficient $\rho$, the parameter $b_{E}$, and the prediction uncertainty $\hat{P}_{\Delta}=\hat{P}^{+}-\hat{P}^{-}$are shown in Figure 7. The scatter plots of $y_{p}$ and $y_{p}+\epsilon\left(y_{p}\right)$ against $y$ are shown in Figure 8. It is seen that the response predictions of the physics-based surrogate model are highly correlated with the responses of the original model, and the data-driven error correction can improve the bias of the surrogate predictions. To estimate the statistical variability of the proposed surrogate modeling method, the box plot of probability estimations using 10 independent runs is shown in Figure 9. It is observed that the method has a small but noticeable bias for rare event probability estimations. Furthermore, increasing the number of initial training points may not improve the prediction bias and variability. Therefore, using 30 initial training points seems to be ideal for the current problem.



The first quartile, median, and third quartile of the rare event probability estimations are presented in Table 1. Finally, importance sampling is implemented to improve the probability estimation. To achieve a coefficient of variation of $5 \%, 400$ runs of the original model is typically required. The final probability estimate ranges from $3.5 \times 10^{-5}$ to $4.0 \times 10^{-5}$, with a correction factor $c_{P}$ between 1.1 and 1.6 .



Figure 6: Heteroscedastic Gaussian process model of the error correction at the final learning stage for Example 1. From left to right, the Gaussian process models are obtained from 30(initial) +31 (active learning), 50(initial) + 34 (active learning), and 100(initial) + 33 (active learning) training data, respectively. It is seen that the heteroscedastic Gaussian process model can capture the noisy errors.



Figure 7: Optimization histories of the proposed method for Example 1. (a) the correlation coefficient $\rho$ between $Y_{p}$ and $Y$ at the training points achieves $0.9781,0.9756$, and 0.9898 for $N_{0}=30, N_{0}=50$, and $N_{0}=100$, respectively; (b) the tunable parameter $b_{E}$ for the physics-based surrogate model converges to $10.7 \mathrm{GPa},-39.7 \mathrm{GPa}$, and 8.8 GPa for $N_{0}=30$, $N_{0}=50$, and $N_{0}=100$, respectively; (c) the prediction uncertainties stabilize after 30 active learning steps.





Figure 8: Response predictions of the physics-based surrogate model and the coupled physics-data-driven surrogate model for Example 1. The response prediction of the physics-based surrogate model $\mathbf{Y}_{\mathrm{p}}$ is highly correlated with the true responses $\mathbf{Y}$, and the data-driven error correction improves the bias. The mean absolute relative errors between the surrogate model predictions and the true responses, before and after error correction, are $65.12 \%$ and $3.83 \%$ for $N_{0}=30$, $67.39 \%$ and $3.75 \%$ for $N_{0}=50$, and $41.85 \%$ and $3.74 \%$ for $N_{0}=100$, respectively.



Figure 9: Probability estimations using different sizes of the initial training set for Example 1. Each box plot is obtained using 10 independent runs of the proposed surrogate modeling method.

# 5.2. Example 2: An oscillator with nonlinear viscous damper 

Consider an oscillator with nonlinear viscous damper under a Gaussian white noise excitation with the equation of motion expressed as

$$
m \ddot{u}(t)+c \dot{u}(t)+k u(t)+c_{d} \operatorname{sign}(\dot{u}(t))|\dot{u}(t)|^{\alpha_{d}}=-m \ddot{u}_{g}(t)
$$

where $m=3000 \mathrm{~kg}, c=3000 \mathrm{~N} /(\mathrm{m} / \mathrm{s})$, and $k=3 \times 10^{5} \mathrm{~N} / \mathrm{m}$ are the mass, damping, and stiffness of the oscillator, respectively, $u(t), \dot{u}(t)$, and $\ddot{u}(t)$ are the displacement, velocity, and acceleration of the oscillator, respectively, $c_{d}=800 \mathrm{~N} /(\mathrm{m} / \mathrm{s}) \alpha_{d}$ and $\alpha_{d}=0.3$ are the damping coefficient and velocity exponent of the nonlinear viscous damper, respectively, $\operatorname{sign}(\cdot)$ is the sign function, and $\ddot{u}_{g}(t)$ is the acceleration excitation. The excitation has a duration of 15 seconds. Using the spectral representation method [75], the white noise can be discretized into a finite set of Gaussian variables:

$$
\ddot{u}_{g}(X, t)=\sum_{i=1}^{D / 2} \sqrt{2 S_{0} \Delta \omega}\left(X_{i} \cos \left(\omega_{i} t\right)+\bar{X}_{i} \sin \left(\omega_{i} t\right)\right)
$$

where $X_{i}$ and $\bar{X} i, i=1,2, \ldots, D / 2$, are mutually independent standard normal variables, $D=1000, \Delta \omega=$ $2 \omega_{\max } / D$ is the frequency increment with $\omega_{\max }=25 \pi$ being the upper cutoff angular frequency, $\omega_{i}=$ $(i-0.5) \Delta \omega$ is the discretized frequency points, and $S_{0}=5 \times 10^{-3} \mathrm{~m}^{2} / \mathrm{s}^{3}$ is the intensity of the white noise.



To obtain the physics-based surrogate model, the nonlinear equation of motion shown in Eq. (19) is linearized into

$$
m \ddot{u}(t)+\left(c+c_{e}\right) \dot{u}(t)+k u(t)=-m \ddot{u}_{g}(t)
$$

where $\left\{c_{e}\right\}=\theta_{p}$ is the equivalent damping coefficient used as the tuning parameter of the physics-based surrogate model. The rare event of interest is defined as the peak absolute displacement of the oscillator exceeding a threshold of 0.06 m , expressed by

$$
\left\{y=0.06-\sup _{t \in[0,15]}|u(t)| \leq 0\right\}
$$

The initial value of $c_{e}$ for optimization is determined by the traditional statistical linearization method [76]. The coupled physics-data-driven surrogate model is trained using 30,50 , and 100 initial samples and around 34 active learning samples. The heteroscedastic Gaussian process model for error correction at the final learning stage is shown in Figure 10. The optimization histories of the correlation coefficient $\rho$, the equivalent damping coefficient $c_{e}$, and the prediction uncertainty $\hat{P}_{\Delta}=\hat{P}^{+}-\hat{P}^{-}$are shown in Figure 11. The scatter plots of $y_{p}$ and $y_{p}+\epsilon\left(y_{p}\right)$ against $y$ are shown in Figure 12. The box plot of probability estimations using 10 independent runs of the proposed surrogate modeling method is shown in Figure 13, and the first quartile, median, and third quartile of the probability estimations are presented in Table 1. Applying importance sampling, the final probability estimate ranges from $2.6 \times 10^{-7}$ to $2.8 \times 10^{-7}$, with a correction factor between 1.2 and 1.4 , based on 400 runs of the original model.



Figure 10: Heteroscedastic Gaussian process model of the error correction at the final learning stage for Example 2. From left to right, the Gaussian process models are obtained using 30(initial) + 37 (active learning), $50(\text { initial })+32$ (active learning), and $100(\text { initial })+34$ (active learning) training data, respectively. The heteroscedastic Gaussian process model captures the noisy errors.





Figure 11: Optimization histories of the proposed method for Example 2. (a) the correlation coefficient $\rho$ between $Y_{p}$ and $Y$ at the training points achieves $0.9983,0.9980$, and 0.9983 for $N_{0}=30, N_{0}=50$, and $N_{0}=100$, respectively; (b) the equivalent damping parameter $c_{e}$ for the physics-based surrogate model stops at $1881.1 \mathrm{~N} /(\mathrm{m} / \mathrm{s}), 1949.0 \mathrm{~N} /(\mathrm{m} / \mathrm{s})$, and $2140.2 \mathrm{~N} /(\mathrm{m} / \mathrm{s})$ for $N_{0}=30, N_{0}=50$, and $N_{0}=100$, respectively; (c) the prediction uncertainties stabilize after 30 active learning steps .



Figure 12: Response predictions of physics-based surrogate model and coupled physics-data-driven surrogate model for Example 2. The response prediction of the physics-based surrogate model $Y_{p}$ is highly correlated with the true responses $Y$, and the data-driven error correction improves the bias. The mean absolute relative errors between the surrogate model predictions and the true responses, before and after error correction, are $7.48 \%$ and $2.33 \%$ for $N_{0}=30,7.03 \%$ and $2.23 \%$ for $N_{0}=50$, and $5.80 \%$ and $1.99 \%$ for $N_{0}=100$, respectively.



Figure 13: Probability estimations using different sizes of the initial training set for Example 2. Each box plot is obtained using 10 independent runs of the proposed surrogate modeling method.



# 5.3. Example 3: A multi-degree-of-freedom hysteretic system 

Consider a 6-degree-of-freedom shear-type hysteretic system under ground motion excitation, shown in Figure 14. The mass and initial stiffness of each storey are $m_{i}=8000 \mathrm{~kg}$ and $k_{i}=1 \times 10^{7} \mathrm{~N} / \mathrm{m}, i=1,2, \ldots, 6$, respectively. Rayleigh damping is assumed for the hysteretic system with a damping ratio of $5 \%$ for the $1^{\text {st }}$ and $6^{\text {th }}$ mode of the system. The restoring force of each storey is described by the Bouc-Wen model [77] as follows:

$$
\begin{gathered}
f_{i}(t)=\alpha_{i} k_{i} u_{i}(t)+\left(1-\alpha_{i}\right) k_{i} z_{i}(t) \\
\dot{z}_{i}(t)=g_{i}\left(\dot{u}_{i}(t), z_{i}(t)\right)=\phi_{i} \dot{u}_{i}(t)-\varphi_{i}\left|\dot{u}_{i}(t)\right| z_{i}(t)\left|z_{i}(t)\right|^{\gamma_{i}-1}-\psi_{i} \dot{u}_{i}(t)\left|z_{i}(t)\right|^{\gamma_{i}}
\end{gathered}
$$

where $\alpha_{i}=0.1$ is the stiffness reduction ratio of the $i$-th storey; $u_{i}(t), \dot{u}_{i}(t)$, and $z_{i}(t)$ are the relative displacement, relative velocity, and the hysteretic displacement of the $i$-th storey, respectively; $\phi_{i}=1$, $\varphi_{i}=\psi_{i}=1 /\left(2 x_{y i}^{\gamma_{i}}\right)$, and $\gamma_{i}=1$ are the shape parameters of the hysteresis loop; and $x_{y i}=1.25 \mathrm{~mm}$ is the yield displacement of the $i$-th storey. The excitation is assumed to be the same as that in Example 2, but the intensity of the white noise is set to $S_{0}=8.5 \times 10^{-4} \mathrm{~m}^{2} / \mathrm{s}^{3}$.



Figure 14: A 6-degree-of-freedom shear-type hysteretic system under ground motion excitation.
The rare event of interest is defined as the peak absolute deformation among the six storeys exceeding a threshold of 0.015 m , expressed by

$$
\left\{y=0.015-\max _{i \in\{1,2, \ldots, 6\}}\left(\sup _{t \in[0,15]}\left|u_{i}(t)\right|\right) \leq 0\right\}
$$

We define the original and physics-based surrogate models based on solvers of the equation of motion shown in Eq. (24). For the original model, Eq. (24) is solved by the implicit Euler algorithm:

$$
z_{i}(t+\Delta t)=z_{i}(t)+g_{i}\left(\dot{u}_{i}(t+\Delta t), z_{i}(t+\Delta t)\right) \Delta t
$$

and for the surrogate model, Eq. (24) is solved by the explicit Euler algorithm:

$$
z_{i}(t+\Delta t)=z_{i}(t)+g_{i}\left(\dot{u}_{i}(t), z_{i}(t)\right) \Delta t
$$

where $\Delta t$ is the time step. The explicit Euler algorithm is highly efficient but less accurate, and thus is ideal in constructing the physics-based surrogate model. The stiffness reduction ratio $\alpha_{i}$, initial stiffness



$k_{i}$, and yield displacement $x y_{i}$ are set as tunable parameters for the physics-based surrogate model, i.e., $\theta_{p}=\left\{\alpha_{i}, k_{i}, x y_{i}\right\}_{i=1}^{6}$. The initial values of the those parameters are set to be the same as the original model.

The coupled physics-data-driven surrogate model is trained using 30,50 , and 100 initial samples and around 45 active learning samples. The heteroscedastic Gaussian process model for error correction at the final learning stage is shown in Figure 15. The optimization histories of the correlation coefficient $\rho$, the first-storey stiffness reduction ratio $\alpha_{1}$, and the prediction uncertainty $\hat{P}_{\Delta}=\hat{P}^{+}-\hat{P}^{-}$are shown in Figure 16 .

Figure 17 confirms the accuracy of the coupled surrogate model. Figure 18 shows the box plot of probability estimations using 10 independent runs of the proposed surrogate modeling method. Table 1 reports the first quartile, median, and third quartile of the probability estimations.



Figure 15: Heteroscedastic Gaussian process model of the error correction at the final learning stage for Example 3. From left to right, the Gaussian process models are obtained using 30(initial) + 43 active learning), $50(\text { initial })+37$ (active learning), and 100(initial) +52 (active learning) training data, respectively. The heteroscedastic Gaussian process model captures the noisy errors.



Figure 16: Optimization histories of the proposed method for Example 3. (a) the correlation coefficient $\rho$ between $Y_{p}$ and $Y$ at the training points achieves $0.9968,0.9965$, and 0.9964 for $N_{0}=30, N_{0}=50$, and $N_{0}=100$, respectively; (b) the first-storey stiffness reduction ratio $\alpha_{1}$ for the physics-based surrogate model converges to $0.0790,0.0961$, and 0.0922 for $N_{0}=30, N_{0}=50$, and $N_{0}=100$, respectively; (c) the prediction uncertainties stabilize after 40 active learning steps.





Figure 17: Response predictions of physics-based surrogate model and coupled physics-data-driven surrogate model for Example 3. The response prediction of the physics-based surrogate model $\mathbf{Y}_{p}$ is highly correlated with the true responses $\mathbf{Y}$, and the data-driven error correction corrects the bias. The mean absolute relative errors between the surrogate model predictions and the true responses, before and after error correction, are $188.29 \%$ and $16.18 \%$ for $N_{0}=30,62.64 \%$ and $10.08 \%$ for $N_{0}=50$, and $67.48 \%$ and $19.09 \%$ for $N_{0}=100$, respectively.



Figure 18: Probability estimations using different sizes of the initial training set for Example 3. Each box plot is obtained using 10 independent runs of the proposed surrogate modeling method.

Table 1: Probability estimations from the proposed surrogate modeling method (10 independent runs).

| Surrogate model solution | Case | $\boldsymbol{N}_{\mathbf{0}}$ | First quartile | Median | Third quartile |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Reference | 30 | $2.4 \times 10^{-5}$ | $2.9 \times 10^{-5}$ | $3.1 \times 10^{-5}$ |  |
| Example 1 | 50 | $2.4 \times 10^{-5}$ | $2.9 \times 10^{-5}$ | $3.1 \times 10^{-5}$ | $3.6 \times 10^{-5}$ |
|  | 100 | $2.4 \times 10^{-5}$ | $2.6 \times 10^{-5}$ | $3.4 \times 10^{-5}$ |  |
|  | 30 | $2.1 \times 10^{-7}$ | $2.2 \times 10^{-7}$ | $2.4 \times 10^{-7}$ |  |
| Example 2 | 50 | $2.2 \times 10^{-7}$ | $2.3 \times 10^{-7}$ | $2.4 \times 10^{-7}$ | $3.0 \times 10^{-7}$ |
|  | 100 | $2.1 \times 10^{-7}$ | $2.2 \times 10^{-7}$ | $2.4 \times 10^{-7}$ |  |
|  | 30 | $1.3 \times 10^{-3}$ | $1.3 \times 10^{-3}$ | $1.4 \times 10^{-3}$ |  |
| Example 3 | 50 | $1.2 \times 10^{-3}$ | $1.3 \times 10^{-3}$ | $1.4 \times 10^{-3}$ | $1.4 \times 10^{-3}$ |
|  | 100 | $1.3 \times 10^{-3}$ | $1.3 \times 10^{-3}$ | $1.4 \times 10^{-3}$ |  |



# 6. Additional remarks and future directions 

### 6.1. Multiple critical domains of the rare event

The data-driven error correction may not perform well in the presence of multiple critical domains with different response behaviors. Here, the crux is not the "multiple critical domains" per se, but the "different response behaviors" within these domains. For instance, the first-passage probability problems examined in Example 2 and 3 are series systems with numerous modes corresponding to the times at which crossing events occur. However, when the response process reaches stationarity, the rare crossing events become homogeneous across different time points. As a result, the error correction function does not need to discern the specific time point of the crossing, since these events have similar statistical properties. In this context, a one-dimensional error correction function is effective. In contrast, if the computational model exhibits different behaviors across multiple critical domains for the rare event of interest, a one-dimensional error correction approach may introduce noise due to its inability to distinguish the details of the critical modes. A potential solution is to incorporate additional output variables to differentiate between critical domains and train distinct error functions for each domain.

### 6.2. Selection of physics-based surrogate models

Large noisy errors can be induced by the aforementioned mechanism, but another source is the inherent limitations of the selected physics-based surrogate model. We can reduce the inherent noise by using a more detailed surrogate model, but a trade-off between accuracy and efficiency is inevitable. Further studies are needed to standardize the selection of physics-based surrogate models for various classes of problems.

### 6.3. Alternative importance sampling strategies

The importance sampling Eq. (16) can be reformulated into the following expression:

$$
P=c_{P} \cdot \hat{P} \equiv \frac{\int_{\boldsymbol{x} \in \mathbb{R}^{n}} \mathbb{I}_{\leq 0}(M(\boldsymbol{x})) h_{M \cup \hat{M}}(\boldsymbol{x}) d \boldsymbol{x}}{\int_{\boldsymbol{x} \in \mathbb{R}^{n}} \mathbb{I}_{\leq 0}\left(\hat{M}\left(\boldsymbol{x} ; \theta_{p}, \theta_{\epsilon}\right)\right) h_{M \cup \hat{M}}(\boldsymbol{x}) d \boldsymbol{x}} \hat{P}
$$

where the importance density $h_{M \cup \hat{M}}$ is associated with the union of the original and surrogate rare events, expressed by:

$$
h_{M \cup \hat{M}}(\boldsymbol{x}):=\frac{\mathbb{I}_{\leq 0}\left(\min \left(M(\boldsymbol{x}), \hat{M}\left(\boldsymbol{x} ; \theta_{p}, \theta_{\epsilon}\right)\right)\right)}{\mathbb{P}\left(\min \left(M(\boldsymbol{X}), \hat{M}\left(\boldsymbol{X} ; \theta_{p}, \theta_{\epsilon}\right)\right) \leq 0\right)} f_{\boldsymbol{X}}(\boldsymbol{x})
$$

Compared to Eq. (16), this alternative formulation allows for the use of a single set of samples from $h_{M \cup \hat{M}}$ to estimate both the numerator and the denominator. On the other hand, since the union event is larger than individual ones, running Markov Chain Monte Carlo on the union increases the likelihood of biased estimation for the correction factor $c_{P}$. From our preliminary tests, we have not observed a decisive performance gain from using this alternative formulation. Further investigations and tests are needed.



# 7. Conclusions 

This paper develops an effective surrogate modeling method for rare event simulation with high-dimensional input uncertainties. The method circumvents the curse of dimensionality by using physics-based surrogate models parameterized by a few tunable parameters. A data-fitting error correction constructed in the output space of the physics-based surrogate model is leveraged to correct the bias of surrogate modeling. Due to inherent stochastic noise in the errors, the heteroscedastic Gaussian process is adopted to model the error correction function. An active learning process is developed to effectively train the coupled-physics-datariven surrogate model to explore the critical region for the rare event. A final importance sampling step is designed to approximate the correction factor for the surrogate model-based probability estimation. Three numerical examples are studied to demonstrate the performance of the proposed method. The first example considers a static problem of a linear elastic cantilever beam with material properties modeled by a Gaussian random field. The second example studies a dynamic problem of a nonlinear viscous damper under stochastic excitation. The third example investigates a multi-degree-of-freedom hysteretic system under stochastic excitation. Three schemes are investigated to construct physics-based surrogate models: a homogenization of material properties is considered in the first example, statistical linearization is used in the second example, and relaxation of the numerical solver is adopted in the third example. The numerical results are highly promising, suggesting that the proposed method can leverage limited calls of the original computational model to effectively estimate rare event probabilities with high-dimensional input uncertainties.

## References

[1] Jérôme Morio and Mathieu Balesdent. Estimation of rare event probabilities in complex aerospace and other systems: A practical approach. Woodhead Publishing, 2015.
[2] Enrico Zio and Romney B Duffey. The risk of the electrical power grid due to natural hazards and recovery challenge following disasters and record floods: What next? In Climate Change and Extreme Events, pages 215-238. Elsevier, 2021.
[3] Wen Jiang, Jason D Hales, Benjamin W Spencer, Blaise P Collin, Andrew E Slaughter, Stephen R Novascone, Aysenur Toptan, Kyle A Gamble, and Russell Gardner. TRISO particle fuel performance and failure analysis with BISON. Journal of Nuclear Materials, 548:152795, 2021.
[4] Chao Dang and Jun Xu. A mixture distribution with fractional moments for efficient seismic reliability analysis of nonlinear structures. Engineering Structures, 208:109912, 2020.
[5] Jun Xu, Long Li, and Zhao-Hui Lu. An adaptive mixture of normal-inverse Gaussian distributions for structural reliability analysis. Journal of Engineering Mechanics, 148(3):04022011, 2022.
[6] Jie Li and Jianbing Chen. Stochastic dynamics of structures. John Wiley \& Sons, 2009.
[7] Guohai Chen and Dixiong Yang. Direct probability integral method for stochastic response analysis of static and dynamic structural systems. Computer Methods in Applied Mechanics and Engineering, 357:112612, 2019.
[8] Jianhua Xian, Cheng Su, and Houzuo Guo. Seismic reliability analysis of energy-dissipation structures by combining probability density evolution method and explicit time-domain method. Structural Safety, 88:102010, 2021.
[9] Meng-Ze Lyu and Jian-Bing Chen. A unified formalism of the GE-GDEE for generic continuous responses and firstpassage reliability analysis of multi-dimensional nonlinear systems subjected to non-white-noise excitations. Structural Safety, 98:102233, 2022.
[10] Reuven Y Rubinstein and Benjamin Melamed. Modern simulation and modeling, volume 7. Wiley New York, 1998.
[11] David Landau and Kurt Binder. A guide to Monte Carlo simulations in statistical physics. Cambridge University Press, 2015 .
[12] Siu-Kui Au and James L Beck. Estimation of small failure probabilities in high dimensions by subset simulation. Probabilistic Engineering Mechanics, 16(4):263-277, 2001.
[13] Nolan Kurtz and Junho Song. Cross-entropy-based adaptive importance sampling using Gaussian mixture. Structural Safety, 42:35-44, 2013.



[14] Ziqi Wang and Junho Song. Cross-entropy-based adaptive importance sampling using von Mises-Fisher mixture for high dimensional reliability analysis. Structural Safety, 59:42-52, 2016.
[15] Michael Engel, Oindrila Kanjilal, Iason Papaioannou, and Daniel Straub. Bayesian updating and marginal likelihood estimation by cross entropy based importance sampling. Journal of Computational Physics, 473:111746, 2023.
[16] Mircea Grigoriu. Data-based importance sampling estimates for extreme events. Journal of Computational Physics, 412:109429, 2020.
[17] Iason Papaioannou, Costas Papadimitriou, and Daniel Straub. Sequential importance sampling for structural reliability analysis. Structural Safety, 62:66-75, 2016.
[18] Ziqi Wang, Marco Broccardo, and Junho Song. Hamiltonian Monte Carlo methods for subset simulation in reliability analysis. Structural Safety, 76:51-67, 2019.
[19] Jianhua Xian and Ziqi Wang. Relaxation-based importance sampling for structural reliability analysis. Structural Safety, 106:102393, 2024.
[20] Malur R Rajashekhar and Bruce R Ellingwood. A new look at the response surface approach for reliability analysis. Structural Safety, 12(3):205-220, 1993.
[21] DIEGO LORENZO Allaix and VINCENZO ILARIO Carbone. An improvement of the response surface method. Structural Safety, 33(2):165-172, 2011.
[22] Bruno Sudret and Armen Der Kiureghian. Comparison of finite element reliability methods. Probabilistic Engineering Mechanics, 17(4):337-348, 2002.
[23] Stefano Marelli and Bruno Sudret. An active-learning algorithm that combines sparse polynomial chaos expansions and bootstrap for structural reliability analysis. Structural Safety, 75:67-74, 2018.
[24] Emiliano Torre, Stefano Marelli, Paul Embrechts, and Bruno Sudret. Data-driven polynomial chaos expansion for machine learning regression. Journal of Computational Physics, 388:601-623, 2019.
[25] Jorge E Hurtado. An examination of methods for approximating implicit limit state functions from the viewpoint of statistical learning theory. Structural Safety, 26(3):271-293, 2004.
[26] Atin Roy and Subrata Chakraborty. Support vector machine in structural reliability analysis: A review. Reliability Engineering E System Safety, page 109126, 2023.
[27] Irfan Kaymaz. Application of kriging method to structural reliability problems. Structural Safety, 27(2):133-151, 2005.
[28] Barron J Bichon, Michael S Eldred, Laura Painton Swiler, Sandaran Mahadevan, and John M McFarland. Efficient global reliability analysis for nonlinear implicit performance functions. AIAA journal, 46(10):2459-2468, 2008.
[29] Benjamin Echard, Nicolas Gayton, and Maurice Lemaire. AK-MCS: An active learning reliability method combining Kriging and Monte Carlo simulation. Structural Safety, 33(2):145-154, 2011.
[30] Benjamin Echard, Nicolas Gayton, Maurice Lemaire, and Nicolas Relun. A combined importance sampling and kriging reliability method for small failure probabilities with time-demanding numerical models. Reliability Engineering (商店 System Safety, 111:232-240, 2013.
[31] Xiaoxu Huang, Jianqiao Chen, and Hongping Zhu. Assessing small failure probabilities by AK-SS: An active learning method combining Kriging and Subset Simulation. Structural Safety, 59:86-95, 2016.
[32] Ziqi Wang and Marco Broccardo. A novel active learning-based Gaussian process metamodelling strategy for estimating the full probability distribution in forward UQ analysis. Structural Safety, 84:101937, 2020.
[33] Donald R Jones. A taxonomy of global optimization methods based on response surfaces. Journal of Global Optimization, 21:345-383, 2001.
[34] Thomas J Santner, Brian J Williams, William I Notz, and Brain J Williams. The design and analysis of computer experiments, volume 1. Springer, 2003.
[35] Bruno Sudret. Meta-models for structural reliability and uncertainty quantification. arXiv preprint arXiv:1203.2062, 2012.
[36] Christos Lataniotis, Stefano Marelli, and Bruno Sudret. Extending classical surrogate modeling to high dimensions through supervised dimensionality reduction: A data-driven approach. International Journal for Uncertainty Quantification, 10(1), 2020.
[37] Dimitris G Giovanis and Michael D Shields. Uncertainty quantification for complex systems with very high dimensional response using Grassmann manifold variations. Journal of Computational Physics, 364:393-415, 2018.
[38] Dimitris G Giovanis and Michael D Shields. Data-driven surrogates for high dimensional models using Gaussian process regression on the Grassmann manifold. Computer Methods in Applied Mechanics and Engineering, 370:113269, 2020.
[39] Ketson R Dos Santos, Dimitrios G Giovanis, and Michael D Shields. Grassmannian diffusion maps-based dimension



reduction and classification for high-dimensional data. SIAM Journal on Scientific Computing, 44(2):B250-B274, 2022.
[40] Katiana Kontolati, Dimitrios Loukrezis, Dimitrios G Giovanis, Lohit Vandanapu, and Michael D Shields. A survey of unsupervised learning methods for high-dimensional uncertainty quantification in black-box-type problems. Journal of Computational Physics, 464:111313, 2022.
[41] Zhongming Jiang and Jie Li. High dimensional structural reliability with dimension reduction. Structural Safety, 69:35-46, 2017.
[42] Tong Zhou and Yongbo Peng. Active learning and active subspace enhancement for PDEM-based high-dimensional reliability analysis. Structural Safety, 88:102026, 2021.
[43] N Navaneeth and Souvik Chakraborty. Surrogate assisted active subspace and active subspace assisted surrogate-A new paradigm for high dimensional structural reliability analysis. Computer Methods in Applied Mechanics and Engineering, 389:114374, 2022.
[44] Jungho Kim, Ziqi Wang, and Junho Song. Adaptive active subspace-based metamodeling for high-dimensional reliability analysis. Structural Safety, 106:102404, 2024.
[45] Zhong-Ming Jiang, De-Cheng Feng, Hao Zhou, and Wei-Feng Tao. A recursive dimension-reduction method for highdimensional reliability analysis with rare failure event. Reliability Engineering \& System Safety, 213:107710, 2021.
[46] Maziar Raissi, Paris Perdikaris, and George E Karniadakis. Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations. Journal of Computational Physics, 378:686-707, 2019.
[47] Yinhao Zhu, Nicholas Zabaras, Phaedon-Stelios Koutsourelakis, and Paris Perdikaris. Physics-constrained deep learning for high-dimensional surrogate modeling and uncertainty quantification without labeled data. Journal of Computational Physics, 394:56-81, 2019.
[48] Kevin Linka, Amelie Schäfer, Xuhui Meng, Zongren Zou, George Em Karniadakis, and Ellen Kuhl. Bayesian physics informed neural networks for real-world nonlinear dynamical systems. Computer Methods in Applied Mechanics and Engineering, 402:115346, 2022.
[49] Zeng Meng, Qiaochu Qian, Mengqiang Xu, Bo Yu, Ali Rıza Yılı prev, and Seyedali Mirjalili. PINN-FORM: A new physicsinformed neural network for reliability analysis with partial differential equation. Computer Methods in Applied Mechanics and Engineering, 414:116172, 2023.
[50] Benjamin Peherstorfer, Karen Willcox, and Max Gunzburger. Survey of multifidelity methods in uncertainty propagation, inference, and optimization. Siam Review, 60(3):550-591, 2018.
[51] Benjamin Peherstorfer, Tiangang Cui, Youssef Marzouk, and Karen Willcox. Multifidelity importance sampling. Computer Methods in Applied Mechanics and Engineering, 300:490-509, 2016.
[52] Boris Kramer, Alexandre Noll Marques, Benjamin Peherstorfer, Umberto Villa, and Karen Willcox. Multifidelity probability estimation via fusion of estimators. Journal of Computational Physics, 392:385-402, 2019.
[53] John W Peterson, Alexander D Lindsay, and Fande Kong. Overview of the incompressible navier-stokes simulation capabilities in the MOOSE framework. Advances in Engineering Software, 119:68-92, 2018.
[54] Zhong-Hua Han, Stefan Görtz, and Ralf Zimmermann. Improving variable-fidelity surrogate modeling via gradientenhanced kriging and a generalized hybrid bridge function. Aerospace Science and Technology, 25(1):177-189, 2013.
[55] Isaac M Held. The gap between simulation and understanding in climate modeling. Bulletin of the American Meteorological Society, 86(11):1609-1614, 2005.
[56] Peter Benner, Serkan Gugercin, and Karen Willcox. A survey of projection-based model reduction methods for parametric dynamical systems. SIAM review, 57(4):483-531, 2015.
[57] Boris Kramer and Karen E Willcox. Nonlinear model order reduction via lifting transformations and proper orthogonal decomposition. AIAA Journal, 57(6):2297-2307, 2019.
[58] D Patsialis and AA Taflanidis. Reduced order modeling of hysteretic structural response and applications to seismic risk assessment. Engineering Structures, 209:110135, 2020.
[59] Stephen H Crandall. A half-century of stochastic equivalent linearization. Structural Control and Health Monitoring: The Official Journal of the International Association for Structural Control and Monitoring and of the European Association for the Control of Structures, 13(1):27-40, 2006.
[60] Isaac Elishakoff and Stephen H Crandall. Sixty years of stochastic linearization technique. Meccanica, 52:299-305, 2017.
[61] Ziqi Wang. Optimized equivalent linearization for random vibration. Structural Safety, 106:102402, 2024.
[62] Somayajulu LN Dhulipala, Michael D Shields, Benjamin W Spencer, Chandrakanth Bolisetti, Andrew E Slaughter, Vincent M Labouré, and Promit Chakroborty. Active learning with multifidelity modeling for efficient rare event simulation.



Journal of Computational Physics, 468:111506, 2022.
[63] Somayajulu LN Dhulipala, Michael D Shields, Promit Chakroborty, Wen Jiang, Benjamin W Spencer, Jason D Hales, Vincent M Laboure, Zachary M Prince, Chandrakanth Bolisetti, and Yifeng Che. Reliability estimation of an advanced nuclear fuel using coupled active learning, multifidelity modeling, and subset simulation. Reliability Engineering \& System Safety, 226:108693, 2022.
[64] Miguel López-Gredilla, Michalis K Titsias, Jochem Verrelst, and Gustavo Camps-Valls. Retrieval of biophysical parameters with heteroscedastic Gaussian processes. IEEE Geoscience and Remote Sensing Letters, 11(4):838-842, 2013.
[65] TJ Rogers, P Gardner, N Dervilis, K Worden, AE Maguire, E Papatheou, and EJ Cross. Probabilistic modelling of wind turbine power curves with application of heteroscedastic Gaussian process regression. Renewable Energy, 148:1124-1136, 2020 .
[66] Jungho Kim, Sang-ri Yi, and Junho Song. Estimation of first-passage probability under stochastic wind excitations by active-learning-based heteroscedastic Gaussian process. Structural Safety, 100:102268, 2023.
[67] Jan Hauke and Tomasz Kossowski. Comparison of values of Pearson's and Spearman's correlation coefficients on the same sets of data. Quaestiones geographicae, 30(2):87-93, 2011.
[68] Søren Taverniers, Eric J Hall, Markos A Katsoulakis, and Daniel M Tartakovsky. Mutual information for explainable deep learning of multiscale systems. Journal of Computational Physics, 444:110551, 2021.
[69] Samir Beneddine. Nonlinear input feature reduction for data-based physical modeling. Journal of Computational Physics, 474:111832, 2023.
[70] Andrew R Conn, Katya Scheinberg, and Luis N Vicente. Introduction to derivative-free optimization. SIAM, 2009.
[71] Vincent Dubourg, Bruno Sudret, and Jean-Marc Bourinet. Reliability-based design optimization using kriging surrogates and subset simulation. Structural and Multidisciplinary Optimization, 44:673-690, 2011.
[72] Maliki Moustapha, Stefano Marelli, and Bruno Sudret. Active learning for structural reliability: Survey, general framework and benchmark. Structural Safety, 96:102174, 2022.
[73] Radford M Neal et al. MCMC using Hamiltonian dynamics. Handbook of Markov Chain Monte Carlo, 2(11):2, 2011.
[74] Iason Papaioannou, Wolfgang Betz, Kilian Zwirglmaier, and Daniel Straub. MCMC algorithms for subset simulation. Probabilistic Engineering Mechanics, 41:89-103, 2015.
[75] Masanobu Shinozuka and George Deodatis. Simulation of stochastic processes by spectral representation. Applied Mechanics Reviews, 44(4):191-204, 1991
[76] Jianhua Xian, Cheng Su, and Billie F Spencer Jr. Stochastic sensitivity analysis of energy-dissipating structures with nonlinear viscous dampers by efficient equivalent linearization technique based on explicit time-domain method. Probabilistic Engineering Mechanics, 61:103080, 2020.
[77] YK Wen. Equivalent linearization for hysteretic systems under random excitation. Journal of Applied Mechanics, $47(1): 150-154,1980$.



