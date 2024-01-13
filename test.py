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

#file_path = '/Users/matillionuser/Desktop/python/admin/spotify_clientidsecret.txt'

#with open(file_path, 'r') as text_file:
#    content = text_file.read()
    #print(content)


#print (content[0])