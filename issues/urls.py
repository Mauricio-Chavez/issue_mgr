from django.urls import path
from . import views

urlpatterns = [
    path('board/', views.IssueCreateView.as_view(), name='board'),
]
