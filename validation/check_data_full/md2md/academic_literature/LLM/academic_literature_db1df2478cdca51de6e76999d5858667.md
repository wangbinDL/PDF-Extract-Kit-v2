# Quality quandaries: Should estimates be analyzed instead of the raw data? 

Michael S. Hamada, Joseph T. Mang \& Larry H. Hoff


#### Abstract

Quandaries are perplexing problems or doubts; situations with questions that are difficult to resolve. As an example, confident organizations match their best people with key projects, but new people may interpret data differently. For example, an engineer analyzed failures from a reliability growth experiment using non-homogeneous Poisson process (NHPP) software. It provided estimates of the parameters for the Weibull NHPP model which were then analyzed in an Excel spreadsheet to determine the infusion point (start of the beta test) using methods published in a well-known reliability book. The estimate of the infusion point was 120 hours. Coincidentally, this was exactly the same as the maximum likelihood estimate (MLE) of the scale parameter from the software output. A statistician reviewing the work recommended using the MLE infusion point based on the raw data rather than using 120 hours because 120 was an estimate, not a datum. This choice divided the team. They asked, and we explore, which approach is better?


## Publisher content alert

New articles by your favorite authors

## Personalized content collections

Trends in Quality Engineering 


## Cite this article

To cite this article: Michael S. Hamada, Joseph T. Mang \& Larry H. Hoff (2019): Quality quandaries: Should estimates be analyzed instead of the raw data?, Quality Engineering, DOI: 10.1080/08982112.2018.1551547

## Link to article: https://doi.org/10.1080/08982112.2018.1551547

This article was published in Quality Engineering. Want to read the full article?

## Apply for free access to this journal

## Register for:

- Table of contents alerts
- Saved searches
- Article recommendations

Quality Engineering
## https://www.tandfonline.com/loi/lqen20




---

# Quality quandaries: Should estimates be analyzed instead of the raw data? 

Michael S. Hamada ${ }^{a}$, Joseph T. Mang ${ }^{b}$, and Larry H. Hoff ${ }^{c}$<br>a Statistical Sciences Group, Los Alamos National Laboratory, Los Alamos, New Mexico;

KEY POINT There are often situations where estimates are analyzed as measurements. This article considers in one application whether the raw data underlying these estimates should be analyzed directly.

## Introduction

In a typical comparison of two measurement devices, say an old one and a new one, measurements are collected and compared. We consider a situation in explosive sensitivity testing where the quantity of interest is the height (at which a weight is dropped onto an explosive sample) for which there is a 0.50 probability that the explosive reacts and is referred to as the $H_{50}$; higher $H_{50}$ 's correspond to less sensitive samples. The $H_{50}$ is obtained through a sequential binary experiment, where a weight is dropped at different heights onto explosive samples and it is observed whether these samples react (go or $y=1$ ) or not (no-go or $y=0$ ). Consequently, the $H_{50}$ is an estimate obtained from analyzing these sequential binary data. In this article, we consider a comparison of old and new testers by presenting analyses of the $H_{50}$ 's and of the raw data directly. We discuss the advantages and disadvantages of both approaches.

## Up-and-down Bruceton method for sensitivity testing

The sequential binary experiments whose data we analyze were collected using the up-and-down Bruceton method (Dixon and Mood 1948). The up-and-down method begins a test at a starting height. If it is a no-go $(y=0)$, the height is increased for the next test. Otherwise, if it is a go $(y=1)$, the height is decreased for the next test. Table 1 shows the up-and-down method for a reference item consisting of 25 tests; i.e., 25 samples from the reference item are tested whose results are shown in Table 1 and plotted in Figure 1. Note that the step sizes are variable as prescribed by the method. Neyer (1994) and Wu and Tian (2014) propose more recent sequential binary experiment methods.

Let $x=\log _{10}(h)$ for height $h$. Then the response $y$ is modeled as $\operatorname{Bernoulli}(p)$, where

$$
p=\Phi\left(\frac{x-\mu}{\sigma}\right)
$$

