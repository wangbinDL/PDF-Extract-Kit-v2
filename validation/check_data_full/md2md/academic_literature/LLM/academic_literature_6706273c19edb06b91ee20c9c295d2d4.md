# HEATS OF FORMATION FOR BORON COMPOUNDS BASED ON QUANTUM CHEMICAL CALCULATIONS 

JIAHENG ZHANG, SHIQIAN WEI, CHAOZHU MAO, LIANG CHEN, HAIXIANG GAO, WENFENG ZHOU* and ZHIQIANG ZHOU*


*Corresponding author.
* E-mail: zhouwenfeng@cau.edu.cn


#### Abstract

We have calculated the heats of formation at 298.15 K of series of boron compounds including $\mathrm{H}, \mathrm{N}, \mathrm{O}, \mathrm{F}, \mathrm{Cl}$ atoms using the atomization enthalpies analysis based on eleven quantum chemical calculations. The majority of calculated values are in excellent agreement with available experiment values and Gaussian-n methods perform more accurate evaluations than other approaches. As with the existing literature, the following calculations of the heats of formation of borides containing light atoms are recommended as accurate values: $\Delta_{f} H_{\mathrm{G} 2,298}(\mathrm{BH})=442.731 \mathrm{~kJ} \cdot \mathrm{mol}^{-1}, \Delta_{f} H_{\mathrm{G} 2,298}\left(\mathrm{BF}_{3}\right)=$ $-1135.749 \mathrm{~kJ} \cdot \mathrm{mol}^{-1}$, the deviations are respectively $0.031 \mathrm{~kJ} \cdot \mathrm{mol}^{-1}$ and $0.251 \mathrm{~kJ} \cdot \mathrm{mol}^{-1}$. Furthermore, ab initio calculations of heats of formation of chlorinated boron compounds also show good accuracy and comparisons with previous thermodynamics data are made.


Keywords: Boride; heat of formation; Gaussian-n method; ab initio calculations.

## 1. Introduction

Boron occupies a unique position in the IIIA main group because of its properties, which borderline between metals and nonmetals; crystalline boron is inert chemically, while amorphous boron is a preferred additive to high-energy propellant for its high-volume heat value and is extensively applied in aerospace engineering. Boron has the capacity to form stable covalently bonded molecular networks; some boron compounds have particular thermodynamic characteristics and thus have much potential for commercial applications. For example, the direct borohydride fuel cell is a novel fuel cell that has a high theoretical specific energy and is environmentally benign. ${ }^{1}$ Another example is boron trihalides, which are of considerable recent interest because of their use in radio-frequency (rf) plasmas and the commercial etching of metals and semiconductors. ${ }^{2}$ Despite these examples of commercial use, our understanding of boron chemistry is limited. For instance, boron's element of




---

atomic heat of formation is associated with uncertainties greater than or equal to about $1 \mathrm{kcal} / \mathrm{mol} .{ }^{3}$ Furthermore, there is no consistent and reliable set of thermodynamic data for boron compounds. From a researcher's perspective, the most basic thermodynamic property of a polyatomic molecule is the heat of formation. Due to the lack of accurate knowledge of the thermodynamic properties for most of the molecules involved in modeling atmospheric processes, experiments focused on these processes and combustion are unable to obtain accurate heat of formation data. With this in mind, it is not surprising to find that some of the boron compounds' heats of formation have been studied using computational chemistry techniques. In 1989, Barone and Minichino studied the structure formation enthalpy of $\mathrm{B}_{2} \mathrm{H}_{6}$ using the Hartree-Fock level and employing the 6-21* basis set. ${ }^{4}$ Rablen and Hartwig computed the atomization energies of $\mathrm{BF}_{n}$ species using the G2 and CBS4 approaches. ${ }^{5}$. Bauschlicher and Ricca evaluated accurate heats of formation for $\mathrm{BF}_{n}$ and $\mathrm{BCl}_{n}(n=1-3)$ optimized by the B3LYP/6-311+G(2df) approach and used CCSD(T) results. ${ }^{6}$ Over the last three years, there has been a large number of papers published in this area, and theoretical research found in these literature include thermodynamic equilibrium calculations for mixtures involving $\mathrm{B} / \mathrm{F} / \mathrm{N} / \mathrm{H} .{ }^{7,8}$

