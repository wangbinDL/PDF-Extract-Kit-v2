# ICONE17-75578  

# Next Generation Safety Analysis Methods for SFRs  (8) Analyses of Eutectics Between Fuel and Steel in Metal Fuel  with FPMD Code VASP  

Masashi Himi, Yuichi Yamamoto  Analysis and Simulation Div., Japan Systems Corporation,   Minami-cho, Kawasaki-ku, Kawasaki, Kanagawa 210-0015, Japan  E-mail:  himi.masashi@jskk.co.jp  

Yasuo Nagamine, Noriyuki Shirakawa, Yasushi Uehara  The Institute of Applied Energy  

Tatsumi Arima  Kyushu University  

# ABSTRACT  

There are two main objectives in this study. One is to  estimate atomic diffusion coefficients in eutectic reaction  between metal fuel and cladding materials in order to establish  the atomic diffusion model for the COMPASS code. The other  is to estimate their material properties such as Young’s modulus  in high temperature up to near melting points in core disruptive  accidents (CDAs) in Sodium-cooled Fast Reactors (SFRs). We  used the first principle molecular dynamics (FPMD) code VASP  to realize the two objectives.  

We tried to understand the initiation mechanism of  eutectics based on change of electronic state energy  accompanied by change of Kohn-Sham energy, including  phonon effect.  

In this project [1], three methods, phase diagram  calculation (CALPHAD), classical molecular dynamics (CMD),  and FPMD, are employed to understand the mechanism of  eutectics and to introduce dynamic characteristics in eutectic  phenomena into the COMPASS code.  

# NOMENCLATURE  

$a$  :  Lattice constant   $D$  :  Diffusion coefficient of ions or atoms   $E^{K S}$  :  Kohn-Sham energy   $E_{X C}$  :  Exchange correlation energy   $E_{g}$   :  Band structure energy   $k_{B}$   :  Boltzmann constant   $N_{i o n}$  :  Number of ions   $n$  :  One-body density of electron   $R$  :  Gas constant  

v  :   ${\bar{R}}_{I}$  Coordinate of nucleus or ion  $I$    v  : 

  $\vec{r}:$  Coordinate of electron 

  $\mathbf{S}\cdot$  :  sound velocity   $t\colon$  :  Time   $\mathrm{T}$  :  Temperature   $u$   :  Displacement of an atom around the node point of  lattice due to thermal fluctuation   $V_{H}$   :  Hartree energy   $x$  :  mixing ratio of metal atoms   $k_{D}$    :  wave number at Debye temperature  

# Greek Symbols  

$\alpha$  :  Index for Lindemann’s criterion of melting   ε :   Energy of state of the Kohn-Sham orbital i 

  $\omega$    Frequency of phonon 

  $\Theta_{\scriptscriptstyle D}$   :  Debye temperature  

# Subscript  

$I,J.$  :    Nucleus or ion number   $i,j$  :    Electron number   $I$  :  Nucleus or ion  

# 1  INTRODUCTION  

Eutectic reaction between metal fuel and steel cladding  and/or steel structures is possibly caused in SFR’s CDA. We  have been studying this phenomenon with three kind of  methods, CALPHAD, CMD, and FPMD since FY2005 [1,2,3].   In this paper, results of the analyses performed with the VASP  code [4] until the end of FY2007, will be presented.  

We have investigated phase transition and eutectics in the  systems containing small number of atoms of solid solution with  multi-kind of atoms and pure metal. We carried out FPMD  analyses of the systems of   $\mathrm{Zr-U}$   and U-Fe each with 16-atom  and tried to extract physical characteristics describing eutectics  from electronic states, where the characteristics are Kohn-Sham  energy, band structure energy, exchange-correlation energy etc.  These analyses suggested that eutectics occur mainly depending  on the intensity of metallic bond that depends on atomic  composition.  

We  have also evaluated  the phase diagram for the crystal  structure of U-Fe 16-atom, by introducing phonons into free  energy formulation to realize finite temperature state from the  crystal structure optimized in 0K. In this investigation, we  showed the process to evaluate the phase diagram of eutectics  quantum-mechanically,  which would  be utilized to judge  eutectics occurrence.  

