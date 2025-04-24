import os
from configparser import ConfigParser
from dotenv import dotenv_values


def load_config(filename='database.ini', section='postgresql') -> dict:
    config_directory = os.path.dirname(__file__)
    filename = config_directory + '/' + filename

    parser = ConfigParser()
    parser.read(filename)

    config = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            config[param[0]] = param[1]
    else:
        raise Exception(f'Section {section} not found in the {filename} file')
    return config


DB_CONFIG = load_config()

args_env = dotenv_values()
JWT_SECRET = args_env['JWT_SECRET']
JWT_REFRESH_SECRET = args_env['REFRESH_JWT_SECRET']
ALGORITHM = args_env['ALGORITHM']
ACCESS_TOKEN_EXPIRE_MINUTES = int(args_env['ACCESS_TOKEN_EXPIRE_MINUTES'])
REFRESH_TOKEN_EXPIRE_MINUTES = int(args_env['REFRESH_TOKEN_EXPIRE_MINUTES'])