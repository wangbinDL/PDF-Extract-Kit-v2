# A systematic database of thin-film measurements by EPMA 

## Part I - Aluminum films

G. F. Bastin* and H. J. M. Heijligers<br>Laboratory of Solid State and Materials Chemistry, University of Technology, P.O. Box 513, NL-5600 MB Eindhoven, The<br>Netherlands


#### Abstract

A systematic database of thin-film measurements on aluminum films by electron probe microanalysis is presented. The measurements were performed between 3 and 30 kV accelerating voltage on films of six different nominal thicknesses, ranging from 100 up to $3200 \AA$, which were deposited simultaneously on 20 different substrates, ranging between Be and Bi . The purpose of this work was to provide systematic data on which existing and future thin-film analysis programs can be tested. A total of 1060 k ratios for the film element Al were collected and 872 k ratios for the various substrate elements from underneath the films. Tests with our own most recent thin-film analysis program, TFA, based on the double Gaussian PROZA96 procedure, on this database showed excellent performance: a mean value of 1.0093 for $\bar{k}_{\text {calc }} / \bar{k}_{\text {meas }}$ and a relative root-mean-square deviation of $4.2457 \%$ in the histogram for the film element. Copyright (C) 2000 John Wiley \& Sons, Ltd.


## INTRODUCTION

The purpose of thin-film correction procedures in electron probe microanalysis (EPMA) is to convert the measured x-ray intensities from film (and/or substrate) elements into the correct thickness and composition of a film on a substrate. It will be obvious that this conversion can only be made correctly if it is exactly known where the x-rays are being produced as a function of depth in the specimen. This knowledge is commonly presented in terms of socalled $\Phi(\rho z)$ curves, in which $\Phi$ represents the number of x-ray photons produced and $\rho z$ the mass depth (product of density $\rho$ and linear depth $z$ ).

Although the correct analytical description of $\Phi(\rho z)$ curves in pure bulk elements and compounds over a wide range in experimental conditions is difficult enough in itself, it appears that a number of modern $\Phi(\rho z)$ models ${ }^{1-7}$ are very successful in this respect. This can be judged from their impressive performance on the most difficult analytical cases, e.g. the bulk analysis of the ultra-light elements $\mathrm{B}, \mathrm{C}, \mathrm{N}$ and $\mathrm{O} .{ }^{3-8}$

Nevertheless, a typical example of bulk analysis in specimens which are supposed to be homogeneous in depth must be considered as relatively simple compared with cases of thin-film analysis where the geometry is much more complex, and where hard discontinuities exist at the interfaces between film(s) and substrate. The question arises, therefore, of how the x-ray generation as a function of mass depth should be described analytically for each of the elements in a film-substrate combination,

[^0]in the case that such discontinuities are present at each of the interfaces.

A number of approaches have been presented in the literature to deal with this problem. These are either based on (semi-)empirical approaches, ${ }^{9-15}$ in which the $\Phi(\rho z)$ curves of each of the film elements are modified empirically according to the specific film-substrate combination at hand, or on more fundamental approaches using Monte Carlo procedures. ${ }^{16,17}$

In a number of previous papers ${ }^{18-20}$ on the subject, we have given a general outline of the approach we developed in our own analytical description of $\Phi(\rho z)$ curves for the elements in a film-substrate combination, and the description of this procedure will briefly be repeated here.

The simplest case of a thin film-substrate combination that can be conceived is that of two neighbouring elements in the periodic system. Since the processes of electron scattering and deceleration and those of x-ray generation will be virtually the same in both elements, the $\Phi(\rho z)$ curves for film and substrate elements will be almost identical. As a result, either of them could be used to calculate the generated and emitted intensities from film and substrate elements by partial integration between the appropriate limits. This simple approximation is known to work well as long as the difference in atomic number between film and substrate element does not exceed, say, $3-4$ units. With increasing difference in atomic number the difference in electron scattering properties between film and substrate elements becomes noticeable and the x-ray production in the film can be influenced substantially. If the substrate element is heavier, then the x-ray production in the film will be increased, and vice versa. Therefore, a correction has to be applied in order to deal with such differences.


[^0]:    * Correspondence to: G. F. Bastin, Laboratory of Solid State and Materials Chemistry, University of Technology, P.O. Box 513, NL-5600 MB Eindhoven, The Netherlands.



weighting laws that are supposed to weight the various contributions over the relevant mass depth region down to $R_{\mathrm{x}}$. Since $R_{\mathrm{x}}$ is not known either, it is necessary to start an iterative procedure to arrive at the final $\alpha$ value and, hence, $R_{\mathrm{x}}$. The first (crude) estimate for $R_{\mathrm{x}}$ is obtained by averaging the constituent $\left(\left(\rho_{\mathrm{zM}}+2.5\right) \alpha_{\mathrm{i}}\right)$ values in the bulk of the film and the substrate, and this mean value can then be used to generate a first estimate for $R_{\mathrm{x}}$. Next, a more accurate weighting procedure is started, in which the weight $(p)$ of each contribution as a function of mass depth ( $\rho z$ ) is described by a fourth-degree polynomial:

$$
p(\rho z)=N(\rho z-L)^{2}(\rho z-R)^{2}
$$

where $L$ and $R$, which are both functions of $R_{x}$ only, are the double roots on the left- and right-hand sides of the polynomial, and $N$ is a normalization factor that ensures the normalization under the $p(\rho z)$ curve. In fact, this weighting procedure is a variant to the one first used by Pouchou and Pichoir. ${ }^{9}$ However, these authors used the polynomial weighting procedure in order to generate sets of fictitious bulk compositions, one set for each $\phi(\rho z)$ parameter, from which all necessary $\phi(\rho z)$ parameters in their double-parabolic model for each particular element in the film-substrate combination were subsequently calculated. In our approach, on the other hand, the weighting is much more direct since we use the basic Gaussian parameters in a straightforward way.
In the iterative procedure for the determination of $R_{\mathrm{x}}$, the roots used are $-0.4 R_{\mathrm{x}}$ for $L$ and $R_{\mathrm{x}}$ for $R$. Using these roots, a new value for $R_{\mathrm{x}}$ is calculated by integration over the $p$ function [Eqn (1)]. The resulting value is normalized by dividing it by the integral of $p(\rho z)$ between 0 and $R$. The newly obtained $R_{x}$ value is now compared with the previous one, and if the relative deviation is smaller than, say, $0.1 \%$, the iteration procedure is stopped. If not, the latest $R_{\mathrm{x}}$ value is used to generate new $L$ and $R$ values, and the weighting procedure is repeated until convergence is obtained. This is usually the case in less than three cycles.
Table 1. Double roots for the Gaussian parameters

| Parameter | $L$ | $R$ |
| :--- | :--- | ---: |
| $\alpha$ | $-0.3 R_{\mathrm{x}}$ | $R_{\mathrm{x}}$ |
| $\rho_{\text {zm }}$ | $-0.9 R_{\mathrm{x}}$ | $0.7 R_{\mathrm{x}}$ |
| $\Phi_{\mathrm{I}}$ | $-0.8 R_{\mathrm{x}}$ | $R_{\mathrm{x}}$ |
| $\phi(0)$ | $-0.5 R_{\mathrm{x}}$ | $0.5 R_{\mathrm{x}}$ |

