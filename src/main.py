from modules.config import read_config
from modules.commands import generate_pcx

configs = read_config()
generate_pcx(configs)