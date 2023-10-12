import asyncio
import os
import psycopg2
from psycopg2 import sql
from car_parser.celeryconfig import app
from car_parser.parse import CollectCar
from config import DB_NAME, POSTGRES_USER


@app.task
def start_collect() -> None:
    client = CollectCar()
    asyncio.run(client.start_collect_links())


dump_dir = "../dumps"
os.makedirs(dump_dir, exist_ok=True)


@app.task
def dump_db() -> None:
    db_name = DB_NAME
    db_user = POSTGRES_USER
    output_file = os.path.join(dump_dir, f"db_dump_{db_name}.sql")

    try:
        conn = psycopg2.connect(database=db_name, user=db_user, password="postgres", host="db", port=5432)
        cursor = conn.cursor()

        with open(output_file, "w") as dump_file:
            cursor.copy_expert(sql.SQL("COPY (SELECT * FROM cars) TO STDOUT"), dump_file)

        conn.commit()
        cursor.close()
        conn.close()

        print(f"Succeeded {output_file}")
    except Exception as e:
        print(f"Error: {e}")
