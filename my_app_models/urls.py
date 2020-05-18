"""my_app_models URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from my_models import views #importing function view
from my_models.views import PublisherListView, cookie_session, cookie_delete, access_session

urlpatterns = [
    path('admin/', admin.site.urls),
    path('display/',views.display, name='display'),
    path('publisher/',PublisherListView.as_view()),
    path('testcookie/', cookie_session),
    path('deletecookie/',cookie_delete),
    path('createsession/', views.create_session, name='create'),
    path('accesssession/',access_session),
	path('upload/',include('my_models.urls')),
]