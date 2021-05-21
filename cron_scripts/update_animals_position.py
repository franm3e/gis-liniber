import psycopg2

from cron_scripts import utils
from cron_scripts.models import Animal

# CONSULTAS
SQL_GET_ANIMALES = 'SELECT * FROM "Animal" WHERE "Activo" = True'
SQL_GET_POSICIONES = 'SELECT TOP 1 * FROM "Animal" WHERE '
SQL_GET_NACIMIENTOS = 'SELECT * FROM "Animal" WHERE "FechaNacimiento" IS NULL'

# OBJETOS GLOBALES
DATABASE = None


def main():
    inicializar_database()

    if DATABASE:
        gestionar_nacimientos()


def inicializar_database():
    global DATABASE
    try:
        DATABASE = psycopg2.connect(
            user="uuxtdvtzsqpoga",
            password="7a8f038d18569907b1db6207d11b07c01b39cf4e12dd41a16134179cc75aa18d",
            host="ec2-79-125-30-28.eu-west-1.compute.amazonaws.com",
            port="5432",
            database="d3fh48t96v7pn0"
        )

    except (ValueError, Exception):
        DATABASE = None
        utils.logger('e', 'No ha sido posible incializar la base de datos', str(ValueError), str(Exception))


def gestionar_nacimientos():
    with DATABASE.cursor() as cursor:
        cursor.execute(SQL_GET_NACIMIENTOS)
        for row in cursor:
            animal = Animal(*row)




if __name__ == "__main__":
    main()
