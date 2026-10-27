# Part 03c · Signals, Systems & Communications · TOPIC LIST

Rules and directives for this part: `index/part03c_signals_systems_and_communications.rules.md`. This file is the topic list only; the Learning method and this domain's prerequisites, depth bar and capstone are in the rules file.

Domain: Signals, Systems & Communications

### Signals and linear time-invariant systems

- **LTI systems and impulse response**: linearity and time invariance; the impulse response h[n] as the output to a unit impulse; the output to any input as convolution with h, derived from the sifting property; discrete-time systems given by difference equations; causality and memory read from h; the unit step u[n] as the running sum of the impulse and the step response as the convolution of u with h; convolution's commutativity, associativity and distributivity over addition, which justify reordering cascaded systems and summing parallel ones
- **Autocorrelation**: r_xx[k] = Σ x[n]·x[n+k] for deterministic and random signals; symmetry and the maximum at zero lag; autocorrelation of an LTI output as the input's autocorrelation filtered by h; the Wiener–Khinchin relation to the power spectral density; biased and unbiased estimators from a finite record; white noise with a flat power spectral density, and the power in a frequency band as the integral of the PSD over that band
- **Periodic sampling and aliasing**: the sampled spectrum as replicas of the original at multiples of the sampling rate; the Nyquist–Shannon condition and folding when it fails; reconstruction by ideal sinc interpolation; anti-aliasing filters before the converter; a tone above half the sampling rate folding to a lower frequency
- **Quadrature signals and the Hilbert transform**: the analytic signal x + j·H{x} and its one-sided spectrum; in-phase and quadrature (I/Q) decomposition of a bandpass signal; instantaneous amplitude and phase read from the analytic signal; why complex baseband mixing underlies every quadrature receiver
- **BIBO stability**: bounded input gives bounded output exactly when Σ|h[n]| is finite (the integral of |h(t)| in continuous time); the proof by the triangle inequality and a counterexample with a non-summable impulse response
- **Signal classes, energy and power**: energy E = Σ|x[n]|² (or ∫|x(t)|² dt) and power P = lim (1/(2N + 1))·Σ from n = −N to N of |x[n]|², with energy signals having finite E and zero P and power signals having finite nonzero P; system classes memoryless, causal, linear, time-invariant, stable and invertible, each decided from the defining input–output rule
- **Complex exponentials, eigenfunctions and frequency response**: a complex exponential e^(jωn) passed through an LTI system with impulse response h gives H(e^(jω))·e^(jωn), where H(e^(jω)) = Σ h[n]·e^(−jωn) is the frequency response; the magnitude |H| and the phase arg H give the gain and phase shift at each frequency

### Transforms and system analysis

- **Laplace transform and its inverse**: X(s) = ∫ x(t)·e^(−st) dt; the transform of a derivative with its initial condition, so a linear differential equation becomes algebra; the inverse by partial fractions and the Bromwich integral; the region of convergence as the half-plane where the integral exists; the initial- and final-value theorems
- **z-transform, its inverse and region of convergence**: X(z) = Σ x[n]·z^(−n); the shift property as multiplication by z^(−1); the inverse by long division, partial fractions and residues; the region of convergence as an annulus that decides causality and whether the unit circle lies inside it, and so stability
- **Transfer functions**: H(s) = Y(s)/X(s) with zero initial state; H(z) from a difference equation; gain and phase by evaluation on the imaginary axis or the unit circle; poles and zeros as the features that set the shape of the response
- **Pole-zero stability**: a causal LTI system is stable exactly when every pole lies in the open left half-plane (continuous time) or strictly inside the unit circle (discrete time); the Routh–Hurwitz and Jury tests; a pole near the boundary as the source of slow, ringing responses
- **State-space analysis of LTI systems**: x′ = Ax + Bu and y = Cx + Du (discrete: x[n+1] = Ax[n] + Bu[n]); the transfer function C(sI − A)⁻¹B + D; the eigenvalues of A as the poles; controllability and observability matrices and their rank tests; different realizations of one transfer function
- **Linear feedback systems**: closed-loop transfer function G/(1 + GK) for negative feedback; the characteristic equation 1 + GK = 0; sensitivity and complementary sensitivity; the Nyquist criterion; gain and phase margins as measures of robustness; feedback gain traded against noise amplification
- **Fourier series and transforms in continuous and discrete time**: the Fourier series of a periodic signal with coefficients c_k = (1/T)∫ x(t)·e^(−j2πkt/T) dt, whose magnitudes |c_k| give the harmonic content; the Fourier transform X(ω) = ∫ x(t)·e^(−jωt) dt and its inverse; the discrete-time Fourier transform X(e^(jω)) = Σ x[n]·e^(−jωn) and the discrete-time Fourier series of a periodic sequence; the convolution theorem, under which convolution in time becomes multiplication of spectra; Parseval's identity for energy; convergence at a jump discontinuity to the midpoint, under Dirichlet's conditions