Taking a wide view of the related questions being researched, there is no system being studied that centers on the boron element and compares the thermodynamic properties of different kinds of borides, especially the heats of formation. Considering the weakness in processing halide-containing systems for Gaussian-n methods, ${ }^{9}$ there are also no series of high-level calculations for chlorinated boron compounds that have been done - in particular the heat of formation for $\mathrm{B}_{2} \mathrm{Cl}_{4}$, despite it being very important for the research of polyboron halide. ${ }^{10}$ Despite the deficiency of Gaussian-n methods, with the development of computer technology, computational quantum chemical calculations have become the most accurate method and can be widely used to predict the heat of formation. The Gaussian-n methods used by Curtiss et al. ${ }^{11,12}$ and the complete basis set (CBS) extrapolation methods ${ }^{13,14}$ are among the most popular theoretical methods for heat of formation calculations. In addition, in this field some modifications of these theoretical approaches have been used frequently, such as G2MP2, G3MP3, ${ }^{15} \mathrm{G} 3 \mathrm{MP} 2 \mathrm{~B} 3,{ }^{16}$ and G3B3. ${ }^{17}$ Therefore, given the interest in these problems, we chose 11 high-level quantum chemical calculations and predicted the heats of formation based on these methods at 298.15 K for 14 boron compounds including $\mathrm{H}, \mathrm{N}, \mathrm{O}, \mathrm{F}$, and Cl atoms. Based on these data, we recommend a reliable computational quantum chemical calculation and, more importantly, determine accurate heats of formation for future studies on chlorinated boron compounds.

# 2. Method 

### 2.1. Computational methods

Our computational approach for calculating the heats of formation for boron compounds was to use atomization enthalpies. This approach has the advantage of using




---

the accurately known enthalpies of formation for the common elements B, H, N, O, F, and Cl and combining them with the computational data. As mentioned above, we used 11 high-level quantum chemical calculations; the Gaussian-n methods and complete basis set methods were our first choice. The general principle of Gaussian$n$ theory is to perform calculations at a high level of theory, such as QCISD(T). The theory is based on corrections to energy due to deficiencies of the basis set; these are performed assuming that high-level correlations can be treated separately and combined in an additive manner. Different versions of Gaussian- $n$ theory with different combination schemes has resulted in different accuracies and computational costs. ${ }^{18}$ It should be noted that the G3 suit of computational methods is only a procedure for calculating total electronic energies of atoms and molecules containing atoms with $Z \leq 18$ (hydrogen to argon). The general principle of the CBS method is to extrapolate SCF and correlation energies with the finite one-electron basis set to the complete basis set limit through a series of single point calculations. Various extrapolation schemes for various one-electron basis sets lead to various correlation levels. ${ }^{19}$ Based on this information, we used three Gaussian-n methods (G1, G2, and G3) and four CBS methods (CBS-QB3, CBS-40, CBS-4 M , and CBS-Q). Although Gaussian- $n$ and CBS methods can obtain accurate computational data, both of them have obvious drawbacks, the main one being that these methods are time-consuming. Thus, many modified methods were used in our calculations, such as G3MP2, G2MP2, G3MP2B3, and G3B3. G3MP2 and G2MP2 theory are modifications of G3 and G2 theory; these methods use second-order Moller-Plesset perturbation theory with the basis sets 6-31G(d) and 6-311+G(2df,2p) on Li-Ne and $6-311+(3 d f, 2 p)$ on Na-Ar. In addition, a single-point quadratic configuration interaction in these methods was carried out for energy in the QCISD(T)/6-31G(d) set. G3MP2B3 and G3B3 theory are further modifications of G3MP2 and G3 theory; compared to the former methods, these methods use geometries and zero-point vibrational energy (ZPVE) scaled by 0.96 from B3LYP/6-31G(d) calculations. They can be applied to larger systems with more than 150 electrons and are evaluation methods that are economical with regard to time. ${ }^{20}$ All calculations for these 11 methods were performed with the Gaussian 03 package of programs. ${ }^{21}$

# 2.2. Thermodynamic analysis 

Calculating heats of formation at 298.15 K is not a straightforward task; it can be split into three steps. The first is to calculate the nonrelativistic atomization energy $\Delta D^{0}$, which is the energy needed to dissociate a molecule into its separate atoms. For any molecule, represented here as $A_{x} B_{y} C_{z}$, the atomization energy is given by:

