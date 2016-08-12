import civis
client = civis.APIClient()
print(client.users.list_me()['name'])