The last problem that has to be solved is to find the $L$ and $R$ values, which apply to the weighting procedures aimed at finding the four independent Gaussian parameters, necessary to describe the $\phi(\rho z)$ curves for each of the elements in the film-substrate combination. These roots will be different for each of the Gaussian parameters. Provisional settings were found originally by a process of optimization on the (often conflicting) thin-film data from the literature. Later, these settings were fine-tuned by using our own databases, of which the present one on aluminum films is an example. It must be emphasized, however, that this fine-tuning process is merely necessary to find the proper translation from the old to the new model, where different parameters with their different meanings are involved. It is not possible to 'optimize' a vast database of measurements with the relatively few parameters at hand, certainly not if the experimental conditions vary widely, as in the present case.

The double roots for the four Gaussian parameters can be summarized as in Table 1. It is clear from this table that more weight is assigned to the deeper regions in the specimen as far as $\alpha$ is concerned, whereas $\phi(0)$ is mainly governed by the near-surface regions. Regarding the latter parameter, it is assumed that electrons scattered back from regions deeper than $0.5 R_{\mathrm{x}}$ will not be able to make it back to the surface and, consequently, cannot contribute to $\phi(0)$.

Once the Gaussian parameters for each of the elements in the film have been obtained, the emitted intensities can be calculated by partial integration; ${ }^{6}$ those for the film elements between the $\rho z$ limits of zero and $T$ (the film thickness) and for the substrate elements from $T$ down to infinity. Appropriate corrections for absorption have, of course, to be made. Taking the ratios to the intensities emitted from the bulk standards will finally give the calculated $k$ ratios which have to be compared with the measured values. This is, in short, the procedure followed in the present work. Normally, one would try to operate such a thin-film program the other way around, i.e. try to determine the thickness and/or composition of a film from measured $k$ ratios. Full details of this procedure can be found in one of our previous publications. ${ }^{20}$

## EXPERIMENTAL

Aluminum films of six different nominal thicknesses (10, $20,40,80,160$ and 320 nm ) were deposited by vacuum evaporation on to polished pieces of 20 different substrate elements, ranging from Be to Bi , mounted in a single specimen mount. In order to avoid problems with simultaneously polishing materials with largely different hardnesses, small pieces of all substrate elements were mounted separately first in copper-filled mounting resin and polished carefully. Next, small rectangular blocks of mounting resin, each containing a polished substrate specimen, were cut out and remounted together to produce the final assembly of 20 polished substrate elements. In total, six such substrate assemblies were manufactured in order to accommodate six different film thicknesses.
During each vacuum deposition run, identical films were also deposited on crystals of rock salt and Si wafers. The former specimens were to be used for independent determination of the film thicknesses by Rutherford backscattering spectroscopy (RBS), whereas the latter served incidentally for transmission electron microscopy (TEM) investigations of cross-sections.
The films deposited on rock salt could be lifted off easily by dissolving the salt in water. These specimens, when picked up on a TEM grid, were eminently suited to perform intensity measurements on unsupported films. In combination with the measurements on the same films on a variety of substrates, this provided the experimental possibility of accessing the surface ionization value $\phi(0)$ by a process of extrapolation towards a film thickness of zero. This will be the subject of a future paper.
The microprobe measurements on the film (Al) and the substrate elements were carried out at accelerating



voltages between 3 and 30 kV , using JEOL 733 and 8600 electron probe microanalyzers. Both instruments have x ray take-off angles of $40^{\circ}$.

## RESULTS

Establishing the real thicknesses of the films turned out to be a major problem; therefore, our primary efforts were concerned with this task. To begin with, there were only two really independent sources of information: RBS (carried out at Philips Research Laboratories, Eindhoven, The Netherlands) and Monte Carlo calculations. ${ }^{17}$ In the latter approach the mass thicknesses are determined by iterative procedures, in which the results of the simulations are compared with the experimental measurements. The results obtained by the two techniques differed markedly, as can be judged from Table 2.
Assuming a bulk density of $2.70 \mathrm{~g} \mathrm{~cm}^{-3}$ for aluminum, the mass thicknesses aimed at would be $2.70,5.40,10.80$, $21.60,43.20$, and $86.40 \mu \mathrm{g} \mathrm{cm}^{-2}$. It is clear that, e.g., RBS finds much larger thicknesses for the three thinner films, whereas for the thicker films increasingly lower film thicknesses are found. With the Monte Carlo method, very much larger thicknesses are found than either the nominal or the RBS values over the full range.

The following remarks can be made concerning Table 2, where the paragraph letters below correspond to the footnote letters in the table.
(a) The Monte Carlo program, using the measured $k$ ratios for $\mathrm{Al} \mathrm{K} \alpha$, was found to produce a consistent variation of $20 \%$ in the mass thicknesses between 3 and 30 kV , starting low and ending high, for both substrates. However, the results for a specific fixed voltage were virtually independent of the atomic number of the substrate, which must be considered as a remarkably good achievement. The mean results over the voltage range have been reported here.
(b) The GMR film program is the computer program written by Waldo. ${ }^{13,22}$ We used the option in this program which is entirely based on the PAP9 (doubleparabolic) procedure. This program was found to produce up to $14 \%$ variation in mass thicknesses on going

Table 2. Aluminum films: reported values are mass thicknesses in $\mu \mathrm{g} \mathrm{cm}{ }^{-2}$

| Nominal | Monte Carlo $^{a}$ |  | GMR $^{\text {b }}$ |  | TFA $^{\mathrm{c}}$ |  | Databased |
| :--- | :--- | :---: | :--- | :--- | :--- | :--- | :--- |
|  | On Be | On Bi <br> program on | Ti |  |  | film on |  |
|  |  |  |  |  |  | Ti |  |
| 2.70 | 3.27 | 3.57 | 3.47 |  | 3.58 | 3.62 | 3.55 |
| 5.40 | 6.14 | 7.20 | 6.96 |  | 6.95 | 7.06 | 7.04 |
| 10.80 | 11.96 | 14.26 | 13.66 |  | 13.69 | 13.95 | 13.80 |
| 21.60 | 21.86 | 24.99 | 24.92 |  | 25.04 | 25.56 | 24.90 |
| 43.20 | 39.46 | 48.84 | 49.23 |  | 48.54 | 49.84 | 49.20 |
| 86.40 | 81.97 | 88.90 | 88.07 |  | 84.66 | 87.11 | 85.40 |

${ }^{\text {a-d }}$ See the corresponding paragraphs (a)-(d) in the text.
(c) The TFA program, based on our own modification ${ }^{2}$ of the surface-centered Gaussian Packwood/Brown approach, ${ }^{1}$ is a predecessor to our present thin-film analysis program. Its results varied by less than $5 \%$ between a Be and a Bi substrate and the results as a function of voltage were satisfactory. As was the case with the GMR program, the results calculated for a Ti substrate are presented here. It is clear that the results from the GMR and TFA programs do not show pronounced differences. In addition, they both show fair agreement with the mean results of the Monte Carlo program, contrary to the RBS results in many cases.
(d) The last column in Table 2 represents the mass thicknesses which were finally adopted in our database. The values are very close to the mean numbers in the other columns.
It is remarkable that, with none of the techniques used, the expected ratio in the mass thicknesses of $1: 2: 4: 8: 16: 32$, which was aimed at during the preparation of the films and which was supposed to be easy to achieve, was in fact attained. With RBS the ratios obtained were $1: 1.88: 3.66: 6.69: 12.07: 25.07$ and with Monte Carlo (mean) $1: 2.01: 3.97: 7.09: 13.94: 25.14$. With the EPMA programs GMR film and TFA sequences of $1: 1.94: 3.82: 6.99: 13.56: 23.65$ and $1: 1.95: 3.85: 7.06$ : $13.77: 24.06$ were calculated, respectively.