$$
\begin{aligned}
\Delta D^{0}\left(A_{x} B_{y} C_{z}\right)= & x \varepsilon^{0}(A)+y \varepsilon^{0}(B)+0 z \varepsilon^{0}(C) \\
& -\varepsilon^{0}\left(A_{x} B_{y} C_{z}, \quad\right)+\varepsilon_{\mathrm{ZPE}}\left(A_{x} B_{y} C_{z}, \quad\right)
\end{aligned}
$$

where $\varepsilon^{0}$ is the total energy for constituent atoms or molecules and $\varepsilon_{\text {ZPE }}$ is the zeropoint energy of the molecule. The second step is to calculate the heat of formation




---

at $0 \mathrm{~K} \Delta f H^{\ominus}$, and it is given by:

$$
\begin{aligned}
\Delta f H^{\Theta}\left(A_{x} B_{y} C_{z}, 0 \mathrm{~K}\right)=x & \Delta f H^{\Theta}(A, 0 \mathrm{~K})+y \Delta f H^{\Theta}(B, 0 \mathrm{~K}) \\
& +z \Delta f H^{\Theta}(C, 0 \mathrm{~K})-D^{\Theta}\left(A_{x} B_{y} C_{z}\right)
\end{aligned}
$$

Theoretical heats of formation at 298.15 K were calculated by correcting $\Delta f H^{\Theta}$ at 0 K as follows:

$$
\begin{aligned}
\Delta f H^{\ominus}\left(A_{x} B_{y} C_{z}, 298 \mathrm{~K}\right)= & \Delta f H^{\ominus}\left(A_{x} B_{y} C_{z}, 0 \mathrm{~K}\right)+H^{\ominus}\left(A_{x} B_{y} C_{z}, 298 \mathrm{~K}\right) \\
& -H^{\ominus}\left(A_{x} B_{y} C_{z}, 0 \mathrm{~K}\right)-x\left[H^{\ominus}(A, 298 \mathrm{~K})-H^{\ominus}(A, 0 \mathrm{~K})\right] \\
& -y\left[H^{\ominus}(B, 298 \mathrm{~K})-H^{\ominus}(B, 0 \mathrm{~K})\right] \\
& -z\left[H^{\ominus}(C, 298 \mathrm{~K})-H^{\ominus}(C, 0 \mathrm{~K})\right]
\end{aligned}
$$

In this step, the value of $\left[H^{\Theta}\left(A_{x} B_{y} C_{z}, 298 \mathrm{~K}\right)-H^{\Theta}\left(A_{x} B_{y} C_{z}, 0 \mathrm{~K}\right)\right.$ ] can be replaced by $H_{\text {corr }}-\varepsilon_{\mathrm{ZPE}}\left(A_{x} B_{y} C_{z}\right)$, where $H_{\text {corr }}$ is the correction to enthalpy due to internal energy. We combine the above three equations and integrate as follows:

$$
\begin{aligned}
\Delta f H^{\Theta}\left(A_{x} B_{y} C_{z}, 298 \mathrm{~K}\right)= & x \Delta f H^{\Theta}(A, 0 \mathrm{~K})+y \Delta f H^{\Theta}(B, 0 \mathrm{~K})+z \Delta f H^{\Theta}(C, 0 \mathrm{~K}) \\
& -x\left[H^{\Theta}(A, 298 \mathrm{~K})-H^{\Theta}(A, 0 \mathrm{~K})\right]-y\left[H^{\Theta}(B, 298 \mathrm{~K})\right. \\
& \left.-H^{\Theta}(B, 0 \mathrm{~K})\right]-z\left[H^{\Theta}(C, 298 \mathrm{~K})-H^{\Theta}(C, 0 \mathrm{~K})\right] \\
& +H_{\mathrm{corr}}+\varepsilon^{\Theta}\left(A_{x} B_{y} C_{z}\right)+x \varepsilon^{\Theta}(A)+y \varepsilon^{\Theta}(B)+{ }^{0} z \varepsilon^{\Theta}(C)
\end{aligned}
$$

In the last two steps, we need a few components of data, both experimental and calculated. The value of $\left[H_{\text {corr }}+\varepsilon^{\Theta}\left(A_{x} B_{y} C_{z},\right)\right]$ and $\varepsilon^{\Theta}$ of each atom can be obtained by calculation. The experimental data used are the JANAF values for the heats of formation of $\mathrm{H}, \mathrm{N}, \mathrm{O}, \mathrm{F}$, and Cl atoms at 0 K , as shown in Table 1. ${ }^{22}$ These heats of formation are recommended because they are well-established in literature and tested to be the most appropriate. However, the experimental value for the heat of formation of the boron atom remains controversial.

