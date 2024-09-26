# Next Generation Safety Analysis Methods for SFRs (8) Analyses of Eutectics Between Fuel and Steel in Metal Fuel with FPMD Code VASP 

Masashi Himi, Yuichi Yamamoto<br>Analysis and Simulation Div., Japan Systems Corporation,<br>Minami-cho, Kawasaki-ku, Kawasaki, Kanagawa 210-0015, Japan<br>E-mail: himi.masashi@jskk.co.jp<br>Yasuo Nagamine, Noriyuki Shirakawa, Yasushi Uehara<br>The Institute of Applied Energy

Tatsumi Arima<br>Kyushu University


#### Abstract

There are two main objectives in this study. One is to estimate atomic diffusion coefficients in eutectic reaction between metal fuel and cladding materials in order to establish the atomic diffusion model for the COMPASS code. The other is to estimate their material properties such as Young's modulus in high temperature up to near melting points in core disruptive accidents (CDAs) in Sodium-cooled Fast Reactors (SFRs). We used the first principle molecular dynamics (FPMD) code VASP to realize the two objectives. We tried to understand the initiation mechanism of eutectics based on change of electronic state energy accompanied by change of Kohn-Sham energy, including phonon effect. In this project [1], three methods, phase diagram calculation (CALPHAD), classical molecular dynamics (CMD), and FPMD, are employed to understand the mechanism of eutectics and to introduce dynamic characteristics in eutectic phenomena into the COMPASS code.


## NOMENCLATURE

$a$ : Lattice constant
$D$ : Diffusion coefficient of ions or atoms
$E_{K S}: \quad$ Kohn-Sham energy
$E_{X C}: \quad$ Exchange correlation energy
$E_{B}: \quad$ Band structure energy
$k_{B}: \quad$ Boltzmann constant
$N_{\text {ion }}: \quad$ Number of ions
$n$ : One-body density of electron
$R$ : Gas constant
$R_{I}^{t}: \quad$ Coordinate of nucleus or ion $I$
$r^{t}: \quad$ Coordinate of electron
$s$ : sound velocity
$t$ : Time
$T$ : Temperature
$u$ : Displacement of an atom around the node point of lattice due to thermal fluctuation
$V_{H}: \quad$ Hartree energy
$x$ : mixing ratio of metal atoms
$k_{D}: \quad$ wave number at Debye temperature
Greek Symbols
$\alpha$ : Index for Lindemann's criterion of melting
$\varepsilon_{i}: \quad$ Energy of state of the Kohn-Sham orbital $i$
$\omega$ : Frequency of phonon
$\Theta_{D}: \quad$ Debye temperature

## Subscript

$I, J: \quad$ Nucleus or ion number
$i, j: \quad$ Electron number
$I$ : Nucleus or ion

## 1 INTRODUCTION

Eutectic reaction between metal fuel and steel cladding and/or steel structures is possibly caused in SFR's CDA. We have been studying this phenomenon with three kind of methods, CALPHAD, CMD, and FPMD since FY2005 [1,2,3]. In this paper, results of the analyses performed with the VASP code [4] until the end of FY2007, will be presented.

We have investigated phase transition and eutectics in the systems containing small number of atoms of solid solution with




---

multi-kind of atoms and pure metal. We carried out FPMD analyses of the systems of $\mathrm{Zr}-\mathrm{U}$ and $\mathrm{U}-\mathrm{Fe}$ each with 16 -atom and tried to extract physical characteristics describing eutectics from electronic states, where the characteristics are Kohn-Sham energy, band structure energy, exchange-correlation energy etc. These analyses suggested that eutectics occur mainly depending on the intensity of metallic bond that depends on atomic composition.

We have also evaluated the phase diagram for the crystal structure of U-Fe 16-atom, by introducing phonons into free energy formulation to realize finite temperature state from the crystal structure optimized in 0 K . In this investigation, we showed the process to evaluate the phase diagram of eutectics quantum-mechanically, which would be utilized to judge eutectics occurrence.

FPMD has been also applied to the evaluation of metal fuel material properties. We evaluated melting points based on the change of Kohn-Sham energy in order to simulate empirical solidus line of U-Pu-Zr metal fuel. However, evaluated line was not in good agreement due to small number of atoms and small number of calculation cases.

Calculating the system of $\mathrm{U}-\mathrm{Pu}-\mathrm{Zr}$ contacting with Fe until 1ps, we observed melting on the interface judging from Lindemann's criterion on melting. Using these results, we evaluated atomic diffusion coefficient across the interface, extracting issues with respect to computing time and the derived limitations. The coefficient could be meaningfully evaluated even in this small time interval and could be utilized in the atomic diffusion model for COMPASS code [1].

