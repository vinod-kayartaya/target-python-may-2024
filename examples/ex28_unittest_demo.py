from unittest import TestCase
from myutils import factorial


class FactorialTest(TestCase):

    def test_for_positive_input(self):
        want = 120
        got = factorial(5)
        self.assertEqual(want, got)

    def test_for_negative_input(self):
        want = 1
        got = factorial(-5)
        self.assertEqual(want, got)

    def test_for_non_numeric_input(self):
        def fn():
            factorial('asdf')
        self.assertRaises(TypeError, fn)

        # try:
        #     factorial('asdf')
        #     self.fail('expecting TypeError, did not get one')
        # except TypeError:
        #     pass
        # except Exception as err:
        #     self.fail(f'expecting TypeError, got {type(err)}')

