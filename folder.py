import os

path = './original/'

def readFiles():
    files = os.listdir(path)
    filePaths = []
    
    for f in files:
        filePaths.append(path+f)
    
    return filePaths