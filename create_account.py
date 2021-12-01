from algosdk import account, mnemonic

def generate_algorand_keypair():
    private_key, address = account.generate_account()
    print("My address: {}".format(address))
    print("My private key: {}".format(private_key))
    print("My passphrase: {}".format(mnemonic.from_private_key(private_key)))

'''
Base64 Private Key: kODwAI6SDKIjcECUUlkZ0lnXvyvfnbVdSik76ObENVFEm+jPi4eV2ud2esb87XVPz3/8Bu6t2D/sTTu8HW6KMA==
Public Algorand Address: ISN6RT4LQ6K5VZ3WPLDPZ3LVJ7HX77AG52W5QP7MJU53YHLORIYL3ZGKNA

Dispenser: https://bank.testnet.algorand.network/

'''

