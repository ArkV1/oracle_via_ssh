# ARM Macs
```
brew install colima
```

```
colima start --arch x86_64 --memory 4 --disk 60 --dns 8.8.8.8,8.8.4.4
```

# Build
```
docker build -t oracle-db-ssh .
```

# Run
```
docker run -d --name oracle-db-ssh -p 1521:1521 -p 5500:5500 -p 2222:22 oracle-db-ssh
```
