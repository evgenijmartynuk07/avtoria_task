# avtoria_task


Information gathering starts at 12:00.
Database dump occurs at 00:00.

```shell

python -m venv venv
source venv/bin/activate

create .env based on .env.sample
change sqlalchemy.url in alembic.ini

run: docker build -t backend .
run: docker-compose up
```