## 2 ANALYSES OF ENERGY STATES OF METAL FUEL AND Fe

After preparing "optimized state", which is the crystal state of mixed metal fuel and Fe atoms that has minimum energy at near zero pressure and 0 K obtained by adjusting lattice constants, energy states were analyzed by FPMD method with phonon effect, increasing temperature.

### 2.1 ANALYSES OF U-Fe AND U-Zr SYSTEMS

Potential energy of eutectic atomic system such as U-Fe becomes smaller than the average potential energy of U-U and Fe-Fe [3]. We related this fact to energy change of electronic state to systematically understand eutectic initiation.

We selected and analyzed two mixed 16-atomic systems, one is $\mathrm{U}-\mathrm{Zr}$ that had no eutectics and the other is $\mathrm{U}-\mathrm{Fe}$ that had eutectics. Phase diagrams of U-Zr and U-Fe are shown in Fig. 1 and Fig. 2 calculated with the ThermoCalc code based on CALPHAD [5,6], where analyzed cases are shown with three and five red circles, respectively. These eight cases are $\mathrm{Zr}_{16}$, $\mathrm{U}_{8} \mathrm{Zr}_{8}, \mathrm{U}_{16}$ in Fig. 1 and $\left(\mathrm{U}_{16}\right), \mathrm{U}_{12} \mathrm{Fe}_{4}, \mathrm{U}_{8} \mathrm{Fe}_{8}, \mathrm{U}_{4} \mathrm{Fe}_{12}$, $\mathrm{Fe}_{16}$ in Fig.2. $\mathrm{U}_{16}$ case is the same in $\mathrm{U}-\mathrm{Zr}$ and $\mathrm{U}-\mathrm{Fe}$. Note that melting points of $\mathrm{Zr}, \mathrm{U}$ and Fe are $2125 \mathrm{~K}, 1405.5 \mathrm{~K}$ and 1808 K , respectively [7].



Fig. 1 Phase diagram of U-Zr (O:melting point)



Fig. 2 Phase diagram of U-Fe (O:melting point)
Two-body correlation functions for seven cases are shown in Fig.3-Fig.9. Each case clearly leaves crystal correlation structure at 500 K in liquid state at higher temperatures, showing that crystal state does not change so much that it makes difficult to discriminate liquid state from solid one by Lindemann's criterion on melting.




---



Fig. 3 Calculated two-body correlation functions in $\mathrm{Zr}_{16}$.



Fig. 4 Calculated two-body correlation functions in $\mathrm{Zr}_{8} \mathrm{U}_{8}$.



Fig. 5 Calculated two-body correlation functions in $\mathrm{U}_{16}$.



Fig. 6 Calculated two-body correlation functions in $\mathrm{U}_{12} \mathrm{Fe}_{4}$.



Fig. 7 Calculated two-body correlation functions in $\mathrm{U}_{8} \mathrm{Fe}_{8}$.



Fig. 8 Calculated two-body correlation functions in $\mathrm{U}_{4} \mathrm{Fe}_{12}$.



Fig. 9 Calculated two-body correlation functions in $\mathrm{Fe}_{16}$.
Eigen values of occupied electronic states included in these seven electronic density of states at 500 K and 2500 K are shown in Fig. 10 and Fig.11, respectively. These eigen values are averaged over wave number space since they distribute in the k -space direction.

Electron configurations of $\mathrm{Zr}, \mathrm{Fe}$ and U are
$\mathrm{Zr}:[\mathrm{Kr}] 5 \mathrm{~s}^{2} 4 \mathrm{~d}^{2}$,
$\mathrm{Fe}:[\mathrm{Ar}] 4 \mathrm{~s}^{2} 3 \mathrm{~d}^{6}$, and
$\mathrm{U}:[\mathrm{Rn}] 7 \mathrm{~s}^{2} 5 \mathrm{f}^{3} 6 \mathrm{~d}^{1}$, respectively, where
$[\mathrm{Ar}]=\left(1 \mathrm{~s}^{2}\right)\left(2 \mathrm{~s}^{2} 2 \mathrm{p}^{6}\right)\left(3 \mathrm{~s}^{2} 3 \mathrm{p}^{6}\right)$,
$[\mathrm{Kr}]=\left(1 \mathrm{~s}^{2}\right)\left(2 \mathrm{~s}^{2} 2 \mathrm{p}^{6}\right)\left(3 \mathrm{~s}^{2} 3 \mathrm{p}^{6}\right)\left(4 \mathrm{~s}^{2} 3 \mathrm{~d}^{10} 4 \mathrm{p}^{6}\right)$, and
$[\mathrm{Rn}]=\left(1 \mathrm{~s}^{2}\right)\left(2 \mathrm{~s}^{2} 2 \mathrm{p}^{6}\right)\left(3 \mathrm{~s}^{2} 3 \mathrm{p}^{6}\right)\left(4 \mathrm{~s}^{2} 3 \mathrm{~d}^{10} 4 \mathrm{p}^{6}\right)\left(5 \mathrm{~s}^{2} 4 \mathrm{~d}^{10} 5 \mathrm{p}^{6}\right)\left(6 \mathrm{~s}^{2} 4 \mathrm{f}^{14} 5 \mathrm{~d}^{10} 6 \mathrm{p}^{6}\right)$.




