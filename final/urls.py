from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^interviewmate/', include('interviewmate.urls', namespace="interviewmate")),
    url(r'^admin/', include(admin.site.urls)),
]