Yetter et al. ${ }^{23}$ and Leroy et al. ${ }^{24}$ used values adopted by JANAF, while Ruscic et al. ${ }^{25}$ and Curvich et al. ${ }^{26}$ concluded that the JANAF value was too small. Curvich et al. recommended a value of $135 \pm 1.2 \mathrm{~kcal} / \mathrm{mol}$, which is somewhat smaller than the values used by Storms and Mueller. ${ }^{30}$ Schlegel and Harris ${ }^{27}$ and Curtiss et al. ${ }^{28}$ used the values derived by Storms and Mueller. ${ }^{30}$ Martin and Taylor ${ }^{29}$ recently calculated the atomization energy of gaseous boron at 0 K as $136.02 \pm 0.4 \mathrm{kcal} / \mathrm{mol}$.

A comparison with JANAF shows agreement between about half of the system theory and JANAF, while in the other half they differ significantly. Given the level of theory used in recent work and the agreement between the different theoretical methods, we concluded that the values derived by Storms and Mueller should be used. The adopted experimental heats of formation at 0 K for gaseous atoms and $\left[H^{\Theta}(298 \mathrm{~K})-H^{\Theta}(0 \mathrm{~K})\right]$ values for elements are presented in Table 1.




---



# 3. Results and Discussion 

The total energies for each atom $\left(\varepsilon_{0}\right)$ studied in all of the methods are collected in Table 2. Experimental values were obtained from the NIST Atomic Reference Data for Electronic Structure Calculations. The absolute deviation between the value for each atom with each method and the experimental data is 0.3-1.0 in Hartree energy units. However, the deviations between different methods are much smaller and within 0.01 Hartree units. Although the deviations between the calculated and experimental values are not in excellent agreement, we consider the calculated values to be usable for practical applications. This is because the experimental values used four separate approximations in successive columns, while local-density approximation (LDA), which has only one single orbital eigenvalue, was adopted for total energy calculation. ${ }^{31}$ Moreover, the goodness of fit with different methods was high, and calculated systematic errors could be canceled by combining with the values for $\left[\mathrm{H}_{\text {corr }}+\varepsilon_{0}\left(\mathrm{~A}_{x} \mathrm{~B}_{y} \mathrm{C}_{z}\right)\right]$.

In our research, molecular geometries were fully optimized for each computational method. From the calculated molecular geometries, we concluded that most binary compounds of boron are linear molecules and in the $C_{\text {infv }}$ point group. The $\mathrm{BX}_{3}$ molecules we calculated were $\mathrm{BH}_{3}, \mathrm{BF}_{3}$, and $\mathrm{BCl}_{3}$; these molecules have the

[^0]
[^0]:    Table 2. Calculated total energies for each atom and experimental values; all data in the table is given in Hartree energy units.





---

$\mathrm{sp}^{2}$ boron and are in $D_{3 h}$ point group. The molecular geometries of $\mathrm{B}_{2} \mathrm{~F}_{4}$ and $\mathrm{B}_{2} \mathrm{Cl}_{4}$ are planar manifestations of the electron deficiency of boron atoms, ${ }^{32}$ both of them possess a perpendicular $D_{2 d}$ equilibrium geometry rather than planar $D_{2 h}$ ones. In addition, the point group symmetries of $\mathrm{B}_{2} \mathrm{O}_{2}, \mathrm{BOF}, \mathrm{B}_{2} \mathrm{H}_{6}$, and $\mathrm{BH}_{3} \mathrm{O}_{3}$ are $C_{2 V}, C_{\text {inf } v}, D_{2 h}$, and $C_{3 h}$, respectively. Summing the total electronic and thermal enthalpies of each molecular value of $\left[\mathrm{H}_{\text {corr }}+\varepsilon_{0}\left(\mathrm{~A}_{x} \mathrm{~B}_{y} \mathrm{C}_{z}\right)\right]$ was another important task in our work, and the values can be calculated on the basis of the optimized molecular geometries. Thus, using Eq. 4, the resulting $\Delta_{f} H_{298}^{0}$ for each compound, calculated by all of the methods, were obtained and are listed in Table 3.

