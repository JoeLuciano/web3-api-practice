import getetherscanaddressinfo as address
import unittest


class TestEtherscanApi(unittest.TestCase):
    def test_convert_days_to_blocks(self):
        self.assertEqual('637868', address.convertDaysToBlockLength(100))


if __name__ == '__main__':
    unittest.main()
