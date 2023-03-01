# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys

# Path setup
sys.path.insert(0, os.path.abspath('.'))

#html_dir = os.path.abspath('../docs')


project = 'Notes From Pycon Fr 2023'
copyright = '2023, Eric Narro'
author = 'Eric Narro'
release = '2023'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["myst_parser",
              "sphinx_rtd_theme"]

templates_path = ['_templates']
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme' #'alabaster'
#html_static_path = ['_static']
html_static_path = [os.path.join(os.path.abspath('.'), 'static')]

html_favicon = '../../input/pycon.jpg'

html_baseurl = '.'
html_output_dir = '../docs'
#html_output_dir = os.path.abspath(os.path.join('..', 'docs'))