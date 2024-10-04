# Contents 

Preface ..... vii
1 Introduction ..... 1
1.1 Introduction ..... 1
1.2 Probability sample ..... 2
1.3 Basic Procedures for survey sampling ..... 6
1.3.1 Survey Planning ..... 6
1.3.2 Design and development ..... 7
1.3.3 Implementation ..... 7
1.3.4 Survey Evaluation ..... 8
1.4 Survey errors ..... 8
2 Horvitz-Thompson estimation ..... 11
2.1 Introduction ..... 11
2.2 Horvitz-Thompson estimation ..... 12
2.3 Other parameters ..... 17
2.4 Discussion ..... 18
3 Simple and systematic sampling designs ..... 21
3.1 Introduction ..... 21
3.2 Simple random sampling ..... 21
3.3 Implementation of simple random sampling ..... 25
3.4 Simple random sampling with replacement ..... 27
3.5 Bernoulli Sampling ..... 29
3.6 Systematic sampling ..... 30
3.7 Entropy for sampling designs ..... 34
4 Stratified Sampling ..... 37
4.1 Introduction ..... 37
4.2 Sample size allocation ..... 38
4.3 Stratum boundary determination ..... 45
4.4 Number of strata ..... 46
4.5 Domain Estimation ..... 47




---

5 Sampling with Unequal probabilities ..... 51
5.1 Introduction ..... 51
5.2 PPS sampling ..... 53
5.3 Poisson sampling ..... 55
5.4 Maximum Entropy Sampling ..... 59
5.5 $\pi$ ps sampling ..... 60
5.6 Systematic $\pi p s$ sampling ..... 65
6 Cluster Sampling: Single stage cluster sampling ..... 67
6.1 Introduction ..... 67
6.2 Single-stage cluster sampling: Equal Size Case ..... 68
6.3 Single-stage cluster sampling: Unequal Size Case ..... 73
7 Cluster Sampling: Two-stage cluster sampling ..... 77
7.1 Introduction ..... 77
7.2 Estimation ..... 78
8 Estimation: Part 1 ..... 87
8.1 Introduction ..... 87
8.2 Ratio Estimation ..... 87
8.3 Regression Estimation ..... 92
9 Estimation: Part 2 ..... 99
9.1 GREG estimation ..... 99
9.2 Optimal Estimation ..... 105
9.3 Model-assisted calibration ..... 109
9.4 Generalized entropy calibration ..... 113
10 Variance Estimation ..... 117
10.1 Introduction ..... 117
10.2 Linearization approach to variance estimation ..... 119
10.3 Replication approach to variance estimation ..... 121
10.3.1 Random group method ..... 122
10.4 Jackknife method ..... 124
11 Two-phase sampling ..... 129
11.1 Introduction ..... 129
11.2 Two-phase sampling for stratification ..... 131
11.3 Regression estimator for two-phase sampling ..... 135
11.4 Non-nested two-phase sampling ..... 143
11.5 Repeated surveys ..... 148




---

# 1 Introduction 

### 1.1 Introduction

Suppose that we are interested in obtaining the employment rate of the US population in a certain time. In this case, we can think of two ways to obtain the employment rate. One is to measure the employment status for every individual in the population and then take the mean of the measurement in the population. The other is to sample a subset of the population and then use the average employment status of the sample as an estimate for the employment status of the population. The former method is called census, and the latter is called sample survey. Roughly speaking, the census may obtain an accurate figure of the true employment rate, but the cost for census can be enormous. On the other hand, the sample survey can reduce the cost greatly, but the sample estimate can be quite different from the true population values. In this simple example, the true employment rate of the target population is called a parameter. From the sample survey, we obtain an estimate of the parameter. There are many different ways of obtaining samples from the same population. Thus, finding the best sample (and the corresponding estimator) is one of the main goals of survey sampling.

Sample survey has the following advantages over the census:

1. It reduces the cost significantly.
2. It takes much less time. Thus, we can obtain information about the population in a timely manner.
3. Because we employ more trained interviewers in survey sampling, it can produce more accurate estimates.
4. Sometimes, it is the only way to get information about the target population.

The third point may sound strange, but it is often true in practice because the census may have larger non-sampling errors than the sample surveys. Because the sample survey is based only on a subset of the finite population, there is always a danger of failing to represent the population properly. The representativeness of a sample is a concept that roughly describes whether the sample can be treated as a miniature of the finite population (Kruskal and Mosteller, 1979). A representative sample can give the most of the pictures




---

of the finite population in a cost-effective way. When we use a subset of the population to make inferences about the population, the sample estimate can be different from the parameter to some extent. The sampling error of an estimator is the difference between the estimator and the parameter. We can reduce the sampling error in two aspects. One is to use a suitable sampling rule and the other is to use enough sample size. Note that the sampling error of an estimator $\hat{\theta}$ can be written as

$$
\hat{\theta}-\theta=\{\hat{\theta}-\mathrm{E}(\hat{\theta})\}+\{\mathrm{E}(\hat{\theta})-\theta\}
$$

The first term, $\hat{\theta}-\mathrm{E}(\hat{\theta})$, can be called the variation of $\hat{\theta}$ and the second term, $\mathrm{E}(\hat{\theta})-\theta$, is called the bias of $\hat{\theta}$. Increasing the sample size will reduce the absolute value of the variation part and using a sampling rule that guarantees unbiasedness will make the second part equal to zero.

The accuracy of an estimator is often measured by mean squared errors, which is give by

$$
\begin{aligned}
\operatorname{MSE}(\hat{\theta}) & \equiv \mathrm{E}\left\{(\hat{\theta}-\theta)^{2}\right\} \\
& =\{\operatorname{Bias}(\hat{\theta})\}^{2}+\mathrm{V}(\hat{\theta})
\end{aligned}
$$

By employing a probability sampling design, we can make $\operatorname{Bias}(\hat{\theta})=0$. By increasing the sample size, we can make the variance smaller. Probability sampling will be introduced in the next section.

# 1.2 Probability sample 

Probability sampling refers to a set of sampling methods in which the selection probability in each element in the population is known and strictly positive. For example, simple random sampling assigns equal probability of selection to each element of the population. In this case, the selected sample is obtained objectively and does not involve subjective human selection. There are many different ways of obtaining probability samples, and the choice depends on the objective of the study, the cost, and the prior information available in the sampling frame. The following simple example will illustrate the basic idea.

Example 1.1. Suppose that there are four farms in a town. The finite population consists of 4 farms in Table 1.1 and we are interested in estimating the average crop yield in the population. Here, the farm acreage is the auxiliary information that is available in advance and the crop yield is the item of interest in the study. Suppose further that, due to the cost restriction, we want to select only $n=2$ farms and estimate the average crop yield from the sample.




---

TABLE 1.1
Farm acreage and crop yield

| ID | Acreage | Yield (y) |
| :--- | :---: | :---: |
| 1 | 4 | 1 |
| 2 | 6 | 3 |
| 3 | 6 | 5 |
| 4 | 20 | 15 |

In this case, there are six ways to select a sample of size $n=2$ from the finite population of size $N=4$. Among the six possible samples, we select one sample and measure the crop yields from the sample. In probability sampling, we can select one sample randomly from the six possible samples. Here, "random" sampling means that the sample selection is determined solely by the random number generated for the sample selection, without involving any subjective human decision. To select a sample randomly, the selection probability is assigned in advance for each possible sample. Once the selection probability is assigned to each sample, the final sample is selected using a random number generated from a random-number-generating mechanism.

When selecting a sample from a finite population, there is a finite number of possible samples, and the probability distribution of the sample can be treated as a probability distribution for a discrete random variable. In this case, the probability distribution of a sample consists of all possible samples and their selection probabilities. The selection probabilities must be sum to one. Simple random sampling refers to the sampling mechanism where the selection probabilities are all equal for samples with the same sample size. Table 1.2 shows the probability distribution of the sample under simple random sampling using the example in Table 1.1. Since there are 6 possible samples of size $n=2$ from the population of size $N=4$, the selection probabilities are all equal to $1 / 6$. The probability distribution of the sample is simply called the sample distribution.

TABLE 1.2
Sample distribution under simple random sampling

| Sample ID | Selection probability |
| :--- | :--- |
| 1,2 | $1 / 6$ |
| 1,3 | $1 / 6$ |
| 1,4 | $1 / 6$ |
| 2,3 | $1 / 6$ |
| 2,4 | $1 / 6$ |
| 3,4 | $1 / 6$ |




---

Determining the sample distribution is equivalent to determining the sampling mechanism, the probability mechanism for sample selection. Sampling design refers to the process of determining the sampling mechanism. Form the sample distribution, we can use a random number to select a sample. For example, in Table 1.2, if the random number is 0.4 then $\{1,4\}$ is selected because 0.4 is greater than $2 / 6$ and less than $3 / 6$.

Note that we can compute an estimator from the sample observations. For example, sample mean can be computed from each sample. Thus, we can the sampling distribution of the sample mean from the sample distribution. Probability distribution of an estimator consists of all possible values of the estimator and their probabilities. The possible value of an estimator can be computed from the observed values in the sample. Thus, sampling distribution of an estimator is induced from the sample distribution, the probability distribution of the sample. Table 1.3 presents the sampling distribution of the sample mean under the simple random sampling given by Table 1.2. From the sampling distribution table, the sample mean $\bar{y}$ is distributed as a discrete random variable taking values on $2,3,4,8,9,10$, with equal probability. Thus, we have $\mathrm{E}(\bar{y})=6$ which is equal to the population mean. Under the sampling distribution in Table 1.3, the expectation of the sample mean is equal to the population mean. That is, sample mean is unbiased for the population mean under simple random sampling.

TABLE 1.3
Sampling distribution of sample mean under simple random sampling


Unbiasedness of an estimator is a desirable property but it does not mean that your estimator in a particular sample is close to the true parameter. In the example above, if sample $\{1,2\}$ is selected, your estimate of the population mean is 2 , which is much smaller than the truth $(=6)$. That is, unbiasedness does not imply accuracy.

How to improve the accuracy of an estimator? One way is to increase the sample size. By increasing the sample size, the variance is reduced. If the estimator is unbiased, smaller variance means smaller mean squared error and it means high accuracy. Another way of improving accuracy is to use more efficient sampling designs. Making an efficient sampling design by properly




---

incorporating the auxiliary information of the sampling frame is one of the main topics in survey sampling. Example 1.2 will provide an illustration for an efficient sampling design.

One thing to note from the above example is that the basis for inference is with respect to the sampling mechanism and has nothing to do with the actual value of $y_{i}$ in the population. That is, the reference distribution in computing the expectation of an estimator is the probability mechanism generated by a repeated application of the sampling design. This approach is called the design-based approach because the sampling design is used mainly to make statistical inferences about the population, treating $y_{i}$ as fixed. On the other hand, the model-based approach refers to an alternative approach to inferring a finite population by making model assumptions about $y_{i}$ in the population. In survey sampling, the design-based approach is more popular because it does not rely on model assumptions, which can be difficult to verify in practice. Also, design-based approach avoids the danger of human subjectivity in sample selection, which is an important issue in government official statistics.

Example 1.2. Consider the simple farm example in Example 1.1 and consider the following alternative sampling mechanism.

TABLE 1.4
An alternative sample distribution

| Sample ID | Selection probability |
| :---: | :---: |
| 1,4 | $1 / 3$ |
| 2,4 | $1 / 3$ |
| 3,4 | $1 / 3$ |

In this new sampling design, farm unit 4 is selected with certainty, and one of the other three farms is selected with equal probability. Table 1.5 gives the sampling distribution of the mean estimator under this alternative sampling design.

TABLE 1.5
Sampling distribution of the mean estimator under the alternative sampling design

| Sample ID | $y$ value | mean estimator | selection probability |
| :---: | :---: | :---: | :---: |
| 1,4 | 1,15 | 4.5 | $1 / 3$ |
| 2,4 | 3,15 | 6 | $1 / 3$ |
| 3,4 | 5,15 | 7.5 | $1 / 3$ |

Table 1.5 shows the sampling distribution of the mean estimator under the




---

alternative sampling design in Table 1.4. Note that each sample has observation $\left\{y_{k}, y_{4}\right\}, k=1,2,3$ and the mean estimator takes the form of $\left(3 y_{k}+y_{4}\right) / 4$ because one selected $y_{k}$ represents three elements $\left\{y_{1}, y_{2}, y_{3}\right\}$ and $y_{4}$ represents itself only. The new sampling design still provides unbiased estimation as the expectation of the mean estimator is equal to 6 . However, the variance of the mean estimator is now 1.5 , which is much lower than the variance 9.67 under simple random sampling.

As can be seen in Table 1.5, the alternative sampling design significantly reduces the sampling variance without increasing the sample size. Efficient sampling design can improve the accuracy of an estimator without increasing the sample size.

# 1.3 Basic Procedures for survey sampling 

Survey sampling is developed to collect information about characteristics of interest from a subset of the population to build a database for analytical or descriptive purposes. The manual "Survey Methods and Practice", published by Statistics Canada (2003), provides an excellent summary of the basic procedures for sample surveys in government agencies. The life of a survey can be broken down into several phases. The first is the planning phase, which is followed by the design and development phase, and then the implementation phase. Finally, the entire survey process is reviewed and evaluated. The phases of the life of a survey are described below.

### 1.3.1 Survey Planning

Survey planning is the first step in any survey sampling procedure. In the preliminary planning stage, those who are considering a sample survey should formulate the objectives of the proposed survey. The objective should include the specification of the information to be gathered and the determination of the target population, to which the findings of the survey will be extrapolated.

Once a survey proposal is formulated, it is important to determine whether a new survey is necessary, considering costs and other practical constraints in conducting a new survey. Sometimes, the goal can be achieved by adding equations to an existing survey's questionnaire or by redesigning an existing survey.

If it is decided to conduct a new survey, the planning team may proceed to formulate the statement of objectives and develop some appreciation of the frame options, the general sample size, the precision requirement, the data collection options and the cost. More discussion of the items in the Statement of Objectives is beyond the scope of this textbook. See Chapter 2 of Statistics Canada (2003) for more details.




---

The selection of a sampling frame is also an important part in survey planning. The sampling frame ultimately defines the population to be surveyed, which may be different from the target population to which the Statement of Objective refers. In order to define the target population, the statistical agency begins with a conceptual population for which no actual list may exist. For example, the conceptual population may be all farmers. To define the target population, "farmers" must be defined. The target population is the population for which information is desired to apply. On the other hand, the survey population is the population that is actually covered by the survey. The survey frame (or sampling frame) is a realized list of the survey population. For example, in the survey of household and expenditures in the US, the target population is the entire resident population of the US on a particular reference date. However, in reality, we do not have addresses for those living in institutions or living without fixed addresses. Thus, the survey population excludes those residents in the US on the same reference date.

# 1.3.2 Design and development 

A subset of the survey population is selected from the sampling frame to collect the information we are interested in. Probability sampling, which is the main topic of this book, will be used to obtain a representative sample of the population. There are several different ways to select a probability sample. The choice of the sampling design depends on several factors such as the availability of the sampling frame, the heterogeneity of the study variable, the target precision and the cost of the survey measurements. For a given population, a balance of sampling error with cost and timeliness is achieved through the choice of design and sample size. A more efficient estimation procedure can also be developed by incorporating the auxiliary information available throughout the finite population.

In addition to the choice of the sampling design and the estimation procedure, there are also choices of measurements to be taken and the procedures for taking these measurements. The subject matter persons, who will be users of the survey data, should provide the primary input to specify the measurements that are needed to meet the objective of the study. Once the measurements are specified, the measurement experts (survey methodologists or psychologists) begin designing the questionnaires or forms to be used to obtain the data from the sample individuals. Survey questionnaires may undergo some pilot survey and revision before being used in the main survey.

### 1.3.3 Implementation

Having ensured that all systems are in place, the survey can now be launched. This is the implementation phase. Interviewers are trained, the sample is selected, and information is collected, all in a manner established during the development phase. Following these activities, data processing begins. Pro-




---

cessing activities include data capture, coding, editing, and imputation. The result is a well-structured and complete data set from which it is possible to produce required tabulations and to analyze survey results. The confidentiality of these results is then checked and distributed. At each step, data quality must be measured and monitored using methods designed and developed in the previous phase.

# 1.3.4 Survey Evaluation 

Once the survey is over, the entire process can be documented and evaluated. This involves assessments of the methods used, as well as evaluations of operational effectiveness and cost performance. These evaluations serve as a test of the suitability of technical practices. They also serve to improve and guide the implementation of specific concepts or components of methodology and operations, within and between surveys.

### 1.4 Survey errors

Estimates obtained from a sample survey can suffer from several sources of errors. The errors of an estimator can be classified into two categories. One is the sampling error, the error due to selecting only a subset of the population, and the other is non-sampling error, the error that can be obtained even under census. Non-sampling errors consist of coverage error, response error, measurement error, and processing error, etc. The coverage error occurs when the sampling frame is incomplete in the sense that it does not fully cover the target population. Response error occurs when the sampled element does not respond to the survey. Measurement error occurs when there is a discrepancy between the actual value and the reported value for certain study items. Measurement error exists when there is misunderstanding of the survey questions, or due to a false answer, or due to interviewer effect. Processing error refers to the errors that occur when transferring the survey answers to the computing process system.

The coverage error, sampling error, and response error are combined to form the non-observation error because the errors are due to not observing the elements in the target population. Measurement error and processing error are combined to form the error of observation because the error occurs even if we observe all elements of the population.






---

tics as a branch of statistics. This book will mainly deal with issues related to survey statistics, and Groves et al. (2009) may be cited as a representative reference book for survey methodology.

TABLE 1.6
Survey Methodology and Survey Statistics

| Survey Methodology | Survey Statistics |
| :---: | :---: |
| Psychology (Cognitive science), sociology | Statistics |
| More interested in non-sampling errors | More interested in sampling errors |
| By properly asking questions, we can <br> reduce survey errors | Measure the uncertainty of survey errors <br> and incorporate them into inference |
| Questionnaire design, Survey management | Sampling design, estimation, imputation etc. |

In general, in order to reduce the coverage error among various nonsampling errors, a good sampling frame should be used. For example, when a yellow book is used to select samples, people who do not have a landline phone will not be sampled, so you will have to get another list to supplement it. Multi-frame survey, using several sampling frames, can be considered in this case, but then we need to worry about duplication problem.

To reduce nonresponse error, we may need to train the interviewer, publicize the survey, manage the survey target, and give higher incentives to survey participation. The measurement error was determined by the survey method, the sincerity and training level of the interviewer, and the clarity of the survey questions. Sufficient motivation and training is also required from the interviewees.

In general, as the sample size increases, the sampling error decreases, but the non-sampling error becomes more difficult to manage. For example, if the sample size is very large, it becomes difficult to manage interviewers, which increases the risk of non-response errors or measurement errors. Therefore, in addition to cost reduction, conducting a sampling of an appropriate size is very important in that non-sampling error can be reduced.




---

# 2 Horvitz-Thompson estimation 

### 2.1 Introduction

We will study some theory for unbiased estimation under probability sampling designs. Let $U=\{1, \cdots, N\}$ be the set of indexes of the target population. A probability sample is simply a subset of $U$, denoted by $A \subset U$, selected by a probability rule, called the sampling design. Let $\mathcal{A}=\{A ; A \subset U\}$ be the set of all possible samples. We have the following formal definition of the sampling distribution.

Definition 2.1. 1. Sampling distribution : probability mass function defined on $\mathcal{A}$. That is, a sampling distribution $P(\cdot)$ satisfies the following properties:
(a) $P(A) \in[0,1], \quad \forall A \in \mathcal{A}$
(b) $\sum_{A \in \mathcal{A}} P(A)=1$.
2. Random sampling $\Longleftrightarrow P(A)<1, \quad$ for all $A \in \mathcal{A}$
3. Purposive sampling $\Longleftrightarrow P(A)=1$ for some $A \in \mathcal{A}$

If the parameter of interest is a population quantity that can be written as $\theta_{N}=\theta\left(y_{i} ; i \in U\right)$, a statistic is written as $\hat{\theta}=\hat{\theta}\left(y_{i} ; i \in A\right)$, which means that it is a function of $y_{i}$ in the sample. If the statistic is used to estimate $\theta_{N}$, then it becomes an estimator. The sampling distribution of an estimator is obtained from the sample distribution. That is, as discussed in Section 1.2, the probability mass function $P(A)$ applied to obtain $A$ is then used to represent $P\left\{\hat{\theta}=\hat{\theta}\left(y_{i} ; i \in A\right)\right\}$, the probability distribution or the sampling distribution of $\hat{\theta}$. Using the sampling distribution of the estimator, we can also compute the expectation and variance of the estimator.

Definition 2.2. For parameter $\theta_{N}$, let $\hat{\theta}(A)=\hat{\theta}\left(y_{i} ; i \in A\right)$ be an estimator of $\theta_{N}$.

1. Expectation : $E(\hat{\theta})=\sum_{A \in \mathcal{A}} P(A) \hat{\theta}(A)$
2. Variance: $V(\hat{\theta})=\sum_{A \in \mathcal{A}} P(A)\{\hat{\theta}(A)-E(\hat{\theta})\}^{2}$
3. Mean squared error : $\operatorname{MSE}(\hat{\theta})=\sum_{A \in \mathcal{A}} P(A)\left\{\hat{\theta}(A)-\theta_{N}\right\}^{2}$



---

Here, the expectation is taken with respect to the sampling design induced by the probability rule for $\mathcal{A}$, treating $\left\{y_{1}, y_{2}, \cdots, y_{N}\right\}$ as fixed. As discussed in Chapter 1, the difference between $\mathrm{E}(\hat{\theta})$ and $\theta_{N}$ is called bias and an estimator is called an unbiased estimator when its bias is zero. When an estimator has high precision, it means that its variance is small, but it does not necessarily mean that its accuracy is high. The accuracy of an estimator is related to the small mean squared error of the estimator.

# 2.2 Horvitz-Thompson estimation 

Does an unbiased estimator always exist for all probability sampling designs? To answer this question, we need the following definition of inclusion probabilities.

Definition 2.3.

1. First-order inclusion probability:

$$
\pi_{i}=\operatorname{Pr}(i \in \mathcal{A})=\sum_{\mathcal{A} ; i \in \mathcal{A}} P(\mathcal{A})
$$

2. Second-order inclusion probability, or joint inclusion probability:

$$
\pi_{i j}=\operatorname{Pr}(i, j \in \mathcal{A})=\sum_{\mathcal{A} ; i, j \in \mathcal{A}} P(\mathcal{A})
$$

3. Probability sampling design: $\pi_{i}>0, \quad \forall i \in \mathcal{U}$
4. Measurable sampling design : $\pi_{i j}>0 \quad \forall i, j \in \mathcal{U}$.

That is, the first-order inclusion probability $\pi_{i}$ refers to the probability that the unit $i$ is included in the sample. Furthermore, the second-order inclusion probability $\pi_{i j}$ refers to the probability that both units, unit $i$ and unit $j$, are included in the sample. Note that $\pi_{i i}=\pi_{i}$ by definition. Probability sampling design is a sampling design in which all first-order inclusion probabilities are strictly greater than zero. Probability sampling design is a sufficient condition for the existence of a design-unbiased estimator of the population total. Measurable sampling design is a sampling design in which all second-order inclusion probabilities are strictly greater than zero. Measurable sampling design is a sufficient condition for the existence of a design unbiased estimator of sampling variance of an unbiased estimator.

The following lemma presents some algebraic properties of the inclusion probabilities.




---

Lemma 2.1. The first order inclusion probabilities satisfy

$$
\sum_{i=1}^{N} \pi_{i}=n
$$

where $n$ is the sample size. If the sampling design is a fixed-size sampling design such that $V(n)=0$,

$$
\sum_{i=1}^{N} \pi_{i j}=n \pi_{j}
$$

Proof. Given the sample index set $A$, define the following indicator function

$$
I_{i}= \begin{cases}1 & \text { if } i \in A \\ 0 & \text { if } i \notin A\end{cases}
$$

In this case, $I_{i}$ is a random variable with $E\left(I_{i}\right)=\pi_{i}$ and $E\left(I_{i} I_{j}\right)=\pi_{i j}$. Furthermore, by the definition of sample size $n$,

$$
\sum_{i=1}^{N} I_{i}=n
$$

Thus, taking expectations of both sides of (2.4), we can obtain (2.1). Also, multiplying both sides of (2.4) and taking the expectations again, we obtain (2.2).

When the sample is obtained from a probability sampling design, an unbiased estimator for the total $Y=\sum_{i=1}^{N} y_{i}$ is given by

$$
\hat{Y}_{\mathrm{HT}}=\sum_{i \in A} \frac{y_{i}}{\pi_{i}}
$$

This is often called Horvitz-Thompson (HT) estimator, which is originally discussed by Horvitz and Thompson (1952) and also by Narain (1951).

The following theorem presents the basic statistical properties of the HT estimator.

Theorem 2.1. The Horvitz-Thompson estimator, given by (2.5), satisfies the following properties:

$$
\begin{aligned}
E\left(\hat{Y}_{\mathrm{HT}}\right) & =Y \\
V\left(\hat{Y}_{\mathrm{HT}}\right) & =\sum_{i=1}^{N} \sum_{j=1}^{N}\left(\pi_{i j}-\pi_{i} \pi_{j}\right) \frac{y_{i}}{\pi_{i}} \frac{y_{j}}{\pi_{j}}
\end{aligned}
$$

Furthermore, for a fixed-size sampling design (i.e., $V(n)=0$ ), we have

$$
V\left(\hat{Y}_{\mathrm{HT}}\right)=-\frac{1}{2} \sum_{i=1}^{N} \sum_{j=1}^{N}\left(\pi_{i j}-\pi_{i} \pi_{j}\right)\left(\frac{y_{i}}{\pi_{i}}-\frac{y_{j}}{\pi_{j}}\right)^{2}
$$




---

Proof. Using the sample indicator function $I_{i}$ defined in (2.3), the HT estimator can be written as

$$
\hat{Y}_{\mathrm{HT}}=\sum_{i=1}^{N} \frac{y_{i}}{\pi_{i}} I_{i}
$$

Treating $\left\{y_{1}, y_{2}, \cdots, y_{N}\right\}$ as fixed and taking expectations with respect to $I_{i}$, we have

$$
\begin{aligned}
\mathrm{E}\left(\hat{Y}_{\mathrm{HT}}\right) & =\sum_{i=1}^{N} \frac{y_{i}}{\pi_{i}} \mathrm{E}\left(I_{i}\right) \\
& =\sum_{i=1}^{N} \frac{y_{i}}{\pi_{i}} \pi_{i}=Y
\end{aligned}
$$

which shows (2.6). Similarly, we have

$$
\begin{aligned}
\mathrm{V}\left(\hat{Y}_{\mathrm{HT}}\right) & =\sum_{i=1}^{N} \sum_{j=1}^{N} \frac{y_{i}}{\pi_{i}} \frac{y_{j}}{\pi_{j}} \operatorname{Cov}\left(I_{i}, I_{j}\right) \\
& =\sum_{i=1}^{N} \sum_{j=1}^{N} \frac{y_{i}}{\pi_{i}} \frac{y_{j}}{\pi_{j}}\left(\pi_{i j}-\pi_{i} \pi_{j}\right)
\end{aligned}
$$

and (2.7) is proved. To show (2.8), define $\Delta_{i j}=\pi_{i j}-\pi_{i} \pi_{j}$ and express (2.8) as

$$
\begin{aligned}
-\frac{1}{2} \sum_{i=1}^{N} \sum_{j=1}^{N} \Delta_{i j}\left(\frac{y_{i}}{\pi_{i}}-\frac{y_{j}}{\pi_{j}}\right)^{2} & =-\sum_{i=1}^{N} \sum_{j=1}^{N} \Delta_{i j}\left(\frac{y_{i}}{\pi_{i}}\right)^{2} \\
& +\sum_{i=1}^{N} \sum_{j=1}^{N} \Delta_{i j} \frac{y_{i}}{\pi_{i}} \frac{y_{j}}{\pi_{j}}
\end{aligned}
$$

Now, using (2.2) and (2.1), we have

$$
\sum_{j=1}^{N} \Delta_{i j}=\sum_{i=1}^{N} \pi_{i j}-\sum_{i=1}^{N} \pi_{i} \pi_{j}=n \pi_{i}-n \pi_{i}=0
$$

Thus, the first term on the right side of the equality in (2.9) becomes zero and (2.8) is established.

Example 2.1. Let $\mathcal{U}=\{1,2,3\}$ be the target population and consider the following sampling design.

$$
P(A)= \begin{cases}0.5 & \text { if } A=\{1,2\} \\ 0.25 & \text { if } A=\{1,3\} \\ 0.25 & \text { if } A=\{2,3\}\end{cases}
$$

In this case, we have $\pi_{1}=0.5+0.25=0.75, \pi_{2}=0.5+0.25=0.75$, and $\pi_{3}=$ $0.25+0.25=0.5$. Thus, the HT estimator for the total is then

$$
\hat{Y}_{\mathrm{HT}}= \begin{cases}y_{1} / 0.75+y_{2} / 0.75 & \text { if } A=\{1,2\} \\ y_{1} / 0.75+y_{3} / 0.5 & \text { if } A=\{1,3\} \\ y_{2} / 0.75+y_{3} / 0.5 & \text { if } A=\{2,3\}\end{cases}
$$




---

Therefore,

$$
\begin{aligned}
\mathrm{E}\left(\hat{Y}_{\mathrm{HT}}\right)= & 0.5\left(y_{1} / 0.75+y_{2} / 0.75\right)+0.25\left(y_{1} / 0.75+y_{3} / 0.5\right) \\
& +0.25\left(y_{2} / 0.75+y_{3} / 0.5\right)=y_{1}+y_{2}+y_{3}
\end{aligned}
$$

and the HT estimator is unbiased for the population total.
The HT estimator provides an unbiased estimate under probability sampling. If $\pi_{i}>0$ does not hold for some elements of the population, the HT estimator cannot be used. Also, the HT estimator is not location-scale invariant. That is, for any constants $a$ and $b$,

$$
\frac{1}{N} \sum_{i \in A} \frac{a+b y_{i}}{\pi_{i}} \neq a+b \frac{1}{N} \sum_{i \in A} \frac{y_{i}}{\pi_{i}}
$$

The variance formula (2.8) was independently discovered by Sen (1953) and Yates and Grundy (1953). Thus, it is often called the Sen-Yates-Grundy(SYG) variance formula. The variance will be minimized when $\pi_{i} \propto y_{i}$. That is, if the first-order inclusion probability is proportional to $y_{i}$, the resulting HT estimator under this sampling design will have zero variance. However, in practice, we cannot construct such a design because we do not know the value of $y_{i}$ in the design stage. If there is an auxiliary variable $x_{i}$ available in the sample frame and $x_{i}$ is believed to be closely related to $y_{i}$, then a sampling design with $\pi_{i} \propto x_{i}$ can lead to a very efficient sampling design.

Now, we discuss an unbiased estimate of the variance of the HT estimator. The variance formula in (2.7) or (2.8) is a population quantity and must be estimated from the sample. Generally speaking, the variance formula is a quadratic function of $y_{i}$ 's in the population. Thus, to estimate the variance, we need to assume a measurable sampling design that satisfies $\pi_{i j}>0$ for all $i$ and $j$. That is, if the parameter of interest is of the form

$$
Q=\sum_{i=1}^{N} \sum_{j=1}^{N} q\left(y_{i}, y_{j}\right)
$$

then, under measurable sampling design, an unbiased estimator of $Q$ is

$$
\hat{Q}=\sum_{i \in A} \sum_{j \in A} \frac{1}{\pi_{i j}} q\left(y_{i}, y_{j}\right)
$$

Thus, an unbiased estimator of variance in (2.7) is

$$
\hat{V}\left(\hat{Y}_{\mathrm{HT}}\right)=\sum_{i \in A} \sum_{j \in A} \frac{\pi_{i j}-\pi_{i} \pi_{j}}{\pi_{i j}} \frac{y_{i}}{\pi_{i}} \frac{y_{j}}{\pi_{j}}
$$

Also, for fixed-sized designs, an unbiased estimator of the SYG variance formula is

$$
\hat{V}\left(\hat{Y}_{\mathrm{HT}}\right)=-\frac{1}{2} \sum_{i \in A} \sum_{j \in A} \frac{\pi_{i j}-\pi_{i} \pi_{j}}{\pi_{i j}}\left(\frac{y_{i}}{\pi_{i}}-\frac{y_{j}}{\pi_{j}}\right)^{2}
$$




---

Another statistical property of the HT estimator is consistency and asymptotic normality, which are established for sufficiently large sample sizes. For an infinite population, the consistency of the sample mean means that the sample mean converges to the population mean in probability. That is, the probability that the absolute difference between the sample mean and the population mean is greater than a given threshold $(\epsilon)$ goes to zero as the sample size increases. That is, for any $\epsilon>0$,

$$
\operatorname{Pr}\left(\left|\bar{y}_{n}-\bar{Y}_{N}\right|>\epsilon\right) \rightarrow 0
$$

as $n \rightarrow \infty$.
In the finite population setup, the finite population is conceptualized to be a sequence of finite population with size $N$ also increasing. The HT estimator of the finite population mean is given by

$$
\bar{Y}_{\mathrm{HT}}=\frac{1}{N} \hat{Y}_{\mathrm{HT}}
$$

and, using Chebyshev inequality,

$$
\operatorname{Pr}\left(\left|\bar{Y}_{\mathrm{HT}}-\bar{Y}_{N}\right|>\epsilon\right) \leq \epsilon^{-2} \mathcal{V}\left(\bar{Y}_{\mathrm{HT}}\right)
$$

Thus, as long as

$$
\lim _{n \rightarrow \infty} \mathcal{V}\left(\bar{Y}_{\mathrm{HT}}\right)=0
$$

the consistency of HT estimator follows. For example, under the simple random sampling that we will study in Chapter 3, we have

$$
\mathcal{V}\left(\bar{Y}_{\mathrm{HT}}\right)=\frac{1}{n}\left(1-\frac{n}{N}\right) S^{2}
$$

Thus, as long as $S^{2}$ is bounded above in probability, condition (2.13) holds and the consistency of the HT estimator follows.

Asymptotic normality is also an important property for obtaining confidence intervals or performing hypothesis testing from the sample. Under some regularity conditions, we can establish

$$
\frac{\hat{Y}_{\mathrm{HT}}-Y}{\sqrt{\hat{\mathcal{V}}\left(\hat{Y}_{\mathrm{HT}}\right)}} \xrightarrow{\mathcal{L}} \mathcal{N}(0,1)
$$

for most sampling designs, where $\xrightarrow{\mathcal{L}}$ denotes convergence in probability. Thus, in this case, the $95 \%$ confidence interval for the population total is computed by

$$
\left(\hat{Y}_{\mathrm{HT}}-1.96 \sqrt{\hat{\mathcal{V}}\left(\hat{Y}_{\mathrm{HT}}\right)}, \hat{Y}_{\mathrm{HT}}+1.96 \sqrt{\hat{\mathcal{V}}\left(\hat{Y}_{\mathrm{HT}}\right)}\right) .
$$

A more in-depth discussion of the asymptotic normality of the HT estimator can be found in Chapter 1 of Fuller (2009).




---

# 2.3 Other parameters 

In the previous section, we have studied the estimation of the total of the finite population, $Y=\sum_{i=1}^{N} y_{i}$. In many practical situations, we estimate other parameters such as population quantiles or domain totals. For example, one may be interested in estimating certain characteristics (such as household income) for a certain age group (for example, over 60) of the householder. At the time of sampling, we do not know the age of the householders. In this case, one can select a sample from the household population and obtain information about the age and income in the sampled households. Let $z_{i}=1$ if $i$ belongs to the particular age group of interest and $z_{i}=0$ otherwise. Also, let $y_{i}$ be the value of the study variable (income in this example) for the element $i$. The domain mean of $y$ can be written as

$$
\theta_{d}=\frac{\sum_{i=1}^{N} z_{i} y_{i}}{\sum_{i=1}^{N} z_{i}}
$$

The indicator variable $z$ is used to identify the domain inclusion in the population. If $z_{i}=1$, then the unit $i$ is eligible for domain estimation.

From (2.14), we can express the domain mean as a ratio of two totals. That is, $\theta_{d}=Y_{d} / D$ where $Y_{d}=\sum_{i=1}^{N} z_{i} y_{i}, D=\sum_{i=1}^{N} z_{i}$. A natural estimator of $\theta_{d}$ is

$$
\hat{\theta}_{d}=\frac{\sum_{i \in \mathcal{A}} z_{i} y_{i} / \pi_{i}}{\sum_{i \in \mathcal{A}} z_{i} / \pi_{i}}
$$

which is the ratio of two corresponding HT estimators. That is, $\hat{\theta}_{d}=$ $\hat{Y}_{d, H T} / \hat{D}_{H T}$ is a special case of the ratio estimator we will study in Chapter 7. Generally speaking, the ratio estimator is not exactly unbiased, but its relative bias can be asymptotically negligible.

In addition to domain estimation, we are often interested in estimating the population distribution. Suppose, for example, that we are interested in estimating the proportion of the population below a certain poverty level. In this case, $\theta_{p}=N^{-1} \sum_{i=1}^{N} I\left(y_{i}<c\right)$ is the parameter of interest, where $c$ is the threshold for the poverty of the household. We can use the theory of HT estimation to estimate $\theta_{p}$ by $\hat{\theta}_{p, H T}=N^{-1} \sum_{i \in \mathcal{A}} \pi_{i}^{-1} I\left(y_{i}<c\right)$. If $N$ is unknown, we use its HT estimator $\hat{N}_{H T}=\sum_{i \in \mathcal{A}} \pi_{i}^{-1}$. Using this idea, we can estimate the entire cumulative distribution function of the population, given by

$$
F(y)=\frac{1}{N} \sum_{i=1}^{N} I\left(y_{i} \leq y\right)
$$

That is, we can use

$$
\hat{F}(y)=\frac{1}{\sum_{i \in \mathcal{A}} \pi_{i}^{-1}} \sum_{i \in \mathcal{A}} \pi_{i}^{-1} I\left(y_{i} \leq y\right)
$$




---

Using $\hat{F}(y)$, we can also perform a quantile estimation. We can define the $q \%$ quantile $(0<q<1)$ of the population as $\theta_{q}=\inf \{y ; F(y) \geq q\}$. Its HT estimator can be written as $\hat{\theta}_{q}=\inf \{y ; \hat{F}(y) \geq q\}$.

Many population parameters can be written as the solution to the population estimating equation

$$
\sum_{i=1}^{N} U\left(\theta ; y_{i}\right)=0
$$

for some estimating function $U\left(\theta ; y_{i}\right)$. For example, the $100 \times q \%$ quantile can be defined as $U(\theta ; y)=I(y<\theta)-q$. To estimate the parameter defined as the solution to

$$
\sum_{i=1}^{N} U\left(\theta ; y_{i}\right)=0
$$

one can use the HT estimation idea to get

$$
\sum_{i \in \mathcal{A}} \pi_{i}^{-1} U\left(\theta ; y_{i}\right)=0
$$

as the estimating equation for $\theta_{N}$ defined through (2.15). Binder (1983) investigated the asymptotic properties of the estimator of the form in (2.16).

# 2.4 Discussion 

In probability sampling, the HT estimator is regarded a gold standard estimator because of its design-unbiasedness. One may wonder whether there is another method to consider. To investigate this, let us consider the following weighted estimator.

$$
\hat{Y}_{w}=\sum_{i \in \mathcal{A}} w_{i} y_{i}
$$

where $w_{i}$ is the fixed weight assigned to unit $i$. The design-expectation of $\hat{Y}_{w}$ is

$$
\mathcal{E}\left(\hat{Y}_{w}\right)=\sum_{i=1}^{N} \pi_{i} w_{i} y_{i}
$$

where $\pi$ is the first-order inclusion probability of unit $i$. To obtain unbiasedness, we require $\sum_{i=1}^{N} \pi_{i} w_{i} y_{i}=\sum_{i=1}^{N} y_{i}$ for all $y_{i}$ in the population, which leads to $w_{i}=\pi_{i}^{-1}$.

Now, suppose that we relax $w_{i}=\pi_{i}^{-1}$ and only require $\sum_{i=1}^{N} \pi_{i} w_{i}=N$. In




---

this case, the bias of $\hat{\bar{Y}}_{w}$ is

$$
\begin{aligned}
\operatorname{Bias}\left(\hat{\bar{Y}}_{w}\right) & =\sum_{i=1}^{N} \pi_{i} w_{i} y_{i}-\sum_{i=1}^{N} y_{i} \\
& =\sum_{i=1}^{N} \pi_{i} w_{i} y_{i}-N^{-1}\left(\sum_{i=1}^{N} \pi_{i} w_{i}\right)\left(\sum_{i=1}^{N} y_{i}\right) \\
& =N \times \operatorname{Cov}\left(q_{i}, y_{i}\right)
\end{aligned}
$$

where $q_{i}=\pi_{i} w_{i}$ and

$$
\operatorname{Cov}\left(q_{i}, y_{i}\right)=\frac{1}{N} \sum_{i=1}^{N}\left(q_{i}-\bar{q}_{N}\right)\left(y_{i}-\bar{y}_{N}\right)
$$

is the population covariance between $q_{i}$ and $y_{i}$, using an operator notation. Thus, $\bar{q}_{N}=N^{-1} \sum_{i=1}^{N} q_{i}=1$, we can express

$$
\begin{aligned}
\frac{\operatorname{Bias}\left(\hat{\bar{Y}}_{w}\right)}{\bar{Y}} & =\operatorname{Cov}\left(q_{i}, y_{i}\right) / \bar{y}_{N} \\
& =\operatorname{Corr}\left(q_{i}, y_{i}\right) \times \mathrm{CV}\left(q_{i}\right) \times \mathrm{CV}\left(y_{i}\right)
\end{aligned}
$$

Note the HT estimator uses $q_{i}=1$ which leads to $\operatorname{Corr}\left(q_{i}, y_{i}\right)=0$ and $\mathrm{CV}\left(q_{i}\right)=0$. Other estimators can also achieve zero bias if $\operatorname{Corr}\left(q_{i}, y_{i}\right)=0$. For example, if $w_{i}=N / n$ and $y_{i}$ is completely independent of $\pi_{i}$, then the bias of $\hat{\bar{Y}}_{w}$ is also zero.

Another class of unbiased estimator is the difference estimator of the form

$$
\hat{Y}_{\text {diff }}=X+\sum_{i \in \mathcal{A}} \frac{1}{\pi_{i}}\left(y_{i}-x_{i}\right)
$$

where $X=\sum_{i=1}^{N} x_{i}$ is the population total of $x_{i}$. The difference estimator is popular in accounting, where $y_{i}$ is the audit value and $x_{i}$ is the book value for the reporting unit $i$. More discussion of the difference estimator will be given in Chapter 8.




---

# 3 

## Simple and systematic sampling designs

### 3.1 Introduction

Before selecting the sample, the population must be divided into parts that are called sampling units, or units. These units must cover the whole population, and they must not overlap in the sense that every element in the population belongs to one and only one unit. Sometimes, the appropriate unit is obvious, as in a population of light bulb, in which the unit is the single bulb. Sometimes there is a choice of unit. When sampling people in a town, the unit might be an individual person, the members of a family, or all persons living in the same city block. In sampling an agricultural crop, the unit might be a field, a farm, or an area of land whose shape and dimensions are at our disposal.

The construction of this list of sampling units, called a sampling frame, is often one of the main practical problems. We use the term direct element sampling to denote sample selection from a frame that directly identifies the individual elements of the population of interest. That is, in element sampling, the sampling unit is equal to the reporting unit. A selection of elements can take place directly from the frame. In this chapter, we first consider a simple type of sampling design in which the first-order inclusion probabilities are equal for every element in the population.

### 3.2 Simple random sampling

Consider the problem of selecting $n$ units from a finite population of size $N$. There are $\binom{N}{n}$ possible samples in this case and the simplest way to select a sample is to select one randomly, that is, to select one realization at random with equal probability. This sampling design is called simple random sampling (SRS) without replacement, or simple random sampling. The sample distribution of the SRS of size $n$ is given by

$$
\mathbb{P}(A)= \begin{cases}\binom{N}{n}^{-1} & \text { if } \quad|A|=n \\ 0 & \text { otherwise }\end{cases}
$$




---

From (3.1), we can obtain the first-order inclusion probability as

$$
\begin{aligned}
\pi_{i} & =P(i \in A) \\
& =\sum_{A \in \mathcal{A}} I(i \in A) P(A) \\
& =\frac{\binom{1}{1}\binom{N-1}{n-1}}{\binom{N}{n}}=\frac{n}{N}
\end{aligned}
$$

Similarly, we can obtain

$$
\pi_{i j}= \begin{cases}N^{-1} n & \text { if } i=j \\ N^{-1}(N-1)^{-1} n(n-1) & \text { if } i \neq j\end{cases}
$$

Thus, the Horvitz-Thompson estimator of the population total $Y=\sum_{i=1}^{N} y_{i}$ can be written

$$
\hat{Y}_{\mathrm{HT}}=\frac{N}{n} \sum_{i \in A} y_{i}=N \bar{y}
$$

and the HT estimator satisfies design-unbiasedness under the SRS design. That is, under SRS, the sample mean $(\bar{y})$ is unbiased for the population mean $\bar{Y}=N^{-1} \sum_{i=1}^{N} y_{i}$. The sampling variance of the HT estimator is, by (2.8),

$$
\begin{aligned}
V\left(\hat{Y}_{\mathrm{HT}}\right) & =\frac{-1}{2} \sum_{i=1}^{N} \sum_{j=1}^{N} \sum_{i \neq j}\left(\pi_{i j}-\pi_{i} \pi_{j}\right)\left(\frac{y_{i}}{\pi_{i}}-\frac{y_{j}}{\pi_{j}}\right)^{2} \\
& =\frac{1}{2} \frac{N}{n} \frac{N-n}{N(N-1)} \sum_{i=1}^{N} \sum_{j=1}^{N}\left(y_{i}-y_{j}\right)^{2}
\end{aligned}
$$

Since

$$
\begin{aligned}
\sum_{i=1}^{N} \sum_{j=1}^{N}\left(y_{i}-y_{j}\right)^{2} & =\sum_{i=1}^{N} \sum_{j=1}^{N}\left(y_{i}-\bar{Y}+\bar{Y}-y_{j}\right)^{2} \\
& =2 N \sum_{i=1}^{N}\left(y_{i}-\bar{Y}\right)^{2}
\end{aligned}
$$

we can obtain

$$
V\left(\hat{Y}_{\mathrm{HT}}\right)=\frac{N^{2}}{n} \frac{N-n}{N} S^{2}
$$




---

where

$$
\begin{aligned}
S^{2} & =\frac{1}{N-1} \sum_{i=1}^{N}\left(y_{i}-\bar{Y}\right)^{2} \\
& =\frac{1}{2} \frac{1}{N(N-1)} \sum_{i=1}^{N} \sum_{j=1}^{N}\left(y_{i}-y_{j}\right)^{2}
\end{aligned}
$$

Thus, we can establish

$$
\mathcal{V}\left(\bar{y}_{n}\right)=\frac{1}{n} \frac{N-n}{N} S^{2}
$$

For the special case of $n=1$, (3.5) becomes

$$
\frac{1}{N} \sum_{i=1}^{N}\left(y_{i}-\bar{Y}\right)^{2}
$$

which is often called population variance, denoted by $\sigma_{y}^{2}$. That is, $\sigma_{y}^{2}$ can be understood as the sampling variance of the single sample observation under SRS with size $n=1$. Using the population variance, the variance formula in (2.14) can be written as

$$
\mathcal{V}\left(\bar{y}_{n}\right)=\frac{1}{n}\left(1-\frac{n-1}{N-1}\right) \sigma_{y}^{2}
$$

where $1-(N-1)^{-1}(n-1)$ is the variance reduction factor due to withoutreplacement sampling and it is often called FPC (Finite population correction) term. The FPC term disappears under simple random sampling with replacement.

Now, consider variance estimation of the HT estimator under SRS. Since SRS is a fixed-sized sampling design, we can use SYG variance estimation formula in (2.12) to get

$$
\begin{aligned}
\hat{\mathcal{V}}\left(\hat{Y}_{\mathrm{HT}}\right) & =\frac{-1}{2} \sum_{i \in \mathcal{A}} \sum_{j \in \mathcal{A}} \frac{\left(\pi_{i j}-\pi_{i} \pi_{j}\right)}{\pi_{i j}}\left(\frac{y_{i}}{\pi_{i}}-\frac{y_{j}}{\pi_{j}}\right)^{2} \\
& =\frac{1}{2} \frac{N}{n} \frac{N-n}{n(n-1)} \sum_{i \in \mathcal{A}} \sum_{j \in \mathcal{A}}\left(y_{i}-y_{j}\right)^{2}
\end{aligned}
$$

Similarly to (3.4), we can show

$$
\sum_{i \in \mathcal{A}} \sum_{j \in \mathcal{A}}\left(y_{i}-y_{j}\right)^{2}=2 n \sum_{i \in \mathcal{A}}\left(y_{i}-\bar{y}\right)^{2}
$$

Thus, we can obtain

$$
\hat{\mathcal{V}}\left(\hat{Y}_{\mathrm{HT}}\right)=\frac{N^{2}}{n} \frac{N-n}{N} s^{2}
$$




---

where

$$
s^{2}=\frac{1}{n-1} \sum_{i \in \mathcal{A}}\left(y_{i}-\bar{y}\right)^{2}
$$

Thus, under SRS, we have

$$
\mathrm{E}\left(s^{2}\right)=S^{2}
$$

If $y$ is dichotomous, taking either 1 or 0 , the population mean of $y$ is equal to the proportion of $y=1$ in the population, namely $P=\operatorname{Pr}(y=1)$. In this case, we can obtain $\sigma_{y}^{2}=P(1-P)$ and the variance of the HT estimator $\hat{P}=\bar{y}$ of $P$ is then equal to

$$
\mathrm{V}(\hat{P})=\frac{1}{n}\left(1-\frac{n}{N}\right) \frac{N}{N-1} P(1-P)
$$

and its unbiased estimator is

$$
\hat{\mathrm{V}}(\hat{P})=\frac{1}{n-1}\left(1-\frac{n}{N}\right) \hat{P}(1-\hat{P})
$$

We now discuss the determination of the sample size $n$ under simple random sampling. Under the significant level $\alpha$, the margin of error, denoted by $d$, is defined to satisfy

$$
\operatorname{Pr}\{|\hat{\theta}-\theta| \leq d\}=1-\alpha
$$

That is, $d$ is half of the length in the confidence interval for $\theta$, Thus, solving

$$
z_{\alpha / 2} \sqrt{\frac{1}{n}\left(1-\frac{n}{N}\right) S^{2}} \leq d
$$

with respect to $n$ to get

$$
n \geq \frac{S^{2}}{\left(d / z_{\alpha / 2}\right)^{2}+S^{2} / N}
$$

which provide the lower bound of the desired sample size for given $d$. However, since we usually do not know $S^{2}$ before the sample observation, we need an estimate for $S^{2}$, from a pilot survey or a similar survey in the same population. In many public opinion surveys, $y$ is a dichotomous variable and the maximum value of $S^{2}$ in this case is $1 / 4$ and (3.10) becomes

$$
n \geq 0.25\left(\frac{z_{\alpha / 2}}{d}\right)^{2}
$$

For $\alpha=0.05, z_{\alpha / 2} \doteq 2$ and the above inequality reduces to $n \geq d^{-2}$.




---

# 3.3 Implementation of simple random sampling 

To implement the SRS method in practice, one may consider a draw-bydraw method as follows: In the first draw, select one element at random from the entire population $\mathcal{U}$ with probability $1 / N$. Let $k_{1}$ be the index of the element selected from the first draw. In the second draw, select one element at random from $\mathcal{U}-\left\{k_{1}\right\}$ with probability $1 /(N-1)$. Let $k_{2}$ be the index of the element selected from the second draw. We can continue the process until the $n$-th draw. In the $n$-th draw, select one element at random from $\mathcal{U}-\left\{k_{1}, \cdots, k_{n-1}\right\}$ with probability $(N-n+1)^{-1}$.

In this draw-by-draw procedure, the probability of selecting $n$ individuals $k_{1}, \cdots, k_{n}$ in order is $(N-n)!/ N$ !, and there are $n$ ! ways to order $\left\{k_{1}, \cdots, k_{n}\right\}$. Thus, the probability of selecting a sample $\mathcal{A}$ of $n$ units is $n$ ! times $(N-$ $n)!/ N!$, which is equal to $\binom{N}{n}^{-1}$. Such a draw-by-draw method may be quite cumbersome if $N$ is very large, as it would require numbering the elements in the population in advance and then repeating the process $n$ times.

Another method of drawing a sample for SRS is the so-called random sorting method. The idea is to sort the population in a random order and then take the first $n$ units from the ordered population as the final sample. Sunter (1977) showed that this random sorting method indeed implements simple random sampling. To see this, let $u_{i}$ be the random number for unit $i$, generated from the $U(0,1)$ distribution. To select a particular sample $\mathcal{A}=\{1, \cdots, n\}$ under the descending order sorting, the largest number among $\left\{u_{n+1}, \cdots, u_{N}\right\}$ should be less than the smallest number among $\left\{u_{1}, \cdots, u_{n}\right\}$.

Let $X$ be the largest number among $\left\{u_{n+1}, \cdots, u_{N}\right\}$. Note that the CDF of $X$ is

$$
\begin{aligned}
F(x) & =P\left(u_{n+1} \leq x, \cdots, u_{N} \leq x\right) \\
& =\prod_{i=n+1}^{N} P\left(u_{i} \leq x\right) \\
& =x^{N-n}
\end{aligned}
$$

for $0<x<1$. The probability of selecting $\mathcal{A}=\{1, \cdots, n\}$ is equal to

$$
\begin{aligned}
P(\mathcal{A}) & =\int_{0}^{1}\left\{\prod_{i=1}^{n} P\left(u_{i}>x\right)\right\} d F(x) \\
& =\int_{0}^{1}(1-x)^{n}(N-n) x^{N-n-1} d x \\
& =\frac{n!(N-n)!}{N!}=\frac{1}{\binom{N}{n}}
\end{aligned}
$$

Thus, the random sorting method indeed implements the simple random sampling. The sorting algorithm can be computationally costly if $N$ is large.




---

We now consider a different sampling method that does not require reading the population list in advance before sampling. The selection-rejection method allows the selection of SRS in a single pass through the population list, but we need to know the population size $N$ and the sample size $n$. The selectionrejection method can be described as follows:
[Step 0] Start with $k=1$.
[Step 1] Generate $u_{k} \sim U(0,1)$ independently.
[Step 2] Check if

$$
u_{k}<\frac{n-\sum_{j=1}^{k-1} I_{j}}{N+1-k}
$$

If yes, select $k+1$ into sample and set $I_{k}=1$. Otherwise, set $I_{k}=0$.
[Step 3] Set $k=k+1$. If $\sum_{j=1}^{k} I_{j}<n$ then goto [Step 1]. Otherwise Stop.
Note that

$$
\mathrm{P}\left(k \in A \mid I_{1, \cdots, k-1}\right)=\frac{n-\sum_{j=1}^{k-1} I_{j}}{N+1-k}
$$

for $k=1, \ldots, N$. Note that $n-\sum_{j=1}^{k-1} I_{j}$ is the remaining sample size and $N+1-k$ is the remaining population size at the $k$-th pass. Thus, writing $n_{k-1}=\sum_{j=1}^{k-1} I_{j}$,

$$
\begin{aligned}
\mathrm{P}(A) & =\left[\prod_{k \in A} \frac{n-n_{k-1}}{N-(k-1)}\right] \times\left[\prod_{k \in A^{c}}\left\{1-\frac{n-n_{k-1}}{N-(k-1)}\right\}\right] \\
& =(\{\prod_{k=1}^{N}(N-k+1)\})^{-1}\left[\prod_{k \in A}\left(n-n_{k-1}\right)\right]\left[\prod_{k \in A^{c}}\left(N-k+1-n+n_{k-1}\right)\right] \\
& =(\mathrm{N}!)^{-1} n!(N-n)!=\frac{1}{\binom{N}{n}}
\end{aligned}
$$

The selection-rejection method implements simple random sampling, but the population size $N$ is needed to compute the selection probability.

McLeod and Bellhouse (1983) proposed a novel method for implementing the SRS in a single pass through the list of records, and does not require a known population size $N$. The method is later named the reservoir sampling method (Vitter, 1985) in the sense that $n$ sample elements are selected in a reservoir and then replaced if the next element in the population is selected. In the proposed reservoir method, the first $n$ elements of the population are stored in the reservoir. The $k$-th element $(k=n+1, \cdots, N)$ is selected in the reservoir with probability $n / k$ and then one of the $n$ elements is removed from the reservoir with equal probability. The elements in the reservoir that remain after the final selection are the elements in the final sample. Note that




---

the population size is not necessarily known. You can stop any time point of the process, then you will obtain a simple random sample from the finite population considered up to that time point.

To explain the reservoir sampling, let $U_{k}=\{1,2, \cdots, k\}$ be the finite population up to element $k$. Let $A_{k}$ be the index set of the sample elements selected from the reservoir sampling. The probability of selecting element $j(<k)$ in the sample can be written as

$$
\begin{aligned}
P\left(j \in A_{k} \mid U_{k}\right)= & P\left(j \in A_{k-1} \mid U_{k-1}\right) P\left(j \in A_{k} \text { and } k \in A_{k} \mid U_{k}, A_{k-1}\right) \\
& +P\left(j \in A_{k-1} \mid U_{k-1}\right) P\left(k \notin A_{k} \mid U_{k}, A_{k-1}\right)
\end{aligned}
$$

Now, by the reservoir sampling mechanism, we obtain

$$
\begin{aligned}
P\left(j \in A_{k} \text { and } k \in A_{k} \mid U_{k}, A_{k-1}\right) & =P\left(j \in A_{k} \mid U_{k}, A_{k-1}\right) P\left(k \in A_{k} \mid U_{k}, A_{k-1}\right) \\
& =\frac{n-1}{n} \times \frac{n}{k}
\end{aligned}
$$

and

$$
P\left(k \notin A_{k} \mid U_{k}, A_{k-1}\right)=1-\frac{n}{k}
$$

Thus, (3.12) reduces to

$$
P\left(j \in A_{k} \mid U_{k}\right)=P\left(j \in A_{k-1} \mid U_{k-1}\right) \times\left(\frac{k-1}{k}\right)
$$

For $k=n, P\left(j \in A_{k} \mid U_{k}\right)=1$. Thus, by (3.13), we obtain

$$
P\left(j \in A_{k} \mid U_{k}\right)=\frac{n}{k}
$$

which is equal to the first-inclusion probability of the SRS of size $n$ from the finite population of size $k$.

# 3.4 Simple random sampling with replacement 

We now consider the sampling design where the sample of size $n$ is selected with equal probability with replacement. The realized sample size can be smaller than $n$ because the sample is selected with replacement, and thus allows for duplication. In the $k$-th sample draw, where $k=1, \cdots, n$, the $i$ th element in the population is selected with probability $1 / N$. Let $z_{1}$ be the realized value of $y_{i}$ in the first draw. The probability distribution of $z_{1}$ is given by

$$
z_{1}= \begin{cases}y_{1} & \text { with probability } 1 / N \\ y_{2} & \text { with probability } 1 / N \\ \vdots \\ y_{N} & \text { with probability } 1 / N\end{cases}
$$




---

Similarly, let $z_{k}$ be the realized value of $y_{i}$ in the $k$-th draw. The withreplacement sampling makes $z_{1}, \cdots, z_{n}$ be independently and identically distributed (IID). The mean and variance of $z_{1}$ is

$$
\begin{aligned}
\mathrm{E}\left(z_{1}\right) & =N^{-1} \sum_{i=1}^{N} y_{i}=\bar{Y} \\
\mathrm{~V}\left(z_{1}\right) & =N^{-1} \sum_{i=1}^{N}\left(y_{i}-\bar{y}_{N}\right)^{2}=\sigma_{y}^{2}
\end{aligned}
$$

Now, since $z_{1}, \cdots, z_{n}$ are IID with mean $\bar{Y}$, we can consider the following class of estimators:

$$
\hat{\bar{Y}}_{w}=\sum_{i=1}^{n} w_{i} z_{i}
$$

where $\sum_{i=1}^{n} w_{i}=1$. Note that $\hat{\bar{Y}}_{w}$ is unbiased regardless of the choice of $w_{i}$. To find the best choice of $w_{i}$ in the sense of minimizing its variance, we introduce the following lemma.

Lemma 3.1. Let $X_{1}, \cdots, X_{n}$ be $n$ IID realization with $\mathrm{E}\left(X_{i}\right)=\mu$ and $\mathrm{V}\left(X_{i}\right)=$ $\sigma_{i}^{2}$. Let $w_{1}, \cdots, w_{n}$ be the fixed constants such that $\sum_{i=1}^{n} w_{i}=1$. The weighted estimator $\hat{\mu}_{w}=\sum_{i=1}^{n} w_{i} X_{i}$ achieves the minimum at

$$
w_{i}^{*}=\frac{\sigma_{i}^{-2}}{\sum_{k=1}^{n} \sigma_{k}^{-2}}
$$

Proof. The variance of $\hat{\mu}_{w}$ is $\mathrm{V}\left(\hat{\mu}_{w}\right)=\sum_{i=1}^{n} w_{i}^{2} \sigma_{i}^{2}$. Using Cauchy-Schwarz inequality, we obtain

$$
\left(\sum_{i=1}^{n} w_{i}^{2} \sigma_{i}^{2}\right)\left(\sum_{i=1}^{n} \sigma_{i}^{-2}\right) \geq\left(\sum_{i=1}^{n} w_{i}\right)^{2}
$$

Since $\sum_{i=1}^{n} w_{i}=1$, we have

$$
\sum_{i=1}^{n} w_{i}^{2} \sigma_{i}^{2} \geq \text { Constant }
$$

and the variance is minimized when $w_{i} \sigma_{i} \propto \sigma_{i}^{-1}$, which is equivalent to $w_{i} \propto$ $\sigma_{i}^{-2}$.

Thus, the best linear unbiased estimator of the population mean $\bar{Y}$ is the sample mean $\bar{z}=n^{-1} \sum_{i=1}^{n} z_{i}$ and its variance is

$$
\mathrm{V}(\bar{z})=\frac{1}{n} \sigma_{y}^{2}
$$




---

The variance formula in (3.6) under SRS is smaller than the variance formula in (3.18) under SRS with replacement. The SRS with replacement is less efficient because the expected value of the actual sample size is smaller as it allows for duplication due to with-replacement sampling.

For variance estimation, since $z_{1}, \cdots, z_{n}$ are IID, the sample variance

$$
s_{z}^{2}=\frac{1}{n-1} \sum_{i=1}^{n}\left(z_{i}-\bar{z}\right)^{2}
$$

can be used to estimate the population variance. Since $z_{1}, z_{2}, \ldots, z_{n}$ are IID with $\left(\bar{Y}, \sigma_{y}^{2}\right)$, we have

$$
\mathrm{E}\left(s_{z}^{2}\right)=\sigma_{y}^{2}
$$

and the variance estimator of $\bar{z}$ is

$$
\hat{V}(\bar{z})=\frac{1}{n} s_{z}^{2}
$$

The SRS with replacement is a special case of the PPS sampling that will be covered in Section 5.2.

# 3.5 Bernoulli Sampling 

Bernoulli sampling design is a sampling design based on independent Bernoulli trials for the element in the population. That is, the sample indicator function follows

$$
I_{i} \stackrel{\text { i.i.d. }}{\sim} \operatorname{Bernoulli}(\pi), \quad i=1,2, \cdots, N
$$

where $\pi$ is the first order inclusion probability for each unit. We can express $\pi=n_{0} / N$ where $n_{0}$ is the expected sample size determined before sample selection. In this Bernoulli sampling, the (realized) sample size follows a binomial distribution $\operatorname{Bin}(N, \pi)$ and the fact that the realized sample size is a random variable can reduce the efficiency of the resulting HT estimator.

Under this Bernoulli sampling, the HT estimator of the population mean is

$$
\widehat{\bar{Y}}_{\mathrm{HT}}=\frac{1}{N} \sum_{i \in \mathcal{A}} \frac{y_{i}}{\pi_{i}}=\frac{n}{n_{0}} \bar{y}
$$

Thus, the HT estimator of the mean is not necessarily equal to the mean of the sample. The asymptotic variance of the sample mean is

$$
\mathrm{V}(\bar{y})=\frac{1}{n_{0}}\left(1-\frac{n_{0}}{N}\right) S^{2}
$$




---

On the other hand, the variance of the HT estimator of the mean is

$$
\mathcal{V}\left(\widehat{\bar{Y}}_{\mathrm{HT}}\right)=\frac{1}{n_{0}}\left(1-\frac{n_{0}}{N}\right) \frac{1}{N} \sum_{i=1}^{N} y_{i}^{2}
$$

Thus, the sample mean is more efficient than the HT estimator in (3.22).

Example 3.1. Suppose that we are interested in estimating the proportion of students who pass a certain test in a university and there are $N=600$ of students who took the test in the university. Using a Bernoulli sampling with $\pi=1 / 6$, the sample size $n=90$ is realized. Among the 90 sample students, 60 students are found to have passed. In this case, the HT estimator of the mean is $0.9 \times 2 / 3$, which is different from the actual passing rate $2 / 3$ in the sample. In the extreme case, even if all the students pass the exam, the HT estimate is still 0.9 .

If the sampling procedure is such that we repeat the Bernoulli sampling until the realized sample size $n$ is equal to the expected sample size $n_{0}$, then the resulting sampling procedure is exactly equal to the SRS of size $n_{0}$. To show this result, note that

$$
\operatorname{Pr}\left(I_{1}, I_{2}, \cdots, I_{N} \mid \sum_{i=1}^{N} I_{i}=n_{0}\right)=\frac{\operatorname{Pr}\left(I_{1}, I_{2}, \cdots, I_{N}, \sum_{i=1}^{N} I_{i}=n_{0}\right)}{\operatorname{Pr}\left(n=n_{0}\right)}
$$

Since

$$
\begin{aligned}
& \operatorname{Pr}\left(I_{1}, I_{2}, \cdots, I_{N}, \sum_{i=1}^{N} I_{i}=n_{0}\right) \\
& = \begin{cases}\prod_{i=1}^{N} p^{I_{i}}(1-p)^{1-I_{i}} & \text { if } \sum_{i=1}^{N} I_{i}=n_{0} \\
0 & \text { otherwise }\end{cases} \\
& = \begin{cases}p^{n_{0}}(1-p)^{N-n_{0}} & \text { if } \sum_{i=1}^{N} I_{i}=n_{0} \\
0 & \text { otherwise }\end{cases}
\end{aligned}
$$

and

$$
\operatorname{Pr}\left(n=n_{0}\right)=\binom{N}{n_{0}} p^{n_{0}}(1-p)^{N-n_{0}}
$$

the conditional density in (3.23) is equal to the sampling design (3.1) under SRS of size $n_{0}$.

# 3.6 Systematic sampling 

Systematic sampling is an alternative method of selecting an equal probability sample, but it offers several practical advantages, particularly its simplicity of execution. In systematic sampling, a first element is drawn at random




---

with equal probability, among the first $G$ elements in the population list. The positive integer $G$ is fixed in advance and is called the sampling interval. The rest of the sample is determined by systematically taking every $G$-th element thereafter, until the end of the list. Thus, there are only $G$ possible samples, each having the same probability of being selected. The simplicity of having only one random draw is a great advantage. For example, to select a sample of 200 students from the list of 20,000 students at Iowa State University, we first select one element among the first 100 students. Suppose that the random integer we choose is 73 . Then the students numbered $73,173,273, \cdots, 19,973$ would be in the sample.

For a more formal definition of systematic sampling, let $G$ be the fixed sampling interval and let $n$ be the integer part of $N / G$, where $N$ is the population size. Then,

$$
N=n \cdot G+c
$$

where the integer $c$ satisfies $0 \leq c<G$. In systematic sampling, we first select one integer from $\{1,2 \cdots, G\}$ with equal probability $1 / G$. If $r$ is selected from the selection, the final sample of systematic sampling is

$$
\mathcal{A}_{r}= \begin{cases}\{r, r+G, r+2 G, \cdots, r+(n-1) G\} & \text { if } c<r \leq G \\ \{r, r+G, r+2 G, \cdots, r+n G\} & \text { if } 1 \leq r \leq c\end{cases}
$$

The first order inclusion probability for each unit is $\pi_{i}=1 / G$ but the second order inclusion probability is

$$
\pi_{i j}= \begin{cases}1 / G & \text { if } j=i+k G \text { for some integer } k \\ 0 & \text { otherwise. }\end{cases}
$$

That is, systematic sampling can be viewed as selecting one cluster at random among the $a$ possible clusters. In this case, the second-order inclusion probability of two units is positive only when the two units belong to the same cluster. Thus, an unbiased estimator of the variance of the HT estimator does not exist. Wolter (1984) discuss variance estimation under systematic sampling. In addition, the efficiency of systematic sampling depends on the way the list is sorted. Such a concept can be investigated using the intracluster correlation coefficient in cluster sampling, which will be covered in Chapter 6.

In systematic sampling, the finite population $\mathcal{U}$ is partitioned into $G$ groups

$$
\mathcal{U}=\mathcal{U}_{1} \cup \mathcal{U}_{2} \cup \cdots \cup \mathcal{U}_{G}
$$

where $\mathcal{U}_{i}$ are mutually disjoint. The population total is then expressed as

$$
Y=\sum_{i \in \mathcal{U}} y_{i}=\sum_{r=1}^{G} \sum_{k \in \mathcal{U}_{r}} y_{k}=\sum_{r=1}^{G} t_{r}
$$

where $t_{r}=\sum_{k \in \mathcal{U}_{r}} y_{k}$. Thus, in estimating the total, the finite population can be treated as a population with $a$ elements with measurements $t_{1}, \cdots, t_{G}$.




---

The HT estimator can be written

$$
\hat{Y}_{\mathrm{HT}}=\frac{t_{r}}{1 / G}=G \sum_{k \in A} y_{k}
$$

if $A=U_{r}$. Since we select SRS from the population of $G$ elements $\left\{t_{1}, \cdots, t_{G}\right\}$, the variance is

$$
\mathbb{V}\left(\hat{Y}_{\mathrm{HT}}\right)=G^{2} \frac{1}{\left(1-\frac{1}{G}\right)} S_{t}^{2}
$$

where

$$
S_{t}^{2}=\frac{1}{G-1} \sum_{r=1}^{G}\left(t_{r}-\bar{t}\right)^{2}
$$

and $\bar{t}=\sum_{r=1}^{G} t_{r} / G$.
Now, assuming $N=n \cdot G$

$$
\mathbb{V}\left(\hat{Y}_{\mathrm{HT}}\right)=\frac{G(G-1) S_{t}^{2}}{n^{2} G}=\sum_{r=1}^{G}\left(\bar{y}_{r}-\bar{y}_{u}\right)^{2}
$$

where $\bar{y}_{r}=t_{r} / n$ and $\bar{y}_{u}=\bar{t} / n$. Since $U=\cup_{r=1}^{G} U_{r}$, we can use the ANOVA decomposition to get

$$
\begin{aligned}
S S T & =\sum_{k \in U}\left(y_{k}-\bar{y}_{u}\right)^{2}=\sum_{r=1}^{G} \sum_{k \in U_{r}}\left(y_{k}-\bar{y}_{u}\right)^{2} \\
& =\sum_{r=1}^{G} \sum_{k \in U_{r}}\left(y_{k}-\bar{y}_{r}\right)^{2}+n \sum_{r=1}^{G}\left(\bar{y}_{r}-\bar{y}_{u}\right)^{2} \\
& =S S W+S S B
\end{aligned}
$$

Thus, the variance can be written

$$
\mathbb{V}\left(\hat{Y}_{\mathrm{HT}}\right)=n G \cdot S S B=N \cdot S S B=N(S S T-S S W)
$$

If $S S B$ is small, then $\bar{y}_{r}$ are more similar and $\mathbb{V}\left(\hat{Y}_{\mathrm{HT}}\right)$ is small. If the $S S W$ is small, then $\mathbb{V}\left(\hat{Y}_{\mathrm{HT}}\right)$ is large.

To compare the systematic sampling and SRS in terms of variance, note that

$$
\begin{aligned}
\mathbb{V}_{\mathrm{SRS}}\left(\hat{Y}_{\mathrm{HT}}\right) & =\frac{N^{2}}{n}\left(1-\frac{n}{N}\right) \frac{1}{N-1} \sum_{k=1}^{N}\left(y_{k}-\bar{Y}_{N}\right)^{2} \\
\mathbb{V}_{\mathrm{SYS}}\left(\hat{Y}_{\mathrm{HT}}\right) & =n^{2} G \sum_{r=1}^{G}\left(\bar{y}_{r}-\bar{y}_{u}\right)^{2}
\end{aligned}
$$




---

We can compare the variance by making additional assumptions about the finite population. Cochran (1946) introduced superpopulation model which the finite population is believed to be generated. The superpopulation model is an assumption about the finite population, and it quantifies the characteristics of the finite population in terms of a smaller number of parameters.

If the finite population is ordered randomly, then we may use an IID model, denoted by $\zeta:\left\{y_{k}\right\} \stackrel{\text { i.i.d. }}{\sim}\left(\mu, \sigma^{2}\right)$. In this case, we can obtain

$$
\begin{aligned}
\mathbb{E}_{\zeta}\left\{\mathbb{V}_{\mathrm{SRS}}\left(\hat{Y}_{\mathrm{HT}}\right)\right\} & =\frac{N^{2}}{n}\left(1-\frac{n}{N}\right) \sigma^{2} \\
\mathbb{E}_{\zeta}\left\{\mathbb{V}_{\mathrm{SYS}}\left(\hat{Y}_{\mathrm{HT}}\right)\right\} & =\frac{N^{2}}{n}\left(1-\frac{n}{N}\right) \sigma^{2}
\end{aligned}
$$

Thus, the model expectations for the design variances are the same in the IID model.

Example 3.2. Consider a finite population of size $N$ with linear trend. That is, we assume the following superpopulation model

$$
\mathbb{E}_{\zeta}\left(y_{k}\right)=\beta_{0}+\beta_{1} k, \quad \mathbb{V}_{\zeta}\left(y_{k}\right)=\sigma^{2}
$$

To compute the model expectation of the design variance, we first note that, under the independence model $\zeta$ with $\mathbb{E}_{\zeta}\left(y_{i}\right)=\mu_{i}$ and $\mathbb{V}_{\zeta}\left(y_{i}\right)=\sigma^{2}$, we can derive

$$
\mathbb{E}_{\zeta}\left(S^{2}\right)=\frac{1}{N-1} \sum_{i=1}^{N}\left(\mu_{i}-\bar{\mu}_{N}\right)^{2}+\sigma^{2}
$$

where $\bar{\mu}_{N}=N^{-1} \sum_{i=1}^{N} \mu_{i}$. Thus, under (3.24), we obtain

$$
\begin{aligned}
\mathbb{E}_{\zeta}\left(S^{2}\right) & =\frac{\beta_{1}^{2}}{N-1} \sum_{i=1}^{N}\left(k-\frac{N+1}{2}\right)^{2}+\sigma^{2} \\
& =\frac{\beta_{1}^{2}}{N} \frac{N-1}{N^{2}-1} \frac{12}{12}+\sigma^{2} \\
& =\frac{N(N+1) \beta_{1}^{2}}{12}+\sigma^{2}
\end{aligned}
$$

and so

$$
\mathbb{E}_{\zeta}\left\{\mathbb{V}_{\mathrm{SRS}}\left(\widehat{\bar{Y}}_{\mathrm{HT}}\right)\right\}=\frac{1}{n}\left(1-\frac{n}{N}\right)\left\{\frac{N(N+1) \beta_{1}^{2}}{12}+\sigma^{2}\right\}
$$

Now, to compute the model expectation of

$$
\mathbb{V}_{\mathrm{SYS}}\left(\widehat{\bar{Y}}_{\mathrm{HT}}\right)=\frac{1}{G} \sum_{i=r}^{G}\left(\bar{y}_{r}-\bar{y}_{i}\right)^{2}=G^{-1} \overline{S_{z}^{2}}
$$




---

where

$$
S_{\mathrm{z}}^{2}=\frac{1}{G-1} \sum_{r=1}^{G}\left(z_{r}-\bar{z}_{G}\right)^{2}
$$

$z_{r}=\bar{y}_{r}$ and $\bar{z}_{G}=G^{-1} \sum_{r=1}^{G} z_{r}$, we can obtain, similarly to (3.25),

$$
\mathrm{E}_{\zeta}\left(S_{\mathrm{z}}^{2}\right)=\frac{1}{G-1} \sum_{r=1}^{G}\left\{\mathrm{E}_{\zeta}\left(z_{r}\right)-\mathrm{E}_{\zeta}\left(\bar{z}_{G}\right)\right\}^{2}+\mathrm{V}_{\zeta}(z)
$$

Since $z_{r}=n^{-1} \sum_{k=1}^{n} y_{r+(k-1) G}$ for $r=1, \cdots, G$, we have

$$
\mathrm{E}\left(z_{r}\right)=\frac{1}{n} \sum_{k=1}^{n}\left\{\beta_{0}+\beta_{1} r+\beta_{1}(k-1) G\right\}=\beta_{0}+\beta_{1} r+\beta_{1} G \frac{n(n-1)}{2}
$$

and $\mathrm{V}_{\zeta}\left(z_{r}\right)=\sigma^{2} / n$. Thus,

$$
\begin{aligned}
\mathrm{E}_{\zeta}\left(S_{\mathrm{z}}^{2}\right) & =\frac{\beta_{1}^{2}}{G-1} \sum_{r=1}^{G}\left\{r-\frac{G+1}{2}\right\}^{2}+\frac{\sigma^{2}}{n} \\
& =\frac{\beta_{1}^{2}}{G} \frac{G^{2}-1}{12}+\frac{\sigma^{2}}{n}
\end{aligned}
$$

and

$$
\begin{aligned}
\mathrm{E}_{\zeta}\left\{\mathrm{V}_{\mathrm{SYS}}\left(\widehat{\bar{Y}}_{\mathrm{HT}}\right)\right\} & =\frac{G-1}{G}\left\{\frac{\beta_{1}^{2} G(G+1)}{12}+\frac{\sigma^{2}}{n}\right\} \\
& =\frac{1}{n}\left(1-\frac{n}{N}\right)\left\{\frac{N(N+n) \beta_{1}^{2}}{12 n}+\sigma^{2}\right\}
\end{aligned}
$$

Therefore, comparing (3.26) and (3.27), we can establish that

$$
\mathrm{E}_{\zeta}\left\{\mathrm{V}_{\mathrm{SYS}}\left(\widehat{\bar{Y}}_{\mathrm{HT}}\right)\right\} \leq \mathrm{E}_{\zeta}\left\{\mathrm{V}_{\mathrm{SRS}}\left(\widehat{\bar{Y}}_{\mathrm{HT}}\right)\right\}
$$

# 3.7 Entropy for sampling designs 

We now introduce a concept which gives a characterization of sampling designs.

Definition 3.1. For a sample design $p(\cdot)$, the entropy of $p(\cdot)$ is the quantity

$$
\mathcal{I}(p)=-\sum_{A \in \mathcal{A}} p(A) \log \{p(A)\}
$$




---

Roughly speaking, entropy is a measure of the randomness of a probability distribution. The larger the entropy, the more randomly the sample is selected. The following lemma shows that the Bernoulli sampling design with $\pi=$ $1 / 2$ is the maximum entropy sampling design among all possible probability sampling designs.

Lemma 3.2. The maximum entropy design in $\mathcal{A}=\{A ; A \subset U\}$ is $P(A)=$ $2^{-N}$, for all $A \subset U$.

Proof. We are interested in maximizing $I(p)$ in (5.6) subject to

$$
\sum_{A \in \mathcal{A}} p(A)=1
$$

Using Lagrange multiplier method, we have only to find the maximizer of

$$
Q(p, \lambda)=-\sum_{A \in \mathcal{A}} p(A) \log \{p(A)\}+\lambda\left(\sum_{A \in \mathcal{A}} p(A)-1\right)
$$

Solving

$$
\frac{\partial}{\partial p(A)} Q(p, \lambda)=0
$$

we obtain

$$
p(A)=\exp (\lambda-1)
$$

Now, inserting (3.30) into (3.29), we get

$$
\sum_{A \in \mathcal{A}} p(A)=2^{N} \exp (\lambda-1)=1
$$

Therefore, we obtain $p(A)=2^{-N}$ for all $A \in \mathcal{A}$.
According to Lemma 3.2, the maximum entropy is the entropy of the Bernoulli sampling design with $\pi=1 / 2$, which is equal to

$$
I\left(p^{*}\right)=-\sum_{A \in \mathcal{A}} p^{*}(A) \log p^{*}(A)=N \log 2
$$

This design is the most random among all sampling designs in the finite population of size $N$.

The following theorem proves that simple random sampling without replacement is also a maximum entropy sampling design among the class of fixed-sample-size designs.

Theorem 3.1. The maximum entropy design with fixed sample size $n$ is the simple random sampling design without replacement with a fixed sample size.




---

Proof. Let $\mathcal{A}_{n}$ be the set of all possible samples of size $n$. Using the Lagrange multiplier method, we only have to find the maximizer of

$$
Q(\mathbf{p}, \lambda)=-\sum_{A \in \mathcal{A}_{n}} p(A) \log \{p(A)\}+\lambda\left(\sum_{A \in \mathcal{A}_{n}} p(A)-1\right)
$$

Solving

$$
\frac{\partial}{\partial p(A)} Q(\mathbf{p}, \lambda)=0
$$

we obtain (3.27). Now, using

$$
\sum_{A \in \mathcal{A}_{n}} p(A)=\binom{N}{n} \exp (\lambda-1)=1
$$

we obtain $p(A)=1 /\binom{N}{n}$ for all $A \in \mathcal{A}_{n}$.
The entropy of a simple random sampling design is

$$
I\left(\mathbf{p}_{\mathrm{SRS}}\right)=-\sum_{A \in \mathcal{A}_{n}} \frac{1}{\binom{N}{n}} \log \binom{N}{n}^{-1}=\log \binom{N}{n}
$$

On the other hand, the systematic sampling design has a very small entropy. There are only $G=N / n$ possible samples, and each of these samples has $1 / G$ selection probability. Thus, the entropy of systematic sampling is

$$
I\left(\mathbf{p}_{\mathrm{SYS}}\right)=-\sum_{A \in \mathcal{A}} p(A) \log \{p(A)\}=G \cdot \frac{1}{G} \cdot \log \left(\frac{1}{G}\right)=\log G
$$

which is much smaller than that of simple random sampling of size $n=N / G$. In fact, Pea et al. (2007) show that systematic sampling designs are minimum entropy designs.




---

# 4 

## Stratified Sampling

### 4.1 Introduction

Stratified sampling refers to sampling designs in which the finite population is divided into several subpopulations, called strata, and sample draws are made independently across each strata. The formal definition of the stratified sampling can be made as follows.

Definition 4.1. Stratified Sampling satisfies the following two conditions.

1. The finite population is stratified into $H$ mutually exclusive and exhaustive subpopulations, called strata.

$$
\mathcal{U}=\mathcal{U}_{1} \cup \cdots \cup \mathcal{U}_{H}
$$

and $\mathcal{U}_{h} \cap \mathcal{U}_{g}=\emptyset$ for $h \neq g$.
2. Within each population (or stratum), samples are drawn independently across the strata.

$$
\operatorname{Pr}\left(i \in \mathcal{A}_{h}, j \in \mathcal{A}_{g}\right)=\operatorname{Pr}\left(i \in \mathcal{A}_{h}\right) \operatorname{Pr}\left(j \in \mathcal{A}_{g}\right), \quad \text { for } h \neq g
$$

where $\mathcal{A}_{h}$ is the index set of the sample in stratum $h, h=1,2, \cdots, H$.
In stratified sampling, the sample size $n_{h}$ in stratum $h$ is under control at the time of sampling design. Thus, we can control the precision of the study domains. Furthermore, by allowing different sampling methods for different strata, we have more flexibility in sample selection and data collection in practice. Generally speaking, stratified sampling improves the efficiency of survey estimates over sample random sampling. For these reasons, stratified sampling is very popular in practice.

Let $\mathcal{U}_{h}=\left\{1, \cdots, N_{h}\right\}$ be the indices in the population elements in stratum $h$ and let $y_{h i}$ denote the measurement of the study item $y$ for unit $i$ in stratum $h$. The population total $Y=\sum_{h=1}^{H} Y_{h}$ is the sum of the stratum totals $Y_{h}=$ $\sum_{i=1}^{N_{h}} y_{h i}$. The HT estimator of $Y$ is the sum of the HT estimator of $Y_{h}$. That is,

$$
\hat{Y}_{\mathrm{HT}}=\sum_{h=1}^{H} \hat{Y}_{\mathrm{HT}, h}
$$




---

Note that $\hat{Y}_{\mathrm{HT}, h}$ is unbiased for $Y_{h}$. By the independence assumption, we obtain

$$
\mathbf{V}\left(\hat{Y}_{\mathrm{HT}}\right)=\sum_{h=1}^{H} \mathbf{V}\left(\hat{Y}_{\mathrm{HT}, h}\right)
$$

# Example 4.1. (Stratified random sampling) 

In stratified random sampling, we have SRS independently for each stratum. In this case, the HT estimator of $Y$ is

$$
\hat{Y}_{\mathrm{HT}}=\sum_{i=1}^{H} \frac{N_{h}}{n_{h}} \sum_{i \in A_{h}} y_{h i}=\sum_{i=1}^{H} N_{h} \bar{y}_{h}
$$

where $N_{h}$ is the size of $U_{h}$ and $n_{h}$ is the size of $A_{h}$. Its variance is

$$
\mathbf{V}\left(\hat{Y}_{\mathrm{HT}}\right)=\sum_{h=1}^{H} N_{h}^{2} \mathbf{V}\left(\bar{y}_{h}\right)=\sum_{h=1}^{H} \frac{N_{h}^{2}}{n_{h}}\left(1-\frac{n_{h}}{N_{h}}\right) S_{h}^{2}
$$

where $\bar{Y}_{h}=N_{h}^{-1} \sum_{i=1}^{N_{h}} y_{h i}$ and $S_{h}^{2}=\left(N_{h}-1\right)^{-1} \sum_{i=1}^{N_{h}}\left(y_{h i}-\bar{Y}_{h}\right)^{2}$.
To estimate the variance in (4.1), we use

$$
\hat{\mathbf{V}}\left(\hat{Y}_{\mathrm{HT}}\right)=\sum_{h=1}^{H} \hat{\mathbf{V}}\left(\hat{Y}_{\mathrm{HT}, h}\right)=\sum_{h=1}^{H} \frac{N_{h}^{2}}{n_{h}}\left(1-\frac{n_{h}}{N_{h}}\right) s_{h}^{2}
$$

where $s_{h}^{2}$ is an unbiased estimator of $S_{h}^{2}$ and is given by

$$
s_{h}^{2}=\frac{1}{n_{h}-1} \sum_{i \in A_{h}}\left(y_{h i}-\bar{y}_{h}\right)^{2}
$$

### 4.2 Sample size allocation

One of the important problems with stratified sampling is that, given the total sample size $n$, how to decide the sample size $n_{h}$ in stratum $h$ such that $\sum_{h=1}^{H} n_{h}=n$. Such a problem is called the sample size allocation problem for stratified sampling.

One simple way is to use the proportional allocation, where the sample size in a stratum is proportional to the population size in the stratum. That is,

$$
n_{h}=\frac{N_{h}}{n} N
$$

In this proportional allocation, the variance in (4.1) reduces to

$$
\mathbf{V}\left(\hat{Y}_{\mathrm{HT}}\right)=\frac{N^{2}}{n}\left(1-\frac{n}{N}\right) \sum_{h=1}^{H} \frac{N_{h}}{N} S_{h}^{2}
$$




---

Assuming that $N_{h}$ are sufficiently large, we have

$$
\begin{aligned}
\sum_{h=1}^{H} \frac{N_{h}}{N} S_{h}^{2} & =\frac{1}{N} \sum_{h=1}^{H} \frac{N_{h}}{N_{h}-1} \sum_{i=1}^{N_{h}}\left(y_{h i}-\bar{Y}_{h}\right)^{2} \\
& \doteq \frac{1}{N-1} \sum_{h=1}^{H} \sum_{i=1}^{N_{h}}\left(y_{h i}-\bar{Y}_{h}\right)^{2} \\
& \leq \frac{1}{N-1} \sum_{h=1}^{H} \sum_{i=1}^{N_{h}}\left(y_{h i}-\bar{Y}\right)^{2}=S^{2}
\end{aligned}
$$

Thus, the variance (4.3) under proportional allocation is no larger than the variance under simple random sampling. That is, stratified sampling under proportional allocation is more efficient than simple random sampling in terms of sampling variance. Here, the inequality in (4.4) is derived from the following equality:

$$
\sum_{h=1}^{H} \sum_{i=1}^{N_{h}}\left(y_{h i}-\bar{Y}\right)^{2}=\sum_{h=1}^{H} N_{h}\left(\bar{Y}_{h}-\bar{Y}\right)^{2}+\sum_{h=1}^{H} \sum_{i=1}^{N_{h}}\left(y_{h i}-\bar{Y}_{h}\right)^{2}
$$

which is often expressed as $S S T=S S B+S S W$. In (4.4), the equality holds when $S S B=0$ which is the case when $\bar{Y}_{h}$ are all the same. That is, there is no between-stratum variation. Another extreme case is when $S S W=0$ which occurs when $y_{h i}=\bar{Y}_{h}$, (perfect homogeneity within stratum). In this extreme case, the variance (4.3) becomes zero. Hence, when stratum boundaries are formed, its statistical efficiency can be improved if the within-stratum variations are minimized, and the between-stratum variations are maximized. However, stratified sampling does not necessarily have a smaller variance than simple random sampling. In some poor sample size allocation, stratified sampling can have a larger sampling variance than simple random sampling.

Another advantage of proportional allocation is that the sampling weights are all equal. A sampling design that has equal sampling weights is called a self-weighting design. Self weighting is very convenient and popular in practice.

To guarantee an unbiased estimate, we need to impose $n_{h} \geq 1$ for all $h=$ $1, \cdots, H$. The proportional allocation satisfies the following three conditions:

1. $n_{h}$ are integer valued with $n_{h} \geq 1$ for all $h=1, \cdots, H$.
2. $\sum_{h=1}^{H} n_{h}=n$
3. $N_{h} / n_{h} \cong N / n$ as closely as possible for every $h$.

To implement the proportional allocation, the Hintington-Hill method can be used as follows.

1. Calculate a set of "priority values" for each stratum $h$, based on



---

the state's apportionment population. The $s$-th priority value in stratum $h$ is defined as

$$
a_{h, s}=\frac{N_{h}}{\sqrt{s(s+1)}}
$$

where $s$ is the number of samples that the stratum has been allocated so far.
2. Sort these values from largest to smallest.
3. Allocate a seat to a state each time one of its priority values is included in the largest 385 values in the list.

To illustrate the Huntington-Hill method, consider the following toy example of $H=4$ strata.


Now, suppose that we are interested in selecting a sample of size $n=8$ for proportional allocation. Due to $n_{h} \geq 1$, we first assign one sample to each stratum. Thus, it remains to select 4 additional sample elements. Based on the values of $a_{h, s}$, the largest 4 values are $a_{1,1}=70710, a_{1,2}=40825, a_{2,1}=35355$, and $a_{1,3}=28868$. Thus, the sample sizes for each stratum are $n_{1}=4, n_{2}=2$, $n_{3}=1$ and $n_{4}=1$. The Huntington-Hill method is currently used to allocate the seats of the House of Representatives. Wright (2012) provides a statistical interpretation of the Huntington-Hill method for stratified sampling.

Following the argument of Wright (2012), we can show that HuntingtonHill method is essentially minimizing

$$
Q=\frac{1}{n} \sum_{h=1}^{H} n_{h}\left(\frac{N_{h}}{n_{h}}-\frac{N}{n}\right)^{2}
$$

It is the average squared distance of the representativeness of individual sample elements from $N / n$. To see this, note that

$$
Q=\frac{1}{n} \sum_{h=1}^{H} \frac{N_{h}^{2}}{n_{h}}-\frac{N^{2}}{n^{2}}
$$

Thus, for fixed $n$, we only have to minimize the first quantity. Now, using

$$
\begin{aligned}
\sum_{h=1}^{H} \frac{N_{h}^{2}}{n_{h}} & =\sum_{h=1}^{N} N_{h}^{2}-\sum_{h=1}^{H} \sum_{k=1}^{n_{h}-1}\left(\frac{1}{k}-\frac{1}{k+1}\right) N_{h}^{2} \\
& =\sum_{h=1}^{N} N_{h}^{2}-\sum_{h=1}^{H} \sum_{k=1}^{n_{h}-1} \frac{N_{h}^{2}}{(k+1) k}
\end{aligned}
$$




---

we have only to maximize the second term:

$$
\sum_{h=1}^{H} \sum_{k=1}^{n_{h}-1} \frac{N_{h}^{2}}{(k+1) k}=\sum_{h=1}^{H} \sum_{k=1}^{n_{h}-1} a_{h, k}^{2}
$$

Therefore, by selecting the largest $n-H$ elements from $a_{h, k}$ 's, we can maximize the above quantity in (4.5).

Now consider another allocation method, which is obtained from an optimization problem. The optimal allocation is obtained by minimizing the variance of the HT estimator under the given constraint. The usual constraint is expressed in terms of the total cost. Total cost is often expressed as $C=c_{0}+\sum_{h=1}^{H} c_{h} n_{h}$, where $c_{0}$ is the initial cost and $c_{h}$ is the cost of interviewing one unit in stratum $h$. The following theorem is useful in determining the optimal allocation.

Theorem 4.1. Assume that the sampling variance of an estimator is

$$
V(\hat{\theta})=\sum_{h} Q_{h} / n_{h}
$$

and the total cost is

$$
C=c_{0}+\sum_{h=1}^{H} c_{h} n_{h}
$$

The sample size allocation that minimizes (4.6) subject to (4.7) is

$$
n_{h} \propto \frac{\sqrt{Q_{h}}}{\sqrt{n_{h}}}
$$

Proof. By the Cauchy-Schwartz inequality, we obtain

$$
\left(\sum_{h} \frac{Q_{h}}{n_{h}}\right)\left(\sum_{h} c_{h} n_{h}\right) \geq\left(\sum_{h} \sqrt{Q_{h} c_{h}}\right)^{2}
$$

where the equality holds when

$$
\frac{c_{h} n_{h}}{Q_{h} / n_{h}}=\text { constant }
$$

which leads to (4.8).
Note that (4.8) is the necessary and sufficient condition for the product of $V(\hat{\theta})$ and $C$ to be minimized. Thus, the same conclusion holds either when minimizing the variance subject to the cost constraints or minimizing the cost subject to the constraint on the variance. For the estimation of the population




---

total, using the variance form in (4.1), we have $Q_{h}=N_{h}^{2} S_{h}^{2}$ and the optimal allocation is

$$
n_{h}^{*} \propto N_{h} S_{h} / \sqrt{c_{h}}
$$

If $c_{h}$ are all equal and $S_{h}$ are the same across the strata, then the optimal allocation reduces to the proportional allocation. The optimal allocation in (4.9) is first proposed by Neyman (1934) and is often called the Neyman allocation.

If $c_{h}$ are all equal, the optimal allocation using

$$
n_{h}=\frac{N_{h} S_{h}}{\sum_{h=1}^{H} N_{h} S_{h}} n
$$

leads to

$$
V_{\mathrm{opt}}\left(\hat{Y}_{\mathrm{HT}}\right)=\frac{N^{2}}{n}\left(\sum_{h=1}^{H} W_{h} S_{h}\right)^{2}-N \sum_{h=1}^{H} W_{h} S_{h}^{2}
$$

where $W_{h}=N_{h} / N$. Note that, under proportional allocation, we have

$$
V_{\text {prop }}\left(\hat{Y}_{\mathrm{HT}}\right)=\frac{N^{2}}{n} \sum_{h=1}^{H} W_{h} S_{h}^{2}-N \sum_{h=1}^{H} W_{h} S_{h}^{2}
$$

Using Jensen's inequality, we obtain

$$
\left(\sum_{h=1}^{H} W_{h} S_{h}\right)^{2} \leq \sum_{h=1}^{H} W_{h} S_{h}^{2}
$$

which implies that

$$
V_{\text {prop }}\left(\hat{Y}_{\mathrm{HT}}\right) \geq V_{\text {opt }}\left(\hat{Y}_{\mathrm{HT}}\right)
$$

Note that the allocation in (4.9) is derived by minimizing the variance of the total estimator. Instead of estimating the population total, if we are more interested in comparing the population means across strata, then the Neyman allocation in (4.9) is not necessarily optimal. For example, if we are interested in comparing the stratum means between stratum 1 and stratum 2 , the parameter of interest is $\theta=\bar{Y}_{1}-\bar{Y}_{2}$ and its unbiased estimator is $\hat{\theta}=$ $\bar{y}_{1}-\bar{y}_{2}$. In this case, given the same cost constraint, the optimal allocation that minimizes the variance of $\hat{\theta}$ is, according to Theorem 4.1,

$$
n_{h}^{*} \propto S_{h} / \sqrt{c_{h}}
$$

which is different from the Neyman allocation in (4.9). Thus, the optimal allocation can be different for different parameters. Assuming that $c_{h}$ are the same across strata and $S_{h}^{2}$ are also the same across the strata, it is better to allocate the sample size proportional to $N_{h}$ if we are going to estimate the total, while it is better to use equal sample size if we are going to compare




---

different stratum populations. When we want to achieve the two conflicting goals, we can use an allocation with $n_{h} \propto N_{h}^{\alpha}(0<\alpha<1)$ as a compromise. This allocation is called a power allocation and $\alpha=1 / 2$ is a popular choice. See Bankier (1988) for more details about the sample size allocation.

Example 4.2. Consider the population with $H=3$ strata with the summary data below. (The costs are all equal.)


Suppose that we wish to allocate the sample size $n=140$ to each stratum using optimal allocation. Using (4.8) with equal $c_{h}$, we obtain

$$
n_{1}=104 n_{2}=23 n_{3}=13
$$

However, $n_{1}=104$ is greater than $N_{1}=100$. Thus, we would take $n_{1}=N_{1}=$ 100 and allocate the remaining 40 elements to strata and 3 to obtain

$$
n_{2}=\frac{110 \times 10}{110 \times 10+120 \times 5} \cdot 40 \doteq 26
$$

and $n_{3}=40-26=14$.

We now briefly discuss the problem of determining the sample size $n$ under stratified random sampling. Given the margin of error, we wish to find the sample size $n$ for stratified sampling. That is, we wish to find $n$ such that

$$
P\{\hat{\theta}-\theta \mid \leq e\}=1-\alpha
$$

Recall that, under proportional allocation, we have

$$
V_{\text {prop }}\left(\hat{Y}_{\mathrm{HT}}\right)=\frac{N^{2}}{n}\left(1-\frac{n}{N}\right) S_{\mathrm{w}}^{2}
$$

where

$$
S_{\mathrm{w}}^{2}=\sum_{h=1}^{H} W_{h} S_{h}^{2}
$$

Thus, under proportional allocation, you can use $S_{\mathrm{w}}^{2}$ instead of $S^{2}$ in the sample size determination formula (3.10) under SRS. That is, use

$$
e=z_{\alpha / 2} \sqrt{\frac{S_{\mathrm{w}}^{2}}{n}\left(1-\frac{n}{N}\right)} \Rightarrow n=\frac{z_{\alpha / 2}^{2} S_{\mathrm{w}}^{2}}{e^{2}+z_{\alpha / 2}^{2} S_{\mathrm{w}}^{2} / N}
$$

for mean estimation.




---

Example 4.3. We illustrate the advantage of the optimal sample-size allocation using the real data example of the US Agricultural Census data (agpop.dat) which is publicly available. The US agriculatural Census data can also be obtained in "SDaA" package in R. The dataset consists of 3,078 counties in the US in the year of 1992. From the population of counties, we are interested in using a stratified random sample of size $n=300$ to estimate the population total of variable "acres92", which represents number of acres devoted to farms in 1992. The stratification variable is "region" with levels S (south), W (west), NC (north central), NE (northeast). Table 4.3 presents some summary statistics for the study variable for each stratum.

TABLE 4.1
Summary statistics for ares devoted to farms in 1992

| Region | Population Size | Total Acres | Standard Dev |
| :--- | :---: | :---: | :---: |
| NE | 220 | $0.199 \times 10^{8}$ | 79,365 |
| NC | 1,054 | $3.435 \times 10^{8}$ | 271,303 |
| S | 1,382 | $2.752 \times 10^{8}$ | 243,956 |
| W | 422 | $3.052 \times 10^{8}$ | 835,638 |
| Total | 3,078 | $9.44 \times 10^{8}$ | 424,686 |

Now, the following table presents the variance under proportional allocation and Neyman allocation.

TABLE 4.2
Sample sizes and sampling variances for estimated total acres devoted to farms in 1992

| Region | Pop. Size | Proportional Allocation |  | Optimal Allocation |  |
| :---: | :---: | :---: | :---: | :---: | :---: |
|  |  | Sample Size | $\mathrm{V}\left(\hat{Y}_{h, H T}\right)$ | Sample Size | $\mathrm{V}\left(\hat{Y}_{h, H T}\right)$ |
| NE | 220 | 21 | $0.13 \times 10^{14}$ | 5 | $0.60 \times 10^{14}$ |
| NC | 1,054 | 103 | $7.16 \times 10^{14}$ | 86 | $8.73 \times 10^{14}$ |
| S | 1,382 | 135 | $7.60 \times 10^{14}$ | 102 | $10.32 \times 10^{14}$ |
| W | 422 | 41 | $27.38 \times 10^{14}$ | 107 | $8.67 \times 10^{14}$ |
| Total | 3,078 | 300 | $42.28 \times 10^{14}$ | 300 | $28.32 \times 10^{14}$ |

The efficiency gain due to optimal allocation over the proportional allocation is about $33 \%$. That is, we can reduce the variance of the HT estimator under proportional allocation by $33 \%$ if we employ the optimal allocation.




---

# 4.3 Stratum boundary determination 

Sample size allocation is a problem of finding the suitable sample size for a given set of stratum boundaries. In some cases, we need to determine the stratum boundaries. The most popular method of finding the stratum boundaries was proposed by Dalenius and Hodges (1959).

To explain the idea of the stratification method of Dalenius and Hodges (1959), assume for now that the population values of $y$ are available or at least a proxy values of $y$ are all available. Let $y_{0}$ and $y_{H}$ be the smallest and largest values of $y$ in the finite population. The problem is to find intermediate stratum boundaries $y_{1}, \cdots, y_{H-1}$ such that

$$
V\left(\hat{\bar{Y}}_{H T}\right)=\sum_{h=1}^{H} W_{h}^{2}\left(\frac{1}{n_{h}}-\frac{1}{N_{h}}\right) S_{h}^{2}
$$

is a minimum, where $W_{h}=N_{h} / N$.
Under Neyman allocation, the above variance reduces to

$$
V\left(\hat{\bar{Y}}_{H T}\right)=\frac{1}{n}\left(\sum_{h=1}^{H} W_{h} S_{h}\right)^{2}-\frac{1}{N} \sum_{h=1}^{H} W_{h} S_{h}^{2}
$$

Thus, if $n_{h} / N_{h}$ are ignored, it suffices to minimize $\sum_{h} W_{h} S_{h}$.
Let $f(y)$ be the frequency function of $y$. If the strata are numerous and narrow, $f(y)$ should be approximately constant (rectangular) within a given stratum. Hence,

$$
\begin{aligned}
W_{h} & =\int_{y_{h-1}}^{y_{h}} f(t) d t \doteq f_{h}\left(y_{h}-y_{h-1}\right) \\
S_{h} & \doteq\left(y_{h}-y_{h-1}\right) / \sqrt{12}
\end{aligned}
$$

where $f_{h}$ is the constant value of $f(y)$ in stratum $h$. Thus, writing $Z(y)=$ $\int_{y_{0}}^{y} \sqrt{f(t)} d t$, we have

$$
\sum_{h=1}^{H} W_{h} S_{h} \propto \sum_{h=1}^{H} f_{h}\left(y_{h}-y_{h-1}\right)^{2} \doteq \sum_{h=1}^{H}\left(Z_{h}-Z_{h-1}\right)^{2}
$$

where $Z_{h}=Z\left(y_{h}\right)$ and

$$
Z(y)=\int_{y_{0}}^{y} \sqrt{f(t)} d t
$$

Since $\left(Z_{H}-Z_{0}\right)$ is fixed, $\sum_{h=1}^{H}\left(Z_{h}-Z_{h-1}\right)^{2}$ is minimized by making ( $Z_{h}-$ $Z_{h-1}$ ) constant. To achieve this goal, the rule is to form the cumulative of $\sqrt{f(y)}$ and choose the $y_{h}$ so that they create equal intervals on the cumulative $\sqrt{f(y)}$ scale.




---

1. Partition the population into $L(>2 H)$ intervals with equal length.
2. For each interval $l$, compute $\sqrt{f_{l}}$, the squared root of the frequency, and its cumulative sum.
3. Choose the boundaries of the stratum so that the sum of the $\sqrt{f_{l}}$ are about the same in each stratum.

# 4.4 Number of strata 

In this section, we explore the relationship between the variance of $\hat{\bar{Y}}_{\mathrm{HT}}=$ $\sum_{h=1}^{H} W_{h} \bar{y}_{h}$ and $H$, the number of strata, under stratified sampling. To do this, we first consider the case when the stratum boundaries are determined by the values of the study variable $Y$. To simplify the discussion, suppose that the realized population values $y_{1}, \cdots, y_{N}$ are generated from a distribution with density $f(y)$ with support in $[a, b]$. In this case, we can determined the stratum boundaries $a_{h}$ in such a way that

$$
\int_{a_{h-1}}^{a_{h}} f(y) d y=\frac{1}{H}
$$

holds. That is, if $y_{i} \in\left[a_{h-1}, a_{h}\right]$ then unit $i$ belongs to stratum $h$. In this case, $S_{h}^{2}$ obtained from $\left(a_{h-1}, a_{h}\right)$ satisfies $S_{h}^{2} \leq\left(a_{h}-a_{h-1}\right)^{2}$. Thus, under proportional allocation, by (4.3),

$$
\begin{aligned}
V\left(\hat{\bar{Y}}_{\mathrm{HT}}\right) & =\frac{1}{n}\left(1-\frac{n}{N}\right) \sum_{h=1}^{H} W_{h} S_{h}^{2} \\
& \leq \frac{1}{n H} \sum_{h=1}^{H}\left(a_{h}-a_{h-1}\right)^{2}
\end{aligned}
$$

and, since $\sum_{h=1}^{H}\left(a_{h}-a_{h-1}\right)^{2} \leq(b-a)^{2}$ is bounded, we obtain

$$
V\left(\hat{\bar{Y}}_{\mathrm{HT}}\right)=O\left(\frac{1}{n H}\right)
$$

Here, $b_{n}=O\left(a_{n}\right)$ denotes that $b_{n} / a_{n}$ is bounded.
Therefore, from the result in (4.12), we can conclude that the relative efficiency of simple probability sampling increases proportionally to $H$. So, we can conclude that the higher the $H$, the better the efficiency. However, in practice, the stratum is not determined by observing the $y$-values of the population in advance, but by observing the values in the frame of the population (which we call $x$ ). From the sampling frame, we can only stratify based on the $x$-values




---

in the frame. In this case, increasing $H$ does not proportionally improve the efficiency. To illustrate, consider the following linear model

$$
y_{i}=\alpha+\beta x_{i}+e_{i}, \quad e_{i} \sim\left(0, \sigma_{e}^{2}\right)
$$

That is, the values of the finite population are generated from model (4.13). Here, $\alpha, \beta, \sigma_{e}^{2}$ are unknown parameters.

In this case, the model expectation of $V\left(\hat{\bar{Y}}_{\mathrm{HT}}\right)$ in (4.11) is

$$
\begin{aligned}
E_{\zeta}\left\{V\left(\hat{\bar{Y}}_{\mathrm{HT}}\right)\right\} & =\frac{1}{n} \sum_{h=1}^{H} W_{h} E_{\zeta}\left(S_{h}^{2}\right) \\
& =\frac{1}{n} \sum_{h=1}^{H} W_{h}\left(\beta^{2} S_{x h}^{2}+\sigma_{e}^{2}\right) \\
& =\frac{1}{n} \sum_{h=1}^{H} W_{h}\left(\beta^{2} S_{x h}^{2}\right)+\frac{1}{n} \sigma_{e}^{2}
\end{aligned}
$$

So, if we stratify based on $x$, the first term will be $O\left(n^{-1} H^{-1}\right)$ as in (4.12), but the second term will be $O\left(n^{-1}\right)$, which is the part that is independent of $H$. In other words, the higher the correlation coefficient between $x$ and $y$, the smaller the second term. If the correlation coefficient between $x$ and $y$ is high, the second term will be small, so we can see a lot of efficiency gain due to stratification. Otherwise, the second term becomes large, so the effect of stratification on reducing variance becomes smaller.

# 4.5 Domain Estimation 

As discussed in Section 2.3, we generally want to make inferences about subpopulations as well as the whole population. Let $U_{d} \subset U$ be the index set of the subpopulation for domain $d$. Let $N_{d}=\left|U_{d}\right|$ be the number of elements in $U_{d}, Y_{d}=\sum_{i \in U_{d}} y_{i}$ be the domain total of $y$ in domain $d$, and $\bar{Y}_{d}=Y_{d} / N_{d}$ be the domain mean of $y$ in domain $d$.

To estimate domain parameters, define

$$
z_{k d}= \begin{cases}1 & \text { if } k \in U_{d} \\ 0 & \text { if } k \notin U_{d}\end{cases}
$$

for $k \in U$. Note that $z_{i d}$ is a characteristic of the population. Using $z_{k d}$, we can exexpress $\sum_{k \in U} z_{k d}=N_{d}$. The HT estimation of $N_{d}$ is

$$
\hat{N}_{d}=\sum_{k \in U} \frac{z_{k d} I_{k}}{\pi_{k}}
$$




---

Also, HT estimation of $Y_{d}=\sum_{k \in U_{d}} y_{k}=\sum_{k \in U} y_{k} z_{k d}$ is

$$
\hat{Y}_{d}=\sum_{k \in U} \frac{y_{k} z_{k d} I_{k}}{\pi_{k}}=\sum_{k \in A} \frac{y_{k} z_{k d}}{\pi_{k}}
$$

To estimate $\bar{Y}_{d}=Y_{d} / N_{d}$, we may use

$$
\bar{y}_{d}=\frac{\hat{Y}_{d}}{\hat{N}_{d}}
$$

which is a ratio of two HT estimators. Ratio of two unbiased estimator is not exactly unbiased as

$$
\mathbb{E}\left(\bar{y}_{d}\right)=\mathbb{E}\left(\frac{\hat{Y}_{d}}{\hat{N}_{d}}\right) \neq \frac{\mathbb{E}\left(\hat{Y}_{d}\right)}{\mathbb{E}\left(\hat{N}_{d}\right)}=\bar{Y}_{d}
$$

but it is asymptotically unbiased as long as $\mathbb{E}\left(\hat{N}_{d}\right) \neq 0$.
The statistical properties of $\bar{y}_{d}$ can be derived from the following approximation:

$$
\begin{aligned}
\bar{y}_{d} & =\frac{\hat{Y}_{d}}{\hat{N}_{d}}=f\left(\hat{N}_{d}, \hat{Y}_{d}\right) \\
& \doteq f\left(N_{d}, Y_{d}\right)+\left\{\frac{\partial}{\partial Y_{d}} f\left(N_{d}, Y_{d}\right)\right\}\left(\hat{Y}_{d}-Y_{d}\right)+\left\{\frac{\partial}{\partial N_{d}} f\left(N_{d}, Y_{d}\right)\right\}\left(\hat{N}_{d}-N_{d}\right) \\
& =\frac{Y_{d}}{N_{d}}+\left(\frac{1}{N_{d}}\right)\left(\hat{Y}_{d}-Y_{d}\right)+\left(-\frac{Y_{d}}{N_{d}^{2}}\right)\left(\hat{N}_{d}-N_{d}\right)
\end{aligned}
$$

Thus,

$$
\mathbb{V}\left(\bar{y}_{d}\right) \doteq \mathbb{V}\left\{\frac{1}{N_{d}}\left(\hat{Y}_{d}-\bar{Y}_{d} \hat{N}_{d}\right)\right\}
$$

Under SRS, result (4.14) can be written as

$$
\begin{aligned}
\mathbb{V}\left(\bar{y}_{d}\right) & \doteq \frac{1}{N_{d}^{2}} \mathbb{V}\left(\frac{N}{n} \sum_{i \in A} z_{i d}\left(y_{i}-\bar{Y}_{d}\right)\right) \\
& =\frac{N^{2}}{N_{d}^{2}}\left(\frac{1}{n}-\frac{1}{N}\right) \frac{1}{N-1} \sum_{i=1}^{N} z_{i d}\left(y_{i}-\bar{Y}_{d}\right)^{2} \\
& \doteq\left(\frac{1}{\mathbb{E}\left(n_{d}\right)}-\frac{1}{N_{d}}\right) \frac{1}{N_{d}-1} \sum_{i \in U_{d}}\left(y_{i}-\bar{Y}_{d}\right)^{2}
\end{aligned}
$$

where $\mathbb{E}\left(n_{d}\right)=N_{d}(n / N)$. Thus, the variance formula suggests that the variance of the domain mean estimator is asymptotically equivalent to the variance of the SRS mean of size $\mathbb{E}\left(n_{d}\right)$ from the subpopulation $U_{d}$.




---

The finite population is decomposed into $G$ groups. Group information was not available at the time of sample selection. The population size of the group $g$, denoted by $N_{g}$, is known. If the group information is available from the sampling frame, then we can use stratified sampling. However, if group information is not available, then we can incorporate population information $N_{g}$ after sample selection. This is called post-stratification.

The post-stratification estimator can be defined as

$$
\hat{Y}_{\text {post }}=\sum_{g=1}^{G} \frac{N_{g}}{\hat{Y}_{g}} \hat{N}_{g}
$$

Note that, unlike stratified sampling, the denominator terms $\left(\hat{N}_{g}\right)$ are random. Using the Taylor expansion again, we obtain

$$
\begin{aligned}
\hat{Y}_{\text {post }} & =\sum_{g=1}^{G} N_{g} \frac{\hat{Y}_{g}}{\hat{N}_{g}} \\
& \doteq \sum_{g=1}^{G} N_{g}\left\{\frac{Y_{d}}{N_{d}}+\frac{1}{N_{d}}\left(\hat{Y}_{d}-\bar{Y}_{d} \hat{N}_{d}\right)\right\} \\
& =Y+\sum_{g=1}^{G} \frac{1}{\pi_{i}} z_{i g}\left(y_{i}-\bar{Y}_{g}\right)
\end{aligned}
$$

Thus, the asymptotic variance can be written as

$$
\mathcal{V}\left(\hat{Y}_{\text {post }}\right) \doteq \mathcal{V}\left\{\sum_{g=1}^{G} \sum_{i \in \mathcal{A}} \frac{1}{\pi_{i}} z_{i g}\left(y_{i}-\bar{Y}_{g}\right)\right\}
$$

Under SRS, the asymptotic variance (4.16) reduces to

$$
\mathcal{V}\left(\hat{Y}_{\text {post }}\right) \doteq \frac{N^{2}}{n}\left(1-\frac{n}{N}\right) \frac{1}{N-1} \sum_{g=1}^{G} \sum_{i \in \mathcal{U}_{g}}\left(y_{i}-\bar{Y}_{g}\right)^{2}
$$

Thus, it is essentially equal to the variance under stratified sampling with proportional allocation.




---

# 5 

## Sampling with Unequal probabilities

### 5.1 Introduction

We now consider unequal probability sampling designs, which is very popular in practice. In unequal probability sampling, we can improve the efficiency of the resulting point estimator by properly incorporating the auxiliary information available in the sampling frame into the sampling design.

Example 5.1. Consider the following artificial example of a finite population of business companies. The total number of employees is available in the whole population, but the annual total income is available only for the sample.

| Company | Size (Number of employees) | $y$ (Income) |
| :---: | :---: | :---: |
| A | 100 | 11 |
| B | 200 | 20 |
| C | 300 | 24 |
| D | 1,000 | 245 |

If we wish to select only one company, we can consider the following two approaches.

1. Equal probability selection
2. Unequal probability selection with the selection probability proportional to size.

The sampling distribution of the total income estimator is then given by

$$
\hat{Y}= \begin{cases}11 \times 4 & \text { if } \mathrm{A} \text { is sampled } \\ 20 \times 4 & \text { if } \mathrm{B} \text { is sampled } \\ 24 \times 4 & \text { if } \mathrm{C} \text { is sampled } \\ 245 \times 4 & \text { if } \mathrm{D} \text { is sampled }\end{cases}
$$

and so

$$
\begin{aligned}
\mathrm{E}(\hat{Y}) & =11+20+24+245=300 \\
\mathrm{~V}(\hat{Y}) & =154,488
\end{aligned}
$$




---

On the other hand, for unequal probability sampling,

$$
\hat{Y}= \begin{cases}11 \times 16 & \text { if } A \text { is sampled } \\ 20 \times(16 / 2) & \text { if } B \text { is sampled } \\ 24 \times(16 / 3) & \text { if } C \text { is sampled } \\ 245 \times(16 / 10) & \text { if } D \text { is sampled }\end{cases}
$$

and so

$$
\begin{aligned}
\mathrm{E}(\hat{Y}) & =11+20+24+245=300 \\
\mathrm{~V}(\hat{Y}) & =14,248
\end{aligned}
$$

Thus, not surprisingly, unequal probability selection using the number of employees as the size is more efficient than the equal probability sampling mechanism. A company with many employees is likely to have more income than a company with a smaller number of employees.

In general, when the sampling frame contains information about the size of the sampling unit, the size information is often considered in the sampling design stage such that the selection probability of a unit is proportional to the size. Unequal probability sampling is also popular in cluster sampling, which we plan to cover in Chapter 7. If the cluster sizes are unequal, it is better to use this information in the cluster sampling. In some cases, unequal probability sampling is implicit. The following example illustrates this point.

Example 5.2. Suppose that we are interested in estimating the percent of families owing home, by obtaining a sample of school children. The following table presents an artificial distribution of the population of school children.


In this example, the reporting unit is school children but the analysis unit is family. Thus, if we are selecting a simple random sample of school children then the large-sized families will be over-sampled. Thus, a simple mean of the sample observations will lead to biased estimation. In this example, about $43 \%$ of the families have their home. However, in the school-children level, among the 100,000 school children, the total number of children with home-owning families is

$$
20,000 \times 0.1+30,000 \times 0.3+30,000 \times 0.4+20,000 \times 0.6=35,000
$$

Thus, only $35 \%$ of the children belong to families with their home.




---

# 5.2 PPS sampling 

As seen in Example 5.1, a sampling design proportional to the number of employs is quite efficient for estimating the total income of the companies in the population. In this case, the total number of employees serves the role of measure of size (MOS), which is an auxiliary variable that reflects the magnitude of $y_{i}$ in the population. A sampling that selects elements with probability proportional to MOS with replacement is called probability proportional to size (PPS) sampling. Since it is easy to select a sample of size one with a selection probability proportional to MOS, we can repeat the selection $n$ times independently with replacement to achieve the PPS sampling of size $n$. PPS sampling is easy to implement, as it is an with-replacement sampling, but it may have duplicated sample elements.

Let $M_{i}$ be the value of MOS associated with element $i$ in the population. In this case,

$$
p_{i}=\frac{M_{i}}{\sum_{i=1}^{N} M_{i}}
$$

is the probability of selecting element $i$ for a single draw of sample selection. Let $a_{k}$ be the index of population element in the $k$-th draw of the PPS sampling, In this case, $a_{k}$ is a random variable with probability $P\left(a_{k}=i\right)=p_{i}$, for $i \in U$. The observed value of $y_{i}$ in the $k$-th draw is $y_{a_{k}}=\sum_{i=1}^{N} I\left(a_{k}=i\right) y_{i}$. Note that $\mathrm{E}\left(y_{a_{k}}\right)=\sum_{i=1}^{N} p_{i} y_{i}$ which is not necessarily equal to the population mean.

If we define

$$
z_{k}=\frac{y_{a_{k}}}{p_{a_{k}}}=\sum_{i=1}^{N} \frac{I\left(a_{k}=i\right) y_{i}}{p_{i}}, \quad k=1,2, \cdots, n
$$

then $z_{1}, z_{2}, \cdots, z_{n}$ are independently and identically distributed with the distribution

$$
z_{k}= \begin{cases}y_{1} / p_{1} & \text { with probability } p_{1} \\ y_{2} / p_{2} & \text { with probability } p_{2} \\ \vdots & \\ y_{N} / p_{N} & \text { with probability } p_{N}\end{cases}
$$

Thus, for each $k=1, \cdots, n$, we have

$$
\begin{aligned}
\mathrm{E}\left(z_{k}\right) & =\sum_{i=1}^{N} \frac{y_{i}}{p_{i}} \\
\mathrm{~V}\left(z_{k}\right) & =\sum_{i=1}^{N} p_{i}\left(\frac{y_{i}}{p_{i}}-\bar{Y}\right)^{2}
\end{aligned}
$$




---

Thus, we can use

$$
\hat{Y}_{\mathrm{PPS}}=\frac{1}{n} \sum_{k=1}^{n} z_{k}=\frac{1}{n} \sum_{k=1}^{n} \frac{y_{a_{k}}}{p_{a_{k}}}
$$

as an estimator for $Y=\sum_{i=1}^{N} y_{i}$. The estimator in (5.1) is sometimes called Hansen-Hurwitz (HH) estimator, as it was first proposed by Hansen and Hurwitz (1943).

Alternatively, we can express

$$
\hat{Y}_{\mathrm{PPS}}=\frac{1}{n} \sum_{k=1}^{n} z_{k}=\sum_{i \in \mathcal{A}} w_{i} y_{i}
$$

where $w_{i}=Q_{i} /\left(n p_{i}\right)$ and $Q_{i}=\sum_{k=1}^{n} I\left(a_{k}=i\right)$ is the number of times that unit $i$ is selected in the sample. The HH estimator in (5.1) is a weighted sum of the sample observations.

To discuss variance estimation of HH estimator, we first prove the following Lemma.

Lemma 5.1. Let $X_{1}, X_{2}, \cdots, X_{n}$ be independent random variables with $E\left(X_{i}\right)=\mu$ and $V\left(X_{i}\right)=\sigma_{i}^{2}$. An unbiased estimator for the variance of $\bar{X}_{n}=n^{-1} \sum_{i=1}^{n} X_{i}$ is given by

$$
\hat{V}\left(\bar{X}_{n}\right)=\frac{1}{n} \frac{1}{n-1} \sum_{i=1}^{n}\left(X_{i}-\bar{X}_{n}\right)^{2}
$$

Proof. Since $X_{i}$ 's are independent,

$$
V\left(\bar{X}_{n}\right)=\frac{1}{n^{2}} \sum_{i=1}^{n} \sigma_{i}^{2}
$$

Also, as we can express

$$
\hat{V}\left(\bar{X}_{n}\right)=\frac{1}{n} \frac{1}{n-1}\left\{\sum_{i=1}^{n}\left(X_{i}-\mu\right)^{2}-n\left(\bar{X}_{n}-\mu\right)^{2}\right\}
$$

by taking the expectation on both sides of the above term, we obtain

$$
E\left\{\hat{V}\left(\bar{X}_{n}\right)\right\}=\frac{1}{n} \frac{1}{n-1}\left\{\sum_{i=1}^{n} \sigma_{i}^{2}-n \frac{1}{n^{2}} \sum_{i=1}^{n} \sigma_{i}^{2}\right\}=\frac{1}{n^{2}} \sum_{i=1}^{n} \sigma_{i}^{2}
$$

which proves the unbiasedness of $\hat{V}\left(\bar{X}_{n}\right)$ in (5.2).
By Lemma 5.1, an unbiased variance estimator of HH estimator is given by

$$
\hat{V}_{\mathrm{PPS}}=\frac{1}{n} S_{z}^{2}=\frac{1}{n} \frac{1}{n-1} \sum_{k=1}^{n}\left(\frac{y_{a_{k}}}{p_{a_{k}}}-\hat{Y}_{\mathrm{PPS}}\right)^{2}
$$




---

Using $Q_{i}$ notation, we can express the above variance estimation formula as

$$
\hat{V}_{\mathrm{PPS}}=\frac{1}{n} \cdot \frac{1}{n-1} \sum_{i \in \mathcal{A}} Q_{i}\left(\frac{y_{i}}{p_{i}}-\hat{Y}_{\mathrm{PPS}}\right)^{2}
$$

If $n / N$ is very small, then $Q_{i}$ are either 0 or 1 . In this case,

$$
\hat{V}_{\mathrm{PPS}}=\frac{n}{n-1} \sum_{i \in \mathcal{A}}\left(w_{i} y_{i}-\frac{1}{n} \hat{Y}_{\mathrm{PPS}}\right)^{2}
$$

In some situation, $y_{i}$ has the meaning of a total value in unit $i$. For example, $y_{i}$ is the total crop yield in the farm $i$ and $M_{i}$ is the total size of the crop acres in form $i$. In this case, $\bar{y}_{i}$ is the average crop yield per acre. In this case, we can express

$$
\hat{Y}_{\mathrm{PPS}}=\left(\sum_{i=1}^{N} M_{i}\right) \times \frac{1}{n} \sum_{k=1}^{n} \bar{y}_{a_{k}}
$$

and

$$
\hat{V}\left(\hat{Y}_{\mathrm{PPS}}\right)=\left(\sum_{i=1}^{N} M_{i}\right)^{2} \times \frac{1}{n} \frac{1}{n-1} \sum_{k=1}^{n}\left(\bar{y}_{a_{k}}-\hat{\bar{Y}}_{\mathrm{PPS}}\right)^{2}
$$

where $\hat{\bar{Y}}_{\text {PPS }}=n^{-1} \sum_{k=1}^{n} \bar{y}_{a_{k}}$. If the parameter of interest is the mean

$$
\bar{Y}=\frac{\sum_{i=1}^{N} y_{i}}{\sum_{i=1}^{N} M_{i}}=\frac{\sum_{i=1}^{N} M_{i} \bar{y}_{i}}{\sum_{i=1}^{N} M_{i}}
$$

then the HH estimator is

$$
\hat{\bar{Y}}_{\mathrm{PPS}}=\frac{1}{n} \sum_{k=1}^{n} \bar{y}_{a_{k}}
$$

and its variance estimator is

$$
\hat{V}\left(\hat{\bar{Y}}_{\mathrm{PPS}}\right)=\frac{1}{n} \frac{1}{n-1} \sum_{k=1}^{n}\left(\bar{y}_{a_{k}}-\hat{\bar{Y}}_{\mathrm{PPS}}\right)^{2}
$$

That is, in the mean estimation under PPS sampling, we can safely treat $\bar{y}_{a_{1}}, \bar{y}_{a_{2}}, \cdots, \bar{y}_{a_{n}}$ as an IID sample with $E\left(\bar{y}_{a_{k}}\right)=\bar{Y}$ and apply Lemma 5.1.

# 5.3 Poisson sampling 

Poisson sampling is a generalization of Bernoulli sampling by allowing unequal probability selection. In Poisson sampling, the sample selection indicator function $I_{i}$ follows

$$
I_{i} \stackrel{\text { indep }}{\sim} \operatorname{Bernoulli}\left(\pi_{i}\right), \quad i=1,2, \cdots, N
$$




---

Thus, the sampling design is

$$
\mathcal{P}(\mathcal{A})=\left(\prod_{k \in \mathcal{A}} \pi_{k}\right) \times\left[\prod_{k \in \mathcal{A}^{c}}\left(1-\pi_{k}\right)\right]
$$

for all $\mathcal{A} \subset \mathcal{U}$. Here, $\pi_{i}$ is the first-order inclusion probability. The following result, also presented in Tillé (2020), gives a useful interpretation of Poisson sampling.
Lemma 5.2. The sampling design that maximizes entropy

$$
\mathcal{I}(\mathbf{p})=-\sum_{\mathcal{A} \in \mathbb{A}} \mathcal{P}(\mathcal{A}) \log \{\mathcal{P}(\mathcal{A})\}
$$

on $\mathbb{A}=\{\mathcal{A} ; \mathcal{A} \subset \mathcal{U}\}$ with fixed inclusion probabilities $\pi_{k}, k \in \mathcal{U}$, is the Poisson sampling design.
Proof. We wish to find the maximizer of $\mathcal{I}(\mathbf{p})$ in (5.6) subject to

$$
\sum_{\mathcal{A} \in \mathbb{A}} I(k \in \mathcal{A}) \mathcal{P}(\mathcal{A})=\pi_{k}, k \in \mathcal{U}
$$

and

$$
\sum_{\mathcal{A} \in \mathbb{A}} \mathcal{P}(\mathcal{A})=1
$$

Using Lagrange multiplier method, we can construct

$$
\begin{aligned}
\mathcal{Q}=- & \sum_{\mathcal{A} \in \mathbb{A}} \mathcal{P}(\mathcal{A}) \log \{\mathcal{P}(\mathcal{A})\}+\sum_{k \in \mathcal{U}} \theta_{k}\left\{\sum_{\mathcal{A} \in \mathbb{A}} I(k \in \mathcal{A}) \mathcal{P}(\mathcal{A})-\pi_{k}\right\} \\
& +\lambda\left\{\sum_{\mathcal{A} \in \mathbb{A}} \mathcal{P}(\mathcal{A})-1\right\}
\end{aligned}
$$

Solving

$$
\frac{\partial}{\partial \mathcal{P}(\mathcal{A})} \mathcal{Q}=-1-\log \{\mathcal{P}(\mathcal{A})\}+\sum_{k \in \mathcal{U}} \theta_{k} I(k \in \mathcal{A})+\lambda=0
$$

we obtain

$$
\mathcal{P}(\mathcal{A})=\exp \left(\sum_{k \in \mathcal{U}} \theta_{k} I_{k}-\mu\right)
$$

where $I_{k}=I(k \in \mathcal{A})$ and $\mu=1-\lambda$. Using (5.8), we obtain

$$
\begin{aligned}
\exp (\mu) & =\sum_{\mathcal{A} \subset \mathcal{U}} \prod_{k \in \mathcal{A}} \exp \left(\theta_{k}\right) \\
& =\prod_{k \in \mathcal{U}}\left\{1+\exp \left(\theta_{k}\right)\right\}
\end{aligned}
$$




---

where the second equality follows from

$$
\prod_{k \in U}\left(a_{k}+b_{k}\right)=\sum_{A \subset U}\left\{\prod_{i \in A} a_{i} \cdot \prod_{j \in U / A} b_{j}\right\}
$$

Also, using (5.7), we obtain

$$
\begin{aligned}
\pi_{k} & =\frac{\sum_{A \in \mathcal{A}} \mathbb{I}(k \in A) \prod_{i \in A} \exp \left(\theta_{i}\right)}{\exp (\mu)} \\
& =\frac{\exp \left(\theta_{k}\right) \sum_{A \in \mathcal{U} /\{k\}} \prod_{i \in A} \exp \left(\theta_{i}\right)}{\exp (\mu)} \\
& =\frac{\exp \left(\theta_{k}\right) \prod_{i \in U /\{k\}}\left\{1+\exp \left(\theta_{i}\right)\right\}}{\exp (\mu)} \\
& =\frac{\exp \left(\theta_{k}\right)}{1+\exp \left(\theta_{k}\right)} \cdot \frac{\prod_{i \in U}\left\{1+\exp \left(\theta_{i}\right)\right\}}{\exp (\mu)} \\
& =\frac{\exp \left(\theta_{k}\right)}{1+\exp \left(\theta_{k}\right)}
\end{aligned}
$$

where the third equality follows from (5.11) and the fifth equality follows from (5.10). Thus, we have

$$
\exp \left(\theta_{k}\right)=\frac{\pi_{k}}{1-\pi_{k}}
$$

and, by $(5.9)$,

$$
\begin{aligned}
\mathbb{P}(\mathcal{A}) & =\frac{\exp \left(\sum_{k \in A} \theta_{k}\right)}{\sum_{A \subset U} \exp \left(\sum_{k \in A} \theta_{k}\right)} \\
& =\frac{\prod_{k \in A} \frac{\pi_{k}}{1-\pi_{k}}}{\prod_{k \in U} \frac{1}{1-\pi_{k}}} \\
& =\left(\prod_{k \in A} \pi_{k}\right) \times\left\{\prod_{k \in A^{c}}\left(1-\pi_{k}\right)\right\}
\end{aligned}
$$

The entropy function in (5.6) is a measure of randomnesss of a probability distribution. Thus, the Poisson sampling design is the most random design possible which respects a priori fixed first-order inclusion probabilities (Tillé, 2020).

Poisson sampling is rarely used in practice, but it is useful in understanding the basic nature of unequal probability sampling. Under Poisson sampling, the variance of HT estimator is expressed as

$$
\mathbb{V}\left(\hat{Y}_{\mathrm{HT}}\right)=\sum_{i=1}^{N}\left(\frac{1}{\pi_{i}}-1\right) y_{i}^{2}
$$




---

The following theorem provides a result for the optimal choice of $\pi_{i}$ under Poisson sampling.

Theorem 5.1. Consider a Poisson sampling with first-order inclusion probability $\pi_{i}$. Given the same (expected) sample size, the variance of HT estimator under Poisson sampling is minimized when

$$
\pi_{i} \propto y_{i}
$$

Proof. Using the Cauchy-Schwarz inequality, we have

$$
\left(\sum_{i=1}^{N} \frac{y_{i}^{2}}{\pi_{i}}\right)\left(\sum_{i=1}^{N} \pi_{i}\right) \geq\left(\sum_{i=1}^{N} y_{i}\right)^{2}
$$

and using the fact that $\sum_{i=1}^{N} \pi_{i}=n$ is a fixed constant, we obtain (5.13) is minimized when (5.14) holds.

Thus, under Poisson sampling, we have only to make $\pi_{i}$ proportional to $y_{i}$. However, since we never observed $y_{i}$ at the time of sampling design, we cannot use $y_{i}$ but instead use $x_{i}$ in the population that is believed to be proportional to $y_{i}$.

Poisson sampling, as with Bernoulli sampling, has the disadvantage that the sample size $n$ is random. In the extreme case, we may have $n$ equal to zero. Thus, Poisson sampling has limited usage in practice, but is useful in developing theory.

If Poisson sampling is used, we can consider the following estimator which is first proposed by Hajék:

$$
\hat{Y}_{\pi}=N \frac{\sum_{i \in \mathcal{A}} \pi_{i}^{-1} y_{i}}{\sum_{i \in \mathcal{A}} \pi_{i}^{-1}}
$$

Hajék estimator is a special case of the ratio estimator that we will study in Chapter 8. The asymptotic variance can be obtained, by applying Taylor method,

$$
\begin{aligned}
\hat{Y}_{\pi} & =N \frac{\hat{Y}_{\mathrm{HT}}}{\hat{N}_{\mathrm{HT}}} \\
& \cong N \frac{E\left(\hat{Y}_{\mathrm{HT}}\right)}{E\left(\hat{N}_{\mathrm{HT}}\right)}+N \frac{1}{E\left(\hat{N}_{\mathrm{HT}}\right)}\left\{\hat{Y}_{\mathrm{HT}}-E\left(\hat{Y}_{\mathrm{HT}}\right)\right\}-N \frac{E\left(\hat{Y}_{\mathrm{HT}}\right)}{\left\{E\left(\hat{N}_{\mathrm{HT}}\right)\right\}^{2}}\left\{\hat{N}_{\mathrm{HT}}-E\left(\hat{N}_{\mathrm{HT}}\right)\right\} \\
& \cong \bar{Y}+\left(\hat{Y}_{\mathrm{HT}}-\bar{Y} \hat{N}_{\mathrm{HT}}\right) .
\end{aligned}
$$

Thus, we obtain

$$
\begin{aligned}
V\left(\hat{Y}_{\pi}\right) & \cong V\left\{\sum_{i \in \mathcal{A}} \frac{1}{\pi_{i}}\left(y_{i}-\bar{Y}\right)\right\} \\
& =\sum_{i=1}^{N}\left(\frac{1}{\pi_{i}}-1\right)\left(y_{i}-\bar{Y}\right)^{2}
\end{aligned}
$$




---

Comparing (5.16) with (5.13), the variance of the HT estimator, the only difference is whether we use $y_{i}^{2}$ or $\left(y_{i}-\bar{Y}\right)^{2}$ in the variance formula. In many cases, we may say that the Hajek estimator is more efficient than the HT estimator under Poisson sampling asymptotically. Furthermore, the Hajek estimator is location invariant after a location transformation of the form $y_{i} \rightarrow y_{i}+c$.

# 5.4 Maximum Entropy Sampling 

The Poisson sampling introduced in the previous section has the drawback of a random sample size. Using the fact that the Poisson sampling is a particular sampling design maximizing the entropy in (5.6) with the constraints on the first-order inclusion probabilities, we can impose an additional constraint on the sample size in the optimization problem. The resulting sampling design is called the maximum entropy sampling design, which was formally studied by Chen et al. (1994) and Tillé (2006). Maximum entropy sampling is closely related to the rejective Poisson sampling of Hájek (1981) and Fuller (2009). In fact, as we can see below, maximum entropy sampling can be implemented using rejective Poisson sampling.

Let $\mathcal{A}_{n}=\{A ; A \subset \mathcal{U},|A|=n\}$ be the set of all possible samples of size $n$. The maximum entropy sampling can be defined as maximizing the entropy in (5.6) subject to

$$
\sum_{A \in \mathcal{A}_{n}} I(k \in A) P(A)=\pi_{k}, k \in \mathcal{U}
$$

and

$$
\sum_{A \in \mathcal{A}_{n}} P(A)=1
$$

Using the same argument for proving Lemma 5.2, the solution to this optimization problem is

$$
P(A)= \begin{cases}\frac{\exp \left(\sum_{k \in A} \theta_{k}\right)}{\sum_{A \in \mathcal{A}_{n}} \exp \left(\sum_{k \in A} \theta_{k}\right)} & \text { if }|A|=n \\ 0 & \text { otherwise }\end{cases}
$$

where $\theta_{1}, \cdots, \theta_{N}$ are the parameters of the maximum entropy design and are determined by (5.17). Thus, (5.19) is the sampling design for the maximum entropy sampling. Equation (5.17) is a system of $N$ equations to solve $\theta_{k}$. Tillé (2006) discussed a fast algorithm for computing $\theta_{k}$ satisfying (5.17).

Now, to compare the maximum entropy sampling with Poisson sampling, define

$$
\tilde{\pi}_{k}=\frac{\exp \left(\theta_{k}+C\right)}{1+\exp \left(\theta_{k}+C\right)}
$$




---

where $C$ is chosen to satisfy

$$
\sum_{k \in U} \tilde{\pi}_{k}=n
$$

We can consider the rejective Poisson sampling as follows:
[Step 1] Use $\tilde{\pi}_{k}$ in (5.20) to select a Poisson sample.
[Step 2] Check if the realized sample size of the Poisson sample is equal to $n$, the target sample size. If yes, it is the final sample. Otherwise, goto [Step 1].

Because the sampling design of the Poisson sampling in [Step 1] is, by (5.12),

$$
\tilde{P}(A)=\frac{\exp \left(\sum_{k \in A} \theta_{k}+C\right)}{\sum_{A \subset U} \exp \left(\sum_{k \in A} \theta_{k}+C\right)}
$$

the maximum entropy sampling design in (5.19) can be written as

$$
P(A)=\frac{\tilde{P}(A)}{\sum_{A \in \mathcal{A}_{n}} \tilde{P}(A)}, A \in \mathcal{A}_{n}
$$

Thus, $P(A)$ in (5.19) is the conditional Poisson sampling conditional on the fixed sample size $n$.

In order to construct an algorithm to implement the maximum entropy design, it is necessary to be able to calculate the vector $\tilde{\boldsymbol{\pi}}=\left(\tilde{\pi}_{1}, \cdots, \tilde{\pi}_{N}\right)^{\prime}$ from the vector $\boldsymbol{\pi}=\left(\pi_{1}, \cdots, \pi_{N}\right)^{\prime}$. This algorithm is implemented in the function UPmaxentropy of 'sampling' package R developed by Tillé and Matei (2016).

# $5.5 \pi$ ps sampling 

The PPS sampling introduced in the previous section has many advantages: it is very easy to implement, the estimation formula is simple. However, since it is a with-replacement sampling, it is inefficient in the sense that it allows for duplicated sample elements. Let $x_{i}$ be the size measure that we want to make $\pi_{i} \propto x_{i}$ as close as possible. The $\pi \mathrm{ps}(\pi$ proportional to size) sampling refers to a set of sampling designs that satisfies the following conditions:

1. The sampling design is a fixed-size sampling design that does not allow for duplication.
2. The first-order inclusion probability $\pi_{i}$ satisfies $\pi_{i} \propto x_{i}$.
3. The second order inclusion probability satisfies $\pi_{i j}>0$ and $\pi_{i j}<$ $\pi_{i} \pi_{j}(i \neq j)$.



---

The third condition guarantees that the SYG variance estimator is always nonnegative.

For a fixed-size design, $\pi_{k} \propto x_{k}$ and $\sum_{i=1}^{N} \pi_{i}=n$ leads to

$$
\pi_{k}=\frac{n x_{k}}{\sum_{i=1}^{N} x_{i}}
$$

If some $x_{k}$ satisfies $x_{k}>(N / n) \bar{X}_{N}$, then we have $\pi_{i}>1$. Thus, the exact proportionality $\pi_{i} \propto x_{i}$ is not always possible. In practice, the units with $\pi_{k}>1$ are automatically selected. The inclusion probabilities are recalculated in the same way excluding the element that is automatically selected. That is, if $k$ satisfies $\pi_{k}>1$, then we set $\pi_{k}=1$ and recompute

$$
\pi_{i}=(n-1) \frac{x_{i}}{\sum_{i \neq k} x_{i}}
$$

This operation is repeated until $\pi_{i} \leq 1$ for all element in the population.
For $n=1$, the $\pi$ ps sampling is the same as the PPS sampling. There are two approaches of implementing a PPS sampling of size $n=1$. One is the cumulative total method, and the other is the Lahiri's method. The cumulative total method is described as follows:
[Step 1] Set $T_{0}=0$ and compute $T_{k}=T_{k-1}+x_{k}, k=1,2, \cdots, N$.
[Step 2] Draw $\epsilon \sim \operatorname{Unif}(0,1)$. If $\epsilon \in\left(T_{k-1} / T_{N}, T_{k} / T_{N}\right)$, element $k$ is selected.
The cumulative total method is very popular because it is easy to understand. It needs a list of all $x_{k}$ in the population.

The other method, developed by Lahiri (1951), can be described as follows:
[Step 0] Choose $M>\left\{x_{1}, x_{2}, \cdots, x_{N}\right\}$. Set $r=1$.
[Step 1] Draw $k_{r}$ by SRS from $\{1,2, \cdots, N\}$.
[Step 2] Draw $\epsilon_{r} \sim \operatorname{Unif}(0,1)$.
[Step 3] If $\epsilon_{r} \leq x_{k_{r}} / M$, then select element $k_{r}$ and stop. Otherwise, reject $k_{r}$ and goto Step 1 with $r=r+1$.

Lahiri's method does not need a list of all $x_{k}$ in the population, but requires the knowledge of the upper bound of $x_{k}$, denoted by $M$.

A formal justification for Lahiri's method can be described as follows:

$$
\begin{aligned}
\pi_{k} & =\operatorname{Pr}(k \in A) \\
& =\sum_{r=1}^{\infty} \operatorname{Pr}(k \in A, R=r) \\
& =\sum_{r=1}^{\infty} \operatorname{Pr}\left\{K_{r}=k, \epsilon_{r}<\frac{x_{k_{r}}}{M}, \bigcap_{j=1}^{r-1}\left(\epsilon_{j}>\frac{x_{k_{j}}}{M}\right)\right\} \\
& =\sum_{r=1}^{\infty} \frac{1}{N} \frac{x_{k}}{M} \times \prod_{j=1}^{r-1} \operatorname{Pr}\left\{\epsilon_{j}>\frac{x_{k_{j}}}{M}\right\}
\end{aligned}
$$




---

Since

$$
\begin{aligned}
\operatorname{Pr}\left(\epsilon_{j}>\frac{x_{k_{j}}}{M}\right) & =\sum_{k} \operatorname{Pr}\left(\epsilon_{j}>\frac{x_{k_{j}}}{M} \mid k_{j}=k\right) \operatorname{Pr}\left(K_{j}=k\right)=\sum_{k}\left(1-\frac{x_{k}}{M}\right) \frac{1}{N}=1-\frac{\bar{x}_{U}}{M} \\
\text { where } \bar{x}_{U} & =N^{-1} \sum_{i=1}^{N} x_{k_{i}}, \text { we can obtain } \\
\pi_{k} & =\sum_{r=1}^{\infty} \frac{1}{N} \frac{x_{k}}{M}\left(1-\frac{\bar{x}_{U}}{M}\right)^{r-1}=\frac{x_{k}}{\sum_{i=1}^{N} x_{i}}
\end{aligned}
$$

We now discuss $\pi$ ps sampling for $n=2$. Most of the existing schemes for fixed-size $\pi$ ps sampling with $n>2$ are quite complicated. The interested reader is referred to Tillé (2006). To discuss $\pi$ ps sampling of size $n=2$, let $\theta_{i}$ be the probability of selecting unit $i$ in the first draw of the $\pi$ ps sampling and let $\theta_{j \mid i}$ be the conditional probability of selecting unit $j$ in the second draw given that unit $i$ is selected in the first draw. Thus, writing $p_{i}=x_{i} /\left(\sum_{j=1}^{N} x_{j}\right)$, the problem at hand is to find a set of $\theta_{i}$ and $\theta_{j \mid i}$ satisfying

$$
\pi_{i}=2 p_{i}
$$

and

$$
\sum_{i} \theta_{i}=\sum_{j} \theta_{j \mid i}=1
$$

Since

$$
\pi_{i j}=\theta_{i} \theta_{j \mid i}+\theta_{j} \theta_{i \mid j}
$$

and, as it is a fixed-size sampling design, we can use (2.2) to get $\sum_{j \neq i} \pi_{i j}=\pi_{i}$, which implies

$$
\pi_{i}=\theta_{i}+\sum_{j \neq i} \theta_{j} \theta_{i \mid j}
$$

Thus, constraint (5.21) reduces to

$$
\theta_{i}+\sum_{j \neq i} \theta_{j} \theta_{i \mid j}=2 p_{i}
$$

Since there are $N^{2}$ unknowns with $N$ equations, we have many solutions to (5.23).

Brewer (1963) proposed using

$$
\theta_{i} \propto \frac{p_{i}\left(1-p_{i}\right)}{1-2 p_{i}}
$$

and

$$
\theta_{j \mid i} \propto p_{j}
$$




---

to obtain (5.23), while Durbin (1967) proposed using

$$
\theta_{i}=p_{i} \quad \text { and } \quad \theta_{j \mid i} \propto p_{j}\left(\frac{1}{1-2 p_{i}}+\frac{1}{1-2 p_{j}}\right)
$$

to achieve the same goal.
In Brewer's method, we first choose $\theta_{j \mid i}=p_{j} /\left(1-p_{i}\right)$ for $i \neq j$ and use (5.23) to get

$$
\begin{aligned}
2 p_{i} & =\theta_{i}+\sum_{j \neq i} \theta_{j} \frac{p_{i}}{1-p_{j}} \\
& =\theta_{i}+p_{i}\left(B-\frac{\theta_{i}}{1-p_{i}}\right)
\end{aligned}
$$

where $B=\sum_{j=1}^{N} \theta_{j} /\left(1-p_{j}\right)$. Thus, we get

$$
\theta_{i}=\frac{2 p_{i}-p_{i} B}{1-\frac{p_{i}}{1-p_{i}}}=\frac{(2-B) p_{i}\left(1-p_{i}\right)}{1-2 p_{i}}
$$

which proves (5.24).
Using (5.22), Brewer's method leads to

$$
\pi_{i j}=C \cdot p_{i} p_{j}\left(\frac{1}{1-2 p_{i}}+\frac{1}{1-2 p_{j}}\right)
$$

for some $C$. Now,

$$
\begin{aligned}
\sum_{j \neq i} \pi_{i j} & =C \cdot p_{i} \sum_{j \neq i} p_{j}\left(\frac{1}{1-2 p_{i}}+\frac{1}{1-2 p_{j}}\right) \\
& =C \cdot p_{i}\left(\sum_{j=1}^{N} \frac{p_{j}}{1-2 p_{j}}-\frac{p_{i}}{1-2 p_{i}}+\frac{1-p_{i}}{1-2 p_{i}}\right)=C \cdot p_{i}\left(\sum_{j=1}^{N} \frac{p_{j}}{1-2 p_{j}}+1\right)
\end{aligned}
$$

Because

$$
\pi_{i}=\sum_{j \neq i} \pi_{i j}=2 p_{i}
$$

we get

$$
\pi_{i j}=\frac{2 p_{i} p_{j}}{1+K\left(\frac{1}{1-2 p_{i}}+\frac{1}{1-2 p_{j}}\right)}
$$

where $K=\sum_{i=1}^{N}\left(1-2 p_{i}\right)^{-1} p_{i}$.
In Durbin (1967), we set $\theta_{i}=p_{i}=\pi_{i} / 2$ and $\theta_{j \mid i}=\pi_{i j} / \pi_{i}$ with $\pi_{i j}$ in (5.28). Thus, we obtain (5.25).




---

We now introduce one $\pi$ ps method proposed by Chao (1982). Chao's sampling is a special case of reservoir sampling with unequal probability of selection. The sampling plan can be described by induction. Let $U_{k}=\{1, \cdots, k\}$ be the set of elements in the finite population up to the element $k$. Let $A_{k}$ be the set of sample elements selected from $U_{k}$ with the first-order inclusion probability proportional to $x$. Let $\pi_{(k ; i)}=\mathrm{P}\left(i \in A_{k} \mid U_{k}\right)$ be the corresponding first-order inclusion probability of the unit $i$ from $U_{k}$ satisfying

$$
\pi_{(k ; i)}=n \cdot \frac{x_{i}}{\sum_{j=1}^{k} x_{j}}
$$

Now, for $U_{k+1}=U_{k} \cup\{k+1\}$, we update the sample as follows:

1. Select element $k+1$ with the selection probability $p_{k+1}=n W_{k+1}$, where

$$
W_{k+1}=\frac{x_{k+1}}{\sum_{j=1}^{k+1} x_{j}}
$$

2. If $k+1$ is selected from Step 1 , remove one element (say $j$ ) from $A_{k}$ with probability $1 / n$ and set $A_{k+1}=A_{k} \cup\{k+1\} /\{j\}$. Otherwise, set $A_{k+1}=A_{k}$.
To explain Chao's sampling, note that we can write

$$
\begin{aligned}
\mathrm{P}\left(j \in A_{k+1} \mid U_{k+1}\right)= & \mathrm{P}\left(j \in A_{k} \mid U_{k}\right) \mathrm{P}\left(j \in A_{k+1} \text { and } k+1 \in A_{k+1} \mid U_{k+1}, A_{k}\right) \\
& +\mathrm{P}\left(j \in A_{k} \mid U_{k}\right) \mathrm{P}\left(k+1 \notin A_{k+1} \mid U_{k+1}, A_{k}\right)
\end{aligned}
$$

Now, by the Chao's sampling mechanism, we obtain

$$
\begin{aligned}
& \mathrm{P}\left(j \in A_{k+1} \text { and } k+1 \in A_{k+1} \mid U_{k+1}, A_{k}\right) \\
= & \mathrm{P}\left(j \in A_{k+1} \mid U_{k+1}, A_{k}\right) \mathrm{P}\left(k+1 \in A_{k+1} \mid U_{k+1}, A_{k}\right) \\
= & \frac{n-1}{n} \times p_{k+1}
\end{aligned}
$$

and

$$
\mathrm{P}\left(k+1 \notin A_{k+1} \mid U_{k+1}, A_{k}\right)=1-p_{k+1}
$$

Thus, (5.30) reduces to

$$
\mathrm{P}\left(j \in A_{k+1} \mid U_{k+1}\right)=\mathrm{P}\left(j \in A_{k} \mid U_{k}\right) \times\left(1-W_{k+1}\right)
$$

Now, by (5.29), we obtain

$$
\mathrm{P}\left(j \in A_{k+1} \mid U_{k+1}\right)=n \cdot \frac{x_{j}}{\sum_{j=1}^{k+1} x_{j}}
$$

Thus, as long as (5.29) holds, the above procedure leads to

$$
\pi_{(k+1 ; i)}=n \cdot \frac{x_{i}}{\sum_{j=1}^{k+1} x_{j}}
$$

which is a $\pi$ ps sampling from population $U_{k+1}$.




---

Remark 5.1. In Chao's sampling, the initial sample $S_{n}=\{1, \cdots, n\}$ for $k=n$ does not satisfy (5.29). In fact, by (5.31),

$$
\pi(k+1 ; j)=P\left(j \in S_{j} \mid U_{j}\right) \prod_{i=j}^{k}\left(1-W_{i+1}\right)=\frac{P\left(j \in S_{j} \mid U_{j}\right)}{\sum_{i=1}^{k+1} x_{i}}
$$

Now, since

$$
P\left(j \in S_{j} \mid U_{j}\right)= \begin{cases}1 & \text { if } j \leq n \\ n W_{j} & \text { if } j>n\end{cases}
$$

result (5.32) holds only for $i>n$. The first-order inclusion probability of unit $j \leq n$ in the $(k+1)$-th population is then

$$
\pi(k+1 ; j)=\frac{\sum_{i=1}^{n} x_{i}}{\sum_{i=1}^{k+1} x_{i}}=\frac{n}{\bar{x}_{n}} \sum_{i=1}^{k+1} x_{i}=\frac{1}{n} \sum_{i=1}^{n} \tilde{\pi}(k+1 ; i),
$$

where $\tilde{\pi}(k+1 ; i)=n x_{i} /\left(\sum_{j=1}^{k+1} x_{j}\right)$.

# 5.6 Systematic $\pi$ ps sampling 

Systematic $\pi p s$ sampling is similar to systematic sampling but allows for unequal probability of sample selection. Let $a=\sum_{i=1}^{N} x_{i} / n$ be the sampling interval for systematic sampling. Assume $x_{k}<a$ for all $k \in U$. (If some of the $x_{k}$ 's are greater than $a$, then such elements are selected in advance and then the systematic sampling is applied in the reduced finite population.) Systematic $\pi p s$ sampling can be described as follows.

1. Choose $R \sim \operatorname{Unif}(0, a]$
2. Unit $k$ is selected iff

$$
L_{k}<R+l \cdot a \leq U_{k}
$$

for some $l=0,1, \cdots, n-1$, where $L_{k}=\sum_{j=1}^{k-1} x_{j}$ with $L_{0}=0$ and $U_{k}=L_{k}+x_{k}$.

Example 5.3. For example, consider the following artificial finite population of size $N=4$.





---

To obtain a systematic sample of size $n=2$ with the first-order inclusion probability proportional to $x_{i}$, note that $a=100 / 2=50$. Thus, we first generate $R$ from a uniform distribution $(0,50]$. If $R$ belongs to $(0,10]$, we select $A=$ $\{1,3\}$. If $R$ belongs to $(10,30]$, we select $A=\{2,4\}$. If $R$ belongs to $(30,50]$, we select $\{3,4\}$. The sampling distribution of the resulting sample will be

$$
P(A)= \begin{cases}0.2, & \text { if } A=\{1,3\} \\ 0.4, & \text { if } A=\{2,4\} \\ 0.4, & \text { if } A=\{3,4\}\end{cases}
$$

To compute the first-order inclusion probability of unit $k$, let $l$ be the integer satisfying $l \cdot a \leq L_{k}<U_{k} \leq(l+1) a$.

$$
\begin{aligned}
\operatorname{Pr}(k \in A) & =\operatorname{Pr}\left\{L_{k}<R+l \cdot a \leq U_{k}\right\} \\
& =\int_{L_{k}-l \cdot a}^{U_{k}-l \cdot a} \frac{1}{a} d t=x_{k} / a=\frac{n x_{k}}{\sum_{k \in U} x_{k}}
\end{aligned}
$$

The systematic $\pi p s$ sampling is easy to implement but it does not allow for design-unbiased variance estimator, as is the case with the classical systematic sampling.




---

# 6 

## Cluster Sampling: Single stage cluster sampling

### 6.1 Introduction

Element sampling designs are not always feasible when there is no sampling frame for the survey units. Instead, the sampling frame is often available in the form of clusters, such as schools or districts. In this case, cluster sampling that samples clusters is commonly used. Also, cluster sampling is often costeffective in terms of reducing the travel cost and also controlling the field work of the interviewers.

In cluster sampling, the finite population is grouped into clusters. A probability sample of clusters is selected, and every element in the selected clusters is surveyed. Clusters are also called primary sampling units (PSUs). If a probability sample of PSUs is drawn and every element in the selected PSUs is measured, the sampling design is called single-stage cluster sampling. On the other hand, if another probability sampling is used to draw sample elements in the selected clusters, the sampling design is called a two-stage sampling design. Multi-stage sampling consists of three or more stages of sampling. There is a hierarchy of sampling units: primary sampling units, secondary sampling units within the PUS, and so on. The sampling units in the last-stage sampling are called the ultimate sampling units. In this chapter, we will focus on single-stage sampling.

Let $\mathcal{U}_{I}=\left\{1, \cdots, N_{I}\right\}$ be the index set of clusters in the population. Let $\mathcal{U}_{i}$ be the set of elements in the $i$-th cluster of size $M_{i}$. Let $y_{i j}$ be the measurement associated with element $i$ in cluster $i$. The population total of $y$ is denoted by $Y=\sum_{i=1}^{N_{I}} \sum_{j \in \mathcal{U}_{i}} y_{i j}=\sum_{i=1}^{N_{I}} Y_{i}=\sum_{i=1}^{N_{I}} M_{i} \bar{Y}_{i}$, where $\bar{Y}_{i}=Y_{i} / M_{i}$ is the population mean of $y$ in cluster $i$.

In the single-stage sampling, we select $\mathcal{A}_{I}$ from $\mathcal{U}_{I}$ by probability sampling. The index set $\mathcal{A}$ of the sample elements can be written as $\mathcal{A}=\cup_{i \in \mathcal{A}_{I}} \mathcal{U}_{i}$ in single-stage sampling. Let $n_{I}=\left|\mathcal{A}_{I}\right|$ be the number of sampled clusters. Let $n_{\mathcal{A}}=|\mathcal{A}|$ be the number of sampled elements. Under single-stage cluster sampling, we have $n_{\mathcal{A}}=\sum_{i \in \mathcal{A}_{I}} M_{i}$.




---

# 6.2 Single-stage cluster sampling: Equal Size Case 

When the cluster size $M_{i}$ is equal to $M$, the following sampling design can be considered.

1. Simple random sampling of $n_{I}$ clusters from $N_{I}$ clusters.
2. Observe all the elements in the selected clusters.

Such a sampling design is called simple random cluster sampling. In this case, the HT estimator of $Y=\sum_{i=1}^{N_{I}} Y_{i}$ is

$$
\hat{Y}_{\mathrm{HT}}=\sum_{i \in A_{I}} \frac{1}{\pi_{I i}} Y_{i}=\frac{N_{I}}{n_{I}} \sum_{i \in A_{I}} Y_{i}
$$

where $\pi_{I i}=\mathbb{P}\left(i \in A_{I}\right)$ is the cluster-level first-order inclusion probability and is equal to $\pi_{I i}=n_{I} / N_{I}$ under simple random cluster sampling. Thus, the HT estimator of $\bar{Y}_{\mathcal{U}}=Y /\left(N_{I} M\right)$ is

$$
\hat{\bar{Y}}_{\mathcal{U}}=\frac{\hat{Y}_{\mathrm{HT}}}{N_{I} M}=\frac{1}{n_{I}} \frac{1}{M} \sum_{i \in A_{I}} Y_{i}=\frac{1}{n_{I}} \sum_{i \in A_{I}} \bar{Y}_{i}
$$

Note that $\hat{\bar{Y}}_{\mathcal{U}}$ is the sample mean of $\bar{Y}_{i}$. Thus, the sampling variance of $\hat{\bar{Y}}_{\mathcal{U}}$ is

$$
\mathbb{V}\left(\hat{\bar{Y}}_{\mathcal{U}}\right)=\frac{1}{n_{I}}\left(1-\frac{n_{I}}{N_{I}}\right) \frac{1}{N_{I}-1} \sum_{i=1}^{N_{I}}\left(\bar{Y}_{i}-\bar{Y}_{\mathcal{U}}\right)^{2}
$$

where $\bar{Y}_{i}=\sum_{j=1}^{M} y_{i j} / M$ and $\bar{Y}_{\mathcal{U}}=Y /\left(N_{I} M\right)=\sum_{i=1}^{N_{I}} \bar{Y}_{i} / N_{I}$.
To discuss the variance form in (6.1), the following ANOVA table is considered.

TABLE 6.1
ANOVA table for the population of clusters with equal size

| Source | d.f | Sum of Squares | Mean SS |
| :--- | :---: | :---: | :---: |
| Between cluster | $N_{I}-1$ | $S S B$ | $S_{b}^{2}$ |
| Within cluster | $N_{I}(M-1)$ | $S S W$ | $S_{w}^{2}$ |
| Total | $N_{I} M-1$ | $S S T$ | $S^{2}$ |

Here, the sum of squares are defined as below and the mean sum of squares




---

are computed by dividing the sum of squares by their degrees of freedom

$$
\begin{aligned}
\mathrm{SST} & =\sum_{i=1}^{N I} \sum_{j=1}^{M}\left(y_{i j}-\bar{Y}\right)^{2} \\
\mathrm{SSB} & =\sum_{i=1}^{N I} \sum_{j=1}^{M}\left(\bar{Y}_{i}-\bar{Y}\right)^{2} \\
\mathrm{SSW} & =\sum_{i=1}^{N I} \sum_{j=1}^{M}\left(y_{i j}-\bar{Y}_{i}\right)^{2}
\end{aligned}
$$

Note that, since $\mathrm{SST}=\mathrm{SSB}+\mathrm{SSW}, S^{2}$ is a weighted average of two mean sum of squares terms:

$$
\begin{aligned}
S^{2} & =\frac{\mathrm{SST}}{N I M-1} \\
& =\frac{(N I-1) S_{b}^{2}+N I(M-1) S_{w}^{2}}{N I M-1} \\
& \cong \frac{S_{b}^{2}+(M-1) S_{w}^{2}}{M}
\end{aligned}
$$

Thus, since $\mathrm{SSB}=M \cdot \sum_{i=1}^{N I}\left(\bar{Y}_{i}-\bar{Y}\right)^{2}$, we have

$$
\frac{1}{N I-1} \sum_{i=1}^{N I}\left(\bar{Y}_{i}-\bar{Y}_{U}\right)^{2}=\frac{\mathrm{SSB}}{(N I-1) M}=\frac{S_{b}^{2}}{M}
$$

and the variance expression in (6.1) can be written as

$$
\mathcal{V}\left(\hat{\bar{Y}}_{U}\right)=\frac{1}{n I M}\left(1-\frac{n I}{N I}\right) S_{b}^{2}
$$

Now, let's compare the variance in (6.2) with the variance of another HT estimator under simple random sample of the same size, which is

$$
\mathcal{V}_{\mathrm{SRS}}\left(\hat{\bar{Y}}_{U}\right)=\frac{1}{n I M}\left(1-\frac{n I M}{N I M}\right) S^{2}
$$

as $n=n I M$ is the size of the sampled elements. To compare (6.3) with (6.2), we first introduce the concept of intracluster correlation coefficient. The intraclass correlation coefficient is the population correlation coefficient between two units in the same cluster.




---

Definition 6.1. Intraclass correlation coefficient:

$$
\begin{aligned}
\rho & =\frac{\operatorname{Cov}\left[y_{i j}, y_{i k} \mid j \neq k\right]}{\sqrt{\mathcal{V}\left(y_{i j}\right)} \sqrt{\mathcal{V}\left(y_{i k}\right)}} \\
& =\frac{\sum_{i=1}^{N_{I}} \sum_{j \neq k} \sum\left(y_{i j}-\bar{Y}\right)\left(y_{i k}-\bar{Y}\right) / \sum_{i=1}^{N_{I}} M(M-1)}{\sum_{i=1}^{N_{I}} \sum_{j=1}^{M}\left(y_{i j}-\bar{Y}\right)^{2} / \sum_{i=1}^{N_{I}} M} \\
& =\frac{1}{M-1} \frac{\sum_{i=1}^{N_{I}} \sum_{j \neq k} \sum\left(y_{i j}-\bar{Y}\right)\left(y_{i k}-\bar{Y}\right)}{\sum_{i=1}^{N_{I}} \sum_{j=1}^{M}\left(y_{i j}-\bar{Y}\right)^{2}}
\end{aligned}
$$

Using the following identity

$$
\begin{aligned}
& \sum_{i} \sum_{j \neq k} \sum_{k}\left(y_{i j}-\bar{Y}\right)\left(y_{i k}-\bar{Y}\right) \\
& =\sum_{i}\left\{\sum_{j}\left(y_{i j}-\bar{Y}\right)\right\}^{2}-\sum_{i} \sum_{j}\left(y_{i j}-\bar{Y}\right)^{2} \\
& =M \cdot \mathrm{SSB}-\mathrm{SST}
\end{aligned}
$$

we can express

$$
\rho=\frac{M \cdot \mathrm{SSB}-\mathrm{SST}}{(M-1) \mathrm{SST}}=1-\frac{M}{M-1} \frac{\mathrm{SSW}}{\mathrm{SST}}
$$

and so

$$
-\frac{1}{M-1} \leq \rho \leq 1
$$

The minimum value of $\rho$ is achieved when $\mathrm{SSB}=0$ which occurs when $\bar{Y}_{i}$ are all equal. The maximum value of $\rho$ is achieved when $\mathrm{SSW}=0$ which occurs when all elements are homogeneous within clusters (i.e. $y_{i j}=\bar{Y}_{i}$ ). Note that we can also express

$$
\rho=1-\frac{\mathrm{SSW} /\left\{N_{I}(M-1)\right\}}{\mathrm{SST} / N_{I} M} \doteq 1-\frac{S_{w}^{2}}{S^{2}}
$$

The following lemma gives alternative expressions for the mean sum of square terms of the ANOVA table in Table 6.2 in terms of the intracluster correlation coefficient $\rho$.

Lemma 6.1. Using $\rho$, we can express

$$
S_{b}^{2} \doteq S^{2}\{1+(M-1) \rho\}
$$

Proof. From (6.4), we can use SST $=\mathrm{SSB}+\mathrm{SSW}$ to get

$$
\operatorname{SSB}=\frac{1}{M}[1+\rho(M-1)] \mathrm{SST} .
$$

Now, using $S_{b}^{2}=\operatorname{SSB} /\left(N_{I}-1\right) \doteq \operatorname{SSB} / N_{I}$ and $S^{2} \doteq \operatorname{SST} /\left(N_{I} M\right)$, we get (6.6).




---

By (6.6), combining (6.2) and (6.3), we can establish the following theorem, which gives an alternative expression of the sampling variance of the HT estimator in a single-stage cluster sampling design.

Theorem 6.1. Under simple random cluster sampling, for sufficiently large $N$, the variance of HT estimator can be written

$$
V\left(\hat{Y}_{\mathrm{HT}}\right) \doteq V_{\mathrm{SRS}}\left(\hat{Y}_{\mathrm{HT}}\right) \cdot\{1+(M-1) \rho\}
$$

where $\rho$ is the intracluster correlation coefficient and $V_{\text {SRS }}\left(\hat{Y}_{\mathrm{HT}}\right)$ is the variance of HT estimator under SRS of equal size.

The above theorem shows that the sampling variance of the HT estimator under simple random cluster sampling is $\{1+(M-1) \rho\}$ times larger than that of HT estimator under SRS of equal size. Thus, $\{1+(M-1) \rho\}$ is the ratio of two variances and expresses the inverse of the relative efficiency of the simple random cluster sampling over the simple random sampling. Kish (1965) first introduced the concept of the design effect as follows.

Definition 6.2. Design effect (deff) of the sampling design $p(\cdot)$ with the sample size $n=n_{p}$ :

$$
\operatorname{deff}\left(p, \hat{Y}_{\mathrm{HT}}\right)=\frac{V_{p}\left(\hat{Y}_{\mathrm{HT}} \mid n_{p}\right)}{V_{\mathrm{SRS}}\left(\hat{Y}_{\mathrm{HT}} \mid n_{p}\right)}
$$

In simple random cluster sampling, we have

$$
\operatorname{deff}=1+(M-1) \rho
$$

For example, if $\rho=0.1$ and $M=11$, deff $=2$. Thus, even if $\rho$ is low, the design effect can be large if $M$ is large.

There are two usages of the design effect. One is to compare designs. For example, if deff $>1$, then $p(\cdot)$ is less efficient than SRS. If deff $<1$, then $p(\cdot)$ is more efficient than SRS.

The other usage is to determine the sample size. When the design effect of a design $p(\cdot)$ is known, the sample size under the design is determined as follows.

1. Have some desired variance $V^{*}$
2. Under SRS, you can easily find required sample size $n^{*}$
3. Choose $n_{p}^{*}=$ deff $\cdot n^{*}$.



---

Then, ignoring the finite population correction term,

$$
\begin{aligned}
V_{\mathrm{p}}\left(\hat{Y}_{\mathrm{HT}} \mid n_{\mathrm{p}}^{*}\right) & =V_{\mathrm{SRS}}\left(\hat{Y}_{\mathrm{HT}} \mid n_{\mathrm{p}}^{*}\right) \cdot \operatorname{deff} \\
& =\frac{N^{2}}{n_{\mathrm{p}}^{*}} S^{2} \cdot \operatorname{deff} \\
& =\frac{N^{2}}{n^{*}} S^{2} \\
& =V^{*}
\end{aligned}
$$

The sample size $n^{*}$ is often called the effective sample size. It is the sample size required for the given $V^{*}$ if the sample design is SRS. Given the current sample size $n$, the effective sample size $n^{*}$ is calculated by

$$
n^{*}=\frac{n}{\text { deff }}
$$

Example 6.1. Suppose that we are interested in estimating the population proportion of certain characteristics by simple random cluster sampling with $M=200$ elements in the cluster. We want to have a margin of error equal to $2 \%$ at the significant level $\alpha=0.05$. How many sampling clusters are needed for this design? Assume that the intracluster correlation coefficient $\rho=0.05$.

To answer this question, first calculate the effective sample size. The effective sample size is equal to $n^{*}=(0.02)^{-2}=2,500$. The design effect is $1+199 * 0.05 \doteq 11$. Thus, the number of sample clusters is $2,500 * 11 / 200=$ 137.5 .

Example 6.2. Assume that a simple random sample of clusters is selected from a population of clusters of equal size. Suppose that there are $N_{\mathrm{I}}$ clusters in the population and that there are $M$ elements in each cluster. Within the sampled cluster, we used simple random sampling to obtain the observed values of the sample elements. The sample observations are summarized in the following ANOVA table.

TABLE 6.2
Sample ANOVA table (equal cluster size $M$ )

| Source | D.F. | Sum of Squares | Mean S.S. |
| :--- | :---: | :---: | :---: |
| Between | $n_{\mathrm{I}}-1$ | Sample $\mathrm{SS}_{\mathrm{B}}\left(=\mathrm{SSS}_{\mathrm{B}}\right)$ | $s_{\mathrm{b}}^{2}=\mathrm{SSS}_{\mathrm{B}} /\left(n_{\mathrm{I}}-1\right)$ |
| Within | $n_{\mathrm{I}}(M-1)$ | Sample $\mathrm{SS}_{\mathrm{W}}\left(=\mathrm{SSS}_{\mathrm{W}}\right)$ | $s_{\mathrm{w}}^{2}=\mathrm{SSS}_{\mathrm{W}} /\left\{n_{\mathrm{I}}(M-1)\right\}$ |
| Total | $n_{\mathrm{I}} M-1$ | Sample $\mathrm{SS}_{\mathrm{T}}\left(=\mathrm{SSS}_{\mathrm{T}}\right)$ | $s^{2}=\mathrm{SSS}_{\mathrm{T}} /\left(n_{\mathrm{I}} M-1\right)$ |




---

In this case, we have

$$
\begin{aligned}
\text { Sample } S S B & =\sum_{i=1}^{n_{I}} M\left\{\bar{Y}_{i}-\left(n^{-1} \sum_{k=1}^{n} \bar{Y}_{k}\right)\right\}^{2} \\
\text { Sample } S S W & =\sum_{i=1}^{n_{I}} \sum_{j=1}^{M}\left(y_{i j}-\bar{Y}_{i}\right)^{2}
\end{aligned}
$$

and Sample $S S T=$ Sample $S S B+$ Sample $S S W$. Since the sampling design is the simple random cluster sampling,

$$
\mathrm{E}\left(s_{b}^{2}\right)=\frac{1}{N_{I}-1} \sum_{i=1}^{N_{I}}\left(\bar{Y}_{i}-\bar{Y}\right)^{2}=S_{b}^{2}
$$

and

$$
\mathrm{E}\left(s_{w}^{2}\right)=\frac{1}{N_{I}(M-1)} \sum_{i=1}^{N_{I}}\left(y_{i j}-\bar{Y}_{i}\right)^{2}=S_{w}^{2}
$$

but we do not have $\mathrm{E}\left(s^{2}\right)=S^{2}$. In this case, we can use

$$
\hat{\rho}=1-\frac{s_{w}^{2}}{\hat{S}_{y}^{2}}
$$

where

$$
\hat{S}_{y}^{2}=\frac{(N-1) s_{b}^{2}+N(M-1) s_{w}^{2}}{N M} \doteq \frac{1}{M} s_{b}^{2}+\left(1-\frac{1}{M}\right) s_{w}^{2}
$$

In other words, we have

$$
\hat{\rho}=\frac{s_{b}^{2}-s_{w}^{2}}{s_{b}^{2}+(M-1) s_{w}^{2}}
$$

# 6.3 Single-stage cluster sampling: Unequal Size Case 

We now consider the case when the cluster sizes $M_{i}$ are unequal and we are interested in estimating the population total or population mean. If the cluster-level first-order inclusion probability is given by $\pi_{I i}=\operatorname{Pr}\left(i \in A_{I}\right)$, the HT estimator of the population total is

$$
\hat{Y}_{\mathrm{HT}}=\sum_{i \in A_{I}} \frac{Y_{i}}{\pi_{I i}}
$$




---

and its variance is, under fixed-size cluster sampling,

$$
\mathcal{V}\left(\hat{Y}_{\mathrm{HT}}\right)=-\frac{1}{2} \sum_{i=1}^{N} \sum_{j=1}^{N}\left(\pi_{I i j}-\pi_{I i} \pi_{I j}\right)\left(\frac{Y_{i}}{\pi_{I i}}-\frac{Y_{j}}{\pi_{I j}}\right)^{2}
$$

The variance is minimized when $\pi_{I i} \propto Y_{i}$. Since we do not know $Y_{i}$ in practice and $Y_{i}=M_{i} \bar{Y}_{i}$, we may use $\pi_{I i} \propto M_{i}$ if $\bar{Y}_{I i}$ is believed to be independent of $M_{i}$.

To formally discuss the problem of optimal choice of the first-order inclusion probability, assume the following superpopulation model

$$
y_{i j}=\mu+a_{i}+e_{i j}
$$

where $\mu$ is an unknown parameter, $a_{i} \sim\left(0, \sigma_{a}^{2}\right)$, and $e_{i j} \sim\left(0, \sigma_{e}^{2}\right)$. The total variance of $\hat{Y}_{\mathrm{HT}}$ under the model (6.9) is

$$
\begin{aligned}
\mathcal{V}\left(\hat{Y}_{\mathrm{HT}}\right) & =\mathcal{V}\left(\sum_{i \in \mathcal{A}_{I}} \pi_{I i}^{-1} M_{i} \mu\right)+\mathcal{E}\left(\sum_{i \in \mathcal{A}_{I}} \pi_{I i}^{-2} \gamma_{i}\right) \\
& =\mathcal{V}\left(\sum_{i \in \mathcal{A}_{I}} \pi_{I i}^{-1} M_{i} \mu\right)+\mathcal{E}\left(\sum_{i \in \mathcal{U}_{I}} \pi_{I i}^{-1} \gamma_{i}\right)
\end{aligned}
$$

where $\gamma_{i}=\mathcal{V}\left(Y_{i}\right)=M_{i}^{2} \sigma_{a}^{2}+M_{i} \sigma_{e}^{2}$. The second term of the total variance is minimized when

$$
\pi_{I i} \propto \gamma_{i}^{1 / 2}=M_{i} \sigma_{a}\left(1+\frac{\sigma_{e}^{2}}{\sigma_{a}^{2}} \cdot \frac{1}{M_{i}}\right)^{1 / 2}
$$

The solution (6.10) is obtained by applying the following Cauchy-Schwartz inequality

$$
\left(\sum_{i \in \mathcal{U}_{I}} \pi_{I i}^{-1} \gamma_{i}\right)\left(\sum_{i \in \mathcal{U}_{I}} \pi_{I i}\right) \geq\left(\sum_{i \in \mathcal{U}_{I}} \sqrt{\gamma_{i}}\right)^{2}
$$

and using that $\sum_{i \in \mathcal{U}_{I}} \pi_{I i}$ is fixed. Thus, if $\sigma_{e}^{2} / \sigma_{a}^{2}$ is small, then $\pi_{I i} \propto M_{i}$ lead to an optimal sampling design. On the other hand, if $\sigma_{e}^{2} / \sigma_{a}^{2}$ is large, then $\pi_{I i} \propto M_{i}^{1 / 2}$ can be a better design.

We now consider the situation when the simple random cluster sampling is used in spite of the fact that $M_{i}$ are unequal. The HT estimator of the total is

$$
\hat{Y}_{\mathrm{HT}}=\frac{N_{I}}{n_{I}} \sum_{i \in \mathcal{A}_{I}} Y_{i}
$$

where $Y_{i}=M_{i} \bar{Y}_{i}$. The variance is

$$
\mathcal{V}_{\mathrm{SRC}}\left(\hat{Y}_{\mathrm{HT}}\right)=\frac{N_{I}^{2}}{n_{I}}\left(1-\frac{n_{I}}{N_{I}}\right) S_{I}^{2}
$$




---

where

$$
S_{\mathrm{I}}^{2}=\frac{1}{N_{\mathrm{I}}-1} \sum_{i \in \mathcal{U}_{\mathrm{I}}}\left(Y_{i}-\bar{Y}_{\mathrm{I}}\right)^{2}=\frac{1}{N_{\mathrm{I}}-1} \sum_{i \in \mathcal{U}_{\mathrm{I}}}\left(M_{i} \bar{Y}_{i}-\bar{M} \bar{Y}_{\mathcal{U}}\right)^{2}
$$

$\bar{M}=N_{\mathrm{I}}^{-1} \sum_{i \in \mathcal{U}_{\mathrm{I}}} M_{i}, \bar{Y}_{\mathrm{I}}=N_{\mathrm{I}}^{-1} \sum_{i \in \mathcal{U}_{\mathrm{I}}} Y_{i}$, and $\bar{Y}_{\mathcal{U}}=\hat{Y}_{\mathrm{I}} / \bar{M}$.
Since $M_{i}$ can be different, we extend the definition of the intracluster correlation coefficient to define the cluster homogeneity coefficient as follows:

$$
\delta=1-\frac{\sum_{i \in \mathcal{U}_{\mathrm{I}}} \sum_{j \in \mathcal{U}_{i}}\left(y_{i j}-\bar{Y}_{i}\right)^{2} /\left(N-N_{\mathrm{I}}\right)}{\sum_{i \in \mathcal{U}_{\mathrm{I}}} \sum_{j \in \mathcal{U}_{i}}\left(y_{i j}-\bar{Y}_{\mathcal{U}}\right)^{2} /(N-1)}=1-\frac{S S W /\left(N-N_{\mathrm{I}}\right)}{S S T /(N-1)}
$$

If $M_{i}$ are all equal, then $\delta$ is equal to the intracluster correlation in (6.4). Using $\delta$ in (6.12), we can express the variance in (6.11) as

$$
\mathcal{V}_{\mathrm{SRC}}\left(\hat{Y}_{\mathrm{HT}}\right)=\left(1+\frac{N-N_{\mathrm{I}}}{N_{\mathrm{I}}-1} \delta\right) \bar{M} S_{\mathrm{y}}^{2} K_{\mathrm{I}}+C^{*} \cdot K_{\mathrm{I}}
$$

where $K_{\mathrm{I}}=\frac{N_{\mathrm{I}}^{2}}{n_{\mathrm{I}}}\left(1-\frac{n_{\mathrm{I}}}{N_{\mathrm{I}}}\right)$ and

$$
C^{*}=\frac{1}{N_{\mathrm{I}}-1} \sum_{i=1}^{N_{\mathrm{I}}}\left(M_{i}-\bar{M}\right) M_{i} \bar{Y}_{i}^{2}
$$

is the population covariance between $M_{i}$ and $M_{i} \bar{Y}_{i}^{2}$. If $\bar{Y}_{i}^{2}$ are all equal, then we have $C^{*}=\operatorname{Cov}\left(M_{i}, M_{j}\right)$. Roughly speaking, the second term in (6.13) is the additional variance due to the unequal cluster sizes.

Now, consider simple random sampling using the same sample size $n=$ $n_{I} \bar{M}$. In this case, the variance under SRS is

$$
\begin{aligned}
\mathcal{V}_{\mathrm{SRS}}\left(\hat{Y}_{\mathrm{HT}}\right) & =\frac{N^{2}}{n_{\mathrm{I}} \bar{M}}\left(1-\frac{n_{\mathrm{I}} \bar{M}}{N}\right) S_{\mathrm{y}}^{2} \\
& =\frac{N}{N_{\mathrm{I}}} \frac{S_{\mathrm{y}}^{2}}{N_{\mathrm{I}}^{2}} n_{\mathrm{I}}\left(1-\frac{n_{\mathrm{I}}}{N_{\mathrm{I}}}\right)=\bar{M} S_{\mathrm{y}}^{2} K_{\mathrm{I}}
\end{aligned}
$$

Thus, the design effect of the simple random cluster sampling design is

$$
\operatorname{deff}=\frac{\mathcal{V}_{\mathrm{SRC}}\left(\hat{Y}_{\mathrm{HT}}\right)}{\mathcal{V}_{\mathrm{SRS}}\left(\hat{Y}_{\mathrm{HT}}\right)}=\left(1+\frac{N-N_{\mathrm{I}}}{N_{\mathrm{I}}-1} \delta\right)+\frac{C^{*}}{\bar{M} S_{\mathrm{y}}^{2}}
$$

Therefore, there are two source of having deff $>1$ in this case.

1. $\delta>0$ : The homogeneity of the $y$ values within the cluster reduces efficiency.
2. $C^{*}>0$ : The variability of cluster size reduces efficiency.



---

If $M_{i}=M$, then the design effect is equal to $1+(M-1) \delta$, which is consistent with the result in (6.8).

We now consider mean estimation under cluster sampling. If the parameter of interest is population mean, we may have two different concepts:

$$
\begin{aligned}
\mu_{1} & =\frac{1}{N_{\mathrm{I}}} \sum_{i=1}^{N_{\mathrm{I}}} \frac{Y_{i}}{M_{i}}=\frac{1}{N_{\mathrm{I}}} \sum_{i=1}^{N_{\mathrm{I}}} \bar{Y}_{i} \\
\mu_{2} & =\frac{1}{N} \sum_{i=1}^{N_{\mathrm{I}}} Y_{i}=\frac{\sum_{i=1}^{N_{\mathrm{I}}} \sum_{j=1}^{M_{i}} y_{i j}}{\sum_{i=1}^{N_{\mathrm{I}}} M_{i}}
\end{aligned}
$$

If $M_{i}=M$, then $\mu_{1}=\mu_{2}$. Otherwise, the two parameters have different meanings. The first parameter $\mu_{1}$ is the cluster-level mean while the second parameter $\mu_{2}$ is the element-level mean.

Suppose that we are interested in estimating $\bar{Y}_{\mathrm{U}}=\mu_{2}$. From each sampled cluster $i$, we observe $\left(M_{i}, \bar{Y}_{i}\right)$. We can estimate the mean by a ratio of the estimated total of $y$ to the estimated total size:

$$
\hat{\bar{Y}}_{\mathrm{R}}=\frac{\sum_{i \in \mathcal{A}_{\mathrm{I}}} Y_{i} / \pi_{\mathrm{Ii}}}{\sum_{i \in \mathcal{A}_{\mathrm{I}}} M_{i} / \pi_{\mathrm{Ii}}}:=\frac{\hat{Y}_{\mathrm{HT}}}{\hat{N}_{\mathrm{HT}}}
$$

Since the ratio is a nonlinear function of two HT estimators, we use a Taylor linearization to get the following approximation

$$
\frac{\hat{Y}_{\mathrm{HT}}}{\hat{N}_{\mathrm{HT}}} \cong \frac{Y}{N}+\frac{1}{N}\left(\frac{\hat{Y}_{\mathrm{HT}}-Y}{N} \hat{N}_{\mathrm{HT}}\right)
$$

Thus, the approximate variance is

$$
\mathbb{V}\left(\hat{\bar{Y}}_{\mathrm{R}}\right) \doteq \frac{1}{N^{2}}\left\{\mathbb{V}\left(\hat{Y}_{\mathrm{HT}}\right)-2 \mu \operatorname{Cov}\left(\hat{Y}_{\mathrm{HT}}, \hat{N}_{\mathrm{HT}}\right)+\mu^{2} \mathbb{V}\left(\hat{N}_{\mathrm{HT}}\right)\right\}
$$

Under simple random cluster sampling, for example, the variance is

$$
\begin{aligned}
\mathbb{V}\left(\hat{\bar{Y}}_{\mathrm{R}}\right) & \doteq \frac{N_{\mathrm{I}}^{2}}{n_{\mathrm{I}} N^{2}}\left(1-\frac{n_{\mathrm{I}}}{N_{\mathrm{I}}}\right) \frac{1}{N_{\mathrm{I}}-1} \sum_{i=1}^{N_{\mathrm{I}}}\left(Y_{i}-M_{i} \bar{Y}_{\mathrm{U}}\right)^{2} \\
& =\frac{1}{n_{\mathrm{I}} \bar{M}^{2}}\left(1-\frac{n_{\mathrm{I}}}{N_{\mathrm{I}}}\right) \frac{1}{N_{\mathrm{I}}-1} \sum_{i=1}^{N_{\mathrm{I}}} M_{i}^{2}\left(\bar{Y}_{i}-\bar{Y}_{\mathrm{U}}\right)^{2}
\end{aligned}
$$

with $\bar{M}=N_{\mathrm{I}}^{-1} \sum_{i=1}^{N_{\mathrm{I}}} M_{i}=N / N_{\mathrm{I}}$. For variance estimation, we can use

$$
\hat{\mathbb{V}}\left(\hat{\bar{Y}}_{\mathrm{R}}\right)=\frac{1}{n_{\mathrm{I}} \bar{M}^{2}}\left(1-\frac{n_{\mathrm{I}}}{N_{\mathrm{I}}}\right) \frac{1}{n_{\mathrm{I}}-1} \sum_{i \in \mathcal{A}_{\mathrm{I}}} M_{i}^{2}\left(\bar{Y}_{i}-\bar{Y}_{\mathrm{U}}\right)^{2}
$$




---

# 7 

## Cluster Sampling: Two-stage cluster sampling

### 7.1 Introduction

In this chapter, we consider two-stage cluster sampling where the sample clusters are selected in the first stage, and the sample elements are selected in the second stage sampling. To formally state this, two-stage sampling can be described as follows:

1. Stage 1: Draw $\mathcal{A}_{I} \subset \mathcal{U}_{I}$ via $p_{I}(\cdot)$
2. Stage 2: For every $i \in \mathcal{A}_{I}$, draw $\mathcal{A}_{i} \subset \mathcal{U}_{i}$ via $p_{i}\left(\cdot \mid \mathcal{A}_{I}\right)$

Sample of elements is now given by $\mathcal{A}=\cup_{i \in \mathcal{A}_{I}} \mathcal{A}_{i}$.
In two-stage sampling, we have two simplifying assumptions about the second stage sampling design $p_{i}\left(\cdot \mid \mathcal{A}_{I}\right)$ :

1. Invariance of the second-stage design $p_{i}\left(\cdot \mid \mathcal{A}_{I}\right)=p_{i}(\cdot)$ for every $i \in \mathcal{U}_{I}$ and for every $\mathcal{A}_{I}$ such that $i \in \mathcal{A}_{I}$
2. Independence of the second-stage design

$$
\operatorname{Pr}\left(\cup_{i \in \mathcal{A}_{I}} \mathcal{A}_{i} \mid \mathcal{A}_{I}\right)=\prod_{i \in \mathcal{A}_{I}} \operatorname{Pr}\left(\mathcal{A}_{i} \mid \mathcal{A}_{I}\right)
$$

Under independence, we have

$$
\operatorname{Pr}\left(k \in \mathcal{A}_{i}, l \in \mathcal{A}_{j}\right)=\operatorname{Pr}\left(k \in \mathcal{A}_{i}\right) \operatorname{Pr}\left(l \in \mathcal{A}_{j}\right), i \neq j
$$

If the invariance assumption does not hold, the sampling design is called twophase sampling design. The two-phase sampling design will be covered in Chapter 11.

In two-stage sampling, we use $n_{I}$ to denote the cluster sample size in the first-stage sampling and use $m_{i}=\left|\mathcal{A}_{i}\right|$ to denote the sample size in cluster $i$. The number of sampled elements is equal to $\sum_{i \in \mathcal{A}_{I}} m_{i}=|\mathcal{A}|$. The first-order inclusion probability of element $k$ in cluster $i$ is a product of the clusterlevel inclusion probability and the conditional inclusion probability given the cluster:

$$
\pi_{i k}=\operatorname{Pr}\{(i k) \in \mathcal{A}\}=\operatorname{Pr}\left(k \in \mathcal{A}_{i} \mid i \in \mathcal{A}_{I}\right) \operatorname{Pr}\left(i \in \mathcal{A}_{I}\right)=\pi_{k \mid i} \pi_{I i}
$$




---

where $\pi_{I i}$ is the cluster-level inclusion probability and $\pi_{k \mid i}=\operatorname{Pr}\left[k \in A_{i} \mid i \in A_{I}\right]$ is the element-level conditional inclusion probability. In general, $\pi_{k \mid i}$ is a random variable (in the sense that it is a function of $A_{I}$ ). Under invariance, it is fixed.

The second-order inclusion probability between two elements can be expressed as

$$
\pi_{i k, j l}= \begin{cases}\pi_{I i} \pi_{k \mid i} & \text { if } i=j \text { and } k=l \\ \pi_{I i} \pi_{k l \mid i} & \text { if } i=j \text { and } k \neq l \\ \pi_{I i j} \pi_{k \mid i} \pi_{l \mid j} & \text { if } i \neq j\end{cases}
$$

where $\pi_{I i j}$ is the cluster level joint inclusion probability and $\pi_{k l \mid i}=$ $\operatorname{Pr}\left[k, l \in A_{i} \mid i \in A_{I}\right]$

# 7.2 Estimation 

In two-stage cluster sampling, we do not observe $Y_{i}$. Instead, we obtain $\hat{Y}_{i}$ from the second stage sampling such that $\mathrm{E}\left(\hat{Y}_{i} \mid A_{I}\right)=Y_{i}$, where the conditional expectation is taken with respect to the second-stage sampling. For simplicity, we use $\mathrm{E}_{2}\left(\hat{Y}_{i}\right)=\mathrm{E}\left(\hat{Y}_{i} \mid A_{I}\right)$.

The HT estimation for $Y=\sum_{i \in U_{I}} Y_{i}=\sum_{i \in U_{I}} \sum_{k \in U_{i}} y_{i k}$ is given by

$$
\hat{Y}_{\mathrm{HT}}=\sum_{i \in A_{I}} \frac{\hat{Y}_{i}}{\pi_{I i}}=\sum_{i \in A_{I}} \sum_{k \in A_{i}} \frac{y_{i k}}{\pi_{k \mid i} \pi_{I i}}
$$

The HT estimator in (7.1) is unbiased and its variance can be computed by

$$
\mathrm{V}\left(\hat{Y}_{\mathrm{HT}}\right)=\mathrm{V}\left\{\mathrm{E}\left(\hat{Y}_{\mathrm{HT}} \mid A_{I}\right)\right\}+\mathrm{E}\left\{\mathrm{V}\left(\hat{Y}_{\mathrm{HT}} \mid A_{I}\right)\right\}
$$

The first term is the variance due to the first-stage sampling (sampling of PSUs) and the second term is the variance due to the second-stage sampling (sampling of SSUs). Thus, we can write

$$
\mathrm{V}\left(\hat{Y}_{\mathrm{HT}}\right)=\mathrm{V}_{\mathrm{PSU}}+\mathrm{V}_{\mathrm{SSU}}
$$

where

$$
\begin{aligned}
\mathrm{V}_{\mathrm{PSU}} & =\mathrm{V}\left\{\sum_{i \in A_{I}} \frac{Y_{i}}{\pi_{I i}}\right\}=\sum_{i \in U_{I}} \sum_{j \in U_{I}}\left(\pi_{I i j}-\pi_{I i} \pi_{I j}\right) \frac{Y_{i}}{\pi_{I i}} \frac{Y_{j}}{\pi_{I j}} \\
\mathrm{~V}_{\mathrm{SSU}} & =\mathrm{E}\left\{\sum_{i \in A_{I}} \frac{1}{\pi_{I i}^{2}} V_{i}\right\}=\sum_{i \in U_{I}} \frac{V_{i}}{\pi_{I i}}
\end{aligned}
$$




---

and

$$
V_{i}=V\left(\hat{Y}_{i} \mid A_{i}\right)=\sum_{k \in U_{i}} \sum_{l \in U_{i}}\left(\pi_{k l \mid i}-\pi_{k \mid i} \pi_{l \mid i}\right) \frac{y_{i k}}{\pi_{k \mid i}} \frac{y_{i l}}{\pi_{l \mid i}}
$$

Example 7.1. Consider the following two-stage sampling design.

1. Stage One: Select $n_{I}$ sample clusters from $N_{I}$ population clusters by simple random cluster sampling.
2. Stage Two: Within sampled cluster $i$, select $m_{i}$ sample elements from $M_{i}$ population elements independently.

Under this two-stage sampling, we have

$$
\hat{Y}_{\mathrm{HT}}=\frac{N_{I}}{n_{I}} \sum_{i \in A_{I}} \hat{Y}_{i}=\sum_{i \in A_{I}} \sum_{j \in A_{i}} \frac{N_{I}}{n_{I}} \frac{M_{i}}{m_{i}} y_{i j}
$$

and its variance is

$$
V\left(\hat{Y}_{\mathrm{HT}}\right)=\frac{N_{I}^{2}}{n_{I}}\left(1-\frac{n_{I}}{N_{I}}\right) S_{I}^{2}+\left(\frac{N_{I}}{n_{I}}\right) N_{I} \sum_{i=1}^{N_{I}} \frac{M_{i}^{2}}{m_{i}}\left(1-\frac{m_{i}}{M_{i}}\right) S_{i}^{2}
$$

where

$$
\begin{aligned}
S_{I}^{2} & =\left(N_{I}-1\right)^{-1} \sum_{i=1}^{N_{I}}\left(Y_{i}-\bar{Y}_{N}\right)^{2} \\
S_{i}^{2} & =\left(M_{i}-1\right)^{-1} \sum_{j=1}^{M_{i}}\left(y_{i j}-\bar{Y}_{i}\right)^{2}
\end{aligned}
$$

Now, consider the estimation of the population mean $\bar{Y}=N^{-1} \sum_{i=1}^{N_{I}} \sum_{j=1}^{M_{i}} y_{i j}$, where $N=\sum_{i=1}^{N_{I}} M_{i}$ is assumed to be known. In this case,

$$
\hat{\bar{Y}}_{\mathrm{HT}}=\frac{\hat{Y}_{\mathrm{HT}}}{N}=\frac{N_{I}}{n_{I} N} \sum_{i \in A_{I}} \hat{Y}_{i}=\frac{1}{n_{I}} \sum_{i \in A_{I}} \frac{\hat{Y}_{i}}{\bar{M}}
$$

where $\bar{M}=N_{I}^{-1} \sum_{i=1}^{N_{I}} M_{i}$. Its variance is, using (7.4),

$$
V\left(\hat{\bar{Y}}_{\mathrm{HT}}\right)=\frac{1}{n_{I}}\left(1-\frac{n_{I}}{N_{I}}\right) S_{q_{1}}^{2}+\frac{1}{n_{I} N_{I} \bar{M}^{2}} \sum_{i=1}^{N_{I}} \frac{M_{i}^{2}}{m_{i}}\left(1-\frac{m_{i}}{M_{i}}\right) S_{2 i}^{2}
$$

where $S_{q_{1}}^{2}=\left(N_{I}-1\right)^{-1} \sum_{i=1}^{N_{I}}\left(q_{i}-\bar{q}_{1}\right)^{2}$ with $q_{i}=Y_{i} / \bar{M}, \bar{q}_{1}=N_{I}^{-1} \sum_{i=1}^{N_{I}} q_{i}$, and $S_{2 i}^{2}=\left(M_{i}-1\right)^{-1} \sum_{k \in U_{i}}\left(y_{i k}-\bar{Y}_{i}\right)^{2}$.




---

If the sampling rate for the second stage sampling is constant such that $m_{i} / M_{i}=f_{2}$, then we can write

$$
\begin{aligned}
\mathbb{V}\left(\hat{\bar{Y}}_{\mathrm{HT}}\right) & =\frac{1}{n_{I}}\left(1-f_{1}\right) S_{q_{1}}^{2}+\frac{1}{n_{I} \bar{m}\left(1-f_{2}\right)} \frac{1}{N} \sum_{i=1}^{N_{I}} M_{i} S_{2 i}^{2} \\
& =\frac{1}{n_{I}}\left(1-f_{1}\right) B^{2}+\frac{1}{n_{I} \bar{m}\left(1-f_{2}\right)} W^{2}
\end{aligned}
$$

where $f_{1}=n_{I} / N_{I}$ and $\bar{m}=N_{I}^{-1} \sum_{i=1}^{N_{I}} m_{i}$.
Example 7.2. We now consider a special case of Example 7.1 where $M_{i}=M$ and $m_{i}=m$. In this case, (7.4) is further simplified

$$
\begin{aligned}
\mathbb{V}\left(\hat{Y}_{\mathrm{HT}}\right) & =\frac{N_{I}^{2}}{n_{I}}\left(1-\frac{n_{I}}{N_{I}}\right) \frac{M \times \mathrm{SSB}}{N_{I}-1}+\left(\frac{N_{I}}{n_{I}}\right)\left(1-\frac{m}{M}\right) \frac{M^{2}}{m(M-1)} \mathrm{SSW} \\
& =\frac{N_{I}^{2}}{n}\left(1-\frac{n_{I}}{N_{I}}\right) M S_{b}^{2}+\left(\frac{N_{I}^{2}}{n_{I}}\right)\left(1-\frac{m}{M}\right) \frac{M^{2}}{m} S_{w}^{2}
\end{aligned}
$$

For the case of mean estimation, we can simply divide (7.5) by $N^{2}=N_{I}^{2} M^{2}$ to get

$$
\mathbb{V}\left(\hat{\bar{Y}}_{\mathrm{HT}}\right)=\left(1-\frac{n_{I}}{N_{I}}\right) \frac{S_{b}^{2}}{n_{I} M}+\left(1-\frac{m}{M}\right) \frac{S_{w}^{2}}{n_{I} m}
$$

Note that the sample size associated with the first term ( $\mathrm{V}_{\mathrm{PSU}}$ term) is $n_{I} M$ while the sample size associated with the second term ( $\mathrm{V}_{\mathrm{SSU}}$ term) is $n_{I} m$.

Now, we can express the variance term in (7.6) in terms of the intracluster correlation coefficient. Using (6.5) and (6.6), the variance term in (7.6) reduces to, ignoring $n_{I} / N_{I}$ term,

$$
\begin{aligned}
\mathbb{V}\left(\hat{\bar{Y}}_{\mathrm{HT}}\right) & \doteq \frac{1}{n_{I} M}[1+(M-1) \rho] S^{2}+\left(1-\frac{m}{M}\right) \frac{1}{n_{I} m}(1-\rho) S^{2} \\
& =\frac{S^{2}}{n_{I} m}\{1+(m-1) \rho\}
\end{aligned}
$$

Thus, the design effect becomes $1+(m-1) \rho$.
In this case of $M_{i}=M$ and $m_{i}=m$, the problem of finding the optimal choice of $m$ given the cost function $C=c_{0}+c_{1} n_{I}+c_{2} n_{I} m$ can be formulated as minimizing

$$
\begin{aligned}
\mathbb{V}\left(\hat{\bar{Y}}_{\mathrm{HT}}\right) & =\frac{S_{b}^{2}}{n_{I} M}+\left(1-\frac{m}{M}\right) \frac{S_{w}^{2}}{n_{I} m} \\
& =\frac{1}{n_{I}}\left\{\frac{1}{M}\left(S_{b}^{2}-S_{w}^{2}\right)+\frac{1}{m} S_{w}^{2}\right\}
\end{aligned}
$$

subject to

$$
C=c_{0}+c_{1} n_{I}+c_{2} n_{I} m
$$




---

When the total cost $C$ is fixed, we have

$$
n=\frac{C-c_{0}}{c_{1}+c_{2} m}
$$

and the optimal choice is given by

$$
m^{*}=\sqrt{\frac{c_{1}}{c_{2}} \frac{M \times S_{w}^{2}}{S_{b}^{2}-S_{w}^{2}}}
$$

The optimal solution (7.8) is obtained by applying

$$
a m+b m \geq 2 \sqrt{a b}
$$

with equality if and only if $m=\sqrt{a / b}$. That is, since

$$
\begin{aligned}
V\left(\hat{\bar{Y}}_{H T}\right) \cdot\left(C-c_{0}\right) & =\left\{\frac{1}{M}\left(S_{b}^{2}-S_{w}^{2}\right)+\frac{1}{m} S_{w}^{2}\right\}\left(c_{1}+c_{2} m\right) \\
& =\text { const. }+\frac{c_{1}}{m} S_{w}^{2}+\frac{c_{2}}{M}\left(S_{b}^{2}-S_{w}^{2}\right) m
\end{aligned}
$$

the lower bound is achieved when

$$
m=\left\{c_{1} S_{w}^{2}\right\}^{1 / 2}\left\{\frac{c_{2}}{M}\left(S_{b}^{2}-S_{w}^{2}\right)\right\}^{-1 / 2}
$$

which equals to (7.8). For sufficiently large $M$, the optimal solution becomes

$$
m^{*} \cong \sqrt{\frac{c_{1}}{c_{2}}}\left(\frac{1}{\rho}-1\right)
$$

More generally, the objective function can be written as

$$
V\left(\hat{\bar{Y}}_{H T}\right)=\frac{1}{n_{I}} B^{2}+\frac{1}{n_{I} \bar{m}}\left(1-f_{2}\right) W^{2}
$$

In this case, the optimal solution becomes

$$
m^{*}=\sqrt{\frac{c_{1}}{c_{2}} \frac{W^{2}}{B^{2}-W^{2} / M}}
$$

We now discuss variance estimation under two-stage cluster sampling.
Theorem 7.1. An unbiased estimator for the variance of HT estimator in (7.1) under two-stage sampling design is

$$
\hat{V}\left(\hat{Y}_{H T}\right)=\sum_{i \in \mathcal{A}_{I}} \sum_{j \in \mathcal{A}_{I}} \frac{\pi_{I i j}-\pi_{I i} \pi_{I j}}{\pi_{I i j}} \frac{\hat{Y}_{i}}{\pi_{I i}} \frac{\hat{Y}_{j}}{\pi_{I j}}+\sum_{i \in \mathcal{A}_{I}} \frac{1}{\pi_{I i}} \hat{V}_{i}
$$

where $\hat{V}_{i}$ satisfies $E\left(\hat{V}_{i} \mid i \in \mathcal{A}_{I}\right)=\operatorname{Var}\left(\hat{Y}_{i} \mid i \in \mathcal{A}_{I}\right)$.




---

Proof. By (7.3),

$$
\mathbb{V}\left(\hat{Y}_{\mathrm{HT}}\right)=\sum_{i=1}^{N_{I}} \sum_{j=1}^{N_{I}}\left(\pi_{I i j}-\pi_{I i} \pi_{I j}\right) \frac{Y_{i}}{\pi_{I i}} \frac{Y_{j}}{\pi_{I j}}+\sum_{i=1}^{N_{I}} \frac{V_{i}}{\pi_{I i}}
$$

By the independence assumption,

$$
\mathbb{E}_{2}\left(\hat{Y}_{i} \hat{Y}_{j}\right)= \begin{cases}Y_{i}^{2}+V_{i} & \text { if } i=j \\ Y_{i} Y_{j} & \text { if } i \neq j\end{cases}
$$

where $\mathbb{E}_{2}(\cdot)$ denotes the expectation with respect to the second-stage sampling. Thus,

$$
\begin{aligned}
& \sum_{i \in \mathcal{A}_{I}} \sum_{j \in \mathcal{A}_{I}} \frac{\pi_{I i j}-\pi_{I i} \pi_{I j}}{\pi_{I i j}} \frac{\mathbb{E}_{2}\left(\hat{Y}_{i} \hat{Y}_{j}\right)}{\pi_{I i} \pi_{I j}}=\sum_{i \in \mathcal{A}_{I}} \sum_{j \in \mathcal{A}_{I}} \frac{\pi_{I i j}-\pi_{I i} \pi_{I j}}{\pi_{I i j}} \frac{Y_{i} Y_{j}}{\pi_{I i} \pi_{I j}} \\
&+\sum_{i \in \mathcal{A}_{I}} \frac{\pi_{I i}-\pi_{I i}^{2}}{\pi_{I i}} \frac{V_{i}}{\pi_{I i}^{2}}
\end{aligned}
$$

and, since $\mathbb{E}_{2}\left(\hat{V}_{i}\right)=V_{i}$, we have

$$
\mathbb{E}_{2}\left\{\hat{\mathbb{V}}\left(\hat{Y}_{\mathrm{HT}}\right)\right\}=\sum_{i \in \mathcal{A}_{I}} \sum_{j \in \mathcal{A}_{I}} \frac{\pi_{I i j}-\pi_{I i} \pi_{I j}}{\pi_{I i j}} \frac{Y_{i} Y_{j}}{\pi_{I i} \pi_{I j}}+\sum_{i \in \mathcal{A}_{I}} \frac{V_{i}}{\pi_{I i}^{2}}
$$

Taking the expectation of the above term with respect to the first-stage sampling design, it equal to the variance term in (7.11).

The variance estimation formula in (7.10) is the sum of two terms. The first term is the variance estimation formula for the first-stage sampling applied to $\hat{Y}_{i}$ and the second term is the point estimator for the first-stage sampling applied to $\hat{V}_{i}$. The validity of the variance estimation formula (7.10) also holds even when $\hat{Y}_{i}$ and $\hat{V}_{i}$ are obtained from multi-stage sampling. That is, as long as $\mathbb{E}\left(\hat{Y}_{i} \mid \mathcal{A}_{I}\right)=Y_{i}$ and $\mathbb{E}\left(\hat{V}_{i} \mid \mathcal{A}_{I}\right)=\mathbb{V}\left(\hat{Y}_{i} \mid \mathcal{A}_{I}\right)$ hold, the variance estimation formula in (7.10) remains unbiased. Such a phenomenon was first discovered by Raj (1966).

If we use only the first term of $(7.10)$

$$
\hat{\mathbb{V}}_{1}=\sum_{i \in \mathcal{A}_{I}} \sum_{j \in \mathcal{A}_{I}} \frac{\pi_{I i j}-\pi_{I i} \pi_{I j}}{\pi_{I i j}} \frac{\hat{Y}_{i}}{\pi_{I i}} \frac{\hat{Y}_{j}}{\pi_{I j}}
$$

to estimate the total variance, the bias can be written

$$
\operatorname{Bias}\left(\hat{V}_{1}\right)=-\sum_{i=1}^{N_{I}} V_{i}
$$




---

and the bias term is of order $O\left(N_{\mathrm{I}}\right)$. Since $\mathbb{V}\left(\hat{Y}_{\mathrm{HT}}\right)$ is of the order $O\left(n_{\mathrm{I}}^{-1} N_{\mathrm{I}}^{2}\right)$, the bias term is negligible when $n_{\mathrm{I}} / N_{\mathrm{I}}=o(1)$.

Under the setup of Example 7.1 where $M_{i}=M, m_{i}=m$, the variance estimation formula in (7.10) reduces to

$$
\hat{\mathbb{V}}\left(\hat{Y}_{\mathrm{HT}}\right)=\frac{N_{\mathrm{I}}^{2}}{n_{\mathrm{I}}}\left(1-\frac{n_{\mathrm{I}}}{N_{\mathrm{I}}}\right) \frac{1}{n_{\mathrm{I}}-1} \sum_{i \in \mathcal{A}_{\mathrm{I}}}\left(\hat{Y}_{i}-\frac{1}{n_{\mathrm{I}}} \sum_{j \in \mathcal{A}_{\mathrm{I}}} \hat{Y}_{i}\right)^{2}+\frac{N_{\mathrm{I}}}{n_{\mathrm{I}}} \sum_{i \in \mathcal{A}_{\mathrm{I}}} \hat{V}_{i}
$$

where $\hat{Y}_{i}=M \bar{y}_{i}$ and

$$
\hat{V}_{i}=\frac{M^{2}}{m}\left(1-\frac{m}{M}\right) \frac{1}{m-1} \sum_{j \in \mathcal{A}_{i}}\left(y_{i j}-\bar{y}_{i}\right)^{2}
$$

In the case of mean estimation, we can divide (7.10) by $N^{2}=N_{\mathrm{I}}^{2} M^{2}$ to get

$$
\hat{\mathbb{V}}\left(\hat{\bar{Y}}_{\mathrm{HT}}\right)=\left(1-\frac{n_{\mathrm{I}}}{N_{\mathrm{I}}}\right) \frac{s_{\mathrm{b}}^{2}}{n_{\mathrm{I}}}+\frac{n_{\mathrm{I}}}{N_{\mathrm{I}}}\left(1-\frac{m}{M}\right) \frac{s_{\mathrm{w}}^{2}}{n_{\mathrm{I}} m}
$$

where

$$
\begin{aligned}
s_{\mathrm{b}}^{2} & =\left(n_{\mathrm{I}}-1\right)^{-1} \sum_{i \in \mathcal{A}_{\mathrm{I}}}\left(\bar{y}_{i}-\hat{\bar{Y}}\right)^{2} \\
s_{\mathrm{w}}^{2} & =n_{\mathrm{I}}^{-1}(m-1)^{-1} \sum_{i \in \mathcal{A}_{\mathrm{I}}} \sum_{j \in \mathcal{A}_{i}}\left(y_{i j}-\bar{y}_{i}\right)^{2}
\end{aligned}
$$

If $f_{1}=n_{\mathrm{I}} / N_{\mathrm{I}}$ is negligible, then we can use

$$
\hat{\mathbb{V}}\left(\hat{\bar{Y}}_{\mathrm{HT}}\right)=\frac{s_{\mathrm{b}}^{2}}{n_{\mathrm{I}}}
$$

as a variance estimator for the mean estimator under simple random sampling.
When the cluster sizes are unequal, simple random sampling in the first stage sampling is not preferable. The following example is a very popular method of two-stage sampling in the case of unequal cluster sizes.

Example 7.3. Consider the following two-stage sampling design.

1. Stage One: Select clusters (of size $n_{\mathrm{I}}$ ) by PPS sampling with size measure $M_{i}$.
2. Stage Two: Select elements by SRS of size $m$ from $M_{i}$ elements in the sample cluster $i$.

We first consider estimation of population total $Y=\sum_{i=1}^{N_{I}} \sum_{j=1}^{M_{i}} y_{i j}$. Under single-stage cluster sampling, we would have observed $Y_{i}=\sum_{j=1}^{M_{i}} y_{i j}$. In this case, an unbiased estimator of $Y$ is given by

$$
\hat{Y}_{\mathrm{PPS}}=\frac{N}{n_{\mathrm{I}}} \sum_{k=1}^{n_{I}} \frac{Y_{a_{k}}}{M_{a_{k}}}
$$




---

where $a_{k}$ is the index of population cluster in the $k$-th draw of the PPS sampling. In the two-stage sampling, we do not observe $Y_{i}$ but we obtain $\hat{Y}_{i}=M_{i} \bar{y}_{i}$, where $\bar{y}_{i}$ is the sample mean of elements in the cluster $i$. Thus, we can use

$$
\hat{Y}_{\mathrm{PPS}}=\frac{N}{n_{\mathrm{I}}} \sum_{k=1}^{n_{\mathrm{I}}} \frac{\hat{Y}_{a_{k}}}{M_{a_{k}}}=\frac{N}{n_{\mathrm{I}}} \sum_{k=1}^{n_{\mathrm{I}}} \bar{y}_{a_{k}}
$$

to estimate the total $Y$. Assuming that there is no duplication of the selected clusters, the sampling weights are all equal to $N /\left(n_{\mathrm{I}} m\right)$, which implies that every element in the population has the same probability of selection. The sampling design that leads to equal sampling weights is called a self-weighting design.

For estimation of the population mean $\bar{Y}=Y / N$, we have

$$
\hat{\bar{Y}}_{\mathrm{PPS}}=\frac{1}{n_{\mathrm{I}}} \sum_{k=1}^{n_{\mathrm{I}}} \bar{y}_{a_{k}}
$$

which takes the sample mean of the cluster means.
To discuss variance estimation, note that the point estimator (7.16) can be written as the sample mean of $z_{1}, \cdots, z_{n_{\mathrm{I}}}$ where $z_{k}$ are independently and identically distributed with the following discrete distribution:

$$
z_{1}=\hat{Y}_{i} / p_{i} \quad \text { with probability } p_{i}=M_{i} / N, i=1, \cdots, N_{\mathrm{I}}
$$

Note that $\mathrm{E}\left(z_{1}\right)=\sum_{i=1}^{N} \hat{Y}_{i}$, which is unbiased for $Y=\sum_{i=1}^{N_{\mathrm{I}}} Y_{i}$ as $\mathrm{E}_{2}\left(\hat{Y}_{i}\right)=Y_{i}$. For variance estimation, since $\hat{Y}_{\text {PPS }}$ in (7.16) can be written as the mean of $n_{\mathrm{I}}$ independent sample of $z_{k} \mathrm{~s}$, we have

$$
\hat{V}_{\mathrm{PPS}}\left(\hat{Y}_{\mathrm{PPS}}\right)=\frac{1}{n_{\mathrm{I}}} S_{z}^{2}=\frac{1}{n_{\mathrm{I}}} \frac{1}{n_{\mathrm{I}}-1} \sum_{k=1}^{n_{\mathrm{I}}}\left(z_{k}-\bar{z}\right)^{2}
$$

Variance estimation of the mean estimator (7.17) can be similarly constructed. Specifically, we can use

$$
\hat{V}_{\mathrm{PPS}}\left(\hat{\bar{Y}}_{\mathrm{PPS}}\right)=\frac{1}{n_{\mathrm{I}}} \frac{1}{n_{\mathrm{I}}-1} \sum_{k=1}^{n_{\mathrm{I}}}\left(\bar{y}_{a_{k}}-\hat{\bar{Y}}_{\mathrm{PPS}}\right)^{2}
$$

as an unbiased estimator for the variance of the mean estimator (7.17).
To illustrate the use of two-stage sampling in Example 7.3, consider a finite population of households in a city. The city consists of $N_{\mathrm{I}}$ clusters of houses, and the cluster $i$ consists of $M_{i}$ houses. We used the following two-stage cluster sampling.
[Stage 1] Select $n_{\mathrm{I}}=3$ sample clusters by the PPS sampling with the measure of size equal to $M_{i}$.




---

[Stage 2] Within each selected cluster $i$, select $m_{i}=4$ sample houses by simple random sampling.

Once the sample households are selected, we obtain two information. One is the number of household members in the house $\left(t_{i j}\right)$ and the other is the number of household members under 6 years of age $\left(y_{i j}\right)$. We are interested in estimating the proportion of the population with age under 6 in the city. That is, the parameter of interest is

$$
P=\frac{\sum_{i=1}^{N_{I}} \sum_{j=1}^{M_{i}} y_{i j}}{\sum_{i=1}^{N_{i}} \sum_{i=1}^{M_{i}} t_{i j}}:=\frac{Y}{T}
$$

The following table gives the summary of the realized sample household from the above two-stage sampling.

TABLE 7.1 An illustrative example of two-stage cluster sample

| Sample Cluster ID | Sample household ID | $t_{i j}$ | $y_{i j}$ |
| :---: | :---: | :---: | :---: |
| 1 | 1 | 8 | 2 |
| 1 | 2 | 7 | 2 |
| 1 | 3 | 7 | 1 |
| 1 | 4 | 6 | 1 |
| 2 | 1 | 8 | 0 |
| 2 | 2 | 12 | 1 |
| 2 | 3 | 10 | 3 |
| 2 | 4 | 11 | 1 |
| 3 | 1 | 4 | 2 |
| 3 | 2 | 5 | 3 |
| 3 | 3 | 5 | 2 |
| 3 | 4 | 6 | 1 |

The proportion of the population with age under 6 in the city is estimated by

$$
\hat{P}=\frac{\hat{Y}}{\hat{T}}=\frac{N n_{I}^{-1} \sum_{k=1}^{n_{I}} \bar{y}_{k}}{N n_{I}^{-1} \sum_{k=1}^{n_{I}} \bar{t}_{k}}=\frac{6 / 4+5 / 4+8 / 4}{28 / 4+41 / 4+20 / 4} \doteq 0.213
$$

where the second equality follows from (7.16). To estimate the variance of $\hat{P}$, we use

$$
\hat{V}(\hat{P})=\frac{1}{n_{I}} \frac{1}{n_{I}-1}\left(\frac{1}{n_{I}} \sum_{i=1}^{n_{I}} \bar{t}_{i}\right)^{-2} \sum_{i=1}^{n_{I}}\left(\bar{y}_{i}-\hat{\theta} \bar{t}_{i}\right)^{2}=0.005302
$$

The design effect can be computed by the ratio of $\hat{V}(\hat{P})$ under the current




---

# 8 

## Estimation: Part 1

### 8.1 Introduction

So far, we have considered HT estimators for various sampling designs. HT estimator is design-unbiased but does not necessarily achieve small variance. To improve the efficiency of the resulting estimator, auxiliary information is often incorporated into the estimation if the population total of the auxiliary variable is known from external sources. An estimator is called a linear estimator if it is a linear function of the sample observations of $y$. That is,

$$
\hat{Y}=\sum_{i \in \mathcal{A}} w_{i} y_{i}
$$

for some $w_{i} \geq 0$ that does not depend on $y$. If $z_{i}=x_{i}+y_{i}$, then the linear estimator applied to $z$ satisfies $\hat{Z}=\hat{X}+\hat{Y}$. This property is called internal consistency. HT estimator is the only linear estimator that is design unbiased. If auxiliary variable $x_{i}$ is observed in the sample and the population total of $x_{i}$ is known from an external source such as census or administrative data, we may want to achieve

$$
\sum_{i \in \mathcal{A}} w_{i} x_{i}=\sum_{i=1}^{N} x_{i}
$$

Property (8.2) is sometimes called external consistency. We will consider two examples of estimators satisfying (8.2). One is the ratio estimator, and the other is the regression estimator.

### 8.2 Ratio Estimation

Suppose that a scalar auxiliary variable $x_{i}$ is available whose population total $X=\sum_{i=1}^{N} x_{i}$ is known from an external source. In this case, the HT estimator of $X, \hat{X}_{\mathrm{HT}}=\sum_{i \in \mathcal{A}} \pi_{i}^{-1} x_{i}$ is not necessarily equal to $X$. We can use




---

X information to modify the HT estimator to get

$$
\hat{Y}_{R}=\frac{X \hat{Y}_{\mathrm{HT}}}{\hat{X}_{\mathrm{HT}}}
$$

Thus, ratio estimator is computed by multiplying $\hat{X}_{\mathrm{HT}}^{-1} X$ to HT estimator of $Y$ and $\hat{X}_{\mathrm{HT}}^{-1} X$ is sometimes called ratio adjustment factor. The ratio adjustment factor is close to one, but not necessarily equal to one. If the realized sample satisfies $\hat{X}_{\mathrm{HT}}<X$, then the ratio adjustment factor is greater than one and $\hat{Y}_{R}>\hat{Y}_{\mathrm{HT}}$. In this case, the HT estimator is inflated by the ratio adjustment factor.

Ratio estimator is a linear estimator of the form in (8.1) and the weight is

$$
w_{i}=\frac{1}{\pi_{i}} \times \frac{X}{\hat{X}_{\mathrm{HT}}}
$$

Thus, the final weight is computed by a product of the design weight $\pi_{i}^{-1}$ and the ratio adjustment factor.

We now consider the statistical properties of the ratio estimator. Note that the ratio estimator is a nonlinear function of $\hat{X}_{\mathrm{HT}}$ and $\hat{Y}_{\mathrm{HT}}$. Thus,

$$
E\left(\frac{\hat{Y}_{\mathrm{HT}}}{\hat{X}_{\mathrm{HT}}}\right) \neq \frac{E\left(\hat{Y}_{\mathrm{HT}}\right)}{E\left(\hat{X}_{\mathrm{HT}}\right)}
$$

and the ratio estimator is not design unbiased for $Y$. To discuss the bias of the ratio estimator, define

$$
\hat{R}=\frac{\hat{Y}_{\mathrm{HT}}}{\hat{X}_{\mathrm{HT}}} \quad \text { and } \quad R=\frac{E\left(\hat{Y}_{\mathrm{HT}}\right)}{E\left(\hat{X}_{\mathrm{HT}}\right)}
$$

The bias of $\hat{R}$ as an estimator of $R$ is equal to $E(\hat{R})-R$ and it is often called ratio bias. To discuss ratio bias, note that

$$
\begin{aligned}
\operatorname{Cov}\left(\hat{R}, \hat{X}_{\mathrm{HT}}\right) & =E\left(\hat{R} \hat{X}_{\mathrm{HT}}\right)-E(\hat{R}) E\left(\hat{X}_{\mathrm{HT}}\right) \\
& =E\left(\hat{Y}_{\mathrm{HT}}\right)-E(\hat{R}) E\left(\hat{X}_{\mathrm{HT}}\right)
\end{aligned}
$$

Dividing both sides of the above equation by $-E\left(\hat{X}_{\mathrm{HT}}\right)$, we get

$$
\operatorname{Bias}(\hat{R})=-\frac{\operatorname{Cov}\left(\hat{R}, \hat{X}_{\mathrm{HT}}\right)}{E\left(\hat{X}_{\mathrm{HT}}\right)}
$$




---

and so

$$
\operatorname{Bias}\left(\hat{Y}_{R}\right)=-\operatorname{Cov}\left(\hat{R}, \hat{X}_{H T}\right)
$$

Even if the ratio estimator is biased, but if the bias is smaller order than its standard error, the bias can be negligible. Generally speaking, we can express

$$
\frac{\hat{\theta}-\theta}{\sqrt{\mathcal{V}(\hat{\theta})}}=\frac{\hat{\theta}-\mathcal{E}(\hat{\theta})}{\sqrt{\mathcal{V}(\hat{\theta})}}+\text { R.B. }(\hat{\theta})
$$

where

$$
\text { R.B. }(\hat{\theta})=\frac{\operatorname{Bias}(\hat{\theta})}{\sqrt{\mathcal{V}(\hat{\theta})}}
$$

is the relative bias of $\hat{\theta}$. The first term on the right hand side of (8.6) converges to the standard normal distribution by the central limit theorem. Thus, when the second term converges to zero, the bias term can be safely ignored. We formalize the concept in the following definition.

Definition 8.1. $\operatorname{Bias}(\hat{\theta})$ is negligible

$$
\Longleftrightarrow \text { R.B. }(\hat{\theta})=\frac{\operatorname{Bias}(\hat{\theta})}{\sqrt{\mathcal{V}(\hat{\theta})}} \rightarrow 0 \quad \text { as } \quad n \rightarrow \infty
$$

In addition, since

$$
\frac{\operatorname{MSE}(\hat{\theta})}{\mathcal{V}(\hat{\theta})}=1+[\text { R.B. }(\hat{\theta})]^{2}
$$

the MSE of $\hat{\theta}$ is approximately equal to $\mathcal{V}(\hat{\theta})$ if the bias of $\hat{\theta}$ is negligible.
Now, to discuss the relative bias of the ratio estimator, first note that the relative bias of the ratio estimator is equal to the relative bias of $\hat{R}$. Thus, by (8.5), we have

$$
\left|\mathrm{R} . \mathrm{B} .\left(\hat{Y}_{R}\right)\right|=|\mathrm{R} . \mathrm{B} .(\hat{R})|=\left|\frac{\operatorname{Corr}\left(\hat{R}, \hat{X}_{H T}\right) \sqrt{\mathcal{V}\left(\hat{X}_{H T}\right)}}{\mathcal{E}\left(\hat{X}_{H T}\right)}\right| \leq \operatorname{CV}\left(\hat{X}_{H T}\right)
$$

where $\operatorname{CV}(\hat{\theta})=\sqrt{\mathcal{V}(\hat{\theta})} / \mathcal{E}(\hat{\theta})$ is the coefficient of variation. For example, under simple random sampling,

$$
\operatorname{CV}\left(\hat{X}_{H T}\right)=\sqrt{\frac{1}{n}\left(1-\frac{n}{N}\right)} \frac{S_{x}}{\bar{X}}
$$

Thus, the bias of the ratio estimator of negligible if one of the following conditions holds:




---

1. $n$ is large
2. $n / N$ is large (close to one)
3. $\operatorname{CV}(x)=S_{x} / \bar{X}$ is small.

For general sampling designs other than SRS, $\operatorname{CV}\left(\hat{X}_{\mathrm{HT}}\right)$ will converge to zero as $n$ increases and the bias of the ratio estimator is negligible.

To further discuss relative bias of the ratio estimator, we use the second order Taylor expansion to get

$$
\begin{aligned}
\widehat{\bar{Y}}_{R} \cong & \bar{Y}+\left(\widehat{\bar{Y}}_{\mathrm{HT}}-\bar{Y}\right)-R\left(\widehat{\bar{X}}_{\mathrm{HT}}-\bar{X}\right) \\
& -\bar{X}^{-1}\left[\left(\widehat{\bar{X}}_{\mathrm{HT}}-\bar{X}\right)\left(\widehat{\bar{Y}}_{\mathrm{HT}}-\bar{Y}\right)-R\left(\widehat{\bar{X}}_{\mathrm{HT}}-\bar{X}\right)^{2}\right]
\end{aligned}
$$

where $\widehat{\bar{Y}}_{R}=N^{-1} \hat{Y}_{R}, \widehat{\bar{X}}_{\mathrm{HT}}=N^{-1} \hat{X}_{\mathrm{HT}}$, and $\widehat{\bar{Y}}_{\mathrm{HT}}=N^{-1} \hat{Y}_{\mathrm{HT}}$. Thus,

$$
\operatorname{Bias}\left(\widehat{\bar{Y}}_{R}\right) \doteq-\bar{X}^{-1}\left[\operatorname{Cov}\left(\widehat{\bar{X}}_{\mathrm{HT}}, \widehat{\bar{Y}}_{\mathrm{HT}}\right)-R \cdot \mathbf{V}\left(\widehat{\bar{X}}_{\mathrm{HT}}\right)\right]
$$

Note that the leading term of the bias of the ratio estimator is of order $n^{-1}$.
Next, we consider the variance of the ratio estimator. By (8.8), we obtain

$$
\widehat{\bar{Y}}_{R}=\bar{Y}+\left(\widehat{\bar{Y}}_{\mathrm{HT}}-R \widehat{\bar{X}}_{\mathrm{HT}}\right)+O_{p}\left(n^{-1}\right)
$$

where $\hat{\theta}_{n}=O_{p}$ (1) denotes that $\hat{\theta}_{n}$ is bounded in probability. Ignoring $O_{p}\left(n^{-1}\right)$ terms, we have

$$
\mathbf{V}\left(\widehat{\bar{Y}}_{R}-\bar{Y}\right) \cong \mathbf{V}\left(\widehat{\bar{Y}}_{\mathrm{HT}}-R \widehat{\bar{X}}_{\mathrm{HT}}\right)
$$

Therefore, the ratio estimator is better than the HT estimator if

$$
-2 R \cdot \operatorname{Cov}\left(\widehat{\bar{Y}}_{\mathrm{HT}}, \widehat{\bar{X}}_{\mathrm{HT}}\right)+R^{2} \mathbf{V}\left(\widehat{\bar{X}}_{\mathrm{HT}}\right)<0
$$

which reduces to, under the simple random sampling,

$$
\frac{1}{2} \frac{\mathrm{CV}(x)}{\mathrm{CV}(y)}<\operatorname{Corr}(x, y)
$$

That is, under (8.12), the ratio estimator is more efficient than the HT estimator under SRS.

For variance estimation, using (8.11), we may use

$$
\sum_{i \in \mathcal{A}} \sum_{j \in \mathcal{A}} \frac{\pi_{i j}-\pi_{i} \pi_{j}}{\pi_{i j}} \frac{y_{i}-R x_{i}}{\pi_{i}} \frac{y_{j}-R x_{j}}{\pi_{j}}
$$

However, since we do not know $R$, we use $\hat{R}$ to obtain

$$
\hat{\mathbf{V}}\left(\hat{Y}_{R}\right)=\sum_{i \in \mathcal{A}} \sum_{j \in \mathcal{A}} \frac{\pi_{i j}-\pi_{i} \pi_{j}}{\pi_{i j}} \frac{y_{i}-\hat{R} x_{i}}{\pi_{i}} \frac{y_{j}-\hat{R} x_{j}}{\pi_{j}}
$$




---

as a variance estimator.
We now introduce Hajék estimator of the population mean as a special case of the ratio estimator. Hajék estimator uses $x_{i}=1$ in the ratio estimator. That is,

$$
\widehat{\bar{Y}}^{\pi}=\frac{\sum_{i \in \mathcal{A}} \pi_{i}^{-1} y_{i}}{\sum_{i \in \mathcal{A}} \pi_{i}^{-1}}
$$

is the Hajék estimator of the population mean and is often more efficient than the HT estimator $\widehat{\bar{Y}}^{\mathrm{HT}}=N^{-1} \sum_{i \in \mathcal{A}} \pi_{i}^{-1} y_{i}$. Using (8.10), we can obtain

$$
\widehat{\bar{Y}}^{\pi}=\bar{Y}+N^{-1} \sum_{i \in \mathcal{A}} \pi_{i}^{-1}\left(y_{i}-\bar{Y}\right)+O_{p}\left(n^{-1}\right)
$$

Thus, the variance of the Hajék estimator is obtained using $y_{i}-\bar{Y}$ instead of $y_{i}$ in the variance formula for the HT estimator.

In some cases, ratio itself is a parameter of interest. Domain estimation is an example of using a ratio for parameter estimation. Suppose that we are interested in the mean of $y$ in a particular domain $D$. That is, the parameter of interest is

$$
\bar{Y}_{D}=\frac{\sum_{i=1}^{N} z_{i} y_{i}}{\sum_{i=1}^{N} z_{i}}
$$

where

$$
z_{i}= \begin{cases}1 & \text { if } i \in D \\ 0 & \text { if } i \notin D\end{cases}
$$

To estimate $\bar{Y}_{D}$, we use

$$
\widehat{\bar{Y}}_{D, \pi}=\frac{\sum_{i \in \mathcal{A}} \pi_{i}^{-1} z_{i} y_{i}}{\sum_{i \in \mathcal{A}} \pi_{i}^{-1} z_{i}}
$$

By the Taylor linearization, we have

$$
\bar{Y}_{D, \pi}=\bar{Y}_{D}+N_{D}^{-1} \sum_{i \in \mathcal{A}} \pi_{i}^{-1} z_{i}\left(y_{i}-\bar{Y}_{D}\right)+O_{p}\left(n^{-1}\right)
$$

where $N_{D}=\sum_{i=1}^{N} z_{i}$. Under SRS,

$$
\begin{aligned}
\mathcal{V}\left(\widehat{\bar{Y}}_{D, \pi}\right) & \doteq \frac{1}{n(1-f)}\left(\frac{N}{N_{d}}\right)^{2} \frac{1}{N-1} \sum_{i=1}^{N} z_{i}\left(y_{i}-\bar{Y}_{D}\right)^{2} \\
& =\frac{1}{n(1-f)}\left(\frac{N}{N_{d}}\right)^{2} \frac{N_{d}-1}{N-1} S_{D}^{2}
\end{aligned}
$$

where $S_{D}^{2}=\left(N_{D}-1\right)^{-1} \sum_{i \in D}\left(y_{i}-\bar{Y}_{D}\right)^{2}$. If the sample size is large such that

$$
\frac{n_{D}}{n} \cong \frac{N_{D}}{N} \cong \frac{N_{D}-1}{N-1}
$$




---

holds, we have

$$
\mathcal{V}\left(\widehat{\bar{Y}}_{\mathrm{D}, \pi}\right) \doteq \frac{1}{n_{\mathrm{D}}}(1-f) S_{\mathrm{D}}^{2}
$$

where $S_{\mathrm{D}}^{2}$ is estimated by $s_{\mathrm{D}}^{2}=\left(n_{\mathrm{D}}-1\right)^{-1} \sum_{i \in \mathcal{A}} z_{i}\left(y_{i}-\bar{y}_{\mathrm{D}}\right)^{2}$.

# 8.3 Regression Estimation 

Ratio estimator is useful when there is strong positive correlation between $x$ and $y$. If the correlation is negative, the ratio estimator is actually worse than using the HT estimator. Also, ratio estimator is not directly applicable for the vector $\boldsymbol{x}$ cases. To overcome such limitation, we consider regression estimation in this section.

Suppose that the auxiliary information for unit $i$ is denoted by a $p$ dimensional vector $\boldsymbol{x}_{i}$ and its population total $\boldsymbol{X}=\sum_{i=1}^{N} \boldsymbol{x}_{i}$ is available. In the sample, we observe $\boldsymbol{x}_{i}$ and $y_{i}$. In this case, regression estimator of $Y=\sum_{i=1}^{N} y_{i}$ is defined as follows:

$$
\hat{Y}_{\mathrm{reg}}=\sum_{i=1}^{N} \hat{y}_{i}
$$

where $\hat{y}_{i}=\boldsymbol{x}_{i}^{\prime} \hat{\boldsymbol{B}}$ and

$$
\hat{\boldsymbol{B}}=\left(\sum_{i \in \mathcal{A}} \pi_{i}^{-1} \boldsymbol{x}_{i} \boldsymbol{x}_{i}^{\prime}\right)^{-1} \sum_{i \in \mathcal{A}} \pi_{i}^{-1} \boldsymbol{x}_{i} y_{i}
$$

If $\sum_{i \in \mathcal{A}} \pi_{i}^{-1} \boldsymbol{x}_{i} \boldsymbol{x}_{i}^{\prime}$ is singular, then its inverse does not exist. In such case, one may use the generalized inverse and still define regression estimator accordingly. For estimation of the population mean $\bar{Y}=N^{-1} \sum_{i=1}^{N} y_{i}$, the regression estimator of $\bar{Y}$ is defined by

$$
\widehat{\bar{Y}}_{\mathrm{reg}}=N^{-1} \sum_{i=1}^{N} \boldsymbol{x}_{i}^{\prime} \hat{\boldsymbol{B}}=\overline{\boldsymbol{X}}^{\prime} \hat{\boldsymbol{B}}
$$

where $\overline{\boldsymbol{X}}=N^{-1} \sum_{i=1}^{N} \boldsymbol{x}_{i}$.
In many cases, $\boldsymbol{x}_{i}$ includes an intercept term. If we write $\boldsymbol{x}_{i}=\left(1, x_{i 1}\right)$, the regression estimator in (8.15) reduces to

$$
\bar{Y}_{\mathrm{reg}}=\hat{B}_{0}+\bar{X}_{1}^{\prime} \hat{\boldsymbol{B}}_{1}
$$

where $\bar{X}_{1}=N^{-1} \sum_{i=1}^{N} x_{i 1}$,

$$
\hat{B}_{0}=\left(\sum_{i \in \mathcal{A}} \pi_{i}\right)^{-1} \sum_{i \in \mathcal{A}} \pi_{i}^{-1}\left(y_{i}-\boldsymbol{x}_{1 i}^{\prime} \hat{\boldsymbol{B}}_{1}\right)
$$




---

and

$$
\hat{\boldsymbol{B}}_{1}=\left[\sum_{i \in \mathcal{A}} \pi_{i}^{-1}\left(\boldsymbol{x}_{i 1}-\widehat{\overline{\boldsymbol{X}}}_{\pi 1}\right)\left(\boldsymbol{x}_{i 1}-\widehat{\overline{\boldsymbol{X}}}_{\pi 1}\right)^{\prime}\right]^{-1} \sum_{i \in \mathcal{A}} \pi_{i}^{-1}\left(\boldsymbol{x}_{i 1}-\widehat{\overline{\boldsymbol{X}}}_{\pi 1}\right) y_{i}
$$

Before we discuss statistical properties of the regression estimator, we briefly discuss some algebraic properties of the regression estimator. First, regression estimator is a linear estimator. That is, we can express the regression estimator in (8.15) as the linear form in (8.1) with

$$
w_{i}=\bar{\boldsymbol{X}}^{\prime}\left(\sum_{i \in \mathcal{A}} \pi_{i}^{-1} \boldsymbol{x}_{i} \boldsymbol{x}_{i}^{\prime}\right)^{-1} \pi_{i}^{-1} \boldsymbol{x}_{i}
$$

Note that the weights satisfy

$$
\sum_{i \in \mathcal{A}} w_{i} \boldsymbol{x}_{i}=\overline{\boldsymbol{X}}
$$

Thus, regression estimator satisfies the external consistency discussed in (8.2). Property (8.19) is also called calibration property or benchmarking property in the survey literature (Deville and Särndal, 1992). If the intercept term is included in $\boldsymbol{x}_{i}$, then $\sum_{i \in \mathcal{A}} w_{i}=1$ holds and the regression estimator is location-scale invariant. That is,

$$
\sum_{i \in \mathcal{A}} w_{i}\left(a+b y_{i}\right)=a+b \sum_{i \in \mathcal{A}} w_{i} y_{i}
$$

We now discuss statistical properties of the regression estimator. First assume that the sampling design and the HT estimators are such that

$$
N^{-1}\left(\sum_{i \in \mathcal{A}} \pi_{i}^{-1} \boldsymbol{z}_{i} \boldsymbol{z}_{i}^{\prime}-\sum_{i=1}^{N} \boldsymbol{z}_{i} \boldsymbol{z}_{i}^{\prime}\right)=O_{p}\left(n^{-1 / 2}\right)
$$

where $\boldsymbol{z}_{i}^{\prime}=\left(\boldsymbol{x}_{i}^{\prime}, y_{i}\right)$. Condition (8.20) means that the HT estimator of the population means converge in probability to their population mean and the order of convergence of the same as that of the sample mean in the IID case. The following lemma dervies Taylor linearization of the regression estimator.

Lemma 8.1. Under (8.20), the regression estimator satisfes

$$
\bar{Y}_{\mathrm{reg}}=\bar{\boldsymbol{X}}^{\prime} \boldsymbol{B}+\bar{\boldsymbol{X}}^{\prime}\left(\sum_{i=1}^{N} \boldsymbol{x}_{i} \boldsymbol{x}_{i}^{\prime}\right)^{-1} \sum_{i \in \mathcal{A}} \pi_{i}^{-1} \boldsymbol{x}_{i}\left(y_{i}-\boldsymbol{x}_{i}^{\prime} \boldsymbol{B}\right)+O_{p}\left(n^{-1}\right)
$$

where $\boldsymbol{B}=\left(\sum_{i=1}^{N} \boldsymbol{x}_{i} \boldsymbol{x}_{i}^{\prime}\right)^{-1} \sum_{i=1}^{N} \boldsymbol{x}_{i} y_{i}$.




---

Proof. Let

$$
(\hat{C}, \hat{d})=\sum_{k \in A} \pi_{k}^{-1}\left(x_{k} x_{k}^{\prime} x_{k} y_{k}\right)
$$

and

$$
(C, d)=\sum_{k=1}^{N}\left(x_{k} x_{k}^{\prime}, x_{k} y_{k}\right)
$$

The estimated regression coefficient $\hat{B}$ can be written as

$$
\hat{B}=f(\hat{C}, \hat{d})=\hat{C}^{-1} \hat{d}
$$

To compute Taylor linearization of vector $\hat{B}$, let $\hat{c}_{i j}$ be the $(i, j)$-th element of $\hat{C}$ and let $\hat{d}_{i}$ be the $i$-th element of $\hat{d}_{i}$. Taylor linearization of $\hat{B}$ can be expressed as

$$
f(\hat{C}, \hat{d}) \cong f(C, d)+\sum_{i}\left(\frac{\partial f}{\partial d_{i}}\right)\left(\hat{d}_{i}-d_{i}\right)+\sum_{i} \sum_{j}\left(\frac{\partial f}{\partial c_{i j}}\right)\left(\hat{c}_{i j}-c_{i j}\right)
$$

Here, we have

$$
\frac{\partial f}{\partial d_{i}}=C^{-1} e_{i}
$$

where $e_{i}$ is a vector where the $i$-th element is 1 and the remaining elements are 0 . Also,

$$
\frac{\partial f}{\partial c_{i j}}=-C^{-1} E_{i j} C^{-1} d
$$

where $E_{i j}=e_{i} e_{j}^{\prime}$ is a matrix where the $(i, j)$ th element is 1 and the remaining elements are zero. Thus, (8.22) reduces to

$$
\begin{aligned}
f(\hat{C}, \hat{d}) & \cong f(C, d)+C^{-1}(\hat{d}-d)-C^{-1}[\hat{C}-C] C^{-1} d \\
& =B+C^{-1}(\hat{d}-\hat{C} B)
\end{aligned}
$$

which proves (8.21).
If $x_{i}$ includes 1 , we can write $a^{\prime} x_{i}=1$ for some $a$ which implies $X a=\mathbf{1}_{N}$ (where $\mathbf{1}_{N}$ is a vector of ones with length $N$ ). Thus,

$$
\bar{X}^{\prime}\left(\sum_{i=1}^{N} x_{i} x_{i}^{\prime}\right)^{-1}=N^{-1}\left(\mathbf{1}_{N}^{\prime} X\right)\left(X^{\prime} X\right)^{-1}=N^{-1} a^{\prime} X^{\prime} X\left(X^{\prime} X\right)^{-1}=N^{-1} a^{\prime}
$$




---

and

$$
\bar{X}^{\prime} B=\bar{Y}
$$

Thus, (8.21) reduces to

$$
\widehat{\bar{Y}}_{\mathrm{reg}}=\bar{Y}+N^{-1} \sum_{i \in \mathcal{A}} \pi_{i}^{-1}\left(y_{i}-x_{i}^{\prime} B\right)+O_{p}\left(n^{-1}\right)
$$

which implies that

$$
\widehat{\bar{Y}}_{\mathrm{reg}}-\bar{Y}=N^{-1} \sum_{i \in \mathcal{A}} \pi_{i}^{-1}\left(y_{i}-x_{i}^{\prime} B\right)+o_{p}\left(n^{-1 / 2}\right)
$$

The leading term is unbiased to zero. The asymptotic variance of the regression estimator is then

$$
\mathcal{V}\left(\widehat{\bar{Y}}_{\text {reg }}\right) \doteq \mathcal{V}\left\{N^{-1} \sum_{i \in \mathcal{A}} \pi_{i}^{-1} e_{i}\right\}=\sum_{i \in \mathcal{U}} \sum_{j \in \mathcal{U}}\left(\pi_{i j}-\pi_{i} \pi_{j}\right) \frac{e_{i}}{\pi_{i}} \frac{e_{j}}{\pi_{j}}
$$

where $e_{i}=y_{i}-x_{i}^{\prime} B$.
Under SRS, the asymptotic variance can be written

$$
\mathcal{V}\left(\widehat{\bar{Y}}_{\text {reg }}\right) \doteq \frac{1}{n}\left(1-\frac{n}{N}\right) \frac{1}{N-1} \sum_{i=1}^{N}\left(y_{i}-x_{i}^{\prime} B\right)^{2}
$$

which leads to

$$
\mathcal{V}\left(\widehat{\bar{Y}}_{\mathrm{reg}}\right) \doteq \mathcal{V}(\bar{y}) \times\left(1-R^{2}\right)
$$

where $R^{2}$ is the coefficient of determination for the regression of $y$ on $x$ in the population level. Thus, the regression estimator is efficient if $R^{2}$ is large, i.e., when there is a strong linear relationship between $y$ and $x$. If the regression relation does not hold, the regression estimator is still asymptotically unbiased. Thus, the regression estimator is model-assisted, not model-dependent (Särndal et al., 1992).

To estimate the asymptotic variance in (8.24), we use

$$
\hat{\mathcal{V}}\left(\hat{Y}_{\mathrm{reg}}\right)=\sum_{i \in \mathcal{A}} \sum_{j \in \mathcal{A}} \frac{\pi_{i j}-\pi_{i} \pi_{j}}{\pi_{i j}} \frac{y_{i}-\hat{B} x_{i}}{\pi_{i}} \frac{y_{j}-\hat{B} x_{j}}{\pi_{j}}
$$

Next, we consider post-stratification which is a special case of regression estimation. Suppose that the finite population is partitioned into $G$ mutually exclusive and exhaustive groups. Assume that $N_{g}$, the population size of group $g$, are known for all $g=1, \cdots, G$. In this case, the auxiliary information can be written as $x_{i}=\left(x_{i 1}, x_{i 2}, \cdots, x_{i G}\right)^{\prime}$ where $x_{i g}$ is the indicator function for group $g$. The regression estimator is

$$
\hat{Y}_{\mathrm{reg}}=\sum_{i=1}^{N} x_{i}^{\prime}\left(\sum_{i \in \mathcal{A}} \pi_{i}^{-1} x_{i} x_{i}^{\prime}\right)^{-1} \sum_{i \in \mathcal{A}} \pi_{i}^{-1} x_{i} y_{i}
$$




---

Since

$$
\begin{aligned}
\sum_{i=1}^{N} \mathbf{x}_{i}^{\prime} & =\left(N_{1}, N_{2}, \cdots, N_{G}\right)^{\prime} \\
\sum_{i \in \mathcal{A}} \pi_{i}^{-1} \mathbf{x}_{i} \mathbf{x}_{i}^{\prime} & =\operatorname{diag}\left(\hat{N}_{1}, \hat{N}_{2}, \cdots, \hat{N}_{G}\right)
\end{aligned}
$$

where $\hat{N}_{g}=\sum_{i \in \mathcal{A}} \pi_{i}^{-1} x_{i g}$, the regression estimator reduces to

$$
\hat{Y}_{\text {post }}=\sum_{g=1}^{G} \sum_{i \in \mathcal{A}_{g}} \frac{\pi_{i}^{-1} N_{g}}{\hat{N}_{g}} y_{i}
$$

where $\mathcal{A}_{g}$ is the set of sample indices in group $g$. Thus, the final weights in post-stratified estimator are obtained by multiplying the design weight by the adjustment factor $\hat{N}_{g}^{-1} N_{g}$. Since $\mathbf{x}_{i}$ includes one, we can use (8.24) to obtain

$$
\mathcal{V}\left(\hat{Y}_{\text {post }}\right)=\mathcal{V}\left\{\sum_{g=1}^{G} \sum_{i \in \mathcal{A}_{g}} \pi_{i}^{-1}\left(y_{i}-\bar{Y}_{g}\right)\right\}+o\left(n^{-1}\right)
$$

Under SRS, the variance is

$$
\mathcal{V}\left(\hat{Y}_{\text {post }}\right) \doteq \frac{N^{2}}{n}\left(1-\frac{n}{N}\right) \frac{1}{N-1} \sum_{g=1}^{G} \sum_{i \in \mathcal{U}_{g}}\left(y_{i}-\bar{Y}_{g}\right)^{2}
$$

which is asymptotically equal to the variance of stratified sampling under proportional allocation.

Example 8.1. (Raking ratio estimation)
Suppose that we have $I \times J$ groups or cells. Cell counts $N_{i j}$ are not known. Marginal counts $N_{i}=P_{j=1}^{J} N_{i j}$ and $N_{. j}=\sum_{i=1}^{I} N_{i j}$ are known. In this case, we may consider the following two-way additive model

$$
\begin{aligned}
\mathcal{E}_{\zeta}\left(Y_{k}\right) & =\alpha_{i}+\beta_{j} \\
\mathcal{V}_{\zeta}\left(Y_{k}\right) & =\sigma^{2}
\end{aligned}
$$

where $\alpha_{i}, \beta_{j}$, and $\sigma^{2}$ are unknown parameters. Define

$$
\delta_{i j k}= \begin{cases}1 & \text { if } k \in \mathcal{U}_{i j} \\ 0 & \text { otherwise }\end{cases}
$$

Unfortunately, we do not observe $\delta_{i j k}$ in the population. Let

$$
\mathbf{x}_{k}=\left(\delta_{1 . k}, \delta_{2 . k}, \cdots, \delta_{I . k}, \delta_{.1 k}, \delta_{.2 k}, \cdots, \delta_{. J k}\right)
$$

and we know $\sum_{k=1}^{N} \mathbf{x}_{k}$.




---

The regression estimator in this case can be written as

$$
\hat{\bar{Y}}_{\mathrm{reg}}=\sum_{i \in \mathcal{A}} \frac{1}{\pi_{i}} g_{i}(\mathcal{A}) y_{i}
$$

where

$$
g_{i}(\mathcal{A})=\left(\sum_{k=1}^{N} \mathbf{x}_{k}\right)^{\prime}\left(\sum_{k \in \mathcal{A}} \frac{1}{\pi_{k}} \mathbf{x}_{k} \mathbf{x}_{k}^{\prime}\right)^{-1} \mathbf{x}_{i}
$$

Unfortunately, we cannot compute the inverse of $\sum_{k \in \mathcal{A}} \frac{1}{\pi_{k}} \mathbf{x}_{k} \mathbf{x}_{k}^{\prime}$ because its rank is $I+J-1$, which is not full rank. Thus, there is no unique solution $\hat{\mathbf{B}}$ to

$$
\sum_{i \in \mathcal{A}} \pi_{i}^{-1} \mathbf{x}_{i} \mathbf{x}_{i}^{\prime} \hat{\mathbf{B}}=\sum_{i \in \mathcal{A}} \pi_{i}^{-1} \mathbf{x}_{i} y_{i}
$$

The goal is to find $g_{k \mathcal{A}}=g_{k}(\mathcal{A})$ such that

$$
\begin{aligned}
\sum_{k \in \mathcal{A}} \frac{g_{k \mathcal{A}}}{\pi_{k}} \delta_{i \cdot, k} & =\sum_{k=1}^{N} \delta_{i . k}, \quad i=1,2, \cdots, I \\
\sum_{k \in \mathcal{A}} \frac{g_{k \mathcal{A}}}{\pi_{k}} \delta_{\cdot j k} & =\sum_{k=1}^{N} \delta_{\cdot j k}, \quad j=1,2, \cdots, J
\end{aligned}
$$

One way to obtain the solution to (8.30) and (8.31) is to solve the equations iteratively as follows:

1. Start with $g_{k \mathcal{A}}^{(0)}=1$.
2. For $\delta_{i . k}=1$,

$$
g_{k \mathcal{A}}^{(t+1)}=g_{k \mathcal{A}}^{(t)} \frac{\sum_{k=1}^{N} \delta_{i \cdot k}}{\sum_{k \in \mathcal{A}} g_{k \mathcal{A}}^{(t)} \delta_{i \cdot k} / \pi_{k}}
$$

It satisfies (8.30), but not necessarily satisfy (8.31).
3. For $\delta_{. j k}=1$,

$$
g_{k \mathcal{A}}^{(t+2)}=g_{k \mathcal{A}}^{(t+1)} \frac{\sum_{k=1}^{N} \delta_{. j k}}{\sum_{k \in \mathcal{A}} g_{k \mathcal{A}}^{(t+1)} \delta_{. j k} / \pi_{k}}
$$

It satisfies (8.31), but not necessarily satisfy (8.30).
4. Set $t \leftarrow t+2$ and go to Step 2 . Continue until convergence.

This computation method is called raking ratio estimation and was first considered by Deming and Stephan (1940) in the Census application. See also Deville et al. (1993).




---

# 9 

## Estimation: Part 2

### 9.1 GREG estimation

In Chapter 8, we have seen that the regression estimator is an efficient estimator when there is a linear relationship between $y$ and $x$. In this chapter, we generalize the concept of regression estimation to a more general class of models for developing model-assisted estimation.

To motivate the generalized regression estimator, we first introduce difference estimator. Suppose that a proxy value of $y_{i}$, denoted by $y_{i}^{(0)}$, throughout the population. The difference estimator of $Y=\sum_{i=1}^{N} y_{i}$ using $y_{1}^{(0)}, \cdots, y_{N}^{(0)}$ is defined as

$$
\hat{Y}_{\text {diff }}=\sum_{i=1}^{N} y_{i}^{(0)}+\sum_{i \in \mathcal{A}} \frac{1}{\pi_{i}}\left(y_{i}-y_{i}^{(0)}\right)
$$

The difference estimator is unbiased regardless of the choice of $y_{i}^{(0)}$. The variance of the difference estimator is

$$
\mathcal{V}\left(\hat{Y}_{\text {diff }}\right)=\mathcal{V}\left(\sum_{i \in \mathcal{A}} \frac{y_{i}-y_{i}^{(0)}}{\pi_{i}}\right)
$$

Thus, the difference estimator is unbiased regardless of $y_{i}^{(0)}$ but its variances are different for different choice of $y_{i}^{(0)}$. If $y_{i}^{(0)}$ is close to the true value of $y_{i}$, then the variance will be small.

In practice, we do not know $y_{i}^{(0)}$. Instead, we use auxiliary variable $x_{i}$ to construct a model for $y_{i}$ and develop $y_{i}^{(0)}$ from the model. That is, we assume that the finite population is a random sample of a superpopulation model that has generated the current finite population. One of the commonly used superpopulation models is

$$
\begin{aligned}
\mathcal{E}_{\zeta}\left(y_{i}\right) & =x_{i}^{\prime} \beta \\
\operatorname{Cov}_{\zeta}\left(y_{i}, y_{j}\right) & = \begin{cases}c_{i} \sigma^{2} & \text { if } i=j \\
0 & \text { if } i \neq j\end{cases}
\end{aligned}
$$

where $c_{i}=c\left(x_{i}\right)$ is a known function of $x_{i}$ and $\beta$ are $\sigma^{2}$ are unknown parameters. Model (9.2)-(9.3) is often called the generalized regression (GREG) model.




---

Under the GREG model, the (model-based) projection estimator is defined to be the sum of the predicted values in the GREG model. That is, we define

$$
\hat{Y}_{p}=\sum_{i=1}^{N} \hat{y}_{i}
$$

where $\hat{y}_{i}=\boldsymbol{x}_{i}^{\prime} \hat{\boldsymbol{\beta}}_{c}$ and

$$
\hat{\boldsymbol{\beta}}_{c}=\left(\sum_{i \in \mathcal{A}} \frac{1}{c_{i}} \boldsymbol{x}_{i} \boldsymbol{x}_{i}^{\prime}\right)^{-1} \sum_{i \in \mathcal{A}} \frac{1}{c_{i}} \boldsymbol{x}_{i} y_{i}
$$

The model-based projection estimator in (9.4) is developed under the GREG model in (9.3). Note that the probability limit of $\hat{\boldsymbol{\beta}}_{c}$ in (9.5) is

$$
\boldsymbol{B}_{c}=\left(\sum_{i=1}^{N} \frac{\pi_{i}}{c_{i}} \boldsymbol{x}_{i} \boldsymbol{x}_{i}^{\prime}\right)^{-1} \sum_{i=1}^{N} \frac{\pi_{i}}{c_{i}} \boldsymbol{x}_{i} y_{i}
$$

To ensure unbiasedness in the face of model misspecification, it's crucial that the resulting estimator also be asymptotically design unbiased (ADU). A key condition for achieving ADU is:

$$
\sum_{i \in \mathcal{A}} \frac{1}{\pi_{i}}\left(y_{i}-\hat{y}_{i}\right)=0
$$

To understand why condition (9.6) leads to ADU, note that (9.6) implies that

$$
\begin{aligned}
\hat{Y}_{p} & =\sum_{i=1}^{N} \boldsymbol{x}_{i}^{\prime} \hat{\boldsymbol{\beta}}+\sum_{i \in \mathcal{A}} \frac{1}{\pi_{i}}\left(y_{i}-\boldsymbol{x}_{i}^{\prime} \hat{\boldsymbol{\beta}}\right) \\
& =\hat{Y}_{\mathrm{HT}}+\left(\overline{\boldsymbol{X}}-\hat{\overline{\boldsymbol{X}}}_{\mathrm{HT}}\right)^{\prime} \hat{\boldsymbol{\beta}}
\end{aligned}
$$

The second term of (9.7) is a bias-correction term of the mode-based projection estimator in (9.4). Note that (9.4) is equivalent to (9.7) under condition (9.6). Condition (9.6) essentially makes the bias correction term identically equal to zero, which implies that the projection estimator in (9.4) is design consistent. In this sense, the condition (9.6) can be called the internally biased calibration (IBC) condition, which is termed by Firth and Bennett (1998).

The following lemma presents a sufficient condition for the projection estimator in (9.4) to be design consistent.

Lemma 9.1. If $c_{i}$ satisfies

$$
c_{i} / \pi_{i}=\lambda^{\prime} \boldsymbol{x}_{i}
$$

for some $\lambda$, then we have

$$
\sum_{i=1}^{N}\left(y_{i}-\boldsymbol{x}_{i}^{\prime} \boldsymbol{B}_{c}\right)=0
$$




---

and

$$
\sum_{i \in \mathcal{A}} \frac{1}{\pi_{i}}\left(y_{i}-\boldsymbol{x}_{i}^{\prime} \hat{\boldsymbol{\beta}}\right)=0
$$

Proof. First, by the definition of $\boldsymbol{B}_{c}$, we obtain

$$
\sum_{i=1}^{N}\left(y_{i}-\boldsymbol{x}_{i}^{\prime} \boldsymbol{B}_{c}\right) \frac{\boldsymbol{x}_{i}}{\pi_{i} c_{i}}=0
$$

Thus, pre-multiplying both sides of the above equation by $\boldsymbol{\lambda}^{\prime}$, we get

$$
\begin{aligned}
0 & =\sum_{i=1}^{N}\left(y_{i}-\boldsymbol{x}_{i}^{\prime} \boldsymbol{B}_{c}\right) \frac{\boldsymbol{\lambda}^{\prime} \boldsymbol{x}_{i}}{\pi_{i} c_{i}} \\
& =\sum_{i=1}^{N}\left(y_{i}-\boldsymbol{x}_{i}^{\prime} \boldsymbol{B}_{c}\right)
\end{aligned}
$$

where the second equality follows from (9.8). Thus, (9.9) is proved.
Now, to show (9.10), by the definition of $\hat{\boldsymbol{\beta}}$, we have

$$
\sum_{i \in \mathcal{A}}\left(y_{i}-\boldsymbol{x}_{i}^{\prime} \hat{\boldsymbol{\beta}}_{c}\right) \boldsymbol{x}_{i}^{\prime} / c_{i}=0
$$

which implies

$$
\sum_{i \in \mathcal{A}} \frac{1}{\pi_{i}}\left(y_{i}-\boldsymbol{x}_{i}^{\prime} \hat{\boldsymbol{\beta}}_{c}\right) \boldsymbol{x}_{i}^{\prime} \boldsymbol{\lambda} / c_{i}=0
$$

Thus, by (9.8), we have (9.10).
If (9.8) holds, then the projection estimator can be safely used as it satisfies ADU. If condition (9.8) does not hold, the projection estimator is not design consistent. To construct a design-consistent prediction estimator under the GREG model in (9.2)-(9.3), we use

$$
\hat{Y}_{\text {GREG }}=\hat{Y}_{\mathrm{HT}}+\left(\boldsymbol{X}-\hat{\boldsymbol{X}}_{\mathrm{HT}}\right)^{\prime} \hat{\boldsymbol{\beta}}_{c}
$$

as the bias-corrected prediction estimator. Now, using (9.11), we can express

$$
\begin{aligned}
\hat{Y}_{\mathrm{GREG}} & =\hat{Y}_{\mathrm{HT}}+\left(\boldsymbol{X}-\hat{\boldsymbol{X}}_{\mathrm{HT}}\right)^{\prime} \boldsymbol{B}_{c}+\left(\boldsymbol{X}-\hat{\boldsymbol{X}}_{\mathrm{HT}}\right)^{\prime}\left(\hat{\boldsymbol{\beta}}_{c}-\boldsymbol{B}_{c}\right) \\
& =\hat{Y}_{\mathrm{HT}}+\left(\boldsymbol{X}-\hat{\boldsymbol{X}}_{\mathrm{HT}}\right)^{\prime} \boldsymbol{B}_{c}+O_{p}\left(n^{-1} N\right)
\end{aligned}
$$

Thus, using (9.9), we obtain

$$
\hat{Y}_{\text {GREG }}-Y=\sum_{i \in \mathcal{A}} \pi_{i}^{-1}\left(y_{i}-\boldsymbol{x}_{i}^{\prime} \boldsymbol{B}_{c}\right)+O_{p}\left(n^{-1} N\right)
$$




---

which justifies the asymptotic unbiasedness of the GREG estimator in (9.7). The asymptotic variance is approximated by

$$
\mathcal{V}\left(\hat{Y}_{\mathrm{GREG}}\right) \cong \mathcal{V}\left(\sum_{i \in \mathcal{A}} \pi_{i}^{-1}\left(y_{i}-\mathbf{x}_{i}^{\prime} \mathbf{B}_{c}\right)\right)
$$

If $e_{i}=y_{i}-\mathbf{x}_{i}^{\prime} \mathbf{B}_{c}$ were observed, the variance (9.13) would be estimated by

$$
\mathcal{V}\left(\hat{Y}_{\mathrm{GREG}}\right) \cong \sum_{i \in \mathcal{A}} \sum_{j \in \mathcal{A}} \frac{\pi_{i j}-\pi_{i} \pi_{j}}{\pi_{i j}} \frac{e_{i}}{\pi_{i}} \frac{e_{j}}{\pi_{j}}
$$

If we use $\hat{e}_{i}=y_{i}-\mathbf{x}_{i}^{\prime} \hat{\boldsymbol{\beta}}$ instead of $E_{i}$, a consistent variance estimator is computed by

$$
\hat{\mathcal{V}}_{\mathrm{GREG}}=\sum_{i \in \mathcal{A}} \sum_{j \in \mathcal{A}} \frac{\pi_{i j}-\pi_{i} \pi_{j}}{\pi_{i j}} \frac{\hat{e}_{i}}{\pi_{i}} \frac{\hat{e}_{j}}{\pi_{j}}
$$

Using (9.11), we can express

$$
\hat{Y}_{\mathrm{GREG}}=\sum_{i \in \mathcal{A}} \hat{\omega}_{i} y_{i}
$$

where

$$
\hat{\omega}_{i}=d_{i}+\left(\mathbf{X}-\hat{\mathbf{X}}_{\mathrm{HT}}\right)^{\prime}\left(\sum_{k \in \mathcal{A}} \frac{1}{c_{k}} \mathbf{x}_{k} \mathbf{x}_{k}^{\prime}\right)^{-1} \frac{1}{c_{i}} \mathbf{x}_{i}
$$

and $d_{i}=\pi_{i}^{-1}$ is the design weight of unit $i$. The second term in (9.16) is the weight adjustment term incorporating the population auxiliary information $\mathbf{X}$. The final weights $\left\{\hat{\omega}_{i} ; i \in \mathcal{A}\right\}$ satisfy the calibration property

$$
\sum_{i \in \mathcal{A}} \hat{\omega}_{i} \mathbf{x}_{i}=\sum_{i=1}^{N} \mathbf{x}_{i}
$$

Since we can express

$$
\hat{\omega}_{i}=d_{i}+\hat{\boldsymbol{\lambda}}^{\prime} \mathbf{x}_{i} / c_{i}
$$

for some $\hat{\boldsymbol{\lambda}}$, it is linear in $\mathbf{x}_{i}$. Thus, if some individual values of $\mathbf{x}_{i}$ are extreme (too large or too small), then the final weights can be too large or too small, even take negative values. Also, if $c_{i}$ is large, then the effect of $\mathbf{x}_{i}$ on the final weight is reduced.

The GREG weight in (9.15) can be viewed as the solution to an optimization problem that minimizes

$$
Q(\boldsymbol{\omega})=\sum_{i \in \mathcal{A}}\left(\omega_{i}-d_{i}\right)^{2} c_{i}
$$




---

subject to

$$
\sum_{i \in \mathcal{A}} \omega_{i} \mathbf{x}_{i}=\sum_{i=1}^{N} \mathbf{x}_{i}
$$

Constraint (9.19) is attractive as it incorporates the external auxiliary information $\mathbf{X}=\sum_{i=1}^{N} \mathbf{x}_{i}$. The calibration condition (9.19) will be satisfied with $w_{i}=d_{i}$ approximately for sufficiently large $n$. Thus, the solution $\hat{w}_{i}$ to the above optimization problem will converge in probability to $d_{i}$.

By the Lagrange multiplier method, it is equivalent to minimizing

$$
Q(\boldsymbol{\omega}, \boldsymbol{\lambda})=\frac{1}{2} \sum_{i \in \mathcal{A}}\left(\omega_{i}-d_{i}\right)^{2} c_{i}+\boldsymbol{\lambda}^{\prime}\left(\mathbf{X}-\sum_{i \in \mathcal{A}} \omega_{i} \mathbf{x}_{i}\right)
$$

with respect to $\omega_{i}$ and $\lambda$. We can solve the optimization problem by computing the partial derivatives:

$$
\frac{\partial}{\partial \omega_{i}} Q=\left(\omega_{i}-d_{i}\right) c_{i}-\boldsymbol{\lambda}^{\prime} \mathbf{x}_{i}=0
$$

to obtain the form

$$
\omega_{i}=d_{i}+\boldsymbol{\lambda}^{\prime} \mathbf{x}_{i} / c_{i} .
$$

To compute $\boldsymbol{\lambda}$, we insert (9.21) to (9.19) and obtain

$$
\hat{\boldsymbol{\lambda}}^{\prime}=\left(\mathbf{X}-\hat{\mathbf{X}}_{\mathrm{HT}}\right)\left(\sum_{i \in \mathcal{A}} \mathbf{x}_{i} \mathbf{x}_{i}^{\prime} / c_{i}\right)^{-1}
$$

Therefore, (9.15) is obtained. Note that $\hat{\boldsymbol{\lambda}}$ will converge to zero in probability as $\hat{\mathbf{X}}_{\mathrm{HT}}$ will converge to $\mathbf{X}$ in probability.

Constraint (9.19) is called the calibration constraint, and the estimator obtained from an optimization problem of finding the final weights subject to the calibration constraint is called the calibration estimator.

More generally, instead of using the squared error distance in (9.18), we may consider minimizing

$$
Q(\boldsymbol{\omega})=\sum_{i \in \mathcal{A}} d_{i} G\left(\omega_{i} / d_{i}\right) c_{i}
$$

subject to the calibration constraints in (9.19), where $G(\cdot, d_{i}): \mathcal{V} \rightarrow \mathcal{R}$ is a nonnegative function that is strictly convex, differentiable, and $G^{\prime}(1)=0$. The domain $\mathcal{V}$ of $G(\cdot)$ is an interval in $\mathcal{R}$. For example, $G(\omega)=\omega \log (\omega)-\omega+1$, with possible domain $\mathcal{V} \subseteq(0, \infty)$, corresponds to the Kullback-Leibler divergence, while $G(\omega)=(\omega-1)^{2}$, with possible domain $\mathcal{V} \subseteq(-\infty, \infty)$, corresponds to the Chi-squared distance from 1 .

Let $\hat{\omega}_{i}$ be the solution to the above optimization problem and $\hat{Y}_{\text {cal }}=$ $\sum_{i \in \mathcal{A}} \hat{\omega}_{i} y_{i}$ be the resulting calibration estimator. Under some conditions on $G(\cdot), \hat{Y}_{\text {cal }}$ is asymptotically equivalent to the GREG estimator in (9.11). The result is summarized in the following theorem.




---

Theorem 9.1. Under some regularity conditions, the calibration estimator $\hat{Y}_{\text {cal }}$ satisfies

$$
\hat{Y}_{\mathrm{cal}}=\hat{Y}_{\mathrm{HT}}+\left(\mathbf{X}-\hat{\mathbf{X}}_{\mathrm{HT}}\right)^{\prime} \mathbf{B}+o_{p}\left(n^{-1 / 2} N\right)
$$

where

$$
\mathbf{B}=\left(\sum_{i=1}^{N} \mathbf{x}_{i} \mathbf{x}_{i}^{\prime} / c_{i}\right)^{-1} \sum_{i=1}^{N} \mathbf{x}_{i} y_{i} / c_{i}
$$

Proof. Using Lagrange multiplier method, the optimization problem can be expressed as maximizing

$$
Q_{1}(\boldsymbol{\omega}, \boldsymbol{\lambda})=-\sum_{i \in \mathcal{A}} d_{i} G\left(\omega_{i} / d_{i}\right) c_{i}+\boldsymbol{\lambda}^{\prime}\left(\sum_{i \in \mathcal{A}} \omega_{i} \mathbf{x}_{i}-\sum_{i=1}^{N} \mathbf{x}_{i}\right)
$$

Since

$$
\frac{\partial}{\partial \omega_{i}} Q_{1}=-g\left(\omega_{i} / d_{i}\right) c_{i}+\boldsymbol{\lambda}^{\prime} \mathbf{x}_{i}
$$

where $g(\omega)=d G(\omega) / d \omega$, the maximizer can be expressed as

$$
\omega_{i}^{\star}(\boldsymbol{\lambda})=d_{i} g^{-1}\left(\boldsymbol{\lambda}^{\prime} \mathbf{x}_{i} / c_{i}\right)
$$

and we obtain $\hat{\omega}_{i}=\omega_{i}^{\star}(\hat{\boldsymbol{\lambda}})$ where $\hat{\boldsymbol{\lambda}}$ satisfies (9.19).
Now, we can express

$$
\hat{Y}_{\mathrm{cal}}=\hat{Y}_{\mathrm{cal}}(\hat{\boldsymbol{\lambda}})=\sum_{i=1}^{N} I_{i} \omega_{i}^{\star}(\hat{\boldsymbol{\lambda}}) y_{i}
$$

where $\hat{\boldsymbol{\lambda}}$ satisfies (9.19), we can express

$$
\hat{Y}_{\mathrm{cal}}=\sum_{i=1}^{N} I_{i} \omega_{i}^{\star}(\hat{\boldsymbol{\lambda}}) y_{i}+\underbrace{\left(\sum_{i=1}^{N} \mathbf{x}_{i}-\sum_{i=1}^{N} I_{i} \omega_{i}^{\star}(\hat{\boldsymbol{\lambda}}) \mathbf{x}_{i}\right)^{\prime}}_{=0} \boldsymbol{\gamma}:=\hat{Y}_{\ell}(\hat{\boldsymbol{\lambda}}, \boldsymbol{\gamma})
$$

That is, $\hat{Y}_{\ell}(\hat{\boldsymbol{\lambda}}, \boldsymbol{\gamma})=\hat{Y}_{\mathrm{cal}}(\hat{\boldsymbol{\lambda}})$ for all $\boldsymbol{\gamma}$.
Let $\boldsymbol{\lambda}^{*}$ be the probability limit of $\hat{\boldsymbol{\lambda}}$. Since $\hat{\boldsymbol{\lambda}}$ satisfies $(9.19), \boldsymbol{\lambda}^{*}$ should satisfy

$$
\underbrace{\mathrm{E}\left\{\sum_{i=1}^{N} I_{i} \omega_{i}^{\star}\left(\lambda^{*}\right) \mathbf{x}_{i} \mid \mathcal{F}_{N}\right\}}_{=\sum_{i=1}^{N} \pi_{i} \omega_{i}^{\star}\left(\boldsymbol{\lambda}^{*}\right) \mathbf{x}_{i}}=\sum_{i=1}^{N} \mathbf{x}_{i}
$$




---

which implies that

$$
\omega_{i}^{\star}\left(\boldsymbol{\lambda}^{*}\right)=\pi_{i}^{-1}=d_{i}
$$

or $g^{-1}\left(\boldsymbol{x}_{i}^{\prime} \boldsymbol{\lambda}^{*} / c_{i}\right)=1$. Since $g(1)=0$ and $g(\cdot)$ is one-to-one, we get $\boldsymbol{\lambda}^{*}=\mathbf{0}$. Now, if we can find $\boldsymbol{\gamma}^{*}$ such that

$$
E\left\{\frac{\partial}{\partial \boldsymbol{\lambda}} \hat{Y}_{\ell}\left(\boldsymbol{\lambda}^{*}, \boldsymbol{\gamma}\right) \mid \mathcal{F}\right\}=\mathbf{0}
$$

at $\boldsymbol{\gamma}=\boldsymbol{\gamma}^{*}$, then the sampling error of $\hat{\boldsymbol{\lambda}}$ can be safely ignored (Randles, 1982) and we can obtain

$$
\hat{Y}_{\mathrm{cal}}=\hat{Y}_{\ell}\left(\boldsymbol{\lambda}^{*}, \boldsymbol{\gamma}^{*}\right)+o_{p}\left(n^{-1 / 2} N\right)
$$

Now, since

$$
\frac{\partial}{\partial \boldsymbol{\lambda}} \hat{Y}_{\ell}\left(\boldsymbol{\lambda}^{*}, \boldsymbol{\gamma}\right)=\sum_{i=1}^{N} I_{i} d_{i} \frac{1}{g^{\prime}\left(\boldsymbol{x}_{i}^{\prime} \boldsymbol{\lambda}^{*} / c_{i}\right)}\left(y_{i}-\boldsymbol{x}_{i}^{\prime} \boldsymbol{\gamma}\right) \boldsymbol{x}_{i} / c_{i}
$$

and $g^{\prime}(0)>0$ is constant, we obtain

$$
\boldsymbol{\gamma}^{*}=\left(\sum_{i=1}^{N} \boldsymbol{x}_{i} \boldsymbol{x}_{i}^{\prime} / c_{i}\right)^{-1} \sum_{i=1}^{N} \boldsymbol{x}_{i} y_{i} / c_{i}
$$

Therefore, by (9.25) with $\gamma^{*}=\boldsymbol{B}$, we obtain (9.23).
See Deville and Särndal (1992) and Fuller (2002) for further discussion of the calibration weighting method.

# 9.2 Optimal Estimation 

So far, we have discussed a class of model-assisted estimators that improve the efficiency of the HT estimator by incorporating auxiliary information. In this section, we explore the optimality of the Generalized Regression (GREG) estimator within a certain class of estimators. We initially demonstrate the nonexistence of the Uniformly Minimum Variance Unbiased Estimator (UMVUE) in a strictly design-based context, which was originally discovered by Godambe and Joshi (1965) and then also proved by Basu (1971) with a simpler proof.

Theorem 9.2. Let any noncensus design with $\pi_{k}>0(k=1,2, \cdots, N)$ be given. Then no uniformly minimum variance estimator exists in the class of all unbiased estimators of $Y=\sum_{i=1}^{N} y_{i}$.




---

Proof. For a given value $\mathbf{y}^{*}=\left(y_{1}^{*}, y_{2}^{*}, \cdots, y_{N}^{*}\right)$, consider the following difference estimator:

$$
\hat{Y}_{\text {diff }}=\sum_{i=1}^{N} y_{i}^{*}+\sum_{i \in \mathcal{A}} \frac{1}{\pi_{i}}\left(y_{i}-y_{i}^{*}\right)
$$

This estimator is unbiased regardless of $\mathbf{y}^{*}=\left(y_{1}^{*}, y_{2}^{*}, \cdots, y_{N}^{*}\right)$, and its variance is zero when $\mathbf{y}=\mathbf{y}^{*}$.

For an unbiased estimator $\hat{Y}$ to be considered a UMVUE, it must satisfy:

$$
\mathbb{V}(\hat{Y}) \leq \mathbb{V}\left(\hat{Y}_{\text {diff }}\right), \quad \forall \mathbf{y}
$$

Given that $\mathbb{V}\left(\hat{Y}_{\text {diff }}\right)=0$ for $\mathbf{y}=\mathbf{y}^{*}$, it implies that $\mathbb{V}(\hat{Y})=0$ for $\mathbf{y}=\mathbf{y}^{*}$. Since any arbitrary $\mathbf{y}^{*}$ can be chosen, it follows that $\mathbb{V}(\hat{Y})=0$ for all $\mathbf{y}$, a condition that only holds for a census.

The theorem discussed above demonstrates that it is not feasible to identify the optimal estimator within the class of unbiased estimators in terms of minimizing the design variance. To address this challenge, we adjust our approach for evaluating the efficiency of estimators by incorporating the superpopulation model into our considerations. More precisely, we will examine the expected value of the design variance under the superpopulation model. This type of variance is referred to as the anticipated variance and is formally defined as follows.
Definition 9.1. Anticipated variance of $\hat{\theta}$ is defined by

$$
\mathbb{A V}(\hat{\theta})=\mathbb{E}_{\zeta}\left\{\mathbb{V}\left(\hat{\theta} \mid \mathcal{F}_{N}\right)\right\}
$$

where subscript $\zeta$ denotes the distribution with respect to the superpopulation model and the conditional expectation given $\mathcal{F}=\left\{y_{1}, \ldots, y_{N}\right\}$ denotes the design-based expectation under the sampling mechanism.

Lemma 9.2. Let $\hat{\theta}$ be design-unbiased for $\theta_{N}$. The anticipated variance of $\hat{\theta}$ can be written as

$$
\mathbb{A V}(\hat{\theta})=\mathbb{E}_{p}\left\{\operatorname{Var}_{\zeta}(\hat{\theta})\right\}+\operatorname{Var}_{p}\left\{\mathbb{E}_{\zeta}(\hat{\theta})\right\}-\operatorname{Var}_{\zeta}\left(\theta_{N}\right)
$$

Proof. Since $\hat{\theta}$ is design-unbiased for $\theta_{N}$, we can write

$$
\mathbb{A V}(\hat{\theta})=\mathbb{E}_{\zeta} \mathbb{V}_{a r p}(\hat{\theta})=\mathbb{E}_{\zeta} \mathbb{E}_{p}\left(\hat{\theta}-\theta_{N}\right)^{2}
$$

Thus,

$$
\begin{aligned}
& \mathbb{A V}(\hat{\theta})=\mathbb{E}_{p} \mathbb{E}_{\zeta}\left(\hat{\theta}-\theta_{N}\right)^{2} \\
& =\mathbb{E}_{p} \mathbb{E}_{\zeta}\left\{\hat{\theta}-\mathbb{E}_{\zeta}(\hat{\theta})+\mathbb{E}_{\zeta}(\hat{\theta})-\mathbb{E}_{\zeta}\left(\theta_{N}\right)+\mathbb{E}_{\zeta}\left(\theta_{N}\right)-\theta_{N}\right\}^{2}
\end{aligned}
$$




---

and

$$
\begin{aligned}
\operatorname{AV}(\hat{\theta})= & \mathrm{E}_{p} \mathrm{E}_{\zeta}\{\hat{\theta}-\mathrm{E}_{\zeta}(\hat{\theta})\}^{2}+\mathrm{E}_{p}\left\{\mathrm{E}_{\zeta}(\hat{\theta})-\mathrm{E}_{\zeta}\left(\theta_{N}\right)\right\}^{2}+\mathrm{E}_{p}\left\{\mathrm{E}_{\zeta}\left(\theta_{N}\right)-\theta_{N}\right\}^{2} \\
& +2 \mathrm{E}_{p}\left\{\left(\hat{\theta}-\mathrm{E}_{\zeta}(\hat{\theta})\right)\left(\mathrm{E}_{\zeta}\left(\theta_{N}\right)-\theta_{N}\right)\right\}
\end{aligned}
$$

and the remaining cross product terms are zero. Since

$$
\mathrm{E}_{p}\left\{\left(\hat{\theta}-\mathrm{E}_{\zeta}(\hat{\theta})\right)\right\}=-\left(\mathrm{E}_{\zeta}\left(\theta_{N}\right)-\theta_{N}\right)
$$

and

$$
\begin{aligned}
& 2 \mathrm{E}_{p}\left\{\left(\hat{\theta}-\mathrm{E}_{\zeta}(\hat{\theta})\right)\left(\mathrm{E}_{\zeta}\left(\theta_{N}\right)-\theta_{N}\right)\right\} \\
= & 2\left(\mathrm{E}_{\zeta}\left(\theta_{N}\right)-\theta_{N}\right) \mathrm{E}_{p}\left\{\left(\hat{\theta}-\mathrm{E}_{\zeta}(\hat{\theta})\right)\right\}=-2\left(\mathrm{E}_{\zeta}\left(\theta_{N}\right)-\theta_{N}\right)^{2}
\end{aligned}
$$

we obtain

$$
\operatorname{AV}(\hat{\theta})=\mathrm{E}_{p} \mathrm{E}_{\zeta}\{\hat{\theta}-\mathrm{E}_{\zeta}(\hat{\theta})\}^{2}+\mathrm{E}_{p}\left\{\mathrm{E}_{\zeta}(\hat{\theta})-\mathrm{E}_{\zeta}\left(\theta_{N}\right)\right\}^{2}-\left\{\mathrm{E}_{\zeta}\left(\theta_{N}\right)-\theta_{N}\right\}^{2}
$$

which proves $(9.27)$.
The following theorem presents the lower bound of the anticipated variance for a design unbiased estimator.

Theorem 9.3. Let $y_{i}$ be independently distributed in the superpopulation model. The anticipate variance of any design-unbiased estimator $\hat{Y}$ of $Y=$ $\sum_{i=1}^{N} y_{i}$ satisfies

$$
\mathrm{E}_{\zeta}\left\{\mathrm{V}\left(\hat{Y} \mid \mathcal{F}_{N}\right)\right\} \geq \sum_{i=1}^{N}\left(\frac{1}{\pi_{i}}-1\right) \operatorname{Var}_{\zeta}\left(y_{i}\right)
$$

Proof. Write $\hat{Y}$ as $\hat{Y}=\hat{Y}_{\mathrm{HT}}+R$ where $\hat{Y}_{\mathrm{HT}}$ is the HT estimator of $Y$. Since $\hat{Y}$ is design unbiased, we have $\mathrm{E}(R)=0$ and, for fixed $j \in U$,

$$
\begin{aligned}
0 & =\mathrm{E}(R) \\
& =\sum_{A \in \mathcal{A}} p(A) R(A) \\
& =\sum_{A \in \mathcal{A} ; j \in A} p(A) R(A)+\sum_{A \in \mathcal{A} ; j \notin A} p(A) R(A)
\end{aligned}
$$

Now, since

$$
\mathrm{V}_{\zeta}(\hat{Y})=\mathrm{V}_{\zeta}\left(\hat{Y}_{\mathrm{HT}}\right)+\mathrm{V}_{\zeta}(R)+2 \operatorname{Cov}_{\zeta}\left(\hat{Y}_{\mathrm{HT}}, R\right)
$$




---

we obtain

$$
\begin{aligned}
\mathrm{E}_{p}\left\{\operatorname{Cov}_{\zeta}\left(\hat{Y}_{\mathrm{HT}, R}\right)\right\}= & \mathrm{E}_{p}\left[\mathrm{E}_{\zeta}\left\{\left(\hat{Y}_{\mathrm{HT}}-\mathrm{E}_{\zeta}\left(\hat{Y}_{\mathrm{HT}}\right)\right) R\right\}\right] \\
= & \mathrm{E}_{p}\left[\sum_{j \in U} \mathrm{E}_{\zeta}\left\{\left(y_{j}-\mathrm{E}_{\zeta}\left(y_{j}\right)\right) \frac{I_{j}}{\pi_{j}} R\right\}\right] \\
= & \sum_{j \in U} \mathrm{E}_{\zeta}\left\{\left(y_{j}-\mathrm{E}_{\zeta}\left(y_{j}\right)\right) \frac{\pi_{j}}{\mathrm{E}\left\{I_{j}(A) R(A)\right\}}\right\} \\
= & \sum_{j \in U} \mathrm{E}_{\zeta}\left\{\left(y_{j}-\mathrm{E}_{\zeta}\left(y_{j}\right)\right) \frac{\pi_{j}}{\sum_{A \in \mathcal{A} ; j \in A} R(A) p(A)}\right\} \\
= & -\sum_{j \in U} \mathrm{E}_{\zeta}\left\{\left(y_{j}-\mathrm{E}_{\zeta}\left(y_{j}\right)\right) \frac{\pi_{j}}{\sum_{A \in \mathcal{A} ; j \notin A} R(A) p(A)}\right\} \\
= & 0
\end{aligned}
$$

where the last equality follows because $\sum_{A \in \mathcal{A} ; j \notin A} R(A) p(A)$ does not depend on $y_{j}$. Thus,

$$
\begin{aligned}
\mathrm{E}_{p}\left\{\mathrm{V}_{\zeta}(\hat{Y})\right\} & =\mathrm{E}_{p}\left\{\mathrm{V}_{\zeta}\left(\hat{Y}_{\mathrm{HT}}\right)\right\}+\mathrm{E}_{p}\left\{\mathrm{V}_{\zeta}(R)\right\} \\
& \geq \mathrm{E}_{p}\left\{\mathrm{V}_{\zeta}\left(\hat{Y}_{\mathrm{HT}}\right)\right\} \\
& =\mathrm{E}_{p}\left\{\mathrm{V}_{\zeta}\left(\sum_{i=1}^{N} y_{i} \frac{I_{i}}{\pi_{i}}\right)\right\} \\
& =\mathrm{E}_{p}\left(\sum_{i=1}^{N} \frac{\sigma_{i}^{2} I_{i}}{\pi_{i}^{2}}\right) \\
& =\sum_{i=1}^{N} \frac{\sigma_{i}^{2}}{\pi_{i}}
\end{aligned}
$$

and we have

$$
\begin{aligned}
\operatorname{AV}(\hat{Y}) & =\mathrm{E}_{p} \mathrm{~V}_{\zeta}(\hat{Y})+\mathrm{V}_{p} \mathrm{E}_{\zeta}(\hat{Y})-\mathrm{V}_{\zeta}(Y) \\
& \geq \mathrm{E}_{p} \mathrm{~V}_{\zeta}(\hat{Y})-\mathrm{V}_{\zeta}(Y) \\
& \geq \sum_{i=1}^{N} \frac{\sigma_{i}^{2}}{\pi_{i}}-\sum_{i \in U} \sigma_{i}^{2}
\end{aligned}
$$

The lower bound in (9.28) is the lower bound of the anticipated variance of any unbiased estimator. The lower bound was first discovered by Godambe and Joshi (1965) and is often called Godambe-Joshi lower bound. For a fix-ed




---

size probability sampling design, the Godambe-Joshi lower bound is minimized when

$$
\pi_{i} \propto\left\{\operatorname{Var}_{\zeta}\left(y_{i}\right)\right\}^{1 / 2}
$$

To show this, we minimize $\sum_{i=1}^{N} \operatorname{Var}_{\zeta}\left(y_{i}\right) / \pi_{i}$ subject to $\sum_{i=1}^{N} \pi_{i}=n$. The solution can be obtained by applying Cauchy -Schwarz inequality to get

$$
\left\{\sum_{i=1}^{N} \sigma_{i}^{2} / \pi_{i}\right\}\left\{\sum_{i=1}^{N} \pi_{i}\right\} \geq\left\{\sum_{i=1}^{N} \sigma_{i}\right\}^{2}
$$

with equality when (9.29) holds.
The following theorem, which was first proved by Isaki and Fuller (1982), shows that the GREG estimator achieves the Godambe-Joshi lower bound asymptotically.

Theorem 9.4. Suppose that $\zeta$ is a superpopulation model with $y_{i}$ 's independent and $\mathrm{E}_{\zeta}\left(y_{i}\right)=\mathbf{x}_{i}^{\prime} \boldsymbol{\beta}$ and $\mathrm{V}_{\zeta}\left(y_{i}\right)=c_{i} \sigma^{2}$. Then, the anticipated variance of the GREG estimator in (9.11) asymptotically attains the Godambe-Joshi lower bound.

Proof. By (9.12), the GREG estimator is asymptotically equivalent to the difference estimator in (9.12). Thus,

$$
\begin{aligned}
\mathrm{E}_{\zeta}\left\{\mathrm{V}\left(\hat{Y}_{\text {GREG }}\right)\right\} & \doteq \mathrm{E}_{\zeta}\left\{\sum_{i=1}^{N} \sum_{j=1}^{N}\left(\pi_{i j}-\pi_{i} \pi_{j}\right) \frac{y_{i}-\mathbf{x}_{i}^{\prime} \mathbf{B}_{c}}{\pi_{i}} \frac{y_{j}-\mathbf{x}_{j}^{\prime} \mathbf{B}_{c}}{\pi_{j}}\right\} \\
& \doteq \mathrm{E}_{\zeta}\left\{\sum_{i=1}^{N} \sum_{j=1}^{N}\left(\pi_{i j}-\pi_{i} \pi_{j}\right) \frac{y_{i}-\mathbf{x}_{i}^{\prime} \boldsymbol{\beta}}{\pi_{i}} \frac{y_{j}-\mathbf{x}_{j}^{\prime} \boldsymbol{\beta}}{\pi_{j}}\right\} \\
& =\sum_{i=1}^{N}\left(\frac{1}{\pi_{i}}-1\right) c_{i} \sigma^{2}
\end{aligned}
$$

which is equal to the Gobambe-Joshi lower bound under the superpopulation model.

# 9.3 Model-assisted calibration 

We now turn our attention to a model-assisted approach for calibration estimation. To illustrate the concept of calibration estimation within the framework of the superpopulation model specified in equations (9.2)-(9.3), let's consider a linear estimator defined as

$$
\hat{Y}_{\omega}=\sum_{i \in \mathcal{A}} \omega_{i} y_{i}
$$




---

for some $\omega_{i}$. Now, note that

$$
\hat{Y}_{\omega}-Y=\underbrace{\left\{\sum_{i \in \mathcal{A}} \omega_{i} x_{i}^{\prime} \beta-\sum_{i=1}^{N} x_{i}^{\prime} \beta\right\}}_{:=C}+\underbrace{\left\{\sum_{i \in \mathcal{A}} \omega_{i} e_{i}-\sum_{i=1}^{N} e_{i}\right\}}_{:=D} .
$$

The first term, $C$, can be eliminated if the weights $\omega_{i}$ satisfy the calibration constraint (9.19). Consequently, our goal shifts to minimizing the model variance of the term $D$. Note that

$$
\begin{aligned}
& \mathbb{E}_{\zeta}\left(D^{2} \mid I_{1}, \cdots, I_{N}\right) \\
& =\sum_{i \in \mathcal{A}} \omega_{i}^{2} c_{i} \sigma^{2}-2 \sum_{i \in \mathcal{A}} \omega_{i} c_{i} \sigma^{2}+\sum_{i=1}^{N} c_{i} \sigma^{2}
\end{aligned}
$$

If the condition $c_{i}=\lambda^{\prime} x_{i}$ is met, then the calibration constraint in (9.19) implies that

$$
\sum_{i \in \mathcal{A}} \omega_{i} c_{i}=\sum_{i=1}^{N} c_{i}
$$

If $c_{i}=1$, then (9.8) means that $x_{i}$ includes an intercept term and constraint $(9.31)$ is a normalization constraint for $\omega_{i}$.

Therefore, under (9.8) and (9.19), minimizing the model variance of $D$ is equivalent to minimizing

$$
Q(w)=\sum_{i \in \mathcal{A}} \omega_{i}^{2} c_{i}
$$

The optimal calibration estimator is then given by

$$
\hat{Y}_{\mathrm{opt}}=\sum_{i \in \mathcal{A}} \hat{\omega}_{i} y_{i}=\sum_{i=1}^{N} x_{i}^{\prime} \hat{\beta}_{c}
$$

where $\hat{\beta}_{c}=\left(\sum_{i \in \mathcal{A}} c_{i}^{-1} x_{i} x_{i}^{\prime}\right)^{-1} \sum_{i \in \mathcal{A}} c_{i}^{-1} x_{i} y_{i}$. This formulation reveals that the final calibration estimator can be interpreted as a projection estimator in Section 9.1.

For the regression projection estimator with $\hat{y}_{i}=x_{i}^{\prime} \hat{\beta}$, by Lemma 9.1, the IBC condition in (9.6) can be met by augmenting $x_{i}$ to include $\frac{\pi_{i}^{-1}}{c_{i}}$. In other words, by defining $z_{i}^{\prime}=\left(x_{i}^{\prime}, \frac{\pi_{i}^{-1}}{c_{i}}\right)$ and calculating $\hat{\gamma}=$ $\left(\sum_{i \in \mathcal{A}} c_{i}^{-1} z_{i} z_{i}^{\prime}\right)^{-1} \sum_{i \in \mathcal{A}} c_{i}^{-1} z_{i} y_{i}$, the property of the residuals ensures that $\hat{y}_{i}=z_{i}^{\prime} \hat{\gamma}$ fulfills

$$
\sum_{i \in \mathcal{A}}\left(y_{i}-\hat{y}_{i}\right) z_{i} c_{i}^{-1}=\mathbf{0}
$$

thereby implying the IBC condition in (9.6). This approach effectively integrates additional calibration into the estimation process, enhancing its robustness against potential model misspecification.




---

To minimize the model variance $\hat{\theta}_{\omega}$ while also adhering to the Asymptotically Design Unbiased (ADU) condition, our objective narrows down to minimizing

$$
\sum_{i \in \mathcal{A}} \omega_{i}^{2} c_{i}
$$

subject to

$$
\sum_{i \in \mathcal{A}} \omega_{i} \mathbf{z}_{i}=\sum_{i=1}^{N} \mathbf{z}_{i}
$$

where $\mathbf{z}_{i}^{\prime}=\left(\mathbf{x}_{i}^{\prime}, \pi_{i}^{-1} c_{i}\right)$.
Let $\hat{\omega}_{i}$ be the solution to the optimization problem described above. Using the Lagrangian multiplier method, it can be shown that the resulting estimator can be written as

$$
\hat{Y}_{\mathrm{cal}}=\sum_{i \in \mathcal{A}} \hat{\omega}_{i} y_{i}=\sum_{i \in \mathcal{U}} \mathbf{z}_{i}^{\prime} \hat{\boldsymbol{\gamma}}+\sum_{i \in \mathcal{A}} \frac{1}{\pi_{i}}\left(y_{i}-\mathbf{z}_{i}^{\prime} \hat{\boldsymbol{\gamma}}\right)
$$

where

$$
\hat{\omega}_{i}=\left(\sum_{i=1}^{N} \mathbf{z}_{i}\right)^{\prime}\left(\sum_{i \in \mathcal{A}} c_{i}^{-1} \mathbf{z}_{i} \mathbf{z}_{i}^{\prime}\right)^{-1} \mathbf{z}_{i} / c_{i}
$$

and

$$
\hat{\boldsymbol{\gamma}}=\left(\sum_{i \in \mathcal{A}} c_{i}^{-1} \mathbf{z}_{i} \mathbf{z}_{i}^{\prime}\right)^{-1} \sum_{i \in \mathcal{A}} c_{i}^{-1} \mathbf{z}_{i} y_{i}
$$

Let $\boldsymbol{\gamma}^{*}$ be the probability limit of $\hat{\boldsymbol{\gamma}}$. Using the standard argument similar to (9.12), we can obtain

$$
N^{-1} \hat{Y}_{\mathrm{cal}}=N^{-1} \hat{Y}_{\mathrm{diff}}+O_{p}\left(n^{-1}\right)
$$

where

$$
\hat{Y}_{\mathrm{diff}}=\sum_{i \in \mathcal{U}} \mathbf{z}_{i}^{\prime} \boldsymbol{\gamma}^{*}+\sum_{i \in \mathcal{A}} \frac{1}{\pi_{i}}\left(y_{i}-\mathbf{z}_{i}^{\prime} \boldsymbol{\gamma}^{*}\right)
$$

Now, note that

$$
\hat{Y}_{\mathrm{diff}}-Y=\sum_{i=1}^{N}\left(\frac{I_{i}}{\pi_{i}}-1\right)\left(y_{i}-\mathbf{z}_{i}^{\prime} \boldsymbol{\gamma}^{*}\right)
$$

and

$$
\begin{aligned}
E\left\{\left(\hat{Y}_{\text {diff }}-Y\right)^{2}\right\} & =E\left\{\sum_{i=1}^{N}\left(\frac{I_{i}}{\pi_{i}}-1\right)^{2} v_{i}\right\} \\
& =\sum_{i=1}^{N}\left(\frac{1}{\pi_{i}}-1\right) v_{i}
\end{aligned}
$$




---

where $v_{i}=\mathrm{E}_{\zeta}\left\{\left(y_{i}-\boldsymbol{z}_{i}^{\prime} \boldsymbol{\gamma}^{*}\right)^{2} \mid \boldsymbol{z}_{i}\right\}$.
If the Generalized Regression (GREG) model specified in equations (9.2)(9.3) is accurate, then the variance component for each unit, $v_{i}$, is equal to $c_{i} \sigma^{2}$. However, if the GREG model does not accurately represent the underlying data structure, it is possible to observe that $c_{i} \sigma^{2}>v_{i}$. This discrepancy arises because the additional covariate $\pi_{i}^{-1} c_{i}$ improves the prediction of $y_{i}$, thus contributing to a more precise estimation.

Consequently, it can be concluded that the model-assisted calibration estimator, which employs the augmented covariate $\boldsymbol{z}_{i}$ for calibration, exhibits greater efficiency compared to the GREG estimator, especially when the superpopulation model delineated in equations (9.2)-(9.3) does not perfectly align with the actual data. This advantage underscores the robustness of the calibration approach in accommodating model inaccuracies and improving the accuracy of the estimate.

For general models, Wu and Sitter (2001) introduced the concept of model calibration, which integrates the working regression model directly into the calibration constraint. This approach involves using $\hat{m}_{i}=m\left(\boldsymbol{x}_{i} ; \hat{\boldsymbol{\beta}}\right)$ as an estimated predictor for $y_{i}$, derived from the working regression model where $\mathrm{E}(Y \mid \boldsymbol{x})=m(\boldsymbol{x} ; \boldsymbol{\beta})$. If it is possible to calculate $\hat{m}_{i}$ for every unit of the population, then the following equation can be employed as the calibration constraint for the weighting problem:

$$
\sum_{i \in \mathcal{A}} w_{i}\left(1, \hat{m}_{i}\right)=\sum_{i=1}^{N}\left(1, \hat{m}_{i}\right)
$$

The uncertainty of $\hat{\boldsymbol{\beta}}$ in $\hat{m}_{i}$ can be safely ignored in the final inference.
Instead of using model calibration, an alternative approach involves calibrating for basis functions. This method is applicable when the expected value of $Y$ on $\boldsymbol{x}$ belongs to the span of a set of basis functions $b_{1}(\boldsymbol{x}), \cdots, b_{L}(\boldsymbol{x})$. In such scenarios, the calibration estimation can utilize the following constraint:

$$
\sum_{i \in \mathcal{A}} w_{i}\left[b_{1}\left(\boldsymbol{x}_{i}\right), \cdots, b_{L}\left(\boldsymbol{x}_{i}\right)\right]=\sum_{i=1}^{N}\left[b_{1}\left(\boldsymbol{x}_{i}\right), \cdots, b_{L}\left(\boldsymbol{x}_{i}\right)\right]
$$

This condition ensures that the $\boldsymbol{C}$ term in (9.30) is nullified. As the sample size increases, the dimension $L$ of the basis functions may also need to be increased. In such instances, regularization methods can be employed to select a suitable $L$.

For example, Montanari and Ranalli (2005) explored the use of neural network models, while Breidt et al. (2005) applied penalized spline models for nonparametric calibration estimation. These methodologies offer a flexible framework for calibration estimation, allowing for the accommodation of complex relationships between the response variable.




---

# 9.4 Generalized entropy calibration 

Instead of the squared error loss in (9.32), we can consider the we now consider maximizing the generalized entropy that does not depend on the design weights, which was proposed by Kwon et al. (2024). Using (9.2)-(9.3) as a working model for model-assisted estimation, the generalized entropy method can be formulated as minimizing

$$
\sum_{i \in \mathcal{A}} c_{i} G\left(\omega_{i}\right)
$$

subject to (9.19) and

$$
\sum_{i \in \mathcal{A}} \omega_{i} g\left(d_{i}\right) c_{i}=\sum_{i=1}^{N} g\left(d_{i}\right) c_{i}
$$

where $g(\omega)=d G(\omega) / d \omega$. Constraint (9.40) plays the role of achieving the ADU condition of the resulting calibration estimator and it is also called the debiasing constraint under model hetergeneity (Kwon et al., 2024).

The following theorem presents the $\sqrt{n}$-consistency of the generalized entropy calibration estimator.

Theorem 9.5. Let $\hat{\omega}_{i}$ be obtained by minimizing (9.39) subject to (9.19) and (9.40). The resulting calibration estimator $\hat{Y}_{\mathrm{gcal}}=\sum_{i \in \mathcal{A}} \hat{\omega}_{i} y_{i}$ satisfies

$$
\hat{Y}_{\mathrm{gcal}}=\hat{Y}_{\mathrm{greg}, \ell}+o_{p}\left(n^{-1 / 2} N\right)
$$

where

$$
\hat{Y}_{\mathrm{greg}, \ell}=\sum_{i \in \mathcal{U}} \boldsymbol{z}_{i}^{\prime} \boldsymbol{\gamma}^{*}+\sum_{i \in \mathcal{A}} \frac{1}{\pi_{i}}\left(y_{i}-\boldsymbol{z}_{i}^{\prime} \boldsymbol{\gamma}^{*}\right)
$$

$\boldsymbol{z}_{i}^{\prime}=\left(\boldsymbol{x}_{i}^{\prime}, g\left(d_{i}\right) c_{i}\right)$ and $\boldsymbol{\gamma}^{*}$ is the probability limit of $\hat{\boldsymbol{\gamma}}$ given by

$$
\hat{\boldsymbol{\gamma}}=\left(\sum_{i \in \mathcal{A}} \frac{1}{g^{\prime}\left(d_{i}\right) c_{i}} \boldsymbol{z}_{i} \boldsymbol{z}_{i}^{\prime}\right)^{-1} \sum_{i \in \mathcal{A}} \frac{1}{g^{\prime}\left(d_{i}\right) c_{i}} \boldsymbol{z}_{i} y_{i}
$$

Proof. The proof is very similar to that of Theorem 9.1. Using Lagrange multiplier method, the optimization problem can be expressed as maximizing

$$
Q_{2}(\boldsymbol{\omega}, \boldsymbol{\lambda})=-\sum_{i \in \mathcal{A}} G\left(\omega_{i}\right) c_{i}+\boldsymbol{\lambda}^{\prime}\left(\sum_{i \in \mathcal{A}} \omega_{i} \boldsymbol{z}_{i}-\sum_{i=1}^{N} \boldsymbol{z}_{i}\right)
$$

Since

$$
\frac{\partial}{\partial \omega_{i}} Q_{2}=-g\left(\omega_{i}\right) c_{i}+\boldsymbol{\lambda}^{\prime} \boldsymbol{z}_{i}
$$




---

the maximizer can be expressed as

$$
\omega_{i}^{\star}(\boldsymbol{\lambda})=g^{-1}\left(\lambda_{1}^{\prime} \mathbf{x}_{i} / c_{i}+\lambda_{2} g_{i}\right)
$$

where $g_{i}=g\left(d_{i}\right)$.
Now, we can express

$$
\hat{Y}_{\mathrm{gcal}}=\hat{Y}_{\mathrm{gcal}}(\hat{\boldsymbol{\lambda}})=\sum_{i=1}^{N} I_{i} \omega_{i}^{\star}(\hat{\boldsymbol{\lambda}}) y_{i}
$$

where $\hat{\boldsymbol{\lambda}}$ satisfies (9.19), we can express

$$
\begin{aligned}
\hat{Y}_{\text {gcal }} & =\sum_{i=1}^{N} I_{i} \omega_{i}^{\star}(\hat{\boldsymbol{\lambda}}) y_{i}+\underbrace{\left(\sum_{i=1}^{N} \mathbf{x}_{i}-\sum_{i=1}^{N} I_{i} \omega_{i}^{\star}(\hat{\boldsymbol{\lambda}}) \mathbf{x}_{i}\right)^{\prime}}_{=0} \boldsymbol{\gamma} \\
& :=\hat{Y}_{\ell}(\hat{\boldsymbol{\lambda}}, \boldsymbol{\gamma})
\end{aligned}
$$

Let $\boldsymbol{\lambda}^{*}$ be the probability limit of $\hat{\boldsymbol{\lambda}}$. Since $\hat{\boldsymbol{\lambda}}$ satisfies $(9.19), \boldsymbol{\lambda}^{*}$ should satisfy

$$
\underbrace{\mathrm{E}\left\{\sum_{i=1}^{N} I_{i} \omega_{i}^{\star}\left(\boldsymbol{\lambda}^{*}\right) \mathbf{z}_{i} \mid \mathcal{F}_{N}\right\}}_{=\sum_{i=1}^{N} \pi_{i} \omega_{i}^{\star}\left(\boldsymbol{\lambda}^{*}\right) \mathbf{z}_{i}}=\sum_{i=1}^{N} \mathbf{z}_{i}
$$

which implies that

$$
\omega_{i}^{\star}\left(\boldsymbol{\lambda}^{*}\right)=\pi_{i}^{-1}=d_{i}
$$

or

$$
g^{-1}\left(\mathbf{x}_{i}^{\prime} \boldsymbol{\lambda}_{1}^{*} / c_{i}+g\left(d_{i}\right) \lambda_{2}^{*}\right)=d_{i}
$$

Since $g(\cdot)$ is one-to-one, we get $\boldsymbol{\lambda}_{1}^{*}=\mathbf{0}$ and $\lambda_{2}^{*}=1$.
Now, to obtain the linearization similar to we wish to find $\boldsymbol{\gamma}^{*}$ such that (9.24) holds at $\boldsymbol{\gamma}=\boldsymbol{\gamma}^{*}$. Now, since

$$
\frac{\partial}{\partial \boldsymbol{\lambda}} \hat{Y}_{\ell}\left(\boldsymbol{\lambda}^{*}, \boldsymbol{\gamma}\right)=\sum_{i=1}^{N} I_{i} \frac{1}{g^{\prime}\left\{g^{-1}\left(\mathbf{z}_{i}^{\prime} \boldsymbol{\lambda}^{*} / c_{i}\right)\right\}}\left(y_{i}-\mathbf{z}_{i}^{\prime} \boldsymbol{\gamma}\right) \mathbf{z}_{i} / c_{i}
$$

we obtain

$$
\boldsymbol{\gamma}^{*}=\left(\sum_{i=1}^{N} \frac{\pi_{i}}{g^{\prime}\left(d_{i}\right) c_{i}} \mathbf{z}_{i} \mathbf{z}_{i}^{\prime}\right)^{-1} \sum_{i=1}^{N} \frac{\pi_{i}}{g^{\prime}\left(d_{i}\right) c_{i}} \mathbf{z}_{i} y_{i}
$$

Therefore, we obtain (9.42).




---

Note that Theorem 9.5 does not use the superpopulation model in (9.2)(9.3) as an assumption. If the GREG superpopulation model is indeed correct, then we obtain $\boldsymbol{\gamma}^{*}=\left(\boldsymbol{\beta}^{\prime}, 0\right)^{\prime}$ and

$$
\hat{Y}_{\text {greg }, \ell}=\sum_{i=1}^{N} \boldsymbol{x}_{i}^{\prime} \boldsymbol{\beta}+\sum_{i \in \mathcal{A}} \frac{1}{\pi_{i}}\left(y_{i}-\boldsymbol{x}_{i}^{\prime} \boldsymbol{\beta}\right)+o_{p}\left(n^{-1 / 2} N\right)
$$

which achieves the Godambe-Joshi lower bound of the anticipate variance (Godambe and Joshi, 1965).

If the superpopulation model is incorrect, Theorem 9.5 is still applicable and the asymptotic variance of $\hat{Y}_{\text {gcal }}$ is equal to

$$
\mathbb{V}\left(\hat{Y}_{\text {greg }, \ell}\right)=\mathbb{V}\left(\sum_{i=1}^{N} y_{i}\right)+\mathbb{E}\left\{\sum_{i=1}^{N}\left(\pi_{i}^{-1}-1\right)\left(y_{i}-\boldsymbol{z}_{i}^{\prime} \boldsymbol{\gamma}^{*}\right)^{2}\right\}
$$

On the other hand, by Theorem 9.1, the classical calibration estimator $\hat{\theta}_{\mathrm{DS}}$ of Deville and Särndal (1992), ignoring the smaller order terms, satisfies

$$
\mathbb{V}\left(\hat{Y}_{\mathrm{DS}}\right)=\mathbb{V}\left(\sum_{i=1}^{N} y_{i}\right)+\mathbb{E}\left\{\sum_{i=1}^{N}\left(\pi_{i}^{-1}-1\right)\left(y_{i}-\boldsymbol{x}_{i}^{\prime} \mathbf{B}\right)^{2}\right\}
$$

where $\boldsymbol{\beta}^{*}$ is the probability limit of $\hat{\boldsymbol{\beta}}_{\text {GLS }}$ where

$$
\hat{\boldsymbol{\beta}}_{\mathrm{GLS}}=\left(\sum_{i \in \mathcal{A}} d_{i} \boldsymbol{x}_{i} \boldsymbol{x}_{i}^{\prime} / c_{i}\right)^{-1} \sum_{i \in \mathcal{A}} d_{i} \boldsymbol{x}_{i} y_{i} / c_{i}
$$

Comparing (9.43) with (9.44), the additional covariate $g_{i} c_{i}$ in $\boldsymbol{z}_{i}$ can improve the prediction power for $y_{i}$. Thus, the proposed calibration estimator is more efficient than the classical calibration estimator when the superpopulation model is incorrect.




---

# 10 

## Variance Estimation

### 10.1 Introduction

Variance estimation is an important practical problem in survey sampling. Variance estimates are used for two purposes. One is an analytic purpose, such as constructing confidence intervals or performing hypothesis tests. The other is descriptive purposed to evaluate the efficiency of survey designs or estimates for planning surveys.

Desirable variance estimates should satisfy the following properties:

- It should be unbiased, or approximately unbiased.
- The variance estimator should be small. That is, the variance estimator is stable.
- It should not take negative values.
- The computation should be simple.

The HT variance estimator is unbiased, but it can take negative values. In addition, computing the joint inclusion probabilities $\pi_{i j}$ can be cumbersome when the sample size is large.

Example 10.1. Consider a finite population of size $N=3$ with $y_{1}=16, y_{2}=$ 21 and $y_{3}=18$ and consider the following sampling design.

TABLE 10.1
A sampling design for Example 10.1

| Sample $(\mathcal{A})$ | $P(\mathcal{A})$ | HT estimator | HT variance estimator |
| :--- | :---: | :---: | :---: |
| $\mathcal{A}_{1}=\{1,2\}$ | 0.4 | 50 | 206 |
| $\mathcal{A}_{2}=\{1,3\}$ | 0.3 | 50 | 200 |
| $\mathcal{A}_{3}=\{2,3\}$ | 0.2 | 60 | -90 |
| $\mathcal{A}_{4}=\{1,2,3\}$ | 0.1 | 80 | -394 |

The sampling variance of the HT estimator is 85 . Note that the HT variance estimator has expectation

$$
206 \times 0.4+200 \times 0.3+(-90) \times 0.2+(-394) \times 0.1=85
$$




---

but it can take negative values in some samples.
The variance estimator under PPS sampling is always nonnegative and can be computed without computing the joint inclusion probability. In practice, the PPS sampling variance estimator is often applied as an alternative variance estimator even for non-replacement sampling. The resulting variance estimator can be written

$$
\hat{V}_{0}=\frac{1}{n(n-1)} \sum_{i \in A}\left(\frac{y_{i}}{p_{i}}-\hat{Y}_{H T}\right)^{2}=\frac{n}{(n-1)} \sum_{i \in A}\left(\frac{y_{i}}{\pi_{i}}-\frac{1}{n} \hat{Y}_{H T}\right)^{2}
$$

where $p_{i}=\pi_{i} / n$. The following theorem expresses the bias of the simplified variance estimator in (10.1) as an estimator of the variance of the HT estimator.

Theorem 10.1. The simplified variance estimator in (10.1) satisfies

$$
\mathrm{E}\left(\hat{V}_{0}\right)-\operatorname{Var}\left(\hat{Y}_{H T}\right)=\frac{n}{n-1}\left\{\operatorname{Var}\left(\hat{Y}_{P P S}\right)-\operatorname{Var}\left(\hat{Y}_{H T}\right)\right\}
$$

where

$$
\operatorname{Var}\left(\hat{Y}_{P P S}\right)=\frac{1}{n} \sum_{i=1}^{N} p_{i}\left(\frac{y_{i}}{p_{i}}-Y\right)^{2}
$$

and $p_{i}=\pi_{i} / n$.
Proof. Note that $\hat{V}_{0}$ satisfies

$$
\begin{aligned}
\mathrm{E}\left(\sum_{k \in A}\left(\frac{y_{k}}{p_{k}}-Y+Y-\hat{Y}_{H T}\right)^{2}\right)= & \mathrm{E}\left(\sum_{k \in A}\left(\frac{y_{k}}{p_{k}}-Y\right)^{2}\right) \\
& +2 \mathrm{E}\left(\sum_{k \in A}\left(\frac{y_{k}}{p_{k}}-Y\right)\left(Y-\hat{Y}_{H T}\right)\right) \\
& +\mathrm{E}\left(\sum_{k \in A}\left(Y-\hat{Y}_{H T}\right)^{2}\right) .
\end{aligned}
$$

The first term is

$$
\mathrm{E}\left(\sum_{k \in A}\left(\frac{y_{k}}{p_{k}}-Y\right)^{2}\right)=\sum_{k=1}^{N}\left(\frac{y_{k}}{p_{k}}-Y\right)^{2} \pi_{k}=n^{2} \operatorname{Var}\left(\hat{Y}_{P P S}\right)
$$

and, using

$$
\sum_{k \in A}\left(\frac{y_{k}}{p_{k}}-Y\right)=n\left(\sum_{k \in A} \frac{y_{k}}{\pi_{k}}-Y\right)=n\left(\hat{Y}_{H T}-Y\right)
$$

the second term equals to $-2 n \operatorname{Var}\left(\hat{Y}_{H T}\right)$ and the last term is equal to $n \operatorname{Var}\left(\hat{Y}_{H T}\right)$, which proves the result.




---

In many cases, the bias term in (10.2) is positive and the simplified variance estimator conservatively estimates the variance. Under SRS, the relative bias of the simplified variance estimator (10.1) is

$$
\frac{\hat{V}_{0}-\operatorname{Var}\left(\hat{Y}_{\mathrm{HT}}\right)}{\operatorname{Var}\left(\hat{Y}_{\mathrm{HT}}\right)}=\frac{n}{N-n}
$$

and the relative bias is negligible when $n / N$ is negligible.
The simplified variance estimator can be directly applicable to multistage sampling designs. Under multistage sampling design, the HT estimator of the total can be written

$$
\hat{Y}_{\mathrm{HT}}=\sum_{i \in A_{I}} \frac{\hat{Y}_{i}}{\pi_{I i}}
$$

where $\hat{Y}_{i}$ is the estimated total for the PSU $i$. The simplified variance estimator is then given by

$$
\hat{V}_{0}=\frac{n}{(n-1)} \sum_{i \in A_{I}}\left(\frac{\hat{Y}_{i}}{\pi_{I i}}-\frac{1}{n} \hat{Y}_{\mathrm{HT}}\right)^{2}
$$

Under stratified multistage cluster sampling, the simplified variance estimator can be written

$$
\hat{V}_{0}=\sum_{h=1}^{H} \frac{n_{h}}{n_{h}-1} \sum_{i=1}^{n_{h}}\left(w_{h i} \hat{Y}_{h i}-\frac{1}{n_{h}} \sum_{j=1}^{n_{h}} w_{h j} \hat{Y}_{h j}\right)^{2}
$$

where $w_{h i}$ is the sampling weight for cluster $i$ in stratum $h$.

# 10.2 Linearization approach to variance estimation 

When the point estimator is a nonlinear estimator, such as a ratio estimator or regression estimator, exact variance estimation for such estimates is very difficult. Instead, we often rely on linearization methods to estimate the sampling variance of such estimators.

Roughly speaking, if $\mathbf{y}$ is a $p$-dimensional vector and when $\overline{\mathbf{y}}_{n}=\overline{\mathbf{Y}}_{N}+$ $O_{p}\left(n^{-1 / 2}\right)$ holds, the Taylor linearization of $g\left(\overline{\mathbf{y}}_{n}\right)$ can be written as

$$
g\left(\overline{\mathbf{y}}_{n}\right)=g(\overline{\mathbf{Y}})+\sum_{j=1}^{p} \frac{\partial g(\overline{\mathbf{Y}})}{\partial \bar{y}_{j}}\left(\bar{y}_{j}-\bar{Y}_{j}\right)+O_{p}\left(n^{-1}\right)
$$




---

Thus, the variance of the linearized term of $g\left(\bar{y}_{n}\right)$ can be written

$$
\mathcal{V}\left\{g\left(\bar{y}_{n}\right)\right\} \doteq \sum_{i=1}^{p} \sum_{j=1}^{p} \frac{\partial g(\bar{Y})}{\partial y_{i}} \frac{\partial g(\bar{Y})}{\partial y_{j}} \operatorname{Cov}\left\{\bar{y}_{i}, \bar{y}_{j}\right\}
$$

and is estimated by

$$
\hat{\mathcal{V}}\left\{g\left(\bar{y}_{n}\right)\right\} \doteq \sum_{i=1}^{p} \sum_{j=1}^{p} \frac{\partial g\left(\bar{y}_{n}\right)}{\partial y_{i}} \frac{\partial g\left(\bar{y}_{n}\right)}{\partial y_{j}} \hat{\mathcal{C}}\left\{\bar{y}_{i}, \bar{y}_{j}\right\}
$$

In summary, the linearization method for variance estimation can be described as follows:

1. Apply Taylor linearization and ignore the remainder terms.
2. Calculate the variance and covariance terms for each component of $\bar{y}_{n}$ using the standard variance estimation formula.
3. Estimate the partial derivative terms $(\partial g / \partial y)$ from the sample observation.

Example 10.2. If the parameter of interest is $R=\bar{Y} / \bar{X}$ and we use $\hat{R}=$ $\frac{\bar{Y}_{\mathrm{HT}}}{\bar{X}_{\mathrm{HT}}}$ to estimate $R$, we can apply Taylor linearization to get

$$
\hat{R}=R+\bar{X}^{-1}\left(\bar{Y}_{\mathrm{HT}}-R \bar{X}_{\mathrm{HT}}\right)+O_{p}\left(n^{-1}\right)
$$

and the variance estimation formula in (10.5) reduces to

$$
\hat{\mathcal{V}}(\hat{R}) \doteq \bar{X}_{\mathrm{HT}}^{-2} \hat{\mathcal{V}}\left(\bar{Y}_{\mathrm{HT}}\right)+\bar{X}_{\mathrm{HT}}^{-2} \hat{R}^{2} \hat{\mathcal{V}}\left(\bar{X}_{\mathrm{HT}}\right)-2 \bar{X}_{\mathrm{HT}}^{-2} \hat{R} \widehat{\operatorname{Cov}}\left(\bar{X}_{\mathrm{HT}}, \bar{Y}_{\mathrm{HT}}\right)
$$

If the variances and covariances of $\bar{X}_{\mathrm{HT}}$ and $\bar{Y}_{\mathrm{HT}}$ are estimated by HT variance estimation formula, (10.6) can be estimated by

$$
\hat{\mathcal{V}}(\hat{R}) \doteq \frac{1}{\hat{X}_{\mathrm{HT}}^{2}} \sum_{i \in \mathcal{A}} \sum_{j \in \mathcal{A}} \frac{\pi_{i j}-\pi_{i} \pi_{j}}{\pi_{i j}} \frac{e_{i}}{\pi_{i}} \frac{e_{j}}{\pi_{j}}
$$

where $e_{i}=y_{i}-\hat{R} x_{i}$.
Using the result in Example 10.2, the variance of the ratio estimator $\hat{Y}_{R}=$ $X \hat{R}$ is estimated by

$$
\hat{\mathcal{V}}\left(\hat{Y}_{R}\right) \doteq\left(\frac{X}{\hat{X}_{\mathrm{HT}}}\right)^{2} \sum_{i \in \mathcal{A}} \sum_{j \in \mathcal{A}} \frac{\pi_{i j}-\pi_{i} \pi_{j}}{\pi_{i j}} \frac{e_{i}}{\pi_{i}} \frac{e_{j}}{\pi_{j}}
$$




---

which is obtained by multiplying $\hat{X}_{\mathrm{HT}}^{-2} X^{2}$ to the variance formula in (8.13). The variance estimator in (10.7) is asymptotically equivalent to the linearization variance estimator in (8.13), but it gives a more adequate measure of the conditional variance of the ratio estimator, as advocated by Royall and Cumberland (1981). More generally, Särndal et al. (1989) proposed using

$$
\hat{V}\left(\hat{Y}_{\mathrm{GREG}}\right)=\sum_{i \in \mathcal{A}} \sum_{j \in \mathcal{A}} \frac{\pi_{i j}-\pi_{i} \pi_{j}}{\pi_{i j}} \frac{g_{i} e_{i}}{\pi_{i}} \frac{g_{j} e_{j}}{\pi_{j}}
$$

as the conditional variance estimator of the GREG estimator of the form $\hat{Y}_{\text {GREG }}=\sum_{i \in \mathcal{A}} \pi_{i}^{-1} g_{i} y_{i}$, where

$$
g_{i}=X^{\prime}\left(\sum_{i \in \mathcal{A}} \frac{1}{\pi_{i} c_{i}} x_{i} x_{i}^{\prime}\right)^{-1} \frac{1}{c_{i}} x_{i}
$$

and

$$
e_{i}=y_{i}-x_{i}^{\prime}\left(\sum_{i \in \mathcal{A}} \frac{1}{\pi_{i} c_{i}} x_{i} x_{i}^{\prime}\right)^{-1} \sum_{i \in \mathcal{A}} \frac{1}{\pi_{i} c_{i}} x_{i} y_{i}
$$

The $g_{i}$ in (10.9) is the factor to applied to the design weight to satisfy the calibration constraint.

Example 10.3. We now consider the estimation of the variance of the poststratification estimator in (8.27). To estimate the variance, the unconditional variance estimator is given by

$$
\hat{V}_{\mathrm{u}}=\frac{N^{2}}{n}\left(1-\frac{n}{N}\right) \sum_{g=1}^{G} \frac{n_{g}-1}{n-1} s_{g}^{2}
$$

where $s_{g}^{2}=\left(n_{g}-1\right)^{-1} \sum_{i \in \mathcal{A}_{g}}\left(y_{i}-\bar{y}_{g}\right)^{2}$. On the other hand, the conditional variance estimator in (10.8) is given by

$$
\hat{V}_{\mathrm{c}}=\left(1-\frac{n}{N}\right) \frac{n}{n-1} \sum_{g=1}^{G} \frac{N_{g}^{2}}{n_{g}} \frac{n_{g}-1}{n_{g}} s_{g}^{2}
$$

Note that the conditional variance formula in (10.11) is very similar to the variance estimation formula under stratified sampling.

# 10.3 Replication approach to variance estimation 

We now consider an alternative approach to variance estimation that is based on several replicates of the original sample estimator. Such a replication approach does not use Taylor linearization, but instead generates several




---

resamples and computes a replicate to each resample. Variability between replicates is used to estimate the sampling variance of the point estimator. Such a replication approach often uses repeated computation of the replicates using a computer. Replication methods include the random group method, jackknife, balanced repeated replication, and the bootstrap method. More details of the replication methods can be found in Wolter (2007).

# 10.3.1 Random group method 

The random group method was first used in jute acreage surveys in Bengal (Mahalanobis; 1939). The random group method is useful in understanding the basic idea for the replication approach to variance estimation. In the random group method, $G$ random groups are constructed from the sample, and the point estimate is calculated for each random group sample and then combined to obtain the final point estimate. Once the final point estimate is constructed, its variance estimate is calculated using the variability of the $G$ random group estimates. There are two versions of the random group method. One is independent random group method and the other is non-independent random group method. We first consider the independent random group method.

The independent random group method can be described as follows.
[Step 1] Using the given sampling design, select the first random group sample, denoted by $A_{(1)}$, and compute $\hat{\theta}_{(1)}$, an unbiased estimator of $\theta$ from the first random group sample.
[Step 2] Using the same sampling design, select the second random group sample, independently from the first random group sample, and compute $\hat{\theta}_{(2)}$ from the second random group sample.
[Step 3] Using the same procedure, obtain $G$ independent estimate $\hat{\theta}_{(1), \cdots}, \hat{\theta}_{(G)}$ from the $G$ random group sample.
[Step 4] The final estimator of $\theta$ is

$$
\hat{\theta}_{\mathrm{RG}}=\frac{1}{G} \sum_{k=1}^{G} \hat{\theta}_{(k)}
$$

and its unbiased variance estimator is

$$
\hat{V}\left(\hat{\theta}_{\mathrm{RG}}\right)=\frac{1}{G} \frac{1}{G-1} \sum_{k=1}^{G}\left(\hat{\theta}_{(k)}-\hat{\theta}_{\mathrm{RG}}\right)^{2}
$$

Since $\hat{\theta}_{(1), \cdots}, \hat{\theta}_{(G)}$ are independently and identically distributed, the variance estimator in (10.13) is unbiased for the variance of $\hat{\theta}_{\mathrm{RG}}$ in (10.12). Such independent random group method is very easy to understand and is applicable for complicated sampling designs for selecting $A_{(g)}$, but the sample allows




---

for duplication of sample elements and the variance estimator may be unstable when $G$ is small.

We now consider non-independent random group method, which does not allow for duplication of the sample elements. In the non-independent random group method, the sample is partitioned into $G$ groups, exhaustive and mutually exclusive, denoted by $A=\cup_{g=1}^{G} A(g)$ and then apply the sample estimation method for independent random group method, by treating the nonindependent random group samples as if they are independent. The following theorem expresses the bias of the variance estimator for this case.

Theorem 10.2. Let $\hat{\theta}(g)$ be an unbiased estimator of $\theta$, calculated from the $g$ th random group sample $A(g)$ for $g=1, \cdots, G$. Then the random group variance estimator (10.13) satisfies

$$
\mathrm{E}\left\{\hat{V}\left(\hat{\theta}_{\mathrm{RG}}\right)\right\}-\mathrm{V}\left(\hat{\theta}_{\mathrm{RG}}\right)=-\frac{1}{G(G-1)} \sum_{i \neq j} \operatorname{Cov}\left(\hat{\theta}(i), \hat{\theta}(j)\right)
$$

Proof. By (10.12), we have

$$
\mathrm{V}\left(\hat{\theta}_{\mathrm{RG}}\right)=\frac{1}{G^{2}}\left\{\sum_{i=1}^{G} \mathrm{~V}(\hat{\theta}(i))+\sum_{i \neq j} \operatorname{Cov}(\hat{\theta}(i), \hat{\theta}(j))\right\}
$$

and, since

$$
\sum_{i=1}^{G}\left(\hat{\theta}(i)-\hat{\theta}_{\mathrm{RG}}\right)^{2}=\sum_{i=1}^{G}(\hat{\theta}(i)-\theta)^{2}-G\left(\hat{\theta}_{\mathrm{RG}}-\theta\right)^{2}
$$

and using $\mathrm{E}(\hat{\theta}(i))=\theta$,

$$
\begin{aligned}
& \mathrm{E}\left\{\sum_{i=1}^{G}\left(\hat{\theta}(i)-\hat{\theta}_{\mathrm{RG}}\right)^{2}\right\}=\sum_{i=1}^{G} \mathrm{~V}(\hat{\theta}(i))-G \times \mathrm{V}\left(\hat{\theta}_{\mathrm{RG}}\right) \\
= & \left(1-G^{-1}\right) \sum_{i=1}^{G} \mathrm{~V}(\hat{\theta}(i))-G^{-1} \sum_{i \neq j} \operatorname{Cov}(\hat{\theta}(i), \hat{\theta}(j))
\end{aligned}
$$

which implies

$$
\mathrm{E}\left\{\hat{V}\left(\hat{\theta}_{\mathrm{RG}}\right)\right\}=G^{-2} \sum_{i=1}^{G} \mathrm{~V}(\hat{\theta}(i))-G^{-2}(G-1)^{-1} \sum_{i \neq j} \operatorname{Cov}(\hat{\theta}(i), \hat{\theta}(j))
$$

Thus, using (10.15), we have (10.14).
The right side of (10.14) is the bias of $\hat{V}\left(\hat{\theta}_{\mathrm{RG}}\right)$ as an estimator for the variance of $\hat{\theta}_{\mathrm{RG}}$. Such bias becomes zero if the sampling for random groups is a with-replacement sampling. For without-replacement sampling, the covariance




---

between the two different replicates is negative, and so the bias term becomes positive. The relative amount of bias is often negligible. The following example computes the amount of the relative bias.

Example 10.4. Consider a sample of size $n$ obtained from simple random sampling of a finite population of size $N$. Let $b=n / G$ be an integer value that is the size of $A(g)$ such that $A=\cup_{g=1}^{G} A(g)$. The sample mean of $y$ obtained from $A(g)$ is denoted by $\bar{y}(g)$ and the overall mean of $y$ is given by

$$
\hat{\theta}=\frac{1}{G} \sum_{g=1}^{G} \bar{y}(g)
$$

In this case, $\bar{y}(1), \cdots, \bar{y}(G)$ are not independently distributed but are identically distributed with the same mean. By (10.15), we have

$$
\operatorname{Var}(\hat{\theta})=\frac{1}{G} V(\bar{y}(1))+\left(1-\frac{1}{G}\right) \operatorname{Cov}(\bar{y}(1), \bar{y}(2))
$$

and since

$$
V(\bar{y}(1))=\left(\frac{1}{b}-\frac{1}{N}\right) S^{2}
$$

we have

$$
\operatorname{Cov}(\bar{y}(1), \bar{y}(2))=\frac{-1}{N} S^{2}
$$

Thus, the bias in (10.14) reduces to

$$
\begin{aligned}
\operatorname{Bias}\left\{\hat{V}\left(\hat{\theta}_{R G}\right)\right\} & =-\operatorname{Cov}(\bar{y}(1), \bar{y}(2)) \\
& =\frac{1}{N} S^{2}
\end{aligned}
$$

which is often negligible. Therefore, the random group variance estimator (10.13) can be safely used to estimate the variance of $\bar{y}_{n}$ in simple random sampling.

The random group method provides a useful computational tool for estimating the variance of point estimators. However, the random group method is applicable only when the sampling design for $A(g)$ has the same structure as the original sample $A$. The partition $A=\cup_{g=1}^{G} A(g)$ that leads to the unbiasedness of $\hat{\theta}(g)$ is not always possible for complex sampling designs.

# 10.4 Jackknife method 

Jackknife was first introduced by Quenouille (1956) to reduce the bias of the ratio estimator and then was suggested by Tukey (1958) to be used for




---

variance estimation. Jackknife is very popular in practice as a tool for variance estimation.

To introduce the idea of Quenouille (1956), suppose that $n$ independent observations of $\left(x_{i}, y_{i}\right)$ are available that are generated from a distribution with mean $\left(\mu_{x}, \mu_{y}\right)$. If the parameter of interest is $\theta=\mu_{y} / \mu_{x}$, then the sample ratio $\hat{\theta}=\bar{x}^{-1} \bar{y}$ has a bias of order $O\left(n^{-1}\right)$. That is, we have

$$
\mathrm{E}(\hat{\theta})=\theta+\frac{C}{n}+O\left(n^{-2}\right)
$$

If we delete the $k$-th observation and recompute the ratio

$$
\hat{\theta}_{(-k)}=\left(\sum_{i \neq k} x_{i}\right)^{-1} \sum_{i \neq k} y_{i}
$$

we obtain

$$
\mathrm{E}\left(\hat{\theta}_{(-k)}\right)=\theta+\frac{C}{n-1}+O\left(n^{-2}\right)
$$

Thus, the jackknife pseudo value defined by $\hat{\theta}_{(k)}=n \hat{\theta}-(n-1) \hat{\theta}_{(-k)}$ can be used to compute

$$
\hat{\theta}_{(.)}=\frac{1}{n} \sum_{k=1}^{n} \hat{\theta}_{(k)}
$$

which has bias of order $O\left(n^{-2}\right)$. Thus, the jackknife can be used to reduce the bias of nonlinear estimators.

Note that if $\hat{\theta}=\bar{y}$ then $\hat{\theta}_{(k)}=y_{k}$. Tukey (1958) suggested using $\hat{\theta}_{(k)}$ as an approximate IID observation to obtain the following jackknife variance estimator.

$$
\hat{V}_{\mathrm{JK}}(\hat{\theta}) \doteq \frac{1}{n} \frac{1}{n-1} \sum_{k=1}^{n}\left(\hat{\theta}_{(k)}-\bar{\theta}_{(.)}\right)^{2}=\frac{n-1}{n} \sum_{k=1}^{n}\left(\hat{\theta}_{(-k)}-\bar{\theta}_{(.)}\right)^{2}
$$

For the special case of $\hat{\theta}_{n}=\bar{y}$, we obtain

$$
\hat{V}_{\mathrm{JK}}=\frac{1}{n} \frac{1}{n-1} \sum_{i=1}^{n}\left(y_{i}-\bar{y}\right)^{2}=\frac{1}{n} s_{y}^{2}
$$

and the jackknife variance estimator is algebraically equivalent to the usual variance estimator of the sample mean under simple random sampling ignoring the finite population correction term.




---

If we are interested in estimating the variance of $\hat{\theta}=f(\bar{x}, \bar{y})$, using $\hat{\theta}_{(-k)}=$ $f\left(\bar{x}_{(-k)}, \bar{y}_{(-k)}\right)$, we can construct

$$
\hat{V}_{\mathrm{JK}}(\hat{\theta})=\frac{n-1}{n} \sum_{k=1}^{n}\left(\hat{\theta}_{(-k)}-\hat{\theta}\right)^{2}
$$

as the jackknife variance estimator of $\hat{\theta}$. The jackknife replicate $\hat{\theta}_{(-k)}$ is computed by using the same formula for $\hat{\theta}$ using the jackknife weight $w_{i}^{(k)}$ instead of the original weight $w_{i}=1 / n$, where

$$
w_{i}^{(-k)}= \begin{cases}(n-1)^{-1} & \text { if } i \neq k \\ 0 & \text { if } i=k\end{cases}
$$

To discuss the asymptotic property of the jackknife variance estimator in (10.17), we use the following Taylor expansion, which is often called secondtype Taylor expansion.

Lemma 10.1. Let $\left\{X_{n}, W_{n}\right\}$ be a sequence of random variables such that

$$
X_{n}=W_{n}+O_{p}\left(r_{n}\right)
$$

where $r_{n} \rightarrow 0$ as $n \rightarrow \infty$. If $g(x)$ is a function with $s$-th continuous derivatives in the line segment joining $X_{n}$ and $W_{n}$ and the $s$-th order partial derivatives are bounded, then

$$
g\left(X_{n}\right)=g\left(W_{n}\right)+\sum_{k=1}^{s-1} \frac{1}{k!} g^{(k)}\left(W_{n}\right)\left(X_{n}-W_{n}\right)^{k}+O_{p}\left(r_{n}^{s}\right)
$$

where $g^{(k)}(a)$ is the $k$-th derivative of $g(x)$ evaluated at $x=a$.
Now, since $\bar{y}_{(-k)}-\bar{y}=(n-1)^{-1}\left(\bar{y}-y_{k}\right)$, we have

$$
\bar{y}_{(-k)}-\bar{y}=O_{p}\left(n^{-1}\right)
$$

For the case of $\hat{\theta}=f(\bar{x}, \bar{y})$, we can apply the above lemma to get

$$
\hat{\theta}_{(-k)}-\hat{\theta}=\frac{\partial f}{\partial x}(\bar{x}, \bar{y})\left(\bar{x}_{(-k)}-\bar{x}\right)+\frac{\partial f}{\partial y}(\bar{x}, \bar{y})\left(\bar{y}_{(-k)}-\bar{y}\right)+o_{p}\left(n^{-1}\right)
$$

so that

$$
\begin{aligned}
& \frac{n-1}{n} \sum_{k=1}^{n}\left(\hat{\theta}_{(-k)}-\hat{\theta}\right)^{2} \\
& =\left\{\frac{\partial f}{\partial x}(\bar{x}, \bar{y})\right\}^{2} \frac{n-1}{n} \sum_{k=1}^{n}\left(\bar{x}_{(-k)}-\bar{x}\right)^{2} \\
& +\left\{\frac{\partial f}{\partial y}(\bar{x}, \bar{y})\right\}^{2} \frac{n-1}{n} \sum_{k=1}^{n}\left(\bar{y}_{(-k)}-\bar{y}\right)^{2} \\
& +2\left\{\frac{\partial f}{\partial x}(\bar{x}, \bar{y})\right\}\left\{\frac{\partial f}{\partial y}(\bar{x}, \bar{y})\right\} \frac{n-1}{n} \sum_{k=1}^{n}\left(\bar{x}_{(-k)}-\bar{x}\right)\left(\bar{y}_{(-k)}-\bar{y}\right)+o_{p}\left(n^{-1}\right)
\end{aligned}
$$




---

Thus, the jackknife variance estimator is asymptotically equivalent to the linearized variance estimator. That is, the second-type Taylor linearization leads to

$$
\begin{aligned}
\hat{V}_{\mathrm{JK}}(\hat{\theta})= & \left\{\frac{\partial f}{\partial x}(\bar{x}, \bar{y})\right\}^{2} \hat{V}(\bar{x})+\left\{\frac{\partial f}{\partial y}(\bar{x}, \bar{y})\right\}^{2} \hat{V}(\bar{y}) \\
& +2\left\{\frac{\partial f}{\partial x}(\bar{x}, \bar{y})\right\}\left\{\frac{\partial f}{\partial y}(\bar{x}, \bar{y})\right\} \hat{C}(\bar{x}, \bar{y})+o_{p}\left(n^{-1}\right)
\end{aligned}
$$

The above jackknife method is constructed under simple random sampling. For multistage stratified sampling, jackknife replicates can be constructed by removing a cluster for each replicate. Let

$$
\hat{Y}_{\mathrm{HT}}=\sum_{h=1}^{H} \sum_{i=1}^{n_{h}} w_{h i} \hat{Y}_{h i}
$$

be the HT estimator of $Y$ under stratified multistage cluster sampling. The jackknife weights are constructed by deleting a cluster sequentially as

$$
w_{h i}^{(-g j)}= \begin{cases}0 & \text { if } h=g \text { and } i=j \\ \left(n_{h}-1\right)^{-1} n_{h} w_{h i} & \text { if } h=g \text { and } i \neq j \\ w_{h i} & \text { otherwise }\end{cases}
$$

and the jackknife variance estimator is computed by

$$
\hat{V}_{\mathrm{JK}}\left(\hat{Y}_{\mathrm{HT}}\right)=\sum_{h=1}^{H} \frac{n_{h}-1}{n_{h}} \sum_{i=1}^{n_{h}}\left(\hat{Y}_{\mathrm{HT}}^{(-h i)}-\frac{1}{n_{h}} \sum_{j=1}^{n_{h}} \hat{Y}_{\mathrm{HT}}^{(-h j)}\right)^{2}
$$

where

$$
\hat{Y}_{\mathrm{HT}}^{(-g j)}=\sum_{h=1}^{H} \sum_{i=1}^{n_{h}} w_{h i}^{(-g j)} \hat{Y}_{h i}
$$

The following theorem presents the algebraic property of the jackknife variance estimator in (10.18).

Theorem 10.3. The jackknife variance estimator in (10.18) is algebraically equivalent to the simplified variance estimator in (10.4).

If $\hat{\theta}=f\left(\hat{X}_{\mathrm{HT}}, \hat{Y}_{\mathrm{HT}}\right)$ then the jackknife replicates are constructed as $\hat{\theta}^{(-g j)}=f\left(\hat{X}_{\mathrm{HT}}^{(-g j)}, \hat{Y}_{\mathrm{HT}}^{(-g j)}\right)$. In this case, the jackknife variance estimator is computed as

$$
\hat{V}_{\mathrm{JK}}(\hat{\theta})=\sum_{h=1}^{H} \frac{n_{h}-1}{n_{h}} \sum_{i=1}^{n_{h}}\left(\hat{\theta}^{(-h i)}-\frac{1}{n_{h}} \sum_{j=1}^{n_{h}} \hat{\theta}^{(-h j)}\right)^{2}
$$




---

or, more simply,

$$
\hat{V}_{\mathrm{JK}}(\hat{\theta})=\sum_{h=1}^{H} \frac{n_{h}-1}{n_{h}} \sum_{i=1}^{n_{h}}\left(\hat{\theta}_{(-h i)}-\hat{\theta}\right)^{2}
$$

The asymptotic properties of the above jackknife variance estimator under stratified multistage sampling can be established. For references, see Krewski and Rao (1981) or Shao and Tu (1995).

Example 10.5. We now revisit Example 10.3 to estimate the variance of the post-stratification estimator using the jackknife. For simplicity, assume that SRS for the sample. The post-stratification estimator is calculated as

$$
\hat{Y}_{\text {post }}=\sum_{g=1}^{G} N_{g} \bar{y}_{g}
$$

where $\bar{y}_{g}=n_{g}^{-1} \sum_{i \in A_{g}} y_{i}$. Now, the $k$-th replicate of $\hat{Y}_{\text {post }}$ is

$$
\hat{Y}_{\text {post }}^{(-k)}=\sum_{g \neq h} N_{g} \bar{y}_{g}+N_{h} \bar{y}_{h}^{(-k)}
$$

where $\bar{y}_{h}^{(-k)}=\left(n_{h}-1\right)^{-1}\left(n_{h} \bar{y}_{h}-y_{k}\right)$. Thus,

$$
\begin{aligned}
\hat{Y}_{\text {post }}^{(-k)}-\hat{Y}_{\text {post }} & =N_{h}\left(\bar{y}_{h}^{(-k)}-\bar{y}_{h}\right) \\
& =N_{h}\left(n_{h}-1\right)^{-1}\left(\bar{y}_{h}-y_{k}\right)
\end{aligned}
$$

and

$$
\begin{aligned}
\hat{V}_{\mathrm{JK}}\left(\hat{Y}_{\text {post }}\right) & =\frac{n-1}{n} \sum_{k=1}^{n}\left(\hat{Y}_{\text {post }}^{(-k)}-\hat{Y}_{\text {post }}\right)^{2} \\
& =\frac{n-1}{n} \sum_{g=1}^{G} N_{g}^{2}\left(n_{g}-1\right)^{-1} s_{g}^{2}
\end{aligned}
$$

which, ignoring $n / N$ term, is asymptotically equivalent to the conditional variance estimator in (10.11).




---

# Two-phase sampling 

### 11.1 Introduction

The two-phase sampling design is a sampling design where sample selection is performed in two phases. I the first phase, the auxiliary variable $x$ is observed, and in the second phase, the study variable $y$ is observed. The second phase sample is a subset of the first phase sample.

Two-phase sampling is particularly attractive when the cost of observing $x$ is relatively low compared to the cost of observing $y$. To formalize the concept, two-phase sampling can be described as follows:
[Step 1] From the finite population, s a first-phase sample $A_{1}$ of size $n_{1}$ is selected, and the auxiliary variable $x$ is observed.
[Step 2] The first-phase sample $A_{1}$ is treated as a finite population, and a second-phase sample $A_{2}$ of size $n_{2}$ is selected from it. Study variable $y$ is observed in the second-phase sample. The probability of selection for the second phase sample is often determined by the values of $x$ obtained from the first-phase sample.

Since the second-phase sample selection probability depends on the observed values of the first-phase sample, the sample inclusion probability for the second-phase sample is a random variable that changes as the first-phase sample changes. In this case, the standard Horvitz-Thompson (HT) estimation theory is not directly applicable.

To discuss this further, note that the overall first-order inclusion probability for the two-phase sampling design is

$$
\pi_{i}=\operatorname{Pr}\left(i \in A_{2}\right)=\sum_{A_{2} ; i \in A_{2}} P\left(A_{2}\right)
$$

where

$$
P\left(A_{2}\right)=\sum_{A_{1} ; A_{2} \subset A_{1}} P_{2}\left(A_{2} \mid A_{1}\right) P_{1}\left(A_{1}\right)
$$

Here, $P_{1}(\cdot)$ is the sample selection probability for the first-phase sample, and $P_{2}\left(\cdot \mid A_{1}\right)$ is the sample selection probability for the second-phase sample,




---

which is conditional on the first-phase sample. Thus,

$$
\begin{aligned}
\pi_{i} & =\sum_{\left\{A_{2} ; i \in A_{2}\right\}} \sum_{\left\{A_{1} ; A_{2} \subset A_{1}\right\}} P_{2}\left(A_{2} \mid A_{1}\right) P_{1}\left(A_{1}\right) \\
& =\sum_{\left\{A_{1} ; i \in A_{1}\right\}} \sum_{\left\{A_{2} ; A_{2} \subset A_{1} \& i \in A_{2}\right\}} P_{2}\left(A_{2} \mid A_{1}\right) P_{1}\left(A_{1}\right) \\
& =\sum_{\left\{A_{1} ; i \in A_{1}\right\}} \sum_{\left\{A_{2} ; i \in A_{2}\right\}} P_{2}\left(A_{2} \mid A_{1}\right) P_{1}\left(A_{1}\right)
\end{aligned}
$$

If we define the conditional first-order inclusion probability for the secondphase sampling as

$$
\pi_{i \mid A_{1}}^{(2)}=\operatorname{Pr}\left(i \in A_{2} \mid A_{1}\right)
$$

then the first order inclusion probability is

$$
\begin{aligned}
\pi_{i} & =\sum_{A_{1} ; i \in A_{1}} \pi_{i \mid A_{1}}^{(2)} P_{1}\left(A_{1}\right) \\
& =E_{1}\left(\pi_{i \mid A_{1}}^{(2)}\right)
\end{aligned}
$$

where $E_{1}(\cdot)$ is the expectation with respect to the first-phase sampling. Here, the conditional first-order inclusion probability $\pi_{i \mid A_{1}}^{(2)}$ is a random variable in the sense that it is a function of $x$ in the first phase sample $A_{1}$. The conditional expectation (11.1) cannot be computed because we have a single realization of the first-phase sample $A_{1}$.

If the sampling design satisfies the invariance condition, as is the case in two-stage sampling, then the conditional first-order inclusion probability $\pi_{i \mid A_{1}}^{(2)}$ is equal to the unconditional first-order inclusion probability $\pi_{i}^{(2)}$. On this case, by (11.1), we have

$$
\begin{aligned}
\pi_{i} & =\sum_{A_{1} ; i \in A_{1}} P_{1}\left(A_{1}\right) \pi_{i}^{(2)} \\
& =\pi_{i}^{(1)} \pi_{i}^{(2)}
\end{aligned}
$$

In this scenario, where the sampling design satisfies the invariance condition, the Horvitz-Thompson (HT) estimator can be directly implemented.

To discuss unbiased estimation for two-phase sampling, let's first consider the following quantity

$$
\hat{Y}_{1}=\sum_{i \in A_{1}} \frac{y_{i}}{\pi_{i}^{(1)}}
$$

This is an unbiased estimator for the population total of $y$. The task is now to construct an unbiased estimator of $\hat{Y}_{1}$ using the two-phase sample.

Applying the Horvitz-Thompson (HT) estimation idea conditionally, we obtain

$$
\hat{Y}^{*}=\sum_{i \in A_{2}} \frac{y_{i}}{\pi_{i}^{(1)} \pi_{i \mid A_{1}}^{(2)}}
$$




---

If we define $\pi_{i}^{*}=\pi_{i}^{(1)} \pi_{i \mid \mathcal{A}_{1}}^{(2)}$, then (11.2) can be written as $\hat{Y}^{*}=\sum_{i \in \mathcal{A}_{2}} y_{i} / \pi_{i}^{*}$. This conditionally unbiased estimator (11.2) is sometimes called the $\pi^{*}$ estimator.

The $\pi^{*}$-estimator is conditional unbiased to $\hat{Y}_{1}$, which is itself an unbiased estimator of the population total $Y$. Therefore, the $\pi^{*}$ estimator is unbiased unconditionally.

The variance of the $\pi^{*}$-estimator is given by

$$
\begin{aligned}
\mathcal{V}\left(\hat{Y}^{*}\right)= & \mathcal{V}\left\{\mathcal{E}\left(\hat{Y}^{*} \mid \mathcal{A}_{1}\right)\right\}+\mathcal{E}\left\{\mathcal{V}\left(\hat{Y}^{*} \mid \mathcal{A}_{1}\right)\right\} \\
= & \mathcal{V}\left\{\sum_{i \in \mathcal{A}_{1}} \frac{y_{i}}{\pi_{i}^{(1)}}\right\}+\mathcal{E}\left\{\sum_{i \in \mathcal{A}_{1}} \sum_{j \in \mathcal{A}_{1}}\left(\pi_{i j \mid \mathcal{A}_{1}}^{(2)}-\pi_{i \mid \mathcal{A}_{1}}^{(2)} \pi_{j \mid \mathcal{A}_{1}}^{(2)}\right) \frac{y_{i}}{\pi_{i}^{*}} \frac{y_{j}}{\pi_{j}^{*}}\right\}
\end{aligned}
$$

Here, $\pi_{i j \mid \mathcal{A}_{1}}^{(2)}=\operatorname{Pr}\left(i \in \mathcal{A}_{2}, j \in \mathcal{A}_{2} \mid \mathcal{A}_{1}\right)$ is the conditional joint inclusion probability. The variance expression in (11.3) has two parts: the first part is the variance due to the first-phase sampling, and the second part is the variance due to the second-phase sampling.

# 11.2 Two-phase sampling for stratification 

Stratified sampling is one of the most popular sampling methods for improving the efficiency of point estimators. To apply stratified sampling, the stratification variables need to be available for the finite population. If that is not the case, the two-phase sampling approach can be used.

Let $\boldsymbol{x}_{i}=\left(x_{i 1}, \ldots, x_{i H}\right)$ be the vector of stratification variables, where $x_{i h}$ takes the value 1 if unit $i$ belongs to stratum $h$, and 0 otherwise. In this case, the auxiliary variable $\boldsymbol{x}$ is not available in the finite population.

The two-phase sampling for stratification can be described as follows:

1. Perform a simple random sample (SRS) of size $n$ from the finite population and obtain $\sum_{i \in \mathcal{A}_{1}} \boldsymbol{x}_{i}=\left(n_{1}, n_{2}, \ldots, n_{H}\right)$ where $n=\sum_{h=1}^{H} n_{h}$.
2. Among the $n_{h}$ elements in each stratum, select $r_{h}$ elements independently by SRS, where $r_{h}$ is determined after when the first-phase sample is selected.
This two-phase sampling approach allows the stratification variables to be obtained, even when they are not directly available in the finite population. In this two-phase sampling design, the realized sample size $n_{h}$ in stratum $h$ is a random variable, and it follows an approximate multinomial distribution:

$$
\left(n_{1}, n_{2}, \ldots, n_{H}\right) \sim \mathrm{MN}\left(n ; W_{1}, W_{2}, \ldots, W_{H}\right)
$$




---

where $\mathcal{M}_{N}(n ; \mathbf{p})$ denotes the multinomial distribution with parameter $\mathbf{p}$, and $W_{h}=N_{h} / N$ is the population proportion of stratum $h$.

This means that the realized sample sizes across the strata follow a multinomial distribution, with the population stratum proportions $W_{h}$ as the underlying probabilities, and the total sample size $n$ as the number of trials.

In this two-phase sampling, the $\pi^{*}$-estimator of the population mean of $y$ is

$$
\hat{\bar{Y}}_{\mathrm{tp}}=\sum_{h=1}^{H} w_{h} \bar{y}_{h 2}
$$

where $w_{h}=n_{h} / n$ and $\bar{y}_{h 2}=r_{h}^{-1} \sum_{i \in A_{2}} x_{i h} y_{i}$. Since the expectation of $w_{h}=$ $n_{h} / n$ is $W_{h}=N_{h} / N$, the $\pi^{*}$-estimator in (11.4) can be viewed as the stratified sample estimator when the stratum size $W_{h}$ is unknown. The total variance is, by (11.3), obtained as

$$
\mathcal{V}\left(\hat{\bar{Y}}_{\mathrm{tp}}\right)=\left(\frac{1}{n}-\frac{1}{N}\right) S^{2}+\mathcal{E}\left\{\sum_{h=1}^{H}\left(\frac{n_{h}}{n}\right)^{2}\left(\frac{1}{r_{h}}-\frac{1}{n_{h}}\right) s_{h 1}^{2}\right\}
$$

where

$$
s_{h 1}^{2}=\frac{1}{n_{h}-1} \sum_{i \in A_{1}} x_{i h}\left(y_{i}-\bar{y}_{h 1}\right)^{2}
$$

and $\bar{y}_{h 1}=n_{h}^{-1} \sum_{i \in A_{1}} x_{i h} y_{i}$. Also, if we define $\bar{y}_{1}=n^{-1} \sum_{h=1}^{H} n_{h} \bar{y}_{h 1}$ and

$$
s_{1}^{2}=\frac{1}{n-1} \sum_{i \in A_{1}}\left(y_{i}-\bar{y}_{1}\right)^{2}
$$

then we have $\mathcal{E}\left(s_{1}^{2}\right)=S^{2}$ and

$$
s_{1}^{2}=\sum_{h=1}^{H}\left\{\frac{n_{h}}{n-1}\left(\bar{y}_{h 1}-\bar{y}_{1}\right)^{2}+\frac{n_{h}-1}{n-1} s_{h 1}^{2}\right\}
$$

Thus, (11.5) is approximately equal to

$$
\mathcal{V}\left(\hat{\bar{Y}}_{\mathrm{tp}}\right)=\mathcal{E}\left\{n^{-1} \sum_{h=1}^{H} w_{h}\left(\bar{y}_{h 1}-\bar{y}_{1}\right)^{2}+\sum_{h=1}^{H} r_{h}^{-1} w_{h}^{2} s_{h 1}^{2}\right\}
$$

Here, the finite population correction term is ignored. The variance formula in (11.6) is expressed as the sum of two terms. One is a function of the betweenstratum variance, and the other is a function of the within-stratum variance. In computing the between-stratum variance, we used the full sample size $n$. However, in computing the within-stratum variance, we only used the smaller sample size $r_{h}$ within each stratum.




---

Therefore, if the between-stratum variance is larger than the withinstratum variance, the efficiency of the two-phase sampling estimator increases. This is because the between-stratum variance is estimated more precisely using the larger sample size $n$, compared to the within-stratum variance estimated with the smaller sample size $r_{h}$.

In addition, the variance formula in (11.6) provides a way to estimate the variance. Since (11.6) is expressed as an expectation of quantities that can be computed from the first-phase sample, we can use $\bar{y}_{h 2}$ and $s_{h 2}^{2}$ instead of $\bar{y}_{h 1}$ and $s_{h 1}^{2}$, respectively, in (11.6). Thus,

$$
\hat{V}\left(\hat{\bar{Y}}_{\mathrm{tp}}\right)=E\left\{n^{-1} \sum_{h=1}^{H} w_{h}\left(\bar{y}_{h 2}-\hat{\bar{Y}}_{\mathrm{tp}}\right)^{2}+\sum_{h=1}^{H} r_{h}^{-1} w_{h}^{2} s_{h 2}^{2}\right\}
$$

is an approximately unbiased estimator of the variance in (11.6). Rao (1973) developed a formal theory for the two-phase sampling for stratification. Alternatively, instead of (11.7), we can also use the Jackknife method to estimate the variance of the two-phase sampling estimator. See Kim et al. (2006) for more details.

To compare the variance (11.6) of the two-phase sampling estimator with that of the simple random sampling (SRS) estimator of equal sample size $r=\sum_{h=1}^{H} r_{h}$, note that

$$
V\left(\hat{\bar{Y}}_{\mathrm{SRS}}\right)=E\left\{r^{-1} \sum_{h=1}^{H} w_{h}\left(\bar{y}_{h 1}-\bar{y}_{1}\right)^{2}+r^{-1} \sum_{h=1}^{H} w_{h} s_{h 1}^{2}\right\}
$$

Therefore, the difference in variances is

$$
V\left(\hat{\bar{Y}}_{\mathrm{SRS}}\right)-V\left(\hat{\bar{Y}}_{\mathrm{tp}}\right)=E\left\{\left(\frac{1}{r}-\frac{1}{n}\right) \sum_{h=1}^{H} w_{h}\left(\bar{y}_{h 1}-\bar{y}_{1}\right)^{2}+\sum_{h=1}^{H}\left(\frac{1}{r}-\frac{w_{h}}{r_{h}}\right) w_{h} s_{h 1}^{2}\right\}
$$

The first term is always positive, as $r<n$. The second term is zero under proportional allocation $\left(r_{h}=r w_{h}\right)$, but it can be made positive for optimal allocation.

This shows that the two-phase sampling estimator can be more efficient than the SRS estimator, depending on the relative magnitudes of the betweenstratum and within-stratum variances and by choosing the optimal sample-size allocation for the second-phase sampling.

To discuss optimal allocation, first consider the cost function. The total cost can be expressed as

$$
C=c_{1} n+\sum_{h=1}^{H} c_{2 h} r_{h}
$$

and, writing $\nu_{h}=r_{h} / n_{h}$, the optimal allocation can be determined by mini-




---

mizing

$$
V=\frac{1}{n}\left(\left(S^{2}-\sum_{h=1}^{H} W_{h} S_{h}^{2}\right)+\sum_{h=1}^{H} W_{h} S_{h}^{2} \frac{1}{\nu_{h}}\right)
$$

subject to

$$
C=n\left(c_{1}+\sum_{h=1}^{H} c_{2 h} W_{h} \nu_{h}\right)
$$

To find the optimal allocation, we have only to find the set of $\nu_{h}$ 's that minimizes $V \times C$. The optimal solution is

$$
\nu_{h}^{*}=\left(\frac{c_{1}}{c_{2 h}} \times \frac{S_{h}^{2}}{S^{2}-\sum_{h=1}^{H} W_{h} S_{h}^{2}}\right)^{1 / 2}
$$

which lead to

$$
\frac{r_{h}^{*}}{n^{*}}=W_{h} \nu_{h}^{*}=W_{h}\left(\frac{c_{1}}{c_{2 h}}\right)^{1 / 2}\left(\frac{S_{h}^{2}}{S^{2}-\sum_{h=1}^{H} W_{h} S_{h}^{2}}\right)^{1 / 2}
$$

If $c_{2 h}=c_{2}$ and $S_{h}^{2}=S_{w}^{2}$ for all $h$, then

$$
\frac{r^{*}}{n^{*}}=\left(\frac{c_{1}}{c_{2}}\right)^{1 / 2}\left(\frac{1}{\phi-1}\right)^{1 / 2}
$$

where

$$
\phi=\frac{S^{2}}{S_{w}^{2}}
$$

denotes the relative efficiency due to stratification (under proportional allocation). If $c_{2}=10 c_{1}$ and $\phi=2$ then $r / n=\sqrt{0.1}=0.32$.

The two-phase sampling for stratification is also a useful method for estimating parameters of subpopulations defined by specific eligibility criteria. For example, if the population of interest is not the entire population, but a subpopulation with certain attributes, and information on these attributes is not available in the population frame, the two-phase sampling approach can be employed. In the first phase, the information on eligibility can be obtained from the initial sample. This allows the population to be stratified based on the eligibility criteria. Then, in the second phase, a sample is selected from the stratum of eligible groups, and the variable of interest $y$ is observed.

For instance, consider a survey where the target population is households with members over the age of 60 . Since there may not be a household population frame with age group information, the two-phase sampling for stratification can be applied. The first phase would identify the eligible households, and the second phase would sample from this stratum of eligible households to observe the variable of interest.

This approach enables efficient estimation of parameters for subpopulations defined by specific eligibility criteria, even when that information is not directly available in the population frame.




---

# 11.3 Regression estimator for two-phase sampling 

In the previous section, the auxiliary variable $\boldsymbol{x}$ obtained from the firstphase sample was used to design the sampling mechanism for the second-phase sampling. In this section, we consider the case where the auxiliary variable is used in the estimation stage, rather than used in the sampling design.

To illustrate the idea, assume the first-phase sample is a simple random sample of size $n$, and the second-phase sample is also a simple random sample of size $r$ from the first-phase sample. Since we observe $\boldsymbol{x}_{i}$ in the first-phase sample, we can compute:

$$
\overline{\boldsymbol{x}}_{1}=\frac{1}{n} \sum_{i \in A_{1}} \boldsymbol{x}_{i}
$$

from the first-phase sample, and

$$
\left(\overline{\boldsymbol{x}}_{2}, \bar{y}_{2}\right)=\frac{1}{r} \sum_{i \in A_{2}}\left(\boldsymbol{x}_{i}, y_{i}\right)
$$

from the second-phase sample.
The two-phase regression estimator is then computed as

$$
\bar{y}_{\mathrm{reg}, \mathrm{tp}}=\bar{y}_{2}+\left(\overline{\boldsymbol{x}}_{1}-\overline{\boldsymbol{x}}_{2}\right)^{\prime} \hat{\boldsymbol{B}}
$$

where

$$
\hat{\boldsymbol{B}}=\left(\sum_{i \in A_{2}} \boldsymbol{x}_{i} \boldsymbol{x}_{i}^{\prime}\right)^{-1} \sum_{i \in A_{2}} \boldsymbol{x}_{i} y_{i}
$$

This two-phase regression estimator utilizes the auxiliary information $\boldsymbol{x}$ obtained from the first-phase sample to improve the estimation of the population mean $\bar{Y}$.

Now, to discuss its statistical properties, note that $\hat{\boldsymbol{B}}-\boldsymbol{B}=O_{p}\left(r^{-1 / 2}\right)$. Thus, we can express have

$$
\bar{y}_{\mathrm{reg}, \mathrm{tp}}=\bar{y}_{2}+\left(\overline{\boldsymbol{x}}_{1}-\overline{\boldsymbol{x}}_{2}\right)^{\prime} \boldsymbol{B}+O_{p}\left(r^{-1}\right)
$$

and obtain

$$
\mathcal{V}\left(\bar{y}_{\mathrm{reg}, \mathrm{tp}}\right) \doteq \boldsymbol{B}^{\prime} \mathcal{V}\left(\overline{\boldsymbol{x}}_{1}\right) \boldsymbol{B}+\mathcal{V}\left(\bar{e}_{2}\right)
$$

where

$$
\bar{e}_{2}=\frac{1}{r} \sum_{i \in A_{2}}\left(y_{i}-\boldsymbol{x}_{i}^{\prime} \boldsymbol{B}\right)
$$

The variance of $\bar{y}_{\text {reg, tp }}$ is then determined. In (11.12), the total variance consists of two components:

1. The variance explained by the regression on $\overline{\boldsymbol{x}}_{1}$, given by $\boldsymbol{B}^{\prime} \mathcal{V}\left(\overline{\boldsymbol{x}}_{1}\right) \boldsymbol{B}$.



---

Two-phase sampling
2. The variance of the mean of the residuals from the second-phase sample, $V\left(\bar{e}_{2}\right)$.

Therefore, under the SRS under both phases, Under simple random sampling (SRS) in both phases, the specific forms of these variance terms are provided below:

$$
V\left(\bar{y}_{\mathrm{reg}, \mathrm{tp}}\right) \doteq\left(\frac{1}{n}-\frac{1}{N}\right) \mathbf{B}^{\prime} \mathbf{S}_{\mathbf{x x}} \mathbf{B}+\left(\frac{1}{r}-\frac{1}{N}\right) S_{\mathrm{ee}}
$$

where

$$
\begin{aligned}
\mathbf{S}_{\mathbf{x x}} & =\frac{1}{N-1} \sum_{i=1}^{N}\left(\mathbf{x}_{i}-\overline{\mathbf{x}}_{N}\right)\left(\mathbf{x}_{i}-\overline{\mathbf{x}}_{N}\right)^{\prime} \\
S_{\mathrm{ee}} & =\frac{1}{N-1} \sum_{i=1}^{N}\left(e_{i}-\bar{e}_{N}\right)^{2}
\end{aligned}
$$

The first term in (11.13) is the variance term explained by $\overline{\mathbf{x}}_{1}$ and the second term in (11.13) is the variance of $\bar{y}_{\text {reg,tp }}$ that is not explained by $\mathbf{x}$.

Note that the efficiency gain due to two-phase sampling can be computed as

$$
V\left(\bar{y}_{2}\right)-V\left(\bar{y}_{\mathrm{reg}, \mathrm{tp}}\right)=\left(\frac{1}{r}-\frac{1}{n}\right) \mathbf{B}^{\prime} \mathbf{S}_{\mathbf{x x}} \mathbf{B}
$$

The gain is larger when the regression relationship is strong (large $\mathbf{B}^{\prime} \mathbf{S}_{\mathbf{x x}} \mathbf{B}$ ) and when the second-phase subsample is much smaller than the first-phase sample (small $r / n$ ).

For variance estimation, we can use (11.13) and estimate each component of the sample separately. That is, we may use

$$
\hat{V}\left(\bar{y}_{\mathrm{reg}, \mathrm{tp}}\right) \doteq\left(\frac{1}{n}-\frac{1}{N}\right) \hat{\mathbf{B}}^{\prime} \hat{\mathbf{S}}_{\mathbf{x x}, 1} \mathbf{B}+\left(\frac{1}{r}-\frac{1}{N}\right) \hat{S}_{\mathrm{ee}, 2}
$$

where

$$
\begin{aligned}
\hat{\mathbf{S}}_{\mathbf{x x}, 1} & =\frac{1}{n-1} \sum_{i \in A_{1}}\left(\mathbf{x}_{i}-\overline{\mathbf{x}}_{1}\right)\left(\mathbf{x}_{i}-\overline{\mathbf{x}}_{1}\right)^{\prime} \\
\hat{S}_{\mathrm{ee}, 2} & =\frac{1}{r-1} \sum_{i \in A_{2}}\left(y_{i}-\mathbf{x}_{i}^{\prime} \hat{\mathbf{B}}\right)^{2}
\end{aligned}
$$

If jackknife is used, one should take into account the sampling variability of $\overline{\mathbf{x}}_{1}$ in the two-phase regression estimator. See Sitter (1997) and Fuller (1998) for more details.

Now, suppose the total cost $C$ is given by $C=c_{0}+c_{1} n+c_{2} r$, where $c_{0}, c_{1}$ and $c_{2}$ are known constants, and the sample sizes $n$ and $r$ are to be determined.




---

We wish to find the sample sizes that minimize the variance expression in (11.13), given the total cost $C$.

Defining $\nu=r / n$, we can express the variance times the term $\left(C-c_{0}\right)$ as

$$
\begin{aligned}
V \times\left(C-c_{0}\right) & =\left(c_{1}+\nu c_{2}\right)\left(B^{\prime} S_{x x} B+\frac{1}{\nu} S_{e e}\right) \\
& =\text { Const. }+c_{2} B^{\prime} S_{x x} B \nu+c_{1} S_{e e} \frac{1}{\nu}
\end{aligned}
$$

The optimal value of $\nu$ that minimizes this expression is

$$
\nu^{*}=\left(\frac{c_{1}}{c_{2}} \times \frac{S_{e e}}{B^{\prime} S_{x x} B}\right)^{1 / 2}
$$

This optimal $\nu^{*}$ can be interpreted as follows:

1. If the regression model has strong predictive power (large $B^{\prime} S_{x x} B$ ), then $\nu^{*}$ can be reduced, as the regression estimation becomes more effective.
2. If the cost of observing $y$ is quite high compared to the cost of observing $x$ (large $c_{2} / c_{1}$ ), then $\nu^{*}$ can be reduced.

Once $\nu^{*}$ is obtained from (11.15), the optimal value of $n^{*}$ can be found by solving the total cost equation

$$
C=c_{0}+c_{1} n+c_{2} n \nu^{*}
$$

with respect to $n$.
We now consider the general situation where the first-phase sampling is not necessarily the simple random sampling. For general two-phase sampling designs, the two-phase regression estimator can be written as

$$
\hat{Y}_{\mathrm{reg}, \mathrm{tp}}=\sum_{i \in A_{1}} w_{1 i} x_{i}^{\prime} \hat{\beta}_{2}+\sum_{i \in A_{2}} w_{1 i} \frac{1}{\pi_{2 i \mid 1}}\left(y_{i}-x_{i}^{\prime} \hat{\beta}_{2}\right)
$$

where $w_{1 i}=1 / \pi_{i}^{(1)}$ are the first-phase sampling weights, $\pi_{2 i \mid 1}=\pi_{i \mid A_{1}}^{(2)}$ are the conditional second-phase inclusion probabilities, and $\hat{\beta}_{2}$ is the regression coefficient estimated from the second-phase sample. This formulation generalizes the previous expression for the two-phase regression estimator, which assumed simple random sampling in both phases. The key distinction is the incorporation of the general sampling weights and probabilities to account for more complex sampling designs in the first and second phases.

Notably, the asymptotic unbiasedness of the two-phase regression estimator in equation (11.16) holds regardless of the specific method used to obtain the estimate $\hat{\beta}_{2}$ from the second-phase sample. This property enhances the flexibility and applicability of this estimator in practical settings with diverse sampling schemes.




---

Now, if we assume that the vector $\mathbf{x}_{i}$ includes $\pi_{2 i \mid 1}^{-1}$ such that $\mathbf{x}_{i}^{\prime} \mathbf{a}=\pi_{2 i \mid 1}^{-1}$ for some vector a, the two-phase regression estimator in equation (11.16) can be shown to be algebraically equivalent to the following form:

$$
\hat{Y}_{\mathrm{reg}, \mathrm{tp}}=\sum_{i \in A_{1}} w_{1 i} \mathbf{x}_{i}^{\prime} \hat{\boldsymbol{\beta}}_{2}
$$

where

$$
\hat{\boldsymbol{\beta}}_{2}=\left(\sum_{i \in A_{2}} w_{1 i} \mathbf{x}_{i} \mathbf{x}_{i}^{\prime}\right)^{-1} \sum_{i \in A_{2}} w_{1 i} \mathbf{x}_{i} y_{i}
$$

This alternative form in equation (11.17) takes the structure of a projection estimator, as discussed in Kim and Rao (2012). In other words, the two-phase regression estimator can be expressed as a projection of the observations onto the space spanned by the covariates $\mathbf{x}_{i}$, with the projection coefficients given by $\hat{\boldsymbol{\beta}}_{2}$.

Importantly, this projection estimator formulation in (11.17) is asymptotically design-unbiased, as the following condition holds:

$$
\sum_{i \in A_{2}} w_{1 i} \frac{1}{\pi_{2 i \mid 1}}\left(y_{i}-\mathbf{x}_{i}^{\prime} \hat{\boldsymbol{\beta}}_{2}\right)=0
$$

holds. This property ensures the asymptotic unbiasedness of the two-phase regression estimator under the assumed condition of the covariate vector $\mathbf{x}_{i}$.

To compute the asymptotic variance of the two-phase regression estimator in equation (11.16), we define $\boldsymbol{\beta}^{*}$ to be the probability limit of the regression coefficient estimate $\hat{\boldsymbol{\beta}}_{2}$. In this case, since $\hat{\boldsymbol{\beta}}_{2}-\boldsymbol{\beta}^{*}=O_{p}\left(n^{-1 / 2}\right)$, we can establish the following linearized representation of the two-phase regression estimator:

$$
\hat{Y}_{\mathrm{reg}, \mathrm{tp}}=\hat{Y}_{\mathrm{reg}, \mathrm{tp}, \ell}+O_{p}\left(n^{-1} N\right)
$$

where the linearized estimator is given by

$$
\hat{Y}_{\mathrm{reg}, \mathrm{tp}, \ell}=\sum_{i \in A_{1}} w_{1 i} \mathbf{x}_{i}^{\prime} \boldsymbol{\beta}^{*}+\sum_{i \in A_{2}} w_{1 i} \frac{1}{\pi_{2 i \mid 1}}\left(y_{i}-\mathbf{x}_{i}^{\prime} \boldsymbol{\beta}^{*}\right)
$$

This linearized form (11.21) reveals that the two-phase regression estimator $\hat{Y}_{\text {reg,tp }}$ can be expressed as the sum of a weighted mean of the first-phase covariates $\mathbf{x}_{i}$ multiplied by the probability limit $\boldsymbol{\beta}^{*}$, and a weighted sum of the residuals $y_{i}-\mathbf{x}_{i}^{\prime} \boldsymbol{\beta}^{*}$ from the second-phase observations. The remainder term $O_{p}\left(n^{-1} N\right)$ vanishes asymptotically as the sample sizes increase.

This linearized representation will facilitate the subsequent derivation of the asymptotic variance of the two-phase regression estimator, which can be obtained by analyzing the properties of the component terms in equation (11.21).




---

Under some regularity conditions, the asymptotic variance of the twophase regression estimator $\hat{Y}_{\text {reg,tp }}$ is equivalent to the variance of the two-phase linearized estimator (or difference estimator) defined in equation (11.21). This variance can be expressed as

$$
\mathcal{V}\left(\hat{Y}_{\text {diff,tp }}\right)=\mathcal{V}\left(\sum_{i \in \mathcal{A}_{1}} w_{1 i} y_{i}\right)+\mathcal{E}\left[\mathcal{V}\left\{\sum_{i \in \mathcal{A}_{2}} w_{1 i} \frac{1}{\pi_{2 i \mid 1}}\left(y_{i}-\boldsymbol{x}_{i}^{\prime} \boldsymbol{\beta}^{*}\right) \mid \mathcal{A}_{1}\right\}\right]
$$

If the second-phase sampling follows a Poisson scheme, then the second term in the above expression can be simplified to

$$
V_{2}=\mathcal{E}\left\{\sum_{i \in \mathcal{A}_{1}} w_{1 i}^{2}\left(\frac{1}{\pi_{2 i \mid 1}}-1\right) e_{i}^{2}\right\}
$$

where $e_{i}=y_{i}-\boldsymbol{x}_{i}^{\prime} \boldsymbol{\beta}^{*}$.
The optimal choice of the conditional second-phase inclusion probabilities $\pi_{2 i \mid 1}^{*}$ that minimizes the variance $V_{2}$ is

$$
\pi_{2 i \mid 1}^{*} \propto w_{1 i}\left[\mathcal{E}\left\{e_{i}^{2} \mid \boldsymbol{x}_{i}\right\}\right]^{1 / 2}
$$

This optimal design of the second-phase sampling probabilities depends on the conditional variance of the residuals $e_{i}$ given the covariates $\boldsymbol{x}_{i}$, as well as the first-phase sampling weights $w_{1 i}$.

The derivation of this asymptotic variance expression and the optimal sampling design result provides a framework for determining efficient twophase sampling strategies in practical applications.

If both phase samples are SRS, the above variance formula reduces to

$$
\begin{aligned}
\mathcal{V}\left(\hat{Y}_{\text {diff,tp }}\right) & =\frac{N^{2}}{n}\left(1-\frac{n}{N}\right) S_{y}^{2}+\left(\frac{N^{2}}{n}\right)^{2} \frac{n_{2}}{r}\left(1-\frac{r}{n}\right) S_{e}^{2} \\
& =N^{2}\left(\frac{1}{n}-\frac{1}{N}\right)\left(S_{y}^{2}-S_{e}^{2}\right)+N^{2}\left(\frac{1}{r}-\frac{1}{N}\right) S_{e}^{2}
\end{aligned}
$$

which is consistent with the result in (11.13).
We now consider variance estimation for two-phase regression estimator. Note that using the linearization formula in (11.20), we can express

$$
\hat{Y}_{\mathrm{reg}, \mathrm{tp}, \ell}=\sum_{i \in \mathcal{A}_{1}} w_{1 i} \eta_{i}
$$

where

$$
\eta_{i}=\boldsymbol{x}_{i}^{\prime} \boldsymbol{\beta}^{*}+\frac{\delta_{i}}{\pi_{2 i}}\left(y_{i}-\boldsymbol{x}_{i}^{\prime} \boldsymbol{\beta}^{*}\right)
$$

is the influence function of the two-phase regression estimator and

$$
\delta_{i}= \begin{cases}1 & \text { if } i \in \mathcal{A}_{2} \text { when is sampled in } \mathcal{A}_{1} \\ 0 & \text { otherwise. }\end{cases}
$$




---

This formulation expresses the linearized two-phase regression estimator as a weighted sum of the influence functions $\eta_{i}$, where the weights are the firstphase sampling weights $w_{1 i}$.

The key aspects to note are:

1. The influence function $\eta_{i}$ combines the contribution from the firstphase covariates $\mathbf{x}_{i}$ and the residual $y_{i}-\mathbf{x}_{i}^{\prime} \boldsymbol{\beta}^{*}$ from the second-phase observations, scaled by the inverse of the conditional second-phase inclusion probability $\pi_{2 i \mid 1}$.
2. The indicator $\delta_{i}$ tracks whether the $i$-th unit was selected in the second-phase sample, given that it was included in the first-phase sample.

This representation of the linearized two-phase regression estimator will facilitate the subsequent development of variance estimation procedures, as the variance can be expressed in terms of the influence functions $\eta_{i}$.

Note that the indicators $\delta_{i}$ are defined across the entire finite population, not just the sampled units in $\mathcal{A}_{1}$. While we only observe the values of $\delta_{i}$ for $i \in \mathcal{A}_{1}$, we can still conceptualize the $\delta_{i}$ as being defined for all $i=1, \ldots, N$ in the population.

Given this view of the finite population, we can apply the reverse framework of Fay (1992), Shao and Steel (1999), and Kim et al. (2006). In this framework, the finite population consists of two components: $\mathcal{R}_{N}=\left\{\delta_{1}, \delta_{2}, \ldots, \delta_{N}\right\}$ and $\mathcal{F}_{N}=\left\{\left(\mathbf{x}_{i}, y_{i}\right) ; i=1, \ldots, N\right\}$. The sample $\mathcal{A}_{1}$ is then selected from this population according to a probability sampling design. We observe $\delta_{i}$ and $\mathbf{x}_{i}$ for $i \in \mathcal{A}_{1}$, and observe $y_{i}$ for the units with $\delta_{i}=1$.

Using this setup, the total variance of the linearized two-phase regression estimator $\hat{Y}_{\text {reg,tp, } \ell}$ can be expressed as

$$
\begin{aligned}
\mathbb{V}\left(\hat{Y}_{\text {reg,tp, } \ell}\right) & =\mathbb{E}\left\{\mathbb{V}\left(\sum_{i \in \mathcal{A}_{1}} w_{1 i} \eta_{i} \mid \mathcal{R}_{N}, \mathcal{F}_{N}\right) \mid \mathcal{F}_{N}\right\}+\mathbb{V}\left\{\mathbb{E}\left(\sum_{i \in \mathcal{A}_{1}} w_{1 i} \eta_{i} \mid \mathcal{R}_{N}, \mathcal{F}_{N}\right) \mid \mathcal{F}_{N}\right\} \\
& =\mathbb{E}\left\{\sum_{i=1}^{N} \sum_{j=1}^{N}\left(\pi_{1 i j}-\pi_{1 i} \pi_{1 j}\right) \eta_{i} \eta_{j} \mid \mathcal{F}_{N}\right\}+\mathbb{V}\left\{\sum_{i=1}^{N} \eta_{i} \mid \mathcal{F}_{N}\right\} \\
& :=V_{1}+V_{2}
\end{aligned}
$$

The first term $V_{1}$ represents the sampling variance of the linearized two-phase regression estimator, treating the $\delta_{i}$ indicators as fixed. The second term $V_{2}$ reflects the variance due to the randomness in the $\delta_{i}$ indicators in the influence function $\eta_{i}$.

Observe that if the influence functions $\eta_{i}$ were observed, the first component $V_{1}$ of the total variance could be easily estimated using the standard




---

variance estimation formula. Therefore, a linearization-based variance estimator for two-phase sampling can be developed as

$$
\hat{V}=\sum_{i \in \mathcal{A}_{1}} \sum_{j \in \mathcal{A}_{1}} \frac{\pi_{1 i j}-\pi_{1 i} \pi_{1 j}}{\pi_{1 i j}} \frac{\hat{\eta}_{i}}{\pi_{1 i}} \frac{\hat{\eta}_{j}}{\pi_{1 j}}
$$

where the estimated influence function $\hat{\eta}_{i}$ is given by

$$
\hat{\eta}_{i}=\mathbf{x}_{i}^{\prime} \hat{\boldsymbol{\beta}}+\frac{\delta_{i}}{\pi_{2 i \mid 1}}\left(y_{i}-\mathbf{x}_{i}^{\prime} \hat{\boldsymbol{\beta}}\right)
$$

This linearization variance estimator $\hat{V}$ approximates the first component $V_{1}$ of the total variance, which can be expressed as

$$
E\left(\hat{V} \mid \mathcal{R}_{N}, \mathcal{F}_{N}\right) \cong V\left(\sum_{i \in \mathcal{A}_{1}} w_{1 i} \eta_{i} \mid \mathcal{R}_{N}, \mathcal{F}_{N}\right)
$$

And taking the expectation with respect to the first-phase sampling design, we have

$$
E\left(\hat{V} \mid \mathcal{F}_{N}\right) \cong E\left\{V\left(\sum_{i \in \mathcal{A}_{1}} w_{1 i} \eta_{i} \mid \mathcal{R}_{N}, \mathcal{F}_{N}\right)\right\}=V_{1}
$$

This implies that the bias of the linearization variance estimator $\hat{V}$ in (11.25) is given by

$$
\begin{aligned}
\operatorname{Bias}(\hat{V}) & =-V\left(\sum_{i=1}^{N} \eta_{i} \mid \mathcal{F}_{N}\right) \\
& =-\sum_{i=1}^{N} \sum_{j=1}^{N} \operatorname{Cov}\left(\delta_{i}, \delta_{j}\right) \pi_{2 i}^{-1} \pi_{2 j}^{-1} e_{i} e_{j}
\end{aligned}
$$

This bias term is of order $O(N)$, which is smaller than the leading order of $V_{1}=O\left(n^{-1} N^{2}\right)$ when the first-phase sampling rate is negligible (i.e., $n / N \doteq 0$ ).

Under Poisson sampling in the second phase, we can estimate the bias by

$$
\widehat{\operatorname{Bias}}(\hat{V})=-\sum_{i \in \mathcal{A}_{1}} w_{1 i} \frac{\delta_{i}}{\pi_{2 i}}\left(\frac{1}{\pi_{2 i}}-1\right)\left(y_{i}-\mathbf{x}_{i}^{\prime} \hat{\boldsymbol{\beta}}\right)^{2}
$$

Replication variance estimator can be easily applied in this case. To do this, we use (11.19) to get

$$
\hat{Y}_{\mathrm{reg}, \mathrm{tp}}=\sum_{i \in \mathcal{A}_{1}} w_{i} \mathbf{x}_{i}^{\prime} \hat{\boldsymbol{\beta}}_{2}=\hat{\mathbf{X}}_{1}^{\prime} \hat{\boldsymbol{\beta}}_{2}
$$




---

which is a product of two random variables. We can easily construct the replicates of $\hat{Y}_{\text {reg,tp }}$ by replacing the original weight $w_{i}$ by its replication weight $w_{i}^{(k)}$ to get

$$
\hat{Y}_{\text {reg,tp }}^{(k)}=\hat{\mathbf{X}}^{(k) \prime} \hat{\boldsymbol{\beta}}_{2}^{(k)}
$$

where

$$
\hat{\mathbf{X}}^{(k)}=\sum_{i \in A_{1}} w_{i}^{(k)} \mathbf{x}_{i}
$$

and

$$
\hat{\boldsymbol{\beta}}_{2}^{(k)}=\left(\sum_{i \in A_{2}} w_{i}^{(k)} \mathbf{x}_{i} \mathbf{x}_{i}^{\prime}\right)^{-1} \sum_{i \in A_{2}} w_{i}^{(k)} \mathbf{x}_{i} y_{i}
$$

Note that we did not construct the replicate of $\pi_{2 i \mid 1}$ in (11.16). Using (11.19), the sampling variability of $\pi_{2 i \mid 1}$ is safely transferred to $\hat{\boldsymbol{\beta}}_{2}$. Once the replicates are calculated, we can use the replication variance formula to estimate the variance. See Park and Kim (2019) for more details of replication variance estimation under two-phase sampling.

The two-phase regression estimator can be implemented using a calibration weighting approach. Specifically, we can obtain the second-phase weights $\omega_{2 i}$ by minimizing the following quadratic objective function

$$
Q\left(\boldsymbol{\omega}_{2}\right)=\sum_{i \in A_{2}}\left\{w_{1 i} \omega_{2 i}-w_{1 i} \pi_{2 i \mid 1}^{-1}\right\}^{2}
$$

subject to the calibration constraint

$$
\sum_{i \in A_{2}} w_{1 i} \omega_{2 i} \mathbf{x}_{i}=\sum_{i \in A_{1}} w_{1 i} \mathbf{x}_{i}
$$

The solution to the optimization problem is

$$
\hat{\omega}_{2 i}=\pi_{2 i \mid 1}^{-1}+\left(\sum_{i \in A_{1}} w_{1 i} \mathbf{x}_{i}-\sum_{i \in A_{2}} w_{1 i} \pi_{2 i \mid 1}^{-1} \mathbf{x}_{i}\right)^{\prime}\left(\sum_{i \in A_{2}} w_{1 i} \mathbf{x}_{i} \mathbf{x}_{i}^{\prime}\right)^{-1} \mathbf{x}_{i}
$$

Importantly, the weighted sum $\sum_{i \in A_{2}} w_{1 i} \hat{\omega}_{2 i} y_{i}$ is algebraically equivalent to the two-phase regression estimator in equation (11.16), where the regression coefficient $\hat{\boldsymbol{\beta}}_{2}$ is obtained using the expression in (11.18). This calibration weighting approach provides an alternative implementation of the two-phase regression estimator, which can be useful as the regression coefficients are estimated indirectly from the data. The calibration constraint (11.27) ensures that the weighted sum of the first-phase covariates in the second-phase sample matches the total from the first-phase sample, thereby achieving the desired calibration.

When the auxiliary variables $\mathbf{x}_{i}$ exhibit a monotone missing pattern, the




---

calibration weighting approach can be implemented sequentially. Suppose the vector of auxiliary variables $\mathbf{x}_{i}$ can be partitioned as $\mathbf{x}_{i}=\left(\mathbf{x}_{i}^{(1)}, \mathbf{x}_{i}^{(2)}\right)$, and the population total of $\mathbf{x}_{i}^{(1)}$ is known. In this case, we can apply the following two-step calibration method:
[Step 1] Obtain $w_{1 i}$ by solving the calibration problem by minimizing

$$
Q_{1}\left(\omega_{1}\right)=\sum_{i \in A_{1}}\left(\omega_{1 i}-\pi_{1 i}^{-1}\right)^{2}
$$

subject to

$$
\sum_{i \in A_{1}} \omega_{1 i} \mathbf{x}_{i}^{(1)}=\sum_{i=1}^{N} \mathbf{x}_{i}^{(1)}
$$

[Step 2] Once the first-phase weights $w_{1 i}=\hat{\omega}_{1 i}$ are obtained from [Step 1], obtain $\omega_{2 i}$ by minimizing $Q\left(\boldsymbol{\omega}_{2}\right)$ in (11.26), subject to the calibration constraint (11.27).

This two-step calibration approach leverages the known population total of the first-part of the auxiliary variables $\mathbf{x}_{i}^{(1)}$ to first determine the appropriate first-phase weights $w_{1 i}$. Then, in the second step, the second-phase weights $\omega_{2 i}$ are obtained by calibrating to the full set of auxiliary variables $\mathbf{x}_{i}$.

This sequential calibration procedure is particularly useful when the auxiliary information exhibits a monotone missing pattern, allowing for efficient utilization of the available data at each phase of the sampling design.

# 11.4 Non-nested two-phase sampling 

In contrast to the classical two-phase sampling framework, non-nested twophase sampling involves two independent surveys conducted on the same target population. The key distinction is that the two samples, denoted as $A_{1}$ and $A_{2}$, are drawn independently rather than sequentially. Table 11.1 presents the data structure for non-nested two-phase sampling.

In the non-nested two-phase sampling, a large probability sample $A_{1}$ is drawn from a finite population, collecting only the $x$ variable, and a smaller sample $A_{2}$ is drawn from the same population, providing information on both the $y$ and $x$ variables. It is assumed that the observed variable $x$ is comparable in the two surveys. Renssen and Nieuwenbroek (1997) formally addressed this non-nested two-phase sampling problem and Merkouris (2004) extended the idea further to develop regression estimation combining information from multiple surveys. Kim and Rao (2012) considered the non-nested two-phase sampling in the context of mass imputation combining two independent surveys at the population and domain levels.




---

TABLE 11.1
Data Structure for non-nested two-phase sampling

| Sample | X | Y |
| :---: | :---: | :---: |
| $\mathcal{A}_{1}$ | $\checkmark$ |  |
| $\mathcal{A}_{2}$ | $\checkmark \checkmark$ |  |

To illustrate the non-nested two-phase sampling approach, let's consider the data structure shown in Table 11.1. This setup involves two independent samples, $\mathcal{A}_{1}$ and $\mathcal{A}_{2}$, drawn from the same target population.

From these two samples, we can compute two unbiased estimators of the population total $X=\sum_{i=1}^{N} x_{i}$ for the auxiliary variable $x$ : $\hat{X}_{1}=\sum_{i \in \mathcal{A}_{1}} \pi_{1 i}^{-1} x_{i}$ and $\hat{X}_{2}=\sum_{i \in \mathcal{A}_{2}} \pi_{2 i}^{-1} x_{i}$. Here, $\pi_{1 i}$ and $\pi_{2 i}$ represent the inclusion probabilities for samples $\mathcal{A}_{1}$ and $\mathcal{A}_{2}$, respectively.

Both $\hat{X}_{1}$ and $\hat{X}_{2}$ are unbiased estimators of the population total $X$ under the respective sampling designs. The availability of these two unbiased estimators is a key feature of the non-nested two-phase sampling design, as it provides opportunities for developing enhanced estimation procedures combining information from different sources.

We can construct a combined estimator of $X$, denoted as $\widehat{X}_{c}$, as follows:

$$
\widehat{X}_{c}=W \hat{X}_{1}+(I-W) \hat{X}_{2}
$$

where $W$ is a $p \times p$ symmetric matrix of constants, and $p=\operatorname{dim}(x)$ is the dimension of the auxiliary variable $x$. The optimal choice of the matrix $W$ can be determined using the Generalized Least Squares (GLS) method. However, other choices of $W$ can also be used. The key idea is to leverage the information from these two independent surveys to obtain a more accurate and efficient estimator of the population total $X$ for the auxiliary variable $x$, compared to using only one of the surveys alone.

Using the combined estimator $\widehat{X}_{c}$ in (11.28), we can construct the following projection estimator:

$$
\widehat{Y}_{p}=\widehat{X}_{c}^{\prime} \hat{\boldsymbol{\beta}}_{q}
$$

where the regression coefficient estimator $\hat{\boldsymbol{\beta}}_{q}$ is defined as

$$
\hat{\boldsymbol{\beta}}_{q}=\left(\sum_{i \in \mathcal{A}_{2}} x_{i} x_{i}^{\prime} / q_{i}\right)^{-1} \sum_{i \in \mathcal{A}_{2}} x_{i} y_{i} / q_{i}
$$

The choice of $q_{i}$ in the regression coefficient estimator is somewhat arbitrary. Two possible choices are:

1. Using the model variance under a regression superpopulation model.
2. Using $q_{i}=\pi_{2 i}^{-2}-\pi_{2 i}^{-1}$ to compute the design-optimal regression estimator under Poisson sampling.



---

The key idea is that by using the combined estimator $\widehat{\mathbf{X}}_{c}$ in the projection estimator $\widehat{Y}_{p}$, we can leverage the information from both the $\mathcal{A}_{1}$ and $\mathcal{A}_{2}$ samples to obtain a more accurate prediction of the variable of interest $Y$. The choice of $q_{i}$ allows for some flexibility in how the regression coefficient is estimated.

To ensure the design-consistency of the projection estimator in (11.29), we can use the following regression estimator under non-nested two-phase sampling:

$$
\widehat{Y}_{\mathrm{tp}, \mathrm{reg}}=\widehat{\bar{Y}}_{2}+\left(\widehat{\overline{\mathbf{X}}}_{c}-\widehat{\overline{\mathbf{X}}}_{2}\right)^{\prime} \hat{\boldsymbol{\beta}}_{q}
$$

By the definition of $\widehat{\overline{\mathbf{X}}}_{c}$, we can also express this as:

$$
\widehat{Y}_{\mathrm{tp}, \mathrm{reg}}=\widehat{\bar{Y}}_{2}+\left(\widehat{\overline{\mathbf{X}}}_{1}-\widehat{\overline{\mathbf{X}}}_{2}\right)^{\prime} \hat{\boldsymbol{\alpha}}_{q}
$$

where $\hat{\boldsymbol{\alpha}}_{q}=\mathbf{W} \hat{\boldsymbol{\beta}}_{q}$. The key points are:

1. The design-consistent regression estimator $\widehat{Y}_{\mathrm{tp}, \mathrm{reg}}$ is constructed by adding a correction term to the projection estimator $\widehat{Y}_{p}$ from the second sample.
2. The regression estimator improves the efficiency of the design unbiased estimator $\hat{Y}_{2}$ by substracting the projection of $\hat{Y}_{2}$ onto the augmentation space (Tsiatis, 2006), the linear space generated by the difference between the combined estimator $\widehat{\overline{\mathbf{X}}}_{c}$ and the estimator $\widehat{\overline{\mathbf{X}}}_{2}$ from the second sample.
3. Alternatively, the augmentation space can be expressed using the difference between the estimators $\widehat{\overline{\mathbf{X}}}_{1}$ and $\widehat{\overline{\mathbf{X}}}_{2}$, weighted by $\hat{\boldsymbol{\alpha}}_{q}$.

The goal is to leverage the information from both samples to obtain a designconsistent regression estimator for the variable of interest $Y$.

Using the standard argument, we can obtain

$$
\widehat{Y}_{\mathrm{tp}, \mathrm{reg}}=\widehat{\bar{Y}}_{2}+\left(\widehat{\overline{\mathbf{X}}}_{1}-\widehat{\overline{\mathbf{X}}}_{2}\right)^{\prime} \boldsymbol{\alpha}_{q}^{*}+O_{p}\left(n^{-1} N\right)
$$

where $\boldsymbol{\alpha}_{q}^{*}$ is the probability limit of $\hat{\boldsymbol{\alpha}}_{q}=\mathbf{W} \hat{\boldsymbol{\beta}}_{q}$. By (11.32), we can obtain

$$
\mathcal{V}\left(\widehat{Y}_{\mathrm{tp}, \mathrm{reg}}\right)=\left(\boldsymbol{\alpha}_{q}^{*}\right)^{\prime} \mathcal{V}\left(\widehat{\overline{\mathbf{X}}}_{1}\right) \boldsymbol{\alpha}_{q}^{*}+\mathcal{V}\left(\hat{u}_{2}\right)
$$

where $\hat{u}_{2}=\sum_{i \in \mathcal{A}_{2}} \pi_{2 i}^{-1}\left(y_{i}-\mathbf{x}_{i}^{\prime} \boldsymbol{\alpha}_{q}^{*}\right)$. From the formula in (11.33), we can construct a linearized variance estimator.

Now, we can use the calibration weighting to construct the regression estimator under non-nested two-phase sampling. For given the design weights $d_{2 i}=\pi_{2 i}^{-1}$, we find the minimizer of

$$
Q(\boldsymbol{\omega})=\sum_{i \in \mathcal{A}_{2}}\left(\omega_{i}-d_{2 i}\right)^{2} q_{i}
$$




---

subject to

$$
\sum_{i \in A_{2}} \omega_{i} \mathbf{x}_{i}=\widehat{\mathbf{X}}_{c}
$$

The solution is

$$
\hat{\omega}_{i}=d_{i}^{2}+\left(\widehat{\mathbf{X}}_{c}-\widehat{\mathbf{X}}_{2}\right)^{-1}\left(\sum_{i \in A_{2}} q_{i}^{-1} \mathbf{x}_{i} \mathbf{x}_{i}^{\prime}\right)^{-1} \mathbf{x}_{i} q_{i}^{-1}
$$

Note that

$$
\sum_{i \in A_{2}} \hat{\omega}_{i} y_{i}=\widehat{Y}_{\mathrm{tp}, \mathrm{reg}}
$$

where $\widehat{Y}_{\text {tp,reg }}$ is defined in (11.31). Thus, the algebraic equivalence between the regression estimator and the calibration weighting estimator is established under non-nested two-phase sampling.

We now consider an extension combining information from three independent samples. Suppose that we have three independent samples, denoted by $A, B$, and $C$, and the observed data structure is summarized in Table 11.2.

TABLE 11.2
Data Structure for three independent samples

|  | Case 1 |  |  | Case 2 |  |  |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Sample | $X_{1}$ | $X_{2}$ | $Y$ | $X_{1}$ | $X_{2}$ | $Y$ |
| $A$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ |  |
| $B$ | $\checkmark$ | $\checkmark$ | $\checkmark$ |  |  |  |
| $C$ |  |  |  | $\checkmark$ | $\checkmark$ |  |

We first consider the data structure in Case 1. In this case, we can use two-step estimation procedure for combining all available information. In the first step, we use the generalized least squares (GLS) method to combine information and obtain the best linear unbiased estimator of the population total of $\mathbf{x}^{\prime}=\left(\mathbf{x}_{1}^{\prime}, \mathbf{x}_{2}^{\prime}\right)$. Let $\hat{\mathbf{X}}_{\text {GLS }}$ be the GLS estimator of $\mathbf{X}=\sum_{i=1}^{N} \mathbf{x}_{i}$.

In the second step, we construct the calibration weights in sample $A$. Given the design weight $d_{i}^{(A)}$ for sample $A$, we find the minimizer of

$$
Q_{A}(\boldsymbol{\omega})=\sum_{i \in A} \frac{\left(\omega_{i}-d_{i}^{(A)}\right)^{2}}{q_{i}}
$$

subject to

$$
\sum_{i \in A} \omega_{i} \mathbf{x}_{i}=\widehat{\mathbf{X}}_{\mathrm{GLS}}
$$




---

The solution is

$$
\hat{\omega}_{i}=d_{i}^{(A)}+\left(\hat{X}_{\mathrm{GLS}}-\hat{X}_{A}\right)^{\prime}\left(\sum_{i \in A} q_{i}^{-1} x_{i} x_{i}^{\prime}\right)^{-1} x_{i} q_{i}^{-1}
$$

Note that

$$
\sum_{i \in A} \hat{\omega}_{i} y_{i}=\hat{Y}_{\mathrm{reg}}
$$

where

$$
\hat{Y}_{\mathrm{reg}}=\hat{Y}_{A}+\left(\hat{X}_{\mathrm{GLS}}-\hat{X}_{A}\right)^{\prime} \hat{\boldsymbol{\beta}}_{q}
$$

and

$$
\hat{\boldsymbol{\beta}}_{q}=\left(\sum_{i \in A} q_{i}^{-1} x_{i} x_{i}^{\prime}\right)^{-1} \sum_{i \in A} q_{i}^{-1} x_{i} y_{i}
$$

Thus, the above calibration estimator is algebraically equivalent to the biascorrected regression estimator using $\widehat{X}_{\text {GLS }}$ as the estimated control for $X$.

Now, in Case 2, we wish to develop calibration weights for sample $B$. The GLS step is the same as Case 1. Now, to construct the calibration weights for sample $B$, given the design weight $d_{i}^{(B)}$ for sample $B$, we find the minimizer of

$$
Q_{B}\left(\boldsymbol{\omega}^{(B)}\right)=\sum_{i \in B} \frac{\left(\omega_{i}^{(B)}-d_{i}^{(B)}\right)^{2}}{q_{i}}
$$

subject to

$$
\sum_{i \in B} \omega_{i}^{(B)} x_{1 i}=\hat{X}_{1, \mathrm{GLS}}
$$

The solution is

$$
\hat{\omega}_{i}^{(B)}=d_{i}^{(B)}+\left(\hat{X}_{1, \mathrm{GLS}}-\hat{X}_{1 B}\right)^{\prime}\left(\sum_{i \in B} q_{i}^{-1} x_{1 i} x_{1 i}^{\prime}\right)^{-1} x_{1 i} q_{i}^{-1}
$$

Note that

$$
\sum_{i \in B} \hat{\omega}_{i}^{(B)} y_{i}=\hat{Y}_{B}+\left(\hat{X}_{1, \mathrm{GLS}}-\hat{X}_{1, B}\right)^{\prime} \hat{\boldsymbol{\beta}}_{1 q}
$$

where $\hat{Y}_{B}=\sum_{i \in B} d_{i}^{(B)} y_{i}, \hat{X}_{1, B}=\sum_{i \in B} d_{i}^{(B)} x_{1 i}$, and

$$
\hat{\boldsymbol{\beta}}_{1 q}=\left(\sum_{i \in B} q_{i}^{-1} x_{1 i} x_{1 i}^{\prime}\right)^{-1} \sum_{i \in B} q_{i}^{-1} x_{1 i} y_{i}
$$

Therefore, the calibration weighting method can be used to combine the information in the multiple surveys effectively.




---

# 11.5 Repeated surveys 

Repeated surveys means that the survey measurement is taken for the same population at different times. For example, in the US Current Population Survey, the employment rates are announced monthly. In this case, the sample selection can be repeated at different times. In the repeated surveys, suppose that there are two different years, there are three different parameters of interest.

1. $\bar{Y}_{1}-\bar{Y}_{2}$ : the difference of the population mean over two different years.
2. $\left(\bar{Y}_{1}+\bar{Y}_{2}\right) / 2$ : overall mean over the two different years.
3. $\bar{Y}_{2}$ : the population mean at the most recent year.

The optimal sampling design for $\theta_{1}=\bar{Y}_{1}-\bar{Y}_{2}$ can be quite different from the optimal sampling design for $\bar{Y}=\left(\bar{Y}_{1}+\bar{Y}_{2}\right) / 2$. Let $\bar{y}_{1}$ and $\bar{y}_{2}$ be an unbiased estimator of $\bar{Y}_{1}$ and $\bar{Y}_{2}$, respectively. If we use $\hat{\theta}=\bar{y}_{1}-\bar{y}_{2}$ to estimate $\bar{Y}_{1}-\bar{Y}_{2}$, the variance of $\hat{\theta}$ is minimized when $\operatorname{Corr}\left(\bar{y}_{1}, \bar{y}_{2}\right)=1$. The correlation increases when the sample for $t=1$ is the same as the sample for $t=2$. That is, it is the case where the same sample is used to obtain the measurement for $t=1$ and for $t=2$. Such a sample is often called a panel sample. On the other hand, if the parameter of interest is $\bar{Y}=\left(\bar{Y}_{1}+\bar{Y}_{2}\right) / 2$, the design of the panel sample increases the variance. Independent sample selection, leading to $\operatorname{Corr}\left(\bar{y}_{1}, \bar{y}_{2}\right)=0$, is more efficient than panel sample design if we are interested in estimating $\bar{Y}=\left(\bar{Y}_{1}+\bar{Y}_{2}\right) / 2$.

Now, if we are interested in estimating $\bar{Y}_{2}$, the following partial overlap sampling design is more efficient than the previous two sampling designs.

1. At $t=1$, using an SRS of size $n$ to obtain $\mathcal{A}_{1}$.
2. At $t=2$, first stratify the finite population into two strata. One is $\mathcal{A}_{1}$ and the other is $\mathcal{U}-\mathcal{A}_{1}$. From the first stratum $\mathcal{A}_{1}$, select an SRS of size $n_{m}$ to obtain $\mathcal{A}_{2 m}$. From the second stratum $\mathcal{U}-$ $\mathcal{A}_{1}$, select an SRS of size $n_{u}=n-n_{m}$, independently of the first stratum, to obtain $\mathcal{A}_{2 u}$. The final sample is $\mathcal{A}_{2}=\mathcal{A}_{2 m} \cup \mathcal{A}_{2 u}$. The first stratum is called "matched" stratum and the second stratum is called "unmatched" stratum.

In this case, the final sample in the matched stratum can be viewed as a two-phase sample where the first phase sample is $\mathcal{A}_{1}$ and the second phase sample is $\mathcal{A}_{2 m}$. Also, the final sample in the unmatched sample is also a two-phase stratified sample, where the first phase sample is $\mathcal{U}-\mathcal{A}_{1}$ and the second-phase sample is $\mathcal{A}_{2 u}$. The following table presents a summary of the two estimators in each two-phase sample.




---

| Stratum | Population Size | Sample Size | Estimator of $\bar{Y}$ |
| :--- | :---: | :---: | :---: |
| Matched | $n$ | $n_{m}$ | $\hat{\bar{Y}}_{m}$ |
| Unmatched | $N-n$ | $n_{u}$ | $\hat{\bar{Y}}_{u}$ |

Now, consider the following class of estimators indexed by a constant $\alpha$ :

$$
\hat{\bar{Y}}_{\alpha}=\alpha \hat{\bar{Y}}_{u}+(1-\alpha) \hat{\bar{Y}}_{m}
$$

Such an estimator is a weighted average of two unbiased estimators, and is often called a composite estimator. The composite estimator is (approximately) unbiased if the two components, $\hat{\bar{Y}}_{u}$ and $\hat{\bar{Y}}_{m}$, are (approximately) unbiased. The optimal value of $\alpha$ that minimizes the variance of the composite estimator is

$$
\alpha^{*}=\frac{\mathcal{V}\left(\hat{\bar{Y}}_{m}\right)-\operatorname{Cov}\left(\hat{\bar{Y}}_{u}, \hat{\bar{Y}}_{m}\right)}{\mathcal{V}\left(\hat{\bar{Y}}_{u}\right)+\mathcal{V}\left(\hat{\bar{Y}}_{m}\right)-2 \operatorname{Cov}\left(\hat{\bar{Y}}_{u}, \hat{\bar{Y}}_{m}\right)}
$$

In this case, the optimal composite estimator is

$$
\hat{\bar{Y}}_{\alpha}^{*}=\alpha^{*} \hat{\bar{Y}}_{u}+\left(1-\alpha^{*}\right) \hat{\bar{Y}}_{m}
$$

and its variance is

$$
\mathcal{V}\left(\hat{\bar{Y}}_{\alpha}^{*}\right)=\frac{\mathcal{V}\left(\hat{\bar{Y}}_{m}\right) \mathcal{V}\left(\hat{\bar{Y}}_{u}\right)-\left\{\operatorname{Cov}\left(\hat{\bar{Y}}_{u}, \hat{\bar{Y}}_{m}\right)\right\}^{2}}{\mathcal{V}\left(\hat{\bar{Y}}_{u}\right)+\mathcal{V}\left(\hat{\bar{Y}}_{m}\right)-2 \operatorname{Cov}\left(\hat{\bar{Y}}_{u}, \hat{\bar{Y}}_{m}\right)}
$$

To discuss the choice of unbiased estimators, we first note that the measurement at $t=1$ can be treated as the auxiliary variable $x$ and the measurement at $t=2$ can be treated as the study variable $y$. In the unmatched stratum, there is no auxiliary information, so we use

$$
\hat{\bar{Y}}_{u}=\frac{1}{n_{u}} \sum_{i \in A_{2 u}} y_{i} \equiv \bar{y}_{u}
$$

On the other hand, in the matched stratum, we can use auxiliary information to get

$$
\hat{\bar{Y}}_{m}=\bar{y}_{m}+\left(\bar{x}_{1}-\bar{x}_{m}\right) b
$$

where

$$
\begin{aligned}
\left(\bar{x}_{m}, \bar{y}_{m}\right) & =n_{m}^{-1} \sum_{i \in A_{2 m}}\left(x_{i}, y_{i}\right) \\
b & =\left\{\sum_{i \in A_{2 m}}\left(x_{i}-\bar{x}_{m}\right)^{2}\right\}^{-1} \sum_{i \in A_{2 m}}\left(x_{i}-\bar{x}_{m}\right) y_{i} .
\end{aligned}
$$

Thus, the following summary can be made to the two estimators.




---


Also, we can show that

$$
\operatorname{Cov}\left(\hat{\bar{Y}}_{m}, \hat{\bar{Y}}_{u}\right)=0
$$

Thus, the optimal solution (11.35) is

$$
\alpha^{*}=\frac{n_{n u}-n_{u}^{2} \rho^{2}}{n^{2}-n_{u}^{2} \rho^{2}}
$$

which is equal to $\alpha^{*}=n_{u} / n$ for $\rho=0$ and equal to $\alpha^{*}=n_{u} /\left(n+n_{u}\right)$ for $\rho=1$. The variance of the optimal composite estimator is then, by (11.36),

$$
V\left(\hat{\bar{Y}}_{\alpha}^{*}\right)=\frac{n-n_{u} \rho^{2}}{n^{2}-n_{u}^{2} \rho^{2}} S^{2} \geq \frac{1}{n} S^{2}
$$

with the equality holds when $n_{m}=n$ or $n_{m}=0$ for $\rho \neq 0$.
The optimal allocation minimizing the variance (11.38) is

$$
\frac{n_{u}}{n}=\frac{1}{1+\sqrt{1-\rho^{2}}}, \quad \frac{n_{m}}{n}=\frac{\sqrt{1-\rho^{2}}}{1+\sqrt{1-\rho^{2}}}
$$

If $\rho$ is large then more sample is selected for the matched stratum. Under this optimal allocation, the variance (11.38) reduces to

$$
V\left(\hat{\bar{Y}}_{\alpha}^{*}\right)=\frac{S^{2}}{2 n\left(1+\sqrt{1-\rho^{2}}\right)}
$$

which takes the value between $S^{2} /(2 n)$ and $S^{2} / n$. More discussion on this type of repeated surveys can be found in Fuller (1990).




---

# 12 

## Nonresponse

### 12.1 Introduction

Most surveys will have nonresponse. There are two types of nonresponse: unit nonresponse, where the survey unit itself is nonresponsive, and item nonresponse, where only some items are nonresponsive. These nonresponses can be handled in two ways: in the case of unit nonresponse, a call-back or followup survey or nonresponse weighting adjustment can be used. For item nonresponse, imputation is commonly used.

To understand the effect of nonresponse, consider the data structure in Table 12.1.

TABLE 12.1
Data structure with nonresponse

| Stratum | Population Size | Population Mean | Sample Size |
| :--- | :---: | :---: | :---: |
| Respondents | $N_{R}$ | $\bar{Y}_{R}$ | $n_{R}$ |
| Non-respondents | $N_{M}$ | $\bar{Y}_{M}$ | $n_{M}$ |
| Population | $N$ | $\bar{Y}$ | $n$ |

In Table 12.1, the entire population consists of a population of respondents and a population of non-respondents. If we were to draw a sample from the entire population using simple random sampling from the entire population, we would only be able to observe the respondents in the sample. In this case, if the respondent mean $\bar{y}_{R}$ is used to estimate the population mean,

$$
\begin{aligned}
\operatorname{Bias}\left(\bar{y}_{R}\right) & \doteq\left(1-\frac{N_{R}}{N}\right)\left(\bar{Y}_{R}-\bar{Y}_{M}\right) \\
\mathcal{V}\left(\bar{y}_{R}\right) & \doteq \frac{1}{n_{R}} S_{R}^{2}
\end{aligned}
$$

Here, two problems arise. One is that the estimate is biased. The only way the bias becomes zero is if the mean of the respondents and the mean of the nonrespondents become equal. The other problem is that the efficiency of the estimation decreases as the sample size decreases $\left(n_{R}<n\right)$. Compensating




---

for this bias and trying to regain lost efficiency is the goal of nonresponse adjustment.

# 12.2 Call-back 

When an investigator calls or conducts an interview, there are several sources for nonresponse. One is refusal, which declines to participate the survey. Another one is not-at-home or non-available at the time of survey. In these cases, one may need to resurvey a subset of the non-respondents reinterviewing a subset of non-respondents, which is often called follow-up survey or callback. The callback can be very effective in reducing non-response bias.

Suppose that we randomly select $\nu n_{M}$ units from the nonrespondents of size $n_{M}$, where $0<\nu<1$, to obtain the final sample, the final data set can be described as in Table 12.2.

TABLE 12.2 Data structure after a callback from nonrespondents

| Stratum | Population <br> size | Original sample |  | Final sample | Final sample |
| :--- | :---: | :---: | :---: | :---: | :---: |
|  |  | size | mean | size | mean |
| Respondents | $N_{R}$ | $n_{R}$ | $\bar{y}_{1}$ | $r_{1}=n_{R}$ |  |
| Nonrespondents | $N_{M}$ | $n_{M}$ |  | $r_{2}=\nu n_{M}$ | $\bar{y}_{2}$ |
| Population | $N$ | $n$ |  | $r$ |  |

If the original sample was selected by SRS, the final estimator of the final sample can be constructed as

$$
\hat{\bar{Y}}_{c b}=\frac{n_{R}}{n} \bar{y}_{1}+\frac{n_{M}}{n} \bar{y}_{2}
$$

Here, we also assume that $r_{2}=\nu n_{M}$ units are selected by SRS for callbacks. In this case, we can apply the theory of two-phase sampling for stratification in Section 11.2 to show that $\hat{\bar{Y}}_{c b}$ in (12.1) is design unbiased. Also, by (11.5), we obtain

$$
\operatorname{Var}(\hat{\bar{Y}})=\frac{1}{n}\left(1-\frac{n}{N}\right) S^{2}+\frac{W_{2} S_{2}^{2}}{n}\left(\frac{1}{\nu}-1\right)
$$

where $W_{2}=N^{-1} N_{M}$. In many practical situations, the second phase sample (which is the callback sample) has a higher survey cost than the original sample. Thus, the total cost can be written as

$$
C=c_{0} n+c_{1} W_{1} n+c_{2} W_{2} \nu n
$$




---

where $c_{1}$ is the unit-level survey cost for the original sample and $c_{2}$ is the unit-level survey cost for the callback sample.

Using (11.8), the optimal sampling rate for the callback sample is calculated as

$$
\nu^{*}=\sqrt{\frac{c_{0}+c_{1} W_{1}}{c_{2}} \times \frac{S_{2}^{2}}{S^{2}-W_{2} S_{2}^{2}}}
$$

The optimal sampling rate for the callback sample balances between the statistical efficiency and the cost efficiency.

# 12.3 Nonresponse weighting adjustment 

We now consider the case of unit nonresponse in survey sampling. Assume that $x_{i}$ is observed throughout the sample, and $y_{i}$ is observed only if $\delta_{i}=1$. We assume that the response mechanism does not depend on $y$. Thus, we assume that

$$
P(\delta=1 \mid \mathbf{x}, \mathbf{y})=P(\delta=1 \mid \mathbf{x})=p\left(\mathbf{x} ; \boldsymbol{\phi}_{0}\right)
$$

for some unknown vector $\boldsymbol{\phi}_{0}$. The first equality implies that the data are missing-at-random (MAR) in the sense of Rubin (1976) at the population level.

Given the response model (12.2), a consistent estimator of $\phi_{0}$ can be obtained by maximizing the pseudo log-likelihood function

$$
\ell_{p}(\boldsymbol{\phi})=\sum_{i \in A} \pi_{i}^{-1}\left[\delta_{i} \log \left\{p\left(\mathbf{x}_{i} ; \boldsymbol{\phi}\right)\right\}+\left(1-\delta_{i}\right) \log \left\{1-p\left(\mathbf{x}_{i} ; \boldsymbol{\phi}\right)\right\}\right]
$$

over the parameter space of $\boldsymbol{\phi}$. Note that $\hat{\boldsymbol{\phi}}$ obtained from (12.3) can be expressed as the solution to the following pseudo-score equation

$$
\hat{S}_{p}(\boldsymbol{\phi}) \equiv \sum_{i \in A} \frac{1}{\pi_{i}}\left\{\frac{\delta_{i}}{p\left(\mathbf{x}_{i} ; \boldsymbol{\phi}\right)}-1\right\} \mathbf{h}\left(\mathbf{x}_{i} ; \boldsymbol{\phi}\right)=\mathbf{0}
$$

where

$$
\mathbf{h}(\mathbf{x} ; \boldsymbol{\phi})=p(\mathbf{x} ; \boldsymbol{\phi}) \cdot \partial \operatorname{logit}\{p(\mathbf{x} ; \boldsymbol{\phi})\} / \partial \boldsymbol{\phi}
$$

Once $\hat{\boldsymbol{\phi}}$ is computed from (12.3) or (12.4), the propensity score (PS) estimator of $Y=\sum_{i=1}^{N} y_{i}$ is given by

$$
\hat{Y}_{\mathrm{PS}}=\sum_{i \in A_{R}} \pi_{i}^{-1}\left\{p\left(\mathbf{x}_{i} ; \hat{\boldsymbol{\phi}}\right)\right\}^{-1} y_{i}
$$

where $A_{R}=\left\{i \in A: \delta_{i}=1\right\}$ is the set of respondents. The following theorem presents the asymptotic properties of the PS estimator in (12.5).




---

Theorem 12.1. Assume that the response model (12.2) is correctly specified. Under some regularity conditions, the PS estimator in (12.5) satisfies

$$
\hat{Y}_{\mathrm{PS}}=\hat{Y}_{\mathrm{PS}, \ell}+O_{p}\left(n^{-1} N\right)
$$

where

$$
\begin{aligned}
\hat{Y}_{\mathrm{PS}, \ell} & =\sum_{i \in A} \pi_{i}^{-1} \mathbf{h}_{i}^{\prime} \mathbf{B}^{*}+\sum_{i \in A_{\mathrm{R}}} \pi_{i}^{-1} p_{i}^{-1}\left(y_{i}-\mathbf{h}_{i}^{\prime} \mathbf{B}^{*}\right) \\
\mathbf{B}^{*} & =\left\{\sum_{i=1}^{N} p_{i}^{-1}\left(1-p_{i}\right) \mathbf{h}_{i} \mathbf{h}_{i}^{\prime}\right\}^{-1} \sum_{i=1}^{N} p_{i}^{-1}\left(1-p_{i}\right) \mathbf{h}_{i} y_{i}
\end{aligned}
$$

$p_{i}=p\left(\mathbf{x}_{i} ; \boldsymbol{\phi}_{0}\right)$, and $\mathbf{h}_{i}=\mathbf{h}\left(\mathbf{x}_{i} ; \boldsymbol{\phi}_{0}\right)$
Proof. Write $\hat{Y}_{\mathrm{PS}}(\boldsymbol{\phi})=\sum_{i \in A_{\mathrm{R}}} \pi_{i}^{-1}\left\{p\left(\mathbf{x}_{i} ; \boldsymbol{\phi}\right)\right\}^{-1} y_{i}$ and define

$$
\hat{Y}_{\mathrm{B}}(\boldsymbol{\phi})=\hat{Y}_{\mathrm{PS}}(\boldsymbol{\phi})-\left\{\hat{S}_{p}(\boldsymbol{\phi})\right\}^{\prime} \mathbf{B}
$$

indexed by $\mathbf{B}$. Note that $\hat{Y}_{\mathrm{B}}(\hat{\boldsymbol{\phi}})=\hat{Y}_{\text {PS }}$ regardless of the choice of $\mathbf{B}$. If we can find $\mathbf{B}^{*}$ such that

$$
E\left\{\frac{\partial}{\partial \phi} \hat{Y}_{\mathrm{B}}\left(\boldsymbol{\phi}_{0}\right)\right\}=0
$$

at $\mathbf{B}=\mathbf{B}^{*}$, then, according to Randles (1982), the effect of estimating $\boldsymbol{\phi}$ can be safely ignored for the choice of $\mathbf{B}=\mathbf{B}^{*}$. Now, note that

$$
\frac{\partial}{\partial \phi}\left\{p\left(\mathbf{x} ; \boldsymbol{\phi}_{0}\right)\right\}^{-1}=-\frac{\left(1-p_{i}\right)}{p_{i}^{2}} \mathbf{h}\left(\mathbf{x} ; \boldsymbol{\phi}_{0}\right)
$$

where $p_{i}=p\left(\mathbf{x}_{i} ; \boldsymbol{\phi}_{0}\right)$. Thus, we have

$$
E\left\{\frac{\partial}{\partial \phi} \hat{Y}_{\mathrm{B}}\left(\boldsymbol{\phi}_{0}\right)\right\}=-\sum_{i=1}^{N} p_{i}^{-1}\left(1-p_{i}\right) \mathbf{h}_{i} y_{i}+\sum_{i=1}^{N} p_{i}^{-1}\left(1-p_{i}\right) \mathbf{h}_{i} \mathbf{h}_{i}^{\prime} \mathbf{B}
$$

Thus, Randles' condition in (12.8) is satisfied at $\mathbf{B}=\mathbf{B}^{*}$ in (12.7). Therefore, we have shown that

$$
\hat{Y}_{\mathrm{PS}}=\hat{Y}_{\mathrm{PS}}\left(\boldsymbol{\phi}_{0}\right)-\left\{\hat{S}_{p}\left(\boldsymbol{\phi}_{0}\right)\right\}^{\prime} \mathbf{B}^{*}+O_{p}\left(n^{-1} N\right)
$$

which proves (12.6).
Now, using the two-phase sampling theory, we can obtain that

$$
E\left(\hat{Y}_{\mathrm{PS}, \ell}\right)=Y
$$

and

$$
V\left(\hat{Y}_{\mathrm{PS}, \ell}\right)=V\left(\hat{Y}_{\mathrm{HT}}\right)+E\left\{\sum_{i \in A} \pi_{i}^{-2}\left(p_{i}^{-1}-1\right)\left(y_{i}-\mathbf{h}_{i}^{\prime} \mathbf{B}^{*}\right)^{2}\right\}
$$




---

where $p_{i}=p\left(\mathbf{x}_{i} ; \boldsymbol{\phi}_{0}\right)$.
We now discuss the estimation of the variance of the PS estimators of the form (12.5) where $\hat{p}_{i}=p_{i}(\hat{\boldsymbol{\phi}})$ is constructed to satisfy (12.4). By (12.6), we can write

$$
\hat{Y}_{\mathrm{PS}}=\sum_{i \in \mathcal{A}} d_{i} \eta_{i}\left(\boldsymbol{\phi}_{0}\right)+O_{p}\left(n^{-1} N\right)
$$

where

$$
\eta_{i}(\boldsymbol{\phi})=\mathbf{h}_{i}(\boldsymbol{\phi})^{\prime} \mathbf{B}^{*}+\frac{\delta_{i}}{p_{i}(\boldsymbol{\phi})}\left\{y_{i}-\mathbf{h}_{i}(\boldsymbol{\phi})^{\prime} \mathbf{B}^{*}\right\}
$$

To derive the variance estimator, we assume that the variance estimator $\hat{V}=$ $\sum_{i \in \mathcal{A}} \sum_{j \in \mathcal{A}} \Omega_{i j} q_{i} q_{j}$ satisfies $\hat{V} / V\left(\hat{q}_{\mathrm{HT}} \mid \mathcal{F}_{N}\right)=1+o_{p}(1)$ for some $\Omega_{i j}$ related to the joint inclusion probability, where $\hat{q}_{\mathrm{HT}}=\sum_{i \in \mathcal{A}} d_{i} q_{i}$ for any $q$ with a finite fourth moment.

To obtain the total variance, the reverse framework of Fay (1992), Shao and Steel (1999), and Kim et al. (2006) is considered. In this framework, the finite population is divided into two groups, a population of respondents and a population of nonrespondents, so the response indicator is extended to the entire population as $\mathcal{R}_{N}=\left\{\delta_{1}, \delta_{2}, \ldots, \delta_{N}\right\}$. Given the population, the sample $\mathcal{A}$ is selected according to a probability sampling design. Then, we have both respondents and nonrespondents in the sample $\mathcal{A}$. The total variance of $\hat{\eta}_{\text {HT }}=\sum_{i \in \mathcal{A}} d_{i} \eta_{i}$ can be written as

$$
V\left(\hat{\eta}_{\mathrm{HT}}\right)=E\left\{V\left(\hat{\eta}_{\mathrm{HT}} \mid \mathcal{R}_{N}\right)\right\}+V\left\{E\left(\hat{\eta}_{\mathrm{HT}} \mid \mathcal{R}_{N}\right)\right\}:=V_{1}+V_{2}
$$

The conditional variance term $V\left(\hat{\eta}_{\mathrm{HT}} \mid \mathcal{R}_{N}\right)$ in (12.11) can be estimated by

$$
\hat{V}_{1}=\sum_{i \in \mathcal{A}} \sum_{j \in \mathcal{A}} \Omega_{i j} \hat{\eta}_{i} \hat{\eta}_{j}
$$

where $\hat{\eta}_{i}=\eta_{i}(\hat{\boldsymbol{\phi}})$ is defined in (12.10) with $\mathbf{B}^{*}$ replaced by a consistent estimator such as

$$
\hat{\mathbf{B}}^{*}=\left(\sum_{i \in \mathcal{A}_{\mathrm{R}}} d_{i} \hat{p}_{i}^{-2}\left(1-\hat{p}_{i}\right) \hat{\mathbf{h}}_{i} \hat{\mathbf{h}}_{i}^{\prime}\right)^{-1} \sum_{i \in \mathcal{A}_{\mathrm{R}}} d_{i} \hat{p}_{i}^{-2}\left(1-\hat{p}_{i}\right) \hat{\mathbf{h}}_{i} y_{i}
$$

and $\hat{\mathbf{h}}_{i}=\mathbf{h}\left(\mathbf{x}_{i} ; \hat{\boldsymbol{\phi}}\right)$. The second term $V_{2}$ in (12.11) is

$$
\begin{aligned}
V\left\{E\left(\hat{\eta}_{\mathrm{HT}} \mid \mathcal{R}_{N}\right)\right\} & =V\left(\sum_{i=1}^{N} \eta_{i}\right) \\
& =\sum_{i=1}^{N} \frac{1-p_{i}}{p_{i}}\left(y_{i}-\mathbf{h}_{i}^{\prime} \mathbf{B}_{\mathrm{z}}\right)^{2}
\end{aligned}
$$

A consistent estimator of $V_{2}$ can be derived as

$$
\hat{V}_{2}=\sum_{i \in \mathcal{A}_{\mathrm{R}}} d_{i} \frac{1-\hat{p}_{i}}{\hat{p}_{i}^{2}}\left(y_{i}-\mathbf{h}_{i}^{\prime} \hat{\mathbf{B}}_{\mathrm{z}}\right)^{2}
$$




---

Therefore,

$$
\hat{V}\left(\hat{Y}_{\mathrm{PS}}\right)=\hat{V}_{1}+\hat{V}_{2}
$$

is consistent for the variance of the PS estimator defined in (12.5) with $\hat{p}_{i}=$ $p_{i}(\hat{\phi})$ satisfying (12.4), where $\hat{V}_{1}$ is in (12.12) and $\hat{V}_{2}$ is in (12.13). When the sampling fraction $n N^{-1}$ is negligible, that is, $n N^{-1}=o(1)$, the second term $V_{2}$ can be ignored and $\hat{V}_{1}$ is a consistent estimator of total variance. Otherwise, the second term $V_{2}$ should be taken into account so that a consistent variance estimator can be constructed as in (12.14).

# 12.4 Calibration weighting for nonresponse adjustment 

Let $\hat{Y}_{\mathrm{n}}=\sum_{i \in A} d_{i} y_{i}$ be any design-consistent estimator of $Y$ where $d_{i}$ can be either design weight or the calibration weight. Unfortunately, we cannot compute $\hat{Y}_{\mathrm{n}}$ due to nonresponse. Our goal is to construct the final weight $\omega_{i}$ in $A_{R}$ so that

$$
\hat{Y}_{\omega}=\sum_{i \in A_{R}} \omega_{i} y_{i}
$$

can be used to estimate $Y$. In addition to the response model in (12.2), we also consider the "working" superpopulation model

$$
y_{i}=\boldsymbol{x}_{i}^{\prime} \boldsymbol{\beta}+e_{i}
$$

with $\mathrm{E}\left(e_{i} \mid \boldsymbol{x}_{i}\right)=0$ and $\mathrm{V}\left(e_{i} \mid \boldsymbol{x}_{i}\right)=c_{i} \sigma^{2}$. By considering the two models, we can develop the final calibration weights that satisfy the double robustness property (Kim and Haziza, 2014). Note that, under (12.15), we can impose

$$
\sum_{i \in A_{R}} \omega_{i} \boldsymbol{x}_{i}=\sum_{i \in A} d_{i} \boldsymbol{x}_{i}
$$

as a calibration constraint incorporating the superpopulation model in (12.15). Note that

$$
\hat{Y}_{\omega}-\hat{Y}_{\mathrm{n}}=\left(\sum_{i \in A_{R}} \omega_{i} \boldsymbol{x}_{i}-\sum_{i \in A} d_{i} \boldsymbol{x}_{i}\right)^{\prime} \boldsymbol{\beta}+\left(\sum_{i \in A_{R}} \omega_{i} e_{i}-\sum_{i \in A} d_{i} e_{i}\right)
$$

The first term is zero when (12.16) is true. Also, the second term has zero expectation under the superpopulation model in (12.15). Therefore, as long as the superpopulation model (12.15) is correct and the MAR is maintained, then (12.16) is a sufficient condition for the unbiasedness of the resulting calibration estimator.




---

In addition, we include

$$
\sum_{i \in A_{R}} \omega_{i} \hat{p}_{i}^{-1} c_{i}=\sum_{i \in A} d_{i} \hat{p}_{i}^{-1} c_{i}
$$

to obtain consistency under the response model in (12.2), where $\hat{p}_{i}=p\left(\mathbf{x}_{i} ; \hat{\boldsymbol{\phi}}\right)$. To construct the objective function for optimization, we use

$$
Q(\boldsymbol{\omega})=\sum_{i \in A_{R}} d_{i}\left(\frac{\omega_{i}}{d_{i}}-1\right)^{2} c_{i}
$$

in the calibration problem. The final calibration weights can be obtained by minimizing (12.18) subject to (12.16) and (12.17). We also assume that $\lambda^{\prime} \mathbf{x}_{i}=$ $c_{i}$ for some $\lambda$ as in (9.8). Now, (9.8) and (12.16) imply that

$$
Q(\boldsymbol{\omega})=\sum_{i \in A_{R}} d_{i}^{-1} \omega_{i}^{2} c_{i}+\text { constant }
$$

Using Lagrange multiplier method, the solution to the optimization problem can be written as

$$
\hat{\omega}_{i}=\left(\sum_{i \in A} d_{i} \mathbf{z}_{i}\right)^{\prime}\left(\sum_{i \in A_{R}} d_{i} \mathbf{z}_{i} \mathbf{z}_{i}^{\prime} / c_{i}\right)^{-1} d_{i} \mathbf{z}_{i} / c_{i}
$$

where $\mathbf{z}_{i}^{\prime}=\left(\mathbf{x}_{i}^{\prime}, \hat{p}_{i}^{-1} c_{i}\right)$. Note that the final weight in (12.19 satisfies

$$
\sum_{i \in A_{R}} \hat{\omega}_{i} y_{i}=\sum_{i \in A} d_{i} \mathbf{z}_{i}^{\prime} \hat{\gamma}_{R}:=\hat{Y}_{\mathrm{reg}}
$$

where

$$
\hat{\gamma}_{R}=\left(\sum_{i \in A_{R}} d_{i} \mathbf{z}_{i} \mathbf{z}_{i}^{\prime} / c_{i}\right)^{-1} \sum_{i \in A_{R}} d_{i} \mathbf{z}_{i} y_{i} / c_{i}
$$

By construction of $\hat{\gamma}_{R}$,

$$
\sum_{i \in A_{R}} d_{i} \hat{p}_{i}^{-1}\left(y_{i}-\mathbf{z}_{i}^{\prime} \hat{\gamma}_{R}\right)=0
$$

which implies that

$$
\sum_{i \in A_{R}} \hat{\omega}_{i} y_{i} \cong \sum_{i \in A} d_{i} \mathbf{z}_{i}^{\prime} \gamma^{*}+\sum_{i \in A_{R}} d_{i} \hat{p}_{i}^{-1}\left(y_{i}-\mathbf{z}_{i}^{\prime} \gamma^{*}\right):=\hat{Y}_{\mathrm{PS}, \mathrm{reg}}
$$

where $\gamma^{*}$ is the probability limit of $\hat{\gamma}_{R}$. Using the argument in Theorem 12.1, we can show that $\hat{Y}_{\text {PS,reg }}$ is asymptotically unbiased under the assumption that the response model (12.2) is specified correctly. Therefore, double robustness of the calibration estimator can be established. The regression estimator in (12.20) was first proposed by Fuller et al. (1994).




---

# Bibliography 

Bankier, M. D. (1988). Power allocations: determining sample sizes for subnational areas. The American Statistician, 42:174-177.

Basu, D. (1971). An essay on the logical foundations of survey sampling, part 1. In Foundations of Statistical Inference, edited by V.P. Godambe and D.A. Sprott, pages 203-242. Holt, Reinhart and Winston.

Binder, D. A. (1983). On the variances of asymptotically normal estimators from complex surveys. International Statistical Reviews, 51:279-292.

Breidt, F. J., Claeskens, G., and Opsomer, J. D. (2005). Model-assisted estimation for complex surveys using penalised splines. Biometrika, 92:831-846.

Brewer, K. R. W. (1963). A method of systematic sampling with unequal probabilities. Australian journal of Statistics, 5:93-105.

Chao, M. T. (1982). A general purpose unequal probability sampling plan. Biometrika, 69:653-656.

Chen, X.-H., Dempster, A. P., and Liu, J. S. (1994). Weighted finite population sampling to maximize entropy. Biometrika, 81:457-469.

Cochran, W. (1946). Relative accuracy of systematic and stratified random samples for a certain class of populations. Annals of Mathematical Statistics, $17: 164-177$.

Dalenius, T. and Hodges, J. L. J. (1959). Minimum variance stratification. Journal of the American Statistical Association, 54:88-101.

Deming, W. E. and Stephan, F. F. (1940). On a least squares adjustment of a sampled frequency table when the expected marginal totals are known. Annals of Mathematical Statistics, 11:427-444.

Deville, J.-C. and Särndal, C.-E. (1992). Calibration estimators in survey sampling. Journal of the American statistical Association, 87(418):376-382.

Deville, J. C. and Särndal, C. E. (1992). Calibration estimators in survey sampling. Journal of the American Statistical Association, 87:376-382.

Deville, J. C., Särnndal, C. E., and Sautory, O. (1993). Generalized raking procedures in survey sampling. Journal of the American Statistical Association, 88:1013-1020.




---

Durbin, J. (1967). Design of multi-stage surveys for the estimation of sampling errors. Applied Statistics, 16:152-164.

Fay, R. E. (1992). When are inferences from multiple imputation valid ? In Proceedings of the Survey Research Methods Section, pages 227-232, Washington, DC. American Statistical Association.

Firth, D. and Bennett, K. E. (1998). Robust models in probability sampling. Journal of the Royal Statistical Society, Series B, 60:3-21.

Fuller, W. A. (1990). Analysis of repeated surveys. Survey Methodology, $16: 167-180$.

Fuller, W. A. (1998). Replication variance estimation for two-phase samples. Statistica Sinica, 8:1153-1164.

Fuller, W. A. (2002). Regression estimation for sample surveys. Survey Methodology, 28:5-23.

Fuller, W. A. (2009). Sampling Statistic. Wiley, Hoboken, NJ.
Fuller, W. A., Loughin, M. M., and Baker, H. D. (1994). Regression weighting in the presence of nonresponse with application to the 1987-1988 nationwide food consumption survey. Survey Methodology, 20:75-85.

Godambe, V. P. and Joshi, V. M. (1965). Admissibility and Bayes estimation in sampling finite populations, 1. Annals of Mathematical Statistics, $36: 1707-1722$.

Groves, R. M., Jr., F. J. F., Couper, M. P., Lepkowski, J. M., Singer, E., and Tourangeau, R. (2009). Survey Methodology. Wiley, 2nd edition.

Hájek, J. (1981). Sampling from a Finite Population. Marcel Dekker.
Hansen, M. H. and Hurwitz, W. N. (1943). On the theory of sampling from finite populations. The Annals of Mathematical Statistics, 14:333-362.

Horvitz, D. G. and Thompson, D. J. (1952). A generalization of sampling without replacement from a finite universe. Journal of the American Statistical Association, 42:663-685.

Kim, J. K. and Haziza, D. (2014). Doubly robust inference with missing data in survey sampling. Statistica Sinica, 24:375-394.

Kim, J. K., Navarro, A., and Fuller, W. A. (2006). Replication variance estimation for two-phase stratified sampling. Journal of the American Statistical Association, 101:312-320.

Kim, J. K. and Rao, J. N. K. (2012). Combining data from two independent surveys: A model-assisted approach. Biometrika, 99:85-100.




---

Kish, L. (1965). Survey Sampling. John Wiley \& Sons, Inc.
Krewski, D. and Rao, J. N. K. (1981). Inference from stratified samples: properties of the linearization, jackknife and balanced repeated replication methods. Annals of Statistics, 9:1010-1019.
Kruskal, W. and Mosteller, F. (1979). Representative sampling. I. nonscientific literature. International Statistical Review, 47:13-24.
Kwon, Y., Kim, J. K., and Qiu, Y. (2024). Debiased calibration estimation using generalized entropy in survey sampling. available at http://arxiv.org/abs/2404.01076.
Lahiri, D. B. (1951). A method of sample selection providing unbiased ratio estimates. Bulletin of the International Statistical Institute, 33:133-140.
McLeod, A. I. and Bellhouse, D. R. (1983). A convenient algorithm for drawing a simple random sample. Applied Statistics, 32:182-184.
Merkouris, T. (2004). Combining independent regression estimators from multiple surveys. Journal of the American Statistical Association, 99:1131-1139.
Montanari, G. E. and Ranalli, M. G. (2005). Nonparametric model calibration estimation in survey sampling. Journal of the American Statistical Association, 100(472):1429-1442.
Narain, R. D. (1951). On sampling without replacement with varying probabilities. Journal of the Indian Society of the Indian Society of Agricultural Statistics, 3:169-174.
Neyman, J. (1934). On the two different aspects of the representative method: The method of stratified sampling and the method of purposive selection. Journal of the Royal Statistical Society, 97:558-625.
Park, S. and Kim, J. K. (2019). Mass imputation for two-phase sampling. Journal of the Korean Statistical Society, 48:578-592.
Pea, J., Qualité, L., and Tillé, Y. (2007). Systematic sampling is a minimal support design. Computational Statistics and Data Analysis, 51:5591-5602.
Quenouille, M. H. (1956). Notes on bias in estimation. Biometrika, 43:353360 .
Raj, D. (1966). Some remarks on a simple procedure of sampling without replacement. Journal of the American Statistical Association, 61:558-625.
Randles, R. H. (1982). On the Asymptotic Normality of Statistics with Estimated Parameters. The Annals of Statistics, 10(2):462 - 474.
Rao, J. N. K. (1973). On double sampling for stratification and analytic surveys. Biometrika, 60:125-133.




---

Renssen, R, H. and Nieuwenbroek, N. J. (1997). Aligning estimates for common variables in two or more sample surveys. Journal of the American Statistical Association, 92:368-375.
Royall, R. M. and Cumberland, W. G. (1981). The finite-population linear regression estimator and estimators of its variance-an empirical study. Journal of the American Statistical Association, 76:924-930.
Rubin, D. B. (1976). Inference and missing data. Biometrika, 63(3):581-592.
Särndal, C., Swensson, B., and Wretman, J. (1992). Model Assisted Survey Sampling. Springer.
Särndal, C. E., Swensson, B., and Wretman, J. H. (1989). The weighted residual technique for estimating the variance of the generalized regression estimator of the finite population total. Biometrika, 76:527-537.
Sen, A. (1953). On the estimate of the variance in sampling with varying probabilities. Journal of the Indian Society of Agricultural Statistics, 5:119127.

Shao, J. and Steel, P. (1999). Variance estimation for survey data with composite imputation and nonnegligible sampling fraction. Journal of the American Statistical Association, 94:254-265.
Shao, J. and Tu, D. (1995). The Jackknife and Bootstrap. Springer-Verlag, New York.
Sitter, R. R. (1997). Variance estimation for the regression estimator in twophase sampling. Journal of the American Statistical Association, 92:780787 .

Statistics Canada (2003). Survey Methods and Practices. Available at "http://www.statcan.gc.ca/pub/12-587-x/12-587-x2003001-eng.pdf".
Sunter, A. B. (1977). List sequential sampling with equal or unequal probabilities without replacement. Applied Statistics, 26:261-268.
Tillé, Y. (2006). Sampling Algorithms. Springer-Verlag, New York.
Tillé, Y. (2020). Sampling and estimation from finite populations. Wiley.
Tillé, Y. and Matei, A. (2016). Sampling: Survey Sampling. R package version 2.8.

Tsiatis, A. A. (2006). Semiparametric Theory and Missing Data. Springer.
Tukey, J. W. (1958). Bias and confidence in not quite large samples. The Annals of Mathematical Statistics, 29:614-623.




---

Vitter, J. S. (1985). Random sampling with a reservoir. ACM Transactions on Mathematical Software, 11:37-57.

Wolter, K. M. (1984). An investigation of some estimators of variance for systematic sampling. Journal of the American Statistical Association, 79:781790 .

Wolter, K. M. (2007). Introduction to Variance Estimation. Springer-Verlag, New York, 2 edition.

Wright, T. (2012). The equivalence of neyman optimum allocation for sampling and equal proportions for apportioning the u.s. house of representatives. The American Statistician, 66:217-224.

Wu, C. and Sitter, R. R. (2001). A model-calibration approach to using complete auxiliary information from survey data. Journal of the American Statistical Association, 96(453):185-193.

Yates, F. and Grundy, P. (1953). Selection without replacement from within strata with probabilities proportion to size. Journal of the Royal Statistical Society, Series B, 15:235-261.




---

