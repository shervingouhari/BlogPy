# BlogPy

Welcome to **BlogPy**! This project showcases the use of various modern technologies and best practices. Below, you'll
find an overview of the technologies used and instructions for setting up and running the project.

## Technologies Used

-   **PostgreSQL**: A powerful, open-source object-relational database system.
-   **Django**: A high-level Python web framework that encourages rapid development and clean, pragmatic design.
-   **Nginx**: A high-performance HTTP server and reverse proxy.
-   **Certbot**: Used for obtaining and renewing SSL/TLS certificates from Let's Encrypt.
-   **Docker**: Used for containerizing the application and managing services with Docker Compose.

## Getting Started

### Prerequisites

-   **Python**: Ensure you have Python installed on your system. You can download it from
    [here](https://www.python.org/downloads/).
-   **Docker**: Ensure you have Docker installed on your system. You can download it from
    [here](https://www.docker.com/products/docker-desktop).
-   **Docker Compose**: Docker Compose should be installed alongside Docker.

### Downloading the Repository

To get started, download the project repository by clicking on the "Code" button above and selecting "Download ZIP".
Once downloaded, extract the contents to your desired location. Alternatively, you can clone the repository using Git:

```bash
git clone https://github.com/shervingouhari/BlogPy.git
```

After downloading or cloning, navigate to the project directory to proceed with setup.

### Setting Up Environment Variables

Create a `.env` file in the root directory of the project (next to `compose.yml`). The example below shows the structure
of this file. Modify the values as needed for your environment.

```env
DJANGO_SETTINGS_MODULE="core.settings.production"
SECRET_KEY="uu^s2g3m$&eh-4l8jzjb(1a2oq)v%o*g+g0fs!u(dmqu95)ngv"
ALLOWED_HOSTS="www.shervingouhari.info,shervingouhari.info"
SECRET_URL_PREFIX="supersecret"
GUNICORN_WORKERS="2"
DATABASE_URL="postgres://postgres:2500persianempire2500@postgres/BlogPy"
POSTGRES_USER="postgres"
POSTGRES_PASSWORD="2500persianempire2500"
POSTGRES_DB="BlogPy"
DOMAIN="shervingouhari.info"
EMAIL="shervingouhari@gmail.com"
GID="1000"
UID="1000"
```

### Explanation of Environment Variables

-   `DJANGO_SETTINGS_MODULE`: The settings module for Django. Check the available options in the `core.settings` folder.
-   `SECRET_KEY`: A secret key for Django used in cryptographic signing.
-   `ALLOWED_HOSTS`: A list of strings representing the host/domain names that the Django site can serve.
-   `SECRET_URL_PREFIX`: A secret prefix for sensitive URLs (e.g., admin interface).
-   `GUNICORN_WORKERS`: The number of worker processes for handling requests.
-   `DATABASE_URL`: The database connection URL.
-   `POSTGRES_USER`: The username for PostgreSQL.
-   `POSTGRES_PASSWORD`: The password for PostgreSQL.
-   `POSTGRES_DB`: The database name for PostgreSQL.
-   `DOMAIN`: The domain name for the application.
-   `EMAIL`: The email address used for Let's Encrypt notifications.
-   `GID`: The group ID to use in Docker containers.
-   `UID`: The user ID to use in Docker containers.

### Running the Application

Build and start the application in detached mode:

```bash
docker compose up --build --detach
```

After executing this command, you must wait for the certbot container to exit and then restart the nginx container for
the SSL/TLS certifications to be loaded:

```bash
docker compose restart nginx
```

### Using the Management Script

The `manage.py` script provides commands to manage the SSL/TLS certifications. Below are the available commands:

-   **Renew SSL/TLS Certificates**: Manually renew the certificates.

    Note that this will restart the nginx container as well.

```bash
python manage.py renew-cert
```

-   **Set Up Cron Job for Certificate Renewal**: Sets up a daily cron job to renew SSL/TLS certificates.

    Note that this will call the `renew-cert` command at midnight.

```bash
python manage.py renew-cert-cron
```

## License

This project is licensed under the MIT License. For more details, refer to the
[LICENSE](https://github.com/shervingouhari/BlogPy/blob/main/LICENSE.txt) file.

---

Thank you for exploring **BlogPy**! If you have any questions or suggestions, feel free to open an issue or contact me
at shervingouhari@gmail.com. Happy coding!
