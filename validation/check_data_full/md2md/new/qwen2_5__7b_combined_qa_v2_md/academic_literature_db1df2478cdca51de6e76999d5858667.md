

# Quality Engineering 

## Quality quandaries: Should estimates be analyzed instead of the raw data?

Michael S. Hamada, Joseph T. Mang \& Larry H. Hoff

To cite this article: Michael S. Hamada, Joseph T. Mang \& Larry H. Hoff (2019): Quality quandaries: Should estimates be analyzed instead of the raw data?, Quality Engineering, DOI: $10.1080 / 08982112.2018 .1551547$

To link to this article: $\underline{h t t p s: / / d o i . o r g / 10.1080 / 08982112.2018 .1551547}$

Published online: 09 Jan 2019.

Submit your article to this journal

Article views: 36

View Crossmark data \lceil



# Quality quandaries: Should estimates be analyzed instead of the raw data? 

Michael S. Hamada ${ }^{\mathrm{a}}$, Joseph T. Mang ${ }^{\mathrm{b}}$, and Larry H. Hoff ${ }^{\mathrm{c}}$<br>${ }^{a}$ Statistical Sciences Group, Los Alamos National Laboratory, Los Alamos, New Mexico; ${ }^{b}$ High Explosives Science and Technology, Los<br>Alamos National Laboratory, Los Alamos, New Mexico; ${ }^{\mathrm{c}}$ Defense Technologies Engineering Division, Lawrence Livermore National<br>Laboratory, Livermore, California


#### Abstract

KEY POINT There are often situations where estimates are analyzed as measurements. This article considers in one application whether the raw data underlying these estimates should be analyzed directly.


## Introduction

In a typical comparison of two measurement devices, say an old one and a new one, measurements are collected and compared. We consider a situation in explosive sensitivity testing where the quantity of interest is the height (at which a weight is dropped onto an explosive sample) for which there is a 0.50 probability that the explosive reacts and is referred to as the $H_{50}$; higher $H_{50}$ 's correspond to less sensitive samples. The $H_{50}$ is obtained through a sequential binary experiment, where a weight is dropped at different heights onto explosive samples and it is observed whether these samples react (go or $y=1$ ) or not (no-go or $y=0$ ). Consequently, the $H_{50}$ is an estimate obtained from analyzing these sequential binary data. In this article, we consider a comparison of old and new testers by presenting analyses of the $H_{50}$ 's and of the raw data directly. We discuss the advantages and disadvantages of both approaches.

## Up-and-down Bruceton method for sensitivity testing

The sequential binary experiments whose data we analyze were collected using the up-and-down Bruceton method (Dixon and Mood 1948). The up-and-down method begins a test at a starting height. If it is a no-go $(y=0)$, the height is increased for the next test.

[^0]Otherwise, if it is a go $(y=1)$, the height is decreased for the next test. Table 1 shows the up-and-down method for a reference item consisting of 25 tests; i.e., 25 samples from the reference item are tested whose results are shown in Table 1 and plotted in Figure 1. Note that the step sizes are variable as prescribed by the method. Neyer (1994) and Wu and Tian (2014) propose more recent sequential binary experiment methods.

Let $x=\log _{10}(h)$ for height $h$. Then the response $y$ is modeled as $\operatorname{Bernoulli}(p)$, where

$$
p=\Phi\left(\frac{x-\mu}{\sigma}\right)
$$

and $\Phi()$ is the standard normal cumulative distribution function. Note that height $h$ has a lognormal distribution on the logarithm base 10 scale not the usual natural logarithm scale; i.e., $\log _{10}(h)$ has a $\operatorname{Normal}\left(\mu, \sigma^{2}\right)$ distribution.

