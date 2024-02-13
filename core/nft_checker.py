import requests
from loguru import logger

from constants import WAPAL_URL


def get_nfts_on_account(address: str, proxy: dict):
    try:
        nft = []

        url = WAPAL_URL.format(address=address)
        response = requests.get(url=url, proxies=proxy)
        response_data = response.json()

        for item in response_data:
            nft.append(item["tokenName"])

        return nft
    except Exception as e:
        logger.error(f"Exception in get nfts function: {str(e)}")
