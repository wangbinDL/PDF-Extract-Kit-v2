# Quality quandaries: Should estimates be analyzed instead of the raw data?  

Michael S. Hamada, Joseph T. Mang & Larry H. Hoff  

To cite this article:  Michael S. Hamada, Joseph T. Mang & Larry H. Hoff (2019): Quality quandaries: Should estimates be analyzed instead of the raw data?, Quality Engineering, DOI: 10.1080/08982112.2018.1551547  

To link to this article:   https://doi.org/10.1080/08982112.2018.1551547  

# Quality quandaries: Should estimates be analyzed instead of the raw data?  

a b c Michael S. Hamada , Joseph T. Mang , and Larry H. Hoff  

a Statistical Sciences Group, Los Alamos National Laboratory, Los Alamos, New Mexico;  b High Explosives Science and Technology, Los   c Alamos National Laboratory, Los Alamos, New Mexico; Defense Technologies Engineering Division, Lawrence Livermore National Laboratory, Livermore, California  

# KEY POINT  

There are often situations where estimates are analyzed as measurements. This article considers in one application whether the raw data underlying these estimates should be analyzed directly.  

# Introduction  

In a typical comparison of two measurement devices, say an old one and a new one, measurements are col- lected and compared. We consider a situation in explosive sensitivity testing where the quantity of interest is the height (at which a weight is dropped onto an explosive sample) for which there is a 0.50 probability that the explosive reacts and is referred to as the H50; higher   $\mathrm{H}50^{\circ}s$   correspond to less sensitive samples. The H50 is obtained through a sequential binary experiment, where a weight is dropped at dif- ferent heights onto explosive samples and it is observed whether these samples react (go or    $y\!=\!1.$  ) or not (no-go or  $y\!=\!0$  ). Consequently, the H50 is an esti- mate obtained from analyzing these sequential binary data. In this article, we consider a comparison of old and new testers by presenting analyses of the   $\mathrm{H}50^{\circ}s$  and of the raw data directly. We discuss the advan- tages and disadvantages of both approaches.  

# Up-and-down Bruceton method for sensitivity testing  

The sequential binary experiments whose data we ana- lyze were collected using the up-and-down Bruceton method (Dixon and Mood  1948 ). The up-and-down method begins a test at a starting height. If it is a no-go  $(y\!=\!0)$  , the height is increased for the next test. Otherwise, if it is a go   $(y\!=\!1)$  ), the height is decreased for the next test.  Table 1  shows the up-and-down method for a reference item consisting of 25 tests; i.e., 25 samples from the reference item are tested whose results are shown in  Table 1  and plotted in  Figure 1 . Note that the step sizes are variable as prescribed by the method. Neyer ( 1994 ) and Wu and Tian ( 2014 ) propose more recent sequential binary experiment methods.  

Let  $x=\log{10(h)}$   for height    $h$  . Then the response  y is modeled as  Bernoulli  $(p)$  , where  

$$
p=\Phi\!\left({\frac{x\!-\!\mu}{\sigma}}\right)
$$  

and    $\Phi(\v u)$   is the standard norm  cumulative distribu- tion function. Note that height  h  has a lognormal dis- tribution on the logarithm base 10 scale not the usual natural logarithm scale; i.e.,  $\log10(h)$  has a Normal  $\operatorname{I}(\mu,\sigma^{2})$   distribution.  

