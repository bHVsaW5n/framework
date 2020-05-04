import unittest

import unittest
from HTMLTestRunner import HTMLTestRunner
from service.test_service import test_service


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        a, b = 2, 3
        response = {'a': 2, 'b': 3}
        self.assertEqual(response, test_service.add(a, b))

    def test_isupper(self):
        a, b = 2, 3
        response = {'a': 3, 'b': 3}
        self.assertEqual(response, test_service.add(a, b))

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestStringMethods))

    with open('HTMLReport.html', 'w') as f:
        runner = HTMLTestRunner(stream=f,
                                title='MathFunc Test Report',
                                description='generated by HTMLTestRunner.',
                                verbosity=2
                                )
        runner.run(suite)