FROM nginx:1.26.1
LABEL maintainer="Shervin Gouhari <shervingouhari@gmail.com>"
RUN apt-get update && \
    apt-get install -y openssl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
COPY options-ssl-nginx.conf /etc/nginx/conf.d/ssl/options-ssl-nginx.conf
COPY default.conf default-ssl.conf /etc/nginx/templates/
COPY launch-nginx.sh /usr/local/bin/launch-nginx.sh
RUN chmod +x /usr/local/bin/launch-nginx.sh && \
    unlink /var/log/nginx/access.log && \
    unlink /var/log/nginx/error.log
EXPOSE 80 443
CMD ["launch-nginx.sh"]
