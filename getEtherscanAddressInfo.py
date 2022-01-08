import unittest
from etherscan import Etherscan
import datetime as dt
import pandas as pd

eth = Etherscan('VEQSPWESY5P3P9AZSUQ7J6C89HUZHZ5BM5')

Wallet_Address = '0x2e96bf59B58Ed7dC0fab4Af637d643727Dd87e54'
eth_balance = eth.get_eth_balance(Wallet_Address)
#
current_time = round(dt.datetime.now().timestamp())
#
current_block = eth.get_block_number_by_timestamp(
    current_time, closest='before')

#

# getStartBlock


def convert_days_ago_to_block_number(number_of_days):
    current_time = dt.datetime.now()
    time_into_past = dt.timedelta(days=number_of_days)
    start_time = current_time - time_into_past
    start_timestamp = round(start_time.timestamp())

    block = eth.get_block_number_by_timestamp(
        start_timestamp, closest='before')
    return block


block_history_length = convert_days_ago_to_block_number(100)
start_block = str(int(current_block) - int(block_history_length))
normal_txns = eth.get_normal_txs_by_address(
    address=Wallet_Address, startblock=start_block, endblock=current_block, sort='asc')

cols = ["blockNumber", "timeStamp", "hash", "nonce", "blockHash", "transactionIndex", "from",
        "to", "value", "gas", "gasPrice", "isError", "txreceipt_status", "input", "contractAddress", "cumulativeGasUsed", "gasUsed", "confirmations"]
normal_txs_df = pd.DataFrame(normal_txns, columns=cols)

print(normal_txs_df)

# print(float(eth_balance)/1000000000000000000)


# class TestEtherscanApi(unittest.TestCase):
#     def test_convert_days_to_blocks(self):
#         self.assertEqual('13222106', convertDaysToBlockLength(100))


if __name__ == '__main__':
    unittest.main()
