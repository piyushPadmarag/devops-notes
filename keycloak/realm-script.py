import requests

# Configuration
keycloak_server = "http://<keycloak-server>"
client_id = "<your-client-id>"
client_secret = "<your-client-secret>"
realm_name = "<realm-name>"
display_name = "<display-name>"

# Get access token
token_url = f"{keycloak_server}/auth/realms/master/protocol/openid-connect/token"
token_data = {
            'grant_type': 'client_credentials',
                'client_id': client_id,
                    'client_secret': client_secret
                    }
token_response = requests.post(token_url, data=token_data)
access_token = token_response.json().get('access_token')

# Create realm
realm_url = f"{keycloak_server}/auth/admin/realms"
headers = {
            'Authorization': f'Bearer {access_token}',
                'Content-Type': 'application/json'
                }
realm_data = {
            'id': realm_name,
                'realm': realm_name,
                    'enabled': True,
                        'displayName': display_name
                        }
response = requests.post(realm_url, headers=headers, json=realm_data)

if response.status_code == 201:
        print("Realm created successfully!")
    else:
            print(f"Failed to create realm: {response.status_code} - {response.text}")

