# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Lamp Light'
copyright = '%Y Zong-han, Xie'
author = 'Zong-han, Xie'
release = ''

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

import sphinx_pdj_theme
#html_theme = 'sphinx_rtd_theme'
#html_theme = 'sphinx_pdj_theme'
html_theme = 'sphinx_book_theme'
#html_theme = 'press'
#html_theme = 'groundwork'
#html_theme = 'alabaster'
#html_theme_path = [sphinx_pdj_theme.get_html_theme_path()]
html_static_path = ['_static']

# -- HTML Theme Options -----------------------------------------------------
html_theme_options = {
    "logo": {
        "image_light": "_static/lamp_3.jpg",
        "image_dark": "_static/lamp_3.jpg",
        "text": "Lamp Light",
    },
    "show_navbar_depth": 2,
    "show_toc_level": 2,
    "navigation_with_keys": False,
}

# Set the site logo
html_logo = "_static/lamp_3.jpg"

# Favicon (the small icon in browser tabs)
html_favicon = "_static/lamp_3.jpg"

# Custom CSS files
html_css_files = [
    'custom.css',
]

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