FPMD has been also applied to the evaluation of metal  fuel material properties. We evaluated melting points based on  the change of Kohn-Sham energy in order to simulate empirical  solidus line of U-Pu-Zr metal fuel. However, evaluated line was  not in good agreement due to small number of atoms and small  number of calculation cases.  

Calculating the system of U-Pu-Zr contacting with Fe until  1ps, we observed melting on the interface judging from  Lindemann’s criterion on melting. Using these results, we  evaluated atomic diffusion coefficient across the interface,  extracting issues with respect to computing time and the derived  limitations. The coefficient could be meaningfully evaluated  even in this small time interval and could be utilized in the  atomic diffusion model for COMPASS code [1].  

# 2  ANALYSES OF ENERGY STATES OF METAL FUEL  AND Fe  

After preparing “optimized state”, which is the crystal state  of mixed metal fuel and Fe atoms that has minimum energy at  near zero pressure and 0K obtained by adjusting lattice  constants, energy states were analyzed by FPMD method with  phonon effect, increasing temperature.  

# 2.1  ANALYSES OF U-Fe AND U-Zr SYSTEMS  

Potential energy of eutectic atomic system such as U-Fe  becomes smaller than the average potential energy of U-U and  Fe-Fe [3]. We related this fact to energy change of electronic  state to systematically understand eutectic initiation.  

We selected and analyzed two mixed 16-atomic systems,  one is U-Zr that had no eutectics and the other is U-Fe that had  eutectics. Phase diagrams of U-Zr and U-Fe are shown in Fig.1  and Fig.2 calculated with the ThermoCalc code based on  CALPHAD  [5,6] , where analyzed cases are shown with three  and five red circles,  respectively.  These eight cases are Zr16,  U8Zr8, U16 in Fig.1 and (U16), U12Fe4, U8Fe8, U4Fe12,  Fe16 in Fig.2. U16 case is the same in U-Zr and U-Fe. Note that  melting points of Zr, U and Fe are 2125K, 1405.5K and 1808K,  respectively [ 7 ].  

  
Fig.1 Phase diagram of U-Zr ( ○ :melting point)  

  
Fig.2 Phase diagram of U-Fe ( ○ :melting point)  

Two-body correlation functions for seven cases are shown  in Fig.3-Fig.9.  Each case clearly leaves crystal correlation  structure at 500K in liquid state at higher temperatures, showing  that crystal state does not change so much that it makes difficult  to discriminate liquid state from solid one by Lindemann’s  criterion on melting.  

  
Fig.6 Calculated two-body correlation functions in U12Fe4.  

  
Fig.9 Calculated two-body correlation functions in Fe16.  

Eigen values of occupied electronic states included in  these seven electronic density of states at  $500\mathrm{K}$   and  $2500\mathrm{K}$   are  shown in Fig.10 and Fig.11, respectively. These eigen values  are averaged over wave number space since they distribute in  the  $\mathbf{k}$  -space direction.  

Electron configurations of  $Z\mathrm{r}$  , Fe and U are   Zr:  $[\mathrm{Kr}]5\mathrm{s}^{2}4\mathrm{d}^{2}$  ,  Fe:   $[\mathrm{Ar}]4\mathrm{s}^{2}3\mathrm{d}^{6}$  , and  U:   $\mathrm{[Rn]}7\mathrm{s}^{2}5\mathrm{f}^{3}6\mathrm{d}^{1}$  , respectively, where 

  $\mathrm{[Ar]=}\mathrm{(1s^{2})(2s^{2}2p^{6})(3s^{2}3p^{6})}$  ,  

  $\bar{[\mathrm{Kr}]}{=}(1\mathrm{s}^{2})(2\mathrm{s}^{2}2\mathrm{\dot{p}}^{6})(3\mathrm{s}^{2}3\mathrm{\dot{p}}^{6})(4\mathrm{s}^{2}3\mathrm{d}^{10}4\mathrm{p}^{6})$  , and  

  $\mathrm{\Delta[Rn]{=}(1s^{2})(2s^{2}2p^{6})(3s^{2}3p^{6})(4s^{2}3d^{10}4p^{6})(5s^{2}4d^{10}5p^{6})\left(6s^{2}4f^{14}5d^{10}6p^{6}\right).}$  

