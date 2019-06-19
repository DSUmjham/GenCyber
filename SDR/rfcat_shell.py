from rflib import *
import binascii 

d = RfCat()
d.setFreq() #frequency to transmit on
d.setMdmModulation() #modulation type (think shape of wave)
d.setMdmDRate() #speed to send the 1's and 0's

d.RFxmit()