import civis
client = civis.APIClient()
# HTTP  GET /users/me
client.users.list_me()
