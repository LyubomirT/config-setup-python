import json
import yaml
import xml.etree.ElementTree as ET
import configparser

class ConfigSetup:
    def __init__(self):
        self.config = {}

    def set(self, key, value):
        """
        Set a value in the config, will be temporarily stored.
        """
        self.config[key] = value

    def get(self, key):
        """
        Get a value from the config, may be temporarily stored.
        """
        return self.config.get(key)

    def clear(self):
        """
        Clears the config, removes all values received using set() or get(), unless they are stored.
        """
        self.config = {}

    def save(self, filename, format):
        """
        Saves the config to a file with the selected format.
        """
        if format == 'json':
            with open(f'{filename}.json', 'w') as f:
                json.dump(self.config, f)
        elif format == 'yaml':
            with open(f'{filename}.yaml', 'w') as f:
                yaml.dump(self.config, f, default_flow_style=False)
        elif format == 'xml':
            root = ET.Element('config')
            for key, value in self.config.items():
                node = ET.SubElement(root, key)
                node.text = str(value)
            tree = ET.ElementTree(root)
            tree.write(f'{filename}.xml')
        elif format == 'ini':
            config_parser = configparser.ConfigParser()
            config_parser.read_dict(self.config)
            with open(f'{filename}.ini', 'w') as f:
                config_parser.write(f)
        elif format == 'cfg':
            config_parser = configparser.ConfigParser()
            config_parser.read_dict(self.config)
            with open(f'{filename}.cfg', 'w') as f:
                config_parser.write(f)

    def load(self, file):
        """
        Loads a config file from a selected directory.
        """
        with open(file, 'r') as f:
            extension = file.split('.')[-1]
            if extension == 'json':
                self.config = json.load(f)
            elif extension in ['yaml', 'yml']:
                self.config = yaml.load(f, Loader=yaml.FullLoader)
            elif extension == 'xml':
                tree = ET.parse(f)
                root = tree.getroot()
                self.config = {elem.tag: elem.text for elem in root}
            elif extension == 'ini':
                config_parser = configparser.ConfigParser()
                config_parser.read_file(f)
                self.config = dict(config_parser.items())
            elif extension == 'cfg':
                config_parser = configparser.ConfigParser()
                config_parser.read_file(f)
                self.config = dict(config_parser.items())

    def validate(self, data, format):
        """
        Validates the provided data by checking if it matches the selected format.
        """
        if format == 'json':
            try:
                json.loads(data)
                return True
            except ValueError:
                return False
        elif format == 'yaml':
            try:
                yaml.load(data, Loader=yaml.FullLoader)
                return True
            except yaml.YAMLError:
                return False
        elif format == 'xml':
            try:
                ET.fromstring(data)
                return True
            except ET.ParseError:
                return False
        elif format == 'ini':
            config_parser = configparser.ConfigParser()
            try:
                config_parser.read_string(data)
                return True
            except configparser.Error:
                return False
        elif format == 'cfg':
            config_parser = configparser.ConfigParser()
            try:
                config_parser.read_string(data)
                return True
            except configparser.Error:
                return False