#!/usr/bin/env python 
# -*- coding: utf-8 -*-

"""Tests for tests!

More for checking compatability with Python versions than that the tests do
what you would expect. We check both the positive and negative versions of all
assertions (i.e.: in situations where we would expect them to pass and fail) in
the hope of getting the broadest code coverage.

"""
from __future__ import with_statement

import unittest

from testy.assertions import (
    assert_raises, assert_raises_and_contains, assert_equal,
    assert_almost_equal, assert_within_tolerance, assert_not_equal, assert_lt,
    assert_lte, assert_gt, assert_gte, assert_in_range, assert_between,
    assert_in, assert_not_in, assert_all_in, assert_starts_with,
    assert_not_reached, assert_rows_equal, assert_length, assert_call,
    assert_is, assert_is_not, assert_all_match_regex, assert_match_regex,
    assert_any_match_regex, assert_all_not_match_regex, assert_sets_equal,
    assert_dicts_equal, assert_dict_subset, assert_subset, assert_list_prefix,
    assert_sorted_equal, assert_isinstance, assert_datetimes_equal,
    assert_exactly_one
)


class PositiveAssertionsTestCase(unittest.TestCase):
    """Test all assertions with the expectation of them all passing."""
    def test_assert_raises(self):
        with assert_raises(TypeError):
            raise TypeError()

        with assert_raises(Exception):
            raise TypeError()

    def test_assert_raises_and_contains(self):
        def fail():
            raise ValueError("choose one of the correct values")
        assert_raises_and_contains(ValueError, "one of", fail)

    def test_assert_equal(self):
        assert_equal(1, 1)
        assert_equal("abc", "abc")
        assert_equal(self, self)

    def test_assert_almost_equal(self):
        assert_almost_equal(1, 1, 1)
        assert_almost_equal(1, 1.01, 1)
        assert_almost_equal(0.99, 1, 1)
        assert_almost_equal(1, 1.001, 2)

    def test_assert_within_tolerance(self):
        assert_within_tolerance(5, 5.1, 0.2)

    def test_assert_not_equal(self):
        assert_not_equal(1, 2)

        class A(object):
            pass

        assert_not_equal(A(), A())

    def test_assert_lt(self):
        assert_lt(1, 2)
        assert_lt(1.0, 1.01)
        assert_lt('a', 'b')
        assert_lt(False, True)

    def test_assert_lte(self):
        assert_lte(1, 1)
        assert_lte(1, 2)
        assert_lte(1.0, 1.01)
        assert_lte('a', 'b')
        assert_lte(False, True)
        assert_lte(False, False)

    def test_assert_gt(self):
        assert_gt(2, 1)
        assert_gt(1.01, 1.0)
        assert_gt('b', 'a')
        assert_gt(True, False)

    def test_assert_gte(self):
        assert_gte(1, 1)
        assert_gte(2, 1)
        assert_gte(1.01, 1.0)
        assert_gte('b', 'a')
        assert_gte(True, False)
        assert_gte(False, False)

    def test_assert_in_range(self):
        assert_in_range(3, 1, 5)
        assert_in_range(3, 1, 3, inclusive=True)

    def test_assert_between(self):
        assert_between(1, 3, 5)
        assert_between(1, 3, 3)

#    def test_assert_in(self):
#        assert_in()
#
#    def test_assert_not_in(self):
#        assert_not_in()
#
#    def test_assert_all_in(self):
#        assert_all_in()
#
#    def test_assert_starts_with(self):
#        assert_starts_with()
#
#    def test_assert_not_reached(self):
#        assert_not_reached()
#
#    def test_assert_rows_equal(self):
#        assert_rows_equal()
#
#    def test_assert_length(self):
#        assert_length()
#
#    def test_assert_call(self):
#        assert_call()
#
#    def test_assert_is(self):
#        assert_is()
#
#    def test_assert_is_not(self):
#        assert_is_not()
#
#    def test_assert_all_match_regex(self):
#        assert_all_match_regex()
#
#    def test_assert_match_regex(self):
#        assert_match_regex()
#
#    def test_assert_any_match_regex(self):
#        assert_any_match_regex()
#
#    def test_assert_all_not_match_regex(self):
#        assert_all_not_match_regex()
#
#    def test_assert_sets_equal(self):
#        assert_sets_equal()
#
#    def test_assert_dicts_equal(self):
#        assert_dicts_equal()
#
#    def test_assert_dict_subset(self):
#        assert_dict_subset()
#
#    def test_assert_subset(self):
#        assert_subset()
#
#    def test_assert_list_prefix(self):
#        assert_list_prefix()
#
#    def test_assert_sorted_equal(self):
#        assert_sorted_equal()
#
#    def test_assert_isinstance(self):
#        assert_isinstance()
#
#    def test_assert_datetimes_equal(self):
#        assert_datetimes_equal()
#
#    def test_assert_exactly_one(self):
#        assert_exactly_one()


