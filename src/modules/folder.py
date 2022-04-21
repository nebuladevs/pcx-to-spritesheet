import os


def readFiles():
    path = './original/'
    files = os.listdir(path)
    filePaths = []
    
    for f in files:
        filePaths.append(path+f)
    
    return filePaths

def getPCXFiles(path):
    pcxFiles = []
    
    for file in os.listdir(path):
        if file.endswith(".PCX"):
            pcxFiles.append(os.path.join(path, file))
    
    return pcxFiles

def removeFiles(files):
    for f in files:
        os.remove(f)