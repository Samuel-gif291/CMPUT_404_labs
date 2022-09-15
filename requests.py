"This version of python prints the version of the requests library"

import requests
temp = requests.get("")
print(temp)
#print(requests.__version__)
