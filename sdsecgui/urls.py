#_*_coding:utf-8_*_
from django.conf.urls import url

from views import postlist, test, d3test, instance

urlpatterns = [
    url(r'^$', postlist.post_list, name='post_list'),
    url(r'^add_post/$', postlist.write_post, name='write_post'),
    url(r'^new_page/$', test.new_page, name='new_page'),
    url(r'^d3test/(?P<page_name>\w+)/$', d3test.page, name='page'),
    url(r'^instance/$', instance.retrieveInstanceList, name='instance')
]