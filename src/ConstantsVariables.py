import os

import wx
from PIL import Image


class C():
    # ------OTHER------
    T_MAIN_FRAME = "图片批量处理GUI版 - Ver 2.01"
    PATH_SUFFIX = "[NEW]"
    ST_FRAME = wx.CAPTION | wx.SYSTEM_MENU | wx.CLOSE_BOX | wx.MINIMIZE_BOX
    B_DEFAULT = 5
    # ------OTHER------

    # ------SIZE------
    SI_MAIN_FRAME = (550, 690)
    SI_DEFAULT = (-1, 25)
    SI_MAX = (9999, 25)
    # ------SIZE------

    # ------LABEL------
    LST_INPUT = "输入文件(夹):"
    LST_OUTPUT = "输出文件(夹):"
    LST_MULTIPLE = "缩小倍数:"
    LST_PROCESS = "进程数:"
    LRB_WEBP = "WEBP"
    LRB_PNG = "PNG"
    LRB_JPEG = "JPEG"
    LCB_W_LOSSLESS = "lossless"
    LCB_P_OPTIMIZE = "optimize"
    LCB_J_OPTIMIZE = "optimize"
    LCB_J_PROGRESSIVE = "progressive"
    LB_CLEAR = "清除输出"
    LB_HELP = "帮助信息"
    LB_START = "开始转换"
    # ------LABEL------

    # ------HINT------
    HTC_INPUT = "请拖入输入文件(夹)."
    HTC_OUTPUT = "输出文件(夹)将自动生成."
    # ------HINT------

    # ------INIT SET------
    # SET
    IVTC_MULTIPLE = "1.2"
    IVTC_PROCESS = str(os.cpu_count())
    ISC_FILTERS = 6 - 1
    ISC_MODES = 1 - 1
    # WEBP
    IVRB_WEBP = True
    IVCB_W_LOSSLESS = False
    ISC_W_QUALITY = 90 - 1
    ISC_W_METHOD = 6 - 1
    # PNG
    IVRB_PNG = False
    IVCB_P_OPTIMIZE = True
    # JPG
    IVRB_JPG = False
    IVCB_J_OPTIMIZE = True
    ISC_J_QUALITY = 90 - 1
    IVCB_J_PROGRESSIVE = True
    # ------INIT SET------

    # ------CHOICES------
    CC_W_QUALITY = ["输出质量: " + str(x) for x in range(1, 100 + 1)]
    CC_W_METHOD = ["质量/速度: " + str(x) for x in range(1, 6 + 1)]
    CC_J_QUALITY = ["输出质量: " + str(x) for x in range(1, 100 + 1)]
    # ------CHOICES------

    # ------FILTERS------
    FILTERS = {
        "过滤器: NEAREST": Image.NEAREST,
        "过滤器: BOX": Image.BOX,
        "过滤器: BILINEAR": Image.BILINEAR,
        "过滤器: HAMMING": Image.HAMMING,
        "过滤器: BICUBIC": Image.BICUBIC,
        "过滤器: LANCZOS": Image.LANCZOS}
    # ------FILTERS------

    # ------MODES------
    MODES = {
        "模式: 不转换": None,
        "模式: 1": "1",
        "模式: L": "L",
        "模式: P": "P",
        "模式: RGB": "RGB",
        "模式: RGBA": "RGBA",
        "模式: CMYK": "CMYK",
        "模式: YCbCr": "YCbCr",
        "模式: LAB": "LAB",
        "模式: HSV": "HSV",
        "模式: I": "I",
        "模式: F": "F",
        "模式: LA": "LA",
        "模式: PA": "PA",
        "模式: RGBX": "RGBX",
        "模式: RGBa": "RGBa",
        "模式: La": "La",
        "模式: I;16": "I;16",
        "模式: I;16L": "I;16L",
        "模式: I;16B": "I;16B",
        "模式: I;16N": "I;16N",
        "模式: BGR;15": "BGR;15",
        "模式: BGR;16": "BGR;16",
        "模式: BGR;24": "BGR;24",
        "模式: BGR;32": "BGR;32"}
    # ------MODES------

    # ------LOG------
    L_DIVIDING_LINE = "------------------------------------------------------------------------------\n"
    L_IMAGE_OLD_INFO = "  图片转换前:\n"
    L_IMAGE_NEW_INFO = "  图片转换后:\n"
    L_IMAGE_INFO_FORMAT = "    图片格式:  "
    L_IMAGE_INFO_MODE = "    图片模式:  "
    L_IMAGE_INFO_SIZE = "    图片大小:  "
    L_IMAGE_INFO_INFO = "    其他信息:  "
    L_IMAGE_CONVERSION_SUCCEEDED = "图片转换成功!\n"
    L_IMAGE_CONVERSION_FINISHED = "图片转换完成!\n"
    # ------LOG------

    # ------WARNING------
    W_HEAD = "警告: "
    W_OUTPUT_PATH_ALREADY_EXISTS = W_HEAD + "输出路径已存在文件夹(夹)!\n"
    # ------WARNING------

    # ------ERROR------
    E_HEAD = "错误:  "
    E_INPUT_PATH_MULTIPLE = E_HEAD + "只允许拖入一个文件(夹)!\n"
    E_INPUT_PATH_NOT_EXIST = E_HEAD + "输入路径不存在文件(夹)!\n"
    E_UNKNOWEN = E_HEAD + "未知错误:  "
    E_IMAGE_CONVERSION_FAILED = "  图片转换失败:  "
    # ------ERROR------

    # ------FORMATS------
    FORMATS = ["BMP", "ICO", "JPEG", "JPG", "PNG", "TIFF", "WEBP", "PSD"]
    FORMATS_RAW = ["BMP", "EPS", "GIF", "ICNS", "ICO", "IM", "JPEG", "JPG", "MSP", "PCX", "PNG", "PPM", "SGI", "TGA", "TIFF", "WebP", "XBM", "BLP", "CUR", "DCX", "DDS", "FLI",
                   "FPX", "FTEX", "GBR", "GD", "IMT", "IPTC", "MCIDAS", "MIC", "MPO", "PCD", "PIXAR", "PSD", "WAL", "XPM", "PALM", "PDF", "BUFR", "FITS", "GRIB", "HDF5", "MPEG", "WMF"]
    # ------FORMATS------