In an isolated case (nominal $800 \AA$, or $21.60 \mu \mathrm{g} \mathrm{cm}^{-2}$ ), a film on NaCl was investigated in a cross-section in the transmission electron microscope (JEOL 2000 FX). Thicknesses corresponding to $25 \mu \mathrm{g} \mathrm{cm}^{-2}$ (assuming the bulk density for Al ) and slightly higher were thereby found, thus corroborating the Monte Carlo and EPMA (GMR and TFA) results, rather than the RBS data. Apparently, it is extremely difficult to find the 'true' film thicknesses. However, we want to emphasize most strongly that, even if the true film thicknesses will presumably never be known with $100 \%$ certainty, the measurements on such (our present) specimens are still extremely useful because it can safely be assumed that the same mass thickness applies to each of the various substrates.

The EPMA measurements for $\mathrm{Al} \mathrm{K} \alpha$ were carried out as a function of atomic number of the substrate, starting with Be and ending with Bi for each specific accelerating voltage. After calibration of the $\mathrm{Al} \mathrm{K} \alpha$ peak with a TAP analyzer crystal on the Al bulk standard, a minimum of 10 intensity measurements were performed in each case and the mean $k$ ratio was used as the entry in the final database. This measuring procedure has the specific advantage of disclosing immediately any erratic behavior in the variation of the intensity of the $\mathrm{Al} \mathrm{K} \alpha$ peak with atomic number of the substrate, a variation which must be assumed to be smooth. Moreover, one would expect the signal to increase monotonically with the atomic number of the substrate. Any sudden increase in the signal might point to a case of fluorescence, e.g. if the Al film is on a Si substrate.

Figure 1 shows some of the results which can typically be obtained in the measurements as a function of atomic number of the substrate at an accelerating voltage of 15 kV for the films with nominal thicknesses of 100 (top) and $400 \AA$ (bottom).

Figure 2 shows similar results, but now for the film with a nominal thickness of $800 \AA$, at accelerating voltages of 20 (top) and 25 kV (bottom).





Figure 1. Variation of the $k$ ratios for $\mathrm{Al} \mathrm{K} \alpha$ as a function of the atomic number of the substrate at 15 kV . Top, nominal thickness $100 \AA$, assumed mass thickness $3.55 \mu \mathrm{g} \mathrm{cm}^{-2}$; bottom, nominal thickness $400 \AA$, assumed mass thickness $13.80 \mu \mathrm{g} \mathrm{cm}^{-2}$. Solid circles represent the measurements and the broken curves show the predictions of the TFA program. X-ray take-off angle, $40^{\circ}$.

It is evident from these results that remarkable agreement exists between the measurements and the calculations and that, in general, measurements with a smooth variation can indeed be obtained. The only case where noticeable and persistent deviations exist is where a silicon substrate $(Z=14)$ is involved, and this must be attributed to fluorescence.

Since the $\mathrm{Al} K \alpha$ intensities emitted from the films are a function not only of the atomic number of the substrate, but also of that of the applied accelerating voltage, it is meaningful to present the results also as a function of the accelerating voltage for the six films for a fixed substrate. This is done in Fig. 3 for the beryllium (top) and titanium (bottom) substrates and in Fig. 4 for the molybdenum (top) and tungsten (bottom) substrates. Again, the agreement between measurements and calculations is remarkably good.
In view of the huge number of measured data collected in the present investigation ( $1060 k$ ratios for $\mathrm{Al} \mathrm{K} \alpha$ from the film element and 872 k ratios from the substrate elements), it is impossible to judge the overall performance of the present TFA program (or any other thin-film program, for that matter) by mere inspection of a relatively small number of graphical representations of the measured and calculated results. We chose, therefore, an approach



Figure 2. Variation of the $k$ ratios for $\mathrm{Al} \mathrm{K}_{\alpha}$ as a function of the atomic number of the substrate for an aluminum film of nominal thickness $800 \AA$, assumed mass thickness $24.90 \mu \mathrm{g} \mathrm{cm}^{-2}$. Top, at 20 kV ; bottom, at 25 kV . Solid circles represent the measurements and the broken curves show the predictions of the TFA program. X-ray take-off angle, $40^{\circ}$.
which is commonly used in tests on the performance of bulk correction programs. In this approach the $k$ ratio $\left(k^{\prime}\right)$ for the given entry in the database under the specific experimental conditions is calculated and compared with the measured value ( $k$ ). The ratio $k^{\prime} / k$ is then displayed in a histogram, showing the number of analyses vs the value of $k^{\prime} / k$, and the narrowness of the histogram (in terms of the relative root-mean-square value in \%), together with the mean value of the distribution are then used as a final measure of success. Figure 5 shows the results which were obtained in the present case. The results must be regarded as excellent, certainly if one takes into consideration that in a number of cases (which have still been included in the final database) the experimental conditions for thin-film analysis are not suitable at all. Examples of these cases are when the accelerating voltage for a given film thickness is simply too low, so that the $\Phi(\lambda)$ curve for the film element barely touches on the substrate. It is evident that the results could become very much better if such cases were eliminated from the database.

As mentioned before, a wide variety of substrate elements was also measured from underneath the films. All possible x-ray lines that could be excited were measured





Figure 3. Variation of the $k$ ratios for $\mathrm{Al} \mathrm{K} \alpha$ as a function of accelerating voltage for the six aluminum films of nominal thicknesses ranging between 100 and $3200 \AA$. Top, for a beryllium substrate; bottom, for a titanium substrate. Symbols represent the measurements and the broken curves show the predictions of the TFA program. X-ray take-off angle, $40^{\circ}$.
and the $k$ ratios were also included in one large data file. Figure 6 shows the results obtained for the silicon (top) and titanium (bottom) substrates, and Fig. 7 gives similar results for the much heavier germanium (top) and molybdenum (bottom) substrates. Again, it appears evident that satisfactory agreement is obtained between calculations and measurements, with very few exceptions. The latter are connected again with those cases where the conditions for thin-film analysis are unsuitable: when the accelerating voltage for the film thickness at hand is low and the $\Phi(\rho z)$ curve hardly extends into the substrate. The results of the overall statistical analysis for the substrate elements, similar to the one performed before for the film element, are shown in Fig. 8. After the elimination of the results obtained under totally unsuitable experimental conditions, most satisfactory mean $k^{\prime} / k$ (1.0125) and r.m.s. values ( $3.6670 \%$ ) are obtained. Full details of the complete database can be found in the Appendix and/or are available from the authors.



Figure 4. Variation of the $k$ ratios for $\mathrm{Al} \mathrm{K} \alpha$ as a function of accelerating voltage for the six aluminum films of nominal thicknesses ranging between 100 and $3200 \AA$. Top, for a molybdenum substrate; bottom, for a tungsten substrate. Symbols represent the measurements and the broken curves show the predictions of the TFA program. X-ray take-off angle, $40^{\circ}$.



Figure 5. Histogram obtained with the TFA thin-film program on $1060 \mathrm{Al} \mathrm{K} \alpha$ analyses, measured between 3 and 30 kV , from aluminum films of six different mass thicknesses. The number of analyses is displayed $v s$ the ratio $k^{\prime} / k$ between the calculated ( $k^{\prime}$ ) and the measured $k$ ratio $(k)$.





