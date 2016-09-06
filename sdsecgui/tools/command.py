#_*_coding:utf-8_*_

import os

from sdsec import log_handler
from sdsec.log_handler import setLogDir, getLogger

#로그불러왓!
setLogDir()
logger = getLogger(level=log_handler.INFO)


def getInstanceList():
    logger.debug("getInstanceList")
    f = os.popen("nova list")
    logger.debug(f.read())
    cmdOut = f.read().replace("+", "").replace("-", "")
    while "  " in cmdOut:
        cmdOut = cmdOut.replace("  ", " ")
    row = cmdOut.splitlines()
    colNmList = row[1][1:-1].split("|")
    instanceList = []
    for value in row[3:-1]:
        instanceDic = {}
        colList = value[1:-1].split("|")
        for idx, col in enumerate(colList):
            key = colNmList[idx].lower().strip().replace(" ", "_")
            value = col.strip()
            instanceDic[key] = value
        instanceList.append(instanceDic)
    return instanceList
