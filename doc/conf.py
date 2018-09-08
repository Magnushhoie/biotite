# This source code is part of the Biotite package and is distributed
# under the 3-Clause BSD License. Please see 'LICENSE.rst' for further
# information.

__author__ = "Patrick Kunzmann"

import pyximport
import numpy as np
pyximport.install(setup_args={'include_dirs': np.get_include()})

from os.path import realpath, dirname, join, basename
from os import listdir, makedirs
import sys
import glob
import shutil
import types
import matplotlib

doc_path = dirname(realpath(__file__))

# Include biotite/doc in PYTHONPATH
# in order to import modules for API doc generation etc.
sys.path.insert(0, doc_path)
import apidoc

# Include biotite/src in PYTHONPATH
# in order to import the 'biotite' package
package_path = join(dirname(doc_path), "src")
sys.path.insert(0, package_path)
import biotite



#Reset matplotlib params
matplotlib.rcdefaults()

# Creation of API documentation
apidoc.create_api_doc(package_path, join(doc_path, "apidoc"))


#### General ####

extensions = ["sphinx.ext.autodoc",
              "sphinx.ext.autosummary",
              "sphinx.ext.doctest",
              "sphinx.ext.mathjax",
              "sphinx.ext.viewcode",
              "sphinx_gallery.gen_gallery",
              "numpydoc"]

templates_path = ["templates"]
source_suffix = [".rst"]
master_doc = "index"

project = "Biotite"
copyright = "2017-2018, the Biotite contributors"
version = biotite.__version__

exclude_patterns = ["build"]

pygments_style = "sphinx"

todo_include_todos = False

# Prevents numpydoc from creating an autosummary which does not work
# due to Biotite's import system
numpydoc_show_class_members = False


#### HTML ####

html_theme = "alabaster"
html_static_path = ["static"]
html_favicon = "static/assets/general/biotite_icon_32p.png"
htmlhelp_basename = "BiotiteDoc"
html_sidebars = {"**": ["about.html",
                        "navigation.html",
                        "searchbox.html",
                        "buttons.html"]}
html_theme_options = {
    "description"   : "A comprehensive framework for " \
                      "computational molecular biology",
    "logo"          : "assets/general/biotite_logo_s.png",
    "logo_name"     : "false",
    "github_user"   : "biotite-dev",
    "github_repo"   : "biotite",
    "github_banner" : "true",
    "page_width"    : "85%",
    "fixed_sidebar" : "true",
    
    "sidebar_link_underscore" : "#FFFFFF"
}

sphinx_gallery_conf = {
    "examples_dirs"             : "examples/scripts",
    "gallery_dirs"              : "examples/gallery",
    "filename_pattern"          : "/",
    "backreferences_dir"        : False,
    "download_section_examples" : False,
    # Never report run time
    "min_reported_time"         : sys.maxsize,
    "default_thumb_file"        : join(
        doc_path, "static/assets/general/biotite_icon_thumb.png"
    )
}


#### App setup ####

# Skip all class members, that are not methods,
# since other attributes are already documented in the class docstring
def maybe_skip_member(app, what, name, obj, skip, options):
    if what == "class":
        if type(obj) not in [types.FunctionType, types.BuiltinFunctionType]:
            return True

def setup(app):
    app.connect('autodoc-skip-member', maybe_skip_member)