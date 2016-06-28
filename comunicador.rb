require 'net/http'
require 'json'
require 'awesome_print'

ap ARGV[0]
data = JSON.parse(ARGV[0])
ap data

#uri = URI('http://192.168.0.16:3000/data') #red CASA 195
#uri = URI('http://localhost:3000/data')
uri = URI('https://secure-eyrie-71751.herokuapp.com/data')
res = Net::HTTP.post_form(uri, 'datum[bruto]' => data, 'datum[id]' => "1")
#ap res.body
