# test_report_generator.py

import unittest
import os
from report_generator import generate_asset_report

class TestReportGenerator(unittest.TestCase):

    def test_generate_report(self):
        generate_asset_report()
        self.assertTrue(os.path.exists('asset_report.csv'))

if __name__ == '__main__':
    unittest.main()