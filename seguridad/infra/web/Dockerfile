FROM php:8.2-fpm-alpine

RUN apk add --no-cache nginx supervisor curl bash

COPY nginx.conf /etc/nginx/nginx.conf
COPY supervisord.conf /etc/supervisord.conf
COPY html/ /var/www/html/

# Place flag3 outside web root (only reachable after RCE)
COPY flag3.txt /opt/flag3.txt
RUN chmod 644 /opt/flag3.txt

# nginx access log readable by php-fpm worker (www-data)
RUN mkdir -p /var/log/nginx \
    && touch /var/log/nginx/access.log /var/log/nginx/error.log \
    && chmod 644 /var/log/nginx/access.log \
    && chown -R www-data:www-data /var/www/html

# Enable directory listing for /backup
EXPOSE 80
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]
