import unittest
import poly

class TestPoly(unittest.TestCase):

   def assertListAlmostEqual(self, l1, l2):
      self.assertEqual(len(l1), len(l2))
      for el1, el2 in zip(l1, l2):
         self.assertAlmostEqual(el1, el2)
   
   def test_poly(self):
      poly1 = [2.0, 4.0, 5.0]
      poly2 = [1.0, 2.0, 6.0]
      poly3 = poly.poly_add2(poly1, poly2)
      self.assertAlmostEqual(poly3, [3.0, 6.0, 11.0])

   def test_poly_1(self):
      poly1 = [1.0, 5.0, 1.0]
      poly2 = [1.0, 6.0, 2.0]
      self.assertListAlmostEqual(poly.poly_mult2(poly1, poly2), [1.0, 11.0, 34.0, 16.0, 2.0])
   # Add tests here

if __name__ == '__main__':
   unittest.main()
