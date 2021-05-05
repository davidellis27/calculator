import psycopg2
import yaml


def db_postgresql_connect():
    """ Connect to the PostgreSQL database server """

    yaml_filename = "database_postgresql.yml"
    yaml_section = "postgresql"

    # read connection parameters
    try:
        with open(yaml_filename, "r") as ymlfile:
            params = yaml.load(ymlfile, Loader=yaml.FullLoader)

    except yaml.YAMLError as error:
        print("Error reading YAML file {} for section {}".format(yaml_filename, yaml_section))
        print(error)
        return -1

    # connect to the PostgreSQL server
    try:
        conn = psycopg2.connect(**params[yaml_section])
    except psycopg2.Error as error:
        print("Error while connecting to PostgreSQL")
        print(error)
        return -1

    return conn


def db_postgresql_close(db_conn):
    if db_conn is not None:
        db_conn.close()


def db_postgresql_select(db_conn, the_select):
    cur = db_conn.cursor()

    try:
        cur.execute(the_select)
    except psycopg2.Error as error:
        print(error)

    rows = cur.fetchall()
    rowcount = cur.rowcount
    db_conn.commit()
    cur.close()

    if rowcount == 0:
        return None
    else:
        return rows


def db_postgresql_update(db_conn, the_update):
    cur = db_conn.cursor()

    try:
        cur.execute(the_update)
    except psycopg2.Error as error:
        print(error)

    rowcount = cur.rowcount
    db_conn.commit()
    cur.close()

    return rowcount


def db_postgresql_insert(db_conn, the_insert):
    cur = db_conn.cursor()

    try:
        cur.execute(the_insert)
    except psycopg2.Error as error:
        print(error)

    rowcount = cur.rowcount
    db_conn.commit()
    cur.close()

    return rowcount
