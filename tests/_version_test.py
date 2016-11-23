
'''
unit testing of pyRestTable._version module
'''

import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from pyRestTable._version import git_release


class TestGitRelease(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass

    def test_git_release_package_exception(self):
        self.assertEqual('release_undefined', git_release('not_the_package_name'))


if __name__ == '__main__':
    unittest.main()
