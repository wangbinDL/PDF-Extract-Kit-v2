# A 5.2 mW IEEE 802.15.6 HBC Standard Compatible Transceiver With Power Efficient Delay-Locked-Loop Based BPSK Demodulator 

Hyunwoo Cho, Student Member, IEEE, Hyungwoo Lee, Student Member, IEEE, Joonsung Bae, Member, IEEE,<br>and Hoi-Jun Yoo, Fellow, IEEE


#### Abstract

A Low-power IEEE 802.15.6 human body communication (HBC) fully compatible transceiver is implemented in 130 nm CMOS process. In this work, the proposed HBC transceiver satisfying all the standard requirements has four key features for low power consumption which includes: 1) low-power analog active filters for TX spectral mask: $30 \%$ power reduction; 2) delayed locked loop (DLL) based BPSK receiver with the S/H operation for turning off unnecessary blocks: 40\% power reduction; 3) low-power mode (LP-mode) receiver with the received signal strength indicator (RSSI) output data: $50 \%$ power reduction; and 4) reconfigurable LNA with RSSI output data: $60 \%$ power reduction. As a result, the proposed transceiver can fully satisfy the HBC standard requirements while consuming 5.2 mW from the 1.2 V supply.


Index Terms-Costas loop, delayed-locked loop (DLL), human body communication (HBC), IEEE 802.15.6, received signal strength indicator (RSSI), spectral mask, standard, wireless body area network (WBAN).

## I. INTRODUCTION

$\mathbf{R}$ECENTLY, wireless body area network (WBAN) is getting more and more attention in the emerging applications which combines healthcare and consumer electronics around the human body. The major design challenge associated with the WBAN is to extend the lifetime of the WBAN devices under limited energy source. Human body communication (HBC) which uses the human body as a communication channel is considered as a power-efficient wireless communication solution of the WBAN because high conductivity of the human body in a low frequency band enables low power communication. Since the HBC was firstly presented in [1], the physical communication principle and a variety of power efficient HBC transceivers have been presented [2]-[14], and eventually in 2012 the WBAN is standardized as IEEE 802.15.6 [15]. However, fully satisfying all requirements of HBC standard (Fig. 1) while consuming low power for long battery life is very difficult because of 1) transmitter (TX) mask with low

[^0]spectrum floor, sharp slope and wide frequency bandwidth, 2) low sensitivity, and 3) received energy detection capability for PHY/MAC protocol.
The previous HBC transceiver was proposed in 2013 [9], but it was not optimized for low power consumption. In the TX, the power-consuming high-order digital filter which consists of high speed DAC with high speed clock generation ( 840 MHz ) to avoid aliasing effect was adopted to satisfy the mask requirements. In the RX, the power-hungry VCO-based BPSK demodulator with I (in phase) and Q (quadrature phase) dual data paths for coherent receiving was employed in RX, which requires significant power consumption. In addition, the energy detector was not implemented which is an essential block for PHY/MAC protocol.
In this paper, we propose a low power and fully IEEE 802. 15.6 HBC compatible transceiver satisfying all the tight specifications by adopting 4 key techniques. First, in the TX, an analog active filter rather than the high speed DAC reduces the power consumption by $30 \%$ because bandwidth requirement of analog active filter is much lower than the DAC in [9]. Second, the delay-locked-loop (DLL) based BPSK demodulator mitigates $40 \%$ of power consumption by turning off synchronization circuits in Q-path data path with the help of sample and hold (S/H) circuit which retains the control voltage of the DLL. Third, the received signal strength indicator (RSSI), which measures the received signal power to obtain the energy detection capability for the energy-efficient PHY/MAC operation, enables the operation of the low-power mode (LP-mode) receiver composed of amplifiers used in RSSI and digital demodulator while turning off all blocks of the DLL-based BPSK receiver with $50 \%$ power reduction. At last, by utilizing the information of the input signal power, the noise and linearity performance of the LNA can be adaptively controlled with the $60 \%$ reduced bias current consumption.
The rest of this paper is organized as follows. In the Section II, the overall architecture of the proposed HBC transceiver will be introduced. In the Section III and IV, the detail design of the transmitter with the analog active filter and DLL-based BPSK receiver will be explained, respectively. In Section V, the low power schemes including LP-mode receiver and reconfigurable LNA will be presented with the RSSI design. After illustrating the measurement results in Section VI, the conclusion will be summarized in Section VII.


