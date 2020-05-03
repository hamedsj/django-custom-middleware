from django.urls import path
from . import views
urlpatterns = [
    path('myview/', views.myview),
    path('process_view_test/', views.process_view_test)
]
