import debug_toolbar
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('task/', include('todolist_app.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
]