---

With respect to Uranium, VASP considers 6 s and 6 p orbitals as valence states and the number of valence electrons is 14. The numbers of valence electrons are 4 in Zr , and 8 in Fe . Mixing of $U$ with Zr or Fe does not change the number of electron states inside those of 6 s and 6 p orbitals, which number of states are shown in both Fig. 10 and Fig.11. For $\mathrm{U}_{12} \mathrm{Fe}_{4}$ and $\mathrm{U}_{4} \mathrm{Fe}_{12}$, the numbers of occupied states per 4 atoms are shown to avoiding fractions. Note that two electrons can seat in one state because spin states are contracted.

From these two figures, it is found that the energy at 2500K (liquid) decreases compared with that at 500 K (solid) in $\mathrm{U}_{12} \mathrm{Fe}_{4}$ and $\mathrm{U}_{4} \mathrm{Fe}_{12}$. On the other hand, energy change in $\mathrm{U}_{8} \mathrm{Fe}_{8}$ is clearly smaller than these two systems. Furthermore, energy change in $\mathrm{Zr}-\mathrm{U}$ is not as significant as that in $\mathrm{Fe}-\mathrm{U}$ is. That is, we could assume that the energy of electronic states in $\mathrm{U}_{12} \mathrm{Fe}_{4}$ and $\mathrm{U}_{4} \mathrm{Fe}_{12}$ that cause eutectics decreases at the temperature higher enough than melting point.

Since FPMD calculations of small number of atoms with finite temperature are often accompanied by large fluctuation, we continued the calculation until the average energy reaches near constant. The following consideration is based on the averaged energy. The energy change without thermal fluctuation at 0 K is shown in Ref.[3].



Fig. 10 Eigen values of occupied states in $\mathrm{Zr}-\mathrm{U}-\mathrm{Fe}$ at 500 K .



Fig. 11 Eigen values of occupied states in $\mathrm{Zr}-\mathrm{U}-\mathrm{Fe}$ at 2500 K .
Kohn-Sham energy is described in Eq.(1),

$$
E_{K S}=E_{v}^{H}+\int \frac{1}{2} V_{r}\left[n_{v}(\overline{\mathbf{r}})\right] d \overline{\mathbf{r}}+\int \varepsilon_{X C}\left[n_{v}(\overline{\boldsymbol{r}})\right] d \overline{\mathbf{r}}+\sum_{i}\left\langle\chi_{i}\left|\frac{\partial \varepsilon_{X C}\left[n_{v}\right]}{\partial n_{v}}\right| \chi_{i}\right\rangle
$$

where the first term in RHS is the band structure energy $\left(E_{B}\right)$ which is the summation of eigen values of electronic states, the second is the Hartree energy $\left(V^{H}\right)$ of coulomb interaction multiplied by $(-1 / 2)$, the third and the forth denote the exchange-correlation interaction for valence electrons.

Phase change from solid to liquid generates energy corresponding to latent heat. Therefore, Kohn-Sham energy as a function of temperature forms an ogive as shown in Fig.12. We assume that melting point is an inflection point of the ogive.

We scaled the Kohn-Sham energy and the temperature, as

$$
f\left(E_{K S}\right)=\frac{E_{K S}(T)-E_{K S}(500 K)}{E_{K S}(2500 K)-E_{K S}(500 K)}
$$

and

$$
f(T)=\frac{\left(T-T_{K}(500 K)\right)}{\left(T_{K}(2500 K)-T_{K}(500 K)\right)}
$$

