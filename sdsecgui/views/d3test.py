#_*_coding:utf-8_*_

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone

from sdsecgui.models import Post
from sdsec import log_handler
from sdsec.log_handler import setLogDir, getLogger

setLogDir()
logger = getLogger(level=log_handler.INFO)

def page(request, page_name):
    return render(request, 'd3test/' + page_name + '.html', {})