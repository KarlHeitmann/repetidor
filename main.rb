require 'net/http'
require 'wiringpi2'
require 'awesome_print'

#DESCARGAR ESTO:
#https://github.com/WiringPi/WiringPi-Ruby

#curl -d "datum[bruto]=qqqqqqqqqq" 10.0.0.2:3000/data
uri = URI('http://10.0.0.2:3000/data')
res = Net::HTTP.post_form(uri, 'datum[bruto]' => 'raspi')
ap res.body
