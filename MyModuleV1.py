import os
import chardet


def walkFiles(dirPath, fileExts):
    filePathList = []
    for dirPath, _, fileNames in os.walk(dirPath):
        for fileName in fileNames:
            for fileExt in fileExts:
                if fileName.lower().endswith(fileExt.lower()):
                    filePathList.append(os.path.join(dirPath, fileName))
                    break
    return filePathList


def detectFileEncoding(filePath):
    with open(filePath, "rb") as fp:
        fileEncoding = chardet.detect(fp.read())["encoding"]
    return fileEncoding