### Digital filters and multirate processing

- **FIR and IIR design**: windowed-sinc and Parks–McClellan equiripple FIR design with linear phase; IIR design by the bilinear transform from Butterworth and Chebyshev analogue prototypes; the trade of FIR length against IIR order and phase distortion
- **Quantization and fixed-point effects**: uniform quantizer noise of Δ²/12 and the signal-to-quantization-noise ratio of about 6.02b + 1.76 dB; rounding versus truncation bias; Q-format fixed-point arithmetic with overflow; coefficient quantization moving poles and zeros; limit cycles in recursive filters
- **Multirate processing**: decimation as anti-alias filtering followed by downsampling; interpolation as zero insertion followed by an image-rejection filter; the noble identities that move filters across rate changers; the spectral scaling by M and by L
- **Polyphase filters and sample-rate conversion**: polyphase decomposition of an FIR filter; efficient decimators and interpolators that compute only the retained outputs; rational resampling by L/M; multiplications per output sample as the cost measure
- **Filter banks and wavelets**: analysis and synthesis banks; perfect-reconstruction conditions for two-channel quadrature mirror and biorthogonal designs; the discrete wavelet transform as a multiresolution decomposition with a scaling function and a wavelet; time–frequency localisation compared with the short-time Fourier transform
- **CIC filters**: cascaded integrator–comb decimators with transfer function ((1 − z^(−RM))/(1 − z^(−1)))^N; multiplier-free operation with wrap-around arithmetic; passband droop and its correction by a short FIR; output bit growth of N·log₂(RM) bits

### Practical spectral analysis

- **Goertzel and chirp-z transforms**: the Goertzel recursion computing one DFT bin with a second-order filter and one multiplication per sample; the chirp-z transform evaluating the z-transform on an arbitrary arc or grid through Bluestein's identity and a convolution; choosing either over the FFT when few or off-grid bins are needed
- **Parseval and reconstruction checks**: Parseval's energy equality Σ|x[n]|² = (1/N)·Σ|X[k]|² for the DFT; round-trip tests of analysis followed by synthesis as unit checks of a transform implementation; the scaling and leakage mistakes these checks catch
- **Signal averaging**: coherent averaging of N time-aligned records improves signal-to-noise ratio by √N when the noise is uncorrelated; time alignment as the precondition; exponential averaging and its effective window; bias introduced by misalignment
- **Cepstral analysis**: the real cepstrum c[n] = IDFT(log|X[k]|), turning multiplication in the spectrum into addition; separating a slowly varying spectral envelope from fine structure by liftering; the quefrency axis
- **Parametric signal modelling (LPC)**: the all-pole autoregressive model x[n] = −Σ a_k·x[n−k] + e[n]; the Levinson–Durbin recursion solving the Yule–Walker equations; the prediction-error filter; all-pole spectrum estimates and model-order choice
- **Frequency translation**: multiplying by a complex exponential shifts the spectrum by its frequency; digital down-conversion with a numerically controlled oscillator and I/Q mixing; the image term from real mixing and its removal by a low-pass filter before decimation
- **Radix-2 FFT and bit reversal**: the decimation-in-time recursion splitting an N-point DFT into DFTs of the even- and odd-indexed samples, each of length N/2, combined with twiddle factors W_N^k = e^(−j2πk/N); bit-reversed input ordering so the butterflies run in place; N log₂ N complex multiplications against N² for the direct sum
- **Leakage, windowing and scalloping**: a tone that does not complete a whole number of cycles in the record leaks into neighbouring bins; a window trades main-lobe width against sidelobe level; the scalloping loss is the dip in a bin's level when the tone falls between bins, about 1.42 dB at the midpoint for the Hann window

### Digital communications

