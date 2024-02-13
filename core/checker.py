from loguru import logger

from core.nft_checker import get_nfts_on_account
from core.total import get_total
from core.tx_checker import get_txs_on_account
from utils import get_tokens_balance_batch, save_to_json, change_mobile_ip


def run_checker(addresses: list, proxies: list):
    data = {}

    for address in addresses:
        try:
            change_mobile_ip()
            logger.debug(f"Wallet: {address}")
            data[f"{address}"] = {}
            current_wallet = data[f"{address}"]

            proxy = None

            if len(proxies) > 0:
                proxy = proxies[addresses.index(address)]

            proxy = None if proxy is None else {"https": f"http://{proxy}"}

            current_wallet["transactions"] = get_txs_on_account(address=address, proxy=proxy)

            current_wallet["nft"] = get_nfts_on_account(address=address, proxy=proxy)

            current_wallet["token_balances"] = get_tokens_balance_batch(address=address, proxy=proxy)

            logger.success("Wallet successfully checked")

        except Exception as e:
            logger.error(f"Error with address: {address} - {str(e)}")

    data["total"] = get_total(data=data)
    save_to_json(data)
    return data
