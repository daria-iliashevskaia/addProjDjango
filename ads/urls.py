from django.conf.urls.static import static
from django.urls import path

from addProj import settings
from ads import views
from ads.views import index

urlpatterns = [
    path('', index),
    path('cat/', views.CategoryView.as_view(), name="category"),
    path('ad/', views.AdsView.as_view(), name="ads"),
    path('cat/<int:pk>', views.CategoryDetailView.as_view()),
    path('ad/<int:pk>', views.AdsDetailView.as_view()),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