Figure 6. Variation of the $\lambda$ ratios for the substrate elements as a function of accelerating voltage from underneath the six aluminum films of nominal thicknesses ranging between 100 and $3200 \AA$. Top, silicon substrate; bottom, titanium substrate. Symbols represent the measurements and the broken curves show the predictions of the TFA program. X-ray take-off angle, $40^{\circ}$.

## DISCUSSION

The results presented in this paper clearly show that accurate analysis of thin films over a wide range of experimental conditions is possible, especially if the accelerating voltage used in the measurements is suitable for the specific film thickness at hand. In all cases it is advisable to apply a sufficiently high voltage so that the $\Phi(\Psi z)$ curve of the film element extends relatively deep into the substrate. In other words, the mass thickness of the film should represent only a minor fraction of the total range of $\Phi(\Psi z)$.

As Figs 1 and 2 indicate, the calculations of the intensities emitted from a film with given mass thickness for a wide variety of substrates closely follow the measurements. This means that if the TFA program were to be used the other way around, virtually constant thicknesses would be found, irrespective of the atomic number of the substrate. This is, of course, one of the two major goals mentioned in the Introduction.



Figure 7. Variation of the k ratios for the substrate elements as a function of accelerating voltage from underneath the six aluminum films of nominal thicknesses ranging between 100 and $3200 \AA$. Top, germanium substrate; bottom, molybdenum substrate. Symbols represent the measurements and the broken curves show the predictions of the TFA program. X-ray take-off angle, $40^{\circ}$.

The other major goal was that the calculations would closely follow the measurements as a function of accelerating voltage for a given film thickness on a specific substrate. The success of these calculations can be judged from Figs 3 and 4 for a small selection of substrates, ranging from Be to Bi. The only noticeable deviations can be found in cases where the conditions are not suitable: low accelerating voltage, heavy substrate, e.g. W, and thick film (Fig. 4, bottom). If such results were to be excluded from the histogram in Fig. 5, then, of course, very much improved results could be obtained.

The fact that the mean $\lambda_{0} / \lambda$ value comes out closely around 1.0 means, of course, nothing else than that the $\lambda$ ratios that we calculate agree closely with those expected from the mass thicknesses adopted in Table 2. If one were to insist on adopting the RBS values, then systematic shifts in the centering of the histogram would be observed. What we consider of much more importance, however, is the narrowness in the histogram, which reflects the ability of the program to yield a remarkably consistent





Figure 8. Histogram obtained with the TFA thin-film program on 872 substrate element analyses, measured between 3 and 30 kV , from underneath the aluminum films of six different mass thicknesses. The number of analyses is displayed $v$ s the ratio between the calculated $\left(k^{0}\right)$ and the measured $k$ ratio ( $k$ ). The reported mean $k^{0} / k$ and r.m.s. values apply to only 829 analyses because the statistical flyers have been accumulated in the two bars at $k^{0} / k=0.75$ ( 7 analyses with $k^{0} / k<0.80$ ) and $k^{0} / k=1.25$ ( 36 analyses with $k^{0} / k>1.20$ ), and have been excluded from the final evaluation.
mass thickness over a wide range of atomic numbers of the substrates and a large range in accelerating voltage.

Any statement about a systematic error requires an exact knowledge about the true 'reference' value, which will presumably never be known.

As far as the substrate elements are concerned, similar remarks apply as in the case of the film element: low accelerating voltages for relatively thick films should be avoided, although, surprisingly, there are also problems sometimes with the thinnest films, for no good reason (Figs 6 and 7). Obviously, it can be difficult enough to measure $k$ ratios which differ only very slightly from unity. This observation, in conjunction with the fact that the slightest deviation in the substrate $k$ ratio can produce a large deviation in the mass thickness of the film if the program is run the other way around, can make it somewhat tricky to use the measured $k$ ratio of the substrate element exclusively in order to find the mass thickness of the film. In all cases much more weight should be assigned to the signals emitted by the film elements; after all, the emitted film signals are more or less directly proportional to the film thickness.

## REFERENCES

1. Packwood RH, Brown JD. X-Ray Spectrom. 1981; 10: 138.
2. Bastin GF, van Loo FJJ, Heijligers HJM. X-Ray Spectrom. 1984; 13: 91.
3. Bastin GF, Heijligers HJM. In Electron Probe Quantitation, Workshop at the National Bureau of Standards, Gaithersburg, Maryland, 1988, Heinrich KFJ, Newbury DE (eds). Plenum Press: New York, 1991; 145-161.
4. Pouchou JL, Pichoir F. Rech. Aérospat. 1984; 3: 13.
5. Pouchou JL, Pichoir F, Boivin D. (a) Proceedings of 12th ICXOM, 28 Aug-1 Sep 1989, Cracow, Poland. Jasienska S, Maksymowicz LJ (eds). Cracow Academy of Mining and Metallurgy, 1990; 52; (b) Further Improvements in Quantitation Procedures for X-ray Microanalysis, ONERA Report TP 157, 1989.
6. Bastin GF, Dijkstra JM, Heijligers HJM. X-Ray Spectrom. 1998; 27: 3.
7. Merlet C. Inst. Phys. Conf. Ser. 1992; No. 130; 123.
8. Bastin GF, Heijligers HJM. Scanning 1990; 12: 225.
9. Pouchou JL, Pichoir F. Rech. Aérospat. 1984; 5: 349.
10. Packwood RH, Milliken KS. A general equation for predicting x-ray intensitites from stratified samples in the electron microprobe, CANMET Report No. PMRL/85-25 (TR), May 1985.
11. August H-J, Wernisch J. Scanning 1987; 9: 145.
12. Hunger H-J. Scanning 1988; 10: 65.
13. Waldo RA. In Microbeam Analysis, Newbury DE (ed). San Francisco Press: San Francisco, 1988; 310-314.
14. Willich P, Obertop D. Surf. Interface Anal. 1988; 13: 20.
15. Willich P, Obertop D. J. Phys. Colloque 1989; C-5: 285.
16. Kyser DF, Murata K. In Proceedings of a Workshop on the Use of Monte Carlo Calculations in Electron Probe Microanalysis and Scanning Electron Microscopy. Heinrich KFJ, Newbury DE, Yakowitz H (eds). NBS Special Publication No. 460. National Bureau of Standards: Washington, DC, 1976; 129-138.
17. Ammann N. Thesis MS, R. W. T. H. Aachen, 1989.
18. Bastin GF, Heijligers HJM, Dijkstra JM. In Proceedings of the XIIth International Congress for Electron Microscopy, Seattle (Washington, USA), August 1990, Peachey LD, Williams DB (eds). San Francisco Press: San Francisco, 1990; 216.
19. Bastin GF, Dijkstra JM, Heijligers HJM. In Proceedings of the 50th Annual Meeting of the Electron Microscopy Society of America/27th Annual Meeting of the Microbeam Analysis Society/19th Annual Meeting of the Microscopical Society of Canada, Baily GW, Bentley J, Small JA (eds). San Francisco Press: San Francisco, 1992; 1648.
20. Bastin GF, Dijkstra JM, Heijligers HJM, Klepper D. Microbeam Anal. 1993; 2: 29-43.
21. Pouchou JL, Pichoir F. In Proceedings of the 11th International Congress on X-Ray Optics and Microanalysis, Brown JD, Packwood RH (eds). Graphic Services, UWO: London, Canada, 1986; 249.
22. Waldo RA. In Microbeam Analysis, Howitt DE (ed). San Francisco Press: San Francisco, 1991; 45-53.