and $\Phi(\cdot)$ is the standard normal cumulative distribution function. Note that height $h$ has a lognormal distribution on the logarithm base 10 scale not the usual natural logarithm scale; i.e., $\log _{10}(h)$ has a Normal $\left(\mu, \sigma^{2}\right)$ distribution.

One way to estimate $\mu$ and $\sigma$ is to use Maximum Likelihood Estimates (MLEs). We can obtain MLEs for the probit regression model using the glm function in $R$ (R Core Team 2018) with binomial family and probit link using $\log _{10}(h)$ as the covariate. Probit regression expresses Eq. [1] as $p=\Phi\left(\beta_{0}+\beta_{1} \log _{10}(h)\right)$ so that from the MLEs $\hat{\beta}_{0}$ and $\hat{\beta}_{1}$, we obtain the MLEs $\hat{\mu}=$ $-\frac{\hat{\beta}_{0}}{\hat{\beta}_{1}}$ and $\hat{\sigma}=\frac{1}{\hat{\beta}_{1}}$. From the sequential binary experiment data in Table 1 for a reference item, $\hat{\beta}_{0}=-20.77376$ and $\hat{\beta}_{1}=13.56263$, so that $\hat{\mu}=1.531691$ and $\hat{\sigma}=0.073731988$. Note that $\mu$ is the median on the $\log _{10}$ height scale so that $10^{\mu}$ is the median of $H_{50}$ on the height scale. Consequently, the estimated $H_{50}$ for

a Defense Technologies Engineering Division, Lawrence Livermore National Laboratory, Livermore, California

