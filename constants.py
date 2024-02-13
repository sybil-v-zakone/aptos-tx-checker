from core.token import Token

WALLET_ADDRESSES_PATH = "data/wallet_addresses.txt"
RESULT_JSON_PATH = "data/result.json"
PROXIES_PATH = "data/proxies.txt"

RPC_URL = ""

RPC_TX_FETCH_URL = RPC_URL + "/v1/accounts/{address}/transactions?start={start}&limit=100"
WAPAL_URL = "https://marketplace-api.wapal.io/user/tokens/{address}"

COIN_STORE = "0x1::coin::CoinStore"


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

CONTRACTS = {
    "pancakeswap": [
        "0xc7efb4076dbe143cbcd98cfaaa929ecfc8f299203dfff63b95ccb6bfe19850fa"
    ],
    "liquidswap": [
        "0x190d44266241744264b964a37b8f09863167a12d3e70cda39376cfb4e3561e12",
        "0x163df34fccbf003ce219d3f1d9e70d140b60622cb9dd47599c25fb2f797ba6e"
    ],
    "sushiswap": [
        "0x31a6675cbe84365bf2b0cbce617ece6c47023ef70826533bde5203d32171dc3c"
    ],
    "thalaswap": [
        "0x48271d39d0b05bd6efca2278f22277d6fcc375504f9839fd73f74ace240861af"
    ],
    "econia": [
        "0xc0deb00c405f84c85dc13442e305df75d1288100cdd82675695f6148c7ece51c"
    ],
    "tortuga": [
        "0x8f396e4246b2ba87b51c0739ef5ea4f26515a98375308c31ac2ec1e42142a57f"
    ],
    "merkle": [
        "0x5ae6789dd2fec1a9ec9cccfb3acaf12e93d432f0a3a42c92fe1a9d490b7bbc06"
    ],
    "amnis": [
        "0x111ae3e5bc816a5e63c2da97d0aa3886519e0cd5e4b046659fa35796bd11542a"
    ],
    "ditto": [
        "0xd11107bdf0d6d7040c6c0bfbdecb6545191fdf13e8d8d259952f53e1713f61b5"
    ],
    "wapal": [
        "0x584b50b999c78ade62f8359c91b5165ff390338d45f8e55969a04e65d76258c9",
        "0x6547d9f1d481fdc21cd38c730c07974f2f61adb7063e76f9d9522ab91f090dac"
    ],
    "topaz": [
        "0x2c7bccf7b31baf770fdbcc768d9e9cb3d87805e255355df5db32ac9a669010a2"
    ],
    "bluemove": [
        "0xd520d8669b0a3de23119898dcdff3e0a27910db247663646ad18cf16e44c6f5"
    ],
    "mercato": [
        "0xe11c12ec495f3989c35e1c6a0af414451223305b579291fc8f3d9d0575a23c26"
    ],
    "swapgpt": [
        "0x1c3206329806286fd2223647c9f9b130e66baeb6d7224a18c1f642ffe48f3b4c"
    ],
    "kanalabs": [
        "0x9538c839fe490ccfaf32ad9f7491b5e84e610ff6edc110ff883f06ebde82463d"
    ],
}
