"""
Test File to test functions Date Arithmetic, File Reader, File Analyzer
"""

import unittest
from HW08_Yash_Navadiya import date_arithmetic, file_reader, FileAnalyzer
import os


class testFuctions(unittest.TestCase):
    """To Implement the different test cases
    """

    def test_date_arithmetic(self) -> None:
        """Test the date arthimetic"""
        self.assertEqual(date_arithmetic(), ('The date three days after Feb 27, 2020 is Mar 01, 2020',
                                             'The date three days after Feb 27, 2019 is Mar 02, 2019', '241 days passed between Feb 01, 2019 and Sep 30, 2019'))

    def test_file_reader(self) -> None:
        """ Test the file reader"""
        expected = [('123', 'Jin He', 'Computer Science'), ('234', 'Nanda Koka',
                                                            'Software Engineering'), ('345', 'Benji Cai', 'Software Engineering')]
        self.assertEqual(list(file_reader(
            'D:\yash\Stevens\SEM 3\SSW 810\Week 8\HW08_Test.txt', 3, '|', True)), expected)
        self.assertNotEqual(list(file_reader(
            'D:\yash\Stevens\SEM 3\SSW 810\Week 8\HW08_Test.txt', 3, '|')), expected)
        with self.assertRaises(ValueError):
            list(file_reader(
                'D:\yash\Stevens\SEM 3\SSW 810\Week 8\HW08_Test.txt', 4, '|', True))
        with self.assertRaises(FileNotFoundError):
            list(file_reader('HW08_Test1.txt', 3, '|', True))

    def test_file_analyzer(self) -> None:
        """ Test the file analyzer """
        test = FileAnalyzer('HW08_Test')
        expected = {'0_p.py': {'classes': 0, 'functions': 0, 'lines': 4, 'characters': 59},
                    'file1.py': {'classes': 2, 'functions': 4, 'lines': 25, 'characters': 269}}
        self.assertEqual(test.files_summary, expected)
        with self.assertRaises(FileNotFoundError):
            FileAnalyzer(' ')


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
