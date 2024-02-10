WALLET_ADDRESSES_PATH = "data/wallet_addresses.txt"
RESULT_JSON_PATH = "data/result.json"
PROXIES_PATH = "data/proxies.txt"

RPC_URL = ""

BLAST_REQUEST_URL = RPC_URL + "/v1/accounts/{address}/transactions?start={start}&limit=100"
WAPAL_URL = "https://marketplace-api.wapal.io/user/tokens/"

COIN_STORE = "0x1::coin::CoinStore"


class Token:
    def __init__(
            self,
            contract_address: str,
            decimals: int,
            symbol: str
    ):
        self.contract_address = contract_address
        self.decimals = decimals
        self.symbol = symbol

    def from_wei(self, value: int) -> int:
        return value / 10 ** self.decimals


APT_TOKEN = Token(
    contract_address="0x1::aptos_coin::AptosCoin",
    decimals=8,
    symbol="APT"
)

USDC_TOKEN = Token(
    contract_address="0xf22bede237a07e121b56d91a491eb7bcdfd1f5907926a9e58338f964a01b17fa::asset::USDC",
    decimals=6,
    symbol="zUSDC"
)

USDT_TOKEN = Token(
    contract_address="0xf22bede237a07e121b56d91a491eb7bcdfd1f5907926a9e58338f964a01b17fa::asset::USDT",
    decimals=6,
    symbol="zUSDT"
)

WETH_TOKEN = Token(
    contract_address="0xf22bede237a07e121b56d91a491eb7bcdfd1f5907926a9e58338f964a01b17fa::asset::WETH",
    decimals=6,
    symbol="zWETH"
)

TAPT_TOKEN = Token(
    contract_address="0x84d7aeef42d38a5ffc3ccef853e1b82e4958659d16a7de736a29c55fbbeb0114::staked_aptos_coin::StakedAptosCoin",
    decimals=8,
    symbol="tAPT"
)

DITTO_TOKEN = Token(
    contract_address="0xd11107bdf0d6d7040c6c0bfbdecb6545191fdf13e8d8d259952f53e1713f61b5::staked_coin::StakedAptos",
    decimals=8,
    symbol="stAPT"
)

ALT_TOKEN = Token(
    contract_address="0xd0b4efb4be7c3508d9a26a9b5405cf9f860d0b9e5fe2f498b90e68b8d2cedd3e::aptos_launch_token::AptosLaunchToken",
    decimals=8,
    symbol="ALT"
)

THL_TOKEN = Token(
    contract_address="0x7fd500c11216f0fe3095d0c4b8aa4d64a4e2e04f83758462f2b127255643615::thl_coin::THL",
    decimals=8,
    symbol="THL"
)

THAPT_TOKEN = Token(
    contract_address="0xfaf4e633ae9eb31366c9ca24214231760926576c7b625313b3688b5e900731f6::staking::ThalaAPT",
    decimals=8,
    symbol="thAPT"
)

SOL_TOKEN = Token(
    contract_address="0xdd89c0e695df0692205912fb69fc290418bed0dbe6e4573d744a6d5e6bab6c13::coin::T",
    decimals=8,
    symbol="SOL"
)
