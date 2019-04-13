from django.urls import path

from api import views

urlpatterns = [
  path('patients/', views.PatientListView.as_view({'get': 'list'}), name = 'get_patients'),
  path('patients/<int:pk>', views.PatientListView.as_view({'get': 'retrieve'}), name = 'get_patient')
]