[^0]:    Manuscript received February 18, 2015; revised May 05, 2015, July 06, 2015, and August 16, 2015; accepted August 17, 2015. This paper was approved by Guest Editor Gregory Chen.
    The authors are with the Korea Advanced Institute of Science and Technology (KAIST), Daejeon 305-701, Korea (e-mail: hwcho@kaist.ac.kr).

    Color versions of one or more of the figures in this paper are available online at http://ieeexplore.ieee.org.

    Digital Object Identifier 10.1109/JSSC.2015.2475179




---



Fig. 1. IEEE 802.15.6 HBC standard requirements.



Fig. 2. Overall architecture of the proposed HBC transceiver.

## II. OVERALL ARCHITECTURE

Fig. 2 shows the overall transceiver architecture which is composed of a transmitter with a spectral mask filter, a direct conversion receiver with a BPSK synchronizer, a RSSI and a digital baseband (PHY and MAC). In the transmitter, the baseband data from the PHY/MAC is modulated with 21 MHz carrier frequency. The modulation is the frequency selective digital transmission (FSDT) which is the same with the rectangular wave modulated BPSK. The spectral mask filter suppresses the low frequency band and high frequency band of the modulated data, and the driver transmits the data through the human body. In the receiver, the direct conversion receiver with the BPSK synchronizer recovers the received data from the LNA. The differential input LNA is adopted to generate differential output without noise figure growth which is essential for the direct conversion receiver configuration. Since the TX is disconnected when the receiver is operated, it does not generate LNA input mismatch. I and Q data paths of the direct conversion receiver consists of active mixers, baseband amplifiers, baseband lowpass filters, and limiting amplifiers. The DLL-based BPSK synchronizer adjusts its local RX clock signal to the rising and falling edge of the input data. Especially compared with the VCO-based architecture [15], [16], the DLL-based architecture can promptly synchronize its clock with the input data without any stability problem. Moreover, the proposed synchronizer in


Fig. 3. Previous HBC transmitter architecture. (b) Proposed HBC transmitter architecture.
Q data path including mixer, baseband amplifier, low pass filter and limiting amplifier is disabled to significantly decrease its power consumption when the phase synchronization loop is stabilized. The RSSI is composed of a seven stage limiting amplifier with seven rectifiers and 8-bit single-slope ADC. The RSSI measures the received input power with a range of -100 dBm to -10 dBm . Based on the output of the RSSI, the operation mode of the LNA is controlled to optimize its consuming power while satisfying the sensitivity requirements, resulting in $60 \%$ power




---



Fig. 4. Spectrum simulation results. (a) Original data (b) Active filter (c) Non-linear modeling (c) off chip filtering.



Fig. 5. The 3rd-order low pass filter and high pass filter architecture.
reduction. In addition, to further reduce the power consumption when the input power is larger than -35 dBm , the direct conversion receiver circuits are turned off, and only the LP-mode receiver with the limiting amplifier and digital demodulator for BPSK is turned on to recover the data. In the LP-mode receiver, over $50 \%$ of power consumption can be reduced.

## III. TRANSMITTER DESIGN

Fig. 3(a) shows the previous transmitter architecture [9] including the digital FSDT modulator, 8th-order digital band-pass filter, 8 bit DAC and driver. The DAC based mask filter is commonly utilized in many RF transceivers because the digital filter enables the convenient simulation environment, and it is insensitive to the PVT variation. However, the DAC is not suitable for the HBC mask filter because the end frequency of the mask is very high. Since the high frequency edge of the mask requirement is 400 MHz , the digital filter and DAC should be operate at least 800 MHz , and a high-Q analog low-pass filter is also required to remove the harmonic frequency and alias terms, which leads to the significant power consumption.

