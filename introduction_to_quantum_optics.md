# Introduction to Photon Statistics and Quantum Optics

## 1. Photon Number Statistics

In classical optics, light is treated as an electromagnetic wave. However, at the quantum level, light consists of discrete energy packets called photons. The statistical distribution of these photons provides profound insights into the nature of light sources.

### 1.1 Random Photon Streams and Poisson Statistics

#### Photon Streams and Time Bins

To understand photon statistics, we first need to conceptualize light as a stream of discrete photons arriving at a detector over time. Let's develop a model where we divide our total observation time $T$ into $M$ equal time bins, each of duration $\Delta t = T/M$.

For a light source with average intensity $I$, the average number of photons expected in the entire observation period is $\bar{n} = \alpha T$, where $\alpha$ is proportional to the intensity. The average number of photons per time bin is therefore $\mu = \bar{n}/M = \alpha \Delta t$.

In a random photon stream, the arrival of each photon is an independent event with no memory of previous arrivals. This means that for small enough time bins, each bin has:
- A probability $p = \mu$ of containing exactly one photon
- A probability $1-p$ of containing no photons
- A negligible probability of containing more than one photon (for sufficiently small $\Delta t$)

#### From Time Bins to Binomial Distribution

Given these properties, we can calculate the probability $P(n,M)$ of detecting exactly $n$ photons in $M$ time bins. This is equivalent to asking: what is the probability of having exactly $n$ successes in $M$ independent trials, where the probability of success in each trial is $p = \mu$?

This is precisely the binomial distribution:

$$P(n,M) = \binom{M}{n} p^n (1-p)^{M-n} = \binom{M}{n} \mu^n (1-\mu)^{M-n}$$

where $\binom{M}{n} = \frac{M!}{n!(M-n)!}$ is the binomial coefficient representing the number of ways to choose $n$ time bins from $M$ total bins.

#### The Poisson Limit

Now, let's consider what happens as we make our time bins smaller and more numerous. In the limit where $M \to \infty$ and $\Delta t \to 0$, while keeping the total observation time $T$ and the average photon number $\bar{n}$ constant:

1. The number of bins $M$ increases
2. The probability per bin $\mu = \bar{n}/M$ decreases
3. The product $M\mu = \bar{n}$ remains constant

In this limit, the binomial distribution approaches the Poisson distribution. To see this, we substitute $\mu = \bar{n}/M$ into the binomial formula:

$$P(n,M) = \binom{M}{n} \left(\frac{\bar{n}}{M}\right)^n \left(1-\frac{\bar{n}}{M}\right)^{M-n}$$

Rearranging:

$$P(n,M) = \frac{M!}{n!(M-n)!} \cdot \frac{\bar{n}^n}{M^n} \cdot \left(1-\frac{\bar{n}}{M}\right)^{M-n}$$

As $M \to \infty$, we can use the following approximations:

$$\frac{M!}{(M-n)!M^n} \approx 1$$

for large $M$ and fixed $n$, and:

$$\left(1-\frac{\bar{n}}{M}\right)^{M-n} \approx \left(1-\frac{\bar{n}}{M}\right)^M \approx e^{-\bar{n}}$$

applying the limit definition of the exponential function.

This gives us the Poisson distribution:

$$P(n) = \lim_{M \to \infty} P(n,M) = \frac{\bar{n}^n e^{-\bar{n}}}{n!}$$

where $\bar{n}$ is the mean photon number in the interval. 

#### Properties of the Poisson Distribution

The Poisson distribution has the remarkable property that its variance equals its mean:

$$\langle (\Delta n)^2 \rangle = \langle n \rangle = \bar{n}$$

This equal mean and variance is a signature of the randomness in the photon arrival process, where events occur independently and at a constant average rate.

To verify this property, we can calculate the mean and variance directly from the probability distribution:

The mean: $\langle n \rangle = \sum_{n=0}^{\infty} n P(n) = \bar{n}$

The variance: $\langle (\Delta n)^2 \rangle = \sum_{n=0}^{\infty} (n-\bar{n})^2 P(n) = \bar{n}$

#### Signal-to-Noise Ratio for Random Light

The signal-to-noise ratio (SNR) is a crucial metric in experimental physics, quantifying our ability to distinguish a signal from the background noise. For a measurement, the SNR is defined as the ratio of the mean signal to the standard deviation of the noise:

$$\text{SNR} = \frac{\text{signal}}{\text{noise}} = \frac{\langle n \rangle}{\sqrt{\langle (\Delta n)^2 \rangle}}$$

For random light following Poisson statistics, we have:

$$\text{SNR} = \frac{\bar{n}}{\sqrt{\bar{n}}} = \sqrt{\bar{n}}$$

