#_*_coding:utf-8_*_

import os
import re

from django.shortcuts import render
from sdsec import log_handler
from sdsec.log_handler import setLogDir, getLogger

#로그불러왓!
setLogDir()
logger = getLogger(level=log_handler.INFO)


def retrieveInstanceList(request):
    logger.info("instance")
    f = os.popen("nova list")
    cmdOut =  f.read().replace("+", "").replace("-", "")
    while "  " in cmdOut:
        cmdOut = cmdOut.replace("  ", " ")
    row = cmdOut.splitlines()
    while "" in row:
        row.remove("")
    colNmList = row[0][1:-1].split("|")
    instanceList = []
    for value in row[1:]:
        instanceDic = {}
        colList = value[1:-1].split("|")
        for idx, col in enumerate(colList):
            key = colNmList[idx].lower().strip().replace(" ", "_")
            value = col.strip()
            instanceDic[key] = value
        instanceList.append(instanceDic)
    print instanceList
    return render(request, 'instance/index.html', { 'instanceList' : instanceList })