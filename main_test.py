from datetime import date
import unittest

from model.person import *

class TestPerson(unittest.TestCase):

	def test_invalid_creation(self):
		with self.assertRaises(Exception) as context:
			Person('Matt','30/12/2022','10/10/2021')

		self.assertTrue('El egreso no puede ser anterior al ingreso' in str(context.exception))

	def test_valid_creation(self):
		name = 'Matt'
		date1 = '30/12/2018'
		date2 = '10/10/2021'
		p = Person(name,date1,date2)
		self.assertIsInstance(p, Person)
		self.assertEqual(p.name, name)
		self.assertEqual(p.ingreso,date1)
		self.assertEqual(p.salida,date2)
		self.assertEqual(p.saldo,0,"this should be zero")


	def test_sum_saldo(self):
		p = Person('Matt','30/12/2018','10/10/2021')
		p.addExpense(30)
		self.assertEqual(p.saldo,30)
		p.addExpense(10)
		self.assertEqual(p.saldo,40)


if __name__ == '__main__':
	unittest.main()