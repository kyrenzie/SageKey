from django.conf.urls import url, include
from django.contrib import admin
from todolist.views import index, logout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name="TodoList"),
    url(r'^accounts/', include('django.contrib.auth.urls')),
]
