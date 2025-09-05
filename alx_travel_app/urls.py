from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from listings.views import BookingViewSet

router = routers.DefaultRouter()
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
