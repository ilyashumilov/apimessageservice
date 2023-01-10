import requests

url = 'http://127.0.0.1:8000/api/v1/messages/'
headers = {'Authorization': 'Bearer 15c94c2f8b3af674174959e346b2ec88781a2956'}
r = requests.get(url, headers=headers, data={"message":"new"})
print(r.text)