With respect to Uranium, VASP considers 6s and 6p  orbitals as valence states and the number of valence electrons is  14.   The numbers of valence electrons are 4 in   $\mathrm{Zr}$  , and 8 in Fe.  Mixing of U with   $Z\mathrm{r}$   or Fe does not change the number of  electron states inside those of 6s and 6p orbitals, which number  of states are shown in both Fig.10 and Fig.11. For U12Fe4 and  U4Fe12, the numbers of occupied states per 4 atoms are shown  to avoiding fractions. Note that two electrons can seat in one  state because spin states are contracted.  

From these two figures, it is found that the energy at  2500K (liquid) decreases compared with that at 500K (solid) in  U12Fe4 and U4Fe12. On the other hand, energy change in  U8Fe8 is clearly smaller than these two systems.  Furthermore,  energy change in   $\mathrm{Zr-U}$   is not as significant as that in Fe-U is.  That is, we could assume that the energy of electronic states in  U12Fe4 and U4Fe12 that cause eutectics decreases at the  temperature higher enough than melting point.  

Since FPMD calculations of small number of atoms with  finite temperature are often accompanied by large fluctuation,  we continued the calculation until the average energy reaches  near constant. The following consideration is based on the  averaged energy. The energy change without thermal fluctuation  at 0K is shown in Ref.[3].  

  
Fig.10 Eigen values of occupied states in Zr-U-Fe at 500K.  

  
Fig.11 Eigen values of occupied states in  $Z\mathrm{r}$  -U-Fe at 2500K.  

Kohn-Sham energy is described in Eq.(1),  

$$
E^{K S}=\sum_{i}\mathcal{E}_{i}-\frac{1}{2}\int d\vec{r}V_{H}\,(\vec{r}\,)n(\vec{r}\,)+E_{X C}[n]-\int d\vec{r}\,\frac{\delta E_{X C}[n]}{\delta n}\,n(\vec{r}\,)\,,
$$  

where the first term in RHS is the band structure energy   $(E_{\scriptscriptstyle B})$  which is the summation of eigen values of electronic states, the  second is the Hartree energy   $(\,\,V_{\!_{H}}\,)$   ) of  coulomb interaction  multiplied by (-1/2), the third and the forth denote the  exchange-correlation interaction for valence electrons.  

Phase change from solid to liquid generates energy  corresponding to latent heat. Therefore, Kohn-Sham energy as a  function of temperature forms an ogive as shown in Fig.12. We  assume that melting point is an inflection point of the ogive.  

We scaled the Kohn-Sham energy and the temperature, as   $f(E^{K S})\!=\!\frac{E^{K S}(T)\!-\!E^{K S}(500K)}{E^{K S}(2500K)\!-\!E^{K S}(500K)},$ ,   (2) and   $f(T)\,{=}\,\frac{T\,{-}\,500(K)}{2500(K)\,{-}\,500(K)}\,,$  ,      (3)  

respectively. Then, the melting point is the temperature that the  ogive Eq.(2) exceeds Eq.(3), that is when the ogive becomes  convex. Estimated melting temperatures are   ${>}2125\mathrm{K}$   for   $Z\mathrm{r}16$  ,   ${>}1600\mathrm{K}$   for   $\mathrm{U}8Z\mathrm{r}8$  , 1405.5K for U16, 1000K for U12Fe4,  1400-1800K for U8Fe8, 1400K for U4Fe12, and 1808K for  Fe16, respectively, which are good estimates.  

  
Fig.12 Dependence of Kohn-Sham energy on temperature for  U-Fe and U-Zr systems.  

Eq.(4) is the non dimensional i zed band structure energy  $E_{g}$     per one valence electron,   $f(E_{B})\!=\!\frac{E_{B}(500K)\!-\!E_{B}(T)}{E_{B}(2500K)\!-\!E_{B}(500K)},$  ,      (4)  

which is shown in Fig.13. Comparing   $f(E_{\scriptscriptstyle B})$   of each system,   $Z\mathrm{r}8\mathrm{U}8$   does not fall below  $Z\mathrm{r}16$   and U16. Meanwhile   $\mathrm{U}12\mathrm{Fe}4$  and U8Fe8 fall below both U16 and Fe16 at 1400K and 1400-  $1800\mathrm{K}$  , respectively, which shows the electronic state energy in  U-Fe system decreases across the phase change, in contrast that  in  $Z\mathrm{r}{\mathrm{-}}\mathrm{U}$   system does not.  

