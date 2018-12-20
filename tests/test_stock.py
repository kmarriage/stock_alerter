import unittest
from ..stock import Stock
from datetime import datetime


class StockTest(unittest.TestCase):
    def test_price_of_a_new_stock_class_should_be_None(self):
        stock = Stock('GOOG')
        self.assertIsNone(stock.price)

    def test_stock_price_update(self):
        """
        An update should set the price on the stock object
        We will be using the 'datetime' module for the timestamp
        """
        goog = Stock('GOOG')
        goog.update(datetime(2014, 2, 12), price=10)
        self.assertEqual(10, goog.price)

    def test_negative_price_should_throw_ValueError(self):
        goog = Stock('GOOG')
        try:
            goog.update(datetime(2014, 2, 13), price=-1)
        except ValueError:
            return
        self.fail("ValueError was not raised")
