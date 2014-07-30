__author__ = 'd3non'

import unittest
import datetime

from c3daysleft import sleep, twitter, get_teweet, get_format, get_nextC3date


class c3daysleftTests(unittest.TestCase):

    def test_get_nextC3date(self):
        self.assertEqual(get_nextC3date(datetime.date(2014, 12, 1)), datetime.date(2014, 12, 27))
        self.assertEqual(get_nextC3date(datetime.date(2014, 12, 27)), datetime.date(2014, 12, 27))
        self.assertEqual(get_nextC3date(datetime.date(2014, 12, 29)), datetime.date(2014, 12, 27))
        self.assertEqual(get_nextC3date(datetime.date(2014, 12, 31)), datetime.date(2015, 12, 27))
        self.assertEqual(get_nextC3date(datetime.date(2015, 6, 1)), datetime.date(2015, 12, 27))

    def test_get_format(self):
        date = datetime.date(2014, 8, 1)
        format_map = get_format(nextC3date=get_nextC3date(date), date=date)
        self.assertEqual(format_map,
                         {'days_left': 148, 'nextC3': '31C3', 'nextC3_date': datetime.date(2014, 12, 27)})

    def test_get_format_day1(self):
        date = datetime.date(2014, 12, 27)
        format_map = get_format(nextC3date=get_nextC3date(date), date=date)
        self.assertEqual(format_map,
                         {'days_left': 0, 'nextC3': '31C3', 'nextC3_date': datetime.date(2014, 12, 27)})

    def test_get_format_day3(self):
        date = datetime.date(2014, 12, 29)
        format_map = get_format(nextC3date=get_nextC3date(date), date=date)
        self.assertEqual(format_map,
                         {'days_left': -2, 'nextC3': '31C3', 'nextC3_date': datetime.date(2014, 12, 27)})

    def test_get_format_day5(self):
        date = datetime.date(2014, 12, 31)
        format_map = get_format(nextC3date=get_nextC3date(date), date=date)
        self.assertEqual(format_map,
                         {'days_left': 361, 'nextC3': '32C3', 'nextC3_date': datetime.date(2015, 12, 27)})

    def test_sleep(self):
        start = datetime.datetime.now()
        sleep(1, 5)
        slept = (datetime.datetime.now() - start).seconds
        self.assertTrue(slept >= 1)
        self.assertTrue(slept <= 5)

    def test_sleep_exact(self):
        start = datetime.datetime.now()
        sleep(3, 3)
        self.assertEqual(3, (datetime.datetime.now() - start).seconds)

if __name__ == "__main__":
    c3daysleftTests().run()