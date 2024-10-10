# Build
docker build -t oracle-db-ssh .

# Run
docker run -d --name oracle-db-ssh -p 1521:1521 -p 5500:5500 -p 2222:22 oracle-db-ssh
