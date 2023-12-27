from configparser import ConfigParser

def Read_config(section, key):
    config=ConfigParser()
    config.read(".\\config\\config.ini")
    return config.get(section, key)