This relationship reveals an important property of random light: the SNR scales as the square root of the mean photon number. This is known as the "shot noise limit" and represents a fundamental quantum limit to measurement precision with coherent light. To improve the SNR by a factor of 2, we need to increase the light intensity (or integration time) by a factor of 4.

This $\sqrt{\bar{n}}$ scaling of SNR is a direct consequence of the statistical independence of photon arrivals in coherent light and plays a crucial role in determining the sensitivity limits of optical measurements, from astronomical observations to laser-based communications.

This statistical behavior is characteristic of coherent light sources such as ideal lasers, where photon emission events are independent of each other.

### 1.2 Beam Splitters and Photon Statistics

A beam splitter is an optical component that splits an incident beam into two parts. For a 50:50 beam splitter, an incoming photon has equal probability of being transmitted or reflected. Interestingly, when random (Poissonian) light is incident on a beam splitter, the statistics of the output beams remain Poissonian.

To understand why, consider that each photon in the input beam makes an independent decision to be transmitted or reflected. If the input beam has Poisson statistics with mean $\bar{n}$, the transmitted beam will have a mean of $\bar{n}_T = R\bar{n}$ and the reflected beam will have a mean of $\bar{n}_R = T\bar{n}$, where $R$ and $T$ are the reflection and transmission coefficients ($R + T = 1$).

The independence of photon behavior ensures that both output beams maintain Poisson statistics, just with scaled means. This is mathematically represented as:

$$P_T(n_T) = \frac{(R\bar{n})^{n_T} e^{-R\bar{n}}}{n_T!}$$

$$P_R(n_R) = \frac{(T\bar{n})^{n_R} e^{-T\bar{n}}}{n_R!}$$

This preservation of statistics is a direct consequence of the binomial sampling of the original Poisson distribution, which yields another Poisson distribution.

### 1.3 Thermal Light and Exponential Statistics

Thermal light, such as that emitted by incandescent bulbs or stars, exhibits different statistical properties. The emission process in thermal sources involves atoms transitioning between energy levels due to thermal excitation. This process leads to what we call "bunching" of photons.

For thermal light, the probability distribution of photons follows:

$$P(n) = \frac{\bar{n}^n}{(1+\bar{n})^{n+1}}$$

This distribution results in a variance that exceeds the mean:

$$\langle (\Delta n)^2 \rangle = \langle n \rangle + \langle n \rangle^2 = \bar{n} + \bar{n}^2$$

The photon number fluctuations are larger than in coherent light, reflecting the bunching tendency of thermal photons. This bunching arises from the Bose-Einstein statistics governing photons, which encourages multiple photons to occupy the same mode.

The intensity fluctuations of thermal light follow an exponential distribution:

$$P(I) = \frac{1}{\langle I \rangle} e^{-I/\langle I \rangle}$$

This exponential behavior is a direct consequence of the random nature of thermal emission processes, where the radiation field is built up from the contributions of many independent atomic emitters.

#### Signal-to-Noise Ratio for Thermal Light

The signal-to-noise ratio for thermal light differs significantly from that of coherent light due to the different statistical distribution of photons. Using the definition of SNR as the ratio of mean signal to the standard deviation of noise:

$$\text{SNR} = \frac{\langle n \rangle}{\sqrt{\langle (\Delta n)^2 \rangle}}$$

For thermal light, with $\langle (\Delta n)^2 \rangle = \bar{n} + \bar{n}^2$, we have:

$$\text{SNR} = \frac{\bar{n}}{\sqrt{\bar{n} + \bar{n}^2}} = \frac{\bar{n}}{\bar{n}\sqrt{\frac{1}{\bar{n}} + 1}}$$

In the limit of large photon numbers ($\bar{n} \gg 1$), which is common for thermal light sources, this simplifies to:

$$\text{SNR} \approx \frac{\bar{n}}{\bar{n}} = 1$$

This is a striking result: for thermal light at high intensities, the SNR approaches a constant value of 1, regardless of how much we increase the intensity. This is in stark contrast to the coherent light case where SNR increases as $\sqrt{\bar{n}}$.

This fundamental limitation on the SNR of thermal light is due to the inherent "excess noise" from photon bunching. It explains why many precision optical measurements preferentially use laser sources (with Poisson statistics) rather than thermal sources, even when high intensities are available.

The comparison between thermal light (SNR ~ 1) and coherent light (SNR ~ $\sqrt{\bar{n}}$) provides a clear example of how the quantum statistical properties of a light source directly impact measurement sensitivity in practical applications.

## 2. From Classical Fields to Quantum Optics

### 2.1 Quantization of the Electromagnetic Field

To transition from classical optics to quantum optics, we need to quantize the electromagnetic field. We start with Maxwell's equations in vacuum and consider a single mode of the field in a cavity of volume $V$.

