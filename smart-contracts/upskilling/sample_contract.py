# https://developer.algorand.org/docs/get-details/dapps/pyteal/

from pyteal import *

"""Basic Counter Application"""

def approval_program():
   program = Return(Int(1))
   # Mode.Application specifies that this is a smart contract
   return compileTeal(program, Mode.Application, version=5)

def clear_state_program():
   program = Return(Int(1))
   # Mode.Application specifies that this is a smart contract
   return compileTeal(program, Mode.Application, version=5)

print (approval_program())
print (clear_state_program())