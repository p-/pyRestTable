# -*- coding: iso-8859-1 -*-

#-----------------------------------------------------------------------------
# :author:    Pete R. Jemian
# :email:     prjemian@gmail.com
# :copyright: (c) 2014-2017, Pete R. Jemian
#
# Distributed under the terms of the Creative Commons Attribution 4.0 International Public License.
#
# The full license is in the file LICENSE.txt, distributed with this software.
#-----------------------------------------------------------------------------

import os
from . import rest_table
Table = rest_table.Table    # shorten the import trail

from ._version import get_versions
_vdict_ = get_versions()
__version__ = _vdict_['version']
__release__ = __version__ + '<' + _vdict_['date'] + '>'
del get_versions, _vdict_

__package_name__ = 'pyRestTable'

_path = os.path.dirname(__file__)

__author__ = 'Pete R. Jemian'
__email__ = 'prjemian@gmail.com'
__copyright_year__ = '2014-2017'
__copyright__ = __copyright_year__ + ', Pete R. Jemian'

__license_url__ = 'http://creativecommons.org/licenses/by/4.0/deed.en_US'
__license__ = 'Creative Commons Attribution 4.0 International Public License (see LICENSE file)'
__description__ = 'Format a nice table in reST (reStructuredText ) from Python'
__author_name__ = __author__
__author_email__ = __email__
__url__ = 'http://pyRestTable.readthedocs.io'
__download_url__ = 'https://github.com/prjemian/pyRestTable/tarball/' + __version__
__keywords__ = ['reST', 'table', 'documentation']
__platforms__ = 'any'
__zip_safe__ = True

__classifiers__ = [
     'Development Status :: 6 - Mature',
     'Environment :: Console',
     'Intended Audience :: Developers',
     'License :: Freely Distributable',
     'License :: Public Domain',
     'Programming Language :: Python',
     'Programming Language :: Python :: 2',
     'Programming Language :: Python :: 2.7',
     'Programming Language :: Python :: 3',
     'Programming Language :: Python :: 3.5',
     'Topic :: Documentation',
     'Topic :: Documentation :: Sphinx',
     'Topic :: Software Development',
     'Topic :: Software Development :: Documentation',
     'Topic :: Text Processing :: Markup',
     'Topic :: Utilities',
   ]

