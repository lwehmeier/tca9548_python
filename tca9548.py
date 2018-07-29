#!/usr/bin/python
# TCA9548A I2C multiplexer
# I2C Address: 70 through 77
# Channel: 0 - 7
 
import smbus
 
# class for the I2C switch
class I2C_SW(object):
  # init
  def __init__(self,name,address,bus_nr):
    self.name=name
    self.address=address
    self.bus_nr=bus_nr
    self.bus=smbus.SMBus(bus_nr)
 
  # Change to i2c channel 0..7
  def chn(self,channel):
    self.bus.write_byte(self.address,2**channel)
 
  # block all channels read only the main I2c (on which is the address SW)
  def _rst(self):
    self.bus.write_byte(self.address,0)
    print self.name,' ','Switch reset'
 
  # read all 8 channels
  def _all(self):
    self.bus.write_byte(self.address,0Xff)
    print self.name,' ','Switch read all lines'

if __name__ == "__main__":
	# define the usual sensor 0X70 bus 1
	SW=I2C_SW('I2C switch 0',0X70, 1)
	# SW._all()
	# SW._rst()
	# Selecteer kanaal nummer (0-7)
	# controleer met i2cdetect y -1 (if bus_nr=1)
	SW.chn(3)
