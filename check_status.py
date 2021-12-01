

from algosdk.v2client import algod
import json 

def check_status(my_address):
    algod_address = "http://localhost:4001"
    algod_token = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    algod_client = algod.AlgodClient(algod_token, algod_address)
    status = algod_client.status()
    print(json.dumps(status, indent=4)) 

check_status('3QYUTA5XR4OD2TA77JJKPRCULPX6QIKTPSPZLTC2Y7XT7LHA2ZY3XJDVAI')