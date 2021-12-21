# from django.urls import path
# from django.urls.resolvers import URLPattern
from django.urls import path
from .views import (
    PersonListView, 
    PersonDetailView,
    PersonCreateView,
    PersonUpdateView,
    PersonDeleteView
)

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', PersonListView.as_view(), name='index'),
    path('<int:pk>/', PersonDetailView.as_view(), name='detail'),
    path('create/', PersonCreateView.as_view(), name='create'),
    path('<int:pk>/update/', PersonUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', PersonDeleteView.as_view(), name='delete'),
    path('about/', views.about, name='about')
]