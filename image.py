from distutils import filelist
from PIL import Image

def generateSpriteSheet(fileList):
    width, height = Image.open(fileList[0][0]).size
    sheetWidth = len(fileList) * width
    sheetHeight = len(fileList) * height
    newImage = Image.new('RGBA', (sheetWidth, sheetHeight), (255, 255, 255, 0))
    
    for f in fileList:
        image = generateOneLineSheet(f)
        fileIndex = fileList.index(f)
        
        if (fileIndex == 0):
            newImage.paste(image, (0,0))
        else:
            newImage.paste(image, (0, height * fileIndex))
    
    newImage.show()
    newImage.save("./sheets/legs.png")
    
    

def generateOneLineSheet(fileList):
    width, height = Image.open(fileList[0]).size
    sheetWidth = len(fileList) * width
    newImage = Image.new('RGBA', (sheetWidth, height), (255, 255, 255, 0))
    
    for f in fileList:
        image = Image.open(f)
        fileIndex = fileList.index(f)
        
        if (fileIndex == 0):
            newImage.paste(image, (0,0))
        else:
            newImage.paste(image, (width * fileIndex, 0))
    
    return newImage