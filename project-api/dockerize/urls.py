from django.urls import path
from .views import DockerizeList, DockerizeDetail

urlpatterns = [
  path('', DockerizeList.as_view(), name='dockerize_list'),
  path('<int:pk>/', DockerizeDetail.as_view(), name='dockerize_detail'),
]