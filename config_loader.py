import json

class Config:
    def __init__(self, filepath='config.json'):
        self.filepath = filepath
        self.config = self.load_config()

    def load_config(self):
        try:
            with open(self.filepath, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading config file {self.filepath}: {e}")
            return {}

    def get_config(self, key, default=None):
        keys = key.split('.')
        value = self.config
        for k in keys:
            if k in value:
                value = value[k]
            else:
                return default
        return value

# Global config instance
config_instance = None

def load_config(filepath='config.json'):
    global config_instance
    config_instance = Config(filepath)

def get_configuration(key, default=None):
    if config_instance is None:
        load_config()
    return config_instance.get_config(key, default)