## APPENDIX

Data file for aluminum films (take-off angle $40^{\circ}$ ). Substrate line: $\mathrm{K}=0 ; \mathrm{L}=1 ; \mathrm{M}=2$
Mass thickness
Accelerating
No. $\quad \mathrm{Z}_{\text {substrate }} \quad\left(\mu \mathrm{g} \mathrm{cm}^{-2}\right) \quad k\left(\mathrm{Al} \mathrm{K} \alpha\right) \quad k$ (substrate) voltage $(\mathrm{kV})$ Substrate line
143.550.18981 — 30
$243.550 .09317$ -
4
2
43.550 .03595 - 6
43.550.01986 - 8
43.550 .01277 - 10
643.550 .00872 - 12
$743.550 .00566$ - 15















|  | Mass thickness <br> $\left(\mu \mathrm{g} \mathrm{cm}^{-2}\right)$ | Accelerating <br> voltage $(\mathrm{kV})$ | No. | Zsubstrate | Substrate line | $k\left(\mathrm{Al} \mathrm{K} \alpha\right.$ ) | $k$ (substrate) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 212 | 14 | 85.40 | 0.07394 | 0.62524 | 30 | 0 |  |
| 213 | 22 | 3.55 | 0.21066 | - |  | 3 | 0 |
| 214 | 22 | 3.55 | 0.11107 | - |  | 4 | 0 |
| 215 | 22 | 3.55 | 0.04766 | 0.80955 |  | 6 | 0 |
| 216 | 22 | 3.55 | 0.02679 | 0.91419 |  | 8 | 0 |
| 217 | 22 | 3.55 | 0.01762 | 0.93847 |  | 10 | 0 |
| 218 | 22 | 3.55 | 0.01226 | 0.95888 |  | 12 | 0 |
| 219 | 22 | 3.55 | 0.00818 | 0.98349 |  | 15 | 0 |
| 220 | 22 | 3.55 | 0.00534 | 0.99000 |  | 20 | 0 |
| 221 | 22 | 3.55 | 0.00382 | 0.99337 |  | 25 | 0 |
| 222 | 22 | 3.55 | 0.00293 | 0.99777 |  | 30 | 0 |
| 223 | 22 | 7.04 | 0.22875 | - |  | 4 | 0 |
| 224 | 22 | 7.04 | 0.10053 | 0.69460 |  | 6 | 0 |
| 225 | 22 | 7.04 | 0.05452 | 0.88046 |  | 8 | 0 |
| 226 | 22 | 7.04 | 0.03466 | 0.92616 |  | 10 | 0 |
| 227 | 22 | 7.04 | 0.02398 | 0.94008 |  | 12 | 0 |
| 228 | 22 | 7.04 | 0.01616 | 0.98089 |  | 15 | 0 |
| 229 | 22 | 7.04 | 0.01019 | 0.97665 |  | 20 | 0 |
| 230 | 22 | 7.04 | 0.00741 | 0.98680 |  | 25 | 0 |
| 231 | 22 | 7.04 | 0.00576 | 0.99399 |  | 30 | 0 |
| 232 | 22 | 13.80 | 0.46874 | - |  | 4 | 0 |
| 233 | 22 | 13.80 | 0.20186 | 0.48491 |  | 6 | 0 |
| 234 | 22 | 13.80 | 0.10816 | 0.76928 |  | 8 | 0 |
| 235 | 22 | 13.80 | 0.07130 | 0.83718 |  | 10 | 0 |
| 236 | 22 | 13.80 | 0.05040 | 0.90110 |  | 12 | 0 |
| 237 | 22 | 13.80 | 0.03324 | 0.94854 |  | 15 | 0 |
| 238 | 22 | 13.80 | 0.02055 | 0.95736 |  | 20 | 0 |
| 239 | 22 | 13.80 | 0.01519 | 0.96398 |  | 25 | 0 |
| 240 | 22 | 13.80 | 0.01161 | 0.98292 |  | 30 | 0 |
| 241 | 22 | 24.90 | 0.79698 | - |  | 4 | 0 |
| 242 | 22 | 24.90 | 0.38579 | 0.24122 |  | 6 | 0 |
| 243 | 22 | 24.90 | 0.21888 | 0.64575 |  | 8 | 0 |
| 244 | 22 | 24.90 | 0.13926 | 0.78693 |  | 10 | 0 |
| 245 | 22 | 24.90 | 0.09642 | 0.85127 |  | 12 | 0 |
| 246 | 22 | 24.90 | 0.06240 | 0.92038 |  | 15 | 0 |
| 247 | 22 | 24.90 | 0.03860 | 0.94062 |  | 20 | 0 |
| 248 | 22 | 24.90 | 0.02757 | 0.95999 |  | 25 | 0 |
| 249 | 22 | 24.90 | 0.02178 | 0.97487 |  | 30 | 0 |
| 250 | 22 | 49.20 | 0.72795 | 0.03735 |  | 6 | 0 |
| 251 | 22 | 49.20 | 0.44316 | 0.36589 |  | 8 | 0 |
| 252 | 22 | 49.20 | 0.29064 | 0.57759 |  | 10 | 0 |
| 253 | 22 | 49.20 | 0.19992 | 0.70950 |  | 12 | 0 |
| 254 | 22 | 49.20 | 0.13154 | 0.83966 |  | 15 | 0 |
| 255 | 22 | 49.20 | 0.07856 | 0.89027 |  | 20 | 0 |
| 256 | 22 | 49.20 | 0.05512 | 0.93257 |  | 25 | 0 |
| 257 | 22 | 49.20 | 0.04





