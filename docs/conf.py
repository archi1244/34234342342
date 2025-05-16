import os
import sys
sys.path.insert(0, os.path.abspath('..'))

project = 'CalculatorDoc'
copyright = '2025, Your Name'
author = 'Your Name'
release = '1.1'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
exclude_patterns = []
html_theme = 'alabaster'
html_static_path = ['_static']
language = 'ru'

def setup(app):
    app.add_css_file('custom.css')
