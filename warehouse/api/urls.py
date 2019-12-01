

from django.urls import path, re_path
from api.views import TrasactionView, ProductView, CategoryView
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'categories', CategoryView)

urlpatterns = [
path("transactions/",TrasactionView.as_view()),
re_path("transactions/(?P<pk>[0-9]+)",TrasactionView.as_view()),
path("products/",ProductView.as_view()),

    
]
urlpatterns = urlpatterns+router.urls
