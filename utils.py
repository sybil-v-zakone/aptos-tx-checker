import json

import requests
from loguru import logger

from config import USE_MOBILE_PROXY, CHANGE_IP_URL
from const.constants import RESULT_JSON_PATH


def change_mobile_ip() -> None:
    try:
        if USE_MOBILE_PROXY:
            res = requests.get(CHANGE_IP_URL)

            if res.status_code == 200:
                logger.info("IP address changed successfully", send_to_tg=False)
            else:
                raise Exception("Failed to change IP address")

    except Exception as e:
        raise Exception(f"Encountered an error when changing ip address, check your proxy provider: {e}")


def read_from_txt(file_path: str) -> list[str]:
    try:
        with open(file_path, "r") as file:
            return [line.strip() for line in file]

    except Exception as e:
        raise Exception(f"Encountered an error while reading a txt file '{file_path}': {str(e)}")


def save_to_json(result: dict | str) -> None:
    try:
        if type(result) is dict:
            result = json.dumps(result, indent=4)

        with open(RESULT_JSON_PATH, 'w') as json_file:
            json_file.write(result)

    except Exception as e:
        raise Exception(f"Error while save json: {str(e)}")