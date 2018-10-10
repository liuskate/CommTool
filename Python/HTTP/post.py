import json
import urllib2
   
url = 'http://www.google.com/someservice'
postdata = {'key':'value'}

req = urllib2.Request(url)
req.add_header('Content-Type','application/json')
data = json.dumps(postdata)
response = urllib2.urlopen(req,data)
