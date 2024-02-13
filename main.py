from core.checker import run_checker
from utils import get_addresses_and_proxies, save_to_exel

if __name__ == "__main__":
    addresses, proxies = get_addresses_and_proxies()
    result = run_checker(addresses=addresses, proxies=proxies)

    save_to_exel(result)