One way to estimate    $\mu$   and    $\sigma$   is to use Maximum Likelihood Estimates (MLEs). We can obtain MLEs for the probit regression model using the glm function in R (R Core Team  2018 ) with binomial family and probit link using   $\log10(h)$   as the covariate. Probit regression expresses Eq. [1 as    $p=\Phi(\beta_{0}+\beta_{1}\log10(h))$   so from the MLEs    $\hat{\beta}_{0}$   and    $\hat{\beta}_{1}$  , we obtain the MLEs  $\hat{\mu}=$   ¼  $-\,\frac{{\hat{\beta}}_{0}}{{\hat{\beta}}_{1}}$    and    $\begin{array}{r}{\hat{\boldsymbol{\sigma}}=\frac{1}{\hat{\beta}_{1}}}\end{array}$  . From the sequential binary experiment data in  Table 1  for a reference item,  $\hat{\beta}_{0}\overset{\cdot}{=}-20.77376$  and  $\hat{\beta}_{1}=13.56263$  so that  $\hat{\mu}=1.531691$   ¼ and

  $\hat{\sigma}=0.073731988$   ¼ 073731988. Note th  $\mu$   is the median on the

  $\log{10}$   height scale so that 10   is the median of H50 on the height scale. Consequently, the estimated H50 for Table 1  data is   $10^{1.531691}=34.01661$  .  

# The comparison experiment  

When an item or group of items is tested (referred to as test items), a reference item is tested because the  

<td><table  border="1"><thead><tr><td></td><td><b>1</b></td><td><b>2</b></td><td><b>3</b></td><td><b>4</b></td><td><b>5</b></td><td><b>6</b></td><td><b>7</b></td><td><b>8</b></td><td><b>9</b></td><td><b>10</b></td><td><b>11</b></td><td><b>12 </b></td><td><b>13 </b></td></tr></thead><tbody><tr><td>h</td><td>25.4</td><td>28.5</td><td>25.4</td><td>28.5</td><td>32.0</td><td>35.9</td><td>32.0</td><td>35.9</td><td>40.3 </td><td>35.9</td><td>32.0</td><td>28.5</td><td>32.0</td></tr><tr><td>Y</td><td>.0</td><td>1</td><td>0</td><td>:</td><td>.:</td><td>.1</td><td>.0</td><td>.:</td><td>.1</td><td>1</td><td>1</td><td>0</td><td>1</td></tr><tr><td>14</td><td>15 </td><td>16</td><td>17</td><td>18</td><td>19</td><td>20</td><td>21</td><td>22 ,</td><td>23 </td><td>24</td><td>25,</td><td></td><td></td></tr><tr><td>h</td><td>28.5</td><td>32.0</td><td>28.5</td><td>32.0</td><td>35.9</td><td>40.3</td><td>35.9</td><td>32.0</td><td>35.9 </td><td>40.3 </td><td>35.9</td><td>40.3</td><td></td></tr><tr><td>Y</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td></td></tr></tbody></table></td>  

![](images/9572bc94404383d6f93b218ebc63ec1a5a7db96581b83980d22d0884b3976b21.jpg)  
Figure 1.  Plot of the up-and-down method for a reference item (heights (h)) for 25 tests and responses (open circle (no-go), solid circle (go)).  

<td><table  border="1"><thead><tr><td colspan="5"><b>New tester</b></td></tr></thead><tbody><tr><td>1.532</td><td>1.456</td><td>1.458</td><td>1.475</td><td>1.460</td></tr><tr><td>1.451</td><td>1.453</td><td>1.489</td><td>1.410</td><td>1.481</td></tr><tr><td>1.399</td><td>1.419</td><td>1.481</td><td>1.399</td><td>1.438</td></tr><tr><td>1.453</td><td>1.489</td><td>1.410</td><td>1.431</td><td></td></tr><tr><td colspan="5">Old tester</td></tr><tr><td>1.421</td><td>1.401</td><td>1.374</td><td>1.407</td><td>1.397</td></tr><tr><td>1.386</td><td>1.360</td><td>1.332</td><td>1.398</td><td>1.359</td></tr><tr><td>1.431</td><td>1.389</td><td></td><td></td><td></td></tr></tbody></table></td>  

inspection criterion is based on    $\mu_{T}\!-\!\mu_{R}$  , where    $T$   and  $R$   denote test and reference, respectively. The test item needs to be less sensitive than the reference item, i.e.,  $\mu_{T}{-}\mu_{R}{>}0$  . To compare the old and new hammer test- ers, several reference items were run on the new and old hammer testers. The same 25 sample sequential binary experiment using the up-and-down method was performed for each of the reference items.  Table 2  displays the   $\log10(\mathrm{H}50)$   estimates for these refer- ence items, 19 on the new tester and 12 on the old tester. The estimate for the first reference item using the new tester (i.e., 1.532) corresponds to the sequen- tial binary experiment results shown in  Table 1 . Figure 2  presents a plot of the   $\log10(\mathrm{H}50)$   estimates from the old and new hammer testers.  

Sequential binary experiments (25 samples each) were performed on 18 test items over a period of time in groups on each of the testers. That is, this experi- ment is paired. Because the testing was performed in groups, a reference item was tested for each group for both the new and old tester.  Table 3  displays the paired   $\log10(\mathrm{H}50)$   estimates of these test items. A  $\log10(\mathrm{H}50)$   estimate for the associated reference item is given for the first test item in the group. For example, the first four test items measured by the new tester are a group. Note that the new tester groups do not always coincide with the old tester groups.  

In the remainder of this article, we consider the analysis of the  $\log10(\mathrm{H}50)$   estimates and the raw data (i.e., the 25   $(h,\ y)$   pairs from the sequential binary experiment) directly.  

# Analysis of the H50 estimates  

First consider the analysis of   $\log10(\mathrm{H}50)$   estimates for the reference items from  Table 2 . Separate normal plots of the estimates from the new and old tester (not shown here) look pretty straight suggesting that normality holds. A test of difference between the two variances (the    $F.$  -test from the    $R$   function var.test) is  

![](images/640f98f474b7dc9fc82a3f93ca7431615094cb8c2cf769a87f189fa95a98d88c.jpg)  

not significant with a    $\boldsymbol{\mathcal{P}}$   value of 0.449. A test of the difference between the two means (the    $t.$  -test from the  $R$   function    $t.$  -test) is highly significant with a    $\boldsymbol{\mathit{p}}$   value of   $6.486\times10^{-6}$  . The estimate of the mean difference is 0.064 with   $95\%$   confidence interval  ð 0 : 040 ;  0 : 087 Þ ; that is, the new tester is producing higher (i.e., less sensitive)  $\log10(\mathrm{H}50)$  estimates for the refer- ence items.  

What is important for the sensitivity testing is whether the relative differences of the   $\log10(\mathrm{H}50)$  estimates of the test and reference items are different between the new and old tester. Consequently, we analyze these relative differences calculated from Table 3  results. A test of difference between the two variances is not significant with a  $\boldsymbol{\mathcal{P}}$  -value of 0.193. A test of difference between the two means (the paired  $t$  -test from the  $R$  function  $t.$  -test with option  $\mathbf{\ddot{\tau}}_{\mathrm{Barred}}\!=\!\mathbf{T}\!\mathbf{R}\mathbf{U}\mathbf{E}^{\ast}\!)$  ) is also not significant with a  $\boldsymbol{\mathcal{P}}$  -value of 0.799; the estimate of the mean difference is 0.0035 with a  $95\%$   confidence interval of    $\left(-0.0252,0.0323\right)$  .  

