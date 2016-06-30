#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_import_string
----------------------------------

Tests for `import_string` module.
"""

import pytest
from import_string.base import ImportStringError
import import_string


class TestImport_string(object):

    def test_import_module(self):
        assert import_string('os.path').join('.') == '.'

    def test_import_function(self):
        assert import_string('os.path:join')('.') == '.'

    def test_import_function_dotted(self):
        assert import_string('os.path.join')('.') == '.'

    def test_silent_errors(self):
        assert import_string('this_does.exist:at_all', silent=True) is None

    def test_raise_import_error(self):
        with pytest.raises(ImportStringError):
            import_string('this_does.exist:at_all')

        with pytest.raises(ImportError):
            import_string('this_does.exist:at_all_also')
