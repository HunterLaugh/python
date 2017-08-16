from urllib.request import urlopen

# get function
url="http://www.baidu.com"
response=urlopen(url)
print(response.read())
