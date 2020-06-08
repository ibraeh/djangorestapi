from django.urls import path ,include
from rest_framework.urlpatterns import format_suffix_patterns
from my_models.api4.views import AuthorViewSet, BookViewSet , PublisherViewSet
from rest_framework import routers


app_name='my_models'
router=routers.DefaultRouter()
router.register('author', AuthorViewSet)
router.register('publisher', PublisherViewSet)
router.register('book', BookViewSet)


urlpatterns=[

	path('hyper/', include(router.urls)),
]