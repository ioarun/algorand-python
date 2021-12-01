# https://developer.algorand.org/docs/get-details/dapps/pyteal/

from pyteal import *

"""Save License number -  Application"""

def approval_program():
   handle_creation = Seq([
       App.globalPut(Bytes("License Number"), Bytes('ABC123456')),
       Return(Int(1))
   ])

   handle_optin = Return(Int(0))

   handle_closeout = Return(Int(0))

   handle_updateapp = Return(Int(0))

   handle_deleteapp = Return(Int(0))

   scratchLicenseNumber = ScratchVar(TealType.bytes)

   save_license_number = Seq([
       scratchLicenseNumber.store(App.globalGet(Bytes("License Number"))),
       App.globalPut(Bytes("License Number"), scratchLicenseNumber.load()),
       Return(Int(1))
   ])

   retrieve_license_number = Seq([
       scratchLicenseNumber.store(App.globalGet(Bytes("License Number"))),
        # If(scratchLicenseNumber.load(),
        #     App.globalPut(Bytes("License Number"), scratchLicenseNumber.load()),
        # ),
        Return(Int(1))
   ])

   handle_noop = Cond(
       [And(
           Global.group_size() == Int(1),
           Txn.application_args[0] == Bytes("Save License Number")
       ), save_license_number],
       [And(
           Global.group_size() == Int(1),
           Txn.application_args[0] == Bytes("Retrieve License Number")
       ), retrieve_license_number],
   )


   program = Cond(
       [Txn.application_id() == Int(0), handle_creation],
       [Txn.on_completion() == OnComplete.OptIn, handle_optin],
       [Txn.on_completion() == OnComplete.CloseOut, handle_closeout],
       [Txn.on_completion() == OnComplete.UpdateApplication, handle_updateapp],
       [Txn.on_completion() == OnComplete.DeleteApplication, handle_deleteapp],
       [Txn.on_completion() == OnComplete.NoOp, handle_noop]
   )
   # Mode.Application specifies that this is a smart contract
   return compileTeal(program, Mode.Application, version=3)


def clear_state_program():
   program = Return(Int(1))
   # Mode.Application specifies that this is a smart contract
   return compileTeal(program, Mode.Application, version=3)

# print out the results
print(approval_program())
print(clear_state_program())