| Mass thickness <br> $\left(\mu \mathrm{g} \mathrm{cm}^{-2}\right)$ | Accelerating <br> voltage ( kV ) | No. | Zsubstrate | k (Al K $\left.{ }_{\alpha}\right)$ | k (substrate) | Substrate line |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 348 | 8 | 348 | 26 | 13.80 | 0.11394 | 0.57793 |
|  | 0 |  |  |  |  |  |
| 349 | 10 | 349 | 26 | 13.80 | 0.07512 | 0.86758 |
|  | 0 |  |  |  |  |  |
| 350 | 12 | 350 | 26 | 13.80 | 0.05282 | 0.94376 |
|  | 0 |  |  |  |  |  |
| 351 | 15 | 351 | 26 | 13.80 | 0.03412 | 0.93564 |
|  | 0 |  |  |  |  |  |
| 352 | 20 | 352 | 26 | 13.80 | 0.02091 | 0.94043 |
|  | 0 |  |  |  |  |  |
| 353 | 25 | 353 | 26 | 13.80 | 0.01563 | 0.97845 |
|  | 0 |  |  |  |  |  |
| 354 | 30 | 354 | 26 | 13.80 | 0.01180 | 0.99999 |
|  | 0 |  |  |  |  |  |
| 355 | 6 | 355 | 26 | 13.80 | - | 0.77222 |
|  | 1 |  |  |  |  |  |
| 356 | 8 | 356 | 26 | 13.80 | - | 0.84891 |
|  | 1 |  |  |  |  |  |
| 357 | 10 | 357 | 26 | 13.80 | - | 0.88585 |
|  | 1 |  |  |  |  |  |
| 358 | 12 | 358 | 26 | 13.80 | - | 0.91239 |
|  | 1 |  |  |  |  |  |
| 359 | 4 | 359 | 26 | 24.90 | 0.78920 | - |
|  | 0 |  |  |  |  |  |
| 360 | 6 | 360 | 26 | 24.90 | 0.39604 | - |
|  | 0 |  |  |  |  |  |
| 361 | 8 | 361 | 26 | 24.90 | 0.22558 | 0.34707 |
|  | 0 |  |  |  |  |  |
| 362 | 10 | 362 | 26 | 24.90 | 0.14407 | 0.73640 |
|  | 0 |  |  |  |  |  |
| 363 | 12 | 363 | 26 | 24.90 | 0.09994 | 0.87865 |
|  | 0 |  |  |  |  |  |
| 364 | 15 | 364 | 26 | 24.90 | 0.06538 | 0.89956 |
|  | 0 |  |  |  |  |  |
| 365 | 20 | 365 | 26 | 24.90 | 0.04013 | 0.94004 |
|  | 0 |  |  |  |  |  |
| 366 | 25 | 366 | 26 | 24.90 | 0.02887 | 0.96704 |
|  | 0 |  |  |  |  |  |
| 367 | 30 | 367 | 26 | 24.90 | 0.02248 | 0.99999 |
|  | 0 |  |  |  |  |  |
| 368 | 6 | 368 | 26 | 24.90 | - | 0.58730 |
|  | 1 |  |  |  |  |  |
| 369 | 8 | 369 | 26 | 24.90 | - | 0.74152 |
|  | 1 |  |  |  |  |  |
| 370 | 10 | 370 | 26 | 24.90 | - | 0.80390 |
|  | 1 |  |  |  |  |  |
| 371 | 12 | 371 | 26 | 24.90 | - | 0.84390 |
|  | 1 |  |  |  |  |  |
| 372 | 6 | 372 | 26 | 49.20 | 0.73609 | - |
|  | 0 |  |  |  |  |  |
| 373 | 8 | 373 | 26 | 49.20 | 0.45993 | 0.09354 |
|  | 0 |  |  |  |  |  |
| 374 | 10 | 374 | 26 | 49.20 | 0.30140 | 0.49089 |
|  | 0 |  |  |  |  |  |
| 375 | 12 | 375 | 26 | 49.20 | 0.20834 | 0.71368 |
|  | 0 |  |  |  |  |  |
| 376 | 15 | 376 | 26 | 49.20 | 0.13693 | 0.80922 |
|  | 0 |  |  |  |  |  |
| 377 | 20 | 377 | 26 | 49.20 | 0.08200 | 0.84567 |
|  | 0 |  |  |  |  |  |
| 378 | 25 | 378 | 26 | 49.20 | 0.05718 | 0.91370 |
|  | 0 |  |  |  |  |  |
| 379 | 30 | 379 | 26 | 49.20 | 0.04557 | 0.96844 |
|  | 0 |  |  |  |  |  |
| 380 | 6 | 380 | 26 | 49.20 | - | 0.29215 |
|  | 1 |  |  |  |  |  |
| 381 | 8 | 381 | 26 | 49.20 | - | 0.51745 |
|  | 1 |  |  |  |  |  |
| 382 | 10 | 38





| Mass thickness <br> $\left(\mu g \mathrm{~g} \mathrm{~cm}^{-2}\right)$ | Accelerating <br> voltage $(\mathrm{kV})$ | No. | Zsubstrate | k (Al K $\left.{ }_{\alpha}\right)$ | k (substrate) | Substrate line |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 484 | 29 |  | 3.55 | 0.23640 | — | 3 |
| 485 | 29 | 3.55 | 0 | 0.11740 | — | 4 |
| 486 | 29 | 3.55 | 0 | 0.05043 | — | 6 |
| 487 | 29 | 3.55 | 0 | 0.02920 | — | 8 |
| 488 | 29 | 3.55 | 0 | 0.01890 | — | 10 |
| 489 | 29 | 3.55 | 0 | 0.01286 | 0.94878 | 12 |
| 490 | 29 | 3.55 | 0 | 0.00884 | 0.97301 | 15 |
| 491 | 29 | 3.55 | 0 | 0.00565 | 0.98319 | 20 |
| 492 | 29 | 3.55 | 0 | 0.00405 | 0.99000 | 25 |
| 493 | 29 | 3.55 | 0 | 0.00311 | 0.99617 | 30 |
| 494 | 29 | 3.55 | — | 0.85512 |  | 4 |
| 495 | 29 | 3.55 | — | 0.93448 |  | 6 |
| 496 | 29 | 3.55 | — | 0.97200 |  | 8 |
| 497 | 29 | 3.55 | — | 0.95705 |  | 10 |
| 498 | 29 | 3.55 | — | 0.97310 |  | 12 |
| 499 | 29 | 3.55 | — | 0.97420 |  | 15 |
| 500 | 29 | 3.55 | — | 0.98663 |  | 20 |
| 501 | 29 | 3.55 | — | 0.99227 |  | 25 |
| 502 | 29 | 3.55 | — | 0.97592 |  | 30 |
| 503 | 29 | 7.04 | 0.24048 | — |  | 4 |
| 504 | 29 | 7.04 | 0 | 0.10579 | — | 6 |
| 505 | 29 | 7.04 | 0 | 0.05826 | — | 8 |
| 506 | 29 | 7.04 | 0 | 0.03732 | - | 10 |
| 507 | 29 | 7.04 | 0 | 0.02594 | 0.92677 | 12 |
| 508 | 29 | 7.04 | 0 | 0.01823 | 0.96248 | 15 |
| 509 | 29 | 7.04 | 0 | 0.01105 | 0.95736 | 20 |
| 510 | 29 | 7.04 | 0 | 0.00784 | 0.97979 | 25 |
| 511 | 29 | 7.04 | 0 | 0.00615 | 0.99000 | 30 |
| 512 | 29 | 7.04 | — | 0.74566 |  | 4 |
| 513 | 29 | 7.04 | — | 0.89242 |  | 6 |
| 514 | 29 | 7.04 | — | 0.94333 |  | 8 |
| 515 | 29 | 7.04 | — | 0.93681 |  | 10 |
| 516 | 29 | 7.04 | — | 0.95592 |  | 12 |
| 517 | 29 | 7.04 | — | 0.95662 |  | 15 |
| 518 | 29 | 7.04 | - | 0.98675 |  | 20 |
| 519 | 29 | 7.04 | — | 0.98785 |  | 25 |
| 520 | 29 | 7.04 | — | 0.99244 |  | 30 |
| 521 | 29 | 13.80 | 0.48384 | — |  | 4 |
| 522 | 29 | 13.80 | 0 | 0.21368 | — | 6 |
| 523 | 29 | 13.80 | 0 | 0.11748 | — | 8 |
| 524 | 29 | 13.80 | 0 | 0.07694 | - | 10 |
| 525 | 29 | 13.80 | 0 | 0.05312 | 0.92344 | 12 |
| 526 | 29 | 13.80 | 0 | 0.03740 | 0.93486 | 15 |
| 527 | 29 | 13.80 | 0 | 0.02196 | 0.93735 | 20 |
| 528 | 29 | 13.80 | 0 | 0.01628 | 0.98826 | 25 |
| 529 | 29 | 13.80 | 0 | 0.01235 | 0.99999 | 30 |
| 530 | 29 | 13.80 | - | 0.57197 |  | 4 |
| 531 | 29 | 13.80 | - | 0.80859 |  | 6 |
| 532 | 29 | 13.80 | — | 0.88203 |  | 8 |
| 533 | 29 | 13.80 | - | 0.90673 |  | 10 |
| 534 | 29 | 13.80 | - | 0.93856 |  | 12 |
| 535 | 29 | 13.80 | - | 0.94743 |  | 15 |
| 536 | 29 | 13.80 | — | 0.95955 |  | 20 |
| 537 | 29 | 13.80 | — | 0.95420 |  | 25 |
| 538 | 29 | 13.80 | — | 0.96708 |  | 30 |






