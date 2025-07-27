# Mathematical Concepts

This article demonstrates various mathematical concepts and formulas using LaTeX notation in Markdown.

## Calculus

### Derivatives

The derivative of a function $f(x)$ is defined as:

$$
f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}
$$

Some common derivatives:
- $\frac{d}{dx}[x^n] = nx^{n-1}$
- $\frac{d}{dx}[e^x] = e^x$
- $\frac{d}{dx}[\sin x] = \cos x$
- $\frac{d}{dx}[\ln x] = \frac{1}{x}$

### Integrals

The fundamental theorem of calculus states:

$$
\int_a^b f'(x) dx = f(b) - f(a)
$$

Some important integrals:

$$
\int e^x dx = e^x + C
$$

$$
\int \frac{1}{x} dx = \ln|x| + C
$$

$$
\int \sin x dx = -\cos x + C
$$

## Linear Algebra

### Matrix Operations

For matrices $A$ and $B$, matrix multiplication is defined when the number of columns in $A$ equals the number of rows in $B$:

$$
(AB)_{ij} = \sum_{k=1}^{n} A_{ik}B_{kj}
$$

### Eigenvalues and Eigenvectors

For a square matrix $A$, an eigenvalue $\lambda$ and its corresponding eigenvector $\mathbf{v}$ satisfy:

$$
A\mathbf{v} = \lambda\mathbf{v}
$$

The characteristic equation is:

$$
\det(A - \lambda I) = 0
$$

## Probability Theory

### Bayes' Theorem

Given events $A$ and $B$, Bayes' theorem states:

$$
P(A|B) = \frac{P(B|A)P(A)}{P(B)}
$$

### Normal Distribution

The probability density function of a normal distribution is:

$$
f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2}
$$

where $\mu$ is the mean and $\sigma$ is the standard deviation.

## Complex Analysis

### Euler's Formula

One of the most beautiful equations in mathematics:

$$
e^{i\theta} = \cos\theta + i\sin\theta
$$

Setting $\theta = \pi$ gives us Euler's identity:

$$
e^{i\pi} + 1 = 0
$$

### Cauchy-Riemann Equations

For a complex function $f(z) = u(x,y) + iv(x,y)$ to be analytic, it must satisfy:

$$
\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}, \quad \frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}
$$