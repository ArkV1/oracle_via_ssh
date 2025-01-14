# ARM Macs
```
brew install colima
```

```
colima start --arch x86_64 --memory 4 --disk 60
```

# Build
```
docker build -t oracle-database-ssh .
```

# Run
```
docker run -d -p 22:22 -p 1521:1521 -p 5500:5500 \
  -e ORACLE_PWD=YourStrongPassword \
  -e ORACLE_CHARACTERSET=AL32UTF8 \
  --name oracle-db-ssh oracle-database-ssh
```

# SSH Access
To SSH into the container:
```
ssh root@localhost -p 22
```
Note: Replace 'localhost' with the appropriate IP if running on a remote machine.

# Alternative Access (without SSH)
You can also access the container's shell directly using Docker:
```
docker exec -it oracle-db-ssh /bin/bash
```

# Environment Variables
When running the container, you can set the following environment variables:

- `ORACLE_PWD`: Set the password for the SYS, SYSTEM, and PDBADMIN accounts.
- `ORACLE_CHARACTERSET`: Set the character set for the database (default is AL32UTF8).

Example:
```
docker run -d -p 22:22 -p 1521:1521 -p 5500:5500 \
  -e ORACLE_PWD=YourStrongPassword \
  -e ORACLE_CHARACTERSET=AL32UTF8 \
  --name oracle-db-ssh oracle-database-ssh
```

# Connecting to the Database
After the container is running, you can connect to the database using SQL*Plus:

```
docker exec -it oracle-db-ssh sqlplus sys/YourStrongPassword@//localhost:1521/FREE as sysdba
```

Replace 'YourStrongPassword' with the password you set in the ORACLE_PWD environment variable.
