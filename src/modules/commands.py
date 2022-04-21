import os
from enums.body import *
from modules.constants import *
from modules.constants import *
from modules.config import set_merge_dcc_config
from modules.folder import getPCXFiles, removeFiles
from modules.image import generateSpriteSheet
from modules.utils import chunkArray

def generate_pcx():    
    bodyParts = [Body.HEAD, Body.LEFT_ARM, Body.LEGS, Body.RIGHT_ARM, Body.TORSO]
    
    for part in bodyParts:
        options = { "cof": "SOTN1HT", f"{part.value}": "LIT" }
        
        set_merge_dcc_config(options)
        os.system(GENERATE_PCX_COMMAND)
        
        splitedFiles = chunkArray(getPCXFiles(MERGE_DCC_PATH), SPRITES_PER_ROW)
        generateSpriteSheet(splitedFiles, part.value)
        removeFiles(getPCXFiles(MERGE_DCC_PATH))