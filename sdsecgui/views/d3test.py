#_*_coding:utf-8_*_

from django.shortcuts import render

from sdsec.log_handler import setLogDir, getLogger

setLogDir()
logger = getLogger()

def page(request, page_name):
    return render(request, 'd3test/' + page_name + '.html', {})