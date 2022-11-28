from django.conf.urls.static import static
from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from addProj import settings
from ads import views
from ads.views import index, LocationViewSet

router = routers.SimpleRouter()
router.register('location', LocationViewSet)

urlpatterns = [
    path('', index),
    path('cat/', views.CategoryListView.as_view(), name="category"),
    path('ad/', views.AdsListView.as_view(), name="ads"),
    path('user/', views.UserListView.as_view(), name="user"),
    path('selections/', views.SelectionsListView.as_view()),

    path('cat/<int:pk>/', views.CategoryDetailView.as_view()),
    path('ad/<int:pk>/', views.AdsDetailView.as_view()),
    path('user/<int:pk>/', views.UserDetailView.as_view()),
    path('selections/<int:pk>/', views.SelectionsDetailView.as_view()),

    path('cat/create/', views.CategoryCreateView.as_view()),
    path('ad/create/', views.AdsCreateView.as_view()),
    path('user/create/', views.UserCreateView.as_view()),
    path('selections/create/', views.SelectionsCreateView.as_view()),

    path('cat/<int:pk>/update/', views.CategoryUpdateView.as_view()),
    path('ad/<int:pk>/update/', views.AdsUpdateView.as_view()),
    path('user/<int:pk>/update/', views.UserUpdateView.as_view()),
    path('selections/<int:pk>/update/', views.SelectionsUpdateView.as_view()),

    path('cat/<int:pk>/delete/', views.CategoryDeleteView.as_view()),
    path('ad/<int:pk>/delete/', views.AdsDeleteView.as_view()),
    path('user/<int:pk>/delete/', views.UserDeleteView.as_view()),
    path('selections/<int:pk>/delete/', views.SelectionsDeleteView.as_view()),

    path('user/token/', TokenObtainPairView.as_view()),
    path('user/token/refresh/', TokenRefreshView.as_view()),
]

urlpatterns += router.urls
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