respectively. Then, the melting point is the temperature that the ogive Eq.(2) exceeds Eq.(3), that is when the ogive becomes convex. Estimated melting temperatures are $>2125 \mathrm{~K}$ for $\mathrm{Zr}_{16}$, $>1600 \mathrm{~K}$ for $\mathrm{U}_{8} \mathrm{Zr}_{8}, 1405.5 \mathrm{~K}$ for $\mathrm{U}_{16}, 1000 \mathrm{~K}$ for $\mathrm{U}_{12} \mathrm{Fe}_{4}$, 1400-1800K for $\mathrm{U}_{8} \mathrm{Fe}_{8}, 1400 \mathrm{~K}$ for $\mathrm{U}_{4} \mathrm{Fe}_{12}$, and 1808 K for $\mathrm{Fe}_{16}$, respectively, which are good estimates.



Fig. 12 Dependence of Kohn-Sham energy on temperature for $\mathrm{U}-\mathrm{Fe}$ and $\mathrm{U}-\mathrm{Zr}$ systems.

Eq.(4) is the nondimensionalized band structure energy $E_{B}$ per one valence electron,

$$
f\left(E_{B}\right)=\frac{E_{B}(T)-E_{B}(500 K)}{E_{B}(2500 K)-E_{B}(500 K)}
$$

which is shown in Fig. 13. Comparing $f\left(E_{B}\right)$ of each system, $\mathrm{Zr}_{8} \mathrm{U}_{8}$ does not fall below $\mathrm{Zr}_{16}$ and $\mathrm{U}_{16}$. Meanwhile $\mathrm{U}_{12} \mathrm{Fe}_{4}$ and $\mathrm{U}_{8} \mathrm{Fe}_{8}$ fall below both $\mathrm{U}_{16}$ and $\mathrm{Fe}_{16}$ at 1400 K and $1400-$ 1800 K , respectively, which shows the electronic state energy in U-Fe system decreases across the phase change, in contrast that in $\mathrm{Zr}-\mathrm{U}$ system does not.

In the same way Hartree energy $V^{H}$ (positive) is also nondimensionalized as Eq.(5),




---

$$
g\left(V_{H}\right)=\frac{V_{H}(T)}{V_{H}(500 \mathrm{~K})+\left\{V_{H}\left(500 \mathrm{~K}^{2}\right)\right)}
$$

which is shown in Fig.14. $g\left(V_{H}\right)$ of each system increases as temperature rises.



Fig. 13 Dependence of band structure energy on temperature for $\mathrm{U}-\mathrm{Fe}$ and $\mathrm{U}-\mathrm{Zr}$ systems.



Fig. 14 Dependence of Hartree energy on temperature for $\mathrm{U}-\mathrm{Fe}$ and $\mathrm{U}-\mathrm{Zr}$ systems.



Fig. 15 Dependence of exchange-correlation energy on temperature for $\mathrm{U}-\mathrm{Fe}$ and $\mathrm{U}-\mathrm{Zr}$ systems.

We also nondimensionalized the exchange-correlation energy $\left(E_{X C}-V_{X C}\right.$ : negative in $\mathrm{Zr}_{16}, \mathrm{Zr}_{8} \mathrm{U}_{8}, \mathrm{U}_{16}$ and positive in $\mathrm{U}_{12} \mathrm{Fe}_{4}, \mathrm{U}_{8} \mathrm{Fe}_{8}, \mathrm{U}_{4} \mathrm{Fe}_{12}, \mathrm{Fe}_{16}$ ) as Eq.(6),

$$
g\left(E_{X C}-V_{X C}\right)=\frac{\left(E_{X C}-V_{X C}\right)(T)}{\left(E_{X C}-V_{X C}\right)(500 \mathrm{~K})+\left\{\left(E_{X C}-V_{X C}\right)(500 \mathrm{~K})\right\}}
$$

which is shown in Fig.15. $g\left(E_{X C}-V_{X C}\right)$ of $\mathrm{Zr}_{8} \mathrm{U}_{8}$ has little dependence on temperature, meanwhile those of $\mathrm{U}_{12} \mathrm{Fe}_{4}$, $\mathrm{U}_{8} \mathrm{Fe}_{8}$, and $\mathrm{U}_{4} \mathrm{Fe}_{12}$ has clear dependence on temperature. We presume the initiation mechanism of eutectics based on these analyses that the Kohn-Sham energy increases around melting point by the latent heat through phase change, the band structure energy decreases, and the exchange-correlation energy changes. Namely, the electronic state energy changes in a certain composition of atoms, which affect the metallic bond.

### 2.2 Phonon effect

