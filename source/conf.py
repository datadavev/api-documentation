#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This work was created by participants in the DataONE project, and is
# jointly copyrighted by participating institutions in DataONE. For
# more information on DataONE, see our web site at http://dataone.org.
#
#   Copyright ${year}
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#
# DataONE Architecture documentation build configuration file, created by
# sphinx-quickstart on Sun Nov  8 12:43:25 2009.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

sys.path.append(os.path.abspath("../api_template"))

# from docutils.parsers.rst import directives
# import plantuml
# directives.register_directive('uml', plantuml.UmlDirective)

from sqltable import SQLTable
from docutils.parsers.rst import directives
directives.register_directive("sqltable", SQLTable)

# -- General configuration -----------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.todo",
    "sphinx.ext.mathjax",
    "sphinx.ext.ifconfig",
    "sphinx.ext.graphviz",
    #'rst2pdf.pdfbuilder',
    "sphinx.ext.todo",
    #'sphinx.ext.inheritance_diagram',
    "sphinx.ext.extlinks",
    #'sphinxcontrib.httpdomain',
    #"sphinxcontrib.plantuml",
    "plantweb.directive",
    "sphinx.ext.napoleon",
]

images_config = {"override_image_directive": True, "default_image_width": "auto"}

#
extlinks = {
    "history": (
        "https://redmine.dataone.org/projects/d1/repository/changes/documents/Projects/cicore/architecture/api-documentation/source/%s",
        "history: ",
    )
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# Napoleon settings
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_admonition_for_hints = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True

# prolog, inserted at start of every file.
rst_prolog = """
"""

#plantuml = 'java -jar "' + os.path.abspath("../tools/docutils/plantuml.jar") + '"'
# plantuml += " -config " + os.path.abspath('../tools/docutils/plantuml.conf')

# Full path to the plantuml jar file.
# plantumljar = os.path.abspath('../tools/docutils/plantuml.jar')

# Full path to the plantuml configuration file
# plantumlconf = os.path.abspath('../tools/docutils/plantuml.conf')

# Full set of argument for executing plantuml expressed as a list. Note that java must be on your path
# plantuml = ['java', '-jar', plantumljar, '-config', plantumlconf]

# The suffix of source filenames.
source_suffix = ".txt"

# The encoding of source files.
# source_encoding = 'utf-8'

# The master toctree document.
master_doc = "index"

# General information about the project.
project = u""  # u'DataONE Architecture'
copyright = u"2009-2019, DataONE"
# copyright = u'''- INTEROP: Creation of an International Virtual Data Center for the Biodiversity,
# Ecological and Environmental Sciences (NSF Award 0753138);
#
# - DataNet Full Proposal: DataNetONE (Observation Network for Earth) (NSF Award 0830944)'''

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#

previous_version = "2.0.0"
# The short X.Y version.
version = "2.2"
# The full version, including alpha/beta/rc tags.
release = "2.2.0"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
# language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = '2010-April-04'
# Else, today_fmt is used as the format for a strftime call.
today_fmt = "%Y-%m-%d"

# List of documents that shouldn't be included in the build.
unused_docs = [
    "design/UseCases/uc_template",
    "design/usecasesoverview",
    "apis/types_auth",
    "apis/types_errors",
    "apis/Types_include.txt",
    "design/SearchMetadata",
]

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
exclude_trees = ["apis/generated", "apis/examples"]

exclude_patterns = [
    #                    'design/userscenarios*',
    #                    'design/Auth*',
    #                    'design/Data*',
    #                    'design/logging*',
    #                    'design/Logging*',
    #                    'design/NodeList*',
]
exclude_patterns = [
    "**/.svn",
    "apis/generated/generated*",
    #"apis/examples/*",
    "apis/Types_crontabentry.txt",
    "apis/Types_SAML.txt",
    "apis/Types_include.txt",
    "apis/types_errors.txt",
    "design/morpho/*",
]

# The reST default role (used for this markup: `text`) to use for all documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = True

mathjax_path = "//cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-MML-AM_CHTML"
# TeX-AMS-MML_HTMLorMML


# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

todo_include_todos = True

# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  Major themes that come with
# Sphinx are currently 'default' and 'sphinxdoc'.
# html_theme = 'default'
html_theme = "dataone_sans"
#html_theme = 'dataone'

# import sphinx_rtd_theme
#html_theme = 'sphinx_rtd_theme'
# html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
# html_theme_options = {'collapsiblesidebar':'true'}
html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = []
html_theme_path = ["themes"]

html_css_files = [
    'custom.css',
]

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = "v" + release

# A shorter title for the navigation bar.  Default is the same as html_title.
html_short_title = ""

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "_static/dataone_logo.png"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
# html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = "%Y-%b-%d"

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_use_modindex = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = ''

# Output file base name for HTML help builder.
htmlhelp_basename = "DataONEArchitecturedoc"

# previous_version points to the previous RELEASED version of the documents
# current version providesthe current version tag of the documents
# if is_development, then a warning is posted at the top of each page.
# otherwise a link to the previous version is placed in the footer.
# purl_path is path on purl.dataone.org that points to previous version docs parent folder
html_context = {
    "previous_version": previous_version,
    "current_version": release,
    "is_development": False,
    "purl_path": "/docs/api/",
    "current_version_URL": "https://purl.dataone.org/architecture",
}

# -- Options for PDF output  --------------------------------------------------

pdf_documents = [("index", u"dataone_arch", u"", u"DataONE")]

# A comma-separated list of custom stylesheets.
# Example: pdf_stylesheets = ['sphinx','kerning','a4']
pdf_stylesheets = ["murphy", "serif", "letter"]

# Create a compressed PDF # Use True/False or 1/0
# Example: compressed=True #pdf_compressed = False

# A colon-separated list of folders to search for fonts. Example:
# pdf_font_path = ['/usr/share/fonts', '/usr/share/texmf-dist/fonts/']

# Language to be used for hyphenation support
pdf_language = "en_US"

# Mode for literal blocks wider than the frame. Can be
# overflow, shrink or truncate
pdf_fit_mode = "shrink"

# Section level that forces a break page.
# For example: 1 means top-level sections start in a new page
# 0 means disabled #pdf_break_level = 0

# When a section starts in a new page, force it to be 'even', 'odd',
# or just use 'any'
# pdf_breakside = 'any'

# Insert footnotes where they are defined instead of
# at the end.
# pdf_inline_footnotes = True

# verbosity level. 0 1 or 2
# pdf_verbosity = 0

# If false, no index is generated.
pdf_use_index = True

# If false, no modindex is generated.
pdf_use_modindex = True

# If false, no coverpage is generated.
pdf_use_coverpage = True

# Name of the cover page template to use
# pdf_cover_template = 'sphinxcover.tmpl'

# Documents to append as an appendix to all manuals.
# pdf_appendices = []

# Enable experimental feature to split table cells. Use it
# if you get "DelayedTable too big" errors
# pdf_splittables = False

# Set the default DPI for images
pdf_default_dpi = 300

# Enable rst2pdf extension modules (default is empty list)
# you need vectorpdf for better sphinx's graphviz support
# pdf_extensions = ['vectorpdf']

# Page template name for "regular" pages
pdf_page_template = "cutePage"

# pdf_documents = [
#  ('index', 'DataONEArchitecture_0_0_4', u'DataONE Architecture Documentation',
#   u'VDC Project, DataONE CCIT', 'manual'),
#  #('MN_APIs_v0_3', 'MN_APIs_v0_3', u'MN API 0.3',
#  #u'VDC Project, DataONE CCIT', 'manual'),
# ]
# pdf_default_dpi = 400
# pdf_stylesheets = ['sphinx', ]

# pdf_fit_mode = "shrink"

# pdf_break_level = 1

# pdf_breakside = 'any'

# pdf_use_index = True

# pdf_use_modindex = True

# pdf_use_coverpage = False

# pdf_splittables = False

# pdf_page_template = 'cutePage'


# -- Options for LaTeX output --------------------------------------------------

# The paper size ('letter' or 'a4').
latex_paper_size = "letter"

# The font size ('10pt', '11pt' or '12pt').
latex_font_size = "10pt"

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
dv_latex_author = u"""Produced by:\\\\INTEROP: Creation of an International Virtual Data Center for the Biodiversity,
Ecological and Environmental Sciences (NSF Award 0753138)\\\\and\\\\DataNet Full Proposal: DataNetONE (Observation Network for Earth) (NSF Award 0830944)"""
latex_documents = [
    ("index", "DataONEArchitecture.tex", project, dv_latex_author, "manual")
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
# latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = True
latex_use_parts = False

# Additional stuff for the LaTeX preamble.
latex_preamble = "\\usepackage{pdflscape}"

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_use_modindex = True


# -- Options for Epub output ---------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = dv_latex_author
epub_publisher = u"DataONE.org"
epub_copyright = copyright

# The language of the text. It defaults to the language option
# or en if the language is not set.
# epub_language = ''

# The scheme of the identifier. Typical schemes are ISBN or URL.
# epub_scheme = ''

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
# epub_identifier = ''

# A unique identification for the text.
# epub_uid = ''

# HTML files that should be inserted before the pages created by sphinx.
# The format is a list of tuples containing the path and title.
# epub_pre_files = []

# HTML files shat should be inserted after the pages created by sphinx.
# The format is a list of tuples containing the path and title.
# epub_post_files = []

# A list of files that should not be packed into the epub file.
# epub_exclude_files = []

# The depth of the table of contents in toc.ncx.
# epub_tocdepth = 3

autoclass_content = 'both'

# try to exclude deprecated
def skip_deprecated(app, what, name, obj, skip, options):
    if hasattr(obj, "func_dict") and "__deprecated__" in obj.func_dict:
        print("skipping " + name)
        return True
    return skip or False

def setup(app):
    app.connect('autodoc-skip-member', skip_deprecated)
    try:

        from docutils.statemachine import StringList
        from sphinx.pycode import ModuleAnalyzer, PycodeError
        from sphinx.ext.autosummary import Autosummary
        from sphinx.ext.autosummary import get_documenter
        from docutils.parsers.rst import directives
        from sphinx.util.inspect import safe_getattr
        import re

        class AutoFuncSummary(Autosummary):
            """
            Based on https://github.com/markovmodel/PyEMMA/blob/devel/doc/source/conf.py

            Use it like::

              .. autofuncsummary:: MODULE_NAME
                 :functions:

            to generate a table of functions in a module.
            """

            #option_spec = {
            #    'functions': directives.unchanged,
            #}
            option_spec = Autosummary.option_spec
            option_spec["functions"] = directives.unchanged

            required_arguments = 1

            @staticmethod
            def get_members(obj, typ, include_public=None):
                if not include_public:
                    include_public = []
                items = []
                for name in dir(obj):
                    try:
                        documenter = get_documenter(app, safe_getattr(obj, name), obj)
                        #print(str(documenter))
                    except AttributeError:
                        continue
                    if documenter.objtype == typ:
                        items.append(name)
                public = [x for x in items if x in include_public or not x.startswith('_')]
                return public, items

            def run(self):
                module_name = self.arguments[0]
                try:
                    m = __import__(module_name, globals(), locals(), [])
                    if 'functions' in self.options:
                        _, methods = self.get_members(m, 'function', ['__init__'])
                        self.content = ["~%s.%s" % (module_name, method) for method in methods if not method.startswith('_')]
                finally:
                    return super(AutoFuncSummary, self).run()


        app.add_directive('autofuncsummary', AutoFuncSummary)
    except BaseException as e:
        raise e
