import requests
import json 

url = "https://openapi.naver.com/v1/search/news?"
clientid = "[Client ID]"
clientSecret ="[Client Secret]"
queryString ="query" + "검색어"
header = {
	"X-Naver-Client-id" : clientid
	"X-Naver-Client-secret" : clientSecret
} 

r = requests.get(url + queryString, headers=header)
print(json.loads(r.text))
