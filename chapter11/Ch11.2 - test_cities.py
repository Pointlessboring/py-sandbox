import unittest

from city_functions_v2 import pair_city_country

class CityCountryTestCase(unittest.TestCase):
	"""Tests for 'city_functions.py'. """
	
	def test_city_country(self):
		"""Let's test it for 'montreal' 'canada'"""
		pair = pair_city_country('montreal','canada', 1000000)
		self.assertEqual(pair, "Montreal, Canada - population 1000000")

if __name__ == '__main__':
	unittest.main()