Fig. 3(b) shows the proposed transmitter architecture [13] with the low-power consuming analog active filters. Compared with the high speed DAC and digital filter, the analog active filter consumes much lower power because the OTA bandwidth requirement in the analog filter is much lower than the DAC. Since the spectral mask is falling at the 23.625 MHz and the end frequency is 400 MHz , the 3 dB frequency and gain bandwidth should be large than 23.625 MHz and 400 MHz , respectively. In this work, we designed the OTA 3 dB bandwidth as 100 MHz which is larger than the 23.625 MHz . Compared with the DAC which requires at least 800 MHz sampling frequency, the analog filter requires only 100 MHz bandwidth, and this bandwidth reduction leads to $30 \%$ power reduction in the transmitter design. Although the proposed analog active filters require off-chip digitally controlled tuning to compensate the frequency characteristics variation caused by the process variation, it takes small




---



Fig. 6. Principle of the proposed DLL-based BPSK receiver.



Fig. 7. The overall architecture of the proposed DLL-based BPSK receiver.



Fig. 8. Schematic of the reconfigurable LNA, and the noise figure and linearity graph.
cost because the tuning is required only at the first time and the process variation can be avoided by using post layout simulation and common centroid layout technique. The proposed transmitter is composed of the level shifter, analog active filters, driver and off-chip analog filters. The signal flow in each stage in the transmitter will be explained in Fig. 4. Since the data is modulated with the rectangular wave swinging from 0 V to 1.2 V , there are excessive DC power and harmonics in high frequency. Second, the data after the level shifter which reduces the swing range in order to avoid the non-linear effect in the following analog circuits is attenuated by 6th-order low-pass filter and 9th-order high-pass filter (Fig. 4(b)). The excessive spectrum power in DC and high frequency band is suppressed under the mask, but the non-linear characteristics of the analog active filter and driver increases the sideband spectrum, which is called spectrum regrowth effect (Fig. 4(c)). The amount of




---



Fig. 9. Active mixer and its replica bias circuit.



Fig. 10. Delay circuit with the linear bias control circuit.
this increased low frequency spectrum power cannot be exactly predicted due to the PVT variation, so we adopt the simple R-C off-chip 2nd-order high-pass filter to additionally attenuate the low frequency power. After the off-chip 2nd-order high-pass filter, all the excessive spectrum power is removed, and finally, the output spectrum can satisfy the spectral mask requirement (Fig. 4(d)).

Fig. 5 shows the circuit of the 3rd-order active low-pass filter and high pass filter. The active filter adopts the multiple feedback architecture which can obtain the $60 \mathrm{~dB} /$ decade slope with only one OTA. The OTA has folded cascade configuration with the frequency compensation technique [14].

## IV. RECEIVER DESIGN

## A. DLL-Based BPSK Receiver

Fig. 6 shows the analysis of the DLL-based BPSK receiver. In the BPSK receiver, the local clock synchronization path, which is called Costas loop, is essential. The receiver should have I path and Q path to calculate the phase difference between the input data and local clock by multiplying output of both paths. Since the multiplied output of I and Q path is proportional to $\sin (2 \phi)$, the phase difference can be zero by composing the synchronization loop to make the $\sin (2 \phi)$ zero. In the conventional works [16], [17], the Costas loop uses the VCO to calibrate the input signal and local clock, which is quite similar with the PLL. Such implementations, however, may have stability



Fig. 11. Measured delay time with respect to the delay control voltage.
concerns. In this work, we proposed a DLL-based Costas loop, which avoid the stability issues associated with 2nd (or higher order) phase-locked loops. Since the frequency of local clock is not changed with respect to the control voltage, the delay cell control voltage can be held with the help of sample and hold buffer while turning off the Q path blocks, reducing $40 \%$ of power consumption. The phase error due to the S/H buffer offset ( $\leq 2$ degrees) is negligible. In addition, the clock difference between the TX and RX can be calibrated in the packet domain. In the HBC standard packet, the pilot which is composed of




---



Fig. 16. Reconfigurable LNA operation.



