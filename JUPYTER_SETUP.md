# Jupyter Notebook Integration with Sphinx

This repository now supports Jupyter notebooks (.ipynb files) as part of the Sphinx documentation build process.

## Setup

### 1. Install Dependencies

#### Python Dependencies
Install the required Python packages:

```bash
pip install -r requirements.txt
```

Or install specific Jupyter-related packages:

```bash
pip install nbsphinx jupyter notebook ipykernel matplotlib numpy pandas seaborn
```

#### System Dependencies
Install Pandoc (required for notebook conversion):

**macOS:**
```bash
brew install pandoc
```

**Ubuntu/Debian:**
```bash
sudo apt-get install pandoc
```

**Windows:**
Download from https://pandoc.org/installing.html

**Alternative (Python package):**
```bash
pip install pandoc
```

### 2. Creating Jupyter Notebooks

1. Create `.ipynb` files in the appropriate topic directories (e.g., `articles/mathematics/`)
2. Add them to the topic index files (e.g., `articles/mathematics.md`)
3. Notebooks will be automatically included in the Sphinx build

### 3. Notebook Configuration

The Sphinx configuration (`conf.py`) includes:

- **nbsphinx extension**: Processes Jupyter notebooks
- **Execution disabled**: Notebooks are not executed during build for performance
- **Error handling**: Allows notebooks with errors to be included
- **Kernel specification**: Uses Python 3 kernel

### 4. Best Practices

#### For Notebook Authors:

1. **Clear outputs before committing**: Use "Restart & Clear Output" before saving
2. **Add markdown cells**: Provide clear explanations between code cells
3. **Use proper headings**: Structure content with # ## ### headings
4. **Include imports**: Make sure all necessary imports are at the beginning
5. **Add docstrings**: Document functions and methods clearly

#### For Documentation:

1. **Link from index pages**: Add notebook links to topic index files
2. **Use descriptive names**: Give notebooks clear, descriptive filenames
3. **Include in toctree**: Add notebooks to Sphinx toctree directives when needed

### 5. Building Documentation

Build the documentation as usual:

```bash
# Using Makefile
make html

# Using sphinx-build directly
sphinx-build . _build
```

### 6. Notebook Features

The example notebook (`articles/mathematics/numerical-methods.ipynb`) demonstrates:

- **Mathematical equations**: LaTeX rendering in markdown cells
- **Code execution**: Python code with output
- **Plots and visualizations**: Matplotlib/Seaborn charts
- **Interactive content**: Demonstrations of numerical methods
- **Professional formatting**: Clean, readable presentation

### 7. Advanced Configuration

You can modify `conf.py` to customize notebook behavior:

```python
# Enable notebook execution during build (slower but shows current outputs)
nbsphinx_execute = 'always'

# Custom timeout for execution
nbsphinx_timeout = 120

# Custom CSS styling
nbsphinx_custom_formats = {
    '.md': ['jupytext.reads', {'fmt': 'mystnb'}]
}
```

### 8. Troubleshooting

**Common issues:**

1. **Missing dependencies**: Install all packages listed in requirements.txt
2. **Kernel not found**: Ensure Python 3 kernel is available: `python -m ipykernel install --user`
3. **Build errors**: Check that notebooks run without errors in Jupyter
4. **Math rendering**: Ensure MathJax is properly configured in conf.py

**Checking notebook validity:**

```bash
# Test notebook execution
jupyter nbconvert --execute --to notebook numerical-methods.ipynb

# Clear outputs
jupyter nbconvert --clear-output numerical-methods.ipynb
```

## Example Integration

See `articles/mathematics/numerical-methods.ipynb` for a complete example showing:

- Newton's method for root finding
- Numerical integration (Trapezoidal and Simpson's rules)
- Monte Carlo integration
- Convergence analysis with visualizations

The notebook is automatically integrated into the mathematics section and rendered as part of the Sphinx documentation.