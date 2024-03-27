import re

from loguru import logger


def get_total(data: dict) -> dict:
    total = {}
    contact_tx_count = {}
    total_token_balances = {}
    total_tx_count = 0
    total_quest_4_nft_count = 0
    total_quest_3_nft_count = 0
    total_quest_2_nft_count = 0
    total_quest_1_nft_count = 0
    total_aptos_domains_count = 0

    domain_pattern = re.compile(r'^[^.]*\.apt$')

    for address in data:
        try:
            address_info = data[address]
            for contract in address_info["transactions"]:
                if contract != "tx_count":
                    if contract in contact_tx_count:
                        contact_tx_count[contract] += address_info["transactions"][contract]
                    else:
                        contact_tx_count[contract] = address_info["transactions"][contract]

            total_tx_count += address_info["transactions"]["tx_count"]

            for nft in address_info["nft"]:
                if "Quest Three" in nft:
                    total_quest_3_nft_count += 1
                elif "Quest Two" in nft:
                    total_quest_2_nft_count += 1
                elif "Quest Four" in nft:
                    total_quest_4_nft_count += 1
                elif "Quest One" in nft:
                    total_quest_1_nft_count += 1
                elif domain_pattern.match(nft):
                    total_aptos_domains_count += 1

            for token in address_info["token_balances"]:
                token_balance = address_info["token_balances"][token]
                if token_balance is not None:
                    if token in total_token_balances:
                        total_token_balances[token] += token_balance
                    else:
                        total_token_balances[token] = address_info["token_balances"][token]

        except Exception as e:
            logger.error(f"Error while getting total: {str(e)}")
            continue

    total["transactions"] = contact_tx_count
    total["tx_count"] = total_tx_count
    total["quest_4_nft_count"] = total_quest_4_nft_count
    total["quest_3_nft_count"] = total_quest_3_nft_count
    total["quest_2_nft_count"] = total_quest_2_nft_count
    total["quest_1_nft_count"] = total_quest_1_nft_count
    total["aptos_domains_count"] = total_aptos_domains_count
    total["token_balances"] = total_token_balances

    return total