In the same way Hartree energy  $V_{H}$  (positive) is also  non dimensional i zed as Eq.(5),  

$$
g(V_{_{H}})\!=\!\frac{V_{_{H}}(T)}{\{V_{_{H}}(500K)+V_{_{H}}(500K)\}/2},
$$  

which is shown in Fig.14.   $g(V_{H})$   of each system increases as  temperature rises.  

  
Fig.13 Dependence of band structure energy on temperature   for U-Fe and   $\mathrm{U}{-}Z\mathrm{r}$   systems.  

  
Fig.14 Dependence of Hartree energy on temperature   for U-Fe and U-Zr systems.  

  
Fig.15 Dependence of  exchange-correlation energy   on temperature for U-Fe and U-Zr systems.  

We also  non dimensional i zed  the exchange-correlation  energy   $\left(E_{X C}-V_{X C}\right.$    : negative in   $Z\mathrm{r}16$  ,  $Z\mathrm{r}8\mathrm{U}8$  , U16 and positive  in  $\mathrm{U}12\mathrm{Fe}4$  , U8Fe8, U4Fe12, Fe16)   as Eq.(6),    $g(E_{_{X C}}-V_{_{X C}})\!=\!\frac{(E_{_{X C}}-V_{_{X C}})(T)}{\{(E_{_{X C}}-V_{_{X C}})(500K)\!+\!(E_{_{X C}}-V_{_{X C}})(500K)\}/2},$  which is shown in Fig.15.   $g(E_{X C}-V_{X C})$   of   $Z\mathrm{r}8\mathrm{U}8$   has little  dependence on temperature, meanwhile those of   $\mathrm{U}12\mathrm{Fe}4$  ,  U8Fe8, and U4Fe12 has clear dependence on temperature.  We presume the initiation mechanism of eutectics based on  these analyses that the Kohn-Sham energy increases around  melting point by the latent heat through phase change, the band  structure energy decreases, and the  exchange-correlation energy  changes. Namely, the electronic state energy changes in a  certain composition of atoms,  which affect the metallic bond.  

# 2.2  Phonon effect  

We statically analyzed optimized   energy states for some U- Fe systems of 16-atom using VASP with phonon model [8].  

Since Fe-crystal structure is bcc and U-crystal structure is  orthorhombic at 0K, we calculated optimized state in each  structure, changing composition ratio. Generally speaking,  stability of crystal can be explained by estimating its free  energy. Figure 16 shows two free energy curves for bcc and  orthorhombic for each atomic composition, and tangent line  common to the two curves. As tangent point corresponds to the  equilibrium state in the atomic composition, coexistent domain  between bcc and orthorhombic, that is eutectic domain, can be  estimated. This result roughly reproduces the phase diagram  shown in Fig.2.  

  
Fig.16 Eutectic domain of U-Fe system at 0K.  

The main effect of finite temperature is thermal fluctuation  of crystal structure, which fluctuation can be interpreted as  phonons. Therefore, we calculated the contribution of phonons  to the free energy as well as the entropy of mixing atoms,  stopping the ion motion and simulating lattice oscillation with  phonons.  

Free energy   $G$   of a system is described by Eq.(7),  

#  $\begin{array}{r}{\boldsymbol{G}\bigl(\boldsymbol{T},\boldsymbol{x}\bigr)\!=\!\boldsymbol{E}\bigl(\boldsymbol{x}\bigr)\!-\!\boldsymbol{T}\!\cdot\!\boldsymbol{S}_{m i x}\bigl(\boldsymbol{x}\bigr)\!+\!N_{_A}\,F_{_{p h}}\bigl(\boldsymbol{T}\bigr),}\end{array}$  ,    (7)  

where the first term in RHS is the cohesive energy that is  obtained from optimization analysis at   $0\mathrm{K}$  ,   $S_{m i x}$   is the mixing  entropy,  

$\begin{array}{r}{{\bf\Pi}_{{\bf c}{m i x}}^{{\bf\Pi}{\bf\alpha}{\bf\alpha}{\bf\beta}{\bf r}{\bf J}},}\\ {{\cal S}_{{m i x}}\big(x\big)\!=\!-R\big\{\!x\ln x+\big(1-x\big)\ln(1-x)\big\},}\end{array}$  ,    (8)  and   $F_{p h}$   is the free energy of phonons,  

