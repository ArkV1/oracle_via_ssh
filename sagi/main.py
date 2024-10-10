import paramiko
import cx_Oracle
import gssapi
import socket
import os

def create_ssh_tunnel(ssh_host, ssh_port, ssh_username, db_host, db_port):
    # Create SSH client
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Connect to SSH server
    ssh.connect(ssh_host, port=ssh_port, username=ssh_username)

    # Create SSH tunnel
    local_port = ssh.get_transport().request_port_forward('', 0, db_host, db_port)

    return ssh, local_port

def connect_to_oracle_with_kerberos(username, service_name, local_port):
    # Set up Kerberos authentication
    os.environ['KRB5CCNAME'] = '/tmp/krb5cc_' + str(os.getuid())

    # Create cx_Oracle connection string
    dsn = cx_Oracle.makedsn('localhost', local_port, service_name=service_name)

    # Connect to Oracle database using Kerberos authentication
    connection = cx_Oracle.connect(
        user=username,
        dsn=dsn,
        auth_mode=cx_Oracle.SYSAUTH,
        externalauth=True
    )

    return connection

def connect_to_oracle_without_kerberos(username, password, service_name, local_port):
    # Create cx_Oracle connection string
    dsn = cx_Oracle.makedsn('localhost', local_port, service_name=service_name)

    # Connect to Oracle database using password authentication
    connection = cx_Oracle.connect(
        user=username,
        password=password,
        dsn=dsn
    )

    return connection

def main():
    # SSH connection details
    ssh_host = 'your_ssh_host'
    ssh_port = 2222  # Use the exposed SSH port from the Docker container
    ssh_username = 'root'

    # Oracle database details
    db_host = 'localhost'  # Use 'localhost' since we're connecting through SSH tunnel
    db_port = 1521
    service_name = 'your_service_name'
    username = 'your_username'

    try:
        # Create SSH tunnel
        ssh, local_port = create_ssh_tunnel(ssh_host, ssh_port, ssh_username, db_host, db_port)

        # Try connecting with Kerberos
        try:
            connection = connect_to_oracle_with_kerberos(username, service_name, local_port)
            print("Connected to Oracle database using Kerberos authentication")
        except Exception as e:
            print(f"Kerberos authentication failed: {e}")
            print("Falling back to password authentication")

            # If Kerberos fails, try connecting without Kerberos
            password = input("Enter your database password: ")
            connection = connect_to_oracle_without_kerberos(username, password, service_name, local_port)
            print("Connected to Oracle database using password authentication")

        # Use the connection to execute queries
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM dual")
        result = cursor.fetchone()
        print(f"Query result: {result}")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close connections
        if 'connection' in locals():
            connection.close()
        if 'ssh' in locals():
            ssh.close()

if __name__ == "__main__":
    main()