The classical electric and magnetic fields for a mode with wavevector $\vec{k}$ and polarization $\vec{\epsilon}$ can be written as:

$$\vec{E}(\vec{r},t) = E_0(a(t)\vec{\epsilon}e^{i\vec{k}\cdot\vec{r}} + a^*(t)\vec{\epsilon}^*e^{-i\vec{k}\cdot\vec{r}})$$
$$\vec{B}(\vec{r},t) = B_0(a(t)(\vec{k}\times\vec{\epsilon})e^{i\vec{k}\cdot\vec{r}} + a^*(t)(\vec{k}\times\vec{\epsilon})^*e^{-i\vec{k}\cdot\vec{r}})$$

where $E_0$ and $B_0$ are constants, and $a(t)$ and $a^*(t)$ are complex amplitudes.

The energy of this field is:

$$H = \frac{1}{2}\int_V (\epsilon_0 E^2 + \frac{1}{\mu_0}B^2)d^3r = \hbar\omega(a^*a + \frac{1}{2})$$

Observe that this has the same form as the Hamiltonian of a quantum harmonic oscillator. This suggests replacing the complex amplitudes $a$ and $a^*$ with operators $\hat{a}$ and $\hat{a}^\dagger$ that satisfy the commutation relation:

$$[\hat{a}, \hat{a}^\dagger] = 1$$

The Hamiltonian then becomes:

$$\hat{H} = \hbar\omega(\hat{a}^\dagger\hat{a} + \frac{1}{2})$$

This is precisely the Hamiltonian of a quantum harmonic oscillator, where $\hat{a}^\dagger\hat{a}$ is the number operator $\hat{n}$ that counts the number of photons in the mode.

### 2.2 Photon States and Quadrature Components

The energy eigenstates of this quantum harmonic oscillator are the Fock states $|n\rangle$, which represent states with exactly $n$ photons. The action of the creation and annihilation operators on these states is:

$$\hat{a}^\dagger|n\rangle = \sqrt{n+1}|n+1\rangle$$
$$\hat{a}|n\rangle = \sqrt{n}|n-1\rangle$$

Just as in a mechanical harmonic oscillator with position $x$ and momentum $p$, we can define quadrature components for the quantized electromagnetic field:

$$\hat{X} = \frac{1}{\sqrt{2}}(\hat{a} + \hat{a}^\dagger)$$
$$\hat{P} = \frac{i}{\sqrt{2}}(\hat{a}^\dagger - \hat{a})$$

These operators are analogous to the position and momentum operators of a mechanical oscillator and satisfy the commutation relation:

$$[\hat{X}, \hat{P}] = i$$

The physical interpretation of these quadratures becomes clear when we look at the expectation value of the electric field operator in a coherent state $|\alpha\rangle$ (which is the quantum state that most closely resembles a classical electromagnetic wave):

$$\langle\alpha|\hat{E}(\vec{r},t)|\alpha\rangle \propto \langle\alpha|(\hat{a}e^{-i\omega t} + \hat{a}^\dagger e^{i\omega t})|\alpha\rangle = 2|\alpha|\cos(\omega t - \phi)$$

where $\alpha = |\alpha|e^{i\phi}$.

We can see that $\hat{X}$ and $\hat{P}$ correspond to the amplitude and phase quadratures of the field, respectively. They are the quantum analogs of the in-phase and out-of-phase components of a classical electromagnetic wave.

The uncertainty principle for these quadratures,

$$\Delta X \cdot \Delta P \geq \frac{1}{2}$$

implies fundamental limits on our ability to simultaneously determine both quadratures with arbitrary precision. This leads to interesting quantum states of light such as squeezed states, where the uncertainty in one quadrature is reduced below the standard quantum limit at the expense of increased uncertainty in the conjugate quadrature.

## 3. Photon Entanglement on a Beam Splitter

### 3.1 Quantum Operator Approach to Entanglement

One of the most fascinating phenomena in quantum optics is the creation of entangled photon states. A beam splitter, beyond its classical role, can actually generate quantum entanglement under specific conditions.

Consider a situation where two identical photons simultaneously enter a 50:50 beam splitter from different input ports. Quantum mechanically, we denote the creation operators for the input ports as $\hat{a}^\dagger$ and $\hat{b}^\dagger$, and for the output ports as $\hat{c}^\dagger$ and $\hat{d}^\dagger$.

The beam splitter transformation can be written as:

$$\hat{c}^\dagger = \frac{1}{\sqrt{2}}(\hat{a}^\dagger + \hat{b}^\dagger)$$
$$\hat{d}^\dagger = \frac{1}{\sqrt{2}}(\hat{a}^\dagger - \hat{b}^\dagger)$$

