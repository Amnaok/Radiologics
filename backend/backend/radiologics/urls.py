
from django.urls import path, include
from radiologics import views
from rest_framework.routers import DefaultRouter
from .views import ContactMessageViewSet,send_email


router = DefaultRouter()
router.register(r'message', ContactMessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('getRoutes/', views.getRoutes, name="getRoutes"),
    path('send_email/', views.send_email, name="send_email"),

     path('get-csrf-token/', views.get_csrf_token, name='get-csrf-token'),
    

]