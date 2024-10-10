# Use the official Oracle Database image as the base
FROM container-registry.oracle.com/database/free:latest

# Switch to root user to perform installations
USER root

# Update the package manager and install OpenSSH server and clients
RUN sed -i 's/yum-us-phoenix-1.oracle.com/yum.oracle.com/' /etc/yum/vars/ociregion && \
    dnf update -y && \
    dnf install -y openssh-server openssh-clients && \
    dnf clean all && \
    mkdir /var/run/sshd && \
    echo 'root:rootpassword' | chpasswd && \
    sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# Expose ports for Oracle and SSH
EXPOSE 1521 5500 22

# Switch back to oracle user
USER oracle

# Start both SSH and Oracle services
CMD ["/bin/sh", "-c", "sudo /usr/sbin/sshd && /bin/tns start"]
