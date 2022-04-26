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
        "animation": config.get('CONFIG', 'animation'),
        "armor_type": config.get('CONFIG', 'armor_type')
    }