We statically analyzed optimized energy states for some UFe systems of 16 -atom using VASP with phonon model [8]. Since Fe-crystal structure is bcc and U-crystal structure is orthorhombic at 0 K , we calculated optimized state in each structure, changing composition ratio. Generally speaking, stability of crystal can be explained by estimating its free energy. Figure 16 shows two free energy curves for bcc and orthorhombic for each atomic composition, and tangent line common to the two curves. As tangent point corresponds to the equilibrium state in the atomic composition, coexistent domain between bcc and orthorhombic, that is eutectic domain, can be estimated. This result roughly reproduces the phase diagram shown in Fig. 2.



Fig. 16 Eutectic domain of U-Fe system at 0 K .
The main effect of finite temperature is thermal fluctuation of crystal structure, which fluctuation can be interpreted as phonons. Therefore, we calculated the contribution of phonons to the free energy as well as the entropy of mixing atoms, stopping the ion motion and simulating lattice oscillation with phonons.
Free energy $G$ of a system is described by Eq.(7),




---

$$
G=T S_{\text {mix }}+E_{0}(\mathbf{x})-\frac{1}{N_{A}} \cdot F_{p h}
$$

where the first term in RHS is the cohesive energy that is obtained from optimization analysis at $0 \mathrm{~K}, S_{\text {mix }}$ is the mixing entropy,
$S_{\text {mix }}=R\left\{x \ln x+(1-x) \ln (1-x)\right\}$,
and $F_{p h}$ is the free energy of phonons,

$$
F_{p h}=\sum_{l} \frac{1}{2} \hbar \omega_{l}+\frac{\hbar}{k_{B} T} \sum_{l} \omega_{l}\left(1+\ln \left(1-e^{-\frac{-1 \omega_{l}}{k_{B} T}}\right)\right)
$$

Here, we used Avogadro number $N_{A}$ and Boltzmann constant $k_{B}$ in [1/mole] and [J/K], respectively, for consistent representation.

We calculated again similar cases in Fig. 16 under finite temperature to estimate dependence of coexistence domain on temperature as shown in Fig.17. The dotted lines in this figure are shown for comparison based on the data shown in Fig.2. Calculated coexistence domain tends to narrow as the temperature rises.

Although calculated coexistence domain has some shift from empirical data, our procedure to quantum mechanically reproduce phase diagram is found to be appropriate and effective.



Fig. 17 Dependence of eutectic domain of U-Fe system on temperature.

## 3 SIMULATION of Metal fuel U-Pu-Zr

From a practical viewpoint of metal fuel, U-Pu-Zr is superior to U-Pu because the former has higher melting point and can coexist with stainless steel cladding due to smaller eutectic reaction rate. We calculated melting points of U-Pu-Zr, changing composition as
$\mathrm{U}_{76 \%} \mathrm{Pu}_{24 \%}\left(\mathrm{U}_{41}, \mathrm{Pu}_{13}\right.$ atoms $)$,
$\mathrm{U}_{50 \%} \mathrm{Pu}_{24 \%} \mathrm{Zr}_{26 \%}\left(\mathrm{U}_{27}, \mathrm{Pu}_{13}, \mathrm{Zr}_{14}\right.$ atoms $)$,
$\mathrm{U}_{26 \%} \mathrm{Pu}_{24 \%} \mathrm{Zr}_{50 \%}\left(\mathrm{U}_{14}, \mathrm{Pu}_{13}, \mathrm{Zr}_{27}\right.$ atoms $)$.
Analytically estimated solidus lines of U-Pu-Zr are shown in Fig. $18[9]$.

Preparing uniformly mixed system for each composition, the system was optimized at each temperature. Two-body correlation functions are shown in Fig.19-Fig.21.

Each case clearly leaves crystal structure even after melting in the same way in section 2.1.



Fig. 18 Solidus lines of U-Pu-Zr Alloys [9]



Fig. 19 Calculated two-body correlation functions in $\mathrm{U}_{76 \%} \mathrm{Pu}_{24 \%}$



Fig. 20 Calculated two-body correlation functions in $\mathrm{U}_{50 \%} \mathrm{Pu}_{24 \%} \mathrm{Zr}_{26 \%}$




---



Fig. 21 Calculated two-body correlation functions in $\mathrm{U}_{26 \%} \mathrm{Pu}_{24 \%} \mathrm{Zr}_{50 \%}$

