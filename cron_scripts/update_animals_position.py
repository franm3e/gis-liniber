import datetime
import os

import psycopg2
import shapely.geometry
import shapely.wkb
from environ import environ

from cron_scripts import utils
from cron_scripts.models import *

# CONSULTAS
SQL_GET_ANIMALES = 'SELECT * FROM "Animal" WHERE "Activo" = True'
SQL_GET_POSICIONES = 'SELECT TOP 1 * FROM "Animal" WHERE '
SQL_GET_NACIMIENTOS = 'SELECT * FROM "v_Animal" WHERE "FechaNacimiento" IS NULL'
SQL_GET_AREA_NACIMIENTO = 'SELECT * FROM "Area_Distribucion" WHERE "Id" = {animal_area_id}'
SQL_INSERT_NACIMIENTO = 'INSERT INTO "Posicion"("Fecha", "Latitud", "Longitud", "geom", "Animal") VALUES (%(fecha)s, %(latitud)s, %(longitud)s, %(geom)s::geometry, %(animal)s) RETURNING "Id";'

# OBJETOS GLOBALES
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATABASE = None


def main():
    inicializar_database()

    if DATABASE:
        gestionar_nacimientos()


def inicializar_database():
    global DATABASE
    try:
        env = environ.Env()
        environ.Env.read_env(env_file=os.path.join(BASE_DIR, '.env'))

        DATABASE = psycopg2.connect(
            user=env('DATABASE_USER'),
            password=env('DATABASE_PASSWORD'),
            host=env('DATABASE_HOST'),
            port=env('DATABASE_PORT'),
            database=env('DATABASE_NAME')
        )
    except (ValueError, Exception):
        DATABASE = None
        utils.logger('e', 'No ha sido posible incializar la base de datos', ValueError, Exception)


def gestionar_nacimientos():
    with DATABASE.cursor() as cursor:
        cursor.execute(SQL_GET_NACIMIENTOS)
        for row in cursor:
            animal = AnimalView(*row)
            cursor.execute(SQL_GET_AREA_NACIMIENTO.format(animal_area_id=animal.area))

            insert_cursor = DATABASE.cursor()
            for row in cursor:
                area_distribucion = AreaDistribucion(*row)
                punto_nacimiento = utils.get_random_point_in_polygon(shapely.wkb.loads(area_distribucion.geom, hex=True))

                insert_cursor.execute(
                    SQL_INSERT_NACIMIENTO,
                    {'geom': punto_nacimiento.wkb_hex, 'fecha': str(datetime.datetime.now()), 'latitud': str(punto_nacimiento.y), 'longitud': str(punto_nacimiento.y), 'animal': str(animal.id)}
                )

            insert_cursor.close()
        cursor.close()
    DATABASE.commit()


if __name__ == "__main__":
    main()
