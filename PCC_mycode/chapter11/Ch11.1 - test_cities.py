import unittest

from city_functions import pair_city_country

class CityCountryTestCase(unittest.TestCase):
	"""Tests for 'city_functions.py'. """
	
	def test_city_country(self):
		"""Let's test it for 'montreal' 'canada'"""
		pair = pair_city_country('montreal','canada')
		self.assertEqual(pair, "Montreal Canada")

if __name__ == '__main__':
	unittest.main()
