from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from my_models.api2 import views

app_name='my_models'
urlpatterns=[
	path('authorpage/',views.author_list, name='list-author'),
	path('authordetail/<int:pk>',views.author_detail, name='detail-author')

]

urlpatterns=format_suffix_patterns(urlpatterns)