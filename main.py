from core.checker import run_checker
from utils import change_mobile_ip, get_addresses_and_proxies, save_to_exel

if __name__ == "__main__":
    change_mobile_ip()

    addresses, proxies = get_addresses_and_proxies()
    result = run_checker(addresses=addresses, proxies=proxies)

    save_to_exel(result)
