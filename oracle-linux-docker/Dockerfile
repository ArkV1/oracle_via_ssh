# Use Oracle Linux 8 as the base image
FROM oraclelinux:8

# Switch to root user to perform installations
USER root

# Update package manager and install OpenSSH server and Oracle Database prerequisites
RUN dnf update -y && \
    dnf install -y dnf-utils && \
    dnf config-manager --add-repo=https://yum.oracle.com/repo/OracleLinux/OL8/baseos/latest/x86_64 && \
    dnf config-manager --add-repo=https://yum.oracle.com/repo/OracleLinux/OL8/appstream/x86_64 && \
    dnf install -y --nogpgcheck openssh-server && \
    dnf clean all && \
    mkdir -p /var/run/sshd && \
    echo 'root:rootpassword' | chpasswd && \
    sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# Expose ports for Oracle and SSH
EXPOSE 1521 5500 22

# Create oracle user (created by oracle-database-preinstall-19c, but we'll set it explicitly)
RUN useradd -m -s /bin/bash oracle

# Switch to oracle user
USER oracle

# Set up environment variables for Oracle Database
ENV ORACLE_BASE=/opt/oracle \
    ORACLE_HOME=/opt/oracle/product/19c/dbhome_1 \
    PATH=$PATH:/opt/oracle/product/19c/dbhome_1/bin

# Create necessary directories
RUN mkdir -p $ORACLE_BASE && \
    mkdir -p $ORACLE_HOME

# Note: You'll need to add steps here to download and install Oracle Database software

# Start both SSH and Oracle services
CMD ["/bin/sh", "-c", "sudo /usr/sbin/sshd && echo 'Oracle Database should be started here'"]