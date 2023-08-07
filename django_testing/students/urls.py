
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CoursesViewSet

app_name = 'students'
router = DefaultRouter()
router.register("courses", CoursesViewSet, basename="courses")

urlpatterns = router.urls
