import yaml
from enum import Enum


DEFAULT_CONFIG_FILE = 'default.yaml'
CONFIG_FILE = 'isat.yaml'

def load_config(file):
    with open(file, 'rb')as f:
        cfg = yaml.load(f.read(), Loader=yaml.FullLoader)
    return cfg

def save_config(cfg, file):
    s = yaml.dump(cfg)
    with open(file, 'w') as f:
        f.write(s)
    return True

class DRAWMode(Enum):
    VIEW = 0
    CREATE = 1
    EDIT = 2


class MAPMode(Enum):
    LABEL = 0
    SEMANTIC = 1
    INSTANCE = 2