class NegativeAssertionsTestCase(unittest.TestCase):
    """Test all assertions with the expectation of them all failing."""
    def test_assert_raises(self):
        class MyException(Exception):
            pass

        try:
            with assert_raises(TypeError):
                raise MyException()
        except MyException:
            pass

    def test_assert_raises_and_contains(self):
        def fail():
            raise ValueError("choose one of the correct values")

        try:
            assert_raises_and_contains(ValueError, "one of", fail)
        except AssertionError:
            pass

    def test_assert_equal(self):
        try:
            assert_equal(1, 1)
        except AssertionError:
            pass

    def test_assert_almost_equal(self):
        try:
            assert_almost_equal(1, 1.01, 2)
        except AssertionError:
            pass

    def test_assert_within_tolerance(self):
        try:
            assert_within_tolerance(5, 5.1, 0.01)
        except AssertionError:
            pass

#    def test_assert_not_equal(self):
#        try:
#            assert_not_equal()
#        except AssertionError:
#            pass
#
#    def test_assert_lt(self):
#        try:
#            assert_lt()
#        except AssertionError:
#            pass
#
#    def test_assert_lte(self):
#        try:
#            assert_lte()
#        except AssertionError:
#            pass
#
#    def test_assert_gt(self):
#        try:
#            assert_gt()
#        except AssertionError:
#            pass
#
#    def test_assert_gte(self):
#        try:
#            assert_gte()
#        except AssertionError:
#            pass
#
#    def test_assert_in_range(self):
#        try:
#            assert_in_range()
#        except AssertionError:
#            pass
#
#    def test_assert_between(self):
#        try:
#            assert_between()
#        except AssertionError:
#            pass
#
#    def test_assert_in(self):
#        try:
#            assert_in()
#        except AssertionError:
#            pass
#
#    def test_assert_not_in(self):
#        try:
#            assert_not_in()
#        except AssertionError:
#            pass
#
#    def test_assert_all_in(self):
#        try:
#            assert_all_in()
#        except AssertionError:
#            pass
#
#    def test_assert_starts_with(self):
#        try:
#            assert_starts_with()
#        except AssertionError:
#            pass
#
#    def test_assert_not_reached(self):
#        try:
#            assert_not_reached()
#        except AssertionError:
#            pass
#
#    def test_assert_rows_equal(self):
#        try:
#            assert_rows_equal()
#        except AssertionError:
#            pass
#
#    def test_assert_length(self):
#        try:
#            assert_length()
#        except AssertionError:
#            pass
#
#    def test_assert_call(self):
#        try:
#            assert_call()
#        except AssertionError:
#            pass
#
#    def test_assert_is(self):
#        try:
#            assert_is()
#        except AssertionError:
#            pass
#
#    def test_assert_is_not(self):
#        try:
#            assert_is_not()
#        except AssertionError:
#            pass
#
#    def test_assert_all_match_regex(self):
#        try:
#            assert_all_match_regex()
#        except AssertionError:
#            pass
#
#    def test_assert_match_regex(self):
#        try:
#            assert_match_regex()
#        except AssertionError:
#            pass
#
#    def test_assert_any_match_regex(self):
#        try:
#            assert_any_match_regex()
#        except AssertionError:
#            pass
#
#    def test_assert_all_not_match_regex(self):
#        try:
#            assert_all_not_match_regex()
#        except AssertionError:
#            pass
#
#    def test_assert_sets_equal(self):
#        try:
#            assert_sets_equal()
#        except AssertionError:
#            pass
#
#    def test_assert_dicts_equal(self):
#        try:
#            assert_dicts_equal()
#        except AssertionError:
#            pass
#
#    def test_assert_dict_subset(self):
#        try:
#            assert_dict_subset()
#        except AssertionError:
#            pass
#
#    def test_assert_subset(self):
#        try:
#            assert_subset()
#        except AssertionError:
#            pass
#
#    def test_assert_list_prefix(self):
#        try:
#            assert_list_prefix()
#        except AssertionError:
#            pass
#
#    def test_assert_sorted_equal(self):
#        try:
#            assert_sorted_equal()
#        except AssertionError:
#            pass
#
#    def test_assert_isinstance(self):
#        try:
#            assert_isinstance()
#        except AssertionError:
#            pass
#
#    def test_assert_datetimes_equal(self):
#        try:
#            assert_datetimes_equal()
#        except AssertionError:
#            pass
#
#    def test_assert_exactly_one(self):
#        try:
#            assert_exactly_one()
#        except AssertionError:
#            pass


if __name__ == '__main__':
    unittest.main()