The average and standard deviation of both Kohn-Sham energy and band structure energy in each case was calculated and shown in Fig.22-Fig.27, where cases of $\mathrm{U}_{100 \%}\left(\mathrm{U}_{16}\right)$, $\mathrm{U}_{50 \%} \mathrm{Zr}_{50 \%}\left(\mathrm{U}_{8}, \mathrm{Zr}_{8}\right), \mathrm{Zr}_{100 \%}\left(\mathrm{Zr}_{16}\right)$ are the same in section 2.1. The deviation of band structure energy is much smaller than that of Kohn-Sham energy.

Point estimate of melting temperature is not obtained due to the variation of temperature in FPMD. Deviation of KohnSham energy is large enough to form clear ogive curve so that the accuracy of flexion point to give melting temperature is not good.

The reading of melting temperature in Fig. 18 is compared for each case with calculated results, giving appropriate results, as follows.

| Solidus line | Calculation |  |
| :---: | :---: | :---: |
|  | $\mathrm{U}_{76 \%} \mathrm{Pu}_{24 \%}:$ | 1200 K |
|  | $\mathrm{U}_{50 \%} \mathrm{Pu}_{24 \%} \mathrm{Zr}_{26 \%}:$ | $1000-1400 \mathrm{~K}$ |
|  | $\mathrm{U}_{50 \%} \mathrm{Pu}_{24 \%} \mathrm{Zr}_{26 \%}:$ | 1400 K |
|  | $\mathrm{U}_{26 \%} \mathrm{Pu}_{24 \%} \mathrm{Zr}_{50 \%}:$ | $1200-1600 \mathrm{~K}$ |
|  | $\mathrm{U}_{100 \%}:$ | 1600 K |
|  |  | $1400-1800 \mathrm{~K}$ |
|  | $\mathrm{U}_{50 \%} \mathrm{Zr}_{50 \%}:$ | 1405 K |
|  |  | $1200-1800 \mathrm{~K}$ |
| $\mathrm{Zr}_{100 \%}:$ | 1700 K | $1400-2100 \mathrm{~K}$ |
|  | 2125 K | $1800-2500 \mathrm{~K}$ |

Note that broader temperature deviation in $\mathrm{U}_{100 \%}$, $\mathrm{U}_{50 \%} \mathrm{Zr}_{50 \%}$, and $\mathrm{Zr}_{100 \%}$ is caused by small number of 16 atoms engaged for each case, meanwhile 54 atoms are used in $\mathrm{U}_{76 \%} \mathrm{Pu}_{24 \%}, \mathrm{U}_{50 \%} \mathrm{Pu}_{24 \%} \mathrm{Zr}_{26 \%}$, and $\mathrm{U}_{26 \%} \mathrm{Pu}_{24 \%} \mathrm{Zr}_{50 \%}$.



Fig. 22 Average and standard deviation of Kohn-Sham energy and band structure energy in $\mathrm{U}_{76 \%} \mathrm{Pu}_{24 \%}$



Fig. 23 Average and standard deviation of Kohn-Sham energy and band structure energy in $\mathrm{U}_{50 \%} \mathrm{Pu}_{24 \%} \mathrm{Zr}_{26 \%}$



Fig. 24 Average and standard deviation of Kohn-Sham energy and band structure energy in $\mathrm{U}_{26 \%} \mathrm{Pu}_{24 \%} \mathrm{Zr}_{50 \%}$




---



Fig. 25 Average and standard deviation of Kohn-Sham energy and band structure energy in $\mathbf{U}_{100 \%}$



Fig. 26 Average and standard deviation of Kohn-Sham energy and band structure energy in $\mathbf{U}_{50 \%} \mathbf{Z r}_{50 \%}$



Fig. 27 Average and standard deviation of Kohn-Sham energy and band structure energy in $\mathrm{Zr}_{100} \%$

## 4 CONTACT ANALYSIS BETWEEN METAL FUEL UPu-Zr AND CLADDING Fe

Contact analysis between metal fuel and cladding Fe is supposed to investigate eutectics formation process in pin failure stage in CDA.

Melting point $\left(T_{m}\right)$ of standard metal fuel $\left(\mathbf{U}_{50 \mathrm{at} \%}\right.$, $\mathbf{P u}_{25 a t} \%, \mathbf{Z r}_{25 a t} \%$ ) is about 1400 K as shown in Fig. 18 and that of Fe is about 1808 K . We analyzed two cases at $1300 \mathrm{~K}\left(<T_{m}\right)$ and $1500 \mathrm{~K}\left(>T_{m}\right)$ of system temperature to examine the difference of electronic states.

The U-Pu-Zr system is composed of $\mathrm{U}_{48}, \mathrm{Pu}_{24}$ and $\mathrm{Zr}_{24}$ atoms, 96 atoms in all. U, Pu and Zr atoms are uniformly contained in the system.

