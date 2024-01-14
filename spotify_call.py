import requests

#endpoint_url = 'https://api.spotify.com/v1/artists/1w5Kfo2jwwIPruYS2UWh56?si=LUT_1-UcRHi9OGA89R5snw'
#endpoint_url = 'https://api.spotify.com/v1/me'
endpoint_url = 'https://api.spotify.com/v1/me/playlists'

file_path = '/Users/matillionuser/Desktop/python/admin/spotify_accesstoken.txt'
token_val = ''

with open(file_path, 'r') as text_file:
    token_val = text_file.read()

print('Token:',token_val)

#https://accounts.spotify.com/authorize?client_id=82de31b0e2464af88fd7ea4f4a568344&response_type=code&scope=streaming%20user-read-email%20playlist-read-private%20user-read-private&redirect_uri=https://localhost:8080


#headers = {
#    'Authorization': 'Bearer '+token_val
#}

# You can customize parameters as needed, e.g., time_range, limit, etc.
#params = {
#    'time_range': 'medium_term',
#    'limit': 10
#}

#response = requests.get(endpoint_url, headers=headers)

#print(response.text)

#if response.status_code == 200:
    # Request was successful
#    data = response.json()
    # Process the data as needed
#    print(data)
#else:
    # Request failed
#    print(f"Error: {response.status_code}, {response.text}")


def get_user_playlists(access_token, limit=10):
    # Spotify API endpoint for getting a list of a user's playlists
    endpoint_url = 'https://api.spotify.com/v1/me/playlists'

    # Headers with the access token
    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    # Parameters for the request, adjust as needed
    params = {
        'limit': limit
    }

    # Make the request to the Spotify API
    response = requests.get(endpoint_url, headers=headers, params=params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Extract and return the playlists from the response
        playlists = response.json()['items']
        return playlists
    else:
        # Print an error message if the request was not successful
        print(f"Error: {response.status_code}, {response.text}")
        return None

# Replace "your_access_token" with a valid access token
access_token = 'BQDhXMrl0qmZ02c-c5na6OLhxzsVABHheDN0c090d4mUrE2ZoIs5RX3bZX0MDaHrH9_YfGRjRuwTtva4_dfW6IopWZqELM8GqlnjZeP0u81RHL8pUd8b1AAKhX2A_3CtHW4AA9RpKjOr95HwkP1_c3A'

# Call the function to get the user's playlists
user_playlists = get_user_playlists(access_token)

# Print the user's playlists
if user_playlists:
    print("User's Playlists:")
    for index, playlist in enumerate(user_playlists, start=1):
        print(f"{index}. {playlist['name']}")
