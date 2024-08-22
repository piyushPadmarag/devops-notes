KEYCLOAK_SERVER="http://localhost:port"


TOKEN=$(curl -s -X POST "$KEYCLOAK_SERVER/realms/master/protocol/openid-connect/token" \
    -H "Content-Type: application/x-www-form-urlencoded" \
    -d "client_id=test-client" \
    -d "client_secret=secret" \
    -d "grant_type=client_credentials" | jq -r '.access_token')



