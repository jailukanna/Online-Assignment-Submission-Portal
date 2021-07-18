"""Assignment_Submission URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from . import settings
from django.urls import path, include
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Django admin customize
admin.site.site_header = "Online Assignment Submission Portal"
admin.site.site_title = "Welcome Admin "
admin.site.index_title = "Welcome to Online Assignment Submission Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Home.urls')),
    path('Student/', include('Student.urls')),
    path('Admin/', include('Admin.urls')),
    path('Teacher/', include('Teacher.urls')),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
