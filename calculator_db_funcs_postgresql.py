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
