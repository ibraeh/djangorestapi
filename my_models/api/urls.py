from django.urls import path

from my_models.api.views import api_detail_view
app_name='my_models'

urlpatterns=[
	path('<slug:name>/', api_detail_view, name='details'),
] 