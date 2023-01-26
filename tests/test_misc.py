import toolkit as tk
from datetime import datetime
import unittest


class TestMisc(unittest.TestCase):

    def test_percent(self):
        self.assertEqual(tk.percent(0), '  0.00%')
        self.assertEqual(tk.percent(0.0314), '  3.14%')
        self.assertEqual(tk.percent(0.1234), ' 12.34%')
        self.assertEqual(tk.percent(0.0001), '  0.01%')
        self.assertEqual(tk.percent(1.56), '156.00%')
        self.assertEqual(tk.percent(0.01), '  1.00%')
        self.assertEqual(tk.percent(-0.01), ' -1.00%')

    def test_now(self):
        self.assertEqual(tk.now(), int(datetime.now().timestamp()))




if __name__ == '__main__': unittest.main()