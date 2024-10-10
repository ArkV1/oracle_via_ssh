# Use the official Oracle Database image as the base
FROM container-registry.oracle.com/database/free:latest

# Switch to root user to perform installations
USER root

# Update package manager and install OpenSSH server
RUN dnf config-manager --add-repo=https://yum.oracle.com/repo/OracleLinux/OL8/baseos/latest/x86_64 && \
    dnf config-manager --add-repo=https://yum.oracle.com/repo/OracleLinux/OL8/appstream/x86_64 && \
    dnf install -y --nogpgcheck openssh-server && \
    dnf clean all && \
    mkdir -p /var/run/sshd && \
    echo 'root:rootpassword' | chpasswd && \
    sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# Expose ports for Oracle and SSH
EXPOSE 1521 5500 22

# Switch back to oracle user
USER oracle

# Start both SSH and Oracle services
CMD ["/bin/sh", "-c", "sudo /usr/sbin/sshd && /bin/tns start"]
