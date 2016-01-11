 require 'rubygems'
 require 'serialport'
 sp = SerialPort.new "/dev/ttyAMA0", 4800
 #sp.write "AT\r\n"
 puts sp.read   # hopefully "OK" ;-)
