import requests
URL = "https://serverdjango.herokuapp.com/app"
w = "1,2,5,7,4,8,1"
var = "5,8,5,6,7,-8,9"
PARAMS = {'w':w,'var':var}
r = requests.post(url= URL, data= PARAMS) 
data = r.json()

print(data)
