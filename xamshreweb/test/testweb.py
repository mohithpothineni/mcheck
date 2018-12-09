import urllib.request as ur
import urllib.parse as up


#working....
#get method for checking the intial index.html
req = ur.Request(url = "http://localhost:8080")
res = ur.urlopen(req)
print(res.read())

#need to develop and test...
#post method for checking the message posting functionality
data_sending = {'lask' : 'hello working'}
data_sending = up.urlencode(data_sending).encode('ascii')
req = ur.Request(url = "http://localhost:8080/message", data = data_sending, method = 'POST')
res = ur.urlopen(req)
print(dir(req))
print(req.data)
print(res.read())


#need to develop and test...
#get method for checking the message getting gunctionality
req = ur.Request(url = "http://localhost:8080/updatemessages", method = 'POST')
res = ur.urlopen(req)
print(res.read())



