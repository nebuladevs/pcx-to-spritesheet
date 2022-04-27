from configparser import ConfigParser
from modules.constants import *

def set_merge_dcc_config(options):
    text = 'format=pcx\n'
    
    for key in options:
        text += f'{key}={options[key]}\n'
    
    with open(MERGE_DCC_CONFIG_PATH, 'w', encoding='utf-8') as f:
        f.write(text)
        
def read_config():
    config = ConfigParser()
    config.read("config.ini")
    
    return {
        "ANIMATION": config.get('CONFIG', ANIMATION),
        "ARMOR_TYPE": config.get('CONFIG', ARMOR_TYPE),
        "FULL_SPRITE": config.get('CONFIG', FULL_SPRITE),
        "BODY_PARTS": dict(config.items(BODY_PARTS))
    }