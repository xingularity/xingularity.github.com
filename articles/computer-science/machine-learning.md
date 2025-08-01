# Machine Learning

## Linear Regression

Cost function for linear regression:

$$
J(\theta) = \frac{1}{2m} \sum_{i=1}^{m} (h_\theta(x^{(i)}) - y^{(i)})^2
$$

Normal equation for optimal parameters:

$$
\theta = (X^T X)^{-1} X^T y
$$

## Gradient Descent

Parameter update rule:

$$
\theta_j := \theta_j - \alpha \frac{\partial}{\partial \theta_j} J(\theta)
$$

where $\alpha$ is the learning rate.

## Neural Networks

**Sigmoid activation function**:
$$
\sigma(z) = \frac{1}{1 + e^{-z}}
$$

**ReLU activation function**:
$$
\text{ReLU}(z) = \max(0, z)
$$

**Softmax function** for multi-class classification:
$$
\text{softmax}(z_i) = \frac{e^{z_i}}{\sum_{j=1}^{K} e^{z_j}}
$$