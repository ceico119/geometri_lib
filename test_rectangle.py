import unittest as t
from rectangle import area
from rectangle import perimeter


class RectangleTestCase(t.TestCase):
    def test_negative_mul_positive(self):
        res = area(-3, 3)
        self.assertEqual(res, None)

    def test_zero_mul_x(self):
        res = area(0, 3)
        self.assertEqual(res, 0)

    def test_float_mul_x(self):
        res = area(4.5, 4)
        self.assertEqual(res, 18)

    def test_negative_and_positive(self):
        res = perimeter(-13, 12)
        self.assertEqual(res, None)

    def test_zero_and_zero(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0)

    def test_float_and_float(self):
        res = perimeter(4.5, 4.5)
        self.assertEqual(res, 18)