|  | Mass thickness <br> $\left(\mu \mathrm{g} \mathrm{cm}^{-2}\right)$ | Accelera <br> voltage (kV) |  |  |  |  |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| No. | Zsubstrate | k (Al K miscarすす | k (substrate) | Substrate line | line |  |
|  |  |  |  |  | 3.80 |  |
| 1 | 620 | 32 | 13.80 | 0.07906 | 0.93829 | 10 |
|  |  | 0 |  | 0.05468 | 0.94851 | 12 |
| 1 | 622 | 32 | 13.80 | 0.03616 | 0.97775 | 15 |
| 1 | 623 | 32 | 13.80 | 0.02227 | 0.98206 | 20 |
| - |  | 1 | 1 | - | 0.96794 | 15 |
| 0 | 628 | 32 | 13.80 | — | 0.98933 | 20 |
| 0 | 629 | 32 | 13.80 | - | 0.99346 | 250 |
| 0 | 6300 | 32 | 24.90 | — | 1.01233 | 30 |
|  |  | 1 | 1 | 0.80986 | 0.29506 | 4 |
|  |  |  | 1 | 0.41186 | 0.65619 | 6 |
| 1 | 632 | 32 | 24.90 | 0.23620 | 0.79279 | 8 |
| 1 | 633 | 32 | 24.90 | 0.14986 | 0.87784 | 10 |
| 1 | 634 | 32 | 24.90 | 0.10544 | 0.90865 | 12 |
| 1 | 635 | 32 | 24.90 | 0.07081 | 0.95099 | 15 |
| 1 | 636 | 32 | 24.90 | 0.04226 | 0.96803 | 20 |
| 1 | 637 | 32 | 24.90 | 0.03024 | 0.98236 | 25 |
| 1 | 638 | 32 | 24.90 | 0.02372 | 0.98582 | 30 |
|  |  | 0 | 0 | 0.90592 | 15 |  |
| 0 | 640 | 32 | 24.90 | - | 0.96277 | 20 |
| 0 final | 641 | 32 | 24.90 | — | 0.99311 | 25 |
|  |  | 0 |  | 0 | 0 | - |
|  |  |  | 1 | 0.7488 \| 0.32890 | 20 |  |
| 6 | 645 | 32 | 49.20 | 0.31592 | 0.72741 | 10 |
|  |  | 1 | 1 | 0.47498 | 0.57985 | 8 |
| 1 | 647 | 32 | 49.20 | 0.14558 | 0.89495 | 15 |
| 1 | 649 | 32 | 49.20 | 0.06162 | 0.95548 | 25 |
| 1 | 651 | 32 | 49.20 | - | 0.76563 | 15 |
| 15 |  | 0 |  | 0 | 0 | - |
| 1 | 653 | 32 | 49.20 | — | 0.95254 | 25 |
| 1 | 654 | 32 | 49.20 | - | 0.97338 | 30 |
|  |  | 1 | 1 |  |  | - |
| 1 | 657 | 32 | 85.40 | 0.54814 | 0.51240 | 10 |
| 1 | 659 | 32 | 85.40 | 0.28466 | 0.78317 | 15 |
| 1 | 661 | 32 | 85.40 | 0.15866 | 0.87321 | 20 |
| 1 | 663 | 32 | 85.40 | — | 0.56032 | 15 |
| 1 | 665 | 32 | 85.40 | - | 0.90512 | 25 |
| - |  | 0 | 0 | - | 0.93941 | 30 |
| 3 | 667 | 40 | 3.55 | 0.25204 | - |  |
| 4 | 668 | 40 | 3.55 | 0.12324 | 0.76180 | 4 |
|  |  | 0 |  | 0.05254 | 0.87800 | 6 |
| 1 | 671 | 40 | 3.55 | 0.01956 | 0.95450 | 10 |
| 1 | 672 | 40 | 3.55 | 0.01366 | 0.95380 | 12 |
| 1 | 673 | 40 | 3.55 | 0.00970 | 0.97620 | 15 |
| , |  | 1 |  | 0.00629 | 0.98440 | 20 |
| , |  | 1 |  | 0.00444 | 0.99230 | 25 |
| 1 | 677 | 40 | 7.04 | — |  |  |
| 2 | 679 | 40 | 7.04 | 0.06148 | 0.87600 | 8 |
|  | 681 | 40 | 7.04 | $0.0395_{0}$ | 0.92750 | 10 |
| 1 | 682 | 40 | 7.04 | 0.02784 | 0.93650 | 12 |
|  |  |  |  | 0.01381 | 0.94980 | 15 |
| 1 | 684 | 40 | 7.04 | — | 0.98010 | 25 |
| 1 | 685 | 40 | 7.04 | 0.00683 | 0.97570 | 0 |
| 2 | 687 | 40 | 13.80 | 0.49426 | 0.41500 | 4 |
| 4 |  |  | 20 | 0.2233 | 

| Mass thickness |  | Accelerating <br> voltage (kV) | No. | Zsubstrate |  | $k$ (Al $\left.\mathrm{K} \alpha\right)$ | $k$ (substrate) | Substrate line |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|  | $\left(\mu \mathrm{g} \mathrm{cm}^{-2}\right)$ |  |  | $\left(\AA_{0}\right)$ | $\left(\AA_{0}\right)$ |  |  |  |
| 688 | 40 | 13.80 | 8 | 0.12316 | 0.80580 |  |  |  |
| 689 | 40 | 13.80 | 10 | 0.08308 | 0.87390 |  |  |  |
| 690 | 40 | 13.80 | 12 | 0.05782 | 0.88920 |  |  |  |
| 691 | 40 | 13.80 | 15 | 0.03933 | 0.92260 |  |  |  |
| 692 | 40 | 13.80 | 20 | 0.02430 | 0.95220 |  |  |  |
| 693 | 40 | 13.80 | 25 | 0.01811 | 0.95710 |  |  |  |
| 694 | 40 | 13.80 | 30 | 0.01375 | 0.95400 |  |  |  |
| 695 | 40 | 24.90 | 4 | 0.80654 | 0.16580 |  |  |  |
| 696 | 40 | 24.90 | 6 | 0.41912 | 0.52560 |  |  |  |
| 697 | 40 | 24.90 | 8 | 0.24331 | 0.69180 |  |  |  |
| 698 | 40 | 24.90 | 10 | 0.15909 | 0.79780 |  |  |  |
| 699 | 40 | 24.90 | 12 | 0.11094 | 0.82590 |  |  |  |
| 700 | 40 | 24.90 | 15 | 0.07749 | 0.87420 |  |  |  |
| 701 | 40 | 24.90 | 20 | 0.04572 | 0.89720 |  |  |  |
| 702 | 40 | 24.90 | 25 | 0.03302 | 0.90640 |  |  |  |
| 703 | 40 | 24.90 | 30 | 0.02580 | 0.91350 |  |  |  |
| 704 | 40 | 49.20 | 6 | 0.75257 | 0.21960 |  |  |  |
| 705 | 40 | 49.20 | 8 | 0.48325 | 0.45830 |  |  |  |
| 706 | 40 | 49.20 | 10 | 0.32296 | 0.60770 |  |  |  |
| 707 | 40 | 49.20 | 12 | 0.22848 | 0.68550 |  |  |  |
| 708 | 40 | 49.20 | 15 | 0.15386 | 0.75850 |  |  |  |
| 709 | 40 | 49.20 | 20 | 0.09228 | 0.81150 |  |  |  |
| 710 | 40 | 49.20 | 25 | 0.06784 | 0.83680 |  |  |  |
| 711 | 40 | 49.20 | 30 | 0.05287 | 0.84970 |  |  |  |
| 712 | 40 | 85.40 | 6 | 0.98987 | 0.03500 |  |  |  |
| 713 | 40 | 85.40 | 8 | 0.78718 | 0.19910 |  |  |  |
| 714 | 40 | 85.40 | 10 | 0.56787 | 0.37090 |  |  |  |
| 715 | 40 | 85.40 | 12 | 0.42383 | 0.48830 |  |  |  |
| 716 | 40 | 85.40 | 15 | 0.29511 | 0.60050 |  |  |  |
| 717 | 40 | 85.40 | 20 | 0.16915 | 0.69700 |  |  |  |
| 718 | 40 | 85.40 | 25 | 0.12714 | 0.72960 |  |  |  |
| 719 | 40 | 85.40 | 30 | 0.09498 | 0.74150 |  |  |  |
| 720 | 42 | 3.55 | 6 | 0.26392 | - |  | 3 | 1 |
| 721 | 42 | 3.55 | 4 | 0.12690 | 0.75760 |  |  |  |
| 722 | 42 | 3.55 | 6 | 0.05420 | 0.89775 |  |  |  |
| 723 | 42 | 3.55 | 8 | 0.03101 | 0.95313 |  |  |  |
| 724 | 42 | 3.55 | 10 | 0.02060 | 0.96561 |  |  |  |
| 725 | 42 | 3.55 | 12 | 0.01446 | 0.97440 |  |  |  |
| 726 | 42 | 3.55 | 15 | 0.00985 | 0.98619 |  |  |  |
| 727 | 42 | 3.55 | 20 | 0.00638 | 0.99148 |  |  |  |
| 728 | 42 | 3.55 | 25 | 0.00455 | 0.99471 |  |  |  |
| 729 | 42 | 3.55 | 30 | 0.00347 | 0.98904 |  |  |  |
| 730 | 42 | 7.04 | 4 | 0.25158 | 0.59394 |  |









| Mass thickness <br> $\left(\mu g \mathrm{~g}^{-2}\right)$ | Accelerating <br> voltage ( kV ) | No. | Zsubstrate | $k\left(\mathrm{Al} \mathrm{K}_{\alpha}\right)$ | $k$ (substrate) | Substrate line |
| :--- | :--- | :---: | :--- | :---: | :---: | :---: |
| 892 | 10 | 1 | 50 | 7.04 | 0.04126 | 0.88881 |
| 893 | 12 | 1 | 50 | 7.04 | 0.02969 | 0.92168 |
| 894 | 15 | 1 | 50 | 7.04 | 0.02057 | 0.94272 |
| 895 | 20 | 1 | 50 | 7.04 | 0.01260 | 0.95546 |
| 896 | 25 | 1 | 50 | 7.04 | 0.00907 | 0.96824 |
| 897 | 30 | 1 | 50 | 7.04 | 0.00698 | 0.98159 |
| 898 | 4 | 1 | 50 | 13.80 | 0.50416 | - |
| 899 | 6 | 1 | 50 | 13.80 | 0.23708 | 0.59419 |
| 900 | 8 | 1 | 50 | 13.80 | 0.12804 | 0.80121 |
| 901 | 10 | 1 | 50 | 13.80 | 0.08573 | 0.83904 |
| 902 | 12 | 1 | 50 | 13.80 | 0.06008 | 0.89992 |
| 903 | 15 | 1 | 50 | 13.80 | 0.04124 | 0.92400 |
| 904 | 20 | 1 | 50 | 13.80 | 0.02447 | 0.94523 |
| 905 | 25 | 1 | 50 | 13.80 | 0.01838 | 0.95999 |
| 906 | 30 | 1 | 50 | 13.80 | 0.01414 | 0.97494 |
| 907 | 4 | 1 | 50 | 24.90 | 0.81764 | - |
| 908 | 6 | 1 | 50 | 24.90 | 0.43128 | 0.40265 |
| 909 | 8 | 1 | 50 | 24.90 | 0.25004 | 0.66827 |
| 910 | 10 | 1 | 50 | 24.90 | 0.16597 | 0.78642 |
| 911 | 12 | 1 | 50 | 24.90 | 0.11766 | 0.86025 |
| 912 | 15 | 1 | 50 | 24.90 | 0.07947 | 0.89165 |
| 913 | 20 | 1 | 50 | 24.90 | 0.04667 | 0.92186 |
| 914 | 25 | 1 | 50 | 24.90 | 0.03366 | 0.95089 |
| 915 | 30 | 1 | 50 | 24.90 | 0.02755 | 0.96763 |
| 916 | 6 | 1 | 50 | 49.20 | 0.75981 | 0.11597 |
| 917 | 8 | 1 | 50 | 49.20 | 0.49385 | 0.42023 |
| 918 | 10 | 1 | 50 | 49.20 | 0.33888 | 0.59281 |
| 919 | 12 | 1 | 50 | 49.20 | 0.23662 | 0.71910 |
| 920 | 15 | 1 | 50 | 49.20 | 0.16276 | 0.79539 |
| 921 | 20 | 1 | 50 | 49.20 | 0.09747 | 0.87948 |
| 922 | 25 | 1 | 50 | 49.20 | 0.06943 | 0.91038 |
| 923 | 30 | 1 | 50 | 49.20 | 0.05405 | 0.93791 |
| 924 | 6 | 1 | 50 | 85.40 | 0.98791 | 0.01060 |
| 925 | 8 | 1 | 50 | 85.40 | 0.79347 | 0.17341 |
| 926 | 10 | 1 | 50 | 85.40 | 0.57306 | 0.38589 |
| 927 | 12 | 1 | 50 | 85.40 | 0.43071 | 0.55331 |
| 928 | 15 | 1 | 50 | 85.40 | 0.30611 | 0.69927 |
| 929 | 20 | 1 | 50 | 85.40 | 0.18653 | 0.81229 |
| 930 | 25 | 1 | 50 | 85.40 | 0.13216 | 0.87045 |
| 931 | 30 | 1 | 50 | 85.40 | 0.10233 | 0.90615 |
| 932 | 72 | 3 | 2 | 3.55 | 0.27510 | - |
| 933 | 72 | 4 | 2 | 3.55 | 0.13310 | - |
| 934 | 72 | 6 | 2 | 3.55 | 0.05782 | - |
| 935 | 72 | 8 | 2 | 3.55 | 0.03336 | - |
| 936 | 72 | 10 | 2 | 3.55 | 0.02213 | - |
| 937 | 72 | 12 | 2 | 3.55 | 0.01582 | - |
| 938 | 72 | 15 | 2 | 3.55 | 0.01075 | - |
| 939 | 72 | 20 | 2 | 3.55 | 0.00686 | - |
| 940 | 72 | 25 | 2 | 3.55 | 0.00485





















