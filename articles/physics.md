# Physics Formulas and Concepts

This article covers fundamental physics concepts with mathematical formulations.

## Classical Mechanics

### Newton's Laws

**First Law (Law of Inertia)**: An object at rest stays at rest, and an object in motion stays in motion at constant velocity, unless acted upon by a net force.

**Second Law**: The acceleration of an object is directly proportional to the net force acting on it:

$$
\mathbf{F} = m\mathbf{a}
$$

**Third Law**: For every action, there is an equal and opposite reaction:

$$
\mathbf{F}_{12} = -\mathbf{F}_{21}
$$

### Energy and Work

The work done by a force $\mathbf{F}$ over a displacement $\mathbf{s}$ is:

$$
W = \mathbf{F} \cdot \mathbf{s} = |\mathbf{F}||\mathbf{s}|\cos\theta
$$

Kinetic energy of an object with mass $m$ and velocity $v$:

$$
K = \frac{1}{2}mv^2
$$

Potential energy in a gravitational field:

$$
U = mgh
$$

Conservation of energy:

$$
K_i + U_i = K_f + U_f
$$

## Electromagnetism

### Coulomb's Law

The force between two point charges $q_1$ and $q_2$ separated by distance $r$:

$$
F = k\frac{q_1 q_2}{r^2} = \frac{1}{4\pi\epsilon_0}\frac{q_1 q_2}{r^2}
$$

### Maxwell's Equations

The four fundamental equations of electromagnetism:

**Gauss's Law**:
$$
\nabla \cdot \mathbf{E} = \frac{\rho}{\epsilon_0}
$$

**Gauss's Law for Magnetism**:
$$
\nabla \cdot \mathbf{B} = 0
$$

**Faraday's Law**:
$$
\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}
$$

**Ampère-Maxwell Law**:
$$
\nabla \times \mathbf{B} = \mu_0\mathbf{J} + \mu_0\epsilon_0\frac{\partial \mathbf{E}}{\partial t}
$$

### Electromagnetic Wave Equation

In vacuum, electromagnetic waves satisfy:

$$
\frac{\partial^2 \mathbf{E}}{\partial t^2} = c^2 \nabla^2 \mathbf{E}
$$

where $c = \frac{1}{\sqrt{\mu_0\epsilon_0}}$ is the speed of light.

## Quantum Mechanics

### Schrödinger Equation

The time-dependent Schrödinger equation:

$$
i\hbar\frac{\partial}{\partial t}\Psi(\mathbf{r},t) = \hat{H}\Psi(\mathbf{r},t)
$$

For a particle in a box, the time-independent equation becomes:

$$
-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} = E\psi
$$

### Heisenberg Uncertainty Principle

The fundamental limit on simultaneous measurement of position and momentum:

$$
\Delta x \Delta p \geq \frac{\hbar}{2}
$$

Similarly for energy and time:

$$
\Delta E \Delta t \geq \frac{\hbar}{2}
$$

### Wave-Particle Duality

De Broglie wavelength of a particle with momentum $p$:

$$
\lambda = \frac{h}{p}
$$

## Thermodynamics

### First Law of Thermodynamics

Energy conservation in thermodynamic processes:

$$
dU = \delta Q - \delta W
$$

where $U$ is internal energy, $Q$ is heat, and $W$ is work done by the system.

### Entropy

The change in entropy for a reversible process:

$$
dS = \frac{\delta Q_{rev}}{T}
$$

Boltzmann's entropy formula:

$$
S = k_B \ln \Omega
$$

where $\Omega$ is the number of microstates.

### Ideal Gas Law

For an ideal gas:

$$
PV = nRT = Nk_B T
$$

where $P$ is pressure, $V$ is volume, $n$ is number of moles, $N$ is number of particles, $R$ is the gas constant, and $k_B$ is Boltzmann's constant.

## Special Relativity

### Lorentz Transformation

Coordinate transformation between inertial frames:

$$
x' = \gamma(x - vt), \quad t' = \gamma\left(t - \frac{vx}{c^2}\right)
$$

where $\gamma = \frac{1}{\sqrt{1-v^2/c^2}}$ is the Lorentz factor.

### Mass-Energy Equivalence

Einstein's famous equation:

$$
E = mc^2
$$

For a moving particle:

$$
E^2 = (pc)^2 + (mc^2)^2
$$