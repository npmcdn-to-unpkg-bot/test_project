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
    result = cmdOut.splitlines()
    for idx, value in enumerate(result):
        print "result[" + str(idx) + "] = " + value
    return render(request, 'instance/index.html', { 'result' : result })