$$
F_{p h}=\frac{1}{2}\sum_{l}\hbar\omega_{l}+\sum_{l}\frac{\hbar\omega_{l}}{e^{\hbar\omega_{l}/k_{B}T}-1}+k_{B}T\sum_{l}\ln(1-e^{-\hbar\omega_{l}/k_{B}T})\;.
$$  

Here, we used Avogadro number  $N_{A}$   and Boltzmann constant  $k_{B}$  in  [1/mole]  and  [J/K],  respectively,  for  consistent  representation.  

We calculated again similar cases in   $\mathrm{Fig.16}$   under finite  temperature to estimate dependence of coexistence domain on  temperature as shown in Fig.17. The dotted lines in this figure  are shown for comparison based on the data shown in Fig.2.  Calculated coexistence domain tends to narrow as the  temperature rises.  

Although calculated coexistence domain has some shift  from empirical data, our procedure to quantum mechanically  reproduce phase diagram is found to be appropriate and  effective.  

  
Fig.17 Dependence of eutectic domain of U-Fe system   on temperature.  

# 3  SIMULATION of Metal fuel U-Pu-Zr  

From a practical viewpoint of metal fuel,   $\mathrm{U.Pu{-}Z r}$   is  superior to   $\mathrm{U}.\mathrm{Pu}$   because the former has higher melting point  and can coexist with stainless steel cladding due to smaller  eutectic reaction rate. We calculated melting points of   $\mathrm{U.Plu.Zr}$  ,  changing composition as  

$\mathrm{U}76\%\mathrm{Pu}24\%$   (U41, Pu13 atoms),  

  $\mathrm{U}50\%\mathrm{Pu}24\%\mathrm{Zr}26\%$   (U27, Pu13, Zr14 atoms), 

  $\mathrm{U}26\%\mathrm{Pu}24\%\mathrm{Zr}50\%$   (U14, Pu13, Zr27 atoms).  Analytically estimated solidus lines of   $\mathrm{U-Nu-Zr}$   are shown  in Fig.18 [9].  

Preparing uniformly mixed system for each composition,  the system was optimized at each temperature. Two-body  correlation functions are shown in Fig.19-Fig.21.  

Each case clearly leaves crystal structure even after  melting in the same way in section 2.1.  

  

  

The average and standard deviation of both Kohn-Sham  energy and band structure energy in each case was calculated  and shown in   $\mathrm{Fig.}22\mathrm{-Fig.}27$  , where cases of   $\mathrm{U}100\%$   (U16), 

  $\mathrm{U}50\%\mathrm{Zr}50\%$   (U8,Zr8),  $Z\mathrm{r}100\%$     $(Z r16)$   are the same in section 

 2.1. The deviation of band structure energy is much smaller  than that of Kohn-Sham energy.  

Point estimate of melting temperature is not obtained due  to the variation of temperature in FPMD. Deviation of Kohn- Sham energy is large enough to form clear ogive curve so that  the accuracy of flexion point to give melting temperature is not  good.  

The reading of melting temperature in Fig.18 is compared  for each case with calculated results, giving appropriate results,  as follows.  

Solidus line  Calculation 

  $\mathrm{U}76\%\mathrm{Pu}24\%$    :   1200K   1000-1400K 

  $\mathrm{U}50\%\mathrm{Pu}24\%\mathrm{Zr}26\%.$  :  1400K   1200-1600K 

  $\mathrm{U}26\%\mathrm{Pu}24\%\mathrm{Zr}50\%$  :  1600K   1400-1800K 

  $\mathrm{U}100\%$  :     1405K   1200-1800K 

  $\mathrm{U}50\%\mathrm{Zr}50\%$  :    1700K   1400-2100K   $Z\mathrm{r}100\%$  :  2125K   1800-2500K  

