from django.urls import path,include

from rest_framework.routers import DefaultRouter
from profiles_api import views
router=DefaultRouter()
router.register('hello-viewset',views.HelloViewSet, base_name='hello-viewset')
router.register('Profile',views.UserProfileViewSet)

urlpatterns=[


     path('helo/',views.HelloApiView.as_view()),
     path('',include(router.urls))

 ]
