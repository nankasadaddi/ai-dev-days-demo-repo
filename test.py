import requests

DATABRICKS_URL = 'https://adb-541623100598197.17.azuredatabricks.net'
TOKEN = 'dapie5fdc595f8cfcf8e2ba5c5d01009b3cf'

response = requests.get(
    f'{DATABRICKS_URL}/api/2.0/repos',
    headers={'Authorization': f'Bearer {TOKEN}'}
)

print('Status:', response.status_code)
print('Response:', response.json())

