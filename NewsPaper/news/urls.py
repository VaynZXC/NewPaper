from django.urls import path
from .views import ProductsList, ProductDetail
from views import PostDetail, PostsList
 
 
urlpatterns = [
    path('', PostsList.as_view()),
    path('<int:pk>', PostDetail.as_view()),
]