The Fe system has 150 Fe atoms in bcc, and this system was prepared to have optimized lattice constants with adjusted pressure at both 1300 K and 1500 K .

Conforming the size of Fe basic cell $(5 \times 5)$ to U-Pu-Zr basic cell $(4 \times 4)$, Fe system was set upper and U-Pu-Zr system lower to make combined system with gap of one Fe basic cell for both 1300 K and 1500 K cases. Cyclic boundary conditions are imposed on this structure as a supercell. This calculation was the largest one we had done until FY2007, so we aimed to calculate up to 1 ps with time step 3 fs to investigate how Fe atoms diffuse into metal fuel through the interface.

Position of atoms, diffusion coefficient, and the index for Lindemann's criterion of melting [10,11] (we call this Lindemann index, shortly hereafter) at 1300 K are shown in Fig.28-Fig.30, and those at 1500 K in Fig.31-Fig. 33 in the end time of calculation, respectively.

Diffusion coefficients $D$ in 1300 K and 1500 K cases are shown in Fig. 29 and Fig. 30, respectively, where $D$ is defined as
$D(\infty)=\lim _{t \rightarrow \infty} D(t)=\lim _{t \rightarrow \infty} \frac{1}{6 N_{I o n}}\left\langle\sum_{i}\left[R^{i}(t)-R^{i}(0)\right]^{2}\right\rangle_{t}$.
Lindemann index $\alpha$ in 1300 K and 1500 K cases are shown in Fig. 30 and Fig. 33, respectively. Equation (11) describes the relation between $\alpha$ and $D$,
$\alpha^{2}(t)=\left\langle u^{2}(t)\right\rangle / a^{2}=\left[6 D(t) \cdot t / a^{2}\right]^{1 / 2}$.
In the beginning of calculation, Zr -atom near the interface starts moving because of its small mass. U- and Pu -atom begin to move affected by Zr -atom displacement.

In the 1300 K case, $D \mathrm{~s}$ of $\mathrm{U}, \mathrm{Pu}$ and Zr approaches to the bulk $D$. Displacement of Fe -atom is smaller because its melting temperature is higher than 1300 K . $D$ converges on a constant and diffusion starts when $\alpha$ becomes proportional to time. In this case, as the index does not become proportional to time until 1 ps , melting through the interface is not judged to occur, which is appropriate because the melting point of metal fuel, around 1400 K , is much higher than 1300 K .

In the 1500 K case, calculation is much more time consuming than the 1300 K case. As shown in Fig.33, time history of the index is not long enough to judge convergence. Parallel calculations with more CPUs have been performed in FY2008.




---



Fig. 28 Atomic configuration in the contact calculation between metal fuel U-Pu-Zr and cladding Fe at 1300 K (at 630 fs ).



Fig. 29 Diffusion coefficient in the contact calculation between metal fuel U-Pu-Zr and cladding Fe at 1300 K .



Fig. 30 Lindemann index in the contact calculation between metal fuel U-Pu-Zr and cladding Fe at 1300 K .



Fig. 31 Atomic configuration in the contact calculation between metal fuel U-Pu-Zr and cladding Fe at 1500 K (at 300 fs ).



Fig. 32 Diffusion coefficient in the contact calculation between metal fuel U-Pu-Zr and cladding Fe at 1500 K .



Fig. 33 Lindemann index in the contact calculation between metal fuel U-Pu-Zr and cladding Fe at 1500 K .

## 5 INITIATION MECHANISM OF EUTECTICS INFERRED FROM FPMD ANALYSES

Metal crystals have a larger number of coordination, that is the number of valence electrons per atom is small so that the distance between ions becomes large, which makes valence electrons be free electrons. As temperature rises, ionic oscillation




---

becomes large disturbing potential configuration, which scatters free electrons, weaken metallic bonds, and giving rise to melting. Furthermore, in the eutectic combination of atoms, band structure energy decreases and correlation function changes. Such change in electronic states could affect metallic bonds.
More specifically speaking in our [U-Pu-Zr, Fe] system, through above described generic phenomenology, Fe-ion moves into $U$ changing bondage between Fe and $U$ to form a local molecular structure capturing neighbor free electrons, which thus decreases the number of electrons involved in metallic bond of $U$ to break the bond and to give eutectic melting.

Lindemann index in high temperature is approximated as

$$
I_{B} \approx \frac{1.6 \Theta_{D}^{2}}{M W^{2} k_{B} T}=\frac{1.6 \Theta_{D}^{2}}{M} \alpha_{k}^{2} \frac{h^{2}}{k_{B} T}
$$

