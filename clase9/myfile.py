import requests
response = requests.get ('http://www.google.com')
print (response)

r = requests.get ('https://www.google.com')
r.text



with open ( google.html, 'w') as f:
    f.write(r.text)