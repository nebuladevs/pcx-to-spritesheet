import os
from enums.body import *
from modules.constants import *
from modules.constants import *
from modules.config import set_merge_dcc_config
from modules.folder import getPCXFiles, removeFiles
from modules.image import generateSpriteSheet
from modules.utils import chunkArray, str_to_bool

def generate_pcx(configs):    
    isFullSprite = str_to_bool(configs[FULL_SPRITE])
    
    if (isFullSprite):
        return generate_full_sprite(configs)
    
    return generate_parts(configs)

def generate_parts(configs):
    for part in BODY_PARTS_LIST:
        options = { "cof": configs[ANIMATION], f"{part.value}": configs[ARMOR_TYPE] }
        
        set_merge_dcc_config(options)
        os.system(GENERATE_PCX_COMMAND)
        
        splitedFiles = chunkArray(getPCXFiles(MERGE_DCC_PATH), SPRITES_PER_ROW)
        generateSpriteSheet(splitedFiles, part.value)
        removeFiles(getPCXFiles(MERGE_DCC_PATH))

def generate_full_sprite(configs):
    options = { "cof": configs[ANIMATION] }
        
    for part in configs[BODY_PARTS]:
        if (configs[BODY_PARTS][part] != ""):
            options[part] = configs[BODY_PARTS][part]
    
    set_merge_dcc_config(options)
    os.system(GENERATE_PCX_COMMAND)
    
    splitedFiles = chunkArray(getPCXFiles(MERGE_DCC_PATH), SPRITES_PER_ROW)
    generateSpriteSheet(splitedFiles, FULL_SPRITE)
    removeFiles(getPCXFiles(MERGE_DCC_PATH))