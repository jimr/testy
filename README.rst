=====
Testy
=====

.. image:: https://travis-ci.org/jimr/testy.png
    :target: http://travis-ci.org/jimr/testy

All the assertions from Testify_ but cleaned up a bit & with added py3k support.

.. _Testify: https://github.com/Yelp/Testify

Should work with Python 2.5-3.3 and pypy 1.9. To make sure it will work for you: ``python setup.py test``.


Installation
============

There are no dependencies. Simply: ``pip install testy``


Example Usage
=============

.. code-block:: python

    import re
    import unittest

    from testy.assertions import assert_dict_subset, assert_raises, assert_match_regex

    class MyTestCase(unittest.TestCase):
        def setUp(self):
            self.x = dict(a=1, b=2)

        def test_x(self):
            assert_dict_subset(dict(b=2), self.x)

        def test_exception(self):
            with assert_raises(TypeError):
                raise TypeError("Call some code you expect to fail here.")

        def test_pattern(self):
            pattern = re.compile('\w')
            assert_match_regex(pattern, 'abc')

        def tearDown(self):
            self.x = None

    if __name__ == "__main__":
        unittest.main()