which by Pines [11] reduces to

$$
I_{B}^{m e l t}=\left(\frac{1.6 \Theta_{D}^{2}}{M}\right)^{1 / 2}\left(\frac{\alpha}{a}\right)=2.4\left(\frac{\Theta_{D}^{2 k_{D}^{2}}}{M}\right)^{1 / 2}\left(\frac{h}{k_{B} T_{m e l t}}\right)^{1 / 2}
$$

Thus,

$$
T_{m e l t} \propto \frac{\Theta_{D} / k_{D}}{\sqrt{a / h}}
$$

where $\Theta_{D} / k_{D}=\hbar \omega_{\Theta_{D}}$ is Debye temperature, $k_{D}$ is the wave number at Debye temperature.

Assuming that the sound velocity $s$ and lattice constant $a$ be constant, $k_{D}$ becomes smaller in $\mathrm{U}_{75 \%} \mathrm{Fe}_{25 \%}$ eutectics to vanish fine lattice oscillation and to left course oscillation, which suggests formation of local molecular structure.

## 6 SUMMARY

We investigated the initiation mechanism of eutectics between metal fuel and fuel pin cladding in Core Disruptive Accidents in Sodium-cooled Fast Reactors, using first principle molecular dynamics code VASP.

Comparing U-Fe with U-Zr, in the eutectic combination UFe , the band structure energy decreases and the correlation function changes accompanied by the change of Kohn-Sham energy. Based on this electronic state change, we tried to ascribe the initiation mechanism to the change in metallic bond. We also tried to establish the procedure to reproduce phase diagram for the eutectic combination with phonon model statically combined VASP results, which is successful at least qualitatively. Furthermore, we analyzed solid lines for metal fuel U-Pu-Zr changing atomic composition and obtained appropriate estimate compared with empirical data.

We preliminary analyzed contact configuration of U-Pu-Zr and Fe. Parallel calculations with more CPUs have been performed in FY2008. These analyses aim to provide atomic diffusion coefficient to the atomic diffusion model between mesoscopic particles to be implemented in the COMPASS code.

Our calculations have to treat much larger number of atoms and much longer physical time to take dynamical aspect of eutectics into account, which would be left to classical molecular dynamics [12]. We continue to make every effort to make potentials between specific combination of atoms such as Pu-Fe.

## ACKNOWLEDGMENTS

The present study was carried out within the task "R \& D of the Next Generation Safety Analysis Methods for Fast Reactors with New Computational Science and Technology" entrusted from the Ministry of Education, Culture, Sports, Science and Technology of Japan.

The computation was mainly carried out using the computer facilities at Research Institute for Information Technology, Kyushu University.

## REFERENCES

[1] Koshizuka, S., et al., "R \& D of the Next Generation Safety Analysis Methods for Fast Reactors with New Computational Science and Technology (1) Brief Introduction of the Project and Development of Structural Mechanics Module of the COMPASS Code," ICONE1648499 (2008).
[2] Ito, T. et al., "R \& D of the Next Generation Safety Analysis Methods for Fast Reactors with New Computational Science and Technology (5) Study of Eutectic Reaction Between Metals: Classical Molecular Dynamics Approach," ICONE16-48500 (2008).
[3] Himi, M., et al., "R \& D of the Next Generation Safety Analysis Methods for Fast Reactors with New Computational Science and Technology (7) Study of Eutectic Reaction Between Metals: First Principle Molecular Dynamics Approach ," ICONE16-48482 (2008).
[4] Kresse, G. and Furthmüller, J., "VASP the GUIDE," http://cms.mpi.univie.ac.at/vasp/.
[5] http://www.calphad.org/
[6] Saunders, N. and Miodownik, A.P., "CALPHAD: A Comprehensive Guide," Pergamon Material Series, Vol. 1, Pergamon, Oxford, UK, 1998.
[7] Metals Handbook, 10th ed., edited by ASM.
[8] https://sourceforge.net/project/showfiles.php?group_id= 161614
[9] Pultonium fuel technology, edited by AESJ(Jan.1998)
[10] Lindemann, F., Phys. Z., 11, 609 (1910).
[11]Pines, D., Elementary Excitations in Solids, W.A.Benjamin, inc. (1964).
[12] Ito, T. et al., "Next Generation Safety Analysis Methods for SFRs (7) Potential Model for Classical Molecular Dynamics on Pu-Fe System," ICONE17-75591 (2009).




---

