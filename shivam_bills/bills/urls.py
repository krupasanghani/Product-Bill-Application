from django.urls import path

from . import views

urlpatterns = [
    path('downaload_sheet/<int:object_id>/', views.downaload_sheet, name='pdf_generate'),
    path('download_bills/<int:object_id>/', views.download_bills, name='download_bills')
]