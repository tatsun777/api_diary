from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from api.views import DiaryViewSet, CreateUserView, MyProfileView

router = routers.DefaultRouter()
router.register('diary', DiaryViewSet ,basename='diary')

urlpatterns = [
    path('myself/', MyProfileView.as_view(), name='myself'),
    path('register/', CreateUserView.as_view(), name='register'),
    path('', include(router.urls))
]