Several theoretically obtained heats of formation can be found in literature for borides containing light atoms, such as $\mathrm{BH}, \mathrm{BH}_{3}, \mathrm{BF}$, and $\mathrm{BF}_{3}$. Takinstov and Golovin ${ }^{8}$ calculated the heats of formation for $\mathrm{BH}_{3}$ and $\mathrm{BF}_{3}$; the same work had been done by Barreto et al., ${ }^{7}$ but they used HF and the G2 and G3 methods to obtain the heats of formation for these four molecules. When we compared their data and experimental data with our research, the deviations were as small as $1-10 \mathrm{~kJ} \cdot \mathrm{mol}^{-1}$. In particular, for $\Delta_{f} H_{298}^{\mathrm{G} 2}(\mathrm{BH})=442.731 \mathrm{~kJ} \cdot \mathrm{mol}^{-1}$ and $\Delta_{f} H_{298}^{\mathrm{G} 2}\left(\mathrm{BF}_{3}\right)=-1135.749 \mathrm{~kJ} \cdot \mathrm{mol}^{-1}$, the errors when compared to experimental data were 0.031 and $0.251 \mathrm{~kJ} \cdot \mathrm{mol}^{-1}$, respectively. Thus, we consider the ab initio theoretical calculations to be a valid systematic approach towards checking the gas phase heats of formation of borides containing light atoms.

As shown in Table 3, the heats of formation for chlorinated boron compounds also showed good accuracy; $\mathrm{BCl}_{3}$, which was described as difficult to obtain by Bauschlicher, was obtained in our study. The Gaussian-n methods provided great results, with errors of less than $1 \mathrm{~kJ} \cdot \mathrm{mol}^{-1}$. The results for $\mathrm{B}_{2} \mathrm{Cl}_{4}$ also agreed well with the experimental data; the G1, G2, G3, and CBS-QB3 methods were more suitable than the other approaches. In particular, $\Delta_{f} H_{298}^{\mathrm{CBS-QB} 3}$ $\left(\mathrm{B}_{2} \mathrm{Cl}_{4}\right)=-490.446 \mathrm{~kJ} \cdot \mathrm{mol}^{-1}$ was the most precise prediction. Using the same calculations as for $\mathrm{B}_{2} \mathrm{Cl}_{4}$, the heat of formation for $\mathrm{B}_{2} \mathrm{~F}_{4}$ could also be obtained exactly from Gaussian-n methods and their modified methods CBS-QB3 and CBS-Q; the average deviation was about $10 \mathrm{~kJ} \cdot \mathrm{mol}^{-1}$. The error between the G1 results and experiment was $3 \mathrm{~kJ} \cdot \mathrm{mol}^{-1}$, which is somewhat smaller than for the other methods. One problem was that the results for $\mathrm{BF}_{3}$ and $\mathrm{BCl}_{3}$ were better than for BF and BCl; it seems that processing systems containing more halogens is much easier. This can be explained in terms of the boron hybridization - boron does not have to hybridize to form the first bond but must $\mathrm{sp}^{2}$ hybridize to form the second bond and the structural stability of $\mathrm{BX}_{3}(\mathrm{X}=\mathrm{F}, \mathrm{Cl})$ is much better than $\mathrm{BX}(\mathrm{X}=$ $\mathrm{F}, \mathrm{Cl})$. Thus, further optimization and energy calculation should be correspondingly more accurate. Similar arguments do not apply to the analogous H system, as approximating solutions for the light atom system are easier to achieve.

The calculations for the other boron compounds are in reasonable agreement with the experimental values. $\Delta_{f} H_{298}^{\mathrm{CBS}-\mathrm{QB} 3}(\mathrm{BO})=22.365 \mathrm{~kJ} \cdot \mathrm{mol}^{-1}$ and $\Delta_{f} H_{298}^{\mathrm{G} 2 \mathrm{MP} 2}\left(\mathrm{B}_{2} \mathrm{O}_{2}\right)=-452.287 \mathrm{~kJ} \cdot \mathrm{mol}^{-1}$ are the best predictions for the




---

