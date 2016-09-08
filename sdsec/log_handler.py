#_*_coding:utf-8_*_
import logging
import logging.handlers
import os
from os.path import join, exists
from time import localtime

DEBUG = logging.DEBUG
INFO = logging.INFO
WARN = logging.WARN
ERROR = logging.ERROR
CRITICAL = logging.CRITICAL



UTF_8='utf-8'
def setLogDir(directory=r"static/logs"):
    directory = directory
    now = localtime()
    s = "log_%02d%02d%02d.log" % (
        now.tm_year, now.tm_mon, now.tm_mday)#, now.tm_hour, now.tm_min, now.tm_sec
    global fileName

    if not exists(directory.decode(UTF_8)):
        os.mkdir(directory.decode(UTF_8))

    fileName = join(directory, s)


def getLogger(loggerName='myLogger', level=DEBUG):
    # 로거 인스턴스를 만든다
    logger = logging.getLogger(loggerName)

    # 포매터를 만든다
    fomatter = logging.Formatter('[%(levelname)s|%(filename)s:%(lineno)s] %(asctime)s > %(message)s')

    # 스트림과 파일로 로그를 출력하는 핸들러를 각각 만든다.
    filename = fileName.decode(UTF_8)
    fileHandler = logging.FileHandler(filename)
    streamHandler = logging.StreamHandler()

    # 각 핸들러에 포매터를 지정한다.
    fileHandler.setFormatter(fomatter)
    streamHandler.setFormatter(fomatter)

    # 로거 인스턴스에 스트림 핸들러와 파일핸들러를 붙인다.
    logger.addHandler(fileHandler)
    logger.addHandler(streamHandler)

    # 로거 인스턴스로 로그를 찍는다.
    logger.setLevel(level)

    # logger.info(message)
    return logger