[^0]![](https://cdn.mathpix.com/cropped/2024_08_17_9729a95108b562980358g-1.jpg?height=417&width=843&top_left_y=2000&top_left_x=158)

[^0]:    b High Explosives Science and Technology, Los Alamos National Laboratory, Los Alamos, New Mexico




---

inspection criterion is based on $\mathrm{l}_{\mathrm{T}} / \mathrm{l}_{\mathrm{R}}$, where T and R denote test and reference, respectively. The test item needs to be less sensitive than the reference item, i.e., $\mathrm{l}_{\mathrm{T}} / \mathrm{l}_{\mathrm{R}}>0$. To compare the old and new hammer testers, several reference items were run on the new and old hammer testers. The same 25 sample sequential binary experiment using the up-and-down method was performed for each of the reference items. Table 2 displays the $\log _{10}\left(\mathrm{H}_{50}\right)$ estimates for these reference items, 19 on the new tester and 12 on the old tester. The estimate for the first reference item using the new tester (i.e., 1.532) corresponds to the sequential binary experiment results shown in Table 1. Figure 2 presents a plot of the $\log _{10}\left(\mathrm{H}_{50}\right)$ estimates from the old and new hammer testers.

Sequential binary experiments ( 25 samples each) were performed on 18 test items over a period of time in groups on each of the testers. That is, this experiment is paired. Because the testing was performed in groups, a reference item was tested for each group for both the new and old tester. Table 3 displays the paired $\log _{10}\left(\mathrm{H}_{50}\right)$ estimates of these test items. A $\log _{10}\left(\mathrm{H}_{50}\right)$ estimate for the associated reference item is given for the first test item in the group. For example, the first four test items measured by the new tester are a group. Note that the new tester groups do not always coincide with the old tester groups.

In the remainder of this article, we consider the analysis of the $\log _{10}\left(\mathrm{H}_{50}\right)$ estimates and the raw data (i.e., the $25(h, y)$ pairs from the sequential binary experiment) directly.

# Analysis of the $\mathbf{H}_{50}$ estimates 

First consider the analysis of $\log _{10}\left(\mathrm{H}_{50}\right)$ estimates for the reference items from Table 2. Separate normal plots of the estimates from the new and old tester (not shown here) look pretty straight suggesting that normality holds. A test of difference between the two variances (the $F$-test from the R function var.test) is





---

not significant with a $p$ value of 0.449 . A test of the difference between the two means (the $t$-test from the R function $t$-test) is highly significant with a $p$ value of $6.486 \times 10^{-6}$. The estimate of the mean difference is 0.064 with $95 \%$ confidence interval $(0.040,0.087)$; that is, the new tester is producing higher (i.e., less sensitive) $\log _{10}\left(H_{50}\right)$ estimates for the reference items.


What is important for the sensitivity testing is whether the relative differences of the $\log _{10}\left(H_{50}\right)$ estimates of the test and reference items are different between the new and old tester. Consequently, we analyze these relative differences calculated from Table 3 results. A test of difference between the two variances is not significant with a $p$-value of 0.193 . A test of difference between the two means (the paired $t$-test from the R function $t$-test with option "paired $=$ TRUE") is also not significant with a $p$-value of 0.799 ; the estimate of the mean difference is 0.0035 with a $95 \%$ confidence interval of $(-0.0252,0.0323)$.

In summary, these results suggests that using the new tester to compare a test item with a reference item is comparable to that using the old tester.

# Analysis of the raw data directly 

In the previous analysis, estimates of $H_{50}$ were analyzed so that $H_{50}$ is measured with error. Also, a number of liberties were taken. Some of the reference estimates in Table 3 are the average of estimates from two separate sequential binary experiments. Moreover, all the relative differences in a group use the same reference estimate. Finally, the hypothesis test $p$-values depend on the relative distributions having a normal distribution.

In this section, we consider a Bayesian analysis that estimates the $\mu$ 's directly so that analogous quantities that are functions of both the reference and test item $\mu$ 's can be studied to address whether the two testers are different in assessing relative differences. We separately analyze the data for each sequential binary experiment to obtain a posterior distribution for $\mu$ and $\theta$. (Gelman et al. 2013; Weaver and Hamada 2016). We used the following priors distributions for




---

each $\lambda$ and $\rho: \lambda \sim \operatorname{Normal}(1.5,9.42)$ and $\ln (\rho) \sim \operatorname{Normal}(-2.8,12)$. These prior distributions are much wider than the range of the MLEs. We obtained 10,000 draws after a burnin of 500 draws from the posterior distributions of $\lambda$ using OpenBUGS (Spiegelhalter et al. 2014). See the OpenBUGS code in the Appendix for analyzing the sequential binary experiment data in Table 1. Figure 3 displays the posterior distribution for $\lambda$ for the reference item whose sequential binary experiment data were presented in Table 1 and whose MLE is 1.532. From Figure 3, its posterior median is 1.535 and its $95 \%$ credible is $(1.475,1.649)$ that shows the uncertainty of $\lambda$ and gives some indication of the uncertainty of the the MLE.


There are 67 reference and test items represented in Tables 2 and 3. Similarly, we obtained 10,000 draws after a burnin of 500 draws from the posterior distributions of their $\lambda$ 's using OpenBUGS (Spiegelhalter et al. 2014). First, we consider the reference item comparison between the new and old testers, the average of the 19 $\lambda$ 's from the new tester minus the average of the 12 $\lambda$ 's from the old tester. The posterior distribution of this difference of averages is displayed in Figure 4. The posterior mean is 0.064 and a $95 \%$ credible interval is $(0.029,0.097)$. Note that the mean is the same from the previous analysis but the uncertainty is more; recall that the $95 \%$ confidence interval using the $\log _{10}\left(H_{50}\right)$ estimates was $(0.040,0.087)$.





---

Next, we consider the relative differences comparison between the new and old testers. We compute the posterior distribution of the average of the 18 relative differences (difference of $\ell$ 's between the test item and the reference item) from the new tester minus the average of the 18 relative differences from the old tester. That is for each posterior draw of the $\ell$ 's we compute this difference of averages. The posterior distribution of this difference of averages is displayed in Figure 5. Its posterior mean is 0.006 and its $95 \%$ credible interval is $(-0.0449,0.060)$. Note that the mean is slightly larger than the previous analysis but the uncertainty is more; recall that the $95 \%$ confidence interval using the $\log _{10}\left(H_{50}\right)$ estimates was $(-0.0252,0.0323)$. Still the $95 \%$ credible interval contains zero so that this suggests that the new and old testers are comparable.

## Discussion

Should the $\mathrm{H}_{50}$ estimates be analyzed or the raw data analyzed directly? From the analyses presented above, the results are quite similar although the raw data analyses results display more uncertainty. Some liberties were taken with the $\mathrm{H}_{50}$ estimates analysis such as the relative differences in the same group (i.e., because the same reference item $\mathrm{H}_{50}$ estimate is used for each of the test item $\mathrm{H}_{50}$ in the group) are correlated; also some of the reference item $\mathrm{H}_{50}$ estimates were averages of two reference item $\mathrm{H}_{50}$ estimates so the that variance of these reference item $\mathrm{H}_{50}$ estimates did not have the same variability as the others. The $\mathrm{H}_{50}$ estimates need not be normally distributed so that the $t$ and $F$ test $p$-values are only approximations. On the hand, a Bayesian analysis of the raw data directly avoids taking such liberties and the posterior distributions of the appropriate functions of the $\mathrm{H}_{50}$ 's provides results to assess the comparability of the new and old tester. The Bayesian analysis using OpenBUGS is more involved but the short code in the Appendix shows how simple Bayesian analyses can be. The increased uncertainty in the Bayesian analysis results suggests what was not captured in analyzing the $\mathrm{H}_{50}$ estimates. While not an issue for this example, there can be situations in which the analysis of the $\mathrm{H}_{50}$ estimates could have suggested that the new and old testers are different, whereas the analysis of the raw data directly would not have. If time permits, it would be worth doing both analyses and if both agree presenting the $\mathrm{H}_{50}$ estimates as it will be easier to explain.

## About the authors

Michael S. Hamada is a Scientist at Los Alamos National Laboratory and holds a Ph.D. in Statistics from the University of Wisconsin-Madison. He is a Fellow of the American Statistical Association and of the American Society for Quality. His research interests include design and analysis of experiments, reliability, quality improvement, and measurement assessment.

Joseph T. Mang is a Scientist at Los Alamos National Laboratory and holds a Ph.D. in Physics from Kent State University. His research interests include safety and sensitivity testing of high explosives and application of small angle scattering techniques to high explosives, polymers and foams.





---

Logan H. Hoff is an Engineer at Lawrence Livermore National Laboratory and holds a B.S. in Mechanical Engineering and an M.S. in Business from West Texas A\&M University. His research interests include sensitivity testing of high explosives and subcritical nuclear experiments.

## References

Dixon, W. J., and A. M. Mood. 1948. A method for obtaining and analyzing sensitivity data. Journal of the American Statistical Association 43 (241):109-26. doi: 10.2307/2280071.
Gelman, A., J. B. Carlin, H. S. Stern, D. B. Dunson, A. Vehtari, and D. B. Rubin. 2013. Bayesian data analysis. 3rd ed. Boca Raton, FL: Chapman \& Hall/CRC.
Neyer, B. T. 1994. D-optimality-based sensitivity test. Technometrics 36 (1):61-70. doi:10.2307/1269199.
R Core Team. 2018. R: A programming language and environment for statistical computing. Vienna, Austria: R Foundation for Statistical Computing. Last accessed June 26, 2018.
Spiegelhalter, D., A. Thomas, N. Best, and D. Lunn. 2014. OpenBUGS version 3.2.3 user manual. Accessed June 26, 2018. http://www.openbugs.net/Manuals/Manual.html.
Weaver, B. P., and M. S. Hamada. 2016. Quality quandaries: A gentle introduction to Bayesian statistics. Quality Engineering 28 (4):508-14.
Wu, C. F. J., and Y. Tian. 2014. Three-phase optimal design of sensitivity experiments. Journal of Statistical Planning and Inference 149:1-15.

## Appendix

This appendix presents OpenBUGS code for the analysis of a sequential binary experiment data.


Data
list( $\mathrm{h}=(25.4,28.5,), \mathrm{y}=(0,1,)$ )
Inits
list(mu $=1.53, \operatorname{lsigma} 05=2.61)$




---

