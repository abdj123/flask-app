from flask import Flask
from flask_restful import Api,Resource,reqparse


from web3 import Web3
from eth_account import Account
from mnemonic import Mnemonic
import secrets

import ast
import requests

app=Flask(__name__)
api=Api(app)

class create_wallet(Resource):
    def get(self):
        # Enable unaudited HD wallet features
        Account.enable_unaudited_hdwallet_features()

        # Generate a new mnemonic (secret phrase)
        mnemo = Mnemonic("english")
        mnemonic = mnemo.generate(strength=128)

        # Create a LocalAccount from the mnemonic
        account = Account.from_mnemonic(mnemonic)

        # Retrieve the private key from the LocalAccount
        private_key = account.key.hex()

        # Create an Ethereum address from the private key
        address = account.address

        return {"private_key":private_key,"address":address,"mnemonic":mnemonic}

class get_token_balance(Resource):

    def get(self,address):

        xrpBalance=ethBalance=bnbBalance=maticBalance=usdcBalance=manaBalance=wbtcBalance=uniswapBlance=shibBalance=usdtBalance=0
        ApiKey="31B2YRCRXKFM5NN484JYTU4AYX6TDN7J78"
        
        

        # get Xrp
        api_url = f"https://data.ripple.com/v2/accounts/{address}/balances"
        response = requests.get(api_url)
        data = response.json()
        
        if response.status_code == 200:
            for balance in data["balances"]:
                if balance["currency"] == "XRP":
                    xrpBalance=float(balance["value"])


        # get Eth 
        api_url = f"https://api.etherscan.io/api?module=account&action=balance&address={address}&tag=latest&apikey={ApiKey}"
        response = requests.get(api_url)
        data = response.json()
        
        if data["status"] == "1":
            balance = int(data["result"]) / 10**18  # Convert balance from wei to ETH
            ethBalance=round(balance,5)   


        # get BNB
        api_url = f"https://api.bscscan.com/api?module=account&action=balance&address={address}&tag=latest"
        response = requests.get(api_url)
        data = response.json()
        
        if data["status"] == "1":
            balance = int(data["result"]) / 10**18  # Convert balance from wei to BNB
            bnbBalance=round(balance,5)   

        # get Polygon

        url = f"https://api.polygonscan.com/api?module=account&action=balance&address={address}&tag=latest&apikey=YourApiKeyToken"
    
        
        response = requests.get(url)
        data = response.json()
        if data['status'] == '1':
            balance = int(data['result']) / 10**18
            maticBalance=round(balance,5)

        # get USDC

        url = f"https://api.etherscan.io/api?module=account&action=tokenbalance&contractaddress=0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48&address={address}&tag=latest&apikey={ApiKey}"
    
    
        response = requests.get(url)
        data = response.json()
        if data['status'] == '1':
            balance = int(data['result']) / 10**18
            usdcBalance=round(balance,5)


        # get WBTC

        url = f"https://api.etherscan.io/api?module=account&action=tokenbalance&contractaddress=0x2260fac5e5542a773aa44fbcfedf7c193bc2c599&address={address}&tag=latest&apikey={ApiKey}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            balance=int(data["result"]) / 10 ** 8
            wbtcBalance=round(balance,5)

        #  get UniSwap

        
        url = f"https://api.etherscan.io/api?module=account&action=tokenbalance&contractaddress=0x1f9840a85d5af5bf1d1762f925bdaddc4201f984&address={address}&tag=latest&apikey={ApiKey}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            balance=int(data["result"]) / 10 ** 8
            uniswapBlance=round(balance,5)


        # get SHIB

        
        url = f"https://api.etherscan.io/api?module=account&action=tokenbalance&contractaddress=0x95ad61b0a150d79219dcf64e1e6cc01f0b64c4ce&address={address}&tag=latest&apikey={ApiKey}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            balance=int(data["result"]) / 10 ** 8
            shibBalance=round(balance,5)

        # get MANA

        
        url = f"https://api.etherscan.io/api?module=account&action=tokenbalance&contractaddress=0x0f5d2fb29fb7d3cfee444a200298f468908cc942&address={address}&tag=latest&apikey={ApiKey}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            balance=int(data["result"]) / 10 ** 8
            manaBalance=round(balance,5)


        # get USDT

        url = f"https://api.etherscan.io/api?module=account&action=tokenbalance&contractaddress=0xdac17f958d2ee523a2206206994597c13d831ec7&address={address}&tag=latest&apikey={ApiKey}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            balance=int(data["result"]) / 10 ** 6
            usdtBalance=round(balance,3)

        

        return {"Balances":{"Eth":ethBalance,"BNB":bnbBalance,"XRP":xrpBalance,"Polygon":maticBalance,
                            "USDC":usdcBalance,"USDT":usdtBalance,"WBTC":wbtcBalance,"SHIB":shibBalance,
                            "UNI SWAP":uniswapBlance,"MANA":manaBalance,}}     


api.add_resource(create_wallet,"/create_wallet")
api.add_resource(get_token_balance,"/get_token_balance/<string:address>")



if __name__ == '__main__':
    app.run(host='0.0.0.0')










    
    


