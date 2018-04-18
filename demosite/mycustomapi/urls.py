from django.urls import include
from django.conf.urls import url
from django.contrib import admin

from mycustomapi.app import application as api
from oscar.app import application as oscar

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', api.urls),
    url(r'', oscar.urls),

]
