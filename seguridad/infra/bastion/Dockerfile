FROM debian:bookworm-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
        openssh-server sudo curl ca-certificates iproute2 procps \
    && rm -rf /var/lib/apt/lists/*

# Crear usuario jdev (password se inyecta abajo)
RUN useradd -m -s /bin/bash jdev \
    && echo 'jdev:qwerty123' | chpasswd \
    && mkdir -p /var/run/sshd

# sudoers — jdev puede ejecutar `find` como root sin password (GTFOBin)
RUN echo 'jdev ALL=(ALL) NOPASSWD: /usr/bin/find' > /etc/sudoers.d/jdev \
    && chmod 440 /etc/sudoers.d/jdev

# Configuración SSH — permitir login por password
RUN sed -i 's/^#\?PasswordAuthentication.*/PasswordAuthentication yes/' /etc/ssh/sshd_config \
    && sed -i 's/^#\?PermitRootLogin.*/PermitRootLogin no/' /etc/ssh/sshd_config

# Token de la bóveda — sólo root puede leerlo
RUN mkdir -p /root \
    && echo 'tok_h3l1c3_n3gr4_8a3f2c91' > /root/.vault_token \
    && chmod 600 /root/.vault_token

# Bienvenida con pista para el alumno
COPY welcome.txt /home/jdev/welcome.txt
RUN chown jdev:jdev /home/jdev/welcome.txt && chmod 644 /home/jdev/welcome.txt

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D", "-e"]