Note that broader temperature deviation in   $\mathrm{U}100\%$  ,   $\mathrm{U}50\%\mathrm{Zr}50\%$  , and   $Z r100\%$   is caused by small number of 16  atoms engaged for each case, meanwhile 54 atoms are used in   $\mathrm{U}76\%\mathrm{Pu}24\%$  ,   $\mathrm{U}50\%\mathrm{Pu}24\%\mathrm{Zr}26\%$  , and  $\mathrm{U}26\%\mathrm{Pu}24\%\mathrm{Zr}50\%$  .  

  
Fig.22 Average and standard deviation of Kohn-Sham energy  and band structure energy in  $\mathrm{U}76\%\mathrm{Pu}24\%$  

  
Fig.23 Average and standard deviation of Kohn-Sham energy  and band structure energy in   $\mathrm{U}50\%\mathrm{Pu}24\%\mathrm{Zr}26\%$  

  
Fig.24 Average and standard deviation of Kohn-Sham energy  and band structure energy in   $\mathrm{U}26\%\mathrm{Pu}24\%\mathrm{Zr}50\%$  

  
Fig.25 Average and standard deviation of Kohn-Sham energy  and band structure energy in  $\mathrm{U}100\%$  

  
Fig.26 Average and standard deviation of Kohn-Sham energy  and band structure energy in  $\mathrm{U}50\%\mathrm{Zr}50\%$  

  
Fig.27 Average and standard deviation of Kohn-Sham energy  and band structure energy in   $Z r100\%$  

# 4  CONTACT ANALYSIS BETWEEN METAL FUEL U- Pu-Zr AND CLADDING Fe  

Melting point   $(T_{m})$   of standard metal fuel   $(\mathrm{U}50\mathrm{at}\%$   $\mathrm{Nu}25\mathrm{at}\%$  ,  $Z\mathrm{r}25{\mathrm{at}}\%$  ) is about 1400K as shown in  ${\mathrm{Fig.18}}$   and that  of Fe is about 1808K. We analyzed two cases at 1300K   $({<}T_{m})$  and 1500K   $(>T_{m})$   of system temperature to examine the  difference of electronic states.  

The   $\mathrm{U.Pau.Zr}$   system is composed of U48,   $\mathrm{Nu}24$   and   $Z\mathrm{r}24$  atoms, 96 atoms in all. U,   $\mathrm{Nu}$   and   $Z\mathrm{r}$   atoms are uniformly  contained in the system.  

The Fe system has   $150~\mathrm{Fe}$   atoms in bcc, and this system  was prepared to have optimized lattice constants with adjusted  pressure at both 1300K and 1500K.  

Conforming the size of Fe basic cell   $(5\!\times\!5)$   to   $\mathrm{U.Pu{-}Z r}$  basic cell   $(4{\times}4)$  , Fe system was set upper and U-Pu-Zr system  lower to make combined system with gap of one Fe basic cell  for both 1300K and 1500K cases. Cyclic boundary conditions  are imposed on this structure as a supercell. This calculation  was the largest one we had done until FY2007, so we aimed to  calculate up to 1ps with time step 3fs to investigate how Fe  atoms diffuse into metal fuel through the interface.  

Position of atoms, diffusion coefficient, and the index for  Lindemann's criterion of melting   $[10,11]$   (we call this  Lindemann index, shortly hereafter) at 1300K are shown in  Fig.28-Fig.30, and those at 1500K in Fig.31-Fig.33 in the end  time of calculation, respectively.  

Diffusion coefficients   $\mathrm{D}$   in   $1300\mathrm{K}$   and   $1500\mathrm{K}$   cases are  shown in Fig.29 and Fig.30, respectively, where  $\mathrm{D}$   is defined as  

$D\!=\!\operatorname*{lim}_{t\to\infty}D(t)\!=\!\operatorname*{lim}_{t\to\infty}\!\frac{1}{N_{i o n}}\sum_{i}\!\frac{\left[\vec{R}_{I}\left(t\right)-\vec{R}_{I}\left(0\right)\right]^{2}}{6t}\,.$  .   (10)  

Lindemann index   $\upalpha$   in 1300K and 1500K cases are shown  in Fig.30 and Fig  $^{33}$  , respectively. Equation (11) describes the  relation between  $\upalpha$   and D,  

$$
\alpha(t)\!=\!\left[\!\left\langle{u(t)^{2}}\right\rangle\!\right]^{1/2}\,/\,a\!=\!\frac{\sqrt{D(t)\cdot6t}}{a}\!\,.
$$  

In the beginning of calculation,   $\mathrm{Zr}\mathrm{.}$  -atom near the interface  starts moving because of its small mass. U- and   $\mathrm{Nu}$  -atom begin  to move affected by  $\mathrm{Zr}$  -atom displacement.  

