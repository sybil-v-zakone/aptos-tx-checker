import requests
from loguru import logger

from constants import RPC_TX_FETCH_URL, CONTRACTS


def get_txs_on_account(address: str, proxy: dict) -> dict:
    try:
        transactions = {}

        start = 0
        tx_count = 0

        while True:
            url = RPC_TX_FETCH_URL.format(address=address, start=start)
            response = requests.get(url=url, proxies=proxy)
            response_data = response.json()

            tx_count_in_response = len(response_data)

            for tx in response_data:
                try:
                    contract_address = tx["payload"]["function"].split("::")[0]
                    for contract in CONTRACTS:
                        if contract_address in CONTRACTS[contract]:
                            if contract in transactions:
                                transactions[contract] += 1
                            else:
                                transactions[contract] = 0

                except Exception:
                    logger.error(f"Error payload at tx: {tx}")

            if tx_count_in_response == 0:
                transactions["tx_count"] = tx_count
                break
            else:
                tx_count += tx_count_in_response
                start += tx_count_in_response
        return transactions
    except Exception as e:
        logger.error(f"Exception in get tx function: {str(e)}")
