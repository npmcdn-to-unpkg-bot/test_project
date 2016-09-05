#_*_coding:utf-8_*_

import os

from django.contrib.auth.models import User
from django.shortcuts import render
from django.utils import timezone

from sdsecgui.models import Post
from sdsec import log_handler
from sdsec.log_handler import setLogDir, getLogger

#로그불러왓!
setLogDir()
logger = getLogger(level=log_handler.INFO)


def new_page(request):
    logger.info("test")
    return render(request, 'test/main.html', {})

def retrieveUsage(request):

    start = request.start
    end = request.end
    f = os.popen("openstack useage list --start " + start + " --end " + end)
    str =  f.read()