$\begin{array}{lccccccccccc}\text { Species } & \mathrm{G} 1 & \mathrm{G} 2 & \mathrm{G} 3 & \text { CBS-QB } 3 & \text { CBS-4M } & \text { CBS-4O } & \text { CBS-Q } & \mathrm{G} 2 \mathrm{MP} 2 & \mathrm{G} 3 \mathrm{MP} 2 & \mathrm{G} 3 \mathrm{MP} 2 \mathrm{~B} 3 & \mathrm{G} 3 \mathrm{~B} 3 & \text { Exp }{ }^{33,34} \\ \mathrm{BH} & 442.808 & 442.731 & 443.272 & 445.997 & 450.589 & 451.438 & 446.612 & 443.356 & 443.327 & 443.159 & 443.403 & 442.7 \\ \mathrm{BH}_{3} & 108.204 & 104.053 & 106.240 & 108.073 & 109.212 & 110.701 & 107.666 & 107.432 & 113.494 & 114.802 & 107.671 & 89.2 \\ \mathrm{B}_{2} \mathrm{H}_{6} & 56.764 & 48.145 & 50.384 & 55.685 & 56.554 & 59.447 & 54.834 & 54.682 & 62.926 & 65.350 & 53.081 & 36.4 \\ \mathrm{BF} & -110.450 & -100.300 & -104.894 & -103.335 & -94.594 & -97.966 & -106.028 & -108.717 & -105.671 & -105.180 & -103.421 & -122.2 \\ \mathrm{BF}_{3} & -1145.030 & -1135.749 & -1133.386 & -1135.161 & -1116.024 & -1125.029 & -1142.439 & -1137.304 & -1128.043 & -1126.886 & -1129.687 & -1136.0 \\ \mathrm{B}_{2} \mathrm{~F}_{4} & -1437.401 & -1421.887 & -1420.603 & -1422.268 & -1384.153 & -1396.530 & -1432.239 & -1423.735 & -1411.480 & -1412.170 & -1417.720 & -1440.1\end{array}$






---

Fig. 1. Calculated values (G1 method) versus experimental data.
oxidation of boron. The deviations are 2 and $3 \mathrm{~kJ} \cdot \mathrm{mol}^{-1} . \Delta_{f} H_{G 3,298}\left(\mathrm{BH}_{3} \mathrm{O}_{3}\right)=$ $-996.227 \mathrm{~kJ} \cdot \mathrm{mol}^{-1}$ also offered accurate estimates with errors of less than $2 \mathrm{~kJ} \cdot \mathrm{mol}^{-1}$. The deviation in the calculation for BOF was about $20 \mathrm{~kJ} \cdot \mathrm{mol}^{-1}$; however, taking into account the fact that the molecule contains oxygen and a halogen, the result is acceptable. Moreover, the calculation for boron nitride was not as accurate as for the other compounds, with an average standard deviation of $33 \mathrm{~kJ} \cdot \mathrm{mol}^{-1}$. Such deviations from the experimental value could be the results of several theoretical approximations (harmonic, incomplete basis sets, electron correlation, etc.) or could also come from experimental measurements. The experimental measurement for boron nitride was $114.00 \pm 29.9 \mathrm{kcal} \cdot \mathrm{mol}^{-1}$; since the uncertainty value is almost $30 \mathrm{kcal} \cdot \mathrm{mol}^{-1}$, the deviation is more likely related to the experimental measurements.

To show the reliability of predicted heats of formation values for boron compounds, the G1, CBS-QB3, and G2MP2 methods were chosen for comparisons with the experimental data. Based on the results, the linear correlation equations were defined respectively by $y=1.0005 x-2.1629, y=1.0055 x-4.9813$, and $y=1.0054 x-0.3527$. Correlation coefficients $R^{2}$ of 0.9992 , 0.9991 , and 0.9991 were obtained when heats of formation from the literature are plotted along the $x$ axis and heats of formation calculated using the present method along the $y$ axis (Figs. 1-3).

By comparing the results, we note that the mean absolute errors between the calculated data and experimental values from the 11 methods are 13.0, 13.9, 14.1, 14.9, 23.5, 20.5, 13.9, 14.6, 18.4, 19.1, and $16.4 \mathrm{~kJ} \cdot \mathrm{mol}^{-1}$. Therefore, it seems that the values obtained with the Gaussian-n methods are the best among the 11 computational quantum chemical calculations; the various best estimations for each molecule we mentioned prove this. On the other hand, the CBS-4M and CBS-4O




---

Fig. 2. Calculated values (CBS-QB3 method) versus experimental data.

