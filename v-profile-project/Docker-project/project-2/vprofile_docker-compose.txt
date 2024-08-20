# Create directory
mkdir compose
cd compose/

# docker compose command
docker compose

# Download docker-compos.yml file for vprofile project
wget https://raw.githubusercontent.com/devopshydclub/vprofile-project/docker/compose/docker-compose.yml
ls
vim docker-compose.yml

# Bring up all the containers
docker compose up -d
docker compose ps
ip addr show
docker compose down

# Go to browser and enter VMIP:80