In the 1300K case, Ds of U,  $\mathrm{Nu}$   and  $Z\mathrm{r}$   approaches to the  bulk D. Displacement of Fe-atom is smaller because its melting  temperature is higher than 1300K. D converges on a constant  and diffusion starts when   $\upalpha$   becomes proportional to time. In  this case, as the index does not become proportional to time  until 1ps, melting through the interface is not judged to occur,  which is appropriate because the melting point of metal fuel,  around 1400K, is much higher than 1300K.  

In the 1500K case, calculation is much more time  consuming than the   $1300\mathrm{K}$   case. As shown in Fig.33, time  history of the index is not long enough to judge convergence.  Parallel calculations with more CPUs have been performed in  FY2008.  

Contact analysis between metal fuel and cladding Fe is  supposed to investigate eutectics formation process in pin  failure stage in CDA.  

  
Fig.28 Atomic configuration in the contact calculation between  metal fuel   $\mathrm{U-Nu-Zr}$   and cladding Fe at 1300K (at 630 fs).  

  
Fig.29 Diffusion coefficient in the contact calculation between  metal fuel   $\mathrm{U-Nu-Zr}$   and cladding Fe at 1300K.  

  
Fig.30 Lindemann index in the contact calculation between  metal fuel  $\mathrm{U-Nu-Zr}$   and cladding Fe at 1300K.  

  
Fig.31 Atomic configuration in the contact calculation between  metal fuel   $\mathrm{U}{\mathrm{-}}\mathrm{Nu-}Z\mathrm{r}$   and cladding Fe at 1500K (at 300 fs).  

  
Fig.32 Diffusion coefficient in the contact calculation between  metal fuel  $\mathrm{U}{\mathrm{-}}\mathrm{Nu-}Z\mathrm{r}$   and cladding Fe at 1500K.  

  
Fig.33 Lindemann index in the contact calculation between  metal fuel  $\mathrm{U}{\mathrm{-}}\mathrm{Nu-}Z\mathrm{r}$   and cladding Fe at 1500K.  

# 5 INITIATION MECHANISM OF EUTECTICS INFERRED  FROM FPMD ANALYSES  

Metal crystals have a larger number of  c oordination, that is  the number of valence electrons per atom is small so that the  distance between ions becomes large, which makes valence  electrons be free electrons. As temperature rises, ionic oscillation  becomes large disturbing potential configuration, which scatters  free electrons, weaken metallic bonds, and giving rise to melting.  

Furthermore, in the eutectic combination of atoms, band  structure energy decreases and correlation function changes.  Such change in electronic states could affect  metallic bonds.  

More specifically speaking in our   $\mathrm{[U-Pu-Zr]}$  , Fe] system,  through above described generic phenomenology,   Fe-ion moves  into U changing bondage between Fe and   $\mathrm{U}$   to form a local  molecular structure capturing neighbor free electrons, which  thus decreases the number of electrons involved in metallic  bond of U to break the bond and to give eutectic melting.  

Lindemann   index in high temperature is approximated as  

$$
\alpha(t)^{2}\approx1.6\frac{k_{_B}T}{M_{_I}s^{^2}}\!=\!1.6\frac{\hbar^{2}{k_{_D}}^{2}}{M_{_I}{k_{_B}}^{2}\Theta_{_D}^{^2}}k_{_B}T\ ,
$$  

which by Pines [11] reduces to  

$$
\begin{array}{c}{{\displaystyle k_{_B}\Theta_{_{D}}=\!\left(\frac{1.6}{\alpha_{m e l t}}\right)^{1/2}\!\left(\frac{\hbar^{2}}{M_{_I}}k_{_B}T_{m e l t}{k_{_D}}^{2}\right)^{1/2}}}\\ {{\displaystyle=\!\left(\frac{1.6}{\alpha_{m e l t}}\right)^{1/2}\!\left[\frac{\hbar^{2}}{M_{_I}}k_{_B}T_{m e l t}\!\left(\frac{2.4}{a}\right)^{2}\right]^{1/2}}}\end{array}.
$$  

Thus,  

$$
\Theta_{_D}=\hbar s k_{_D}\,/\,k_{_B}\propto T_{m e l t}^{\quad1/\,2}\,/\,a\,,
$$  