One way to estimate $\mu$ and $\sigma$ is to use Maximum Likelihood Estimates (MLEs). We can obtain MLEs for the probit regression model using the glm function in $R$ (R Core Team 2018) with binomial family and probit link using $\log _{10}(h)$ as the covariate. Probit regression expresses Eq. [1] as $p=\Phi\left(\beta_{0}+\beta_{1} \log _{10}(h)\right)$ so that from the MLEs $\hat{\beta}_{0}$ and $\hat{\beta}_{1}$, we obtain the MLEs $\hat{\mu}=$ $-\frac{\hat{\beta}_{0}}{\hat{\beta}_{1}}$ and $\hat{\sigma}=\frac{1}{\hat{\beta}_{1}}$. From the sequential binary experiment data in Table 1 for a reference item, $\hat{\beta}_{0}=-20.77376$ and $\hat{\beta}_{1}=13.56263, \quad$ so $\quad$ that $\hat{\mu}=1.531691$ and $\hat{\sigma}=0.073731988$. Note that $\mu$ is the median on the $\log _{10}$ height scale so that $10^{\mu}$ is the median of $H_{50}$ on the height scale. Consequently, the estimated $H_{50}$ for Table 1 data is $10^{1.531691}=34.01661$

## The comparison experiment

When an item or group of items is tested (referred to as test items), a reference item is tested because the


[^0]:    CONTACT Michael S. Hamada hamada@lanl.gov Statistical Sciences, Los Alamos National Laboratory, Los Alamos, NM, USA. M.S. Hamada and B.P. Weaver are the Quality Quandaries co-editors.
    (C) 2019 Taylor \& Francis Group, LLC



Table 1. Up-and-down method for a reference item.


inspection criterion is based on $\mu_{\mathrm{T}}-\mu_{\mathrm{R}}$, where T and R denote test and reference, respectively. The test item needs to be less sensitive than the reference item, i.e., $\mu_{\mathrm{T}}-\mu_{\mathrm{R}}>0$. To compare the old and new hammer testers, several reference items were run on the new and old hammer testers. The same 25 sample sequential binary experiment using the up-and-down method was performed for each of the reference items. Table 2 displays the $\log _{10}\left(H_{50}\right)$ estimates for these reference items, 19 on the new tester and 12 on the old tester. The estimate for the first reference item using the new tester (i.e., 1.532) corresponds to the sequential binary experiment results shown in Table 1. Figure 2 presents a plot of the $\log _{10}\left(H_{50}\right)$ estimates from the old and new hammer testers.

Sequential binary experiments ( 25 samples each) were performed on 18 test items over a period of time in groups on each of the testers. That is, this experiment is paired. Because the testing was performed in groups, a reference item was tested for each group for both the new and old tester. Table 3 displays the paired $\log _{10}\left(H_{50}\right)$ estimates of these test items. A $\log _{10}\left(H_{50}\right)$ estimate for the associated reference item is given for the first test item in the group. For example, the first four test items measured by the new tester are a group. Note that the new tester groups do not always coincide with the old tester groups.

In the remainder of this article, we consider the analysis of the $\log _{10}\left(H_{50}\right)$ estimates and the raw data (i.e., the $25(h, y)$ pairs from the sequential binary experiment) directly.

## Analysis of the $H_{50}$ estimates

First consider the analysis of $\log _{10}\left(H_{50}\right)$ estimates for the reference items from Table 2. Separate normal plots of the estimates from the new and old tester (not shown here) look pretty straight suggesting that normality holds. A test of difference between the two variances (the $F$-test from the $R$ function var.test) is

Table 2. $\log _{10}\left(H_{50}\right)$ estimates for reference items from new and old hammer testers.

| New tester |  |  |  |  |  |  |  |  |  |  |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1.532 | 1.456 | 1.458 | 1.475 | 1.460 | 1.451 | 1.453 | 1.489 | 1.410 | 1.481 | 1.399 | 1.419 | 1.481 | 1.399 |
| 1.438 | 1.453 | 1.489 | 1.410 | 1.431 |  |  |  |  |  |  |  |  |  |
| Old tester |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 1.421 | 1.401 | 1.374 | 1.407 | 1.397 | 1.386 | 1.360 | 1.332 | 1.398 | 1.359 | 1.431 | 1.389 |  |  |





Figure 2. $\log _{10}\left(H_{50}\right)$ estimates for reference items for new and old hammer testers.
not significant with a $p$ value of 0.449 . A test of the difference between the two means (the $t$-test from the $R$ function $t$-test) is highly significant with a $p$ value of $6.486 \times 10^{-6}$. The estimate of the mean difference is 0.064 with $95 \%$ confidence interval $(0.040,0.087)$; that is, the new tester is producing higher (i.e., less sensitive) $\log _{10}\left(H_{50}\right)$ estimates for the reference items.

