import requests

#endpoint_url = 'https://api.spotify.com/v1/artists/1w5Kfo2jwwIPruYS2UWh56?si=LUT_1-UcRHi9OGA89R5snw'
#endpoint_url = 'https://api.spotify.com/v1/me'
endpoint_url = 'https://api.spotify.com/v1/me/top/artists'

file_path = '/Users/matillionuser/Desktop/python/admin/spotify_accesstoken.txt'
token_val = ''

with open(file_path, 'r') as text_file:
    token_val = text_file.read()
    print('Token:',token_val)

#https://accounts.spotify.com/authorize?client_id=7199d571ed484bd7912f30c26482bbeb&response_type=code&scope=streaming%20user-read-email%20user-read-private&redirect_uri=https://example.com/callback


headers = {
    'Authorization': 'Bearer  '+token_val
}

# You can customize parameters as needed, e.g., time_range, limit, etc.
#params = {
#    'time_range': 'medium_term',
#    'limit': 10
#}

response = requests.get(endpoint_url, headers=headers)

print(response.text)

if response.status_code == 200:
    # Request was successful
    data = response.json()
    # Process the data as needed
    print(data)
else:
    # Request failed
    print(f"Error: {response.status_code}, {response.text}")

    