require 'net/https'
uri = URI('https://api.clever.com/v1.1/sections/530e5979049e75a9262d0af2/students')

http = Net::HTTP.new(uri.host, uri.port)
http.use_ssl = true
http.verify_mode = OpenSSL::SSL::VERIFY_PEER

request = Net::HTTP::Get.new(uri.request_uri)
request.add_field 'Authorization', 'Bearer DEMO_TOKEN'

response = http.request(request)
puts response.body.length