In summary, these results suggests that using the new tester to compare a test item with a reference item is comparable to that using the old tester.  

# Analysis of the raw data directly  

In the previous analysis, estimates of H50 were ana- lyzed so that H50 is measured with error. Also, a number of liberties were taken. Some of the reference estimates in  Table 3  are the average of estimates from two separate sequential binary experiments. Moreover,  

<td><table  border="1"><thead><tr><td colspan="2"><b>New tester</b></td><td colspan="2"><b>Old tester</b></td></tr><tr><td><b>Test</b></td><td><b>Ref.</b></td><td><b>Test</b></td><td><b>Ref</b></td></tr></thead><tbody><tr><td>1.603</td><td>1.481</td><td>1.586</td><td>1.386</td></tr><tr><td>1.626</td><td></td><td>1.586</td><td></td></tr><tr><td>1.637</td><td></td><td>1.479</td><td></td></tr><tr><td>1.615</td><td></td><td>1.513</td><td></td></tr><tr><td>1.656</td><td>1.399</td><td>1.516</td><td>1.331</td></tr><tr><td>1.622</td><td></td><td>1.565</td><td></td></tr><tr><td>1.631</td><td></td><td>1.508</td><td>1.360</td></tr><tr><td>1.607</td><td></td><td>1.600</td><td></td></tr><tr><td>1.592</td><td>1.445</td><td>1.529</td><td>1.398</td></tr><tr><td>1.599</td><td></td><td>1.524</td><td></td></tr><tr><td>1.609</td><td></td><td>1.544</td><td></td></tr><tr><td>1.610</td><td>1.449</td><td>1.560</td><td>1.359</td></tr><tr><td>1.595</td><td></td><td>1.503</td><td></td></tr><tr><td>1.618</td><td></td><td>1.597</td><td></td></tr><tr><td>1.604</td><td>1.431</td><td>1.594</td><td>1.389</td></tr><tr><td>1.588</td><td></td><td>1.564</td><td></td></tr><tr><td>1.585</td><td></td><td>1.579</td><td></td></tr><tr><td>1.629</td><td></td><td>1.488</td><td>1.431</td></tr></tbody></table></td>  

