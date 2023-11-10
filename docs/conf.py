# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys

sys.path.insert(0, os.path.abspath(".."))

project = 'calculator'
copyright = '2023, ampersandor'
author = 'ampersandor'
release = '0.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.napoleon",
    "sphinx.ext.autodoc",
    "sphinx.ext.todo",
    "sphinx.ext.githubpages",
    "sphinx.ext.viewcode",
    "sphinx.ext.autosummary",
    "sphinx_autodoc_typehints",
    'sphinxcontrib.mermaid',
    'myst_parser'
]

templates_path = ['_templates']
exclude_patterns = [".venv", "_build", "Thumbs.db", "*.egg-info", ".DS_Store", "**.ipynb_checkpoints"]



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "pydata_sphinx_theme"
html_static_path = ['_static']
html_css_files = ["style.css"]


##########################################  Manual configuration ##########################################
# default config
add_module_names = True  # Remove namespaces from class/method signatures

# sphinx.ext.napoleon
# napoleon_include_init_with_doc = True  # __init__ 출력

# sphinx.ext.todo
todo_include_todos = True  # Todo 출력

# sphinx.ext.autodoc
autosummary_generate = True  # Turn on sphinx.ext.autosummary
# autodoc_inherit_docstrings = True  # If no docstring, inherit from base class
# autosummary_mock_imports = ["src.catcher.config", "src.tag.config"]  # Prevent config modules converted into rst

html_show_sphinx = False

html_theme_options = {
  "show_toc_level": 2,
  "logo": {
      "text": "ampersandor",
      "image_dark": "_static/favicon.ico",
      "alt_text": "ampersandor",
  },
  "show_toc_level": 1,
  "navbar_align": "left",
  "navigation_with_keys": True
}

# -- Extension configuration -------------------------------------------------
html_js_files = [
  'https://cdn.jsdelivr.net/npm/mermaid@10.2.4/dist/mermaid.min.js'
]