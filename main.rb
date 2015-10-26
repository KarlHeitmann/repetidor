#DESCARGAR ESTO:
#https://github.com/WiringPi/WiringPi-Ruby

require 'net/http'
require 'wiringpi2'
require 'awesome_print'

PIN_LECTURA = 18
PINES = [1, 12, 18]
#Configuracion
io = WiringPi::GPIO.new do |gpio|
  #gpio.pin_mode(PIN_LECTURA, WiringPi::INPUT)
  PINES.each do |pin_lectura|
    gpio.pin_mode(pin_lectura, WiringPi::INPUT)
  end

end

i=0
while true
  sleep(0.1)
  PINES.each do |pin_lectura|
    ap pin_lectura
    input_value = io.digital_read(pin_lectura)
    ap input_value
  end
end
uri = URI('http://10.0.0.2:3000/data')
res = Net::HTTP.post_form(uri, 'datum[bruto]' => 'raspi')
ap res.body
