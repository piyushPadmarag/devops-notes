# #!/bin/bash

# Variables
KEYCLOAK_SERVER="http://localhost:port"
ADMIN_USERNAME="user"
ADMIN_PASSWORD="sss"
REALM_NAME="piyush-realm"

# Obtain an admin access token
TOKEN=$(curl -s -X POST "$KEYCLOAK_SERVER/realms/master/protocol/openid-connect/token" \
    -H "Content-Type: application/x-www-form-urlencoded" \
    -d "client_id=test-client" \
    -d "client_secret=secret" \
    -d "grant_type=client_credentials" | jq -r '.access_token')


# Check if TOKEN is not empty
if [ -z "$TOKEN" ]; then
  echo "Failed to obtain access token."
  exit 1
fi

# Create a new realm
curl -X POST "$KEYCLOAK_SERVER/auth/admin/realms" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $TOKEN" \
    -d "{
          \"id\": \"$REALM_NAME\",
          \"realm\": \"$REALM_NAME\",
          \"enabled\": true
        }"

echo "Realm '$REALM_NAME' created successfully."
