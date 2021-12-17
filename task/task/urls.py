import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from todolist_app import views as views_todolist_app
#from users_app import views as views_users_app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('task/', include('todolist_app.urls')),
    path('account/', include('users_app.urls')),
    path('', views_todolist_app.index, name = 'index'),
    path('__debug__/', include(debug_toolbar.urls)),
    path('contact', views_todolist_app.contact, name = 'contact'),
    path('about', views_todolist_app.about, name = 'about'),

]
