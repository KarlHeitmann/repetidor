require 'net/http'
require 'json'
#require 'wiringpi2'
require 'awesome_print'

#DESCARGAR ESTO:
#https://github.com/WiringPi/WiringPi-Ruby

#data = JSON.parse(ARGV[0])
ap ARGV[0]
#data = JSON.parse('{"hello": "goodbye"}')
data = JSON.parse(ARGV[0])
ap data

uri = URI('http://localhost:3000/data')
res = Net::HTTP.post_form(uri, 'datum[bruto]' => ARGV[0])
ap res.body
