"This version of python prints the version of the requests library"

import requests
temp = requests.get("https://raw.githubusercontent.com/Samuel-gif291/CMPUT_404_labs/main/requests.py")
print(temp.text)