Fig. 17. TX spectrum measurement results.



Fig. 18. Eye diagram of the main and LP-mode receiver.
simple $0,1,0,1$ for clock calibration must be inserted if the payload length is longer than 64 bytes. Since the clock drift of the crystal oscillator is usually under 10 ppm and it must be smaller than 100 ppm in HBC standard, the clock offset can be periodically calibrated at the pilot time without BER degradation.

Fig. 7 shows the detailed block diagram of the proposed DLL-based BPSK receiver. I path and Q path are composed of mixer buffer, mixer, baseband filter, and limiting amplifier. The voltage to current converter and a capacitor make the 1st-order loop filter, and S/H buffer with a switch is employed for holding the control voltage while turning off the Q path blocks. The delayed 21 MHz reference clock signal through the delay cell in Costas loop works as a local clock of the RX.



Fig. 19. TX output power measurement results.




---



Fig. 20. (a) FM-radio input power measurement results (b) Measurement results of the relationship between 100 MHz FM blocker input power and receiver sensitivity.

## B. Circuit Design

Fig. 8 shows the schematic of the reconfigurable LNA [8]. The common gate LNA with the $\sqrt{2}$-boosting cross coupled NMOS is adopted for low noise characteristics. The size of the input NMOS $\mathrm{M}_{1}$ and $\mathrm{M}_{2}$ are controlled by 6 bit control code $\mathrm{C}_{\mathrm{LNA}}$ to adaptively change the LNA performance for low-power consumption which will be explained in Section V, and the noise figure and the 1 dB compression point value in accordance with the control code is shown in Fig. 8.

Fig. 9 shows the schematic of the active mixer and replica bias circuit. The active mixer has a simple Gilbert mixer configuration, and resistor $\mathrm{R}_{\mathrm{P}}$ is added to reducing the switching noise and increasing the linearity of mixer. The resistor $\mathrm{R}_{\mathrm{P}}$ and $\mathrm{R}_{\mathrm{D}}$ are composing the replica bias circuit. It has a same configuration of the half circuit of the Gilbert mixer, but resistor value is four times larger and size of transistor is four times smaller than the original ones, reducing the current consumption of the replica bias circuit by $25 \%$.

Fig. 10 presents the delay cell and delay control bias circuit. The delay cell is composed of six stages inverter based unit delay cells whose bias current is supplied by the delay control bias circuit. In the bias circuit, the output current is linearly changed by the input control voltage $\mathrm{V}_{\mathrm{CTL}}$. The two differential MOS pairs $\mathrm{M}_{7}, \mathrm{M}_{8}$ remove the 2 nd-order harmonics to increase the linearity while consuming more power consumption. Fig. 11 shows the measurement results of the delay time of the delay cell in accordance with the control voltage $\mathrm{V}_{\mathrm{CTL}}$ and bias current.

## V. RSSI AND LOW-POWER RECEIVER

## A. RSSI Design

In the PHY/MAC protocol for multi-nodes operation, the energy detection block is an essential. Fig. 12 shows the principle and architecture of the RSSI for energy detection [18]-[20]. The RSSI is composed of seven amplifiers, seven rectifiers, current adder with low-pass filter and ADC. Since the number of the amplifiers decides the dynamic range of the RSSI and we need -10 dBm to +100 dBm input dynamic range to sense the HBC input signal power, seven amplifiers with the voltage gain of 15 dB and seven rectifiers are adopted. Each amplifier and rectifier



Fig. 21. RSSI measurement results.
covers the different input power range, and we can achieve wide dynamic range by adding all rectifiers' results.

Fig. 13 shows the schematic of the rectifier and current adder. The output current of each of the rectifier with the size ratio of $\mathrm{k} \simeq \mathrm{W}_{\mathrm{M} 3} / \mathrm{W}_{\mathrm{M} 1}$ can be expressed as

$$
\mathrm{I}_{\mathrm{OUT}}=\frac{\mathrm{I}_{\mathrm{IN}}}{2}\left[1+\frac{\mathrm{V}_{\mathrm{OUT}}}{\mathrm{V}_{\mathrm{T}}\left(1+1 / \mathrm{k}\right)}\right]
$$

