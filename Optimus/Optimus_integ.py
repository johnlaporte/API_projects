import base64
from altapay import utils
import json
import requests
'''
def create_lead(token):
  url = "https://optimus-api.io/createlead"
  payload = '{"tracking": {"aff_id": "2313","funnelname": "Funnel","source": "source"},"lead": {"fname":"TEST","lname":"TEST","email":"testx645333@gmail.com","phone":"16135440449","country":"CA"}}'
  #payload = '{\r\n    \"tracking\": {\r\n        \"aff_id\": \"2313\",\r\n        \"funnelname\": \"Funnel\",\r\n        \"source\": \"source\", \r\n    },\r\n    \"lead\": {\r\n        \"fname\":\"TEST\",\r\n        \"lname\":\"TEST\",\r\n        \"email\":\"testx645334@gmail.com\",\r\n        \"phone\":\"16135440450\",\r\n        \"country\":\"CA\"\r\n    }\r\n}'
  #payload = {"tracking":{"aff_id":"2313","funnelname":"Funnel","source":"source"},"lead":{"fname":"TEST","lname":"TEST","email":"testx645340@gmail.com","phone":"16135440450","country":"CA"}}
  str_with_token = 'TraffleBearer ' + token
  print()
  headers = {
    'TraffleAuthorization': 'TraffleBearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiJ9.eyJpc3MiOiJ0cmFmZmxlIiwiYXVkIjoicGFydG5lcnMiLCJpYXQiOjE2NjMyNDM1MDMsIm5iZiI6MTY2MzI0MzUwMywiZXhwIjoxNjYzMzI5OTAzLCJhcHBfa2V5IjoiZmtnVSFpOVRranlLbm1PMXRYb0JwVzczMk02dkMzUTRjZTU1MUZzc3NPJDI0NSFQI2lZRHJ0Y1htTXhrYkc5NkAxaDNYd3ptWDlWUU9RQ3FoeSIsImxvY2tlciI6IjdJT3h1NHBsc2lUVXpmaSNoT25PNjVMVVI4IU1JNzlxQnpiMG9IM29zUW8zWmpWMFVUcXkhQERiaHpJWmlVYSNlQHA1cEAlTSIsImtleSI6ImtIWHAtY2pWTzR0d25NNkRjVFRNcU53X2Y4bFprRzBKIiwidWlkIjo3MDIsInVzZXJuYW1lIjoiMTIxOF9vTnFnZUxrbyJ9.',
    'Content-Type': 'application/json'
  }
print(payload) #for checking

headers = {
  'TraffleAuthorization': 'TraffleBearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiJ9.eyJpc3MiOiJ0cmFmZmxlIiwiYXVkIjoicGFydG5lcnMiLCJpYXQiOjE2NjMyNDM1MDMsIm5iZiI6MTY2MzI0MzUwMywiZXhwIjoxNjYzMzI5OTAzLCJhcHBfa2V5IjoiZmtnVSFpOVRranlLbm1PMXRYb0JwVzczMk02dkMzUTRjZTU1MUZzc3NPJDI0NSFQI2lZRHJ0Y1htTXhrYkc5NkAxaDNYd3ptWDlWUU9RQ3FoeSIsImxvY2tlciI6IjdJT3h1NHBsc2lUVXpmaSNoT25PNjVMVVI4IU1JNzlxQnpiMG9IM29zUW8zWmpWMFVUcXkhQERiaHpJWmlVYSNlQHA1cEAlTSIsImtleSI6ImtIWHAtY2pWTzR0d25NNkRjVFRNcU53X2Y4bFprRzBKIiwidWlkIjo3MDIsInVzZXJuYW1lIjoiMTIxOF9vTnFnZUxrbyJ9.',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=utils.http_build_query(payload))
print(response)
print(response.text)
'''
'''
#payload = '{"tracking":{"aff_id":"2313","funnelname":"QUANTUM-AI","aff_sub":"test","aff_sub2":"test2","aff_sub3": "test3","aff_sub4": "test4","aff_sub5": "test5"},"lead":{"fname":"TEST","lname":"TEST","email":"testtest103@gmail.com","phone":"4407087939145","country":"CA"}}'
#url1 = "https://optimus-api.io/introduceyourself/login"
url = "https://optimus-api.io/introduceyourself/login"
username = '1218_oNqgeLko'
password = 'x#9RH$UZIji7e!$J'


payload={}
headers = {
  'Authorization': 'Basic {MTIxOF9vTnFnZUxrbzp4IzlSSCRVWklqaTdlISRK}'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
'''
import requests
import json

url = "https://optimus-api.io/deposits"

payload = json.dumps({
  "filter": {
    "from": "2020-09-15 10:20:32",
    "to": "2020-09-15 16:20:32"
  }
})
headers = {
  'TraffleAuthorization': 'TraffleBearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiJ9.eyJpc3MiOiJ0cmFmZmxlIiwiYXVkIjoicGFydG5lcnMiLCJpYXQiOjE2NjMyNDYwNDcsIm5iZiI6MTY2MzI0NjA0NywiZXhwIjoxNjYzMzMyNDQ3LCJhcHBfa2V5IjoiZmtnVSFpOVRranlLbm1PMXRYb0JwVzczMk02dkMzUTRjZTU1MUZzc3NPJDI0NSFQI2lZRHJ0Y1htTXhrYkc5NkAxaDNYd3ptWDlWUU9RQ3FoeSIsImxvY2tlciI6IjdJT3h1NHBsc2lUVXpmaSNoT25PNjVMVVI4IU1JNzlxQnpiMG9IM29zUW8zWmpWMFVUcXkhQERiaHpJWmlVYSNlQHA1cEAlTSIsImtleSI6ImtIWHAtY2pWTzR0d25NNkRjVFRNcU53X2Y4bFprRzBKIiwidWlkIjo3MDIsInVzZXJuYW1lIjoiMTIxOF9vTnFnZUxrbyJ9.',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
