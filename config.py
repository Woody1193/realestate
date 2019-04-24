from configparser import ConfigParser

class Configuration:

    def __init__(self, filename: str):
        config = ConfigParser()
        config.read(filename)

        for section in config.sections():
            for key in config[section]:
                setattr(self, key, config[section][key])