Fig. 3. Calculated values (G2MP2 method) versus experimental data.
had larger mean absolute errors, and the CBS-4M method had the poorest estimation of $\mathrm{B}_{2} \mathrm{~F}_{4}$ with a deviation of up to $56 \mathrm{~kJ} \cdot \mathrm{mol}^{-1}$. Although the CBS-4M and CBS-4O methods are popular computational calculations and can provide accurate estimation for some molecules in some theoretical methods, ${ }^{35}$ it is obvious that the CBS-4 method is not suitable to calculating the heats of formation for boron compounds, especially boron halide, from atomization enthalpy analysis.

Moreover, by comparing the mean absolute error for each method, we noted that CBS-Q, G2MP2, and CBS-QB3 are next to the Gaussian-n methods. Each of G2MP2 and CBS-QB3 provide the best prediction for one of the molecules - $\mathrm{B}_{2} \mathrm{O}_{2}$ and BO, respectively - while the average absolute deviation of CBS-Q method was the smallest of the three methods. Recently, Chin et al. employed G2MP2 theory to investigate the energies of BO and $\mathrm{B}_{2} \mathrm{O}_{2} .{ }^{36}$ Since these methods are suitable




---

for $\mathrm{BO}$ and $\mathrm{B}_{2} \mathrm{O}_{2}$, we recommend that G2MP2 and CBS-QB3 methods be used to produce the heat of formation values for other oxidations of boron.

The accuracy of each method also has a certain relation with the computing time. To give an extensive comparison, excluding CBS-4M and CBS-4O in calculating $\mathrm{BCl}_{3}$, in terms of time consumption, the various methods rank, in descending order, as G1, G3, G3B3, CBS-Q, CBS-QB3, G3MP2B3, G3MP2, G2MP2, and G2. We have previously noted that these methods rank almost the same in terms of accuracy. The G1 method provides the most accurate estimation and has the most computational cost as well. The computational cost of G3 theory is second only to G1 and the accuracy is almost as good. The modifications of Gaussian-n methods greatly reduce the time overhead through second-order Moller-Plesset perturbation theory or further geometry calculation, and the results are acceptable. In addition, we should mention that the G2 method provides the second greatest agreement between the calculated and experimental values with the least time consumption. On the basis of the above analysis, we believe that Gaussian-n methods are suitable for calculating heats of formation based on atomization enthalpy analysis, and G2 is the best choice to predict HOFs for borides in terms of accuracy and time efficiency.

# 4. Conclusions 

With the help of computational techniques, we analyzed the molecular geometries of several boron compounds. A variety of theoretical available methods were applied to estimate the heats of formation at 298.15 K for $\mathrm{BH}, \mathrm{BH}_{3}, \mathrm{~B}_{2} \mathrm{H}_{6}, \mathrm{BF}, \mathrm{BF}_{3}, \mathrm{~B}_{2} \mathrm{~F}_{4}$, $\mathrm{BCl}, \mathrm{BCl}_{3}, \mathrm{~B}_{2} \mathrm{Cl}_{4}, \mathrm{BO}, \mathrm{B}_{2} \mathrm{O}_{2}, \mathrm{BN}, \mathrm{BOF}$, and $\mathrm{BH}_{3} \mathrm{O}_{3}$ molecules. Good agreement was found between our calculations and the experimental values for both borohydride and chlorinated boron compounds. For several molecules we analyzed, the deviation was reasonable and within the experimental error bar. We also made comparisons with thermodynamic data taken from other literature and our values. In addition, we recommend some suitable theoretical methods for future work with borides.

## References

1. Stantos DMF, Sequeira CAC, J Electrochem Soc 156:F67, 2009.
2. Lee TM, Hak OJ, Anna DR, Zhennan B, J Amer Chem Soc 131:3733, 2009.
3. Karton A, Martin JML, J Phys Chem A 111:5936, 2007.
4. Barone V, Minichino C, Theor Chim Acta 76:53, 1989.
5. Rablen PR, Hartwig JF, J Am Chem Soc 118, 1996.
6. Bauschlicher CW, Ricca Jr A, J Phys Chem A 103:4313, 1999.
7. Barreto PRP, Vilela AFA, Gargano R, Int J Quant Chem 103:659, 2005.
8. Takhistov VV, Golovin AV, J Mol Struct 784:47, 2006.
9. Ricca A, Bauschlicher CW, J Phys Chem 102:876, 1998.
10. Pardoe JAJ, Norman NC, Timms PL, Polyhedron 21:543, 2002.
11. Curtiss LA, Raghavachari K, Pople JA, J Chem Phys 98:1293, 1993.



---

