"""Function for Date Arithmetic Operations, Organize the file and Scanning directories and files"""

import os
import csv
from datetime import datetime, timedelta
from prettytable import PrettyTable
from typing import List, Iterator, Tuple, Dict


def date_arithmetic() -> Tuple[datetime, datetime, int]:
    """Function to perform Date Arithmetic Operations"""
    d1: str = 'Feb 27, 2020'
    d2: str = 'Feb 27, 2019'
    d3: str = 'Feb 1, 2019'
    d4: str = 'Sep 30, 2019'

    dt1: datetime = datetime.strptime(d1, '%b %d, %Y')
    dt2: datetime = datetime.strptime(d2, '%b %d, %Y')
    dt3: datetime = datetime.strptime(d3, '%b %d, %Y')
    dt4: datetime = datetime.strptime(d4, '%b %d, %Y')

    dt5: datetime = dt4 - dt3

    three_days_after_02272000: datetime = f'The date three days after {dt1:%b %d, %Y} is {(dt1 + timedelta(days=3)):%b %d, %Y}'
    three_days_after_02272019: datetime = f'The date three days after {dt2:%b %d, %Y} is {(dt2 + timedelta(days=3)):%b %d, %Y}'
    days_passed_02012019_09302019: int = f'{dt5.days} days passed between {dt3:%b %d, %Y} and {dt4:%b %d, %Y}'

    return three_days_after_02272000, three_days_after_02272019, days_passed_02012019_09302019


def file_reader(path: str, fields: int, sep: str = ',', header: bool = False) -> Iterator[Tuple[str]]:
    """ Write a generator function to read text files and return all of the values"""

    try:
        fp = open(path, 'r')
    except FileNotFoundError:
        raise FileNotFoundError("File Not Found")
    else:
        line_num: int = 0
        with fp:
            reader = csv.reader(fp, delimiter=sep)

            for line in reader:
                line_num += 1
                if len(line) != fields:
                    raise ValueError(
                        f'{path} has {len(line)} fields on line {line_num} expected {fields}')
                if header == False:
                    yield tuple(line)
                else:
                    header = False


class FileAnalyzer():

    """Analyze the file"""

    def __init__(self, directory: str) -> None:
        """Directory for File Analyzer  """
        self.directory: str = directory
        self.files_summary: Dict[str, Dict[str, int]] = dict()
        self.analyze_files()

    def analyze_files(self) -> None:
        """File Analyzing """
        path: str = self.directory
        direct: List[str] = os.listdir(path)
        for file in direct:
            if file.endswith('.py'):
                try:
                    fp = open(os.path.join(path, file), 'r')
                except FileNotFoundError:
                    raise FileNotFoundError('Sorry file doesnt exist')
                else:
                    with fp:
                        character_count: int = 0
                        class_count: int = 0
                        function_count: int = 0
                        line_count: int = 0

                        for line in fp:
                            character_count += len(line)
                            line_count += 1

                            if line.strip().startswith('def '):
                                function_count += 1
                            if line.startswith('class '):
                                class_count += 1

                        self.files_summary[file] = {
                            'classes': class_count,
                            'functions': function_count,
                            'lines': line_count,
                            'characters': character_count
                        }

    def pretty_print(self) -> None:
        """ Organize the table """
        x: PrettyTable = PrettyTable()
        x.field_names = ['File Name', 'Classes',
                         'Functions', 'Lines', 'Characters']

        for i, j in self.files_summary.items():
            x.add_row([i, j['classes'], j['functions'],
                       j['lines'], j['characters']])

        return x
