import webbrowser

class Sepolia_Browser:
    def open_etherscan(self, url=None):
        if url is None:
            url = f"https://sepolia.etherscan.io/address/0xA0Fcc5F09B4D221AB1C69F1798BD1F5E5F167139"
        webbrowser.open(url)
        return True

    def open_faucet(self, url=None):
        if url is None:
            url = "https://cloud.google.com/application/web3/faucet/ethereum/sepolia"
        webbrowser.open(url)
        return True
