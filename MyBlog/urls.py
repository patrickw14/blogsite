from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'blog.views.home', name='home'),
    url(r'^about/$', 'blog.views.about'),
    url(r'^contact/$', 'blog.views.contact'),
    url(r'^page/(?P<page_number>\d+)/$', 'blog.views.viewBlogPosts'),
    url(r'^newpost/$', 'blog.views.writeNewPost', name='newpost'),
    url(r'^viewpost/(?P<blog_id>\d+)/$', 'blog.views.viewpost'),
    url(r'^edit/(?P<blog_id>\d+)/$', 'blog.views.editpost'),
    url(r'^login/$', 'log.views.login'),
    url(r'^logout/$', 'log.views.logout'),

    url(r'^search/$', 'search.views.search'),
    # url(r'^MyBlog/', include('MyBlog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

from MyBlog import settings
if settings.DEBUG:
    urlpatterns += patterns('',
                     (r'^mymedia/(?P<path>.*)$',
                      'django.views.static.serve',
                      {'document_root':
                           settings.MEDIA_ROOT}),
                     )
