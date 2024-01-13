import requests as r
import re
import json


file_path = '/Users/matillionuser/Desktop/python/admin/spotify_clientidsecret.json'

# Read the entire JSON content
with open(file_path, 'r') as json_file:
    data = json.load(json_file)

# Access specific elements in the JSON data
client_id = data.get('client_id')
client_secret = data.get('client_secret')

# Print the values
print(f"Client ID: {client_id}")
print(f"Client Secret: {client_secret}")

post_url = "https://accounts.spotify.com/api/token"

h = {
    "Content-Type": "application/x-www-form-urlencoded"
}

d = 'grant_type=client_credentials&client_id='+client_id+'&client_secret='+client_secret

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