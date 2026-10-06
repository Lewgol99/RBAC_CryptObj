from web3 import Web3
from colorama import Fore
import json
from web3.middleware import ExtraDataToPOAMiddleware as geth_poa_middleware
from blockchain_browser import Sepolia_Browser
from blockchain_latency_monitor import BlockchainLatencyMonitor

browser = Sepolia_Browser()
browser.open_etherscan()
browser.open_faucet()

class Token:
    def __init__(self):
        self.blockchain_latency_monitor = BlockchainLatencyMonitor()
        self.user_wallets = []
        self.w3 = None
        
    def Web3_Connect(self):
        self.w3 = Web3(Web3.HTTPProvider(self.blockchain_config['INFURA_URL']))
        self.private_key = self.blockchain_config["PRIVATE_KEY"]
        self.from_address = self.blockchain_config["FROM_ADDRESS"]
        self.contract_address = self.blockchain_config["CONTRACT_ADDRESS"]

        if self.w3.is_connected():
            self.w3.middleware_onion.inject(geth_poa_middleware, layer=0)

            self.contract = self.w3.eth.contract(
                address=Web3.to_checksum_address(self.contract_address),
                abi=self.contract_abi
            )

            print(Fore.GREEN + "Web3 Connection Successful")
            return True
        else:
            print(Fore.RED + "Web3 Connection Failed")
            return False

    def Send_Token(self, to_address, amount, wait_for_receipt=True, timeout=120):
        try:
            token_amount = self.w3.to_wei(amount, 'ether')
            
            # Get fresh nonce for each transaction
            nonce = self.w3.eth.get_transaction_count(self.from_address)
            
            transaction = self.contract.functions.transfer(
                Web3.to_checksum_address(to_address), 
                token_amount
            ).build_transaction({
                'chainId': self.blockchain_network['network']['chainId'],
                'gas': self.blockchain_network['network']['gas'],
                'gasPrice': self.w3.eth.gas_price,
                'nonce': nonce,
            })
            
            signed_txn = self.w3.eth.account.sign_transaction(transaction, self.private_key)
            tx_hash = self.w3.eth.send_raw_transaction(signed_txn.raw_transaction)
            
            print(f"Transaction sent! Hash: {tx_hash.hex()}")
            
            # Wait for transaction to be mined
            if wait_for_receipt:
                receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash, timeout=timeout)
                print(f"Transaction confirmed in block {receipt['blockNumber']}")
            
            return tx_hash.hex()

        except Exception as e:
            print(f"Error: {e}")
            return None
    
    def Get_Wallet_Address(self, name):
        if name in self.user_wallets:
            return self.user_wallets[name]['address']
        return None