all the relative differences in a group use the same ref- erence estimate. Finally, the hypothesis test    $\boldsymbol{\mathcal{P}}$  -values depend on the relative distributions having a normal distribution.  

In this section, we consider a Bayesian analysis that estimates the    $\mu\dot{s}$   directly so that analogous quantities that are functions of both the reference and test item l ’ s can be studied to address whether the two testers are different in assessing relative differences. We sep- arately analyze the data for each sequential binary experiment to obtain a posterior distribution for    $\mu$  and    $\sigma$  . (Gelman et al.  2013 ; Weaver and Hamada 2016 ). We used the following priors distributions for  

![](images/73e94d4270c7ef641287d36595a95a38c8e5eebace728b789163306380df54d3.jpg)  
Figure 3.  Posterior distribution of    $\mu$   for a reference item.  

![](images/e553f033af0154ca2fb1f536f5bb77fc4d4d8e1dd6808552c39186608be37455.jpg)  
Figure 4.  Posterior distribution of the average of reference item    $\mu^{\prime}\mathsf{s}$   from the new tester minus the average of the reference item  $\mu^{\prime}\mathsf{s}$   from the old tester.  

each  $\mu$  and  $\sigma$  :  $\mu{\sim}N o r m a l(1.5,9.4^{2})$  and  $\ln{(\sigma)}{\sim}N o r m a l({-}2.8,1^{2})$  . These prior distributions are much wider than the range of the MLEs. We obtained 10,000 draws after a burnin of 500 draws from the posterior distributions of  $\mu$  using OpenBUGS (Spiegelhalter et al.  2014 ). See the OpenBUGS code in the Appendix for analyzing the sequential binary experiment data in  Table 1 .  Figure 3  displays the pos- terior distribution for    $\mu$   for the reference item whose sequential binary experiment data were presented in Table 1  and whose MLE is 1.532. From  Figure 3 , its posterior median is 1.535 and its   $95\%$   credible is ð 1 : 475 ;  1 : 649 Þ  that shows the uncertainty of    $\mu$   and gives some indication of the uncertainty of the the MLE.  

