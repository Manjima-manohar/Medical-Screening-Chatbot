from django.urls import path
from .views import MedicalScreeningAPIView

urlpatterns = [
    path(
        "screening/",
        MedicalScreeningAPIView.as_view(),
        name="medical-screening"
    ),
]