Since the output current is proportional to the input voltage, we can know that the rectifier converts the voltage value to the power value. The output current of each rectifiers are added by simple current mirror, and R-C load is adopted to sense the DC value while attenuating the voltage ripple with the frequency of the input carrier signal.

## B. LP-Mode Receiver

The FM-radio band from 80 MHz to 110 MHz becomes the strong interference to the HBC transceiver due to the body antenna effect. The direct conversion BPSK receiver consumes large amount of power to achieve good selectivity, but RSSI and the proposed LP-mode receiver can relax the selectivity overhead. Fig. 14 shows the concept and the architecture of the




---



Fig. 22. Chip photograph and performance summary.
LP-mode receiver. When the input power we can know from the RSSI is over -35 dBm which is 10 dB larger than maximum FM-radio input power, the LP-mode receiver which reuses the amplifiers in RSSI and digital demodulator can replace the direct conversion receiver. Since the power consumption of the direct conversion receiver becomes zero and the power consumption of the reused amplifiers are very low because of low required bandwidth $(21 \mathrm{MHz})$, the LP-mode receiver can reduce the $60 \%$ of power consumption.

Fig. 15 shows the signal recovery flow and demodulator circuit. Data from the human body is recovered to the digital data by amplifier chain. In the demodulator, the input data is firstly sampled by 42 MHz clock. A Logic with several gates which is shown in Fig. 16 helps to find the data non-inverting time to demodulate the BPSK data. The phase ambiguity can be solved in the PHY processor by comparing the input data with the promising data sequence of preamble stage in data packet.

## C. Reconfigurable LNA With RSSI

Fig. 16 shows the operation of the reconfigurable LNA. If the voltage gain of the LNA is fixed, LNA should have both good sensitivity and good linearity to cover the both weak input and strong input, resulting in large power consumption in LNA. On the other hand, since we can know the input signal power by using the RSSI, the LNA can adaptively control the sensitivity and linearity performance with much lower power consumption. For instance, if the input signal is strong, the LNA is controlled to locate in (1) with the good linearity, and if the input signal is weak, the LNA is adjusted to locate in (3) with the good noise performance, which leads to reducing the power consumption by $60 \%$.

## VI. MEASUREMENT RESULTS

Fig. 17 shows the TX spectrum measurement results. The spectrum with various data rate is measured and white line shows the required mask. All the measurement results satisfy the mask requirements. The spectrum of low frequency band and high frequency band cannot be shown in one screen due to the noise floor of the spectrum analyzer.
Fig. 18 shows the measured eye diagram of the direct conversion receiver and LP-mode receiver. The eye diagram of the direct conversion receiver is measured with the -70 dBm input power at 1.3125 Mbps data rate. The eye diagram, of the LP-mode receiver is measured with -30 dBm input power at 1.3125 Mbps .

Fig. 19 shows the measurement results of the transmitter output power. The output power is controlled by changing the MOS size of the transmitter driver. The maximum output power is around -10 dBm , and measured EVM of the BPSK modulated data from the TX driver is $6.4 \%$. The error is mainly caused by analog filters.
Fig. 20(a) shows the blocker measurement results. Since the human body height is similar to the half of the FM-radio wavelength, the FM-radio signal can be easily coupled to the human body. The maximum input power of the FM-radio interference, or FM-blocker, is -38 dBm . Fig. 20(b) shows the relationship between input FM-blocker power and receiver sensitivity. If the FM-blocker power is larger than -35 dBm , the BER becomes larger than $10 \%$. The sensitivity becomes lower when the input FM-blocker becomes lower.
Fig. 21 shows the RSSI measurement results. The X axis is the input signal power, left Y axis is output RSSI output voltage and right Y axis is the error between input signal power and calculated input power from the RSSI output voltage. The measured input dynamic range is from -10 dBm to -100 dBm and the measured error is under 2 dBm in -20 dBm to -80 dBm input range.

