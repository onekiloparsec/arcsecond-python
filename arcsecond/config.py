import os
from configparser import SafeConfigParser


def config_file_path():
    return os.path.expanduser('~/.arcsecond.ini')


def config_file_exists():
    path = config_file_path()
    return os.path.exists(path) and os.path.isfile(path)


def config_file_is_valid():
    if not config_file_exists():
        return False
    config = SafeConfigParser()
    config.read(config_file_path())
    return config['main'].get('api_key')


def config_file_save_api_key(api_key, username, debug=False):
    config = SafeConfigParser()
    config.read(config_file_path())
    section = 'debug' if debug else 'main'
    if not section in config.keys():
        config.add_section(section)
    config.set(section, 'username', username)
    config.set(section, 'api_key', api_key)
    with open(config_file_path(), 'w') as f:
        config.write(f)


def config_file_read_key(key):
    config = SafeConfigParser()
    config.read(config_file_path())
    return config['main'].get(key)


def config_file_read_api_key():
    return config_file_read_key('api_key')


def config_file_read_username():
    return config_file_read_key('username')