from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from my_models.api3.views import AuthorList, AuthorDetail, AuthorGenericList, AuthorGenericDetail




app_name='my_models'

urlpatterns=[
	path('authorlistclass/', AuthorList.as_view()),
	path('authordetailclass/<int:pk>/', AuthorDetail.as_view()),
	path('authorgenericlist/', AuthorGenericList.as_view()),
	path('authorgenericdetail/<int:pk>/', AuthorGenericDetail.as_view() ), 
	

]

urlpatterns=format_suffix_patterns(urlpatterns)