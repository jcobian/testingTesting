import civis
from civis.base import Endpoint
Endpoint._base_url = 'https://api-staging.civisanalytics.com/'
client = civis.APIClient()
print(client.users.list_me()['name'])
