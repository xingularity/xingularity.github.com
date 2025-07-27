# Sphinx Test Documentation

Welcome to the Sphinx Test Documentation repository! This documentation demonstrates the power of Sphinx with Markdown support using MyST parser.

## Features

- **Markdown Support**: Write documentation in Markdown format
- **Math Formulas**: Full LaTeX math support with MathJax
- **Code Highlighting**: Syntax highlighting for multiple languages
- **Rich Content**: Support for admonitions, tables, and more

## Table of Contents

```{toctree}
:maxdepth: 2
:caption: Contents:

articles/mathematics
articles/physics
articles/computer-science
```

## Quick Start

To build this documentation:

1. Install dependencies:
   ```bash
   make install
   ```

2. Build HTML documentation:
   ```bash
   make html
   ```
   or
   ```bash
   sphinx-build . _build
   ```

3. Serve locally:
   ```bash
   make serve
   ```

## Mathematical Example

Here's a quick example of inline mathematics: $E = mc^2$

And a display equation:

$$
\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
$$

Enjoy exploring the documentation!
