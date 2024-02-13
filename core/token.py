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