The initial state with one photon in each input port is $|1_a, 1_b\rangle = \hat{a}^\dagger \hat{b}^\dagger |0\rangle$. After passing through the beam splitter, this state becomes:

$$\hat{a}^\dagger \hat{b}^\dagger |0\rangle \rightarrow \frac{1}{2}(\hat{c}^\dagger + \hat{d}^\dagger)(\hat{c}^\dagger - \hat{d}^\dagger)|0\rangle = \frac{1}{2}((\hat{c}^\dagger)^2 - (\hat{d}^\dagger)^2)|0\rangle$$

Simplifying, we get:

$$\frac{1}{\sqrt{2}}(|2_c, 0_d\rangle - |0_c, 2_d\rangle)$$

This is an entangled state where either both photons exit through port $c$ or both exit through port $d$, with no possibility of one photon in each output port. This phenomenon, known as the Hong-Ou-Mandel effect, is a direct manifestation of quantum interference and photon indistinguishability.

The entanglement is evident because the state cannot be factorized into a product of states for the two output modes. This non-classical correlation is a resource for quantum information processing and quantum communication protocols.

### 3.2 Probability Amplitude Approach to Entanglement

We can also understand photon entanglement through the language of probability amplitudes and phase factors, which may be more intuitive for visualizing what happens at a beam splitter.

When a single photon encounters a beam splitter, there are two possible outcomes: reflection or transmission. In quantum mechanics, we associate probability amplitudes with each outcome:

- For reflection: amplitude $r = \sqrt{R}e^{i\phi_r}$, where $R$ is the reflection probability and $\phi_r$ is a phase factor
- For transmission: amplitude $t = \sqrt{T}e^{i\phi_t}$, where $T$ is the transmission probability and $\phi_t$ is a phase factor

For a 50:50 beam splitter, $R = T = 1/2$. Importantly, the phase relationship between reflection and transmission must satisfy $\phi_r - \phi_t = \pi/2$ for energy conservation, which is typically implemented as $r = 1/\sqrt{2}$ and $t = i/\sqrt{2}$, where the imaginary unit $i$ represents a 90u00b0 phase shift.

Now, consider two photons entering the beam splitter from different input ports (let's call them 1 and 2). There are four possible outcomes:

1. Both photons are reflected: Amplitude = $r_1 r_2 = 1/2$
2. Both photons are transmitted: Amplitude = $t_1 t_2 = (i/\sqrt{2})^2 = i^2/2 = -1/2$
3. Photon 1 reflected, Photon 2 transmitted: Amplitude = $r_1 t_2 = (1/\sqrt{2})(i/\sqrt{2}) = i/2$
4. Photon 1 transmitted, Photon 2 reflected: Amplitude = $t_1 r_2 = (i/\sqrt{2})(1/\sqrt{2}) = i/2$

The key insight comes when we consider the output ports (let's call them 3 and 4). For both photons to exit through port 3, either both must be reflected or both must be transmitted. The combined amplitude is:

$$A_{both~in~3} = r_1 r_2 + t_1 t_2 = 1/2 + (-1/2) = 0$$

Similarly, for both photons to exit through port 4:

$$A_{both~in~4} = t_1 r_2 + r_1 t_2 = i/2 + i/2 = i$$

For one photon in each output port, the amplitude is zero due to destructive interference.

Squaring these amplitudes to get probabilities:

- Probability of both photons in port 3: $|0|^2 = 0$
- Probability of both photons in port 4: $|i|^2 = 1$
- Probability of one photon in each port: $0$

This means the photons always exit together through the same port (in this case, port 4), never one in each port. The two photons are now entangled - they behave as a single entity rather than two independent particles.

If we adjust our phase convention slightly to maintain symmetry between the ports, we get the state:

$$\frac{1}{\sqrt{2}}(|2_3, 0_4\rangle - |0_3, 2_4\rangle)$$

which matches our result from the operator formalism.

This phase-dependent quantum interference demonstrates how the simple process of reflection and transmission, combined with the wave nature of quantum particles, leads to complex phenomena like entanglement. The phase factors are crucial - without the $\pi/2$ phase difference between reflection and transmission, this entanglement would not occur.

## Conclusion

This introduction has taken us from the statistical nature of photons to the quantum description of the electromagnetic field. We've seen how random photon streams lead to Poisson statistics, how beam splitters interact with these statistics, and how thermal light exhibits exponential intensity distribution due to the bunching of photons.

We've also established the connection between Maxwell's equations and the quantum harmonic oscillator, introducing the concept of photon number states and field quadratures. Finally, we've explored how beam splitters can create quantum entanglement between photons, demonstrating the non-classical nature of light.

These foundations of quantum optics open the door to a rich field of study, including quantum information processing, quantum metrology, and quantum communication, where the quantum properties of light are harnessed for technological applications beyond the capabilities of classical systems.