import os
import chardet


def walkFiles(dir_path, file_exts):
    filePathList = []
    for dirPath, _, fileNames in os.walk(dir_path):
        for fileName in fileNames:
            for fileExt in file_exts:
                if fileName.lower().endswith(fileExt.lower()):
                    filePathList.append(os.path.join(dirPath, fileName))
                    break
    return filePathList


def detectFileEncoding(filePath):
    with open(filePath, "rb") as fp:
        fileEncoding = chardet.detect(fp.read())["encoding"]
    return fileEncoding
