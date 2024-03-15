from django.urls import path

from . import views


urlpatterns = [
    path('home/', views.HomePageView.as_view(), name='home'),
    # path('', views.AdListView.as_view(), name='ad_list'),
    # path('<int:pk>/', views.AdDetailView.as_view(), name='ad_detail'),
]
