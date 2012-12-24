#!/usr/bin/env python 
# -*- coding: utf-8 -*-

"""Tests for tests!

More for checking compatability with Python versions than that the tests do
what you would expect. We check both the positive and negative versions of all
assertions (i.e.: in situations where we would expect them to pass and fail) in
the hope of getting the broadest code coverage.

"""
from __future__ import with_statement

import re
import unittest

from datetime import datetime

from testy.assertions import (
    assert_raises, assert_raises_and_contains, assert_equal,
    assert_almost_equal, assert_within_tolerance, assert_not_equal, assert_lt,
    assert_lte, assert_gt, assert_gte, assert_in_range, assert_between,
    assert_in, assert_not_in, assert_all_in, assert_starts_with,
    assert_not_reached, assert_rows_equal, assert_length,
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

    def test_assert_in(self):
        assert_in(2, [1,2,3])
        assert_in('b', 'abc')

    def test_assert_not_in(self):
        assert_not_in(1, [2,3,4])
        assert_not_in('a', 'bcd')

    def test_assert_all_in(self):
        assert_all_in([2,3,4], [1,2,3,4,5,6])
        assert_all_in('bc1', 'abc123')

    def test_assert_starts_with(self):
        assert_starts_with([1,2,3,4,5,6], [1,2,3])
        assert_starts_with('abcdef', 'abc')

    def test_assert_not_reached(self):
        try:
            assert_not_reached()
        except AssertionError:
            pass

    def test_assert_rows_equal(self):
        row1 = dict(a=1, b=2)
        row2 = dict(b=2, a=1)
        assert_rows_equal([row1, row2], [row2, row1])

    def test_assert_length(self):
        assert_length('abc', 3)

    def test_assert_is(self):
        x = 3
        y = x
        assert_is(x, y)

        x = 300
        assert_is(x, 300)

        assert_is(None, None)

        from testy.aliases import eq
        assert_is(eq, assert_equal)

    def test_assert_is_not(self):
        assert_is_not(assert_is, assert_is_not)
        assert_is_not('abc', list('abc'))

        l = [1, 2, 3]
        assert_is_not(l, l[:])

    def test_assert_all_match_regex(self):
        values = [
            'abc',
            '123 abc def',
        ]
        pattern = re.compile(r'\w+')
        assert_all_match_regex(pattern, values)

    def test_assert_match_regex(self):
        pattern = re.compile(r'\w+')
        assert_match_regex(pattern, 'abc 123')

    def test_assert_any_match_regex(self):
        values = [
            '"$',
            'abc',
            '@#~',
        ]
        pattern = re.compile(r'\w+')
        assert_any_match_regex(pattern, values)

    def test_assert_all_not_match_regex(self):
        values = [
            '"$',
            '@#~',
        ]
        pattern = re.compile(r'\w+')
        assert_all_not_match_regex(pattern, values)

    def test_assert_sets_equal(self):
        s1 = set(['a', 'b', 'c', 1, 2, 3])
        s2 = set([1, 'a', 3, 'b', 'c', 2])
        assert_sets_equal(s1, s2)

    def test_assert_dicts_equal(self):
        d1 = dict(a=3, b=True, c=None)
        d2 = dict(b=True, c=None, a=3)
        assert_dicts_equal(d1, d2)

    def test_assert_dict_subset(self):
        d1 = dict(b=True)
        d2 = dict(a=3, b=True, c=None)
        assert_dict_subset(d1, d2)

    def test_assert_subset(self):
        s1 = set([3, 'b', 'c', 2])
        s2 = set(['a', 'b', 'c', 1, 2, 3])
        assert_subset(s1, s2)

    def test_assert_list_prefix(self):
        l1 = [1, 2, 3]
        l2 = [1, 2, 3, 'a', 'b', 'c']
        assert_list_prefix(l1, l2)

    def test_assert_sorted_equal(self):
        s1 = set(['a', 'b', 'c'])
        s2 = set(['b', 'c', 'a'])
        assert_sorted_equal(s1, s2)

    def test_assert_isinstance(self):
        class A(object):
            pass
        assert_isinstance(A(), A)
        assert_isinstance(dict(a=1), dict)

    def test_assert_datetimes_equal(self):
        # times are compared to the millisecond, so this ought to pass
        t0 = datetime.now()
        t1 = datetime.now()
        assert_datetimes_equal(t0, t1)

        t0 = datetime(1970, 1, 1)
        t1 = datetime(1970, 1, 1)
        assert_datetimes_equal(t0, t1)

    def test_assert_exactly_one(self):
        assert_exactly_one(None, False, None, None)
        assert_exactly_one(None, True, None, None)


class NegativeAssertionsTestCase(unittest.TestCase):
    """Test all assertions with the expectation of them all failing."""
    def test_assert_raises(self):
        class MyException(Exception):
            pass

        with assert_raises(AssertionError):
            with assert_raises(TypeError):
                raise MyException()

    def test_assert_raises_and_contains(self):
        def fail():
            raise ValueError("choose one of the correct values")

        with assert_raises(AssertionError):
            assert_raises_and_contains(ValueError, "two of", fail)

    def test_assert_equal(self):
        with assert_raises(AssertionError):
            assert_equal(1, 2)

    def test_assert_almost_equal(self):
        with assert_raises(AssertionError):
            assert_almost_equal(1, 1.01, 2)

    def test_assert_within_tolerance(self):
        with assert_raises(AssertionError):
            assert_within_tolerance(5, 5.1, 0.01)

    def test_assert_not_equal(self):
        with assert_raises(AssertionError):
            assert_not_equal(1, 1)

    def test_assert_lt(self):
        with assert_raises(AssertionError):
            assert_lt(3, 2)

    def test_assert_lte(self):
        with assert_raises(AssertionError):
            assert_lte(10, 1)

    def test_assert_gt(self):
        with assert_raises(AssertionError):
            assert_gt(1, 4)

    def test_assert_gte(self):
        with assert_raises(AssertionError):
            assert_gte(3, 5)

    def test_assert_in_range(self):
        with assert_raises(AssertionError):
            assert_in_range(1, 2, 4)

    def test_assert_between(self):
        with assert_raises(AssertionError):
            assert_between(1, 3, 2)

    def test_assert_in(self):
        with assert_raises(AssertionError):
            assert_in('a', [1, 2, 3])

    def test_assert_not_in(self):
        with assert_raises(AssertionError):
            assert_not_in(1, [1, 2, 3])

    def test_assert_all_in(self):
        with assert_raises(AssertionError):
            assert_all_in([1, 2], [1, 3])

    def test_assert_starts_with(self):
        with assert_raises(AssertionError):
            assert_starts_with('abc123', 'bc')

    def test_assert_not_reached(self):
        # The only way to test this assertion negatively is to not reach it :)
        pass

    def test_assert_rows_equal(self):
        with assert_raises(AssertionError):
            row1 = dict(a=1, b=2)
            row2 = dict(b=3, a=1)
            row3 = dict(b=1, a=1)
            assert_rows_equal([row1, row2], [row2, row3])

    def test_assert_length(self):
        with assert_raises(AssertionError):
            assert_length('abc', 4)

    def test_assert_is(self):
        with assert_raises(AssertionError):
            assert_is(True, False)

    def test_assert_is_not(self):
        with assert_raises(AssertionError):
            assert_is_not(True, True)

    def test_assert_all_match_regex(self):
        with assert_raises(AssertionError):
            values = [
                '$%`',
                '123 abc def',
            ]
            pattern = re.compile(r'\w+')
            assert_all_match_regex(pattern, values)

    def test_assert_match_regex(self):
        with assert_raises(AssertionError):
            pattern = re.compile(r'\w+')
            assert_match_regex(pattern, '$')

    def test_assert_any_match_regex(self):
        with assert_raises(AssertionError):
            values = [
                '"$',
                '@#~',
            ]
            pattern = re.compile(r'\w+')
            assert_any_match_regex(pattern, values)

    def test_assert_all_not_match_regex(self):
        with assert_raises(AssertionError):
            values = [
                '"$',
                'abc',
                '@#~',
            ]
            pattern = re.compile(r'\w+')
            assert_all_not_match_regex(pattern, values)

    def test_assert_sets_equal(self):
        with assert_raises(AssertionError):
            assert_sets_equal(set([1, 2, 3]), set([1, 'b', 'c']))

    def test_assert_dicts_equal(self):
        with assert_raises(AssertionError):
            assert_dicts_equal(dict(a=1), dict(a=2))

    def test_assert_dict_subset(self):
        with assert_raises(AssertionError):
            assert_dict_subset(dict(a=2), dict(b=3))

    def test_assert_subset(self):
        with assert_raises(AssertionError):
            assert_subset(set([1, 2, 3]), set([1, 2]))

    def test_assert_list_prefix(self):
        with assert_raises(AssertionError):
            assert_list_prefix([1, 2, 3], [4, 5, 6])

    def test_assert_sorted_equal(self):
        with assert_raises(AssertionError):
            assert_sorted_equal([1, 2, 3], [3, 2, 3])

    def test_assert_isinstance(self):
        with assert_raises(AssertionError):
            assert_isinstance(dict(), list)

    def test_assert_datetimes_equal(self):
        with assert_raises(AssertionError):
            assert_datetimes_equal(datetime(1970, 1, 1), datetime.now())

    def test_assert_exactly_one(self):
        with assert_raises(AssertionError):
            assert_exactly_one(True, False, None, 1)


if __name__ == '__main__':
    unittest.main()
