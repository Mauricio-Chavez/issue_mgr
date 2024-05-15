from django.urls import path
from . import views

urlpatterns = [
    path('board/', views.BoardView.as_view(), name='board'),
    path('new/', views.IssueCreateView.as_view(), name='new'),
    path('<int:pk>/update/', views.StatusUpdateView.as_view(), name='update_status'),
]
