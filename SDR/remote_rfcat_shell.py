from rflib import *
import binascii 

d = RfCat()
d.setFreq(314950000)
d.setMdmModulation(MOD_ASK_OOK)
d.setMdmDRate(4800)

d.RFxmit(("\x8e\xe8\xe8\x88\x88\xe8\x88\x8e\x00\x00\x00" * 21))