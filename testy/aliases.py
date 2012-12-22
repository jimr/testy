#!/usr/bin/env python 
# -*- coding: utf-8 -*-
"""Some abbreviated shortcuts to common assertions.

For particularly lazy people who would rather type::

    import testy as t
    with t.raises(AssertionError):
        t.lt(3, 2)

than::

    from testy.assertions import assert_raises, assert_lt
    with assert_raises(AssertionError):
        assert_lt(3, 2)

"""

from __future__ import absolute_import

from .assertions import *

raises = assert_raises
eq = assert_equal
equals = eq
equal = eq
ne = assert_not_equal
not_equal = ne
lt = assert_lt
lte = assert_lte
gt = assert_gt
gte = assert_gte
in_range = assert_in_range
between = in_range
in_seq = assert_in
not_in_seq = assert_not_in
not_in = not_in_seq
all_in = assert_all_in
regex = assert_match_regex
