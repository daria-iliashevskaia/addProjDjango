from django.urls import path

from ads import views
from ads.views import index, insert_categories, insert_ads

urlpatterns = [
    path('', index),
    path('cat/', views.CategoryView.as_view(), name="category"),
    path('ad/', views.AdsView.as_view(), name="ads"),
    path('cat/insert', insert_categories, name="category insert"),
    path('ad/insert', insert_ads, name="ads insert"),
    path('cat/<int:pk>', views.CategoryDetailView.as_view()),
    path('ad/<int:pk>', views.AdsDetailView.as_view()),
]
