import civis
client = civis.APIClient()
# HTTP  GET /users/me
print(client.users.list_me())
