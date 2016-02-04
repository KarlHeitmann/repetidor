require 'net/http'
require 'json'
require 'awesome_print'

ap ARGV[0]
data = JSON.parse(ARGV[0])
ap data

uri = URI('http://localhost:3000/data')
res = Net::HTTP.post_form(uri, 'datum[bruto]' => data)
#ap res.body
