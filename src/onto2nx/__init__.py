# -*- coding: utf-8 -*-

"""
onto2nx is a package for parsing ontologies in the OWL and OBO format into NetworkX graphs
for easy traversal of entity hierarchies
"""

from . import (aba, owl_rdf, owl_xml)
from .aba import *
from .owl_rdf import *
from .owl_xml import *

__all__ = (
    aba.__all__ +
    owl_rdf.__all__ +
    owl_xml.__all__
)

__version__ = '0.1.1-dev'

__title__ = 'onto2nx'
__description__ = "A package for parsing ontologies into NetworkX graphs"
__url__ = 'https://github.com/cthoyt/onto2nx'

__author__ = 'Charles Tapley Hoyt, Aliaksandr Masny'
__email__ = 'charles.hoyt@scai.fraunhofer.de'

__license__ = 'GPL 3.0 License'
__copyright__ = 'Copyright (c) 2016 Charles Tapley Hoyt'
