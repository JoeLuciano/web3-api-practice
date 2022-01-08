from etherscan import Etherscan
from pycoingecko import CoinGeckoAPI
import datetime as dt
import pandas as pd


eth = Etherscan('VEQSPWESY5P3P9AZSUQ7J6C89HUZHZ5BM5')
cg = CoinGeckoAPI()

Wallet_Address = '0x2e96bf59B58Ed7dC0fab4Af637d643727Dd87e54'
eth_balance = eth.get_eth_balance(Wallet_Address)
current_time = round(dt.datetime.now().timestamp())
current_block = eth.get_block_number_by_timestamp(
    current_time, closest='before')


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


def get_column_list(structure):
    return list(structure[0].keys())


erc20_txns = eth.get_erc20_token_transfer_events_by_address(address=Wallet_Address,
                                                            startblock=start_block, endblock=current_block, sort='asc')

erc20_cols = get_column_list(erc20_txns)

erc20_dataframe = pd.DataFrame(erc20_txns, columns=erc20_cols)

unique_contracts = erc20_dataframe['contractAddress'].drop_duplicates()
unique_tokens = erc20_dataframe['tokenSymbol'].drop_duplicates()

tokens = []
amounts = []
prices = []
amounts_in_dollars = []
for token, contract_address in zip(unique_tokens, unique_contracts):
    token_amount = eth.get_acc_balance_by_token_and_contract_address(
        contract_address, Wallet_Address)
    token_price = cg.get_token_price(
        id='ethereum', contract_addresses=contract_address, vs_currencies='usd')

    if len(token_amount) > 17:  # AGIX seems to function differently...?
        real_token_amount = int(token_amount)/1e18
    else:
        real_token_amount = int(token_amount)/1e8

    try:
        real_token_price = token_price[contract_address]['usd']
    except:
        print(token)  # Liquidity pool tokens

    tokens.append(token)
    amounts.append(real_token_amount)
    prices.append(f"$ {real_token_price}")
    amounts_in_dollars.append(f"$ {real_token_amount * real_token_price}")

token_df = pd.DataFrame(
    {"Token Name": tokens, "Amount": amounts, "Price": prices, "Total": amounts_in_dollars})
print(token_df)