What is important for the sensitivity testing is whether the relative differences of the $\log _{10}\left(H_{50}\right)$ estimates of the test and reference items are different between the new and old tester. Consequently, we analyze these relative differences calculated from Table 3 results. A test of difference between the two variances is not significant with a $p$-value of 0.193 . A test of difference between the two means (the paired $t$-test from the $R$ function $t$-test with option "paired = TRUE") is also not significant with a $p$-value of 0.799 ; the estimate of the mean difference is 0.0035 with a $95 \%$ confidence interval of $(-0.0252,0.0323)$.

In summary, these results suggests that using the new tester to compare a test item with a reference item is comparable to that using the old tester.

## Analysis of the raw data directly

In the previous analysis, estimates of $H_{50}$ were analyzed so that $H_{50}$ is measured with error. Also, a number of liberties were taken. Some of the reference estimates in Table 3 are the average of estimates from two separate sequential binary experiments. Moreover, all the relative differences in a group use the same reference estimate. Finally, the hypothesis test $p$-values depend on the relative distributions having a normal distribution.

In this section, we consider a Bayesian analysis that estimates the $\lambda$ 's directly so that analogous quantities that are functions of both the reference and test item $\lambda$ 's can be studied to address whether the two testers are different in assessing relative differences. We separately analyze the data for each sequential binary experiment to obtain a posterior distribution for $\lambda$ and $\tau$. (Gelman et al. 2013; Weaver and Hamada 2016). We used the following priors distributions for

Table 3. Paired $\log _{10}\left(H_{50}\right)$ estimates of test items and $\log _{10}\left(H_{50}\right)$ estimates of their associated reference items.

|  | New tester | Test |
| :--- | :---: | :---: |
| Ref. | Old tester |  |
|  | Test | Ref. |
|  | 1.603 | 1.481 |
|  | 1.586 | 1.386 |
|  | 1.626 | 1.586 |
|  | 1.637 | 1.479 |
| 1.615 | 1.513 | 1.656 |
|  | 1.399 | 1.516 |
|  | 1.331 | 1.622 |
|  | 1.565 | 1.631 |
|  | 1.508 | 1.360 |
|  | 1.607 | 1.600 |
|  | 1.592 | 1.445 |
|  | 1.529 | 1.398 |
|  | 1.599 | 1.524 |
|  | 1.609 | 1.544 |
|  | 1.610 | 1.449 |
|  | 1.560 | 1.359 |
|  | 1.595 | 1.503 |
|  | 1.618 | 1.597 |
|  | 1.604 | 1.431 |
|  | 1.594 | 1.389 |
|  | 1.588 | 1.564 |
|  | 1.585 | 1.579 |
|  | 1.629 | 1.488 |
|  |  | 1.431 |





Figure 3. Posterior distribution of $\lambda$ for a reference item.
each $\lambda$ and $\rho: \lambda \sim \operatorname{Normal}(1.5,9.42)$ and $\ln (\rho) \sim \operatorname{Normal}(-2.8,12)$. These prior distributions are much wider than the range of the MLEs. We obtained 10,000 draws after a burnin of 500 draws from the posterior distributions of $\lambda$ using OpenBUGS (Spiegelhalter et al. 2014). See the OpenBUGS code in the Appendix for analyzing the sequential binary experiment data in Table 1. Figure 3 displays the posterior distribution for $\lambda$ for the reference item whose sequential binary experiment data were presented in Table 1 and whose MLE is 1.532 . From Figure 3, its posterior median is 1.535 and its $95 \%$ credible is $(1.475,1.649)$ that shows the uncertainty of $\lambda$ and gives some indication of the uncertainty of the the MLE.

