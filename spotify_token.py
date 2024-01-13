import requests as r
import re

post_url = "https://accounts.spotify.com/api/token"

h = {
    "Content-Type": "application/x-www-form-urlencoded"
}

d = 'grant_type=client_credentials&client_id=7199d571ed484bd7912f30c26482bbeb&client_secret=e431e476019c4927a6a7329ad8b79dfa'

token_r = r.post(post_url,
                  headers=h,
                  data=d
                  )

response = token_r.text
print('response: ',response)

token_val = re.search('''"access_token":"(.*)","token_type":"Bearer","expires_in":3600}''', response)
print(token_val.group(1))
token_val = token_val.group(1)


with open('token_val.csv', 'w') as out:
    out.write(token_val)