- **Modulation: AM, PAM, PSK and QAM**: amplitude modulation as a message times a carrier; pulse amplitude modulation mapping bits to levels; phase-shift keying as points on the unit circle; quadrature amplitude modulation as two PAM streams on cosine and sine carriers; Gray mapping; average symbol energy and bandwidth set by the pulse shape; the Nyquist criterion for zero intersymbol interference and the raised-cosine pulse
- **Optimum receivers in AWGN**: the matched filter as the receiver that maximizes output signal-to-noise ratio, equal to the correlator; the minimum-distance (maximum-likelihood) decision rule for equiprobable symbols; the Q-function error probability, for example BPSK bit error probability Q(√(2E_b/N₀)); the union bound for M-ary constellations
- **Carrier and symbol synchronization (PLL)**: the phase-locked loop with phase detector, loop filter and voltage-controlled oscillator; the loop-bandwidth trade of tracking speed against noise; the Costas loop for suppressed-carrier signals; the Gardner timing-error detector for symbol timing; acquisition and cycle slips
- **Adaptive equalization**: intersymbol interference from a dispersive channel; the least-mean-squares (LMS) and recursive least-squares (RLS) updates for adaptive linear equalizers; decision-feedback equalizers; training sequences and convergence speed
- **Spread spectrum and OFDM**: direct-sequence spreading with pseudo-noise codes and processing gain; frequency hopping; orthogonal frequency-division multiplexing as an inverse DFT over subcarriers; the cyclic prefix turning linear into circular convolution; a one-tap equalizer per subcarrier
- **MIMO and multiple antennas**: the channel matrix H linking transmit and receive antennas; spatial multiplexing gain min(N_t, N_r); diversity from the Alamouti space–time code; capacity log₂ det(I + (SNR/N_t)·HH*) in bits per second per hertz
- **Fading channels (Rayleigh and Ricean)**: multipath, Doppler spread, coherence time and coherence bandwidth; Rayleigh fading without a line-of-sight path and Ricean fading with its K-factor; average bit-error rate over Rayleigh fading and its diversity slope
- **Multiuser communications**: multiple access by frequency, time and code (FDMA, TDMA, CDMA); the capacity region of the Gaussian multiple-access channel; successive interference cancellation and the order of decoding

### Exercises

- From scratch: a discrete LTI system from its difference equation, its impulse response and its output by convolution, checked against direct simulation; a tone sampled above and below the Nyquist rate, with the aliased frequency predicted before it is measured
- From scratch: a pole-zero and stability checker for a rational transfer function, with a state-space realization and a step response compared with the predicted pole locations
- From scratch: an FIR filter by windowed sinc and an IIR low-pass by the bilinear transform, both designed by hand, then reproduced with a library design routine and compared on frequency response and fixed-point quantization error
- From scratch: a polyphase decimator and interpolator, checked by a spectrum comparison and a round-trip test; a CIC decimator with its bit-width computed before the run
- From scratch: a Goertzel tone detector and an LPC estimator by the Levinson–Durbin recursion, each compared with a periodogram on the same record
- From scratch: a BPSK and QAM link over an AWGN channel at baseband, measuring bit-error rate across a range of Eb/N0 and plotting it against the theoretical Q-function curve
- From scratch: a PLL carrier-recovery loop that locks to a frequency offset, and an OFDM transmitter and receiver with a cyclic prefix and one-tap equalizer over a Rayleigh fading channel
- From scratch: a radix-2 FFT with bit-reversed ordering, checked against the direct DFT on random records and counted in complex multiplications against N log₂ N, then used to measure the Hann-windowed leakage of a tone placed between two bins
- **Reasoning drills**
  - Given an impulse response h[n] = 0.9ⁿ for n ≥ 0 and a bounded input, decide BIBO stability by summing |h[n]|, then predict the peak output before simulating it
  - Given a rational transfer function, find its poles and region of convergence, decide stability from the pole locations, then predict the step response before simulating it
  - Show that quantizing a sine wave to b bits gives a signal-to-quantization-noise ratio near 6.02b + 1.76 dB, then measure it and explain any gap
  - Predict the signal-to-noise gain from coherently averaging 64 time-aligned records of a tone in noise, measure it, then predict what a one-sample misalignment does to the gain
  - For a 16-QAM link at a stated Eb/N₀, estimate the bit-error rate from the AWGN curve, then predict how much a Rayleigh fading channel changes it and why
