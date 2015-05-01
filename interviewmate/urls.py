from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),  # ADD NEW PATTERN!
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_question/$', views.add_question, name='add_question'),
    url(r'^add_category/$', views.add_category, name='add_category'),  # ADD NEW PATTERN!
]