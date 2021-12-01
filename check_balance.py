from algosdk.v2client import algod

def check_balance(my_address):
    algod_address = "http://localhost:4001"
    algod_token = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    algod_client = algod.AlgodClient(algod_token, algod_address)
    account_info = algod_client.account_info(my_address)
    print("Account balance: {} microAlgos".format(account_info.get('amount')) + "\n")

check_balance('HVEDLSIDXNQC2JDUZJEARRHT2NXNSECJMPPQM5PQJNEAHREPT6XPMJS3LI')