Fig. 22 shows the chip photograph and performance summary table. The proposed HBC transceiver is implemented in SMIC 130 nm process and it satisfies all the standard requirements including sensitivity, data-rate, modulation, spectral mask and




---

TABLE I
PERFORMANCE COMPARISON TABLE

|  | [4] | [5] | [6] | [7] | [8] | [9] | [10] | [13] | Proposed |  |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Process Technology | $0.13 \mu \mathrm{m}$ | $0.13 \mu \mathrm{m}$ | $0.13 \mu \mathrm{m} / \mathrm{SiGe}$ | $0.13 \mu \mathrm{m}$ | $0.13 \mu \mathrm{m}$ | $0.13 \mu \mathrm{m}$ | $0.13 \mu \mathrm{m}$ | $65 \mathrm{~nm}$ | $130 \mathrm{~nm}$ |  |
| Standard <br> Compatibility <br> (IEEE802.15.6) | $\checkmark$ | $\times$ | $\times$ | $\times$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\times$ | $\checkmark$ |  |
| Energy <br> Detection <br> Capability | $\times$ | $\times$ | $\times$ | $\times$ | $\times$ | $\checkmark$ | $\times$ | $\times$ | $\checkmark$ |  |
| Inductor <br> (On-die MIM <br> & Off-chip) | $\times$ | $\times$ | $\checkmark$ | $\times$ | $\times$ | $\times$ | $\times$ | $\times$ | $\times$ |  |
| RX Curr. <br> Consum. <br> (Active/Sleep) | $7.2 / 0.1 \mathrm{~mA}$ | $\left(11.25 / 0.65) \mathrm{mA}\right.$ | $5.8(0.6) \mathrm{mA}$ | 2.7 mA | $3.7 / 0.2 \mathrm{~mA}$ | $5.5(0.2) \mathrm{mA}$ | $7.2 / 0.9 \mathrm{~mA}$ | $3.6(0.7) \mathrm{mA}$ | $2.1(0.2) \mathrm{mA}$ |  |
| TX Curr. <br> Consum. <br> (Active/Sleep) | $5.3 / 0.1 \mathrm{~mA}$ | $0.29-7.5$ mA <br> $(0.29)$ mA | $2.2(12.8) \mathrm{mA}$ | - | $9.4 / 0.1 \mathrm{~mA}$ | $4.5(34.5) \mathrm{mA}$ | $7.7 / 0.2 \mathrm{~mA}$ | $9.6(10.6) \mathrm{mA}$ | $5.6(0.1) \mathrm{mA}$ |  |
| Total Curr. <br> Consum. <br> (Active/Leakage) | $12.5-15.2$ <br> $(4.4) \mathrm{mA}$ | $12.5-18.75$ <br> $(1.34) \mathrm{mA}$ | 8 | 2.7 mA | 13.1 <br> $(1.1) \mathrm{mA}$ | $10 \& 39$ <br> $(0.7) \mathrm{mA}$ | $14.9-22.6$ <br> $(8.2)$ | 13 <br> $(4.1) \mathrm{mA}$ | $5.2(0.4) \mathrm{mA}$ | $2.1(0.2) \mathrm{mA}$ |
| RX O/P <br> Sensitivity | -80 dBm | -70 dBm | -70 dBm | -47 dBm | -90 dBm | -100 dBm | -89 dBm | -13 dBm | -100 dBm |  |
| TX Output Amplitude <br> (Low/Medium/High) | $\times$ | $\times$ | $\checkmark$ | $\times$ | $\times$ | $\times$ | $\times$ | $\times$ |  | $\checkmark$ |
| LP-mode <br> Capability | $\times$ | $\times$ | $\times$ | $\times$ | $\times$ | $\times$ | $\times$ | $\times$ | $\checkmark$ |  |

energy detection capability. The transmitter power consumption is 1.3 mW and the power consumption of the direct conversion receiver at sample time and at hold time is 6.2 mW and 3.8 mW , respectively. The RSSI successfully measure the input signal power with the -100 dBm to -10 dBm input dynamic range. The LP-mode receiver and reconfigurable-LNA utilize the RSSI output to reduce the power consumption, resulting in $50 \%$ and $60 \%$ power reduction, respectively.

