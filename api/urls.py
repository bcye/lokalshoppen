from django.urls import path
from api import views


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('confirm/<int:id>/', views.confirm_purchase, name="confirm"),
]
