from django.urls import path
from .views import StationCreateView, StationListView, StationDetailView, StationUpdateView, StationDeleteView

urlpatterns = [ 
    path('new/', StationCreateView.as_view(), name='station-new'),
    path('list/', StationListView.as_view(), name='station-list'),
    path('<int:pk>/', StationDetailView.as_view(), name='station-detail'),
    path('<int:pk>/update', StationUpdateView.as_view(), name='station-update'),
    path('<int:pk>/delete', StationDeleteView.as_view(), name='station-delete')
]