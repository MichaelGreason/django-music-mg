"""django_music URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from albums import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path('', views.list_albums, name="home"),
    path('albums/new', views.add_album, name="add_album"),
    path('albums/<int:pk>', views.detail_album, name='detail-album'),
    path('albums/<int:pk>/edit', views.edit_album, name='edit-album'),
    path('albums/<int:pk>/delete', views.delete_album, name='delete-album'),
    # where user visits, what view is called, name used within
    # the app to refer to this url/ page
]
