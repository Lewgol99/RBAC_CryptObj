from colorama import Fore
from web3 import Web3
import json

class Blockchain:
    def __init__(self):
        pass
    
    def extract_blockchain_configuration(self):
        with open('blockchain_config.json', 'r') as config_file:
            self.blockchain_config = json.load(config_file)
        print(Fore.LIGHTMAGENTA_EX + "blockchain_config.json loaded Successfully!")

        with open('blockchain_network.json', 'r') as network_file:
            self.blockchain_network = json.load(network_file)
        print(Fore.LIGHTMAGENTA_EX + "blockchain_network.json loaded Successfully!")
                
        with open('abi-counter.json', 'r') as abi_file:
            self.contract_abi = json.load(abi_file)
        print(Fore.LIGHTMAGENTA_EX + "abi-counter.json loaded Successfully!")

        with open('tokens.json', 'r') as wallet_file:
            self.tokens = json.load(wallet_file)
        print(Fore.LIGHTMAGENTA_EX + "tokens.json loaded Successfully!")
        return True