where   $\Theta_{_D}=\hbar s k_{D}\,/\,k_{B}$   is Debye temperature,   $k_{D}$    is the wave  number at Debye temperature.  

Assuming that the sound velocity   $s$   and lattice constant   $a$  be constant,   $k_{D}$   becomes smaller in   $\mathrm{U}75\%\mathrm{Fe}25\%$   eutectics to  vanish fine lattice oscillation and to left course oscillation,  which suggests formation of local molecular structure.  

# 6  SUMMARY  

We investigated the initiation mechanism of eutectics  between metal fuel and fuel pin cladding in Core Disruptive  Accidents in Sodium-cooled Fast Reactors, using first principle  molecular dynamics code VASP.  

Comparing U-Fe with U-Zr, in the eutectic combination U- Fe, the band structure energy decreases and the correlation  function changes accompanied by the change of Kohn-Sham  energy. Based on this electronic state change, we tried to  ascribe the initiation mechanism to the change in metallic bond.  

We also tried to establish the procedure to reproduce phase  diagram for the eutectic combination with phonon model  statically combined VASP results, which is successful at least  qualitatively. Furthermore, we analyzed solid lines for metal  fuel   $\mathrm{U.Pu{-}Z r}$   changing atomic composition and obtained  appropriate estimate compared with empirical data.  

Our calculations have to treat much larger number of  atoms and much longer physical time to take dynamical aspect  of eutectics into account, which would be left to classical  molecular dynamics [12]. We continue to make every effort to  make potentials between specific combination of atoms such as  Pu-Fe.  

# ACKNOWLEDGMENTS  

The present study was carried out within the task "R & D  of the Next Generation Safety Analysis Methods for Fast  Reactors with New Computational Science and Technology"  entrusted from the Ministry of Education, Culture, Sports,  Science and Technology of Japan.  

The computation was mainly carried out using the  computer facilities at Research Institute for Information  Technology, Kyushu University.  

# REFERENCES  

[1] Koshizuka, S., et al., "R & D of the Next Generation Safety  Analysis  Methods  for  Fast  Reactors  with  New  Computational  Science  and  Technology  (1)  Brief  Introduction of the Project and Development of Structural  Mechanics Module of the COMPASS Code," ICONE16- 48499 ( 2008 ). 

 [2] Ito, T. et al., "R & D of the Next Generation Safety Analysis  Methods for Fast Reactors with New Computational Science  and Technology (5) Study of Eutectic Reaction Between  Metals:  Classical  Molecular  Dynamics  Approach,"  ICONE16-48500 ( 2008 ). 

 [3] Himi, M., et al., "R & D of the Next Generation Safety  Analysis  Methods  for  Fast  Reactors  with  New  Computational Science and Technology (7) Study of  Eutectic  Reaction  Between  Metals:  First  Principle  Molecular Dynamics Approach ," ICONE16-48482 ( 2008 ). 

 [4] Kresse, G. and Furthmüller, J., "VASP the GUIDE,"  http://cms.mpi.univie.ac.at/vasp/. 

 [5] http://www.calphad.org/ 

 [6] Saunders, N. and Miodownik, A.P., "CALPHAD: A  Comprehensive Guide," Pergamon Material Series, Vol. 1,  Pergamon, Oxford, UK, 1998. 

 [7] Metals Handbook, 10th ed., edited by ASM. 

 [8] https://sourceforge.net/project/showfiles.php?group_id=  161614 

 [9] Pultonium fuel technology, edited by AESJ(Jan.1998) 

 [10] Lindemann, F., Phys. Z., 11, 609 (1910). 

 [11]  Pines,  D.,  Elementary  Excitations  in  Solids,  W.A.Benjamin, inc. (1964). 

 [12] Ito, T. et al., "Next Generation Safety Analysis Methods for  SFRs (7) Potential Model for Classical Molecular Dynamics  on Pu-Fe System," ICONE17-75591 ( 2009 ).  We preliminary analyzed contact configuration of U-Pu-Zr  and Fe. Parallel calculations with more CPUs have been  performed in FY2008. These analyses aim to provide atomic  diffusion coefficient to the atomic diffusion model between  mesoscopic particles to be implemented in the COMPASS code.  