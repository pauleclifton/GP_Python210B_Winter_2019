import mock

import unittest
import target_code

class SampleTest(unittest.TestCase):
    @mock.patch('target_code.input', mock.Mock(return_value = '54'))
    def test_correct_input(self):
        self.assertEqual(target_code.get_value('Enter a value:', int), 54)

    @mock.patch('target_code.input', mock.Mock(return_value = 'Hello World'))
    def test_wrong_input(self):
        self.assertEqual(target_code.get_value('Enter a value:', int), 'Invalid value.  Please try again')
