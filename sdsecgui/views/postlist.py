#_*_coding:utf-8_*_

from django.contrib.auth.models import User
from django.shortcuts import render
from django.utils import timezone

from sdsecgui.models import Post
from sdsec.log_handler import setLogDir, getLogger

setLogDir()
logger = getLogger()


def post_list(request):
    logger.info("post_list")
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'postlist/main.html', {'posts': posts})

def write_post(request):
    logger.info("write_post")
    me = User.objects.get(username='admin')
    title = request.GET['title']
    text  = request.GET['text' ]
    post = Post.objects.create(author=me, title=title, text=text)
    post.publish()
    return render(request, 'postlist/main.html', {})