import urllib.request

get_url= urllib.request.urlopen('https://www.google.com/')

print("Response Status: "+ str(get_url.getcode()) )