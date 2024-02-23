import requests, json
url = "https://api-basketball.p.rapidapi.com/standings" 
querystring = {"league":"12","season":"2023-2024"}
headers = { 	"X-RapidAPI-Key": "8bfe3d3abemsh75b3d7e3f7e6723p159819jsn9ac0c169c73e", 	"X-RapidAPI-Host": "api-basketball.p.rapidapi.com" } 
response = requests.get(url, headers=headers, params=querystring)

with open('basketball.json','w') as file:
  json.dump(response.json(), file, indent = 2)

#print(response.json())
