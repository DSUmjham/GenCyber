from rflib import *
import binascii 

d = RfCat()
d.setFreq(314950000)
d.setMdmModulation(MOD_ASK_OOK)
d.setMdmDRate(4800)

d.RFxmit()