# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Sphinx Test Documentation'
copyright = '2025, Documentation Team'
author = 'Documentation Team'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.mathjax',
    'nbsphinx',
    'sphinx.ext.intersphinx',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# -- MyST Parser Configuration -----------------------------------------------
myst_enable_extensions = [
    "amsmath",
    "attrs_inline",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]

# Enable math rendering
myst_dmath_double_inline = True

# Source file suffixes
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
    '.ipynb': 'jupyter_notebook',
}

# -- nbsphinx Configuration --------------------------------------------------
# Don't execute notebooks during build (for performance and reproducibility)
nbsphinx_execute = 'never'

# Timeout for notebook execution (if enabled)
nbsphinx_timeout = 60

# Allow errors in notebooks (optional)
nbsphinx_allow_errors = True

# Configure notebook kernels
nbsphinx_kernel_name = 'python3'

# Use nbconvert's built-in HTML converter instead of Pandoc
nbsphinx_codecell_lexer = 'ipython3'

# Suppress pandoc warnings and use alternative conversion
suppress_warnings = ['nbsphinx.pandoc']

# Configure nbsphinx to work without pandoc by using nbconvert directly
import os
import sys
try:
    # Try to use system pandoc if available
    import subprocess
    result = subprocess.run(['pandoc', '--version'], capture_output=True, text=True)
    if result.returncode != 0:
        raise FileNotFoundError
except (FileNotFoundError, subprocess.SubprocessError):
    # If pandoc not found, configure nbsphinx to use alternatives
    pass
