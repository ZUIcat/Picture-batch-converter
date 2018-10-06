import os
from multiprocessing import Pool, Queue

from PIL import Image

from ConstantsVariables import C
from LogTextCtrl import LogTextCtrl as L
from MyModuleV1 import walkFiles

# ------global variables------ #
g_logTextCtrl = None
g_queue = None
# ------global variables------ #


# ------init method------ #
def init(logTextCtrl):
    global g_logTextCtrl
    g_logTextCtrl = logTextCtrl
    Image.MAX_IMAGE_PIXELS = None
# ------init method------ #


# ------get queue------ #
def getQueue(queue):
    global g_queue
    g_queue = queue
# ------get queue------ #


# ------get image information------ #
def getImageInfo(imagePath, isOld):
    global g_queue
    if isOld:
        info = C.L_DIVIDING_LINE + \
            os.path.basename(imagePath) + C.L_IMAGE_OLD_INFO
    else:
        info = os.path.basename(imagePath) + C.L_IMAGE_NEW_INFO
    try:
        with Image.open(imagePath) as image:
            info += C.L_IMAGE_INFO_FORMAT + str(image.format) + "\n"
            info += C.L_IMAGE_INFO_MODE + str(image.mode) + "\n"
            info += C.L_IMAGE_INFO_SIZE + str(image.size) + "\n"
            info += C.L_IMAGE_INFO_INFO + str(image.info) + "\n"
        return L.ID_LOG + info
    except Exception as e:
        return L.ID_ERROR + C.E_UNKNOWEN + repr(e) + "\n"
# ------get image information------ #


# ------convert image------ #
def convertImage(imageFormat, oldFilePath, newFilePath, multiple, filters, toRGB, **kwargs):
    global g_logTextCtrl
    try:
        if not os.path.isdir(os.path.dirname(newFilePath)):
            os.makedirs(os.path.dirname(newFilePath))
        with Image.open(oldFilePath) as image:
            if toRGB:
                image = image.convert("RGB")
            image.thumbnail(
                (image.width//multiple, image.height//multiple),
                filters
            )
            image.save(newFilePath, format=imageFormat, **kwargs)
        g_logTextCtrl.AppendLogAuto(
            getImageInfo(oldFilePath, True),
            getImageInfo(newFilePath, False)
        )
    except Exception as e:
        g_logTextCtrl.AppendError(C.E_UNKNOWEN + repr(e) + "\n")
    else:
        g_logTextCtrl.AppendLog(C.L_IMAGE_CONVERSION_SUCCEEDED)
# ------convert image------ #


# ------_convert image------ #
# Program private method.
# Do not call this method.
def _convertImage(imageFormat, oldFilePath, newFilePath, multiple, filters, toRGB, **kwargs):
    global g_queue
    try:
        if not os.path.isdir(os.path.dirname(newFilePath)):
            os.makedirs(os.path.dirname(newFilePath))
        with Image.open(oldFilePath) as image:
            if toRGB:
                image = image.convert("RGB")
            image.thumbnail(
                (image.width//multiple, image.height//multiple),
                filters
            )
            image.save(newFilePath, format=imageFormat, **kwargs)
        g_queue.put(
            (getImageInfo(oldFilePath, True),
             getImageInfo(newFilePath, False))
        )
    except Exception as e:
        g_queue.put(
            L.ID_ERROR + C.E_UNKNOWEN + oldFilePath +
            C.E_IMAGE_CONVERSION_FAILED + repr(e) + "\n"
        )
# ------_convert image------ #


# ------convert images------ #
def convertImages(imageFormat, oldDirPath, newDirPath, multiple, filters, toRGB, processNum, **kwargs):
    global g_logTextCtrl
    global g_queue
    oldDirPath = os.path.abspath(oldDirPath)
    newDirPath = os.path.abspath(newDirPath)
    try:
        queue = Queue()
        pool = Pool(processNum, getQueue, (queue,))
        oldFilePathList = walkFiles(oldDirPath, C.FORMATS)
        for oldFilePath in oldFilePathList:
            newFilePath = os.path.splitext(
                oldFilePath.replace(oldDirPath, newDirPath)
            )[0] + "." + imageFormat.lower()
            pool.apply_async(
                _convertImage,
                (imageFormat, oldFilePath, newFilePath, multiple, filters, toRGB),
                kwargs
            )
        pool.close()
        for _, __ in enumerate(oldFilePathList):
            result = queue.get()
            g_logTextCtrl.AppendLogAuto(result)
    except Exception as e:
        g_logTextCtrl.AppendError(C.E_UNKNOWEN + repr(e) + "\n")
    else:
        g_logTextCtrl.AppendLog(C.L_IMAGE_CONVERSION_FINISHED)
# ------convert images------ #
