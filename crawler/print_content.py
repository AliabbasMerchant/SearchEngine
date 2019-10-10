# https://summerofcode.withgoogle.com/organizations

import requests

# URL = "http://www.values.com/inspirational-quotes"
URL = "https://summerofcode.withgoogle.com/organizations"
r = requests.get(URL)
print(r.content.decode('utf-8'))
