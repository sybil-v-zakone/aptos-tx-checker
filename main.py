import requests
from loguru import logger

from utils import change_mobile_ip, read_from_txt
from const.constants import WALLET_ADDRESSES_PATH, ANKR_REQUEST_URl, PROXIES_PATH

if __name__ == "__main__":
    change_mobile_ip()

    addresses = read_from_txt(WALLET_ADDRESSES_PATH)
    proxies = read_from_txt(PROXIES_PATH)

    if 0 < len(proxies) != len(addresses):
        logger.error("Proxies and addresses should be one to one")
        exit()

    for address in addresses:
        proxy = None

        logger.debug(f"Wallet: {address}")

        if len(proxies) > 0:
            proxy = proxies[address.index(address)]

        url = ANKR_REQUEST_URl.format(address=address, offset=0)
        proxy = None if proxy is None else {"https": f"http://{proxy}"}

        response = requests.get(url=url, proxies=proxy)
        data = response.json()
        print(data)
