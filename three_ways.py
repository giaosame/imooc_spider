import urllib.request
import http.cookiejar

print(urllib.request)
print(http.cookiejar)
url = "http://www.baidu.com"

# The first method to download a webpage
# print('The second method to download a webpage:')
# response1 = urllib.request.urlopen(url)
# print(response1.getcode())
# print(len(response1.read()))

# The second method to download a webpage:
print('The second method to download a webpage:')
request = urllib.request.Request(url)
request.add_header("User-Agent", "Chrome/60.0.3112.78")
response2 = urllib.request.urlopen(request)
print(response2.getcode())
print(len(response2.read()))

# The third method to download a webpage:
print('The third method to download a webpage:')
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
urllib.request.install_opener(opener)
response3 = urllib.request.urlopen(url)
print(response3.getcode())
print(response3.read())