12. Curtiss LA, Redfern PC, Raghavachari K, Pople JA, Chem Phys Lett 359:390, 2002.
13. $\mathrm{Li} \mathrm{XH, Zhang RZ, Zhang XZ, Cheng XL, Yang XD, J Theor Comput Chem 6: 675}$, 2007
14. Montgomery JA, Frisch MJ, Ochterski JW, Petersson GA, J Chem Phys 112:6532, 2000.
15. Verevkin SP, Emel'yanenko VN, Toktonov AV, J Chem Thermodynamics 40:1428, 2008
16. Fabian WMF, Janoschek R, Combustion Flame 145:282, 2006.
17. Stein K, Stian S, Bjornar A, J Phys Chem A 113:1869, 2009.
18. Curtiss LA, Redfern PC, Raghavachari K, J Chem Phy 126:1, 2007.
19. Huh SB, Lee JS, J Chem Phys 118:3035, 2003.
20. Baboul AG, Curtis LA, Redfern PC, Raghavachari K, J Chem Phys 110:7650, 1999.
21. Frisch MJ, Trucks GW, Schlegel HB, Scuseria GE, Robb MA, Cheeseman JR, Montgomery Jr JA, Vreven T, Kudin KN, Burant JC, Millam JM, Iyengar SS, Tomasi J, Barone V, Mennucci B, Cossi M, Scalmani G, Rega N, Petersson GA, Nakatsuji H, Hada M, Ehara M, Toyota K, Fukuda R, Hasegawa J, Ishida M, Nakajima T, Honda Y, Kitao O, Nakai H, Klene M, Li X, Knox JE, Hratchian HP, Cross JB, Bakken V, Adamo C, Jaramillo J, Gomperts R, Stratmann RE, Yazyev O, Austin AJ, Cammi R, Pomelli C, Ochterski JW, Ayala PY, Morokuma K, Voth GA, Salvador P, Dannenberg JJ, Zakrzewski VG, Dapprich S, Daniels AD, Strain MC, Farkas O, Malick DK, Rabuck AD, Raghavachari K, Foresman JB, Ortiz JV, Cui Q, Baboul AG, Clifford S, Cioslowski J, Stefanov BB, Liu G, Liashenko A, Piskorz P, Komaromi I, Martin RL, Fox DJ, Keith T, Al-Laham MA, Peng CY, Nanayakkara A, Challacombe M, Gill PMW, Johnson B, Chen W, Wong MW, Gonzalez C, Pople JA, Gaussian 03, Revision C.02, Gaussian, Inc., Wallingford CT, 2004
22. Curtiss LA, Raghavachari K, Paul CR, J Chem Phys 106:1063, 1997.
23. Yetter RA, Rabitz H, Dryler FL, Brown C, Kolb CE, Combust Flame 83:43, 1991.
24. Leroy C, Sana M, Wilante C, van Zieleghem MJ, J Mol Struct 247:199, 1991.
25. Ruscic B, Mayhew CA, Berkowitz J, J Chem Phys 88:5580, 1988.
26. Curvich LV, Veyts IV, Alcock CB, Thermodynamic Properties of Individual Substances, Vol. 3, CRC Press: Boca Raton, FL, 1994
27. Schlegel HB, Harris SJ, J Phys Chem 98:11178, 1994.
28. Curtiss LA, Raghavachari KL, Redfern PC, Pople JA, J Chem Phys 106:1063, 1997.
29. Martin JML, Taylor PR, J Phys Chem A 102:2995, 1998
30. Storms E, Mueller B, J Phys Chem 81:318, 1977.
31. http://physis.nist.gov/PhysRefData/DFTdata/Tables/ptable.html (NIST. Atom Reference Data for Electronic Structure Calculations).
32. Jun-ichi A, Hideaki K, Toshimasa I, J Amer Chem Soc 127:13324, 2995.
33. Gurvich LV, Veyts IV, Alcock CB, Thermodynamic Properties of Individual Substances, 4th edn., Vol. 1, Hermisphere Publishing Corp., New York, 1989
34. Gurvich LV, Veyts IV, Alcock CB, Thermodynamic Properties of Individual Substances, 4th edn., Vol. 3, CRC Press, Boca Raton, FL, 1994.
35. Li XH, Zhang RZ, Cheng XL, Yang XD, J Theor Comput Chem 6:449, 2007
36. Chin CH, Mebel AM, Hwang DY, J Phys Chem A 108:473, 2004.



---

