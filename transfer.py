import utility
from utility import get_balance
import config
import subprocess

balance = utility.get_balance()
print balance

if balance > 10:
    transfer_amount = (float(balance)) - (float(config.minerfee))
    print transfer_amount
    subprocess.check_output("feathercoind sendtoaddress %s %s" % (config.forwardaddress, transfer_amount), shell=True)
else:
    print 'balance below 10ftc'
