from django.urls import path
from . import views

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('api/predict/', views.PredictAPIView.as_view(), name='api-predict'),
    path('upload-csv/', views.CSVUploadView.as_view(), name='upload-csv'),
]
