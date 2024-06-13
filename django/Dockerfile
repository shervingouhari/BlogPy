FROM python:3.12.3-slim-bullseye
LABEL maintainer="Shervin Gouhari <shervingouhari@gmail.com>"
ARG GID=1000
ARG UID=1000
ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PATH=/django:$PATH
WORKDIR /django
COPY requirements.txt .
RUN apt-get update && \
    apt-get install -y gcc libpq-dev netcat && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --upgrade pip && \
    pip install -r requirements.txt && \
    apt-get purge -y --auto-remove gcc
COPY . .
RUN mkdir -p static media logs && \
    addgroup --gid $GID django && \
    adduser --uid $UID --gid $GID --disabled-password --gecos "" django && \
    chown -R django:django /django && \
    chmod -R 755 /django
USER django:django
EXPOSE 8000
CMD ["launch-django.sh"]
