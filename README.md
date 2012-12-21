# Testy

All the assertions from [Testify](https://github.com/Yelp/Testify) but with py3k support.

The only requirement is `six` (for combined Python 2.x & 3.x support):
    
    pip install -r requirements.txt


### Example Usage

```python
import re
import unittest

from testy.assertions import assert_equal, assert_raises, assert_matches_regex

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.x = 1

    def test_x(self):
        assert_equal(self.x, 1)

    def test_exception(self):
        with assert_raises(TypeError):
            raise TypeError("Call some code you expect to fail here.")

    def test_pattern(self):
        pattern = re.compile('\w')
        assert_matches_regex(pattern, 'abc')

    def tearDown(self):
        self.x = None


if __name__ == "__main__":
    unittest.main()
```
