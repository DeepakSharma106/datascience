

import unittest
from Employee import Employee

class TestEmployee(unittest.TestCase):

	def setUp(self):
		print('setUp')
		self.e1 = Employee('deepak','sharma', 5000)
		self.e2 = Employee('kanishk','sharma', 6000)

	def tearDown(self):
		print('tearDown')



	def test_email(self):
		print('test_email')
		self.assertEqual(self.e1.email, 'deepak.sharma@email.com')
		self.assertEqual(self.e2.email, 'kanishk.sharma@email.com')

		self.e1.first = 'John'
		self.e2.first = 'Jane'

		self.assertEqual(self.e1.email, 'John.sharma@email.com')
		self.assertEqual(self.e2.email, 'Jane.sharma@email.com')


if __name__ == '__main__':
	unittest.main()