Table I shows the comparison table with previous HBC transceivers, The proposed transceiver in this work fully satisfies the HBC standard and lower power consumption, simultaneously, compared with the previous works.

## VII. CONCLUSION

In this paper, the IEEE 802.15.6 fully compatible HBC transceiver is proposed with four low-power features. First, compared with the high speed DAC architecture, analog active filter based TX mask filter is adopted with $30 \%$ power reduction. Second, the DLL-based BPSK receiver saves the $40 \%$ power consumption by turning off the Q data path with the S/H operation. Third, the LP-mode receiver with the measured input power by RSSI reduces the $50 \%$ power consumption. At last, the reconfigurable LNA with the RSSI output information is adopted with $60 \%$ power reduction. As a result, the proposed standard compatible receiver implemented in 130 nm CMOS technology consumes as low as 5.2 mW power while satisfying all the standard requirements.

## REFERENCES

[1] T. Zimmerman, "Personal area network: Near-field intra-body communication," IBM Syst. J., vol. 35, no. 3-4, pp. 609-617, 1996.
[2] N. Cho et al., "The human body characteristics as a signal transmission medium for intra-body communication," IEEE Trans. Microw. Theory Techn., vol. 55, no. 5, pp. 1080-1086, May 2007.
[3] J. Bae et al., "The signal transmission mechanism on the surface of human body for body channel communication," IEEE Trans. Microw. Theory Techn., vol. 60, no. 3, pp. 582-593, Mar. 2012.
[4] S. Song et al., "A 0.9 V 2.6 mW Body-coupled scalable PHY transceiver for body sensor applications," in IEEE ISSCC Dig. Tech. Papers, 2007, pp. 366-367.
[5] N. Cho et al., "A $60 \mathrm{~kb} / \mathrm{s}$-to- $10 \mathrm{Mb} / \mathrm{s} 0.37 \mathrm{~nJ} / \mathrm{b}$ adaptive-frequency-hopping transceiver for interference resilient body channel communication," IEEE J. Solid-State Circuits, vol. 44, no. 3, pp. 708-717, Mar. 2009.
[6] N. Cho et al., "A 10.8 mW body channel communication/MICS dualband transceiver for a unified body sensor network controller," IEEE J. Solid-State Circuits, vol. 44, no. 12, pp. 3459-3468, Dec. 2009.
[7] A. Fazzi et al., "A 2.75 mW wideband correlation-based transceiver for body-coupled communication," in IEEE ISSCC Dig. Tech. Papers, 2009, pp. 204-205.
[8] J. Bae et al., "A $0.24-\mathrm{nJ} / \mathrm{b}$ wireless body-area-network transceiver with scalable double-FSK modulation," IEEE J. Solid-State Circuits, vol. 47, no. 1, pp. 310-322, Jan. 2012.
[9] H. Lee et al., "A 5.5 mW IEEE 802.15.6 wireless body area network standard transceiver for multi-channel electro-acupuncture application," in IEEE ISSCC Dig. Tech. Papers, 2013, pp. 452-45


---



