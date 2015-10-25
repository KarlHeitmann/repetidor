require 'net/http'
#curl -d "datum[bruto]=qqqqqqqqqq" 10.0.0.2:3000/data
uri = URI('http://10.0.0.2:3000/data')
res = Net::HTTP.post_form(uri, 'datum[bruto]' => 'raspi')
puts res.body
