import urllib
import urllib2

url = "http://abcde.com"
form = {'name':'abc','password':'1234'}
form_data = urllib.urlencode(form)
request = urllib2.Request(url,form_data)
response = urllib2.urlopen(request)
print response.read()