from django.urls import include, path
from rest_framework import routers
from api import views


router = routers.DefaultRouter()
router.register(r'anfragen', views.AnfrageViewSet)
router.register(r'unternehmen', views.UnternehmenViewSet)
router.register(r'ober_kategorien', views.OberKategorienViewSet)
router.register(r'unter_kategorien', views.UnterKategorienViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('confirm/<int:id>/', views.confirm_purchase, name="confirm"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
