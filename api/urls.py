from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from api.views import UserViewSet, MigrateView, CreateSuperuserView

router = DefaultRouter(trailing_slash=False)
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'migrate', MigrateView.as_view()),
    url(r'createsuperuser', CreateSuperuserView.as_view()),
]