There are 67 reference and test items represented in Tables 2 and 3. Similarly, we obtained 10,000 draws after a burnin of 500 draws from the posterior distributions of their $\lambda$ 's using OpenBUGS (Spiegelhalter et al. 2014). First, we consider the reference item comparison between the new and old testers, the average of the 19 $\lambda$ 's from the new tester minus the average of the 12 $\lambda$ 's from the old tester. The posterior distribution of this difference of averages is displayed in Figure 4. The posterior mean is 0.064 and a $95 \%$ credible interval is $(0.029,0.097)$. Note that the mean is the same from the previous analysis but the uncertainty is more; recall that the $95 \%$ confidence interval using the $\log _{10}\left(H_{50}\right)$ estimates was $(0.040,0.087)$.



Figure 4. Posterior distribution of the average of reference item $\lambda$ 's from the new tester minus the average of the reference item $\lambda$ 's from the old tester.





Figure 5. Posterior distribution of average of the relative differences (difference of $\lambda$ 's between the test item and the reference item) from the new tester minus the average the relative differences from the old tester.

Next, we consider the relative differences comparison between the new and old testers. We compute the posterior distribution of the average of the 18 relative differences (difference of $\lambda$ 's between the test item and the reference item) from the new tester minus the average of the 18 relative differences from the old tester. That is for each posterior draw of the $\lambda$ 's we compute this difference of averages. The posterior distribution of this difference of averages is displayed in Figure 5. Its posterior mean is 0.006 and its $95 \%$ credible interval is $(-0.0449,0.060)$. Note that the mean is slightly larger than the previous analysis but the uncertainty is more; recall that the $95 \%$ confidence interval using the $\log _{10}\left(H_{50}\right)$ estimates was $(-0.0252,0.0323)$. Still the $95 \%$ credible interval contains zero so that this suggests that the new and old testers are comparable.

## Discussion

Should the $H_{50}$ estimates be analyzed or the raw data analyzed directly? From the analyses presented above, the results are quite similar although the raw data analyses results display more uncertainty. Some liberties were taken with the $H_{50}$ estimates analysis such as the relative differences in the same group (i.e.,
because the same reference item $H_{50}$ estimate is used for each of the test item $H_{50}$ in the group) are correlated; also some of the reference item $H_{50}$ estimates were averages of two reference item $H_{50}$ estimates so the that variance of these reference item $H_{50}$ estimates did not have the same variability as the others. The $H_{50}$ estimates need not be normally distributed so that the $t$ and $F$ test $p$-values are only approximations. On the hand, a Bayesian analysis of the raw data directly avoids taking such liberties and the posterior distributions of the appropriate functions of the $H_{50}$ 's provides results to assess the comparability of the new and old tester. The Bayesian analysis using OpenBUGS is more involved but the short code in the Appendix shows how simple Bayesian analyses can be. The increased uncertainty in the Bayesian analysis results suggests what was not captured in analyzing the $H_{50}$ estimates. While not an issue for this example, there can be situations in which the analysis of the $H_{50}$ estimates could have suggested that the new and old testers are different, whereas the analysis of the raw data directly would not have. If time permits, it would be worth doing both analyses and if both agree presenting the $H_{50}$ estimates as it will be easier to explain.

## About the authors

Michael S. Hamada is a Scientist at Los Alamos National Laboratory and holds a Ph.D. in Statistics from the University of Wisconsin-Madison. He is a Fellow of the American Statistical Association and of the American Society for Quality. His research interests include design and analysis of experiments, reliability, quality improvement, and measurement assessment.

Joseph T. Mang is a Scientist at Los Alamos National Laboratory and holds a Ph.D. in Physics from Kent State University. His research interests include safety and sensitivity testing of high explosives and application of small angle scattering techniques to high explosives, polymers and foams.





Images of theLicensed underCC BY
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

```
model {
    for(i in 1: 25) {
    x[i]<-log(h[i])/log(10) # log10 of height
    prob[i]<-phi((x[i]-mu)/sigma)
    y[i] ~ dbern(prob[i])
    }
    # priors
    sigma <- exp(lsigma)
    lsigma ~ dnorm(2.8,1)
    mu ~ dnorm(1.5,6.25)
}
```

Data
list $(\mathrm{h}=(25.4,28.5}, \mathrm{y}=(0,1,))$

Inits
list(mu $=1.53$, lsigma05 $=2.61$ )



