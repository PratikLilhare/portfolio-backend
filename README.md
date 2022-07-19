# Portfolio Backend

<p align="center">
    <img src="https://img.shields.io/pypi/pyversions/fastapi.svg?color=%2334D058" alt="Supported Python versions">
</p>


## Installation and starting up:
```bash
docker-compose up --build
docker-compose up
```

---

## Check server

Upon successful execution, you will see something like:

```bash
backend_1       | INFO:     Waiting for application shutdown.
backend_1       | INFO:     Application shutdown complete.
backend_1       | INFO:     Finished server process [35]
backend_1       | INFO:     Started server process [36]
backend_1       | INFO:     Waiting for application startup.
backend_1       | INFO:     Application startup complete.
```

Open your browser at <a href="http://127.0.0.1:8080/docs" class="external-link" target="_blank">http://127.0.0.1:8080/docs</a>

You will see the documented APIs

---


## Running migrations:
```bash
docker-compose exec backend aerich init -t app.db.TORTOISE_ORM
docker-compose exec backend aerich init-db
docker-compose exec backend aerich migrate
```

---

## Deployment

### Nginx:


#### Installation
```bash
sudo apt-get install nginx
```

#### Create configuration file for nginx
```bash
sudo vi /etc/nginx/sites-enabled/portfolio
```

#### Add configuration for nginx
```conf
server {
    listen 80;
    server_name <PUBLIC_IP>;
    location / {
        proxy_pass http://127.0.0.1:8000;
    }
}
```

#### Restart nginx and docker
```
sudo service nginx restart
sudo service docker restart
sudo docker-compose up
```