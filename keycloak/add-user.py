import requests

# Configuration
keycloak_server = "http://<keycloak-server>"
client_id = "<your-client-id>"
client_secret = "<your-client-secret>"
realm_name = "<your-realm-name>"
username = "<new-username>"
email = "<new-user-email>"
first_name = "<new-user-first-name>"
last_name = "<new-user-last-name>"
password = "<new-user-password>"

# Get access token
token_url = f"{keycloak_server}/auth/realms/master/protocol/openid-connect/token"
token_data = {
            'grant_type': 'client_credentials',
                'client_id': client_id,
                    'client_secret': client_secret
                    }
token_response = requests.post(token_url, data=token_data)
access_token = token_response.json().get('access_token')

# Check if the token was obtained
if not access_token:
        print("Failed to obtain access token.")
            exit(1)

            # Create a new user
            user_url = f"{keycloak_server}/auth/admin/realms/{realm_name}/users"
            headers = {
                        'Authorization': f'Bearer {access_token}',
                            'Content-Type': 'application/json'
                            }
            user_data = {
                        'username': username,
                          

