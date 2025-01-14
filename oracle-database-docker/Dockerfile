# Use the official Oracle Database image as the base
FROM container-registry.oracle.com/database/free:latest

# Switch to root user to perform installations
USER root

# Install SSH server and other necessary packages
RUN yum update -y && yum install -y openssh-server && yum clean all

# Set up SSH
RUN mkdir /var/run/sshd
RUN ssh-keygen -A
RUN echo 'root:your_password' | chpasswd

# Allow root login via SSH (Note: This is not recommended for production)
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

# Expose SSH port
EXPOSE 22 1521 5500

# Start SSH service and Oracle
CMD ["/usr/sbin/sshd", "-D"]

# Switch back to oracle user
USER oracle