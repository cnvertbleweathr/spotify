import requests as r
import re
import json


# Read the entire JSON content
file_path = '/Users/matillionuser/Desktop/python/admin/spotify_clientidsecret.json'
with open(file_path, 'r') as json_file:
    data = json.load(json_file)

# Access specific elements in the JSON data
client_id = data.get('client_id')
client_secret = data.get('client_secret')
scope= '''streaming%20user-read-email%20user-top-read%20user-read-private&redirect_uri=https://example.com/callback'''

# Print the values
print(f"\nClient ID: {client_id}")
print(f"\nClient Secret: {client_secret}")


# api post to retrieve token
post_url = "https://accounts.spotify.com/api/token"
h = {
    "Content-Type": "application/x-www-form-urlencoded"
}
d = f"grant_type=client_credentials&client_id={client_id}&client_secret={client_secret}&scope={scope}"
    

token_r = r.post(post_url,
                  headers=h,
                  data=d
                  )

response = token_r.text
print('\nResponse: ',response)


#parse response for token
token_val = re.search('''"access_token":"(.*)","token_type":"Bearer","expires_in":3600,"scope":"streaming user-read-email user-top-read user-read-private"}''', response)
print('\nToken from API: ',token_val.group(1))
token_val = token_val.group(1)


#write token value to local machine, in spotify_accesstoken
file_path = '/Users/matillionuser/Desktop/python/admin/spotify_accesstoken.txt'

with open(file_path, 'w') as out:
    out.write(token_val)

with open(file_path, 'r') as text_file:
    content = text_file.read()
    print('\nToken in spotify_accesstoken: ',content)
