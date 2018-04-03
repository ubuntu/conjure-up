#!/usr/bin/env python
#
# tests bundle loading, merging, output
#
# Copyright 2016-2018 Canonical, Ltd.


import argparse
import unittest
from pathlib import Path

from conjureup.models.conjurefile import Conjurefile


class ConjurefileTestCase(unittest.TestCase):

    def setUp(self):
        self.tests_dir = Path(__file__).absolute().parent
        self.conjurefile_path = self.tests_dir / 'Conjurefile'
        self.conjurefile = Conjurefile.load(self.conjurefile_path)

    def test_conjurefile_argv_override(self):
        "conjurefile.test_argv_override"
        args = argparse.Namespace()
        args.registry = 'https://github.com/conjure-up/spells.git'
        assert self.conjurefile['registry'] == (
            'https://github.com/battlemidget/spells.git')
        self.conjurefile.merge_argv(args)
        assert self.conjurefile['registry'] == (
            'https://github.com/conjure-up/spells.git')