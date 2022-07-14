Docker:
docker-compose up --build
docker-compose up


aerich migrations:
docker-compose exec backend aerich init -t app.db.TORTOISE_ORM

docker-compose exec backend aerich init-db

docker-compose exec backend aerich migrate
docker-compose exec backend aerich upgrade