There are 67 reference and test items represented in  Tables 2  and  3 . Similarly, we obtained 10,000 draws after a burnin of 500 draws from the poster- ior distributions of their l ’ s using OpenBUGS (Spiegelhalter et al.  2014 ). First, we consider the ref- erence item comparison between the new and old testers, the average of the 19  l ’ s from the new tester minus the average of the   $12\ \mu\mathrm{\'s}$   from the old tester. The posterior distribution of this difference of aver- ages is displayed in  Figure 4 . The posterior mean is 0.064 and a   $95\%$   credible interval is  ð 0 : 029 ;  0 : 097 Þ . Note that the mean is the same from the previous analysis but the uncertainty is more; recall that the  $95\%$   confidence interval using the   $\log10(\mathrm{H}50)$   esti- mates was 0 : 040 ;  0 : 087 .  

![](images/36faaa1342ca7c39b3034842a3c45105c820e113c9f386af28acb79d7b4b3fe1.jpg)  
Figure 5.  Posterior distribution of average of the relative differences (difference of    $\mu^{\prime}\mathsf{s}$   between the test item and the reference item) from the new tester minus the average the relative differences from the old tester.  

Next, we consider the relative differences compari- son between the new and old testers. We compute the posterior distribution of the average of the 18 relative differences (difference of    $\mu^{*}$  ’ s between the test item and the reference item) from the new tester minus the average of the 18 relative differences from the old tester. That is for each posterior draw of the    $\mu^{*}$  ’ s we compute this difference of averages. The posterior dis- tribution of this difference of averages is displayed in Figure 5 . Its posterior mean is 0.006 and its   $95\%$   cred- ible interval is    $\left(-0.0449,0.060\right)$  . Note that the mean is slightly larger than the previous analysis but the uncertainty is more; recall that the   $95\%$   confidence interval using the  $\log10(\mathrm{H}50)$  estimates was  $\left(-0.0252,0.0323\right)$  . Still the   $95\%$   credible interval con- tains zero so that this suggests that the new and old testers are comparable.  

# Discussion  

Should the H50 estimates be analyzed or the raw data analyzed directly? From the analyses presented above, the results are quite similar although the raw data analyses results display more uncertainty. Some liber- ties were taken with the H50 estimates analysis such as the relative differences in the same group (i.e., because the same reference item H50 estimate is used for each of the test item H50 in the group) are corre- lated; also some of the reference item H50 estimates were averages of two reference item H50 estimates so the that variance of these reference item H50 esti- mates did not have the same variability as the others.  

The H50 estimates need not be normally distributed so that the    $t$   and    $F$   test  $\boldsymbol{\mathcal{P}}$  -values are only approxima- tions. On the hand, a Bayesian analysis of the raw data directly avoids taking such liberties and the pos- terior distributions of the appropriate functions of the  $\mathrm{H}50^{\circ}s$   provides results to assess the comparability of the new and old tester. The Bayesian analysis using OpenBUGS is more involved but the short code in the Appendix shows how simple Bayesian analyses can be. The increased uncertainty in the Bayesian ana- lysis results suggests what was not captured in analyz- ing the H50 estimates. While not an issue for this example, there can be situations in which the analysis of the H50 estimates could have suggested that the new and old testers are different, whereas the analysis of the raw data directly would not have. If time per- mits, it would be worth doing both analyses and if both agree presenting the H50 estimates as it will be easier to explain.  

# About the authors  

Michael S. Hamada is a Scientist at Los Alamos National Laboratory and holds a Ph.D. in Statistics from the University of Wisconsin-Madison. He is a Fellow of the American Statistical Association and of the American Society for Quality. His research interests include design and analysis of experiments, reliability, quality improve- ment, and measurement assessment.  

Joseph T. Mang is a Scientist at Los Alamos National Laboratory and holds a Ph.D. in Physics from Kent State University. His research interests include safety and sensi- tivity testing of high explosives and application of small angle scattering techniques to high explosives, polymers and foams.  

Logan H. Hoff is an Engineer at Lawrence Livermore National Laboratory and holds a B.S. in Mechanical Engineering and an M.S. in Business from West Texas A&M University. His research interests include sensitivity testing of high explosives and subcritical nuclear experiments.  

# References  

Dixon, W. J., and A. M. Mood.  1948 . A method for obtain- ing and analyzing sensitivity data. Journal of the American Statistical Association  43 (241):109 – 26. doi: 10.2307/2280071 . Gelman, A., J. B. Carlin, H. S. Stern, D. B. Dunson, A. Vehtari, and D. B. Rubin.  2013 .  Bayesian data analysis . 3rd ed. Boca Raton, FL: Chapman & Hall/CRC. Neyer, B. T. 1994 . D-optimality-based sensitivity test. Technometrics  36 (1):61 – 70. doi: 10.2307/1269199 . R Core Team.  2018 .  R: A programming language and environ- ment for statistical computing . Vienna, Austria: R Foundation for Statistical Computing. Last accessed June 26, 2018. Spiegelhalter, D., A. Thomas, N. Best, and D. Lunn.  2014 . OpenBUGS version 3.2.3 user manual . Accessed June 26, 2018.  http://www.openbugs.net/Manuals/Manual.html . Weaver, B. P., and M. S. Hamada.  2016 . Quality quandaries: A gentle introduction to Bayesian statistics.  Quality Engineering  28 (4):508 – 14. Wu, C. F. J., and Y. Tian.  2014 . Three-phase optimal design of sensitivity experiments.  Journal of Statistical Planning and Inference  149:1 – 15.  

# Appendix  

This appendix presents OpenBUGS code for the analysis of a sequential binary experiment data.  

model { for( i  in 1: 25) { x[ i ] < -log( h [ i ])/log(10) # log10 of height prob[i]<-phi((x[i]-mu)/sigma)y[i]  dbern(prob[i])} # priors sigma    $<-$   exp(lsigma) ls gma  $\sim$  dnorm(2.8,1) mu    dnorm(1.5,6.25) } Data list(  $^(\,h=\,(\,25\,.\,4\,,\,28\,.\,5\,,\,\,)\,,\,\,y=\,(\,0\,,1\,,\,\,)\,\,)$  Inits list(mu  ¼  1.53,lsigma05  ¼  2.61)  