import requests
from loguru import logger

from config import TOKENS
from utils import change_mobile_ip, read_from_txt, save_to_json, get_token_balance
from constants import WALLET_ADDRESSES_PATH, BLAST_REQUEST_URL, PROXIES_PATH, WAPAL_URL

if __name__ == "__main__":
    change_mobile_ip()

    addresses = read_from_txt(WALLET_ADDRESSES_PATH)
    proxies = read_from_txt(PROXIES_PATH)

    if 0 < len(proxies) != len(addresses):
        logger.error("Proxies and addresses should be one to one")
        exit()

    data = {}
    index = 0

    for address in addresses:
        try:
            logger.debug(f"Wallet: {address}")
            data[f"{address}"] = {}
            current_wallet = data[f"{address}"]

            proxy = None
            if len(proxies) > 0:
                proxy = proxies[address.index(address)]

            current_wallet["pancakeswap"] = 0
            current_wallet["liquidswap"] = 0
            current_wallet["sushiswap"] = 0
            current_wallet["thalaswap"] = 0
            current_wallet["econia"] = 0
            current_wallet["tortuga"] = 0
            current_wallet["merkle"] = 0
            current_wallet["amnis"] = 0
            current_wallet["ditto"] = 0
            current_wallet["wapal"] = 0
            current_wallet["topaz"] = 0
            current_wallet["bluemove"] = 0
            current_wallet["mercato"] = 0
            current_wallet["swapgpt"] = 0
            current_wallet["kanalabs"] = 0

            proxy = None if proxy is None else {"https": f"http://{proxy}"}

            start = 0
            tx_count = 0

            while True:
                url = BLAST_REQUEST_URL.format(address=address, start=start)
                response = requests.get(url=url, proxies=proxy)
                response_data = response.json()

                tx_count_in_response = len(response_data)

                for tx in response_data:
                    try:
                        contract_address = tx["payload"]["function"].split("::")[0]

                        if contract_address == "0xc7efb4076dbe143cbcd98cfaaa929ecfc8f299203dfff63b95ccb6bfe19850fa":
                            current_wallet["pancakeswap"] += 1
                        elif contract_address == "0x190d44266241744264b964a37b8f09863167a12d3e70cda39376cfb4e3561e12":
                            current_wallet["liquidswap"] += 1
                        elif contract_address == "0x163df34fccbf003ce219d3f1d9e70d140b60622cb9dd47599c25fb2f797ba6e":
                            current_wallet["liquidswap"] += 1
                        elif contract_address == "":
                            current_wallet["pancakeswap"] += 1
                        elif contract_address == "0x31a6675cbe84365bf2b0cbce617ece6c47023ef70826533bde5203d32171dc3c":
                            current_wallet["sushiswap"] += 1
                        elif contract_address == "0x48271d39d0b05bd6efca2278f22277d6fcc375504f9839fd73f74ace240861af":
                            current_wallet["thalaswap"] += 1
                        elif contract_address == "0xc0deb00c405f84c85dc13442e305df75d1288100cdd82675695f6148c7ece51c":
                            current_wallet["econia"] += 1
                        elif contract_address == "0x8f396e4246b2ba87b51c0739ef5ea4f26515a98375308c31ac2ec1e42142a57f":
                            current_wallet["tortuga"] += 1
                        elif contract_address == "0x5ae6789dd2fec1a9ec9cccfb3acaf12e93d432f0a3a42c92fe1a9d490b7bbc06":
                            current_wallet["merkle"] += 1
                        elif contract_address == "0x111ae3e5bc816a5e63c2da97d0aa3886519e0cd5e4b046659fa35796bd11542a":
                            current_wallet["amnis"] += 1
                        elif contract_address == "0xd11107bdf0d6d7040c6c0bfbdecb6545191fdf13e8d8d259952f53e1713f61b5":
                            current_wallet["ditto"] += 1
                        elif contract_address == "0x584b50b999c78ade62f8359c91b5165ff390338d45f8e55969a04e65d76258c9":
                            current_wallet["wapal"] += 1
                        elif contract_address == "0x6547d9f1d481fdc21cd38c730c07974f2f61adb7063e76f9d9522ab91f090dac":
                            current_wallet["wapal"] += 1
                        elif contract_address == "0x2c7bccf7b31baf770fdbcc768d9e9cb3d87805e255355df5db32ac9a669010a2":
                            current_wallet["topaz"] += 1
                        elif contract_address == "0xd520d8669b0a3de23119898dcdff3e0a27910db247663646ad18cf16e44c6f5":
                            current_wallet["bluemove"] += 1
                        elif contract_address == "0xe11c12ec495f3989c35e1c6a0af414451223305b579291fc8f3d9d0575a23c26":
                            current_wallet["mercato"] += 1
                        elif contract_address == "0x1c3206329806286fd2223647c9f9b130e66baeb6d7224a18c1f642ffe48f3b4c":
                            current_wallet["swapgpt"] += 1
                        elif contract_address == "0x9538c839fe490ccfaf32ad9f7491b5e84e610ff6edc110ff883f06ebde82463d":
                            current_wallet["kanalabs"] += 1
                    except Exception as e:
                        logger.error(f"Error payload at tx: {tx}")

                if tx_count_in_response == 0:
                    tx_count += tx_count_in_response
                    current_wallet["tx_count"] = tx_count
                    break
                else:
                    tx_count += tx_count_in_response
                    start += tx_count_in_response

            nft = []

            url = WAPAL_URL + address
            response = requests.get(url=url, proxies=proxy)
            response_data = response.json()

            for item in response_data:
                nft.append(item["tokenName"])

            current_wallet["nft"] = nft

            token_balances = {}

            for token in TOKENS:
                token_balances[token.symbol] = get_token_balance(token, address, proxy)

            current_wallet["token_balances"] = token_balances

            logger.success("Wallet successfully checked, save to result")
            save_to_json(data)

        except Exception as e:
            logger.error(f"Error with address: {address}")
