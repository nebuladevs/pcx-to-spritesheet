from folder import readFiles
from utils import chunkArray
from pprint import pprint
import image

bodyParts = chunkArray(readFiles(), 16)

image.generateSpriteSheet(bodyParts)