Hyunwoo Cho (S'10) received the B.S. degree from the Department of Physics, Korea Advanced Institute of Science and Technology (KAIST), Daejeon, Korea, in 2010, and the M.S. degree from the Department of Electrical Engineering, KAIST, in 2012, where he is currently working toward the Ph.D. degree.
He has worked on developing power and energyefficient CMOS wireless transceivers for portable and wearable devices working around the human body. His current research interest is low-power and low-energy body-area-network transceiver design and body-channel characteristics analysis.



Hyungwoo Lee (M'15) received the B.S., M.S., and Ph.D. degrees in electrical engineering from the Korea Advanced Institute of Science and Technology (KAIST), Daejeon, Korea, in 2010, 2012, and 2015, respectively. His Ph.D. research concerned wireless body area network circuits and systems and is focused on the network optimization among multiple sensor nodes using the human body communication PHY\&MAC.
Since 2015, he has been with Samsung Advanced Institute of Technology (SAIT), Samsung Electronics. He is currently a research staff member and his research interest is in low-energy system design for mobile healthcare applications.



Joonsung Bae (S'07) graduated from the Electrical Engineering Department of Korea Advanced Institute of Science and Technology (KAIST), Daejeon, Korea, in 2007 and received the M.S. and Ph.D. degrees in electrical engineering from KAIST in 2009 and 2013, respectively. His Ph.D. work concerned the Wireless Body Area Network (WBAN) circuits and systems.
In 2012, he was a visiting scholar of IMEC, Belgium, and researched noise analysis of the dry electrode for body channel communication. Since 2013, he has been with the Memory Business of Samsung Electronics, Korea, where he developed the SoC Design for the SSD (Solid-State Drive) and UFS (Universal Flash Storage). As a senior engineer, he designed the integrated circuits for PCI-Express 3.0 and M-PHY 3.0. In 2014, he joined the Information and Electronics Research Institute in KAIST as a postdoctoral researcher. Now he is an analog circuit designer in IMEC, Belgium, where he investigates ultra-lowpower biomedical circuits. His current research interests are high-speed serial interface PHY, short-range wireless connections, WBAN circuits and systems, and biomedical circuits and systems.
Dr. Bae received the Asian Solid-State Circuits Conference (A-SSCC) Best Design Awards in 2011 and the Global Internship Scholarship of National Research Foundation of Korea in 2012.



Hoi-Jun Yoo (M'95-SM'04-F'08) graduated from the Electronic Department of Seoul National University, Seoul, Korea, in 1983 and received the M.S. and Ph.D. degrees in electrical engineering from the Korea Advanced Institute of Science and Technology (KAIST), Daejeon, Korea, in 1985 and 1988, respectively.
Since 1998, he has been on the faculty of the Department of Electrical Engineering at KAIST and now is a full Professor. From 2001 to 2005, he was the Director of Korean System Integration and IP Authoring Research Center (SIPAC). From 2003 to 2005, he was the full time Advisor to Minister of Korea Ministry of Information and Communication and National Project Manager for SoC and Computer. In 2007, he founded System Design Innovation \& Application Research Center (SDIA) at KAIST. Since 2010, he has served on the general chair of Korean Institute of Next Generation Computing. His current interests are computer vision SoC , body area networks, biomedical devices and circuits. He is a co-author of DRAM Design (Korea: Hongleung, 1996), High Performance DRAM (Korea: Sigma, 1999), Networks on Chips (Morgan Kaufmann, 2006), Low-Power NoC for High-Performance SoC Design (CRC Press, 2008), Circuits at the Nanoscale (CRC Press, 2009), Embedded Memories for Nano-Scale VLSIs (Springer, 2009), Mobile 3D Graphics SoC from Algorithm to Chip (Wiley, 2010), and Bio-Medical CMOS ICs (Springer, 2011).
Dr. Yoo received the Electronic Industrial Association of Korea Award for his contribution to DRAM technology in 1994, Hynix Development Award in 1995, the Korea Semiconductor Industry Association Award in 2002, Best Research of KAIST Award in 2007, Scientist/Engineer of this month Award from Ministry of Education, Science and Technology of Korea in 2010, Best Scholarship Awards of KAIST in 2011, and Order of Service Merit from Ministry of Public Administration and Security of Korea in 2011 and has been co-recipients of ASP-DAC Design Award 2001, Outstanding Design Awards of 2005, 2006, 2007, 2010, 2011 A-SSCC, Student Design Contest Award of 2007, 2008, 2010, 2011 DAC/ISSCC. He has served as a member of the executive committee of ISSCC, Symposium on VLSI, and A-SSCC and the TPC chair of the A-SSCC 2008 and ISWC 2010, IEEE Fellow, IEEE Distinguished Lecturer ('10-'11), Far East Chair of ISSCC ('11-'12), Technology Direction Sub-Committee Chair of ISSCC ('13), TPC Vice Chair of ISSCC ('14), and TPC Chair of ISSCC ('15).




---

