import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    stock, bid_price, ask_price, price = getDataPoint(quotes[1])
    self.assertEqual(bid_price, 117.87)   # bid_price of DEF
    self.assertEqual(ask_price, 121.68)   # ask_price of DEF


  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    stock, bid_price, ask_price, price = getDataPoint(quotes[0])
    self.assertEqual(bid_price, 120.48)
    self.assertEqual(ask_price, 119.2)

  def test_getDataPoint_emptyQuotes(self):
    quotes = {}
    result = getDataPoint(quotes)
    self.assertIsNone(result)

  def test_getDataPoint_priceNone(self):
    quotes = {'top_ask': {'price': None, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': None, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'}
    stock, bid_price, ask_price, price = getDataPoint(quotes)
    self.assertIsNone(bid_price)
    self.assertIsNone(ask_price)

  def test_getRatio(self):
    quotes = {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    stock, bid_price, ask_price, price = getDataPoint(quotes)
    expected_ratio = 121.68/117.87
    ratio = getRatio(ask_price, bid_price)
    self.assertEqual(ratio, expected_ratio)

  def test_getRatio_priceNone(self):
    ratio = getRatio(None, 117.87)
    self.assertIsNone(ratio)

  def test_getRatio_priceNotExist(self):
    quotes = {'top_ask': {'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'}
    stock, bid_price, ask_price, price = getDataPoint(quotes)
    self.assertIsNone(bid_price)
    self.assertIsNone(ask_price)

if __name__ == '__main__':
    unittest.main()
